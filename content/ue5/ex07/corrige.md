# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 7 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 architecture et urbanisation, F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026 ; Data Act et Data Governance Act relus sur le texte officiel le 10/11/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Organisation des données du parc | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données | 3 |
| 1.2 Interopérabilité avec les bailleurs | `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 2 |
| 1.3 Analyse des données et aide à la décision | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 3,5 |
| 1.4 Gouvernance, cycle de vie et valeur des données | `2.3.a` Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques ; `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ; `2.3.f` Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques | 3,5 |
| 1.5 Valorisation des données | `2.3.e` Aspects réglementaires (RGPD, archivage légal) et monétisation des données | 2 |
| **Dossier 1 – Organiser, analyser et valoriser les données des appareils connectés** |  | **14** |

Répartition indicative : connaissances (définitions, chaîne de valeur, méthodes d'analyse) 3 points (items 1.1 b-1 pour moitié, 1.2 a-1, 1.3 a pour moitié, 1.3 b pour moitié, 1.4 a-1, 1.4 c-1 pour moitié, 1.5-1) ; analyse des annexes et recommandations 11 points, soit environ 79 %. Durée conseillée : 14 points × 4,5 minutes ≈ 1 h 03.

---

### 1.1 – Organisation des données du parc (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ».

**Annexes mobilisées** : annexes 1.1 (parc, agences), 1.2 (sources, flux, constats du profilage, témoignages de Mme CHAMBRUN et de Mme OLLAGNIER) et 1.3 (usages attendus des données).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Atteinte à la **cohérence** démontrée par un constat chiffré (identifiants multiples, boîtiers non rattachés, décomptes divergents) et sa conséquence | 0,5 |
| a-2 | Atteinte à la **qualité** démontrée par un constat chiffré (codes panne « autre », dates de mise en service manquantes) et sa conséquence | 0,5 |
| a-3 | Atteinte à la **circulation** démontrée par un constat (fichier nocturne propriétaire, ressaisies, tableurs trimestriels, PDF mensuel) et sa conséquence | 0,5 |
| b-1 | Données de référence définies et trois principes d'organisation cible appliqués au parc (référentiel unique des appareils, identifiant commun, données de référence partagées et gouvernées) | 0,5 |
| b-2 | Schéma lisible des flux cibles : sources, intégration, plateforme de données (référentiel des appareils, données de fonctionnement, données intégrées), utilisateurs internes et externes, sens des flux | 1 |

**Réponse indicative**

*1.1 a) – Une organisation qui nuit à la cohérence, à la qualité et à la circulation des données*

- **Cohérence** (0,5 pt) : un même appareil connecté porte quatre identifiants (numéro de série du boîtier, numéro d'appareil propre à l'agence, numéro de contrat, adresse de l'immeuble), reliés par une table de correspondance tenue à la main, et les appareils non connectés sont repérés dans les tableurs par l'agence ou l'adresse ; 1 800 boîtiers sur 31 000 (environ 6 %) ne sont rattachés à aucun appareil identifié, et le parc compte 52 000 appareils selon le progiciel de gestion mais 52 900 selon les fichiers des agences. Conséquence : on ne peut pas relier une alarme à un contrat ni à l'historique de l'appareil, ni même compter le parc de façon incontestable ; tout taux de panne par appareil est faussé.
- **Qualité** (0,5 pt) : 35 % des bons de dépannage portent le code « autre » ou aucun code, parce que la liste de 140 codes est inutilisable sur le terminal (Mme OLLAGNIER) ; la date de mise en service manque pour 30 % des appareils non connectés. Conséquence : les causes de panne et l'âge des appareils, variables clés de la maintenance qui anticipe, sont inexploitables ; l'exactitude et la complétude font défaut.
- **Circulation** (0,5 pt) : les données de fonctionnement détaillées restent sur la plateforme du constructeur, dans son format propriétaire, consultables écran par écran et effacées après 13 mois ; seul un fichier nocturne des alarmes en sort ; les interventions hors contrat sont ressaisies ; les tableurs des 21 000 appareils non connectés remontent par courriel chaque trimestre ; les bailleurs reçoivent un PDF mensuel fait à la main. Conséquence : données tardives, recopiées, captives d'un fournisseur et inaccessibles aux clients qui les demandent.

Conclusion : les données sont organisées par outil et par agence, non par objet de gestion ; l'appareil, objet central du métier, n'a pas de description unique.

*1.1 b) – Organisation cible et flux*

Les **données de référence** (données maîtres) sont les données partagées et stables qui décrivent les objets de gestion de l'organisation (ici les appareils, les immeubles et les clients, les contrats, les modèles de composants, les codes panne) ; elles sont gérées une seule fois, dans un référentiel unique, sous la responsabilité d'un propriétaire, et utilisées par toutes les applications (F07 § 1).

Trois principes (0,5 pt avec la définition) :
1. **Référentiel unique des appareils** (gestion des données de référence, en anglais *master data management*) : une fiche par appareil, connecté ou non, avec ses caractéristiques (marque, modèle, date de mise en service, niveaux, composants), l'immeuble, le client et le contrat ; il remplace la table de correspondance manuelle et les 34 tableurs ; le progiciel de gestion reste la référence des contrats.
2. **Identifiant commun** : un identifiant d'appareil attribué par le groupe, unique et stable pendant toute la vie de l'appareil, que portent le boîtier, le bon d'intervention, le contrat, la pièce posée et l'échange avec le bailleur ; le rattachement des 1 800 boîtiers orphelins et le dédoublonnage des 52 900 fiches précèdent la mise en service.
3. **Données de référence partagées et gouvernées** : nomenclatures communes (liste de codes panne resserrée et utilisable sur le terminal, types d'appareils, types d'immeubles), dictionnaire des données (définition de la « disponibilité », d'une « panne »), propriétaire désigné pour chaque domaine, contrôles à la saisie (date de mise en service obligatoire).

Schéma attendu (1 pt ; format libre, JUR-T10) :

```
SOURCES                         INTÉGRATION                PLATEFORME DE DONNÉES DU GROUPE             UTILISATEURS
Boîtiers de télésurveillance ─┐                          ┌───────────────────────────────────┐   ┌─> Direction de la maintenance (tableaux de bord)
  (plateforme du constructeur)│  connecteurs, API,       │ Référentiel unique des appareils   │   ├─> Responsables d'agence (mobile)
Terminaux des techniciens ────┼─> contrôles de qualité ─>│ (identifiant commun, immeubles,    │──>├─> Techniciens (historique de l'appareil)
Progiciel de gestion          │  et rapprochement par    │  clients, contrats, nomenclatures) │   ├─> Analyse et prévision des pannes
  (contrats, clients) ────────┤  l'identifiant commun    │ Données de fonctionnement          │   ├─> Bailleurs et syndics (API, format ouvert)
Gestion des stocks (pièces) ──┤                          │  historisées au-delà de 13 mois    │   └─> Partenaires autorisés (données convenues)
Saisie des appareils non      │                          │ Données intégrées pour l'analyse   │
  connectés (fin des tableurs)┘                          └───────────────────────────────────┘
                     <── retour du référentiel vers les sources (l'identifiant commun est inscrit dans chaque outil)
```

Sont valorisés : le sens des flux et le retour du référentiel vers les applications sources ; la fin des tableurs et des ressaisies ; la récupération en continu des données du constructeur (portabilité) ; un point d'exposition unique vers les clients et les partenaires, avec contrôle des droits.

**Réponses tolérées**
- Constats différents de ceux du corrigé (rapport PDF mensuel pour la circulation, liste de codes trop longue pour la qualité) dès lors qu'ils sont tirés de l'annexe 1.2 et rattachés à la bonne propriété.
- Dimensions de la qualité nommées selon ISO/IEC 25012 (exactitude, complétude, unicité, cohérence, actualité) ; les doublons d'appareils rattachés à l'unicité plutôt qu'à la cohérence.
- Plateforme de données décrite comme un lac de données associé à un référentiel de données de référence, ou comme un entrepôt alimenté par le référentiel, si le rôle de chaque composant est juste (le lac pour les données brutes des boîtiers, le référentiel pour l'appareil).
- Schéma en tableau des flux (source, donnée, destination, fréquence) au lieu d'un dessin, s'il fait apparaître les mêmes éléments.

**Erreurs types**
- *Interopérabilité ou organisation des données réduite à la technique* (`ET-36`) — « acheter un logiciel de données » ou « tout mettre dans le cloud » ; juste : l'organisation cible repose d'abord sur un référentiel, un identifiant et des responsabilités.
- *Définition sans application au cas* (`JUR-T01`) — principes de gestion des données de référence récités sans les 1 800 boîtiers, les quatre identifiants ni les 34 tableurs ; juste : chaque principe corrige un constat de l'annexe 1.2.
- *Schéma illisible ou sans flux* (`JUR-T10`) — liste d'applications sans sources, sans sens des échanges ni utilisateurs ; juste : sources, plateforme et utilisateurs reliés par des flux orientés.
- *MDM non explicité* (`ET-13`) — sigle employé seul, confondu avec la gestion des terminaux mobiles des techniciens ; juste : écrire « gestion des données de référence ».

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Données de référence, référentiel unique, dictionnaire de données | définition, principes, rôle du propriétaire | F07 § 1 et 6.2 | notion de cours |
| ISO/IEC 25012 (2008) — Modèle de qualité des données | dimensions de la qualité, à titre d'exemple | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| Urbanisation : une donnée de référence, un seul propriétaire ; zone d'échange | principes d'architecture des flux | F03 § 1 et 3 | notion de cours |

---

### 1.2 – Interopérabilité avec les bailleurs (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) » ; `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ».

**Annexes mobilisées** : annexes 1.2 (demande des grands clients, témoignage de la directrice du patrimoine) et 1.4 (repères du Data Act).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Interopérabilité définie (capacité de systèmes hétérogènes à échanger des données et à les utiliser sans intervention manuelle) | 0,5 |
| a-2 | Dimensions technique, sémantique et organisationnelle appliquées à la demande des bailleurs | 0,5 |
| b-1 | Mode d'échange proposé et justifié : interface de programmation (API) publiée par le groupe, commune à tous les bailleurs, données en format ouvert et structuré (JSON ou XML) | 0,5 |
| b-2 | Trois conditions de succès appliquées (documentation et dictionnaire partagé, sécurisation des accès, versionnement et contrat d'interface, qualité préalable des données) ; 0,5 pour les trois | 0,5 |

**Réponse indicative**

*1.2 a) – Définition et dimensions*

L'interopérabilité est la capacité de systèmes hétérogènes, appartenant le cas échéant à des organisations différentes, à échanger des données et à les utiliser sans ressaisie ni intervention manuelle, grâce à des normes et des standards partagés (0,5 pt). Appliquée à la demande des bailleurs (0,5 pt pour les trois dimensions) :
- **technique** : une interface automatisée, disponible chaque jour, entre la plateforme du groupe et des outils de gestion de patrimoine différents d'un bailleur à l'autre ; aujourd'hui, un PDF établi à la main ;
- **sémantique** : un sens commun des données échangées : définition de la disponibilité (période de mesure, pannes prises en compte, arrêts programmés exclus ou non), identifiant de l'appareil et de l'immeuble que le bailleur sait rapprocher de son propre patrimoine, codes panne compréhensibles ;
- **organisationnelle** : règles partagées sur qui publie et qui consomme, à quelle fréquence, avec quel niveau de service, qui traite les écarts et les demandes d'évolution ; les services informatiques des bailleurs ne développeront pas d'échange propre à chaque prestataire.

*1.2 b) – Mode d'échange et conditions de succès*

Mode d'échange recommandé (0,5 pt) : une **API** publiée par le groupe, c'est-à-dire une interface documentée qui permet à l'outil de chaque bailleur d'interroger la plateforme de données et d'obtenir, pour ses seuls appareils, la disponibilité et les pannes, dans un **format ouvert et structuré** (JSON, ou XML si les outils des bailleurs l'exigent). Justification : une seule interface pour les trois bailleurs et les clients suivants, au lieu de développements spécifiques ; échange quotidien ou en continu, sans ressaisie ; format couramment utilisé et lisible par machine, ce que le Data Act attend du détenteur des données lorsqu'un utilisateur demande l'accès aux données de son produit connecté (annexe 1.4) ; indépendance vis-à-vis du format propriétaire du constructeur des boîtiers. Un export de fichier en format ouvert peut compléter l'API pour les petits clients sans outil.

Trois conditions de succès (0,5 pt pour les trois) :
1. **Documentation et dictionnaire partagés** : description publiée des données, de leur définition (disponibilité) et de leur fréquence de mise à jour, validée avec les bailleurs ;
2. **Sécurisation des accès** : chaque bailleur n'accède qu'à ses appareils (droits par client), authentification des systèmes appelants, journalisation des accès, exclusion des données à caractère personnel (enregistrements d'appels, nom du technicien) ;
3. **Versionnement et contrat d'interface** : chaque évolution de l'API fait l'objet d'une nouvelle version, l'ancienne restant disponible pendant un délai annoncé ; un contrat d'interface fixe la disponibilité du service, le support et le traitement des incidents.

Condition préalable à mentionner : la qualité des données (identifiant commun, rattachement des 1 800 boîtiers) ; exposer des données fausses à des clients ruinerait la confiance.

**Réponses tolérées**
- Dimension **syntaxique** (formats) distinguée de la dimension technique : acceptée, la question n'en exigeant que trois.
- Échange de fichiers en format ouvert (CSV, XML) déposés chaque nuit sur un espace sécurisé, si le candidat en montre les limites (fraîcheur, contrôle des versions) et le présente comme une étape avant l'API.
- Portail client en ligne en complément de l'API pour les clients qui consultent sans intégrer les données.

**Erreurs types**
- *Interopérabilité seulement technique* (`ET-36`) — l'API présentée comme suffisante, sans définition commune de la disponibilité ni règles partagées ; juste : les trois dimensions sont traitées.
- *Approfondissement technique des protocoles* — détail des méthodes d'appel, des schémas ou des mécanismes d'authentification ; juste : le principe et le rôle de l'API et du format ouvert suffisent (limite du programme).
- *Analyse générique* (`JUR-T01`) — avantages des API en général, sans les bailleurs, leurs outils différents ni le PDF mensuel ; juste : la recommandation part de la demande de l'annexe 1.2.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Interopérabilité : niveaux technique, syntaxique, sémantique, organisationnel ; API, XML, JSON, formats ouverts | définition, principes, conditions | F07 § 7 ; F03 § 3 | notion de cours |
| Règlement (UE) 2023/2854 (Data Act) | accès de l'utilisateur, format structuré, couramment utilisé et lisible par machine | `data_act` / F07 § 8.5 ; annexe 1.4 | applicable depuis le 12/09/2025 |

---

### 1.3 – Analyse des données et aide à la décision (3,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.d` « Outils décisionnels : Excel avancé, Power BI, Tableau, etc. » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ».

**Annexes mobilisées** : annexes 1.2 (sources et constats), 1.3 (chiffres de 2026, étude de Lyon-Est, tableau de bord actuel, usages, outils, témoignage de M. PRADELLE) et 1.1 (poids de la maintenance).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Étapes de la chaîne de valeur des données dans l'ordre (collecte, nettoyage et intégration, stockage et structuration, analyse, restitution, décision et action), chacune illustrée par le cas, et chaîne reliée à la décision stratégique (maintenance qui anticipe) | 0,5 |
| b-1 | Usage 1 → analyse **descriptive**, avec une limite tirée des annexes | 0,5 |
| b-2 | Usage 2 → analyse **exploratoire**, avec une limite tirée des annexes (corrélation et causalité, données manquantes) | 0,5 |
| b-3 | Usage 3 → analyse **prédictive**, avec une limite tirée des annexes (appareils non connectés, historique, fausses alertes, représentativité, explicabilité) | 0,5 |
| c-1 | Outil de visualisation recommandé et justifié par les besoins du cas, la BI étant présentée comme une démarche et non comme un outil | 0,5 |
| c-2 | Deux visualisations adaptées à leurs destinataires, chacune avec un indicateur complet (formule, source, fréquence, cible, axe) ; 0,5 par visualisation | 1 |

**Réponse indicative**

*1.3 a) – La chaîne de valeur des données du parc*

La chaîne de valeur des données est la suite des étapes qui transforment des données brutes en décisions et en actions ; la valeur se crée à chaque étape et se perd au maillon le plus faible. Appliquée au parc (0,5 pt pour les étapes illustrées) :

| Étape | Application à ALTIVERNE |
|---|---|
| Collecte | boîtiers des 31 000 appareils connectés, bons d'intervention des 1 500 techniciens, contrats, pièces ; saisie des 21 000 appareils non connectés |
| Nettoyage et intégration | rapprochement par l'identifiant commun, rattachement des 1 800 boîtiers, correction des codes panne, contrôle des dates de mise en service ; règles documentées dans le dictionnaire |
| Stockage et structuration | plateforme de données : référentiel des appareils, historique des données de fonctionnement au-delà des 13 mois du constructeur, données intégrées pour l'analyse |
| Analyse | descriptive, exploratoire et prédictive (question b) |
| Restitution | tableaux de bord de la direction et des agences, alertes sur mobile, rapports aux clients |
| Décision et action | programmer une visite avant la panne, affecter les techniciens, prioriser les modernisations, proposer des services aux clients |

La chaîne sert la stratégie : la maintenance représente 55 % d'un chiffre d'affaires de 590 M€ (environ 325 M€), et le plan vise 1,4 panne par appareil connecté en 2030 contre 2 en 2026.

*1.3 b) – Méthodes d'analyse et limites*

| Usage (annexe 1.3) | Méthode | Limite qui ressort des annexes |
|---|---|---|
| 1. Comprendre les pannes passées | **descriptive** : que s'est-il passé ? Agrégats, répartitions, évolutions, écarts à une cible, par agence et par type d'appareil | les causes sont illisibles quand 35 % des bons portent le code « autre » ; les appareils non connectés ne remontent qu'une fois par trimestre ; le tableau actuel compare des pannes en valeur absolue, sans rapport au nombre d'appareils de chaque agence (0,5 pt) |
| 2. Explorer les facteurs de panne | **exploratoire** : pourquoi ? Croisements, distributions, recherche de motifs et de valeurs atypiques entre pannes, âge, marque, usage, immeuble, signaux faibles | une corrélation n'est pas une causalité : les appareils connectés tombent moins en panne (2 contre 3 par an), mais 80 % d'entre eux ont moins de quinze ans contre 25 % des autres ; l'âge est un facteur commun, la connexion n'est pas en soi la cause ; la date de mise en service manque pour 30 % des appareils non connectés (0,5 pt) |
| 3. Prévoir les pannes | **prédictive** : que va-t-il se passer ? Estimation, pour chaque appareil connecté, du risque de panne à quinze jours ; le groupe n'a pas à construire le modèle mais à en apprécier la fiabilité | elle ne couvre que les 31 000 appareils connectés, les 21 000 autres restant hors de portée ; l'historique s'arrête à 13 mois alors que la direction souhaite cinq ans ; l'étude de Lyon-Est porte sur 1 200 appareils, moins de 4 % du parc connecté, avec des codes corrigés à la main ; les signaux faibles ne précèdent que 40 % des pannes : six pannes sur dix (1 440 sur 2 400) surviennent sans signal ; à l'inverse, ils ont été relevés 3 000 fois sans panne, contre au moins 960 fois avant une panne, soit jusqu'à trois signaux sur quatre sans suite : c'est le risque de fausses alertes que redoute M. PRADELLE, qui exige aussi une prévision explicable (0,5 pt) |

Conclusion : les trois méthodes se suivent ; la prévision ne vaudra que si la description et l'exploration ont d'abord fiabilisé les données et validé les facteurs.

*1.3 c) – Outil et visualisations*

Outil recommandé (0,5 pt) : l'**outil de visualisation** testé par la DSI, qui répond aux besoins exprimés : connexion à plusieurs sources (plateforme de données, interventions, contrats), rafraîchissement programmé au lieu d'une mise à jour à la main à J+15, consultation sur terminal mobile pour les responsables d'agence, droits d'accès par agence. Le tableur avancé reste utile pour des analyses ponctuelles, mais ses limites sont celles du tableau actuel : saisie manuelle, versions multiples, volumes, traçabilité. L'outil n'est qu'un maillon : sans référentiel des appareils, définitions partagées, formation des responsables d'agence et règles de diffusion, il afficherait plus vite les mêmes chiffres faux.

Deux visualisations (0,5 pt pour chacune, avec son indicateur complet) :

| Destinataire | Visualisation | Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|---|---|
| Directeur de la maintenance et des services | barres horizontales triées des 34 agences, appareils connectés et non connectés distingués, ligne de cible ; courbe d'évolution sur 24 mois pour l'ensemble du parc | Nombre de pannes par appareil et par an | pannes ayant donné lieu à un dépannage sur les douze derniers mois / appareils entretenus | logiciel des interventions rapproché du référentiel unique des appareils | mensuelle, sur douze mois glissants | 1,4 pour les appareils connectés en 2030 (2 en 2026), avec une trajectoire annuelle | processus |
| Responsable d'agence | liste des appareils en alerte classés par niveau de risque, sur carte du secteur, consultable sur mobile, avec une jauge du taux d'alertes confirmées | Taux d'alertes confirmées | alertes ayant donné lieu à une visite au cours de laquelle un défaut a été constaté / alertes ayant donné lieu à une visite | plateforme de données (alertes) et logiciel des interventions (constat du technicien) | hebdomadaire (chaque lundi) | au moins 50 % à la fin de 2028, alors qu'à Lyon-Est un signal sur quatre au moins précédait une panne | processus |

Les visualisations rapportent les pannes au nombre d'appareils, affichent la cible et distinguent les appareils connectés, à l'inverse du tableau actuel. L'indicateur des agences mesure la pertinence des alertes, et non le seul nombre de visites déclenchées : M. PRADELLE refuse d'envoyer ses techniciens sur de fausses alertes (annexe 1.3 F).

**Réponses tolérées**
- Analyse **diagnostique** citée entre descriptive et exploratoire, ou analyse **prescriptive** citée en prolongement de la prévision (affectation optimale des visites).
- Tableur avancé retenu pour une première phase, si le candidat en montre les limites et prévoit le passage à l'outil de visualisation.
- Autres indicateurs pertinents et complets : délai moyen d'arrivée du technicien par agence (cible 2 h 30 pour les appareils connectés, 4 h pour les autres en 2026), disponibilité moyenne des appareils (98,5 % en 2026).
- Indicateur de la seconde visualisation rattaché à l'axe client (disponibilité des appareils des clients).
- Taux d'alertes traitées à temps (alertes suivies d'une visite programmée dans les cinq jours / alertes émises) : accepté s'il est complet et si le candidat le complète par une mesure de la pertinence des alertes ; seul, il pousse à multiplier les visites sur de fausses alertes.

**Erreurs types**
- *BI réduite à un outil* (`JUR-D02`, `ET-05`) — « il suffit d'acheter l'outil de visualisation » ; juste : démarche qui suppose données fiables, gouvernance et compétences.
- *Chaîne de valeur incomplète* (`JUR-D01`) — oubli du nettoyage et de l'intégration, alors que c'est le maillon faible du cas ; juste : collecte, intégration, stockage, analyse, restitution, décision.
- *Corrélation présentée comme causalité* (`ET-26`) — « connecter les 21 000 appareils réduira leurs pannes d'un tiers » ; juste : l'âge des appareils explique au moins en partie l'écart.
- *Développement d'un modèle de prévision* — choix d'un algorithme ou description de son apprentissage ; juste : apprécier la fiabilité et les conditions d'usage de la prévision (limite du programme).
- *Indicateurs incomplets ou génériques* (`JUR-A02`, `ET-18`) — « nombre de pannes » sans formule, cible ni rapport au parc ; juste : cinq champs et cible tirée du plan.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne décisionnelle : collecte, intégration, entrepôt, restitution | étapes et maillons | F08 § 1 | notion de cours |
| Méthodes d'analyse descriptive, exploratoire, prédictive, prescriptive | association aux usages | F08 § 2 | notion de cours |
| Outils décisionnels, choix de la visualisation, corrélation et causalité | fonctions, limites, biais | F08 § 5 et 6 | notion de cours |

---

### 1.4 – Gouvernance, cycle de vie et valeur des données (3,5 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.a` « Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques » ; `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression » ; `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) » ; `2.3.f` « Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques ».

**Annexes mobilisées** : annexes 1.1 (organigramme), 1.2 (sources, conservation chez le constructeur, constats), 1.3 (besoin d'historique, prévision) et 1.4 (propositions, état des lieux de la propriété et de la conservation, repères).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance stratégique des données définie (cadre de décisions, de rôles, de règles et de contrôles qui traite les données comme un actif au service de la stratégie) | 0,5 |
| a-2 | Quatre principes (qualité, conformité, sécurité, valorisation) appliqués au cas, avec leur porteur ; le principe de qualité n'est compté qu'avec son indicateur (au moins formule et cible) ; 0,5 pour deux principes | 1 |
| b | Cycle de vie de la donnée de fonctionnement : cinq étapes, chacune avec une durée ou un événement déclencheur justifié par les annexes ; 0,5 pour trois étapes | 1 |
| c-1 | Données du parc qualifiées de patrimoine immatériel (valeur d'usage, valeur d'échange, rareté de l'historique, lien avec la stratégie) | 0,5 |
| c-2 | Trois risques pesant sur ce patrimoine, tirés des annexes | 0,5 |

**Réponse indicative**

*1.4 a) – Gouvernance stratégique et quatre principes*

La gouvernance stratégique des données est le cadre de décisions, de rôles, de règles et de contrôles par lequel la direction traite les données comme un actif de l'organisation : elle fixe qui décide de leur définition, de leur qualité, de leur accès, de leur partage et de leur valorisation, en cohérence avec la stratégie, sur tout leur cycle de vie (0,5 pt). Elle est portée au plus haut niveau, ici par un comité des données présidé par le directeur général, que le responsable de la transformation numérique anime ; les rôles (propriétaire, intendant, responsable des données) sont illustratifs et s'adaptent au groupe. Le DAMA-DMBOK peut en structurer les domaines.

| Principe | Application au cas | Porteur |
|---|---|---|
| **Qualité** : la donnée est corrigée à la source et mesurée | référentiel unique, liste de codes panne resserrée et utilisable sur mobile, date de mise en service obligatoire ; indicateur ci-dessous | propriétaire du domaine « appareils et interventions » : directeur de la maintenance et des services ; intendants dans les agences |
| **Conformité** : chaque usage a une finalité et un cadre | inscription au registre des traitements des enregistrements d'appels et des données des boîtiers ; durées de conservation fixées ; respect des droits d'accès des clients (Data Act) ; clauses sur les données dans les contrats de maintenance | délégué à la protection des données ; directeur commercial pour les contrats |
| **Sécurité** : accès selon le besoin et la sensibilité | classification des données (enregistrements vocaux sensibles, données de fonctionnement), droits par client et par agence, journalisation des accès, récupération des données chez le constructeur | DSI et responsable de la sécurité des systèmes d'information |
| **Valorisation** : tout partage ou toute vente de données est décidé par la direction, après analyse | grille d'examen des propositions (valeur, droits des clients, risques, éthique) ; catalogue des données disponibles | comité des données, présidé par le directeur général |

(0,5 pt pour deux principes appliqués avec leur porteur.)

Indicateur associé au principe de qualité :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de bons de dépannage portant un code panne précis | bons de dépannage dont le code panne n'est ni « autre » ni vide / bons de dépannage de la période | logiciel des interventions | mensuelle, par agence | au moins 95 % fin 2028 (65 % en 2026) | processus |

*1.4 b) – Cycle de vie d'une donnée de fonctionnement*

(1 pt pour les cinq étapes justifiées ; 0,5 pt pour trois.)

| Étape | Contenu | Durée ou événement déclencheur |
|---|---|---|
| Création | le boîtier mesure trajets, ouvertures de portes, durée des trajets, défauts | en continu, dès la mise en service du boîtier, rattachée à l'identifiant commun de l'appareil |
| Stockage | récupération en continu depuis la plateforme du constructeur vers la plateforme du groupe, en données détaillées puis en synthèses | données détaillées conservées cinq ans, durée demandée par M. PRADELLE pour la prévision, au lieu des 13 mois actuels |
| Usage | alertes, tableaux de bord, prévision, rapports aux clients, accès des clients | tant que l'appareil est sous contrat (cinq ans en moyenne, renouvelables) |
| Archivage | conservation d'une synthèse de l'historique (pannes, composants, modernisations), accès restreint | à la fin du contrat, ou au-delà de cinq ans pour les données détaillées : on ne garde qu'une synthèse, avec un accès restreint, tant que l'appareil reste dans le parc (environ 25 ans de vie), utile pour une modernisation ou un renouvellement du contrat |
| Suppression | effacement des données détaillées et de la synthèse, avec trace de la destruction | à la sortie de l'appareil du parc (environ 2 500 par an) : restitution au client s'il la demande, puis effacement ; à défaut, à l'expiration de la durée fixée dans le contrat |

Le cycle est fixé par la gouvernance et écrit dans les contrats de maintenance, aujourd'hui muets (annexe 1.4) ; les enregistrements vocaux, données à caractère personnel, relèvent d'une durée courte fondée sur leur finalité, distincte de celle des données de fonctionnement.

*1.4 c) – Patrimoine immatériel et risques*

Les données du parc constituent un **patrimoine immatériel** (0,5 pt) : actif non physique, accumulé dans le temps, qui procure une **valeur d'usage** (réduire les pannes de 2 à 1,4 par appareil connecté, programmer les visites des 1 500 techniciens, prioriser les modernisations, qui pèsent 25 % du chiffre d'affaires) et une **valeur d'échange** (services aux clients, partenariats de l'annexe 1.4) ; l'historique de 31 000 appareils connectés est rare et difficile à reproduire pour un concurrent ; sa valeur dépend de sa qualité, de sa durée et de son exploitation, non de son seul volume. Aucun traitement comptable n'est attendu.

Trois risques (0,5 pt), parmi :
- **perte** : l'historique détaillé est effacé après 13 mois par le constructeur, et une partie du parc ne vit que dans 34 tableurs envoyés par courriel ;
- **dépendance** : format propriétaire et extraction facturée par le constructeur des boîtiers ; demande d'exclusivité du fabricant de composants (P3) ;
- **fuite ou atteinte aux droits** : enregistrements d'appels conservés sans durée et absents du registre ; cession de données d'usage à des tiers (P2) ;
- **dégradation de la qualité** : 35 % de codes « autre », 1 800 boîtiers orphelins : un actif mal tenu perd sa valeur ;
- **perte de confiance des clients** : les bailleurs considèrent que « ce sont leurs données ».

**Réponses tolérées**
- Rôle de responsable des données (*Chief Data Officer*) confié au responsable de la transformation numérique, si le candidat ne le présente pas comme obligatoire.
- Durées différentes de celles du corrigé (trois ans de données détaillées, archivage limité à dix ans), si elles sont justifiées par les besoins de l'annexe 1.3 ou par l'état des lieux de l'annexe 1.4.
- Cycle de vie en sept étapes (collecte, stockage, traitement, partage, archivage, destruction…), si les cinq étapes du programme y figurent.
- Principe de conformité porté par le directeur administratif et financier pour les clauses contractuelles.

**Erreurs types**
- *Gouvernance réduite à la DSI ou à un outil* (`JUR-G10`) — « la DSI gère les données » ; juste : la gouvernance est stratégique, portée par la direction générale, avec des propriétaires métiers.
- *Organisation normative imposée* — un organigramme de gouvernance présenté comme obligatoire ; juste : les rôles sont illustratifs (limite du programme).
- *Cycle de vie sans durée ni déclencheur* — étapes récitées ; juste : chaque étape porte une durée ou un événement tiré des annexes.
- *Patrimoine immatériel traité comptablement* — valeur au bilan des données ; juste : valeur d'usage et d'échange et risques, sans traitement comptable, qui relève de l'UE 4.
- *DPO confondu avec le RSSI* (`ET-29`) — juste : le délégué à la protection des données conseille et contrôle la conformité, le responsable de la sécurité pilote la sécurité.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK (DAMA International), 2e édition, révision 2024 | domaines de la gestion des données autour de la gouvernance | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Gouvernance des données, rôles, cycle de vie, donnée comme actif | principes, étapes, risques | F07 § 8.1, 8.4 et 8.6 | notion de cours |
| Délégué à la protection des données, registre des traitements | conformité | F15 § 1 et 2 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | conservation limitée à la finalité ; registre | `rgpd` / F15 ; annexe 1.4 | en vigueur depuis le 25/05/2018 |

---

### 1.5 – Valorisation des données (2 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.e` « Aspects réglementaires (RGPD, archivage légal) et monétisation des données ».

**Annexes mobilisées** : annexes 1.4 (propositions, état des lieux, repères du RGPD, du Data Act et du Data Governance Act), 1.2 (demande des bailleurs) et 1.3 (prévision des pannes).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Monétisation des données définie (directe : vente, licence, service payant ; indirecte : amélioration des opérations et des offres), avec la nécessité d'une approche critique | 0,5 |
| 2 | Trois propositions évaluées au regard des repères (données personnelles, droits de l'utilisateur et du détenteur) et de leurs enjeux économiques et éthiques ; 0,5 pour deux | 1 |
| 3 | Recommandation justifiée et deux conditions de mise en œuvre | 0,5 |

**Réponse indicative**

La monétisation des données consiste à en tirer une valeur économique, soit **directement** (vente ou licence de jeux de données, service payant fondé sur les données), soit **indirectement** (amélioration des opérations, fidélisation, offres nouvelles) ; elle s'analyse de façon critique : droits des personnes et des clients, valeur réelle, risques de réputation et de dépendance (0,5 pt).

Évaluation (1 pt ; 0,5 pour deux propositions) :
- **P1 – Rapport de disponibilité** : données de fonctionnement non personnelles pour l'essentiel (à condition d'exclure le nom du technicien et les enregistrements d'appels) ; mais le Data Act donne aux clients, utilisateurs des appareils, le droit d'obtenir **sans frais** les données facilement accessibles de leurs appareils, ce que les bailleurs demandent déjà : le groupe ne peut pas faire payer l'accès aux données brutes, seulement un service à valeur ajoutée (analyses, comparaisons, prévisions). Économiquement : 0,9 M€ par an visés, fidélisation des grands comptes, cohérence avec le plan ; risque éthique faible si l'accès gratuit est garanti. Proposition favorable, sous conditions.
- **P2 – Cession de données d'usage** : des trajets par heure et par niveau desservi, rattachés à une adresse, peuvent révéler les habitudes des occupants d'un petit immeuble : ce ne sont pas des données anonymes, le RGPD s'appliquerait ; le Data Act interdit au détenteur de mettre ces données à disposition de tiers à d'autres fins que l'exécution du contrat avec l'utilisateur, ce qui supposerait l'accord contractuel de chaque client ; l'assureur pourrait s'en servir pour tarifer les immeubles des clients du groupe, conflit d'intérêts et risque de réputation majeurs ; 150 000 € par an, moins de 0,1 % du chiffre d'affaires de maintenance. L'intermédiaire devrait respecter les conditions du Data Governance Act (neutralité, personne morale distincte), ce qui ne lève aucune des objections. Proposition à écarter.
- **P3 – Partenariat avec le fabricant** : données de fonctionnement des 9 000 appareils équipés, non personnelles ; mais leur transmission à un tiers suppose un contrat avec les clients (Data Act) ; gain de 200 000 € par an (8 % de 2,5 M€) et accès à des analyses de défaillance utiles à la prévision ; l'exclusivité et le droit de réutilisation libre créent une dépendance et livrent le savoir-faire du groupe à un fournisseur qui pourrait l'utiliser ailleurs. Proposition intéressante à renégocier : sans exclusivité, réutilisation limitée à l'amélioration des produits, durée limitée, réciprocité.

Recommandation (0,5 pt) : **P1**, la plus alignée sur le plan « ALTIVERNE 2030 » (nouveaux services fondés sur les données) et sur la demande des clients, au risque juridique et éthique le plus faible. Deux conditions, parmi : garantir aux clients l'accès gratuit aux données brutes de leurs appareils (API de la question 1.2) et ne facturer que le service à valeur ajoutée ; inscrire dans les contrats de maintenance des clauses sur l'usage, le partage et la conservation des données ; fiabiliser auparavant les données (référentiel unique, rattachement des boîtiers), un rapport erroné vendu à un client étant pire que pas de rapport ; exclure les données à caractère personnel et faire valider l'offre par le délégué à la protection des données.

**Réponses tolérées**
- Recommandation de **P3** renégociée, si le candidat montre son apport à la maintenance qui anticipe et lève l'exclusivité et la réutilisation libre.
- Recommandation de P1 et P3 ensemble, P2 étant écartée, si les conditions de chacune sont précisées.
- P2 jugée envisageable sur des données réellement agrégées à grande échelle (par département, sans adresse), avec l'accord contractuel des clients, à condition d'en montrer les limites éthiques.

**Erreurs types**
- *Monétisation sans regard critique* — « les données sont un gisement : vendons-les au plus offrant » ; juste : droits des clients, données personnelles, réputation et dépendance mis en regard du gain (limite du programme).
- *« Les données appartiennent au groupe »* — le groupe, détenteur, n'en dispose pas librement : le client utilisateur a des droits d'accès et de partage, et l'usage des données suppose un contrat (Data Act) ; les données d'usage rattachées à une adresse peuvent être personnelles (RGPD).
- *Pseudonymisation confondue avec l'anonymisation* — retirer le nom du client ne suffit pas quand l'adresse et les heures de trajet permettent d'identifier des personnes.
- *Analyse juridique approfondie* (`JUR-T07`) — articles et contentieux développés ; juste : appliquer les repères de l'annexe 1.4 au cas, sans aller au-delà.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2023/2854 (Data Act) | accès sans frais de l'utilisateur, partage avec un tiers, usage par le détenteur sur la base d'un contrat ; conception des produits mis sur le marché après le 12/09/2026 | `data_act` / F07 § 8.5 ; annexe 1.4 | applicable depuis le 12/09/2025 |
| Règlement (UE) 2016/679 (RGPD) | donnée identifiable indirectement, pseudonymisation et anonymisation | `rgpd` / F07 § 8.6 ; annexe 1.4 | en vigueur depuis le 25/05/2018 |
| Règlement (UE) 2022/868 (Data Governance Act) | conditions imposées aux services d'intermédiation de données | `dga` ; annexe 1.4 | applicable depuis le 24/09/2023 |
| Monétisation des données, approche critique | modèles directs et indirects, limites | F07 § 8.6 | notion de cours |
