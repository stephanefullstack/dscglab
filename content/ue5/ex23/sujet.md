# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 23

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES COMMANDES ET DES MISSIONS (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 8, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. QUENTALIS Emploi est une entreprise de travail temporaire indépendante dont le siège est à Amiens. Fondée en 1994 par M. Arnaud VERQUELLE, qui la préside toujours, elle est constituée en société par actions simplifiée, détenue à 70 % par la famille fondatrice et à 30 % par vingt-cinq cadres et directeurs d'agence. Elle exploite un réseau de 46 agences en Hauts-de-France et en Normandie, qui délèguent des intérimaires auprès d'environ 3 200 entreprises clientes de l'industrie, de la logistique, du bâtiment et du tertiaire ; un centre de services installé à Amiens assure la paie des intérimaires, la facturation et la relation avec les intérimaires. QUENTALIS Emploi emploie 310 salariés permanents et a délégué en 2026 environ 19 000 intérimaires différents, soit 5 800 personnes en équivalent temps plein. Son chiffre d'affaires de 2026 s'élève à 290 millions d'euros ; 3,5 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « QUENTALIS 2030 », adopté par le comité de direction en décembre 2026, fixe trois priorités : défendre et moderniser le modèle d'agence de proximité face aux plateformes numériques de mise en relation ; mieux exploiter les données des commandes, des missions et des intérimaires pour servir plus vite et plus sûrement les clients ; sécuriser le système d'information, transmettre les savoir-faire des équipes et réduire l'empreinte du numérique. La directrice générale, Mme Nadia BRÉQUEMONT, en rend compte chaque trimestre au président.

Vous êtes contrôleur de gestion de QUENTALIS Emploi depuis 2025, rattaché à la directrice administrative et financière, et chargé du pilotage économique du système d'information et des projets de transformation. Mme BRÉQUEMONT vous demande trois travaux : éclairer la stratégie du système d'information et en piloter les coûts (dossier 1) ; organiser et exploiter les données des commandes et des missions (dossier 2) ; sécuriser le système d'information du réseau, transmettre les savoir-faire et rendre le numérique plus responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de QUENTALIS Emploi et chiffres clés

QUENTALIS Emploi est une société par actions simplifiée, entreprise de travail temporaire indépendante fondée en 1994, dont le siège est à Amiens. Elle est détenue à 70 % par la famille fondatrice et à 30 % par vingt-cinq cadres et directeurs d'agence. Ses agences recrutent des intérimaires et les délèguent auprès d'entreprises clientes ; le centre de services d'Amiens établit la paie des intérimaires et la facturation des clients et répond aux questions des intérimaires. L'exercice social coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires | 290 M€ : industrie 40 % (116 M€), logistique 30 % (87 M€), bâtiment 20 % (58 M€), tertiaire 10 % (29 M€) |
| Clients | environ 3 200 entreprises clientes, dont une trentaine de grands comptes qui représentent environ 35 % du chiffre d'affaires |
| Intérimaires et candidats | environ 19 000 intérimaires différents délégués dans l'année, soit 5 800 personnes en équivalent temps plein ; environ 80 000 candidats inscrits dans le fichier |
| Réseau | 46 agences en Hauts-de-France et en Normandie ; un centre de services à Amiens ; le siège à Amiens |
| Effectif permanent | 310 salariés : environ 200 dans les agences (directeurs d'agence, chargés de recrutement, assistants), 70 au centre de services (paie des intérimaires, facturation, relation avec les intérimaires), 40 au siège, dont une équipe informatique de 9 personnes ; forte rotation des chargés de recrutement |
| Système d'information | un logiciel de gestion du travail temporaire, en mode SaaS, fourni par un éditeur spécialisé (commandes des clients, contrats de mission, relevés d'heures, paie des intérimaires, facturation) ; un portail et une application mobile des intérimaires ; un portail des clients |
| Budget du système d'information | 3,5 M€ (environ 1,2 % du chiffre d'affaires) |
| Plan « QUENTALIS 2030 » (adopté en décembre 2026) | défendre et moderniser le modèle d'agence de proximité face aux plateformes numériques de mise en relation ; mieux exploiter les données des commandes, des missions et des intérimaires pour servir plus vite et plus sûrement les clients ; sécuriser le système d'information, transmettre les savoir-faire des équipes et réduire l'empreinte du numérique |

**Organigramme simplifié (mars 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Présidence | président fondateur | M. Arnaud VERQUELLE |
| Direction générale | directrice générale, qui porte le plan « QUENTALIS 2030 » et anime le comité de direction | Mme Nadia BRÉQUEMONT |
| Rattaché à la directrice générale | directeur du réseau et des agences (46 directeurs d'agence) | M. Julien HAVERCQ |
| Rattaché à la directrice générale | directeur commercial et des grands comptes | M. Stéphane DUQUESNEL |
| Rattachée à la directrice générale | responsable du centre de services (paie des intérimaires, facturation, relation avec les intérimaires) | Mme Aurélie CAMBRELIN |
| Rattachée à la directrice générale | directrice administrative et financière (comptabilité, contrôle de gestion, juridique, achats) | Mme Claire MAUBRECQ |
| Rattaché à la directrice administrative et financière | contrôleur de gestion | vous |
| Rattaché à la directrice générale | directeur des systèmes d'information (équipe informatique de 9 personnes) | M. Thomas ROUVELIN |
| Rattachée à la directrice générale | responsable des ressources humaines des salariés permanents | Mme Virginie DORVELLE |

Le comité de direction réunit chaque mois la directrice générale et les six responsables qui lui sont rattachés.

### ANNEXE 2.1 – Les données des commandes et des missions (note de M. Thomas ROUVELIN, directeur des systèmes d'information, février 2027)

**A. D'où viennent nos données (volumes de 2026)**

| Source | Données | Volume 2026 | Forme |
|---|---|---|---|
| Logiciel de gestion du travail temporaire (SaaS) | commandes des clients, saisies par les agences (90 %) ou par les clients sur le portail des clients (10 %) | 100 milliers de commandes | données structurées |
| | contrats de mission, renouvellements compris | 140 milliers | données structurées |
| | relevés d'heures hebdomadaires | 300 milliers | données structurées, après saisie ou validation |
| | factures | 60 milliers | données structurées |
| Portail et application des intérimaires | fiches des candidats (identité, coordonnées, métiers recherchés, qualifications), saisies par les candidats ou par les agences | 80 milliers de fiches | données structurées |
| | documents déposés (pièces d'identité, diplômes, habilitations, curriculum vitae) | 150 milliers de fichiers | images et documents |
| Fichiers tenus par les agences | tableurs de suivi des commandes non pourvues, tenus par 30 agences sur 46, chacune avec ses colonnes | environ 12 milliers de lignes | tableurs, formats propres à chaque agence |
| | notes sur les intérimaires (« fiable », « à ne plus proposer chez tel client », disponibilités) | environ 40 milliers de notes | texte libre, dans des tableurs ou dans un champ de commentaire du logiciel |

Les disponibilités des intérimaires ne sont saisies nulle part de manière structurée : les chargés de recrutement les notent après chaque appel, chacun à sa façon.

**B. Les relevés d'heures des grands comptes**

La trentaine de grands comptes nous transmettent environ 100 milliers des 300 milliers de relevés d'heures de l'année.

| Mode de transmission | Grands comptes | Relevés d'heures 2026 | Traitement au centre de services |
|---|---|---|---|
| Courriel avec un tableur ou un PDF, dans la présentation propre au client | 12 | 35 milliers | ressaisie dans le logiciel de gestion |
| Fichier extrait du logiciel de gestion des temps du client, dans son format propre, déposé sur un espace d'échange | 10 | 35 milliers | retraitement par une macro différente pour chaque client, puis contrôle |
| Saisie par le client sur le portail des clients | 7 | 20 milliers | aucune ressaisie |
| Échange automatisé entre le logiciel de gestion des temps du client et notre logiciel de gestion, par une interface de programmation (API) | 1 | 10 milliers | aucune ressaisie |
| **Total** | **30** | **100 milliers** | |

Trois personnes du centre de services consacrent l'essentiel de leur temps à ces ressaisies et retraitements. En 2026, 1 500 factures des grands comptes ont été corrigées par un avoir à la suite d'une erreur sur les heures ; chaque changement de présentation d'un fichier par un client oblige à refaire sa macro. Le grand compte relié par API l'a demandé lui-même en 2025 ; trois autres ont proposé en 2026 d'ouvrir le même échange. Notre logiciel de gestion dispose d'une API documentée et accepte l'import de relevés d'heures dans un format ouvert et standardisé, publié par l'éditeur.

**C. Constats sur la qualité des données**

1. **« Commande pourvue »** : chaque agence a sa définition. Certaines comptent une commande comme pourvue dès qu'un candidat est proposé au client, d'autres à la signature du contrat de mission, d'autres seulement si l'intérimaire est présent le premier jour. Une commande de dix caristes dont huit postes sont occupés est « pourvue » dans certaines agences, « non pourvue » dans d'autres. Les commandes annulées par le client sont tantôt exclues, tantôt comptées comme non pourvues.
2. **Commandes non saisies** : environ un tiers des lignes des tableurs de suivi des commandes non pourvues, soit 4 milliers, correspondent à des commandes reçues par téléphone qui n'ont jamais été saisies dans le logiciel de gestion. La date et l'heure de réception d'une commande ne sont enregistrées que si l'assistant la saisit dès l'appel, ce qui n'est pas le cas d'environ 40 % des commandes.
3. **Codes métiers** : le logiciel de gestion propose une liste de 400 codes métiers ; les agences y ont ajouté 250 codes locaux. Le métier de cariste apparaît sous quatorze libellés différents, et 25 % des commandes portent le code « autre ».
4. **Doublons de candidats** : un candidat inscrit sur le portail puis reçu en agence, ou inscrit dans deux agences, a souvent deux fiches ; nous estimons les doublons à environ 8 000 fiches sur 80 000 (10 %). Environ 24 000 fiches (30 %) n'ont donné lieu à aucune mission ni à aucun contact depuis plus de deux ans.
5. **Restitution** : chaque mois, l'équipe informatique extrait du logiciel de gestion un fichier qu'elle adresse au directeur du réseau et des agences ; chaque agence calcule en outre son taux de service dans son propre tableur. Le comité de direction reçoit le taux du réseau environ trois semaines après la fin du mois.

### ANNEXE 2.2 – Le taux de service en 2026

Le taux de service rapporte les commandes pourvues aux commandes reçues. Chiffres arrondis, établis à partir du logiciel de gestion selon la définition propre à chaque agence.

**A. Par secteur des clients**

| Secteur | Commandes reçues 2026 | Commandes pourvues 2026 | Taux de service 2025 → 2026 | Délai moyen de pourvoi 2026 | Part des missions renouvelées 2026 | Part des intérimaires délégués de nouveau dans les trois mois 2026 |
|---|---|---|---|---|---|---|
| Industrie | 30 milliers | 27 milliers | 90 % → 90 % | 2 jours | 50 % | 70 % |
| Logistique | 40 milliers | 32 milliers | 87 % → 80 % | 1 jour | 30 % | 50 % |
| Bâtiment | 20 milliers | 18 milliers | 89 % → 90 % | 3 jours | 40 % | 60 % |
| Tertiaire | 10 milliers | 8 milliers | 82 % → 80 % | 4 jours | 30 % | 50 % |
| **Réseau** | **100 milliers** | **85 milliers** | **88 % → 85 %** | **2 jours** | **38 %** | **58 %** |

**B. Trois agences**

| Agence | Profil | Commandes reçues 2026 | Commandes pourvues 2026 | Taux de service 2025 → 2026 | Délai moyen de pourvoi 2026 | Part des missions renouvelées 2026 | Part des intérimaires délégués de nouveau dans les trois mois 2026 | Définition de la commande pourvue appliquée par l'agence |
|---|---|---|---|---|---|---|---|---|
| Lens | logistique, 70 % de ses commandes | 4 000 | 3 000 | 82 % → 75 % | 0,5 jour | 25 % | 40 % | intérimaire présent le premier jour ; commande partiellement pourvue comptée comme non pourvue |
| Évreux | industrie, 60 % de ses commandes | 2 000 | 1 900 | 94 % → 95 % | 3 jours | 60 % | 80 % | candidat proposé au client ; commandes annulées exclues |
| Saint-Quentin | généraliste | 2 500 | 2 250 | 90 % → 90 % | 2 jours | 40 % | 60 % | contrat de mission signé ; commandes non pourvues suivies dans un tableur, en partie non saisies dans le logiciel |

**C. Deux lectures (comité de direction de février 2027)**

**M. Julien HAVERCQ, directeur du réseau et des agences** : « Nous avons perdu trois points en un an. Évreux est à 95 %, Lens à 75 % : la méthode d'Évreux doit s'appliquer partout. Je propose de fixer à chaque agence un objectif de 90 % dès le second semestre et de publier chaque mois le classement des agences. »

**Mme Coralie DESVRAINE, directrice de l'agence de Lens** : « À Lens, une commande n'est pourvue que si l'intérimaire est là le premier matin, et une commande de dix caristes dont nous plaçons huit compte comme non pourvue ; à Évreux, proposer un nom suffit. Nos clients logisticiens commandent la veille à 17 heures pour le lendemain à 5 heures. Et quand nos bons intérimaires ne sont pas rappelés dans la semaine qui suit la fin de leur mission, nous les perdons. Un classement établi sur ces chiffres découragera les agences qui mesurent honnêtement. »

### ANNEXE 2.3 – Le projet « Pilotage des missions » (note de cadrage de M. Thomas ROUVELIN, directeur des systèmes d'information, et de Mme Claire MAUBRECQ, directrice administrative et financière, mars 2027)

**A. Objectif**

Alimenter chaque nuit un dépôt de données commun à partir du logiciel de gestion, du portail des intérimaires et du portail des clients, pour produire :
- pour chaque agence, un tableau de bord hebdomadaire : commandes reçues et pourvues, taux de service, délai de pourvoi, commandes non pourvues par métier et par client ;
- pour la direction, un tableau de bord mensuel : taux de service par secteur, par agence et par grand compte, fidélisation des intérimaires.

Objectif du plan « QUENTALIS 2030 » : un taux de service de 90 % en 2028, mesuré de la même façon dans toutes les agences. Le comité de direction choisira l'architecture et l'hébergement en avril 2027.

**B. Deux options d'architecture (montants en milliers d'euros, hors temps interne)**

| | Option 1 – Entrepôt de données | Option 2 – Lac de données |
|---|---|---|
| Contenu | données structurées des trois applications, nettoyées et rapprochées selon des définitions communes avant leur chargement, historisées depuis 2024 | toutes les données, structurées ou non (fiches, documents et curriculum vitae, notes des agences, courriels des clients), conservées brutes, sans transformation à l'entrée |
| Préparation des données | règles de transformation fixées une fois pour toutes, avant le chargement | préparation au moment de chaque analyse |
| Utilisateurs prévus | 46 directeurs d'agence et leurs chargés de recrutement, comité de direction, contrôle de gestion | un analyste de données, à recruter (QUENTALIS Emploi n'en compte aucun) |
| Mise en place | 120 : consultant décisionnel (60 jours à 1 000 €), raccordement des trois applications (30), licences de l'outil de restitution la première année (20), formation (10) | 80 |
| Fonctionnement annuel, hors hébergement | 30 : licences de l'outil de restitution (20), maintenance des flux de chargement (10) | 90 : licences (20), analyste de données (70) |
| Hébergement annuel | 40 (H1) ou 60 (H2) | 30 (H1) ou 50 (H2) |

**M. Stéphane DUQUESNEL, directeur commercial et des grands comptes** : « Prenons le lac : gardons tout, curriculum vitae, notes et courriels compris. Nous ne savons pas encore ce que nous en ferons, mais un jour ces données vaudront de l'or. »

**C. Deux options d'hébergement**

| | H1 – Fournisseur de cloud public | H2 – Prestataire français |
|---|---|---|
| Fournisseur | grand fournisseur dont le siège est situé hors de l'Union européenne ; il reste soumis au droit de son pays d'origine, qui peut, dans certains cas, permettre aux autorités de ce pays de lui demander l'accès aux données qu'il héberge, y compris en Europe | prestataire dont le capital est majoritairement détenu en France ; offre qualifiée SecNumCloud |
| Localisation des données | centres de données situés dans l'Union européenne | centres de données situés en France |
| Services | nombreux services d'analyse intégrés, prêts à l'emploi | services d'analyse plus limités |
| Fin de contrat | export des données possible ; les traitements construits avec les services intégrés du fournisseur sont à reconstruire ailleurs | restitution des données et des traitements dans des formats ouverts, assistance comprise |

Données concernées : identité, coordonnées, qualifications et missions des candidats et des intérimaires ; commandes, tarifs et heures facturées des clients. Un grand compte de l'industrie aéronautique demande, depuis janvier 2027, que les données relatives à ses commandes soient hébergées par un prestataire qui ne relève pas d'un droit extérieur à l'Union européenne.

**D. Tâches, durées et ressources (option 1)**

| Tâche | Contenu | Durée | Ressources | Antériorités |
|---|---|---|---|---|
| A | Cadrage et dictionnaire des données (définitions communes, dont celle de la commande pourvue, liste unique des codes métiers) | 3 semaines | cheffe de projet, consultant, référents d'agence | — |
| B | Choix et mise en place de l'hébergement et des environnements | 4 semaines | ingénieur de données de l'équipe informatique | — |
| C | Nettoyage des données sources (doublons de candidats, codes métiers, commandes des tableurs) | 6 semaines | référents d'agence, assistants du centre de services | A |
| D | Construction des flux de collecte et de chargement | 5 semaines | ingénieur de données, consultant | A, B |
| E | Conception des tableaux de bord des agences et de la direction | 3 semaines | consultant, référents d'agence | A |
| F | Recette des données et des tableaux de bord dans six agences pilotes | 3 semaines | référents d'agence, cheffe de projet | C, D, E |
| G | Formation des directeurs d'agence et des chargés de recrutement | 2 semaines | référents d'agence, cheffe de projet | F |
| H | Mise en production dans tout le réseau | 1 semaine | équipe informatique | G |

Ressources et contraintes :
- la cheffe de projet est une personne de l'équipe informatique, à plein temps sur le projet ; l'ingénieur de données aussi ; les sept autres personnes de l'équipe continuent à faire fonctionner l'existant ;
- les six référents sont des directeurs d'agence ou des chargés de recrutement des agences pilotes ; ils consacrent une journée par semaine au projet et ne peuvent pas mener deux tâches en même temps ; ils ne sont pas disponibles du lundi 5 juillet au vendredi 27 août 2027, en pleine période de remplacements d'été ;
- aucune mise en production n'est possible du 1er juillet au 31 août ni du 15 novembre au 31 décembre, périodes de pointe de l'activité ;
- le projet commence le lundi 3 mai 2027.

Première estimation de l'équipe informatique : « En enchaînant les tâches au plus tôt, le projet dure 15 semaines : mise en production à la mi-août 2027. »

**E. Coûts du projet (option 1)**

Outre les 120 k€ de prestations externes (B), le temps de l'équipe informatique consacré au projet est valorisé à 80 k€ et celui des référents d'agence à 30 k€ ; la directrice administrative et financière demande une réserve pour aléas de 20 k€. L'hébergement est imputé au budget courant du système d'information dès sa mise en place ; il ne fait pas partie de l'enveloppe du projet. L'enveloppe des projets du budget du système d'information de 2027 est de 500 k€.

**F. Exigences de qualité retenues par le comité de direction**

- données de la veille disponibles chaque matin à 7 heures ;
- au plus 1 % de lignes rejetées à chaque chargement, chaque rejet étant expliqué ;
- un taux de service calculé selon la seule définition du dictionnaire, identique dans toutes les restitutions ;
- un nombre de commandes du mois identique dans l'entrepôt et dans le logiciel de gestion ;
- chaque directeur d'agence ne voit que les données de son agence et les totaux du réseau ;
- trois mois après la mise en production, 90 % des directeurs d'agence consultent leur tableau de bord chaque semaine.

**G. Durées de conservation fixées par la politique interne de QUENTALIS Emploi**

Établies en 2024 avec l'avocat de l'entreprise et le délégué à la protection des données ; elles ne sont pas à discuter.

| Données | Durée et sort final |
|---|---|
| Fiche et documents d'un candidat jamais délégué | deux ans après le dernier contact, puis suppression |
| Fiche et documents d'un intérimaire | en base active tant qu'il est délégué et pendant deux ans après sa dernière mission ; puis suppression de la fiche et des documents qui ne sont pas liés à une mission |
| Contrats de mission et relevés d'heures | archivés, avec un accès réservé au centre de services, jusqu'à la fin de la cinquième année qui suit la fin de la mission, puis supprimés |
| Statistiques de l'entrepôt | conservées sans limite si elles ne permettent plus d'identifier une personne (agrégats par agence, métier, client et mois) |

Les notes des agences sur les intérimaires ne sont pas mentionnées dans la politique ; elles ne sont jamais supprimées.

### ANNEXE 2.4 – Repères sur les données et leur hébergement (au 31/12/2026)

| Texte ou référentiel | Repères utiles | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 du 27 avril 2016 (RGPD) | Les données personnelles sont collectées pour des finalités déterminées, limitées à ce qui est nécessaire au regard de ces finalités (minimisation) et conservées sous une forme permettant d'identifier les personnes pendant une durée qui n'excède pas celle nécessaire à ces finalités. Le prestataire qui traite des données pour le compte de l'entreprise (sous-traitant) agit sur ses instructions, dans le cadre d'un contrat écrit (article 28). | Applicable depuis le 25/05/2018 |
| Règlement (UE) 2023/2854 (« Data Act ») | Organise notamment le changement de fournisseur de services d'informatique en nuage : portabilité des données, assistance à la sortie. | Applicable depuis le 12/09/2025 |
| SecNumCloud, version 3.2 (ANSSI) | Référentiel d'exigences qui permet de qualifier des offres de services d'informatique en nuage, y compris au regard de leur protection contre l'application de lois extra-européennes. | En vigueur |
| DAMA-DMBOK, 2e édition (2017), révision 2024 (DAMA International) | Référentiel de bonnes pratiques de gestion des données, organisé en onze domaines de connaissance autour de la gouvernance des données (dont la qualité des données, les métadonnées, les entrepôts de données et l'informatique décisionnelle). | En vigueur |

Aucune analyse juridique n'est attendue : les durées de conservation sont celles de l'annexe 2.3 G.

### Travail à faire

Mme BRÉQUEMONT veut que les données servent la deuxième priorité du plan « QUENTALIS 2030 » : servir plus vite et plus sûrement les clients. Avant la décision du comité de direction d'avril 2027, elle vous demande d'éclairer le choix de l'architecture et de l'hébergement du projet « Pilotage des missions », d'organiser la fiabilité des données et de leurs échanges, de porter un diagnostic sur le taux de service et de planifier le projet. Vous mobiliserez pour cela les annexes 1.1, 2.1, 2.2, 2.3 et 2.4 ainsi que vos connaissances professionnelles.

**2.1 – Entrepôt ou lac de données (2,5 points)**

a) Comparez l'entrepôt de données et le lac de données selon quatre critères : la finalité, la structuration des données, les utilisateurs et les coûts, en appliquant chaque critère aux deux options de l'annexe 2.3 B.

b) Recommandez, en la justifiant par trois besoins de QUENTALIS Emploi tirés des annexes, l'architecture à retenir pour le projet, puis répondez à la proposition de M. DUQUESNEL.

**2.2 – Fiabilité des données et échanges avec les grands comptes (2 points)**

a) Après avoir défini le dictionnaire de données, fixez ses rubriques (définition, règle de gestion ou formule, valeurs admises, source, propriétaire, fréquence de mise à jour) pour deux données clés du projet, la commande pourvue et le taux de service ; proposez ensuite trois règles de qualité, chacune rattachée à un constat de l'annexe 2.1 C, et désignez les responsables de la donnée (propriétaires et intendants).

b) Proposez l'organisation des échanges des relevés d'heures avec les grands comptes, en montrant l'intérêt des API et des formats ouverts par rapport à la situation de l'annexe 2.1 B, sur les plans technique et organisationnel. Aucun détail technique des échanges n'est attendu.

**2.3 – Chaîne de traitement et diagnostic du taux de service (4 points)**

a) Après avoir défini la chaîne de traitement des données, décrivez celle qui produira les tableaux de bord du projet, de la collecte à la restitution, puis indiquez, en le justifiant, le type d'outil décisionnel adapté à ces restitutions.

b) À partir de l'annexe 2.2, formulez un diagnostic argumenté du taux de service : trois constats, une hypothèse d'explication pour chacun et deux précautions de lecture, puis appréciez la proposition de M. HAVERCQ. Aucun calcul statistique n'est attendu.

c) Indiquez, en la justifiant, la méthode d'analyse (descriptive ou exploratoire) adaptée à chacun des deux besoins suivants : le suivi hebdomadaire des agences et la recherche des causes de la baisse du taux de service dans la logistique ; proposez ensuite deux représentations visuelles, l'une pour les directeurs d'agence, l'autre pour le comité de direction. Aucune manipulation d'outil n'est attendue.

**2.4 – Cycle de vie et hébergement des données (1,5 point)**

a) Présentez les cinq étapes du cycle de vie des données des candidats et des intérimaires (création, stockage, usage, archivage, suppression), en les appliquant aux durées de l'annexe 2.3 G, puis relevez deux écarts entre la pratique actuelle et ces durées, en indiquant leur conséquence pour le projet.

b) Après avoir défini la souveraineté numérique, appréciez les deux options d'hébergement de l'annexe 2.3 C selon trois critères (le droit applicable au prestataire, la dépendance et la réversibilité, le coût) et recommandez-en une. Aucune expertise technique des infrastructures n'est attendue.

**2.5 – Planification et risques du projet « Pilotage des missions » (3 points)**

a) À partir de l'annexe 2.3 D à F, planifiez le projet sous la forme d'un diagramme de Gantt simplifié en semaines : affectation des ressources, enchaînement des tâches, durée totale du travail et date de mise en production, quatre jalons datés ; critiquez la première estimation de l'équipe informatique, puis indiquez l'enveloppe de coûts du projet et la manière dont les exigences de qualité seront contrôlées avant la mise en production.

b) Identifiez trois risques du projet, en précisant pour chacun sa cause, son effet et son traitement.
