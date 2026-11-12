# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Sujet d'entraînement complet n° 11

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue2/fiches/`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (investissement, emprunts, coût du capital, DCF, multiples, portefeuille, LBO, BPA, équilibre des bilans, couvertures, barème sur 50, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Adosser les placements aux engagements : risque de taux et poche actions | 18 | 1.1 à 1.6 | `exercices/ex31_adossement_placements_mutuelle` |
| 2 – Un épisode de grêle : coût du sinistre, transfert du risque climatique et liquidité du groupe | 16 | 2.1 à 2.5 | `exercices/ex32_grele_reassurance_tresorerie` |
| 3 – Entrer au capital d'une jeune société de courtage en ligne : choisir la méthode d'évaluation selon le cycle de vie | 16 | 3.1 à 3.5 | `exercices/ex33_entree_capital_courtier_en_ligne` |
| **Total** | **50** | | |

---

## DOSSIER 1 – ADOSSER LES PLACEMENTS AUX ENGAGEMENTS : RISQUE DE TAUX ET POCHE ACTIONS (18 points)

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

---

## DOSSIER 2 – UN ÉPISODE DE GRÊLE : COÛT DU SINISTRE, TRANSFERT DU RISQUE CLIMATIQUE ET LIQUIDITÉ DU GROUPE (16 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Coût de l'épisode, indemnité du réassureur, effets sur le résultat technique et la trésorerie | `6.4.a` Sensibiliser aux instruments de couverture des risques physiques et financiers liés au changement climatique et à la raréfaction des ressources naturelles | 3 |
| 2.2 Réassurance, couverture paramétrique et obligation catastrophe | `6.4.a` Sensibiliser aux instruments de couverture des risques physiques et financiers liés au changement climatique et à la raréfaction des ressources naturelles | 2,5 |
| 2.3 Centralisation de la trésorerie du groupe | `6.1.a` Appliquer les mécanismes de centralisation de trésorerie | 3,5 |
| 2.4 Centralisation physique ou notionnelle, financement du besoin et placement de l'indemnité | `6.1.b` Discerner les différents types de financement et de placement ; `6.1.a` Appliquer les mécanismes de centralisation de trésorerie | 3 |
| 2.5 Contrats à terme sur Euribor 3 mois pour le placement de l'indemnité | `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) | 4 |
| **Total** | | **16** |

Part du calcul : environ 9 points (2.1-01 à 2.1-06, 2.2-02 et 2.2-03, 2.3-01 à 2.3-04, 2.5-02 à 2.5-05). Part de l'analyse : environ 7 points. La question 2.4, entièrement rédigée, et les limites de la couverture (2.5-06) ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 2.1 Coût de l'épisode, indemnité du réassureur, effets sur le résultat technique et la trésorerie (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Sinistres 55,20 M€ ; frais 3,30 M€ (experts 2,20, gestion interne 1,10) ; coût brut 58,50 M€ | 0,5 |
| 2.1-02 | Sinistre au sens du traité 57,40 M€ (frais internes exclus) ; un seul événement (deux jours, dans une même période de 72 heures) | 0,5 |
| 2.1-03 | Indemnité = min(40,00 ; 57,40 − 20,00) = 37,40 M€ ; portée non épuisée (2,60 M€ disponibles) | 0,5 |
| 2.1-04 | Prime de reconstitution 1,87 M€ ; coût net 58,50 + 1,87 − 37,40 = 22,97 M€ | 0,5 |
| 2.1-05 | Résultat technique de 2027 : 40,00 → 17,03 M€ | 0,5 |
| 2.1-06 | Trésorerie de 2027 : décaissements 47,10 M€, encaissement de 37,40 M€ le 1er décembre, effet net de − 9,70 M€ (158,00 → 148,30 M€) ; commentaire de l'écart (13,27 M€ décaissés en 2028, besoin temporaire avant le 1er décembre) | 0,5 |

**Coût brut de l'épisode (0,5 pt).**

| Poste (M€) | Coût après expertise | Dont réglé en 2027 |
|---|---:|---:|
| Récoltes | 21,40 | 16,40 |
| Serres et cultures sous abri | 5,80 | 4,60 |
| Bâtiments agricoles et matériel | 9,60 | 6,40 |
| Habitations et locaux professionnels | 12,30 | 10,30 |
| Véhicules | 6,10 | 6,10 |
| **Sinistres** | **55,20** | **43,80** |
| Honoraires des experts extérieurs | 2,20 | 2,20 |
| Frais internes de gestion | 1,10 | 1,10 |
| **Coût brut** | **58,50** | **47,10** |

Les récoltes pèsent 39 % des sinistres (21,40 / 55,20, calcul facultatif) : l'épisode frappe d'abord les exploitants agricoles, qui sont à l'origine de la mutuelle et apportent 38 % de ses cotisations.

**Sinistre au sens du traité (0,5 pt).** Les deux jours d'orages (21 et 22 juin) tombent dans une même période de 72 heures : ils forment **un seul événement**, auquel s'applique une seule priorité. Le sinistre retenu par le traité comprend les indemnités dues aux sociétaires et les honoraires des experts extérieurs, mais pas les frais internes : 55,20 + 2,20 = **57,40 M€**.

**Indemnité du réassureur (0,5 pt).** Le traité en excédent de sinistre joue comme une assurance avec franchise et plafond : la priorité (20,00 M€) reste à la charge de la mutuelle, le réassureur paie au-delà, dans la limite de la portée (40,00 M€).
- Sinistre au-delà de la priorité : 57,40 − 20,00 = 37,40 M€, inférieur à la portée.
- **Indemnité = 37,40 M€**, soit 65 % du sinistre retenu (calcul facultatif). La portée n'est pas épuisée : il reste 2,60 M€ de capacité ; un événement dont le sinistre dépasserait 60,00 M€ (priorité + portée) laisserait le surplus à la mutuelle.

**Coût net (0,5 pt).** La reconstitution de la portée coûte 5 % × 37,40 = **1,87 M€**.

| M€ | Montant |
|---|---:|
| Coût brut | 58,50 |
| Prime de reconstitution | + 1,87 |
| Indemnité du réassureur | − 37,40 |
| **Coût net pour la mutuelle** | **22,97** |

Le coût net se lit aussi par ce que le traité laisse à la mutuelle : priorité 20,00 + frais internes 1,10 + reconstitution 1,87 = 22,97 M€.

**Résultat technique de 2027 (0,5 pt).** Le coût net est imputé en totalité à 2027 (annexe 2.6) : résultat technique 40,00 − 22,97 = **17,03 M€**, en baisse de 57 % (calcul facultatif). Après impôt, l'effet sur le résultat net serait de 22,97 × 0,75 = 17,23 M€ (calcul facultatif).

**Trésorerie de 2027 et commentaire (0,5 pt).**
- Décaissements de 2027 : 43,80 + 2,20 + 1,10 = 47,10 M€ ; encaissement de l'indemnité le 1er décembre : 37,40 M€.
- **Effet net sur la trésorerie de 2027 : − 9,70 M€** : trésorerie au 31 décembre 158,00 → **148,30 M€**.
- L'effet sur le résultat (22,97 M€) dépasse l'effet sur la trésorerie (9,70 M€) de 13,27 M€ : le solde des règlements (11,40 M€) et la prime de reconstitution (1,87 M€) ne seront décaissés qu'en 2028.
- Le chiffre de fin d'année masque un **besoin temporaire** : la mutuelle règle les sociétaires dès juillet, alors que le réassureur ne paie que le 1er décembre. Jusqu'à cette date, elle avance la quasi-totalité des 47,10 M€ : la réassurance protège le résultat, pas la trésorerie de l'automne (questions 2.3 et 2.4).
- Pour une mutuelle sans actionnaires, le résultat est la seule source de renforcement des fonds propres (610 M€) : l'épisode en consomme une part modeste (environ 4 %, calcul facultatif), mais il annonce des événements plus fréquents (un tiers des sinistres payés sont climatiques).

**Réponses tolérées** : coût net présenté sans la prime de reconstitution (21,10 M€) si celle-ci est ensuite ajoutée à l'effet sur le résultat ; effet après impôt donné en complément ; trésorerie exprimée par le seul effet net (− 9,70 M€) sans le niveau de fin d'année.

**Erreurs fréquentes**
- `JUR-T03` — inclure les frais internes dans le sinistre du traité (base 58,50, indemnité 38,50 M€), ou compter deux événements et deux priorités pour deux jours d'orages.
- Appliquer la portée au sinistre total (indemnité = min(40 ; 57,40) = 40,00 M€) au lieu de la part qui dépasse la priorité ; oublier la prime de reconstitution.
- Confondre l'effet sur le résultat et l'effet sur la trésorerie ; ignorer la date de versement de l'indemnité.

---

### 2.2 Réassurance, couverture paramétrique et obligation catastrophe (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Mutualisation et transfert par la réassurance ; ce que le traité laisse à la mutuelle : priorité, frais internes, reconstitution, part au-delà de 60 M€, délai de paiement, cumul de plusieurs événements | 1 |
| 2.2-02 | Couverture paramétrique : versement de 16,00 M€ en juin 2027 et nul en mai 2024 (risque de base) ; coût 1,60 M€ par an ; rapidité du paiement | 0,5 |
| 2.2-03 | Obligation catastrophe : coût de 3,60 M€ par an (et 1,50 M€ de frais de mise en place), coupon de 8,40 % pour les investisseurs ; aucun capital perdu en juin 2027 (sinistre de 57,40 M€ sous le seuil de 60 M€) ; avantages et limites | 0,5 |
| 2.2-04 | Conclusion pour une mutuelle régionale à risque concentré | 0,5 |

**Mutualisation et transfert (1 pt).**
- **Mutualisation** : la mutuelle répartit entre 410 000 sociétaires le coût des sinistres de quelques-uns ; cette mutualisation est efficace pour des risques nombreux et indépendants (incendie, vol), mais pas pour un orage qui frappe des milliers de sociétaires le même jour sur deux départements : le risque climatique est **concentré** (corrélé) sur son territoire.
- **Transfert** : le réassureur, qui couvre des risques dans de nombreuses régions et sur plusieurs continents, mutualise à son tour des événements peu liés entre eux : il diversifie un risque que la mutuelle ne peut pas diversifier. On retrouve l'idée de Markowitz (1952) : le risque d'un ensemble dépend des corrélations entre ses éléments.
- **Ce que le traité laisse à la mutuelle** (application au cas) :
  - la **priorité** de 20,00 M€ par événement, que plusieurs événements de l'année feraient jouer plusieurs fois (un orage en juin, une tempête en décembre) ;
  - les **frais internes** (1,10 M€) et la **prime de reconstitution** (1,87 M€) ;
  - le sinistre au-delà de **60,00 M€** (priorité + portée), c'est-à-dire l'événement extrême ;
  - le **décalage de trésorerie** : le paiement n'intervient que le 1er décembre, sans avance ;
  - le **risque de renouvellement** : après un sinistre, le réassureur peut relever la prime ou la priorité ; le risque de contrepartie sur le réassureur, limité par le groupe de réassureurs.

**Couverture paramétrique (0,5 pt).** Versement = 0,05 × (indice − 300), dans la limite de 20,00 M€.

| Épisode | Indice | Versement | Part du sinistre au sens du traité restée à la charge de la mutuelle |
|---|---:|---:|---:|
| Juin 2027 | 620 | 0,05 × 320 = **16,00 M€** | 20,00 M€ (la priorité ; coût net de la question 2.1 : 22,97 M€) |
| Mai 2024 | 240 | **0** (indice sous 300 mailles) | 17,80 M€ |

- Avantages : paiement **rapide** (dans les 30 jours de la publication de l'indice, soit au plus tard début août pour l'épisode de juin 2027, quatre mois avant le réassureur) et sans expertise, ce qui aurait couvert une grande part de la pointe de trésorerie ; mesure objective, publiée par un tiers ; elle couvre la tranche de la priorité, que le traité laisse à la mutuelle (en juin 2027, 16,00 M€ sur 20,00 M€, soit 80 %). Coût : 1,60 M€ par an, soit 8 % du versement maximal (calcul facultatif).
- Limite : le **risque de base** : le versement dépend de l'indice, pas du sinistre. En mai 2024, une grêle très localisée sur des cultures de forte valeur a coûté 17,80 M€ sans déclencher de versement ; à l'inverse, un indice élevé sur une zone peu assurée par la mutuelle paierait plus que la perte.

**Obligation catastrophe (0,5 pt).**
- Coût annuel pour la mutuelle : 6,00 % × 60,00 = **3,60 M€**, plus **1,50 M€** de frais de mise en place ; les investisseurs reçoivent 2,40 % + 6,00 % = **8,40 %** par an, un coupon élevé qui rémunère le risque de perdre leur capital.
- Juin 2027 : sinistre de 57,40 M€, sous le seuil de 60,00 M€ : **aucun capital perdu**, rien n'est versé à la mutuelle. Pour un événement de 95 M€, les investisseurs perdraient 95 − 60 = 35,00 M€, versés à la mutuelle (calcul facultatif).
- Avantages : elle couvre la tranche **au-delà du traité** (de 60 à 120 M€), celle de l'événement extrême, le « cygne noir » au sens de Taleb (2007) ; la somme est placée en garantie dès l'émission, ce qui réduit fortement le risque de contrepartie ; le prix est fixé pour trois ans. Le déclencheur repose sur le sinistre du traité : pas de risque de base.
- Limites : coût élevé et frais fixes lourds pour une émission de petite taille ; montage complexe (structure dédiée, modélisation, notation) ; transparence exigée sur les sinistres ; capacité dépendante de l'appétit des investisseurs, qui recherchent un risque indépendant des marchés financiers mais le paient cher quand il est concentré sur deux départements.

**Conclusion (0,5 pt).**
- Le **traité en excédent de sinistre** reste l'outil central : il couvre la tranche la plus probable des événements graves (20 à 60 M€) et a pris en charge 37,40 M€ en 2027.
- La **couverture paramétrique** peut compléter la priorité et apporter de la liquidité rapide, mais son risque de base est réel sur un territoire de cultures de forte valeur et de grêles localisées : à n'étudier qu'avec un indice plus fin ou un seuil plus bas, et pour un montant limité.
- L'**obligation catastrophe** ne se justifie que si la mutuelle juge probable un événement de plus de 60 M€ et si les réassureurs réduisent leur capacité ou relèvent fortement leurs prix ; pour une mutuelle régionale, une tranche supplémentaire de réassurance traditionnelle est en général moins coûteuse. Aucun instrument ne réduit le risque physique lui-même : la prévention (filets paragrêle, normes de toitures, conseils aux sociétaires) relève de la même politique de gestion des risques.

**Réponses tolérées** : comparaison des coûts annuels rapportés à la capacité couverte (traité 4,40 / 40 = 11 % ; paramétrique 8 % ; obligation 6 %), donnée en complément ; recommandation d'une obligation catastrophe si elle est justifiée par la hausse de la fréquence des événements et le risque de renouvellement du traité.

**Erreurs fréquentes**
- `JUR-T13` — définitions générales de la réassurance et des obligations catastrophe sans les chiffres du cas (priorité, seuil de 60 M€, versement de 16 M€, épisode de mai 2024).
- Confondre la couverture paramétrique avec une assurance de dommages (elle ne mesure pas la perte) ; croire que l'obligation catastrophe aurait payé en juin 2027.
- Tenter de valoriser l'obligation ou de calculer une probabilité d'événement : non demandé, tous les paramètres sont donnés.

---

### 2.3 Centralisation de la trésorerie du groupe (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Intérêts de chaque société sans centralisation, au taux débiteur ou créditeur selon le signe du solde : − 229 264 € ; 9 462 € ; 22 729 € | 1 |
| 2.3-02 | Total sans centralisation : charge nette de 197 073 € | 0,5 |
| 2.3-03 | Soldes nets du groupe (− 2,50 ; − 14,00 ; − 20,50 M€) et intérêts du compte centralisateur (− 106 155 €) ; résultat avec centralisation, frais compris : − 119 655 € | 0,5 |
| 2.3-04 | Gain de la centralisation : 77 418 € sur trois mois | 0,5 |
| 2.3-05 | Origine du gain : compensation des soldes de signe contraire (environ 64 k€) et meilleures conditions du compte centralisateur (environ 26,5 k€), moins les frais (13,5 k€) ; lecture | 1 |

**Intérêts sans centralisation (1 pt).** Intérêts d'un mois = solde × taux × jours / 360, au taux débiteur si le solde est négatif, au taux créditeur s'il est positif.

| Euros | Septembre (30 j) | Octobre (31 j) | Novembre (30 j) | Total |
|---|---:|---:|---:|---:|
| Mutuelle (débitrice, 4,25 %) | − 42 500 | − 80 514 | − 106 250 | **− 229 264** |
| VERCÈNE Courtage (créditrice, 1,25 %) | 3 646 | 2 691 | 3 125 | **9 462** |
| VERCÈNE Gestion (créditrice, 1,50 %) | 7 500 | 7 104 | 8 125 | **22 729** |
| **Total sans centralisation** | − 31 354 | − 70 719 | − 95 000 | **− 197 073** |

Exemple : mutuelle en octobre, − 22 000 000 × 4,25 % × 31 / 360 = − 80 514 €. Chaque société gardant le même signe sur les trois mois, on peut aussi calculer par société sur les capitaux × jours (mutuelle : 1 942 M€ × jours × 4,25 % / 360).

**Total sans centralisation (0,5 pt).** Le groupe paie **197 073 €** d'intérêts nets en trois mois, alors que ses filiales disposent de 8 à 9,5 M€ d'excédents.

**Avec centralisation (0,5 pt).** Le compte centralisateur porte chaque jour la somme des soldes.

| | Septembre | Octobre | Novembre | Total |
|---|---:|---:|---:|---:|
| Solde net du groupe (M€) | − 2,50 | − 14,00 | − 20,50 | |
| Intérêts au taux débiteur de 3,40 % (€) | − 7 083 | − 40 989 | − 58 083 | **− 106 155** |
| Frais (3 × 4 500 €) | | | | − 13 500 |
| **Résultat avec centralisation** | | | | **− 119 655** |

**Gain (0,5 pt).** Gain = − 119 655 − (− 197 073) = **77 418 €** sur trois mois, soit près de 40 % de la charge d'intérêts initiale (calcul facultatif).

**Origine du gain (1 pt).**
- **Compensation des soldes de signe contraire** : sans centralisation, les excédents des filiales sont rémunérés à 1,25 % et 1,50 % pendant que la mutuelle emprunte à 4,25 %. Centralisés, ils réduisent d'autant le découvert du groupe : chaque euro d'excédent « gagne » l'écart entre le taux débiteur de la mutuelle et le taux créditeur de la filiale, soit environ 22,7 k€ pour Courtage et 41,7 k€ pour Gestion (calcul facultatif).
- **Meilleures conditions du compte centralisateur** : le découvert net restant est facturé 3,40 % au lieu de 4,25 %, soit environ 26,5 k€ (calcul facultatif) : la banque principale consent un meilleur taux au groupe pris dans son ensemble, dont elle voit tous les soldes, et le groupe pèse davantage dans la négociation.
- **Moins les frais** de 13,5 k€ : environ 64,4 + 26,5 − 13,5 = 77,4 k€.
- Lecture : le gain augmente avec l'écart entre taux débiteur et créditeur et avec la simultanéité de soldes de signe contraire. Ici, l'essentiel du besoin (jusqu'à 20,50 M€ net en novembre) subsiste après centralisation : la centralisation réduit le coût du besoin, elle ne le finance pas (question 2.4).

**Réponses tolérées** : intérêts calculés par société sur les capitaux × jours sans arrondi mensuel (écart de 1 € : 106 156 € au lieu de 106 155 €) ; frais comptés pour trois mois et gain présenté comme une économie d'intérêts ; décomposition du gain présentée sans chiffres, à partir d'un raisonnement juste.

**Erreurs fréquentes**
- Appliquer à un solde négatif le taux créditeur, ou le taux du compte centralisateur aux soldes des sociétés sans centralisation.
- Oublier les frais, ou les compter pour une année entière (54 000 €).
- `JUR-T04` — erreur de base de calcul (jours / 365 ou mois / 12 au lieu de jours / 360).

---

### 2.4 Centralisation physique ou notionnelle, financement du besoin et placement de l'indemnité (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Centralisation physique et notionnelle comparées : autonomie des filiales, visibilité, sécurité, prérequis | 1 |
| 2.4-02 | Choix de la ressource pour la pointe : placements monétaires dans la limite du plancher de 80 M€, ligne de crédit en secours, refus de la cession d'obligations | 1 |
| 2.4-03 | Support de placement de l'indemnité, cohérent avec l'horizon de 90 jours, le couple rendement-risque et la liquidité | 1 |

**Centralisation physique ou notionnelle (1 pt).**

| Critère | Physique (mise à zéro quotidienne) | Notionnelle (fusion des échelles d'intérêts) |
|---|---|---|
| Autonomie des filiales | réduite : leurs fonds remontent chaque soir au compte centralisateur ; elles détiennent une créance (ou une dette) sur la mutuelle, rémunérée par une convention de trésorerie | préservée : chaque société garde ses comptes, ses banques et ses fonds ; seuls les intérêts sont calculés sur le solde global |
| Visibilité | complète et quotidienne : un seul solde, utilisable par la mutuelle pour placer ou financer | partielle : la position globale est connue, mais les fonds restent dispersés et ne peuvent pas être utilisés par une autre société |
| Sécurité | fonds réunis et contrôlés par la direction financière du groupe, moins de comptes ouverts ; en revanche, risque concentré sur une banque et sur la mutuelle, et besoin de règles internes | pas de mouvement de fonds ; mais garanties croisées des trois sociétés exigées par la banque et dépendance à la transmission quotidienne des soldes par trois banques |
| Prérequis | convention de trésorerie, conditions internes proches du marché, accord des dirigeants des filiales | accord de la banque principale et des autres banques, garanties croisées |

Application : les trois sociétés sont françaises, en euros, détenues à 100 % : rien n'empêche la centralisation physique, qui permet en plus à la mutuelle d'utiliser réellement les excédents des filiales pendant la pointe. VERCÈNE Gestion, société de gestion de portefeuille, doit garder une trésorerie propre suffisante à son activité : les conditions internes et un solde minimal peuvent y pourvoir. La centralisation notionnelle conviendrait surtout si les filiales tenaient à leurs banques ou si les transferts de fonds étaient contraints.

**Ressource pour couvrir le besoin (1 pt).** Le besoin est **temporaire** (septembre à novembre, jusqu'à 30 M€ pour la mutuelle et 20,50 M€ pour le groupe centralisé) et son terme est connu (1er décembre).
- **Cession d'obligations : à écarter.** Placement de long terme pour un besoin de trois mois : la vente cristalliserait une moins-value de 6 % en moyenne (de l'ordre de 1,2 M€ pour 20 M€ cédés, calcul facultatif), plus les frais, et ferait perdre un rendement de 3,20 % ; elle déformerait aussi l'adossement des obligations à l'échéancier des règlements futurs. Le coût dépasse de loin celui des autres solutions.
- **Rachat de parts d'OPCVM monétaires : solution principale.** Liquidité en un jour, aucun frais, coût d'opportunité d'environ 2,35 % l'an, inférieur au coût de la ligne de crédit (3,50 %). Le plancher de 80 M€ laisse 140 − 80 = 60 M€ mobilisables, plus que la pointe : la mutuelle peut racheter au fur et à mesure des besoins et reconstituer ces placements avec l'indemnité.
- **Ligne de crédit confirmée de 40 M€ : en secours.** Elle coûte plus cher (3,50 % sur les tirages, 0,25 % sur la partie non tirée, que la mutuelle paie déjà) mais préserve la réserve de liquidité : à tirer si un nouvel événement climatique survenait à l'automne et faisait descendre les placements monétaires vers leur plancher. Le découvert du compte centralisateur, un peu moins cher (3,40 %), n'est pas confirmé : la banque peut le retirer au moment où le groupe en a le plus besoin ; la ligne, confirmée jusqu'en 2029, est la vraie ressource de secours.
- Conclusion : rachats d'OPCVM monétaires dans la limite du plancher, après centralisation de la trésorerie des filiales, et ligne de crédit maintenue en réserve.

**Placement de l'indemnité (1 pt).** Montant connu (37,40 M€), horizon connu de 90 jours (paiements du 29 février 2028), objectif de sécurité du capital.
- **Compte à terme de 3 mois : recommandé** pour l'essentiel. Le capital est garanti, l'échéance coïncide avec le besoin et le taux est fixé pour toute la durée dès l'ouverture, ce qui permet de le protéger dès aujourd'hui par des contrats à terme (question 2.5). La pénalité de sortie anticipée n'est pas gênante puisque l'horizon est certain. Limite : concentration sur une seule banque.
- **NEU CP à 3 mois** : rendement un peu supérieur (20 points de base de plus que le compte à terme), mais risque de crédit de chaque émetteur et titres à conserver jusqu'à l'échéance ; une fraction diversifiée sur plusieurs émetteurs bien notés est acceptable.
- **OPCVM monétaire** : utile pour la part qui pourrait être appelée avant l'échéance, mais rendement variable, exposé à la baisse de l'€STR que craint M. PERDRIEL.
- **Obligations à 5 ans : à écarter** : horizon sans rapport avec le besoin, risque de taux.

**Réponses tolérées** : recours principal à la ligne de crédit si le candidat justifie la volonté de garder intacte la réserve monétaire face au risque d'un second événement ; secours assuré par le découvert du compte centralisateur si le candidat relève qu'il n'est pas confirmé et en tire la limite ; répartition de l'indemnité entre compte à terme et NEU CP ; choix de la centralisation notionnelle s'il est justifié par l'autonomie de VERCÈNE Gestion.

**Erreurs fréquentes**
- `JUR-T13` — liste des avantages de chaque solution sans rapprochement avec les données du cas (plancher de 80 M€, moins-value de 6 %, horizon de 90 jours).
- Financer un besoin de trois mois par la cession de placements de long terme ; placer une somme à horizon connu sur un support risqué.
- S'écarter de l'analyse financière : la question porte sur le coût, l'horizon et le risque, pas sur la rédaction des accords entre les sociétés du groupe.

---

### 2.5 Contrats à terme sur Euribor 3 mois pour le placement de l'indemnité (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Risque : baisse des taux d'ici au 1er décembre ; achat de contrats ; cotation 100 − taux, taux de 2,45 % assuré par le cours de 97,55, soit un taux visé de 2,35 % pour le placement | 0,5 |
| 2.5-02 | 37,40 contrats arrondis à 37 ; valeur du point 25 € ; dépôt de garantie 22 200 € ; principe des appels de marge | 1 |
| 2.5-03 | Scénario de baisse (1,85 %) : gain de 55 500 €, intérêts 163 625 €, produit total 219 125 €, taux de 2,34 % | 0,5 |
| 2.5-04 | Scénario de hausse (2,85 %) : perte de 37 000 €, intérêts 257 125 €, produit total 220 125 €, taux de 2,35 % | 0,5 |
| 2.5-05 | Comparaison sans couverture (1,75 % ou 2,75 %) : taux stabilisé autour de 2,35 %, renonciation au gain en cas de hausse | 0,5 |
| 2.5-06 | Limites : risque de base (dates, taux du placement), nombre entier de contrats, appels de marge à financer, instrument ferme | 1 |

**Risque et principe (0,5 pt).** La mutuelle placera 37,40 M€ le 1er décembre à un taux fixé ce jour-là : elle est exposée à une **baisse** des taux entre le 1er septembre et le 1er décembre. Le contrat est coté 100 − taux : si les taux baissent, son cours monte. La mutuelle **achète** des contrats aujourd'hui à 97,55 et les revendra le 1er décembre : le gain sur les contrats compensera la baisse des intérêts. Le cours de 97,55 correspond à un taux de 100 − 97,55 = **2,45 %** pour l'Euribor 3 mois de décembre (le marché anticipe déjà une baisse par rapport à 2,65 %) ; le compte à terme étant rémunéré 10 points de base de moins, le taux visé est de **2,35 %**.

**Nombre de contrats, dépôt et appels de marge (1 pt).**
- Nombre de contrats = 37 400 000 / 1 000 000 × (3 mois / 3 mois) = 37,4, arrondi à **37 contrats** ; 0,40 M€ restent non couverts.
- Valeur d'un point de base : 1 000 000 × 0,01 % × 3 / 12 = **25 €** par contrat.
- Dépôt de garantie : 37 × 600 = **22 200 €**, versé à l'achat et restitué au dénouement.
- **Appels de marge** : chaque jour, la chambre de compensation crédite ou débite le compte de la mutuelle de la variation de valeur de ses contrats, au cours de compensation de la séance (gain si le cours monte, perte s'il baisse). Ces règlements quotidiens garantissent la bonne fin des engagements et réduisent fortement le risque de contrepartie ; ils obligent la mutuelle à disposer de trésorerie si les taux montent avant décembre. La somme des appels de marge est égale au résultat final sur les contrats.

**Scénario de baisse : Euribor 3 mois de 1,85 % (0,5 pt).**
- Cours au 1er décembre : 100 − 1,85 = 98,15 ; gain = (98,15 − 97,55) × 100 points × 25 € × 37 = 60 × 25 × 37 = **55 500 €**.
- Intérêts du compte à terme : 37 400 000 × (1,85 % − 0,10 %) × 90 / 360 = 37 400 000 × 1,75 % × 90 / 360 = **163 625 €**.
- Produit total = **219 125 €** ; taux obtenu = 219 125 / (37 400 000 × 90 / 360) = **2,34 %**.

**Scénario de hausse : Euribor 3 mois de 2,85 % (0,5 pt).**
- Cours : 97,15 ; perte = 40 × 25 × 37 = **− 37 000 €**.
- Intérêts : 37 400 000 × 2,75 % × 90 / 360 = **257 125 €**.
- Produit total = **220 125 €** ; taux obtenu = **2,35 %**.

**Comparaison (0,5 pt).**

| Scénario | Taux sans couverture | Produit sans couverture | Produit avec couverture | Taux avec couverture |
|---|---:|---:|---:|---:|
| Baisse (1,85 %) | 1,75 % | 163 625 € | 219 125 € | 2,34 % |
| Hausse (2,85 %) | 2,75 % | 257 125 € | 220 125 € | 2,35 % |

La couverture stabilise le taux autour du taux visé de 2,35 % : elle protège contre la baisse (+ 55 500 €), mais fait renoncer au bénéfice d'une hausse (− 37 000 €), car le contrat à terme est un engagement ferme. L'écart à 2,35 % dans le scénario de baisse vient des 0,40 M€ non couverts (sans arrondi, le taux serait exactement de 2,35 % dans les deux scénarios, calcul facultatif).

**Limites (1 pt).**
- **Risque de base** : le contrat de décembre cesse d'être négocié le 13 décembre, alors que la position est dénouée le 1er décembre ; ce jour-là, son cours reflète l'Euribor attendu au 13 décembre et peut s'écarter de 100 − Euribor du 1er décembre, que l'énoncé suppose égal. De plus, le compte à terme est rémunéré sur un taux proposé par la banque, qui peut ne pas suivre exactement l'Euribor.
- **Nombre entier de contrats** : 37 contrats pour 37,4 M€ ; la couverture est imparfaite (ici sous-couverture de 0,40 M€). Le montant même de l'indemnité doit être certain : il l'est, le décompte étant arrêté au 31 octobre.
- **Appels de marge** : en cas de hausse des taux avant décembre, la mutuelle verse des appels de marge (37 000 € au total dans le scénario de hausse) et immobilise le dépôt de garantie : charge de trésorerie faible pour elle, mais à prévoir.
- **Instrument ferme et standardisé** : montants, échéances et taux de référence imposés ; aucune possibilité de profiter d'une hausse. Si la mutuelle voulait garder ce bénéfice, il lui faudrait une couverture optionnelle, avec une prime.
- Conclusion : pour 37 contrats, un coût limité au dépôt et aux frais de courtage, la mutuelle fixe dès le 1er septembre le rendement de l'indemnité à environ 2,35 %, ce qui convient à un placement de sécurité dont l'horizon est connu.

**Réponses tolérées** : nombre de contrats arrondi à 38 si la sur-couverture est signalée et commentée (gain de 57 000 € et perte de 38 000 € ; taux de 2,36 % et 2,34 %) ; résultat sur les contrats calculé comme nominal couvert × écart de taux × 3 / 12 (37 000 000 × 0,60 % × 3 / 12 = 55 500 €) ; taux exprimés à quatre décimales (2,3436 % et 2,3543 %).

**Erreurs fréquentes**
- Vendre les contrats (position de l'emprunteur qui craint une hausse) alors que la mutuelle place et craint une baisse.
- Calculer le résultat sur le nominal d'un contrat sans tenir compte du nombre de contrats, ou en oubliant le facteur 3 / 12 dans la valeur du point.
- Oublier les 10 points de base retranchés par la banque ; présenter les appels de marge comme une prime perdue.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme DSCG UE 2, partie 6 ; guide pédagogique DSCG, juillet 2026, p. 77-80 | centralisation de la trésorerie, supports de placement et de financement, futures de taux (cotation, nombre de contrats, appels de marge en principe), assurance et réassurance des risques climatiques, paramètres fournis | [V] | F07 § 0 ; `perimetre_ue2.yaml` 6.1, 6.2, 6.4 |
| Réassurance (quote-part, excédent de sinistre), obligations catastrophe | mutualisation et transfert, capital perdu si l'événement survient | [S] | F07 § 5 |
| Couverture paramétrique sur indice, risque de base | versement selon un indice mesuré, sans lien direct avec la perte ; présentée par analogie avec les dérivés climatiques sur indice | [S] | F07 § 5 (dérivés climatiques, risque de base) |
| Priorité, portée, événement de 72 heures, prime de reconstitution | vocabulaire usuel des traités en excédent de sinistre, conditions fixées par l'annexe 2.2 | [S] ; conditions : hypothèses d'énoncé | annexe 2.2 |
| Cash pooling physique et notionnel ; NEU CP, compte à terme, OPCVM monétaire | mécanismes, avantages et prérequis ; supports de placement | [S] | F07 § 4.1 et 4.2 ; F99 (NEU CP) |
| Contrat à terme sur Euribor 3 mois : nominal 1 000 000 €, cotation 100 − taux, 25 € par point de base | caractéristiques usuelles, posées dans l'annexe 2.5 | [S] (F07 § 2.2) ; [?] selon F07 § 7 | F07 § 2.2 et § 7 ; annexe 2.5 |
| Markowitz (1952) | diversification et corrélations, appliquées à la mutualisation par le réassureur | [V programme 5.3] | F10 § 2 |
| Taleb (2007), facultatif | événement extrême, à impact majeur | [V programme 5.1] | F10 § 1 |
| Euribor 3 mois de 2,65 %, €STR, rendement des placements en garantie de 2,40 % | ordres de grandeur d'octobre 2026, posés en hypothèses d'énoncé pour 2027 | hypothèses d'énoncé | F11 |
| Montants des sinistres, traité, offres, soldes et conditions bancaires, scénarios de taux | données fictives du cas | — | annexes 2.1 à 2.6 |

---

## DOSSIER 3 – ENTRER AU CAPITAL D'UNE JEUNE SOCIÉTÉ DE COURTAGE EN LIGNE : CHOISIR LA MÉTHODE D'ÉVALUATION SELON LE CYCLE DE VIE (16 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Cycle de vie et choix des méthodes | `3.3.c` Savoir calculer la valeur d'une entreprise en fonction de son cycle de vie | 1,5 |
| 3.2 ANC, ANCC, goodwill et limites de l'approche patrimoniale | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine ; `3.3.b` Savoir calculer la survaleur de l'entreprise à partir de ses actifs intangibles (goodwill) | 4,5 |
| 3.3 CMPC, flux actualisés, valeur terminale, VGE et VCP | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance ; `3.1.d` Distinguer la valeur globale de l'entreprise (VGE) de la valeur des capitaux propres (VCP) | 5,5 |
| 3.4 Méthode du capital-risque et comparaison des méthodes | `3.3.c` | 2,5 |
| 3.5 Fourchette, prix d'entrée et négociation | `3.3.c` ; `3.1.d` | 2 |
| **Total** | | **16** |

Part du calcul : environ 10 points (3.2-01 à 3.2-04, 3.3-01 à 3.3-06, 3.4-01 et 3.4-02, la moitié de 3.5-01 et de 3.5-02). Part de l'analyse : environ 6 points. Les questions 3.1, 3.4 et 3.5 relient les calculs au stade de développement de la société : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 Cycle de vie et choix des méthodes (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Stade de croissance, sortie de la phase de création, justifié par des indicateurs chiffrés : chiffre d'affaires + 200 %, + 116,67 % puis + 73,08 % ; clients + 72,22 % en 2026 ; premier résultat positif (0,05 M€) après 3,75 M€ de pertes ; flux négatifs en 2027 et 2028 (− 1,60 M€) ; croissance prévue ramenée de 55,56 % à 12,90 % | 0,5 |
| 3.1-02 | Méthodes adaptées et pourquoi : capital-risque (horizon de sortie, TRI exigé, risque d'échec) ; flux actualisés utiles mais fragiles (valeur terminale dominante) ; approche patrimoniale réduite à un plancher (valeur portée par l'immatériel) ; croiser les méthodes | 1 |

**Stade du cycle de vie (0,5 pt).** Le guide (p. 67) distingue quatre stades : création, croissance, maturité, déclin. ALTIMOISSON est **en croissance**, au sortir de la phase de création :
- **une croissance très rapide qui ralentit** : chiffre d'affaires de 0,40 M€ en 2023 à 4,50 M€ en 2026 (+ 200 % en 2024, + 116,67 % en 2025, + 73,08 % en 2026) ; exploitations clientes de 300 à 6 200 (+ 72,22 % en 2026) ; effectif de 6 à 41 personnes. Les prévisions gardent une forte croissance, en baisse régulière : + 55,56 % en 2027, + 12,90 % en 2031 ;
- **une rentabilité à peine atteinte** : 2026 est le premier exercice bénéficiaire (0,05 M€, soit 1,11 % du chiffre d'affaires), après 3,75 M€ de pertes cumulées de 2022 à 2025 ; la marge nette prévue atteint 14,86 % en 2031 ;
- **des besoins de financement** : les flux de trésorerie disponibles restent négatifs en 2027 et en 2028 (− 1,60 M€ au total), pour financer de nouveaux modules et des recrutements ; aucun dividende avant 2032 ;
- **une valeur surtout immatérielle et des risques élevés** : plateforme logicielle, fichier de clients, équipe, données ; dépendance envers trois assureurs (62 % du chiffre d'affaires) et quelques personnes clés.

Ce n'est plus une création (le produit est vendu, la société est rentable), ce n'est pas encore la maturité (croissance supérieure à 10 % par an, flux négatifs, résultat très faible).

**Méthodes adaptées à ce stade (1 pt).**
- **Méthode du capital-risque** : c'est la méthode d'évaluation propre aux jeunes sociétés au programme (guide, p. 67). Elle part de la valeur espérée à l'horizon de sortie de l'investisseur et l'actualise au TRI qu'il exige, qui rémunère le risque d'échec et l'illiquidité. Elle correspond exactement à la situation de la mutuelle : un apport minoritaire, une sortie envisagée dans cinq ans, un TRI fixé par son conseil.
- **Flux de trésorerie actualisés** : méthode de référence pour une entreprise en croissance, puisque sa valeur vient de ses flux futurs. Mais les premiers flux sont négatifs ou faibles, si bien que la valeur repose surtout sur la valeur terminale, et les prévisions sont établies par les dirigeants : la méthode est utile, à condition d'en mesurer la sensibilité.
- **Approche patrimoniale** : peu pertinente pour une société dont la valeur tient à l'immatériel et à la croissance. Elle donne un **plancher** (valeur des actifs si la croissance ne venait pas) ; le goodwill ne capte qu'une partie des perspectives.
- **Comparables** : possibles en théorie, mais les sociétés cotées comparables sont plus grandes et matures, et les agrégats d'ALTIMOISSON (résultat de 0,05 M€) sont trop faibles pour être multipliés ; le dossier ne les retient pas.
- Aucune méthode ne suffit seule : il faut **croiser** les approches pour bâtir une fourchette de négociation (`JUR-E03`).

**Réponses tolérées** : société qualifiée de « fin de création » ou de « début de croissance », si les indicateurs sont cités ; mention de l'approche par les multiples comme méthode de recoupement, sans calcul ; méthode des flux actualisés présentée comme méthode principale du stade de croissance (guide, p. 67), et méthode du capital-risque comme approche de l'investisseur minoritaire qui prévoit une sortie : réponse acceptée pour la totalité des points.

**Erreurs fréquentes**
- Qualifier la société de mature parce qu'elle a atteint l'équilibre, ou de start-up en création alors qu'elle réalise 4,50 M€ de chiffre d'affaires.
- Citer d'autres méthodes d'évaluation des jeunes sociétés, hors programme : seule la méthode du capital-risque est attendue.
- `JUR-T13` — exposé général sur le cycle de vie sans les chiffres de l'annexe 3.1.

---

### 3.2 ANC, ANCC, goodwill et limites de l'approche patrimoniale (4,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | ANC = 5,20 − 0,80 − 0,90 = 3,50 M€, soit 7,00 € par action | 0,5 |
| 3.2-02 | Corrections + 1,60 (plateforme) et + 1,20 (fichier de clients) ; impôt latent 0,70 ; ANCC = 3,50 + 2,80 − 0,70 = 5,60 M€, soit 11,20 € par action | 1 |
| 3.2-03 | Rentes du goodwill = bénéfice associé − 6 % × 5,00 : 0,10 ; 0,60 ; 1,20 ; 1,80 ; 2,30 M€ | 0,5 |
| 3.2-04 | Rentes actualisées à 12 % : 0,09 ; 0,48 ; 0,85 ; 1,14 ; 1,31 ; goodwill 3,87 M€ ; valeur patrimoniale = 5,60 + 3,87 = 9,47 M€ (par action : 18,94 €, non exigé) | 1 |
| 3.2-05 | Interprétation du goodwill et limites de l'approche pour une société en croissance (croissance après 2031 et immatériel non inscrit ignorés, rente sur cinq ans, valeurs estimées, valeur d'une entreprise qui continue) | 1,5 |

**Conventions rappelées** (annexes 3.2 et 3.6) : liste limitative des corrections ; impôt latent de 25 % sur chaque correction ; CPNE de 5,00 M€ et bénéfices associés fournis ; rémunération normale de 6 % ; actualisation de la rente à 12 % sur cinq ans ; 500 000 actions.

**ANC (0,5 pt).** ANC = total de l'actif − dettes = 5,20 − (0,80 + 0,90) = **3,50 M€**, égal aux capitaux propres comptables (7,20 − 3,75 + 0,05). Par action : 3,50 M€ / 500 000 = **7,00 €**. Les pertes accumulées pendant la création (3,75 M€) ont absorbé une grande partie des 7,20 M€ apportés par les actionnaires.

**ANCC (1 pt).**

| | M€ |
|---|---:|
| ANC | 3,50 |
| + Plateforme logicielle : 3,20 − 1,60 | + 1,60 |
| + Fichier des exploitations clientes (non inscrit) | + 1,20 |
| − Impôt latent : 25 % × (1,60 + 1,20) | − 0,70 |
| **= ANCC** | **5,60** |

Par action : 5,60 M€ / 500 000 = **11,20 €**. Les corrections portent sur les deux actifs qui font la valeur de la société et que le bilan sous-évalue : la plateforme, inscrite au coût de développement amorti, et le fichier de clients, créé par la société et donc absent du bilan. L'impôt latent traduit l'impôt qui serait dû si ces plus-values étaient réalisées.

**Rente du goodwill (0,5 pt).** La rente (ou superprofit) est le bénéfice qui dépasse la rémunération normale des capitaux nécessaires à l'exploitation : rente = bénéfice associé − 6 % × 5,00 = bénéfice associé − 0,30.

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Bénéfice associé (résultat net prévu) | 0,40 | 0,90 | 1,50 | 2,10 | 2,60 |
| − Rémunération normale des CPNE (6 % × 5,00) | − 0,30 | − 0,30 | − 0,30 | − 0,30 | − 0,30 |
| **= Rente du goodwill** | **0,10** | **0,60** | **1,20** | **1,80** | **2,30** |
| Coefficient 1,12^−t | 0,8929 | 0,7972 | 0,7118 | 0,6355 | 0,5674 |
| Rente actualisée | 0,09 | 0,48 | 0,85 | 1,14 | 1,31 |

**Goodwill et valeur patrimoniale (1 pt).**
- Goodwill = 0,09 + 0,48 + 0,85 + 1,14 + 1,31 = **3,87 M€**.
- Valeur patrimoniale = ANCC + goodwill = 5,60 + 3,87 = **9,47 M€**, soit **18,94 €** par action.

**Interprétation et limites pour une société en croissance (1,5 pt).**
- **Ce que mesure le goodwill** : la capacité d'ALTIMOISSON à rapporter plus que la rémunération normale de ses capitaux d'exploitation, grâce à des éléments qui ne figurent pas, ou mal, à l'actif : savoir-faire de l'équipe, modèles d'estimation des dommages, données accumulées, relations avec les assureurs, marque auprès des exploitants (guide, p. 66). Il représente 40,87 % de la valeur patrimoniale (3,87 / 9,47).
- **Ce que l'approche laisse de côté** :
  - **la croissance après 2031** : la rente est limitée à cinq ans, alors que la société a toutes les chances d'exister et de croître au-delà ; le plan fait passer le résultat de 0,40 à 2,60 M€, et la valeur créée ensuite est ignorée ;
  - **la montée progressive des bénéfices** : la rente de 2027 (0,10 M€) est presque nulle, et l'essentiel du goodwill vient des années les plus lointaines, donc les plus incertaines ;
  - **l'immatériel non retenu** : seuls deux actifs sont réévalués ; l'équipe, les données et les contrats avec les assureurs ne le sont pas ;
  - **les besoins de financement** : la rente se calcule sur des CPNE constants de 5,00 M€, alors que la société va investir (flux négatifs en 2027 et 2028) ; ce que coûte la croissance n'apparaît pas ;
  - **des valeurs estimées et une hypothèse de continuité** : le coût de reconstitution de la plateforme et la valeur du fichier n'ont de sens que si l'activité continue ; en cas d'échec, ils vaudraient beaucoup moins.
- **Conclusion** : l'ANCC (5,60 M€) est un **plancher** de négociation ; la valeur patrimoniale avec goodwill (9,47 M€) rapproche le patrimoine de la rentabilité, sans mesurer la croissance qui fait l'essentiel de la valeur d'une jeune société.

**Réponses tolérées** : ANC présenté comme capitaux propres comptables ; rentes actualisées non arrondies (goodwill 3,87 M€, valeur 9,47 M€) ; goodwill calculé en une seule expression ; mention du goodwill négatif possible (badwill) si la rente l'était, sans calcul.

**Erreurs fréquentes**
- Oublier l'impôt latent (ANCC de 6,30 M€) ou ne l'appliquer qu'à la plateforme (5,90 M€).
- Ajouter le goodwill à l'ANC au lieu de l'ANCC (7,37 M€).
- Actualiser la rente au taux de rémunération de 6 % (goodwill de 4,78 M€) ou additionner les rentes sans les actualiser (6,00 M€).
- Refaire, à partir du bilan, les bases du goodwill (capitaux permanents nécessaires à l'exploitation, bénéfices associés) au lieu d'utiliser les montants fournis de l'annexe 3.2.
- `JUR-E03` — présenter la valeur patrimoniale sans dire ce qu'elle ne mesure pas pour une société en croissance.
- `JUR-T07` — rentes présentées sans tableau.

---

### 3.3 CMPC, flux actualisés, valeur terminale, VGE et VCP (5,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Bêtas désendettés : 1,2000 ; 1,0000 ; 1,0800 ; 1,2000 ; moyenne 1,1200 | 0,5 |
| 3.3-02 | D/CP cible = 20 / 80 = 0,25 ; bêta réendetté = 1,1200 × 1,1875 = 1,3300 | 0,5 |
| 3.3-03 | ke = 4 % + 1,3300 × 5 % + 3 % = 13,65 % ; kd après impôt = 3,75 % ; CMPC = 80 % × 13,65 % + 20 % × 3,75 % = 11,67 % | 1 |
| 3.3-04 | Flux actualisés à 11,67 % : − 1,25 ; − 0,16 ; 0,57 ; 0,90 ; 1,04, soit 1,10 M€ | 1 |
| 3.3-05 | Valeur terminale 2031 = 1,80 × 1,02 / 0,0967 = 18,99 M€, actualisée 10,93 M€ | 0,5 |
| 3.3-06 | VGE = 1,10 + 10,93 = 12,03 M€ ; trésorerie nette = 2,10 − 0,80 = 1,30 M€ ; VCP = 12,03 + 1,30 = 13,33 M€ (par action : 26,66 €, non exigé), avant l'apport | 1 |
| 3.3-07 | Part de la valeur terminale : 90,86 % de la VGE ; commentaire (sensibilité au CMPC et à la croissance, plan établi par les dirigeants, risque d'échec non pris en compte par les flux d'un scénario de réussite) | 1 |

**Conventions rappelées** (annexes 3.3, 3.4 et 3.6) : formule de Hamada avec impôt ; moyenne arithmétique ; bêtas à quatre décimales ; ke arrondi dans le CMPC, CMPC arrondi pour l'actualisation ; flux de trésorerie disponibles fournis, à utiliser tels quels ; croissance de 2 % à l'infini ; VCP = VGE + trésorerie nette au 31/12/2026.

**Bêtas désendettés de l'échantillon (0,5 pt).** β désendetté = β des capitaux propres / [1 + (1 − 25 %) × D/CP] :

| Société | β des capitaux propres | D/CP | 1 + 0,75 × D/CP | β désendetté |
|---|---:|---:|---:|---:|
| ASSURELLO | 1,38 | 0,20 | 1,15 | 1,2000 |
| KLARVIK | 1,30 | 0,40 | 1,30 | 1,0000 |
| MEDORAN Courtage | 1,08 | 0,00 | 1,00 | 1,0800 |
| HOLTVEER | 1,74 | 0,60 | 1,45 | 1,2000 |
| **Moyenne** | | | | **1,1200** |

Le bêta désendetté mesure le risque économique du métier (distribution d'assurance en ligne et logiciels de sinistres), sans l'effet de la dette propre à chaque société. MEDORAN Courtage, sans dette, a un bêta désendetté égal à son bêta des capitaux propres.

**Bêta réendetté (0,5 pt).** D/CP cible = 20 % / 80 % = **0,25** ; β des capitaux propres = 1,1200 × (1 + 0,75 × 0,25) = 1,1200 × 1,1875 = **1,3300**.

**Coût des fonds propres et CMPC (1 pt).**
- ke = 4 % + 1,3300 × 5 % + 3 % = 4,00 % + 6,65 % + 3,00 % = **13,65 %** (MEDAF de Sharpe, 1964, majoré de la prime de taille et d'illiquidité).
- kd après impôt = 5 % × (1 − 25 %) = **3,75 %**.
- CMPC = 80 % × 13,65 % + 20 % × 3,75 % = 10,92 % + 0,75 % = **11,67 %**.

Le CMPC actualise les flux de trésorerie disponibles parce que ces flux reviennent à tous les apporteurs de capitaux, actionnaires et prêteurs (guide, p. 64). La prime de 3 % traduit la petite taille et l'illiquidité des titres d'ALTIMOISSON, que le bêta de sociétés cotées ne mesure pas.

**Flux actualisés (1 pt).**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| FTD (M€) | − 1,40 | − 0,20 | 0,80 | 1,40 | 1,80 |
| Coefficient 1,1167^−t | 0,8955 | 0,8019 | 0,7181 | 0,6431 | 0,5759 |
| FTD actualisé | − 1,25 | − 0,16 | 0,57 | 0,90 | 1,04 |

Somme des flux actualisés : **1,10 M€**. Les flux négatifs de 2027 et de 2028 effacent presque la valeur des trois années suivantes.

**Valeur terminale (0,5 pt).** Flux de 2032 = 1,80 × 1,02 = 1,836 M€ ; VT au 31/12/2031 = 1,836 / (11,67 % − 2 %) = 1,836 / 0,0967 = **18,99 M€** (Gordon et Shapiro) ; actualisée : 18,9866 × 1,1167^−5 = **10,93 M€**.

**VGE et VCP (1 pt).**
- VGE = 1,10 + 10,93 = **12,03 M€** : valeur de l'actif économique, qui revient à tous les apporteurs de capitaux.
- Trésorerie nette au 31/12/2026 = disponibilités − dettes financières = 2,10 − 0,80 = **1,30 M€** : ALTIMOISSON a plus de trésorerie que de dettes ; on l'ajoute donc à la VGE au lieu de retrancher une dette.
- VCP = 12,03 + 1,30 = **13,33 M€**, soit 26,66 € par action. C'est une valeur **avant l'apport** de la mutuelle : les 2,50 M€ apportés augmenteront la trésorerie et donc la VCP après l'opération, sans rien changer à la VGE, qui ne dépend que des flux d'exploitation.

**Part de la valeur terminale et commentaire (1 pt).**
- Part : 10,93 / 12,03 = **90,86 %** de la VGE (90,88 % sans arrondi, accepté) : plus de neuf dixièmes de la valeur viennent d'après 2031.
- **Sensibilité** (calculs facultatifs, sans arrondi intermédiaire) : VCP en M€ selon le CMPC et la croissance à l'infini.

| CMPC \ g | 1 % | 2 % | 3 % |
|---|---:|---:|---:|
| 10,67 % | 13,80 | 15,24 | 17,04 |
| 11,67 % | 12,21 | 13,33 | 14,71 |
| 12,67 % | 10,90 | 11,80 | 12,88 |

Un point de CMPC ou de croissance déplace la VCP de 1,1 à 1,9 M€, soit 8 % à 14 % de sa valeur.
- **Lecture pour une société en croissance** : c'est la situation typique d'une jeune société, dont les flux sont négatifs au début et dont la valeur dépend de sa réussite future. La valeur terminale suppose que le flux de 2031 est normatif, alors que la croissance prévue y est encore de 12,90 % et que la société investit ; elle dépend d'une prévision à cinq ans établie par les dirigeants, qui ont intérêt à présenter un plan favorable (asymétrie d'information, Akerlof, 1970).
- Les flux de l'annexe 3.3 correspondent à un **scénario de réussite**, et non à une espérance tenant compte du risque d'échec. Le CMPC, fondé sur le bêta de sociétés cotées et établies, ne rémunère pas ce risque : la VCP de 13,33 M€ est donc plutôt un **plafond**.

**Réponses tolérées** : coefficients d'actualisation arrondis à quatre décimales, avec des écarts de 0,01 M€ ; valeur terminale actualisée à partir de la valeur arrondie (10,94 M€, VGE de 12,04 M€ et VCP de 13,34 M€) ; part de la valeur terminale calculée sans arrondi intermédiaire (90,88 %).

**Erreurs fréquentes**
- Réendetter avec D/VGE (0,20) au lieu de D/CP (0,25) : bêta de 1,2880, ke de 13,44 %, CMPC de 11,50 % et VCP de 13,62 M€ (13,63 M€ sans arrondi intermédiaire).
- Faire la moyenne des bêtas des capitaux propres (1,3750) sans les désendetter, ou appliquer la formule sans impôt (bêta désendetté moyen de 1,0615, ke de 13,63 %) alors que l'annexe impose la formule avec impôt.
- Multiplier la prime de taille et d'illiquidité par le bêta, ou l'oublier (ke de 10,65 % et CMPC de 9,27 %).
- Actualiser les flux au coût des fonds propres de 13,65 % : VGE de 9,26 M€ et VCP de 10,56 M€.
- Oublier de multiplier le flux de 2031 par (1 + g) : VT de 18,61 M€ et VCP de 13,12 M€ ; actualiser la valeur terminale sur six ans (9,79 M€, VCP de 12,19 M€).
- Retrancher la trésorerie nette au lieu de l'ajouter (VCP de 10,73 M€), ou ajouter l'apport de 2,50 M€ à la VCP (15,83 M€) et confondre ainsi valeur avant et après l'opération.
- `JUR-E02` — coût du capital d'une société non cotée mal construit à partir de l'échantillon.
- `JUR-T07` — flux actualisés présentés sans tableau.

---

### 3.4 Méthode du capital-risque et comparaison des méthodes (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Valeur de sortie fin 2031 = 15 × 2,60 = 39,00 M€ ; valeur post-money = 39,00 / 1,30^5 = 39,00 / 3,71293 = 10,50 M€ | 0,5 |
| 3.4-02 | Valeur pré-money = 10,50 − 2,50 = 8,00 M€ ; prix par action = 8,00 M€ / 500 000 = 16,00 € ; actions nouvelles = 2 500 000 / 16,00 = 156 250 ; part de la mutuelle = 156 250 / 656 250 = 23,81 % | 1 |
| 3.4-03 | Comparaison : 8,00 M€ contre 5,60 (ANCC), 9,47 (valeur patrimoniale) et 13,33 M€ (flux) ; explication des écarts (TRI de 30 % contre CMPC de 11,67 %, risque d'échec, illiquidité, horizon de l'investisseur, croissance ignorée par l'approche patrimoniale) | 1 |

**Conventions rappelées** (annexes 3.5 et 3.6) : sortie le 31/12/2031, cinq ans après l'apport ; aucune émission ni dividende d'ici là ; valeurs post-money et pré-money arrondies à deux décimales, la pré-money arrondie servant au prix par action.

**Valeur de sortie et valeur post-money (0,5 pt).**
- Valeur de sortie des capitaux propres à la fin de 2031 = 15 × 2,60 = **39,00 M€**.
- La mutuelle exige un TRI de 30 % par an : la valeur aujourd'hui de la société **après** l'apport est la valeur de sortie actualisée à ce taux, soit 39,00 / 1,30^5 = 39,00 / 3,71293 = **10,50 M€** (valeur post-money).

**Valeur pré-money, prix et part du capital (1 pt).**
- Valeur pré-money = valeur post-money − apport = 10,50 − 2,50 = **8,00 M€** : c'est la valeur des capitaux propres **avant** l'apport, comparable à la VCP de la question 3.3.
- Prix par action = 8 000 000 / 500 000 = **16,00 €** ; actions nouvelles = 2 500 000 / 16,00 = **156 250** ; total après l'opération : 656 250 actions.
- Part de la mutuelle = 156 250 / 656 250 = **23,81 %** (= 2,50 / 10,50) : une participation minoritaire. Les fondateurs passeraient de 70 % à 53,33 % (350 000 / 656 250) et FERNIQUE Amorçage de 30 % à 22,86 %.
- Vérification : à la sortie, la mutuelle détiendrait 23,81 % de 39,00 M€, soit 9,29 M€, environ 3,7 fois sa mise (1,30^5 = 3,71) : le TRI de 30 % est obtenu si le plan se réalise.

**Comparaison avec les autres méthodes (1 pt).**

| Méthode | Valeur des capitaux propres avant l'apport (M€) | Par action (€) |
|---|---:|---:|
| ANCC | 5,60 | 11,20 |
| Méthode du capital-risque (pré-money) | 8,00 | 16,00 |
| Valeur patrimoniale (ANCC + goodwill) | 9,47 | 18,94 |
| Flux de trésorerie actualisés (VCP) | 13,33 | 26,66 |

- La valeur pré-money dépasse l'ANCC de 42,86 % (8,00 / 5,60 = 1,43) : l'investisseur paie une partie de la croissance, au-delà du patrimoine.
- Elle est **inférieure de 5,33 M€ à la valeur par les flux**, alors que les deux méthodes reposent sur le même plan. L'écart vient du taux : la mutuelle exige 30 % par an, contre un CMPC de 11,67 %. Ce TRI élevé rémunère ce que le CMPC ne prend pas en compte : le **risque d'échec** (le plan est un scénario de réussite ; dans un portefeuille de participations de ce type, une partie des lignes est perdue), l'**illiquidité** d'une participation minoritaire non cotée, et le temps que l'investisseur consacre à accompagner la société. Elle retient aussi un horizon court (cinq ans) et une valeur de sortie par un multiple, au lieu d'une croissance à l'infini.
- Entrer à la VCP par les flux (13,33 M€) donnerait à la mutuelle 15,79 % du capital pour 2,50 M€ et un TRI de 19,76 % seulement si le plan se réalise, loin de l'exigence de son conseil.
- Elle est **inférieure de 1,47 M€ à la valeur patrimoniale** : le goodwill est actualisé à 12 %, un taux bien plus faible que 30 %.
- Chaque méthode répond à une question différente : l'ANCC mesure ce que vaut le patrimoine ; la méthode des flux, ce que vaut le plan s'il réussit ; la méthode du capital-risque, le prix qu'un investisseur minoritaire peut payer pour obtenir la rentabilité qu'il exige.

**Réponses tolérées** : valeur post-money non arrondie (10,5038 M€), avec une pré-money de 8,0038 M€, un prix de 16,01 € et 156 152 actions nouvelles (23,80 % du capital), notée en cohérence ; part du capital calculée par 2,50 / 10,50 (23,81 %) sans le nombre d'actions ; comparaison présentée en valeurs par action.

**Erreurs fréquentes**
- Confondre post-money et pré-money : prix calculé sur 10,50 M€ (21,00 €), ou part de la mutuelle calculée sur la pré-money (2,50 / 8,00 = 31,25 %).
- Actualiser la valeur de sortie au CMPC (22,46 M€, pré-money de 19,96 M€) : le TRI exigé est le taux de la méthode.
- Appliquer un taux simple (39,00 / (1 + 5 × 30 %) = 15,60 M€) au lieu d'un taux composé.
- Comparer la valeur post-money (10,50 M€) à la VCP de la question 3.3, qui est une valeur avant l'apport.
- `JUR-E03` — juxtaposer les valeurs sans expliquer leurs écarts.

---

### 3.5 Fourchette, prix d'entrée et négociation (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Note à la directrice générale : fourchette de valeur **des capitaux propres** avant l'apport argumentée (la borne tirée des flux est la VCP de 13,33 M€, et non la VGE de 12,03 M€ ; par exemple de 5,60 M€, ANCC, à 8,00 M€, capital-risque, les flux donnant un plafond de 13,33 M€) ; prix d'entrée par action et part du capital qui en résulte (par exemple 12,50 €, pré-money de 6,25 M€, 200 000 actions nouvelles, 28,57 % du capital, fondateurs à 50,00 %) | 1 |
| 3.5-02 | Cycle de vie et synergies : valeur pré-money sans les agences de VERCÈNE (sortie 15 × 1,70 = 25,50 M€, post-money 6,87 M€, pré-money 4,37 M€) ; la mutuelle ne doit pas payer seule la valeur qu'elle apporte (3,63 M€) ; risques et conditions de l'entrée (information, gouvernance, contrôle des fondateurs, financement par étapes) | 1 |

**Synergies de distribution** (annexe 3.5). Sans les agences de VERCÈNE, le résultat net de 2031 serait de 1,70 M€ : valeur de sortie 15 × 1,70 = **25,50 M€** ; post-money 25,50 / 3,71293 = 6,87 M€ ; pré-money 6,87 − 2,50 = **4,37 M€** (8,74 € par action ; 36,39 % du capital pour 2,50 M€). La distribution dans les agences apporte donc **3,63 M€** à la valeur pré-money (8,00 − 4,37), près de la moitié.

**Exemple de note** (exemple développé ; une note de dix à quinze lignes reprenant ces éléments, avec le chiffrage de la valeur sans les agences, obtient la totalité des points)

> **À** : Mme Claire ESTAGNOL, directrice générale — **De** : cabinet — **Objet** : entrée au capital d'ALTIMOISSON SAS
>
> **1. Fourchette de valeur.** Avant votre apport, les capitaux propres d'ALTIMOISSON valent de 5,60 M€ (ANCC, plancher qui ne paie aucune croissance) à 8,00 M€ (méthode du capital-risque, au TRI de 30 % exigé par le conseil). La valeur par les flux (13,33 M€) et la valeur patrimoniale avec goodwill (9,47 M€) supposent la réussite du plan et un taux bien inférieur à votre exigence : ce sont des plafonds, que les fondateurs mettront en avant. Hormis l'ANCC, ces valeurs reposent sur le plan des dirigeants, qui suppose la vente de l'offre dans vos agences à partir de 2028.
>
> **2. Prix d'entrée proposé.** Je vous propose d'ouvrir la négociation à **12,50 € par action**, soit une valeur pré-money de 6,25 M€ : 200 000 actions nouvelles pour 2,50 M€, **28,57 %** du capital. Ce prix partage à peu près à parts égales la valeur apportée par vos agences ((4,37 + 8,00) / 2 = 6,185 M€). Il reste supérieur à l'ANCC et laisse aux fondateurs **50,00 %** du capital (350 000 / 700 000), le seuil qu'ils souhaitent conserver. Si le plan se réalise, la participation vaudrait 39,00 × 28,57 % = 11,14 M€ en 2031, soit un TRI de 34,83 %, qui offre une marge de sécurité face au risque d'échec. Le prix maximal acceptable est de 16,00 € (8,00 M€, 23,81 % du capital), au-delà duquel le TRI tombe sous 30 %.
>
> **3. Ce qu'impliquent le cycle de vie et les synergies.**
> - La société est en croissance : son résultat vient d'atteindre l'équilibre, ses flux restent négatifs jusqu'en 2028 et plus de 90 % de sa valeur par les flux viennent d'après 2031. Le prix doit donc rémunérer un risque élevé. Plutôt que de payer d'avance une croissance incertaine, un apport **en deux étapes** est préférable : une partie en 2027, le reste quand la distribution dans les agences aura donné ses premiers résultats.
> - La distribution par vos 64 agences apporte près de la moitié de la valeur pré-money (3,63 M€ sur 8,00). C'est la mutuelle qui apporte cette valeur : elle ne doit pas la payer une seconde fois dans le prix. C'est votre principal argument face à des fondateurs qui partiront de la valeur par les flux.
> - Les fondateurs connaissent mieux que vous la société et leur plan (asymétrie d'information, Akerlof, 1970). En tant qu'actionnaire minoritaire, vous devrez suivre la gestion (Jensen et Meckling, 1976) : un siège au conseil, une information régulière sur les indicateurs du plan (clients, sinistres gérés, part des ventes en agence) et l'accord de la mutuelle pour les décisions importantes. La dépendance envers trois assureurs et quelques personnes clés justifie aussi d'en faire des conditions de l'opération.
> - Enfin, la valeur de la participation n'est pas seulement financière : la plateforme peut améliorer le service rendu aux sociétaires agricoles et la gestion des sinistres climatiques de la mutuelle. Ce gain ne figure pas dans le TRI ; il peut justifier, à la marge, d'accepter un prix plus proche de 16,00 €.

**Réponses tolérées** : toute fourchette et tout prix cohérents avec les calculs du candidat et justifiés (par exemple une entrée à 16,00 €, pré-money de 8,00 M€, si le candidat considère que le TRI de 30 % rémunère déjà le risque, ou une fourchette de 8,00 à 13,33 M€ si les synergies sont laissées aux fondateurs pour préserver la relation) ; prix d'entrée exprimé par la seule valeur pré-money et la part du capital ; partage des synergies dans une autre proportion, s'il est expliqué.

**Erreurs fréquentes**
- Proposer comme prix d'entrée la valeur par les flux (13,33 M€) sans voir que le TRI obtenu (19,76 %) est inférieur à l'exigence du conseil.
- Proposer une fourchette qui mêle la valeur post-money et des valeurs avant l'apport.
- Retenir la VGE (12,03 M€) comme borne d'une fourchette de valeur des capitaux propres.
- Ignorer que les valeurs fondées sur le plan (goodwill, flux, capital-risque) incluent les synergies apportées par la mutuelle.
- Développer le régime juridique de l'augmentation de capital réservée ou de l'intermédiation en assurance : hors du champ de l'épreuve.
- `JUR-T01` — note sans posture de conseil (prix, part du capital, conditions) ; `JUR-T02` — recommandation sans lien avec les chiffres (4,37 ; 8,00 ; 13,33 M€).

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 64 ; programme l. 509-519 | flux de trésorerie disponibles, CMPC, MEDAF avec prime de taille, valeur terminale, passage de la VGE à la VCP | [V] | F03 § 2 ; F02 § 2, 3 et 5 |
| Guide pédagogique DSCG, juillet 2026, p. 65-66 ; programme l. 531-532 | ANC et ANCC, corrections indiquées par l'énoncé, rente du goodwill à partir des CPNE et des bénéfices associés fournis, limites | [V] | F03 § 4 et 5 |
| Guide pédagogique DSCG, juillet 2026, p. 67 ; programme l. 535-536 | cycle de vie et choix de la méthode ; méthode du capital-risque (valeur de sortie, TRI exigé, post-money, pré-money, part de l'investisseur) | [V] | F03 § 7 et 8 |
| Sujet 2025, annexe 1 (désendettement et réendettement du bêta d'un échantillon) | structure du calcul de la question 3.3 | [S] | F02 § 3 |
| Sharpe (1964) | MEDAF | [V contexte] | F10 § 2 |
| Gordon et Shapiro (1956) | valeur terminale à croissance constante | [V programme 3.1] | F10 § 2 |
| Akerlof (1970) | asymétrie d'information entre fondateurs et investisseur | [V programme 5.1] | F10 § 1 |
| Jensen et Meckling (1976) | théorie de l'agence (suivi de la gestion par l'actionnaire minoritaire) | [V programme 2.1] | F10 § 3 |
| Taux sans risque 4,0 %, prime de risque du marché 5,0 %, prime de taille et d'illiquidité 3,0 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 |
| Échantillon de sociétés cotées, corrections patrimoniales, CPNE, prévisions, multiple de sortie, TRI exigé | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 3.2 à 3.5 |
