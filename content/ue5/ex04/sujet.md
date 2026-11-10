# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 4

**DOSSIER 1 – ALIGNER LA STRATÉGIE DU SI ET REFONDER LA GOUVERNANCE DE LA FONCTION INFORMATIQUE (15 points)**

Durée conseillée : 1 h 10 (15 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 1.2 – Plan « LORVANNE 2030 » et constats sur le système d'information

**A. Répartition des produits de l'exercice 2025-2026**

| Origine | Montant |
|---|---|
| Frais de scolarité | 46 M€ |
| Financement de l'apprentissage | 14 M€ |
| Formation des cadres | 5 M€ |
| Autres produits (partenariats d'entreprises, produits divers) | 3 M€ |
| **Total** | **68 M€** |

**B. Objectifs chiffrés du plan « LORVANNE 2030 » (conseil d'administration de juin 2026)**

| Objectif | Situation 2025-2026 | Cible 2029-2030 |
|---|---|---|
| Chiffre d'affaires de la formation des cadres | 5 M€, dont 0,3 M€ en ligne | 10 M€, dont 5 M€ en ligne |
| Apprentis | 1 450 | 2 000 |
| Universités partenaires à l'étranger accueillant des étudiants de l'école | 70 | 120 |
| Part des étudiants satisfaits de leur école (enquête annuelle) | 68 % | 85 % |
| dont part des étudiants satisfaits des démarches de candidature et d'inscription | 41 % | non fixée |
| Satisfaction des entreprises partenaires (employeurs d'apprentis, clients de la formation des cadres) | non mesurée | non fixée |

**C. Constats sur le système d'information (note de M. CORNAVIN à la directrice générale, février 2027)**
- Le dernier schéma directeur du système d'information couvrait les années 2016 à 2019 ; il n'a pas été renouvelé. Le plan « LORVANNE 2030 » ne comporte aucun volet consacré au système d'information.
- Les projets informatiques sont décidés campus par campus, sur le budget de chaque campus : en 2024, le campus de Besançon a souscrit seul un logiciel de gestion des relations avec les entreprises en mode SaaS ; en 2025, le campus de Chalon-sur-Saône a mis en ligne son propre formulaire de candidature, construit avec un outil gratuit de formulaires.
- Budget du système d'information de l'exercice 2025-2026, par entité : siège 1,7 M€ ; campus de Dijon 0,6 M€ ; campus de Besançon 0,4 M€ ; campus de Chalon-sur-Saône 0,2 M€. Les dépenses informatiques des campus sont enregistrées dans leurs budgets de fonctionnement et ne sont consolidées qu'à la clôture de l'exercice.
- Sur ces 2,9 M€, 2,5 M€ sont consacrés au fonctionnement de l'existant (personnel, licences, maintenance, matériel) et 0,4 M€ à des projets nouveaux.
- La plateforme pédagogique en ligne, hébergée au siège depuis 2014, arrive en fin de vie ; son remplacement fait l'objet d'un projet distinct. Un rançongiciel a paralysé le campus de Besançon pendant neuf jours en novembre 2026 ; l'audit de sécurité est conduit séparément.

**D. Technologies signalées à la directrice générale (veille informelle, 2026-2027)**

| Technologie | Description | Origine de la proposition |
|---|---|---|
| IA générative dans la pédagogie | assistant conversationnel de tutorat ouvert aux étudiants, qui répond à leurs questions sur les cours ; aide à la conception des supports de cours pour les enseignants | présentée à Mme FERRIOL lors d'un salon de l'enseignement supérieur ; deux écoles concurrentes l'annoncent dans leur communication |
| Plateforme de candidature et de recrutement en ligne des candidats | dossier de candidature unique en ligne pour tous les programmes et tous les campus, dépôt des pièces, prise de rendez-vous pour les entretiens, suivi de l'avancement par le candidat, paiement en ligne de l'acompte, proposée en mode SaaS par plusieurs éditeurs | demandée par les services des admissions des trois campus |
| Badges numériques | attestations numériques des compétences acquises, vérifiables en ligne et partageables par leur titulaire sur ses profils professionnels, délivrées à l'issue d'une formation courte ou d'un module | demandés par plusieurs entreprises clientes de la formation des cadres |

### ANNEXE 1.3 – Organisation de la fonction informatique et cartographie applicative simplifiée

**A. Organisation de la fonction informatique (avril 2027)**

| Équipe | Effectif | Rattachement hiérarchique | Missions |
|---|---|---|---|
| Informatique du siège | 6 | responsable informatique du siège, rattaché depuis 2025 au directeur administratif et financier | applications de gestion communes (comptabilité, paie, scolarité), plateforme pédagogique, site internet |
| Informatique du campus de Dijon | 7 | directeur du campus de Dijon | support des utilisateurs, salles de cours, serveurs et réseau du campus, outil de candidature du campus |
| Informatique du campus de Besançon | 5 | directrice du campus de Besançon | support des utilisateurs, salles de cours, serveurs et réseau du campus, seconde installation du progiciel de scolarité, logiciel de relations avec les entreprises |
| Informatique du campus de Chalon-sur-Saône | 3 | directeur du campus de Chalon-sur-Saône | support des utilisateurs, salles de cours, formulaire de candidature du campus |

Il n'existe ni catalogue des services informatiques, ni outil commun de suivi des demandes, ni règle commune d'achat de logiciels. Chaque campus gère son propre annuaire des comptes des utilisateurs.

**B. Cartographie applicative simplifiée**

| Domaine | Campus de Dijon | Campus de Besançon | Campus de Chalon-sur-Saône |
|---|---|---|---|
| Admissions (candidatures, épreuves, décisions) | application de candidature développée en interne en 2012 | dossiers reçus par courriel, suivis dans un tableur | formulaire en ligne gratuit (2025) et tableur |
| Scolarité (inscriptions, notes, diplômes) | progiciel de scolarité, installation du siège | seconde installation du même progiciel, dans une version plus ancienne, sur un serveur du campus | progiciel de scolarité, installation du siège |
| Plateforme pédagogique | plateforme commune, hébergée au siège depuis 2014 | plateforme commune | plateforme commune |
| Apprentissage et relations avec les entreprises | tableurs du service des relations entreprises | logiciel de gestion des relations avec les entreprises en SaaS (2024) | tableurs |
| Formation des cadres | catalogue publié sur le site internet ; inscriptions par formulaire et tableur, au siège | — | — |
| Finances et paie | progiciel comptable et de paie commun, au siège | progiciel commun | progiciel commun |

Aucun identifiant unique de l'étudiant n'existe : chaque application crée sa propre fiche, et un étudiant inscrit à Besançon reçoit un numéro différent de celui des deux autres campus.

**C. Processus « candidature – admission – inscription » (campagne 2026)**

1. Le candidat dépose son dossier selon les modalités du campus choisi (application de Dijon, courriel à Besançon, formulaire en ligne à Chalon-sur-Saône). Un candidat qui vise deux campus dépose deux dossiers.
2. Le service des admissions du campus contrôle les pièces, organise les épreuves et les entretiens par courriel, puis reporte les résultats dans son outil.
3. Le jury d'admission du campus statue ; la décision est notifiée au candidat par un courrier électronique rédigé à la main.
4. Le candidat admis verse un acompte par virement ; le service comptable du siège le rapproche des relevés bancaires et le saisit dans le progiciel comptable.
5. Le service de scolarité ressaisit l'identité et le programme de l'étudiant dans le progiciel de scolarité ; l'informatique du siège crée chaque semaine, à partir d'un fichier extrait du progiciel, les comptes de la plateforme pédagogique ; l'informatique du campus crée le compte dans l'annuaire du campus. Pour un apprenti, le service des relations entreprises ressaisit en outre l'étudiant et son employeur dans son propre outil.

| Mesure (campagne 2026) | Valeur |
|---|---|
| Candidatures reçues | 8 000, dont 900 déposées en double sur deux campus |
| Admissions prononcées | 3 000 |
| Inscriptions de nouveaux étudiants | 1 800 |
| Délai moyen entre le dépôt d'un dossier complet et la réponse au candidat | 5 semaines |
| Nombre de saisies de l'identité d'un nouvel étudiant | 4 (5 pour un apprenti) |
| Fiches d'étudiants en double ou erronées dans le progiciel de scolarité | 6 % |

### ANNEXE 1.4 – Témoignages (recueillis en mars 2027)

**Mme Agnès FERRIOL, directrice générale** : « Le conseil a adopté "LORVANNE 2030" ; je ne veux pas d'un grand chantier informatique de plus, je veux un système d'information au service du plan. J'ai découvert le logiciel de Besançon en signant une facture. Je veux savoir qui décide, et sur quels critères. Et à chaque salon, on me parle d'IA générative : nos concurrents l'affichent, nous ne pouvons pas rester en retrait. »

**M. Rémi VERCLOS, directeur du campus de Dijon** : « Mon équipe dépanne une salle de cours dans l'heure. Si l'on rapatrie tout au siège, mes enseignants attendront deux jours. Je veux bien des règles communes, pas une informatique lointaine. »

**Mme Hélène MARCOIRE, directrice du campus de Besançon** : « Le siège ne nous a jamais écoutés : nous avons acheté notre outil de relations avec les entreprises parce que les tableurs ne suffisaient plus pour nos 550 apprentis. Depuis novembre, on nous reproche notre autonomie ; mes informaticiens ont pourtant travaillé jour et nuit. »

**M. Karim SADOUNI, directeur du campus de Chalon-sur-Saône** : « Avec trois informaticiens, je n'ai personne pour les projets. Nos candidats nous écrivent pour savoir où en est leur dossier, et certains s'inscrivent ailleurs avant d'avoir reçu notre réponse. »

**Mme Laure ROUVIÈRE, directrice des programmes** : « Doubler la formation des cadres en ligne suppose qu'une entreprise puisse inscrire et payer en ligne ; aujourd'hui, quand elle inscrit dix cadres, nous saisissons dix fois la même commande. Ses responsables des ressources humaines nous demandent des preuves de compétences vérifiables, pas des attestations en papier. Quant à l'IA générative, une bonne partie de nos enseignants l'utilisent déjà avec leurs comptes personnels, sans aucune règle. »

**M. Antoine DELORMEAU, directeur administratif et financier** : « Je ne connais le coût informatique des campus qu'à la clôture. Le responsable informatique m'a été rattaché faute de mieux : je peux tenir un budget, pas porter une stratégie. Et presque tout l'argent sert à faire tourner l'existant. »

**M. Fabien CORNAVIN, responsable informatique du siège** : « J'assure l'intérim depuis 2025 sans aucune autorité sur les campus. J'apprends leurs projets quand ils me demandent d'ouvrir un accès ou de créer un échange de fichiers. On me demande à la fois de maintenir l'existant et de préparer la nouvelle plateforme pédagogique. Personne n'arbitre. »

### Travail à faire

Mme FERRIOL veut que le système d'information devienne un levier du plan « LORVANNE 2030 » et que la fonction informatique soit gouvernée comme une fonction de l'école, et non comme la somme des équipes de trois campus. Vous mobiliserez pour cela les annexes 1.1 à 1.4 ainsi que vos connaissances professionnelles.

**1.1 – Alignement stratégique du système d'information (3,5 points)**

a) Après avoir défini l'alignement stratégique du système d'information, présentez le modèle d'alignement stratégique de Henderson et Venkatraman et appliquez-le à l'Institut LORVANNE en caractérisant la situation de chacun de ses quatre domaines.

b) Identifiez trois zones de désalignement entre les objectifs du plan « LORVANNE 2030 » et le système d'information actuel, en précisant pour chacune l'objectif menacé et les faits des annexes qui la révèlent, puis indiquez la perspective d'alignement que l'école devrait suivre.

**1.2 – Schéma directeur et veille technologique (3,5 points)**

a) Après avoir défini le schéma directeur du système d'information, présentez les étapes de la démarche qui permettrait à l'Institut LORVANNE de l'élaborer en 2027.

b) Proposez trois axes prioritaires du schéma directeur pour les années 2027 à 2030, chacun relié à un objectif du plan « LORVANNE 2030 » et aux constats des annexes.

c) Après avoir précisé ce qu'est une veille technologique active, évaluez l'opportunité de l'une des trois technologies de l'annexe 1.2 pour l'Institut LORVANNE, au regard de ses besoins réels, et concluez.

**1.3 – Organisation et gouvernance de la fonction informatique (4,5 points)**

a) Caractérisez le modèle organisationnel actuel de la fonction informatique de l'Institut LORVANNE et deux de ses effets, puis comparez deux modèles cibles et recommandez l'un d'eux.

b) Après avoir défini la gouvernance du système d'information, proposez deux instances de gouvernance (composition, fréquence, décisions) et deux leviers pour apaiser les relations entre la future direction des systèmes d'information, la direction générale et les directions de campus.

**1.4 – Urbanisation et rationalisation du processus d'admission (3,5 points)**

a) Présentez les principes de l'urbanisation du système d'information et les quatre couches de sa cartographie (métier, fonctionnelle, applicative, infrastructure), en les illustrant par la situation de l'Institut LORVANNE.

b) Schématisez, en format libre, la cartographie cible du processus « candidature – admission – inscription », en faisant apparaître les acteurs et les étapes, les applications, le référentiel de l'étudiant et les échanges entre applications.

c) Montrez, en deux points, comment l'architecture cible rationalise ce processus, en assortissant chacun d'un indicateur (formule, source, fréquence, cible et axe du tableau de bord prospectif).
