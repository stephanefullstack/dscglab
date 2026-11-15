# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 21

**DOSSIER 3 – MAÎTRISER LES RISQUES DES JOURS DE MATCH ET L'EMPREINTE DU STADE CONNECTÉ (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 7, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en juin 2027. MONTALBRET XV est le club de rugby professionnel de l'agglomération de Montalbret, ville fictive du Sud-Ouest de 180 000 habitants. Il est exploité par une société anonyme sportive professionnelle détenue à 80 % par la holding familiale de son président, M. Damien ROQUESSOL, et à 20 % par l'association MONTALBRET XV, qui gère la formation et les équipes amateurs. Le club dispute la deuxième division professionnelle et vise l'accession à l'élite d'ici 2030. Il emploie 150 salariés permanents, dont 48 joueurs et entraîneurs, et fait appel les jours de match à environ 400 intervenants extérieurs (accueil, sécurité, restauration). Il joue dans un stade de 16 000 places appartenant à la communauté d'agglomération et compte 7 000 abonnés. Son chiffre d'affaires de la saison 2025-2026 s'élève à 28 millions d'euros ; 0,9 million d'euros est consacré au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « MONTALBRET 2030 », adopté par le conseil d'administration en janvier 2027, fixe trois priorités : mieux connaître les supporters et les partenaires pour développer les recettes hors droits sportifs ; structurer la gouvernance du numérique du club et étudier de nouvelles formes de relation avec les supporters ; fiabiliser l'organisation des jours de match dans un stade modernisé et réduire son empreinte environnementale. La directrice générale, Mme Inès LAFERRADE, en rend compte chaque trimestre au conseil d'administration.

Vous êtes responsable administratif et financier de MONTALBRET XV depuis 2025. Mme LAFERRADE vous a aussi confié la responsabilité du système d'information du club, et elle vous demande trois travaux : organiser et valoriser les données des supporters (dossier 1) ; gouverner le numérique du club et évaluer le projet de jetons de supporters (dossier 2) ; maîtriser les risques des jours de match et l'empreinte du stade connecté (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de MONTALBRET XV et chiffres clés

MONTALBRET XV est une société anonyme sportive professionnelle qui exploite le club de rugby professionnel de l'agglomération de Montalbret, ville fictive du Sud-Ouest de 180 000 habitants. Elle est détenue à 80 % par la holding familiale de son président et à 20 % par l'association MONTALBRET XV, qui gère la formation et les équipes amateurs. La saison sportive court de juillet à juin : la saison 2025-2026 est la dernière saison close, la saison 2026-2027 est en cours de clôture. Le club dispute la deuxième division professionnelle et vise l'accession à l'élite d'ici 2030.

**Chiffres clés de la saison 2025-2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires | 28 M€ : partenariats et publicité 11 M€ ; billetterie et abonnements 6 M€ ; droits audiovisuels et dotations 5 M€ ; hospitalités (loges, salons) 4 M€ ; boutique et licences 2 M€ |
| Matchs à domicile | 15 par saison, environ 12 000 spectateurs en moyenne |
| Effectif | 150 salariés permanents, dont 48 joueurs et entraîneurs ; environ 400 intervenants extérieurs les jours de match (accueil, sécurité, restauration), fournis par des prestataires |
| Stade | 16 000 places, propriété de la communauté d'agglomération, mis à la disposition du club ; modernisation en cours (écran géant, éclairage, réseau sans fil pour le public, contrôle d'accès par billet dématérialisé) |
| Supporters et clients | 7 000 abonnés ; environ 120 000 contacts dans les fichiers du club (billetterie, boutique en ligne, application mobile, lettre d'information) ; 250 entreprises partenaires |
| Budget du système d'information | 0,9 M€ (environ 3 % du chiffre d'affaires) |
| Plan « MONTALBRET 2030 » (adopté en janvier 2027) | mieux connaître les supporters et les partenaires pour développer les recettes hors droits sportifs ; structurer la gouvernance du numérique du club et étudier de nouvelles formes de relation avec les supporters ; fiabiliser l'organisation des jours de match dans un stade modernisé et réduire son empreinte environnementale |

**Organigramme simplifié (juin 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil d'administration | représentants de la holding familiale et de l'association MONTALBRET XV ; se réunit chaque trimestre | — |
| Présidence | président du conseil d'administration | M. Damien ROQUESSOL |
| Direction générale | directrice générale, qui porte le plan « MONTALBRET 2030 » | Mme Inès LAFERRADE |
| Rattaché à la directrice générale | directeur sportif (équipe professionnelle, staff technique et médical, lien avec le centre de formation de l'association) | M. Xavier TOURNEBIAU |
| Rattaché à la directrice générale | directeur commercial et des partenariats (partenaires, hospitalités, loges et salons) | M. Cédric BARRALOU |
| Rattachée à la directrice générale | responsable du pôle marketing et numérique (communication, lettre d'information, réseaux sociaux, application mobile, boutique en ligne) | Mme Léa SOUBIRAC |
| Rattachée à la directrice générale | responsable de la billetterie (abonnements, billets, accueil du public au guichet) | Mme Nathalie ARRIBEUX |
| Rattaché(e) à la directrice générale | responsable administratif et financier (comptabilité, contrôle de gestion, ressources humaines, achats, juridique, système d'information) | vous |
| Rattaché au responsable administratif et financier | responsable informatique | M. Bastien PEYRASTRE |
| Rattaché à la directrice générale | responsable du stade et de la sécurité (exploitation du stade, organisation des jours de match, relations avec les prestataires d'accueil et de sécurité) | M. Franck DOUMERGAT |

### ANNEXE 3.1 – Le système d'information d'un jour de match (note de M. Franck DOUMERGAT, responsable du stade et de la sécurité, mai 2027)

La modernisation du stade, conduite en 2026 par la communauté d'agglomération avec le club, a fait du jour de match une chaîne de systèmes numériques. Un match du vendredi se déroule ainsi (coup d'envoi à 21 h).

**A. Déroulé d'un jour de match**

| Moment | Activité | Systèmes utilisés | Acteurs |
|---|---|---|---|
| Veille et jour du match, jusqu'à 17 h | préparation de l'entrée du public | la billetterie (logiciel en mode SaaS) transmet par une interface de programmation (API) la liste des billets et des cartes d'abonnement valides au logiciel de contrôle d'accès, installé sur un serveur du local technique du stade ; les billets des partenaires et des loges sont envoyés aux partenaires sous forme de fichiers par courriel | billetterie ; PORTALVÈNE Accès |
| De 17 h à 19 h | préparation du stade | consignes et affectation des 400 intervenants diffusées dans un groupe de messagerie instantanée grand public créé par le prestataire d'accueil ; essais de l'écran géant, de la sonorisation et de l'éclairage depuis la régie | responsable du stade ; GARDALEINE Sécurité ; prestataire d'accueil ; agent technique de l'agglomération |
| 19 h, ouverture des portes | entrée de 12 000 à 16 000 spectateurs en deux heures | contrôle d'accès par billet dématérialisé : 80 lecteurs répartis sur 8 entrées lisent le code du billet sur le téléphone du spectateur ou la carte d'abonnement ; le poste de supervision indique en temps réel le nombre d'entrées par tribune | agents de GARDALEINE Sécurité ; 30 superviseurs (agents de GARDALEINE et salariés du club) |
| De 19 h à la fin du match | restauration | paiement sans espèces (carte bancaire, carte d'abonnement rechargeable) sur les 60 terminaux de paiement des 30 buvettes, reliés à la plateforme de SOLDÉRIS Paiement | prestataire de restauration ; SOLDÉRIS Paiement |
| Pendant tout l'événement | animation et sécurité du public | écran géant (vidéo du match, ralentis, messages des partenaires, consignes de sécurité) et sonorisation, pilotés depuis la régie ; les vidéos et les messages sont remis à la régie par le pôle marketing et numérique sur une clé USB ; réseau sans fil gratuit pour le public (120 bornes), environ 5 000 connexions simultanées ; diffusion en direct sur l'application mobile du club des images d'avant-match | pôle marketing et numérique ; régisseur ; agglomération |
| Après le match | clôture | export des passages enregistrés au contrôle d'accès ; relevé des ventes des buvettes, sur lequel le club perçoit une redevance | billetterie ; prestataire de restauration |

**B. Acteurs et responsabilités**

| Acteur | Rôle dans les systèmes du jour de match | Cadre écrit |
|---|---|---|
| Communauté d'agglomération (M. Paul CASTÉRADE, directeur des équipements sportifs) | propriétaire du stade ; a financé et fait installer en 2026 l'écran géant, l'éclairage pilotable, les 120 bornes du réseau sans fil et le câblage des réseaux du stade ; un agent technique est présent les soirs de match | convention de mise à disposition du stade signée en 2024 pour dix ans |
| Club : responsable du stade et de la sécurité | organise le jour de match ; a choisi PORTALVÈNE Accès et signé son contrat ; coordonne les prestataires | contrats des prestataires |
| Club : informatique (M. Bastien PEYRASTRE et un technicien, avec un prestataire d'infogérance) | gère le réseau administratif du club et les postes des bureaux ; associée au contrôle d'accès trois mois avant sa mise en service | — |
| PORTALVÈNE Accès | fournit les lecteurs, le logiciel et le serveur du contrôle d'accès ; les maintient à distance par un accès permanent | contrat de 2026, trois saisons, 60 000 € par an |
| SOLDÉRIS Paiement | fournit les terminaux, la plateforme de paiement et les cartes rechargeables | contrat avec le prestataire de restauration |
| GARDALEINE Sécurité et le prestataire d'accueil | fournissent environ 400 intervenants : agents de sécurité et de contrôle aux entrées, stewards, hôtesses | contrats de prestation |

**C. Les trois réseaux du stade**
- Le **réseau du public** relie les 120 bornes du réseau sans fil ; il est exploité par l'opérateur de la communauté d'agglomération.
- Le **réseau des systèmes du stade** relie le contrôle d'accès, l'éclairage pilotable, l'écran géant, la sonorisation et les terminaux de paiement des buvettes ; il a été installé par la communauté d'agglomération en 2026.
- Le **réseau administratif du club** relie les bureaux du club, situés dans la tribune Ouest : postes de travail, messagerie, accès aux logiciels en ligne (dont la billetterie).
- Interconnexions : le poste de supervision du contrôle d'accès est installé dans les bureaux du club et relié à la fois au réseau administratif et au réseau des systèmes du stade ; PORTALVÈNE Accès accède à son serveur depuis Internet ; dans la tribune Est, les terminaux de paiement des six buvettes sont raccordés au réseau du public (voir l'annexe 3.3).

### ANNEXE 3.2 – Deux incidents de la saison 2026-2027

**A. La panne du contrôle d'accès du vendredi 5 mars 2027**

Le match, joué à guichets fermés (16 000 spectateurs), opposait le club au premier du championnat. À 17 h, PORTALVÈNE Accès a installé à distance une mise à jour de son logiciel, sans en informer le club. À 19 h 05, à l'ouverture des portes, les 80 lecteurs ont refusé tous les billets. L'astreinte de PORTALVÈNE Accès, ouverte du lundi au vendredi de 9 h à 18 h, ne répondait pas ; à 19 h 40, un ingénieur joint sur son téléphone personnel a remis en service la version précédente du logiciel. La panne a duré 35 minutes.

Faute de consigne écrite, les agents ont d'abord fermé les entrées, puis, à partir de 19 h 25, sur instruction orale du responsable du stade, laissé entrer environ 2 000 spectateurs à deux entrées en vérifiant le billet à l'œil sur le téléphone. Les files d'attente ont atteint 45 minutes.

Conséquences relevées :
- 3 000 spectateurs sont entrés après le coup d'envoi, avec jusqu'à 30 minutes de retard, dont 200 invités de partenaires installés en loge ;
- les passages des 2 000 spectateurs entrés sans lecture ne sont pas enregistrés : le nombre d'entrées par tribune de ce match est inconnu ;
- le club a offert un avoir de 15 € aux 3 000 spectateurs entrés en retard, utilisable sur un prochain billet ou à la boutique, soit 45 000 € ; la redevance perçue sur les ventes des buvettes a été inférieure de 10 000 € à celle d'un match comparable ; les heures supplémentaires des prestataires ont coûté 5 000 € ; au total, 60 000 € ;
- la billetterie a traité 1 200 réclamations en trois semaines ; environ 2 000 messages critiques ont été publiés sur les réseaux sociaux le soir même ;
- le contrat de PORTALVÈNE Accès ne prévoyant aucun délai de rétablissement, le club n'a pu lui opposer aucune pénalité.

**B. Les faux billets du samedi 16 janvier 2027**

Pour ce match (13 000 spectateurs), un partenaire a reçu par courriel, comme chaque fois, un fichier de 400 billets d'invitation non nominatifs, accompagné de la liste de ses invités (nom et adresse électronique). Un de ses salariés a déposé ce fichier sur un service de partage en ligne, avec un lien accessible à toute personne qui le connaissait. Des copies des billets ont été revendues 25 € pièce sur un réseau social, sous une annonce qui reprenait le logo du club.

Le jour du match, 1 100 personnes se sont présentées avec un billet issu de ce fichier : les 400 premières sont entrées ; 700 ont été refusées aux lecteurs, le billet ayant déjà servi, dont 150 invités du partenaire, entrés après vérification de leur identité à la billetterie, et 550 acheteurs de copies, refoulés. Le logiciel de contrôle d'accès n'a émis aucune alerte : les agents n'ont compris la situation qu'après une heure. L'incident a coûté environ 10 000 € au club (renfort d'agents, traitement des réclamations, gestes envers le partenaire). Le club ne sait pas s'il doit signaler la diffusion de la liste des invités à l'autorité de contrôle ; aucune décision n'a été prise.

Repère (au 31/12/2026) : le règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018, impose au responsable du traitement de notifier à l'autorité de contrôle une violation de données à caractère personnel dans les 72 heures après en avoir pris connaissance, sauf si elle n'est pas susceptible d'engendrer un risque pour les droits et libertés des personnes.

### ANNEXE 3.3 – Constats de l'audit flash des systèmes du jour de match (cabinet ARMÉLIAC Conseil, avril 2027)

**Périmètre et méthode.** Mission de huit jours commandée par Mme LAFERRADE après l'incident du 5 mars 2027, conduite par un cabinet indépendant du club et de ses prestataires. Périmètre : les systèmes utilisés les jours de match (contrôle d'accès, paiement des buvettes, écran géant et sonorisation, réseaux du stade, communication avec les intervenants) et leur organisation. Méthode : entretiens avec le responsable du stade et de la sécurité, le responsable informatique, la communauté d'agglomération, PORTALVÈNE Accès, SOLDÉRIS Paiement et GARDALEINE Sécurité ; revue de la convention de mise à disposition du stade et des contrats ; observation du match du samedi 3 avril 2027. Référentiels utilisés : ISO/IEC 27001:2022 (mesures de sécurité) et bonnes pratiques de continuité d'activité. Aucun essai technique n'a été réalisé.

**Constats (dans l'ordre de leur relevé, sans hiérarchie)**
1. Les 30 superviseurs se connectent au logiciel de contrôle d'accès avec deux comptes partagés, « superviseur » et « administrateur », dont les mots de passe n'ont pas changé depuis la mise en service et sont notés sur une feuille affichée dans le local technique.
2. Il n'existe aucune procédure écrite pour faire entrer le public en cas de panne du contrôle d'accès ; la liste des billets valides n'est disponible que sur le serveur du local technique.
3. Le contrat de PORTALVÈNE Accès ne comporte aucun engagement de délai de rétablissement ni de pénalité ; son astreinte n'est ouverte qu'en semaine, de 9 h à 18 h, alors qu'aucun match ne se joue pendant ces heures.
4. PORTALVÈNE Accès installe ses mises à jour à distance quand il le décide, y compris le jour d'un match, sans prévenir le club ; son accès à distance est ouvert en permanence.
5. Dans la tribune Est, les terminaux de paiement des six buvettes sont raccordés au réseau du public, installation provisoire de septembre 2026 qui n'a jamais été reprise.
6. Le poste de supervision du contrôle d'accès est relié à la fois au réseau administratif du club et au réseau des systèmes du stade.
7. Aucun exercice de crise n'a été organisé depuis la modernisation ; les membres de la cellule de crise d'un jour de match ne sont pas désignés et aucun moyen de communication de secours n'est prévu.
8. La convention de mise à disposition du stade, signée en 2024, ne mentionne ni l'écran géant, ni l'éclairage pilotable, ni les réseaux installés en 2026 : personne ne sait qui décide d'une intervention sur ces systèmes, qui la paie, ni qui est joignable un soir de match.
9. Le groupe de messagerie instantanée qui sert à diffuser les consignes aux intervenants compte 520 membres, dont 120 anciens intervenants qui ne travaillent plus pour les prestataires.
10. Les billets des partenaires et des loges sont envoyés en fichiers par courriel, sans le nom du porteur ; le logiciel de contrôle d'accès ne signale pas un même billet présenté plusieurs fois.
11. Il n'existe aucun inventaire des systèmes du stade précisant leur propriétaire, leur exploitant et leur importance pour le jour de match ; le responsable informatique n'a jamais été associé ni à l'écran géant, ni aux réseaux du stade.

### ANNEXE 3.4 – Le stade connecté et son empreinte (juin 2027)

**A. Équipements numériques du stade**

| Équipement | Avant la modernisation (saison 2024-2025) | Après la modernisation (saison 2026-2027) | Utilisation |
|---|---|---|---|
| Écran géant | un écran de 40 m², installé en 2010 | deux écrans de 60 m² chacun, installés en 2026, durée de vie annoncée de dix ans | allumés pendant les 15 matchs et les 40 autres événements accueillis chaque année (concerts, séminaires), et pour les visites des partenaires |
| Éclairage du terrain | projecteurs à halogénures | projecteurs à diodes électroluminescentes, pilotables (allumage partiel, spectacles lumineux d'avant-match) | matchs, entraînements du soir, événements |
| Réseau sans fil du public | aucun | 120 bornes | allumées en permanence, toute l'année |
| Écrans des loges et des salons | 60 écrans installés en 2021 | 200 écrans neufs installés en 2026 ; les 60 écrans de 2021, âgés de cinq ans, ont été jetés | allumés en permanence, la mise en veille n'ayant pas été programmée |
| Contrôle d'accès et paiement | contrôle visuel des billets papier ; paiement en espèces et par carte | 80 lecteurs, remplacés à chaque renouvellement du contrat de PORTALVÈNE Accès, soit tous les trois ans ; 60 terminaux de paiement | jours de match |

Le club ne tient aucun inventaire de ces équipements (voir l'annexe 3.3, constat 11).

**B. Consommation d'électricité du stade (en MWh par an, relevés des sous-compteurs de la communauté d'agglomération ; l'électricité est refacturée au club selon un forfait annuel)**

| Usage | 2024-2025 | 2026-2027 | Évolution |
|---|---|---|---|
| Éclairage du terrain | 300 | 120 | − 60 % |
| Écrans (écran géant, loges et salons) | 15 | 80 | |
| Réseaux et systèmes du stade (bornes, contrôle d'accès, paiement, régie) | 5 | 40 | |
| **Total** | **320** | **240** | **− 25 %** |

La consommation des écrans, des réseaux et des systèmes, qui ne représentait qu'environ 6 % de l'ensemble, a été multipliée par six et en représente désormais la moitié.

Selon une estimation d'un bureau d'études mandaté par la communauté d'agglomération (valeurs fictives), les équipements numériques du stade (écrans, bornes, lecteurs, terminaux, régie) émettent environ 40 tonnes d'équivalent CO2 par an, dont 75 % au titre de leur fabrication, répartie sur leur durée de vie prévue, et 25 % au titre de leur consommation d'électricité. Les contenus numériques du club n'ont jamais été mesurés.

**C. Contenus numériques du club**
- **Application mobile** : 40 000 utilisateurs actifs ; elle pèse 180 Mo et lance automatiquement une vidéo à son ouverture ; la page d'accueil du site internet du club obtient la note F à l'EcoIndex.
- **Vidéos** : 400 vidéos publiées par saison, toutes en très haute définition et en lecture automatique, conservées sans limite depuis 2015 (40 To stockés sur une plateforme de vidéos) ; 70 % ne sont plus regardées un mois après leur publication.
- **Diffusions en direct** : 60 par saison (avant-matchs, conférences de presse, matchs des équipes de l'association), en très haute définition, suivies en moyenne par 300 personnes.

**D. La demande d'ÉNERVALDE (courriel de Mme Hélène MARTISSAC, directrice des achats du groupe ÉNERVALDE, partenaire principal du club, 900 000 € par saison, 12 mai 2027)**

« Notre groupe établit un état de durabilité conforme aux normes européennes d'information en matière de durabilité. Nous interrogeons nos 300 principaux fournisseurs et partenaires sur leur empreinte : je vous adresse un questionnaire de 140 questions, à retourner avant le 30 septembre 2027, sur vos consommations d'énergie, vos émissions de gaz à effet de serre et votre politique de numérique responsable, en particulier pour l'écran géant et les vidéos qui portent notre marque. La durabilité sera un critère du renouvellement de notre partenariat en 2028. »

M. Cédric BARRALOU, directeur commercial et des partenariats : « Nous ne savons même pas ce que consomme le stade, c'est l'agglomération qui paie l'électricité. Et si nous répondons à 140 questions pour ÉNERVALDE, les autres grands partenaires nous enverront chacun leur propre questionnaire. »

**E. Repères au 31/12/2026**

| Texte ou source | Repères utiles | Situation au 31/12/2026 |
|---|---|---|
| Directive (UE) 2022/2464 (CSRD), modifiée par la directive (UE) 2026/470 « Omnibus I » | l'obligation de publier un état de durabilité est réservée aux entreprises de plus de 1 000 salariés et de plus de 450 M€ de chiffre d'affaires ; ÉNERVALDE entre dans le champ de la directive ; **MONTALBRET XV n'y entre pas** (données de l'énoncé, à ne pas discuter) | directive Omnibus I en vigueur depuis le 18/03/2026 ; non transposée en France |
| Règlement délégué (UE) 2026/1560, norme volontaire d'information en matière de durabilité pour les PME (VSME) | norme que les entreprises non soumises à l'obligation peuvent appliquer volontairement, en deux modules (module de base, module complet) ; une entreprise soumise ne peut exiger d'une entreprise de sa chaîne de valeur qui ne compte pas plus de 1 000 salariés d'autres informations que celles de la liste fixée par ce règlement pour la chaîne de valeur, pour les exercices commençant à compter du 01/01/2027 | en vigueur |
| Loi n° 2021-1485 du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique en France (REEN) | sensibilisation au numérique responsable ; limitation du renouvellement des terminaux ; écoconception des services numériques ; centres de données et réseaux moins énergivores ; stratégie numérique responsable des communes et intercommunalités de plus de 50 000 habitants ; la communauté d'agglomération de Montalbret a adopté la sienne en 2025 | en vigueur |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | critères d'écoconception des services numériques (stratégie, contenus, interface, hébergement…), publiés par l'Arcep et l'Arcom avec l'ADEME | en vigueur |
| Étude ADEME-Arcep sur l'empreinte environnementale du numérique en France (volet du 19/01/2022 ; mise à jour du 17/01/2025, données 2022) | le numérique représente environ 4 % de l'empreinte carbone de la France en 2022 ; selon le volet de 2022, les terminaux concentraient 65 à 92 % de l'empreinte environnementale du numérique selon l'indicateur considéré, principalement du fait de leur fabrication | publiée |

### Travail à faire

L'incident du 5 mars 2027 a montré que le jour de match repose désormais sur des systèmes numériques partagés entre le club, la communauté d'agglomération et plusieurs prestataires, sans que personne en maîtrise l'ensemble. Mme LAFERRADE veut aborder la saison 2027-2028, dont le premier match à domicile est prévu en septembre 2027, avec des risques identifiés et traités, une organisation claire de la sécurité et de la résilience, et une réponse argumentée au partenaire principal du club sur l'empreinte du stade connecté. Vous mobiliserez pour cela les annexes 1.1, 3.1, 3.2, 3.3 et 3.4 ainsi que vos connaissances professionnelles.

**3.1 – Risques des jours de match (3 points)**

a) Après avoir présenté les trois catégories de risques liés aux systèmes d'information (cybermenaces, défaillances opérationnelles, risques réglementaires et métiers), identifiez, à partir des annexes 3.1 et 3.2, six risques d'un jour de match, deux par catégorie.

b) Après avoir défini l'analyse d'impact sur l'activité, analysez l'impact de l'incident A sur les processus du jour de match, sur la continuité du service aux spectateurs et sur les états financiers du club (postes exposés, sans évaluation chiffrée).

c) Retenez trois risques prioritaires, en justifiant votre choix par leur probabilité et leur impact, puis proposez pour chacun une option de traitement et une mesure, en indiquant le référentiel ou la méthode sur lequel vous vous appuieriez.

**3.2 – Gouvernance et résilience des systèmes du stade (2,5 points)**

a) Après avoir précisé ce qu'est un système critique, répartissez les rôles et les responsabilités de la sécurité des systèmes du stade entre la direction générale du club, le responsable du stade et de la sécurité, l'informatique du club, la communauté d'agglomération et les prestataires, puis indiquez le document et l'instance qui les formaliseraient.

b) Présentez trois principes de séparation entre le réseau du public, le réseau des systèmes du stade et le réseau administratif du club, sans entrer dans le détail technique, en les reliant aux constats des annexes 3.1 et 3.3.

c) Proposez l'organisation de la résilience des jours de match : contenu de la procédure dégradée d'entrée du public et d'un exercice de crise (scénario, participants, fréquence), en situant ces deux dispositifs par rapport au plan de continuité d'activité.

**3.3 – Diagnostic d'audit (2,5 points)**

a) À partir des constats de l'annexe 3.3, rédigez, à l'attention de Mme LAFERRADE, une note de synthèse de 20 lignes au maximum présentant le diagnostic d'audit : constats regroupés et hiérarchisés, risques associés, recommandations priorisées et datées.

b) Précisez en quelques lignes ce qui distingue cette mission d'audit d'un simple contrôle, puis les suites à lui donner.

**3.4 – Empreinte du stade connecté et demande du partenaire (5 points)**

a) Après avoir distingué le Green IT et la sobriété numérique, analysez l'empreinte environnementale du stade connecté et des contenus numériques du club sous trois angles (fabrication des équipements, usage, durée de vie), à partir de l'annexe 3.4, puis présentez deux outils ou indicateurs de mesure adaptés au cas, en précisant la limite de chacun.

b) Proposez quatre mesures de numérique responsable, priorisées et portant sur quatre domaines distincts : contenus et application ; durée de vie des équipements ; pilotage des écrans, de l'éclairage et du réseau sans fil ; mutualisation. Pour chacune, précisez le principe, l'effet attendu au regard de l'annexe 3.4 et son porteur.

c) Expliquez pourquoi ÉNERVALDE interroge le club, puis ce que le club peut lui fournir en s'appuyant sur la norme volontaire pour les PME, et le rôle du système d'information dans la fiabilité de ces données.

d) Proposez deux indicateurs de suivi de la démarche de numérique responsable du stade, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
