# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 1 — Dossier 1 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F09 performance du SI, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle de données exécuté en SQLite, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Modélisation de l'entrepôt de pilotage | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) ; `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) | 5 |
| 1.2 Gouvernance des données | `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données | 4 |
| 1.3 Qualité des données | `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution | 4 |
| 1.4 Critique du tableau de bord mensuel | `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `3.1.e` Revue et amélioration continue des dispositifs de pilotage | 3 |
| **Dossier 1 – Gouverner et modéliser les données de pilotage** |  | **16** |

Répartition indicative : connaissances (définitions, règles de passage, référentiels) 3,5 points (items 1.1 b-1 et c-1, 1.2 a-1, a-2 et b-1, 1.3 a-1, 1.4 a-1) ; modélisation, analyse des annexes et recommandations 12,5 points. Durée conseillée : 16 points × 4,5 minutes ≈ 1 h 10.

---

### 1.1 – Modélisation de l'entrepôt de pilotage (5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) » ; `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) ».

**Annexes mobilisées** : annexes 1.2 (règles de gestion RG1 à RG6, objectif du projet Boussole) et 1.4 (attente de comparaison entre magasins).

**Barème indicatif (5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cinq entités avec identifiant souligné (Magasin, Produit, Famille, Fournisseur, Mois) | 0,5 |
| a-2 | Attributs élémentaires correctement placés, aucun attribut calculé ni clé étrangère dans le MCD | 0,5 |
| a-3 | Associations *appartenir* et *fournir* avec cardinalités justifiées par RG3 et RG4 | 0,5 |
| a-4 | Association ternaire *vendre* (Magasin, Produit, Mois) portant quantité vendue, chiffre d'affaires HT et quantité démarquée ; cardinalités 0,n / 0,n / 1,n justifiées par RG6 | 1 |
| b-1 | Règles de passage énoncées (entité → table ; association à cardinalité maximale 1 → clé étrangère ; association n-aire → table à clé composée) | 0,5 |
| b-2 | Table Produit avec deux clés étrangères | 0,5 |
| b-3 | Table Vente_mensuelle à clé composée de trois clés étrangères, avec les trois mesures | 0,5 |
| c-1 | Entrepôt défini et choix argumenté contre le lac de données (besoin de pilotage stable, données structurées, historique) | 0,5 |
| c-2 | Lecture en étoile : table de faits au grain mensuel, trois dimensions (magasin, produit, mois) dont le temps, mesures additives ; famille et fournisseur en flocon, ou dénormalisées dans Produit | 0,5 |

**Réponse indicative**

*1.1 a) – Modèle conceptuel des données*

Le MCD représente les objets de gestion (entités), leurs propriétés et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique.

Entités (identifiant en premier, souligné sur la copie) :
- MAGASIN (<u>code_magasin</u>, nom_magasin, ville, surface_vente, date_adhesion) – RG1 ;
- PRODUIT (<u>code_produit</u>, libelle_produit, code_ean, label) – RG2 ;
- FAMILLE (<u>code_famille</u>, libelle_famille) – RG3 ;
- FOURNISSEUR (<u>code_fournisseur</u>, raison_sociale, commune, type_fournisseur, distance_km) – RG4 ;
- MOIS (<u>code_mois</u>, annee, numero_mois, trimestre) – RG5 (0,5 pt pour les entités, 0,5 pt pour les attributs).

Associations et cardinalités :

```
FAMILLE (1,n) ---- appartenir ---- (1,1) PRODUIT (1,1) ---- fournir ---- (1,n) FOURNISSEUR

MAGASIN (0,n) ---- vendre [quantite_vendue, ca_ht, quantite_demarquee] ---- (0,n) PRODUIT
                                   |
                                 (1,n)
                                  MOIS
```

- *appartenir* : un produit appartient à une et une seule famille (1,1) ; une famille regroupe au moins un produit (1,n) – RG3 ;
- *fournir* : un produit est fourni par un et un seul fournisseur (1,1) ; un fournisseur fournit au moins un produit (1,n) – RG4 (0,5 pt) ;
- *vendre*, association ternaire : les trois mesures dépendent du couple magasin × produit × mois et ne peuvent être portées par aucune des trois entités ; un magasin qui vient d'adhérer peut n'avoir aucune vente (0,n), un produit peut n'être vendu nulle part un mois donné (0,n), chaque mois chargé comporte au moins une vente (1,n) – RG6 (1 pt).

*1.1 b) – Modèle logique des données*

Règles de passage (0,5 pt) : chaque entité devient une table dont l'identifiant est la clé primaire ; pour une association binaire dont une patte a une cardinalité maximale de 1 (*appartenir*, *fournir*), l'identifiant de l'entité côté n migre comme clé étrangère dans la table côté 1 (non nulle, puisque la cardinalité minimale est 1) ; une association ternaire devient une table dont la clé primaire est la concaténation des trois identifiants, chacun clé étrangère, et qui porte les attributs de l'association.

- Magasin (<u>code_magasin</u>, nom_magasin, ville, surface_vente, date_adhesion)
- Famille (<u>code_famille</u>, libelle_famille)
- Fournisseur (<u>code_fournisseur</u>, raison_sociale, commune, type_fournisseur, distance_km)
- Produit (<u>code_produit</u>, libelle_produit, code_ean, label, #code_famille, #code_fournisseur) (0,5 pt)
- Mois (<u>code_mois</u>, annee, numero_mois, trimestre)
- Vente_mensuelle (<u>#code_magasin, #code_produit, #code_mois</u>, quantite_vendue, ca_ht, quantite_demarquee) (0,5 pt)

Le modèle physique (types, index, contraintes de non-nullité) se déduit du MLD lors de l'implantation dans le SGBD de l'entrepôt ; il n'est pas demandé.

*1.1 c) – Entrepôt plutôt que lac ; lecture en étoile*

Un entrepôt de données est une base orientée sujet, intégrée, historisée et non volatile, structurée pour l'analyse ; un lac de données stocke des données brutes et hétérogènes dont le schéma n'est défini qu'à la lecture, pour l'exploration. En l'espèce, le besoin est un pilotage récurrent par des indicateurs stables (chiffre d'affaires, démarque, part du local), à partir de sources structurées (caisses, ERP), avec un historique mensuel et des comparaisons entre magasins demandées par les gérants (annexe 1.4) : un entrepôt alimenté par une chaîne d'extraction, de transformation et de chargement répond à ce besoin ; un lac n'apporterait rien tant qu'aucune donnée non structurée n'est exploitée et exigerait une gouvernance que la coopérative n'a pas encore (0,5 pt).

Le modèle obtenu est un schéma en étoile : Vente_mensuelle est la table de faits, au grain « magasin × produit × mois », qui porte des mesures additives (quantités, chiffre d'affaires) ; Magasin, Produit et Mois sont des dimensions, et la dimension temps est explicite. Famille et Fournisseur, rattachées à Produit et non à la table de faits, font du modèle un léger flocon ; les dénormaliser dans la dimension Produit le ramènerait à une étoile stricte et simplifierait les restitutions par famille ou par type de fournisseur (0,5 pt).

**Réponses tolérées**
- Noms d'entités, d'associations ou d'attributs différents s'ils restent explicites (« Article », « Période », « Ligne_vente ») ; attributs complémentaires pertinents (prix de vente conseillé, région du magasin) ; notation « pattes de corbeau » ou UML lisible (format libre, JUR-T10).
- Entité VENTE_MENSUELLE à identifiant propre (id_vente) reliée par trois associations (1,1) à Magasin, Produit et Mois, si le candidat signale que le triplet doit rester unique : modélisation acceptée (barème de a-4 et b-3 maintenu si la contrainte d'unicité est mentionnée).
- Cardinalité 1,n côté Magasin si le candidat suppose explicitement que tout magasin chargé a déjà vendu : hypothèse acceptée.
- Réponse en c) qui recommande une architecture combinant un entrepôt et un référentiel de données maîtres (produits, fournisseurs) : valorisée.

**Erreurs types**
- *MCD et MLD confondus* — clés étrangères dessinées dans le MCD, MLD sans table issue de l'association ternaire ou clé de Vente_mensuelle réduite à un seul identifiant ; juste : le MCD ne comporte ni clé étrangère ni table, le MLD dérive de règles de passage énoncées.
- *MCD et MLD confondus* (`JUR-T06`) — confondre « modéliser » et « décrire » : liste d'entités sans associations ni cardinalités ; juste : chaque cardinalité est justifiée par une règle de gestion.
- *Entrepôt et lac de données confondus* — entrepôt et lac présentés comme équivalents ou le lac comme « entrepôt moderne » ; juste : finalités, schémas et gouvernance différents, et complémentaires.
- *BI réduite à un outil* (`JUR-D02`) — réduire l'entrepôt à l'outil de restitution (« le projet consiste à acheter un outil de BI ») ; juste : chaîne collecte, transformation, entrepôt, restitution (JUR-D01).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Formalisme Merise (MCD, MLD, règles de passage) | entités, associations, cardinalités | F07 § 2 à 5 | manuels |
| Entrepôt et lac de données ; schéma en étoile | définitions, faits, dimensions, grain | F07 § 6 | notion de cours |

---

### 1.2 – Gouvernance des données (4 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ».
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ».

**Annexes mobilisées** : annexes 1.1 (organisation, absence de responsable des données, articles créés en caisse), 1.2 (règles de gestion, constats) et 1.4 (témoignages de Mme BENALI, de M. FERNANDES et de Mme OUHIBI).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance des données définie (décisions, rôles, règles, contrôle) | 0,5 |
| a-2 | DAMA-DMBOK présenté comme référentiel de bonnes pratiques, domaines prioritaires reliés au cas | 0,5 |
| b-1 | Propriétaire et intendant distingués | 0,5 |
| b-2 | Répartition pour les trois domaines, justifiée par les annexes (0,5 par domaine dans la limite de 1) | 1 |
| b-3 | Instance d'arbitrage : composition, fréquence, décisions | 0,5 |
| c | Deux entrées du dictionnaire complètes (0,5 chacune) | 1 |

**Réponse indicative**

*1.2 a) – Gouvernance des données et DAMA-DMBOK*

La gouvernance des données est l'ensemble des décisions, des rôles, des règles et des contrôles qui organisent la responsabilité sur les données, leur qualité, leur sécurité et leur usage tout au long de leur cycle de vie ; elle fait de la donnée un actif partagé et non un sous-produit des applications (0,5 pt). À Comptoirs Ligériens, elle est absente : aucun responsable des données n'est désigné, les fiches sont saisies par la DSI sur formulaire et chaque magasin crée ses propres articles (annexe 1.1) ; la directrice des achats tient la qualité pour « un problème informatique » (annexe 1.4).

Le DAMA-DMBOK (DAMA International, 2e édition) est un référentiel, c'est-à-dire un corpus de bonnes pratiques et non une norme certifiable, qui organise la gestion des données en onze domaines de connaissance autour de la gouvernance. Pour la coopérative, il fournit un vocabulaire commun et une grille pour hiérarchiser les chantiers : les domaines prioritaires sont la gouvernance (rôles, politiques), les données de référence et données maîtres (référentiel unique des produits et des fournisseurs), la qualité des données et les métadonnées (dictionnaire), puis l'entrepôt et le décisionnel, qui ne vaudront que si les trois premiers sont maîtrisés (0,5 pt).

*1.2 b) – Rôles par domaine et instance d'arbitrage*

Le propriétaire des données est le responsable métier d'un domaine : il définit les données, fixe les règles de gestion et le niveau de qualité attendu, autorise les accès et arbitre ; l'intendant met en œuvre ces règles au quotidien : il tient le dictionnaire, contrôle, corrige et anime les producteurs de données. Le propriétaire décide, l'intendant opère ; ni l'un ni l'autre n'est nécessairement à la DSI, qui fournit les outils et l'architecture (0,5 pt).

| Domaine | Propriétaire | Intendant | Justification tirée des annexes |
|---|---|---|---|
| Produits (catalogue, familles, labels) | directrice des achats et de l'offre (Mme BENALI) | l'une des deux assistantes de la DSI, rattachée fonctionnellement aux achats | les achats définissent l'offre ; les fiches sont déjà saisies par ces assistantes (annexe 1.1) : l'intendance leur donne un mandat métier sans charge nouvelle pour Mme BENALI, qui craint de « corriger 9 000 fiches » (annexe 1.4) |
| Fournisseurs (producteurs et grossistes) | directrice des achats et de l'offre, responsable du référencement | la seconde assistante, avec la direction administrative et financière pour les données de paiement | doublons et distances manquantes (annexe 1.2) relèvent du référencement ; la distance conditionne l'indicateur « local » |
| Ventes et démarque | directeur du réseau (M. ARNAUD), qui anime les magasins | contrôleur de gestion (M. FERNANDES), appuyé d'un référent dans chaque magasin pour la démarque | les ventes et la démarque sont produites par les magasins ; le contrôleur de gestion connaît les écarts (annexe 1.4) et sera libéré des rapprochements manuels |

(0,5 pt par domaine justifié, dans la limite de 1 pt.)

Instance : un comité de gouvernance des données, présidé par le directeur général, réunissant les propriétaires, la DSI, le contrôle de gestion et deux gérants administrateurs (dont Mme OUHIBI), qui se réunit chaque trimestre ; il valide les règles de gestion et le dictionnaire, arbitre les conflits (création d'articles locaux par les magasins, définition du « produit local ») et suit les indicateurs de qualité (question 1.3). La présence des gérants est décisive dans une coopérative où les magasins sont autonomes (0,5 pt).

*1.2 c) – Entrées du dictionnaire de données*

| Rubrique | Distance du fournisseur | Quantité démarquée |
|---|---|---|
| Nom technique | distance_km | quantite_demarquee |
| Définition | distance routière, en kilomètres, entre le lieu de production (ou l'entrepôt du grossiste) et la plateforme de Tours | quantité d'un produit retirée de la vente dans un magasin au cours du mois (produits jetés ou donnés), en unité de vente |
| Type et format | entier positif ; 0 à 2 000 | décimal positif (deux décimales pour les produits au poids) ; agrégé au mois |
| Règle de gestion et de contrôle | obligatoire pour tout fournisseur ; un fournisseur à moins de 150 km rend ses produits « locaux » ; contrôle de vraisemblance à la création | obligatoire pour chaque magasin et chaque produit frais vendu ; valeur nulle saisie explicitement ; alerte si elle dépasse la quantité vendue |
| Source | fiche fournisseur de l'ERP, saisie au référencement | logiciel de caisse (fonction de démarque), et non plus le tableur commun |
| Propriétaire / intendant | directrice des achats / intendante fournisseurs | directeur du réseau / contrôleur de gestion |
| Sensibilité | publique dans le réseau | interne |

(0,5 pt par entrée comportant au moins définition, type, règle, source et propriétaire.)

**Réponses tolérées**
- Désignation d'un *Chief Data Officer* ou d'un délégué aux données : acceptée si le candidat la justifie par la taille du réseau et rappelle que l'organisation de la gouvernance reste « illustrative, non normative » (programme 2.3).
- Propriétaire du domaine « ventes » confié au directeur administratif et financier : accepté s'il est justifié (fiabilité du chiffre d'affaires).
- Dictionnaire présenté sous forme de liste plutôt que de tableau ; rubriques supplémentaires (historique, durée de conservation) valorisées.

**Erreurs types**
- *Norme, référentiel et solution confondus* (`JUR-S06`) — présenter le DAMA-DMBOK comme une norme internationale certifiable ou comme un logiciel ; juste : référentiel associatif de bonnes pratiques, non certifiable.
- `JUR-T01` — gouvernance définie sans application au cas, ou réduite à un outil (catalogue de données) ; juste : rôles, règles et instances reliés aux témoignages.
- Confier la propriété des données à la DSI (« la DSI saisit, donc elle possède ») ; juste : la DSI est dépositaire technique, la responsabilité est métier (JUR-G10).
- *MCD et MLD confondus* — confondre dictionnaire de données et MCD ; juste : le dictionnaire décrit chaque donnée (définition, format, règle, source, propriétaire), le MCD leurs relations.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (DAMA International) | référentiel, onze domaines de connaissance | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Rôles de propriétaire et d'intendant | gouvernance illustrative | F07 § 8.1 | notion de cours |

---

### 1.3 – Qualité des données (4 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ».
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ».

**Annexes mobilisées** : annexes 1.2 (constats du profilage), 1.3 (indicateurs du mois) et 1.4 (témoignages).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Qualité des données définie (aptitude à l'usage, dimensions) | 0,5 |
| a-2 | Quatre constats rattachés chacun à une dimension, avec la conséquence pour le pilotage (0,5 par constat) | 2 |
| b-1 | Plan d'action hiérarchisé : correction à la source, contrôles à la saisie, responsabilités | 0,5 |
| b-2 | Deux indicateurs de qualité à cinq champs (0,5 chacun) | 1 |

**Réponse indicative**

*1.3 a) – Dimensions de la qualité appliquées aux constats*

La qualité des données est leur aptitude à l'usage prévu ; elle s'apprécie selon des dimensions décrites notamment par le modèle de qualité des données ISO/IEC 25012 (exactitude, complétude, cohérence, actualité, accessibilité) ; l'unicité est une dimension usuelle des référentiels de pratique, dont le DAMA-DMBOK (0,5 pt).

| Constat (annexe 1.2) | Dimension dégradée | Conséquence pour le pilotage |
|---|---|---|
| Une vingtaine de doublons pour 430 fiches de fournisseurs | unicité | achats et volumes d'un même producteur dispersés : poids réel des producteurs locaux et négociations faussés |
| Distance non renseignée pour 12 % des producteurs | complétude | indicateur « part des ventes de produits locaux » (38 %, annexe 1.3) sous-estimé ou non calculable ; risque d'affichage « local » non étayé |
| 1 700 articles créés en caisse, sans famille ni fournisseur, libellés hétérogènes (4 % du chiffre d'affaires) | cohérence (et conformité au référentiel) | ventes non rattachables aux familles ni aux producteurs ; comparaisons entre magasins faussées |
| Démarque saisie par 31 magasins sur 46 | complétude | taux de démarque de 2,9 % calculé sur un échantillon biaisé ; l'objectif du projet de prévision (annexe 3.1) ne pourra pas être mesuré |
| Écart de 1,8 % entre le tableau de bord et les caisses | exactitude | chiffre d'affaires contesté par les gérants, perte de confiance dans tout le tableau de bord |
| Diffusion à J+12 | actualité | décisions de commande prises avant la publication (annexe 1.4) |

(Quatre constats attendus, 0,5 pt chacun.)

*1.3 b) – Plan d'action et indicateurs*

Plan hiérarchisé (0,5 pt) :
1. avant le chargement de l'entrepôt (avril-mai 2027) : dédoublonner le référentiel des fournisseurs par le numéro SIRET et compléter les distances, sous la responsabilité de l'intendante des fournisseurs ; c'est la condition de l'indicateur « local » ;
2. à la source : rendre la distance obligatoire au référencement, interdire la création d'articles en caisse hors catalogue ou la soumettre à une validation de la centrale sous 48 heures (décision du comité de gouvernance, question 1.2) ; faire saisir la démarque dans le logiciel de caisse par tous les magasins ;
3. dans la chaîne de chargement : contrôles automatiques (rejet des articles sans famille, rapprochement du chiffre d'affaires de l'entrepôt avec les caisses), fin des ressaisies manuelles ;
4. en continu : tableau de bord de qualité présenté au comité trimestriel, correction à la source plutôt que dans l'entrepôt.

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de complétude de la distance des fournisseurs | fiches de producteurs locaux actifs avec distance renseignée / fiches de producteurs locaux actifs | référentiel des fournisseurs de l'ERP | mensuelle | 100 % avant l'ouverture de l'entrepôt (88 % en février 2027) | processus |
| Taux de magasins saisissant leur démarque | magasins ayant transmis leur démarque du mois / magasins associés | logiciel de caisse, chargement de l'entrepôt | mensuelle | 46 sur 46, soit 100 %, fin 2027 (31 sur 46 en 2026) | processus |

(0,5 pt par indicateur complet.)

**Réponses tolérées**
- Autres indicateurs à cinq champs : taux de doublons de fournisseurs, part du chiffre d'affaires réalisée sur des articles hors catalogue (cible inférieure à 1 %), écart de chiffre d'affaires entre entrepôt et caisses (cible 0 %), délai de mise à disposition (J+2).
- Rattachement des articles locaux à la « conformité » ou à l'« exactitude » s'il est argumenté ; axe « gouvernance » (ESG) ou « apprentissage » accepté s'il est justifié.

**Erreurs types**
- *Indicateurs génériques* (`JUR-A02`) — indicateurs génériques sans formule, source ni cible, ou sans lien avec les constats ; juste : chaque indicateur mesure la correction d'un constat de l'annexe 1.2.
- Corriger les données dans l'entrepôt sans traiter la cause à la source ; juste : correction et contrôle à la saisie, responsabilité du propriétaire.
- `JUR-T03` — paraphrase des constats sans dimension ni conséquence ; juste : constat → dimension → effet sur une décision du réseau.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 25012 — Modèle de qualité des données | dimensions de la qualité | `iso_iec_25012` / F07 § 8.3 | en vigueur |

---

### 1.4 – Critique du tableau de bord mensuel (3 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ».
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.e` « Revue et amélioration continue des dispositifs de pilotage ».

**Annexes mobilisées** : annexes 1.3 (graphiques et indicateurs) et 1.4 (témoignages de Mme OUHIBI et de M. FERNANDES).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Tableau de bord de pilotage défini (indicateurs sélectionnés, reliés aux objectifs, avec cibles, au service d'une décision) | 0,5 |
| a-2 | Trois défauts identifiés, chacun relié à un risque de décision erronée (0,5 par défaut) | 1,5 |
| b | Principes de la nouvelle restitution : contenu et indicateurs à cible, représentations adaptées, comparaisons par groupes de magasins, délai (0,5 par principe, dans la limite de 1) | 1 |

**Réponse indicative**

*1.4 a) – Trois défauts et leurs risques*

Un tableau de bord de pilotage est un ensemble restreint d'indicateurs, choisis en fonction des objectifs et des décisions de ses destinataires, assortis de cibles et de seuils d'alerte et diffusés à temps pour agir ; il n'est pas un recueil de toutes les données disponibles (0,5 pt). Une visualisation doit rendre une donnée fidèlement lisible ; sa lecture critique porte sur la représentation (échelle, type de graphique) et sur l'interprétation (biais, corrélation et causalité). Défauts attendus, trois parmi :
- **Axe tronqué et comparaison saisonnière inadaptée (graphique 1)** : l'axe commence à 13,5 M€, si bien que la barre de janvier paraît huit fois plus courte que celle de décembre alors que le chiffre d'affaires ne baisse que d'environ 13 % (13,8 contre 15,9 M€) ; décembre est un mois de fêtes, et la bonne comparaison est janvier 2026 : 13,8 M€ contre 13,2 M€, soit une hausse d'environ 4,5 %. Risque : alarme injustifiée et mesures commerciales inutiles (promotions, baisse des commandes) (0,5 pt).
- **Corrélation présentée comme une causalité (graphique 3)** : les magasins de centre-ville des grandes agglomérations cumulent forte utilisation de la carte et fort chiffre d'affaires au mètre carré ; un facteur commun (emplacement, clientèle, taille de l'agglomération) explique les deux variables. Risque : généraliser une remise de 5 % qui réduit la marge de tous les magasins sans effet démontré sur les ventes (0,5 pt).
- **Indicateur calculé sur un échantillon biaisé et signaux sans seuils (tableau)** : le taux de démarque de 2,9 %, affiché en vert, ne porte que sur 31 magasins, sans doute les plus rigoureux ; les seuils des signaux ne sont pas documentés et la part du local (38 %) repose sur des distances incomplètes. Risque : sous-estimer la démarque et renoncer à des actions de réduction du gaspillage (0,5 pt).
- **Diagramme circulaire en trois dimensions à 46 secteurs (graphique 2)** : illisible, la perspective déforme les surfaces et aucune comparaison n'est possible. Risque : aucune décision possible, perte de confiance des gérants (0,5 pt, en remplacement d'un des trois défauts précédents).

*1.4 b) – Principes de la nouvelle restitution*

- **Contenu** : un nombre limité d'indicateurs reliés aux objectifs du réseau (chiffre d'affaires, marge, démarque, part du local, panier moyen), chacun avec formule, source, cible et seuils d'alerte documentés ; la qualité des données affichée (part des magasins inclus).
- **Représentations** : courbes sur treize mois glissants avec l'année précédente pour les évolutions, axes commençant à zéro pour les histogrammes, histogrammes classés plutôt que secteurs pour les comparaisons, nuages de points accompagnés d'une mise en garde sur la causalité.
- **Comparaisons et délai** : comparaison de chaque magasin à des magasins de taille et d'emplacement comparables, comme le demande Mme OUHIBI ; diffusion à J+2 depuis l'entrepôt ; une page de synthèse pour le conseil et une page par magasin pour les gérants ; fin de l'ajout de graphiques au fil des comités (M. FERNANDES), revue annuelle du tableau de bord.

(0,5 pt par principe justifié, dans la limite de 1 pt.)

**Réponses tolérées**
- Tout autre défaut pertinent (absence de cible, absence de source, signal « orange » du panier moyen non expliqué), s'il est relié à un risque de décision.
- Variation de janvier exprimée en valeur (+0,6 M€) plutôt qu'en pourcentage ; ordre de grandeur de la baisse depuis décembre arrondi (« environ 2 M€ »).
- Mention d'outils de restitution du marché, à titre d'exemple seulement.

**Erreurs types**
- *Corrélation prise pour une causalité* (`JUR-D06`) — valider la conclusion « la carte fait vendre » ; juste : corrélation n'est pas causalité, facteur commun à identifier, test sur des magasins comparables avant toute généralisation.
- *BI réduite à un outil* (`JUR-D02`) — répondre par le changement d'outil de visualisation ; juste : la qualité du tableau de bord tient aux indicateurs, aux données et aux règles de représentation.
- *Indicateurs génériques* — proposer une liste d'indicateurs sans cible ni seuil ; juste : chaque indicateur a une cible et un seuil d'alerte documentés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Choix des représentations, biais de lecture, corrélation et causalité | lecture critique | F08 § 4 et 5 | guide p. 240 |
