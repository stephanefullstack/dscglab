# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 37

**DOSSIER 1 – PRÉPARER LE SCHÉMA DIRECTEUR NUMÉRIQUE ET LA TRANSMISSION DES SAVOIRS (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 13, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en avril 2027. CASTELRIVE Agglomération est une communauté d'agglomération créée en 2017 qui regroupe 30 communes et 180 000 habitants, dont 62 000 dans la ville-centre de Castelrive. Elle exerce notamment les compétences de collecte des déchets ménagers, qu'elle assure en régie, de mobilités, de développement économique, d'habitat et de gestion de quatre piscines ; le traitement des déchets est confié à un syndicat auquel elle adhère, et le réseau de bus à un exploitant. Elle emploie 1 100 agents, dont 380 à la collecte et aux six déchèteries. Depuis 2025, les 78 000 foyers et 6 000 professionnels du territoire paient une redevance incitative d'enlèvement des ordures ménagères, qui comprend une part fixe et une part calculée selon le nombre de levées de leur bac, lu par les camions de collecte. Sa direction du numérique, forte de 45 agents, est mutualisée avec la ville de Castelrive : elle sert les deux collectivités et propose ses services à 18 petites communes membres. Les organisations, les personnes et les données de ce cas sont fictives.

Le projet de territoire « Castelrive 2032 », adopté en janvier 2027 par le conseil communautaire, fixe cinq objectifs : simplifier les démarches des usagers en offrant un guichet unique, en ligne et dans les mairies ; réduire de 15 % d'ici 2030 les ordures ménagères résiduelles collectées ; piloter les politiques publiques par les données et ouvrir les données du territoire ; garantir la continuité et la sécurité des services publics, numériques et techniques ; réduire l'empreinte environnementale du numérique. Le schéma directeur numérique 2022-2026 de la ville et de l'agglomération est arrivé à son terme, et un tiers des agents techniques partira en retraite d'ici 2032.

Vous êtes directeur(rice) général(e) adjoint(e) chargé(e) des ressources de CASTELRIVE Agglomération depuis 2025, rattaché(e) à la directrice générale des services, Mme Hélène VARSANGE ; vous supervisez les finances, les ressources humaines, les affaires juridiques et la relation avec la direction du numérique mutualisée. Mme VARSANGE vous demande trois travaux : préparer le futur schéma directeur numérique et la transmission des savoirs (dossier 1) ; organiser et exploiter les données de la redevance incitative (dossier 2) ; fiabiliser, sécuriser et rendre plus sobre le système d'information (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de CASTELRIVE Agglomération et chiffres clés

CASTELRIVE Agglomération est une communauté d'agglomération créée en 2017. Son siège est à Castelrive, la ville-centre. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Le territoire et les compétences**

| Donnée | Valeur |
|---|---|
| Communes membres | 30 : la ville-centre de Castelrive (62 000 habitants), quatre communes de 8 000 à 15 000 habitants et 25 communes rurales ou périurbaines |
| Population | 180 000 habitants |
| Compétences exercées (principales) | collecte des déchets ménagers, en régie : 40 camions de collecte, six déchèteries ; mobilités ; développement économique ; habitat ; gestion de quatre piscines |
| Compétences confiées à des tiers | traitement des déchets : syndicat auquel l'agglomération adhère ; réseau de bus : exploitant |
| Usagers de la collecte | 78 000 foyers et 6 000 professionnels ; environ 85 000 bacs équipés d'une puce |

**La redevance incitative en quelques lignes**

Depuis 2025, chaque foyer et chaque professionnel paie une redevance incitative d'enlèvement des ordures ménagères. Elle comprend une part fixe annuelle, qui dépend du volume du bac, et une part variable, due pour chaque levée au-delà d'un forfait de 12 levées par an. Chaque levée est lue par le camion de collecte, qui identifie la puce du bac ; les levées sont transmises au logiciel de facturation. La facture est semestrielle.

**L'effectif au 31/12/2026**

| Direction ou service | Agents |
|---|---|
| Collecte et déchèteries | 380 |
| Piscines et équipements | 210 |
| Services techniques (voirie des zones d'activités, bâtiments, ateliers) | 220 |
| Mobilités, développement économique et habitat | 70 |
| Fonctions ressources (finances, ressources humaines, affaires juridiques, relation aux usagers) | 170 |
| Administration générale et cabinet | 50 |
| **Total** | **1 100** |

Environ 600 agents travaillent sur le terrain, sans poste informatique attitré. Les 45 agents de la direction du numérique mutualisée sont des agents de la ville de Castelrive : ils ne sont pas compris dans l'effectif ci-dessus.

**La direction du numérique mutualisée et le système d'information en quelques lignes**

La direction du numérique est portée par la ville de Castelrive et mutualisée avec l'agglomération : elle sert les deux collectivités et propose ses services à 18 petites communes membres. Elle exploite deux salles informatiques, l'une à l'hôtel de ville, l'autre au siège de l'agglomération. Le système d'information comprend notamment : des progiciels de gestion financière et de gestion des ressources humaines partagés par la ville et l'agglomération ; le logiciel de facturation de la redevance, acquis auprès d'un éditeur et hébergé chez lui ; les ordinateurs embarqués et les lecteurs de puces des 40 camions ; le logiciel de contrôle d'accès des six déchèteries, où l'on entre avec un badge ; les logiciels de caisse et de billetterie des piscines ; la télégestion des chaufferies et du traitement de l'eau des piscines ; le site internet et ses formulaires en ligne ; la messagerie et la bureautique. En 2026, les dépenses du numérique de l'agglomération (contribution à la direction mutualisée et projets propres) ont atteint environ 4 M€.

**Organigramme simplifié (avril 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | président de CASTELRIVE Agglomération | M. Arnaud TELMONDIER |
| Rattachée au président | directrice générale des services | Mme Hélène VARSANGE |
| Rattaché(e) à la directrice générale des services | directeur(rice) général(e) adjoint(e) chargé(e) des ressources : finances, ressources humaines, affaires juridiques, relation avec la direction du numérique mutualisée | vous |
| Rattachées à la directrice générale des services | direction de la collecte et des déchèteries ; direction des piscines et des équipements ; direction des services techniques ; direction des mobilités et du développement | — |
| Service de la ville de Castelrive, au service des deux collectivités | direction du numérique mutualisée | — |

### ANNEXE 1.2 – Le bilan du schéma directeur 2022-2026 et la mutualisation (note de M. Thierry LANDOUSSE, directeur du numérique mutualisé, et témoignages recueillis en mars 2027)

**A. Le bilan du schéma directeur 2022-2026 (note de M. LANDOUSSE)**

« Le schéma directeur 2022-2026, rédigé par la direction du numérique en 2021 et commun à la ville et à l'agglomération, comptait 18 projets. 9 ont été réalisés, 4 ont été reportés et 5 ont été abandonnés.

- **Réalisés**, notamment : le progiciel de gestion des ressources humaines partagé par les deux collectivités (2023) ; la messagerie et la bureautique en ligne (2023) ; les lecteurs de puces et les ordinateurs embarqués des camions (2024) ; le logiciel de facturation de la redevance incitative (2025) ; une quarantaine de formulaires en ligne sur le site de l'agglomération (2024).
- **Reportés**, notamment : le plan de continuité du système d'information, reporté deux fois ; le renouvellement des postes de travail.
- **Abandonnés**, notamment : le portail unique des démarches des deux collectivités, prévu pour 2024, abandonné en 2026 faute de service pour le porter ; l'accès des agents de terrain à l'intranet depuis un téléphone, abandonné en 2025.
- **Hors schéma** : nous avons en outre conduit 11 projets non prévus, lancés à la demande d'un service, comme le nouveau logiciel de billetterie des piscines choisi par leur responsable en 2025 ou l'application de signalement des dépôts sauvages demandée par la ville. Ils ont absorbé environ 30 % du temps de nos équipes de projet.

Faute d'instance, j'arbitre moi-même les priorités chaque lundi, selon l'urgence et l'insistance des demandeurs. Les services de la ville sont dans le même bâtiment que nous et relancent plus souvent : en 2026, une demande d'évolution a été traitée en 3 mois en moyenne pour la ville, en 7 mois pour l'agglomération. La convention de mutualisation prévoit un comité de pilotage commun deux fois par an ; il ne s'est réuni qu'une fois depuis 2022, pour le lancement du schéma. Elle répartit les coûts selon le nombre de postes informatiques de chaque collectivité, soit environ 55 % pour la ville et 45 % pour l'agglomération ; l'agglomération conteste cette clé, qui ne tient pas compte de ses 600 agents de terrain sans poste. Aucun projet du schéma ne portait sur les données ni sur l'empreinte environnementale du numérique. Les 18 petites communes membres ont été consultées une seule fois, par un questionnaire de 2021 auquel 6 d'entre elles ont répondu. »

**B. L'auto-évaluation de maturité numérique (février 2027)**

La direction du numérique a évalué seule, sans entretien avec les services ni avec les communes, la maturité numérique « de la ville et de l'agglomération », par une note unique pour les deux collectivités. Elle a utilisé une échelle de cinq niveaux inspirée des niveaux de maturité du modèle CMMI :
- **1 – initial** : chacun fait à sa façon ; rien n'est écrit et tout repose sur quelques personnes ;
- **2 – reproductible** : certains services ont leurs habitudes, qu'ils reproduisent, mais elles diffèrent d'un service à l'autre ;
- **3 – défini** : une même façon de faire est formalisée et respectée dans la ville comme dans l'agglomération ;
- **4 – mesuré** : les résultats de cette façon de faire sont mesurés et comparés à des objectifs publiés ;
- **5 – en amélioration continue** : les mesures servent chaque année à corriger et à améliorer les pratiques.

| Domaine | Note | Justification retenue par la direction du numérique |
|---|---|---|
| Stratégie numérique | 3 | « un schéma directeur commun a été adopté pour 2022-2026 » |
| Gouvernance | 3 | « un comité de pilotage commun est prévu par la convention de mutualisation » |
| Services aux usagers | 4 | « une quarantaine de formulaires en ligne, accessibles 24 heures sur 24 » |
| Données | 2 | « données réparties dans les logiciels métiers, sans responsable désigné » |
| Sécurité | 3 | « une politique de sécurité a été rédigée en 2023 » |
| Compétences | 4 | « 95 % des agents de la direction du numérique ont suivi une formation en 2026 » |
| Numérique responsable | 1 | « aucune démarche engagée » |

Conclusion de la direction du numérique : « Notre maturité est bonne, autour du niveau 3. Ce qui nous manque, ce sont des moyens supplémentaires. »

**C. Témoignages**

**Mme Odile FERRANCHE, vice-présidente de l'agglomération chargée du numérique et des relations avec les communes** : « J'ai appris le choix du nouveau logiciel de billetterie des piscines par la presse locale. Les élus n'ont jamais été associés aux priorités du numérique : le comité de pilotage ne se réunit pas, et je ne sais pas qui doit porter le guichet unique voulu par "Castelrive 2032". »

**M. Arnaud TELMONDIER, président** : « Le prochain schéma directeur ne doit pas être celui de la direction du numérique, mais celui de nos deux collectivités. Je veux qu'il serve d'abord les habitants, toutes les communes, et pas seulement la ville-centre. »

**Le maire d'une commune rurale de 900 habitants, adhérente au service commun** : « On nous propose des services, on ne nous demande jamais notre avis. Notre secrétaire de mairie reçoit chaque semaine des questions sur les bacs et sur les factures de la redevance ; elle les transfère par courriel au siège, sans savoir ce qu'elles deviennent. »

**Une responsable de service de l'agglomération** : « Pour obtenir quelque chose de la direction du numérique, il faut connaître quelqu'un. La ville passe toujours avant nous. »

### ANNEXE 1.3 – Les demandes des usagers aujourd'hui (constats de Mme Leïla MANDROUX, responsable du service de la relation aux usagers, mars 2027)

**A. Les canaux et les demandes**

En 2026, le service a reçu environ 120 000 demandes relevant de l'agglomération.

| Canal | Part des demandes |
|---|---|
| Accueil du siège de l'agglomération | 15 % |
| Téléphone | 40 % |
| Courriel | 15 % |
| Formulaires du site internet | 20 % |
| Accueil des mairies, qui transmettent au siège | 10 % |

| Demande | Part des demandes | Logiciel dans lequel elle est traitée |
|---|---|---|
| Bac neuf, changement de volume ou réparation d'un bac | 25 % | logiciel de facturation de la redevance |
| Emménagement ou départ d'un foyer | 20 % | logiciel de facturation de la redevance, puis logiciel de contrôle d'accès des déchèteries |
| Contestation d'une facture de redevance | 15 % | logiciel de facturation de la redevance |
| Badge de déchèterie (création, perte, droits d'un professionnel) | 20 % | logiciel de contrôle d'accès des déchèteries |
| Abonnement aux piscines | 10 % | logiciel de billetterie des piscines |
| Autres demandes | 10 % | — |

**B. Les constats**

- Les formulaires du site arrivent dans une boîte de courriel commune ; un agent les ressaisit dans le logiciel concerné. Pour un emménagement, la même information (nom, adresse, composition du foyer) est saisie trois fois : dans le logiciel de facturation, dans le logiciel de contrôle d'accès des déchèteries et dans le tableur de suivi du service. Les trois logiciels ne sont pas reliés entre eux.
- Les mairies transmettent les demandes reçues à leur accueil par courriel, sans modèle commun : 30 % de ces courriels sont incomplets (adresse imprécise, bac non identifié) et donnent lieu à un rappel de la mairie ou de l'usager.
- Aucune demande ne reçoit de numéro de suivi ; l'usager ne peut pas savoir où en est sa demande. 35 % des demandes sont suivies d'au moins une relance, le plus souvent par téléphone.
- Délais moyens de traitement en 2026 : 15 jours pour un bac neuf (l'objectif affiché sur le site est de 5 jours) ; 3 semaines pour enregistrer un emménagement ou un départ ; 10 jours pour un badge de déchèterie ; 6 semaines pour répondre à une contestation de facture. Une contestation de facture sur trois vient d'un emménagement ou d'un départ enregistré trop tard.
- Les formulaires du site de l'agglomération et ceux du site de la ville sont gérés séparément ; un habitant de Castelrive qui déménage effectue des démarches distinctes auprès des deux collectivités.

**C. Le guichet unique de « Castelrive 2032 »**

Le projet de territoire prévoit « un guichet unique des démarches, en ligne et dans les mairies : un seul point d'entrée pour toutes les démarches de l'agglomération, un suivi de chaque demande jusqu'à la réponse et un usager qui ne donne qu'une fois les mêmes informations ». Aucun projet n'a encore été lancé.

### ANNEXE 1.4 – Les savoirs des agents qui partent (note de Mme Corinne ABRESCAL, directrice des ressources humaines, et témoignages recueillis en mars 2027)

**A. Les départs prévus (note de la directrice des ressources humaines)**

D'ici 2032, environ 270 agents techniques partiront en retraite, soit un tiers des agents techniques.

| Direction | Départs prévus d'ici 2032 | Dont postes clés |
|---|---|---|
| Collecte et déchèteries | 130 | 25 des 40 chefs d'équipe de collecte ; 15 des 40 agents des déchèteries |
| Piscines et équipements | 70 | 8 des 12 techniciens des chaufferies et du traitement de l'eau des piscines |
| Services techniques | 70 | — |
| **Total** | **270** | |

Aujourd'hui, un poste n'est remplacé qu'après le départ de son titulaire : le successeur arrive sans avoir travaillé avec lui.

**B. Les six savoirs critiques repérés par la direction des ressources humaines et les chefs de service (février 2027)**

| Repère | Savoir | Détenteur | Départ prévu | Formalisation actuelle | Effet de sa perte | Successeur |
|---|---|---|---|---|---|---|
| S1 | Points de vigilance des douze tournées du secteur nord : impasses où il faut reculer, rues fermées les jours de marché, bacs à aller chercher chez des personnes âgées, horaires près des écoles | M. Patrick SERVOLLE, chef d'équipe de collecte | juin 2028 | aucune : l'ordinateur embarqué n'affiche que l'itinéraire théorique | sécurité des équipes et des riverains ; bacs oubliés et réclamations | non désigné |
| S2 | Ajustement du traitement de l'eau des bassins selon la fréquentation et la météo | M. Gilles TARNÈDE, technicien du centre aquatique | mars 2029 | partielle : carnet personnel et photos sur son téléphone | sécurité sanitaire des baigneurs ; fermeture d'un bassin | désigné : un technicien arrivé en 2026 |
| S3 | Réponse aux alarmes de la télégestion des chaufferies la nuit et le week-end : alarmes sans suite, alarmes qui imposent un déplacement, gestes à faire à distance ou sur place | deux techniciens d'astreinte | 2028 et 2030 | aucune | continuité du service (bassins fermés après un arrêt de chaudière) ; déplacements inutiles | non désigné |
| S4 | Reconnaissance des apports des professionnels en déchèterie et application de leurs droits d'accès | agents des déchèteries (15 départs) | de 2027 à 2032 | partielle : note de service de 2019, jamais mise à jour | litiges avec les professionnels ; apports refusés ou acceptés à tort | recrutés après chaque départ |
| S5 | Consignes de sécurité des quais de déchèterie et des locaux de traitement de l'eau | responsables des sites | — | complète, mais dans des classeurs papier des locaux, version de 2018 | accidents d'agents ou d'usagers | sans objet : consignes collectives |
| S6 | Contacts du secteur rural : secrétaires de mairie, gardiens d'immeubles, entreprises des zones d'activités | chef d'équipe de collecte du secteur sud | décembre 2027 | aucune : répertoire sur son téléphone personnel | relations avec les communes et les entreprises ; demandes mal orientées | désigné |

**C. Les outils déjà utilisés sur le terrain et les outils documentaires**

- **Collecte** : l'ordinateur embarqué de chaque camion affiche l'itinéraire de la tournée et permet de signaler un bac non présenté.
- **Chaufferies et traitement de l'eau** : les alarmes de la télégestion arrivent sur le téléphone de service du technicien d'astreinte.
- **Déchèteries** : à l'entrée de chaque déchèterie, l'agent dispose de l'écran du logiciel de contrôle d'accès, qui affiche le badge présenté et ses droits.
- **Outils documentaires** : la gestion électronique des documents (GED), installée en 2023 pour les deux collectivités, n'est vraiment utilisée que par 2 services administratifs ; 20 agents de terrain y ont un compte. L'intranet n'est consultable que depuis un poste relié au réseau des deux collectivités.
- Les agents de terrain n'ont pas de poste attitré ; la collecte commence à 5 h, les piscines et les déchèteries ouvrent le week-end ; les réunions de service ont lieu une fois par mois, au siège.

**D. Témoignages**

**M. Patrick SERVOLLE, chef d'équipe de collecte, départ prévu en juin 2028** : « Ce que je sais, je l'ai appris sur le tas, en vingt-cinq ans de tournées. Je veux bien le donner. Mais si on me filme au travail, je veux être sûr que ça ne servira pas à juger comment je fais mon métier, ni celui de mes collègues. »

**Mme Sandrine PELLOUAN, agente de déchèterie depuis 2024** : « Encore un outil ? J'ai déjà l'écran des badges à l'entrée et le téléphone de service. Si l'information n'est pas sous mes yeux au moment où un professionnel se présente, je ne la chercherai pas. »

**Le responsable de l'équipe de collecte du secteur nord** : « Faire travailler un ancien avec un nouveau, c'est deux agents sur le même camion. Avec une prise de poste à 5 h et des absents à remplacer chaque lundi, je n'ai personne à libérer. »

**Le technicien arrivé en 2026 au centre aquatique** : « J'ai remplacé un collègue parti trois semaines avant mon arrivée. J'ai appris en appelant les techniciens des autres piscines. M. TARNÈDE m'aide quand il est là, mais nous ne sommes jamais de service en même temps. »

### Travail à faire

Le schéma directeur numérique 2022-2026 est échu, les usagers attendent un guichet unique et un tiers des agents techniques partira d'ici 2032. Mme VARSANGE vous demande de préparer le schéma directeur 2028-2032 commun à la ville et à l'agglomération, d'éclairer la maturité numérique et la gouvernance de la direction du numérique mutualisée, de préparer le guichet unique et d'organiser la transmission des savoirs des agents qui partent. Vous mobiliserez pour cela les annexes 1.1 à 1.4 ainsi que vos connaissances professionnelles.

**1.1 – Le schéma directeur numérique 2028-2032 et l'alignement du système d'information mutualisé (4 points)**

a) Après avoir défini le schéma directeur numérique, proposez la démarche d'élaboration du schéma directeur 2028-2032 commun à la ville et à l'agglomération : ses étapes, ses acteurs (dont les élus, les communes membres, les agents et les usagers) et ses livrables. Il n'est demandé ni feuille de route ni classement des projets.

b) Après avoir défini l'alignement stratégique du système d'information, appréciez l'alignement du système d'information mutualisé sur les objectifs de « Castelrive 2032 » en relevant trois décalages tirés de l'annexe 1.2, puis concluez.

**1.2 – La maturité numérique et la gouvernance de la direction du numérique mutualisée (3,5 points)**

a) Après avoir présenté le principe d'une évaluation de la maturité numérique en vous référant à un modèle de maturité, interprétez l'auto-évaluation de l'annexe 1.2 B : deux limites de la méthode suivie, deux écarts entre les notes et les faits relatés dans les annexes 1.2 et 1.3, puis deux domaines à traiter en priorité, justifiés.

b) Après avoir défini la gouvernance du système d'information, proposez la gouvernance de la direction du numérique mutualisée : deux instances communes à la ville et à l'agglomération (composition, fréquence, décisions), la place des 18 petites communes membres, et quatre critères d'arbitrage des demandes entre les deux collectivités. Aucune analyse juridique de la convention de mutualisation ni aucun calcul de la clé de répartition ne sont attendus.

**1.3 – Les demandes des usagers et le guichet unique (3 points)**

a) Analysez le processus actuel de traitement des demandes des usagers en relevant trois dysfonctionnements tirés de l'annexe 1.3, avec leurs effets pour les usagers et pour les services.

b) Après avoir défini l'urbanisation du système d'information, décrivez le processus cible du guichet unique, de la demande à la réponse, puis présentez, en principe, l'architecture urbanisée qui le soutient : le portail des démarches, l'outil de gestion de la relation avec les usagers, le référentiel commun des usagers, les échanges avec les logiciels métiers et avec les mairies. Aucun schéma technique détaillé ni aucun choix de logiciel ne sont attendus.

**1.4 – La transmission des savoirs des agents qui partent (3,5 points)**

a) Après avoir distingué savoirs tacites et savoirs explicites, classez les six savoirs critiques de l'annexe 1.4 B selon deux critères que vous expliciterez. Pour les trois savoirs que vous jugez prioritaires, proposez ensuite une forme de transmission adaptée, en précisant qui la conduit et avant quelle échéance.

b) Montrez comment intégrer ces trois savoirs aux outils déjà utilisés sur le terrain (annexe 1.4 C), en précisant le rôle de la GED et de l'intranet. Proposez ensuite la gouvernance du dispositif : les rôles, les règles de mise à jour et un indicateur de suivi, précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

c) Proposez trois leviers d'appropriation du dispositif adaptés aux agents de terrain, chacun en réponse à une réticence ou à une difficulté exprimée dans l'annexe 1.4 D.
