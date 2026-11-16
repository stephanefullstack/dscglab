# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 26

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES PARCELLES ET DES APPORTS ; AUTHENTIFIER LES BOUTEILLES (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 9, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. Les Vignerons de ROCALDÈNE sont une union de coopératives agricoles dont le siège est à Pézenas, dans l'Hérault. Fondée en 1987, l'union regroupe neuf caves coopératives de l'Hérault et de l'Aude, auxquelles environ 1 400 viticulteurs apportent la vendange de quelque 6 500 hectares de vignes. Chaque cave reçoit et vinifie la vendange de ses adhérents ; l'union assemble et élève les vins, les conditionne sur son site de Pézenas et les commercialise en vrac auprès de négociants, en bouteilles auprès de la grande distribution et à l'export. L'union est administrée par un conseil composé des présidents des neuf caves, que préside M. Gilles ESCOURBIAC, viticulteur ; sa directrice générale, Mme Hélène MAZERANDE, dirige les services de l'union. L'union et ses caves emploient 260 salariés permanents, rejoints par environ 180 saisonniers pendant les vendanges. Le chiffre d'affaires de l'union s'est élevé à 145 millions d'euros en 2026 ; 2,2 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Le plan « ROCALDÈNE 2030 », adopté par le conseil de l'union en décembre 2026, fixe trois priorités : adapter le vignoble et l'offre au changement climatique et conquérir de nouveaux marchés, notamment à l'export et dans la vente en ligne ; mieux connaître la qualité des apports, de la parcelle à la bouteille, pour mieux la valoriser ; garantir la continuité du système d'information pendant les campagnes et en réduire l'empreinte environnementale. Mme MAZERANDE en rend compte au conseil à chaque réunion.

Vous êtes responsable administratif et financier adjoint de l'union depuis 2025, rattaché à la directrice générale et chargé du projet de refonte du système d'information. Mme MAZERANDE vous demande trois travaux : éclairer la stratégie du système d'information et préparer sa refonte (dossier 1) ; organiser et exploiter les données des parcelles et des apports, et apprécier un projet d'authentification des bouteilles (dossier 2) ; assurer la continuité du système d'information pendant les vendanges, fiabiliser les apports et choisir un hébergement responsable (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation des Vignerons de ROCALDÈNE et chiffres clés

Les Vignerons de ROCALDÈNE sont une union de coopératives agricoles fondée en 1987, dont le siège et le site de conditionnement sont à Pézenas (Hérault). Neuf caves coopératives de l'Hérault et de l'Aude en sont membres. Les viticulteurs sont adhérents de leur cave : chaque cave reçoit la vendange de ses adhérents pendant les vendanges, de fin août à mi-octobre, la vinifie et conserve les vins dans ses cuves. L'union assemble et élève les vins des neuf caves, les conditionne et les commercialise. L'exercice coïncide avec l'année civile : l'exercice 2026 est le dernier exercice clos.

**Chiffres clés de 2026**

| Donnée | Valeur |
|---|---|
| Chiffre d'affaires de l'union | 145 M€ : vrac auprès de négociants 35 % (environ 51 M€), bouteilles vendues à la grande distribution en France 40 % (58 M€), export 25 % (environ 36 M€ ; Europe du Nord, Amérique du Nord, Asie) ; vente en ligne aux particuliers à l'étude |
| Vendange 2026 | environ 380 000 hectolitres, soit 380 milliers d'hectolitres |
| Vignoble | environ 6 500 hectares, exploités par environ 1 400 viticulteurs adhérents des caves |
| Effectif permanent | 260 salariés : environ 150 à l'union (conditionnement et logistique 75, commercial et service clients 25, production, qualité et laboratoire 20, services administratifs et financiers et direction 24, équipe informatique 6) et 110 dans les caves ; environ 180 saisonniers dans les caves pendant les vendanges ; aucune cave n'a d'informaticien |
| Système d'information | à l'union : un progiciel de gestion (gestion commerciale, stocks, comptabilité), dont le support par l'éditeur s'arrête fin 2028 ; le laboratoire d'analyses de l'union ; un portail des adhérents aux fonctions limitées ; une salle informatique au siège de Pézenas. Dans chaque cave : un logiciel de cave (réception et pesée des apports, suivi des cuves) ; les neuf caves utilisent les logiciels de quatre éditeurs différents |
| Budget du système d'information | 2,2 M€ (environ 1,5 % du chiffre d'affaires) |
| Plan « ROCALDÈNE 2030 » (adopté en décembre 2026) | adapter le vignoble et l'offre au changement climatique et conquérir de nouveaux marchés (export, vente en ligne) ; mieux connaître la qualité des apports, de la parcelle à la bouteille, pour mieux la valoriser ; garantir la continuité du système d'information pendant les campagnes et en réduire l'empreinte environnementale |

**Les neuf caves coopératives**

| Cave | Département | Adhérents | Vignes (hectares) | Salariés permanents |
|---|---|---|---|---|
| Cave de CAUSSELAC | Hérault | 230 | 1 100 | 18 |
| Cave de ROQUEVERNE | Hérault | 200 | 950 | 16 |
| Cave de LAURADEL | Aude | 180 | 850 | 14 |
| Cave de SAINT-BRÉZIAN | Hérault | 170 | 800 | 13 |
| Cave de CABRISSAC | Aude | 150 | 700 | 12 |
| Cave de GRAUSSELLE | Hérault | 140 | 650 | 11 |
| Cave de PECHAUROUX | Aude | 130 | 550 | 10 |
| Cave de TERRAGOUSSE | Hérault | 110 | 500 | 9 |
| Cave de VALCROZIÈRES | Aude | 90 | 400 | 7 |
| **Total** | | **1 400** | **6 500** | **110** |

Chaque cave est dirigée par un directeur salarié, sous l'autorité de son propre conseil, que préside un viticulteur élu ; le président de chaque cave siège au conseil de l'union.

**Organigramme simplifié (mars 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil de l'union | président du conseil, composé des présidents des neuf caves | M. Gilles ESCOURBIAC, viticulteur |
| Direction générale | directrice générale, qui porte le plan « ROCALDÈNE 2030 » | Mme Hélène MAZERANDE |
| Rattaché à la directrice générale | directeur commercial (vrac, grande distribution, export, service clients, projet de vente en ligne) | M. Damien SALVERNAC |
| Rattachée à la directrice générale | directrice de la production et de la qualité (assemblage et élevage des vins, laboratoire d'analyses, conditionnement et logistique) | Mme Claire BOUSQUIÉRAN |
| Rattaché à la directrice générale | directeur administratif et financier (comptabilité, contrôle de gestion, paie et ressources humaines, achats) | M. Philippe VERDAGNOL |
| Direction administrative et financière | responsable administratif et financier adjoint, rattaché à la directrice générale pour le projet de refonte du système d'information | vous |
| Rattaché au directeur administratif et financier | responsable du système d'information (équipe informatique de 6 personnes) | M. Sébastien CAUSSINEL |
| Caves | neuf caves coopératives, chacune avec son président et son directeur | — |

Le comité de direction de l'union réunit chaque mois la directrice générale et les trois directeurs qui lui sont rattachés. La directrice générale réunit chaque trimestre les neuf directeurs de cave.

### ANNEXE 2.1 – Les données des parcelles et des apports (note de Mme Claire BOUSQUIÉRAN, directrice de la production et de la qualité, février 2027)

**A. D'où viennent les données**

| Source | Tenue par | Contenu | Forme et volume |
|---|---|---|---|
| Fichier des parcelles | chaque cave | parcelles de ses adhérents : numéro de parcelle propre à la cave, adhérent exploitant, commune, lieu-dit, surface, cépage, année de plantation | tableur dans six caves, module du logiciel de cave dans trois ; environ 11 000 parcelles au total |
| Fichier des adhérents | chaque cave | numéro d'adhérent propre à la cave, nom, prénom, commune, téléphone, adresse électronique, date d'adhésion | logiciel de cave ; 1 400 fiches au total |
| Logiciels de cave (réception de la vendange) | chaque cave | bon d'apport établi à la pesée : date et heure, adhérent, parcelle déclarée par le viticulteur, poids, degré potentiel mesuré à la réception, état sanitaire noté par l'agent de réception | logiciels de quatre éditeurs ; environ 20 000 apports pendant la vendange 2026 |
| Laboratoire de l'union | union | un prélèvement de moût de chaque apport, analysé le jour même : acidité totale, pH | logiciel du laboratoire ; environ 22 000 prélèvements en 2026, rattachés à l'apport par le numéro du bon de la cave, ressaisi à la main |
| Stations météorologiques et sondes | union | pluie, température, humidité ; humidité du sol | quatre stations, dans les secteurs de ROQUEVERNE, LAURADEL, SAINT-BRÉZIAN et VALCROZIÈRES ; sondes dans 30 parcelles des caves de SAINT-BRÉZIAN et de ROQUEVERNE ; relevés consultés sur le site du fournisseur des stations, sans lien avec les autres données |
| Observations des techniciens viticoles | union | visites des parcelles : maladies, stade de maturité, estimation de la récolte | trois tableurs personnels des trois techniciens de l'union |

Chaque lundi, mon équipe reçoit par courriel neuf extractions différentes des logiciels de cave. Les tableaux de l'annexe 2.2 ont été établis à la main, en janvier 2027 ; c'est la première fois que l'union rassemble ces données pour les neuf caves.

**B. Ce que nous avons constaté en rapprochant les neuf fichiers (janvier 2027)**

1. *Identifiants de parcelle propres à chaque cave* : chaque cave numérote ses parcelles à sa manière ; le même numéro (par exemple « P-0123 ») désigne des parcelles différentes dans sept caves.
2. *Cépages codés différemment* : les neuf fichiers emploient 31 codes ou libellés différents pour 12 cépages (« SYR », « Syrah », « SY », « syrah N »…).
3. *Adhérents en double* : environ 40 viticulteurs livrent deux caves ; ils ont deux numéros d'adhérent et deux fiches, dont les coordonnées diffèrent parfois. Les 1 400 fiches correspondent donc à environ 1 360 viticulteurs.
4. *Apports sans parcelle* : la parcelle est déclarée oralement à la pesée ; elle manque ou ne correspond à aucune parcelle du fichier pour un peu plus d'un tiers des volumes livrés (annexe 2.2).
5. *Surfaces non tenues à jour* : les fichiers totalisent 6 650 hectares, contre 6 500 hectares effectivement en production ; les arrachages et les cessions de parcelles ne sont pas toujours enregistrés.
6. *Mesures non homogènes* : sept caves enregistrent le degré potentiel en % vol. ; LAURADEL et CABRISSAC enregistrent les sucres en grammes par litre, que mon équipe convertit. L'état sanitaire est noté de 1 (sain) à 3 (dégradé) dans les cinq caves de l'Hérault et de 1 (sain) à 5 (très dégradé) dans les quatre caves de l'Aude, souvent par des saisonniers ; aucune définition écrite ne précise ce que recouvre chaque note.
7. *Analyses orphelines* : environ 1 100 prélèvements (5 %) ne sont rattachés à aucun apport, parce que le numéro du bon a été mal ressaisi au laboratoire.

**C. Règles de gestion retenues pour le futur référentiel commun « parcelles et apports »**

- RG1 : un adhérent est identifié par un numéro unique attribué par l'union ; on enregistre son nom, son prénom, sa commune, son téléphone et son adresse électronique.
- RG2 : une cave est identifiée par un code ; on enregistre son nom et son département.
- RG3 : un adhérent adhère à une ou plusieurs caves ; on enregistre la date d'adhésion à chaque cave ; chaque cave compte au moins un adhérent.
- RG4 : une parcelle est identifiée par un numéro unique attribué par l'union ; on enregistre sa commune, son lieu-dit, sa surface en hectares et son année de plantation. Une parcelle est exploitée par un et un seul adhérent, l'exploitant actuel ; un adhérent exploite une ou plusieurs parcelles.
- RG5 : une parcelle est plantée d'un seul cépage ; un cépage est identifié par un code commun à l'union, avec son libellé et sa couleur ; un cépage peut n'être planté sur aucune parcelle (cépage retenu pour les replantations, pas encore planté).
- RG6 : un apport est identifié par le numéro du bon attribué à la pesée ; on enregistre la date, l'heure de pesée, le poids, le degré potentiel et l'état sanitaire. Un apport est la livraison d'un adhérent à une cave ; il porte sur une seule parcelle. Un adhérent, une cave ou une parcelle peut n'avoir aucun apport.
- RG7 : un apport donne lieu à un ou plusieurs prélèvements ; un prélèvement, identifié par un numéro attribué par le laboratoire, concerne un seul apport ; on enregistre la date d'analyse, l'acidité totale et le pH.
- RG8 : les relevés météorologiques, les sondes et les observations des techniciens ne sont pas à modéliser à ce stade.

### ANNEXE 2.2 – Les apports de la vendange 2026 et le projet de mieux rémunérer la qualité

**A. Les apports par cave (tableau établi par la direction de la production et de la qualité, janvier 2027)**

| Cave | Département | Volume (milliers d'hl) | Rendement (hl/ha) | Degré moyen (% vol.) | Part retenue pour les cuvées haut de gamme | Part des apports à l'état sanitaire dégradé | Part des volumes rattachés à une parcelle | Station météorologique dans le secteur |
|---|---|---|---|---|---|---|---|---|
| CAUSSELAC | Hérault | 77 | 70 | 12,5 | 5 % | 6 % | 50 % | non |
| ROQUEVERNE | Hérault | 57 | 60 | 13,0 | 10 % | 5 % | 70 % | oui |
| LAURADEL | Aude | 51 | 60 | 13,0 | 10 % | 15 % | 60 % | oui |
| SAINT-BRÉZIAN | Hérault | 36 | 45 | 14,0 | 30 % | 3 % | 95 % | oui |
| CABRISSAC | Aude | 42 | 60 | 12,5 | 5 % | 20 % | 40 % | non |
| GRAUSSELLE | Hérault | 39 | 60 | 13,5 | 15 % | 4 % | 80 % | non |
| PECHAUROUX | Aude | 33 | 60 | 12,5 | 5 % | 25 % | 30 % | non |
| TERRAGOUSSE | Hérault | 25 | 50 | 13,5 | 20 % | 5 % | 90 % | non |
| VALCROZIÈRES | Aude | 20 | 50 | 13,5 | 20 % | 10 % | 70 % | oui |
| **Union** | | **380** | **environ 58** | **13,0** | **environ 12 %** | **environ 10 %** | **environ 62 %** | **4 secteurs sur 9** |

Notes : rendement calculé sur les surfaces en production ; degré moyen de LAURADEL et de CABRISSAC converti à partir des sucres ; état sanitaire « dégradé » : note 3 sur l'échelle de 1 à 3 dans l'Hérault, notes 3 à 5 sur l'échelle de 1 à 5 dans l'Aude ; la part retenue pour les cuvées haut de gamme est décidée par les œnologues de l'union lors des assemblages, selon la qualité des cuves et les besoins commerciaux des cuvées haut de gamme (environ 44 milliers d'hl en 2026). Données d'une seule vendange.

**B. Pluies relevées du 10 au 25 septembre 2026, en pleine vendange (stations de l'union)**

| Secteur | ROQUEVERNE | SAINT-BRÉZIAN | LAURADEL | VALCROZIÈRES |
|---|---|---|---|---|
| Pluie (mm) | 30 | 20 | 110 | 70 |

**C. Le projet du conseil**

Aujourd'hui, chaque cave rémunère ses adhérents selon ses propres règles, fondées sur le volume et le degré. Le conseil de l'union souhaite, dans le cadre du plan « ROCALDÈNE 2030 », que la qualité des apports soit mieux reconnue, à partir de critères communs aux neuf caves ; il doit en débattre en avril 2027. Les modalités de calcul ne sont pas arrêtées et ne sont pas l'objet de ce dossier.

**D. Positions exprimées lors du conseil de février 2027**

- M. Henri SOULAGNET, président de la cave de SAINT-BRÉZIAN : « Nos rendements sont les plus faibles de l'union, notre vendange est la plus saine et 30 % de nos apports partent en haut de gamme. Les chiffres sont clairs : il faut payer la qualité dès la vendange 2027, sur la base de ce tableau. »
- Mme Brigitte TARASCOUL, présidente de la cave de PECHAUROUX : « Ce tableau compare ce qui ne se compare pas. Chez nous, l'état sanitaire est noté sur cinq par des saisonniers, ailleurs sur trois ; il a plu bien plus dans l'Aude en septembre ; et c'est l'union qui choisit seule les cuves qui partent en haut de gamme, selon ce qu'elle a vendu. Payer sur ces chiffres, ce serait punir nos adhérents pour une averse. »
- Un prestataire a présenté au conseil un service qui « prévoirait dès juillet, parcelle par parcelle, la qualité de la vendange », à partir des données des caves et des stations météorologiques, afin de fixer les primes à la qualité avant les vendanges. M. Gilles ESCOURBIAC demande ce qu'il faut en penser.

### ANNEXE 2.3 – Le projet d'authentification des cuvées exportées (mars 2027)

**A. Le problème signalé**

L'union exporte chaque année environ 600 000 bouteilles de ses cuvées haut de gamme « Signature ROCALDÈNE » vers l'Asie et l'Amérique du Nord. En novembre 2026, son importateur de Hong Kong a signalé des bouteilles portant des étiquettes copiées de ces cuvées, vendues sur des sites en ligne ; il estime leur nombre à environ 2 000 en 2026. Un distributeur canadien demande de son côté « une preuve d'origine que ses équipes puissent vérifier elles-mêmes, sans compte chez l'union ».

**B. La proposition de SCELLAVIN, jeune entreprise créée en 2024**

- Chaque bouteille des cuvées concernées reçoit, au conditionnement à Pézenas, une étiquette connectée : une puce sans contact que le consommateur lit avec son téléphone et qui se détruit si on tente de la décoller.
- À chaque bouteille est associé un jeton non fongible, unique, inscrit sur une blockchain publique fonctionnant par preuve d'enjeu, choisie par SCELLAVIN. L'union y inscrit, au conditionnement, la cuvée, le lot, la date de mise en bouteille et les caves d'origine des vins assemblés.
- L'importateur puis le distributeur enregistrent la réception de la bouteille ; le consommateur qui lit la puce voit l'historique et peut inscrire son prénom et sa ville « pour devenir propriétaire du jeton de sa bouteille ».
- SCELLAVIN envisage, « dans un second temps », de permettre la revente des jetons des bouteilles de collection, indépendamment des bouteilles, sur sa propre place de marché.

**C. Coûts annoncés et alternative (en milliers d'euros hors taxes, sans actualisation)**

| Poste | SCELLAVIN | Alternative proposée par M. Sébastien CAUSSINEL |
|---|---|---|
| Mise en place | 120 | 150 (registre des bouteilles dans une base de données de l'union, page de vérification en ligne en trois langues) |
| Coût annuel des étiquettes ou des codes | 180 (0,30 € par bouteille) | 30 (0,05 € par bouteille pour un code imprimé sur l'étiquette, signé numériquement par l'union) |
| Abonnement annuel à la plateforme et frais d'inscription sur la blockchain | 60 | — |
| Exploitation annuelle par l'équipe informatique | — | 30 |
| Adaptation de la ligne de conditionnement des cuvées concernées (dépense unique, la première année) | 90 | — |

Dans l'alternative, chaque bouteille porte un numéro de série unique, enregistré par l'union au conditionnement avec la cuvée, le lot et la date ; la lecture du code ouvre la page de vérification de l'union, qui confirme l'origine et signale qu'un même code a déjà été lu ailleurs.

**D. Avis recueillis**

- M. Damien SALVERNAC, directeur commercial : « Nos importateurs asiatiques adorent l'idée : c'est moderne et cela rassure. L'image du jeton vaut à elle seule l'investissement. »
- M. Sébastien CAUSSINEL, responsable du système d'information : « Nous serions les seuls à écrire l'origine des bouteilles dans ce registre. Si nos données de départ sont fausses, la blockchain les gardera fausses pour toujours. Et je ne vois pas ce que deviennent les prénoms des consommateurs inscrits sur une blockchain publique. »

### ANNEXE 2.4 – Repères sur les données et la blockchain (au 31/12/2026)

| Texte ou référentiel | Objet principal | Situation au 31/12/2026 |
|---|---|---|
| DAMA-DMBOK (*Data Management Body of Knowledge*), DAMA International | Référentiel de bonnes pratiques de gestion des données, organisé en onze domaines de connaissance autour de la gouvernance des données (dont la qualité, les données de référence, les métadonnées) ; il décrit notamment les rôles de propriétaire et d'intendant des données. Ce n'est ni une norme ni un logiciel. | 2e édition (2017), révision 2024 |
| Règlement (UE) 2016/679 (RGPD) | Protection des données à caractère personnel, c'est-à-dire se rapportant à une personne physique identifiée ou identifiable (par exemple un adhérent exploitant en nom propre ou un consommateur) : données collectées pour des finalités déterminées, limitées à ce qui est nécessaire, conservées pendant une durée limitée, effacées dans les cas prévus par le règlement ; registre des activités de traitement ; délégué à la protection des données. | Applicable depuis le 25/05/2018 |
| Règlement (UE) 2023/1114 sur les marchés de crypto-actifs (« MiCA ») | Définit le crypto-actif comme une représentation numérique d'une valeur ou d'un droit pouvant être transférée et stockée de manière électronique au moyen de la technologie des registres distribués ou d'une technologie similaire. Encadre l'offre au public et l'admission à la négociation de crypto-actifs, l'émission des jetons qui visent une valeur stable et l'agrément des prestataires de services sur crypto-actifs. Sont exclus de son champ les crypto-actifs uniques et non fongibles avec d'autres crypto-actifs (article 2, paragraphe 3). | Applicable depuis le 30/12/2024 |
| ISO 22739:2024 | Norme de vocabulaire des chaînes de blocs et des technologies de registres distribués (bloc, nœud, consensus, jeton…) ; ce n'est pas une norme d'exigences. | En vigueur (2e édition) |

### Travail à faire

Le plan « ROCALDÈNE 2030 » veut mieux connaître la qualité des apports, de la parcelle à la bouteille, pour mieux la valoriser. Mme MAZERANDE vous demande d'organiser les données des parcelles et des apports des neuf caves, d'éclairer avec ces données le débat du conseil sur une meilleure rémunération de la qualité, puis de lui donner un avis sur le projet d'authentification des cuvées exportées. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.4 ainsi que vos connaissances professionnelles.

**2.1 – Modèle conceptuel des données des parcelles et des apports (2 points)**

À partir des règles de gestion de l'annexe 2.1 C, construisez le modèle conceptuel des données du référentiel commun (entités, identifiants, attributs, associations et cardinalités), en justifiant chaque cardinalité par une règle de gestion. Le modèle logique n'est pas demandé.

**2.2 – Cohérence, interopérabilité et qualité des données (3 points)**

a) Après avoir défini l'interopérabilité, proposez l'organisation qui rendra les données des parcelles et des apports cohérentes et interopérables entre les neuf caves et l'union : référentiel commun, identifiants uniques et circulation des données, sur les plans technique, sémantique et organisationnel. Aucun détail technique des échanges n'est attendu.

b) Après avoir défini le dictionnaire de données, rédigez son entrée pour deux données : le degré potentiel de l'apport et l'état sanitaire de l'apport. Chaque entrée précisera quatre rubriques que vous choisirez et justifierez.

c) Proposez trois règles de qualité des données, chacune rattachée à une dimension de la qualité et à un constat de l'annexe 2.1 B.

**2.3 – Rôles et responsabilités sur les données (1 point)**

En vous appuyant sur le référentiel DAMA-DMBOK, proposez la répartition des rôles et des responsabilités sur les données des parcelles et des apports entre l'union et les caves : trois rôles, avec pour chacun ses missions et son titulaire.

**2.4 – Chaîne de valeur des données et analyse des apports de la vendange 2026 (4,5 points)**

a) Après avoir présenté la chaîne de valeur des données, appliquez-la au cas, de la parcelle au conseil de l'union, et montrez comment elle peut éclairer la décision de mieux rémunérer la qualité des apports.

b) À partir de l'annexe 2.2, formulez trois constats argumentés sur les apports de la vendange 2026, en assortissant chacun d'une précaution de lecture, puis appréciez les positions des deux présidents de cave. Aucun calcul statistique n'est attendu.

c) Indiquez, en la justifiant, la méthode d'analyse (descriptive ou exploratoire) adaptée à l'étape suivante, puis expliquez, par deux arguments tirés des annexes, pourquoi la prévision de la qualité par parcelle proposée au conseil est prématurée.

d) Proposez deux représentations visuelles, l'une pour le conseil de l'union, l'autre pour les directeurs de cave, en précisant pour chacune le message qu'elle porte et le piège de lecture à éviter.

**2.5 – Le projet d'authentification des cuvées exportées (2,5 points)**

a) Après avoir rappelé ce qu'est une blockchain et ce qui la distingue d'une base de données centralisée, situez le projet de SCELLAVIN dans la typologie des applications de la blockchain.

b) Appréciez deux opportunités et trois risques ou limites du projet au regard du problème signalé, puis comparez-le à l'alternative proposée par M. CAUSSINEL, en estimant de tête le coût de chacune sur trois ans, et recommandez une solution.

c) À partir des repères de l'annexe 2.4, indiquez à quelle condition les jetons du projet échappent au règlement MiCA et quelle autre réglementation le projet doit respecter. Aucune analyse juridique n'est attendue.
