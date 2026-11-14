# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 18

**DOSSIER 3 – ÉVALUER LE PILOTE DE LA BASE DE CONNAISSANCES ET CONDUIRE SA GÉNÉRALISATION (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 3.1 – La connaissance technique du cabinet

*Note de Mme Sophie ESCARBEL et de M. Julien PRADONNET, experts du pôle technique, à Mme VARENNAT (février 2027)*

Le pôle technique, animé par M. François DUVERNAIL, associé, compte deux experts : l'une pour la fiscalité, l'autre pour la comptabilité et le droit des affaires. Il assure la veille et répond aux questions techniques des six bureaux.

**A. Où se trouve aujourd'hui la connaissance technique du cabinet**

| Source | Contenu | Constat |
|---|---|---|
| Dossiers partagés de chaque bureau | notes, modèles et tableaux de travail rédigés par les collaborateurs et les associés du bureau | six arborescences différentes, une par bureau ; les mêmes documents existent en plusieurs versions, sans date ni auteur ; personne ne sait laquelle est à jour |
| Notes internes du pôle technique | 300 notes rédigées depuis 2015, diffusées par courriel | jamais retirées ni mises à jour ; une partie porte sur des règles qui ont changé depuis |
| Réponses données par courriel | réponses des experts aux questions des bureaux | elles restent dans les boîtes de messagerie de l'expert et du demandeur ; personne d'autre ne peut les retrouver |
| Abonnements à deux bases documentaires d'éditeurs juridiques | codes, doctrine administrative, commentaires, modèles | 30 accès nominatifs, dont 20 à Poitiers ; la plupart des collaborateurs des autres bureaux n'y ont pas accès |
| Modèles de lettres de mission et de dossiers de travail | documents types utilisés pour chaque client | chaque bureau a sa propre version de chaque modèle |

**B. Les questions posées au pôle technique**

Nous recevons en moyenne 300 questions par mois, et jusqu'à 500 par mois de janvier à mai. Selon notre décompte, six questions sur dix portent sur un sujet que nous avons déjà traité pour un autre collaborateur, souvent d'un autre bureau. En période fiscale, nous répondons en trois jours en moyenne, et la veille passe au second plan.

**C. Une connaissance concentrée chez quelques associés**

Trois associés partiront à la retraite d'ici la fin de 2029, dont M. Jean-Pierre VERDALHAC, associé du bureau de Saintes, que les collaborateurs de tous les bureaux appellent pour les associations et les professions libérales. Ce qu'ils savent tient à l'expérience de nombreux cas particuliers : la manière de conduire un dossier difficile, ce qu'il faut vérifier en priorité, ce qui a déjà posé problème chez un client semblable. Leurs réponses ne sont écrites nulle part.

**D. Les outils existants**

- **Gestion électronique des documents (GED)**, en place depuis 2019 : elle conserve les documents des dossiers des clients selon un plan de classement par client et par exercice ; elle ne comporte aucun espace pour la documentation technique.
- **Intranet**, ouvert en 2018 : actualités du cabinet, annuaire, procédures administratives ; 25 % des salariés le consultent au moins une fois par mois ; ses pages techniques n'ont pas été mises à jour depuis 2022.
- **Forum interne**, ouvert en 2020 : 150 messages la première année, aucun depuis mars 2023 ; 40 questions y sont restées sans réponse.

### ANNEXE 3.2 – Le pilote « Base CORLANDEAU » et le projet de généralisation

**A. Le dispositif expérimenté (septembre 2026 – mars 2027)**

Mme VARENNAT a lancé en septembre 2026, dans les bureaux de Poitiers et de Niort, un pilote ouvert aux 70 collaborateurs et chefs de mission des deux bureaux (45 à Poitiers, 25 à Niort). Il réunit deux composants, fournis par la société de services numériques qui a construit le pilote :

1. **Une base de connaissances doctrinale** : des fiches rédigées par les deux experts du pôle technique à partir de leurs notes et de leurs réponses, selon un modèle commun (question, réponse, sources, auteur, date de validation). La base comptait 250 fiches en septembre 2026 et 400 en mars 2027. Aucune date de revue des fiches n'a été prévue.
2. **Un assistant de recherche documentaire fondé sur l'IA générative** : le collaborateur pose sa question en langage courant ; l'assistant répond en citant les fiches sur lesquelles il s'appuie. Lorsque aucune fiche ne répond à la question, il formule une réponse à partir des connaissances générales du modèle et le signale par une mention en bas de la réponse. L'assistant est un service en ligne sur abonnement, qui s'appuie sur le modèle généraliste d'un grand fournisseur ; il est accessible par une adresse distincte, avec un identifiant propre, et n'est relié ni à la GED, ni à l'intranet.

Le lancement a donné lieu à une présentation d'une heure dans chaque bureau. Une charte d'une page, remise à cette occasion, interdit de saisir dans l'assistant des données des clients. Aucun objectif chiffré n'a été fixé au lancement du pilote.

**B. Résultats du pilote**

| Donnée | Octobre 2026 | Mars 2027 |
|---|---|---|
| Collaborateurs ayant utilisé l'assistant au moins une fois dans le mois (sur 70) | 56 | 35 |
| Recherches effectuées dans le mois | 1 500 | 1 000 |
| Fiches dans la base | 280 | 400 |
| Fiches devenues inexactes après un changement de règle et non encore corrigées | 0 | 60 |
| Réponses jugées exactes par le pôle technique (50 réponses relues chaque mois) | 90 % | 80 % |
| Réponses ne citant aucune fiche (réponse tirée des connaissances générales du modèle) | 10 % | 20 % |
| Questions adressées au pôle technique par les deux bureaux | 250 en mars 2026 | 200 en mars 2027 |

Autres éléments recueillis :
- **Temps de recherche** : selon un questionnaire de janvier 2027, auquel 30 des 70 collaborateurs ont répondu, une recherche prenait en moyenne 30 minutes avant le pilote et en prend 10 avec l'assistant.
- **Contenu des questions** : sur 200 questions posées en février 2027 et relues par le responsable informatique, 30 contenaient le nom d'un client ou des montants tirés de son dossier.
- **Journaux** : le service conserve les questions et les réponses pendant 30 jours, puis les efface ; le cabinet n'en garde aucune copie.

**C. Le projet de généralisation aux six bureaux**

Si le comité des associés de juin 2027 en décide ainsi, le dispositif serait étendu, à partir de septembre 2027, aux quatre autres bureaux et à l'ensemble des 180 salariés. Le prestataire prévoit alors environ 3 000 questions par mois.

*Tâches et jalons envisagés*
1. Décision du comité des associés, au vu de l'audit du pilote (jalon, 24 juin 2027).
2. Rédaction du cahier des charges fonctionnel de la généralisation et choix du service d'IA (annexe 3.4 B).
3. Reprise des notes et des modèles des six bureaux : environ 2 000 documents à trier ; objectif de 800 fiches validées à la fin de 2027.
4. Raccordement de l'assistant à l'intranet et à la GED, connexion avec le compte habituel du cabinet, droits d'accès par bureau et par pôle.
5. Recette.
6. Formation des salariés et désignation d'un référent dans chaque bureau.
7. Mise en service dans les bureaux de La Rochelle, d'Angoulême, de Saintes et de Châtellerault.

*Contrainte fixée par le comité des associés* : aucune mise en service ni aucun changement de version d'un logiciel utilisé par les collaborateurs du 15 janvier au 31 mai, période des clôtures et des déclarations fiscales.

*Deux options de méthode proposées par le prestataire*

| | Option A – Cycle en V | Option B – Démarche agile |
|---|---|---|
| Déroulement | spécifications détaillées de l'ensemble des fonctions de juin à août ; réalisation de septembre à novembre ; recette globale en décembre ; formation des salariés en janvier ; mise en service simultanée dans les six bureaux en février 2028 | itérations de trois semaines dès juin ; mise en service dans un premier bureau en septembre, puis dans un bureau chaque mois ; nouvelles fonctions livrées à la fin de chaque itération, « y compris de janvier à mai, pour suivre les nouveautés fiscales » |
| Rôle du cabinet | valider les spécifications en août et la recette en décembre | un expert du pôle technique, responsable du produit, disponible deux jours par semaine pour classer les demandes par priorité et valider chaque livraison |
| Engagement du prestataire | prix forfaitaire, délai et contenu fixés au contrat | facturation au temps passé, contenu ajusté à chaque itération |

### ANNEXE 3.3 – Témoignages recueillis en avril 2027

**Mme Camille ROUSSELANGE, collaboratrice comptable, bureau de Poitiers** : « Pour une question courante, je trouve la réponse en cinq minutes au lieu d'une demi-heure, et je vois de quelle fiche elle vient. Mais en mars, l'assistant m'a donné un seuil qui avait changé en début d'année : la fiche n'avait pas été corrigée. Depuis, je vérifie tout, et pour un dossier sensible j'appelle directement Mme ESCARBEL. »

**M. Thomas BERLANDIN, chef de mission, bureau de Niort** : « Les plus jeunes s'en servent beaucoup. Les plus anciens préfèrent appeler un expert : c'est plus rapide, et l'on discute vraiment du dossier. De janvier à mai, personne n'a le temps d'apprendre un nouvel outil. Un collaborateur de mon équipe, malvoyant, travaille avec un logiciel de lecture d'écran : il n'arrive pas à utiliser l'assistant. Et je ne sais toujours pas si j'ai le droit d'y coller un extrait de dossier pour gagner du temps. »

**Mme Nadia LEFRANDIER, cheffe de mission, bureau d'Angoulême** : « Nous avons nos propres modèles et nos notes, qui marchent très bien. Je ne veux pas qu'une base conçue à Poitiers remplace ce que nous avons construit. Si je rédige une fiche, qui la relira, et est-ce que quelqu'un le saura ? »

**M. Jean-Pierre VERDALHAC, associé, bureau de Saintes** : « Tout écrire ? Une bonne part de ce que je sais tient à des cas particuliers. Je n'ai pas envie qu'une machine ressorte mes réponses hors de leur contexte. Je préfère transmettre en travaillant avec les plus jeunes sur de vrais dossiers. »

**Mme Sophie ESCARBEL et M. Julien PRADONNET, experts du pôle technique** : « Valider 400 fiches à deux, en plus des questions, n'est pas tenable : en début d'année, il a fallu reprendre 60 fiches en pleine période fiscale. Si chaque bureau écrit ses fiches et nous les envoie, nous serons submergés. Et nous ne voulons pas répondre d'une réponse de la machine que nous n'avons jamais relue. »

**M. Damien QUINTAREL, responsable informatique** : « Je ne sais pas où sont traitées les questions des collaborateurs, ni ce que le fournisseur du modèle en fait ; les journaux disparaissent au bout de 30 jours. L'assistant demande une connexion de plus. Pour six bureaux, il faudra quelqu'un pour administrer les droits et suivre le prestataire ; mon équipe de trois personnes n'en a pas le temps. »

### ANNEXE 3.4 – Préparation de l'audit post-implémentation

**A. La demande de Mme VARENNAT (courriel du 12 avril 2027)**

« Je proposerai au comité des associés du 24 juin 2027 de généraliser, ou non, la Base CORLANDEAU. Je vous demande auparavant un audit du pilote. Il portera sur la base de connaissances, sur l'assistant et sur le service d'IA qui le fait fonctionner, ainsi que sur l'organisation mise en place à Poitiers et à Niort : rédaction, validation et mise à jour des fiches, accompagnement des utilisateurs. Vous disposez de six semaines, du 19 avril au 31 mai. Vous rencontrerez les associés responsables des bureaux de Poitiers et de Niort, M. DUVERNAIL et les deux experts du pôle technique, M. QUINTAREL, le prestataire et des collaborateurs des deux bureaux. Je veux savoir si les réponses sont fiables, si les données de nos clients sont protégées, si l'outil est réellement utilisé, et à quelles conditions le généraliser. Je n'attends pas un rapport technique. »

**B. Le service d'IA de la généralisation : deux options (proposition du prestataire, avril 2027)**

Hypothèse : 3 000 questions par mois, 180 utilisateurs.

| | Option 1 – Modèle généraliste (celui du pilote) | Option 2 – Modèle plus petit, limité à la recherche documentaire |
|---|---|---|
| Fournisseur et hébergement | grand fournisseur dont le siège est hors de l'Union européenne ; questions traitées dans des centres de données situés hors de l'Union européenne ; questions conservées 30 jours par le fournisseur | fournisseur établi dans l'Union européenne ; centres de données situés en France ; questions effacées après la réponse |
| Fonctions | recherche dans les fiches avec citation des sources ; en outre, rédaction de courriers aux clients, résumés de dossiers, traductions | recherche dans les fiches avec citation des sources ; aucune autre fonction |
| Réponses exactes sur un jeu d'essai de 100 questions couvertes par une fiche, préparé par le pôle technique | 85 % | 85 % |
| Question sans fiche correspondante | réponse tirée des connaissances générales du modèle, signalée en bas de la réponse | aucune réponse ; l'assistant propose de transmettre la question au pôle technique |
| Consommation électrique annuelle estimée par le prestataire (méthode non communiquée) | 10 MWh | 2 MWh |
| Information publiée sur les centres de données | aucune donnée propre au service | consommation d'énergie et origine de l'électricité publiées chaque année |
| Coût | 50 k€ par an | 35 k€ par an, plus 15 k€ d'adaptation la première année |

**C. Repères au 31/12/2026**

| Référence | Contenu utile au dossier | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | L'organisation qui traite des données personnelles pour le compte d'une autre (le prestataire et le fournisseur du modèle pour le cabinet) le fait dans le cadre d'un contrat et en assure la sécurité. | Applicable depuis le 25/05/2018. |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser la maîtrise de l'IA de leur personnel (article 4, dans sa rédaction issue du règlement (UE) 2026/1744). | Obligation applicable depuis le 2 février 2025 ; rédaction modifiée en vigueur depuis le 27 juillet 2026. |

Aucune qualification de l'assistant au regard du règlement sur l'intelligence artificielle, ni aucune analyse juridique des données personnelles, des transferts de données hors de l'Union européenne ou des droits des éditeurs n'est attendue.

### Travail à faire

Mme VARENNAT doit proposer au comité des associés du 24 juin 2027 de généraliser, ou non, la Base CORLANDEAU. Elle attend de vous une stratégie de gestion des connaissances, l'audit du pilote, l'organisation du projet de généralisation, les conditions de l'appropriation du dispositif et un avis sur le service d'IA à retenir. Vous mobiliserez pour cela les annexes 1.1, 3.1, 3.2, 3.3 et 3.4 ainsi que vos connaissances professionnelles.

**3.1 – Stratégie de gestion des connaissances et environnement existant (2,5 points)**

a) Après avoir distingué connaissances explicites et connaissances tacites, proposez la stratégie de gestion des connaissances du cabinet en trois axes, en précisant pour chacun la connaissance qu'il vise et ce que la base et son assistant peuvent, ou ne peuvent pas, y apporter.

b) Proposez l'intégration de la base et de l'assistant dans l'environnement existant : pour chacun des quatre éléments suivants — la GED, l'intranet, le forum interne et les dossiers partagés des bureaux —, indiquez s'il doit être conservé, transformé ou abandonné, et justifiez votre choix par l'annexe 3.1.

**3.2 – Audit post-implémentation du pilote (3 points)**

a) Après avoir défini l'audit post-implémentation, présentez la démarche de l'audit du pilote demandé par Mme VARENNAT : objectifs, périmètre, étapes, livrables et calendrier, en tenant compte de la demande de l'annexe 3.4 A.

b) Définissez quatre critères d'appréciation du pilote — la fiabilité des réponses, la traçabilité des sources, la confidentialité des données des clients et l'usage — et appréciez le pilote au regard de chacun à partir de l'annexe 3.2 ; signalez deux limites des résultats présentés.

c) Indiquez deux facteurs de succès et deux points de vigilance propres à l'audit d'un outil fondé sur l'IA générative.

**3.3 – Méthode de conduite de la généralisation et cahier des charges (2 points)**

a) Comparez les deux options de méthode de l'annexe 3.2 C au regard de trois critères — la stabilité du besoin, la disponibilité des experts du pôle technique et la contrainte de la période fiscale —, puis recommandez, en la justifiant, la démarche de conduite de la généralisation. Aucun planning détaillé n'est attendu.

b) Après avoir précisé le rôle d'un cahier des charges fonctionnel, indiquez quatre rubriques indispensables à celui de la généralisation, en illustrant chacune par un contenu tiré des annexes.

**3.4 – Risques, plan qualité et recette de la généralisation (2 points)**

a) Identifiez trois risques du projet de généralisation, portant respectivement sur la maintenance de la base, l'évolutivité du dispositif et la sécurité et la confidentialité ; pour chacun, précisez sa cause dans les annexes, sa conséquence et une mesure de traitement.

b) Après avoir défini le plan qualité d'un projet, proposez son contenu pour la généralisation, puis décrivez la recette : acteurs, jeu d'essai, critères d'acceptation et calendrier.

**3.5 – Appropriation et gouvernance du dispositif (2 points)**

a) À partir des témoignages de l'annexe 3.3, analysez les résistances au dispositif, puis proposez quatre leviers d'appropriation, chacun en réponse à une résistance identifiée.

b) Précisez la gouvernance du dispositif : rôles des experts du pôle technique, des référents de bureau et des contributeurs, règles de validation et de mise à jour des fiches ; proposez un indicateur de pilotage du dispositif, précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

**3.6 – Choix du service d'IA et transition numérique responsable (1,5 point)**

Après avoir défini une stratégie de transition numérique responsable, appréciez les deux options de l'annexe 3.4 B sous trois angles — la sobriété du modèle et des usages, l'éthique et la transparence envers les clients, l'inclusion des collaborateurs —, puis recommandez l'une d'elles et deux règles d'usage de l'assistant. Aucun calcul d'empreinte n'est attendu.
