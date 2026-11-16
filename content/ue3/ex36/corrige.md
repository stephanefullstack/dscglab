# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 3 – Contrôle de gestion et stratégie — Exercice d'entraînement n° 36 — Dossier 2 (7 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F05 pilotage des projets, F08 gestion des risques et contrôle interne, F13 registre des auteurs (toutes à jour au 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (planning, durée de coût total minimal et pas à pas de l'accélération, indicateurs du processus des redevances recalculés ; cotation des risques, effet de la ligne de secours, coût total par durée et contrôle des redevances : calculs divers recalculés par script ; barème partiel sur 7 ; liste noire ; hors-programme).

Bien que le corrigé mentionne des auteurs, des textes et des données, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur le choix et la justification des outils, la justesse des calculs, la pertinence de l'analyse au regard du cas et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet) ; pour chaque question, la présentation des concepts et outils avant leur mobilisation puis la conclusion sont notées. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Typologie des risques du réseau, cotation, criticité, hiérarchie, cartographie ; dépendance envers l'usine unique | `2.5.a` Identifier les risques rencontrés par l'organisation ; `2.5.b` Analyser les risques rencontrés par l'organisation | 1,5 |
| 2.2 Planning de la ligne de secours tiré du compte rendu ; durée de coût total minimal entre accélération et façonnage, pas à pas ; effet de la ligne sur la cotation des risques et limites | `2.2.b` Élaborer la planification du projet ; `2.2.d` Analyser les résultats obtenus | 2,5 |
| 2.3 Rapprochement du chiffre d'affaires déclaré et du café acheté, cafés anormaux, redevance manquante et limites ; processus des redevances au regard des composantes du contrôle interne et de la séparation des tâches ; contrôles et indicateurs | `2.5.c` Mettre en œuvre les outils de gestion des risques ; `2.3.a` Analyser la situation de gestion ; `2.3.f` Élaborer des préconisations afin de mieux piloter la performance des activités hors production | 1,5 |
| 2.4 Note à la présidente et au directeur administratif et financier (20 lignes au maximum) | `2.5.d` Élaborer des préconisations permettant de gérer les risques ; `2.2.e` Produire une synthèse rédigée et structurée concernant le pilotage du projet | 1,5 |
| **Dossier 2 – Sécuriser le réseau : cartographie des risques, seconde ligne de torréfaction et contrôle des redevances** | | **7** |

---

## DOSSIER 2 – SÉCURISER LE RÉSEAU : CARTOGRAPHIE DES RISQUES, SECONDE LIGNE DE TORRÉFACTION ET CONTRÔLE DES REDEVANCES (7 points)

### 2.1 Classer par type les risques du réseau, les coter, calculer leur criticité, les hiérarchiser, en présenter la cartographie et montrer ce qu'elle révèle de la dépendance envers l'usine unique (1,5 pt)

**Compétences visées :**
- `2.5.a` — Identifier les risques rencontrés par l'organisation (typologie : stratégiques, opérationnels, financiers, de conformité, d'image ; risques issus des incidents et des processus)
- `2.5.b` — Analyser les risques rencontrés par l'organisation (criticité = probabilité × gravité, échelles de cotation, hiérarchisation, matrice)

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Concepts présentés (risque comme événement incertain qui menace un objectif, typologie, probabilité, gravité, criticité, cartographie) ; chaque risque formulé comme un événement et classé par type, avec justification : stratégiques R3, R9 ; opérationnels R1, R2, R4, R6 ; financiers R5, R7, R8 ; de conformité R11 ; d'image R10 (variantes argumentées acceptées, voir ci-dessous) | 0,5 |
| 2.1-02 | Niveaux tirés des échelles de l'annexe 2.1 et criticités : **R1, R3 et R5 = 12** ; **R6 = 9** (critiques) ; R2, R7, R8 = 8 ; R4, R9 = 6 ; R10 = 4 (significatifs) ; R11 = 2 (faible) ; hiérarchie présentée (tableau trié ou matrice probabilité × gravité) | 0,5 |
| 2.1-03 | Lecture : trois des quatre risques critiques (panne longue R1, capacité R3, lot contaminé R6) et le seul autre risque de gravité 4 (incendie R2) viennent de l'**usine unique**, qui alimente les 148 cafés : un seul point de défaillance pour tout le réseau ; R1 et R2 ont la gravité maximale ; R5, critique, relève des achats et non de l'usine ; les risques liés aux franchisés (R7, R8, R9) sont significatifs mais très probables ; conclusion : priorité à la continuité de la torréfaction, puis au prix du café vert et aux redevances | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : la **cartographie des risques**. Chaque risque est identifié à partir des faits du cas, classé par type, puis coté en probabilité et en gravité sur les échelles de la société ; la **criticité** (probabilité × gravité) permet de les hiérarchiser, et la **matrice** probabilité × gravité les représente. C'est l'outil que le programme associe à l'analyse des risques (« notion de criticité »).
- Alternatives acceptées : tableau trié par criticité sans matrice, si la hiérarchie et les classes sont claires ; matrice orientée autrement (probabilité en lignes) ; typologie plus détaillée (risque d'approvisionnement, de qualité, de marché, de crédit, humain).

**Conventions rappelées** (annexes 2.1 et 2.5)

- Probabilité d'ici la fin de 2031 : 1 si moins de 10 %, 2 de 10 % à moins de 30 %, 3 de 30 % à moins de 60 %, 4 à partir de 60 %. Gravité selon la perte de résultat d'exploitation : 1 sous 250 k€, 2 de 250 à moins de 750 k€, 3 de 750 à moins de 1 500 k€, 4 à partir de 1 500 k€.
- Criticité = probabilité × gravité ; critique ≥ 9, significatif de 4 à 8, faible de 1 à 3.

**Réponse attendue**

*Concepts (2.1-01).* Un **risque** est un événement incertain qui, s'il survient, empêche l'organisation d'atteindre un de ses objectifs ; il se formule comme un événement (cause et conséquence), pas comme un thème. La **typologie** distingue les risques stratégiques (qui menacent le modèle de développement), opérationnels (qui touchent les processus), financiers (qui touchent les marges, les créances ou les revenus), de conformité (non-respect d'une règle) et d'image (atteinte à la réputation). La **cartographie** recense ces risques, les cote en **probabilité** et en **gravité** sur des échelles communes, calcule leur **criticité** (probabilité × gravité) et les représente sur une matrice. Elle sert à décider où agir en priorité.

*Classement et cotation (2.1-01 et 2.1-02).*

| Risque | Type | Probabilité | Niveau | Perte (k€) | Gravité | **Criticité** | Classe |
|---|---|---:|---:|---:|---:|---:|---|
| R1 Panne longue de la ligne principale | opérationnel | 40 % | 3 | 1 800 | 4 | **12** | critique |
| R3 Capacité de l'usine insuffisante pour la croissance | stratégique | 70 % | 4 | 1 000 | 3 | **12** | critique |
| R5 Nouvelle hausse du prix du café vert | financier | 60 % | 4 | 1 200 | 3 | **12** | critique |
| R6 Lot contaminé à retirer du réseau | opérationnel (qualité) | 35 % | 3 | 800 | 3 | **9** | critique |
| R2 Incendie qui arrête l'usine | opérationnel | 15 % | 2 | 4 000 | 4 | **8** | significatif |
| R7 Impayés et défaillances de franchisés | financier | 90 % | 4 | 400 | 2 | **8** | significatif |
| R8 Sous-déclaration du chiffre d'affaires | financier | 70 % | 4 | 300 | 2 | **8** | significatif |
| R4 Défaillance du principal négociant | opérationnel (approvisionnement) | 15 % | 2 | 900 | 3 | **6** | significatif |
| R9 Départ de franchisés vers une chaîne concurrente | stratégique | 50 % | 3 | 450 | 2 | **6** | significatif |
| R10 Atteinte à l'image de l'enseigne | d'image | 25 % | 2 | 600 | 2 | **4** | significatif |
| R11 Fermeture d'un café après un contrôle sanitaire | de conformité | 20 % | 2 | 60 | 1 | **2** | faible |

*Cartographie (matrice gravité × probabilité).*

| Gravité \ Probabilité | 1 (< 10 %) | 2 (10 à < 30 %) | 3 (30 à < 60 %) | 4 (≥ 60 %) |
|---|---|---|---|---|
| **4** (≥ 1 500 k€) | | R2 (8) | **R1 (12)** | |
| **3** (750 à < 1 500 k€) | | R4 (6) | **R6 (9)** | **R3, R5 (12)** |
| **2** (250 à < 750 k€) | | R10 (4) | R9 (6) | R7, R8 (8) |
| **1** (< 250 k€) | | R11 (2) | | |

*Lecture (2.1-03).*
- **L'usine unique concentre les risques les plus graves.** Trois des quatre risques critiques en viennent : la panne longue du torréfacteur (R1), la capacité qui manquera avant 2031 (R3) et le lot contaminé (R6), qui touche d'un coup les 41 cafés livrés. L'incendie (R2), peu probable, a la gravité la plus forte du registre (4 000 k€, sans assurance des pertes d'exploitation). Une seule usine alimente les 148 cafés, les clients professionnels et la vente en ligne : c'est un **point de défaillance unique**, aggravé par un délai de six semaines pour certaines pièces.
- **Le prix du café vert (R5)** est l'autre risque critique. Il vient des achats, faits lot par lot au prix du moment, et non de l'usine ; il pèse directement sur la marge, comme l'a montré la hausse de 38 % entre 2024 et 2026.
- **Les risques liés aux franchisés** (R7 impayés, R8 sous-déclaration, R9 départs) sont moins graves un par un, mais très probables : ils sont déjà en train de se produire. R8, et en partie R7 (délais de paiement accordés sans l'accord d'un responsable), relèvent d'un défaut de contrôle de la société elle-même (question 2.3).
- Conclusion : la priorité va à la **continuité de la torréfaction**, puis au prix du café vert et à la maîtrise des redevances. La conformité sanitaire (R11) peut être acceptée et suivie.

**Réponses tolérées**
- R3 classé comme risque opérationnel (capacité de production) et R4 comme stratégique (dépendance envers un fournisseur), si c'est justifié ; R5 classé comme risque de marché ou opérationnel (approvisionnement) ; R6 classé aussi comme risque d'image ; R8 classé comme risque de conformité (manquement des franchisés à leurs engagements) ; R7 classé comme risque stratégique (fragilité du réseau).
- Matrice présentée avec la probabilité en lignes, ou criticités présentées seulement dans un tableau trié, si la hiérarchie est juste.
- R2 jugé prioritaire malgré sa classe « significatif », au nom de sa gravité maximale, si l'argument est posé.

**Erreurs fréquentes**
- `JUR-P02` — Ne pas appliquer les échelles données : coter « au jugé », multiplier le pourcentage par la perte, ou prendre la perte en k€ comme gravité.
- `JUR-T03` — Recopier le registre sans lire la cartographie : ne pas voir que les risques de l'usine se concentrent en haut de la matrice.
- `JUR-T02` — Lister des risques génériques (« risque de marché », « risque humain ») au lieu des événements du cas.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.5 (cartographie des risques, types de risques, « notion de criticité ») ; guide p. 123 | typologie, cotation, matrice | [V] | F08 § 0, § 1, § 2 |
| Criticité = probabilité × gravité (pratique sans auteur) | cotation | [S] | F08 § 2.1 ; F13 § 6 |

---

### 2.2 Établir le planning de la ligne de secours, déterminer la durée de coût total minimal et son coût, apprécier l'effet de la ligne sur la cotation des risques et ses limites (2,5 pts)

**Compétences visées :**
- `2.2.b` — Élaborer la planification du projet (réseau ou diagramme de Gantt construit à partir d'un texte, dates au plus tôt et au plus tard, marges, chemin critique ; arbitrage coût-délai)
- `2.2.d` — Analyser les résultats obtenus (actions correctives, risques du projet et risques que le projet traite)

**Barème (2,5 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Concepts présentés (tâche, antériorité, date au plus tôt et au plus tard, marge totale et libre, chemin critique) ; tableau des antériorités tiré du texte, avec les antériorités multiples : **F après C et D** ; **G après E et F** ; **J après G et I** ; dates au plus tôt et au plus tard de chaque tâche (tableau ci-dessous) | 0,5 |
| 2.2-02 | Marges totales : D et E 3, H et I 6, les autres nulles (marges libres : E 3, I 6) ; durée **31 semaines**, chemin critique **A-B-C-F-G-J-K-L** ; fin le vendredi 3 décembre 2027, soit **5 semaines** après l'échéance du 29 octobre ; sans accélération, 5 × 12 = **60 k€** de façonnage | 0,5 |
| 2.2-03 | Pas à pas : F (4 k€, 30 semaines), C (5 k€, 29), C (5 k€, 28) ; à 28 semaines, deux chemins critiques (A-B-C-F-G-J-K-L et A-D-E-G-J-K-L) : C + D (11 k€) moins cher que C + E (13 k€) et que J (14 k€), et moins cher qu'une semaine de façonnage (12 k€) : **27 semaines** ; ensuite, seule J reste possible sur le premier chemin (14 k€ > 12 k€) : arrêt | 0,5 |
| 2.2-04 | **Durée de coût total minimal : 27 semaines** (fin le vendredi 5 novembre 2027, une semaine après l'échéance) ; accélération **25 k€** (C de 3 semaines, D et F d'une semaine) + façonnage **12 k€** = **37 k€**, contre 60 k€ sans accélération et 39 k€ pour tenir l'échéance (26 semaines) ; lecture : tenir l'échéance coûterait plus cher que la semaine de façonnage ; après accélération, toutes les tâches sauf H et I (2 semaines de marge) sont critiques : projet fragile | 0,5 |
| 2.2-05 | Effet sur les risques : la ligne réduit la **gravité** de R1 (perte de 1 800 à 600 k€ : criticité **12 → 6**) et de R2 (4 000 à 1 200 k€ : **8 → 6**), et la **probabilité** de R3 (70 % à 5 % : **12 → 3**) ; elle ne réduit pas la probabilité d'une panne ou d'un incendie ; ce qu'elle ne traite pas : R5 prix du café vert, R4 négociant (les deux lignes torréfient les mêmes cafés verts), R6 contamination (qualité du procédé), risques liés aux franchisés (R7 à R9), image (R10) ; limite majeure : si elle absorbe la croissance (184 t en 2031), elle ne couvre plus que **31,41 %** des besoins quand la ligne principale s'arrête (41,67 % en 2026) : secours et croissance se concurrencent | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **réseau des antécédents** (tâches, durées, antériorités), parcouru en avant pour les dates au plus tôt et en arrière, depuis la durée totale, pour les dates au plus tard, complété au besoin par un **diagramme de Gantt** pour le calendrier. Le compte rendu doit d'abord être transformé en tableau des antériorités (« construire des diagrammes à partir de données brutes (textes) »). Pour le délai, l'outil est l'**arbitrage coût-délai** : on raccourcit le chemin critique, semaine après semaine, par l'ensemble de tâches le moins cher qui raccourcit tous les chemins critiques, tant que ce coût reste inférieur à la semaine de façonnage évitée.
- Alternatives acceptées : réseau en tâches sur les nœuds (méthode des potentiels) ou sur les flèches (avec des tâches fictives correctement placées) ; Gantt seul s'il porte les dates au plus tard et les marges ; arbitrage présenté par un tableau du coût total pour chaque durée de 31 à 26 semaines, si le coût minimal d'accélération de chaque durée est justifié.

**Conventions rappelées** (annexes 2.2 et 2.5)

- Semaines entières ; date 0 = début de la semaine 1 (lundi 3 mai 2027) ; marge totale = début au plus tard − début au plus tôt ; marge libre = plus petit début au plus tôt des successeurs (ou fin du projet) − fin au plus tôt.
- Réduction par semaines entières jusqu'à la durée minimale ; coût total = accélération + 12 k€ par semaine au-delà de la fin de la semaine 26 ; durée de coût total minimal retenue.

**Réponse attendue**

*Concepts (2.2-01).* Le planning ordonne les tâches selon leurs antériorités. La **date au plus tôt** d'une tâche est la plus grande des fins au plus tôt de ses prédécesseurs ; la **date au plus tard** est la date à laquelle elle doit commencer pour ne pas retarder la fin du projet. La **marge totale** mesure le retard qu'une tâche peut prendre sans retarder le projet, la **marge libre** celui qu'elle peut prendre sans retarder aucun de ses successeurs. Le **chemin critique**, formé des tâches sans marge totale, fixe la durée du projet. **Accélérer** une tâche critique raccourcit le projet à un coût ; l'arbitrage compare ce coût à celui du retard.

*Planning (2.2-01 et 2.2-02).*

| Tâche | Durée | Antériorités | Début au plus tôt | Fin au plus tôt | Début au plus tard | Fin au plus tard | Marge totale | Marge libre |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| A Étude détaillée et cahier des charges | 4 | — | 0 | 4 | 0 | 4 | **0** | 0 |
| B Choix du fournisseur et commande | 3 | A | 4 | 7 | 4 | 7 | **0** | 0 |
| C Fabrication et livraison du torréfacteur | 12 | B | 7 | 19 | 7 | 19 | **0** | 0 |
| D Aménagement de la zone de l'entrepôt | 9 | A | 4 | 13 | 7 | 16 | 3 | 0 |
| E Silos et convoyeurs | 6 | D | 13 | 19 | 16 | 22 | 3 | 3 |
| F Montage du torréfacteur | 3 | C, D | 19 | 22 | 19 | 22 | **0** | 0 |
| G Raccordements et essais à vide | 2 | E, F | 22 | 24 | 22 | 24 | **0** | 0 |
| H Recrutement des opérateurs | 8 | A | 4 | 12 | 10 | 18 | 6 | 0 |
| I Formation sur la ligne principale | 6 | H | 12 | 18 | 18 | 24 | 6 | 6 |
| J Essais de torréfaction et réglage des profils | 3 | G, I | 24 | 27 | 24 | 27 | **0** | 0 |
| K Validation par la qualité | 2 | J | 27 | 29 | 27 | 29 | **0** | 0 |
| L Montée en cadence | 2 | K | 29 | 31 | 29 | 31 | **0** | 0 |

| Chemin | Durée (semaines) |
|---|---:|
| A-B-C-F-G-J-K-L | **31** (critique) |
| A-D-E-G-J-K-L | 28 |
| A-D-F-G-J-K-L | 25 |
| A-H-I-J-K-L | 25 |

Le projet dure **31 semaines** : la ligne serait en service le vendredi 3 décembre 2027, **5 semaines** après l'échéance du 29 octobre, en pleine saison des fêtes. Le chemin critique passe par la fabrication du torréfacteur (12 semaines chez un fournisseur extérieur). Sans accélération, le façonnage coûterait 5 × 12 = **60 k€**.

*Durée de coût total minimal (2.2-03 et 2.2-04).*

| Étape | Chemins critiques | Possibilités (coût d'une semaine) | Choix | Coût de l'étape (k€) | Durée | Accélération cumulée (k€) | Façonnage (k€) | **Coût total (k€)** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 0 | A-B-C-F-G-J-K-L (31) | — | — | — | 31 | 0 | 60 | **60** |
| 1 | A-B-C-F-G-J-K-L (31) | F 4, C 5, J 14 | F | 4 | 30 | 4 | 48 | **52** |
| 2 | A-B-C-F-G-J-K-L (30) | C 5, J 14 | C | 5 | 29 | 9 | 36 | **45** |
| 3 | A-B-C-F-G-J-K-L (29) | C 5, J 14 | C | 5 | 28 | 14 | 24 | **38** |
| 4 | A-B-C-F-G-J-K-L et A-D-E-G-J-K-L (28) | C + D 11, C + E 13, J 14 | C + D | 11 | 27 | 25 | 12 | **37** |
| (5) | les deux mêmes (27) | J 14 (C et F à leur minimum) | — | 14 | 26 | 39 | 0 | 39 |

À chaque étape, on gagne une semaine au moindre coût sur **tous** les chemins critiques. À 28 semaines, le chemin de l'aménagement (A-D-E-G-J-K-L) devient critique : il faut raccourcir les deux chemins à la fois. C + D coûte 11 k€, moins qu'une semaine de façonnage : on la gagne. Ensuite, C et F sont à leur durée minimale ; seule J, commune aux deux chemins, peut encore être raccourcie, pour 14 k€, plus que les 12 k€ de façonnage évités : on s'arrête.

**Durée retenue : 27 semaines**, fin le vendredi 5 novembre 2027. Coût d'accélération **25 k€** (fabrication prioritaire du torréfacteur : 3 semaines, 15 k€ ; équipe de travaux renforcée : 1 semaine, 6 k€ ; seconde équipe de monteurs : 1 semaine, 4 k€) ; une semaine de façonnage, **12 k€** ; **coût total 37 k€**, soit 23 k€ de moins que sans accélération et 2 k€ de moins que s'il fallait tenir l'échéance (39 k€). Ce surcoût représente 1,61 % du budget du projet (2 300 k€). Lecture : l'échéance n'est pas un dogme ; tenir le 29 octobre coûterait plus cher que de faire torréfier 20 tonnes à façon pendant une semaine. Mais après accélération, toutes les tâches sont critiques sauf le recrutement et la formation (2 semaines de marge) : le moindre retard du fabricant ou des travaux coûtera 12 k€ par semaine. Il faut donc suivre de près la fabrication du torréfacteur et lancer le recrutement à sa date au plus tôt.

*Effet sur les risques et limites (2.2-05).*

| Risque | Avant la ligne | Avec la ligne | Ce qui change |
|---|---|---|---|
| R1 Panne longue | P 3 × G 4 = **12** (critique) | P 3 × G 2 = **6** (significatif) | gravité : perte de 1 800 à 600 k€ |
| R2 Incendie de l'usine | P 2 × G 4 = **8** | P 2 × G 3 = **6** | gravité : perte de 4 000 à 1 200 k€, entrepôt distinct |
| R3 Capacité insuffisante | P 4 × G 3 = **12** (critique) | P 1 × G 3 = **3** (faible) | probabilité : 70 % à 5 %, capacité de 4 000 t |

- La ligne est une mesure de **réduction** : elle ne rend ni la panne ni l'incendie moins probables, elle en réduit la gravité ; elle supprime en revanche presque le risque de capacité.
- **Ce qu'elle ne traite pas** : le prix du café vert (R5, critique), la défaillance du négociant (R4 : les deux lignes torréfient les mêmes cafés verts), la contamination d'un lot (R6, critique : elle relève du contrôle de la qualité, et une nouvelle ligne ajoute même un risque de réglage au démarrage), les risques liés aux franchisés (R7 à R9) et à l'image (R10).
- **Limite majeure.** Si le réseau grandit comme prévu, la ligne principale tournera à pleine capacité en 2031 et la ligne de secours torréfiera 3 184 − 3 000 = **184 t**. En cas d'arrêt de la ligne principale, elle ne couvrira que 1 000 / 3 184 = **31,41 %** des besoins, contre 41,67 % en 2026. Plus elle sert la croissance, moins elle sert de secours : la gravité de R1 remontera à mesure que le réseau grandira. Il faudra donc compléter la ligne par d'autres mesures : stock des pièces critiques (brûleur, tambour), accord préalable avec un torréfacteur à façon, assurance des pertes d'exploitation.

Conclusion : retenir une durée de 27 semaines pour 37 k€ de surcoût ; la ligne ramène deux risques critiques sur trois liés à l'usine au niveau significatif ou faible, mais elle ne suffit ni pour le prix du café vert, ni pour la qualité, ni pour les franchisés.

**Réponses tolérées**
- Semaines numérotées de 1 à 31 au lieu des dates à partir de 0, si l'écriture est cohérente.
- Arbitrage présenté par un tableau des coûts totaux de 31 à 26 semaines sans pas à pas, si le coût minimal d'accélération de chaque durée est juste (0, 4, 9, 14, 25, 39 k€).
- Étapes 2 et 3 regroupées (C raccourcie de 2 semaines pour 10 k€), si le raisonnement par semaine reste visible.
- Limite de la ligne exprimée autrement (part couverte calculée sur 3 000 t, ou capacité restante de 816 t en 2031), si l'idée de concurrence entre secours et croissance est posée.

**Erreurs fréquentes**
- `JUR-T10` — Oublier une antériorité multiple (F après C **et** D ; G après E **et** F ; J après G **et** I) ; calculer les dates au plus tard sans repartir de la durée totale ; confondre marge totale et marge libre.
- `JUR-T10` — Accélérer jusqu'à l'échéance quoi qu'il en coûte (39 k€ au lieu de 37 k€), ou s'arrêter à 28 semaines sans voir que C + D (11 k€) coûte moins qu'une semaine de façonnage ; raccourcir un seul des deux chemins critiques à la 4e étape ; accélérer J dès la 1re étape parce qu'elle est sur tous les chemins.
- `JUR-T05` — Présenter la ligne comme une solution à tous les risques, sans voir qu'elle réduit la gravité et non la probabilité, ni qu'elle perd son rôle de secours en absorbant la croissance.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (« construire des diagrammes à partir de données brutes (textes) » ; Gantt, marges, jalons, chemin critique ; triptyque QCD ; risques du projet) | planning | [V] | F05 § 0, § 4 |
| `ue3/00_LISEZMOI.md`, conventions d'ordonnancement et d'arbitrage coût-délai ; marge libre : formule de cours | dates, marges, durée de coût total minimal | [V] ; [S] marge libre | F05 § 1 |
| Diagramme de Gantt (Henry L. Gantt, années 1910) | lecture calendaire | [V] programme ; [S] origine | F13 § 8 |
| Programme UE 3, partie 2.5 ; traitement des risques (réduire, transférer, éviter, accepter) | effet de la ligne sur la cotation | [V] ; [S] | F08 § 2.1 |

---

### 2.3 Rapprocher le chiffre d'affaires déclaré et le café acheté, repérer les cafés anormaux, estimer la redevance manquante et ses limites ; analyser le processus des redevances au regard des composantes du contrôle interne ; proposer des contrôles et des indicateurs (1,5 pt)

**Compétences visées :**
- `2.5.c` — Mettre en œuvre les outils de gestion des risques (contrôle interne : objectifs, composantes du COSO, séparation des tâches, positionnement par rapport au contrôle de gestion)
- `2.3.a` — Analyser la situation de gestion (processus administratif de facturation et d'encaissement des redevances)
- `2.3.f` — Élaborer des préconisations afin de mieux piloter la performance des activités hors production (contrôles et indicateurs du processus)

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Ratios des dix cafés (tableau ci-dessous) ; cafés **3 (55,75), 7 (54,05) et 9 (58,82)** sous le seuil de 60,00 € par kg ; chiffre d'affaires estimé 820,0, 740,0 et 850,0 k€ ; non déclaré **180,0 + 180,0 + 150,0 = 510,0 k€** ; redevance manquante **10,8 + 10,8 + 9,0 = 30,6 k€** (6,63 % de la redevance déclarée par l'échantillon) ; limites : ratio moyen de cafés en propre, mieux placés et à l'offre différente ; vente de café en grains (café 5, à 64,29, sous la référence mais au-dessus du seuil) ; stocks et pertes ; seuil conventionnel ; échantillon de dix cafés ; une **présomption** à examiner avec le franchisé, pas une preuve | 0,5 |
| 2.3-02 | Analyse au regard des cinq composantes du contrôle interne (COSO, 2013) : environnement de contrôle (pas de procédure écrite, pas de responsabilités définies, aucune suppléance), évaluation des risques (sous-déclaration jamais évaluée), activités de contrôle (**fonctions incompatibles cumulées** par la comptable : enregistrement, facturation, encaissement, autorisation des délais ; aucun rapprochement ; délais sans accord), information et communication (les animateurs ne transmettent rien ; le DAF ne reçoit qu'un total trimestriel), pilotage (aucun indicateur, aucune revue) ; constats appuyés sur les chiffres de 2026 de l'annexe 2.3 (381 déclarations en retard sur 1 524, 487 k€ impayés depuis plus de 60 jours sur 6 492 k€ facturés, aucun des 46 délais soumis à un responsable), en valeur ou en pourcentage (25,00 %, 7,50 %, 0 %) | 0,5 |
| 2.3-03 | Contrôles proposés, rattachés aux composantes : rapprochement mensuel ou trimestriel du chiffre d'affaires déclaré et du café acheté, avec alerte sous le seuil et examen par l'animateur et le DAF ; séparation des fonctions (saisie et facturation / encaissement / autorisation des délais par le DAF / contrôle) ; relances à dates fixes ; procédure écrite et suppléance ; fiche de visite des animateurs transmise à la comptabilité ; deux ou trois indicateurs avec formule et cible (par exemple taux de déclarations en retard, part des impayés à plus de 60 jours, nombre de cafés sous le seuil, part des délais validés, redevance récupérée après examen) ; coût des contrôles à mettre en regard des 30,6 k€ de l'échantillon (l'ordre de grandeur pour le réseau, environ 375 à 400 k€, est valorisé, non exigé) | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : un **contrôle de vraisemblance** par rapprochement de deux données indépendantes, le chiffre d'affaires déclaré par le franchisé et le café que la société lui a facturé, ramenées à un ratio et comparées à une référence et à un seuil d'alerte. Il est complété par une **analyse du processus** selon les cinq composantes du référentiel de contrôle interne du COSO (2013) et par l'examen de la **séparation des tâches**, puis par des **indicateurs** de pilotage du processus.
- Alternatives acceptées : ratio inverse (kg de café par millier d'euros déclaré, référence 14, anormal au-dessus de 16,67) si le seuil est converti de façon cohérente ; grille de séparation des tâches (fonctions × personnes) à la place de l'analyse par composantes, si les cinq composantes sont au moins citées.

**Conventions rappelées** (annexes 2.4 et 2.5)

- Ratio = chiffre d'affaires déclaré (€) / café acheté (kg), à deux décimales ; référence 71,43 € par kg ; anormal sous 60,00 € par kg.
- Chiffre d'affaires estimé (k€) = kg / 14 ; non déclaré = estimé − déclaré ; redevance manquante = 6 % du non déclaré ; k€ à une décimale.

**Réponse attendue**

*Concepts.* Le **contrôle interne** est, selon le COSO (2013), un processus mis en œuvre par la direction et le personnel pour donner une assurance raisonnable que l'organisation atteint ses objectifs d'opérations, de reporting et de conformité ; il s'organise en cinq composantes (environnement de contrôle, évaluation des risques, activités de contrôle, information et communication, pilotage). La **séparation des tâches** interdit qu'une même personne cumule des fonctions incompatibles : autoriser, enregistrer, détenir ou encaisser, contrôler. Le contrôle interne vise la **maîtrise** du processus ; le contrôle de gestion vise le **pilotage** de la performance. Ici, le contrôle de gestion repère une anomalie par un ratio ; le contrôle interne doit rendre le processus fiable pour qu'elle ne se reproduise pas.

*Rapprochement (2.3-01).*

| Café | Chiffre d'affaires déclaré (k€) | Café acheté (kg) | **Ratio (€ par kg)** | Écart à la référence | Anormal | Chiffre d'affaires estimé (k€) | Non déclaré (k€) | **Redevance manquante (k€)** |
|---|---:|---:|---:|---:|---|---:|---:|---:|
| 1 | 980 | 13 230 | 74,07 | + 3,70 % | | | | |
| 2 | 760 | 10 500 | 72,38 | + 1,33 % | | | | |
| 3 | 640 | 11 480 | **55,75** | − 21,95 % | oui | 820,0 | 180,0 | **10,8** |
| 4 | 870 | 11 650 | 74,68 | + 4,55 % | | | | |
| 5 | 720 | 11 200 | 64,29 | − 10,00 % | | | | |
| 6 | 905 | 12 320 | 73,46 | + 2,84 % | | | | |
| 7 | 560 | 10 360 | **54,05** | − 24,32 % | oui | 740,0 | 180,0 | **10,8** |
| 8 | 815 | 11 060 | 73,69 | + 3,16 % | | | | |
| 9 | 700 | 11 900 | **58,82** | − 17,65 % | oui | 850,0 | 150,0 | **9,0** |
| 10 | 740 | 10 220 | 72,41 | + 1,37 % | | | | |
| **Total** | **7 690** | **113 920** | 67,50 | | **3 cafés** | | **510,0** | **30,6** |

Exemple : café 3 : 640 000 / 11 480 = 55,75 € par kg ; chiffre d'affaires estimé = 11 480 / 14 = 820,0 k€ ; non déclaré = 820,0 − 640 = 180,0 k€ ; redevance manquante = 6 % × 180,0 = 10,8 k€.

Trois cafés sur dix sont anormaux. Leur sous-déclaration estimée est de 510,0 k€ de chiffre d'affaires, soit **30,6 k€ de redevance** manquante, 6,63 % de la redevance déclarée par l'échantillon (461,4 k€). Les sept autres cafés sont proches de la référence, sauf le café 5 (64,29 €, − 10,00 %), que l'animateur explique par ses ventes de café en grains : il reste au-dessus du seuil. Valorisé, non exigé : appliquée aux 122 cafés franchisés ouverts avant 2026, parmi lesquels l'échantillon a été tiré, la proportion de l'échantillon donnerait un ordre de grandeur de 30,6 / 10 × 122 = **373,3 k€** de redevance manquante par an (403,9 k€ si l'on retient les 132 cafés, base tolérée), plus que les 300 k€ estimés au registre (R8), mais sous le seuil de gravité 3.

*Limites de l'estimation.*
- La **référence** est une moyenne des seize cafés en propre : leurs emplacements, leur offre et leur clientèle peuvent différer de ceux des cafés franchisés (part des boissons, de la restauration, du café en grains), et la moyenne cache elle-même une dispersion.
- Un café qui **vend beaucoup de café en grains** a un ratio plus bas sans rien cacher (café 5). Les **stocks** (achats de décembre pour janvier), les pertes et le café offert faussent aussi le rapprochement sur une année.
- Le **seuil** de 60,00 € par kg (84 % de la référence) est conventionnel : un seuil plus haut repérerait aussi le café 5. À l'inverse, un franchisé qui achèterait du café ailleurs, contrairement à son engagement, échapperait au contrôle : la sous-déclaration serait alors sous-estimée.
- **Dix cafés** seulement, qui déclarent en moyenne 769 k€, moins que la moyenne du réseau (108,2 M€ / 132 = 820 k€) : l'extrapolation au réseau est fragile et n'est qu'un ordre de grandeur.
- Le ratio fournit une **présomption**, pas une preuve : il désigne les cafés à examiner avec leur franchisé, au cours d'une visite, à partir de ses propres relevés.

*Analyse du processus (2.3-02).*

| Composante du contrôle interne | Constat (annexe 2.3) | Conséquence |
|---|---|---|
| Environnement de contrôle | aucune procédure écrite ; responsabilités non définies ; une seule personne connaît le dossier, sans suppléance ; les animateurs voient leur rôle comme un soutien, pas comme un contrôle | dépendance envers une personne ; aucune culture du contrôle des redevances |
| Évaluation des risques | la sous-déclaration n'a jamais été évaluée (R8 coté pour la première fois en janvier 2027) ; les délais accordés ne sont pas reliés au risque d'impayé (R7) | le risque grandit sans être mesuré |
| Activités de contrôle | **la même personne enregistre, facture, encaisse et autorise les délais** : fonctions incompatibles ; aucun rapprochement avec les achats de café ; aucune pièce justificative ; aucun délai validé (0 sur 46) ; relances irrégulières | erreurs et omissions non détectées ; aucune barrière contre une sous-déclaration ou un délai de complaisance |
| Information et communication | les animateurs, qui voient l'activité réelle, ne transmettent rien ; les ventes de café aux franchisés, connues de la société, ne sont pas exploitées ; le DAF ne reçoit qu'un total trimestriel | l'information existe mais ne circule pas |
| Pilotage | aucun indicateur ; aucune revue du processus | dérive constatée trop tard : **25,00 %** des déclarations en retard (381 / 1 524), **7,50 %** des redevances impayées depuis plus de 60 jours (487 / 6 492), **0 %** des délais validés |

Le cumul des fonctions n'accuse pas la comptable : il prive la société de toute vérification croisée. Le processus est un **processus support** (administratif) dont la défaillance coûte du chiffre d'affaires (redevances non facturées) et de la trésorerie (impayés).

*Contrôles et indicateurs proposés (2.3-03).*
- **Activités de contrôle.** Rapprochement trimestriel, puis mensuel, du chiffre d'affaires déclaré et du café facturé à chaque café, avec alerte automatique sous 60,00 € par kg (contrôle de vraisemblance) ; examen des cafés en alerte par l'animateur et le DAF, avec le franchisé, à partir de ses relevés de ventes. **Séparation des fonctions** : saisie et facturation par la comptable, encaissements enregistrés par une autre personne de la direction financière, délais de paiement autorisés par le DAF au-delà d'un montant fixé, contrôle par le contrôle de gestion. Relances à dates fixes (J + 5, J + 15, puis appel de l'animateur).
- **Environnement de contrôle.** Procédure écrite ; suppléance organisée ; mission de l'animateur précisée (accompagner **et** signaler les écarts).
- **Information et communication.** Fiche de visite des animateurs transmise à la comptabilité ; rapport mensuel au DAF par café.
- **Pilotage : indicateurs du processus.**

| Indicateur | Formule | Valeur 2026 | Cible proposée | Sens |
|---|---|---:|---:|---|
| Taux de déclarations reçues après le 10 du mois | déclarations en retard / déclarations reçues × 100 | 25,00 % | 5 % | à la baisse |
| Part des redevances impayées depuis plus de 60 jours | redevances échues depuis plus de 60 jours / redevances de l'année × 100 | 7,50 % | 2 % | à la baisse |
| Part des délais de paiement autorisés par un responsable | délais validés / délais accordés × 100 | 0 % | 100 % | à la hausse |
| Part des cafés rapprochés dans le trimestre | cafés rapprochés / cafés franchisés × 100 | 0 % | 100 % | à la hausse |
| Cafés sous le seuil d'alerte | nombre de cafés dont le ratio est inférieur à 60,00 € par kg | 3 sur 10 dans l'échantillon | en baisse | à la baisse |
| Redevance récupérée après examen | redevance facturée en plus après examen (k€) | — | suivi | à la hausse |

- **Coût et bénéfice.** Le rapprochement utilise des données déjà connues (factures de café) et ne coûte presque rien ; la séparation des fonctions demande quelques heures par mois d'une autre personne. Face à 30,6 k€ de redevance manquante sur dix cafés et à un ordre de grandeur de 375 à 400 k€ pour le réseau, ces contrôles sont rentables.

Conclusion : la sous-déclaration se repère à faible coût par le rapprochement avec le café acheté ; elle s'explique par un processus sans séparation des fonctions ni circulation de l'information. Il faut d'abord séparer les fonctions et organiser le rapprochement, puis piloter le processus par quelques indicateurs.

**Réponses tolérées**
- Ratio inverse en kg par millier d'euros (anormaux : cafés 3, 7, 9, au-dessus de 16,67 kg), si les conclusions sont les mêmes.
- Chiffre d'affaires estimé calculé par kg × 71,43 € (820,02 k€ au lieu de 820,0 pour le café 3), si l'écart d'arrondi est signalé.
- Café 5 proposé pour un examen, au nom d'un seuil plus prudent, s'il n'est pas compté dans la redevance manquante sans justification.
- Cibles différentes des indicateurs, si elles sont justifiées.

**Erreurs fréquentes**
- `JUR-P02` — Calculer le ratio à l'envers sans convertir le seuil ; estimer le chiffre d'affaires non déclaré de tous les cafés sous la référence, au lieu des seuls cafés sous le seuil.
- `JUR-T03` — Conclure à une fraude établie ou proposer des sanctions, au lieu de traiter le ratio comme une alerte à examiner ; ne pas discuter les limites de la référence.
- `JUR-T10` — Réciter les cinq composantes ou les dix-sept principes du COSO sans les appliquer au processus ; confondre contrôle interne et contrôle de gestion.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| COSO, *Internal Control—Integrated Framework*, 1992, révisé en 2013 : cinq composantes, dix-sept principes | composantes du contrôle interne | [V] composantes et principes ; [S] définition | F08 § 3.1, § 3.2 ; F13 § 6 |
| Positionnement du contrôle interne par rapport au contrôle de gestion | maîtrise et pilotage | [S] | F08 § 3.4 |
| Programme UE 3, partie 2.3 (pilotage des processus support, dont administratifs) et partie 2.5 (contrôle interne, principes du COSO) | processus des redevances, contrôles, indicateurs | [V] | F08 § 0, § 5 |
| `ue3/00_LISEZMOI.md`, convention des indicateurs | valeur, cible, sens | [V] | F12 |

---

### 2.4 Note à Mme TERVAUDAN et à M. BARNIÈRE (20 lignes au maximum) (1,5 pt)

**Compétences visées :**
- `2.5.d` — Élaborer des préconisations permettant de gérer les risques (préconisations hiérarchisées selon la criticité : éviter, réduire, transférer, accepter)
- `2.2.e` — Produire une synthèse rédigée et structurée concernant le pilotage du projet (décision de durée et de coût, conditions de suivi)

**Barème (1,5 pt)** — grille de notation d'une réponse rédigée (six critères : concept défini et attribué ; mobilisation pertinente ; faits du cas ; analyse et non description ; préconisation faisable ; forme et longueur).

| Note | Descripteur |
|---:|---|
| 0 | Absence de réponse, hors sujet ou cours récité sans aucun fait du cas |
| 0,5 | Note qui résume les calculs sans prise de position, ou qui dépasse nettement les 20 lignes |
| 1 | Risques majeurs, ligne de secours et redevances présentés avec leurs chiffres clés, mais sans traitement par type de réponse (éviter, réduire, transférer, accepter), sans décision chiffrée sur la ligne ou sans risques résiduels à suivre |
| 1,5 | Six critères satisfaits : note structurée (objet, risques et traitements, ligne de secours, redevances, risques à suivre, conclusion) ; chiffres clés repris sans recalcul (quatre risques critiques dont trois liés à l'usine ; 27 semaines, 25 k€ d'accélération, 37 k€ de surcoût ; criticités ramenées à 6, 6 et 3 ; trois cafés anormaux, 30,6 k€) ; traitements adaptés à chaque risque critique ; limite de la ligne (secours et croissance) ; 20 lignes au maximum |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : une **note de décision** organisée selon le **plan de traitement des risques** (éviter, réduire, transférer, accepter), hiérarchisé selon la criticité, avec la décision sur le projet (durée, coût) et un dispositif de suivi.
- Alternatives acceptées : tableau des risques (risque, traitement, responsable, indicateur) avec phrases de liaison et conclusion ; décision de tenir l'échéance de 26 semaines si le surcoût de 2 k€ est assumé au nom de la marge de sécurité pour la saison des fêtes.

**Réponse attendue** (modèle de note, 20 lignes au maximum)

**Objet : sécurisation du réseau, ligne de secours et redevances.**

**1. Risques majeurs.** Quatre risques sont critiques : panne longue de la ligne principale, capacité qui manquera vers 2030, nouvelle hausse du café vert, lot contaminé. Trois viennent de l'usine unique, qui reste notre point de défaillance pour 148 cafés.

**2. Traitements.** Réduire la panne et l'incendie par la ligne de secours, un stock de pièces critiques et un accord préalable avec un torréfacteur à façon ; transférer la perte d'exploitation par une assurance ; réduire le risque de prix par des contrats d'achat à prix fixé avec les négociants, un stock de cafés verts et une répercussion partielle sur les prix ; rééquilibrer les achats entre les trois négociants (le premier fournit 55 %) limiterait notre dépendance ; contrôler chaque lot avant expédition. Accepter le risque sanitaire, faible, sous surveillance.

**3. Ligne de secours.** À lancer le 3 mai : 27 semaines (5 novembre), 25 k€ d'accélération et une semaine de façonnage (12 k€), soit 37 k€ au lieu de 60 k€ ; tenir le 29 octobre coûterait 39 k€. Elle ramène la panne à 6, l'incendie à 6, la capacité à 3.

**4. Redevances.** Trois cafés sur dix déclarent moins que leur café ne le laisse supposer : 30,6 k€ de redevance manquante, près de 400 k€ sur le réseau. Séparer saisie, encaissement et délais ; rapprocher chaque trimestre ventes déclarées et café acheté ; suivre retards et impayés.

**5. À suivre.** Prix du café vert, franchisés fragiles, et la ligne elle-même : en 2031, absorbant la croissance, elle ne couvrira que 31 % des besoins en cas de panne.

**Conclusion.** Décider la ligne et les contrôles en avril ; prévoir dès 2028 la capacité de 2031.

*Éléments attendus dans la note.*
- **Traitement par type de réponse.** Éviter (renoncer à l'activité qui crée le risque : par exemple, ne pas ouvrir plus de cafés que l'usine ne peut en servir tant que la ligne n'est pas en service) ; réduire (ligne de secours, pièces, contrôle des lots, contrôles des redevances) ; transférer (assurance des pertes d'exploitation, accord de façonnage) ; accepter (R11, et le risque résiduel une fois les mesures prises).
- **Décision sur le projet.** Durée de 27 semaines et coût total de 37 k€, conditions de suivi : fabrication du torréfacteur, travaux et recrutement, qui sont critiques ou presque.
- **Risques résiduels.** Prix du café vert, franchisés (impayés, départs), image, et la concurrence entre secours et croissance pour la nouvelle ligne.

**Réponses tolérées**
- Décision de tenir l'échéance (26 semaines, 39 k€), si l'écart de 2 k€ est présenté comme le prix d'une marge de sécurité.
- Recommandation d'une capacité supplémentaire plus importante pour 2031, si elle est reliée aux 3 184 t prévues, sans calcul de rentabilité.

**Erreurs fréquentes**
- `JUR-T05` — Traiter les risques, le projet et les redevances séparément, sans les relier à la cartographie.
- `JUR-T06` — Dépasser les 20 lignes ; absence de structure ou de conclusion.
- `JUR-T03` — Résumer les calculs sans traitement des risques ni décision sur la ligne.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.5 ; guide p. 123 (préconisations hiérarchisées selon la criticité) | plan de traitement | [V] | F08 § 2.1, § 5 |
| Programme UE 3, partie 2.2 (reporting du projet) | décision de durée et de coût | [V] | F05 § 7 |
| Grille à six critères des réponses rédigées | notation | [V] | gabarits/corrige_ue3_template.md ; bareme_grille.yaml |

---

## Contrôles avant publication

- [x] `python3 -I outils/dscgcheck ue3/exercices/ex36_risques_usine_unique_redevances/corrige.yaml` : 0 erreur, 0 avertissement ; planning, durée de coût total minimal et pas à pas, indicateurs du processus recalculés ; cotation des risques, effet de la ligne, coût total par durée et contrôle des redevances : calculs divers recalculés par script (`/paperclip/shared/dscglab-travail/DSC-879/calculs.py`, qui énumère aussi tous les plans d'accélération) ; barème partiel sur 7 ; liste noire ; hors-programme.
- [x] Données partagées du sujet n° 13 respectées : usine unique de 3 000 t pour 2 400 t, redevance de 6 %, 108,2 M€ déclarés, 132 cafés franchisés ; cohérence avec le dossier 1 : 14 kg de café par millier d'euros de chiffre d'affaires, 3 184 t en 2031 (106,13 % de la capacité), 122 cafés franchisés ouverts avant 2026, trois fermetures et 22 cafés sous 3 % de résultat en 2026 ; présentation commune reprise mot pour mot.
- [x] Compétences visées présentes dans `programme/perimetre_ue3.yaml` ; aucun outil prescrit dans l'énoncé ; chaque question présente le concept, l'applique au cas, conclut ; synthèse bornée (2.4, 20 lignes au maximum).
- [x] Entités et personnes fictives (M. Lionel FAVRESSE, M. Kévin TALOIRE, Mme Nadège ROUVERAND, M. Florent QUIRIEUX ; négociants, fabricant, entreprise de travaux et torréfacteur à façon non nommés) ; aucun chiffre réel du café ni texte réel sur l'hygiène des aliments ou les rappels de produits ; ni financement ni rentabilité du projet ; aucun instrument financier pour le prix du café vert ; aucune qualification juridique ni sanction de la sous-déclaration.
