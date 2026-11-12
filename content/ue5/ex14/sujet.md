# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 14

**DOSSIER 2 – PRÉPARER L'INTÉGRATION DU SYSTÈME D'INFORMATION D'UN TRANSPORTEUR ACQUIS (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 5, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en avril 2027. ORMESTAL France est une société par actions simplifiée, filiale à 100 % du groupe ORMESTAL, spécialiste européen de la logistique sous température dirigée, dont le siège est à Rotterdam et qui est présent dans huit pays. Basée à Mâcon, ORMESTAL France emploie 650 salariés et exploite 14 entrepôts frigorifiques (9 en froid positif, 5 en froid négatif) ainsi qu'une flotte de 260 camions réfrigérés, pour le compte d'industriels de l'agroalimentaire et d'enseignes de la grande distribution. Son chiffre d'affaires de l'exercice 2026 s'élève à 180 millions d'euros ; 4,5 millions d'euros sont consacrés au système d'information. Le 4 janvier 2027, elle a acquis la société Transports CAUVERLIN, transporteur frigorifique régional de l'Ain (110 salariés, 85 camions, 16 millions d'euros de chiffre d'affaires en 2026). Les organisations, les personnes et les données de ce cas sont fictives.

Le plan stratégique du groupe, « ORMESTAL 2030 », adopté en novembre 2026, fixe trois priorités à toutes les filiales : réduire de 20 % la consommation d'énergie des entrepôts et l'empreinte environnementale du système d'information d'ici 2030 ; réussir l'intégration des sociétés acquises en moins d'un an ; adopter, d'ici fin 2028, le socle SI commun que propose la direction des systèmes d'information du groupe pour les fonctions support. La directrice générale d'ORMESTAL France, Mme Valérie DUCHASTEL, rend compte de la mise en œuvre de ce plan au directeur des opérations du groupe pour l'Europe de l'Ouest, M. Pieter DORMAELS.

Vous êtes consultant(e) au sein d'un cabinet de conseil en systèmes d'information, missionné(e) par Mme DUCHASTEL. Elle vous confie trois travaux : rendre le système d'information de la filiale plus sobre et plus durable et en piloter les résultats (dossier 1) ; préparer l'intégration du système d'information de Transports CAUVERLIN (dossier 2) ; éclairer la décision d'adhérer au socle SI du groupe (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation d'ORMESTAL France et chiffres clés

ORMESTAL France est une société par actions simplifiée détenue à 100 % par le groupe ORMESTAL, spécialiste européen de la logistique sous température dirigée, dont le siège est à Rotterdam et qui est présent dans huit pays. Basée à Mâcon, elle stocke, prépare et transporte, sous température dirigée, les produits d'industriels de l'agroalimentaire et d'enseignes de la grande distribution, vers leurs entrepôts et leurs magasins. Son exercice coïncide avec l'année civile. Le groupe fixe les orientations de ses filiales par son plan stratégique « ORMESTAL 2030 » ; sa direction des systèmes d'information propose aux filiales un socle SI commun pour les fonctions support.

**Chiffres clés de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Activité | entreposage frigorifique (froid positif et froid négatif), préparation de commandes, transport réfrigéré vers les entrepôts et les magasins des enseignes |
| Clients | industriels de l'agroalimentaire et enseignes de la grande distribution |
| Chiffre d'affaires | 180 M€ |
| Salariés | 650 |
| Entrepôts | 14 entrepôts frigorifiques : 9 en froid positif, 5 en froid négatif |
| Flotte | 260 camions réfrigérés |
| Budget du système d'information | 4,5 M€ (2,5 % du chiffre d'affaires) |
| Société acquise | Transports CAUVERLIN, transporteur frigorifique régional de l'Ain, acquise le 4 janvier 2027 : 110 salariés, 85 camions, chiffre d'affaires 2026 de 16 M€ |
| Plan « ORMESTAL 2030 » (adopté en novembre 2026) | réduire de 20 % la consommation d'énergie des entrepôts et l'empreinte environnementale du SI d'ici 2030 ; intégrer les sociétés acquises en moins d'un an ; adopter d'ici fin 2028 le socle SI commun proposé par la direction des systèmes d'information du groupe pour les fonctions support |

**Organigramme simplifié (avril 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Groupe ORMESTAL (Rotterdam) | directeur des opérations du groupe pour l'Europe de l'Ouest, à qui la directrice générale d'ORMESTAL France rend compte de la mise en œuvre du plan « ORMESTAL 2030 » | M. Pieter DORMAELS |
| Groupe ORMESTAL (Rotterdam) | directeur des systèmes d'information du groupe | M. Joost KAMPERVELD |
| Direction générale d'ORMESTAL France | directrice générale | Mme Valérie DUCHASTEL |
| Comité de direction | directeur des opérations (entrepôts et transport) | M. Marc DRAVIGNOL |
| Rattaché au directeur des opérations | responsable des entrepôts (14 entrepôts) | M. Karim TALBREUX |
| Rattachée au directeur des opérations | responsable du transport (flotte de 260 camions) | Mme Sandrine VALDRESSE |
| Comité de direction | directrice administrative et financière | Mme Isabelle MERCOIRAN |
| Comité de direction | responsable des systèmes d'information, rattaché à la directrice générale, en lien avec la direction des systèmes d'information du groupe | M. Thomas BRÉVANNE |
| Rattachée à la directrice générale | responsable RSE | Mme Léa PRUNEYRAC |

### ANNEXE 2.1 – Les deux systèmes d'information

*Note de M. Thomas BRÉVANNE, responsable des systèmes d'information d'ORMESTAL France, à la directrice générale (mars 2027). La note décrit les fonctions et les échanges des applications, sans détail technique.*

**A. Le système d'information d'ORMESTAL France**

| Application | Fonctions couvertes | Échanges |
|---|---|---|
| Logiciel de gestion des entrepôts | réception, stockage, préparation des commandes et expédition dans les 14 entrepôts | reçoit les ordres des clients par échange de données informatisé ; transmet chaque expédition au logiciel de gestion du transport |
| Logiciel de gestion du transport | réception des commandes de transport ; calcul de propositions de tournées (ordre des livraisons, affectation des camions et des conducteurs), que les exploitants valident ou modifient ; suivi de l'exécution | reçoit les commandes de transport de 70 % des clients par échange de données informatisé, dans un format normalisé ; les autres clients saisissent leurs commandes sur le portail ; transmet les tournées réalisées au logiciel de gestion comptable et commerciale |
| Télématique des camions | dans chaque camion, une tablette et un boîtier : position, températures du caisson, heure d'arrivée, signature du destinataire sur la tablette (preuve de livraison) | transmet ces informations en continu au logiciel de gestion du transport et au portail des clients |
| Portail des clients | suivi des livraisons, téléchargement des preuves de livraison et des certificats de température, saisie de commandes | les clients qui le souhaitent récupèrent les preuves de livraison par une interface de programmation (API) |
| Logiciel de gestion comptable et commerciale | fichier des clients, grilles de tarifs datées, facturation mensuelle calculée à partir des tournées réalisées, comptabilité | reçoit les tournées réalisées du logiciel de gestion du transport |

Identifiants : un client porte un code à cinq chiffres attribué par le logiciel de gestion comptable et commerciale ; un site de livraison, un code créé par les exploitants dans le logiciel de gestion du transport ; un camion, son numéro de parc.

Points faibles : le fichier des clients existe en deux exemplaires, dans le logiciel de gestion comptable et commerciale et dans le logiciel de gestion du transport, rapprochés à la main chaque semaine ; chaque exploitant peut créer un site de livraison, sans contrôle des doublons.

**B. Le système d'information de Transports CAUVERLIN**

| Outil | Fonctions couvertes | Échanges |
|---|---|---|
| Logiciel de transport acquis en 2009, installé dans les bureaux de la société | saisie des commandes, édition des documents de transport, enregistrement des tournées réalisées, export mensuel des tournées pour la facturation | aucun échange automatisé ; l'éditeur cessera d'assurer la maintenance de cette version le 30 septembre 2027 |
| Tableur de planification, partagé par les deux exploitants | construction, chaque après-midi, des tournées du lendemain ; contraintes de chaque site (horaires de réception, quai, accès) notées dans des onglets | les tournées sont ensuite ressaisies dans le logiciel de transport |
| Fichiers des clients et des tarifs, tenus par le fondateur dans un tableur de son ordinateur portable | coordonnées des clients, tarifs négociés par liaison | envoyés chaque mois par courriel au cabinet d'expertise comptable |
| Facturation et comptabilité, confiées à un cabinet d'expertise comptable | factures mensuelles, comptabilité, comptes annuels | le cabinet ressaisit les exports du logiciel de transport et applique les tarifs du tableur |
| Échanges avec les 120 chargeurs | 80 chargeurs envoient leurs commandes par courriel (fichier de tableur ou texte libre), 30 chargeurs par téléphone, 10 chargeurs déposent un fichier dans un espace partagé | aucun portail ; les relevés de température, conservés par l'enregistreur de chaque caisson, sont lus au retour du camion et envoyés au chargeur à sa demande |

Les 85 camions ne sont pas équipés de télématique : les exploitants suivent les tournées par téléphone avec les conducteurs. Identifiants : un client est désigné par son nom, un site de livraison par son adresse, un camion par son immatriculation.

**C. Calendrier et contraintes**

- Le plan « ORMESTAL 2030 » demande que l'intégration de Transports CAUVERLIN soit achevée moins d'un an après son acquisition, le 4 janvier 2027.
- L'éditeur de l'ancien logiciel de transport cesse d'en assurer la maintenance le 30 septembre 2027.
- M. Bernard CAUVERLIN, fondateur, conseiller de la direction depuis l'acquisition, part en retraite le 31 décembre 2027.
- La période de pointe (fêtes de fin d'année) court de la mi-novembre à la fin de décembre : aucune bascule n'y est envisageable.

### ANNEXE 2.2 – Les données à reprendre

**A. Volumes (fin 2026)**

| Données | ORMESTAL France | Transports CAUVERLIN |
|---|---|---|
| Clients (chargeurs) | 400 clients | 140 fiches dans le fichier du fondateur, pour 120 chargeurs réels |
| Sites de livraison | 6 000 sites | 2 500 sites, dont environ 1 000 (magasins et entrepôts des enseignes) déjà connus d'ORMESTAL France sous un autre code |
| Véhicules | 260 camions | 85 camions, dont 12 camions loués dont l'immatriculation change à chaque renouvellement du contrat de location |
| Tarifs | grilles datées, dans le logiciel de gestion comptable et commerciale | 300 grilles, dans le tableur du fondateur |
| Historique des tournées | depuis 2018, dans le logiciel de gestion du transport | environ 200 000 tournées de 2016 à 2026 dans l'ancien logiciel ; horaires réels et incidents de 2024 à 2026 dans les tableurs des exploitants |
| Relevés de température | transmis en continu par la télématique | fichiers lus sur les enregistreurs des caissons, conservés depuis 2020 dans un dossier partagé, classés par camion et par date |

30 chargeurs sont clients des deux sociétés ; ils représentent environ 40 % du chiffre d'affaires de Transports CAUVERLIN.

**B. Constats de qualité (examen des fichiers, février 2027)**

- Clients : 20 doublons dans le fichier de Transports CAUVERLIN (même chargeur sous deux noms, ou une fiche par établissement) ; les 30 chargeurs communs ont un code à cinq chiffres chez ORMESTAL France et un nom, parfois abrégé, chez Transports CAUVERLIN ; le numéro SIREN n'est renseigné que dans la moitié des fiches de Transports CAUVERLIN.
- Sites de livraison : 500 adresses incomplètes (code postal absent, horaires de réception ou quai non renseignés) ; les contraintes d'accès ne figurent que dans les onglets des exploitants.
- Tarifs : 100 grilles sur 300 n'ont pas de date d'effet ; pour 12 des 30 chargeurs communs, les deux sociétés appliquent des tarifs différents à une même liaison.
- Sauvegarde et diffusion : la sauvegarde de l'ancien logiciel est faite sur un disque externe rangé dans le bureau du fondateur ; elle n'a jamais été relue. Le fichier des tarifs a été envoyé par erreur à un chargeur en 2025.

**C. Options étudiées pour les référentiels communs**

| | Option 1 – Référentiel de données maîtres | Option 2 – Entrepôt de données commun | Option 3 – Lac de données |
|---|---|---|---|
| Principe | un référentiel unique des clients, des sites de livraison et des véhicules attribue à chaque objet un identifiant unique et le diffuse aux applications (gestion du transport, portail des clients, gestion comptable et commerciale, télématique) | les données des deux systèmes d'information sont copiées chaque nuit dans un entrepôt où elles sont rapprochées pour produire des tableaux de bord communs ; chaque application garde ses propres fichiers et ses propres identifiants | tous les fichiers (tableurs, exports de l'ancien logiciel, relevés de température) sont déposés en l'état, sans rapprochement préalable, pour des analyses ultérieures |
| Mise en place | 150 k€, 5 mois | 100 k€, 4 mois | 80 k€, 3 mois |
| Fonctionnement annuel | 30 k€ | 20 k€ | 40 k€ |
| Organisation requise | un responsable désigné pour chaque référentiel ; des règles de création et de rapprochement des fiches | des règles de rapprochement appliquées dans l'entrepôt | des spécialistes de l'analyse des données |

### ANNEXE 2.3 – Témoignages (recueillis en mars 2027)

**M. Bernard CAUVERLIN, fondateur de Transports CAUVERLIN** : « J'ai créé la société en 1994. Les tarifs, je les ai négociés un par un avec chaque chargeur ; beaucoup ne sont écrits que dans mon tableur, et certains seulement dans ma tête. Nos clients nous restent fidèles parce que nos exploitants connaissent chaque magasin : la cour trop étroite, le quai qui ferme à 6 heures. Je pars fin décembre : il faudra que tout cela soit ailleurs que chez moi. »

**Mme Coralie ESTARDEL, exploitante chez Transports CAUVERLIN** : « Je reçois une commande par courriel, je la recopie dans le tableur, je construis la tournée, puis je la ressaisis dans le logiciel : deux heures par jour de saisie. Le cabinet comptable la ressaisit une troisième fois pour facturer. Le logiciel d'ORMESTAL, je veux bien, mais je ne veux pas devenir une presse-bouton. »

**M. Kévin MORLANDIER, exploitant chez Transports CAUVERLIN** : « Le logiciel calcule des tournées sur une carte ; il ne sait pas qu'un magasin refuse les livraisons le mardi matin. Si sa tournée est mauvaise et que je la valide, qui est responsable de la marchandise perdue ? Et si je la modifie, il faut qu'on sache pourquoi. »

**Mme Sandrine VALDRESSE, responsable du transport d'ORMESTAL France** : « Dans l'Ain, nos camions et ceux de CAUVERLIN se croisent chez les mêmes clients, parfois à moitié vides. Avec un seul logiciel de gestion du transport et un seul fichier des camions, nous mutualiserions les tournées. Chez nous, l'exploitant ne construit plus les tournées : il vérifie les propositions du logiciel, traite les imprévus et parle aux clients. »

**Mme Isabelle MERCOIRAN, directrice administrative et financière d'ORMESTAL France** : « Depuis janvier, je supervise la facturation et les comptes de CAUVERLIN. Sur environ 1 400 factures par an, 5 % donnent lieu à un avoir, presque toujours pour un tarif contesté : sans date d'effet, impossible de prouver quel tarif s'appliquait. Il a fallu dix semaines pour arrêter les comptes de 2026 : on ne peut pas remonter d'une facture à la tournée et à la commande, et les tournées réalisées en décembre mais pas encore facturées ont été estimées à la main. Pour 2027, je veux pouvoir suivre chaque montant facturé jusqu'à la commande d'origine et clôturer en quatre semaines, comme chez ORMESTAL France. »

**Mme Hélène SORVIGNAC, responsable logistique de la Fromagerie BRÉMACIER, cliente des deux sociétés** : « Nos commandes partent automatiquement vers ORMESTAL France depuis notre logiciel, au format normalisé ; vers CAUVERLIN, par courriel, avec un fichier de tableur. Pour les températures, ORMESTAL me donne un certificat sur son portail ; CAUVERLIN m'envoie un relevé quand je le réclame, parfois une semaine plus tard, alors que les enseignes l'exigent sous 48 heures. Je veux un seul interlocuteur et un seul format, mais pas de changement en pleine période des fêtes, et je veux savoir à l'avance qui fait quoi si un échange échoue. »

### Travail à faire

Mme DUCHASTEL souhaite que le système d'information de Transports CAUVERLIN soit intégré à celui d'ORMESTAL France avant la fin de 2027, sans perdre ni le savoir-faire de la société acquise ni la confiance de ses chargeurs. Vous mobiliserez pour cela les annexes 1.1, 2.1, 2.2 et 2.3 ainsi que vos connaissances professionnelles.

**2.1 – Urbanisation et cible de convergence (3 points)**

a) Après avoir présenté les principes de l'urbanisation du système d'information (zones, quartiers, îlots), établissez le diagnostic des deux systèmes d'information décrits à l'annexe 2.1 : deux recouvrements, deux ruptures de flux et deux fonctions sans application.

b) Proposez la cible de convergence, zone par zone, en indiquant pour chaque application ou outil des deux sociétés s'il est repris, remplacé ou abandonné, et pourquoi. Un schéma en format libre est admis ; aucune architecture technique n'est attendue.

**2.2 – Référentiels communs (3 points)**

a) Après avoir défini les données de référence, proposez l'organisation des trois référentiels communs aux deux sociétés (clients, sites de livraison, véhicules) en précisant, pour chacun, l'identifiant unique, la règle de rapprochement des fiches des deux sociétés et le propriétaire. Aucun modèle de données n'est attendu.

b) Comparez les trois options de l'annexe 2.2 C selon trois critères de votre choix, puis recommandez l'architecture adaptée à l'intégration.

**2.3 – Échanges avec les chargeurs (2 points)**

Après avoir défini l'interopérabilité, proposez le dispositif d'échange des commandes de transport et des preuves de livraison (dont les relevés de température) avec les 120 chargeurs de Transports CAUVERLIN : deux choix techniques, sans détail technique des échanges, puis trois dispositions organisationnelles portant respectivement sur l'accord d'échange, les responsabilités et le calendrier de bascule.

**2.4 – Impacts sur les métiers de Transports CAUVERLIN (2 points)**

Après avoir caractérisé la transformation des métiers qu'entraîne une nouvelle architecture du système d'information, analysez, à partir des témoignages de l'annexe 2.3, trois impacts de l'intégration sur les métiers de Transports CAUVERLIN : un impact organisationnel sur le métier d'exploitant, un impact juridique sur la responsabilité en cas d'erreur de planification et un impact comptable sur la piste d'audit et l'arrêté des comptes. Proposez pour chacun une mesure d'accompagnement. Aucune analyse de droit du travail ni de droit des transports n'est attendue.

**2.5 – Valeur, reprise et gouvernance des données (3 points)**

a) Montrez que les données de Transports CAUVERLIN (historique des tournées, fichiers des clients et des tarifs, contraintes des sites) constituent un actif immatériel, puis illustrez par les annexes trois risques qui pèsent sur cet actif : la perte, la fuite et la dépendance à une personne. Aucune évaluation comptable n'est attendue.

b) Proposez la démarche de reprise de ces données en quatre étapes, du nettoyage des doublons et des adresses jusqu'au contrôle après reprise.

c) Proposez trois règles de gouvernance des données de l'ensemble intégré, portant sur trois enjeux différents parmi la qualité, la conformité, la sécurité et le cycle de vie, dont une règle de qualité assortie d'un indicateur précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
