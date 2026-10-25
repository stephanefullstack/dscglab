# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Sujet d'entraînement complet n° 2

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue2/fiches/`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (investissement, emprunts, coût du capital, DCF, multiples, portefeuille, LBO, BPA, équilibre des bilans, couvertures, barème sur 50, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Diagnostic financier des comptes consolidés | 17 | 1.1 à 1.6 | `exercices/ex04_diagnostic_consolide` |
| 2 – Investissement et désinvestissement en avenir incertain | 18 | 2.1 à 2.5 | `exercices/ex05_investissement_incertain` |
| 3 – Politique de distribution et lecture du marché | 15 | 3.1 à 3.5 | `exercices/ex06_dividende_marches` |
| **Total** | **50** | | |

---

## DOSSIER 1 – DIAGNOSTIC FINANCIER DES COMPTES CONSOLIDÉS (17 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Bilan économique | `1.c` Apprécier la performance opérationnelle et financière d'un groupe (construire un bilan économique) | 3 |
| 1.2 ROCE et ROE | `1.c` Apprécier la performance opérationnelle et financière d'un groupe | 4 |
| 1.3 Effet de levier | `1.c` Apprécier la performance opérationnelle et financière d'un groupe | 3 |
| 1.4 Contrats de location | `1.b` Interpréter les états financiers des groupes en normes comptables internationales (IFRS) | 2 |
| 1.5 Flux de trésorerie | `1.a` Réaliser une analyse financière des comptes consolidés ; `1.c` (analyse par les flux de trésorerie) | 2 |
| 1.6 Synthèse et recommandations | `1.a` Réaliser une analyse financière des comptes consolidés ; `1.c` | 3 |
| **Total** | | **17** |

---

### 1.1 Bilan économique consolidé (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Bilan économique des comptes publiés 2025 et 2026 : immobilisations 375 / 390, BFR 96 / 110, DFN 168 / 180, égalité à 471 / 500 | 1,5 |
| 1.1-02 | Bilan économique sans droits d'utilisation ni obligations locatives : 443 / 470 | 0,5 |
| 1.1-03 | Commentaire de l'évolution de l'actif économique | 1 |

**Démarche.** Le bilan économique regroupe, à l'actif, les capitaux investis dans l'exploitation (immobilisations et BFR) et, au passif, leur financement par les actionnaires (capitaux propres totaux, minoritaires compris) et par la dette nette de la trésorerie [F04 § 2 ; V guide p. 58].

**Comptes publiés (droits d'utilisation et obligations locatives compris), M€**

| | 2025 | 2026 |
|---|---:|---:|
| Goodwill + autres incorporelles + corporelles | 45 + 15 + 287 = 347,0 | 45 + 15 + 300 = 360,0 |
| Droits d'utilisation | 28,0 | 30,0 |
| **Immobilisations** | **375,0** | **390,0** |
| Stocks + clients + autres créances | 120 + 98 + 14 = 232,0 | 134 + 102 + 14 = 250,0 |
| − Fournisseurs − autres dettes d'exploitation | − 104 − 32 = − 136,0 | − 106 − 34 = − 140,0 |
| **BFR** | **96,0** | **110,0** |
| **Actif économique** | **471,0** | **500,0** |
| Capitaux propres part du groupe + intérêts minoritaires | 281 + 22 = 303,0 | 296 + 24 = 320,0 |
| Emprunts (non courants + courants) | 160 + 25 = 185,0 | 170 + 30 = 200,0 |
| + Obligations locatives | 28,0 | 30,0 |
| − Trésorerie | − 45,0 | − 50,0 |
| **DFN** | **168,0** | **180,0** |
| **Capitaux propres + DFN** | **471,0** | **500,0** |

**Sans droits d'utilisation ni obligations locatives** : on retire 28,0 (2025) et 30,0 (2026) des deux côtés, puisque la note 1 pose droits d'utilisation = obligations locatives.

| | 2025 | 2026 |
|---|---:|---:|
| Immobilisations hors droits d'utilisation | 347,0 | 360,0 |
| BFR | 96,0 | 110,0 |
| **Actif économique** | **443,0** | **470,0** |
| Capitaux propres | 303,0 | 320,0 |
| DFN hors obligations locatives | 140,0 | 150,0 |
| **Capitaux propres + DFN** | **443,0** | **470,0** |

**Commentaire (1 pt).**
- L'actif économique progresse de 29,0 M€ (+ 6,2 %), un peu plus vite que le chiffre d'affaires (+ 5,1 %).
- La hausse vient pour près de la moitié du **BFR** (+ 14,0 M€, + 14,6 %) : il passe de 16,3 % à 17,7 % du chiffre d'affaires, soit de 58,6 à 63,9 jours de chiffre d'affaires. Les stocks représentent à eux seuls 77,8 jours de chiffre d'affaires en 2026, contre 73,2 en 2025 : le renchérissement des matières agricoles et la saisonnalité des campagnes de récolte immobilisent davantage de trésorerie.
- Les immobilisations corporelles augmentent de 13,0 M€ : le groupe investit au-delà du simple renouvellement (question 1.5).
- Ce supplément d'actif est financé par les capitaux propres (+ 17,0 M€, résultat mis en réserve) et par la dette (+ 12,0 M€) : la structure de financement reste stable, autour d'un tiers de dette (180 / 500 = 36 %).

**Réponses tolérées** : BFR présenté en emplois et ressources ; trésorerie portée à l'actif économique si le candidat le dit et en tire une dette brute cohérente (l'égalité doit tenir) ; commentaire limité à 2026.

**Erreurs fréquentes**
- Capitaux propres part du groupe seuls (281 / 296) au lieu des capitaux propres totaux : le bilan ne s'équilibre plus (écart égal aux minoritaires) [F04 § 3].
- Dette brute au lieu de la dette nette, ou obligations locatives oubliées dans la DFN alors que les droits d'utilisation restent à l'actif.
- `JUR-T07` — bilan économique présenté en texte plutôt qu'en tableau ; `JUR-T03` — trésorerie et obligations locatives oubliées parce qu'elles figurent dans des lignes distinctes de l'annexe.

---

### 1.2 Rentabilité économique et rentabilité des capitaux propres (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | ROCE après impôt 9,55 % (2025) et 7,50 % (2026) | 1 |
| 1.2-02 | ROE global 12,77 % et 9,38 % | 0,5 |
| 1.2-03 | ROE part du groupe 12,81 % et 9,12 % ; ROE des minoritaires 12,27 % et 12,50 % | 1 |
| 1.2-04 | Comparaison argumentée au CMPC (8 %) et au coût des capitaux propres (8,5 %) | 1 |
| 1.2-05 | Écart part du groupe / minoritaires expliqué par l'information sectorielle | 0,5 |

**Calculs** (conventions de l'annexe 1.3, montants de clôture, DFN obligations locatives comprises).

| | 2025 | 2026 |
|---|---:|---:|
| ROCE après impôt = RO × 0,75 / actif économique | 60,0 × 0,75 / 471 = 45,0 / 471 = **9,55 %** | 50,0 × 0,75 / 500 = 37,5 / 500 = **7,50 %** |
| ROE global = RN ensemble / CP totaux | 38,7 / 303 = **12,77 %** | 30,0 / 320 = **9,38 %** |
| ROE part du groupe | 36,0 / 281 = **12,81 %** | 27,0 / 296 = **9,12 %** |
| ROE des minoritaires | 2,7 / 22 = **12,27 %** | 3,0 / 24 = **12,50 %** |

**Comparaison au coût du capital (1 pt).**
- La **rentabilité économique** doit être comparée au **CMPC**, coût de l'ensemble des ressources qui financent l'actif économique. En 2025, le ROCE (9,55 %) dépasse le CMPC de 8 % : le groupe crée de la valeur, de l'ordre de (9,55 % − 8 %) × 471 ≈ 7,3 M€. En 2026, le ROCE tombe à 7,50 %, sous le CMPC : l'exploitation ne couvre plus le coût de ses ressources, soit une destruction de valeur d'environ (7,50 % − 8 %) × 500 = − 2,5 M€. Ce raisonnement est celui de l'EVA, facultative en copie [F10, S].
- Le **ROE** se compare au **coût des capitaux propres** (8,5 %). Le ROE part du groupe reste supérieur en 2026 (9,12 %), mais l'écart s'est réduit de 4,31 points à 0,62 point. Il reste positif grâce à l'endettement et non grâce à l'exploitation (question 1.3).
- Les deux exercices montrent un effet ciseau : le chiffre d'affaires progresse de 5,1 %, mais le résultat opérationnel baisse de 16,7 % (marge opérationnelle de 10,2 % à 8,1 %), surtout parce que les achats consommés passent de 46,0 % à 48,4 % du chiffre d'affaires.

**Écart part du groupe / minoritaires (0,5 pt).** Les minoritaires ne détiennent que 30 % de VERDALYS, la filiale la plus rentable : ROE de VERDALYS = 10,0 / 80,0 = 12,5 %, égal au ROE des minoritaires ; ROCE après impôt du secteur des plats végétaux = 14,0 × 0,75 / 90 = **11,67 %**. La part du groupe porte en revanche les secteurs moins rentables : légumes surgelés et conserves (35,6 × 0,75 / 350 = 7,63 %) et surtout ingrédients déshydratés (0,4 × 0,75 / 60 = **0,50 %**). La rentabilité des minoritaires résiste en 2026 (12,27 % → 12,50 %) alors que celle des actionnaires de TERRALBE recule de 3,7 points : la dégradation vient du cœur historique et de la branche à céder, pas des plats végétaux.

**Réponses tolérées** : ROCE avant impôt (12,74 % et 10,00 %) en complément, s'il n'est pas comparé au CMPC ; ROE global 9,375 % ou 9,37 % ; calcul sur actif économique hors obligations locatives (2026 : 48,8 × 0,75 / 470 = 7,79 %) s'il est présenté comme une variante et justifié.

**Erreurs fréquentes**
- Comparer un ROCE **avant** impôt à un CMPC **après** impôt, ou un ROE au CMPC [F04 § 3].
- ROE part du groupe calculé avec le résultat net total, ou ROE global avec les capitaux propres part du groupe (38,7 / 281 = 13,77 % : faux).
- `JUR-T13` — rentabilités calculées sans conclusion sur la création de valeur ni lien avec les secteurs du groupe.

---

### 1.3 Décomposition du ROE et effet de levier (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | Coût net de la dette 3,75 % et 4,17 % ; DFN / CP 0,5545 et 0,5625 | 1 |
| 1.3-02 | Effet de levier 3,22 points et 1,88 point ; ROE = ROCE + levier vérifié | 1 |
| 1.3-03 | Explication de la baisse du ROE et appréciation du risque | 1 |

**Calculs**

| | 2025 | 2026 |
|---|---:|---:|
| Coût net de la dette i = CEFN × 0,75 / DFN | 8,4 × 0,75 / 168 = **3,75 %** | 10,0 × 0,75 / 180 = **4,17 %** |
| Écart ROCE − i | 9,55 − 3,75 = 5,80 points | 7,50 − 4,17 = 3,33 points |
| DFN / capitaux propres | 168 / 303 = **0,5545** | 180 / 320 = **0,5625** |
| Effet de levier (ROCE − i) × DFN / CP | 5,80 × 0,5545 = **3,22 points** | 3,33 × 0,5625 = **1,88 point** |
| ROE = ROCE + effet de levier | 9,55 + 3,22 = **12,77 %** | 7,50 + 1,88 = **9,38 %** |

L'identité est exacte, car le résultat net est égal au résultat opérationnel diminué du coût de l'endettement, l'ensemble après impôt à 25 %, sans autre élément.

**Explication et risque (1 pt).**
- Le ROE perd 3,40 points sur valeurs non arrondies (3,39 sur valeurs arrondies : 12,77 − 9,38). La baisse de la rentabilité économique en explique 2,05 points et celle de l'effet de levier 1,34 point.
- L'effet de levier diminue alors que le taux d'endettement est presque stable (0,55 à 0,56) : c'est l'**écart ROCE − i** qui se resserre, de 5,80 à 3,33 points, sous le double effet de la baisse du ROCE et de la hausse du coût net de la dette (3,75 % à 4,17 %).
- Le levier reste favorable (ROCE > i) mais il **amplifie** la baisse : le ROE recule de 3,40 points pour un recul de 2,05 points du ROCE. Si le ROCE tombait sous 4,17 %, le levier deviendrait défavorable (effet de massue) et l'endettement réduirait le ROE.
- En 2026, l'essentiel du ROE vient de l'exploitation (7,50 points sur 9,38) ; la dette n'ajoute que 1,88 point. Selon Modigliani et Miller (1958), la hausse du ROE permise par la dette ne crée pas de valeur par elle-même en marché parfait : elle rémunère un **risque financier** plus élevé, qui accroît la rentabilité exigée par les actionnaires [F10, S]. Le ROE de 9,38 %, juste supérieur au coût des capitaux propres de 8,5 %, ne doit donc pas masquer un ROCE devenu inférieur au CMPC.
- Recommandation : ne pas compter sur un endettement supplémentaire pour soutenir le ROE ; restaurer d'abord la rentabilité économique (marge, BFR, branche peu rentable).

**Réponses tolérées** : calcul de l'effet de levier avec des taux arrondis (2026 : 3,33 × 0,5625 = 1,87 ; ROE 9,37 %) ; DFN / CP arrondi à deux décimales (0,55 et 0,56 : levier 3,19 et 1,86 point), si l'écart avec le ROE observé est signalé et attribué à l'arrondi ; décomposition de la baisse présentée sans chiffrage, si le resserrement de l'écart ROCE − i est expliqué.

**Erreurs fréquentes**
- Coût de la dette avant impôt (10,0 / 180 = 5,56 %) combiné à un ROCE après impôt : l'identité ne tombe plus juste.
- Levier calculé avec la dette brute (230 M€ en 2026) ou avec les capitaux propres part du groupe [F04 § 3].
- `JUR-T14` — effet de levier présenté comme une création de valeur, sans le risque financier qui l'accompagne.

---

### 1.4 Effet de la norme sur les contrats de location (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | EBITDA 74,4 / 67,2 ; DFN 180 / 150 ; DFN / EBITDA 2,42 / 2,23 ; gearing 56,25 % / 46,88 % | 1 |
| 1.4-02 | Lecture retenue pour la clause bancaire et pour la comparaison sectorielle | 1 |

**Effets sur les indicateurs de 2026**

| 2026 | Comptes publiés | Sans effet de la norme | Effet de la norme |
|---|---:|---:|---:|
| EBITDA | 74,4 | 74,4 − 7,2 = 67,2 | + 7,2 (+ 10,7 %) |
| Marge d'EBITDA | 12,00 % | 10,84 % | + 1,16 point |
| DFN | 180,0 | 150,0 | + 30,0 |
| DFN / EBITDA | 180 / 74,4 = **2,42** | 150 / 67,2 = **2,23** | + 0,19 |
| Gearing (DFN / CP) | 180 / 320 = **56,25 %** | 150 / 320 = **46,88 %** | + 9,38 points |

**Lecture (1 pt).**
- La norme traite la location comme un **financement** de l'actif loué : primauté de la substance sur la forme. Les loyers sortent des charges externes ; ils sont remplacés par un amortissement (sous l'EBITDA) et des intérêts. L'EBITDA augmente donc de 7,2 M€ et la dette de 30,0 M€, sans aucun changement de l'activité ni de la trésorerie [F04 § 2 ; V guide p. 58].
- Le ratio DFN / EBITDA bouge peu (+ 0,19), car le numérateur et le dénominateur augmentent ensemble ; le gearing, lui, augmente de 9,4 points, car les capitaux propres ne changent pas.
- **Clause bancaire** : le contrat définit le ratio hors effet de la norme. C'est donc la lecture à retenir : 2,23 ≤ 3,0, la clause est respectée. La marge de sécurité est réelle sans être large : à dette constante, l'EBITDA hors norme pourrait baisser jusqu'à 150 / 3 = 50,0 M€, soit une baisse de 17,2 M€ (− 25,6 %) ; à EBITDA constant, la dette pourrait augmenter de 3 × 67,2 − 150 = 51,6 M€. Ce montant borne le financement par dette de l'usine de plats végétaux.
- **Comparaison sectorielle** : le panel est calculé obligations locatives comprises (annexe 1.4) ; il faut donc le comparer aux comptes publiés (2,42 contre 2,50 ; 56,25 % contre 60 %). Mélanger les deux lectures fausse la comparaison.

**Réponses tolérées** : effet de la norme sur la marge d'EBITDA non chiffré ; lecture de la clause qui mentionne aussi le seuil d'alerte bancaire usuel de 3 fois l'EBITDA [F04 § 4].

**Erreurs fréquentes**
- Conclure que la norme améliore la rentabilité ou la capacité de remboursement : elle ne change ni les flux ni le risque, seulement leur présentation.
- Tester la clause sur le ratio des comptes publiés (2,42), sans lire la définition contractuelle.
- Exposer les critères comptables de la norme : la question porte sur l'interprétation, la justification technique relève de l'UE 4.

---

### 1.5 Analyse des flux de trésorerie (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | CAF 61,3 / 54,4 ; variation du BFR 4,0 / 14,0 ; flux de trésorerie disponible 24,8 / 3,0 | 1 |
| 1.5-02 | Analyse des emplois et du financement des dividendes | 1 |

**Calculs (M€)**

| | 2025 | 2026 |
|---|---:|---:|
| CAF = RN ensemble + dotations | 38,7 + 22,6 = **61,3** | 30,0 + 24,4 = **54,4** |
| CAF / chiffre d'affaires | 10,39 % | 8,77 % |
| − Variation du BFR | − 4,0 | − **14,0** |
| = Flux net lié à l'activité | 57,3 | 40,4 |
| − Acquisitions d'immobilisations | − 27,0 | − 31,4 |
| − Remboursements des obligations locatives | − 5,5 | − 6,0 |
| = **Flux de trésorerie disponible** | **24,8** | **3,0** |
| Flux disponible / chiffre d'affaires | 4,20 % | 0,48 % |
| − Dividendes versés (TERRALBE + minoritaires) | − 11,8 | − 13,0 |
| = Flux après dividendes | + 13,0 | − **10,0** |
| Variation de la DFN hors obligations locatives (35,0 − 20,0 d'emprunts nets − 5,0 de trésorerie en 2026) | − 13,0 | + 10,0 |

**Analyse (1 pt).**
- La CAF baisse de 6,9 M€ avec le résultat. La hausse du BFR (14,0 M€, contre 4,0 en 2025) en absorbe plus du quart : le flux lié à l'activité recule de 30 % (57,3 à 40,4).
- Les investissements (31,4 M€) représentent 1,71 fois les dotations aux amortissements hors droits d'utilisation (24,4 − 6,0 = 18,4 M€) : le groupe investit pour sa croissance, pas seulement pour renouveler son outil.
- Le flux de trésorerie disponible s'effondre de 24,8 à 3,0 M€ (0,5 % du chiffre d'affaires, contre 3,0 % pour le panel). En 2025, il couvrait deux fois les dividendes et permettait de réduire la dette de 13,0 M€. En 2026, il ne couvre plus les 13,0 M€ de dividendes : **le dividende est financé par l'endettement** (+ 10,0 M€ de DFN).
- Un dividende de 1,20 € maintenu sur le résultat de 2026 représenterait 1,20 / 2,70 = 44 % du résultat par action, contre 33 % au titre de 2025. La politique de distribution n'est soutenable que si le flux disponible se redresse.
- Lecture théorique : selon le financement hiérarchique de Myers et Majluf (1984), l'entreprise finance d'abord ses besoins par l'autofinancement, puis par la dette. TERRALBE a déjà épuisé son autofinancement en 2026 ; l'usine de plats végétaux devra donc être financée par la dette, une cession ou des fonds propres [F10, V programme 7.2].

**Réponses tolérées** : flux de trésorerie disponible avant remboursement des obligations locatives (9,0 M€ en 2026, 30,3 en 2025), si le candidat le signale et compare de manière cohérente ; analyse en emplois et ressources.

**Erreurs fréquentes**
- Confondre la CAF et le flux lié à l'activité (oubli de la variation du BFR) [F04 § 5].
- Soustraire le BFR total (110,0) au lieu de sa variation (14,0).
- `JUR-T07` — flux commentés sans tableau ; `JUR-T13` — description ligne à ligne sans conclusion sur la couverture des dividendes.

---

### 1.6 Synthèse pour le comité d'audit (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.6-01 | Forces et faiblesses hiérarchisées, chiffrées et comparées au panel | 1 |
| 1.6-02 | Zones de risque identifiées | 1 |
| 1.6-03 | Deux recommandations argumentées, liées à « Horizon 2030 » | 1 |

**Grille** : 1 point par item quand la réponse s'appuie sur des chiffres du cas et du panel ; 0,5 point pour une liste juste mais non chiffrée ou non hiérarchisée ; 0 pour une réponse générale sans lien avec TERRALBE (`JUR-T13`).

**Positionnement de TERRALBE en 2026**

| Indicateur | TERRALBE 2026 | Panel | Lecture |
|---|---:|---:|---|
| Croissance du chiffre d'affaires | 5,1 % | 4,0 % | force |
| Marge d'EBITDA | 12,0 % | 13,0 % | faiblesse (14,0 % en 2025) |
| ROCE après impôt | 7,50 % | 9,0 % | faiblesse, sous le CMPC |
| ROE global | 9,38 % | 10,5 % | faiblesse |
| DFN / EBITDA | 2,42 | 2,50 | correct |
| Gearing | 56,25 % | 60,0 % | correct |
| BFR / chiffre d'affaires | 17,7 % | 15,0 % | faiblesse |
| Flux disponible / chiffre d'affaires | 0,5 % | 3,0 % | faiblesse majeure |

**Forces.** Une croissance supérieure à celle du secteur (+ 5,1 % contre 4,0 %) ; une structure financière encore saine, légèrement moins endettée que le panel, avec une clause bancaire respectée (2,23 contre 3,0) ; une filiale de croissance rentable, VERDALYS (ROCE de 11,67 %, marge d'EBITDA de 14,5 %), qui porte la stratégie des plats végétaux.

**Faiblesses.** Une profitabilité en recul et inférieure au secteur (marge d'EBITDA de 12,0 % contre 13,0 %, sous l'effet du coût des achats) ; une rentabilité économique passée sous le CMPC (7,50 % contre 8 %) et inférieure au panel ; un BFR lourd (17,7 % du chiffre d'affaires contre 15,0 %) ; un flux de trésorerie disponible presque nul.

**Zones de risque.**
- Le **dividende est financé par la dette** : situation non durable si les marges ne se redressent pas.
- Le **levier se resserre** (écart ROCE − i de 3,33 points) ; une nouvelle baisse du ROCE ou une hausse des taux réduiraient encore le ROE.
- La branche « ingrédients déshydratés » ne rapporte presque rien (ROCE de 0,50 %) et son goodwill de 12,0 M€ n'est couvert qu'avec une marge de 2,0 M€ : une **dépréciation** ou une moins-value de cession est possible.
- L'**exposition aux coûts agricoles et climatiques** pèse sur la marge et sur les stocks ; une part de la rentabilité de VERDALYS revient aux minoritaires (30 %).
- Le financement de l'usine par la dette est **borné** par la clause bancaire (environ 51,6 M€ de dette supplémentaire à EBITDA constant).

**Recommandations (deux attendues).**
1. **Céder la branche « ingrédients déshydratés »** : elle immobilise 60 M€ d'actif économique pour un ROCE de 0,50 %. Sans elle, le ROCE du groupe serait de (37,5 − 0,3) / 440 = 8,45 %, de nouveau supérieur au CMPC. Le produit de cession peut réduire la dette ou financer l'usine. Il faut cependant anticiper l'effet sur le résultat d'un prix inférieur à la valeur comptable.
2. **Réduire le BFR** : ramener le BFR à 15 % du chiffre d'affaires libérerait 110,0 − 0,15 × 620 = 17,0 M€, par la gestion des stocks de campagne et des délais clients. Ce montant équivaut à plus de cinq fois le flux disponible de 2026.
3. Autres recommandations admises : **aligner la distribution sur le flux disponible** (ne plus financer le dividende par la dette, ce que le conseil doit trancher avant l'assemblée de juin 2027) ; **financer l'usine** en préservant la marge de la clause bancaire (financement mixte : dette, produit de cession, autofinancement), conformément à la hiérarchie des financements de Myers et Majluf (1984) ; **restaurer la marge** (indexation des prix d'achat, contrats avec les producteurs, couverture de l'énergie).

**Réponses tolérées** : toute recommandation cohérente appuyée sur un chiffre du cas ; recommandation d'une croissance de VERDALYS, y compris par le rachat des minoritaires, si le candidat en mesure l'enjeu (3,0 M€ de résultat revenant aux minoritaires) sans le chiffrer davantage.

**Erreurs fréquentes**
- `JUR-T13` — synthèse générale (« le groupe doit améliorer sa rentabilité ») sans chiffre du cas ni comparaison au panel.
- `JUR-T02` — forces et faiblesses énumérées sans hiérarchie ni recommandation.
- Attribuer la croissance à un changement de périmètre : le périmètre est constant, la croissance est organique.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 57-58 | bilan économique, ROCE, ROE global, part du groupe et des minoritaires, effet de levier, lecture des normes IFRS, démarche de diagnostic | [V] | F04 § 0 |
| Corrigé du sujet zéro, p. 104 | seuil d'alerte bancaire de 3 fois l'EBITDA pour la dette nette | [V] | F04 § 4 |
| Norme IFRS sur les contrats de location | droits d'utilisation, obligations locatives, reclassement des loyers | [S] | F04 § 2 |
| Modigliani et Miller (1958) | neutralité de la structure financière, risque financier et rentabilité exigée | [S] | F10 |
| Myers et Majluf (1984) | financement hiérarchique : autofinancement, puis dette, puis actions | [V programme] | F10 |
| EVA (Stern Stewart, 1991) | création de valeur = (ROCE − CMPC) × capitaux investis | [S, facultatif] | F10 |

---

## DOSSIER 2 – INVESTISSEMENT ET DÉSINVESTISSEMENT EN AVENIR INCERTAIN (18 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Flux, VAN, TRI et indice de profitabilité | `7.1.a` Évaluer et classer des projets en milieu certain | 5 |
| 2.2 VAN probabilisée et risque | `7.1.b` Évaluer et classer des projets en milieu incertain ; `5.2.a` Identifier la relation entre incertitude et rentabilité exigée | 4 |
| 2.3 Arbre de décision | `7.1.b` Évaluer et classer des projets en milieu incertain | 3 |
| 2.4 Conserver ou céder la branche | `7.1.c` Déterminer la création de valeur d'un désinvestissement | 3 |
| 2.5 Recommandation au conseil | `7.1.a`, `7.1.b`, `7.1.c` | 3 |
| **Total** | | **18** |

Part du calcul : environ 12 points (2.1 ; 2.2 sans la lecture du risque ; 2.3 et 2.4 sans la comparaison et l'interprétation). Part de l'analyse : environ 6 points.

---

### 2.1 Flux, VAN, TRI et indice de profitabilité du projet en une tranche (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Flux d'exploitation des années 1 à 5 : EBITDA 14 600, dotations 8 400, résultat d'exploitation 6 200, IS 1 550, flux 13 050 | 1,5 |
| 2.1-02 | Flux de la date 0 (− 48 000 : équipements et BFR) et de l'année 5 (22 800 : BFR récupéré et revente nette d'impôt de 3 750) | 1 |
| 2.1-03 | VAN au CMPC de 8 % : 10 741 k€ | 1 |
| 2.1-04 | TRI ≈ 15,48 % (15,47 % à 15,49 % par interpolation entre deux taux entiers) | 1 |
| 2.1-05 | Indice de profitabilité 1,22 et conclusion | 0,5 |

**Conventions rappelées** (annexe 2.1) : date 0 au 31/12/2027 ; flux en fin d'année ; IS de 25 % sur le résultat d'exploitation, sans frais financiers ; taux d'actualisation de 8 % ; indice de profitabilité = flux actualisés des années 1 à 5 / décaissement de la date 0 ; montants au k€, taux à deux décimales.

**Tableau des flux, scénario central (12 000 t), k€**

| | Date 0 | Années 1 à 4 | Année 5 |
|---|---:|---:|---:|
| Chiffre d'affaires (12 000 t × 5 000 €) | | 60 000 | 60 000 |
| − Coûts variables (12 000 t × 3 200 €) | | − 38 400 | − 38 400 |
| − Charges fixes décaissées | | − 7 000 | − 7 000 |
| **= EBITDA** | | **14 600** | **14 600** |
| − Dotations aux amortissements (42 000 / 5) | | − 8 400 | − 8 400 |
| = Résultat d'exploitation | | 6 200 | 6 200 |
| − IS à 25 % | | − 1 550 | − 1 550 |
| = Résultat d'exploitation après impôt | | 4 650 | 4 650 |
| + Dotations aux amortissements | | 8 400 | 8 400 |
| = Flux d'exploitation (CAF d'exploitation) | | 13 050 | 13 050 |
| − Équipements | − 42 000 | | |
| − BFR constitué / + BFR récupéré | − 6 000 | | + 6 000 |
| + Revente des équipements nette d'impôt (5 000 × 0,75) | | | + 3 750 |
| **= Flux net de trésorerie** | **− 48 000** | **13 050** | **22 800** |
| Coefficient d'actualisation (1,08^−t) | 1 | 0,9259 ; 0,8573 ; 0,7938 ; 0,7350 | 0,6806 |
| Flux actualisé | − 48 000 | 12 083 ; 11 188 ; 10 360 ; 9 592 | 15 517 |

Les équipements étant totalement amortis en fin d'année 5, leur valeur nette comptable est nulle : la plus-value égale le prix de revente, d'où un impôt de 5 000 × 25 % = 1 250 et une revente nette de 3 750.

**VAN (1 pt)** = − 48 000 + 13 050 × [1 − 1,08^−5] / 0,08 + (6 000 + 3 750) × 1,08^−5 = − 48 000 + 13 050 × 3,9927 + 9 750 × 0,6806 = − 48 000 + 52 105 + 6 636 = **10 741 k€**.

**TRI (1 pt).** VAN à 15 % = + 593 k€ ; VAN à 16 % = − 628 k€. Par interpolation linéaire : 15 % + 1 % × 593 / (593 + 628) = **15,49 %** ; la valeur exacte est **15,48 %**. Entre 14 % (VAN + 1 866) et 15 %, l'interpolation donne 15,47 %.

**Indice de profitabilité (0,5 pt)** = 58 741 / 48 000 = **1,22** : chaque euro investi (équipements et BFR) restitue 1,22 € en valeur actuelle.

**Conclusion.** Dans le scénario central, le projet crée de la valeur : VAN de 10,7 M€, TRI de 15,48 %, supérieur au CMPC de 8 % de près de 7,5 points. Le délai de récupération actualisé est de 4,31 ans pour une durée de 5 ans : la marge est étroite, car une part du flux de l'année 5 vient de la récupération du BFR et de la revente (calcul facultatif ; délai simple : 3,68 ans). Ce résultat repose sur un seul scénario : il faut l'éprouver sur les autres niveaux de demande (question 2.2).

**Réponses tolérées** : flux présentés en CAF puis variation du BFR (même résultat) ; EBITDA appelé EBE ; TRI compris entre 15,45 % et 15,50 % selon les taux d'interpolation ; VAN à ± 5 k€ selon l'arrondi des coefficients (10 739 avec des coefficients à quatre décimales) ; indice de profitabilité calculé comme 1 + VAN / 48 000 ; BFR présenté en début d'année 1 (assimilé à la date 0).

**Erreurs fréquentes**
- `JUR-T04` — VAN et TRI sont des acquis du DCG exigibles : oubli de la récupération du BFR ou de la valeur résiduelle en année 5, revente prise brute (5 000) au lieu de nette d'impôt (3 750), investissement actualisé.
- IS calculé sur l'EBITDA (14 600 × 25 % = 3 650) au lieu du résultat d'exploitation, ou dotations non réintégrées : flux de 10 950 ou de 4 650, faux.
- Frais financiers déduits des flux alors que le taux d'actualisation (CMPC) rémunère déjà les prêteurs : double comptage.
- Indice de profitabilité calculé sur les seuls équipements (58 741 / 42 000 = 1,40) alors que l'annexe inclut le BFR.
- `JUR-T07` — flux présentés sans tableau.

---

### 2.2 VAN probabilisée et risque du projet (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | VAN demande faible − 5 430 k€ ; VAN demande forte 21 521 k€ | 1 |
| 2.2-02 | Espérance de la VAN : 9 393 k€ | 0,5 |
| 2.2-03 | Écart-type de la VAN : 9 623 k€ (variance pondérée par les probabilités) | 1 |
| 2.2-04 | Coefficient de variation 1,02 ; probabilité de VAN négative 25 % | 0,5 |
| 2.2-05 | Appréciation du risque et prise en compte par le taux d'actualisation | 1 |

**VAN des scénarios (1 pt).** Seul le volume change ; date 0 (− 48 000) et éléments de l'année 5 (+ 9 750) identiques.

| k€ | Faible (9 000 t) | Centrale (12 000 t) | Forte (14 000 t) |
|---|---:|---:|---:|
| EBITDA = volume × 1 800 € − 7 000 | 9 200 | 14 600 | 18 200 |
| Résultat d'exploitation (− 8 400) | 800 | 6 200 | 9 800 |
| IS à 25 % | 200 | 1 550 | 2 450 |
| Flux d'exploitation des années 1 à 5 | 9 000 | 13 050 | 15 750 |
| Flux × 3,9927 | 35 934 | 52 105 | 62 885 |
| + 9 750 × 0,6806 − 48 000 | − 41 364 | − 41 364 | − 41 364 |
| **VAN** | **− 5 430** | **10 741** | **21 521** |

Raccourci accepté : 1 000 tonnes de plus ou de moins font varier le flux annuel de 1 000 × 1 800 € × 0,75 = 1 350 k€, et la VAN de 1 350 × 3,9927 = 5 390 k€. D'où 10 741 − 3 × 5 390 = − 5 430 et 10 741 + 2 × 5 390 = 21 521.

**Espérance, écart-type, coefficient de variation (2 pts)**

| Scénario | Probabilité p | VAN | p × VAN | Écart à E(VAN) | p × écart² |
|---|---:|---:|---:|---:|---:|
| Faible | 0,25 | − 5 430 | − 1 357 | − 14 823 | 54 929 858 |
| Centrale | 0,50 | 10 741 | 5 370 | 1 348 | 907 932 |
| Forte | 0,25 | 21 521 | 5 380 | 12 128 | 36 771 227 |
| **Total** | **1** | | **E(VAN) = 9 393** | | **V(VAN) = 92 609 017** |

- **E(VAN) = 9 393 k€** ; **σ(VAN) = √92 609 017 = 9 623 k€** ; **coefficient de variation = 9 623 / 9 393 = 1,02**.
- **Probabilité de VAN négative = 25 %**, lue directement sur les scénarios : seul le scénario de demande faible a une VAN négative. Elle ne se calcule pas à partir de l'écart-type.

**Appréciation du risque et taux d'actualisation (1 pt).**
- Le projet crée de la valeur **en espérance** (9,4 M€), mais son risque est élevé : l'écart-type est du même ordre que l'espérance (coefficient de variation supérieur à 1) et une fois sur quatre, le projet détruit 5,4 M€. La VAN s'annule pour un volume d'environ 10 000 tonnes, soit 17 % sous le scénario central (calcul facultatif : 12 000 − 10 741 / 5,390) : la marge de sécurité est faible.
- Ce risque est supérieur à celui des activités historiques : la demande de plats végétaux est plus sensible à la conjoncture et aux modes de consommation. Le marché le confirme : le bêta des fabricants cotés de plats végétaux est de 1,30, contre 0,90 pour TERRALBE.
- **Lien entre risque et rentabilité exigée** : selon le MEDAF (Sharpe, 1964), la rentabilité exigée des capitaux propres d'un projet dépend de son risque systématique. Elle serait de 4 % + 1,30 × 5 % = **10,5 %** pour les plats végétaux, contre 4 % + 0,90 × 5 % = 8,5 % pour TERRALBE. Actualiser au CMPC du groupe (8 %) revient à traiter l'usine comme un actif aussi risqué que les légumes surgelés : cela surestime la VAN. Le projet devrait être actualisé à un **taux propre au projet**, supérieur à 8 % : un CMPC calculé avec le coût des fonds propres du secteur (10,5 %, les comparables ayant un endettement comparable à celui du groupe) et le coût de la dette après impôt. À titre d'illustration, même au taux de 10,5 %, majorant de ce CMPC, la VAN centrale resterait de 6 763 k€ (minorant) ; le TRI des flux espérés (14,56 %) lui est supérieur.
- **Deux approches à ne pas cumuler** : le risque est pris en compte soit par le taux (flux espérés actualisés à un taux ajusté au risque), soit par la dispersion de la VAN (scénarios, écart-type) au taux de base. Majorer le taux **et** retenir le scénario pessimiste pénaliserait deux fois le projet.
- **Nuance** : l'écart-type de la VAN mesure le risque **total** du projet. Selon Markowitz (1952), le risque spécifique se réduit par la diversification ; selon le MEDAF, seul le risque systématique est rémunéré par le marché. Les actionnaires du public (43 %) sont diversifiés. LESTRADEC Participations (54 %) concentre en revanche son patrimoine sur TERRALBE : pour elle, le risque total compte aussi.

**Réponses tolérées** : variance calculée avec les VAN arrondies (même résultat au k€ près) ; coefficient de variation 1,02 ou 102 % ; lecture du taux ajusté sans calcul du ke à 10,5 %, si le lien risque systématique / rentabilité exigée est expliqué ; autre méthode cohérente de prise en compte du risque, si elle est présentée sans calcul complexe.

**Erreurs fréquentes**
- Variance divisée par n ou n − 1 alors que l'énoncé fournit des **probabilités** : 92 609 017 seulement si les écarts sont pondérés par p [F01 § 5].
- Écart-type confondu avec la variance, ou exprimé en pourcentage.
- Probabilité de VAN négative calculée par une formule ou une table : hors programme et inutile, elle se lit sur les scénarios.
- `JUR-T13` — espérance et écart-type calculés sans conclusion sur le niveau de risque ni lien avec le cas.
- `JUR-T14` — affirmer que le marché rémunère tout le risque du projet, sans distinguer risque systématique et risque spécifique.

---

### 2.3 Construction en deux tranches : arbre de décision (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Arbre et valeurs en fin d'année 2 : sans extension 29 236 ; avec extension 27 724 (demande centrale) et 34 682 (demande forte) | 1 |
| 2.3-02 | Décisions (étendre seulement si la demande est forte), valeur espérée en fin d'année 2 de 30 598, VAN espérée de la stratégie de 8 050 k€ | 1 |
| 2.3-03 | Comparaison avec la construction en une tranche, en espérance et en risque | 1 |

**Arbre de décision** (■ décision, ○ événement ; valeurs en fin d'année 2, k€)

```
Date 0 ■ Tranche 1 : − 34 500 ; flux certains de 9 150 en années 1 et 2
   └── Fin d'année 2 ○ demande observée
         ├── faible (25 %)   ■ ne pas étendre ............................. 29 236
         ├── centrale (50 %) ■ ┬ étendre : − 15 000 + flux 13 575 ; 13 575 ; 23 325 ... 27 724
         │                     └ ne pas étendre ............................ 29 236  ← retenu
         └── forte (25 %)    ■ ┬ étendre : − 15 000 + flux 16 275 ; 16 275 ; 26 025 ... 34 682  ← retenu
                               └ ne pas étendre ............................ 29 236
```

**Valeurs en fin d'année 2 (1 pt)**, actualisées sur les années 3 à 5 [facteur sur trois ans : (1 − 1,08^−3) / 0,08 = 2,5771 ; 1,08^−3 = 0,7938] :
- sans extension : 9 150 × 2,5771 + 7 125 × 0,7938 = 23 580 + 5 656 = **29 236** ;
- avec extension, demande centrale : − 15 000 + 13 575 × 2,5771 + 9 750 × 0,7938 = − 15 000 + 34 984 + 7 740 = **27 724** ;
- avec extension, demande forte : − 15 000 + 16 275 × 2,5771 + 7 740 = − 15 000 + 41 942 + 7 740 = **34 682**.

**Décisions et VAN espérée (1 pt).** On remonte l'arbre de droite à gauche :
- demande faible : ne pas étendre (29 236) ;
- demande centrale : **ne pas étendre**, car l'extension détruirait 29 236 − 27 724 = 1 513 k€ : les 3 000 tonnes supplémentaires ne sont vendues que pendant trois ans, ce qui ne suffit pas à amortir 15 000 k€ ;
- demande forte : **étendre** (+ 5 446 k€).

Valeur espérée en fin d'année 2 = 0,25 × 29 236 + 0,50 × 29 236 + 0,25 × 34 682 = **30 598**.
VAN avant décision = − 34 500 + 9 150 × (0,9259 + 0,8573) = − 34 500 + 16 317 = − 18 183.
**VAN espérée de la stratégie = − 18 183 + 30 598 × 1,08^−2 = − 18 183 + 26 233 = 8 050 k€.**

**Comparaison avec la construction en une tranche (1 pt)**

| k€ | Une tranche | Deux tranches (stratégie optimale) |
|---|---:|---:|
| VAN espérée | 9 393 | 8 050 |
| VAN si la demande est faible | − 5 430 | 6 882 |
| VAN si la demande est centrale | 10 741 | 6 882 |
| VAN si la demande est forte | 21 521 | 11 551 |
| Écart-type de la VAN | 9 623 | 2 022 |
| Probabilité de VAN négative | 25 % | 0 % |
| Décaissement à la date 0 | 48 000 | 34 500 |

- **En espérance**, la construction en une tranche est préférable (+ 1 343 k€) : la tranche 1 plafonne les ventes à 9 000 tonnes pendant deux ans, puis en cas de demande centrale, et l'extension coûte plus cher (13 500 + 30 000 = 43 500 contre 42 000).
- **En risque**, la construction en deux tranches est nettement meilleure : aucune VAN négative, un écart-type divisé par près de cinq, un engagement initial réduit de 13 500 k€. La **flexibilité** de la décision d'extension, prise après observation de la demande, protège contre le scénario faible.
- **Calculer chaque branche est nécessaire** : la règle « étendre dès que la demande dépasse la capacité de la tranche 1 » (demandes centrale et forte) donnerait une VAN espérée de 7 401 k€ seulement, soit 648 k€ de moins que la stratégie optimale.
- **Conclusion** : les deux variantes, mutuellement exclusives, ont une VAN positive. Le choix dépend de l'aversion au risque du groupe : renoncer à 1,3 M€ de VAN espérée (14 %) pour supprimer le risque de destruction de valeur. Pour un groupe dont les marges baissent et dont l'actionnaire de contrôle est peu diversifié, la construction en deux tranches est défendable (question 2.5).

**Réponses tolérées** : arbre présenté sous forme de tableau ; valeurs actualisées directement à la date 0 (VAN par état : 6 882 / 6 882 / 11 551, puis espérance 8 050) ; écart-type de la variante (2 022) non calculé si la comparaison du risque s'appuie sur les VAN par état ; écarts de quelques k€ dus aux arrondis.

**Erreurs fréquentes**
- Calculer l'espérance des valeurs de **toutes** les branches, au lieu de retenir dans chaque état la **meilleure** décision.
- Actualiser les flux des années 3 à 5 sur 3, 4 et 5 ans **et** actualiser ensuite la valeur en fin d'année 2 : double actualisation.
- Oublier le décaissement de l'extension (15 000) ou la VAN des années 1 et 2.
- `JUR-I05` — comparer deux variantes mutuellement exclusives sur le seul critère de l'espérance, sans analyser ce qui les départage ici (le risque).

---

### 2.4 Branche « ingrédients déshydratés » : conserver ou céder (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Valeur de conservation : flux actualisés 14 398 + valeur de 2032 actualisée 37 432 = 51 830 k€ | 1 |
| 2.4-02 | Produit net de cession 59 500 k€ ; création de valeur de la cession 7 670 k€ | 1 |
| 2.4-03 | Conclusion et explication de l'écart de valeur entre acquéreur et cédant | 1 |

**Valeur de la branche conservée (1 pt)**, à la date 0 (31/12/2027), au taux de 8 % :

| k€ | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|
| Flux de trésorerie disponibles | 2 000 | 3 500 | 4 000 | 4 500 | 4 500 |
| Valeur de la branche fin 2032 | | | | | 55 000 |
| Coefficient d'actualisation | 0,9259 | 0,8573 | 0,7938 | 0,7350 | 0,6806 |
| Flux actualisés | 1 852 | 3 001 | 3 175 | 3 308 | 3 063 + 37 432 |

Valeur de conservation = 14 398 + 37 432 = **51 830 k€**. La valeur de 2032 en représente 72 % : le résultat dépend surtout de la réussite du plan de redressement au-delà de 2032.

**Produit net de cession (1 pt)** = 63 500 − 1 500 − 2 500 = **59 500 k€**, encaissé à la date 0.

**Création de valeur de la cession** = 59 500 − 51 830 = **+ 7 670 k€**. De manière équivalente, conserver la branche revient à « investir » 59 500 k€, le produit de cession auquel on renonce, pour recevoir les flux de la branche : VAN de − 7 670 k€ et TRI de 4,75 %, inférieur au CMPC de 8 %.

**Conclusion et interprétation (1 pt).**
- La cession crée de la valeur pour les actionnaires de TERRALBE : elle procure aujourd'hui, nets de frais et d'impôt, 14,8 % de plus que ce que la branche rapporterait au groupe.
- La comparaison se fait avec la **valeur de conservation** (flux futurs auxquels le groupe renonce, ou « flux évités »), non avec la valeur comptable de la branche ni avec son seul résultat de cession.
- **Pourquoi l'acquéreur paie plus** : (1) il prévoit de regrouper la production avec celle de ses usines, d'où des **synergies** (économies d'échelle, réduction des coûts fixes et énergétiques, réseau commercial) que TERRALBE ne peut pas obtenir seule ; (2) spécialiste des ingrédients, il peut évaluer le risque de la branche plus favorablement et l'actualiser à un taux plus faible ; (3) la branche n'est pas stratégique pour TERRALBE, qui y consacrerait des ressources rares (capitaux, attention de la direction). Le prix partage ces synergies entre acheteur et vendeur.
- **Vigilance** : l'avantage de la cession repose sur une offre qui devra être confirmée (conditions suspensives, garanties demandées par l'acquéreur), et sur un plan de redressement que le cédant pourrait juger trop prudent. À l'inverse, si ce plan est optimiste, l'avantage de la cession est plus grand encore.

**Réponses tolérées** : valeur de conservation à quelques k€ près ; comparaison présentée comme une VAN différentielle (VAN de la cession = + 7 670) ; mention de la perte des éventuels liens commerciaux avec le reste du groupe, à condition de l'avancer comme une hypothèse.

**Erreurs fréquentes**
- Oublier la valeur de 2032 (valeur de conservation de 14 398 seulement) : la cession paraît alors créer 45 M€ de valeur.
- Comparer le prix brut (63 500) à la valeur de conservation, sans déduire les coûts de sortie et l'impôt.
- Actualiser le produit de cession, alors qu'il est encaissé à la date 0.
- `JUR-T13` — conclure sans expliquer l'écart de valeur entre l'acheteur et le vendeur.

---

### 2.5 Recommandation au conseil d'administration (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Décision sur l'usine (une ou deux tranches), justifiée par la création de valeur et le risque, chiffres à l'appui | 1 |
| 2.5-02 | Décision sur la branche et cohérence avec « Horizon 2030 » (recentrage, financement de l'usine) | 1 |
| 2.5-03 | Limites des critères utilisés et éléments non financiers | 1 |

**Grille** : 1 point par item quand la réponse s'appuie sur des chiffres du dossier et prend position ; 0,5 point pour une réponse juste mais générale ou non chiffrée ; 0 pour une réponse sans lien avec TERRALBE (`JUR-T13`). Une recommandation de construction en une tranche est acceptée si elle est argumentée (espérance supérieure, capacité de financement).

**Exemple de recommandation**

1. **Usine de plats végétaux : construire, de préférence en deux tranches.** Les deux variantes créent de la valeur en espérance (9 393 k€ en une tranche, 8 050 k€ en deux tranches). La construction en une tranche fait courir un risque de destruction de valeur de 5,4 M€ une fois sur quatre, avec un coefficient de variation de 1,02. En deux tranches, aucune VAN n'est négative et l'écart-type passe à 2 022 k€, pour un manque à gagner espéré de 1,3 M€. Ce choix est cohérent avec la situation du groupe : marges en baisse en 2026, cours en recul de 15 %, et un actionnaire de contrôle peu diversifié. L'extension sera décidée fin 2029 si la demande observée atteint le niveau fort.
2. **Branche « ingrédients déshydratés » : accepter l'offre.** La cession crée 7,7 M€ de valeur par rapport à la conservation. Elle recentre le groupe sur ses métiers stratégiques, conformément au plan « Horizon 2030 ». Le produit net de 59,5 M€ couvre la tranche 1 de l'usine (34,5 M€), et même la construction en une tranche (48,0 M€). Selon le financement hiérarchique de Myers et Majluf (1984), une ressource interne évite d'émettre des actions à un cours déprimé (42 €) ou d'alourdir l'endettement.
3. **Limites des critères.**
   - Les probabilités des scénarios sont subjectives et trois scénarios ne décrivent pas tous les états possibles. Un événement extrême, comme une récolte catastrophique ou une rupture des habitudes de consommation, échappe à ce découpage (Taleb, 2007, facultatif).
   - L'espérance de la VAN est neutre au risque. L'écart-type mélange risque spécifique et risque systématique.
   - Le taux de 8 % sous-estime le risque des plats végétaux : un taux propre au projet, compris entre 8 % et 10,5 % (coût des fonds propres du secteur), réduirait la VAN sans la rendre négative dans le scénario central (au moins 6,8 M€).
   - La durée de 5 ans est courte pour une usine : la valeur résiduelle est prudente.
   - La valeur de conservation de la branche dépend à 72 % de la valeur estimée pour 2032.
   - Les critères financiers ignorent des enjeux de performance durable que le conseil doit intégrer : la demande de protéines végétales s'inscrit dans la transition alimentaire et la baisse de l'empreinte carbone. Il faut aussi tenir compte de l'emploi sur le site cédé (devenir des salariés, l'acquéreur prévoyant de regrouper la production : point à négocier) et de l'image auprès des distributeurs (`JUR-T05`).

**Réponses tolérées** : recommandation de construction en une tranche, si le candidat la justifie par l'espérance plus élevée et par la capacité du groupe à supporter le risque ; mention de la flexibilité de la construction en deux tranches sans la chiffrer ; toute limite pertinente illustrée par une donnée du dossier.

**Erreurs fréquentes**
- `JUR-T02` et `JUR-T06` — recommandation sans lien entre théorie, calculs et cas, ou sans auteur ni notion de cours (risque systématique, arbitrage espérance-risque, valeur de conservation).
- `JUR-T13` — recommandation générale (« investir si la VAN est positive ») sans arbitrage entre espérance et risque.
- `JUR-T15` — question bâclée faute de temps, alors qu'elle vaut 3 points.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 80-81 | VAN, TRI, IP, délais ; scénarios, espérance et écart-type de la VAN, sensibilité, arbre de décision simple ; désinvestissement (flux évités, valeur de cession, coûts associés) ; exclusion des techniques avancées | [V] | F01 § 1, 4 et 5 |
| Formules de la VAN, du TRI par interpolation, de l'indice de profitabilité | critères de choix d'investissement | [S] | F01 § 4 |
| MEDAF (Sharpe, 1964) | rentabilité exigée fonction du risque systématique (bêta) | [S] | F10 § 2 |
| Markowitz (1952) | diversification : le risque spécifique se diversifie, le risque systématique non | [V programme 5.3] | F10 § 2 |
| Myers et Majluf (1984) | financement hiérarchique : ressources internes, puis dette, puis actions | [V programme 7.2] | F10 |
| Taleb (2007), facultatif | événements extrêmes non décrits par quelques scénarios | [V programme 5.1] | F10 § 1 |
| Taux sans risque 4 % et prime de risque du marché 5 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 |

---

## DOSSIER 3 – POLITIQUE DE DISTRIBUTION ET LECTURE DU MARCHÉ (15 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Politique de dividende et théories | `4.1.a` Déchiffrer la politique de dividende et les signaux associés | 3 |
| 3.2 Dividende exceptionnel ou rachat d'actions | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital ; `4.1.a` | 3 |
| 3.3 Valeur de l'action par Gordon-Shapiro | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique d'un titre | 2 |
| 3.4 Réaction du cours à l'avertissement sur résultats | `5.1.c` Efficience informationnelle (Fama, 1970) ; `5.1.d` Finance comportementale | 3 |
| 3.5 Portefeuille de la holding familiale | `5.3.a` Risque spécifique et risque systématique ; `5.3.b` Diversification (Markowitz, 1952) ; `5.3.c` Rentabilité et risque d'un portefeuille | 4 |
| **Total** | | **15** |

Part du calcul : environ 7 points (3.1-01, 3.2-01 et 3.2-02, 3.3-01 et 3.3-02, 3.5-01 à 3.5-03). Part de l'analyse : environ 8 points. Ce dossier, placé en fin d'épreuve, vaut autant qu'un dossier calculatoire : il ne doit pas être bâclé faute de temps (`JUR-T15`).

---

### 3.1 Politique de dividende et théories (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Taux de distribution : 33,3 % de 2022 à 2025, 44,4 % en 2026 ; rendements : 2,50 % ; 2,33 % ; 2,20 % ; 2,43 % ; 2,86 % | 1 |
| 3.1-02 | Caractérisation : taux de distribution cible d'un tiers et dividende croissant jusqu'en 2025 ; en 2026, maintien à 1,20 € au lieu de 0,90 € : effet cliquet | 0,5 |
| 3.1-03 | Neutralité (Modigliani et Miller, 1961) appliquée au cas | 0,5 |
| 3.1-04 | Théorie du signal (Spence, 1973 ; Ross, 1977) appliquée à la proposition | 0,5 |
| 3.1-05 | Frictions (fiscalité, coûts d'agence, coûts de transaction) et conclusion | 0,5 |

**Calculs (1 pt).** Taux de distribution = dividende par action / BPA ; rendement = dividende par action au titre de l'exercice / cours au 31 décembre.

| Exercice | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|---:|
| BPA (€) | 3,00 | 3,15 | 3,30 | 3,60 | 2,70 |
| Dividende par action (€) | 1,00 | 1,05 | 1,10 | 1,20 | 1,20 (proposé) |
| **Taux de distribution** | **33,3 %** | **33,3 %** | **33,3 %** | **33,3 %** | **44,4 %** |
| Cours au 31/12 (€) | 40,00 | 45,00 | 50,00 | 49,40 | 42,00 |
| **Rendement de l'action** | **2,50 %** | **2,33 %** | **2,20 %** | **2,43 %** | **2,86 %** |

**Caractérisation (0,5 pt).**
- De 2022 à 2025, TERRALBE distribue exactement un tiers de son résultat : le dividende suit le BPA et progresse chaque année (+ 20 % en trois ans). C'est une politique de taux de distribution cible, rassurante pour les actionnaires.
- En 2026, le BPA baisse de 25 % (3,60 € → 2,70 €). Appliquer le taux habituel donnerait 2,70 / 3 = **0,90 €**, soit un dividende en baisse de 25 %. Le conseil propose au contraire de **maintenir 1,20 €**, ce qui porte le taux de distribution à 44,4 % : c'est l'**effet cliquet**. Une entreprise hésite à baisser un dividende, car le marché interprète une baisse comme une mauvaise nouvelle durable (lissage décrit par Lintner, 1956).
- La hausse du rendement (2,86 % contre 2,43 %) ne vient pas d'un dividende plus élevé mais de la baisse du cours (− 15 %).

**Neutralité (0,5 pt).** Selon Modigliani et Miller (1961), en marché parfait (sans impôt ni coûts de transaction, information partagée, politique d'investissement donnée), la politique de dividende n'affecte pas la valeur : ce que l'actionnaire reçoit en dividende, il le perd en valeur de l'action (le cours baisse du dividende lors du détachement). En l'espèce, maintenir 1,20 € plutôt que 0,90 € ne crée pas de valeur : les 3 M€ supplémentaires (0,30 € × 10 000 000) sortent de la trésorerie du groupe. Un actionnaire qui a besoin de liquidités peut se fabriquer un « dividende maison » en cédant des titres : LESTRADEC Participations pourrait couvrir son besoin de 5,5 M€ en vendant une partie de ses parts du fonds indiciel (97,2 M€, annexe 3.4).

**Signal (0,5 pt).** La politique de dividende n'est pas neutre en pratique, parce que les dirigeants en savent plus que le marché sur les perspectives de l'entreprise.
- Au sens de Spence (1973), un signal est crédible s'il est coûteux à imiter : maintenir le dividende malgré un résultat en baisse de 25 % signale que la direction juge la baisse temporaire (récolte exceptionnellement mauvaise) et croit au redressement, puisqu'elle s'engage à verser 12,0 M€ sur un résultat de 27,0 M€.
- Ross (1977) a construit la théorie du signal sur la structure financière : un dirigeant qui accroît l'endettement signale sa confiance dans les flux futurs, car il supporte le risque de défaillance. Appliquée au dividende, la logique est la même : un dividende maintenu au prix d'une trésorerie moindre, donc d'une dette nette plus élevée, engage la direction de la même façon.
- Le signal a déjà été envoyé : le communiqué du 14 octobre 2026 (annexe 3.3) a confirmé un dividende « au moins égal » à celui de l'exercice précédent. Revenir à 0,90 € décevrait un engagement public et serait lu comme un aveu de difficultés durables.

**Frictions et conclusion (0,5 pt).**
- **Fiscalité** : l'imposition du dividende chez l'actionnaire peut être plus lourde que celle d'une plus-value réalisée plus tard ; certains actionnaires préfèrent donc un dividende faible (effet de clientèle). Aucun calcul n'est attendu.
- **Coûts d'agence** (Jensen et Meckling, 1976) : distribuer réduit la trésorerie laissée à la discrétion des dirigeants. Chez TERRALBE, l'enjeu porte aussi sur la relation entre l'actionnaire de contrôle et les minoritaires : avec 0,90 €, LESTRADEC Participations recevrait 5 400 000 × 0,90 = 4,86 M€, moins que ses besoins (5,5 M€), contre 6,48 M€ avec 1,20 €. Le conseil, présidé par Mme LESTRADEC, doit montrer que le maintien sert tous les actionnaires et pas seulement la holding.
- **Coûts de transaction** : céder des titres pour se créer un dividende a un coût ; les petits porteurs préfèrent un revenu régulier.
- **Conclusion** : le maintien à 1,20 € est défendable comme signal de confiance et pour la stabilité attendue par les actionnaires, à condition que le redressement soit crédible : un taux de distribution de 44 % durablement supérieur au taux cible réduirait l'autofinancement du plan « Horizon 2030 ». La revue de la politique de distribution annoncée par le plan devrait fixer une règle claire (dividende ordinaire stable, retour de l'excédent par des opérations exceptionnelles).

**Réponses tolérées** : taux de distribution calculés en masse (dividendes / résultat net part du groupe, mêmes résultats) ; taux de distribution donnés à deux décimales (un tiers, 44,44 %) ; rendement calculé sur un autre cours si le candidat le précise ; référence à Lintner (1956) facultative ; signal présenté seulement par Spence si le raisonnement est juste.

**Erreurs fréquentes**
- `JUR-I04` — ne pas opposer le revenu immédiat de l'actionnaire et le renforcement des fonds propres du groupe.
- `JUR-T14` et `JUR-M01` — citer « Ross » pour un signal par le dividende sans préciser qu'il s'agit à l'origine d'un signal par l'endettement ; confondre neutralité et absence d'intérêt du dividende.
- Conclure que la hausse du rendement en 2026 traduit une politique plus généreuse, alors qu'elle vient de la baisse du cours.
- `JUR-T13` — exposé des théories sans lien avec TERRALBE (taux de 44,4 %, besoins de la holding, communiqué d'octobre).

---

### 3.2 Dividende exceptionnel ou rachat d'actions (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | BPA pro forma : 2,70 € avant ; option A : 2,63 € ; option B : 909 090 actions rachetées, 9 090 910 actions, 2,89 € | 1 |
| 3.2-02 | Effets : capitaux propres 320 → 280 M€ dans les deux options ; dette financière nette 150 → 190 M€ et ratio du crédit syndiqué 2,23 → 2,83 ; LESTRADEC Participations 54 % → 59,40 % (option B), inchangé avec l'option A | 1 |
| 3.2-03 | Signal de chaque option et recommandation argumentée | 1 |

**Conventions rappelées** (annexe 3.2) : opération supposée réalisée le 1er janvier 2026 pour le BPA ; produits financiers perdus sur 40 M€ à 2,4 %, après IS à 25 % ; actions rachetées arrondies à l'unité inférieure ; effets sur la structure au 31/12/2026, hors dividende ordinaire.

**BPA pro forma (1 pt).**
- Produits financiers perdus, nets d'impôt : 40 M€ × 2,4 % × (1 − 25 %) = **0,72 M€** ; résultat pro forma : 27,0 − 0,72 = **26,28 M€**.
- **Option A** (dividende exceptionnel de 40 / 10 = 4,00 € par action) : le nombre d'actions ne change pas. BPA = 26,28 / 10 = **2,63 €** (− 2,7 %).
- **Option B** (rachat à 44 €) : 40 000 000 / 44 = 909 090,9, soit **909 090 actions** rachetées (9,09 % du capital) pour 39 999 960 €. Actions restantes : 10 000 000 − 909 090 = **9 090 910**. BPA = 26 280 000 / 9 090 910 = **2,89 €** (+ 7,1 %).
- Le rachat est relutif parce que le rendement bénéficiaire de l'action au prix de rachat (BPA / prix = 2,70 / 44 = 6,14 %) dépasse le coût après impôt de la trésorerie utilisée (2,4 % × 0,75 = 1,80 %).

**Effets sur la structure et le contrôle (1 pt).**

| | Avant | Option A | Option B |
|---|---:|---:|---:|
| Capitaux propres consolidés (M€) | 320,0 | 280,0 | 280,0 |
| Trésorerie (M€) | 50,0 | 10,0 | 10,0 |
| Dette financière nette hors obligations locatives (M€) | 150,0 | 190,0 | 190,0 |
| Ratio du crédit syndiqué (DFN / 67,2) | 2,23 | 2,83 | 2,83 |
| Ratio d'endettement net (DFN / capitaux propres), facultatif | 46,88 % | 67,86 % | 67,86 % |
| Part du capital de LESTRADEC Participations | 54 % | 54 % | 59,40 % |

- Les deux options réduisent les capitaux propres de 40 M€ (dividende prélevé sur les réserves, ou annulation des actions rachetées) et augmentent d'autant la dette financière nette, puisque la trésorerie diminue.
- **Ratio du crédit syndiqué** : 190 / 67,2 = **2,83**, sous le plafond de 3,0, mais la marge devient étroite. Le ratio atteindrait 3,0 si l'EBITDA hors effet de la norme tombait à 190 / 3 = 63,3 M€, soit une baisse de 5,75 % seulement (contre une baisse admissible de 25,6 % avant l'opération : 150 / 3 = 50 M€). Après une année de marges en recul, ce risque n'est pas théorique.
- **Contrôle** : avec l'option B, LESTRADEC Participations conserve 5 400 000 actions sur 9 090 910, soit **59,40 %**, sans rien débourser ; le flottant diminue (le public passerait de 43 % à 37,30 % si toutes les actions rachetées venaient de lui, calcul facultatif). Avec l'option A, sa part reste de 54 % et elle reçoit 5 400 000 × 4,00 = **21,6 M€**.

**Signal et recommandation (1 pt).**
- **Le BPA n'est pas la valeur.** La hausse du BPA de l'option B est mécanique : selon Modigliani et Miller, en marché parfait, la richesse des actionnaires est la même dans les deux options et la même qu'avant. Le BPA augmente, mais l'endettement aussi : le risque par action augmente et le PER devrait baisser. Le rachat ne crée de valeur pour les actionnaires restants que si l'action est achetée sous sa valeur : il transfère alors de la valeur des vendeurs vers ceux qui restent. Si la valeur est de 42 €, payer 44 € transfère de la valeur aux vendeurs (cours théorique après rachat : (420 − 40) / 9,09 M ≈ 41,80 €) ; si elle est de 48 € (question 3.3), les actionnaires restants y gagnent (cours théorique ≈ 48,40 €).
- **Signal de l'option A** : un dividende qualifié d'exceptionnel n'engage pas l'avenir, ce qui évite l'effet cliquet. Il peut toutefois être lu comme l'aveu d'un manque de projets rentables, au moment où le groupe annonce une usine. Il traite tous les actionnaires à égalité et procure à la holding 21,6 M€, qu'elle peut diversifier (question 3.5).
- **Signal de l'option B** : racheter ses actions à 44 € signale que la direction juge le cours de 42 € trop bas, au lendemain d'une baisse jugée excessive (annexe 3.3). Le signal est crédible parce que coûteux : il mobilise la trésorerie et accroît l'endettement (Ross, 1977). Le rachat est aussi plus souple qu'un dividende : il peut être étalé ou interrompu.
- **Points de vigilance** : le rachat renforce le contrôle de la famille sans contrepartie et réduit la liquidité du titre, ce que les minoritaires peuvent contester ; les deux options rapprochent le groupe du plafond du crédit syndiqué au moment où il doit financer le plan « Horizon 2030 ».
- **Recommandation type** : préférer le rachat d'actions, pour le signal et la souplesse, mais l'exécuter progressivement et pour un montant compatible avec une marge de sécurité sur le ratio du crédit syndiqué (par exemple une première tranche de 20 M€, à compléter si l'EBITDA de 2027 se redresse). Une recommandation de dividende exceptionnel est acceptée si elle est argumentée : égalité de traitement, absence de renforcement du contrôle, liquidités permettant à la holding de diversifier son patrimoine.

**Réponses tolérées** : nombre d'actions arrondi à 909 091 (BPA 2,89 €, part de LESTRADEC 59,40 %) ; BPA calculé sans la perte de produits financiers s'il est présenté comme une première approche, puis corrigé (2,70 € et 2,97 €) : 0,5 point sur l'item 3.2-01 ; capitaux propres part du groupe (296 → 256 M€) au lieu des capitaux propres consolidés ; toute recommandation argumentée qui tient compte du signal, du contrôle et de la contrainte du crédit syndiqué.

**Erreurs fréquentes**
- Oublier les produits financiers perdus : le rachat paraît plus relutif (2,97 €) et le dividende exceptionnel neutre pour le BPA (2,70 €).
- Présenter la hausse du BPA comme une création de valeur.
- Calculer la nouvelle part de LESTRADEC sur 10 000 000 actions, ou supposer qu'elle apporte ses titres au rachat.
- Développer la procédure juridique du rachat (autorisation, plafonds légaux) : hors programme.
- `JUR-T13` — recommandation sans lien avec la situation du groupe (ratio du crédit syndiqué, cours après l'avertissement, contrôle familial).

---

### 3.3 Valeur de l'action par le modèle de Gordon-Shapiro (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Valeur théorique : 1,20 / (8,5 % − 6 %) = 48,00 € | 0,5 |
| 3.3-02 | Rentabilité implicite au cours de 42 € : 1,20 / 42 + 6 % = 8,86 % | 0,5 |
| 3.3-03 | Interprétation de l'écart | 1 |

**Valeur théorique (0,5 pt).** Le modèle de Gordon-Shapiro actualise à l'infini un dividende qui croît à un taux constant g, inférieur à la rentabilité exigée k. Le prochain dividende (1,20 €) est perçu dans un an :

P0 = D1 / (k − g) = 1,20 / (0,085 − 0,06) = 1,20 / 0,025 = **48,00 €**.

**Rentabilité implicite (0,5 pt).** Un investisseur qui achète l'action 42 € obtient, si le dividende croît de 6 % par an, une rentabilité égale au rendement du dividende plus la croissance : 1,20 / 42 + 6 % = 2,86 % + 6 % = **8,86 %**.

**Interprétation (1 pt).**
- Selon les hypothèses de la direction, l'action vaut 48,00 €, soit 14,3 % de plus que le cours. De même, la rentabilité implicite (8,86 %) dépasse la rentabilité exigée par le MEDAF (8,5 %) : l'action paraît sous-évaluée.
- Le marché ne partage pas ces hypothèses. Au cours de 42 € et pour une rentabilité exigée de 8,5 %, la croissance implicite du dividende est de 8,5 % − 2,86 % = **5,64 %** : le marché anticipe une croissance un peu plus faible, ou exige une rentabilité plus élevée après l'avertissement de 2026.
- Le modèle est très sensible à l'écart k − g, ici de 2,5 points seulement : avec une croissance de 5,5 %, la valeur tombe à 40,00 € ; avec 5 %, à 34,29 €. Une différence d'un demi-point sur la croissance suffit à expliquer l'écart avec le cours.
- La croissance de 6 % est discutable. Elle est supposée constante et illimitée, alors qu'elle dépasse la croissance de long terme de l'économie. Elle n'est finançable sans ressources nouvelles qu'au prix d'un retour au taux de distribution cible : rentabilité des capitaux propres part du groupe × taux de rétention = 27,0 / 296 × (1 − 44,4 %) = 9,12 % × 55,6 % = 5,07 % avec le taux de 2026, mais 9,12 % × 2/3 = 6,08 % avec le taux cible d'un tiers (calcul facultatif). Maintenir durablement un taux de distribution de 44,4 % et une croissance de 6 % n'est donc pas compatible, sauf si le plan « Horizon 2030 » relève la rentabilité.
- **Conclusion** : l'écart ne prouve pas une erreur du marché ; il mesure la différence entre les anticipations de la direction et celles des investisseurs, que la communication du plan devra réduire. Il éclaire la question 3.2 : racheter à 44 € n'enrichit les actionnaires restants que si la valeur réelle dépasse 44 €, ce qui suppose une croissance d'au moins 5,77 % (8,5 % − 1,20 / 44, calcul facultatif).

**Réponses tolérées** : croissance implicite présentée à la place de la sensibilité ; rentabilité implicite arrondie à 8,9 % ; autres valeurs de sensibilité, si elles sont justes.

**Erreurs fréquentes**
- Augmenter de 6 % le dividende proposé alors que l'annexe donne directement le prochain dividende : 1,20 × 1,06 = 1,272 € et une valeur de 50,88 €. L'item 3.3-01 est perdu ; la suite est notée en cohérence.
- Appliquer la formule sans vérifier que la rentabilité exigée dépasse la croissance.
- Conclure que l'action « doit » remonter à 48 € : la valeur dépend d'une hypothèse de croissance que le marché ne partage pas.
- `JUR-T13` — calcul sans interprétation, ou interprétation sans lien avec le cours de 42 € et le rachat envisagé.

---

### 3.4 Réaction du cours à l'avertissement sur résultats (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Définition de l'efficience et de ses trois formes (Fama, 1970) | 0,5 |
| 3.4-02 | Réaction de J+1 : intégration rapide de l'information publique, cohérente avec la forme semi-forte | 0,5 |
| 3.4-03 | Mouvements de J−3 et J−2 sans information publique : forme forte mise en défaut | 0,5 |
| 3.4-04 | Poursuite de la baisse puis rebond : sur-réaction et biais comportementaux (Kahneman et Tversky, 1973) | 1 |
| 3.4-05 | Conséquences pour la communication financière de TERRALBE | 0,5 |

**Efficience (0,5 pt).** Selon Fama (1970), un marché est efficient si les cours reflètent à tout instant l'information disponible, si bien qu'aucun investisseur ne peut obtenir durablement une rentabilité anormale. Trois formes : **faible** (les cours intègrent l'information contenue dans les cours passés), **semi-forte** (ils intègrent toute l'information publique), **forte** (ils intègrent toute l'information, y compris non publique).

**Le jour de la réaction (0,5 pt).** Le communiqué est publié le 14 octobre après la clôture. Dès la séance suivante (J+1), la rentabilité anormale est de − 9,0 % et 412 000 titres s'échangent, près de 19 fois le volume moyen de septembre (22 000). L'information publique est intégrée en une séance : c'est conforme à l'efficience au sens semi-fort. L'ampleur est cohérente avec la nouvelle : le résultat attendu passe de 34 M€ à 27 M€ (− 21 %).

**Avant l'annonce (0,5 pt).** Les 9 et 12 octobre (J−3 et J−2), le titre perd 3,3 points de rentabilité anormale, avec des volumes triples de la normale (64 000 et 71 000 titres), alors qu'aucune information n'est publiée. Des investisseurs semblent avoir agi sur une information non publique (fuite, initiés) : la forme forte n'est pas vérifiée, ce qui est le cas général. Nuance : l'article du 30 septembre sur les récoltes était public, mais il ne permettait pas de chiffrer l'impact sur le résultat ; on ne peut pas affirmer que le marché l'a ignoré.

**Après l'annonce (1 pt).**
- La baisse se poursuit en J+2 et J+3 (− 2,6 % et − 1,6 % de rentabilité anormale) alors qu'aucune information nouvelle sur TERRALBE n'est publiée, hormis des commentaires d'analystes et de forums. Au plus bas (19 octobre), la rentabilité anormale cumulée atteint − 16,5 %. Le titre regagne ensuite 5,5 points de J+4 à J+10, après l'article du 21 octobre, pour finir à − 11,0 %.
- Ce profil (chute, prolongement, rebond partiel) évoque une **sur-réaction** puis une correction, difficile à concilier avec un ajustement instantané et juste des cours. La sanction paraît forte pour une baisse de résultat présentée comme liée à une récolte exceptionnelle : un an de résultat amputé de 7 M€ représente environ 0,70 € par action, bien moins que les 7,79 € perdus par le cours entre le 6 et le 19 octobre (49,20 € → 41,41 €).
- **Biais en jeu** (Kahneman et Tversky, 1973) : **représentativité**, les investisseurs extrapolent une mauvaise année en tendance (« 2027 ne sera-t-il pas pire encore ? ») ; **disponibilité**, les informations frappantes et récentes (pluies, chute du cours, forums) pèsent plus que les données de long terme ; **ancrage**, sur l'objectif de 34 M€ annoncé en juillet (surprise amplifiée) puis sur les objectifs de cours abaissés à 38 € ; **mimétisme**, les ventes entraînent les ventes (188 000 titres en J+2). La finance comportementale (rationalité limitée, comportements mimétiques) explique pourquoi les prix peuvent s'écarter un temps de la valeur.
- Nuance : la baisse résiduelle (− 11 %) peut aussi être rationnelle si le marché révise la croissance de long terme (pression des marques de distributeurs, coûts de l'énergie), comme le suggère la croissance implicite de 5,64 % (question 3.3).

**Conséquences pour TERRALBE (0,5 pt).**
- Publier sans délai et de façon égale pour tous les investisseurs toute information susceptible d'influencer le cours : les mouvements des 9 et 12 octobre montrent un coût de l'asymétrie d'information (soupçon d'initiés, perte de confiance). L'AMF veille à cette égalité d'information.
- Donner des objectifs prudents ou en fourchette, et expliquer la part conjoncturelle (récolte) et la part durable (marges) de la baisse, pour limiter les sur-réactions.
- Présenter le plan « Horizon 2030 » avec des hypothèses vérifiables, pour rapprocher les anticipations du marché de celles de la direction (question 3.3).
- Dans un marché efficient, choisir le moment d'une opération sur le capital n'apporte rien ; si le cours a sur-réagi, un rachat d'actions après la baisse peut au contraire profiter aux actionnaires restants, à condition que la direction ne dispose pas d'une information défavorable non publiée.

**Réponses tolérées** : lecture des volumes comme une anticipation par des analystes à partir de l'information publique (forme semi-forte discutée), si elle est argumentée ; autres biais pertinents reliés à une donnée de l'annexe (aversion aux pertes, excès de confiance des investisseurs avant l'annonce) ; référence facultative à d'autres auteurs (Shiller, De Bondt et Thaler) si elle est reliée au cas.

**Erreurs fréquentes**
- Calculer ou recalculer les rentabilités anormales : elles sont données, aucun calcul n'est demandé.
- Affirmer qu'Euronext est efficient au sens fort, ou que Fama a fondé la finance comportementale.
- Réciter une liste de biais sans les relier aux dates, aux volumes et aux articles de l'annexe (`JUR-T13`).
- `JUR-M01` — oublier les références aux théories fondatrices (efficience, asymétrie d'information) dans une question de réflexion.

---

### 3.5 Portefeuille de LESTRADEC Participations (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Poids 70 % / 30 % ; rentabilité espérée 9,35 % ; écart-type 20,29 % ; bêta 0,93 | 1,5 |
| 3.5-02 | Sharpe : 0,22 (TERRALBE), 0,33 (fonds), 0,26 (portefeuille) ; Treynor : 6,11 %, 5,00 %, 5,75 % | 1 |
| 3.5-03 | Risque de l'action TERRALBE : systématique 29,16 % de la variance (écart-type 13,50 %), spécifique 70,84 % (21,04 %) | 0,5 |
| 3.5-04 | Lecture au sens de Markowitz (1952) et conseil à la holding | 1 |

**Rentabilité, risque et bêta du portefeuille (1,5 pt).**
- Poids : actions TERRALBE 5 400 000 × 42 = 226,8 M€ ; fonds 97,2 M€ ; total 324,0 M€. Poids : **70 %** et **30 %**.
- Rentabilité espérée : 0,70 × 9,5 % + 0,30 × 9,0 % = **9,35 %**.
- Variance : 0,70² × 0,25² + 0,30² × 0,15² + 2 × 0,70 × 0,30 × 0,54 × 0,25 × 0,15 = 0,030625 + 0,002025 + 0,008505 = 0,041155. Écart-type = √0,041155 = **20,29 %**.
- Bêta : 0,70 × 0,90 + 0,30 × 1,00 = **0,93**.

**Ratios de performance (1 pt).**

| | Rentabilité espérée | Écart-type | Bêta | Sharpe = (E − 4 %) / σ | Treynor = (E − 4 %) / β |
|---|---:|---:|---:|---:|---:|
| Action TERRALBE | 9,50 % | 25,00 % | 0,90 | 0,22 | 6,11 % |
| Fonds indiciel | 9,00 % | 15,00 % | 1,00 | 0,33 | 5,00 % |
| Portefeuille | 9,35 % | 20,29 % | 0,93 | 0,26 | 5,75 % |

**Risque systématique et risque spécifique de l'action TERRALBE (0,5 pt).** Variance totale : 0,25² = 0,0625. Risque systématique : 0,90² × 0,15² = 0,018225, soit **29,16 %** de la variance (écart-type 13,50 %). Risque spécifique : 0,0625 − 0,018225 = 0,044275, soit **70,84 %** de la variance (écart-type 21,04 %). Pour le portefeuille (facultatif) : risque systématique 0,93² × 0,0225 = 0,019460 et risque spécifique 0,70² × 0,044275 = 0,021695, soit 52,71 % de la variance.

**Lecture et conseil (1 pt).**
- **Diversification** : l'écart-type du portefeuille (20,29 %) est inférieur à la moyenne pondérée des écarts-types (0,70 × 25 % + 0,30 × 15 % = 22,00 %) parce que la corrélation (0,54) est inférieure à 1. Selon Markowitz (1952), le risque d'un portefeuille dépend des corrélations entre ses titres : en combiner de faiblement corrélés réduit le risque sans réduire la rentabilité espérée en proportion.
- **Deux ratios, deux classements** : le ratio de Treynor place l'action TERRALBE en tête (6,11 %), parce qu'il ne retient que le risque systématique et que la holding attend 9,5 %, plus que les 8,5 % exigés par le MEDAF. Le ratio de Sharpe la place en dernier (0,22), parce qu'il retient le risque total, dont 71 % est spécifique. Le ratio de Treynor convient à un investisseur déjà diversifié ; pour LESTRADEC Participations, dont 70 % du patrimoine est investi dans TERRALBE, c'est le risque total qui compte : le ratio de Sharpe est le bon critère.
- **Risque non rémunéré** : le marché ne rémunère que le risque systématique. La holding supporte un risque spécifique important (récoltes, marques de distributeurs, avertissement d'octobre) qui n'est pas rémunéré : c'est le prix du contrôle familial. Le fonds seul offrirait un meilleur ratio de Sharpe (0,33) que le portefeuille (0,26).
- **Conseil** : la holding ne peut pas céder de titres TERRALBE sans menacer son contrôle (54 %). Elle peut réduire son risque en orientant vers le fonds les liquidités qu'elle reçoit au-delà de ses besoins, en particulier les 21,6 M€ du dividende exceptionnel si l'option A est retenue. Avec un cours ex-dividende théorique de 38 €, ses actions TERRALBE vaudraient 205,2 M€ et le fonds 118,8 M€ : le poids de TERRALBE tomberait à 63 % et l'écart-type du portefeuille à 19,36 % (calcul facultatif). Le rachat (option B) va dans le sens inverse : il renforce le poids de TERRALBE dans le contrôle familial et l'endettement du groupe, donc le risque de l'action. L'estimation de 9,5 % mérite aussi d'être discutée : un actionnaire familial peut surestimer les perspectives de sa propre société (excès de confiance).

**Réponses tolérées** : écart-type à 20,29 % ou 20,3 % ; ratio de Sharpe à trois décimales (0,220 ; 0,333 ; 0,264) ; Treynor exprimé en fraction (0,0611) ; décomposition présentée par le carré du coefficient de corrélation (0,54² = 29,16 %), le fonds étant assimilé au marché ; conseil fondé sur d'autres moyens de diversification (placements de la holding, recours à l'emprunt limité) s'il est argumenté.

**Erreurs fréquentes**
- Calculer l'écart-type du portefeuille comme la moyenne pondérée des écarts-types (22,00 %) : c'est ignorer la corrélation, cœur de l'apport de Markowitz.
- Oublier le facteur 2 dans le terme de covariance, ou utiliser la corrélation au lieu de la covariance (ρ × σT × σM = 0,02025).
- Inverser les dénominateurs des ratios : Sharpe sur l'écart-type, Treynor sur le bêta.
- Conclure que la diversification supprime tout risque : le risque systématique demeure.
- `JUR-T02` — résultats sans conseil adapté à la situation d'une holding de contrôle.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 67-69 | politique de dividende (signal, neutralité, effet cliquet, frictions) ; rachats d'actions (effets sur le nombre d'actions, le BPA, les capitaux propres, signal) ; aspects juridiques exclus | [V] | F05 § 0, 2 et 3 |
| Guide pédagogique DSCG, juillet 2026, p. 73-77 | efficience (trois formes, rôle de l'information, timing) ; finance comportementale ; Gordon-Shapiro ; portefeuille de deux titres, corrélation fournie, Sharpe et Treynor ; vérifications empiriques et calcul de la frontière exclus | [V] | F06 § 0 et 3 ; `perimetre_ue2.yaml` |
| Modigliani et Miller (1961) | neutralité du dividende en marché parfait, « dividende maison » | [V programme 4.1] | F10 § 3 |
| Spence (1973) ; Ross (1977) | signal coûteux ; signal par la structure financière | [V programme 4.1] | F10 § 3 |
| Lintner (1956), facultatif | lissage du dividende, effet cliquet | [S] | F10 § 2 |
| Jensen et Meckling (1976) | coûts d'agence | [V programme 2.1] | F10 § 3 |
| Gordon et Shapiro | valeur d'une action à croissance constante du dividende | [V programme 5.2, sans année] | F10 § 2 |
| Fama (1970) | efficience informationnelle, trois formes | [V programme 5.1] | F10 § 1 ; F06 § 3 |
| Kahneman et Tversky (1973) | représentativité, disponibilité, ancrage | [V programme 5.1 pour la référence ; S pour le contenu] | F10 § 1 ; F06 § 4 |
| Markowitz (1952) | diversification, rôle de la corrélation | [V programme 5.3] | F10 § 2 |
| MEDAF (Sharpe, 1964) ; ratio de Treynor (1965) ; ratio de Sharpe (1966) | risque systématique rémunéré ; mesures de performance | [S] | F10 § 2 ; F02 § 2 |
| Taux sans risque 4 % et prime de risque du marché 5 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 |
| Placement de trésorerie à 2,4 % | hypothèse d'énoncé, proche de l'€STR d'octobre 2026 (2,44 %) | [V] pour l'€STR | F11 § 1 |
