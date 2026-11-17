# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 28

**DOSSIER 1 – STRUCTURER LA GOUVERNANCE ET LE PILOTAGE DU SYSTÈME D'INFORMATION (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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

### ANNEXE 1.2 – Le système d'information de SOLVÉRANCE Habitat aujourd'hui (note de M. Romain TRÉVASSOU, responsable informatique, et témoignages recueillis en mars 2027)

**A. Les applications et leurs usages**

| Repère | Application (service en ligne, sauf les tableurs) | Usage | Utilisateurs | Souscrite en, par |
|---|---|---|---|---|
| A1 | gestion de la relation client | demandes des particuliers, rendez-vous de visite, relances, suivi des devis ; comporte un module de prise de rendez-vous en ligne, compris dans l'abonnement et jamais activé | pôle commercial, accueil, direction | 2019, le président |
| A2 | application de visite technique sur tablette | formulaires de visite, photos, croquis cotés à la main | conseillers, techniciens du bureau d'études | 2022, le président |
| A3 | logiciel de calcul thermique | calcul de la consommation avant et après travaux ; résultat édité en PDF | bureau d'études | 2019, la responsable du bureau d'études |
| A4 | logiciel de devis et de facturation spécialisé dans le bâtiment | bibliothèque de prix, devis, factures | conseillers, conducteurs de travaux (en partie), assistantes d'exploitation, comptabilité | 2018, le président |
| A5 | progiciel de comptabilité et de paie | comptabilité, paie | comptabilité et paie | 2018, le président |
| A6 | messagerie et suite bureautique en ligne | courriel, agendas, documents ; espace de stockage et de partage de fichiers compris, qui permet aussi d'envoyer des fichiers volumineux à des destinataires extérieurs | tous les salariés qui disposent d'un compte | 2018, le président |
| A7 | outil de prise de rendez-vous en ligne | les particuliers réservent un créneau de visite depuis le site internet | pôle commercial | 2025, la responsable commerciale, sans avis de l'informatique |
| A8 | service de partage de fichiers volumineux | plans et études envoyés aux clients et aux partenaires | bureau d'études | 2024, la responsable du bureau d'études, sans avis de l'informatique |
| A9 | service de partage de fichiers volumineux, d'un autre fournisseur | photos et documents des chantiers envoyés aux partenaires | conducteurs de travaux | 2025, la directrice des opérations, sans avis de l'informatique |
| T1 | tableur partagé du planning des équipes | affectation des équipes et des partenaires aux chantiers | assistantes d'exploitation, conducteurs de travaux | 2019 |
| T2 | tableur partagé de suivi des dossiers d'aides | pièces, dépôts et paiements des aides des clients | chargées des dossiers d'aides | 2020 |

A7, A8 et A9 sont payés par la carte bancaire des services ou sur notes de frais. Je n'ai découvert A8 et A9 qu'en préparant cette note.

**B. Les échanges entre les applications, de la visite à la comptabilité**

| Flux | De | Vers | Contenu | Mode |
|---|---|---|---|---|
| F1 | A7 rendez-vous en ligne | A1 gestion de la relation client | rendez-vous pris par les particuliers | ressaisie par l'accueil |
| F2 | A1 gestion de la relation client | A2 visite technique | coordonnées du client et adresse du logement | ressaisie par le conseiller |
| F3 | A2 visite technique | A3 calcul thermique | caractéristiques du logement (surfaces, parois, équipements) | ressaisie par le bureau d'études |
| F4 | A2 visite technique | A4 devis et facturation | métrés et ouvrages relevés | ressaisie par le conseiller |
| F5 | A3 calcul thermique | A4 devis et facturation | résultat du calcul thermique | fichier PDF joint au devis |
| F6 | A4 devis et facturation | A1 gestion de la relation client | devis signé (imprimé, signé, numérisé) | ressaisie du statut par le conseiller |
| F7 | A4 devis et facturation | T1 planning | chantier signé à planifier | ressaisie par les assistantes d'exploitation |
| F8 | T1 planning | A4 devis et facturation | fin de chantier, signalée par courriel du conducteur de travaux | ressaisie pour établir la facture |
| F9 | A4 devis et facturation, A3 calcul thermique | T2 suivi des aides | devis, facture, résultat du calcul thermique | ressaisie, puis dépôt des pièces sur les portails des organismes d'aides |
| F10 | A4 devis et facturation | A5 comptabilité | factures de vente | fichier exporté chaque mois, importé par la comptabilité |

Sur dix échanges, huit sont des ressaisies et deux passent par un fichier ; aucun n'est automatique. Les coordonnées du client et les caractéristiques de son logement sont saisies dans cinq outils (A1, A2, A3, A4, T2).

**C. Comment se prennent les décisions informatiques**

- Il n'existe ni plan du système d'information, ni budget, ni instance où les demandes sont examinées. Le président décide au fil des occasions : l'application de visite technique a été souscrite en 2022 après la démonstration d'un éditeur sur un salon ; en 2025, 20 tablettes ont été achetées lors d'une promotion, puis réservées aux chefs d'équipe pour consulter les plans, l'application de visite y fonctionnant mal ; en février 2027, le président a promis à l'éditeur du logiciel de devis d'essayer son outil de chiffrage (annexe 1.3).
- Les services souscrivent eux-mêmes des outils en ligne (A7, A8, A9), en acceptant les conditions des fournisseurs. Personne ne tient la liste des abonnements ni celle des comptes ouverts.
- Le responsable informatique ne participe à aucune réunion de direction ni au comité stratégique.

**D. Mon travail et le support du parc**

- Je consacre environ 60 % de mon temps à dépanner les utilisateurs, 25 % à administrer les services en ligne (comptes, droits, mises à jour) et 15 % aux projets. Je suis le pompier de l'entreprise : je n'ai jamais pu préparer l'ouverture des agences.
- Le prestataire local, BRIVALDE Informatique, est payé au ticket : environ 500 tickets en 2026, à 120 € en moyenne. Le contrat ne prévoit ni délai d'intervention, ni délai de rétablissement, ni matériel de remplacement, ni compte rendu. Le délai moyen de résolution a été de 4 jours ouvrés ; 80 pannes ont concerné des tablettes de chantier, et 40 visites techniques ont dû être reportées faute de tablette. Le prestataire ne connaît ni nos priorités ni nos applications métier.
- Si je suis absent, personne ne connaît les accès d'administration des services en ligne.

**E. Témoignages**

- **M. Mathieu ROUSSERGUES, président** : « J'ai toujours décidé vite, et c'est ce qui nous a fait grandir. Mais chacun vient me voir avec son outil, et je ne sais plus arbitrer entre la directrice des opérations, la responsable commerciale et le bureau d'études. Je ne veux pas d'une administration de grand groupe : nous sommes une PME. »
- **Mme Nadège CHAMBAROUX, directrice des opérations** : « Le planning tient dans un tableur que trois assistantes modifient en même temps ; avec deux agences de plus, ce ne sera plus possible. Quand une tablette tombe en panne, un conducteur de travaux travaille quatre jours sans ses dossiers. Je veux un outil de planning cette année, et je connais mieux que personne les besoins du terrain : je ne veux pas qu'un comité choisisse à ma place. »
- **Mme Sophie MARQUENDE, responsable commerciale** : « Nos concurrents remettent leurs devis en quelques jours ; nous mettons trois semaines, et le client signe ailleurs. L'outil de rendez-vous en ligne a soulagé l'accueil : je l'ai pris parce que personne n'avait le temps de s'en occuper. Le relevé en trois dimensions et le chiffrage assisté, c'est maintenant. »
- **M. Arnaud VORGNAC, directeur de participations de TALVÉRIS Croissance** : « Le fonds est prêt à financer l'ouverture des deux agences. Avant de s'engager, il demande une revue indépendante du système d'information, dont les conclusions seront présentées au comité stratégique de juillet 2027 : le système d'information peut-il supporter le doublement de l'activité ? Les données des clients sont-elles fiables, protégées et traitées conformément aux règles ? Qui décide, et sur quelle base ? L'entreprise dépend-elle d'une seule personne et de quelques éditeurs ? Combien coûte réellement le système d'information ? »

### ANNEXE 1.3 – Les technologies envisagées (note de Mme Léa FONTRIVAL, responsable du bureau d'études, et de Mme Sophie MARQUENDE, responsable commerciale, mars 2027)

**A. Du premier contact au devis signé : la situation de 2026**

| Donnée | 2026 |
|---|---|
| Visites techniques réalisées | environ 2 400 |
| Devis remis | environ 2 000 |
| Devis signés | environ 1 000, soit un taux de signature de 50 % des devis remis |
| Délai moyen entre la visite et la remise du devis | 15 jours ouvrés (25 pour une rénovation globale, 12 pour des travaux par lots) |
| Taux de signature selon ce délai | 65 % des devis remis en moins de 7 jours ouvrés sont signés ; 35 % au-delà de 15 jours ouvrés |
| Délai moyen entre l'accord du client et le retour du devis signé (devis envoyé par courriel, imprimé, signé, numérisé et renvoyé) | 6 jours ouvrés |
| Temps de travail du conseiller pour un devis | 2 heures de visite, 3 heures d'établissement du devis (ressaisie des métrés, recherche des ouvrages dans la bibliothèque de prix) |
| Écart moyen entre les métrés estimés à la visite et les métrés réels du chantier | 10 % ; un chantier sur quatre dépasse cet écart |
| Surcoûts de matériaux et de main-d'œuvre dus aux écarts de métrés, non refacturés aux clients | environ 250 k€ (1 % du chiffre d'affaires) |

**B. Trois technologies**

1. **Relevé du logement en trois dimensions par tablette et maquette numérique** : une tablette munie d'un capteur adapté produit en une demi-heure une maquette numérique du logement, d'où sont tirés les métrés (écart annoncé de 2 à 3 %). Coût annoncé : 12 tablettes adaptées pour 18 k€ et un abonnement de 12 k€ par an. *Réserve de Mme FONTRIVAL* : « La maquette n'est pas lisible par notre logiciel de calcul thermique ; l'éditeur promet un format d'échange ouvert "d'ici 2028". »
2. **Outil d'aide au chiffrage par intelligence artificielle** : proposé par l'éditeur du logiciel de devis en complément de son abonnement (30 k€ par an), il propose, à partir des photos et des relevés, les ouvrages et les quantités puisés dans notre bibliothèque de prix ; le conseiller valide ou corrige la proposition avant d'éditer le devis. L'outil a été construit à partir des devis de plusieurs centaines d'entreprises clientes de l'éditeur. L'éditeur annonce des devis remis « en 48 heures ». Dans deux entreprises qui l'ont essayé, les propositions ont dû être corrigées dans 30 % des cas pour les maisons anciennes. *Réserves des conseillers* : « Un logiciel ne voit pas l'humidité derrière un doublage » ; « Si l'outil chiffre à notre place, à quoi servons-nous ? » ; « Les photos de l'intérieur des maisons de nos clients partent chez l'éditeur. » L'outil ne fonctionne qu'avec le logiciel de devis de cet éditeur.
3. **Signature électronique des devis** : signature sur la tablette du conseiller ou à distance par un lien sécurisé, pour 5 k€ par an. Une partie des clients âgés préfère le papier.

**C. Effets attendus des trois technologies réunies (estimations de l'éditeur et de la responsable commerciale, non vérifiées)**

| Donnée | 2026 | Attendu |
|---|---|---|
| Délai moyen entre la visite et la remise du devis | 15 jours ouvrés | 5 jours ouvrés |
| Taux de signature des devis remis | 50 % | 60 % |
| Écart moyen entre les métrés estimés et réels | 10 % | 3 % |
| Délai entre l'accord du client et le devis signé | 6 jours ouvrés | 1 jour ouvré |

Mme MARQUENDE ajoute : « À nombre de devis égal, 60 % de signature, ce sont 200 chantiers de plus par an. » Mme CHAMBAROUX rappelle que les équipes et les entreprises partenaires sont déjà pleinement occupées.

### ANNEXE 1.4 – Les dépenses du système d'information en 2026 (relevé que vous avez établi en mars 2027)

**A. Le suivi actuel**

Le seul suivi des dépenses du système d'information est le compte « dépenses informatiques » de la comptabilité, examiné une fois par an lors de la clôture : 360 k€ en 2026. Il n'existe ni budget, ni répartition par service, ni indicateur, ni inventaire des abonnements et des licences. En rapprochant les factures, les notes de frais et la paie, vous avez reconstitué 450 k€ de dépenses : 90 k€ sont enregistrés dans d'autres comptes (A7, A8 et A9 en frais divers et notes de frais pour 20 k€, formation pour 10 k€, salaire chargé du responsable informatique pour 60 k€).

**B. Les dépenses reconstituées de 2026 par nature (en milliers d'euros)**

| Nature | Détail | Montant |
|---|---|---|
| Abonnements aux services en ligne | détail au tableau C | 164 |
| Matériel | achats d'ordinateurs, de tablettes, de smartphones et d'imprimantes | 110 |
| Télécommunications | lignes mobiles des tablettes et smartphones, accès à internet | 40 |
| Support du parc par BRIVALDE Informatique | environ 500 tickets à 120 € en moyenne | 60 |
| Paramétrages par les éditeurs | modèles de devis, export des factures vers la comptabilité | 6 |
| Formation aux outils | | 10 |
| Temps interne | salaire chargé du responsable informatique | 60 |
| **Total** | | **450** |

**C. Les abonnements aux services en ligne**

| Application | Licences ou comptes payés | Licences ou comptes utilisés en mars 2027 | Prix annuel par licence ou compte | Montant 2026 (k€) |
|---|---|---|---|---|
| A1 gestion de la relation client | 20 | 15 | 1 200 € | 24 |
| A2 visite technique | 25 | 20 | 800 € | 20 |
| A3 calcul thermique | 8 | 8 | 2 500 € | 20 |
| A4 devis et facturation | 30 | 24 | 1 500 € | 45 |
| A5 comptabilité et paie | forfait | — | — | 15 |
| A6 messagerie et suite bureautique | 100 | 85 | 200 € | 20 |
| A7 prise de rendez-vous en ligne | 12 | 12 | 500 € | 6 |
| A8 partage de fichiers du bureau d'études | 8 | 8 | 750 € | 6 |
| A9 partage de fichiers des opérations | 10 | 10 | 800 € | 8 |
| **Total** | | | | **164** |

Les abonnements se renouvellent chaque année à leur date anniversaire ; le nombre de licences peut être réduit à cette date.

**D. Des coûts que personne ne suit (estimations de mars 2027)**

- **Ressaisies** : environ 600 jours de travail par an (conseillers 150, bureau d'études 100, assistantes d'exploitation 150, chargées des dossiers d'aides 150, comptabilité 50). Une journée de travail coûte en moyenne 250 €, charges comprises.
- **Attente des dépannages** : 80 pannes de tablettes de chantier, avec 4 jours ouvrés d'attente en moyenne ; 40 visites techniques reportées.
- **Entraide informelle** : les salariés les plus à l'aise dépannent leurs collègues, pour environ 100 jours de travail par an.
- **Temps du responsable informatique** absorbé par le dépannage (60 %), au détriment des projets.

### ANNEXE 1.5 – Repères méthodologiques et réglementaires (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Tenue d'un registre des activités de traitement (finalités, catégories de personnes, de données et de destinataires, délais d'effacement, mesures de sécurité). Recours à un sous-traitant (par exemple l'éditeur d'un service en ligne) encadré par un contrat qui prévoit notamment les instructions, la sécurité, le sort des données à la fin du contrat et les audits. Sécurité adaptée au risque. Notification à l'autorité de contrôle d'une violation de données dans les 72 heures. | Applicable depuis le 25/05/2018. Une proposition européenne de simplification (« omnibus numérique », 19/11/2025) modifiant ce règlement est en discussion et n'est pas applicable. |
| COBIT 2019 (ISACA) | Référentiel de gouvernance et de management de l'informatique : 40 objectifs répartis en cinq domaines (évaluer, diriger et surveiller ; aligner, planifier et organiser ; construire, acquérir et mettre en œuvre ; délivrer, servir et soutenir ; surveiller, évaluer et apprécier). | En vigueur |
| ISO/IEC 27001:2022 | Norme d'exigences d'un système de management de la sécurité de l'information, assortie d'une annexe de 93 mesures de sécurité. | En vigueur |
| ITIL (PeopleCert) | Référentiel de bonnes pratiques de gestion des services informatiques : gestion des niveaux de service, des incidents, amélioration continue. | En vigueur |

Il n'est demandé aucune analyse juridique des obligations de l'entreprise ni des contrats.

### Travail à faire

Le système d'information de SOLVÉRANCE Habitat a grandi au rythme des occasions. Avant d'ouvrir deux agences, M. ROUSSERGUES veut qu'il serve le plan « Cap 2029 », qu'il soit gouverné et que son coût soit connu ; le fonds TALVÉRIS Croissance demande en outre une revue indépendante. Le président vous demande d'éclairer les choix technologiques, de représenter le système d'information actuel, d'organiser la fonction et la gouvernance du système d'information, de revoir le contrat de support, de mettre en place le suivi de ses dépenses et de cadrer la revue demandée par le fonds. Vous mobiliserez pour cela les annexes 1.1 à 1.5 ainsi que vos connaissances professionnelles.

**1.1 – Les technologies du devis et la stratégie du système d'information (3,5 points)**

a) Après avoir défini le modèle économique d'une entreprise et rappelé l'intérêt d'une veille technologique active, analysez, à partir de l'annexe 1.3, l'impact des trois technologies envisagées sur le modèle économique de SOLVÉRANCE Habitat, selon quatre composantes : la création de valeur pour le client, le délai et le taux de signature des devis, la marge des chantiers, la relation avec le client. Vous indiquerez pour chaque composante une limite ou une condition tirée des réserves exprimées, puis conclurez sur les conditions auxquelles ces technologies peuvent servir le plan « Cap 2029 ».

b) Proposez trois orientations de la stratégie du système d'information au service du plan « Cap 2029 », chacune justifiée par une priorité du plan et par un constat des annexes ; l'une d'elles au moins intégrera une technologie émergente, dont vous préciserez la famille, l'apport et la condition de réussite. Le fonctionnement interne des outils d'intelligence artificielle n'est pas attendu.

**1.2 – La cartographie du système d'information (1,5 point)**

Après avoir précisé ce qu'est une cartographie applicative et ce qui la distingue d'une cartographie fonctionnelle, établissez, sous la forme d'un schéma ou d'un tableau, une cartographie simplifiée du système d'information de l'annexe 1.2 (domaines fonctionnels, applications, principaux flux), puis dégagez-en trois faiblesses : les ressaisies, les redondances, les applications isolées. Aucune architecture cible n'est attendue.

**1.3 – L'organisation de la fonction système d'information et sa gouvernance (3 points)**

a) Comparez trois façons d'organiser la fonction système d'information de SOLVÉRANCE Habitat : recruter un responsable des systèmes d'information, recourir à un directeur des systèmes d'information à temps partagé, confier davantage au prestataire. Pour chacune, précisez un avantage et une limite au regard du cas, puis recommandez, en la justifiant, l'organisation à retenir pour les trois années du plan, en la situant parmi les modèles d'organisation de la fonction système d'information.

b) Après avoir défini la gouvernance du système d'information, proposez-en le dispositif pour SOLVÉRANCE Habitat : une instance (composition, fréquence, décisions), le rôle du président, des responsables des services et du fonds, et trois règles de gouvernance, dont une règle d'avis préalable à toute souscription d'un service en ligne, en répondant aux craintes exprimées par le président et la directrice des opérations.

**1.4 – Le contrat de support du parc (1 point)**

Caractérisez le contrat actuel avec BRIVALDE Informatique, puis indiquez, en le justifiant, le type de contrat adapté au support du parc (au ticket, au forfait, infogérance avec niveaux de service) et deux engagements à y faire figurer, chacun relié à un constat de l'annexe 1.2. Aucune analyse juridique n'est attendue.

**1.5 – Les dépenses du système d'information et leur suivi (3 points)**

a) Après avoir défini les coûts cachés et rappelé l'apport du contrôle de gestion appliqué au système d'information, montrez, à partir de l'annexe 1.4, trois limites du suivi actuel des dépenses, identifiez trois coûts cachés en les estimant de tête quand l'annexe le permet, et chiffrez de tête, en milliers d'euros, une économie réalisable dès 2027.

b) Proposez le dispositif de suivi des dépenses du système d'information : la structure du budget (par nature et par service), deux indicateurs dont vous préciserez la formule, la source, la fréquence, la cible et l'axe du tableau de bord, et la revue périodique du dispositif dans une démarche d'amélioration continue. Aucun calcul d'écart budgétaire n'est attendu.

**1.6 – La revue du système d'information demandée par le fonds (2 points)**

Après avoir défini l'audit du système d'information, cadrez la revue demandée par TALVÉRIS Croissance : ses objectifs, son périmètre, sa démarche en quatre étapes, les quatre critères de performance et de conformité qu'elle retiendra (fiabilité, sécurité, conformité au RGPD, gouvernance), chacun illustré par un point à examiner chez SOLVÉRANCE Habitat, et ses livrables. Le diagnostic lui-même n'est pas attendu.
