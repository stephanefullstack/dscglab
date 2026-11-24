# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 50 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance (§ 2 à 4, modèle conceptuel, cardinalités et règles de passage ; § 1 et 8.3, dictionnaire et qualité des données ; § 8.1 et 8.2, rôles et DAMA-DMBOK ; § 8.4, cycle de vie ; § 8.6, valeur des données), F08 décisionnel et visualisation (§ 1, chaîne de traitement ; § 2, méthodes d'analyse ; § 3, tableau de bord et indicateurs ; § 5, représentations et biais), F09 performance du SI (§ 4.1, tableau de bord et axes ; § 4.3, revue et amélioration continue), F15 RGPD opérationnel, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle logique exécuté, indicateurs, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Les données des cartes d'acheteur et des passages au péage | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 3,5 |
| 2.2 L'analyse de la fréquentation des acheteurs | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model | 3,5 |
| 2.3 La gouvernance des données des flux alimentaires | `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ; `2.3.a` Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques ; `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `2.3.f` Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques | 3,5 |
| 2.4 Le tableau de bord du conseil d'administration | `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ; `3.1.e` Revue et amélioration continue des dispositifs de pilotage | 2,5 |
| **Dossier 2 – Organiser et exploiter les données des acheteurs et des flux, revoir le pilotage** |  | **13** |

Répartition indicative : connaissances (modèle conceptuel, règles de passage, dictionnaire et dimensions de la qualité, chaîne de traitement, analyses descriptive et exploratoire, gouvernance des données et DAMA-DMBOK, cycle de vie, donnée comme actif, tableau de bord et indicateur à cinq champs) environ 2 points (la moitié des items 2.1 a-3, 2.1 b-1, 2.2 a-1, 2.2 c-1, 2.3 a-1, 2.3 c-1, 2.4 a-1 et 2.4 b-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 11 points, soit environ 85 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Les données des cartes d'acheteur et des passages au péage (3,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) », modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données » ; `2.1.a` « Structurer et organiser les données […] afin d'en garantir la cohérence, la qualité […] ». Aucune requête ; modèle physique seulement nommé.

**Annexes mobilisées** : annexe 2.1 (fonctionnement actuel, problèmes de qualité, règles de gestion RG1 à RG6) ; annexe 1.1 (système de péage, application des acheteurs, 9 000 cartes actives) ; annexe 2.5 (principes du RGPD, qualité des données).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Six entités, avec leur identifiant et des attributs élémentaires tirés de RG1 à RG6 ; catégorie et type d'abonnement traités en entités ; véhicule, unique par carte, en attribut de la carte | 0,5 |
| a-2 | Cinq associations et leurs cardinalités, justifiées par les règles de gestion et lues dans les deux sens (une carte peut n'avoir aucun passage ; une entreprise détient au moins une carte) | 0,5 |
| a-3 | Règles de passage énoncées ; modèle logique de six tables, clés primaires et clés étrangères (#) ; tarif appliqué conservé dans le passage | 0,5 |
| b-1 | Dictionnaire des données défini ; deux entrées complètes (définition, format, règle de validité, source, propriétaire) | 0,5 |
| b-2 | Deux autres entrées complètes (une donnée personnelle signalée comme telle est valorisée, sans être exigée) | 0,5 |
| b-3 | Deux règles de qualité, chacune rattachée à un problème de l'annexe 2.1 B et à une dimension de la qualité | 0,5 |
| b-4 | Troisième règle de qualité, rattachée à un problème de l'annexe 2.1 B, et sa dimension (la correction à la source et le responsable désigné sont valorisés, sans être exigés) | 0,5 |

**Réponse attendue**

*2.1 a) – Le modèle conceptuel et le modèle logique*

**Le modèle conceptuel** (0,5 pt pour les entités, 0,5 pt pour les associations) représente les objets de gestion (entités), leurs propriétés et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique (F07 § 1 et 2). Les identifiants sont soulignés.

Entités et attributs :
- **Categorie** (<u>code_categorie</u>, libelle_categorie) (RG2) ;
- **Entreprise_acheteuse** (<u>num_entreprise</u>, raison_sociale, siren, commune, date_fermeture) (RG1) ;
- **Carte** (<u>num_carte</u>, nom_titulaire, prenom_titulaire, immatriculation, date_emission, date_fin_validite, statut_carte) (RG3) ;
- **Type_abonnement** (<u>code_type</u>, libelle_type, tarif_en_vigueur) (RG4) ;
- **Borne** (<u>num_borne</u>, entree, date_mise_service) (RG5) ;
- **Passage** (<u>num_passage</u>, date_passage, heure_passage, tarif_applique) (RG6).

Deux choix sont à justifier. La catégorie et le type d'abonnement sont des **entités**, et non de simples attributs : ce sont des listes de référence, avec un code et un libellé, qui imposent une valeur parmi des valeurs connues ; c'est aussi la réponse à la saisie en texte libre des catégories (annexe 2.1 B). Le **véhicule** n'est pas une entité : un seul véhicule est enregistré par carte (RG3) et on ne connaît que son immatriculation ; une entité Véhicule reliée à la carte par des cardinalités 1,1 des deux côtés serait à fusionner avec elle (F07 § 2, point 6).

| Association | Entités et cardinalités | Lecture (règle de gestion) |
|---|---|---|
| appartenir | Entreprise_acheteuse **1,1** — Categorie **0,n** | une entreprise appartient à une seule catégorie ; une catégorie peut ne compter aucune entreprise (RG2) |
| detenir | Carte **1,1** — Entreprise_acheteuse **1,n** | une carte appartient à une seule entreprise ; une entreprise détient au moins une carte (RG3) |
| relever | Carte **1,1** — Type_abonnement **0,n** | une carte relève d'un seul type d'abonnement ; un type peut n'avoir aucune carte (RG4) |
| rattacher | Passage **1,1** — Carte **0,n** | un passage est rattaché à une seule carte ; une carte peut n'avoir encore aucun passage (RG6) |
| enregistrer | Passage **1,1** — Borne **0,n** | un passage est enregistré par une seule borne ; une borne enregistre zéro, un ou plusieurs passages (RG6) |

Toutes les associations ont une patte de cardinalité maximale 1 : le modèle n'a pas d'association « plusieurs à plusieurs ». La catégorie d'un passage payé à la borne n'est pas modélisée : RG6 exige un passage rattaché à une carte, et la règle de qualité de la question b) traite ces passages.

**Le modèle logique** (0,5 pt) s'obtient par les règles de passage (F07 § 4) :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire et dont les attributs deviennent des colonnes ;
2. pour chaque association dont une patte a une cardinalité maximale 1, l'identifiant de l'entité du côté n migre comme clé étrangère dans la table de l'entité du côté 1 ; une cardinalité 1,1 impose une clé étrangère toujours renseignée.

- Categorie (<u>code_categorie</u>, libelle_categorie)
- Entreprise_acheteuse (<u>num_entreprise</u>, raison_sociale, siren, commune, date_fermeture, #code_categorie)
- Type_abonnement (<u>code_type</u>, libelle_type, tarif_en_vigueur)
- Carte (<u>num_carte</u>, nom_titulaire, prenom_titulaire, immatriculation, date_emission, date_fin_validite, statut_carte, #num_entreprise, #code_type)
- Borne (<u>num_borne</u>, entree, date_mise_service)
- Passage (<u>num_passage</u>, date_passage, heure_passage, tarif_applique, #num_carte, #num_borne)

Le **tarif appliqué** est stocké dans le passage, alors qu'il semble se déduire du type d'abonnement : c'est voulu. Le tarif en vigueur change au 1er janvier (RG4) ; s'il n'était lu que dans Type_abonnement, les passages de 2026 seraient relus au tarif de 2027. Le modèle physique (types, index sur les clés étrangères, contraintes d'unicité du SIREN) se déduirait du modèle logique ; il n'est pas demandé.

Les données des titulaires (nom, prénom, immatriculation, heures de passage) sont des données personnelles : le modèle s'en tient à celles qui servent à la carte et au contrôle d'accès, conformément au principe de minimisation (annexe 2.5).

*2.1 b) – Le dictionnaire des données et les règles de qualité*

**Le dictionnaire des données** (0,5 pt avec deux entrées) est le référentiel qui décrit chaque donnée : nom, définition, type et format, domaine de valeurs ou règle de validité, source, propriétaire, sensibilité (F07 § 1). Il donne à tous le même sens d'une donnée : à BRÉVALIM, c'est lui qui dira ce qu'est une « entreprise active » ou un « restaurant ». Quatre entrées parmi les suivantes (0,5 pt pour deux entrées complètes) :

| Donnée | Définition | Type et format | Règle de validité | Source | Propriétaire |
|---|---|---|---|---|---|
| siren | numéro SIREN de l'entreprise acheteuse | texte, neuf chiffres | obligatoire ; unique dans Entreprise_acheteuse ; vérifié auprès du répertoire officiel des entreprises à la création | saisie à l'accueil du péage, sur justificatif | direction de l'exploitation (Mme DUCHÉRAN) |
| code_categorie | catégorie d'acheteurs de l'entreprise | code de la table Categorie | valeur de la liste ; « autre » seulement avec un motif ; tout changement daté | saisie à l'accueil, revue par le service commercial | service commercial (Mme QUÉRINEL) |
| statut_carte | état de la carte | liste : active, suspendue, désactivée | « active » seulement si la date de fin de validité n'est pas dépassée et si l'entreprise n'a pas de date de fermeture | système de péage | direction de l'exploitation |
| tarif_applique | tarif du passage le jour du passage | décimal, en euros, deux décimales | égal au tarif en vigueur du type d'abonnement de la carte à la date du passage ; jamais modifié ensuite | système de péage, au passage | direction de l'exploitation, tarifs fixés par la direction générale |
| heure_passage | heure de l'entrée du véhicule | heure, hh:mm | entre 3 heures et 11 heures, sauf exception tracée | borne d'entrée | direction de l'exploitation |
| nom_titulaire | nom de la personne titulaire de la carte | texte | obligatoire ; **donnée personnelle** : accès limité aux agents de péage et au service commercial, conservée tant que la carte est valide puis pendant une durée fixée | saisie à l'accueil | direction de l'exploitation, avec l'avis de la déléguée à la protection des données |

**Trois règles de qualité** (0,5 pt pour deux règles, 0,5 pt pour la troisième), chacune rattachée à un problème de l'annexe 2.1 B et à une dimension de la qualité des données (F07 § 8.3 ; ISO/IEC 25012, annexe 2.5) :

1. **Contre les doublons d'entreprises – unicité.** Le SIREN devient obligatoire et unique : à la création d'une carte, l'agent cherche d'abord l'entreprise par son SIREN, et n'en crée une nouvelle que si elle n'existe pas. Les 400 doublons actuels sont fusionnés une fois (une fiche maîtresse par SIREN, à laquelle les cartes sont rattachées). Sans cela, le nombre d'entreprises actives de l'annexe 2.2 est surestimé.
2. **Contre les catégories « autre » – exactitude et cohérence.** La catégorie est choisie dans la liste de la table Categorie, et non saisie en texte libre ; « autre » exige un motif et les fiches « autre » (800, plus d'une sur dix) sont revues chaque trimestre par le service commercial. Tout reclassement est daté et tracé, ce qui permet de recalculer les années passées dans la nouvelle catégorie : c'est ce qui a manqué en 2026 (annexe 2.2).
3. **Contre les cartes d'entreprises fermées – actualité.** Une carte ne peut être active que si son entreprise n'a pas de date de fermeture : les SIREN sont rapprochés chaque trimestre du répertoire officiel des entreprises ; une date de fermeture désactive toutes les cartes de l'entreprise, et toute carte a une date de fin de validité. Le contrôle de janvier (une carte sur vingt, soit de l'ordre de 450 cartes sur 9 000 si l'échantillon est représentatif) sert de point de départ.
4. **Contre les passages sans carte – complétude.** Tout passage est rattaché à une carte : à la borne, l'acheteur sans carte saisit le SIREN de son entreprise, et la borne lui délivre une carte « à la nuit » provisoire, rattachée à l'entreprise après vérification du SIREN et saisie du titulaire par l'accueil (RG3) ; à défaut, le passage est marqué « non rattaché » et compté à part. Un passage sur dix deviendrait ainsi rattaché à une entreprise.

**Conclusion** : ces règles corrigent les données **à la source**, à la saisie, plutôt qu'à chaque extraction ; elles supposent un propriétaire désigné (direction de l'exploitation pour les cartes et les passages, service commercial pour les catégories) et un suivi par des indicateurs simples (taux de doublons, part des fiches « autre », part des passages non rattachés).

**Réponses tolérées**
- Catégorie ou type d'abonnement en simple attribut de l'entreprise ou de la carte, si la liste fermée des valeurs est posée dans le dictionnaire ou par une règle de qualité.
- Entité Véhicule reliée à la carte, si le candidat discute la cardinalité 1,1 de part et d'autre et la fusion possible ; ou cardinalité Entreprise 0,n pour detenir, si le candidat suppose qu'une fiche peut exister avant sa première carte.
- Entité Tarif (type d'abonnement et année) reliée au passage, à la place de l'attribut tarif_applique, si l'historique des tarifs est bien conservé.
- Association rattacher en 0,1 du côté du passage (clé étrangère facultative), si le candidat l'explique par les passages payés à la borne et le signale comme un écart à RG6.
- Représentation graphique en notation Merise ou en « pattes de corbeau », si elle est lisible (`JUR-T10`).
- Autres entrées du dictionnaire (raison_sociale, date_fermeture, immatriculation), si elles portent les mêmes rubriques.
- Trois règles parmi les quatre, ou une autre dimension justifiée (cohérence pour les cartes d'entreprises fermées).

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dans le modèle conceptuel, ou clé étrangère placée du mauvais côté (#num_carte dans Entreprise_acheteuse).
- *Cardinalités lues à l'envers* — « une entreprise a une seule carte » ; ou passage relié directement à l'entreprise, ce qui perd la carte et la borne.
- *Tarif lu dans le seul type d'abonnement* — les passages anciens seraient relus au tarif du jour, contre RG4 et RG6.
- *Morceau de cours* (`JUR-T01`) — définition du dictionnaire ou des dimensions de la qualité sans les quatre problèmes de l'annexe 2.1 B ; règles « vérifier la qualité » sans contrôle précis.
- *Requêtes écrites* (`JUR-T07`) — la question n'en demande aucune.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, cardinalités, règles de passage, modèle logique | définitions et méthode | F07 § 1 à 4 | notion de cours |
| Dictionnaire des données ; dimensions de la qualité (unicité, exactitude, complétude, cohérence, actualité) | définitions | F07 § 1 et 8.3 ; F08 § 4 | notion de cours |
| ISO/IEC 25012, modèle de qualité des données | caractéristiques de la qualité, données en annexe 2.5 | `iso_iec_25012` / F07 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) : minimisation, durée limitée | principes donnés en annexe 2.5 | `rgpd` / F15 | applicable depuis le 25/05/2018 |

---

### 2.2 – L'analyse de la fréquentation des acheteurs (3,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ». Limites : aucun calcul statistique, aucune manipulation d'outil ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexe 2.2 (passages, entreprises actives et paiement à la borne par catégorie et par saison, limites des chiffres de 2026, affirmation de Mme GARBUSSAC) ; annexe 2.1 (fonctionnement du péage, problèmes de qualité).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Étapes de la chaîne présentées ; collecte et nettoyage, chacune avec une limite de l'annexe 2.2 (panne, piétons, véhicules partagés ; doublons, passages non rattachés) | 0,5 |
| a-2 | Structuration, analyse et restitution, chacune avec une limite (reclassement, périmètre constant, unité de mesure) ; conclusion | 0,5 |
| b-1 | Deux constats argumentés et chiffrés, avec leur portée | 0,5 |
| b-2 | Troisième constat argumenté et chiffré | 0,5 |
| b-3 | Affirmation : unité de mesure (80 passages de véhicules, non 80 restaurants) et reclassement (périmètre constant) | 0,5 |
| b-4 | Affirmation : passages non enregistrés et véhicules partagés en ordre de grandeur ; cause non démontrée (aucune donnée sur les plateformes, autres explications) ; conclusion nuancée et suite à donner | 0,5 |
| c-1 | Analyses descriptive et exploratoire distinguées ; descriptive à périmètre constant puis exploratoire, justifiées ; courbes par catégorie à périmètre constant, annotées | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de traitement des indicateurs de fréquentation*

**La chaîne de traitement** (0,5 pt avec la collecte et le nettoyage) transforme des données brutes en information utile à la décision : **collecte** des données à leur source, **nettoyage** (doublons, valeurs manquantes ou incohérentes), **structuration** (règles de gestion et de calcul, rapprochements, chargement dans une base historisée), **analyse**, puis **restitution** aux décideurs (F08 § 1). Une erreur introduite à une étape n'est pas rattrapée par les suivantes. Pour la fréquentation des acheteurs :

| Étape | Ce que fera la chaîne | Limite traitée (annexe 2.2) |
|---|---|---|
| **Collecte** | chargement chaque nuit des passages du serveur du péage, avec la carte et la borne ; collecte aussi de l'état des bornes (journal des pannes) ; comptage de l'entrée des piétons ; lecture de chaque carte présente dans un véhicule | la panne de dix-huit nuits n'est signalée nulle part ; les piétons ne sont pas comptés ; un véhicule partagé ne compte qu'une carte |
| **Nettoyage** | nuits incomplètes repérées et marquées ; doublons d'entreprises fusionnés ; passages payés à la borne isolés tant qu'ils ne sont pas rattachés | les 9 000 passages perdus de juillet abaissent l'été 2026 sans le dire ; les doublons faussent les entreprises actives (annexe 2.1) |
| **Structuration** | catégories tirées de la table de référence ; reclassement daté et appliqué aussi aux années passées ; définitions écrites (passage, entreprise active) | le reclassement de 400 entreprises en janvier 2026 rend 2025 et 2026 incomparables |
| **Analyse** | comparaisons à périmètre constant, par saison, nuits de panne exclues ou estimées et signalées ; plusieurs mesures côte à côte : véhicules, cartes lues, entreprises actives | une baisse de passages de véhicules n'est pas une baisse d'acheteurs |
| **Restitution** | tableau de bord avec la définition de chaque indicateur, ses limites et les ruptures de série (reclassement, panne, ouverture du tramway) | des chiffres présentés sans conventions, qui nourrissent des lectures hâtives |

**Conclusion** (0,5 pt avec les trois dernières étapes) : les limites de l'annexe 2.2 ne sont pas des erreurs de calcul, mais des informations non collectées et des règles non écrites ; la chaîne les traite en amont (collecter l'état des bornes, lire toutes les cartes, dater les reclassements) plutôt que par des corrections à la main.

*2.2 b) – Trois constats et l'affirmation de Mme GARBUSSAC*

**Trois constats** parmi les suivants (0,5 pt pour deux constats, 0,5 pt pour le troisième : le fait chiffré, son interprétation et sa portée) :

1. **La fréquentation d'ensemble tient ; elle baisse l'été.** 2 060 passages par nuit en 2025, 2 000 en 2026 (moins de 3 %) ; l'hiver est stable (1 860 les deux années) et toute la baisse vient de l'été (de 2 260 à 2 140). Les commerces de détail (+ 20), les marchés forains (+ 10) et la restauration collective (+ 10) progressent ; la baisse d'« autre » (− 20) n'est que l'effet du reclassement. L'attractivité du marché n'est pas en cause : la question porte sur les restaurants et sur l'été.
2. **La baisse des passages de restaurants est réelle en véhicules et concentrée l'été.** De 800 à 720 passages par nuit (− 10 %) ; à périmètre constant, sans les 20 passages des entreprises reclassées, de 800 à 700 (− 100, soit − 12,5 %). Elle vient surtout de l'été (de 900 à 740 à périmètre constant, − 160) et peu de l'hiver (de 700 à 660, − 40) : c'est l'été qu'ont eu lieu la panne de la borne et la plupart des véhicules partagés.
3. **Les entreprises actives ne disent pas ce qu'elles semblent dire.** Les restaurants passent de 1 500 à 1 800 et « autre » de 1 000 à 600 : c'est le reclassement de 400 entreprises. À périmètre constant, les restaurants actifs passent de 1 500 à 1 400 (environ − 7 %), une baisse bien plus faible que celle des passages ; « autre » est stable (1 000). Les restaurateurs qui viennent dans le véhicule d'un autre n'ont plus de passage à leur nom : une partie de ces 100 entreprises « inactives » vient sans doute encore.
4. **Le paiement à la borne double pour les restaurants et les commerces de détail.** De 5 % à 10 % des passages, et d'environ 7 % à 10 % pour l'ensemble, après la hausse de 10 % du tarif des cartes annuelles et mensuelles au 1er janvier 2026. Les acheteurs arbitrent le prix : ils viennent moins régulièrement, ou à plusieurs. Ces passages ne sont rattachés à aucune entreprise, ce qui fragilise encore la mesure, et ils éloignent BRÉVALIM d'une relation dématérialisée avec des acheteurs connus, voulue par le plan.

**L'affirmation de Mme GARBUSSAC** (0,5 pt pour l'unité de mesure et le reclassement, 0,5 pt pour la suite) : « les restaurateurs désertent le marché au profit des plateformes de livraison » n'est pas démontré par les chiffres.
- **L'unité de mesure** : la baisse de 80 porte sur des passages de véhicules par nuit, non sur des restaurants ; un restaurant ne vient pas chaque nuit et un véhicule peut porter deux ou trois restaurateurs. Parler de « 80 restaurants perdus par nuit » confond le véhicule, l'acheteur et l'entreprise.
- **Le reclassement** : la comparaison mêle deux périmètres. À périmètre constant, la baisse des passages est un peu plus forte (100 et non 80), mais le nombre de restaurants actifs ne baisse que d'environ 7 % (de 1 500 à 1 400) : on est loin d'une désertion.
- **Les passages non enregistrés** : la panne a fait perdre environ 9 000 passages (18 nuits × 500), soit environ 60 par nuit sur l'été, toutes catégories confondues, dont une partie seulement concerne les restaurants : un effet réel mais faible au regard des 160 passages de restaurants perdus l'été. Les restaurateurs venus à pied depuis septembre 2026 ne sont pas comptés, sans qu'on puisse les chiffrer.
- **Les véhicules partagés** expliquent l'essentiel : 100 véhicules partagés par nuit l'été 2026, à deux ou trois, ce sont 100 à 200 véhicules de moins pour le même nombre d'acheteurs ; 40 l'hiver, soit 40 à 80. C'est l'ordre de grandeur de toute la baisse à périmètre constant (160 l'été, 40 l'hiver) : les restaurateurs viennent ensemble plutôt que moins.
- **La cause n'est pas mesurée** : aucune donnée de l'annexe ne porte sur les plateformes de livraison. Que la baisse coïncide avec leur essor ne prouve rien (corrélation n'est pas causalité) ; d'autres explications sont dans l'annexe : la hausse du tarif des cartes, qui pousse à partager un véhicule ou à payer à la borne, et le tramway. Retenir la seule explication qui conforte une conviction relève du **biais de confirmation** (F08 § 5).

Conclusion : les chiffres montrent moins de véhicules de restaurateurs, surtout l'été, pas moins de restaurateurs. Avant toute campagne, il faut mesurer les acheteurs et non les véhicules (lecture de chaque carte, comptage des piétons), comparer à périmètre constant, interroger quelques restaurateurs, et réexaminer l'effet de la hausse du tarif des cartes.

*2.2 c) – La méthode d'analyse et la représentation visuelle*

**La méthode** (0,5 pt avec la représentation) : l'**analyse descriptive** résume ce qui s'est passé (évolutions, répartitions, écarts) ; l'**analyse exploratoire** cherche, en croisant les données, des motifs et des explications que l'on ne connaissait pas d'avance (F08 § 2). La question « les restaurateurs désertent-ils le marché ? » est d'abord une question de fait : elle relève de l'**analyse descriptive**, à condition de la mener à périmètre constant, par saison et dans la bonne unité (acheteurs et entreprises, pas seulement véhicules). Pour comprendre pourquoi les passages baissent, il faut ensuite une **analyse exploratoire** : croiser les passages par quartier d'origine, par type d'abonnement, par heure, par entrée, rapprocher le paiement à la borne et la hausse du tarif. Ni l'une ni l'autre ne prouve la cause invoquée ; une analyse prédictive serait sans objet ici.

**La représentation** : des **courbes** mensuelles de 2025 et 2026, une par catégorie (ou un petit graphique par catégorie, à la même échelle), des passages par nuit **à périmètre constant** (2025 recalculé avec les catégories de 2026), **annotées** des ruptures (hausse du tarif en janvier 2026, panne de juillet, tramway en septembre), sur un axe qui part de zéro. La courbe montre l'évolution et la saisonnalité ; les annotations empêchent de lire une panne comme une désertion. À éviter : un graphique en secteurs, des barres en valeurs cumulées, un axe tronqué qui grossirait la baisse.

**Réponses tolérées**
- Chaîne présentée selon les étapes de l'informatique décisionnelle (collecte, extraction-transformation-chargement, stockage, restitution), si une limite est rattachée à chaque étape.
- Limites rattachées à une autre étape que celles du corrigé, si le rattachement est justifié (le reclassement traité à l'analyse, les véhicules partagés à la restitution comme limite de l'unité de mesure).
- Ordres de grandeur non exigés : une lecture qualitative de la panne et des véhicules partagés suffit si elle est argumentée.
- Autres constats tirés de l'annexe 2.2 (restauration collective plus forte l'hiver, « autre » toujours payé à la borne pour un passage sur cinq), s'ils sont chiffrés et interprétés.
- Analyse diagnostique présentée comme une variante de l'analyse exploratoire ; réponse « exploratoire » si le candidat montre qu'elle s'appuie sur une description à périmètre constant.
- Histogramme groupé par catégorie, 2025 et 2026, été et hiver, à périmètre constant.

**Erreurs fréquentes**
- *Corrélation lue comme causalité* (`ET-26`) — la baisse attribuée aux plateformes de livraison sans aucune donnée sur elles.
- *Prudence d'interprétation oubliée* (`JUR-D06`) — 1 800 restaurants actifs lus comme une hausse, ou 80 passages lus comme 80 restaurants.
- *Informatique décisionnelle réduite à un outil* (`ET-05`, `JUR-D02`) — « le tableau de bord corrigera les chiffres », sans collecte de l'état des bornes ni règles écrites.
- *Analyse prédictive ou calcul statistique proposés* (`JUR-T07`) — prévision de la fréquentation, tests statistiques, hors attente.
- *Chaîne récitée* (`JUR-T01`) — les cinq étapes sans les limites de l'annexe 2.2.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement des données | définitions et méthode | F08 § 1 | notion de cours |
| Analyses descriptive, exploratoire et prédictive | définitions | F08 § 2 | notion de cours |
| Choix d'une représentation ; biais de confirmation ; corrélation et causalité ; axe tronqué | méthode | F08 § 5 | notion de cours |

---

### 2.3 – La gouvernance des données des flux alimentaires (3,5 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) » ; `2.3.a` « Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques » ; `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression » ; `2.3.f` « Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques ». Limites : rôles « illustratifs, non normatifs » ; aucune analyse juridique ; aucune expertise des infrastructures ; aucune vente de données.

**Annexes mobilisées** : annexe 2.3 (demande de la métropole, collecte actuelle, avis de l'Union des grossistes, usages attendus) ; annexe 1.1 (organigramme, portail des entreprises installées, bureautique en ligne, plan « Marché de Brévaline 2031 ») ; annexe 2.5 (DAMA-DMBOK, principes du RGPD, déléguée à la protection des données).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance des données définie ; DAMA-DMBOK situé (référentiel, domaines utiles au cas) ; propriétaire et son titulaire chez BRÉVALIM | 0,5 |
| a-2 | Intendant et responsable du référentiel, avec leurs titulaires chez BRÉVALIM et chez les grossistes (déclarants, Union) ; instance de décision | 0,5 |
| b-1 | Création (déclaration) et stockage, avec une règle chacun | 0,5 |
| b-2 | Usage et diffusion agrégée à la métropole : règle de seuil, refus des déclarations individuelles, définitions jointes | 0,5 |
| b-3 | Archivage et suppression, durées fixées ; coordonnées des déclarants ; anciens tableurs | 0,5 |
| c-1 | Donnée comme actif immatériel ; valeur d'usage pour BRÉVALIM tirée de l'annexe 2.3 D, et ses conditions | 0,5 |
| c-2 | Deux risques tirés du cas, avec leurs effets et une parade | 0,5 |

**Réponse attendue**

*2.3 a) – L'organisation de la gouvernance des données des flux*

**La gouvernance des données** (0,5 pt avec le propriétaire) est l'ensemble des rôles, des règles, des instances et des processus qui fixent qui décide de quoi sur les données (définitions, qualité, accès, conservation, diffusion), pour en faire un actif fiable, protégé et utile (F07 § 8). Le **DAMA-DMBOK** est un **référentiel** de bonnes pratiques, ni norme ni logiciel ; il organise la gestion des données en onze domaines autour de la gouvernance (annexe 2.5). Pour les tonnages, quatre domaines comptent : la **qualité** (déclarations manquantes, origines vides), les **métadonnées** (définition écrite du produit régional), les **données de référence** (liste des grossistes déclarants, nomenclatures des filières et des origines) et la **sécurité** (accès, diffusion). Les rôles sont illustratifs : ils s'adaptent à une société de 210 salariés, sans créer de direction des données.

| Rôle | Mission pour les données des flux | Titulaire chez BRÉVALIM | Titulaire chez les grossistes |
|---|---|---|---|
| **Propriétaire** | décide de ce qui est collecté, des définitions, des droits d'accès et des règles de diffusion ; valide les chiffres de chaque trimestre avant leur envoi | Mme Nadège QUÉRINEL, responsable commerciale et des relations avec les entreprises, qui reçoit les déclarations et porte la relation avec les grossistes ; arbitrage par vous, directeur(rice) général(e) délégué(e) | chaque grossiste reste maître de ses données détaillées : il les déclare, en connaît l'usage et y accède ; aucune n'est transmise à un tiers sans son accord |
| **Intendant** | applique les règles au quotidien : dictionnaire, contrôles, relances, corrections, journal des estimations, indicateurs de qualité | un(e) chargé(e) des données des flux du service commercial, nommément désigné(e), avec du temps prévu pour ce rôle (celui qu'occupe aujourd'hui, sans mandat, l'assistante) | un déclarant nommé par chaque grossiste, qui répond de l'exactitude et de la ponctualité de sa déclaration |
| **Responsable du référentiel** | tient les données de référence datées : grossistes déclarants et leur filière, filières, origines, définition du produit régional ; gère l'outil, les droits et le journal des accès | le service des systèmes d'information, M. Corentin LAVEYRAC, pour l'outil et les droits ; le contenu des nomenclatures est arrêté par le propriétaire | l'Union des grossistes, qui valide avec le propriétaire les nomenclatures et la définition du produit régional ; chaque grossiste signale ses changements |

**L'instance** (0,5 pt avec l'intendant et le responsable du référentiel) : un **comité des données des flux**, chaque trimestre avant l'envoi, réunit le propriétaire, l'intendant, le responsable des systèmes d'information, la déléguée à la protection des données (Mme TALMONDIER, pour les coordonnées des déclarants) et un représentant de l'Union des grossistes ; il arrête les définitions, la règle de diffusion et les durées de conservation. La métropole est **destinataire** des chiffres, consultée sur ses besoins, mais n'en est pas propriétaire. Ce dispositif répond à la défiance des grossistes : ils participent aux règles qui protègent leurs données.

*2.3 b) – Le cycle de vie des données des flux*

Le cycle de vie suit la donnée de sa **création** à sa **suppression** : stockage, usage, archivage, avec une règle et un responsable à chaque étape (F07 § 8.4). Une règle par étape (0,5 pt pour la création et le stockage, 0,5 pt pour l'usage et la diffusion, 0,5 pt pour l'archivage et la suppression) :

| Étape | Règle |
|---|---|
| **Création (déclaration)** | un formulaire unique sur le portail des entreprises installées remplace les tableurs envoyés par courriel ; filières et origines (région, reste de la France, étranger) choisies dans des listes ; origine obligatoire ; définition écrite du produit régional affichée ; écart important avec le même mois de l'année précédente à confirmer ; déclaration avant le 10 du mois suivant, par le déclarant nommé |
| **Stockage** | une seule base des flux ; plus aucun tableur dans la bureautique en ligne ; accès réservé au propriétaire, à l'intendant et au service des systèmes d'information, chaque grossiste ne voyant que ses propres données ; les placiers et le reste du service commercial n'y ont plus accès ; accès journalisés |
| **Usage (traitement)** | relance automatique quelques jours avant et après l'échéance ; une déclaration manquante n'est estimée que selon une règle écrite et marquée « estimée » ; le taux de déclarations reçues et la part des origines renseignées accompagnent chaque chiffre ; validation trimestrielle par le propriétaire |
| **Usage (diffusion à Brévaline Métropole)** | chaque trimestre, des **totaux** par filière et par origine et la part des produits régionaux, avec leurs définitions et leur taux de couverture ; **jamais la déclaration d'un grossiste**, ce qui conduit à décliner cette partie de la demande de la métropole ; une case filière × origine n'est diffusée que si elle regroupe au moins trois grossistes et que les deux premiers n'en font pas, ensemble, plus des deux tiers ; sinon, les origines de la filière sont regroupées ; pour les produits laitiers, où deux grossistes font les trois quarts des volumes, seul le total de la filière est diffusé, sans détail par origine, comme l'Union l'accepte (annexe 2.3 C) ; une convention de partage des données écrite avec la métropole fixe l'usage (l'observatoire) et la citation des définitions |
| **Archivage** | déclarations détaillées conservées pendant une durée arrêtée par le comité, par exemple cinq ans, pour comparer les années et suivre le plan jusqu'en 2031, en accès restreint ; séries agrégées conservées durablement |
| **Suppression** | au terme de la durée, suppression programmée et tracée des déclarations détaillées ; reprise des tableurs utiles depuis 2012, puis suppression des fichiers du dossier partagé ; coordonnées d'un déclarant supprimées dès qu'il ne l'est plus, conformément aux principes de minimisation et de durée limitée (annexe 2.5) |

Les tonnages d'une entreprise ne sont pas des données personnelles ; seules les coordonnées des déclarants le sont. Leur protection tient donc d'abord à la confiance et aux règles que BRÉVALIM se donne, plus qu'à une obligation, qu'il n'est pas demandé d'analyser.

*2.3 c) – La valeur des données des flux et deux risques*

**La valeur** (0,5 pt) : les données sont un **actif immatériel** du marché, sans traduction au bilan : leur valeur est une **valeur d'usage**, qui tient aux décisions qu'elles éclairent (F07 § 8.6). Pour BRÉVALIM, d'après l'annexe 2.3 D :
- **piloter le plan** : la part des produits régionaux (de 30 % à 40 %) n'est mesurable qu'avec ces données ;
- **dialoguer avec les actionnaires**, et d'abord avec la métropole (60 % du capital), qui en fait la demande, et rendre compte chaque trimestre comme le prévoit le plan ;
- **expliquer les redevances d'emplacement** à l'Union des grossistes, à partir de l'activité réelle du marché ;
- **montrer l'attractivité du marché** aux grossistes qui envisagent de s'installer et aux acheteurs.
Cette valeur dépend de deux conditions qui manquent aujourd'hui : la **qualité** (une déclaration sur dix manquante, 15 % en retard, 35 % des tonnages sans origine utile, aucune définition, donc une part de 30 % fragile) et la **confiance des grossistes**, qui produisent la donnée. Sans eux, l'actif disparaît. Il ne s'agit pas de vendre ces données.

**Deux risques** parmi (0,5 pt) :
- **la fuite des données d'un grossiste** : l'envoi d'octobre 2025 l'a montré, et le dossier partagé reste ouvert aux 15 personnes du service commercial et à des placiers ; un concurrent connaîtrait les fournisseurs et la part de marché d'un grossiste. Effet : défiance, déclarations qui se tarissent, relation dégradée avec l'Union, actionnaire à 12 %. Parade : accès restreint, diffusion seulement agrégée, journal des accès ;
- **la publication d'un chiffre faux** : l'observatoire publierait une part de produits régionaux calculée sans définition, avec des origines vides comptées dans le total et des déclarations manquantes remplacées sans le dire ; l'Union la conteste déjà. Effet : crédibilité de BRÉVALIM et du plan atteinte auprès de la métropole, décisions publiques prises sur un chiffre erroné. Parade : définition écrite, contrôles, validation du propriétaire, taux de couverture publié avec chaque chiffre ;
- **la perte ou la dépendance** : des tableurs dispersés depuis 2012, consolidés par une seule personne quand elle en a le temps ; une absence ou une erreur de manipulation, et la série est perdue ;
- **le détournement d'usage** : des déclarations individuelles transmises à la métropole pourraient servir à d'autres fins que l'observatoire, ce que craignent les grossistes.

**Réponses tolérées**
- Propriétaire placé à la direction générale (Mme VAUCLERC) ou chez vous, si le rôle de Mme QUÉRINEL dans la relation avec les grossistes est reconnu ; intendant chargé aussi du référentiel, si le dépositaire technique est nommé.
- Grossiste présenté comme « producteur » de la donnée plutôt que comme propriétaire de ses données détaillées, si ses droits (accès à ses données, aucun usage sans accord) sont posés.
- Responsable des données (CDO) cité, si le candidat le présente comme facultatif pour une société de cette taille.
- Autre seuil de diffusion (au moins cinq grossistes, part maximale des deux premiers grossistes), s'il empêche de déduire les chiffres des deux grossistes des produits laitiers ; autre durée d'archivage justifiée. Un seuil portant sur la part du seul premier grossiste ne suffit pas : deux grossistes peuvent peser chacun moins de la moitié et ensemble les trois quarts.
- Cycle de vie en sept étapes (collecte, stockage, traitement, partage, archivage, destruction…), si une règle est posée à chacune.
- Autres risques justifiés (obsolescence d'une série si la définition change sans être datée).

**Erreurs fréquentes**
- *Gouvernance confiée à l'informatique* (`JUR-G10`) — le service des systèmes d'information « propriétaire » des tonnages, alors que les définitions et la diffusion sont des décisions métier.
- *Norme, référentiel et solution confondus* (`ET-01`, `JUR-S06`) — DAMA-DMBOK présenté comme un logiciel ou une norme à laquelle se conformer.
- *Rôles récités* (`JUR-T01`) — propriétaire, intendant et comité définis sans titulaires chez BRÉVALIM et chez les grossistes.
- *Diffusion sans règle* — transmettre les déclarations individuelles à la métropole, ou des totaux qui révèlent les deux grossistes des produits laitiers.
- *Dérive juridique* (`JUR-T07`) — analyse du secret des affaires, du droit de la concurrence ou des droits des personnes, non demandée.
- *Valeur réduite à un prix* — vente des données ou valeur inscrite au bilan, hors attente.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 (DAMA International) | référentiel de gestion des données, domaines (gouvernance, qualité, métadonnées, données de référence, sécurité) | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Rôles de la gouvernance des données (propriétaire, intendant, comité) ; cycle de vie | définitions | F07 § 8.1 et 8.4 | notion de cours |
| Donnée comme actif immatériel ; valeur d'usage ; risques de perte, de fuite, d'obsolescence | définitions | F07 § 8.6 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) : minimisation, durée limitée ; déléguée à la protection des données | principes donnés en annexe 2.5 | `rgpd` / F15 | applicable depuis le 25/05/2018 |

---

### 2.4 – Le tableau de bord du conseil d'administration (2,5 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) » ; `3.1.e` « Revue et amélioration continue des dispositifs de pilotage ». Limites : recul critique sur les indicateurs, reliés au plan et aux remarques des administrateurs.

**Annexes mobilisées** : annexe 2.4 (tableau du quatrième trimestre 2026, production, remarques des administrateurs) ; annexes 2.2 (panne de la borne) et 2.3 (envoi d'octobre 2025, part des produits régionaux) ; annexe 1.1 (plan « Marché de Brévaline 2031 », chiffre d'affaires de 28 M€, dépenses du SI d'environ 1,3 M€).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Tableau de bord défini ; trois défauts tirés de l'annexe 2.4 et des remarques des administrateurs | 0,5 |
| b-1 | Indicateur d'un objectif du plan, à cinq champs | 0,5 |
| b-2 | Indicateur de risque, à cinq champs | 0,5 |
| b-3 | Troisième indicateur à cinq champs, qui équilibre le tableau (coût du SI ou autre objectif du plan) | 0,5 |
| c-1 | Deux mesures de revue et d'amélioration continue, applicables par le conseil et la direction | 0,5 |

**Réponse attendue**

*2.4 a) – Trois défauts du tableau de bord*

**Le tableau de bord** est un ensemble restreint d'indicateurs choisis pour piloter des objectifs, présentés pour décider : chaque indicateur a une définition, une source, une cible et une tendance, et il est commenté (F08 § 3). Celui d'un conseil d'administration est stratégique : trimestriel, de huit à douze indicateurs, équilibrés entre la performance, les risques et les coûts (F09 § 4.1). Trois défauts parmi les suivants (0,5 pt) :
- **aucune cible ni référence** : 7 300 k€ de chiffre d'affaires ne disent rien sans objectif ni prévision, comme le relève le représentant de la Banque VERDELIN ; seule la comparaison avec le même trimestre de 2025 est donnée ;
- **aucune source ni définition** : le chiffre d'affaires du tableau (7 300 k€) diffère de celui de la comptabilité (7 000 k€), soit 300 k€ d'écart, et personne ne sait d'où il vient ; les tonnes viennent du tableur des déclarations, dont la fiabilité est faible (annexe 2.3) ;
- **aucun indicateur du plan** « Marché de Brévaline 2031 », adopté en janvier : ni part des produits régionaux, ni dématérialisation, ni déchets valorisés, ni sûreté et sécurité des données, comme le relève le président ;
- **un tableau déséquilibré** : neuf indicateurs de volume ou de moyens (dont les nuits d'ouverture, qui ne varient pas), aucun indicateur de risque (la panne du péage, l'envoi des tonnages n'y figurent pas) ni de coût du système d'information, que demande l'administratrice du Département ;
- **une production artisanale** : trois jours de recopie à la main, un tableau inchangé depuis 2015, envoyé la veille sans commentaire : risque d'erreur et aucune analyse pour le conseil.

*2.4 b) – Trois indicateurs qui complètent le tableau de bord*

Un indicateur par item (0,5 pt chacun), avec ses cinq champs :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des produits régionaux dans les tonnages entrés (objectif du plan) | tonnes entrées d'origine régionale, selon la définition écrite du produit régional / tonnes entrées déclarées × 100 | base des déclarations mensuelles des grossistes, après contrôles de l'intendant des données des flux | trimestrielle | 40 % en 2031 (plan), soit environ deux points de plus par an ; point de départ de 2026 recalculé selon la définition écrite | environnement |
| Nombre d'incidents majeurs du système d'information (risque) | nombre d'interruptions de plus de deux heures, pendant les heures d'activité, du péage, du logiciel de gestion du marché ou de l'application des acheteurs, et de fuites de données, dans le trimestre | registre des incidents tenu par le service des systèmes d'information | trimestrielle | aucun incident majeur ; chaque incident présenté au conseil avec sa cause et l'action engagée | processus |
| Dépenses du système d'information rapportées au chiffre d'affaires (coût) | dépenses du système d'information de l'exercice / chiffre d'affaires de l'exercice × 100 | progiciel comptable (comptabilité de BRÉVALIM) | annuelle, avec le cumul de l'exercice présenté chaque trimestre | au plus 5 % (un peu moins de 5 % en 2026 : environ 1,3 M€ pour 28 M€), toute hausse étant rattachée à un projet du plan | financier |

Chaque indicateur répond à une remarque de l'annexe 2.4 : le plan pour le président, les incidents pour Mme GARBUSSAC, le coût pour l'administratrice du Département. Le premier ne vaudra que si la gouvernance des données des flux (question 2.3) est en place : un indicateur n'est pas plus fiable que sa source.

*2.4 c) – Deux mesures pour revoir et améliorer le tableau de bord*

Deux mesures parmi (0,5 pt) :
- **une revue annuelle formalisée** : chaque année, en début d'exercice, le conseil revoit les indicateurs (supprimer, regrouper, ajouter : F09 § 4.3 ; supprimer ceux qui ne servent pas, comme les nuits d'ouverture ; ajouter ceux qu'exige le plan), fixe les cibles et les responsables, réajuste les cibles et compare les résultats à la trajectoire du plan ; les remarques des administrateurs sont relevées à chaque séance pour nourrir cette revue (F09 § 4.3) ;
- **une fiche par indicateur et un responsable du tableau de bord** : définition, formule, source, propriétaire, cible, date de révision ; vous en êtes responsable devant le conseil ; le chiffre d'affaires est rapproché de la comptabilité avant chaque envoi ;
- **une production fiabilisée** : le tableau est alimenté depuis les sources fiabilisées (péage, base des flux, comptabilité) plutôt que recopié pendant trois jours, envoyé une semaine avant le conseil, avec un commentaire des écarts à la cible.

Ces mesures s'adressent au conseil et à la direction générale, destinataires du tableau, et non au seul service des systèmes d'information.

**Réponses tolérées**
- Autre indicateur du plan, à cinq champs : part des déchets valorisés (tonnes valorisées / tonnes de déchets du site × 100 ; pont-bascule et suivi des déchets ; trimestrielle ; 80 % en 2031 ; environnement) ; dématérialisation (part des acheteurs utilisant la carte sur téléphone, ou des entreprises installées utilisant le portail ; 100 % en 2029 ; client).
- Autre indicateur de risque : disponibilité du péage pendant les heures d'activité ; part des déclarations de tonnages reçues dans le délai (risque sur la donnée publiée).
- Axe « gouvernance » pour l'indicateur de risque, ou « client » pour la part des produits régionaux, s'il est justifié.
- Autres mesures de revue justifiées (comparaison avec le tableau de bord d'autres marchés, si les chiffres sont donnés comme repères).
- Revue présentée selon la roue de Deming (planifier, faire, vérifier, agir), si elle est appliquée au tableau du conseil.

**Erreurs fréquentes**
- *Indicateurs génériques ou incomplets* (`ET-18`) — « taux de satisfaction », « nombre de projets », sans formule, source, cible ni lien avec le plan ou les remarques des administrateurs.
- *Tableau limité aux indicateurs techniques* (`ET-18`) — disponibilité des serveurs, nombre de tickets, sans le plan ni le coût.
- *Calcul de coût hors attente* — coût complet ou retour sur investissement du système d'information, non demandés.
- *Défauts sans preuve* (`JUR-T08`) — défauts génériques, sans les 7 300 et 7 000 k€, le plan absent ou les remarques des administrateurs.
- *Réponse à la mauvaise échelle* (`JUR-T07`) — mesures adressées au seul service des systèmes d'information, alors que le tableau sert le conseil d'administration.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Tableau de bord ; indicateur à cinq champs (formule, source, fréquence, cible, axe) | définitions et méthode | F08 § 3 ; F09 § 4.1 | notion de cours |
| Axes du tableau de bord prospectif (financier, client, processus, apprentissage) et axes ESG | structure | F09 § 4.1 | notion de cours |
| Revue et amélioration continue ; critique d'un reporting (supprimer, regrouper, ajouter, cibles et responsables) | méthode | F09 § 4.3 | notion de cours |
