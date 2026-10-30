# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 3 – Contrôle de gestion et stratégie — Exercice d'entraînement n° 13 — Dossier 2 (10 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F05 pilotage des projets, F06 pilotage des processus support, F12 pilotage de la performance globale, F13 registre des auteurs (toutes à jour au 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (planning initial et planning mis à jour, valeur acquise, plan d'accélération optimal recalculé exactement, indicateurs du bureau d'études ; calculs divers recalculés par script ; barème partiel sur 10 ; liste noire ; hors-programme).

Bien que le corrigé mentionne des auteurs, des textes et des données, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur le choix et la justification des outils, la justesse des calculs, la pertinence de l'analyse au regard du cas et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet) ; pour chaque question, la présentation des concepts et outils avant leur mobilisation puis la conclusion sont notées. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Planning initial : dates, marges, durée, chemin critique, date du salon | `2.2.b` Élaborer la planification du projet | 2 |
| 2.2 Revue d'avancement : écarts, indices, coût final estimé, estimation à retenir | `2.2.c` Réaliser un suivi de l'avancement et des coûts du projet ; `2.2.d` Analyser les résultats obtenus | 1,5 |
| 2.3 Planning mis à jour, plan d'accélération le moins coûteux, semaine de marge, enjeu commercial et risques QCD | `2.2.b` Élaborer la planification du projet ; `2.2.d` Analyser les résultats obtenus | 2,5 |
| 2.4 Bureau d'études : charge, capacité, coût horaire, indicateurs, préconisations | `2.3.a` Analyser la situation de gestion ; `2.3.f` Élaborer des préconisations afin de mieux piloter la performance des activités hors production | 2 |
| 2.5 Note au comité de pilotage (20 lignes au maximum) | `2.2.e` Produire une synthèse rédigée et structurée concernant le pilotage du projet ; `2.3.g` Produire une synthèse rédigée et structurée concernant les décisions liées aux processus support | 2 |
| **Dossier 2 – Piloter le projet du prototype et le bureau d'études** | | **10** |

---

## DOSSIER 2 – PILOTER LE PROJET DU PROTOTYPE ET LE BUREAU D'ÉTUDES (10 points)

### 2.1 Établir le planning initial du projet de l'Orlanvel 39, vérifier la date du salon et apprécier la robustesse du planning (2 pts)

**Compétence visée :**
- `2.2.b` — Élaborer la planification du projet (réseau ou diagramme de Gantt construit à partir d'un texte, dates au plus tôt et au plus tard, marges, chemin critique, jalons ; triptyque QCD et risques du projet)

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Tableau des tâches tiré du texte (durées et antériorités), en particulier les antériorités multiples : F après C **et** D ; H après B, E **et** F ; J après G, H **et** I ; réseau ou diagramme de Gantt cohérent | 0,5 |
| 2.1-02 | Dates de début et de fin au plus tôt et au plus tard de chaque tâche (tableau ci-dessous) | 0,5 |
| 2.1-03 | Marges totales et libres justes et lues : B (6 et 0), C (1 et 0), F (1 et 1), G (6 et 6), I (2 et 2), les autres nulles ; la marge libre nulle de B et de C signifie qu'un retard sur ces tâches consomme d'abord la marge de leurs successeurs | 0,5 |
| 2.1-04 | Durée **46 semaines**, chemin critique **A-D-E-H-J-K-L** ; fin à la fin de la semaine 46 (vendredi 20 août 2027), soit **une semaine de marge** sur la fin de la semaine 47 : la date du salon était tenable ; robustesse faible (marge d'une semaine, chemins presque critiques A-C-F-H-J-K-L de 45 semaines et A-C-I-J-K-L de 44, modèles sous-traités sur le chemin critique, plans de détail sans marge libre) | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **réseau des antécédents** (tâches, durées, antériorités), parcouru en avant pour les dates au plus tôt et en arrière, depuis la durée totale, pour les dates au plus tard, puis le **diagramme de Gantt** pour la lecture calendaire, les jalons et les marges. Le texte de l'annexe 2.1 doit d'abord être transformé en tableau des antériorités : c'est la compétence que le programme attend (« construire des diagrammes à partir de données brutes »).
- Alternatives acceptées : réseau en tâches sur les nœuds ou sur les flèches (avec tâches fictives correctement placées), Gantt seul s'il porte les dates au plus tôt et au plus tard et les marges ; numérotation des semaines de 1 au lieu des dates à partir de 0, si elle est annoncée et cohérente (début de A en semaine 1, fin de L en semaine 46).

**Conventions rappelées** (annexe 2.1)

- Semaines entières ; date 0 = début de la semaine 1 (lundi 5 octobre 2026) ; une tâche commencée en *t* et de durée *d* finit en *t* + *d* (fin de la semaine *t* + *d*).
- Marge totale = début au plus tard − début au plus tôt ; marge libre = plus petit début au plus tôt des successeurs (ou fin du projet) − fin au plus tôt ; chemin critique = tâches de marge totale nulle.

**Réponse attendue**

*Concepts.* Le planning d'un projet ordonne ses tâches selon leurs antériorités. La **date au plus tôt** d'une tâche est la plus grande des fins au plus tôt de ses prédécesseurs ; la **date au plus tard** est la date à laquelle elle doit commencer pour ne pas retarder la fin du projet. La **marge totale** mesure le retard qu'une tâche peut prendre sans retarder le projet, la **marge libre** celui qu'elle peut prendre sans retarder aucun de ses successeurs. Le **chemin critique**, formé des tâches sans marge totale, fixe la durée du projet : tout retard sur l'une d'elles le retarde d'autant.

*Application.*

| Tâche | Durée | Antériorités | Début au plus tôt | Fin au plus tôt | Début au plus tard | Fin au plus tard | Marge totale | Marge libre |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| A Conception générale | 8 | — | 0 | 8 | 0 | 8 | **0** | 0 |
| B Calculs de structure | 4 | A | 8 | 12 | 14 | 18 | 6 | 0 |
| C Plans de détail | 8 | A | 8 | 16 | 9 | 17 | 1 | 0 |
| D Maquette et modèles | 6 | A | 8 | 14 | 8 | 14 | **0** | 0 |
| E Moule de coque | 8 | D | 14 | 22 | 14 | 22 | **0** | 0 |
| F Moule de pont | 5 | C, D | 16 | 21 | 17 | 22 | 1 | 1 |
| G Quille relevable et puits | 10 | B | 12 | 22 | 18 | 28 | 6 | 6 |
| H Stratification du prototype | 6 | B, E, F | 22 | 28 | 22 | 28 | **0** | 0 |
| I Menuiserie intérieure | 10 | C | 16 | 26 | 18 | 28 | 2 | 2 |
| J Montage | 12 | G, H, I | 28 | 40 | 28 | 40 | **0** | 0 |
| K Essais en mer | 4 | J | 40 | 44 | 40 | 44 | **0** | 0 |
| L Dossier technique de conformité | 2 | K | 44 | 46 | 44 | 46 | **0** | 0 |

Durée du projet : **46 semaines** ; chemin critique **A → D → E → H → J → K → L** (8 + 6 + 8 + 6 + 12 + 4 + 2 = 46).

*Lecture des marges.* B a une marge totale de 6 semaines mais une **marge libre nulle** : tout retard des calculs de structure retarde la quille (G), qui dispose elle-même de 6 semaines ; un retard de plus de 6 semaines sur B ou sur G retarderait le projet. C a une marge totale d'une semaine et une marge libre nulle : un retard des plans de détail se reporte aussitôt sur le moule de pont (F) et sur la menuiserie (I). La menuiserie dispose de 2 semaines.

*Date du salon et robustesse.* Le projet devait se terminer à la fin de la semaine 46 (vendredi 20 août 2027), pour une date à tenir à la fin de la semaine 47 (vendredi 27 août) : le planning initial **permettait de présenter le prototype au salon, avec une semaine de marge seulement**. Il est **fragile** : (1) la marge d'une semaine représente 2,17 % de la durée du projet, alors que le projet précédent a pris cinq mois de retard ; (2) les chemins A-C-F-H-J-K-L (45 semaines) et A-C-I-J-K-L (44 semaines) sont presque critiques : trois semaines de retard sur les plans de détail suffisent à faire manquer le salon ; (3) le chemin critique passe par une tâche sous-traitée (les modèles, D), sur laquelle le chantier a peu de prise, et par la stratification et le montage, qui mobilisent les ateliers pendant la saison des livraisons ; (4) les essais en mer (K) et le dossier technique (L) sont en fin de chemin : aucun retard pris en amont ne pourra y être rattrapé. Il fallait donc fixer des **jalons** suivis (conception validée en fin de semaine 8, modèles livrés en fin de semaine 14, plans de détail figés en fin de semaine 16, moules prêts en fin de semaine 22, prototype à flot en fin de semaine 40) et suivre en priorité D, E et C. Conclusion : planning tenable, mais sans réserve pour les aléas.

**Calculs détaillés**

| Chemin | Durée (semaines) | Écart à la date à tenir (47) |
|---|---:|---:|
| A-D-E-H-J-K-L | 46 | 1 semaine de marge |
| A-C-F-H-J-K-L | 45 | 2 |
| A-C-I-J-K-L | 44 | 3 |
| A-D-F-H-J-K-L | 43 | 4 |
| A-B-G-J-K-L | 40 | 7 |
| A-B-H-J-K-L | 36 | 11 |

Contrôle : les marges totales se retrouvent par différence entre la durée du projet et le plus long chemin passant par chaque tâche (C : 46 − 45 = 1 ; I : 46 − 44 = 2 ; B et G : 46 − 40 = 6).

**Réponses tolérées**
- Semaines numérotées de 1 à 46 (début de A en semaine 1) au lieu des dates à partir de 0, si l'écriture est cohérente.
- Dates au plus tard exprimées seulement en début ou seulement en fin de tâche, si la marge totale est juste.
- Robustesse appréciée par d'autres arguments tirés du cas (dépendance au sous-traitant de la quille, saison des livraisons, nouvelle quille relevable jamais construite), si la conclusion porte sur la faiblesse de la marge.

**Erreurs fréquentes**
- `JUR-T10` — Oublier une antériorité multiple (H après B, E **et** F) et trouver une durée plus courte ; calculer les dates au plus tard sans repartir de la durée totale ; confondre marge totale et marge libre.
- `JUR-T07` — Dessiner un Gantt sans dates au plus tard ni marges, ou conclure sans confronter la durée à la date du salon.
- `JUR-T03` — Recopier le tableau sans lecture des marges ni appréciation de la robustesse.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 791-801 : « construire des diagrammes à partir de données brutes (textes) » ; Gantt, marges, jalons, chemin critique ; triptyque QCD, risques du projet) | planification | [V] | F05 § 0, § 4 |
| `ue3/00_LISEZMOI.md`, convention d'ordonnancement ; marge libre : formule de cours | dates, marges | [V] ; [S] marge libre | F05 § 1 |
| Diagramme de Gantt (Henry L. Gantt, années 1910) | outil de lecture calendaire | [V] programme ; [S] origine | F13 § 8 |

---

### 2.2 Mesurer les écarts et les indices du projet à la revue, estimer son coût final et choisir l'estimation à retenir (1,5 pt)

**Compétences visées :**
- `2.2.c` — Réaliser un suivi de l'avancement et des coûts du projet (CBTP, CRTE, CBTE, écarts de coût et de délai, IPC, IPD)
- `2.2.d` — Analyser les résultats obtenus (interpréter, estimer le coût final, proposer des actions correctives)

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Les trois grandeurs définies et calculées : **CBTP = 739 k€**, **CBTE = 612 k€**, **CRTE = 720 k€** (détail par tâche) | 0,5 |
| 2.2-02 | **Écart de coût = − 108 k€** et **écart de délai = − 127 k€**, tous deux défavorables ; **IPC = 0,8500**, **IPD = 0,8281** ; **coût final estimé = 1 700 / 0,85 = 2 000 k€** (dérive de 300 k€, 17,65 %) ; lecture : surcoût concentré sur A, C et D (− 100 k€ sur − 108), retard sur C, E, F et I ; la comparaison du budget planifié et du coût réel (739 contre 720) masquerait la double dérive | 0,5 |
| 2.2-03 | Comparaison avec l'estimation du chef de projet : 720 + 1 128 = **1 848 k€** (dérive de 148 k€, 8,71 %) ; estimation à retenir argumentée : la formule reconduit l'IPC sur tout le reste à faire, alors que la dérive tient à trois tâches terminées ou presque ; l'estimation tâche par tâche est plus pertinente mais optimiste (aucune réserve pour aléas, reprises possibles, accélération non comprise : 1 899 k€ avec les 51 k€ de la question 2.3) ; retenir l'estimation tâche par tâche complétée d'une réserve, avec 2 000 k€ comme seuil d'alerte | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : la **méthode de la valeur acquise**, seule capable de séparer, à une date donnée, ce qui relève du coût (le travail fait a-t-il coûté plus que son budget ?) et ce qui relève du délai (le travail fait correspond-il au travail prévu ?), à partir de l'avancement physique et non des dépenses. Le reste à faire réestimé tâche par tâche est l'alternative de prévision que le cas fournit.
- Alternatives acceptées : CBTP retrouvé à partir du planning de la question 2.1 au lieu de l'avancement prévu donné (même résultat) ; variante du coût final « reste au budget » (720 + 1 700 − 612 = 1 808 k€) présentée en complément, si elle est distinguée de la convention de l'annexe ; durée estimée 46 / IPD = 55,55 semaines citée comme ordre de grandeur, si le candidat voit qu'elle est moins fiable que le planning mis à jour (question 2.3 : 50 semaines).

**Conventions rappelées** (annexe 2.2)

- CBTP = Σ budget × avancement prévu ; CRTE = coûts réels engagés ; CBTE = Σ budget × avancement physique.
- Écart de coût = CBTE − CRTE ; écart de délai = CBTE − CBTP ; négatif = défavorable ; IPC = CBTE / CRTE ; IPD = CBTE / CBTP ; coût final estimé = budget total / IPC (IPC non arrondi).
- Montants en k€ arrondis à l'unité, indices à quatre décimales, pourcentages à deux décimales.

**Réponse attendue**

*Concepts.* À la date de la revue, le **CBTP** (valeur planifiée) mesure le budget du travail qui aurait dû être fait, le **CBTE** (valeur acquise) le budget du travail réellement fait, le **CRTE** ce que ce travail a coûté. L'**écart de coût** (CBTE − CRTE) isole la performance de coût, l'**écart de délai** (CBTE − CBTP) celle de l'avancement, exprimée en euros ; l'IPC et l'IPD en sont les rapports.

*Application.*

| Tâche | Budget | CBTP | CBTE | CRTE | Écart de coût | Écart de délai |
|---|---:|---:|---:|---:|---:|---:|
| A | 128 | 128 | 128 | 148 | − 20 | 0 |
| B | 56 | 56 | 56 | 56 | 0 | 0 |
| C | 160 | 160 | 120 | 184 | − 64 | − 40 |
| D | 180 | 180 | 180 | 196 | − 16 | 0 |
| E | 192 | 72 | 24 | 32 | − 8 | − 48 |
| F | 120 | 24 | 0 | 0 | 0 | − 24 |
| G | 208 | 104 | 104 | 104 | 0 | 0 |
| I | 150 | 15 | 0 | 0 | 0 | − 15 |
| H, J, K, L | 506 | 0 | 0 | 0 | 0 | 0 |
| **Total (k€)** | **1 700** | **739** | **612** | **720** | **− 108** | **− 127** |

IPC = 612 / 720 = **0,8500** : chaque euro dépensé n'a produit que 0,85 € de travail budgété. IPD = 612 / 739 = **0,8281** : le projet n'a réalisé que 82,81 % du travail prévu à cette date (36 % du budget réalisé au lieu de 43,47 %). Coût final estimé = 1 700 / 0,85 = **2 000 k€**, soit une dérive de 300 k€ (17,65 %), du même ordre que celle de l'Orlanvel 36 (18 %).

*Lecture.* Le projet cumule un **surcoût** et un **retard**. Le surcoût (− 108 k€) vient pour l'essentiel de trois tâches : les plans de détail repris (− 64 k€), la conception (− 20 k€, variante de quille abandonnée) et les modèles (− 16 k€, modification facturée par le sous-traitant). Le retard (− 127 k€) porte sur les plans de détail, le moule de coque et les deux tâches qu'ils bloquent (moule de pont et menuiserie). Une lecture budgétaire classique, qui compare le budget planifié à la date (739 k€) au coût réel (720 k€), ferait croire à une économie de 19 k€ : la valeur acquise montre qu'il s'agit d'un **retard qui masque un surcoût**.

*Estimation à retenir.* Le chef de projet estime le reste à faire à 1 128 k€, soit un coût final de 720 + 1 128 = **1 848 k€** (dérive de 148 k€, 8,71 %), contre 2 000 k€ par la formule. La formule suppose que l'inefficience constatée (IPC de 0,85) se reproduira sur tout le travail restant ; or 1 088 k€ de travail budgété restent à faire, pour l'essentiel en atelier et en sous-traitance (moules, stratification, menuiserie, montage, quille), alors que la dérive tient à trois tâches de conception terminées ou presque. L'estimation **tâche par tâche est plus pertinente**, à trois réserves près : (1) elle est optimiste, puisqu'elle suppose tous les budgets restants tenus, alors que le développement de l'Orlanvel 36 a dépassé son budget de 18 % et que les plans repris peuvent encore provoquer des reprises en atelier ; (2) elle ne comprend aucune accélération : avec les 51 000 € de la question 2.3, le coût final atteint **1 899 k€** (11,71 % de dérive) ; (3) elle émane du chef de projet, juge et partie. Il convient donc de retenir l'estimation tâche par tâche, majorée du coût de l'accélération et d'une réserve pour aléas sur les tâches d'atelier, et de garder les 2 000 k€ de la formule comme **seuil d'alerte** suivi à chaque revue. Action corrective : geler les plans de détail par une revue commune avec les ateliers avant la transmission, faire valider toute modification demandée aux sous-traitants.

**Réponses tolérées**
- Choix de l'estimation par la formule (2 000 k€) si le candidat le justifie par la prudence et par l'historique du chantier (Orlanvel 36), et discute l'optimisme du chef de projet : points de l'item 2.2-03 accordés.
- IPD arrondi à 0,83 et IPC à 0,85, si les montants sont justes.

**Erreurs fréquentes**
- `JUR-T10` — Inverser le signe des écarts (CRTE − CBTE), calculer le CBTE à partir des dépenses (CRTE / budget) au lieu de l'avancement physique, ou confondre CBTP et budget total.
- `JUR-T03` — Énumérer les indices sans dire d'où viennent la dérive et le retard (tâches A, C, D et C, E, F, I).
- `JUR-T05` — Choisir une estimation sans critère ni conséquence pour le pilotage (réserve, seuil d'alerte, action corrective).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 802-806 : coût budgété du travail prévu, coût réel du travail effectué, coût budgété du travail effectué, écarts ; tableau de bord du projet) ; guide pédagogique juillet 2026, p. 121 (IPC, IPD) | valeur acquise | [V] | F05 § 0, § 5 |
| `ue3/00_LISEZMOI.md`, convention de la valeur acquise (coût final estimé = budget / IPC) ; variante « reste au budget » | coût final estimé | [V] ; [S] variante | F05 § 1, § 5 |

---

### 2.3 Mettre à jour le planning, déterminer le plan d'accélération le moins coûteux et le coût d'une semaine de marge, apprécier l'intérêt et les risques de l'accélération (2,5 pts)

**Compétences visées :**
- `2.2.b` — Élaborer la planification du projet (replanification, chemins critiques, triptyque QCD et risques)
- `2.2.d` — Analyser les résultats obtenus (actions correctives, arbitrage coût-délai)

**Barème (2,5 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Planning mis à jour à partir de la date 17 : fin à la date **50** (fin de la semaine 50, vendredi 17 septembre 2027), soit **3 semaines de retard** sur la date à tenir ; nouveau chemin critique **C-F-H-J-K-L** : le retard des plans de détail est devenu critique, celui du moule de coque ne l'est plus (marge de 2 semaines) ; I a une marge d'une semaine, G de 10 | 0,5 |
| 2.3-02 | Plan d'accélération justifié étape par étape, en recalculant les chemins critiques : (1) seul C-F-H-J-K-L est critique : **F** (10 000 €) → 49 ; (2) C-F-H et C-I sont critiques : **C** (18 000 €) moins cher que H + I (23 000 €), F (2e semaine) + I (24 000 €) ou J (25 000 €) → 48 ; (3) trois chemins critiques (C-F-H, C-I, E-H) : **H + I** (23 000 €) moins cher que J (25 000 €) → 47 ; coût total **51 000 €** (C, F, H et I raccourcies d'une semaine) ; trois chemins critiques après accélération | 1 |
| 2.3-03 | Semaine de marge supplémentaire : **23 000 €** (H et I encore d'une semaine), soit 74 000 € pour finir en semaine 46 ; comparaison avec l'enjeu : 8 commandes × 52 000 € = **416 000 €** de marge sur coûts variables (8,16 fois le coût de l'accélération, qu'un seul voilier couvre presque : 0,98) ; le coût d'un retard d'une semaine est celui de trois, puisque le salon a une date fixe | 0,5 |
| 2.3-04 | Risques QCD de l'accélération et décision : plans de détail en heures supplémentaires (les 400 heures que le directeur technique juge possibles, risque de nouvelles erreurs ; variante sans eux à 56 000 €), stratification de nuit (cuisson de la résine, contrôles, défauts reproduits en série), intérimaires en menuiserie (finition), sous-traitance du moule de pont (qualité de l'ajustage), fatigue et sécurité des équipes ; essais en mer non réduits ; marge nulle après accélération ; recommandation argumentée et décisions échelonnées | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **planning mis à jour** (durées restantes à partir de la date 17), puis l'**arbitrage coût-délai** : on raccourcit le projet semaine par semaine, en choisissant à chaque étape le moyen le moins coûteux de raccourcir **tous** les chemins critiques, et l'on recalcule les chemins critiques après chaque étape. La décision est ensuite éclairée par un raisonnement **différentiel** : coût de l'accélération comparé à la marge sur coûts variables des commandes que seul le salon permet de prendre (les charges fixes ne varient pas).
- Alternatives acceptées : recherche directe de la combinaison la moins chère qui ramène chaque chemin sous 30 semaines (tableau des chemins et de leurs réductions), si le résultat est justifié ; présentation en semaines du calendrier (semaines 50 → 47) ou en durées restantes (33 → 30). Le plan obtenu ici par le pas à pas est aussi l'optimum : le plan suivant coûte 53 000 € (C, F et J).

**Conventions rappelées** (annexes 2.1 et 2.3)

- Durées restantes à partir de la date 17 ; tâches non commencées avec leurs durées et antériorités initiales ; date à tenir : fin de la semaine 47, soit 30 semaines après la revue.
- Réduction par semaines entières, jamais sous la durée minimale ; coût d'une tâche = somme des coûts des semaines gagnées ; antériorités inchangées ; plan retenu = le moins coûteux qui tient la date ; plusieurs chemins critiques : les raccourcir tous.

**Réponse attendue**

*Concepts.* Lorsqu'un projet est en retard sur une date imposée, on peut **raccourcir** certaines tâches en y consacrant des moyens supplémentaires (heures supplémentaires, intérim, sous-traitance, travail en équipes), dans la limite d'une durée minimale et à un coût par semaine gagnée. Seules les tâches **critiques** méritent d'être accélérées ; dès que plusieurs chemins sont critiques, il faut raccourcir chacun d'eux, et le chemin critique doit être recalculé après chaque semaine gagnée. C'est l'arbitrage entre les sommets **coût** et **délai** du triptyque QCD, qui ne doit pas sacrifier le troisième, la **qualité**.

*Planning mis à jour (0,5 pt).*

| Tâche | Durée restante | Antériorités | Début au plus tôt | Fin au plus tôt | Début au plus tard | Marge totale | Marge libre |
|---|---:|---|---:|---:|---:|---:|---:|
| C Plans de détail | 4 | — | 17 | 21 | 17 | **0** | 0 |
| E Moule de coque | 7 | — | 17 | 24 | 19 | 2 | 2 |
| G Quille et puits | 5 | — | 17 | 22 | 27 | 10 | 10 |
| F Moule de pont | 5 | C | 21 | 26 | 21 | **0** | 0 |
| H Stratification | 6 | E, F | 26 | 32 | 26 | **0** | 0 |
| I Menuiserie | 10 | C | 21 | 31 | 22 | 1 | 1 |
| J Montage | 12 | G, H, I | 32 | 44 | 32 | **0** | 0 |
| K Essais en mer | 4 | J | 44 | 48 | 44 | **0** | 0 |
| L Dossier technique | 2 | K | 48 | 50 | 48 | **0** | 0 |

Le projet se termine désormais à la date **50**, fin de la semaine 50 (vendredi 17 septembre 2027), au lieu de la semaine 47 : **3 semaines de retard**, et le salon serait manqué. Le chemin critique a **changé** : ce n'est plus le moule de coque (marge de 2 semaines), mais les **plans de détail**, qui bloquent le moule de pont, puis la stratification (chemin C-F-H-J-K-L, 33 semaines) ; la menuiserie est presque critique (C-I-J-K-L, 32 semaines ; marge d'une semaine) et le moule de coque le redeviendrait au-delà de 2 semaines de gain (E-H-J-K-L, 31 semaines).

*Plan d'accélération (1 pt).* Il faut gagner 3 semaines (33 → 30).

| Étape | Chemins critiques avant l'étape | Possibilités comparées | Choix | Coût | Fin du projet |
|---|---|---|---|---:|---:|
| 0 | C-F-H-J-K-L (33) | — | — | — | 50 |
| 1 | C-F-H-J-K-L (33) | F 10 000 ; H 15 000 ; C 18 000 ; J 25 000 | **F** (sous-traitance d'une partie du moule de pont) | 10 000 € | 49 |
| 2 | C-F-H-J-K-L et C-I-J-K-L (32) | **C 18 000** ; H + I 23 000 ; F (2e semaine) + I 24 000 ; J 25 000 | **C** (heures supplémentaires des dessinateurs) | 18 000 € | 48 |
| 3 | C-F-H-J-K-L, C-I-J-K-L et E-H-J-K-L (31) | **H + I 23 000** ; J 25 000 ; F (2e) + E + I 38 000 ; C : durée minimale atteinte | **H** (deux équipes) **et I** (intérimaires) | 23 000 € | 47 |
| **Total** | | | C, F, H, I : une semaine chacune | **51 000 €** | **47** |

Après accélération, trois chemins sont critiques (C-F-H-J-K-L, C-I-J-K-L et E-H-J-K-L, 30 semaines chacun) ; seule la quille garde une marge (G-J-K-L, 23 semaines). Le plan coûte **51 000 €** ; c'est le moins coûteux de tous ceux qui tiennent la date (le suivant, C + F + J, coûte 53 000 €).

*Semaine de marge et enjeu commercial (0,5 pt).* Une semaine de plus coûterait **23 000 €** (H et I raccourcies d'une seconde semaine, moins cher que J à 25 000 €), soit 74 000 € pour finir en semaine 46. En face, le service commercial attend 12 commandes du salon, dont 8 seraient perdues sans prototype à flot : **416 000 €** de marge sur coûts variables, puisque les charges fixes du chantier ne dépendent pas de ces commandes. L'accélération coûte 8,16 fois moins que ce qu'elle protège ; un seul Orlanvel 39 vendu au salon la paie presque (51 000 / 52 000 = 0,98 voilier). Parce que la date du salon est fixe, un retard d'une semaine coûte autant qu'un retard de trois : la semaine de marge à 23 000 € est une **assurance** contre la perte de 416 000 €, d'autant que les essais en mer dépendent de la météo.

*Risques et décision (0,5 pt).* L'accélération déplace le risque vers la **qualité** et la **sécurité**. (1) Les plans de détail accélérés absorbent 400 heures supplémentaires (18 000 / 45 €), tout ce que le directeur technique juge possible sans dégrader la qualité des plans, dans un bureau d'études déjà surchargé et qui reprend 20 % de ses heures (question 2.4) : nouvelle reprise possible. Une **variante sans heures supplémentaires au bureau d'études** existe : F, H et I accélérées (H et I de deux semaines) pour **56 000 €**, soit 5 000 € de plus. (2) La stratification en deux équipes impose de chauffer l'atelier la nuit et de contrôler chaque couche : un défaut de stratification du prototype se reproduirait sur la série. (3) La sous-traitance d'une partie du moule de pont pose la question de l'ajustement des cadènes, précisément le point qui a fait reprendre les plans. (4) Les intérimaires en menuiserie connaissent mal les finitions du chantier. (5) Le travail de nuit et les heures supplémentaires accroissent la fatigue et le risque d'accident. (6) Les essais en mer ne sont pas réduits : c'est la sécurité des clients. Après accélération, le projet n'a **plus aucune marge**. Recommandation : engager l'accélération, qui protège 416 000 € pour 51 000 € ; préférer la variante à 56 000 € si le directeur technique confirme que les heures supplémentaires feraient courir un risque d'erreur ; décider dès le comité du 4 février les mesures sur les tâches imminentes (plans de détail en cours, sous-traitance du moule de pont qui commence en semaine 21), et décider à la revue de début mars, au vu de l'avancement, de la semaine de marge : la stratification ne commencera qu'en semaine 25 et la menuiserie, commencée en semaine 21, peut encore recevoir un renfort d'intérimaires ; renforcer les contrôles qualité sur les tâches accélérées et suivre la date de fin à chaque revue.

**Calculs détaillés**

| Chemin restant | Avant | Après F | Après C | Après H + I | + 1 semaine (H, I) |
|---|---:|---:|---:|---:|---:|
| C-F-H-J-K-L | 33 | 32 | 31 | 30 | 29 |
| C-I-J-K-L | 32 | 32 | 31 | 30 | 29 |
| E-H-J-K-L | 31 | 31 | 31 | 30 | 29 |
| G-J-K-L | 23 | 23 | 23 | 23 | 23 |
| Coût cumulé (€) | 0 | 10 000 | 28 000 | 51 000 | 74 000 |
| Fin du projet (semaine) | 50 | 49 | 48 | 47 | 46 |

Contrôle : 10 000 + 18 000 + 23 000 = 51 000 € ; 416 000 / 51 000 = 8,16 ; variante sans le bureau d'études : F 10 000 + H 2 × 15 000 + I 2 × 8 000 = 56 000 €.

**Réponses tolérées**
- Recommandation de la variante à 56 000 € (sans heures supplémentaires au bureau d'études), ou du plan à 74 000 € (avec une semaine de marge), si elle est argumentée par les risques ou par la valeur du salon.
- Présentation directe de la combinaison optimale, sans tableau pas à pas, si chaque chemin est vérifié à 30 semaines et si l'absence de combinaison moins chère est justifiée.
- Comparaison avec la marge des 12 commandes attendues (624 000 €) au lieu des 8 commandes perdues, si l'hypothèse est dite : moitié des points de l'item 2.3-03.

**Erreurs fréquentes**
- `JUR-T10` — Raccourcir la tâche la moins chère sans vérifier qu'elle est critique (I à 8 000 € dès la première étape : aucun gain), ou ne raccourcir qu'un chemin quand plusieurs sont critiques ; accélérer les essais en mer, déclarés non réductibles.
- `JUR-T02` — Comparer le coût de l'accélération au chiffre d'affaires des commandes, ou y ajouter des charges fixes qui ne varient pas.
- `JUR-T05` — Arbitrer coût et délai sans parler de la qualité ni de la sécurité (triptyque QCD), ni de la marge nulle après accélération.
- `JUR-T08` — Appliquer une procédure sans conclure : la question attend une décision argumentée.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (l. 795-801 : triptyque QCD, risques du projet, chemin critique) | arbitrage coût-délai, risques | [V] | F05 § 0, § 2, § 6 |
| `ue3/00_LISEZMOI.md`, convention d'arbitrage coût-délai (durée minimale, coût par unité gagnée, raccourcir tous les chemins critiques) | plan d'accélération | [V] | F05 § 1 |
| Raisonnement différentiel par la marge sur coûts variables (acquis du DCG) | valeur des commandes du salon | [S] acquis du DCG | — |

---

### 2.4 Analyser la situation du bureau d'études, concevoir ses indicateurs de pilotage et formuler des préconisations (2 pts)

**Compétences visées :**
- `2.3.a` — Analyser la situation de gestion (processus support : bureau d'études)
- `2.3.f` — Élaborer des préconisations afin de mieux piloter la performance des activités hors production

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Bureau d'études qualifié de **processus support** (conception et développement, au service de clients internes : le projet, les ateliers, l'après-vente et les concessionnaires) ; capacité **13 × 800 = 10 400 h** (le directeur technique encadre et n'est pas compté) ; charge **11 440 h** ; taux de charge **110 %** (1 040 h de trop, 1,3 personne) ; coût horaire complet **520 000 / 10 400 = 50 €** | 0,5 |
| 2.4-02 | Trois ou quatre indicateurs conçus, chacun avec formule, objectif et sens, valeur et lecture : taux de charge 110 % (objectif ≤ 95 %) ; jalons tenus 50 % (objectif 100 %) ; part des heures de reprise 20 % (objectif ≤ 5 %, 56 000 € au coût complet) ; délai moyen de réponse à l'après-vente 9 jours ouvrés (objectif ≤ 5, 4,5 en 2025) ; aucun objectif atteint | 1 |
| 2.4-03 | Préconisations argumentées et chiffrées : priorités (projet daté, puis après-vente) et report des 1 600 h de la gamme 2028 (taux de charge ramené à 94,62 %) ; heures supplémentaires réservées à l'accélération des plans (400 h) ; sous-traitance des calculs de structure pour les pointes et l'expertise (44 800 €, coût décaissé, alors que le coût horaire interne est en grande partie fixe) ; recrutement à décider dès maintenant pour un besoin durable (un modèle tous les deux ans, trois à quatre mois de formation) ; polyvalence et revues de conception avec les ateliers pour réduire les reprises ; conclusion | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outils retenus : le rapprochement **charge / capacité**, qui montre si le service peut faire ce qu'on lui demande ; le **coût horaire complet**, qui valorise ses heures (reprises, sous-traitance) ; quelques **indicateurs de pilotage** reliés aux objectifs de la présidente, mêlant indicateurs de moyens (charge) et de résultats (jalons, reprises, délai de réponse), sans liste « à la Prévert ».
- Alternatives acceptées : indicateurs différents s'ils sont calculables avec les données de l'annexe 2.4 et reliés à un objectif (par exemple, part des heures consacrées au projet, heures de reprise par jalon, nombre de demandes de l'après-vente par semaine) ; capacité de 14 × 800 = 11 200 h (taux de charge 102,14 %, coût horaire 46,43 €) si le candidat écrit l'hypothèse que le directeur technique produit aussi : moitié des points de l'item 2.4-01. Non accepté : un tableau d'indicateurs sans formule ni objectif.

**Conventions rappelées** (annexe 2.4)

- Capacité = heures que peuvent consacrer aux activités les personnes qui produisent ; heures par personne = 26 × 35 − 70 − 40 = 800 h.
- Taux de charge = charge / capacité ; coût horaire complet = charges du semestre / capacité.
- Indicateur = numérateur / dénominateur (× 100 pour un taux) ; écart à l'objectif = valeur − objectif ; atteint si la valeur est au moins égale (hausse) ou au plus égale (baisse) à l'objectif ; deux décimales.

**Réponse attendue**

*Concepts et situation (0,5 pt).* Un **processus support** ne produit pas lui-même ce que l'entreprise vend, mais permet aux processus de production et de vente de fonctionner ; dans la chaîne de valeur de Porter (1985), le développement technologique fait partie des **activités de soutien**. Au chantier, le bureau d'études a trois clients internes, aux exigences différentes : le **projet** de l'Orlanvel 39 (date imposée), les **ateliers** (adaptations demandées par les clients des modèles existants) et l'**après-vente**, c'est-à-dire les concessionnaires, qui attendent des réponses rapides. Le piloter, c'est rapprocher ce qu'on lui demande de ce qu'il peut produire, à un coût connu. Chaque personne dispose de 26 × 35 − 70 − 40 = **800 heures** au semestre ; le directeur technique encadre et ne produit pas : la capacité est de 13 × 800 = **10 400 heures**. La charge atteint **11 440 heures** (projet 36,36 %, évolutions des modèles 45,45 %, après-vente 18,18 %) : taux de charge **110 %**, soit 1 040 heures de trop, l'équivalent de 1,3 personne. Les charges du semestre s'élèvent à 455 000 + 39 000 + 26 000 = 520 000 € : **coût horaire complet = 520 000 / 10 400 = 50 €**. Le bureau d'études est le **goulot** du chantier : il conditionne la date du salon, la qualité des plans transmis aux ateliers et la satisfaction des concessionnaires.

*Indicateurs (1 pt).*

| Indicateur | Formule | Objectif et sens | Valeur | Lecture |
|---|---|---|---:|---|
| Taux de charge du semestre | heures demandées / capacité × 100 = 11 440 / 10 400 × 100 | ≤ 95 % (à la baisse) | **110 %** | non atteint (+ 15 points) : surcharge structurelle, aucune réserve pour les aléas |
| Taux de jalons tenus | jalons tenus à la date prévue / jalons prévus × 100 = 2 / 4 × 100 | 100 % (à la hausse) | **50 %** | non atteint : modèles et plans de détail en retard |
| Part des heures de reprise de plans | heures de reprise / heures consacrées aux projets × 100 = 1 120 / 5 600 × 100 | ≤ 5 % (à la baisse) | **20 %** | non atteint (quatre fois l'objectif) : 1 120 h × 50 € = 56 000 € de non-qualité (ordre de grandeur, au coût horaire du premier semestre 2027) |
| Délai moyen de réponse à l'après-vente | somme des délais / nombre de demandes = 1 008 / 112 | ≤ 5 jours ouvrés (à la baisse) | **9 jours** | non atteint (+ 4 jours ; 4,5 jours en 2025) : les concessionnaires paient la priorité donnée au projet |

Aucun objectif n'est atteint, et les quatre indicateurs racontent la même histoire : le bureau d'études, surchargé, a donné la priorité au projet d'octobre à janvier (5 600 heures), au détriment de l'après-vente, tout en produisant des plans repris, faute d'échanges avec les ateliers avant leur transmission. Le taux de charge est un indicateur d'**alerte** (moyens) ; les trois autres mesurent les **résultats** attendus par les clients internes. À suivre chaque mois, présentés au comité de pilotage.

*Préconisations (0,5 pt).* (1) **Fixer des priorités** : le projet daté d'abord, l'après-vente ensuite (relation avec les concessionnaires), les évolutions différables en dernier ; reporter au second semestre les **1 600 heures** de modifications de la gamme 2028 ramène la charge à 9 840 heures, soit **94,62 %** de la capacité, sous l'objectif de 95 %, sans aucun coût. (2) **Réserver les heures supplémentaires** à l'accélération des plans de détail (400 heures, 18 000 €), qui en consomme tout le volume admissible. (3) **Sous-traiter les calculs de structure** des pointes (640 heures, 44 800 €) : utile pour une compétence pointue et pour libérer des ingénieurs sur le prototype, mais c'est un coût décaissé, alors que le coût horaire interne de 50 € est pour l'essentiel fixe (salaires, amortissements) et ne serait pas économisé ; à réserver aux pointes. (4) **Recruter** un dessinateur-projeteur si la surcharge est durable : le plan « ORLANVEL 2030 » prévoit un nouveau modèle tous les deux ans et le recruté ne sera opérationnel qu'après trois à quatre mois, ce qui impose de décider dès le printemps pour le second semestre. (5) **Polyvalence** : former deux dessinateurs aux questions de l'après-vente et organiser une permanence pour les concessionnaires. (6) **Réduire les reprises à la source** : revue des plans avec la stratification, le montage et les achats avant leur transmission, gel des plans à un jalon ; dans le sujet complet, la répétition de la cause (cadènes impossibles à réaliser, déjà à l'origine des reprises de l'Orlanvel 36 selon le dossier 1) montre l'absence de retour d'expérience. Conclusion : le report et la priorisation règlent le semestre ; la réduction des reprises et un recrutement règlent la durée.

**Calculs détaillés**

| Élément | Calcul | Résultat |
|---|---|---:|
| Heures par personne | 26 × 35 − 70 − 40 | 800 h |
| Capacité | 13 × 800 | 10 400 h |
| Charge | 4 160 + 5 200 + 2 080 | 11 440 h |
| Taux de charge | 11 440 / 10 400 | 110 % |
| Heures excédentaires | 11 440 − 10 400 (1 040 / 800 = 1,3 personne) | 1 040 h |
| Charges du semestre | 455 000 + 39 000 + 26 000 | 520 000 € |
| Coût horaire complet | 520 000 / 10 400 | 50,00 € |
| Coût complet des reprises (ordre de grandeur, au coût horaire du premier semestre 2027) | 1 120 × 50 | 56 000 € |
| Charge après report de la gamme 2028 | 11 440 − 1 600 (taux 9 840 / 10 400) | 9 840 h (94,62 %) |
| Heures supplémentaires au maximum | 400 × 45 | 18 000 € |
| Sous-traitance des calculs de structure | 640 × 70 | 44 800 € |

**Réponses tolérées**
- Indicateurs exprimés autrement (part des demandes traitées en moins de 5 jours, nombre de jalons manqués), si la formule est calculable et l'objectif adapté.
- Préconisation de recruter deux dessinateurs, comme le demande le directeur technique, si le candidat discute le coût et le délai d'intégration, et ne la présente pas comme la réponse à la surcharge du semestre.

**Erreurs fréquentes**
- `JUR-T10` — Compter le directeur technique dans la capacité alors que l'annexe dit qu'il ne produit pas, ou oublier les congés et les absences ; présenter le coût horaire complet comme une économie réalisable en sous-traitant.
- `JUR-T07` — Dresser une liste d'indicateurs sans formule, sans objectif ni sens, ou sans lien avec les objectifs de la présidente.
- `JUR-T02` — Préconiser « recruter » ou « sous-traiter » en général, sans les données de l'annexe (1 600 h reportables, 400 h au plus, 70 € de l'heure, trois à quatre mois de formation).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.3 (l. 811-817 : exploitation dans divers processus, dont la R&D ; pilotage des activités hors production) ; guide p. 121 (la distinction production / support dépend de l'organisation) | processus support | [V] | F06 § 0, § 7 |
| Porter (1985), chaîne de valeur : activités principales et de soutien | qualification du bureau d'études | [V] guide p. 115 ; [S] date | F13 § 1 |
| `ue3/00_LISEZMOI.md`, convention des indicateurs de tableau de bord ; guide p. 126 (pas de liste « à la Prévert ») | indicateurs | [V] | F05 § 7 ; F12 § 2, § 3 |

---

### 2.5 Note au comité de pilotage du 4 février 2027 (20 lignes au maximum) (2 pts)

**Compétences visées :**
- `2.2.e` — Produire une synthèse rédigée et structurée concernant le pilotage du projet
- `2.3.g` — Produire une synthèse rédigée et structurée concernant les décisions liées aux processus support

**Barème (2 pts)** — grille de notation d'une réponse rédigée (six critères : concept défini et attribué ; mobilisation pertinente ; faits du cas ; analyse et non description ; préconisation faisable ; forme et longueur).

| Note | Descripteur |
|---:|---|
| 0 | Absence de réponse, hors sujet ou cours récité sans aucun fait du cas |
| 0,5 | Note qui résume les calculs sans décision, ou qui dépasse nettement les 20 lignes |
| 1 | Avancement et dérives chiffrés et décision d'accélération proposée, sans conditions de réussite ou sans le bureau d'études |
| 1,5 | Avancement, dérives, décision chiffrée (51 000 € contre 416 000 €), risques et conditions de réussite, mesures pour le bureau d'études ; structure ou lien entre projet et bureau d'études perfectible |
| 2 | Six critères satisfaits : note structurée (objet, situation, décision, conditions, bureau d'études, conclusion), chiffres clés repris sans recalcul, décisions datées, lien explicite entre la surcharge du bureau d'études et les dérives du projet, 20 lignes au maximum |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : note de **reporting** au comité de pilotage : situation (avancement, coût, délai), causes, projection, décisions demandées, conditions et indicateurs de suivi ; elle relie le projet au processus support qui en est le goulot.
- Alternatives acceptées : décision fondée sur la variante à 56 000 € ou sur le plan à 74 000 €, si elle est cohérente avec la question 2.3 ; présentation par feux (vert, orange, rouge) sur les axes qualité, coût, délai, si les phrases de liaison et la conclusion existent.

**Réponse attendue** (modèle de note, 20 lignes au maximum)

**Objet : Orlanvel 39, revue de fin janvier et décisions pour tenir le salon.**

**1. Situation.** À fin janvier, 36 % du budget de travail est réalisé contre 43,47 % prévus. Surcoût de 108 k€ (IPC 0,85) et retard (IPD 0,83), dus aux plans de détail repris, à la conception et aux modèles. Coût final estimé : 1 848 k€ selon le chef de projet, 2 000 k€ si la dérive se poursuit (seuil d'alerte). Le planning mis à jour finit en semaine 50 : trois semaines après la date de départ vers le salon.

**2. Décision proposée.** Accélérer les plans de détail, le moule de pont, la stratification et la menuiserie d'une semaine chacun : 51 000 €, plan le moins coûteux, qui ramène la fin en semaine 47. Il protège 416 000 € de marge attendue du salon. Une semaine de marge coûterait 23 000 € de plus : à décider à la revue de début mars.

**3. Conditions de réussite.** Plans figés après revue avec les ateliers ; contrôle renforcé de la stratification de nuit ; essais en mer non réduits ; autorité du chef de projet sur les équipes accélérées ; revue toutes les deux semaines.

**4. Bureau d'études.** Chargé à 110 %, il reprend 20 % de ses heures et répond aux concessionnaires en 9 jours. Reporter la gamme 2028 (charge à 94,62 %), suivre quatre indicateurs, étudier un recrutement.

**Conclusion.** Le salon reste accessible, à condition de protéger la qualité et de soulager le bureau d'études.

**Réponses tolérées**
- Décision différente (variante sans heures supplémentaires au bureau d'études, semaine de marge achetée tout de suite), si elle reprend le coût et l'enjeu.
- Indicateurs du bureau d'études cités autrement, si deux au moins sont chiffrés.

**Erreurs fréquentes**
- `JUR-T05` — Traiter séparément le projet et le bureau d'études, sans voir que la surcharge du service explique les reprises et le retard.
- `JUR-T06` — Dépasser les 20 lignes, absence de structure ou de conclusion.
- `JUR-T03` — Résumer les calculs sans décision demandée au comité ni conditions de réussite.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, parties 2.2 et 2.3 (reporting de projet, l. 806 ; synthèse sur les processus support, l. 818-820) ; guide p. 113 et p. 121 | périmètre de la note | [V] | F05 § 7 ; F06 § 0 |
| Grille à six critères des réponses rédigées | notation | [V] | gabarits/corrige_ue3_template.md ; bareme_grille.yaml |

---

## Contrôles avant publication

- [x] `python3 -I outils/dscgcheck ue3/exercices/ex13_projet_prototype_bureau_etudes/corrige.yaml` : 0 erreur, 0 avertissement ; planning initial et planning mis à jour, valeur acquise, plan d'accélération optimal (calcul exact, unicité vérifiée, pas à pas conforme), semaine de marge et variante sans heures supplémentaires au bureau d'études, indicateurs recalculés ; calculs divers recalculés par script (`/paperclip/shared/dscglab-travail/DSC-219/calculs_dossier2.py`) ; barème partiel sur 10 ; liste noire ; hors-programme.
- [x] Cohérence avec les données partagées du sujet n° 5 : 14 personnes au bureau d'études ; projet démarré en octobre 2026 (semaine 1 = lundi 5 octobre 2026) ; prototype présenté au salon de septembre 2027, salon non nommé ; Orlanvel 36 en retard de cinq mois avec un budget dépassé de 18 % ; noms repris du dossier 1 (MM. TRÉVANNEC et BRÉHAMET, Mme MERLANDOU) et chef de projet désigné à titre d'essai en octobre 2026.
- [x] Compétences visées présentes dans `programme/perimetre_ue3.yaml` ; aucun outil prescrit dans l'énoncé ; chaque question présente le concept, l'applique au cas, conclut ; synthèse bornée (2.5, 20 lignes au maximum).
- [x] Entités et personnes fictives (M. Erwan DORVENEC ; sous-traitants et salon non nommés) ; attribution limitée à F13 (Porter, 1985) ; aucune réglementation de la conformité des bateaux citée ; ni budget par période, ni plan de financement, ni critère de choix d'investissement, ni méthode de gestion de projet informatique.
