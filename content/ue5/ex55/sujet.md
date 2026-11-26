# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 55

**DOSSIER 1 – PRÉPARER L'ÉVOLUTION DE LA STRATÉGIE ET DE L'ORGANISATION DU SYSTÈME D'INFORMATION, LA RENÉGOCIATION D'UN CONTRAT ET LA TRANSMISSION DES SAVOIRS (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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
