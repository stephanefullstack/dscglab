# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 6

**DOSSIER 3 – CONDUIRE LE PROJET DE PLATEFORME PÉDAGOGIQUE ET PILOTER LES COÛTS DU SI (11 points)**

Durée conseillée : 50 min (11 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 2, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en avril 2027. L'Institut LORVANNE est une école de management privée, constituée en association régie par la loi du 1er juillet 1901 et créée en 1987 à Dijon. Elle forme 4 900 étudiants, dont 1 450 apprentis, dans un bachelor, un programme grande école, six mastères spécialisés et des formations courtes destinées aux cadres en activité. Elle est implantée sur trois campus : Dijon, siège de l'association (2 900 étudiants), Besançon (1 400 étudiants) et Chalon-sur-Saône, ouvert en 2023 (600 étudiants). Elle emploie 610 salariés, dont 140 enseignants-chercheurs, et fait appel chaque année à quelque 450 intervenants vacataires. Ses produits de l'exercice 2025-2026, clos le 31 août 2026, s'élèvent à 68 millions d'euros, dont 2,9 millions d'euros consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

En juin 2026, le conseil d'administration, présidé par M. Didier LAMBRESC, a adopté le plan stratégique « LORVANNE 2030 », porté par la directrice générale, Mme Agnès FERRIOL : doubler le chiffre d'affaires de la formation des cadres grâce à une offre en ligne, développer l'apprentissage et les partenariats internationaux, améliorer l'expérience des étudiants et des entreprises partenaires. Le système d'information ne suit pas : chaque campus a gardé sa propre équipe informatique et une partie de ses applications, l'école n'a plus de directeur des systèmes d'information depuis le départ du précédent titulaire en 2025, et un rançongiciel a paralysé le campus de Besançon pendant neuf jours en novembre 2026. La plateforme pédagogique en ligne, hébergée sur les serveurs de l'école depuis 2014, arrive par ailleurs en fin de vie.

Consultant(e) dans un cabinet de conseil en management des systèmes d'information, vous êtes missionné(e) par Mme FERRIOL sur trois axes : aligner la stratégie du système d'information sur le plan « LORVANNE 2030 » et refonder la gouvernance de la fonction informatique (dossier 1) ; auditer la sécurité du système d'information après l'incident de Besançon et fonder une politique de sécurité (dossier 2) ; conduire le projet de nouvelle plateforme pédagogique et en piloter les coûts (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de l'Institut LORVANNE et chiffres clés

L'Institut LORVANNE est une association régie par la loi du 1er juillet 1901, créée en 1987 à Dijon. École de management privée, il est financé par les frais de scolarité, par le financement de l'apprentissage et par la formation des cadres. Son exercice court du 1er septembre au 31 août.

**Chiffres clés de l'exercice 2025-2026 (clos le 31 août 2026)**

| Donnée | Valeur |
|---|---|
| Étudiants | 4 900, dont 1 450 apprentis |
| Répartition par campus | Dijon, siège de l'association : 2 900 ; Besançon : 1 400 ; Chalon-sur-Saône (ouvert en 2023) : 600 |
| Formations | un bachelor, un programme grande école, six mastères spécialisés, des formations courtes destinées aux cadres en activité |
| Salariés | 610, dont 140 enseignants-chercheurs |
| Intervenants vacataires | environ 450 par an |
| Produits de l'exercice | 68 M€ |
| Budget du système d'information | 2,9 M€ (environ 4 % des produits) |
| Fonction informatique | 21 personnes : 6 au siège, 15 rattachées aux directeurs de campus |

**Organigramme simplifié de la direction et de la fonction informatique (avril 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil d'administration | président | M. Didier LAMBRESC |
| Direction générale | directrice générale, qui porte le plan « LORVANNE 2030 » | Mme Agnès FERRIOL |
| Comité de direction | directrice des programmes (bachelor, programme grande école, mastères spécialisés, formation des cadres) | Mme Laure ROUVIÈRE |
| Comité de direction | directeur administratif et financier | M. Antoine DELORMEAU |
| Comité de direction | directeur du campus de Dijon | M. Rémi VERCLOS |
| Comité de direction | directrice du campus de Besançon | Mme Hélène MARCOIRE |
| Comité de direction | directeur du campus de Chalon-sur-Saône | M. Karim SADOUNI |
| Fonction informatique du siège (6 personnes : applications de gestion, plateforme pédagogique) | responsable informatique du siège ; il assure l'intérim de la direction des systèmes d'information depuis le départ du précédent directeur en 2025, sans autorité sur les équipes informatiques des campus | M. Fabien CORNAVIN |
| Fonction informatique des campus (15 personnes : support des utilisateurs et infrastructures locales) | équipes rattachées aux directeurs de campus | — |

### ANNEXE 3.1 – Projet de nouvelle plateforme pédagogique

**A. Situation actuelle et calendrier**
- La plateforme pédagogique en ligne a été installée en 2014 sur deux serveurs du siège. C'est une solution libre, dont la version installée n'est plus mise à jour par la communauté qui la développe depuis 2025 ; les serveurs, achetés en 2019, ne sont plus couverts par la garantie du constructeur. Elle compte 2 500 espaces de cours actifs, utilisés par les 4 900 étudiants, les 140 enseignants-chercheurs, les quelque 450 vacataires et les cadres en formation, soit environ 6 000 utilisateurs.
- Les comptes des étudiants sont créés chaque semaine à partir d'un fichier extrait du progiciel de scolarité ; les notes des examens passés en ligne sont ressaisies dans le progiciel par les services de scolarité.
- Le plan « LORVANNE 2030 » prévoit de porter le chiffre d'affaires de la formation des cadres en ligne de 0,3 M€ en 2025-2026 à 5 M€ en 2029-2030.
- Calendrier fixé par Mme FERRIOL : choix de la solution par le conseil d'administration en juin 2027, signature du contrat en septembre 2027, mise en service pour tous les programmes à la rentrée de septembre 2028. La date de la rentrée ne peut pas être déplacée.

**B. Besoins exprimés lors des entretiens (mars 2027)**
- Formation des cadres : parcours en ligne alternant modules à distance et classes virtuelles ; espace réservé à chaque entreprise cliente, où ses responsables des ressources humaines suivent l'assiduité et les résultats de leurs cadres ; attestation de fin de parcours. La directrice des programmes souhaite vendre un premier parcours entièrement en ligne dès janvier 2028.
- Examens surveillés à distance, pour les cadres et pour les étudiants en mobilité à l'étranger : l'étudiant est filmé et enregistré par la caméra et le micro de son ordinateur pendant l'épreuve ; un surveillant de l'école visionne les enregistrements signalés. Jusqu'à 600 étudiants composent en même temps lors des sessions d'examens.
- Accessibilité : 160 étudiants bénéficient en 2025-2026 d'un aménagement de leurs études au titre d'un handicap ; la plateforme doit être utilisable au clavier seul et avec un lecteur d'écran, et appliquer automatiquement le temps majoré accordé aux examens.
- Intégration avec la scolarité : création et suppression automatiques des comptes à partir des inscriptions enregistrées dans le progiciel de scolarité, inscription automatique de chaque étudiant aux cours de son programme, transfert des notes des examens en ligne vers le progiciel.
- Usage sur téléphone mobile pour la consultation des cours et des annonces.

**C. Les deux options étudiées (offres reçues en mars 2027 ; montants hors taxes en milliers d'euros, sur trois années d'utilisation, de septembre 2028 à août 2031, mise en place comprise)**

| Poste de coût | Option A – plateforme en mode SaaS de l'éditeur Quorvel Learning | Option B – solution libre hébergée et maintenue par ARDÉVAL |
|---|---|---|
| Abonnement (A) ou licence (B) | 300 (100 par an pour 6 000 utilisateurs) | 0 (licence libre, sans redevance) |
| Hébergement et exploitation | compris dans l'abonnement | 150 (50 par an) |
| Intégration avec le progiciel de scolarité et paramétrage | 40 | 120 |
| Surveillance des examens à distance | 60 (module optionnel, 20 par an) | 30 (adaptation d'une extension libre, une fois) |
| Formation des utilisateurs | 20 | 30 |
| Maintenance et assistance | comprises dans l'abonnement | 150 (50 par an, dont les montées de version) |
| **Total de l'offre** | **420** | **480** |

| Caractéristique | Option A | Option B |
|---|---|---|
| Fournisseur | éditeur de droit américain, dont le siège est aux États-Unis ; il déclare adhérer au cadre de protection des données UE-États-Unis | hébergeur et intégrateur français, qui exploite deux centres de données situés en France ; son offre n'est pas qualifiée SecNumCloud |
| Localisation des données | centres de données de l'éditeur aux États-Unis ; hébergement en Irlande proposé en option, pour 10 k€ par an de plus | France |
| Délai de mise en service après la signature | 4 mois | 8 mois, dont un pilote possible sur un parcours de la formation des cadres à partir de février 2028 |
| Fonctions | toutes les fonctions demandées sont disponibles en standard, application mobile comprise ; l'éditeur décide seul de ses évolutions, publiées trois fois par an | même famille logicielle que la plateforme actuelle ; l'espace des entreprises clientes et le transfert des notes sont à développer par ARDÉVAL ; application mobile de la communauté |
| Fin du contrat | export des notes et des journaux d'activité au format tableur pendant 30 jours ; cours exportables dans le format propre de l'éditeur ; assistance à la migration facturée en sus | contenus et données dans des formats ouverts ; restitution de toutes les données et des sauvegardes sous 30 jours, avec assistance au transfert comprise dans l'offre |

**D. Témoignages (recueillis en mars 2027)**

**Mme Laure ROUVIÈRE, directrice des programmes** : « Il me faut un premier parcours vendable en janvier 2028, avant même la rentrée. Pour le reste de l'offre aux entreprises, nous découvrirons les besoins avec nos premiers clients. Et la plateforme de nos concurrents fonctionne sur téléphone : pas la nôtre. »

**M. Julien TERVILLAC, enseignant-chercheur, référent du numérique pédagogique** : « Avec l'option A, chaque espace de cours sera à reconstruire à la main : comptez deux heures par espace, soit 5 000 heures pour les 2 500 espaces actifs, et l'éditeur facture 60 k€ la reprise automatique de ce qui peut l'être. Avec l'option B, l'essentiel se reprend tout seul : une demi-heure par espace pour vérifier, soit 1 250 heures, et ARDÉVAL demande 20 k€. Les enseignants ne sont disponibles ni pendant les examens ni en été. En janvier, la plateforme a encore lâché pendant une épreuve en ligne. »

**Mme Inès FAVRIGNY, référente handicap** : « Nos étudiants malvoyants ne peuvent pas utiliser la plateforme actuelle avec leur lecteur d'écran. Je veux pouvoir le vérifier moi-même avec eux avant la mise en service, pas sur une simple déclaration du fournisseur. »

**M. Antoine DELORMEAU, directeur administratif et financier** : « Aucune offre ne comprend la reprise des contenus ni le maintien de l'ancienne plateforme, qui devra rester ouverte pour les rattrapages et la consultation des archives : 40 k€ pour toute l'année 2028-2029 avec l'option A, 20 k€ pour le premier semestre avec l'option B. J'ai valorisé l'heure d'enseignant à 40 €, soit 200 k€ pour l'option A et 50 k€ pour l'option B, et un poste à temps plein de l'équipe du siège à 60 k€ par an. Les directeurs de campus me demandent déjà combien la plateforme coûtera à chacun. »

**M. Fabien CORNAVIN, responsable informatique du siège** : « Avec l'option A, l'éditeur fait presque tout : il nous restera l'administration des comptes et le lien avec la scolarité, soit un demi-poste. Avec l'option B, il faudra en plus piloter ARDÉVAL, valider chaque montée de version et chaque extension : un poste à temps plein. L'équipe du siège n'a jamais conduit un projet de cette taille, et je dois continuer à faire tourner l'existant. »

### ANNEXE 3.2 – Extrait du tableau de bord actuel de l'informatique et budget du SI

**A. Tableau de bord de l'informatique (premier trimestre 2027)**, établi chaque mois par l'informatique du siège et adressé au seul directeur administratif et financier

| Indicateur | Janvier 2027 | Février 2027 | Mars 2027 |
|---|---|---|---|
| Tickets ouverts auprès de l'informatique du siège | 420 | 390 | 360 |
| Tickets clos par l'informatique du siège | 400 | 380 | 370 |
| Taux de disponibilité de la plateforme pédagogique (mesuré 24 h sur 24, 7 jours sur 7) | 98,6 % | 99,1 % | 99,4 % |
| Taux de disponibilité de la messagerie | 99,9 % | 99,9 % | 99,8 % |
| Postes de travail en service (tous campus) | 1 400 | 1 400 | 1 400 |
| Serveurs en service | 48 | 48 | 48 |
| Volume de stockage occupé | 58 To | 60 To | 61 To |

Notes : les équipes informatiques des campus suivent les demandes de leurs utilisateurs par courriel ou dans leurs propres outils ; ces demandes ne figurent pas dans le tableau de bord. Aucune cible n'est fixée. En janvier 2027, la plateforme pédagogique a été indisponible une dizaine d'heures, dont la moitié pendant la session d'examens en ligne du premier semestre.

**B. Budget du système d'information de l'exercice 2025-2026**

| Nature de dépense | Montant |
|---|---|
| Personnel informatique (21 personnes) | 1,2 M€ |
| Licences et abonnements | 0,6 M€ |
| Matériel (postes de travail, serveurs, équipements des salles de cours) | 0,5 M€ |
| Maintenance et prestations externes | 0,4 M€ |
| Réseaux et télécommunications | 0,2 M€ |
| **Total** | **2,9 M€**, dont 2,5 M€ pour le fonctionnement de l'existant et 0,4 M€ pour des projets nouveaux |

| Entité | Budget du SI | Étudiants | Postes de travail en service |
|---|---|---|---|
| Siège (applications de gestion communes, plateforme pédagogique, site internet, liaisons entre les campus) | 1,7 M€ | — | comptés avec le campus de Dijon |
| Campus de Dijon | 0,6 M€ | 2 900 | 800 |
| Campus de Besançon | 0,4 M€ | 1 400 | 400 |
| Campus de Chalon-sur-Saône | 0,2 M€ | 600 | 200 |

Les dépenses informatiques des campus sont enregistrées dans leurs budgets de fonctionnement et ne sont consolidées qu'à la clôture de l'exercice. Les dépenses du siège, qui servent les trois campus, ne sont ni réparties entre eux ni refacturées ; aucune n'est rattachée à une application ou à un service.

**C. Consommation électrique des salles informatiques (exercice 2025-2026)**

| Salle | Consommation |
|---|---|
| Siège, dont 20 MWh pour les deux serveurs de la plateforme pédagogique | 110 MWh |
| Campus de Dijon | 40 MWh |
| Campus de Besançon | 30 MWh |
| Campus de Chalon-sur-Saône | 20 MWh |
| **Total** | **200 MWh** |

Aucune autre donnée environnementale n'est suivie. Ni Quorvel Learning ni ARDÉVAL ne mentionnent d'indicateur environnemental dans leur offre.

### ANNEXE 3.3 – Repères réglementaires et référentiels (au 31/12/2026)

| Texte ou référentiel | Objet | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 (RGPD) | Protection des données personnelles. Un transfert de données personnelles vers un pays situé hors de l'Union européenne n'est permis que si la Commission européenne a reconnu à ce pays un niveau de protection adéquat ou si des garanties appropriées sont prévues, par exemple des clauses contractuelles types. Le prestataire qui traite des données pour le compte de l'école (sous-traitant) agit sur ses instructions, dans le cadre d'un contrat écrit (article 28). Une analyse d'impact est réalisée avant tout traitement susceptible d'engendrer un risque élevé pour les personnes. | Applicable depuis le 25/05/2018 |
| Décision d'adéquation de la Commission européenne pour les États-Unis (cadre de protection des données UE-États-Unis) | Permet les transferts de données personnelles vers les organisations américaines qui adhèrent à ce cadre. Elle a été adoptée après l'invalidation du cadre précédent par la Cour de justice de l'Union européenne (arrêt du 16/07/2020). | En vigueur depuis le 10/07/2023 |
| Règlement (UE) 2023/2854 (« Data Act ») | Accès aux données et changement de fournisseur de services d'informatique en nuage (portabilité des données, assistance à la sortie). | Applicable depuis le 12/09/2025 |
| SecNumCloud (ANSSI, version 3.2) | Référentiel d'exigences permettant de qualifier des offres de services d'informatique en nuage, y compris des critères de protection contre l'application de lois extra-européennes. | En vigueur depuis le 08/03/2022 |
| Référentiel du cloud de confiance du Cigref | Grille d'exigences fondée sur trois piliers : sécurité, immunité aux lois extra-européennes, maîtrise de la dépendance au fournisseur ; ni label ni certification. | V1 publiée le 27/05/2021 ; une V2 est disponible |

### Travail à faire

Mme FERRIOL vous confie la conduite du projet de nouvelle plateforme pédagogique, qui doit être en service à la rentrée de septembre 2028, ainsi que la refonte du pilotage des coûts du système d'information. Le conseil d'administration choisira la solution en juin 2027. Vous mobiliserez pour cela les annexes 1.1, 3.1, 3.2 et 3.3 ainsi que vos connaissances professionnelles.

**3.1 – Méthode de conduite du projet et cahier des charges (3 points)**

a) Comparez le cycle en V, les méthodes agiles et l'approche hybride, puis recommandez la méthode à retenir pour le projet de nouvelle plateforme pédagogique, en la justifiant par trois contraintes du projet tirées de l'annexe 3.1.

b) Présentez le contenu du cahier des charges fonctionnel et technique du projet, en illustrant chacune de ces deux parties par deux exigences tirées des besoins exprimés.

**3.2 – Coût complet des deux options et souveraineté des données (3 points)**

a) Après avoir défini le coût total de possession (TCO), comparez les deux options sur trois ans, d'abord à partir des seules offres, puis en intégrant les coûts cachés signalés dans les témoignages de l'annexe 3.1.

b) Discutez de façon qualitative le retour sur investissement du projet, en identifiant deux gains attendus et les conditions de leur réalisation.

c) Analysez les deux options au regard des enjeux de l'informatique en nuage et de la souveraineté numérique (localisation des données, droit applicable au fournisseur, réversibilité), puis recommandez une option au conseil d'administration.

**3.3 – Plan qualité du projet (1,5 point)**

Proposez les éléments du plan qualité du projet : la répartition des responsabilités, la recette assortie de trois critères d'acceptation, et un indicateur de qualité, en précisant sa formule, sa source, sa fréquence, sa cible et son axe du tableau de bord prospectif.

**3.4 – Pilotage des coûts et tableau de bord du SI (3,5 points)**

a) Après avoir présenté les fondamentaux du contrôle de gestion appliqué au système d'information, critiquez en trois points le tableau de bord actuel de l'informatique (annexe 3.2), puis proposez une méthode de répartition des coûts du SI entre les campus, en précisant ses inducteurs.

b) Proposez la structure d'un tableau de bord du SI destiné au comité de direction, équilibré entre performance, risques et coûts et intégrant la dimension ESG, avec cinq indicateurs dont au moins un pour chacune de ces quatre dimensions. Pour chaque indicateur, précisez la formule, la source, la fréquence, la cible et l'axe.
