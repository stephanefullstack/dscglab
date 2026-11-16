# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 26 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F11 blockchain et crypto-actifs, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle de données exécuté, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Modèle conceptuel des données des parcelles et des apports | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) | 2 |
| 2.2 Cohérence, interopérabilité et qualité des données | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données | 3 |
| 2.3 Rôles et responsabilités sur les données | `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) | 1 |
| 2.4 Chaîne de valeur des données et analyse des apports de la vendange 2026 | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model | 4,5 |
| 2.5 Le projet d'authentification des cuvées exportées | `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.a` Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ; `3.3.d` Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO | 2,5 |
| **Dossier 2 – Organiser et exploiter les données des parcelles et des apports ; authentifier les bouteilles** |  | **13** |

Répartition indicative : connaissances (formalisme du MCD, interopérabilité, dictionnaire de données, DAMA-DMBOK, chaîne de valeur des données, méthodes d'analyse, blockchain, champ de MiCA) environ 3 points (la moitié des items 2.1 a-1 à a-4, et la moitié des items 2.2 a-1, 2.2 b-1, 2.3-1, 2.4 a-1, 2.4 c-1, 2.5 a et 2.5 c) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Modèle conceptuel des données des parcelles et des apports (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) ». Seul le modèle conceptuel est demandé.

**Annexes mobilisées** : annexe 2.1 (règles de gestion RG1 à RG8 ; constats 3 et 4 de la partie B pour la justification de l'adhésion et du rattachement de l'apport à la parcelle).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Six entités avec identifiant souligné et attributs élémentaires correctement placés (Adhérent, Cave, Parcelle, Cépage, Apport, Prélèvement), sans clé étrangère ni attribut répété | 0,5 |
| a-2 | Association n:m *adhérer* entre Adhérent et Cave, porteuse de la date d'adhésion (1,n / 1,n, RG3) ; association *exploiter* (Adhérent 1,n / Parcelle 1,1, RG4) | 0,5 |
| a-3 | Association *planter* (Parcelle 1,1 / Cépage 0,n, RG5) et associations de l'apport *livrer*, *recevoir*, *provenir* (Apport 1,1 / 0,n, RG6) | 0,5 |
| a-4 | Association *donner lieu* (Prélèvement 1,1 / Apport 1,n, RG7) et justification de chaque cardinalité par une règle de gestion ; la justification du lien direct *livrer* et la contrainte sur la cave d'adhésion sont valorisées, non exigées | 0,5 |

**Réponse attendue**

Le modèle conceptuel des données (MCD) représente les objets de gestion (entités), leurs propriétés (attributs) et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique (F07 § 1).

Entités (identifiant en premier, souligné sur la copie) (0,5 pt) :
- ADHÉRENT (<u>num_adherent</u>, nom, prenom, commune, telephone, courriel) – RG1 ;
- CAVE (<u>code_cave</u>, nom_cave, departement) – RG2 ;
- PARCELLE (<u>num_parcelle</u>, commune_parcelle, lieu_dit, surface_ha, annee_plantation) – RG4 ;
- CÉPAGE (<u>code_cepage</u>, libelle_cepage, couleur) – RG5 ;
- APPORT (<u>num_apport</u>, date_apport, heure_pesee, poids_kg, degre_potentiel, etat_sanitaire) – RG6 ;
- PRÉLÈVEMENT (<u>num_prelevement</u>, date_analyse, acidite_totale, ph) – RG7.

Associations et cardinalités :

```
ADHÉRENT    (1,n) ──── adhérer [date_adhesion] ──── (1,n) CAVE
ADHÉRENT    (1,n) ──── exploiter ────────────────── (1,1) PARCELLE
PARCELLE    (1,1) ──── planter ──────────────────── (0,n) CÉPAGE
APPORT      (1,1) ──── livrer ───────────────────── (0,n) ADHÉRENT
APPORT      (1,1) ──── recevoir ─────────────────── (0,n) CAVE
APPORT      (1,1) ──── provenir ─────────────────── (0,n) PARCELLE
PRÉLÈVEMENT (1,1) ──── donner_lieu ──────────────── (1,n) APPORT
```

Sur la copie, chaque entité n'est dessinée qu'une fois : APPORT au centre, relié à ADHÉRENT, CAVE, PARCELLE et PRÉLÈVEMENT ; ADHÉRENT relié aussi à CAVE et à PARCELLE ; PARCELLE reliée à CÉPAGE.

- *adhérer*, association n:m porteuse de la date d'adhésion : un adhérent adhère à une ou plusieurs caves (environ 40 viticulteurs livrent deux caves, constat 3) ; chaque cave compte au moins un adhérent (1,n de part et d'autre) ; la date d'adhésion ne dépend ni de l'adhérent seul ni de la cave seule, mais du couple – RG3 ;
- *exploiter* : une parcelle est exploitée par un et un seul adhérent (1,1) ; un adhérent exploite au moins une parcelle (1,n) – RG4 (0,5 pt pour ces deux associations) ;
- *planter* : une parcelle est plantée d'un seul cépage (1,1) ; un cépage peut n'être planté sur aucune parcelle, s'il est retenu pour les replantations (0,n) – RG5 ;
- *livrer*, *recevoir*, *provenir* : un apport est livré par un seul adhérent, à une seule cave, et porte sur une seule parcelle (1,1) ; un adhérent, une cave ou une parcelle peut n'avoir aucun apport (0,n) – RG6 (0,5 pt pour ces quatre associations) ;
- *donner_lieu* : un prélèvement concerne un seul apport (1,1) ; un apport donne lieu à au moins un prélèvement (1,n) – RG7.

Justification du lien direct *livrer* (valorisée, non exigée : RG6 impose déjà ce lien) : on pourrait retrouver l'adhérent par la parcelle, mais RG4 n'enregistre que l'exploitant **actuel** ; si une parcelle change d'exploitant, les apports passés doivent rester attribués à celui qui les a livrés. Le lien direct permet en outre un contrôle de cohérence (l'adhérent qui livre est l'exploitant de la parcelle déclarée), utile au constat 4. De même, la cave qui reçoit l'apport ne se déduit pas de l'adhérent, qui peut adhérer à deux caves : *recevoir* est indispensable.

RG8 ne crée ni entité ni association. Une contrainte non représentable par les cardinalités peut être signalée : l'apport ne peut être reçu que par une cave à laquelle l'adhérent qui livre adhère. Le modèle logique, non demandé, comporterait sept tables, dont une table Adhesion à clé composée (#num_adherent, #code_cave) portant la date d'adhésion.

**Réponses tolérées**
- Noms d'entités, d'associations ou d'attributs différents s'ils restent explicites (« Viticulteur », « Livraison », « Analyse ») ; notation « pattes de corbeau » ou UML lisible (format libre, `JUR-T10`).
- Omission de l'association *livrer* si le candidat la justifie explicitement (l'adhérent se déduit de la parcelle) et signale la limite liée au changement d'exploitant.
- Adhésion modélisée comme une entité ADHÉSION à identifiant propre reliée par deux associations 1,1 à Adhérent et à Cave, si le candidat signale l'unicité du couple adhérent × cave.
- Entité supplémentaire justifiée (COMMUNE, STATION) si elle ne contredit pas RG8 ; pas de pénalité pour une commune modélisée en entité, pas de bonification non plus.

**Erreurs fréquentes**
- *MCD et MLD confondus* (`ET-23`, `JUR-T06`) — clés étrangères (num_adherent dans PARCELLE, num_apport dans PRÉLÈVEMENT) dessinées dans le MCD ; juste : le MCD ne comporte ni clé étrangère ni table.
- *Attribut d'association mal placé* — date d'adhésion portée par l'adhérent ou par la cave, ce qui interdit de décrire l'adhérent qui livre deux caves ; juste : elle dépend du couple.
- *Adhérent rattaché à une seule cave* (1,1) — le modèle reproduit les doublons du constat 3 ; juste : association n:m.
- *Cardinalités non justifiées* (`JUR-T01`) — liste d'entités sans renvoi aux règles ; juste : chaque cardinalité est rattachée à une règle de gestion.
- *Hors sujet technique* — modèle logique détaillé, requêtes ou scripts de création de tables, que la question exclut.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Formalisme Merise (MCD, cardinalités, association porteuse) | entités, associations, cardinalités | F07 § 1 à 3 | manuels |

---

### 2.2 – Cohérence, interopérabilité et qualité des données (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ».

**Annexes mobilisées** : annexes 1.1 (neuf logiciels de cave de quatre éditeurs, aucun informaticien dans les caves, équipe informatique de 6 personnes), 2.1 (sources, constats 1 à 7, règles de gestion) et 2.2 (notes du tableau : conversions, échelles sanitaires).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Interopérabilité définie ; référentiel commun des données de référence (adhérents, caves, parcelles, cépages) tenu par l'union et alimentant les neuf logiciels de cave et le laboratoire | 0,5 |
| a-2 | Identifiants uniques attribués par l'union, non signifiants et stables, avec table de correspondance des anciens numéros ; reprise (fusion des doublons, mise à jour des surfaces) | 0,5 |
| a-3 | Circulation des données sur les trois plans : technique (échanges automatisés, formats ouverts, lecture du numéro de bon), sémantique (nomenclature des cépages, unités, échelle sanitaire), organisationnel (qui crée, qui valide, calendrier, engagement des éditeurs) | 0,5 |
| b-1 | Dictionnaire de données défini et quatre rubriques choisies et justifiées | 0,5 |
| b-2 | Entrées du degré potentiel et de l'état sanitaire cohérentes avec les constats (unité unique, échelle commune définie note par note, source, propriétaire) | 0,5 |
| c | Trois règles de qualité, chacune rattachée à une dimension (unicité, complétude, cohérence, exactitude, actualité, validité) et à un constat de l'annexe 2.1 B | 0,5 |

**Réponse attendue**

*2.2 a) – Référentiel commun, identifiants uniques et circulation des données*

L'**interopérabilité** est la capacité de systèmes hétérogènes à échanger des données et à les utiliser sans intervention manuelle ; elle est à la fois **technique** (échanges, formats), **sémantique** (même sens des données) et **organisationnelle** (processus, responsabilités) (F07 § 7 ; le niveau syntaxique, celui des formats, est ici rattaché au plan technique). À ROCALDÈNE, neuf logiciels de quatre éditeurs, des tableurs et un laboratoire décrivent les mêmes objets sans langage commun : neuf extractions envoyées chaque lundi et des tableaux établis à la main.

**Référentiel commun** (0,5 pt avec la définition) : l'union tient un référentiel des **données de référence** (gestion des données de référence) : adhérents, caves, parcelles et cépages, selon le modèle de la question 2.1. Il est la **seule source** de ces données : les logiciels de cave, le laboratoire et les outils d'analyse s'y alimentent au lieu de tenir chacun leur fichier. Les caves restent maîtresses de la réception de la vendange dans leur logiciel ; elles cessent de créer chacune leurs parcelles et leurs adhérents.

**Identifiants uniques** (0,5 pt) : numéro d'adhérent et numéro de parcelle attribués par l'union (RG1, RG4), **non signifiants** (ni la cave, ni la commune, qui peuvent changer), **stables** et jamais réattribués ; code de cépage commun (RG5) ; numéro de bon unique pour l'union (préfixé par le code de la cave, par exemple « SBZ-2026-01877 » : ce préfixe est acceptable pour un bon, car la cave qui reçoit un apport ne change jamais, mais non pour une parcelle ou un adhérent). Une **table de correspondance** conserve les anciens numéros de chaque cave pendant la transition (« P-0123 » de sept caves devient sept numéros distincts). La **reprise** fusionne les 40 adhérents en double (une fiche, deux adhésions), rapproche les 11 000 parcelles et corrige l'écart de 150 hectares (6 650 contre 6 500) avec les caves avant la vendange 2027.

**Circulation des données sur les trois plans** (0,5 pt) :
- *technique* : les logiciels de cave reçoivent du référentiel les listes d'adhérents, de parcelles et de cépages et renvoient chaque jour de vendange les apports à l'union par des échanges automatisés (interfaces de programmation ou fichiers dans un format ouvert décrit par le dictionnaire), au lieu des neuf extractions du lundi ; le laboratoire lit le numéro du bon (code imprimé sur l'échantillon) au lieu de le ressaisir ; les relevés des stations sont récupérés dans le même format ;
- *sémantique* : nomenclature unique des 12 cépages (fin des 31 codes), degré potentiel toujours en % vol., échelle sanitaire commune définie note par note, définitions du dictionnaire (b) partagées par les neuf caves et le laboratoire ;
- *organisationnel* : règles de création et de validation (la cave déclare une parcelle nouvelle, l'union la valide et lui attribue son numéro), calendrier (mise à jour des parcelles chaque hiver, hors vendanges), engagement des quatre éditeurs à lire et à transmettre les données au format commun, formation des agents de réception et des saisonniers, appui de l'équipe informatique aux caves, qui n'ont pas d'informaticien.

*2.2 b) – Dictionnaire de données*

Le **dictionnaire de données** est le référentiel qui décrit chaque donnée de façon unique et partagée : nom, définition, unité ou format, valeurs admises, règle de mesure ou de calcul, source, propriétaire, fréquence de mise à jour ; il fixe le sens commun des données, ce qui le distingue du MCD, qui décrit les relations entre les données (F07 § 1). Pour l'union, il met fin aux mesures hétérogènes du constat 6 : sans lui, deux caves qui écrivent « 3 » ne disent pas la même chose.

Quatre rubriques suffisent (0,5 pt avec la définition) ; le tableau en propose six, parmi lesquelles le candidat en retient quatre : **définition** (sens partagé), **unité et valeurs admises** (contrôle à la saisie, comparabilité), **règle de mesure** (qui mesure, quand, comment), **source de référence**, **propriétaire**, **fréquence de mise à jour**.

| Rubrique | Degré potentiel de l'apport | État sanitaire de l'apport |
|---|---|---|
| Définition | teneur en alcool que donnerait la vendange de l'apport si tous ses sucres étaient transformés, mesurée à la réception | proportion de raisins atteints par des maladies ou des altérations dans l'apport, appréciée à la réception |
| Unité et valeurs admises | % vol., une décimale ; valeurs plausibles de 8,0 à 16,0, toute valeur hors de cette plage étant bloquée et vérifiée ; jamais en grammes de sucres par litre (la conversion de LAURADEL et de CABRISSAC disparaît) | échelle commune de 1 (sain) à 4 (très dégradé), chaque note étant définie par une part de raisins atteints et illustrée par des photographies de référence ; « dégradé » = notes 3 et 4 dans les neuf caves |
| Règle de mesure | mesure à la pesée sur l'échantillon de l'apport, avec un appareil étalonné selon une procédure commune | note attribuée par un agent de réception formé, et non laissée aux seuls saisonniers ; note contrôlée sur un échantillon d'apports par le laboratoire |
| Source de référence | logiciel de cave, transmis au référentiel le jour même | logiciel de cave, transmis au référentiel le jour même |
| Propriétaire | directrice de la production et de la qualité de l'union | directrice de la production et de la qualité de l'union |
| Fréquence de mise à jour | à chaque apport ; définition revue chaque hiver | à chaque apport ; échelle revue chaque hiver avec les directeurs de cave |

(0,5 pt pour les deux entrées.) Sont valorisées : l'unité imposée et la fin des conversions ; l'échelle commune définie note par note, qui répond directement aux critiques de Mme TARASCOUL ; la formation des agents.

*2.2 c) – Trois règles de qualité* (0,5 pt)

| Règle | Dimension | Constat de l'annexe 2.1 B |
|---|---|---|
| Un viticulteur, un seul numéro d'adhérent : recherche obligatoire dans le référentiel avant toute création ; les 40 doublons sont fusionnés | unicité | 3 (adhérents en double) |
| Aucun apport sans parcelle du référentiel : la pesée exige un numéro de parcelle existant, choisi dans la liste des parcelles de l'adhérent qui livre, et non une déclaration orale | complétude et cohérence | 4 (plus d'un tiers des volumes sans parcelle) |
| Cépage choisi dans la nomenclature commune ; degré en % vol. et état sanitaire sur l'échelle commune, valeurs hors plage bloquées | validité (conformité) | 2 et 6 (31 codes pour 12 cépages, mesures non homogènes) |
| Surfaces revues chaque hiver avec les adhérents ; arrachages et cessions enregistrés dans le mois | exactitude et actualité | 5 (6 650 ha dans les fichiers pour 6 500 ha en production) |
| Tout prélèvement rattaché à un apport existant, par lecture du numéro du bon et non par ressaisie | cohérence (intégrité des liens) | 7 (1 100 prélèvements orphelins, 5 %) |
| Identifiant de parcelle unique pour l'union | unicité | 1 (même numéro dans sept caves) |

Trois règles sont attendues, chacune avec sa dimension et son constat.

**Réponses tolérées**
- Plateforme d'échange ou bus d'intégration cité, si le principe (référentiel unique, fin des fichiers du lundi) reste au premier plan ; référentiel placé dans le futur progiciel commun, si son rôle de source unique est préservé.
- Échelle sanitaire commune de 1 à 3 ou de 1 à 5, si elle est définie note par note et appliquée dans les neuf caves.
- Rubriques différentes du dictionnaire (type, exemple, sensibilité, durée de conservation) si elles sont justifiées.
- Dimensions de la qualité nommées autrement (intégrité, conformité, fraîcheur) ou citées d'après ISO/IEC 25012 ; un indicateur de suivi proposé en plus n'est pas exigé.

**Erreurs fréquentes**
- *Interopérabilité seulement technique* (`ET-36`) — interfaces proposées sans nomenclature commune ni règles de création ; juste : technique, sémantique et organisationnelle ensemble.
- *Sigle employé seul* (`ET-13`) — « mettre en place un MDM » sans dire qu'il s'agit de la gestion des données de référence ; juste : écrire en toutes lettres.
- *Identifiant signifiant* — numéro de parcelle construit avec le code de la cave ou de la commune : il change quand la parcelle change d'exploitant ou de cave ; juste : identifiant non signifiant et stable.
- *Dictionnaire confondu avec le MCD* — liste des entités au lieu de la description de chaque donnée ; juste : le dictionnaire décrit le sens, l'unité, la mesure et la source.
- *Qualité laissée à l'informatique* (`JUR-T03`) — « l'équipe informatique corrigera les fichiers » ; juste : la règle est fixée par le métier et appliquée à la saisie dans les caves.
- *Détail technique hors attente* (`JUR-T12`) — description de formats ou de serveurs ; la question l'exclut.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 25012 (2008) — Modèle de qualité des données | dimensions de la qualité, à titre d'exemple | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| Interopérabilité (niveaux technique, sémantique, organisationnel) ; données de référence ; dictionnaire | définitions, principes | F07 § 1, 6.2 et 7 | notion de cours |

---

### 2.3 – Rôles et responsabilités sur les données (1 point)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ».

**Annexes mobilisées** : annexes 1.1 (organigramme, directeurs de cave, aucun informaticien dans les caves), 2.1 (sources, agents de réception, laboratoire, techniciens) et 2.4 (DAMA-DMBOK, RGPD).

**Barème indicatif (1 pt)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | DAMA-DMBOK présenté comme un référentiel de bonnes pratiques (et non une norme ni un logiciel), qui place la gouvernance au centre et décrit les rôles de propriétaire et d'intendant | 0,5 |
| 2 | Trois rôles avec missions et titulaires, répartis entre l'union et les caves (propriétaire à l'union, intendants dans les caves et au laboratoire, troisième rôle : instance commune, dépositaire technique ou délégué à la protection des données) | 0,5 |

**Réponse attendue**

Le **DAMA-DMBOK** (2e édition, 2017, révision 2024) est un **référentiel** de bonnes pratiques de gestion des données, organisé en onze domaines de connaissance autour de la gouvernance des données ; il distingue notamment le **propriétaire** des données, responsable métier qui en fixe les définitions, les règles et la qualité attendue, et l'**intendant**, qui les applique au quotidien. Ce n'est ni une norme ni un logiciel, et ses rôles sont illustratifs, non normatifs (annexe 2.4 ; F07 § 8.1-8.2) (0,5 pt). Pour l'union, les domaines prioritaires sont les données de référence, la qualité et les métadonnées (dictionnaire).

Répartition proposée entre l'union et les caves (0,5 pt pour trois rôles avec missions et titulaires) :

| Rôle | Missions | Titulaire |
|---|---|---|
| **Propriétaire** des données des parcelles et des apports | fixe les définitions et les règles (dictionnaire, échelle sanitaire), arbitre les désaccords entre caves, valide les données qui serviront au conseil | Mme Claire BOUSQUIÉRAN, directrice de la production et de la qualité de l'union |
| **Intendants** des données | appliquent les règles à la saisie, contrôlent les apports sans parcelle et les valeurs hors plage, mettent à jour les parcelles chaque hiver, signalent les anomalies | dans chaque cave, un agent de réception ou l'adjoint du directeur, désigné par le directeur de cave ; au laboratoire, un technicien pour le rattachement des prélèvements |
| **Comité des données** des parcelles et des apports | réunit la propriétaire, les neuf directeurs de cave et le responsable du système d'information ; adopte le dictionnaire et l'échelle sanitaire, suit la qualité chaque trimestre, prépare ce qui sera présenté au conseil | instance présidée par la directrice de la production et de la qualité, avant chaque vendange et chaque trimestre |
| **Dépositaire technique** | met en œuvre le référentiel, les échanges, les droits d'accès et la sécurité, sans décider du contenu | M. Sébastien CAUSSINEL, responsable du système d'information |
| **Délégué à la protection des données** | conseille sur les données des adhérents exploitants en nom propre, qui sont des données personnelles (annexe 2.4) : finalités, minimisation, durée de conservation, mise à jour du registre des traitements | délégué de l'union s'il en a été désigné un (désignation facultative ici, mais recommandée), mutualisable avec les caves |

Sont valorisés : la responsabilité métier à l'union, la saisie et le contrôle là où naît la donnée (les caves), et la place des directeurs de cave dans les décisions, qui conditionne l'acceptation des données par les présidents (annexe 2.2 D).

**Réponses tolérées**
- Propriété des données d'apport confiée à chaque directeur de cave pour ses apports, l'union restant propriétaire des données de référence et des définitions communes, si la répartition est justifiée.
- Administrateur des données (CDO) proposé à titre illustratif, sans être présenté comme obligatoire.
- Le candidat peut s'attribuer la coordination du dispositif, comme responsable du projet de refonte.

**Erreurs fréquentes**
- *Norme / référentiel / solution* (`ET-01`, `JUR-S06`) — « installer DAMA-DMBOK » ou « certifier l'union DAMA » ; juste : référentiel de bonnes pratiques.
- *Qualité confiée à l'informatique* — le responsable du système d'information désigné propriétaire des données ; juste : il est dépositaire technique, la propriété est métier.
- *Rôles sans titulaire ni application au cas* (`JUR-T01`) — liste de rôles récitée ; juste : qui, dans l'union ou dans les caves, fait quoi.
- *Organisation normative* — présenter un organigramme de gouvernance comme imposé par le référentiel ; le programme la veut illustrative.
- *Délégué confondu avec un responsable informatique* (`ET-29`) — le délégué ne tient pas les outils et ne décide pas des moyens.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines de connaissance, rôles de propriétaire et d'intendant (repères de l'annexe 2.4) | `dama_dmbok2` / F07 § 8.1-8.2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | données personnelles des adhérents exploitants en nom propre, registre, délégué (repères de l'annexe 2.4) | `rgpd` / F15 | en vigueur |

---

### 2.4 – Chaîne de valeur des données et analyse des apports de la vendange 2026 (4,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ».

**Annexes mobilisées** : annexes 1.1 (plan « ROCALDÈNE 2030 », neuf caves), 2.1 (sources, constats, établissement manuel des tableaux) et 2.2 (tableau par cave, pluies, projet du conseil, positions de M. SOULAGNET et de Mme TARASCOUL, prévision proposée par le prestataire).

**Barème indicatif (4,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de valeur des données définie et appliquée au cas, de la parcelle au conseil : collecte, préparation et rapprochement, stockage et structuration, analyse, restitution, décision | 0,5 |
| a-2 | Apport de la chaîne à la décision de mieux rémunérer la qualité : critères objectivés, comparables entre caves, traçables jusqu'à la parcelle et acceptés par les caves | 0,5 |
| b-1 | Premier constat argumenté, avec sa précaution de lecture | 0,5 |
| b-2 | Deuxième constat argumenté, avec sa précaution de lecture | 0,5 |
| b-3 | Troisième constat argumenté, avec sa précaution de lecture | 0,5 |
| b-4 | Appréciation des deux positions (biais de confirmation de M. SOULAGNET ; critiques fondées mais hypothèse météorologique invérifiable de Mme TARASCOUL) et conséquence pour le conseil | 0,5 |
| c-1 | Méthode recommandée et justifiée : analyse exploratoire, après une analyse descriptive fiabilisée | 0,5 |
| c-2 | Prévision par parcelle prématurée : deux arguments tirés des annexes | 0,5 |
| d | Deux représentations visuelles, l'une pour le conseil, l'autre pour les directeurs de cave, chacune avec son message et le piège de lecture à éviter | 0,5 |

**Réponse attendue**

*2.4 a) – La chaîne de valeur des données, de la parcelle au conseil*

La **chaîne de valeur des données** décrit les étapes par lesquelles une donnée brute devient une information utile à la décision : collecte, préparation (nettoyage, rapprochement), stockage et structuration, analyse, restitution, puis décision et action ; la valeur se crée à chaque étape et se perd au maillon le plus faible (F08 § 1). Appliquée au cas (0,5 pt) :
1. **Collecte** : à la parcelle (fichier des parcelles, sondes, stations, observations des techniciens), à la réception (bon d'apport : poids, degré, état sanitaire, parcelle), au laboratoire (acidité, pH) et aux assemblages (part retenue pour les cuvées haut de gamme) ;
2. **Préparation** : rapprochement par les identifiants uniques du référentiel (question 2.2), conversion supprimée par l'unité commune, fusion des doublons, rattachement des prélèvements orphelins, traitement des apports sans parcelle ;
3. **Stockage et structuration** : base d'analyse de l'union organisée selon le modèle de la question 2.1, historisée vendange après vendange ;
4. **Analyse** : comparaisons par cave, par cépage, par secteur et par parcelle, croisements entre état sanitaire, pluie, rendement et destination des vins ;
5. **Restitution** : représentations commentées pour le conseil et pour chaque cave (d), avec leurs précautions ;
6. **Décision** : choix par le conseil des critères de qualité communs et de leur calendrier.

**Apport à la décision** (0,5 pt) : aujourd'hui, la chaîne est rompue dès la collecte (mesures non homogènes, un tiers des volumes sans parcelle) et la préparation est manuelle (neuf extractions, tableaux établis à la main) ; toute rémunération de la qualité serait contestée, comme le montre Mme TARASCOUL. Une chaîne maîtrisée permet au conseil de fonder les critères de qualité sur des données **définies en commun, comparables entre les neuf caves, traçables jusqu'à la parcelle et acceptées** par les caves qui les produisent ; elle permet d'apprécier à l'avance l'effet de chaque critère sur chaque cave et de suivre ensuite ses effets, au service de la deuxième priorité du plan « ROCALDÈNE 2030 ». Les modalités de calcul ne relèvent pas de la question.

*2.4 b) – Trois constats argumentés et leurs précautions* (0,5 pt par constat avec sa précaution ; trois constats parmi les quatre suivants)

1. **L'état sanitaire paraît nettement plus dégradé dans l'Aude** : 15 % à 25 % des apports dans trois caves de l'Aude (PECHAUROUX 25 %, CABRISSAC 20 %, LAURADEL 15 %), 10 % à VALCROZIÈRES, contre 3 % à 6 % dans les cinq caves de l'Hérault ; les deux stations de l'Aude ont relevé 70 et 110 mm de pluie du 10 au 25 septembre, contre 20 et 30 mm dans l'Hérault. *Hypothèse* : les pluies de septembre ont favorisé les maladies. *Précaution* : les échelles diffèrent (« dégradé » couvre les notes 3 à 5 sur cinq dans l'Aude, la seule note 3 sur trois dans l'Hérault), les notes sont souvent posées par des saisonniers sans définition écrite, et les deux caves les plus touchées (PECHAUROUX, CABRISSAC) n'ont pas de station : l'écart est en partie un **effet de mesure**, et la pluie une hypothèse non vérifiée pour elles.
2. **Les caves aux rendements les plus faibles fournissent le plus de vins haut de gamme** : SAINT-BRÉZIAN (45 hl/ha, 14,0 % vol., 30 % en haut de gamme), TERRAGOUSSE et VALCROZIÈRES (50 hl/ha, 20 %), contre CAUSSELAC (70 hl/ha, 5 %). *Hypothèse* : des rendements plus faibles donnent des raisins plus concentrés, mieux valorisés. *Précaution* : c'est une **corrélation**, non une causalité ; un **facteur commun** (situation des vignes, âge des vignes, cépages) peut expliquer à la fois le faible rendement et la qualité ; surtout, la part haut de gamme est **décidée par l'union** selon la qualité des cuves et ses besoins commerciaux (environ 44 milliers d'hl, soit environ 12 % de la vendange) : elle mesure aussi les choix de l'union, comme le dit Mme TARASCOUL ; enfin, les fichiers des parcelles n'étant pas à jour (constat 5), aucun rendement ne peut encore être calculé par parcelle.
3. **La traçabilité jusqu'à la parcelle est inégale et faible là où l'état sanitaire est le plus dégradé** : environ 62 % des volumes sont rattachés à une parcelle, de 95 % à SAINT-BRÉZIAN à 30 % à PECHAUROUX et 40 % à CABRISSAC ; dans l'Aude, moins de la moitié des volumes l'est. *Conséquence* : une reconnaissance de la qualité **par parcelle** est impossible aujourd'hui pour plus d'un tiers de la vendange. *Précaution* : les données manquantes **ne sont pas réparties au hasard** (biais de sélection) : les moyennes calculées sur les seuls apports rattachés représentent mal les caves les moins renseignées.
4. **Le degré, critère actuel de rémunération, est un indicateur ambigu de la qualité** : il va de 12,5 à 14,0 % vol. et suit la part haut de gamme, mais le plan « ROCALDÈNE 2030 » veut adapter l'offre au changement climatique, ce qui ne pousse pas à récompenser toujours plus de degré. *Précaution* : les degrés de LAURADEL et de CABRISSAC sont convertis à partir des sucres, et une moyenne par cave masque la dispersion entre parcelles et entre cépages.

Précautions communes, valorisées si elles sont citées : **une seule vendange** (aucune tendance), données **agrégées par cave** (rien sur les parcelles ni les viticulteurs), tableau **établi à la main** pour la première fois.

**Appréciation des deux positions** (0,5 pt) : M. SOULAGNET lit le tableau dans le sens qui favorise sa cave (**biais de confirmation**) et en tire une conclusion que les données ne portent pas : la part haut de gamme dépend des choix de l'union, et l'état sanitaire n'est pas mesuré de la même façon partout. Mme TARASCOUL relève à juste titre deux défauts de comparabilité (échelles, part haut de gamme décidée par l'union), mais son explication par la pluie n'est pas vérifiable pour sa cave, sans station, et ne vaut pas preuve. Conclusion pour le conseil : ce tableau peut ouvrir le débat, il ne peut pas fonder une rémunération ; il faut d'abord des mesures communes (dictionnaire, échelle, parcelle obligatoire) dès la vendange 2027, puis décider sur des données comparables, éventuellement après une année d'observation.

*2.4 c) – Méthode d'analyse et prévision par parcelle*

**Méthode** (0,5 pt) : l'annexe 2.2 relève de l'analyse **descriptive** (moyennes et parts par cave, ce qui s'est passé), encore fragile. L'étape suivante est une analyse **exploratoire** : au niveau de l'apport et de la parcelle, rechercher les profils et les facteurs associés à la qualité (cépage, âge des vignes, secteur, pluie, rendement, date d'apport), repérer les valeurs aberrantes, et tester les hypothèses du b) (rôle de la pluie, effet de l'échelle, effet du rendement). Elle sert la question du conseil (quels critères de qualité retenir et sont-ils équitables entre caves) et reste explicable aux présidents. Elle suppose les données harmonisées de la question 2.2 ; sur la vendange 2026, elle se limite aux caves et aux apports rattachés.

**Prévision par parcelle prématurée** (0,5 pt pour deux arguments, parmi les suivants) :
1. **Pas d'historique fiable au niveau de la parcelle** : une seule vendange rassemblée, à la main ; identifiants de parcelle non uniques ; plus d'un tiers des volumes sans parcelle ; un modèle de prévision apprend sur des exemples passés, qui n'existent pas.
2. **Des données de qualité non comparables** : la variable à prévoir (l'état sanitaire, le degré) est mesurée sur des échelles et dans des unités différentes ; le modèle apprendrait les différences de notation entre caves plutôt que la qualité.
3. **Une couverture météorologique trop partielle** : quatre stations pour neuf secteurs, des sondes dans 30 parcelles sur 11 000, des observations dispersées dans trois tableurs personnels.
4. **Un usage à fort enjeu et peu explicable** : fixer des primes avant les vendanges sur une prévision opaque, pour 1 400 adhérents, serait contesté par les caves dès la première erreur ; la décision doit rester humaine et fondée sur des critères compris.
La prévision pourra être reconsidérée après plusieurs vendanges de données propres, comme aide aux techniciens plutôt que comme base de rémunération.

*2.4 d) – Deux représentations visuelles* (0,5 pt)

| Destinataire | Représentation | Message | Piège à éviter |
|---|---|---|---|
| Conseil de l'union | barres horizontales triées par cave de la part des apports à l'état sanitaire dégradé (à partir de la vendange 2027, sur l'échelle commune ; pour 2026, en séparant les deux échelles), avec la part des volumes rattachés à une parcelle affichée à côté (ou nuage de points rendement / part haut de gamme, une bulle par cave proportionnelle au volume) | où sont les écarts de qualité et quelle confiance leur accorder | comparer des notes d'échelles différentes ; axe tronqué qui grossit les écarts ; lire une corrélation comme une causalité ; volumes absolus au lieu de taux |
| Directeurs de cave | carte des parcelles de la cave colorée selon l'état sanitaire moyen des apports (ou histogramme de la répartition des apports de la cave par note, comparé à celle de l'union) | quelles parcelles et quels secteurs améliorer ou mieux renseigner | carte en valeurs brutes, qui fait ressortir les grandes parcelles ; couleurs non signifiantes ; parcelles sans apport rattaché laissées vides sans le signaler |

**Réponses tolérées**
- Chaîne de valeur présentée selon les étapes de la chaîne décisionnelle (collecte, extraction, transformation et chargement, entrepôt, restitution), si la décision du conseil la termine.
- Autres constats tirés de l'annexe 2.2 (CAUSSELAC, première cave en volume, la moins valorisée ; écart de structure entre Hérault et Aude) s'ils sont assortis d'une précaution.
- Position recommandant une rémunération limitée à un critère déjà fiable (par exemple l'apport rattaché à une parcelle), si elle est argumentée.
- Analyse descriptive fiabilisée recommandée pour la vendange 2027, avant l'exploratoire, si le candidat le justifie par la qualité des données.
- Autres représentations adaptées (barres empilées à 100 % par note sanitaire, carte choroplèthe en taux), si le message et le piège sont précisés.

**Erreurs fréquentes**
- *Corrélation = causalité* (`ET-26`) — « les faibles rendements font la qualité » ou « la pluie explique l'état sanitaire de l'Aude » ; juste : hypothèses à vérifier, facteurs communs et effets de mesure examinés.
- *Extrapolation sans précaution* (`JUR-D06`) — conclusions tirées d'une seule vendange ; juste : une année ne fait pas une tendance.
- *Interprétation isolée de la décision* (`JUR-T03`) — constats décrits sans conséquence pour le conseil ; juste : chaque constat dit ce que le conseil peut ou ne peut pas décider.
- *Science des données = BI* (`ET-25`) — confondre l'analyse descriptive du tableau et la prévision du prestataire ; juste : finalités et exigences de données différentes.
- *Calculs inutiles ou hors sujet* (`JUR-T07`) — moyennes pondérées recalculées, barème de primes construit ; juste : interpréter les écarts lus, sans calcul de rémunération.
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — le service de prévision présenté comme un assistant conversationnel ; juste : une prévision apprend des régularités sur des données passées.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne décisionnelle et chaîne de valeur des données | étapes, points de vigilance | F08 § 1 | notion de cours |
| Analyses descriptive, exploratoire, prédictive | finalités, prérequis, limites | F08 § 2 | notion de cours |
| Choix des représentations, biais de lecture, corrélation et causalité | graphiques adaptés, pièges | F08 § 5 | notion de cours |

---

### 2.5 – Le projet d'authentification des cuvées exportées (2,5 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.a` « Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain » ; `3.3.d` « Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO ».

**Annexes mobilisées** : annexes 1.1 (export 25 % du chiffre d'affaires, budget du SI de 2 200 k€, plan « ROCALDÈNE 2030 » et empreinte environnementale), 2.3 (problème signalé, proposition de SCELLAVIN, coûts, alternative, avis) et 2.4 (MiCA, RGPD, ISO 22739).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Blockchain définie (registre distribué, consensus, inaltérabilité pratique, confiance sans tiers) et distinguée d'une base centralisée ; projet situé dans la typologie : certification d'authenticité et traçabilité, au moyen de jetons non fongibles | 0,5 |
| b-1 | Deux opportunités et trois risques ou limites tirés de l'annexe 2.3 (dont l'oracle : la chaîne garantit l'enregistrement, pas la bouteille) | 0,5 |
| b-2 | Comparaison avec l'alternative : coûts de tête sur trois ans (930 k€ contre 330 k€), apports et limites du code signé | 0,5 |
| b-3 | Recommandation argumentée et conditionnée | 0,5 |
| c | Condition d'exclusion du champ de MiCA (jetons réellement uniques et non fongibles) et respect du RGPD pour les prénoms et les villes des consommateurs ; la remarque sur la revente séparée est valorisée | 0,5 |

**Réponse attendue**

*2.5 a) – Blockchain et typologie* (0,5 pt)

Une **blockchain** est un registre distribué, répliqué entre plusieurs nœuds, dont les blocs de transactions sont chaînés par des empreintes cryptographiques et validés par un mécanisme de consensus (ici la preuve d'enjeu) ; elle permet à des acteurs qui ne se font pas confiance de partager une information horodatée et pratiquement inaltérable, **sans tiers de confiance**. Une **base de données centralisée** est tenue par un administrateur unique (ici l'union), qui peut la modifier et en qui les utilisateurs doivent avoir confiance ; elle est plus simple, moins coûteuse et plus rapide (F11 § 1 ; ISO 22739:2024 pour le vocabulaire).

Le projet de SCELLAVIN relève de deux usages de la typologie : la **certification d'authenticité** (preuve que la bouteille vient de l'union) et la **traçabilité** (historique des détenteurs successifs), au moyen d'un **jeton non fongible (NFT)** par bouteille, sorte de double numérique de l'objet physique. Il ne relève ni de la finance décentralisée ni de la tokenisation d'un actif financier ; la revente envisagée des jetons sur une place de marché le ferait glisser vers un usage spéculatif.

*2.5 b) – Opportunités, risques et comparaison avec l'alternative*

**Deux opportunités** (parmi les suivantes) :
1. une **preuve d'origine vérifiable par des tiers** sans compte chez l'union ni confiance dans son site, ce que demande le distributeur canadien ;
2. un **historique horodaté des détenteurs**, qui permettrait de repérer des bouteilles sorties du circuit prévu ;
3. une **étiquette connectée** qui se détruit au décollage, plus difficile à copier qu'une étiquette imprimée ;
4. une **image de modernité** auprès des importateurs asiatiques (M. SALVERNAC), à ne pas surestimer.

**Trois risques ou limites** (0,5 pt avec les opportunités, parmi les suivants) :
1. **Le problème de l'oracle** : la blockchain garantit que l'enregistrement n'a pas été modifié, non qu'il est vrai, ni que la bouteille est celle qui a été enregistrée (« si nos données de départ sont fausses, la blockchain les gardera fausses pour toujours ») ; la protection contre la copie tient à l'étiquette, non à la blockchain.
2. **Un seul acteur écrit l'origine** : l'union est la seule source des informations de départ ; selon la grille d'opportunité (plusieurs acteurs qui écrivent et ne se font pas confiance), une base centralisée tenue par l'union, propriétaire de la marque, suffit (F11 § 2.2).
3. **Des données personnelles inscrites sur une blockchain publique** : prénoms et villes des consommateurs ne pourraient plus être effacés, ce qui heurte la minimisation et l'effacement prévus par le RGPD (annexe 2.4).
4. **Coût et proportionnalité** : environ 2 000 bouteilles contrefaites signalées, soit environ 0,3 % des 600 000 bouteilles exportées, pour un projet de 930 k€ sur trois ans.
5. **Dépendance** envers une jeune entreprise qui choisit seule la blockchain et tient la place de marché ; avenir des jetons et de la vérification si elle disparaît.
6. **Empreinte environnementale** : la preuve d'enjeu consomme peu d'énergie, mais une puce électronique jetable sur 600 000 bouteilles par an produit des déchets électroniques, à rebours de la priorité du plan « ROCALDÈNE 2030 » sur l'empreinte environnementale.

**Comparaison avec l'alternative** (0,5 pt) : estimation de tête, sans actualisation :
- SCELLAVIN : 120 + 90 + 3 × (180 + 60) = 210 + 720 = **930 k€** sur trois ans, soit environ 310 k€ par an (environ 14 % du budget annuel du SI de 2 200 k€) ;
- alternative : 150 + 3 × (30 + 30) = 150 + 180 = **330 k€** sur trois ans, soit environ 110 k€ par an (environ 5 % du budget du SI) ; écart : 600 k€.

L'alternative répond au besoin principal (prouver l'origine, lire le code avec un téléphone, signaler un code déjà lu ailleurs), garde les données et la maîtrise à l'union, n'inscrit aucune donnée personnelle dans un registre inaltérable et ne met pas de puce sur chaque bouteille. Ses limites : un code imprimé peut être **copié** sur une fausse bouteille (d'où la détection des lectures multiples, et éventuellement une capsule ou une étiquette inviolable), et les tiers doivent faire confiance au site de l'union, ce qui est acceptable puisque l'union est le producteur et le propriétaire de la marque.

**Recommandation** (0,5 pt) : retenir l'alternative centralisée, en pilote d'une campagne sur le marché de Hong Kong, complétée si besoin par un dispositif inviolable sur la capsule ; mesurer les lectures multiples et les retours des importateurs ; ne pas inscrire de données de consommateurs. Reconsidérer une blockchain, plutôt **permissionnée et partagée avec les importateurs et distributeurs**, seulement si plusieurs acteurs doivent écrire dans le registre sans se fier à l'union et si le coût se justifie. Refuser en tout état de cause la revente séparée des jetons.

*2.5 c) – Cadre réglementaire* (0,5 pt)

D'après les repères de l'annexe 2.4, le règlement (UE) 2023/1114 « MiCA », applicable depuis le 30/12/2024, exclut de son champ les crypto-actifs **uniques et non fongibles** (article 2 § 3) : les jetons de SCELLAVIN y échappent **à condition d'être réellement uniques et non fongibles** : un jeton par bouteille, non interchangeable et non fractionné. La revente des jetons séparément des bouteilles ne relève pas de cette condition, mais elle détacherait la preuve d'authenticité de la bouteille et donnerait au projet un caractère spéculatif ; un avis spécialisé serait utile avant de l'envisager (remarque valorisée, non exigée). Le projet doit en revanche respecter le **RGPD** (applicable depuis le 25/05/2018) pour les prénoms et villes des consommateurs, comme pour les données des adhérents : finalités, minimisation, durée de conservation, effacement, ce qu'une inscription sur une blockchain publique rend impossible. ISO 22739:2024 n'est qu'une norme de vocabulaire : elle ne crée aucune exigence ni certification.

**Réponses tolérées**
- Projet situé seulement dans la traçabilité ou seulement dans la certification, si le rôle du jeton non fongible est expliqué.
- Recommandation de l'étiquette connectée sans blockchain, adossée au registre centralisé de l'union, si le coût et l'empreinte des puces sont discutés.
- Pilote limité du projet de SCELLAVIN sur une cuvée, si le candidat exige l'absence de données personnelles sur la chaîne, la réversibilité et l'abandon de la revente séparée.
- Coûts estimés par an plutôt que sur trois ans, si la comparaison reste juste.

**Erreurs fréquentes**
- *Blockchain = base de données distribuée* (`ET-08`) — « la blockchain est une base partagée plus sûre » ; juste : registre de confiance entre acteurs qui ne se font pas confiance, au prix de la performance.
- *Opportunités sans risques* (`ET-19`) — reprendre l'enthousiasme de M. SALVERNAC sans l'oracle, le coût ni le RGPD.
- *Inaltérabilité = vérité* — croire que l'inscription prouve l'authenticité de la bouteille ; juste : la chaîne garantit l'intégrité de l'enregistrement, pas l'exactitude des données saisies.
- *MiCA appliqué à tout jeton* (`ET-35`) — affirmer que les jetons de SCELLAVIN exigent un agrément ; juste : exclusion des crypto-actifs uniques et non fongibles, sous condition.
- *Analyse juridique, fiscale ou comptable* (`JUR-T07`) — développements sur le statut juridique des jetons ou leur traitement dans les comptes ; juste : s'en tenir aux repères fournis.
- *Énergie oubliée ou exagérée* — preuve d'enjeu confondue avec la preuve de travail ; juste : consommation modérée, mais déchets des puces à prendre en compte.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2023/1114 « MiCA », applicable depuis le 30/12/2024 | définition du crypto-actif, exclusion des crypto-actifs uniques et non fongibles (article 2 § 3) (repères de l'annexe 2.4) | `mica` / F11 § 3 ; `commun/fiches/sapin2_lcbft_mica.md` § 3.1 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | minimisation, effacement, données des consommateurs | `rgpd` / F15 | en vigueur |
| ISO 22739:2024 | vocabulaire des chaînes de blocs et des registres distribués | `iso_22739_2024` / F11 § 3.4 | en vigueur |
| Typologie des usages, grille d'opportunité, limites (oracle, énergie, gouvernance) | analyse du projet | F11 § 1 et 2 | notion de cours |
