# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 3 – Contrôle de gestion et stratégie — Exercice d'entraînement n° 54 — Dossier 2 (6 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F04 pilotage des processus de production (coûts pertinents, coûts de la qualité), F05 pilotage des projets, F08 gestion des risques et contrôle interne, F13 registre des auteurs (toutes à jour au 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (planning, durée de coût total minimal et pas à pas de l'accélération, puis optimum recalculé sans raccourcir la formation sur site ni les essais de couleur ; coût d'une semaine de retard, coût total par durée et cotation du risque de non-conformité : calculs divers recalculés par script ; barème partiel sur 6 ; liste noire ; hors-programme).

Bien que le corrigé mentionne des auteurs, des textes et des données, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur le choix et la justification des outils, la justesse des calculs, la pertinence de l'analyse au regard du cas et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet) ; pour chaque question, la présentation des concepts et outils avant leur mobilisation puis la conclusion sont notées. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Planning de l'installation de la troisième presse tiré du compte rendu : antériorités, dates, marges totales et libres, chemin critique, durée ; retard sur la date contractuelle | `2.2.b` Élaborer la planification du projet | 2 |
| 2.2 Coût pertinent d'une semaine de retard ; durée de coût total minimal, plan d'accélération et coût, pas à pas | `2.2.d` Analyser les résultats obtenus ; `2.1.a` Analyser la situation de gestion | 2 |
| 2.3 Cotation et coût attendu du risque de non-conformité au démarrage ; optimum sans raccourcir la formation sur site ni les essais de couleur ; arbitrage qualité-coût-délai et relation avec le client | `2.2.d` Analyser les résultats obtenus ; `2.5.b` Analyser les risques rencontrés par l'organisation | 1 |
| 2.4 Note à M. CHARMEYRAN et au comité de pilotage du projet (20 lignes au maximum) | `2.2.e` Produire une synthèse rédigée et structurée concernant le pilotage du projet | 1 |
| **Dossier 2 – Installer la troisième presse numérique à temps : planning et arbitrage entre coût, délai et qualité** | | **6** |

---

## DOSSIER 2 – INSTALLER LA TROISIÈME PRESSE NUMÉRIQUE À TEMPS : PLANNING ET ARBITRAGE ENTRE COÛT, DÉLAI ET QUALITÉ (6 points)

### 2.1 Établir le planning du projet, son chemin critique et sa durée, et situer la date de démarrage par rapport à la date contractuelle (2 pts)

**Compétences visées :**
- `2.2.b` — Élaborer la planification du projet (réseau ou diagramme de Gantt construit à partir d'un texte, dates au plus tôt et au plus tard, marges, chemin critique, jalons)

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Concepts présentés (tâche, antériorité, date au plus tôt et au plus tard, marge totale et libre, chemin critique, jalon) ; tableau des antériorités tiré du texte, avec les antériorités multiples : **E après B et C** ; **F après D et E** ; **H après F et G** ; **J après H et I** | 0,5 |
| 2.1-02 | Dates de début et de fin au plus tôt et au plus tard de chaque tâche (tableau ci-dessous), calculées en avant puis en arrière depuis la durée totale | 0,5 |
| 2.1-03 | Marges totales : C et D 9, G 25, H 1, les autres nulles ; marges libres : C **0**, D 9, G **24**, H 1 ; lecture de la différence entre marge totale et marge libre de C et de G | 0,5 |
| 2.1-04 | Durée **42 semaines**, chemin critique **A-B-E-F-I-J-K** ; démarrage à la fin de la semaine 42 (vendredi 11 février 2028), soit **4 semaines** après la fin de la semaine 38 imposée par le contrat ; lecture : la livraison du constructeur (21 semaines, non compressible) pèse la moitié du projet, la formation sur site n'a qu'une semaine de marge, les travaux (C, D) en ont 9 | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : le **réseau des antécédents** (tâches, durées, antériorités), parcouru en avant pour les dates au plus tôt et en arrière, depuis la durée totale, pour les dates au plus tard, complété par un **diagramme de Gantt** pour lire le calendrier et placer les jalons. Le compte rendu doit d'abord être transformé en tableau des antériorités : le programme demande de « construire des diagrammes à partir de données brutes (textes) ».
- Alternatives acceptées : réseau en tâches sur les nœuds (méthode des potentiels) ou sur les flèches (avec des tâches fictives correctement placées) ; Gantt seul s'il porte les dates au plus tard et les marges.

**Conventions rappelées** (annexe 2.4)

- Semaines entières, comptées sans interruption ; date 0 = début de la semaine 1 (lundi 26 avril 2027) ; une tâche commencée en *t* et de durée *d* finit en *t* + *d* (fin de la semaine *t* + *d*).
- Marge totale = début au plus tard − début au plus tôt ; marge libre = plus petit début au plus tôt des successeurs (ou fin du projet) − fin au plus tôt.

**Réponse attendue**

*Concepts (2.1-01).* Le planning ordonne les tâches selon leurs antériorités. La **date au plus tôt** d'une tâche est la plus grande des fins au plus tôt de ses prédécesseurs ; sa **date au plus tard** est la date à laquelle elle doit commencer pour ne pas retarder la fin du projet. La **marge totale** mesure le retard qu'une tâche peut prendre sans retarder le projet, la **marge libre** celui qu'elle peut prendre sans retarder aucun de ses successeurs. Le **chemin critique**, formé des tâches sans marge totale, fixe la durée du projet. Les **jalons** (commande signée, presse livrée, presse raccordée, presse calibrée, bons à tirer signés, démarrage) bornent les étapes et servent au suivi.

*Planning (2.1-01 à 2.1-03).*

| Tâche | Durée | Antériorités | Début au plus tôt | Fin au plus tôt | Début au plus tard | Fin au plus tard | Marge totale | Marge libre |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| A Configuration et commande | 2 | — | 0 | 2 | 0 | 2 | **0** | 0 |
| B Fabrication et livraison de la presse | 21 | A | 2 | 23 | 2 | 23 | **0** | 0 |
| C Dalle et fosse | 6 | A | 2 | 8 | 11 | 17 | 9 | 0 |
| D Traitement de l'air et de l'hygrométrie | 10 | C | 8 | 18 | 17 | 27 | 9 | 9 |
| E Installation mécanique | 4 | B, C | 23 | 27 | 23 | 27 | **0** | 0 |
| F Raccordements et mise sous tension | 3 | D, E | 27 | 30 | 27 | 30 | **0** | 0 |
| G Formation chez le constructeur | 4 | A | 2 | 6 | 27 | 31 | 25 | 24 |
| H Formation sur site | 4 | F, G | 30 | 34 | 31 | 35 | 1 | 1 |
| I Essais et calibration colorimétrique | 5 | F | 30 | 35 | 30 | 35 | **0** | 0 |
| J Qualification avec le client et bons à tirer | 4 | H, I | 35 | 39 | 35 | 39 | **0** | 0 |
| K Démarrage et montée en cadence | 3 | J | 39 | 42 | 39 | 42 | **0** | 0 |

| Chemin | Durée (semaines) |
|---|---:|
| A-B-E-F-I-J-K | **42** (critique) |
| A-B-E-F-H-J-K | 41 |
| A-C-D-F-I-J-K | 33 |
| A-C-E-F-I-J-K | 27 |
| A-G-H-J-K | 17 |

*Lecture (2.1-03 et 2.1-04).*
- Le projet dure **42 semaines** : la presse serait démarrée le vendredi 11 février 2028, **4 semaines** après la fin de la semaine 38 (vendredi 14 janvier 2028) qu'impose le contrat pour livrer le lundi 17 janvier. Les premières livraisons partiraient le lundi 14 février.
- La **livraison du constructeur** (B, 21 semaines) représente la moitié du projet et ne peut pas être raccourcie : le chemin critique ne peut être raccourci qu'en aval (installation, raccordements, essais, démarrage), sur la phase où la qualité se joue.
- La **formation sur site** (H) n'a qu'**une semaine** de marge : tout gain sur les essais de couleur (I) la rendra critique à son tour.
- La **dalle** (C) a 9 semaines de marge totale mais **aucune marge libre** : un retard de C retarde aussitôt le traitement de l'air (D), qui dispose lui-même des 9 semaines ; au-delà de 9 semaines, le projet est retardé. Le traitement de l'air n'étant pas critique, l'accélérer serait inutile.
- La **formation chez le constructeur** (G) a 25 semaines de marge totale et 24 de marge libre : placée au plus tôt (semaines 3 à 6), elle laisserait vingt-quatre semaines entre la formation et la pratique sur la presse. Mieux vaut la programmer près de sa date de début au plus tard (date 27, soit au début de la semaine 28), pour que les conducteurs arrivent sur la presse avec des acquis frais.
- Jalons : commande signée (fin de la semaine 2), presse livrée (fin de la semaine 23, vendredi 1er octobre 2027), presse raccordée (30), presse calibrée (35), bons à tirer signés (39), démarrage (42).

Conclusion : sans action, le projet ne tient pas la date du contrat ; quatre semaines sont à gagner, sur des tâches proches du démarrage.

**Réponses tolérées**
- Semaines numérotées de 1 à 42 au lieu des dates à partir de 0, si l'écriture est cohérente.
- Diagramme de Gantt présenté à la place du tableau, s'il fait apparaître dates au plus tard et marges.
- Lecture de la marge de G limitée au calcul, sans la recommandation de programmer la formation plus tard : 2.1-03 accordé si la différence entre marge totale et marge libre est expliquée sur C.

**Erreurs fréquentes**
- `JUR-T10` — Oublier une antériorité multiple (E après B **et** C ; F après D **et** E ; H après F **et** G ; J après H **et** I) ; calculer les dates au plus tard sans repartir de la durée totale ; confondre marge totale et marge libre (C : 9 et 0).
- `JUR-T03` — Recopier le compte rendu sans en tirer de lecture : poids de la livraison non compressible, marge d'une semaine de la formation sur site, formation chez le constructeur trop éloignée de la pratique.
- `JUR-T02` — Ne pas convertir la durée en date et ne pas la comparer à la date contractuelle (fin de la semaine 38).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (« construire des diagrammes à partir de données brutes (textes) » ; Gantt, marges, jalons, chemin critique) | planning | [V] | F05 § 0, § 4 |
| `ue3/00_LISEZMOI.md`, conventions d'ordonnancement ; marge libre : formule de cours | dates, marges | [V] ; [S] marge libre | F05 § 1, § 4 |
| Diagramme de Gantt (Henry L. Gantt, années 1910) | lecture calendaire | [V] programme ; [S] origine | F13 § 8 |

---

### 2.2 Déterminer le coût pertinent d'une semaine de retard, puis la durée de coût total minimal, le plan d'accélération et son coût (2 pts)

**Compétences visées :**
- `2.2.d` — Analyser les résultats obtenus (arbitrage coût-délai, actions correctives sur le planning)
- `2.1.a` — Analyser la situation de gestion (coûts pertinents, coûts irrécupérables, approche marginale)

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Concepts : coût pertinent (futur et différentiel entre les options), coût irrécupérable, approche marginale ; coût d'une semaine de retard = pénalité **9 k€** + sous-traitance 150 × (68,00 − 28,00) = 150 × 40,00 € = **6,0 k€**, soit **15,0 k€** | 0,5 |
| 2.2-02 | Coûts écartés et pourquoi : prix de vente (inchangé) ; chiffre d'affaires et marge des étiquettes personnalisées (décalés, pas perdus) ; charges fixes de la presse, 15,00 € par millier (amortissement, salaires des conducteurs : payés quelle que soit la date) ; prix de la presse et travaux, 1 740 k€ (identiques quelle que soit la date) ; frais déjà réglés, 46 k€ (irrécupérables) ; amortissement sur huit ans (répartition de l'investissement, non modifiée par la décision) ; erreur signalée : retenir le coût complet de 43,00 € donnerait 3 750 € (3,8 k€) de sous-traitance et 12,8 k€ par semaine | 0,5 |
| 2.2-03 | Pas à pas : I (4 k€, 41 semaines) ; à 41 semaines, deux chemins critiques (par H et par I) : F (10 k€) moins cher que H + I (5 + 8 = 13 k€) : 40 semaines ; puis H + I (13 k€ < 15 k€) : 39 semaines ; ensuite E (18 k€) ou K (20 k€) coûtent plus qu'une semaine de retard : arrêt ; D (3 k€) écartée parce qu'elle n'est pas critique | 0,5 |
| 2.2-04 | **Durée de coût total minimal : 39 semaines** (démarrage le vendredi 21 janvier 2028, une semaine après la date contractuelle) ; accélération **27 k€** (I deux semaines 12 k€, F une semaine 10 k€, H une semaine 5 k€) + retard **15 k€** = **42 k€**, contre 60 k€ sans accélération et 45 k€ pour tenir la date ; lecture : ce plan gagne deux semaines sur les essais de couleur et une sur la formation sur site | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : l'**arbitrage coût-délai**. On raccourcit le projet semaine après semaine par l'ensemble de tâches le moins cher qui raccourcit **tous** les chemins critiques, tant que ce coût reste inférieur au coût d'une semaine de retard évitée (raisonnement marginal). Le coût de la semaine de retard se construit par l'**approche des coûts pertinents** : seuls comptent les coûts futurs qui changent avec la date de démarrage.
- Alternatives acceptées : tableau du coût total pour chaque durée de 42 à 38 semaines, si le coût minimal d'accélération de chaque durée est justifié (0, 4, 14, 27, 45 k€) ; présentation sous forme de comparaison marginale (coût de la semaine gagnée contre 15 k€) sans tableau complet.

**Conventions rappelées** (annexes 2.2 à 2.4)

- Réduction par semaines entières jusqu'à la durée minimale ; coût d'une tâche = somme des coûts des semaines gagnées ; antériorités inchangées ; aucune prime d'avance.
- Coût total d'une durée = coût d'accélération + coût d'une semaine de retard × semaines au-delà de la fin de la semaine 38.

**Réponse attendue**

*Concepts et coût d'une semaine de retard (2.2-01 et 2.2-02).* Un **coût pertinent** est un coût futur qui diffère selon l'option retenue ; un coût **irrécupérable** est déjà engagé et ne change pas avec la décision : il est écarté. La décision porte ici sur la **date de démarrage** : n'entrent dans le coût d'une semaine de retard que les coûts qui existent parce que la presse démarre une semaine plus tard.

| Élément (annexe 2.3) | Pertinent ? | Montant par semaine de retard |
|---|---|---:|
| Pénalité contractuelle | oui : due seulement en cas de retard | 9,0 k€ |
| Achat au confrère : 150 milliers × 68,00 € | oui : n'existe qu'en cas de retard | 10,2 k€ |
| Coûts variables évités sur la troisième presse : 150 milliers × 28,00 € | oui, en déduction : non engagés pendant le retard | − 4,2 k€ |
| Surcoût de sous-traitance : 150 × (68,00 − 28,00) = 150 × 40,00 € | | **6,0 k€** |
| **Coût d'une semaine de retard** | | **15,0 k€** |
| Prix de vente au client | non : inchangé | — |
| Charges fixes de la presse, 15,00 € par millier (amortissement, salaires des quatre conducteurs) | non : supportées quelle que soit la date | — |
| Prix de la presse et travaux (1 480 + 260 = 1 740 k€) | non : identiques quelle que soit la date | — |
| Chiffre d'affaires et marge des étiquettes personnalisées | non : décalés, pas perdus (annexe 2.3) | — |
| Visites, essais et étude déjà réglés (46 k€) | non : irrécupérables | — |
| Amortissement sur huit ans | non : répartition de l'investissement dans le temps, sans dépense nouvelle liée à la date | — |

Retenir le coût de production complet de 43,00 € conduirait à un surcoût de 150 × (68,00 − 43,00) = 3 750 € (3,8 k€) et à une semaine de retard à 12,8 k€ : les charges fixes de la presse ne sont pas évitées pendant le retard, elles ne doivent pas être déduites.

*Durée de coût total minimal (2.2-03 et 2.2-04).*

| Étape | Chemins critiques | Possibilités (coût d'une semaine, k€) | Choix | Coût de l'étape (k€) | Durée | Accélération cumulée (k€) | Retard (k€) | **Coût total (k€)** |
|---|---|---|---|---:|---:|---:|---:|---:|
| 0 | A-B-E-F-I-J-K (42) | — | — | — | 42 | 0 | 4 × 15 = 60 | **60** |
| 1 | A-B-E-F-I-J-K (42) | I 4, F 10, E 18, K 20 | I | 4 | 41 | 4 | 45 | **49** |
| 2 | A-B-E-F-I-J-K et A-B-E-F-H-J-K (41) | F 10, H + I 5 + 8 = 13, E 18, K 20 | F | 10 | 40 | 14 | 30 | **44** |
| 3 | les deux mêmes (40) | H + I 13, E 18, K 20 | H + I | 13 | 39 | 27 | 15 | **42** |
| (4) | les deux mêmes (39) | E 18, K 20 (F, H et I à leur minimum) | — | 18 | 38 | 45 | 0 | 45 |

À chaque étape, on gagne une semaine au moindre coût sur **tous** les chemins critiques. À la première étape, la tâche la moins chère, D (3 k€), n'est pas critique (9 semaines de marge) : la raccourcir ne ferait rien gagner. Les essais de couleur (I, 4 k€) le sont : on les raccourcit d'une semaine. La formation sur site (H) devient alors critique : à 41 semaines, il faut raccourcir à la fois le chemin qui passe par H et celui qui passe par I. Les raccordements (F, 10 k€), communs aux deux, coûtent moins que H + I (13 k€) : on les raccourcit d'abord, puis H + I, dont le coût (13 k€) reste inférieur aux 15 k€ de la semaine de retard évitée. Ensuite, seules E (18 k€) et K (20 k€) peuvent encore être raccourcies, pour plus que les 15 k€ évités : on s'arrête.

**Durée retenue : 39 semaines**, démarrage le vendredi 21 janvier 2028 et premières livraisons le lundi 24 janvier, une semaine après la date du contrat. Coût d'accélération **27 k€** (essais en deux équipes et protocole allégé : 2 semaines, 12 k€ ; électriciens en équipes alternées : 1 semaine, 10 k€ ; formation sur site resserrée : 1 semaine, 5 k€), retard **15 k€** : **coût total 42 k€**, soit 18 k€ de moins que sans accélération et 3 k€ de moins que s'il fallait tenir la date (45 k€). Ce plan atteint son coût minimal en raccourcissant de deux semaines les essais de couleur et d'une semaine la formation sur site : il faut en apprécier l'effet sur la qualité (question 2.3).

**Réponses tolérées**
- Tableau des coûts totaux de 42 à 38 semaines sans pas à pas, si le coût minimal d'accélération de chaque durée est juste.
- Étapes 2 et 3 présentées dans l'autre ordre (H + I puis F), si le candidat justifie que le coût cumulé à 39 semaines (27 k€) est le même : 2.2-03 accordé.
- Sous-traitance calculée en € (6 000 €) ou coût de la semaine exprimé en € (15 000 €).
- Amortissement classé comme « non pertinent car non décaissable » plutôt que comme répartition de l'investissement, si le candidat l'écarte.

**Erreurs fréquentes**
- `JUR-T10` — Accélérer D, la moins chère, alors qu'elle n'est pas critique ; à 41 semaines, ne raccourcir qu'un des deux chemins critiques (I seule) ; accélérer jusqu'à tenir la date quoi qu'il en coûte (45 k€ au lieu de 42 k€).
- `JUR-T10` — Déduire le coût de production complet (43,00 €) au lieu du seul coût variable évité, ou ajouter au coût du retard l'investissement, les frais déjà réglés ou l'amortissement.
- `JUR-T05` — S'arrêter au calcul sans voir que l'optimum de coût se fait sur les essais de couleur et la formation, au détriment possible de la qualité.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| `ue3/00_LISEZMOI.md`, arbitrage coût-délai (durée de coût total minimal, plusieurs chemins critiques à raccourcir ensemble) | pas à pas, optimum | [V] | F05 § 1 |
| Programme et guide UE 3, partie 2.1 (coûts pertinents, coûts irrécupérables, approche marginale « qui devra servir à l'ensemble de l'UE ») | coût d'une semaine de retard | [V] programme et guide ; [S] définitions | F04 § 8 |
| Programme UE 3, partie 2.2 (triptyque QCD ; risques du projet) | lecture du plan retenu | [V] | F05 § 2 |

---

### 2.3 Coter le risque de non-conformité dans le plan de coût minimal, recalculer l'optimum en protégeant la qualité et recommander le plan à retenir (1 pt)

**Compétences visées :**
- `2.2.d` — Analyser les résultats obtenus (risques du projet, actions correctives)
- `2.5.b` — Analyser les risques rencontrés par l'organisation (criticité, échelles de cotation)

**Barème (1 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Plan de coût minimal : probabilité 40 % (niveau **3**), coût 36 + 14 = **50 k€** (gravité **3**), criticité **9**, risque **critique** : le directoire n'engage pas le projet sans mesure ; coût attendu 40 % × 50 = **20,0 k€** ; sans raccourcir H ni I : F seule (10 k€), **41 semaines**, retard 3 × 15 = 45 k€, **coût total 55 k€** (E à 18 k€ > 15 k€) ; risque 5 % (niveau 1) × 3 = **3**, faible, coût attendu **2,5 k€** | 0,5 |
| 2.3-02 | Comparaison : surcoût de la qualité préservée 55 − 42 = **13 k€** < réduction du coût attendu 20 − 2,5 = **17,5 k€** : gain attendu net **4,5 k€** (57,5 k€ contre 62 k€ risque compris) ; recommandation argumentée : retenir le plan à 41 semaines (qualité protégée) au nom du triptyque qualité-coût-délai (on cède deux semaines de délai et 13 k€ pour ramener un risque critique au niveau faible), de la perte de part non chiffrée et de l'enjeu stratégique de la première offre personnalisée ; prévenir tout de suite le client et négocier | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outils retenus : la **cotation du risque** (probabilité × gravité sur les échelles de l'annexe 2.4) pour qualifier le risque au regard de la règle du directoire, et son **coût attendu** (probabilité × coût) pour le comparer, en euros, au surcoût du plan qui protège la qualité. L'optimum est recalculé par le même arbitrage coût-délai, H et I étant tenues à leur durée normale.
- Alternatives acceptées : intégrer directement le coût attendu du risque dans le coût total des deux plans (62 k€ contre 57,5 k€) ; raisonner en seuil (protéger la qualité est rentable dès que la probabilité dans le plan de coût minimal dépasse 5 % + 13 / 50 = **31 %**) ; lecture par les coûts de la qualité (prévention contre défaillance externe).

**Conventions rappelées** (annexe 2.4)

- Criticité = niveau de probabilité × niveau de gravité ; critique ≥ 9, significatif 4 à 8, faible 1 à 3 ; coût attendu = probabilité × coût du risque s'il survient.
- Probabilité 5 % avec la formation sur site et les essais complets, 40 % dès que l'une de ces deux tâches est raccourcie ; coût d'une non-conformité 36 + 14 = 50 k€.

**Réponse attendue**

*Cotation dans le plan de coût minimal (2.3-01).* Ce plan raccourcit les essais de couleur de deux semaines et la formation sur site d'une semaine : la probabilité d'une campagne non conforme passe à **40 %** (niveau 3, de 25 % à moins de 50 %). Une non-conformité coûterait 36 k€ de réimpression et 14 k€ d'indemnité, soit **50 k€** (gravité 3, de 30 à moins de 75 k€). **Criticité 3 × 3 = 9 : risque critique**, que le directoire n'accepte pas sans mesure. Coût attendu : 40 % × 50 = **20,0 k€**.

*Optimum sans raccourcir H ni I (2.3-01).*

| Étape | Chemin critique | Possibilités (k€) | Choix | Durée | Accélération (k€) | Retard (k€) | **Coût total (k€)** |
|---|---|---|---|---:|---:|---:|---:|
| 0 | A-B-E-F-I-J-K (42) | F 10, E 18, K 20 | — | 42 | 0 | 60 | **60** |
| 1 | A-B-E-F-I-J-K (42) | F 10 | F | 41 | 10 | 45 | **55** |
| (2) | A-B-E-F-I-J-K (41) | E 18, K 20 | — | 40 | 28 | 30 | 58 |

Sans toucher à la formation sur site ni aux essais, seule la semaine gagnée sur les raccordements (10 k€) coûte moins qu'une semaine de retard : **41 semaines**, démarrage le vendredi 4 février 2028, trois semaines après la date du contrat ; **coût total 55 k€** (10 k€ d'accélération, 27 k€ de pénalités et 18 k€ de sous-traitance). La probabilité reste à 5 % (niveau 1) : criticité 1 × 3 = **3, risque faible** ; coût attendu 5 % × 50 = **2,5 k€**.

*Comparaison (2.3-02).*

| | Plan de coût minimal (39 semaines) | Qualité protégée (41 semaines) | Écart |
|---|---:|---:|---:|
| Coût total : accélération et retard (k€) | 42,0 | 55,0 | + 13,0 |
| Coût attendu du risque (k€) | 20,0 | 2,5 | − 17,5 |
| **Total, risque compris (k€)** | **62,0** | **57,5** | **− 4,5** |
| Criticité | 9 (critique) | 3 (faible) | |

Protéger la qualité coûte 13 k€ de plus en accélération et en retard, mais réduit le coût attendu du risque de 17,5 k€ : le plan à 41 semaines est **moins coûteux en espérance de 4,5 k€**. Le résultat tient tant que la probabilité d'une non-conformité dans le plan de coût minimal dépasse 31 % : l'estimation de 40 % laisse une marge, mais elle repose sur deux installations seulement.

*Recommandation (2.3-02).* Retenir le **plan à 41 semaines**, qui ne raccourcit que les raccordements.
- **Triptyque qualité-coût-délai** : le plan de coût minimal optimise le coût et le délai en reportant le risque sur la qualité ; le second cède deux semaines de délai et 13 k€ pour ramener un risque critique au niveau faible. Garder les essais et la formation complets relève de la **prévention**, moins coûteuse que la **défaillance externe** (réimpression, indemnité) qu'elle évite.
- **Ce que le calcul ne chiffre pas** : le client menace de réduire la part de LORSAVEL la deuxième année d'un contrat de 2,4 M€ par an ; une non-conformité au lancement de l'offre personnalisée, sur un client de la cosmétique qui ne tolère aucun écart de teinte, atteindrait la réputation de la société sur le segment que vise le deuxième axe du plan « LORSAVEL 2031 ». Ces enjeux renforcent la conclusion.
- **Relation avec le client** : le retard de trois semaines a lui aussi un coût relationnel. Il faut prévenir le client dès avril, en expliquant que le retard protège la conformité de ses teintes, et négocier : premières livraisons sur un nombre réduit de références, pénalité réduite ou plafonnée en contrepartie de bons à tirer sans écart. Les séries habituelles restent livrées à temps grâce au confrère.
- **Autres leviers à étudier**, sans toucher à la qualité : signer la commande avant le 26 avril (chaque semaine gagnée au départ vaut 15 k€ et ne coûte rien en accélération) ; programmer la formation chez le constructeur près de sa date au plus tard.

**Réponses tolérées**
- Plan à 39 semaines recommandé, si le candidat le justifie de manière argumentée et le **complète** par une mesure qui ramène le risque au niveau significatif (contrôle renforcé des premières campagnes, présence du constructeur au démarrage), conformément à la règle du directoire : 2.3-02 accordé à moitié au plus, le calcul de la comparaison étant juste.
- Coût attendu intégré au coût total sans tableau de comparaison, si les deux totaux (62 et 57,5 k€) sont justes.
- Probabilité exprimée en fraction (0,40) ou criticité représentée sur une matrice.
- Gravité cotée 4 en raison de la menace non chiffrée sur la deuxième année, si l'hypothèse est écrite (criticité 12, critique) : 2.3-01 accordé.

**Erreurs fréquentes**
- `JUR-T05` — Retenir le plan de coût minimal sans voir qu'il crée un risque critique, ou protéger la qualité sans chiffrer ce qu'elle coûte : l'arbitrage doit articuler calcul et stratégie.
- `JUR-T10` — Garder H ou I raccourcie dans le second plan ; oublier que le retard passe de 1 à 3 semaines (45 k€) ; comparer le surcoût au coût attendu total (20 k€) au lieu de sa réduction (17,5 k€).
- `JUR-T02` — Recommander sans parler du client : sa menace sur la deuxième année, la négociation du retard, la continuité de ses séries habituelles.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.5 (« notion de criticité des risques ») ; criticité = probabilité × gravité (sans auteur) | cotation | [V] programme ; [S] formule | F08 § 2.1 ; F13 § 6 |
| Programme UE 3, partie 2.2 (triptyque QCD ; risques du projet) | arbitrage qualité-coût-délai | [V] | F05 § 2, § 6 |
| Coûts de la qualité : prévention, détection, défaillances internes et externes | lecture du surcoût de la qualité préservée | [S] | F04 § 9 |

---

### 2.4 Note à M. CHARMEYRAN et au comité de pilotage du projet (20 lignes au maximum) (1 pt)

**Compétences visées :**
- `2.2.e` — Produire une synthèse rédigée et structurée concernant le pilotage du projet

**Barème (1 pt)** — grille de notation d'une réponse rédigée (six critères : concept défini et attribué ; mobilisation pertinente ; faits du cas ; analyse et non description ; préconisation faisable ; forme et longueur).

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Décision : démarrage à la fin de la semaine 41 (vendredi 4 février 2028), raccordements accélérés d'une semaine (10 k€), coût total 55 k€ ; formation sur site et essais complets, risque ramené de critique (9) à faible (3) ; ce qu'il faut dire au client et négocier | 0,5 |
| 2.4-02 | Trois indicateurs du tableau de bord du projet avec formule et seuil d'alerte : avancement des jalons (jalons atteints à leur date / jalons prévus à cette date) ; IPC = CBTE / CRTE ; IPD = CBTE / CBTP ; note structurée, 20 lignes au maximum, destinataires et objet | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : la **note de reporting** au comité de pilotage, structurée en situation, décision, conditions et suivi, appuyée sur un **tableau de bord du projet** réduit à quelques indicateurs ciblés, avec formule et seuil d'alerte, par axe du triptyque qualité-coût-délai.
- Alternatives acceptées : un indicateur de qualité en plus des trois demandés (bons à tirer signés sans reprise, essais conformes) ; seuils d'alerte différents s'ils sont justifiés (IPC ou IPD < 1 sur une tâche critique, par exemple) ; présentation en feux vert, orange et rouge.

**Réponse attendue** (modèle de note, 20 lignes au maximum)

À : M. CHARMEYRAN, comité de pilotage du projet ; de : contrôleur de gestion ; 6 avril 2027.

**Objet : troisième presse numérique, date de démarrage et moyens.**

**1. Situation.** Sans action, démarrage le 11 février 2028, quatre semaines après la date du contrat (14 janvier) : la livraison du constructeur dure 21 semaines. Une semaine de retard coûte 15 k€ (pénalité 9, sous-traitance 6).

**2. Décision proposée.** Démarrage le **vendredi 4 février 2028** ; raccordements en équipes alternées (une semaine, **10 k€**) ; coût total **55 k€**, dont 45 k€ de retard. Le plan à 42 k€ raccourcirait essais et formation : non-conformité à 40 % (criticité 9), coût attendu 20 k€ ; protéger la qualité coûte 13 k€ et en économise 17,5.

**3. Client.** Le prévenir dès avril : le délai protège ses teintes ; négocier un démarrage sur quelques références et la pénalité ; le confrère livre ses séries habituelles. À étudier : signer la commande avant le 26 avril.

**4. Tableau de bord** (revue hebdomadaire, comité mensuel).
- Avancement des jalons = jalons atteints à leur date / jalons prévus à cette date × 100 ; alerte dès qu'un jalon critique manque (livraison semaine 23, raccordement 29, calibration 34, bons à tirer 38).
- IPC = CBTE (coût budgété du travail effectué) / CRTE (coût réel du travail effectué) ; alerte sous 0,95.
- IPD = CBTE / CBTP (coût budgété du travail prévu) ; alerte sous 0,95, à lire avec la marge du chemin critique.

**Réponses tolérées**
- Note qui retient le plan à 39 semaines en le complétant d'une mesure de réduction du risque, en cohérence avec la question 2.3 (2.4-01 accordé à moitié au plus).
- Indicateurs formulés en valeur acquise et valeur planifiée (IPC = valeur acquise / coût réel ; IPD = valeur acquise / valeur planifiée).
- Note légèrement plus longue si elle reste structurée et lisible.

**Erreurs fréquentes**
- `JUR-T04` — Indicateurs sans formule ni seuil d'alerte, ou liste de nombreux indicateurs sans lien avec les risques du projet.
- `JUR-T03` — Note qui résume les calculs sans décision ni message pour le client.
- `JUR-T10` — Inverser les formules (CRTE / CBTE) ou confondre IPD et avancement des jalons.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.2 (« tableau de bord du projet et reporting ») | note au comité de pilotage | [V] | F05 § 7 |
| Méthode de la valeur acquise (CBTP, CRTE, CBTE ; IPC, IPD ; sans auteur) | indicateurs de coût et de délai | [V] programme et guide | F05 § 5 ; F13 § 8 |
