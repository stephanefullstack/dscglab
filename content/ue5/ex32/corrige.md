# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 32 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance, F08 décisionnel et visualisation, F09 performance du SI, F15 RGPD opérationnel, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le référentiel des personnes accompagnées et les échanges avec les partenaires | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) | 5 |
| 2.2 Les listes d'attente et l'occupation | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 3,5 |
| 2.3 Le tableau de bord des parcours | `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ; `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord ; `3.1.e` Revue et amélioration continue des dispositifs de pilotage | 2,5 |
| 2.4 Le cycle de vie des données des anciens logiciels | `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression ; `2.3.e` Aspects réglementaires (RGPD, archivage légal) et monétisation des données | 2 |
| **Dossier 2 – Organiser et exploiter les données des parcours** |  | **13** |

Répartition indicative : connaissances (données de référence et identifiant, dictionnaire de données, interopérabilité et ses plans, analyses descriptive et exploratoire, tableau de bord et indicateur à cinq champs, cycle de vie des données) environ 3 points (items 2.1 b-1, 2.1 c-1, 2.2 a-1, 2.4 a-1, et la moitié des items 2.1 a-1, 2.3 b-1 et 2.3 c) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le référentiel des personnes accompagnées et les échanges avec les partenaires (5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) ». L'approfondissement technique des échanges est exclu ; l'interopérabilité est traitée sur les plans technique et organisationnel. Aucun modèle des données n'est demandé.

**Annexes mobilisées** : annexes 1.1 (établissements et services, logiciels des trois anciennes associations, organigramme), 2.1 (numéros des trois logiciels, dossiers en trop, notions définies différemment, demandes d'admission et états d'activité, témoignages), 2.2 (rapprochement des listes, valeurs contradictoires) et 2.5 (RGI, DAMA-DMBOK, principes du RGPD).

**Barème indicatif (5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Référentiel des personnes accompagnées tenu dans le dossier unique, seule source qui fait foi pour l'identité et la situation de la personne ; justifié par deux constats chiffrés de l'annexe 2.1 (2 300 dossiers actifs pour 2 000 personnes, trois numéros, listes d'attente éparses, états ressaisis) | 0,5 |
| a-2 | Identifiant de la personne : attribué une seule fois par le dossier unique, unique, non signifiant, stable d'un établissement à l'autre, jamais réattribué ; anciens numéros et numéro de la maison départementale conservés comme références rattachées | 0,5 |
| a-3 | Trois règles de dédoublonnage : critères de rapprochement, traitement des cas certains et des cas douteux (validation humaine, fiche maîtresse, traçabilité de la fusion), contrôle à la saisie pour prévenir les nouveaux doublons ; dédoublonnage fait avant la reprise (0,5 pour les critères et le traitement, 0,5 pour la prévention et le calendrier) | 1 |
| b-1 | Dictionnaire de données défini (description partagée de chaque donnée : nom, définition, format, règle de calcul, source, propriétaire, règle de qualité), distingué d'un modèle des données | 0,5 |
| b-2 | « Place occupée » et « personne en attente » : définition commune, règle de calcul ou d'enregistrement, propriétaire, règle de qualité | 0,5 |
| b-3 | « Sortie » : définition qui distingue sortie de la Fondation et changement d'établissement, règle, propriétaire, règle de qualité ; cohérence d'ensemble des trois fiches | 0,5 |
| c-1 | Interopérabilité définie, avec ses plans technique, sémantique et organisationnel ; formats ouverts et interface de programmation définis | 0,5 |
| c-2 | Maisons départementales : interface de programmation avec celle d'Indre-et-Loire, fichiers en format ouvert déposés sur l'espace sécurisé avec celle du Loir-et-Cher ; deux conditions organisationnelles | 0,5 |
| c-3 | Départements et agence régionale de santé : états d'activité produits à partir du dossier unique selon les définitions communes, fichiers structurés en format ouvert ; deux conditions organisationnelles | 0,5 |

**Réponse attendue**

*2.1 a) – Le référentiel des personnes accompagnées, l'identifiant et le dédoublonnage*

**Le constat** : la Fondation ne sait pas, aujourd'hui, qui elle accompagne. Les trois logiciels comptent 2 300 dossiers « actifs » pour environ 2 000 personnes dans les 32 établissements et services équipés : environ 200 personnes ont deux dossiers et environ 100 dossiers de personnes parties n'ont jamais été clôturés (annexe 2.1 A). Chaque logiciel a son numéro, dont l'un change quand la personne change d'établissement. Les listes d'attente sont tenues par chaque établissement, et les états d'activité sont recopiés à la main. Le même jeune est « sorti » d'un logiciel et « admis » dans un autre (M. ROSPARIN). Mme QUÉRANDEAU le résume : reprendre ces doublons dans le dossier unique, ce serait « les avoir pour vingt ans ».

**Le référentiel des personnes accompagnées** (0,5 pt) : les **données de référence** sont les données partagées et stables dont tous les processus ont besoin (ici : l'identité de la personne, ses représentants légaux, sa décision d'orientation, ses inscriptions en liste d'attente, ses admissions et ses sorties). Elles sont gérées dans un **référentiel unique**, qui fait foi (F07 § 1). Pour la Fondation :
- le référentiel des personnes est tenu **dans le dossier unique**, qui devient la **seule source qui fait foi** pour l'identité, la situation administrative et le parcours de la personne. Une donnée est saisie une fois, à l'endroit où elle naît (l'admission pour l'identité, l'établissement pour les présences), puis elle circule vers les autres usages : planning des équipes, ateliers, états d'activité, tableau de bord ;
- la **liste d'attente commune** fait partie de ce référentiel : une inscription est un événement rattaché à la personne et à un établissement demandé, et non une ligne dans le tableur d'un établissement ;
- les huit établissements à dossiers papier sont intégrés au référentiel dès la reprise : environ 400 personnes doivent y être créées, faute de quoi elles resteront hors du pilotage.

**L'identifiant de la personne** (0,5 pt) :
- un identifiant **attribué une seule fois**, par le dossier unique, lors de la première inscription ou de la première admission ;
- **unique** : une personne, un identifiant ;
- **non signifiant** : ni lettres du nom ni date de naissance, contrairement au numéro de l'ancienne association MIRANDELLE, car un nom s'écrit de plusieurs façons et peut changer ; ni code d'établissement, contrairement au numéro de l'ancienne association LUMERANDE ;
- **stable** tout au long du parcours, d'un établissement et d'un pôle à l'autre, **jamais réattribué**, même après la sortie ;
- les **anciens numéros** des trois logiciels sont conservés comme références rattachées (table de correspondance utile pour la reprise et l'archivage, question 2.4). Le **numéro de la maison départementale** est enregistré comme référence externe, utile aux échanges ; il ne sert pas d'identifiant, car toutes les personnes n'en ont pas et il change quand la personne change de département.

**Trois règles de dédoublonnage** (1 pt), parmi :
1. **Critères de rapprochement** : nom de naissance, prénom, date de naissance et commune de naissance, ainsi que le numéro de la maison départementale quand il existe ; le nom d'usage est enregistré à part, avec des comparaisons tolérantes (accents, inversions, fautes de frappe) pour repérer les cas probables.
2. **Traitement des cas certains et des cas douteux** : la fusion est automatique si tous les critères concordent ; si seuls certains concordent, une **validation humaine** est confiée à l'équipe de l'admission et des parcours (intendante des données des personnes), qui vérifie avec l'établissement. Une seule **fiche maîtresse** est retenue ; les autres dossiers lui sont rattachés et non supprimés à l'aveugle, et chaque fusion est **tracée** (qui, quand, quels dossiers) pour pouvoir être annulée.
3. **Prévention** : avant toute création, le dossier unique recherche les personnes proches, et la création d'un doublon probable est bloquée ou signalée. La **clôture** du dossier est obligatoire à la sortie de la Fondation, et un contrôle mensuel des doublons probables et des dossiers sans activité est confié à l'intendante.
4. **Calendrier** : dédoublonner **avant la reprise**, à partir des extractions en tableur fournies par les éditeurs (annexe 2.4), en commençant par les 300 dossiers en trop ; ne reprendre que des fiches validées.

*2.1 b) – Un extrait de dictionnaire de données*

Un **dictionnaire de données** est le référentiel qui décrit chaque donnée de manière partagée : son nom, sa définition, son format et son domaine de valeurs, sa règle de calcul ou d'enregistrement, sa source, son propriétaire, sa sensibilité et ses règles de qualité (0,5 pt). Il fixe le **sens** des données, et non leur structure : ce n'est pas un modèle conceptuel. Il sert ici à mettre fin aux trois définitions héritées (annexe 2.1 B), qui rendent incomparables les chiffres des établissements (95 % ou 91 % d'occupation, 280 ou 220 sorties, annexe 2.2 C) (F07 § 1 et 8.3).

| Notion | Définition commune | Règle de calcul ou d'enregistrement | Propriétaire | Règle de qualité |
|---|---|---|---|---|
| **Place occupée** (0,5 pt avec la suivante) | une place est occupée un jour donné si une personne admise y est présente, ou absente pour un motif enregistré (hospitalisation, retour en famille, vacances) depuis moins d'une durée fixée par la Fondation (par exemple quinze jours) | taux d'occupation = journées d'occupation / (places × jours d'ouverture) ; journées de présence et d'absence comptées séparément, pour pouvoir produire aussi les journées de présence demandées par les financeurs | directrice générale, sur proposition des directeurs de pôle (définition commune à toute la Fondation) | présence ou absence saisie chaque jour pour chaque personne ; motif d'absence obligatoire ; aucune journée d'occupation sans admission en cours |
| **Personne en attente** | personne non accueillie dans l'établissement demandé, qui a une décision d'orientation correspondante, une demande d'admission enregistrée et confirmée depuis moins de douze mois ; une personne déjà accompagnée par la Fondation qui attend une autre solution est comptée à part | nombre de personnes **distinctes** (par identifiant) ayant au moins une inscription en cours ; le nombre d'inscriptions est suivi à part | responsable de l'admission et des parcours | une personne n'a qu'une inscription par établissement demandé ; date de dernière confirmation renseignée ; relance à onze mois et retrait sans confirmation à douze mois ; retrait automatique de toutes les inscriptions à l'admission |
| **Sortie** (0,5 pt) | **sortie de la Fondation** : fin de tout accompagnement par la Fondation ; un passage d'un établissement à un autre de la Fondation est un **changement d'établissement**, enregistré comme tel, et non une sortie | date et motif de sortie (orientation ailleurs, retour à domicile, déménagement, décès…) obligatoires ; un changement d'établissement clôt le séjour et en ouvre un autre dans le même dossier | responsable de l'admission et des parcours, pour le compte de la directrice générale | aucun dossier sans activité depuis plus de trois mois sans sortie ni absence motivée ; nombre de sorties rapproché chaque mois du nombre de dossiers clôturés |

Les propriétaires sont des **responsables métiers**, et non la DSI : ils arbitrent les définitions et la qualité attendue. Des **intendants** (équipe de l'admission, secrétariats des établissements) corrigent les anomalies au quotidien (F07 § 8.1). Le DAMA-DMBOK (annexe 2.5) range ces sujets dans ses domaines « données de référence », « métadonnées » et « qualité des données ».

*2.1 c) – Les échanges avec les maisons départementales et les financeurs*

L'**interopérabilité** est la capacité de systèmes hétérogènes, appartenant le cas échéant à des organisations différentes, à échanger des données et à les utiliser sans ressaisie (0,5 pt). Elle a un plan **technique** (moyen d'échange : interface de programmation, dépôt de fichiers), un plan **syntaxique** (format), un plan **sémantique** (même sens des données : le dictionnaire de la question b) et un plan **organisationnel** (qui transmet quoi, quand, sous quelle responsabilité). Une **interface de programmation (API)** permet à un logiciel d'interroger ou d'alimenter un autre logiciel automatiquement. Un **format ouvert** est un format dont la spécification est publique et que tout logiciel peut lire. Le RGI (annexe 2.5) recommande ces formats aux administrations, dont les départements : la Fondation a intérêt à s'y aligner (F07 § 7).

**Avec les deux maisons départementales des personnes handicapées** (0,5 pt) :
- **Solution** : avec celle d'Indre-et-Loire, une **interface de programmation** entre le dossier unique et son service de suivi des orientations. Le dossier unique reçoit les décisions d'orientation et les demandes, qui alimentent la liste d'attente commune sans ressaisie, et il renvoie chaque mois les admissions, comme le souhaite la maison départementale (annexe 2.1 C). Avec celle du Loir-et-Cher, un **fichier structuré en format ouvert** (par exemple un fichier à séparateurs ou XML) déposé sur l'espace d'échange sécurisé, produit automatiquement par le dossier unique.
- **Deux conditions organisationnelles**, parmi : une **convention d'échange** avec chaque maison départementale (données échangées, fréquence, délais, interlocuteurs, traitement des anomalies) ; un **interlocuteur unique** à la Fondation (l'équipe de l'admission et des parcours) au lieu de quarante établissements ; une correspondance entre le numéro de la maison départementale et l'identifiant de la Fondation ; des échanges limités aux données nécessaires (minimisation, annexe 2.5), et non des tableurs contenant des diagnostics envoyés par courriel (Mme PELLEGRAIN).

**Avec les deux départements et l'agence régionale de santé** (0,5 pt) :
- **Solution** : les états d'activité sont **produits par le dossier unique** à partir des données saisies une seule fois et des définitions communes du dictionnaire (journées de présence, personnes accompagnées, admissions, sorties). Ils sont transmis sous forme de **fichiers structurés en format ouvert**, selon le modèle de chaque financeur, ou par un service en ligne de dépôt si le financeur en propose un. On supprime ainsi les deux jours de recopie mensuels par secrétariat (Mme TRÉMOLIÈRE) et les corrections du siège.
- **Deux conditions organisationnelles**, parmi : une **table de correspondance** entre les définitions de la Fondation et celles de chaque financeur (par exemple : journées de présence, sans les absences), validée avec lui ; un **circuit de validation** (directeur d'établissement, puis siège) avant l'envoi ; à terme, un modèle commun négocié avec les deux départements ; un calendrier d'envoi fixe et une personne responsable au siège.

**Réponses tolérées**
- Référentiel des personnes présenté comme une démarche de gestion des données de référence, si le terme est écrit en toutes lettres et si le référentiel reste dans le dossier unique (aucune nouvelle base n'est justifiée).
- Autres critères de rapprochement (adresse, nom des parents) ou autres règles de prévention (liste des pièces obligatoires à la création), s'ils sont justifiés.
- Autres définitions des trois notions, si elles sont uniques pour toute la Fondation, mesurables et accompagnées d'une règle et d'un propriétaire ; propriétaire unique (la directrice générale) pour les trois notions.
- Échange de données informatisé ou plateforme d'échange cités, si les plans sémantique et organisationnel sont traités ; interface de programmation proposée aussi avec le Loir-et-Cher à terme.
- Plans de l'interopérabilité présentés en deux ou trois niveaux (le plan syntaxique rattaché au plan technique).

**Erreurs fréquentes**
- *Modèle des données hors attente* (`JUR-T06`, `ET-23`) — entités, associations et cardinalités dessinées au lieu de règles d'organisation, alors que la question les exclut.
- *Identifiant signifiant ou externe* — identifiant construit avec le nom et la date de naissance, ou numéro de la maison départementale pris comme identifiant ; juste : identifiant interne, non signifiant et stable, avec des références externes rattachées.
- *Dédoublonnage aveugle* — suppression automatique des dossiers proches, sans validation ni traçabilité : on perd des informations ou on fusionne deux personnes différentes.
- *Sigle ambigu* (`ET-13`) — « mettre en place un MDM » sans préciser qu'il s'agit de la gestion des données de référence.
- *Interopérabilité seulement technique* (`ET-36`) — interface de programmation proposée partout, sans convention, sans définitions communes ni interlocuteur.
- *Morceau de cours* (`JUR-T01`) — définitions du dictionnaire ou de l'interopérabilité sans les trois notions et sans les partenaires du cas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Référentiel général d'interopérabilité (RGI), version 2.0, arrêté du 20/04/2016 | normes et standards recommandés aux administrations, formats ouverts | `rgi_v2` / F07 § 7 | en vigueur |
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines données de référence, métadonnées, qualité, intégration et interopérabilité | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Données de référence, identifiant, dictionnaire de données, dimensions de la qualité, propriétaire et intendant, plans de l'interopérabilité | définitions et principes | F07 § 1, 7, 8.1 et 8.3 | notion de cours |

---

### 2.2 – Les listes d'attente et l'occupation (3,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Aucun calcul statistique ni aucune manipulation d'outil ; lecture critique des biais, reliée à la stratégie.

**Annexes mobilisées** : annexes 1.1 (900 personnes annoncées en liste d'attente, projet « Horizon 2030 »), 2.1 (définitions héritées, listes tenues par établissement) et 2.2 (tableau par pôle, rapprochement des listes, valeurs contradictoires, demande du président).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Analyse descriptive et analyse exploratoire définies et distinguées ; analyse prédictive écartée ou située | 0,5 |
| a-2 | Méthode retenue et justifiée par l'annexe 2.2 : description fiable d'abord, après nettoyage (dédoublonnage, définitions), puis exploration des causes (places vacantes, parcours bloqués) ; place dans la chaîne de traitement | 0,5 |
| b-1 | Premier constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-2 | Deuxième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-3 | Troisième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| c-1 | Réponse au président, de tête : 900 inscriptions, 600 personnes distinctes, 450 non accompagnées par la Fondation, environ 350 dont la demande est confirmée, plus 150 personnes déjà accompagnées qui attendent une autre solution ; durée d'attente réelle non mesurée, avec la raison | 0,5 |
| c-2 | Deux représentations adaptées au conseil d'administration, chacune justifiée par son message et assortie d'un piège évité | 0,5 |

**Réponse attendue**

*2.2 a) – Le choix de la méthode d'analyse*

L'**analyse descriptive** résume ce qui s'est passé : effectifs, agrégats, répartitions, évolutions et écarts à une cible. L'**analyse exploratoire** recherche, sans hypothèse arrêtée à l'avance, des profils, des valeurs atypiques, des croisements et des relations qui orientent vers des explications. L'**analyse prédictive** estime ce qui va se passer (prévision, score) (F08 § 2) (0,5 pt).

**La méthode retenue** (0,5 pt) : une **analyse descriptive d'abord**, parce que la question du conseil d'administration est descriptive (combien de personnes, depuis combien de temps) et que les chiffres actuels ne sont même pas fiables. Elle n'a de sens qu'après le **nettoyage** des données : dédoublonnage des 900 inscriptions, retrait des demandes non confirmées, définitions communes. C'est l'étape de la chaîne de traitement que la Fondation a sautée jusqu'ici (collecte, nettoyage, structuration, analyse, restitution, F08 § 1). Vient ensuite une **analyse exploratoire**, pour comprendre pourquoi des places restent vides alors que des personnes attendent, et où se bloquent les parcours : croisement des délais de vacance, des délais d'attente, des inscriptions multiples et des jeunes adultes maintenus en institut médico-éducatif. Une analyse prédictive (prévoir les besoins de places) serait prématurée : les données de base sont incertaines et l'historique n'existe pas encore.

*2.2 b) – Trois constats argumentés et leurs précautions de lecture*

Trois constats parmi les suivants (0,5 pt chacun : le fait chiffré, son interprétation au regard des parcours, la précaution de lecture) :

1. **Un tiers des inscriptions sont des doublons.** Les 900 « personnes en attente » du rapport annuel (annexe 1.1) sont 900 **inscriptions**, qui correspondent à 600 personnes distinctes : 150 personnes sont inscrites sur deux listes et 50 sur quatre. S'y ajoutent 100 demandes non confirmées depuis plus d'un an, dont une majorité sont probablement caduques (six familles sur dix jointes). *Précaution* : le rapprochement a été fait à la main, sur le nom, le prénom et la date de naissance ; certaines personnes n'ont pas pu être rapprochées avec certitude. Le chiffre de 600 est donc un ordre de grandeur, et l'échantillon de dix familles est trop petit pour être généralisé. Les sources divergent d'ailleurs : 350 ou 280 personnes en attente pour le pôle Enfance (annexe 2.2 C), selon que l'on compte les demandes des familles ou les orientations notifiées.
2. **Des places restent vides alors que des personnes attendent.** Entre une sortie et l'admission suivante s'écoulent en moyenne 45 jours dans le pôle Enfance et 60 jours dans le pôle Hébergement, où l'attente dure trois ans et où 300 inscriptions sont en cours. Le manque n'est donc pas seulement un manque de places : c'est un défaut de **coordination**. Les listes sont dispersées, et le dossier de la personne suivante n'est pas prêt quand la place se libère. C'est précisément ce que vise le passage « des places aux parcours » d'« Horizon 2030 ». *Précaution* : un délai moyen masque la dispersion (quelques places restées vides plusieurs mois suffisent à l'allonger), et une « sortie » n'a pas le même sens d'une ancienne association à l'autre (280 ou 220 sorties, annexe 2.2 C).
3. **Les parcours se bloquent au passage à l'âge adulte.** 100 jeunes adultes de plus de 20 ans restent dans un institut médico-éducatif faute de place en foyer ou en établissement d'aide par le travail. Ils occupent des places du pôle Enfance (96 % d'occupation, deux ans d'attente), alors que les pôles pour adultes ont les attentes les plus longues (trois ans pour l'Hébergement, 18 mois pour le Travail). L'engorgement des pôles pour adultes se reporte donc sur le pôle Enfance. *Précaution* : c'est une relation plausible, non démontrée. Les durées d'attente du pôle Enfance ont aussi d'autres causes possibles, et une corrélation n'est pas une causalité. Il faudrait suivre les parcours personne par personne, ce que permettra l'identifiant unique.
4. **Les taux d'occupation ne sont pas comparables.** Le pôle Hébergement affiche 95 % dans le tableau de bord du siège et 91 % dans l'état transmis au département. L'écart s'explique pour l'essentiel par les absences (environ 4 % des journées) : elles sont comptées comme occupation selon la définition de l'ancienne association GERVELLE, et en partie selon celle de LUMERANDE, mais pas dans les journées de présence. Le taux de 90 % du pôle Domicile n'est donc pas forcément le plus faible. *Précaution* : aucun classement des établissements ni des pôles avant l'application de la définition commune (question 2.1 b).
5. **Le délai d'attente est sous-estimé.** Il n'est calculé que sur les personnes admises en 2026 : celles qui attendent toujours, souvent depuis plus longtemps, en sont exclues (biais de sélection). Au rythme de 2026, les 300 inscriptions du pôle Hébergement représentent plus de sept années d'admissions (300 pour 40 par an), contre trois ans affichés. *Précaution* : ces 300 inscriptions contiennent des doublons ; l'ordre de grandeur reste cependant très supérieur à trois ans.

*2.2 c) – La réponse au président et deux représentations*

**La réponse à M. LABASTROU** (0,5 pt), de tête :
- 900 inscriptions sur les listes des établissements ;
- soit **600 personnes distinctes** (400 + 150 + 50) ;
- dont **150** déjà accompagnées par la Fondation, qui attendent une autre solution (dont 100 jeunes adultes en institut médico-éducatif) ;
- soit **450 personnes** que la Fondation n'accompagne pas encore ;
- dont environ **350** dont la demande est confirmée depuis moins d'un an, les 100 autres devant être relancées avant d'être comptées.

Réponse : « Environ 350 personnes attendent vraiment une première place, et 150 personnes déjà accompagnées attendent une autre solution ; le chiffre de 900 compte des inscriptions et non des personnes. » **Depuis combien de temps** : la Fondation ne le sait pas. Le délai publié (deux à trois ans selon les pôles) ne porte que sur les personnes admises, et chaque établissement tient sa liste dans un tableur ou dans un cahier (annexe 2.1 C), sans date d'inscription commune. Il faut l'écrire, et le mesurer dès la mise en service de la liste d'attente commune (date d'inscription et de dernière confirmation obligatoires).

**Deux représentations** (0,5 pt), parmi :
- **Barres horizontales décroissantes, de type entonnoir** : 900 inscriptions, 600 personnes distinctes, 450 personnes non accompagnées, 350 demandes confirmées, avec, sur chaque barre, la raison de l'écart (doublons, personnes déjà accompagnées, demandes non confirmées). *Message* : comment on passe de 900 à 350. *Piège évité* : la mention de la source et de la date du rapprochement manuel évite de présenter 350 comme un chiffre exact.
- **Barres groupées par pôle**, avec pour chaque pôle les inscriptions en attente et les admissions de l'année. *Message* : dans le pôle Hébergement, 300 inscriptions pour 40 admissions par an. *Piège évité* : on compare des volumes de même nature, avec une échelle qui part de zéro, et l'on signale que les inscriptions contiennent des doublons.
- **Barres par pôle du délai moyen entre une sortie et l'admission suivante**, avec une ligne cible (par exemple 15 jours). *Message* : des places restent vides de 20 à 60 jours. *Piège évité* : une moyenne sans dispersion ; l'on indique le nombre de places concernées.
- **Courbe mensuelle**, à partir de la mise en service de la liste commune, du nombre de personnes distinctes en attente. *Message* : l'évolution. *Piège évité* : on ne la montre qu'à partir de données fiables, sans la raccorder à l'ancien chiffre de 900.

Un graphique en secteurs à quatre pôles ou un tableau de chiffres sans référence sont de mauvais choix pour un conseil d'administration qui doit comprendre un écart.

**Réponses tolérées**
- Analyse exploratoire placée en premier, si le candidat montre qu'elle sert d'abord à repérer les doublons et les incohérences avant toute description.
- Autres constats tirés de l'annexe 2.2 (rythme d'admission très différent entre le pôle Domicile et le pôle Hébergement, divergence des sorties), s'ils portent une précaution.
- Réponse au président donnée sous forme de fourchette (350 à 450 personnes extérieures), si les 150 personnes déjà accompagnées sont distinguées.
- Autres représentations (graphique en cascade, jauge par pôle avec cible), si le message et le piège sont précisés.

**Erreurs fréquentes**
- *Additionner les inscriptions comme des personnes* — répondre « 900 personnes » ou ajouter les listes des pôles ; juste : 600 personnes distinctes, puis le tri.
- *Corrélation présentée comme une causalité* (`ET-26`) — « les jeunes adultes sont la cause des délais du pôle Enfance » sans réserve.
- *Prudence d'interprétation absente* (`JUR-D06`) — prendre le délai moyen des personnes admises pour le délai d'attente réel, ou comparer des taux d'occupation de définitions différentes.
- *Calcul ou outil hors attente* (`JUR-T07`) — moyennes pondérées, écarts-types, prévisions, ou description de la manipulation d'un outil décisionnel.
- *Constat sans conséquence* (`JUR-T03`) — chiffres recopiés sans lien avec la coordination des parcours voulue par « Horizon 2030 ».

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Analyses descriptive, exploratoire et prédictive ; chaîne de traitement des données | définitions et choix de la méthode | F08 § 1 et 2 | notion de cours |
| Choix d'une représentation, biais de sélection, corrélation et causalité | représentations et précautions | F08 § 5 | notion de cours |

---

### 2.3 – Le tableau de bord des parcours (2,5 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) » ; `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.e` « Revue et amélioration continue des dispositifs de pilotage ». Limite : des indicateurs choisis avec recul critique, reliés aux objectifs.

**Annexes mobilisées** : annexes 1.1 (pôles, comité de direction, projet « Horizon 2030 »), 2.2 (délais, jeunes adultes maintenus) et 2.3 (tableau actuel, extrait de mars 2027, attentes).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Quatre critiques appuyées sur l'annexe 2.3 A : trop d'indicateurs et sans hiérarchie, aucune cible ni commentaire, pas d'indicateur des parcours, envoi tardif et identique à tous, volumes non comparables, définitions hétérogènes | 0,5 |
| b-1 | Tableau de bord défini (ensemble restreint d'indicateurs reliés à des objectifs, avec cibles, pour décider) ; destinataires (quatre directeurs de pôle, avec comparaison de leurs établissements), fréquence et alimentation par le dossier unique | 0,5 |
| b-2 | Quatre indicateurs (activité, qualité de l'accompagnement, ressources, risque), chacun avec sa formule, sa source, sa fréquence, sa cible justifiée et son axe (0,5 pour deux indicateurs complets, 0,5 pour les deux autres) | 1 |
| c | Revue périodique : lecture mensuelle en comité de pôle avec actions, révision annuelle des indicateurs et des cibles au regard d'« Horizon 2030 », suppression de ce qui n'est pas utilisé, mesure de l'usage (logique d'amélioration continue) | 0,5 |

**Réponse attendue**

*2.3 a) – Critique du tableau de bord actuel*

Quatre arguments parmi (0,5 pt) :
1. **Un rapport et non un tableau de bord** : 30 indicateurs sur six pages, sans hiérarchie, qui mêlent activité, ressources humaines et finances et descendent jusqu'aux repas servis et aux litres de carburant. Un directeur n'y trouve pas ce qui demande une décision ; 10 directeurs sur 44 le lisent.
2. **Aucune cible, aucun seuil, aucun commentaire** : 95 % d'occupation ou 9 % d'absentéisme ne disent ni si c'est bien, ni qui doit agir.
3. **Rien sur les parcours** : aucun indicateur sur les délais d'attente, les places vacantes, les jeunes adultes maintenus ou la révision des projets personnalisés, alors qu'« Horizon 2030 » veut passer « des places aux parcours » (Mme BRÉCHEVAL, Mme LÉVRAUD). Les postes vacants, qui fragilisent l'accompagnement, n'y figurent pas (Mme OSMONDE).
4. **Des chiffres peu fiables et mal présentés** : définitions de chaque ancienne association ; 910 « personnes en attente » qui sont des inscriptions ; des volumes bruts qui trompent (les journées « augmentent » de 49 000 à 54 000 parce que mars a 31 jours et février 28) ; des charges cumulées qu'on ne peut comparer d'un mois à l'autre.
5. **Un document tardif, coûteux et uniforme** : cinq jours de travail par mois de recopie d'extractions, un envoi vers le 25 du mois suivant, la même version pour la directrice générale et pour chaque directeur d'établissement, et rien pour le conseil d'administration.

*2.3 b) – Le tableau de bord des parcours des directeurs de pôle*

Un **tableau de bord** est un ensemble **restreint** d'indicateurs choisis pour piloter des objectifs : il est présenté avec ses cibles, ses seuils d'alerte et ses tendances, et sert à décider et à agir (F08 § 3 ; F09 § 4.1).

**Destinataires, fréquence, alimentation** (0,5 pt) :
- les **quatre directeurs de pôle** : chacun voit son pôle, ses établissements comparés entre eux et la moyenne de la Fondation (M. MARCILHAC). La directrice générale reçoit la synthèse des quatre pôles, et chaque directeur d'établissement la page de son établissement ; un extrait trimestriel de quelques indicateurs est présenté au conseil d'administration (M. LABASTROU) ;
- **mensuel**, disponible dans les premiers jours du mois, avec une **alerte** dès qu'un indicateur franchit son seuil (une place libérée depuis plus de quinze jours, par exemple) ;
- **alimenté par le dossier unique**, le progiciel de paie et de gestion des ressources humaines, selon les définitions du dictionnaire (question 2.1 b), sans recopie : le temps de la contrôleuse de gestion passe de la production à l'analyse.

**Quatre indicateurs** (1 pt), équilibrant activité, qualité, ressources et risque :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Activité** – taux d'occupation, selon la définition commune | journées d'occupation selon la définition commune / (places × jours d'ouverture) | dossier unique (présences et absences motivées) | mensuelle | au moins 95 %, à confirmer après six mois de mesure selon la définition commune ; alerte en dessous de 92 % | processus |
| **Qualité de l'accompagnement** – part des projets personnalisés à jour | nombre de personnes dont le projet personnalisé a été révisé depuis moins de douze mois / nombre de personnes accompagnées depuis plus de douze mois | dossier unique (module du projet personnalisé) | mensuelle | 90 % fin 2027 et 100 % fin 2028 (environ 70 % en mars 2027) | client |
| **Ressources** – taux de postes d'accompagnement vacants | nombre de postes d'accompagnement non pourvus en fin de mois / nombre de postes d'accompagnement prévus | progiciel de paie et de gestion des ressources humaines | mensuelle | au plus 4 % fin 2027 (7 % fin mars 2027) | apprentissage |
| **Risque** – jeunes adultes maintenus faute de place adaptée | nombre de personnes de plus de 20 ans accompagnées par un institut médico-éducatif et inscrites en attente d'un établissement pour adultes | dossier unique (date de naissance, inscriptions de la liste d'attente commune) | mensuelle | au plus 70 fin 2027 et 40 fin 2028 (100 en mars 2027) | client |

Chaque indicateur répond à un constat des annexes : définitions hétérogènes de l'occupation, enquête sur les projets personnalisés, postes vacants signalés par la DRH, parcours bloqués du pôle Enfance. Ensemble, ils mesurent l'activité, la qualité, les ressources et le risque de rupture de parcours, et non plus les seuls volumes.

*2.3 c) – La revue du tableau de bord*

La revue applique la logique d'**amélioration continue** (roue de Deming, ou PDCA : planifier, faire, vérifier, agir ; périmètre 3.1.e) (0,5 pt), parmi :
- **chaque mois**, en réunion de pôle : lecture des écarts à la cible, commentaire et action décidée pour chaque alerte, suivi des actions du mois précédent ;
- **chaque trimestre**, au comité de direction : synthèse des quatre pôles, arbitrages entre pôles (places pour adultes, par exemple), extrait pour le conseil d'administration ;
- **chaque année** : revue complète. Les indicateurs servent-ils encore « Horizon 2030 » ? Sont-ils lus et fiables ? Les cibles sont révisées, ce qui n'est pas utilisé est supprimé et, si besoin, un indicateur est ajouté (délai de réattribution d'une place, par exemple). L'avis des directeurs est recueilli, et l'usage réel est mesuré (consultations) ;
- un **dictionnaire des indicateurs** tenu par le responsable du contrôle interne et de la performance ou par la contrôleuse de gestion (formule, source, propriétaire, date de modification), pour que toute modification soit tracée.

**Réponses tolérées**
- Autres indicateurs complets et justifiés par les annexes, par exemple : délai moyen de réattribution d'une place libérée (cible au plus 15 jours, 20 à 60 jours en 2026, axe client) ; part des inscriptions confirmées depuis moins de douze mois (axe processus) ; heures d'intérim rapportées aux heures travaillées (axe financier ou apprentissage) ; part des événements indésirables analysés dans le mois (axe processus).
- Axes ESG au lieu des axes du tableau de bord prospectif (axe social pour les postes vacants), s'ils sont cohérents.
- Fréquence hebdomadaire pour l'alerte sur les places libérées, mensuelle pour le reste.

**Erreurs fréquentes**
- *Indicateurs génériques ou incomplets* (`ET-18`, `JUR-A02`) — liste sans formule, source, cible ou axe, ou sans lien avec un constat des annexes.
- *Tableau de bord du système d'information* — disponibilité du dossier unique ou délai de résolution des incidents, alors que la question porte sur les parcours.
- *Plus d'indicateurs qu'avant* — reprendre les 30 indicateurs et en ajouter, au lieu d'un tableau resserré.
- *Cible sans référence* — « 100 % » partout, sans le point de départ de mars 2027 ni d'échéance.
- *Morceau de cours* (`JUR-T01`) — définition du tableau de bord ou du tableau de bord prospectif sans application aux directeurs de pôle.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Tableau de bord, indicateur à cinq champs, axes du tableau de bord prospectif et ESG | conception du tableau de bord | F08 § 3 ; F09 § 4.1 | notion de cours |
| Revue et amélioration continue, roue de Deming (PDCA) | revue du tableau de bord | F09 § 4.3 ; périmètre 3.1.e (notions incluses) | notion de cours |

---

### 2.4 – Le cycle de vie des données des anciens logiciels (2 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.b` « Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression » ; `2.3.e` « Aspects réglementaires (RGPD, archivage légal) et monétisation des données ». Les durées de conservation sont données par l'énoncé ; aucune analyse juridique ; ni hébergement ni souveraineté.

**Annexes mobilisées** : annexes 2.1 (dossiers en trop, tableurs qui circulent), 2.4 (contenu des anciens logiciels, coûts, contrats, trois options, avis) et 2.5 (principes du RGPD, durées de conservation retenues).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cycle de vie défini et ses cinq étapes (création, stockage, usage, archivage, suppression), avec la durée de conservation comme fil conducteur | 0,5 |
| a-2 | Étapes appliquées aux données des personnes de la Fondation et aux deux durées données : archivage à la sortie de la Fondation et non à un changement d'établissement, destruction à 20 ans et à 2 ans, volumes à détruire dès maintenant (1 500 et 1 000 dossiers, 2 000 demandes) | 0,5 |
| b-1 | Trois options comparées au regard de la minimisation, de la limitation de la conservation, de la confidentialité, du coût de tête sur les cinq ans demandés (150 k€ ; 120 k€ ; 84 k€ par an, soit 420 k€) et des risques | 0,5 |
| b-2 | Recommandation argumentée (option 2) et ses conditions : destruction préalable de ce qui a dépassé les durées, correspondance des numéros, accès tracé, dossiers papier, résiliation des contrats | 0,5 |

**Réponse attendue**

*2.4 a) – Le cycle de vie des données des personnes accompagnées*

Le **cycle de vie** des données décrit les étapes qu'une donnée traverse de sa création à sa suppression : **création** (ou collecte), **stockage**, **usage** (traitement et partage), **archivage**, **suppression**. Pour chaque étape, on fixe un responsable et des règles, et la **durée de conservation** (utilité courante, puis conservation intermédiaire, puis sort final) en est le fil conducteur (F07 § 8.4) (0,5 pt).

**Appliqué à la Fondation** (0,5 pt) :

| Étape | Données des personnes accompagnées |
|---|---|
| Création | la demande d'admission crée la personne dans le référentiel et son inscription dans la liste d'attente commune ; le dossier s'enrichit à l'admission. On ne collecte que ce qui est nécessaire à l'accompagnement (minimisation), avec une date de dernière confirmation de la demande |
| Stockage | dans le dossier unique, hébergé dans l'Union européenne par un éditeur dont l'offre satisfait aux exigences applicables aux données de santé (annexe 2.4, sans analyse), et non dans des tableurs envoyés par courriel |
| Usage | accompagnement au quotidien, selon les droits de chaque professionnel ; échanges limités aux données nécessaires avec les maisons départementales et les financeurs (question 2.1 c) ; pilotage sur des données agrégées (question 2.3) |
| Archivage | à la **sortie de la Fondation**, et non à un changement d'établissement (le dossier suit la personne) : dossier clôturé, retiré de l'usage courant, accessible seulement sur demande motivée, avec un accès tracé, pendant **20 ans** après la dernière sortie |
| Suppression | destruction à l'issue des 20 ans pour le dossier, et **2 ans** après le dernier contact pour une demande qui n'a pas abouti ; destruction tracée et validée par la déléguée à la protection des données. **Dès maintenant**, les règles données conduisent à détruire environ 1 500 dossiers des anciens logiciels et 1 000 dossiers papier sortis depuis plus de 20 ans, ainsi qu'environ 2 000 demandes non abouties sans contact depuis plus de deux ans (annexe 2.4 A) |

*2.4 b) – Les trois options et la recommandation*

**Comparaison** (0,5 pt) :

| Critère | Option 1 : tout reprendre | Option 2 : actifs repris, autres archivés | Option 3 : anciens logiciels en consultation |
|---|---|---|---|
| Minimisation et limitation de la conservation (annexe 2.5) | 8 000 dossiers de personnes sorties et 150 000 pièces dans l'outil de travail quotidien, dont 1 500 dossiers à détruire : contraire au principe | seules les données nécessaires à l'accompagnement restent dans le dossier unique ; l'export est l'occasion de détruire ce qui a dépassé les durées | aucune purge prévue ; les données restent sans limite de durée |
| Confidentialité | dossiers anciens visibles par tous les utilisateurs selon leurs droits habituels | consultation sur demande motivée, chaque accès enregistré | comptes actuels des anciens logiciels, peu maîtrisés ; logiciels vieillissants |
| Qualité du référentiel | doublons et dossiers non clôturés repris : le référentiel naît pollué (« on les aura pour vingt ans ») | dédoublonnage limité aux 2 300 dossiers actifs | — |
| Coût (de tête) | 150 k€ une fois | 60 + 5 × 12 = 120 k€ sur cinq ans | (4 + 3) × 12 = 84 k€ par an, soit 420 k€ sur cinq ans, sans fin |
| Risques et dépendance | contrôle de reprise alourdi, retard possible du projet | formats ouverts lisibles sans les éditeurs ; travail d'export et de classement | dépendance aux anciens éditeurs ; les 1 000 dossiers du logiciel de l'ancienne association LUMERANDE doivent de toute façon être exportés |

**Recommandation : l'option 2** (0,5 pt). C'est la seule qui applique la minimisation et la limitation de la conservation : le dossier unique ne contient que les personnes accompagnées, et les dossiers des personnes sorties restent consultables pendant la durée retenue, dans des formats ouverts, avec un accès restreint et tracé, ce qui permet aussi de répondre à une personne qui demande communication de son dossier. Sur les cinq ans demandés par la directrice générale, son coût (120 k€) est inférieur à celui de l'option 1 (150 k€). Il la dépasserait au-delà de sept ans et demi, mais l'écart reste modeste et sans commune mesure avec l'option 3, qui se prolongerait sans fin : le choix repose d'abord sur la minimisation et la limitation de la conservation. Conditions :
- **détruire avant l'export** ce qui a dépassé les durées (environ 1 500 dossiers, 2 000 demandes, et 1 000 dossiers papier), après validation par la déléguée à la protection des données et la directrice générale, en gardant une trace de la destruction ;
- conserver la **table de correspondance** entre les anciens numéros et l'identifiant unique, pour retrouver un dossier archivé ;
- fixer la **procédure de consultation** des archives et sa durée de 20 ans, avec une destruction programmée à l'échéance ;
- **dossiers papier** : les inventorier ; numériser ceux des personnes accompagnées avant la reprise et conserver les dossiers de personnes sorties en armoire jusqu'à leur échéance ;
- **résilier les trois contrats** avec un préavis de trois mois avant leur échéance annuelle, une fois la reprise et l'archivage contrôlés, pour ne pas payer une année de plus.

**Réponses tolérées**
- Cycle de vie en sept étapes (collecte, stockage, traitement, partage, archivage, destruction…), s'il couvre les cinq étapes du programme.
- Option 1 limitée aux dossiers encore dans leur durée de conservation et placés dans un espace d'archives à accès restreint du dossier unique, si le candidat justifie la minimisation et les droits d'accès.
- Mention d'un archivage électronique à valeur probante (norme NF Z42-013) en complément, sans développement.
- Calcul sur une autre durée (par exemple dix ans : 180 k€ pour l'option 2, 840 k€ pour l'option 3), si le raisonnement est juste et si le candidat relève que l'option 1 devient alors moins chère que l'option 2.

**Erreurs fréquentes**
- *Cycle de vie récité* (`JUR-T01`) — cinq étapes définies sans les durées de l'annexe 2.5 ni les volumes de l'annexe 2.4.
- *Archivage confondu avec la sauvegarde* — proposer des copies de sécurité au lieu d'un archivage à accès restreint et à durée fixée.
- *Analyse juridique hors attente* (`JUR-T07`, `ET-41`) — discussion des durées légales ou des obligations de la Fondation, alors que l'énoncé donne les durées comme hypothèses.
- *Tout garder « au cas où »* — option 1 ou 3 retenue sans examiner la limitation de la conservation ni la destruction des dossiers anciens.
- *Hors du sujet* — choix d'un hébergeur ou souveraineté des données, que la question exclut.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | principes de finalité, de minimisation, d'exactitude, de limitation de la conservation, d'intégrité et de confidentialité (repères de l'annexe 2.5) | `rgpd` / F15 § 0 | en vigueur |
| Proposition « omnibus numérique » du 19/11/2025 | non applicable | `omnibus_numerique_donnees` | projet |
| Loi n° 78-17 du 6 janvier 1978, modifiée en 2018 | complément du RGPD en droit français, cité par l'annexe 2.5 | `loi_informatique_libertes` | en vigueur |
| Cycle de vie des données, archivage, suppression | définitions et étapes | F07 § 8.4 | notion de cours |
