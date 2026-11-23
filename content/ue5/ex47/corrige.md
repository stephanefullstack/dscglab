# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 47 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F06 connaissances et dématérialisation (cachet électronique), F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F09 performance du SI, F11 chaîne de blocs et crypto-actifs, F13 intelligence artificielle, F15 RGPD opérationnel, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, schéma en étoile exécuté, indicateurs, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 L'entrepôt des séjours | `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) ; `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 3,5 |
| 2.2 L'analyse de l'occupation et des demandes d'intervention | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation | 4 |
| 2.3 Le retour sur investissement du projet d'entrepôt | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord | 3 |
| 2.4 Les attestations de logement et la chaîne de blocs | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.a` Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations ; `3.3.d` Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO | 2,5 |
| **Dossier 2 – Organiser et exploiter les données des séjours, éclairer deux projets** |  | **13** |

Répartition indicative : connaissances (entrepôt de données, table des faits, dimensions et granularité, règles de passage, chaîne de traitement, analyses descriptive et exploratoire, retour sur investissement, indicateur à cinq champs, chaîne de blocs publique et empreinte, typologie des applications, objet de MiCA) environ 2,5 points (la moitié des items 2.1 a-1, 2.1 b-1, 2.1 b-4, 2.2 a-1, 2.2 c-2, 2.3 a-1, 2.3 c-1, 2.4 a-1, 2.4 a-2 et 2.4 c-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – L'entrepôt des séjours (3,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) » ; `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) », dont le schéma en étoile d'un entrepôt (faits, dimensions) fait à la main à partir de règles de gestion écrites ; `2.1.a` « Structurer et organiser les données […] afin d'en garantir la cohérence, la qualité […] ». Aucune requête ; modèle physique seulement nommé.

**Annexes mobilisées** : annexe 2.1 (situation actuelle, questions du directoire, règles de gestion de l'entrepôt) ; annexe 1.1 (logiciel de gestion locative, portail, logiciel de suivi des demandes d'intervention, parc).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Entrepôt de données défini (orienté sujet, intégré, historisé, non volatile, structuré pour l'analyse) ; première raison appliquée à l'annexe 2.1 | 0,5 |
| a-2 | Deuxième raison, tirée de l'annexe 2.1 | 0,5 |
| a-3 | Troisième raison ; conclusion : une seule version des chiffres, à condition d'écrire les règles de calcul, sans données nominatives (RG8) | 0,5 |
| b-1 | Table des faits et granularité justifiée par RG6 (un logement, un mois, un profil de séjour, un canal de réservation) ; faits et dimensions distingués | 0,5 |
| b-2 | Quatre dimensions et leurs attributs, dont la dimension temps ; résidence et ville dénormalisées dans la dimension Logement (étoile) | 0,5 |
| b-3 | Quatre mesures additives (RG7), dont les jours-places ; taux d'occupation calculé à la restitution, non stocké ; profil « aucun séjour » pour la vacance | 0,5 |
| b-4 | Modèle logique de cinq tables, avec la clé composée des quatre clés étrangères de la table des faits, déduit par les règles de passage énoncées | 0,5 |

**Réponse attendue**

*2.1 a) – L'entrepôt de données et les extractions mensuelles*

**Définition** (0,5 pt avec la première raison) : un **entrepôt de données** est une base **orientée sujet** (ici, les séjours et l'occupation), **intégrée** (les données de plusieurs applications y sont rapprochées selon des identifiants et des définitions communes), **historisée** et **non volatile** (les données chargées ne sont ni écrasées ni modifiées, l'historique s'accumule), structurée pour l'analyse, en général selon un schéma en étoile (faits et dimensions). Il est alimenté par des chargements réguliers depuis les applications de gestion, qu'il ne remplace pas (F07 § 1 et 6).

Trois raisons parmi les suivantes (0,5 pt par raison, la troisième avec la conclusion) :

1. **L'intégration des trois sources.** Aujourd'hui, deux personnes rapprochent à la main, chaque mois, le logiciel de gestion locative, le portail et le logiciel des demandes d'intervention, par l'adresse, faute de numéro de logement commun : huit jours-personne par mois, avec des risques d'erreur. L'entrepôt est chargé chaque nuit et rapproche les données par un **numéro unique de logement**, commun à toutes les applications (RG1).
2. **L'historisation.** Chaque extraction remplace la précédente, et l'historique n'existe que dans des tableurs aux colonnes changeantes : comparer 2025 et 2026, ou un été à l'autre, suppose de retraiter les fichiers. L'entrepôt conserve chaque mois, avec la dimension temps, ce qui permet de suivre l'occupation par mois, par saison et par année universitaire.
3. **Des définitions communes, donc un seul chiffre.** Le taux d'occupation de 2026 vaut 93 %, 91 % ou 95 % selon la direction, parce que chacune applique ses propres règles, écrites nulle part. L'entrepôt calcule les indicateurs selon des règles écrites et partagées (RG6 et RG7, documentées dans le dictionnaire des données) : une seule version des chiffres pour le directoire.
4. **Des axes d'analyse croisés.** Les questions du directoire croisent la résidence, la ville, le type de logement, le mois, le profil de séjour, l'origine du résident et le canal : le schéma en étoile en fait des dimensions, sur lesquelles on agrège et on fore (de la ville à la résidence, puis au logement) sans retraitement.
5. **Une diffusion possible sans risque pour les résidents.** L'entrepôt ne contient ni donnée nominative ni donnée sensible (RG8) : il peut être ouvert aux directions et aux responsables de résidence, ce que ne permettent pas des extractions brutes du logiciel de gestion locative.

**Conclusion** : l'entrepôt ne vaut que par ses règles. Le gain tient moins à l'outil qu'à la décision de fixer un identifiant commun, des définitions écrites et un propriétaire de chaque indicateur ; c'est aussi la condition pour suivre l'objectif de 95 % d'« ORVANELLE 2030 » avec un chiffre incontesté.

*2.1 b) – Le schéma en étoile de l'entrepôt des séjours*

**La table des faits et sa granularité** (0,5 pt) : la **table des faits** enregistre les mesures d'un événement ou d'une situation, au **grain** choisi ; les **dimensions** sont les axes d'analyse, avec leurs attributs descriptifs (F07 § 6.1). Ici, la table des faits **Occupation_mensuelle** a pour grain : **un logement, un mois, un profil de séjour et un canal de réservation** (RG6). Un grain « logement × mois » ne suffirait pas : une colocation dont les chambres sont louées à des résidents de profils différents, ou un logement qui passe en juillet de l'année universitaire à un séjour court d'été, demandent une ligne par profil et par canal. Un grain plus fin (le jour, le séjour) n'est pas nécessaire aux questions du directoire.

**Les quatre dimensions** (0,5 pt) :
- **Logement** (num_logement, type_logement, nb_places, code_residence, nom_residence, date_ouverture_residence, ville) : la hiérarchie logement → résidence → ville (RG1 et RG2) est **dénormalisée** dans la dimension, ce qui fait un schéma en **étoile** et permet de forer de la ville au logement ;
- **Mois** (code_mois, annee, numero_mois, saison, annee_universitaire) : la dimension temps, avec la saison (été ou année universitaire) et l'année universitaire, qui ne coïncide pas avec l'année civile (RG3) ;
- **Profil_sejour** (code_profil, type_sejour, origine_resident) : le type de séjour (année universitaire, séjour court d'été, aucun séjour) et l'origine du résident (RG4) ; c'est la seule trace du résident, conformément à RG8 ;
- **Canal_reservation** (code_canal, libelle_canal) (RG5).

**Les mesures** (0,5 pt), toutes **additives** selon chaque dimension : jours_places_ouverts, jours_places_occupes, redevance_facturee, nb_demandes_intervention (RG7). Les jours où un logement pouvait être loué mais est resté libre forment une ligne du profil « aucun séjour », avec des jours-places ouverts et aucun jour-place occupé ; un logement en travaux ou dans une résidence pas encore ouverte n'a pas de jours-places ouverts. Les indicateurs sont calculés à la restitution, par somme puis rapport, à n'importe quel niveau :
- taux d'occupation = somme des jours-places occupés / somme des jours-places ouverts ; taux de vacance = 1 − taux d'occupation ;
- part des séjours courts dans l'été = jours-places occupés par le profil « séjour court d'été » en saison « été » / jours-places occupés en été ;
- part du portail = jours-places occupés par des séjours réservés sur le portail / jours-places occupés ;
- demandes d'intervention par logement, par résidence ou par type.

Un taux ne se stocke pas dans la table des faits : il ne s'additionne pas.

**Le modèle logique** (0,5 pt), obtenu par les règles de passage :
1. chaque dimension devient une table, dont l'identifiant devient la clé primaire ;
2. la table des faits traduit une association entre les quatre dimensions dont toutes les cardinalités maximales valent n : elle devient une table dont la clé primaire est composée des identifiants des quatre dimensions, chacun étant aussi clé étrangère, et qui porte les mesures.

- Logement (<u>num_logement</u>, type_logement, nb_places, code_residence, nom_residence, date_ouverture_residence, ville)
- Mois (<u>code_mois</u>, annee, numero_mois, saison, annee_universitaire)
- Profil_sejour (<u>code_profil</u>, type_sejour, origine_resident)
- Canal_reservation (<u>code_canal</u>, libelle_canal)
- Occupation_mensuelle (<u>#num_logement, #code_mois, #code_profil, #code_canal</u>, jours_places_ouverts, jours_places_occupes, redevance_facturee, nb_demandes_intervention)

Exemple de lecture : une colocation de trois chambres de Rennes, en octobre 2026, dont deux chambres sont louées pour l'année universitaire à des résidents venus de l'étranger, réservées sur le portail, et la troisième reste libre, donne deux lignes : (profil « année universitaire, étranger », canal « portail », 62 jours-places ouverts, 62 occupés) et (profil « aucun séjour », canal « sans objet », 31 ouverts, 0 occupé). Son taux d'occupation d'octobre est de deux tiers, et non de zéro comme dans le tableau actuel.

**Réponses tolérées**
- Schéma en flocon (tables Résidence et Ville, ou Type de logement, reliées à la dimension Logement), s'il est justifié (moins de redondance, plus de jointures) et si les faits restent reliés au logement.
- Cinquième dimension (Résidence ou Type de logement) reliée directement à la table des faits, si la redondance avec la dimension Logement est signalée.
- Grain « logement × mois », avec le profil et le canal du séjour principal du mois, si le candidat signale la perte d'information pour les colocations.
- Identifiant technique de ligne dans la table des faits, en plus des quatre clés étrangères.
- Représentation de type Merise (association porteuse des mesures entre quatre entités) ou dessin de l'étoile, si elle est lisible (`JUR-T10`).
- Autres raisons tirées de l'annexe 2.1 en a), si elles sont appliquées au cas (fraîcheur quotidienne, libre-service des directions).

**Erreurs fréquentes**
- *Entrepôt confondu avec un lac de données ou avec une base de production* (`ET-24`) — entrepôt présenté comme une copie des applications ou comme un stockage de données brutes.
- *Modèle de gestion au lieu d'un schéma en étoile* — entités Résident, Bail, Candidature avec leurs associations : c'est le modèle d'un logiciel de gestion, non celui d'un entrepôt ; un résident nominatif contredit en outre RG8.
- *Granularité absente ou incohérente* — table des faits sans grain énoncé, ou mesures qui ne s'additionnent pas (taux d'occupation stocké).
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères oubliées ou clé de la table des faits non composée.
- *Morceau de cours ou requête hors attente* (`JUR-T01`, `JUR-T07`) — définition de l'entrepôt sans application au cas, ou requêtes écrites alors que la question n'en demande pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Entrepôt de données ; schéma en étoile et en flocon ; faits, dimensions, grain, mesures additives | définitions et méthode | F07 § 1 et 6 ; F08 § 1 | notion de cours |
| Règles de passage au modèle logique | méthode | F07 § 4 | notion de cours |

---

### 2.2 – L'analyse de l'occupation et des demandes d'intervention (4 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique ». Limites : aucun calcul statistique, aucune manipulation d'outil, aucun développement d'algorithme ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexe 2.2 (occupation par ville et par type, affirmation du directeur commercial, limites) ; annexe 2.3 (demandes d'intervention, extraits, projet de l'équipe données) ; annexes 2.1 (règles de l'entrepôt) et 2.6 (principes du RGPD) ; « ORVANELLE 2030 » (présentation).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Étapes de la chaîne présentées ; résidences de Rennes et logements en travaux de Toulouse : étape où chaque limite est corrigée, et comment | 0,5 |
| a-2 | Colocations comptées par logement et écart entre les taux des directions : étape et correction ; conclusion | 0,5 |
| b-1 | Deux constats argumentés et chiffrés, avec leur portée pour « ORVANELLE 2030 » | 0,5 |
| b-2 | Troisième constat argumenté et chiffré | 0,5 |
| b-3 | Affirmation appréciée (résidences ouvertes en cours d'année et effet de structure, unité de mesure des colocations, été et groupes, canal) ; conclusion nuancée | 0,5 |
| c-1 | Deux apports de l'exploitation du texte des demandes, appliqués au cas (catégories, langues, problèmes récurrents, interventions) | 0,5 |
| c-2 | Méthode d'analyse : descriptive et surtout exploratoire, justifiée ; ni prédiction ni développement | 0,5 |
| c-3 | Deux précautions justifiées par l'annexe 2.3 et les principes de l'annexe 2.6 | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de traitement des indicateurs d'occupation*

**La chaîne de traitement** (0,5 pt avec les limites de Rennes et de Toulouse) transforme des données brutes en information utile à la décision : **collecte** des données à leur source, **nettoyage** (doublons, valeurs manquantes, aberrantes ou incohérentes), **structuration** (règles de gestion et de calcul, rapprochements, chargement dans un entrepôt historisé), **analyse**, puis **restitution** aux décideurs (F08 § 1). Chaque étape peut introduire un biais que les suivantes ne corrigent pas. Pour les indicateurs d'occupation :

| Étape | Ce que fera la chaîne | Limite corrigée (annexe 2.2 D, écart des taux de l'annexe 2.1 A) |
|---|---|---|
| **Collecte** | chargement chaque nuit des trois applications, par le numéro unique de logement ; collecte, en plus des baux, des dates d'ouverture des résidences, des périodes de travaux et des baux par chambre de colocation | le tableau ignore l'ouverture des résidences de Rennes au 1er septembre et la fermeture de 120 logements à Toulouse : l'information n'est pas collectée |
| **Nettoyage** | contrôles de cohérence : aucun jour vacant compté pour un logement fermé ou une résidence pas encore ouverte ; rejets tracés dans un journal | les 120 logements de Toulouse en travaux sont comptés comme vacants pendant six mois, ce qui fait passer Toulouse de 94 % à 88 % |
| **Structuration** | application des règles RG6 et RG7 au chargement : jours-places, une place par chambre de colocation, jours ouverts seulement après l'ouverture et hors travaux | le dénominateur « logements en fin d'année × 365 » compte Rennes sur douze mois, été compris ; une colocation n'est occupée que si toutes ses chambres le sont |
| **Analyse** | taux calculés comme rapports de sommes, à n'importe quel niveau ; comparaison à périmètre constant (résidences ouvertes les deux années) à côté du total | l'ensemble mêle les résidences nouvelles et anciennes : la baisse de 94 % à 91 % est lue comme une dégradation |
| **Restitution** | tableau de bord dans l'outil décisionnel, avec la définition de chaque indicateur, le périmètre et la cible de 95 % ; occupation par chambre pour les colocations | écart entre les taux des directions (93 %, 91 % et 95 %, annexe 2.1 A) : un seul taux, défini une fois, pour tous |

En résumé : Rennes est corrigé à la collecte (date d'ouverture) et à la structuration (jours ouverts) ; Toulouse à la collecte (périodes de travaux) et au nettoyage ; les colocations à la collecte (baux par chambre) et à la structuration (jours-places) ; l'écart entre les directions à la structuration (règles écrites RG6 et RG7) et à la restitution.

**Conclusion** (0,5 pt avec les colocations et l'écart des directions) : les limites du tableau ne sont pas des erreurs de calcul, mais des règles implicites. La chaîne les corrige en amont, par la collecte des bonnes informations et des règles écrites, et non par des retraitements à la main en fin de mois.

*2.2 b) – Trois constats et l'affirmation de M. CALVÉRAC*

**Trois constats** parmi les suivants (0,5 pt pour deux constats, 0,5 pt pour le troisième : le fait chiffré, son interprétation et sa portée) :

1. **La baisse de l'occupation de 94 % à 91 % est surtout un effet de mesure.** Lyon (96 %) et Montpellier (95 %) sont stables, les onze autres villes progressent (de 93 % à 94 %). La baisse vient de Rennes (30 %), dont les 400 logements, ouverts en septembre, sont comptés sur l'année entière, et de Toulouse (de 94 % à 88 %), où 120 logements étaient fermés pour travaux. Rennes pèse à lui seul près de trois points sur l'ensemble ; mesurée sur les seuls jours ouverts, l'occupation de 2026 serait plutôt de l'ordre de 94 à 95 %, proche de l'objectif de 95 %. Le directoire ne doit pas réagir à une baisse qui n'existe pas.
2. **L'été est le vrai creux.** L'occupation tombe à 69 % en juillet et août, contre 91 % sur l'année ; les séjours courts y font de 30 % (studios) à 70 % (colocations) de l'occupation. Atteindre 95 % en moyenne annuelle passera par l'été : offre de séjours courts, accueil de groupes, ce que l'entrepôt permettra de suivre par profil et par canal.
3. **Le portail progresse, sauf pour les colocations.** La part des réservations faites sur le portail passe de 62 % à 65 %, et de 65 % à 70 % pour les studios, mais reste à 30 % pour les colocations : le portail ne permet pas de réserver une chambre seule. C'est un frein commercial, en contradiction avec le parcours entièrement en ligne voulu par « ORVANELLE 2030 ».
4. **Le délai de relocation des colocations est mesuré à la dernière chambre.** 35 jours contre 10 pour les studios, mais une colocation n'est relouée, dans le tableau, que lorsque sa dernière chambre libre l'est : l'indicateur compare des unités différentes.

**L'affirmation de M. CALVÉRAC** (0,5 pt) : « les colocations se louent mal, de plus en plus mal » n'est pas démontré :
- **les résidences ouvertes en cours d'année créent un effet de structure** : 200 des 900 colocations, soit plus d'une sur cinq, sont à Rennes, ouvertes en septembre et comptées sur l'année et sur l'été. La baisse de 84 % à 74 % sur l'année et de 78 % à 61 % en été vient de ce changement de composition : les 200 colocations de Rennes n'existaient pas l'été 2026. Hors Rennes, les colocations anciennes ont plutôt progressé ;
- **l'unité de mesure les pénalise** : une colocation de trois chambres dont deux sont louées est comptée vacante, et n'est relouée qu'avec sa dernière chambre. Comparer ce taux à celui d'un studio, qui n'a qu'une place, compare des unités différentes ; mesurée par chambre, l'occupation des colocations serait plus élevée et leur délai de relocation plus court ;
- **elles sont le meilleur produit de l'été** : 78 % d'occupation en juillet et août 2025, le taux le plus élevé des trois types, avec 70 % de séjours courts, surtout des groupes. Les transformer en studios ferait perdre une partie de ces séjours, qui relèvent des 8 M€ de services et de séjours courts ;
- **le canal explique une partie de la difficulté** : 30 % seulement des colocations sont réservées sur le portail, qui ne vend pas les chambres une à une.

Conclusion : retenir le chiffre qui conforte une conviction, sans examiner la composition ni l'unité de mesure, relève du **biais de confirmation** (F08 § 5). Avant toute transformation, il faut mesurer l'occupation des colocations par chambre, à périmètre constant et par saison, dans l'entrepôt, et d'abord ouvrir la réservation des chambres sur le portail.

*2.2 c) – Le texte des demandes d'intervention*

**Deux apports** parmi les suivants (0,5 pt) :
- **des catégories fiables, quelle que soit la langue** : 40 % des 30 000 demandes de l'application sont classées « autre » et une sur quatre est mal classée, un tiers ne sont pas rédigées en français. Aujourd'hui, aucune statistique par catégorie n'a de sens ;
- **les problèmes récurrents, par résidence** : regrouper les demandes semblables fait apparaître la panne qui revient (le chauffe-eau qui donne vingt demandes, l'eau froide le matin chez plusieurs voisins, la coupure du réseau chaque soir, la moisissure qui revient chaque hiver) ;
- **des interventions mieux ciblées** : traiter la cause une fois (remplacer les chauffe-eau d'une résidence) au lieu d'envoyer vingt fois un plombier, prioriser les résidences, réduire une partie des 2 M€ d'interventions extérieures, et améliorer la satisfaction des résidents ;
- **un enrichissement de l'entrepôt** : le nombre de demandes par logement, déjà prévu, pourrait être analysé par catégorie.

**La méthode d'analyse** (0,5 pt) : l'**analyse descriptive** résume ce qui s'est passé (nombre de demandes par catégorie, par résidence, par mois) ; elle ne devient possible qu'une fois les demandes bien classées. L'**analyse exploratoire** cherche des motifs que l'on ne connaissait pas d'avance, dans des données non structurées : regroupements de demandes semblables, problèmes récurrents, croisements par résidence, par saison ou par type de logement (fouille de textes) (F08 § 2). C'est elle qui est surtout mobilisée ici, puisque personne ne sait quelles pannes reviennent. Le service de l'équipe données repose sur l'**apprentissage automatique** (il apprend, à partir de 3 000 demandes classées à la main, à classer les suivantes), à distinguer de l'IA générative (F13) ; il ne fait aucune prévision, et il n'est demandé ni de le construire ni de le régler.

**Deux précautions** parmi (0,5 pt) :
- **la minimisation des données transmises** : certaines demandes contiennent un nom, un numéro de téléphone ou un problème de santé (« je suis asthmatique »), donnée soumise à des règles plus strictes (annexe 2.6). Avant l'envoi à l'éditeur, masquer ces mentions et ne transmettre que ce qui sert au classement (texte nettoyé, résidence), pour la seule finalité d'amélioration de la maintenance ;
- **l'encadrement de l'éditeur, sous-traitant** : contrat qui limite l'usage des textes à cette finalité, interdit leur réutilisation, fixe la localisation et une durée de conservation plus courte que douze mois ; avis du délégué à la protection des données et mention du traitement au registre des traitements ;
- **le contrôle de la qualité du classement** : les 3 000 demandes d'apprentissage doivent être bien reclassées (une sur quatre l'est mal aujourd'hui) ; vérifier le classement par langue, les langues rares étant moins bien représentées ; garder la validation du responsable de résidence pour les décisions d'intervention, et revoir la liste des huit catégories avec les équipes techniques ;
- **la finalité et la gouvernance** : n'utiliser les demandes ni pour juger les résidents ni pour évaluer les agents ; désigner la direction des résidences comme propriétaire des données.

**Réponses tolérées**
- Chaîne présentée selon les étapes de l'informatique décisionnelle (collecte, extraction-transformation-chargement, entrepôt, restitution), si une limite corrigée est rattachée à chaque étape.
- Chacune des trois limites et l'écart des directions rattachés à une autre étape que celles du corrigé, si le rattachement est justifié.
- Estimation de tête de l'occupation des colocations hors Rennes (environ 87 à 88 % en 2026, en supposant les studios de Rennes presque pleins depuis l'ouverture) ou de l'effet de Rennes sur l'ensemble : non exigée ; la lecture qualitative suffit.
- Autres constats tirés de l'annexe 2.2 (stabilité de Lyon et de Montpellier, délai de relocation des deux pièces), s'ils sont chiffrés et interprétés.
- Analyse diagnostique présentée comme une variante de l'analyse exploratoire.
- Autres précautions justifiées (pilote sur quelques résidences avant la généralisation, mesure du gain sur les interventions).

**Erreurs fréquentes**
- *Corrélation ou composition ignorée* (`ET-26`) — baisse des colocations attribuée au produit sans examiner Rennes, l'unité de mesure et la saison.
- *Prudence d'interprétation oubliée* (`JUR-D06`) — baisse de 94 % à 91 % lue comme une dégradation de l'activité.
- *Analyse prédictive invoquée à tort* — l'outil présenté comme une prévision des pannes ; ou description de son fonctionnement interne (algorithme, paramètres), hors attente (`JUR-T07`) ; confusion entre IA générative et apprentissage automatique (`ET-09`).
- *Informatique décisionnelle réduite à un outil* (`ET-05`, `JUR-D02`) — « l'outil décisionnel corrigera les chiffres », sans règles écrites ni collecte des bonnes informations.
- *Précautions génériques* (`JUR-T01`) — « respecter le RGPD » sans dire quelles données masquer, pourquoi, ni comment encadrer l'éditeur.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement, analyses descriptive et exploratoire, biais de confirmation, effet de composition | définitions et méthode | F08 § 1, 2 et 5 | notion de cours |
| Apprentissage automatique et IA générative distingués | définitions | F13 ; F08 § 2 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) : finalité, minimisation, conservation limitée, sous-traitant | principes donnés en annexe 2.6 | `rgpd` / F15 | applicable depuis le 25/05/2018 |

---

### 2.3 – Le retour sur investissement du projet d'entrepôt (3 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI » ; `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI […] des indicateurs et des leviers d'optimisation via des tableaux de bord ». Limites : total de tête en sommes rondes ; aucun calcul actualisé ; recul critique sur les indicateurs.

**Annexes mobilisées** : annexe 2.4 (coûts, gains annoncés, avis du membre du directoire chargé des finances) ; annexes 2.1 et 2.2 (temps de production du tableau, effets de mesure) ; présentation (remplacement du logiciel de gestion locative avant la rentrée 2028, objectif de 95 %).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Retour sur investissement défini (formule, horizon, délai de récupération ; gains financiers et non financiers ; sans actualisation) | 0,5 |
| a-2 | Calcul de tête : 720 k€ par an, 2 160 k€ sur trois ans ; coût de 600 k€ ; retour annoncé de 260 % | 0,5 |
| b-1 | Attribution discutée et réponse à M. LORMIÈRE : l'entrepôt éclaire des décisions ; autres facteurs ; effet de mesure ; entrepôt en service en 2028 ; redevances et résultat | 0,5 |
| b-2 | Deux coûts cachés tirés du cas | 0,5 |
| c-1 | Premier indicateur de suivi des bénéfices, à cinq champs | 0,5 |
| c-2 | Second indicateur à cinq champs | 0,5 |

**Réponse attendue**

*2.3 a) – Le retour sur investissement annoncé*

**Définition** (0,5 pt) : le **retour sur investissement** d'un projet de système d'information rapporte le gain net qu'il procure à son coût, sur un horizon donné : (gains cumulés − coût total) / coût total. Il se complète du **délai de récupération** (coût / gain annuel). C'est un indicateur simple, sans actualisation ; il suppose des gains mesurables, réellement attribuables au projet, et il ne dit rien des bénéfices non financiers (qualité des décisions, fin des chiffres contradictoires), qui doivent être exposés à côté (F09 § 3.3).

**Le calcul de tête** (0,5 pt) :
- gain annoncé : un point d'occupation sur 9 000 logements = 90 logements ; 90 × 8 k€ = **720 k€ par an**, soit **2 160 k€ sur trois ans** ;
- coût sur trois ans : 300 + 3 × (40 + 60) = 300 + 300 = **600 k€** ;
- retour annoncé : (2 160 − 600) / 600 = 1 560 / 600 = **260 %** ; le gain d'une année (720 k€) dépasse le coût des trois ans, ce que dit la note.

*2.3 b) – Un calcul à apprécier*

**L'attribution du point d'occupation** (0,5 pt). M. LORMIÈRE a raison sur le principe : un entrepôt ne loue aucun logement. Il éclaire des décisions (offre de l'été, vente des chambres de colocation sur le portail, travaux hors de la rentrée), et ce sont ces décisions, avec les prix, les équipes commerciales, les ouvertures de résidences et le marché, qui font l'occupation. Le calcul appelle quatre réserves :
- **le gain est attribué sans référence ni mesure** : il faudrait une situation de départ mesurée selon les mêmes règles, des décisions identifiées qui s'appuient sur l'entrepôt, et le suivi de leur effet ;
- **une partie du point peut n'être qu'un effet de mesure** : avec les règles de l'entrepôt (jours ouverts, chambres), l'occupation mesurée de 2026 remonterait de 91 % vers 94 à 95 % sans un logement loué de plus (question 2.2). Le risque est de compter comme gain la correction d'un chiffre ;
- **le calendrier** : l'entrepôt est construit en 2027 et mis en service en janvier 2028 ; compter un gain dès 2027 est impossible. Sur 2028 et 2029 seulement, le gain annoncé serait de 2 × 720 = 1 440 k€, soit un retour de (1 440 − 600) / 600 = 140 % ;
- **des redevances ne sont pas un résultat** : 720 k€ de redevances supplémentaires portent des charges (énergie, ménage, entretien, accueil) ; le gain se mesure en marge.

Réponse à M. LORMIÈRE : l'entrepôt n'est pas rentable par lui-même ; il se justifie par la fiabilité des chiffres, le temps libéré et les décisions qu'il rend possibles. Le directoire doit l'approuver sur un dossier qui sépare gains mesurables et bénéfices qualitatifs, avec des indicateurs de suivi et un responsable des bénéfices.

**Deux coûts cachés** parmi (0,5 pt) :
- **la reconstruction des chargements** : l'entrepôt est alimenté par le logiciel de gestion locative actuel, qui doit être remplacé avant la rentrée 2028, quelques mois après la mise en service de l'entrepôt : les chargements et les règles de rapprochement seront à refaire ;
- **le temps des directions** : ateliers de définition des indicateurs, recette, formation des utilisateurs, non comptés (annexe 2.4 B) ;
- **la reprise et le nettoyage de l'historique** : tableurs aux colonnes changeantes, numéros de logement différents selon les applications (annexe 2.1 A) ; créer le numéro unique commun (RG1) est un chantier à part entière ;
- **la gouvernance des données** : propriétaires des indicateurs, dictionnaire, contrôles de qualité, dans la durée ;
- **la croissance de l'abonnement** avec le nombre d'utilisateurs et un parc porté à 12 000 logements.

Le temps libéré des deux personnes (huit jours-personne par mois) n'est un gain financier que s'il est redéployé ; sinon, c'est un bénéfice qualitatif.

*2.3 c) – Deux indicateurs de suivi des bénéfices*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Temps de production des indicateurs d'occupation | nombre de jours-personne consacrés chaque mois à produire et rapprocher les indicateurs d'occupation | relevé des temps de la direction commerciale et de l'équipe données | mensuelle | au plus un jour-personne par mois au second semestre 2028 (huit aujourd'hui) | processus |
| Taux d'occupation à périmètre constant | jours-places occupés / jours-places ouverts × 100, pour les résidences ouvertes depuis plus d'un an | entrepôt des séjours (table des faits Occupation_mensuelle) | mensuelle, bilan annuel présenté au directoire | au moins 95 % en 2030 (objectif d'« ORVANELLE 2030 »), avec une référence 2026-2027 recalculée selon les règles de l'entrepôt | financier |

Le second indicateur n'attribue pas à lui seul le gain à l'entrepôt : il se lit avec le registre des décisions prises à partir de l'entrepôt et de leur effet (par exemple, l'occupation de l'été des colocations après l'ouverture de la réservation par chambre).

**Réponses tolérées**
- Délai de récupération calculé (600 / 720, moins d'un an) à la place ou en plus du retour en pourcentage.
- Gain calculé avec 8 160 € par logement (680 € × 12), soit environ 734 k€ par an, si l'arrondi de l'énoncé est signalé.
- Autres coûts cachés justifiés par le cas (conduite du changement, dépendance à l'éditeur de l'outil décisionnel, réversibilité).
- Autres indicateurs à cinq champs : taux d'utilisation de l'outil décisionnel par les directions (axe apprentissage), part des indicateurs du directoire documentés dans le dictionnaire, occupation des chambres de colocation en été.

**Erreurs fréquentes**
- *Calcul hors attente* (`JUR-T07`) — calcul financier élaboré, alors que la question demande un total de tête en sommes rondes.
- *Retour sur investissement et coût total confondus* (`ET-33`) — ou coûts récurrents oubliés dans le coût.
- *Gain repris sans examen* (`JUR-T03`) — chiffre de la direction des systèmes d'information accepté tel quel, sans attribution, calendrier ni distinction entre redevance et marge.
- *Indicateur incomplet ou générique* (`ET-18`) — indicateur sans formule, source, fréquence, cible ou axe, ou sans lien avec les bénéfices annoncés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Retour sur investissement, délai de récupération, coûts cachés | définitions et méthode | F09 § 2 et 3.3 | notion de cours |
| Indicateur à cinq champs, axes du tableau de bord | méthode | F08 § 3 ; F09 § 4 | notion de cours |

---

### 2.4 – Les attestations de logement et la chaîne de blocs (2,5 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.a` « Évaluer les opportunités, les risques et le cadre réglementaire […] » ; `3.3.d` « Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO ». Limites : aucun développement de chaîne de blocs ni de contrat intelligent ; effets énergétiques intégrés ; aucune analyse juridique.

**Annexes mobilisées** : annexe 2.5 (constats, proposition d'ANCRALYS, alternative de la direction des systèmes d'information) ; annexe 2.6 (MiCA, ISO 22739, eIDAS, RGPD) ; annexe 1.1 (un quart de résidents venus de l'étranger).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fonctionnement d'une chaîne de blocs publique : registre répliqué entre nœuds, blocs chaînés par empreintes, consensus (preuve d'enjeu), ouverte à tous, inaltérabilité pratique ; distincte d'une base distribuée | 0,5 |
| a-2 | Empreinte d'un document : preuve d'existence à une date et d'intégrité, ni de l'auteur ni de la véracité ; proposition classée dans la certification de documents | 0,5 |
| b-1 | Deux apports et deux limites de la proposition face au cachet électronique, appliqués aux constats | 0,5 |
| b-2 | Recommandation justifiée (critères de pertinence d'une chaîne de blocs), refus de l'option nominative | 0,5 |
| c-1 | MiCA ne s'applique pas à ORVANELLE : ni émission, ni offre, ni détention, ni service sur crypto-actifs ; frais payés par le prestataire | 0,5 |

**Réponse attendue**

*2.4 a) – Chaîne de blocs publique, empreinte et typologie*

**Le fonctionnement** (0,5 pt) : une **chaîne de blocs** est un registre de transactions **répliqué** entre de nombreux **nœuds**, sans administrateur central. Les transactions sont regroupées en **blocs**, chacun contenant l'**empreinte** du bloc précédent : modifier un bloc passé changerait toutes les empreintes suivantes et serait rejeté par les autres nœuds (**inaltérabilité pratique**, et non absolue). Les nouveaux blocs sont validés selon une règle de **consensus** : ici, la **preuve d'enjeu**, où les validateurs sont choisis selon les crypto-actifs qu'ils immobilisent, bien moins consommatrice d'énergie que la preuve de travail. Une chaîne **publique** est ouverte à tous en lecture et en écriture ; chaque transaction est signée par la clé privée de son émetteur et donne lieu à des frais, payés en crypto-actifs. Elle organise la confiance entre des acteurs qui ne se connaissent pas ; ce n'est pas une base de données distribuée, administrée par un seul acteur qui peut en modifier le contenu (F11 § 1 ; vocabulaire de l'ISO 22739:2024).

**L'empreinte et la typologie** (0,5 pt) : l'**empreinte** (hachage) est une suite de taille fixe calculée à partir d'un document par une fonction à sens unique : la moindre modification du document change l'empreinte, et l'on ne peut pas reconstituer le document à partir d'elle. Inscrire l'empreinte dans une transaction prouve que le document existait à la date du bloc (**horodatage**) et qu'il n'a pas été modifié depuis (**intégrité**) ; le document lui-même n'est pas inscrit. Elle ne prouve ni l'auteur du document, ni la vérité de son contenu : une attestation erronée, une fois inscrite, est « certifiée » erronée (limite de l'« oracle »). La proposition d'ANCRALYS relève de la **certification de documents** (horodatage et preuve d'intégrité), et non de la traçabilité d'une filière, des jetons non fongibles ou de la finance décentralisée (F11 § 2.1).

*2.4 b) – La proposition d'ANCRALYS face au cachet électronique*

**Deux apports et deux limites** (0,5 pt), à choisir dans le tableau suivant. Apports possibles : détection d'un document modifié ou jamais émis ; preuve qui survit au prestataire ; aucune donnée personnelle si seule l'empreinte est inscrite. Limites possibles : émetteur non identifié ; retrait impossible ; vérification peu commode pour les destinataires ; option nominative contraire à la minimisation ; frais en crypto-actifs et énergie.

| Critère | Proposition d'ANCRALYS | Cachet électronique qualifié et page de vérification d'ORVANELLE |
|---|---|---|
| Falsifications | détecte un document modifié ou jamais émis (aucune empreinte inscrite) | détecte un document modifié ou jamais émis ; le cachet identifie l'émetteur |
| Identité de l'émetteur | la transaction est signée par ANCRALYS : la preuve dit qu'ANCRALYS a inscrit une empreinte, et l'organisme doit faire confiance à la page d'ANCRALYS, qu'un faussaire peut imiter par un faux code | le certificat qualifié atteste que le document émane d'ORVANELLE, personne morale ; la page de vérification est sur le site d'ORVANELLE |
| Attestation devenue fausse (départ anticipé) | impossible à retirer : l'inscription est définitive | la page indique que l'attestation n'est plus valable |
| Usage par les destinataires | déposer le PDF sur une page inconnue des banques et des consulats | tout lecteur de PDF courant affiche le cachet ; cadre de confiance européen (eIDAS) |
| Durée de la preuve | l'empreinte reste dans la chaîne même si ANCRALYS disparaît, mais la page de vérification disparaît avec elle | dépend du certificat et du service d'ORVANELLE, à maintenir |
| Données personnelles | sans risque si seule l'empreinte est inscrite ; l'option « nom et adresse en clair » est contraire à la minimisation et impossible à effacer | aucune donnée inscrite hors d'ORVANELLE |
| Coût et énergie | environ 90 k€ sur trois ans ; frais en crypto-actifs et énergie de la chaîne, faible en preuve d'enjeu mais non nulle | environ 70 k€ sur trois ans |

La cause première des falsifications n'est pas l'absence de chaîne de blocs : ce sont des documents produits à partir d'un modèle de traitement de texte, avec une signature scannée, faciles à imiter. Les deux solutions supposent de produire les documents automatiquement à partir du logiciel de gestion locative.

**Recommandation** (0,5 pt) : retenir le **cachet électronique qualifié**, avec la page de vérification d'ORVANELLE, et refuser la proposition d'ANCRALYS, et en tout cas son option nominative. Les critères de pertinence d'une chaîne de blocs ne sont pas réunis (F11 § 2.2) : un seul acteur, ORVANELLE, écrit les attestations, sans besoin d'un registre partagé entre des acteurs qui ne se font pas confiance ; un tiers de confiance reconnu existe (prestataire de services de confiance qualifié) ; il faut identifier l'émetteur et pouvoir retirer une attestation, ce que la chaîne ne fait pas. Le cachet répond aux 40 falsifications signalées et réduit les 1 500 demandes de confirmation et leurs deux jours de délai, puisque l'organisme vérifie seul. ORVANELLE informe les banques, les consulats et les établissements de la façon de vérifier, et ajoute au besoin un horodatage électronique qualifié.

*2.4 c) – MiCA et le projet*

**Non** (0,5 pt) : d'après l'annexe 2.6, MiCA encadre l'offre au public et l'admission à la négociation de crypto-actifs, l'émission de jetons qui visent une valeur stable et l'agrément des prestataires de services sur crypto-actifs (PSCA). Dans ce projet, ORVANELLE n'émet ni n'offre de crypto-actifs, n'en détient aucun et ne rend aucun service sur crypto-actifs : elle achète en euros un service d'horodatage. Les frais de transaction en crypto-actifs sont payés par ANCRALYS, pour son propre compte. Le règlement ne régit pas non plus la certification de documents, et l'ISO 22739 n'est qu'un vocabulaire. Si ORVANELLE achetait un jour elle-même des crypto-actifs pour payer ces frais, le prestataire qui les lui fournirait ou les conserverait devrait être un PSCA agréé : depuis le 02/07/2026, un ancien PSAN ne peut plus exercer sans agrément (annexe 2.6).

**Réponses tolérées**
- Proposition d'ANCRALYS retenue en complément du cachet (horodatage indépendant d'ORVANELLE), si l'identification de l'émetteur et le retrait des attestations sont assurés par le cachet et la page de vérification, et si l'option nominative est refusée.
- Proposition rattachée à l'« horodatage » ou à la « preuve d'antériorité », formes de la certification.
- Réponse à c) qui s'interroge sur la situation d'ANCRALYS au regard de MiCA, si la réponse pour ORVANELLE est donnée ; aucune analyse juridique n'est attendue.
- Signature électronique de la personne habilitée au lieu du cachet, si le candidat signale qu'elle engage une personne physique et non ORVANELLE.

**Erreurs fréquentes**
- *Chaîne de blocs confondue avec une base de données distribuée* (`ET-08`) — ou présentée comme inaltérable sans nuance.
- *Empreinte confondue avec le chiffrement ou avec le document* — croire que le document est stocké dans la chaîne, ou que l'empreinte prouve l'auteur et la vérité du contenu.
- *Opportunités sans risques* (`ET-19`) — chaîne de blocs recommandée parce qu'elle est « infalsifiable », sans examiner l'émetteur, le retrait, les destinataires et les données personnelles.
- *MiCA mal situé* (`ET-35`) — MiCA présenté comme applicable à toute utilisation d'une chaîne de blocs, ou comme un cadre de la certification de documents ; ISO 22739 présentée comme une norme d'exigences.
- *Analyse juridique hors attente* (`JUR-T07`) — valeur probante des documents développée comme un juriste.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2023/1114 (MiCA) | objet : offre au public, jetons visant une valeur stable, PSCA ; fin des anciens PSAN au 02/07/2026 | `mica` / F11 § 3.1 | applicable depuis le 30/12/2024 |
| ISO 22739:2024 | vocabulaire des chaînes de blocs et des registres distribués | `iso_22739_2024` / F11 § 3.4 | en vigueur (2e édition) |
| Règlement (UE) n° 910/2014 (eIDAS), révisé par le règlement (UE) 2024/1183 | services de confiance : cachet électronique, horodatage, registres électroniques | `eidas_910_2014`, `eidas2` / F06 § 5 ; F11 § 3.4 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | minimisation ; données inscrites dans une chaîne de blocs impossibles à effacer | `rgpd` / F11 § 2.3 ; F15 | applicable depuis le 25/05/2018 |
| Chaîne de blocs publique, consensus, empreinte, critères de pertinence, typologie des applications | définitions et méthode | F11 § 1 et 2 ; glossaire (hachage, cachet électronique) | notion de cours |
