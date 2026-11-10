# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 7

**DOSSIER 1 – ORGANISER, ANALYSER ET VALORISER LES DONNÉES DES APPAREILS CONNECTÉS (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 3, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mai 2027. Le groupe ALTIVERNE est un groupe familial non coté, constitué autour d'une société par actions simplifiée créée en 1962 à Lyon. Il conçoit, installe, modernise et entretient des ascenseurs, des monte-charges et des portes automatiques pour des bailleurs sociaux, des syndics de copropriété, des établissements de santé et des centres commerciaux. Il emploie 2 400 salariés, dont 1 500 techniciens de maintenance répartis dans 34 agences en France, une usine de fabrication des cabines et des armoires de commande à Roanne et deux filiales, en Belgique et en Suisse. Son chiffre d'affaires consolidé de l'exercice 2026 s'élève à 590 millions d'euros, dont 55 % pour la maintenance, 25 % pour la modernisation et 20 % pour les installations neuves ; 14 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le groupe entretient 52 000 appareils, dont 31 000 sont reliés à son centre de télésurveillance : chacun remonte en continu ses alarmes, ses pannes et ses données de fonctionnement. La présidente, Mme Claire ALTIVERNE, petite-fille du fondateur, et le directeur général, M. Hugo DESMAREST, ont adopté en janvier 2027 le plan « ALTIVERNE 2030 » : passer d'une maintenance qui répare à une maintenance qui anticipe, proposer de nouveaux services fondés sur les données des appareils, fiabiliser les processus financiers et faire de la durabilité un argument commercial. Le groupe a décidé de publier volontairement, dès l'exercice 2026, un état de durabilité conforme aux ESRS. Il doit aussi transmettre le savoir-faire de ses techniciens expérimentés, dont 300 partiront à la retraite d'ici 2030.

Vous venez de rejoindre le groupe comme responsable de la transformation numérique, rattaché(e) au directeur général. M. DESMAREST vous confie trois chantiers : organiser et valoriser les données des appareils connectés (dossier 1) ; fiabiliser le système d'information financier et évaluer l'apport des nouvelles technologies (dossier 2) ; inscrire le système d'information dans la démarche de durabilité du groupe et capitaliser les savoir-faire des techniciens (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation du groupe ALTIVERNE et chiffres clés

Le groupe ALTIVERNE est un groupe familial non coté. Sa société mère, une société par actions simplifiée créée en 1962 à Lyon, où se trouve le siège, détient l'usine de Roanne, qui fabrique les cabines et les armoires de commande, ainsi que les 34 agences françaises ; deux filiales exercent le même métier en Belgique et en Suisse. Ses clients sont des bailleurs sociaux, des syndics de copropriété, des établissements de santé et des centres commerciaux. Son exercice coïncide avec l'année civile.

**Chiffres clés de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Activité | conception, installation, modernisation et maintenance d'ascenseurs, de monte-charges et de portes automatiques |
| Chiffre d'affaires consolidé | 590 M€ : maintenance 55 %, modernisation 25 %, installations neuves 20 % |
| Salariés | 2 400, dont 1 500 techniciens de maintenance |
| Implantations | siège à Lyon ; usine à Roanne ; 34 agences en France ; filiales en Belgique et en Suisse |
| Parc entretenu | 52 000 appareils, dont 31 000 reliés au centre de télésurveillance du groupe (alarmes, pannes et données de fonctionnement remontées en continu) |
| Budget du système d'information | 14 M€ (environ 2,4 % du chiffre d'affaires) |
| Plan « ALTIVERNE 2030 » (adopté en janvier 2027) | maintenance qui anticipe ; nouveaux services fondés sur les données des appareils ; processus financiers fiabilisés ; durabilité comme argument commercial |
| Durabilité | le groupe publie volontairement, dès l'exercice 2026, un état de durabilité conforme aux ESRS |
| Savoir-faire | 300 techniciens expérimentés partiront à la retraite d'ici 2030 |

**Organigramme simplifié de la direction (mai 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Présidence | présidente, petite-fille du fondateur | Mme Claire ALTIVERNE |
| Direction générale | directeur général, qui porte le plan « ALTIVERNE 2030 » | M. Hugo DESMAREST |
| Rattaché(e) au directeur général | responsable de la transformation numérique (poste créé en 2027) | vous |
| Rattachée au directeur général | responsable RSE | Mme Amélie TESSANDIER |
| Comité de direction | directeur de la maintenance et des services (34 agences, dirigées chacune par un responsable d'agence ; centre de télésurveillance de Lyon) | M. Julien PRADELLE |
| Comité de direction | directrice des installations neuves et de la modernisation | Mme Agathe RIBOULET |
| Comité de direction | directeur industriel (usine de Roanne, achats de composants, pièces détachées) | M. Patrick VIALLARD |
| Comité de direction | directeur commercial et des grands comptes | M. Nicolas BERTHOLON |
| Comité de direction | directeur administratif et financier | M. Thibault MARSANGE |
| Comité de direction | directrice des systèmes d'information | Mme Isabelle CHAMBRUN |
| Comité de direction | directrice des ressources humaines | Mme Céline MAUFRAS |
| Filiales | directeurs des filiales belge et suisse, rattachés au directeur général | — |

### ANNEXE 1.2 – Les données du parc et leur circulation actuelle

**A. Les sources de données (note de la DSI, mars 2027)**

| Source | Données | Outil et format | Identifiant de l'appareil utilisé |
|---|---|---|---|
| Boîtiers de télésurveillance (31 000 appareils) | alarmes, pannes, données de fonctionnement (nombre de trajets, ouvertures de portes, durée des trajets, défauts de l'armoire de commande) ; appels vocaux des personnes bloquées en cabine vers le centre de télésurveillance | plateforme du constructeur des boîtiers, format propriétaire ; historique détaillé conservé 13 mois par le constructeur, puis effacé | numéro de série du boîtier |
| Interventions des techniciens (52 000 appareils) | bons d'intervention saisis sur le terminal mobile : appareil, motif, code panne choisi dans une liste de 140 codes, commentaire libre, pièces utilisées, durée, nom du technicien | logiciel de gestion des interventions | numéro d'appareil attribué par l'agence, selon une numérotation propre à chaque agence |
| Contrats et clients | contrats de maintenance, niveaux de service promis, adresses des immeubles, facturation | progiciel de gestion intégré du groupe | numéro de contrat et adresse (un contrat couvre souvent plusieurs appareils) |
| Pièces détachées | stocks de l'usine de Roanne et des agences, consommations, références des fabricants de composants | logiciel de gestion des stocks | aucun : le lien avec l'appareil passe par le bon d'intervention |
| Appareils non connectés (21 000 appareils) | caractéristiques (marque, année de mise en service, nombre de niveaux), historique des visites et des pannes | 34 tableurs d'agence, aux structures différentes | numéro de l'agence ou adresse de l'immeuble |

**B. Les flux actuels**
- Chaque nuit, la plateforme du constructeur produit un fichier des alarmes et des pannes de la veille, chargé dans le logiciel des interventions ; les données de fonctionnement détaillées restent sur la plateforme du constructeur, consultables écran par écran ; leur extraction est facturée par le constructeur.
- Les bons d'intervention sont transmis au progiciel de gestion en fin de journée pour la facturation ; les interventions hors contrat sont ressaisies par les assistantes d'agence.
- Une table de correspondance entre numéros de boîtier, numéros d'agence et numéros de contrat est tenue à la main par une assistante du centre de télésurveillance.
- Les tableurs des agences sont envoyés par courriel au siège chaque trimestre.

**C. Constats du profilage des données (mars 2027)**

| Constat | Mesure |
|---|---|
| Boîtiers non rattachés à un appareil identifié dans le logiciel des interventions | 1 800 sur 31 000 |
| Nombre d'appareils entretenus selon la source | 52 000 dans le progiciel de gestion (référence des contrats) ; 52 900 en cumulant les listes d'appareils tenues par les 34 agences (numérotation propre à chaque agence et tableurs) |
| Bons de dépannage portant le code panne « autre » ou aucun code | 35 % |
| Appareils non connectés dont la date de mise en service n'est pas renseignée | 30 % des fiches des tableurs |
| Délai de mise à disposition au siège des données des appareils non connectés | trimestriel |

**D. La demande des grands clients**

Trois grands bailleurs sociaux, qui confient au groupe 11 000 appareils, reçoivent aujourd'hui un rapport mensuel au format PDF, établi à la main par les agences. Ils demandent à récupérer chaque jour, dans leur propre outil de gestion de patrimoine et par une interface automatisée, les données de disponibilité et les pannes de leurs appareils. Leurs outils sont différents et leurs services informatiques ne sont pas disponibles pour développer des échanges propres à chaque prestataire.

**E. Témoignages (avril 2027)**

**Mme Isabelle CHAMBRUN, directrice des systèmes d'information** : « Un même ascenseur a quatre numéros selon l'outil qui le décrit. Le constructeur des boîtiers nous livre chaque nuit un fichier dans son format à lui, et tout ce qui a plus de treize mois disparaît. Nous n'avons pas de référentiel des appareils : chacun corrige les données dans son coin. »

**Mme Sandrine OLLAGNIER, responsable de l'agence de Saint-Étienne (1 600 appareils)** : « Mes techniciens choisissent "autre" parce que la liste des 140 codes est illisible sur le téléphone. Mon tableur d'agence, je le tiens moi-même, et personne ne s'en sert au siège. »

**La directrice du patrimoine d'un bailleur social client (4 500 appareils)** : « Ce sont nos ascenseurs, et ce sont nos locataires qui restent bloqués. Nous voulons les données de disponibilité tous les jours dans notre outil, pas un PDF à la fin du mois. »

### ANNEXE 1.3 – Projet « maintenance qui anticipe » et premiers résultats

**A. Chiffres de l'exercice 2026 (direction de la maintenance et des services)**

| Indicateur | Appareils connectés (31 000) | Appareils non connectés (21 000) | Ensemble du parc (52 000) |
|---|---|---|---|
| Pannes ayant donné lieu à un dépannage | 62 000 (2 par appareil et par an) | 63 000 (3 par appareil et par an) | 125 000 |
| Délai moyen entre la panne et l'arrivée du technicien | 2 h 30 (alarme automatique) | 4 h (appel du client) | environ 3 h 15 |
| Disponibilité moyenne des appareils | 98,5 % | non mesurée | — |
| Appareils mis en service ou modernisés depuis moins de quinze ans | 80 % | 25 % | — |

Objectif du plan « ALTIVERNE 2030 » : réduire de 30 % les pannes des appareils connectés, soit 1,4 panne par appareil et par an en 2030.

**B. Étude rétrospective de l'agence pilote de Lyon-Est (1 200 appareils connectés, exercice 2026)**

Sur les 2 400 pannes de l'année, 40 % ont été précédées, dans les quinze jours, d'au moins un « signal faible » enregistré par le boîtier (défauts de porte répétés, allongement de la durée des trajets, arrêts hors niveau). Les mêmes signaux ont été relevés 3 000 fois sans être suivis d'une panne. Les bons d'intervention de l'agence ont été relus un à un par deux techniciens pour corriger les codes panne avant l'étude.

**C. Le tableau de bord actuel de la direction de la maintenance**

Un classeur de tableur, mis à jour à la main par l'assistante de direction et diffusé à J+15 : une page unique de 24 indicateurs nationaux, dont le nombre de pannes de chaque agence en valeur absolue, sans rapport au nombre d'appareils entretenus, et le délai moyen d'intervention national, sans cible ni détail par agence. Les responsables d'agence déclarent ne pas le consulter.

**D. Les trois usages envisagés par la direction de la maintenance et des services**
1. **Comprendre les pannes passées** : combien de pannes, où, sur quels types d'appareils, pour quelles causes et avec quelle évolution, agence par agence.
2. **Explorer les facteurs de panne** : rechercher les liens entre les pannes et l'âge, la marque, l'intensité d'usage des appareils, le type d'immeuble et les signaux faibles.
3. **Prévoir les pannes** : estimer, chaque jour, les appareils connectés exposés à une panne dans les quinze jours, pour programmer une visite avant la panne. Un prestataire spécialisé propose de construire le modèle de prévision à partir des données du groupe.

**E. Les outils disponibles**
- Le tableur avancé, dont tous les cadres disposent, utilisé pour le tableau de bord actuel et les tableurs d'agence.
- Un outil de visualisation du marché, testé par la DSI pendant trois mois : connexion aux différentes sources, tableaux de bord interactifs, consultation sur ordinateur et sur terminal mobile, droits d'accès par agence, rafraîchissement programmé des données.

**F. Témoignage de M. Julien PRADELLE, directeur de la maintenance et des services**

« Je veux savoir le lundi quels appareils risquent de tomber en panne dans la semaine, et je veux que mes responsables d'agence le voient sur leur téléphone. Mais je ne ferai pas confiance à une prévision que personne ne sait expliquer, et je ne veux pas envoyer mes techniciens sur des fausses alertes. »

### ANNEXE 1.4 – Propositions de valorisation des données et repères (au 31/12/2026)

**A. Trois propositions présentées au comité de direction d'avril 2027**

| Proposition | Description | Porteur | Données utilisées | Enjeu financier annoncé |
|---|---|---|---|---|
| P1 – Rapport de disponibilité | service payant proposé aux bailleurs et aux syndics : tableau de bord en ligne par appareil (disponibilité, pannes, délais d'intervention, comparaison avec des appareils semblables du parc, prévisions de pannes), alertes | M. Nicolas BERTHOLON | télésurveillance, interventions, contrats | 5 € par appareil et par mois ; 15 000 appareils abonnés visés à trois ans, soit 0,9 M€ par an |
| P2 – Cession de données d'usage | un assureur de dommages aux immeubles et un promoteur immobilier proposent d'acheter, pour chaque immeuble identifié par son adresse, les données d'usage (nombre de trajets par heure et par niveau desservi) et de pannes ; les données transiteraient par une société qui se présente comme un service d'intermédiation de données | M. Nicolas BERTHOLON | télésurveillance, contrats (adresses) | 150 000 € par an |
| P3 – Partenariat avec un fabricant de composants | un fabricant européen de moteurs et de variateurs, qui équipe 9 000 appareils connectés du parc, demande à recevoir en continu leurs données de fonctionnement pour améliorer ses produits ; en échange, il accorde une remise de 8 % sur les achats de ses pièces (2,5 M€ par an) et l'accès à ses analyses de défaillance ; il demande l'exclusivité et le droit de réutiliser librement les données reçues | M. Patrick VIALLARD | télésurveillance, interventions | remise sur les achats de pièces |

**B. Propriété et conservation des données : état des lieux**
- Les contrats de maintenance ne disent rien des données recueillies par les boîtiers : ni de leur utilisation par le groupe, ni de leur communication au client ou à des tiers, ni de leur durée de conservation.
- Les données de fonctionnement détaillées sont conservées 13 mois par le constructeur des boîtiers, puis effacées ; les bons d'intervention sont conservés sans limite de durée ; les enregistrements des appels vocaux des personnes bloquées en cabine sont conservés sans durée fixée par le centre de télésurveillance.
- Le registre des traitements tenu par le délégué à la protection des données du groupe ne mentionne ni les données des boîtiers ni les enregistrements des appels.
- Un contrat de maintenance dure en moyenne cinq ans ; environ 2 500 appareils quittent chaque année le parc, à la suite d'un changement de prestataire ou d'un remplacement ; un appareil fonctionne environ 25 ans avant une modernisation lourde. M. PRADELLE souhaite disposer de cinq ans d'historique pour fiabiliser la prévision des pannes.
- Pour l'application des repères ci-dessous, on retiendra que l'appareil relié à un boîtier est un produit connecté, que son utilisateur est le client propriétaire de l'appareil (bailleur, copropriété représentée par son syndic, établissement) et que le groupe ALTIVERNE, qui recueille les données par le service de télésurveillance, en est le détenteur.

**C. Repères réglementaires (au 31/12/2026)**

| Texte | Objet principal | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 (RGPD) | Protection des données à caractère personnel, c'est-à-dire de toute information se rapportant à une personne physique identifiée ou identifiable, directement ou indirectement ; des données pseudonymisées restent des données à caractère personnel, seules des données rendues anonymes de manière irréversible n'en sont plus. Registre des traitements, délégué à la protection des données, conservation limitée à la durée nécessaire à la finalité du traitement. | Applicable depuis le 25/05/2018 |
| Règlement (UE) 2023/2854 (« Data Act ») | L'utilisateur d'un produit connecté peut obtenir du détenteur, sans frais, les données de ce produit qui sont facilement accessibles au détenteur, avec les métadonnées nécessaires à leur interprétation, dans un format structuré, couramment utilisé et lisible par machine, le cas échéant en continu ; il peut demander leur transmission à un tiers de son choix. Le détenteur n'utilise les données à caractère non personnel qu'en vertu d'un contrat avec l'utilisateur et ne les met pas à la disposition de tiers à d'autres fins que l'exécution de ce contrat. | Applicable depuis le 12/09/2025. Les produits connectés mis sur le marché après le 12/09/2026 doivent être conçus de telle sorte que ces données soient, par défaut, accessibles à l'utilisateur. |
| Règlement (UE) 2022/868 sur la gouvernance des données (« Data Governance Act ») | Encadre notamment les services d'intermédiation de données : le prestataire ne peut pas utiliser les données qui transitent par lui à d'autres fins que leur mise à disposition des utilisateurs de données, et il fournit ce service par une personne morale distincte. | Applicable depuis le 24/09/2023 |

### Travail à faire

M. DESMAREST veut que les données des 52 000 appareils deviennent le socle du plan « ALTIVERNE 2030 » : une maintenance qui anticipe, des services nouveaux pour les clients, sans mettre en péril la confiance de ces derniers. Vous mobiliserez pour cela les annexes 1.1 à 1.4 ainsi que vos connaissances professionnelles.

**1.1 – Organisation des données du parc (3 points)**

a) À partir de trois constats de l'annexe 1.2, montrez en quoi l'organisation actuelle des données du parc nuit successivement à leur cohérence, à leur qualité et à leur circulation.

b) Après avoir défini les données de référence, proposez une organisation cible des données du parc fondée sur trois principes, puis schématisez, en format libre, les flux cibles entre les sources, la plateforme de données du groupe et ses utilisateurs internes et externes.

**1.2 – Interopérabilité avec les bailleurs (2 points)**

a) Définissez l'interopérabilité et appliquez ses dimensions technique, sémantique et organisationnelle à la demande des bailleurs sociaux (annexe 1.2).

b) Proposez, en le justifiant, un mode d'échange des données avec les bailleurs, puis trois conditions de son succès.

**1.3 – Analyse des données et aide à la décision (3,5 points)**

a) Décrivez la chaîne de valeur des données du parc, de la collecte à la décision, en illustrant chacune de ses étapes par le cas.

b) Associez à chacun des trois usages de l'annexe 1.3 une méthode d'analyse de données, et montrez pour chacun une limite qui ressort des annexes.

c) Recommandez, en le justifiant, l'un des deux outils de l'annexe 1.3, puis proposez deux visualisations, l'une destinée au directeur de la maintenance et des services, l'autre aux responsables d'agence. Pour l'indicateur représenté par chacune, précisez la formule, la source, la fréquence, la cible et l'axe du tableau de bord.

**1.4 – Gouvernance, cycle de vie et valeur des données (3,5 points)**

a) Après avoir défini la gouvernance stratégique des données, proposez quatre principes de gouvernance des données du parc, portant respectivement sur la qualité, la conformité, la sécurité et la valorisation, en précisant pour chacun qui le porte. Le principe relatif à la qualité sera assorti d'un indicateur (formule, source, fréquence, cible et axe).

b) Décrivez le cycle de vie d'une donnée de fonctionnement remontée par un boîtier de télésurveillance, en fixant pour chacune des cinq étapes (création, stockage, usage, archivage, suppression) une durée ou un événement déclencheur justifié par les annexes.

c) Montrez en quoi les données du parc constituent un patrimoine immatériel du groupe ALTIVERNE, puis identifiez trois risques qui pèsent sur ce patrimoine.

**1.5 – Valorisation des données (2 points)**

Après avoir défini la monétisation des données, évaluez chacune des trois propositions de l'annexe 1.4 au regard des repères réglementaires fournis et de leurs enjeux économiques et éthiques, puis recommandez l'une d'elles en précisant deux conditions de sa mise en œuvre.
