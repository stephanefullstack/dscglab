# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 31 — Dossier 1 (18 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 risques de taux, de change et trésorerie, F10 auteurs et théories, F11 données de marché d'octobre 2026 et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (prix, duration, sensibilité et variations des trois lignes obligataires ; équilibre des tableaux de placements et des valeurs des lignes ; moyennes, variances, écarts types, covariances, bêtas, décomposition du risque et ratios de Sharpe des fonds ; rentabilité, écart type et ratio de Sharpe des deux allocations ; rentabilités exigées par le MEDAF ; barème, liste noire, hors-programme ; duration du portefeuille, valeur et duration des engagements, effet sur l'écart et montant à transférer vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée ; les écarts d'arrondi de 0,01 M€ qui viennent d'un calcul mené sans arrondi intermédiaire sont acceptés. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une duration de portefeuille erronée à la question 1.1, reprise dans la comparaison de la question 1.2 et dans le montant à transférer de la question 1.6).

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Prix, duration et sensibilité du portefeuille obligataire | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 3 |
| 1.2 Adossement aux règlements futurs et immunisation | `6.2.a` | 2 |
| 1.3 Rentabilités moyennes, écarts types et bêtas des deux fonds | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier | 2,5 |
| 1.4 MEDAF, rentabilité exigée et limites du modèle | `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 2,5 |
| 1.5 Risque systématique et spécifique, risque des deux allocations et diversification | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres ; `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) | 5 |
| 1.6 Note au conseil d'administration | `5.3.b` ; `5.2.a` ; `6.2.a` | 3 |
| **Total** | | **18** |

Part du calcul : environ 10 points (1.1-01 à 1.1-04, 1.2-01, 1.2-02, 1.3-01 à 1.3-03, 1.4-01, 1.5-01 à 1.5-04 et une partie de 1.6-02). Part de l'analyse : environ 8 points. Les questions 1.3 à 1.5 se traitent sans les questions 1.1 et 1.2, et la note de la question 1.6 peut s'appuyer sur des résultats partiels.

---

### 1.1 Prix, duration et sensibilité du portefeuille obligataire (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Prix pour 100 € de nominal : A 98,65 € ; B 98,19 € ; C 74,20 € ; valeurs des lignes : 473,52 / 559,68 / 296,80 M€ (total 1 330,00 M€) | 0,5 |
| 1.1-02 | Durations : A 1,980 an ; B 4,714 ans ; C 8,000 ans ; sensibilités − 1,928 / − 4,559 / − 7,707 ; tableau des flux actualisés | 1 |
| 1.1-03 | Duration du portefeuille, pondérée par les valeurs : 4,474 ans | 0,5 |
| 1.1-04 | Hausse de 100 points de base : variation estimée − 57,52 M€ (− 4,32 %) ; valeurs après la hausse (prix fournis) 1 274,31 M€, variation exacte − 55,69 M€ (− 4,19 %) ; explication de l'écart | 0,5 |
| 1.1-05 | Relation inverse entre la valeur et le taux, illustrée par les trois lignes | 0,5 |

**Prix et duration (1,5 pt).** Le prix est la somme des flux futurs actualisés au taux actuariel du marché de la ligne ; la duration est la moyenne des dates des flux pondérées par leurs valeurs actuelles (annexe 1.5).

*Ligne A* (coupon de 2 € dans 1 an, 102 € dans 2 ans, taux de 2,70 %)

| Année t | Flux (€) | Valeur actuelle à 2,70 % | t × valeur actuelle |
|---:|---:|---:|---:|
| 1 | 2 | 1,9474 | 1,9474 |
| 2 | 102 | 96,7073 | 193,4146 |
| **Total** | | **98,6547** | **195,3620** |

Prix = **98,65 €** ; duration = 195,3620 / 98,6547 = **1,980 an** ; sensibilité = − 1,980 / 1,027 = **− 1,928**.

*Ligne B* (coupon de 3 € de l'année 1 à l'année 4, 103 € dans 5 ans, taux de 3,40 %)

| Année t | Flux (€) | Valeur actuelle à 3,40 % | t × valeur actuelle |
|---:|---:|---:|---:|
| 1 | 3 | 2,9014 | 2,9014 |
| 2 | 3 | 2,8060 | 5,6119 |
| 3 | 3 | 2,7137 | 8,1411 |
| 4 | 3 | 2,6245 | 10,4978 |
| 5 | 103 | 87,1434 | 435,7170 |
| **Total** | | **98,1889** | **462,8692** |

Prix = **98,19 €** ; duration = 462,8692 / 98,1889 = **4,714 ans** ; sensibilité = − 4,714 / 1,034 = **− 4,559**.

*Ligne C* (coupon zéro : un seul flux de 100 € dans 8 ans, taux de 3,80 %) : prix = 100 / 1,038⁸ = **74,20 €** ; la duration d'un titre à coupon zéro est égale à sa durée de vie, **8,000 ans**, puisque toute la valeur est perçue à l'échéance ; sensibilité = − 8 / 1,038 = **− 7,707**.

**Valeurs des lignes et duration du portefeuille (0,5 pt).**

| Ligne | Valeur (M€) | Poids | Duration | Valeur × duration |
|---|---:|---:|---:|---:|
| A : 480 × 98,65 / 100 | 473,52 | 35,60 % | 1,980 | 937,57 |
| B : 570 × 98,19 / 100 | 559,68 | 42,08 % | 4,714 | 2 638,33 |
| C : 400 × 74,20 / 100 | 296,80 | 22,32 % | 8,000 | 2 374,40 |
| **Portefeuille** | **1 330,00** | **100 %** | | **5 950,30** |

Duration du portefeuille = 5 950,30 / 1 330,00 = **4,474 ans**. La ligne C ne représente que 22 % de la valeur, mais 40 % de la duration du portefeuille (2 374,40 / 5 950,30).

**Effet d'une hausse de 100 points de base (0,5 pt).**

| Ligne | Sensibilité | Variation estimée (M€) | Prix après la hausse | Valeur après (M€) | Variation exacte (M€) |
|---|---:|---:|---:|---:|---:|
| A (taux 3,70 %) | − 1,928 | 473,52 × − 1,928 % = − 9,13 | 96,78 € | 464,54 | − 8,98 |
| B (taux 4,40 %) | − 4,559 | 559,68 × − 4,559 % = − 25,52 | 93,84 € | 534,89 | − 24,79 |
| C (taux 4,80 %) | − 7,707 | 296,80 × − 7,707 % = − 22,87 | 68,72 € | 274,88 | − 21,92 |
| **Portefeuille** | | **− 57,52 (− 4,32 %)** | | **1 274,31** | **− 55,69 (− 4,19 %)** |

Les prix après la hausse sont fournis par l'annexe 1.1 (pour vérification : A = 2 / 1,037 + 102 / 1,037² = 96,78 € ; B = 2,8736 + 2,7525 + 2,6365 + 2,5253 + 83,0491 = 93,84 € ; C = 100 / 1,048⁸ = 68,72 €).

La sensibilité donne une estimation linéaire, valable pour une petite variation : elle mesure la pente de la relation prix-taux au taux de départ. Cette relation est courbe (la baisse du prix ralentit à mesure que le taux monte), si bien que l'estimation **surestime la perte** de 1,83 M€ (57,52 contre 55,69). L'écart est le plus fort sur la ligne C, la plus longue (0,95 M€). Il grandit avec la duration et avec l'ampleur de la variation de taux ; sa mesure (convexité) n'est pas demandée.

**Relation inverse (0,5 pt).** Les flux d'une obligation à taux fixe sont fixés à l'émission : quand le taux du marché monte, ces flux sont actualisés à un taux plus élevé et leur valeur baisse. Un investisseur n'achète un titre ancien que si son prix baisse assez pour lui procurer le nouveau taux du marché [F07 § 2.1]. En l'espèce, A et B cotent sous le pair parce que leurs coupons (2 % et 3 %) sont inférieurs aux taux du marché (2,70 % et 3,40 %). La baisse est d'autant plus forte que la duration est longue : − 1,90 % pour A, − 4,43 % pour B, − 7,39 % pour C, qui ne verse aucun coupon avant 8 ans. À l'inverse, une baisse des taux augmenterait la valeur du portefeuille. La perte reste latente si les titres sont conservés jusqu'à l'échéance, mais elle devient réelle si la mutuelle doit les vendre pour payer des sinistres.

**Réponses tolérées** : sensibilité exprimée en valeur absolue si le sens de la variation est indiqué ; variation estimée du portefeuille calculée avec sa sensibilité moyenne pondérée (− 4,325 × 1 % × 1 330,00 = − 57,52 M€) ; écarts d'arrondi de 0,01 € sur un prix ou de 0,001 sur une duration.

**Erreurs fréquentes**
- Confondre duration et maturité pour les lignes A et B, ou oublier le remboursement dans le dernier flux.
- Chercher des coupons pour la ligne C, ou lui attribuer une duration inférieure à 8 ans.
- Appliquer la sensibilité au nominal (1 450 M€) au lieu de la valeur de marché (1 330,00 M€).
- Pondérer la duration du portefeuille par les nominaux : (480 × 1,980 + 570 × 4,714 + 400 × 8,000) / 1 450 = 4,715 ans, au lieu de 4,474 ans : la ligne C, qui cote loin sous le pair, serait surpondérée.
- `JUR-T07` — durations calculées sans tableau des flux actualisés ; `JUR-T12` — affirmer qu'une hausse des taux augmente la valeur des obligations détenues.

---

### 1.2 Adossement aux règlements futurs et immunisation (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | Valeur actualisée des règlements : 1 146,65 M€ ; duration 3,386 ans (tableau) | 1 |
| 1.2-02 | Comparaison des durations (4,474 contre 3,386 ans) ; effet de + 100 points de base : obligations − 57,52 M€, engagements − 37,69 M€, écart − 19,83 M€ (de 183,35 à 163,52 M€) | 0,5 |
| 1.2-03 | Principe de l'immunisation ; duration cible d'environ 3,39 ans (ou 2,919 ans pour égaliser les variations en M€) | 0,5 |

**Valeur actualisée et duration des engagements (1 pt).** Règlements de l'annexe 1.2, versés en fin d'année, actualisés à 3,00 %.

| Année | t | Règlements (M€) | Coefficient 1,03⁻ᵗ | Valeur actuelle (M€) | t × valeur actuelle arrondie |
|---|---:|---:|---:|---:|---:|
| 2027 | 1 | 300 | 0,970874 | 291,26 | 291,26 |
| 2028 | 2 | 230 | 0,942596 | 216,80 | 433,60 |
| 2029 | 3 | 180 | 0,915142 | 164,73 | 494,19 |
| 2030 | 4 | 150 | 0,888487 | 133,27 | 533,08 |
| 2031 | 5 | 130 | 0,862609 | 112,14 | 560,70 |
| 2032 | 6 | 110 | 0,837484 | 92,12 | 552,72 |
| 2033 | 7 | 90 | 0,813092 | 73,18 | 512,26 |
| 2034 | 8 | 80 | 0,789409 | 63,15 | 505,20 |
| **Total** | | **1 270** | | **1 146,65** | **3 883,01** |

Valeur actualisée des engagements = **1 146,65 M€** ; duration = 3 883,01 / 1 146,65 = **3,386 ans** (même résultat sans arrondi intermédiaire : 3 883,03 / 1 146,65) ; sensibilité = − 3,386 / 1,03 = − 3,287.

**Comparaison et effet sur l'écart (0,5 pt).** La duration du portefeuille obligataire (4,474 ans) dépasse de près de 1,1 an celle des engagements (3,386 ans) : l'actif est plus sensible aux taux que le passif qu'il doit couvrir.

| | Valeur au 31/12/2026 (M€) | Variation estimée pour + 100 pb (M€) | Valeur après (M€) |
|---|---:|---:|---:|
| Obligations | 1 330,00 | − 57,52 (− 4,32 %) | 1 272,48 |
| Engagements | 1 146,65 | 1 146,65 × − 3,287 % = − 37,69 (− 3,29 %) | 1 108,96 |
| **Écart** | **183,35** | **− 19,83 (− 10,82 %)** | **163,52** |

Une hausse d'un point réduit l'écart de 19,83 M€, soit 3,25 % des fonds propres (610 M€). L'écart réagit comme un placement de duration très longue (environ 11 ans), parce qu'il est la différence de deux montants élevés de durations différentes. Une baisse des taux produirait l'effet inverse : l'actif, plus sensible, gagnerait plus de valeur que les engagements, et l'écart augmenterait d'environ 19,83 M€. L'exposition de la mutuelle porte donc sur la **hausse** des taux.

**Immunisation (0,5 pt).** Un portefeuille est immunisé quand une variation des taux modifie de la même façon la valeur de l'actif et celle des engagements : l'écart ne varie plus. Pour un engagement unique, une obligation de duration égale à l'horizon de cet engagement compense la perte en capital due à la hausse des taux par le réinvestissement des coupons à un taux plus élevé, et inversement. Pour une série de règlements, la règle consiste à **égaliser la duration des obligations et celle des engagements**, soit environ **3,39 ans** contre 4,474 aujourd'hui : des variations relatives égales préservent le taux de couverture des engagements par les obligations (1 330,00 / 1 146,65 = 1,16 ; après le transfert de la question 1.6, l'actif perdrait 3,28 % et les engagements 3,29 % pour un point de hausse). Si l'on veut neutraliser l'écart en M€, alors que l'actif (1 330,00 M€) dépasse les engagements (1 146,65 M€), il faut égaliser les variations en M€ : duration cible ≈ 1 146,65 × 3,386 / 1 330,00 = **2,919 ans**. L'immunisation ne protège que contre une petite variation de même ampleur de tous les taux ; elle doit être ajustée régulièrement, car les durations changent avec le temps et les taux.

**Réponses tolérées** : duration cible exprimée en sensibilité (− 3,287 pour des valeurs égales, ou une variation de l'actif égale à 37,69 M€ pour un point) ; effet exact sur les engagements (− 36,67 M€) et sur l'écart (− 19,02 M€) au lieu de l'estimation ; valeurs actuelles et sensibilités calculées sans arrondi intermédiaire (duration de 3,386 ans dans les deux cas ; − 37,70 M€ pour les engagements et − 19,82 M€ pour l'écart, écarts de 0,01 M€ acceptés).

**Erreurs fréquentes**
- Calculer la duration sur les règlements non actualisés : 4 480 / 1 270 = 3,53 ans.
- Conclure que l'écart augmente quand les taux montent au motif que les engagements baissent, sans comparer les montants des deux variations.
- Recommander d'allonger la duration de l'actif.
- `JUR-T13` — immunisation définie sans chiffrer la duration cible ; `JUR-T07` — valeur actualisée des engagements sans tableau.

---

### 1.3 Rentabilités moyennes, écarts types et bêtas des deux fonds (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | Rentabilités moyennes : Actions Europe 8,50 % ; Infrastructures Cotées 7,50 % ; indice 8,00 % | 0,5 |
| 1.3-02 | Variances (n − 1) 341,26 / 156,50 / 256,00 %² ; écarts types 18,47 % / 12,51 % / 16,00 % | 1 |
| 1.3-03 | Covariances avec l'indice 281,60 et 128,00 %² ; bêtas 1,10 et 0,50 | 0,5 |
| 1.3-04 | Interprétation : niveau de risque, sensibilité au marché, profil défensif du fonds d'infrastructures | 0,5 |

**Calculs** (E = VERCÈNE Actions Europe, I = VERCÈNE Infrastructures Cotées, M = indice ; variances et covariances sur n − 1 = 4)

| Année | E | E − 8,50 | I | I − 7,50 | M | M − 8,00 | (E − Ē)(M − M̄) | (I − Ī)(M − M̄) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2022 | − 21,8 | − 30,3 | 0,0 | − 7,5 | − 15,0 | − 23,0 | 696,90 | 172,50 |
| 2023 | 20,0 | 11,5 | 15,0 | 7,5 | 23,0 | 15,0 | 172,50 | 112,50 |
| 2024 | 3,5 | − 5,0 | − 1,5 | − 9,0 | − 2,0 | − 10,0 | 50,00 | 90,00 |
| 2025 | 22,2 | 13,7 | − 2,0 | − 9,5 | 15,0 | 7,0 | 95,90 | − 66,50 |
| 2026 | 18,6 | 10,1 | 26,0 | 18,5 | 19,0 | 11,0 | 111,10 | 203,50 |
| **Somme** | 42,5 | | 37,5 | | 40,0 | | **1 126,40** | **512,00** |

| | E | I | M |
|---|---:|---:|---:|
| Rentabilité moyenne | 42,5 / 5 = **8,50 %** | 37,5 / 5 = **7,50 %** | 40,0 / 5 = **8,00 %** |
| Somme des carrés des écarts | 1 365,04 | 626,00 | 1 024,00 |
| Variance (÷ 4) | 341,26 %² | 156,50 %² | 256,00 %² |
| Écart type | **18,47 %** | **12,51 %** | **16,00 %** |
| Covariance avec M (÷ 4) | 281,60 %² | 128,00 %² | |
| Bêta = covariance / 256,00 | **1,10** | **0,50** | 1 |

**Interprétation (0,5 pt).** Le fonds d'actions européennes est le plus rentable (8,50 %) mais aussi le plus risqué (écart type de 18,47 %, supérieur à celui de l'indice) ; son bêta de 1,10 signifie qu'il amplifie de 10 % les variations du marché : il a perdu 21,8 % en 2022, quand l'indice perdait 15,0 %. Le fonds d'infrastructures est moins rentable (7,50 %), moins risqué (12,51 %) et peu sensible au marché (bêta de 0,50) : ses revenus encadrés par des contrats et des tarifs le rendent défensif (0,0 % en 2022). Mais ses rentabilités s'écartent souvent de celles du marché (− 2,0 % en 2025 quand l'indice gagne 15,0 % ; 26,0 % en 2026) : une grande partie de son risque lui est propre (question 1.5). Ces mesures portent sur cinq années seulement : ce sont des estimations fragiles.

**Réponses tolérées** : calculs en fraction (variance de l'indice 0,025600) ; écarts d'arrondi de 0,01 point ; bêta calculé par le coefficient de corrélation avec l'indice (bêta = corrélation × écart type du fonds / écart type de l'indice), s'il est justifié.

**Erreurs fréquentes**
- Écarts types calculés sur n au lieu de n − 1 (16,52 % / 11,19 % / 14,31 %), contrairement à l'annexe 1.5.
- Bêta calculé en divisant la covariance par la variance du fonds (281,60 / 341,26 = 0,83) au lieu de celle de l'indice.
- Confondre le bêta (sensibilité au marché) avec l'écart type (risque total).
- `JUR-T07` — calculs sans tableau des écarts ; `JUR-T13` — interprétation sans référence aux années du tableau.

---

### 1.4 MEDAF, rentabilité exigée et limites du modèle (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Rentabilités exigées : Actions Europe 4,00 % + 1,10 × 5,00 % = 9,50 % ; Infrastructures Cotées 4,00 % + 0,50 × 5,00 % = 6,50 % | 0,5 |
| 1.4-02 | Comparaison : − 1,00 point pour Actions Europe, + 1,00 point pour Infrastructures Cotées ; interprétation prudente | 0,5 |
| 1.4-03 | Lien entre incertitude et rentabilité exigée ; seul le risque systématique est rémunéré | 0,5 |
| 1.4-04 | Limites du MEDAF pour un investisseur de long terme comme la mutuelle | 1 |

**Rentabilités exigées (0,5 pt).** MEDAF (Sharpe, 1964) : rentabilité exigée = taux sans risque + bêta × prime de risque du marché [F10].
- Actions Europe : 4,00 % + 1,10 × 5,00 % = **9,50 %**.
- Infrastructures Cotées : 4,00 % + 0,50 × 5,00 % = **6,50 %**.

**Comparaison et interprétation (0,5 pt).** Le fonds d'actions européennes a rapporté 8,50 %, soit **1,00 point de moins** que sa rentabilité exigée : il n'a pas rémunéré son risque de marché. Le fonds d'infrastructures a rapporté 7,50 %, soit **1,00 point de plus** que la sienne : il a fait mieux que ce que son faible bêta laissait attendre. Deux nuances s'imposent :
- sur la période, l'indice lui-même n'a rapporté que 8,00 %, contre 9,00 % exigés (4,00 % + 5,00 %). Avec la rentabilité observée du marché, le MEDAF donnerait 4,00 % + 1,10 × 4,00 % = 8,40 % pour le fonds d'actions européennes, qui fait alors à peu près jeu égal, et 6,00 % pour le fonds d'infrastructures, qui garde 1,50 point d'avance ;
- cinq années ne suffisent pas pour conclure à un talent de gestion : l'écart peut venir d'événements propres à quelques sociétés (2026 pour le fonds d'infrastructures).

**Incertitude et rentabilité exigée (0,5 pt).** Un investisseur averse au risque n'accepte de détenir un placement incertain que s'il en attend une rentabilité supérieure au taux sans risque : la **prime de risque** rémunère l'incertitude sur les flux futurs. Selon le MEDAF, le marché ne rémunère que le **risque systématique**, mesuré par le bêta, car le risque spécifique peut être éliminé sans coût par la diversification. Le fonds d'actions européennes, de bêta 1,10, exige donc une prime de 5,50 points ; le fonds d'infrastructures, de bêta 0,50, une prime de 2,50 points seulement, même si son écart type n'est pas deux fois plus faible (12,51 % contre 18,47 %).

**Limites du MEDAF pour la mutuelle (1 pt).**
- **Modèle d'une seule période** : il raisonne sur un horizon unique, alors que la mutuelle place à long terme (aucun retrait de la poche actions avant 2035) et que ses engagements s'étalent sur huit ans ; les primes de risque et les bêtas changent dans le temps.
- **Paramètres estimés** : le bêta est mesuré sur cinq années ; la prime de risque du marché et le taux sans risque sont des hypothèses (4,00 % et 5,00 %), et le résultat change avec eux.
- **Un seul facteur de risque** : d'autres facteurs (taille, valeur, sensibilité aux taux, à l'inflation ou au climat) peuvent expliquer les rentabilités ; le fonds d'infrastructures est sensible aux taux d'intérêt et aux tarifs réglementés, que le bêta ne mesure pas.
- **Hypothèses fortes** : marché efficient, investisseurs diversifiés qui ne s'intéressent qu'à l'espérance et à la variance de la rentabilité. La mutuelle ne détient que deux fonds : leur **risque total** la concerne, et pas seulement leur bêta. Pour un assureur, le risque pertinent est aussi celui de ne pas pouvoir payer les sinistres : une baisse des actions au moment d'un sinistre climatique important obligerait à vendre au plus bas.
- **Indice de référence** : l'indice large européen est assimilé au portefeuille de marché, ce qui reste une approximation.

**Réponses tolérées** : écart désigné comme l'alpha de Jensen (1968), facultatif [F10] ; mention du modèle à trois facteurs comme prolongement, sans le développer ; rentabilité exigée exprimée en fraction (0,095 ; 0,065).

**Erreurs fréquentes**
- Multiplier le bêta par la rentabilité du marché au lieu de la prime de risque : 4,00 % + 1,10 × 9,00 % = 13,90 %.
- Conclure que le fonds d'infrastructures « crée de la valeur » de façon certaine, sans réserve sur la période.
- Affirmer que le MEDAF rémunère le risque total ou l'écart type.
- `JUR-T14` — MEDAF cité sans ses hypothèses ni ses limites ; `JUR-T13` — limites générales sans lien avec l'horizon et les engagements de la mutuelle.

---

### 1.5 Risque systématique et spécifique, risque des deux allocations et diversification (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | Décomposition : Actions Europe 309,76 %² systématique (90,77 %) et 31,50 %² spécifique (9,23 %) ; Infrastructures Cotées 64,00 %² (40,89 %) et 92,50 %² (59,11 %) | 1 |
| 1.5-02 | Rentabilités espérées : allocation actuelle 8,30 % ; allocation proposée 8,10 % | 0,5 |
| 1.5-03 | Covariance des deux fonds 103,99 %² ; écarts types : 16,06 % (actuelle) et 14,06 % (proposée) | 1 |
| 1.5-04 | Ratios de Sharpe : 0,27 (actuelle) et 0,29 (proposée) ; comparaison | 0,5 |
| 1.5-05 | Markowitz (1952) : rôle de la corrélation ; diversification du risque spécifique, pas du risque systématique | 1,5 |
| 1.5-06 | Application au cas : risque propre du fonds d'infrastructures, bêta de la poche, plafond de la charte | 0,5 |

**Décomposition du risque de chaque fonds (1 pt).** Variance = bêta² × variance de l'indice + variance spécifique (annexe 1.5).

| | Actions Europe | Infrastructures Cotées |
|---|---:|---:|
| Variance totale | 341,26 %² | 156,50 %² |
| Variance systématique = bêta² × 256,00 | 1,10² × 256,00 = 309,76 %² | 0,50² × 256,00 = 64,00 %² |
| Part systématique | **90,77 %** | **40,89 %** |
| Variance spécifique | 341,26 − 309,76 = 31,50 %² | 156,50 − 64,00 = 92,50 %² |
| Part spécifique | **9,23 %** | **59,11 %** |

Le risque du fonds d'actions européennes est presque entièrement celui du marché : diversifié sur de nombreuses sociétés de tous secteurs, il suit l'indice. Le risque du fonds d'infrastructures est surtout spécifique : il dépend de quelques secteurs (énergie, eau, autoroutes, télécommunications), de leurs tarifs et des taux d'intérêt.

**Rentabilité et écart type des deux allocations (1,5 pt).** Covariance des deux fonds = 0,45 × 18,47 × 12,51 = **103,99 %²** (calculée avec les écarts types non arrondis ; 103,98 %² avec les écarts types arrondis, également acceptée).

| | Actuelle 80 / 20 | Proposée 60 / 40 |
|---|---:|---:|
| Rentabilité espérée | 0,80 × 8,50 + 0,20 × 7,50 = **8,30 %** | 0,60 × 8,50 + 0,40 × 7,50 = **8,10 %** |
| wE² × 341,26 | 0,64 × 341,26 = 218,41 | 0,36 × 341,26 = 122,85 |
| wI² × 156,50 | 0,04 × 156,50 = 6,26 | 0,16 × 156,50 = 25,04 |
| 2 × wE × wI × 103,99 | 0,32 × 103,99 = 33,28 | 0,48 × 103,99 = 49,92 |
| Variance (calcul sans arrondi intermédiaire) | 257,94 %² (257,95 en additionnant les termes arrondis) | 197,81 %² |
| **Écart type** | **16,06 %** | **14,06 %** |
| **Ratio de Sharpe** = (Rp − 4,00 %) / σp | 4,30 / 16,06 = **0,27** | 4,10 / 14,06 = **0,29** |

**Comparaison des ratios de Sharpe (0,5 pt).** L'allocation proposée perd 0,20 point de rentabilité espérée (0,46 M€ par an sur 230 M€) mais réduit l'écart type de 2,00 points : elle rémunère mieux chaque point de risque total (0,29 contre 0,27). Pour information, les ratios des fonds pris isolément sont de 0,24 (actions européennes), 0,28 (infrastructures) et 0,25 (indice) : l'allocation proposée fait mieux que chacun des deux fonds, ce qui est l'effet de la diversification.

**Diversification au sens de Markowitz (1952) (1,5 pt)** [F10].
- **Rôle de la corrélation** : le risque d'un portefeuille ne dépend pas seulement des risques des titres, mais aussi de leur covariance, donc de leur corrélation. Tant que la corrélation est inférieure à 1, l'écart type du portefeuille est inférieur à la moyenne pondérée des écarts types. En l'espèce, avec une corrélation de 0,45 : 16,06 % au lieu de 0,80 × 18,47 + 0,20 × 12,51 = 17,28 % pour l'allocation actuelle (gain de 1,22 point), 14,06 % au lieu de 0,60 × 18,47 + 0,40 × 12,51 = 16,09 % pour l'allocation proposée (gain d'environ 2 points). Avec une corrélation de 1, ces deux gains disparaîtraient ; plus la corrélation est faible, plus ils sont importants.
- **Risque spécifique et risque systématique** : le risque spécifique tient aux événements propres à chaque société ou secteur (un contrat perdu, une révision de tarif, une grève). Ces aléas se compensent en partie d'un titre à l'autre : la diversification les réduit et, avec un grand nombre de titres, les élimine presque. Le risque systématique tient aux facteurs qui touchent toutes les sociétés à la fois (croissance, taux d'intérêt, inflation, crise financière) : il ne se compense pas et subsiste quel que soit le nombre de titres. Il ne se réduit qu'en choisissant des titres de bêta plus faible, au prix d'une rentabilité espérée plus faible.
- **Illustration** : dans la poche actions, la variance spécifique ne vaut plus que 257,94 − 0,98² × 256,00 = 12,08 %² dans l'allocation actuelle et 197,81 − 0,86² × 256,00 = 8,47 %² dans l'allocation proposée, alors qu'elle atteint 31,50 %² et 92,50 %² pour chaque fonds pris isolément. La variance systématique (245,86 %² puis 189,34 %²) ne recule que parce que le bêta de la poche passe de 0,98 à 0,86, sous l'effet de la composition, et non grâce à la diversification.

**Application au cas (0,5 pt).** Le fonds d'infrastructures paraît moins intéressant pris seul (7,50 % contre 8,50 %), mais 59 % de son risque est spécifique : dans la poche actions, ce risque se dilue, et le fonds apporte surtout un bêta faible et une corrélation modérée. Le porter à 40 % ramène l'écart type de la poche à 14,06 %, sous le plafond de 15,00 % fixé par la charte de placement, que l'allocation actuelle dépasse (16,06 %). Le bêta de la poche passe de 0,98 à 0,86 : une baisse de 10 % du marché ne lui ferait plus perdre qu'environ 8,6 %.

**Réponses tolérées** : calculs en fraction ; parts du risque calculées sur les écarts types, si le candidat le précise (la convention de l'annexe porte sur la variance) ; covariance de 103,98 %² calculée avec les écarts types arrondis ; écart type du portefeuille calculé avec la covariance des séries (103,80 %², soit 16,06 % et 14,06 %) ; écarts d'arrondi de 0,01 point.

**Erreurs fréquentes**
- Calculer l'écart type du portefeuille comme moyenne pondérée des écarts types (17,28 % et 16,09 %), c'est-à-dire avec une corrélation implicite de 1.
- Oublier le facteur 2 du terme de covariance, ou multiplier par la corrélation sans les écarts types.
- Comparer les allocations sur la seule rentabilité espérée et retenir l'allocation actuelle.
- Affirmer que la diversification élimine tout le risque, ou qu'elle réduit le risque de marché.
- `JUR-T14` — Markowitz cité sans le rôle de la corrélation ; `JUR-T13` — diversification présentée sans les chiffres des deux allocations.

---

### 1.6 Note au conseil d'administration (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.6-01 | Poche actions : recommandation de l'allocation 60 / 40, justifiée (ratio de Sharpe, écart type sous le plafond de la charte, bêta, coût en rentabilité espérée) et réponse à l'objection du directeur financier | 1 |
| 1.6-02 | Portefeuille obligataire : transfert d'environ 240 M€ de la ligne C vers la ligne A pour ramener la duration à 3,39 ans ; effet résiduel et coût en rendement ; réponse à l'objection de l'administrateur | 1 |
| 1.6-03 | Prise en compte des engagements envers les sociétaires, de l'horizon et du statut mutualiste ; forme d'une note structurée, chiffrée et conclusive | 1 |

**Montant à transférer.** Chaque M€ déplacé de la ligne C (8,000 ans) vers la ligne A (1,980 an) réduit la somme des valeurs × durations de 6,020. Pour atteindre la duration des engagements :
transfert = (4,474 − 3,386) × 1 330,00 / (8,000 − 1,980) = 1,088 × 1 330,00 / 6,020 = **240,37 M€**, soit environ 240 M€ sur les 296,80 M€ de la ligne C. Après le transfert, la ligne A vaut 713,89 M€, la ligne C 56,43 M€, et la variation estimée de l'actif pour + 100 points de base n'est plus que de − 43,63 M€, contre − 37,69 M€ pour les engagements : l'écart ne baisse plus que de 5,94 M€ au lieu de 19,83 M€. Le reliquat vient de l'excédent de l'actif sur les engagements (183,35 M€) ; la cible « en euros » de 2,919 ans demanderait un transfert de (4,474 − 2,919) × 1 330,00 / 6,020 = 343,55 M€, supérieur à la ligne C, donc une réduction de la ligne B ou un recours aux placements monétaires.

**Exemple de note**

> **Note à l'attention du conseil d'administration de la Mutuelle d'assurances VERCÈNE**
> *Objet : politique de placement de 2028 — adossement des obligations aux règlements des sinistres et allocation de la poche actions*
> *Établie à la demande de Mme Claire ESTAGNOL et de M. Julien PERDRIEL, à partir des données au 31 décembre 2026*
>
> **1. Le portefeuille obligataire est plus exposé à la hausse des taux que nos engagements.** Nos obligations (1 330,00 M€) ont une duration de 4,47 ans, alors que les règlements prévus des sinistres déjà survenus (1 146,65 M€ en valeur actualisée) ont une duration de 3,39 ans. Une hausse d'un point des taux ferait perdre 57,52 M€ aux obligations et réduirait de 37,69 M€ la valeur des engagements : l'excédent de l'actif reculerait de 19,83 M€, soit 3,25 % de nos fonds propres. La ligne C (titres à coupon zéro à 8 ans) concentre ce risque : 22 % de la valeur, 40 % de la duration.
>
> **2. Nous recommandons de ramener la duration à celle des engagements.** Céder environ 240 M€ de la ligne C pour acquérir des titres de la ligne A ramène la duration à 3,39 ans et limite la baisse de l'excédent à environ 6 M€ pour un point de hausse. Le coût est réel : l'écart de taux actuariel entre les deux lignes (3,80 % contre 2,70 %) représente environ 2,64 M€ de rendement par an. C'est le prix d'une protection : la ligne C offre le taux le plus élevé parce qu'elle porte le risque de taux le plus fort. Conserver une partie de la ligne C (environ 57 M€) reste possible : l'excédent des obligations sur les engagements (183,35 M€), qui n'est pas destiné à payer les sinistres déjà survenus, peut être placé plus longtemps. L'adossement devra être revu chaque année, et après tout sinistre important, car les règlements et les taux changent.
>
> **3. Nous recommandons de porter la part du fonds d'infrastructures à 40 % de la poche actions.** L'allocation proposée par VERCÈNE Gestion (60 % / 40 %) ramène l'écart type de la poche de 16,06 % à 14,06 %, sous le plafond de 15,00 % de notre charte, que l'allocation actuelle dépasse. Elle ne coûte que 0,20 point de rentabilité espérée (8,10 % contre 8,30 %, soit 0,46 M€ par an) et améliore le ratio de Sharpe (0,29 contre 0,27). Le fonds d'infrastructures a certes moins rapporté que le fonds d'actions européennes, mais sa rentabilité a dépassé ce qu'exigeait son faible bêta (7,50 % contre 6,50 %), et l'essentiel de son risque, propre à ses secteurs, se dilue dans la poche. Le bêta de la poche passe de 0,98 à 0,86.
>
> **4. Ces choix servent d'abord nos sociétaires.** La mutuelle n'a pas d'actionnaires à qui demander des fonds propres : ses fonds propres (610 M€) se reconstituent principalement par ses résultats et garantissent, avec la réassurance, le paiement des sinistres au-delà des placements adossés. Nos placements doivent donc d'abord permettre de payer les sinistres à leur échéance, sans vendre dans un marché défavorable. La poche actions, sans retrait prévu avant 2035, peut supporter des variations de court terme, mais leur ampleur doit rester mesurée. La hausse des sinistres climatiques plaide aussi pour des titres plus courts et liquides.
>
> **Décisions proposées** : (1) transfert d'environ 240 M€ de la ligne C vers la ligne A au cours du second semestre 2027 ; (2) allocation de la poche actions à 60 % / 40 % au 1er janvier 2028 ; (3) suivi semestriel de la duration de l'actif et des engagements et de l'écart type de la poche actions par le comité financier.

**Réponses tolérées** : transfert calculé avec la cible de 2,919 ans, si le candidat montre qu'il dépasse la ligne C et propose de réduire aussi la ligne B ; transfert vers des placements monétaires ou vers une ligne courte autre que A, s'il est chiffré de façon cohérente ; transfert progressif ; maintien de l'allocation actuelle de la poche actions si le candidat traite le dépassement du plafond de la charte et propose une autre mesure (réduction de la poche) ; montants arrondis (240 M€, 57 M€).

**Erreurs fréquentes**
- Recommander de conserver la ligne C pour son taux élevé, sans voir qu'il rémunère le risque de taux.
- Note sans chiffres, ou qui reprend les calculs sans recommandation ni calendrier.
- Ignorer la charte de placement (plafond de 15,00 %) ou le statut mutualiste (absence d'actionnaires, fonds propres reconstitués principalement par les résultats).
- `JUR-T01` — note qui ne s'adresse pas au conseil d'administration ; `JUR-T13` — recommandation générale sans lien avec les chiffres du dossier ; `JUR-T08` — note sans structure ni phrases directes.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 77-78 ; programme l. 615-617 | relation inverse entre la valeur et les taux ; logique de duration et de sensibilité ; diagnostic d'une exposition au risque de taux | [V] | F07 § 2.1 |
| Duration de Macaulay, sensibilité, effet de la courbure | formules usuelles, exemple vérifié | [S] | F07 § 2.1 |
| Guide pédagogique DSCG, juillet 2026, p. 74-76 ; programme l. 578-592 | rentabilité espérée, variance, écart type, bêta ; MEDAF et ses limites ; risque systématique et spécifique ; diversification ; portefeuille de deux titres ; ratio de Sharpe | [V] | F10 |
| Markowitz (1952) | diversification ; rôle de la corrélation ; risque spécifique diversifiable, risque systématique non diversifiable | [V programme 5.3] | F10 |
| Sharpe (1964) ; ratio de Sharpe | MEDAF ; prime par unité de risque total | [V contexte ; MEDAF au programme 5.2] | F10 |
| Jensen (1968), facultatif | écart entre rentabilité observée et rentabilité exigée | [S] | F10 |
| Taux sans risque de 4,00 % et prime de risque du marché de 5,00 % | ordres de grandeur d'octobre 2026, posés comme hypothèses d'énoncé | [V] | F11 § 1 et 2 |
| Placements, lignes obligataires, taux du marché, règlements des sinistres, rentabilités des fonds et de l'indice, corrélation, charte de placement | hypothèses d'énoncé, fictives, à utiliser telles quelles | — | annexes 1.1 à 1.5 |
