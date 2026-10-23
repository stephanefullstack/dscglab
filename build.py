"""Build the static site for every UE that has a ue.yaml with a ``site`` section.

Usage (from anywhere): python3 -I build.py
For each UE: copies the Markdown of its exercises and complete subjects into
content/<ue>/, converts it with pandoc and writes docs/ (served by GitHub Pages).
docs/index.html is the hub of the seven UE; each UE has docs/ueN/index.html.
The UE 4 pages keep their historical URLs (docs/exercices/, docs/sujets/).
"""
from __future__ import annotations

import html
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CONTENT = HERE / "content"
DOCS = HERE / "docs"
sys.path.insert(0, str(ROOT / "outils"))
from dscgcheck.config import UEConfig, all_ues  # noqa: E402

FONTS = ("https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;"
         "0,8..60,600;0,8..60,700;1,8..60,400;1,8..60,600&display=swap")
ICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
        "%3Crect width='32' height='32' fill='%23fbfbf9'/%3E%3Cpath d='M8 0v32' stroke='%23c8475d' "
        "stroke-width='2'/%3E%3Cpath d='M0 11h32M0 19h32M0 27h32' stroke='%23a9c4e0'/%3E%3C/svg%3E")
FOOTER = ("Supports d'entraînement non officiels, sans lien avec le ministère ni avec les organisateurs "
          "de l'examen. Réglementation applicable au {date}. Les corrigés ont été contrôlés par un outil "
          "de vérification automatique ; ils peuvent néanmoins comporter des erreurs.")
IGNORE_RE = re.compile(r"\s*<!-- (?:ue4check|dscgcheck):ignorer -->")


def esc(s) -> str:
    """HTML-escape prose: apostrophes are left as they are (attributes are double-quoted)."""
    return html.escape(str(s), quote=False)


def fr_date(iso: str) -> str:
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre",
            "octobre", "novembre", "décembre"]
    y, m, d = str(iso).split("-")
    return f"{int(d)}{'er' if int(d) == 1 else ''} {mois[int(m) - 1]} {y}"


def rel(page_dir: str, target: str) -> str:
    """Relative href from the directory of a page to a target, both relative to docs/."""
    return os.path.relpath(target, page_dir or ".").replace(os.sep, "/")


def pandoc(md: str) -> str:
    return subprocess.run(["pandoc", "-f", "gfm", "-t", "html5", "--wrap=none"],
                          input=md, capture_output=True, text=True, check=True).stdout


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# --- per-UE paths and metadata -------------------------------------------------

def ue_dir(cfg: UEConfig) -> str:
    return f"ue{cfg.numero}"


def pages_root(cfg: UEConfig) -> str:
    return str(cfg.get("site.racine_pages", "") or "")


def pair_dir(cfg: UEConfig, kind: str, item_id: str) -> str:
    return f"{pages_root(cfg)}{kind}/{item_id}"


def exercise_meta(cfg: UEConfig, item: dict) -> tuple[dict, float, str]:
    """(dossier of ue.yaml, points, duration) of an exercise."""
    dossier = cfg.bareme.dossier(int(item["dossier"])) or {"titre": f"Dossier {item['dossier']}"}
    pts = dossier.get("points")
    if pts is None:
        data = yaml.safe_load((cfg.root / "exercices" / item["source"] / "corrige.yaml")
                              .read_text(encoding="utf-8"))
        pts = sum(float(q["points"]) for q in data["bareme"]["dossiers"][0]["questions"])
    # Barème libre : l'exercice donne son propre titre et sa durée (site.exercices).
    dossier = {**dossier, **{k: item[k] for k in ("titre", "duree") if item.get(k)}}
    return dossier, float(pts), str(dossier.get("duree", ""))


def fmt_pts(x: float) -> str:
    return f"{x:g}".replace(".", ",")


# --- markdown cleaning ----------------------------------------------------------

def clean(md: str, cfg: UEConfig, page_dir: str) -> str:
    """Strip the title lines and the working-folder references; link the exercise paths."""
    lines = md.split("\n")
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
        if lines and lines[0].startswith("## "):
            lines = lines[1:]
    md = "\n".join(lines)
    for rule in cfg.get("site.nettoyage") or []:
        md = re.sub(rule["motif"], rule.get("remplacement", ""), md)
    md = IGNORE_RE.sub("", md)
    by_source = {e["source"]: e for e in cfg.get("site.exercices") or []}

    def link(m: re.Match) -> str:
        e = by_source.get(m.group(1))
        if not e:
            return m.group(0)
        return f"[{e['cas']}]({rel(page_dir, pair_dir(cfg, 'exercices', e['id']) + '/sujet.html')})"

    md = re.sub(r"`exercices/([a-z0-9_]+)`", link, md)
    left = [w for w in ("corrige.yaml", "ue4check", "dscgcheck", "gabarits/") if w in md]
    if left:
        print(f"ATTENTION, références internes restantes (UE {cfg.numero}) :", left, file=sys.stderr)
    return md


# --- page skeleton ----------------------------------------------------------------

def page(*, title: str, page_dir: str, margin: str, body: str, kind: str, cfg: UEConfig | None,
         description: str, date: str) -> str:
    sigle = (f'<a class="sigle" href="{rel(page_dir, "index.html")}"><span>DSCG</span></a>'
             if cfg is None else
             f'<a class="sigle" href="{rel(page_dir, "index.html")}"><span>DSCG</span></a>'
             f'<a class="sigle ue" href="{rel(page_dir, ue_dir(cfg) + "/index.html")}">'
             f'<span>{esc(str(cfg.get("site.sigle", "UE " + str(cfg.numero))))}</span></a>')
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="icon" href="{ICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="{rel(page_dir, "style.css")}">
</head>
<body class="{kind}">
<div class="copie">
<aside class="marge">
{sigle}
{margin}
</aside>
<main>
{body}
</main>
</div>
<footer>
<p>{FOOTER.format(date=date)}</p>
</footer>
</body>
</html>
"""


def margin_block(items: list[str], links: list[tuple[str, str]], current: str = "") -> str:
    out = "".join(f"<p>{esc(i)}</p>" for i in items)
    if links:
        out += "<nav>" + "".join(
            f'<a href="{href}"{" aria-current=" + chr(34) + "page" + chr(34) if href == current else ""}>'
            f'{esc(label)}</a>' for label, href in links) + "</nav>"
    return out


# --- builders -------------------------------------------------------------------

def build_pair(cfg: UEConfig, kind: str, item: dict, head: str, items: list[str], title: str) -> None:
    """A sujet/corrigé pair: exercise or complete subject."""
    src = cfg.root / kind / item["source"]
    dst = CONTENT / ue_dir(cfg) / item["id"]
    dst.mkdir(parents=True, exist_ok=True)
    for name in ("sujet.md", "corrige.md"):
        shutil.copy(src / name, dst / name)
    page_dir = pair_dir(cfg, kind, item["id"])
    links = [("Sujet", "sujet.html"), ("Corrigé", "corrige.html")]
    date = fr_date(cfg.data["date_reglementaire"])
    desc = str(cfg.get("site.description_meta", ""))
    sujet_md = clean((dst / "sujet.md").read_text(encoding="utf-8"), cfg, page_dir)
    corr_md = clean((dst / "corrige.md").read_text(encoding="utf-8"), cfg, page_dir)
    write(DOCS / page_dir / "sujet.html", page(
        title=title, page_dir=page_dir, kind="sujet", cfg=cfg, description=desc, date=date,
        margin=margin_block(items, links, "sujet.html"),
        body=head + pandoc(sujet_md)
        + '<p class="vers-corrige">Quand vous avez terminé : <a href="corrige.html">ouvrir le corrigé</a>.</p>'))
    avant = str(cfg.get("site.textes.avant_corrige", "Corrigé indicatif et barème."))
    write(DOCS / page_dir / "corrige.html", page(
        title=f"Corrigé : {title}", page_dir=page_dir, kind="corrige", cfg=cfg, description=desc, date=date,
        margin=margin_block(items, links, "corrige.html"),
        body=head + f'<p class="avant">{esc(avant)}</p>' + pandoc(corr_md)))


def build_exercise(cfg: UEConfig, item: dict) -> None:
    dossier, pts, dur = exercise_meta(cfg, item)
    items = [f"Dossier {item['dossier']}", f"{fmt_pts(pts)} points"] + ([dur] if dur else [])
    head = f"<h1>{esc(dossier['titre'])}</h1><p class=\"cas\">{esc(item['cas'])}</p>"
    build_pair(cfg, "exercices", item, head, items, f"{dossier['titre']} : {item['cas']}")


def build_subject(cfg: UEConfig, item: dict) -> None:
    by_id = {e["id"]: e for e in cfg.get("site.exercices") or []}
    comp = " ; ".join(f"dossier {by_id[p]['dossier']}, {by_id[p]['cas']}" for p in item["composition"])
    ep = cfg.data["epreuve"]
    items = ["Sujet complet", f"{ep['duree_heures']} heures", f"{fmt_pts(cfg.bareme.total)} points"]
    head = f"<h1>Sujet d'entraînement n° {item['numero']}</h1><p class=\"cas\">{esc(comp)}.</p>"
    build_pair(cfg, "sujets", item, head, items, f"Sujet complet n° {item['numero']}")


def build_ue_index(cfg: UEConfig) -> None:
    t = cfg.get("site.textes") or {}
    page_dir = ue_dir(cfg)
    exercises = cfg.get("site.exercices") or []
    subjects = cfg.get("site.sujets") or []
    by_id = {e["id"]: e for e in exercises}
    dossiers = sorted(cfg.bareme.dossiers, key=lambda d: int(d["numero"]))

    def links(kind: str, item_id: str) -> str:
        base = pair_dir(cfg, kind, item_id)
        return (f'<a href="{rel(page_dir, base + "/sujet.html")}">Sujet</a> '
                f'<a href="{rel(page_dir, base + "/corrige.html")}">Corrigé</a>')

    body = f"""
<h1>{t.get("titre", cfg.data["intitule"])}</h1>
<p class="chapeau">{esc(str(t.get("chapeau", "")))}</p>
"""
    if subjects:
        heads = "".join(
            f'<th>Dossier {d["numero"]}<br><span>{esc(d.get("titre_court", d["titre"]))}'
            f'{", " + fmt_pts(float(d["points"])) + " points" if d.get("points") is not None else ""}</span></th>'
            for d in dossiers)
        rows = "".join(
            f'<tr><th scope="row">N° {s["numero"]}</th>'
            + "".join(f"<td>{esc(by_id[p]['cas'])}</td>" for p in s["composition"])
            + f'<td class="liens">{links("sujets", s["id"])}</td></tr>' for s in subjects)
        body += f"""
<h2>{esc(str(t.get("titre_sujets", "Sujets complets")))}</h2>
<p>{esc(str(t.get("presentation", "")))}</p>
<table class="sujets">
<thead><tr><th></th>{heads}<th></th></tr></thead>
<tbody>{rows}</tbody></table>
"""
        if t.get("note_sujets"):
            body += f'<p class="note">{esc(str(t["note_sujets"]))}</p>\n'
    if exercises:
        body += f"""
<h2>{esc(str(t.get("titre_dossiers", "Dossiers à la pièce")))}</h2>
<p>{esc(str(t.get("intro_dossiers", "")))}</p>
"""
        for d in dossiers:
            es = [e for e in exercises if int(e["dossier"]) == int(d["numero"])]
            if not es:
                continue
            lis = ""
            for e in es:
                _, pts, dur = exercise_meta(cfg, e)
                meta = f"{fmt_pts(pts)} points" + (f", {dur}" if dur else "")
                lis += (f'<li><span class="cas">{esc(e["cas"])}</span>'
                        f'<span class="meta">{esc(meta)}</span>'
                        f'<span class="liens">{links("exercices", e["id"])}</span></li>')
            name = f"Dossier {d['numero']}"
            if d["titre"] != name:
                name += f" : {d['titre']}"
            body += f'<h3>{esc(name)}</h3><ul class="dossiers">{lis}</ul>'
    if t.get("methode"):
        body += "\n<h2>Comment s'entraîner</h2>\n<ol class=\"methode\">\n" + "".join(
            f"<li>{esc(str(m))}</li>\n" for m in t["methode"]) + "</ol>\n"
    if t.get("ce_que_vous_lisez"):
        body += f"\n<h2>Ce que vous lisez</h2>\n<p>{esc(str(t['ce_que_vous_lisez']))}</p>\n"
    write(DOCS / page_dir / "index.html", page(
        title=f"DSCG UE {cfg.numero}, entraînement session 2027", page_dir=page_dir, kind="accueil", cfg=cfg,
        description=str(cfg.get("site.description_meta", "")), date=fr_date(cfg.data["date_reglementaire"]),
        margin=margin_block(["Entraînement", "session 2027"], []), body=body))


def build_hub(configs: dict[int, UEConfig]) -> None:
    registry = yaml.safe_load((ROOT / "commun" / "ues.yaml").read_text(encoding="utf-8"))["ues"]
    rows = ""
    for ue in registry:
        n = int(ue["numero"])
        cfg = configs.get(n)
        if cfg is not None and cfg.get("site.publier", False):
            n_ex = len(cfg.get("site.exercices") or [])
            n_su = len(cfg.get("site.sujets") or [])
            what = []
            if n_su:
                what.append(f"{n_su} sujet{'s' if n_su > 1 else ''} complet{'s' if n_su > 1 else ''}")
            if n_ex:
                what.append(f"{n_ex} dossier{'s' if n_ex > 1 else ''} à la pièce")
            status = f'<a href="{ue_dir(cfg)}/index.html">{esc(", ".join(what) or "Ouvrir")}</a>'
            klass = ""
        else:
            status = "En préparation"
            klass = ' class="attente"'
        rows += (f'<li{klass}><span class="num">UE {n}</span><span class="cas">{esc(ue["intitule"])}</span>'
                 f'<span class="meta">{esc(ue["format"])}</span><span class="liens">{status}</span></li>')
    body = f"""
<h1>DSCG<br>s'entraîner pour la session 2027</h1>
<p class="chapeau">Des sujets au format de chaque épreuve, avec leur corrigé et leur barème, construits sur le programme de l'arrêté du 4 août 2025 et sur la réglementation en vigueur au 31 décembre 2026. Une unité d'enseignement à la fois : les autres arrivent.</p>
<h2>Les sept unités d'enseignement</h2>
<ul class="dossiers hub">{rows}</ul>
<h2>Comment s'entraîner</h2>
<ol class="methode">
<li>Choisissez une épreuve, puis un sujet complet ou un dossier seul.</li>
<li>Composez dans le temps indiqué, dans les conditions de l'examen : les corrigés sont sur une page séparée.</li>
<li>Notez-vous avec le barème, item par item, puis relisez les erreurs fréquentes relevées par les jurys.</li>
</ol>
<h2>Ce que vous lisez</h2>
<p>Les cas sont originaux. Les corrigés citent les textes applicables et signalent par la mention [V] les règles vérifiées sur le texte officiel ; leurs calculs et leurs barèmes ont été contrôlés par un outil de vérification automatique. Aucun document officiel (sujets d'annales, guide pédagogique, rapports du jury) n'est reproduit ici.</p>
"""
    write(DOCS / "index.html", page(
        title="DSCG, entraînement session 2027", page_dir="", kind="accueil hub", cfg=None,
        description="Entraînement au DSCG, session 2027 : sujets et corrigés pour les sept unités d'enseignement.",
        date="31 décembre 2026", margin=margin_block(["Entraînement", "session 2027"], []), body=body))


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    DOCS.mkdir()
    (DOCS / ".nojekyll").write_text("")
    shutil.copy(HERE / "style.css", DOCS / "style.css")
    configs = {cfg.numero: cfg for cfg in all_ues() if cfg.data.get("site")}
    for cfg in configs.values():
        if not cfg.get("site.publier", False):
            continue
        for item in cfg.get("site.exercices") or []:
            build_exercise(cfg, item)
        for item in cfg.get("site.sujets") or []:
            build_subject(cfg, item)
        build_ue_index(cfg)
    build_hub(configs)
    n = sum(1 for _ in DOCS.rglob("*.html"))
    print(f"{n} pages écrites dans {DOCS}")


if __name__ == "__main__":
    main()
