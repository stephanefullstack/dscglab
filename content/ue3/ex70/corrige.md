# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 3 – Contrôle de gestion et stratégie — Exercice d'entraînement n° 70 — Dossier 3 (6 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 pilotage stratégique et gestion prévisionnelle (§ 0, compétences ; § 2, boucle du pilotage ; § 5, écarts sur chiffre d'affaires et sur marge ; § 7, écarts conçus pour une situation atypique), F04 pilotage des processus de production (§ 8, coûts pertinents et approche marginale), F02 valeur et business model (§ 2, coût-volume-profit et levier opérationnel ; § 5, parties prenantes), F13 registre des auteurs (toutes à jour au 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (schéma conçu pour la marge contrôlé par la somme des sous-écarts ; tonnage et composition des destinations, chiffre d'affaires par destination et coûts variables recalculés ; lecture par cause et budget flexible contrôlés par la somme ; grandeurs du trafic au budget et au réel recalculées ; pistes de traction recalculées comme des décisions marginales ; grandeurs par destination, réponse à la coopérative et effets des préconisations : calculs divers recalculés par script ; barème partiel sur 6 ; liste noire ; hors-programme).

Bien que le corrigé mentionne des auteurs, des textes et des données, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur le choix et la justification des outils, la justesse des calculs, la pertinence de l'analyse au regard du cas et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet) ; pour chaque question, la présentation des concepts et outils avant leur mobilisation puis la conclusion sont notées. Une erreur n'est sanctionnée qu'une fois : les calculs et les analyses qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Procédure budgétaire dans la boucle du pilotage, budget par trafic qui décline le troisième axe du plan, contrôle qui confirme ou réoriente les choix, effet de la position d'associé-client | `3.1.a` S'approprier la boucle du pilotage stratégique | 1 |
| 3.2 Grandeurs du trafic céréalier au budget et au réel, écart total sur la marge, schéma conçu (tarif, tonnage, distance moyenne, chargement, coût du train-kilomètre) avec ses formules et contrôle de la somme | `3.1.c` Concevoir et mettre en œuvre des outils de contrôle budgétaire adaptés au contexte | 2 |
| 3.3 Interprétation des écarts par l'environnement et la traction, part maîtrisée et part subie chiffrées, réponse au reproche de la coopérative | `3.1.d` Interpréter les résultats obtenus | 1 |
| 3.4 Note à la présidente (20 lignes au maximum) : bilan du contrôle de 2027, préconisations sur le budget et les tarifs de 2028 et sur la traction, fondées sur l'effet marginal des pistes | `3.1.e` Élaborer des préconisations ; `3.1.f` Produire une synthèse rédigée et structurée portant sur la gestion prévisionnelle ; `2.1.e` Élaborer des préconisations en matière de gestion des processus de production ; `2.1.f` Produire une synthèse rédigée et structurée portant sur les décisions concernant les processus de production | 2 |
| **Dossier 3 – Piloter le trafic céréalier : boucle du pilotage, schéma d'écart sur la marge en tonnes-kilomètres et préconisations** | | **6** |

---

## DOSSIER 3 – PILOTER LE TRAFIC CÉRÉALIER : BOUCLE DU PILOTAGE, SCHÉMA D'ÉCART SUR LA MARGE EN TONNES-KILOMÈTRES ET PRÉCONISATIONS (6 points)

### 3.1 La procédure budgétaire dans la boucle du pilotage (1 pt)

**Compétences visées :**
- `3.1.a` — S'approprier la boucle du pilotage stratégique (budget par trafic, contrôle budgétaire, adaptation des choix, associés-clients)

**Barème (1 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Boucle présentée (stratégie → plan → budgets → réalisations → écarts → actions correctives ou réorientation), avec l'apprentissage en simple et en double boucle d'Argyris et Schön (1978) ; **budget par trafic** relié au troisième axe : il chiffre les tonnes, les destinations, les trains et les coûts de chaque trafic et fonde le tarif ; limites de la procédure actuelle reliées à l'annexe 3.1 : budget arrêté en novembre sur une récolte moyenne, jamais révisé, suivi mensuel des seules tonnes, contrôle quatorze mois après le budget, tarif unique quelle que soit la distance ; **trois leviers** que le contrôle peut confirmer ou réorienter : tarifs (indexation, distance), dessertes (malterie, port, gare de jonction), moyens de traction (locomotives, chargement des trains), avec le lien vers les axes 1 et 2 du plan | 0,5 |
| 3.1-02 | **Associé-client** : le même acteur fournit les prévisions de tonnage, paie le tarif, préfère un tarif bas à un dividende et reçoit le résultat du contrôle ; le budget devient un **outil de négociation et de justification** auprès d'une partie prenante puissante (Freeman, 1984) ; conséquences pour la boucle : prévisions à fiabiliser avec les chargeurs, risque d'un tarif négocié sous les coûts, nécessité d'un contrôle qui sépare ce que la société maîtrise de ce qui vient des chargeurs et de l'environnement ; conclusion : un contrôle annuel tardif ne permet ni d'adapter les choix pendant la campagne, ni de justifier les tarifs | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : la **boucle du pilotage stratégique** (programme, partie 3.1), lue avec l'**apprentissage en simple et en double boucle** d'Argyris et Schön (1978) : corriger l'action sans toucher aux normes (simple boucle), ou remettre en cause les hypothèses et les règles elles-mêmes (double boucle). Les associés-clients sont analysés comme des **parties prenantes**, au sens de Freeman (1984).
- Alternatives acceptées : une présentation du **cycle de contrôle** (prévoir, réaliser, comparer, corriger) appliquée au trafic céréalier ; la typologie de la saillance de Mitchell, Agle et Wood (1997) pour qualifier le poids de la coopérative (pouvoir, légitimité, urgence). Non accepté : une analyse des organes de la société ou des droits des associés (hors du programme de l'UE 3).

**Réponse attendue**

*Concept.* La **boucle du pilotage stratégique** relie la stratégie au plan à moyen terme, puis aux budgets annuels, qui déclinent la stratégie en actions et en chiffrent les conséquences. Le contrôle budgétaire compare ensuite les réalisations aux budgets. Il ne sert pas seulement à corriger : il doit **confirmer ou réorienter les choix**. Selon Argyris et Schön (1978), corriger l'action sans changer les normes relève de la simple boucle ; réviser les objectifs et les règles à partir des écarts relève de la double boucle.

*Le budget par trafic décline le troisième axe (3.1-01).* Le plan « TERNAVAL 2031 » demande de « renforcer le pilotage budgétaire de chaque trafic pour justifier les tarifs auprès des associés ». Le budget par trafic en est l'outil. Il traduit les prévisions des chargeurs en tonnes par destination, en trains et en trains-kilomètres. Il en déduit les coûts variables, la marge et la contribution de chaque trafic, puis le tarif. Le budget de 2027 a été bâti selon une procédure ancienne, avant le plan de juin 2027 ; celui de 2028 sera le premier à devoir le décliner. La procédure actuelle ferme mal la boucle :
- **Prévision** : le budget est arrêté en novembre, sur une récolte moyenne, alors que le tonnage dépend d'une moisson connue en juillet.
- **Suivi** : il n'est jamais révisé, et l'état mensuel ne suit que les tonnes. Personne ne voit la marge se dégrader pendant la campagne.
- **Contrôle** : la comparaison arrive en janvier, quatorze mois après le budget. Elle sert à rendre compte, plus à décider.
- **Tarif** : un tarif unique par tonne-kilomètre, quelle que soit la distance et sans indexation, laisse la société seule face aux coûts et à la concurrence routière. La règle a d'ailleurs dû être levée en juillet 2027 pour la malterie, sous la pression de la route (annexe 3.4) : une correction en simple boucle, faite hors de toute procédure, qui plaide pour revoir la structure du tarif.

*Ce que le contrôle peut confirmer ou réorienter.* Un contrôle par trafic qui décompose l'écart par cause permet d'agir sur trois leviers :
- **les tarifs** : simple boucle, ajuster le niveau du tarif ; double boucle, changer sa **structure**, en l'indexant sur le coût du train-kilomètre ou en le modulant selon la distance ;
- **les dessertes** : garder ou non les courtes distances que la route conteste (malterie), et suivre le report des exportations vers le port, signe que la remise aux opérateurs nationaux à la gare de jonction pèse sur les chargeurs. Ce constat conforte le premier axe du plan, le service de trains complets vers le port maritime ;
- **les moyens de traction** : le chargement des trains et les trains perdus mesurent en euros le coût des pannes. Ils chiffrent l'enjeu du deuxième axe du plan, fiabiliser la maintenance avant la campagne de 2028.

*Ce que change la position d'associé-client (3.1-02).* Chez TERNAVAL Fret, les principaux clients sont aussi les associés. La boucle s'en trouve modifiée à chaque étape :
- **Les prévisions viennent des clients** : le tonnage budgété est celui que les chargeurs annoncent en octobre. Une part de l'écart sur tonnage leur revient donc, comme la récolte moyenne retenue par la coopérative pour 2027.
- **Le budget fixe un prix payé par les associés** : la réunion tarifaire fait du budget un **outil de négociation**. Un associé qui paie le tarif sur tout son tonnage gagne plus à une baisse de tarif qu'à un dividende ; la coopérative le dit en demandant 0,010 € de moins par tonne-kilomètre.
- **Le contrôle est lu par ceux qu'il doit convaincre** : selon Freeman (1984), une partie prenante peut affecter la réalisation des objectifs de l'organisation, ou être affectée par elle. La coopérative, qui détient 40 % du capital et apporte l'essentiel des céréales, en est la plus puissante. Le contrôle doit donc être **lisible et partagé**. Il doit séparer ce qui relève de la société (pannes, chargement des trains) de ce qui vient des chargeurs ou de l'environnement (récolte, route, prix de l'énergie).

Conclusion : la boucle actuelle est annuelle et tardive. Elle ne permet ni de réagir pendant la campagne, ni de répondre aux associés-chargeurs autrement que par une négociation sur le seul niveau du tarif. Le troisième axe du plan suppose un budget révisé après la moisson, un contrôle de la marge par cause et des règles de tarif discutées à l'avance avec les associés.

**Réponses tolérées**
- Boucle présentée sans Argyris et Schön, si l'idée de réorientation des choix (et non de simple correction) figure.
- Lecture des associés-clients par les attentes et les contre-pouvoirs des parties prenantes, ou par le partage de la valeur entre la société et ses chargeurs, si elle reste reliée au budget et au tarif.

**Erreurs fréquentes**
- `JUR-G02` — Décrire la procédure de l'annexe 3.1 sans montrer ce que le contrôle permet de réviser l'année suivante.
- `JUR-T01` — Réciter la boucle du pilotage sans l'appliquer au budget par trafic et à la réunion tarifaire.
- `JUR-T05` — Traiter la position d'associé-client comme une question de droit des sociétés, sans lien avec le pilotage budgétaire.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 3.1 (l. 868-869 : boucle du pilotage) ; guide p. 124-125 (« confirmer ou réorienter les choix stratégiques ») | boucle du pilotage | [V] | F10 § 0, § 2 |
| Argyris et Schön, *Organizational Learning: A Theory of Action Perspective*, 1978 | simple et double boucle | [S] | F13 |
| Freeman, *Strategic Management: A Stakeholder Approach*, 1984 | parties prenantes | [S] | F13 ; F02 § 5 |

---

### 3.2 Le schéma d'écart sur la marge du trafic céréalier (2 pts)

**Compétences visées :**
- `3.1.c` — Concevoir et mettre en œuvre des outils de contrôle budgétaire adaptés au contexte (schéma d'écart conçu pour une marge en tonnes-kilomètres)

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Grandeurs au budget et au réel : tonnes-kilomètres **55 000 000** et **48 300 000** ; distance moyenne **40,00 km** et **42,00 km** ; trains **1 100** (440 / 220 / 440) et **1 000** (460 / 130 / 410) ; trains-kilomètres **88 000** et **84 000** ; chiffre d'affaires 7 700 000 € et 6 702 200 € ; coûts variables 770 000 € et 819 000 € ; marge sur coûts variables **6 930 000 €** et **5 883 200 €** ; écart total **− 1 046 800 €, défavorable** | 0,5 |
| 3.2-02 | Formules écrites et calculées : écart sur **tarif** = Σ (tarif réel − tarif budgété) × tonnes-kilomètres réelles = **− 59 800 €** ; écart sur **tonnage** = (tonnes réelles − tonnes budgétées) × distance moyenne budgétée × marge budgétée par tonne-kilomètre, avec marge budgétée par tonne-kilomètre = 0,140 − 2 × 8,75 / 1 250 = **0,1260 €** (soit 5,04 € par tonne), = **− 1 134 000 €** | 0,5 |
| 3.2-03 | Écart sur **distance moyenne** = tonnes réelles × (distance réelle − distance budgétée) × 0,126 = **+ 289 800 €** ; écart sur **chargement** = − coût budgété du train-kilomètre × (trains-kilomètres réels − 2 × tonnes-kilomètres réelles / chargement budgété) = − 8,75 × (84 000 − 77 280) = **− 58 800 €** ; écart sur **coût du train-kilomètre** = − (9,75 − 8,75) × 84 000 = **− 84 000 €** ; sens de chaque sous-écart | 0,5 |
| 3.2-04 | Contrôle : − 59 800 − 1 134 000 + 289 800 − 58 800 − 84 000 = **− 1 046 800 €** ; cohérence de la méthode (chaque facteur change une seule fois, écarts de prix sur les quantités réelles, écarts de quantité au tarif et au coût budgétés) ; mention qu'un autre ordre, justifié, donne d'autres sous-écarts de même total ; écart sur distance moyenne relu comme un **écart sur composition des destinations** | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : un **schéma d'écart conçu pour le cas**, qui suit la formation de la marge d'un trafic ferroviaire. Le chiffre d'affaires dépend des tonnes-kilomètres, donc du tonnage et de la distance ; les coûts dépendent des trains-kilomètres, donc des tonnes-kilomètres et du chargement des trains. L'écart classique en prix et en quantité de tonnes mélangerait la récolte, la composition des destinations et l'efficacité de la traction.
- Alternatives acceptées :
  - un **autre ordre** de décomposition, annoncé, justifié et appliqué de façon cohérente, s'il retrouve l'écart total. Par exemple, le coût du train-kilomètre isolé avant le chargement, aux trains-kilomètres qu'aurait donnés le chargement budgété (− 1 × 77 280 = **− 77 280 €**), puis le chargement au coût réel (− 9,75 × 6 720 = **− 65 520 €**) : la somme reste de − 142 800 € ;
  - un écart sur **volume en tonnes-kilomètres** (− 6 700 000 × 0,126 = − 844 200 €), décomposé ensuite en tonnage et distance ;
  - une décomposition par **destination**, avec la marge budgétée par tonne de chaque destination (port 6,30 €, malterie 2,52 €, gare de jonction 5,04 €), en volume global et en composition, si les cinq effets apparaissent ;
  - une présentation en budget flexible (question 3.3).

**Conventions rappelées** (annexe 3.3)

- Trains = tonnes / chargement moyen ; trains-kilomètres = 2 × distance × trains ; donc trains-kilomètres = 2 × tonnes-kilomètres / chargement.
- Marge = tarif × tonnes-kilomètres − coût du train-kilomètre × trains-kilomètres.
- Écart = réel − budget ; positif favorable sur la marge. Tarif et coût du train-kilomètre sur les quantités réelles ; tonnage, puis distance moyenne, puis chargement, au tarif et au coût budgétés.

**Réponse attendue**

*Concept.* Le contrôle budgétaire compare le réel au budget et décompose l'écart en causes, chacune rattachée à un responsable. Un **schéma conçu pour le cas** suit les facteurs qui forment la grandeur contrôlée. Ici, la marge s'écrit :

marge = tonnes × distance moyenne × tarif − coût du train-kilomètre × 2 × tonnes × distance moyenne / chargement

soit marge = tonnes × distance moyenne × (tarif − 2 × coût du train-kilomètre / chargement), avec un tarif moyen pondéré par les tonnes-kilomètres.

*Grandeurs du trafic (3.2-01).*

| Destination | Distance (km) | Tonnes-kilomètres budget | Tonnes-kilomètres réel | Trains budget | Trains réel | Trains-km budget | Trains-km réel |
|---|---:|---:|---:|---:|---:|---:|---:|
| Port d'Escaudrin | 50 | 27 500 000 | 26 450 000 | 440 | 460 | 44 000 | 46 000 |
| Malterie MALTEVIN | 20 | 5 500 000 | 2 990 000 | 220 | 130 | 8 800 | 5 200 |
| Gare de jonction | 40 | 22 000 000 | 18 860 000 | 440 | 410 | 35 200 | 32 800 |
| **Total** | | **55 000 000** | **48 300 000** | **1 100** | **1 000** | **88 000** | **84 000** |

| Élément | Budget | Réel |
|---|---:|---:|
| Tonnes | 1 375 000 | 1 150 000 |
| Distance moyenne (tonnes-kilomètres / tonnes) | 40,00 km | 42,00 km |
| Chiffre d'affaires | 55 000 000 × 0,140 = 7 700 000 | 26 450 000 × 0,140 + 2 990 000 × 0,120 + 18 860 000 × 0,140 = 6 702 200 |
| Coûts variables | 88 000 × 8,75 = 770 000 | 84 000 × 9,75 = 819 000 |
| **Marge sur coûts variables** | **6 930 000** | **5 883 200** |
| Taux de marge sur coûts variables | 90,00 % | 87,78 % |

**Écart total** = 5 883 200 − 6 930 000 = **− 1 046 800 €, défavorable**.

*Formules et calculs (3.2-02 et 3.2-03).* La marge budgétée par tonne-kilomètre vaut 0,140 − 2 × 8,75 / 1 250 = 0,140 − 0,014 = **0,1260 €** : chaque tonne-kilomètre coûte 0,0140 € de traction au budget. La marge budgétée par tonne vaut 40 × 0,126 = **5,04 €**.

| Sous-écart | Formule | Calcul | Montant (€) | Sens |
|---|---|---|---:|---|
| Tarif | Σ (tarif réel − tarif budgété) × tonnes-kilomètres réelles | (0,120 − 0,140) × 2 990 000 (port et gare de jonction : 0) | − 59 800 | défavorable |
| Tonnage | (T réel − T budget) × distance moyenne budgétée × marge budgétée par tonne-kilomètre | (1 150 000 − 1 375 000) × 40 × 0,126 | − 1 134 000 | défavorable |
| Distance moyenne | T réel × (distance moyenne réelle − budgétée) × marge budgétée par tonne-kilomètre | 1 150 000 × (42 − 40) × 0,126 | + 289 800 | favorable |
| Chargement des trains | − coût budgété du train-km × (trains-km réels − 2 × tonnes-km réelles / chargement budgété) | − 8,75 × (84 000 − 2 × 48 300 000 / 1 250) = − 8,75 × (84 000 − 77 280) | − 58 800 | défavorable |
| Coût du train-kilomètre | − (coût réel − coût budgété) × trains-km réels | − (9,75 − 8,75) × 84 000 | − 84 000 | défavorable |
| **Écart total** | marge réelle − marge budgétée | 5 883 200 − 6 930 000 | **− 1 046 800** | **défavorable** |

Les signes « − » des deux derniers écarts viennent de ce que les coûts diminuent la marge : des trains-kilomètres en plus ou un coût plus élevé réduisent la marge.

*Contrôle et cohérence (3.2-04).* − 59 800 − 1 134 000 + 289 800 − 58 800 − 84 000 = **− 1 046 800 €** : la somme retrouve l'écart total. Chaque facteur passe une seule fois du budget au réel. Les trois écarts de quantité s'enchaînent : le tonnage à la distance et au chargement budgétés, la distance au tonnage réel, le chargement aux tonnes-kilomètres réelles. Les deux écarts de prix portent sur les quantités réelles (tonnes-kilomètres réelles pour le tarif, trains-kilomètres réels pour le coût). Le résultat dépend de l'ordre : en isolant le coût du train-kilomètre avant le chargement, on obtiendrait − 77 280 € et − 65 520 €, pour le même total de − 142 800 €.

L'écart sur distance moyenne est un **écart sur composition des destinations**. Avec la marge budgétée par tonne de chaque destination (port 6,30 €, malterie 2,52 €, gare de jonction 5,04 €), et les 1 150 000 t réparties selon la composition budgétée (40 % / 20 % / 40 %) : port (529 000 − 460 000) × 6,30 = + 434 700 € ; malterie (149 500 − 230 000) × 2,52 = − 202 860 € ; gare de jonction (471 500 − 460 000) × 5,04 = + 57 960 € ; total **+ 289 800 €**. Le trafic s'est déplacé de la malterie (20 % → 13 % des tonnes) vers le port (40 % → 46 %), dont les tonnes portent plus de kilomètres.

**Réponses tolérées**
- Écarts présentés en k€, au dixième (− 1 046,8 k€).
- Formules écrites sous une forme équivalente, par exemple écart sur chargement = − 2 × 8,75 × 48 300 000 × (1 / 1 150 − 1 / 1 250).
- Ordre différent ou décomposition par destination, si elle est annoncée, cohérente et retrouve l'écart total (voir les alternatives).

**Erreurs fréquentes**
- `JUR-P01` — Se limiter à un écart sur chiffre d'affaires et à un écart sur coûts variables (− 997 800 € et − 49 000 €), sans isoler la distance, le chargement et le coût du train-kilomètre.
- `JUR-P03` — Calculer le train-kilomètre sur un aller simple, oublier le retour à vide, ou valoriser deux écarts aux mêmes valeurs, de sorte que la somme ne retrouve pas l'écart total.
- `JUR-T08` — Recopier une formule classique de volume et de composition sans l'adapter au cas.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 3.1 (l. 874 : « contrôle budgétaire : calculs et analyse d'écarts ») ; guide p. 125 (schémas adaptés à des situations spécifiques) ; rapport du jury 2025 p. 30 | schéma conçu pour le cas | [V] | F10 § 0, § 7 |
| Écarts sur marge à plusieurs produits : volume global et composition | lecture par destination | [V] LISEZMOI ; [S] | F10 § 5 |

---

### 3.3 Interpréter les écarts et répondre à la coopérative (1 pt)

**Compétences visées :**
- `3.1.d` — Interpréter les résultats obtenus (écarts reliés au micro et au macro-environnement et à la traction ; part maîtrisée et part subie)

**Barème (1 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Écarts **interprétés** et reliés aux faits de l'annexe 3.4 : tonnage (récolte, macro-environnement ; route à la malterie, menace des substituts ; trains perdus pendant les pannes, fonctionnement interne) ; distance moyenne favorable mais **trompeuse** (perte des courtes distances, report vers le port faute de fiabilité à la gare de jonction) ; tarif (choix commercial pour garder la malterie) ; chargement (trains incomplets pendant les pannes) ; coût du train-kilomètre (gazole, redevance) ; **part maîtrisée et part subie chiffrées** : subi − 355 152 € (récolte − 560 952 €, coût du train-kilomètre − 84 000 €, composition + 289 800 €), commercial − 412 600 € (route − 352 800 €, tarif − 59 800 €), pannes − 279 048 € (trains perdus − 220 248 €, chargement − 58 800 €) | 0,5 |
| 3.3-02 | Réponse argumentée à la coopérative : une marge sur coûts variables de **87,78 %** n'est pas un résultat ; après 5 400 k€ de charges fixes propres, la contribution du trafic tombe à **483 200 €** (7,21 % du chiffre d'affaires, contre 1 530 000 € et 19,87 % au budget) ; la baisse demandée de 0,010 € par tonne-kilomètre coûterait **483 000 €**, presque toute la contribution ; le tarif n'explique que 59 800 € de l'écart, le tonnage 1 134 000 € ; le reproche est en partie fondé sur les courtes distances et sur la lisibilité du tarif, qui appellent une autre structure de tarif plutôt qu'une baisse générale | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : une **lecture des écarts par cause**, à partir des estimations de l'annexe 3.4. Chaque cause est rattachée à son origine (macro-environnement, concurrence, chargeurs, fonctionnement interne) et qualifiée de maîtrisée ou de subie. Le **raisonnement coût-volume-profit** sert ensuite à répondre à la coopérative : contribution, poids des charges fixes et levier opérationnel.
- Alternatives acceptées : un **budget flexible** au tonnage réel (1 150 000 × 5,04 = 5 796 000 €), qui isole l'écart de volume (− 1 134 000 €) d'un écart du réel sur le budget flexible de **+ 87 200 €** ; une autre répartition entre maîtrisé et subi, si elle est justifiée (par exemple la route rangée parmi les écarts subis, ou la composition parmi les écarts commerciaux). L'orge partie par la route peut aussi être valorisée à la marge de la malterie (70 000 × 2,52 = − 176 400 €), la différence se retrouvant alors dans l'écart sur composition.

**Réponse attendue**

*Concept.* Interpréter un écart, ce n'est pas le décrire (« le tonnage a baissé ») : c'est en trouver la cause, dire qui en répond et ce qu'il annonce pour la suite. Un écart **subi** vient de l'environnement ; un écart **maîtrisé** relève des choix ou du fonctionnement de la société.

*Interprétation par cause (3.3-01).*

| Origine | Cause (annexe 3.4) | Montant (€) | Lecture |
|---|---|---:|---|
| Subi : macro-environnement | récolte inférieure à la récolte moyenne retenue (111 300 t × 5,04) | − 560 952 | aléa climatique ; il vient aussi d'une prévision fondée sur une récolte moyenne, fournie par la coopérative |
| Subi : prix de l'énergie et de l'infrastructure | gazole + 0,75 € et redevance + 0,25 € par train-kilomètre | − 84 000 | hausse que le tarif, non indexé, ne répercute pas ; 1,25 % du chiffre d'affaires réel |
| Subi en partie : comportement des chargeurs | composition des destinations : moins de courtes distances, report vers le port (près de 29 000 t) | + 289 800 | favorable en apparence ; voir ci-dessous |
| Commercial : concurrence routière | orge de la malterie partie par la route (70 000 t × 5,04) | − 352 800 | menace des substituts sur les courtes distances |
| Commercial : choix de la société | tarif de 0,120 € consenti à la malterie | − 59 800 | prix consenti pour garder 149 500 t |
| Maîtrisable : traction et maintenance | 38 trains perdus pendant les pannes (43 700 t × 5,04) | − 220 248 | défaillance interne, enjeu du deuxième axe du plan |
| Maîtrisable : traction et maintenance | trains incomplets (1 150 t contre 1 250 t) | − 58 800 | même cause : moins de locomotives, dessertes maintenues |
| **Total** | | **− 1 046 800** | |

- **Le tonnage explique plus que l'écart total** (108,33 %). La récolte en est la première cause, et la société la subit. Mais deux autres causes relèvent d'elle : les trains perdus pendant les pannes, et l'orge que la malterie a confiée à la route. Pour la malterie, la route est un **substitut**, au sens des cinq forces de Porter (1979). Sur vingt kilomètres, le camion charge au silo et livre au quai sans manœuvre, alors que le tarif au kilomètre du train est le même à vingt et à cinquante kilomètres.
- **L'écart sur distance moyenne est favorable, mais il ne mesure aucune performance.** La distance moyenne passe de 40 à 42 km parce que le trafic court de la malterie a fondu (− 45,64 %) et que des exportations sont passées de la gare de jonction au port. La société gagne des tonnes-kilomètres en perdant des clients sur les courtes distances. Le report vers le port signale aussi que la remise aux opérateurs nationaux, sans date garantie pendant la campagne, détourne les chargeurs de la gare de jonction : c'est l'argument du premier axe du plan.
- **Le tarif consenti à la malterie** est un choix raisonné à la marge : à 0,120 €, la tonne-kilomètre rapporte encore bien plus que son coût variable réel (2 × 9,75 / 1 150 = **0,0170 €**). Le trafic gardé dégage 308 100 € de marge sur coûts variables (358 800 − 5 200 × 9,75).
- **La traction** a perdu 279 048 € pendant les pannes : 38 trains, puis des trains incomplets pour ne laisser aucun silo sans desserte. C'est le coût, mesuré en marge, d'une maintenance que le deuxième axe du plan doit fiabiliser.
- **Le coût du train-kilomètre** (− 84 000 €) est subi à court terme, mais la société en porte seule le risque, faute d'indexation du tarif.

Au total, **355 152 €** de l'écart sont subis (récolte et coûts, nets du gain de composition), **412 600 €** tiennent à la position commerciale sur les courtes distances et **279 048 €** au fonctionnement de la traction pendant les pannes. Au tonnage réel, la marge dépasse même le budget flexible de 87 200 € ; ce résultat ne tient qu'au gain de composition, et il passerait à − 202 600 € sans lui.

*Réponse à la coopérative PLAINAVRE (3.3-02).*
- **La coopérative confond la marge sur coûts variables et le résultat.** Le taux de marge sur coûts variables atteint bien 87,78 % (90,00 % au budget), parce que le coût variable de la traction est faible : 0,0170 € par tonne-kilomètre. Mais le ferroviaire est une activité à **charges fixes élevées** : locomotives, conducteurs affectés à la campagne, wagons, embranchements. Après 5 400 k€ de charges fixes propres, la contribution du trafic céréalier tombe à **483 200 €**, soit 7,21 % de son chiffre d'affaires, contre 1 530 000 € au budget. L'ensemble de la société n'a dégagé que 0,6 M€ de résultat d'exploitation.
- **Le levier opérationnel** dit le risque : la contribution a fondu de 68 % pour une baisse du tonnage de 16,36 %. Le rapport de la marge à la contribution passe de 4,53 au budget à 12,18 au réel.
- **Le tarif n'est pas la cause de l'écart** : il n'en explique que 59 800 €, et il a baissé pour la malterie. La baisse demandée, 0,010 € par tonne-kilomètre (− 7,14 %), coûterait **483 000 €** sur les tonnes-kilomètres de 2027, presque toute la contribution du trafic.
- **Le reproche est pourtant en partie fondé.** Sur les courtes distances, le tarif unique au kilomètre rend la route compétitive. Les hausses du gazole et de la redevance ont été absorbées sans règle connue à l'avance. La coopérative a enfin subi les 38 trains perdus. La réponse n'est pas une baisse générale du tarif, mais une **autre structure de tarif** et des engagements réciproques : fiabilité des trains d'un côté, prévisions et tonnage engagés de l'autre.

**Réponses tolérées**
- Répartition maîtrisé / subi différente, justifiée (la récolte peut être dite « subie, mais mal prévue » ; la route, « subie » si l'on juge la réponse commerciale impossible).
- Réponse à la coopérative sans le levier opérationnel, si la confusion entre marge et résultat est démontrée par la contribution.

**Erreurs fréquentes**
- `JUR-T03` — Paraphraser les écarts (« l'écart sur tonnage est défavorable de 1 134 000 € ») sans cause ni conséquence.
- `JUR-G02` — Ne pas relier les écarts à l'environnement (récolte, route, énergie) et aux faits de la traction.
- `JUR-T02` — Lire l'écart sur distance comme une bonne performance, ou répondre à la coopérative sans aucun chiffre du cas.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide p. 125 : « non pas décrire, ni commenter, mais interpréter » ; sujet 2024 q. 2.1 | interprétation des écarts | [V] | F10 § 0, § 5 |
| Porter, « How Competitive Forces Shape Strategy », *HBR*, 1979 | menace des substituts | [V] | F13 |
| Coût-volume-profit, contribution et levier opérationnel | réponse à la coopérative | [S] | F02 § 2 |
| Coûts pertinents et approche marginale | tarif plancher de la malterie | [V] | F04 § 8 |

---

### 3.4 Note à Mme DARVAUX (20 lignes au maximum) (2 pts)

**Compétences visées :**
- `3.1.e` — Élaborer des préconisations (budget et tarifs de 2028)
- `3.1.f` — Produire une synthèse rédigée et structurée portant sur la gestion prévisionnelle
- `2.1.e` — Élaborer des préconisations en matière de gestion des processus de production (traction : locomotive de réserve, dessertes regroupées, par l'approche marginale)
- `2.1.f` — Produire une synthèse rédigée et structurée portant sur les décisions concernant les processus de production

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | **Bilan du contrôle de 2027**, chiffré et hiérarchisé : marge 5 883 k€, − 1 047 k€ ; contribution 483 k€ ; tonnage − 1 134 k€ (récolte, route, pannes) ; tarif − 60 k€ seulement ; distance favorable mais trompeuse ; réponse de principe à la coopérative (pas de baisse générale) | 0,5 |
| 3.4-02 | **Budget et tarifs de 2028** : budget révisé après la moisson et suivi mensuel de la marge pendant la campagne, avec un contrôle qui sépare écarts subis et maîtrisés ; tarif indexé sur le coût du train-kilomètre (environ 0,0017 € par tonne-kilomètre pour 1 € par train-kilomètre, à 1 150 t par train), selon une règle annoncée ; tarif selon la distance, avec un plancher au coût variable (0,0170 € par tonne-kilomètre) et un engagement de tonnage des chargeurs | 0,5 |
| 3.4-03 | **Traction**, préconisations fondées sur l'effet marginal : piste A, + 285 768 € de marge contre 140 000 € de location, soit **+ 145 768 €** ; piste B, **+ 76 250 €** seule mais **+ 10 730 €** seulement après la piste A ; hiérarchie (A d'abord, B à tester sur quelques silos) et conditions (silos qui chargent à l'heure, conducteurs) ; deux ou trois indicateurs de suivi (chargement moyen, trains perdus, coût du train-kilomètre, marge par tonne-kilomètre) | 0,5 |
| 3.4-04 | **Forme** : note adressée et structurée, 20 lignes au maximum, chiffres repris des questions précédentes, lien avec les trois axes du plan et avec les associés-chargeurs, conclusion qui prend position | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : une **note de synthèse et de préconisation** qui relie le contrôle budgétaire aux décisions de 2028. Les pistes de traction sont jugées par l'**approche marginale** : seuls comptent les coûts et les marges qui changent avec la décision. L'effet d'une piste dépend aussi de la situation de départ : la piste B rapporte 76 250 € seule, mais 10 730 € seulement si la piste A a déjà rétabli des trains de 1 250 t.
- Alternatives acceptées : une note en deux parties (tarifs et budget, puis traction), si les quatre éléments du barème y figurent ; la piste B retenue d'emblée, si l'argument de la faible marge après la piste A est discuté ; un tarif à deux composantes (une part fixe par tonne et une part par tonne-kilomètre) à la place d'un tarif par tranches de distance.

**Réponse attendue** (modèle de note, 20 lignes au maximum)

> **À Mme Hélène DARVAUX — Objet : trafic céréalier, contrôle de 2027 et propositions pour la réunion tarifaire de février 2028**
>
> **1. Ce que révèle 2027.** La marge sur coûts variables du trafic céréalier atteint 5 883 k€, soit 1 047 k€ de moins que le budget. Après 5 400 k€ de charges fixes propres, le trafic ne contribue plus que pour 483 k€. Le tonnage explique tout l'écart (− 1 134 k€) : récolte − 561 k€, orge de la malterie partie par la route − 353 k€, trains perdus pendant les pannes − 220 k€. Le tarif n'en explique que 60 k€. Le gain de distance (+ 290 k€) vient de la perte des courtes distances : c'est une fragilité, pas une performance.
>
> **2. Réponse à la coopérative.** Une marge de 88 % n'est pas un bénéfice. La baisse demandée, 0,010 € par tonne-kilomètre, coûterait 483 k€, toute la contribution du trafic. Je propose de la refuser, mais de rendre le tarif lisible et prévisible.
>
> **3. Budget et tarifs de 2028.** (1) Réviser le budget en août, après la moisson, et suivre chaque mois la marge et ses écarts, en séparant ce qui est subi de ce qui est maîtrisé. (2) Indexer le tarif sur le coût du train-kilomètre : + 0,0017 € par tonne-kilomètre pour 1 € de hausse, selon une règle annoncée en décembre. (3) Moduler le tarif selon la distance : plus bas sur les courtes distances, jamais sous 0,0170 € par tonne-kilomètre, en échange d'un engagement de tonnage des chargeurs.
>
> **4. Traction.** (1) Louer une locomotive de réserve pour la campagne : + 146 k€ net. (2) Tester les dessertes regroupées sur quelques silos : + 76 k€ seules, 11 k€ après la location. (3) Suivre chaque semaine le chargement moyen (cible 1 250 t), les trains perdus (cible 0) et le coût du train-kilomètre.
>
> **En conclusion**, présentons aux associés un budget partagé et révisable : des tarifs justifiés par les coûts, et des trains fiables en contrepartie de leurs engagements.

**Réponses tolérées**
- Révision du budget à une autre date (fin de la moisson, fin de la campagne), ou budget glissant par trimestre, si l'objectif de suivre la marge pendant la campagne est atteint.
- Indexation sur le seul gazole (0,75 € par train-kilomètre en 2027, environ 0,0013 € par tonne-kilomètre), si la règle est expliquée.
- Montants arrondis au k€ dans la note.
- Piste B calculée avec un nombre de trains arrondi à l'unité par destination (378, 107 et 337 trains de 1 400 t : 69 040 trains-kilomètres, + 75 860 € net seule), si l'arrondi est annoncé.

**Erreurs fréquentes**
- `JUR-T06` — Dépasser les 20 lignes, ou rédiger une note sans structure ni conclusion.
- `JUR-G02` — Constater les écarts sans préconisations pour 2028, ou proposer des actions sans les chiffrer à partir des écarts.
- `JUR-T05` — Séparer la tarification de la traction : les pannes ont coûté plus que le tarif consenti à la malterie, et la fiabilité des trains est la contrepartie que les associés-chargeurs attendent.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 3.1 (l. 876 : préconisations) ; guide p. 125 et 146-147 (révision des prix, synthèse) | préconisations et synthèse budgétaires | [V] | F10 § 0 |
| Programme UE 3, partie 2.1 ; guide p. 120 (approche marginale, coûts pertinents) | pistes de traction | [V] | F04 § 8 |
| Grille à six critères des réponses rédigées | notation | [V] | gabarits/corrige_ue3_template.md ; bareme_grille.yaml |

---

## Contrôles avant publication

- [x] `python3 -I outils/dscgcheck ue3/exercices/ex70_ecarts_marge_trafic_cerealier/corrige.yaml` : 0 erreur, 0 avertissement ; schéma conçu pour la marge contrôlé par la somme des sous-écarts ; tonnage et composition des destinations, chiffre d'affaires par destination et coûts variables recalculés ; lecture par cause et budget flexible contrôlés par la somme ; grandeurs du trafic au budget et au réel recalculées ; pistes A et B recalculées comme des décisions marginales ; grandeurs par destination, réponse à la coopérative et effets des préconisations : calculs divers recalculés par script (`/paperclip/shared/dscglab-travail/DSC-1339/calculs.py`) ; barème partiel sur 6 ; liste noire ; hors-programme.
- [x] Données partagées du sujet n° 24 respectées : trafic céréalier réel de 1,15 Mt, concentré de juillet à novembre ; coopérative PLAINAVRE à 40 % ; pannes de la campagne de 2027 (38 trains perdus, comme au dossier 2) ; hausse du gazole et de la redevance ; chiffre d'affaires céréalier de 6,7 M€, compatible avec 21,4 M€ au total ; gare de jonction à 40 km des silos, gazole et part variable des conducteurs compatibles avec le dossier 1 ; présentation commune reprise mot pour mot.
- [x] Compétences visées présentes dans `programme/perimetre_ue3.yaml` ; schéma conçu pour le cas, formules non données dans l'énoncé ; chaque question présente le concept, l'applique au cas, conclut ; synthèse bornée (3.4, 20 lignes au maximum) ; ni budget de trésorerie, ni état financier prévisionnel, ni question sur les organes de la société.
- [x] Entités et personnes fictives (Mme Maëlle TRÉVANDIER ; M. Bastien QUERVILLAC repris du dossier 2 ; transporteur routier, opérateurs nationaux et gestionnaire de l'infrastructure non nommés) ; aucun prix réel du gazole, aucune redevance réelle, aucun tarif réel du transport routier ; distances, tarifs, chargements et coûts présentés comme des hypothèses du cas.
