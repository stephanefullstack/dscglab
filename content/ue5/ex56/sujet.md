# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 56

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES INSTALLATIONS, EN GARDER LA MAÎTRISE (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 19, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en juin 2027. ESTRAVENT Énergies SA est un producteur indépendant d'électricité renouvelable, fondé en 2004 à Reims par trois ingénieurs. Société anonyme à conseil d'administration, elle est cotée sur Euronext Growth depuis 2015 ; ses fondateurs en détiennent 34 % du capital, un fonds d'infrastructure 21 %, et 45 % sont détenus par le public. Elle développe, construit et exploite en France 64 parcs éoliens terrestres (420 éoliennes, 1 000 MW) et 38 centrales solaires au sol (400 MW), portés chacun par une société de projet qu'elle détient à 100 %. En 2026, ses installations ont produit 2,7 TWh, et son chiffre d'affaires a atteint 250 M€. ESTRAVENT emploie 520 salariés, au siège de Reims, au centre de conduite qui surveille les installations jour et nuit, et dans quatre agences régionales. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « ESTRAVENT 2031 », adopté en mars 2027 par le conseil d'administration, fixe quatre objectifs : porter la puissance installée à 2 500 MW, en renouvelant les éoliennes des parcs les plus anciens et en développant de nouveaux projets ; vendre 40 % de la production à des industriels par des contrats d'achat direct, contre 10 % en 2026, à mesure que les parcs sortent de leurs contrats de vente à prix garanti ; porter la disponibilité des éoliennes de 95 % à 97 %, en assurant elle-même la maintenance des machines sorties des contrats des constructeurs ; maîtriser les données et la sécurité de ses installations. Le système d'information s'est construit en deux mondes séparés : l'informatique de gestion, confiée à la DSI, et l'informatique de conduite des installations, gérée par la direction de l'exploitation avec les constructeurs et une entreprise de services du numérique.

Vous êtes directeur (directrice) de la performance et des systèmes d'information d'ESTRAVENT depuis janvier 2027 ; vous dirigez la DSI et le contrôle de gestion et vous rendez compte au directeur financier. La présidente-directrice générale, Mme Sidonie VARLAMBERT, vous demande trois travaux : préparer l'évolution de la stratégie et de l'organisation du SI, la renégociation d'un contrat et la transmission des savoirs (dossier 1) ; organiser et exploiter les données des installations, et en garder la maîtrise (dossier 2) ; maîtriser les coûts, la fiabilité et la sécurité du SI de conduite (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation d'ESTRAVENT Énergies et chiffres clés

ESTRAVENT Énergies SA développe, construit et exploite des parcs éoliens terrestres et des centrales solaires au sol en France, dans quatre régions : Grand Est, Hauts-de-France, Centre-Val de Loire et Occitanie. Son siège est à Reims (Marne). Chaque parc éolien et chaque centrale solaire est porté par une société de projet, détenue à 100 % par ESTRAVENT : les 102 sociétés de projet n'ont aucun salarié, et ESTRAVENT leur facture ses services. Les communes où sont implantés les parcs sont fictives. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**L'actionnariat et la gouvernance**

| Donnée | Valeur |
|---|---|
| Forme et cotation | société anonyme à conseil d'administration, cotée sur Euronext Growth depuis 2015 |
| Capital | fondateurs 34 % ; fonds d'infrastructure 21 % ; public 45 % |
| Conseil d'administration | 9 membres ; un comité d'audit ; présidente-directrice générale : Mme Sidonie VARLAMBERT, cofondatrice |
| Plan stratégique | « ESTRAVENT 2031 », adopté en mars 2027 par le conseil d'administration |

**Les installations et l'activité en 2026**

| Donnée | Valeur |
|---|---|
| Parcs éoliens terrestres | 64 parcs, 420 éoliennes, 1 000 MW ; les éoliennes viennent de trois constructeurs, désignés dans ce cas par les lettres A, B et C |
| Centrales solaires au sol | 38 centrales, 400 MW |
| Puissance installée | 1 400 MW ; objectif du plan : 2 500 MW en 2031 |
| Production | 2,7 TWh, dont éolien 2,2 TWh et solaire 0,5 TWh |
| Disponibilité moyenne des éoliennes | 95 % ; objectif du plan : 97 % |
| Chiffre d'affaires | 250 M€ |
| Projets en développement | 70 projets ; sept à neuf ans s'écoulent entre la recherche d'un site et la mise en service |

**La vente de l'électricité en 2026**

| Mode de vente | Part de l'électricité vendue |
|---|---|
| Contrats de vente à prix garanti de quinze ans | 70 % |
| Vente sur le marché par un agrégateur | 20 % |
| Trois contrats d'achat direct de dix ans avec des industriels, signés en 2025 et 2026 | 10 % ; objectif du plan : 40 % en 2031 |

18 parcs éoliens sortent de leur contrat de vente à prix garanti entre 2026 et 2029.

**L'effectif (520 salariés)**

| Direction | Effectif |
|---|---|
| Exploitation | 210 : centre de conduite 40, techniciens de maintenance 150, ingénieurs de la performance 20 ; la cellule supervision (8 personnes) fait partie de la direction de l'exploitation |
| Développement | 130, dans quatre agences régionales |
| Construction | 60 |
| Énergie (vente de l'électricité) | 25 |
| Fonctions support | 95, dont 22 à la DSI et 6 au contrôle de gestion |

**Le système d'information en quelques lignes**

En 2026, les dépenses du système d'information ont atteint 9 M€ : 5 M€ pour la DSI et 4 M€ pour l'informatique de conduite, dont 1,5 M€ pour le contrat de l'entreprise de services du numérique (ESN).

- **Informatique de conduite**, gérée par la direction de l'exploitation : dans chaque parc éolien, un système de supervision et d'acquisition de données fourni par le constructeur des éoliennes (trois constructeurs, trois systèmes), dont les données remontent aussi dans le nuage de chaque constructeur ; une **plateforme de supervision** commune au centre de conduite, développée en 2016 pour ESTRAVENT et maintenue par une ESN au forfait jusqu'au 31/12/2027 ; des systèmes de supervision propres aux centrales solaires.
- **Informatique de gestion**, confiée à la DSI : progiciel de gestion intégré (comptabilité, achats, immobilisations, facturation) ; paie ; logiciel de gestion de la maintenance en mode SaaS ; outil de prévision de la production fourni par un prestataire ; gestion des contrats de vente et facturation de l'électricité (tableurs et module du progiciel) ; système d'information géographique et gestion électronique des documents des projets ; gestion des relations avec les propriétaires des terrains et les communes ; messagerie et bureautique en ligne.
- Les données de production sont stockées dans une base de données relationnelle au siège.

**Organigramme simplifié (juin 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil d'administration, avec un comité d'audit | présidente : Mme Sidonie VARLAMBERT ; président du comité d'audit : M. Bernard ESCOLIÈRE, administrateur indépendant |
| Conseil d'administration | présidence-direction générale | Mme Sidonie VARLAMBERT |
| Présidente-directrice générale | direction financière | M. Thibault ORLANCOURT, directeur financier |
| | direction de l'exploitation : centre de conduite, cellule supervision, maintenance, ingénieurs de la performance | Mme Gaëlle MONTREVIAU, directrice de l'exploitation ; responsable du centre de conduite : M. Yannick FERRASSOT ; responsable de la cellule supervision : Mme Nadège QUILLEBRAND ; responsable des ingénieurs de la performance : M. Fabien LACROUZE |
| | direction de l'énergie (vente de l'électricité) | M. Arnaud VELDRIMONT, directeur de l'énergie |
| | direction du développement, avec quatre agences régionales | Mme Isaure TRÉMOLLAC, directrice du développement |
| | direction de la construction | M. Jérôme CALVIGNAC, directeur de la construction |
| | déléguée à la protection des données | Mme Léa VINCHEREAU |
| Directeur financier | direction de la performance et des systèmes d'information : DSI et contrôle de gestion | vous ; responsable de la DSI : M. Olivier SAUVERNAY ; responsable du contrôle de gestion : Mme Agnès DORMEVAL |

### ANNEXE 2.1 – Le référentiel des installations et les données de conduite (note de M. Fabien LACROUZE, responsable des ingénieurs de la performance, mai 2027)

**A. Les éoliennes et leurs données aujourd'hui**

| Constructeur | Éoliennes | Puissance | Âge moyen des éoliennes |
|---|---|---|---|
| A | 180 | 420 MW | 9 ans |
| B | 140 | 330 MW | 14 ans |
| C | 100 | 250 MW | 6 ans |
| **Ensemble** | **420** | **1 000 MW** | — |

- **Une même éolienne a trois noms, dans cinq systèmes de nommage.** Le système du constructeur A désigne ses éoliennes par leur numéro de machine (« 41207 »), celui de B par l'abréviation du parc et la position (« CSV-T03 »), celui de C par un code interne (« C-7731 ») ; la plateforme de supervision et le logiciel de gestion de la maintenance donnent à chacune un autre code (pour l'éolienne CSV-T03 de B : « P07-E03 » et « ÉOL-0287 »). Les alarmes ont le même défaut : A compte 2 500 codes d'alarme, B 1 800 et C 3 000, sans aucune correspondance ; une surchauffe du multiplicateur porte trois codes différents. Mes ingénieurs tiennent à la main, dans un tableur, la correspondance des 200 alarmes les plus fréquentes.
- **Les composants sont suivis dans des tableurs.** Les 2 100 composants majeurs des éoliennes (un multiplicateur, une génératrice et trois pales par machine) sont suivis par leur numéro de série dans quatre tableurs, un par région, tenus par les techniciens. En 2026, sur 200 composants contrôlés lors des visites, 30 ne correspondaient pas au tableur : composant remplacé sans mise à jour, numéro mal recopié ou saisi sur la mauvaise machine. En 2026, 60 composants majeurs ont été remplacés.
- **Les mesures saturent la base du siège.** Les éoliennes transmettent à la plateforme de supervision des moyennes à dix minutes de 80 mesures (vent, puissance, températures, vibrations…), stockées dans la base de données relationnelle du siège. Depuis 2025, elle reçoit aussi les mesures à la seconde d'une cinquantaine de variables de 60 éoliennes du constructeur A, dans le cadre d'un essai. La base est passée de 4 To en 2024 à 12 To en 2026 ; elle est occupée à 95 %, et l'extraction d'une année de mesures d'un parc prend une nuit.
- **Les analyses commencent par des exports.** Mes 20 ingénieurs exportent les mesures et les alarmes à la main, de la base et des portails des constructeurs, puis les mettent en forme dans des tableurs : environ 40 % de leur temps y passe.

**B. Les usages attendus des données**

1. **Analyses de la performance** : comparer les éoliennes d'un même modèle, repérer celles qui produisent moins que prévu pour le vent mesuré, expliquer l'énergie non produite.
2. **Maintenance prédictive** des multiplicateurs et des génératrices, à partir des mesures à la seconde.
3. **Reporting mensuel** de la disponibilité et de l'énergie non produite au comité de direction.
4. **Études de renouvellement** des parcs les plus anciens, qui comparent dix ans ou plus de production ; d'ici 2031, des éoliennes d'autres modèles, parfois d'autres constructeurs, remplaceront les plus anciennes.

**C. Les deux options d'architecture étudiées par la DSI**

| | Option 1 : entrepôt de données | Option 2 : lac de données et référentiel de données maîtres |
|---|---|---|
| Données reçues | moyennes à dix minutes, alarmes et interventions du logiciel de gestion de la maintenance, transformées chaque nuit | toutes les données, reçues telles quelles : moyennes à dix minutes, mesures à la seconde, alarmes, rapports d'intervention en PDF, photos des inspections de pales, données météorologiques |
| Organisation | une base structurée pour le reporting, alimentée par des traitements de chargement qui contrôlent et transforment les données | un lac organisé en « lakehouse » : une zone de données brutes, et une zone de données structurées et contrôlées, interrogeable comme un entrepôt ; un référentiel de données maîtres des installations (parcs, éoliennes, modèles, composants, liste commune des alarmes), tenu par un responsable désigné |
| Mise en service | 12 mois | 18 mois |

Aucun chiffrage du projet n'est attendu.

**D. Les règles de gestion du référentiel des installations**

Le référentiel ne porte, dans un premier temps, que sur les éoliennes.

- **RG1** – Un parc est identifié par un code ; on connaît son nom, sa commune, sa région et sa date de mise en service. Un parc compte une ou plusieurs éoliennes.
- **RG2** – Une éolienne est identifiée par un code unique attribué par ESTRAVENT ; on connaît son numéro de position dans le parc et sa désignation dans le système de son constructeur. Une éolienne appartient à un seul parc.
- **RG3** – Une éolienne relève d'un seul modèle. Un modèle est identifié par un code ; on connaît sa désignation, son constructeur et sa puissance. Un modèle peut n'équiper encore aucune éolienne d'ESTRAVENT (modèles étudiés pour le renouvellement).
- **RG4** – Un composant majeur (multiplicateur, génératrice ou pale) est identifié par son numéro de série ; on connaît son type. Une éolienne comporte au moins un composant majeur. À un moment donné, un composant est monté sur une seule éolienne, ou sur aucune lorsqu'il est en stock ou en réparation.
- **RG5** – Un remplacement est identifié par un numéro ; on connaît sa date et son motif (panne, usure, maintenance préventive). Il concerne une seule éolienne ; il retire un composant, le composant déposé, et en installe un autre, le composant posé. Au cours de sa vie, un composant peut être déposé lors de plusieurs remplacements et posé lors de plusieurs autres (après une réparation), ou d'aucun ; une éolienne peut n'avoir connu aucun remplacement.
- **RG6** – Un intervenant est identifié par un code ; on connaît son nom et sa catégorie (technicien d'ESTRAVENT ou entreprise sous-traitante). Un remplacement est réalisé par un ou plusieurs intervenants ; un intervenant peut n'avoir réalisé aucun remplacement.

### ANNEXE 2.2 – L'énergie non produite de 2024 à 2026 (tableaux de M. Fabien LACROUZE, avril 2027)

Conventions : l'**énergie non produite** est l'énergie que les éoliennes auraient produite, d'après le vent mesuré, pendant leurs arrêts et leurs réductions de puissance ; elle est estimée par les ingénieurs de la performance à partir des moyennes à dix minutes. La **disponibilité** est la part du temps pendant laquelle une éolienne est en état de produire : les pannes et la maintenance la réduisent ; les bridages, les arrêts pour la faune et le givre ne la réduisent pas, l'éolienne restant en état de produire.

**A. Énergie non produite par cause (en GWh, chiffres publiés)**

| Cause | 2024 | 2025 | 2026 |
|---|---|---|---|
| Pannes | 70 | 80 | 90 |
| Maintenance programmée | 30 | 25 | 25 |
| Bridages demandés par le gestionnaire du réseau | 20 | 35 | 50 |
| Arrêts pour la protection des oiseaux et des chauves-souris | 15 | 20 | 25 |
| Givre | 10 | 15 | 10 |
| **Ensemble** | **145** | **175** | **200** |

**B. Énergie non produite en 2026 par constructeur (en GWh) et disponibilité**

| Constructeur | Pannes | Maintenance programmée | Bridages | Faune | Givre | Ensemble | Par éolienne | Disponibilité 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|---|---|---|---|
| A (180 éoliennes) | 30 | 10 | 25 | 5 | 5 | 75 | environ 420 MWh | 96 % | 96 % | 96 % |
| B (140 éoliennes) | 40 | 10 | 15 | 15 | 0 | 80 | environ 570 MWh | 95 % | 94 % | 94 % |
| C (100 éoliennes) | 20 | 5 | 10 | 5 | 5 | 45 | 450 MWh | 96 % | 95 % | 95 % |
| **Ensemble** | **90** | **25** | **50** | **25** | **10** | **200** | — | **96 %** | **95 %** | **95 %** |

**C. Les pannes du multiplicateur**

| | 2024 | 2025 | 2026 |
|---|---|---|---|
| Part du multiplicateur dans l'énergie non produite par les pannes | 30 % | 35 % | 40 % |
| Multiplicateurs remplacés | 6 | 9 | 12, dont 8 sur des éoliennes du constructeur B |

Un multiplicateur qui casse immobilise l'éolienne 30 jours en moyenne, dont cinq jours de travaux : le reste est l'attente de la pièce et de la grue.

**D. Ce que l'on sait de ces chiffres**

- **Définition des causes revue en 2025** : depuis le 1er janvier 2025, l'attente du technicien après une panne, auparavant classée en maintenance programmée, est classée en pannes. Elle représente environ 5 GWh par an ; les chiffres de 2024 n'ont pas été recalculés.
- **Données manquantes** : à la suite d'un changement de son portail, les données du constructeur C de janvier et février 2026 n'ont jamais été reçues ; l'énergie non produite de ses éoliennes pendant ces deux mois, environ 10 GWh, manque dans les chiffres de 2026.
- **Arrêts mal saisis** : dans le parc de Castelvérune (20 éoliennes du constructeur B, en Occitanie), les arrêts pour la protection des chauves-souris, les soirs d'été, sont saisis comme des pannes depuis 2025, soit environ 10 GWh par an ; ils retirent environ un point à la disponibilité du constructeur B en 2025 et en 2026.

**E. L'affirmation de Mme Gaëlle MONTREVIAU, directrice de l'exploitation, au comité de direction du 15/04/2027**

« Nos pertes viennent du constructeur B ; il suffit de reprendre sa maintenance. »

### ANNEXE 2.3 – Les données des éoliennes chez les constructeurs (note de Mme Gaëlle MONTREVIAU, directrice de l'exploitation, mai 2027, et extraits des contrats)

**A. Ce que produisent les éoliennes.** L'automate de chaque éolienne enregistre environ 300 variables à la seconde (vent, puissance, orientation de la nacelle et des pales, températures, vibrations, pression d'huile…) et toutes ses alarmes. Ces données partent en continu vers le système de supervision du parc, puis vers le nuage du constructeur : environ 150 To par an pour les 420 éoliennes (65 To chez A, 50 To chez B, 35 To chez C). ESTRAVENT ne reçoit, par la plateforme de supervision, que les moyennes à dix minutes de 80 de ces variables et la liste des alarmes, avec les codes de chaque constructeur.

**B. Les conditions des trois constructeurs**

| | Constructeur A | Constructeur B | Constructeur C |
|---|---|---|---|
| Lieu de stockage des données à la seconde | centres de données situés dans l'Union européenne | centres de données situés dans l'Union européenne | nuage d'un fournisseur de services dont le siège est hors de l'Union européenne ; centres de données hors de l'Union européenne, dans des pays que le contrat ne précise pas |
| Accès d'ESTRAVENT aux données à la seconde | sur abonnement, 500 € par éolienne et par an ; essai sur 60 éoliennes depuis 2025, pour une cinquantaine de variables, soit 30 k€ par an | aucun : B utilise ces données pour sa propre maintenance | consultation sur le portail de C, sans export ; extraction ponctuelle sur demande, en quinze jours |
| Format | propre au constructeur | propre au constructeur | propre au constructeur |
| Transmission à un tiers | possible pour les éoliennes abonnées | refusée à tout prestataire de maintenance concurrent | non prévue |
| À la fin du contrat de maintenance du constructeur | accès maintenu sur abonnement | accès au portail fermé ; rien n'est prévu pour la restitution des données | rien n'est prévu |

**Extraits des contrats de maintenance**

- Constructeur A : « Les données de fonctionnement à la seconde sont accessibles au client au moyen d'un abonnement annuel par éolienne, au tarif en vigueur. »
- Constructeur B : « Les données collectées par le système du constructeur sont réservées à l'exécution du présent contrat. Elles ne peuvent être communiquées à un prestataire de maintenance tiers sans l'accord écrit du constructeur. »
- Constructeur C : « Le constructeur peut héberger les données dans tout centre de données exploité par lui-même ou par ses sous-traitants. »

**C. Les faits récents**

- En 2027, 40 éoliennes du constructeur B sortent de leur contrat de maintenance ; ESTRAVENT veut en confier l'entretien à une entreprise de maintenance indépendante, qui l'a prévenue : « Sans les mesures à la seconde, nous entretiendrons ces machines à l'aveugle. »
- Un ingénieur de la performance : « Quand un multiplicateur casse, je demande au constructeur les mesures des semaines précédentes. J'attends quinze jours, et je reçois un fichier que je ne peux comparer à aucun autre. »
- Mme MONTREVIAU : « Ces données sont produites par nos machines, sur nos parcs ; nous ne les voyons qu'à travers les constructeurs. »

Aucune analyse juridique des contrats n'est attendue.

### ANNEXE 2.4 – Le stockage des mesures (note de M. Olivier SAUVERNAY, responsable de la DSI, mai 2027)

**A. Aujourd'hui.** Toutes les mesures reçues depuis la mise en service du premier parc, en 2007, sont gardées sans limite de durée, en trois copies : la base de production, une copie de secours dans une seconde salle du siège, et une copie mensuelle chez un hébergeur. Copies comprises, hors exports des ingénieurs dans les tableurs du serveur de fichiers, le volume des mesures a été multiplié par trois en deux ans : 12 To en 2024, 36 To en 2026. Aucune règle ne dit ce qui doit être gardé, ni combien de temps.

**B. Ce que montrent les journaux de consultation de 2026**

- 90 % des consultations portent sur des mesures de moins de deux ans.
- Les moyennes à dix minutes de plus de cinq ans ne servent qu'aux études de renouvellement des parcs anciens, une dizaine par an.
- Les mesures à la seconde ne servent qu'à analyser les pannes, sur les semaines qui les précèdent, et à construire les modèles de maintenance prédictive. Selon les ingénieurs de la performance, ces modèles n'utilisent qu'une trentaine des 300 variables.

**C. Le projet de lac.** Dans l'option 2 de l'annexe 2.1, le lac recevrait et garderait sans limite toutes les mesures à la seconde des 420 éoliennes, avec trois copies : environ 150 To par an, soit 450 To par an copies comprises, auxquels s'ajouteront les mesures des nouveaux parcs.

**D. Les deux offres de centre de données reçues pour héberger le lac**

| | Offre 1 | Offre 2 |
|---|---|---|
| Localisation | France, Grand Est, à 30 km de Reims | France, Île-de-France |
| Consommation électrique des équipements informatiques du lac, estimée par la DSI pour la première année, pour le même matériel et sans l'effet du stockage à deux niveaux | 300 MWh | 300 MWh |
| PUE annoncé (énergie totale du centre / énergie des équipements informatiques) | 1,2 | 1,5 |
| Consommation électrique totale estimée pour la première année | 360 MWh | 450 MWh |
| Origine de l'électricité | électricité du réseau | électricité du réseau, et achat d'électricité solaire à un producteur pour la moitié de la consommation |
| Refroidissement | par l'air extérieur la plus grande partie de l'année | tours de refroidissement à eau, environ 5 000 m³ d'eau par an |
| Chaleur dégagée par les serveurs | récupérée et cédée au réseau de chaleur d'une commune voisine | non récupérée |
| Stockage proposé | deux niveaux : disques rapides pour les données récentes, stockage lent et peu consommateur pour les données anciennes | disques rapides pour toutes les données |
| Renouvellement des serveurs | tous les sept ans | tous les quatre ans |
| Informations environnementales remises au client | consommation électrique et PUE, chaque mois, pour les équipements du client | PUE annuel de l'ensemble du centre |

Les deux offres ont un prix voisin, et aucune procédure de choix de l'hébergeur n'est à organiser. Aucune ne fournit d'empreinte carbone. ESTRAVENT ne mesure aujourd'hui ni la consommation ni l'empreinte de son système d'information.

### ANNEXE 2.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir | Statut au 31/12/2026 |
|---|---|---|---|
| Accès aux données et changement de fournisseur | Règlement (UE) 2023/2854 sur les données (Data Act) | L'utilisateur d'un produit connecté peut accéder aux données que génère son utilisation et demander qu'elles soient transmises à un tiers de son choix ; les produits connectés mis sur le marché après le 12/09/2026 doivent être conçus de telle sorte que ces données soient, par défaut, accessibles à l'utilisateur. Les fournisseurs de services d'informatique en nuage doivent permettre à leurs clients de changer de fournisseur et d'emporter leurs données. | Applicable depuis le 12/09/2025 |
| Cloud de confiance | Référentiel du cloud de confiance du Cigref | Grille d'exigences fondée sur trois piliers : la sécurité ; l'immunité aux lois extra-européennes ; la maîtrise de la dépendance au fournisseur. Toute exigence opérationnelle doit être également exigible par contrat. Ce n'est ni un label, ni une certification. | Première version publiée le 27/05/2021 ; deuxième version disponible |

### Travail à faire

ESTRAVENT a 420 éoliennes, qui produisent chaque seconde des données dont elle ne voit qu'une petite partie, sous des noms différents selon les constructeurs, dans une base saturée. Elle ne sait pas expliquer sûrement son énergie non produite, et le plan « ESTRAVENT 2031 » lui demande de reprendre la maintenance des machines et la maîtrise de ses données. Mme VARLAMBERT vous demande d'organiser les données des installations, d'en tirer une analyse fiable de l'énergie non produite, d'apprécier la dépendance d'ESTRAVENT envers les constructeurs pour ses données et de rendre leur stockage plus sobre. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.5 ainsi que vos connaissances professionnelles.

**2.1 – Le référentiel des installations et l'architecture des données (4 points)**

a) À partir des règles de gestion de l'annexe 2.1 D, établissez le modèle conceptuel des données du référentiel des installations, puis traduisez-le en modèle logique, en énonçant les règles de passage que vous appliquez. Aucune requête n'est attendue.

b) Après avoir défini l'entrepôt de données, le lac de données et le référentiel de données maîtres, comparez les deux options de l'annexe 2.1 C selon trois critères que vous justifierez par les usages de l'annexe 2.1 B, puis recommandez une architecture. Montrez enfin comment elle règle les problèmes de nommage et de qualité des données décrits dans l'annexe 2.1 A.

**2.2 – L'analyse de l'énergie non produite (4 points)**

a) Décrivez la chaîne de traitement des données qui produira chaque mois l'analyse de l'énergie non produite, de la collecte à la restitution, en montrant à chaque étape une limite des chiffres de l'annexe 2.2 ou un problème de l'annexe 2.1 A qu'elle doit traiter.

b) Formulez trois constats argumentés tirés de l'annexe 2.2, puis appréciez l'affirmation de Mme MONTREVIAU. Aucun calcul statistique n'est attendu.

c) Indiquez ce qu'une démarche d'analyse prédictive apporterait à la maintenance des multiplicateurs, en précisant deux conditions de sa réussite et deux de ses limites. Proposez enfin la représentation visuelle qui montrerait le mieux au comité de direction l'énergie non produite par cause et par constructeur, et justifiez-la.

**2.3 – Les données des éoliennes et la souveraineté d'ESTRAVENT (2,5 points)**

a) Après avoir caractérisé le Big Data, montrez en quoi les données à la seconde des éoliennes en relèvent, et pourquoi la base de données relationnelle du siège ne peut pas les accueillir.

b) Analysez, à partir de l'annexe 2.3, les enjeux de souveraineté et de dépendance que crée la détention de ces données par les constructeurs : localisation, accès, coût, liberté de choisir la maintenance. Proposez ensuite trois mesures pour en reprendre la maîtrise, en mobilisant en principe les repères de l'annexe 2.5. Aucune analyse juridique du règlement ni des contrats n'est attendue.

**2.4 – La sobriété des données de mesure (2,5 points)**

a) Proposez, à partir de l'annexe 2.4, une politique de sobriété des données de mesure : la granularité conservée, les durées de conservation et le nombre de copies, en tenant compte des usages de l'annexe 2.1 B. Indiquez qui la décide et qui la fait respecter.

b) Après avoir défini une stratégie de transition numérique responsable, appréciez les deux offres de centre de données de l'annexe 2.4 D au regard de cette stratégie, puis concluez. Aucun calcul d'empreinte n'est attendu.

c) Proposez un indicateur de mesure de l'impact environnemental du lac, précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
