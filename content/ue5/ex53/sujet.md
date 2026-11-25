# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 53

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES INTERVENTIONS, EN MAÎTRISER LA CONSERVATION (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 2.1 – Les interventions, les engins et les équipages (note de M. Rémi TRÉVIGNAN, chef de l'observatoire de l'activité, avril 2027)

**A. Le fonctionnement actuel**

À chaque appel qui donne lieu à un départ de secours, l'opérateur du centre de traitement de l'alerte crée une intervention dans le logiciel de traitement de l'alerte : il en choisit la nature, localise le lieu et engage les engins que le logiciel lui propose. L'équipage de chaque engin est enregistré au départ du centre d'incendie et de secours. Pendant l'intervention, le chef d'agrès, qui commande l'engin, signale sur la tablette de l'engin son arrivée sur les lieux en appuyant sur un bouton ; les heures de départ et d'arrivée sont transmises au logiciel. Chaque mois, l'observatoire extrait les interventions du logiciel dans un tableur pour produire les chiffres de l'activité. En 2026, les 50 000 interventions ont donné lieu à 70 000 départs d'engins.

**B. Les problèmes de qualité relevés sur les données de 2026**

- **Heures d'arrivée manquantes** : sur 70 000 départs d'engins, 7 000, un sur dix, n'ont pas d'heure d'arrivée sur les lieux : le chef d'agrès a oublié d'appuyer sur le bouton de la tablette, souvent parce qu'il était occupé par la victime.
- **Natures « autre »** : l'opérateur peut choisir la nature « autre » quand la situation est confuse au moment de l'appel ; il l'a fait pour 2 500 interventions, une sur vingt. En janvier 2027, l'observatoire les a reclassées à la main, d'après les comptes rendus, dans l'une des quatre natures ; ce travail a pris 15 jours.
- **Équipages incomplets** : quand un sapeur-pompier remplace un autre au dernier moment, l'équipage enregistré au départ n'est pas corrigé ; le chef de centre le ressaisit ensuite dans un tableur. C'est arrivé pour 3 500 départs, un sur vingt.
- **Communes** : quand la localisation automatique échoue, l'opérateur saisit la commune en texte libre ; c'est le cas pour 4 000 interventions. La base compte ainsi 1 100 libellés différents (« Montcerneau », « MONTCERNEAU », « Mtcerneau », « Montcerneau Sud »…) pour les 480 communes du département.

**C. Les règles de gestion des interventions, des engins et des équipages**

- **RG1** – Une intervention est identifiée par un numéro attribué par le logiciel de traitement de l'alerte ; on connaît la date et l'heure de l'appel et l'adresse du lieu.
- **RG2** – Une intervention relève d'une seule nature. Une nature est identifiée par un code et porte un libellé (secours d'urgence aux personnes, accident de la circulation, incendie, opération diverse) ; une nature peut ne compter encore aucune intervention.
- **RG3** – Une intervention a lieu dans une seule commune. Une commune est identifiée par un code ; on connaît son nom et sa population. Une commune peut n'avoir connu aucune intervention.
- **RG4** – Une commune relève d'un seul centre de premier appel, qui envoie les premiers secours ; un centre est le centre de premier appel d'une ou de plusieurs communes. Un centre est identifié par un code ; on connaît son nom, son type (mixte ou volontaire) et son groupement territorial.
- **RG5** – Un engin est identifié par un numéro ; on connaît son type (ambulance de secours, fourgon d'incendie, camion-citerne, véhicule de secours routier…) et sa date de mise en service. Un engin appartient à un seul centre ; un centre possède un ou plusieurs engins.
- **RG6** – Une intervention mobilise un ou plusieurs engins ; un engin peut n'avoir encore été engagé sur aucune intervention. Pour chaque engin engagé sur une intervention, on connaît l'heure de départ et l'heure d'arrivée sur les lieux.
- **RG7** – Un agent est identifié par un matricule ; on connaît son nom, son prénom et son statut (professionnel, volontaire, ou professionnel et volontaire). Un agent est rattaché à un ou plusieurs centres ; un centre compte un ou plusieurs agents.
- **RG8** – Sur une intervention, un agent arme un engin dans un seul rôle : chef d'agrès, conducteur ou équipier. Sur une même intervention, un agent peut armer successivement plusieurs engins (par exemple lors d'une relève), dans un rôle pour chacun. Une intervention compte au moins un agent armant un engin ; un agent ou un engin peut n'avoir encore participé à aucune intervention.

### ANNEXE 2.2 – La sollicitation opérationnelle de 2022 à 2026 (tableaux de l'observatoire de l'activité, mars 2027)

**A. Interventions par nature et par an (chiffres publiés, en nombre d'interventions)**

| Nature | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Secours d'urgence aux personnes | 31 000 | 32 000 | 35 000 | 36 000 | 39 000 |
| Accidents de la circulation | 3 500 | 3 500 | 3 500 | 3 400 | 3 500 |
| Incendies | 3 500 | 3 000 | 3 000 | 3 100 | 3 500 |
| Opérations diverses | 5 000 | 5 500 | 3 500 | 3 500 | 4 000 |
| **Ensemble** | **43 000** | **44 000** | **45 000** | **46 000** | **50 000** |

**B. Quelques séries complémentaires**

| Série | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|
| Carences (comprises dans les secours d'urgence aux personnes) | 3 000 | 3 500 | 4 500 | 5 000 | 6 000 |
| Interventions pour des personnes de 80 ans et plus, à leur domicile (toutes natures) | 10 000 | 10 500 | 11 000 | 11 500 | 12 500 |
| Part des secours d'urgence aux personnes entre 18 heures et 8 heures | 40 % | 41 % | 42 % | 44 % | 45 % |
| Interventions par mois, en moyenne, en juillet et août | 4 200 | 4 300 | 4 400 | 4 500 | 5 000 |
| Interventions par mois, en moyenne, en janvier et février | 3 300 | 3 400 | 3 500 | 3 600 | 3 800 |

Conventions : une **carence** est une intervention de secours d'urgence aux personnes demandée par le centre de régulation médicale du SAMU, sans caractère d'urgence, parce qu'aucun autre moyen (ambulance privée, médecin de garde) n'était disponible. L'âge de la victime est celui noté sur le compte rendu de secours. Les séries se recoupent : une carence peut concerner une personne âgée à domicile.

**C. Ce que l'on sait de ces chiffres**

- **Reclassement de 2024** : au 1er janvier 2024, le SDIS a revu la liste des natures d'intervention. Les relevages de personnes tombées à leur domicile sans blessure apparente, environ 2 000 par an, sont passés des opérations diverses aux secours d'urgence aux personnes. Les chiffres de 2022 et de 2023 n'ont pas été recalculés.
- **Interface défaillante en 2025** : en mars et avril 2025, l'interface entre le logiciel de traitement de l'alerte et la base de l'observatoire a mal fonctionné ; environ 1 000 interventions de ces deux mois, surtout des secours d'urgence aux personnes, n'ont pas été transmises et manquent dans les chiffres de 2025.
- **Touristes** : le Haut-Aurande accueille jusqu'à 100 000 touristes en juillet et en août. Les chiffres rapportés aux habitants sont calculés sur la population résidente, 640 000 habitants.
- **Épisodes de chaleur** : en juillet 2026, deux épisodes de forte chaleur ont porté les interventions à 1 500 par semaine, contre 1 100 environ pour une semaine d'été ordinaire.

**D. L'affirmation de M. Thibaut PRUNEVAUX, administrateur, maire d'une commune du Haut-Aurande, au conseil d'administration du 30/03/2027**

« Si les interventions augmentent, c'est parce que la population vieillit. Il suffit de recruter des volontaires. »

### ANNEXE 2.3 – Les enregistrements des appels et les comptes rendus de secours (note de Mme Coralie FAVERJON, déléguée à la protection des données, et du Dr Agathe MÉRIGNOLLE, médecin-chef, avril 2027)

**A. Les enregistrements des appels**

Tous les appels reçus au centre de traitement de l'alerte, 150 000 en 2026, sont enregistrés par l'enregistreur des appels, installé en 2017 ; il en conserve environ 1,5 million, sans aucune suppression. Un enregistrement est retrouvé par la date, l'heure et le poste de l'opérateur : il n'est pas relié au numéro de l'intervention. Pour répondre à des demandes, des enregistrements sont copiés sur des clés USB ou envoyés par messagerie.

En septembre 2026, la justice a demandé l'enregistrement d'un appel de novembre 2024 relatif à un accident de la circulation. Après trois jours de recherche, le centre de traitement de l'alerte ne l'a pas retrouvé : l'horloge de l'enregistreur avait été décalée après une panne, et l'appel ne pouvait pas être rapproché de l'intervention.

**B. Les comptes rendus de secours**

Depuis la fin de 2021, le chef d'agrès rédige sur la tablette de l'engin un compte rendu de secours pour chaque victime : identité, état de la victime, gestes réalisés. Le compte rendu est envoyé au centre de régulation médicale du SAMU et à l'hôpital qui accueille la victime, puis stocké sur un serveur du siège. Le serveur en conserve plus de 200 000, à raison d'environ 40 000 par an ; il est occupé à 85 %. Aucun compte rendu n'a jamais été trié ni supprimé. Pour préparer les retours d'expérience ou répondre à des demandes, des chefs de centre et des médecins en exportent des copies en PDF dans leur messagerie : un contrôle de dix messageries, en mars 2027, en a trouvé 3 000.

Le Dr MÉRIGNOLLE rappelle que les comptes rendus contiennent des données de santé ; un compte rendu peut être demandé plusieurs années après l'intervention, notamment en cas de litige.

**C. Les demandes de copies en 2026**

| Demandeur | Nombre de demandes |
|---|---|
| Avocats | 150 |
| Assureurs | 150 |
| Familles des victimes | 80 |
| Justice | 20 |
| **Ensemble** | **400** |

Chaque demande est traitée par celui qui la reçoit (centre, centre de traitement de l'alerte, médecin-chef), sans registre ; le délai moyen de réponse est de deux mois.

**D. Les durées de conservation fixées par le SDIS**

Par une décision du 15/03/2027, prise après l'avis de la déléguée à la protection des données et du médecin-chef, le directeur départemental a fixé les durées suivantes, qui ne sont pas à discuter :
- **enregistrements des appels** : deux ans après l'appel, puis destruction, sauf si une demande portant sur l'intervention est en cours ;
- **comptes rendus de secours** : consultation courante pendant deux ans après l'intervention, puis archivage jusqu'à vingt ans après l'intervention, puis destruction.

Aucune règle n'a encore été mise en œuvre.

### ANNEXE 2.4 – La proposition d'un fournisseur d'équipements de protection individuelle (note de M. Pascal LAUZERAC, chef du groupement technique et logistique, avril 2027)

**A. Le suivi actuel des tenues de feu**

Le SDIS dispose de 8 000 tenues de feu (veste et surpantalon), deux par sapeur-pompier. Le fabricant garantit leur protection pendant dix ans ou 50 lavages, au premier des deux termes atteint. Chaque tenue suit le même parcours : livraison par le fournisseur, attribution à un sapeur-pompier par le magasin du groupement, lavage par le blanchisseur après chaque incendie, contrôle annuel par le magasin, réparation par le fournisseur, réforme. Les six magasiniers enregistrent ces événements à la main dans le logiciel de gestion du parc, à partir des bons du fournisseur et du blanchisseur.

Constats de l'inventaire de 2026 : 400 tenues, une sur vingt, n'ont pas été localisées ; une tenue sur quatre n'a aucun historique de lavage ; le blanchisseur LAVORDÈNE a facturé 30 000 lavages, alors que le logiciel de gestion du parc n'en a enregistré que 24 000 ; 1 000 contrôles annuels sont en retard. Après un accident survenu lors d'un incendie en 2026, il a fallu une semaine pour reconstituer l'historique de la tenue de l'agent blessé.

**B. La proposition de PROTÉVANCE**

PROTÉVANCE, fournisseur des tenues du SDIS et de deux SDIS voisins de la région, propose de coudre une puce dans chaque tenue. À chaque événement de sa vie, la puce est lue par un lecteur, chez le fournisseur, au magasin ou chez le blanchisseur, et l'événement est inscrit dans une chaîne de blocs partagée entre cinq acteurs : les trois SDIS, PROTÉVANCE et LAVORDÈNE, qui lave aussi les tenues des deux SDIS voisins. Chaque acteur disposerait d'un nœud ; PROTÉVANCE propose d'héberger les nœuds des SDIS qui le souhaitent. Selon PROTÉVANCE, les événements sont validés par les participants identifiés, sans minage, et ne peuvent plus être modifiés une fois inscrits ; aucune monnaie ni aucun jeton n'est utilisé. L'événement « attribution » enregistrerait le matricule du sapeur-pompier.

Les deux SDIS voisins n'ont pas encore pris position.

**C. Les coûts pour le SDIS du Val-d'Aurande et une autre solution**

| Poste | Chaîne de blocs de PROTÉVANCE | Base de données partagée |
|---|---|---|
| Lecteurs de puces (une fois) | 20 k€ | 20 k€ |
| Puces pour les tenues existantes (une fois) | 5 € par tenue | 5 € par tenue |
| Abonnement annuel | 30 k€ | 10 k€ |

La **base de données partagée** serait hébergée et administrée par un prestataire de services informatiques, retenu par les trois SDIS ; les cinq acteurs y enregistreraient les mêmes événements, lus par les mêmes puces, et le prestataire en tiendrait le journal des modifications. Aucun chiffrage du projet au-delà de ce tableau n'est attendu, et aucune procédure de choix du fournisseur n'est à organiser.

### ANNEXE 2.5 – Repères (au 31/12/2026)

| Repère | Nom exact et version | Ce qu'il faut en retenir |
|---|---|---|
| Données personnelles | règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | les données à caractère personnel sont collectées pour des finalités déterminées, limitées à ce qui est nécessaire (minimisation), conservées pendant une durée limitée, fixée selon la finalité (limitation de la conservation) et protégées contre la perte et l'accès non autorisé (intégrité et confidentialité) ; les données de santé sont des données sensibles, protégées de façon renforcée ; le registre des activités de traitement indique, pour chaque traitement, les délais prévus pour l'effacement des données ; le SDIS a désigné une déléguée à la protection des données, Mme Coralie FAVERJON ; aucune analyse juridique n'est attendue |
| Archivage électronique | NF Z42-013 (AFNOR) et son équivalent international ISO 14641 | normes d'application volontaire qui fixent les spécifications de conception et d'exploitation d'un système d'archivage électronique, pour assurer la conservation et l'intégrité des documents : intégrité, pérennité de la lecture, traçabilité des opérations ; elles servent de référence pour conserver des documents qui pourront servir de preuve |
| Gestion des documents d'activité | ISO 15489-1 — Information et documentation : gestion des documents d'activité (concepts et principes), édition de 2016 | norme qui pose les concepts et les principes de la gestion des documents d'activité : les documents sont gérés selon des règles écrites, de leur création à leur sort final (destruction ou conservation) |
| Chaînes de blocs | ISO 22739:2024 — Chaînes de blocs et technologies de registres distribués — Vocabulaire | norme de vocabulaire (bloc, nœud, consensus, registre distribué…), ni norme d'exigences ni solution |

### Travail à faire

Le SDIS produit chaque année 50 000 interventions, 150 000 enregistrements d'appels et 40 000 comptes rendus de secours, mais ses données ne lui permettent ni de mesurer sûrement sa sollicitation, ni de retrouver un enregistrement demandé par la justice. Le colonel hors classe GRANVOISE vous demande d'organiser les données des interventions, d'en tirer une analyse fiable de la sollicitation opérationnelle à présenter au conseil d'administration, de maîtriser la conservation des enregistrements et des comptes rendus, et de donner votre avis sur la proposition de PROTÉVANCE. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.5 ainsi que vos connaissances professionnelles.

**2.1 – Les données des interventions, des engins et des équipages (3,5 points)**

a) À partir des règles de gestion de l'annexe 2.1 C, établissez le modèle conceptuel des données des interventions, des engins et des équipages, puis traduisez-le en modèle logique, en énonçant les règles de passage que vous appliquez. Aucune requête n'est attendue.

b) Après avoir défini le dictionnaire des données, rédigez-en trois entrées pour des données de votre modèle. Proposez ensuite trois règles de qualité qui traitent chacune l'un des problèmes de l'annexe 2.1 B, en précisant la dimension de la qualité des données concernée.

**2.2 – L'analyse de la sollicitation opérationnelle (4,5 points)**

a) Après avoir défini la chaîne de valeur des données, décrivez la chaîne de traitement qui produira l'analyse de la sollicitation opérationnelle, en montrant, à chaque étape, une limite des chiffres de l'annexe 2.2 ou un problème de qualité de l'annexe 2.1 B qu'elle doit traiter.

b) Formulez trois constats argumentés tirés de l'annexe 2.2, puis appréciez l'affirmation de M. PRUNEVAUX. Aucun calcul statistique n'est attendu.

c) Après avoir défini l'analyse prédictive, indiquez ce qu'elle apporterait au SDIS, en précisant deux conditions de sa réussite et deux de ses limites. Proposez enfin la représentation visuelle qui montrerait le mieux au conseil d'administration la sollicitation opérationnelle par commune, et justifiez-la.

**2.3 – La conservation des enregistrements et des comptes rendus de secours (3 points)**

a) Décrivez le cycle de vie des enregistrements des appels et des comptes rendus de secours, de leur création à leur destruction, en fixant une règle à chaque étape.

b) Après avoir distingué le stockage et l'archivage électronique, indiquez ce que le RGPD et les normes d'archivage électronique imposent ou apportent au SDIS pour ces données, puis proposez trois mesures. Aucune analyse juridique n'est attendue.

**2.4 – La proposition de PROTÉVANCE (2 points)**

a) Après avoir défini la chaîne de blocs, expliquez le fonctionnement de la chaîne de blocs de consortium proposée par PROTÉVANCE et précisez le type d'application dont il s'agit.

b) Appréciez la valeur ajoutée, les coûts et les limites de cette proposition au regard de la base de données partagée de l'annexe 2.4 C, puis concluez.
