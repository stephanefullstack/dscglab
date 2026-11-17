# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 30

**DOSSIER 3 – CAPITALISER LES RETOURS D'EXPÉRIENCE, SÉCURISER LES ACCÈS DES PARTENAIRES ET RENDRE LE NUMÉRIQUE PLUS RESPONSABLE (13 points)**

Durée conseillée : 58 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 10, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en avril 2027. SOLVÉRANCE Habitat est une société par actions simplifiée créée en 2018 à Vénissieux, dans la métropole de Lyon, par M. Mathieu ROUSSERGUES, qui la préside. L'entreprise rénove des logements pour les rendre moins consommateurs d'énergie : isolation des murs et des combles, remplacement des menuiseries, ventilation et chauffage. Ses clients sont des particuliers, propriétaires de maisons individuelles ou de logements en petite copropriété, qu'elle accompagne de la visite technique à la réception des travaux, y compris dans leurs demandes d'aides publiques. SOLVÉRANCE Habitat emploie 95 salariés (compagnons et chefs d'équipe, conducteurs de travaux, conseillers en rénovation, techniciens du bureau d'études, services administratifs) et confie une partie des travaux à une quarantaine d'entreprises partenaires. Son chiffre d'affaires a atteint 25 millions d'euros en 2026, contre 9 millions d'euros en 2022. En 2025, un fonds d'investissement régional est entré au capital à hauteur de 35 %. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « Cap 2029 », arrêté par M. ROUSSERGUES avec le fonds en janvier 2027, fixe trois priorités : doubler le chiffre d'affaires en ouvrant deux agences, à Grenoble et à Saint-Étienne, et en développant les rénovations globales ; maîtriser la marge de chaque chantier et la qualité des travaux ; structurer l'entreprise, notamment son système d'information, pour qu'elle grandisse sans perdre ses savoir-faire ni la confiance de ses clients. Le fonds suit ces priorités à chaque comité stratégique trimestriel.

Vous êtes directeur administratif et financier de SOLVÉRANCE Habitat depuis 2026, rattaché au président. L'entreprise n'ayant pas de direction des systèmes d'information, vous êtes aussi chargé du système d'information. M. ROUSSERGUES vous demande trois travaux : structurer la gouvernance et le pilotage du système d'information (dossier 1) ; organiser et exploiter les données des chantiers et des logements (dossier 2) ; capitaliser les retours d'expérience, sécuriser les accès des partenaires et rendre le numérique plus responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de SOLVÉRANCE Habitat et chiffres clés

SOLVÉRANCE Habitat est une société par actions simplifiée créée en 2018 par M. Mathieu ROUSSERGUES, son président, qui détient 65 % du capital. Le fonds d'investissement régional TALVÉRIS Croissance en détient 35 % depuis 2025. Le siège et le dépôt de matériaux sont à Vénissieux (métropole de Lyon). L'entreprise intervient dans la métropole de Lyon, dans l'Ain et dans le nord de l'Isère. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires | 25 M€ (9 M€ en 2022) |
| Chantiers achevés | environ 1 000, d'un montant moyen de l'ordre de 25 k€ |
| Rénovations globales (plusieurs postes de travaux traités ensemble : isolation, menuiseries, ventilation, chauffage) | environ 125 chantiers, de l'ordre de 60 k€ chacun : 7,5 M€, soit 30 % du chiffre d'affaires |
| Travaux par lots (un ou deux postes de travaux) | environ 875 chantiers, de l'ordre de 20 k€ chacun : 17,5 M€, soit 70 % du chiffre d'affaires |
| Entreprises partenaires | environ 40 entreprises (plomberie et chauffage, électricité, couverture), qui réalisent environ 35 % des travaux |
| Effectif | 95 salariés : environ 50 compagnons et chefs d'équipe, 10 conducteurs de travaux, 12 conseillers en rénovation, 8 techniciens du bureau d'études, 15 personnes aux services administratifs et à la direction |
| Dépenses du système d'information | environ 450 k€ (1,8 % du chiffre d'affaires) |
| Plan « Cap 2029 » (janvier 2027) | doubler le chiffre d'affaires (agences de Grenoble et de Saint-Étienne, développement des rénovations globales) ; maîtriser la marge de chaque chantier et la qualité des travaux ; structurer l'entreprise et son système d'information pour grandir sans perdre les savoir-faire ni la confiance des clients |

**Le système d'information en quelques lignes**

Le système d'information s'est constitué au fil de la croissance, par la souscription de services en ligne : un logiciel de gestion de la relation client, un logiciel de devis et de facturation spécialisé dans le bâtiment, une application de visite technique sur tablette (formulaires, photos), un logiciel de calcul thermique utilisé par le bureau d'études, un progiciel de comptabilité et de paie, une messagerie et une suite bureautique en ligne. Le planning des équipes et le suivi des dossiers d'aides sont tenus sur des tableurs partagés. Le parc compte environ 60 tablettes et smartphones de chantier et 40 ordinateurs ; son support est assuré par un prestataire informatique local. L'entreprise n'a pas de direction des systèmes d'information : son seul informaticien est le responsable informatique.

**Organigramme simplifié (avril 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Direction | président fondateur | M. Mathieu ROUSSERGUES |
| Comité stratégique (trimestriel) | le président, M. Arnaud VORGNAC, directeur de participations de TALVÉRIS Croissance, et le directeur administratif et financier | — |
| Rattachée au président | directrice des opérations : 10 conducteurs de travaux, environ 50 compagnons et chefs d'équipe, coordination des entreprises partenaires, 3 assistantes d'exploitation (planning des équipes, achats de matériaux) | Mme Nadège CHAMBAROUX |
| Rattachée au président | responsable du bureau d'études (8 techniciens, dont elle-même : visites techniques des rénovations globales, calculs thermiques) | Mme Léa FONTRIVAL |
| Rattachée au président | responsable commerciale (pôle commercial : 12 conseillers en rénovation, dont elle-même, qui conduisent les visites techniques et établissent les devis) | Mme Sophie MARQUENDE |
| Rattaché au président | directeur administratif et financier : comptabilité et paie (4 personnes), dossiers d'aides des clients (3 chargées), accueil (1 personne), responsable informatique | vous |
| Rattaché au directeur administratif et financier | responsable informatique, seul informaticien de l'entreprise | M. Romain TRÉVASSOU |

Les 15 personnes des services administratifs et de la direction sont le président, la directrice des opérations, le directeur administratif et financier, les 3 assistantes d'exploitation, les 4 personnes de la comptabilité et de la paie, les 3 chargées des dossiers d'aides, la personne de l'accueil et le responsable informatique. Les responsables du bureau d'études et du pôle commercial sont comptées dans leurs équipes.

### ANNEXE 3.1 – Les retours d'expérience des chantiers (note de Mme Nadège CHAMBAROUX, directrice des opérations, et témoignages recueillis en mars 2027)

**A. Les réserves à la réception des chantiers achevés en 2026**

Sur les environ 1 000 chantiers achevés en 2026, 300 (30 %) ont fait l'objet d'au moins une réserve du client à la réception, pour un total de 400 réserves. Leur reprise (retour d'une équipe ou d'un partenaire, matériaux, déplacements) a coûté environ 400 k€, soit 1,6 % du chiffre d'affaires ; il a fallu en moyenne 45 jours pour lever une réserve. Les réserves sont notées sur le procès-verbal de réception, numérisé par le conducteur de travaux ; aucune liste de leurs causes n'est tenue. Le relevé ci-dessous a été établi à la main, en février 2027, par une assistante d'exploitation.

| Défaut à l'origine de la réserve | Réserves | Coût des reprises (k€) |
|---|---|---|
| Étanchéité à l'air mal traitée autour des menuiseries remplacées | 80 | 100 |
| Pare-vapeur discontinu dans les combles isolés | 60 | 80 |
| Entrées d'air de ventilation absentes ou mal placées après le remplacement des menuiseries | 40 | 40 |
| Réglage des pompes à chaleur à la mise en service (lots des entreprises partenaires) | 40 | 40 |
| Finitions de l'isolation des murs par l'extérieur (angles, appuis de fenêtres) | 20 | 20 |
| **Sous-total : cinq défauts récurrents** | **240** | **280** |
| Autres défauts, peu répétés | 160 | 120 |
| **Total** | **400** | **400** |

| Qui a réalisé l'ouvrage en cause | Chantiers concernés en 2026 | Réserves | Réserves pour 100 chantiers |
|---|---|---|---|
| Les 4 équipes dirigées par un chef d'équipe de plus de dix ans de métier | 300 | 30 | 10 |
| Les 8 autres équipes, dont 5 créées depuis 2024 | 550 | 220 | 40 |
| Les entreprises partenaires (lots de plomberie et de chauffage, d'électricité, de couverture) | 500 | 150 | 30 |

Un même chantier peut associer une équipe de l'entreprise et une ou plusieurs entreprises partenaires. Les 12 équipes réunissent les 50 compagnons et chefs d'équipe.

**B. Les savoir-faire et leur support**

- Les quatre chefs d'équipe les plus anciens savent éviter la plupart des défauts du tableau : « ce sont des tours de main », résume l'un d'eux. Deux d'entre eux partiront encadrer les nouvelles équipes de Grenoble (trois équipes à l'ouverture, en septembre 2027) et de Saint-Étienne (trois équipes en 2028) ; il faudra recruter environ quinze compagnons et travailler avec une dizaine de nouvelles entreprises partenaires.
- Trois classeurs rangés au dépôt de Vénissieux contiennent environ 60 fiches de pose, dont la moitié date d'avant 2022 ; certaines ne correspondent plus aux produits posés.
- Les chefs d'équipe photographient les bonnes et les mauvaises pratiques avec les smartphones de chantier ; les photos restent dans les appareils ou partent dans le groupe de messagerie instantanée « Astuces chantier » (35 membres, salariés et quelques artisans partenaires, environ 2 000 messages en 2026), où rien ne se retrouve.
- Les réserves sont évoquées oralement à la réunion mensuelle des conducteurs de travaux, sans compte rendu. Le bureau d'études n'en est pas informé.

**C. Témoignages**

- **M. Patrice GOURDANNE, chef d'équipe depuis 2018** : « Ce que je sais, je l'ai appris en me trompant. Je veux bien montrer aux jeunes, mais je ne suis pas un écrivain, et je n'ai pas envie de passer mes soirées à rédiger des fiches. »
- **Un compagnon recruté en 2025** : « Sur le chantier, on n'a pas le temps de lire : le client attend et le camion repart à 17 h. Et puis, on apprend en faisant, pas dans un classeur. »
- **Un conducteur de travaux** : « Les mêmes réserves reviennent. On en parle à la réunion du mois, puis tout le monde oublie. »
- **Le gérant d'une entreprise partenaire de plomberie et de chauffage** : « Je travaille pour quatre entreprises. Vos consignes m'intéressent si elles sont courtes ; mais je ne veux pas qu'on me montre du doigt à chaque réserve. »
- **Mme Léa FONTRIVAL, responsable du bureau d'études** : « Une partie des réserves de ventilation vient de nos préconisations, pas de la pose. Si personne ne nous le dit, nous referons les mêmes. »

### ANNEXE 3.2 – Les accès des entreprises partenaires et l'incident de février 2027 (note de M. Romain TRÉVASSOU, responsable informatique, mars 2027)

**A. Comment les partenaires accèdent à nos outils**

- Environ 25 des 40 entreprises partenaires consultent chaque soir le tableur partagé du planning pour connaître leurs chantiers du lendemain, et déposent leurs photos dans les dossiers partagés des chantiers, rangés par conducteur de travaux dans l'espace de stockage de la suite bureautique en ligne.
- Pour ne pas payer de licences, ils se connectent avec trois comptes génériques (« partenaires-plomberie », « partenaires-électricité », « partenaires-couverture »), créés en 2022. Les mots de passe n'ont jamais été changés ; les conducteurs de travaux les transmettent par SMS à chaque nouveau partenaire ; environ 60 personnes les connaissent, chez les partenaires.
- Chaque compte générique voit l'ensemble du planning et des dossiers partagés : nom, adresse et téléphone des clients, codes d'accès (digicodes, codes des boîtes à clés laissées par les clients absents) et dates d'absence des clients, pour environ 400 chantiers planifiés.
- Aucune entreprise partenaire n'a signé d'engagement de confidentialité. Personne ne tient la liste des partenaires qui ont accès, ni celle des salariés des partenaires qui connaissent les mots de passe.

**B. Les tablettes et les smartphones de chantier**

- Les 60 appareils de chantier ne sont pas verrouillés : « avec des gants, un code à chaque fois, c'est impossible », disent les équipes. La messagerie, le planning et les dossiers partagés y restent ouverts en permanence.
- Il n'existe ni inventaire des appareils et de leurs utilisateurs, ni moyen de les localiser ou de les effacer à distance. Les mises à jour du système des appareils dépendent de la bonne volonté de chacun.
- L'abonnement à la suite bureautique en ligne comprend l'authentification à deux facteurs et un service de gestion des appareils mobiles ; ni l'un ni l'autre n'ont été activés.

**C. L'incident de février 2027**

- Le 9 février 2027, un client de l'est lyonnais nous a appelés : un électricien lui proposait directement des travaux, en citant la date de son prochain déplacement et le code de sa boîte à clés. Il s'agissait du gérant de VERCLAUZE Électricité, entreprise avec laquelle nous avons cessé de travailler en octobre 2026, après plusieurs malfaçons.
- Le journal des connexions de la suite bureautique, conservé six mois, montre que le compte « partenaires-électricité » a été utilisé une trentaine de fois depuis le réseau de VERCLAUZE Électricité entre novembre 2026 et février 2027.
- Le 20 février 2027, la tablette d'un conducteur de travaux a été oubliée sur un chantier de l'est lyonnais ; elle n'a pas été retrouvée. Elle n'était pas verrouillée et donnait accès à sa messagerie, au planning et aux dossiers partagés.
- J'ai changé les mots de passe des trois comptes génériques et de ceux du conducteur de travaux, puis prévenu les 25 partenaires actifs. Sur le conseil d'un avocat, l'entreprise a notifié la violation de données à l'autorité de contrôle et informé les quelque 150 clients dont les codes d'accès figuraient dans le planning ; 40 boîtes à clés ont été remplacées à nos frais, pour environ 6 k€. L'incident a mobilisé une quinzaine de jours de travail.

**D. Qui est responsable de quoi ?**

| Acteur | Position constatée |
|---|---|
| Fournisseur de la messagerie et de la suite bureautique en ligne | ses conditions générales indiquent qu'il assure la sécurité de son service et de ses centres de données, et que « la gestion des comptes, des droits et des appareils relève du client » |
| Éditeur de l'application de visite technique | crée les comptes que je lui demande ; ne sait pas qui les utilise |
| BRIVALDE Informatique, prestataire local qui assure le support du parc | prépare les appareils neufs et les répare ; estime que « les comptes et les accès, c'est l'affaire des éditeurs » |
| Conducteurs de travaux | invitent les partenaires et leur transmettent les mots de passe ; pensent que « la sécurité, c'est l'informatique » |
| Entreprises partenaires | leurs salariés changent souvent ; aucune n'a désigné d'interlocuteur pour ces accès |
| Responsable informatique | seul informaticien de l'entreprise ; aucune règle écrite ne fixe ses responsabilités en matière de sécurité |

**E. Témoignages**

- **Mme Nadège CHAMBAROUX, directrice des opérations** : « Les partenaires doivent voir le planning le soir pour le lendemain. Si l'accès devient compliqué, ils m'appelleront tous à 7 h du matin. »
- **Le gérant d'une entreprise partenaire de couverture** : « J'ai trois salariés, qui changent souvent. Je ne vais pas gérer vos comptes à votre place. »
- **M. Mathieu ROUSSERGUES, président** : « Nos clients nous confient les clés de leur maison. Je ne veux plus jamais vivre une histoire pareille, mais je ne veux pas non plus d'une usine à gaz. »

### ANNEXE 3.3 – Le numérique de SOLVÉRANCE Habitat et l'environnement (notes de M. Romain TRÉVASSOU et de Mme Léa FONTRIVAL, mars 2027)

**A. Le parc des appareils de chantier**

- Les 60 appareils de chantier se répartissent ainsi : une tablette pour chacun des 12 conseillers en rénovation, des 8 techniciens du bureau d'études et des 10 conducteurs de travaux (30 tablettes) ; un smartphone pour chacun des 12 chefs d'équipe et des 10 conducteurs de travaux (22 smartphones) ; 8 appareils de réserve au dépôt de Vénissieux. Les techniciens du bureau d'études n'utilisent leur tablette qu'une à deux journées par semaine, pour les visites des rénovations globales.
- Depuis 2022, la règle fixée par le président est de renouveler chaque appareil tous les deux ans, par un modèle neuf haut de gamme. En 2026, 50 appareils ont été achetés neufs, pour environ 35 k€ : 30 au titre du renouvellement, 15 pour remplacer des appareils cassés (écrans, chutes) et 5 pour remplacer des appareils perdus.
- Les appareils sont protégés par des coques ordinaires. Selon BRIVALDE Informatique, deux casses sur trois auraient été évitées par une coque renforcée et un verre de protection, pour environ 60 € par appareil.
- Le fabricant des appareils actuels assure leurs mises à jour de sécurité pendant au moins cinq ans après leur sortie. Un reconditionneur de la région propose des tablettes et des smartphones reconditionnés, garantis deux ans, pour environ 60 % du prix du neuf ; il rachète les appareils retirés et remet une attestation de réemploi ou de recyclage.
- Les quelque 80 appareils retirés depuis 2023 sont stockés dans une armoire du dépôt ; aucun n'a été revendu, donné ni recyclé.

**B. Les photos et les vidéos des chantiers**

- Les équipes prennent en moyenne 200 photos et 5 vidéos par chantier (avant, pendant et après les travaux). Chaque photo est envoyée dans le groupe de messagerie instantanée, copiée dans le dossier partagé du chantier et sauvegardée automatiquement par l'appareil : elle existe en moyenne en trois exemplaires.
- L'espace de stockage de la suite bureautique contient 8 To de photos et de vidéos de chantiers, dont 3 To de vidéos ; il augmente d'environ 3 To par an. Rien n'est jamais supprimé. Au-delà des 10 To compris dans l'abonnement, chaque téraoctet supplémentaire est facturé.

**C. Les économies d'énergie affichées**

- La brochure commerciale et le site internet annoncent : « Avec SOLVÉRANCE Habitat, jusqu'à 60 % d'économies d'énergie garanties ».
- Mme FONTRIVAL a examiné 30 devis remis en 2026 qui affichent une économie d'énergie. Pour les 10 rénovations globales, l'économie vient du calcul thermique du bureau d'études (de 35 % à 60 % selon les logements). Pour les 20 devis de travaux par lots, le conseiller l'a indiquée lui-même : à partir d'un tableau de pourcentages tiré de la documentation d'un fabricant (12 devis) ou « d'expérience » (8 devis). Pour le remplacement des menuiseries de maisons comparables, les économies annoncées vont de 10 % à 30 % selon le conseiller. Aucun devis ne précise les hypothèses retenues (température de chauffage, occupation du logement, consommation de départ).
- Ces chiffres ne sont conservés nulle part ailleurs que dans les devis en PDF. Aucune consommation n'est relevée après les travaux.
- En 2026, 6 clients ont contesté les économies obtenues ; l'un a publié sur internet un avis intitulé « Économies garanties ? Ma facture n'a pas bougé ».
- Mme FONTRIVAL : « Une économie calculée n'est pas une économie constatée : elle dépend du logement, du climat et de la façon dont les occupants se chauffent. »

**D. Les projets du président et de la responsable commerciale**

- **M. Mathieu ROUSSERGUES, président** : « Les grandes entreprises publient un rapport de durabilité ; nous devrions faire de même, selon les mêmes normes, et le présenter au comité stratégique et à la banque qui finance l'ouverture des agences. Nos chantiers font économiser de l'énergie à nos clients : c'est notre meilleure carte de visite. Je veux afficher l'énergie économisée par nos clients depuis 2018. »
- **Mme Sophie MARQUENDE, responsable commerciale** : « Demandons à tous nos clients leurs factures d'énergie pendant deux ans après les travaux, et publions sur le site internet les meilleurs résultats, avec la photo de la maison et sa commune. Ces factures nous serviront aussi à leur proposer d'autres travaux. »
- Personne, dans l'entreprise, n'est chargé des questions environnementales ; le numérique n'a jamais été examiné sous cet angle.

### ANNEXE 3.4 – Repères sur la sécurité, la durabilité et le numérique responsable (au 31/12/2026)

| Texte ou référentiel | Repères utiles | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Données collectées pour des finalités déterminées et limitées à ce qui est nécessaire ; sécurité adaptée au risque ; recours à un sous-traitant (par exemple l'éditeur d'un service en ligne) encadré par un contrat ; notification à l'autorité de contrôle d'une violation de données dans les 72 heures et, en cas de risque élevé, information des personnes concernées. | Applicable depuis le 25/05/2018 |
| Guide d'hygiène informatique de l'ANSSI (2017) | 42 mesures de bonnes pratiques, dont l'identification nominative de chaque personne qui accède au système d'information, l'encadrement des arrivées et des départs des utilisateurs, des règles de choix des mots de passe et la sécurisation des terminaux mobiles (smartphones et tablettes). | En vigueur |
| ISO/IEC 27001:2022 | Norme internationale qui spécifie les exigences d'un système de management de la sécurité de l'information, fondé sur l'appréciation et le traitement des risques ; son annexe A énumère 93 mesures de sécurité, dont la gestion des identités et des droits d'accès, la sécurité dans les relations avec les fournisseurs et la protection des terminaux des utilisateurs. | En vigueur |
| ISO/IEC 27002:2022 | Guide de mise en œuvre des mesures de sécurité de l'information (mesures organisationnelles, liées aux personnes, physiques et technologiques). | En vigueur |
| Directive (UE) 2022/2464 dite CSRD, modifiée par la directive (UE) 2026/470 dite « Omnibus I » | Publication d'informations en matière de durabilité, établies selon les normes ESRS et vérifiées par un tiers ; la directive Omnibus I réserve l'obligation aux entreprises de très grande taille. | En vigueur ; directive Omnibus I non transposée en France |
| Normes ESRS révisées (règlement délégué (UE) 2026/1563) | Normes européennes d'information en matière de durabilité : normes transversales (exigences générales, informations générales) et normes thématiques environnementales (dont le climat et l'utilisation des ressources), sociales et de gouvernance. | Applicables aux exercices ouverts à compter du 01/01/2027 |
| Loi n° 2021-1485 du 15 novembre 2021 visant à réduire l'empreinte environnementale du numérique en France (REEN) | Sensibilisation au numérique responsable, allongement de la durée de vie des équipements, écoconception des services numériques, centres de données et réseaux moins énergivores. | En vigueur |
| Référentiel général d'écoconception de services numériques (RGESN), version 2024 | Critères d'écoconception des services numériques (stratégie, contenus, hébergement, etc.). | En vigueur |
| Étude de l'ADEME et de l'Arcep sur l'empreinte environnementale du numérique en France | Les terminaux représentent de 65 % à 92 % de l'empreinte environnementale du numérique selon l'indicateur considéré, principalement du fait de leur fabrication. | Volets de 2022 et de 2023 ; mise à jour du 17/01/2025 |

SOLVÉRANCE Habitat n'entre pas dans le champ de la directive CSRD : c'est une donnée de l'énoncé, qui n'est pas à discuter. Aucune analyse juridique n'est attendue.

### Travail à faire

Le plan « Cap 2029 » veut que SOLVÉRANCE Habitat grandisse sans perdre ses savoir-faire ni la confiance de ses clients. Or les mêmes défauts se répètent d'un chantier à l'autre, un ancien partenaire a pu consulter les codes d'accès et les dates d'absence de clients, et l'entreprise affiche des économies d'énergie qu'elle ne sait pas justifier. M. ROUSSERGUES vous demande de capitaliser les retours d'expérience des chantiers, de sécuriser les accès des entreprises partenaires et des appareils de chantier, et de rendre le numérique de l'entreprise plus responsable. Vous mobiliserez pour cela les annexes 1.1 et 3.1 à 3.4 ainsi que vos connaissances professionnelles.

**3.1 – La capitalisation des retours d'expérience des chantiers (3,5 points)**

a) Après avoir défini le retour d'expérience et distingué connaissances tacites et connaissances explicites, proposez, à partir de l'annexe 3.1, l'architecture fonctionnelle d'un dispositif de capitalisation des retours d'expérience des chantiers en cinq fonctions (capter, valider, stocker, diffuser, mettre à jour), en précisant pour chacune son contenu chez SOLVÉRANCE Habitat et son intégration dans les outils existants (appareils de chantier, espace de stockage partagé, messagerie, réunions). La cartographie des savoirs n'est pas attendue.

b) Précisez le pilotage et la gouvernance du dispositif (rôles et règles), ainsi qu'un indicateur de son efficacité, précisé par sa formule, sa source, sa fréquence, sa cible et son axe ; proposez ensuite trois leviers d'appropriation par les équipes et par les entreprises partenaires, chacun en réponse à une réserve exprimée dans l'annexe 3.1. La gestion des compétences n'est pas à traiter.

**3.2 – Les accès des entreprises partenaires et les appareils de chantier (5 points)**

a) Après avoir présenté les trois catégories de risques liés aux systèmes d'information (cybermenaces, défaillances opérationnelles, risques réglementaires et métiers), identifiez trois risques révélés par l'annexe 3.2, un par catégorie, en précisant pour chacun ses conséquences pour l'entreprise et pour ses clients.

b) Après avoir défini la gestion des identités et des accès, proposez-en trois règles pour les entreprises partenaires, portant respectivement sur les comptes et les droits, sur les arrivées et les départs, et sur la revue périodique des droits, en tenant compte des contraintes exprimées par la directrice des opérations et par les partenaires.

c) Après avoir précisé ce qu'est une architecture de confiance, proposez deux mesures pour les tablettes et les smartphones de chantier, chacune reliée à un constat de l'annexe 3.2 et assortie d'une condition de réussite sur le chantier. Aucun paramétrage n'est attendu.

d) Après avoir expliqué le principe de la responsabilité partagée entre une entreprise et les fournisseurs de ses services en ligne, répartissez les rôles et les responsabilités de la sécurité des accès entre SOLVÉRANCE Habitat (direction, responsable informatique, conducteurs de travaux), les éditeurs des services en ligne, le prestataire informatique local et les entreprises partenaires, puis indiquez comment cette répartition sera formalisée et suivie. Aucune analyse juridique n'est attendue.

**3.3 – Un numérique plus responsable et des économies d'énergie fiables (4,5 points)**

a) Après avoir distingué la sobriété numérique et le Green IT, proposez quatre mesures de numérique responsable, portant respectivement sur la durée de vie et le reconditionnement des appareils de chantier, leur protection contre la casse, la sobriété des photos et des vidéos, et la mutualisation des appareils. Justifiez chacune par l'annexe 3.3, puis classez-les par ordre de priorité en vous appuyant sur les repères de l'annexe 3.4. Aucun calcul d'empreinte n'est attendu.

b) Après avoir précisé ce qu'est une gouvernance du système d'information orientée vers la responsabilité sociétale, proposez-en deux principes pour SOLVÉRANCE Habitat, l'un sur l'éthique de l'usage des données des clients, en réponse à la proposition de la responsable commerciale, l'autre sur la sobriété, en précisant qui les porte.

c) Situez SOLVÉRANCE Habitat au regard de la CSRD et des ESRS d'après l'annexe 3.4 et répondez au président, puis montrez comment le système d'information peut fiabiliser les économies d'énergie affichées dans les devis, dans la brochure et dans les informations que l'entreprise publierait, afin d'éviter une communication trompeuse. Aucune règle du calcul thermique n'est attendue.

d) Proposez deux indicateurs de suivi, l'un pour le numérique responsable, l'autre pour la fiabilité des économies d'énergie affichées, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
