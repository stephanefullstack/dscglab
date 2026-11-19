# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 35 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F09 performance du SI, F13 intelligence artificielle, F15 RGPD opérationnel, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le référentiel des articles et les échanges avec les places de marché | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) | 4 |
| 2.2 Les délais de vente, les retours et les outils d'analyse | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 4,5 |
| 2.3 La gouvernance des données | `2.3.a` Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques ; `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) | 2 |
| 2.4 Le projet de studio de mise en ligne | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI | 2,5 |
| **Dossier 2 – Organiser et exploiter les données des articles et des ventes** |  | **13** |

Répartition indicative : connaissances (données de référence, dictionnaire de données, interopérabilité, chaîne de traitement, analyses descriptive et exploratoire, gouvernance des données et ses rôles, DAMA-DMBOK, retour sur investissement et délai de récupération) environ 3,5 points (item 2.1 b-1 et la moitié des items 2.1 a-1, 2.1 c-1, 2.2 a-1, 2.2 a-2, 2.3-1, 2.3-4 et 2.4 a-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 9,5 points, soit environ 73 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le référentiel des articles et les échanges avec les places de marché (4 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) ». L'approfondissement technique des échanges est exclu ; l'interopérabilité est traitée sur les plans technique et organisationnel. Aucun modèle des données n'est demandé.

**Annexes mobilisées** : annexes 1.1 (modèle d'activité, canaux de vente, système d'information, organigramme), 2.1 (trois descriptions de l'article, constats de mars 2027, témoignages), 2.2 (ventes annulées par canal) et 2.5 (principes du RGPD, DAMA-DMBOK).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Données de référence définies ; référentiel des articles, seule source qui fait foi pour la description de chaque article, alimentant le site, l'application, les boutiques et les places de marché ; justifié par deux constats chiffrés de l'annexe 2.1 (trois descriptions, 2 300 libellés pour 400 marques, 100 fiches sur 500 à l'état trop favorable, 900 ventes en double) | 0,5 |
| a-2 | Identifiant de l'article attribué une seule fois, non signifiant, stable même après un retour, jamais réattribué, avec les autres numéros rattachés ; trois attributs normalisés (marque et modèle, état, et un autre attribut à liste de valeurs) avec leur règle | 0,5 |
| a-3 | Résultat de l'authentification enregistré dans le référentiel et rattaché à l'article (statut, auteur, date, observations, photographies de contrôle) ; étapes du cycle de l'article sous forme de statuts, avec le cycle de la future place de marché (annonce, vente, authentification, livraison) | 0,5 |
| b-1 | Dictionnaire de données défini (description partagée de chaque donnée : nom, définition, format, domaine de valeurs, règle, source, propriétaire, règle de qualité) et distingué d'un modèle des données | 0,5 |
| b-2 | « État de l'article » et « article disponible » : définition commune, règle, propriétaire, règle de qualité | 0,5 |
| b-3 | « Date de mise en vente » : définition commune, règle, propriétaire, règle de qualité ; cohérence d'ensemble des trois fiches | 0,5 |
| c-1 | Interopérabilité définie, avec ses plans ; API et format ouvert définis ; interface de programmation avec A et C, fichier en format ouvert toutes les heures avec B, disponibilité tenue par le référentiel et transmise à chaque réservation ou vente | 0,5 |
| c-2 | Deux conditions organisationnelles (correspondance des catégories et des échelles d'état, convention d'échange et suivi des rejets, données des vendeurs limitées au nécessaire, règle de retrait des articles de valeur) | 0,5 |

**Réponse attendue**

*2.1 a) – Le référentiel des articles, l'identifiant, les attributs, l'authentification et le cycle de l'article*

**Le constat** : un article unique est décrit trois fois, par trois équipes, sous trois numéros (annexe 2.1 A). La ressaisie produit des écarts : 2 300 libellés de marque pour environ 400 marques réelles, un même modèle de sac sous 17 libellés, une fiche sur cinq (100 sur 500) qui affiche un état plus favorable que celui noté par l'atelier. Le résultat de l'authentification, cœur du métier, vit dans un tableur déjà écrasé une fois. La disponibilité est transmise une fois par nuit, d'où 900 articles vendus deux fois en 2026.

**Le référentiel des articles** (0,5 pt) : les **données de référence** sont les données partagées et stables dont plusieurs processus ont besoin ; elles sont gérées dans un **référentiel unique**, qui fait foi (F07 § 1). Pour ORSALIE :
- un **référentiel des articles** devient la **seule source** de la description de chaque article. Il est créé à la réception, enrichi par l'atelier puis par le catalogue, et il **alimente** sans ressaisie le site et l'application, le logiciel de caisse et les annonces des places de marché ;
- une donnée est saisie **une fois, là où elle naît** : la marque et le modèle à la réception, l'état et l'authentification à l'atelier, la description, les photographies et le prix au catalogue ; une correction faite dans le référentiel se propage à tous les canaux ;
- le référentiel peut être porté par le logiciel des dépôts, à faire évoluer, ou par le futur catalogue du site refondu : l'essentiel est qu'il n'y en ait **qu'un**, et que les autres logiciels le consultent au lieu de garder leur propre copie modifiable.

**L'identifiant et trois attributs normalisés** (0,5 pt) :
- l'**identifiant de l'article** est attribué **une seule fois**, à la première réception (ou, demain, à la publication de l'annonce par le vendeur). Il est **unique**, **non signifiant** (ni marque, ni date, ni code de boutique) et **stable** : un article retourné par un client garde son identifiant, ses photographies et son historique, au lieu de recevoir un nouveau numéro de réception (annexe 2.1 B). Il n'est **jamais réattribué**. Le numéro de réception de chaque arrivée, la référence du site et les références des places de marché A, B et C sont conservés comme **références rattachées** ;
- trois **attributs normalisés**, parmi :
  1. **marque et modèle**, choisis dans une **liste de référence** des marques et des modèles tenue par le catalogue avec l'atelier, au lieu du texte libre : une nouvelle marque est créée après vérification, et les 2 300 libellés sont ramenés aux 400 marques réelles ;
  2. **état**, noté sur **une seule échelle** commune à l'atelier et au catalogue, avec une table de correspondance vers les échelles des places de marché (question b) ;
  3. **catégorie, matière et couleur**, choisies dans des listes de valeurs, et **dimensions** dans un format fixé (unité, ordre longueur × hauteur × profondeur), pour réduire les retours pour fiche inexacte.

**L'authentification et le cycle de l'article** (0,5 pt) :
- le **résultat de l'authentification** est enregistré **dans le référentiel**, rattaché à l'identifiant : statut (authentique, refusé, second avis), authentificateur, date, observations et photographies de contrôle. Le tableur disparaît ; la mention « authentifié par ORSALIE » n'est affichée que si le statut le permet, et le service clients retrouve la preuve en un clic (M. BELLASTRE). Ce résultat est une donnée **sensible** : il n'est modifiable que par l'atelier, et chaque modification est tracée ;
- le **cycle de l'article** est décrit par des **statuts** successifs : reçu (ou annoncé) ; en attente d'authentification ; authentifié ou refusé (rendu au vendeur) ; en remise en état ; en attente de photographie ; en vente ; réservé (dans un panier, en boutique ou sur une place de marché) ; vendu ; retourné, puis remis en vente sous le même identifiant ou rendu au vendeur. Chaque changement de statut est **daté** : on mesure ainsi le délai de chaque étape (annexe 2.2 D) et la disponibilité réelle ;
- **demain**, sur la place de marché, le cycle s'inverse : annonce publiée par le vendeur, vente, envoi à l'atelier, authentification, livraison à l'acheteur, ou annulation si l'article n'est pas authentique ou non conforme. Le référentiel doit accepter les deux cycles, avec le même identifiant et les mêmes listes de marques et d'états.

*2.1 b) – Un extrait de dictionnaire de données*

Un **dictionnaire de données** décrit chaque donnée de manière partagée : nom, définition, format et domaine de valeurs, règle d'enregistrement ou de calcul, source, propriétaire, sensibilité et règles de qualité (0,5 pt). Il fixe le **sens** des données, et non leur structure : ce n'est pas un modèle conceptuel (F07 § 1 et 8.3). Il met fin, ici, aux trois sens de chaque mot relevés dans les témoignages de l'annexe 2.1 C, qui rendent les chiffres incomparables d'un canal à l'autre.

| Notion | Définition commune | Règle d'enregistrement ou de calcul | Propriétaire | Règle de qualité |
|---|---|---|---|---|
| **État de l'article** (0,5 pt avec la suivante) | appréciation de l'usure et des défauts de l'article, sur une échelle unique (par exemple cinq niveaux, du « neuf » à « état correct »), chaque niveau étant décrit par des critères observables (rayures, coins, fonctionnement) | noté par l'authentificateur à l'issue de l'authentification, puis mis à jour après la remise en état ; le catalogue le reprend sans le modifier ; une table de correspondance traduit l'échelle unique dans celle de chaque place de marché | responsable de l'atelier | aucun article en vente sans état noté ; état affiché identique à l'état enregistré par l'atelier, contrôlé chaque mois sur un échantillon (100 fiches sur 500 en écart en mars 2027) |
| **Article disponible** | article authentifié, en vente, ni réservé ni vendu, qui peut être acheté immédiatement sur tous les canaux | statut « en vente » dans le référentiel ; il passe à « réservé » dès la mise au panier, la vente en boutique ou la commande sur une place de marché, et cette information est transmise à tous les canaux ; un article en attente d'authentification ou de photographie est « en préparation », non disponible | directeur commercial | aucun article vendu deux fois : les ventes annulées faute de stock sont suivies chaque semaine (900 en 2026) ; écart entre le nombre d'articles disponibles du référentiel et celui de chaque canal contrôlé chaque jour |
| **Date de mise en vente** (0,5 pt) | date à laquelle l'article devient disponible pour la première fois, sur le site et l'application | horodatage automatique du passage au statut « en vente » dans le référentiel, et non saisie manuelle ; la date de publication sur chaque place de marché est enregistrée à part, comme une donnée distincte | responsable du catalogue | date toujours postérieure à la date de réception et à la date d'authentification ; écart entre la mise en vente et la publication sur chaque place de marché suivi (de un à dix jours en 2026) |

Les **propriétaires** sont des responsables métiers, et non l'équipe numérique : ils arbitrent la définition et la qualité attendue. Des **intendants** (un rédacteur référent du catalogue, un authentificateur référent) corrigent les anomalies au quotidien (F07 § 8.1). La date de mise en vente fixe aussi le point de départ commun du délai de mise en vente (depuis la réception) et du délai de vente (jusqu'à la vente), utilisés dans l'annexe 2.2.

*2.1 c) – Les échanges avec les places de marché*

L'**interopérabilité** est la capacité de systèmes hétérogènes, appartenant le cas échéant à des organisations différentes, à échanger des données et à les utiliser sans ressaisie. Elle a un plan **technique** (moyen d'échange : interface de programmation, dépôt de fichiers), un plan **syntaxique** (format), un plan **sémantique** (même sens des données : catégories, échelles d'état) et un plan **organisationnel** (qui transmet quoi, quand, sous quelle responsabilité). Une **interface de programmation (API)** permet à un logiciel d'interroger ou de mettre à jour un autre logiciel automatiquement, à chaque événement. Un **format ouvert** est un format dont la spécification est publique et que tout logiciel peut lire (F07 § 7).

**Les solutions d'échange** (0,5 pt, avec la définition) :
- avec les **places de marché A et C** : l'**interface de programmation** qu'elles proposent, et qu'ORSALIE n'utilise pas (annexe 2.1 B). L'annonce est publiée dès la mise en vente, à partir du référentiel, et la **disponibilité est mise à jour à chaque événement** : dès qu'un article est réservé ou vendu sur un canal, il est retiré des autres en quelques secondes. Les commandes reçues des places de marché réservent l'article dans le référentiel de la même façon ;
- avec la **place de marché B**, qui n'accepte que des fichiers : un **fichier en format ouvert** produit automatiquement par le référentiel et déposé **toutes les heures**, au lieu d'une fois par nuit ; comme un délai d'une heure laisse subsister un risque, les articles de forte valeur ou très demandés peuvent n'être proposés sur B qu'après un délai, ou retirés dès leur mise au panier sur un autre canal ;
- les **boutiques** enregistrent la vente dans le logiciel de caisse relié au référentiel, et non plus par messagerie ;
- dans tous les cas, le **référentiel** est la seule source de la disponibilité ; les connecteurs ne font que la transmettre.

**Deux conditions organisationnelles** (0,5 pt), parmi :
- une **table de correspondance** des catégories et des échelles d'état de chaque place de marché, tenue par le catalogue (plan sémantique) : c'est elle qui supprime les compléments saisis à la main ;
- une **convention d'échange** avec chaque place de marché (données transmises, fréquence, délais de prise en compte, interlocuteurs) et un **suivi des échanges** : alerte en cas d'échec d'un envoi, rejets traités le jour même par un intendant désigné, ventes annulées suivies chaque semaine (600 sur les places de marché en 2026, et une suspension de huit jours de la place de marché B) ;
- des **données limitées au nécessaire** : le nom et la commune du vendeur particulier ne sont plus transmis à la place de marché B, qui ne les utilise pas (principe de minimisation du RGPD, annexe 2.5), et les données transmises sont encadrées par les conditions conclues avec chaque place de marché ;
- une **règle de priorité** des canaux, décidée par le directeur commercial (articles réservés au site et aux boutiques, délai avant publication sur B).

**Réponses tolérées**
- Référentiel présenté comme une démarche de gestion des données de référence, si le terme est écrit en toutes lettres et si une seule source de description est retenue.
- Autres attributs normalisés justifiés par l'annexe 2.1 (photographies rattachées à l'identifiant, prix, dimensions), si chacun porte une règle.
- Autres définitions des trois notions, si elles sont uniques pour toute l'entreprise, mesurables, et accompagnées d'une règle et d'un propriétaire ; propriétaire unique (la responsable du catalogue) pour les trois notions, s'il est justifié.
- Fichier structuré en XML ou à séparateurs cité pour la place de marché B ; synchronisation par API proposée aussi pour B à terme, si la place de marché l'ouvre.
- Plans de l'interopérabilité présentés en deux ou trois niveaux (le plan syntaxique rattaché au plan technique).

**Erreurs fréquentes**
- *Modèle des données hors attente* (`JUR-T06`, `ET-23`) — entités, associations et cardinalités dessinées au lieu de règles d'organisation, alors que la question les exclut.
- *Identifiant signifiant ou instable* — numéro de réception, marque ou date retenus comme identifiant : l'article retourné change encore de numéro et perd son historique.
- *Sigle ambigu* (`ET-13`) — « mettre en place un MDM » sans préciser qu'il s'agit de la gestion des données de référence.
- *Interopérabilité seulement technique* (`ET-36`) — interface de programmation proposée partout, sans correspondance des catégories et des états, sans suivi ni responsable.
- *Détail technique hors attente* (`JUR-T07`) — description des formats d'API, des méthodes d'appel ou de l'authentification des échanges.
- *Morceau de cours* (`JUR-T01`) — définitions du référentiel, du dictionnaire ou de l'interopérabilité sans les articles, les trois notions et les trois places de marché.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines données de référence, métadonnées, qualité, intégration et interopérabilité | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | principe de minimisation appliqué aux données des vendeurs transmises (annexe 2.5) | `rgpd` / F15 § 0 | en vigueur |
| Données de référence, identifiant, dictionnaire de données, dimensions de la qualité, propriétaire et intendant, plans de l'interopérabilité, API et formats ouverts | définitions et principes | F07 § 1, 7, 8.1 et 8.3 | notion de cours |

---

### 2.2 – Les délais de vente, les retours et les outils d'analyse (4,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.d` « Outils décisionnels : Excel avancé, Power BI, Tableau, etc. » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Aucun calcul statistique ni aucune manipulation d'outil ; lecture critique des biais, reliée à la stratégie.

**Annexes mobilisées** : annexes 1.1 (canaux, catégories, délai de 21 jours, effectif de l'équipe numérique, dépenses du numérique), 2.1 (définitions divergentes, ventes en double), 2.2 (tableaux par catégorie et par canal, motifs de retour, décomposition du délai, question de la présidente) et 2.3 (rapport mensuel, attentes, deux options).

**Barème indicatif (4,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de traitement appliquée aux sources d'ORSALIE : collecte, nettoyage, structuration autour de l'identifiant et des définitions communes, analyse, restitution ; rôles | 0,5 |
| a-2 | Analyses descriptive et exploratoire définies et distinguées, prédictive écartée ; combinaison justifiée par l'annexe 2.2 (décrire où passent le temps et l'argent, puis explorer les causes) | 0,5 |
| b-1 | Premier constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-2 | Deuxième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-3 | Troisième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| c-1 | Réponse à la présidente, de tête : 11 jours d'attente sur 21, montres ; retours pour fiche inexacte (3 000 × 40 € = 120 k€, sur 360 k€ de retours), 900 ventes en double dont 600 sur les places de marché, montres invendues ; conséquence pour l'objectif de 7 jours | 0,5 |
| c-2 | Deux représentations adaptées, chacune justifiée par son message et assortie d'un piège évité | 0,5 |
| d-1 | Comparaison des deux options selon quatre critères, avec le coût de tête sur trois ans (150 k€ et 60 k€) | 0,5 |
| d-2 | Recommandation argumentée (option 1) et deux conditions de réussite ; informatique décisionnelle présentée comme une démarche et non comme un outil | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de traitement et la méthode d'analyse*

**La chaîne de traitement** (0,5 pt) transforme des données brutes en décisions (F08 § 1) :
- **collecte** : extraction automatique, chaque nuit, des données du référentiel des articles (ou, en attendant, du logiciel des dépôts et du tableur de l'atelier), du site, du logiciel de caisse, des places de marché A, B et C et de l'outil de gestion de la relation client (motifs de retour) ;
- **nettoyage** : rapprochement des numéros de réception d'un même article, correction des dates de réception saisies en retard, classement des motifs de retour saisis en texte libre, repérage des mois manquants (place de marché C avant avril, boutique de Paris en août), des doublons et des valeurs aberrantes, consignés dans un journal des rejets et corrigés à la source ;
- **structuration** : chargement dans une base d'analyse commune, organisée par article, date, catégorie, canal et pays, selon les définitions du dictionnaire (question 2.1 b) : une seule définition de la date de mise en vente, du retour ou du montant des ventes, au lieu des trois montants de mars 2027 (3,8, 4,0 et 4,2 M€) ;
- **analyse**, puis **restitution** dans des tableaux de bord adaptés à chaque destinataire (présidente, commerce, catalogue, atelier), avec des alertes, et **décision** suivie d'actions.

L'analyste de données conçoit et documente la chaîne ; les propriétaires des données valident les définitions et la qualité ; les règles de préparation, aujourd'hui connues d'elle seule, sont écrites.

**La méthode** (0,5 pt) : l'**analyse descriptive** résume ce qui s'est passé (volumes, délais moyens, répartitions, écarts à une cible) ; l'**analyse exploratoire** recherche, sans hypothèse arrêtée à l'avance, des croisements, des profils et des valeurs atypiques qui orientent vers des explications ; l'**analyse prédictive** estime ce qui va se passer (F08 § 2). ORSALIE combinera :
- une **analyse descriptive d'abord**, parce que la question de la présidente est descriptive (où, combien) et que les chiffres doivent d'abord être fiabilisés : délai par étape, retours par motif, ventes annulées par canal ;
- puis une **analyse exploratoire** pour comprendre les causes : croiser les délais des montres avec la charge de l'horloger, les retours pour fiche inexacte avec les écarts d'état relevés par le contrôle de mars 2027, les ventes annulées avec l'heure de la vente et le canal ;
- une analyse **prédictive** (prévoir les ventes d'un article) serait prématurée : l'historique est court, et les définitions changent selon les canaux.

*2.2 b) – Trois constats argumentés et leurs précautions de lecture*

Trois constats parmi les suivants (0,5 pt chacun : le fait chiffré, son interprétation au regard du plan « ORSALIE 2030 », la précaution de lecture) :

1. **Plus de la moitié du délai de mise en vente est de l'attente.** Sur 21 jours, 11 sont passés à attendre : 6 avant l'authentification, 5 avant la photographie (annexe 2.2 D). Le travail lui-même (authentification, photographie, fiche, prix) prend 4 jours. Le délai tient donc d'abord à la capacité et à l'organisation des files d'attente de l'atelier et du catalogue. L'objectif de 7 jours ne sera pas atteint en accélérant seulement le travail. *Précaution* : l'échantillon porte sur 1 000 articles reçus en février 2027, un seul mois, qui n'est pas forcément représentatif (saisonnalité des dépôts). De plus, la date de réception est parfois saisie plusieurs jours après l'arrivée du colis : le délai réel est plutôt sous-estimé.
2. **Les montres sont la catégorie la plus lente à chaque étape.** Il leur faut 35 jours pour être mises en vente (contre 17 pour la maroquinerie) et 60 jours pour être vendues, et 25 % sont encore invendues 90 jours après leur mise en vente. Un seul horloger les authentifie et contrôle leur fonctionnement (Mme VERCHAMP) ; le défaut de fonctionnement est leur premier motif de retour. *Précaution* : un goulet d'étranglement chez l'horloger est une explication plausible, non démontrée ; le prix plus élevé des montres ou leur clientèle peuvent aussi expliquer une vente plus lente (corrélation n'est pas causalité). La part des invendus ne porte que sur les articles mis en vente avant le 1er octobre 2026.
3. **Un tiers des retours vient d'une fiche inexacte.** 3 000 retours sur 9 000 ont pour motif un article différent de la fiche ; c'est le premier motif de la maroquinerie, qui a le taux de retour le plus élevé (13 %). Le contrôle de mars 2027 va dans le même sens : une fiche sur cinq affiche un état plus favorable que celui noté par l'atelier (annexe 2.1 B). La qualité des données coûte donc directement de l'argent et la confiance des clients. *Précaution* : jusqu'en juin 2026, les motifs étaient saisis en texte libre, puis classés à la main par l'analyste ; le total de 9 000 mêle des retours effectifs et les réclamations comptées comme retours par les places de marché.
4. **Les places de marché concentrent les ventes en double.** Elles représentent un sixième des articles vendus (16 000 sur 96 000), mais deux tiers des ventes annulées (600 sur 900), parce que leur disponibilité n'est mise à jour qu'une fois par nuit ; la suspension de huit jours par la place de marché B en est la conséquence. *Précaution* : leur taux de retour (15 %) et leur délai de vente (20 jours) ne sont pas comparables à ceux du site, car ils ne sont pas définis de la même façon (réclamations comptées comme retours, délai compté à partir de la publication de l'annonce), et la place de marché C n'a transmis que neuf mois de données.
5. **Les données des boutiques ne permettent aucune conclusion.** Les échanges ne sont pas enregistrés, et les ventes de la boutique de Paris manquent pour août 2026. *Précaution* : on ne compare pas le délai de vente des boutiques (50 jours) à celui des autres canaux tant que les données sont incomplètes.

*2.2 c) – La réponse à la présidente et deux représentations*

**La réponse à Mme VELDRANE** (0,5 pt), de tête :
- **le temps** se perd dans les **files d'attente** : 11 jours sur 21, avant l'authentification et avant la photographie. Les **montres** cumulent 35 jours avant la mise en vente et 60 jours avant la vente, soit plus de trois mois de la réception à la vente. Pour atteindre 7 jours, il faut supprimer l'essentiel de ces 11 jours d'attente : la capacité de l'atelier, celle de l'horlogerie et celle du catalogue sont les leviers ;
- **l'argent** se perd :
  - dans les **retours** : 9 000 retours à environ 40 € coûtent environ 360 k€ par an ; ceux qui sont dus à une **fiche inexacte** (3 000) coûtent environ 120 k€, sans compter les ventes perdues, et ils sont évitables par la qualité des données ;
  - dans les **ventes en double** : 900 ventes annulées, dont 600 sur les places de marché, avec des pénalités, une mauvaise note et huit jours de suspension de la place de marché B ;
  - dans les **montres invendues** : un quart des montres reste invendu après 90 jours, soit près de 4 000 articles à l'échelle de l'année, dont une partie a été rachetée par ORSALIE et immobilise sa trésorerie.

Réponse : « Nous perdons surtout du temps dans les files d'attente de l'atelier et du catalogue, et sur les montres ; nous perdons de l'argent sur les retours dus à des fiches inexactes, sur les ventes en double des places de marché et sur les montres qui ne se vendent pas. Ces trois pertes viennent en grande partie de la qualité et de la circulation des données. »

**Deux représentations** (0,5 pt), parmi :
- **Barre horizontale empilée des 21 jours par étape**, en distinguant les attentes (en couleur vive) du travail (en gris), avec une ligne repère à 7 jours. *Message* : 11 jours sur 21 sont de l'attente. *Piège évité* : on indique la source et le mois de l'échantillon, pour ne pas présenter février 2027 comme une moyenne annuelle.
- **Barres triées des motifs de retour**, du plus fréquent au moins fréquent, avec en regard le coût estimé à 40 € par retour. *Message* : la fiche inexacte arrive en tête et coûte environ 120 k€. *Piège évité* : on signale que la moitié de l'année a été classée à la main, et que les réclamations des places de marché sont comptées comme des retours.
- **Barres empilées par catégorie** du délai de mise en vente et du délai de vente, sur une même échelle qui part de zéro. *Message* : il faut près de 95 jours pour une montre, contre moins de 50 pour la maroquinerie. *Piège évité* : des moyennes qui cachent la dispersion ; on indique aussi le nombre d'articles de chaque catégorie.
- **Barres par canal** des ventes et des ventes annulées. *Message* : les places de marché font un sixième des ventes et deux tiers des annulations. *Piège évité* : on compare des parts, et non des valeurs absolues de tailles différentes.

Un graphique en secteurs des quatre catégories, ou des taux de retour des canaux comparés sans mention de leur définition, sont de mauvais choix.

*2.2 d) – Les deux options d'outils d'analyse*

**Comparaison** (0,5 pt), selon quatre critères parmi :

| Critère | Option 1 : outil décisionnel en libre-service | Option 2 : tableaux de bord des logiciels existants |
|---|---|---|
| Réponse aux attentes de l'annexe 2.3 B | vue croisée des canaux, des pays et des étapes ; chaque responsable compose ses analyses, la présidente a « les mêmes chiffres pour tout le monde » | chaque logiciel ne voit que ses propres données : ni les ventes par canal et par pays en un seul écran, ni le délai par étape |
| Fiabilité et cohérence | jeux de données certifiés, selon des définitions communes, si le dictionnaire existe | chaque logiciel garde ses définitions : les trois montants des ventes de mars 2027 subsisteront |
| Coût (de tête, sur trois ans) | 90 + 3 × 20 = 150 k€, soit 50 k€ par an, environ 2 % des 2,4 M€ de dépenses du numérique | 30 + 3 × 10 = 60 k€ |
| Délai et dépendance | quatre mois ; peu de charge pour l'équipe numérique | trois mois, mais seulement quand l'équipe numérique, prise par la refonte, sera disponible |
| Pérennité | indépendante des logiciels sources : elle survit à la refonte du site | les écrans du site seront à refaire après la refonte |
| Risques | multiplication d'indicateurs concurrents si personne ne certifie les données ; données « pas plus justes » que les sources | morcellement durable ; l'analyste continue de répondre à la main aux 150 demandes d'extraction |

**Recommandation : l'option 1** (0,5 pt). C'est la seule qui croise les sources et donne à chacun les mêmes chiffres, ce que demandent la présidente et les responsables. Son surcoût, d'environ 90 k€ sur trois ans, est à rapprocher des 48 jours par an que l'analyste consacre au rapport mensuel, des 150 demandes d'extraction traitées à la main et des pertes chiffrées à la question c. L'option 2 coûte moins cher, mais elle prolonge le problème : des définitions différentes selon les logiciels, et des écrans à refaire après la refonte. Deux conditions de réussite, parmi :
- **les données avant l'outil** : référentiel des articles et dictionnaire de données d'abord (question 2.1), car l'outil « ne rendra pas les données plus justes » ; la préparation des données (60 k€) est le poste essentiel de l'option ;
- **des jeux de données et des indicateurs certifiés** par leurs propriétaires et validés par l'instance de gouvernance (question 2.3) ; les analyses personnelles restent possibles, mais seuls les indicateurs certifiés circulent ;
- **un rôle nouveau pour l'analyste** : elle documente la chaîne, certifie les jeux de données et accompagne les utilisateurs, au lieu d'extraire ;
- **la formation et la culture de la donnée** des 25 utilisateurs, et un démarrage par trois tableaux de bord : celui de la présidente (hebdomadaire), celui du catalogue et de l'atelier (articles en attente par étape), celui du commerce (ventes de la veille) ;
- des **droits d'accès** limités : les responsables n'ont pas besoin des données personnelles des vendeurs et des clients pour leurs analyses.

**Réponses tolérées**
- Analyse exploratoire placée en premier, si le candidat montre qu'elle sert d'abord à repérer les incohérences (dates, motifs, mois manquants) avant toute description.
- Autres constats tirés de l'annexe 2.2 (bijoux : 20 % d'invendus et 25 jours de mise en vente ; taux de retour élevé de la maroquinerie), s'ils portent une précaution.
- Coût des retours présenté pour les seuls retours évitables (120 k€) ou pour l'ensemble des retours (360 k€), si le calcul est juste.
- Option 2 retenue à titre transitoire jusqu'à la refonte, si le candidat en montre les limites et prévoit l'option 1 ensuite.
- Un outil décisionnel du marché cité à titre d'exemple, si la démarche (données, gouvernance, compétences) est développée.

**Erreurs fréquentes**
- *Informatique décisionnelle réduite à un outil* (`JUR-D02`, `ET-05`) — recommander l'outil en libre-service sans préparation des données, sans définitions communes ni rôle de l'analyste.
- *Corrélation présentée comme une causalité* (`ET-26`) — « l'horloger est la cause des invendus de montres » sans réserve.
- *Prudence d'interprétation absente* (`JUR-D06`) — comparer le taux de retour ou le délai des places de marché à ceux du site sans relever que leurs définitions diffèrent, ou généraliser l'échantillon de février 2027.
- *Calcul ou manipulation hors attente* (`JUR-T07`) — moyennes pondérées, écarts-types, prévisions, ou description de la manipulation d'un outil décisionnel.
- *Constat sans conséquence* (`JUR-T03`) — chiffres recopiés sans lien avec l'objectif de 7 jours ni avec la question de la présidente.
- *Lecture partielle des annexes* (`JUR-T08`) — ignorer la décomposition du délai (annexe 2.2 D) ou les témoignages qui l'expliquent.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement des données, analyses descriptive, exploratoire et prédictive | définitions et choix de la méthode | F08 § 1 et 2 | notion de cours |
| Choix d'une représentation, biais de lecture, corrélation et causalité | représentations et précautions | F08 § 5 | notion de cours |
| Outils décisionnels, libre-service et gouvernance centrale | comparaison des options | F08 § 6 | notion de cours |

---

### 2.3 – La gouvernance des données (2 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.a` « Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques » ; `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ». Le rôle du *Chief Data Officer* et la structuration de la gouvernance sont illustratifs, non normatifs ; aucune expertise des infrastructures.

**Annexes mobilisées** : annexes 1.1 (organigramme, plan « ORSALIE 2030 »), 2.1 (constats, données des vendeurs, absence de responsable, future place de marché), 2.3 (montants des ventes divergents, analyste seule à connaître les règles) et 2.5 (RGPD, DAMA-DMBOK, ISO/IEC 25012).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Gouvernance des données définie ; trois enjeux appliqués au cas (qualité, conformité, usage des données pour la future place de marché) | 0,5 |
| 2 | Instance de gouvernance : composition, fréquence, décisions, rattachement à la présidente | 0,5 |
| 3 | Propriétaire et intendant de trois domaines de données, rôle de l'équipe numérique | 0,5 |
| 4 | DAMA-DMBOK présenté comme un référentiel de bonnes pratiques et non comme une norme ; domaines prioritaires pour ORSALIE et usage concret | 0,5 |

**Réponse attendue**

La **gouvernance des données** est l'ensemble des rôles, des instances, des règles et des processus qui garantissent que les données sont définies, fiables, conformes, protégées et utilisées au service de la stratégie de l'organisation (F07 § 8). Elle relève des métiers et de la direction, et non de la seule équipe numérique.

**Trois enjeux pour ORSALIE** (0,5 pt) :
- **qualité** : les données des articles sont le produit lui-même, puisque le client achète sur une fiche. Les 2 300 libellés de marque, l'état trop favorable d'une fiche sur cinq, les 3 000 retours pour fiche inexacte et les 900 ventes en double montrent que la qualité se paie en retours, en pénalités et en confiance ;
- **conformité** : les données des vendeurs particuliers sont des données personnelles. Leur transmission inutile à la place de marché B est contraire au principe de minimisation, et ORSALIE doit pouvoir démontrer le respect des principes du RGPD (annexe 2.5). Le résultat de l'authentification est la **preuve** de la promesse faite au client ; il doit être exact, traçable et protégé, ce qui exclut un tableur partagé qui a déjà été écrasé ;
- **usage des données pour la future place de marché** : à partir de 2028, des particuliers publieront eux-mêmes leurs annonces. La liste de référence des marques et des modèles, l'échelle d'état et l'historique des articles vendus et de leurs prix fonderont l'estimation du prix proposée aux vendeurs et la garantie d'authenticité. Sans gouvernance, les erreurs actuelles seraient multipliées par le nombre d'annonces.

**L'instance** (0,5 pt) : un **comité des données**, par exemple :
- **composition** : le (la) secrétaire général(e), qui l'anime et qui supervise l'équipe numérique ; les propriétaires des données (responsable du catalogue, responsable de l'atelier, directeur commercial, responsable du service clients) ; le responsable technique ; l'analyste de données, qui en assure le secrétariat ; le service juridique, ainsi que le délégué à la protection des données si ORSALIE en a désigné un ;
- **fréquence** : mensuelle pendant la première année (mise en place du référentiel et du dictionnaire), puis trimestrielle ;
- **décisions** : valider les définitions du dictionnaire et leurs propriétaires ; fixer les règles de qualité, les cibles et les priorités de correction ; arbitrer les conflits de définition (le montant des ventes de mars 2027) ; décider des données transmises aux places de marché et des droits d'accès ; certifier les indicateurs de l'outil décisionnel ;
- **rattachement** : un compte rendu à la présidente, qui arbitre en dernier ressort et inscrit la qualité des données parmi les conditions du plan « ORSALIE 2030 ». Pour une entreprise de 130 salariés, aucun poste de directeur des données n'est indispensable : la structure est illustrative.

**Les rôles** (0,5 pt) : le **propriétaire** est le responsable métier d'un domaine de données (définitions, règles, qualité attendue, droits d'accès) ; l'**intendant** met en œuvre au quotidien (dictionnaire, contrôles, corrections) (F07 § 8.1).

| Domaine de données | Propriétaire | Intendant |
|---|---|---|
| Description des articles (marque, modèle, attributs, photographies, fiches) | Mme Clémence DUVERNAIS, responsable du catalogue | un rédacteur référent du catalogue |
| Authentification et état des articles | Mme Sabine VERCHAMP, responsable de l'atelier | un authentificateur référent |
| Ventes, disponibilités et retours | M. Damien ROCHAMBEL, directeur commercial, avec M. Karim BELLASTRE pour les retours | Mme Léa CORVENNAT, analyste de données |

L'**équipe numérique** est dépositaire technique des données : elle exploite et protège les logiciels et les échanges, mais elle ne décide pas du sens des données. Les données personnelles des vendeurs relèvent du service juridique pour leur conformité, sans être pour autant gérées par l'équipe numérique.

**Le DAMA-DMBOK** (0,5 pt) : c'est un **référentiel** de bonnes pratiques de gestion des données, et non une norme certifiable ni un logiciel ; il organise la gestion des données en onze domaines autour de la gouvernance (annexe 2.5 ; F07 § 8.2). ORSALIE s'en sert pour :
- **choisir ses priorités** : les données de référence (référentiel des articles), la qualité des données, les métadonnées (dictionnaire), l'intégration et l'interopérabilité (places de marché), puis l'entreposage et l'informatique décisionnelle (outil de la question 2.2 d) ;
- **évaluer sa situation** domaine par domaine, et suivre ses progrès d'une année sur l'autre ;
- **nommer les rôles** et structurer le plan d'action du comité, sans tout mettre en œuvre d'un coup.

La norme ISO/IEC 25012 (annexe 2.5) complète le dispositif : ses caractéristiques (exactitude, complétude, cohérence, actualité) servent à formuler les règles de qualité du dictionnaire.

**Réponses tolérées**
- Instance présidée par la présidente, ou comité intégré au comité de direction, si sa composition associe les métiers et si ses décisions sont précisées.
- Autres domaines de données (prix, photographies, données des vendeurs), si chacun a un propriétaire métier et un intendant.
- Mention d'un responsable des données (*Chief Data Officer*) à terme, présentée comme une option et non comme une obligation.
- Enjeu de sécurité des données (accès au résultat de l'authentification, tableur partagé) traité à la place de la conformité, s'il est appliqué au cas.

**Erreurs fréquentes**
- *Gouvernance confiée à l'équipe numérique* — le responsable technique « propriétaire » de toutes les données ; les métiers absents du comité.
- *Norme, référentiel et solution confondus* (`ET-01`, `JUR-S06`) — DAMA-DMBOK présenté comme une norme à certifier ou comme un logiciel.
- *Organisation imposée* — création d'une direction des données avec plusieurs postes pour une entreprise de 130 salariés, alors que le programme présente cette structuration comme illustrative.
- *Hors du sujet* — développement sur la vente des données ou sur leur valeur comptable, que la question ne demande pas.
- *Morceau de cours* (`JUR-T01`) — rôles définis sans les personnes et les domaines d'ORSALIE.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | onze domaines, priorités d'ORSALIE | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| ISO/IEC 25012 (2008), modèle de qualité des données | caractéristiques de la qualité citées dans les règles | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | minimisation, exactitude, intégrité et confidentialité, responsabilité (annexe 2.5) | `rgpd` / F15 § 0 | en vigueur |
| Proposition « omnibus numérique » du 19/11/2025 | non applicable (annexe 2.5) | `omnibus_numerique_donnees` | projet |
| Gouvernance des données, propriétaire, intendant, rôles illustratifs | définitions | F07 § 8.1 | notion de cours |

---

### 2.4 – Le projet de studio de mise en ligne (2,5 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI » ; `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI ». Les calculs se font de tête, sur des sommes rondes, sans prise en compte du coût du capital ; les méthodes financières qui en tiennent compte relèvent de l'UE 2.

**Annexes mobilisées** : annexes 1.1 (effectif du catalogue, délai de 21 jours, plan « ORSALIE 2030 »), 2.2 (motifs et coût des retours, décomposition du délai) et 2.4 (temps, coûts, gains, essai de mars 2027).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Retour sur investissement et délai de récupération définis ; coût d'une fiche : 8 € aujourd'hui, 5 € avec le studio (4 € de temps, 0,50 € de coûts annuels, 0,50 € d'investissement réparti) | 0,5 |
| a-2 | Gains en trésorerie : 60 k€ de retours évités et 90 k€ de marge, soit 150 k€, nets des coûts annuels 100 k€ ; délai de récupération 2,5 ans ; retour sur investissement sur cinq ans 100 % | 0,5 |
| a-3 | Temps libéré (10 000 h, environ six postes, 400 k€) écarté du calcul : gain de capacité et non de trésorerie, sauf recrutements évités ; conclusion nuancée (hypothèses, délai ramené à 15 jours seulement) | 0,5 |
| b | Trois coûts indirects ou cachés tirés de l'annexe 2.4 | 0,5 |
| c | Un indicateur de suivi complet : formule, source, fréquence, cible justifiée, axe | 0,5 |

**Réponse attendue**

*2.4 a) – Le coût d'une fiche, le délai de récupération et le retour sur investissement*

Le **retour sur investissement** (ROI) rapporte le gain net cumulé d'un projet sur une durée à son coût : (gains cumulés − investissement) / investissement. Le **délai de récupération** est le temps nécessaire pour que les gains nets annuels remboursent l'investissement : investissement / gain net annuel. Ce sont des indicateurs simples, qui ignorent le coût du capital ; ils ne retiennent que les gains mesurables et se complètent d'une appréciation des gains non financiers (F09 § 3.3).

**Le coût d'une fiche** (0,5 pt avec les définitions), en raisonnant en coût complet par article publié (l'article est l'inducteur des coûts du catalogue) :
- **aujourd'hui** : 12 minutes, soit un cinquième d'heure, à 40 € de l'heure : **8 €** par fiche ;
- **avec le studio** :
  - 6 minutes de temps, soit **4 €** ;
  - les coûts annuels, 30 + 20 = 50 k€ pour 100 000 fiches, soit **0,50 €** ;
  - l'investissement, 250 k€ réparti sur cinq ans, soit 50 k€ par an pour 100 000 fiches, ou **0,50 €** ;
  - au total, **5 €** par fiche, soit une baisse de 3 € (près de 40 %).

**Le délai de récupération et le retour sur investissement** (0,5 pt), en ne retenant que les gains qui se traduisent en trésorerie :
- **retours évités** : les 3 000 retours pour fiche inexacte (annexe 2.2 C) divisés par deux, soit 1 500 retours à 40 € de dépenses : **60 k€** par an (le temps interne de traitement des retours, que l'annexe 2.2 C exclut des 40 €, n'est pas compté, comme le temps libéré) ;
- **marge supplémentaire** estimée : **90 k€** par an ;
- **gains en trésorerie** : 60 + 90 = **150 k€** par an ; nets des coûts annuels du studio : 150 − 50 = **100 k€** par an ;
- **délai de récupération** : 250 / 100 = **2,5 ans**, inférieur à la durée d'utilisation prévue de cinq ans ;
- **retour sur investissement sur cinq ans** : (5 × 100 − 250) / 250 = **100 %**. Le studio rapporte, sur sa durée d'utilisation, deux fois ce qu'il a coûté.

**Le traitement du temps libéré** (0,5 pt) : le studio libère 6 minutes sur 100 000 articles, soit **10 000 h** par an, environ six postes à 1 600 heures sur les 20 du catalogue, d'une valeur de **400 k€** au coût horaire. Ce n'est pas un gain de trésorerie : Mme DUVERNAIS ne prévoit aucun départ. Le compter conduirait à un gain net de 500 k€ par an et à un délai de récupération de six mois, ce qui serait trompeur. C'est un **gain de capacité**. Il ne devient un gain financier que s'il évite des recrutements : la croissance des ventes à l'étranger et les annonces de la place de marché en exigeraient, et c'est l'hypothèse qu'il faut écrire et suivre.

**Conclusion** : le studio est rentable sans compter le temps libéré, mais sa rentabilité repose sur deux estimations, la marge supplémentaire et la division par deux des retours. Or cette dernière dépend de la qualité des données saisies par l'atelier, puisque l'outil rédige à partir d'elles : sans le référentiel de la question 2.1, une erreur d'état sera recopiée dans cinq langues. Le studio ramène le délai de mise en vente de 21 à 15 jours seulement ; l'objectif de 7 jours exige aussi de réduire les 6 jours d'attente avant l'authentification (annexe 2.2 D). Recommandation : lancer le studio après la mise en place du référentiel, ou en même temps, en commençant par la maroquinerie, qui fait plus de la moitié des articles mis en vente et dont le premier motif de retour est la fiche inexacte.

*2.4 b) – Trois coûts indirects ou cachés*

Trois coûts parmi les suivants (0,5 pt), tirés de l'annexe 2.4 :
- **la relecture** : à l'essai, une fiche sur dix (20 sur 200) contenait une erreur ; 3 minutes de relecture peuvent ne pas suffire, et une erreur qui passe crée un retour. Il s'agit d'une IA générative, qui produit un texte plausible et non une vérité, à distinguer du détourage, qui relève de la reconnaissance d'images par apprentissage automatique (F13 § 1) ;
- **les reprises de photographies** : une photographie de bijou brillant sur dix est à reprendre à la main, soit du temps de photographe qui n'est pas compté pour les bijoux (20 000 articles par an) ;
- **le stockage et l'affichage** de photographies trois fois plus lourdes : un hébergement en nuage plus coûteux et des pages plus lentes ;
- **l'abonnement au-delà de 120 000 fiches** : si la rédaction assistée est offerte aux vendeurs de la place de marché (environ 300 000 annonces en 2030), il faudrait payer au moins 180 000 fiches au-delà du forfait, soit au moins 54 k€ de plus par an, et environ 84 k€ si les 100 000 fiches d'ORSALIE relèvent du même abonnement ((300 000 + 100 000 − 120 000) × 0,30 €) ;
- **le raccordement** au site, à refaire après la refonte, par une équipe numérique déjà mobilisée ; et la dépendance à l'éditeur de l'outil de rédaction (prix révisables, récupération des fiches en fin de contrat) ;
- **la conduite du changement** des sept photographes, dont le métier change (formation, reconversion, risque de départ), au-delà des 40 k€ prévus, et la perte de productivité des premiers mois.

*2.4 c) – Un indicateur de suivi du projet*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Coût complet d'une fiche publiée** | (heures de catalogue consacrées aux fiches × coût horaire + coûts annuels du studio + investissement réparti sur cinq ans) / nombre de fiches publiées | référentiel des articles (horodatage des étapes et fiches publiées) et contrôle de gestion (coûts) | mensuelle | au plus 5 € fin 2028 (8 € en 2026) | financier |

L'indicateur relie le projet à son objectif économique ; il est utilement complété par un indicateur de qualité (taux de retour pour fiche inexacte) et par le délai de mise en vente (réponses tolérées), pour équilibrer coût, qualité et délai.

**Réponses tolérées**
- Coût d'une fiche avec le studio limité au temps (4 €), si le candidat ajoute ensuite les coûts annuels et l'investissement de façon explicite.
- Retour sur investissement exprimé en gain net cumulé sur cinq ans (5 × 100 − 250 = 250 k€), si le ratio est aussi donné ou si la confusion entre montant et ratio n'est pas faite.
- Surcoût de l'abonnement chiffré à 54 k€ (annonces des vendeurs seules) ou à 84 k€ (annonces et fiches d'ORSALIE), si l'hypothèse est écrite.
- Temps libéré valorisé partiellement, si l'hypothèse de recrutements évités est écrite et chiffrée de façon cohérente (par exemple deux ou trois postes évités).
- Autres indicateurs complets, par exemple : délai moyen entre la réception et la mise en vente (somme des jours entre réception et mise en vente / articles mis en vente ; référentiel des articles ; mensuelle ; 15 jours fin 2028 puis 7 jours en 2030, 21 jours en 2026 ; axe processus) ; taux de retour pour fiche inexacte (retours pour fiche inexacte / ventes en ligne ; outil de gestion de la relation client ; mensuelle ; au plus 2 % fin 2028, près de 4 % en 2026 ; axe client) ; part des fiches corrigées à la relecture (fiches corrigées / fiches rédigées par l'outil ; référentiel des articles ; mensuelle ; au plus 5 % fin 2028, 10 % à l'essai ; axe processus).

**Erreurs fréquentes**
- *Temps libéré compté comme une économie de trésorerie* — délai de récupération de six mois annoncé sans hypothèse de redéploiement ni de recrutements évités (F09 § 3.3).
- *Retour sur investissement et coût total confondus* (`ET-33`) — ROI présenté comme un montant, ou coûts annuels oubliés dans le calcul.
- *Calcul financier hors attente* (`JUR-T07`) — calculs qui tiennent compte du coût du capital, alors que l'énoncé demande un calcul de tête simple.
- *IA générative et apprentissage automatique confondus* (`ET-09`) — la rédaction assistée présentée comme un modèle qui « apprend » l'état des articles, ou comme infaillible.
- *Indicateur incomplet ou générique* (`ET-18`, `JUR-A02`) — « suivre la rentabilité » sans formule, source, fréquence, cible ni axe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Retour sur investissement et délai de récupération, coûts cachés, gain de productivité et trésorerie | définitions et calcul de tête | F09 § 2 et 3.3 | notion de cours |
| Coût complet et inducteur de coûts appliqués au système d'information | coût d'une fiche par article publié | F09 § 2 | notion de cours |
| IA générative et apprentissage automatique | limites de la rédaction assistée | F13 § 1 | notion de cours |
| Indicateur à cinq champs, axes du tableau de bord prospectif | indicateur de suivi du projet | F08 § 3 ; F09 § 4.1 | notion de cours |
