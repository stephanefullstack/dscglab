# DSCG UE 4 : entraînement, session 2027

Site statique de sujets d'entraînement à l'épreuve UE 4 (comptabilité et audit) du DSCG, avec corrigés et barèmes. Format de l'épreuve : 4 heures, coefficient 1,5, trois dossiers (comptes de groupe 45 points, restructurations 25 points, audit 30 points dont 12 sur la durabilité). Programme de l'arrêté du 4 août 2025 ; réglementation applicable au 31 décembre 2026.

Les cas sont originaux. Aucun document officiel (sujets d'annales, guide pédagogique, rapports du jury) n'est reproduit ici.

## Contenu

- `content/` : les sujets et corrigés en Markdown, une paire `sujet.md` / `corrige.md` par exercice (`ex01` à `ex06`) et par sujet complet (`sujet-1` à `sujet-3`).
- `docs/` : le site généré, servi par GitHub Pages.
- `build.py` et `style.css` : le générateur et la feuille de style.

## Générer le site

Nécessite Python 3 et pandoc.

```sh
python3 -I build.py
```

Le script lit les sources dans `../ue4/exercices` et `../ue4/sujets` (dossier de travail, non publié), les copie dans `content/`, puis écrit `docs/`.

Supports d'entraînement non officiels, sans lien avec le ministère ni avec les organisateurs de l'examen.
