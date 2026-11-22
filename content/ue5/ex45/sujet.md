# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 45

**DOSSIER 3 – SÉCURISER LA PLATEFORME ET LES BORNES, AUDITER LA TARIFICATION VARIABLE ET RENDRE LE RÉSEAU PLUS RESPONSABLE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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
