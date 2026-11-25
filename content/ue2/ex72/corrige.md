# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 72 — Dossier 3 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F02 coût du capital, F05 ingénierie financière, F06 marchés et finance comportementale, F07 risques de taux et de change, F10 auteurs et théories, F11 données de marché, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (plan de financement de FERVANNE Associés ; tableaux d'amortissement de la dette senior et du crédit-vendeur ; service de la dette, couverture, trésorerie cumulée et années en défaut dans le plan de la banque et avec la distribution plafonnée ; fonds propres à l'horizon, multiple et TRI ; BPA du rachat suivi de l'annulation ; coûts actuariels avant et après IS ; bêta réendetté et rentabilité exigée ; cap dans trois scénarios, valeur intrinsèque et valeur temps ; barème, liste noire, hors-programme ; répartition du capital, dette nette pro forma, dividendes nécessaires, taux de distribution et valeur de sortie vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un service de la dette erroné à la question 3.2, repris dans les dividendes nécessaires et la couverture, ou des fonds propres investis erronés à la question 3.5, repris dans le rapport dettes / fonds propres et le bêta réendetté).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Voies de sortie de la famille : répartition du capital, rachat suivi de l'annulation, indépendance, contrôle, actionnariat salarié | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital | 2 |
| 3.2 Plan de financement de FERVANNE Associés, service de la dette, dividendes nécessaires, taux de distribution, couverture et trésorerie cumulée | `4.2.d` Décrypter les montages financiers avec et sans levier financier | 2,5 |
| 3.3 Effets et risques du montage, politique de dividende de FERVANNE Instruments | `4.2.d` Décrypter les montages financiers avec et sans levier financier ; `4.1.a` Déchiffrer la politique de dividende et les signaux associés | 2,5 |
| 3.4 Coûts actuariels de la dette senior et du crédit-vendeur, asymétrie d'information, financement hiérarchique et compromis | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `5.1.b` Maîtriser les enseignements des asymétries d'information (Akerlof, 1970) ; `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives | 3,5 |
| 3.5 TRI des fonds propres de FERVANNE Associés, bêta réendetté, rentabilité exigée, risque et levier, limites de la mesure | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier ; `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 3,5 |
| 3.6 Cap sur l'Euribor 3 mois, valeur intrinsèque et valeur temps, comparaison avec le swap | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux ; `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) | 3 |
| **Total** | | **17** |

Répartition par sous-partie : 4.2 ≈ 6 points (4.2.a ≈ 2, 4.2.d ≈ 4) ; 4.1 : 1 point (4.1.a) ; 7.2 ≈ 2,5 points (7.2.a ≈ 1, 7.2.d ≈ 1,5) ; 5.1 : 1 point (5.1.b) ; 5.2 ≈ 3,5 points (5.2.b ≈ 1 pour le TRI, 5.2.c ≈ 1,5 pour le bêta réendetté, le MEDAF et leurs limites, 5.2.a ≈ 1) ; 6.2 : 3 points (6.2.b ≈ 1,5, 6.2.c ≈ 1,5). Part du calcul : environ 8,5 points (3.1-01, 3.1-02, 3.2-01 à 3.2-04, 3.4-01, 3.4-02, 3.5-01 à 3.5-04, 3.6-01 à 3.6-03). Part de l'analyse : environ 8,5 points. La question 3.6 (3 points) se traite sans les résultats des questions précédentes : elle ne doit pas être sacrifiée faute de temps (`JUR-T15`).

---

### 3.1 Voies de sortie de la famille et stratégie de gestion du capital (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Répartition du capital : voie 2, 320 000 actions rachetées puis annulées, **1 280 000 actions** ; FERVANNE Associés **50 %**, FCPE **25 %**, famille **25 %** ; voie 3 : FERVANNE Associés **80 %** (1 280 000 actions), FCPE **20 %** ; voie 1 : 40 % / 20 % / 40 % au groupe concurrent, qui vise la majorité | 0,5 |
| 3.1-02 | Voie 2 : rachat 320 000 × 57,50 = **18,40 M€** ; dette nette pro forma 9,50 + 18,40 = 27,90 M€, soit **1,53** fois l'EBITDA 2026 (0,52 avant) ; BPA 2028 : 9,35 / 1,6 = **5,84 €** sans rachat ; (9,35 − 18,40 × 4,50 % × 0,75) / 1,28 = 8,729 / 1,28 = **6,82 €** après, soit une hausse d'environ 17 % | 0,5 |
| 3.1-03 | Indépendance et contrôle : la voie 1 fait entrer un industriel qui veut la majorité et transférer une partie de la fabrication (perte d'indépendance, risque pour l'usine de Vesoul et l'emploi) ; la voie 2 donne la moitié du capital aux cadres sans apport, mais pas la majorité, et laisse une famille minoritaire sans sortie organisée ; la voie 3 donne aux cadres le contrôle (80 %) et règle toute la sortie, au prix d'une dette portée par FERVANNE Associés | 0,5 |
| 3.1-04 | Actionnariat salarié et fonds d'épargne salariale : le FCPE passe à 25 % sans rien payer dans la voie 2, mais il supporte, comme tous les actionnaires, la dette de 18,40 M€ prise par la société ; il reste à 20 % dans la voie 3, minoritaire face à un actionnaire endetté dont la dette dépend des dividendes ; dans la voie 1, il devient le partenaire minoritaire d'un groupe qui peut décider d'une politique contraire à l'intérêt des salariés porteurs de parts ; conclusion argumentée (la voie 3 est la seule qui conserve l'indépendance et règle toute la sortie, sous réserve de la solidité du montage, question 3.2) | 0,5 |

**Répartition du capital (item 3.1-01).**

| Actionnaire | Avant | Voie 1 : groupe concurrent | Voie 2 : rachat puis annulation | Voie 3 : FERVANNE Associés |
|---|---:|---:|---:|---:|
| FERVANNE Associés | 640 000 (40 %) | 640 000 (40 %) | 640 000 / 1 280 000 = **50 %** | 1 280 000 / 1 600 000 = **80 %** |
| FCPE FERVANNE Actionnariat | 320 000 (20 %) | 320 000 (20 %) | 320 000 / 1 280 000 = **25 %** | 320 000 / 1 600 000 = **20 %** |
| Indivision OSMONDIER | 640 000 (40 %) | 0 | 320 000 / 1 280 000 = **25 %** | 0 |
| Groupe concurrent | 0 | 640 000 (40 %), majorité visée à trois ans | 0 | 0 |
| Nombre d'actions | 1 600 000 | 1 600 000 | **1 280 000** | 1 600 000 |

**Rachat suivi de l'annulation (item 3.1-02).** FERVANNE Instruments paie 320 000 × 57,50 € = **18,40 M€**, financés par emprunt : sa dette financière nette passerait de 9,50 M€ à **27,90 M€**, soit de 0,52 à **1,53** fois l'EBITDA de 2026. Le résultat de 2028 baisse des intérêts nets d'impôt, 18,40 × 4,50 % × (1 − 25 %) = 0,621 M€, et le nombre d'actions baisse d'un cinquième : le BPA passe de 9,35 / 1 600 000 = **5,84 €** à 8,729 / 1 280 000 = **6,82 €**. L'effet relutif vient de ce que le coût de la dette après impôt (3,375 %) est inférieur au rendement du résultat pour le prix payé (9,35 / 92,00 = 10,2 %) ; il ne crée pas de valeur par lui-même : il rémunère le risque supplémentaire que la dette fait porter aux actionnaires restants.

**Comparaison du point de vue de la gestion du capital (items 3.1-03 et 3.1-04).**
- *Indépendance.* La vente au groupe concurrent est la plus rémunératrice pour la famille (environ 5 % de plus, comptant), mais elle ouvre la voie à une prise de contrôle : le groupe veut la majorité dans trois ans, regrouper les achats d'acier et transférer une partie des ancillaires. Les deux autres voies gardent FERVANNE indépendante.
- *Contrôle par les cadres.* Le rachat suivi de l'annulation est une opération sur le nombre d'actions : en réduisant le capital, il porte mécaniquement les cadres à 50 % sans qu'ils déboursent rien, mais ne leur donne pas la majorité, et laisse la famille à 25 %, sans acheteur pour la suite : la sortie n'est que partielle. Le montage de FERVANNE Associés donne 80 % aux cadres.
- *Qui porte la dette.* Dans la voie 2, c'est FERVANNE Instruments qui s'endette : tous les actionnaires, FCPE compris, en supportent le risque, et l'entreprise consomme sa capacité d'emprunt (1,53 fois l'EBITDA au lieu de 0,52). Dans la voie 3, la dette est portée par FERVANNE Associés et remboursée par les dividendes de FERVANNE Instruments : l'entreprise n'emprunte pas, mais elle doit distribuer beaucoup plus (question 3.2).
- *Actionnariat salarié.* Le FCPE est relué dans la voie 2 (25 %) ; il reste à 20 % dans la voie 3 ; dans la voie 1, les 430 salariés porteurs de parts deviennent les associés minoritaires d'un concurrent. Dans les trois cas, leur épargne reste concentrée sur une seule société non cotée.

La voie 3 est la seule qui règle toute la sortie de la famille et garde l'entreprise indépendante, sous la direction de ses cadres ; elle n'est acceptable que si le montage est solide (question 3.2). La voie 2 peut servir de complément (rachat d'une partie du bloc) pour réduire la dette du montage, si la famille accepte une sortie en deux temps.

**Réponses tolérées** : BPA calculé sur le résultat net de 2026 (8,00 M€ : 5,00 € puis 5,76 €), si le candidat signale qu'il comprend une perte de change non récurrente ; dette nette pro forma rapportée aux capitaux propres consolidés (68,00 M€) plutôt qu'à l'EBITDA ; voie 2 analysée avec un rachat des 640 000 actions (deux tiers / un tiers, 36,80 M€ de dette, 2,54 fois l'EBITDA) si le candidat le présente comme une variante.

**Erreurs fréquentes**
- Calculer les parts après le rachat sur 1 600 000 actions : les actions annulées disparaissent du capital.
- Présenter la hausse du BPA comme une création de valeur, sans le risque de la dette (`JUR-T14`).
- Développer les règles du rachat de ses propres actions par une société par actions simplifiée ou de l'épargne salariale : les conditions sont des faits d'énoncé.
- Comparer les voies par le seul prix offert, sans le contrôle, l'indépendance ni les salariés (`JUR-T13`).

**Références** : F05 § 3 (rachat d'actions, annulation, BPA) [V guide p. 68-69 ; S] ; programme 4.2.a, guide p. 68-69 (gestion du capital comme levier stratégique, opérations sur le nombre d'actions, indicateurs simples) [V] ; F05 § 1.1 (holding de reprise) [V guide p. 70].

---

### 3.2 Plan de financement, service de la dette, dividendes nécessaires et couverture (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Plan de financement : emplois 36,80 + 0,46 + 0,24 = **37,50 M€** ; ressources : apports **5,50 (14,67 %)**, dette senior **24,00 (64,00 %)**, crédit-vendeur **8,00 (21,33 %)** | 0,5 |
| 3.2-02 | Service de la dette : senior 6,00 ; 5,76 ; 5,52 ; 5,28 ; 5,04 (intérêts 1,20 à 0,24, amortissement 4,80) ; intérêts du crédit-vendeur 0,48 par an ; **service total 6,48 ; 6,24 ; 6,00 ; 5,76 ; 5,52 M€** | 0,5 |
| 3.2-03 | Besoin 6,56 ; 6,32 ; 6,08 ; 5,84 ; 5,60 ; dividendes que FERVANNE Instruments doit verser (besoin / 80 %) : **8,20 ; 7,90 ; 7,60 ; 7,30 ; 7,00 M€** ; taux de distribution nécessaire **87,70 % ; 81,03 % ; 74,88 % ; 69,19 % ; 63,93 %** (40 % en 2026) | 0,5 |
| 3.2-04 | Distribution plafonnée à 80 % : dividendes reçus 5,984 ; 6,240 ; 6,496 ; 6,752 ; 7,008 ; flux nets des charges 5,904 à 6,928 ; couverture **0,91 ; 0,99 ; 1,07 ; 1,16 ; 1,26** ; trésorerie cumulée **− 0,576 ; − 0,656 ; − 0,240 ; + 0,672 ; + 2,080 M€** | 0,5 |
| 3.2-05 | Conclusion : montage tendu ; avec le plafond de 80 %, FERVANNE Associés ne paie pas ses échéances de 2028 et 2029 (manque cumulé de 0,656 M€) et ne retrouve une trésorerie positive qu'en 2031 ; le plan de la banque exige 87,70 % du résultat en 2028, au-delà de l'engagement de la présidente ; aucune marge pour un choc ; ajustements possibles (différé ou allongement de la dette senior, crédit-vendeur plus élevé, prix plus bas, apport complémentaire) | 0,5 |

**Plan de financement de FERVANNE Associés au 31 décembre 2027 (item 3.2-01).**

| Emplois | M€ | Ressources | M€ | Part |
|---|---:|---|---:|---:|
| 640 000 actions × 57,50 € | 36,80 | Apports nouveaux des 52 cadres | 5,50 | 14,67 % |
| Frais d'acquisition | 0,46 | Dette senior (Banque HAUTMERLE) | 24,00 | 64,00 % |
| Frais de dossier (1 % × 24,00) | 0,24 | Crédit-vendeur (indivision OSMONDIER) | 8,00 | 21,33 % |
| **Total** | **37,50** | **Total** | **37,50** | 100 % |

Après l'opération, FERVANNE Associés détient 640 000 + 640 000 = 1 280 000 actions, soit **80 %** du capital ; le FCPE garde 320 000 actions, soit **20 %**.

**Service de la dette (item 3.2-02).** Taux du plan : 2,65 % + 2,35 % = 5,00 % ; amortissement constant de 24,00 / 5 = 4,80 M€ ; crédit-vendeur : 8,00 × 6 % = 0,48 M€ d'intérêts par an, capital remboursé à l'horizon.

| M€ | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|
| Capital senior dû au début | 24,00 | 19,20 | 14,40 | 9,60 | 4,80 |
| Intérêts senior (5,00 %) | 1,20 | 0,96 | 0,72 | 0,48 | 0,24 |
| Amortissement senior | 4,80 | 4,80 | 4,80 | 4,80 | 4,80 |
| Intérêts du crédit-vendeur | 0,48 | 0,48 | 0,48 | 0,48 | 0,48 |
| **Service de la dette** | **6,48** | **6,24** | **6,00** | **5,76** | **5,52** |
| Charges propres | 0,08 | 0,08 | 0,08 | 0,08 | 0,08 |
| **Besoin de FERVANNE Associés** | **6,56** | **6,32** | **6,08** | **5,84** | **5,60** |

**Dividendes nécessaires et taux de distribution (item 3.2-03).** FERVANNE Associés ne reçoit que 80 % des dividendes : pour lui faire parvenir 1 €, FERVANNE Instruments doit distribuer 1,25 €, dont 0,25 € au FCPE.

| M€ | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|
| Dividendes totaux nécessaires (besoin / 0,80) | **8,20** | **7,90** | **7,60** | **7,30** | **7,00** |
| dont FCPE (20 %) | 1,64 | 1,58 | 1,52 | 1,46 | 1,40 |
| Résultat distribuable | 9,35 | 9,75 | 10,15 | 10,55 | 10,95 |
| **Taux de distribution nécessaire** | **87,70 %** | **81,03 %** | **74,88 %** | **69,19 %** | **63,93 %** |

En 2026, FERVANNE a distribué 3,20 M€ : le dividende de 2,00 € versé en 2026 représente environ 40 % du BPA de 2026 (5,00 €), lui-même diminué par une perte de change : c'est un ordre de grandeur. Le montage impose de distribuer, en 2028, plus de 5 € par action.

**Distribution plafonnée à 80 % (item 3.2-04).**

| M€ | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|
| Dividendes totaux (80 % du résultat) | 7,48 | 7,80 | 8,12 | 8,44 | 8,76 |
| Reçus par FERVANNE Associés (80 %) | 5,984 | 6,240 | 6,496 | 6,752 | 7,008 |
| − charges propres = flux disponible | 5,904 | 6,160 | 6,416 | 6,672 | 6,928 |
| Service de la dette | 6,48 | 6,24 | 6,00 | 5,76 | 5,52 |
| Écart de l'année | − 0,576 | − 0,080 | + 0,416 | + 0,912 | + 1,408 |
| **Couverture** | **0,91** | **0,99** | **1,07** | **1,16** | **1,26** |
| **Trésorerie cumulée** | **− 0,576** | **− 0,656** | **− 0,240** | **+ 0,672** | **+ 2,080** |

**Conclusion (item 3.2-05).** La condition de réussite d'un montage à levier (dividendes reçus au moins égaux au service de la dette, chaque année) n'est pas remplie en 2028 et 2029 avec la distribution plafonnée : il manque 0,576 M€ puis 0,080 M€, que FERVANNE Associés devrait emprunter à court terme ou demander aux cadres, alors que la banque interdit toute distribution aux cadres avant 2033 et que ceux-ci disent ne pas pouvoir apporter davantage. Le plan de la banque, lui, n'équilibre les échéances qu'en supposant une distribution de 87,70 % du résultat de 2028, contraire à l'engagement pris devant le FCPE. La couverture ne dépasse 1,10 qu'en 2031 : le moindre écart sur les résultats (une perte de change comme celle de 2026, une baisse de prix des grands clients, une hausse du prix de l'acier) ou sur le taux de la dette senior (question 3.6) rend le montage déficitaire plus longtemps. Le montage est faisable mais fragile ; il gagnerait à être ajusté : différé d'un an ou allongement à six ou sept ans de l'amortissement de la dette senior, part plus grande du crédit-vendeur (dont le capital n'est dû qu'en 2032), prix plus bas, ou rachat préalable d'une partie du bloc par FERVANNE Instruments (voie 2).

**Réponses tolérées** : couverture calculée sur les dividendes reçus avant charges (0,92 ; 1,00 ; 1,08 ; 1,17 ; 1,27) ou sur le besoin (dividendes reçus / besoin), si la définition est écrite ; trésorerie cumulée arrondie à deux décimales ; dividendes nécessaires exprimés aussi par action ; charges propres ajoutées au service plutôt que déduites des flux (même conclusion).

**Erreurs fréquentes**
- Calculer les dividendes nécessaires sans tenir compte des 20 % du FCPE (6,56 au lieu de 8,20 M€) : c'est l'erreur centrale du dossier.
- Inclure dans le service de 2032 le capital du crédit-vendeur (8,00 M€), remboursé à l'horizon (question 3.5).
- Calculer des annuités constantes pour une dette à amortissement constant, ou appliquer le taux trimestriel du cap au plan (`JUR-I01`).
- Constater le déficit de 2028 sans conclure sur la condition de réussite du montage ni proposer d'ajustement (`JUR-I02`).

**Références** : F05 § 1.2 (calculs attendus d'un montage : bilan de la holding, tableaux d'amortissement, dividendes remontés, condition de réussite) [V guide p. 70 ; S] ; F01 § 3 (amortissement constant) [S] ; programme 4.2.d [V].

---

### 3.3 Effets et risques du montage, politique de dividende (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Effet de levier financier : FERVANNE Associés détient 1 280 000 actions, soit 73,60 M€ au prix de travail, avec 32,00 M€ de dettes pour 5,50 M€ d'argent nouveau (42,30 M€ de fonds propres en valeur en comptant la participation existante, dettes / fonds propres 0,76 ; le seul rapport dettes / apports nouveaux est accepté) ; la dette amplifie la rentabilité des fonds propres si le rendement des actions acquises dépasse le coût de la dette, et amplifie aussi les pertes | 0,5 |
| 3.3-02 | Contrôle avec une mise limitée et dépendance aux dividendes : 5,50 M€ d'apports nouveaux font passer les cadres de 40 % à 80 % du capital (14,67 % du financement du rachat) ; FERVANNE Associés n'a pas d'autre ressource que les dividendes de FERVANNE Instruments, décidés par les cadres eux-mêmes, et doit en faire verser 1,25 € pour en recevoir 1 € | 0,5 |
| 3.3-03 | Risques : pour l'entreprise, prélèvement de 38,00 M€ de dividendes en cinq ans (16,00 M€ au rythme de 2026), moindre capacité à investir (6 M€ par an) et à absorber un choc ; pour les cadres, concentration de leur emploi et de leur épargne sur la même société ; pour les 430 salariés porteurs de parts, minorité face à un actionnaire endetté qui décide de la distribution ; conflit d'intérêts de la présidente des deux sociétés (Jensen et Meckling) | 0,5 |
| 3.3-04 | Politique de dividende : le taux de distribution passe d'environ 40 % à 64-88 % ; le dividende n'est plus un arbitrage entre distribution et réinvestissement mais une contrainte fixée par la dette de FERVANNE Associés ; il baisse ensuite avec le service (profil décroissant), à rebours de la progression régulière de 2024-2026 (1,80 ; 1,90 ; 2,00 €) | 0,5 |
| 3.3-05 | Signal et théories : effet cliquet (Lintner) et lecture d'une baisse future du dividende par les porteurs de parts ; signal (Spence, Ross) brouillé, puisque le dividende reflète le besoin de l'actionnaire principal et non les perspectives ; neutralité (Modigliani et Miller, 1961) en marchés parfaits, mais frictions ici (dette de FERVANNE Associés, actions non cotées, coûts d'agence) ; le plafond de 80 % protège l'investissement et les minoritaires | 0,5 |

**Les trois effets du montage (items 3.3-01 et 3.3-02).**
- *Levier financier.* FERVANNE Associés détient après l'opération 1 280 000 actions, soit 73,60 M€ au prix de travail, avec des fonds propres en valeur de 36,80 + 5,50 = 42,30 M€ et 32,00 M€ de dettes. Tant que le rendement des actions de FERVANNE (dividendes et hausse de valeur) dépasse le coût de la dette (5,38 % pour la dette senior, 6,00 % pour le crédit-vendeur, question 3.4), l'écart revient aux cadres et la rentabilité de leurs fonds propres augmente (TRI de 15,10 %, question 3.5). Le levier joue dans les deux sens : une baisse des résultats ou du multiple de sortie se reporte, amplifiée, sur les fonds propres.
- *Contrôle avec une mise limitée.* Avec 5,50 M€ d'argent nouveau, soit 14,67 % du financement du rachat, les cadres doublent leur participation et obtiennent 80 % du capital : la dette senior et le crédit-vendeur financent 85,33 % du rachat. C'est l'effet de la holding : une société détenue par les cadres contrôle FERVANNE Instruments sans que chaque cadre détienne directement ses actions.
- *Dépendance aux dividendes.* FERVANNE Associés n'a ni activité ni trésorerie : elle ne peut payer ses échéances qu'avec les dividendes de FERVANNE Instruments. Comme le FCPE reçoit 20 % de toute distribution, chaque euro remonté coûte 1,25 € de trésorerie à l'entreprise.

**Risques (item 3.3-03).**
- *Pour l'entreprise.* Elle verserait 38,00 M€ de dividendes de 2028 à 2032 dans le plan de la banque, contre 16,00 M€ au rythme de 2026 : autant de trésorerie qui ne finance ni les investissements (6 M€ par an), ni les stocks, ni une éventuelle acquisition. Elle devient moins capable d'absorber un choc (perte de change sur les francs suisses, baisse de prix demandée par les grands clients) et de saisir une occasion. Un défaut de FERVANNE Associés mettrait en jeu le contrôle de l'entreprise, et l'indépendance que le montage devait préserver serait perdue.
- *Pour les cadres.* Leur emploi, leur rémunération et une grande partie de leur patrimoine (42,30 M€ en valeur) dépendent de la même entreprise : un risque spécifique qu'ils ne peuvent pas diversifier.
- *Pour les salariés porteurs de parts du FCPE.* Ils perçoivent davantage de dividendes à court terme (1,64 M€ en 2028 contre 0,64 M€ en 2026), mais leur épargne dépend d'une société dont l'actionnaire principal, endetté, décide de la distribution : c'est un conflit d'agence (Jensen et Meckling, 1976) entre la dirigeante, présidente de l'actionnaire majoritaire, et les actionnaires minoritaires, renforcé par la double présidence de Mme PRÉVERANGE. Le plafond de 80 % et l'engagement sur les investissements en sont la réponse.

**Effet sur la politique de dividende (items 3.3-04 et 3.3-05).** FERVANNE distribuait environ 40 % de son résultat et augmentait régulièrement son dividende (1,80 €, 1,90 €, 2,00 €), politique de lissage typique d'une entreprise familiale. Le montage la remplace par une distribution dictée par la dette de FERVANNE Associés : 87,70 % en 2028, puis un taux décroissant à mesure que la dette senior s'amortit. L'arbitrage entre distribution et réinvestissement disparaît pendant cinq ans. Le dividende perd sa fonction de signal (Spence, 1973 ; Ross, 1977, pour le signal par l'endettement) : il ne dit plus rien des perspectives, puisqu'il reflète le besoin de l'actionnaire principal. En marchés parfaits, la politique de dividende serait neutre (Modigliani et Miller, 1961) ; ici, les frictions dominent : FERVANNE Associés ne peut pas vendre d'actions pour se créer un dividende, les actions ne sont pas cotées, et chaque euro distribué sort de l'entreprise. Après 2032, la distribution pourra revenir vers un taux plus bas : l'effet cliquet (Lintner, 1956) rend une baisse du dividende difficile à faire accepter aux porteurs de parts, d'où l'intérêt d'annoncer dès 2027 que le taux élevé est temporaire et lié au rachat.

**Réponses tolérées** : effet de levier illustré par le TRI de la question 3.5 ou par un raisonnement littéral (rentabilité des fonds propres = rentabilité de l'actif + (rentabilité de l'actif − coût de la dette) × dettes / fonds propres) ; mention de la théorie du flux de trésorerie disponible (la dette discipline les dirigeants en les obligeant à distribuer) comme effet positif du montage ; risque de garantie des actions évoqué sans le détailler.

**Erreurs fréquentes**
- Confondre l'effet de levier financier et l'effet de contrôle (holding) : le premier porte sur la rentabilité, le second sur le pouvoir.
- Analyser le montage du seul point de vue des cadres, sans l'entreprise ni les salariés du FCPE (`JUR-T13`).
- Citer la neutralité de Modigliani et Miller sans dire pourquoi elle ne s'applique pas ici (`JUR-I04`, `JUR-T14`).
- Décrire des clauses de garantie ou de contrat de prêt : elles ne sont pas demandées.

**Références** : F05 § 1.3 (effet de levier, risques) et § 2.1 (théories de la politique de dividende) [V guide p. 67-68, p. 70 ; S] ; F10 (Jensen et Meckling, 1976 ; Spence, 1973 ; Ross, 1977 ; Modigliani et Miller, 1961 ; Lintner, 1956 [S]) ; programme 4.1.a et 4.2.d [V].

---

### 3.4 Coûts actuariels, asymétrie d'information et théories du financement (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Dette senior avant IS : flux + 23,76 ; − 6,00 ; − 5,76 ; − 5,52 ; − 5,28 ; − 5,04 ; coût actuariel **5,38 %** (taux nominal 5,00 % + effet des frais) | 0,5 |
| 3.4-02 | Dette senior après IS : + 23,82 ; − 5,70 ; − 5,52 ; − 5,34 ; − 5,16 ; − 4,98 ; coût **4,02 %** (approximation 4,03 % ou 4,04 % admise) ; crédit-vendeur : **6,00 %** avant IS, **4,50 %** après IS ; le crédit-vendeur coûte plus, mais il est subordonné, in fine, sans frais | 0,5 |
| 3.4-03 | Asymétrie d'information (Akerlof, 1970) : les cadres acheteurs, qui dirigent l'entreprise et ont établi les prévisions, en savent plus que la famille vendeuse ; la famille craint de vendre trop bas (sélection adverse : les acheteurs informés n'achètent que si le prix est inférieur à ce qu'ils savent) ; elle exige une prime ou se tourne vers l'acheteur qui paie le plus (le groupe concurrent) ; la vente aux mieux informés peut échouer | 0,5 |
| 3.4-04 | Réponse du crédit-vendeur : 8,00 M€ du prix (21,74 %) ne sont payés que si les résultats futurs le permettent, après la dette senior : la famille partage le risque des prévisions qu'elle ne peut pas vérifier et obtient en contrepartie une information régulière ; les cadres, qui acceptent cette créance et apportent 5,50 M€ personnels, envoient un signal coûteux ; la banque y voit une protection ; limite : à taux fixe, la famille supporte le risque de baisse sans profiter d'une hausse (un complément de prix lié aux résultats la ferait participer) | 0,5 |
| 3.4-05 | Financement hiérarchique (Myers et Majluf, 1984) : FERVANNE Associés n'a pas de ressources internes ; après l'apport des cadres, la dette bancaire puis le crédit-vendeur sont préférés à des fonds propres extérieurs (un fonds), les plus coûteux en présence d'asymétrie d'information et qui dilueraient le contrôle | 0,5 |
| 3.4-06 | Théorie du compromis (Myers, 1977) : économie d'impôt sur les intérêts (coût après IS) contre coûts de détresse financière ; ici couverture inférieure à 1 en 2028 et 2029, une seule source de revenus : le montage est proche de la limite où le coût de la détresse l'emporte | 0,5 |
| 3.4-07 | Réponse argumentée à la question « faut-il modifier la composition du financement ? » : garder le crédit-vendeur, qui coûte moins que les fonds propres (4,50 % après IS contre 14,35 %) et n'exige aucun capital avant 2032 ; réduire ou étaler la dette senior ; ne pas faire entrer de fonds | 0,5 |

**Coût actuariel de la dette senior (items 3.4-01 et 3.4-02, 1 pt avec le crédit-vendeur).** Montant reçu à la date 0 : 24,00 − 0,24 = 23,76 M€ ; décaissements annuels = amortissement de 4,80 + intérêts à 5,00 % (taux supposé constant).

| Année | 0 | 1 (2028) | 2 | 3 | 4 | 5 (2032) |
|---|---:|---:|---:|---:|---:|---:|
| Flux avant IS | + 23,76 | − 6,00 | − 5,76 | − 5,52 | − 5,28 | − 5,04 |
| Économie d'IS (25 % des frais et des intérêts) | + 0,06 | + 0,30 | + 0,24 | + 0,18 | + 0,12 | + 0,06 |
| Flux après IS | + 23,82 | − 5,70 | − 5,52 | − 5,34 | − 5,16 | − 4,98 |

Avant IS, la valeur actuelle nette des flux vaut − 0,11 à 5,2 % et + 0,02 à 5,4 % ; par interpolation, **t = 5,38 %**. Les frais de 1 %, payés d'emblée sur un prêt dont la durée moyenne est courte (un cinquième remboursé chaque année), ajoutent 0,38 point au taux de 5,00 %. Après IS : − 0,02 à 4,0 % et + 0,05 à 4,1 %, **t' = 4,02 %** ; l'approximation 5,38 % × 0,75 = 4,04 % (4,03 % avec le taux non arrondi) est admise si elle est annoncée. Ce coût suppose un taux de référence constant : il est variable (question 3.6).

**Coût du crédit-vendeur.** Sans frais et remboursé in fine, son coût actuariel est égal à son taux : **6,00 %** avant IS, 6,00 % × 0,75 = **4,50 %** après IS (flux + 8,00 ; − 0,36 de 2028 à 2031 ; − 8,36 en 2032).

Le crédit-vendeur coûte 0,62 point de plus que la dette senior avant IS (0,48 après IS), parce que la famille est remboursée après la banque. Mais il ne demande aucun remboursement de capital avant 2032, n'entraîne aucun frais et vient compléter le financement là où la banque refuse d'aller : sans lui, le prix de travail ne pourrait pas être payé. Pour la banque, c'est presque un apport de fonds propres.

**Asymétrie d'information (item 3.4-03).** Akerlof (1970) montre que lorsque le vendeur d'un bien en connaît mieux la qualité que l'acheteur, l'acheteur ne paie qu'un prix moyen, les meilleurs biens se retirent et le marché peut disparaître : c'est la sélection adverse, qui joue avant le contrat. Ici l'asymétrie est inversée : ce sont les acheteurs, les cadres, qui connaissent le mieux FERVANNE ; ils ont eux-mêmes établi les prévisions de 2028 à 2032, retenues par la banque, alors que la famille ne connaît l'entreprise que par les comptes annuels et les assemblées. La famille ne peut pas savoir si le prix proposé reflète ce que savent les cadres ; elle peut craindre que ceux-ci n'achètent que parce qu'ils savent le prix inférieur à la valeur. Elle réagit comme l'acheteur d'Akerlof : elle exige une prime, ou elle préfère l'acheteur extérieur qui paie davantage comptant (le groupe concurrent, environ 5 % de plus), même si ce n'est pas l'acheteur qui valorise le mieux l'entreprise. La banque, elle aussi moins informée que les cadres, limite son prêt à 24,00 M€.

**Réponse apportée par le crédit-vendeur (item 3.4-04).**
- 8,00 M€, soit 21,74 % du prix de 36,80 M€, ne sont payés que si FERVANNE réalise les résultats annoncés : la famille devient créancière des résultats futurs et partage le risque des prévisions qu'elle ne peut pas vérifier. En contrepartie, elle obtient une information régulière (comptes semestriels, plan de remboursement, présence aux présentations des comptes), qui réduit l'asymétrie pendant toute la durée du crédit.
- Les cadres acceptent une dette dont le remboursement dépend de leurs propres prévisions, et engagent 5,50 M€ personnels : c'est un signal coûteux, au sens de Spence (1973) et de Ross (1977), qu'un acheteur qui aurait embelli ses prévisions hésiterait à donner. Il rend le prix de travail plus crédible pour la famille.
- Pour la banque, une famille qui accepte d'être remboursée après elle montre qu'elle ne cherche pas à se défaire au plus vite d'une entreprise en difficulté ; le crédit-vendeur et les apports forment une protection sous la dette senior.
- Limite : à taux fixe, le crédit-vendeur fait supporter à la famille le risque d'une baisse des résultats, sans la faire profiter d'une performance meilleure que prévu. Si la famille craint surtout que les cadres sous-estiment l'avenir, un complément de prix fonction des résultats de 2028 à 2032 répondrait mieux à sa crainte.

**Théories du financement (items 3.4-05 à 3.4-07).**
- *Financement hiérarchique (Myers et Majluf, 1984).* En présence d'asymétrie d'information, une société préfère l'autofinancement, puis la dette, et n'émet des actions qu'en dernier recours, parce que les apporteurs extérieurs de fonds propres exigent une décote pour se protéger de ce qu'ils ne savent pas. FERVANNE Associés n'a pas de ressources internes ; ses associés apportent ce qu'ils peuvent (5,50 M€), puis elle emprunte auprès de la banque et du vendeur. Faire entrer un fonds d'investissement, apporteur extérieur et moins informé, coûterait le plus cher (rentabilité exigée élevée, droits de regard) et diluerait le contrôle que les cadres cherchent à obtenir. La composition du financement suit cet ordre.
- *Théorie du compromis (Myers, 1977).* La dette procure une économie d'impôt (coût de la dette senior ramené de 5,38 % à 4,02 % dans l'hypothèse de l'annexe 3.6) mais expose à des coûts de détresse financière. Ici, FERVANNE Associés n'a qu'une source de revenus, la couverture est inférieure à 1 en 2028 et 2029, et un défaut ferait perdre le contrôle de l'entreprise, déstabiliserait les clients et les salariés : le montage est proche du point où le coût attendu de la détresse dépasse l'avantage fiscal. Le niveau de dette senior (64 % du financement) est le point faible.
- *Recommandation.* Garder le crédit-vendeur, et même l'augmenter si la famille l'accepte : il coûte 4,50 % après IS, bien moins que la rentabilité exigée des fonds propres des cadres (14,35 %, question 3.5), et son capital n'est dû qu'en 2032. Réduire le service de la dette senior des premières années (différé, allongement) plutôt que d'ouvrir le capital à un fonds.

**Réponses tolérées** : coûts actuariels à ± 0,02 point (interpolation) ; approximation par le coût avant IS × 0,75 si elle est signalée ; frais déduits de l'impôt de l'année 1 si l'hypothèse est écrite ; remarque selon laquelle l'économie d'impôt suppose que FERVANNE Associés ait un résultat imposable (sinon coût après IS = coût avant IS), si l'hypothèse de l'annexe 3.6 est ensuite appliquée (la remarque nourrit aussi l'item 3.4-06) ; analyse de l'asymétrie du point de vue de la banque prêteuse plutôt que de la famille, si le crédit-vendeur y est relié ; mention de l'aléa moral (comportement des cadres après la cession), si elle est distinguée de la sélection adverse ; lecture du crédit-vendeur comme signal de la famille envers la banque.

**Erreurs fréquentes**
- Oublier les frais de dossier, ou les déduire du montant prêté sans les rattacher à la date 0 (`JUR-T04`).
- Présenter l'asymétrie d'information comme une asymétrie au détriment des acheteurs, comme dans le marché des voitures d'occasion, sans voir qu'ici ce sont les acheteurs qui sont informés.
- Confondre sélection adverse (avant le contrat) et aléa moral (après le contrat).
- Attribuer le financement hiérarchique à Modigliani et Miller, ou inverser l'ordre dette / actions (`JUR-T14`).

**Références** : F01 § 2 et § 3 (actualisation, tableaux d'amortissement) [S] ; programme 7.2.a, guide p. 81-82 (coût actuariel, frais, coût net d'IS) [V] ; F06 § 2 et F10 (Akerlof, 1970 ; Spence, 1973 ; Ross, 1977 ; Myers et Majluf, 1984 ; Myers, 1977, attribution du programme 7.2) [V programme 5.1 et 7.2] ; programme 5.1.b, guide p. 73 (sélection adverse, conséquences sur le coût du financement) [V].

---

### 3.5 TRI des fonds propres de FERVANNE Associés et rentabilité exigée (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Fonds propres investis en valeur : 640 000 × 57,50 + 5,50 = 36,80 + 5,50 = **42,30 M€** ; valeur d'une action en 2032 : (5,5 × 22,00 − 4,20) / 1,6 = 116,80 / 1,6 = **73,00 €** ; 1 280 000 actions : **93,44 M€** ; fonds propres à l'horizon : 93,44 + 0 − 8,00 = **85,44 M€** | 0,5 |
| 3.5-02 | Multiple de la mise 85,44 / 42,30 = **2,02** ; TRI = (85,44 / 42,30)^(1/5) − 1 = **15,10 %** | 0,5 |
| 3.5-03 | Dettes / fonds propres = 32,00 / 42,30 = **0,7565** ; bêta réendetté = 1,00 × (1 + 0,75 × 0,7565) = **1,57** | 0,5 |
| 3.5-04 | Rentabilité exigée = 4,0 % + 1,57 × 5,0 % + 2,5 % = **14,35 %** (11,50 % sans dette de montage) | 0,5 |
| 3.5-05 | Comparaison : TRI supérieur de 0,75 point à la rentabilité exigée : le montage crée de la valeur pour les cadres dans le plan de la banque, avec une marge étroite ; un multiple de sortie de 5,0 au lieu de 5,5 ramène le TRI à 12,62 %, sous la rentabilité exigée | 0,5 |
| 3.5-06 | Pourquoi l'endettement augmente le risque et la rentabilité exigée : les créanciers sont payés avant les associés et à montant fixe ; toute variation de la valeur de l'actif se reporte, amplifiée, sur les fonds propres (risque financier ajouté au risque d'exploitation) ; le bêta passe de 1,00 à 1,57, la rentabilité exigée de 11,50 % à 14,35 % ; un TRI plus élevé n'est pas en soi une création de valeur | 0,5 |
| 3.5-07 | Limites : le MEDAF ne rémunère que le risque systématique, alors que les cadres, non diversifiés, supportent aussi un risque spécifique ; formule de Hamada (dette sans risque, structure constante alors que la dette baisse chaque année) ; valeur de sortie fixée par une hypothèse de multiple ; prime d'illiquidité forfaitaire | 0,5 |

**Fonds propres investis et valeur à l'horizon (item 3.5-01).** Les cadres auraient pu vendre les 640 000 actions détenues par FERVANNE Associés au prix de travail : leur mise de départ est la valeur de cette participation, 36,80 M€, augmentée des apports nouveaux de 5,50 M€, soit **42,30 M€** (annexe 3.4). À l'horizon 2032 :
- valeur de l'entreprise : 5,5 × 22,00 = 121,00 M€ ; valeur des capitaux propres : 121,00 − 4,20 = 116,80 M€ ; valeur d'une action : 116,80 / 1 600 000 = **73,00 €** ;
- valeur des 1 280 000 actions de FERVANNE Associés : **93,44 M€** ;
- la dette senior est entièrement remboursée ; FERVANNE Associés rembourse le crédit-vendeur de 8,00 M€ ; sa trésorerie est nulle dans le plan de la banque ;
- fonds propres de FERVANNE Associés à l'horizon : 93,44 − 8,00 = **85,44 M€**.

**TRI (item 3.5-02).** Aucun flux n'est versé aux associés de FERVANNE Associés avant 2032 :

42,30 = 85,44 / (1 + TRI)^5, d'où TRI = (85,44 / 42,30)^(1/5) − 1 = 2,0199^(0,2) − 1 = **15,10 %** ; multiple de la mise : **2,02**.

**Bêta réendetté et rentabilité exigée (items 3.5-03 et 3.5-04).** Dettes de FERVANNE Associés : 24,00 + 8,00 = 32,00 M€ ; dettes / fonds propres = 32,00 / 42,30 = 0,7565.

Bêta des fonds propres = 1,00 × [1 + (1 − 0,25) × 0,7565] = 1,5674, arrondi à **1,57**.

Rentabilité exigée = 4,0 % + 1,57 × 5,0 % + 2,5 % = **14,35 %**. Sans dette de montage, avec le bêta du secteur, elle serait de 4,0 % + 1,00 × 5,0 % + 2,5 % = **11,50 %**.

**Comparaison et lien entre risque et rentabilité exigée (items 3.5-05 à 3.5-07).**
- Le TRI attendu (15,10 %) dépasse la rentabilité exigée (14,35 %) de 0,75 point : dans le plan de la banque, l'opération rémunère le risque que prennent les cadres, et un peu au-delà. La marge est étroite : avec un multiple de sortie de 5,0, les fonds propres à l'horizon tomberaient à 76,64 M€ et le TRI à 12,62 %, inférieur à la rentabilité exigée ; avec 6,0, il atteindrait 17,38 %. Ce TRI suppose aussi que FERVANNE distribue ce que demande la banque (87,70 % du résultat en 2028), contrairement au plafond de 80 %.
- Sans dette, la rentabilité exigée serait de 11,50 % : la dette de montage l'augmente de 2,85 points. Les prêteurs ont une créance fixe et prioritaire ; les cadres sont créanciers du résidu. Toute variation de la valeur de FERVANNE, dont le risque d'exploitation est mesuré par le bêta de l'actif de 1,00, se reporte sur des fonds propres plus étroits que l'actif : le risque financier s'ajoute au risque d'exploitation, et le bêta des fonds propres passe à 1,57. Un investisseur rationnel exige une prime de risque plus élevée pour un actif plus risqué : c'est le lien entre incertitude et rentabilité exigée. Comme l'ont montré Modigliani et Miller, la rentabilité exigée des fonds propres croît avec l'endettement : le supplément de TRI permis par la dette est d'abord la rémunération de ce risque, et non une création de valeur. La création de valeur se lit dans l'écart entre le TRI et la rentabilité exigée correspondant au même niveau de dette.
- Limites : le MEDAF suppose des investisseurs diversifiés ; les cadres ne le sont pas (leur emploi et leur épargne dépendent de FERVANNE), et leur risque réel dépasse celui que mesure le bêta. La formule de Hamada suppose une dette sans risque et une structure constante, alors que la dette est remboursée chaque année : la rentabilité exigée baisse au fil du plan. La valeur de sortie dépend d'une hypothèse de multiple fournie par la banque, et la prime d'illiquidité de 2,5 points est forfaitaire.

**Réponses tolérées** : TRI calculé avec le multiple arrondi à 2,02 (même résultat, 15,10 %) ; rentabilité exigée calculée avec le bêta non arrondi (14,34 %) ; commentaire sur la baisse du bêta au fil du remboursement.

**Erreurs fréquentes**
- Rapporter la valeur de sortie aux seuls apports nouveaux de 5,50 M€ en gardant la valeur de toute la participation (TRI aberrant de 73 % ; 47,75 % si l'on ne garde que les 640 000 actions achetées, ce qui oublie que les dividendes de la participation existante servent la dette).
- Oublier de déduire le crédit-vendeur de la valeur de sortie.
- Réendetter le bêta avec la dette financière nette de FERVANNE (9,50 M€) au lieu des dettes de FERVANNE Associés, ou oublier le facteur (1 − 25 %) de la formule donnée (`JUR-E02`).
- Conclure que l'opération crée de la valeur parce que le TRI dépasse le coût de la dette, sans le comparer à la rentabilité exigée des fonds propres.

**Références** : F02 § 2 et § 3 (MEDAF, réendettement par Hamada avec IS) [V programme 5.2 ; S] ; F05 § 1.3 (TRI et multiple de la mise d'un montage) [S] ; F10 (Sharpe, 1964 ; Modigliani et Miller, 1958, 1963) ; programme 5.2.a, 5.2.b et 5.2.c, guide p. 74-75 (incertitude et rentabilité exigée ; primes de risque fournies) [V] ; F11 (taux sans risque de 4 % et prime de 5 %, hypothèses d'énoncé) [V].

---

### 3.6 Cap sur l'Euribor 3 mois et comparaison avec le swap (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Prime du trimestre : 24 000 000 × 0,50 % × 91 / 360 = **30 333,33 €** ; intérêts : **263 900,00 €** (taux constaté 2,00 %), **324 566,67 €** (3,00 %), **373 100,00 €** (3,80 %) ; versement du cap nul, nul, **33 366,67 €** | 0,5 |
| 3.6-02 | Coût net : **294 233,33 € ; 354 900,00 € ; 370 066,67 €** ; taux effectif **4,85 % ; 5,85 % ; 6,10 %** ; plafond 3,25 % + 2,35 % + 0,50 % = 6,10 %, au-dessus du taux de 5,00 % du plan (le surcoût de 0,264 M€ d'intérêts en 2028 au plafond n'est pas exigé) | 0,5 |
| 3.6-03 | Valeur intrinsèque au taux du jour : 2,65 % < 3,25 %, **0 €** (cap hors de la monnaie) ; valeur temps **30 333,33 €** par trimestre : la prime rémunère la probabilité que le taux dépasse 3,25 % pendant cinq ans | 0,5 |
| 3.6-04 | Cap et swap : le cap est une option (droit, non obligation) qui plafonne le taux et laisse profiter d'une baisse, contre une prime payée dans tous les cas ; le swap est un engagement ferme, sans prime, qui fixe le taux et fait perdre le bénéfice d'une baisse | 0,5 |
| 3.6-05 | Gré à gré : contrat adapté au nominal qui s'amortit, aux dates d'intérêts et à la durée de la dette, sans dépôt de garantie ni appels de marge ; en contrepartie, risque de contrepartie sur la banque, contrat peu liquide, coût de sortie si la dette est remboursée par anticipation ; différent des options standardisées des marchés organisés | 0,5 |
| 3.6-06 | Recommandation argumentée pour une capacité de remboursement tendue : le swap fixe le service sur lequel repose le plan, sans prime ; le cap protège contre une forte hausse, mais coûte 0,12 M€ par an et laisse le taux monter jusqu'à 6,10 %, ce que la couverture de 2028 ne supporterait pas ; cap acceptable si les cadres veulent garder la baisse des taux ou prévoient un remboursement anticipé, avec un prix d'exercice adapté | 0,5 |

**Calculs du premier trimestre de 2028 (items 3.6-01 et 3.6-02).** Nominal 24 000 000 € ; 91 jours ; base Exact/360 ; marge 2,35 % ; prix d'exercice 3,25 % ; prime 24 000 000 × 0,50 % × 91 / 360 = 30 333,33 €.

| Taux constaté | 2,00 % | 3,00 % | 3,80 % |
|---|---:|---:|---:|
| Intérêts : 24 000 000 × (taux + 2,35 %) × 91 / 360 | 263 900,00 | 324 566,67 | 373 100,00 |
| Versement du cap : 24 000 000 × max(0 ; taux − 3,25 %) × 91 / 360 | 0 | 0 | 33 366,67 |
| Prime du trimestre | 30 333,33 | 30 333,33 | 30 333,33 |
| **Coût net** | **294 233,33** | **354 900,00** | **370 066,67** |
| **Taux effectif** (coût net / nominal × 360 / 91) | **4,85 %** | **5,85 %** | **6,10 %** |

Le taux effectif ne peut pas dépasser 3,25 % + 2,35 % + 0,50 % = **6,10 %**, quel que soit le taux constaté. Dans le scénario de baisse, FERVANNE Associés profite de la baisse (4,85 %), diminuée de la prime. Le plafond reste supérieur au taux de 5,00 % du plan de la banque : au plafond, les intérêts de 2028 seraient de 24,00 × 6,10 % = 1,464 M€ au lieu de 1,20 M€, soit 0,264 M€ de plus ; avec la distribution plafonnée, la couverture de 2028 tomberait de 0,91 à 5,904 / 6,744 = 0,88.

**Valeur intrinsèque et valeur temps (item 3.6-03).** Au taux du jour (2,65 %), l'option est hors de la monnaie : sa valeur intrinsèque, 24 000 000 × max(0 ; 2,65 % − 3,25 %) × 91 / 360, est **nulle**. Toute la prime du trimestre, **30 333,33 €**, est de la valeur temps : elle rémunère le vendeur pour la probabilité que le taux de référence dépasse 3,25 % au cours des cinq ans. Elle diminuera à mesure que l'échéance approche et que le nominal s'amortit.

**Cap ou swap (items 3.6-04 à 3.6-06).**
- *Nature des instruments.* Le cap est un instrument optionnel : FERVANNE Associés achète le droit de recevoir l'excédent du taux sur 3,25 %, sans obligation ; elle paie une prime quoi qu'il arrive (0,12 M€ par an sur 24,00 M€, puis moins à mesure que le nominal baisse) et garde le bénéfice d'une baisse. Le swap est un instrument ferme : FERVANNE Associés paierait un taux fixe et recevrait le taux variable ; sans prime, il transforme la dette en dette à taux fixe, ce qui protège contre la hausse mais fait perdre la baisse.
- *Gré à gré.* Le cap et le swap proposés sont négociés directement avec la Banque HAUTMERLE : le nominal peut suivre le capital restant dû, les dates coïncident avec celles des intérêts, la durée avec celle du prêt, sans dépôt de garantie ni appels de marge. En contrepartie, FERVANNE Associés dépend de la solidité de la banque, ne peut pas revendre facilement le contrat, et le swap devrait être dénoué (à un coût qui dépend des taux) si la dette était remboursée par anticipation. Une option sur un contrat à terme de taux d'un marché organisé serait standardisée (montant, échéances), avec une chambre de compensation, mais mal adaptée à un nominal qui s'amortit.
- *Recommandation.* Le montage est tendu : la couverture est inférieure à 1 en 2028 et 2029 au taux de 5,00 %. Ce qui compte est de connaître et de tenir le service sur lequel repose le plan. Le swap fixe ce service sans prime : si son taux fixe est proche du taux de référence actuel, le coût reste voisin de 5,00 % et le plan est sécurisé. Le cap ne joue qu'au-delà d'un taux de référence de 3,25 % et plafonne le coût, prime comprise, à 6,10 %, niveau que le montage ne supporterait pas ; sa prime alourdit chaque année un service déjà difficile à couvrir. Il conviendrait mieux à un emprunteur qui a de la marge et veut garder le bénéfice d'une baisse, ou qui prévoit de rembourser par anticipation. Le swap est donc préférable ici, à demander chiffré à la banque ; à défaut, un cap de prix d'exercice plus élevé et moins cher, ou un tunnel, limite le risque extrême.

**Réponses tolérées** : taux effectif calculé hors prime (4,35 % ; 5,35 % ; 5,60 %) si la prime est ensuite ajoutée en taux annuel ; recommandation du cap si elle est justifiée par le souhait de profiter d'une baisse des taux, par un remboursement anticipé probable (cession, refinancement) ou par l'absence de coût de sortie, et si le candidat montre que le plafond de 6,10 % dégrade la couverture ; mention d'un tunnel (achat du cap et vente d'un floor) pour réduire la prime.

**Erreurs fréquentes**
- Calculer les intérêts sur une année au lieu de 91 jours, ou en base 365 (`JUR-T04`).
- Appliquer le versement du cap à la marge (taux + 2,35 % − 3,25 %) : le cap porte sur le seul taux de référence.
- Oublier la prime dans le coût net, ou la compter seulement quand le cap est exercé.
- Décrire le swap comme une option, ou dire que le cap est gratuit parce qu'il n'est pas exercé.
- Valoriser la prime par un modèle d'évaluation des options : la prime est donnée.

**Références** : F07 § 2.2 (swap de taux), § 2.3 (cap, valeur intrinsèque et valeur temps, prime donnée) et § 2.4 (choix d'une couverture : coût, flexibilité, risque résiduel) [V programme 6.2 ; guide p. 78 ; S] ; F01 § 7 (base Exact/360) [S] ; F11 (Euribor 3 mois de 2,65 %, hypothèse d'énoncé cohérente avec la moyenne de septembre 2026) [V].
