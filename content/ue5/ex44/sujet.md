# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 44

**DOSSIER 2 – ORGANISER, EXPLOITER ET VALORISER LES DONNÉES DE RECHARGE (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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
