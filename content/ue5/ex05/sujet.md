# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 5

**DOSSIER 2 – AUDITER LA SÉCURITÉ DU SI ET FONDER UNE POLITIQUE DE SÉCURITÉ (14 points)**

Durée conseillée : 1 h 05 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 2.1 – L'incident de novembre 2026 : chronologie et conséquences

**A. Chronologie (reconstituée en décembre 2026 par le prestataire de réponse aux incidents de sécurité)**

| Date | Événement |
|---|---|
| Mardi 3 novembre 2026 | Une gestionnaire du service de scolarité du campus de Besançon reçoit un courriel qui imite un avertissement de la messagerie de l'école (« votre boîte aux lettres sera désactivée ») et saisit son identifiant et son mot de passe sur la page frauduleuse indiquée. |
| Du 4 au 13 novembre | L'attaquant utilise ce compte depuis l'étranger, par la messagerie en ligne et par l'accès à distance aux serveurs du campus, qui ne demandent qu'un mot de passe. Sur le serveur de fichiers, il trouve un tableur qui contient le mot de passe d'un compte d'administration utilisé en commun par les cinq informaticiens du campus. Il copie environ 40 Go de fichiers et commence à explorer les serveurs du siège, accessibles depuis le réseau du campus. Aucune alerte n'est relevée. |
| Nuit du samedi 14 au dimanche 15 novembre | Chiffrement du serveur de fichiers du campus, du serveur qui héberge l'installation du progiciel de scolarité propre au campus et de la sauvegarde en ligne de ces deux serveurs, accessible avec le même compte d'administration. Une demande de rançon est déposée sur les serveurs : l'attaquant menace de publier les fichiers copiés. |
| Lundi 16 novembre, 8 h | Les premiers personnels arrivés constatent que les fichiers sont illisibles. La directrice du campus, Mme Hélène MARCOIRE, prévient M. Fabien CORNAVIN, qui fait couper à 10 h les liaisons entre le campus et le reste de l'école. Aucune procédure de crise n'existe : une cellule de crise est improvisée autour de Mme FERRIOL, de Mme MARCOIRE, de M. CORNAVIN et de M. DELORMEAU. Une plainte est déposée le jour même ; l'école décide de ne pas payer la rançon. |
| Mardi 17 novembre | Intervention d'un prestataire spécialisé dans la réponse aux incidents de sécurité. |
| Mercredi 18 novembre | L'attaquant publie sur un site de divulgation un échantillon des fichiers copiés. |
| Vendredi 20 novembre | La violation de données personnelles est notifiée à l'autorité de contrôle. |
| Mardi 24 novembre | Reprise des services essentiels du campus sur des serveurs reconstruits. Le serveur de fichiers repart vide. La base de scolarité du campus est restaurée à partir d'une extraction transmise au siège le 30 septembre 2026 pour les statistiques de rentrée, seule copie restée intacte. |
| Vendredi 27 novembre | Information par courriel des étudiants, des vacataires et des entreprises dont les données ont été copiées. |

**B. Conséquences de l'incident**

| Domaine | Conséquences |
|---|---|
| Examens et jurys | Les jurys de diplôme des mastères spécialisés du campus (180 diplômés), prévus les 19 et 20 novembre, se tiennent le 10 décembre ; 25 diplômés attendus par leur nouvel employeur reçoivent leur attestation de réussite avec trois semaines de retard. Les 2 600 copies numérisées des partiels d'octobre, que les enseignants corrigeaient à partir du serveur de fichiers, sont perdues : 2 000 sont reconstituées à partir des originaux papier ; pour les 600 autres, les étudiants concernés repassent l'épreuve en janvier 2027. |
| Scolarité | Les quelque 9 000 notes saisies entre le 30 septembre et le 14 novembre sont perdues, puis ressaisies en décembre à partir des relevés des enseignants. Pendant neuf jours, le campus ne peut délivrer ni attestation de scolarité ni relevé de notes. |
| Paie | Les états d'heures de novembre des 130 vacataires du campus, tenus dans des tableurs du serveur de fichiers, sont perdus : leur rémunération est versée avec dix jours de retard. La paie des salariés, traitée au siège par le progiciel commun, est versée à la date habituelle. |
| Apprentissage | La facturation des contrats des 550 apprentis du campus prévue en novembre (environ 1,3 M€) est émise avec cinq semaines de retard, faute d'accès aux justificatifs d'assiduité conservés sur le serveur de fichiers. |
| Données personnelles | Les fichiers copiés comprennent l'identité, les coordonnées et les résultats des 1 400 étudiants du campus, les contrats des apprentis avec les coordonnées de 420 entreprises employeuses, ainsi que les relevés d'identité bancaire des vacataires. |
| Coût et image | Coût direct estimé à 0,3 M€ (prestataire de réponse à incident, matériels remplacés, heures supplémentaires), hors temps passé par les équipes. Plusieurs entreprises employeuses d'apprentis ont demandé par écrit quelles mesures l'école avait prises. |

**C. Témoignages (recueillis en mars 2027)**

**Mme Agnès FERRIOL, directrice générale** : « En décembre, le conseil d'administration m'a demandé qui était responsable de la sécurité à l'école : je n'ai pas su répondre. Je veux un diagnostic objectif pour le conseil de juin et une organisation claire. »

**Mme Hélène MARCOIRE, directrice du campus de Besançon** : « Mes cinq informaticiens ont travaillé jour et nuit pour remettre le campus debout. Le tableur des mots de passe servait à se dépanner quand l'un d'eux était absent. Si l'audit sert à désigner des coupables, vous n'obtiendrez pas grand-chose de mes équipes. »

**Mme Nathalie QUERVEL, responsable de la scolarité du campus de Besançon** : « Pendant neuf jours, nous avons travaillé sur des listes papier. Personne ne savait ce qui passait en premier : les jurys, les attestations réclamées par les apprentis ou les relevés de notes attendus par nos universités partenaires. En décembre, nous avons tout ressaisi à la main. »

**Mme Isabelle TRÉVANS, juriste du siège, déléguée à la protection des données** : « J'ai appris l'incident le jeudi 19 novembre. Il a fallu reconstituer les données touchées sans registre à jour, d'où une notification le vendredi. Je consacre à cette fonction un dixième de mon temps. »

**M. Antoine DELORMEAU, directeur administratif et financier** : « Je découvre que nos sauvegardes n'avaient jamais été restaurées pour de vrai. Je veux bien financer la sécurité, mais je veux savoir ce que nous achetons et comment nous saurons que cela fonctionne. »

**M. Fabien CORNAVIN, responsable informatique du siège** : « Au siège, nous testons une restauration de temps en temps ; la dernière date de 2023. Chaque campus a ses comptes, ses sauvegardes et ses règles. Je n'ai ni le mandat ni le temps d'imposer une politique de sécurité, et il n'en existe pas d'écrite. Je compte bien participer à l'audit : je connais l'existant mieux que personne. »

### ANNEXE 2.2 – Audit flash de la sécurité (février 2027) et lettre de mission

**A. Constats de l'audit flash** (réalisé en deux semaines, en février 2027, par le prestataire de réponse aux incidents, sur le siège et les trois campus)

| N° | Domaine | Constat |
|---|---|---|
| 1 | Comptes des utilisateurs | Trois annuaires de comptes distincts, un par campus. 1 200 comptes d'intervenants vacataires sont actifs ; seuls 450 d'entre eux correspondent à un vacataire qui intervient en 2026-2027 ; les plus anciens de ces comptes datent de 2018. Aucune procédure ne prévoit la désactivation d'un compte à la fin d'une vacation ou au départ d'un salarié : chaque campus crée les comptes à la demande et ne les supprime jamais. |
| 2 | Authentification | Aucune authentification multifacteur, ni pour la messagerie en ligne, ni pour l'accès à distance, ni pour les comptes d'administration. Après l'incident, les mots de passe n'ont été changés qu'à Besançon. |
| 3 | Comptes d'administration | Neuf comptes d'administration génériques sont partagés par les 21 informaticiens de l'école ; deux d'entre eux ont le même mot de passe sur les trois campus. Aucune opération d'administration ne peut être attribuée à une personne. |
| 4 | Cloisonnement | Sur chaque campus, les postes en libre-service des étudiants, les postes des services administratifs et les serveurs partagent le même réseau, relié sans cloisonnement à ceux des autres campus et du siège. |
| 5 | Sauvegardes | Les sauvegardes de chaque campus sont copiées sur un service en ligne accessible avec les comptes d'administration ordinaires ; il n'existe aucune copie déconnectée. Aucun test de restauration n'a jamais été réalisé sur les campus ; au siège, le dernier date de 2023. À Besançon, la base de scolarité n'était sauvegardée qu'une fois par semaine. |
| 6 | Continuité | Ni plan de continuité ni plan de reprise d'activité ; aucune liste des processus critiques ni des délais d'interruption qu'ils supportent ; aucune procédure de gestion de crise. |
| 7 | Gouvernance et sensibilisation | Aucun responsable de la sécurité des systèmes d'information n'est désigné et aucune politique de sécurité n'est écrite. La charte informatique de 2015 est signée par les salariés, mais ni par les vacataires ni par les étudiants. Dernière action de sensibilisation : 2020. Lors d'un exercice d'hameçonnage simulé mené en février 2027 auprès des 610 salariés, 120 ont cliqué sur le lien et 60 ont saisi leur mot de passe. |
| 8 | Inventaire et données personnelles | L'inventaire tenu au siège recense 38 applications ; l'audit flash en identifie 55, dont des services en ligne souscrits par les campus ou par des enseignants sans validation. Le registre des activités de traitement, tenu par la déléguée à la protection des données désignée en 2019, compte 22 traitements et n'a pas été mis à jour depuis 2021 ; il ne mentionne pas le logiciel de gestion des relations avec les entreprises utilisé en mode SaaS par le campus de Besançon. |

**B. Lettre de mission de Mme FERRIOL au cabinet (1er avril 2027)**
- Objet : évaluer la gouvernance de la sécurité, le niveau de sécurité et la capacité de continuité du système d'information de l'école ; proposer une politique de sécurité et un plan d'action priorisé.
- Durée : huit semaines, du lundi 12 avril au vendredi 4 juin 2027 ; restitution au conseil d'administration le jeudi 24 juin 2027.
- Moyens : deux consultants du cabinet ; accès aux documents, aux personnes et aux sites ; M. CORNAVIN est l'interlocuteur désigné.
- Demande du conseil d'administration : que le rapport précise « qui est responsable de quoi ».

### ANNEXE 2.3 – Repères réglementaires et méthodologiques (au 31/12/2026) et échelle de cotation des risques

**A. Textes et référentiels**

| Texte ou référentiel | Nature et objet | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 (RGPD) | Protection des données personnelles. Le responsable du traitement met en œuvre des mesures de sécurité appropriées au risque et tient un registre des activités de traitement ; le délégué à la protection des données, lorsqu'il est désigné, informe et conseille le responsable du traitement et contrôle le respect du règlement. Toute violation de données personnelles présentant un risque est notifiée à l'autorité de contrôle dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance ; les personnes concernées sont informées si le risque est élevé ; toutes les violations sont consignées dans un registre interne. | Applicable depuis le 25/05/2018 |
| ISO/IEC 27001:2022 | Norme d'exigences, certifiable, d'un système de management de la sécurité de l'information : engagement de la direction, appréciation et traitement des risques, mesure de l'efficacité, amélioration continue. Son annexe A comporte 93 mesures (organisationnelles, liées aux personnes, physiques et technologiques), détaillées par le guide ISO/IEC 27002:2022. | En vigueur ; la version de 2013 est remplacée |
| ISO 22301:2019 | Norme d'exigences d'un système de management de la continuité d'activité. | En vigueur |
| COBIT 2019 (ISACA) | Référentiel de gouvernance et de management de l'informatique : 40 objectifs répartis en cinq domaines (évaluer, diriger et surveiller ; aligner, planifier et organiser ; bâtir, acquérir et mettre en œuvre ; délivrer, servir et soutenir ; surveiller, évaluer et apprécier). | En vigueur |
| Guide d'hygiène informatique de l'ANSSI (version de 2017) | Guide de 42 mesures de sécurité de base, de niveau standard ou renforcé, destiné à toute organisation. | En vigueur |
| EBIOS Risk Manager (ANSSI, version 1.5 de 2024) | Méthode d'appréciation et de traitement des risques numériques, en cinq ateliers, compatible avec la norme ISO/IEC 27005:2022. | En vigueur |

**B. Échelle de cotation des risques retenue par l'école**

| Note | Probabilité | Gravité |
|---|---|---|
| 1 | Rare : moins d'une occurrence en dix ans | Mineure : gêne interne, sans effet sur les étudiants ni sur les partenaires |
| 2 | Possible : une occurrence en dix ans | Significative : activité d'un campus perturbée moins de deux jours, sans perte ni divulgation de données |
| 3 | Probable : une occurrence en trois ans | Grave : activité d'un campus interrompue plusieurs jours, ou perte ou divulgation de données personnelles |
| 4 | Quasi certaine : au moins une occurrence par an | Critique : processus critique de plusieurs campus interrompu plus d'une semaine, divulgation massive de données personnelles ou atteinte durable à la réputation de l'école |

Niveau de risque = probabilité × gravité : de 1 à 3, faible (risque accepté et surveillé) ; de 4 à 6, modéré (traitement planifié dans l'année) ; 8 ou 9, élevé (traitement prioritaire dans les six mois) ; 12 ou 16, critique (traitement immédiat, suivi par la direction générale).

### Travail à faire

Mme FERRIOL vous confie l'audit de la sécurité du système d'information et la préparation d'une politique de sécurité, dont les conclusions seront présentées au conseil d'administration du 24 juin 2027. Vous mobiliserez pour cela les annexes 1.1, 2.1, 2.2 et 2.3 ainsi que vos connaissances professionnelles.

**2.1 – Méthodologie de la mission d'audit (4 points)**

a) Après avoir défini l'audit du système d'information, présentez la méthodologie de la mission que vous conduirez à l'Institut LORVANNE : périmètre et objectifs, trois référentiels de l'annexe 2.3 en précisant ce que chacun apporte à la mission, étapes et livrables.

b) Indiquez quatre critères de performance ou de conformité que la mission évaluera, en illustrant chacun par un point de contrôle tiré des annexes.

c) Présentez deux facteurs de succès et deux points de vigilance propres à cette mission d'audit.

**2.2 – Analyse des risques révélés par l'incident (3 points)**

a) Classez les risques révélés par l'incident et par l'audit flash selon la typologie des risques du système d'information (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers), en illustrant chaque catégorie par des faits des annexes.

b) Après avoir défini l'analyse d'impact sur l'activité, analysez l'impact de l'incident sur quatre processus critiques de l'école et sur la continuité de ses activités.

c) Cotez cinq risques sur l'échelle de l'annexe 2.3 en justifiant la probabilité et la gravité retenues, puis indiquez les risques à traiter en priorité.

**2.3 – Politique de sécurité et continuité (4 points)**

a) Après avoir rappelé les objectifs de la sécurité de l'information, présentez les principes d'une politique de sécurité du système d'information fondée sur l'analyse des risques et adaptée à l'Institut LORVANNE.

b) Proposez quatre mesures prioritaires — gestion des identités et des accès sur tout le cycle de vie des comptes, authentification, segmentation, sauvegardes — en précisant pour chacune son principe, sa pertinence au regard de l'annexe 2.2 et un indicateur d'efficacité (formule, source, fréquence, cible et axe du tableau de bord prospectif).

c) Distinguez le plan de continuité d'activité (PCA) et le plan de reprise d'activité (PRA), puis fixez, en les définissant, un RTO et un RPO justifiés pour deux processus de l'école.

**2.4 – Note de synthèse au conseil d'administration (3 points)**

Rédigez, à l'attention du conseil d'administration présidé par M. LAMBRESC, une note de synthèse de 20 lignes au maximum qui présente le diagnostic d'audit établi à partir des annexes (appréciation globale et trois constats majeurs), les priorités d'action assorties d'une échéance, et la répartition des rôles et des responsabilités dans la gouvernance de la sécurité entre le conseil d'administration, la direction générale, le futur responsable de la sécurité des systèmes d'information (RSSI), la déléguée à la protection des données, les propriétaires des processus et les directeurs de campus.
