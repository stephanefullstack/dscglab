# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Sujet d'entraînement complet n° 1

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue2/fiches/`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (investissement, emprunts, coût du capital, DCF, multiples, portefeuille, LBO, BPA, équilibre des bilans, couvertures, barème sur 50, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Coût du capital et évaluation | 20 | 1.1 à 1.5 | `exercices/ex01_evaluation_cout_capital` |
| 2 – Gestion des risques de change, de taux et climatique | 15 | 2.1 à 2.5 | `exercices/ex02_couverture_risques` |
| 3 – Conformité, éthique et financement durable | 15 | 3.1 à 3.5 | `exercices/ex03_conformite_ethique` |
| **Total** | **50** | | |

---

## DOSSIER 1 – COÛT DU CAPITAL ET ÉVALUATION (20 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Coût du capital | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers (MEDAF, CMPC) | 5 |
| 1.2 Flux de trésorerie disponibles | `3.1.b` Construire un business plan | 5 |
| 1.3 DCF | `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance ; `3.1.d` VGE et VCP | 4 |
| 1.4 Multiples et fourchette | `3.2.b` Déterminer le multiple d'un échantillon pour valoriser l'entreprise | 3 |
| 1.5 Notation extra-financière | `2.1.c` Utiliser les outils de notation financière et extra-financière | 3 |
| **Total** | | **20** |

---

### 1.1 Coût des capitaux propres et CMPC (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Justification du désendettement puis du réendettement | 1 |
| 1.1-02 | Bêtas désendettés des trois comparables et moyenne 0,86 | 1,5 |
| 1.1-03 | Bêta réendetté d'ORVANE 1,1825 | 0,5 |
| 1.1-04 | ke = 11,91 % avec justification de la prime spécifique | 1 |
| 1.1-05 | kd net 3,75 % et CMPC 9,19 % | 1 |

**Pourquoi désendetter puis réendetter (1 pt).** ORVANE n'est pas cotée : son bêta ne peut pas être observé. On l'estime à partir de sociétés cotées du même secteur. Mais le bêta observé d'une action mesure à la fois le **risque économique** (celui de l'activité) et le **risque financier** (celui du levier) : plus une société est endettée, plus ses actionnaires supportent un risque élevé. Les comparables n'ayant pas la même structure financière qu'ORVANE, on retire d'abord l'effet de leur endettement (bêta de l'actif, ou bêta désendetté), on fait la moyenne de ce risque d'activité, puis on y applique la structure financière cible d'ORVANE (bêta réendetté) [F02 § 3].

**Bêtas désendettés (1,5 pt)**, formule de l'annexe 1.1 : βa = βe / [1 + (1 − t) × D/E].

| Comparable | D/E | 1 + 0,75 × D/E | βe | βa |
|---|---:|---:|---:|---:|
| Société A | 600 / 1 500 = 0,40 | 1,30 | 1,04 | **0,8000** |
| Société B | 640 / 800 = 0,80 | 1,60 | 1,44 | **0,9000** |
| Société C | 900 / 2 700 = 0,3333 | 1,25 | 1,10 | **0,8800** |
| **Moyenne** | | | | **0,8600** |

**Bêta réendetté d'ORVANE (0,5 pt)** : βe = 0,86 × (1 + 0,75 × 0,5) = 0,86 × 1,375 = **1,1825**.

**Coût des capitaux propres (1 pt)** : ke = 4 % + 1,1825 × 5 % + 2 % = 4 % + 5,9125 % + 2 % = 11,9125 %, soit **ke = 11,91 %**.

La prime de 2 % rémunère des risques que le MEDAF ne capte pas pour une société non cotée : sa **taille** plus modeste que celle des comparables (dépendance à quelques dirigeants, à quelques clients) et l'**illiquidité** de ses titres, qu'un investisseur ne peut pas revendre rapidement sur un marché. Le guide pédagogique admet ces primes complémentaires « lorsque cela est nécessaire », à partir de données fournies [V guide p. 64 ; F02 § 0].

**CMPC (1 pt)** : kd net = 5 % × (1 − 25 %) = **3,75 %**. Avec D/E = 0,5, les poids sont E/V = 1 / 1,5 = 2/3 et D/V = 1/3.

CMPC = 11,91 % × 2/3 + 3,75 % × 1/3 = 7,94 % + 1,25 % = **9,19 %**.

Le CMPC est le taux de rentabilité minimal exigé par l'ensemble des apporteurs de capitaux ; c'est le taux d'actualisation des flux de trésorerie disponibles de la question 1.3.

**Réponses tolérées** : ke conservé à 11,9125 % dans le CMPC (9,1917 %, arrondi à 9,19 %) ; poids écrits sous forme décimale (0,6667 et 0,3333).

**Erreurs fréquentes**
- `JUR-E02` — bêta des comparables utilisé sans désendettement, ou réendetté avec la structure du comparable au lieu de celle d'ORVANE.
- Traiter les 5 % comme la rentabilité du marché et en retrancher encore le taux sans risque : la prime de 5 % est déjà E(Rm) − rf, elle se multiplie directement par le bêta.
- Multiplier la prime spécifique par le bêta : elle s'ajoute au résultat du MEDAF [F02 § 2].
- Pondérer le CMPC avec les valeurs comptables alors que l'énoncé donne une structure cible en valeurs de marché.

---

### 1.2 Flux de trésorerie disponibles 2027-2031 (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | IS calculé sur le résultat d'exploitation | 1 |
| 1.2-02 | Variation du BFR (et non le BFR lui-même) | 1,5 |
| 1.2-03 | FTD justes (0,5 par année, dans la limite de 2) | 2 |
| 1.2-04 | Absence des frais financiers justifiée | 0,5 |

Formule : FTD = EBITDA − IS sur le résultat d'exploitation − variation du BFR − investissements [F03 § 2.1].

| k€ | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| EBITDA | 10 080 | 10 560 | 11 040 | 11 400 | 11 640 |
| − Dotations aux amortissements | 3 000 | 3 200 | 3 400 | 3 500 | 3 600 |
| = Résultat d'exploitation | 7 080 | 7 360 | 7 640 | 7 900 | 8 040 |
| IS à 25 % sur le résultat d'exploitation | 1 770 | 1 840 | 1 910 | 1 975 | 2 010 |
| BFR (15 % du chiffre d'affaires) | 12 600 | 13 200 | 13 800 | 14 250 | 14 550 |
| Variation du BFR (BFR 2026 : 12 000) | 600 | 600 | 600 | 450 | 300 |
| Investissements | 4 000 | 4 000 | 3 800 | 3 600 | 3 600 |
| **FTD = EBITDA − IS − ΔBFR − investissements** | **3 710** | **4 120** | **4 730** | **5 375** | **5 730** |

Les dotations ne sont pas décaissées : elles n'interviennent que pour calculer l'impôt. Formulation équivalente : FTD = résultat d'exploitation × (1 − 25 %) + dotations − ΔBFR − investissements (2027 : 5 310 + 3 000 − 600 − 4 000 = 3 710).

**Pourquoi pas de frais financiers (0,5 pt).** Les FTD sont les flux disponibles pour **tous** les apporteurs de capitaux, actionnaires et prêteurs. La rémunération des prêteurs est prise en compte dans le taux d'actualisation, le CMPC, à travers le coût de la dette après impôt. Déduire en plus les intérêts du flux reviendrait à compter deux fois le coût de la dette. Pour la même raison, l'IS est calculé sur le résultat d'exploitation et non sur le résultat après frais financiers : l'économie d'impôt liée aux intérêts est déjà dans kd × (1 − t) [F03 § 2.1].

**Réponses tolérées** : présentation à partir de la capacité d'autofinancement d'exploitation ; tableau en colonnes ou en lignes.

**Erreurs fréquentes**
- `JUR-E01` — FTD mal connus : soustraction du BFR total (12 600 en 2027) au lieu de sa variation ; déduction des frais financiers ; oubli de l'IS.
- `JUR-T07` — calculs sans tableau.

---

### 1.3 Valeur par les flux actualisés (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | Somme des FTD actualisés 17 960 | 1 |
| 1.3-02 | Valeur terminale 81 288 et actualisation 52 373 | 1 |
| 1.3-03 | VGE 70 333, VCP 47 333, 94,67 € par action | 1 |
| 1.3-04 | Commentaire sur le poids de la valeur terminale | 1 |

Taux d'actualisation : CMPC = 9,19 %, flux en fin d'année.

| k€ | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| FTD | 3 710 | 4 120 | 4 730 | 5 375 | 5 730 |
| Coefficient 1,0919^−n | 0,915835 | 0,838753 | 0,768159 | 0,703507 | 0,644296 |
| FTD actualisé | 3 397,75 | 3 455,66 | 3 633,39 | 3 781,35 | 3 691,82 |

Somme des FTD actualisés = **17 960 k€**.

**Valeur terminale** (Gordon-Shapiro, fin 2031) : VT = FTD 2031 × (1 + g) / (CMPC − g) = 5 730 × 1,02 / (0,0919 − 0,02) = 5 844,6 / 0,0719 = **81 288 k€**.

Valeur terminale actualisée : 81 288 × 1,0919^−5 = 81 288 / 1,552081 = **52 373 k€**.

**VGE** = 17 960 + 52 373 = **70 333 k€**.

**VCP** = VGE − dettes financières nettes = 70 333 − 23 000 = **47 333 k€**, soit 47 333 000 € / 500 000 actions = **94,67 € par action**.

**Commentaire (1 pt).** La valeur terminale représente 52 373 / 70 333 = **74,5 % de la VGE**. L'essentiel de la valeur repose donc sur des flux postérieurs à 2031, donc sur deux hypothèses fragiles : une croissance de 2 % à l'infini et le maintien d'un CMPC de 9,19 %. Une variation de l'écart CMPC − g modifie fortement le résultat : il faut présenter la valeur avec une analyse de sensibilité, et vérifier que le flux de 2031 est bien normatif (en 2031, les investissements égalent les dotations, ce qui est cohérent avec une croissance faible ; la variation du BFR de 300 k€ est proche de celle qu'impliquerait une croissance de 2 % du chiffre d'affaires, environ 290 k€). Cohérence de la structure financière : 23 000 / 47 333 = 0,49, proche du ratio cible de 0,5 retenu pour le CMPC.

**Réponses tolérées** : valeur terminale écrite VT = FTD 2032 / (CMPC − g), avec FTD 2032 = 5 730 × 1,02 = 5 844,6 (même résultat) ; écarts d'arrondi de quelques k€ dus aux coefficients d'actualisation.

**Erreurs fréquentes**
- Valeur terminale non actualisée, ou actualisée sur six ans.
- Confusion entre VGE et VCP : la dette nette doit être retranchée pour obtenir la valeur revenant aux actionnaires.
- Actualiser les FTD au coût des capitaux propres (11,91 %) au lieu du CMPC.

---

### 1.4 Multiples et fourchette de négociation (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Multiples des comparables, médiane 8, multiple décoté 6,8 | 1 |
| 1.4-02 | VGE 65 280, VCP 42 280 | 1 |
| 1.4-03 | Fourchette pour 40 % et arguments du fonds | 1 |

**Multiples de l'échantillon (1 pt)** : VGE d'un comparable = capitalisation + dettes financières nettes.

| Comparable | VGE (M€) | EBITDA (M€) | VGE / EBITDA |
|---|---:|---:|---:|
| Société A | 1 500 + 600 = 2 100 | 250 | 8,4 |
| Société B | 800 + 640 = 1 440 | 180 | 8,0 |
| Société C | 2 700 + 900 = 3 600 | 450 | 8,0 |

Médiane = **8,0** ; multiple décoté de 15 % : 8,0 × 0,85 = **6,8**.

**Valeur d'ORVANE (1 pt)** : VGE = 9 600 × 6,8 = **65 280 k€** ; VCP = 65 280 − 23 000 = **42 280 k€**, soit **84,56 € par action**. Sans décote, le multiple de 8 donnerait une VGE de 76 800 k€ et une VCP de 53 800 k€.

**Fourchette et arguments (1 pt).** Les deux méthodes encadrent la VCP entre **42 280 k€** (multiples décotés) et **47 333 k€** (DCF). Pour 40 % du capital, la fourchette de prix est de **16 912 k€ à 18 933 k€**, soit 84,56 € à 94,67 € par action. Le croisement des méthodes fonde la négociation [F03 § 8 ; `JUR-E03`].

Arguments que le fonds peut avancer pour un prix bas :
- il acquiert une participation **minoritaire** sans contrôle : une décote de minorité peut s'ajouter, sauf si les accords conclus entre actionnaires lui accordent des droits renforcés (sortie conjointe, droits de veto) ;
- la valeur DCF repose aux trois quarts sur la valeur terminale et sur un plan d'affaires établi par la direction ;
- la dépendance à la présidente et la succession non organisée accroissent le risque ;
- la note extra-financière actuelle place ORVANE en catégorie C, ce qui, selon sa politique, le conduit à retenir la borne basse (question 1.5).

**Réponses tolérées** : multiple moyen (8,13) si l'écart avec la consigne de médiane est signalé ; fourchette établie sur la VCP totale avec mention du pourcentage acquis.

**Erreurs fréquentes**
- Multiple de VGE appliqué pour obtenir directement la VCP, sans déduire la dette nette.
- Capitalisation boursière divisée par l'EBITDA (mélange d'un numérateur de capitaux propres et d'un agrégat avant frais financiers).

---

### 1.5 Notation extra-financière (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | Notes des piliers et note globale 54,95, catégorie C | 1,5 |
| 1.5-02 | Nouvelle note 60,95, catégorie B | 0,5 |
| 1.5-03 | Conclusion argumentée | 1 |

**Notes des piliers et note globale (1,5 pt)**

| Pilier | Calcul | Note |
|---|---|---:|
| Environnement | 0,50 × 55 + 0,25 × 70 + 0,25 × 80 = 27,5 + 17,5 + 20 | 65,0 |
| Social | 0,40 × 60 + 0,30 × 75 + 0,30 × 50 = 24 + 22,5 + 15 | 61,5 |
| Gouvernance | 0,50 × 40 + 0,50 × 30 = 20 + 15 | 35,0 |

Note globale = 0,40 × 65,0 + 0,30 × 61,5 + 0,30 × 35,0 = 26,00 + 18,45 + 10,50 = **54,95**, soit la **catégorie C** (de 45 à moins de 60).

**Effet du comité stratégique (0,5 pt)** : la note de gouvernance passe à 0,50 × 80 + 0,50 × 30 = 55,0. La note globale gagne 0,30 × (55,0 − 35,0) = 6,00 points : 54,95 + 6,00 = **60,95**, soit la **catégorie B**.

**Conclusion (1 pt).** Le point faible d'ORVANE n'est pas son activité, favorable à la transition énergétique (pilier environnemental à 65), mais sa **gouvernance** : capital entièrement familial, présidente fondatrice, aucun regard extérieur au comité stratégique, aucun critère de durabilité dans sa rémunération. Pour un investisseur minoritaire, des membres indépendants réduisent les **coûts d'agence** : ils contrôlent la direction et protègent les minoritaires [F10 : Jensen et Meckling, 1976]. Engager la démarche avant la négociation a donc un double intérêt :
- financier : en catégorie B, le prix se négocie sur toute la fourchette de la question 1.4, et non plus sur sa borne basse. L'enjeu peut atteindre 18 933 − 16 912 = **2 021 k€** au plus pour 40 % du capital ;
- stratégique : la gouvernance ouverte prépare la succession de Mme VARENNE et l'arrivée d'un actionnaire extérieur.

Recommandation : nommer les deux membres indépendants avant l'ouverture des négociations, et proposer un critère de durabilité dans la rémunération de la présidente, qui renforcerait encore le pilier de gouvernance (encore à 55).

Il n'est pas attendu du candidat qu'il cite le règlement (UE) 2024/3005 sur les notations ESG. Une grille établie par un fonds pour son propre usage relève en principe de ses exclusions (notations à usage interne), mais la question de la fiabilité et de la comparabilité des notations reste pertinente [F08 § 3.2].

**Réponses tolérées** : toute recommandation cohérente appuyée sur un chiffre du cas, par exemple un plan d'amélioration du critère « partage de la valeur » ; l'outil de notation peut aussi être critiqué (pondérations choisies par le fonds, notes attribuées par ses propres analystes).

**Erreurs fréquentes**
- `JUR-D01` — confusion entre RSE (démarche de l'entreprise) et ESG (critères d'évaluation utilisés par les investisseurs).
- `JUR-T13` — conclusion générale sur la RSE sans lien avec la négociation ni avec les chiffres du cas.
- Additionner les notes des critères sans les pondérer.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 63-65 | MEDAF avec primes complémentaires, CMPC, FTD, valeur terminale, multiples | [V] | F02, F03 |
| Hamada (1972) | désendettement et réendettement du bêta avec impôt | [S] | F02 § 3 |
| Gordon et Shapiro (1956) | valeur terminale à croissance constante | [V programme ; année S] | F10 |
| Jensen et Meckling (1976) | théorie de l'agence, rôle des administrateurs indépendants | [V programme] | F10, F08 |
| Règlement (UE) 2024/3005, art. 2 § 2 | exclusion des notations à usage interne | [V] | F08 § 3.2 |

---

## DOSSIER 2 – GESTION DES RISQUES DE CHANGE, DE TAUX ET CLIMATIQUE (15 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Position de change et achat à terme | `6.3.a` Caractériser la position de change ; `6.3.b` marché comptant et à terme | 3 |
| 2.2 Option de change | `6.3.d` Contrats à terme et optionnels (change) | 3 |
| 2.3 Swap et cap | `6.2.b` Principaux instruments de couverture du risque de taux | 4 |
| 2.4 Option climatique | `6.4.a` Instruments de couverture des risques liés au changement climatique | 3 |
| 2.5 Discussion | `6.4.a` ; `2.1.d` double matérialité | 2 |
| **Total** | | **15** |

---

### 2.1 Position de change et achat à terme (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Position courte en USD, risque d'appréciation du dollar | 1 |
| 2.1-02 | Cours à terme 1,1239 et coût 1 779 518 € | 1 |
| 2.1-03 | Explication par le différentiel de taux (report de l'euro) | 1 |

**Position (1 pt).** ORVANE doit payer 2 000 000 USD dans 90 jours sans détenir de dollars : elle a une **position courte** et **ouverte** en dollars. Elle supporte un **risque de transaction** : si le dollar s'**apprécie**, ce qui correspond au certain à une **baisse** du cours EUR/USD, il lui faudra davantage d'euros pour régler sa dette. À 1,0800, la commande coûterait 2 000 000 / 1,08 = 1 851 852 €, soit 66 138 € de plus qu'au cours du jour [F07 § 3.1].

**Cours à terme (1 pt).**

F = 1,1200 × (1 + 4,00 % × 90/360) / (1 + 2,60 % × 90/360) = 1,1200 × 1,0100 / 1,0065 = 1,123895, soit **1,1239**.

Coût de la commande couverte à terme : 2 000 000 / 1,1239 = **1 779 518 €**, connu dès le 31/12/2026. Au comptant du jour : 2 000 000 / 1,1200 = 1 785 714 €.

**Pourquoi le terme est plus favorable (1 pt).** Le cours à terme se déduit de la parité des taux d'intérêt. Le dollar est mieux rémunéré que l'euro (4,00 % contre 2,60 %) : il cote en **déport**, et l'euro en **report** (F > S, + 39 points). À terme, un euro achète donc davantage de dollars qu'au comptant. Pour livrer des dollars dans trois mois, la banque emprunte des euros à 2,60 %, les convertit au comptant et place les dollars à 4,00 % ; elle répercute ce différentiel dans le cours à terme. L'économie de 6 196 € n'est pas un gain de change : elle traduit le différentiel de taux d'intérêt sur 90 jours.

**Réponses tolérées** : cours à terme non arrondi (1,123895, coût 1 779 526 €) ; raisonnement par les points de swap.

**Erreurs fréquentes**
- Inverser le sens du risque : un importateur craint la hausse de la devise qu'il doit payer, pas sa baisse.
- Inverser les taux dans la formule (euro au numérateur) en cotation au certain : on obtient 1,1161, cours incohérent avec un taux du dollar plus élevé.

---

### 2.2 Option de change (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Prime 21 429 €, VI nulle, VT = prime | 1 |
| 2.2-02 | Coûts dans les deux scénarios et comparaison | 1 |
| 2.2-03 | Recommandation argumentée | 1 |

**Prime et décomposition (1 pt).** Prime = 2 000 000 × 1,2 % = 24 000 USD, soit 24 000 / 1,12 = **21 429 €**. Au 31/12/2026, le prix d'exercice (1,1200) est égal au cours comptant : l'option est **à la monnaie**. Son exercice immédiat ne rapporterait rien : **valeur intrinsèque = 0**. Toute la prime est de la **valeur temps**, dite aussi valeur spéculative (21 429 €) : elle rémunère la possibilité que le dollar s'apprécie d'ici l'échéance [F07 § 3.3]. La prime est donnée : aucun modèle d'évaluation n'est attendu.

**Coût de la commande (1 pt)**

| € | 1 EUR = 1,0800 USD (dollar en hausse) | 1 EUR = 1,1600 USD (dollar en baisse) |
|---|---:|---:|
| Sans couverture | 2 000 000 / 1,08 = 1 851 852 | 2 000 000 / 1,16 = 1 724 138 |
| Achat à terme | 1 779 518 | 1 779 518 |
| Option | exercée : 2 000 000 / 1,12 = 1 785 714 + prime 21 429 = **1 807 143** | abandonnée : 1 724 138 + prime 21 429 = **1 745 567** |

L'option plafonne le coût à 1 807 143 € tout en laissant profiter d'une baisse du dollar. Elle devient plus intéressante que le terme dès que le cours dépasse 2 000 000 / (1 779 518 − 21 429) = 1,1376 au 31/03/2027.

**Recommandation (1 pt).** La commande est **ferme** et son montant est **certain** : l'**achat à terme** est la couverture adaptée. Elle est gratuite, simple, et même favorable ici grâce au report de l'euro. Elle supprime le risque, mais aussi la possibilité de profiter d'une baisse du dollar. L'option ne se justifierait que si la commande pouvait être annulée, ou si la direction anticipait une forte baisse du dollar, au-delà de 1,1376. Les critères du choix sont le coût, la souplesse, la simplicité et le risque résiduel [V guide p. 79].

**Réponses tolérées** : recommandation de l'option si elle est justifiée par une anticipation chiffrée ; couverture partielle (terme pour une partie, option pour le reste).

**Erreurs fréquentes**
- Oublier la prime dans le coût de l'option, ou la retrancher alors qu'ORVANE la paie.
- Exercer l'option dans le scénario 1,1600 : au comptant, l'euro achète plus de dollars qu'au prix d'exercice.
- Tenter de calculer la prime : les modèles de valorisation des options sont hors programme.

---

### 2.3 Swap et cap (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Coûts et taux sans couverture | 0,5 |
| 2.3-02 | Swap : différentiels, coût net 150 000 €, taux 5,00 % | 1,5 |
| 2.3-03 | Cap : versement, prime, coût net, taux 4,75 % et 5,35 % | 1,5 |
| 2.3-04 | Conseil à la direction | 0,5 |

Intérêts du trimestre = 12 000 000 × taux × 90/360. Taux annuel = coût du trimestre / (12 000 000 × 90/360).

| € (90 jours) | Euribor 2,40 % | Euribor 3,40 % |
|---|---:|---:|
| **Sans couverture** : intérêts au taux variable, marge de 2,10 % comprise | 135 000 (4,50 %) | 165 000 (5,50 %) |
| **Swap** : différentiel (2,90 % contre Euribor) | versé : 15 000 | reçu : 15 000 |
| Coût net avec le swap | **150 000 (5,00 %)** | **150 000 (5,00 %)** |
| **Cap** : versement reçu (Euribor − 3 %) | 0 | 12 000 |
| Prime du trimestre (0,25 % × 90/360) | 7 500 | 7 500 |
| Coût net avec le cap | **142 500 (4,75 %)** | **160 500 (5,35 %)** |

Le swap transforme l'emprunt variable en emprunt à **taux fixe de 5,00 %** (2,90 % + 2,10 %), quel que soit l'Euribor. Le cap fixe un **taux maximal de 5,35 %** (3,00 % + 2,10 % + 0,25 %) et laisse profiter d'une baisse, moyennant la prime.

**Conseil (0,5 pt).** Le choix dépend des anticipations de la direction et de son aversion au risque :
- le **swap** est sans prime et donne une visibilité complète sur les frais financiers pendant cinq ans, ce que le fonds appréciera dans le plan d'affaires. En contrepartie, il fait renoncer à toute baisse des taux, et le débouclage avant terme peut être coûteux ;
- le **cap** coûte 0,25 % par an, soit 30 000 € par an, mais conserve le bénéfice d'une baisse ;
- un compromis possible : couvrir une partie du nominal par swap et laisser le reste variable, ou acheter un **tunnel** (cap acheté et floor vendu), dont la prime nette est plus faible.

Si la direction anticipe une stabilité ou une hausse des taux, le swap est la solution la plus prudente pour une ETI qui s'endette sur cinq ans ; si elle anticipe une baisse, le cap ou une couverture partielle se défendent.

**Réponses tolérées** : calcul en mois/12 (3 mois), qui donne ici les mêmes montants ; taux actuariel si la méthode est explicitée ; recommandation du cap justifiée par une anticipation de baisse.

**Erreurs fréquentes**
- Inverser le sens du différentiel de swap : le payeur de fixe reçoit quand l'Euribor dépasse le taux fixe.
- Oublier la marge de 2,10 %, qui reste due dans toutes les solutions.
- Oublier la prime du cap dans le coût net.
- `JUR-T07` — résultats donnés sans tableau.

---

### 2.4 Option climatique (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Indemnités et effets nets dans les trois scénarios | 1,5 |
| 2.4-02 | Nature du risque couvert (volume) | 0,5 |
| 2.4-03 | Limites de la couverture | 1 |

Indemnité = 4 000 € × max(0 ; 2 500 − indice), plafonnée à 800 000 €. Effet de l'hiver sur l'EBITDA = 4 000 € × (indice − 2 600).

| € | 2 600 (normal) | 2 400 | 2 200 |
|---|---:|---:|---:|
| Effet de l'hiver sur l'EBITDA | 0 | − 800 000 | − 1 600 000 |
| Indemnité de l'option | 0 | + 400 000 | + 800 000 (plafond atteint) |
| Prime | − 120 000 | − 120 000 | − 120 000 |
| **Effet net sur le résultat avant impôt** | **− 120 000** | **− 520 000** | **− 920 000** |

**Nature du risque (0,5 pt).** L'option couvre un **risque de volume**, et non de prix : un hiver doux réduit les ventes. Le sous-jacent est un **indice météorologique non livrable** ; le contrat se dénoue en espèces.

**Lecture et limites (1 pt).**
- La couverture laisse à la charge d'ORVANE une **franchise** de 100 degrés-jours entre la normale (2 600) et le prix d'exercice (2 500), soit 400 000 €, plus la prime. Entre 2 500 et 2 300 degrés-jours, la perte nette reste donc limitée à 520 000 €.
- Le **plafond** de 800 000 € est atteint à 2 300 degrés-jours. En dessous, la perte reprend : à 2 200, l'option ne compense que la moitié de la baisse d'EBITDA.
- **Risque de base** : la station est à 30 km, et la sensibilité de 4 000 € par degré-jour est une estimation statistique sur douze ans. La perte réelle peut différer de l'indemnité.
- La prime est perdue si l'hiver est normal ou froid ; un hiver froid augmente toutefois l'EBITDA.
- **Risque de contrepartie** : l'indemnité dépend de la solidité de la banque.

**Erreurs fréquentes**
- Oublier le plafond à 2 200 degrés-jours (indemnité de 1 200 000 €).
- Confondre dérivé climatique et assurance des dommages : l'option indemnise un écart d'indice, sans sinistre ni constat de perte.

---

### 2.5 Discussion : « le risque climatique est réglé » (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Limites de l'affirmation (risques non couverts) | 1 |
| 2.5-02 | Mise en perspective stratégique et recommandation | 1 |

L'affirmation est excessive.
- **L'option transfère un risque financier, elle ne réduit pas l'exposition.** Elle couvre une partie de l'effet d'un hiver doux sur une seule saison. Avec le réchauffement, la « normale » de 2 600, calculée sur le passé, sera de moins en moins atteinte : les vendeurs d'options intégreront cette tendance, et les primes augmenteront. C'est un outil de lissage du résultat, pas une adaptation.
- **D'autres risques climatiques ne sont pas couverts** [F07 § 5] :
  - **risques physiques** : canicule ou inondation sur le site de production, rupture d'approvisionnement des compresseurs ;
  - **risques de transition** : durcissement de la réglementation des fluides frigorigènes, évolution des aides publiques à la rénovation, prix de l'énergie.
- **Le climat crée aussi des opportunités** pour ORVANE : les étés plus chauds augmentent la demande de pompes à chaleur réversibles, qui climatisent. Une offre réversible constitue une **couverture naturelle**, plus durable que l'option.
- **Double matérialité** : il faut analyser l'effet du climat sur ORVANE (matérialité financière), mais aussi l'effet d'ORVANE sur le climat (matérialité d'impact). Ses produits remplacent des chaudières à énergie fossile. C'est un argument fort auprès d'un fonds de la transition énergétique, lui-même tenu à des obligations de transparence sur la durabilité de ses investissements [F08 ; SFDR].

**Recommandation.** Intégrer le risque climatique dans la cartographie des risques et dans le plan d'affaires : diversification vers les pompes à chaleur réversibles, plan d'adaptation du site, sécurisation des approvisionnements. L'option climatique ne doit être qu'un complément de court terme.

**Réponses tolérées** : toute argumentation qui distingue couverture financière et réduction de l'exposition, en s'appuyant sur les données du cas.

**Erreurs fréquentes**
- `JUR-T05` — performance durable traitée à part, sans lien avec les calculs du dossier.
- `JUR-T13` — discussion générale sur le réchauffement, sans référence à ORVANE.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 2, partie 6 ; guide pédagogique, juillet 2026, p. 77-80 | instruments de couverture, critères de choix (coût, simplicité, flexibilité, risque résiduel), exclusion des modèles de valorisation des options | [V] | F07 § 0 |
| Parité des taux d'intérêt | cours à terme | [S] | F07 § 3.3 |
| Corrigé DSCG 2023, dossier 3 | présentation d'un swap en tableau par scénario | [V] | F07 § 2.2 |
| Dérivés climatiques sur degrés-jours | indemnité, risque de base | [S] | F07 § 5 |

---

## DOSSIER 3 – CONFORMITÉ, ÉTHIQUE ET FINANCEMENT DURABLE (15 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Morale, éthique, déontologie, conformité | `2.2.a` Distinguer l'éthique, la morale, la déontologie et la conformité | 2 |
| 3.2 Loi Sapin II | `2.2.d` Sensibiliser au risque de corruption et de fraude | 3 |
| 3.3 Trois situations | `2.2.c` LCB-FT ; `2.2.d` corruption et fraude ; `2.2.e` risque cyber | 4 |
| 3.4 Prêt à impact | `7.2.c` Analyser les nouveaux outils de financement | 3 |
| 3.5 Comte-Sponville | `2.2.a` Hiérarchie des ordres | 3 |
| **Total** | | **15** |

---

### 3.1 Morale, éthique, déontologie, conformité (2 pts)

0,5 point par notion correctement définie **et** illustrée par le cas.

| Notion | Définition | Illustration dans le cas |
|---|---|---|
| **Morale** | Devoirs et interdits à portée universelle (le bien et le mal), qui s'imposent à la personne indépendamment de son intérêt | Refuser de verser une commission suspecte même si personne ne devait l'apprendre (situation A) |
| **Éthique** | Réflexion sur les valeurs et sur la manière de bien agir dans une situation donnée ; en entreprise, valeurs qu'elle se donne (charte). Chez Comte-Sponville, l'éthique relève de l'amour et des liens, la morale du devoir : les deux acceptions sont admises | Ce que Mme VARENNE veut que soit ORVANE, entreprise familiale qu'elle s'apprête à transmettre |
| **Déontologie** | Règles de conduite propres à une profession, codifiées et contrôlées par l'instance de la profession | Les obligations du cabinet d'expertise comptable : secret professionnel, devoir de conseil, vigilance anti-blanchiment |
| **Conformité** | Organisation qui garantit le respect des normes externes (lois, règlements) et internes (code de conduite) : cartographie des risques, procédures, contrôles, formation, alerte | Le dispositif que demande à consulter le fonds ; la procédure de vérification d'un changement de coordonnées bancaires (situation C) |

[F09 § 1]

**Erreur fréquente** : définir les notions sans les relier au cas (`JUR-T13`), ou confondre morale (le devoir) et droit (la loi).

---

### 3.2 Loi Sapin II (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | ORVANE non soumise aujourd'hui | 0,5 |
| 3.2-02 | Soumise après l'acquisition : effectif 540, chiffre d'affaires consolidé 106 000 k€ | 1 |
| 3.2-03 | Mesures à mettre en place | 0,5 |
| 3.2-04 | Intérêt d'une adoption volontaire | 1 |

**Aujourd'hui (0,5 pt).** ORVANE emploie 410 salariés (moins de 500) et réalise 80 000 k€ de chiffre d'affaires (pas plus de 100 M€). Les deux conditions sont cumulatives, et aucune n'est remplie : sa présidente n'est **pas tenue** de mettre en place le dispositif de l'article 17 [V loi Sapin II, art. 17 I].

**Après l'acquisition (1 pt).** ORVANE deviendrait société mère d'un groupe dont le siège est en France :
- effectif du groupe : 410 + 130 = **540 salariés**, au moins 500 ;
- chiffre d'affaires consolidé : 80 000 + 28 000 − 2 000 (ventes d'ORVANE au distributeur, éliminées en consolidation) = **106 000 k€**, supérieur à 100 M€.

Les deux conditions seraient remplies : la présidente devrait mettre en place les mesures pour ORVANE **et** sa filiale.

**Mesures (0,5 pt)**, les huit de l'article 17 II [V] :
- code de conduite ;
- dispositif d'alerte interne ;
- cartographie des risques de corruption ;
- évaluation des clients, fournisseurs de premier rang et intermédiaires ;
- contrôles comptables ;
- formation des personnels exposés ;
- régime disciplinaire ;
- contrôle et évaluation interne du dispositif.

**Intérêt d'une adoption volontaire (1 pt)**
- **Les situations de l'annexe 3.2 montrent que le risque existe déjà** : intermédiaire à l'export, nouveau client mal identifié, tentative de fraude. La cartographie des risques et l'évaluation des tiers auraient permis de les traiter selon une procédure, et non dans l'urgence.
- **La négociation avec le fonds** : celui-ci examine le dispositif de conformité lors de ses vérifications préalables, et un dispositif défaillant peut compromettre son entrée. Il exigera en tout état de cause sa mise en place avant l'acquisition qu'il projette.
- **Les autres parties prenantes** : banques, assureurs, donneurs d'ordre publics et grands clients demandent de plus en plus à leurs fournisseurs un dispositif anticorruption.
- **L'anticipation** : un dispositif construit progressivement coûte moins cher qu'un dispositif imposé en urgence après l'acquisition.

**Réponses tolérées** : chiffre d'affaires consolidé de 108 000 k€ sans élimination des ventes intragroupe, si la conclusion est juste (la conclusion ne change pas) ; ne pas exiger le détail des huit mesures, quatre ou cinq bien choisies suffisent.

---

### 3.3 Les trois situations (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Situation A : risque de corruption et conduite à tenir | 1 |
| 3.3-02 | Situation B : risque de blanchiment, MiCA, conduite à tenir | 1 |
| 3.3-03 | Situation C : fraude au faux fournisseur, conduite à tenir | 1 |
| 3.3-04 | Obligations du cabinet | 1 |

**Situation A : risque de corruption (1 pt).** Plusieurs signaux d'alerte se cumulent :
- client public ;
- commission trois fois supérieure aux usages : 9 % × 6 000 = **540 k€**, contre 180 k€ à 3 % ;
- compte dans un troisième pays ;
- prestations non justifiées.

L'écart de 360 k€ pourrait servir à rémunérer un décideur. Le droit français réprime aussi la corruption d'agents publics étrangers : ORVANE et ses dirigeants seraient exposés, quel que soit le lieu des faits. S'y ajoutent l'exclusion des marchés publics, la perte de confiance du fonds et des banques, et le coût réputationnel [S].

Conduite à tenir : ne pas signer en l'état. Mener une évaluation de l'intermédiaire (identité, bénéficiaires effectifs, références, réalité des prestations). Exiger un contrat écrit qui détaille les prestations, une rémunération au niveau des usages et un paiement sur un compte au nom de l'agent dans son pays d'activité. Refuser si l'agent persiste.

**Situation B : risque de blanchiment (1 pt).** Là encore, les signaux s'accumulent :
- client nouveau, introduit par un tiers ;
- refus de révéler ses actionnaires, donc son **bénéficiaire effectif** ;
- paiement **fractionné** depuis plusieurs portefeuilles ;
- moyen de paiement difficile à tracer ;
- urgence.

Le schéma est typique du blanchiment : des fonds d'origine illicite seraient intégrés dans l'économie légale par l'achat de biens réels. Par ailleurs, depuis le 2 juillet 2026, la période transitoire du règlement MiCA ayant pris fin le 1er juillet, seuls les prestataires de services sur crypto-actifs **agréés** peuvent fournir ces services dans l'Union. Passer par une plateforme non agréée prive ORVANE des garanties prévues par MiCA (conservation et ségrégation des actifs des clients, surveillance par une autorité) [V MiCA art. 59 et 143 ; communiqué AMF du 06/07/2026]. Les jetons proposés, émis hors de l'Union, ne relèvent vraisemblablement pas du régime des jetons de monnaie électronique autorisés (signal supplémentaire, non exigé). Enfin, un paiement en crypto-actifs fait supporter un risque de volatilité et de conservation.

Conduite à tenir : refuser le paiement en crypto-actifs. Exiger un virement depuis un compte bancaire au nom du client, et l'identification de ses actionnaires. Ne pas livrer tant que le paiement n'est pas encaissé et justifié. Renoncer à la vente si le client refuse. La banque d'ORVANE, elle-même assujettie, pourrait d'ailleurs bloquer l'opération.

**Situation C : tentative de fraude au faux fournisseur (1 pt).** Les signes sont classiques : changement de coordonnées bancaires annoncé par courriel, compte dans un autre pays, urgence, confidentialité, approche d'un paiement important. L'enjeu atteint 2 000 000 USD, soit environ 1,8 M€, près d'un cinquième de l'EBITDA annuel [F09 § 5].

Conduite à tenir : suspendre le paiement. Vérifier par un **contre-appel** au fournisseur, à un numéro déjà connu et non à celui du courriel. Appliquer une double validation de tout changement de coordonnées bancaires. Sensibiliser les équipes.

Si un virement avait déjà été émis : demander immédiatement son rappel à la banque, porter plainte et se faire assister par les dispositifs publics : cybermalveillance.gouv.fr pour l'assistance, les services spécialisés de police et de gendarmerie (COMCYBER-MI) pour l'enquête [F09 § 5.2]. Les chances de récupération décroissent en quelques heures.

**Obligations du cabinet (1 pt).** L'expert-comptable est lui-même **assujetti** aux obligations de lutte contre le blanchiment et le financement du terrorisme [V fiche commune § 2.2] :
- connaître son client ;
- exercer une vigilance constante sur ses opérations ;
- mener un examen renforcé des opérations inhabituelles ;
- en cas de soupçon que des sommes proviennent d'une infraction punie de plus d'un an d'emprisonnement, faire une **déclaration de soupçon à Tracfin**, sans en informer le client [V fiche commune § 2.3].

Pour les situations A et B, le cabinet doit donc documenter son analyse, conseiller la présidente de refuser et, si le soupçon persiste, faire une déclaration de soupçon à Tracfin, y compris pour une simple tentative d'opération, sans en informer le client [V fiche commune § 2.3]. Son **devoir de conseil** et sa déontologie le conduisent aussi à recommander les procédures de la situation C.

**Réponses tolérées** : toute conduite à tenir prudente et motivée ; la date de fin de la période transitoire de MiCA n'est pas exigée. Il n'est pas demandé de rattacher les faits à une infraction précise [V guide p. 62].

**Erreurs fréquentes**
- Considérer qu'ORVANE, société industrielle, est elle-même assujettie aux obligations de déclaration de soupçon : ce sont sa banque et son expert-comptable qui le sont.
- Croire que la déclaration de soupçon exige une preuve : un soupçon suffit.

---

### 3.4 Prêt à impact (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Effets annuels et sur cinq ans | 1,5 |
| 3.4-02 | Avantages | 0,5 |
| 3.4-03 | Risques et conclusion | 1 |

Effet annuel = 12 000 000 × (2,10 % − marge de l'année) − 6 000 € de vérification.

| € | Deux indicateurs atteints | Un seul | Aucun |
|---|---:|---:|---:|
| Écart de marge par rapport au prêt classique | + 12 000 | 0 | − 12 000 |
| Coût de la vérification | − 6 000 | − 6 000 | − 6 000 |
| **Effet annuel** | **+ 6 000** | **− 6 000** | **− 18 000** |
| **Effet sur cinq ans** | **+ 30 000** | **− 30 000** | **− 90 000** |

**Lecture.** L'enjeu financier est faible au regard des intérêts annuels de l'emprunt : la seule marge représente 12 000 000 × 2,10 % = 252 000 € par an, avant même l'Euribor. Le prêt n'est gagnant que si les **deux** indicateurs sont atteints, à cause du coût de la vérification.

**Avantages (0,5 pt)** :
- incitation à progresser sur des indicateurs matériels pour ORVANE, l'intensité carbone et la sécurité au travail ;
- crédibilité de ces engagements grâce à la vérification par un tiers ;
- signal adressé au fonds et cohérence avec sa grille de notation : les accidents du travail y sont un critère social ;
- relation renforcée avec la banque.

**Risques et conclusion (1 pt)** :
- surcoût si les objectifs sont manqués ;
- coût et charge de la collecte des données ;
- le taux de fréquence actuel des accidents n'est pas donné : il faut le connaître pour apprécier la difficulté de l'objectif ;
- risque d'**écoblanchiment** si les objectifs sont peu ambitieux. Une réduction de 5 % par an doit être comparée à la trajectoire du secteur.

À la différence d'un prêt vert, dont les fonds sont affectés à un projet, le prêt à impact finance l'entreprise en général et indexe sa marge sur des objectifs [F08 § 5]. Recommandation : l'accepter si ORVANE est en mesure d'atteindre les deux objectifs, et en faire un élément de son plan de progrès présenté au fonds.

**Erreur fréquente** : oublier le coût de la vérification, ou actualiser alors que l'énoncé l'exclut.

---

### 3.5 Hiérarchie des ordres (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Présentation des quatre ordres et des deux confusions | 1 |
| 3.5-02 | Application à la position du directeur commercial | 1,5 |
| 3.5-03 | Conclusion | 0,5 |

**La théorie (1 pt).** André Comte-Sponville distingue quatre ordres, chacun régi par sa propre logique et incapable de se limiter lui-même [F10 ; F09 § 1] :
1. l'ordre **techno-scientifique et économique** : le possible et l'impossible, le rentable ;
2. l'ordre **juridico-politique** : le légal et l'illégal ;
3. l'ordre **moral** : le bien et le mal, le devoir ;
4. l'ordre **éthique**, ou de l'amour.

Chaque ordre est limité par l'ordre supérieur. Deux confusions menacent :
- la **barbarie** : un ordre inférieur prétend régir un ordre supérieur ;
- l'**angélisme** : un ordre supérieur prétend remplacer un ordre inférieur.

L'économie n'est pas morale par elle-même : elle est amorale.

**Application (1,5 pt)**
- **Ordre économique** : le directeur commercial raisonne en chiffre d'affaires (6 000 k€) et en EBITDA (720 k€). Même sur ce terrain, l'argument est fragile : la commission de 540 k€ ramènerait l'EBITDA du contrat à 180 k€, sans compter le risque de sanctions, d'annulation du marché et d'échec de l'entrée du fonds.
- **Ordre juridique** : « ce qui se passe là-bas ne nous regarde pas » est inexact. Le droit français s'applique aux actes de corruption commis à l'étranger, et la prévention de la corruption fait partie des exigences des partenaires d'ORVANE. Faire dicter la règle par « la pratique du marché » revient à soumettre l'ordre juridique à l'ordre économique : c'est la **barbarie** au sens de Comte-Sponville.
- **Ordre moral** : même si aucune loi ne s'appliquait, verser un pot-de-vin détourne de l'argent public d'un hôpital et fausse la concurrence. Ce n'est pas à l'entreprise, abstraction amorale, mais à des personnes, la présidente et le directeur commercial, de se poser la question du devoir.
- **Ordre éthique** : ce que Mme VARENNE veut transmettre, une entreprise familiale réputée pour sa loyauté, et la confiance de ses salariés.
- **Angélisme** à éviter : il ne suffit pas de « bien se conduire » pour réussir à l'export. Il faut aussi des procédures (évaluation des tiers, contrats, contrôles) et une stratégie commerciale qui permette de gagner des marchés sans intermédiaire douteux.

**Conclusion (0,5 pt).** La décision relève de la responsabilité personnelle de la présidente, et non de la logique du marché. Il faut refuser l'agent dans ces conditions et chercher, si nécessaire, un intermédiaire évalué et rémunéré aux conditions usuelles. La conformité (question 3.2) donne le cadre, la morale et l'éthique donnent le sens.

**Réponses tolérées** : présentation des ordres dans un tableau ; les deux vocabulaires sont admis, celui de l'ouvrage (techno-scientifique, juridico-politique, moral, éthique) et celui du sujet zéro (économique, politique, moral, de l'amour) ; toute application pertinente de chaque ordre au cas.

**Erreurs fréquentes**
- `JUR-T14` — théorie méconnue ou ordres mal nommés ; oubli de l'ordre éthique.
- `JUR-T13` — récitation de la théorie sans application au cas.
- Moraliser en condamnant le directeur commercial au lieu d'analyser son raisonnement.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Loi n° 2016-1691 du 9 décembre 2016 (Sapin II), art. 17 | seuils, huit mesures, sanctions | [V] | fiche commune § 1.2 ; F09 § 4.2 |
| Lutte contre le blanchiment et le financement du terrorisme | assujettissement des experts-comptables, déclaration de soupçon | [V] | fiche commune § 2.2-2.3 |
| Règlement (UE) 2023/1114 (MiCA), art. 59 et 143 ; communiqué AMF du 06/07/2026 | agrément des prestataires, fin de la période transitoire | [V] | fiche commune § 3 |
| Guide pédagogique, juillet 2026, p. 60-63 | attendus de la partie 2.2, approche par les principes | [V] | F09 § 0 |
| A. Comte-Sponville, *Le capitalisme est-il moral ?* (2004) | hiérarchie des ordres, barbarie, angélisme | [S] | F10 ; F09 § 1 |
| Prêts indexés sur la durabilité | marge indexée sur des indicateurs, vérification par un tiers | [S] | F08 § 5 |
