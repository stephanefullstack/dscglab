# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 17 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 interopérabilité et qualité des données, F08 décisionnel et visualisation, F13 apprentissage automatique et biais, F09 tableau de bord du SI, F01 alignement stratégique et veille, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Chaîne de traitement et organisation de la collecte | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 3 |
| 2.2 Méthodes d'analyse et outil d'alerte | `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation | 3 |
| 2.3 Diagnostic de la production et restitution au comité des associés | `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. | 2 |
| 2.4 Indicateurs de pilotage de la transformation de la production | `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ; `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord | 2 |
| 2.5 Modèle économique et stratégie du système d'information | `1.1.d` Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 3 |
| **Dossier 2 – Exploiter les données des clients au service du conseil** |  | **13** |

Répartition indicative : connaissances (chaîne de traitement, interopérabilité, méthodes d'analyse, tableau de bord équilibré, modèle économique, alignement stratégique) 3 points (items 2.1 a-1, 2.1 b-1, 2.2 a-1, 2.4-1, 2.5 a-1, 2.5 b-1) ; analyse des annexes et recommandations 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Chaîne de traitement et organisation de la collecte (3 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ».
- §2.1 – Structurer, modéliser et sécuriser les données : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) ». Limites : « L'interopérabilité doit être abordée à la fois sur le plan technique et sur le plan organisationnel » ; le détail technique des échanges est exclu.

**Annexes mobilisées** : annexes 2.1 (canaux, traitements, offre de l'éditeur), 1.1 (3 000 clients, six bureaux, période fiscale, secret professionnel) et 2.4 (objectifs 2029, repères sur la facturation électronique).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de traitement définie (suite organisée d'étapes qui transforme des données brutes de sources hétérogènes en informations fiables restituées pour décider), valeur limitée par le maillon le plus faible | 0,5 |
| a-2 | Cinq étapes appliquées aux données des clients du cabinet (canaux et flux, contrôles, rattachement au dossier, révision et analyse, comptes annuels et situations) | 0,5 |
| a-3 | Quatre faiblesses tirées de l'annexe 2.1, chiffrées et rattachées chacune à la bonne étape ; 0,5 dès trois faiblesses justes | 0,5 |
| b-1 | Interopérabilité définie, avec ses dimensions technique, sémantique et organisationnelle | 0,5 |
| b-2 | Quatre mesures de l'organisation cible (formats structurés et ouverts, API, nommage et rapprochement, accompagnement des clients), chacune reliée à une faiblesse et précisant ce qui change pour les clients ; 0,5 pour deux mesures | 1 |

**Réponse attendue**

*2.1 a) – Définition, chaîne du cabinet et faiblesses*

La **chaîne de traitement des données** est la suite organisée des opérations qui transforment des données brutes, issues de sources hétérogènes, en informations fiables, structurées et restituées à ceux qui décident : collecte, nettoyage, structuration, analyse, restitution. C'est une démarche, et non un outil : chaque étape a ses règles, ses responsables et ses contrôles, et la qualité du résultat se perd au maillon le plus faible (F08 § 1) (0,5 pt). Pour un cabinet, la matière première est la pièce du client : la chaîne va de la pièce déposée au conseil donné au dirigeant.

| Étape | Chaîne des données des clients de CORLANDEAU Expertise | Faiblesse constatée (annexe 2.1) |
|---|---|---|
| **Collecte** | 600 000 pièces par an, environ 200 par client, par quatre canaux (portail 250 000, application mobile 100 000, courriel 150 000, papier 100 000) ; relevés bancaires par flux automatisé pour 1 200 clients, en PDF ou sur papier pour 1 800 ; relevés de ventes des logiciels de caisse ou de facturation | **canaux non maîtrisés** : le papier n'est jamais intégré automatiquement et arrive en 45 jours ; 60 % des clients « papier » et 40 % des clients « courriel » avaient un dossier incomplet à la clôture, contre 20 % par le portail ; 30 % des dossiers incomplets, relances individuelles sans liste des pièces attendues ; **donnée structurée perdue** : les factures électroniques reçues par les clients depuis septembre 2026 arrivent en PDF ou imprimées |
| **Nettoyage** | contrôle des pièces lues automatiquement (date, montant, TVA, fournisseur), repérage des doublons, des pièces illisibles | **une pièce lue sur dix** comporte une erreur, corrigée à la révision, plusieurs semaines plus tard (plusieurs dizaines de milliers de pièces par an) ; **5 % de doublons** (30 000 pièces) repérés à la main |
| **Structuration** | rattachement de chaque pièce au bon dossier, au bon tiers et au bon mouvement bancaire ; classement | **aucune règle de nommage** (« scan_0012.pdf ») ; un même fournisseur sous plusieurs libellés, qui fausse les soldes ; rapprochement manuel pour 1 800 clients sans flux |
| **Analyse** | révision, contrôles de cohérence, préparation des déclarations, analyses pour le conseil | analyse tardive, faite sur des données incomplètes et corrigées tard ; aucune analyse en cours d'année pour 90 % des clients |
| **Restitution** | comptes annuels, déclarations, situations en cours d'année | comptes remis 98 jours après la clôture en moyenne ; situations pour **10 % des clients seulement**, à la main dans un tableur |

(0,5 pt pour la chaîne appliquée ; 0,5 pt pour au moins trois faiblesses chiffrées et bien rattachées.)

La faiblesse de fond est **organisationnelle** : chaque bureau collecte à sa façon (portail exigé à Poitiers, papier accepté sans limite à Saintes et à Châtellerault), et la chaîne s'arrête à la clôture : elle produit des comptes annuels, pas des données fraîches pour conseiller.

*2.1 b) – Interopérabilité et organisation cible de la collecte*

L'**interopérabilité** est la capacité de systèmes hétérogènes à échanger des données et à les utiliser sans intervention manuelle. Elle a une dimension **technique** (connexions, API : interfaces d'accès programmatique à un service), **syntaxique et sémantique** (formats structurés et ouverts, comme XML ou JSON, et sens partagé des données : mêmes libellés, mêmes référentiels de tiers) et **organisationnelle** (processus, responsabilités, engagements des parties) ; le programme exige les plans technique et organisationnel (F07 § 7) (0,5 pt).

| Mesure | Contenu (sans détail technique des échanges) | Faiblesse traitée | Ce qui change pour les clients |
|---|---|---|---|
| 1. **Données structurées plutôt qu'images** | récupérer les factures électroniques reçues par les clients **dans leur format structuré** (Factur-X, UBL ou CII : annexe 2.4 E), avec leur accord, au lieu de PDF relus par la lecture automatique ; demander les relevés de ventes dans un format ouvert et documenté ; réserver la photographie et le PDF aux pièces qui n'existent pas autrement | lecture automatique fautive une fois sur dix, donnée structurée perdue | le client n'envoie plus ses factures d'achat électroniques : il autorise une fois leur transmission ; il en dépose moins, et moins souvent |
| 2. **Connexions par API activées** | activer les connexions déjà comprises dans l'abonnement (annexe 2.1 C) : flux bancaires pour tous les clients qui l'acceptent (objectif 80 % fin 2029, contre 40 %), connexions aux logiciels de caisse et de facturation des clients | 1 800 clients sans flux, rapprochement manuel, données fraîches pour 40 % des clients seulement | le client autorise le flux auprès de sa banque et le renouvelle ; il ne dépose plus ses relevés ; ses données sont disponibles chaque jour pour le tableau de bord mensuel |
| 3. **Règles communes de nommage et de rapprochement** | fichier nommé automatiquement à l'arrivée (client, date, type de pièce), référentiel unique des tiers dans chaque dossier (un fournisseur, un libellé), détection des doublons à l'arrivée, rapprochement automatique pièce – mouvement bancaire ; un propriétaire des règles au pôle technique et un correspondant dans chaque bureau | noms de fichiers libres, tiers en double, 30 000 doublons, rapprochement manuel | le client dépose sans renommer ; il reçoit un accusé de réception et l'alerte « pièce déjà reçue » |
| 4. **Accompagnement des clients et règle commune aux six bureaux** | liste des pièces attendues par client et par mois, visible sur le portail, avec relances automatiques ; portail et application comme canaux normaux dans tous les bureaux, papier réservé à des cas définis et numérisé à l'accueil le jour même ; formation des clients (réunion, tutoriel, premier dépôt accompagné), en commençant par Saintes et Châtellerault ; engagement réciproque inscrit dans la lettre de mission (rythme de dépôt, délai de traitement du cabinet) | 30 % de dossiers incomplets, pratiques différentes selon les bureaux, papier sans limite | le client sait ce qu'il doit déposer et quand ; il est aidé à passer au portail ; il gagne des comptes plus rapides et un suivi en cours d'année |

(0,5 pt pour deux mesures, 1 pt pour quatre, chacune reliée à une faiblesse et à ce qui change pour le client.)

Ces mesures relèvent de l'objectif `2.1.a` : une donnée cohérente (règles, référentiel des tiers), de qualité (contrôle à la source, à l'arrivée) et qui circule sans ressaisie, du client au cabinet. Elles préparent l'offre « Pilotage dirigeant », qui suppose des données mensuelles fraîches. Le secret professionnel reste une contrainte : seules les données utiles à la mission sont collectées, avec l'accord du client pour chaque connexion.

**Réponses tolérées**
- Chaîne présentée selon le vocabulaire décisionnel (collecte, ETL, entrepôt, restitution), ou en six étapes avec la décision du dirigeant comme dernier maillon, si les cinq étapes du programme y figurent.
- Faiblesses qualifiées par les dimensions de la qualité des données (complétude, exactitude, unicité, actualité ; ISO/IEC 25012).
- Doublons ou erreurs de lecture rattachés à la collecte, si le candidat prévoit leur détection à l'arrivée.
- Interopérabilité présentée en quatre niveaux (technique, syntaxique, sémantique, organisationnel) ou en deux (technique et organisationnel), si le sens partagé des données apparaît.
- Rôle du portail public de facturation ou des plateformes agréées mentionné comme contexte, sans analyse des obligations de la réforme.
- Mesures regroupées autrement (une mesure « référentiel des tiers », une mesure « liste des pièces attendues »), si les quatre thèmes de la consigne sont couverts.

**Erreurs fréquentes**
- *Chaîne réduite à un outil* (`JUR-D02` BI réduite à un simple outil ; `ET-05`) — « il suffit d'activer la lecture automatique » ; juste : règles, responsables et contrôles à chaque étape, à commencer par la collecte.
- *Interopérabilité seulement technique* (`ET-36`) — API et formats sans accord du client, sans règle commune aux bureaux ni responsable ; juste : la dimension organisationnelle (clients, bureaux, propriétaire des règles) est demandée.
- *Détail technique des échanges ou modélisation des données* — description des appels d'une API, schéma de tables ; juste : rôle des API et des formats, en principe.
- *Mesures sans le client* (`JUR-T01` contextualiser chaque notion) — organisation pensée pour le cabinet seul ; juste : chaque mesure dit ce que le client fait de différent et ce qu'il y gagne.
- *Analyse juridique de la réforme de la facturation électronique* — obligations, calendrier détaillé, rôle des plateformes ; juste : la réforme est un contexte daté qui rend disponibles des données structurées.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne décisionnelle : collecte, nettoyage, structuration, analyse, restitution | définition et application | F08 § 1 | notion de cours |
| Interopérabilité : niveaux technique, sémantique, organisationnel ; API, formats ouverts | définition, mesures 1 à 3 | F07 § 7 | notion de cours |
| ISO/IEC 25012 (2008) — Modèle de qualité des données | dimensions de la qualité, à titre d'exemple | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| Généralisation de la facturation électronique (article 91 de la loi de finances pour 2024) | factures structurées reçues par les clients depuis le 01/09/2026 | `facturation_electronique_fr` / annexe 2.4 E | en vigueur ; émission des PME au 01/09/2027 |

---

### 2.2 – Méthodes d'analyse et outil d'alerte (3 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique ». Limites : « Le développement d'algorithmes de machine learning n'est pas attendu » ; « L'usage des outils ne dispense pas d'une lecture critique des corrélations et biais ».

**Annexes mobilisées** : annexes 2.2 (offre, outil d'alerte, essai, avis) et 2.1 (flux bancaires, rythme des pièces).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Trois méthodes définies et distinguées (que s'est-il passé ? pourquoi ? que va-t-il se passer ?) | 0,5 |
| a-2 | Chaque méthode rattachée au bon service de l'offre, avec les données mobilisées et le résultat pour le dirigeant | 0,5 |
| b | Quatre angles d'analyse de l'essai, appuyés sur les chiffres de l'annexe 2.2 C ; 0,5 pour deux angles | 1 |
| c-1 | Trois conditions pour une aide à la décision (données, validation humaine et explication, gouvernance et suivi des résultats) | 0,5 |
| c-2 | Position argumentée sur la proposition de M. CHAMPEYRAC (refus de l'ouverture générale et de l'alerte automatique, déploiement progressif et encadré) | 0,5 |

**Réponse attendue**

*2.2 a) – Trois méthodes et trois services*

| Méthode | Définition | Service de l'offre | Données et résultat pour le dirigeant |
|---|---|---|---|
| **Descriptive** | que s'est-il passé ? Agrégats, évolutions, écarts à une référence | **tableau de bord mensuel** | trésorerie, marge brute, délais de paiement des clients et des fournisseurs, comparés au mois précédent et au même mois de l'année précédente : le dirigeant voit sa situation chaque mois au lieu de l'apprendre aux comptes annuels |
| **Exploratoire** | pourquoi ? Croisements, comparaisons, recherche de régularités et de valeurs atypiques | **entretien trimestriel** | marge par activité, par client, par saison ; délais de paiement par client : le chef de mission cherche avec le dirigeant les causes d'un écart (un client qui paie de plus en plus tard, une activité dont la marge se dégrade) ; les pistes sont à vérifier, pas des preuves |
| **Prédictive** | que va-t-il se passer ? Estimation d'une probabilité ou d'une tendance à partir de l'historique | **outil d'alerte** | niveau de risque de difficulté de trésorerie à douze mois, établi par apprentissage automatique : le cabinet peut appeler le dirigeant avant que la difficulté survienne ; il doit en apprécier la fiabilité, non construire le modèle |

(0,5 pt pour les trois définitions ; 0,5 pt pour les trois rattachements appliqués.)

Les trois méthodes s'enchaînent : la prévision ne vaut que si la description est fiable (données fraîches, question 2.1) et si l'exploration a confirmé les facteurs. L'analyse descriptive relève de l'informatique décisionnelle ; l'exploratoire et la prédictive mobilisent la science des données (F08 § 2 ; `ET-25`).

*2.2 b) – Analyse de l'essai sous quatre angles*

1. **Fausses alertes et difficultés non détectées.** Sur 400 clients, 100 alertes : 30 justes, **70 fausses** (sept sur dix) ; 40 clients ont connu une difficulté, dont **10 non détectés** (un sur quatre). L'outil détecte bien (trois difficultés sur quatre, l'argument de M. CHAMPEYRAC), mais il se trompe le plus souvent quand il alerte. Les deux erreurs n'ont pas le même coût : une fausse alerte inquiète un dirigeant à tort et fait perdre du temps aux chefs de mission ; une difficulté manquée prive le client du conseil promis et donne une fausse assurance. Le seuil du niveau élevé règle l'arbitrage entre les deux : l'abaisser détecterait plus de difficultés au prix de plus de fausses alertes.
2. **Corrélation et causalité.** Le modèle repère des clients qui **ressemblent** à ceux qui ont connu des difficultés, il n'explique pas pourquoi (Mme MONTÉGRIER). Le retard de déclaration fait monter le niveau de risque même quand il vient de pièces que le cabinet attendait : la variable mesure en partie l'organisation de la collecte, non la santé du client. Le secteur est associé au risque sans en être la cause : un restaurant en pleine forme est signalé parce qu'il est restaurant.
3. **Biais des données.** **Biais de fraîcheur** : 8 des 10 difficultés manquées concernent des clients sans flux bancaire, dont les pièces arrivent par trimestre ou à la clôture ; l'outil voit mal les clients dont les données sont anciennes, soit 60 % du cabinet (1 800 clients sans flux). **Biais de sélection** : modèle établi sur deux bureaux urbains et trois années ; il a peu vu la clientèle d'artisans, d'exploitations agricoles et d'associations de Saintes et de Châtellerault. **Biais sectoriel** : la restauration et le bâtiment font la moitié des fausses alertes (35 sur 70) pour un cinquième de l'échantillon (80 clients sur 400).
4. **Explicabilité au client.** L'écran affiche un niveau de risque sans les éléments qui l'ont déterminé. Or le conseil suppose d'expliquer : le chef de mission ne peut ni vérifier l'alerte, ni dire au dirigeant ce qu'il doit surveiller (« je ne peux pas appeler un dirigeant… », M. ORTELIER). Un niveau de risque inexpliqué, envoyé automatiquement, nuirait à la relation de confiance que l'offre veut créer.

(0,5 pt pour deux angles appuyés sur les chiffres, 1 pt pour les quatre.)

*2.2 c) – Trois conditions et position*

Trois conditions pour faire de l'outil une **aide à la décision**, non une décision automatique (0,5 pt) :
1. **Des données fraîches et représentatives** : n'appliquer l'outil qu'aux clients dont les données sont à jour (flux bancaire, pièces mensuelles, question 2.1) et l'afficher avec cette précision ; ne pas compter comme retard du client un retard dû au cabinet ; réévaluer le modèle sur les six bureaux et sur une nouvelle année avant de l'étendre.
2. **Un chef de mission qui vérifie, explique et décide** : chaque alerte est d'abord examinée par le chef de mission, qui connaît le dossier ; l'écran affiche les trois ou quatre éléments qui ont le plus pesé (trésorerie en baisse, clients qui paient plus tard) pour qu'il puisse les confronter à sa connaissance du client et les expliquer ; c'est lui qui décide d'appeler le dirigeant.
3. **Une gouvernance et un suivi des résultats** : un responsable de l'outil (l'analyste de données, avec l'associé porteur), une règle sur le seuil d'alerte, une revue trimestrielle des alertes justes, fausses et manquées par secteur et par bureau, et un indicateur de fiabilité suivi dans le temps ; l'accord du client pour cet usage de ses données, dans le respect du secret professionnel.

**Position** (0,5 pt) : il ne faut **pas** ouvrir l'outil à tous les clients dès septembre avec une alerte envoyée automatiquement au dirigeant. Dans les mêmes proportions, les 3 000 clients produiraient environ 750 alertes, dont quelque 525 fausses, à expliquer par une seule analyste et des chefs de mission en pleine reprise d'activité ; et l'outil est le moins fiable pour les clients dont les données sont anciennes, majoritaires. Je recommande de lancer en septembre 2027 le **tableau de bord mensuel** (descriptif, fiable dès que les données sont fraîches), de réserver l'outil d'alerte à un **usage interne** des chefs de mission, d'abord pour les clients à données fraîches de deux ou trois bureaux, puis de l'ouvrir aux clients, comme support d'un échange avec le chef de mission, quand la revue des résultats aura montré moins de fausses alertes et que le flux bancaire sera généralisé.

**Réponses tolérées**
- Analyse **diagnostique** citée pour l'entretien trimestriel, à la place de l'exploratoire ou en complément ; analyse **prescriptive** mentionnée comme prolongement.
- Lecture des résultats en termes de « faux positifs » et « faux négatifs », de précision et de rappel, sans calcul au-delà des lectures de tête de l'annexe.
- Biais présentés comme un **biais de confirmation** possible du chef de mission (ne retenir que les alertes qui confirment son opinion), en plus des biais des données.
- Position favorable à une ouverture rapide, si elle est limitée à des clients volontaires à données fraîches, sans alerte automatique et avec validation par le chef de mission.
- Condition de sobriété des données : ne collecter que les données nécessaires à l'outil.

**Erreurs fréquentes**
- *Corrélation présentée comme causalité* (`ET-26` ; `JUR-D06` prudence d'interprétation) — « les restaurants sont en difficulté » ; juste : le secteur est un facteur associé, le niveau de risque désigne des ressemblances.
- *« Trois sur quatre détectées » pris pour la fiabilité de l'outil* — sans voir que sept alertes sur dix sont fausses ; juste : lire les deux erreurs et leur coût.
- *Construction d'un modèle prédictif* — choix d'algorithme, variables à ajouter, paramétrage ; juste : apprécier la fiabilité et les conditions d'usage (limite du programme).
- *Outil d'alerte confondu avec l'IA générative* (`ET-09`) — « l'outil rédige l'alerte » ; juste : apprentissage automatique qui classe les clients par niveau de risque.
- *Analyse juridique* — droit des entreprises en difficulté, procédures, obligations déontologiques ; juste : analyse de la donnée et de son usage pour conseiller.
- *Méthodes récitées sans application* (`JUR-T01`) — descriptive, exploratoire, prédictive définies sans les trois services.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Méthodes d'analyse descriptive, exploratoire, prédictive, prescriptive ; BI et science des données | association aux trois services | F08 § 2 | notion de cours |
| Corrélation et causalité, biais de sélection, de fraîcheur et de confirmation | analyse de l'essai | F08 § 5 | notion de cours |
| Apprentissage automatique : classement par niveau de risque, biais, explicabilité, revue des résultats | outil d'alerte, conditions | F13 § 1 et 3 | notion de cours |

---

### 2.3 – Diagnostic de la production et restitution au comité des associés (2 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.d` « Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ». Limites : « L'usage des outils ne dispense pas d'une lecture critique des corrélations et biais » ; « L'interprétation doit être reliée à la stratégie globale ».

**Annexes mobilisées** : annexes 2.3 (indicateurs par bureau, précisions, outils) et 2.4 (honoraires, objectifs 2029).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux constats chiffrés, chacun avec une hypothèse d'explication tirée des précisions de l'annexe 2.3 B | 0,5 |
| a-2 | Deux précautions de lecture tirées des annexes et conclusion reliée au plan « CORLANDEAU 2030 », en douze lignes au maximum | 0,5 |
| b-1 | Une représentation adaptée à chaque constat et au comité des associés (message, type de graphique, comparaison et cible) | 0,5 |
| b-2 | Outil de visualisation recommandé et justifié par le cas (sources, rafraîchissement, une seule définition), avec ses conditions (démarche, définitions communes, compétences) | 0,5 |

**Réponse attendue**

*2.3 a) – Diagnostic argumenté (note modèle)*

<!-- note -->
Constat 1 : là où le portail est adopté, la saisie recule. À Poitiers, Niort et La Rochelle, 80 % des clients l'utilisent et la saisie est passée de 12 à 8 h par client ; à Saintes et à Châtellerault, le portail stagne à 25 % et la saisie reste à 15 h. Hypothèse : le portail et la lecture automatique suppriment de la saisie, mais une clientèle d'artisans, d'exploitations et d'associations dépose encore sur papier. Constat 2 : le temps libéré ne devient pas du conseil. Pour le même gain de 4 h, le conseil passe de 7 % à 14 % à La Rochelle, de 7 % à 8 % à Poitiers et à Niort. Hypothèse : seule La Rochelle a réorganisé son travail (cellule dédiée, formation). Précautions : ce sont des associations entre bureaux de taille et de clientèle différentes, pas des causes ; la part du conseil monte aussi quand la tenue baisse (−0,5 M€) : la lire avec son montant ; le délai de Niort tient à des départs et à une autre définition. Conclusion : le portail ne suffit pas, il faut organiser le conseil.
<!-- /note -->

(0,5 pt pour les deux constats et leurs hypothèses ; 0,5 pt pour deux précautions et la conclusion.)

*2.3 b) – Représentations et outil décisionnel*

| Constat | Message pour le comité | Représentation | Pourquoi |
|---|---|---|---|
| 1. Portail et saisie | « là où le portail est utilisé, la saisie recule » | **nuage de points** : taux d'utilisation du portail en abscisse, heures de saisie par client en ordonnée, une bulle par bureau proportionnelle au nombre de clients, une flèche de 2025 à 2026, la cible de 6 h en ligne horizontale ; ou barres triées par bureau | montre la relation entre deux variables et la trajectoire de chaque bureau ; la cible situe l'effort restant ; le titre rappelle qu'il s'agit d'une association |
| 2. Temps libéré et conseil | « le temps libéré ne devient du conseil que là où le bureau s'est organisé » | **barres groupées** par bureau : part des honoraires de conseil en 2025 et 2026, axe partant de zéro, ligne de la cible de 20 % en 2030 ; en appui, le gain d'heures de saisie de chaque bureau | compare des catégories et l'écart à la cible ; l'axe à zéro évite d'amplifier des écarts d'un point |

(0,5 pt pour deux représentations adaptées.)

**Outil recommandé** (0,5 pt) : l'**outil de visualisation** déjà acquis (12 k€ par an, 15 licences, trois utilisateurs), plutôt que les six classeurs de tableur. Il se connecte directement au logiciel de production et au logiciel de temps, rafraîchit les données chaque nuit et publie un même tableau de bord pour tout le comité, au lieu d'une synthèse refaite à la main chaque trimestre à partir de six classeurs aux définitions différentes. Conditions : la décision n'est pas d'acheter un outil mais de conduire une démarche décisionnelle : des définitions communes à tous les bureaux (le délai court jusqu'à l'envoi des comptes partout, y compris à Niort), un responsable des données de production, des utilisateurs formés au-delà de l'analyste et de deux associés. Le tableur reste utile aux analyses ponctuelles d'un bureau.

**Réponses tolérées**
- Constats différents s'ils sont chiffrés et tirés de l'annexe 2.3 : délai des comptes annuels plus court là où la dématérialisation progresse (Poitiers, La Rochelle), écart persistant entre les bureaux urbains et ceux de Saintes et de Châtellerault.
- Hypothèse du constat 1 fondée sur l'activation des flux bancaires ou sur l'obligation du portail pour les nouveaux clients à Poitiers (annexe 2.1 B).
- Précautions différentes : deux années seulement, moyennes par bureau qui masquent la dispersion entre collaborateurs, heures déclarées et non mesurées.
- Une seule représentation de type tableau de bord d'une page réunissant les deux graphiques, ou des petits graphiques identiques par bureau, si chaque constat y trouve sa représentation.
- Tableur avancé retenu pour une phase transitoire, si ses limites sont montrées (classeurs multiples, saisie manuelle, définitions divergentes).

**Erreurs fréquentes**
- *Corrélation présentée comme causalité* (`ET-26` ; `JUR-D06`) — « le portail fait baisser les heures de saisie, donc il suffit de l'imposer » ; juste : association entre bureaux, clientèles différentes.
- *Part du conseil lue sans son dénominateur* — hausse attribuée au seul développement du conseil alors que les honoraires de tenue baissent.
- *Diagnostic sans lien avec la stratégie* (limite du programme) — chiffres commentés sans conclusion sur le plan « CORLANDEAU 2030 ».
- *BI réduite à un outil* (`JUR-D02` ; `ET-05`) — « l'outil de visualisation résoudra le problème » ; juste : définitions communes, responsables, compétences.
- *Manipulation d'outil* — étapes de construction du graphique dans le logiciel ; juste : choix argumenté sur papier.
- *Représentation inadaptée* — secteurs pour comparer six bureaux, axe tronqué pour des écarts d'un point.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Choix du graphique selon le message, biais de lecture, corrélation et causalité | diagnostic, représentations | F08 § 5 | notion de cours |
| Outils décisionnels : fonctions, limites, critères de choix ; BI comme démarche | recommandation de l'outil | F08 § 6 | notion de cours |

---

### 2.4 – Indicateurs de pilotage de la transformation de la production (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ». Limite : « Le pilotage stratégique par les indicateurs suppose une capacité de recul critique ».

**Annexes mobilisées** : annexes 2.4 (objectifs fin 2029, coût horaire, honoraires), 2.1 (canaux, dossiers incomplets, flux bancaires) et 2.3 (heures de saisie, délais).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Tableau de bord équilibré défini (ensemble restreint d'indicateurs reliés à un objectif, équilibrant résultats et leviers, performance, risques et coûts ; Balanced Scorecard) et équilibre du choix justifié | 0,5 |
| 2 | Quatre indicateurs complets (formule, source, fréquence, cible tirée des annexes, axe), pertinents pour la transformation de la production et couvrant performance, risques et coûts ; 1 pour trois, 0,5 pour deux | 1,5 |

**Réponse attendue**

Un **tableau de bord équilibré** est un ensemble restreint d'indicateurs choisis pour piloter un objectif, présentés pour décider (cible, tendance, responsable) ; dans l'esprit du Balanced Scorecard (Kaplan et Norton, 1992), décliné au SI par l'IT Balanced Scorecard (Van Grembergen), il équilibre les résultats et leurs leviers, et, pour un projet de transformation, la performance, les risques et les coûts (F09 § 4) (0,5 pt). Celui de la transformation de la production relie la chaîne de collecte (question 2.1) à l'objectif du plan : libérer du temps pour le conseil.

| Dimension | Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|---|
| Performance (levier) | Taux d'intégration automatique des pièces | pièces intégrées automatiquement dans les dossiers, sans ressaisie / pièces reçues sur la période | logiciel de production comptable (journal de la lecture automatique et des flux) | mensuelle | 80 % fin 2029 (220 000 pièces sur 600 000 en 2026, un peu plus d'une sur trois) | processus |
| Coûts | Coût de saisie et de rapprochement par client | heures de saisie et de rapprochement déclarées sur douze mois × coût horaire moyen chargé (50 €) / nombre de clients en tenue | logiciel de temps ; coût horaire issu de la paie du cabinet | trimestrielle, sur douze mois glissants | 300 € fin 2029 (6 h × 50 €), contre 500 € en 2026 (10 h × 50 €) | financier |
| Risques (qualité des données) | Taux de dossiers incomplets à la clôture | dossiers auxquels manquent des pièces de la liste des pièces attendues à la date de clôture / dossiers en tenue | logiciel de production comptable (liste commune des pièces attendues et suivi des relances) | mensuelle de janvier à mai, bilan annuel | 10 % fin 2029 (30 % à la clôture 2026), suivi par bureau et par canal principal | processus |
| Performance (résultat) | Part des honoraires de conseil dans le chiffre d'affaires | honoraires de conseil aux dirigeants facturés / honoraires totaux du cabinet | facturation et comptabilité du cabinet | trimestrielle, cumul sur douze mois | 20 % en 2030 (7 % en 2025, 9 % en 2026) | financier |

(0,5 pt par indicateur complet et pertinent au-delà du premier : 1,5 pt pour quatre, 1 pt pour trois, 0,5 pt pour deux.)

Les deux premiers mesurent le levier de la transformation et son coût, le troisième le principal risque (des données incomplètes, qui retardent les comptes et faussent le conseil), le quatrième le résultat attendu par le plan. Lu ensemble, le tableau de bord évite le piège du constat 2 de la question 2.3 : des heures de saisie en baisse sans hausse du conseil signalent un temps libéré non réinvesti. Le quatrième indicateur se lit avec le montant des honoraires de conseil, car sa part monte aussi quand les honoraires de tenue baissent.

**Réponses tolérées**
- Part des clients dont les relevés bancaires arrivent par flux automatisé (clients dont le flux est actif / clients en tenue, cible 80 % fin 2029), délai moyen de remise des comptes annuels (cible 75 jours), taux de départ des clients (axe client, cible sous 5 % : 150 TPE parties en 2026), part des chefs de mission formés à l'entretien de conseil (axe apprentissage), à la place d'un des indicateurs du corrigé.
- Heures de saisie par client (cible 6 h) comme indicateur de performance, si le coût est suivi par un autre indicateur.
- Taux d'erreurs de lecture automatique (pièces corrigées / pièces lues automatiquement, une sur dix en 2026) comme indicateur de risque, avec une cible justifiée.
- Taux de dossiers incomplets rattaché à l'axe client ; part du conseil rattachée à l'axe client.

**Erreurs fréquentes**
- *Indicateurs incomplets ou génériques* (`JUR-A02` distinguer et justifier les indicateurs ; `ET-18`) — « taux de dématérialisation » sans formule, source, fréquence ni cible ; juste : cinq champs, cibles du séminaire (annexe 2.4 C).
- *Tableau de bord limité à la performance* (`ET-18`) — aucun indicateur de risque ni de coût, contrairement à la consigne.
- *Indicateurs du SI technique* — disponibilité des serveurs, tickets d'assistance ; juste : indicateurs de la transformation de la production.
- *Calcul d'écarts budgétaires ou tarification* — décomposition d'écarts, prix de l'offre ; juste : rapports simples de deux chiffres ronds.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Balanced Scorecard (Kaplan et Norton, 1992) ; IT Balanced Scorecard (Van Grembergen) | tableau de bord équilibré | `van_grembergen_it_bsc` / F09 § 4.1 | modèle publié |
| Fiche d'indicateur à cinq champs ; tableau de bord restreint | indicateurs | F08 § 3 ; F09 § 4 | notion de cours |

---

### 2.5 – Modèle économique et stratégie du système d'information (3 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.d` « Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limites : « Ne pas confondre alignement stratégique et simple adéquation technique » ; « Ne pas se limiter à une veille passive : intégrer l'analyse prospective dans l'évaluation des opportunités SI ».

**Annexes mobilisées** : annexes 2.4 (honoraires, concurrence, attentes, temps, budget du SI, objectifs, positions, repères), 1.1 (plan « CORLANDEAU 2030 »), 2.1 (offre de l'éditeur), 2.2 (offre « Pilotage dirigeant ») et 2.3 (bureaux).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Modèle économique défini (manière dont l'organisation crée de la valeur pour ses clients, la produit avec ses ressources et en tire ses revenus) | 0,5 |
| a-2 | Effets de l'automatisation et des données analysés sous les trois angles, chacun appuyé sur l'annexe 2.4 ; 0,5 pour deux angles | 1 |
| b-1 | Alignement stratégique défini (mise en cohérence permanente et réciproque de la stratégie du SI et de la stratégie de l'organisation), sans le réduire à un choix d'outil ; la référence au modèle SAM est valorisée sans être exigée | 0,5 |
| b-2 | Trois priorités hiérarchisées, chacune justifiée par les annexes et reliée à l'objectif de développer le conseil ; 0,5 pour deux | 1 |

**Réponse attendue**

*2.5 a) – Effet de l'automatisation et des données sur le modèle économique*

Le **modèle économique** décrit la manière dont une organisation crée de la valeur pour ses clients (proposition de valeur), la produit avec ses ressources et ses activités clés, et en tire ses revenus. Les technologies de l'automatisation et de la donnée le transforment : il s'agit d'en analyser l'impact, dans une démarche de veille active, pour orienter la stratégie (F01 § 0) (0,5 pt).

| Angle | Modèle actuel | Effet de l'automatisation de la saisie | Effet de l'exploitation des données |
|---|---|---|---|
| **Proposition de valeur** | produire des comptes et des déclarations fiables, une fois l'an | la tenue devient une commodité : les plateformes en ligne la proposent pour moins de 100 € par mois ; 150 TPE sont parties en 2026 ; la valeur ne tient plus à la saisie | une valeur nouvelle : aider le dirigeant à décider en cours d'année ; 60 % des clients veulent un point régulier sur leur trésorerie, 45 % jugent que le cabinet intervient trop tard, 30 % paieraient un tableau de bord mensuel |
| **Ressources** | des collaborateurs qui consacrent un quart de leur temps à la saisie, au rapprochement et aux relances ; un SI centré sur la production (80 % du budget pour faire fonctionner l'existant) | du temps libéré : 4 heures de moins par client si l'objectif de 6 h est atteint, soit environ 12 000 heures par an sur 3 000 clients ; mais il ne devient du conseil que là où le bureau s'organise (La Rochelle, annexe 2.3) | de nouvelles ressources clés : des données fraîches et fiables (flux, formats structurés), des compétences d'analyse (une seule analyste aujourd'hui), des chefs de mission formés à l'entretien, la confiance des clients qui confient leurs données, sous la contrainte du secret professionnel |
| **Revenus** | des honoraires de tenue forfaitaires (14 M€, 64 % des honoraires), en baisse (−0,5 M€ en 2026, −10 % sur le forfait d'une TPE en deux ans) | pression continue sur les forfaits : le gain de productivité est capté par les clients si le cabinet ne fait que baisser ses coûts | des revenus de conseil récurrents, sur abonnement (2 M€ en 2026, 9 % ; objectif 20 % en 2030) : moins dépendants du volume de pièces et mieux protégés de la concurrence des plateformes |

(0,5 pt pour deux angles, 1 pt pour les trois, appuyés sur l'annexe 2.4.)

Le débat du séminaire en découle : automatiser pour baisser les coûts (Mme FERNIAC) protège un temps la tenue mais aligne le cabinet sur des concurrents moins chers ; s'appuyer sur les données pour vendre du conseil (M. CHAMPEYRAC) change la proposition de valeur mais suppose des ressources que le cabinet n'a pas encore. Les deux se complètent : l'automatisation finance et libère le temps du conseil.

*2.5 b) – Stratégie du SI alignée et trois priorités*

L'**alignement stratégique** est la mise en cohérence permanente et réciproque de la stratégie du SI avec la stratégie de l'organisation. Le modèle SAM de Henderson et Venkatraman (1993) peut l'éclairer, sans être exigé : la technologie peut aussi ouvrir une stratégie nouvelle. Il ne se réduit ni à un choix d'outil ni à une standardisation logicielle (F01 § 1) (0,5 pt). Ici, la stratégie métier est fixée : faire du conseil un relais de croissance, sans perdre la tenue. Mme VARENNAT ne veut pas « un projet informatique de plus » : le SI doit être réorienté de la production vers la donnée.

Trois priorités, dans l'ordre (1 pt) :
1. **Fiabiliser et fluidifier la collecte des données des clients** (priorité absolue, condition des deux autres) : activer les connexions déjà comprises dans l'abonnement (flux bancaires pour 80 % des clients, factures structurées, logiciels de caisse), règles communes de nommage, de rapprochement et de pièces attendues dans les six bureaux (question 2.1). Justification : sans données fraîches, ni le tableau de bord mensuel ni l'outil d'alerte ne fonctionnent (8 difficultés manquées sur 10 chez des clients sans flux) ; c'est aussi le moyen d'atteindre 6 h de saisie par client et de résister aux plateformes.
2. **Construire un socle décisionnel commun au service du conseil** : un entrepôt de données de production et de clients alimenté automatiquement, des définitions partagées, l'outil de visualisation déjà acquis comme couche de restitution pour le comité et pour les clients (tableau de bord mensuel), des compétences d'analyse renforcées au-delà d'une seule analyste et un responsable des données. Justification : l'offre « Pilotage dirigeant » et le pilotage de la transformation (questions 2.3 et 2.4) reposent sur la même donnée ; aujourd'hui, six classeurs et des définitions divergentes.
3. **Mettre le SI au service d'un nouveau métier de conseil, avec des règles d'usage des données** : outils du chef de mission (préparation de l'entretien trimestriel, alertes expliquées et validées), accord des clients et respect du secret professionnel, revue des résultats de l'outil d'alerte, veille active sur les plateformes concurrentes et les usages des données ; rééquilibrer le budget du SI au profit des projets (20 % aujourd'hui). Justification : le conseil vendu sur la base des données des clients engage la confiance ; l'exemple de La Rochelle montre que le temps libéré ne devient du conseil que s'il est organisé.

Cet ordre répond aux deux positions du séminaire : la première priorité sert l'automatisation de la tenue voulue par Mme FERNIAC, les deux suivantes le conseil voulu par M. CHAMPEYRAC, dans une même trajectoire.

**Réponses tolérées**
- Modèle économique présenté en neuf blocs (proposition de valeur, segments de clients, canaux, relations, flux de revenus, ressources clés, activités clés, partenaires, structure de coûts), si les trois angles demandés sont appliqués au cas.
- Analyse par la chaîne de valeur (Porter, 1985) : l'automatisation fait de la production une activité de commodité, la valeur se déplace vers le conseil.
- Priorités ordonnées autrement (socle décisionnel avant la collecte), si la dépendance entre la qualité des données et l'offre de conseil est explicitée.
- Référence au modèle SAM et à l'une de ses perspectives d'alignement, valorisée si elle est appliquée au cas.
- Une priorité consacrée aux compétences (analystes, formation des chefs de mission au conseil et à la lecture des données), si elle reste une priorité de la stratégie du SI et non un plan de formation détaillé.

**Erreurs fréquentes**
- *Alignement réduit à un choix d'outil* (`ET-06` ; `JUR-G02`) — « la stratégie consiste à généraliser l'outil de visualisation » ; juste : priorités dérivées de l'objectif de développer le conseil.
- *Modèle économique décrit sans effet des technologies* (`JUR-T03` analyser et argumenter) — description du cabinet sans analyse de ce que l'automatisation et les données changent.
- *Opportunités sans risques* (`ET-19`) — conseil fondé sur les données présenté comme acquis, sans les compétences, la qualité des données ni la confiance des clients.
- *Schéma directeur complet* (`ET-07`) — diagnostic, cible, portefeuille et budget de tout le SI ; juste : trois priorités hiérarchisées.
- *Tarification de l'offre ou calcul de rentabilité* — prix de l'abonnement, retour sur investissement ; juste : analyse qualitative appuyée sur les ordres de grandeur de l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Strategic Alignment Model (Henderson et Venkatraman, 1993) | stratégie du SI alignée, référence valorisée sans être exigée | `henderson_venkatraman_1993` / F01 § 1 | modèle publié |
| Chaîne de valeur (Porter, 1985) | réponse tolérée | `porter_chaine_valeur_1985` / F01 § 2 | modèle publié |
| Veille active et analyse de l'impact des technologies sur le modèle économique | effet de l'automatisation et des données | F01 § 0 (1.1.d) | notion de cours |
| DAMA-DMBOK, 2e édition (2017) | gouvernance des données du socle décisionnel, à titre d'exemple | `dama_dmbok2` / F07 § 8.2 | en vigueur |
