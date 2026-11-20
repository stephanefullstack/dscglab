# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 38

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DE LA REDEVANCE INCITATIVE (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 13, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en avril 2027. CASTELRIVE Agglomération est une communauté d'agglomération créée en 2017 qui regroupe 30 communes et 180 000 habitants, dont 62 000 dans la ville-centre de Castelrive. Elle exerce notamment les compétences de collecte des déchets ménagers, qu'elle assure en régie, de mobilités, de développement économique, d'habitat et de gestion de quatre piscines ; le traitement des déchets est confié à un syndicat auquel elle adhère, et le réseau de bus à un exploitant. Elle emploie 1 100 agents, dont 380 à la collecte et aux six déchèteries. Depuis 2025, les 78 000 foyers et 6 000 professionnels du territoire paient une redevance incitative d'enlèvement des ordures ménagères, qui comprend une part fixe et une part calculée selon le nombre de levées de leur bac, lu par les camions de collecte. Sa direction du numérique, forte de 45 agents, est mutualisée avec la ville de Castelrive : elle sert les deux collectivités et propose ses services à 18 petites communes membres. Les organisations, les personnes et les données de ce cas sont fictives.

Le projet de territoire « Castelrive 2032 », adopté en janvier 2027 par le conseil communautaire, fixe cinq objectifs : simplifier les démarches des usagers en offrant un guichet unique, en ligne et dans les mairies ; réduire de 15 % d'ici 2030 les ordures ménagères résiduelles collectées ; piloter les politiques publiques par les données et ouvrir les données du territoire ; garantir la continuité et la sécurité des services publics, numériques et techniques ; réduire l'empreinte environnementale du numérique. Le schéma directeur numérique 2022-2026 de la ville et de l'agglomération est arrivé à son terme, et un tiers des agents techniques partira en retraite d'ici 2032.

Vous êtes directeur(rice) général(e) adjoint(e) chargé(e) des ressources de CASTELRIVE Agglomération depuis 2025, rattaché(e) à la directrice générale des services, Mme Hélène VARSANGE ; vous supervisez les finances, les ressources humaines, les affaires juridiques et la relation avec la direction du numérique mutualisée. Mme VARSANGE vous demande trois travaux : préparer le futur schéma directeur numérique et la transmission des savoirs (dossier 1) ; organiser et exploiter les données de la redevance incitative (dossier 2) ; fiabiliser, sécuriser et rendre plus sobre le système d'information (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de CASTELRIVE Agglomération et chiffres clés

CASTELRIVE Agglomération est une communauté d'agglomération créée en 2017. Son siège est à Castelrive, la ville-centre. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Le territoire et les compétences**

| Donnée | Valeur |
|---|---|
| Communes membres | 30 : la ville-centre de Castelrive (62 000 habitants), quatre communes de 8 000 à 15 000 habitants et 25 communes rurales ou périurbaines |
| Population | 180 000 habitants |
| Compétences exercées (principales) | collecte des déchets ménagers, en régie : 40 camions de collecte, six déchèteries ; mobilités ; développement économique ; habitat ; gestion de quatre piscines |
| Compétences confiées à des tiers | traitement des déchets : syndicat auquel l'agglomération adhère ; réseau de bus : exploitant |
| Usagers de la collecte | 78 000 foyers et 6 000 professionnels ; environ 85 000 bacs équipés d'une puce |

**La redevance incitative en quelques lignes**

Depuis 2025, chaque foyer et chaque professionnel paie une redevance incitative d'enlèvement des ordures ménagères. Elle comprend une part fixe annuelle, qui dépend du volume du bac, et une part variable, due pour chaque levée au-delà d'un forfait de 12 levées par an. Chaque levée est lue par le camion de collecte, qui identifie la puce du bac ; les levées sont transmises au logiciel de facturation. La facture est semestrielle.

**L'effectif au 31/12/2026**

| Direction ou service | Agents |
|---|---|
| Collecte et déchèteries | 380 |
| Piscines et équipements | 210 |
| Services techniques (voirie des zones d'activités, bâtiments, ateliers) | 220 |
| Mobilités, développement économique et habitat | 70 |
| Fonctions ressources (finances, ressources humaines, affaires juridiques, relation aux usagers) | 170 |
| Administration générale et cabinet | 50 |
| **Total** | **1 100** |

Environ 600 agents travaillent sur le terrain, sans poste informatique attitré. Les 45 agents de la direction du numérique mutualisée sont des agents de la ville de Castelrive : ils ne sont pas compris dans l'effectif ci-dessus.

**La direction du numérique mutualisée et le système d'information en quelques lignes**

La direction du numérique est portée par la ville de Castelrive et mutualisée avec l'agglomération : elle sert les deux collectivités et propose ses services à 18 petites communes membres. Elle exploite deux salles informatiques, l'une à l'hôtel de ville, l'autre au siège de l'agglomération. Le système d'information comprend notamment : des progiciels de gestion financière et de gestion des ressources humaines partagés par la ville et l'agglomération ; le logiciel de facturation de la redevance, acquis auprès d'un éditeur et hébergé chez lui ; les ordinateurs embarqués et les lecteurs de puces des 40 camions ; le logiciel de contrôle d'accès des six déchèteries, où l'on entre avec un badge ; les logiciels de caisse et de billetterie des piscines ; la télégestion des chaufferies et du traitement de l'eau des piscines ; le site internet et ses formulaires en ligne ; la messagerie et la bureautique. En 2026, les dépenses du numérique de l'agglomération (contribution à la direction mutualisée et projets propres) ont atteint environ 4 M€.

**Organigramme simplifié (avril 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | président de CASTELRIVE Agglomération | M. Arnaud TELMONDIER |
| Rattachée au président | directrice générale des services | Mme Hélène VARSANGE |
| Rattaché(e) à la directrice générale des services | directeur(rice) général(e) adjoint(e) chargé(e) des ressources : finances, ressources humaines, affaires juridiques, relation avec la direction du numérique mutualisée | vous |
| Rattachées à la directrice générale des services | direction de la collecte et des déchèteries ; direction des piscines et des équipements ; direction des services techniques ; direction des mobilités et du développement | — |
| Service de la ville de Castelrive, au service des deux collectivités | direction du numérique mutualisée | — |

### ANNEXE 2.1 – Les données de la redevance aujourd'hui (note de Mme Sylvie DARNÉZAN, responsable du service de la facturation de la redevance, mars 2027)

**A. Les règles de gestion de la redevance**

Le service de la facturation a écrit, avec la direction de la collecte, les règles de gestion suivantes :

- **RG1** – Un logement est identifié par un numéro unique attribué par l'agglomération. Il est situé à une adresse, désignée par son code dans le référentiel des adresses ; on connaît aussi son complément d'adresse (bâtiment, étage, porte) et son type (maison ou appartement).
- **RG2** – Un foyer est identifié par un numéro unique ; on connaît le nom du titulaire du compte, son téléphone et son adresse électronique.
- **RG3** – Un logement peut être occupé successivement par plusieurs foyers ; un foyer peut occuper successivement plusieurs logements du territoire. Pour chaque occupation, on enregistre la date d'arrivée et la date de départ du foyer. Un logement peut être vacant ; un foyer connu du service occupe ou a occupé au moins un logement.
- **RG4** – Un bac est identifié par le numéro gravé sur sa cuve. Il porte une puce, dont on enregistre le numéro : la puce peut être remplacée sans que le bac change. On connaît aussi son volume, en litres, et sa date de mise en service. Un bac est affecté à un seul logement, et non à une personne : il reste dans le logement quand le foyer déménage. Un logement dispose d'aucun, d'un ou de plusieurs bacs.
- **RG5** – Une tournée est identifiée par un numéro ; on connaît sa date, son secteur et l'immatriculation du camion qui l'a effectuée.
- **RG6** – Une levée est identifiée par un numéro. Elle concerne un seul bac et elle est lue par le camion lors d'une seule tournée, à une date et à une heure qui sont enregistrées. Un bac peut n'avoir encore fait l'objet d'aucune levée ; une tournée comporte au moins une levée.
- **RG7** – Un foyer reçoit des factures semestrielles. Une facture est identifiée par un numéro ; elle est adressée à un seul foyer ; on connaît son semestre, sa date d'émission et son montant. Un foyer qui vient d'arriver peut n'avoir encore reçu aucune facture.
- **RG8** – Les professionnels suivent les mêmes règles : leur local est enregistré comme un logement. Les tarifs, le calcul du montant des factures, les paiements et les réclamations ne sont pas concernés par ces règles.

**B. Extrait du modèle logique actuel du logiciel de facturation**

Clé primaire en gras ; # : clé étrangère.

- REDEVABLE (**num_redevable**, nom, adresse, commune, telephone, courriel, num_puce, volume_bac, date_arrivee)
- LEVEE (**num_levee**, num_puce, date_levee)
- FACTURE (**num_facture**, semestre, date_emission, nb_levees, montant, #num_redevable)

Précisions de Mme DARNÉZAN :
- « L'adresse est saisie en texte libre par l'agent qui crée la fiche : nous avons, pour un même logement, "12 r. des Lilas", "12 rue des lilas bât. B" ou "Les Lilas, 12". »
- « Le numéro de puce figure dans la fiche du redevable. Dans la table des levées, ce n'est qu'un numéro lu par le camion : quand aucune fiche ne porte ce numéro, par exemple parce que la puce vient d'être remplacée, la levée est mise de côté. »
- « Quand un foyer emménage, deux pratiques coexistent : certains agents remplacent, dans la fiche existante, le nom, le téléphone, le courriel et la date d'arrivée, et l'ancien occupant disparaît ; d'autres créent une nouvelle fiche en y recopiant le numéro de puce du bac resté dans le logement. »

**C. Les anomalies relevées en 2026**

- Environ 2 millions de levées ont été lues par les camions. 40 000 d'entre elles, soit une sur cinquante, n'ont été rattachées à aucun redevable, dont les trois quarts dans la ville-centre. Deux agents de la direction de la collecte consacrent chacun une journée par semaine à les rapprocher à la main.
- Le logiciel compte 80 000 fiches de foyers pour 78 000 foyers : environ 2 000 doublons, le plus souvent un même logement dont l'adresse est écrite de deux façons, ou un nouvel occupant créé sans que la fiche de l'ancien soit close.
- Environ 1 700 factures sur 168 000 ont été adressées à un foyer qui avait quitté son logement.
- Lorsqu'un foyer conteste une levée, le service ne peut dire ni à quelle heure, ni lors de quelle tournée, ni par quel camion le bac a été levé : « nous ne savons pas prouver une levée ».
- Le logiciel ne permet pas de savoir quel foyer occupait un logement à une date passée.

### ANNEXE 2.2 – Les données à réunir et les deux options proposées (note de M. Yann PELVOISIN, chargé d'études des données de la direction de la collecte, mars 2027)

**A. Les données à réunir pour piloter la redevance et la prévention des déchets**

| Données | Producteur et lieu de stockage | Forme | Volume et fréquence |
|---|---|---|---|
| Levées des bacs | camions de collecte ; logiciel de facturation de l'éditeur | enregistrements structurés (puce, date et heure, camion) ; le logiciel de facturation n'en garde que la puce et la date | environ 2 millions par an ; à chaque tournée |
| Passages et apports en déchèterie | logiciel de contrôle d'accès des six déchèteries ; pesée des bennes à leur enlèvement | enregistrements structurés (badge, date, type d'apport) ; poids par benne | environ 300 000 passages par an ; en continu |
| Remplissage des 300 colonnes de verre | capteurs posés en 2026 ; plateforme en ligne du fabricant | mesures horodatées (taux de remplissage, température) | une mesure par heure et par capteur, soit environ 2,6 millions par an ; en continu |
| Réclamations sur les levées et les factures | courriels, formulaires du site, tableur de suivi du service de la facturation | textes libres, parfois des photographies | près de 20 000 par an |
| Signalements de dépôts sauvages | application de signalement de la ville, depuis 2025 ; appels des mairies notés dans un tableur | photographies géolocalisées, commentaires | environ 1 500 en 2026 |
| Tonnages collectés et traités, refus de tri | syndicat de traitement | tableurs mensuels | quelques centaines de lignes par mois, transmises avec deux mois de retard |
| Adresses et logements | chacune des 30 communes | tableurs ou logiciels différents, sans format commun ; 6 communes n'ont pas de liste à jour | mises à jour irrégulières |

Le fabricant des capteurs conserve les mesures sur sa plateforme, qui n'affiche qu'un tableau de bord par colonne ; il facture 15 k€ par an l'export de l'historique.

**B. Les deux options proposées par la direction du numérique mutualisée**

- **Option A – Un entrepôt de données classique.** Chaque mois, les données structurées (levées, factures, passages en déchèterie, tonnages) sont extraites, nettoyées et chargées dans un entrepôt organisé par date, commune, flux de déchets et type de logement. Pour les capteurs, seule une moyenne journalière par colonne est chargée ; les réclamations et les photographies ne sont pas reprises. Les adresses continuent d'être rapprochées à partir des fichiers des communes. Mise en place en neuf mois.
- **Option B – Un lac de données associé à un entrepôt, ou réunis dans une architecture « lakehouse ».** Toutes les données, y compris les mesures des capteurs en continu, les textes des réclamations et les photographies, sont conservées brutes, avec leur historique, dans le lac ; les données nécessaires aux indicateurs de pilotage sont structurées dans l'entrepôt. Une architecture « lakehouse » réunit sur une même plateforme le stockage des données brutes et des tables structurées, avec des règles de gouvernance communes. L'option comprend un **référentiel des adresses et des logements**, tenu avec les 30 communes : chaque commune y crée et met à jour ses adresses et ses logements, l'agglomération les valide, et le logiciel de facturation, le logiciel des déchèteries et les analyses l'utilisent. Mise en place en quinze mois, en deux étapes.

Aucune des deux options n'est chiffrée à ce stade. La direction du numérique mutualisée penche pour l'option A : « C'est plus simple, et nos équipes savent le faire. » M. PELVOISIN : « Avec l'option A, nous perdrons le détail des capteurs et des réclamations, et nous continuerons de rapprocher les adresses à la main. »

### ANNEXE 2.3 – Deux ans de redevance incitative (tableau préparé par M. PELVOISIN, mars 2027)

**A. Les indicateurs de 2024 et de 2026**

| Indicateur | Ville-centre 2024 | Ville-centre 2026 | Quatre communes moyennes 2024 | Quatre communes moyennes 2026 | 25 communes rurales et périurbaines 2024 | 25 communes rurales et périurbaines 2026 |
|---|---|---|---|---|---|---|
| Population | 63 000 | 62 000 | 44 000 | 44 000 | 71 000 | 74 000 |
| Ordures ménagères résiduelles collectées (kg par habitant) | 250 | 225 | 240 | 192 | 220 | 154 |
| Emballages et papiers collectés pour le tri (kg par habitant) | 50 | 60 | 55 | 70 | 60 | 80 |
| Apports en déchèterie (kg par habitant) | 150 | 160 | 210 | 240 | 240 | 290 |
| Refus de tri (part des emballages et papiers collectés qui ne peuvent pas être triés) | 15 % | 18 % | 15 % | 22 % | 15 % | 28 % |
| Signalements de dépôts sauvages | 300 | 900 | 100 | 200 | 100 | 400 |
| Levées moyennes par foyer et par an | — | 24 | — | 18 | — | 13 |
| Contestations de factures, pour 1 000 redevables | — | 260 | — | 200 | — | 170 |

Ordures ménagères résiduelles collectées sur tout le territoire : environ 42 000 tonnes en 2024, environ 34 000 tonnes en 2026.

**B. L'affirmation du vice-président**

M. Rémi BASTÉROLE, vice-président chargé des déchets et de la prévention : « Les chiffres sont clairs : la redevance a fait baisser nos déchets de 20 % en deux ans. L'objectif de "Castelrive 2032" est déjà dépassé. Je veux l'annoncer au prochain conseil communautaire, avec un graphique. »

**C. Les limites signalées par M. PELVOISIN**

- Les quantités par habitant sont rapportées à la population municipale de chaque année. Dix communes rurales comptent de nombreuses résidences secondaires, dont les occupants ne sont pas comptés dans cette population.
- Les déchets des professionnels sont collectés avec ceux des foyers. Depuis 2025, environ 500 professionnels, surtout de la ville-centre, ont confié leurs déchets à un collecteur privé : ces déchets ne sont plus comptés.
- En 2025, le syndicat de traitement a changé de prestataire pour son centre de tri ; le nouveau prestataire mesure les refus de tri selon une autre méthode.
- Les tonnages de 2024 par type de commune ont été reconstitués à partir des pesées des camions, dont les tournées traversent souvent plusieurs communes. Les levées de 2024 n'ont pas été enregistrées : les lecteurs de puces ont été installés progressivement au cours de l'année.
- L'application de signalement des dépôts sauvages n'existe que dans la ville-centre, depuis 2025 ; ailleurs, les signalements sont ceux que les mairies transmettent par téléphone.
- 2025, année de mise en place de la redevance, n'est pas présentée : la comparaison ne porte que sur deux années.

### ANNEXE 2.4 – Les demandes sur les données (mars 2027)

**A. La publication des données du territoire**

En février 2027, le conseil communautaire a décidé de publier les données du territoire sur un portail de données ouvertes. La règle applicable à l'agglomération au 31/12/2026, donnée par l'énoncé et qui n'est pas à discuter, est la suivante : l'agglomération met en ligne, dans un format ouvert et librement réutilisable, les données qu'elle produit ou reçoit dans le cadre de ses missions et dont la publication présente un intérêt, sous réserve de la protection de la vie privée ; des données comportant des données à caractère personnel ne sont publiées qu'après un traitement qui empêche d'identifier les personnes.

La direction de la collecte propose de publier six jeux de données :

| N° | Jeu de données |
|---|---|
| J1 | tonnages mensuels collectés, par commune et par flux de déchets, de 2024 à 2026 |
| J2 | emplacement des 300 colonnes de verre et leur taux de remplissage, heure par heure |
| J3 | fichier des levées : pour chaque bac, adresse du logement, date et heure de chaque levée |
| J4 | nombre moyen de levées par foyer, par commune et par semestre |
| J5 | signalements de dépôts sauvages : photographies, position exacte, commentaires des agents |
| J6 | horaires et fréquentation des six déchèteries, par jour et par tranche horaire |

La plus petite commune du territoire compte 180 habitants et 80 foyers ; environ 40 rues du territoire comptent moins de cinq logements. Les agents relèvent que les dépôts sauvages contiennent souvent des courriers ou des cartons d'expédition portant un nom et une adresse, et que certaines photographies montrent des personnes ou des plaques d'immatriculation.

**B. La proposition de KOMPAVEL**

KOMPAVEL, jeune entreprise de Castelrive qui vend des composteurs et des services de conseil en prévention des déchets, propose d'acheter 30 k€ par an un fichier mensuel des levées par foyer (nom du titulaire, adresse, nombre de levées du mois), pour proposer un composteur et un accompagnement aux foyers qui présentent le plus souvent leur bac. Elle demande l'exclusivité de ce fichier pendant trois ans. Son dirigeant : « Tout le monde y gagne : moins de déchets pour vous, des clients pour nous. » M. BASTÉROLE est favorable : « 30 k€ de recettes et moins de déchets, c'est une bonne affaire. »

**C. Le délégué à la protection des données**

Depuis 2019, la ville et l'agglomération ont désigné le même délégué à la protection des données (DPO), Mme Agnès VILLEROUSSE, agente de la ville rattachée au directeur du numérique mutualisé, qui y consacre un mi-temps. En 2024 et en 2025, elle a aussi été la cheffe du projet de mise en place du logiciel de facturation de la redevance. Le registre des activités de traitement de l'agglomération compte 35 fiches ; celle de la redevance date de 2023 : elle ne mentionne ni les levées horodatées, ni l'hébergement du logiciel chez l'éditeur, ni les échanges avec les communes. Mme VILLEROUSSE n'a été consultée ni sur les options de l'annexe 2.2, ni sur la proposition de KOMPAVEL.

**D. Les durées de conservation**

Durées fixées par le tableau de gestion des archives de l'agglomération (données par l'énoncé, qui ne sont pas à discuter) :

| Données | Durée de conservation | Sort à l'issue |
|---|---|---|
| Factures de la redevance | dix ans à compter de leur émission, dont deux ans dans le logiciel de facturation, puis en archivage intermédiaire | destruction |
| Levées détaillées (bac, date, heure, tournée) | jusqu'à la fin du délai de contestation de la facture qu'elles justifient, soit au plus deux ans après son émission | destruction ; seules des données agrégées par commune et par mois sont conservées au-delà, pour l'analyse |
| Fiche d'un foyer parti | deux ans après son départ et le paiement de sa dernière facture | destruction |
| Tonnages annuels et rapports aux élus | sans limite | conservation définitive dans les archives de l'agglomération |

Pratiques constatées en mars 2027 : le logiciel de l'éditeur conserve toutes les levées et toutes les fiches depuis sa mise en service, en 2025, sans purge ; le tableur de suivi des réclamations n'a jamais été purgé ; les extractions de levées envoyées aux communes qui en font la demande sont conservées dans les messageries.

### ANNEXE 2.5 – Le coût du dispositif numérique de la redevance (note du contrôle de gestion, mars 2027)

**A. Les coûts de 2026**

| Poste | Coût annuel (k€) |
|---|---|
| Abonnement au logiciel de facturation en ligne de l'éditeur | 240 |
| Maintenance des lecteurs de puces et des ordinateurs embarqués des 40 camions | 80 |
| Remplacement des puces (environ 4 000 puces par an) | 40 |
| Transmissions entre les camions et le logiciel | 20 |
| Part de la direction du numérique mutualisée (deux équivalents temps plein) | 100 |
| Temps du service de la facturation et des réclamations (huit agents) | 360 |
| **Total** | **840** |

Ne sont comptées que les dépenses que la comptabilité analytique de l'agglomération rattache au dispositif. Le contrat avec l'éditeur prend fin en 2029 ; il ne précise pas les conditions dans lesquelles les données seront restituées à l'agglomération à son terme. Le ramassage des dépôts sauvages mobilise l'équivalent de trois agents des services techniques.

**B. Le rapport trimestriel actuel aux élus**

Chaque trimestre, les élus reçoivent une page : les tonnages collectés par flux (ordures ménagères résiduelles, emballages et papiers, verre, déchèteries), comparés au même trimestre de l'année précédente. Le rapport ne dit rien du coût du dispositif, de la qualité des données, des réclamations ni des dépôts sauvages. Mme VARSANGE : « Je veux savoir ce que nous coûte ce dispositif et quels risques il nous fait courir, pas seulement combien de tonnes nous collectons. »

### ANNEXE 2.6 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Une donnée à caractère personnel est toute information se rapportant à une personne physique identifiée ou identifiable, directement ou indirectement. Les données sont collectées pour des finalités déterminées et ne sont pas traitées ultérieurement de manière incompatible avec elles ; elles sont limitées à ce qui est nécessaire (minimisation) et conservées pendant une durée n'excédant pas celle nécessaire aux finalités. Chaque responsable du traitement tient un registre des activités de traitement. La désignation d'un délégué à la protection des données est obligatoire pour les autorités et organismes publics ; un même délégué peut être désigné pour plusieurs d'entre eux, compte tenu de leur structure et de leur taille. Le délégué informe et conseille le responsable du traitement et les agents, contrôle le respect du règlement et coopère avec l'autorité de contrôle ; il dispose des moyens nécessaires et ses autres missions ne doivent pas entraîner de conflit d'intérêts. | Applicable depuis le 25/05/2018. Une proposition européenne de simplification (« omnibus numérique », 19/11/2025) modifiant ce règlement est en discussion et n'est pas applicable. |
| L'anonymisation de données personnelles (publication de l'autorité de contrôle française, 19/05/2020) | L'anonymisation rend impossible, en pratique et de façon irréversible, l'identification des personnes ; des données anonymisées ne sont plus des données personnelles. Trois critères permettent de l'apprécier : l'individualisation (il ne doit pas être possible d'isoler un individu), la corrélation (il ne doit pas être possible de relier des ensembles de données distincts concernant un même individu) et l'inférence (il ne doit pas être possible de déduire de façon quasi certaine de nouvelles informations sur un individu). La pseudonymisation, qui remplace les données directement identifiantes par un pseudonyme, laisse les données personnelles. | Publiée le 19/05/2020 |
| La monétisation des données personnelles (publication de l'autorité de contrôle française, 17/11/2025) | Une personne ne peut pas céder la propriété de ses données personnelles ni renoncer aux garanties dont elle bénéficie sur ces données. | Publiée le 17/11/2025 |
| Règlement (UE) 2022/868 sur la gouvernance européenne des données (Data Governance Act) | Fixe notamment les conditions de la réutilisation de certaines catégories de données protégées détenues par les organismes du secteur public, dont les données personnelles ; les accords qui accordent un droit exclusif de réutilisation de ces données sont en principe interdits. Encadre aussi les services d'intermédiation de données et l'altruisme en matière de données. | Applicable depuis le 24/09/2023 |
| Règlement (UE) 2023/2854 sur les données (Data Act) | Donne à l'utilisateur d'un produit connecté un droit d'accès aux données générées par l'utilisation de ce produit ; facilite le changement de fournisseur de services de traitement de données en nuage. | Applicable depuis le 12/09/2025 |
| DAMA-DMBOK (DAMA International), 2e édition | Référentiel de bonnes pratiques de gestion des données, organisé en onze domaines autour de la gouvernance des données, dont l'architecture des données, la modélisation, les données de référence et les données maîtres, la qualité des données, l'entreposage et l'informatique décisionnelle. | 2e édition (2017), révisée en 2024 |

Il n'est demandé aucune analyse juridique.

### Travail à faire

Deux ans après la mise en place de la redevance incitative, ses données sont dispersées, peu fiables et peu exploitées, alors que « Castelrive 2032 » veut piloter les politiques publiques par les données et ouvrir les données du territoire. Mme VARSANGE vous demande d'organiser les données de la redevance, de choisir l'architecture qui les réunira, d'analyser l'effet de la redevance, de répondre aux demandes dont ces données font l'objet et d'éclairer le coût du dispositif et son pilotage. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.6 ainsi que vos connaissances professionnelles.

**2.1 – Le modèle des données de la redevance (2,5 points)**

a) Relevez trois défauts du modèle logique actuel (annexe 2.1 B) au regard des règles de gestion de l'annexe 2.1 A, en reliant chacun à une anomalie de l'annexe 2.1 C.

b) Après avoir distingué le modèle conceptuel et le modèle logique des données, construisez le modèle conceptuel des données de la redevance (entités, identifiants, attributs, associations et cardinalités) à partir des règles de gestion de l'annexe 2.1 A, puis déduisez-en le modèle logique en énonçant les règles de passage utilisées. Aucune requête n'est attendue.

**2.2 – L'architecture des données et le référentiel des adresses et des logements (2 points)**

a) Après avoir défini l'entrepôt de données et le lac de données, comparez les deux options de l'annexe 2.2 B selon trois critères (le volume et la variété des données, leur qualité et leur historique, les usages attendus), puis recommandez l'une d'elles en la justifiant.

b) Après avoir défini les données de référence, justifiez le référentiel des adresses et des logements partagé avec les communes, puis précisez deux règles de son fonctionnement. Aucune expertise des infrastructures n'est attendue.

**2.3 – L'effet de la redevance incitative (4 points)**

a) Décrivez la chaîne de traitement qui permettra d'analyser de façon fiable l'effet de la redevance, en illustrant chacune de ses cinq étapes (collecte, nettoyage, structuration, analyse, restitution) par les sources et les limites des annexes 2.2 et 2.3.

b) Justifiez la méthode d'analyse que vous retenez pour exploiter l'annexe 2.3 (analyse descriptive, puis exploratoire), puis formulez trois constats argumentés tirés de cette annexe, chacun assorti d'une précaution de lecture. Aucun calcul statistique n'est attendu.

c) Appréciez l'affirmation du vice-président (annexe 2.3 B), puis proposez deux représentations visuelles adaptées aux élus du conseil communautaire, en justifiant chacune.

**2.4 – L'ouverture et la valorisation des données (2,5 points)**

a) Après avoir distingué anonymisation et pseudonymisation, indiquez, pour chacun des six jeux de données de l'annexe 2.4 A, s'il peut être publié et à quelles conditions, en vous appuyant sur les trois critères de l'anonymisation rappelés dans l'annexe 2.6.

b) Appréciez de façon critique la proposition de KOMPAVEL (annexe 2.4 B), puis formulez une recommandation.

c) Précisez le rôle du délégué à la protection des données mutualisé entre la ville et l'agglomération, en relevant deux points à corriger dans la situation décrite par l'annexe 2.4 C, puis présentez les règles de conservation et d'archivage à appliquer aux données de la redevance au regard de l'annexe 2.4 D.

**2.5 – Le coût du dispositif numérique de la redevance et son pilotage (2 points)**

a) Après avoir défini le coût complet d'un système d'information (coût total de possession), calculez de tête le coût annuel du dispositif numérique de la redevance par redevable à partir de l'annexe 2.5, puis relevez dans les annexes deux coûts cachés que ce calcul omet.

b) Proposez deux indicateurs qui complètent le rapport trimestriel actuel aux élus (annexe 2.5 B), l'un de coût, l'autre de risque, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
