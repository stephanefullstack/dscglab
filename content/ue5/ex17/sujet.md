# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 17

**DOSSIER 2 – EXPLOITER LES DONNÉES DES CLIENTS AU SERVICE DU CONSEIL (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 6, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mai 2027. CORLANDEAU Expertise est une société par actions simplifiée d'expertise comptable, détenue par ses quatorze associés experts-comptables. Son siège est à Poitiers et elle compte cinq autres bureaux, à Niort, La Rochelle, Angoulême, Saintes et Châtellerault. Elle emploie 180 salariés et accompagne environ 3 000 clients, surtout des TPE et des PME, mais aussi des associations et des professions libérales : tenue et révision de la comptabilité, comptes annuels, déclarations fiscales, paie et conseil aux dirigeants. Son chiffre d'affaires de l'exercice 2026 s'élève à 22 millions d'euros ; 1,1 million d'euros est consacré au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « CORLANDEAU 2030 », adopté par les associés en décembre 2026, fixe trois priorités : sécuriser l'organisation de travail hybride, puisque la moitié des collaborateurs travaillent à distance deux jours par semaine et que les échanges avec les clients sont presque tous dématérialisés ; tirer parti des données que les clients confient au cabinet pour développer une offre de conseil, alors que les honoraires de tenue comptable baissent sous l'effet de l'automatisation ; capitaliser la connaissance technique du cabinet, aujourd'hui dispersée entre les bureaux et concentrée chez quelques associés. La présidente, Mme Hélène VARENNAT, en rend compte chaque trimestre au comité des associés.

Vous avez rejoint CORLANDEAU Expertise en janvier 2027 comme chargé(e) de mission « systèmes d'information et transformation numérique », rattaché(e) à Mme VARENNAT. Elle vous confie trois travaux : sécuriser le système d'information d'un cabinet qui travaille à distance (dossier 1) ; exploiter les données des clients au service du conseil (dossier 2) ; évaluer le pilote de la base de connaissances du cabinet et en conduire la généralisation (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de CORLANDEAU Expertise et chiffres clés

CORLANDEAU Expertise est une société par actions simplifiée d'expertise comptable, détenue par ses quatorze associés experts-comptables. Elle accompagne environ 3 000 clients, surtout des TPE et des PME, mais aussi des associations et des professions libérales, depuis son siège de Poitiers et cinq autres bureaux, à Niort, La Rochelle, Angoulême, Saintes et Châtellerault. Son exercice coïncide avec l'année civile. Son activité connaît une forte période de janvier à mai, qui réunit les clôtures des comptes au 31 décembre et les déclarations fiscales. Les experts-comptables sont tenus au secret professionnel, qui s'étend aux informations que les clients confient au cabinet.

**Chiffres clés de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Activité | tenue et révision de la comptabilité, comptes annuels, déclarations fiscales, paie, conseil aux dirigeants |
| Clients | environ 3 000 : TPE et PME surtout, associations, professions libérales |
| Chiffre d'affaires | 22 M€ |
| Effectif | 180 salariés, dont les 14 associés experts-comptables |
| Organisation du travail | la moitié des collaborateurs travaillent à distance deux jours par semaine ; les échanges avec les clients sont presque tous dématérialisés |
| Budget du système d'information | 1,1 M€ (5 % du chiffre d'affaires) |
| Plan « CORLANDEAU 2030 » (adopté en décembre 2026) | sécuriser l'organisation de travail hybride ; tirer parti des données des clients pour développer une offre de conseil ; capitaliser la connaissance technique du cabinet |

**Répartition des salariés entre les bureaux (décembre 2026)**

| Bureau | Salariés |
|---|---|
| Poitiers (siège) | 60 |
| Niort | 30 |
| La Rochelle | 30 |
| Angoulême | 25 |
| Saintes | 20 |
| Châtellerault | 15 |
| **Total** | **180** |

**Organigramme simplifié (mai 2027)**

| Niveau | Fonction | Rôle |
|---|---|---|
| Direction | présidente, Mme Hélène VARENNAT | dirige le cabinet, met en œuvre le plan « CORLANDEAU 2030 » et en rend compte chaque trimestre au comité des associés |
| Direction | comité des associés (les 14 associés) | adopte les orientations et le budget, arbitre les décisions qui engagent le cabinet |
| Production | six bureaux, chacun dirigé par un associé responsable de bureau | chefs de mission et collaborateurs comptables : tenue, révision, comptes annuels, déclarations fiscales, conseil aux clients du bureau |
| Expertise | pôle technique, au siège, animé par un associé | veille juridique, fiscale et comptable, réponse aux questions techniques des bureaux |
| Expertise | pôle social, au siège, animé par un associé | paie et déclarations sociales des clients, conseil en droit social |
| Fonctions support | rattachées à la présidente | administration et finances, ressources humaines, informatique |

### ANNEXE 2.1 – La collecte des données des clients aujourd'hui

*Note de M. Bastien ORTELIER, chef de mission au bureau de Niort, à Mme VARENNAT (février 2027)*

**A. Les pièces reçues en 2026, par canal**

| Canal | Pièces reçues (milliers) | Part intégrée automatiquement dans le dossier, sans ressaisie | Délai moyen entre la date de la pièce et son intégration dans le dossier | Clients dont c'est le canal principal | Part de ces clients dont le dossier était incomplet à la clôture 2026 |
|---|---|---|---|---|---|
| Portail d'échange (dépôt de fichiers par le client) | 250 | 60 % | 10 jours | 1 500 | 20 % |
| Application mobile (photographie de la pièce) | 100 | 40 % | 10 jours | 450 | 20 % |
| Courriel adressé au collaborateur | 150 | 20 % | 20 jours | 600 | 40 % |
| Papier (dépôt au bureau ou envoi postal) | 100 | 0 % | 45 jours | 450 | 60 % |
| **Ensemble** | **600** | **220 000 pièces, un peu plus d'une sur trois** | — | **3 000** | **30 %** |

**B. Ce qui se passe ensuite**

1. **Relevés bancaires.** Pour 1 200 clients (40 %), les relevés arrivent chaque jour par un flux automatisé que propose l'éditeur du logiciel de production comptable ; chaque client doit l'autoriser auprès de sa banque. Pour les 1 800 autres, les relevés arrivent en PDF ou sur papier, chaque mois, chaque trimestre ou à la clôture, et les opérations sont rapprochées des pièces à la main.
2. **Lecture automatique des pièces.** Le logiciel lit la date, le montant, la TVA et le fournisseur des pièces déposées sur le portail ou photographiées, et de celles que les collaborateurs y déposent depuis leur messagerie. Une pièce lue sur dix comporte une erreur sur l'un de ces champs, corrigée par le collaborateur, souvent à la révision, plusieurs semaines plus tard.
3. **Formats.** Photographies floues ou coupées, fichiers PDF qui regroupent plusieurs factures, relevés de ventes extraits des logiciels de caisse ou de facturation des clients, chacun dans son format. Depuis septembre 2026, une partie des factures d'achat parviennent aux clients sous forme électronique structurée ; ils nous les transmettent pourtant en PDF ou imprimées, et le logiciel doit les relire comme des images.
4. **Nommage et rattachement.** Les fichiers arrivent sous des noms comme « scan_0012.pdf » ou « facture.pdf » ; chaque collaborateur les renomme et les classe à sa façon. Un même fournisseur est parfois enregistré sous plusieurs libellés dans le dossier d'un client (« Garage Belmontier », « GARAGE BELMONTIER SARL »), ce qui fausse les soldes par fournisseur.
5. **Doublons.** Environ 5 % des pièces nous parviennent deux fois, par exemple par courriel puis sur le portail, soit 30 000 pièces par an à repérer.
6. **Pièces manquantes.** À la clôture 2026, il manquait des pièces dans 30 % des dossiers (tableau A). Chaque collaborateur relance ses clients par courriel, sans liste commune des pièces attendues ni suivi des relances.
7. **Restitution.** Les comptes annuels sont remis en moyenne 98 jours après la clôture. Une situation en cours d'année n'est produite que pour 10 % des clients, à la main, dans un tableur.
8. **Organisation.** Chaque bureau organise la collecte à sa façon : depuis 2025, le bureau de Poitiers exige le portail de tout nouveau client ; ceux de Saintes et de Châtellerault acceptent les dépôts de papier sans limite.

**C. Ce que propose l'éditeur du logiciel de production comptable**

L'éditeur propose, dans l'abonnement actuel, des connexions par API à la plupart des banques et à une vingtaine de logiciels de caisse et de facturation du marché, ainsi que la récupération des factures électroniques reçues par les clients, dans leur format structuré, avec leur accord. Aucune de ces connexions n'est activée aujourd'hui, à l'exception des flux bancaires des 1 200 clients cités plus haut.

### ANNEXE 2.2 – Le projet d'offre « Pilotage dirigeant »

**A. L'offre envisagée (note de M. Laurent CHAMPEYRAC, associé chargé du conseil aux dirigeants, mars 2027)**

L'offre comprendrait trois services, proposés sur abonnement aux clients volontaires à partir de septembre 2027 :
1. **un tableau de bord mensuel** : trésorerie, marge brute, délais de paiement des clients et des fournisseurs, comparés au mois précédent et au même mois de l'année précédente ;
2. **un entretien trimestriel** avec le chef de mission, pour comprendre les écarts : pourquoi la marge baisse (par activité, par client, selon la saison), pourquoi la trésorerie se tend ;
3. **un outil d'alerte** qui estime, pour chaque client, le risque qu'il connaisse une difficulté de trésorerie dans les douze mois.

**B. L'outil d'alerte**

Mme Léa MONTÉGRIER, analyste de données recrutée par le cabinet en 2026, en a construit un prototype. Il classe chaque client en trois niveaux de risque (faible, moyen, élevé), à partir des données que le client confie au cabinet : retards de paiement de ses propres clients, niveau et évolution de sa trésorerie, retards de dépôt de ses déclarations fiscales et sociales, secteur d'activité. Le modèle a été établi par apprentissage automatique sur l'historique 2022-2024 des clients des bureaux de Poitiers et de Niort. Une alerte est émise au niveau élevé. L'écran affiche le niveau, sans les éléments qui l'ont déterminé.

**C. Résultats d'un premier essai (janvier 2027)**

Le prototype a été appliqué aux données arrêtées au 31/12/2025 de 400 clients des bureaux de Poitiers et de Niort ; ses alertes ont ensuite été comparées à ce qui s'est réellement passé en 2026. Une difficulté de trésorerie s'entend ici d'un découvert non autorisé de plus de trois mois, d'un incident de paiement d'une échéance fiscale ou sociale ou d'un échéancier demandé à un créancier.

| | Difficulté de trésorerie en 2026 | Pas de difficulté en 2026 | Total |
|---|---|---|---|
| Alerte émise | 30 | 70 | 100 |
| Pas d'alerte | 10 | 290 | 300 |
| **Total** | **40** | **360** | **400** |

Observations de l'analyste de données :
- 35 des 70 alertes sans difficulté concernent des entreprises de la restauration et du bâtiment, qui ne représentent que 80 clients de l'échantillon ;
- 8 des 10 difficultés non détectées concernent des clients dont les relevés bancaires n'arrivent pas par flux automatisé et dont les pièces arrivent par trimestre ou à la clôture ;
- un retard de dépôt d'une déclaration fait monter le niveau de risque, même lorsqu'il vient de pièces que le cabinet attendait encore.

**D. Avis recueillis**

**M. Laurent CHAMPEYRAC, associé chargé du conseil aux dirigeants** : « Trois difficultés sur quatre repérées à l'avance : c'est un argument décisif face aux plateformes en ligne. Ouvrons l'outil à tous les clients dès septembre, avec une alerte envoyée automatiquement au dirigeant. »

**Mme Léa MONTÉGRIER, analyste de données** : « Le prototype repose sur deux bureaux et trois années d'historique, et il ne voit bien que les clients dont les données sont fraîches. Il indique quels clients ressemblent à ceux qui ont connu des difficultés, pas pourquoi ils en connaîtraient. Je suis seule pour tout le cabinet, et personne n'a décidé qui vérifie une alerte avant qu'elle parte. »

**M. Bastien ORTELIER, chef de mission, bureau de Niort** : « Dans mes dossiers, l'outil a signalé un restaurant en pleine forme et ignoré une entreprise de maçonnerie que je savais fragile, dont les pièces n'arrivent qu'à la clôture. Je ne peux pas appeler un dirigeant pour lui dire qu'un logiciel le juge en danger sans pouvoir lui expliquer pourquoi. Et un tableau de bord mensuel suppose des pièces mensuelles : chez la moitié de mes clients, elles arrivent par trimestre. »

### ANNEXE 2.3 – Indicateurs de production du cabinet par bureau

**A. Tableau des indicateurs (2025 → 2026, chiffres arrondis)**

| Bureau | Clients (2026) | Part des pièces reçues sous forme dématérialisée | Délai moyen de remise des comptes annuels (jours après la clôture) | Heures de saisie et de rapprochement par client et par an | Taux d'utilisation du portail (part des clients qui y déposent leurs pièces, application comprise) | Honoraires de conseil (part des honoraires du bureau) |
|---|---|---|---|---|---|---|
| Poitiers | 1 000 | 80 % → 90 % | 100 → 85 | 12 → 8 | 60 % → 80 % | 7 % → 8 % |
| Niort | 500 | 80 % → 90 % | 100 → 110 | 12 → 8 | 65 % → 80 % | 7 % → 8 % |
| La Rochelle | 500 | 80 % → 90 % | 100 → 85 | 12 → 8 | 55 % → 80 % | 7 % → 14 % |
| Angoulême | 400 | 70 % → 75 % | 110 → 100 | 14 → 12 | 45 % → 50 % | 6 % → 7 % |
| Saintes | 350 | 60 % → 65 % | 120 → 120 | 16 → 15 | 20 % → 25 % | 6 % → 6 % |
| Châtellerault | 250 | 60 % → 65 % | 120 → 120 | 16 → 15 | 20 % → 25 % | 6 % → 6 % |
| **Cabinet** | **3 000** | **75 % → 83 %** | **105 → 98** | **13 → 10** | **50 % → 65 %** | **7 % → 9 %** |

Ligne Cabinet, honoraires de conseil : part des honoraires totaux du cabinet (annexe 2.4 A).

**B. Précisions apportées par les bureaux**

- Niort : trois collaborateurs sont partis au premier semestre 2026 et n'ont été remplacés qu'en janvier 2027.
- La Rochelle : l'associée responsable du bureau a créé en 2026 une cellule de deux collaborateurs consacrée au conseil et formé ses chefs de mission à l'entretien avec les dirigeants.
- Saintes et Châtellerault : la clientèle compte davantage d'artisans, d'exploitations agricoles et d'associations, qui déposent plus souvent leurs pièces sur papier ou par courriel.
- Les heures sont déclarées par les collaborateurs dans le logiciel de temps ; à Niort, le délai des comptes annuels court jusqu'à leur signature par le client, dans les autres bureaux jusqu'à leur envoi.
- Les honoraires de tenue de l'ensemble du cabinet ont baissé de 0,5 M€ en 2026 (annexe 2.4).

**C. Les outils d'analyse disponibles**

- **Tableur avancé** : chaque bureau tient ses indicateurs dans son propre classeur, alimenté chaque mois par des extractions du logiciel de production et du logiciel de temps ; la synthèse du cabinet est refaite à la main chaque trimestre par l'assistante de la présidente.
- **Outil de visualisation** acquis en septembre 2026 (15 licences, 12 k€ par an) : il peut se connecter directement au logiciel de production et au logiciel de temps, rafraîchir les données chaque nuit et publier des tableaux de bord interactifs consultables sur ordinateur et sur tablette. Trois personnes l'utilisent régulièrement : l'analyste de données et deux associés.

### ANNEXE 2.4 – Le modèle économique en question

*Extrait du compte rendu du séminaire des associés (janvier 2027)*

**A. Les honoraires (M€)**

| Activité | 2025 | 2026 |
|---|---|---|
| Tenue, révision, comptes annuels et déclarations fiscales | 14,5 | 14,0 |
| Paie et social | 5,5 | 6,0 |
| Conseil aux dirigeants | 1,5 | 2,0 |
| **Total** | **21,5** | **22,0** |

**B. Constats présentés au séminaire**

- **Prix de la tenue** : le forfait annuel moyen de tenue d'une TPE a baissé de 10 % en deux ans, sous l'effet de renégociations demandées par les clients.
- **Concurrence** : des plateformes en ligne proposent aux TPE une tenue automatisée (connexion à la banque, lecture automatique des pièces) et les comptes annuels pour moins de 100 € par mois ; 150 clients, des TPE, sont partis vers ces plateformes en 2026, soit 5 % de la clientèle.
- **Attentes des clients** (enquête de satisfaction 2026, 1 000 répondants) : 60 % souhaitent un point régulier sur leur trésorerie en cours d'année ; 45 % estiment que le cabinet « intervient trop tard, au moment des comptes annuels » ; 30 % se disent prêts à payer un tableau de bord mensuel.
- **Temps des collaborateurs comptables** (enquête de temps 2026) : 25 % pour la saisie, le rapprochement et les relances de pièces ; 65 % pour la révision, les comptes annuels et les déclarations ; 10 % pour le conseil. Le coût horaire moyen d'un collaborateur comptable, charges comprises, est de 50 €.
- **Budget du système d'information** (1,1 M€) : 80 % pour faire fonctionner l'existant (abonnements aux logiciels de production comptable et de paie, postes de travail, assistance), 20 % pour les projets. Le cabinet compte une seule analyste de données.

**C. Objectifs retenus par le séminaire pour fin 2029**

95 % des pièces reçues sous forme dématérialisée ; 80 % des pièces intégrées automatiquement ; relevés bancaires par flux automatisé pour 80 % des clients ; 6 heures de saisie et de rapprochement par client et par an ; 10 % de dossiers incomplets à la clôture ; comptes annuels remis en 75 jours en moyenne ; honoraires de conseil portés à 20 % du chiffre d'affaires en 2030.

**D. Positions exprimées**

**Mme Hélène VARENNAT, présidente** : « La saisie disparaît ; ce que nos clients attendent, c'est que nous les aidions à décider. Je ne veux pas d'un projet informatique de plus : je veux savoir ce que notre système d'information doit devenir pour servir cette ambition. »

**M. Laurent CHAMPEYRAC, associé chargé du conseil aux dirigeants** : « Nous connaissons nos clients mieux que leur banquier : leurs données sont notre meilleur atout. Le conseil doit devenir notre premier métier. »

**Mme Odile FERNIAC, associée au bureau de Saintes** : « Automatisons d'abord la tenue pour rester compétitifs face aux plateformes : c'est elle qui paie les salaires. Nos collaborateurs sont des comptables, pas des consultants, et beaucoup de nos clients ne veulent pas du portail. »

**E. Repères au 31/12/2026**

| Référence | Contenu utile au dossier | Situation au 31/12/2026 |
|---|---|---|
| Généralisation de la facturation électronique et du e-reporting (article 91 de la loi de finances pour 2024 ; code général des impôts) | Les factures entre entreprises assujetties à la TVA établies en France sont émises, transmises et reçues sous forme électronique par l'intermédiaire d'une plateforme agréée par l'administration ; les formats admis sont Factur-X, UBL et CII. | Depuis le 01/09/2026 : réception obligatoire pour toutes les entreprises ; émission obligatoire pour les grandes entreprises et les entreprises de taille intermédiaire. À compter du 01/09/2027 : émission obligatoire pour les PME et les micro-entreprises. |

Aucune analyse des obligations issues de cette réforme n'est attendue.

### Travail à faire

Mme VARENNAT présentera au comité des associés de juin 2027 la manière dont le cabinet compte tirer parti des données de ses clients pour développer le conseil. Elle attend de vous une organisation de la collecte des données, un avis sur l'offre « Pilotage dirigeant » et son outil d'alerte, un diagnostic de la production, des indicateurs pour piloter sa transformation et une analyse du modèle économique du cabinet. Vous mobiliserez pour cela les annexes 1.1, 2.1, 2.2, 2.3 et 2.4 ainsi que vos connaissances professionnelles.

**2.1 – Chaîne de traitement et organisation de la collecte (3 points)**

a) Après avoir défini la chaîne de traitement des données, décrivez celle des données des clients du cabinet, de la collecte à la restitution, puis identifiez, à partir de l'annexe 2.1, quatre faiblesses en les rattachant à l'étape concernée.

b) Après avoir défini l'interopérabilité, proposez une organisation cible de la collecte en quatre mesures qui garantissent la qualité et la circulation des données : formats structurés et ouverts, connexions par API aux banques et aux logiciels des clients, règles de nommage et de rapprochement, accompagnement des clients. Pour chaque mesure, précisez ce qui change pour les clients. Aucun détail technique des échanges ni aucune modélisation de données n'est attendu.

**2.2 – Méthodes d'analyse et outil d'alerte (3 points)**

a) Présentez les méthodes d'analyse descriptive, exploratoire et prédictive, en rattachant chacune à l'un des trois services de l'offre « Pilotage dirigeant » (annexe 2.2 A).

b) Analysez les résultats de l'essai de l'outil d'alerte (annexe 2.2 C) sous quatre angles : fausses alertes et difficultés non détectées, corrélation et causalité, biais des données, explicabilité au client. Aucun calcul statistique n'est attendu.

c) Formulez trois conditions pour faire de cet outil une aide à la décision des chefs de mission, puis prenez position, en la justifiant, sur la proposition de M. CHAMPEYRAC.

**2.3 – Diagnostic de la production et restitution au comité des associés (2 points)**

a) À partir de l'annexe 2.3, formulez, en douze lignes au maximum, un diagnostic argumenté de la production du cabinet : deux constats, une hypothèse d'explication pour chacun et deux précautions de lecture.

b) Proposez, pour chacun des deux constats, la représentation visuelle la plus adaptée au comité des associés, puis recommandez, en le justifiant, l'outil décisionnel de l'annexe 2.3 C qui convient pour la produire. Aucune manipulation d'outil n'est attendue.

**2.4 – Indicateurs de pilotage de la transformation de la production (2 points)**

Après avoir précisé ce qu'est un tableau de bord équilibré, proposez quatre indicateurs pour piloter la transformation de la production du cabinet, qui équilibrent performance, risques et coûts, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

**2.5 – Modèle économique et stratégie du système d'information (3 points)**

a) Après avoir défini le modèle économique d'une organisation, analysez l'effet de l'automatisation de la saisie et de l'exploitation des données des clients sur celui du cabinet, sous trois angles : la proposition de valeur, les ressources et les revenus.

b) Après avoir défini l'alignement stratégique, recommandez une stratégie du système d'information alignée sur l'objectif de développer le conseil, sous la forme de trois priorités hiérarchisées et justifiées par les annexes.
