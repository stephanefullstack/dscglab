# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 42

**DOSSIER 3 – RENFORCER LA RÉSILIENCE OPÉRATIONNELLE NUMÉRIQUE ET FIABILISER LES DONNÉES DE DURABILITÉ (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 14, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. VALMÉRIS Assistance est une société anonyme créée en 1994, dont le siège est à Limoges. Entreprise d'assurance agréée pour la branche assistance, elle organise et finance, pour le compte de ses partenaires, l'aide apportée à leurs assurés jour et nuit : dépannage et remorquage des véhicules, véhicule de remplacement, intervention d'urgence au domicile après un dégât des eaux ou une effraction, aide à domicile et garde d'enfants après un accident. Elle est détenue à 70 % par le groupe d'assurance mutualiste TERRANDÈLE et à 30 % par un réseau bancaire coopératif. Ses garanties sont vendues par le groupe TERRANDÈLE et par quatorze partenaires (assureurs, banques, deux constructeurs automobiles et un loueur de véhicules), qui lui transmettent les contrats de leurs clients. En 2026, ses trois plateaux d'assistance de Limoges, Metz et Valence ont reçu 3,2 millions d'appels et ouvert 520 000 dossiers, confiés à un réseau de 3 400 prestataires agréés ; son chiffre d'affaires a atteint 310 M€. Elle emploie 820 salariés. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan stratégique « Assister 2030 », adopté en décembre 2026 par le conseil d'administration, fixe cinq objectifs : déclencher l'assistance sans appel quand un véhicule connecté signale une panne ou un accident ; informer chaque bénéficiaire en temps réel de l'arrivée de son prestataire ; réduire de 20 % d'ici 2029 le délai moyen d'arrivée sur place ; garantir la continuité du service jour et nuit et respecter durablement le règlement européen sur la résilience opérationnelle numérique du secteur financier (DORA), applicable à VALMÉRIS depuis le 17 janvier 2025 ; fournir au groupe TERRANDÈLE des données de durabilité fiables et réduire l'empreinte des interventions. Le logiciel de gestion des dossiers d'assistance, développé en interne en 2008, doit être remplacé avant la fin de 2028 par une solution du marché, dans le cadre du projet PASSERELLE.

Vous êtes directeur(rice) de la stratégie et des projets de VALMÉRIS Assistance depuis 2024, rattaché(e) au directeur général, M. Étienne MARVÉJOL ; vous animez le plan stratégique, le portefeuille de projets et les relations avec les principaux prestataires informatiques. M. MARVÉJOL vous demande trois travaux : préparer la transformation numérique de l'assistance et le projet PASSERELLE (dossier 1) ; organiser et exploiter les données des dossiers et du réseau de prestataires (dossier 2) ; renforcer la résilience opérationnelle numérique et fiabiliser les données de durabilité (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de VALMÉRIS Assistance et chiffres clés

VALMÉRIS Assistance est une société anonyme créée en 1994, dont le siège est à Limoges. Entreprise d'assurance agréée pour la branche assistance, elle organise et finance l'aide apportée jour et nuit aux assurés de ses distributeurs. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**L'activité, les actionnaires et les distributeurs**

| Donnée | Valeur |
|---|---|
| Actionnaires | groupe d'assurance mutualiste TERRANDÈLE : 70 % ; réseau bancaire coopératif : 30 % |
| Prestations d'assistance | dépannage et remorquage des véhicules, véhicule de remplacement ; intervention d'urgence au domicile après un dégât des eaux ou une effraction ; aide à domicile, garde d'enfants et transport après un accident |
| Distributeurs | 15 : le groupe TERRANDÈLE et 14 partenaires (assureurs, banques, deux constructeurs automobiles et un loueur de véhicules), qui vendent les garanties d'assistance à leurs clients et transmettent à VALMÉRIS les contrats et les bénéficiaires couverts |
| Réseau de prestataires | 3 400 prestataires agréés : dépanneurs et garages, serruriers, plombiers et vitriers, taxis et loueurs, services d'aide à domicile |

**L'activité en 2026**

| Donnée | Valeur |
|---|---|
| Appels reçus par les trois plateaux | 3,2 millions |
| Dossiers d'assistance ouverts | 520 000 : automobile 60 % ; habitation 25 % ; aide aux personnes 15 % |
| Chiffre d'affaires | 310 M€ |
| Dépenses du système d'information | environ 22 M€, dont 9 M€ de prestations externes |

**L'effectif au 31/12/2026**

| Direction ou service | Salariés |
|---|---|
| Plateaux d'assistance (chargés d'assistance et superviseurs) : Limoges 300, Metz 170, Valence 90 | 560 |
| Réseau de prestataires (sélection, suivi de la qualité, règlement des factures) | 90 |
| Direction des systèmes d'information | 70 |
| Fonctions support (finances, ressources humaines, juridique, risques et conformité, audit interne, relations avec les partenaires) | 100 |
| **Total** | **820** |

**Le système d'information en quelques lignes**

- Logiciel de gestion des dossiers d'assistance, développé en interne en 2008, à remplacer par une solution du marché avant la fin de 2028 (projet PASSERELLE).
- Téléphonie et distribution des appels en ligne, fournies par un opérateur sous forme de service.
- Application mobile des prestataires : acceptation des missions, géolocalisation, photos.
- Progiciel de règlement des prestataires ; progiciels de comptabilité et de paie ; messagerie et bureautique en ligne.
- Échanges quotidiens de fichiers avec les partenaires (contrats et bénéficiaires couverts) ; interfaces de programmation avec les deux constructeurs partenaires (alertes des véhicules connectés).
- Serveurs hébergés par un infogéreur dans deux centres de données situés en France.

**Organigramme simplifié (mars 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil d'administration, présidé par un représentant du groupe TERRANDÈLE | — |
| Nommé par le conseil d'administration | directeur général | M. Étienne MARVÉJOL |
| Rattachés au directeur général | direction des plateaux d'assistance (Limoges, Metz, Valence) | M. Damien CORTHELAY |
| | direction du réseau de prestataires | Mme Sophie GALANDRET |
| | direction des systèmes d'information | Mme Anne-Laure FERVIGNAC |
| | direction de la stratégie et des projets | vous |
| | direction des risques et de la conformité | Mme Isabelle KERDALOU |
| | direction administrative et financière (finances, ressources humaines, juridique, relations avec les partenaires) | M. Franck SALVEDOUX |
| | audit interne | Mme Laure VENDROUX |

### ANNEXE 3.1 – La panne du 14 janvier 2027 (récit de M. Damien CORTHELAY, directeur des plateaux, février 2027)

**A. La chronologie**

| Heure | Ce qui s'est passé |
|---|---|
| 19 h 50 | Le jeudi 14 janvier 2027, la neige tombe depuis l'après-midi sur l'est et le centre de la France. CALVÉNIS Télécom, l'opérateur qui fournit la téléphonie et la distribution des appels en ligne (annexe 3.3), installe une mise à jour de son logiciel de distribution des appels, sans en avoir averti VALMÉRIS. |
| 20 h | Les postes des chargés des trois plateaux ne reçoivent plus aucun appel. Les appels sont renvoyés vers une messagerie générique : « Nos services sont momentanément indisponibles, laissez votre numéro, nous vous rappellerons. » |
| 20 h 35 | Une superviseure de Limoges, surprise par le silence du plateau, prévient l'astreinte de la DSI. VALMÉRIS ne surveille pas elle-même le fonctionnement de la téléphonie. |
| 21 h | Trente chargés commencent à rappeler, depuis les téléphones mobiles de service, les bénéficiaires qui ont laissé un message. Le logiciel des dossiers n'ouvre un dossier qu'avec l'identifiant de l'appel transmis par la téléphonie : les chargés ouvrent les dossiers sur papier. |
| 21 h 10 | Le service d'assistance de CALVÉNIS répond enfin à la DSI. Croyant d'abord à une attaque par saturation de sa plateforme, l'opérateur isole ses équipements pendant une heure avant de mettre en cause sa mise à jour. |
| 22 h 30 | Le directeur général est informé par un SMS de la DSI. Aucune cellule de crise n'est réunie. |
| 23 h 55 | CALVÉNIS revient à la version précédente de son logiciel. Les appels arrivent de nouveau sur les postes à minuit. |
| 0 h à 6 h | Les chargés ressaisissent dans le logiciel les 1 200 dossiers ouverts sur papier, grâce à une procédure d'exception ouverte par la DSI à minuit. |
| Lendemain, 10 h | Les partenaires sont informés par un courriel de la direction des plateaux. |

**B. Les conséquences, en chiffres ronds**

- Environ 4 000 appels ont été présentés entre 20 h et minuit, contre 1 500 un jeudi soir ordinaire de janvier. 2 500 appelants ont laissé un message ; 1 500 ont raccroché sans laisser de message.
- 1 200 dossiers ont été ouverts sur papier, puis ressaisis ; 40 l'ont été en double ou de façon incomplète.
- Sur les 900 dépannages demandés pendant la panne, 600 ont été réalisés plus de trois heures après le premier appel du bénéficiaire. 150 bénéficiaires immobilisés ont été conduits en taxi ou logés à l'hôtel aux frais de VALMÉRIS : environ 40 k€ de frais supplémentaires.
- Les chargés rappelés et ceux qui ont prolongé leur service ont effectué environ 1 200 heures supplémentaires et de nuit, soit environ 50 k€.
- L'accord conclu avec un assureur partenaire prévoit une pénalité quand moins de 85 % des appels d'une journée sont décrochés : il réclame 60 k€. L'accord avec le loueur de véhicules partenaire prévoit une pénalité pour chaque véhicule immobilisé plus de quatre heures : il réclame 40 k€. Ce loueur a représenté environ 12 M€ du chiffre d'affaires de VALMÉRIS en 2026.
- 700 réclamations ont été reçues dans les quinze jours qui ont suivi, contre 350 environ sur une même période d'hiver.
- La presse régionale s'en est fait l'écho : « Une nuit de neige sans assistance : des automobilistes bloqués sans réponse ».

**C. Ce que nous avions prévu**

Le plan de continuité d'activité date de 2019. Il prévoit l'incendie d'un plateau, qui serait relayé par les deux autres, et la panne du logiciel des dossiers ; il ne prévoit pas la défaillance de l'opérateur de téléphonie, qui sert les trois plateaux à la fois. Il n'a jamais été exercé. VALMÉRIS ne dispose d'aucun second opérateur ni d'aucun renvoi automatique des appels vers un autre fournisseur. Dans le tableur des incidents de la DSI, la panne est inscrite sous le libellé « panne téléphonie, 4 h », sans autre précision.

**D. Les réactions**

**Le directeur de la relation client de l'assureur partenaire** : « Nos assurés nous ont appelés toute la nuit, et nous ne savions rien. Nous avons appris la cause de la panne par la presse. »

**La directrice des opérations du loueur de véhicules partenaire** : « Une panne peut arriver. Mais si cela se reproduit, nous réexaminerons notre accord. »

**M. CORTHELAY** : « Mes équipes ont été remarquables. Mais nous avons improvisé : personne ne savait qui devait décider quoi. »

### ANNEXE 3.2 – Le dispositif de gestion du risque lié aux TIC (constats de Mme Isabelle KERDALOU, directrice des risques et de la conformité, février 2027)

**A. Les constats**

| Domaine | Constat |
|---|---|
| Politique de sécurité | La politique de sécurité du système d'information date de 2018. Rédigée par la DSI, elle n'a jamais été mise à jour et ne s'appuie sur aucune analyse des risques. Elle ne cite ni la téléphonie en ligne, ni l'application mobile des prestataires, ni les interfaces avec les constructeurs, apparues depuis. |
| Conseil d'administration et direction générale | Le conseil d'administration n'a jamais validé de cadre de gestion du risque lié aux TIC et ne reçoit aucun compte rendu sur ces risques ; son comité d'audit et des risques n'examine que les rapports de l'audit interne. Le comité de direction n'a jamais traité le sujet avant la panne du 14 janvier 2027. |
| Responsable de la sécurité des SI | M. Nicolas BRESTAVIN, responsable de la sécurité des systèmes d'information (RSSI), est rattaché à la directrice des systèmes d'information, Mme Anne-Laure FERVIGNAC. Il administre aussi les serveurs et les comptes des utilisateurs ; son budget est une ligne du budget de la DSI. |
| Fonction de gestion des risques | La cartographie des risques de VALMÉRIS comporte une seule ligne « risque informatique », cotée une fois par an par la DSI elle-même. La direction des risques et de la conformité n'exerce aucun contrôle sur les risques liés aux TIC. |
| Incidents | En 2026, 160 incidents ont été inscrits dans un tableur tenu par le support de la DSI, sans classification par gravité, sans critère commun, sans mesure de leur effet sur les plateaux ni recherche de leurs causes. Aucun n'a été signalé au directeur général. |
| Objectifs de reprise | Aucun objectif de reprise n'est fixé par activité. Le contrat de l'infogéreur prévoit un rétablissement « dans les meilleurs délais » ; la DSI applique un objectif unique de 24 heures à toutes les applications, du logiciel des dossiers, utilisé jour et nuit, à la paie. En moyenne, environ 60 dossiers sont ouverts chaque heure, davantage en journée et les soirs d'hiver. |
| Sauvegardes | Le logiciel des dossiers est sauvegardé chaque nuit à 2 h, et la copie est conservée dans le second centre de données de l'infogéreur. Aucune sauvegarde n'a jamais été restaurée pour essai. En 2023, après une erreur de manipulation, la restauration d'une partie de la base a demandé 30 heures. |
| Identités et accès | Les plateaux utilisent 80 comptes génériques (« renfort1 », « renfort2 »…), partagés par les intérimaires et par les chargés en formation. Sur les 120 chargés partis en 2026, 45 ont encore un compte actif. Les droits sont demandés par courriel ; aucune revue des droits n'a eu lieu depuis 2024. |
| Tests | Aucun exercice du plan de continuité depuis 2019, aucun essai de bascule entre les deux centres de données de l'infogéreur, aucun test de résilience. |
| Prestataires | Le registre des accords conclus avec les prestataires de services TIC, établi en 2025, recense 30 accords ; il ne distingue pas ceux dont dépend la continuité des plateaux. |

**B. Le point de vue de Mme KERDALOU**

« La conformité au règlement DORA n'est pas un projet de la DSI. Le premier pilier du règlement, la gestion du risque lié aux TIC, suppose à mes yeux un cadre approuvé et suivi par le conseil d'administration, et un contrôle exercé par une fonction indépendante de ceux qui exploitent le système d'information. Le comité de direction a réservé 600 k€ en 2027 pour la sécurité et la résilience ; le conseil d'administration du 24 juin 2027 attend une proposition. »

### ANNEXE 3.3 – L'opérateur de téléphonie en ligne (fiche établie par la direction de la stratégie et des projets, mars 2027, et demande de l'auditrice interne)

**A. La fiche du prestataire**

| Rubrique | Situation |
|---|---|
| Prestataire | CALVÉNIS Télécom, opérateur de téléphonie et de distribution des appels en ligne |
| Service rendu | réception des appels composés sur les numéros d'assistance des 15 distributeurs ; distribution des appels aux 560 postes des trois plateaux selon le distributeur, la langue et la file d'attente ; messagerie ; enregistrement des conversations, conservées 90 jours (lieu et nature de la panne ou de l'urgence au domicile, immatriculation, composition de la famille) ; statistiques d'appels ; transmission de l'identifiant de chaque appel au logiciel des dossiers |
| Criticité | service critique : sans lui, aucun appel n'est reçu sur aucun plateau |
| Contrat | signé en mars 2021 pour cinq ans, reconduit tacitement en 2026 pour trois ans ; abonnement de 3 200 k€ en 2026, facturé selon le nombre d'appels |
| Engagement de service | disponibilité contractuelle de 99,9 % par mois, soit environ 43 minutes d'indisponibilité admise par mois, mesurée par l'opérateur ; un rapport mensuel de disponibilité est prévu, mais aucun n'a été reçu depuis un an ; VALMÉRIS ne mesure pas elle-même la disponibilité du service |
| Incidents connus | outre la panne du 14 janvier 2027, les plateaux ont relevé en 2026 cinq interruptions de 10 à 40 minutes, que l'opérateur n'a jamais expliquées |
| Hébergement | un seul centre de données, situé en France ; l'offre « deux sites » de l'opérateur n'a pas été souscrite en 2021 |
| Supervision | la supervision de la plateforme, jour et nuit, est confiée par CALVÉNIS à un sous-traitant établi hors de l'Union européenne, qui y accède à distance, y compris aux enregistrements, pour diagnostiquer les anomalies ; VALMÉRIS l'a appris en 2026 par une brochure commerciale |
| Mises à jour | installées par l'opérateur, en soirée, sans préavis à ses clients |
| Sécurité | l'opérateur présente un certificat de conformité à ISO/IEC 27001:2022, valable jusqu'en 2028, dont le périmètre couvre l'hébergement dans son centre de données, mais ni la supervision ni le développement de son logiciel ; il affirme disposer d'un plan de continuité, qu'il n'a jamais communiqué |
| Données personnelles | VALMÉRIS est responsable du traitement des données des appelants ; CALVÉNIS agit comme sous-traitant |
| Audit | le contrat permet à VALMÉRIS de faire auditer, une fois par an et avec un préavis de 30 jours, les moyens affectés au service ; cette faculté n'a jamais été exercée |
| Fin du contrat | le contrat ne prévoit ni la restitution des paramétrages de distribution des appels, des enregistrements et des statistiques, ni l'assistance de l'opérateur en cas de changement de prestataire |

**B. La demande de Mme Laure VENDROUX, auditrice interne**

« Le comité d'audit et des risques m'a demandé d'auditer CALVÉNIS Télécom au deuxième trimestre de 2027. J'y consacrerai 25 jours, avec l'appui d'un auditeur spécialisé dans les systèmes d'information, et je remettrai mon rapport en septembre 2027. Le commercial de CALVÉNIS m'a déjà dit que "le certificat suffit". Aidez-moi à préparer la démarche et les critères de cet audit. »

### ANNEXE 3.4 – Les données de durabilité demandées par le groupe (note de Mme Claire HAUDEMARE, directrice de la durabilité du groupe TERRANDÈLE, janvier 2027, et constats de la direction administrative et financière de VALMÉRIS)

**A. La demande du groupe**

« Le groupe TERRANDÈLE publie depuis l'exercice 2024 un état de durabilité consolidé conforme aux ESRS, qui inclut VALMÉRIS. Son analyse de double matérialité a retenu, pour l'activité d'assistance, le climat (les émissions liées aux interventions, mais aussi les épisodes de neige, de tempête et d'inondation, de plus en plus fréquents, qui font croître les demandes d'assistance et leur coût), le personnel et la relation avec les bénéficiaires. Deux assureurs partenaires demandent désormais l'empreinte des interventions dans leurs consultations. L'état de durabilité du groupe est vérifié par un auditeur de durabilité, qui exprime un avis sur l'état consolidé et peut demander, pour chaque information, comment elle a été obtenue.

Pour l'exercice 2026, VALMÉRIS transmettra avant le 31 mars 2027 :

| Thème | Informations attendues |
|---|---|
| Climat | émissions liées aux kilomètres parcourus par les prestataires pour les missions (dépanneurs, taxis, artisans) et aux véhicules de remplacement ; consommation d'énergie des trois plateaux et des serveurs |
| Personnel | effectif au 31 décembre, départs, heures de formation |
| Bénéficiaires | satisfaction, réclamations |

Chaque information sera accompagnée de sa méthode d'obtention, de ses sources et du nom de la personne qui l'a validée. »

**B. Les constats de la direction administrative et financière (M. Franck SALVEDOUX, février 2027)**

- Les informations sont collectées auprès de cinq services (plateaux, réseau de prestataires, DSI, ressources humaines, services généraux), chacun par un tableur envoyé par courriel ; un salarié de la direction administrative et financière les rassemble dans un tableur de synthèse.
- Les kilomètres des dépanneurs sont estimés à partir de leurs factures : frais de déplacement facturés, divisés par le prix moyen du kilomètre du barème. Les taxis et les artisans ne facturent pas de kilomètres : on retient 20 km par mission.
- L'application mobile des prestataires enregistre la position du prestataire quand il accepte la mission et quand il arrive sur place ; ces données ne sont pas utilisées et sont effacées au bout de 3 mois.
- Les loueurs indiquent le nombre de jours de location des véhicules de remplacement, mais pas le type de motorisation des véhicules.
- L'infogéreur ne fournit aucune donnée sur la consommation des serveurs de VALMÉRIS ; la DSI retient une estimation forfaitaire.
- Les tableurs sont écrasés d'une année à l'autre ; aucune correction n'est tracée.
- Pour 2025, les émissions des interventions ont été transmises en mars 2026 pour 9 000 tCO2e, corrigées en avril à 12 000 tCO2e (les taxis avaient été oubliés), puis en mai à 11 000 tCO2e (des missions avaient été comptées deux fois). Le groupe a dû corriger deux fois son chiffre consolidé. L'auditeur de durabilité du groupe a demandé comment le chiffre initial avait été obtenu : VALMÉRIS n'a pas pu le reconstituer.

**C. Les premières informations de 2026 (provisoires)**

| Information | Valeur 2026 |
|---|---|
| Missions confiées aux prestataires | environ 700 000 |
| Kilomètres parcourus pour les missions (estimation selon la méthode actuelle) | environ 40 millions |
| Émissions liées aux interventions (méthode et facteurs d'émission du groupe) | environ 10 000 tCO2e |
| Véhicules de remplacement | 90 000 locations, 300 000 jours de location |
| Électricité des trois plateaux | 2 400 MWh |
| Électricité des serveurs | non connue |
| Heures de formation | 28 000 |
| Réclamations ; bénéficiaires satisfaits ou très satisfaits | 9 000 réclamations ; 82 % |

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2022/2554 sur la résilience opérationnelle numérique du secteur financier (DORA) | Règlement d'application directe, sans transposition. Il repose sur cinq piliers : la gestion du risque lié aux technologies de l'information et de la communication (TIC) ; la gestion, la classification et la notification des incidents liés aux TIC ; les tests de résilience opérationnelle numérique ; la gestion des risques liés aux prestataires tiers de services TIC ; le partage d'informations. Pour les prestataires de services TIC, il demande en principe de tenir un registre des accords contractuels, de prévoir des droits d'audit et d'accès et de définir une stratégie de sortie. Il s'applique à VALMÉRIS. | Applicable depuis le 17/01/2025 |
| ISO/IEC 27001:2022 | Norme d'exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques ; 93 mesures en annexe A (dont le contrôle d'accès, la gestion des incidents, la sauvegarde, la continuité et la sécurité des relations avec les fournisseurs). | En vigueur |
| ISO/IEC 27005:2022 | Lignes directrices de gestion des risques liés à la sécurité de l'information : identification, analyse, évaluation et traitement des risques. | En vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI, 2024) | Méthode française d'appréciation et de traitement des risques numériques en cinq ateliers, compatible avec ISO/IEC 27005 ; elle intègre l'écosystème de l'organisation, dont ses prestataires. | Version 1.5 publiée en 2024 |
| ISO 22301:2019 | Norme d'exigences d'un système de management de la continuité d'activité : analyse d'impact sur l'activité, stratégies et plans de continuité, exercices et amélioration. | En vigueur |
| COBIT 2019 (ISACA) | Cadre de gouvernance et de management de l'information et des technologies : 40 objectifs de gouvernance et de management, dont la gestion des fournisseurs, des services et de la continuité. | Version 2019 |
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Le responsable du traitement ne fait appel qu'à des sous-traitants présentant des garanties suffisantes, liés par un contrat ; un sous-traitant ne recrute un autre sous-traitant qu'avec l'autorisation écrite préalable du responsable du traitement ; les transferts de données hors de l'Union européenne sont soumis à des garanties. | Applicable depuis le 25/05/2018 |
| Directive (UE) 2022/2464 (CSRD), modifiée par les directives (UE) 2025/794 et 2026/470, et normes européennes d'information en matière de durabilité (ESRS) | L'état de durabilité présente les impacts de l'entreprise sur les personnes et l'environnement et les effets des enjeux de durabilité sur sa situation (double matérialité) ; un groupe l'établit sur une base consolidée, en y intégrant ses filiales. Les ESRS comprennent des normes transversales et des normes thématiques (environnement, social, gouvernance). L'état de durabilité est vérifié par un auditeur de durabilité. Le groupe TERRANDÈLE y est soumis : cela n'est pas à déterminer. | Directive 2026/470 en vigueur depuis le 18/03/2026 ; ESRS révisées applicables aux exercices ouverts à compter du 01/01/2027, au choix pour 2026 |
| GHG Protocol (WRI et WBCSD) | Cadre de mesure et de déclaration des émissions de gaz à effet de serre en trois périmètres : émissions directes (scope 1), émissions liées à l'énergie achetée (scope 2), autres émissions indirectes de la chaîne de valeur (scope 3). | Édition révisée (2004) ; norme scope 3 (2011) |

Il n'est demandé aucune analyse juridique.

### Travail à faire

Un soir de neige, la panne de l'opérateur de téléphonie a privé les trois plateaux de tout appel pendant quatre heures ; le dispositif de gestion du risque lié aux TIC est loin de ce qu'attend le règlement DORA, et le groupe TERRANDÈLE a dû corriger deux fois les données de durabilité transmises par VALMÉRIS. M. MARVÉJOL vous demande de tirer les leçons de la panne, de proposer le cadre de gestion du risque lié aux TIC qui sera présenté au conseil d'administration du 24 juin 2027, de préparer avec l'auditrice interne l'audit de l'opérateur et de fiabiliser les données de durabilité destinées au groupe. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – L'analyse d'impact de la panne du 14 janvier 2027 (2,5 points)**

a) Après avoir présenté la typologie des risques liés aux systèmes d'information (cybermenaces, défaillances opérationnelles, risques réglementaires et métiers), classez dans cette typologie quatre causes ou facteurs d'aggravation de la panne relatés dans l'annexe 3.1, en couvrant les trois catégories.

b) Après avoir défini l'analyse d'impact sur l'activité, évaluez les effets de la panne sur les processus de VALMÉRIS, sur la continuité du service aux bénéficiaires, sur la relation avec les partenaires et sur les états financiers (postes exposés, en principe), puis tirez-en deux enseignements pour le plan de continuité d'activité. Aucune évaluation chiffrée ni aucun traitement comptable des pénalités ne sont attendus.

**3.2 – Le cadre de gestion du risque lié aux TIC (5 points)**

a) Après avoir situé la gestion du risque lié aux TIC parmi les cinq piliers du règlement DORA (annexe 3.5) et défini une politique de sécurité du système d'information fondée sur l'analyse des risques, proposez la démarche qui remplacera la politique de 2018 : l'appréciation des risques, en précisant la nature du référentiel de l'annexe 3.5 sur lequel vous vous appuyez, puis le contenu de la nouvelle politique.

b) Proposez la répartition des rôles et des responsabilités de la gestion du risque lié aux TIC entre le conseil d'administration, le directeur général, la direction des risques et de la conformité, le RSSI, la DSI et les prestataires, puis justifiez le positionnement que vous recommandez pour le RSSI.

c) Proposez quatre dispositifs de surveillance et de résilience répondant aux constats de l'annexe 3.2, portant respectivement sur la gestion des identités et des accès, sur le PCA et le PRA (avec un RTO et un RPO justifiés pour deux activités critiques), sur la classification et la remontée des incidents, et sur le programme de tests de résilience. Aucun délai de notification, aucun test technique de sécurité ni aucun paramétrage ne sont attendus.

d) Hiérarchisez quatre mesures à engager en 2027, en justifiant le rang de la première.

**3.3 – L'audit de l'opérateur de téléphonie (2 points)**

a) Présentez la démarche de l'audit de CALVÉNIS Télécom que préparera Mme VENDROUX : ses objectifs, la cartographie du service rendu, de l'appel du bénéficiaire à l'ouverture du dossier, et les principaux risques à couvrir.

b) Proposez quatre critères de performance et de conformité de cet audit, portant respectivement sur la disponibilité, la sécurité, la localisation et la confidentialité des données, et la réversibilité ; pour chacun, indiquez un contrôle à examiner et une preuve à demander à l'opérateur. Aucune analyse juridique du contrat n'est attendue.

**3.4 – Les données de durabilité destinées au groupe (3,5 points)**

a) Situez la demande du groupe TERRANDÈLE dans le cadre de la CSRD et des ESRS (annexe 3.5) : l'état de durabilité consolidé et la place qu'y tient VALMÉRIS, la double matérialité, illustrée par deux éléments de l'annexe 3.4, et la vérification par un auditeur de durabilité. Aucun calcul d'assujettissement n'est attendu, ni aucune démarche de l'auditeur.

b) Proposez le rôle du système d'information dans la collecte et la fiabilité des données de durabilité de VALMÉRIS, en quatre mesures portant respectivement sur les sources et la collecte automatisée, le référentiel des indicateurs, les contrôles et la piste d'audit, et la gouvernance des données ; reliez chacune à un constat de l'annexe 3.4.

c) Proposez deux indicateurs environnementaux, l'un mesurant l'empreinte des interventions, l'autre celle du système d'information de VALMÉRIS, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Aucun calcul d'empreinte n'est attendu.
