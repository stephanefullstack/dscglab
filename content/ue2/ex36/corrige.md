# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 36 — Dossier 3 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F07 risques de taux et de change, F08 gouvernance et ESG, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (VAN, TRI et indice de profitabilité des deux projets et des flux différentiels, coût actuariel avant et après impôt de l'emprunt, du prêt indexé sur la durabilité dans ses deux cas et du crédit-bail, rapport dette financière nette / EBITDA et gearing avant et après le financement, cours à terme, vente à terme, option de vente de devises dans les deux scénarios, valeur intrinsèque et valeur temps de la prime, barème, liste noire, hors-programme ; VAN par action, poids de la valeur résiduelle et de la montée en charge, effet annuel du prêt indexé, perte de change et cours d'indifférence vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un classement des financements fondé sur un coût du crédit-bail erroné, ou une comparaison des couvertures fondée sur un cours à terme erroné).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 VAN, TRI et IP des deux projets, conflit de classement et choix | `7.1.a` Évaluer et classer des projets en milieu certain ; `7.1.c` Déterminer la création de valeur à travers la décision d'investissement ou de désinvestissement | 4 |
| 3.2 VAN et valeur créée pour les actionnaires, hypothèses clés | `7.1.c` | 1,5 |
| 3.3 Coût actuariel des trois financements | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `7.2.c` Analyser les nouveaux outils de financement | 3 |
| 3.4 Prêts indexés sur la durabilité, structure financière et recommandation | `7.2.c` ; `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière et identifier ses déterminants ; `7.2.a` | 2,25 |
| 3.5 Position de change, marché au comptant et à terme, vente à terme | `6.3.a` Caractériser la position de change courte ou longue, ouverte ou fermée ; `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) | 2 |
| 3.6 Option de vente de devises, comparaison avec le terme | `6.3.d` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (change) | 2,25 |
| **Total** | | **15** |

Part du calcul : environ 8,4 points (3.1-01 à 3.1-03, la moitié de 3.2-01, 3.3-01 à 3.3-04, la moitié de 3.4-02, la moitié de 3.5-01, 3.5-03, 3.6-01, 3.6-02 et le quart de 3.6-03). Part de l'analyse : environ 6,6 points. Le dossier est le dernier de l'épreuve : les questions 3.4 et 3.6, qui demandent une recommandation, ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 VAN, TRI et IP des deux projets, conflit de classement et choix (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Flux actualisés à 8 % (tableau) ; VAN de A = 48,13 − 42,00 = **6,13 M€** ; VAN de B = 88,95 − 80,00 = **8,95 M€** | 1 |
| 3.1-02 | TRI de A **10,69 %** (VAN de 1,45 à 10 % et de − 0,65 à 11 %) ; TRI de B **9,92 %** (VAN de 4,13 à 9 % et de − 0,33 à 10 % ; 9,93 % par interpolation) ; les deux TRI dépassent le CMPC | 1 |
| 3.1-03 | IP de A = 48,13 / 42,00 = **1,15** ; IP de B = 88,95 / 80,00 = **1,11** | 0,5 |
| 3.1-04 | Conflit : la VAN classe B en tête, le TRI et l'IP classent A ; causes : tailles différentes (80 contre 42 M€), profils temporels différents (montée en charge de B, valeur résiduelle), hypothèse implicite de réinvestissement des flux au TRI | 0,75 |
| 3.1-05 | Décision par les flux différentiels B − A : 38,00 M€ investis en plus, VAN **2,82 M€** (TRI de 9,19 % > 8 %, non exigé) ; pas de rationnement du capital : l'IP n'est pas le bon critère ; retenir **B**, qui crée le plus de valeur | 0,75 |

**Conventions rappelées** (annexes 3.2 et 3.5) : date 0 = 31 août 2029 ; investissement à la date 0 ; flux en fin d'année universitaire ; valeur résiduelle ajoutée au flux de l'année 10 ; CMPC de 8,00 % ; coefficients d'actualisation non arrondis et chaque flux actualisé arrondi au centième.

**Flux actualisés à 8 % (1 pt).**

| Année | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Somme |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Coefficient 1,08^−t | 0,9259 | 0,8573 | 0,7938 | 0,7350 | 0,6806 | 0,6302 | 0,5835 | 0,5403 | 0,5002 | 0,4632 | |
| A : flux (valeur résiduelle comprise en 10) | 5,00 | 6,40 | 6,40 | 6,40 | 6,40 | 6,40 | 6,40 | 6,40 | 6,40 | 20,40 | |
| A : flux actualisés | 4,63 | 5,49 | 5,08 | 4,70 | 4,36 | 4,03 | 3,73 | 3,46 | 3,20 | 9,45 | **48,13** |
| B : flux (valeur résiduelle comprise en 10) | 6,50 | 9,00 | 11,00 | 12,50 | 12,50 | 12,50 | 12,50 | 12,50 | 12,50 | 44,50 | |
| B : flux actualisés | 6,02 | 7,72 | 8,73 | 9,19 | 8,51 | 7,88 | 7,29 | 6,75 | 6,25 | 20,61 | **88,95** |

- VAN de A = 48,13 − 42,00 = **6,13 M€** ; VAN de B = 88,95 − 80,00 = **8,95 M€**. Les deux projets sont acceptables isolément : ils rapportent plus que le CMPC.
- Calcul plus rapide par les annuités, accepté : pour A, 5,00 × 1,08^−1 + 6,40 × (6,7101 − 0,9259) + 14,00 × 1,08^−10 = 4,63 + 37,02 + 6,48 = 48,13.

**TRI (1 pt).** Le TRI annule la VAN. Par interpolation linéaire :
- A : VAN à 10 % = 1,45 ; à 11 % = − 0,65 ; TRI = 10 % + 1 % × 1,45 / (1,45 + 0,65) = **10,69 %** ;
- B : VAN à 9 % = 4,13 ; à 10 % = − 0,33 ; TRI = 9 % + 1 % × 4,13 / (4,13 + 0,33) = 9,93 % par interpolation (**9,92 %** pour la valeur exacte).

Les deux TRI dépassent le CMPC de 8 % : chaque projet, pris seul, est rentable.

**IP (0,5 pt).** IP = somme des flux actualisés / investissement : A = 48,13 / 42,00 = **1,15** ; B = 88,95 / 80,00 = **1,11**. Chaque euro investi dans A rapporte 1,15 € en valeur actuelle, contre 1,11 € dans B.

**Le conflit de classement (0,75 pt).**

| Critère | A : réhabilitation | B : campus neuf | Classement |
|---|---:|---:|---|
| VAN (M€) | 6,13 | 8,95 | B |
| TRI | 10,69 % | 9,92 % | A |
| IP | 1,15 | 1,11 | A |

- **Tailles différentes** : le TRI et l'IP sont des mesures **relatives** (rentabilité par euro investi), la VAN une mesure **absolue** (richesse créée). B rapporte un peu moins par euro, mais sur presque deux fois plus d'euros (80,00 contre 42,00 M€).
- **Profils temporels différents** : B est plus long à remplir (55 % la première année) ; une plus grande part de ses flux arrive tard, dont une valeur résiduelle de 32,00 M€. Ces flux lointains pèsent moins quand le taux monte : la VAN de B baisse plus vite que celle de A.
- **Hypothèse de réinvestissement** : le TRI suppose que les flux intermédiaires sont réinvestis au TRI du projet (10,69 % pour A), la VAN qu'ils le sont au CMPC (8 %), hypothèse plus prudente et commune aux deux projets.
- **Taux d'indifférence** (non exigé) : les deux VAN sont égales pour un taux de 9,19 %. En dessous de ce taux, B a la plus forte VAN ; au-dessus, A. Au CMPC de 8 %, B l'emporte.

**La décision (0,75 pt).** Choisir B revient à investir **38,00 M€ de plus** que pour A, pour obtenir les flux différentiels B − A :

| Année | 0 | 1 | 2 | 3 | 4 à 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|
| Flux B − A (M€) | − 38,00 | 1,50 | 2,60 | 4,60 | 6,10 | 24,10 |

Cet investissement supplémentaire a une VAN de 8,95 − 6,13 = **2,82 M€** : il crée de la valeur (son TRI, 9,19 %, supérieur au CMPC, le confirme ; non exigé). Le groupe n'est pas rationné en capital (annexe 3.2 : il peut financer l'un ou l'autre projet, et aucun autre projet n'attend ces fonds) ; l'IP, utile pour répartir un budget limité, n'est donc pas le critère pertinent. Entre deux projets exclusifs, on retient celui qui crée le plus de valeur pour les actionnaires : le **campus neuf (B)**.

**Réponses tolérées** : TRI de B de 9,93 %, résultat de l'interpolation prévue par l'annexe 3.5 ; TRI par interpolation entre d'autres taux encadrants (par exemple 10,7 % et 9,9 %) ; VAN différentielle de 2,81 M€ si les flux B − A sont actualisés un à un ; IP de 1,146 et 1,112 ; décision justifiée par la seule VAN, sans les flux différentiels, si le candidat explique pourquoi le TRI et l'IP ne conviennent pas à des projets de tailles différentes (0,5 sur 0,75 à l'item 3.1-05) ; mention de la VAN globale et du TRI global au taux de réinvestissement de 8 % comme solution au conflit, sans calcul ; choix de A justifié par le risque de remplissage de B, si le candidat reconnaît que B a la plus forte VAN (0,25 sur 0,75 à l'item 3.1-05).

**Erreurs fréquentes**
- Actualiser l'investissement de la date 0, ou oublier la valeur résiduelle de l'année 10 (VAN de − 0,35 ou − 0,36 M€ pour A, selon la méthode, et de − 5,87 M€ pour B).
- Calculer l'IP sur la VAN seule (0,15 et 0,11).
- Retenir A au motif que son TRI est le plus élevé, sans voir la différence de taille.
- `JUR-I05` — calculer les critères sans analyser la divergence du classement ; `JUR-T04` — erreurs d'actualisation ou d'interpolation, acquis du DCG exigibles.
- `JUR-T07` — flux actualisés présentés sans tableau.

---

### 3.2 VAN et valeur créée pour les actionnaires, hypothèses clés (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | La VAN au CMPC est ce qui reste après la rémunération exigée par les prêteurs et les actionnaires ; les prêteurs recevant une rémunération contractuelle, ce surplus revient aux actionnaires ; effet par action : 8,95 M€ / 40 000 000 = **0,22 €** | 0,75 |
| 3.2-02 | Hypothèses qui pèsent le plus, chiffrées : valeur résiduelle (14,82 M€ actualisés, sans laquelle la VAN serait de − 5,87 M€) ; remplissage (la montée en charge des trois premières années coûte déjà 9,75 M€ actualisés, plus que la VAN) ; recette par étudiant (9 600 €, dont la revalorisation est supposée absorbée par la hausse des charges) | 0,75 |

**La VAN, mesure de la valeur créée pour les actionnaires (0,75 pt).**
- Les flux du projet sont des flux d'exploitation, avant toute rémunération des apporteurs de capitaux ; ils sont actualisés au **CMPC**, qui est la rentabilité exigée en moyenne par les prêteurs et par les actionnaires pour un risque égal à celui du groupe (annexe 3.2).
- Une VAN nulle signifie que le projet rémunère tout juste ces exigences. Une VAN positive est un **surplus** : les prêteurs ne reçoivent que leurs intérêts et leur remboursement, fixés par contrat ; le surplus revient donc aux **actionnaires**. Si le marché anticipe correctement le projet, la valeur des capitaux propres augmente de la VAN.
- Le choix du financement n'entre pas dans la VAN : il est étudié à part (questions 3.3 et 3.4), le coût des ressources étant déjà pris en compte par le CMPC.
- **Effet par action** : 8,95 M€ / 40 000 000 actions = **0,22 €** par action. La VAN représente 11,19 % de l'investissement (8,95 / 80,00) : la création de valeur est réelle mais modeste à l'échelle du groupe.

**Les hypothèses qui pèsent le plus (0,75 pt).**
- **La valeur résiduelle** : 32,00 × 1,08^−10 = **14,82 M€** actualisés, soit plus que la VAN. Sans elle, la VAN de B serait de 8,95 − 14,82 = **− 5,87 M€**. Le projet n'est créateur de valeur sur dix ans que si le bâtiment garde une valeur élevée en 2039.
- **Le remplissage** : le campus neuf part de 55 % de remplissage. La montée en charge des années 1 à 3 coûte, par rapport au flux de plein régime de 12,50 M€, (12,50 − 6,50) × 1,08^−1 + (12,50 − 9,00) × 1,08^−2 + (12,50 − 11,00) × 1,08^−3 = 5,56 + 3,00 + 1,19 = **9,75 M€** actualisés, plus que la VAN : une montée en charge plus lente que prévu, faute de notoriété des trois écoles à Bordeaux, peut suffire à la rendre nulle.
- **La recette par étudiant** : les flux supposent 9 600 € par étudiant et par an, pour des formations nouvelles, dont la revalorisation est supposée absorbée par la hausse des charges : une revalorisation plus faible, ou des charges plus dynamiques, réduirait les flux. Une concurrence plus vive ou une baisse de la prise en charge des contrats d'apprentissage réduirait tous les flux.
- À ces trois hypothèses s'ajoute le taux : au-delà de 9,92 %, la VAN de B devient négative.

**Réponses tolérées** : effet par action exprimé en pourcentage de la valeur par action sans la chiffrer (la valeur de l'action n'est pas donnée dans ce dossier) ; analyse de la sensibilité par la baisse uniforme du flux annuel qui annulerait la VAN (1,33 M€ par an, soit 8,95 / 6,7101), non exigée ; hypothèses citées sans chiffrage mais reliées aux données de l'annexe 3.1 (0,25 sur 0,75 à l'item 3.2-02).

**Erreurs fréquentes**
- Dire que la VAN revient aux prêteurs, ou la diviser par le nombre d'actions après l'introduction en bourse sans le justifier.
- Déduire les frais financiers des flux du projet, ce qui compte deux fois le coût de la dette.
- `JUR-T13` — citer « les hypothèses » en général sans les chiffres du projet.

---

### 3.3 Coût actuariel des trois financements (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Emprunt classique in fine sans frais : coût avant impôt **4,20 %** ; après impôt 4,20 % × 0,75 = **3,15 %** (flux après impôt de − 1,89 M€ par an, − 61,89 M€ en année 12) | 0,5 |
| 3.3-02 | Prêt indexé : indicateurs atteints, taux 4,05 %, charge annuelle 2,43 + 0,048 = 2,478 M€, coût **4,13 %** avant impôt et **3,10 %** après ; indicateurs manqués, taux 4,35 %, charge 2,658 M€, coût **4,43 %** et **3,32 %** | 1 |
| 3.3-03 | Crédit-bail : flux après impôt, + 60,00 en 0 ; − 6,75 × 0,75 − 0,25 × 60,00 / 24 = − 5,6875 M€ des années 1 à 12 ; − 0,625 M€ des années 13 à 24 (économies d'impôt sur l'amortissement perdues) | 0,5 |
| 3.3-04 | Crédit-bail : coût avant impôt **4,95 %** (12 loyers de 6,75 M€) ; après impôt **3,24 %** | 0,5 |
| 3.3-05 | Classement après impôt : prêt indexé, indicateurs atteints (3,10 %) < emprunt classique (3,15 %) < crédit-bail (3,24 %) < prêt indexé, indicateurs manqués (3,32 %) ; l'avantage du prêt indexé dépend de l'atteinte des objectifs | 0,5 |

**Conventions rappelées** (annexes 3.3 et 3.5) : 60,00 M€ reçus à la date 0 ; flux annuels en fin d'année vus de l'emprunteur ; intérêts, coût de la vérification et loyers déductibles l'année de leur paiement ; IS 25 % ; bâtiment amortissable sur 24 ans s'il est acheté.

**Emprunt bancaire classique (0,5 pt).** Flux avant impôt : + 60,00 en 0 ; − 60,00 × 4,20 % = − 2,52 M€ par an ; − 62,52 M€ en année 12. Le capital étant reçu et remboursé pour sa valeur, sans frais, le taux actuariel est égal au taux nominal : **4,20 %**. Après impôt, chaque intérêt procure une économie d'impôt de 25 % : flux de − 2,52 × 0,75 = − 1,89 M€ par an et − 61,89 M€ en année 12, d'où un coût de 4,20 % × 0,75 = **3,15 %**.

**Prêt indexé sur la durabilité (1 pt).** Selon l'annexe 3.5, l'ajustement s'applique dès les intérêts de l'année 1 et il est le même pendant les douze ans dans chacun des deux cas ; la charge annuelle comprend les intérêts et le coût de la vérification (0,048 M€), qui sont déductibles. Le prêt étant in fine et sans frais, le coût actuariel est égal à la charge annuelle rapportée au capital.

| | Indicateurs atteints | Indicateurs manqués |
|---|---:|---:|
| Taux d'intérêt : 4,20 % ∓ 2 × 0,075 point | 4,05 % | 4,35 % |
| Intérêts (M€) | 2,430 | 2,610 |
| + Vérification et suivi (M€) | 0,048 | 0,048 |
| = Charge annuelle avant impôt (M€) | 2,478 | 2,658 |
| **Coût avant impôt** (charge / 60,00) | **4,13 %** | **4,43 %** |
| Charge annuelle après impôt (× 0,75) | 1,8585 | 1,9935 |
| **Coût après impôt** | **3,10 %** | **3,32 %** |

La vérification coûte 0,048 / 60,00 = 0,08 point par an : elle absorbe plus de la moitié de la baisse de taux obtenue si les objectifs sont atteints (0,15 point).

**Crédit-bail immobilier (1 pt).** Par rapport à un achat, le crédit-bail évite de décaisser 60,00 M€ à la date 0 ; en contrepartie, le groupe paie douze loyers déductibles et perd les économies d'impôt sur l'amortissement du bâtiment qu'il aurait pratiqué en l'achetant : 25 % × 60,00 / 24 = 0,625 M€ par an pendant 24 ans. L'option d'achat d'un euro symbolique est négligée ; après sa levée, le bâtiment n'est plus amortissable.

| Années | 0 | 1 à 12 | 13 à 24 |
|---|---:|---:|---:|
| Montant financé | + 60,00 | | |
| Loyers après impôt : − 6,75 × 0,75 | | − 5,0625 | |
| Économies d'impôt sur l'amortissement perdues : − 0,25 × 60,00 / 24 | | − 0,625 | − 0,625 |
| **Flux après impôt** | **+ 60,00** | **− 5,6875** | **− 0,625** |

- **Coût avant impôt** : taux qui égalise 60,00 et la valeur actuelle de douze loyers de 6,75 M€. VAN des flux à 4,5 % : − 1,55 ; à 5 % : + 0,17 ; par interpolation **4,95 %**.
- **Coût après impôt** : taux qui annule 60,00 − 5,0625 × [1 − (1 + r)^−12] / r − 0,625 × [1 − (1 + r)^−24] / r. À 3 % : 60,00 − 5,0625 × 9,9540 − 0,625 × 16,9355 = − 0,98 ; à 3,5 % : 60,00 − 5,0625 × 9,6633 − 0,625 × 16,0584 = + 1,04 ; par interpolation **3,24 %**.

**Classement (0,5 pt).**

| Financement | Coût avant impôt | Coût après impôt | Rang après impôt |
|---|---:|---:|---:|
| Prêt indexé, indicateurs atteints | 4,13 % | 3,10 % | 1 |
| Emprunt classique | 4,20 % | 3,15 % | 2 |
| Crédit-bail immobilier | 4,95 % | 3,24 % | 3 |
| Prêt indexé, indicateurs manqués | 4,43 % | 3,32 % | 4 |

Le prêt indexé n'est le moins cher que si les deux objectifs sont atteints chaque année ; s'ils sont manqués, il devient le plus cher. Le crédit-bail coûte nettement plus que les emprunts avant impôt (4,95 % contre 4,20 %), mais l'écart se réduit après impôt (3,24 % contre 3,15 %), parce que les loyers sont déduits en douze ans alors que l'amortissement d'un bâtiment acheté l'aurait été en vingt-quatre ans. Cet avantage tient aux conventions de l'énoncé : la fiscalité propre au crédit-bail immobilier, qui relève de l'UE 1, n'est pas prise en compte.

**Réponses tolérées** : coûts des emprunts obtenus par interpolation plutôt que par le raisonnement direct ; coût après impôt du prêt indexé exprimé comme (taux ajusté + 0,08 point) × 0,75 ; coût du crédit-bail après impôt de 3,25 % si les flux sont arrondis à − 5,69 et − 0,63 M€ ; cas intermédiaire (un objectif atteint, l'autre manqué : 4,28 % et 3,21 %) présenté en plus.

**Erreurs fréquentes**
- Oublier les économies d'impôt sur l'amortissement perdues en crédit-bail (coût après impôt de 0,19 %, résultat absurde qui ferait du crédit-bail un financement presque gratuit), ou ne les compter que pendant les douze ans du contrat.
- Oublier le coût de la vérification (coûts après impôt de 3,04 % et 3,26 %), ou ne pas tenir compte de l'économie d'impôt qu'il procure (3,12 % et 3,34 %).
- Appliquer l'ajustement de 0,075 point une seule fois au lieu d'une fois par indicateur.
- `JUR-T04` — coût actuariel d'un emprunt non maîtrisé (acquis du DCG).

---

### 3.4 Prêts indexés sur la durabilité, structure financière et recommandation (2,25 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Prêts indexés : principe (usage libre des fonds, taux ajusté selon des objectifs de durabilité), conditions d'accès (stratégie de durabilité, indicateurs importants pour l'activité, mesurables et vérifiés, objectifs ambitieux, publication), risque d'écoblanchiment et coût de la vérification (48 000 €, 0,08 point ; gain net de 31 500 € par an après impôt si les objectifs sont atteints) ; appréciation des deux indicateurs : l'objectif d'énergie est atteint par construction (85 contre 90 kWh), celui des boursiers est exigeant et lié à la mission | 1 |
| 3.4-02 | Dette financière nette / EBITDA : 214,00 / 112,00 = **1,91** avant, 274,00 / 112,00 = **2,45** après ; gearing **50,95 %** puis **65,24 %** ; même effet pour les trois offres en IFRS ; marge de 62,00 M€ sous la clause de 3,00, de 6,00 M€ seulement sous l'objectif de 2,50 ; remboursement in fine des emprunts contre amortissement progressif du crédit-bail | 0,75 |
| 3.4-03 | Recommandation argumentée, cohérente avec les coûts et la structure financière (par exemple le prêt indexé, sous réserve d'un objectif d'énergie plus exigeant) | 0,5 |

**Les prêts indexés sur la durabilité (1 pt).**
- **Principe** : un prêt dont les fonds sont d'**usage libre** (à la différence d'un prêt vert, affecté à un projet), mais dont le **taux est ajusté**, à la hausse ou à la baisse, selon que l'emprunteur atteint ou non des objectifs de durabilité chiffrés, mesurés par des indicateurs et vérifiés chaque année (F08 § 5.1). L'ajustement est faible (ici 0,075 point par indicateur) : il incite plus qu'il n'enrichit.
- **Conditions d'accès** : une stratégie de durabilité déjà formalisée ; des indicateurs **importants** pour l'activité de l'emprunteur, **mesurables** et **vérifiés** par un tiers ; des objectifs **ambitieux** par rapport à la situation de départ, fixés à l'avance ; une publication régulière. Le coût fixe de la mesure et de la vérification réserve ce financement aux emprunteurs d'une certaine taille.
- **Coût de la vérification** : 48 000 € par an, soit 0,08 point. Si les objectifs sont atteints, le gain de taux (60,00 × 0,15 % = 0,09 M€) moins la vérification laisse **0,042 M€** par an avant impôt, **31 500 €** après impôt. S'ils sont manqués, le surcoût atteint 0,138 M€ par an avant impôt (0,1035 M€ après impôt) par rapport à l'emprunt classique. L'avantage financier direct est donc faible et dissymétrique ; l'intérêt est ailleurs : crédibilité de la stratégie de durabilité auprès des futurs actionnaires, des étudiants et des familles, discipline interne.
- **Risque d'écoblanchiment** : si les objectifs sont trop faciles à atteindre, le prêt affiche un engagement de durabilité qui ne change rien aux pratiques ; le groupe s'expose alors à un risque de réputation, d'autant plus grave à l'approche de l'introduction en bourse, où les investisseurs examinent l'information extra-financière.
- **Appréciation des deux indicateurs proposés** :
  - **énergie** : l'objectif (90 kWh par m²) est moins exigeant que la performance prévue par l'étude thermique du bâtiment neuf (85 kWh par m²) ; il sera atteint par construction, sans effort supplémentaire. C'est l'exemple même d'un objectif peu ambitieux, d'autant que la banque l'a accepté sans le discuter. Un objectif plus exigeant (par exemple 75 kWh par m², ou une baisse de la consommation de l'ensemble des campus du groupe, aujourd'hui de 165 kWh par m²) serait plus crédible ;
  - **boursiers** : passer de 11 % à 18 % d'étudiants boursiers est un objectif exigeant, lié à la mission d'un établissement d'enseignement et à l'attente de ses parties prenantes (Freeman, 1984) ; il comporte un risque d'échec réel, ce qui le rend crédible, mais il peut peser sur la recette par étudiant si le groupe accorde ses propres réductions de frais.

**Effet sur la structure financière (0,75 pt).**

| Au 31 décembre 2029 (M€) | Avant le financement du bâtiment | Après |
|---|---:|---:|
| Dette financière nette | 214,00 | 214,00 + 60,00 = 274,00 |
| EBITDA consolidé de 2029 | 112,00 | 112,00 |
| **Dette financière nette / EBITDA** | **1,91** | **2,45** |
| Capitaux propres | 420,00 | 420,00 |
| **Gearing** | **50,95 %** | **65,24 %** |

- L'effet est **le même pour les trois offres** : en IFRS, le crédit-bail est inscrit au bilan (droit d'utilisation et dette de 60,00 M€) et les loyers sortent de l'EBITDA. Le crédit-bail n'apporte donc aucun allègement apparent de l'endettement dans les comptes consolidés.
- Le rapport passe de 1,91 à 2,45 : il reste sous la clause des prêteurs (3,00, marge de 3,00 × 112,00 − 274,00 = 62,00 M€), mais presque à l'objectif de 2,50 que la direction veut annoncer aux investisseurs (marge de 280,00 − 274,00 = **6,00 M€**). Toute acquisition supplémentaire devra être financée surtout par fonds propres ou par l'autofinancement.
- **Profil de remboursement** : les deux emprunts sont in fine ; la dette de 60,00 M€ reste entière pendant douze ans et doit être remboursée ou refinancée en 2041. Le crédit-bail s'amortit avec les loyers : la dette diminue chaque année et le risque de refinancement disparaît, au prix d'un coût plus élevé.

**Recommandation (0,5 pt).** Exemple de réponse : retenir le **prêt indexé sur la durabilité**, à condition de renégocier l'objectif d'énergie.
- Si les objectifs sont atteints, c'est le financement le moins cher (3,10 % après impôt) ; le risque de surcoût est limité (0,10 M€ par an après impôt au pire) et il est maîtrisé par le groupe.
- Il donne à l'introduction en bourse un signal de l'engagement de durabilité du groupe : signal crédible seulement s'il est coûteux à imiter (Spence, 1973), donc avec des objectifs exigeants ; l'objectif d'énergie actuel, atteint d'avance, l'affaiblirait et exposerait le groupe à une accusation d'écoblanchiment.
- Le choix d'une dette plutôt que d'une émission d'actions pour le campus est conforme au financement hiérarchique (Myers et Majluf, 1984) ; mais, à 2,45 fois l'EBITDA, le groupe approche le niveau d'endettement qu'il s'est fixé, ce qui, selon la théorie du compromis (Myers, 1977), limite l'intérêt de dettes supplémentaires.
- Préparer dès maintenant le remboursement de 2041 (trésorerie, refinancement) ; à défaut, le crédit-bail, plus cher de 0,09 point que l'emprunt classique après impôt, est la solution qui évite ce risque.

**Réponses tolérées** : recommandation du crédit-bail pour son amortissement progressif et l'absence de risque de refinancement, ou de l'emprunt classique pour sa simplicité et l'absence de coût de suivi, si elle est justifiée par les chiffres ; dette financière nette après le financement calculée en ajoutant 80,00 M€ si le candidat explique son hypothèse (le paiement des équipements étant déjà compris dans les 214,00 M€, 0,25 sur 0,75 à l'item 3.4-02) ; gearing exprimé en nombre (0,51 et 0,65).

**Erreurs fréquentes**
- Affirmer que le crédit-bail ne figure pas dans l'endettement : c'est faux dans les comptes consolidés en IFRS (annexe 3.3).
- Confondre prêt indexé (objectifs de l'emprunteur, fonds libres) et prêt vert ou obligation verte (fonds affectés à un projet).
- Juger le prêt indexé sur le seul gain de taux, sans le coût de la vérification ni le cas des objectifs manqués.
- `JUR-T05` et `JUR-T10` — traiter la durabilité sans chiffres, ou les chiffres sans la durabilité ; `JUR-T01` — recommandation sans posture de conseil ; `JUR-T02` — théories citées sans lien avec le cas.

---

### 3.5 Position de change, marché au comptant et à terme, vente à terme (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Position **longue** en CAD (créance de 8 000 000 CAD, aucune dette en CAD), **ouverte** (non couverte), à 180 jours ; risque de transaction : baisse du dollar canadien, soit une hausse du cours EUR/CAD au certain ; à 1,6800 : 4 761 905 € contre 5 000 000 € au comptant, perte de **238 095 €** | 0,75 |
| 3.5-02 | Marché au comptant (cours du jour, livraison immédiate) et à terme (cours fixé aujourd'hui pour une livraison à l'échéance, engagement ferme) ; cours à terme déterminé par la parité des taux d'intérêt ; report et déport | 0,5 |
| 3.5-03 | Cours à terme = 1,6000 × (1 + 2,30 % × 180/360) / (1 + 2,70 % × 180/360) = **1,5968** ; − 32 points : dollar canadien en report, euro en déport ; vente à terme : 8 000 000 / 1,5968 = **5 010 020 €** | 0,75 |

**Position de change (0,75 pt).** Le groupe détient une créance de 8 000 000 CAD encaissable le 28 novembre 2027, sans aucune dette ni dépense dans cette devise : sa position est **longue** en dollars canadiens et **ouverte**, puisqu'aucune opération ne la couvre (F07 § 3.1). Il s'agit d'un risque de transaction : le montant en euros de la redevance dépend du cours du 28 novembre. Le groupe craint une **baisse du dollar canadien**, c'est-à-dire, en cotation au certain, une **hausse** du cours EUR/CAD.
- Au comptant du jour : 8 000 000 / 1,6000 = **5 000 000 €** ;
- à 1,6800 : 8 000 000 / 1,6800 = **4 761 905 €**, soit une perte de **238 095 €** (4,76 %).

**Marché des changes au comptant et à terme (0,5 pt).**
- **Au comptant** : la devise est échangée au cours du jour, pour une livraison immédiate (en pratique deux jours ouvrés plus tard).
- **À terme** : la banque et le groupe fixent aujourd'hui le cours auquel ils échangeront un montant donné à une date future ; l'engagement est **ferme** pour les deux parties, quel que soit le cours à l'échéance, et ne coûte aucune prime.
- La banque se couvre en empruntant aujourd'hui des dollars canadiens, qu'elle convertit au comptant et place en euros jusqu'à l'échéance : le cours à terme dépend donc du cours comptant et de l'écart entre les taux d'intérêt des deux devises (**parité des taux d'intérêt**). La devise au taux le plus faible est en **report** (plus chère à terme qu'au comptant), celle au taux le plus élevé en **déport**.

**Cours à terme et vente à terme (0,75 pt).**
- Cours à terme = 1,6000 × (1 + 0,0230 × 180/360) / (1 + 0,0270 × 180/360) = 1,6000 × 1,0115 / 1,0135 = 1,596843, soit **1,5968** CAD pour 1 EUR.
- Points de terme : 1,5968 − 1,6000 = − 0,0032, soit **− 32 points** : il faut moins de dollars canadiens pour un euro à terme qu'au comptant ; le **dollar canadien est en report** et l'euro en déport, parce que le taux du dollar canadien (2,30 %) est inférieur à celui de l'euro (2,70 %).
- Vente à terme : 8 000 000 / 1,5968 = **5 010 020 €**, encaissés le 28 novembre 2027 quel que soit le cours. C'est 10 020 € de plus que la contre-valeur au comptant du jour : cet écart reflète le différentiel de taux, ce n'est ni un gain de change ni un coût de la couverture.

**Réponses tolérées** : position qualifiée de « créance en devise non couverte » avec le sens du risque ; perte exprimée par rapport au cours à terme (248 115 €) si le candidat le précise ; montant à terme de 5 009 886 € si le cours à terme n'est pas arrondi.

**Erreurs fréquentes**
- Qualifier la position de courte, ou dire que le groupe craint une hausse du dollar canadien.
- Inverser les taux dans la formule (cours à terme de 1,6032) ou utiliser une base de 365 jours.
- Multiplier le montant en dollars canadiens par le cours au lieu de le diviser (cotation au certain).
- `JUR-T13` — présenter le marché à terme en général, sans l'appliquer à la redevance.

---

### 3.6 Option de vente de devises, comparaison avec le terme (2,25 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Prime : 1,50 % × 8 000 000 = 120 000 CAD, soit **75 000 €** au comptant ; à 1,6800 (supérieur au prix d'exercice) : **exercice**, 8 000 000 / 1,6000 = 5 000 000 €, net de la prime **4 925 000 €** | 0,75 |
| 3.6-02 | À 1,5200 (inférieur au prix d'exercice) : **abandon**, vente au comptant 8 000 000 / 1,5200 = 5 263 158 €, net de la prime **5 188 158 €** | 0,5 |
| 3.6-03 | Cours d'indifférence : 8 000 000 / (5 010 020 + 75 000) = **1,5732** ; comparaison (coût, souplesse, risque résiduel) et recommandation : montant arrêté et certain, d'où une vente à terme | 1 |

**L'option et ses deux scénarios (1,25 pt).** L'option donne au groupe le **droit**, et non l'obligation, de vendre 8 000 000 CAD au cours de 1,6000 le 28 novembre 2027. La prime est fournie : 1,50 % × 8 000 000 = 120 000 CAD, soit 120 000 / 1,6000 = **75 000 €** payés le 1er juin 2027. Le prix d'exercice étant égal au cours comptant du jour, l'option est à la monnaie : sa valeur intrinsèque est nulle et la prime n'est que de la valeur temps (non exigé).

| Cours au 28/11/2027 | 1,6800 (baisse du CAD) | 1,5200 (hausse du CAD) |
|---|---:|---:|
| Décision | exercice (1,6800 > 1,6000) | abandon (1,5200 < 1,6000) |
| Euros reçus | 8 000 000 / 1,6000 = 5 000 000 | 8 000 000 / 1,5200 = 5 263 158 |
| − Prime | − 75 000 | − 75 000 |
| **Montant net de la prime** | **4 925 000** | **5 188 158** |
| Sans couverture | 4 761 905 | 5 263 158 |
| Vente à terme | 5 010 020 | 5 010 020 |

- À 1,6800, l'option protège : 4 925 000 € au lieu de 4 761 905 € sans couverture, mais 85 020 € de moins que la vente à terme.
- À 1,5200, l'option est abandonnée et le groupe profite de la hausse du dollar canadien : 5 188 158 €, soit 178 138 € de plus qu'à terme.

**Comparaison et recommandation (1 pt).**
- **Cours d'indifférence** : l'option procure plus d'euros que la vente à terme si 8 000 000 / cours − 75 000 > 5 010 020, soit pour un cours inférieur à 8 000 000 / 5 085 020 = **1,5732** (dollar canadien en hausse de plus de 1,7 % par rapport au comptant du jour). Au-dessus, la vente à terme est préférable.

| Critère | Vente à terme | Option de vente |
|---|---|---|
| Coût | aucune prime ; cours de 1,5968 connu dès aujourd'hui | prime de 75 000 €, payée d'avance et perdue dans tous les cas |
| Souplesse | engagement ferme : le groupe doit livrer 8 000 000 CAD, même si la redevance n'est pas versée à temps | droit, et non obligation : le groupe garde le gain si le dollar canadien monte, et n'est pas tenu de livrer |
| Risque résiduel | nul sur le cours ; le groupe renonce à tout gain de change | le plancher est de 4 925 000 €, inférieur de 85 020 € au montant garanti à terme |
| Simplicité | simple, sans décaissement | décision d'exercice à l'échéance ; prime à décaisser le 1er juin |

- **Recommandation** : le montant de la redevance est arrêté et l'université Aurelmont est un partenaire régulier : le groupe n'a pas besoin de la souplesse de l'option. La **vente à terme** garantit 5 010 020 €, sans prime, et supprime le risque de change. L'option ne se justifierait que si le montant ou la date d'encaissement étaient incertains, ou si la direction anticipait nettement une hausse du dollar canadien au-delà de 1,5732, ce qui relève de la spéculation et non de la couverture. Une couverture partielle (par exemple la moitié à terme, la moitié par option) est défendable si elle est justifiée.

**Réponses tolérées** : prime ajoutée au coût de la couverture sans coût de financement (convention de l'énoncé) ; option présentée comme « put CAD / call EUR » ; recommandation de l'option si le candidat la fonde sur une anticipation explicite de hausse du dollar canadien ou sur un risque de retard de paiement de l'université, en reconnaissant son coût (0,5 sur 1 à l'item 3.6-03, le cours d'indifférence restant noté).

**Erreurs fréquentes**
- Exercer l'option à 1,5200 (le groupe recevrait 5 000 000 € au lieu de 5 263 158 €) ou l'abandonner à 1,6800.
- Oublier la prime, ou la convertir au cours de l'échéance.
- Chercher à calculer la valeur de la prime par un modèle : elle est fournie (programme 6.3.d).
- Présenter l'option comme meilleure dans tous les cas parce qu'elle « laisse le gain » : son plancher est inférieur au cours à terme.
- `JUR-T01` — comparaison sans recommandation.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 80-81 ; programme l. 643-648 | VAN, TRI, indice de profitabilité, projets mutuellement exclusifs, lecture de la VAN comme création de valeur | [V] | F01 § 4 |
| Sujet 2025, dossier 1 ; rapport du jury 2025, p. 25 | deux projets exclusifs évalués par la VAN et le TRI, puis analyse de leur divergence (structure de la question 3.1) | [S] | F01 § 4.2 |
| Guide pédagogique DSCG, juillet 2026, p. 81-82 ; programme l. 653-666 | coût actuariel des financements avant et après impôt, crédit-bail, effet sur la structure financière, financements durables et prêts indexés sur la durabilité | [V] | F01 § 3 ; F08 § 5 |
| Principes de place des prêts indexés sur la durabilité (LMA) | indicateurs, objectifs, vérification, ajustement de marge | [S] | F08 § 5.1 et 5.3 |
| Guide pédagogique DSCG, juillet 2026, p. 78-79 ; programme l. 625-631 | position de change, marché au comptant et à terme, parité des taux d'intérêt, option de change à prime fournie, critères de choix (coût, souplesse, simplicité, risque résiduel) | [V] | F07 § 3 |
| Spence (1973) | signal coûteux et crédible (engagement de durabilité) | [V programme 4.1] | F10 § 3 |
| Myers et Majluf (1984) ; Myers (1977) | financement hiérarchique ; théorie du compromis et endettement cible | [V programme 7.2] | F10 § 3 |
| Freeman (1984) | parties prenantes (indicateur social du prêt) | [V programme 2.1] | F10 § 3 |
| CMPC de 8,00 %, cours EUR/CAD de 1,6000, taux à 180 jours de 2,70 % (euro) et 2,30 % (dollar canadien), prime de 1,50 % | hypothèses d'énoncé, plausibles fin 2026 ; taux de l'euro proche de l'Euribor de F11 | [S] | F11 |
| Projets, flux, valeurs résiduelles, offres de financement, indicateurs, structure financière prévisionnelle, redevance | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 3.1 à 3.4 |
