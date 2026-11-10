# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 3

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Organiser, analyser et valoriser les données des appareils connectés | 14 | 1.1 à 1.5 | `exercices/ex07_donnees_appareils_connectes` |
| 2 – Fiabiliser le système d'information financier et évaluer l'apport des nouvelles technologies | 14 | 2.1 à 2.5 | `exercices/ex08_fiabilite_si_financier_cryptoactifs` |
| 3 – Inscrire le système d'information dans la démarche de durabilité et capitaliser les savoir-faire | 12 | 3.1 à 3.4 | `exercices/ex09_durabilite_si_savoir_faire` |
| **Total** | **40** | | |

---

## DOSSIER 1 – ORGANISER, ANALYSER ET VALORISER LES DONNÉES DES APPAREILS CONNECTÉS (14 points)

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

---

## DOSSIER 2 – FIABILISER LE SYSTÈME D'INFORMATION FINANCIER ET ÉVALUER L'APPORT DES NOUVELLES TECHNOLOGIES (14 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Fiabilité des données comptables et décisionnelles | `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers | 3 |
| 2.2 Facturation électronique et architecture du SI financier | `1.3.a` Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) ; `1.3.e` Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers ; `1.3.b` Cartographie applicative et fonctionnelle des SI ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) | 3 |
| 2.3 Intelligence artificielle et prévention des fraudes | `4.1.f` Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques ; `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA | 2 |
| 2.4 Sécurisation du contrat avec l'ESN | `1.4.a` Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques ; `1.4.b` Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle ; `1.4.c` Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD ; `1.4.d` Méthodologie de négociation contractuelle et analyse des risques ; `1.4.e` Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) | 3 |
| 2.5 Blockchain et crypto-actifs : trois propositions | `3.3.a` Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations ; `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.d` Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain | 3 |
| **Dossier 2 – Fiabiliser le système d'information financier et évaluer l'apport des nouvelles technologies** |  | **14** |

Répartition indicative : connaissances (définitions de la fiabilité d'un SI comptable et décisionnel, du principe de la détection d'anomalies par apprentissage automatique, du contrat au forfait et de la blockchain : items 2.1 a-1, 2.3-1, 2.4 a-1 et 2.5 a-1) 2 points ; analyse des annexes et recommandations 12 points. Durée conseillée : 14 points × 4,5 minutes ≈ 1 h 03.

---

### 2.1 – Fiabilité des données comptables et décisionnelles (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ».

**Annexes mobilisées** : annexes 1.1 (organisation, plan « ALTIVERNE 2030 ») et 2.1 (note du directeur administratif et financier, incidents, remarques des auditeurs externes).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fiabilité d'un SI comptable et décisionnel définie (exhaustivité, exactitude, réalité et autorisation, rattachement à la bonne période, cohérence, traçabilité, disponibilité à temps) | 0,5 |
| a-2 | Quatre risques distincts, chacun étayé par un fait chiffré de l'annexe 2.1 (0,5 par paire de risques) | 1 |
| b-1 | Quatre mesures, une par famille imposée, chacune reliée explicitement à un risque identifié (0,5 par paire de mesures) | 1 |
| b-2 | Un indicateur complet (formule, source, fréquence, cible, axe) attaché à l'une des mesures | 0,5 |

**Réponse indicative**

*2.1 a) – Définition et risques*

Un système d'information comptable et décisionnel est fiable lorsque les données qu'il produit sont **exhaustives** (toutes les opérations sont enregistrées, une seule fois), **exactes** (montants, tiers, comptes), **réelles et autorisées** (elles correspondent à des opérations validées par une personne habilitée), **rattachées à la bonne période**, **cohérentes** d'une application à l'autre et **traçables** : une piste d'audit permet de remonter de la pièce justificative au solde et au tableau de bord, et inversement. Pour un groupe qui veut des « processus financiers fiabilisés » (plan « ALTIVERNE 2030 »), la fiabilité tient autant aux contrôles intégrés au SI qu'à l'organisation des tâches (0,5 pt).

Quatre risques parmi les suivants, chacun étayé (1 pt, 0,5 par paire) :

| Risque | Faits de l'annexe 2.1 |
|---|---|
| R1 – Paiements frauduleux ou non autorisés | une même comptable modifie les coordonnées bancaires des fournisseurs et prépare les campagnes de virements ; validation globale de campagnes d'environ 1 200 virements sans liste des coordonnées modifiées ; aucun contre-appel ; 350 000 € virés vers le compte frauduleux, 100 000 € récupérés, soit 250 000 € perdus ; 14 personnes ayant des droits d'administration du PGI et 30 comptes d'anciens salariés actifs |
| R2 – Chiffre d'affaires de maintenance incomplet ou inexact | avenants transmis par courriel une fois par mois ; 600 contrats facturés après leur résiliation (0,9 M€ d'avoirs) et 400 appareils jamais facturés (0,6 M€ par an) ; ressaisie des interventions hors contrat : 1 500 avoirs de correction ; environ 3 000 factures encore établies sur papier en agence |
| R3 – Dettes fournisseurs et charges inexactes (doublons) | réception par trois canaux (plateforme, courriel, courrier) et ressaisie de la plupart des 90 000 factures ; 220 factures payées deux fois (0,4 M€) ; aucun rapprochement de la facture avec la commande et la réception |
| R4 – Intégrité des interfaces et du paramétrage, piste d'audit rompue | fichier d'interface des bons d'intervention modifiable avant intégration, sans nombre de lignes ni total de contrôle, contrôlé à l'œil ; modifications du paramétrage (conditions de paiement, taux de TVA) faites en production par le prestataire, sans trace ni validation : une erreur de paramétrage se répercute sur toutes les factures |
| R5 – Information décisionnelle peu fiable et tardive | reporting du chiffre d'affaires de maintenance établi sur tableur, avec un écart inexpliqué d'environ 2 % avec la comptabilité ; comptes des filiales remontés par tableur ; clôture mensuelle à J+12 pour une cible de J+5 ; comptes 2026 arrêtés avec quatre semaines de retard |

*2.1 b) – Quatre mesures de fiabilisation et un indicateur*

| Famille | Mesure proposée à ALTIVERNE | Risque traité |
|---|---|---|
| Contrôles applicatifs | contrôles bloquants à la saisie et avant paiement : unicité du couple fournisseur / numéro de facture / montant ; rapprochement automatique de la facture avec la commande et la réception des pièces avant mise en paiement ; blocage de tout paiement vers des coordonnées bancaires modifiées depuis moins de trente jours tant qu'elles n'ont pas été confirmées | R3, R1 |
| Séparation des tâches | matrice des rôles : la création et la modification des fiches fournisseurs et des coordonnées bancaires sont confiées à une cellule « référentiel des tiers » distincte des comptables qui préparent les virements ; contre-appel du fournisseur à un numéro déjà connu, et non à celui du courriel ; liste des coordonnées modifiées jointe à chaque campagne soumise au directeur administratif et financier ; retrait des 14 droits d'administration, désactivation des 30 comptes d'anciens salariés, revue semestrielle des habilitations | R1 |
| Traçabilité | journalisation des modifications des fiches tiers et du paramétrage (auteur, date, ancienne et nouvelle valeur) ; gestion des changements : demande écrite, essai dans un environnement de recette, validation par la direction financière, mise en production par une autre personne que l'auteur ; piste d'audit fiable de la facture au paiement | R4 |
| Interfaces automatisées et rapprochements | interface automatisée entre le logiciel des interventions et le PGI, avec nombre de bons et total de contrôle, rejets tracés et traités sous 24 heures, suppression des ressaisies et des carnets papier ; saisie des avenants en agence dans un circuit de validation du PGI ; rapprochement mensuel automatique des contrats actifs, des appareils et des factures ; rapprochement bancaire automatique ; reporting alimenté par le PGI, seule source du chiffre d'affaires | R2, R5 |

Indicateur (0,5 pt), un parmi :

| Axe | Indicateur | Formule | Source | Fréquence | Cible |
|---|---|---|---|---|---|
| Processus | Changements de coordonnées bancaires vérifiés | changements de coordonnées bancaires confirmés par contre-appel et validés par une seconde personne avant tout paiement / changements de coordonnées bancaires enregistrés | journal des modifications des fiches fournisseurs du PGI | mensuelle | 100 % dès juin 2027 |
| Processus | Intégration automatique des factures fournisseurs | factures fournisseurs intégrées dans le PGI sans ressaisie / factures fournisseurs reçues | PGI et plateforme agréée | mensuelle | au moins 90 % fin 2027 (aucune aujourd'hui : depuis septembre 2026, 30 % des factures arrivent par la plateforme, toutes ressaisies) |
| Financier | Écarts entre contrats actifs et facturation | nombre d'écarts constatés au rapprochement (contrats résiliés encore facturés + appareils ajoutés par avenant non facturés) | rapprochement mensuel du PGI (contrats et factures) | trimestrielle | 0 écart fin 2027 (1 000 écarts en novembre 2026 : 600 contrats résiliés encore facturés et 400 appareils non facturés) |

Priorité : la séparation des tâches sur les coordonnées bancaires et la mise en paiement, qui ne coûte presque rien et traite le risque qui a déjà coûté 250 000 €, puis les contrôles applicatifs et l'interface, à livrer avant le 1er septembre 2027.

**Réponses tolérées**
- Risques formulés selon les assertions de l'audit (exhaustivité, réalité, exactitude, séparation des exercices) ou selon la typologie des risques du SI (défaillances opérationnelles, risque de fraude, risque réglementaire), dès lors qu'ils sont étayés par l'annexe 2.1.
- Mesures réparties autrement entre les quatre familles (par exemple le contrôle de doublon classé en rapprochement), si chacune des familles imposées est couverte et reliée à un risque.
- Référence au COSO 2013 (activités de contrôle, contrôles généraux informatiques) ou à COBIT 2019 en appui, sans développement.
- Tout autre indicateur complet et contextualisé (délai de clôture mensuelle, cible J+5 ; nombre de factures payées en double, cible 0).

**Erreurs fréquentes**
- *Risques énumérés sans lien avec le cas* (`JUR-T01`, `ET-39`) — liste générique (« risque de fraude, risque d'erreur ») ; juste : chaque risque appuyé sur un fait et un chiffre de l'annexe 2.1.
- *Fiabilisation réduite à l'outil* (`JUR-T12`) — « changer de PGI » ; juste : contrôles applicatifs, organisation des tâches, habilitations et traçabilité, dans le PGI existant.
- *Dérive vers l'audit des comptes* (`ET-34`) — écritures de correction, provisions, appréciation des comptes 2026 ; juste : l'UE 5 traite les processus et les contrôles du SI qui produisent les données.
- *Indicateur incomplet* (`JUR-A02`, `ET-18`) — « taux de fraude » sans formule, source ni cible ; juste : cinq champs renseignés et reliés à la mesure.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Fiabilisation des SI comptables et décisionnels | séparation des tâches, piste d'audit, contrôles applicatifs, interfaces, SI décisionnel | F10 § 2 et 3 | guide p. 266-267 et 307 |
| Contrôles généraux informatiques (accès, changements, exploitation) | remarques des auditeurs externes | `nep_315` ; F10 § 1.3 | en vigueur (arrêté du 13/11/2024) |

---

### 2.2 – Facturation électronique et architecture du SI financier (3 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.a` « Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) » ; `1.3.e` « Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers » ; `1.3.b` « Cartographie applicative et fonctionnelle des SI ».
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) » (rôle de la plateforme agréée et des formats Factur-X, UBL et CII, seulement nommés).

**Annexes mobilisées** : annexes 1.1 (filiales), 2.1 (outils, volumes, facturation électronique et ses repères datés) et 2.2 (périmètre du projet, module de détection).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Impacts organisationnels, distingués entre comptabilité fournisseurs et facturation des clients | 0,5 |
| a-2 | Impacts juridiques, appuyés sur le calendrier de l'annexe 2.1 (ETI émettrice depuis le 01/09/2026 ; fournisseurs PME au 01/09/2027) | 0,5 |
| a-3 | Impacts comptables (processus et qualité de l'information, sans écriture) | 0,5 |
| b-1 | Schéma lisible : composants demandés, zones de la cartographie, flux structurés et contrôles | 1 |
| b-2 | Deux règles d'urbanisation justifiées par le cas | 0,5 |

**Réponse indicative**

*2.2 a) – Impacts du passage à la facturation électronique*

| Impact | Comptabilité fournisseurs | Facturation des clients |
|---|---|---|
| Organisationnel (0,5 pt) | les 18 comptables passent de la ressaisie (environ 5 000 factures chacune par an) au contrôle des anomalies, au traitement des rejets et des litiges et à la relation avec les fournisseurs ; un circuit d'approbation (« bon à payer ») associe les acheteurs, l'usine et les agences qui ont reçu les pièces ; les statuts de traitement renvoyés par la plateforme (reçue, refusée, approuvée, payée) sont attribués à des responsables ; pic de charge à partir du 1er septembre 2027, quand les 4 800 PME et micro-entreprises fournisseurs, 80 % des fournisseurs, émettront à leur tour ; formation et conduite du changement, que le contrat de LUMIGRÈS exclut | fin des carnets de factures en agence : les interventions hors contrat sont facturées depuis le PGI ou le logiciel des interventions ; les assistantes d'agence cessent la ressaisie ; l'annuaire impose de tenir à jour l'identification et l'adresse de facturation électronique de chaque client (bailleurs, syndics, établissements) ; le service de facturation suit les factures refusées par les clients |
| Juridique (0,5 pt) | la réception électronique est obligatoire pour toutes les entreprises depuis le 01/09/2026 : la société mère la respecte techniquement, mais télécharge en PDF puis ressaisit les factures, ce qui fait perdre l'intérêt et la traçabilité du flux électronique ; à partir du 01/09/2027, la quasi-totalité des factures arrivera par la plateforme ; la plateforme agréée, souscrite dans l'urgence, est un prestataire critique : contrat à revoir (niveaux de service, sécurité, réversibilité) | entreprise de taille intermédiaire, la société mère doit **émettre** ses factures électroniques par une plateforme agréée depuis le 01/09/2026 : parmi les quelque 3 000 factures papier des agences, celles adressées à des clients assujettis ne sont pas conformes ; pour les clients non assujettis (syndicats de copropriétaires, par exemple), les données de l'opération relèvent du e-reporting, que les carnets papier ne permettent pas davantage ; les opérations internationales (clients étrangers) relèvent du e-reporting par la plateforme ; les filiales relèvent de leur propre droit (annexe 2.1) |
| Comptable (0,5 pt) | factures reçues en données structurées : intégration automatique, pré-imputation, rapprochement avec la commande et la réception, canal unique qui supprime les doublons nés de la réception par courriel et par courrier (220 doublons en 2026) ; piste d'audit de bout en bout, horodatée ; dettes fournisseurs plus fiables et clôture accélérée (cible J+5) | factures émises en données structurées et suivies par statut : chiffre d'affaires et créances plus fiables, relances fondées sur des statuts, rapprochement des encaissements facilité ; facture électronique conservée comme original |

*2.2 b) – Architecture cible et cartographie urbanisée*

Schéma attendu (1 pt), format libre ; exemple :

```
ZONE PILOTAGE        Reporting et tableaux de bord de la direction financière  <—  PGI (source unique)
                     Consolidation : comptes des filiales belge et suisse remontés dans un plan de comptes commun
                     Module de détection des anomalies (lecture seule) —> alertes —> cellule de contrôle (décision humaine)
                                    ^ lit fiches tiers, factures, paiements
ZONE RÉFÉRENTIELS    Référentiel des tiers (clients, fournisseurs, coordonnées bancaires), contrats et appareils, plan de comptes
                     un seul propriétaire par référentiel ; modifications par circuit de validation
ZONE GESTION         PGI : achats, comptabilité fournisseurs et clients, facturation, trésorerie
ZONE OPÉRATIONS      Logiciel des interventions (bons des techniciens)  —> bons valorisés —>  PGI
ZONE ÉCHANGES        Couche d'intégration : interfaces automatisées avec totaux de contrôle et rejets tracés
                     <—> Plateforme agréée (Factur-X, UBL ou CII) <—> fournisseurs et clients ; statuts de traitement —> PGI
                         Plateforme agréée —> administration (e-reporting ; annuaire et concentration des données par le portail public)
                     <—> Banque : fichiers de virements validés —> ; <— relevés pour le rapprochement automatique
                     <—  Logiciels comptables des filiales (remontée normalisée)
```

Deux règles d'urbanisation, justifiées (0,5 pt) parmi :
- **un référentiel unique par donnée, avec un propriétaire** : les fiches fournisseurs et leurs coordonnées bancaires n'existent qu'à un endroit, modifiées par une seule cellule selon un circuit de validation ; c'est la réponse architecturale à la fraude d'octobre 2026 et la condition d'une détection fiable ;
- **des échanges par une zone d'échange maîtrisée**, et non par des fichiers modifiables d'application à application : interfaces automatisées avec contrôle de complétude, statuts et rejets tracés ; cela supprime les ressaisies et les fichiers sans total de contrôle relevés par les auditeurs ;
- **le découplage des blocs** : le module d'IA lit les données du PGI sans les modifier et peut être remplacé sans toucher à la comptabilité, ce qui limite la dépendance à LUMIGRÈS ;
- **une fonction implantée une seule fois** : toute la facturation passe par le PGI et la plateforme, plus de carnets d'agence ni de reporting parallèle sur tableur.

Cette cartographie relève de l'urbanisation, démarche stratégique qui organise le SI en blocs cohérents au service des processus financiers du plan « ALTIVERNE 2030 », et non d'un inventaire des logiciels.

**Réponses tolérées**
- Schéma en couches (métier, fonctionnelle, applicative, technique) ou en blocs, avec ou sans le vocabulaire zones, quartiers et îlots, s'il fait apparaître les flux et les contrôles.
- Module d'IA placé dans une zone « contrôle et conformité » ou dans la zone de gestion, s'il est présenté en lecture seule et relié à une décision humaine.
- Proposition d'étendre à terme le PGI ou un plan de comptes commun aux filiales, présentée comme une étape ultérieure.
- Impacts présentés en texte plutôt qu'en tableau, si les deux processus et les trois natures d'impact sont couverts.
- Distinction entre clients assujettis (facturation électronique) et non assujettis (e-reporting), si la conclusion sur les carnets papier est tirée.

**Erreurs fréquentes**
- *Urbanisation réduite à un inventaire technique* (`ET-20`, `JUR-G07`) — liste de serveurs et de logiciels ; juste : zones fonctionnelles, référentiels, flux et règles d'urbanisme au service des processus.
- *Calendrier faux ou vocabulaire périmé* (`ET-41`, `JUR-N02`) — écrire que l'émission ne concerne le groupe qu'en 2027, employer l'ancienne appellation des plateformes ou faire du portail public la plateforme d'échange ; juste : ETI émettrice depuis le 01/09/2026, plateformes agréées, portail public limité à l'annuaire et à la concentration des données.
- *Impacts comptables traités comme une question de régularité des comptes* (`ET-34`) — écritures, TVA détaillée ; juste : processus comptables (intégration, rapprochement, piste d'audit, délais de clôture).
- *Format de facture détaillé* (`JUR-T07`) — description de la structure d'un fichier ; juste : les formats sont seulement nommés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Généralisation de la facturation électronique (art. 91 de la loi de finances pour 2024) | calendrier 01/09/2026 et 01/09/2027, formats, e-reporting | `facturation_electronique_fr` ; F10 § 3.4 | en vigueur ; émission des PME et micro-entreprises applicable le 01/09/2027 [S] |
| Plateformes agréées ; portail public de facturation | plateforme d'échange, annuaire, concentrateur | `facturation_electronique_pa` ; F10 § 3.4 | en vigueur [S] |
| Urbanisation, cartographies, règles d'urbanisme | zones, référentiels uniques, zone d'échange, découplage | F03 § 1 et 2 | — |

---

### 2.3 – Intelligence artificielle et prévention des fraudes (2 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.f` « Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques » ; `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ».

**Annexes mobilisées** : annexes 2.1 (incidents, volumes, effectif de la comptabilité fournisseurs) et 2.2 (module et démonstration, clauses 3 et 7).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Principe présenté : apprentissage à partir de l'historique, score d'écart au comportement habituel, alerte au-delà d'un seuil ; distinction avec des règles fixes | 0,5 |
| 2 | Deux apports appliqués aux anomalies de l'annexe 2.1 | 0,5 |
| 3 | Trois limites appuyées sur la démonstration (faux positifs, explicabilité, qualité des données d'apprentissage ; faux négatifs ou dépendance acceptés) | 0,5 |
| 4 | Conditions de la supervision humaine (qui décide, seuils, traçabilité, revue des performances) | 0,5 |

**Réponse indicative**

La détection d'anomalies par apprentissage automatique consiste à faire apprendre à un modèle, à partir de l'historique (ici les factures, les fiches fournisseurs et les paiements de 2024 à 2026), ce qu'est une opération habituelle, puis à attribuer à chaque opération nouvelle un **score** qui mesure son écart à ce comportement ; au-delà d'un **seuil**, une alerte est émise. L'apprentissage peut être non supervisé (repérer ce qui s'écarte de la norme) ou supervisé (apprendre à partir de cas déjà qualifiés de fraude ou de doublon). À la différence d'un contrôle par règles fixes (« bloquer deux factures de même numéro »), le modèle repère des combinaisons inhabituelles qu'aucune règle n'a prévues ; il produit une probabilité, non une décision (0,5 pt).

Deux apports parmi (0,5 pt) :
- **l'exhaustivité** : le module examine toutes les opérations, environ 90 000 factures et près de 29 000 virements par an, quand le directeur administratif et financier valide des campagnes de 1 200 virements sans les détailler ;
- **la prévention avant le paiement** : lors de la démonstration, le module a signalé le changement de coordonnées bancaires frauduleux d'octobre, qui a coûté 250 000 €, et 150 des 220 doublons ; utilisé avant chaque campagne, il aurait permis de suspendre ces paiements ;
- **la détection de schémas combinés** : coordonnées modifiées récemment, montant inhabituel, demande pressante, bénéficiaire nouveau, que des règles simples ne croisent pas ;
- **la libération de temps** : les comptables concentrent leurs contrôles sur les opérations les plus risquées.

Trois limites parmi (0,5 pt) :
- **les faux positifs** : 6 000 alertes sur l'année, soit 500 par mois et près de 28 par comptable fournisseurs, pour 151 anomalies réelles (le changement de coordonnées frauduleux et 150 doublons), soit à peine 2,5 % des alertes, les 5 849 autres s'étant révélées sans fondement ; au-delà, la lassitude conduit à ignorer les alertes, y compris les vraies ;
- **l'explicabilité** : le module « ne fournit pas de justification détaillée de chaque score » ; or il faudra justifier la suspension d'un paiement auprès d'un fournisseur et documenter les contrôles auprès des auditeurs externes ;
- **la qualité des données d'apprentissage** : l'historique n'a pas été nettoyé ; les doublons non corrigés et les fournisseurs créés deux fois risquent d'être appris comme « normaux » (biais), ce que confirme la détection de 150 doublons seulement sur 220 ;
- **les faux négatifs** : 70 doublons non signalés ; le module ne remplace pas les contrôles bloquants d'unicité ni la séparation des tâches de la question 2.1 ;
- **la dépendance** : seuils réglés par LUMIGRÈS et règles apprises sur les données d'ALTIVERNE restant sa propriété (clauses 3 et 7).

Conditions de la supervision humaine (0,5 pt) :
- l'IA alerte, une personne décide : toute suspension ou libération d'un paiement signalé est décidée par une cellule de contrôle distincte des comptables qui préparent les virements, jamais automatiquement ;
- les seuils sont fixés et révisés par la direction financière d'ALTIVERNE, non par l'ESN, pour ramener les alertes à un volume traitable ;
- chaque alerte et la décision prise sont journalisées ; les alertes qualifiées (vraie anomalie ou fausse alerte) sont réinjectées pour améliorer le modèle ;
- une revue trimestrielle des performances (alertes confirmées, anomalies découvertes après coup) est présentée au directeur administratif et financier ; les utilisateurs sont formés à l'interprétation des scores.

Indicateur possible de cette supervision (valorisé, non exigé) : précision des alertes = alertes confirmées comme anomalies / alertes examinées ; source : journal des alertes et des décisions ; fréquence mensuelle ; cible : au moins 20 % à fin 2027, contre environ 2,5 % lors de la démonstration ; axe processus.

**Réponses tolérées**
- Présentation du module comme apprentissage supervisé ou non supervisé, si le principe du score et du seuil est exact.
- Apports formulés en termes de rapidité de détection ou de couverture des trois familles d'anomalies, s'ils sont appliqués au cas.
- Mention des biais ou de la protection des données personnelles des fournisseurs entrepreneurs individuels comme limite, si elle est reliée au cas.

**Erreurs fréquentes**
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — le module « rédige » ou « converse » ; juste : modèle qui classe et attribue un score à partir de données structurées.
- *Apports sans limites* (`ET-19`) — l'IA « supprime la fraude » ; juste : gains réels, mais faux positifs, explicabilité, qualité des données et supervision humaine.
- *IA décrite comme un outil technique* (`JUR-T12`) — architecture interne du modèle, choix d'un algorithme ; juste : effets sur le métier de la comptabilité fournisseurs et sur le contrôle interne.
- *Hors sujet réglementaire* (`JUR-T07`) — qualification du module au regard du règlement sur l'intelligence artificielle : non demandée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Apprentissage automatique et IA générative ; détection de fraude ; risques (biais, explicabilité, dépendance) ; gouvernance et supervision humaine | principe, apports et limites | F13 § 1 à 4 | guide p. 336 et 354-355 |

---

### 2.4 – Sécurisation du contrat avec l'ESN (3 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.a` « Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques » ; `1.4.b` « Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle » ; `1.4.c` « Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD » ; `1.4.d` « Méthodologie de négociation contractuelle et analyse des risques » ; `1.4.e` « Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) ».

**Annexes mobilisées** : annexes 2.1 (échéance du 01/09/2027, données financières) et 2.2 (offre, module, clauses, témoignage de la DSI).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Contrat au forfait caractérisé (livrables définis, prix et délai fixés, engagement de résultat, risque porté par le prestataire), et contradiction relevée avec les clauses 2 à 5 | 0,5 |
| a-2 | Trois clauses à renégocier ou à ajouter, chacune justifiée par le cas et assortie d'une formulation de principe (0,5 par clause) | 1,5 |
| b-1 | Instance de pilotage adaptée (composition, fréquence, objet) | 0,5 |
| b-2 | Indicateur de suivi complet (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse indicative**

*2.4 a) – Caractérisation du contrat et clauses à renégocier*

Le contrat proposé est un **contrat d'intégration au forfait** : l'ESN s'engage à livrer des résultats définis (raccordement à la plateforme, interface, module) pour un prix (900 000 €) et une date fixés à l'avance ; c'est en principe un engagement de résultat, et le risque de dépassement pèse sur le prestataire. Il s'y ajoute un abonnement au module (100 000 € par an) et une maintenance corrective (60 000 € par an), soit environ 1,38 M€ sur trois ans. Or les clauses 2 à 5 vident le forfait de sa substance : simples « meilleurs efforts » sur la date, aucun résultat garanti pour le module, recette tacite et pénalités symboliques ; le risque revient à ALTIVERNE (0,5 pt).

Trois clauses parmi les suivantes (1,5 pt, 0,5 par clause justifiée et reformulée) :

| Clause | Pourquoi la renégocier ou l'ajouter | Formulation de principe |
|---|---|---|
| 2 et 5 – Délais et pénalités | le 1er septembre 2027 est une échéance réglementaire et opérationnelle : les 4 800 PME fournisseurs émettront par la plateforme et les 18 comptables ne pourront plus ressaisir ; « meilleurs efforts » et une pénalité plafonnée à 9 000 €, soit 1 % du prix ou six semaines de retard, ne protègent pas | date ferme de mise en service, avec jalons intermédiaires (réception automatique, émission, interface) et essais de bout en bout avant l'été ; obligations d'ALTIVERNE (disponibilités, données) listées précisément ; pénalités proportionnées au préjudice et plafond relevé, par exemple 10 % du prix |
| 4 – Recette | une recette réputée acquise en dix jours et une mise en production qui « vaut recette » interdisent de vérifier l'interface sur des données réelles, alors que les fichiers d'interface actuels sont déjà une source d'erreurs | cahier de recette validé par ALTIVERNE, essais sur des données réelles d'un mois complet, procès-verbal signé par la direction financière et la DSI, réserves bloquantes et non bloquantes, période de vérification de bon fonctionnement couvrant une clôture mensuelle |
| 3 – Résultats du module d'IA | sans objectif mesurable ni maîtrise des seuils, ALTIVERNE paie 250 000 € et 100 000 € par an pour 500 alertes par mois sans garantie | objectifs mesurés à l'issue d'une période d'apprentissage sur un jeu d'essai (part des doublons et des changements de coordonnées frauduleux détectés, nombre maximal d'alertes par mois), seuils fixés par ALTIVERNE, motifs principaux de chaque alerte restitués, nettoyage préalable de l'historique inclus au périmètre |
| 7 – Propriété des développements et des paramétrages | les interfaces sont spécifiques à ALTIVERNE et les règles apprises le sont sur ses propres données : laissées à LUMIGRÈS, elles empêchent de changer de prestataire | développements spécifiques cédés à ALTIVERNE (ou licence permanente), paramétrages, seuils et documentation appartenant à ALTIVERNE, code source accessible (dépôt chez un tiers) |
| 8 – Accès aux données (et clause de sécurité à ajouter) | factures, coordonnées bancaires et paiements sont des données confidentielles, dont certaines à caractère personnel (fournisseurs entrepreneurs individuels) ; réutilisation pour d'autres clients et hébergement de localisation inconnue | interdiction de toute réutilisation ; accord de sous-traitance des données personnelles (instructions, sécurité, sous-traitants ultérieurs autorisés, sort des données en fin de contrat) ; hébergement dans l'Union européenne ; engagements de sécurité et notification des incidents ; clause d'audit |
| 10 – Durée et sortie (réversibilité à ajouter) | tacite reconduction, prix révisable par la seule ESN et restitution dans un format propriétaire, sans assistance : dépendance totale | plan de réversibilité : restitution des données, des paramétrages et de l'historique des alertes dans un format ouvert et documenté, assistance au transfert vers un autre prestataire, délais et coût fixés ; révision de prix encadrée ; préavis de non-reconduction |
| 1 – Périmètre (formation à ajouter) | la formation des comptables et des agences est exclue alors que le métier change (question 2.2) ; la reprise des données antérieures à 2024 n'est pas prévue | formation et accompagnement inclus ; option chiffrée pour les filiales ; procédure de demande de changement avec chiffrage préalable |

Les clauses 6 (maintenance corrective) et 9 (comité mensuel) sont acceptables, la seconde à compléter (question b).

*2.4 b) – Pilotage de la relation*

Instance (0,5 pt) : un **comité de pilotage** mensuel, hebdomadaire jusqu'au 1er septembre 2027, réunissant le chef de projet de LUMIGRÈS, la DSI et la direction financière (M. MARSANGE ou Mme FRESSINAUD), car les résultats attendus sont d'abord métier : avancement des jalons, recette, anomalies, alertes du module, risques ; complété par un **comité stratégique** trimestriel (directeur général, direction de LUMIGRÈS) qui arbitre les avenants et la reconduction. Côté ALTIVERNE, un responsable du contrat contrôle le reporting de l'ESN avec ses propres outils.

Indicateur (0,5 pt), un parmi :

| Axe | Indicateur | Formule | Source | Fréquence | Cible |
|---|---|---|---|---|---|
| Processus | Respect des jalons | jalons livrés et recettés à la date prévue / jalons prévus à cette date | planning contractuel et procès-verbaux de recette | mensuelle | 100 % des jalons nécessaires au 1er septembre 2027 |
| Processus | Délai de correction des anomalies bloquantes | anomalies bloquantes corrigées en deux jours ouvrés au plus / anomalies bloquantes signalées | outil de suivi des anomalies d'ALTIVERNE | mensuelle | 100 % (engagement de la clause 6) |

**Réponses tolérées**
- Choix d'autres clauses de l'annexe 2.2 ou de clauses absentes (audit, sécurité, sous-traitance des données personnelles, réversibilité), dès lors qu'elles sont justifiées par le cas et reformulées.
- Qualification de l'abonnement au module comme un service en ligne (SaaS) distinct du forfait.
- Proposition d'un lotissement du contrat ou d'une consultation d'un second intégrateur, si elle tient compte du délai rappelé par la DSI.

**Erreurs fréquentes**
- *Forfait et régie confondus* (`ET-31`) — « le forfait est payé au temps passé » ; juste : prix et livrables fixés, engagement de résultat ; la régie met à disposition des compétences pilotées par le client.
- *Analyse juridique approfondie* (programme 1.4, exclusions) — qualification du contrat, régime de la responsabilité, décisions de justice ; juste : enjeux opérationnels et principes de sécurisation.
- *Données laissées au prestataire, réversibilité oubliée* (F04, piège 4 ; `JUR-A05`) ; juste : données, paramétrages et règles apprises propriété du client, restitution en format ouvert.
- *Pénalités sans mesure* (F04, piège 3) — pénalités sans niveaux mesurables ; juste : jalons et niveaux mesurés, pénalités proportionnées.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des contrats, clauses critiques, gouvernance de la relation | forfait, recette, pénalités, propriété, réversibilité, comités | F04 § 1, 3 à 6 | guide p. 235-236, 255-256 |
| RGPD, règlement (UE) 2016/679 | sous-traitance des données personnelles (art. 28) | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 2.5 – Blockchain et crypto-actifs : trois propositions (3 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.a` « Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations » ; `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.d` « Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ».

**Annexes mobilisées** : annexes 1.1 (chiffre d'affaires, clients) et 2.3 (propositions et repères au 31/12/2026).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Blockchain définie (registre distribué, blocs chaînés par empreintes, consensus, horodatage, inaltérabilité pratique, confiance entre acteurs) | 0,5 |
| a-2 | Rattachement des trois propositions à la typologie | 0,5 |
| b-1 | Proposition (a) : opportunités, risques, cadre | 0,5 |
| b-2 | Proposition (b) : opportunités, risques, cadre (prestataire non agréé, MiCA) | 0,5 |
| b-3 | Proposition (c) : opportunités, risques, cadre (NFT et champ de MiCA) | 0,5 |
| b-4 | Recommandations justifiées et hiérarchisées pour les trois propositions | 0,5 |

**Réponse indicative**

*2.5 a) – Définition et typologie*

La blockchain est un registre distribué, partagé et synchronisé entre plusieurs nœuds, dont les transactions sont regroupées en blocs chaînés par des empreintes cryptographiques et validées par un mécanisme de consensus ; elle permet à des acteurs qui ne se font pas mutuellement confiance de partager une information horodatée et pratiquement inaltérable, sans administrateur central. Elle se distingue d'une base de données distribuée, que son administrateur peut modifier. Les blockchains publiques sont ouvertes à tous ; les blockchains permissionnées réservent la validation à des participants identifiés (0,5 pt).

Rattachement (0,5 pt) :
- (a) rapports de visite : **certification** (preuve d'existence et d'intégrité d'un document à une date, par ancrage de son empreinte) ;
- (b) paiements en jeton de monnaie électronique : applications **financières** des crypto-actifs, de la famille de la **finance décentralisée**, ici avec un intermédiaire qui conserve et convertit les jetons ;
- (c) certificat d'appareil et fidélité : **NFT**, avec une dimension de **traçabilité** de l'historique de l'appareil.

*2.5 b) – Évaluation et recommandations*

| Proposition | Opportunités | Risques et limites | Cadre (annexe 2.3) |
|---|---|---|---|
| (a) Rapports de visite certifiés (0,5 pt) | preuve que le rapport n'a pas été modifié depuis sa date, vérifiable par le client sans faire confiance au groupe : répond directement aux deux contestations de 2026 ; coût modeste (40 000 € par an, de l'ordre de 0,1 € par rapport pour environ 400 000 rapports) ; argument commercial auprès des bailleurs | l'ancrage prouve l'intégrité du document, pas la réalité de la visite ni l'exactitude de son contenu (problème de l'« oracle ») : la saisie du rapport doit rester contrôlée ; le rapport cite le technicien : seule l'empreinte, et jamais le rapport, doit être inscrite dans un registre inaltérable ; dépendance au prestataire d'ancrage ; consommation d'énergie selon le mécanisme de consensus de la blockchain choisie | aucun crypto-actif émis ni offert : MiCA ne s'applique pas ; risque RGPD (minimisation, effacement) fortement réduit si seule l'empreinte, jamais le rapport, est inscrite ; alternative de l'horodatage électronique d'un service de confiance (eIDAS 2) ; ISO 22739:2024 fixe seulement le vocabulaire |
| (b) Paiements en jeton stable (0,5 pt) | faible : un seul client, 1,2 M€ de chiffre d'affaires, 0,2 % du chiffre d'affaires du groupe ; règlement international plus rapide | le prestataire, ancien PSAN dont l'agrément MiCA est en cours d'instruction, ne peut plus fournir en France de services sur crypto-actifs depuis le 02/07/2026 : recourir à lui exposerait ALTIVERNE à un prestataire en situation irrégulière ; risque de perte ou de vol des jetons conservés (clés), risque de contrepartie, vigilance sur l'origine des fonds d'un client établi hors de l'Union ; commission de 1 % (environ 12 000 € par an) ; rapprochements bancaires plus complexes, à rebours de la fiabilisation | ALTIVERNE n'émettrait pas de jeton et ne fournirait pas de service sur crypto-actifs : elle n'a pas à être agréée ; en revanche, la conservation pour son compte et l'échange contre des euros sont des services sur crypto-actifs réservés aux PSCA agréés ; le jeton de monnaie électronique doit être émis par un établissement de crédit ou de monnaie électronique ; la facture reste établie en euros ; l'opération, internationale, relève du e-reporting par la plateforme (annexe 2.1) |
| (c) Certificat et fidélité en NFT (0,5 pt) | différenciation des appareils modernisés ; certificat unique et transférable au nouveau propriétaire ou syndic | les clients n'ont pas de portefeuille de crypto-actifs : usage improbable ; ALTIVERNE serait seule à écrire l'historique, qui doit être mis à jour à chaque intervention : une blockchain n'apporte rien qu'une base centralisée tenue par le groupe n'assure déjà ; image d'objets spéculatifs auprès de bailleurs sociaux et d'établissements de santé ; coût de 60 000 € la première année ; énergie | les NFT réellement uniques sont exclus du champ de MiCA ; des NFT « de collection » émis en série et échangeables risquent de ne pas être regardés comme uniques et de relever alors de MiCA (offre au public de crypto-actifs) |

Recommandations hiérarchisées (0,5 pt) :
1. **Proposition (a) : expérimenter**, sur le parc des deux bailleurs qui ont contesté des rapports, l'ancrage de la seule empreinte des rapports, en le comparant à un horodatage électronique fourni par un service de confiance au sens d'eIDAS 2 ; décision de généralisation sur la base du coût, de l'usage par les clients et de la valeur de preuve.
2. **Proposition (c) : abandonner** les NFT de collection ; remplacer le certificat NFT par un certificat numérique de l'appareil remis dans l'espace client, dont l'empreinte peut être ancrée comme en (a).
3. **Proposition (b) : refuser** en l'état ; proposer au client un virement international en euros ; ne réexaminer qu'avec un PSCA agréé et une conversion immédiate en euros, si la demande devient significative.

Lorsqu'un registre distribué entre dans un processus financier, les auditeurs légaux en prennent connaissance comme de tout système d'information (NEP), sans norme propre à la blockchain : le projet (a), qui ne touche pas les comptes, n'en relève pas.

**Réponses tolérées**
- Proposition (a) rattachée à la traçabilité, ou (c) à la certification, si l'usage est justifié.
- Proposition (b) rattachée aux crypto-actifs et aux jetons stables plutôt qu'à la finance décentralisée, avec la remarque qu'un intermédiaire agréé est requis.
- Recommandation de lancer (a) directement ou de lui préférer l'horodatage d'un service de confiance, si le choix est argumenté par la preuve, le coût et la protection des données.
- Évaluation des trois propositions présentée dans un tableau compact (opportunités, risques, cadre), si chaque case s'appuie sur l'annexe 2.3.
- Grille d'opportunité (plusieurs acteurs qui écrivent, absence de tiers de confiance, besoin d'inaltérabilité, données partageables, volume, coût et énergie) appliquée aux trois propositions.

**Erreurs fréquentes**
- *Blockchain confondue avec une base de données distribuée* (`ET-08`) ; juste : registre partagé entre acteurs sans confiance mutuelle, synchronisé par consensus.
- *MiCA invoqué pour la tenue des comptes ou l'impôt, NFT soumis sans réserve à MiCA* (`ET-35`) ; juste : MiCA encadre l'offre au public, les jetons stables et les prestataires ; les NFT réellement uniques en sont exclus.
- *Régime français antérieur à MiCA présenté comme en vigueur* (F11, piège 2) ; juste : depuis le 02/07/2026, seuls les PSCA agréés au titre de MiCA peuvent exercer.
- *Inaltérabilité confondue avec la vérité de la donnée* (F11, piège 3) ; juste : le registre garantit l'intégrité de ce qui y est inscrit, pas son exactitude.
- *Opportunités sans risques ni énergie* (`ET-19`) ; juste : apports, limites, coûts et consommation d'énergie mis en regard.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2023/1114 (MiCA) | offre au public, jetons stables, PSCA, exclusion des NFT uniques, fin de la période transitoire des anciens PSAN le 01/07/2026 | `mica` ; F11 § 3 ; fiche commune § 3 | applicable depuis le 30/12/2024 (jetons stables depuis le 30/06/2024) |
| Règlement (UE) 2024/1183 (eIDAS 2) | services de confiance : horodatage | `eidas2` ; F11 § 3.4 | en vigueur |
| RGPD, règlement (UE) 2016/679 | minimisation, effacement face à l'inaltérabilité | `rgpd` ; F11 § 2.3 | applicable depuis le 25/05/2018 |
| ISO 22739:2024 | vocabulaire des registres distribués | `iso_22739_2024` ; F11 § 3.4 | en vigueur [S] |
| NEP | aucune norme propre à la blockchain | `nep_315` ; F11 § 3.4 | en vigueur |
| Usages, grille d'opportunité, limites | certification, NFT, oracle, énergie | F11 § 1 et 2 | guide p. 268-269 |

---

## DOSSIER 3 – INSCRIRE LE SYSTÈME D'INFORMATION DANS LA DÉMARCHE DE DURABILITÉ ET CAPITALISER LES SAVOIR-FAIRE (12 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Le SI au service de l'état de durabilité | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.b` Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) | 3 |
| 3.2 Transition numérique responsable et gouvernance du SI | `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ; `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété ; `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale | 3 |
| 3.3 Maturité des processus | `1.2.d` Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) | 2 |
| 3.4 Transmission des savoir-faire des techniciens | `1.6.a` Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle ; `1.6.b` Architecture fonctionnelle des systèmes de knowledge management ; `1.6.c` Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) ; `1.6.d` Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums ; `1.6.e` Leviers d'appropriation et de transformation des pratiques professionnelles | 4 |
| **Dossier 3 – Inscrire le système d'information dans la démarche de durabilité et capitaliser les savoir-faire** |  | **12** |

Répartition indicative : connaissances (architecture des ESRS et double matérialité, sobriété numérique, gouvernance orientée RSE, maturité d'un processus, connaissances tacites et explicites : items 3.1 a-1, 3.1 a-2 pour moitié, 3.2 a-1 pour moitié, 3.2 b-1 pour moitié, 3.3-1, 3.4 a-1 pour moitié) 2 points ; analyse des annexes et recommandations 10 points, soit environ 83 %. Durée conseillée : 12 points × 4,5 minutes = 54 minutes.

---

### 3.1 – Le SI au service de l'état de durabilité (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.b` « Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) ».

**Annexes mobilisées** : annexes 1.1 (plan « ALTIVERNE 2030 », publication volontaire), 3.1 (production de l'état de durabilité 2026, demandes des clients, empreinte du SI, application mobile) et 3.2 (repères sur la CSRD et les ESRS).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Architecture des ESRS présentée : normes transversales et normes thématiques regroupées en trois piliers (environnement, social, gouvernance), avec les normes thématiques qui concernent le SI du groupe (climat, ressources et économie circulaire, personnel) | 0,5 |
| a-2 | Double matérialité expliquée (impact **ou** financière, ou les deux) et illustrée par un enjeu d'impact et un enjeu financier liés au SI du groupe | 0,5 |
| b-1 | **Collecte** : faiblesse tirée de l'annexe 3.1 et mesure relevant du SI | 0,5 |
| b-2 | **Fiabilité** : faiblesse tirée de l'annexe 3.1 et mesure relevant du SI | 0,5 |
| b-3 | **Traçabilité** : faiblesse tirée de l'annexe 3.1 et mesure relevant du SI | 0,5 |
| c | Deux principes de stratégie SI responsable reliés au plan « ALTIVERNE 2030 » | 0,5 |

**Réponse indicative**

*3.1 a) – Architecture des ESRS et double matérialité*

Les ESRS sont les normes européennes selon lesquelles est établi l'état de durabilité prévu par la CSRD ; le groupe s'y conforme **volontairement** (annexes 1.1 et 3.2). Elles comprennent **deux normes transversales**, qui fixent les exigences générales (principes, double matérialité, chaîne de valeur) et les informations générales sur l'entreprise (gouvernance, stratégie, gestion des impacts, risques et opportunités), et des **normes thématiques** regroupées en trois piliers : **environnement** (notamment le climat, les ressources et l'économie circulaire), **social** (notamment le personnel de l'entreprise) et **gouvernance** (conduite des affaires). Le SI du groupe intéresse au premier chef les normes climat (énergie de la salle informatique, fabrication des équipements) et ressources et économie circulaire (durée d'usage et fin de vie des terminaux et des boîtiers), ainsi que la norme relative au personnel (formation, inclusion des techniciens) (0,5 pt).

La **double matérialité** signifie qu'un enjeu est à traiter dans l'état de durabilité s'il est matériel du point de vue des **impacts** de l'entreprise sur les personnes et l'environnement, y compris dans sa chaîne de valeur (approche « de l'intérieur vers l'extérieur »), **ou** du point de vue **financier**, c'est-à-dire de ses effets sur la performance, la situation financière, l'accès au financement ou le coût du capital de l'entreprise (approche « de l'extérieur vers l'intérieur »), ou des deux (0,5 pt avec les deux illustrations) :
- **matérialité d'impact** : l'empreinte du SI, notamment la fabrication de 500 terminaux neufs par an alors que 70 % des terminaux retirés fonctionnent encore, les 600 MWh de la salle du siège, dont la moitié part en refroidissement, et les 6 000 boîtiers à remplacer d'ici 2030 (annexe 3.1 B) ; dans le pilier social, l'application mobile inaccessible à une quinzaine de techniciens malvoyants ou daltoniens (annexe 3.1 D) ;
- **matérialité financière** : la durabilité est devenue un critère commercial, puisque trois grands clients demandent l'empreinte des prestations et qu'un groupe de cliniques en fait un critère du choix de son prestataire (annexe 3.1 A) ; des données de durabilité peu fiables ou une empreinte mal maîtrisée exposent le groupe à la perte de contrats et à un risque de réputation, alors que le plan « ALTIVERNE 2030 » fait de la durabilité un argument commercial.

Le SI est donc à la fois une **source d'impacts** à publier et l'**outil de production** de l'état de durabilité.

*3.1 b) – Collecte, fiabilité et traçabilité des données*

Le SI organise la chaîne de production de l'état de durabilité : il collecte les données à la source, les contrôle, les consolide et en conserve la piste d'audit ; la DSI en est l'architecte et la garante de la qualité, la responsable RSE fixant le contenu attendu et validant les informations. Aujourd'hui, cette chaîne repose sur 40 tableurs consolidés à la main par une seule personne en six semaines.

| Propriété | Faiblesse (annexe 3.1 A) | Mesure relevant du SI |
|---|---|---|
| **Collecte** (0,5 pt) | 40 tableurs transmis par courriel ; factures d'énergie ressaisies ; 3 agences n'ont rien envoyé et ont été estimées sur 2025 ; fichiers des filiales reçus avec trois semaines de retard | **collecte automatisée à la source**, dans un outil unique de collecte des données de durabilité : extraction directe des données des fournisseurs d'énergie et des cartes carburant, interface avec le logiciel de paie et avec ceux des filiales, saisie guidée pour le reste (bordereaux), avec un calendrier et des relances automatiques |
| **Fiabilité** (0,5 pt) | unités hétérogènes (kWh, MWh, euros) ; 10 % des kilométrages manquants ou incohérents ; « heure de formation » définie différemment selon les pays ; formules remplacées par des valeurs | **dictionnaire des données de durabilité** (définition, unité, méthode de calcul, périmètre, source et propriétaire de chaque donnée), commun au groupe et aux filiales, et **contrôles automatiques** à la saisie (unités imposées, complétude, bornes, comparaison avec l'année précédente), avec validation par le propriétaire de la donnée |
| **Traçabilité** (0,5 pt) | aucun lien entre le bordereau et le chantier ; justificatifs introuvables pour un quart des tonnages ; corrections ni datées ni attribuées ; chiffres publiés non rapprochables de leur source | **piste d'audit** : chaque valeur est rattachée à sa source et à son justificatif (bordereau numérisé et lié au chantier dans l'application des interventions, facture dans la GED), chaque modification est journalisée (qui, quand, quelle valeur, pourquoi) et les données sont verrouillées après validation |

Conclusion : la fiabilité et la traçabilité des données sont la condition pour que la durabilité devienne un argument commercial crédible ; un chiffre que le groupe ne sait pas justifier devant un client est un risque, non un atout.

*3.1 c) – Deux principes d'une stratégie SI responsable (0,5 pt pour deux principes justes et reliés au plan)*

Parmi :
1. **Intégrer la durabilité dans la gouvernance et la planification du SI**, et non en ajout marginal : critères environnementaux et sociaux dans chaque arbitrage de projet et dans le schéma directeur, indicateurs de durabilité intégrés au tableau de bord SI à côté des indicateurs de coût et de service.
2. **La sobriété d'abord** : interroger le besoin avant de chercher l'efficacité (durée d'usage des équipements, volume de données conservées, fonctionnalités réellement utiles), en cohérence avec les axes de la loi REEN et du RGESN (annexe 3.2).
3. **Le SI au service de la durabilité du groupe** (« IT for green ») : fournir des données de durabilité fiables, aider à réduire les déplacements des 1 300 véhicules et la consommation des sites, faire de ces résultats un argument commercial du plan « ALTIVERNE 2030 ».
4. **Un numérique inclusif et éthique** : des outils accessibles à tous les techniciens et un usage proportionné des données qui les concernent.

**Réponses tolérées**
- Vocabulaire des ESRS de 2023 (« double importance », « incidences », « déclaration relative à la durabilité ») : accepté, l'exercice 2026 admettant les deux versions.
- Illustration de la matérialité d'impact par les déplacements des techniciens ou les déchets électroniques des modernisations, et de la matérialité financière par le coût de la climatisation à remplacer, si le lien avec le SI est fait.
- Mesures de traçabilité et de fiabilité regroupées autour d'une plateforme ou d'un module de collecte des données de durabilité, si la piste d'audit et les définitions communes y figurent.
- Principes formulés avec la distinction Green IT / IT for green, s'ils sont appliqués au groupe.

**Erreurs types**
- *Codes et contenu détaillé des normes* (`ET-17`) — énumérer les codes des normes thématiques ou leurs informations détaillées, ou discuter l'assujettissement du groupe à la CSRD ; juste : l'architecture générale suffit, et le groupe publie volontairement (annexe 3.2).
- *Double matérialité réduite à l'une de ses faces* — ne retenir que l'impact environnemental ou que le risque financier ; juste : un enjeu est matériel par l'une **ou** l'autre approche, ou par les deux.
- *Rôle de la DSI confondu avec celui du vérificateur* (`ET-17`) — « la DSI certifie l'état de durabilité » ; juste : la DSI organise la collecte, la qualité et la piste d'audit ; la vérification éventuelle relève d'un tiers.
- *Définition sans application au cas* (`JUR-T01`) — architecture et double matérialité récitées sans les 40 tableurs, les demandes des clients ni l'empreinte du SI.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Directive (UE) 2022/2464 « CSRD », modifiée par la directive (UE) 2026/470 « Omnibus I » | objet de l'état de durabilité ; publication volontaire du groupe, sans discussion du champ | `csrd`, `csrd_omnibus` / fiche commune § 1 et 5 ; annexe 3.2 | en vigueur ; Omnibus I non transposée en France |
| Règlement délégué (UE) 2026/1563 (ESRS révisées) | architecture (normes transversales et thématiques), double matérialité | `esrs_2026` / fiche commune § 1-2 ; F14 § 2 | applicable aux exercices ouverts à compter du 01/01/2027, option pour 2026 |
| Loi REEN (loi n° 2021-1485) ; RGESN, version 2 | axes de la sobriété numérique, écoconception | `loi_reen`, `rgesn_2024` / F14 § 2 | en vigueur |
| Rôle de la DSI dans la collecte, la qualité et la traçabilité des données de durabilité | architecte de la collecte, garante de la piste d'audit | F14 § 2 ; corrigé du sujet zéro p. 362 | notion de cours |

---

### 3.2 – Transition numérique responsable et gouvernance du SI (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) » ; `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété » ; `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ».

**Annexes mobilisées** : annexes 3.1 (empreinte du SI, options A et B, application mobile) et 3.2 (loi REEN, RGESN, étude ADEME-Arcep).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Sobriété numérique définie (interroger le besoin avant l'efficacité) ; option A évaluée : gains (PUE, énergie, chaleur), limite du transfert « à l'identique », conditions de réussite | 0,5 |
| a-2 | Option B évaluée : poids de la fabrication des terminaux, 300 au lieu de 500 terminaux neufs par an, conditions de réussite (application allégée, batterie, réemploi) | 0,5 |
| a-3 | Plan en trois actions priorisées et justifiées (ordre, échéance, lien entre les actions) | 0,5 |
| a-4 | Indicateur de l'action placée en premier : formule, source, fréquence, cible et axe | 0,5 |
| b-1 | Gouvernance du SI orientée RSE définie ; principe d'**inclusion** appliqué à l'application mobile, avec son porteur | 0,5 |
| b-2 | Principes d'**éthique** et de **sobriété** appliqués (géolocalisation, options de l'annexe 3.1), avec leurs porteurs | 0,5 |

**Réponse indicative**

*3.2 a) – Évaluation des deux options et plan de transition*

La **sobriété numérique** consiste à interroger la nécessité des équipements, des services et des données avant de chercher à les rendre plus efficaces : renoncer, réduire, faire durer ; elle se distingue du Green IT, qui réduit l'empreinte d'un SI donné, et ne se limite pas aux économies d'énergie.

**Option A – Hébergement chez un prestataire** (0,5 pt avec la définition) :
- *Effets sur l'empreinte* : l'indicateur d'efficacité énergétique passerait d'environ 2 à 1,3 (moins d'énergie perdue en refroidissement que dans une salle de 2001), avec une électricité d'origine renouvelable et la chaleur des serveurs réutilisée par un réseau de chaleur ; la mutualisation évite l'achat d'une climatisation neuve. Coûts comparables sur trois ans : 0,4 + 3 × 0,3 = 1,3 M€, contre 3 × 0,2 + 0,8 = 1,4 M€ pour le maintien de la salle ; la décision se prend donc sur d'autres critères que le coût.
- *Sobriété* : transférer **à l'identique** 60 serveurs utilisés à 15 % de leur capacité et 400 To de données, dont 30 % n'ont pas été rouverts depuis deux ans et qui sont conservés en trois copies, revient à **déplacer l'empreinte sans la réduire** : l'énergie consommée chez le prestataire reste une empreinte de la chaîne de valeur du groupe.
- *Conditions de réussite* : inventaire préalable des applications et des données (absent aujourd'hui), consolidation et virtualisation des serveurs avant la migration, purge des données inutiles et règles de conservation des photos et vidéos, engagements du prestataire mesurés et rapportés chaque année (consommations attribuées au groupe), possibilité de changer de prestataire et localisation des données en France, avant la fin de vie de la climatisation en 2028.

**Option B – Allongement de la durée d'usage des terminaux** (0,5 pt) :
- *Effets sur l'empreinte* : selon le volet de 2022 de l'étude ADEME-Arcep, les terminaux concentraient 65 à 92 % de l'empreinte environnementale du numérique, principalement du fait de leur fabrication (annexe 3.2) ; à l'échelle du groupe, 1 500 terminaux renouvelés tous les trois ans pèsent bien plus que l'énergie de 60 serveurs ; passer de trois à cinq ans ramène les achats de 500 à 300 terminaux neufs par an, soit 40 % de moins, et donc autant d'empreinte de fabrication et de déchets électroniques en moins ; le réemploi par un reconditionneur prolonge encore la vie des terminaux, dont 70 % fonctionnent encore lorsqu'ils sont retirés. C'est l'axe de la loi REEN sur le renouvellement des terminaux. Les achats passent d'environ 0,4 M€ à 0,24 M€ par an, auxquels s'ajoutent environ 300 révisions à 100 €, soit 0,03 M€ : l'économie avoisine 0,13 M€ par an en régime établi.
- *Sobriété* : c'est une mesure de sobriété au sens propre (faire durer plutôt que remplacer).
- *Conditions de réussite* : la cause du remplacement est logicielle : l'application des interventions, dont chaque version exige la dernière version du système d'exploitation et pèse davantage, doit être **écoconçue** pour rester utilisable sur des terminaux de cinq ans, comme le demande le RGESN ; remplacement des batteries et révision au bout de trois ans ; adhésion des techniciens, qui ne doivent pas subir un outil lent ; traçabilité du devenir des terminaux repris (réemploi ou recyclage).

**Plan de transition en trois actions priorisées** (0,5 pt) :
1. **Allonger dès 2027 la durée d'usage des terminaux à cinq ans** et organiser leur réemploi (option B) : premier levier d'empreinte, rapide, peu coûteux, porté par la direction de la maintenance et la responsable RSE.
2. **Écoconcevoir et rendre accessible l'application des interventions** (critères du RGESN) : version allégée compatible avec les terminaux anciens, et fonctions d'accessibilité (agrandissement, contraste, saisie vocale) ; c'est la condition de réussite de l'action 1 et la réponse au point d'inclusion de l'annexe 3.1 D ; portée par la DSI en 2027-2028.
3. **Rendre l'option A sobre avant de la réaliser** : inventaire, consolidation des 60 serveurs, purge et règles de conservation des données, puis migration en 2028 chez le prestataire, avant le remplacement de la climatisation, avec un rapport annuel des consommations ; portée par la DSI.

**Indicateur de l'action 1** (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Durée d'usage moyenne des terminaux des techniciens | somme des durées d'usage des terminaux retirés du service sur la période / nombre de terminaux retirés | inventaire des terminaux mobiles (outil de gestion de la flotte de terminaux) | semestrielle | 5 ans en 2029, contre 3 ans en 2026 | environnement |

Mesurée sur les seuls terminaux retirés, cette moyenne ne devient significative qu'à partir de 2029 : en 2027 et en 2028, seuls les terminaux en panne sont retirés et ils la font baisser. On la suit donc avec une cible intermédiaire : 300 terminaux neufs achetés par an au plus dès 2028.

*3.2 b) – Trois principes de gouvernance du SI orientée RSE*

La **gouvernance du SI orientée RSE** intègre les enjeux sociaux, environnementaux et éthiques dans les instances, les règles de décision et le pilotage du SI : critères de durabilité dans les arbitrages, responsabilités désignées, indicateurs intégrés au tableau de bord SI, charte du numérique responsable ; elle prend souvent la forme d'un comité du numérique responsable réunissant la DSI, la responsable RSE, la DRH, le délégué à la protection des données et des représentants des utilisateurs, sous l'autorité du directeur général.

1. **Inclusion** (0,5 pt avec la définition) : toute application interne est **accessible dès sa conception** et testée avec les utilisateurs concernés ; pour l'application des interventions : agrandissement des caractères, contraste renforcé, saisie vocale, pictogrammes et choix guidés plutôt que commentaires libres, pour la quinzaine de techniciens malvoyants ou daltoniens et les quelque 150 qui écrivent difficilement. Porteurs : la DSI, responsable de l'application, avec la DRH ; critère d'acceptation de chaque nouvelle version validé par le comité.
2. **Éthique** (0,5 pt avec le principe de sobriété) : la collecte de données sur les salariés est **proportionnée à une finalité définie et transparente** : géolocalisation limitée aux interventions (pas pendant les pauses), finalité expliquée aux techniciens et à leurs représentants, durée de conservation fixée, traitement inscrit au registre des traitements sur avis du délégué à la protection des données. Porteurs : le comité du numérique responsable et le délégué à la protection des données ; règle inscrite dans une charte.
3. **Sobriété** : chaque projet et chaque renouvellement passe une revue de sobriété (besoin réel, durée d'usage, données conservées, consommation) ; pour les options de l'annexe 3.1 : pas de migration « à l'identique », pas de renouvellement des terminaux au bout de trois ans par défaut, règles de conservation des photos et vidéos. Porteurs : la DSI et la responsable RSE, rendant compte au comité de direction.

**Réponses tolérées**
- Plan qui place l'option A en premier en raison de l'échéance de la climatisation en 2028, si le candidat impose la consolidation et la purge avant la migration et justifie l'ordre.
- Troisième action consacrée à la sobriété du stockage ou au remplacement des 6 000 boîtiers de première génération par des boîtiers reconditionnés, si elle est justifiée par l'annexe 3.1.
- Autre indicateur complet pour l'action 1 : nombre de terminaux neufs achetés par an (cible 300), taux de terminaux retirés réemployés.
- Principe d'éthique appliqué à un autre usage des données des salariés, si la proportionnalité et la transparence sont au cœur de la réponse.
- Référence à un référentiel ou à des règles d'accessibilité numérique, acceptée en appui du principe d'inclusion, sans analyse du champ de l'obligation.

**Erreurs types**
- *Sobriété confondue avec l'économie d'énergie* (`ET-12`) — juger l'option A sobre parce que son PUE est meilleur ; juste : la sobriété interroge d'abord le besoin (60 serveurs à 15 %, données jamais rouvertes).
- *Empreinte réduite à l'électricité* (`ET-38`) — préférer l'option A parce qu'elle réduit les MWh ; juste : la fabrication des équipements pèse lourd dans l'empreinte, et d'abord celle des terminaux (annexe 3.2) ; l'énergie d'une salle n'en est qu'une partie.
- *Durabilité en ajout marginal* — principes de gouvernance sans porteur ni règle de décision ; juste : la durabilité s'intègre aux instances et aux arbitrages du SI (limite du programme).
- *Liste d'indicateurs génériques* (`ET-18`) — catalogue d'indicateurs de Green IT sans lien avec l'action ; juste : un indicateur relié à l'action prioritaire, avec ses cinq champs.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Étude ADEME-Arcep (volet du 19/01/2022 ; mise à jour du 17/01/2025, données 2022) | poids des terminaux et de leur fabrication dans l'empreinte du numérique | `etude_ademe_arcep_numerique` / F14 § 1 ; annexe 3.2 | publiée |
| Loi REEN (loi n° 2021-1485 du 15 novembre 2021) | limiter le renouvellement des terminaux, centres de données moins énergivores | `loi_reen` / F14 § 2 ; annexe 3.2 | en vigueur |
| RGESN, version 2 (2024) | écoconception, service utilisable sur des équipements anciens | `rgesn_2024` / F14 § 2 ; annexe 3.2 | en vigueur |
| Sobriété numérique, Green IT, centres de données, PUE, gouvernance orientée RSE | définitions, leviers, limites du PUE | F14 § 3-5 | notion de cours |

---

### 3.3 – Maturité des processus (2 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.d` « Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) ».

**Annexes mobilisées** : annexe 3.3 (auto-évaluation des deux processus, enjeu des départs) ; l'annexe 3.1 A peut appuyer le positionnement du processus des données de durabilité.

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Maturité d'un processus définie ; échelle à niveaux différenciés, chaque niveau décrit en une ligne | 0,5 |
| 2 | Gestion des connaissances techniques située (niveau 1 : initial) et justifiée par l'annexe | 0,5 |
| 3 | Gestion des données de durabilité située (niveau 2 : géré) et justifiée par l'annexe | 0,5 |
| 4 | Deux priorités déduites du positionnement (niveau visé, actions, échéance) | 0,5 |

**Réponse indicative**

La **maturité d'un processus** est le degré auquel il est défini, géré, mesuré et amélioré de façon continue, de sorte que ses résultats ne dépendent plus des seules personnes qui l'exécutent ; les modèles de maturité, comme le CMMI ou les niveaux de capacité de COBIT 2019, la situent sur une échelle de niveaux pour fixer une cible et un plan de progression (0,5 pt avec l'échelle).

Échelle inspirée du CMMI et positionnement :

| Niveau | Description | Gestion des connaissances techniques | Gestion des données de durabilité |
|---|---|---|---|
| 1 – Initial | activité menée au cas par cas, résultat dépendant des personnes | **niveau actuel** : ni processus, ni responsable, ni mesure ; binômes à Lyon-Est et à Grenoble seulement, à l'initiative des agences | — |
| 2 – Géré | activité planifiée et suivie, responsabilités désignées, mais pratiques propres à chaque entité | cible fin 2027 | **niveau actuel** : calendrier, liste des données attendues, contributeur par entité, état publié à la date prévue ; suivi encore fragile (envois manquants, retards : annexe 3.1 A) et méthodes propres à chaque entité |
| 3 – Défini | processus standardisé et documenté pour toute l'organisation, définitions communes | cible 2028 | cible pour la campagne de l'exercice 2027 : définitions communes, procédure de groupe, contrôles formalisés |
| 4 – Géré quantitativement | processus mesuré, objectifs de qualité chiffrés et suivis | — | cible ultérieure : mesure de la qualité des données |
| 5 – En optimisation | amélioration continue fondée sur les mesures | — | — |

- **Gestion des connaissances techniques : niveau 1** (0,5 pt) : aucun processus, aucun responsable, rien n'est mesuré ; les deux agences qui organisent des binômes montrent des pratiques locales non reproduites, ce qui ne suffit pas pour le niveau 2 à l'échelle du groupe ; personne ne sait quels savoirs disparaîtront.
- **Gestion des données de durabilité : niveau 2** (0,5 pt) : la campagne 2026 a été planifiée et suivie, avec des contributeurs désignés et un état publié à la date prévue, malgré un suivi encore fragile (trois agences absentes, filiales en retard : annexe 3.1 A) ; mais l'absence de définitions communes, de procédure de groupe, de contrôles et de mesure de la qualité l'empêche d'atteindre le niveau 3, ce que confirment les constats de l'annexe 3.1 A (unités hétérogènes, définitions divergentes).

Deux priorités (0,5 pt) :
1. **Porter la gestion des connaissances au niveau 2 d'ici fin 2027** : désigner un responsable, planifier la capitalisation des savoirs critiques et généraliser les binômes, car les départs se concentrent en 2028 et 2029 et la perte serait irréversible ; c'est la priorité la plus urgente.
2. **Porter la gestion des données de durabilité au niveau 3 avant la campagne de l'exercice 2027** : dictionnaire des données, procédure écrite de groupe, outil unique de collecte et contrôles formalisés (mesures de la question 3.1 b).

**Réponses tolérées**
- Niveaux de capacité de COBIT 2019, de 0 à 5 : gestion des connaissances au niveau 0 ou 1, données de durabilité au niveau 2, si les niveaux sont décrits et le positionnement justifié.
- Grille à trois ou à quatre niveaux, si les niveaux sont différenciés et la justification tirée de l'annexe.
- Gestion des connaissances située entre les niveaux 1 et 2 en raison des pratiques de Lyon-Est et de Grenoble, si le candidat montre qu'elles restent locales.
- Gestion des données de durabilité située entre les niveaux 1 et 2, si le candidat s'appuie sur les envois manquants et les retards de l'annexe 3.1 A et reconnaît la planification de la campagne.
- Référence au modèle MAGNum 2026 du Cigref pour une évaluation plus large de la gouvernance du numérique.

**Erreurs types**
- *Grille sans niveaux différenciés* — niveaux nommés sans description, ou positionnement sans justification ; juste : chaque niveau décrit, chaque positionnement appuyé sur un fait de l'annexe (corrigé du sujet zéro p. 364).
- *Référentiel confondu avec une norme ou un outil* (`ET-01`, `JUR-S06`) — « installer COBIT », « la norme CMMI » ; juste : le CMMI et COBIT 2019 sont des référentiels de bonnes pratiques, non des normes ni des logiciels.
- *Priorités sans lien avec le positionnement* (`JUR-T03`) — liste d'actions génériques ; juste : passer au niveau supérieur, avec une échéance tirée du cas (départs de 2028-2029, campagne 2027).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| CMMI V3.0 (CMMI Institute, ISACA) | cinq niveaux de maturité | `cmmi_v3` / F01 § 5 ; F02 § 5 | en vigueur |
| COBIT 2019 (ISACA) | niveaux de capacité des processus de 0 à 5 | `cobit_2019` / F02 § 3 ; F01 § 5 | en vigueur |
| MAGNum 2026 (Cigref, IFACI, ISACA) | modèle de maturité de la gouvernance du numérique (toléré) | `magnum_2026` / F01 § 5 | en vigueur |

---

### 3.4 – Transmission des savoir-faire des techniciens (4 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.a` « Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle » ; `1.6.b` « Architecture fonctionnelle des systèmes de knowledge management » ; `1.6.c` « Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) » ; `1.6.d` « Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums » ; `1.6.e` « Leviers d'appropriation et de transformation des pratiques professionnelles ».

**Annexes mobilisées** : annexes 1.1 (300 départs d'ici 2030, organigramme) et 3.3 (enjeu, outils existants, témoignages).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Connaissances tacites et explicites distinguées et appliquées au savoir-faire de dépannage des appareils anciens | 0,5 |
| a-2 | Stratégie : identification des savoirs critiques et de leurs détenteurs, priorités selon le calendrier des départs, modes de transmission (sur le terrain et par formalisation), mise à jour | 0,5 |
| a-3 | Pilotage, gouvernance et rôles (sponsor, comité, responsable de la gestion des connaissances, référents techniques, contributeurs, DSI, DRH) | 0,5 |
| b-1 | Premier outil recommandé, son rôle et son articulation avec l'existant | 0,5 |
| b-2 | Second outil recommandé, son rôle et son articulation avec l'existant | 0,5 |
| c-1 | Levier répondant au frein du technicien expérimenté (temps, crainte de perdre sa valeur, préférence pour la transmission sur le terrain) | 0,5 |
| c-2 | Levier répondant au frein du jeune technicien (accès en mobilité, format court) | 0,5 |
| c-3 | Deux leviers répondant aux freins de la responsable d'agence (objectifs de productivité) et de la DRH (échec du wiki de 2024) ; 0,5 pour les deux | 0,5 |

**Réponse indicative**

*3.4 a) – Stratégie de gestion des connaissances*

Les **connaissances explicites** sont formalisées et transmissibles par un support (notice, schéma, procédure) ; les **connaissances tacites** sont incorporées dans les personnes, issues de l'expérience, et difficiles à formaliser. Le savoir-faire de dépannage des quelque 8 000 appareils à armoire à relais est **tacite** : astuces de diagnostic, schémas annotés dans des classeurs personnels, contacts avec d'anciens fournisseurs ; les notices de la GED, explicites, ne suffisent pas, d'où un dépannage deux fois plus long (6 heures contre 3) et une seconde visite dans 30 % des cas quand il est confié à un technicien récent (0,5 pt).

**Stratégie** (0,5 pt) :
1. **Identifier les savoirs critiques** : cartographier, par famille d'appareils et de pannes, les savoirs qui disparaîtront avec les 300 départs, et d'abord ceux des 120 spécialistes des armoires à relais, avec leurs détenteurs et la date de leur départ ; prioriser selon l'urgence (départs de 2028) et l'enjeu (nombre d'appareils concernés).
2. **Transmettre sur le terrain** : binômes entre anciens et nouveaux sur les appareils anciens, généralisés à partir des pratiques de Lyon-Est et de Grenoble.
3. **Formaliser ce qui peut l'être** : fiches de dépannage courtes, photos annotées et vidéos de deux minutes réalisées pendant les interventions en binôme, entretiens d'explicitation avec les partants ; numérisation des classeurs.
4. **Diffuser et faire vivre** : contenus accessibles depuis le terminal, au moment de l'intervention ; revue périodique et retrait des contenus obsolètes.

**Pilotage, gouvernance et rôles** (0,5 pt) :
- **sponsor** : M. PRADELLE, directeur de la maintenance et des services, qui inscrit la transmission dans les priorités des agences, avec l'appui du directeur général ;
- **comité de pilotage** trimestriel : direction de la maintenance, DRH, DSI, responsable de la transformation numérique et quelques responsables d'agence ; il arbitre les priorités et suit l'avancement ;
- **responsable de la gestion des connaissances**, rattaché à la direction de la maintenance : anime le dispositif, la cartographie et la communauté ;
- **référents techniques** par famille d'appareils (techniciens expérimentés) : valident les contenus et répondent aux questions ;
- **contributeurs** : tous les techniciens ;
- **DSI** : outils, intégration à l'application des interventions, sécurité et conservation des contenus ;
- **DRH** : formation, reconnaissance des référents et articulation avec la gestion des compétences, complémentaire mais distincte.

Indicateur de pilotage possible :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de couverture des savoirs critiques | savoirs critiques transmis en binôme ou formalisés et validés par un référent / savoirs critiques recensés dans la cartographie | cartographie des savoirs critiques tenue par le responsable de la gestion des connaissances | trimestrielle | 100 % des savoirs des partants de 2028 avant leur départ | apprentissage |

*3.4 b) – Deux outils intégrés à l'environnement SI*

1. **Une base de connaissances de type wiki, accessible depuis l'application des interventions** (0,5 pt) : fiches de dépannage, photos annotées et vidéos courtes, organisées par famille d'appareils et par modèle d'armoire, et ouvertes directement depuis le bon d'intervention de l'appareil concerné ; chaque contenu a un propriétaire et une date de revue, et il est validé par un référent. Articulation : la **GED** reste le référentiel des notices des constructeurs, mais ses 25 000 documents sont indexés par modèle d'appareil (métadonnées) et liés aux fiches, ce qui les rend consultables depuis le terminal ; l'**intranet** devient le point d'entrée unique vers la base et l'annuaire des référents.
2. **Un forum de questions et réponses intégré à l'application mobile**, qui remplace le groupe « Dépann'Entraide » (0,5 pt) : il en garde la rapidité (question avec photo, réponse des pairs et des référents), mais dans un outil du groupe, avec des droits d'accès et des photos d'immeubles conservées hors des téléphones personnels ; les meilleures réponses sont versées dans la base de connaissances par les référents, ce qui **capitalise** ce qui se perd aujourd'hui dans le fil des messages.

Les vidéos et les photos sont soumises aux règles de sobriété de la question 3.2 (formats compressés, durée de conservation, revue des contenus inutilisés).

*3.4 c) – Quatre leviers d'appropriation*

| Frein (annexe 3.3 C) | Levier |
|---|---|
| **M. VERNOUX** (0,5 pt) : pas de temps, « écrire, ce n'est pas mon métier », crainte de perdre sa valeur, préférence pour la démonstration sur le terrain | **Reconnaissance et transmission par le geste** : statut de référent ou de tuteur valorisé (nom cité sur les contenus, mission reconnue), temps de transmission compté dans sa charge ; il montre en binôme, un jeune filme ou rédige la fiche, et il la valide |
| **M. BOURDALET** (0,5 pt) : besoin d'une réponse rapide en mobilité, GED inaccessible depuis le terminal, intranet inconnu, préférence pour la vidéo | **Intégration au flux de travail** : contenus courts (vidéos de deux minutes, photos annotées) et forum accessibles depuis l'application des interventions, sur l'appareil où il intervient, sans changer d'outil |
| **Mme GRANJOUX** (0,5 pt avec le suivant) : des objectifs fondés sur le seul nombre d'interventions et le délai d'arrivée | **Pilotage et objectifs** : la transmission entre dans les objectifs des agences (heures de binôme, savoirs transmis), son temps est prévu dans les plannings ; le gain se voit aussi en productivité (6 heures contre 3, seconde visite évitée) |
| **Mme MAUFRAS** : un wiki ouvert sans prévenir, sans animateur et sans changement du travail | **Accompagnement du changement** : sponsor visible, communication, animation par le responsable de la gestion des connaissances, lancement par un pilote dans les agences de Lyon-Est et de Grenoble, où les binômes existent déjà, et premiers contenus utiles avant l'ouverture à tous |

Conclusion : le dispositif réussira s'il part de la pratique qui fonctionne déjà (l'entraide entre techniciens et les binômes) pour la capitaliser, plutôt que d'imposer un outil de plus.

**Réponses tolérées**
- Modèle SECI (Nonaka et Takeuchi) en appui de la stratégie : socialisation par les binômes, externalisation par les vidéos et les fiches, combinaison dans la base de connaissances, internalisation par l'usage en intervention ; non exigé.
- Leviers structurés par un modèle de conduite du changement (ADKAR, huit étapes de Kotter), s'ils restent reliés aux témoignages.
- Assistant d'IA générative de recherche dans la GED et dans la base de connaissances, si le candidat en précise la gouvernance (validation humaine, sources limitées aux contenus validés) et la tension avec la sobriété.
- Trois outils au lieu de deux (par exemple GED réorganisée, base de connaissances et forum), si le rôle et l'articulation de chacun sont précisés.

**Erreurs types**
- *Gestion des connaissances réduite à la GED ou à un outil* (`ET-21`) — « numériser les classeurs dans la GED » ou « rouvrir le wiki » ; juste : un dispositif systémique (outils, processus, culture), qui organise d'abord la transmission des savoirs tacites sur le terrain.
- *Confusion avec la gestion des compétences* — plan de formation et recrutements présentés comme la réponse ; juste : la gestion des compétences est complémentaire mais distincte (limite du programme, témoignage de Mme MAUFRAS).
- *Leviers génériques* (`JUR-T08`) — « communiquer, former » sans lien avec les quatre témoignages ; juste : un levier par frein exprimé.
- *Groupe de messagerie ignoré ou simplement interdit* — le supprimer sans solution de remplacement ; juste : en reprendre la rapidité dans un outil du groupe qui capitalise les réponses.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Connaissances tacites et explicites ; dispositif de gestion des connaissances (rôles, outils, appropriation) | définitions, architecture fonctionnelle, gouvernance | F06 § 1-2 | notion de cours |
| Modèle SECI (Nonaka et Takeuchi, 1995) | toléré en appui | `nonaka_takeuchi_seci` / F06 § 1 | publié |
| ADKAR (Prosci) | toléré pour structurer les leviers | `adkar` / F05 § 7 | publié |
| Huit étapes de la conduite du changement (Kotter) | toléré pour structurer les leviers | `kotter_8_etapes` / F05 § 7 | publié |
