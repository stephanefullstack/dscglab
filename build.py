"""Build the static site from the UE 4 training material.

Usage (from ue4/… or anywhere): python3 -I build.py
Reads ../ue4/exercices and ../ue4/sujets, copies their Markdown into content/,
converts it with pandoc and writes the site into docs/ (served by GitHub Pages).
"""
from __future__ import annotations

import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UE4 = HERE.parent / "ue4"
CONTENT = HERE / "content"
DOCS = HERE / "docs"

# id, source folder, dossier number, dossier title, case, points, duration
EXERCISES = [
    ("ex03", "ex03_consolidation", 1, "Comptes de groupe", "Groupe ARGOS, règlement ANC 2020‑01", 45, "1 h 45"),
    ("ex05", "ex05_consolidation_ifrs", 1, "Comptes de groupe", "Groupe NORDAL, normes IFRS", 45, "1 h 45"),
    ("ex01", "ex01_restructurations", 2, "Opérations de restructuration", "Absorption d'ORION par HÉLIOS", 25, "1 h"),
    ("ex02", "ex02_apport_partiel", 2, "Opérations de restructuration", "Apport partiel d'actif d'ATLAS à BORÉE", 25, "1 h"),
    ("ex04", "ex04_audit_durabilite", 3, "Audit", "NORDALIS, entité d'intérêt public", 30, "1 h 15"),
    ("ex06", "ex06_audit_durabilite", 3, "Audit", "LUMIVERT et OPTIBOX, hors entité d'intérêt public", 30, "1 h 15"),
]
SUBJECTS = [
    ("sujet-1", "sujet_complet_01", 1, ["ex03", "ex01", "ex04"]),
    ("sujet-2", "sujet_complet_02", 2, ["ex03", "ex02", "ex04"]),
    ("sujet-3", "sujet_complet_03", 3, ["ex05", "ex02", "ex06"]),
]
EX = {e[0]: e for e in EXERCISES}

# Sentences that only make sense inside the working folder (tool, data files).
INTERNAL = [
    (r" ?Données structurées et écritures : `corrige\.yaml`, vérifié par `outils/ue4check` \([^)]*\)\.", ""),
    (r"Les écritures complètes sont dans `corrige\.yaml`\. ", ""),
    (r"Les écritures complètes \(comptes, intitulés, montants\) figurent dans `corrige\.yaml` \(R1 à R6\)\. "
     r"Toutes sont équilibrées \(contrôle `ue4check`\)\. Schémas types : [^\n]*\.", "Toutes les écritures ci-dessous sont équilibrées."),
    (r"Écritures complètes dans `corrige\.yaml` \(B1, B2\), toutes équilibrées\. Schéma type : [^\n]*\.",
     "Les écritures B1 et B2 ci-dessous sont équilibrées."),
    (r" ?Le barème et l'absence de références périmées ou hors programme sont vérifiés par `outils/ue4check` \(`corrige\.yaml`\)\.", ""),
    (r"<!-- ue4check:ignorer -->", ""),
]


def clean(md: str, depth: int) -> str:
    """Strip the title lines and the working-folder references; link the exercise paths."""
    lines = md.split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
        if lines and lines[0].startswith("## "):
            lines = lines[1:]
    md = "\n".join(lines)
    for pattern, repl in INTERNAL:
        md = re.sub(pattern, repl, md)
    root = "../" * depth
    md = re.sub(r"`exercices/(ex\d\d)_[a-z_]+`",
                lambda m: f"[{EX[m.group(1)][4]}]({root}exercices/{m.group(1)}/sujet.html)", md)
    left = [w for w in ("corrige.yaml", "ue4check", "gabarits/") if w in md]
    if left:
        print("ATTENTION, références internes restantes :", left, file=sys.stderr)
    return md


def pandoc(md: str) -> str:
    return subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"],
                          input=md, capture_output=True, text=True, check=True).stdout


def page(*, title: str, depth: int, margin: str, body: str, kind: str = "") -> str:
    root = "../" * depth
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="Entraînement à l'UE 4 du DSCG, comptabilité et audit, session 2027 : sujets et corrigés.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23fbfbf9'/%3E%3Cpath d='M8 0v32' stroke='%23c8475d' stroke-width='2'/%3E%3Cpath d='M0 11h32M0 19h32M0 27h32' stroke='%23a9c4e0'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}style.css">
</head>
<body class="{kind}">
<div class="copie">
<aside class="marge">
<a class="sigle" href="{root}index.html"><span>DSCG</span><span>UE 4</span></a>
{margin}
</aside>
<main>
{body}
</main>
</div>
<footer>
<p>Supports d'entraînement non officiels, sans lien avec le ministère ni avec les organisateurs de l'examen. Réglementation applicable au 31 décembre 2026. Les corrigés ont été contrôlés par un outil de vérification automatique ; ils peuvent néanmoins comporter des erreurs.</p>
</footer>
</body>
</html>
"""


def margin_block(items: list[str], links: list[tuple[str, str]], current: str = "") -> str:
    out = "".join(f"<p>{html.escape(i)}</p>" for i in items)
    if links:
        out += "<nav>" + "".join(
            f'<a href="{href}"{chr(32) + "aria-current=" + chr(34) + "page" + chr(34) if href == current else ""}>{html.escape(label)}</a>'
            for label, href in links) + "</nav>"
    return out


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build_exercise(e) -> None:
    eid, src, dossier, dtitle, case, pts, dur = e
    (CONTENT / eid).mkdir(parents=True, exist_ok=True)
    for name in ("sujet.md", "corrige.md"):
        shutil.copy(UE4 / "exercices" / src / name, CONTENT / eid / name)
    sujet_md = clean((CONTENT / eid / "sujet.md").read_text(encoding="utf-8"), 2)
    corr_md = clean((CONTENT / eid / "corrige.md").read_text(encoding="utf-8"), 2)
    items = [f"Dossier {dossier}", f"{pts} points", dur]
    links = [("Sujet", "sujet.html"), ("Corrigé", "corrige.html")]
    head = f"<h1>{html.escape(dtitle)}</h1><p class=\"cas\">{html.escape(case)}</p>"
    write(DOCS / "exercices" / eid / "sujet.html", page(
        title=f"{dtitle} : {case}", depth=2, kind="sujet",
        margin=margin_block(items, links, "sujet.html"),
        body=head + pandoc(sujet_md)
        + '<p class="vers-corrige">Quand vous avez terminé : <a href="corrige.html">ouvrir le corrigé</a>.</p>'))
    write(DOCS / "exercices" / eid / "corrige.html", page(
        title=f"Corrigé : {dtitle}, {case}", depth=2, kind="corrige",
        margin=margin_block(items, links, "corrige.html"),
        body=head + '<p class="avant">Corrigé indicatif et barème. Les mentions [V] signalent une règle vérifiée sur le texte officiel ; les renvois F01 à F13 et JUR désignent des fiches de travail et les constats des rapports du jury.</p>'
        + pandoc(corr_md)))


def build_subject(s) -> None:
    sid, src, num, parts = s
    (CONTENT / sid).mkdir(parents=True, exist_ok=True)
    for name in ("sujet.md", "corrige.md"):
        shutil.copy(UE4 / "sujets" / src / name, CONTENT / sid / name)
    sujet_md = clean((CONTENT / sid / "sujet.md").read_text(encoding="utf-8"), 2)
    corr_md = clean((CONTENT / sid / "corrige.md").read_text(encoding="utf-8"), 2)
    items = ["Sujet complet", "4 heures", "100 points"]
    links = [("Sujet", "sujet.html"), ("Corrigé", "corrige.html")]
    comp = " ; ".join(f"dossier {EX[p][2]}, {EX[p][4]}" for p in parts)
    head = f"<h1>Sujet d'entraînement n° {num}</h1><p class=\"cas\">{html.escape(comp)}.</p>"
    write(DOCS / "sujets" / sid / "sujet.html", page(
        title=f"Sujet complet n° {num}", depth=2, kind="sujet",
        margin=margin_block(items, links, "sujet.html"),
        body=head + pandoc(sujet_md)
        + '<p class="vers-corrige">Quand vous avez terminé : <a href="corrige.html">ouvrir le corrigé</a>.</p>'))
    write(DOCS / "sujets" / sid / "corrige.html", page(
        title=f"Corrigé du sujet complet n° {num}", depth=2, kind="corrige",
        margin=margin_block(items, links, "corrige.html"),
        body=head + '<p class="avant">Corrigé indicatif et barème. Les mentions [V] signalent une règle vérifiée sur le texte officiel ; les renvois F01 à F13 et JUR désignent des fiches de travail et les constats des rapports du jury.</p>'
        + pandoc(corr_md)))


def build_index() -> None:
    rows = []
    for sid, _, num, parts in SUBJECTS:
        cells = "".join(f"<td>{html.escape(EX[p][4])}</td>" for p in parts)
        rows.append(f'<tr><th scope="row">N° {num}</th>{cells}'
                    f'<td class="liens"><a href="sujets/{sid}/sujet.html">Sujet</a> <a href="sujets/{sid}/corrige.html">Corrigé</a></td></tr>')
    subjects_table = f"""<table class="sujets">
<thead><tr><th></th><th>Dossier 1<br><span>Comptes de groupe, 45 points</span></th><th>Dossier 2<br><span>Restructurations, 25 points</span></th><th>Dossier 3<br><span>Audit, 30 points</span></th><th></th></tr></thead>
<tbody>{"".join(rows)}</tbody></table>"""

    groups = []
    for d in (1, 2, 3):
        es = [e for e in EXERCISES if e[2] == d]
        lis = "".join(
            f'<li><span class="cas">{html.escape(e[4])}</span>'
            f'<span class="meta">{e[5]} points, {html.escape(e[6])}</span>'
            f'<span class="liens"><a href="exercices/{e[0]}/sujet.html">Sujet</a> <a href="exercices/{e[0]}/corrige.html">Corrigé</a></span></li>'
            for e in es)
        groups.append(f"<h3>Dossier {d} : {html.escape(es[0][3])}</h3><ul class=\"dossiers\">{lis}</ul>")

    body = f"""
<h1>Comptabilité et audit<br>s'entraîner pour la session 2027</h1>
<p class="chapeau">Des sujets au format de l'épreuve de l'UE 4 du DSCG, avec leur corrigé et leur barème, construits sur le programme de l'arrêté du 4 août 2025 et sur la réglementation en vigueur au 31 décembre 2026.</p>

<h2>Trois sujets complets</h2>
<p>L'épreuve dure 4 heures, coefficient 1,5. Elle se compose de trois dossiers indépendants : comptes de groupe (45 points), opérations de restructuration (25 points) et audit (30 points, dont 12 sur la durabilité). Seul document autorisé : la liste des comptes du plan comptable général.</p>
{subjects_table}
<p class="note">Les sujets n° 1 et n° 2 partagent leurs dossiers 1 et 3 ; le sujet n° 3 est entièrement différent.</p>

<h2>Six dossiers à la pièce</h2>
<p>Pour travailler un dossier seul, dans le temps que lui laisserait l'épreuve.</p>
{"".join(groups)}

<h2>Comment s'entraîner</h2>
<ol class="methode">
<li>Imprimez le sujet, ou affichez-le seul : les corrigés sont sur une page séparée.</li>
<li>Composez dans le temps indiqué, avec la liste des comptes et une calculatrice sans mémoire. Écrivez vos hypothèses quand l'énoncé l'exige.</li>
<li>Notez-vous avec le barème du corrigé, item par item. Les réponses tolérées y sont indiquées.</li>
<li>Relisez la rubrique des erreurs fréquentes : elle reprend les reproches des rapports du jury.</li>
</ol>

<h2>Ce que vous lisez</h2>
<p>Les cas sont originaux. Les corrigés citent les textes applicables (plan comptable général, règlement ANC 2020‑01, IFRS, code de commerce, normes d'exercice professionnel, lignes directrices de la H2A) et indiquent par la mention [V] les règles vérifiées sur le texte officiel. Les calculs, les écritures et les barèmes ont été contrôlés par un outil de vérification automatique. Comme le rappellent les corrigés officiels, il n'est pas attendu du candidat qu'il cite les numéros d'articles ou de normes.</p>
"""
    write(DOCS / "index.html", page(
        title="DSCG UE 4, entraînement session 2027", depth=0, kind="accueil",
        margin=margin_block(["Entraînement", "session 2027"], []), body=body))


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    (DOCS / ".nojekyll").write_text("")
    shutil.copy(HERE / "style.css", DOCS / "style.css")
    for e in EXERCISES:
        build_exercise(e)
    for s in SUBJECTS:
        build_subject(s)
    build_index()
    n = sum(1 for _ in DOCS.rglob("*.html"))
    print(f"{n} pages écrites dans {DOCS}")


if __name__ == "__main__":
    main()
