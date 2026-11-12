# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 14 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 architecture et urbanisation, F07 données, modélisation et gouvernance, F05 projets et changement, F08 décisionnel (chaîne de traitement), F10 audit et fiabilisation, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026 et le 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Urbanisation et cible de convergence | `1.3.a` Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) ; `1.3.c` Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle | 3 |
| 2.2 Référentiels communs | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) | 3 |
| 2.3 Échanges avec les chargeurs | `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 2 |
| 2.4 Impacts sur les métiers de Transports CAUVERLIN | `1.3.e` Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers | 2 |
| 2.5 Valeur, reprise et gouvernance des données | `2.3.f` Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.3.a` Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques | 3 |
| **Dossier 2 – Préparer l'intégration du système d'information d'un transporteur acquis** |  | **13** |

Répartition indicative : connaissances (principes de l'urbanisation, données de référence, caractérisation des trois architectures orientées données, interopérabilité, transformation des métiers, donnée comme actif immatériel) 3 points (items 2.1 a-1, 2.2 a-1, 2.2 b-1 pour moitié, 2.3-1, 2.4-1, 2.5 a-1) ; analyse des annexes et recommandations 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Urbanisation et cible de convergence (3 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.a` « Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes (blockchain, IA, registres distribués,…) » ; `1.3.c` « Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle ».

**Annexes mobilisées** : annexes 1.1 (activité, plan « ORMESTAL 2030 », organigramme), 2.1 (les deux systèmes d'information, calendrier et contraintes) et 2.3 (témoignages des exploitants, de la responsable du transport et du chargeur).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Urbanisation définie comme démarche stratégique (analogie de la ville, zones, quartiers, îlots) et deux de ses règles (une fonction implantée une seule fois, référentiels uniques, échanges par une zone d'échange) | 0,5 |
| a-2 | Diagnostic tiré de l'annexe 2.1 : deux recouvrements, deux ruptures de flux, deux fonctions sans application, chacun appuyé sur un fait ; 1 pt pour six éléments justes ; 0,5 pour trois à cinq ; 0 en deçà | 1 |
| b-1 | Cible organisée par zones (relation et échanges avec les clients, opérations, gestion et comptabilité, référentiels, pilotage, échanges), schéma ou tableau lisible | 0,5 |
| b-2 | Sort de chaque application ou outil (repris, remplacé, abandonné) justifié par les annexes : fin de maintenance au 30 septembre 2027, départ du fondateur, mutualisation des tournées, doubles saisies ; 0,5 si les décisions sont justes mais non justifiées | 1 |

**Réponse attendue**

*2.1 a) – Principes de l'urbanisation et diagnostic*

**Urbaniser** le système d'information, c'est l'organiser, par analogie avec l'urbanisme d'une ville, en blocs fonctionnels faiblement couplés pour qu'il évolue au rythme de la stratégie sans être reconstruit à chaque changement. Le SI est découpé en **zones** (grands domaines : relation avec les clients, opérations, gestion, référentiels, pilotage, échanges), en **quartiers** (sous-domaines : entreposage, transport, facturation) et en **îlots** (ensembles cohérents de fonctions portés par une application : planification des tournées, suivi de l'exécution). Ses règles : une fonction n'est implantée qu'une fois, une donnée de référence a un seul propriétaire, les applications échangent par une zone d'échange plutôt que par des liaisons et des ressaisies au cas par cas. C'est une démarche stratégique, au service des processus et du plan « ORMESTAL 2030 » (intégrer en moins d'un an), et non un inventaire de logiciels (F03 § 1) (0,5 pt).

Diagnostic des deux SI (1 pt pour six éléments justes ; 0,5 pour trois à cinq ; 0 en deçà) :

| Constat | Fait de l'annexe 2.1 | Conséquence |
|---|---|---|
| **Recouvrement 1** : deux îlots de planification des tournées | logiciel de gestion du transport d'ORMESTAL France, qui propose les tournées ; chez Transports CAUVERLIN, tableur de planification et ancien logiciel de transport | deux façons de planifier dans le même quartier transport ; aucune mutualisation possible des camions qui « se croisent chez les mêmes clients » dans l'Ain (Mme VALDRESSE) |
| **Recouvrement 2** : plusieurs fichiers pour les mêmes clients, sites et camions | fichier des clients en deux exemplaires chez ORMESTAL France, rapprochés à la main chaque semaine ; fichier du fondateur chez Transports CAUVERLIN ; 30 chargeurs communs et environ 1 000 sites connus sous deux identifiants ; camions identifiés par numéro de parc d'un côté, par immatriculation de l'autre | les mêmes clients et sites n'ont pas le même identifiant, et les camions relèvent de deux règles d'identification (numéro de parc, immatriculation) : aucun rapprochement automatique, tarifs divergents pour 12 chargeurs communs |
| **Rupture 1** : la commande de transport est saisie trois fois | courriel ou téléphone → tableur de planification → ancien logiciel → ressaisie des exports par le cabinet d'expertise comptable | deux heures de saisie par jour et par exploitante (Mme ESTARDEL), erreurs de recopie, facturation tardive |
| **Rupture 2** : les relevés de température ne circulent pas | enregistreurs lus au retour du camion, relevé envoyé à la demande du chargeur | relevé obtenu « parfois une semaine plus tard » contre 48 heures exigées par les enseignes (Mme SORVIGNAC) |
| **Rupture 3** (variante acceptée) : les tarifs passent par courriel | tableur du fondateur envoyé chaque mois au cabinet | tarifs appliqués à la main, 5 % de factures donnant lieu à un avoir |
| **Fonction sans application 1** : suivi en temps réel des tournées | aucun camion de Transports CAUVERLIN n'est équipé de télématique : suivi par téléphone | ni heure d'arrivée, ni preuve de livraison, ni alerte de température |
| **Fonction sans application 2** : gestion des tarifs et des données de référence | tarifs et clients dans le tableur personnel du fondateur ; contraintes des sites dans les onglets des exploitants | aucune règle, aucun contrôle, savoir détenu par des personnes |
| **Fonction sans application 3** (variante acceptée) : mise à disposition des documents aux chargeurs | aucun portail chez Transports CAUVERLIN | chargeurs servis à la demande, sans délai garanti |

*2.1 b) – Cible de convergence zone par zone*

| Zone (quartiers) | Cible | Sort des applications et outils, et justification |
|---|---|---|
| **Relation et échanges avec les clients** (prise de commande, documents de livraison) | portail des clients et échanges normalisés d'ORMESTAL France, ouverts aux 120 chargeurs de Transports CAUVERLIN (question 2.3) | portail **repris et étendu** ; courriels, appels et espace partagé **remplacés** par le portail ou par l'échange automatisé : fin de la première saisie et délai de 48 heures tenu |
| **Opérations** – quartier transport (planification, exécution, preuves de livraison) | un seul logiciel de gestion du transport pour les 345 camions (260 + 85), télématique sur tous les camions | logiciel de gestion du transport d'ORMESTAL France **repris** et étendu aux deux exploitants : seul outil maintenu, il permet la mutualisation des tournées ; ancien logiciel de transport **remplacé** avant le 30 septembre 2027, date de fin de sa maintenance, après reprise de son historique ; tableur de planification **abandonné**, les contraintes des sites qu'il contient étant reprises dans le référentiel des sites ; télématique **reprise** et installée sur les 85 camions : suivi, preuve de livraison et relevés transmis en continu |
| **Opérations** – quartier entreposage | logiciel de gestion des entrepôts inchangé | **repris** sans changement : Transports CAUVERLIN n'a pas d'entrepôt ; la cible relie seulement les expéditions au logiciel de transport unique |
| **Gestion** (tarifs, facturation, comptabilité) | logiciel de gestion comptable et commerciale d'ORMESTAL France, tenu pour Transports CAUVERLIN comme société distincte | logiciel **repris** : grilles de tarifs datées, facturation calculée à partir des tournées réalisées ; tableur des tarifs du fondateur **abandonné** après reprise des grilles datées ; ressaisie par le cabinet d'expertise comptable **abandonnée** (le maintien d'une mission du cabinet relève de la directrice administrative et financière) |
| **Référentiels** (clients, sites de livraison, véhicules, tarifs) | référentiels uniques et gouvernés (question 2.2) | fichiers du fondateur et fichiers en double d'ORMESTAL France **remplacés** par les référentiels : fin du rapprochement hebdomadaire à la main |
| **Pilotage** | tableaux de bord communs du transport (ponctualité, remplissage des camions, chiffre d'affaires par chargeur) alimentés par le logiciel unique | à construire après la bascule ; aucun outil de Transports CAUVERLIN à reprendre |
| **Échanges** (zone transverse) | échanges entre applications et avec les chargeurs par des interfaces normalisées, sans ressaisie | remplace les exports manuels et les courriels |

Ce qui est repris de Transports CAUVERLIN n'est donc pas un logiciel mais un **patrimoine** : l'historique des tournées, les contraintes des sites, les tarifs négociés et le savoir-faire des exploitants (question 2.5). Le candidat peut représenter la cible par un schéma en blocs emboîtés (zones contenant les quartiers et les îlots, flèches vers la zone d'échange), légendé et commenté en trois ou quatre phrases.

**Réponses tolérées**
- Découpage des zones différent (par exemple une zone « exécution du transport » distincte de la planification, ou les référentiels rangés dans une zone « données ») s'il respecte la logique zones, quartiers, îlots et s'applique aux deux SI.
- Fonctions sans application autres que celles du tableau (optimisation des tournées faite à la main, absence d'outil de gestion des sauvegardes), si elles sont tirées des annexes.
- Maintien provisoire de l'ancien logiciel en consultation seule pour l'historique, jusqu'à la fin de la reprise, si la date du 30 septembre 2027 est prise en compte.
- Cartographie présentée en tableau plutôt qu'en schéma (format libre).
- Mention, pour la zone gestion, de l'adoption ultérieure du socle SI commun du groupe annoncée par la présentation, sans développement ; elle ne remet pas en cause la reprise du logiciel d'ORMESTAL France en 2027.

**Erreurs fréquentes**
- *Urbanisation réduite à un inventaire technique* (`ET-20`, `JUR-G07` le pourquoi puis le comment de l'urbanisation) — lister des serveurs ou des postes ; juste : zones, quartiers, îlots au service des processus de transport et de facturation.
- *Garder les deux SI côte à côte sans décision argumentée* (`JUR-G09` mise en cohérence de SI inter-organisationnels : décision argumentée et accompagnement du changement) — alors que l'ancien logiciel n'est plus maintenu après le 30 septembre 2027 et que le plan impose l'intégration en moins d'un an.
- *Diagnostic sans faits de l'annexe* (`JUR-T01` morceau de cours) — « il y a des doublons » sans dire lesquels ; juste : 30 chargeurs communs, triple saisie, relevés envoyés en une semaine.
- *Schéma illisible ou non légendé* (`JUR-T10`).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Urbanisation du SI (zones, quartiers, îlots ; règles d'urbanisme) | définition, découpage, démarche | F03 § 1 et § 6 | notion de cours [S] |
| Cartographies fonctionnelle et applicative | repérage des recouvrements et des ruptures | F03 § 2 | notion de cours |

---

### 2.2 – Référentiels communs (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) ».

**Annexes mobilisées** : annexes 1.1 (organigramme : propriétaires possibles), 2.1 (identifiants actuels, calendrier), 2.2 (volumes, constats de qualité, options) et 2.3 (témoignages).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Données de référence définies (données partagées, stables, utilisées par plusieurs processus et applications, gérées une seule fois) et gestion d'un référentiel de données maîtres | 0,5 |
| a-2 | Trois référentiels organisés : identifiant unique, règle de rapprochement, propriétaire métier, appliqués aux constats de l'annexe 2.2 ; 0,5 pour deux référentiels complets | 1 |
| b-1 | Trois options caractérisées et comparées selon trois critères appliqués au cas (réponse au besoin des opérations, qualité des données à la source, coût sur trois ans et délai) | 1 |
| b-2 | Recommandation justifiée (référentiel de données maîtres, entrepôt ultérieur pour le pilotage, lac écarté) et compatible avec le calendrier | 0,5 |

**Réponse attendue**

*2.2 a) – Données de référence et organisation des trois référentiels*

Les **données de référence** (*master data*) sont les données partagées et relativement stables qui décrivent les objets de l'activité (clients, sites, véhicules, tarifs) et que plusieurs processus et applications utilisent ; elles doivent exister **une seule fois**, sous un identifiant unique, avec un propriétaire. La gestion des données maîtres (*Master Data Management*, à écrire en toutes lettres pour ne pas la confondre avec la gestion des terminaux mobiles) est la discipline et l'outil qui les créent, les contrôlent et les diffusent aux applications (F07 § 1 et § 6.2) (0,5 pt).

| Référentiel | Identifiant unique | Règle de rapprochement des fiches des deux sociétés | Propriétaire (et intendant) |
|---|---|---|---|
| **Clients** (400 + 120, dont 30 communs, soit 490) | code client unique de l'ensemble, attribué par le référentiel ; les 30 chargeurs communs conservent leur code à cinq chiffres d'ORMESTAL France | numéro SIREN d'abord (à compléter pour la moitié des fiches de Transports CAUVERLIN qui ne l'ont pas), puis raison sociale normalisée et adresse ; les 140 fiches ramenées à 120 chargeurs ; une fiche par chargeur, ses établissements rattachés | Mme MERCOIRAN, directrice administrative et financière, car le client porte la facturation et les tarifs ; intendant : un collaborateur de la facturation |
| **Sites de livraison** (6 000 + 2 500, dont environ 1 000 communs, soit environ 7 500) | code site attribué par le référentiel, et non l'adresse, qui varie selon la saisie | adresse normalisée (code postal, voie, commune) et enseigne, complétées par le code du magasin chez l'enseigne quand il existe ; environ 1 000 sites communs fusionnés ; horaires de réception, quai et contraintes d'accès deviennent des informations de la fiche ; création réservée aux intendants, ce qui corrige aussi le défaut d'ORMESTAL France | Mme VALDRESSE, responsable du transport ; intendants : les deux exploitants de Transports CAUVERLIN pour les sites de l'Ain, qui en connaissent les contraintes |
| **Véhicules** (260 + 85) | numéro de parc unique, étendu aux 85 camions, y compris les 12 camions loués | immatriculation (et numéro d'identification du véhicule) conservée comme attribut daté, et non comme identifiant, puisqu'elle change à chaque renouvellement d'une location | Mme VALDRESSE, responsable du transport (ou M. DRAVIGNOL, directeur des opérations) ; intendant : le gestionnaire du parc |

Les tarifs sont rattachés au client du référentiel et portent obligatoirement une date d'effet. Le responsable des systèmes d'information administre l'outil ; il n'est propriétaire d'aucun référentiel (1 pt ; 0,5 pour deux référentiels complets).

*2.2 b) – Comparaison des options et recommandation*

Un **référentiel de données maîtres** gère à la source les données partagées et les diffuse aux applications ; un **entrepôt de données** rassemble, après coup, des données intégrées, historisées et non volatiles pour l'analyse ; un **lac de données** stocke des données brutes, hétérogènes, dont la structure n'est définie qu'à la lecture (F07 § 6) (0,5 pt sur l'item b-1).

| Critère | Option 1 – Référentiel de données maîtres | Option 2 – Entrepôt de données commun | Option 3 – Lac de données |
|---|---|---|---|
| Réponse au besoin des opérations (identifiants communs dans le logiciel de transport, le portail, la facturation) | oui : les applications utilisent le même client, le même site, le même camion ; condition de la mutualisation des tournées | non : chaque application garde ses fichiers ; les doubles saisies demeurent ; utile au pilotage seulement | non : aucun rapprochement ; les fichiers restent dans leur état |
| Qualité et cohérence des données | contrôlées à la création (SIREN, adresse complète, date d'effet), avec un propriétaire par référentiel | rapprochement chaque nuit, a posteriori : les erreurs sont constatées, non évitées | risque de « marécage de données » : 20 doublons, 500 adresses incomplètes et 100 grilles non datées déposés tels quels |
| Coût sur trois ans et délai | 150 + 3 × 30 = 240 k€ ; 5 mois | 100 + 3 × 20 = 160 k€ ; 4 mois | 80 + 3 × 40 = 200 k€ ; 3 mois |

(0,5 pt sur l'item b-1 pour la comparaison selon trois critères appliqués.)

**Recommandation** : l'**option 1**. C'est la plus chère (80 k€ de plus que l'entrepôt sur trois ans), mais c'est la seule qui supprime la cause des difficultés, à savoir des objets identifiés différemment et créés sans règle : elle met fin aux doubles saisies (deux heures par jour et par exploitante), aux avoirs sur les tarifs (5 % des factures) et permet la mutualisation des tournées. Elle doit être lancée dès avril pour être prête en cinq mois, avant la seconde vague de septembre ; les référentiels des clients et des sites passent en premier, celui des véhicules suit avec la pose de la télématique. L'entrepôt (option 2) pourra venir ensuite, alimenté par des données déjà rapprochées, pour les tableaux de bord communs. Le lac (option 3) est écarté : il ne crée aucun identifiant commun et coûte le plus cher en fonctionnement (40 k€ par an) (0,5 pt).

**Réponses tolérées**
- Autres propriétaires, s'ils sont des responsables métier justifiés : directeur des opérations pour les sites et les véhicules, responsable du transport pour les clients si l'on retient le point de vue de l'exploitation.
- Code client des deux sociétés conservé avec une table de correspondance gérée par le référentiel, si l'identifiant de l'ensemble est unique.
- Recommandation combinant les options 1 et 2 dès le départ, si le candidat montre que l'entrepôt ne remplace pas le référentiel et que le calendrier le permet.
- Autres critères de comparaison (organisation requise, adéquation au calendrier du 30 septembre 2027, risque de dépendance à des spécialistes rares), s'ils sont appliqués aux options.

**Erreurs fréquentes**
- *Sigle MDM sans précision* (`ET-13`) — confusion avec la gestion des terminaux mobiles ; juste : gestion des données maîtres, écrite en toutes lettres.
- *Entrepôt et lac confondus, ou lac présenté comme un entrepôt moderne* (`ET-24`) — juste : l'entrepôt intègre et structure pour l'analyse, le lac stocke du brut ; ni l'un ni l'autre ne fournit d'identifiants aux applications.
- *Propriétaire du référentiel = responsable des systèmes d'information* — juste : un responsable métier décide des règles et de la qualité ; la fonction SI administre l'outil (F07 § 8.1).
- *Immatriculation ou adresse retenue comme identifiant* — elles changent (12 camions loués, adresses incomplètes) ; juste : un identifiant attribué par le référentiel.
- *Modèle conceptuel ou logique des données dessiné* (`ET-23`) — non demandé : l'énoncé exclut tout modèle de données.
- *Choix fondé sur le seul coût* (`JUR-T03` analyser et argumenter) — retenir l'option la moins chère sans examiner si elle répond au besoin.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK (2e édition, 2017, révision 2024) | domaine « données de référence et données maîtres », rôles de propriétaire et d'intendant | `dama_dmbok2` / F07 § 8.2 | en vigueur (référentiel, non norme) |
| Données de référence, entrepôt, lac, référentiel de données maîtres | définitions et choix | F07 § 1 et § 6.2 | notion de cours |
| Rôles de propriétaire et d'intendant des données | gouvernance des référentiels | F07 § 8.1 | notion de cours (illustratif) |

---

### 2.3 – Échanges avec les chargeurs (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) » ; `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ».

**Annexes mobilisées** : annexes 2.1 (échanges d'ORMESTAL France et de Transports CAUVERLIN, calendrier et contraintes), 2.2 (chargeurs communs) et 2.3 (témoignage de Mme SORVIGNAC).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Interopérabilité définie, avec ses dimensions technique (formats, interfaces), sémantique (mêmes identifiants, même sens) et organisationnelle (processus, responsabilités) | 0,5 |
| 2 | Deux choix techniques adaptés aux chargeurs (échange automatisé au format normalisé ou par API pour les chargeurs équipés ; portail pour les autres ; preuves et relevés transmis par la télématique et mis à disposition sous 48 heures) | 0,5 |
| 3 | Trois dispositions organisationnelles : accord d'échange, responsabilités, calendrier de bascule en vagues hors période de pointe ; 0,5 pour deux | 1 |

**Réponse attendue**

L'**interopérabilité** est la capacité de systèmes différents, ici ceux d'ORMESTAL France et des chargeurs, à échanger des données et à les utiliser sans intervention manuelle. Elle a une dimension **technique** (formats normalisés ou ouverts comme XML ou JSON, interfaces de programmation), une dimension **sémantique** (une commande désigne le même client, le même site et la même date pour les deux parties, grâce aux identifiants des référentiels de la question 2.2) et une dimension **organisationnelle** (processus, engagements, responsabilités) ; le programme exige les deux plans, technique et organisationnel (F07 § 7) (0,5 pt).

**Deux choix techniques** (0,5 pt) :
1. **Commandes** : les chargeurs qui transmettent déjà leurs commandes à ORMESTAL France par échange automatisé (70 % de ses clients), comme la Fromagerie BRÉMACIER parmi les 30 chargeurs communs, utilisent le même échange, au format normalisé, pour les livraisons de l'ancien périmètre de Transports CAUVERLIN, ou l'interface de programmation du logiciel de gestion du transport ; les autres chargeurs, qui commandent aujourd'hui par courriel, par téléphone ou par l'espace partagé, saisissent leurs commandes sur le portail des clients. La commande entre ainsi une seule fois, directement dans le logiciel de transport.
2. **Preuves de livraison et relevés de température** : produits par la télématique installée sur les 85 camions (signature sur la tablette, températures du caisson), ils sont mis à disposition automatiquement sur le portail et, pour les chargeurs qui le demandent, par l'interface de programmation, dans un format ouvert ; le délai de 48 heures exigé par les enseignes est tenu sans demande du chargeur.

**Trois dispositions organisationnelles** (1 pt ; 0,5 pour deux) :
1. **Accord d'échange** avec chaque chargeur raccordé : contenu de la commande et identifiants utilisés (code client et code site du référentiel), heure limite de transmission pour une livraison le lendemain, délai de mise à disposition des preuves et des relevés, confidentialité, traitement des messages rejetés. Pour les chargeurs qui passent au portail, des conditions d'utilisation et une formation courte.
2. **Responsabilités** : un interlocuteur unique chez ORMESTAL France pour chaque chargeur (attente de Mme SORVIGNAC) ; un correspondant chez le chargeur ; le propriétaire du flux (responsable du transport) répond de sa disponibilité ; une procédure écrite dit qui détecte un échange en échec, qui prévient l'autre partie et comment la commande est passée en secours (portail ou téléphone, avec saisie unique par l'exploitant).
3. **Calendrier de bascule** par vagues, compatible avec les dates de l'annexe 2.1 C : en juin 2027, en pilote, les 30 chargeurs communs, déjà raccordés à ORMESTAL France et dont les codes clients existent déjà dans ses applications ; en septembre, les 90 autres chargeurs, avant l'arrêt de la maintenance de l'ancien logiciel le 30 septembre 2027 ; période de fonctionnement en parallèle de deux à trois semaines pour chaque vague ; aucune bascule de la mi-novembre à la fin de décembre ; chaque chargeur est informé de sa date au moins un mois à l'avance. Le pilote s'appuie sur les codes clients et sites déjà présents dans les applications d'ORMESTAL France pour ces chargeurs (la plupart de leurs sites figurent parmi les quelque 1 000 sites déjà connus) ; les camions de Transports CAUVERLIN affectés au pilote sont équipés de la télématique en priorité ; le référentiel de données maîtres, livré fin août, reprend ces fiches avant la seconde vague.

**Réponses tolérées**
- Échange de données informatisé cité comme exemple de format normalisé, sans détail de sa syntaxe.
- Calendrier différent (par exemple trois vagues, ou les chargeurs par téléphone basculés en dernier) s'il respecte le 30 septembre 2027, la période de pointe et l'objectif de moins d'un an.
- Pilote placé après la livraison du référentiel (début septembre), si la seconde vague reste achevée avant le 30 septembre 2027 ou si le maintien de l'ancien logiciel en consultation seule est justifié.
- Maintien, pour quelques petits chargeurs, d'une commande par téléphone saisie une seule fois par l'exploitant dans le logiciel de transport, si le choix est justifié.

**Erreurs fréquentes**
- *Interopérabilité traitée sous le seul angle technique* (`ET-36`) — juste : formats et interfaces, mais aussi mêmes identifiants, accord d'échange, responsabilités et calendrier.
- *Description détaillée des normes d'échange ou des messages* — hors programme (le programme exclut l'approfondissement technique des échanges) ; une mention des formats suffit.
- *Facturation électronique traitée à la place des commandes et des preuves de livraison* — hors du sujet de la question.
- *Témoignage de la Fromagerie BRÉMACIER ignoré* (`JUR-T08`) — un seul interlocuteur, un seul format, pas de bascule pendant les fêtes, procédure en cas d'échec.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Interopérabilité : niveaux technique, syntaxique, sémantique, organisationnel | définition et dimensions | F07 § 7 ; F03 § 3 | notion de cours [S] |
| Référentiel général d'interopérabilité (RGI), version 2.0 | exemple de cadre de recommandations sur les normes et standards, propre aux administrations (réponse tolérée, non attendue) | `rgi_v2` / F07 § 7 | en vigueur |

---

### 2.4 – Impacts sur les métiers de Transports CAUVERLIN (2 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.e` « Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers ».

**Annexes mobilisées** : annexes 1.1 (organigramme), 2.1 (outils actuels, calendrier) et 2.3 (témoignages de M. CAUVERLIN, de Mme ESTARDEL, de M. MORLANDIER, de Mme VALDRESSE et de Mme MERCOIRAN).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Transformation des métiers caractérisée : la nouvelle architecture déplace le travail de la production (saisie, construction) vers la supervision, le contrôle et la relation, et modifie compétences, responsabilités et contrôles | 0,5 |
| 2 | Impact organisationnel sur le métier d'exploitant, appuyé sur les témoignages, et une mesure d'accompagnement | 0,5 |
| 3 | Impact juridique sur la responsabilité en cas d'erreur de planification, et une mesure (validation humaine tracée, motifs des modifications) | 0,5 |
| 4 | Impact comptable sur la piste d'audit et l'arrêté des comptes, et une mesure (facturation à partir des tournées réalisées, tarifs datés, rapprochement mensuel) | 0,5 |

**Réponse attendue**

Une nouvelle architecture ne change pas seulement les outils : en automatisant la saisie et en centralisant les données, elle **transforme les métiers**, qui passent de la production (saisir, construire, recopier) à la **supervision** (vérifier, arbitrer, traiter les exceptions) et à la relation avec les clients. Elle modifie les compétences attendues, la répartition des responsabilités et les contrôles, qui s'appuient désormais sur des traces informatiques (programme 1.3.e ; guide p. 349 : évolution des métiers vers la supervision et le conseil, responsabilité en cas d'erreur, piste d'audit) (0,5 pt).

| Impact | Analyse à partir de l'annexe 2.3 | Mesure d'accompagnement |
|---|---|---|
| **Organisationnel** : le métier d'exploitant (0,5 pt) | les exploitants ne construiront plus les tournées sur le tableur ni ne ressaisiront les commandes (deux heures par jour libérées) : ils vérifieront les propositions du logiciel, traiteront les imprévus et parleront aux clients, comme chez ORMESTAL France (Mme VALDRESSE) ; crainte de devenir « une presse-bouton » (Mme ESTARDEL) ; risque de perdre la connaissance fine des sites qui fait la fidélité des clients (M. CAUVERLIN) | associer les deux exploitants à la reprise des contraintes des sites et en faire les intendants du référentiel des sites de l'Ain ; formation au logiciel en binôme avec des exploitants d'ORMESTAL France ; démarche de conduite du changement qui valorise le rôle d'arbitre et de conseil |
| **Juridique** : la responsabilité en cas d'erreur de planification (0,5 pt) | le logiciel propose, l'exploitant valide : envers le chargeur, la société reste responsable de la prestation ; en interne, il faut pouvoir établir qui a décidé quoi, si la proposition ignorait une contrainte (« le mardi matin ») ou si une modification a causé l'erreur (M. MORLANDIER) ; les preuves de livraison et les relevés horodatés deviennent les éléments de preuve en cas de litige sur une marchandise perdue | validation humaine obligatoire de chaque tournée ; journal des propositions, des validations et des modifications avec leur motif et leur auteur ; contraintes des sites saisies dans le référentiel pour que le logiciel les respecte ; règles de délégation de validation écrites ; les données personnelles des conducteurs recueillies par la télématique sont inscrites au registre des traitements (mention, sans analyse juridique) |
| **Comptable** : la piste d'audit et l'arrêté des comptes (0,5 pt) | aujourd'hui, on ne peut pas remonter d'une facture à la tournée et à la commande ; 5 % des 1 400 factures annuelles donnent lieu à un avoir faute de tarif daté ; les tournées réalisées non facturées au 31 décembre ont été estimées à la main ; dix semaines pour arrêter les comptes de 2026 (Mme MERCOIRAN) ; avec un identifiant commun, chaque montant facturé se rattache à une tournée réalisée, à une preuve de livraison et à une commande | facturation calculée par le logiciel de gestion comptable et commerciale à partir des tournées réalisées dès le 1er octobre 2027, avec des tarifs datés ; rapprochement mensuel des tournées réalisées et des tournées facturées ; liste des prestations réalisées non facturées produite par le logiciel au 31 décembre 2027 ; objectif d'arrêté en quatre semaines |

**Réponses tolérées**
- Impact organisationnel portant sur le fondateur (passage de la négociation au cas par cas à des grilles tarifaires gouvernées) ou sur le cabinet d'expertise comptable, si le métier d'exploitant est aussi traité.
- Reprise de la comptabilité de Transports CAUVERLIN dans le logiciel d'ORMESTAL France à l'ouverture de l'exercice 2028 plutôt qu'en cours d'exercice, si la facturation bascule plus tôt et si le choix est justifié.
- Mesures de conduite du changement formulées selon un modèle connu (ADKAR, huit étapes de Kotter : F05 § 7), si elles sont appliquées aux exploitants.

**Erreurs fréquentes**
- *« Le logiciel est responsable de l'erreur »* — un logiciel n'est pas responsable : la société répond envers le chargeur et la décision validée par l'exploitant doit être tracée.
- *Développement de droit du travail (fiche de poste, temps de travail) ou de droit des transports (lettre de voiture, responsabilité du voiturier)* — exclu par l'énoncé ; juste : responsabilité, preuve et traçabilité dans le SI.
- *Transformation des métiers présentée comme une simple suppression de postes ou de tâches* (`JUR-D03` transformation des métiers et compétences) — juste : déplacement vers la supervision, le contrôle et la relation, compétences nouvelles.
- *Témoignages non exploités* (`JUR-T08`).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Effets métiers des nouvelles architectures (production → supervision, responsabilité en cas d'erreur, piste d'audit) | transformation des métiers | programme 1.3.e ; guide p. 349 | notion de cours |
| Conduite du changement : résistances, leviers | accompagnement des exploitants | F05 § 7 | notion de cours |
| ADKAR (Prosci ; Hiatt, 2003) ; huit étapes de Kotter (1995-1996) | modèles de conduite du changement (réponse tolérée) | `adkar`, `kotter_8_etapes` / F05 § 7 | publiés |
| Piste d'audit dans le SI | traçabilité de la facture à la commande | F10 § 3.2 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | registre des traitements (simple mention) | `rgpd` / F15 § 2 | en vigueur depuis le 25/05/2018 |

---

### 2.5 – Valeur, reprise et gouvernance des données (3 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.f` « Notions de valeur, de patrimoine immatériel et de risque lié aux actifs numériques » ; `2.3.a` « Mettre en place une gouvernance stratégique de la donnée intégrant les enjeux de qualité, de conformité, de sécurité, de valorisation et de cycle de vie des actifs numériques ».
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ».

**Annexes mobilisées** : annexes 2.1 (outils, calendrier), 2.2 (volumes, constats de qualité, sauvegarde et diffusion) et 2.3 (témoignages de M. CAUVERLIN, des exploitants et de Mme MERCOIRAN).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Donnée présentée comme actif immatériel (ressource maîtrisée, source de valeur d'usage, voire d'échange) et appliquée aux données de Transports CAUVERLIN | 0,5 |
| a-2 | Trois risques (perte, fuite, dépendance à une personne), chacun illustré par un fait des annexes | 0,5 |
| b | Démarche de reprise en quatre étapes (inventaire et profilage, nettoyage, structuration et chargement, contrôle après reprise), appliquée aux chiffres de l'annexe 2.2 ; 0,5 pour deux ou trois étapes justes | 1 |
| c-1 | Trois règles de gouvernance portant sur trois enjeux différents, avec un responsable, appliquées au cas | 0,5 |
| c-2 | Indicateur de qualité complet (formule, source, fréquence, cible, axe), relié à un constat | 0,5 |

**Réponse attendue**

*2.5 a) – Les données, actif immatériel, et leurs risques*

Une donnée est un **actif immatériel** quand l'entreprise la maîtrise et qu'elle en tire une valeur durable : une **valeur d'usage** (mieux décider, mieux servir, gagner du temps) et, parfois, une **valeur d'échange** ; c'est un patrimoine qu'il faut inventorier, protéger et entretenir (F07 § 8.6) (0,5 pt). Les données de Transports CAUVERLIN en sont un : l'historique d'environ 200 000 tournées de 2016 à 2026 renseigne sur les volumes, les délais et les incidents de chaque liaison et servira au calcul des tournées mutualisées ; les contraintes des 2 500 sites sont le savoir-faire qui fidélise les clients ; les 300 grilles de tarifs traduisent la relation commerciale avec 120 chargeurs. Ces données font partie de ce qu'ORMESTAL France a acquis le 4 janvier 2027 ; leur valeur se perd si elles ne sont pas reprises.

Trois risques (0,5 pt) :
- **Perte** : l'ancien logiciel n'est plus maintenu après le 30 septembre 2027 ; sa sauvegarde est faite sur un disque externe rangé dans le bureau du fondateur et n'a jamais été relue ; une partie de l'historique (horaires réels, incidents) n'existe que dans les tableurs des exploitants.
- **Fuite** : les tarifs, qui sont des données confidentielles, sont tenus sur l'ordinateur portable du fondateur et envoyés chaque mois par courriel ; le fichier a déjà été envoyé par erreur à un chargeur en 2025.
- **Dépendance à une personne** : certains tarifs ne sont écrits que « dans la tête » de M. CAUVERLIN, qui part le 31 décembre 2027 ; les contraintes des sites sont connues des deux seuls exploitants.

*2.5 b) – Démarche de reprise en quatre étapes* (1 pt)

1. **Inventaire et profilage des sources** (collecte) : recenser l'ancien logiciel, les tableurs de planification, le fichier des clients et des tarifs, les fichiers de relevés ; mesurer la qualité de chacune (20 doublons sur 140 fiches, SIREN dans la moitié des fiches, 500 adresses incomplètes sur 2 500, 100 grilles sur 300 sans date d'effet) ; décider de ce qui est repris (par exemple les trois dernières années de tournées dans le logiciel de transport, le reste archivé en consultation seule).
2. **Nettoyage** : fusionner les 20 doublons et rattacher les 30 chargeurs communs à leur code d'ORMESTAL France par le SIREN ; compléter les 500 adresses avec les exploitants et les codes des magasins des enseignes ; dater les 100 grilles avec M. CAUVERLIN avant son départ, puis les faire confirmer par les chargeurs ; faire arbitrer par la direction le tarif retenu pour les 12 chargeurs communs qui ont deux tarifs pour une même liaison.
3. **Structuration et chargement** : attribuer à chaque objet l'identifiant du référentiel (client, site, véhicule), convertir les données aux formats du logiciel de gestion du transport et du logiciel de gestion comptable et commerciale, charger d'abord dans un environnement d'essai.
4. **Contrôle après reprise** : comptages (140 fiches devenues 120 clients ; environ 1 000 sites fusionnés et environ 1 500 sites nouveaux ; 85 camions), contrôle par échantillon des fiches et des tarifs, recette signée par chaque propriétaire de référentiel, fonctionnement en parallèle pendant la première vague ; l'ancien logiciel n'est arrêté qu'après cette validation et l'archivage de son historique.

*2.5 c) – Trois règles de gouvernance des données de l'ensemble intégré* (0,5 pt pour les règles, 0,5 pt pour l'indicateur)

| Enjeu | Règle | Responsable |
|---|---|---|
| **Qualité** | tout client, site ou véhicule est créé uniquement dans le référentiel, par un intendant, avec des champs obligatoires (SIREN pour un client, adresse complète, horaires et quai pour un site, date d'effet pour un tarif) ; contrôle mensuel de la qualité | propriétaire de chaque référentiel (Mme MERCOIRAN, Mme VALDRESSE) |
| **Sécurité** | les tarifs et les données des clients sont classés confidentiels et ne sont conservés que dans les applications de l'entreprise, avec des droits d'accès par fonction ; aucun fichier de données sur un poste personnel ni envoyé par courriel ; sauvegardes hors des bureaux, relues au moins une fois par trimestre | responsable des systèmes d'information, M. BRÉVANNE, sur décision des propriétaires |
| **Cycle de vie** (ou **conformité**) | durée de conservation fixée pour chaque catégorie (historique des tournées accessible pendant trois ans puis archivé, archives de l'ancien logiciel conservées en consultation seule puis supprimées au terme de la durée de conservation légale ou contractuelle fixée pour chaque catégorie, les tournées réalisées justifiant la facturation : F07 § 8.4) ; ou, pour la conformité, inscription au registre des traitements des données personnelles reprises (contacts chez les chargeurs, conducteurs) | propriétaires des données, avec le responsable des systèmes d'information |

**Indicateur associé à la règle de qualité** :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de fiches complètes des référentiels clients et sites | fiches comportant tous les champs obligatoires de leur type (client : SIREN et adresse ; site : adresse complète, horaires de réception et quai) / fiches actives | référentiel de données maîtres (contrôle automatique des champs obligatoires) | mensuelle | 100 % des fiches créées après la reprise ; au moins 98 % de l'ensemble fin 2027 (aujourd'hui, la moitié des clients de Transports CAUVERLIN sans SIREN et 500 sites incomplets sur 2 500) | processus |

**Réponses tolérées**
- Autres risques (obsolescence de l'ancien logiciel, erreur de reprise), s'ils s'ajoutent aux trois demandés.
- Démarche présentée selon les cinq étapes de la chaîne de traitement (collecte, nettoyage, structuration, analyse, restitution), si le contrôle après reprise y figure.
- Indicateur de qualité différent mais complet : taux de doublons du référentiel clients (doublons détectés / fiches actives, cible 0 %) ou part des grilles de tarifs datées (grilles avec date d'effet / grilles actives, cible 100 %, un tiers sans date aujourd'hui).
- Mention du délégué à la protection des données, s'il est désigné, pour la règle de conformité, sans analyse juridique.

**Erreurs fréquentes**
- *Valeur comptable des données calculée ou inscription au bilan proposée* — exclu par l'énoncé ; juste : valeur d'usage et risques, sans évaluation comptable (F07 § 8.6).
- *Reprise réduite à une copie des fichiers* — les doublons, les adresses incomplètes et les tarifs non datés seraient transférés tels quels ; juste : nettoyer avant de charger, contrôler après.
- *Règles de gouvernance génériques ou sans responsable* (`JUR-T07` répondre à la seule question posée ; `JUR-T01`) — juste : trois règles appliquées aux constats de l'annexe 2.2, chacune avec un propriétaire.
- *Indicateur sans formule ni cible* (`ET-18`).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Donnée comme actif immatériel, risques de perte, de fuite, d'obsolescence | valeur d'usage et risques, sans évaluation comptable | F07 § 8.6 | notion de cours |
| Chaîne de traitement des données (collecte, nettoyage, structuration) | démarche de reprise | F08 § 0, § 1 et § 4 ; F07 § 8.3 | notion de cours |
| ISO/IEC 25012 (modèle de qualité des données) | dimensions complétude, unicité, exactitude | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| DAMA-DMBOK (2e édition, 2017, révision 2024) | gouvernance, qualité, sécurité, cycle de vie | `dama_dmbok2` / F07 § 8.2 | en vigueur (référentiel) |
| Règlement (UE) 2016/679 (RGPD) | registre des traitements (règle de conformité, simple mention) | `rgpd` / F15 § 2 | en vigueur depuis le 25/05/2018 |
