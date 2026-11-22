# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 43

**DOSSIER 1 – PRÉPARER LES CHOIX STRATÉGIQUES ET LE PILOTAGE DU SYSTÈME D'INFORMATION (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 15, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. AMPÉRANE est une société par actions simplifiée créée en 2018, dont le siège est à Nantes. Opérateur de bornes de recharge pour véhicules électriques, elle installe, exploite et entretient des points de recharge sur des sites que lui confient leurs propriétaires : parkings de supermarchés, hôtels et restaurants, aires de services, parkings de collectivités et d'entreprises. Elle vend la recharge aux conducteurs, qui paient par son application, par carte bancaire sur les bornes rapides ou avec la carte ou l'application de leur opérateur de mobilité, grâce à deux plateformes d'itinérance. Ses fondateurs et ses salariés détiennent 34 % de son capital, deux fonds d'infrastructure 66 %. Fin 2026, AMPÉRANE exploitait 8 000 points de recharge, dont 2 400 rapides, sur 1 200 sites ; elle a enregistré 4 millions de sessions de recharge en 2026 et réalisé un chiffre d'affaires de 118 M€. Elle emploie 430 salariés. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « AMPÉRANE 2030 », adopté en janvier 2027 par la présidente après avis du comité de surveillance, où siègent les deux fonds, fixe cinq objectifs : porter le réseau à 20 000 points de recharge en 2030 ; garantir à chaque point une disponibilité d'au moins 98 % ; généraliser en 2027 une tarification variable selon l'heure et l'affluence ; tirer de nouvelles recettes des données et des services aux sites hôtes ; rendre la recharge accessible à tous en réduisant l'empreinte environnementale du réseau. Toutes les bornes sont pilotées par CIRCÉA, la plateforme de supervision et de gestion développée en interne depuis 2019. Les fonds, qui envisagent une nouvelle levée de fonds en 2028, demandent un système d'information sûr, documenté et piloté.

Vous êtes directeur(rice) de cabinet de la présidente, Mme Hélène SORBADIÈRE, depuis 2025 ; vous suivez le plan stratégique et les dossiers transverses de l'entreprise. Mme SORBADIÈRE vous demande trois travaux : préparer les choix stratégiques et le pilotage du système d'information (dossier 1) ; organiser, exploiter et valoriser les données de recharge (dossier 2) ; sécuriser la plateforme et les bornes, auditer la tarification variable et rendre le réseau plus responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation d'AMPÉRANE et chiffres clés

AMPÉRANE est une société par actions simplifiée créée en 2018, dont le siège est à Nantes. Opérateur de bornes de recharge pour véhicules électriques, elle installe, exploite et entretient des points de recharge sur des sites que lui confient leurs propriétaires, les sites hôtes. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Le modèle et les actionnaires**

| Donnée | Valeur |
|---|---|
| Sites hôtes | propriétaires de parkings de supermarchés, d'hôtels et de restaurants, d'aires de services, de parkings de collectivités et d'entreprises, qui confient un emplacement à AMPÉRANE ; AMPÉRANE leur vend aussi des services (rapports d'activité, partage des recettes) |
| Conducteurs | environ 650 000 conducteurs différents en 2026, dont 120 000 utilisateurs actifs de l'application d'AMPÉRANE |
| Paiement des sessions | par l'application d'AMPÉRANE ; par carte bancaire sur les bornes rapides ; avec la carte ou l'application de leur opérateur de mobilité, grâce à deux plateformes d'itinérance qui relient AMPÉRANE à ces opérateurs |
| Actionnaires | fondateurs et salariés : 34 % ; fonds d'infrastructure VARNEDAL Infrastructures : 46 % ; fonds d'infrastructure OSTRALIN Transition : 20 % |
| Comité de surveillance | les deux fonds y siègent ; il donne son avis sur la stratégie et sur les investissements importants |

**Le réseau et l'activité en 2026**

| Donnée | Valeur |
|---|---|
| Points de recharge (fin 2026) | 8 000 : 2 400 rapides et 5 600 normaux ; une borne porte d'un à quatre points ; bornes de quatre constructeurs |
| Sites hôtes | 1 200 : parkings de supermarchés 55 % ; hôtels et restaurants 20 % ; aires de services 10 % ; parkings de collectivités et d'entreprises 15 % |
| Sessions de recharge | 4 millions, payées à 40 % par l'itinérance, à 35 % par l'application et à 25 % par carte bancaire sur les bornes rapides |
| Chiffre d'affaires | 118 M€ : vente de recharge 108 M€ ; services aux sites hôtes 10 M€ |
| Dépenses du système d'information, hors rémunérations des équipes internes | environ 14 M€, dont 6 M€ de services en ligne et de prestations et 2,4 M€ d'hébergement |
| Maintenance | 45 % des interventions de maintenance confiées à sept entreprises de maintenance sous-traitantes régionales |

**L'effectif au 31/12/2026**

| Direction ou service | Salariés |
|---|---|
| Exploitation et maintenance, dont 90 techniciens itinérants et 40 personnes au centre de supervision, ouvert jour et nuit | 150 |
| Direction technique : équipes produit et développement de CIRCÉA, données, infrastructure | 110 |
| Développement du réseau : recherche de sites, relations avec les sites hôtes, travaux | 70 |
| Service clients, ouvert jour et nuit | 50 |
| Fonctions support : finances, achats, ressources humaines, juridique | 50 |
| **Total** | **430** |

**Le système d'information en quelques lignes**

- **CIRCÉA**, plateforme de supervision et de gestion des bornes développée en interne depuis 2019 : commande à distance des bornes, sessions, tarifs, mises à jour des micrologiciels, échanges avec les plateformes d'itinérance. Elle est hébergée chez un fournisseur de cloud dont le siège est hors de l'Union européenne, dans une région de centres de données située en France.
- Application mobile des conducteurs ; terminaux de paiement par carte bancaire sur les bornes rapides.
- Bornes reliées à CIRCÉA par le réseau mobile d'un opérateur.
- Logiciel en ligne de gestion des interventions, partagé avec les entreprises de maintenance ; logiciel en ligne de relation clients ; progiciel de gestion intégré (finances, achats).

**Organigramme simplifié (mars 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | comité de surveillance, où siègent les deux fonds | — |
| — | présidente | Mme Hélène SORBADIÈRE |
| Rattachés à la présidente | directeur(rice) de cabinet | vous |
| | direction technique | M. Yann QUÉLAVEC |
| | direction de l'exploitation et de la maintenance (techniciens, centre de supervision) | Mme Sandrine FOLCARIAS |
| | direction du développement du réseau | Mme Pauline ESCARDINE |
| | service clients | M. Romain TÉVENARD |
| | direction administrative et financière (finances, achats, ressources humaines, juridique) | M. Olivier MANTRELLE |

### ANNEXE 1.2 – CIRCÉA dans l'activité d'AMPÉRANE (note de M. Yann QUÉLAVEC, directeur technique, et témoignages recueillis en février 2027)

**A. Ce que fait CIRCÉA pour chaque activité**

| Activité | Qui la conduit | Ce que fait CIRCÉA | Constats de 2026 |
|---|---|---|---|
| Recherche et contractualisation des sites | développement du réseau | rien : les prospects et les contrats des sites hôtes sont suivis dans le logiciel de relation clients et dans des tableurs | pour atteindre 20 000 points en 2030, il faut ouvrir environ 450 sites par an |
| Installation et mise en service | développement du réseau (travaux), avec des entreprises d'installation | déclare chaque borne, la configure et la teste à distance, l'ouvre à la vente | un nouveau site est ouvert à la vente deux jours après la fin des travaux |
| Exploitation et maintenance | exploitation et maintenance (centre de supervision, techniciens) | supervise les bornes jour et nuit, les commande à distance (redémarrage, reconfiguration), lit leurs codes d'erreur, met à jour leurs micrologiciels ; le centre de supervision crée ensuite à la main la demande d'intervention dans le logiciel de gestion des interventions | 70 % des pannes sont résolues à distance, sans déplacement ; disponibilité moyenne du réseau : 97 % ; la moitié des points est sous 98 % |
| Vente de la recharge | direction technique (tarifs), direction administrative et financière | fixe les tarifs de chaque point, autorise et enregistre les sessions, échange avec les deux plateformes d'itinérance | 4 millions de sessions ; le module de tarification variable, en pilote sur une partie du réseau depuis le quatrième trimestre 2026, a été développé en interne en cinq mois |
| Relation avec les conducteurs | service clients | alimente l'application (points libres en temps réel, démarrage et suivi de la session, historique) ; donne au service clients l'état de chaque borne et la commande à distance | — |
| Services aux sites hôtes | développement du réseau | calcule chaque mois le partage des recettes avec chaque site et produit un rapport d'activité standard (sessions, énergie délivrée, recettes) | 10 M€ de chiffre d'affaires ; les sites hôtes demandent des rapports adaptés et un accès en ligne à leurs chiffres, que CIRCÉA ne fournit pas |

Pour les fonctions support, CIRCÉA transmet chaque mois les sessions et les recettes au progiciel de gestion intégré. Lors des achats de bornes, elle permet de mettre en concurrence les constructeurs : en 2026, les bornes d'un quatrième constructeur ont été intégrées à CIRCÉA en deux mois. L'équipe produit et développement de CIRCÉA compte 60 des 110 personnes de la direction technique.

**B. Faits complémentaires**

- Selon le cabinet de conseil mandaté par les fonds en 2026, les opérateurs comparables qui utilisent une solution du marché résolvent à distance environ la moitié de leurs pannes, et il leur faut six à neuf mois pour faire intégrer un nouveau modèle de borne par leur éditeur.
- En 2026, l'équipe de CIRCÉA a consacré 60 % de son temps à la tarification variable et à l'intégration du quatrième constructeur, 30 % à l'exploitation et à la sécurité de la plateforme, 10 % aux demandes du développement du réseau.
- 45 demandes d'évolution du développement du réseau et de l'exploitation sont en attente ; le délai moyen de réalisation d'une demande est de six mois.
- La documentation de CIRCÉA est incomplète ; deux développeurs expérimentés ont quitté l'entreprise en 2026.
- Selon M. Olivier MANTRELLE, directeur administratif et financier, un point de disponibilité du réseau représente environ 1 M€ de ventes de recharge par an.

**C. Témoignages**

**M. Arnaud TREVÉLOC, représentant de VARNEDAL Infrastructures au comité de surveillance** : « Un opérateur n'a pas à être éditeur de logiciel. Soixante développeurs, c'est le coût d'un éditeur sans ses clients. Achetons une solution du marché et concentrons-nous sur les sites. »

**M. Yann QUÉLAVEC, directeur technique** : « CIRCÉA est ce qui nous distingue : la disponibilité, parce que nous réglons sept pannes sur dix sans camion ; la tarification variable, que nous avons construite en cinq mois ; la rapidité d'intégration de nouveaux constructeurs, qui nous laisse libres de nos achats. »

**Mme Pauline ESCARDINE, directrice du développement du réseau** : « Mes demandes passent toujours après le reste. J'attends depuis un an un accès en ligne aux chiffres pour les sites hôtes. En décembre, une chaîne d'hôtels de quarante établissements a choisi un concurrent qui lui offrait ce suivi. »

### ANNEXE 1.3 – Les deux options pour la plateforme (note de la direction technique et offre d'un éditeur, février 2027)

**A. Hypothèses communes**

- Périmètre comparé : la plateforme de supervision et de gestion seule (CIRCÉA ou la solution en ligne de l'éditeur). L'application des conducteurs, le logiciel de gestion des interventions, le logiciel de relation clients et le progiciel de gestion intégré ne changent pas.
- Croissance du réseau (points de recharge en fin d'année) : 8 000 en 2026 ; 11 000 en 2027 ; 14 000 en 2028 ; 17 000 en 2029 ; 20 000 en 2030.
- Coût d'une personne de l'équipe : 80 k€ par an, charges comprises.
- Montants en k€, sur les quatre années 2027 à 2030, additionnés tels quels.

**B. Option A – Garder et renforcer CIRCÉA**

| Poste | 2027-2030 |
|---|---|
| Équipe produit et développement actuelle (60 personnes) | 19 200 |
| Renfort de 10 personnes à partir de 2028 (développeurs et spécialistes de la sécurité), frais de recrutement compris | 2 600 |
| Hébergement de CIRCÉA (1 200 en 2027, puis croissance avec le réseau) | 5 600 |
| Outils de sécurité et documentation de la plateforme | 600 |

**C. Option B – Solution en ligne d'un éditeur**

L'éditeur est une entreprise européenne qui fournit sa solution en ligne à une quarantaine d'opérateurs de recharge.

| Poste | 2027-2030 |
|---|---|
| Abonnement : 150 € par point et par an (12,50 € par mois), facturé sur le parc moyen de chaque année (9 500 points en 2027, puis 12 500, 15 500 et 18 500) | 8 400 |
| Équipe interne de 25 personnes dès 2027 (pilotage de l'éditeur, paramétrage, interfaces, assistance aux utilisateurs) | 8 000 |
| Migration des 8 000 points en 2027 par l'éditeur (reconfiguration des bornes, reprise des données, essais) | 2 000 |
| Interfaces avec l'application des conducteurs, le logiciel de gestion des interventions, le progiciel de gestion intégré et les deux plateformes d'itinérance | 1 200 |
| Formation des équipes du centre de supervision, du service clients et du développement du réseau | 300 |
| Réversibilité prévue au contrat (export des données en fin de contrat) | 100 |

**D. Informations complémentaires recueillies par la direction technique**

1. L'offre de l'éditeur suppose que l'équipe interne passe à 25 personnes dès janvier 2027. M. QUÉLAVEC : « Tant que des bornes restent sur CIRCÉA, il faut l'exploiter, la corriger et la sécuriser. Nous garderons au moins 45 personnes jusqu'à la fin de 2027, et l'hébergement de CIRCÉA continuera de courir toute l'année. »
2. La solution reconnaît les bornes de deux des quatre constructeurs du réseau. Pour les deux autres, l'éditeur propose d'adapter ses interfaces, hors offre, pour 500 k€ par constructeur.
3. La solution propose des tarifs par tranche horaire ; les tarifs selon l'affluence sont annoncés par l'éditeur pour 2029. Pendant la migration, aucune évolution de CIRCÉA ne sera engagée.
4. Les évolutions de la solution sont décidées par l'éditeur pour l'ensemble de ses clients ; une demande propre à AMPÉRANE est facturée et réalisée selon ses priorités. L'intégration d'un nouveau modèle de borne demande six à neuf mois.
5. Le contrat dure cinq ans ; le prix de l'abonnement est révisable chaque année. En fin de contrat, les données sont exportées dans le format de l'éditeur.
6. Plusieurs développeurs de CIRCÉA, qui connaissent les défauts des micrologiciels de chaque constructeur, ont fait savoir qu'ils ne resteraient pas pour piloter un éditeur.
7. Après 2030, l'abonnement continue de suivre le nombre de points de recharge.

### ANNEXE 1.4 – Le pilotage actuel du système d'information (note de M. Olivier MANTRELLE, directeur administratif et financier, février 2027)

**A. Le tableau mensuel remis au comité de direction (extrait de décembre 2026)**

| Indicateur | Décembre 2026 | Année 2026 |
|---|---|---|
| Disponibilité moyenne du réseau | 97 % | 97 % |
| Dépenses du système d'information (hors rémunérations) | 1 200 k€ | 14 000 k€ |

**B. Les constats**

1. Le comité de direction réunit chaque mois la présidente et les cinq responsables de direction et de service. Il ne parle du système d'information qu'après un incident.
2. Aucune instance n'arbitre entre les demandes du développement du réseau (accès en ligne des sites hôtes, rapports adaptés), de l'exploitation (outils du centre de supervision, base de connaissances des interventions) et de la direction technique (montée en charge de CIRCÉA, sécurité, documentation). Chacun s'adresse directement aux développeurs qu'il connaît ; le directeur technique tranche seul, selon l'urgence.
3. Le comité de surveillance se réunit quatre fois par an. Il ne reçoit aucune information sur le système d'information. En janvier 2027, M. TREVÉLOC a demandé que le choix de la plateforme lui soit soumis pour avis.
4. Les deux fonds adressent chaque année à AMPÉRANE un questionnaire sur ses indicateurs environnementaux, sociaux et de gouvernance (ESG). Sa partie « système d'information » a été remplie à la main, en trois semaines, à partir de tableurs :

| Question du questionnaire des fonds | Réponse pour 2026 | Comment la réponse a été obtenue |
|---|---|---|
| Consommation d'électricité de l'hébergement | non fournie | l'hébergeur ne la communique pas ; seule la facture est connue |
| Consommation d'électricité des bornes en veille | estimation | fiches techniques des constructeurs multipliées par le nombre de points ; aucune mesure, alors que chaque borne mesure l'énergie qu'elle consomme |
| Durée de vie des équipements (bornes, terminaux de paiement, ordinateurs) | 10 ans pour les bornes | durée annoncée par les constructeurs ; aucun inventaire daté des équipements |
| Incidents de sécurité | 3 | incidents dont la direction technique se souvenait ; aucun registre |
| Demandes des personnes sur leurs données | environ 200 | courriels comptés dans la boîte du service clients ; les demandes reçues par l'application ne sont pas comptées |
| Accessibilité de l'application | non renseigné | aucune évaluation |
| Part de femmes dans les équipes techniques | 18 % | logiciel de paie |

En retour, les fonds ont jugé plusieurs réponses « non vérifiables » et demandé qu'elles soient fiabilisées avant 2028.

**C. La demande de la présidente**

« Je veux un tableau de bord du système d'information que je puisse présenter au comité de surveillance et qui nous serve aussi à répondre aux fonds. »

### ANNEXE 1.5 – Les savoirs des interventions (note de Mme Sandrine FOLCARIAS, directrice de l'exploitation et de la maintenance, février 2027)

**A. Les constats**

- En 2026, 30 000 interventions ont eu lieu sur site : 55 % par nos 90 techniciens itinérants, 45 % par les sept entreprises de maintenance.
- La panne est résolue dès la première intervention dans 80 % des cas pour nos techniciens et dans 60 % des cas pour les entreprises de maintenance. Près de 9 000 interventions ont dû être suivies d'un second déplacement, avec en moyenne trois jours de panne supplémentaires pour le point concerné.
- Le savoir-faire est concentré chez une douzaine de techniciens expérimentés, que les autres appellent jusqu'à vingt fois par jour.
- D'ici 2030, nous recruterons 60 techniciens ; les entreprises de maintenance recrutent aussi.

**B. Où se trouvent les savoirs aujourd'hui**

- Les notices des quatre constructeurs sont des fichiers épars sur un espace partagé, en plusieurs versions ; deux constructeurs en réservent l'usage aux techniciens qu'ils ont habilités.
- Les astuces s'échangent dans une messagerie de groupe, sur les téléphones personnels des techniciens : environ 1 500 messages par mois, introuvables quelques jours plus tard. Quelques techniciens des entreprises de maintenance y ont été invités, sans règle.
- Les diagnostics à distance du centre de supervision ne sont pas conservés : l'opérateur résume en une ligne, dans la demande d'intervention, ce qu'il a constaté. CIRCÉA conserve en revanche les codes d'erreur des bornes et la version du micrologiciel de chacune.
- À la clôture d'une intervention, le compte rendu est un texte libre, vide une fois sur deux.

**C. Les deux options envisagées** (coûts à comparer sur les quatre années 2027 à 2030)

| | Option 1 – Wiki autonome | Option 2 – Base de connaissances intégrée au logiciel de gestion des interventions |
|---|---|---|
| Principe | wiki en ligne, ouvert aux techniciens internes et à ceux des entreprises de maintenance ; pages rédigées librement ; recherche par mots | module proposé par l'éditeur du logiciel de gestion des interventions, relié aux diagnostics de CIRCÉA : à l'ouverture de l'intervention, le code d'erreur de la borne fait apparaître, dans l'application mobile du technicien, les fiches du modèle de borne concerné ; à la clôture, le technicien choisit la cause et la solution dans des listes, ajoute une photo ou dicte un commentaire |
| Accès | un compte par technicien, mêmes droits pour tous | droits définis par profil, par entreprise et par constructeur |
| Coût | 20 k€ de mise en place, puis 30 k€ par an dès la première année | 150 k€ la première année, puis 60 k€ par an |
| Délai | deux mois | six mois, dont trois mois de travail de l'équipe de CIRCÉA pour relier la plateforme au logiciel de gestion des interventions |

**D. Les réserves exprimées**

**Le dirigeant de l'une des sept entreprises de maintenance** : « Nous formons nos techniciens à nos frais ; nos méthodes, c'est ce qui nous fait gagner vos contrats. Si nous les versons dans votre base, vous les donnerez à nos concurrents, ou vous ferez le travail vous-mêmes. »

**Un technicien itinérant d'AMPÉRANE** : « Sur un parking, sous la pluie, avec un client qui attend, je n'ai pas le temps d'écrire. Le soir, je n'en ai pas envie. »

**Un technicien expérimenté d'AMPÉRANE** : « Je veux bien donner mes astuces. Mais si elles sont fausses six mois plus tard, après une mise à jour du micrologiciel, qui les corrigera ? »

### Travail à faire

« AMPÉRANE 2030 » prévoit de multiplier le réseau par deux et demi en quatre ans, avec une disponibilité d'au moins 98 % par point, alors que l'un des fonds conteste l'intérêt de garder une plateforme développée en interne et que les deux fonds demandent un système d'information sûr, documenté et piloté. Mme SORBADIÈRE vous demande de situer CIRCÉA dans la création de valeur et d'en déduire les orientations de la stratégie du système d'information, d'éclairer le choix de la plateforme par son coût complet et son enjeu, de proposer la gouvernance et le tableau de bord du système d'information, et de choisir et gouverner la base de connaissances des interventions. Vous mobiliserez pour cela les annexes 1.1 à 1.5 ainsi que vos connaissances professionnelles.

**1.1 – CIRCÉA dans la chaîne de valeur et la stratégie du système d'information (4 points)**

a) Après avoir présenté la chaîne de valeur et le rôle qu'y joue le système d'information, situez CIRCÉA dans les activités principales et de soutien d'AMPÉRANE, puis montrez, à partir de l'annexe 1.2, en quoi elle est, ou n'est pas, une source d'avantage concurrentiel au regard d'« AMPÉRANE 2030 ».

b) Après avoir défini la stratégie du système d'information, déduisez de votre analyse trois orientations de la stratégie du système d'information, chacune justifiée par un objectif du plan. Il n'est demandé ni schéma directeur, ni feuille de route.

**1.2 – Le coût complet des deux options pour la plateforme (3 points)**

a) Après avoir défini le coût complet d'un système d'information (coût total de possession), comparez de tête le coût des deux options de l'annexe 1.3 sur les années 2027 à 2030, puis relevez trois coûts cachés que les tableaux ne font pas apparaître, en les chiffrant quand l'annexe le permet, et indiquez l'écart entre les deux options qui en résulte.

b) Recommandez l'une des deux options à Mme SORBADIÈRE en croisant le coût et l'enjeu stratégique, et répondez à l'argument de M. TREVÉLOC. Aucun autre calcul n'est attendu.

**1.3 – La gouvernance et le tableau de bord du système d'information (3,5 points)**

a) Après avoir défini la gouvernance du système d'information, proposez celle qui répond aux constats de l'annexe 1.4 : l'instance d'arbitrage (composition, fréquence, décisions), l'information du comité de surveillance, le rôle de la présidente, des directions et des fonds.

b) Après avoir relevé les limites du tableau mensuel actuel, construisez le tableau de bord du système d'information destiné au comité de direction et au comité de surveillance : quatre indicateurs, dont deux au moins portent sur des dimensions ESG tirées du questionnaire des fonds, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Indiquez ensuite trois mesures pour fiabiliser les réponses au questionnaire. Aucune analyse d'un cadre de publication d'informations de durabilité n'est attendue.

**1.4 – La base de connaissances des interventions (3,5 points)**

a) Après avoir défini l'architecture fonctionnelle d'un système de gestion des connaissances, comparez les deux options de l'annexe 1.5 C selon trois critères que vous expliciterez, puis recommandez l'une d'elles. Décrivez ensuite le parcours d'un technicien d'une entreprise de maintenance devant une borne en panne, en montrant les fonctions du dispositif qu'il mobilise.

b) Proposez la gouvernance du dispositif : les rôles (propriétaire, référents par constructeur, contributeurs), trois règles, dont l'une répond à la crainte des entreprises de maintenance, et un indicateur de suivi, précisé par sa formule, sa source, sa fréquence, sa cible et son axe. La gestion des compétences n'est pas à traiter.
