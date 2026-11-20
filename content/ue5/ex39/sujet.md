# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 39

**DOSSIER 3 – FIABILISER, SÉCURISER ET RENDRE PLUS SOBRE LE SYSTÈME D'INFORMATION (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 3.1 – L'audit des caisses et de la billetterie des piscines (notes de travail de Mme Laure TRÉVAZIN, auditrice interne de la ville de Castelrive, mars 2027)

**A. Le cadre de la mission**

L'agglomération n'a pas de service d'audit interne. Depuis 2024, à la demande de la directrice générale des services de l'agglomération, Mme TRÉVAZIN, auditrice interne de la ville de Castelrive rattachée au directeur général des services de la ville, conduit chaque année une mission pour l'agglomération. Celle de 2027 porte sur les caisses et la billetterie des quatre piscines : vente des entrées et des abonnements aux accueils et sur internet, encaissements, fichier des abonnés. Elle s'est déroulée de janvier à mars 2027, sur les opérations de 2026.

Les quatre piscines ont reçu environ 600 000 entrées en 2026, pour environ 2 400 k€ de recettes (entrées, abonnements, leçons de natation). Les ventes sont enregistrées sur 14 postes de caisse, tenus par 60 agents d'accueil, et sur la billetterie en ligne mise en service en 2025.

**B. Les constats (notes brutes, dans l'ordre où ils ont été relevés)**

- Dans trois piscines sur quatre, chaque poste de caisse s'ouvre avec un identifiant et un mot de passe uniques, connus de toute l'équipe d'accueil : 45 des 60 agents travaillent sur un compte partagé. Le mot de passe de chaque caisse est noté dans le classeur des consignes, posé à l'accueil.
- 6 000 tickets ont été annulés en 2026, pour environ 30 k€. Une annulation ne demande ni motif ni validation d'un responsable, et personne ne consulte l'état des annulations. La moitié d'entre elles ont été enregistrées au centre aquatique, sur un compte partagé : on ne sait pas quel agent les a faites.
- Le total des encaissements constatés (espèces comptées en fin de journée, paiements par carte, ventes en ligne) est inférieur d'environ 18 k€ aux ventes enregistrées par la billetterie pour 2026. Les écarts quotidiens, de quelques euros à 400 €, sont notés sur la fiche de clôture, mais ils ne sont ni expliqués ni suivis.
- Le logiciel de caisse installé sur les postes n'a reçu aucune mise à jour depuis 2022 ; son éditeur a publié depuis cinq correctifs, dont deux de sécurité. Les postes de caisse fonctionnent avec un système d'exploitation dont le support a pris fin en 2025.
- Le réseau sans fil offert au public dans les halls des quatre piscines est relié au même réseau que les postes de caisse et que les terminaux de paiement par carte.
- Le fichier des abonnés compte 41 000 fiches (nom, adresse, date de naissance, photographie pour la carte d'accès, coordonnées bancaires pour les prélèvements) pour 9 000 abonnés actifs : 32 000 fiches sont celles de personnes qui n'ont plus d'abonnement, dont 25 000 depuis plus de trois ans. Aucune durée de conservation n'est fixée et le fichier n'a jamais été purgé.
- L'éditeur de la billetterie en ligne a mis six semaines à fournir l'extraction des annulations demandée pour l'audit.
- Les audits de 2021 (cabinet extérieur) et de 2023 (Mme TRÉVAZIN) avaient déjà relevé les comptes partagés et l'absence de validation des annulations. Chacun s'est conclu par un plan d'action accepté par la direction des piscines ; personne n'a vérifié ensuite s'il avait été appliqué. L'agglomération n'a ni comité d'audit ni tableau de suivi des recommandations.

**C. Les réactions recueillies à la réunion de clôture (mars 2027)**

**M. Didier SALVÉRAC, directeur des piscines et des équipements** : « Mes agents sont honnêtes. Un écart de 18 k€ pour 2,4 M€ de recettes, c'est moins de 1 %. Un identifiant par agent, ce sont des minutes perdues à chaque changement d'équipe, avec des familles qui attendent à l'accueil le samedi matin. Je conteste ces conclusions. »

**M. Thierry LANDOUSSE, directeur du numérique mutualisé** : « Le remplacement des postes de caisse et le réseau des piscines seront traités dans le prochain schéma directeur, à partir de 2028. D'ici là, je n'ai personne à y consacrer. Et la billetterie en ligne a été choisie sans nous. »

**Mme TRÉVAZIN** : « Je suis agente de la ville : mon programme de travail est arrêté par le directeur général des services de la ville, dont dépend aussi la direction du numérique, que plusieurs de mes constats concernent. À l'agglomération, certains parlent déjà de "l'audit de la ville". »

**D. La demande de la directrice générale des services**

Mme VARSANGE : « Je veux une note de synthèse d'une page, que je présenterai au comité de direction du 18 mai 2027, puis au président. Elle doit me dire ce qui est grave, ce que l'on fait, qui le fait et pour quand. Je ne veux pas d'un troisième plan d'action sans suite. »

### ANNEXE 3.2 – La chaîne « levée → facture » de la redevance incitative (note de Mme Sylvie DARNÉZAN, responsable du service de la facturation de la redevance, mars 2027)

**A. Le déroulement**

| Étape | Ce qui se passe | Acteur et outil |
|---|---|---|
| 1. Lecture | à chaque levée, le lecteur du camion lit la puce du bac ; l'ordinateur embarqué enregistre le numéro de la puce, la date, l'heure, le camion et la tournée | équipage ; lecteur et ordinateur embarqué |
| 2. Transmission | au retour au dépôt, l'ordinateur embarqué envoie le fichier des levées de la tournée, par le réseau mobile, à un serveur d'échange de la direction du numérique mutualisée situé dans la salle informatique du siège ; il efface ensuite son fichier | ordinateur embarqué ; serveur d'échange |
| 3. Import | chaque nuit, le serveur d'échange dépose les fichiers reçus dans le logiciel de facturation, qui les importe ; chaque matin, un agent du service lit le compte rendu de l'import et réimporte à la main les fichiers rejetés | service de la facturation ; logiciel de facturation, hébergé par son éditeur |
| 4. Calcul et édition | deux fois par an, l'agent chargé du paramétrage saisit les tarifs votés par le conseil communautaire, lance le calcul de la part fixe et de la part variable, puis l'édition des 84 000 factures du semestre | un agent du service ; logiciel de facturation |
| 5. Transmission au comptable public | après l'édition, le logiciel transmet au comptable public les éléments nécessaires au recouvrement des factures (étape qui n'est pas à étudier) | logiciel de facturation |
| 6. Réclamations | les usagers contestent par courriel, par le formulaire du site ou à l'accueil ; un agent corrige, s'il y a lieu, la levée ou la facture dans le logiciel | service de la facturation |

**B. Les constats de 2026**

- En 2026, les 40 camions ont effectué environ 12 000 tournées et lu environ 2 millions de levées. 120 tournées (1 %) n'ont pas été reçues, ou l'ont été incomplètes : camion rentré au dépôt dans une zone mal couverte par le réseau mobile, ordinateur embarqué éteint avant la fin de l'envoi. Comme l'ordinateur efface son fichier après chaque tentative d'envoi, environ 20 000 levées ont été perdues ; elles n'ont pas été facturées.
- 300 fichiers ont été rejetés par le logiciel (format incorrect, nom de fichier déjà utilisé) et réimportés à la main ; certains l'ont été deux fois : environ 5 000 levées ont ainsi été facturées en double, ce que des réclamations ont révélé.
- Le même agent saisit les tarifs et lance la facturation, et personne ne contrôle ses saisies. En juillet 2026, le prix de la levée au-delà du forfait a été saisi à 25 € au lieu de 2,50 € pour les bacs de 240 litres : 3 000 factures erronées ont été envoyées, et 900 usagers ont réclamé avant que l'erreur ne soit comprise.
- Les six agents qui traitent les réclamations utilisent le même compte « facturation ». Le logiciel ne garde aucune trace des corrections : 4 000 factures ont été modifiées en 2026, sans que l'on sache qui les a modifiées, pourquoi, ni quelle était la valeur d'origine.
- Personne ne rapproche le nombre de levées importées dans le logiciel du nombre de levées enregistrées par les camions, ni de la liste des tournées réalisées : une tournée dont le fichier manque passe inaperçue.
- L'éditeur déclare sauvegarder chaque nuit la base du logiciel de facturation ; le contrat ne fixe ni délai de restauration ni perte de données admissible, et aucune restauration n'a jamais été essayée. Le serveur d'échange du siège est sauvegardé sur un disque placé dans la même salle. En octobre 2026, après la suppression par erreur d'un répertoire de ce serveur, la direction du numérique a constaté que la dernière sauvegarde exploitable datait de deux mois : la sauvegarde ne fonctionnait plus depuis l'été, sans que personne s'en aperçoive. Les fichiers supprimés avaient heureusement déjà été importés.

**C. L'enjeu selon Mme DARNÉZAN**

« Chaque facture fausse, c'est une réclamation, un usager mécontent et un élu interpellé : la redevance n'est acceptée que si elle est juste. La prochaine facturation, celle du premier semestre 2027, sera lancée en juillet 2027. »

### ANNEXE 3.3 – Les équipements connectés et les systèmes techniques (note de M. Bastien MERLANDOT, responsable de la sécurité des systèmes d'information mutualisé, mars 2027)

**A. L'inventaire que j'ai pu reconstituer**

| Équipements | Direction utilisatrice | Maintenance | Constats |
|---|---|---|---|
| Ordinateurs embarqués et lecteurs de puces des 40 camions | collecte et déchèteries | fabricant des équipements embarqués (contrat de maintenance) | installés en 2024 et jamais mis à jour ; le même mot de passe d'administration, celui livré par le fabricant, sur les 40 ordinateurs ; une carte d'accès au réseau mobile dans chaque camion |
| Capteurs de remplissage des 300 colonnes de verre, posés en 2026 | collecte et déchèteries | fabricant des capteurs, qui héberge la plateforme en ligne | mesures transmises sans chiffrement ; un seul compte d'accès à la plateforme, partagé par 8 agents |
| Contrôle d'accès des six déchèteries : lecteurs de badges, caméras de lecture des plaques d'immatriculation des véhicules des professionnels, barrières | collecte et déchèteries | éditeur du logiciel de contrôle d'accès | logiciel installé sur un serveur de la salle informatique du siège ; caméras reliées au réseau de bureau ; images des plaques conservées sans limite de durée |
| Télégestion des chaufferies et du traitement de l'eau des quatre piscines : automates et poste de supervision | piscines et équipements | mainteneur des chaufferies (contrat) | le mainteneur y accède à distance, à tout moment, par un logiciel de prise de main installé sur le poste de supervision, avec un compte unique partagé par ses 12 techniciens et un mot de passe inchangé depuis 2019 ; le poste de supervision sert aussi à consulter la messagerie |

Ces équipements sont reliés au même réseau que les postes de bureau de l'agglomération, lui-même relié à celui de la ville. Aucun d'eux ne figure dans l'inventaire de la direction du numérique mutualisée. Aucun contrat de maintenance ne traite de la sécurité : ni les mises à jour, ni les accès à distance, ni le signalement d'un incident.

**B. Les incidents**

- En novembre 2026, une communauté de communes voisine a dû fermer ses deux piscines pendant trois semaines : un rançongiciel, entré par l'accès à distance d'un mainteneur, avait chiffré le poste de supervision de ses chaufferies, puis ses serveurs de bureau. Le traitement de l'eau ne pouvait plus être piloté ni contrôlé à distance.
- En septembre 2026, la panne du serveur du contrôle d'accès a bloqué les barrières des six déchèteries de l'agglomération pendant tout un samedi : environ 2 000 usagers ont été refoulés ou admis sans contrôle.
- En 2026, le fabricant des équipements embarqués a publié une mise à jour qui corrige une faille de ses ordinateurs ; elle n'a pas été installée.

**C. Qui fait quoi ? (propos recueillis en mars 2027)**

**M. SALVÉRAC, directeur des piscines et des équipements** : « La télégestion, c'est technique : c'est l'affaire du mainteneur et de la direction du numérique. »

**M. LANDOUSSE, directeur du numérique mutualisé** : « Nous gérons les postes de bureau, les serveurs et le réseau. Les automates, les camions et les capteurs ne sont pas dans notre inventaire, et nous ne signons pas les contrats des directions de l'agglomération : nous ne savons pas ce que les mainteneurs y font. »

**Le chef d'agence du mainteneur des chaufferies** : « Notre contrat porte sur le chauffage et sur le traitement de l'eau, pas sur l'informatique. L'accès à distance nous permet d'intervenir vite, la nuit. »

**Le fabricant des équipements embarqués** : « Les mises à jour sont disponibles sur notre portail ; c'est au client de les installer. »

**M. MERLANDOT** : « Je suis arrivé en 2026. Je suis agent de la ville, rattaché au directeur du numérique, et je n'ai aucune autorité sur les directions de l'agglomération ni sur leurs prestataires. La politique de sécurité de 2023 ne dit rien des équipements techniques. »

### ANNEXE 3.4 – Le numérique de l'agglomération et son empreinte (note de Mme Aurore PRÉVILLAN, chargée de mission pour la transition écologique de l'agglomération, mars 2027)

**A. Une stratégie qui manque**

« L'agglomération n'a pas adopté la stratégie numérique responsable prévue par la loi pour les établissements de plus de 50 000 habitants (annexe 3.5) ; la ville de Castelrive non plus. En 2023, un groupe de volontaires a affiché dix "écogestes" dans les bureaux. Depuis, personne n'est chargé du sujet, et l'empreinte du numérique n'a jamais été présentée aux élus. »

**B. L'état des lieux (agglomération, 2026, ordres de grandeur)**

| Domaine | Situation |
|---|---|
| Postes de travail | 550 postes fixes et portables, renouvelés tous les quatre ans par lots entiers, y compris ceux qui fonctionnent ; 900 écrans |
| Téléphones et tablettes | 700 téléphones mobiles de service, renouvelés tous les deux ans dans le cadre de l'offre de l'opérateur ; 250 tablettes achetées en 2024 pour les agents de terrain, dont 30 % n'ont jamais été utilisées |
| Équipements retirés | environ 400 postes et 900 téléphones stockés au sous-sol du siège, en attente d'enlèvement par un collecteur de déchets électroniques |
| Impressions | 150 imprimantes individuelles et 30 copieurs ; environ 4 millions de pages imprimées en 2026 |
| Salles informatiques, communes à la ville et à l'agglomération | 120 serveurs physiques, utilisés en moyenne à 15 % de leur capacité, dont 40 n'hébergent plus aucune application utilisée ; climatisation ancienne ; indicateur d'efficacité énergétique (PUE) de 2,2 à l'hôtel de ville et de 2,0 au siège, quand des centres de données récents visent 1,3 à 1,5 ; environ 900 MWh consommés en 2026 |
| Achats | matériels choisis par la direction du numérique mutualisée sur le seul critère du prix, sans exigence de durée de garantie, de réparabilité ou de reprise |
| Services en ligne | formulaires du site, logiciel de facturation de la redevance, billetterie des piscines, plateforme des capteurs : hébergés par leurs éditeurs, qui ne donnent aucune information sur leur consommation |

**C. Les premières mesures (bilan simplifié établi fin 2026 par un bureau d'études)**

- Empreinte carbone du numérique de l'agglomération : environ 300 tCO2e en 2026, hors services hébergés par les éditeurs, faute de données.
- Répartition : fabrication des équipements (postes, écrans, téléphones, tablettes, imprimantes, part des serveurs) environ 70 % ; électricité des salles informatiques et des postes (environ 1 100 MWh, y compris la totalité des deux salles communes, faute de clé de répartition avec la ville) environ 20 % ; impressions et autres usages environ 10 %.
- Le bureau d'études précise que ces résultats sont des estimations, établies avec des facteurs d'émission moyens.

**D. Le projet de tournées optimisées**

La direction de la collecte propose, avec une jeune entreprise, d'équiper 2 000 bacs collectifs (immeubles et professionnels) de capteurs de remplissage à pile, d'une durée de vie de cinq ans, et de calculer chaque nuit les tournées du lendemain au moyen d'un modèle d'apprentissage automatique hébergé dans le cloud de cette entreprise ; chaque camion recevrait sa tournée sur une nouvelle tablette. Gain annoncé par la jeune entreprise : 10 % de kilomètres en moins, soit environ 120 000 km sur 1,2 million parcourus chaque année, et environ 150 tCO2e de gazole évitées par an. Elle ne donne aucune estimation de l'empreinte de ses capteurs, de ses calculs ni des tablettes.

**M. Rémi BASTÉROLE, vice-président chargé des déchets et de la prévention** : « C'est la meilleure action pour le climat de toute l'agglomération : 150 tonnes évitées, la moitié de l'empreinte de tout notre numérique. Je veux les 2 000 capteurs dès cette année. »

**Mme PRÉVILLAN** : « Je ne suis pas contre. Mais nous ne savons pas ce que coûteront, en carbone et en déchets, 2 000 capteurs à pile renouvelés tous les cinq ans, de nouvelles tablettes et un calcul chaque nuit. Et dans les communes rurales, les tournées changent peu d'une semaine à l'autre. »

### ANNEXE 3.5 – Repères (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| ISO/IEC 27001:2022 et ISO/IEC 27002:2022 | La première spécifie les exigences d'un système de management de la sécurité de l'information fondé sur l'appréciation des risques, avec 93 mesures en annexe A (dont le contrôle d'accès, l'authentification, la journalisation, la gestion des vulnérabilités, la sauvegarde, la séparation des réseaux, la cryptographie et la sécurité des relations avec les fournisseurs) ; la seconde est le guide de mise en œuvre de ces mesures. | En vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | 42 mesures de bonnes pratiques, dont la maîtrise des risques liés aux prestataires, l'identification nominative de chaque personne qui accède au système, le changement des éléments d'authentification par défaut des équipements, le cloisonnement du réseau et une politique de mise à jour des logiciels et des équipements. | En vigueur |
| Le modèle Zero Trust (avis de l'ANSSI, 2021) | Modèle d'architecture : aucune confiance implicite n'est accordée à un utilisateur, à un équipement ou à une connexion du seul fait de sa place dans le réseau ; chaque accès est authentifié, autorisé et contrôlé. Il s'adopte progressivement et ne remplace pas la défense en profondeur ; ce n'est pas un produit. | Publié en 2021 |
| COSO 2013 (contrôle interne) | Cinq composantes du contrôle interne : environnement de contrôle, évaluation des risques, activités de contrôle, information et communication, pilotage (suivi du dispositif et des faiblesses relevées). | Version 2013 |
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Les données sont conservées sous une forme permettant d'identifier les personnes pendant une durée n'excédant pas celle nécessaire aux finalités du traitement ; le responsable du traitement met en œuvre des mesures de sécurité adaptées au risque. | Applicable depuis le 25/05/2018 |
| Règlement (UE) 2024/2847 sur la cyber-résilience (Cyber Resilience Act) | Exigences de cybersécurité pour les produits comportant des éléments numériques mis sur le marché, à la charge des fabricants : sécurité dès la conception, gestion des vulnérabilités, mises à jour de sécurité. | Signalement des vulnérabilités activement exploitées par les fabricants depuis le 11/09/2026 ; application générale le 11/12/2027 |
| Loi n° 2021-1485 du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique en France (REEN) | Sensibilisation au numérique responsable, allongement de la durée de vie des équipements, écoconception des services numériques, centres de données et réseaux moins énergivores ; les communes et les établissements publics de coopération intercommunale de plus de 50 000 habitants définissent une stratégie numérique responsable. | En vigueur ; stratégie à définir au plus tard le 01/01/2025 |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | Critères d'écoconception regroupés par thèmes (stratégie, spécifications, architecture, contenus, hébergement, algorithmie et intelligence artificielle…), dont l'interrogation du besoin et la publication d'une déclaration d'écoconception. | Version 2 publiée le 17/05/2024 |
| Étude ADEME-Arcep sur l'empreinte environnementale du numérique | Le numérique représente environ 4,4 % de l'empreinte carbone de la France en 2022. Les terminaux en représentent environ la moitié, surtout du fait de leur fabrication ; les centres de données, y compris ceux situés à l'étranger, environ 46 % ; les réseaux, environ 4 %. | Mise à jour du 17/01/2025 |

Il n'est demandé aucune analyse juridique.

### Travail à faire

Une collectivité voisine a dû fermer ses piscines après une cyberattaque, les audits des piscines restent sans suite, la facture de la redevance n'est acceptée que si elle est juste, et la stratégie numérique responsable prévue par la loi n'a pas été adoptée. Mme VARSANGE vous demande de faire de l'audit des piscines un audit suivi d'effets, de fiabiliser la chaîne de facturation de la redevance avant la facturation de juillet 2027, de sécuriser les équipements connectés et les systèmes techniques et de proposer la stratégie numérique responsable de l'agglomération. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.5 ainsi que vos connaissances professionnelles.

**3.1 – La note de synthèse de l'audit des piscines et ses suites (2,5 points)**

a) Après avoir précisé ce qui distingue une note de synthèse d'audit d'un rapport d'audit, rédigez, à l'attention de Mme VARSANGE, la note de synthèse de l'audit des caisses et de la billetterie des piscines (20 lignes au maximum) : une appréciation globale, puis quatre constats hiérarchisés, chacun assorti du risque, de la recommandation, de son responsable, de sa priorité et de son échéance. La démarche de l'audit et ses tests ne sont pas demandés.

b) Indiquez deux facteurs de succès et deux points de vigilance pour que cet audit soit, cette fois, suivi d'effets, au regard des réactions relatées dans l'annexe 3.1 et de la mutualisation entre la ville et l'agglomération.

**3.2 – La fiabilité de la chaîne « levée → facture » (3 points)**

Après avoir défini la fiabilisation d'un système d'information de gestion et distingué les contrôles généraux informatiques des contrôles applicatifs, proposez quatre contrôles qui fiabilisent la chaîne « levée → facture », portant respectivement sur l'intégrité de l'interface entre les camions et le logiciel de facturation, sur les tarifs et le calcul des factures, sur la traçabilité des corrections, et sur la sauvegarde et la restauration. Pour chacun, précisez le constat de l'annexe 3.2 auquel il répond, le risque qu'il traite, sa nature (préventive ou détective) et qui le met en œuvre. Indiquez enfin celui que vous mettriez en place en premier, avant la facturation de juillet 2027, en le justifiant. Aucune règle de comptabilité publique ni de finances locales n'est attendue.

**3.3 – Les risques et la sécurité des équipements connectés et des systèmes techniques (3,5 points)**

a) Après avoir présenté la typologie des risques liés aux systèmes d'information (cybermenaces, défaillances opérationnelles, risques réglementaires et métiers), classez cinq risques révélés par l'annexe 3.3, en couvrant les trois catégories, puis retenez-en deux prioritaires en justifiant votre choix par leur probabilité et leur impact.

b) Après avoir défini l'architecture de confiance, proposez-en quatre principes pour les équipements connectés et les systèmes techniques, portant respectivement sur la séparation entre les réseaux techniques et le réseau de bureau, sur l'authentification et la traçabilité des accès à distance des mainteneurs, sur le chiffrement et sur les mises à jour. Reliez chacun à un constat de l'annexe 3.3. Aucun paramétrage n'est attendu.

c) Répartissez les rôles et les responsabilités de la sécurité de ces équipements entre l'agglomération (directrice générale des services et directions utilisatrices), la direction du numérique mutualisée et son responsable de la sécurité des systèmes d'information, les éditeurs et les fabricants, et les mainteneurs. Indiquez ensuite comment cette répartition sera formalisée et comment devrait évoluer le positionnement du responsable de la sécurité des systèmes d'information. Aucune analyse juridique des contrats ni de la convention de mutualisation n'est attendue.

**3.4 – La stratégie numérique responsable de l'agglomération (4 points)**

a) Après avoir défini la sobriété numérique et distingué le Green IT de l'IT for green, situez l'agglomération sur une grille de maturité du numérique responsable à quatre niveaux (initial, engagé, structuré, piloté) : pour trois dimensions au moins, décrivez son niveau actuel et le niveau visé en 2030. Proposez ensuite sa stratégie numérique responsable : quatre axes priorisés, chacun relié à un constat de l'annexe 3.4, la gouvernance qui la portera et sa trajectoire jusqu'en 2030. Aucun calcul d'empreinte n'est attendu.

b) Appréciez le projet de tournées optimisées de l'annexe 3.4 D au regard de la sobriété numérique : deux arguments en sa faveur, deux limites, puis les conditions auxquelles vous le recommanderiez.

c) Proposez deux indicateurs de suivi de la stratégie numérique responsable, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
