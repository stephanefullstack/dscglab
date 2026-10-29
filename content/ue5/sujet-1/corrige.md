# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 1

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Gouverner et modéliser les données de pilotage | 16 | 1.1 à 1.4 | `exercices/ex01_donnees_pilotage` |
| 2 – Infogérance, transition et transfert des connaissances | 14 | 2.1 à 2.4 | `exercices/ex02_infogerance_transition` |
| 3 – Intelligence artificielle, traçabilité et numérique responsable | 10 | 3.1 à 3.3 | `exercices/ex03_ia_tracabilite_numerique_responsable` |
| **Total** | **40** | | |

---

## DOSSIER 1 – GOUVERNER ET MODÉLISER LES DONNÉES DE PILOTAGE (16 points)

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

---

## DOSSIER 2 – INFOGÉRANCE, TRANSITION ET TRANSFERT DES CONNAISSANCES (14 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Choix des formes de contrat | `1.4.b` Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle ; `1.4.d` Méthodologie de négociation contractuelle et analyse des risques | 4 |
| 2.2 Niveaux de service, pénalités et réversibilité | `1.4.c` Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD ; `1.4.e` Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) | 4 |
| 2.3 Planification de la transition | `1.5.d` Planification des ressources, délais, coûts et qualité ; `1.5.e` Identification et gestion des risques (maintenance, évolutivité, sécurité) | 3 |
| 2.4 Transfert des connaissances | `1.6.b` Architecture fonctionnelle des systèmes de knowledge management ; `1.6.c` Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) | 3 |
| **Dossier 2 – Infogérance, transition et transfert des connaissances** |  | **14** |

Répartition indicative : connaissances (définitions de la régie, du forfait, de l'infogérance, du SLA, de l'OLA, du modèle SECI : items 2.1 a, 2.2 a, 2.4 a) 3,5 points, la définition du chemin critique étant notée avec son identification (2.3 b-1) ; analyse du contrat et des niveaux de service, Gantt, dispositif de transfert 10,5 points. Durée conseillée : 14 points × 4,5 minutes ≈ 1 h 05.

---

### 2.1 – Choix des formes de contrat (4 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.b` « Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle » ; `1.4.d` « Méthodologie de négociation contractuelle et analyse des risques ».

**Annexes mobilisées** : annexes 1.4 (témoignages de M. LEMOINE et de Mme VASSEUR) et 2.1 (architecture, niveaux de service de 2026, offre de Nexalis, plan de transition).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Régie : mise à disposition de compétences au temps passé, sous la direction du client, qui porte le risque | 0,5 |
| a-2 | Forfait : livrable défini, prix et délai fixés, risque de dépassement porté par le prestataire | 0,5 |
| a-3 | Infogérance : prise en charge durable de tout ou partie du SI avec engagements de niveaux de service | 0,5 |
| b-1 | Limites de la régie actuelle tirées de l'annexe 2.1 et des témoignages (0,5 par limite, dans la limite de 1) | 1 |
| b-2 | Migration : forfait justifié (périmètre défini, recette, délai impératif) | 0,5 |
| b-3 | Exploitation : infogérance avec SLA justifiée (continuité 7 jours sur 7, fin de la dépendance à une personne) | 0,5 |
| b-4 | Conditions : compétence de pilotage conservée à la DSI, coût complet à comparer, dépendance maîtrisée | 0,5 |

**Réponse indicative**

*2.1 a) – Régie, forfait, infogérance*

- **Régie** (assistance technique) : l'ESN met à disposition des compétences facturées au temps passé (ici 90 jours à 650 € HT, soit 58 500 € HT en 2026) ; elle s'engage sur les moyens fournis, et le client, qui dirige les travaux, porte le risque de délai et de résultat (0,5 pt).
- **Forfait** : l'ESN s'engage à livrer un résultat défini par un cahier des charges, à un prix et dans un délai fixés ; elle porte le risque de dépassement, sauf avenant si le besoin change (0,5 pt).
- **Infogérance** : le client confie durablement à l'ESN tout ou partie de son SI (hébergement, exploitation, supervision, support) ; l'ESN s'engage sur des niveaux de service mesurables, assortis de pénalités ; le client reste responsable de son SI et de ses données et doit piloter la prestation (0,5 pt).

*2.1 b) – Limites de la régie actuelle et recommandations*

Limites de la régie pour Comptoirs Ligériens (1 pt pour deux limites étayées) :
- aucun engagement de niveau de service : disponibilité de 98,6 % sur la plage 6 h – 22 h, 14 incidents bloquants dont 9 un week-end, alors que les commandes du week-end préparent les livraisons du lundi, et 7 heures en moyenne pour rétablir le service, sans levier contractuel ;
- la régie suppose un client capable de diriger les intervenants ; or le pilotage repose sur M. LEMOINE seul, qui part le 30 juin 2027, et les ingénieurs d'Altinéa « changent tous les six mois » : aucune capitalisation ;
- des risques non maîtrisés : aucune restauration de sauvegarde testée, 22 nuits d'interface en échec ou corrigées à la main.

Recommandations :
- **Migration de l'ERP et du portail : forfait** (offre de 36 000 € HT, environnement recetté livré). Le besoin est ponctuel, son périmètre est connu (inventaire de la tâche B), le délai est impératif (30 juin 2027) : le forfait transfère le risque de dépassement à Nexalis, à condition de définir les livrables et les critères de recette (tâche D) et de lier le paiement à la recette (0,5 pt).
- **Exploitation durable : infogérance** avec des niveaux de service adaptés au rythme des magasins (7 jours sur 7, 6 h – 22 h). Elle répond au souhait de Mme VASSEUR d'une DSI qui « pilote » au lieu de « surveiller des serveurs la nuit » et met fin à la dépendance envers une personne (0,5 pt).
- **Conditions** : la DSI garde un responsable du contrat capable de contrôler les niveaux de service (sinon la dépendance envers M. LEMOINE devient une dépendance envers Nexalis, ce que redoute Mme VASSEUR) ; le surcoût apparent (168 000 € HT par an contre 58 500 € HT de régie en 2026) s'apprécie en coût complet, en ajoutant au coût actuel le remplacement de M. LEMOINE, le renouvellement de la salle informatique, une astreinte de week-end et le coût des incidents ; une réversibilité négociée dès la signature limite le risque d'enfermement (0,5 pt).

**Réponses tolérées**
- Forfait de migration confié à un autre prestataire que l'infogérant, ou régie maintenue quelques mois en assistance à la transition, si la cohérence avec le délai et le pilotage est démontrée.
- Mention d'un hébergement en mode SaaS de l'ERP ou d'une tierce maintenance applicative pour l'interface, si elle est justifiée.
- Ordre de grandeur du coût complet, sans chiffrage poste par poste (non attendu).

**Erreurs types**
- *Régie, forfait et infogérance confondus* — confondre régie et forfait ou affirmer que la régie transfère le risque au prestataire ; juste : en régie, le client dirige et porte le risque ; au forfait, le prestataire s'engage sur le livrable.
- `JUR-A05` / `JUR-G11` — présenter l'infogérance comme un transfert de responsabilité ; juste : le client reste responsable de son SI, de ses données et du pilotage de la prestation.
- Recommander un seul contrat pour deux besoins de nature différente (projet ponctuel et service récurrent).
- `JUR-T01` — définitions sans exploitation des chiffres de l'annexe 2.1.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des contrats de prestation informatique | régie, forfait, infogérance | F04 § 1 | guide p. 255 |

---

### 2.2 – Niveaux de service, pénalités et réversibilité (4 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.c` « Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD » ; `1.4.e` « Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) ».

**Annexes mobilisées** : annexes 2.1 (niveaux de service de 2026, articles du projet de contrat, observation de la DSI) et 3.3 (RGPD, NIS 2, Data Act).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | SLA défini : engagement contractuel sur des niveaux mesurables, avec mesure, reporting et conséquences | 0,5 |
| a-2 | OLA distingué : accord interne entre équipes qui soutient le SLA | 0,5 |
| b-1 | Trois faiblesses des articles 6, 7 et 9 confrontées aux chiffres de 2026 (0,5 par faiblesse) | 1,5 |
| b-2 | Rédactions ou indicateurs de remplacement mesurables | 0,5 |
| c-1 | Clause de réversibilité : contenu adapté au cas | 0,5 |
| c-2 | Deux autres clauses justifiées (sous-traitance des données personnelles, audit, sécurité et notification) | 0,5 |

**Réponse indicative**

*2.2 a) – SLA et OLA*

La convention de niveau de service (*Service Level Agreement*) est l'engagement contractuel du prestataire envers son client sur des niveaux de service mesurables (disponibilité, délais de prise en charge et de rétablissement, sauvegardes), avec la méthode et la période de mesure, le reporting et les conséquences d'un manquement, dont les pénalités (0,5 pt). L'accord de niveau opérationnel (*Operational Level Agreement*) est un accord interne entre équipes d'une même organisation (par exemple, chez Nexalis, entre l'hébergement et le support) qui permet de tenir le SLA ; il n'engage pas le prestataire envers le client. Ces notions sont décrites par le référentiel ITIL (0,5 pt).

*2.2 b) – Trois faiblesses du projet de contrat*

| Article | Faiblesse au regard de 2026 | Rédaction ou indicateur proposé |
|---|---|---|
| 6 – plage de mesure | disponibilité mesurée du lundi au vendredi, de 8 h à 18 h : 9 des 14 incidents bloquants de 2026 sont survenus un week-end, et les commandes du week-end préparent les livraisons du lundi ; un taux de 99,5 % ainsi mesuré peut coexister avec des week-ends sans service | disponibilité mesurée de 6 h à 22 h, 7 jours sur 7, soit environ 480 heures par mois : 99,5 % tolère environ 2,4 heures d'indisponibilité par mois ; mesure par la supervision du client ou un outil partagé |
| 6 – prise en charge | prise en charge d'un incident bloquant en 4 heures « ouvrées » : un incident survenu le samedi matin peut n'être pris en charge que le lundi, alors que 9 des 14 incidents bloquants de 2026 sont survenus un week-end | prise en charge en 30 minutes à 1 heure, 7 jours sur 7, sur la plage 6 h – 22 h (astreinte) |
| 6 – rétablissement | « meilleurs efforts » : aucun engagement, alors que le rétablissement moyen a été de 7 heures en 2026 | garantie de temps de rétablissement d'un incident bloquant de 4 heures, y compris le week-end ; indicateur : part des incidents bloquants rétablis en moins de 4 heures, cible 95 % |
| 7 – pénalités | plafond de 5 % de la redevance mensuelle, soit 700 € HT au plus par mois ; déclenchement subordonné à une réclamation écrite dans les 15 jours d'un rapport trimestriel établi par le prestataire lui-même : peu dissuasif et facile à perdre | pénalités automatiques, calculées sur un reporting mensuel contradictoire, plafond porté par exemple à 10 à 15 % de la redevance, et droit de résiliation en cas de manquements répétés |
| 9 – sauvegardes | conservation de sept jours, aucun test de restauration, alors qu'aucune restauration n'a été testée en 2026 : une corruption découverte après une semaine serait irrécupérable | perte de données maximale admissible (RPO) de 24 heures, rétention de 30 jours et archive mensuelle sur un an, copie dans un second site ; test de restauration chaque semestre avec procès-verbal ; indicateur : tests de restauration réussis / tests prévus, cible 100 % |

(Trois faiblesses attendues parmi les cinq, 0,5 pt chacune ; 0,5 pt pour des propositions mesurables.)

*2.2 c) – Réversibilité et autres clauses*

Clause de réversibilité (0,5 pt) : elle organise dès la signature la sortie du contrat, à son terme ou en cas de résiliation, sans interruption de service : restitution de toutes les données (ERP, portail, sauvegardes, historiques) dans un format ouvert et documenté, avec la documentation d'exploitation, en particulier celle de l'interface caisses-ERP ; assistance du prestataire sortant et transfert de compétences vers le repreneur ou la DSI ; maintien du service pendant une période de transition (par exemple six mois) ; prix et délais fixés au contrat, et non « à convenir » ; plan de réversibilité tenu à jour et testé. Pour un service d'informatique en nuage, le Data Act, applicable depuis le 12/09/2025, organise aussi le changement de fournisseur (portabilité des données, assistance à la sortie) (annexe 3.3) ; depuis le 12/01/2027, aucun frais de changement de fournisseur ne peut être facturé (article 29 § 1), à condition que l'hébergement de Nexalis soit un « service de traitement de données » au sens du règlement et non un service conçu en majorité sur mesure pour la coopérative (article 31). Le référentiel du cloud de confiance du Cigref rappelle que toute exigence opérationnelle doit être contractuellement exigible.

Deux autres clauses, parmi (0,5 pt) :
- **Données personnelles** : l'infogérant traite pour le compte de la coopérative des données personnelles (comptes des utilisateurs du portail, coordonnées des producteurs exploitants individuels) ; il est sous-traitant au sens de l'article 28 du RGPD, qui impose un contrat écrit (traitement sur instruction, confidentialité, sécurité, assistance, sort des données en fin de contrat) et interdit le recours à un autre sous-traitant sans autorisation écrite préalable, spécifique ou générale, du responsable du traitement (en cas d'autorisation générale, information préalable et droit d'objection) : l'article 14 doit être modifié en conséquence.
- **Audit** : droit pour la coopérative, ou un tiers qu'elle mandate, d'auditer la prestation, la sécurité et le respect des niveaux de service, avec accès aux preuves et rapports d'audit indépendants.
- **Sécurité et notification des incidents** : engagements de sécurité (authentification multifacteur des administrateurs, localisation des données dans l'Union européenne, chiffrement des sauvegardes) et notification sans délai de tout incident de sécurité. NIS 2 fait de la sécurité de la chaîne d'approvisionnement une mesure de gestion des risques ; sa transposition française n'est pas promulguée au 31/12/2026 (annexe 3.3), mais l'anticiper par contrat est une bonne pratique. La coopérative, centrale d'achat et grossiste alimentaire de plus de 50 salariés, entrerait elle-même dans le champ de NIS 2 comme entité importante dès l'entrée en vigueur de la loi de transposition (annexe II, point 4), et Nexalis, fournisseur de services gérés, également : la sécurité de la chaîne d'approvisionnement deviendrait alors une obligation, que le contrat doit anticiper dès 2027.

**Réponses tolérées**
- Autres valeurs cibles cohérentes avec le contexte (99,7 % sur 6 h – 22 h, rétablissement en 2 ou 6 heures, RPO de 12 heures) si elles sont justifiées par les commandes du week-end.
- Faiblesse relevée sur le reporting trimestriel produit par le seul prestataire, ou sur l'exclusion des « maintenances programmées » sans encadrement, en remplacement de l'une des trois attendues.
- Qualification de la coopérative comme future entité importante au sens de NIS 2 (grossiste alimentaire de plus de 50 salariés) et de Nexalis comme fournisseur de services gérés, présentée comme dépendante de la transposition française.
- Clause de durée et de sortie anticipée, ou clause d'évolution des prix, si elle est justifiée par le risque de dépendance.

**Erreurs types**
- *SLA et OLA confondus* — confondre SLA et OLA ; juste : le SLA engage le prestataire envers le client, l'OLA organise les équipes qui le tiennent.
- *Indicateurs génériques* — proposer des niveaux de service sans plage ni méthode de mesure ; juste : un engagement vaut par sa mesure, sa période et sa conséquence.
- *RTO et RPO inversés* — confondre perte de données admissible (RPO) et durée d'interruption admissible (RTO) dans l'article 9.
- *NIS 2 confondue avec le RGPD ; Statut réglementaire affirmé sans date* — présenter NIS 2 comme applicable en droit français ou la confondre avec le RGPD ; juste : statut de l'annexe 3.3, et deux textes distincts (cybersécurité / données personnelles).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ITIL (PeopleCert) | SLA, OLA, catalogue de services | `itil` / F04 § 3 | en vigueur |
| RGPD, règlement (UE) 2016/679, art. 28 | sous-traitant, contrat écrit | `rgpd` / F15 § 5 | en vigueur |
| Data Act, règlement (UE) 2023/2854 | changement de fournisseur de services en nuage | `data_act` / F07 § 8.5 | applicable depuis le 12/09/2025 |
| Directive (UE) 2022/2555 (NIS 2) et sa transposition française | chaîne d'approvisionnement ; projet de loi non promulgué | `nis2`, `nis2_transposition_fr` / F12 § 6 | non promulguée au 31/12/2026 |
| Référentiel du cloud de confiance (Cigref) | exigences contractuellement exigibles, réversibilité | `cigref_cloud_confiance` / F04 § 4 | publié |

---

### 2.3 – Planification de la transition (3 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.d` « Planification des ressources, délais, coûts et qualité » ; `1.5.e` « Identification et gestion des risques (maintenance, évolutivité, sécurité) ».

**Annexes mobilisées** : annexes 2.1 (plan de transition, contrainte sur M. LEMOINE, échéance du 30 juin 2027) et 1.4 (témoignage de M. LEMOINE).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Barres placées au plus tôt, antériorités respectées | 1 |
| a-2 | Jalons (signature, environnement prêt, recette, décision de bascule, bascule, fin de la régie) | 0,5 |
| a-3 | Contrainte de ressource de M. LEMOINE vérifiée (B, E et F jamais simultanées) | 0,5 |
| b-1 | Chemin critique défini (suite des tâches sans marge, qui fixe la durée minimale du projet) et identifié : A-C-D-F-G-H ; fin en semaine 15 | 0,5 |
| b-2 | Échéance tenue avec une marge d'environ deux semaines et demie ; tâche A (puis D) à surveiller ; marges de B et E | 0,5 |

**Réponse indicative**

*2.3 a) – Diagramme de Gantt (semaine 1 = semaine du 1er mars 2027)*

```
Tâche                          S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15
A Contrats (3)                 ██ ██ ██                                          ◆ J1 fin S3 : contrats signés
B Inventaire, documentation (4)██ ██ ██ ██ ·· ··                                 (marge 2 semaines)
C Environnement (3)                     ██ ██ ██                                 ◆ J2 fin S6 : environnement prêt
D Migration à blanc, recette (4)                  ██ ██ ██ ██                    ◆ J3 fin S10 : recette validée
E Transfert de compétences (3)             ██ ██ ██ ·· ·· ··                     (marge 3 semaines, voir b)
F Restauration, répétition (2)                                ██  ██             ◆ J4 fin S12 : décision de bascule
G Bascule, accompagnement (2)                                         ██  ██     ◆ J5 bascule le week-end des 29 et 30 mai
H Fin de la régie, bilan (1)                                                  ██ ◆ J6 fin S15 : projet clos
```

Dates au plus tôt : A semaines 1 à 3 ; B semaines 1 à 4 ; C semaines 4 à 6 ; D semaines 7 à 10 (après B et C) ; E semaines 5 à 7 (après B) ; F semaines 11 et 12 ; G semaines 13 et 14 (après E et F) ; H semaine 15 (1 pt).

Jalons : contrats signés (fin de la semaine 3, 21 mars), environnement prêt (fin de la semaine 6), recette validée (fin de la semaine 10), décision de bascule après la répétition générale (fin de la semaine 12, 23 mai), bascule (week-end du 29 et 30 mai, semaine 13), fin de la régie et bilan (semaine 15, du 7 au 13 juin) (0,5 pt).

Ressource : M. LEMOINE intervient sur B (semaines 1 à 4), E (semaines 5 à 7) et F (semaines 11 et 12) : aucune semaine commune, le plan au plus tôt respecte la contrainte (0,5 pt).

*2.3 b) – Chemin critique, échéance et points de vigilance*

Le chemin critique est la suite des tâches dont la marge est nulle : tout retard sur l'une d'elles retarde d'autant la fin du projet, dont il fixe la durée minimale. Ici, c'est A-C-D-F-G-H : 3 + 3 + 4 + 2 + 2 + 1 = 15 semaines. Le projet s'achève à la fin de la semaine 15 (13 juin 2027) et la bascule a lieu fin mai : l'échéance du mercredi 30 juin (semaine 18) est tenue, avec une marge d'environ deux semaines et demie (0,5 pt).

Vigilance (0,5 pt) :
- la tâche A est critique et c'est la plus exposée : la négociation des clauses de la question 2.2 peut l'allonger ; si elle dure 5 semaines au lieu de 3, le projet finit en semaine 17 (27 juin), sans plus aucune marge. Il faut donc lancer la négociation des niveaux de service et de la réversibilité dès la semaine 1, en priorité ;
- la tâche D (recette) dépend de la disponibilité des acheteurs et des magasins ;
- B a 2 semaines de marge ; E a 5 semaines de marge au regard des seules antériorités, mais seulement 3 si l'on tient compte de M. LEMOINE, qui doit aussi participer à F en semaines 11 et 12 : E ne doit pas glisser au-delà de la semaine 10.

**Réponses tolérées**
- Gantt dessiné à la main dans un autre format lisible (format libre, JUR-T10), jalons représentés autrement ; numérotation des semaines par dates.
- Bascule placée en fin de semaine 12 ou au début de la semaine 13, si le candidat le justifie.
- Mention d'un réseau PERT en complément, sans calcul développé.

**Erreurs types**
- `JUR-P01` — Gantt illisible, sans jalons, ou noyé de commentaires non demandés.
- Antériorités non respectées (D lancée avant la fin de B ; G avant la fin de E) ou contrainte de ressource ignorée (B, E et F en parallèle pour M. LEMOINE).
- Chemin critique confondu avec la liste des tâches les plus longues ; juste : la suite des tâches sans marge.
- *Schéma directeur confondu avec un plan de projet* — confondre le plan de projet avec un schéma directeur.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Diagramme de Gantt, chemin critique, jalons | planification à partir d'un texte | F05 § 4 | guide p. 285 |

---

### 2.4 – Transfert des connaissances (3 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.b` « Architecture fonctionnelle des systèmes de knowledge management » ; `1.6.c` « Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) ».

**Annexes mobilisées** : annexes 1.4 (témoignage de M. LEMOINE) et 2.1 (interface, nuits corrigées à la main, tâches B, E et F du plan).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Connaissances tacites et explicites distinguées | 0,5 |
| a-2 | Modèle SECI : quatre modes de conversion en spirale | 0,5 |
| b-1 | Trois modes au moins appliqués au cas, chacun avec une action concrète (0,5 par mode) | 1,5 |
| b-2 | Calendrier intégré au plan (B, E, F) et indicateur d'efficacité à cinq champs | 0,5 |

**Réponse indicative**

*2.4 a) – Connaissances tacites et explicites ; modèle SECI*

La connaissance explicite est formalisée et transmissible par un support (procédure, documentation, base de connaissances) ; la connaissance tacite est incorporée à la personne (savoir-faire, intuition, « je sais quels magasins posent problème ») et difficile à formuler (0,5 pt). Le modèle SECI (Nonaka et Takeuchi, 1995) décrit la création de connaissances par quatre conversions successives, en spirale : socialisation (tacite vers tacite, par l'observation et la pratique partagée), externalisation (tacite vers explicite, par la formalisation), combinaison (explicite vers explicite, par l'assemblage et la diffusion) et internalisation (explicite vers tacite, par la mise en pratique) (0,5 pt).

*2.4 b) – Dispositif de transfert des savoirs de M. LEMOINE*

Le savoir critique de M. LEMOINE (corrections nocturnes de l'interface, clôture mensuelle des stocks) est presque entièrement tacite : « ce n'est écrit nulle part ». Dispositif :
- **Externalisation (tâche B, semaines 1 à 4)** : entretiens d'explicitation menés par la DSI ; rédaction, avec M. LEMOINE, des procédures de l'interface et de la clôture, de la liste des magasins dont les fichiers posent problème et des corrections types ; chaque correction manuelle est décrite comme une anomalie à traiter à la source (contrôle de complétude du fichier de caisse) (0,5 pt).
- **Socialisation (tâche E, semaines 5 à 7)** : binôme entre M. LEMOINE et l'ingénieur de Nexalis et le technicien de la DSI qui reprendront l'exploitation ; observation des chargements de 6 heures et de la clôture de mars, puis travail à deux sur les corrections réelles (0,5 pt).
- **Combinaison (tâches E et F)** : intégration des procédures dans la base de connaissances de la DSI et dans la documentation d'exploitation de Nexalis, rapprochement avec la documentation livrée par Altinéa en 2019, et inscription de ces documents dans le plan de réversibilité (question 2.2) (0,5 pt).
- **Internalisation (tâche F, semaines 11 et 12, et clôture de mai)** : les repreneurs exécutent seuls les procédures pendant la répétition générale de la bascule et la clôture de mai, M. LEMOINE n'intervenant qu'en observateur ; les écarts enrichissent la documentation (0,5 pt, si trois modes ne sont pas déjà notés).

Indicateur et pilotage (0,5 pt) : taux de procédures critiques exécutées sans aide par un repreneur = procédures critiques exécutées seules avec succès / procédures critiques recensées en tâche B ; source : registre de la répétition générale et des clôtures ; fréquence : hebdomadaire jusqu'à la bascule ; cible : 100 % à la décision de bascule (fin de la semaine 12) ; axe : apprentissage. Un référent de la DSI est responsable de la base de connaissances après le départ de M. LEMOINE.

**Réponses tolérées**
- Indicateur différent s'il mesure l'appropriation et non la seule production de documents (nombre de nuits d'anomalie traitées sans M. LEMOINE, cible : toutes à partir de mai).
- Proposition de solliciter M. LEMOINE pour un appui ponctuel après son départ, présentée comme une mesure de secours et non comme la solution.
- Mobilisation d'outils (wiki, base de connaissances, vidéos de démonstration), valorisée si elle est rattachée à un mode du modèle.

**Erreurs types**
- *Gestion des connaissances réduite à la GED* — réduire la gestion des connaissances à la rédaction de documents ou à une GED ; juste : dispositif systémique (outils, processus, culture) qui organise aussi la pratique partagée.
- Inverser les modes du modèle (l'externalisation va du tacite vers l'explicite) ; dater ou attribuer le modèle à tort (Polanyi a introduit la connaissance tacite, il n'est pas l'auteur du modèle SECI).
- Dispositif hors calendrier, qui commence après le départ de M. LEMOINE ou ignore sa contrainte de disponibilité.
- Confondre transfert des connaissances et gestion prévisionnelle des emplois (relève des ressources humaines, hors de la question).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Nonaka et Takeuchi, *The Knowledge-Creating Company* (1995) | modèle SECI | `nonaka_takeuchi_seci` / F06 § 1 | publié |

---

## DOSSIER 3 – INTELLIGENCE ARTIFICIELLE, TRAÇABILITÉ ET NUMÉRIQUE RESPONSABLE (10 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Projets d'intelligence artificielle | `1.3.d` Fonctionnement et usages des technologies émergentes : blockchain, registres distribués, IA, … ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. | 4 |
| 3.2 Traçabilité de l'origine locale | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain | 3 |
| 3.3 Indicateurs du numérique responsable | `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI | 3 |
| **Dossier 3 – Intelligence artificielle, traçabilité et numérique responsable** |  | **10** |

Répartition indicative : connaissances (familles d'IA, blockchain, Green IT et sobriété : items 3.1 a, 3.2 a, 3.3 a-1) 2,5 points ; qualification des projets au regard des textes datés, gouvernance, évaluation de la proposition de Tracéo, indicateurs 7,5 points. Durée conseillée : 10 points × 4,5 minutes = 45 minutes.

---

### 3.1 – Projets d'intelligence artificielle (4 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.d` « Fonctionnement et usages des technologies émergentes : blockchain, registres distribués, IA, … ».
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ».

**Annexes mobilisées** : annexes 3.1 (projets A, B et C), 3.3 (AI Act et RGPD datés) et 1.4 (témoignage de Mme PERRAULT).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Apprentissage automatique et IA générative distingués | 0,5 |
| a-2 | Projets A et B rattachés à l'apprentissage automatique, projet C à l'IA générative | 0,5 |
| b-1 | Projet A : risque minimal, contrôle du gérant ; mention de l'article 4 (maîtrise de l'IA) attendue pour au moins un projet | 0,5 |
| b-2 | Projet B, module de notation : haut risque (annexe III), obligations à compter du 02/12/2027, à anticiper ; analyse d'impact au titre du RGPD | 0,5 |
| b-3 | Projet B, option vidéo : pratique interdite depuis le 02/02/2025 | 0,5 |
| b-4 | Projet C : obligations de transparence depuis le 02/08/2026 ; risque propre (allergènes) | 0,5 |
| c | Deux mesures de gouvernance contextualisées (0,5 chacune) | 1 |

**Réponse indicative**

*3.1 a) – Deux familles d'IA*

L'apprentissage automatique regroupe les méthodes par lesquelles un modèle apprend, à partir de données, à prédire, classer ou noter ; ses résultats se mesurent par un taux d'erreur. L'IA générative, famille de l'apprentissage profond fondée sur de grands modèles pré-entraînés, produit des contenus nouveaux (textes, images) plausibles mais non garantis exacts, avec un risque propre d'hallucination (0,5 pt). Le projet A (prévision des commandes à partir des ventes, de la démarque et de la météo) et le module de notation du projet B (note de 0 à 100) relèvent de l'apprentissage automatique ; l'option vidéo du projet B relève aussi de modèles d'apprentissage, appliqués à l'image et à la voix ; le projet C (rédaction de fiches, agent conversationnel) relève de l'IA générative (0,5 pt).

*3.1 b) – Qualification au regard du règlement européen sur l'IA (annexe 3.3)*

Le règlement (UE) 2024/1689 classe les systèmes selon leur niveau de risque : pratiques interdites, haut risque, risque soumis à des obligations de transparence, risque minimal.
- **Projet A – prévision des commandes** : il ne figure ni parmi les pratiques interdites ni parmi les domaines à haut risque ; risque minimal : aucune obligation propre à ce niveau de risque, mais, comme pour tout système d'IA déployé, l'obligation de maîtrise de l'IA (article 4, depuis le 02/02/2025, assouplie par le règlement (UE) 2026/1744) : la coopérative prend des mesures pour former les gérants et les équipes qui utilisent le module. Le gérant valide chaque proposition, ce qui limite les effets d'une erreur ; l'enjeu est la qualité des données d'apprentissage, à commencer par la démarque, saisie par 31 magasins sur 46 seulement (dossier 1) (0,5 pt).
- **Projet B – module de notation des candidatures** : un système destiné au recrutement et à la sélection des candidats relève du haut risque de l'annexe III. Les obligations correspondantes s'appliquent à compter du 02/12/2027, date reportée par le règlement (UE) 2026/1744 : elles ne sont pas encore applicables en mars 2027 ; elles s'appliqueront au module s'il est mis en service à partir du 02/12/2027 ou s'il subit ensuite des modifications importantes (article 111 § 2 modifié par le règlement 2026/1744), ce qui est probable pour un logiciel en mode SaaS régulièrement mis à jour : il est prudent de les anticiper dès le choix de l'outil ; la coopérative, en tant qu'utilisatrice, devra assurer un contrôle humain effectif, utiliser le système conformément aux instructions de l'éditeur, en surveiller le fonctionnement et informer les candidats. Le traitement de leurs données relève dès maintenant du RGPD : un tel profilage justifie une analyse d'impact (0,5 pt).
- **Projet B – option « entretien vidéo augmenté »** : inférer la motivation ou la résistance au stress à partir des expressions du visage et de la voix est une reconnaissance des émotions sur le lieu de travail, interdite depuis le 02/02/2025 hors raisons médicales ou de sécurité ; les lignes directrices de la Commission (C(2025) 5052 final, point 254) étendent la notion de lieu de travail aux candidats pendant la sélection et le recrutement. L'option doit être refusée, quel que soit le gain de temps espéré par les gérants (0,5 pt).
- **Projet C – assistant et agent conversationnel** : les obligations de transparence s'appliquent depuis le 02/08/2026 : les clients du site doivent être informés qu'ils dialoguent avec une IA, et les contenus générés sont marqués par le fournisseur de l'outil. Au-delà du texte, les réponses sur les allergènes exposent la coopérative à une hallucination aux conséquences sanitaires : elles ne doivent provenir que des fiches produits validées, et les fiches rédigées doivent être relues avant publication (0,5 pt).

*3.1 c) – Deux mesures de gouvernance*

- **Comité IA et inventaire** : un comité réunissant la DSI, les ressources humaines, la direction du réseau, la communication et le délégué à la protection des données recense les usages, y compris ceux proposés par les éditeurs de logiciels déjà en place, et les classe selon les niveaux de risque du règlement avant toute activation ; décision immédiate : refuser l'option vidéo et conditionner le module de notation à une analyse d'impact (0,5 pt).
- **Contrôle humain et charte d'usage** : aucune candidature écartée sans examen par le gérant ; aucune réponse sur les allergènes générée hors des fiches validées ; charte interdisant la saisie de données personnelles de candidats ou de clients dans un outil non contractualisé ; formation des utilisateurs (maîtrise de l'IA) ; indicateur de suivi, par exemple la part des notes de présélection modifiées par les gérants ou le taux de fiches générées corrigées en relecture (0,5 pt).

**Réponses tolérées**
- Qualification de l'option vidéo comme système à haut risque plutôt qu'interdit, aucun point pour la qualification, mais 0,5 point sur l'item b-3 si le candidat recommande et justifie l'abandon de l'option (le barème de l'UE 5 est au pas de 0,5).
- Mention de la norme ISO/IEC 42001 (système de management de l'IA) comme cadre possible de la gouvernance, valorisée sans être exigée.
- Projet A analysé aussi sous l'angle de la sobriété (consommation du modèle) : valorisé, en lien avec la question 3.3.

**Erreurs types**
- *IA générative confondue avec l'apprentissage automatique* — confondre IA générative et apprentissage automatique ; juste : prédiction ou classement d'un côté, production de contenu de l'autre.
- *Statut réglementaire affirmé sans date* — dater faux le règlement : affirmer que les obligations du haut risque s'appliquaient dès 2026 ; juste : 02/12/2027 pour l'annexe III, après le report décidé par le règlement (UE) 2026/1744 (omnibus numérique).
- *Opportunités présentées sans les risques* — présenter les projets sans leurs risques, ou une gouvernance purement technique ; juste : rôles, validation humaine, charte, indicateurs.
- Oublier le RGPD pour le recrutement (analyse d'impact, information des candidats) ; renvoyer le droit des personnes en détail : il relève de l'UE 1.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2024/1689 (AI Act) | niveaux de risque, interdictions, transparence, haut risque | `ai_act` / F13 § 5 | en vigueur, application échelonnée |
| Règlement (UE) 2026/1744 (omnibus numérique sur l'IA) | report du haut risque de l'annexe III au 02/12/2027 ; article 4 et article 111 § 2 modifiés | `omnibus_numerique_ia` / F13 § 5.2 | en vigueur |
| Lignes directrices de la Commission sur les pratiques interdites, C(2025) 5052 final (29/07/2025), point 254 | lieu de travail étendu aux candidats | `ai_act_lignes_directrices_pratiques_interdites` | publié, non contraignant |
| RGPD, règlement (UE) 2016/679 | analyse d'impact, information des personnes | `rgpd` / F15 | en vigueur |
| ISO/IEC 42001:2023 | système de management de l'IA (réponse tolérée) | `iso_42001_2023` / F13 § 4 | en vigueur |

---

### 3.2 – Traçabilité de l'origine locale (3 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ».

**Annexes mobilisées** : annexes 3.1 (proposition de Tracéo, incident de septembre 2026, piste de la DSI), 1.4 (témoignage de Mme OUHIBI) et 1.1 (410 producteurs locaux).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Blockchain définie : registre partagé, consensus, blocs chaînés, ajout seul | 0,5 |
| a-2 | Distinction avec une base de données distribuée (administrateur unique, absence de consensus entre parties) | 0,5 |
| b-1 | Trois arguments d'évaluation tirés des annexes (0,5 chacun) | 1,5 |
| b-2 | Recommandation argumentée et alternative | 0,5 |

**Réponse indicative**

*3.2 a) – Blockchain et base distribuée*

Une blockchain est un registre distribué, répliqué chez plusieurs participants (nœuds), dans lequel les transactions sont regroupées en blocs horodatés et chaînés par une empreinte cryptographique, ajoutés selon une règle de consensus ; toute modification d'un bloc passé rompt la chaîne, ce qui rend le registre pratiquement inaltérable (0,5 pt). Une base de données distribuée répartit des données sur plusieurs serveurs sous l'autorité d'un administrateur unique, qui peut les modifier ; la blockchain, elle, organise la confiance entre des acteurs qui ne se font pas mutuellement confiance, au prix de la performance et de la complexité. La blockchain de consortium proposée par Tracéo est permissionnée : seuls des nœuds autorisés valident, par vote, sans minage (0,5 pt).

*3.2 b) – Pertinence de la proposition et recommandation*

Arguments (0,5 pt chacun, trois attendus) :
- **Le problème n'est pas l'intégrité du registre mais la vérité de la donnée saisie et de l'étiquette** : la fraude de septembre 2026 a eu lieu à l'étiquetage, en magasin ; une blockchain garantit que ce qui est enregistré n'est pas modifié, pas que ce qui est enregistré ou affiché est vrai (problème de l'« oracle ») ; un magasin pourrait toujours coller une étiquette « local » sur un lot importé.
- **Un tiers de confiance existe déjà** : la coopérative référence les producteurs, approvisionne les magasins et fixe les règles du réseau ; les cinq nœuds sont tenus par la coopérative et Tracéo, si bien que le registre est quasi centralisé, et Mme OUHIBI rappelle que les clients « croient sur parole » le réseau. Une base centralisée, auditée et journalisée, apporte la même preuve à moindre coût.
- **Coût et adoption** : 45 000 € HT puis 1 200 € HT par mois, soit 59 400 € HT la première année ; saisie lot par lot imposée à 410 producteurs, dont les deux tiers sont de très petites exploitations et 40 % n'utilisent pas de smartphone pour leur activité : saisies incomplètes ou tardives probables, qui videraient la preuve de son sens.
- **Points favorables, à mentionner** : consensus sans minage, donc consommation énergétique faible ; QR code utile pour la communication. Aucune donnée personnelle des producteurs exploitants individuels ne doit être inscrite en clair dans un registre inaltérable (RGPD).

Recommandation au conseil d'administration (0,5 pt) : ne pas lancer la blockchain de Tracéo en 2027. Traiter la cause : retenir la piste de la DSI (gestion des lots et des attestations d'origine dans l'ERP, contrôlées par sondage), faire produire les étiquettes « local » par la centrale à partir du numéro de lot, et non plus en magasin, contrôler les magasins et prévoir des sanctions dans le règlement intérieur de la coopérative ; publier l'origine par un QR code alimenté par l'ERP. Réexaminer une blockchain si un besoin multi-acteurs sans tiers de confiance apparaît, par exemple une filière partagée avec d'autres réseaux ou des transformateurs.

**Réponses tolérées**
- Recommandation d'un pilote limité à une filière (fraises, produits laitiers) avec des indicateurs d'adoption et de fraude, si les limites ci-dessus sont traitées.
- Typologie publique, privée, de consortium développée, si elle sert l'argumentation.
- Mention du vocabulaire normalisé des registres distribués (ISO 22739), sans en faire un argument.

**Erreurs types**
- *Blockchain confondue avec une base de données distribuée* — confondre blockchain et base de données distribuée ; juste : consensus entre parties qui ne se font pas confiance.
- *Opportunités présentées sans les risques* — présenter les seuls apports (transparence, image) sans les limites (oracle, coût, adoption, gouvernance du consortium).
- Présenter la blockchain comme une garantie de vérité de l'information ; juste : elle garantit l'intégrité de l'enregistrement.
- Hors sujet : développer le règlement MiCA ou la technique de programmation du registre ; aucun jeton n'est émis ni échangé dans le projet de Tracéo.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO 22739 — Chaînes de blocs et registres distribués, vocabulaire | définitions (réponse tolérée) | `iso_22739_2024` / F11 § 1 | en vigueur |
| RGPD, règlement (UE) 2016/679 | minimisation, données personnelles et registre inaltérable | `rgpd` / F11 § 2.3 | en vigueur |

---

### 3.3 – Indicateurs du numérique responsable (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI ».

**Annexes mobilisées** : annexes 3.2 (situation de 2026 et engagements 2029), 3.1 (projets d'IA), 2.1 (migration vers Nexalis) et 3.3 (loi REEN, RGESN).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Green IT et sobriété numérique définis et distingués | 0,5 |
| a-2 | Levier des équipements démontré à partir de l'annexe 3.2 (part de la fabrication, durée d'usage) | 0,5 |
| b | Quatre indicateurs à cinq champs, dont un pour l'hébergement chez Nexalis ou les projets d'IA (0,5 par indicateur) | 2 |

**Réponse indicative**

*3.3 a) – Green IT, sobriété et levier des équipements*

Le Green IT consiste à concevoir, acheter, utiliser et faire recycler les équipements et services numériques de façon à réduire leur impact environnemental (écoconception, mutualisation, allongement de la durée de vie, reconditionnement) ; la sobriété numérique interroge d'abord le besoin : renoncer aux équipements, aux données et aux usages qui n'apportent pas de valeur suffisante. Le premier réduit l'impact de ce que l'on fait, la seconde réduit ce que l'on fait ; aucune ne se réduit à l'économie d'énergie (0,5 pt).

En l'espèce, 72 % des 310 tCO2e du SI viennent de la fabrication des équipements, soit environ 223 tCO2e, alors que l'électricité de la salle informatique du siège en représente moins de 1 % (annexe 3.2) : la fermeture de la salle ne fera que déplacer une consommation modeste chez Nexalis. L'engagement de − 25 % (environ 78 tCO2e) passe donc par les équipements : porter la durée d'usage de 4 à 6 ans réduit d'un tiers les renouvellements annuels ; si l'on suppose que l'essentiel des émissions de fabrication tient aux postes et terminaux, annualisées sur leur durée d'usage, le gain atteint au plus un tiers de 223 tCO2e, soit environ 74 tCO2e par an à parc constant et en régime de croisière, l'ordre de grandeur de l'engagement de − 25 % (environ 78 tCO2e) ; le reconditionnement (5 % des achats en 2026, 30 % visés) réduit l'impact de chaque achat. La sobriété complète ce levier : ticket de caisse dématérialisé, stabilisation des 42 To stockés (+ 30 % par an), usages d'IA limités à ceux qui créent de la valeur (0,5 pt).

*3.3 b) – Quatre indicateurs*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Durée d'usage moyenne des postes remplacés | somme des durées d'usage des postes retirés du service / nombre de postes retirés | inventaire du parc de la DSI | annuelle | 6 ans en 2029 (4 ans en 2026) | environnement |
| Part d'équipements reconditionnés dans les achats | équipements reconditionnés achetés / équipements achetés dans l'année | achats informatiques, inventaire du parc | semestrielle | 30 % en 2029 (5 % en 2026) | environnement |
| Électricité consommée pour l'ERP et le portail hébergés chez Nexalis | consommation des serveurs affectés à la coopérative × indicateur d'efficacité énergétique (PUE) du centre de données | reporting environnemental de Nexalis, à rendre contractuel (avenant, question 2.2) | trimestrielle | au plus 38 MWh par an (niveau de la salle du siège en 2026), puis en baisse | environnement |
| Part des salariés sensibilisés au numérique responsable | salariés de la coopérative et des magasins ayant suivi la sensibilisation / effectif total | registre des formations des ressources humaines mutualisées | semestrielle | 80 % en 2029 (10 % en 2026) | social |

(0,5 pt par indicateur complet ; l'indicateur relatif à l'hébergement ou à l'IA est obligatoire.)

Ces indicateurs s'intègrent au tableau de bord SI à côté des indicateurs de coût et de qualité de service, et non dans une liste séparée ; les émissions totales du SI, recalculées chaque année selon la même méthode (Bilan Carbone, scopes 1 à 3), servent d'indicateur de résultat, les quatre ci-dessus d'indicateurs d'action.

**Réponses tolérées**
- Autres indicateurs complets et contextualisés : taux de tickets de caisse dématérialisés (cible 50 %), EcoIndex moyen du site de retrait (de E à C, en lien avec le RGESN), volume de données stockées (stabilisé à 42 To), consommation électrique par proposition de commande du projet A ou par millier de conversations de l'agent du projet C, émissions totales du SI (cible environ 230 tCO2e en 2029).
- Axe « processus » ou « gouvernance » s'il est justifié ; présentation sous forme de liste.

**Erreurs types**
- *Sobriété numérique réduite à l'économie d'énergie* — confondre sobriété numérique et économie d'énergie, ou sobriété et Green IT.
- *Empreinte du SI limitée à l'électricité* — limiter l'empreinte du SI à l'électricité ; juste : la fabrication des équipements (scope 3) domine, 72 % ici.
- *Indicateurs génériques* — indicateurs sans formule, source ou cible, ou isolés du tableau de bord SI.
- Considérer que la migration vers Nexalis supprime l'impact de l'hébergement : il est déplacé, et doit être mesuré par contrat.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Loi n° 2021-1485 du 15 novembre 2021 (REEN) | réduction de l'empreinte environnementale du numérique | `loi_reen` / F14 | en vigueur |
| RGESN, version 2 (2024) | écoconception des services numériques | `rgesn_2024` / F14 | en vigueur |
| EcoIndex | indicateur relatif d'une page web | `ecoindex` / F14 | en vigueur |
| Méthode Bilan Carbone | estimation des émissions du SI | `methode_bilan_carbone` / F14 | en vigueur |
| GHG Protocol | scopes 1, 2 et 3 | `ghg_protocol` / F14 | en vigueur |
