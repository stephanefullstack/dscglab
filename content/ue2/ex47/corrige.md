# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 47 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F02 coût du capital, F06 marchés et finance comportementale, F07 risques de taux, de change et trésorerie, F09 éthique, conformité et réglementation bancaire, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (CMPC, flux d'exploitation des scénarios central et fort, VAN, TRI, délai de récupération actualisé et flux actualisés, VAN des trois scénarios, espérance, écart-type, coefficient de variation et probabilité d'une VAN négative, valeur, duration, sensibilité et variation de valeur du prêt intragroupe, swap et cap dans trois scénarios, valeur intrinsèque et valeur temps de la prime, coûts actuariels avant et après IS, barème, liste noire, hors-programme ; flux du scénario faible, effet d'une hausse de l'Euribor, seuil entre swap et cap et coût de la marge sans lettre d'intention vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VAN calculée avec un CMPC erroné à la question 2.1).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Coût des fonds propres par le MEDAF et CMPC du projet | `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 1 |
| 2.2 Flux du scénario central, VAN, TRI et délai de récupération actualisé | `7.1.a` Évaluer et classer des projets en milieu certain | 2,5 |
| 2.3 VAN des trois scénarios, espérance, écart-type, probabilité d'une VAN négative, opportunité du projet | `7.1.b` Évaluer et classer des projets en milieu incertain | 1,5 |
| 2.4 Exposition au risque de taux, valeur, duration et sensibilité du prêt intragroupe, effet d'une baisse des taux | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 2 |
| 2.5 Swap à départ différé et cap dans trois scénarios d'Euribor, valeur intrinsèque et valeur temps de la prime | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux ; `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) | 3,5 |
| 2.6 Comparaison des couvertures et recommandation | `6.2.b` | 1 |
| 2.7 Coût actuariel du prêt bancaire couvert et du prêt de la holding, choix du financement | `7.2.a` Comparer les sources de financement et notamment leurs coûts | 2 |
| 2.8 Financement intermédié ou de marché, asymétrie d'information, lettre d'intention | `5.1.a` Appréhender le rôle des sources de financement et le rôle des banques dans l'économie réelle ; `5.1.b` Maîtriser les enseignements des asymétries d'information (Akerlof, 1970) | 2,5 |
| 2.9 Exigences de fonds propres des banques, notation interne, marge et garanties | `2.2.b` Mettre en œuvre la déontologie, la conformité et l'organisation déontologique (réglementation bancaire : principes du comité de Bâle) | 1 |
| **Total** | | **17** |

Part du calcul : environ 10 points (2.1-01, 2.2-01 à 2.2-03, 2.3-01, 2.3-02, 2.4-02, 2.4-03, 2.5-01 à 2.5-04, 2.7-01, 2.7-02 et la moitié de 2.4-01). Part de l'analyse : environ 7 points. Les questions 2.8 et 2.9, rédactionnelles, valent 3,5 points : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 2.1 Coût des fonds propres par le MEDAF et CMPC du projet (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Bêta réendetté = 0,84 × [1 + 0,75 × 40/60] = **1,26** ; ke = 4,0 % + 1,26 × 5,0 % = **10,30 %** ; kd net = 4,40 % × 0,75 = 3,30 % ; CMPC = 60 % × 10,30 % + 40 % × 3,30 % = **7,50 %** | 0,75 |
| 2.1-02 | Justification : les flux du projet sont des flux d'exploitation, avant frais financiers, qui reviennent à tous les apporteurs de fonds ; on les actualise au CMPC, qui reflète le risque de l'activité (bêta de l'actif des fabricants de verres) et la structure cible, pas le financement particulier du projet | 0,25 |

**Calcul (0,75 pt).** Le bêta de l'actif mesure le risque économique de l'activité de traitement de verres, sans effet de l'endettement (F02 § 3). On le réendette avec la structure cible du sous-groupe (relation de Hamada avec impôt, donnée par l'annexe 2.2) :
- dettes / capitaux propres = 40 / 60 = 0,6667 ;
- bêta des capitaux propres = 0,84 × (1 + 0,75 × 0,6667) = 0,84 × 1,50 = **1,26** ;
- coût des fonds propres (MEDAF) : ke = 4,0 % + 1,26 × 5,0 % = **10,30 %** ;
- coût de la dette après impôt : 4,40 % × (1 − 25 %) = **3,30 %** ;
- CMPC = 0,60 × 10,30 % + 0,40 × 3,30 % = 6,18 % + 1,32 % = **7,50 %**.

**Justification du taux (0,25 pt).** Les flux de l'annexe 2.1 sont des flux d'exploitation, calculés sans frais financiers : ils rémunèrent ensemble les actionnaires et les prêteurs. Le taux qui leur correspond est le coût moyen des deux ressources, pondéré par la structure cible, c'est-à-dire le CMPC (F02 § 5). Le coût des fonds propres de 10,30 % rémunère les seuls actionnaires : l'appliquer aux flux d'exploitation sous-estimerait la VAN. Le taux ne dépend pas du financement retenu pour ce projet (prêt de 6 000 k€ pour 8 400 k€ d'investissement) : la décision d'investissement est jugée sur le risque de l'activité, la décision de financement l'est séparément (questions 2.7 à 2.9). VERMONDAZ n'étant pas cotée, le risque du projet est mesuré par le bêta de l'actif d'entreprises cotées qui exercent la même activité que lui, le traitement de verres, distincte de la fabrication de montures.

**Réponses tolérées** : CMPC écrit avec les pondérations D/V et E/V sous forme fractionnaire ; ke de 10,30 % arrondi à 10,3 %.

**Erreurs fréquentes**
- Pondérer par D/E (0,6667) au lieu de D/V (40 %), ou réendetter le bêta avec D/V : bêta de 1,092 et ke de 9,46 %.
- Oublier l'économie d'impôt sur la dette (CMPC de 7,94 %).
- Actualiser les flux du projet au coût des fonds propres de 10,30 % (VAN de 183 k€ dans le scénario central au lieu de 1 024 k€, non exigée).
- `JUR-E02` — démarche bêta de l'actif, réendettement, MEDAF, CMPC mal enchaînée ; `JUR-T04` — acquis du DCG.

---

### 2.2 Flux du scénario central, VAN, TRI et délai de récupération actualisé (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Flux annuel : achats évités 2 600 + ventes 3 000 − coûts variables 2 250 − charges fixes 1 200 = EBE **2 150** ; dotations 1 400 ; résultat d'exploitation 750 ; IS 187,5 ; flux = **1 962,5 k€** par an ; année 6 = 1 962,5 + 500 + 600 = **3 062,5 k€** ; date 0 = − 8 400 − 500 = **− 8 900 k€** | 1 |
| 2.2-02 | VAN à 7,50 % = **1 024 k€** (1 025 avec les flux actualisés arrondis) ; TRI = **10,97 %** | 0,75 |
| 2.2-03 | Délai de récupération actualisé = 5 + 960 / 1 984 = **5,48 ans** | 0,5 |
| 2.2-04 | Conclusion : VAN positive, TRI supérieur au CMPC : le projet crée de la valeur dans le scénario central, mais la marge est mince : le délai approche la durée de vie du projet | 0,25 |

**Construction des flux (1 pt).** Pour VERMONDAZ, les achats de verres polarisés qu'elle ne fera plus à Bienne sont une économie de trésorerie : ils s'ajoutent aux ventes aux fabricants tiers (annexe 2.6). Les coûts variables portent sur toutes les paires produites, pour VERMONDAZ et pour les tiers.

| k€ | Calcul | Scénario central |
|---|---|---:|
| Achats évités à Bienne | 400 milliers de paires × 6,50 € | 2 600 |
| Ventes aux fabricants tiers | 500 × 6,00 € | 3 000 |
| Coûts variables | (400 + 500) × 2,50 € | − 2 250 |
| Charges fixes décaissées | | − 1 200 |
| **EBE** | | **2 150** |
| Dotations aux amortissements | 8 400 / 6 | − 1 400 |
| Résultat d'exploitation | | 750 |
| IS à 25 % | | − 187,5 |
| **Flux d'exploitation annuel** (EBE − IS) | | **1 962,5** |

| k€ | 31/12/2028 (0) | 2029 (1) | 2030 (2) | 2031 (3) | 2032 (4) | 2033 (5) | 2034 (6) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Investissement | − 8 400 | | | | | | |
| BFR constitué, puis récupéré | − 500 | | | | | | + 500 |
| Revente nette d'impôt (800 × 0,75) | | | | | | | + 600 |
| Flux d'exploitation | | 1 962,5 | 1 962,5 | 1 962,5 | 1 962,5 | 1 962,5 | 1 962,5 |
| **Flux du projet** | **− 8 900** | **1 962,5** | **1 962,5** | **1 962,5** | **1 962,5** | **1 962,5** | **3 062,5** |
| Coefficient d'actualisation à 7,50 % | 1 | 0,930233 | 0,865333 | 0,804961 | 0,748801 | 0,696559 | 0,647962 |
| Flux actualisés | − 8 900 | 1 826 | 1 698 | 1 580 | 1 470 | 1 367 | 1 984 |
| Cumul des flux actualisés | − 8 900 | − 7 074 | − 5 376 | − 3 796 | − 2 327 | − 960 | **+ 1 024** |

La ligne est entièrement amortie à la fin de 2034 : la plus-value de revente est égale au prix, soit 800 k€, imposée à 25 % ; le flux net est de 600 k€. La récupération du BFR n'est pas imposée.

**VAN et TRI (0,75 pt).**
- VAN = 1 962,5 × [1 − 1,075^−6] / 0,075 + 1 100 × 1,075^−6 − 8 900 = 1 962,5 × 4,693846 + 1 100 × 0,647962 − 8 900 = 9 211,67 + 712,76 − 8 900 = **1 024 k€**.
- TRI : taux qui annule la VAN ; par interpolation entre 10 % (VAN = 268 k€, non exigé) et 11 % (VAN = − 9 k€) : **TRI = 10,97 %**, supérieur au CMPC de 7,50 %.

**Délai de récupération actualisé (0,5 pt).** Le cumul des flux actualisés devient positif au cours de la sixième année : 5 + 960 / 1 984 = **5,48 ans**, soit environ cinq ans et six mois après la mise en service.

**Conclusion (0,25 pt).** Dans le scénario central, le projet crée 1 024 k€ de valeur pour VERMONDAZ (indice de profitabilité de 1,12, non exigé) et son TRI dépasse le CMPC de près de 3,5 points. Mais l'investissement n'est récupéré qu'au cours de la dernière année. Sans la récupération du BFR ni la revente de la ligne, la VAN tomberait à 312 k€ (non exigé) : la rentabilité dépend fortement de la tenue des volumes jusqu'en 2034, ce qu'étudie la question 2.3.

**Réponses tolérées** : VAN de 1 025 k€ obtenue en additionnant les flux actualisés arrondis ; TRI de 10,96 % à 10,98 % selon l'interpolation ; cumuls à 1 k€ près selon l'arrondi des flux actualisés ; délai de 5,48 ans calculé avec les montants non arrondis ; délai exprimé en années et en mois (5 ans et 6 mois) ; flux annuels arrondis à 1 963 k€ si la VAN reste comprise entre 1 024 et 1 027 k€.

**Erreurs fréquentes**
- Oublier les achats évités à Bienne, qui sont le premier avantage du projet (flux annuel de 12,5 k€ et VAN fortement négative).
- Calculer les coûts variables sur les seules ventes aux tiers (500 × 2,50) et oublier la production destinée à VERMONDAZ.
- Déduire les frais financiers du prêt des flux : ils sont dans le CMPC.
- Imposer la récupération du BFR, ou retenir la revente de 800 k€ avant impôt.
- `JUR-T04` — VAN et TRI sont des acquis du DCG ; `JUR-T07` — absence de tableau des flux.

---

### 2.3 VAN des trois scénarios, espérance, écart-type, probabilité d'une VAN négative, opportunité du projet (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Flux annuels : faible 1 175 (EBE 1 100, résultat d'exploitation − 300, économie d'impôt 75) ; fort 2 750 (EBE 3 200, IS 450) ; VAN faible = **− 2 672 k€** ; VAN fort = **4 721 k€** | 0,5 |
| 2.3-02 | Espérance de la VAN = 0,30 × (− 2 672) + 0,50 × 1 024 + 0,20 × 4 721 = **655 k€** ; écart-type = **2 587 k€** ; coefficient de variation = **3,95** ; probabilité d'une VAN négative = **30 %** | 0,5 |
| 2.3-03 | Conclusion : espérance positive, mais inférieure à la VAN centrale et très dispersée ; trois chances sur dix de détruire 2,7 M€ ; risque porté par les ventes aux tiers (VAN nulle vers 417 milliers de paires, non exigé) ; recommandation : investir sous condition d'engagements de fabricants clients, ou différer | 0,5 |

**VAN des scénarios (0,5 pt).** Seules les ventes aux fabricants tiers changent d'un scénario à l'autre.

| k€ | Faible | Central | Fort |
|---|---:|---:|---:|
| Achats évités | 2 600 | 2 600 | 2 600 |
| Ventes aux tiers (6,00 €) | 1 200 | 3 000 | 4 800 |
| Coûts variables (2,50 €) | − 1 500 | − 2 250 | − 3 000 |
| Charges fixes | − 1 200 | − 1 200 | − 1 200 |
| EBE | 1 100 | 2 150 | 3 200 |
| Résultat d'exploitation (EBE − 1 400) | − 300 | 750 | 1 800 |
| IS (économie d'impôt si négatif) | + 75 | − 187,5 | − 450 |
| Flux annuel | 1 175 | 1 962,5 | 2 750 |
| VAN à 7,50 % | **− 2 672** | **1 024** | **4 721** |

Calcul rapide : 300 milliers de paires de plus ou de moins changent le flux annuel de 300 × (6,00 − 2,50) × 0,75 = 787,5 k€, donc la VAN de 787,5 × 4,693846 = 3 696 k€. VAN faible = 1 024 − 3 696 = − 2 672 k€ ; VAN fort = 1 024 + 3 696 = 4 721 k€ (arrondis). Dans le scénario faible, le résultat d'exploitation négatif de la ligne procure une économie d'impôt de 75 k€, imputée sur les autres bénéfices de VERMONDAZ (annexe 2.6).

**Espérance et risque (0,5 pt).** Variance calculée avec les probabilités des scénarios (annexe 2.6) :

| Scénario | Probabilité | VAN (k€) | Probabilité × VAN | Écart à l'espérance | Probabilité × écart² |
|---|---:|---:|---:|---:|---:|
| Faible | 0,30 | − 2 672 | − 801,6 | − 3 327 | 3 320 679 |
| Central | 0,50 | 1 024 | 512,0 | 369 | 68 081 |
| Fort | 0,20 | 4 721 | 944,2 | 4 066 | 3 306 471 |
| **Total** | 1,00 | | **E(VAN) = 655** | | **Variance = 6 695 231** |

Écart-type = √6 695 231 ≈ 2 588 avec les VAN arrondies du tableau ; **2 587 k€** avec les VAN non arrondies ; coefficient de variation = 2 587 / 655 = **3,95** ; probabilité d'une VAN négative, lue sur les scénarios : celle du seul scénario faible, **30 %**.

**Conclusion sur l'opportunité du projet (0,5 pt).**
- L'espérance de la VAN est positive (655 k€) : selon le critère de l'espérance, le projet est acceptable. Elle est inférieure à la VAN du scénario central, parce que le scénario défavorable est plus probable (30 %) que le scénario favorable (20 %).
- Le risque est élevé : l'écart-type vaut près de quatre fois l'espérance, et VERMONDAZ a trois chances sur dix de perdre 2,7 M€ de valeur, soit près d'un tiers de l'investissement.
- Le risque ne vient pas des achats évités, certains, mais des ventes aux fabricants tiers : la VAN s'annule pour environ 417 milliers de paires vendues par an, à peine 17 % sous le volume central de 500. Sans aucune vente aux tiers, la VAN serait d'environ − 5,1 M€ (non exigé) : les seules économies sur les achats à Bienne ne justifient pas la ligne.
- Recommandation : présenter le projet à la holding comme créateur de valeur en espérance, mais conditionner la décision à des engagements d'achat de fabricants de la région (contrats pluriannuels, lettres de commande) qui rendent le scénario faible moins probable ; à défaut, attendre ces engagements avant de commander les équipements.

**Réponses tolérées** : écart-type de 2 587 ou 2 588 k€ selon les arrondis ; coefficient de variation de 3,95 ou 3,96 ; conclusion inverse (refuser ou différer le projet) si elle s'appuie sur la dispersion des résultats et sur l'aversion au risque de la holding ; mention du point de vue du groupe (marge de l'usine de Bienne), si le candidat note que la holding a réaffecté la capacité libérée.

**Erreurs fréquentes**
- Calculer une moyenne simple des trois VAN (1 024 k€) au lieu de l'espérance pondérée par les probabilités.
- Appliquer l'impôt de 25 % au résultat négatif du scénario faible comme une charge (flux de 1 025 k€ au lieu de 1 175 k€).
- Calculer une probabilité de VAN négative à partir d'une distribution continue : elle se lit sur les scénarios.
- `JUR-T13` — conclusion sans lien avec les données du cas ; `JUR-T07` — absence de tableau.

---

### 2.4 Exposition au risque de taux, valeur, duration et sensibilité du prêt intragroupe, effet d'une baisse des taux (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Prêt bancaire à taux variable tiré le 30/06/2028 : risque sur les flux d'intérêts (hausse de l'Euribor d'ici le tirage et pendant six ans) ; + 1 point → **60 k€** de plus la première année avant IS, **45 k€** après IS ; prêt intragroupe à taux fixe : charge d'intérêts certaine, mais risque de valeur et coût d'opportunité si les taux baissent | 0,5 |
| 2.4-02 | Valeur au 30/06/2028 au taux de marché de 4,40 % = **6 000 k€** (taux du prêt = taux de marché) ; duration = **4,596 ans** ; sensibilité = − 4,596 / 1,044 = **− 4,402** | 0,75 |
| 2.4-03 | Baisse d'un point : variation estimée = − 4,402 × (− 1 %) × 6 000 = **+ 264 k€** ; valeur exacte à 3,40 % = **6 272 k€**, soit **+ 272 k€** ; interprétation : la valeur de la dette augmente quand les taux baissent ; VERMONDAZ paie 4,40 % au lieu de 3,40 % pendant cinq ans sans pouvoir rembourser par anticipation : coût d'opportunité de 272 k€ en valeur actuelle | 0,75 |

**Diagnostic de l'exposition (0,5 pt).**
- **Prêt de la Banque SAVERDINE (taux variable)** : la charge d'intérêts suit l'Euribor 3 mois, constaté chaque trimestre pendant six ans. VERMONDAZ craint la **hausse** des taux, dès aujourd'hui : la marge est fixée à la signature (juin 2027), mais l'Euribor du premier trimestre ne sera connu que le 30 juin 2028, dans plus de quatorze mois. C'est un risque sur les **flux** (le budget retient 4,50 % au plus), pas sur la valeur de la dette, qui reste proche du capital dû puisque le taux s'ajuste. Une hausse d'un point de l'Euribor augmenterait les intérêts de la première année de 6 000 × 1 % = **60 k€** avant impôt, **45 k€** après impôt ; l'effet diminue ensuite avec l'amortissement.
- **Prêt d'ALDENWYL Holding SA (taux fixe)** : la charge d'intérêts est certaine, 264 k€ par an. Le risque est inverse : si les taux **baissent**, VERMONDAZ continue de payer 4,40 % alors que le marché prête moins cher, et elle ne peut pas rembourser par anticipation. C'est un risque de **valeur** de la dette, mesuré par la duration et la sensibilité.

**Valeur, duration et sensibilité (0,75 pt).** Au 30 juin 2028, le prêt verse 264 k€ d'intérêts (6 000 × 4,40 %) à la fin de chaque année et 6 000 k€ à la fin de la cinquième année.

| Année | Flux (k€) | Facteur à 4,40 % | Flux actualisé | t × flux actualisé |
|---:|---:|---:|---:|---:|
| 1 | 264 | 0,957854 | 252,87 | 252,87 |
| 2 | 264 | 0,917485 | 242,22 | 484,43 |
| 3 | 264 | 0,878817 | 232,01 | 696,02 |
| 4 | 264 | 0,841779 | 222,23 | 888,92 |
| 5 | 6 264 | 0,806302 | 5 050,67 | 25 253,37 |
| **Total** | | | **6 000** | **27 575,61** |

- Valeur = **6 000 k€** : au taux de marché égal au taux du prêt, la dette vaut son nominal.
- Duration = 27 575,61 / 6 000 = **4,596 ans** : la dette in fine a une duration proche de sa durée, car l'essentiel du flux est payé au terme.
- Sensibilité = − 4,596 / 1,044 = **− 4,402** : une variation de 1 point du taux de marché fait varier la valeur de la dette d'environ 4,40 % en sens inverse.

**Baisse d'un point et interprétation (0,75 pt).**
- Variation estimée par la sensibilité : − 4,402 × (− 0,01) × 6 000 = **+ 264 k€**.
- Valeur exacte au taux de 3,40 % : 264 × [1 − 1,034^−5] / 0,034 + 6 000 × 1,034^−5 = **6 272 k€**, soit **+ 272 k€**. L'écart de 8 k€ avec l'estimation vient de la courbure de la relation valeur-taux : la sensibilité n'en donne qu'une approximation linéaire.
- Interprétation : la valeur d'une dette à taux fixe varie en sens inverse des taux. Pour un prêteur, la hausse de valeur serait un gain ; pour l'**emprunteur**, c'est une perte : VERMONDAZ doit des flux qui valent désormais 6 272 k€ pour un capital de 6 000 k€. Elle paie 1 point de plus que le marché pendant cinq ans (60 k€ par an) sans pouvoir rembourser par anticipation : la valeur actuelle de ce surcoût, 272 k€, est son **coût d'opportunité**. Symétriquement, une hausse des taux lui serait favorable. Le taux fixe supprime le risque de flux mais crée un risque de valeur ; le prêt bancaire couvert par le swap aurait la même exposition, puisque le swap fixe aussi le taux (question 2.6).

**Réponses tolérées** : duration calculée par la formule d'une obligation au pair ; variation estimée de 264,13 k€ ; valeur exacte de 6 271,67 k€ ; interprétation en termes de « perte latente » ou de « manque à gagner » pour l'emprunteur.

**Erreurs fréquentes**
- Écrire que la baisse des taux est favorable à VERMONDAZ parce que « la valeur du prêt augmente » : c'est la valeur de sa dette qui augmente.
- Sensibilité écrite positive, ou égale à la duration.
- Confondre le risque de flux du taux variable et le risque de valeur du taux fixe.
- `JUR-T12` — réponse superficielle sur la relation valeur-taux ; `JUR-T13` — absence de lien avec le cas (budget de 4,50 %, absence de remboursement anticipé).

---

### 2.5 Swap à départ différé et cap dans trois scénarios d'Euribor, valeur intrinsèque et valeur temps de la prime (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Intérêts du prêt sans couverture, aux taux de 5,20 %, 4,20 % et 3,20 % : **78 000 €**, **63 000 €**, **48 000 €** (6 000 000 × (Euribor + 1,40 %) × 90 / 360) | 0,5 |
| 2.5-02 | Swap : différentiel **+ 12 000**, **− 3 000**, **− 18 000 €** ; coût net **66 000 €** et taux effectif **4,40 %** dans les trois scénarios | 1 |
| 2.5-03 | Cap : versement **8 250 €** à 3,80 %, nul sinon ; prime **3 750 €** ; coût net **73 500 €** (**4,90 %**), **66 750 €** (**4,45 %**), **51 750 €** (**3,45 %**) | 1 |
| 2.5-04 | Valeur intrinsèque au 15/04/2027 = 6 000 000 × max (0 ; 2,40 % − 3,25 %) × 90 / 360 = **0** (cap hors de la monnaie) ; valeur temps = **3 750 €** | 0,5 |
| 2.5-05 | Signification : valeur intrinsèque = gain d'un exercice immédiat ; valeur temps = prix de la possibilité que l'Euribor dépasse 3,25 % d'ici le 31/12/2028 (vingt mois et demi, volatilité des taux, taux à terme supérieurs au taux du jour) ; elle diminue à l'approche de l'échéance | 0,5 |

**Conventions.** Période du 31 décembre 2028 au 31 mars 2029 : 90 jours, base Exact/360, nominal 6 000 000 € (premier amortissement le 30 juin 2029). 6 000 000 × 90 / 360 = 1 500 000 € : chaque point de taux annuel vaut 15 000 € sur la période.

**Intérêts sans couverture, swap et cap (2,5 pts).**

| Euribor constaté le 31/12/2028 | 3,80 % | 2,80 % | 1,80 % |
|---|---:|---:|---:|
| Intérêts du prêt (Euribor + 1,40 %) | 78 000 | 63 000 | 48 000 |
| *Taux sans couverture* | *5,20 %* | *4,20 %* | *3,20 %* |
| **Swap** : différentiel = 1 500 000 × (Euribor − 3,00 %) | + 12 000 reçu | − 3 000 versé | − 18 000 versé |
| Coût net avec le swap | **66 000** | **66 000** | **66 000** |
| Taux effectif avec le swap | **4,40 %** | **4,40 %** | **4,40 %** |
| **Cap** : versement = 1 500 000 × max (0 ; Euribor − 3,25 %) | 8 250 | 0 | 0 |
| Prime de la période = 1 500 000 × 0,25 % | 3 750 | 3 750 | 3 750 |
| Coût net avec le cap (intérêts − versement + prime) | **73 500** | **66 750** | **51 750** |
| Taux effectif avec le cap | **4,90 %** | **4,45 %** | **3,45 %** |

Montants en euros. Lecture :
- **Swap** : VERMONDAZ paie 3,00 % et reçoit l'Euribor ; combiné au prêt, son coût est figé à 3,00 % + 1,40 % = **4,40 %** quel que soit l'Euribor. Ce taux respecte le budget de 4,50 %. Quand l'Euribor baisse à 1,80 %, elle verse 18 000 € et ne profite pas de la baisse.
- **Cap** : le coût est plafonné à 3,25 % + 1,40 % + 0,25 % = **4,90 %**, au-dessus du budget ; sous le prix d'exercice, VERMONDAZ paie le taux constaté majoré de la marge (1,40 %) et de la prime (0,25 %), et profite de la baisse (3,45 % à 1,80 %).

**Valeur intrinsèque et valeur temps (1 pt).**
- Prime de la période : 6 000 000 × 0,25 % × 90 / 360 = **3 750 €**.
- Valeur intrinsèque au 15 avril 2027 : ce que rapporterait un exercice immédiat, avec l'Euribor du jour : 6 000 000 × max (0 ; 2,40 % − 3,25 %) × 90 / 360 = **0**. Le cap est **hors de la monnaie** : l'Euribor du jour est inférieur au prix d'exercice.
- Valeur temps = 3 750 − 0 = **3 750 €** : toute la prime est de la valeur temps (dite aussi valeur spéculative). Elle rémunère la banque pour la possibilité que l'Euribor dépasse 3,25 % le 31 décembre 2028, dans vingt mois et demi : plus l'échéance est lointaine et plus les taux sont volatils, plus cette possibilité vaut cher. Ici, les taux à terme du marché sont supérieurs au taux du jour (le taux fixe du swap à départ différé, 3,00 %, dépasse l'Euribor du jour de 2,40 %) : le marché anticipe une hausse, ce qui rapproche le cap de la monnaie. La valeur temps diminue à mesure que l'on approche de la date de constatation et devient nulle à cette date, où la prime ne vaut plus que sa valeur intrinsèque. La prime est donnée par la banque ; aucun modèle ne sert à la calculer.

**Réponses tolérées** : taux effectifs calculés directement en points (Euribor + marge − différentiel) ; valeur intrinsèque appréciée par rapport au taux à terme implicite de 3,00 %, si le candidat le justifie (elle reste nulle) ; prime totale de la durée du cap décomposée qualitativement.

**Erreurs fréquentes**
- Inverser le sens du différentiel du swap (VERMONDAZ, payeuse du fixe, reçoit quand l'Euribor dépasse 3,00 %).
- Oublier la prime dans le coût net du cap, ou l'ajouter seulement quand le cap est exercé.
- Calculer les intérêts en base 365 (76 932 € au lieu de 78 000 € à 3,80 %) alors que l'annexe impose Exact/360.
- Prendre l'Euribor du 31/12/2028 pour la valeur intrinsèque au 15/04/2027.
- `JUR-T07` — absence de tableau par scénario ; `JUR-T12` — valeur temps confondue avec le coût de portage.

---

### 2.6 Comparaison des couvertures et recommandation (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Comparaison : coût (swap sans prime, cap 0,25 % l'an ; le cap n'est moins cher que le swap que si l'Euribor est inférieur à 2,75 %), flexibilité (swap ferme, cap qui laisse profiter de la baisse), risque résiduel (aucun avec le swap mais un coût d'opportunité ; avec le cap, taux plafond de 4,90 % au-dessus du budget de 4,50 %), engagement avant le tirage (swap à dénouer à sa valeur de marché, éventuellement négative ; cap résiliable pour 5 000 €) ; instruments de gré à gré | 0,5 |
| 2.6-02 | Recommandation argumentée : si le prêt bancaire est retenu et le projet décidé, le swap, seul compatible avec le budget de 4,50 %, conclu seulement quand la décision d'investir et le choix du financement sont acquis ; le cap si la direction veut garder la baisse ou si le tirage reste incertain | 0,5 |

**Comparaison (0,5 pt).**

| Critère | Swap payeur du taux fixe à départ différé | Cap |
|---|---|---|
| Coût | aucune prime ; coût figé à 4,40 % | prime de 0,25 % l'an (3 750 € par trimestre au départ) ; seuil de 3,00 % − 0,25 % = **2,75 %** d'Euribor : en dessous seulement, le cap est moins cher que le swap |
| Protection contre la hausse | totale : 4,40 % | plafond de 4,90 %, au-dessus du budget de 4,50 % |
| Flexibilité | aucune : VERMONDAZ paie 4,40 % même si l'Euribor tombe à 1,80 % (coût d'opportunité de 14 250 € par rapport au cap sur la période) | garde le bénéfice d'une baisse (3,45 % à 1,80 %) |
| Risque résiduel | aucun sur les flux ; risque de valeur (comme le prêt à taux fixe de la question 2.4) ; risque de contrepartie sur la banque quand le différentiel est reçu | Euribor entre 2,40 % et 3,25 % non couvert, prime perdue si les taux baissent ; risque de contrepartie |
| Engagement avant le tirage | ferme dès juin 2027 : si le projet est retardé ou si la holding prête à la place de la banque, le swap reste dû ou doit être dénoué à sa valeur de marché, que VERMONDAZ paie si les taux ont baissé | VERMONDAZ peut renoncer au cap avant son départ pour 5 000 € : perte maximale connue d'avance |

Les deux instruments sont négociés de gré à gré avec la banque prêteuse : ils épousent le nominal amortissable et les dates du prêt, sans dépôt de garantie, mais ils exposent VERMONDAZ au risque de contrepartie et sont moins liquides qu'un instrument standardisé.

**Recommandation (0,5 pt).** Si VERMONDAZ retient le prêt de la Banque SAVERDINE, le **swap à départ différé** est la couverture adaptée : il fixe le coût à 4,40 %, dans le budget du projet, sans prime, et le projet, dont la VAN est sensible aux volumes (question 2.3), n'a pas besoin d'un second aléa sur les frais financiers. Le cap protège mal : son plafond de 4,90 % dépasse le budget. Le swap engage toutefois VERMONDAZ un an avant le tirage : il ne doit être signé qu'avec le prêt, une fois la décision d'investir prise par la holding et le choix entre la banque et la holding arrêté (question 2.7). Tant que ces décisions ne sont pas prises, ou si la direction anticipe une baisse des taux, le cap est préférable : sa perte maximale est connue (indemnité de 5 000 € ou primes).

**Réponses tolérées** : recommandation du cap, si elle est justifiée par l'incertitude sur le tirage, par une anticipation de baisse des taux et par l'acceptation d'un dépassement possible du budget ; mention d'un tunnel ou d'une couverture partielle, si elle reste un prolongement de la comparaison.

**Erreurs fréquentes**
- Recommander le cap au seul motif qu'il est le moins cher dans un scénario.
- Ignorer l'engagement pris avant le tirage, propre au départ différé.
- `JUR-T01` — absence de recommandation au dirigeant ; `JUR-T13` — critères génériques sans les chiffres du cas.

---

### 2.7 Coût actuariel du prêt bancaire couvert et du prêt de la holding, choix du financement (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Prêt bancaire couvert : flux après IS 5 977,5 ; − 1 198 ; − 1 165 ; − 1 132 ; − 1 099 ; − 1 066 ; − 1 033 → **3,42 %** (4,56 % avant IS, non exigé) | 0,75 |
| 2.7-02 | Prêt d'ALDENWYL Holding SA : flux après IS 6 000 ; − 198 pendant quatre ans ; − 6 198 → **3,30 %** | 0,25 |
| 2.7-03 | Comparaison qualitative : écart de coût faible (0,12 point après IS) dû aux seuls frais ; prêt in fine à cinq ans contre amortissement aligné sur les six ans du projet (6 000 k€ à rembourser en 2033) ; garanties et engagements (lettre d'intention, distribution limitée à 50 %) ; couverture nécessaire ; dépendance envers la holding et trésorerie immobilisée du groupe ; relation bancaire propre de VERMONDAZ | 0,5 |
| 2.7-04 | Recommandation argumentée (prêt de la holding, le moins cher et sans asymétrie d'information, à condition de préparer le remboursement de 2033 ; ou prêt bancaire couvert, si l'adossement et l'autonomie bancaire priment) | 0,5 |

**Coûts actuariels (1 pt).** Échéances annuelles au 30 juin, date 0 au versement des fonds (annexe 2.6) ; k€.

Prêt de la Banque SAVERDINE couvert par le swap (taux fixe effectif de 4,40 % sur le capital restant dû, amortissement de 1 000 par an, frais de 30) :

| Année | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Capital restant dû en début d'année | | 6 000 | 5 000 | 4 000 | 3 000 | 2 000 | 1 000 |
| Intérêts (4,40 %) | | 264 | 220 | 176 | 132 | 88 | 44 |
| Flux avant IS (6 000 − 30, puis intérêts + 1 000) | 5 970 | − 1 264 | − 1 220 | − 1 176 | − 1 132 | − 1 088 | − 1 044 |
| Économie d'IS (25 % des frais, puis des intérêts) | + 7,5 | + 66 | + 55 | + 44 | + 33 | + 22 | + 11 |
| Flux après IS | 5 977,5 | − 1 198 | − 1 165 | − 1 132 | − 1 099 | − 1 066 | − 1 033 |

Taux qui annule la valeur actuelle des flux après IS : **3,42 %** (avant IS : 4,56 %, non exigé).

Prêt d'ALDENWYL Holding SA (in fine, sans frais) : flux avant IS 6 000 ; − 264 pendant quatre ans ; − 6 264 → **4,40 %** ; après IS : 6 000 ; − 198 pendant quatre ans ; − 6 198 → 4,40 % × 0,75 = **3,30 %**.

**Comparaison (0,5 pt).**
- **Coût** : le prêt de la holding est le moins cher, de 0,16 point avant IS et de 0,12 point après IS. Les deux prêts portent le même taux, 4,40 %, celui du marché pour le risque de VERMONDAZ : l'écart vient des seuls frais de dossier (30 k€, 22,5 k€ après IS). Sans lettre d'intention, la marge bancaire serait de 1,90 % et l'écart bien plus large (question 2.9).
- **Adéquation au projet** : le prêt bancaire s'amortit sur six ans, au rythme des flux de la ligne (1 962,5 k€ par an dans le scénario central) ; le prêt de la holding impose de rembourser 6 000 k€ en une fois le 30 juin 2033, un an avant la fin de l'exploitation : VERMONDAZ devra accumuler la trésorerie ou se refinancer, et ce risque est le plus fort dans le scénario faible.
- **Garanties et contraintes** : la banque exige la lettre d'intention de la holding, les comptes de la holding et la limitation des dividendes à 50 % du résultat ; elle impose de couvrir le taux (swap ou cap). La holding ne demande aucune garantie et son taux est fixe d'emblée.
- **Dépendance et ressources du groupe** : le prêt intragroupe immobilise 6 000 k€ de trésorerie de la holding pendant cinq ans et accroît la dépendance de VERMONDAZ envers sa maison mère ; le prêt bancaire donne à la filiale une relation et une histoire de crédit propres, utiles pour ses besoins futurs, et garde la trésorerie du groupe pour les autres sociétés.

**Recommandation (0,5 pt).** Le prêt d'ALDENWYL Holding SA est le moins cher et le plus simple : pas de frais, pas de couverture à négocier, pas de garantie. Il illustre l'avantage d'un financement interne au groupe : la holding connaît sa filiale et n'a pas à se protéger contre l'asymétrie d'information que la banque fait payer (question 2.8). La recommandation est de le retenir, en demandant à la holding un amortissement ou une échéance alignés sur la durée de la ligne (2034), et en préparant dès 2029 le remboursement de 2033 ; VERMONDAZ conserve la Banque SAVERDINE pour ses financements courants. Si la holding ne peut pas immobiliser 6 000 k€ pendant cinq ans, le prêt bancaire couvert par le swap reste une solution proche en coût (3,42 % après IS), mieux adaptée au profil du projet.

**Réponses tolérées** : recommandation du prêt bancaire couvert, si elle s'appuie sur l'adossement aux flux, sur l'autonomie de la filiale et sur la préservation de la trésorerie du groupe ; coût après IS du prêt bancaire calculé avec une économie d'impôt sur les frais étalée sur six ans (3,42 % également), si l'hypothèse est écrite ; comparaison exprimée en k€ d'écart de coût.

**Erreurs fréquentes**
- Comparer les taux nominaux (4,40 % et 4,40 %) sans les frais.
- Calculer le coût après IS en appliquant (1 − 25 %) au taux avant IS frais compris (3,42 % est ici proche, mais la démarche n'est pas actuarielle).
- Analyser le régime juridique de la lettre d'intention ou les règles d'impôt propres aux prêts intragroupe (UE 1) : le dossier les traite sous l'angle financier.
- `JUR-I01` — tableau d'amortissement faux (intérêts calculés sur le capital initial chaque année) ; `JUR-T01` — absence de recommandation.

---

### 2.8 Financement intermédié ou de marché, asymétrie d'information, lettre d'intention (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.8-01 | Financement de marché (placement privé obligataire) : relation directe avec des investisseurs, taille minimale (20 M€), information publique et régulière, notation, frais fixes (180 k€, soit 3 % de 6 M€) ; financement intermédié : la banque collecte l'information privée, suit l'emprunteur dans la durée, porte le risque de crédit et fixe des clauses ; pour une filiale non cotée et non notée, avec un besoin de 6 M€, la banque est la voie adaptée | 1 |
| 2.8-02 | Akerlof (1970) : asymétrie d'information, sélection adverse (une marge moyenne fait fuir les bons emprunteurs et attire les mauvais), d'où rationnement ou surcoût ; appliquée au cas : comptes de VERMONDAZ dépendant de décisions du groupe que la banque n'observe pas (prix des achats à Bienne, dividendes, répartition des fabrications), holding non notée qui ne publie pas ses comptes, intentions inconnues ; réponses de la banque : note de 6, marge plus élevée, garanties, information exigée, limite des dividendes | 1 |
| 2.8-03 | Lettre d'intention : la holding, mieux informée, déclare son soutien et son maintien au capital ; elle réduit l'asymétrie et le risque perçu (note 6 → 4) ; marge 1,90 % → 1,40 % (30 k€ la première année et 105 k€ sur six ans, non exigés) et pas de nantissement ; pour la holding, un engagement de soutien qu'elle doit pouvoir tenir | 0,5 |

**Financement intermédié ou de marché (1 pt).**
- Le **financement de marché** (ou direct) met l'entreprise en relation avec des investisseurs : actions, obligations, placement privé obligataire. Il suppose une **taille** suffisante, une **information** publique et régulière, souvent une notation par une agence, et des **coûts fixes** de mise en place élevés (guide p. 72 ; F06). La Banque SAVERDINE l'écrit : les investisseurs ne souscrivent pas moins de 20 M€, exigent une documentation complète et une information régulière, et les frais fixes avoisinent 180 k€, soit 3 % d'un emprunt de 6 M€ (près de 0,6 point par an de coût actuariel).
- Le **financement intermédié** (ou indirect) passe par une banque, qui collecte des dépôts et prête. Elle **produit de l'information privée** sur l'emprunteur, qu'elle connaît depuis longtemps, le **suit dans la durée**, porte le **risque de crédit** et l'encadre par des clauses (garanties, limitation des dividendes, information annuelle).
- En l'espèce, VERMONDAZ est une filiale non cotée et non notée, de 54 M€ de chiffre d'affaires, qui cherche 6 M€ : son besoin est plus de trois fois inférieur au minimum d'un placement privé, et elle ne publie pas l'information que demanderaient des investisseurs. Le financement intermédié, par la banque ou par la holding, qui joue ici le rôle d'un intermédiaire interne au groupe, est la voie adaptée.

**Asymétrie d'information (1 pt).**
- Selon **Akerlof (1970)**, quand le vendeur connaît mieux la qualité de son bien que l'acheteur, celui-ci offre un prix moyen ; les bons produits quittent le marché, la qualité moyenne baisse et le marché peut disparaître : c'est la **sélection adverse** (F10). Transposée au crédit : la banque connaît mal le risque de l'emprunteur ; si elle applique à tous une marge moyenne, les emprunteurs sûrs la trouvent trop chère et vont ailleurs, les plus risqués restent ; elle relève alors ses marges ou rationne le crédit.
- En l'espèce, l'asymétrie est renforcée par l'appartenance à un groupe étranger : les comptes de VERMONDAZ **dépendent de décisions du groupe** que la banque n'observe pas (prix de ses achats à l'usine de Bienne, dividendes remontés à la holding, répartition des fabrications entre les sociétés). La rentabilité de la filiale peut donc être modifiée par la holding, et la trésorerie qu'elle génère peut remonter en Suisse au détriment du prêteur. ALDENWYL Holding SA n'est pas notée, ne publie pas ses comptes, et ses intentions à long terme envers sa filiale française sont inconnues.
- La banque y répond par des **mécanismes de réduction de l'asymétrie** : une notation interne prudente (6 sur 10), une marge plus élevée et un nantissement des équipements sans soutien de la holding, la communication des comptes de la holding et l'engagement de ne pas distribuer plus de 50 % du résultat, qui limite la remontée de trésorerie pendant la durée du prêt.

**Rôle de la lettre d'intention (0,5 pt).** La lettre d'intention est un engagement de la partie la mieux informée, la holding, qui déclare soutenir sa filiale pendant la durée du prêt et conserver sa participation. Elle rend crédible, pour la banque, le soutien du groupe, et transfère une partie du risque perçu de la filiale vers la holding : la note passe de 6 à 4, la marge de 1,90 % à 1,40 % et le nantissement disparaît. Sur le prêt de 6 000 k€, l'écart de marge de 0,50 point représente 30 k€ d'intérêts la première année et 105 k€ sur six ans (capitaux restant dus de 6 000 à 1 000 k€). Pour la holding, ce soutien n'est pas gratuit : elle engage sa réputation et sa capacité à soutenir la filiale en cas de difficulté ; la lettre montre aussi que le crédit bancaire repose en partie sur la holding, ce qui relativise l'avantage d'un financement « indépendant » du groupe (question 2.7).

**Réponses tolérées** : mention de la théorie du signal (un engagement coûteux de la holding est crédible) et de la théorie de l'agence entre la banque, la filiale et la holding (risque que la holding prélève la trésorerie), si elles sont reliées au cas ; mention du financement hiérarchique de Myers et Majluf (1984), qui place le financement interne au groupe avant la dette bancaire.

**Erreurs fréquentes**
- Définir le financement intermédié et le financement de marché sans les appliquer au besoin de 6 M€ de VERMONDAZ.
- Réduire Akerlof au marché des voitures d'occasion, sans transposition au crédit.
- Analyser la force juridique de la lettre d'intention (UE 1) au lieu de son effet sur le risque et la marge.
- `JUR-M01` — théories fondatrices absentes ; `JUR-T14` — méconnaissance des théories ; `JUR-T13` — réponse non contextualisée.

---

### 2.9 Exigences de fonds propres des banques, notation interne, marge et garanties (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.9-01 | Principes : réglementation issue des accords de Bâle (Bâle III, finalisé en 2017, appliqué dans l'Union européenne), fonds propres proportionnels aux risques de crédit ; le besoin de fonds propres d'un crédit dépend de la probabilité de défaut (notation interne) et de la perte que la banque subirait si l'emprunteur faisait défaut (garanties) ; la marge doit couvrir le coût du risque et la rémunération des fonds propres mobilisés | 0,5 |
| 2.9-02 | Application : note de 6 sans soutien → plus de fonds propres → marge de 1,90 % et nantissement ; lettre d'intention → note 4, moins de fonds propres → marge de 1,40 %, sans garantie sur les équipements ; conséquences pour VERMONDAZ : information de la banque, solidité de ses comptes et soutien du groupe améliorent l'accès au crédit et son coût ; aucun calcul de ratio | 0,5 |

**Principes (0,5 pt).** Les accords de Bâle, élaborés par le comité de Bâle et appliqués dans l'Union européenne (règlement CRR3 applicable depuis le 1er janvier 2025 pour la finalisation de Bâle III), imposent aux banques de détenir des **fonds propres en proportion des risques** de leurs crédits (F09 § 2). Le montant de fonds propres qu'un crédit mobilise dépend de deux éléments : la **probabilité de défaut** de l'emprunteur, que la banque estime par sa **notation interne**, et la **perte que la banque subirait si l'emprunteur faisait défaut**, que les garanties réduisent. Les fonds propres coûtent cher à la banque : chaque crédit doit les rémunérer, en plus du coût du risque (les pertes que la banque prévoit sur ses crédits) et des frais de gestion. La réglementation relie ainsi directement le risque de l'emprunteur au prix et aux conditions du crédit (guide p. 61).

**Application au cas (0,5 pt).**
- Sur ses seuls comptes, VERMONDAZ est notée 6 sur 10 : le crédit consomme beaucoup de fonds propres, d'où une marge de 1,90 % et un **nantissement des équipements**, qui réduit la perte de la banque si VERMONDAZ faisait défaut.
- Avec la lettre d'intention de la holding, la note passe à 4 : la probabilité de défaut retenue baisse, le crédit consomme moins de fonds propres, la marge tombe à 1,40 % et la banque renonce au nantissement. La garantie et la notation sont donc des leviers directs du coût du crédit.
- Pour VERMONDAZ, la leçon est pratique : pour obtenir de meilleures conditions, il faut réduire le risque perçu par la banque (information régulière, comptes de la holding, soutien du groupe, structure financière solide) ou lui offrir des garanties ; une dégradation de la note, par exemple dans le scénario faible du projet, renchérirait et raréfierait le crédit.

**Réponses tolérées** : mention des trois piliers (exigences de fonds propres, surveillance prudentielle, discipline de marché) ; mention des contraintes de liquidité des banques, qui les poussent vers des crédits plus courts ou mieux garantis, si elles restent au niveau des principes ; mention de l'incitation au financement de marché pour les entreprises de grande taille.

**Erreurs fréquentes**
- Calculer un ratio prudentiel ou citer des pourcentages réglementaires sans lien avec le cas : le programme demande les principes et leurs conséquences pour l'entreprise.
- Employer l'appellation informelle donnée à la finalisation de Bâle III au lieu de « finalisation de Bâle III » (F99).
- `JUR-T12` — réponse superficielle ; `JUR-T13` — absence de lien avec la note et la marge du cas.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 2, parties 2.2, 5.1, 5.2, 6.2, 7.1 et 7.2 (arrêté du 4 août 2025, annexe 2) ; guide pédagogique de juillet 2026, p. 61, 72-73, 74-75, 77-78, 80-82 | compétences évaluées, principes de Bâle sans calcul, financement direct et indirect, asymétrie d'information, relation valeur-taux, couvertures à prime donnée, VAN en milieu certain et probabilisable, coût des financements | [V] | `ue2/programme/perimetre_ue2.yaml` |
| MEDAF, relation de Hamada avec impôt, CMPC | coût des fonds propres de l'activité et taux d'actualisation du projet | [S] formules de cours | F02 § 2, 3 et 5 |
| VAN, TRI, délai de récupération actualisé, espérance et écart-type de la VAN | critères de choix d'investissement | [S] formules de cours | F01 § 4 et 5 |
| Duration de Macaulay, sensibilité, swap, cap, valeur intrinsèque et valeur temps | risque de taux du prêt intragroupe et couvertures | [S] formules de cours ; [V] programme pour la décomposition de la prime | F07 § 2 |
| Akerlof (1970), « The Market for "Lemons" » | asymétrie d'information et sélection adverse | [V programme] année ; [S] contenu | F10 § 1 |
| Accords de Bâle ; règlement (UE) 2024/1623 (CRR3), applicable depuis le 1er janvier 2025 | exigences de fonds propres des banques, en principes | [V] date d'application ; [S] mécanismes | F09 § 2 |
| Taux sans risque de 4,0 %, prime de marché de 5,0 % | hypothèses d'énoncé cohérentes avec les données d'octobre 2026 | [V] fourchettes | F11 § 1 et 2 |
