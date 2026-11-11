# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 4

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Exploiter les données de télérelève pour réduire les pertes et piloter le programme | 14 | 1.1 à 1.4 | `exercices/ex10_telereleve_pertes_pilotage` |
| 2 – Sécuriser le système de supervision des installations et ses accès | 13 | 2.1 à 2.5 | `exercices/ex11_securite_supervision_identites` |
| 3 – Auditer le portail des abonnés et orienter la stratégie de la relation numérique | 13 | 3.1 à 3.4 | `exercices/ex12_audit_portail_relation_numerique` |
| **Total** | **40** | | |

---

## DOSSIER 1 – EXPLOITER LES DONNÉES DE TÉLÉRELÈVE POUR RÉDUIRE LES PERTES ET PILOTER LE PROGRAMME (14 points)

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

---

## DOSSIER 2 – SÉCURISER LE SYSTÈME DE SUPERVISION DES INSTALLATIONS ET SES ACCÈS (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Risques pesant sur le système de supervision | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers | 4 |
| 2.2 Démarche et principes de la politique de cybersécurité | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques | 3 |
| 2.3 Architecture de confiance | `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) | 2 |
| 2.4 Gestion des identités et surveillance des connexions | `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA | 2 |
| 2.5 Gouvernance de la sécurité de la supervision | `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ; `4.2.a` Définir et piloter une politique de sécurité du SI […] de gouvernance des systèmes critiques | 2 |
| **Dossier 2 – Sécuriser le système de supervision des installations et ses accès** |  | **13** |

Répartition indicative : connaissances (typologie des risques, analyse d'impact sur l'activité, politique de sécurité et étapes d'EBIOS Risk Manager, modèle Zero Trust, intérêt d'une matrice de responsabilités) 3 points (items 2.1 a-1, 2.1 b-1, 2.2 a-1, 2.2 a-2 pour moitié, 2.3-1, 2.5 a pour un quart) ; analyse des annexes et recommandations 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Risques pesant sur le système de supervision (4 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ».

**Annexes mobilisées** : annexes 1.1 (120 sites supervisés, organisation), 2.1 (fonctionnement, inventaire des comptes, organisation de la sécurité), 2.2 (chronologie, constats, scénario redouté) et 2.3 (NIS 2 et son statut).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée : quatre catégories définies (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers), un risque étant formulé comme un événement redouté, avec sa cause et sa conséquence | 0,5 |
| a-2 | Six risques tirés des annexes, chacun formulé et rattaché à la bonne catégorie, au moins un par catégorie ; 0,5 pour quatre risques correctement classés | 1 |
| b-1 | Analyse d'impact sur l'activité définie (processus critiques, conséquences dans le temps, interruption tolérable, priorités) | 0,5 |
| b-2 | Conséquences du scénario analysées sur les trois plans (processus, continuité du service, santé des usagers), avec les chiffres et les faits des annexes et une conclusion sur la criticité ; 0,5 pour deux plans | 1 |
| c | Trois constats tirés de l'annexe 2.2 : détection fortuite et tardive, traitement lent et sans procédure, risques connus non traités faute de propriétaire ; 0,5 pour deux constats | 1 |

**Réponse attendue**

*2.1 a) – Typologie et classement de six risques*

Un **risque du système d'information** est un événement possible qui, s'il survient, porte atteinte à la disponibilité, à l'intégrité, à la confidentialité ou à la traçabilité de l'information et des traitements, et par là aux missions de l'organisation ; on le formule par sa cause, l'événement redouté et sa conséquence. Le programme en distingue quatre catégories : les **cybermenaces** (actes malveillants délibérés : usurpation de compte, logiciel malveillant, rançongiciel, attaque par un prestataire), les **défaillances opérationnelles** (erreurs, pannes, obsolescence, procédures absentes ou mal appliquées), les **risques réglementaires** (non-respect d'obligations présentes ou à venir, responsabilité des dirigeants) et les **risques métiers** (atteinte aux missions, à la santé, à la confiance, aux finances) (F12 § 0 et 5) (0,5 pt).

| Catégorie | Risque (cause → événement redouté → conséquence) | Faits des annexes |
|---|---|---|
| **Cybermenace** | 1. Usurpation d'un compte de prestataire ou d'un compte générique, par l'accès à distance protégé par un seul mot de passe → modification des consignes ou désactivation des alarmes d'un site → réservoir vidé, traitement de l'eau altéré | incident du 22 novembre : compte d'un technicien parti fin juin ; 10 des 25 comptes de prestataires (40 %) au nom de techniciens partis ; accès ouverts en permanence ; aucune authentification multifacteur |
| **Cybermenace** | 2. Logiciel malveillant (rançongiciel, pièce jointe piégée) introduit par la messagerie, internet ou un poste de bureautique et propagé jusqu'aux postes de supervision → perte du pilotage à distance des 120 sites | réseau commun aux 300 postes de bureautique et aux six postes de supervision, sans cloisonnement ; messagerie et internet sur les postes de supervision ; quatre postes sans mises à jour de sécurité depuis 2023 ; trois agents d'astreinte sur leur ordinateur personnel |
| **Cybermenace** (chaîne d'approvisionnement) | 3. Compromission d'un des trois prestataires ou de son poste de télémaintenance → accès à la supervision sans contrôle de la régie | KERVALDIS, BRÉMONTAL et PURIMANE se connectent à toute heure sans prévenir ; contrats sans obligation de signaler les départs |
| **Défaillance opérationnelle** | 4. Actions non imputables et droits excessifs → erreur de manipulation ou acte malveillant interne impossible à retrouver | 3 comptes génériques pour environ 45 personnes, mots de passe inchangés de 2019 à novembre 2026 ; 52 des 60 comptes peuvent modifier les consignes ; compte « admin » partagé avec l'éditeur ; un quart des comptes (15) appartiennent à des personnes parties |
| **Défaillance opérationnelle** | 5. Absence de surveillance et de procédure d'incident → attaque détectée tard ou pas du tout, réaction improvisée | journaux conservés 30 jours, jamais consultés, aucune alerte ; connexion du 4 novembre passée inaperçue ; 3 h 30 avant une détection fortuite ; compte désactivé 28 heures après la détection |
| **Risque réglementaire** | 6. Écart entre les pratiques de la régie et les exigences qu'impose la directive NIS 2 aux entités qui entrent dans son champ (analyse des risques, chaîne d'approvisionnement, contrôle d'accès, authentification multifacteur, notification sous 24 heures, responsabilité des organes de direction) → mise en conformité tardive et coûteuse, responsabilité des dirigeants exposée, si la régie y était soumise, ce que le dossier ne demande pas d'apprécier | directive non transposée en droit français au 31/12/2026 (annexe 2.3) : le risque est **à venir** et appelle une anticipation ; conseil d'administration informé 18 jours après l'incident ; aucune procédure de notification |
| **Risque métier** | 7. Interruption de la distribution ou mise en distribution d'une eau impropre → atteinte à la santé des usagers, perte de confiance des abonnés et des élus de la communauté d'agglomération, coûts | réservoir de la Combe-Martel : 12 000 habitants, dont un établissement pour personnes âgées dépendantes, qui auraient manqué d'eau vers 8 h 30 ; scénario redouté (annexe 2.2 C) ; coût direct de 25 000 € pour un incident sans conséquence |

(1 pt pour six risques correctement formulés et classés, au moins un par catégorie ; 0,5 pt pour quatre. Le corrigé en propose sept ; six suffisent.)

*2.1 b) – Analyse d'impact du scénario redouté*

L'**analyse d'impact sur l'activité** (BIA) identifie les processus critiques d'une organisation, mesure, dans le temps, les conséquences de leur interruption ou de leur altération (humaines, opérationnelles, financières, d'image, juridiques) et fixe la durée d'interruption tolérable de chacun ; elle sert à hiérarchiser les mesures de sécurité et de continuité. C'est une démarche, distincte du plan de continuité, qu'elle prépare (F12 § 4) (0,5 pt).

Application au scénario de l'annexe 2.2 C (modification, une même nuit, des consignes de plusieurs réservoirs et du dosage des réactifs d'une usine) (1 pt) :

- **Processus de la régie** : sont atteints à la fois la **production** (dosage des réactifs dans une usine), la **distribution** (remplissage des réservoirs, marche des pompes) et le **contrôle de la qualité de l'eau** : l'alarme des analyseurs remonte par la supervision elle-même, de sorte qu'un attaquant qui la contrôle peut aussi aveugler la détection. La supervision est un **point unique** de pilotage et de détection pour 120 sites ; les interventions d'astreinte, l'accueil et l'information des abonnés sont ensuite saturés. La facturation, elle, n'est pas atteinte : l'impact ne se mesure pas d'abord en euros.
- **Continuité du service** : dans l'incident réel, un seul réservoir dont les pompes ont été arrêtées à 2 h 25 aurait été vide vers 8 h 30, soit en six heures environ, au moment de la pointe du matin ; plusieurs réservoirs modifiés en même temps priveraient d'eau ou de pression des quartiers entiers. Le mode manuel existe, mais il faut environ deux heures pour mobiliser une équipe la nuit, et huit agents d'astreinte ne peuvent pas conduire sur place 120 sites : la durée d'interruption tolérable se compte en heures et dépend de la détection. Le retour à la normale (remise en eau, vérification des installations, reprise du pilotage à distance de confiance) prolongerait l'interruption au-delà de l'attaque elle-même.
- **Santé des usagers** : une eau mal traitée (excès ou insuffisance de réactif) peut être distribuée avant toute détection, puisque l'alarme de qualité passe par le système compromis ; les personnes vulnérables (établissement pour personnes âgées dépendantes de la Combe-Martel) sont les plus exposées ; une perte de pression dans les canalisations aggrave le risque sanitaire ; la régie devrait alors restreindre la consommation et fournir de l'eau autrement.
- **Conclusion** : la gravité est maximale (atteinte possible à la santé de milliers d'habitants), et la vraisemblance n'est pas faible (un quart des comptes appartiennent à des personnes parties, accès à distance par simple mot de passe, incident déjà survenu). La supervision est un **système critique** dont la disponibilité et l'intégrité priment ; la régie a besoin d'une détection qui ne dépende pas de la seule supervision et d'un mode manuel préparé.

*2.1 c) – Ce que l'incident révèle* (1 pt)

1. **Une détection fortuite et tardive** : 3 h 30 entre la connexion et la détection, due au hasard (un agent d'astreinte connecté pour une autre alarme), et 3 h 15 après l'arrêt des pompes, que l'attaquant avait masqué en désactivant l'alarme de niveau bas ; la connexion du 4 novembre est passée inaperçue ; les journaux, conservés 30 jours et jamais consultés, ne permettent pas de savoir si le compte a servi avant le 23 octobre. La régie ne surveille pas ses accès : elle découvre les attaques quand elles produisent un effet visible.
2. **Un traitement lent et improvisé** : faute de procédure, l'agent ne coupe pas les accès ; le directeur de l'exploitation attend le lundi ; le compte est désactivé 28 heures après la détection, le responsable de la sécurité des systèmes d'information informé plus de 29 heures après, la directrice générale à midi le lundi, le conseil d'administration 18 jours plus tard ; les neuf autres comptes de prestataires au nom de techniciens partis ne sont désactivés que le 25 novembre et les mots de passe génériques changés le 27. Personne ne sait qui décide ni qui alerte.
3. **Des risques connus mais non traités, faute de propriétaire** : la supervision est hors du champ de la politique de sécurité de 2021 et n'a jamais fait l'objet d'une analyse des risques ; la recommandation d'authentification multifacteur de 2025 n'a pas été suivie « faute de budget et de responsable désigné » ; les comptes ne sont pas revus depuis 2019 ; les contrats n'obligent pas les prestataires à signaler les départs ; la sécurité représente moins de 3 % du budget du SI. Le risque n'a pas été accepté par une décision : il l'a été par défaut.

L'incident n'est donc pas un accident isolé : il révèle une gouvernance de la sécurité absente pour le système le plus critique de la régie.

**Réponses tolérées**
- Typologie en trois catégories (risques réglementaires et métiers regroupés, comme dans l'intitulé du programme), si les six risques sont correctement formulés.
- Risque d'interception ou d'altération des échanges non chiffrés avec les 80 sites reliés par l'opérateur classé en cybermenace ; obsolescence des quatre postes classée en défaillance opérationnelle.
- Dépendance à l'égard des prestataires (savoir-faire détenu par l'éditeur et l'intégrateur) présentée comme un risque métier.
- Analyse d'impact présentée sous forme de tableau (processus, conséquence à 1 heure, 6 heures, 24 heures) ou accompagnée d'une cotation probabilité × gravité, si elle est justifiée par les annexes.
- Constat sur le partage des responsabilités entre l'exploitation et la DSI (« deux mondes ») au titre de la troisième faiblesse.
- Responsabilité de la régie à l'égard des usagers en cas de distribution d'une eau impropre, présentée sans analyse juridique et classée en risque réglementaire ou en risque métier.

**Erreurs fréquentes**
- *Morceau de cours* (`JUR-T01` contextualiser chaque notion) — typologie récitée sans les comptes, les accès à distance ni la Combe-Martel ; juste : chaque risque porte un fait chiffré des annexes.
- *Annexes survolées* (`JUR-T08` exploiter toutes les annexes) — connexion du 4 novembre, durée de conservation des journaux ou désactivation de l'alarme oubliées ; juste : ce sont les faits qui montrent les faiblesses de détection.
- *Statut de NIS 2 affirmé sans date* (`ET-41`) — présenter NIS 2 comme déjà applicable en droit français à la régie, ou trancher son assujettissement ; juste : directive non transposée au 31/12/2026 (annexe 2.3), risque à anticiper.
- *Analyse d'impact confondue avec le plan de continuité* (`ET-02`) — elle mesure les conséquences et fixe les priorités ; le plan organise le maintien de l'activité.
- *Impact réduit au coût de l'incident* (`JUR-T03` analyser et argumenter) — les 25 000 € ne mesurent pas l'enjeu ; juste : santé des usagers et continuité de la distribution.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques du SI, menaces (chaîne d'approvisionnement, compromission de comptes) | classement des risques | F12 § 0 et 5 | notion de cours |
| Analyse d'impact sur l'activité (BIA) | conséquences du scénario, interruption tolérable | F12 § 4 | notion de cours |
| Directive (UE) 2022/2555 (« NIS 2 ») | risque réglementaire à venir, mesures et responsabilité des organes de direction | `nis2` / F12 § 6.1 | en vigueur ; transposition due au 17/10/2024 |
| Transposition française de NIS 2 | statut au 31/12/2026 | `nis2_transposition_fr` / F12 § 6.2 | non transposée au 31/12/2026 |

---

### 2.2 – Démarche et principes de la politique de cybersécurité (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ».

**Annexes mobilisées** : annexes 2.1 (fonctionnement, comptes, politique de 2021, points de vue), 2.2 (incident, scénario redouté) et 2.3 (EBIOS Risk Manager, ISO/IEC 27001:2022, guide d'hygiène, NIS 2).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Politique de sécurité du SI définie (document approuvé par la direction : objectifs de disponibilité, d'intégrité, de confidentialité et de traçabilité, périmètre, principes, organisation, règles, contrôle), distinguée de la charte | 0,5 |
| a-2 | Les cinq ateliers d'EBIOS Risk Manager présentés dans l'ordre, chacun illustré par un élément du cas ; la formalisation, l'approbation, la déclinaison et la revue de la politique sont valorisées mais non exigées ; 0,5 pour trois ateliers illustrés | 1 |
| b | Quatre principes propres à un système critique, chacun justifié par les annexes ; 1 pour trois, 0,5 pour deux | 1,5 |

**Réponse attendue**

*2.2 a) – Définition et démarche*

La **politique de sécurité du système d'information** (PSSI) est le document de référence, approuvé par la direction, qui fixe les **objectifs** de sécurité (disponibilité, intégrité, confidentialité et traçabilité de l'information), le **périmètre**, les **principes**, l'**organisation** (rôles et responsabilités), les **règles** et le **dispositif de contrôle** ; elle se décline en procédures et en une charte opposable aux utilisateurs, qui n'en est qu'une déclinaison (F12 § 1) (0,5 pt). Fondée sur l'analyse des risques, elle proportionne les mesures aux risques réels au lieu d'empiler des règles.

Étapes, en s'appuyant sur EBIOS Risk Manager, méthode de l'ANSSI (annexe 2.3) (1 pt) :

| Étape | Contenu | Application à la supervision |
|---|---|---|
| 1. Cadrage et socle de sécurité | périmètre, missions et biens à protéger, événements redoutés et leur gravité ; écart au socle de règles de base | périmètre : centre de supervision, 120 sites, liaisons, accès à distance, comptes ; missions : produire et distribuer en continu une eau potable, traiter les eaux usées ; événements redoutés : consignes altérées, alarmes neutralisées, perte du pilotage ; écarts au guide d'hygiène de l'ANSSI et aux mesures de l'ISO/IEC 27002:2022 : pas d'authentification multifacteur, comptes génériques, postes obsolètes, réseau non cloisonné |
| 2. Sources de risque | qui pourrait attaquer et dans quel but | ancien technicien ou ancien agent mécontent, cybercriminel cherchant une rançon, attaquant opportuniste qui trouve un accès à distance ouvert sur internet, acteur cherchant à nuire à une infrastructure |
| 3. Scénarios stratégiques | chemins d'attaque par l'écosystème | trois prestataires à accès permanent, opérateur de téléphonie mobile, agents d'astreinte à domicile dont trois sur un ordinateur personnel : chaque tiers est évalué selon son exposition et la confiance qu'on peut lui accorder |
| 4. Scénarios opérationnels | modes opératoires détaillés et vraisemblance | compte de prestataire inactif → accès à distance → arrêt des pompes d'un réservoir et désactivation de son alarme (scénario réalisé en novembre 2026) ; message piégé ouvert sur un poste de bureautique → rebond vers un poste de supervision |
| 5. Traitement du risque | plan de mesures priorisé, risques résiduels | mesures des questions 2.3 et 2.4, échéancées sur l'enveloppe de 200 000 € par an ; risques résiduels acceptés par décision de la direction générale et présentés au conseil d'administration |

Puis la PSSI est **formalisée** en étendant celle de 2021 à la supervision, **approuvée** par la direction générale et présentée au conseil d'administration, **déclinée** en procédures (gestion des accès, gestion d'incident), en charte pour les agents et en exigences de sécurité dans les contrats des prestataires, enfin **revue** chaque année et après chaque incident, dans une logique d'amélioration continue analogue à celle de l'ISO/IEC 27001:2022 (planifier, réaliser, vérifier, ajuster), sans qu'une certification soit visée.

*2.2 b) – Quatre principes propres à un système critique* (1,5 pt)

1. **Priorité à la disponibilité et à l'intégrité du service** : pour la supervision, l'enjeu premier est que l'eau soit distribuée et correctement traitée, avant la confidentialité ; aucune mesure ne doit empêcher une intervention légitime de nuit, comme le redoute M. SALVANHAC ; chaque mesure est conçue avec l'exploitation et prévoit une procédure de secours. Justification : scénario redouté, réservoir vide en six heures.
2. **Cloisonnement et défense en profondeur** : la supervision est isolée de la bureautique, de la messagerie et d'internet, et protégée par plusieurs barrières successives, de sorte qu'une faille unique ne suffise pas. Justification : réseau commun aux 300 postes de bureautique, messagerie et internet sur les postes de supervision, quatre postes obsolètes.
3. **Moindre privilège et imputabilité** : chacun n'a que les droits nécessaires à son rôle, sur un compte nominatif ; toute action est tracée et attribuable ; les actions les plus sensibles (seuils d'alarme, dosage des réactifs, création de comptes) sont réservées à quelques personnes et enregistrées. Justification : 52 comptes sur 60 peuvent modifier les consignes, trois comptes génériques pour environ 45 personnes, compte « admin » partagé avec l'éditeur.
4. **Maîtrise des tiers** (sécurité de la chaîne d'approvisionnement) : un prestataire n'accède à la supervision que sur demande, pour une durée limitée, sous le contrôle de la régie, avec des obligations contractuelles (signalement des départs, règles d'accès, droit de contrôle). Justification : 25 comptes de prestataires dont 10 au nom de techniciens partis, accès ouverts en permanence, incident venu d'un compte de BRÉMONTAL ; NIS 2 range cette sécurité parmi les mesures attendues (annexe 2.3).

**Réponses tolérées**
- Démarche présentée selon les étapes de l'ISO/IEC 27005:2022 (identification, analyse, évaluation, traitement, acceptation des risques) ou selon les six fonctions du NIST Cybersecurity Framework 2.0 (gouverner, identifier, protéger, détecter, répondre, rétablir), si elle part de l'analyse des risques et est appliquée au cas.
- Principe de **détection et de réaction** (surveiller en continu, alerter, savoir qui décide) ou de **responsabilité** (un propriétaire du risque désigné pour la supervision) à la place de l'un des quatre principes.
- Principe d'un **mode dégradé maîtrisé** (conduite manuelle des sites préparée), s'il reste énoncé comme un principe et n'est pas développé en plan de continuité.

**Erreurs fréquentes**
- *PSSI confondue avec la charte informatique* (`ET-27`) — la charte n'en est qu'une déclinaison destinée aux utilisateurs.
- *Norme, méthode et solution confondues* (`JUR-S06` confondre référentiels, normes et solutions ; `ET-01`) — « installer ISO 27001 », EBIOS Risk Manager présenté comme un logiciel ; juste : ISO/IEC 27001:2022 est une norme d'exigences, EBIOS Risk Manager une méthode, le guide d'hygiène un guide.
- *Objectifs de sécurité oubliés* (`JUR-S01` triade CID) — la politique doit dire ce qu'elle protège : disponibilité et intégrité d'abord, pour la supervision.
- *Principes génériques* (`JUR-T01`) — « sensibiliser le personnel » sans lien avec la supervision ; juste : principes propres à un système qui pilote des installations.
- *Démarche de certification proposée* — hors programme et hors de la demande ; juste : la norme sert de référence.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| EBIOS Risk Manager (ANSSI, version 1.5 de 2024) | cinq ateliers appliqués à la supervision | `ebios_rm_1_5` / F12 § 2 | en vigueur |
| ISO/IEC 27005:2022 | gestion des risques (réponse tolérée) | `iso_27005_2022` / F12 § 2 | en vigueur |
| ISO/IEC 27001:2022 et ISO/IEC 27002:2022 | amélioration continue, mesures de référence | `iso_27001_2022`, `iso_27002_2022` / F12 § 2 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | socle de mesures de base | `guide_hygiene_anssi_2017` / F12 § 2 | en vigueur |
| NIST Cybersecurity Framework 2.0 (2024) | six fonctions (réponse tolérée) | `nist_csf_2_0` / F12 § 2 | en vigueur |
| PSSI, triade CID et traçabilité | définition et objectifs | F12 § 1 | notion de cours |

---

### 2.3 – Architecture de confiance (2 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) ».

**Annexes mobilisées** : annexes 2.1 (liaisons, réseau, accès à distance, authentification, points de vue) et 2.3 (modèle Zero Trust).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Modèle Zero Trust présenté comme un modèle d'architecture (aucune confiance implicite, vérification de chaque accès selon l'identité, le terminal et le contexte, démarche progressive), et non comme un produit, et appliqué à la régie (fin de la confiance accordée au réseau commun et aux accès à distance ouverts) | 0,5 |
| 2 | Mesure d'authentification, rattachée à son constat, avec une condition de réussite | 0,5 |
| 3 | Mesure de chiffrement, rattachée à son constat, avec une condition de réussite | 0,5 |
| 4 | Mesure de segmentation entre la bureautique et la supervision, rattachée à son constat, avec une condition de réussite | 0,5 |

**Réponse attendue**

Le **modèle Zero Trust** est un modèle d'architecture fondé sur le principe « ne jamais faire confiance par défaut, toujours vérifier » : aucune confiance n'est accordée à un utilisateur ou à un terminal du seul fait qu'il est connecté au réseau de la régie ; chaque accès à une ressource est authentifié, autorisé et évalué selon le contexte (identité, état du terminal, sensibilité de la ressource, horaire), avec le moindre privilège et une surveillance continue. Ce n'est ni un produit ni un logiciel que l'on achète : c'est une démarche progressive de transformation, qui ne remplace pas la défense en profondeur (avis de l'ANSSI, annexe 2.3). À la régie, il conduit à ne plus considérer comme sûr un poste du simple fait qu'il est sur le réseau commun, et à vérifier chaque connexion à la supervision (0,5 pt).

| Mesure | Constat de l'annexe 2.1 | Condition de réussite |
|---|---|---|
| **Authentification multifacteur** pour tous les accès à distance (agents d'astreinte, prestataires) et pour les comptes d'administration, sur des comptes nominatifs ; accès à distance depuis des terminaux fournis et gérés par la régie (fin des ordinateurs personnels) ; accès d'un prestataire autorisé seulement pendant une intervention demandée (0,5 pt) | identifiant et mot de passe pour tous les comptes ; accès à distance joignable depuis internet ; recommandation de 2025 non suivie ; trois agents d'astreinte sur leur ordinateur personnel ; incident venu d'un mot de passe obtenu on ne sait comment | être utilisable à 3 heures du matin : facteur de possession remis à chaque agent d'astreinte, procédure de secours en cas de perte, essai avec l'exploitation avant généralisation (point de vue de M. SALVANHAC) ; mêmes exigences imposées aux prestataires par contrat |
| **Chiffrement** des échanges entre le centre de supervision et les sites, en priorité les 80 sites reliés par l'opérateur de téléphonie mobile, et des sessions d'accès à distance (0,5 pt) | échanges entre le centre et les sites non chiffrés ; 80 sites reliés par un réseau extérieur | le chiffrement protège surtout l'**intégrité** et l'authenticité des consignes (une consigne ne doit pas pouvoir être modifiée en chemin) ; il suppose de vérifier avec BRÉMONTAL la compatibilité des automates, de commencer par les sites les plus critiques (usines, grands réservoirs) et d'organiser la gestion des clés |
| **Segmentation** : zone réservée à la supervision, séparée de la bureautique ; aucun accès à la messagerie ni à internet depuis les postes de supervision ; tous les flux interdits sauf ceux qui sont explicitement autorisés ; accès à distance par un point d'entrée unique, contrôlé et journalisé ; découpage plus fin par type de site pour limiter les mouvements latéraux (0,5 pt) | réseau commun aux 300 postes de bureautique et aux six postes de supervision, sans cloisonnement ; messagerie et internet sur les postes de supervision ; « deux mondes qui partagent les mêmes câbles » | inventaire préalable des échanges légitimes, conduit ensemble par la DSI et l'exploitation ; remplacement ou isolement des quatre postes sans mises à jour, qui resteraient le maillon faible ; règle de gestion des exceptions validée par le responsable de la sécurité des systèmes d'information |

**Réponses tolérées**
- Gestion des terminaux mobiles (MDM, *Mobile Device Management*) des ordinateurs portables d'astreinte au titre de l'authentification ou d'une condition de réussite.
- Accès conditionnel (refus d'une connexion de prestataire hors d'une fenêtre d'intervention, ou depuis un terminal non conforme) présenté comme application du Zero Trust.
- Mesure de segmentation qui prévoit une passerelle unique d'échange entre la supervision et la bureautique pour les rares données qui doivent circuler (rapports d'exploitation).

**Erreurs fréquentes**
- *Zero Trust présenté comme un produit* (`JUR-S03` Zero Trust cadre architectural et non solution logicielle ; `ET-04`) — « acheter le Zero Trust d'un éditeur » ; juste : modèle et démarche progressive.
- *Authentification multifacteur confondue avec un mot de passe complexe* (`ET-28`) — juste : au moins deux facteurs de nature différente.
- *Micro-segmentation confondue avec une segmentation applicative* (`ET-14`) — juste : cloisonnement des flux entre zones pour limiter les mouvements latéraux.
- *Réponse technique* (`JUR-T12` moins de technique, plus de management) — description du réglage des équipements de sécurité, ligne par ligne : hors programme ; juste : mesure, constat, condition.
- *Mesure sans condition de réussite* (`JUR-T03`) — une authentification forte qui bloque l'astreinte serait contournée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Le modèle Zero Trust (avis de l'ANSSI, 2021) | définition, démarche progressive | `zero_trust_anssi` / F12 § 3 | en vigueur |
| Authentification multifacteur, segmentation, micro-segmentation, chiffrement | trois mesures | F12 § 3 | notion de cours |
| Directive (UE) 2022/2555 (« NIS 2 ») | chiffrement et authentification multifacteur parmi les mesures | `nis2` / F12 § 6.1 | en vigueur ; non transposée en France au 31/12/2026 |

---

### 2.4 – Gestion des identités et surveillance des connexions (2 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ».

**Annexes mobilisées** : annexes 2.1 (inventaire des comptes, accès à distance, journaux, organisation) et 2.2 (chronologie, constats).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Quatre règles de gestion des identités et des accès (cycle de vie, comptes génériques, comptes à privilèges, revue périodique), applicables aux agents et aux prestataires, chacune rattachée à un constat de l'inventaire ; 0,5 pour deux règles | 1 |
| b-1 | Dispositif de surveillance : journaux centralisés et conservés plus longtemps, règles d'alerte propres à la supervision, traitement des alertes à toute heure, revue des connexions des prestataires | 0,5 |
| b-2 | Deux indicateurs d'efficacité complets (formule, source, fréquence, cible, axe) ; 0 si un seul indicateur est complet | 0,5 |

**Réponse attendue**

*2.4 a) – Quatre règles de gestion des identités et des accès* (1 pt)

La gestion des identités et des accès (IAM) organise, pour chaque personne, l'attribution, l'évolution et le retrait des droits sur tout le cycle de vie, selon son rôle et le principe du moindre privilège (F12 § 3 ; F10 § 3.1). Le directeur de l'exploitation, propriétaire de la supervision, décide des droits ; la DSI les met en œuvre ; le responsable de la sécurité des systèmes d'information contrôle.

1. **Cycle de vie des comptes** : tout compte est créé sur demande validée, rattaché à une personne et à un rôle, modifié à chaque mutation et désactivé le jour du départ. Pour les agents, la direction des ressources humaines signale chaque arrivée, mutation et départ ; pour les prestataires, le contrat oblige à signaler le départ d'un technicien sous 24 heures, et les comptes expirent d'eux-mêmes à la fin du contrat ou après une période sans usage. Constat : 15 comptes (un quart) appartiennent à des personnes parties ; le compte utilisé le 22 novembre était actif depuis près de cinq mois après le départ du technicien.
2. **Comptes génériques** : suppression des trois comptes « exploitation », « astreinte » et « maintenance » au profit d'un compte nominatif pour chacune des quelque 45 personnes ; toute exception (poste de consultation du centre) est limitée à la lecture et justifiée. Constat : aucune action n'est attribuable ; mots de passe inchangés de 2019 à novembre 2026.
3. **Comptes à privilèges** : les quatre comptes d'administration deviennent nominatifs, distincts du compte quotidien, protégés par une authentification multifacteur et utilisés par le point d'entrée contrôlé, avec enregistrement des sessions ; suppression du compte « admin » partagé avec l'éditeur ; les prestataires n'obtiennent des droits que sur demande, pour la durée de l'intervention, après validation par l'exploitation ; les droits de modification des consignes sont réservés aux rôles qui en ont besoin (opérateurs, astreinte), les autres en consultation. Constat : 52 comptes sur 60 peuvent modifier les consignes.
4. **Revue périodique des droits** : revue semestrielle des 60 comptes par le directeur de l'exploitation, la liste des comptes de chaque prestataire étant confirmée par celui-ci, sous le contrôle du responsable de la sécurité des systèmes d'information ; tout compte non confirmé est désactivé ; revue supplémentaire après chaque incident. Constat : aucune revue des comptes de prestataires depuis 2019.

*2.4 b) – Surveillance des connexions et indicateurs*

**Dispositif** (0,5 pt) :
- **Journalisation** : les journaux de la supervision, de l'accès à distance et des comptes d'administration sont centralisés hors de la supervision et conservés au moins un an, pour reconstituer un incident (30 jours aujourd'hui, ce qui interdit de savoir si le compte a servi avant le 23 octobre).
- **Règles d'alerte** propres à la supervision : connexion d'un prestataire sans demande d'intervention ouverte ; connexion de nuit d'un compte qui n'est pas d'astreinte ; modification d'une consigne ou désactivation d'une alarme hors des heures d'exploitation ; échecs répétés de connexion ; connexion d'un compte inactif depuis plusieurs semaines. L'incident du 22 novembre aurait déclenché au moins trois de ces alertes.
- **Traitement des alertes à toute heure** : le responsable de la sécurité des systèmes d'information, à mi-temps, ne peut pas veiller seul ; la régie confie la surveillance à un centre opérationnel de sécurité (SOC) externe ou mutualisé, appuyé sur un outil de collecte et de corrélation des journaux (SIEM), qui alerte l'agent d'astreinte et le responsable de la sécurité selon une procédure d'escalade (qui coupe les accès, qui prévient la directrice générale) ; les alarmes critiques de qualité de l'eau sont doublées par une voie qui ne dépend pas de la supervision.
- **Revue hebdomadaire** par l'exploitation de la liste des connexions de prestataires, rapprochée des interventions demandées.

**Indicateurs d'efficacité** (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Délai de détection d'une connexion anormale | moyenne, sur les connexions anormales du mois, de (heure de prise en charge de l'alerte − heure de la connexion) | journaux centralisés et registre des alertes du centre opérationnel de sécurité | mensuelle | moins de 15 minutes (3 h 30, et par hasard, en novembre 2026) | processus |
| Taux de connexions de prestataires autorisées | connexions de prestataires rattachées à une demande d'intervention validée / connexions de prestataires | journaux de l'accès à distance et registre des demandes d'intervention | mensuelle | 100 % (accès aujourd'hui ouverts en permanence, sans demande) | processus |

**Réponses tolérées**
- Rôles (RBAC) définis par métier (opérateur, agent d'astreinte, automaticien, prestataire) en guise de règle sur le cycle de vie ou sur les privilèges.
- Revue trimestrielle des comptes de prestataires et semestrielle des comptes d'agents.
- Indicateur « taux de comptes désactivés dans les 24 heures suivant le départ » (comptes désactivés dans les 24 heures suivant le départ de la personne (ou son signalement par le prestataire) / départs du mois ; source : signalements de la direction des ressources humaines et des prestataires, inventaire des comptes ; mensuelle ; cible 100 % ; axe processus) ou « part des comptes nominatifs » (comptes nominatifs / comptes actifs de la supervision ; source : inventaire des comptes ; trimestrielle ; cible 100 % fin 2027 ; axe processus), s'il est relié au dispositif de surveillance ou de gestion des accès.
- Analyse comportementale des connexions, éventuellement appuyée sur l'intelligence artificielle, pour repérer les écarts aux habitudes d'un compte, avec ses limites (faux positifs, réglage initial).
- Indicateur rattaché à l'axe « apprentissage » ou à l'axe ESG « gouvernance », si le choix est justifié.

**Erreurs fréquentes**
- *Plan de continuité ou de reprise développé à la place de la surveillance* (`ET-02` PCA et PRA ; `JUR-S02`) — la question porte sur l'IAM et la détection ; le PCA et le PRA ne sont pas demandés.
- *Identification, authentification et autorisation confondues* (`ET-28`) — un compte nominatif identifie, l'authentification multifacteur prouve l'identité, la revue des droits règle l'autorisation.
- *IAM réduit à un outil* (`JUR-S05` mesures opérationnelles cohérentes) — l'IAM est d'abord un processus (demande, validation, retrait, revue) avec des responsables.
- *Indicateurs incomplets ou génériques* (`ET-18`) — « nombre d'incidents » sans formule, source ni cible ; juste : cinq champs, point de départ de l'annexe.
- *Surveillance confiée au seul responsable de la sécurité à mi-temps* (`JUR-T03`) — l'incident a eu lieu un samedi à 2 heures du matin.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| IAM : cycle de vie, rôles, comptes à privilèges, revues ; SIEM et SOC en principe | quatre règles, dispositif de surveillance | F12 § 0 et 3 ; glossaire (SIEM) | notion de cours |
| Habilitations, moindre privilège, revue semestrielle des droits | revue périodique | F10 § 3.1 | notion de cours |
| Indicateurs d'efficacité des mesures (délai de détection, délai de révocation des droits) | deux indicateurs | F12 § 3 | notion de cours |
| IA défensive : analyse comportementale (réponse tolérée) | surveillance | F13 ; F12 § 0 | notion de cours |

---

### 2.5 – Gouvernance de la sécurité de la supervision (2 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques » ; `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ».

**Annexes mobilisées** : annexes 1.1 (organigramme), 2.1 (organisation de la sécurité, points de vue), 2.2 (chronologie de l'information des acteurs) et 2.3 (NIS 2 : responsabilité des organes de direction).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Intérêt de la matrice précisé (qui réalise, qui approuve — un seul par activité —, qui est consulté, qui est informé ; éviter les vides et les doublons de responsabilité) et matrice cohérente pour les quatre activités et les six acteurs ; 0,5 pour deux activités correctement réparties | 1 |
| b | Deux évolutions de l'organisation justifiées par les annexes, dont le positionnement du responsable de la sécurité des systèmes d'information ; 0,5 par évolution | 1 |

**Réponse attendue**

*2.5 a) – Matrice de responsabilités* (1 pt)

Une **matrice de responsabilités** (RACI) indique, pour chaque activité, qui la **réalise** (R), qui l'**approuve** et en répond (A, un seul par activité), qui est **consulté** avant la décision (C) et qui est **informé** après (I) (F05 § 1 ; F02 § 0). Elle répond au défaut que révèle l'incident : personne ne savait qui décidait de couper les accès ni qui informait la direction (annexe 2.2), et la supervision n'était sous la responsabilité de sécurité de personne.

| Activité | Conseil d'administration | Directrice générale | Responsable de la sécurité des SI | Directeur de l'exploitation | Responsable de la DSI | Prestataires |
|---|---|---|---|---|---|---|
| Approbation de la politique de sécurité de la supervision | **A** (approuve les orientations et le niveau de risque accepté, suit leur mise en œuvre) | R (porte la politique et arbitre les moyens) | R (élabore) | C | C | I |
| Analyse des risques de la supervision | I | **A** (accepte les risques résiduels) | R (pilote la méthode) | R (missions, événements redoutés, scénarios) | C | C (écosystème, scénarios) |
| Gestion des accès des prestataires | — | I | C (fixe les règles, contrôle la revue) | **A** (valide chaque ouverture d'accès) | R (crée, ouvre, ferme, désactive) | R (demandent les accès, signalent les départs) |
| Traitement d'un incident | I (sans délai si l'incident est grave) | **A** (dirige la cellule de crise, décide de la communication) | R (coordonne la réponse, qualifie l'incident) | R (protège les installations, passe en mode manuel) | R (coupe les accès, conserve les traces) | C (investigation, correction) |

*2.5 b) – Deux évolutions de l'organisation* (1 pt)

1. **Repositionner le responsable de la sécurité des systèmes d'information** : le rattacher à la directrice générale et non plus à la DSI, étendre sa mission à la supervision (droit de regard, accès aux journaux, contrôle des comptes) et en faire une fonction à temps plein, au besoin appuyée par un prestataire. Justification : à mi-temps et rattaché à la DSI dont il gère aussi les infrastructures, il est juge et partie ; il n'a « aucun droit de regard » sur le système le plus critique et a été informé plus de 29 heures après la détection. L'enveloppe de 200 000 € par an permet de financer ce temps et la surveillance externe.
2. **Installer une gouvernance de la sécurité au niveau de la direction et du conseil** : un comité de sécurité trimestriel (directrice générale, responsable de la sécurité, directeur de l'exploitation, responsable de la DSI, directrice des ressources humaines pour le cycle de vie des comptes) qui suit le plan de traitement et les indicateurs ; un examen annuel de la sécurité par le conseil d'administration, une information sans délai en cas d'incident grave (au lieu de 18 jours) et une formation des administrateurs, en anticipation de la responsabilité que NIS 2 donne aux organes de direction, sans préjuger de son application à la régie (annexe 2.3). Justification : avant décembre 2026, le conseil n'avait jamais examiné la sécurité ; Mme ROCHEVAL veut dire « qui en répond et dans quels délais ».

**Réponses tolérées**
- Directrice générale en A pour l'approbation de la politique, le conseil d'administration étant informé et approuvant les orientations et l'enveloppe, si le choix est justifié.
- Directeur de l'exploitation en A pour l'analyse des risques, comme propriétaire de la supervision, la directrice générale arbitrant les risques résiduels les plus graves.
- Évolution portant sur la désignation du directeur de l'exploitation comme **propriétaire du risque** de la supervision, avec un correspondant sécurité parmi les automaticiens, ou sur l'ajout de clauses de sécurité dans les contrats des trois prestataires (signalement des départs, accès sur demande, droit de contrôle), sans analyse juridique des contrats.
- Matrice présentée avec les activités en colonnes et les acteurs en lignes.

**Erreurs fréquentes**
- *Responsable de la sécurité vu comme un technicien ou maintenu sous la DSI sans indépendance* (`ET-15`) — juste : il pilote la politique et contrôle, y compris la DSI.
- *Deux « A » sur une même activité* — la matrice perd son intérêt : une seule personne approuve et répond.
- *Prestataires absents de la matrice* (`JUR-T08`) — alors que l'incident vient d'un compte de prestataire.
- *Conseil d'administration chargé de réaliser* — il approuve et contrôle, il n'exécute pas.
- *Recommandations irréalistes* (`JUR-G05` déséquilibres organisationnels et recommandations réalistes) — créer une direction de la sécurité de dix personnes pour une DSI de 14 agents ; juste : temps plein, rattachement, appui externe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Matrice RACI | répartition des rôles | F05 § 1 ; F02 § 0 ; glossaire | notion de cours |
| Rôles du responsable de la sécurité des SI, de la direction, des prestataires | positionnement, indépendance | F12 § 1 | notion de cours |
| Directive (UE) 2022/2555 (« NIS 2 ») | responsabilité et formation des organes de direction, en anticipation | `nis2` / F12 § 6.1 | en vigueur ; transposition due au 17/10/2024 |
| Transposition française de NIS 2 | statut au 31/12/2026 | `nis2_transposition_fr` / F12 § 6.2 | non transposée au 31/12/2026 |

---

## DOSSIER 3 – AUDITER LE PORTAIL DES ABONNÉS ET ORIENTER LA STRATÉGIE DE LA RELATION NUMÉRIQUE (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Démarche de la mission d'audit du portail | `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ; `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes | 2 |
| 3.2 Appréciation et diagnostic d'audit | `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse | 3 |
| 3.3 Veille technologique et stratégie de la relation numérique | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.d` Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques | 5 |
| 3.4 Gouvernance de la relation numérique | `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 3 |
| **Dossier 3 – Auditer le portail des abonnés et orienter la stratégie de la relation numérique** |  | **13** |

Répartition indicative : connaissances (audit du SI, critères d'appréciation, veille technologique active, stratégie du SI alignée, principes de gouvernance) 2,25 points (items 3.1 a-1, 3.2 a pour moitié, 3.3 a-1, 3.3 c-1, 3.4 b pour un quart) ; analyse des annexes et recommandations 10,75 points, soit environ 83 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Démarche de la mission d'audit du portail (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance » ; `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; « La conformité financière et comptable n'est pas traitée dans le programme de l'UE 5 » ; « L'audit SI suppose une approche multidisciplinaire et une posture critique vis-à-vis de la gouvernance ».

**Annexes mobilisées** : annexes 3.1 (fonctions, organisation, échanges avec la facturation, chiffres), 3.2 (constats, repères) et 1.1 (organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit du SI défini (examen indépendant et méthodique, au regard d'un référentiel, de la gouvernance, de la performance, de la sécurité et de la conformité du SI, conclu par des recommandations) | 0,5 |
| a-2 | Démarche appliquée au portail : objectifs de performance et de conformité, périmètre (inclus et exclus), étapes de la mission jusqu'au suivi, avec référentiels et livrables | 0,5 |
| b-1 | Cartographie du processus en cinq étapes, avec l'acteur et l'application de chaque étape (les échanges entre portail et facturation sont valorisés, non exigés) | 0,5 |
| b-2 | Trois contrôles internes précis, chacun rattaché à une étape ; 0,5 dès deux contrôles précis et rattachés | 0,5 |

Une copie qui énonce les étapes de la mission en une ligne chacune, avec au moins un livrable, obtient l'item a-2 : le détail de la réponse ci-dessous est indicatif, au regard des neuf minutes que laisse la question.

**Réponse attendue**

*3.1 a) – Définition et démarche de la mission*

L'**audit du système d'information** est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel (COBIT 2019, RGPD, contrat, engagements internes), la gouvernance, la performance (efficacité, efficience), la sécurité et la conformité d'un système ou d'un processus, et qui conclut par des recommandations hiérarchisées (F10 § 1.1). Il évalue le dispositif de contrôle interne sans s'y substituer (0,5 pt).

Appliqué au portail (0,5 pt) :
- **Mandant et auditeur** : la directrice générale, qui veut présenter les conclusions au conseil d'administration de juin 2027 ; le chargé de mission, rattaché à elle et indépendant de la direction de la clientèle et de la DSI, appuyé par la déléguée à la protection des données pour le volet RGPD.
- **Objectifs de performance** : fiabilité des données et des échanges entre le portail et la facturation (doublons, rejets, paiements enregistrés en retard) ; disponibilité au regard de l'engagement contractuel de 99,5 % ; efficacité du traitement des réclamations au regard de l'engagement de 8 jours ; satisfaction des utilisateurs (62 %, contre 75 % à l'accueil).
- **Objectifs de conformité** : RGPD (fiche du registre, durées de conservation, protection des données par défaut dans les choix d'alertes, contrat de sous-traitance avec VELIZANE) ; respect du contrat de l'éditeur et de la charte de service ; qualité de la gouvernance du portail (qui décide des évolutions).
- **Périmètre** : les six fonctions du portail, le module de prise de rendez-vous, les échanges de la nuit avec le logiciel de facturation et l'import des données de télérelève ; les processus « de la souscription au paiement » et de traitement des réclamations ; les acteurs (direction de la clientèle, accueil et centre d'appels, DSI, déléguée à la protection des données, VELIZANE) ; l'exercice 2026 et le début de 2027. **Exclus** : la sécurité technique de la solution de l'éditeur (aucune diligence technique sur ses serveurs), la supervision des installations, la tenue de la comptabilité.
- **Étapes** (six semaines environ, de mars à mi-avril 2027) : (1) **cadrage** : lettre de mission signée par la directrice générale (objectifs, périmètre, référentiels — COBIT 2019 pour la gouvernance et les services, ITIL pour les niveaux de service et les changements, RGPD, contrat VELIZANE, charte de service —, calendrier) ; (2) **prise de connaissance** : entretiens avec Mmes FARGEMONT, CORVESSE et BARJOLLE, des agents de l'accueil et l'agent de la DSI chargé des échanges, revue du contrat, du registre, des comptes rendus d'arbitrage ; (3) **analyse des risques** : cartographie du processus (question b) et des points de contrôle ; (4) **programme de travail et collecte** : revue documentaire, examen de la matrice des droits du portail, rapprochement sur échantillon des fichiers de plusieurs nuits avec la facturation, sondage sur les réclamations clôturées et sur les comptes d'anciens abonnés, analyse des relevés de disponibilité ; (5) **restitution** : constats validés contradictoirement avec les directions, diagnostic d'audit et note de synthèse à la directrice générale ; (6) **suivi** : plan d'action (responsable, échéance), point d'étape à six mois.
- **Livrables** : lettre de mission, cartographie du processus et des risques, programme de travail, feuilles de constats, diagnostic et note de synthèse, plan d'action.

*3.1 b) – Cartographie du processus « de la souscription au paiement » et contrôles internes*

| Étape | Acteur | Application | Échanges et points de risque |
|---|---|---|---|
| 1. Souscription du contrat | abonné (en ligne) ou agent de l'accueil | portail VELIZANE, puis logiciel de facturation | création du compte et transmission nocturne du contrat à la facturation ; risque de doublon (4 000 abonnés à deux comptes), de rejet |
| 2. Gestion du contrat (mensualisation, coordonnées bancaires, choix des alertes) | abonné ou agent de l'accueil et du centre d'appels | portail, puis facturation | modification des coordonnées bancaires par un profil unique de 35 agents ; choix d'alertes coché d'avance |
| 3. Relevé de la consommation | releveurs ou plateforme de télérelève ; service de la facturation | logiciel de facturation (index), portail (consommation affichée) | index relevés deux fois par an ou importés chaque mois |
| 4. Facturation et mise à disposition de la facture | service de la facturation | logiciel de facturation, puis portail (facture, alerte) | transmission nocturne au portail ; pics de connexion lors des deux vagues de facturation |
| 5. Paiement et suivi du compte | abonné ; prestataire de paiement ; service de la facturation | portail et prestataire de paiement, puis facturation | paiement transmis la nuit à la facturation ; rejets repris à la main en huit jours ; relances envoyées à tort |

La réclamation (portail, téléphone, accueil) peut intervenir à chaque étape ; la résiliation ferme la boucle et ouvre la question de la conservation des données (0,5 pt pour la cartographie).

Trois contrôles internes à vérifier (0,5 pt) :
1. **Étape 1 — contrôle d'unicité à la souscription** : avant la création d'un compte, rapprochement automatique avec les contrats existants (numéro de contrat, adresse du point de comptage) ; l'auditeur vérifie son existence et son effectivité sur un échantillon d'emménagements de 2026 (constat 1).
2. **Étape 5 (et 1, 2) — contrôle des échanges entre le portail et la facturation** : comptage des enregistrements et totaux de contrôle de chaque fichier, journal des rejets, délai et responsable de leur traitement, rapprochement des paiements reçus sur le portail et enregistrés dans la facturation ; l'auditeur rapproche les fichiers de quelques nuits (constat 1).
3. **Étape 2 — contrôle des habilitations** : profils séparés selon le moindre privilège, validation par un second agent de toute modification de coordonnées bancaires, confirmation à l'abonné, revue périodique des droits ; l'auditeur examine la matrice des droits et le journal des modifications (constat 5).

**Réponses tolérées**
- Démarche en cinq ou sept étapes (fusion de l'analyse des risques et du programme de travail, ou étape distincte de validation contradictoire), si le cadrage, la collecte, la restitution et le suivi y figurent.
- Cartographie en schéma (couloirs par acteur, flèches) ou dans une notation de processus, si les cinq étapes, les acteurs et les applications apparaissent.
- Étapes découpées autrement (création du compte distinguée de la souscription ; relevé et facturation regroupés, paiement et relance distingués), si le processus va de la souscription au paiement.
- Autre contrôle pertinent : suivi des réclamations sans clôture automatique (constat 6), traçabilité des choix d'alertes (constat 3), purge des comptes clos (constat 4).
- Référentiel d'audit autre que COBIT 2019, s'il est adapté à l'objet (engagements de la charte de service, contrat de l'éditeur).

**Erreurs fréquentes**
- *Méthodologie d'audit incomplète* (`JUR-A01` méthodologie structurée : périmètre, objectifs, étapes, livrables, échéancier) — étapes sans périmètre, sans livrables ni calendrier.
- *Audit de sécurité ou diligences techniques* — examen des vulnérabilités de la solution, essais d'intrusion ou de montée en charge ; juste : les diligences portent sur les processus, les contrôles et les documents ; la sécurité n'est appréciée qu'au travers des habilitations et de la traçabilité.
- *Audit du SI confondu avec l'audit des comptes* (`ET-34`) — vérification de la régularité des encaissements ou des comptes de la régie ; juste : fiabilité des échanges et du service.
- *Contrôle interne confondu avec l'audit* — « l'auditeur contrôle chaque paiement » ; juste : l'audit apprécie la conception et l'effectivité des contrôles mis en place par les directions.
- *Cartographie sans acteurs ni applications* (`JUR-G07` cartographie de processus) — liste d'activités qui ne montre ni qui agit ni où transitent les données.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI : définition, démarche, livrables | démarche de la mission | F10 § 1.1 et 1.2 | notion de cours |
| Contrôles applicatifs et contrôles des interfaces, habilitations | trois contrôles internes | F10 § 2 et 3.1 | notion de cours |
| COBIT 2019 (ISACA) | référentiel de gouvernance et de management | `cobit_2019` / F02 § 3 | en vigueur |
| ITIL (PeopleCert) | niveaux de service, changements | `itil` / F02 § 5 | en vigueur |

---

### 3.2 – Appréciation et diagnostic d'audit (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ».

**Annexes mobilisées** : annexes 3.2 (constats, repères au 31/12/2026) et 3.1 (chiffres, engagements, appels, satisfaction).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Quatre critères définis et chacun rattaché à au moins un constat de l'annexe 3.2 ; 0,5 pour deux ou trois critères | 1 |
| b-1 | Tableau de diagnostic pour quatre constats : critère juste, risque précis, recommandation opérationnelle, priorité ; 1 pour trois lignes, 0,5 pour deux | 1,5 |
| b-2 | Ordre de priorité justifié par des critères explicites (gravité, probabilité, nombre d'abonnés concernés, coût et délai de la mesure, caractère préalable aux projets du plan) | 0,5 |

**Réponse attendue**

*3.2 a) – Quatre critères d'appréciation*

| Critère | Définition | Constats rattachés (annexe 3.2) |
|---|---|---|
| **Fiabilité** | exactitude, complétude et cohérence des données et des traitements : une même information est juste et identique dans le portail et dans la facturation | 1 (4 000 abonnés à deux comptes, 150 rejets par nuit repris en huit jours, 900 paiements enregistrés en retard, 600 relances à tort) |
| **Efficacité** | atteinte des objectifs de service assignés au portail : disponibilité, délais, satisfaction (l'efficience rapporte en outre ces résultats aux moyens) | 2 (près de 90 heures d'interruption contre 45 au plus, dont 60 pendant les vagues de facturation) ; 6 (1 500 des 6 000 réclamations du portail, soit 25 %, clôturées sans réponse ; 18 jours pour un engagement de 8) |
| **Sécurité** | protection de la confidentialité, de l'intégrité et de la disponibilité des données, et traçabilité des actions | 5 (profil unique de 35 agents autorisés à modifier les coordonnées bancaires, sans validation ni revue ; deux modifications non demandées) |
| **Conformité au RGPD** | respect, démontrable, des obligations d'organisation du règlement : registre à jour, délais d'effacement définis, protection des données par défaut, contrat de sous-traitance, consultation du délégué à la protection des données | 4 (12 000 comptes d'anciens abonnés sans durée de conservation, dont 5 000 avec coordonnées bancaires ; pas de fiche au registre ; contrat muet sur le sort des données) ; 3 (case cochée d'avance, choix non tracé) |

(1 pt pour les quatre critères définis et rattachés ; 0,5 pt pour deux.)

*3.2 b) – Diagnostic d'audit*

| Constat | Critère | Risque | Recommandation | Priorité |
|---|---|---|---|---|
| **5 – Droits des agents** : profil unique pour 35 agents, modification des coordonnées bancaires sans validation ni information de l'abonné, aucune revue depuis 2020, deux modifications non demandées en 2026 | sécurité | détournement de prélèvements ou de remboursements par une modification frauduleuse ou erronée (déjà survenu deux fois) ; consultation abusive des données de 82 000 comptes ; actions sensibles non contrôlées | profils différenciés selon le moindre privilège (consultation pour tous ; modification des coordonnées bancaires réservée à quelques agents, validée par un second agent et confirmée à l'abonné par message ; clôture d'un compte ou d'une réclamation par un responsable) ; journal nominatif des modifications ; revue semestrielle des droits par la directrice de la clientèle avec la DSI | **1** — fin avril 2027 ; directrice de la clientèle et DSI |
| **1 – Doublons et échanges avec la facturation** : 4 000 abonnés à deux comptes, 150 rejets par nuit repris en huit jours, aucun total comparé, 900 paiements enregistrés en retard, 600 relances à tort | fiabilité | factures, paiements et relances erronés pour des milliers d'abonnés ; perte de confiance dans le portail (30 % des appels portent sur une de ses difficultés) ; toute fonction nouvelle (alertes quotidiennes de télérelève) bâtie sur des échanges non fiables | contrôles des échanges (comptages et totaux de contrôle, rapprochement quotidien des paiements, rejets traités sous 48 heures par un responsable désigné) ; contrôle d'unicité à la souscription et fusion des 4 000 doublons ; documentation de chaque échange avant toute évolution | **1** — fin juin 2027 ; DSI et service de la facturation |
| **4 – Comptes des anciens abonnés** : 12 000 comptes conservés sans durée, dont 5 000 avec coordonnées bancaires ; portail absent du registre ; contrat muet sur le sort des données | conformité au RGPD | conservation de données personnelles au-delà de ce que justifie la finalité ; exposition de ces données en cas de violation ; impossibilité de démontrer la conformité ; dépendance envers l'éditeur à la fin du contrat | fiche « portail des abonnés » au registre ; durées de conservation fixées par la régie, avec l'avis de la déléguée à la protection des données, pour chaque catégorie (compte, consommation, coordonnées bancaires, réclamations) ; suppression ou archivage des comptes clos au-delà de ces durées, puis purge automatique ; masquage immédiat des coordonnées bancaires des comptes clos ; avenant au contrat VELIZANE sur le sort des données | **2** — fin septembre 2027 (masquage immédiat) ; déléguée à la protection des données, directrice de la clientèle, DSI |
| **2 – Interruptions pendant les périodes de facturation** : près de 90 heures d'interruption, dont 60, soit les deux tiers, pendant les vagues de mars et de septembre ; disponibilité mesurée par le seul éditeur | efficacité | service indisponible quand les abonnés en ont le plus besoin, report des demandes sur un centre d'appels déjà saturé ; engagement de 99,5 % non tenu (deux fois plus d'interruption qu'admis) sans que la régie puisse le démontrer | mesure de la disponibilité par la régie elle-même et revue mensuelle des niveaux de service avec VELIZANE ; application des engagements du contrat ; calendrier des mises en service excluant les vagues de facturation (gestion des changements) ; envoi des factures étalé sur plusieurs jours ; plan de capacité demandé à l'éditeur | **2** — avant la vague de septembre 2027 ; DSI |

(1,5 pt pour quatre lignes complètes ; 1 pt pour trois ; 0,5 pt pour deux.)

**Ordre de priorité** (0,5 pt) : il croise la **gravité** de l'atteinte aux abonnés, la **probabilité** (le risque s'est-il déjà réalisé ?), l'**étendue** (nombre d'abonnés concernés), le **coût et le délai** de la mesure et son caractère **préalable** aux projets du plan. Les droits des agents viennent en premier : risque de fraude déjà réalisé deux fois, mesure rapide et peu coûteuse (paramétrage des profils et procédure de validation). Les échanges avec la facturation suivent : ils touchent des milliers d'abonnés et conditionnent toute fonction nouvelle, dont les alertes de télérelève. La conservation des données relève d'une décision à préparer avec la déléguée à la protection des données (priorité 2, avec une mesure conservatoire immédiate), et les interruptions ont une échéance naturelle, la vague de facturation de septembre 2027.

**Réponses tolérées**
- Constats 3 ou 6 retenus à la place d'un des quatre constats du corrigé : choix des alertes coché d'avance et non tracé (conformité au RGPD : case non cochée par défaut, historique daté de chaque choix, désinscription en ligne) ; réclamations non suivies (efficacité : suppression de la clôture automatique, outil unique pour tous les canaux, délai suivi chaque mois).
- Constat 5 rattaché aussi à la conformité au RGPD (accès aux données limité au nécessaire), ou constat 2 rattaché à la sécurité (disponibilité, volet de la triade confidentialité, intégrité, disponibilité), si le rattachement est justifié.
- Échelle de priorité différente (élevée, moyenne, faible ; court, moyen terme), et ordre différent s'il est justifié par des critères explicites.
- Diagnostic présenté sous forme de feuilles de constats (constat, cause, risque, recommandation, responsable, échéance).

**Erreurs fréquentes**
- *Constat sans risque ni recommandation opérationnelle* (`JUR-T03` analyser et argumenter) — « les droits sont trop larges, il faut les réduire » ; juste : risque concret pour les abonnés et la régie, mesure précise, responsable et échéance.
- *Recommandations non hiérarchisées* — toutes en priorité 1, ou ordre non justifié.
- *Dérive vers le droit des données personnelles* — bases légales, droits des abonnés, pouvoirs de l'autorité de contrôle ; juste : l'organisation de la conformité (registre, durées de conservation, protection par défaut, contrat de sous-traitance, rôle du délégué), le reste relevant de l'UE 1 (F15 § 9).
- *Délégué à la protection des données présenté comme responsable de la conformité* (`ET-29`) — c'est la régie, responsable du traitement, qui fixe les durées de conservation ; le délégué conseille et contrôle.
- *Critères confondus* — l'efficacité (atteinte des objectifs) prise pour l'efficience (rapport aux moyens), ou la fiabilité réduite à la disponibilité.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Critères d'audit ; feuille de constats (constat, risque, recommandation, priorité, responsable, échéance) | appréciation et diagnostic | F10 § 0, 1.2 et 5 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) : registre, délais d'effacement, protection par défaut, sous-traitance | critère de conformité | `rgpd` / F15 § 2, 4 et 5 | en vigueur |
| Proposition « omnibus numérique » COM(2025) 837 | non applicable au 31/12/2026 | `omnibus_numerique_donnees` / F15 § 8 | projet |
| Séparation des tâches, moindre privilège, revue des droits | constat 5 | F10 § 3.1 | notion de cours |

---

### 3.3 – Veille technologique et stratégie de la relation numérique (5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.d` « Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques ». Limites : « Ne pas confondre alignement stratégique et simple adéquation technique » ; « Ne pas se limiter à une veille passive : intégrer l'analyse prospective dans l'évaluation des opportunités SI ».

**Annexes mobilisées** : annexes 3.3 (technologies, attentes, sources de veille), 3.1 (chiffres du portail, appels, réclamations, satisfaction), 3.2 (constats 1 et 4) et 1.1 (plan « MORVÈZE EAU 2032 », télérelève).

**Barème indicatif (5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Veille technologique active définie (organisée, continue, orientée vers la décision, prospective) et opposée à la situation de la régie (veille passive, dépendante de l'éditeur) | 0,5 |
| a-2 | Dispositif complet appliqué au cas : axes, sources, outils, acteurs, fréquence, diffusion ; 0,5 pour trois ou quatre des six composantes | 1 |
| b-1 | Assistant conversationnel : valeur pour les abonnés, coûts (330 000 € sur trois ans et coûts internes), risques, effet sur le modèle de service | 1 |
| b-2 | Alertes et espace enrichi : valeur pour les abonnés, coûts (170 000 € sur trois ans et prérequis), risques, effet sur le modèle de service | 1 |
| c-1 | Stratégie du SI alignée définie (mise en cohérence permanente avec les objectifs métiers, technologies émergentes comprises ; modèle SAM) | 0,5 |
| c-2 | Deux orientations reliées aux priorités du plan et aux annexes, chacune avec la suite donnée à une technologie de l'annexe 3.3 ; 0,5 par orientation | 1 |

**Réponse attendue**

*3.3 a) – Veille technologique active et dispositif proposé*

La **veille technologique active** est un dispositif organisé et continu qui recherche, sélectionne, analyse et diffuse les informations sur les technologies susceptibles de modifier les services, les processus ou le modèle de l'organisation, pour éclairer ses décisions ; elle est prospective (elle évalue l'effet probable d'une technologie au regard des besoins et des risques) et s'oppose à la veille passive, qui reçoit les nouveautés au fil de l'eau (F01 § 0). À la régie, la veille est passive et fragmentée : revues lues « selon le temps disponible », congrès sans compte rendu, réseau de régies sans la DSI, et les deux propositions viennent des démonstrations commerciales de l'éditeur déjà en place, faute de responsable et d'espace commun (0,5 pt).

Dispositif proposé (1 pt) :
- **Axes de veille**, tirés du plan : relation numérique avec les abonnés (assistants, espaces personnalisés, canaux) ; valorisation des données de télérelève pour les abonnés ; inclusion et accessibilité des services en ligne ; protection des données et réglementation du numérique (avec la déléguée à la protection des données).
- **Sources** : les sources existantes, mieux exploitées (deux revues, congrès annuel, réseau des régies, que la DSI rejoint) ; des retours d'expérience organisés avec d'autres régies et services publics (dont la régie qui utilise l'assistant depuis 2026) ; plusieurs éditeurs et non le seul VELIZANE ; les publications des organismes professionnels et de l'autorité de contrôle ; les besoins exprimés par le comité des usagers et les motifs d'appels et de réclamations.
- **Outils** : un espace partagé de veille ; une fiche de veille type (technologie, besoin auquel elle répond, maturité, retours d'expérience, coûts, risques, prérequis du SI, conformité) ; une grille d'évaluation commune qui permet de comparer les opportunités ; des alertes thématiques et lettres d'information agrégées.
- **Acteurs** : un pilote de la veille (le chargé de mission ou un agent de la DSI) ; des correspondants dans la direction de la clientèle, la DSI et la direction de l'exploitation ; la déléguée à la protection des données pour la veille réglementaire ; la directrice générale comme commanditaire ; le comité des usagers comme source des besoins.
- **Fréquence** : collecte continue ; point mensuel des correspondants ; synthèse trimestrielle présentée au comité de la relation numérique (question 3.4) ; bilan annuel au conseil d'administration, avec le compte rendu du plan.
- **Diffusion et décision** : lettre de veille trimestrielle d'une page ; fiches d'opportunité soumises au comité, qui décide d'écarter, de surveiller ou d'expérimenter, avec des critères d'évaluation fixés à l'avance ; compte rendu des salons et des réunions du réseau versé dans l'espace commun.

*3.3 b) – Impact des deux technologies sur le modèle de service*

| Angle | Assistant conversationnel fondé sur l'IA générative | Alertes de surconsommation et espace enrichi par la télérelève |
|---|---|---|
| **Valeur pour les abonnés** | réponses jour et nuit aux questions courantes (factures, mensualisation, déménagement, restrictions), quand le centre d'appels ne décroche pas un appel sur quatre aux heures de pointe ; agents recentrés sur les cas complexes. Mais la valeur dépend de l'exactitude des réponses ; les abonnés âgés sans internet n'en tirent aucun bénéfice et le comité des usagers demande de pouvoir toujours parler à un agent | fuite après compteur signalée en quelques jours au lieu d'environ quatre mois (1 200 abonnés en 2026, 1 500 réclamations) ; consommation suivie jour par jour et messages ciblés lors des restrictions d'usage, attendus par les élus après la sécheresse ; service de conseil qui prolonge le plan ; valeur limitée aux 60 000 abonnés équipés jusqu'à la généralisation de 2029 |
| **Coûts** | 330 000 € sur trois ans (60 000 € + 3 × 90 000 €), auxquels s'ajoutent la mise à jour de la documentation, la supervision des réponses et la formation des agents ; gain incertain : les 40 % d'appels évités sont annoncés par l'éditeur, non démontrés, alors que 30 % des appels portent sur des difficultés du portail lui-même | 170 000 € sur trois ans (80 000 € + 3 × 30 000 €), plus l'échange quotidien avec la plateforme de télérelève (charge de la DSI, dont un seul agent suit les échanges) et les envois de SMS ; gains en réclamations évitées et en eau économisée chez l'abonné |
| **Risques** | réponses inexactes mais plausibles (environ une sur dix dans la régie qui l'utilise : démarches, dates de restriction), engageant la parole du service public ; données du compte transmises au modèle d'un fournisseur tiers dont l'hébergement n'est pas précisé (contrat de sous-traitance, analyse d'impact à envisager avec la déléguée à la protection des données) ; image d'un service « déshumanisé » redoutée par les élus ; dépendance accrue envers VELIZANE ; consommation d'énergie | alertes fausses ou manquées si les index sont incomplets ou si les échanges restent peu fiables (constat 1) ; consommations quotidiennes qui révèlent la présence ou l'absence au domicile (inquiétude du comité des usagers) : minimisation, accès restreint, durées de conservation courtes, comparaison avec d'autres foyers soumise au choix de l'abonné ; écart de service entre abonnés équipés ou non ; dépendance envers l'éditeur |
| **Effet sur le modèle de service** | du guichet et du téléphone vers le libre-service en ligne avec renvoi vers un agent : le rôle des agents évolue (supervision, cas complexes), ce qui suppose un accompagnement du changement | d'un service qui facture deux fois par an à un service qui accompagne l'abonné en continu : la régie devient conseillère de la consommation, en cohérence avec sa mission de service public après la sécheresse |

(1 pt par technologie analysée sous les trois angles, appliquée aux annexes ; 0,5 pt si un angle manque.)

*3.3 c) – Stratégie du SI alignée et deux orientations*

Une **stratégie du système d'information alignée** est un ensemble de choix (applications, données, organisation, compétences, partenaires) mis en cohérence de façon permanente avec les objectifs de l'organisation ; selon le modèle SAM de Henderson et Venkatraman (1993), l'alignement combine l'ajustement entre les choix externes et l'organisation interne et l'intégration entre domaine métier et domaine SI ; il intègre les opportunités des technologies émergentes sans se réduire à l'achat d'un outil (F01 § 1). Pour la relation avec les abonnés, l'objectif métier est fixé par le plan : moderniser la relation (40 % d'utilisateurs du portail), en valorisant les données de télérelève (0,5 pt).

Deux orientations (0,5 pt chacune) :
1. **Faire des données de télérelève un service de conseil à l'abonné, sur un socle fiabilisé et protecteur des données** (priorité « moderniser la relation avec les abonnés », en valorisant pour l'abonné les données des compteurs en télérelève que le plan déploie d'abord pour réduire les pertes du réseau ; les fuites après compteur, comptées dans les consommations, ne sont pas des pertes du réseau, mais leur détection répond à l'attente de sobriété exprimée après la sécheresse) : fiabiliser d'abord les échanges entre le portail, la facturation et la plateforme de télérelève et le compte unique de l'abonné (constat 1) ; protéger les données dès la conception (minimisation, choix de l'abonné, durées de conservation : constats 3 et 4). **Suite** : retenir le module d'alertes ; l'expérimenter au second semestre 2027 auprès d'abonnés volontaires équipés, une fois les échanges fiabilisés, avec la déléguée à la protection des données et le comité des usagers ; l'étendre au rythme de la généralisation de la télérelève jusqu'en 2029.
2. **Construire une relation multicanal inclusive, où le numérique libère du temps pour l'accompagnement humain** (priorité « moderniser la relation avec les abonnés », attentes des élus et des usagers) : même information et même suivi des réclamations sur le portail, au téléphone et à l'accueil (outil unique, constat 6), simplification des parcours du portail qui suscitent 30 % des appels, maintien d'un agent joignable et de l'accueil ; maîtrise de la dépendance envers l'éditeur (échanges documentés, données récupérables). **Suite** : ne pas généraliser l'assistant en 2027 ; traiter d'abord les causes des appels ; puis une expérimentation limitée aux questions générales (documentation publique, sans données du compte), avec renvoi visible vers un agent et des critères d'évaluation fixés à l'avance (exactitude des réponses, appels évités, satisfaction), après clarification de l'hébergement et du contrat de sous-traitance ; décision du comité de la relation numérique au vu des résultats, présentée au conseil d'administration.

**Réponses tolérées**
- Dispositif de veille piloté par la DSI seule, ou par un comité de veille, si les métiers et la déléguée à la protection des données y contribuent et si la diffusion vers la décision est organisée.
- Cycle de veille présenté en étapes (définir les besoins, collecter, analyser, diffuser, décider), si les cinq composantes demandées y figurent.
- Analyse d'une technologie sous la forme forces, faiblesses, opportunités, menaces, si la valeur, les coûts et les risques ressortent.
- Assistant retenu pour 2027 si le candidat le conditionne à une expérimentation limitée, à la validation des réponses, au maintien d'un agent joignable et à la clarification de l'hébergement des données.
- Orientations formulées autrement (« un portail fiable avant d'être riche », « la donnée au service de la sobriété des usages »), si chacune est reliée à une priorité du plan et indique la suite donnée à une technologie.
- Référence à la chaîne de valeur (Porter) ou à une perspective du modèle SAM (la technologie de télérelève ouvre un service nouveau), si elle est appliquée au cas.

**Erreurs fréquentes**
- *Veille passive ou réduite aux éditeurs* (`ET-19`) — « s'abonner à des revues » ou « suivre les propositions de VELIZANE » ; juste : axes, sources diversifiées, analyse, diffusion et décision.
- *Opportunités sans risques* (`ET-19`) — assistant présenté comme une économie certaine de 40 % des appels ; juste : gains annoncés à vérifier, réponses inexactes, données, inclusion, dépendance.
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — l'assistant « prédit les fuites » ; juste : il produit des réponses en langage courant, d'exactitude non garantie ; les alertes de télérelève reposent sur des règles de détection.
- *Alignement réduit à un choix d'outil* (`ET-06` ; `JUR-G02`) — « la stratégie consiste à acheter les deux modules » ; juste : orientations dérivées des objectifs du plan, technologies au service de ces orientations.
- *Schéma directeur complet* (`ET-07`) — diagnostic, cible, portefeuille et budget du SI de toute la régie ; juste : deux orientations de la relation numérique.
- *Analyse juridique de l'assistant* — qualification au regard de la réglementation de l'IA ; juste : risques de service, de données et de dépendance.
- *Fuites après compteur confondues avec les pertes du réseau* — « les alertes réduisent les pertes du réseau » ; juste : elles réduisent l'eau perdue chez l'abonné et les réclamations, et réutilisent les données du programme de télérelève.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Veille technologique active et analyse prospective | dispositif de veille | F01 § 0 (1.1.d) | notion de cours |
| Strategic Alignment Model (Henderson et Venkatraman, 1993) | stratégie du SI alignée | `henderson_venkatraman_1993` / F01 § 1 | modèle publié |
| Risques de l'IA générative (hallucination, confidentialité, dépendance, énergie) | analyse de l'assistant | F13 § 3 | notion de cours |
| Protection des données dès la conception, analyse d'impact, sous-traitance | conditions des deux technologies | `rgpd` / F15 § 3 à 5 | en vigueur |

---

### 3.4 – Gouvernance de la relation numérique (3 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ». Limite : « Le pilotage ESG est à comprendre dans une logique d'indicateurs intégrés, non isolés ».

**Annexes mobilisées** : annexes 3.1 (relations entre les directions, demandes d'évolution, arbitrages, module de rendez-vous), 3.3 (attentes, comité des usagers) et 1.1 (organigramme, conseil d'administration).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Trois enjeux relationnels tirés de l'annexe 3.1 (logiques opposées mais légitimes, absence d'instance et escalade vers la directrice générale, contournement de la DSI et dépendance envers l'éditeur) ; 0,5 pour deux enjeux | 1 |
| b | Gouvernance du SI définie (évaluer, diriger, surveiller ; distincte du management) et gouvernance à plusieurs niveaux associant le conseil d'administration, la directrice générale, les directions, la déléguée à la protection des données et le comité des usagers, chaque instance avec sa composition, son rôle et sa fréquence (les règles de décision sont valorisées, non exigées) | 1 |
| c | Un indicateur de performance et un critère de durabilité complets (formule, source, fréquence, cible, axe), reliés au cas ; 0,5 par indicateur | 1 |

**Réponse attendue**

*3.4 a) – Trois enjeux relationnels*

1. **Deux logiques légitimes mais opposées, sans lieu pour les concilier** : la direction de la clientèle porte la valeur pour les abonnés et la rapidité (« le service qu'ils trouvent auprès de leur banque ») ; la DSI porte la stabilité, la sécurité et la protection des données (« rien sans recette »). Chacune voit l'autre comme l'obstacle ou le risque : 40 demandes, 12 réalisées (30 %), 18 sans décision, et des interruptions que la DSI attribue à des échanges ajoutés sans documentation. La relation est de type client-fournisseur plutôt que partenaire.
2. **Une escalade vers la directrice générale, faute d'instance et de critères** : six arbitrages en 2026, au cas par cas et par courriel, sans connaissance des coûts ni des risques, que Mme ROCHEVAL ne veut plus rendre seule ; les décisions ne sont ni tracées ni expliquées ; le conseil d'administration n'a jamais examiné le portail, alors que le plan en fait une priorité.
3. **Un contournement qui ruine la confiance et renforce la dépendance envers l'éditeur** : le module de rendez-vous commandé directement à VELIZANE, sans la DSI ni la déléguée à la protection des données (informatique parallèle), n'est pas relié à l'agenda de l'accueil (200 abonnés concernés) ; la déléguée découvre les fonctions une fois en ligne ; l'éditeur, qui propose aussi les deux nouveaux modules, devient l'arbitre de fait des évolutions, ce que redoute la responsable de la DSI.

La réponse est donc une gouvernance partagée, non le choix d'un camp ni d'un outil (1 pt pour trois enjeux ; 0,5 pt pour deux).

*3.4 b) – Gouvernance de la relation numérique*

La gouvernance du SI est le système par lequel l'organe de direction **évalue**, **dirige** et **surveille** l'usage du SI au service de la stratégie (ISO/IEC 38500 ; domaine « évaluer, diriger et surveiller » de COBIT 2019) ; elle se distingue du management, qui planifie et exécute (F02 § 2).

| Instance | Composition | Rôle | Fréquence |
|---|---|---|---|
| **Conseil d'administration** | M. VAUQUIERS et les administrateurs ; présentation par la directrice générale | approuve les orientations de la relation numérique et leur enveloppe, examine le compte rendu (indicateurs, suites de l'audit, risques), décide des engagements significatifs (généralisation d'un module, assistant) | deux fois par an, dont la séance de juin 2027 |
| **Comité de la relation numérique** (niveau stratégique) | directrice générale (présidente), directrice de la clientèle, responsable de la DSI, déléguée à la protection des données (avis), directeur administratif et financier ; responsable de la sécurité des systèmes d'information invité ; chargé de mission (secrétariat) | arbitre le portefeuille des évolutions selon des critères partagés (valeur pour les abonnés, contribution au plan, coût, risques, capacité de la DSI), suit le plan d'action de l'audit et les indicateurs, décide des expérimentations issues de la veille ; décisions écrites et motivées, qui remplacent les arbitrages par courriel | trimestrielle |
| **Comité des usagers** (consultation) | Mme BRESSANDE et les représentants des associations ; directrice de la clientèle et déléguée à la protection des données | donne son avis sur les évolutions qui changent la relation (alertes, assistant, canaux non numériques, conservation des données) ; un panel d'usagers participe aux expérimentations et à leur évaluation ; avis transmis au comité et au conseil d'administration | deux fois par an et avant toute mise en service majeure |
| **Comité du portail** (niveau opérationnel) | responsable fonctionnel du portail (direction de la clientèle), agent de la DSI chargé des échanges, représentant de l'accueil ; VELIZANE selon l'ordre du jour ; déléguée à la protection des données consultée | file unique et priorisée des demandes d'évolution, recette conjointe, calendrier des mises en service hors périodes de facturation, revue des niveaux de service de l'éditeur | mensuelle |

**Règles et rôles** : la directrice de la clientèle est **propriétaire** du portail (elle porte le besoin, la valeur et la recette) ; la DSI est **garante** de l'architecture, des échanges, de la sécurité et de la relation technique avec l'éditeur ; la déléguée à la protection des données est consultée dès la conception ; aucune commande à l'éditeur sans passage par le comité du portail ; tout désaccord persistant remonte au comité de la relation numérique, non à la directrice générale seule (1 pt).

*3.4 c) – Un indicateur de performance et un critère de durabilité*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Délai moyen de traitement des réclamations** (performance) | somme des délais entre l'enregistrement de chaque réclamation et la réponse apportée à l'abonné / nombre de réclamations ayant reçu une réponse dans le mois ; les clôtures sans réponse sont comptées à part | outil unique de suivi des réclamations (module du portail étendu au téléphone et à l'accueil) | mensuelle | 8 jours au plus fin 2027, engagement de la charte de service (18 jours en 2026), et aucune réclamation close sans réponse | client |
| **Taux de satisfaction des abonnés reçus à l'accueil ou au téléphone** (durabilité : inclusion) | abonnés satisfaits / abonnés interrogés parmi ceux qui ont contacté l'accueil ou le centre d'appels | enquête de satisfaction de la direction de la clientèle | semestrielle | au moins 75 % (niveau de 2026), maintenu pendant toute la modernisation | social (ESG) |

(0,5 pt par indicateur complet et pertinent.)

Le premier mesure le résultat attendu des abonnés, sur lequel la clientèle et la DSI doivent coopérer (outil unique, fin de la clôture automatique). Le second traduit un critère de durabilité sociale : la modernisation ne doit pas dégrader le service rendu aux abonnés qui n'utilisent pas le portail, comme le demandent le comité des usagers et les élus (inclusion numérique, F14 § 4). Les deux figurent dans le même compte rendu au comité et au conseil d'administration, sans liste ESG isolée.

**Réponses tolérées**
- Instances nommées autrement (comité stratégique du numérique, comité de pilotage du portail), ou comité stratégique et comité du portail réunis en une instance pour une régie de cette taille, si les niveaux de décision et la place des usagers sont distingués.
- Organisation présentée en modèle bimodal (un mode stable pour la facturation, un mode exploratoire pour les services en ligne), si les règles de coordination sont précisées.
- Matrice de responsabilités (réalise, approuve, consulté, informé) en complément des instances.
- Indicateur fondé sur l'engagement de la charte, réclamation par réclamation : part des réclamations traitées en 8 jours au plus (cible 90 %, axe client), à la place du délai moyen ou en complément, une moyenne de 8 jours pouvant cacher des dépassements.
- Autre indicateur de performance complet : taux de disponibilité du portail mesuré par la régie (cible 99,5 %, axe processus) ; part des abonnés utilisant le portail (cible tirée du plan, axe client) ; délai de décision sur une demande d'évolution (axe processus).
- Autre critère de durabilité complet : part des démarches du portail également réalisables à l'accueil ou par téléphone (cible 100 %, axe social) ; volume d'eau des fuites après compteur détectées par alerte (axe environnement), si la formule et la source sont précisées.

**Erreurs fréquentes**
- *Prise de parti pour une direction* (`JUR-G05` déséquilibres organisationnels et recommandations réalistes) — « la DSI freine, il faut la contourner » ou « la clientèle doit attendre » ; juste : reconnaître deux logiques légitimes et organiser leur arbitrage.
- *Gouvernance sans les parties prenantes externes* — ni conseil d'administration ni comité des usagers, alors que la consigne et l'annexe 3.3 les désignent.
- *Gouvernance réduite à un outil ou à un comité informatique* (`ET-06`) — « un logiciel de gestion des demandes » ; juste : instances, rôles, règles de décision.
- *Indicateur incomplet ou générique* (`JUR-A02` ; `ET-18`) — « satisfaction » sans formule, source ni cible.
- *Critère de durabilité isolé* — un indicateur environnemental sans lien avec la relation numérique, présenté dans une liste à part (limite du programme : indicateurs intégrés).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 38500:2024 — gouvernance des technologies de l'information | évaluer, diriger, surveiller | `iso_38500_2024` / F02 § 4 | en vigueur |
| COBIT 2019 (ISACA), domaine « évaluer, diriger et surveiller » | gouvernance distincte du management | `cobit_2019` / F02 § 3 | en vigueur |
| Comitologie SI ; relations DSI, direction générale, métiers | instances et rôles | F02 § 6 ; F01 § 4 | notion de cours |
| Indicateurs d'inclusion (volet social de l'ESG) | critère de durabilité | F14 § 4 | notion de cours |
| Fiche d'indicateur à cinq champs | indicateurs | F09 § 4 | notion de cours |
