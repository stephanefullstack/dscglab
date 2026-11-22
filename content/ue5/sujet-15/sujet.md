# DSCG UE 5 — Management des systèmes d'information — Sujet d'entraînement complet n° 15

Durée de l'épreuve : 3 heures – Coefficient : 1

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026.

**Document et matériel autorisés** : Aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Le sujet se présente sous la forme de 3 dossiers indépendants :

| Dossier | Intitulé | Points | Durée conseillée |
|---|---|---:|---|
| DOSSIER 1 | PRÉPARER LES CHOIX STRATÉGIQUES ET LE PILOTAGE DU SYSTÈME D'INFORMATION | 14 points | 1 h 03 |
| DOSSIER 2 | ORGANISER, EXPLOITER ET VALORISER LES DONNÉES DE RECHARGE | 13 points | 59 min |
| DOSSIER 3 | SÉCURISER LA PLATEFORME ET LES BORNES, AUDITER LA TARIFICATION VARIABLE ET RENDRE LE RÉSEAU PLUS RESPONSABLE | 13 points | 58 min |

Le sujet comporte 15 annexes, dont 1 communes aux dossiers.

| Dossier | Annexe | Intitulé |
|---|---|---|
| Tous les dossiers | Annexe 1.1 | Présentation d'AMPÉRANE et chiffres clés |
| DOSSIER 1 | Annexe 1.2 | CIRCÉA dans l'activité d'AMPÉRANE (note de M. Yann QUÉLAVEC, directeur technique, et témoignages recueillis en février 2027) |
|  | Annexe 1.3 | Les deux options pour la plateforme (note de la direction technique et offre d'un éditeur, février 2027) |
|  | Annexe 1.4 | Le pilotage actuel du système d'information (note de M. Olivier MANTRELLE, directeur administratif et financier, février 2027) |
|  | Annexe 1.5 | Les savoirs des interventions (note de Mme Sandrine FOLCARIAS, directrice de l'exploitation et de la maintenance, février 2027) |
| DOSSIER 2 | Annexe 2.1 | Les règles de gestion du réseau et des sessions, et le modèle actuel (note de M. Gaël OLMAREC, responsable des données, février 2027) |
|  | Annexe 2.2 | Les échanges de données avec les plateformes d'itinérance, le logiciel des interventions et les sites hôtes (constats de M. Yann QUÉLAVEC, directeur technique, février 2027) |
|  | Annexe 2.3 | L'utilisation et la disponibilité des points (tableaux et note de l'équipe données, février 2027) |
|  | Annexe 2.4 | Les propositions de valorisation des données et la question de l'hébergement (note de Mme Hélène SORBADIÈRE, présidente, et courriers reçus, février 2027) |
|  | Annexe 2.5 | Repères (au 31/12/2026) |
| DOSSIER 3 | Annexe 3.1 | Les incidents de 2026 et l'outil de détection des anomalies (relevé du centre de supervision, établi par Mme Sandrine FOLCARIAS, directrice de l'exploitation et de la maintenance, février 2027) |
|  | Annexe 3.2 | Les constats sur la sécurité de CIRCÉA et des bornes (note du cabinet de conseil mandaté par les fonds, janvier 2027) |
|  | Annexe 3.3 | Le pilote de la tarification variable (note de Mme Hélène SORBADIÈRE, présidente, février 2027, et réclamations reçues) |
|  | Annexe 3.4 | Une recharge plus responsable (constats de Mme Sandrine FOLCARIAS, directrice de l'exploitation et de la maintenance, et de M. Romain TÉVENARD, responsable du service clients, février 2027) |
|  | Annexe 3.5 | Repères (au 31/12/2026) |

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

---

## DOSSIER 1 – PRÉPARER LES CHOIX STRATÉGIQUES ET LE PILOTAGE DU SYSTÈME D'INFORMATION (14 points)

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

---

## DOSSIER 2 – ORGANISER, EXPLOITER ET VALORISER LES DONNÉES DE RECHARGE (13 points)

### ANNEXE 2.1 – Les règles de gestion du réseau et des sessions, et le modèle actuel (note de M. Gaël OLMAREC, responsable des données, février 2027)

**A. Les règles de gestion**

L'équipe données a écrit, avec le centre de supervision et le service clients, les règles de gestion que la nouvelle base des sessions de CIRCÉA devra respecter :

- **RG1** – Un site hôte est identifié par un numéro attribué par AMPÉRANE ; on connaît son nom, son adresse, sa commune, son type (parking de supermarché, hôtel ou restaurant, aire de services, parking de collectivité ou d'entreprise) et le code de son propriétaire. Un site appartient à un seul propriétaire ; la liste des propriétaires, tenue dans le progiciel de gestion intégré, n'est pas à modéliser. Un site porte une ou plusieurs bornes.
- **RG2** – Une borne est identifiée par son numéro de série ; on connaît la référence de son modèle, son constructeur et sa date de mise en service. Elle est installée sur un seul site. La liste des modèles et des constructeurs, tenue par la direction technique, n'est pas à modéliser.
- **RG3** – Une borne porte d'un à quatre points de recharge ; un point appartient à une seule borne. Un point est identifié par un identifiant unique attribué par AMPÉRANE ; on connaît sa catégorie (normal ou rapide) et sa puissance maximale en kilowatts.
- **RG4** – Un point a un ou deux connecteurs ; un connecteur appartient à un seul point. Un connecteur est identifié par un numéro ; on connaît son type (la liste des types de connecteurs n'est pas à modéliser).
- **RG5** – Une session de recharge est identifiée par un numéro ; on connaît la date et l'heure de son début, sa durée en minutes et l'énergie délivrée en kilowattheures. Elle se déroule sur un seul connecteur ; un connecteur peut n'avoir encore servi à aucune session.
- **RG6** – Le conducteur d'une session est reconnu par un seul moyen de paiement, dont on enregistre le type (compte de l'application, badge d'un opérateur de mobilité ou carte bancaire) et la référence : numéro du compte, numéro du badge, ou jeton remis par la banque, jamais le numéro de la carte. Une session payée avec le badge d'un opérateur de mobilité est rattachée à cet opérateur ; les autres ne sont rattachées à aucun opérateur.
- **RG7** – Un opérateur de mobilité est identifié par un code ; on connaît sa raison sociale et la plateforme d'itinérance par laquelle il est relié à AMPÉRANE. Un opérateur nouvellement relié peut n'avoir encore apporté aucune session.
- **RG8** – Un tarif s'applique à un seul point, pour une tranche horaire ; on connaît l'heure de début et l'heure de fin de la tranche, le prix par kilowattheure, le prix par minute de branchement et les dates de début et de fin de validité du tarif. Un point porte un tarif par tranche horaire, et chaque changement de prix crée un nouveau tarif : les tarifs passés sont conservés. Un point qui n'est pas encore ouvert à la vente peut n'avoir aucun tarif.
- **RG9** – Une session est facturée selon un seul tarif : celui qui s'appliquait, au début de la session, au point dont relève le connecteur. Un tarif peut n'avoir servi à aucune session.
- **RG10** – Les factures, les reversements aux sites hôtes et les interventions de maintenance ne sont pas concernés par ces règles.

**B. Extrait du modèle logique actuel de la base des sessions de CIRCÉA**

Clé primaire en gras ; # : clé étrangère.

- SITE (**num_site**, nom_site, commune, type_site, proprietaire)
- BORNE (**num_borne**, num_serie, modele, constructeur, puissance_kw, type_connecteur_1, type_connecteur_2, #num_site)
- TARIF (**#num_borne**, prix_kwh_jour, prix_kwh_nuit)
- SESSION (**num_session**, date_heure_debut, duree_min, energie_kwh, moyen_paiement, tarif, #num_borne)

Précisions de M. OLMAREC :

- « Une borne qui porte plusieurs points est enregistrée autant de fois qu'elle a de points : la borne 1234, qui a quatre points, devient les "bornes" 1234-A, 1234-B, 1234-C et 1234-D, avec le même numéro de série. »
- « Le champ "tarif" de la session est un texte, recopié au démarrage de la session depuis l'écran des tarifs, ou saisi par l'équipe qui ouvre un nouveau site. »
- « Quand un prix change, la ligne de la borne est mise à jour dans TARIF : l'ancien prix est remplacé. »
- « Le champ "moyen_paiement" vaut "application", "carte" ou "itinérance". »

**C. Les constats de 2026**

- CIRCÉA compte 8 000 « bornes » pour environ 3 600 bornes physiques. Le logiciel de gestion des interventions, qui suit les bornes physiques par leur numéro de série, ne peut être rapproché de CIRCÉA qu'au moyen d'une table de correspondance tenue à la main (annexe 2.2).
- Le champ « tarif » des sessions de 2026 contient environ 60 libellés différents (« 0,45 €/kWh jour », « jour 0.45 », « tarif nuit »…) ; il est vide pour environ 3 % des sessions. On ne sait pas analyser les sessions selon leur tarif.
- Depuis le quatrième trimestre 2026, les prix des 600 points du pilote de la tarification variable changent jusqu'à six fois par jour. La table TARIF ne garde que le dernier prix de chaque « borne », en deux tranches (jour et nuit) : personne ne peut dire quel tarif s'appliquait à un point un jour donné.
- Les 1,6 million de sessions payées par l'itinérance portent la seule mention « itinérance » : pour savoir combien de sessions apporte chacun des quelque 200 opérateurs de mobilité, l'équipe données rapproche chaque mois, à la main, les relevés des deux plateformes d'itinérance.
- La session ne dit pas sur quel connecteur elle s'est déroulée : les pannes d'un connecteur ne peuvent pas être reliées aux sessions qui ont échoué.

### ANNEXE 2.2 – Les échanges de données avec les plateformes d'itinérance, le logiciel des interventions et les sites hôtes (constats de M. Yann QUÉLAVEC, directeur technique, février 2027)

**A. Les échanges en 2026**

| Échange | Émetteur et destinataires | Forme actuelle | Constat |
|---|---|---|---|
| Statuts des points (disponible, occupé, hors service) | CIRCÉA → deux plateformes d'itinérance → applications des opérateurs de mobilité | envoi groupé toutes les quinze minutes ; CIRCÉA distingue neuf états, la plateforme A en reconnaît quatre, la plateforme B trois, chacune avec ses propres libellés ; l'état « en maintenance » est transmis comme « hors service » à la plateforme A et comme « disponible » à la plateforme B | lors d'un contrôle de l'équipe données en janvier 2027, environ un statut affiché sur dix était périmé ou faux au moment où le conducteur le consultait |
| Tarifs | CIRCÉA → deux plateformes → opérateurs de mobilité | un fichier par semaine, avec un seul prix par point ; ni les tranches horaires ni les changements de prix en cours de semaine ne sont transmis | le prix affiché par l'application de l'opérateur de mobilité diffère du tarif que lui facture AMPÉRANE pour environ une session d'itinérance sur quatre sur les points du pilote de la tarification variable, et pour une sur cinquante ailleurs ; environ un tiers des réclamations reçues par le service clients sur l'itinérance portent sur le prix |
| Identifiants des points | CIRCÉA, logiciel de gestion des interventions, plateformes | CIRCÉA désigne le point par le numéro de sa « borne » (1234-A) ; le logiciel des interventions, par le numéro de série de la borne physique et la position du point (« gauche », « droite ») ; chaque plateforme, par un identifiant qu'elle compose elle-même ; deux personnes tiennent à la main une table de correspondance dans un tableur | environ 5 % des points sont mal rapprochés ; environ une demande d'intervention sur vingt-cinq désigne un mauvais point |
| Interventions | centre de supervision → logiciel des interventions | le centre de supervision crée la demande d'intervention à la main ; la clôture de l'intervention n'est pas transmise à CIRCÉA | un point réparé reste déclaré « hors service » jusqu'à ce qu'un opérateur du centre de supervision le remette en service à la main, en moyenne une demi-journée plus tard |
| Rapports aux sites hôtes | CIRCÉA → 1 200 sites hôtes | un tableur mensuel par site (sessions, énergie, recettes), envoyé par courriel vers le 10 du mois suivant ; ses colonnes varient selon la personne qui le prépare | une enseigne de supermarchés, propriétaire de 300 de nos sites, demande les données de chaque jour, dans un format ouvert, pour les intégrer à son propre outil de pilotage |

**B. Des mots qui n'ont pas le même sens**

Il n'existe aucun dictionnaire des données commun à CIRCÉA, au logiciel des interventions, au service clients et aux plateformes d'itinérance. Trois exemples :

- « session » : pour CIRCÉA, tout branchement d'un véhicule, même de quelques secondes ; pour les plateformes, une session facturée à un opérateur de mobilité ;
- « disponible » : pour CIRCÉA, la borne répond à ses messages ; pour le conducteur, il peut y recharger son véhicule ;
- « point » : pour CIRCÉA, une « borne » ; pour le logiciel des interventions, une position sur une borne physique.

**C. Le courriel d'un opérateur de mobilité** (directeur d'un opérateur qui apporte environ 8 % des sessions d'itinérance d'AMPÉRANE, janvier 2027)

« Nos clients voient vos points "disponibles" et les trouvent en panne, ou paient un prix que notre application ne leur avait pas annoncé. C'est à nous qu'ils s'en prennent. Si rien ne change d'ici l'été, votre réseau ne sera plus mis en avant dans notre application. »

### ANNEXE 2.3 – L'utilisation et la disponibilité des points (tableaux et note de l'équipe données, février 2027)

**A. Les indicateurs par type de site, 2025 et 2026**

Toutes les valeurs sont arrondies. Sessions par point et par jour : sessions de l'année / (nombre moyen de points ouverts pendant l'année × 365). Taux d'occupation : part du temps pendant laquelle un véhicule est branché au point. Disponibilité : part du temps pendant laquelle le point est en état de fonctionner, selon CIRCÉA.

| Indicateur | Supermarchés 2025 | Supermarchés 2026 | Hôtels et restaurants 2025 | Hôtels et restaurants 2026 | Aires de services 2025 | Aires de services 2026 | Collectivités et entreprises 2025 | Collectivités et entreprises 2026 | Ensemble 2025 | Ensemble 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| Points de recharge en fin d'année | 3 500 | 4 200 | 900 | 1 000 | 1 200 | 1 200 | 1 500 | 1 600 | 7 100 | 8 000 |
| dont points rapides | 900 | 1 200 | 100 | 100 | 1 000 | 1 000 | 100 | 100 | 2 100 | 2 400 |
| Sessions par point et par jour | 1,5 | 1,4 | 1,0 | 1,0 | 2,7 | 2,8 | 0,9 | 0,9 | 1,5 | 1,5 |
| Taux d'occupation | 6 % | 5 % | 24 % | 24 % | 6 % | 6 % | 19 % | 20 % | 11 % | 11 % |
| Part des sessions échouées | 4 % | 4 % | 3 % | 3 % | 7 % | 9 % | 3 % | 3 % | 5 % | 5 % |
| Disponibilité mesurée par CIRCÉA | 96 % | 97 % | 96 % | 97 % | 97 % | 98 % | 95 % | 96 % | 96 % | 97 % |
| Part des signalements de panne reçus alors que CIRCÉA indiquait le point disponible | 25 % | 30 % | 20 % | 25 % | 40 % | 50 % | 20 % | 20 % | 30 % | 35 % |

**B. Les points en 2026, par puissance**

| Indicateur 2026 | Supermarchés | Hôtels et restaurants | Aires de services | Collectivités et entreprises | Ensemble |
|---|---|---|---|---|---|
| Sessions par point rapide et par jour | 3,0 | 1,6 | 3,2 | 1,4 | 3,0 |
| Sessions par point normal et par jour | 0,8 | 0,9 | 0,6 | 0,9 | 0,8 |
| Part des sessions de moins de deux minutes | 5 % | 3 % | 15 % | 2 % | 7 % |

**C. L'affirmation de la directrice du développement du réseau**

Mme Pauline ESCARDINE : « Les aires de services sont nos meilleurs sites : deux fois plus de sessions par point que les supermarchés, et la meilleure disponibilité du réseau. Je propose de leur réserver l'essentiel des ouvertures de 2027. »

**D. Les limites signalées par l'équipe données**

- 900 points ont été ouverts en cours d'année 2026, dont 700 dans des parkings de supermarchés (300 rapides et 400 normaux). Un point nouvellement ouvert met environ un an à atteindre l'utilisation des points plus anciens du même type.
- La disponibilité est calculée par CIRCÉA à partir de l'état que chaque borne lui déclare. Les heures de maintenance programmée sont retirées du temps de référence ; les bornes rapides en reçoivent environ deux fois plus que les bornes normales. Quand une borne perd sa liaison avec CIRCÉA, la plateforme conserve son dernier état connu jusqu'au retour de la liaison.
- Les sessions de moins de deux minutes sont comptées comme réussies ; il s'agit le plus souvent d'un démarrage interrompu, que le conducteur relance aussitôt.
- Les signalements de panne sont les appels reçus par le service clients. Ils sont enregistrés dans le logiciel de relation clients avec le numéro du site, rarement avec celui du point, et ne sont pas rapprochés des états enregistrés par CIRCÉA. Pour le tableau A, l'équipe données a rapproché à la main, en fin d'année, les appels qui précisaient le point des états enregistrés par CIRCÉA au même moment ; ce rapprochement n'est fait ni en continu ni pour tous les appels.
- La disponibilité est présentée chaque mois au comité de direction sous la forme d'un seul chiffre : la moyenne de l'ensemble des points.

**E. Le modèle de prévision des sites candidats**

Pour classer les 300 sites candidats proposés par la direction du développement du réseau, l'équipe données a construit un modèle d'apprentissage automatique qui prévoit, pour chaque site, le nombre de sessions par point et par jour qu'il atteindrait après un an d'exploitation.

- Variables : trafic routier à proximité ; nombre de véhicules électriques immatriculés dans la commune ; durée moyenne de stationnement sur le site ; nombre de commerces à moins de 500 mètres ; type de site ; puissance des points prévus.
- Données d'apprentissage : les sessions de 2024 à 2026 des sites exploités par AMPÉRANE.
- Vérification : sur 200 sites existants mis de côté, la prévision s'écarte de moins de 20 % de la réalité pour sept sites sur dix.
- Résultats : 60 sites classés en priorité 1 (plus de deux sessions par point et par jour prévues), 140 en priorité 2 et 100 en priorité 3. Parmi les 60 sites de priorité 1 figurent 45 aires de services ; les 300 candidats en comptent 50. Les candidats comprennent aussi 80 parkings de gares et de centres de loisirs, types de sites qu'AMPÉRANE n'exploite pas encore.
- M. OLMAREC : « Le modèle classe bien les sites qui ressemblent aux nôtres. Il ne dit pas pourquoi un site est classé premier. »

**F. Deux façons de restituer les données**

| | Tableaux préparés par l'équipe données | Outil décisionnel en libre-service |
|---|---|---|
| Principe | l'équipe données (huit personnes) prépare à la demande les tableaux des directions et les rapports mensuels des sites hôtes | outil en ligne relié aux données de CIRCÉA : chaque direction compose ses propres tableaux de bord ; un portail donne à chaque site hôte l'accès à ses chiffres |
| Situation ou conditions | 60 demandes en attente ; chaque direction retravaille ensuite les chiffres dans ses tableurs, avec ses propres définitions | abonnement de 60 k€ par an ; trois mois de mise en place par l'équipe données ; formation des utilisateurs |

M. OLMAREC : « Si chacun compose ses tableaux sans définitions communes, nous aurons dix disponibilités différentes. » Mme ESCARDINE : « Les sites hôtes veulent voir leurs chiffres quand ils le veulent, pas le 10 du mois suivant. »

### ANNEXE 2.4 – Les propositions de valorisation des données et la question de l'hébergement (note de Mme Hélène SORBADIÈRE, présidente, et courriers reçus, février 2027)

**A. Les données d'AMPÉRANE**

- Environ 12 millions de sessions enregistrées depuis 2019, avec, pour chacune, le point, la date, l'heure, la durée, l'énergie délivrée et le moyen de paiement.
- Les comptes des 120 000 utilisateurs actifs de l'application : nom, adresse électronique, modèle et immatriculation du véhicule, historique des sessions.
- Les numéros des badges des opérateurs de mobilité et les jetons des cartes bancaires.
- Les états et les codes d'erreur des bornes, relevés en continu par CIRCÉA. Les journaux détaillés de fonctionnement des bornes de deux des quatre constructeurs ne sont accessibles qu'à leurs propres services.
- Les contrats conclus avec les sites hôtes ne disent rien de l'usage des données produites sur leurs parkings.

Mme Solène VERLOISE, déléguée à la protection des données : « Les conducteurs ont été informés que leurs données servent à la facturation, au service clients et à l'amélioration du réseau. Rien d'autre. »

**B. Trois propositions**

- **(a)** La direction du développement du réseau propose de vendre aux supermarchés hôtes un rapport trimestriel de fréquentation : nombre de sessions, durée de recharge et heures d'arrivée des conducteurs, par jour de la semaine et par heure, comparés aux heures d'ouverture du magasin. L'enseigne propriétaire de 300 de nos sites (annexe 2.2) est intéressée ; elle demande en outre « la liste des conducteurs qui rechargent plus d'une heure, avec leur adresse électronique, pour leur adresser nos offres ».
- **(b)** Plusieurs collectivités souhaitent acheter des données de recharge agrégées par commune et par heure (sessions, énergie délivrée, taux d'occupation, part des sessions des conducteurs venus d'un autre département) pour planifier leurs propres équipements.
- **(c)** SELVAREN Automobiles, constructeur de véhicules électriques, propose d'acheter, pour chacun de ses véhicules identifié par son immatriculation, l'historique complet de ses recharges sur le réseau (lieux, heures, durées, énergie), afin d'étudier l'usure des batteries et de proposer des offres à leurs propriétaires ; elle propose une rémunération annuelle par véhicule.

**C. La demande des fonds**

M. Arnaud TREVÉLOC, représentant de VARNEDAL Infrastructures au comité de surveillance : « Douze millions de sessions, c'est un patrimoine que les investisseurs regarderont en 2028. Il faut le valoriser : vendons tout ce qui peut l'être. »

**D. L'appel à partenaires de LOIRAVEL Agglomération**

LOIRAVEL Agglomération cherche un partenaire pour équiper et exploiter 40 de ses parkings publics, soit environ 600 points de recharge, à partir de 2028 ; les réponses sont attendues avant le 30 juin 2027. Elle exige que « les données des sessions et des usagers de ses parkings soient hébergées par un prestataire soumis au seul droit de l'Union européenne ». Trois autres agglomérations préparent des appels semblables.

**E. Les deux options d'hébergement** (note de M. Yann QUÉLAVEC, directeur technique)

CIRCÉA, l'application des conducteurs, les outils d'analyse de l'équipe données et leurs données sont hébergés chez un fournisseur de cloud dont le siège est hors de l'Union européenne, dans une région de centres de données située en France (2 400 k€ en 2026, dont environ 1 100 k€ pour CIRCÉA). CIRCÉA utilise plusieurs services gérés propres à ce fournisseur : base de données, file de messages, outils d'analyse de l'équipe données.

| | Option 1 – Rester chez le fournisseur actuel, avec des protections renforcées | Option 2 – Migrer vers un hébergeur européen dont l'offre est qualifiée SecNumCloud |
|---|---|---|
| Principe | chiffrement de toutes les données, avec des clés gérées par AMPÉRANE dans un service du fournisseur ; avenant au contrat : localisation en France garantie, information d'AMPÉRANE de toute demande d'accès d'une autorité, engagement du fournisseur de contester ces demandes | migration de CIRCÉA, de l'application des conducteurs et de toutes leurs données chez un hébergeur dont le siège est dans l'Union européenne et le capital détenu par des actionnaires européens |
| Coût | 150 k€ par an | migration : 1 200 k€ au total, répartis sur 2027 et 2028, dont l'adaptation de CIRCÉA aux services de l'hébergeur ; hébergement plus cher d'environ 15 %, soit 360 k€ par an au volume de 2026 |
| Délai | trois mois | douze mois ; deux outils d'analyse de l'équipe données n'ont pas d'équivalent chez l'hébergeur et doivent être remplacés |
| Autres éléments | le fournisseur reste soumis au droit du pays de son siège ; ses services gérés rendent tout changement de fournisseur long et coûteux | l'hébergeur s'engage à exporter les données dans des formats ouverts en fin de contrat ; son catalogue de services gérés est plus restreint ; il est dix fois plus petit que le fournisseur actuel |

### ANNEXE 2.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Une donnée à caractère personnel est toute information se rapportant à une personne physique identifiée ou identifiable, directement ou indirectement (nom, numéro d'identification, données de localisation…). Les données sont collectées pour des finalités déterminées, explicites et légitimes, et ne sont pas traitées ensuite d'une manière incompatible avec ces finalités ; elles sont adéquates et limitées à ce qui est nécessaire (minimisation). Les personnes sont informées des finalités du traitement et des destinataires de leurs données. Le responsable du traitement ne fait appel qu'à des sous-traitants qui présentent des garanties suffisantes, liés à lui par un contrat ; un hébergeur est en principe un sous-traitant. | Applicable depuis le 25/05/2018 |
| Règlement (UE) 2023/2854 sur les données (Data Act) | L'utilisateur d'un produit connecté peut accéder aux données que génère son utilisation. Les fournisseurs de services d'informatique en nuage doivent permettre à leurs clients de changer de fournisseur et d'emporter leurs données. | Applicable depuis le 12/09/2025 |
| SecNumCloud (ANSSI), version 3.2 | Référentiel d'exigences de l'ANSSI qui permet de qualifier des offres d'informatique en nuage : exigences de sécurité et critères de protection contre l'application de lois extra-européennes. | Version 3.2 en vigueur depuis le 08/03/2022 |
| Référentiel du cloud de confiance du Cigref | Trois piliers : la sécurité ; l'immunité aux lois extra-européennes ; la maîtrise de la dépendance. Toute exigence opérationnelle doit être également exigible par contrat. Ce n'est ni un label, ni une certification. | Première version publiée le 27/05/2021 ; deuxième version disponible |

Il n'est demandé aucune analyse juridique.

### Travail à faire

« AMPÉRANE 2030 » veut porter le réseau à 20 000 points, garantir à chaque point une disponibilité d'au moins 98 % et tirer de nouvelles recettes des données. Or les données de recharge sont mal structurées, circulent mal entre CIRCÉA, les plateformes d'itinérance, le logiciel des interventions et les sites hôtes, et une collectivité pose une condition d'hébergement. Mme SORBADIÈRE vous demande de préparer le modèle des données du réseau et des sessions, d'organiser les échanges de données, d'exploiter les données d'utilisation et de disponibilité pour décider, et d'éclairer la valorisation des données et le choix de l'hébergement. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.5 ainsi que vos connaissances professionnelles.

**2.1 – Le modèle des données du réseau, des sessions et des tarifs (3 points)**

a) Relevez trois défauts du modèle logique actuel (annexe 2.1 B) au regard des règles de gestion de l'annexe 2.1 A, en précisant pour chacun le constat de l'annexe 2.1 C qu'il explique.

b) Après avoir distingué le modèle conceptuel et le modèle logique des données, construisez le modèle conceptuel des données du réseau, des sessions et des tarifs (entités, identifiants, attributs, associations et cardinalités) à partir des règles de gestion de l'annexe 2.1 A, en montrant comment il conserve l'historique des tarifs. Déduisez-en le modèle logique, en énonçant les règles de passage utilisées. Aucune requête n'est attendue.

**2.2 – Les échanges de données avec les plateformes d'itinérance, le logiciel des interventions et les sites hôtes (2 points)**

a) Après avoir défini l'interopérabilité, analysez trois problèmes d'échange tirés de l'annexe 2.2 et leurs conséquences pour les conducteurs, les opérateurs de mobilité et les sites hôtes.

b) Proposez l'organisation cible des échanges en quatre mesures : l'identifiant unique du point ; des statuts et des tarifs normalisés ; les interfaces de programmation et les formats ouverts ; les règles de cohérence entre CIRCÉA, le logiciel des interventions et les plateformes, assorties d'un indicateur précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Le détail technique des échanges n'est pas attendu.

**2.3 – L'utilisation et la disponibilité des points (4 points)**

a) Après avoir présenté les étapes de la chaîne de traitement des données, décrivez celle qui produit l'indicateur de disponibilité présenté chaque mois au comité de direction, en montrant, à chaque étape, un biais tiré de l'annexe 2.3.

b) Formulez trois constats argumentés tirés de l'annexe 2.3 A et B, puis appréciez l'affirmation de Mme ESCARDINE (annexe 2.3 C). Aucun calcul statistique n'est attendu.

c) Après avoir distingué l'analyse descriptive et l'analyse prédictive, justifiez l'usage du modèle de prévision de l'annexe 2.3 E pour classer les sites candidats. Donnez-en ensuite deux limites, dont celle qui tient aux données d'apprentissage, et indiquez comment en tenir compte dans la décision.

d) Choisissez, à l'aide de deux critères que vous expliciterez, l'un des deux modes de restitution de l'annexe 2.3 F, puis proposez une représentation visuelle destinée aux sites hôtes, justifiée par son message.

**2.4 – La valeur des données et leur hébergement (4 points)**

a) Après avoir défini le patrimoine informationnel, montrez deux sources de valeur des données de recharge d'AMPÉRANE et deux risques qui menacent cette valeur.

b) Appréciez les trois propositions de l'annexe 2.4 B au regard des principes du RGPD et des repères de l'annexe 2.5, puis recommandez celles qu'AMPÉRANE peut retenir, et à quelles conditions. Répondez ensuite à M. TREVÉLOC. Aucune valorisation chiffrée des données et aucune analyse juridique ne sont attendues.

c) Comparez les deux options d'hébergement de l'annexe 2.4 E selon les trois piliers du référentiel du cloud de confiance, puis recommandez l'une d'elles en tenant compte de la demande de LOIRAVEL Agglomération.

---

## DOSSIER 3 – SÉCURISER LA PLATEFORME ET LES BORNES, AUDITER LA TARIFICATION VARIABLE ET RENDRE LE RÉSEAU PLUS RESPONSABLE (13 points)

### ANNEXE 3.1 – Les incidents de 2026 et l'outil de détection des anomalies (relevé du centre de supervision, établi par Mme Sandrine FOLCARIAS, directrice de l'exploitation et de la maintenance, février 2027)

**A. Les quatre incidents marquants de 2026**

Il n'existe pas de registre des incidents : ce relevé a été reconstitué à partir des notes du centre de supervision et du service clients. Chiffres ronds.

| Date | Ce qui s'est passé | Conséquences |
|---|---|---|
| Mai 2026 | L'un des quatre constructeurs adresse par courriel le fichier d'une nouvelle version du micrologiciel de son modèle de borne rapide. Le soir même, l'équipe de CIRCÉA l'installe à distance, en une seule fois, sur toutes les bornes de ce modèle. La nouvelle version bloque les 300 points concernés, qui restent hors service pendant deux jours, le temps que le constructeur fournisse une version corrigée. | environ 1 800 sessions perdues, soit environ 50 k€ de ventes ; 40 déplacements de techniciens pour remettre en service des bornes qui ne répondaient plus à distance |
| Septembre 2026 | Un conducteur signale un autocollant portant un faux code à scanner collé sur une borne. Le code renvoie vers un faux site de paiement qui imite celui d'AMPÉRANE. Les techniciens en retrouvent sur 30 bornes de huit aires de services. | environ 200 conducteurs signalent un débit frauduleux sur leur carte ; écho dans la presse régionale : « Recharge électrique : de faux codes pour vider votre compte » |
| Novembre 2026 | Le compte qu'une des sept entreprises de maintenance utilise dans CIRCÉA est employé, en pleine nuit, depuis un ordinateur de cette entreprise infecté par un logiciel malveillant, pour redémarrer à distance 40 bornes. Ce compte est partagé par ses douze techniciens et permet de commander toutes les bornes du réseau ; son mot de passe n'avait pas changé depuis 2022. La cause n'est comprise qu'au bout de deux jours. | environ 150 sessions interrompues ; aucune donnée ni aucun tarif modifiés, selon la direction technique, qui ne peut pas l'établir avec certitude |
| Décembre 2026 | Une panne chez le fournisseur de cloud rend CIRCÉA inaccessible pendant cinq heures, un samedi après-midi. Le centre de supervision ne voit plus aucune borne ; les sessions par l'application et par les opérateurs de mobilité ne peuvent plus démarrer ; seules les bornes rapides acceptent encore la carte bancaire. Aucune procédure de fonctionnement dégradé n'était prévue. | environ 2 500 sessions n'ont pas pu démarrer ; 600 appels au service clients en cinq heures |

**B. L'essai de l'outil de détection des anomalies (octobre à décembre 2026)**

- L'équipe données de la direction technique a développé un outil d'apprentissage automatique qui repère les comportements inhabituels des bornes. Il a appris, à partir des journaux de communication entre les bornes et CIRCÉA et des sessions de juin à septembre 2026, ce qu'est un fonctionnement « normal » ; il signale ensuite au centre de supervision tout écart à ce fonctionnement.
- Les journaux détaillés des bornes de deux des quatre constructeurs ne sont accessibles qu'à leurs propres services : pour ces bornes, l'outil ne dispose que des états et des codes d'erreur.
- En trois mois, l'outil a émis 1 800 alertes. Après examen, 270 correspondaient à une anomalie réelle (bornes sur le point de tomber en panne, connecteurs défectueux, redémarrages de novembre) ; les 1 530 autres étaient de fausses alertes, dont les trois quarts sur les bornes des deux constructeurs dont les journaux ne sont pas accessibles.
- Les redémarrages à distance de novembre ont été signalés par l'outil dix minutes après le premier d'entre eux ; l'alerte, perdue parmi les autres, n'a été lue que le lendemain matin.
- L'outil ne voit ni les autocollants collés sur les bornes ni l'état de l'hébergement.
- Pendant la dernière semaine, l'équipe données l'a autorisé à couper seul l'alimentation des bornes qu'il jugeait suspectes. Le samedi 19 décembre, il a coupé à tort les 12 points d'une aire de services pendant trois heures, un jour de départs en vacances : mise en service en septembre 2026, cette aire n'avait connu aucun jour de grands départs pendant la période d'apprentissage, et son affluence de ce jour-là avait été prise pour une anomalie.

**C. Les points de vue**

**M. Gaël OLMAREC, responsable des données** : « L'outil voit ce que personne ne voit. Le centre de supervision réagit trop lentement : laissons l'outil couper seul les bornes suspectes, sans attendre un opérateur. »

**Mme Sandrine FOLCARIAS** : « Mes opérateurs reçoivent près de vingt alertes par jour, dont plus de huit sur dix sont fausses. Ils ont cessé de les lire. Et je ne veux plus qu'une machine coupe une aire de services un samedi de départs. »

**D. Les échelles retenues pour l'évaluation des risques**

| Niveau | Probabilité | Impact |
|---|---|---|
| 1 | rare : jamais survenu, peu plausible | gêne locale : quelques points, quelques heures |
| 2 | possible : plausible, ou déjà survenu une fois pour une cause extérieure à AMPÉRANE | plusieurs sites touchés, pertes limitées |
| 3 | probable : déjà survenu alors que la pratique qui l'a permis est toujours en place, ou facile à provoquer | des centaines de points ou de conducteurs touchés, écho public |
| 4 | fréquent : plusieurs fois par an | une grande partie du réseau arrêtée ou sous le contrôle d'un tiers, confiance durablement atteinte |

La criticité d'un risque est le produit de sa probabilité par son impact (de 1 à 16).

### ANNEXE 3.2 – Les constats sur la sécurité de CIRCÉA et des bornes (note du cabinet de conseil mandaté par les fonds, janvier 2027)

**A. Les constats**

| Domaine | Constat |
|---|---|
| Politique de sécurité | AMPÉRANE n'a pas de politique de sécurité écrite. Une charte informatique de 2020, signée par les salariés, fixe les règles d'usage des postes et de la messagerie ; elle ne s'applique pas aux techniciens des entreprises de maintenance. Aucune analyse des risques n'a jamais été conduite. |
| Organisation | Il n'existe pas de responsable de la sécurité. M. Yann QUÉLAVEC, directeur technique, « s'en charge », alors que sa direction développe, met en production et exploite CIRCÉA. Ni la présidente ni le comité de surveillance n'ont jamais reçu de compte rendu sur la sécurité. |
| Développement de CIRCÉA | Les développeurs mettent en production environ deux nouvelles versions par semaine, sans revue de sécurité. CIRCÉA utilise environ 400 composants logiciels libres, qui ne sont pas inventoriés : quand une faille est rendue publique dans un composant, personne ne sait si CIRCÉA l'utilise. |
| Micrologiciels des bornes | Les nouvelles versions sont reçues des constructeurs par courriel ou téléchargées sur leur site, puis installées sans essai préalable, sans vérification de leur origine et en une seule fois sur tout un modèle ; aucun retour à la version précédente n'est prévu. Les contrats d'achat des bornes ne disent rien de la durée pendant laquelle les constructeurs fourniront des correctifs de sécurité. |
| Comptes des entreprises de maintenance | Chacune des sept entreprises dispose dans CIRCÉA d'un compte unique, partagé par tous ses techniciens (environ 120 personnes au total), qui permet de commander toutes les bornes du réseau. Les mots de passe ne sont jamais changés ; aucune revue des comptes n'a eu lieu. |
| Supervision | Le centre de supervision suit l'état de fonctionnement des bornes jour et nuit, mais pas les événements de sécurité (connexions, commandes à distance, modifications de tarifs). Les journaux de CIRCÉA sont conservés sept jours. |
| Sauvegardes | La base de CIRCÉA est sauvegardée chaque nuit, dans la même région de centres de données que la plateforme. Aucune sauvegarde n'a jamais été restaurée pour essai. |

**B. La position des fonds**

« Avant la levée de fonds de 2028, nous attendons une politique de sécurité de CIRCÉA et des bornes, validée par la présidente et présentée au comité de surveillance, et des premières mesures engagées en 2027. »

**C. Les trois options envisagées pour la fonction sécurité**

| Option | Description | Avis exprimés |
|---|---|---|
| 1 | recruter un responsable de la sécurité des systèmes d'information (RSSI) rattaché au directeur technique | M. QUÉLAVEC : « Il doit être au plus près des développeurs. » |
| 2 | recruter un RSSI rattaché à la présidente | les fonds y sont favorables ; recrutement estimé à six mois |
| 3 | faire appel à un RSSI à temps partagé, fourni par un cabinet spécialisé, deux jours par semaine | disponible dès avril 2027 ; le cabinet le partage entre plusieurs clients |

### ANNEXE 3.3 – Le pilote de la tarification variable (note de Mme Hélène SORBADIÈRE, présidente, février 2027, et réclamations reçues)

**A. Le pilote**

- Depuis octobre 2026, 600 points de 150 sites pratiquent une tarification variable. Un programme écrit par l'équipe données recalcule toutes les quinze minutes le prix du kilowattheure de chaque point, selon l'heure et l'occupation du site ; le prix d'un point change jusqu'à six fois par jour.
- Le prix est affiché dans l'application d'AMPÉRANE et sur l'écran des bornes rapides au début de la session ; AMPÉRANE s'est engagée à facturer la session à ce prix.
- Parmi les 150 sites du pilote figurent 60 sites de communes rurales (parkings de supermarchés et de collectivités) qui n'ont qu'une borne rapide de deux points, la plus proche borne d'un autre opérateur étant à plus de 20 km.
- « AMPÉRANE 2030 » prévoit de généraliser la tarification variable à tout le réseau en septembre 2027.

**B. Les constats d'octobre 2026 à février 2027**

| Constat | Chiffres ronds |
|---|---|
| Sessions du pilote | environ 125 000 sessions, dont environ 75 000 payées par l'application ou par carte bancaire |
| Sessions payées par l'application ou par carte bancaire facturées à un prix différent du prix affiché par AMPÉRANE au début de la session | environ 3 000 sessions, dont quatre sur cinq à un prix plus élevé ; écart moyen d'environ 2 € par session concernée |
| Documentation des règles de calcul | aucune : les prix plancher et plafond, le poids de l'occupation et les règles propres aux jours fériés ne sont écrits que dans le programme ; deux personnes de l'équipe données les connaissent |
| Modifications du programme | 15 modifications mises en production depuis octobre 2026 par l'équipe données elle-même, dont 10 sans aucune trace (ni demande, ni description, ni validation) ; les données d'occupation qui ont servi à calculer chaque prix ne sont pas conservées |
| Réclamations sur les prix | 900 réclamations sur les sessions du pilote, sur 2 000 réclamations sur les prix pour tout le réseau |
| Prix moyen du kilowattheure sur les bornes rapides du pilote | 0,65 € sur les 60 sites ruraux à borne unique ; 0,52 € sur les sites urbains |

**C. Deux réclamations**

**Un conducteur** : « L'application m'annonçait 0,49 € le kilowattheure quand j'ai branché ma voiture. J'ai été facturé 0,61 €. Personne au service clients n'a su m'expliquer pourquoi. »

**Le maire d'une commune rurale du pilote** : « Notre seule borne rapide est toujours occupée le samedi, donc toujours au prix fort. Les habitants n'ont pas d'autre choix : votre tarif "selon l'affluence" les pénalise parce qu'ils vivent à la campagne. »

**D. La demande de la présidente**

« Je ne généraliserai pas la tarification variable sans un audit du programme et de ses résultats. AMPÉRANE n'a pas d'audit interne : je confierai l'audit à un auditeur des systèmes d'information externe, qui y consacrera 20 jours en avril et en mai 2027, pour que je décide en juin. Préparez-en le cadrage. »

M. OLMAREC : « Le programme, c'est notre savoir-faire. L'auditeur peut juger les résultats, je lui fournirai les extractions dont il aura besoin. »

### ANNEXE 3.4 – Une recharge plus responsable (constats de Mme Sandrine FOLCARIAS, directrice de l'exploitation et de la maintenance, et de M. Romain TÉVENARD, responsable du service clients, février 2027)

**A. La recharge sans application**

- Les 5 600 points normaux n'acceptent pas la carte bancaire : on ne peut y recharger qu'avec l'application d'AMPÉRANE ou avec la carte ou l'application d'un opérateur de mobilité.
- La réservation d'un point et le tarif réduit de 20 % aux heures creuses sont réservés aux utilisateurs de l'application. Le prix variable n'est affiché que dans l'application et sur l'écran des bornes rapides.
- En 2026, le service clients a reçu environ 2 000 appels de conducteurs qui ne parvenaient pas à recharger sans l'application : conducteurs sans téléphone intelligent, téléphone trop ancien pour installer l'application, absence de réseau mobile sur le parking ; une bonne partie étaient des conducteurs âgés. Le service clients peut démarrer une session à distance, mais l'appel dure en moyenne huit minutes.
- 300 réclamations ont porté sur l'accessibilité de l'application : caractères trop petits et impossibles à agrandir, contrastes insuffisants, boutons trop proches les uns des autres, écrans illisibles par les lecteurs d'écran des personnes malvoyantes. L'application n'a jamais été évaluée au regard des règles d'accessibilité numérique.

**B. Les équipements du réseau**

- Les écrans des quelque 3 600 bornes (état de la borne et, sur les bornes rapides, prix) restent allumés jour et nuit, à pleine luminosité, y compris sur les sites fermés la nuit (environ la moitié des sites). Selon les constructeurs, l'écran représente environ la moitié de la consommation d'électricité d'une borne au repos.
- 1 200 bornes, installées en 2019, sont équipées de modems qui ne sont plus fabriqués et que l'opérateur de réseau mobile cessera de prendre en charge à la fin de 2028 ; les pannes de leurs cartes électroniques ont doublé depuis 2025. Leur structure, leurs câbles et leurs connecteurs sont en bon état.
- Deux options sont étudiées pour ces 1 200 bornes : remplacer chaque borne entière par un modèle récent de même puissance (environ 10 k€ par borne, pose comprise, douze mois de travaux sur les sites) ; ou remplacer seulement le modem et la carte électronique par un ensemble fourni par le constructeur (environ 2 k€ par borne, une demi-journée d'intervention), ce qui prolonge la durée de vie de la borne d'au moins cinq ans selon lui.
- Les 1 200 terminaux de paiement des bornes rapides sont remplacés par série tous les quatre ans par le prestataire de paiement, quel que soit leur état : 300 en 2026.
- En 2026, environ 4 000 équipements ont été déposés lors des interventions (cartes électroniques, modems, écrans, terminaux de paiement, connecteurs). Certains sont stockés dans les dépôts régionaux des techniciens, d'autres sont repris par les entreprises de maintenance ou jetés avec les déchets des chantiers. Aucun inventaire n'en est tenu ; AMPÉRANE ne sait pas lesquels ont été réparés, réemployés ou recyclés.
- Ces données ne permettent pas de calculer une empreinte environnementale, et aucun calcul n'est demandé.

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| ISO/IEC 27001:2022 | Norme d'exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques ; 93 mesures en annexe A (dont le contrôle d'accès, la sécurité du développement, la gestion des vulnérabilités, la journalisation, la sauvegarde et la sécurité des relations avec les fournisseurs). | En vigueur |
| ISO/IEC 27005:2022 | Lignes directrices de gestion des risques liés à la sécurité de l'information : identification, analyse, évaluation et traitement des risques. | En vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI, 2024) | Méthode française d'appréciation et de traitement des risques numériques en cinq ateliers (cadrage et socle de sécurité, sources de risque, scénarios stratégiques passant par l'écosystème, scénarios opérationnels, traitement), compatible avec ISO/IEC 27005. | Version 1.5 publiée en 2024 |
| Guide d'hygiène informatique (ANSSI, 2017) | Guide de 42 mesures de bonnes pratiques de sécurité (gestion des comptes et des accès, mises à jour, sauvegardes, journalisation…). | Version de 2017 |
| COBIT 2019 (ISACA) | Cadre de gouvernance et de management de l'information et des technologies : 40 objectifs de gouvernance et de management, dont la gestion des changements. | Version 2019 |
| Règlement (UE) 2024/2847 sur la cyberrésilience (CRA) | Exigences de cybersécurité pour les produits comportant des éléments numériques, à la charge de leurs fabricants : sécurité dès la conception, gestion des vulnérabilités, fourniture de mises à jour de sécurité. Les bornes connectées comportent des éléments numériques ; l'application du règlement à chaque modèle n'est pas à déterminer. | Signalement par les fabricants des vulnérabilités activement exploitées et des incidents graves depuis le 11/09/2026 ; application générale le 11/12/2027 |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | Approche par niveaux de risque. Les organisations qui utilisent un système d'IA veillent à ce que leur personnel ait un niveau suffisant de maîtrise de l'IA. Aucune classification de l'outil de détection de l'annexe 3.1 n'est demandée. | Maîtrise de l'IA depuis le 02/02/2025 ; application générale depuis le 02/08/2026 |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | Critères d'écoconception des services numériques publiés par l'Arcep et l'Arcom, avec l'ADEME, dont l'utilisation d'un service sur des équipements anciens. | Version 2 publiée en 2024 |

Il n'est demandé aucune analyse juridique.

### Travail à faire

En 2026, une mise à jour de micrologiciel, un compte d'entreprise de maintenance détourné, de faux codes à scanner et une panne de l'hébergement ont montré la fragilité de CIRCÉA et des bornes ; le pilote de la tarification variable suscite des écarts de prix et des réclamations ; une partie des conducteurs ne peut pas recharger sans l'application, et 1 200 bornes de 2019 doivent être renouvelées en tout ou en partie. Mme SORBADIÈRE vous demande d'analyser les risques et l'usage de l'outil de détection, de proposer la politique de sécurité de CIRCÉA et des bornes et son organisation, de cadrer l'audit de la tarification variable et de rendre le réseau plus responsable. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – Les risques de la flotte et de la plateforme, et l'outil de détection (3 points)**

a) En vous appuyant sur une méthode d'analyse des risques de l'annexe 3.5, dont vous justifierez le choix et préciserez la nature, identifiez quatre risques révélés par l'annexe 3.1 sur les bornes et sur CIRCÉA, évaluez la probabilité et l'impact de chacun selon les échelles de l'annexe 3.1 D, puis retenez-en deux prioritaires.

b) Après avoir caractérisé l'outil de détection des anomalies, situez-le dans le traitement des risques (prévenir, détecter, réagir) et montrez ses limites. Fixez ensuite trois règles de son emploi, dont l'une répond à la demande de M. OLMAREC, et assortissez l'une d'elles d'un indicateur précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Aucune classification de l'outil au titre du règlement sur l'intelligence artificielle n'est attendue.

**3.2 – La politique de sécurité de CIRCÉA et des bornes (4 points)**

a) Après avoir défini une politique de sécurité du système d'information fondée sur l'analyse des risques, proposez celle de CIRCÉA et des bornes : ses objectifs, son périmètre et ses règles dans quatre domaines, portant respectivement sur la sécurité du développement de CIRCÉA et l'inventaire de ses composants, sur les mises à jour des micrologiciels, sur les comptes des entreprises de maintenance, et sur la supervision et les sauvegardes. Aucun paramétrage ni aucun test technique de sécurité ne sont attendus.

b) Hiérarchisez quatre mesures à engager en 2027, en justifiant le rang de la première.

c) Choisissez, parmi les trois options de l'annexe 3.2 C, le positionnement de la fonction sécurité, puis répartissez les rôles entre la présidente, le comité de surveillance, le RSSI, la direction technique, le centre de supervision, les constructeurs, au regard du règlement sur la cyberrésilience en principe, et les entreprises de maintenance.

**3.3 – L'audit de la tarification variable (2,5 points)**

a) Cadrez l'audit du programme de tarification variable que conduira l'auditeur externe : ses objectifs, son périmètre, ses étapes et les preuves à demander. Proposez ensuite quatre critères de performance et de conformité de cet audit.

b) Indiquez deux facteurs de succès et deux points de vigilance propres à l'audit d'un programme qui calcule des prix, en les reliant à l'annexe 3.3. Aucune analyse juridique des prix n'est attendue.

**3.4 – Une recharge plus responsable (3,5 points)**

a) Après avoir défini une gouvernance du système d'information orientée vers la responsabilité sociétale, proposez deux principes et leur traduction concrète, l'un sur l'équité de la tarification variable, l'autre sur l'inclusion des conducteurs, en précisant qui les porte.

b) Proposez quatre bonnes pratiques de Green IT sur le cycle de vie des équipements du réseau, portant respectivement sur l'allongement de la durée de vie et la réparation, le choix entre les deux options pour les 1 200 bornes de 2019, la sobriété des écrans et la fin de vie des équipements déposés, puis classez-les par priorité. Aucun calcul d'empreinte n'est attendu.
