# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 1 — Dossier 1 (20 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F08 gouvernance et ESG, F10 auteurs (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (coût du capital, DCF, multiples, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des auteurs et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

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
