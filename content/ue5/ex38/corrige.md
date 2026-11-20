# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 38 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F09 performance du SI, F15 RGPD opérationnel, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle des données exécuté, indicateurs, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le modèle des données de la redevance | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) | 2,5 |
| 2.2 L'architecture des données et le référentiel des adresses et des logements | `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) ; `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) | 2 |
| 2.3 L'effet de la redevance incitative | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 4 |
| 2.4 L'ouverture et la valorisation des données | `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `2.3.e` Aspects réglementaires (RGPD, archivage légal) et monétisation des données | 2,5 |
| 2.5 Le coût du dispositif numérique de la redevance et son pilotage | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) | 2 |
| **Dossier 2 – Organiser et exploiter les données de la redevance incitative** |  | **13** |

Répartition indicative : connaissances (modèles conceptuel et logique et règles de passage, entrepôt et lac de données, données de référence, chaîne de traitement, analyses descriptive et exploratoire, anonymisation et pseudonymisation, rôle du délégué à la protection des données, cycle de vie, coût complet) environ 3,5 points (la moitié des items 2.1 b-1, 2.1 b-3, 2.2 a-1, 2.2 b-1, 2.3 a-1, 2.3 b-1, 2.4 a-1, 2.4 c-1, 2.4 c-2 et 2.5 a-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 9,5 points, soit environ 73 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le modèle des données de la redevance (2,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) ». Modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites ; modèle physique seulement nommé ; aucune requête.

**Annexes mobilisées** : annexe 2.1 (règles de gestion, extrait du modèle logique actuel, précisions de la responsable de la facturation, anomalies de 2026).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux défauts du modèle actuel, chacun rapporté à une règle de gestion et relié à une anomalie chiffrée de l'annexe 2.1 C | 0,5 |
| a-2 | Troisième défaut, rapporté à une règle et à une anomalie ; conclusion : les anomalies viennent de la structure des données, pas seulement des saisies | 0,5 |
| b-1 | Modèle conceptuel et modèle logique distingués ; six entités avec identifiant et attributs élémentaires (logement, foyer, bac, tournée, levée, facture) | 0,5 |
| b-2 | Cinq associations et leurs cardinalités, justifiées par les règles : occupation n:m porteuse des dates d'arrivée et de départ, bac affecté au logement, levée rattachée à un bac et à une tournée, facture adressée à un foyer | 0,5 |
| b-3 | Modèle logique de sept tables déduit par les règles de passage énoncées (clé étrangère côté 1,1 ; table d'association à clé composée pour l'occupation) | 0,5 |

**Réponse attendue**

*2.1 a) – Trois défauts du modèle logique actuel*

Trois défauts parmi les suivants (0,5 pt pour deux défauts, 0,5 pt pour le troisième et la conclusion), chacun rapporté à une règle de gestion et à une anomalie :

1. **Le bac est rattaché au redevable, et non au logement.** Le numéro de puce et le volume du bac sont des colonnes de la table REDEVABLE, alors que la règle RG4 affecte le bac à un logement, où il reste quand le foyer déménage. À chaque emménagement, l'agent écrase l'ancien occupant ou recopie la puce dans une nouvelle fiche : deux fiches portent alors la même puce, et les levées du nouvel occupant peuvent être imputées à l'ancien. Ce défaut explique une partie des **2 000 doublons** et des **1 700 factures** adressées à un foyer parti. Il manque en outre au bac un identifiant propre : la puce sert d'identifiant de fait, si bien qu'une puce remplacée rend ses levées orphelines (RG4 : la puce peut changer sans que le bac change).
2. **L'historique des occupants est perdu.** Le modèle ne connaît ni le logement (RG1) ni l'occupation datée (RG3) : une seule date d'arrivée, aucune date de départ, et une fiche écrasée à chaque changement d'occupant. On ne peut donc pas savoir quel foyer occupait un logement à une date passée (annexe 2.1 C), ni attribuer à coup sûr une levée au foyer présent ce jour-là : d'où les factures adressées à d'anciens occupants et les contestations impossibles à trancher.
3. **L'adresse est saisie en texte libre.** RG1 situe le logement à une adresse désignée par son code dans le référentiel des adresses, alors que le logiciel stocke une chaîne libre (« 12 r. des Lilas », « Les Lilas, 12 »). Le même logement apparaît sous plusieurs formes : c'est la cause la plus fréquente des **2 000 doublons**, et elle rend impossible tout rapprochement avec les fichiers des communes. Le défaut pèse surtout dans la ville-centre, où les compléments d'adresse (bâtiment, porte) sont nombreux, et qui concentre les trois quarts des levées non rattachées.
4. **Les levées n'ont ni heure, ni tournée, ni lien contrôlé avec un bac.** La table LEVEE ne garde que la puce et la date, alors que RG5 et RG6 rattachent chaque levée à une tournée, effectuée par un camion, à une date et à une heure. De plus, le numéro de puce n'y est pas une clé étrangère : rien ne garantit qu'il désigne un bac connu. D'où les **40 000 levées non rattachées** (une sur cinquante), rapprochées à la main par deux agents, et l'impossibilité de « prouver une levée » lors d'une contestation.

**Conclusion** : les anomalies de 2026 ne sont pas d'abord des erreurs de saisie ; elles viennent de la **structure des données**, qui ne traduit pas les règles de gestion. Les corriger à la main chaque semaine ne les fera pas disparaître : il faut corriger le modèle.

*2.1 b) – Le modèle conceptuel et le modèle logique des données de la redevance*

**Les deux modèles** : le **modèle conceptuel des données** représente les objets de gestion (entités), leurs propriétés et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique ; il ne comporte aucune clé étrangère. Le **modèle logique** le traduit en tables, avec leurs clés primaires et leurs clés étrangères, selon des règles de passage, indépendamment du logiciel de gestion de base de données ; le modèle physique, propre à ce logiciel (types, index), n'est pas demandé (F07 § 1 et 2).

**Les entités** (0,5 pt avec la distinction ; identifiant souligné dans la copie, ici en premier) :
- **Logement** (num_logement, code_adresse, complement_adresse, type_logement) ;
- **Foyer** (num_foyer, nom_titulaire, telephone, courriel) ;
- **Bac** (num_bac, num_puce, volume_litres, date_mise_service) : l'identifiant est le numéro gravé sur la cuve, et non la puce, qui peut être remplacée (RG4) ;
- **Tournee** (num_tournee, date_tournee, secteur, immatriculation_camion) : le camion est un attribut de la tournée, aucune règle ne lui donnant d'autres propriétés (RG5) ;
- **Levee** (num_levee, date_levee, heure_levee) ;
- **Facture** (num_facture, semestre, date_emission, montant).

Le code de l'adresse est un attribut du logement, qui renvoie au référentiel des adresses (question 2.2 b) ; le montant est enregistré tel qu'il a été facturé, son calcul n'étant pas modélisé (RG8).

**Les associations et leurs cardinalités** (0,5 pt) :

| Association | Entités et cardinalités | Règle de gestion |
|---|---|---|
| *occuper* (date_arrivee, date_depart) | Foyer (1,n) — Logement (0,n) | RG3 : un logement est occupé successivement par zéro, un ou plusieurs foyers (il peut être vacant) ; un foyer occupe ou a occupé au moins un logement, parfois plusieurs ; les dates dépendent du couple foyer-logement : ce sont des attributs de l'association |
| *etre_affecte* | Bac (1,1) — Logement (0,n) | RG4 : un bac est affecté à un seul logement ; un logement dispose d'aucun, d'un ou de plusieurs bacs |
| *concerner* | Levee (1,1) — Bac (0,n) | RG6 : une levée concerne un seul bac ; un bac peut n'avoir fait l'objet d'aucune levée |
| *etre_lue_lors_de* | Levee (1,1) — Tournee (1,n) | RG6 : une levée est lue lors d'une seule tournée ; une tournée comporte au moins une levée |
| *etre_adressee* | Facture (1,1) — Foyer (0,n) | RG7 : une facture est adressée à un seul foyer ; un foyer qui vient d'arriver peut n'en avoir reçu aucune |

Le foyer n'est pas relié directement au bac ni à la levée : on retrouve le foyer facturé pour une levée en passant par le bac, le logement et l'occupation en cours à la date de la levée. C'est ce qui permet de facturer le bon occupant après un déménagement.

**Le modèle logique** (0,5 pt), obtenu par les règles de passage :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire ;
2. pour une association dont l'une des pattes a pour cardinalité maximale 1 (*etre_affecte*, *concerner*, *etre_lue_lors_de*, *etre_adressee*), la clé primaire de l'entité du côté « n » migre comme clé étrangère dans la table de l'entité du côté 1,1 (obligatoire, puisque la cardinalité minimale est 1) ;
3. l'association *occuper*, dont les deux cardinalités maximales sont n, devient une table dont la clé primaire est composée des clés des deux entités, chacune clé étrangère, et qui porte les attributs de l'association.

- Logement (<u>num_logement</u>, code_adresse, complement_adresse, type_logement)
- Foyer (<u>num_foyer</u>, nom_titulaire, telephone, courriel)
- Occupation (<u>#num_foyer, #num_logement</u>, date_arrivee, date_depart)
- Bac (<u>num_bac</u>, num_puce, volume_litres, date_mise_service, #num_logement)
- Tournee (<u>num_tournee</u>, date_tournee, secteur, immatriculation_camion)
- Levee (<u>num_levee</u>, date_levee, heure_levee, #num_bac, #num_tournee)
- Facture (<u>num_facture</u>, semestre, date_emission, montant, #num_foyer)

Le numéro de bac devient une clé étrangère de la table des levées : une levée ne peut plus être enregistrée sans un bac connu. Une levée lue avec une puce inconnue est alors rejetée dans un journal et traitée à la source (puce remplacée à enregistrer), au lieu d'être « mise de côté ». Le numéro de puce, attribut du bac, doit être unique : c'est une contrainte du modèle physique.

**Réponses tolérées**
- Formalisme différent (notation « pattes de corbeau », schéma relationnel dessiné), s'il est lisible et cohérent (`JUR-T10`).
- Entité Camion distincte de la tournée, ou entité Adresse distincte du logement, si le modèle reste dans la limite de six entités ou si le candidat justifie la septième ; entité Occupation (1,1 vers le foyer et vers le logement) au lieu de l'association porteuse, si le modèle logique obtenu est équivalent.
- Date d'arrivée incluse dans la clé de l'occupation, pour admettre qu'un foyer revienne dans un logement qu'il a déjà occupé, si le candidat l'explique.
- Facture rattachée aussi au logement, ou lignes de facture par levée, si une règle est posée en hypothèse.
- Date et heure de la levée réunies en un seul horodatage.

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dessinées dans le modèle conceptuel, ou modèle logique qui ne découle pas du modèle conceptuel.
- *Bac rattaché au foyer* — le défaut de l'annexe 2.1 B reproduit dans le modèle corrigé : c'est précisément ce qui crée les doublons et les factures adressées aux anciens occupants.
- *Puce retenue comme identifiant du bac* — contraire à RG4 : un remplacement de puce rendrait de nouveau les levées orphelines.
- *Table d'occupation oubliée* — association n:m traduite par une clé étrangère simple, qui fait perdre l'historique des occupants ; dates d'arrivée et de départ placées dans la table du foyer.
- *Morceau de cours ou requête hors attente* (`JUR-T01`, `JUR-T07`) — règles de passage récitées sans les appliquer, ou requêtes écrites alors que la question n'en demande pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, modèle logique, modèle physique ; règles de passage ; lecture des cardinalités | définitions et méthode | F07 § 1 à 4 | notion de cours |

---

### 2.2 – L'architecture des données et le référentiel des adresses et des logements (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) ». Entrepôt, lac, architecture « lakehouse » et référentiel de données maîtres : comparaison et choix justifié ; aucune expertise des infrastructures (serveurs, réseaux), aucun choix de produit.
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) », mobilisée pour la gouvernance du lac et les responsabilités du référentiel (propriétaire, intendant).

**Annexes mobilisées** : annexes 1.1 (territoire, 30 communes, système d'information, direction du numérique mutualisée), 2.1 (anomalies d'adresses), 2.2 (données à réunir, deux options, positions), 2.4 D (durées de conservation) et 2.6 (Data Act, DAMA-DMBOK).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Entrepôt et lac de données définis et distingués ; premier critère (volume et variété) appliqué aux deux options | 0,5 |
| a-2 | Deuxième et troisième critères (qualité et historique, usages) appliqués aux deux options | 0,5 |
| a-3 | Recommandation argumentée (option B, lac associé à un entrepôt, en deux étapes) et deux conditions, dont la gouvernance qui évite le « marécage » et le respect des durées de conservation | 0,5 |
| b-1 | Données de référence définies ; référentiel des adresses et des logements justifié par les anomalies et par le rôle des communes ; deux règles de fonctionnement | 0,5 |

**Réponse attendue**

*2.2 a) – Les deux options*

**Définitions** : un **entrepôt de données** est une base orientée sujet, intégrée, historisée et non volatile, structurée pour l'analyse (faits et dimensions) ; ses données sont nettoyées et mises en forme avant leur chargement (schéma défini à l'écriture). Un **lac de données** stocke des données brutes et hétérogènes (structurées, textes, images, mesures de capteurs), dont la structure n'est définie qu'à la lecture, pour l'exploration ; sans gouvernance, il devient un « marécage » de données inutilisables. Les deux se complètent plus qu'ils ne s'opposent ; une architecture **« lakehouse »** les réunit sur une même plateforme (F07 § 1 et 6).

**Comparaison** (0,5 pt pour le premier critère avec les définitions, 0,5 pt pour les deux autres) :

| Critère | Option A : entrepôt de données classique | Option B : lac associé à un entrepôt (ou « lakehouse ») et référentiel |
|---|---|---|
| Volume et variété des données | adapté aux données structurées (2 millions de levées, 300 000 passages, tonnages, factures), dont le volume reste modeste ; mais il écarte la variété : les mesures horaires des 300 capteurs sont réduites à une moyenne journalière, les textes des réclamations et les photographies des dépôts sauvages ne sont pas repris | accueille toutes les formes de données : mesures en continu (environ 2,6 millions par an), textes, photographies géolocalisées, tableurs des communes et du syndicat ; c'est la **variété** plus que le volume qui justifie le lac |
| Qualité et historique | données nettoyées avant chargement, donc indicateurs fiables ; mais la cause des anomalies demeure, les adresses étant toujours rapprochées à la main à partir des fichiers des communes ; seuls les extraits mensuels sont historisés : si une règle change (méthode des refus de tri, tonnages de 2024 reconstitués), on ne peut pas recalculer | conserve les données brutes et leur historique, ce qui permet de recalculer une série après un changement de méthode ; le **référentiel des adresses et des logements** traite la cause des doublons et des levées non rattachées ; en revanche, la qualité n'est pas garantie par l'outil : sans règles, le lac accumule des données non documentées |
| Usages attendus | le rapport trimestriel et les tableaux de bord récurrents (tonnages, levées par commune) | les mêmes tableaux de bord, plus l'**analyse exploratoire** des effets de report (dépôts sauvages, colonnes de verre pleines, réclamations : question 2.3), la publication des données du territoire (question 2.4) et le partage avec les communes |

On retient aussi que l'option A est plus rapide (neuf mois contre quinze) et que la direction du numérique sait la mettre en œuvre, ce qui réduit le risque de projet.

**Recommandation : l'option B, dans sa forme « lac associé à un entrepôt »** (0,5 pt), parce qu'elle seule réunit les données nécessaires aux objectifs de « Castelrive 2032 » (pilotage par les données, ouverture des données du territoire, baisse des ordures ménagères résiduelles mesurée avec ses effets de report) et qu'elle traite, par le référentiel, la cause des anomalies de l'annexe 2.1. Deux conditions, parmi :
- **procéder en deux étapes**, en commençant par le référentiel et l'entrepôt des données de la redevance, qui répondent aux besoins urgents (facturation fiable, rapport aux élus), puis le lac pour les capteurs, les réclamations et les photographies : on limite ainsi le risque lié aux compétences de l'équipe, qui penche pour l'option A ;
- **gouverner le lac dès le départ** : un propriétaire et une description (catalogue, dictionnaire de données) pour chaque source, des droits d'accès, une qualité contrôlée à l'entrée, faute de quoi il devient un marécage (DAMA-DMBOK : architecture des données, métadonnées, qualité, annexe 2.6) ;
- **respecter les durées de conservation** : « conserver toutes les données brutes avec leur historique » ne vaut pas pour les données personnelles ; les levées détaillées doivent être détruites deux ans au plus après l'émission de la facture, seuls des agrégats par commune et par mois étant conservés au-delà (annexe 2.4 D) ;
- **récupérer les données des capteurs** : le fabricant les garde sur sa plateforme et facture l'export de l'historique ; le Data Act donne à l'utilisateur d'un produit connecté un droit d'accès aux données que génère son utilisation (annexe 2.6) : les conditions d'accès, y compris les frais d'export de 15 k€ par an, sont à discuter avec le fabricant au regard de ce droit, sans analyse juridique ici.

*2.2 b) – Le référentiel des adresses et des logements*

**Définition** (0,5 pt avec la justification et les règles) : les **données de référence** (ou données maîtres) sont des données partagées et stables, utilisées par plusieurs processus et plusieurs applications ; elles sont gérées dans un **référentiel unique**, qui fait foi, et que les autres applications consultent au lieu d'en tenir leur propre copie (F07 § 1).

**Justification** : l'adresse et le logement sont utilisés par la facturation, par les déchèteries (accès des foyers et des professionnels), par les tournées de collecte et par les analyses par commune ; ils sont créés par les **communes**, qui connaissent les premières les nouvelles adresses et les nouveaux logements. Or chacune les tient à sa façon, et 6 communes n'ont pas de liste à jour. Un référentiel partagé supprime la cause des 2 000 doublons et d'une grande partie des 40 000 levées non rattachées. Il permet aussi d'attribuer chaque levée au bon logement, donc au bon occupant, et de produire des données par commune comparables d'un service à l'autre.

**Deux règles de fonctionnement**, parmi :
- **une seule source** : une adresse ou un logement n'est créé, modifié ou fermé que dans le référentiel, et jamais dans le logiciel de facturation ou dans celui des déchèteries, qui le consultent ;
- **des responsabilités partagées** : chaque commune est responsable de ses adresses et de ses logements (propriétaire local), l'agglomération les valide et contrôle les doublons (intendant), dans un délai fixé, par exemple dès l'attribution d'une nouvelle adresse ; les communes sans liste à jour sont accompagnées ;
- **un identifiant unique, non signifiant et stable** pour chaque logement, jamais réattribué, avec un format commun de l'adresse (numéro, voie choisie dans une liste, complément : bâtiment, étage, porte) ;
- **un historique** : chaque adresse et chaque logement portent une date de création et, le cas échéant, de fermeture ; les changements sont tracés, et des indicateurs de qualité (doublons, adresses incomplètes) sont suivis.

**Réponses tolérées**
- Option A recommandée, si le candidat la justifie par la simplicité, le délai et les compétences disponibles, l'accompagne du référentiel des adresses et des logements et prévoit d'y ajouter plus tard les données non structurées.
- Option B retenue sous sa forme « lakehouse », si la gouvernance commune et le respect des durées de conservation sont traités.
- Autres critères ou conditions tirés des annexes (délai, compétences, dépendance envers le fabricant des capteurs).
- Référentiel présenté comme une démarche de gestion des données de référence (données maîtres), si le sigle anglais est écrit en toutes lettres (`ET-13`).

**Erreurs fréquentes**
- *Entrepôt et lac confondus* (`ET-24`) — lac présenté comme un « entrepôt moderne », ou entrepôt comme une simple grosse base.
- *Choix technique hors attente* (`JUR-T07`) — serveurs, capacités de stockage, logiciels ou produits du marché détaillés, alors que l'expertise des infrastructures est exclue.
- *Lac sans gouvernance* — « tout garder » sans propriétaires ni description, et sans regard pour les durées de conservation des données personnelles.
- *Référentiel sans les communes* — référentiel tenu par la seule agglomération, alors que les communes créent les adresses : la cause des anomalies demeure.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines architecture des données, données de référence et données maîtres, métadonnées, qualité | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Règlement (UE) 2023/2854 (Data Act), applicable depuis le 12/09/2025 | accès de l'utilisateur aux données des capteurs (annexe 2.6) | `data_act` / F07 § 8.5 | en vigueur |
| Entrepôt, lac de données, architecture « lakehouse », données de référence | définitions et comparaison | F07 § 1 et 6 | notion de cours |

---

### 2.3 – L'effet de la redevance incitative (4 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Aucun calcul statistique ni aucune manipulation d'outil ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexes 1.1 (territoire, redevance, effectif, « Castelrive 2032 » dans la présentation), 2.2 (sources), 2.3 (indicateurs 2024 et 2026, affirmation du vice-président, limites) et, pour la conclusion, 2.1 (levées non rattachées concentrées dans la ville-centre).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Collecte et nettoyage appliqués aux sources et aux limites des annexes (doublons, ruptures de méthode, données de 2024 reconstituées, signalements hétérogènes) | 0,5 |
| a-2 | Structuration (faits, dimensions, définitions communes), analyse et restitution appliquées ; rôles | 0,5 |
| b-1 | Analyses descriptive et exploratoire définies et distinguées, prédictive écartée ; combinaison justifiée par l'annexe 2.3 | 0,5 |
| b-2 | Premier constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-3 | Deuxième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-4 | Troisième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| c-1 | Affirmation appréciée : ordures ménagères résiduelles et déchets confondus, causalité non établie (biais), effets de report, base de l'objectif non fixée ; formulation juste proposée | 0,5 |
| c-2 | Deux représentations adaptées aux élus, chacune justifiée par son message et assortie d'un piège évité | 0,5 |

**Réponse attendue**

*2.3 a) – La chaîne de traitement*

La **chaîne de traitement** transforme des données brutes en informations utiles à la décision ; c'est une démarche, et non un outil (F08 § 1). Pour mesurer l'effet de la redevance :
- **collecte** (0,5 pt avec le nettoyage) : extraction automatique des levées avec leur heure, leur tournée et leur camion (et non plus la seule date gardée par le logiciel de facturation), des passages et des pesées des déchèteries, des mesures des capteurs (à obtenir du fabricant), des tonnages et des refus de tri du syndicat, chaque mois malgré deux mois de retard, des réclamations, des signalements de dépôts sauvages (application de la ville et tableur des mairies) ; on y ajoute les données de contexte qui manquent aujourd'hui : population de chaque commune, résidences secondaires, liste des professionnels passés à un collecteur privé ;
- **nettoyage** : dédoublonnage des foyers et rattachement des levées aux bacs et aux logements à l'aide du référentiel (question 2.2 b) ; repérage des valeurs manquantes et aberrantes ; **signalement des ruptures de série** (méthode des refus de tri changée en 2025, signalements comptés autrement dans la ville-centre depuis l'application) ; marquage des tonnages de 2024 comme **reconstitués** ; journal des rejets et correction à la source ;
- **structuration** (0,5 pt avec l'analyse et la restitution) : chargement dans l'entrepôt de faits (levées, tonnages, passages, signalements, réclamations), à un grain défini (le mois, la commune, le flux), selon des dimensions communes (date, commune et type de commune, flux de déchets, type de logement, foyer ou professionnel) et des **définitions écrites** dans le dictionnaire de données : ce qu'est une ordure ménagère résiduelle collectée, un habitant (avec ou sans les résidences secondaires), un refus de tri ;
- **analyse** : descriptive, puis exploratoire (question b) ;
- **restitution** : tableau de bord trimestriel des élus (question 2.5 b), tableau de bord détaillé de la direction de la collecte, données publiées sur le portail (question 2.4), chaque fois avec les sources, les dates et les limites ; puis **décision** et actions de prévention.

Le chargé d'études conçoit et documente la chaîne ; les directions qui produisent les données en sont propriétaires et valident les définitions ; la direction du numérique en assure l'exploitation ; la déléguée à la protection des données est consultée sur les données personnelles.

*2.3 b) – La méthode et trois constats*

**La méthode** (0,5 pt) : l'**analyse descriptive** résume ce qui s'est passé (niveaux, évolutions, répartitions, écarts à un objectif) ; l'**analyse exploratoire** recherche, sans hypothèse arrêtée, des croisements, des profils et des valeurs atypiques qui orientent vers des explications ; l'**analyse prédictive** estime ce qui va se passer (F08 § 2). On retient :
- l'**analyse descriptive d'abord**, parce que les élus demandent ce qui a changé entre 2024 et 2026, et parce qu'il faut établir des chiffres fiables avant de les expliquer ;
- puis l'**analyse exploratoire**, pour chercher où sont allés les déchets et pourquoi les résultats diffèrent selon les communes : croiser la baisse des ordures ménagères résiduelles avec le tri, les déchèteries, les refus de tri et les dépôts sauvages ; rapprocher les contestations de factures de la qualité des données ;
- une analyse **prédictive** (l'atteinte de l'objectif de 2030) serait prématurée : deux années seulement, une base de 2024 reconstituée, des séries rompues en 2025.

**Trois constats** parmi les suivants (0,5 pt chacun : le fait chiffré, son interprétation au regard de « Castelrive 2032 », la précaution de lecture) :

1. **Les ordures ménagères résiduelles collectées ont nettement baissé, d'autant plus que la commune est petite.** Elles passent d'environ 42 000 à 34 000 tonnes, soit près d'un cinquième de moins ; par habitant, − 10 % dans la ville-centre (250 à 225 kg), − 20 % dans les communes moyennes (240 à 192 kg), − 30 % dans les communes rurales et périurbaines (220 à 154 kg). Les levées suivent la même pente : 24 par foyer et par an dans la ville-centre, 13 dans les communes rurales, à peine plus que le forfait de 12. *Précaution* : la base de 2024 est reconstituée à partir des pesées de camions dont les tournées traversent plusieurs communes, et la répartition par type de commune est donc fragile ; une partie de la baisse de la ville-centre vient du départ d'environ 500 professionnels vers un collecteur privé, dont les déchets ne sont plus comptés.
2. **La quantité totale de déchets par habitant n'a presque pas changé.** En additionnant ordures ménagères résiduelles, emballages et papiers et apports en déchèterie, on passe de 450 à 445 kg par habitant dans la ville-centre, de 505 à 502 kg dans les communes moyennes, de 520 à 524 kg dans les communes rurales. La redevance a donc surtout **déplacé** les déchets vers le tri (+ 10 à + 20 kg) et les déchèteries (+ 10 à + 50 kg) ; elle n'a pas, à ce stade, réduit les déchets produits. *Précaution* : les apports en déchèterie mêlent ceux des professionnels et les végétaux, sensibles à la météo ; les quantités par habitant ignorent les résidences secondaires, nombreuses dans dix communes rurales, qui gonflent les ratios de ces communes.
3. **Des effets de report apparaissent là où la baisse est la plus forte.** Dans les communes rurales, les refus de tri passent de 15 % à 28 % et les signalements de dépôts sauvages sont multipliés par quatre (100 à 400) : des ordures sont mises dans les bacs de tri ou déposées dans la nature pour éviter des levées. *Précaution* : le nouveau prestataire du centre de tri mesure les refus autrement depuis 2025 (rupture de série) ; les signalements ruraux dépendent des appels des mairies, et le triplement dans la ville-centre (300 à 900) tient en partie à l'application lancée en 2025, qui facilite le signalement : une hausse des signalements n'est pas forcément une hausse des dépôts. Une concomitance n'est pas une causalité.
4. **Les contestations de factures sont les plus nombreuses dans la ville-centre**, avec 260 pour 1 000 redevables contre 170 dans les communes rurales. Deux explications sont possibles. D'une part, les foyers y dépassent le plus le forfait (24 levées contre 13, pour un forfait de 12) et paient donc la part variable la plus élevée. D'autre part, la ville-centre concentre les trois quarts des levées non rattachées (annexe 2.1) : les contestations traduisent aussi la **qualité des données**. *Précaution* : on ne peut pas départager ces explications ; il n'existe aucune donnée de 2024, et les réclamations, en texte libre dans un tableur, ne sont pas classées par motif.

*2.3 c) – L'affirmation du vice-président et deux représentations*

**L'affirmation de M. BASTÉROLE** (0,5 pt) : « la redevance a fait baisser nos déchets de 20 % » est à corriger sur quatre points :
- **ce qui a baissé**, ce sont les ordures ménagères résiduelles collectées, d'environ un cinquième (42 000 à 34 000 tonnes), et non « nos déchets » : leur total par habitant est stable (constat 2) ;
- **la cause n'est pas établie** : la redevance est la cause la plus plausible, mais la comparaison ne porte que sur deux années, sans groupe de comparaison, sur une base reconstituée, avec le départ de professionnels et des changements de mesure ; un élu qui porte la réforme est exposé au **biais de confirmation**, qui consiste à retenir le chiffre qui conforte sa conviction ;
- **les effets de report** (tri moins bon, dépôts sauvages, apports en déchèterie) ont un coût : le ramassage des dépôts sauvages occupe l'équivalent de trois agents (annexe 2.5) ;
- **l'objectif de « Castelrive 2032 »** (− 15 % d'ici 2030), adopté en janvier 2027, n'indique pas son année de référence : s'il part de 2026, il reste entièrement à atteindre ; s'il part de 2024, la baisse affichée doit encore être confirmée.

Formulation proposée au conseil : « Depuis la redevance, les ordures ménagères résiduelles collectées ont baissé d'environ un cinquième, surtout dans les communes rurales. Une partie s'est reportée vers le tri, les déchèteries et des dépôts sauvages, et la quantité totale de déchets n'a pas diminué. L'objectif de 2030 doit être mesuré à partir d'une base que nous fixons aujourd'hui. »

**Deux représentations** (0,5 pt), parmi :
- **Barres empilées par type de commune, en 2024 et en 2026**, des kilogrammes par habitant d'ordures ménagères résiduelles, d'emballages et papiers et d'apports en déchèterie. *Message* : la hauteur totale ne change presque pas, seule sa composition change. *Piège évité* : axe partant de zéro, quantités par habitant plutôt qu'en tonnes, pour comparer des communes de tailles différentes.
- **Courbe des ordures ménagères résiduelles collectées** par habitant, avec la **trajectoire de l'objectif** de − 15 % tracée depuis l'année de référence retenue. *Message* : où en est-on de l'objectif, et ce qui reste à faire. *Piège évité* : le point de 2024 est signalé comme reconstitué, et l'année de référence est écrite.
- **Barres groupées des refus de tri et des signalements de dépôts sauvages** par type de commune, en 2024 et en 2026. *Message* : les effets de report sont les plus forts dans les communes rurales. *Piège évité* : une mention de la rupture de méthode de 2025 et du lancement de l'application dans la ville-centre.
- **Carte des communes** colorée selon la baisse des ordures ménagères résiduelles par habitant, ou selon les levées par foyer. *Message* : la géographie de l'effet de la redevance. *Piège évité* : une carte en taux et non en tonnes, qui ferait ressortir la seule ville-centre.

Un chiffre isolé de « − 20 % » en grand caractère, ou un histogramme dont l'axe est tronqué pour accentuer la baisse, sont de mauvais choix.

**Réponses tolérées**
- Chaîne de traitement présentée avec l'extraction, la transformation et le chargement comme étape intermédiaire, si les cinq étapes de la question sont couvertes.
- Analyse diagnostique présentée comme une variante de l'analyse exploratoire.
- Autres constats tirés de l'annexe 2.3 (levées par foyer selon le type de commune, hausse des apports en déchèterie), s'ils sont chiffrés et assortis d'une précaution ; baisse globale lue comme « environ 20 % » ou « 19 % ».
- Constat sur les contestations de factures expliqué par la seule part variable plus élevée dans la ville-centre, ou par la seule qualité des données, si l'explication est argumentée.
- Autres représentations adaptées aux élus (jauge de l'objectif, petits multiples par type de commune), si le message et le piège évité sont précisés.

**Erreurs fréquentes**
- *Corrélation présentée comme une causalité* (`ET-26`) — baisse des ordures ménagères résiduelles imputée à la seule redevance, ou hausse des signalements prise pour une hausse des dépôts.
- *Prudence d'interprétation oubliée* (`JUR-D06`) — base de 2024 reconstituée et ruptures de méthode ignorées, objectif de 2030 jugé atteint sans année de référence.
- *Informatique décisionnelle réduite à un outil* (`ET-05`, `JUR-D02`) — logiciel de tableaux de bord proposé sans la chaîne de traitement ni les définitions communes.
- *Calcul hors attente* (`JUR-T07`) — moyennes pondérées ou tests statistiques, alors que la question demande des constats argumentés en chiffres ronds.
- *Morceau de cours* (`JUR-T01`) — définitions des méthodes d'analyse sans les appliquer aux communes et aux années de l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement, analyses descriptive, exploratoire et prédictive, choix des graphiques, biais de lecture, corrélation et causalité | définitions et méthode | F08 § 1, 2 et 5 | notion de cours |
| Faits, dimensions, grain, dictionnaire de données | structuration | F07 § 1 et 6 | notion de cours |

---

### 2.4 – L'ouverture et la valorisation des données (2,5 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression » ; `2.3.e` « Aspects réglementaires (RGPD, archivage légal) et monétisation des données ». Délégué à la protection des données et registre des traitements, archivage, monétisation analysée de façon critique ; le principe d'ouverture des données publiques est donné par l'énoncé ; ni prérogatives des usagers sur leurs données, ni fondement juridique des traitements, ni pouvoirs de l'autorité de contrôle (UE 1), ni analyse juridique.

**Annexes mobilisées** : annexes 1.1 (collectivités, direction du numérique mutualisée), 2.2 (capteurs, signalements), 2.4 (règle d'ouverture, six jeux de données, proposition de KOMPAVEL, délégué à la protection des données, durées de conservation) et 2.6 (RGPD, anonymisation, monétisation, Data Governance Act).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Anonymisation et pseudonymisation définies et distinguées ; jeux J1, J2 et J6 publiables, avec leurs conditions | 0,5 |
| a-2 | Jeux J3, J4 et J5 appréciés selon les trois critères : J3 non publiable tel quel, J4 publiable avec un seuil, J5 publiable après retrait des éléments identifiants | 0,5 |
| b-1 | Proposition de KOMPAVEL appréciée de façon critique (données personnelles non anonymisables pour cet usage, finalité, monétisation, exclusivité, confiance, prix dérisoire) ; recommandation | 0,5 |
| c-1 | Rôle du DPO mutualisé (missions, désignation commune possible) et deux points à corriger (conflit d'intérêts, rattachement, moyens, consultation, registre) | 0,5 |
| c-2 | Cycle de vie et règles de conservation et d'archivage appliquées aux données de la redevance, écarts aux pratiques actuelles corrigés | 0,5 |

**Réponse attendue**

*2.4 a) – Les six jeux de données*

**Définitions** (0,5 pt avec J1, J2 et J6) : l'**anonymisation** rend impossible, en pratique et de façon irréversible, l'identification des personnes ; les données anonymisées ne sont plus des données personnelles. La **pseudonymisation** remplace les éléments directement identifiants (nom, numéro de foyer) par un pseudonyme : la personne reste identifiable par recoupement, et les données restent personnelles (annexe 2.6 ; F07 § 8.6). Une donnée qui permet d'identifier une personne indirectement, comme l'adresse d'un logement individuel, est une donnée personnelle.

| Jeu | Publication | Conditions et justification |
|---|---|---|
| J1 – tonnages mensuels par commune et par flux | **oui** | données agrégées par commune et par flux, qui ne se rapportent à aucun foyer ; publiées dans un format ouvert, avec une description : tonnages de 2024 reconstitués, rupture de méthode des refus de tri en 2025 |
| J2 – colonnes de verre et taux de remplissage | **oui** | mesures de capteurs sur des équipements publics, sans donnée personnelle ; l'agglomération doit d'abord obtenir les données auprès du fabricant (annexe 2.2) |
| J6 – horaires et fréquentation des déchèteries par tranche horaire | **oui** | décomptes de passages agrégés, sans numéro de badge ni plaque d'immatriculation |
| J3 – levées par bac avec l'adresse, la date et l'heure | **non, tel quel** | l'adresse d'un logement désigne un foyer (individualisation, même sans le nom : un simple pseudonyme du bac n'y change rien) ; on peut la relier à d'autres sources (corrélation) ; les dates et heures révèlent les habitudes et les absences (inférence), ce qui fait aussi courir un risque aux occupants ; seul un agrégat par commune ou par quartier et par mois peut être publié |
| J4 – levées moyennes par foyer, par commune et par semestre | **oui, avec un seuil** | moyenne sur au moins 80 foyers dans la plus petite commune : aucun foyer n'est isolé ; la publication à la rue est exclue (40 rues de moins de cinq logements, où l'on pourrait déduire le comportement d'un foyer) ; un seuil minimal de foyers par case est fixé, et les petites communes sont regroupées si nécessaire |
| J5 – signalements de dépôts sauvages | **oui, après retrait des éléments identifiants** | les photographies montrant des personnes, des plaques ou des courriers nominatifs identifient des personnes ; les commentaires peuvent désigner un auteur supposé, ce qui revient à publier un soupçon (inférence) ; on publie la date, la commune ou le quartier, une position arrondie hors des domiciles et la nature des déchets, sans photographie ni commentaire |

(0,5 pt pour J3, J4 et J5.) Avant publication, la déléguée à la protection des données vérifie les trois critères, et chaque jeu publié est décrit (définition, source, fréquence de mise à jour, limites).

*2.4 b) – La proposition de KOMPAVEL*

**Appréciation critique** (0,5 pt avec la recommandation), en quatre arguments parmi :
- **un fichier de données personnelles qu'on ne peut pas anonymiser pour cet usage** : nom, adresse et nombre de levées par mois décrivent le comportement de chaque foyer ; le ciblage commercial exige précisément d'identifier les foyers (individualisation), si bien que l'anonymisation viderait l'offre de son intérêt ;
- **une autre finalité** : les levées sont collectées pour facturer la redevance ; les céder pour une prospection commerciale par une entreprise est une finalité différente, a priori incompatible avec la finalité initiale (annexe 2.6), et les usagers y verraient une surveillance de leurs poubelles : la **confiance** dans la redevance, déjà contestée, en souffrirait, avec un risque pour l'image de l'agglomération ;
- **la monétisation des données personnelles a des limites** : une personne ne peut ni céder la propriété de ses données ni renoncer à ses garanties (annexe 2.6) ; l'agglomération n'est pas « propriétaire » des données des foyers et ne peut pas les vendre comme une marchandise ;
- **l'exclusivité** demandée pendant trois ans va à l'encontre du principe, posé par le Data Governance Act, selon lequel les accords qui accordent un droit exclusif de réutilisation de données protégées détenues par le secteur public sont en principe interdits ; elle favoriserait aussi une entreprise au détriment des autres, à l'inverse de l'ouverture décidée par le conseil ;
- **un gain dérisoire et une logique fragile** : 30 k€ par an, soit moins de 40 centimes par foyer, au regard du risque pris ; et un foyer qui présente souvent son bac n'est pas forcément celui qui produit le plus de déchets ou qui peut composter (volume du bac, taille du foyer, appartement sans jardin).

**Recommandation** : refuser la vente du fichier, et répondre à l'intérêt réel de la proposition, la prévention, autrement : publier les données agrégées (J1, J4), utilisables par KOMPAVEL comme par toute autre entreprise ; conduire, au besoin, une campagne de compostage portée par l'agglomération elle-même, auprès de tous les foyers ou des communes où les levées sont les plus nombreuses, sans transmettre de fichier nominatif ; consulter la déléguée à la protection des données avant toute nouvelle utilisation des données de la redevance.

*2.4 c) – Le délégué à la protection des données mutualisé, la conservation et l'archivage*

**Le rôle du délégué** (0,5 pt avec deux points à corriger) : la désignation d'un délégué à la protection des données est obligatoire pour l'agglomération comme pour la ville, organismes publics ; un **même délégué** peut être désigné pour les deux, compte tenu de leur structure et de leur taille, ce qui est cohérent avec la direction du numérique mutualisée (annexe 2.6). Le délégué **informe et conseille** les deux collectivités et leurs agents, **contrôle** le respect du règlement (registre, durées de conservation, sous-traitants), conseille les projets dès leur conception et coopère avec l'autorité de contrôle. Il n'est pas responsable du traitement : c'est l'agglomération qui l'est, pour la redevance, et qui tient son registre avec son aide (F15 § 1 et 2).

**Deux points à corriger**, parmi :
- **le conflit d'intérêts** : Mme VILLEROUSSE a été cheffe du projet du logiciel de facturation, dont elle a contribué à fixer les moyens ; elle ne peut pas contrôler en toute indépendance un traitement qu'elle a conduit. Ses missions doivent être séparées de la conduite de projets ;
- **le rattachement** : rattachée au directeur du numérique mutualisé, qui décide des moyens des traitements, elle ne peut pas lui rendre compte de leur conformité ; elle doit rendre compte au plus haut niveau de chacune des deux collectivités (les directions générales) ;
- **les moyens** : un mi-temps pour deux collectivités, dont l'une emploie 1 100 agents et tient 35 fiches de registre, avec des projets de données d'envergure, ne suffit pas ; on peut prévoir des référents dans les directions ;
- **sa consultation** : elle n'a été consultée ni sur les options d'architecture ni sur la proposition de KOMPAVEL, alors que la protection des données doit être prise en compte dès la conception ;
- **le registre** : la fiche de la redevance, de 2023, est à mettre à jour (levées horodatées, hébergement chez l'éditeur, qui agit comme sous-traitant, échanges avec les communes, entrepôt et lac, publication de données, durées de conservation).

**La conservation et l'archivage** (0,5 pt) : le cycle de vie des données comprend leur **création**, leur **stockage**, leur **usage**, leur **archivage** et leur **suppression** ; à chaque catégorie de données sont associées une durée d'utilité courante, une durée de conservation et un sort final (F07 § 8.4). Appliqué à la redevance :
- **les levées détaillées** sont détruites deux ans au plus après l'émission de la facture qu'elles justifient ; au-delà, seules des données agrégées par commune et par mois sont conservées pour l'analyse. Les levées qui justifient les premières factures, émises en 2025, atteignent ce délai dès 2027 : la purge doit être programmée maintenant. Le logiciel de l'éditeur, qui garde tout depuis 2025, doit être purgé, et la règle s'impose aussi au futur lac de données ;
- **les factures** restent deux ans dans le logiciel de facturation, puis passent en **archivage intermédiaire** (accès restreint, intégrité garantie) jusqu'à dix ans après leur émission, avant une destruction tracée ;
- **les fiches des foyers partis** sont détruites deux ans après le départ et le paiement de la dernière facture, une fois les doublons fusionnés ;
- **les tonnages annuels et les rapports aux élus** sont conservés définitivement dans les archives de l'agglomération ;
- **les copies non maîtrisées** sont supprimées : le tableur des réclamations est purgé selon les mêmes durées, et les extractions de levées conservées dans les messageries sont effacées, puis remplacées par un partage sécurisé, limité aux données nécessaires aux communes ;
- **le contrat avec l'éditeur** doit prévoir les purges sur instruction de l'agglomération et la restitution des données à son terme, en 2029.

Le service de la facturation, propriétaire des données, décide de ces règles avec l'archiviste ; la direction du numérique les met en œuvre ; la déléguée à la protection des données en contrôle l'application.

**Réponses tolérées**
- J4 jugé publiable sans seuil, si le candidat montre que la plus petite commune compte encore 80 foyers ; J2 jugé publiable avec un délai ou une moyenne horaire.
- J5 jugé non publiable, si le candidat propose une version agrégée (nombre de signalements par commune et par mois).
- Recommandation d'une convention de prévention avec plusieurs entreprises, sans transmission de données nominatives, après avis du délégué.
- Autres points à corriger tirés de l'annexe 2.4 C, s'ils sont justifiés.
- Cycle de vie présenté en sept étapes (collecte, stockage, traitement, partage, archivage, destruction…), si les durées de l'annexe sont appliquées.

**Erreurs fréquentes**
- *Anonymisation et pseudonymisation confondues* — fichier des levées jugé publiable une fois le nom ou le numéro du bac retirés, alors que l'adresse et les heures suffisent à identifier le foyer.
- *Monétisation présentée sans regard critique* (programme 2.3, limite : « la monétisation doit être abordée de façon critique ») — « 30 k€ de recettes » acceptés sans examiner la finalité, la confiance des usagers et l'exclusivité.
- *Délégué confondu avec le responsable du traitement ou avec le RSSI* (`ET-29`, `JUR-D05`) — délégué présenté comme celui qui « décide » des traitements, ou mutualisation jugée impossible.
- *Analyse juridique hors programme* (`JUR-T07`) — développement sur les prérogatives des usagers sur leurs données, les fondements juridiques des traitements ou les pouvoirs de l'autorité de contrôle, au lieu de l'application des repères fournis.
- *Durées inventées ou discutées* — remise en cause des durées de l'annexe 2.4 D, qui sont données.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | donnée personnelle, finalité, minimisation, conservation, registre, délégué (désignation commune, missions, conflit d'intérêts) | `rgpd` / F15 § 1 et 2 | en vigueur |
| Proposition « omnibus numérique » du 19/11/2025 | projet, non applicable | `omnibus_numerique_donnees` / F15 § 8 | projet |
| Publication de l'autorité de contrôle sur l'anonymisation, 19/05/2020 | trois critères : individualisation, corrélation, inférence ; pseudonymisation | `cnil_anonymisation_2020` / F07 § 8.6 | publiée |
| Publication de l'autorité de contrôle sur la monétisation, 17/11/2025 | limites de la monétisation des données personnelles | `cnil_monetisation_2025` / F07 § 8.6 | publiée |
| Règlement (UE) 2022/868 (Data Governance Act), applicable depuis le 24/09/2023 | réutilisation des données protégées du secteur public, exclusivité en principe interdite | `dga` / F07 | en vigueur |
| Cycle de vie des données, archivage intermédiaire et définitif | règles de conservation appliquées | F07 § 8.4 | notion de cours |

---

### 2.5 – Le coût du dispositif numérique de la redevance et son pilotage (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ». Total de tête en sommes rondes ; aucun calcul actualisé, aucune règle de finances locales.

**Annexes mobilisées** : annexes 1.1 (78 000 foyers et 6 000 professionnels redevables, collecte), 2.1 (rapprochement manuel des levées, factures erronées), 2.2 (export des données des capteurs), 2.3 (dépôts sauvages) et 2.5 (coûts de 2026, contrat avec l'éditeur, rapport trimestriel).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Coût complet défini ; 840 k€ / 84 000 redevables = 10 € par redevable et par an ; poids du temps du service | 0,5 |
| a-2 | Deux coûts cachés tirés des annexes, chacun expliqué | 0,5 |
| b-1 | Indicateur de coût complet, avec ses cinq champs | 0,5 |
| b-2 | Indicateur de risque complet, avec ses cinq champs ; complémentarité avec les tonnages du rapport actuel | 0,5 |

**Réponse attendue**

*2.5 a) – Le coût par redevable et deux coûts cachés*

**Le coût complet** (0,5 pt avec le calcul) : le **coût complet**, ou coût total de possession (TCO), d'un système d'information réunit tous les coûts supportés sur sa durée de vie : acquisition ou abonnement, exploitation et maintenance, matériel, personnel interne, support, formation, et jusqu'à la sortie (restitution des données, migration) ; il comprend des coûts directs, des coûts indirects et des coûts cachés, et ne se réduit pas au prix du logiciel (F09 § 3.1).

**Le calcul, de tête** : 240 + 80 + 40 + 20 + 100 + 360 = **840 k€** par an ; pour 78 000 foyers et 6 000 professionnels, soit **84 000 redevables** : 840 000 € / 84 000 = **10 € par redevable et par an**. Le premier poste est le **temps du service** de la facturation et des réclamations (360 k€, plus de 40 % du total), devant l'abonnement au logiciel (240 k€) : une grande partie du coût est humaine, et elle dépend directement de la qualité des données, puisque les doublons, les levées non rattachées et les factures adressées à d'anciens occupants alimentent les réclamations.

**Deux coûts cachés** (0,5 pt), parmi ceux que la comptabilité analytique ne rattache pas au dispositif :
- **le rapprochement manuel des levées non rattachées** : deux agents de la direction de la collecte y consacrent chacun une journée par semaine, soit une centaine de journées par an, comptées dans la collecte et non dans le dispositif (annexe 2.1) ;
- **la sortie du contrat avec l'éditeur** : le contrat, qui prend fin en 2029, ne prévoit pas la restitution des données ; leur récupération et leur reprise dans un nouveau logiciel auront un coût, qui n'est pas provisionné (réversibilité) ;
- **le traitement des factures erronées** : 1 700 factures adressées à des foyers partis entraînent des annulations, de nouvelles factures et des relances, ainsi qu'une perte de confiance des usagers ;
- **les effets de report de la redevance** : le ramassage des dépôts sauvages mobilise l'équivalent de trois agents des services techniques (annexe 2.5) ; c'est un coût indirect de la politique plutôt que du dispositif numérique, à signaler aux élus ;
- **l'accès aux données des capteurs**, facturé 15 k€ par an par le fabricant pour l'export de l'historique, dès lors que ces données doivent être réunies avec celles de la redevance (annexe 2.2) ; montant à discuter avec le fabricant au regard du droit d'accès du Data Act (annexe 2.6).

*2.5 b) – Deux indicateurs pour compléter le rapport trimestriel*

Le rapport actuel ne mesure que la **performance** (tonnages). Les deux indicateurs proposés y ajoutent le **coût** et le **risque**, pour équilibrer le pilotage, comme le demande Mme VARSANGE (0,5 pt par indicateur complet) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Coût complet du dispositif numérique par redevable** | (coûts annuels du dispositif, y compris les coûts cachés identifiés : rapprochement manuel, traitement des factures erronées) / nombre de redevables actifs | comptabilité analytique (contrôle de gestion) et logiciel de facturation (redevables actifs) | trimestrielle, sur douze mois glissants | au plus 10 € par redevable en 2028, coûts cachés compris (10 € en 2026 sans eux) | financier |
| **Taux de levées non rattachées** | levées non rattachées à un bac affecté à un logement / levées lues × 100 | logiciel de facturation (journal des levées rejetées), puis entrepôt de données | mensuelle, présentée chaque trimestre | au plus 0,5 % fin 2027 (2 % en 2026) | processus |

Le premier suit l'**efficience** du dispositif : il doit baisser à mesure que la qualité des données réduit le temps de correction et de réclamation. Le second mesure le **risque** de facturer à tort, ou de ne pas facturer, et de perdre la confiance des usagers : il vérifie que le modèle corrigé et le référentiel des adresses produisent leur effet. Présentés à côté des tonnages, avec leur tendance et leur cible, ils remplacent une page de chiffres par un tableau de bord qui relie le coût, le risque et le résultat.

**Réponses tolérées**
- Coût par foyer seul (840 k€ / 78 000, un peu moins de 11 €), si l'hypothèse est écrite ; coût calculé hors temps du service (480 k€, soit un peu moins de 6 € par redevable), si le candidat le signale comme partiel.
- Autres coûts cachés tirés des annexes (formation des agents, temps de la déléguée à la protection des données, mise à jour du registre), s'ils sont expliqués.
- À la place de l'indicateur de risque : part des factures adressées à un foyer parti (factures adressées à un foyer parti / factures émises ; logiciel de facturation et référentiel des logements ; semestrielle ; au plus 0,2 % en 2028, environ 1 % en 2026 ; axe client) ; signalements de dépôts sauvages pour 10 000 habitants (signalements / population × 10 000 ; application de la ville et tableur des mairies ; trimestrielle ; en baisse chaque année à partir de 2027 ; axe environnement), qui mesure le risque d'effets de report. Comme indicateur complémentaire de performance seulement : délai de réponse aux réclamations sur les levées (somme des jours entre réception et réponse / réclamations ; tableur puis outil de suivi ; mensuelle ; au plus quinze jours ; axe client).

**Erreurs fréquentes**
- *Coût complet réduit au prix du logiciel* (`ET-33`) — seul l'abonnement de 240 k€ retenu, en oubliant le temps du service, qui pèse davantage.
- *Calcul hors attente* (`JUR-T07`) — actualisation ou retour sur investissement calculés, alors que la question demande un coût par redevable de tête.
- *Indicateur incomplet ou générique* (`ET-18`, `JUR-A02`) — « suivre les coûts » sans formule, source, fréquence, cible ni axe, ou deux indicateurs de tonnages qui doublent le rapport actuel.
- *Finances locales hors attente* — discussion du tarif de la redevance ou de son équilibre budgétaire, que la question n'appelle pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Coût complet (TCO), coûts directs, indirects et cachés, réversibilité | définition et calcul de tête | F09 § 3.1 | notion de cours |
| Indicateur à cinq champs, équilibre performance, risque et coût, axes du tableau de bord prospectif | deux indicateurs du rapport trimestriel | F08 § 3 ; F09 § 4 | notion de cours |
