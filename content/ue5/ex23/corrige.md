# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 23 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, entrepôt et gouvernance, F08 décisionnel et visualisation, F03 cloud et souveraineté, F05 projets, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Entrepôt ou lac de données | `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) | 2,5 |
| 2.2 Fiabilité des données et échanges avec les grands comptes | `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) | 2 |
| 2.3 Chaîne de traitement et diagnostic du taux de service | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation | 4 |
| 2.4 Cycle de vie et hébergement des données | `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `2.3.d` Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique | 1,5 |
| 2.5 Planification et risques du projet « Pilotage des missions » | `1.5.d` Planification des ressources, délais, coûts et qualité ; `1.5.e` Identification et gestion des risques (maintenance, évolutivité, sécurité) ; `1.5.a` Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable | 3 |
| **Dossier 2 – Organiser et exploiter les données des commandes et des missions** |  | **13** |

Répartition indicative : connaissances (entrepôt et lac de données, dictionnaire de données, chaîne de traitement, cycle de vie, souveraineté numérique) environ 2,5 points (items 2.1 a-1, 2.2 a-1, 2.3 a-1, 2.4 a-1 et la définition de 2.4 b) ; analyse des annexes et recommandations environ 10,5 points, soit environ 80 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Entrepôt ou lac de données (2,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) ». La modélisation des données n'est pas demandée.

**Annexes mobilisées** : annexes 2.3 A et B (objectif, deux options, position de M. DUQUESNEL), 2.1 (sources, formes et volumes des données, constats de qualité), 1.1 (46 agences, aucune équipe d'analyse des données, budget du SI) et 2.4 (RGPD, minimisation).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Entrepôt de données et lac de données définis et distingués (données intégrées et structurées avant le chargement pour le pilotage ; données brutes de toute forme, structurées à la lecture, pour l'exploration) | 0,5 |
| a-2 | Quatre critères (finalité, structuration, utilisateurs, coûts) appliqués aux deux options de l'annexe 2.3 B, avec les montants ; 0,5 pour deux critères | 1 |
| b-1 | Recommandation de l'entrepôt de données, justifiée par trois besoins tirés des annexes | 0,5 |
| b-2 | Réponse argumentée à M. DUQUESNEL par au moins deux arguments tirés des annexes (valeur non démontrée sans finalité ni analyste, coût de fonctionnement, qualité des données, minimisation et durées de conservation des données personnelles) | 0,5 |

**Réponse attendue**

*2.1 a) – Comparaison des deux architectures*

Un **entrepôt de données** est une base orientée sujet, intégrée, historisée et non volatile, destinée à l'analyse : les données de plusieurs applications y sont extraites, nettoyées et rapprochées selon des définitions communes **avant** d'être chargées dans un modèle fixé à l'avance (schéma défini à l'écriture). Un **lac de données** conserve des données **brutes** de toutes formes (structurées, textes, documents, images), sans transformation à l'entrée ; leur structure n'est définie qu'au moment de chaque analyse (schéma défini à la lecture) ; sans gouvernance, il devient un « marécage de données » (F07 § 6.2) (0,5 pt).

| Critère | Option 1 – Entrepôt de données | Option 2 – Lac de données |
|---|---|---|
| **Finalité** | pilotage par des indicateurs stables et comparables : taux de service, délai de pourvoi, fidélisation des intérimaires, par agence, secteur, métier et client, historisés depuis 2024 | exploration de données variées pour des questions qui ne sont pas encore posées (« nous ne savons pas encore ce que nous en ferons ») |
| **Structuration** | données structurées des trois applications (100 milliers de commandes, 140 milliers de contrats, 300 milliers de relevés d'heures par an) ; règles de transformation fixées une fois (définition unique de la commande pourvue, liste unique des codes métiers, dédoublonnage des candidats) | toutes les données, y compris les 150 milliers de documents, les curriculum vitae, les 40 milliers de notes en texte libre et les courriels ; préparation à chaque analyse, avec les défauts actuels (quatorze libellés de cariste, 10 % de doublons) |
| **Utilisateurs** | 46 directeurs d'agence et leurs chargés de recrutement, comité de direction, contrôle de gestion : des utilisateurs métiers, non spécialistes, qui consultent des tableaux de bord prêts à l'emploi | un analyste de données, à recruter : QUENTALIS Emploi n'en compte aucun ; les agences n'auraient pas d'accès direct |
| **Coûts** (k€, hors temps interne) | mise en place 120 ; fonctionnement 30 par an, plus 40 (H1) ou 60 (H2) d'hébergement, soit 70 à 90 par an | mise en place 80 ; fonctionnement 90 par an (dont l'analyste, 70), plus 30 ou 50 d'hébergement, soit 120 à 140 par an ; mise en place puis trois années de fonctionnement avec H2 : environ 500, contre 390 pour l'entrepôt |

(0,5 pt pour deux critères appliqués, 1 pt pour les quatre.)

Le lac est moins cher à mettre en place (80 contre 120 k€) parce qu'il reporte le travail de préparation sur chaque analyse ; il coûte plus cher à faire vivre (analyste, stockage de données volumineuses), et ne produit pas par lui-même les tableaux de bord hebdomadaires des agences.

*2.1 b) – Recommandation et réponse à M. DUQUESNEL*

**Recommandation : l'entrepôt de données (option 1)**, justifiée par trois besoins (0,5 pt) :
1. **Des indicateurs comparables entre agences** : l'objectif de 90 % en 2028 est « mesuré de la même façon dans toutes les agences » (annexe 2.3 A) ; aujourd'hui chaque agence a sa définition de la commande pourvue (annexe 2.1 C) ; l'entrepôt impose les définitions communes au chargement, le lac les laisserait à chaque analyse.
2. **Des restitutions régulières pour des utilisateurs non spécialistes** : un tableau de bord hebdomadaire pour chacune des 46 agences et un tableau de bord mensuel pour la direction, qui reçoit aujourd'hui le taux du réseau trois semaines après la fin du mois ; c'est l'usage type de l'entrepôt.
3. **Des moyens limités et des données surtout structurées** : aucune compétence d'analyse de données en interne, une équipe informatique de neuf personnes qui doit faire fonctionner l'existant ; les données utiles au pilotage sont déjà structurées dans le logiciel de gestion et les portails ; les volumes, de quelques centaines de milliers de lignes par an, ne relèvent pas du Big Data.

**Réponse à M. DUQUESNEL** (0,5 pt) : « tout garder » n'est pas une stratégie de données. La valeur d'une donnée tient à son usage : sans question à traiter, sans analyste et sans données fiables (doublons, codes métiers, notes en texte libre), le lac accumulerait des coûts (90 k€ par an hors hébergement) sans produire de décision. Il contredit en outre la **minimisation** et la **limitation de la conservation** des données personnelles (annexe 2.4 ; durées de l'annexe 2.3 G) : conserver sans finalité les curriculum vitae, les notes sur les intérimaires (« à ne plus proposer chez tel client ») et les courriels des clients exposerait QUENTALIS Emploi. Une ouverture reste possible : une fois l'entrepôt fiable et la gouvernance des données en place, un espace d'exploration limité à une question précise (par exemple les causes des commandes non pourvues dans la logistique) pourra être envisagé, avec les seules données nécessaires.

**Réponses tolérées**
- Entrepôt défini par les quatre caractéristiques d'Inmon (orienté sujet, intégré, historisé, non volatil) sans les nommer, si l'idée de données intégrées et historisées pour l'analyse apparaît.
- Recommandation d'une architecture mixte (entrepôt pour le pilotage, lac plus tard pour l'exploration) ou d'une architecture unifiée de type « lakehouse », si le pilotage des agences par l'entrepôt est prioritaire et si le lac est borné par une finalité et par les durées de conservation.
- Coûts comparés sur une autre durée ou sans l'hébergement, si les ordres de grandeur sont justes et si le coût de l'analyste est pris en compte.
- Mention d'un référentiel de données maîtres (candidats, clients, métiers) comme complément de l'entrepôt.

**Erreurs fréquentes**
- *Entrepôt et lac confondus* (`ET-24`) — « le lac est un entrepôt moderne, plus complet » ; juste : finalités, structuration et utilisateurs différents.
- *Comparaison sans application au cas* (`JUR-T01` contextualiser chaque notion) — tableau de cours sans les montants, les utilisateurs ni les données de l'annexe 2.3 B.
- *Choix fondé sur le seul coût de mise en place* — retenir le lac parce qu'il coûte 80 k€ au lieu de 120 k€ ; juste : coût de fonctionnement, analyste à recruter, absence de restitutions pour les agences.
- *Modélisation des données* (schéma en étoile, tables de faits et de dimensions détaillées) — non demandée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Entrepôt, lac, référentiel de données maîtres : choisir | définitions, critères de comparaison | F07 § 6.2 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | minimisation, limitation de la conservation (annexe 2.4) | `rgpd` / F15 | applicable depuis le 25/05/2018 |

---

### 2.2 – Fiabilité des données et échanges avec les grands comptes (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) ». Limites : l'interopérabilité est abordée sur le plan technique et sur le plan organisationnel ; le détail technique des échanges est exclu.
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) » (propriétaires, intendants, instance de gouvernance). Limite : le rôle du *Chief Data Officer* et la structuration de la gouvernance sont illustratifs, non normatifs.

**Annexes mobilisées** : annexes 2.1 B et C (relevés d'heures des grands comptes, constats de qualité), 2.2 (définition du taux de service), 2.3 A et F (objectif de 90 %, exigences de qualité), 2.4 (DAMA-DMBOK) et 1.1 (organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Dictionnaire de données défini ; six rubriques de la consigne renseignées pour la commande pourvue et pour le taux de service | 0,5 |
| a-2 | Trois règles de qualité, chacune rattachée à un constat de l'annexe 2.1 C et assortie d'un contrôle | 0,5 |
| a-3 | Propriétaires métiers et intendants désignés pour les données du projet, la DSI administrant sans être propriétaire | 0,5 |
| b | Échanges des relevés d'heures : intérêt montré par rapport à l'annexe 2.1 B ; plan technique (API, format ouvert ou portail selon le profil des grands comptes) et plan organisationnel (convention d'échange, responsables) | 0,5 |

**Réponse attendue**

*2.2 a) – Dictionnaire, règles de qualité et responsables*

Le **dictionnaire de données** est le document de référence, partagé et gouverné, qui décrit chaque donnée utilisée : son nom, sa définition métier, sa règle de gestion ou de calcul, son format et ses valeurs admises, sa source, son propriétaire et sa fréquence de mise à jour. Il donne le même sens à une donnée dans toutes les agences et toutes les restitutions (F07 § 1 et § 8 ; métadonnées dans le DAMA-DMBOK).

| Rubrique | Commande pourvue | Taux de service |
|---|---|---|
| Définition métier | commande dont tous les postes demandés sont occupés, le premier jour prévu, par un intérimaire présent | part des commandes reçues qui ont été entièrement pourvues |
| Règle de gestion ou formule | statut fixé à la fin du premier jour prévu ; postes demandés et postes occupés enregistrés ; une commande annulée par le client avant le début de la mission n'est ni pourvue ni non pourvue | commandes entièrement pourvues / (commandes reçues − commandes annulées par le client avant le début de la mission) ; indicateur complémentaire : postes occupés / postes demandés |
| Valeurs admises | entièrement pourvue, partiellement pourvue, non pourvue, annulée par le client | pourcentage de 0 à 100 % |
| Source | logiciel de gestion : commande (date et heure de réception), contrat de mission, confirmation de présence le premier jour | entrepôt, alimenté chaque nuit par le logiciel de gestion |
| Propriétaire | directeur du réseau et des agences | directeur du réseau et des agences |
| Fréquence de mise à jour | quotidienne | hebdomadaire pour les agences, mensuelle pour la direction |
| Cible, exemple | une commande de dix caristes dont huit sont présents est « partiellement pourvue » (Lens) | 90 % en 2028, selon cette seule définition (85 % en 2026 selon des définitions hétérogènes) ; axe client |

(0,5 pt pour la définition et les rubriques appliquées aux deux données.)

**Trois règles de qualité** (0,5 pt) :

| Règle | Constat de l'annexe 2.1 C | Dimension de la qualité | Contrôle |
|---|---|---|---|
| 1. Toute commande est saisie dans le logiciel de gestion dès sa réception, avec sa date et son heure, qu'elle soit pourvue ou non ; les tableurs de suivi des commandes non pourvues sont supprimés après leur reprise | 4 milliers de commandes jamais saisies ; heure de réception absente pour environ 40 % des commandes | complétude, actualité | part des commandes saisies dans l'heure de leur réception : cible 95 % fin 2027 |
| 2. Toute commande porte un code de la liste unique des métiers ; les 250 codes locaux sont rattachés à cette liste ; le code « autre » est réservé aux cas validés par l'intendant | 650 codes en usage, quatorze libellés de cariste, 25 % de « autre » | cohérence, validité | part des commandes codées dans la liste unique hors « autre » : cible 98 % à la mise en production |
| 3. Un contrôle de doublon est fait à l'inscription d'un candidat (nom, date de naissance, téléphone ou courriel) ; les fiches en double sont fusionnées par l'agence de rattachement | environ 8 000 doublons (10 % des fiches) | unicité | taux de doublons de candidats : cible moins de 1 % fin 2027 |

**Responsables de la donnée** (0,5 pt), à titre illustratif (le programme n'impose aucune organisation) :
- **propriétaires** (responsables métiers, qui fixent les définitions, les règles et les droits d'accès) : le directeur du réseau et des agences pour les commandes, les missions et les candidats ; la responsable du centre de services pour les relevés d'heures et la facturation ; le directeur commercial et des grands comptes pour les données des clients ;
- **intendants** (qui appliquent les règles au quotidien, corrigent et animent) : les six référents d'agence pendant le projet, puis un correspondant dans chaque agence ;
- la **direction des systèmes d'information** administre l'entrepôt, les flux et les droits, sans être propriétaire des données ; le délégué à la protection des données veille au respect des durées de conservation ;
- en complément, non exigé par la consigne, une **instance de gouvernance des données** (trimestrielle, présidée par la directrice générale ou par son représentant, avec les propriétaires, le directeur des systèmes d'information et le contrôleur de gestion) valide le dictionnaire, suit les indicateurs de qualité et arbitre les désaccords de définition. Le DAMA-DMBOK, référentiel de bonnes pratiques, place cette gouvernance au centre de la gestion des données.

*2.2 b) – Échanges des relevés d'heures avec les grands comptes*

L'**interopérabilité** est la capacité de systèmes différents à échanger des données et à les utiliser sans ressaisie ; elle est technique (API, formats), sémantique (même sens des données) et organisationnelle (engagements et responsabilités des parties) (F07 § 7). Une **API** est une interface documentée qui permet à une application d'échanger des données avec une autre de manière automatisée ; un **format ouvert** est un format dont la spécification est publique, qui ne dépend pas d'un éditeur ou d'un client (0,5 pt pour l'ensemble de la réponse b).

- **Plan technique** : relier par API les grands comptes qui disposent d'un logiciel de gestion des temps, en commençant par les trois volontaires, puis les dix qui envoient aujourd'hui un fichier dans leur format propre ; à défaut, faire déposer les relevés dans le **format ouvert et standardisé** publié par l'éditeur, qui remplace les dix macros propres à chaque client ; faire saisir ou valider les relevés sur le portail des clients par les douze grands comptes qui écrivent par courriel.
- **Plan sémantique** : un référentiel commun aux deux parties (identifiant du contrat de mission et de l'intérimaire, types d'heures, période) pour que chaque heure se rattache sans interprétation.
- **Plan organisationnel** : une convention d'échange avec chaque grand compte (données transmises, échéance hebdomadaire, contrôles, traitement des anomalies, interlocuteurs), portée par le directeur commercial et des grands comptes auprès des clients et par la responsable du centre de services, propriétaire des relevés ; suivi de la part des relevés reçus sous forme structurée.
- **Gains** : 70 milliers de relevés par an aujourd'hui ressaisis ou retraités, le temps de trois personnes du centre de services, 1 500 avoirs de 2026, une facturation plus rapide ; et, pour le projet, des heures fiables et disponibles chaque nuit dans l'entrepôt.

**Réponses tolérées**
- Autres rubriques du dictionnaire (exemples, date de validation, durée de conservation, niveau de sensibilité), si les principales sont présentes.
- Autre définition de la commande pourvue (à la signature du contrat, par exemple), si elle est unique, précise et justifiée, et si le cas des commandes partielles et annulées est réglé ; taux de service calculé en postes plutôt qu'en commandes, s'il est défini sans ambiguïté.
- Deuxième donnée clé traitée sous l'angle du code métier ou du délai de pourvoi en plus du taux de service.
- Règle de qualité portant sur la définition de la commande pourvue (constat 1) à la place de l'une des trois règles ; dimensions de la qualité nommées d'après ISO/IEC 25012.
- Mention d'un responsable des données au niveau de la direction générale (*Chief Data Officer*), si elle est présentée comme une possibilité et non comme une obligation.
- Échange de données informatisé ou portail présenté comme solution pour une partie des grands comptes, si le principe du format structuré et commun est respecté.

**Erreurs fréquentes**
- *Dictionnaire réduit à une liste de champs techniques* (type, longueur) — sans définition métier, propriétaire ni règle de gestion ; juste : le sens partagé de la donnée.
- *Interopérabilité seulement technique* (`ET-36`) — API sans convention d'échange, sans référentiel commun ni responsable.
- *Détail technique des échanges* — description des messages, des méthodes d'appel ou de l'authentification d'une API ; non attendu.
- *La DSI propriétaire des données* — juste : propriétaires métiers, la DSI administre.
- *DAMA-DMBOK présenté comme une norme ou un logiciel* (`ET-01`) — juste : référentiel de bonnes pratiques.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Dictionnaire de données, rôles (propriétaire, intendant), qualité | définitions, règles, responsables | F07 § 1 et § 8.1 à 8.3 | notion de cours |
| DAMA-DMBOK, 2e édition (2017), révision 2024 (DAMA International) | gouvernance au centre de la gestion des données (annexe 2.4) | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| ISO/IEC 25012 (2008) — Modèle de qualité des données | dimensions de la qualité, en réponse tolérée | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| Interopérabilité : technique, sémantique, organisationnelle ; API, formats ouverts | échanges des relevés d'heures | F07 § 7 | notion de cours |

---

### 2.3 – Chaîne de traitement et diagnostic du taux de service (4 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.d` « Outils décisionnels » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique ». Limites : « L'usage des outils ne dispense pas d'une lecture critique des corrélations et biais » ; « L'interprétation doit être reliée à la stratégie globale ». Aucun calcul statistique ni aucune manipulation d'outil.

**Annexes mobilisées** : annexes 2.2 (taux de service par secteur et par agence, deux lectures), 2.1 (sources, constats de qualité, restitution actuelle) et 2.3 (objectif, restitutions prévues, exigences de qualité).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de traitement définie comme une démarche organisée en cinq étapes | 0,5 |
| a-2 | Cinq étapes appliquées au projet (sources, nettoyage, entrepôt, indicateurs, tableaux de bord des agences et de la direction) | 0,5 |
| a-3 | Outil de visualisation décisionnelle connecté à l'entrepôt, justifié par les besoins des restitutions (par exemple au regard des tableurs actuels) | 0,5 |
| b-1 | Trois constats chiffrés tirés de l'annexe 2.2, avec une hypothèse d'explication pour chacun ; 0,5 pour deux constats avec leur hypothèse | 1 |
| b-2 | Deux précautions de lecture et appréciation argumentée de la proposition de M. HAVERCQ | 0,5 |
| c-1 | Méthode descriptive pour le suivi hebdomadaire, exploratoire pour la recherche des causes, justifiées | 0,5 |
| c-2 | Deux représentations visuelles adaptées à leur destinataire et justifiées | 0,5 |

**Réponse attendue**

*2.3 a) – Chaîne de traitement et outil décisionnel*

La **chaîne de traitement des données** est la suite organisée des opérations qui transforment des données brutes, issues de sources hétérogènes, en informations fiables restituées à ceux qui décident : collecte, nettoyage, structuration, analyse, restitution. C'est une démarche, non un outil : chaque étape a ses règles, ses responsables et ses contrôles, et la qualité du résultat dépend du maillon le plus faible (F08 § 1) (0,5 pt).

| Étape | Chaîne du projet « Pilotage des missions » |
|---|---|
| **Collecte** | extraction chaque nuit, par les interfaces des applications, des commandes, contrats de mission, relevés d'heures et factures du logiciel de gestion, des fiches du portail des intérimaires et des commandes et validations du portail des clients ; reprise unique des tableurs des agences pendant le nettoyage, puis abandon de ces tableurs |
| **Nettoyage** | application des règles du dictionnaire : dédoublonnage des candidats, rattachement des codes locaux à la liste unique des métiers, contrôle des commandes sans date ni heure de réception, statut de la commande selon la définition unique ; journal des rejets (au plus 1 % des lignes, chaque rejet expliqué) |
| **Structuration** | chargement dans l'entrepôt, historisé depuis 2024 : faits (commandes, missions, heures) analysés selon des axes communs (date, agence, secteur et client, métier) ; calcul des indicateurs selon le dictionnaire ; rapprochement mensuel du nombre de commandes avec le logiciel de gestion |
| **Analyse** | taux de service, délai de pourvoi, commandes non pourvues, missions renouvelées et intérimaires délégués de nouveau, par agence, secteur, métier et client, comparés à la cible de 90 % et à la période précédente |
| **Restitution** | tableau de bord hebdomadaire de chaque agence (données de la veille disponibles à 7 heures, accès limité à l'agence et aux totaux du réseau), tableau de bord mensuel de la direction ; puis décisions et actions (plan d'action des agences, revue en comité de direction) |

(0,5 pt pour la chaîne appliquée.)

**Outil décisionnel adapté** (0,5 pt) : un **outil de visualisation décisionnelle** (informatique décisionnelle en libre-service gouverné), connecté à l'entrepôt : rafraîchissement automatique chaque nuit, publication à 46 agences et à la direction, droits d'accès par agence, indicateurs calculés une seule fois selon le dictionnaire, filtres par secteur, métier et client. Le tableur avancé, outil actuel, ne convient pas à ces restitutions : un classeur par agence, des définitions divergentes, des versions multiples, une synthèse obtenue trois semaines après la fin du mois ; il reste utile pour des analyses ponctuelles du contrôle de gestion à partir de l'entrepôt. L'outil ne suffit pas : il suppose des définitions partagées, des propriétaires et la formation des directeurs d'agence (l'informatique décisionnelle est une démarche).

*2.3 b) – Diagnostic du taux de service*

**Trois constats et leurs hypothèses** (1 pt) :
1. **Une baisse de trois points concentrée sur la logistique.** Le taux du réseau passe de 88 % à 85 % ; l'industrie (90 %) et le bâtiment (89 % → 90 %) sont stables, la logistique perd sept points (87 % → 80 %) et le tertiaire deux (82 % → 80 %). La logistique pèse 40 % des commandes mais 8 des 15 milliers de commandes non pourvues, plus de la moitié. *Hypothèse* : des commandes passées très tard et pour plusieurs postes à la fois (délai moyen de pourvoi d'un jour, d'une demi-journée à Lens ; commandes « la veille à 17 heures pour le lendemain à 5 heures ») : l'agence doit trouver dans la soirée plusieurs intérimaires disponibles, ce que l'absence de disponibilités enregistrées rend difficile.
2. **Le taux de service est plus faible là où les intérimaires sont moins fidélisés.** Dans la logistique, 30 % des missions sont renouvelées et 50 % des intérimaires sont délégués de nouveau dans les trois mois, contre 50 % et 70 % dans l'industrie ; à Lens, 25 % et 40 %, contre 60 % et 80 % à Évreux. *Hypothèse* : faute d'être rappelés à la fin de leur mission, les intérimaires de la logistique ne restent pas dans le vivier de QUENTALIS Emploi (« nous les perdons ») ; l'agence doit alors chercher de nouveaux candidats à chaque commande urgente. C'est une corrélation : la nature des missions (courtes, pour des pointes d'activité) peut expliquer à la fois une fidélisation et un taux de service plus faibles.
3. **Les écarts entre agences mêlent performance et mesure.** Évreux affiche 95 % et Lens 75 %, vingt points d'écart ; mais Lens applique la définition la plus stricte (intérimaire présent le premier jour, commande partielle comptée comme non pourvue), Évreux la plus large (candidat proposé, commandes annulées exclues), et Saint-Quentin ne saisit pas toutes ses commandes non pourvues. Les profils diffèrent aussi : 70 % des commandes de Lens viennent de la logistique, 60 % de celles d'Évreux de l'industrie. *Hypothèse* : une partie de l'écart tient à la définition et au secteur, non à la qualité du travail de l'agence ; comparée à la logistique du réseau (80 %, selon des définitions elles-mêmes hétérogènes), Lens reste en dessous, mais l'écart réel est bien inférieur à vingt points.

(0,5 pt pour deux constats chiffrés avec leur hypothèse, 1 pt pour trois.)

**Deux précautions de lecture et appréciation de la proposition de M. HAVERCQ** (0,5 pt) :
- *Des données incomplètes et hétérogènes* : chaque agence a sa définition, et environ 4 000 commandes non pourvues n'ont jamais été saisies ; en les réintégrant, le taux du réseau serait plutôt de l'ordre de 82 % (85 milliers sur 104), et non de 85 %. Le délai de pourvoi est fragile : l'heure de réception manque pour environ 40 % des commandes.
- *Des comparaisons à manier avec prudence* : deux années seulement, des moyennes qui masquent la dispersion entre clients et entre métiers, un effet de structure (une agence orientée vers la logistique paraît moins performante qu'une agence orientée vers l'industrie) et des corrélations qui ne prouvent pas de causalité ; le biais de confirmation guette celui qui cherche dans les chiffres la preuve d'une conviction (« la méthode d'Évreux »).

*La proposition de M. HAVERCQ* : l'objectif de 90 % est celui du plan, mais **le classement mensuel des agences est prématuré**. Établi sur ces chiffres, il récompenserait la définition la plus large et pénaliserait les agences qui mesurent strictement ; il inciterait Lens à changer de définition plutôt que de pratiques (effet pervers), comme le dit Mme DESVRAINE. Il faut d'abord la définition unique du dictionnaire et la saisie de toutes les commandes, puis des cibles par secteur ou des comparaisons entre agences de profil voisin ; ce que fait Évreux pour fidéliser ses intérimaires mérite d'être étudié, mais n'est pas démontré par ces seuls chiffres.

*2.3 c) – Méthodes d'analyse et représentations visuelles*

**Méthodes** (0,5 pt) :
- **Suivi hebdomadaire des agences : analyse descriptive.** Il s'agit de constater ce qui s'est passé (taux de service, délai, commandes non pourvues de la semaine), de le comparer à la cible et à la période précédente, avec des indicateurs stables et définis une fois pour toutes ; le directeur d'agence agit sur ce constat.
- **Causes de la baisse dans la logistique : analyse exploratoire.** Il s'agit de chercher pourquoi, sans hypothèse arrêtée : croiser le taux de service avec le délai entre la commande et le début de la mission, le nombre de postes par commande, le métier, le client, l'heure de la commande et la fidélisation des intérimaires, repérer des régularités et des cas atypiques. Les pistes trouvées sont à vérifier avec les agences avant d'en tirer des décisions. Une analyse prédictive n'est pas adaptée aujourd'hui : les données ne sont ni fiables ni homogènes, et QUENTALIS Emploi ne compte aucun analyste de données.

**Deux représentations visuelles** (0,5 pt) :
- **Pour les directeurs d'agence** : une **jauge ou une barre de progression** du taux de service de la semaine par rapport à la cible de 90 %, accompagnée d'un **diagramme en barres horizontales triées** des commandes non pourvues de la semaine par métier ou par client. Le directeur voit d'un coup d'œil s'il atteint la cible et où agir ; les barres triées se lisent sans calcul.
- **Pour le comité de direction** : des **courbes mensuelles du taux de service par secteur** (quatre courbes, sur au moins douze mois), avec la ligne de la cible de 90 %, sur un axe dont l'origine est indiquée et qui n'amplifie pas artificiellement les écarts. Le comité voit la tendance, le décrochage de la logistique et l'écart à l'objectif du plan. Un classement brut des agences, un diagramme circulaire ou un graphique en trois dimensions sont à éviter.

**Réponses tolérées**
- Chaîne présentée avec le vocabulaire décisionnel (collecte, ETL, entrepôt, restitution), si les cinq étapes du programme y figurent ; la décision et l'action ajoutées comme sixième étape.
- Autres constats tirés de l'annexe 2.2, s'ils sont chiffrés : délai de pourvoi plus long dans le tertiaire (4 jours) pour un taux de service bas, ou situation de Saint-Quentin, stable à 90 % mais dont le taux est surestimé.
- Autres hypothèses plausibles et présentées comme telles : manque de caristes disponibles, horaires des agences, pratiques des clients qui passent commande à plusieurs agences.
- Autre précaution : faiblesse de l'échantillon des trois agences (8 500 commandes sur 100 000), taux reconstitué non calculé si le sens de l'effet (surestimation) est donné.
- Acceptation de l'objectif de 90 % pour chaque agence, si la définition unique et la saisie complète sont posées comme préalables et si le classement est rejeté ou différé.
- Représentation pour la direction sous forme de barres groupées par agence et par secteur, de carte des agences en taux (et non en volumes) ou de tableau croisé avec mise en forme conditionnelle, si le choix est justifié et les biais évités ; outil cité comme exemple de catégorie, jamais comme solution en soi.

**Erreurs fréquentes**
- *Informatique décisionnelle réduite à un outil* (`JUR-D02` BI réduite à un simple outil ; `ET-05`) — « il suffit d'acheter un outil de visualisation » ; juste : chaîne, définitions, propriétaires, formation.
- *Corrélation présentée comme causalité* (`ET-26`) — « la fidélisation fait le taux de service » ; juste : hypothèse à vérifier, facteur commun possible.
- *Lecture des chiffres sans critique de leur production* (`JUR-D06` prudence d'interprétation) — comparer Évreux et Lens sans voir que leurs définitions diffèrent ; reprendre le classement de M. HAVERCQ.
- *Constats non chiffrés ou paraphrase de l'annexe* (`JUR-T03` analyser, ne pas décrire) — juste : constat, hypothèse, conséquence pour la décision.
- *Calcul statistique ou analyse prédictive proposée* — non demandés, et non adaptés à des données non fiables.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne décisionnelle : collecte, nettoyage, structuration, analyse, restitution | définition et application | F08 § 1 | notion de cours |
| Analyses descriptive, exploratoire, prédictive | choix de la méthode | F08 § 2 | notion de cours |
| Choix et critique d'une représentation ; biais de lecture ; corrélation et causalité | représentations, précautions | F08 § 5 | notion de cours |
| Outils décisionnels en principe (tableur avancé, outils de visualisation) | choix de l'outil | F08 § 6 | notion de cours |

---

### 2.4 – Cycle de vie et hébergement des données (1,5 point)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression » ; `2.3.d` « Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique ». Limites : « L'expertise technique des infrastructures (serveurs, réseaux) n'est pas attendue » ; aucune analyse juridique, les durées de conservation sont données.

**Annexes mobilisées** : annexes 2.3 C et G (options d'hébergement, données concernées, exigence d'un grand compte, durées de conservation), 2.1 C (fiches sans contact, notes des agences), 2.4 (RGPD, Data Act, SecNumCloud) et 1.1 (budget du SI).

**Barème indicatif (1,5 pt)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cinq étapes du cycle de vie présentées et appliquées aux données des candidats et des intérimaires, avec les durées de l'annexe 2.3 G | 0,5 |
| a-2 | Deux écarts entre la pratique et les durées, tirés des annexes (par exemple les fiches sans contact depuis plus de deux ans et les notes des agences jamais supprimées), avec leur conséquence pour le projet | 0,5 |
| b | Souveraineté numérique définie ; deux options appréciées selon les trois critères de la consigne ; recommandation justifiée par le cas (sensibilité des données, exigence du grand compte) | 0,5 |

**Réponse attendue**

*2.4 a) – Cycle de vie des données des candidats et des intérimaires*

Le **cycle de vie des données** décrit les étapes qu'une donnée traverse, de sa création à sa suppression, avec pour chacune une règle, un lieu et un responsable (F07 § 8.4).

| Étape | Données des candidats et des intérimaires de QUENTALIS Emploi |
|---|---|
| **Création** | inscription sur le portail des intérimaires ou en agence, dépôt des documents, création d'une seule fiche par personne (contrôle de doublon) et des seules données nécessaires |
| **Stockage** | base active du logiciel de gestion et du portail ; dans l'entrepôt, les seules données utiles au pilotage, avec un accès limité selon l'agence |
| **Usage** | recherche et proposition des candidats, délégation, relevés d'heures et facturation, pilotage du taux de service et de la fidélisation dans l'entrepôt |
| **Archivage** | contrats de mission et relevés d'heures archivés, avec un accès réservé au centre de services, jusqu'à la fin de la cinquième année qui suit la fin de la mission |
| **Suppression** | fiche et documents d'un candidat jamais délégué deux ans après le dernier contact ; fiche et documents non liés à une mission deux ans après la dernière mission d'un intérimaire ; contrats et relevés à la fin de l'archivage ; seules les statistiques qui ne permettent plus d'identifier une personne sont conservées sans limite |

(0,5 pt.)

**Deux écarts et leur conséquence pour le projet** (0,5 pt) :
1. **Environ 24 000 fiches (30 %) sans mission ni contact depuis plus de deux ans** : selon la politique interne, celles des candidats jamais délégués et des intérimaires sans mission depuis deux ans auraient dû être supprimées. *Conséquence* : purger ces fiches **avant** le nettoyage et le chargement (tâche C), plutôt que de les dédoublonner et de les charger dans l'entrepôt ; programmer ensuite la suppression automatique à l'échéance, dans les applications sources comme dans l'entrepôt.
2. **Les notes des agences sur les intérimaires ne sont couvertes par aucune durée et ne sont jamais supprimées** ; en texte libre, elles contiennent des appréciations sur les personnes. *Conséquence* : ne pas les charger dans l'entrepôt (et ne pas les verser dans un lac) ; demander au délégué à la protection des données et au propriétaire des données de compléter la politique, puis structurer ce qui est utile (par exemple des disponibilités) et purger le reste. La durée de conservation devient une rubrique du dictionnaire de données.

*2.4 b) – Souveraineté numérique et choix de l'hébergement*

La **souveraineté numérique** est la capacité d'une organisation à garder la maîtrise de ses données et de ses traitements : leur localisation, le droit auquel est soumis celui qui les héberge, sa dépendance à l'égard d'un fournisseur (réversibilité) et ses compétences (F07 § 8.5 ; F03 § 5.3). Elle ne se réduit pas à la localisation des centres de données.

| Critère | H1 – Fournisseur de cloud public | H2 – Prestataire français |
|---|---|---|
| Droit applicable | soumis au droit de son pays d'origine, qui peut permettre à ses autorités de demander l'accès aux données, même hébergées dans l'Union européenne : la localisation européenne ne protège pas de ce risque | offre qualifiée SecNumCloud, référentiel qui tient compte de la protection contre l'application de lois extra-européennes (annexe 2.4) |
| Dépendance et réversibilité | traitements construits avec les services intégrés du fournisseur, à reconstruire en cas de départ ; le Data Act facilite le changement de fournisseur, sans supprimer cette dépendance | restitution des données et des traitements dans des formats ouverts, assistance comprise |
| Services | nombreux services d'analyse prêts à l'emploi | services plus limités, suffisants pour un entrepôt et ses tableaux de bord |
| Coût | 40 k€ par an pour l'entrepôt | 60 k€ par an, soit 20 k€ de plus, environ 0,6 % du budget du SI de 3,5 M€ |

**Recommandation : H2**, parce que l'entrepôt contiendra l'identité, les qualifications et les missions de dizaines de milliers de candidats et d'intérimaires, ainsi que les tarifs et les heures facturées des clients ; parce qu'un grand compte de l'industrie aéronautique l'exige depuis janvier 2027 et que d'autres pourraient suivre ; et parce que la réversibilité y est meilleure, pour un surcoût faible. Dans les deux cas, l'hébergeur est un sous-traitant qui agit sur instructions de QUENTALIS Emploi, dans le cadre d'un contrat écrit (RGPD, article 28) (0,5 pt pour l'ensemble de la réponse b).

**Réponses tolérées**
- Cycle de vie présenté en six ou sept étapes (collecte, stockage, traitement, partage, archivage, destruction), si les cinq étapes du programme y figurent et si les durées sont appliquées.
- Autre écart pertinent : doublons de fiches qui prolongent la conservation d'une personne au-delà de la durée prévue, ou proposition de M. DUQUESNEL de tout conserver dans un lac.
- Anonymisation des données avant leur conservation sans limite, présentée comme condition des statistiques de l'entrepôt.
- Recommandation de H1 assortie de conditions (données des clients sensibles hébergées ailleurs, chiffrement dont QUENTALIS garde les clés, plan de réversibilité), si le risque lié au droit applicable est identifié et si l'exigence du grand compte est traitée.

**Erreurs fréquentes**
- *Hébergement « souverain » assimilé à un hébergement en Europe ou en France* (`ET-37`) — juste : le droit applicable au prestataire et la dépendance comptent autant que la localisation.
- *Analyse juridique des durées ou des transferts* — détermination de durées légales, régime des transferts hors de l'Union européenne ; non attendue : les durées sont données.
- *Statut d'un texte affirmé sans date* (`ET-41`) — juste : renvoi à l'annexe 2.4, datée au 31/12/2026.
- *Expertise technique des infrastructures* — description des serveurs, du stockage ou du réseau de l'hébergeur ; non attendue.
- *Cycle de vie récité sans application* (`JUR-T01`) — juste : étapes appliquées aux fiches, documents, contrats et notes de QUENTALIS Emploi.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cycle de vie et archivage ; souveraineté et portabilité | étapes, durées, purge ; définition de la souveraineté | F07 § 8.4 et § 8.5 ; F03 § 5.3 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | minimisation, limitation de la conservation, sous-traitant (article 28) | `rgpd` / F15 § 5 | applicable depuis le 25/05/2018 |
| Règlement (UE) 2023/2854 (Data Act) | changement de fournisseur d'informatique en nuage | `data_act` / F07 § 8.5 | applicable depuis le 12/09/2025 |
| SecNumCloud, version 3.2 (ANSSI) | qualification des offres d'informatique en nuage, protection contre les lois extra-européennes | `secnumcloud_3_2` / F03 § 5.3 | en vigueur |

---

### 2.5 – Planification et risques du projet « Pilotage des missions » (3 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.d` « Planification des ressources, délais, coûts et qualité » ; `1.5.e` « Identification et gestion des risques (maintenance, évolutivité, sécurité) » ; `1.5.a` « Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ». Limite : le chiffrage budgétaire poste par poste du projet ne relève pas du programme (programme l. 1346-1347).

**Annexes mobilisées** : annexe 2.3 D à F (tâches, durées, ressources, contraintes, première estimation, coûts, exigences de qualité), 2.3 B (prestations externes), 2.1 C (qualité des données) et 1.1 (équipe informatique, rotation des chargés de recrutement).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Affectation des ressources et enchaînement : référents sur A, C, E, F et G, donc C et E en série ; ingénieur de données sur B puis D, en parallèle ; diagramme de Gantt lisible | 0,5 |
| a-2 | Durée totale de 18 semaines de travail, pause d'été de huit semaines, mise en production la semaine du 25 octobre 2027 ; critique de l'estimation à 15 semaines | 0,5 |
| a-3 | Quatre jalons datés, cohérents avec le planning | 0,5 |
| a-4 | Enveloppe de 250 k€, temps interne compris (120 + 80 + 30 + 20), et contrôle des exigences de qualité à la recette | 0,5 |
| b | Trois risques avec leur cause, leur effet et leur traitement ; 0,5 pour deux risques | 1 |

**Réponse attendue**

*2.5 a) – Planning, durée, jalons, enveloppe et qualité*

**Affectation des ressources et enchaînement** (0,5 pt). Les référents d'agence interviennent sur A, C, E, F et G et ne peuvent pas mener deux tâches en même temps : C et E, qui ne dépendent que de A, sont donc enchaînées. L'ordre C puis E est préférable : les tableaux de bord sont conçus sur des données nettoyées, et le consultant, qui travaille sur D avec l'ingénieur de données jusqu'au début de juillet, est libre pour E à la rentrée. L'ingénieur de données mène B puis D ; ce chemin (4 + 5 = 9 semaines) se déroule en parallèle et se termine le 2 juillet ; l'ingénieur et le consultant n'étant pas concernés par la pause d'été, D pourrait glisser jusqu'à la fin d'août sans retarder la recette ni obliger le consultant à mener D et E en même temps (environ huit semaines de marge).

| Tâche | Ressources | Semaines de travail | Calendrier 2027 |
|---|---|---|---|
| A Cadrage et dictionnaire | cheffe de projet, consultant, référents | 1 à 3 | 3 au 21 mai |
| B Hébergement et environnements | ingénieur de données | 1 à 4 | 3 au 28 mai |
| C Nettoyage des données sources | référents, centre de services | 4 à 9 | 24 mai au 2 juillet |
| D Flux de collecte et de chargement | ingénieur de données, consultant | 5 à 9 | 31 mai au 2 juillet |
| *Référents indisponibles* | — | — | *5 juillet au 27 août* |
| E Tableaux de bord | consultant, référents | 10 à 12 | 30 août au 17 septembre |
| F Recette dans six agences pilotes | référents, cheffe de projet | 13 à 15 | 20 septembre au 8 octobre |
| G Formation | référents, cheffe de projet | 16 et 17 | 11 au 22 octobre |
| H Mise en production | équipe informatique | 18 | 25 au 29 octobre |

**Durée, jalons et critique de l'estimation** (0,5 pt pour la durée, la date et la critique ; 0,5 pt pour quatre jalons datés) :
- **Durée totale du travail** : 3 + 6 + 3 + 3 + 2 + 1 = **18 semaines** sur le chemin des référents ; avec les huit semaines d'indisponibilité de l'été, **26 semaines** de calendrier : mise en production la semaine du **25 au 29 octobre 2027**, hors des périodes de pointe et deux semaines avant le gel du 15 novembre.
- **Jalons** (quatre suffisent) : dictionnaire des données validé par le comité de direction (21 mai) ; environnements d'hébergement prêts (28 mai) ; données nettoyées et flux de chargement opérationnels (2 juillet) ; procès-verbal de recette (8 octobre) ; mise en production dans le réseau (29 octobre) ; bilan d'usage trois mois plus tard (fin janvier 2028).
- **Critique de l'estimation à 15 semaines** : elle suppose que les référents mènent C et E en même temps, ce qu'ils ne peuvent pas faire, et ignore leur indisponibilité de juillet et d'août ; elle conduit à une mise en production le 13 août 2027, en pleine période de pointe où elle est interdite, avec une recette prévue en juillet sans les référents.

**Enveloppe et exigences de qualité** (0,5 pt) :
- **Enveloppe du projet** : 120 k€ de prestations externes + 80 k€ de temps de l'équipe informatique + 30 k€ de temps des référents + 20 k€ de réserve pour aléas = **250 k€**, soit la moitié de l'enveloppe des projets de 2027 (500 k€) ; le fonctionnement relève du budget courant, hors enveloppe : l'hébergement dès sa mise en place en mai 2027 (60 k€ par an avec H2, annexe 2.3 E), les licences et la maintenance des flux (30 k€ par an) à partir de 2028, soit 90 k€ par an. L'enveloppe est suivie globalement, à chaque jalon, sans gestion poste par poste.
- **Contrôle des exigences de qualité** : elles deviennent les **critères d'acceptation de la recette** (tâche F) dans les six agences pilotes : données de la veille disponibles à 7 heures chaque jour de la recette ; au plus 1 % de lignes rejetées à chaque chargement, chaque rejet expliqué ; nombre de commandes du mois identique dans l'entrepôt et dans le logiciel de gestion ; taux de service recalculé à la main sur un échantillon de commandes de chaque agence pilote selon la définition du dictionnaire ; droits d'accès vérifiés (un directeur ne voit que son agence et les totaux du réseau). Le procès-verbal de recette, sans réserve bloquante, conditionne la mise en production ; l'usage (90 % des directeurs d'agence chaque semaine) est mesuré à trois mois.

*2.5 b) – Trois risques du projet*

| Risque | Cause | Effet | Traitement |
|---|---|---|---|
| **1. Indisponibilité des référents d'agence** | une journée par semaine prise sur l'activité de l'agence, forte rotation des chargés de recrutement, pointes d'activité | glissement de C, E, F et G, recette écourtée ; mise en production repoussée après le gel du 15 novembre, donc en janvier 2028 | engagement écrit des directeurs d'agence, un suppléant pour chaque référent, calendrier des journées fixé dès mai, suivi des jalons en comité de projet ; la marge de deux semaines avant le gel est préservée |
| **2. Données sources de mauvaise qualité et définitions non adoptées** | 10 % de doublons, 650 codes métiers, commandes non saisies, définitions propres à chaque agence | indicateurs contestés par les agences, retour aux tableurs, perte de confiance dans l'entrepôt | dictionnaire validé par le comité de direction au premier jalon, règles de saisie et propriétaires (question 2.2), nettoyage avant chargement, recette sur des données réelles rapprochées du logiciel de gestion, communication sur le changement de définition |
| **3. Maintenance et évolutivité des flux de chargement** | flux construits sur un logiciel de gestion en mode SaaS, que l'éditeur met à jour plusieurs fois par an ; connaissance concentrée sur un ingénieur et un consultant | flux interrompus ou données fausses après une mise à jour, sans que les agences s'en aperçoivent | utiliser l'API documentée plutôt que des extractions ad hoc, contrôle du journal des rejets et du rapprochement après chaque mise à jour, maintenance corrective et évolutive prévue (10 k€ par an), documentation des flux et transfert des compétences du consultant à l'équipe informatique |

(0,5 pt pour deux risques complets, 1 pt pour trois.)

Le planning tient compte des ressources réelles et du calendrier de l'activité, les exigences de qualité sont vérifiées avant la mise en production et les risques renvoient aux constats des annexes : c'est le pilotage d'un projet dans une logique de performance durable (valeur pour les agences, qualité, maîtrise de la maintenance).

**Réponses tolérées**
- Ordre E puis C : si C est interrompue par la pause d'été (trois semaines avant, trois après), même durée de 18 semaines et même date de mise en production ; si C n'est pas interrompue (du 30 août au 8 octobre), F, G et H glissent et la mise en production tombe la semaine du 15 novembre, dans le gel : elle est reportée à janvier 2028. Ce planning est accepté si le report est vu et justifié ; il montre l'intérêt de l'ordre C puis E. Dans les deux cas, le chevauchement de E et de D pour le consultant est à signaler.
- Hébergement des mois de 2027 (à partir de mai) ajouté à l'enveloppe, s'il est présenté comme une hypothèse.
- Diagramme de Gantt dessiné à la main avec des barres et des losanges pour les jalons, en semaines ou en dates, sans tableau.
- Autres jalons pertinents (choix de l'hébergement, fin de la formation), s'ils sont datés et cohérents avec le planning.
- Autres risques appuyés sur les annexes : confidentialité des données des intérimaires pendant la recette ou droits d'accès mal réglés entre agences ; dépendance au consultant ; adoption insuffisante par les directeurs d'agence ; retard de l'hébergeur.

**Erreurs fréquentes**
- *Gantt sans ressources ni jalons* (`JUR-P01` Gantt lisible et pertinent) — tâches enchaînées au plus tôt sans voir que les référents ne mènent qu'une tâche à la fois.
- *Reprise de l'estimation à 15 semaines* — mise en production en août, période interdite.
- *Risques génériques* (`JUR-P02` facteurs clés de succès et risques dans le contexte) — « risque de retard », sans cause tirée des annexes ni traitement.
- *Chiffrage du projet poste par poste* (coûts par tâche, écarts, valeur acquise) — non attendu : une enveloppe en sommes rondes suffit.
- *Qualité réduite à des tests techniques* — juste : critères d'acceptation métiers (définition du taux de service, rapprochement, droits) et mesure de l'usage.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Planification : WBS et Gantt à partir d'un texte, contraintes de ressources, jalons | planning, durée, critique de l'estimation | F05 § 4 | notion de cours |
| Risques projet : identifier, coter, traiter, suivre | trois risques et leur traitement | F05 § 5 | notion de cours |
| Recette, critères d'acceptation, maintenance corrective et évolutive | contrôle des exigences de qualité, risque 3 | F05 § 6 | notion de cours |
