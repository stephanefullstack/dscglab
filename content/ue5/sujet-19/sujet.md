# DSCG UE 5 — Management des systèmes d'information — Sujet d'entraînement complet n° 19

Durée de l'épreuve : 3 heures – Coefficient : 1

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026.

**Document et matériel autorisés** : Aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Le sujet se présente sous la forme de 3 dossiers indépendants :

| Dossier | Intitulé | Points | Durée conseillée |
|---|---|---:|---|
| DOSSIER 1 | PRÉPARER L'ÉVOLUTION DE LA STRATÉGIE ET DE L'ORGANISATION DU SYSTÈME D'INFORMATION, LA RENÉGOCIATION D'UN CONTRAT ET LA TRANSMISSION DES SAVOIRS | 14 points | 1 h 03 |
| DOSSIER 2 | ORGANISER ET EXPLOITER LES DONNÉES DES INSTALLATIONS, EN GARDER LA MAÎTRISE | 13 points | 59 min |
| DOSSIER 3 | MAÎTRISER LES COÛTS, LA FIABILITÉ ET LA SÉCURITÉ DU SYSTÈME D'INFORMATION DE CONDUITE | 13 points | 58 min |

Le sujet comporte 16 annexes, dont 1 communes aux dossiers.

| Dossier | Annexe | Intitulé |
|---|---|---|
| Tous les dossiers | Annexe 1.1 | Présentation d'ESTRAVENT Énergies et chiffres clés |
| DOSSIER 1 | Annexe 1.2 | Ce que la fin des prix garantis change pour ESTRAVENT (note de M. Arnaud VELDRIMONT, directeur de l'énergie, mai 2027, et témoignages) |
|  | Annexe 1.3 | Deux mondes dans le système d'information (constats établis par M. Olivier SAUVERNAY, responsable de la DSI, et Mme Nadège QUILLEBRAND, responsable de la cellule supervision, mai 2027) |
|  | Annexe 1.4 | Le contrat de maintenance de la plateforme de supervision (note de Mme Nadège QUILLEBRAND, responsable de la cellule supervision, mai 2027) |
|  | Annexe 1.5 | Les savoirs du développement des parcs (note de Mme Isaure TRÉMOLLAC, directrice du développement, mai 2027, et témoignages) |
|  | Annexe 1.6 | Repères (au 31/12/2026) |
| DOSSIER 2 | Annexe 2.1 | Le référentiel des installations et les données de conduite (note de M. Fabien LACROUZE, responsable des ingénieurs de la performance, mai 2027) |
|  | Annexe 2.2 | L'énergie non produite de 2024 à 2026 (tableaux de M. Fabien LACROUZE, avril 2027) |
|  | Annexe 2.3 | Les données des éoliennes chez les constructeurs (note de Mme Gaëlle MONTREVIAU, directrice de l'exploitation, mai 2027, et extraits des contrats) |
|  | Annexe 2.4 | Le stockage des mesures (note de M. Olivier SAUVERNAY, responsable de la DSI, mai 2027) |
|  | Annexe 2.5 | Repères (au 31/12/2026) |
| DOSSIER 3 | Annexe 3.1 | Les coûts du système d'information et leur refacturation (note de Mme Agnès DORMEVAL, responsable du contrôle de gestion, mai 2027, et extrait du reporting annuel) |
|  | Annexe 3.2 | Du comptage au chiffre d'affaires (note de M. Thibault ORLANCOURT, directeur financier, mai 2027) |
|  | Annexe 3.3 | Les accès à distance aux installations (constats de Mme Nadège QUILLEBRAND, responsable de la cellule supervision, et de M. Olivier SAUVERNAY, responsable de la DSI, mai 2027) |
|  | Annexe 3.4 | La demande du comité d'audit (courriel de M. Bernard ESCOLIÈRE, président du comité d'audit, mai 2027) |
|  | Annexe 3.5 | Repères (au 31/12/2026) |

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

---

## DOSSIER 1 – PRÉPARER L'ÉVOLUTION DE LA STRATÉGIE ET DE L'ORGANISATION DU SYSTÈME D'INFORMATION, LA RENÉGOCIATION D'UN CONTRAT ET LA TRANSMISSION DES SAVOIRS (14 points)

### ANNEXE 1.2 – Ce que la fin des prix garantis change pour ESTRAVENT (note de M. Arnaud VELDRIMONT, directeur de l'énergie, mai 2027, et témoignages)

**A. La sortie des contrats à prix garanti.** Les 18 parcs qui sortent de leur contrat de vente à prix garanti entre 2026 et 2029 représentent environ 250 MW. Leur production sera vendue de deux façons :
- sur le marché, par l'agrégateur, qui vend chaque jour l'électricité pour le lendemain à partir du programme de production que nous lui envoyons ; plus ce programme est juste, mieux nous vendons ;
- à des industriels, par des contrats d'achat direct. Chaque contrat nous engage à livrer un profil horaire, c'est-à-dire une quantité d'énergie fixée pour chaque heure, et à facturer chaque mois l'énergie livrée, heure par heure, soit environ 720 valeurs horaires par contrat et par mois. Quand nos parcs produisent moins que le profil, l'agrégateur achète l'énergie manquante sur le marché, à nos frais.

Vendre ainsi suppose une prévision fine de la production de chaque parc, mise à jour plusieurs fois par jour, et un suivi du portefeuille de contrats : volumes engagés, prix, échéances, écarts entre le profil et la production. Nous avons trois contrats d'achat direct ; il en faudra environ 15 contrats en 2031 pour atteindre l'objectif du plan.

**B. Comment nous travaillons aujourd'hui.**
- Les prévisions de production arrivent une fois par jour, à 10 heures, par un fichier du prestataire de prévision, pour le lendemain.
- Chaque contrat d'achat direct est suivi dans son propre tableur ; le progiciel de gestion intégré ne connaît que le montant de la facture.
- Les factures horaires sont préparées à la main par deux personnes de la direction de l'énergie, qui y passent chacune cinq jours par mois : elles rapprochent les données de production de la supervision, les relevés mensuels de comptage du gestionnaire du réseau et le profil de chaque contrat.
- En 2026, deux factures mensuelles adressées à des industriels ont été contestées, puis refaites.

**C. Les autres évolutions du plan « ESTRAVENT 2031 ».**
- **Renouvellement** : d'ici 2031, les éoliennes de dix parcs parmi les plus anciens seront remplacées par des machines plus puissantes, d'un autre modèle et parfois d'un autre constructeur.
- **Maintenance reprise aux constructeurs** : ESTRAVENT assure elle-même la maintenance des éoliennes sorties des contrats des constructeurs, 60 éoliennes en 2027 et environ 200 en 2031, avec ses techniciens et des sous-traitants ; il faut planifier les interventions, gérer les pièces de rechange et connaître l'historique des alarmes de chaque machine.
- **Stockage** : deux sites de stockage par batteries, installés à côté de parcs, seront à l'essai à partir de 2028 ; ils devront se charger quand l'électricité est abondante et se décharger quand elle est chère, ce qui suppose de piloter les batteries à partir des prévisions et des prix.
- **Développement** : la puissance installée doit passer de 1 400 MW à 2 500 MW en 2031.

**D. Les projets du système d'information.** ESTRAVENT n'a pas de plan stratégique du système d'information. Le dernier exercice de ce type, un schéma directeur 2018-2021, n'a jamais été mis à jour. Chaque direction lance ses projets : la direction de l'énergie veut acheter un logiciel de gestion des contrats de vente, la direction de l'exploitation veut étendre le logiciel de gestion de la maintenance aux techniciens et aux sous-traitants, la direction du développement veut remplacer le système d'information géographique. Le comité de direction n'examine les dépenses du système d'information qu'une fois par an, au budget.

**Témoignages recueillis en mai 2027**

**M. Thibault ORLANCOURT, directeur financier** : « Le plan "ESTRAVENT 2031" a été adopté sans un mot sur le système d'information. Le conseil a voté des objectifs de vente et de disponibilité ; personne ne lui a dit ce qu'ils supposaient en outils, en données et en compétences. »

**Une chargée de facturation de la direction de l'énergie** : « Avec trois contrats, nous tenons, en faisant attention. Avec quinze, sans autre méthode, nous ne tiendrons pas. Et quand un industriel nous demande pourquoi nous avons livré moins que le profil à telle heure, il nous faut deux jours pour lui répondre. »

**Mme Gaëlle MONTREVIAU, directrice de l'exploitation** : « Nous savons conduire des éoliennes. Ce que nous ne savons pas encore faire, c'est les entretenir nous-mêmes : nos techniciens doivent avoir sur leur tablette l'historique de la machine, les alarmes du jour et les pièces disponibles. »

### ANNEXE 1.3 – Deux mondes dans le système d'information (constats établis par M. Olivier SAUVERNAY, responsable de la DSI, et Mme Nadège QUILLEBRAND, responsable de la cellule supervision, mai 2027)

**A. Qui fait quoi.**
- La **DSI** (22 personnes, rattachée à la direction de la performance et des systèmes d'information, elle-même rattachée au directeur financier) gère l'informatique de gestion : applications, postes de travail, messagerie, réseau du siège et des agences, support aux utilisateurs.
- La **cellule supervision** (8 personnes, direction de l'exploitation) gère la plateforme de supervision, les liens avec les systèmes des trois constructeurs et des centrales solaires, et les postes du centre de conduite, avec l'ESN qui maintient la plateforme. Elle a son propre calendrier, sa propre astreinte et ses propres achats.
- Les deux équipes ne se réunissent jamais. Aucune instance ne traite ensemble l'informatique de gestion et l'informatique de conduite ; le comité de direction ne les voit que dans le budget.

**B. Les frictions relevées.**
1. En mars 2026, la DSI a installé une mise à jour de la messagerie un mardi soir. Les alarmes du centre de conduite, envoyées aux techniciens d'astreinte par la messagerie, ont été coupées pendant deux heures ; ni la cellule supervision ni le centre de conduite n'avaient été prévenus.
2. En 2026, la direction de l'exploitation a souscrit seule un outil en ligne d'analyse des vibrations des éoliennes. La DSI l'a découvert à la réception de la facture ; l'outil n'est relié à aucun autre, et les ingénieurs de la performance y chargent les données à la main.
3. Personne n'a la liste complète des postes reliés aux installations : la DSI en recense 40, la cellule supervision 55, et ni l'une ni l'autre ne sait qui doit tenir la liste.
4. Les techniciens ont un compte dans l'annuaire de la DSI et un autre sur la plateforme de supervision, créés et supprimés séparément : 30 comptes de personnes parties sont encore actifs sur la plateforme. Chaque intervention est saisie dans le logiciel de gestion de la maintenance, puis ressaisie dans la plateforme de supervision pour suspendre les alarmes de la machine pendant les travaux.

**C. Les échanges avec les organisations extérieures.**

| Organisation extérieure | Ce qui est échangé | Comment, aujourd'hui |
|---|---|---|
| Constructeurs A, B et C | données de fonctionnement et alarmes des éoliennes ; rapports de maintenance des machines encore sous contrat | trois liens spécifiques avec la plateforme de supervision ; pour le reste, trois portails différents, chacun avec ses formats ; les ingénieurs exportent les données à la main |
| Gestionnaire du réseau de distribution | relevés de comptage mensuels de chaque parc et de chaque centrale | fichiers téléchargés chaque mois sur son portail, puis copiés dans les tableurs de facturation |
| Agrégateur | programme de production du lendemain ; quantités vendues et prix obtenus | programme envoyé chaque jour par courriel, en tableur ; relevés de ventes reçus en PDF |
| Industriels clients (trois contrats) | profils horaires ; factures mensuelles et détail horaire | profils en tableur ; factures envoyées en PDF par courriel |
| Quatre sous-traitants de maintenance | ordres de travail ; comptes rendus d'intervention | ordres envoyés par courriel ; comptes rendus en PDF, ressaisis dans le logiciel de gestion de la maintenance |
| Prestataire de prévision | prévisions de production par parc | un fichier par jour |

Aucun de ces échanges n'a de responsable désigné ; chacun a été construit au fil des besoins, par la direction qui en avait l'usage.

### ANNEXE 1.4 – Le contrat de maintenance de la plateforme de supervision (note de Mme Nadège QUILLEBRAND, responsable de la cellule supervision, mai 2027)

**Le contrat.** La plateforme de supervision du centre de conduite, développée en 2016 pour ESTRAVENT, est maintenue par KALVENTIS Services, une ESN, dans le cadre d'un contrat au forfait de trois ans qui court du 01/01/2025 au 31/12/2027, pour 1,5 M€ par an. Le forfait couvre la correction des anomalies, le support jour et nuit en cas de panne et un volume d'évolutions ; les autres évolutions sont facturées en plus, sur devis. Le contrat fixe deux niveaux de service :
- une **panne bloquante** (le centre de conduite ne voit plus un ou plusieurs parcs) doit être rétablie en 4 heures, jour et nuit, dans 95 % des cas ;
- une **anomalie majeure** doit être corrigée en cinq jours ouvrés, dans 90 % des cas.

Des pénalités sont prévues en cas de manquement, dans la limite de 5 % du forfait annuel ; elles n'ont jamais été réclamées. Le contrat prévoit qu'ESTRAVENT notifie sa décision de renouveler ou non avant le 30/09/2027.

**Le suivi de la prestation**

| Indicateur | Cible du contrat | 2025 | 2026 |
|---|---|---|---|
| Pannes bloquantes | — | 12 | 20 |
| Part des pannes bloquantes rétablies en 4 heures | 95 % | 90 % | 70 % |
| Anomalies majeures | — | 60 | 80 |
| Part des anomalies majeures corrigées en cinq jours ouvrés | 90 % | 80 % | 60 % |
| Évolutions facturées hors forfait | — | 100 k€ | 300 k€ |
| Ingénieurs de KALVENTIS Services affectés à la plateforme | — | 6 | 6 |
| dont ingénieurs remplacés dans l'année | — | 2 | 3 |

**Mes constats.**
- Deux ingénieurs de KALVENTIS Services, présents depuis 2016, sont les seuls à connaître le code de la plateforme ; l'un d'eux m'a dit qu'il quitterait l'ESN en 2028. Les nouveaux venus mettent des mois à être autonomes.
- La documentation de la plateforme n'est plus tenue à jour depuis 2021.
- Aucun comité de suivi ne s'est réuni depuis janvier 2025 ; les chiffres du tableau ci-dessus sont ceux que l'ESN nous envoie, et nous ne les vérifions pas.
- Le contrat ne prévoit ni clause d'audit, ni plan de réversibilité. Il ne dit pas à qui appartiennent les développements spécifiques réalisés depuis 2016 ; le code source est chez KALVENTIS Services, et ESTRAVENT n'en a aucune copie.

**La position de KALVENTIS Services (courrier d'avril 2027).** L'ESN propose de renouveler le contrat pour trois ans, de 2028 à 2030, avec une hausse de 15 % du forfait annuel, qu'elle justifie par la hausse des salaires de ses ingénieurs et par la complexité croissante de la plateforme (nouveaux modèles d'éoliennes, futurs sites de batteries). Elle ne s'engage pas sur de nouveaux niveaux de service.

**Les options connues.** Deux autres ESN ont fait savoir qu'elles pourraient reprendre la maintenance de la plateforme, après six mois de transfert des connaissances. Une reprise partielle par une équipe interne supposerait de recruter quatre développeurs, sur un marché où ils sont rares. Aucune procédure de choix d'un prestataire n'est à organiser dans ce dossier.

### ANNEXE 1.5 – Les savoirs du développement des parcs (note de Mme Isaure TRÉMOLLAC, directrice du développement, mai 2027, et témoignages)

**A. Un métier long, des savoirs rares.** Un projet de parc demande sept à neuf ans entre la recherche d'un site et la mise en service. Il est conduit par un chef de projet d'une des quatre agences régionales, qui le suit d'un bout à l'autre. Nos 45 chefs de projet portent les 70 projets en développement ; 12 des plus expérimentés partiront d'ici 2030, 8 à la retraite et 4 vers d'autres postes ou d'autres entreprises.

| Savoir | Ce qu'il recouvre | Où il se trouve aujourd'hui |
|---|---|---|
| Choisir un site et lire les mesures de vent | repérer les sites possibles ; juger si le mât de mesure est bien placé, si une année de mesures est représentative, si un écart vient du vent ou de l'appareil | dans la tête de quelques chefs de projet anciens ; les rapports de mesure sont dans la gestion électronique des documents, sans le raisonnement qui a conduit à garder ou à écarter un site |
| Dialoguer avec les communes et les riverains | savoir qui rencontrer, dans quel ordre, quand présenter le projet, comment répondre aux inquiétudes | dans les carnets et les téléphones des chefs de projet ; un tiers des communes seulement sont renseignées dans l'outil de gestion des relations avec les propriétaires et les communes |
| Organiser les études environnementales | choisir les bureaux d'études, caler leurs observations de terrain sur une année complète, relire leurs rapports | dans des modèles de cahiers des charges propres à chaque agence ; aucun retour d'expérience écrit |
| Obtenir l'accord des propriétaires et des exploitants des terrains | les rencontrer, négocier, garder leur accord pendant des années | dans l'outil de gestion des relations, pour les coordonnées et les dates ; le reste dans la mémoire des chefs de projet |
| Préparer le raccordement au réseau | savoir, tôt, si le poste électrique voisin pourra accueillir le parc, et préparer la demande au gestionnaire du réseau | chez deux chefs de projet de l'agence Grand Est, qui partiront tous deux à la retraite d'ici 2029 |

**B. Ce qui existe.**
- La gestion électronique des documents des projets contient 60 000 documents ; chaque agence les classe à sa façon, et la recherche ne porte que sur le nom des fichiers.
- Les quatre agences se réunissent une journée par an ; chacune y présente ses mises en service.
- Un wiki du développement a été lancé en 2023 : il compte 12 pages, et personne ne l'a modifié depuis 2024.
- En 2025, l'agence Hauts-de-France a abandonné, après quatre ans d'études, un projet dont le poste électrique voisin ne pouvait plus accueillir de parc : environ 0,5 M€ d'études perdues. L'agence Grand Est avait rencontré la même difficulté en 2021, sur un site comparable ; personne aux Hauts-de-France ne le savait.

**C. Ce que disent les chefs de projet et les agences (témoignages recueillis en mai 2027).**
- Un chef de projet de l'agence Occitanie, 30 ans de métier : « Je n'ai pas le temps d'écrire. Un projet, c'est vingt réunions publiques par an, des soirées en mairie, des week-ends chez les agriculteurs. Le wiki, je l'ai ouvert une fois. »
- Une cheffe de projet de l'agence Grand Est : « Mes contacts dans les mairies, c'est mon travail. Ce sont des relations de confiance, construites sur dix ans ; cela ne se met pas dans une fiche. »
- Le directeur de l'agence Centre-Val de Loire : « Nos primes sont calculées sur nos propres mises en service. Pourquoi passerais-je du temps à aider l'agence voisine, qui nous dispute parfois les mêmes sites ? »
- Un jeune chef de projet de l'agence Hauts-de-France : « Quand je cherche quelque chose, j'appelle un ancien qui sait. Quand il sera parti, j'appellerai qui ? »

### ANNEXE 1.6 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Alignement stratégique | modèle d'alignement stratégique (SAM), J. C. Henderson et N. Venkatraman, *IBM Systems Journal*, 1993 | modèle théorique : cohérence à rechercher entre la stratégie de l'entreprise, la stratégie des technologies de l'information, l'organisation et ses processus, et l'infrastructure du SI |
| Gouvernance du système d'information | COBIT 2019, ISACA (évolution de COBIT 5) | référentiel de gouvernance et de management de l'information et des technologies, ni norme ni logiciel ; un domaine « aligner, planifier, organiser » (APO) |
| Architecture d'entreprise | The TOGAF Standard, 10e édition, The Open Group | méthode d'architecture d'entreprise, ni norme ni logiciel ; conduit le passage d'une architecture existante à une architecture cible |
| Gestion des services informatiques | ITIL 4, PeopleCert (ex-AXELOS), 2019 ; coexiste depuis 2026 avec ITIL (version 5) | référentiel de bonnes pratiques, ni norme ni logiciel : gestion des incidents, des changements et des niveaux de service |
| Gestion des connaissances | modèle SECI, I. Nonaka et H. Takeuchi, *The Knowledge-Creating Company*, 1995 (traduction française : *La connaissance créatrice*, 1997) | modèle théorique : la connaissance se crée par quatre conversions successives entre connaissances tacites et connaissances explicites, en spirale |
| Conduite du changement | ADKAR, Prosci | modèle théorique de l'adhésion individuelle à un changement, en cinq étapes successives |

### Travail à faire

Le plan « ESTRAVENT 2031 » change le métier d'ESTRAVENT : elle devra vendre elle-même une part croissante de son électricité, entretenir ses éoliennes et piloter des batteries. Or son système d'information n'a pas de plan stratégique, ses deux mondes s'ignorent, la plateforme de supervision dépend d'une seule ESN dont le contrat arrive à échéance, et les savoirs du développement des parcs vont partir avec leurs détenteurs. Mme VARLAMBERT vous demande d'analyser les effets du plan sur le système d'information et de préparer sa planification stratégique, de rapprocher l'informatique de gestion et l'informatique de conduite et d'urbaniser le système d'information, de préparer la renégociation du contrat de l'ESN, enfin de concevoir la transmission des savoirs du développement. Vous mobiliserez pour cela les annexes 1.1 à 1.6 ainsi que vos connaissances professionnelles.

**1.1 – Les effets du plan sur le système d'information et sa planification stratégique (3,5 points)**

a) Analysez, à partir de l'annexe 1.2, les effets de la fin des contrats de vente à prix garanti et des autres évolutions du plan « ESTRAVENT 2031 » sur le système d'information : les fonctions nouvelles qu'il devra assurer, les données dont il aura besoin et les délais dans lesquels il devra les fournir. Proposez ensuite trois orientations du système d'information, chacune justifiée par un objectif du plan et par un constat de l'annexe.

b) Après avoir défini la planification stratégique du système d'information, présentez la démarche qui permettrait de bâtir le plan stratégique du système d'information d'ESTRAVENT : ses étapes, ses acteurs, son horizon et la manière d'y rendre les arbitrages. Il n'est demandé ni portefeuille de projets, ni grille de priorisation, ni chiffrage.

**1.2 – Le rapprochement de l'informatique de gestion et de l'informatique de conduite (4 points)**

a) Après avoir présenté les modèles d'organisation de la fonction système d'information (centralisé, décentralisé, fédéral, bimodal), recommandez, à partir de l'annexe 1.3, l'organisation qui rapproche l'informatique de gestion et l'informatique de conduite des installations : rattachement de la cellule supervision, rôles de la DSI et de la direction de l'exploitation, instance commune. Montrez ensuite comment votre recommandation traite trois des frictions décrites dans l'annexe.

b) Après avoir défini l'urbanisation du système d'information, proposez un découpage du système d'information d'ESTRAVENT en zones (gestion, conduite des installations, énergie, développement, et toute zone que vous jugerez utile), en y plaçant les applications des annexes 1.1 et 1.3. Énoncez ensuite deux règles qui rendent cohérents les échanges avec les organisations extérieures de l'annexe 1.3, en montrant ce que chacune change pour l'une d'elles. Il n'est demandé ni cartographie applicative complète, ni détail technique des échanges.

**1.3 – La renégociation du contrat de l'ESN (3 points)**

a) Identifiez, à partir de l'annexe 1.4, quatre risques de la relation avec KALVENTIS Services, chacun appuyé sur un constat de l'annexe.

b) Préparez la négociation du renouvellement : vos objectifs prioritaires, deux concessions que vous pourriez accepter et la solution de repli si la négociation échoue, avec son calendrier. Aucune analyse juridique du contrat ni aucune procédure de choix d'un prestataire n'est attendue.

c) Proposez le dispositif de gouvernance de la relation avec l'ESN (instances, clause d'audit, plan de sortie) et deux indicateurs de suivi, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

**1.4 – La transmission des savoirs du développement des parcs (3,5 points)**

a) Après avoir distingué connaissances tacites et connaissances explicites et présenté le modèle SECI, identifiez, à partir de l'annexe 1.5, trois savoirs critiques du développement des parcs, en justifiant leur criticité, et proposez pour chacun un mode de transmission adapté.

b) Décrivez l'architecture fonctionnelle du dispositif de gestion des connaissances du développement (capter, organiser, retrouver, partager, mettre à jour), en vous appuyant sur les outils existants d'ESTRAVENT. Proposez ensuite sa gouvernance : les rôles, une règle de mise à jour et un indicateur de suivi, précisé par sa formule, sa source, sa fréquence, sa cible et son axe. La gestion des compétences n'est pas à traiter.

c) Proposez trois leviers d'appropriation du dispositif, chacun en réponse à une résistance exprimée dans l'annexe 1.5.

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES INSTALLATIONS, EN GARDER LA MAÎTRISE (13 points)

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

---

## DOSSIER 3 – MAÎTRISER LES COÛTS, LA FIABILITÉ ET LA SÉCURITÉ DU SYSTÈME D'INFORMATION DE CONDUITE (13 points)

### ANNEXE 3.1 – Les coûts du système d'information et leur refacturation (note de Mme Agnès DORMEVAL, responsable du contrôle de gestion, mai 2027, et extrait du reporting annuel)

**A. Les dépenses du système d'information en 2026, par ensemble de services.** Je les ai reconstituées pour la première fois, à partir des factures et des temps déclarés.

| Ensemble de services | Contenu | Dépenses 2026 (k€) |
|---|---|---|
| Informatique de gestion (DSI) | progiciel de gestion intégré, paie, logiciel de gestion de la maintenance, prévision de la production, gestion des contrats de vente et facturation de l'électricité, système d'information géographique et gestion électronique des documents des projets, relations avec les propriétaires et les communes, messagerie et bureautique, postes de travail, réseau du siège et des agences ; 22 personnes | 5 000 |
| *dont services rendus aux sociétés de projet* | *facturation de l'électricité, gestion des contrats de vente et tenue de la comptabilité de chaque société de projet* | *1 500* |
| Supervision des éoliennes | plateforme de supervision et ses serveurs, contrat de l'ESN (1 500 k€), liens avec les systèmes des trois constructeurs, part de la cellule supervision | 2 600 |
| Supervision des centrales solaires | systèmes de supervision propres aux centrales, part de la cellule supervision | 400 |
| Liaisons de télécommunication des sites | liaisons des 64 parcs et des 38 centrales avec le centre de conduite | 800 |
| Centre de conduite | postes et équipements du centre de conduite | 200 |
| **Total** | | **9 000** |

La plateforme de supervision et le contrat de l'ESN servent pour l'essentiel aux éoliennes : chaque centrale solaire n'y remonte qu'une alarme générale, et elle est suivie par son propre système.

**B. La refacturation actuelle.** Depuis 2015, la totalité des dépenses du système d'information est refacturée chaque année aux 102 sociétés de projet, au prorata de leur chiffre d'affaires.
- En 2026, les 38 sociétés de projet des centrales solaires ont réalisé 50 M€ de chiffre d'affaires, et les 64 sociétés de projet des parcs éoliens 200 M€. Les centrales solaires ont donc payé 20 % des dépenses du système d'information, y compris de la supervision des éoliennes, qu'elles n'utilisent pas.
- Un parc éolien du Centre-Val de Loire, arrêté quatre mois en 2026 après la casse d'un multiplicateur, a vu son chiffre d'affaires passer de 4 M€ en 2025 à 2 M€ en 2026, et sa part refacturée baisser de moitié. Ses alarmes sont passées de 2 000 à 6 000, et le centre de conduite l'a suivi de près pendant tout l'arrêt.
- Deux parcs voisins de même puissance paient des montants différents selon que leur électricité est vendue à prix garanti ou sur le marché.
- Les dépenses des outils des projets en développement (système d'information géographique, gestion électronique des documents des projets) sont refacturées aux sociétés de projet des installations en service.

Les règles comptables, fiscales et juridiques de la refacturation ne sont pas à traiter.

**C. Les inducteurs disponibles (2026)**

| Inducteur | Parcs éoliens | Centrales solaires | Source |
|---|---|---|---|
| Puissance installée | 1 000 MW | 400 MW | inventaire technique des installations |
| Sites raccordés au centre de conduite | 64 parcs | 38 centrales | inventaire des liaisons |
| Machines supervisées | 420 éoliennes | 2 000 onduleurs | systèmes de supervision |
| Alarmes reçues par le centre de conduite | 180 000 | 20 000 | plateforme de supervision et systèmes des centrales |
| Utilisateurs des applications | 520 salariés d'ESTRAVENT, toutes directions confondues ; les sociétés de projet n'ont aucun salarié | | annuaire de la DSI |

**D. Ce que nos chiffres ne montrent pas**
- Les 150 techniciens de maintenance passent chacun environ trois heures par semaine à exporter des données des portails des constructeurs et des systèmes des centrales, puis à les recopier dans des tableurs pour préparer leurs interventions.
- Chaque matin, deux opérateurs du centre de conduite passent deux heures à recopier dans un tableur les arrêts de la nuit, pour le point quotidien de la direction de l'exploitation. Une trentaine de tableurs de ce genre circulent dans l'exploitation ; personne n'en tient la liste.
- En 2026, la direction de l'exploitation a acheté sur ses propres frais généraux des abonnements en ligne, des logiciels et des boîtiers de connexion pour environ 350 k€ ; ces achats ne figurent pas dans les dépenses du système d'information.

**E. Extrait du reporting annuel du système d'information (présenté au comité de direction en février 2027)**

| Nature des dépenses | 2026 (k€) |
|---|---|
| Personnel | 2 700 |
| Prestations externes | 2 300 |
| Licences et abonnements | 1 900 |
| Matériel | 1 100 |
| Télécommunications | 1 000 |
| **Total des dépenses du système d'information** | **9 000** |

Ce reporting est établi une fois par an, pour la préparation du budget. Il ne présente ni l'année précédente, ni objectif, ni la répartition entre l'informatique de gestion et l'informatique de conduite, ni aucun indicateur.

**F. Deux avis**

**M. Thibault ORLANCOURT, directeur financier** : « La clé du chiffre d'affaires a un mérite : elle est simple, et personne ne la discute. »

**Mme Gaëlle MONTREVIAU, directrice de l'exploitation** : « Si l'on refacture au nombre d'alarmes, nos parcs les plus anciens paieront pour les défauts de leurs machines. »

### ANNEXE 3.2 – Du comptage au chiffre d'affaires (note de M. Thibault ORLANCOURT, directeur financier, mai 2027)

**A. La chaîne de facturation des contrats d'achat direct.** En 2026, nos trois contrats d'achat direct ont porté sur 10 % de l'électricité vendue et sur environ 20 M€ de chiffre d'affaires ; le plan « ESTRAVENT 2031 » en suppose une quinzaine en 2031. Chaque contrat est adossé à deux à quatre parcs éoliens, et chaque facture mensuelle porte sur l'énergie livrée heure par heure.

1. **Comptage.** Au point de livraison de chaque parc, un compteur mesure l'énergie injectée sur le réseau. Le gestionnaire du réseau de distribution le relève et met à disposition chaque mois, sur son portail, un fichier par parc, avec la valeur de chaque heure : environ 720 valeurs par mois.
2. **Supervision.** La plateforme de supervision enregistre de son côté la production de chaque éolienne. Pour un même parc, elle dépasse normalement le comptage d'environ 2 %, du fait des pertes dans les câbles du parc.
3. **Calcul.** Chaque contrat a son tableur. Une chargée de facturation de la direction de l'énergie y copie les fichiers de comptage des parcs du contrat et calcule l'énergie livrée à l'industriel, heure par heure. Quand le fichier d'un parc manque ou n'est pas reconnu, elle reprend les données de la supervision. Elle a sous les yeux la production enregistrée par la supervision, mais aucun seuil d'écart n'est fixé, et rien n'oblige à expliquer un écart avant d'envoyer la facture.
4. **Facturation.** Le montant de la facture est saisi à la main dans le module de facturation du progiciel de gestion intégré, qui émet la facture ; le détail horaire est joint en PDF.
5. **Chiffre d'affaires.** Le chiffre d'affaires de chaque semestre, publié par ESTRAVENT, est établi à partir des factures du progiciel. La direction financière ne rapproche ni les volumes facturés des volumes comptés, ni le chiffre d'affaires des contrats de leurs tableurs.

**B. Ce qui s'est passé en 2026**
- En avril 2026, le fichier de comptage de mars d'un parc a été copié deux fois dans le tableur d'un contrat : l'énergie de ce parc a été comptée deux fois, et la facture a été majorée d'environ 300 k€. L'industriel l'a contestée ; elle a été refaite.
- De juin à août 2026, pour un parc d'un autre contrat, la production enregistrée par la supervision a dépassé de 8 % le comptage, sans que personne en cherche la cause. Le gestionnaire du réseau avait remplacé le compteur ; son fichier portait un nouveau numéro, que le tableur ne reconnaissait pas, et les volumes de ce parc ont été repris de la supervision pendant trois mois. L'industriel a contesté la facture d'août ; les trois factures ont été refaites.
- Dans le tableur du troisième contrat, une formule erronée, recopiée d'une ligne à l'autre, a omis pendant six mois une partie des heures livrées : l'industriel a été sous-facturé d'environ 150 k€. L'erreur n'a été découverte qu'en février 2027, après la publication du chiffre d'affaires de 2026.
- Les tableurs sont corrigés directement, sans historique. Les factures refaites ont remplacé les premières dans le dossier de chaque contrat, sans mention du motif. Pour une facture de 2026, nous ne savons plus dire quelles données ont servi, ni qui les a modifiées.
- Deux chargées de facturation préparent les factures horaires. L'une d'elles a construit les trois tableurs, et elle seule sait les modifier ou en créer un pour un nouveau contrat. Chacune prépare, vérifie et envoie ses propres factures ; personne ne relit ses calculs. Les tableurs sont rangés dans un dossier partagé auquel accèdent les 25 salariés de la direction de l'énergie.

**C. Les échelles retenues par le comité de direction**

| Niveau | Probabilité | Impact |
|---|---|---|
| 1 – faible | jamais constaté et peu plausible | erreur corrigée avant l'envoi de la facture, sans effet pour l'industriel |
| 2 – moyen | plausible, sans avoir été constaté chez ESTRAVENT | facture retardée, ou chiffre d'affaires impossible à justifier sans recherches longues, sans facture fausse envoyée |
| 3 – fort | constaté chez ESTRAVENT en 2026, ou certain en l'état | facture fausse envoyée à un industriel, ou chiffre d'affaires publié inexact |

Quand plusieurs niveaux conviennent, on retient le plus élevé. Le comité de direction traite en priorité les risques dont la probabilité et l'impact sont tous deux de niveau 3. Ni règle comptable, ni écriture, ni contrôle des comptes ne sont à traiter.

### ANNEXE 3.3 – Les accès à distance aux installations (constats de Mme Nadège QUILLEBRAND, responsable de la cellule supervision, et de M. Olivier SAUVERNAY, responsable de la DSI, mai 2027)

**A. Qui se connecte, et comment**
- Huit entreprises extérieures se connectent à distance aux installations : les constructeurs A, B et C, aux systèmes de supervision de leurs parcs, pour dépanner et régler leurs machines ; quatre sous-traitants de maintenance, aux systèmes des centrales solaires et des postes électriques des parcs ; l'ESN qui maintient la plateforme de supervision, à cette plateforme.
- Chacune utilise son propre outil de connexion à distance, soit huit outils différents. 110 boîtiers de connexion ont été installés dans les parcs et les centrales au fil des mises en service ; 20 boîtiers ne sont rattachés à aucune entreprise connue.
- Les huit entreprises disposent de 60 comptes d'accès, dont 50 sont partagés par tous les techniciens d'une même entreprise. La plupart des mots de passe n'ont jamais changé depuis la mise en service des installations.
- Les accès sont ouverts en permanence, jour et nuit ; le centre de conduite n'est pas prévenu des connexions.
- D'après les entreprises extérieures, il y a eu environ 9 000 connexions à distance en 2026. ESTRAVENT n'en conserve aucune trace : seuls les constructeurs gardent les journaux de leurs systèmes.
- Les postes du centre de conduite servent aussi à la messagerie et à la navigation sur internet. Ils sont reliés au réseau de bureautique du siège, comme les serveurs de la plateforme de supervision.
- Plusieurs systèmes de supervision des parcs les plus anciens fonctionnent sur des systèmes d'exploitation qui ne reçoivent plus de correctifs de sécurité ; les constructeurs n'en autorisent aucune modification.

**B. Deux événements**
- En septembre 2026, le compte partagé d'un sous-traitant de maintenance, dont le contrat avait pris fin en juin et qui n'intervenait que sur les postes électriques, a servi à se connecter un dimanche, à 3 heures, au système de supervision d'un parc du constructeur C, pendant 40 minutes. Aucune commande n'a été envoyée aux éoliennes. C'est le constructeur C qui l'a signalé, trois semaines plus tard ; on ne sait toujours pas qui s'est connecté.
- En février 2027, selon l'écho qu'en a donné la presse, un autre producteur d'électricité a vu plusieurs de ses parcs arrêtés à distance pendant deux jours ; l'attaque serait passée par l'accès d'un prestataire de maintenance.

**C. L'organisation de la sécurité aujourd'hui**
- La politique de sécurité de la DSI, approuvée par le comité de direction en 2022, ne couvre que l'informatique de gestion ; M. SAUVERNAY en a la charge. L'informatique de conduite n'a ni politique de sécurité, ni analyse des risques.
- Personne n'est chargé de la sécurité de l'informatique de conduite : la cellule supervision en traite les incidents « quand ils se présentent ».
- Les contrats des constructeurs, des sous-traitants et de l'ESN ne disent rien de la sécurité des accès à distance.
- Le centre de conduite fonctionne jour et nuit ; c'est lui qui décide d'arrêter ou de redémarrer une installation.

**D. Ce qu'en disent les responsables**

**Mme Gaëlle MONTREVIAU, directrice de l'exploitation** : « Si nous fermons les accès, les constructeurs ne pourront plus dépanner la nuit, et la disponibilité baissera. Or le plan nous demande 97 %. »

**M. Yannick FERRASSOT, responsable du centre de conduite** : « Mes opérateurs voient tout ce qui se passe sur les machines, mais pas qui s'y connecte. »

Aucun paramétrage d'équipement ni aucun essai technique n'est attendu ; aucune procédure de choix d'un fournisseur n'est à organiser, et aucune analyse juridique des contrats n'est demandée.

### ANNEXE 3.4 – La demande du comité d'audit (courriel de M. Bernard ESCOLIÈRE, président du comité d'audit, mai 2027)

« Le comité d'audit a examiné, le 12 mai, l'incident de septembre 2026 et l'attaque subie par un autre producteur. Il a pris acte de votre intention de mettre en place, d'ici la fin de 2027, de nouvelles règles pour les accès à distance des entreprises extérieures.

Le comité souhaite qu'un auditeur des systèmes d'information externe en vérifie l'application six mois après leur mise en place, et lui en rende compte. Avant de lancer cette mission, il voudrait savoir sur quels critères l'auditeur jugera ces accès, sur quels éléments il s'appuiera, et à quoi il faudra veiller.

Je rappelle nos contraintes : nos installations produisent jour et nuit, et aucune ne doit être arrêtée pour l'audit ; les systèmes des constructeurs ne peuvent pas être modifiés ; huit entreprises extérieures et 102 sites, dans quatre régions, sont concernés ; les journaux des systèmes des parcs sont chez les constructeurs. Le choix de l'auditeur viendra ensuite. »

Ni la démarche détaillée de l'audit, ni son calendrier, ni aucun essai technique ne sont demandés.

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Sécurité de l'information | ISO/IEC 27001:2022 | norme d'exigences d'un système de management de la sécurité de l'information, fondé sur l'appréciation et le traitement des risques, dans une logique d'amélioration continue ; son annexe A compte 93 mesures en quatre thèmes (organisationnelles, liées aux personnes, physiques, technologiques) |
| Gestion des risques | ISO/IEC 27005:2022 | lignes directrices de gestion des risques liés à la sécurité de l'information : établir le contexte, identifier, analyser, évaluer puis traiter les risques, et les surveiller ; quatre options de traitement : réduire le risque, l'accepter, l'éviter ou le transférer ; elle ne prescrit pas de méthode particulière |
| Bonnes pratiques | Guide d'hygiène informatique de l'ANSSI, version de 2017 | guide de 42 mesures de sécurité, en niveau standard et renforcé, qui portent notamment sur l'authentification, les mises à jour, le cloisonnement des réseaux, les appareils nomades et les sauvegardes |
| Architecture de confiance | Le modèle Zero Trust, avis de l'ANSSI (2021) | modèle d'architecture, et non un produit : aucune confiance n'est accordée d'office selon la place sur le réseau ; chaque accès est authentifié, autorisé et vérifié selon le contexte ; démarche progressive, qui ne remplace pas la défense en profondeur |
| Gouvernance et audit du système d'information | COBIT 2019 (ISACA) | cadre de gouvernance et de management de l'information et des technologies, ni norme ni logiciel ; 40 objectifs de gouvernance et de management en cinq domaines ; il peut servir de référentiel à un audit du système d'information |

### Travail à faire

Les dépenses du système d'information sont refacturées aux sociétés de projet selon une clé qui ne dit rien de leur usage, et le reporting n'en dit guère plus. La facturation des contrats d'achat direct, appelés à se multiplier, repose sur des tableurs qui ont produit trois erreurs en 2026. Huit entreprises extérieures se connectent jour et nuit aux installations avec des comptes partagés, et le compte d'un sous-traitant parti a servi en 2026. Mme VARLAMBERT vous demande de revoir le pilotage et la refacturation des coûts du système d'information, de fiabiliser la chaîne qui va du comptage au chiffre d'affaires, de fonder la sécurité de l'informatique de conduite et des accès à distance, et de répondre au comité d'audit. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – Les coûts du système d'information et leur refacturation aux sociétés de projet (3,5 points)**

a) Après avoir présenté les fondamentaux du contrôle de gestion appliqué au système d'information (centre de coûts ou centre de services, refacturation interne, inducteurs), critiquez par trois arguments tirés de l'annexe 3.1 la refacturation actuelle des dépenses du système d'information aux sociétés de projet. Proposez ensuite une répartition fondée sur des inducteurs : associez un inducteur, ou l'absence de refacturation, à chacun des ensembles de services de l'annexe 3.1 A, et justifiez le choix de deux de ces inducteurs. Aucun calcul de répartition n'est demandé.

b) Relevez, à partir de l'annexe 3.1 D, trois coûts cachés du système d'information de conduite. Pour chacun, expliquez pourquoi il échappe au suivi actuel et comment le mesurer.

c) Proposez trois améliorations du reporting annuel des coûts du système d'information (annexe 3.1 E), portant respectivement sur les comparaisons, les objectifs et la revue périodique. Deux d'entre elles s'appuient sur un indicateur, précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

**3.2 – La fiabilité de la chaîne du comptage au chiffre d'affaires (3,5 points)**

a) Après avoir présenté la typologie des risques liés aux systèmes d'information, suivez la chaîne « comptage → facturation → chiffre d'affaires » de l'annexe 3.2 étape par étape et retenez-y quatre risques, chacun formulé comme un événement redouté et rattaché à l'étape où il naît. Indiquez la catégorie de chacun dans cette typologie, puis cotez leur probabilité et leur impact selon les échelles de l'annexe 3.2 C.

b) Après avoir défini la fiabilisation d'un système d'information de gestion, choisissez, pour les deux risques les plus graves, un traitement parmi les options de l'ISO/IEC 27005 (annexe 3.5), puis proposez, pour chacun d'eux, deux contrôles qui fiabilisent les données de facturation et le chiffre d'affaires publié. Pour chaque contrôle, précisez sa nature (préventive ou détective, manuelle ou automatisée), son responsable et ce qu'il garantit. Indiquez enfin comment rendre les corrections traçables et réduire la dépendance envers une seule personne. Aucune règle comptable ni aucune écriture n'est attendue.

**3.3 – La sécurité de l'informatique de conduite et des accès à distance (3,5 points)**

a) Après avoir défini une politique de sécurité du système d'information fondée sur l'analyse des risques, présentez, à partir de l'annexe 3.3, quatre principes de la politique de sécurité de l'informatique de conduite d'ESTRAVENT, en montrant en quoi ils se distinguent de ceux de l'informatique de gestion. Précisez ensuite le rôle que doivent y tenir la présidente-directrice générale, vous-même, la directrice de l'exploitation, la responsable de la cellule supervision, le responsable du centre de conduite et les entreprises extérieures.

b) Après avoir présenté le modèle Zero Trust, proposez quatre mesures d'architecture de confiance pour les accès à distance des entreprises extérieures, portant respectivement sur l'authentification et les comptes, le point d'accès aux installations, la séparation entre l'informatique de conduite et la bureautique, l'ouverture et la traçabilité des accès. Pour chacune, précisez le constat de l'annexe 3.3 auquel elle répond et le risque qu'elle traite. Répondez enfin à la crainte de Mme MONTREVIAU. Aucun paramétrage d'équipement ni aucun essai technique n'est attendu.

**3.4 – La réponse au comité d'audit (2,5 points)**

a) Après avoir défini un critère d'appréciation et un élément probant en audit des systèmes d'information, présentez à M. ESCOLIÈRE trois critères sur lesquels l'auditeur jugera les accès à distance — la sécurité, la fiabilité des traces et la conformité à la politique de sécurité — en indiquant pour chacun ce qui sera attendu et un élément probant que l'auditeur demandera.

b) Présentez trois points de vigilance propres à l'audit des accès à distance d'installations qui produisent jour et nuit, en indiquant pour chacun la manière d'y répondre. La démarche détaillée de l'audit et son calendrier ne sont pas demandés.
