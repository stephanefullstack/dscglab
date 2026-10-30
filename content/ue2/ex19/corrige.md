# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 19 — Dossier 1 (18 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières, F04 diagnostic financier consolidé, F08 gouvernance et ESG, F09 réglementation bancaire, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (équilibre des bilans et des flux, ratios de diagnostic et de crédit avec et sans dettes locatives, note financière et score extra-financier sur grille, taux actuariels avant et après impôt, barème, liste noire, hors-programme ; scénarios d'apport et de gouvernance vérifiés par script).

Bien que le corrigé mentionne des auteurs et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une note financière établie avec des ratios erronés à la question 1.2, ou un taux actuariel calculé avec le coupon de secours de 5,00 %).

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Bilan économique, rentabilités et effet de levier | `1.c` Apprécier la performance opérationnelle et financière d'un groupe ; `1.a` Réaliser une analyse financière des comptes consolidés | 4 |
| 1.2 Ratios de crédit et lecture des retraitements | `1.b` Interpréter les états financiers des groupes en normes comptables internationales (IFRS) ; `1.a` | 3 |
| 1.3 Note financière et conditions de l'émission | `2.1.c` Utiliser les outils de notation financière et extra-financière ; `1.a` | 4 |
| 1.4 Score extra-financier | `2.1.c` ; `2.1.a` Identifier les éléments extra-financiers pour le diagnostic, dans la lignée du modèle d'affaires ; `2.1.d` Maîtriser le principe de double matérialité | 3 |
| 1.5 Coût et choix du financement | `6.1.b` Discerner les différents types de financement et de placement ; `7.2.a` Comparer les sources de financement et notamment leurs coûts | 4 |
| **Total** | | **18** |

Part du calcul : environ 11,25 points (1.1-01 à 1.1-03, 1.2-01, 1.2-02, 1.3-01, 1.3-02 pour moitié, 1.3-03 pour moitié, 1.4-01, 1.5-01). Part de l'analyse : environ 6,75 points. Les questions 1.4 et 1.5 valent ensemble 7 points : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 1.1 Bilan économique, rentabilités et effet de levier (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Bilan économique : immobilisations 254,33 / 265,00, BFR 3,87 / 5,00, actif économique 258,20 / 270,00 = capitaux propres 143,50 / 152,00 + DFN 114,70 / 118,00 | 1 |
| 1.1-02 | ROCE après impôt 5,64 % / 6,13 % ; ROE global 7,74 % / 8,42 % ; ROE part du groupe 7,70 % / 8,39 % ; ROE des minoritaires 8,24 % / 8,89 % | 1 |
| 1.1-03 | Coût net de la dette 3,01 % / 3,18 % ; DFN / CP 0,7993 / 0,7763 ; effet de levier 2,10 / 2,29 points ; ROE = ROCE + effet de levier vérifié | 1 |
| 1.1-04 | Commentaire du point de vue d'un prêteur : rentabilité modeste mais en hausse, levier favorable avec une marge de sécurité, rôle de la juste valeur, place des minoritaires et de la holding | 1 |

**Démarche.** Le bilan économique regroupe, à l'actif, les capitaux investis dans l'exploitation (immobilisations et BFR) et, au passif, leur financement par les actionnaires (capitaux propres totaux, minoritaires compris) et par la dette nette de la trésorerie [F04 § 2 ; V guide p. 58].

**Bilan économique (M€)**

| | 2025 | 2026 |
|---|---:|---:|
| Goodwill + autres incorporelles + corporelles | 18,00 + 4,00 + 193,20 = 215,20 | 18,00 + 4,00 + 200,00 = 222,00 |
| + Immeuble de placement + droits d'utilisation | 8,13 + 31,00 = 39,13 | 9,00 + 34,00 = 43,00 |
| **Immobilisations** | **254,33** | **265,00** |
| Stocks + clients + autres créances | 2,57 + 47,20 + 8,30 = 58,07 | 3,00 + 50,00 + 9,00 = 62,00 |
| − Fournisseurs − autres dettes d'exploitation | − 31,80 − 22,40 = − 54,20 | − 33,00 − 24,00 = − 57,00 |
| **BFR** | **3,87** | **5,00** |
| **Actif économique** | **258,20** | **270,00** |
| Capitaux propres part du groupe + intérêts minoritaires | 135,00 + 8,50 = 143,50 | 143,00 + 9,00 = 152,00 |
| Emprunts bancaires + dettes locatives − trésorerie | 106,00 + 31,00 − 22,30 = 114,70 | 112,00 + 34,00 − 28,00 = 118,00 |
| **Capitaux propres + DFN** | **258,20** | **270,00** |

**Rentabilités et effet de levier** (conventions de l'annexe 1.3, montants de clôture, DFN dettes locatives comprises)

| | 2025 | 2026 |
|---|---:|---:|
| ROCE après impôt = RO × 0,75 / actif économique | 19,40 × 0,75 / 258,20 = 14,55 / 258,20 = **5,64 %** | 22,07 × 0,75 / 270,00 = 16,55 / 270,00 = **6,13 %** |
| ROE global = RN ensemble / CP totaux | 11,10 / 143,50 = **7,74 %** | 12,80 / 152,00 = **8,42 %** |
| ROE part du groupe | 10,40 / 135,00 = **7,70 %** | 12,00 / 143,00 = **8,39 %** |
| ROE des minoritaires | 0,70 / 8,50 = **8,24 %** | 0,80 / 9,00 = **8,89 %** |
| Coût net de la dette i = CEFN × 0,75 / DFN | 4,60 × 0,75 / 114,70 = **3,01 %** | 5,00 × 0,75 / 118,00 = **3,18 %** |
| DFN / CP totaux | 114,70 / 143,50 = **0,7993** | 118,00 / 152,00 = **0,7763** |
| Effet de levier = (ROCE − i) × DFN / CP | (5,64 − 3,01) × 0,7993 = **2,10 points** | (6,13 − 3,18) × 0,7763 = **2,29 points** |
| ROE = ROCE + effet de levier | 5,64 + 2,10 = **7,74 %** | 6,13 + 2,29 = **8,42 %** |

L'identité tombe juste, car le résultat net est égal au résultat opérationnel diminué du coût de l'endettement, l'ensemble après impôt à 25 % ; en 2026, l'arrondi de l'impôt au centième (4,27 pour 4,2675) ne modifie pas le deuxième chiffre après la virgule.

**Commentaire du point de vue d'un prêteur (1 pt).**
- **Activité et marges en progression** : chiffre d'affaires + 6,72 %, EBITDA + 9,52 % (marge de 15,67 % à 16,08 %), résultat opérationnel courant + 10,99 %. À périmètre constant, la croissance est organique.
- **Rentabilité économique modeste**, typique d'un métier à forte intensité capitalistique : 1,06 € de chiffre d'affaires par euro d'actif économique, ROCE après impôt de 6,13 % (8,17 % avant impôt). Une partie de la hausse vient de la juste valeur : hors variation de juste valeur, le ROCE passe de 5,55 % à 5,89 % seulement (question 1.2).
- **Levier favorable** : l'écart ROCE − i passe de 2,63 à 2,95 points ; le ROE gagne 0,68 point (8,42 − 7,74), dont 0,49 point vient du ROCE et 0,19 point du levier. Pour un prêteur, la question est la **marge de sécurité** : le levier ne deviendrait défavorable (effet de massue) que si le résultat opérationnel tombait à 5,00 × 270,00 / 118,00 = 11,44 M€ (ROCE égal au coût net de la dette), soit une baisse d'environ 48 %. Le risque financier existe : avec une dette nette égale à 78 % des capitaux propres, toute baisse du ROCE est amplifiée sur le ROE (Modigliani et Miller, 1958 : la rentabilité exigée par les actionnaires augmente avec l'endettement) [F10, S].
- **Minoritaires et holding** : GIVRÉANE est un peu plus rentable que le reste du groupe (ROE des minoritaires 8,89 % contre 8,39 % pour la part du groupe) et 6,25 % du résultat revient à son fondateur. Les obligations seront émises par HIVERLANE Participations, qui se rembourse avec les dividendes de ses filiales : 20 % des distributions de GIVRÉANE lui échappent, et les créanciers des filiales sont payés avant elle sur les actifs de celles-ci.
- **BFR très faible** (5,00 / 286,00 × 360 = 6,3 jours de chiffre d'affaires) : l'exploitation ne consomme presque pas de trésorerie ; le besoin de financement vient des investissements (25,00 M€ en 2026, 1,37 fois les dotations hors droits d'utilisation), qui font baisser le flux de trésorerie disponible de 5,80 à 4,00 M€.

**Réponses tolérées** : ROCE avant impôt en complément ; ROCE calculé sur le résultat opérationnel courant (5,55 % et 5,89 %), si le candidat l'annonce et en tire un effet de levier cohérent, l'identité ne tombant plus juste de l'effet de la juste valeur ; ROE global 2026 de 8,421 % arrondi à 8,42 % ; effet de levier calculé sur valeurs non arrondies (2,10 et 2,29, identiques).

**Erreurs fréquentes**
- Capitaux propres part du groupe seuls (135,00 / 143,00) dans le bilan économique ou le ROE global : le bilan ne s'équilibre plus, l'écart est égal aux minoritaires [F04 § 3].
- Oublier l'immeuble de placement ou les droits d'utilisation à l'actif alors que les dettes locatives restent dans la DFN.
- Coût de la dette avant impôt (5,00 / 118,00 = 4,24 %) combiné à un ROCE après impôt : l'identité ne tombe plus juste.
- `JUR-T07` — bilan économique et rentabilités présentés en texte plutôt qu'en tableau ; `JUR-T13` — rentabilités calculées sans lecture du point de vue du prêteur ; `JUR-T14` — effet de levier présenté comme une création de valeur, sans le risque financier qui l'accompagne.

---

### 1.2 Ratios de crédit et lecture des retraitements (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | Flux de trésorerie disponible 4,00 ; ratios dettes locatives comprises (2,57 ; 77,63 % ; 9,20 ; 3,39 %) et hors effet de la norme (2,21 ; 55,26 % ; 10,56 ; 4,76 %) | 1,5 |
| 1.2-02 | Juste valeur : 0,87 M€ dans le résultat opérationnel, résultat net hors juste valeur 12,15 M€, ROE 7,99 % ; aucun effet sur l'EBITDA, la trésorerie ni les ratios de la grille | 0,5 |
| 1.2-03 | Lecture retenue : dettes locatives comprises pour la notation (méthode de l'agence) ; hors effet de la norme pour l'engagement bancaire (2,21 ≤ 3,00, marge chiffrée) | 1 |

**Flux de trésorerie disponible 2026** (convention de l'annexe 1.3) : 35,60 − 25,00 − 6,60 = **4,00 M€** (5,80 M€ en 2025). Il est identique dans les deux lectures : hors effet de la norme, les loyers seraient des charges d'exploitation et diminueraient le flux lié à l'activité du montant des remboursements de dettes locatives ; la trésorerie, elle, ne change pas.

**Ratios de 2026** (retraitements fournis par la note 1, à utiliser tels quels)

| 2026 | Dettes locatives comprises | Hors effet de la norme | Écart |
|---|---:|---:|---:|
| EBITDA | 46,00 | 38,00 | + 8,00 (loyers) |
| Coût de l'endettement financier net | 5,00 | 3,60 | + 1,40 |
| DFN | 118,00 | 84,00 | + 34,00 |
| DFN / EBITDA | 118,00 / 46,00 = **2,57** | 84,00 / 38,00 = **2,21** | + 0,36 |
| Gearing (DFN / CP) | 118,00 / 152,00 = **77,63 %** | 84,00 / 152,00 = **55,26 %** | + 22,37 points |
| Couverture des frais financiers par l'EBITDA | 46,00 / 5,00 = **9,20 fois** | 38,00 / 3,60 = **10,56 fois** | − 1,36 |
| Flux de trésorerie disponible / DFN | 4,00 / 118,00 = **3,39 %** | 4,00 / 84,00 = **4,76 %** | − 1,37 point |

- La norme traite la location comme un **financement** de l'actif loué (primauté de la substance sur la forme) : les loyers sortent des charges d'exploitation et sont remplacés par un amortissement et des intérêts. L'EBITDA augmente de 8,00 M€ et la dette de 34,00 M€, sans changement de l'activité ni de la trésorerie [F04 § 2 ; V guide p. 58].
- Tous les ratios de crédit se **dégradent** dettes locatives comprises : la dette locative (34,00 M€) représente 4,25 fois les loyers (8,00 M€), plus que le rapport DFN / EBITDA du groupe ; le gearing augmente fortement, car les capitaux propres ne changent pas ; la couverture baisse, car les intérêts locatifs s'ajoutent.

**Juste valeur (0,5 pt).** La variation de juste valeur de l'immeuble de placement (+ 0,87 M€) représente 3,94 % du résultat opérationnel. Elle augmente le résultat net de 0,87 × 0,75 = 0,65 M€ : hors juste valeur, le résultat net serait de 12,80 − 0,65 = **12,15 M€** et le ROE global de 12,15 / 152,00 = **7,99 %** au lieu de 8,42 %. Le ROCE passe de 6,13 % à 5,89 %. C'est un gain latent, non encaissé et non récurrent : il dépend de l'évolution du marché immobilier et rend le résultat plus volatil, ce qui est le prix de l'approche de marché du référentiel IFRS [V guide p. 58]. Il ne modifie ni l'EBITDA (il est présenté sous le résultat opérationnel courant), ni la capacité d'autofinancement (la note 2 et l'annexe 1.2 l'en retirent), ni le flux disponible : les ratios de la grille de l'agence n'en sont pas affectés.

**Lecture à retenir (1 pt).**
- **Notation** : l'agence calcule ses ratios dettes locatives comprises (annexe 1.4) ; la note se calcule donc avec 2,57 ; 9,20 ; 3,39 % et 77,63 %. C'est la lecture économique : un entrepôt loué pour une longue durée engage le groupe comme une dette.
- **Engagement des crédits bancaires en cours** : le contrat définit le ratio hors effet de la norme (note 4). Avec 2,21 ≤ 3,00, l'engagement est respecté. À EBITDA constant, la DFN hors dettes locatives pourrait augmenter de 3,00 × 38,00 − 84,00 = **30,00 M€** ; à dette constante, l'EBITDA hors effet de la norme pourrait baisser jusqu'à 84,00 / 3,00 = 28,00 M€ (− 26,3 %).
- Mélanger les deux lectures fausse l'analyse : une note calculée avec les ratios hors effet de la norme serait surestimée (question 1.3).

**Réponses tolérées** : ratios exprimés en multiple ou en pourcentage (3,39 % ou 0,0339) ; gearing 77,6 % ; effet de la juste valeur sur le résultat net donné avant impôt (0,87), si le candidat signale l'impôt de 25 % ; capacité d'autofinancement rapportée à la DFN en complément (31,13 % dettes locatives comprises ; 30,13 / 84,00 = 35,87 % hors effet de la norme).

**Erreurs fréquentes**
- Recalculer le flux disponible hors effet de la norme en ajoutant les loyers : la trésorerie est la même dans les deux lectures.
- Conclure que la norme améliore la capacité de remboursement parce qu'elle augmente l'EBITDA : elle augmente aussi la dette, et tous les ratios de crédit se dégradent.
- Exposer les critères comptables de la norme : la question porte sur l'interprétation, la technique comptable relève de l'UE 4.
- `JUR-T03` — oublier la note 2 (juste valeur) ou la note 4 (définition contractuelle du ratio) ; `JUR-T13` — ratios calculés sans indiquer qui les utilise.

---

### 1.3 Note financière et conditions de l'émission (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | Points par critère (3 ; 4 ; 2 ; 3 ; 3), score pondéré 2,90, note BB, en dessous de la catégorie « investissement » | 1,5 |
| 1.3-02 | Ratios contraignants (DFN / EBITDA, flux disponible / DFN, gearing) ; apport de 3,50 M€ : score 3,35, note BBB ; réduction de la dette sans apport : score 3,20, note BB | 1,5 |
| 1.3-03 | Influence de la note (accès aux investisseurs, marge, engagements) ; coupon 5,80 % (BB) contre 4,60 % (BBB) ; écart de 0,72 M€ par an avant impôt et 0,54 M€ après impôt | 1 |

**Note du groupe** (ratios dettes locatives comprises, question 1.2)

| Critère | Valeur 2026 | Palier | Points | Poids | Points pondérés |
|---|---:|---|---:|---:|---:|
| DFN / EBITDA | 2,57 | ≤ 3,50 | 3 | 30 % | 0,90 |
| Couverture des frais financiers | 9,20 | ≥ 8,00 | 4 | 10 % | 0,40 |
| Flux disponible / DFN | 3,39 % | ≥ 2 % | 2 | 20 % | 0,40 |
| Gearing | 77,63 % | ≤ 100 % | 3 | 15 % | 0,45 |
| Profil d'activité | appréciation | — | 3 | 25 % | 0,75 |
| **Score** | | | | | **2,90** |

Le score de 2,90 est compris entre 2,50 et 3,25 : la note est **BB**, un cran sous la catégorie « investissement ». Plusieurs investisseurs pressentis ne pourraient pas souscrire.

**Ratios qui contraignent la note (1,5 pt avec les deux scénarios).**
- **DFN / EBITDA** (poids le plus fort) : 2,57, juste au-dessus du seuil de 2,50. Il suffit d'une DFN de 2,50 × 46,00 = 115,00 M€, soit 3,00 M€ de moins, pour gagner un palier (+ 0,30 point de score).
- **Gearing** : 77,63 %, juste au-dessus de 75 %. Le palier supérieur est atteint avec une DFN de 114,00 M€ à capitaux propres constants (4,00 M€ de moins), ou avec un apport en capital d'au moins (118,00 − 0,75 × 152,00) / 1,75 = 2,29 M€, qui réduit la dette et augmente les capitaux propres (+ 0,15 point).
- **Flux disponible / DFN** : 3,39 %, loin du palier de 5 % (il faudrait 5,90 M€ de flux disponible, au lieu de 4,00) : l'effort d'investissement pèse sur la note.
- La couverture des frais financiers (9,20) n'est pas une contrainte.

**Scénarios** (frais financiers et flux disponible inchangés)

| | DFN | Capitaux propres | DFN / EBITDA | Gearing | Points (DFN/EBITDA ; gearing) | Score | Note |
|---|---:|---:|---:|---:|---|---:|---|
| Situation 2026 | 118,00 | 152,00 | 2,57 | 77,63 % | 3 ; 3 | 2,90 | BB |
| Apport en capital de 3,50 M€ affecté à la dette | 114,50 | 155,50 | 2,49 | 73,63 % | 4 ; 4 | **3,35** | **BBB** |
| Réduction de la DFN de 3,50 M€ sans apport (cession d'actifs) | 114,50 | 152,00 | 2,49 | 75,33 % | 4 ; 3 | **3,20** | **BB** |

Conformément à l'annexe 1.4, l'apport réalisé avant l'attribution de la note est pris en compte sur une base pro forma. Le flux disponible / DFN reste au palier de 2 points (4,00 / 114,50 = 3,49 %). L'apport en capital agit sur deux critères à la fois (moins de dette, plus de capitaux propres) et fait passer la note en BBB ; la même réduction de dette obtenue par une cession d'actifs n'améliore que le premier critère. Différer 3,50 M€ d'investissements améliorerait aussi le flux disponible (7,50 / 114,50 = 6,55 %, 3 points, score 3,40), mais retarderait la conversion des fluides (question 1.4) : amélioration ponctuelle, que l'agence corrigerait l'année suivante. La note BBB obtenue avec l'apport reste **fragile** : le rapport DFN / EBITDA de 2,49 est à la limite du palier, et toute hausse de la dette en 2027 (investissements dans les fluides) ou baisse de l'EBITDA la ferait perdre.

**Influence de la note sur l'émission (1 pt).**
- La notation financière exprime l'opinion de l'agence sur le **risque de défaut** de l'émetteur ; elle conditionne l'accès au marché, le taux et les engagements demandés [V guide p. 61 ; F08 § 3.1].
- **Accès** : en BB, l'émission s'adresse à une base d'investisseurs plus étroite (plusieurs ne peuvent pas acheter sous BBB) ; le placement de 60 M€ est moins sûr.
- **Coût** : coupon = 3,00 % + 2,80 % = **5,80 %** en BB, contre 3,00 % + 1,60 % = **4,60 %** en BBB. Écart : 1,20 point × 60,00 = **0,72 M€ par an** avant impôt, 0,72 × 0,75 = **0,54 M€ par an** après impôt, soit 4,32 M€ avant impôt et 3,24 M€ après impôt sur six ans, sans actualisation.
- **Contraintes** : un émetteur moins bien noté se voit demander des engagements plus stricts (limitation des distributions ou de l'endettement) ; la note doit être maintenue pendant toute la durée de l'emprunt, et une dégradation renchérirait les refinancements suivants.

**Réponses tolérées** : écart de coût exprimé en points de base (120) en plus du montant ; scénarios présentés en variation du score (+ 0,45 et + 0,30) ; flux disponible / DFN du scénario non recalculé, si le candidat indique que son palier ne change pas.

**Erreurs fréquentes**
- Noter le groupe avec les ratios hors effet de la norme (2,21 ; 55,26 % ; 10,56 ; 4,76 %) : points 4 ; 4 ; 2 ; 4 ; 3, score 3,35 et note BBB, alors que l'agence calcule ses ratios dettes locatives comprises.
- Lire un palier sur un ratio non arrondi de manière incohérente avec la convention de l'annexe 1.3, ou classer une valeur égale à une borne dans le palier inférieur (la borne appartient au palier).
- Additionner les points sans les pondérer (15 points sur 25) puis appliquer l'échelle des scores pondérés.
- `JUR-T13` — influence de la note décrite en général (« une meilleure note réduit le coût ») sans les marges de l'annexe ni le chiffrage de l'écart ; `JUR-T10` — question traitée sans le calcul du score.

---

### 1.4 Score extra-financier (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Points par critère (4 ; 2 ; 2 ; 2 ; 2), score 2,40, catégorie « Limité » | 1,5 |
| 1.4-02 | Points faibles reliés au modèle d'affaires et aux risques financiers ; conséquences pour l'émission ; actions chiffrées pour atteindre « Confirmé » (score d'au moins 3,00) | 1,5 |

**Calcul du score**

| Critère | Donnée | Points | Poids | Points pondérés | Manque par rapport à 5 points |
|---|---:|---:|---:|---:|---:|
| E1 Intensité énergétique | 28 kWh/m³/an (≤ 32) | 4 | 20 % | 0,80 | 0,20 |
| E2 Fluides à faible effet de serre | 30 % (≥ 20 %) | 2 | 25 % | 0,50 | 0,75 |
| S1 Taux de fréquence des accidents | 31 (≤ 40) | 2 | 20 % | 0,40 | 0,60 |
| G1 Membres indépendants | 1 sur 8 = 12,5 % (≥ 10 %) | 2 | 15 % | 0,30 | 0,45 |
| G2 Dispositifs de gouvernance | 2 sur 5 (charte familiale, critère extra-financier de rémunération) | 2 | 20 % | 0,40 | 0,60 |
| **Score** | | | | **2,40** | |

Le score de 2,40 classe le groupe dans la catégorie **« Limité »** (de 2,00 à moins de 3,00). Présenté par pilier, comme le prévoit le règlement européen sur les notations ESG (notes E, S et G distinctes ou pondérations publiées) : E = (0,80 + 0,50) / 0,45 = 2,89 ; S = 2,00 ; G = (0,30 + 0,40) / 0,35 = 2,00 [V règlement (UE) 2024/3005, art. 23 ; F08 § 3.2].

**Points faibles et conséquences (1,5 pt avec le plan d'actions).**
- **Fluides frigorigènes (E2)** : c'est le critère le plus pondéré et le plus pénalisant (0,75 point de manque). Il touche le cœur du modèle d'affaires : dix entrepôts sur quatorze utilisent des fluides à fort effet de serre, qui deviendront plus coûteux et plus difficiles à se procurer. Le risque est à la fois un impact sur l'environnement et un risque financier (double matérialité) : le remplacement coûte 10 × 2,40 = 24,00 M€, presque une année d'investissements, ce qui pèsera sur le flux disponible et donc sur la note financière (question 1.3).
- **Sécurité au travail (S1)** : 31 accidents avec arrêt par million d'heures, juste au-dessus du palier de 30 ; métier de manutention dans le froid, qui expose à l'absentéisme, aux difficultés de recrutement et à un risque de réputation auprès des clients (grande distribution, laboratoires).
- **Gouvernance (G1 et G2)** : un seul membre indépendant sur huit, pas de comité d'audit ni de plan de succession formalisé, indicateurs extra-financiers non vérifiés. Pour des porteurs d'obligations, qui ne votent pas, c'est la principale protection contre les conflits d'intérêts : entre les branches familiales (certains associés veulent des dividendes plus élevés) et entre actionnaires et créanciers (distribuer plutôt que rembourser). Ces mécanismes de contrôle réduisent les coûts d'agence au sens de Jensen et Meckling (1976) [F10 § 3 ; F08 § 1.1] ; l'attention portée aux salariés, aux clients et à l'environnement relève de l'approche partenariale de Freeman (1984).
- **Conséquences pour l'émission** : en « Limité », le groupe est exclu de la part des souscriptions réservée aux émetteurs « Confirmé » ; la demande se réduit et la marge risque d'augmenter, ce qui s'ajoute à la note BB.

**Actions pour atteindre « Confirmé » (il manque 0,60 point)**

| Action | Effet sur les points | Effet sur le score |
|---|---|---:|
| Créer un comité d'audit et formaliser le plan de succession (4 dispositifs sur 5) | G2 : 2 → 4 | + 0,40 |
| Nommer un second membre indépendant à la place d'un membre familial (2 sur 8 = 25 %) | G1 : 2 → 3 | + 0,15 |
| Convertir deux entrepôts (30 % + 2 × 7 % = 44 % de la puissance), pour 2 × 2,40 = 4,80 M€ | E2 : 2 → 3 | + 0,25 |
| **Score après le plan** | | **3,20 : « Confirmé »** |

Les deux mesures de gouvernance seules donnent 2,95, encore « Limité » ; elles sont rapides et peu coûteuses, mais il faut un troisième levier : la conversion de deux entrepôts, la vérification des indicateurs par un tiers (G2 à 5 points, score 3,15) ou un taux de fréquence ramené à 30 (S1 à 3 points, score 3,15). Le candidat doit relever la limite de l'exercice : un score qui progresse grâce aux seuls dispositifs de gouvernance ne réduit pas le risque principal, celui des fluides, que les investisseurs regarderont dans le détail.

**Réponses tolérées** : score exprimé sur 100 (48/100) si la conversion est expliquée ; toute combinaison d'actions chiffrée qui atteint 3,00 ; mention que TALVÉRINE, fournisseur de notations ESG agréé par l'AEMF, ne peut pas exercer d'activité de notation de crédit (séparation des activités) [V règlement (UE) 2024/3005, art. 16 ; F08 § 3.2].

**Erreurs fréquentes**
- `JUR-D01` — confondre la démarche RSE du groupe et les critères ESG utilisés par les investisseurs pour le noter.
- Compter l'indépendance en nombre de membres (1) au lieu de la proportion (12,5 %), ou lire le palier « ≥ 10 % » comme non atteint.
- `JUR-T05` — commenter le score sans lien avec la performance financière (coût des fluides, flux disponible, note financière).
- `JUR-T13` — liste générale de bonnes pratiques ESG sans les données de l'annexe 1.5 ni le chiffrage du plan.

---

### 1.5 Coût et choix du financement (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | Obligation au coupon de 5,80 % : flux avant impôt (59,10 ; − 3,48 ; … ; − 63,48), taux 6,11 % ; flux après impôt (59,33 ; − 2,61 ; … ; − 62,61), taux 4,57 % ; comparaison au crédit bancaire (5,06 % et 3,79 %, fournis) | 2 |
| 1.5-03 | Comparaison argumentée des trois financements (horizon, coût, liquidité, contraintes) et recommandation cohérente | 2 |

**Émission obligataire notée BB** (coupon 5,80 %, frais de 0,90 M€ à la date 0, remboursement in fine)

| Date | 0 | 1 à 5 | 6 |
|---|---:|---:|---:|
| Flux avant impôt | 60,00 − 0,90 = 59,10 | − 60,00 × 5,80 % = − 3,48 | − 3,48 − 60,00 = − 63,48 |
| Flux après impôt | 59,10 + 0,90 × 25 % = 59,33 | − 3,48 × 0,75 = − 2,61 | − 2,61 − 60,00 = − 62,61 |

Taux actuariel avant impôt : t tel que 59,10 = 3,48 × [1 − (1 + t)^−6] / t + 60,00 × (1 + t)^−6, soit **t = 6,11 %** (le coupon de 5,80 % est majoré par les frais). Après impôt : 59,33 = 2,61 × [1 − (1 + t)^−6] / t + 60,00 × (1 + t)^−6, soit **t = 4,57 %**. Avec le coupon de secours de 5,00 % : 5,30 % et 3,96 %. Pour comparaison, une émission notée BBB (coupon 4,60 %) coûterait 4,89 % avant impôt et 3,66 % après impôt.

**Crédit bancaire amortissable** (amortissement constant de 10,00 M€, taux 4,90 %, frais de 0,30 M€) : taux fournis par l'annexe 1.6 ; le tableau ci-dessous les justifie, il n'est pas demandé au candidat.

| Année | Capital dû en début d'année | Intérêts | Amortissement | Flux avant impôt | Flux après impôt |
|---|---:|---:|---:|---:|---:|
| 0 | | | | 59,70 | 59,78 |
| 1 | 60,00 | 2,94 | 10,00 | − 12,94 | − 12,21 |
| 2 | 50,00 | 2,45 | 10,00 | − 12,45 | − 11,84 |
| 3 | 40,00 | 1,96 | 10,00 | − 11,96 | − 11,47 |
| 4 | 30,00 | 1,47 | 10,00 | − 11,47 | − 11,10 |
| 5 | 20,00 | 0,98 | 10,00 | − 10,98 | − 10,74 |
| 6 | 10,00 | 0,49 | 10,00 | − 10,49 | − 10,37 |

Taux actuariel : **5,06 %** avant impôt et **3,79 %** après impôt (donnée de l'annexe 1.6). L'obligation notée BB coûte donc 1,05 point de plus avant impôt et 0,78 point de plus après impôt que le crédit.

**Comparaison (1 pt).**

| | Émission obligataire (BB) | Crédit bancaire amortissable | Apport en capital des associés |
|---|---|---|---|
| Horizon | 6 ans, aucun remboursement avant l'échéance : adapté au financement d'installations durables (fluides) | 6 ans, mais 10,00 M€ remboursés chaque année | permanent |
| Coût | le plus élevé de la dette : 6,11 % / 4,57 % (4,89 % / 3,66 % si BBB) | 5,06 % / 3,79 % | pas d'intérêts, pas d'économie d'impôt ; rémunération exigée par les associés plus élevée que celle des prêteurs, car leur risque est plus grand |
| Liquidité | préserve la trésorerie : 3,48 M€ d'intérêts par an, puis 60,00 M€ à refinancer en 2033 (risque de refinancement) | service de la dette de 12,94 M€ la première année, plus de trois fois le flux disponible de 2026 (4,00 M€) : il faudrait réduire les investissements ou se refinancer | améliore la liquidité et les ratios, mais 3,50 M€ au plus |
| Contraintes | note publique à maintenir, information semestrielle des porteurs ; aucune sûreté ; diversifie les prêteurs | hypothèque sur trois entrepôts ; ratio de 2,75 vérifié chaque année, plus strict que l'engagement actuel (marge de 2,75 × 38,00 − 84,00 = 20,50 M€ au lieu de 30,00 M€) ; dépendance accrue envers les banques | répartition du capital inchangée, mais réticence de plusieurs associés de la troisième génération, qui préfèrent un dividende plus élevé |

**Recommandation (1 pt)** (toute recommandation cohérente avec les calculs est acceptée).
- Selon le financement hiérarchique de Myers et Majluf (1984), le groupe, dont l'autofinancement ne couvre plus les investissements, recourt d'abord à la dette ; l'apport en capital vient en dernier [F10 § 3 ; V programme 7.2]. Ici, un **petit apport** a pourtant un effet de levier sur le coût de la dette : avec 3,50 M€, la note passe en BBB (question 1.3), le coupon baisse de 1,20 point et l'économie atteint 0,54 M€ par an après impôt. L'apport est avantageux pour les associés tant que leur rentabilité exigée reste inférieure à 0,54 / 3,50 = 15,43 % par an, sans compter l'élargissement de la base d'investisseurs.
- **Recommandation** : émettre l'obligation de 60 M€ in fine après un apport en capital de 3,50 M€ souscrit par tous les associés au prorata, et mettre en place avant la présentation aux investisseurs le comité d'audit, le plan de succession et un second membre indépendant (question 1.4). Le groupe obtient alors un financement long, sans amortissement ni sûreté, moins coûteux que le crédit bancaire (4,89 % contre 5,06 % avant impôt), et diversifie ses prêteurs. Les fonds économisés sur l'amortissement financent la conversion des entrepôts.
- **Conditions** : conserver des lignes bancaires à court terme ; préparer dès 2030 le refinancement de l'échéance de 2033 ; suivre les ratios de la grille chaque année, car la note BBB est à la limite (2,49 pour un seuil de 2,50) ; présenter aux associés de la troisième génération le gain de l'apport, qui sert aussi la soutenabilité du dividende. La théorie du compromis (Myers, 1977) rappelle qu'au-delà d'un certain endettement les coûts de défaillance dépassent l'avantage fiscal de la dette : la note en est ici la mesure.

**Réponses tolérées** : taux actuariels obtenus par interpolation linéaire (écart de 0,02 point au plus) ; économie d'impôt sur les frais étalée sur la durée, si elle est annoncée (taux après impôt voisins) ; recommandation du crédit bancaire, ou d'un financement mixte (par exemple 40 M€ d'obligations et 20 M€ de crédit), si le candidat traite la charge de remboursement et l'engagement de 2,75 ; recommandation de l'obligation sans apport (note BB), si le surcoût de 0,72 M€ par an est assumé et justifié par le refus des associés.

**Erreurs fréquentes**
- `JUR-T04` — taux actuariel confondu avec le coupon (5,80 %) : les frais augmentent le coût réel ; ou économie d'impôt sur le remboursement du capital, qui n'est pas une charge.
- Comparer le coût de l'obligation avant impôt au coût du crédit après impôt.
- Présenter l'apport en capital comme une ressource gratuite parce qu'il ne verse pas d'intérêts.
- `JUR-T02` — recommandation sans lien avec la note (question 1.3), le score (question 1.4) ou le flux disponible ; `JUR-T14` — choix de financement sans référence aux théories de la structure financière.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 57-58 ; programme l. 465-473 | bilan économique, ROCE, ROE global, part du groupe et des minoritaires, effet de levier, flux de trésorerie, lecture des normes IFRS (substance, juste valeur) sans justification technique | [V] | F04 § 0 à 5 |
| Guide pédagogique DSCG, juillet 2026, p. 60-61 | calcul d'un score à partir d'une grille fournie ; influence de la notation financière sur les conditions de crédit | [V] | F08 § 0 et 3 |
| Guide pédagogique DSCG, juillet 2026, p. 77 et 81-82 | choix d'un support de financement selon l'horizon, le couple rendement-risque et la trésorerie ; comparaison des financements par leur taux actuariel avant et après impôt | [V] | F01 ; F09 § 2.2 |
| Norme IFRS sur les contrats de location | droits d'utilisation, dettes locatives, reclassement des loyers | [S] | F04 § 2 |
| Règlement (UE) 2024/3005 sur les activités de notation ESG, art. 16 et 23 | agrément par l'AEMF, séparation de la notation de crédit, notes E, S et G distinctes | [V] | F08 § 3.2 |
| Agences de notation de crédit (règlement (CE) n° 1060/2009) | enregistrement des agences, opinion sur le risque de défaut | [S] | F08 § 3.1 |
| Modigliani et Miller (1958) | risque financier et rentabilité exigée par les actionnaires | [S] | F10 |
| Jensen et Meckling (1976) | théorie de l'agence, mécanismes de contrôle | [V programme 2.1] | F10 § 3 |
| Freeman (1984) | parties prenantes | [V programme 2.1] | F10 § 3 |
| Myers et Majluf (1984) ; Myers (1977) | financement hiérarchique ; théorie du compromis | [V programme 7.2] | F10 § 3 |
| Taux de swap à 6 ans 3,00 %, grilles de SÉVRANNE Notation et de TALVÉRINE Durabilité, marges par note | hypothèses d'énoncé, plausibles fin 2026 (Euribor 3 mois 2,65 % et taux à 10 ans de la courbe AAA de la zone euro proche de 3,4 % en octobre 2026) | [S] | F11 § 1 |
