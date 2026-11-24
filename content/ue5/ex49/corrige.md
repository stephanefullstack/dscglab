# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 49 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique (§ 3, planification et portefeuille ; § 4, organisation de la DSI, rôle et relations du DSI), F02 gouvernance et référentiels (§ 1, norme, référentiel et solution ; § 5, ITIL ; § 6, comitologie), F03 architecture et urbanisation (§ 1 et § 2, cartographies ; § 3, intégration), F04 relations avec les ESN et contrats (§ 3, niveaux de service ; § 4, clauses critiques), F06 gestion des connaissances (§ 1, connaissances tacites et explicites ; § 2, dispositif, gouvernance et appropriation), F13 intelligence artificielle (§ 1, typologie ; § 3, risques ; § 4, gouvernance), F15 RGPD opérationnel (§ 5, sous-traitance), glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Les orientations de la stratégie du système d'information et le portefeuille de projets | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.c` Méthodologies de planification stratégique du SI | 3,5 |
| 1.2 L'organisation de la fonction système d'information | `1.2.b` Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 3 |
| 1.3 La cartographie applicative et l'extraction automatique des documents d'arrivage | `1.3.b` Cartographie applicative et fonctionnelle des SI ; `1.3.d` Fonctionnement et usages des technologies émergentes : blockchain, registres distribués, IA, … | 2,5 |
| 1.4 Le partage des bonnes pratiques avec les entreprises installées | `1.6.a` Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle ; `1.6.d` Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums ; `1.6.c` Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) ; `1.6.e` Leviers d'appropriation et de transformation des pratiques professionnelles | 3 |
| 1.5 Les niveaux de service du contrat d'infogérance | `1.4.a` Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques ; `1.4.c` Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD | 2 |
| **Dossier 1 – Préparer la stratégie et l'organisation du système d'information** |  | **14** |

Répartition indicative : connaissances (planification stratégique et portefeuille, modèles d'organisation, cartographies, apprentissage automatique, gestion des connaissances, niveaux de service) environ 2,5 points (items 1.1 a-1, 1.2 a-1, 1.3 a-1, 1.3 b-1 pour moitié, 1.4 a-1, 1.5 a-1 pour moitié) ; analyse des annexes et recommandations environ 11,5 points, soit environ 82 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – Les orientations de la stratégie du système d'information et le portefeuille de projets (3,5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.c` « Méthodologies de planification stratégique du SI ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 1.3 (six projets, enveloppe, conventions), 1.2 (témoignages), 1.4 (applications et échanges), 1.1 (plan, activité, dépenses du SI) et 1.5 à 1.7 pour les constats qui fondent les orientations.

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Planification stratégique du SI définie (traduction de la stratégie en orientations pluriannuelles du SI, cible, projets priorisés, moyens, révision) et gestion d'un portefeuille de projets définie (ensemble des projets arbitré comme un tout par la valeur, le risque, le coût et les ressources, sous une enveloppe, avec des décisions de lancer, différer ou abandonner) | 0,5 |
| a-2 | Deux orientations de la stratégie du SI, chacune justifiée par un objectif du plan et par un constat des annexes | 0,5 |
| a-3 | Troisième orientation, même exigence ; les orientations ne se réduisent ni à une liste de projets ni à un choix technique | 0,5 |
| b-1 | Grille de trois ou quatre critères définis, dont la contribution au plan et le risque du projet, avec une échelle de notation | 0,5 |
| b-2 | Grille appliquée aux six projets, avec des notes justifiées par l'annexe 1.3 (et non par le seul objectif invoqué par le demandeur) | 0,5 |
| b-3 | Sélection dans l'enveloppe de 900 k€ (total de tête) et ordre de lancement justifié par l'urgence, les dépendances et la capacité du service (deux projets à la fois) ; projets différés et motif | 0,5 |
| b-4 | Rôle du conseil d'administration : valide les orientations et l'enveloppe, approuve le portefeuille et les projets importants avant tout engagement, suit leur avancement chaque trimestre ; il n'arbitre pas le détail, que prépare la direction générale | 0,5 |

**Réponse attendue**

*1.1 a) – La planification stratégique du SI, le portefeuille et trois orientations*

La **planification stratégique du système d'information** est la démarche par laquelle la direction, avec les directions métiers et le service des systèmes d'information, traduit la stratégie de l'organisation en **orientations du SI** pour plusieurs années, en déduit une cible (applications, données, organisation, compétences, partenaires) et un ensemble de **projets priorisés**, avec leurs moyens, puis la révise périodiquement ; le schéma directeur en est la forme la plus complète (non demandée ici). La **gestion d'un portefeuille de projets** consiste à considérer l'ensemble des projets et des demandes **comme un tout** : on les compare selon des critères communs (contribution à la stratégie, risque, coût, ressources), sous une **enveloppe** et une capacité données, pour décider de les lancer, de les différer ou de les abandonner, puis on revoit ces décisions en comité. Chez BRÉVALIM, cette démarche n'existe pas : chaque direction décide seule de ses outils, et le conseil découvre les projets une fois engagés (annexe 1.2) (0,5 pt).

**Trois orientations** (0,5 pt pour deux orientations, 0,5 pt pour la troisième ; trois parmi les suivantes) :

| Orientation | Constats des annexes | Objectif du plan servi |
|---|---|---|
| **Construire un socle de gestion unique des entreprises installées et des acheteurs**, qui partage leurs données de référence et échange automatiquement avec la facturation, la comptabilité et les outils d'exploitation, au lieu des ressaisies | logiciel de gestion de 2011, plus maintenu après 2029 (annexe 1.3) ; cartes d'acheteur et consommations de froid ressaisies pour être facturées (annexe 1.4) ; 0,8 M€ sur 1,3 M€ engagés par les directions hors du service des systèmes d'information (annexe 1.2) | fiabiliser la facturation et le pilotage |
| **Faire du portail des entreprises installées le point d'entrée unique de la relation** : factures, demandes techniques suivies, consignes du marché, accessible sur téléphone et dans les pavillons | 90 entreprises sur 240 ont un compte ; factures papier ; demandes imprimées, ressaisies et réponse par courrier (annexes 1.2 et 1.4) | dématérialiser d'ici 2029 toute la relation avec les entreprises installées et les acheteurs |
| **Mesurer à la source les flux du marché** utiles au plan : origine et tonnage des produits, déchets par entreprise, au lieu de saisies et de recopies tardives | documents d'arrivage saisis à la main, données complètes six semaines après le mois (annexe 1.5) ; pont-bascule relié à rien, totaux recopiés dans un tableur (annexe 1.4) | porter de 30 % à 40 % la part des produits régionaux ; valoriser 80 % des déchets en 2031 |
| **Gouverner le SI comme un ensemble et sécuriser son exploitation, de jour comme de nuit** : décisions partagées entre directions, service des systèmes d'information associé à tout choix, niveaux de service adaptés à l'activité de nuit, données protégées chez les prestataires | personne au service après 18 heures ; 14 incidents de nuit en 2026 ; sauvegardes chez un prestataire inconnu ; aucune clause sur les données (annexes 1.2 et 1.7) | garantir la sûreté du site et la sécurité des données |

*1.1 b) – La grille d'arbitrage et le portefeuille 2027-2029*

**Grille d'arbitrage** (0,5 pt), chaque critère noté de 1 (faible) à 3 (fort) :
- **contribution au plan** : nombre et poids des objectifs servis, au-delà de celui que le demandeur invoque ;
- **urgence** : risque de ne pas faire (fin de maintenance, saturation, échéance du plan) ;
- **risque du projet** (noté à l'envers : 3 = risque faible) : complexité, dépendances, adhésion des tiers, qualité de l'outil ;
- **coût au regard de l'enveloppe** (noté à l'envers : 3 = coût faible) et charge pour le service des systèmes d'information.

**Application aux six projets** (0,5 pt) :

| Projet | Contribution au plan | Urgence | Risque (3 = faible) | Coût (3 = faible) | Décision |
|---|---|---|---|---|---|
| P1. Logiciel de gestion du marché (450 k€, 18 mois) | 3 : facturation et pilotage, socle du portail, préalable à P2 | 3 : fin de maintenance à la fin de 2029, 18 mois de projet | 1 : projet long, cœur de l'activité, reprise des contrats | 1 | **retenu, lancé en premier** |
| P2. Application des acheteurs (250 k€, 12 mois) | 2 : relation avec les acheteurs | 1 | 1 : dépend de P1 ; 25 grossistes sur 150 prêts | 2 | **différé** |
| P3. Extraction des documents d'arrivage (120 k€, 6 mois) | 3 : origine des produits, pilotage, deux personnes libérées de la saisie | 2 : données à six semaines | 2 : outil déjà utilisé, mais documents manuscrits mal lus | 3 | **retenu, lancé en premier** |
| P4. Renouvellement du péage (600 k€, 12 mois) | 1 : sûreté invoquée, mais le système fonctionne | 1 : maintenu jusqu'en 2031 | 2 | 1 : deux tiers de l'enveloppe | **différé** |
| P5. Wifi du site (150 k€, 6 mois) | 2 : accès au portail dans les pavillons, fiabilité des tablettes des placiers | 2 : réseau mobile saturé certaines nuits | 3 : aucune dépendance | 3 | **retenu** |
| P6. Suivi des déchets par entreprise (180 k€, 9 mois) | 2 : déchets valorisés, données par entreprise | 2 : échéance de 2031, il faut mesurer avant d'agir | 2 : raccordement du pont-bascule | 2 | **retenu** |

P1 est un projet de maintien en condition (fin de maintenance à la fin de 2029) : il est retenu d'office, quelle que soit sa note ; la grille départage les autres projets.

**Sélection et ordre** (0,5 pt). Les projets demandés coûtent 1 750 k€ pour 900 k€ disponibles. Le portefeuille retenu tient dans l'enveloppe : 450 + 120 + 150 + 180 = 900 k€ (P1, P3, P5, P6) ; 850 k€ sont différés (P2, P4). Ordre de lancement, avec au plus deux projets à la fois :
1. **septembre 2027 : P1 et P3**. P1 d'abord, parce qu'il est le plus urgent et le plus structurant : lancé en septembre 2027, il s'achève en février 2029, avant la fin de la maintenance ; P3 en parallèle, parce qu'il est court, peu coûteux, sans dépendance, et donne vite des résultats sur l'objectif des produits régionaux ;
2. **mars 2028 : P5**, une fois P3 achevé : il prépare l'usage du portail dans les pavillons et fiabilise les tablettes des placiers ;
3. **septembre 2028 : P6**, après P5, pour un achèvement au printemps 2029.

**Projets différés** : P2 dépend de P1 ; lancé au mieux en mars 2029, il ne s'achèverait qu'en février 2030, et la plupart des grossistes ne sont pas prêts : il est préparé avec l'Union des grossistes pendant P1. P4 est demandé au nom de la sûreté, mais le système fonctionne et reste maintenu jusqu'en 2031 ; il absorberait les deux tiers de l'enveloppe : il est réexaminé en 2029 pour 2030-2031.

**Rôle du conseil d'administration** (0,5 pt). Le conseil, qui a adopté le plan, n'arbitre pas projet par projet : la direction générale instruit les demandes et prépare l'arbitrage avec un comité du SI (question 1.2). Le conseil **valide les orientations du SI et l'enveloppe** de 900 k€ sur trois ans, **approuve le portefeuille**, et en particulier les projets les plus importants, comme P1, **avant tout engagement** ; il **suit l'avancement** des projets dans le compte rendu trimestriel aux actionnaires et décide des reports ou des réexamens (P4 en 2029). C'est la réponse au constat de son président : « le conseil ne voit jamais les projets du système d'information avant qu'ils soient engagés ».

**Réponses tolérées**
- Autres critères pertinents (dépendances, capacité du service, adhésion des entreprises), autre échelle, ou grille qualitative (fort, moyen, faible), si la contribution au plan et le risque y figurent et si l'application est justifiée par l'annexe 1.3.
- Portefeuille comprenant P1 et P2 (P1 + P3 + P2, 820 k€ ; P1 + P2 + P5, 850 k€ ; P1 + P2 + P6, 880 k€), si le candidat montre qu'il tient dans l'enveloppe et assume l'achèvement de P2 en 2030 ; tout portefeuille qui écarte P1 n'est pas accepté, faute de solution à la fin de la maintenance.
- P5 ou P6 différé au profit d'une réserve pour imprévus, si le choix est justifié.
- Lancement de P5 avant P3, si l'ordre respecte la règle des deux projets à la fois et est justifié.
- Orientation sur l'ouverture des données des flux à la métropole : acceptée comme orientation si elle est justifiée par le plan et la demande de Brévaline Métropole, sans en détailler la gouvernance.

**Erreurs fréquentes**
- *Orientations réduites à une liste de projets ou à des choix techniques* (`JUR-G02` alignement réduit à un choix technique ou à une standardisation logicielle ; ET-06) — « acheter un nouveau logiciel de gestion » n'est pas une orientation : l'orientation dit ce que le SI doit permettre au plan.
- *Projets retenus selon l'objectif invoqué par le demandeur* (`JUR-T03` analyser et argumenter) — chaque demandeur rattache son projet au plan ; la grille sert précisément à comparer.
- *Enveloppe dépassée ou ignorée, ou dépendance de P2 à P1 oubliée* (`JUR-T08` exploiter toutes les annexes) — la limite, la date de démarrage et la capacité du service sont données.
- *Conseil d'administration chargé de choisir les outils, ou absent de l'arbitrage* (`JUR-T07` répondre à la seule question posée) — il fixe le cadre, approuve et suit ; il ne gère pas.
- *Schéma directeur, feuille de route complète ou calcul de rentabilité construits* (`JUR-T07`) — non demandés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Planification stratégique du SI et portefeuille de projets | orientations déduites de la stratégie ; arbitrage par la valeur, le risque et le coût | F01 § 3.1 et § 3.2 ; `erreurs_types.md` ET-06 et ET-07 | notion de cours |
| Comitologie du SI | comité d'arbitrage du portefeuille | F02 § 6 | notion de cours |

---

### 1.2 – L'organisation de la fonction système d'information (3 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.b` « Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ».

**Annexes mobilisées** : annexes 1.1 (organigramme, effectif, dépenses du SI), 1.2 (témoignages), 1.3 (demandeurs des projets) et 1.7 (infogérance).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Quatre modèles présentés (centralisée, décentralisée, fédérée, externalisée), chacun avec son principe, une force et une limite | 0,5 |
| a-2 | Organisation actuelle qualifiée : service unique en apparence, rattaché à la direction administrative et financière et cantonné au support, mais décisions et dépenses décentralisées dans les directions ; infogérance non pilotée ; rattachement ambigu (le (la) directeur(rice) général(e) délégué(e) est chargé(e) du SI) | 0,5 |
| a-3 | Effets tirés des annexes : applications qui ne se parlent pas, dépenses non maîtrisées (0,8 M€ hors du service), activité de nuit sans appui, conseil non informé, demandes sans priorité | 0,5 |
| a-4 | Modèle fédéré recommandé et justifié (service central pour la gouvernance, l'architecture, les contrats et la sécurité ; référents dans les directions), et rattachement au (à la) directeur(rice) général(e) délégué(e) chargé(e) du SI, membre de la direction générale, plutôt qu'à la direction administrative et financière | 0,5 |
| b-1 | Deux mesures parmi les trois axes demandés, chacune reliée à un constat | 0,5 |
| b-2 | Troisième mesure, sur l'axe restant ; les trois axes (instances, rôle du responsable, information des actionnaires) sont couverts | 0,5 |

**Réponse attendue**

*1.2 a) – Les modèles d'organisation et la situation de BRÉVALIM*

**Les modèles d'organisation de la fonction SI** (0,5 pt) :

| Modèle | Principe | Force | Limite |
|---|---|---|---|
| **Centralisée** | une direction des systèmes d'information unique décide et opère pour toute l'organisation | cohérence, économies, sécurité homogène | éloignement des métiers, lenteur |
| **Décentralisée** | chaque direction ou entité choisit et gère ses outils | proximité, réactivité | redondances, applications qui ne communiquent pas, sécurité inégale |
| **Fédérée** | un service central fixe les règles communes (gouvernance, architecture, référentiels, contrats, sécurité) ; des correspondants dans les directions portent les besoins et administrent leurs outils dans ce cadre | équilibre entre cohérence et proximité | coordination à organiser, rôles à clarifier |
| **Externalisée** | tout ou partie du SI confié à des prestataires (infogérance) | compétences, coûts variables | dépendance, perte de maîtrise si le client ne pilote pas |

**L'organisation actuelle** (0,5 pt). En apparence, BRÉVALIM a une organisation **centralisée** : un service unique de sept personnes. En réalité, elle est **décentralisée** : la direction de l'exploitation a choisi le péage (2019), la direction technique la supervision du froid (2025), et 0,8 M€ des 1,3 M€ de dépenses du SI sont engagés directement par les directions ; Mme DUCHÉRAN déclare : « je ne vais pas attendre l'informatique ». Le service des systèmes d'information, rattaché à la direction administrative et financière, est cantonné au **support** (« Nous passons nos journées à dépanner et à installer »), apprend les projets par les factures et reçoit des demandes par courriel, sans priorité. L'exploitation des serveurs est **externalisée** depuis 2024, sans pilotage réel (annexe 1.7). Le rattachement est en outre ambigu : depuis 2025, le (la) directeur(rice) général(e) délégué(e) est chargé(e) du système d'information, mais le service dépend toujours de la direction administrative et financière (annexe 1.1).

**Ses effets** (0,5 pt) :
- des applications choisies séparément **qui ne se parlent pas** : ressaisies des cartes et des consommations de froid, pont-bascule et badges isolés (annexe 1.4) ;
- des **dépenses et des risques non maîtrisés** : 0,8 M€ hors du service, serveurs du péage et des badges hors de l'infogérance, découverts « quand ils tombent en panne » ;
- une **activité de nuit sans appui** : personne au service après 18 heures, alors que le marché vit de minuit à 11 heures ;
- un **conseil d'administration non informé** : la supervision du froid (90 k€) ne lui a jamais été présentée ;
- aucun moyen d'arbitrer les demandes au regard du plan.

**Recommandation : un modèle fédéré, rattaché au (à la) directeur(rice) général(e) délégué(e)** (0,5 pt). Un **service central** (qui devient direction des systèmes d'information) fixe et garde les règles communes : orientations et portefeuille, architecture et référentiel unique des entreprises et des acheteurs, contrats et niveaux de service des prestataires (infogérance, fournisseurs du péage et du froid, agence web), sécurité et données. Dans chaque direction (exploitation, technique, commercial), un **référent** porte les besoins, administre les outils métiers dans ce cadre et assure le premier niveau d'aide la nuit. Ce modèle est préférable à une centralisation complète, hors de portée de sept personnes et trop éloignée d'une exploitation de nuit, et à la décentralisation actuelle, qui contredit les objectifs de dématérialisation, de fiabilité et de sécurité. Le service est **rattaché au (à la) directeur(rice) général(e) délégué(e) chargé(e) de l'exploitation et du SI**, membre de la direction générale, et non plus à la direction administrative et financière : le SI sert les cinq objectifs du plan et d'abord l'exploitation, principale utilisatrice ; un rattachement financier le réduit à un centre de coûts et de support.

*1.2 b) – Trois mesures pour les relations entre le service, la direction générale, les directions et le conseil*

(0,5 pt pour deux mesures, 0,5 pt pour la troisième ; une mesure par axe)
1. **Les instances : un comité du système d'information**, présidé par la directrice générale, réunissant chaque trimestre le (la) directeur(rice) général(e) délégué(e), les directeurs, la responsable commerciale, le responsable des systèmes d'information et, selon l'ordre du jour, la déléguée à la protection des données. Il arbitre le portefeuille (question 1.1), suit les projets et fixe une règle : **aucun outil ni aucun service numérique n'est acheté sans avis du service des systèmes d'information** (réponse au péage, à la supervision du froid et aux 0,8 M€ engagés par les directions).
2. **Le rôle du responsable des systèmes d'information : de « dépanneur » à partenaire des directions**. M. LAVEYRAC participe au comité de direction, est consulté avant tout choix d'outil, porte l'architecture, les contrats et la sécurité, et anime le réseau des référents des directions. Il publie un catalogue des services du SI avec leurs niveaux de service internes, y compris la nuit, et traite les demandes selon des priorités connues de tous, au lieu des courriels sans priorité.
3. **L'information des actionnaires** : présentation chaque année au conseil d'administration des orientations du SI et du portefeuille ; présentation au conseil, **avant engagement**, de tout projet au-delà d'un montant fixé par lui ; point d'avancement des projets du SI dans le compte rendu trimestriel aux actionnaires. Le président du conseil ne découvrira plus les dépenses une fois engagées.

**Réponses tolérées**
- Modèle centralisé renforcé recommandé, s'il est justifié par la taille de BRÉVALIM et assorti de correspondants dans les directions et d'une présence la nuit : accepté.
- Rattachement direct à la directrice générale : accepté, s'il est justifié par le poids du SI dans le plan et l'éloignement de la direction administrative et financière.
- Mention du modèle bimodal, à titre de comparaison, s'il n'est pas confondu avec un modèle « mi-interne, mi-externe ».
- Comité du SI ouvert à l'Union des grossistes, ou comité des usagers des entreprises installées, en plus des trois mesures demandées.
- Mesures qui confient à un administrateur le suivi du numérique, si l'information de l'ensemble du conseil est prévue.

**Erreurs fréquentes**
- *Organisation qualifiée de centralisée parce qu'il n'existe qu'un service* (`JUR-G05` analyser les déséquilibres organisationnels) — les choix et les dépenses sont faits par les directions.
- *Modèle fédéré confondu avec la décentralisation* (F01 § 8) — le modèle fédéré suppose des règles communes fixées par un service central.
- *Recommandation irréaliste* (`JUR-G05` recommander de façon réaliste) — une direction des systèmes d'information qui ferait tout, la nuit comme le jour, avec sept personnes.
- *Mesures sans lien avec les témoignages* (`JUR-T01` contextualiser chaque notion) — chaque mesure répond à un constat de l'annexe 1.2.
- *Tableau de bord du conseil construit* (`JUR-T07` répondre à la seule question posée) — l'information des actionnaires porte ici sur les projets du SI, pas sur le pilotage de l'activité.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèles d'organisation de la DSI | centralisée, décentralisée, fédérée, externalisée ; rattachement du DSI | F01 § 4 | notion de cours |
| Comitologie du SI | comité stratégique ou de gouvernance du SI | F02 § 6 | notion de cours |

---

### 1.3 – La cartographie applicative et l'extraction automatique des documents d'arrivage (2,5 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.b` « Cartographie applicative et fonctionnelle des SI » ; `1.3.d` « Fonctionnement et usages des technologies émergentes : blockchain, registres distribués, IA, … ». Limites : « Ne pas réduire l'urbanisation à une vision strictement technique : elle s'inscrit dans une stratégie globale. » ; « L'usage de l'IA doit notamment être analysé dans ses effets métiers et non uniquement comme outil technique. »

**Annexes mobilisées** : annexes 1.4 (applications et échanges), 1.5 (documents d'arrivage et outil proposé), 1.8 (repère sur le règlement sur l'intelligence artificielle) et 1.1 (système d'information).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cartographie fonctionnelle (fonctions groupées en domaines, indépendamment des logiciels) et cartographie applicative (applications, leurs utilisateurs et les flux entre elles) définies et distinguées | 0,5 |
| a-2 | Cartographie applicative représentée de façon lisible : neuf applications regroupées par domaine, échanges avec leur nature (fichier, ressaisie, impression, aucun) et leur fréquence, légende | 0,5 |
| a-3 | Trois faiblesses relevées, chacune avec son effet (ressaisies, applications isolées, absence de référentiel unique, échanges par fichiers et tableurs, hébergements dispersés hors de l'infogérance) | 0,5 |
| b-1 | Fonctionnement expliqué : apprentissage automatique supervisé sur des exemples saisis, prédiction des quatre données, indice de confiance, erreurs liées à la qualité et à la représentativité des exemples ; outil distingué de l'IA générative | 0,5 |
| b-2 | Deux conditions d'usage justifiées par l'annexe 1.5 : contrôle humain sous un seuil de confiance et par sondage, traitement des documents manuscrits, et à titre complémentaire mesure des erreurs, minimisation des données, essai sur les documents de BRÉVALIM | 0,5 |

**Réponse attendue**

*1.3 a) – Les cartographies et la cartographie applicative de BRÉVALIM*

La **cartographie fonctionnelle** représente les **fonctions** du système d'information (gérer les contrats, facturer, contrôler les accès, superviser le froid…), regroupées en **domaines** (zones et quartiers de l'urbanisation), indépendamment des logiciels qui les portent. La **cartographie applicative** représente les **applications** effectivement en place, leur périmètre, leurs utilisateurs et les **flux** entre elles (nature, sens, fréquence, mode : automatique ou manuel). Leur rapprochement montre quelles fonctions sont couvertes deux fois, mal couvertes ou reliées par des ressaisies (0,5 pt).

**Cartographie applicative de BRÉVALIM** (0,5 pt) :

| Domaine fonctionnel | Applications (hébergement) | Utilisateurs |
|---|---|---|
| Gestion du marché et facturation | logiciel de gestion du marché (serveurs du siège, infogérant) | service commercial, comptabilité, placiers sur tablette |
| Relation avec les entreprises installées | portail des entreprises (serveurs du siège) | 90 entreprises, surtout leurs dirigeants |
| Relation avec les acheteurs | application des acheteurs (hébergeur de l'agence web) | acheteurs, sur téléphone |
| Accès et sûreté | péage et contrôle d'accès (serveur propre, fournisseur) ; badges (serveur propre, poste de sûreté) | agents de péage ; agents de sûreté |
| Exploitation technique du site | supervision du froid (service en ligne) ; pont-bascule et suivi des déchets (poste dédié, tableur) | techniciens ; agents de la direction technique |
| Gestion interne et support | progiciel comptable et de paie (service en ligne) ; bureautique en ligne | finances, ressources humaines ; tous |

| N° | Émetteur → destinataire | Donnée | Nature (F fichier automatique ; R ressaisie ; I impression) | Fréquence |
|---|---|---|---|---|
| 1 | gestion du marché → progiciel comptable | factures | F | mensuelle |
| 2 | gestion du marché → portail des entreprises | factures en PDF | F | mensuelle |
| 3 | péage → application des acheteurs | cartes actives | F | chaque nuit |
| 4 | péage → gestion du marché | cartes créées, pour facturer les abonnements | R (service commercial) | au fil de l'eau |
| 5 | supervision du froid → gestion du marché | consommations de froid par cellule | R | mensuelle |
| 6 | portail → tableur des interventions (direction technique) | demandes techniques | I puis R ; réponse par courrier | au fil de l'eau |
| 7 | pont-bascule → tableur de suivi des déchets | totaux des pesées | R | mensuelle |
| 8 | tableurs de plannings → progiciel de paie | éléments variables des agents de nuit | R | mensuelle |
| — | badges | — | aucun échange | — |

Schéma possible (légende : ═ fichier automatique ; ┄ ressaisie ou impression ; ✕ aucun échange) :

```
[Péage] ══ cartes (nuit) ══> [Application des acheteurs]
   ┄┄ cartes ressaisies ┄┄> [Logiciel de gestion du marché] ══ factures (mois) ══> [Progiciel comptable]
[Supervision du froid] ┄┄ consommations ┄┄>        ║ ══ factures PDF (mois) ══> [Portail des entreprises]
                                                                                 ┄┄ demandes imprimées ┄┄> [Tableur des interventions]
[Pont-bascule] ┄┄ totaux ┄┄> [Tableur des déchets]        [Badges] ✕        [Plannings] ┄┄> [Paie]
```

**Trois faiblesses** (0,5 pt ; trois parmi les suivantes) :
- **Des ressaisies multiples** (flux 4 à 8) : cartes d'acheteur, consommations de froid, demandes, pesées, paie ; elles exposent à des erreurs la facturation des abonnements et la refacturation du froid (comprise dans les 5 M€ de refacturations de l'énergie, de l'eau et du froid), des délais et une charge de travail.
- **Des applications isolées** : badges, pont-bascule, supervision du froid n'échangent avec rien ; les données nécessaires au plan (déchets par entreprise, consommations) n'existent que dans des tableurs.
- **Aucun référentiel unique des entreprises et des acheteurs** : une même entreprise existe dans le logiciel de gestion, le portail, les badges ; une même carte dans le péage, l'application et le logiciel de gestion ; chacune est tenue séparément, avec des écarts inévitables.
- **Des échanges par fichiers périodiques et point à point, et des tableurs envoyés par courriel en guise de lien** : décalages (mensuels), fragilité, aucune supervision des échanges.
- **Des hébergements dispersés, hors de l'infogérance** : serveurs du péage et des badges, poste du pont-bascule, deux services en ligne, hébergeur de l'agence web ; personne n'a de vue d'ensemble de la sécurité ni de la continuité, en particulier la nuit.

*1.3 b) – Le fonctionnement de l'outil d'extraction et ses conditions d'usage*

**Fonctionnement** (0,5 pt). L'outil relève de l'**apprentissage automatique supervisé** : il **apprend** à partir d'exemples dont on connaît la bonne réponse, les 20 000 documents de 2025 et 2026 déjà saisis par le service commercial, à reconnaître où et sous quelle forme apparaissent le produit, l'origine, le poids et la date dans 25 formats différents. Sur un nouveau document, il **prédit** ces quatre valeurs ; il ne crée pas de contenu, à la différence d'une IA générative. Pour chaque valeur, l'**indice de confiance** exprime la probabilité, estimée par le modèle, que sa lecture soit juste : il est bas quand le document ressemble peu aux exemples appris (photo floue, format nouveau, écriture manuscrite). Les **erreurs** dépendent donc de la qualité et de la représentativité des exemples : 2 % des données extraites sont erronées sur les documents dactylographiés, mais 25 % sur les documents manuscrits, qui représentent environ un document sur cinq ; si les saisies passées contiennent des erreurs, l'outil les reproduit. Les corrections faites par les équipes peuvent servir à l'entraîner de nouveau. Effet métier : les deux personnes passent de la saisie à la vérification et au contrôle de cohérence, et les données sont disponibles bien avant les six semaines actuelles.

**Deux conditions d'usage** (0,5 pt ; deux parmi les suivantes) :
1. **Un contrôle humain sous un seuil de confiance** : toute donnée dont l'indice est inférieur au seuil (fixé après un essai, par exemple 90) est vérifiée par les deux personnes du service commercial ; les données au-dessus du seuil sont contrôlées par sondage chaque mois ; l'outil propose, l'agent valide ; les corrections sont réutilisées pour l'entraîner.
2. **Un traitement à part des documents manuscrits** : tant que leur taux d'erreur reste de cet ordre, ils sont saisis ou vérifiés en totalité à la main ; BRÉVALIM demande aux grossistes et à leurs transporteurs des documents dactylographiés ou électroniques.
3. **Un essai préalable sur les documents de BRÉVALIM** : les taux annoncés portent sur les documents d'autres clients ; un essai sur un mois de documents de 2026, comparé aux saisies, fixe le seuil et le taux d'erreur réel avant la généralisation ; ce taux est ensuite suivi chaque mois.
4. **La maîtrise des données** : ne pas extraire ni conserver les noms et numéros des chauffeurs, ni les prix d'achat des grossistes (données personnelles et commerciales sans utilité pour le besoin) ; contrat avec l'éditeur, qui héberge les documents et agit en sous-traitant au sens du RGPD ; formation des deux personnes à l'usage de l'outil (maîtrise de l'intelligence artificielle, annexe 1.8).

**Réponses tolérées**
- Cartographie présentée en schéma de blocs par domaine plutôt qu'en tableaux, si les neuf applications, les échanges et leur nature apparaissent avec une légende.
- Ajout à la cartographie du circuit actuel des documents d'arrivage (courriel puis tableur de saisie) : accepté.
- Autres domaines fonctionnels cohérents (par exemple « carreau des producteurs » distingué de la facturation).
- Indice de confiance présenté comme un score plutôt qu'une probabilité, si son usage (seuil, vérification) est compris.
- Mention de la reconnaissance optique de caractères comme première étape de la lecture : acceptée, si l'apprentissage à partir des saisies est expliqué.

**Erreurs fréquentes**
- *Cartographie applicative confondue avec un inventaire de serveurs, ou avec un modèle des données* (ET-20 urbanisation réduite à une vision technique ; `JUR-G07` cartographie et démarche d'urbanisation) — ce sont les applications, leurs domaines et leurs échanges qui sont demandés.
- *Schéma sans légende ni nature des échanges* (`JUR-T10` schémas et tableaux lisibles) — la distinction entre fichier automatique et ressaisie est le cœur de l'analyse.
- *Outil présenté comme une IA générative ou un grand modèle de langage* (ET-09 IA générative confondue avec l'apprentissage automatique) — il prédit des valeurs à partir d'exemples étiquetés.
- *Gains sans limites, ou rejet de l'outil sans proposer de conditions* (ET-19 opportunités sans risques) — l'annexe donne à la fois le gain et les taux d'erreur.
- *Classification de l'outil au titre du règlement sur l'intelligence artificielle, ou fonctionnement mathématique détaillé* (`JUR-T07` répondre à la seule question posée) — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cartographies fonctionnelle et applicative | domaines, applications, flux, ruptures | F03 § 1 et § 2 | notion de cours |
| Apprentissage automatique et IA générative | apprentissage supervisé, prédiction, erreurs, contrôle humain | F13 § 1, § 3 et § 4 ; `erreurs_types.md` ET-09 | notion de cours |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | maîtrise de l'intelligence artificielle du personnel (annexe 1.8), en principe | `ai_act` ; `omnibus_numerique_ia` ; F13 § 5 | en vigueur ; application échelonnée |
| RGPD (règlement (UE) 2016/679) | éditeur sous-traitant, minimisation (condition complémentaire) | `rgpd` ; F15 § 5 | en vigueur |

---

### 1.4 – Le partage des bonnes pratiques avec les entreprises installées (3 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.a` « Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle » ; `1.6.d` « Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums » ; `1.6.c` « Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) » ; `1.6.e` « Leviers d'appropriation et de transformation des pratiques professionnelles ». Limites : « La gestion des connaissances dépasse la seule numérisation de l'information. » ; « Le pilotage nécessite une approche systémique : outils, processus, culture. »

**Annexes mobilisées** : annexes 1.6 (bonnes pratiques, incidents, personnes, outils), 1.2 (témoignage de la présidente de l'Union des grossistes), 1.3 (wifi du site), 1.4 (portail, application des acheteurs, tablettes) et 1.1 (entreprises installées, organigramme).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gestion des connaissances définie comme une démarche systémique (outils, processus, culture) ; connaissances tacites et explicites distinguées et illustrées par l'annexe 1.6 (savoir des agents de nuit ; règles écrites sur les affiches) | 0,5 |
| a-2 | Objectifs reliés aux incidents et au plan ; contenus partagés avec toutes les entreprises et contenus réservés à chacune (savoir-faire des grossistes, données de sa cellule), avec des droits d'accès séparés | 0,5 |
| b | Intégration aux outils existants : portail (point d'entrée, espace commun et espaces privés, version pour téléphone), application des acheteurs, tablettes des placiers, wifi du site ; accès sans ordinateur | 0,5 |
| c-1 | Gouvernance : sponsor, animateur, référents par domaine, relais dans les entreprises, Union des grossistes, service des systèmes d'information ; règles de validation et de mise à jour ; animation (retours d'expérience, campagnes) | 0,5 |
| c-2 | Deux indicateurs complets (formule, source, fréquence, cible, axe), reliés aux objectifs | 0,5 |
| d | Trois leviers d'appropriation adaptés à des salariés de nuit, sans ordinateur, qui parlent plusieurs langues | 0,5 |

**Réponse attendue**

*1.4 a) – La gestion des connaissances, les objectifs et les contenus du dispositif*

La **gestion des connaissances** est une démarche systémique, qui combine outils, processus et culture, pour identifier, formaliser, partager et faire réutiliser les connaissances utiles à l'action ; elle dépasse la mise en ligne de documents. Une **connaissance explicite** est formalisée et transmissible (les règles de tri ou de fermeture des cellules écrites sur les affiches) ; une **connaissance tacite** est incorporée dans les personnes et difficile à formaliser (les agents de nuit qui savent quelles portes ferment mal, comment relancer une borne du péage, quel transporteur arrive avant l'heure). Le dispositif doit faire passer le savoir tacite des agents en fiches partagées, et faire entrer les règles écrites dans les gestes des salariés. Il est ici **inter-organisationnel** : il relie BRÉVALIM à 240 entreprises indépendantes, dont certaines sont concurrentes (0,5 pt).

**Objectifs** (0,5 pt avec les contenus) :
- réduire les incidents liés aux pratiques : les 40 ruptures de froid dues aux portes ouvertes et les 300 bennes refusées (2,5 % des bennes collectées), au service de l'objectif de 80 % de déchets valorisés en 2031 ;
- appliquer partout les mêmes consignes, la nuit comme le jour, en particulier lors des pannes du péage (8 pannes traitées de façons différentes) et pour la sûreté ;
- rendre ces règles accessibles à chaque salarié, y compris aux nouveaux (un sur trois remplacé dans l'année), dans sa langue ;
- écrire et diffuser le savoir tacite des agents de nuit.

**Contenus** :

| Contenus partagés avec toutes les entreprises | Contenus réservés à chaque entreprise |
|---|---|
| règles d'usage du site : chaîne du froid dans les cellules, tri des cinq bennes, sûreté de nuit, consignes en cas de panne du péage ; fiches tirées du savoir des agents de nuit ; retours d'expérience des incidents, rendus anonymes ; contacts et numéros d'urgence | savoir-faire propres que les grossistes ne veulent pas partager (mûrissage, conservation des produits de la mer, préparation des commandes) ; consignes de sa cellule et de ses cases ; ses incidents de froid et ses bennes refusées ; ses demandes techniques |

Chaque entreprise dispose d'un **espace privé** : elle seule y accède et le gère, avec ses référents ; BRÉVALIM n'y intervient que pour l'administration de l'outil ; aucun contenu d'un grossiste n'est visible par un concurrent.

*1.4 b) – L'intégration aux outils existants*

(0,5 pt)
- **Le portail des entreprises installées**, point d'entrée unique : une base de fiches pratiques, de type wiki, avec un espace commun et des espaces privés ; une version consultable sur téléphone ; des comptes ouverts aux chefs d'équipe et non plus aux seuls dirigeants, au-delà des 90 entreprises qui ont un compte.
- **Des codes à flasher** sur la porte de chaque cellule, sur chaque benne et à chaque borne du péage, qui ouvrent sur téléphone la fiche du lieu, sans compte pour les fiches communes ; le wifi du site (P5) permet de les consulter dans les pavillons.
- **L'application des acheteurs**, pour les consignes qui les concernent : tri des cartons qu'ils laissent, conduite à tenir en cas de panne du péage, horaires.
- **Les tablettes des placiers**, pour les consignes internes de la nuit (panne du péage, carreau) et pour **signaler** une mauvaise pratique ou proposer une fiche : c'est le canal par lequel le savoir des agents de nuit est recueilli.
- Le lien avec les outils d'exploitation peut suivre : une alarme de température de la supervision du froid renvoie à la fiche « portes et rideaux », adressée au référent de l'entreprise.

*1.4 c) – La gouvernance et les indicateurs*

**Rôles et animation** (0,5 pt) :
- **sponsor** : le (la) directeur(rice) général(e) délégué(e), qui porte le dispositif devant les entreprises et le relie au plan ;
- **animatrice** : Mme QUÉRINEL, responsable commerciale et des relations avec les entreprises, interlocutrice naturelle des entreprises ;
- **référents par domaine**, propriétaires des contenus : froid et déchets (direction technique, M. PERRAGUÈS), sûreté et péage (direction de l'exploitation, Mme DUCHÉRAN) ; ils valident chaque fiche et la revoient chaque année et après chaque incident ;
- **relais dans les entreprises** : un chef d'équipe par entreprise, qui diffuse les fiches et fait remonter les pratiques ;
- **Union des grossistes** : associée au comité éditorial trimestriel, ce qui donne au dispositif sa légitimité auprès des entreprises ;
- **service des systèmes d'information** : outils, droits d'accès des espaces privés, sécurité ; avis de la déléguée à la protection des données pour les vidéos et les contacts ;
- **animation** : retour d'expérience diffusé après chaque incident, campagne thématique chaque mois (froid avant l'été, tri avant les fêtes), réunion des relais en fin de marché, accueil des nouveaux salariés des entreprises.

**Deux indicateurs** (0,5 pt ; deux parmi les suivants) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des entreprises installées qui consultent les fiches | entreprises installées dont au moins un compte du portail a consulté une fiche dans le trimestre / 240 entreprises installées × 100 | statistiques de connexion du portail des entreprises installées (les consultations anonymes par code à flasher sont suivies à part, par lieu) | trimestrielle | au moins 75 % à la fin de 2028 | apprentissage |
| Taux de bennes refusées pour mauvais tri | bennes refusées par le prestataire de collecte / bennes collectées × 100 | pont-bascule et bordereaux du prestataire de collecte | mensuelle | au plus 1 % à la fin de 2028 (2,5 % en 2026) | environnement |
| Nombre de ruptures de froid dues à une porte laissée ouverte | nombre de ruptures de froid dont la cause enregistrée est une porte laissée ouverte, sur le trimestre | alarmes de la supervision du froid et fiches d'intervention de la direction technique | trimestrielle | au plus 3 par trimestre en 2028 (40 en 2026) | processus |

*1.4 d) – Trois leviers d'appropriation*

(0,5 pt ; trois parmi les suivants)
1. **Des formats sans ordinateur et sans barrière de langue** : pictogrammes, vidéos d'une minute sans parole ou sous-titrées, fiches courtes traduites dans les principales langues du marché, consultées sur téléphone à l'endroit du geste (porte de cellule, benne, borne).
2. **L'intégration au travail de nuit** : une « minute consigne » en début de nuit par les chefs d'équipe ; un parcours d'accueil de quelques minutes pour tout nouveau salarié à son arrivée sur le site ; un tutorat par les agents de nuit, qui transmettent leur savoir sur le terrain (socialisation) avant de l'écrire.
3. **Des relais et de la reconnaissance** : des chefs d'équipe formés et reconnus comme relais ; l'Union des grossistes qui porte le dispositif ; la publication des résultats (ruptures de froid, bennes refusées) par pavillon ; la valorisation des entreprises et des salariés qui proposent des fiches.
4. **La simplicité d'accès** : fiches communes sans identifiant, wifi dans les pavillons, une seule adresse pour tout trouver.

**Réponses tolérées**
- Modèle SECI de Nonaka et Takeuchi mobilisé pour structurer le dispositif (socialisation par le tutorat, externalisation des savoirs des agents, combinaison dans la base de fiches, internalisation par la pratique), s'il est appliqué au cas.
- Autres indicateurs complets (fraîcheur des fiches, nombre de fiches proposées par les entreprises, part des nouveaux salariés accueillis), s'ils sont reliés aux objectifs.
- Responsable du dispositif choisi à la direction technique, si la relation avec les entreprises est assurée par le service commercial.
- Modèle ADKAR (Prosci), ou huit étapes de la conduite du changement de Kotter, mobilisés pour les leviers, s'ils sont appliqués aux salariés de nuit.
- Affiches papier conservées et complétées par les codes à flasher : accepté.

**Erreurs fréquentes**
- *Gestion des connaissances réduite à une base documentaire ou au portail* (ET-21 gestion des connaissances confondue avec la GED ; limite du programme 1.6) — sans relais, animation et formats adaptés, le portail actuel touche les seuls dirigeants.
- *Savoir-faire des grossistes mis en commun* (`JUR-T08` exploiter toutes les annexes) — l'annexe 1.6 l'interdit : la séparation des contenus est une exigence du dispositif.
- *Modèle SECI récité sans application* (`JUR-T01` contextualiser chaque notion, pas de morceau de cours) — seuls ses usages dans le cas rapportent des points.
- *Indicateurs incomplets ou génériques* (ET-18 indicateurs génériques) — formule, source, fréquence, cible et axe sont exigés.
- *Leviers pensés pour des salariés de bureau* (formation en ligne, lettre par courriel) (`JUR-P04` conduite du changement adaptée) — les salariés visés travaillent la nuit, sans ordinateur, et parlent plusieurs langues.
- *Dispositif traité comme une gestion des compétences des salariés* (limite du programme 1.6) — le lien est complémentaire mais distinct.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gestion des connaissances | tacite et explicite ; dispositif, gouvernance, indicateurs, appropriation | F06 § 1 et § 2 ; `erreurs_types.md` ET-21 | notion de cours |
| Modèle SECI (Nonaka et Takeuchi, 1995) | quatre modes de conversion (réponse tolérée) | `nonaka_takeuchi_seci` ; F06 § 1 | publié |
| ADKAR (Prosci) ; huit étapes de Kotter (1995-1996) | conduite du changement (réponse tolérée) | `adkar` ; `kotter_8_etapes` ; F05 | publié |

---

### 1.5 – Les niveaux de service du contrat d'infogérance (2 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.a` « Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques » ; `1.4.c` « Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD ». Limite : « L'analyse juridique approfondie relève du droit des contrats informatiques et est exclue du programme de l'UE. »

**Annexes mobilisées** : annexes 1.7 (extraits du contrat et note du responsable des systèmes d'information), 1.8 (ITIL, RGPD) et 1.1 (horaires de l'activité, système d'information).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Accord de niveau de service défini (engagement contractuel mesurable, méthode de mesure, suivi, conséquences) ; inadéquation démontrée par les annexes : plage et astreinte de jour, prise en charge en heures ouvrées sans délai de rétablissement, disponibilité mesurée hors des heures du marché, aucune pénalité, rapport annuel « sans manquement » malgré six nuits sur papier | 0,5 |
| a-2 | Trois niveaux de service chiffrés et adaptés à l'activité de nuit, parmi la plage de service, le délai de rétablissement, l'astreinte et la mesure de la disponibilité | 0,5 |
| b-1 | Clause de sous-traitance des données personnelles : infogérant sous-traitant, BRÉVALIM responsable du traitement ; instructions, sécurité, sort des données ; recours au prestataire des sauvegardes soumis à l'autorisation écrite préalable de BRÉVALIM, avec les mêmes obligations | 0,5 |
| b-2 | Clause de confidentialité des données commerciales des grossistes : usage limité à la prestation, accès restreints et tracés, extension au prestataire des sauvegardes, durée au-delà du contrat, restitution ou destruction | 0,5 |

**Réponse attendue**

*1.5 a) – L'adéquation des niveaux de service et trois niveaux à inscrire*

Un **accord de niveau de service** (SLA) est l'engagement contractuel du prestataire envers son client sur des **niveaux mesurables** (plage de service, délais de prise en charge et de rétablissement, disponibilité), avec une **méthode de mesure**, un **suivi** périodique et des **conséquences** en cas de manquement, comme des pénalités. ITIL, référentiel de bonnes pratiques et non norme, en fait un outil de gestion des niveaux de service (0,5 pt avec l'analyse).

**Un contrat conçu pour des heures de bureau, face à un marché de nuit** :
- **plage de service et astreinte** : du lundi au vendredi de 8 heures à 18 heures, astreinte jusqu'à 20 heures ; or le marché vit six nuits sur sept, de minuit (placiers) à 11 heures, samedi compris : les heures critiques, de minuit à 8 heures, et tout le samedi sont hors contrat ;
- **délai** : la prise en charge en quatre heures ouvrées, sans délai de rétablissement, signifie qu'une panne à 3 heures peut n'être traitée qu'à midi, après la fin du marché ; en 2026, six nuits, les tablettes des placiers ont perdu l'accès au logiciel, le carreau a été attribué sur papier et le service n'a été rétabli que vers 11 heures, huit heures après ; les pannes du samedi n'ont été traitées que le lundi ;
- **mesure de la disponibilité** : 99 % mesurés sur la plage de service, par l'infogérant lui-même ; les incidents de nuit n'entrent pas dans la mesure : le rapport affiche 99,9 % et conclut qu'« aucun engagement n'a été manqué », alors que le service a manqué quand il était nécessaire ;
- **suivi** : un rapport annuel et aucune pénalité ne donnent à BRÉVALIM aucun moyen de pilotage.

Le contrat est respecté, mais il ne couvre pas le besoin.

**Trois niveaux de service à inscrire au renouvellement** (0,5 pt ; trois parmi les suivants) :

| Niveau de service | Engagement proposé | Constat auquel il répond |
|---|---|---|
| **Plage de service** | du lundi au samedi, de minuit à 18 heures, soit les heures du marché et les heures de bureau | incidents de minuit à 8 heures et du samedi hors contrat |
| **Délai de rétablissement** selon la priorité | priorité 1 (logiciel de gestion inaccessible aux tablettes des placiers ou à la facturation pendant le marché) : prise en charge en 15 minutes, rétablissement en une heure au plus ; priorité 2 : quatre heures ; priorité 3 : jour ouvré suivant | six nuits de carreau sur papier, rétablissement huit heures après la panne |
| **Astreinte** | astreinte joignable et capable d'intervenir à distance de minuit à 8 heures les nuits d'activité et le samedi, avec intervention sur site possible dans l'heure | aucune astreinte la nuit ni le samedi ; personne au service après 18 heures |
| **Mesure de la disponibilité** | au moins 99,5 % chaque mois, mesurés sur les heures d'activité du marché (minuit à 11 heures, six jours sur sept), par une supervision dont BRÉVALIM voit les résultats ; rapport mensuel ; pénalités en cas de manquement | 99,9 % affichés sur une plage où le marché est fermé ; aucune pénalité, rapport annuel |

*1.5 b) – Deux clauses sur les données, en principe*

**La sous-traitance des données personnelles** (0,5 pt). L'infogérant administre des serveurs qui portent les nom, adresse et coordonnées des titulaires des cartes d'acheteur et les contacts des entreprises installées : il traite des données personnelles pour le compte de BRÉVALIM, qui reste **responsable du traitement** ; il agit en **sous-traitant** au sens du RGPD (annexe 1.8). Une clause, ou une annexe au contrat, fixe ses obligations : traitement sur les seules instructions écrites de BRÉVALIM, confidentialité de son personnel, mesures de sécurité, signalement sans délai de toute violation de données, assistance à BRÉVALIM, sort des données à la fin du contrat (restitution puis suppression), possibilité d'audit. **Le recours au prestataire des sauvegardes**, aujourd'hui inconnu, n'est possible qu'avec l'**autorisation écrite préalable** de BRÉVALIM ; son nom et le lieu de conservation sont communiqués, et les mêmes obligations lui sont imposées. La déléguée à la protection des données, Mme TALMONDIER, est associée à la rédaction.

**La confidentialité des données commerciales des grossistes** (0,5 pt). Les serveurs portent les contrats, les redevances et les factures de chaque entreprise installée, données sensibles entre concurrents. La clause engage l'infogérant à n'utiliser ces données que pour la prestation, à ne les communiquer à aucun tiers, à en limiter l'accès aux seules personnes qui en ont besoin, avec des accès tracés, à imposer la même obligation au prestataire des sauvegardes, à la maintenir après la fin du contrat et à restituer ou détruire les données à son terme.

**Réponses tolérées**
- Plage de service couvrant sept jours sur sept, si elle est justifiée par la préparation du marché ou l'exploitation du dimanche.
- Engagement de mise en place d'un mode de secours pour les placiers (attribution possible hors connexion, puis synchronisation), en plus des trois niveaux demandés.
- Valeurs différentes des engagements (délai de rétablissement de deux heures, disponibilité de 99 %), si elles sont justifiées par l'activité de nuit et mesurées sur les heures du marché.
- Mention de l'extension du périmètre au serveur du péage, ou de pénalités et d'un rapport mensuel comme quatrième niveau : valorisée.
- Mention de la localisation des sauvegardes dans l'Union européenne : acceptée.

**Erreurs fréquentes**
- *Contrat jugé satisfaisant au vu du rapport de l'infogérant* (`JUR-T03` analyser et argumenter) — la disponibilité est mesurée là où le marché est fermé.
- *Délai de prise en charge confondu avec le délai de rétablissement* (F04 § 3) — un incident pris en charge peut rester non résolu pendant tout le marché.
- *Niveaux de service non chiffrés ou sans mesure* (F04 § 7) — un niveau de service se mesure.
- *Infogérant présenté comme responsable du traitement, ou externalisation présentée comme un transfert de responsabilité* (`JUR-A05` externalisation, infogérance et contractualisation ; F04 § 7) — BRÉVALIM reste responsable.
- *Analyse juridique des clauses, ou procédure de choix d'un autre prestataire* (`JUR-T07` répondre à la seule question posée ; limite du programme 1.4) — non attendues : l'énoncé exclut toute procédure de choix.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ITIL 4 (PeopleCert, 2019) | gestion des niveaux de service et des incidents | `itil_4` ; F02 § 5 | en vigueur |
| ITIL (version 5) | coexiste avec ITIL 4 (annexe 1.8) | `itil_5` ; F02 § 5 | en vigueur |
| Niveaux de service et clauses critiques | SLA, délais, astreinte, disponibilité, pénalités ; confidentialité, données personnelles, sous-traitance | F04 § 3 et § 4 ; `erreurs_types.md` ET-22 | notion de cours |
| RGPD (règlement (UE) 2016/679) | sous-traitant, contrat écrit, autorisation écrite préalable d'un autre sous-traitant (en principe) | `rgpd` ; F15 § 5 | en vigueur |
