# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 29

**DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES CHANTIERS ET DES LOGEMENTS (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 2.1 – Les données d'un chantier (note de Mme Nadège CHAMBAROUX, directrice des opérations, mars 2027)

**A. Du premier contact à la réception : qui produit quoi, dans quel outil, sous quel identifiant**

| Étape | Données produites | Outil | Identifiant utilisé |
|---|---|---|---|
| Demande du particulier, rendez-vous | coordonnées, adresse du logement, origine de la demande | gestion de la relation client | numéro de contact |
| Visite technique | formulaire (surfaces, parois, menuiseries, équipements, consommations d'énergie déclarées par le propriétaire), croquis, photos avant travaux | application de visite technique | numéro de visite, attribué par la tablette |
| Calcul thermique | consommation estimée avant et après travaux | logiciel de calcul thermique | nom du client et commune, dans le nom du fichier |
| Devis et avenants | ouvrages, quantités, prix, lots confiés aux entreprises partenaires | logiciel de devis et de facturation | numéro de devis, qui change à chaque nouvelle version |
| Commande de matériaux | articles, quantités, date et lieu de livraison | courriel ou site internet du négociant | référence du négociant ; numéro de devis indiqué sur une commande sur deux |
| Planning | dates, équipe ou entreprise partenaire affectée | tableur partagé du planning | nom du client et commune |
| Suivi du chantier | heures des équipes ; photos en cours et après travaux ; attestations d'autocontrôle des partenaires | feuilles d'heures papier ; tablettes de chantier, puis espace de stockage partagé (un dossier par conducteur de travaux) | nom du client |
| Réception | procès-verbal signé par le client, réserves éventuelles | papier, numérisé par le conducteur de travaux | nom du client |
| Facturation | situations de travaux (rénovations globales), facture finale | logiciel de devis et de facturation | numéro de facture |
| Dossier d'aides | pièces demandées par les organismes (devis, facture, calcul thermique, photos, procès-verbal, justificatifs du ménage) | tableur partagé de suivi des aides ; portails des organismes | numéro de dossier de l'organisme |

**B. Le contrôle de 100 dossiers de chantiers achevés en 2026 (février 2027)**

| Défaut constaté | Dossiers concernés, sur 100 |
|---|---|
| Adresse du logement écrite différemment d'un outil à l'autre | 35 |
| Photos avant travaux introuvables ou non datées | 20 |
| Devis signé différent de la dernière version enregistrée dans le logiciel de devis (avenant non reporté) | 15 |
| Procès-verbal de réception absent ou non signé | 12 |
| Calcul thermique ne correspondant pas aux travaux réalisés | 10 |
| Au moins un de ces défauts | 55 |

En 2026, environ 700 dossiers d'aides ont été déposés pour nos clients : environ 140 ont été jugés incomplets à la première demande (20 %) et environ 35 ont été rejetés définitivement pour une pièce manquante ou incohérente (5 %). Ces 35 dossiers représentaient environ 175 k€ d'aides perdues pour nos clients ; pour préserver la relation, nous leur avons accordé environ 70 k€ de gestes commerciaux. Retrouver toutes les pièces d'un chantier demande souvent plus d'une heure : il faut les chercher dans cinq outils, sous des identifiants différents.

**C. Les échanges avec les entreprises partenaires et les fournisseurs de matériaux**

- **Entreprises partenaires** : ce sont des PME et des micro-entreprises de 2 à 15 salariés. Chacune reçoit par courriel, ou par un lien de partage de fichiers, l'extrait du devis qui correspond à son lot, les plans et les photos ; elle renvoie par courriel son planning, ses photos de fin de travaux, son attestation d'autocontrôle et sa facture en PDF, que la comptabilité ressaisit. Les fichiers arrivent sous des noms libres ; une facture de partenaire sur trois ne mentionne ni notre numéro de devis ni l'adresse du chantier. Trois partenaires seulement disposent d'un logiciel de gestion capable d'échanger des données avec d'autres logiciels ; les autres établissent leurs documents avec un tableur ou un traitement de texte.
- **Fournisseurs de matériaux** : trois négociants, entreprises de taille intermédiaire, assurent environ 70 % de nos achats. Les commandes partent par courriel ou sur leur site internet ; les bons de livraison sont signés sur papier, au dépôt ou sur le chantier. Depuis septembre 2026, leurs factures arrivent sous forme électronique structurée dans le progiciel de comptabilité, par la plateforme agréée à laquelle il est raccordé ; mais elles ne portent le numéro de devis que si la commande l'indiquait. Deux des trois négociants proposent à leurs clients professionnels une interface de programmation (API) qui permet de passer commande depuis un logiciel et d'en recevoir le suivi (confirmation, livraison, facture) ; notre logiciel de devis possède lui aussi une interface de programmation documentée. Ces possibilités n'ont jamais été utilisées.

**D. Le projet de « dossier numérique du chantier »**

Je propose que chaque chantier dispose d'un dossier numérique unique, qui réunisse dès la signature du devis toutes ses données et toutes ses pièces, consultable sur tablette par le conducteur de travaux et le chef d'équipe, partagé avec chaque entreprise partenaire pour son lot, et où la chargée des dossiers d'aides trouverait les pièces sans les chercher. M. Romain TRÉVASSOU, responsable informatique, indique que l'éditeur du logiciel de devis et de facturation propose en option un module de suivi de chantier (environ 4 k€ par an), que l'application de visite technique exporte ses formulaires en fichier tableur et ses photos par lots, et que le logiciel de calcul thermique n'exporte ses résultats qu'en PDF.

Avis recueillis en mars 2027 :
- **Mme Léa FONTRIVAL, responsable du bureau d'études** : « Le dossier doit naître à la visite, pas à la signature : nos relevés et nos calculs servent avant le devis, et plus de la moitié des logements visités ne deviennent jamais des chantiers. »
- **Une chargée des dossiers d'aides** : « Je n'ai pas besoin de toutes les versions de chaque pièce, mais de la bonne. »
- **Le gérant d'une entreprise partenaire de plomberie et de chauffage** : « Je travaille pour quatre entreprises qui ont chacune leur outil. Je veux bien déposer mes documents chez vous, mais je ne les ressaisirai pas dans un cinquième logiciel. »
- **Un conducteur de travaux** : « Si je dois classer chaque photo à la main, ce ne sera pas fait. »

### ANNEXE 2.2 – Les marges des chantiers en 2026 (relevé que vous avez établi avec la comptabilité, février 2027)

**A. Les marges des chantiers achevés en 2026**

Conventions : la marge d'un chantier est sa marge sur coûts directs, c'est-à-dire le chiffre d'affaires facturé, diminué des matériaux, de la main-d'œuvre des équipes (heures imputées au chantier multipliées par un coût horaire standard) et des factures des entreprises partenaires. La marge prévue est celle du devis signé, avenants enregistrés compris. Montants en milliers d'euros ; taux en pourcentage du chiffre d'affaires, arrondis à l'unité. Relevé établi le 31 janvier 2027, avec les factures reçues à cette date.

*Tableau 1 – Par type de travaux*

| Type de travaux | Chantiers | Chiffre d'affaires | Marge prévue | Marge constatée | Chantiers dont la marge constatée est inférieure de plus de 5 points à la marge prévue |
|---|---|---|---|---|---|
| Rénovations globales | 125 | 7 500 | 2 400 (32 %) | 1 650 (22 %) | 50 (40 %) |
| Travaux par lots | 875 | 17 500 | 4 900 (28 %) | 4 550 (26 %) | 105 (12 %) |
| **Total** | **1 000** | **25 000** | **7 300 (29 %)** | **6 200 (25 %)** | **155 (16 %)** |

Dix rénovations globales expliquent à elles seules environ 300 k€ de l'écart entre la marge prévue et la marge constatée.

*Tableau 2 – Selon la réalisation des travaux*

| Réalisation | Chantiers | Chiffre d'affaires | Marge prévue | Marge constatée |
|---|---|---|---|---|
| Par les seules équipes de SOLVÉRANCE Habitat | 550 | 11 000 | 28 % | 23 % |
| Avec au moins une entreprise partenaire (dont les 125 rénovations globales) | 450 | 14 000 | 30 % | 26 % |

*Tableau 3 – Par secteur*

| Secteur | Chantiers | Chiffre d'affaires | Part des rénovations globales dans le chiffre d'affaires | Marge prévue | Marge constatée |
|---|---|---|---|---|---|
| Lyon Est (dont Vénissieux) | 400 | 9 500 | 24 % | 29 % | 26 % |
| Lyon Ouest et Nord | 300 | 7 500 | 30 % | 29 % | 25 % |
| Ain | 200 | 5 000 | 30 % | 29 % | 24 % |
| Nord de l'Isère | 100 | 3 000 | 50 % | 30 % | 21 % |

*Tableau 4 – Par trimestre d'achèvement*

| Trimestre | 1er | 2e | 3e | 4e |
|---|---|---|---|---|
| Chiffre d'affaires des chantiers achevés | 5 500 | 6 000 | 6 500 | 7 000 |
| Marge constatée | 27 % | 26 % | 24 % | 23 % |

Quinze compagnons ont été recrutés en 2026, pour la plupart au second semestre.

**B. Les données utilisées et leurs défauts**

- **Heures** : chaque chef d'équipe remplit le vendredi, de mémoire, une feuille d'heures hebdomadaire sur papier, que les assistantes d'exploitation saisissent dans le progiciel de paie. Sur environ 80 000 heures productives des compagnons en 2026, environ 12 000 (15 %) ont été imputées à « dépôt et divers », sans chantier : elles ne figurent dans aucune marge.
- **Achats de matériaux** : 8,6 M€ en 2026, dont environ 1,7 M€ (20 %) ne sont rattachés à aucun chantier (achats au comptoir des négociants, sorties du stock du dépôt) ; dans le tableur, ils sont répartis chaque mois entre les chantiers au prorata de leur chiffre d'affaires.
- **Factures des entreprises partenaires** : elles arrivent souvent plus d'un mois après la fin des travaux ; au 31 janvier 2027, environ 300 k€ de factures relatives à des chantiers achevés en 2026 n'étaient pas reçues.
- **Avancement des rénovations globales** : les situations de travaux sont établies chaque mois d'après l'avancement déclaré par le conducteur de travaux, sans autre contrôle ; une situation peut être modifiée dans le logiciel de facturation tant qu'elle n'a pas été transférée en comptabilité. Au 31 décembre 2026, 40 rénovations globales étaient en cours ; les situations qui leur avaient été facturées atteignaient 1,2 M€. En janvier 2027, le bureau d'études a examiné dix de ces chantiers : l'avancement réel était inférieur de 15 points en moyenne à l'avancement déclaré.
- **Avenants** : des avenants acceptés par les clients ne sont pas enregistrés dans le logiciel de devis (15 dossiers sur 100 lors du contrôle de février 2027).
- Les comptes de l'exercice 2026, présentés au comité stratégique de mars 2027, ont été arrêtés à partir des mêmes données.

**C. L'outil d'analyse aujourd'hui et deux possibilités**

- **Aujourd'hui** : la comptable principale consolide chaque mois, à la main, dans un tableur, quatre extractions (devis et factures ; achats et factures des partenaires, tirés de la comptabilité ; heures, tirées de la paie ; planning), rapprochées par le nom du client. Ce travail lui prend environ trois jours par mois ; l'analyse est disponible vers le 20 du mois suivant. En 2026, trois versions différentes de l'analyse de juin ont circulé. Les conducteurs de travaux ne la reçoivent pas ; seul le total par type de travaux est présenté au comité stratégique.
- **Possibilité 1 – tableur avancé structuré** : requêtes de préparation enregistrées qui importent les extractions, modèle qui relie les tables par le numéro de chantier, tableaux croisés et graphiques mis à jour à chaque import ; formation de la comptable : 5 k€ ; environ un jour de travail par mois ; le fichier reste sur le poste de la comptable et l'analyse est diffusée en PDF.
- **Possibilité 2 – outil décisionnel en ligne** : connexion automatique aux logiciels de devis et de facturation, de comptabilité et de paie par leurs interfaces de programmation, préparation des données programmée chaque nuit, tableaux de bord consultables sur ordinateur et sur tablette, droits par profil (comité stratégique, direction, chaque conducteur de travaux pour ses chantiers) ; mise en place par un intégrateur : 25 k€ ; abonnement : 6 k€ par an pour 20 utilisateurs. L'intégrateur prévient : « L'outil ne corrigera pas vos données ; il lui faut un numéro de chantier commun à tous vos logiciels. »

M. Arnaud VORGNAC, directeur de participations de TALVÉRIS Croissance, a demandé lors du comité de mars 2027 : « Je veux voir chaque trimestre où nous perdons de la marge, pas seulement un total. »

### ANNEXE 2.3 – Les données des logements et leurs usages (note de M. Romain TRÉVASSOU, responsable informatique, mars 2027)

**A. La base des logements**

- Depuis 2022, environ 8 000 logements visités ont été enregistrés dans l'application de visite technique : caractéristiques (surface, année de construction, parois, menuiseries, mode de chauffage), croquis, consommations d'énergie déclarées par les propriétaires, une quarantaine de photos de l'intérieur par logement (environ 320 000 photos). Les fiches papier des visites de 2018 à 2021, environ 1 000, ont été numérisées en PDF.
- Plus de la moitié de ces logements n'ont jamais fait l'objet d'un chantier : le propriétaire n'a pas signé le devis.
- Les calculs thermiques (environ 3 000) sont dans le logiciel du bureau d'études. Les justificatifs fournis par les ménages pour leurs dossiers d'aides (avis d'imposition, titres de propriété) sont dans l'espace de stockage partagé, dans un dossier ouvert à tous les salariés des services administratifs.
- Aucune donnée n'a jamais été supprimée. Il n'existe ni durée de conservation, ni registre des activités de traitement, ni liste des personnes qui ont accès à ces données ; personne n'est désigné pour en répondre.

**B. Les services en ligne qui portent ces données**

| Service en ligne | Données portées | Éditeur et lieu d'hébergement | Récupération des données en fin de contrat |
|---|---|---|---|
| Gestion de la relation client | coordonnées des clients et des prospects, historique des contacts | éditeur établi dans l'Union européenne ; hébergement dans l'Union | export complet en fichier tableur, à tout moment |
| Application de visite technique | formulaires, croquis, photos, consommations déclarées | éditeur dont le siège est hors de l'Union européenne ; données hébergées hors de l'Union | formulaires exportables en fichier tableur ; photos téléchargeables une à une ; données supprimées 30 jours après la fin du contrat ; conditions générales acceptées en ligne en 2022, modifiables par l'éditeur |
| Logiciel de calcul thermique | calculs avant et après travaux | éditeur français ; hébergement en France | résultats en PDF ; fichiers de calcul lisibles par ce seul logiciel |
| Logiciel de devis et de facturation | devis, factures, bibliothèque de prix construite depuis 2018 | éditeur français ; hébergement en France | devis et factures en PDF ; bibliothèque de prix exportable dans le seul format de l'éditeur ; export complet non prévu par le contrat, « étudié au cas par cas » |
| Messagerie, bureautique et espace de stockage | courriels, photos de chantier, procès-verbaux, justificatifs des ménages | fournisseur dont le siège est hors de l'Union européenne ; données stockées dans l'Union | export complet possible par l'administrateur |

Un fournisseur dont le siège est hors de l'Union européenne reste soumis au droit de son pays, qui peut, dans certains cas, permettre aux autorités de ce pays d'exiger l'accès aux données qu'il héberge, y compris en Europe.

**C. Positions exprimées**

- **M. Arnaud VORGNAC, directeur de participations de TALVÉRIS Croissance** : « Le fonds envisage de céder sa participation d'ici cinq ans. Neuf mille logements de la région lyonnaise décrits pièce par pièce, c'est un actif que les acquéreurs regarderont : il faudra le mettre en avant. En attendant, exploitez-le : relancez tous les propriétaires visités depuis 2018. »
- **M. Mathieu ROUSSERGUES, président** : « Ces données nous appartiennent : nous les avons collectées, nous en faisons ce que nous voulons. »
- **Mme Léa FONTRIVAL, responsable du bureau d'études** : « Comparer les logements visités nous aiderait à chiffrer plus juste. Encore faut-il que les relevés soient fiables : une consommation déclarée n'est pas une consommation mesurée. »
- **M. Romain TRÉVASSOU** : « Si l'éditeur de l'application de visite disparaît ou change ses conditions, je ne sais pas récupérer les photos. »

### ANNEXE 2.4 – Repères sur les données (au 31/12/2026)

| Texte ou référentiel | Objet principal | Situation au 31/12/2026 |
|---|---|---|
| DAMA-DMBOK (*Data Management Body of Knowledge*), DAMA International | Référentiel de bonnes pratiques de gestion des données, organisé en onze domaines de connaissance autour de la gouvernance des données (dont la qualité, la sécurité, les données de référence, les métadonnées) ; il décrit notamment les rôles de propriétaire et d'intendant des données. Ce n'est ni une norme ni un logiciel. | 2e édition (2017), révision 2024 |
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Données se rapportant à une personne physique identifiée ou identifiable : collectées pour des finalités déterminées, limitées à ce qui est nécessaire, conservées pendant une durée limitée au regard de la finalité, protégées par une sécurité adaptée au risque ; registre des activités de traitement ; recours à un sous-traitant (par exemple l'éditeur d'un service en ligne) encadré par un contrat qui prévoit notamment le sort des données à la fin du contrat ; en principe, transfert hors de l'Union européenne seulement vers un pays reconnu par la Commission européenne comme assurant une protection adéquate, ou moyennant des garanties appropriées. | Applicable depuis le 25/05/2018 |
| Règlement (UE) 2023/2854 sur les données (Data Act) | Les fournisseurs de services d'informatique en nuage, y compris de services en ligne, doivent permettre à leurs clients de changer de fournisseur et d'emporter leurs données (portabilité, assistance à la sortie, conditions fixées par le contrat) (chapitre VI). | Applicable depuis le 12/09/2025 |
| SecNumCloud, version 3.2 (ANSSI) | Référentiel d'exigences qui permet de qualifier des offres de services d'informatique en nuage, y compris au regard de leur protection contre l'application de lois extra-européennes. | En vigueur |
| Généralisation de la facturation électronique (article 91 de la loi de finances pour 2024 ; code général des impôts) | Les factures entre entreprises assujetties à la TVA établies en France sont émises, transmises et reçues sous forme électronique par l'intermédiaire d'une plateforme agréée par l'administration ; les formats admis sont Factur-X, UBL et CII. | Depuis le 01/09/2026 : réception obligatoire pour toutes les entreprises ; émission obligatoire pour les grandes entreprises et les entreprises de taille intermédiaire. À compter du 01/09/2027 : émission obligatoire pour les PME et les micro-entreprises. |

Il n'est demandé aucune analyse juridique des obligations de l'entreprise ni de ses contrats.

### Travail à faire

Le plan « Cap 2029 » veut maîtriser la marge de chaque chantier et préserver la confiance des clients ; le fonds TALVÉRIS Croissance s'intéresse, lui, à la valeur des données accumulées. M. ROUSSERGUES vous demande d'organiser les données des chantiers autour d'un dossier numérique, d'en tirer une analyse fiable des marges et de proposer une gouvernance des données de l'entreprise, notamment de la base des logements. Vous mobiliserez pour cela les annexes 1.1 et 2.1 à 2.4 ainsi que vos connaissances professionnelles.

**2.1 – Le dossier numérique du chantier et les échanges avec les partenaires (3 points)**

a) À partir de trois constats de l'annexe 2.1, montrez ce que coûte à SOLVÉRANCE Habitat l'organisation actuelle des données d'un chantier, puis proposez l'organisation qui fera du dossier numérique du chantier une source unique et cohérente : l'identifiant commun (attribution, propriétés, diffusion), le référentiel des clients et des logements, l'outil qui fait foi pour chaque grande catégorie de données et la circulation des données entre les outils. Vous tiendrez compte des avis recueillis. Aucun modèle des données n'est attendu.

b) Après avoir défini l'interopérabilité, proposez la solution d'échange de données à retenir, d'une part avec les entreprises partenaires, d'autre part avec les fournisseurs de matériaux (interface de programmation, formats ouverts, échanges structurés), en la justifiant par les annexes 2.1 et 2.4, et indiquez pour chacune deux conditions organisationnelles de réussite. Aucun détail technique des échanges n'est attendu.

**2.2 – L'analyse des marges des chantiers (4,5 points)**

a) Décrivez la chaîne de traitement des données qui produirait chaque mois l'analyse des marges par chantier, de la collecte à la restitution, en indiquant pour chaque étape ce qu'elle traite chez SOLVÉRANCE Habitat et le défaut de l'annexe 2.2 qu'elle doit corriger.

b) Après avoir montré qu'un outil ne suffit pas à fonder une démarche décisionnelle, choisissez entre les deux possibilités de l'annexe 2.2 C en justifiant votre choix par trois critères, puis estimez de tête le coût de l'outil décisionnel en ligne sur trois ans et rapprochez-le de l'enjeu d'un point de marge.

c) À partir de l'annexe 2.2, formulez trois constats argumentés sur les marges des chantiers achevés en 2026, chacun assorti d'une précaution de lecture tirée des annexes et de sa conséquence pour le plan « Cap 2029 ». Aucun calcul statistique n'est attendu.

d) Proposez deux représentations visuelles, l'une pour le comité stratégique, l'autre pour les conducteurs de travaux, en précisant pour chacune le message, le type de graphique, le piège de lecture à éviter et l'indicateur représenté (formule, source, fréquence, cible et axe du tableau de bord).

**2.3 – La fiabilité des données de gestion des chantiers (2,5 points)**

a) Montrez en quoi la fiabilité des heures, des achats, de l'avancement déclaré et des situations de travaux facturées conditionne celle des marges par chantier et celle des comptes présentés au comité stratégique. Aucune règle comptable n'est attendue.

b) Proposez quatre contrôles intégrés au système d'information pour fiabiliser ces données : un contrôle à la saisie, un contrôle de rattachement, un rapprochement et un verrouillage. Pour chacun, précisez le risque couvert, sa nature (préventif ou détectif) et son responsable.

**2.4 – La gouvernance stratégique des données et la base des logements (3 points)**

a) Après avoir défini la gouvernance des données, proposez-en les principes pour SOLVÉRANCE Habitat selon cinq enjeux (qualité, conformité, sécurité, valorisation, cycle de vie), chacun appliqué à un constat des annexes, et indiquez qui en répond dans une PME sans direction des systèmes d'information.

b) Appréciez la base des logements comme actif immatériel (deux sources de valeur, trois risques qui la menacent), puis répondez aux positions de M. VORGNAC et de M. ROUSSERGUES. Aucune valorisation chiffrée ni analyse juridique n'est attendue.

c) À partir des annexes 2.3 et 2.4, analysez les enjeux de souveraineté et de réversibilité liés aux services en ligne qui portent les données de l'entreprise, puis proposez trois mesures. Le choix d'un hébergement n'est pas attendu.
