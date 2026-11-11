# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 10 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données et gouvernance, F08 décisionnel et visualisation, F09 performance du SI, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Chaîne de traitement des données de pertes | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution | 3 |
| 1.2 Méthodes d'analyse | `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique | 3 |
| 1.3 Diagnostic, visualisations et outil décisionnel | `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. | 4 |
| 1.4 Tableau de bord du programme | `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ; `3.1.e` Revue et amélioration continue des dispositifs de pilotage | 4 |
| **Dossier 1 – Exploiter les données de télérelève pour réduire les pertes et piloter le programme** |  | **14** |

Répartition indicative : connaissances (définitions de la chaîne de traitement et des méthodes d'analyse, principes de choix d'une représentation et d'un outil, structure d'un tableau de bord) 2,75 points (items 1.1 a-1, 1.1 a-2 pour moitié, 1.2 a pour un tiers, 1.3 c-2 pour moitié, 1.4 a pour un quart, 1.4 c pour moitié) ; analyse des annexes et recommandations 11,25 points, soit environ 80 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – Chaîne de traitement des données de pertes (3 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ».

**Annexes mobilisées** : annexes 1.1 (télérelève, réseau, plan « MORVÈZE EAU 2032 »), 1.2 (sources, défauts constatés, outils actuels) et 1.3 (volumes, secteurs).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de traitement définie (suite organisée d'étapes qui transforme des données brutes de sources hétérogènes en informations fiables restituées pour décider), avec l'idée que sa valeur dépend de son maillon le plus faible | 0,5 |
| a-2 | Cinq étapes décrites dans l'ordre et appliquées aux sources de l'annexe 1.2 ; 0,5 pour trois étapes appliquées | 1 |
| b-1 | Trois défauts rattachés à la bonne étape, chacun avec un traitement précis (à la source et dans la chaîne) ; 0,5 pour deux défauts | 1 |
| b-2 | Conséquence démontrée sur les décisions de la régie (secteur prioritaire, affectation de l'équipe de recherche de fuites, renouvellement, compte rendu au conseil d'administration) | 0,5 |

**Réponse attendue**

*1.1 a) – Définition et application aux sources*

La **chaîne de traitement des données** est la suite organisée des opérations qui transforment des données brutes, issues de sources hétérogènes, en informations fiables, structurées et restituées à ceux qui décident : collecte, nettoyage, structuration, analyse, restitution. Elle relève d'une démarche décisionnelle, et non d'un outil : chaque étape a ses règles, ses responsables et ses contrôles, et la valeur de l'ensemble se perd au maillon le plus faible (F08 § 1) (0,5 pt).

| Étape | Application aux données de pertes de la régie |
|---|---|
| **Collecte** | index quotidiens des 60 000 compteurs en télérelève (plateforme du prestataire) ; index semestriels des 100 000 autres compteurs (logiciel de facturation) ; volumes entrant dans les cinq secteurs, mesurés toutes les quinze minutes par 40 débitmètres (supervision) ; fiches de casse et de réparation (logiciel des interventions) ; caractéristiques des canalisations (base patrimoniale). La collecte est automatisée et régulière : extraction quotidienne de la plateforme, de la supervision et des interventions au lieu de copies manuelles mensuelles |
| **Nettoyage** | repérage et traitement des index manquants (3 000 par jour), des index aberrants (2 000 par mois), des valeurs de débitmètres manquantes ou remplacées ; contrôle de complétude des fiches de casse ; chaque correction est tracée dans un journal des rejets et des corrections |
| **Structuration** | rattachement de chaque compteur, de chaque débitmètre et de chaque tronçon à un secteur, selon un référentiel unique et daté des secteurs ; agrégation à un même pas de temps (jour, mois, douze mois glissants) ; historisation dans une base décisionnelle commune (entrepôt de données), qui remplace la dizaine de classeurs et les trois listes de secteurs |
| **Analyse** | bilan des volumes entrés et consommés par secteur, suivi du débit nocturne, croisement des pertes et des casses avec l'âge, le matériau et la densité des abonnés, anticipation des casses (question 1.2) |
| **Restitution** | tableaux de bord adaptés aux destinataires : équipes de l'exploitation chaque matin, directrice générale avant chaque comité de direction, conseil d'administration chaque trimestre (questions 1.3 et 1.4), au lieu d'un rapport établi à la main en deux jours et diffusé vers le 20 du mois suivant |

(1 pt pour les cinq étapes appliquées ; 0,5 pt pour trois.)

*1.1 b) – Trois défauts, leur étape et leur traitement*

| Défaut (annexe 1.2 B) | Étape concernée | Traitement à prévoir |
|---|---|---|
| **3 000 compteurs muets chaque jour**, dont 600 depuis plus d'un mois ; jours manquants laissés vides | collecte et nettoyage | à la source : liste quotidienne des compteurs muets transmise aux équipes pour remplacer piles et émetteurs (les 600 muets depuis un mois d'abord) ; dans la chaîne : valeur manquante complétée par une estimation signalée comme telle (interpolation entre deux index reçus), jamais par un zéro, et taux de complétude publié avec chaque résultat |
| **2 000 index aberrants par mois** | nettoyage | règles de détection documentées (index en baisse, consommation journalière supérieure à un seuil) ; mise en quarantaine et vérification plutôt que suppression d'office, car certains révèlent de vraies fuites après compteur, à signaler à l'abonné ; correction tracée |
| **Lotissement des Prés-Hauts** (2 000 abonnés, 0,2 million de m³) alimenté par les Faubourgs nord mais rattaché au Plateau est | structuration | référentiel unique et daté des secteurs, avec un propriétaire (le bureau d'études) et une procédure de mise à jour à chaque modification du réseau, que la facturation, l'exploitation et le bureau d'études utilisent tous ; recalcul des bilans 2025 et 2026 des deux secteurs |
| **4 débitmètres en panne** plus d'un mois, valeurs remplacées à la main sans signalement | collecte et nettoyage | alerte automatique de panne, réparation prioritaire ; valeur de remplacement marquée comme estimée et conservée à côté de la valeur mesurée |
| **30 % des fiches de casse incomplètes**, ressaisies avec deux à trois semaines de retard | collecte | correction à la source : saisie sur tablette au moment de l'intervention, adresse localisée automatiquement, matériau et diamètre obligatoires (repris de la base patrimoniale), fin des fiches papier |
| **Date de pose inconnue pour 25 % du linéaire** | collecte et structuration | complétude progressive de la base patrimoniale à chaque intervention ; âge publié avec la part du linéaire couverte |

(1 pt pour trois défauts traités ; 0,5 pt pour deux.)

**En quoi la maîtrise de la chaîne conditionne les décisions** (0,5 pt) : les décisions du plan reposent directement sur ces données ; un maillon défaillant les fausse. Avec le lotissement mal rattaché, les pertes des Faubourgs nord sont surestimées d'environ 0,2 million de m³ (1,4 au lieu de 1,6) et celles du Plateau est sous-estimées d'autant (0,9 au lieu de 0,7) : l'équipe de recherche de fuites (0,6 M€ par an) risque d'être envoyée au mauvais endroit, ce que redoute M. SALVANHAC. Les fiches de casse incomplètes empêchent de cibler le renouvellement des canalisations ; les compteurs muets et les estimations semestrielles rendent incertain le bilan de chaque secteur ; le conseil d'administration recevrait un chiffre de pertes évitées qu'on ne saurait justifier. La qualité de la chaîne est donc une condition de la crédibilité du programme (11,7 M€ sur trois ans) et de l'objectif de 3,5 millions de m³ en 2029.

**Réponses tolérées**
- Chaîne présentée selon le vocabulaire décisionnel (collecte, ETL — extraction, transformation, chargement —, entrepôt, restitution) ou en six étapes, avec la décision et l'action en dernier maillon, si les cinq étapes du programme y figurent.
- Dimensions de la qualité des données nommées d'après ISO/IEC 25012 (complétude, exactitude, cohérence, actualité) pour qualifier les défauts.
- Défauts différents de ceux du corrigé, dès lors qu'ils sont tirés de l'annexe 1.2 et rattachés à la bonne étape.
- Fiches de casse incomplètes rattachées à l'étape de nettoyage, si le candidat prévoit aussi la correction à la source.

**Erreurs fréquentes**
- *Chaîne de traitement réduite à un outil* (`JUR-D02` BI réduite à un simple outil ; `ET-05`) — « il suffit d'acheter un logiciel de visualisation » ; juste : règles, responsables et contrôles à chaque étape.
- *Étape du nettoyage ou de la structuration oubliée* (`JUR-D01` chaîne de valeur de la BI) — alors que c'est le maillon faible du cas ; juste : cinq étapes, le nettoyage et le référentiel des secteurs au centre.
- *Suppression des valeurs aberrantes sans vérification* — une consommation anormale peut être une fuite chez l'abonné ; juste : quarantaine, vérification, trace.
- *Morceau de cours* (`JUR-T01` contextualiser chaque notion) — étapes récitées sans les compteurs muets, le lotissement ni les fiches de casse ; juste : chaque étape porte un exemple tiré de l'annexe 1.2.
- *Modélisation de données détaillée* — schéma de tables ou de clés pour l'entrepôt ; juste : la structuration est décrite dans son principe (référentiel des secteurs, pas de temps commun, historisation).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne décisionnelle : collecte, ETL, entrepôt, restitution ; qualité d'un extrait (valeurs manquantes, aberrantes, incohérences) | étapes, traitements, correction à la source | F08 § 1 et 4 | notion de cours |
| Données de référence et référentiel unique | référentiel des secteurs | F07 § 1 | notion de cours |
| ISO/IEC 25012 (2008) — Modèle de qualité des données | dimensions de la qualité, à titre d'exemple | `iso_iec_25012` / F07 § 8.3 | en vigueur |

---

### 1.2 – Méthodes d'analyse (3 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique ». Limite : « Le développement d'algorithmes de machine learning n'est pas attendu. »

**Annexes mobilisées** : annexes 1.2 (sources, défauts), 1.3 (volumes, secteurs, questions de la directrice générale) et 1.4 (objectifs 2029, équipe de recherche de fuites).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Question 1 → analyse **descriptive**, avec données mobilisées et résultat attendu | 0,5 |
| a-2 | Question 2 → analyse **exploratoire**, avec données mobilisées et résultat attendu | 0,5 |
| a-3 | Question 3 → analyse **prédictive**, avec données mobilisées et résultat attendu, la prévision étant interprétée et non construite | 0,5 |
| b-1 | Première limite tirée des annexes : corrélation n'est pas causalité (âge des canalisations et densité des abonnés, débit nocturne de la zone d'activités) | 0,5 |
| b-2 | Seconde limite tirée des annexes : biais des données manquantes ou inégales (télérelève de 10 % à 70 % selon les secteurs, compteurs muets, dates de pose inconnues, fiches incomplètes, historique court) | 0,5 |
| b-3 | Conséquence des limites pour la décision et précaution proposée (vérification sur le terrain, comparaison de secteurs semblables, part des données couvertes publiée) | 0,5 |

**Réponse attendue**

*1.2 a) – Une méthode par question*

| Question de la directrice générale | Méthode | Données mobilisées | Résultat attendu |
|---|---|---|---|
| 1. Où et combien perdons-nous d'eau ? | **descriptive** : que s'est-il passé ? Agrégats, répartitions, évolutions, écarts à une cible | volumes mis en distribution (25 millions de m³), consommations relevées ou estimées (20 millions), volumes entrant dans chaque secteur, débit nocturne, longueur des secteurs | pertes par secteur en volume et rapportées au kilomètre de canalisation, sur douze mois glissants, et leur évolution : 5 millions de m³ en 2026, dont 64 % dans le Centre ancien et les Faubourgs nord |
| 2. Quels facteurs semblent liés aux pertes ? | **exploratoire** : pourquoi ? Croisements, comparaisons, recherche de régularités et de valeurs atypiques | pertes par km, casses pour 100 km, âge et matériau des canalisations (base patrimoniale), densité des abonnés, causes des casses (fiches d'intervention) | facteurs associés aux pertes à confirmer : pertes et casses plus élevées là où le réseau est ancien et dense ; pistes à vérifier sur le terrain, pas une démonstration |
| 3. Pouvons-nous anticiper les casses des deux prochaines années ? | **prédictive** : que va-t-il se passer ? Estimation, pour chaque tronçon, d'un risque de casse à deux ans | historique des casses de plusieurs années, caractéristiques des tronçons (âge, matériau, diamètre), débits | classement des tronçons par niveau de risque, qui oriente le programme de renouvellement et le planning de l'équipe de recherche de fuites ; la régie n'a pas à construire le modèle, mais à en apprécier la fiabilité et à le confronter aux constats des équipes |

(0,5 pt par ligne complète : méthode juste, données et résultat appliqués au cas.)

Les trois méthodes s'enchaînent : la prévision n'a de valeur que si la description est fiable et si l'exploration a validé les facteurs. Une analyse prescriptive (quel tronçon renouveler en premier, à budget donné) peut prolonger la démarche.

*1.2 b) – Deux limites qui ressortent des annexes*

1. **Corrélation n'est pas causalité** (0,5 pt). Les pertes par km suivent l'âge des canalisations dans les secteurs urbains (8 milliers de m³ par km pour 55 ans dans le Centre ancien, 1 millier pour 20 ans dans la zone d'activités), mais les Coteaux sud, dont le réseau a 40 ans, perdent le moins par km (0,8) : l'âge n'explique pas tout. Le Centre ancien est aussi le plus dense (250 abonnés par km, contre 30 dans les Coteaux sud) : les branchements, nombreux en ville, sont un facteur commun possible. De même, le débit nocturne de la zone d'activités comprend la consommation de nuit de trois usines, qui n'est pas une fuite. Conclure « renouveler les canalisations les plus anciennes réduira les pertes » sans contrôler la densité serait une causalité supposée.
2. **Biais des données manquantes ou inégales** (0,5 pt). La télérelève couvre 60 % des abonnés du Centre ancien mais 10 % des Coteaux sud et 20 % des Faubourgs nord : ailleurs, les consommations sont relevées deux fois par an ou estimées sur l'année précédente, de sorte que les pertes de ces secteurs sont les moins sûres, et le sont davantage les années de sécheresse, quand la consommation change. S'y ajoutent les 3 000 compteurs muets par jour, l'âge calculé sur 75 % du linéaire seulement, 30 % de fiches de casse sans localisation ni matériau et un historique de casses fiable sur peu d'années : une prévision construite sur ces données reproduirait leurs lacunes et surestimerait le risque là où les données sont les mieux tenues.

**Conséquence et précaution** (0,5 pt) : ces analyses orientent la recherche de fuites et le renouvellement, elles ne les décident pas seules ; chaque résultat est publié avec la part des données qu'il couvre, comparé entre secteurs semblables (urbains denses entre eux), puis vérifié sur le terrain (campagne de recherche de fuites ciblée) avant d'engager des travaux ; la prévision des casses est réévaluée chaque année à mesure que la télérelève et les fiches complètes s'étendent.

**Réponses tolérées**
- Analyse **diagnostique** citée pour la question 2, à la place de l'exploratoire ou en complément.
- Limites différentes, dès lors qu'elles sont tirées des annexes : extrapolation d'une année de sécheresse, limites de secteurs non mises à jour, échelle tronquée du graphique, historique trop court pour une prévision à deux ans.
- Mention de l'apprentissage automatique comme technique possible de la prévision, sans choix ni description de modèle.

**Erreurs fréquentes**
- *Corrélation présentée comme causalité* (`ET-26` ; `JUR-D06` prudence d'interprétation) — « l'âge cause les pertes » ; juste : facteur commun (densité), autres explications, vérification.
- *Développement d'un modèle de prévision* — choix d'un algorithme, variables à paramétrer ; juste : apprécier la fiabilité et les conditions d'usage de la prévision (limite du programme).
- *Méthodes définies sans application* (`JUR-T01`) — descriptive, exploratoire, prédictive récitées sans les données ni le résultat attendu pour la régie.
- *Science des données confondue avec la BI* (`ET-25`) — la description relève du décisionnel ; l'exploration et la prévision mobilisent d'autres compétences.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Méthodes d'analyse descriptive, exploratoire, prédictive, prescriptive | association aux questions de la direction | F08 § 2 | notion de cours |
| Corrélation et causalité, biais de sélection et de données manquantes | limites | F08 § 5 | notion de cours |

---

### 1.3 – Diagnostic, visualisations et outil décisionnel (4 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.d` « Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ». Limites : « L'usage des outils ne dispense pas d'une lecture critique des corrélations et biais » ; « L'interprétation doit être reliée à la stratégie globale ».

**Annexes mobilisées** : annexes 1.2 (défauts, outils actuels), 1.3 (volumes, tableau des secteurs, graphique des Faubourgs nord, outils envisagés) et 1.4 (trajectoire 2029, attentes).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux secteurs prioritaires justifiés par les chiffres de l'annexe 1.3 (Centre ancien, Faubourgs nord) | 0,5 |
| a-2 | Deux facteurs apparents (âge des canalisations et casses ; densité des abonnés et branchements), présentés comme des associations | 0,5 |
| a-3 | Deux précautions de lecture tirées des annexes (lotissement des Prés-Hauts et hausse de septembre 2025, axe tronqué, volume ou taux par km, fiabilité inégale selon la télérelève, débit nocturne de la zone d'activités) | 0,5 |
| a-4 | Diagnostic conclu par une orientation reliée au plan (fiabiliser, puis cibler la recherche de fuites et le renouvellement), en quinze lignes au maximum | 0,5 |
| b-1 | Visualisation pour le directeur de l'exploitation : message, représentation adaptée, indicateur complet | 0,5 |
| b-2 | Visualisation pour le conseil d'administration : message, représentation adaptée, indicateur complet | 0,5 |
| c-1 | Outil de visualisation recommandé et justifié par les besoins du cas (volumes, sources, fraîcheur, cartes, mobilité, coût modeste) | 0,5 |
| c-2 | Conditions de réussite : la BI est une démarche (référentiel des secteurs, définitions partagées, propriétaires des données, compétences et formation) ; place résiduelle du tableur | 0,5 |

**Réponse attendue**

*1.3 a) – Diagnostic argumenté (note modèle)*

<!-- note -->
Les pertes atteignent 5 millions de m³ en 2026 (20 % de l'eau distribuée) ; deux secteurs en font 64 % sur le quart du réseau. Le **Centre ancien** est la première priorité : 8 milliers de m³ perdus par km, près de quatre fois la moyenne, 90 casses pour 100 km, un réseau de 55 ans, un débit nocturne élevé et stable (fuites anciennes, diffuses). Puis les **Faubourgs nord** : 4 milliers de m³ par km, 55 casses pour 100 km, débit nocturne en hausse de 30 % depuis 2024. Deux facteurs apparaissent : l'âge des canalisations, lié aux casses, et la densité des branchements (250 abonnés par km au Centre ancien). Ce sont des associations : les Coteaux sud (40 ans) perdent le moins par km. Deux précautions s'imposent. La hausse des Faubourgs nord coïncide avec le raccordement des Prés-Hauts (septembre 2025), qui change le périmètre du secteur : elle ne prouve pas une fuite tant que la série n'est pas recalculée à périmètre constant, et un axe commençant à 180 m³/h l'amplifie ; les compteurs du lotissement, rattachés au Plateau est, y gonflent les pertes d'environ 0,2 million de m³. Les pertes des secteurs peu équipés en télérelève (Coteaux sud, Faubourgs nord) sont les moins sûres. Il faut corriger le rattachement des secteurs, puis concentrer l'équipe de recherche de fuites sur les Faubourgs nord et le renouvellement sur le Centre ancien.
<!-- /note -->

(0,5 pt par item : secteurs, facteurs, précautions, conclusion.)

*1.3 b) – Deux visualisations pour deux décideurs*

| Destinataire | Message | Représentation | Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|---|---|---|
| Directeur de l'exploitation | où chercher une fuite ce matin ? | carte des secteurs colorée selon l'écart du débit nocturne à la référence (vert, orange, rouge), complétée par la courbe des 90 derniers jours de chaque secteur avec la ligne du seuil d'alerte ; consultable sur tablette par les équipes | Écart du débit nocturne minimal à la référence du secteur | (débit nocturne minimal du jour − débit nocturne de référence du secteur) / débit nocturne de référence du secteur ; la référence est recalculée après chaque campagne de recherche de fuites et chaque modification des limites du secteur | débitmètres d'entrée des secteurs (supervision), rapprochés du référentiel des secteurs | quotidienne, chaque matin | écart inférieur à 10 % ; au-delà, recherche de fuites engagée dans les 48 heures | processus |
| Conseil d'administration | sommes-nous sur la trajectoire de 2029 ? | courbe trimestrielle des pertes sur douze mois glissants de 2026 à 2029, axe partant de zéro, avec la trajectoire cible en pointillés et une barre par secteur en appui | Volume de pertes sur douze mois glissants | volumes mis en distribution − volumes consommés comptabilisés, sur les douze derniers mois | compteurs de sortie des usines (supervision) ; consommations de la plateforme de télérelève et du logiciel de facturation | trimestrielle | 4,5 millions de m³ fin 2027, 4 fin 2028, 3,5 fin 2029 (5 en 2026) | environnement (ESG) |

(0,5 pt par visualisation adaptée à son destinataire, avec un indicateur complet.)

Le directeur de l'exploitation a besoin d'un détail quotidien et localisé pour agir ; le conseil d'administration d'une tendance trimestrielle comparée à l'engagement, lisible sans connaissance technique. Les deux représentations évitent les biais relevés : taux et écarts plutôt que valeurs brutes, axe à zéro pour la courbe du conseil, cible toujours affichée.

*1.3 c) – Outil décisionnel recommandé*

**Outil de visualisation du marché** (0,5 pt), parce qu'il répond aux besoins du cas que le tableur ne couvre pas :
- **volume** : 60 000 index par jour, environ 22 millions de lignes par an, que le technicien ne peut manipuler au tableur et réduit à des totaux mensuels ; la généralisation à 160 000 compteurs multipliera ce volume par près de trois ;
- **sources** : connexion directe aux quatre sources (télérelève, supervision, interventions, base patrimoniale) au lieu d'une dizaine de classeurs alimentés par copie ;
- **fraîcheur** : rafraîchissement chaque nuit, contre un rapport diffusé vers le 20 du mois suivant ; le directeur de l'exploitation veut savoir chaque matin où chercher ;
- **représentation** : cartes des secteurs et consultation sur tablette et téléphone pour les équipes ;
- **coût** : 85 000 € sur trois ans (25 000 € par an et 10 000 € de formation), modeste au regard du programme (11,7 M€ sur trois ans) et de l'équipe de recherche de fuites qu'il doit orienter.

**Conditions** (0,5 pt) : l'outil n'est qu'un maillon d'une démarche décisionnelle ; sans référentiel unique des secteurs, définitions partagées des pertes et du débit nocturne, propriétaires des données (exploitation, clientèle, bureau d'études) et formation des utilisateurs, il afficherait plus vite les mêmes chiffres faux. La compétence repose aujourd'hui sur un seul agent de la DSI : il faut la partager (formation d'un référent à l'exploitation). Le tableur reste utile pour des analyses ponctuelles sur des extraits agrégés.

**Réponses tolérées**
- Secteur Plateau est cité comme troisième priorité après correction du rattachement (0,9 million de m³, 1,8 millier par km), si le candidat l'argumente.
- Faubourgs nord placés en première priorité en raison de la hausse du débit nocturne, si la précaution liée au lotissement est faite.
- Hausse de septembre 2025 interprétée comme une fuite possible sur le raccordement du lotissement, à vérifier sur le terrain, si la rupture de périmètre est signalée.
- Autres indicateurs complets pour les visualisations : pertes par km de canalisation par secteur (barres triées), délai de réparation des fuites signalées, casses pour 100 km.
- Tableur avancé retenu pour une phase transitoire de quelques mois, si ses limites sont montrées et le passage à l'outil de visualisation prévu.
- Indicateur du conseil rattaché à l'axe processus, ou aux axes environnement et financier à la fois.

**Erreurs fréquentes**
- *BI réduite à un outil* (`JUR-D02` ; `ET-05`) — « l'outil de visualisation résoudra le problème des pertes » ; juste : démarche, données fiables, rôles, compétences.
- *Diagnostic sans précaution de lecture* (`ET-26` ; `JUR-D06`) — la hausse de 30 % des Faubourgs nord lue comme une fuite certaine, sans voir qu'elle coïncide avec le raccordement du lotissement, ni l'axe tronqué.
- *Classement en valeur absolue* — les Coteaux sud placés devant le Plateau est sur le volume, sans rapporter les pertes à la longueur du réseau ; juste : comparer des taux.
- *Même visualisation pour tous les destinataires* (`JUR-A04` bon destinataire) — le détail quotidien des secteurs présenté aux élus ; juste : niveau de détail et fréquence adaptés à la décision de chacun.
- *Manipulation d'outil* — formules, mesures ou étapes de construction du tableau de bord dans l'outil ; juste : choix argumenté et structure sur papier.
- *Indicateur incomplet* (`JUR-A02` ; `ET-18`) — « pertes » sans formule, source, fréquence ni cible.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Choix du graphique, biais de lecture (axe tronqué, valeurs absolues, données manquantes), corrélation et causalité | diagnostic et visualisations | F08 § 5 | notion de cours |
| Outils décisionnels : fonctions, limites, critères de choix | recommandation de l'outil | F08 § 6 | notion de cours |
| Fiche d'indicateur à cinq champs | indicateurs des visualisations | F08 § 3 ; F09 § 4 | notion de cours |

---

### 1.4 – Tableau de bord du programme (4 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) » ; `3.1.e` « Revue et amélioration continue des dispositifs de pilotage ». Limites : pas d'approfondissement des méthodes classiques de suivi des écarts au budget ; comptes rendus exigés par une autorité exclus ; recul critique sur les indicateurs.

**Annexes mobilisées** : annexes 1.4 (objectifs, coûts, extrait du rapport, attentes), 1.2 (défauts) et 1.3 (volumes, secteurs), 1.1 (gouvernance de la régie).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Quatre indicateurs complets (formule, source, fréquence, cible chiffrée tirée de l'annexe 1.4, axe), couvrant la performance, les risques et les coûts ; 0,5 par indicateur complet et pertinent | 2 |
| b | Trois arguments tirés de l'extrait du rapport (indicateurs d'activité sans mesure du résultat, absence de cible et de référence, absence de source et de fréquence, absence de coûts et de risques, destinataire mal défini) ; 0,5 pour deux arguments | 1 |
| c-1 | Instance et fréquence de revue précisées (comité de pilotage du programme, compte rendu au conseil d'administration) | 0,5 |
| c-2 | Règle d'ajustement des cibles et règle de retrait d'un indicateur, inscrites dans une boucle d'amélioration continue | 0,5 |

**Réponse attendue**

*1.4 a) – Quatre indicateurs équilibrés*

Un tableau de bord est un ensemble restreint d'indicateurs choisis pour piloter un objectif, présentés pour décider (cible, tendance, alerte, responsable) ; celui du programme suit l'esprit du Balanced Scorecard (Kaplan et Norton) en équilibrant résultat, processus, risques et coûts (F09 § 4).

| Dimension | Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|---|
| Performance (résultat) | Volume de pertes sur douze mois glissants | volumes mis en distribution − volumes consommés comptabilisés, sur les douze derniers mois | compteurs de sortie des usines (supervision) ; plateforme de télérelève et logiciel de facturation | mensuelle (trimestrielle pour le conseil d'administration) | 4,5 millions de m³ fin 2027, 4 fin 2028, 3,5 fin 2029 (5 en 2026) | environnement (ESG) |
| Performance (processus) | Délai moyen de réparation d'une fuite signalée | somme des délais entre le signalement et la fin de la réparation / nombre de fuites réparées dans le mois | logiciel des interventions | mensuelle | 3 jours au plus fin 2029 (10 jours en 2026) | processus |
| Risques (fiabilité des données) | Taux d'index de télérelève exploitables | index quotidiens reçus et validés, ni manquants ni aberrants / (compteurs en télérelève posés × jours du mois) | plateforme de télérelève, journal des contrôles de nettoyage | mensuelle, contrôlée chaque jour | au moins 98 % (environ 95 % en janvier 2027) | processus |
| Coûts | Coût de fonctionnement du programme par m³ de pertes évitées | (abonnement à la plateforme + coût de l'équipe de recherche de fuites, sur douze mois) / (pertes de 2026 − pertes des douze derniers mois) | contrôle de gestion ; indicateur de volume de pertes | trimestrielle | 0,60 € par m³ au plus en 2029 (0,9 M€ / 1,5 million de m³) | financier |

(0,5 pt par indicateur complet et pertinent.)

Le premier indicateur mesure l'objectif du plan, le deuxième le levier opérationnel (l'équipe de recherche de fuites), le troisième le risque principal du programme (décider sur des données fausses : 5 % de compteurs muets chaque jour), le quatrième répond à la question du président du conseil d'administration sur le coût de chaque mètre cube économisé. Le coût de pose des compteurs, investissement de 3 M€ par an, est suivi à part : l'inclure donnerait 2,60 € par m³ en 2029 (3,9 M€ / 1,5 million de m³), sans rendre compte de l'efficacité courante du programme. Aucun écart budgétaire n'est calculé : l'indicateur rapproche un coût d'un résultat.

*1.4 b) – En quoi ce tableau de bord corrige le rapport actuel*

1. **Du compte rendu d'activité à la mesure du résultat** : le rapport aligne un volume produit, un nombre de casses réparées, un nombre de compteurs posés et un débit de nuit, mais aucun ne mesure les pertes, objet du programme ; le tableau de bord part de l'objectif 2029 et le mesure directement.
2. **Des chiffres sans référence aux cibles et aux tendances** : 61 200 compteurs posés ne disent rien sans trajectoire ; rapportés à l'objectif, ils révèlent un retard (1 200 posés en janvier quand 100 000 en 36 mois en demandent près de 2 800 par mois) ; 265 m³/h ne disent rien sans la référence du secteur ; le volume produit d'un mois varie avec la saison. Chaque indicateur porte désormais une cible, une trajectoire et une tendance sur douze mois glissants.
3. **Des chiffres sans source, ni fréquence, ni fiabilité** : un rapport établi à la main en deux jours et diffusé à J+20 ; le tableau de bord fixe pour chaque indicateur sa source et sa fréquence dans une fiche, l'alimente automatiquement et affiche la fiabilité des données.
4. **Un équilibre absent** : ni coût, ni risque, ni destinataire défini (un débit de secteur relève de l'exploitation, pas de la direction générale) ; le tableau de bord en quatre indicateurs, lisible en cinq minutes, répond à la directrice générale et au conseil d'administration.

(1 pt pour trois arguments ; 0,5 pt pour deux.)

*1.4 c) – Revue et amélioration continue*

- **Instance et fréquence** (0,5 pt) : un **comité de pilotage du programme**, présidé par la directrice générale, animé par le chargé de mission, réunissant le directeur de l'exploitation, la directrice de la clientèle (relève des compteurs, facturation), la responsable de la DSI et le responsable du contrôle de gestion, chaque mois, avant le comité de direction ; chaque indicateur a un responsable qui commente l'écart et propose une action ; compte rendu trimestriel au conseil d'administration ; **revue annuelle** du tableau de bord lui-même, à l'automne, après la période de forte consommation et avant l'arbitrage du budget.
- **Règles** (0,5 pt), dans une boucle planifier, réaliser, vérifier, ajuster :
  - **ajustement des cibles** : une fois par an, lors de la revue annuelle ; seulement pour une cause documentée (changement de périmètre comme le rattachement d'un lotissement, cible atteinte durablement, hypothèse démentie par les mesures) ; la cible de 3,5 millions de m³ en 2029, fixée par le plan, n'est modifiée que par le conseil d'administration ; chaque modification est datée dans la fiche de l'indicateur, pour que les séries restent comparables ;
  - **retrait d'un indicateur** : un indicateur qui n'a déclenché aucune décision pendant deux revues, ou dont la cible est tenue douze mois de suite, sort du tableau de bord de la direction générale et rejoint le tableau de bord opérationnel de l'exploitation (le taux d'index exploitables, une fois stable au-dessus de 98 %) ; le suivi de la pose des compteurs disparaît fin 2029 ; tout retrait est décidé par le comité, motivé, et le nombre d'indicateurs reste limité (quatre à six) pour que le tableau de bord reste lisible.

**Réponses tolérées**
- Indicateur d'avancement de la pose des compteurs (compteurs posés / 100 000 compteurs à poser, cible : 2 800 par mois en moyenne, 160 000 abonnés équipés fin 2029, axe processus) à la place du taux d'index exploitables, comme indicateur de risque de retard du programme.
- Coût par m³ calculé avec la pose des compteurs (2,60 € en 2029), si le candidat explique ce que mesure ce choix.
- Volume de pertes rattaché à l'axe processus ; délai de réparation rattaché à l'axe client.
- Boucle d'amélioration continue nommée roue de Deming (PDCA).
- Revue annuelle placée en fin d'exercice ou au moment du rapport d'activité au conseil d'administration.

**Erreurs fréquentes**
- *Indicateurs incomplets ou génériques* (`JUR-A02` distinguer et justifier les indicateurs ; `ET-18`) — « nombre de fuites » sans formule, source, fréquence ni cible ; juste : cinq champs, cibles de l'annexe 1.4.
- *Tableau de bord limité à la performance* (`ET-18`) — aucun indicateur de coût ni de risque, contrairement à la consigne d'équilibre.
- *Calcul d'écarts budgétaires* — décomposition des écarts entre coûts prévus et réalisés ; juste : un ratio de deux chiffres ronds rapproche coût et résultat (limite du programme).
- *Indicateurs réglementaires du service d'eau ou rapport annuel réglementaire* — hors du sujet et du programme ; juste : indicateurs de pilotage du programme.
- *Revue sans règle* (`JUR-T03` analyser et argumenter) — « on revoit le tableau de bord régulièrement » ; juste : instance, fréquence, règles d'ajustement et de retrait.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Balanced Scorecard (Kaplan et Norton, 1992) adapté au SI | structure et équilibre du tableau de bord | F09 § 4.1 | notion de cours |
| Fiche d'indicateur à cinq champs ; tableau de bord restreint | indicateurs | F08 § 3 ; F09 § 4 | notion de cours |
| Critique d'un reporting existant, plan d'amélioration | revue et amélioration continue | F09 § 4.3 | notion de cours |
