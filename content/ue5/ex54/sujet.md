# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 54

**DOSSIER 3 – TIRER LES CONCLUSIONS D'UN AUDIT, MAÎTRISER LES RISQUES ET LA SÉCURITÉ DU SYSTÈME D'INFORMATION OPÉRATIONNEL ET EN RÉDUIRE L'EMPREINTE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 18, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mai 2027. Le service départemental d'incendie et de secours (SDIS) du Val-d'Aurande est un établissement public administratif départemental chargé de la prévention, de la protection et de la lutte contre les incendies et des secours aux personnes dans un département de 640 000 habitants, rural pour l'essentiel, qui s'étend du massif du Haut-Aurande aux plaines de la vallée de l'Aurande. Son conseil d'administration réunit des élus du département, des communes et des intercommunalités, qui le financent à hauteur de 55 % et 45 %. En 2026, le centre de traitement de l'alerte, installé au siège de Montcerneau, a reçu 150 000 appels, et les 60 centres d'incendie et de secours du département ont réalisé 50 000 interventions avec 420 engins. Le SDIS compte 700 sapeurs-pompiers professionnels, 250 personnels administratifs et techniques et 3 900 sapeurs-pompiers volontaires ; son budget de fonctionnement s'est élevé à 105 M€. Les organisations, les personnes et les données de ce cas sont fictives.

Le projet d'établissement « Val-d'Aurande Secours 2031 », adopté en mars 2027 par le conseil d'administration, fixe cinq objectifs : maintenir le délai moyen d'arrivée des premiers secours sous 20 minutes dans toutes les communes ; fidéliser les volontaires en simplifiant leur engagement, au premier rang leur déclaration de disponibilité ; garantir la continuité du traitement de l'alerte, jour et nuit ; partager les données utiles avec les partenaires (centre de régulation médicale du SAMU, communes, département) ; réduire de 20 % l'empreinte environnementale de l'établissement d'ici 2031. Le système d'information s'est construit autour du logiciel de traitement de l'alerte, installé en 2012 ; les autres outils ont été ajoutés au fil des besoins, et plusieurs arrivent en fin de vie.

Vous êtes chef(fe) du groupement « Pilotage et systèmes d'information » du SDIS depuis 2026 ; vous dirigez le contrôle de gestion, le service des systèmes d'information et de communication et l'observatoire de l'activité. Le directeur départemental, le colonel hors classe Étienne GRANVOISE, vous demande trois travaux : préparer la gouvernance du SI et la conduite du projet VIGIE (dossier 1) ; organiser et exploiter les données des interventions, et en maîtriser la conservation (dossier 2) ; tirer les conclusions d'un audit, maîtriser les risques et la sécurité du SI opérationnel et en réduire l'empreinte (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation du SDIS du Val-d'Aurande et chiffres clés

Le SDIS du Val-d'Aurande est un établissement public administratif départemental. Il assure la prévention, la protection et la lutte contre les incendies et les secours aux personnes dans le département fictif du Val-d'Aurande, dans le centre-est de la France : 640 000 habitants, un territoire rural pour l'essentiel, du massif du Haut-Aurande aux plaines de la vallée de l'Aurande. Son siège et son centre de traitement de l'alerte sont à Montcerneau, chef-lieu du département. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**La gouvernance et le financement**

| Donnée | Valeur |
|---|---|
| Conseil d'administration | 22 membres, élus du département, des communes et des intercommunalités ; président : M. Lucien FERMONTEIL, vice-président du conseil départemental |
| Direction | directeur départemental : le colonel hors classe Étienne GRANVOISE |
| Financement | département 55 % ; communes et intercommunalités 45 % |
| Budget 2026 | fonctionnement 105 M€, dont dépenses de personnel 80 % (indemnités des sapeurs-pompiers volontaires : 14 M€) ; investissement 15 M€ ; dépenses du système d'information, hors réseau radio : 3,6 M€ |

**L'activité en 2026**

| Donnée | Valeur |
|---|---|
| Centres d'incendie et de secours | 60, répartis en quatre groupements territoriaux : 12 centres mixtes, avec des professionnels et des volontaires, et 48 centres armés par des volontaires seulement |
| Appels reçus au centre de traitement de l'alerte | 150 000 |
| Interventions | 50 000 : secours d'urgence aux personnes 78 % ; accidents de la circulation 7 % ; incendies 7 % ; opérations diverses 8 % |
| Engins | 420 |
| Délai moyen d'arrivée des premiers secours | 14 minutes dans le département ; plus de 20 minutes dans une trentaine de communes du Haut-Aurande |

**L'effectif**

| Catégorie | Effectif |
|---|---|
| Sapeurs-pompiers professionnels | 700 |
| Personnels administratifs et techniques | 250, dont 24 au service des systèmes d'information et de communication (12 en informatique, 8 aux transmissions, 4 au soutien du centre de traitement de l'alerte) |
| Sapeurs-pompiers volontaires | 3 900, dont 600 professionnels également volontaires dans leur centre |

**Le système d'information en quelques lignes**

- **Logiciel de traitement de l'alerte et de gestion opérationnelle**, installé en 2012 et édité par un petit éditeur spécialisé : réception des appels, localisation, proposition des engins à engager, suivi des interventions. Il est hébergé sur des serveurs de la salle informatique du siège, doublée par une salle de secours au centre de Montcerneau-Sud.
- **Enregistreur des appels** du centre de traitement de l'alerte.
- **Logiciel de gestion des disponibilités des volontaires** (site web et messages SMS), installé en 2010 ; le support de son éditeur est assuré jusqu'à la fin de 2028.
- **Logiciel de gestion des indemnités des volontaires**, relié au logiciel de paie par un fichier mensuel.
- **Application de comptes rendus de secours** sur 300 tablettes embarquées dans les engins (2021).
- **Logiciel de gestion du parc** des engins et des équipements de protection individuelle.
- **Base des points d'eau d'incendie**, avec un système d'information géographique.
- Logiciel de ressources humaines et de paie ; progiciel financier ; plateforme de formation ; bureautique.

**Organigramme simplifié (mai 2027)**

| Rattachement | Fonction | Titulaire |
|---|---|---|
| — | conseil d'administration | président : M. Lucien FERMONTEIL |
| Conseil d'administration | direction départementale | directeur départemental : le colonel hors classe Étienne GRANVOISE |
| Direction départementale | déléguée à la protection des données | Mme Coralie FAVERJON |
| | groupement « Pilotage et systèmes d'information » : contrôle de gestion, service des systèmes d'information et de communication, observatoire de l'activité | vous ; cheffe du service des systèmes d'information et de communication : Mme Solène VARANGEOT ; chef de l'observatoire de l'activité : M. Rémi TRÉVIGNAN |
| | groupement des opérations, dont le centre de traitement de l'alerte | lieutenant-colonel Bertrand OSSELIN ; cheffe du centre de traitement de l'alerte : commandante Maëlle TOURNEVAL |
| | groupement du volontariat | lieutenant-colonel Hervé DOMBRESSAC |
| | service de santé et de secours médical | médecin-chef : Dr Agathe MÉRIGNOLLE |
| | groupement technique et logistique | M. Pascal LAUZERAC |
| | groupement des finances | Mme Laure CHAMBREUIL |
| | quatre groupements territoriaux | un chef de groupement territorial pour chacun |
| Groupements territoriaux | 60 centres d'incendie et de secours | un chef de centre pour chacun |

### ANNEXE 3.1 – Les constats de l'audit de la base des points d'eau d'incendie (rapport de M. Gaël VORMESSAC, auditeur des systèmes d'information externe, avril 2027)

**A. La mission et la base**

À la demande du directeur départemental, M. VORMESSAC a audité, de janvier à mars 2027, la base des points d'eau d'incendie et sa transmission au logiciel de traitement de l'alerte. La mission est terminée : la réunion de clôture s'est tenue le 15/04/2027.

La base recense 14 000 points d'eau : 10 000 poteaux et bouches d'incendie raccordés aux réseaux d'eau, 3 000 citernes et réserves, 1 000 points d'aspiration aménagés sur des étangs ou des rivières. Elle est tenue, avec le système d'information géographique, par la cellule cartographie du groupement des opérations, qui compte trois agents. Chaque mois, un fichier extrait de la base est chargé dans le logiciel de traitement de l'alerte, dont la carte indique aux opérateurs et aux équipages les points d'eau proches du sinistre et leur état (disponible ou indisponible).

L'organisation fixée par le SDIS, qui n'est pas à discuter, est la suivante : chaque point d'eau est contrôlé au moins une fois tous les deux ans ; les communes et les gestionnaires des réseaux d'eau font les contrôles et en transmettent les résultats au SDIS ; toute indisponibilité (poteau hors service, citerne vide, travaux) est signalée au SDIS dès qu'elle est connue. Aucune règle de droit n'est à connaître.

**B. Les constats (notes brutes, dans l'ordre où ils ont été relevés)**

- 3 500 points d'eau, un sur quatre, n'ont aucun contrôle enregistré depuis plus de deux ans ; la plupart sont des citernes et des points d'aspiration du Haut-Aurande.
- En 2026, le SDIS a reçu 6 000 résultats de contrôles, envoyés par courriel par les 480 communes du département et par les 6 gestionnaires des réseaux d'eau, dans des tableurs de formats différents (colonnes, codes des points, libellés des états). Les trois agents de la cellule cartographie les ressaisissent un par un. Au 31/03/2027, 1 500 de ces résultats, un sur quatre, n'avaient pas encore été saisis.
- En 2026, 800 indisponibilités ont été signalées, par téléphone, par courriel ou au cours d'une réunion, à des interlocuteurs différents : le centre de traitement de l'alerte, un centre d'incendie et de secours ou la cellule cartographie. Il s'est écoulé en moyenne 12 jours entre le signalement et la saisie dans la base ; s'y ajoute l'attente du chargement mensuel suivant dans le logiciel de traitement de l'alerte.
- Le 01/03/2027, l'auditeur a comparé la base et la carte du logiciel de traitement de l'alerte : 600 points d'eau diffèrent (état, position ou caractéristiques), dont 150 points indisponibles dans la base qui figurent comme disponibles sur la carte. Le fichier mensuel est chargé à la main par un agent du soutien du centre de traitement de l'alerte, sans contrôle du nombre de points chargés. Le chargement de septembre 2026 a échoué, et personne ne s'en est aperçu avant celui d'octobre.
- Un relevé sur le terrain de 200 points d'eau du Haut-Aurande a trouvé 20 points, un sur dix, placés sur la carte à plus de 100 mètres de leur position réelle.
- Les 1 200 comptes de la bureautique ont le droit de modifier la base : tout agent peut changer l'état, la position ou le débit d'un point d'eau.
- La base ne conserve que la dernière valeur de chaque donnée : on ne peut savoir ni qui a modifié un point d'eau, ni quand, ni quelle était la valeur précédente.
- La base est sauvegardée chaque nuit sur un disque de la salle informatique du siège, où se trouve aussi son serveur. Aucune restauration n'a jamais été essayée.
- Le 12/08/2026, lors de l'incendie d'un hangar agricole dans le Haut-Aurande, le premier engin s'est rendu au poteau d'incendie que la carte indiquait comme le plus proche. Ce poteau était hors service depuis trois semaines ; la commune l'avait signalé par courriel à un centre d'incendie et de secours. L'engin a dû rejoindre une réserve située à 2 km : l'alimentation en eau a été retardée d'environ 15 minutes, et le hangar a été détruit. Il n'y a pas eu de victime.

**C. Les réactions recueillies à la réunion de clôture**

**Lieutenant-colonel Bertrand OSSELIN, chef du groupement des opérations** : « Mes chefs d'agrès connaissent leur secteur : la carte n'est qu'une aide. Et la cellule cartographie n'a que trois agents. »

**Mme Solène VARANGEOT, cheffe du service des systèmes d'information et de communication** : « Une liaison automatique entre la base et le logiciel de l'alerte passe par l'éditeur de ce logiciel, et son calendrier est déjà chargé. »

**D. La demande du directeur départemental**

« Je veux une note de synthèse d'une page, que je présenterai au comité de direction du 7 juin 2027. Elle doit me dire ce qui est grave, ce que l'on fait, qui le fait et pour quand. »

### ANNEXE 3.2 – Le logiciel de traitement de l'alerte et son éditeur (note de Mme Solène VARANGEOT, cheffe du service des systèmes d'information et de communication, avril 2027)

**A. Le logiciel et son éditeur**

- Le logiciel de traitement de l'alerte, installé en 2012 et mis à niveau en 2019, reçoit les appels, localise l'appelant, propose les engins à engager et suit les interventions. Il échange des données avec l'enregistreur des appels, le logiciel des disponibilités des volontaires, la base des points d'eau et les tablettes des engins.
- Son éditeur est une société de 40 salariés, qui équipe une quinzaine de SDIS ; le nôtre est l'un de ses trois principaux clients. Il a annoncé que la version que nous utilisons ne serait plus maintenue après le 31/12/2029. Sa nouvelle version, proposée en ligne, était annoncée pour 2028 ; elle l'est désormais « à partir de 2029 », et aucun SDIS ne l'utilise encore.
- Chez l'éditeur, deux développeurs seulement connaissent nos interfaces, et l'un d'eux part à la retraite en 2028. Aucune documentation de ces interfaces ne nous a été remise.
- Le contrat de maintenance, renouvelé chaque année, ne prévoit ni la remise du code source si l'éditeur cessait son activité, ni d'aide à la sortie. L'éditeur intervient à distance sur nos serveurs par un accès ouvert en permanence, avec un compte commun à tous ses techniciens.

**B. Les serveurs et les pannes de 2026**

- Le logiciel fonctionne sur quatre serveurs dans la salle informatique du siège et sur deux serveurs dans la salle de secours de Montcerneau-Sud. Ces six serveurs ont été installés en 2017. Leur système d'exploitation ne reçoit plus de correctifs de sécurité depuis 2025 ; selon l'éditeur, notre version du logiciel ne fonctionne pas avec un système plus récent.
- Ces serveurs sont reliés au même réseau informatique que les postes de bureautique du siège et que les tablettes des engins (annexe 3.3).
- En juillet 2026, pendant un épisode de forte chaleur, la climatisation de la salle du siège est tombée en panne et les serveurs se sont arrêtés. La bascule sur la salle de secours a pris 45 minutes, pendant lesquelles une trentaine d'appels ont été traités sur papier ; la salle du siège n'est revenue en service qu'après 2 h 30.
- En novembre 2026, un correctif de l'éditeur, installé le même soir dans les deux salles, a bloqué pendant 2 heures la proposition des engins à engager. Les opérateurs ont choisi eux-mêmes les engins, à partir de tableaux imprimés. Un seul des deux développeurs a pu être joint.

**C. L'analyse demandée et les échelles du comité de direction**

Aucune analyse des risques du logiciel n'a été formalisée. Le directeur départemental veut présenter les principaux risques et leur traitement au conseil d'administration du 1er juillet 2027. Les échelles retenues par le comité de direction sont les suivantes :

| Niveau | Probabilité | Impact |
|---|---|---|
| 1 – faible | jamais constaté et peu plausible | gêne interne, sans effet sur le traitement des appels ni sur l'engagement des secours |
| 2 – moyen | constaté dans un autre SDIS, ou plausible sans être facile à provoquer | traitement de l'alerte dégradé (bascule sur la salle de secours, procédure sur papier, engins choisis à la main), sans arrêt de la réception des appels |
| 3 – fort | constaté au SDIS en 2026, certain à une date connue, ou facile à provoquer en l'état | réception des appels ou engagement des secours arrêtés dans les deux salles, ou impossibles à rétablir rapidement |

Quand plusieurs niveaux conviennent, on retient le plus élevé. Le comité de direction traite en priorité les risques dont la probabilité et l'impact sont tous deux de niveau 3. Aucune procédure de choix d'un nouvel éditeur n'est à organiser, et aucun chiffrage n'est demandé.

### ANNEXE 3.3 – Les tablettes embarquées et la transmission des comptes rendus de secours (constats de Mme Solène VARANGEOT et de Mme Coralie FAVERJON, déléguée à la protection des données, avril 2027)

**A. Les tablettes et les comptes rendus**

- Les 300 tablettes, installées en 2021, équipent les ambulances et les premiers engins de départ des 60 centres. Chacune est partagée par tous les équipages de son engin. Elle s'ouvre avec un code à quatre chiffres, le même pour toutes les tablettes d'un centre, inchangé depuis 2021 et connu des agents partis comme des nouveaux. L'application de comptes rendus de secours ne demande aucun identifiant : le chef d'agrès tape son nom au bas du compte rendu.
- Le chef d'agrès rédige sur la tablette un compte rendu par victime : identité, état de la victime, gestes réalisés ; environ 40 000 sont rédigés chaque année. La tablette l'envoie, en pièce jointe d'un courriel non chiffré, au centre de régulation médicale du SAMU et au service des urgences de l'hôpital qui accueille la victime, parmi les six hôpitaux du département. Une copie reste dans la tablette, qui n'est jamais vidée.
- 120 des 300 tablettes ont un système qui ne reçoit plus de mises à jour de sécurité. Le service des systèmes d'information et de communication ne peut ni localiser une tablette, ni la bloquer, ni l'effacer à distance.
- Les tablettes se connectent par le réseau mobile au réseau informatique du siège, le même que celui des postes de bureautique et des serveurs du logiciel de traitement de l'alerte.
- Les 300 tablettes seront remplacées de septembre à décembre 2027. Les besoins des nouvelles tablettes sont en cours de rédaction ; aucune procédure de choix du fournisseur n'est à organiser.

**B. Les pertes, les vols et deux incidents**

- 6 tablettes ont été perdues ou volées en 2025, 10 en 2026 : 8 oubliées sur les lieux d'une intervention ou perdues, 2 volées dans un engin.
- En octobre 2026, une tablette a été volée dans une ambulance pendant une intervention. Elle contenait plus de 1 000 comptes rendus de secours. Le centre a porté plainte ; Mme FAVERJON ne l'a appris que trois semaines plus tard, par hasard. Le code des tablettes du centre n'a pas été changé.
- En février 2027, le SDIS d'un département voisin a subi une attaque par rançongiciel. Selon l'écho qu'en a donné la presse, l'attaque, partie d'un courriel piégé ouvert sur un poste de bureautique, a gagné les serveurs de son traitement de l'alerte, arrêté pendant une journée ; ses appels ont été pris par les centres de traitement de l'alerte des départements voisins, dont le nôtre.

**C. Qui fait quoi aujourd'hui**

- Aucune politique de sécurité n'a été approuvée par la direction ; seule existe une charte d'usage, signée par chaque agent à son arrivée.
- Aucun responsable de la sécurité des systèmes d'information n'est désigné : Mme VARANGEOT et l'informaticien d'astreinte traitent les incidents « quand ils remontent ».
- Les chefs de centre communiquent le code des tablettes aux nouveaux arrivants et signalent les pertes « quand ils y pensent ».
- La cheffe du centre de traitement de l'alerte, la commandante Maëlle TOURNEVAL, décide de la bascule sur la salle de secours ; elle n'est pas consultée avant l'installation des correctifs du logiciel.
- L'éditeur du logiciel de traitement de l'alerte installe ses correctifs à distance, à la date qu'il choisit.
- La déléguée à la protection des données n'est informée ni des pertes de tablettes, ni des incidents.

### ANNEXE 3.4 – Les salles informatiques et la proposition du département (note de M. Pascal LAUZERAC, chef du groupement technique et logistique, avril 2027)

**A. Les deux salles du SDIS**

| Donnée | Salle du siège (Montcerneau) | Salle de secours (Montcerneau-Sud) |
|---|---|---|
| Serveurs | 40 : 10 pour le traitement de l'alerte, l'enregistreur des appels et la base des points d'eau ; 30 pour les applications de gestion | 4, pour le traitement de l'alerte et l'enregistreur des appels |
| Climatisation | installée en 2008, tombée en panne en juillet 2026 | installée en 2017 |
| Électricité consommée en 2026 | 400 MWh, dont 200 MWh pour les équipements informatiques | 30 MWh |

- Les 30 serveurs des applications de gestion portent la messagerie et la bureautique, les ressources humaines et la paie, le progiciel financier, la plateforme de formation, la gestion du parc, les indemnités des volontaires et les comptes rendus de secours. Seuls 8 d'entre eux sont virtualisés. Les processeurs des 30 serveurs sont utilisés en moyenne à 10 % de leur capacité.
- Les 900 postes de travail et les serveurs sont renouvelés tous les quatre ans. Les équipements remplacés sont remis à une entreprise de recyclage, qui les détruit. Les 300 tablettes de 2021 seront remplacées à la fin de 2027 (annexe 3.3).
- L'empreinte environnementale du système d'information n'a jamais été mesurée. Le projet d'établissement vise une baisse de 20 % de l'empreinte environnementale de l'établissement d'ici 2031.

**B. La proposition du département (courrier de la direction du numérique du département, mars 2027)**

- Le département a mis en service en 2024, à Montcerneau, une salle informatique où il héberge ses propres applications et celles de plusieurs collectivités. Il propose d'y héberger, à partir de 2028, les 30 serveurs des applications de gestion du SDIS, sous la forme de serveurs virtuels installés sur ses équipements.
- Cette salle est refroidie en grande partie par l'air extérieur. Sa consommation est mesurée en continu, et son indicateur d'efficacité énergétique (énergie totale consommée par la salle / énergie consommée par les équipements informatiques) est de 1,3. La chaleur qu'elle dégage chauffe un collège voisin.
- La salle est exploitée par les agents du département, présents les jours ouvrés de 8 heures à 18 heures ; en dehors de ces heures, aucune astreinte n'est prévue.
- Le traitement de l'alerte, l'enregistreur des appels et la base des points d'eau resteraient dans les salles du SDIS.
- Une convention entre le SDIS et le département fixerait les conditions de l'hébergement ; elle n'est pas rédigée. Aucun chiffrage n'est demandé.

**C. Deux avis**

**Mme Solène VARANGEOT** : « Nous gagnerions de la place et du temps. Mais la messagerie sert aussi à envoyer les comptes rendus de secours, jour et nuit. »

**M. Pascal LAUZERAC** : « Sans les 30 serveurs de gestion, la salle du siège consommerait beaucoup moins. Mais sa climatisation de 2008 resterait à remplacer pour les serveurs de l'alerte. »

Aucune mesure ni aucun calcul de l'empreinte n'est demandé.

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Sécurité de l'information | ISO/IEC 27001:2022 | norme d'exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques, dans une logique d'amélioration continue ; son annexe A compte 93 mesures en quatre thèmes (organisationnelles, liées aux personnes, physiques, technologiques) |
| Gestion des risques | ISO/IEC 27005:2022 | lignes directrices de gestion des risques liés à la sécurité de l'information : établir le contexte, identifier, analyser, évaluer puis traiter les risques, et les surveiller ; quatre options de traitement : réduire le risque, l'accepter, l'éviter ou le transférer (par exemple par une assurance) ; elle ne prescrit pas de méthode particulière |
| Appréciation des risques | EBIOS Risk Manager, version 1.5 (ANSSI, 2024) | méthode française d'appréciation et de traitement des risques numériques, compatible avec l'ISO/IEC 27005, en cinq ateliers : cadrage et socle de sécurité ; sources de risque et objectifs qu'elles visent ; scénarios stratégiques, qui passent par l'écosystème (éditeurs, prestataires, partenaires) ; scénarios opérationnels ; traitement du risque |
| Bonnes pratiques | Guide d'hygiène informatique de l'ANSSI, version de 2017 | guide de 42 mesures de sécurité, en niveau standard et renforcé, qui portent notamment sur l'authentification, les mises à jour, le cloisonnement des réseaux, les appareils nomades et les sauvegardes |
| Architecture de confiance | Le modèle Zero Trust, avis de l'ANSSI (2021) | modèle d'architecture, et non un produit : aucune confiance accordée d'office selon la place sur le réseau ; chaque accès est authentifié, autorisé et vérifié selon le contexte ; démarche progressive, qui ne remplace pas la défense en profondeur |
| Données personnelles | règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | les données personnelles sont protégées par des mesures de sécurité appropriées ; les données de santé sont des données sensibles, protégées de façon renforcée ; toute violation de données personnelles est inscrite dans un registre et, si elle présente un risque pour les personnes, notifiée à l'autorité de contrôle dans les meilleurs délais et, si possible, dans les 72 heures ; les personnes concernées sont informées en cas de risque élevé, sauf si les données étaient rendues incompréhensibles, par exemple par un chiffrement ; un organisme qui traite des données pour le compte du SDIS est un sous-traitant, lié par un contrat qui fixe notamment les mesures de sécurité ; le SDIS a désigné une déléguée à la protection des données, Mme Coralie FAVERJON ; aucune analyse juridique n'est attendue |

### Travail à faire

La base des points d'eau d'incendie n'est plus fiable, et un engin s'est rendu en 2026 à un poteau hors service. Le logiciel de traitement de l'alerte dépend d'un petit éditeur et d'une version qui ne sera plus maintenue après 2029. Les tablettes des engins transportent des données de santé sans protection, sur le réseau du siège. Les salles informatiques consomment beaucoup d'énergie pour des serveurs peu utilisés, alors que le projet d'établissement vise une baisse de 20 % de l'empreinte. Le colonel hors classe GRANVOISE vous demande de tirer les conclusions de l'audit de la base des points d'eau, d'analyser les risques du logiciel de traitement de l'alerte, de sécuriser les tablettes et la transmission des comptes rendus en clarifiant les rôles de chacun, et d'apprécier la proposition du département. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – Les conclusions de l'audit de la base des points d'eau d'incendie (3 points)**

a) Rédigez, à l'attention du colonel hors classe GRANVOISE, la note de synthèse de l'audit de la base des points d'eau (20 lignes au maximum) : une appréciation d'ensemble, puis quatre constats, regroupés à partir des notes brutes de l'annexe 3.1 B et hiérarchisés, chacun assorti du risque, de la recommandation, de son responsable et de son échéance. La note répond à l'objection du lieutenant-colonel OSSELIN. La démarche de l'audit n'est pas demandée.

b) Après avoir défini un critère d'appréciation en audit des systèmes d'information, présentez les trois critères que l'auditeur a mobilisés, la fiabilité des données, la sécurité et l'efficacité du processus : pour chacun, indiquez ce qui est attendu de la base et de sa mise à jour, et rattachez-y deux constats de l'annexe 3.1.

**3.2 – Les risques du logiciel de traitement de l'alerte (3 points)**

a) Identifiez, à partir de l'annexe 3.2, quatre risques liés au logiciel de traitement de l'alerte et à la dépendance envers son éditeur, formulés comme des événements redoutés. Classez-les selon la typologie des risques liés aux systèmes d'information, que vous présenterez brièvement, puis cotez leur probabilité et leur impact selon les échelles de l'annexe 3.2 C.

b) Après avoir comparé en quelques lignes l'approche de l'ISO/IEC 27005 et la méthode EBIOS Risk Manager (annexe 3.5), indiquez celle que le SDIS devrait employer pour l'analyse demandée par le directeur départemental, et justifiez votre choix.

c) Proposez un traitement pour chacun des deux risques les plus graves, en choisissant parmi les options de traitement (réduire, transférer, accepter, éviter) et en justifiant ce choix par leur probabilité et leur impact.

**3.3 – La sécurité des tablettes et la gouvernance du traitement de l'alerte (4 points)**

a) Après avoir défini l'architecture de confiance, proposez, à partir de l'annexe 3.3, quatre mesures de sécurité pour les tablettes et la transmission des comptes rendus de secours, portant respectivement sur l'authentification des équipages, le chiffrement, la séparation des réseaux et l'effacement à distance. Rattachez chaque mesure au risque qu'elle traite, dans le cadre d'une politique de sécurité fondée sur l'analyse des risques, et associez-lui un indicateur d'efficacité précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Aucun réglage d'équipement ni aucun essai technique n'est attendu.

b) Présentez, dans un tableau, les rôles et les responsabilités, dans la gouvernance du traitement de l'alerte, système critique, du directeur départemental, du (de la) chef(fe) du groupement « Pilotage et systèmes d'information », de la cheffe du service des systèmes d'information et de communication, de la cheffe du centre de traitement de l'alerte, des chefs de centre, de l'éditeur du logiciel de traitement de l'alerte et de la déléguée à la protection des données. Proposez la désignation d'un responsable de la sécurité des systèmes d'information et justifiez son positionnement.

**3.4 – Les salles informatiques et la transition numérique responsable (3 points)**

a) Après avoir défini la transition numérique responsable, appréciez la proposition du département de l'annexe 3.4 B : ce qu'elle apporte (mutualisation, efficacité de la salle, chaleur récupérée) et ses limites (dépendance, sécurité et confidentialité, système critique conservé dans les salles du SDIS). Indiquez à quelles conditions vous la recommanderiez.

b) Proposez deux autres bonnes pratiques de Green IT, l'une sur l'allongement de la durée de vie des équipements, l'autre sur leur réemploi, puis deux indicateurs de mesure de l'impact environnemental du système d'information, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe. Aucun calcul d'empreinte n'est attendu.
