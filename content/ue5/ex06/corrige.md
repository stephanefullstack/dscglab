# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 6 — Dossier 3 (11 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 architecture, urbanisation et cloud, F05 projets et changement, F09 performance du SI, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Les statuts réglementaires à retenir sont ceux de l'annexe 3.3 ; toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Méthode de conduite du projet et cahier des charges | `1.5.a` Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ; `1.5.b` Méthodologies de gestion de projet (cycle en V, agile, hybride) ; `1.5.c` Élaboration d'un cahier des charges fonctionnel et technique | 3 |
| 3.2 Coût complet des deux options et souveraineté des données | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `2.3.d` Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique | 3 |
| 3.3 Plan qualité du projet | `1.5.f` Mise en œuvre et contrôle du plan qualité ; `1.5.a` Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable | 1,5 |
| 3.4 Pilotage des coûts et tableau de bord du SI | `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord ; `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ; `1.2.e` Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) | 3,5 |
| **Dossier 3 – Conduire le projet de plateforme pédagogique et piloter les coûts du SI** |  | **11** |

Répartition indicative : connaissances (méthodes de projet, rubriques du cahier des charges, TCO, plan qualité, contrôle de gestion du SI, structure d'un tableau de bord : items 3.1 a-1, 3.2 a-1, 3.4 a-1, et pour moitié 3.1 b, 3.3 a et 3.4 b-1) environ 2,5 points ; analyse des annexes et recommandations environ 8,5 points. Durée conseillée : 11 points × 4,5 minutes ≈ 50 minutes.

---

### 3.1 – Méthode de conduite du projet et cahier des charges (3 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.a` « Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable » ; `1.5.b` « Méthodologies de gestion de projet (cycle en V, agile, hybride) » ; `1.5.c` « Élaboration d'un cahier des charges fonctionnel et technique ».

**Annexes mobilisées** : annexes 3.1 (situation actuelle, calendrier, besoins exprimés, options, témoignages) et 1.1 (organisation de l'école et de la fonction informatique).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cycle en V, méthodes agiles (Scrum) et approche hybride caractérisés et comparés (principe, atouts, limites) | 0,5 |
| a-2 | Trois contraintes du projet tirées de l'annexe 3.1 | 0,5 |
| a-3 | Recommandation justifiée d'une approche hybride, avec ce qui relève du cycle en V, ce qui relève des itérations, et les rôles | 1 |
| b-1 | Cahier des charges fonctionnel : rubriques et deux exigences fonctionnelles du cas | 0,5 |
| b-2 | Cahier des charges technique : rubriques et deux exigences techniques du cas | 0,5 |

**Réponse indicative**

*3.1 a) – Choix de la méthode*

Trois familles de méthodes (0,5 pt) :
- le **cycle en V** enchaîne l'expression du besoin, les spécifications, la conception et la réalisation, puis remonte par des tests en miroir de chaque niveau jusqu'à la recette ; il convient à un besoin stable et bien connu, se contractualise facilement au forfait et documente la recette, mais il expose à l'effet tunnel : les écarts au besoin apparaissent tard ;
- les **méthodes agiles**, dont Scrum, livrent le produit par incréments au cours d'itérations courtes (sprints d'un mois au plus), à partir d'un carnet de produit priorisé par la valeur ; le *Product Owner* porte le besoin, le *Scrum Master* garantit le cadre, les développeurs réalisent l'incrément. Elles conviennent à un besoin évolutif, mais exigent des utilisateurs disponibles et un responsable du produit qui décide ;
- l'**approche hybride** conduit le cadrage et le socle en cycle en V (architecture, interfaces, reprise des données, recette d'ensemble) et les modules dont le besoin se découvre à l'usage en itérations.

Contraintes du projet (0,5 pt pour trois) :
- **une date impossible à déplacer** : mise en service pour tous les programmes à la rentrée de septembre 2028, contrat signé en septembre 2027 ; la directrice des programmes veut en outre un premier parcours vendable dès janvier 2028 ;
- **des besoins de deux natures** : un socle connu et stable (cours en ligne, intégration avec la scolarité, examens surveillés, accessibilité, reprise des 2 500 espaces de cours), à côté d'une offre aux entreprises dont les besoins « se découvriront avec les premiers clients » (Mme ROUVIÈRE) ;
- **une solution existante à paramétrer**, non un développement complet : progiciel en mode SaaS (A) ou solution libre complétée de quelques développements (B), avec un prestataire sous contrat ;
- **des ressources rares** : enseignants indisponibles pendant les examens et l'été, équipe du siège de six personnes qui « n'a jamais conduit un projet de cette taille » et doit faire tourner l'existant, aucun directeur des systèmes d'information (annexe 1.1).

Recommandation (1 pt) : une **approche hybride**.
- En **cycle en V**, avec des jalons fixes : cadrage et cahier des charges (avant le choix de juin 2027), contrat (septembre 2027), paramétrage et interface avec le progiciel de scolarité, reprise des espaces de cours (à vérifier par les enseignants entre février et avril 2028, hors des sessions d'examen et avant l'été), recette d'ensemble au printemps 2028, bascule en août 2028. Ce socle conditionne la rentrée : il doit être spécifié, contractualisé et recetté de façon complète.
- En **itérations courtes** : l'espace des entreprises clientes et les parcours de la formation des cadres, construits avec un premier parcours pilote dès le début de 2028, puis enrichis sprint après sprint à partir des retours des entreprises ; le *Product Owner* est désigné par la directrice des programmes, qui priorise le carnet de produit.
- Un **comité de pilotage** mensuel, présidé par Mme FERRIOL (sponsor), arbitre entre les deux volets ; la date de septembre 2028 est un jalon ferme, le contenu des itérations est la variable d'ajustement.

Un cycle en V intégral ne permettrait pas de livrer le parcours de janvier 2028 ni d'ajuster l'offre aux entreprises ; un projet entièrement agile laisserait sans engagement contractuel ni recette d'ensemble l'interface avec la scolarité et la reprise des contenus, dont dépend la rentrée.

*3.1 b) – Contenu du cahier des charges*

Le cahier des charges exprime le besoin de l'école (maîtrise d'ouvrage), indépendamment de la solution, et sert de base au choix, au contrat et à la recette ; chaque exigence est priorisée (par exemple selon la méthode MoSCoW) et assortie d'un critère d'acceptation vérifiable.

- **Partie fonctionnelle** (ce que la plateforme doit permettre) : contexte et objectifs mesurables (plan « LORVANNE 2030 », fin de vie de la plateforme de 2014), périmètre (programmes, formation des cadres, environ 6 000 utilisateurs), profils d'utilisateurs, processus cibles, exigences fonctionnelles priorisées, volumétrie, contraintes (calendrier, protection des données, accessibilité), critères d'acceptation. Exigences du cas, deux attendues : espace réservé à chaque entreprise cliente pour suivre l'assiduité et les résultats de ses cadres ; examens surveillés à distance avec enregistrement et visionnage des signalements par un surveillant ; application automatique du temps majoré ; inscription automatique de chaque étudiant aux cours de son programme (0,5 pt).
- **Partie technique** (contraintes d'environnement et de service) : mode d'hébergement et localisation des données, interfaces avec le progiciel de scolarité et les annuaires des comptes, performances et disponibilité, compatibilité avec les outils d'accessibilité et les téléphones mobiles, exigences de sécurité et de protection des données, reprise des données, réversibilité et formats, niveaux de service et assistance. Exigences du cas, deux attendues : création et suppression automatiques des comptes et transfert des notes vers le progiciel de scolarité, sans ressaisie ; 600 étudiants composant en même temps sans interruption ; disponibilité mesurée sur les plages d'usage et pendant les examens ; restitution des données dans des formats ouverts en fin de contrat ; navigation au clavier seul et avec un lecteur d'écran (0,5 pt).

**Réponses tolérées**
- Recommandation d'un **cycle en V** pour l'ensemble du projet, si le candidat organise un pilote de la formation des cadres avant la rentrée et justifie le choix par la date fixe et le contrat au forfait : 0,5 point sur l'item a-3.
- Kanban mentionné pour le suivi des demandes d'évolution après la mise en service : valorisé.
- Une exigence classée dans l'autre partie (l'accessibilité, fonctionnelle ou technique selon la formulation) : acceptée si elle est vérifiable.

**Erreurs types**
- *Agile confondu avec l'absence de méthode ou de cahier des charges* (`ET-32`) — « en agile, pas besoin de cahier des charges » ; juste : les itérations partent d'un carnet de produit priorisé, avec un responsable du produit et des critères d'acceptation.
- *Méthodes récitées sans lien avec le cas* (`JUR-T01`, `JUR-P02`) — phases du cycle en V décrites sans les contraintes de LORVANNE ; juste : le choix découle de la date fixe, de la nature des besoins et des ressources disponibles.
- *Rôles Scrum faux ou maîtrise d'ouvrage et maîtrise d'œuvre inversées* (`ET-32`) — « le Scrum Master est le chef de projet », « le fournisseur rédige le cahier des charges » ; juste : l'école, maîtrise d'ouvrage, exprime le besoin et recette ; le fournisseur, maîtrise d'œuvre, réalise.
- *Cahier des charges réduit à une liste de fonctions* — exigences sans priorité ni critère d'acceptation, ou cahier des charges qui décrit une solution ; juste : besoin exprimé, priorisé et vérifiable.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| *The Scrum Guide* (Schwaber et Sutherland, novembre 2020) | rôles, sprint d'un mois au plus, carnet de produit | `scrum_guide_2020` / F05 § 2.2 | en vigueur |
| Cycle en V, approche hybride, MoSCoW, cahier des charges | méthodes et critères de choix | F05 § 2 et § 3 | notions de cours |

---

### 3.2 – Coût complet des deux options et souveraineté des données (3 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ».
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.d` « Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique ».

**Annexes mobilisées** : annexes 3.1 (offres, caractéristiques des options, témoignages) et 3.3 (RGPD, décision d'adéquation, Data Act, SecNumCloud, référentiel du Cigref).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | TCO défini : coût complet sur le cycle de vie, postes, horizon, coûts cachés | 0,5 |
| a-2 | Offres (420 et 480 k€) puis TCO complets (810 et 750 k€) comparés et interprétés : le classement s'inverse | 0,5 |
| b | ROI discuté qualitativement : deux gains attendus et leurs conditions | 0,5 |
| c-1 | Localisation et droit applicable au fournisseur analysés (adéquation n'est pas immunité ; option irlandaise) | 0,5 |
| c-2 | Réversibilité et dépendance analysées (formats, assistance, Data Act, évolutions décidées par l'éditeur) | 0,5 |
| c-3 | Recommandation argumentée et assortie de conditions | 0,5 |

**Réponse indicative**

*3.2 a) – TCO des deux options*

Le coût total de possession (TCO) est le coût complet d'une solution sur son cycle de vie : acquisition, mise en œuvre (intégration, reprise des données, formation, conduite du changement), exploitation (hébergement, maintenance, assistance, administration interne), utilisation (temps des utilisateurs, indisponibilités) et sortie (réversibilité). Il se calcule sur un horizon donné, ici trois ans, sans actualisation, et inclut les **coûts cachés**, absents des offres mais supportés par l'organisation (0,5 pt).

| En k€, sur trois ans | Option A (SaaS) | Option B (libre, ARDÉVAL) |
|---|---|---|
| Total des offres | 420 | 480 |
| Reprise des contenus (prestation) | 60 | 20 |
| Temps des enseignants (5 000 h ou 1 250 h à 40 €) | 200 | 50 |
| Maintien de l'ancienne plateforme | 40 | 20 |
| Temps de l'équipe du siège (0,5 ou 1 poste à 60 k€ par an) | 90 | 180 |
| Coûts cachés | 390 | 270 |
| **TCO complet** | **810** | **750** |

Sur les seules offres, l'option A paraît moins chère de 60 k€ ; une fois les coûts cachés intégrés, l'option B l'est de 60 k€ : **le classement s'inverse**. Les coûts cachés représentent près de la moitié du TCO de A, dont 200 k€ de temps d'enseignants : c'est un coût d'opportunité plutôt qu'un décaissement, mais aussi un risque de calendrier, puisque les enseignants ne sont disponibles ni pendant les examens ni en été. L'hébergement en Irlande ajouterait 30 k€ à l'option A (840 k€). L'option A est presque entièrement en charges de fonctionnement (abonnement) ; l'option B comporte davantage de dépenses de mise en place (intégration, développements), puis des coûts récurrents proches de ceux de A : environ 150 k€ par an pour A et 160 k€ pour B, temps de l'équipe compris. L'écart tient donc surtout à la reprise des contenus (0,5 pt).

*3.2 b) – Retour sur investissement*

Le retour sur investissement rapporte les gains nets attendus au coût du projet. Il ne peut être chiffré ici : les gains principaux ne sont ni mesurés ni attribuables au seul projet, et les marges de la formation des cadres ne sont pas connues. Deux gains attendus, avec leurs conditions (0,5 pt) :
- **la croissance de la formation des cadres en ligne** (0,3 M€ en 2025-2026, 5 M€ visés en 2029-2030) : la plateforme en est une condition nécessaire mais non suffisante ; le gain dépend de l'offre de parcours, de l'effort commercial et de l'espace des entreprises clientes ;
- **des coûts et des risques évités** : renouvellement de serveurs hors garantie et d'une version qui n'est plus maintenue, interruptions pendant les examens (une dizaine d'heures en janvier 2027, dont la moitié pendant une session), ressaisie des notes et création hebdomadaire des comptes ; à condition que l'interface avec la scolarité fonctionne dès la rentrée ;
- autres gains qualitatifs : accessibilité pour 160 étudiants, satisfaction des étudiants et des enseignants, usage mobile, image de l'école face à ses concurrents.

Le projet se justifie donc comme un investissement stratégique au service du plan, dont les bénéfices seront suivis par des indicateurs (chiffre d'affaires en ligne, disponibilité pendant les examens, saisies supprimées) plutôt que par un ratio calculé a priori.

*3.2 c) – Informatique en nuage, souveraineté et recommandation*

La souveraineté numérique désigne la capacité de l'école à garder la maîtrise de ses données : où elles sont, quel droit s'applique au fournisseur qui les détient, et si elle peut en changer.

- **Localisation et droit applicable** (0,5 pt) : avec l'option A, les données d'environ 6 000 utilisateurs, leurs notes et les enregistrements vidéo des examens sont hébergés aux États-Unis. Le transfert est aujourd'hui permis, puisque l'éditeur adhère au cadre couvert par la décision d'adéquation du 10/07/2023 (annexe 3.3), mais ce cadre succède à un cadre invalidé en 2020 et peut l'être à son tour. Surtout, l'éditeur, de droit américain, reste soumis aux lois de son pays, y compris lorsqu'elles ont une portée extraterritoriale : l'option d'hébergement en Irlande améliore la localisation, pas l'immunité au droit étranger. L'option B, hébergée en France par une société française, y est beaucoup moins exposée ; seule une qualification SecNumCloud l'attesterait. L'absence de qualification SecNumCloud n'est pas rédhibitoire pour des données pédagogiques ; la grille du Cigref (sécurité, immunité, dépendance) peut servir à comparer les offres. Dans les deux cas, le fournisseur est sous-traitant de l'école, qui reste responsable de ses données et de leurs usages : un contrat conforme à l'article 28 du RGPD est nécessaire, et l'analyse d'impact s'impose pour la surveillance filmée des examens.
- **Réversibilité et dépendance** (0,5 pt) : l'option A limite la sortie à un export des notes au format tableur pendant 30 jours et à des cours dans le format propre de l'éditeur, l'assistance étant facturée en sus ; l'éditeur décide seul des évolutions. Changer de fournisseur reproduirait la reprise manuelle de 5 000 heures. Le Data Act, applicable depuis le 12/09/2025, facilite le changement de fournisseur d'informatique en nuage, mais la portabilité doit être organisée par le contrat. L'option B repose sur des formats ouverts, une restitution complète avec assistance et une licence libre : l'école peut changer d'hébergeur sans changer de plateforme. Sa dépendance tient aux développements propres d'ARDÉVAL (espace des entreprises, transfert des notes), à documenter et à livrer sous licence libre.
- **Recommandation** (0,5 pt) : retenir l'**option B**, moins chère en coût complet, plus réversible et plus souveraine, sous trois conditions : un pilote sur un parcours de la formation des cadres dès février 2028 (un mois après le souhait de la directrice des programmes), sur un environnement où les espaces de cours sont repris à blanc, pour que les enseignants vérifient les 1 250 heures de reprise entre février et avril 2028, hors des sessions d'examen et avant l'été, avec une décision de poursuite au printemps 2028 ; des jalons contractuels fermes, car la mise en service complète de mai 2028 ne laisse que quatre mois, qui coïncident avec les examens et l'été ; un poste à temps plein affecté au pilotage d'ARDÉVAL au siège, sans quoi l'existant en pâtira. Les coûts de l'option A ne couvrent ni l'hébergement dans l'Union européenne ni une réversibilité réelle.

**Réponses tolérées**
- Recommandation de l'**option A**, si le candidat la justifie par le calendrier (marge de huit mois, toutes les fonctions en standard, application mobile, ou relève que la marge de B coïncide avec les périodes où les enseignants ne sont pas disponibles) et l'assortit de conditions sur la souveraineté (hébergement en Irlande, export des cours dans un format ouvert, assistance à la sortie comprise) : 0,5 point sur l'item c-3.
- Temps des enseignants exclu du TCO et traité comme un coût d'opportunité, si le candidat le signale et en tire la conséquence sur le calendrier (offres 420 et 480, autres coûts cachés 190 et 220, TCO 610 et 700) : accepté sur l'item a-2.
- Données des 160 étudiants bénéficiant d'un aménagement : le candidat qui demande de n'enregistrer que l'aménagement (temps majoré), sans son motif, et d'inclure ce point dans l'analyse d'impact est valorisé.
- Temps de l'équipe du siège pendant l'année de mise en place (2027-2028) ajouté au TCO, posé comme hypothèse : accepté, l'annexe comptant trois années d'utilisation.
- Mention du modèle de responsabilité partagée de l'informatique en nuage et de la distinction SaaS / hébergement d'une solution libre (IaaS ou PaaS chez l'hébergeur) : valorisée.
- Délai de récupération évoqué en principe, sans chiffrage : valorisé.

**Erreurs types**
- *TCO réduit au prix des offres* (`ET-33`, `JUR-A03`) — comparer 420 et 480 k€ et conclure en faveur de A ; juste : intégrer la reprise des contenus, le temps des enseignants et de l'équipe, et le maintien de l'ancienne plateforme.
- *TCO et ROI confondus, ou TCO actualisé* (`ET-33`) — « le ROI de l'option B est de 60 k€ » ; juste : le TCO est un coût complet non actualisé, le ROI rapporte des gains à un coût.
- *Hébergement souverain confondu avec hébergement en Europe ou en France* (`ET-37`) — « avec l'option irlandaise, l'option A devient souveraine » ; juste : le droit applicable au fournisseur compte autant que la localisation.
- *En SaaS, la responsabilité des données est celle du fournisseur* (`ET-30`, `JUR-G11`) — juste : l'école reste responsable de ses données, des comptes et des usages ; le fournisseur est sous-traitant.
- Hors sujet : analyser le contrat comme un juriste ou développer le droit des transferts de données (UE 1) ; le dossier attend l'enjeu de maîtrise des données.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| TCO, coûts cachés, CAPEX / OPEX, ROI | coût complet sur trois ans | F09 § 3 | notions de cours |
| RGPD, règlement (UE) 2016/679 | transferts hors de l'Union, sous-traitant (art. 28), analyse d'impact | `rgpd` / F15 | en vigueur |
| Décision d'adéquation UE-États-Unis du 10/07/2023 | transferts vers les organisations adhérentes | `dpf_ue_usa_2023` / F15 | en vigueur |
| Règlement (UE) 2023/2854 (Data Act) | changement de fournisseur d'informatique en nuage | `data_act` / F03 § 5.3 | applicable depuis le 12/09/2025 |
| SecNumCloud, version 3.2 (ANSSI) | qualification des offres de confiance | `secnumcloud_3_2` / F03 § 5.3 | en vigueur |
| Référentiel du cloud de confiance du Cigref | sécurité, immunité, maîtrise de la dépendance | `cigref_cloud_confiance` / F03 § 5.3 | publié |

---

### 3.3 – Plan qualité du projet (1,5 point)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.f` « Mise en œuvre et contrôle du plan qualité » ; `1.5.a` « Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ».

**Annexes mobilisées** : annexe 3.1 (besoins exprimés, calendrier, témoignages).

**Barème indicatif (1,5 pt)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Responsabilités du projet réparties (sponsor, comité de pilotage, maîtrise d'ouvrage et utilisateurs clés, maîtrise d'œuvre), appliquées aux acteurs du cas | 0,5 |
| b | Recette organisée (technique, fonctionnelle, accessibilité, examen blanc, procès-verbal) et trois critères d'acceptation vérifiables | 0,5 |
| c | Un indicateur de qualité complet (formule, source, fréquence, cible, axe), relié à un critère d'acceptation | 0,5 |

**Réponse indicative**

Le plan qualité du projet fixe l'organisation, les règles et les contrôles qui garantissent que la plateforme livrée répond au cahier des charges : rôles, revues, gestion des changements, plan de tests et recette, critères d'acceptation et indicateurs.

- **Responsabilités** (0,5 pt) : Mme FERRIOL, sponsor, arbitre et préside le comité de pilotage mensuel (directrice des programmes, directeur administratif et financier, directeurs de campus, chef de projet, fournisseur) ; la directrice des programmes porte la maîtrise d'ouvrage et désigne le responsable du produit pour l'offre aux entreprises ; les utilisateurs clés rédigent et exécutent les cas de test : M. TERVILLAC pour les enseignants, la scolarité pour l'interface et les notes, Mme FAVRIGNY pour l'accessibilité, une ou deux entreprises clientes pour le pilote ; le fournisseur, maîtrise d'œuvre, réalise et conduit la recette technique ; M. CORNAVIN et l'équipe du siège pilotent l'interface avec le progiciel de scolarité ; la personne chargée de la protection des données est consultée sur la surveillance filmée des examens. Un tableau RACI formalise ces rôles.
- **Recette et critères d'acceptation** (0,5 pt) : recette technique par le fournisseur, puis recette fonctionnelle par l'école sur un cahier de recette dont chaque cas de test est relié à une exigence ; recette d'accessibilité menée par la référente handicap avec des étudiants concernés ; examen blanc en conditions réelles ; reprise des contenus à blanc puis vérifiée par chaque enseignant ; anomalies classées (bloquante, majeure, mineure) ; procès-verbal de recette, avec ou sans réserves, et décision de mise en service par le comité de pilotage avant l'été 2028. Trois critères d'acceptation parmi : toutes les exigences essentielles validées et aucune anomalie bloquante ouverte ; un examen blanc de 600 étudiants simultanés sans interruption, avec transfert automatique des notes au progiciel ; des parcours types utilisables au clavier seul et avec un lecteur d'écran, validés par Mme FAVRIGNY ; tous les espaces de cours repris validés par leur enseignant.
- **Indicateur de qualité** (0,5 pt pour un indicateur complet, relié à un critère d'acceptation) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de réussite des cas de test des exigences essentielles | cas de test réussis des exigences essentielles / cas de test des exigences essentielles | cahier de recette et outil de suivi des anomalies | hebdomadaire pendant la recette | 100 % et aucune anomalie bloquante ouverte avant le procès-verbal de recette (printemps 2028) | processus |

**Réponses tolérées**
- Autres indicateurs complets : taux d'espaces de cours repris et validés par leur enseignant (espaces repris et validés / 2 500 espaces actifs ; tableau de suivi de la reprise des contenus ; hebdomadaire ; 100 % fin avril 2028 ; processus), nombre d'anomalies bloquantes ouvertes (cible 0 à la mise en service), taux de disponibilité pendant l'examen blanc (cible 100 %), part des parcours types validés en accessibilité (cible 100 %), taux de notes transférées sans ressaisie (cible 100 %) ; axe « client » accepté pour un indicateur tourné vers les utilisateurs.
- Mention de la norme ISO 9001 (édition 2026) comme cadre de management de la qualité : valorisée sans être exigée.
- Mention de la maintenance corrective et évolutive après la mise en service : valorisée.

**Erreurs types**
- *Recette confondue avec les tests du fournisseur* — laisser au seul prestataire la validation de la plateforme ; juste : la recette fonctionnelle appartient à la maîtrise d'ouvrage et se conclut par un procès-verbal.
- *Indicateurs génériques* (`ET-18`, `JUR-A02`) — « taux de satisfaction » sans formule, source ni cible ; juste : indicateur relié à un critère d'acceptation du projet.
- *Plan qualité réduit à une norme* (`ET-01`) — « appliquer ISO 9001 » ; juste : rôles, recette, critères et indicateurs propres au projet ; la norme n'en est qu'un cadre possible.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Plan qualité, recette, procès-verbal, RACI | organisation de la qualité du projet | F05 § 1 et § 6 | notions de cours |
| ISO 9001:2026 — Systèmes de management de la qualité | cadre de management de la qualité (réponse tolérée) | `iso_9001_2026` / F05 § 6 | en vigueur |

---

### 3.4 – Pilotage des coûts et tableau de bord du SI (3,5 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ».
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.e` « Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) ».

**Annexes mobilisées** : annexes 3.2 (tableau de bord, budget du SI par nature et par entité, consommation électrique), 1.1 (chiffres clés, fonction informatique) et 3.1 (plateforme, options).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fondamentaux du contrôle de gestion du SI : coût complet, centres de coûts, inducteurs, répartition ou refacturation, lien entre coût et valeur | 0,5 |
| a-2 | Trois critiques du tableau de bord actuel, chacune fondée sur l'annexe 3.2 | 0,5 |
| a-3 | Méthode de répartition des coûts entre les campus et inducteurs justifiés | 0,5 |
| b-1 | Structure du tableau de bord : destinataire, fréquence, axes, équilibre performance / risques / coûts, ESG intégré | 0,5 |
| b-2 | Cinq indicateurs complets couvrant les quatre dimensions (voir la gradation) | 1,5 |

**Gradation de la notation** (item b-2) : 0,5 point pour deux ou trois indicateurs complets et pertinents ; 1 point pour quatre, ou pour cinq qui ne couvrent pas les quatre dimensions ; 1,5 point pour cinq indicateurs complets couvrant la performance, les risques, les coûts et l'ESG. Un indicateur auquel manque la formule, la source, la fréquence, la cible ou l'axe n'est pas compté.

**Réponse indicative**

*3.4 a) – Contrôle de gestion du SI, critique et répartition*

Le contrôle de gestion appliqué au système d'information vise à connaître le coût complet des services informatiques (coûts directs, indirects et cachés), à le rattacher aux services rendus et aux entités qui les consomment au moyen de centres de coûts et d'inducteurs, éventuellement à le répartir ou à le refacturer, et à le rapprocher de la valeur produite (niveau de service, contribution à la stratégie), au moyen d'indicateurs assortis de cibles. Le budget du SI de LORVANNE, 2,9 M€, représente environ 4 % des produits, dont 0,4 M€ seulement (14 %) pour des projets nouveaux (0,5 pt).

Critiques du tableau de bord actuel, trois attendues (0,5 pt) :
- **des indicateurs techniques, d'activité et sans cible** : tickets, postes, serveurs et téraoctets décrivent un volume, pas une performance ; aucun ne mesure la satisfaction, le délai de résolution ou la contribution au plan « LORVANNE 2030 », et aucun n'a de cible ;
- **des mesures qui masquent les problèmes** : une disponibilité de 98,6 % mesurée 24 heures sur 24 en janvier correspond à une dizaine d'heures d'interruption, dont la moitié pendant les examens en ligne ; mesurée sur les plages d'usage et les sessions d'examen, la performance serait jugée tout autrement ;
- **un périmètre incomplet et aucune donnée de coût** : les demandes traitées par les campus ne figurent pas dans le tableau de bord ; les dépenses des campus ne sont consolidées qu'à la clôture ; le 1,7 M€ du siège (près de 60 % du budget) n'est rattaché à aucun service ni réparti ; aucun indicateur de risque ni d'environnement, alors que la consommation des salles est connue (200 MWh) ;
- **un destinataire unique** : adressé au seul directeur administratif et financier, le tableau de bord ne sert ni la direction générale ni les directeurs de campus, qui ignorent ce que l'informatique leur coûte.

Méthode de répartition (0,5 pt) : regrouper les dépenses du SI, siège et campus, en **centres de coûts par service** (postes de travail et assistance, applications de gestion, plateforme pédagogique, réseau et liaisons entre campus), consolidés chaque trimestre ; répartir le coût de chaque service entre les campus et la formation des cadres selon un **inducteur** représentatif de sa consommation :
- plateforme pédagogique : nombre d'utilisateurs actifs, ou à défaut d'étudiants (2 900, 1 400 et 600), les cadres en formation étant imputés à la formation des cadres ;
- postes de travail et assistance : nombre de postes (800, 400 et 200), puis nombre de demandes lorsqu'un outil commun les comptera ;
- applications de gestion : nombre d'étudiants ou d'utilisateurs.

Les campus n'étant pas des entités juridiques distinctes, il s'agit d'une **répartition analytique** plutôt que d'une facturation ; elle se fait à un coût standard fixé en début d'exercice, pour ne pas reporter sur les campus les inefficacités de l'informatique, et elle est validée par le comité de direction. Elle rend visibles des écarts aujourd'hui ignorés : avant toute répartition du siège, le SI du campus de Chalon-sur-Saône coûte environ 330 € par étudiant, contre 200 € environ à Dijon (0,2 M€ pour 600 étudiants, contre 0,6 M€ pour 2 900).

*3.4 b) – Structure et indicateurs du tableau de bord du SI*

Structure (0,5 pt) : un tableau de bord stratégique du SI, présenté chaque trimestre au comité de direction, limité à une douzaine d'indicateurs, organisé selon les axes du tableau de bord prospectif adaptés au SI (IT Balanced Scorecard de Van Grembergen, d'après Kaplan et Norton) : contribution financière, utilisateurs, processus, orientation future ; les indicateurs ESG sont intégrés à ces axes et non isolés. Chaque indicateur porte une cible, un seuil d'alerte et un responsable ; le tableau équilibre performance, risques et coûts. Les indicateurs techniques actuels restent dans le tableau de bord opérationnel des équipes. Dans le tableau ci-dessous, la colonne « Axe » emploie les noms usuels du tableau de bord prospectif (financier, client, processus) ou, pour les indicateurs de risque et d'ESG, la dimension ESG qu'ils portent : l'indicateur de risque relève de l'axe processus (dimension gouvernance), l'indicateur ESG de l'axe orientation future ou processus (dimension environnement). Les deux façons de nommer les axes sont acceptées.

Indicateurs (1,5 pt selon la gradation) :

| Dimension | Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|---|
| Coûts | Coût complet du SI par étudiant | dépenses du SI consolidées (siège et campus) / nombre d'étudiants inscrits | comptabilité analytique, centres de coûts du SI | trimestrielle | au plus 600 € par étudiant en 2028-2029 (environ 590 € en 2025-2026), malgré la nouvelle plateforme | financier |
| Performance | Disponibilité de la plateforme pédagogique sur les plages d'usage | heures de disponibilité sur les plages d'usage (7 h – 23 h et sessions d'examen) / heures des plages d'usage | rapports de niveau de service du fournisseur, contrôlés par l'école | mensuelle | au moins 99,5 % et aucune interruption pendant une session d'examen | processus |
| Performance | Taux de demandes résolues dans le délai convenu, tous campus | demandes résolues dans le délai convenu / demandes closes au siège et sur les campus | outil commun de suivi des demandes, à mettre en place | mensuelle | au moins 90 % à la rentrée 2028 | client |
| Risques | Part des applications critiques réversibles et hébergées dans l'Union européenne | applications critiques dotées d'une clause de réversibilité et dont les données sont hébergées dans l'Union / applications critiques inventoriées | inventaire des applications et registre des contrats | semestrielle | 100 % en 2029 | gouvernance |
| ESG | Consommation électrique du SI, hébergement externe compris | consommation relevée dans les salles informatiques de l'école + consommation déclarée par les hébergeurs pour les services de l'école (MWh) | compteurs des salles et déclarations contractuelles des hébergeurs | trimestrielle | au plus 150 MWh en 2029-2030 (200 MWh en 2025-2026) | environnement |

La part du budget consacrée aux projets nouveaux (14 % en 2025-2026) et le chiffre d'affaires de la formation des cadres en ligne peuvent compléter l'axe « orientation future ».

**Réponses tolérées**
- Autres indicateurs complets et contextualisés : part du budget du SI consacrée aux projets nouveaux (cible 25 % en 2029-2030), satisfaction des étudiants et des enseignants à l'égard de la plateforme (enquête annuelle), part des parcours en ligne conformes aux exigences d'accessibilité (axe social, cible 100 %), durée moyenne d'usage des postes remplacés (axe environnement), coût de la plateforme par utilisateur actif.
- Un indicateur de risque lié à la sécurité (part des comptes désactivés au départ de leur titulaire, par exemple) : accepté pour la dimension « risques ».
- Refacturation interne à un coût standard proposée au lieu d'une répartition analytique, si le candidat en montre l'effet sur la responsabilisation des campus : accepté.
- Axes « parties prenantes » ou « ESG » nommés comme un cinquième axe, si les indicateurs y restent reliés aux autres axes.

**Erreurs types**
- *Tableau de bord limité aux indicateurs techniques ou indicateurs génériques* (`ET-18`, `JUR-A02`) — reprendre tickets et serveurs en ajoutant des cibles ; juste : indicateurs de performance, de qualité de service, de coût et de risque, reliés aux objectifs de l'école.
- *Indicateurs ESG isolés* (`ET-18`) — une liste « verte » séparée du tableau de bord ; juste : indicateurs ESG intégrés aux axes et suivis par le même comité.
- *Empreinte déplacée prise pour une empreinte réduite* — se féliciter de la baisse de consommation des salles de l'école après le départ des serveurs de la plateforme ; juste : l'externalisation déplace la consommation chez l'hébergeur, qui doit être mesurée.
- *Contrôle de gestion du SI réduit au suivi du budget* (`ET-33`) — juste : coût complet par service, inducteurs, lien entre coût et valeur ; le calcul d'écarts n'est pas attendu dans cette UE.
- *Répartition sans inducteur ou à parts égales* (`JUR-A03`) — « chaque campus paie un tiers » ; juste : un inducteur qui reflète la consommation (étudiants, postes, demandes).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| IT Balanced Scorecard (Van Grembergen, 2001) | axes du tableau de bord du SI | `van_grembergen_it_bsc` / F09 § 4.1 | modèle théorique |
| Balanced Scorecard (Kaplan et Norton, 1992) | tableau de bord prospectif | F09 § 4.1 | modèle théorique |
| Contrôle de gestion du SI : centres de coûts, inducteurs, refacturation | fondamentaux | F09 § 2 | notions de cours |
