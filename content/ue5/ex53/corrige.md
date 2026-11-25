# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 53 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance (§ 1 à 4, modèle conceptuel, cardinalités et règles de passage ; § 1 et 8.3, dictionnaire et qualité des données ; § 8.4, cycle de vie et archivage), F08 décisionnel et visualisation (§ 1, chaîne décisionnelle ; § 2, méthodes d'analyse ; § 5, représentations et biais), F06 gestion des connaissances et documentaire (§ 4 et 5, cycle de vie documentaire, archivage électronique), F11 chaîne de blocs (§ 1 et 2, principes, usages, grille d'opportunité et limites), F15 RGPD opérationnel (§ 2, registre des activités de traitement), glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle logique exécuté, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Les données des interventions, des engins et des équipages | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 3,5 |
| 2.2 L'analyse de la sollicitation opérationnelle | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model | 4,5 |
| 2.3 La conservation des enregistrements et des comptes rendus de secours | `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `2.3.e` Aspects réglementaires (RGPD, archivage légal) et monétisation des données | 3 |
| 2.4 La proposition de PROTÉVANCE | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain | 2 |
| **Dossier 2 – Organiser et exploiter les données des interventions, en maîtriser la conservation** |  | **13** |

Répartition indicative : connaissances (modèle conceptuel, règles de passage, dictionnaire et dimensions de la qualité, chaîne de valeur et chaîne de traitement, analyse prédictive, cycle de vie, stockage et archivage électronique, principes du RGPD, chaîne de blocs de consortium) environ 2,25 points (la moitié des items 2.1 a-4, 2.1 b-1, 2.2 a-1, 2.2 c-1, 2.3 a-1, 2.3 b-1, 2.3 b-2, 2.4 a-1 et 2.4 a-2, qui mêlent définition et application) ; analyse des annexes et recommandations environ 10,75 points, soit environ 83 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Les données des interventions, des engins et des équipages (3,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) », modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites, avec une association ternaire ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données » ; `2.1.a` « Structurer et organiser les données […] afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité […] ». Aucune requête ; modèle physique seulement nommé.

**Annexes mobilisées** : annexe 2.1 (fonctionnement actuel, problèmes de qualité de 2026, règles de gestion RG1 à RG8) ; annexe 1.1 (logiciel de traitement de l'alerte, application de comptes rendus sur tablettes, 60 centres, 420 engins, 50 000 interventions).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Six entités, avec leur identifiant et des attributs élémentaires tirés de RG1 à RG8 ; nature et commune traitées en entités (listes de référence), et non en texte libre | 0,5 |
| a-2 | Associations binaires et leurs cardinalités, justifiées par les règles de gestion et lues dans les deux sens (classer, situer, desservir, appartenir, mobiliser avec ses deux heures, rattacher) | 0,5 |
| a-3 | Association ternaire « armer » entre l'agent, l'engin et l'intervention, porteuse du rôle, avec ses cardinalités (une intervention au moins un armement) | 0,5 |
| a-4 | Règles de passage énoncées ; modèle logique de neuf tables, clés primaires, clés étrangères (#) et trois tables d'association à clé composée | 0,5 |
| b-1 | Dictionnaire des données défini et appliqué ; trois entrées complètes (définition, format, règle de validité, source, propriétaire) | 0,5 |
| b-2 | Deux règles de qualité, chacune rattachée à un problème de l'annexe 2.1 B et à une dimension de la qualité | 0,5 |
| b-3 | Troisième règle de qualité, rattachée à un problème de l'annexe 2.1 B, et sa dimension (la correction à la source, le responsable désigné et le référentiel des communes partagé avec les partenaires sont valorisés, sans être exigés) | 0,5 |

**Réponse attendue**

*2.1 a) – Le modèle conceptuel et le modèle logique*

**Le modèle conceptuel** (0,5 pt pour les entités, 0,5 pt pour les associations binaires, 0,5 pt pour l'association ternaire) représente les objets de gestion (entités), leurs propriétés et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique (F07 § 1 et 2). Les identifiants sont soulignés.

Entités et attributs :
- **Intervention** (<u>num_intervention</u>, date_appel, heure_appel, adresse) (RG1) ;
- **Nature** (<u>code_nature</u>, libelle_nature) (RG2) ;
- **Commune** (<u>code_commune</u>, nom_commune, population) (RG3) ;
- **Centre** (<u>code_centre</u>, nom_centre, type_centre, groupement_territorial) (RG4) ;
- **Engin** (<u>num_engin</u>, type_engin, date_mise_service) (RG5) ;
- **Agent** (<u>matricule</u>, nom_agent, prenom_agent, statut_agent) (RG7).

La nature et la commune sont des **entités**, et non de simples attributs de l'intervention : ce sont des listes de référence, avec un code et un libellé, qui imposent une valeur parmi des valeurs connues ; c'est la réponse aux 2 500 natures « autre » et aux 1 100 libellés de communes de l'annexe 2.1 B. La commune porte en outre ses propres propriétés (population) et un lien vers son centre de premier appel.

| Association | Entités et cardinalités | Lecture (règle de gestion) |
|---|---|---|
| classer | Intervention **1,1** — Nature **0,n** | une intervention relève d'une seule nature ; une nature peut ne compter aucune intervention (RG2) |
| situer | Intervention **1,1** — Commune **0,n** | une intervention a lieu dans une seule commune ; une commune peut n'avoir connu aucune intervention (RG3) |
| desservir | Commune **1,1** — Centre **1,n** | une commune relève d'un seul centre de premier appel ; un centre est le centre de premier appel d'au moins une commune (RG4) |
| appartenir | Engin **1,1** — Centre **1,n** | un engin appartient à un seul centre ; un centre possède au moins un engin (RG5) |
| mobiliser (heure_depart, heure_arrivee) | Intervention **1,n** — Engin **0,n** | une intervention mobilise au moins un engin ; un engin peut n'avoir été engagé sur aucune intervention ; les deux heures dépendent du couple intervention-engin (RG6) |
| rattacher | Agent **1,n** — Centre **1,n** | un agent est rattaché à au moins un centre ; un centre compte au moins un agent (RG7) |
| armer (role) | Agent **0,n** — Engin **0,n** — Intervention **1,n** | sur une intervention, un agent arme un engin dans un seul rôle ; une intervention compte au moins un armement ; un agent ou un engin peut n'en avoir aucun (RG8) |

L'association **armer** est **ternaire** : le rôle ne dépend pas du seul couple agent-intervention, car sur une même intervention un agent peut armer successivement deux engins, dans des rôles différents (RG8) ; il ne dépend pas non plus du seul couple agent-engin, car un agent qui arme le même engin sur deux interventions peut y être conducteur puis chef d'agrès ; il dépend du triplet agent-engin-intervention. Un même agent n'a qu'un rôle sur un engin donné d'une intervention donnée. Les heures de départ et d'arrivée sont, elles, des attributs de l'association binaire **mobiliser** : elles dépendent de l'engin et de l'intervention, pas de l'agent. Le modèle n'exprime pas, par ses seules clés, qu'un agent n'arme qu'un engin effectivement engagé sur l'intervention : c'est une contrainte d'inclusion (armer ⊂ mobiliser) à contrôler par une règle applicative (valorisé, non exigé).

**Le modèle logique** (0,5 pt) s'obtient par les règles de passage (F07 § 4) :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire et dont les attributs deviennent des colonnes ;
2. pour une association binaire dont une patte a une cardinalité maximale 1 (classer, situer, desservir, appartenir), l'identifiant de l'entité du côté n migre comme clé étrangère dans la table de l'entité du côté 1, toujours renseignée si la cardinalité est 1,1 ;
3. une association dont toutes les pattes ont une cardinalité maximale n (mobiliser, rattacher), et toute association ternaire (armer), devient une table dont la clé primaire est composée des identifiants des entités reliées, chacun clé étrangère ; les attributs de l'association en deviennent des colonnes.

- Nature (<u>code_nature</u>, libelle_nature)
- Centre (<u>code_centre</u>, nom_centre, type_centre, groupement_territorial)
- Commune (<u>code_commune</u>, nom_commune, population, #code_centre)
- Engin (<u>num_engin</u>, type_engin, date_mise_service, #code_centre)
- Agent (<u>matricule</u>, nom_agent, prenom_agent, statut_agent)
- Intervention (<u>num_intervention</u>, date_appel, heure_appel, adresse, #code_nature, #code_commune)
- Engagement (<u>#num_intervention, #num_engin</u>, heure_depart, heure_arrivee)
- Rattachement (<u>#matricule, #code_centre</u>)
- Armement (<u>#matricule, #num_engin, #num_intervention</u>, role)

Dans Commune, `#code_centre` désigne le centre de premier appel ; dans Engin, le centre d'appartenance : ce sont deux associations différentes vers la même table. Le modèle physique (types, index sur les clés étrangères, liste fermée des rôles) se déduirait du modèle logique ; il n'est pas demandé. Les noms et prénoms des agents sont des données personnelles : le modèle s'en tient à ce qui sert à l'activité opérationnelle (minimisation).

*2.1 b) – Le dictionnaire des données et les règles de qualité*

**Le dictionnaire des données** (0,5 pt avec les trois entrées) est le référentiel qui décrit chaque donnée : nom, définition, type et format, domaine de valeurs ou règle de validité, source, propriétaire, sensibilité (F07 § 1). Il donne à tous, au centre de traitement de l'alerte, dans les centres et à l'observatoire, le même sens d'une donnée : c'est lui qui dira ce qu'est l'« heure d'arrivée » ou une « nature ». Trois entrées parmi les suivantes :

| Donnée | Définition | Type et format | Règle de validité | Source | Propriétaire |
|---|---|---|---|---|---|
| heure_arrivee | heure à laquelle l'engin arrive sur les lieux de l'intervention | date et heure, jj/mm/aaaa hh:mm | obligatoire pour clôturer l'engagement ; postérieure à l'heure de départ ; toute saisie après coup est tracée (auteur, date) | tablette de l'engin (bouton du chef d'agrès) | groupement des opérations |
| code_nature | nature de l'intervention | code de la table Nature (quatre valeurs) | valeur de la liste ; une nature provisoire choisie à l'appel est confirmée ou corrigée à la clôture ; tout changement de liste est daté | logiciel de traitement de l'alerte (opérateur), confirmée par le chef d'agrès | groupement des opérations |
| code_commune | commune du lieu de l'intervention | code de la table Commune (480 communes) | valeur du référentiel des communes ; aucune saisie libre | localisation du logiciel, ou choix dans la liste | observatoire de l'activité |
| role | rôle de l'agent sur l'engin pour l'intervention | liste : chef d'agrès, conducteur, équipier | un seul chef d'agrès et un seul conducteur par engin et par intervention | équipage enregistré au départ, corrigé dans le logiciel | groupement des opérations |

**Trois règles de qualité** (0,5 pt pour deux règles, 0,5 pt pour la troisième), chacune rattachée à un problème de l'annexe 2.1 B et à une dimension de la qualité des données (F07 § 8.3) :

1. **Contre les heures d'arrivée manquantes – complétude.** La tablette ne permet pas de clôturer l'engagement sans heure d'arrivée ; si le chef d'agrès a oublié le bouton, il la saisit à la clôture, et la saisie est marquée « déclarée après coup ». Un départ sur dix (7 000) n'a aujourd'hui pas d'heure d'arrivée : ce sont autant de données manquantes pour mesurer le délai d'arrivée, premier objectif du projet d'établissement.
2. **Contre les natures « autre » – exactitude.** La nature « autre » disparaît de la liste : l'opérateur choisit une nature provisoire, que le chef d'agrès confirme ou corrige à la clôture, d'après le compte rendu ; la correction est tracée. Les 15 jours de reclassement à la main de janvier deviennent inutiles, et une intervention sur vingt n'est plus classée au jugé.
3. **Contre les équipages incomplets – exactitude et cohérence.** Un remplacement au dernier moment est corrigé dans le logiciel de traitement de l'alerte, avant ou juste après le départ, par le chef d'agrès ou le centre, et non dans un tableur ; il n'existe qu'une source de l'équipage. Les 3 500 départs, un sur vingt, ressaisis aujourd'hui dans des tableurs de centre, sont autant de versions divergentes de la même donnée.
4. **Contre les communes mal orthographiées – unicité et cohérence.** La commune est choisie dans le référentiel des 480 communes (table Commune, identifiée par un code), jamais saisie en texte libre ; les 1 100 libellés actuels sont rapprochés une fois de ce référentiel, avec une table de correspondance conservée. Le même code de commune, partagé avec le département et les communes, rend les données échangeables avec eux (interopérabilité sémantique), comme le veut le projet d'établissement.

**Conclusion** : ces règles corrigent les données **à la source**, au moment où elles naissent (alerte, tablette, départ), plutôt qu'à chaque extraction mensuelle de l'observatoire ; elles supposent un propriétaire désigné pour chaque donnée (groupement des opérations, observatoire) et des listes de référence uniques.

**Réponses tolérées**
- Rôle traité en entité (Role, avec un code et un libellé) : l'association armer relie alors quatre entités, ou le rôle devient une clé étrangère de la table Armement, si le candidat le justifie par la liste fermée des rôles.
- Armement modélisé comme une association entre l'agent et l'engagement (association mobiliser traitée en entité, ou agrégation), si la clé reste agent-engin-intervention et le rôle porté par elle ; cette solution exprime d'ailleurs mieux la contrainte d'inclusion.
- Groupement territorial traité en entité reliée au centre ; attributs supplémentaires plausibles (dates de rattachement, coordonnées du lieu, immatriculation de l'engin).
- Cardinalité 0,n du centre dans desservir ou appartenir, si le candidat suppose un centre sans commune de premier appel ou sans engin propre, et le dit.
- Représentation graphique en notation Merise ou en « pattes de corbeau », si elle est lisible (`JUR-T10`).
- Autres entrées du dictionnaire (num_intervention, heure_depart, population), si elles portent les mêmes rubriques ; trois règles parmi les quatre, ou une autre dimension justifiée (actualité pour les équipages).

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dans le modèle conceptuel, ou clé étrangère placée du mauvais côté (#num_engin dans Centre).
- *Association ternaire décomposée en deux binaires* — agent-engin et agent-intervention séparées : on ne sait plus quel agent a armé quel engin sur quelle intervention, ni dans quel rôle.
- *Heures de départ et d'arrivée placées dans Intervention ou dans Engin* — elles dépendent du couple intervention-engin (RG6).
- *Morceau de cours* (`JUR-T01`) — définition du dictionnaire ou des dimensions de la qualité sans les problèmes chiffrés de l'annexe 2.1 B ; règles « vérifier la qualité » sans contrôle précis.
- *Requêtes écrites* (`JUR-T07`) — la question n'en demande aucune.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, cardinalités, association ternaire, règles de passage, modèle logique | définitions et méthode | F07 § 1 à 4 | notion de cours |
| Dictionnaire des données ; dimensions de la qualité (complétude, exactitude, unicité, cohérence, actualité) | définitions | F07 § 1 et 8.3 ; F08 § 4 | notion de cours |
| Interopérabilité sémantique (référentiel commun) | principe | F07 § 7 | notion de cours |

---

### 2.2 – L'analyse de la sollicitation opérationnelle (4,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique […] » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ». Limites : aucun calcul statistique, aucun développement d'algorithme ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexe 2.2 (interventions par nature et par an, séries complémentaires, reclassement de 2024, interface défaillante de 2025, touristes, épisodes de chaleur, affirmation de M. PRUNEVAUX) ; annexe 2.1 (extraction mensuelle dans un tableur, problèmes de qualité) ; annexe 1.1 (640 000 habitants, projet d'établissement).

**Barème indicatif (4,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de valeur des données définie ; collecte et nettoyage, chacune avec une limite de l'annexe 2.2 ou un problème de qualité de l'annexe 2.1 B (interface défaillante de 2025 ; natures « autre », communes) | 0,5 |
| a-2 | Structuration et analyse, chacune avec une limite (reclassement de 2024 ; touristes, séries qui se recoupent) | 0,5 |
| a-3 | Restitution et décision, avec une limite (ruptures non signalées) ; conclusion | 0,5 |
| b-1 | Deux constats argumentés et chiffrés, avec leur portée | 0,5 |
| b-2 | Troisième constat argumenté et chiffré | 0,5 |
| b-3 | Affirmation appréciée : part réelle du vieillissement (environ un tiers de la hausse) ; carences, reclassement, nuit, saisonnalité ; corrélation et causalité ; conclusion sur le recrutement | 0,5 |
| c-1 | Analyse prédictive définie et distinguée de la descriptive ; apport au SDIS (pics de l'été et des épisodes de chaleur, gardes) | 0,5 |
| c-2 | Deux conditions de réussite et deux limites, appliquées au cas | 0,5 |
| c-3 | Carte des communes en taux pour 1 000 habitants, justifiée (comparaison de communes de tailles différentes) ; précautions (touristes, petites communes) | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de valeur des données et la chaîne de traitement de la sollicitation*

**La chaîne de valeur des données** (0,5 pt avec la collecte et le nettoyage) est l'ensemble des étapes par lesquelles une donnée brute devient une information utile, puis une décision et une action : collecte, nettoyage, structuration et stockage, analyse, restitution, décision (F08 § 1). La valeur ne se crée qu'au bout de la chaîne, mais elle se perd à chaque étape mal tenue : une erreur de collecte n'est pas rattrapée par l'analyse. La chaîne de traitement en est le cœur technique et organisationnel. Pour la sollicitation opérationnelle :

| Étape | Ce que fera la chaîne | Limite traitée (annexe 2.2) |
|---|---|---|
| **Collecte** | extraction des interventions du logiciel de traitement de l'alerte, avec la nature, la commune, les heures ; âge de la victime tiré des comptes rendus ; population résidente et fréquentation touristique, données externes ; contrôle d'exhaustivité (chaque numéro d'intervention du logiciel est retrouvé dans la base) | l'interface défaillante de mars et avril 2025 a fait perdre environ 1 000 interventions sans que personne ne s'en aperçoive ; elles existent dans le logiciel et doivent être rechargées |
| **Nettoyage** | application des règles de la question 2.1 : natures « autre » corrigées, communes rapprochées du référentiel, heures manquantes marquées ; journal des rejets | une intervention sur vingt classée « autre » et 1 100 libellés de communes faussent la répartition par nature et par commune |
| **Structuration** | chargement dans une base historisée, alimentée automatiquement et non plus par un tableur ; table de correspondance des natures qui recalcule 2022 et 2023 selon la liste de 2024 ; définitions écrites (carence, nuit de 18 heures à 8 heures, âge) | le reclassement de 2024 (environ 2 000 relevages par an) rend 2022 et 2023 incomparables avec les années suivantes |
| **Analyse** | comparaisons à nomenclature constante, par saison, par tranche horaire, par commune ; taux rapportés à la population présente l'été ; séries croisées sans les additionner | jusqu'à 100 000 touristes en juillet et août ne sont pas dans les 640 000 habitants ; carences et personnes âgées se recoupent |
| **Restitution et décision** | tableaux et graphiques pour la direction et le conseil d'administration, annotés des ruptures (2024, 2025) et accompagnés d'une note de méthode ; décisions sur les gardes et les partenariats | des chiffres publiés sans ces annotations font croire à une hausse du secours d'urgence aux personnes de 8 000 interventions, au lieu de 6 000 |

**Conclusion** (0,5 pt avec la restitution) : les limites de l'annexe 2.2 ne sont pas des erreurs de calcul, mais des ruptures non documentées (reclassement, interface, population de référence). La chaîne les traite en amont, par des contrôles et des règles écrites, plutôt que par des corrections à la main dans le tableur de l'observatoire ; c'est la condition pour que le conseil d'administration décide sur des chiffres fiables.

*2.2 b) – Trois constats et l'affirmation de M. PRUNEVAUX*

**Trois constats** parmi les suivants (0,5 pt pour deux constats, 0,5 pt pour le troisième : le fait chiffré, son interprétation et sa portée) :
1. **Une hausse réelle, portée par les secours d'urgence aux personnes.** Les interventions passent de 43 000 à 50 000 en quatre ans (+ 7 000, environ + 16 %). À nomenclature constante, le secours d'urgence aux personnes passe de 33 000 à 39 000 (+ 6 000, environ + 18 %), et non de 31 000 à 39 000 : 2 000 de la hausse apparente viennent du reclassement de 2024. Les autres natures sont presque stables (de 10 000 à 11 000 à nomenclature constante).
2. **Les carences ont doublé.** De 3 000 à 6 000, elles expliquent à elles seules la moitié de la hausse réelle du secours d'urgence aux personnes et en représentent environ 15 % en 2026. Ce sont des interventions sans caractère d'urgence, faites faute d'autre moyen : une partie de la hausse ne relève pas de l'urgence.
3. **Les personnes âgées pèsent davantage.** Les interventions pour des personnes de 80 ans et plus à domicile passent de 10 000 à 12 500 (+ 2 500, environ + 25 %), plus vite que l'ensemble ; une partie de ces interventions sont aussi des carences.
4. **La sollicitation se déplace vers la nuit et vers l'été.** La part de nuit du secours d'urgence aux personnes passe de 40 % à 45 % ; l'écart entre les mois d'été et d'hiver passe de 900 à 1 200 interventions par mois, et les épisodes de chaleur de juillet 2026 ont porté l'activité à 1 500 interventions par semaine, contre 1 100 environ. Les pics, plus que la moyenne, dimensionnent les besoins.
5. **2025 est sous-estimée.** Environ 1 000 interventions manquent : 2025 compte en réalité environ 47 000 interventions, et la hausse de 2025 à 2026 est d'environ 3 000, et non de 4 000.

**L'affirmation de M. PRUNEVAUX** (0,5 pt) est en partie fondée, mais incomplète et sa conclusion ne suit pas :
- le vieillissement joue : + 2 500 interventions pour des personnes de 80 ans et plus, soit environ un tiers de la hausse de 7 000 ; il n'explique pas les deux autres tiers ;
- deux évolutions qui vont de pair ne prouvent pas que l'une cause l'autre : le vieillissement, les carences et la hausse des interventions évoluent ensemble, et les séries se recoupent (`ET-26`) ;
- les carences (+ 3 000) traduisent un manque d'autres moyens (ambulances privées, médecins de garde) : la réponse passe par la coordination avec le centre de régulation médicale du SAMU et le partage des données avec lui, objectif du projet d'établissement, plus que par de nouveaux volontaires ;
- une partie de la hausse **du secours d'urgence aux personnes** est artificielle : 2 000 relevages reclassés en 2024, sans effet sur le total ; et le saut de 2025 à 2026 (+ 4 000) est gonflé par une année 2025 sous-estimée d'environ 1 000 ; la hausse totale de 7 000 entre 2022 et 2026, elle, est réelle ;
- la pression se concentre la nuit et l'été (touristes, chaleur) : recruter des volontaires augmente les moyens, mais ne réduit pas la demande, et ne règle rien si ces moyens ne sont pas présents aux bonnes heures, aux bonnes saisons et dans les bonnes communes.

Conclusion : le recrutement peut faire partie de la réponse, mais le conseil d'administration doit d'abord disposer de chiffres à nomenclature constante, distinguer l'urgence des carences, et traiter celles-ci avec les partenaires.

*2.2 c) – L'analyse prédictive et la représentation par commune*

**L'analyse prédictive** (0,5 pt avec l'apport) estime ce qui va probablement se produire (combien d'interventions, où, quand), à partir de l'historique et de facteurs explicatifs (calendrier, météo, fréquentation touristique), avec une marge d'incertitude. Elle se distingue de l'analyse descriptive, qui dit ce qui s'est passé, et de l'analyse exploratoire, qui explore les données pour y repérer des profils, des motifs ou des anomalies (F08 § 2). Pour le SDIS, elle permettrait d'anticiper, semaine par semaine et par groupement territorial, les pics de l'été et des épisodes de chaleur (1 500 interventions par semaine en juillet 2026), d'adapter les gardes et le nombre d'agents d'astreinte aux heures de nuit et aux semaines chargées, de prépositionner des engins dans le Haut-Aurande l'été et de prévenir les partenaires.

**Deux conditions** parmi (0,5 pt avec les deux limites) : un historique fiable et homogène sur plusieurs années (règles de la question 2.1, nomenclature recalculée, 2025 complétée) ; des données externes obtenues des partenaires (prévisions météorologiques, fréquentation touristique) ; des compétences d'analyse à l'observatoire et une validation humaine des prévisions par le groupement des opérations, qui garde la décision ; des données agrégées, sans donnée personnelle des victimes.
**Deux limites** parmi : l'avenir ne reproduit pas forcément le passé (épisode exceptionnel, changement des pratiques des partenaires, `JUR-D06`) ; les petites communes comptent trop peu d'interventions pour une prévision fiable ; les biais des données passées (sous-enregistrement de 2025, natures « autre ») se retrouvent dans les prévisions ; une prévision donne un ordre de grandeur, pas une certitude, et ne dit pas pourquoi. Aucun développement d'algorithme n'est attendu.

**La représentation** (0,5 pt) : une **carte des 480 communes colorée selon le taux d'interventions pour 1 000 habitants** (carte choroplèthe), en quatre ou cinq classes, avec la légende, la source et l'année ; de préférence deux cartes à la même échelle, l'été et l'hiver. La carte montre la géographie de la sollicitation, que lit immédiatement un conseil composé d'élus des communes ; le taux permet de comparer des communes de tailles très différentes, alors qu'une carte en nombre d'interventions ne montrerait que Montcerneau et les grandes communes. Précautions : l'été, le taux calculé sur les seuls résidents surestime la sollicitation des communes touristiques du Haut-Aurande ; les petites communes, aux chiffres faibles, peuvent être regroupées. À éviter : un graphique en secteurs à 480 parts, un tableau de chiffres bruts.

**Réponses tolérées**
- Autres étapes de la chaîne (stockage distinct de la structuration, décision et action en étape propre), si chacune porte une limite de l'annexe 2.2.
- Autres constats tirés de l'annexe (incendies en hausse en 2026, accidents stables), s'ils sont chiffrés et interprétés.
- Appréciation de l'affirmation plus ou moins sévère, si elle s'appuie sur les chiffres de l'annexe et distingue la part du vieillissement du reste.
- Carte en symboles proportionnels complétée d'un taux, ou carte par groupement territorial assortie d'un tableau des communes les plus sollicitées, si le choix est justifié.
- Analyse prescriptive évoquée en complément (proposer le nombre d'agents de garde), si elle reste une aide à la décision humaine.

**Erreurs fréquentes**
- *Corrélation présentée comme causalité* (`ET-26`) — « la population vieillit, donc les interventions augmentent », sans mesurer la part du vieillissement.
- *Reclassement présenté comme une cause de la hausse totale* — il déplace 2 000 interventions des opérations diverses vers le secours d'urgence aux personnes, sans changer le total de 43 000 à 50 000.
- *Chiffres lus sans les ruptures* (`JUR-D06`) — hausse du secours d'urgence aux personnes de 8 000 prise telle quelle ; baisse des opérations diverses en 2024 interprétée comme une amélioration.
- *Chaîne réduite à un outil* (`ET-05`, `JUR-D01`) — « il suffit d'un logiciel de tableaux de bord », sans collecte, nettoyage ni structuration.
- *Calcul statistique ou algorithme* (`JUR-T07`) — coefficients, régressions ou modèle à programmer : hors attente.
- *Carte en valeurs absolues* — elle reflète la taille des communes, non leur sollicitation.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de valeur des données, chaîne décisionnelle (collecte, nettoyage, structuration, analyse, restitution) | définitions et méthode | F08 § 1 | notion de cours |
| Analyses descriptive, exploratoire, prédictive | définitions | F08 § 2 | notion de cours |
| Choix d'une représentation, carte en taux, biais, corrélation et causalité | méthode | F08 § 5 | notion de cours |

---

### 2.3 – La conservation des enregistrements et des comptes rendus de secours (3 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression », durées de conservation données par l'énoncé ; `2.3.e` « Aspects réglementaires (RGPD, archivage légal) […] », en principe, sans analyse juridique. Limites : ni prérogatives des personnes sur leurs données, ni fondement juridique des traitements (UE 1) ; aucune durée tirée d'un texte.

**Annexes mobilisées** : annexe 2.3 (enregistrements, comptes rendus, demandes de copies, enregistrement non retrouvé, durées fixées par le SDIS) ; annexe 2.5 (principes du RGPD, NF Z42-013 et ISO 14641, ISO 15489-1) ; annexe 1.1 (enregistreur des appels, application de comptes rendus, déléguée à la protection des données, médecin-chef).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cycle de vie des enregistrements, de la création à la destruction, une règle par étape (horodatage et lien avec l'intervention, accès, gel, destruction à deux ans) | 0,5 |
| a-2 | Cycle de vie des comptes rendus, une règle par étape (création structurée, usage courant deux ans, archivage jusqu'à vingt ans, destruction) | 0,5 |
| a-3 | Règles transversales appliquées au cas : demandes de copies centralisées et tracées, fin des copies en PDF et sur clés, rattrapage du stock existant | 0,5 |
| b-1 | Stockage et archivage électronique distingués et appliqués (serveur et enregistreur actuels : du stockage) | 0,5 |
| b-2 | Ce que le RGPD impose (limitation de la conservation, sécurité renforcée des données de santé, registre) et ce que les normes apportent (intégrité, pérennité, traçabilité, preuve), en principe | 0,5 |
| b-3 | Trois mesures précises, rattachées aux constats de l'annexe 2.3 | 0,5 |

**Réponse attendue**

*2.3 a) – Le cycle de vie des enregistrements et des comptes rendus*

Le cycle de vie d'une donnée va de sa **création** à sa **suppression**, en passant par le **stockage**, l'**usage** et l'**archivage** (F07 § 8.4) ; chaque étape a une règle, une durée et un responsable. Les durées sont celles que le SDIS a fixées le 15/03/2027 (annexe 2.3 D).

| Étape | Enregistrements des appels | Comptes rendus de secours |
|---|---|---|
| **Création** | enregistrement automatique de l'appel ; règle : horloge de l'enregistreur synchronisée sur une heure de référence, et numéro de l'intervention associé à l'enregistrement dès sa création (métadonnée) | rédaction sur la tablette, dans des champs structurés, rattachée au numéro de l'intervention ; règle : une fois validé, le compte rendu n'est plus modifié, toute correction crée une nouvelle version datée |
| **Stockage et usage courant** | conservation dans l'enregistreur pendant deux ans ; règle : écoute réservée aux personnes habilitées du centre de traitement de l'alerte, chaque écoute et chaque copie journalisées | consultation courante pendant deux ans, sur le serveur ; règle : accès réservé au service de santé et aux personnes habilitées, selon leur profil, journalisé ; aucune copie en PDF dans les messageries |
| **Gel en cas de demande** | si une demande portant sur l'intervention est en cours (justice, litige), l'enregistrement est copié, avec son empreinte, dans l'archive, et exclu de la destruction jusqu'à la fin de la procédure | même règle : le compte rendu demandé est gelé, et la copie remise est tracée |
| **Archivage** | sans objet, sauf enregistrement gelé | au-delà de deux ans, versement dans un système d'archivage électronique jusqu'à vingt ans après l'intervention ; règle : format pérenne, empreinte, journal des accès, consultation sur demande motivée seulement, validée par le médecin-chef |
| **Destruction** | à deux ans, destruction automatique, consignée dans un journal (quoi, quand, par qui), sauf gel | à vingt ans, destruction proposée automatiquement, validée par le médecin-chef, sous le contrôle de la déléguée à la protection des données, et consignée |

**Règles transversales** (0,5 pt) : les 400 demandes de copies de 2026 passent par un point d'entrée unique (une cellule rattachée à la direction, avec le centre de traitement de l'alerte et le médecin-chef), la déléguée à la protection des données étant consultée sur les règles et en contrôlant l'application ; elles sont inscrites dans un registre, avec un délai cible ; les copies sur clés USB et par messagerie cessent ; les 3 000 PDF trouvés dans dix messageries, et ceux des autres, sont supprimés. Le stock existant est remis en ordre une fois : les enregistrements de plus de deux ans, ceux de 2017 à 2024 environ, de l'ordre de 1,2 million, sont détruits, sauf ceux qui font l'objet d'une demande en cours ; les comptes rendus de plus de deux ans sont versés à l'archive. Avec ces règles, l'appel de novembre 2024 demandé en septembre 2026, encore dans le délai de deux ans, aurait été retrouvé par le numéro de l'intervention.

*2.3 b) – Stockage et archivage électronique, ce qu'imposent et apportent le RGPD et les normes, trois mesures*

**Stockage et archivage électronique** (0,5 pt) ne se confondent pas. Le **stockage** conserve des données sur un support pour leur usage courant : elles restent modifiables, se copient et se perdent, sans garantie dans la durée. L'**archivage électronique** conserve, pour une durée fixée, des documents qui ne sont plus d'usage courant, dans un système qui en garantit l'intégrité (aucune modification non tracée), la pérennité (lisibilité dans le temps, formats pérennes) et la traçabilité (journaux de toutes les opérations), et qui en organise le sort final (F06 § 4 et 5). Une sauvegarde, qui sert à restaurer un système, n'est pas un archivage. Au SDIS, l'enregistreur et le serveur des comptes rendus ne font que du **stockage** : 1,5 million d'enregistrements sans tri, un serveur occupé à 85 %, des copies partout et un enregistrement introuvable le jour où la justice le demande.

**Ce que le RGPD impose** (0,5 pt avec les normes ; en principe, annexe 2.5, sans analyse juridique) : les enregistrements, qui contiennent la voix et souvent l'identité des appelants, et les comptes rendus, qui contiennent des données de santé, sont des données personnelles ; ils ne peuvent être conservés que pendant une durée limitée, fixée selon la finalité : la conservation sans limite actuelle ne respecte pas ce principe, alors que le SDIS a désormais des durées. Le registre des activités de traitement doit les indiquer (F15 § 2). La minimisation proscrit les copies inutiles en PDF ; les données de santé appellent une protection renforcée (accès restreints, journalisés) ; la déléguée à la protection des données conseille et contrôle.
**Ce que les normes apportent** : NF Z42-013 et son équivalent international ISO 14641 sont des normes d'application volontaire, et non des obligations ; elles décrivent comment concevoir et exploiter un système d'archivage électronique qui garantit l'intégrité, la pérennité et la traçabilité, ce qui permet de produire, quinze ans après, un compte rendu qui puisse servir de preuve dans un litige. ISO 15489-1 donne le principe d'ensemble : des règles écrites pour chaque catégorie de documents, de la création au sort final.

**Trois mesures** parmi (0,5 pt) :
1. **Une politique de conservation écrite et appliquée** : les durées du 15/03/2027 sont inscrites au registre des activités de traitement, paramétrées dans l'enregistreur et sur le serveur (purge automatique et journalisée), avec la procédure de gel ; la déléguée à la protection des données en contrôle l'application chaque année.
2. **Un système d'archivage électronique conforme aux principes de NF Z42-013** pour les comptes rendus de plus de deux ans et les enregistrements gelés : formats pérennes, empreintes, journal des accès, accès réservé au service de santé.
3. **Un point d'entrée unique des demandes de copies** : registre des 400 demandes annuelles, copie tracée et remise par un canal sécurisé, fin des clés USB et des copies en messagerie, suppression des PDF existants.
4. **Des métadonnées qui rendent les données retrouvables** : numéro d'intervention associé à chaque enregistrement et à chaque compte rendu, horloges synchronisées sur une heure de référence, contrôle de l'horloge après chaque panne.
5. **Des habilitations par profil** : écoute des enregistrements réservée au centre de traitement de l'alerte, lecture des comptes rendus au service de santé, revue annuelle des droits.

**Réponses tolérées**
- Cycle en trois âges (courant, intermédiaire, définitif ou destruction) au lieu des cinq étapes du programme, s'il est appliqué aux deux catégories avec une règle par étape.
- Archivage intermédiaire des enregistrements entre six mois et deux ans, si la durée totale de deux ans est respectée.
- Responsable différent du point d'entrée des demandes (centre de traitement de l'alerte pour les enregistrements, médecin-chef pour les comptes rendus), si la demande est enregistrée et tracée. Valorisé : la déléguée à la protection des données conseille et contrôle sans traiter elle-même les demandes ni décider des destructions (indépendance, F15 § 1).
- Prestataire d'archivage externe évoqué, si le candidat garde les exigences d'intégrité, d'accès restreint et de réversibilité, sans développer l'hébergement.
- Trois mesures parmi les cinq, ou d'autres mesures précises et rattachées à l'annexe 2.3.

**Erreurs fréquentes**
- *Stockage et archivage confondus* — « le serveur archive les comptes rendus », ou sauvegarde présentée comme un archivage.
- *Durée tirée d'un texte de loi* (`JUR-T07`) — les durées sont celles fixées par le SDIS et données par l'annexe ; aucune n'est à citer ni à discuter.
- *Dérive juridique* (`JUR-T07`) — développements sur les prérogatives des familles ou des avocats, ou sur le fondement juridique des traitements (UE 1) : la question porte sur l'organisation de la conservation.
- *Norme présentée comme une obligation ou comme une solution* (`ET-01`) — norme d'archivage présentée comme imposée au SDIS, ou comme un produit à installer : elle est d'application volontaire et décrit des exigences, que l'outil choisi doit respecter.
- *Destruction sans gel* — détruire à deux ans un enregistrement qui fait l'objet d'une demande en cours.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cycle de vie des données (création, stockage, usage, archivage, suppression) | définition et méthode | F07 § 8.4 ; F06 § 4 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) : minimisation, limitation de la conservation, données de santé, registre des activités de traitement | principes donnés en annexe 2.5 | `rgpd` / F15 § 2 | applicable depuis le 25/05/2018 |
| NF Z42-013, archivage électronique | intégrité, pérennité, traçabilité, en principe | `nf_z42_013` / F06 § 5 | en vigueur, norme volontaire |
| ISO 14641, archivage électronique | équivalent international de NF Z42-013 | `iso_14641` / F06 § 5 | en vigueur |
| ISO 15489-1, gestion des documents d'activité (2016) | concepts et principes | `iso_15489_1` / F06 § 4 | en vigueur |

---

### 2.4 – La proposition de PROTÉVANCE (2 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ». Limites : aucun développement ; effets énergétiques intégrés à l'analyse ; aucun cryptoactif.

**Annexes mobilisées** : annexe 2.4 (suivi actuel des tenues, constats de l'inventaire, proposition de PROTÉVANCE, coûts, base de données partagée) ; annexe 2.5 (ISO 22739:2024, principes du RGPD) ; annexe 1.1 (logiciel de gestion du parc, effectif).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de blocs définie ; fonctionnement de la chaîne de consortium appliqué à la proposition (nœuds des cinq acteurs, événements signés, validation par les participants identifiés, blocs chaînés, inaltérabilité pratique) ; distinction avec une base de données distribuée | 0,5 |
| a-2 | Type d'application : traçabilité d'un bien physique dans une chaîne d'acteurs (preuve horodatée des événements), sans cryptoactif | 0,5 |
| b-1 | Valeur ajoutée (historique commun, lavages contestés, accident) et coûts comparés (150 k€ contre 90 k€ sur trois ans) ; limites (donnée d'entrée, gouvernance à cinq, nœuds hébergés par le fournisseur, matricule inscrit, énergie) | 0,5 |
| b-2 | Conclusion argumentée et conditions | 0,5 |

**Réponse attendue**

*2.4 a) – Le fonctionnement et le type d'application*

**La chaîne de blocs** (0,5 pt avec le fonctionnement) est un registre distribué : il est partagé et synchronisé entre plusieurs nœuds, les transactions y sont regroupées en blocs chaînés par des empreintes (chaque bloc contient l'empreinte du précédent), et un mécanisme de consensus valide chaque ajout ; une fois inscrite, une transaction est horodatée et pratiquement inaltérable (F11 § 1). Elle permet à des acteurs qui ne se font pas pleinement confiance de partager un même historique sans qu'aucun d'eux ne puisse le modifier seul. C'est ce qui la distingue d'une **base de données distribuée**, qui répartit les données d'un même gestionnaire, lequel peut les modifier (`ET-08`).

Dans la proposition de PROTÉVANCE, la chaîne est **de consortium** (permissionnée) : seuls cinq acteurs identifiés (les trois SDIS, PROTÉVANCE, LAVORDÈNE) disposent d'un nœud et d'une copie du registre. Quand le blanchisseur lit la puce d'une tenue lavée, il émet une transaction « lavage », signée par sa clé ; les participants autorisés la valident, sans minage, puis elle est ajoutée à un bloc et recopiée sur tous les nœuds. Chaque événement (livraison, attribution, lavage, contrôle, réparation, réforme) s'ajoute ainsi à l'historique de la tenue, que chaque acteur lit sans pouvoir le réécrire.

**Le type d'application** (0,5 pt) : il s'agit d'une application de **traçabilité** : suivre un bien physique, la tenue, tout au long de sa vie et entre plusieurs organisations, avec une preuve horodatée de chaque événement, proche de la certification d'événements (nombre de lavages, date du dernier contrôle). Ce n'est ni de la finance décentralisée, ni un jeton non fongible, ni un cryptoactif : aucune monnaie ni aucun jeton n'est émis.

*2.4 b) – Valeur ajoutée, coûts, limites et conclusion*

**Valeur ajoutée, coûts et limites** (0,5 pt) :
- **valeur ajoutée** : un historique commun et infalsifiable, que ni le fournisseur ni le blanchisseur ne peuvent retoucher ; il réglerait les contestations sur les lavages (30 000 facturés, 24 000 enregistrés), dirait sans délai qui portait quelle tenue et quand elle a été contrôlée (une semaine de recherche après l'accident de 2026), et suivrait le terme de dix ans ou de 50 lavages ; il serait commun aux trois SDIS. Mais l'essentiel du gain vient de la **puce**, qui supprime la saisie à la main, et non de la chaîne : la base partagée l'apporte aussi ;
- **coûts** : sur trois ans, la chaîne coûterait au SDIS 20 + 40 + 3 × 30 = 150 k€, la base partagée 20 + 40 + 3 × 10 = 90 k€, soit 60 k€ de plus pour la chaîne ;
- **limites** : la chaîne garantit que l'événement inscrit n'a pas été modifié, pas qu'il est vrai : une puce lue ne prouve pas que la tenue a été bien lavée (donnée d'entrée) ; la gouvernance à cinq reste à construire (admission des nœuds, évolution des règles, partage des coûts, sortie d'un acteur), alors que les deux SDIS voisins n'ont pas pris position ; si PROTÉVANCE héberge les nœuds des SDIS, la confiance redevient centrée sur le fournisseur, qui est aussi partie aux contestations, et le SDIS en dépend ; le matricule inscrit dans un registre inaltérable est une donnée personnelle qu'on ne pourra plus supprimer au terme de sa durée de conservation : il faut n'y inscrire qu'un identifiant de tenue et garder le lien avec l'agent dans le logiciel de gestion du parc ; la validation sans minage consomme peu, mais cinq copies du registre consomment davantage qu'une base unique ; il faut enfin relier la chaîne au logiciel de gestion du parc pour éviter une double saisie.

**Conclusion** (0,5 pt) : les acteurs sont peu nombreux, identifiés et liés par des contrats, et un tiers de confiance peut être désigné : le prestataire que retiendraient les trois SDIS, à condition que PROTÉVANCE et LAVORDÈNE l'acceptent aussi. Selon la grille d'opportunité (F11 § 2.2), une base de données partagée, avec un journal des modifications tenu par ce tiers, des droits d'écriture propres à chaque acteur et des exports réguliers, répond au besoin pour 60 k€ de moins sur trois ans. Il est recommandé d'équiper les tenues de puces et de retenir la base partagée, en prévoyant la récupération des données en fin de contrat ; la chaîne de blocs ne serait à réexaminer que si le consortium s'élargissait sans qu'un tiers soit accepté de tous, avec des nœuds tenus par chaque acteur et sans matricule inscrit.

**Réponses tolérées**
- Conclusion en faveur d'un essai limité de la chaîne de blocs, si le candidat pose des conditions précises (adhésion des deux SDIS voisins, nœud propre au SDIS, aucun matricule inscrit, comparaison au bout d'un an avec la base partagée).
- Consensus nommé « preuve d'autorité » ou « tolérance aux pannes byzantines », en principe, sans développement technique.
- Coût comparé par an (20 k€ de plus par an) plutôt que sur trois ans.
- Certification citée comme type d'application, si la traçabilité est reconnue comme l'usage principal.

**Erreurs fréquentes**
- *Chaîne de blocs confondue avec une base de données distribuée* (`ET-08`) — « une base partagée sur plusieurs serveurs ».
- *Opportunités sans limites* (`ET-19`) — chaîne présentée comme la solution aux oublis de saisie, alors qu'elle ne garantit pas la donnée d'entrée.
- *Oubli de l'énergie ou de la gouvernance* — le programme impose d'intégrer les effets énergétiques ; la gouvernance à cinq est la difficulté principale.
- *Cryptoactif ou jeton évoqué* (`JUR-T07`) — la proposition n'en comporte aucun.
- *Morceau de cours* (`JUR-T01`) — définition sans les chiffres de l'annexe 2.4 ni la comparaison avec la base partagée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Registre distribué, chaîne de blocs de consortium, consensus, distinction avec une base distribuée | définitions | F11 § 1 | notion de cours |
| Usages (traçabilité, certification), grille d'opportunité, limites (donnée d'entrée, gouvernance, énergie, données personnelles) | méthode | F11 § 2 | notion de cours |
| ISO 22739:2024, vocabulaire des chaînes de blocs et des registres distribués | terminologie, donnée en annexe 2.5 | `iso_22739_2024` / F11 § 3.4 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) : minimisation, limitation de la conservation | principe donné en annexe 2.5 | `rgpd` / F15 | applicable depuis le 25/05/2018 |
