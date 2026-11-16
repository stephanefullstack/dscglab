# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 25

**DOSSIER 1 – ÉCLAIRER LA STRATÉGIE DU SYSTÈME D'INFORMATION ET PRÉPARER SA REFONTE (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 9, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. Les Vignerons de ROCALDÈNE sont une union de coopératives agricoles dont le siège est à Pézenas, dans l'Hérault. Fondée en 1987, l'union regroupe neuf caves coopératives de l'Hérault et de l'Aude, auxquelles environ 1 400 viticulteurs apportent la vendange de quelque 6 500 hectares de vignes. Chaque cave reçoit et vinifie la vendange de ses adhérents ; l'union assemble et élève les vins, les conditionne sur son site de Pézenas et les commercialise en vrac auprès de négociants, en bouteilles auprès de la grande distribution et à l'export. L'union est administrée par un conseil composé des présidents des neuf caves, que préside M. Gilles ESCOURBIAC, viticulteur ; sa directrice générale, Mme Hélène MAZERANDE, dirige les services de l'union. L'union et ses caves emploient 260 salariés permanents, rejoints par environ 180 saisonniers pendant les vendanges. Le chiffre d'affaires de l'union s'est élevé à 145 millions d'euros en 2026 ; 2,2 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « ROCALDÈNE 2030 », adopté par le conseil de l'union en décembre 2026, fixe trois priorités : adapter le vignoble et l'offre au changement climatique et conquérir de nouveaux marchés, notamment à l'export et dans la vente en ligne ; mieux connaître la qualité des apports, de la parcelle à la bouteille, pour mieux la valoriser ; garantir la continuité du système d'information pendant les campagnes et en réduire l'empreinte environnementale. Mme MAZERANDE en rend compte au conseil à chaque réunion.

Vous êtes responsable administratif et financier adjoint de l'union depuis 2025, rattaché à la directrice générale et chargé du projet de refonte du système d'information. Mme MAZERANDE vous demande trois travaux : éclairer la stratégie du système d'information et préparer sa refonte (dossier 1) ; organiser et exploiter les données des parcelles et des apports, et apprécier un projet d'authentification des bouteilles (dossier 2) ; assurer la continuité du système d'information pendant les vendanges, fiabiliser les apports et choisir un hébergement responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation des Vignerons de ROCALDÈNE et chiffres clés

Les Vignerons de ROCALDÈNE sont une union de coopératives agricoles fondée en 1987, dont le siège et le site de conditionnement sont à Pézenas (Hérault). Neuf caves coopératives de l'Hérault et de l'Aude en sont membres. Les viticulteurs sont adhérents de leur cave : chaque cave reçoit la vendange de ses adhérents pendant les vendanges, de fin août à mi-octobre, la vinifie et conserve les vins dans ses cuves. L'union assemble et élève les vins des neuf caves, les conditionne et les commercialise. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires de l'union | 145 M€ : vrac auprès de négociants 35 % (environ 51 M€), bouteilles vendues à la grande distribution en France 40 % (58 M€), export 25 % (environ 36 M€ ; Europe du Nord, Amérique du Nord, Asie) ; vente en ligne aux particuliers à l'étude |
| Vendange 2026 | environ 380 000 hectolitres, soit 380 milliers d'hectolitres |
| Vignoble | environ 6 500 hectares, exploités par environ 1 400 viticulteurs adhérents des caves |
| Effectif permanent | 260 salariés : environ 150 à l'union (conditionnement et logistique 75, commercial et service clients 25, production, qualité et laboratoire 20, services administratifs et financiers et direction 24, équipe informatique 6) et 110 dans les caves ; environ 180 saisonniers dans les caves pendant les vendanges ; aucune cave n'a d'informaticien |
| Système d'information | à l'union : un progiciel de gestion (gestion commerciale, stocks, comptabilité), dont le support par l'éditeur s'arrête fin 2028 ; le laboratoire d'analyses de l'union ; un portail des adhérents aux fonctions limitées ; une salle informatique au siège de Pézenas. Dans chaque cave : un logiciel de cave (réception et pesée des apports, suivi des cuves) ; les neuf caves utilisent les logiciels de quatre éditeurs différents |
| Budget du système d'information | 2,2 M€ (environ 1,5 % du chiffre d'affaires) |
| Plan « ROCALDÈNE 2030 » (adopté en décembre 2026) | adapter le vignoble et l'offre au changement climatique et conquérir de nouveaux marchés (export, vente en ligne) ; mieux connaître la qualité des apports, de la parcelle à la bouteille, pour mieux la valoriser ; garantir la continuité du système d'information pendant les campagnes et en réduire l'empreinte environnementale |

**Les neuf caves coopératives**

| Cave | Département | Adhérents | Vignes (hectares) | Salariés permanents |
|---|---|---|---|---|
| Cave de CAUSSELAC | Hérault | 230 | 1 100 | 18 |
| Cave de ROQUEVERNE | Hérault | 200 | 950 | 16 |
| Cave de LAURADEL | Aude | 180 | 850 | 14 |
| Cave de SAINT-BRÉZIAN | Hérault | 170 | 800 | 13 |
| Cave de CABRISSAC | Aude | 150 | 700 | 12 |
| Cave de GRAUSSELLE | Hérault | 140 | 650 | 11 |
| Cave de PECHAUROUX | Aude | 130 | 550 | 10 |
| Cave de TERRAGOUSSE | Hérault | 110 | 500 | 9 |
| Cave de VALCROZIÈRES | Aude | 90 | 400 | 7 |
| **Total** | | **1 400** | **6 500** | **110** |

Chaque cave est dirigée par un directeur salarié, sous l'autorité de son propre conseil, que préside un viticulteur élu ; le président de chaque cave siège au conseil de l'union.

**Organigramme simplifié (mars 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil de l'union | président du conseil, composé des présidents des neuf caves | M. Gilles ESCOURBIAC, viticulteur |
| Direction générale | directrice générale, qui porte le plan « ROCALDÈNE 2030 » | Mme Hélène MAZERANDE |
| Rattaché à la directrice générale | directeur commercial (vrac, grande distribution, export, service clients, projet de vente en ligne) | M. Damien SALVERNAC |
| Rattachée à la directrice générale | directrice de la production et de la qualité (assemblage et élevage des vins, laboratoire d'analyses, conditionnement et logistique) | Mme Claire BOUSQUIÉRAN |
| Rattaché à la directrice générale | directeur administratif et financier (comptabilité, contrôle de gestion, paie et ressources humaines, achats) | M. Philippe VERDAGNOL |
| Direction administrative et financière | responsable administratif et financier adjoint, rattaché à la directrice générale pour le projet de refonte du système d'information | vous |
| Rattaché au directeur administratif et financier | responsable du système d'information (équipe informatique de 6 personnes) | M. Sébastien CAUSSINEL |
| Caves | neuf caves coopératives, chacune avec son président et son directeur | — |

Le comité de direction de l'union réunit chaque mois la directrice générale et les trois directeurs qui lui sont rattachés. La directrice générale réunit chaque trimestre les neuf directeurs de cave.

### ANNEXE 1.2 – Le plan « ROCALDÈNE 2030 » et le système d'information actuel (note de Mme Hélène MAZERANDE, directrice générale, et témoignages recueillis en février 2027)

**A. Ce que la première priorité du plan demande à l'union**

- **Le climat change le calendrier** : les vendanges commencent environ dix jours plus tôt qu'il y a quinze ans, et les volumes varient davantage d'une année à l'autre. Les caves replanteront environ 400 hectares en cépages plus résistants à la chaleur d'ici 2030.
- **L'offre doit évoluer** : Mme Claire BOUSQUIÉRAN prépare des assemblages adaptés, dont trois cuvées moins riches en alcool à lancer en 2028. Pour les composer, elle doit savoir chaque semaine quels vins sont disponibles, dans quelles cuves et dans quelle cave.
- **Les marchés doivent se diversifier** : la part de l'export doit passer de 25 % à 35 % du chiffre d'affaires en 2030, surtout en Amérique du Nord et en Asie ; une vente en ligne aux particuliers doit ouvrir en 2028 et représenter environ 3 % du chiffre d'affaires en 2030. Les enseignes de la grande distribution exigent de leur côté des livraisons toujours plus fiables (annexe 1.3).

**B. L'état du système d'information**

- Le progiciel de gestion de l'union, installé en 2010 et très adapté par des développements spécifiques, ne sera plus maintenu par son éditeur après le 31 décembre 2028. Il ne gère ni plusieurs devises, ni plusieurs langues, ni la vente aux particuliers.
- Les neuf logiciels de cave ont été choisis par chaque cave entre 2012 et 2020 ; ils proviennent de quatre éditeurs, sous des versions différentes, et ne sont reliés ni entre eux ni au progiciel de l'union. Chaque cave code ses cuves et ses vins à sa manière.
- Une vingtaine de tableurs tiennent lieu d'outils de travail : disponibilités des vins, planning du conditionnement, documents d'export, fiches d'assemblage.
- Le portail des adhérents permet de consulter des actualités et des documents ; il n'offre aucun service aux caves elles-mêmes.
- Le budget du système d'information de 2026 (2 200 k€) se répartit en 1 800 k€ de fonctionnement courant (licences, maintenance, postes de travail, réseau, équipe informatique) et 400 k€ de projets.

**C. Les projets numériques de 2025 et 2026**

| Projet | Demandé par | Coût | Observation |
|---|---|---|---|
| Mises à jour imposées par les éditeurs | — | 240 k€ (sur le budget du SI) | aucun choix possible |
| Refonte du site internet vitrine | direction commerciale | 80 k€ (sur le budget du SI) | site plus moderne, sans vente en ligne ni lien avec le progiciel |
| Bornes tactiles de présentation des vins au caveau de vente de Pézenas | direction commerciale | 50 k€ (sur le budget du SI) | utilisées par les visiteurs l'été |
| Dématérialisation des notes de frais | direction administrative et financière | 30 k€ (sur le budget du SI) | 25 utilisateurs |
| Logiciel de gestion de la relation client pour l'export, en mode SaaS | direction commerciale | 25 k€ par an, payés sur le budget de la direction commerciale | souscrit en 2025 sans en informer l'équipe informatique ; non relié au progiciel |

Aucun de ces projets n'a été présenté au conseil ni rapproché des priorités du plan, adopté après leur lancement. Il n'existe ni liste commune des demandes, ni règle pour choisir entre elles.

**D. Témoignages**

- M. Damien SALVERNAC, directeur commercial : « L'informatique ne suit pas. Quand un importateur canadien me demande une date de livraison, je ne sais pas lui répondre avant deux ou trois jours : il faut savoir si le vin existe dans les caves, s'il faut le conditionner, quand la ligne sera libre. Mes fiches techniques sont faites à la main sous traitement de texte, en trois langues, et nos importateurs asiatiques en demandent davantage. Je ne sais pas non plus prévoir mes ventes par cuvée : nous assemblons sur la base des ventes de l'année précédente. J'ai pris un logiciel de gestion de la relation client moi-même, parce que j'attendais depuis trois ans. Et je veux la vente en ligne en 2028, pas en 2031. »
- M. Robert MALVEIRAC, président de la cave de LAURADEL et membre du conseil de l'union : « L'union décide sans nous. Nous avons choisi notre logiciel de cave en 2018, nos salariés le connaissent, il fonctionne. On nous annonce un logiciel commun sans nous avoir demandé ce dont nous avons besoin. Nos directeurs ressaisissent déjà tous les lundis la liste de leurs cuves pour l'union. Je veux bien partager nos informations, mais je veux savoir ce que l'union en fait et ce que deviennent nos vins. »
- M. Sébastien CAUSSINEL, responsable du système d'information : « On me demande tout en même temps. Mon équipe de six personnes passe l'essentiel de son temps à maintenir le progiciel, à dépanner les postes et à aider les caves, qui n'ont pas d'informaticien, surtout pendant les vendanges. Les demandes arrivent par courriel, directement des directeurs, chacun estimant la sienne prioritaire. Je ne participe pas au comité de direction : j'ai appris l'existence du logiciel d'export quand il a fallu le relier au progiciel. Je n'ai jamais pu présenter un plan pour le système d'information. »
- Mme Claire BOUSQUIÉRAN, directrice de la production et de la qualité : « Chaque lundi, mon assistante consolide neuf fichiers différents envoyés par les caves pour savoir quels vins sont disponibles. Le jeudi, ces informations sont déjà fausses. Pour les nouvelles cuvées, il me faudrait une vision à jour des vins de toutes les caves et des ventes attendues. »

### ANNEXE 1.3 – Le processus « commande → expédition » (description établie avec le service clients et le responsable du conditionnement, février 2027)

**A. Une commande d'une enseigne de la grande distribution**

1. *Réception* : la centrale d'achat de l'enseigne envoie sa commande par la plateforme d'échange de données informatisé utilisée avec les enseignes (80 % des commandes ; les autres arrivent par courriel). La plateforme n'est pas reliée au progiciel : le service clients imprime la commande et la ressaisit dans le progiciel.
2. *Disponibilité des vins* : le progiciel connaît le stock de bouteilles de l'entrepôt de Pézenas. S'il est insuffisant, le service clients interroge par courriel la production, qui consulte le tableur des disponibilités des vins des caves, mis à jour chaque lundi.
3. *Programmation du conditionnement* : le responsable du conditionnement inscrit le besoin dans le tableur du planning des trois lignes d'embouteillage, puis ressaisit l'ordre de conditionnement dans le progiciel. Le stock de matières sèches (bouteilles, bouchons, étiquettes, cartons) du progiciel est souvent faux : il arrive qu'une ligne s'arrête faute d'étiquettes.
4. *Préparation* : le progiciel imprime les bons de préparation ; les préparateurs notent à la main les quantités réellement préparées, que le service clients saisit le lendemain.
5. *Expédition* : le service clients réserve l'enlèvement sur le site internet de l'un des quatre transporteurs ; le progiciel envoie automatiquement à l'enseigne, par la plateforme d'échange, l'avis d'expédition.
6. *Facturation* : la facture est établie dans le progiciel après la saisie des quantités préparées et transmise automatiquement par la plateforme d'échange.

**B. Une commande export**

1. *Réception* : l'importateur envoie sa commande par courriel. L'assistante export l'enregistre dans le logiciel de gestion de la relation client de l'export, puis la ressaisit dans le progiciel.
2. *Disponibilité et conditionnement* : mêmes étapes que pour la grande distribution, avec souvent une étiquette propre au pays, commandée à l'imprimeur après confirmation de la commande.
3. *Documents* : l'assistante export établit sous tableur et traitement de texte les documents demandés par l'importateur et le transitaire (facture en devise et en anglais, liste de colisage, certificats d'analyse), en reprenant les informations du progiciel et du logiciel de gestion de la relation client.
4. *Expédition et facturation* : le transitaire organise le transport ; ses instructions sont saisies sur son portail. La facture du progiciel, en euros, sert à la comptabilité ; la facture en devise remise à l'importateur est celle du tableur.

**C. Cartographie applicative simplifiée du processus**

| Flux | De | Vers | Contenu | Mode |
|---|---|---|---|---|
| F1 | plateforme d'échange avec les enseignes | progiciel de l'union | commandes de la grande distribution | impression et ressaisie |
| F2 | messagerie | logiciel de gestion de la relation client de l'export | commandes export | ressaisie |
| F3 | logiciel de gestion de la relation client de l'export | progiciel de l'union | commandes export | ressaisie |
| F4 | logiciels des neuf caves | tableur des disponibilités des vins | vins disponibles par cuve | fichier envoyé par courriel chaque lundi, consolidé à la main |
| F5 | tableur des disponibilités et progiciel | tableur du planning du conditionnement | besoins à conditionner | ressaisie |
| F6 | tableur du planning du conditionnement | progiciel de l'union | ordres de conditionnement | ressaisie |
| F7 | progiciel de l'union | entrepôt, puis retour au progiciel | bons de préparation, quantités préparées | papier, saisie le lendemain |
| F8 | progiciel de l'union | sites des transporteurs et portail du transitaire | réservations et instructions de transport | ressaisie |
| F9 | progiciel et logiciel de gestion de la relation client | tableur des documents d'export | documents d'export | ressaisie |
| F10 | progiciel de l'union | plateforme d'échange avec les enseignes | avis d'expédition et factures | automatique (interface développée en 2015) |
| F11 | progiciel, gestion commerciale | progiciel, comptabilité | factures | automatique |

Deux flux sur onze sont automatisés. Aucun ne relie les logiciels des caves au progiciel de l'union.

**D. Quelques chiffres de 2026**

| Donnée | Grande distribution | Export |
|---|---|---|
| Clients | 12 enseignes | environ 60 importateurs dans 18 pays |
| Commandes reçues | environ 9 000 | environ 1 200 |
| Saisies successives d'une même commande | 2 | 4 |
| Commandes livrées complètes et à l'heure | 88 % (les enseignes exigent 98 %) | 80 % |
| Délai moyen entre la réception de la commande et l'expédition | 4 jours ouvrés (les enseignes en exigent 3) | 12 jours ouvrés |
| Réclamations | 540 (6 % des commandes), surtout des quantités ou des références erronées | 120 (10 % des commandes), surtout des documents erronés |
| Autres constats | 350 k€ de pénalités logistiques facturées par les enseignes pour livraisons incomplètes ou en retard | facture établie en moyenne 3 jours ouvrés après l'expédition |

### ANNEXE 1.4 – Le projet de refonte du système d'information (note de cadrage de M. Sébastien CAUSSINEL, responsable du système d'information, février 2027, complétée en mars 2027)

**A. Objet, périmètre et calendrier**

- *Objet* : remplacer le progiciel de l'union et les neuf logiciels de cave par un progiciel de gestion intégré spécialisé dans la filière vin, commun à l'union et aux caves : réception de la vendange et suivi des cuves dans les caves ; assemblage et élevage ; conditionnement ; commandes, logistique et facturation ; comptabilité ; portail des adhérents. Il devra être relié à la plateforme d'échange avec les enseignes et à la future boutique en ligne.
- *Utilisateurs* : environ 220, dont 130 à l'union et 90 dans les caves, auxquels s'ajoutent les saisonniers des caves pendant les vendanges.
- *Calendrier* : consultation des éditeurs et des intégrateurs de mars à mai 2027, choix en juin 2027. Le progiciel de l'union n'est plus maintenu après le 31 décembre 2028 ; les éditeurs des logiciels de cave en assurent la maintenance au moins jusqu'en 2030.
- *Contrainte* : aucune mise en service n'est possible d'août à novembre (vendanges, vinifications, pic des commandes de fin d'année). Les directeurs et le personnel des caves sont indisponibles de mi-août à fin octobre.

**B. Deux méthodes envisagées**

- *Méthode 1 – cycle en V et bascule unique* (proposée par l'intégrateur pour une offre au forfait) : rédaction des spécifications complètes de juin à octobre 2027, réalisation et paramétrage, recette, puis mise en service simultanée à l'union et dans les neuf caves en mars 2028.
- *Méthode 2 – méthode agile* (souhaitée par M. SALVERNAC) : itérations de trois semaines à partir de juillet 2027 ; chaque fonction est mise en service à l'union et dans les caves dès qu'elle est prête, y compris à l'automne.
- Remarque de M. CAUSSINEL : « Le module de réception de la vendange ne se juge vraiment qu'en vendanges. La comptabilité, les stocks et les codes communs des vins doivent être complets dès le premier jour. La boutique en ligne et le portail, eux, gagneront à être montrés aux utilisateurs au fur et à mesure. »

**C. Extrait du brouillon de cahier des charges (janvier 2027)**

- E1 – « Le logiciel doit être simple à utiliser. »
- E2 – « Le logiciel doit gérer les apports. »
- E3 – « Les commandes doivent être traitées rapidement. »
- E4 – « Le logiciel doit permettre l'export. »
- E5 – « Les caves doivent pouvoir voir leurs informations. »
- E6 – « Le logiciel doit être compatible avec la vente en ligne. »

Le brouillon a été rédigé par l'équipe informatique, sans entretien avec les caves ni avec le service clients. La version de mars 2027, envoyée aux candidats de la consultation, reprend ce brouillon sans changement.

**D. Un souvenir : la montée de version du progiciel de novembre 2022**

La recette a été conduite par l'équipe informatique seule, en deux jours, sur 30 commandes types, sans utilisateur du service clients ni de la comptabilité, sans critère d'acceptation écrit ni procès-verbal. La nouvelle version a été mise en service un lundi de novembre. Pendant trois semaines, les conditions tarifaires de deux enseignes ont été mal appliquées : 300 factures erronées ont dû être annulées par des avoirs et refaites, et la facturation a pris quatre semaines de retard.

**E. La proposition de VALTRÉMIS Intégration, intégrateur du progiciel envisagé (mars 2027)**

- *Option régie* : environ 2 000 jours de consultants, facturés 600 € par jour, soit environ 1 200 k€, facturés chaque mois au temps passé ; les consultants travaillent sous la direction de l'union. Lors du déploiement du portail des adhérents en 2021, réalisé en régie par un autre prestataire, les jours consommés avaient dépassé de 30 % l'estimation : au même rythme, la régie coûterait environ 1 560 k€.
- *Option forfait* : 1 500 k€, prix ferme pour le périmètre décrit dans le cahier des charges « dans sa version de mars 2027 » ; toute demande nouvelle donne lieu à un avenant facturé au tarif de la régie ; paiement de 40 % du prix à la signature et de 60 % à la mise en service.
- *Engagements proposés dans les deux options* : la recette est « réputée prononcée » dix jours après chaque livraison en l'absence de réserve écrite ; les anomalies sont corrigées gratuitement pendant trois mois après la mise en service ; le chef de projet de VALTRÉMIS « peut être remplacé selon les besoins de l'intégrateur » ; les développements spécifiques (interfaces avec la plateforme d'échange des enseignes et avec la boutique en ligne) restent la propriété de VALTRÉMIS et sont concédés en licence.
- *Ce que la proposition ne prévoit pas* : ni jalons datés ni pénalités de retard, ni transfert de compétences à l'équipe informatique, ni documentation des paramétrages, ni plafond de jours pour la régie.
- Les licences du progiciel font l'objet d'un contrat distinct avec son éditeur, qui n'est pas à traiter ici.

### Travail à faire

Le progiciel de gestion de l'union ne sera plus maintenu après 2028. Mme MAZERANDE veut que sa refonte serve le plan « ROCALDÈNE 2030 » et ne se réduise pas au remplacement d'un logiciel. Elle vous demande d'apprécier l'alignement actuel du système d'information sur le plan, d'analyser le processus « commande → expédition » et l'architecture qui le supporte, de proposer la gouvernance du programme de refonte, puis de préparer la méthode, le cahier des charges, le plan qualité et le contrat d'intégration du projet. Vous mobiliserez pour cela les annexes 1.1 à 1.4 ainsi que vos connaissances professionnelles.

**1.1 – Alignement du système d'information sur le plan « ROCALDÈNE 2030 » (4 points)**

a) Après avoir défini l'alignement stratégique et présenté le modèle d'alignement stratégique de Henderson et Venkatraman, appréciez l'alignement actuel du système d'information de l'union sur la première priorité du plan : vous identifierez trois désalignements, en les situant sur les axes du modèle et en les appuyant sur les annexes 1.2 et 1.3, puis vous montrerez pourquoi le seul remplacement du progiciel ne suffirait pas à rétablir l'alignement.

b) Proposez trois orientations de la stratégie du système d'information de l'union, chacune justifiée par un enjeu du plan ; l'une d'elles au moins intégrera une technologie émergente adaptée au cas, dont vous préciserez l'apport et une limite.

**1.2 – Le processus « commande → expédition » et l'urbanisation du système d'information (3 points)**

a) À partir de l'annexe 1.3, identifiez trois dysfonctionnements du processus « commande → expédition », en précisant pour chacun ses effets chiffrés et sa cause dans l'architecture actuelle, puis portez une appréciation d'ensemble sur cette architecture.

b) Après avoir défini l'urbanisation du système d'information, proposez, sous la forme d'un schéma ou d'un tableau, une architecture cible urbanisée qui rationalise ce processus (zones, référentiels, échanges).

c) Présentez les impacts organisationnels de cette cible sur trois métiers : le service clients, le conditionnement et la logistique, les caves.

**1.3 – Gouvernance du programme de refonte (3 points)**

a) Après avoir défini la gouvernance du système d'information, proposez la gouvernance du programme de refonte : le rôle de chaque partie prenante (conseil de l'union, directrice générale, directions de l'union, responsable du système d'information, caves, adhérents), trois instances (composition, fréquence, rôle) et quatre critères d'arbitrage entre les demandes.

b) Analysez trois tensions entre le système d'information, la direction générale, les directions de l'union et les caves, révélées par l'annexe 1.2, puis proposez trois leviers pour les dépasser.

**1.4 – Méthode, cahier des charges et plan qualité du projet (2,5 points)**

a) Comparez les deux méthodes envisagées dans l'annexe 1.4 B au regard de la contrainte des vendanges et de la disponibilité des caves, puis recommandez, en la justifiant, la méthode de conduite du projet. Aucun planning détaillé n'est attendu.

b) Réécrivez trois exigences du brouillon de cahier des charges (annexe 1.4 C) pour les rendre vérifiables, puis indiquez la structure attendue du cahier des charges fonctionnel du projet.

c) En tirant les enseignements de la montée de version de 2022, proposez quatre éléments clés du plan qualité du projet portant sur la recette, les critères d'acceptation et les revues.

**1.5 – Contrat d'intégration avec VALTRÉMIS Intégration (1,5 point)**

a) Recommandez, en la justifiant par les données de l'annexe 1.4 E et par la méthode retenue, la forme du contrat d'intégration.

b) Proposez trois clauses à négocier avec VALTRÉMIS Intégration, en reliant chacune à un risque du projet.
