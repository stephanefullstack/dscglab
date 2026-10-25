# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 5 — Dossier 2 (18 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et critères d'investissement, F10 auteurs et théories, F11 données de marché (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (VAN, TRI, indice de profitabilité, VAN probabilisée, arbre de décision, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat. Les écarts de quelques k€ dus à l'arrondi des coefficients d'actualisation (par exemple à quatre décimales) sont acceptés.

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
