# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 17

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Préparer la stratégie et l'organisation du système d'information | 14 | 1.1 à 1.5 | `exercices/ex49_portefeuille_cartographie_savoirs_infogerance` |
| 2 – Organiser et exploiter les données des acheteurs et des flux, revoir le pilotage | 13 | 2.1 à 2.4 | `exercices/ex50_donnees_peage_flux_tableau_bord` |
| 3 – Fiabiliser la facturation, maîtriser les accès, auditer le carreau et répondre aux demandes de données de durabilité | 13 | 3.1 à 3.4 | `exercices/ex51_facturation_acces_audit_carreau_durabilite` |
| **Total** | **40** | | |

---

## DOSSIER 1 – PRÉPARER LA STRATÉGIE ET L'ORGANISATION DU SYSTÈME D'INFORMATION (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES ACHETEURS ET DES FLUX, REVOIR LE PILOTAGE (13 points)

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

---

## DOSSIER 3 – FIABILISER LA FACTURATION, MAÎTRISER LES ACCÈS, AUDITER LE CARREAU ET RÉPONDRE AUX DEMANDES DE DONNÉES DE DURABILITÉ (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les risques et la fiabilisation de la facturation | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels | 3,5 |
| 3.2 La gestion des badges et des comptes | `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 3,5 |
| 3.3 L'audit de l'attribution des emplacements du carreau | `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 2 |
| 3.4 Les données de durabilité, l'affichage dynamique et la gouvernance responsable du système d'information | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.b` Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) ; `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété | 4 |
| **Dossier 3 – Fiabiliser la facturation, maîtriser les accès, auditer le carreau et répondre aux demandes de données de durabilité** |  | **13** |

Répartition indicative : connaissances (typologie des risques, fiabilisation, gestion des identités et des accès, audit d'un processus, état de durabilité, sobriété numérique) environ 3 points (items 3.1 a-1, 3.1 b-1, 3.2 a-1, 3.3 a-1, 3.4 a-1 et 3.4 b-1, chacun en partie appliqué au cas) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – Les risques et la fiabilisation de la facturation (3,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels ». Limites : la conformité financière et comptable n'est pas traitée en UE 5 ; aucune règle de facturation, aucun traitement comptable des avoirs ni aucune incidence chiffrée sur les comptes n'est attendu.

**Annexes mobilisées** : annexe 3.1 (chaîne de facturation, constats, échéance de septembre 2027, échelles), annexe 3.5 (facturation électronique) et annexe 1.1 (240 entreprises installées, chiffre d'affaires de 28 M€ dont 17 M€ de redevances et de loyers et 5 M€ de refacturations, logiciel de gestion du marché, portail, progiciel comptable).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée (cybermenaces et malveillance, y compris interne ; défaillances opérationnelles ; risques réglementaires ; risques métiers), avec les critères touchés (intégrité, traçabilité, disponibilité, confidentialité) | 0,5 |
| a-2 | Quatre risques formulés comme des événements redoutés, tirés de l'annexe 3.1 avec leur cause et leurs chiffres, et classés de façon justifiée | 0,5 |
| b-1 | Fiabilisation définie (exhaustivité, exactitude, réalité, traçabilité des données comptables et décisionnelles ; contrôles applicatifs et généraux, séparation des tâches, piste d'audit, rapprochements) | 0,5 |
| b-2 | Cinq points de contrôle de la chaîne, du contrat au chiffre d'affaires, chacun avec le risque traité, le contrôle, sa nature et son responsable | 0,5 |
| b-3 | Parmi eux, le rapprochement de l'occupation constatée et des contrats facturés, et un contrôle de l'interface ou du chiffre d'affaires (rejets corrigés à la source, écart de 900 k€ expliqué) | 0,5 |
| c-1 | Quatre risques cotés selon les échelles de l'annexe 3.1 D, de façon justifiée | 0,5 |
| c-2 | Deux actions prioritaires avant le 01/09/2027, justifiées par la probabilité et l'impact et reliées aux risques forts | 0,5 |

**Réponse attendue**

*3.1 a) – La typologie et les quatre risques*

**Typologie** (a-1) : les risques liés aux systèmes d'information se classent en quatre familles (F12 § 0 et § 5) :
- les **cybermenaces et actes malveillants**, externes ou internes : hameçonnage, compromission de comptes, fraude interne ;
- les **défaillances opérationnelles**, non intentionnelles : erreur de saisie, interface défaillante, procédure absente, panne ;
- les **risques réglementaires** : manquement à une obligation, ici l'émission des factures sous forme électronique à compter du 01/09/2027 (annexe 3.5) ;
- les **risques métiers** : effets sur l'activité et la stratégie, ici le chiffre d'affaires, la relation avec les entreprises installées et la confiance des actionnaires.

Chaque risque porte atteinte à un ou plusieurs critères : intégrité (exactitude et exhaustivité des données), traçabilité, disponibilité, confidentialité. Pour une chaîne de facturation, l'**intégrité** et la **traçabilité** sont les critères dominants.

**Risques de la chaîne de facturation** (a-2 ; quatre sont attendus, six sont proposés) :

| Risque (événement redouté) et cause | Famille | Critère touché |
|---|---|---|
| R1 – Une entreprise occupe une case ou une cellule sans contrat à jour, et elle n'est pas facturée ou l'est mal : les changements arrivent par téléphone ou par courriel, sans procédure ni rapprochement (15 cases ou cellules en février 2027, sur 60 changements en 2026 ; 150 k€ par an) | défaillance opérationnelle (processus) ; effet métier : perte de revenus, inégalité entre entreprises | intégrité (exhaustivité) |
| R2 – Des tarifs erronés sont facturés après la révision annuelle : saisie à la main, contrat par contrat, sans contrôle (20 contrats en janvier 2027) | défaillance opérationnelle (erreur humaine) ; effet métier : réclamations de l'Union des grossistes | intégrité (exactitude) |
| R3 – Un avoir injustifié, par erreur ou par fraude, annule une facture sans que personne le voie : les mêmes agents créent factures et avoirs, sans validation ni motif ; 18 personnes ont tous les droits ; aucune trace des modifications (300 avoirs, 400 k€ en 2026) | acte malveillant interne rendu possible par une défaillance du contrôle interne (séparation des tâches) ; effet métier : perte | intégrité, traçabilité |
| R4 – Le chiffre d'affaires présenté aux actionnaires est inexact et impossible à justifier : les lignes rejetées sont corrigées ou supprimées dans le seul progiciel comptable, sans liste ; aucun rapprochement entre les deux applications (480 lignes, 2 % ; écart de 900 k€, environ 4 % de 22 000 k€) | défaillance opérationnelle (intégrité de l'interface) ; risque métier : confiance des actionnaires, compte rendu trimestriel du plan | intégrité, traçabilité |
| R5 – À partir du 01/09/2027, des factures électroniques erronées partent en série vers les entreprises et la plateforme agréée : identifiant absent ou faux pour 30 entreprises (12,5 %), contrats non à jour, tarifs erronés ; « une facture fausse sera transmise telle quelle » | risque réglementaire (obligation d'émission électronique) ; effet métier : réclamations, avoirs en chaîne | intégrité |
| R6 – Des entreprises sont relancées à tort et contestent : relances préparées sur une extraction, sans rapprochement des avoirs et des paiements (25 entreprises en 2026) | défaillance opérationnelle ; effet métier : relation avec les entreprises installées | intégrité |

*3.1 b) – La fiabilisation et la cartographie des contrôles*

**Définition** (b-1) : **fiabiliser un système d'information comptable et décisionnel**, c'est garantir que les données qui vont de l'événement de gestion (ici, l'occupation d'un emplacement) jusqu'au chiffre présenté aux décideurs sont **exhaustives, exactes, réelles et traçables**. Le dispositif combine les **contrôles applicatifs** (à la saisie, au traitement, aux interfaces, en sortie), les **contrôles généraux** (gestion des accès et des modifications, exploitation), la **séparation des tâches** incompatibles (saisir, valider, annuler) et une **piste d'audit** qui permet de reconstituer le chemin d'un chiffre jusqu'à sa source, avec des **rapprochements** réguliers entre applications (F10 § 2 et § 3). Chez BRÉVALIM, la chaîne va du contrat d'emplacement au chiffre d'affaires du compte rendu trimestriel aux actionnaires ; elle se rompt aujourd'hui à chaque maillon.

**Cartographie des contrôles** (b-2 et b-3 ; cinq points de contrôle sont attendus, sept sont proposés) :

| Point de contrôle | Risque traité | Contrôle | Nature | Responsable |
|---|---|---|---|---|
| 1. Création ou modification d'un contrat (changement de case) | R1, R3 | toute modification passe par une demande écrite, enregistrée, validée par la responsable commerciale avant saisie ; journal des modifications des contrats (auteur, date, valeur avant et après) demandé à l'éditeur ; droits de modification limités au service commercial | préventif, manuel et automatisé | service commercial (Mme QUÉRINEL) |
| 2. **Rapprochement de l'occupation constatée et des contrats facturés** | R1 | chaque trimestre, relevé des cases, bureaux et cellules effectivement occupés (placiers, agents de sûreté, direction technique pour les cellules), rapproché de la liste des contrats facturés ; chaque écart régularisé dans le mois | détectif, manuel | service commercial avec la direction de l'exploitation ; revue par le directeur administratif et financier |
| 3. Révision annuelle des tarifs | R2 | tarifs saisis une fois dans une grille, appliqués par le logiciel à tous les contrats ; à défaut, état « avant / après » de chaque contrat contrôlé par une seconde personne avant l'émission de janvier, avec un contrôle de vraisemblance (hausse égale au taux de révision) | préventif, automatisé ; détectif, manuel | facturation, validé par la direction administrative et financière |
| 4. Avoirs | R3, R6 | motif obligatoire ; validation par une personne distincte de l'émetteur (comptable, puis directeur administratif et financier au-delà d'un montant) ; état mensuel des avoirs par auteur et par entreprise revu par le directeur administratif et financier | préventif et détectif | M. MORVÉLAN |
| 5. Fichier mensuel des écritures vers le progiciel comptable | R4 | totaux de contrôle (nombre de lignes, montant) comparés avant et après chargement ; liste des rejets conservée ; correction **dans le logiciel de gestion du marché**, puis nouvel envoi ; aucune correction directe en comptabilité | détectif, automatisé et manuel | comptabilité |
| 6. Chiffre d'affaires présenté aux actionnaires | R4 | rapprochement mensuel, rubrique par rubrique, du chiffre d'affaires du logiciel et de celui de la comptabilité ; écart expliqué et documenté avant chaque compte rendu trimestriel ; source et date du chiffre indiquées | détectif, manuel | directeur administratif et financier |
| 7. Données des entreprises et relances | R5, R6 | identifiant de l'entreprise vérifié à la création et après tout rachat ou changement de nom ; relances préparées après rapprochement des paiements et des avoirs | préventif ; détectif | service commercial ; comptabilité |

Ces contrôles supposent des **droits séparés** dans le logiciel : le service commercial gère les contrats, la facturation émet, un tiers valide les avoirs, personne n'a tous les droits (lien avec la question 3.2).

*3.1 c) – La cotation et les deux actions prioritaires*

**Cotation selon les échelles de l'annexe 3.1 D** (c-1) :

| Risque | Probabilité | Impact | Priorité |
|---|---|---|---|
| R3 – Avoir injustifié | **forte** : 300 avoirs par an, chaque mois, sans validation ; facile à provoquer | **fort** : 400 k€ d'avoirs émis en 2026 sans validation ni motif ; la part injustifiée est inconnue, et une perte de plus de 200 k€ ne peut pas être exclue | **oui** |
| R4 – Chiffre d'affaires inexact | **forte** : des rejets chaque mois, cause toujours là | **fort** : écart de 900 k€ ; chiffre d'affaires présenté aux actionnaires inexact | **oui** |
| R5 – Factures électroniques erronées en série | **forte** : quasi certaine dès le 01/09/2027 si rien ne change : 30 identifiants faux ou absents aujourd'hui, contrats et tarifs non fiables | **fort** : factures électroniques erronées en série, chaque mois, aux 240 entreprises | **oui** |
| R1 – Occupation sans contrat à jour | forte : 15 occupations sans contrat à jour en février 2027, pour 60 changements demandés en 2026 ; aucune procédure | moyen : 150 k€ par an | non, mais il alimente R5 |
| R2 – Tarifs erronés | moyenne : une fois par an, 20 contrats | moyen : réclamations | non |
| R6 – Relances à tort | moyenne | moyen : réclamations | non |

**Deux actions à mener avant le 01/09/2027** (c-2) :
1. **Fiabiliser les données de base avant la première facture électronique** (R5, et R1 et R2 qui l'alimentent) : corriger les identifiants des 30 entreprises ; rapprocher les 240 contrats de l'occupation réelle, par un relevé contradictoire avec les placiers et les entreprises ; vérifier les tarifs 2027 ; mettre en place la procédure écrite des changements d'emplacement (points 1, 2 et 7). C'est la seule priorité qui a une **date** : à partir de septembre, chaque erreur de données partira chaque mois, telle quelle, vers les 240 entreprises et la plateforme. La plateforme transmet les données, elle ne les corrige pas.
2. **Mettre sous contrôle les avoirs et le passage vers la comptabilité** (R3 et R4, probabilité et impact forts) : validation des avoirs par une personne distincte, avec motif ; correction des rejets à la source ; rapprochement mensuel du chiffre d'affaires (points 4, 5 et 6). Puisqu'une facture fausse sera transmise telle quelle (annexe 3.1 C), chaque erreur devra être corrigée après coup : un circuit d'avoirs sans contrôle deviendrait la principale faiblesse de la chaîne.

Ces deux actions précèdent l'outil : la version du logiciel livrée en juin ne fiabilise rien si les données et les droits restent en l'état.

**Réponses tolérées**
- Autre typologie (risques internes et externes, accidentels et intentionnels, ou par critère d'intégrité, de traçabilité, de disponibilité), si les quatre familles du programme apparaissent dans le classement ; R3 classé en défaillance du contrôle interne plutôt qu'en malveillance, si la possibilité de fraude est signalée.
- R1 coté fort en impact, au titre de l'inégalité entre entreprises installées et de son effet sur R5, et retenu dans une action prioritaire, si c'est justifié.
- R3 coté moyen en impact, si le candidat relève que la part injustifiée des 400 k€ est inconnue ; les deux actions prioritaires portent alors sur R4 et R5, et la validation des avoirs peut figurer dans l'action sur le passage vers la comptabilité.
- Deuxième action différente si elle traite un risque fort : traçabilité des modifications des contrats et des tarifs exigée de l'éditeur dans la version de juin ; séparation des droits dans le logiciel.
- Contrôles regroupés autrement (par étape : contrat, facture, écritures, encaissement, chiffre présenté), si le rapprochement de l'occupation et des contrats y figure et si chaque contrôle porte sa nature et son responsable.

**Erreurs fréquentes**
- *Typologie récitée sans application, ou risques réduits aux constats* (`JUR-T01`, `JUR-T07`) — juste : des événements redoutés, avec leur cause et leurs chiffres, classés puis cotés selon les échelles de l'annexe.
- *Facturation électronique présentée comme la solution aux erreurs* (`JUR-T03`) — juste : elle transmet des données structurées ; des données fausses deviennent des factures électroniques fausses.
- *Contrôles sans responsable ni nature, ou limités à « contrôler les factures »* (`JUR-T11`) — juste : un contrôle par maillon de la chaîne, du contrat au chiffre d'affaires, avec la séparation des tâches.
- *Plateforme agréée appelée de son ancien nom, ou calendrier ancien de la réforme* (`JUR-N02`) — juste : plateforme agréée ; émission par BRÉVALIM à compter du 01/09/2027 (annexe 3.5).
- *Règles de facturation, mentions obligatoires, TVA, traitement comptable des avoirs, catégorie d'entreprise à déterminer* — non attendus (UE 1 et UE 4 ; date donnée par l'annexe).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI, critères | cybermenaces, défaillances, risques réglementaires et métiers | F12 § 0, § 1 et § 5 | notion de cours |
| Fiabilisation, contrôles applicatifs et généraux, séparation des tâches, piste d'audit | du contrat au chiffre d'affaires | F10 § 2 et § 3 | notion de cours |
| Généralisation de la facturation électronique | réception depuis le 01/09/2026 ; émission par BRÉVALIM à compter du 01/09/2027 ; formats structurés | `facturation_electronique_fr` ; F10 § 3.4 | en vigueur ; émission par BRÉVALIM à compter du 01/09/2027 (annexe 3.5) |
| Plateformes agréées | transmission des factures | `facturation_electronique_pa` ; F10 § 3.4 | en vigueur |

---

### 3.2 – La gestion des badges et des comptes (3,5 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique des solutions de cybersécurité n'est pas exigée ; la sécurité est envisagée de façon systémique (organisationnelle, humaine) ; les normes se mobilisent sans entrer dans leur démarche de conformité formelle.

**Annexes mobilisées** : annexe 3.2 (badges par population, zones, comptes, incidents, points de vue), annexe 3.5 (ISO/IEC 27001:2022 et 27002:2022, RGPD en principe) et annexe 1.1 (organigramme, effectif, entreprises installées, badges et portail).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gestion des identités et des accès définie (cycle de vie, une identité par personne, moindre privilège, revue, traçabilité), pour les accès physiques et logiques | 0,5 |
| a-2 | Cycle de vie (arrivée, changement, départ) des salariés de BRÉVALIM et des saisonniers, à partir d'une source qui fait foi, avec une date de fin | 0,5 |
| a-3 | Cycle de vie des salariés des entreprises installées et des prestataires (référent, déclaration simple, expiration), réponse à l'objection de Mme GARBUSSAC ; traitement immédiat des quelque 500 badges de personnes parties | 0,5 |
| a-4 | Moindre privilège appliqué aux zones (cellules, locaux techniques) et aux comptes ; réponse à l'objection de Mme DUCHÉRAN | 0,5 |
| a-5 | Revue périodique des droits (fréquence, acteurs) et fin des comptes partagés du portail et des comptes génériques des tablettes | 0,5 |
| b-1 | Rôles de la direction générale, du responsable de la sûreté, du responsable des systèmes d'information et des directions métiers, distingués | 0,5 |
| b-2 | Rôles des entreprises installées et des prestataires (référent, signalement des départs, revue, usage) | 0,5 |

**Réponse attendue**

*3.2 a) – Le dispositif de gestion des badges et des comptes*

**Définition** (a-1) : la **gestion des identités et des accès** (IAM) organise, pour chaque personne, la **création** de son identité et de ses droits à l'arrivée, leur **modification** quand elle change de fonction et leur **révocation** à son départ. Elle repose sur quelques principes : une identité par personne (badges et comptes **nominatifs**), le **moindre privilège** (droits limités au besoin de la fonction, par profils), la **séparation des tâches**, la **revue périodique** des droits et la **traçabilité** des accès (F12 § 3). Elle distingue l'identification (déclarer qui l'on est), l'authentification (le prouver) et l'autorisation (les droits accordés). Ses mesures figurent parmi celles de l'annexe A d'ISO/IEC 27001:2022 (gestion des identités, contrôle d'accès, sécurité physique des locaux), détaillées par ISO/IEC 27002:2022 (annexe 3.5). Chez BRÉVALIM, elle doit couvrir **ensemble** les accès physiques (badges) et logiques (comptes), car ce sont les mêmes personnes et les mêmes départs non signalés : environ 500 badges sur 2 600, près d'un sur cinq, appartiennent à des personnes parties.

**Le cycle de vie des identités, par population** (a-2 et a-3) :

| Population | Arrivée | Changement | Départ |
|---|---|---|---|
| Salariés de BRÉVALIM (230 badges, 20 de personnes parties) | l'entrée dans la paie, déclarée par les ressources humaines, déclenche le badge et les comptes du profil du poste, prêts le premier jour | le manager demande le nouveau profil ; les anciens droits sont retirés le jour du changement | la sortie déclarée par les ressources humaines désactive badge et comptes le dernier jour ; le badge est rendu |
| Saisonniers d'été (80 badges, tous de personnes parties) | liste de la direction de l'exploitation ; badge et compte nominatifs **datés** du premier au dernier jour du contrat | changement de mission validé par la chef des placiers | **expiration automatique** à la fin du contrat : plus aucun badge actif en octobre |
| Salariés des entreprises installées (2 150 badges, environ 350 de personnes parties) | demande du **référent des accès** désigné par chaque entreprise, sur le portail plutôt que sur papier ; badge lié à l'entreprise et à ses zones, valable un an au plus | le référent modifie les zones (nouvelle cellule, autre pavillon) | le référent déclare le départ sur le portail sous 48 heures ; à défaut, un badge non utilisé pendant deux mois est suspendu, et chaque badge expire s'il n'est pas reconfirmé lors de la revue |
| Prestataires de nettoyage et de maintenance du froid (140 badges, environ 50 de personnes parties) | liste nominative des intervenants transmise par le prestataire et validée par la direction qui a commandé la prestation ; badge limité aux zones et aux plages de l'intervention, jusqu'à la fin du contrat | toute nouvelle zone est validée par la direction technique | le prestataire signale chaque départ ; les **10 badges sans nom sont supprimés** |

**Réponse à Mme GARBUSSAC** : il ne s'agit pas d'un formulaire à chaque départ, mais d'une déclaration en quelques clics sur le portail par un référent, complétée par l'expiration automatique et la suspension des badges inutilisés : le dispositif tient même si une entreprise oublie de déclarer. La rotation d'un salarié sur trois rend ce dispositif plus nécessaire, non moins.

**Mesure immédiate** : désactiver les 80 badges des saisonniers et les 20 des anciens salariés de BRÉVALIM, puis demander à chaque entreprise et à chaque prestataire de confirmer sa liste dans le mois, faute de quoi les badges non confirmés sont suspendus. Cinq des 12 vols de 2026 ont été commis avec le badge d'une personne partie.

**Le moindre privilège** (a-4) : chaque personne n'accède qu'aux zones et aux applications dont sa fonction a besoin, aux heures où elle en a besoin.

| Zone ou application | Accès proposé |
|---|---|
| Pavillons | salariés des entreprises installées dans le pavillon, agents de BRÉVALIM et prestataires concernés, aux heures d'activité ; hors de ces heures, sûreté et agents de nuit |
| Entrepôt frigorifique (quais, couloirs) | entreprises locataires de cellules, agents de nuit, techniciens et prestataire de maintenance du froid |
| Chacune des 40 cellules | les seuls salariés de l'entreprise locataire ; droit d'intervention nominatif des agents de nuit et des techniciens du froid, tracé et revu |
| Locaux techniques (salle des machines du froid, locaux électriques) | direction technique, prestataire de maintenance pendant ses interventions, agents de sûreté |
| Portail des entreprises installées | un compte par personne, avec un profil : factures pour le dirigeant et le comptable, demandes techniques pour les salariés concernés |
| Logiciel de gestion du marché | profils séparés : contrats, facturation, validation des avoirs, attribution du carreau (lien avec la question 3.1) |

**Réponse à Mme DUCHÉRAN** : le moindre privilège n'empêche pas d'intervenir, il réserve l'intervention à ceux qui en ont la fonction. Les agents de nuit et les techniciens du froid gardent l'ouverture des cellules, avec leur badge nominatif. Chaque ouverture d'une cellule par une personne qui n'en est pas locataire est relue le matin par la sûreté, et un badge de secours reste sous la garde du poste de sûreté. Aujourd'hui, 2 600 badges ouvrent les 40 cellules ; demain, quelques dizaines, en plus des locataires. Le saisonnier trouvé dans la salle des machines n'y aurait pas eu accès.

**La revue périodique et la fin des comptes partagés et génériques** (a-5) :
- **Revue des droits** chaque semestre, avant l'été et à l'automne, pour les badges et les comptes : chaque direction métier, chaque référent d'entreprise et chaque prestataire reçoit la liste de ses personnes et de leurs droits, confirme ou retire, et ce qui n'est pas confirmé est suspendu. La revue est trimestrielle pour les droits étendus (validation des avoirs, administration des applications). Le rapprochement avec la liste de la paie est mensuel. La première revue a lieu avant la saison d'été 2027.
- **Fin des comptes partagés du portail** : un compte nominatif par personne, créé et retiré par le référent de l'entreprise, au lieu d'un identifiant commun connu même d'anciens salariés. L'incident de novembre 2026 (factures d'un grossiste consultées par un concurrent) en est la conséquence directe.
- **Fin des comptes génériques des tablettes** : un compte nominatif par placier et par saisonnier, avec une connexion rapide adaptée au travail de nuit (badge ou code personnel) ; le mot de passe écrit au dos des tablettes est changé tout de suite. Sans cela, aucune attribution du carreau n'est imputable à une personne (question 3.3).
- **Journaux** : relus par sondage chaque semaine et après chaque incident ; ce sont des données personnelles, à conserver pendant une durée limitée et à n'ouvrir qu'aux personnes habilitées, sur avis de la déléguée à la protection des données (annexe 3.5).

*3.2 b) – Les rôles et les responsabilités*

| Acteur | Rôle et responsabilités dans le dispositif |
|---|---|
| **Direction générale** (Mme VAUCLERC ; vous, directeur(rice) général(e) délégué(e)) | approuve la politique des accès (zones, populations, règles d'arrivée et de départ, revue) ; désigne les responsables ; arbitre les conflits entre sûreté et exploitation ; donne les moyens ; reçoit le bilan de chaque revue et rend compte de l'objectif de sûreté du plan |
| **Responsable de la sûreté** (M. MARCHEVIEL) | gère les badges : création, zones et horaires, désactivation ; contrôle sur le terrain (badges prêtés) ; relit les journaux de passage ; organise la revue des badges et en présente le bilan |
| **Responsable des systèmes d'information** (M. LAVEYRAC) | gère les comptes des applications, y compris l'administration des comptes du portail reprise à l'éditeur ; définit les profils types avec les métiers ; relie badges et comptes à une même source (ressources humaines, référentiel des entreprises) ; organise la revue des comptes ; n'accorde pas seul un droit qu'aucun métier n'a validé |
| **Directions métiers** (exploitation, technique, commercial, administrative et financière avec les ressources humaines) | propriétaires des droits de leur domaine : définissent les accès nécessaires à chaque fonction et valident demandes et revues ; les ressources humaines déclarent les arrivées et les départs ; l'exploitation, les placiers et les saisonniers ; la direction technique, les prestataires et les locaux techniques ; le service commercial, les référents des entreprises et le portail ; la direction administrative et financière, la séparation des tâches de la facturation |
| **Déléguée à la protection des données** (Mme TALMONDIER) | conseille sur la minimisation des données des badges et des journaux, leur durée de conservation et l'information des personnes |
| **Entreprises installées** | désignent un référent des accès ; demandent les badges et les comptes de leurs salariés ; déclarent chaque départ sous 48 heures ; répondent à la revue ; répondent de l'usage des badges par leurs salariés (aucun prêt), par un engagement écrit à la remise des badges |
| **Prestataires** | transmettent la liste nominative de leurs intervenants et signalent chaque départ ; n'utilisent que des badges nominatifs, dans les zones et aux heures de leur intervention ; répondent à la revue semestrielle de leur liste |

Chaque utilisateur, enfin, ne prête pas son badge et signale sa perte.

**Réponses tolérées**
- Cycle de vie présenté par étape (arrivée, changement, départ) plutôt que par population, si les quatre populations y figurent avec leur source et leur date de fin.
- Revue annuelle pour les badges des entreprises installées, alignée sur le contrat annuel d'emplacement, si elle est complétée par la suspension des badges inutilisés.
- Authentification à deux facteurs proposée pour les comptes du portail qui donnent accès aux factures, si elle ne remplace pas les comptes nominatifs.
- Désignation d'un référent sécurité ou rôle du comité de direction ajouté au tableau, s'il ne se substitue pas aux propriétaires métiers des droits.

**Erreurs fréquentes**
- *Réponse limitée aux badges ou aux comptes* (`JUR-S05`) — juste : un même dispositif pour les accès physiques et logiques, qui partagent les mêmes personnes et les mêmes départs non signalés.
- *Identification, authentification et autorisation confondues ; mot de passe complexe présenté comme une authentification forte* (`ET-28`) — juste : comptes nominatifs, preuve de l'identité, droits limités au besoin.
- *Moindre privilège appliqué au point d'empêcher l'exploitation, ou rejeté au nom de l'exploitation* (`JUR-T03`) — juste : droits nominatifs d'intervention, tracés et relus.
- *Responsable des systèmes d'information seul propriétaire des droits* (`JUR-T03`) — juste : les métiers décident des droits, la sûreté et les systèmes d'information les mettent en œuvre, la direction générale arbitre.
- *Réglage des équipements de contrôle d'accès, mesures techniques détaillées, analyse juridique des données des badges* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gestion des identités et des accès, moindre privilège, revue | cycle de vie, profils, traçabilité | F12 § 3 ; F10 § 3.1 | notion de cours |
| ISO/IEC 27001:2022 | norme d'exigences ; mesures de l'annexe A : gestion des identités, contrôle d'accès, sécurité physique | `iso_27001_2022` ; F12 § 2 | en vigueur |
| ISO/IEC 27002:2022 | guide de mise en œuvre des mesures | `iso_27002_2022` ; F12 § 2 | en vigueur |
| Rôles dans la sécurité | direction, métiers, prestataires, déléguée à la protection des données | F12 § 1 ; F15 § 1 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | minimisation, conservation limitée et sécurité des journaux, en principe | `rgpd` ; F15 § 2 | applicable depuis le 25/05/2018 |

---

### 3.3 – L'audit de l'attribution des emplacements du carreau (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : aucun test technique détaillé ; aucune analyse juridique, ni règle de non-discrimination ou de concurrence.

**Annexes mobilisées** : annexe 3.3 (règles écrites, journal, écarts de l'été 2026, plaintes, demande du conseil d'administration), annexe 3.2 (comptes génériques des tablettes, saisonniers), annexe 3.5 (RGPD en principe) et annexe 1.1 (300 emplacements, 180 producteurs par nuit l'été, placiers sur tablette, activité de nuit).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit d'un processus du SI défini ; objectifs et périmètre de la mission tirés de l'annexe 3.3 | 0,5 |
| a-2 | Étapes réparties sur les quatre semaines (fériés, conclusions au conseil du 31 mai) avec leurs livrables ; quatre preuves à demander, dont l'extraction du journal des modifications avant son effacement | 0,5 |
| b-1 | Trois critères (équité, traçabilité, fiabilité des données) : ce qui est attendu et ce que l'annexe laisse craindre, avec ses chiffres | 0,5 |
| b-2 | Deux facteurs de succès et deux points de vigilance propres à cet audit (nuit, placiers, données incomplètes, calendrier) | 0,5 |

**Réponse attendue**

*3.3 a) – Le cadrage de l'audit*

**Définition** (a-1) : l'**audit d'un processus du système d'information** est un examen indépendant et méthodique qui compare le fonctionnement réel d'un processus appuyé sur le système d'information (règles, pratiques, données, accès, traces) à un **référentiel** et à des **critères**, relève les écarts, en apprécie les risques et formule des recommandations hiérarchisées (F10 § 1.1 et § 1.2). Ici, c'est un **audit externe contractuel** demandé par le conseil d'administration. Son référentiel est le règlement du carreau de 2018, avec les règles internes d'accès aux tablettes. Ce n'est ni un audit légal des comptes, ni une enquête disciplinaire sur les placiers.

**Objectifs** (trois sont attendus, quatre sont proposés) :
- vérifier que les attributions de l'été 2026 respectent l'ordre de priorité écrit : abonnés, puis ancienneté, puis ordre d'arrivée ;
- apprécier la **fiabilité** des données enregistrées par rapport à l'occupation réelle ;
- apprécier la **traçabilité** des attributions et des modifications, et les contrôles existants ;
- recommander des règles et des contrôles applicables dès la saison d'été 2027, qui commence le 1er juin, et donner au conseil une réponse étayée aux 35 plaintes.

**Périmètre** :
- le processus d'attribution, de l'arrivée du producteur au péage à l'occupation constatée de l'emplacement ;
- la saison d'été 2026, de juin à septembre, et deux nuits observées en mai 2027 ;
- les données : journal des attributions et des modifications, liste des abonnés, ancienneté des producteurs, heures d'arrivée au péage, relevés des agents de sûreté, feuilles papier ;
- les acteurs : chef des placiers, 12 placiers, saisonniers, agents de sûreté, service commercial pour les abonnements, service des systèmes d'information.

Sont exclus : l'opportunité des règles elles-mêmes, que le conseil a fixées (l'audit peut toutefois signaler une règle ambiguë) ; la facturation des emplacements ; toute analyse juridique.

**Étapes, calendrier et livrables** (a-2 ; 18 jours ouvrés) :

| Semaine | Étape | Livrable |
|---|---|---|
| 1 (3-7 mai ; jeudi 6 mai férié) | **cadrage** : lettre de mission signée par la directrice générale sur mandat du conseil (objectifs, périmètre, référentiel, critères, accès garantis aux données et aux nuits du carreau, confidentialité, interlocuteurs) ; réunion de lancement avec Mme TRÉMOULAC et les placiers ; **extraction et conservation d'une copie du journal de l'été 2026** par le service des systèmes d'information | lettre de mission, liste des preuves demandées |
| 2 (10-14 mai) | **prise de connaissance** : entretiens avec la chef des placiers, plusieurs placiers, des agents de sûreté, le service commercial et le responsable des systèmes d'information ; **observation de deux nuits** sur le carreau, de minuit à 5 heures ; **cartographie du processus** d'attribution (étapes, données, contrôles) ; analyse des risques ; programme de travail | cartographie du processus, programme de travail |
| 3 (18-21 mai ; lundi 17 mai férié) | **examen** : reconstitution de l'ordre de priorité sur un échantillon de nuits ; analyse des modifications faites après 3 heures (emplacements, bénéficiaires, comptes) ; rapprochement des attributions et des relevés de 5 heures ; examen des feuilles papier et des ressaisies | dossier de travail |
| 4 (24-28 mai) | **constats** (constat, cause, risque, recommandation, priorité, responsable, échéance), **validation contradictoire** avec Mme TRÉMOULAC et la direction générale ; **rapport et note de synthèse**, avec les mesures applicables au 1er juin | rapport, note de synthèse, plan d'action |

Les conclusions sont présentées au conseil du lundi 31 mai ; le suivi du plan d'action revient à la direction de l'exploitation.

**Preuves à demander** (a-2 ; quatre sont attendues, huit sont proposées) :
- l'**extraction intégrale du journal des attributions et de leurs modifications** de l'été 2026 (date, heure, compte, emplacement, producteur), à faire dès la première semaine : les nuits de juin 2026 seront effacées à partir de juillet 2027 ;
- le règlement du carreau de 2018 et les consignes écrites ou orales données aux placiers ;
- la liste des abonnés de la saison 2026 et la liste d'ancienneté des producteurs ;
- les heures d'arrivée des producteurs au péage ;
- les relevés de 5 heures des agents de sûreté des 10 nuits d'août et la comparaison faite par Mme TRÉMOULAC (270 écarts) ;
- les feuilles papier conservées des six nuits sans tablettes et leurs ressaisies ;
- la liste des comptes des tablettes, de leurs utilisateurs et les plannings des placiers ;
- les 35 plaintes de 2026 et les réponses qui leur ont été faites.

*3.3 b) – Les trois critères, les facteurs de succès et les points de vigilance*

**Trois critères d'appréciation** (b-1) :

| Critère | Ce qui est attendu | Ce que l'annexe 3.3 laisse craindre |
|---|---|---|
| **Équité** | chaque emplacement est attribué selon l'ordre écrit, le même pour tous ; l'emplacement d'un abonné absent à 3 heures est réellement remis en attribution ; les dérogations sont rares, motivées et contrôlées | 30 des 40 emplacements de l'entrée occupés plus de huit nuits sur dix par les mêmes 25 producteurs, dont 10 ne sont ni abonnés ni parmi les plus anciens ; 40 % des modifications faites après 3 heures, sans motif ; emplacements « pris » qui restent vides jusqu'à 4 heures ; 35 plaintes |
| **Traçabilité** | chaque attribution et chaque modification est imputable à une personne, horodatée, motivée, et conservée assez longtemps pour être contrôlée | deux comptes génériques, utilisés aussi par les saisonniers, mot de passe au dos des tablettes : impossible de savoir qui a modifié ; aucun motif ; conservation de treize mois ; feuilles papier en partie perdues |
| **Fiabilité des données** | les données enregistrées reflètent l'occupation réelle : exactes, complètes, à jour | 270 occupations sur 1 800, soit 15 %, ne correspondent pas à l'attribution enregistrée ; six nuits ressaisies le lendemain ; toute statistique tirée du logiciel sur le carreau est donc douteuse |

**Deux facteurs de succès** (b-2 ; deux parmi les suivants) :
- un **mandat clair du conseil** et un **sponsor** à la direction générale, qui garantissent à l'auditeur l'accès aux données, aux personnes et au carreau la nuit, et l'**indépendance** de ses conclusions ;
- l'**adhésion des placiers** : l'audit porte sur le processus et ses contrôles, non sur les personnes ; Mme TRÉMOULAC est associée dès le lancement, les entretiens restent confidentiels et les constats sont validés contradictoirement ;
- des **compétences doubles** : l'exploitation d'un journal de données et la connaissance du fonctionnement réel du carreau ;
- la **conservation immédiate des preuves**, avant l'effacement du journal.

**Deux points de vigilance** (b-2 ; deux parmi les suivants) :
- le **travail de nuit** : les attributions se font de minuit à 5 heures, quand le service des systèmes d'information est absent ; l'auditeur doit planifier des nuits d'observation et disposer d'un interlocuteur de nuit ;
- les **données incomplètes** : avec des comptes génériques et des feuilles perdues, aucune modification ne peut être imputée à un placier ; l'audit doit le dire comme une limite et ne pas conclure à une faute individuelle ;
- la **relation avec les placiers**, qui vivront l'audit « comme une accusation », et la pression des producteurs : confidentialité, ton factuel, restitution d'abord aux audités ;
- le **calendrier** : 18 jours ouvrés, conclusions au conseil du 31 mai, saison le lendemain ; les recommandations doivent être hiérarchisées et applicables tout de suite ;
- les **données personnelles** des placiers et des producteurs dans le journal : accès limité aux besoins de la mission (annexe 3.5).

**Réponses tolérées**
- Démarche en cinq ou six étapes (cadrage, prise de connaissance, analyse des risques, examen, constats, restitution, suivi), si elle tient dans les quatre semaines et aboutit au conseil du 31 mai.
- Critère d'efficacité (temps d'attribution, attente des producteurs) ou de sécurité des accès aux tablettes en complément des trois critères, s'il est appliqué au cas.
- Facteurs de succès ou points de vigilance différents s'ils sont propres à cet audit (par exemple la neutralité de l'auditeur vis-à-vis des producteurs qui se plaignent).

**Erreurs fréquentes**
- *Méthodologie incomplète* (`JUR-A01`) — juste : objectifs, périmètre, référentiel, étapes, livrables, calendrier et preuves.
- *Audit du SI confondu avec l'audit légal ou avec une enquête disciplinaire* (`ET-34`) — juste : audit contractuel d'un processus, commandé par le conseil, qui conclut sur le processus et ses contrôles.
- *Facteurs de succès génériques* (`JUR-T01`, `JUR-T08`) — juste : nuit, placiers, données incomplètes, calendrier de la saison.
- *Conclusion sur des personnes à partir de comptes génériques* (`JUR-T03`) — juste : l'imputabilité manque ; c'est un constat en soi.
- *Analyse juridique de l'égalité d'accès ou de la concurrence entre producteurs ; tests techniques sur les tablettes* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Démarche d'audit du SI, livrables | cadrage, prise de connaissance, risques, examen, constats, restitution, suivi | F10 § 1.1 et § 1.2 | notion de cours |
| Critères d'audit, facteurs de succès | équité, traçabilité, fiabilité ; indépendance, adhésion, accès aux données | F10 § 0 et § 1 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | données personnelles du journal, accès limité, en principe | `rgpd` ; F15 § 2 | applicable depuis le 25/05/2018 |

---

### 3.4 – Les données de durabilité, l'affichage dynamique et la gouvernance responsable du système d'information (4 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.b` « Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) » ; `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété ». Limites : la durabilité est intégrée à la gouvernance globale du SI ; aucun calcul d'empreinte, aucun assujettissement à déterminer, aucune exigence détaillée des ESRS.

**Annexes mobilisées** : annexe 3.4 (demandes de trois entreprises installées, sources des données, erreurs, projet d'affichage, absence de règle), annexe 3.5 (CSRD, ESRS révisées, norme volontaire VSME) et annexe 1.1 (40 cellules, refacturation de l'énergie, de l'eau et du froid de 5 M€, supervision du froid, pont-bascule, portail, application des acheteurs, horaires du marché).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | État de durabilité selon les ESRS rappelé (double matérialité, chaîne de valeur, information fiable et justifiable) ; raisons des demandes : BRÉVALIM détient seule les mesures de consommations et de déchets des entreprises ; enjeu commercial pour BRÉVALIM | 0,5 |
| a-2 | Rôle du SI dans la collecte, la traçabilité et la fiabilité, appliqué aux trois sources (logiciel de gestion, supervision du froid, pont-bascule) et aux erreurs de 2026 | 0,5 |
| a-3 | Trois mesures justifiées | 0,5 |
| b-1 | Sobriété numérique définie et distinguée de l'efficacité (Green IT) et de l'économie d'énergie | 0,5 |
| b-2 | Projet apprécié : besoin, durée d'allumage (48 heures d'activité sur 168), définition des vidéos, rafraîchissement, réemploi des 20 écrans | 0,5 |
| b-3 | Trois mesures de sobriété justifiées | 0,5 |
| c-1 | Instance (composition, rôle) et trois critères de durabilité dans les décisions sur les projets | 0,5 |
| c-2 | Un indicateur complet (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.4 a) – Les demandes de données de durabilité et le rôle du système d'information*

**L'état de durabilité** (a-1) : une entreprise dans le champ de la CSRD publie un **état de durabilité** établi selon les normes ESRS (annexe 3.5 ; fiche commune). Il repose sur la **double matérialité** : les impacts de l'entreprise sur l'environnement et les personnes, et les effets des enjeux de durabilité sur l'entreprise. Il couvre ses propres activités et sa **chaîne de valeur**. Ses informations doivent être **fiables, traçables et justifiables** : ce n'est pas un simple rapport rédigé à partir d'estimations.

**Pourquoi les entreprises installées s'adressent à BRÉVALIM** :
- l'électricité, l'eau et le froid consommés dans leurs cellules et leurs cases, et les déchets qu'elles produisent sur le site, font partie de leurs propres consommations et de leurs impacts ; or **seule BRÉVALIM les mesure**, avec ses compteurs, la supervision du froid et le pont-bascule ;
- BRÉVALIM est dans leur **chaîne de valeur** : elle leur loue les emplacements, leur fournit l'énergie, l'eau et le froid, et collecte leurs déchets ;
- BRÉVALIM n'établit pas d'état de durabilité et n'a aucun assujettissement à déterminer : elle répond à une **demande de ses clients**. L'enjeu est commercial (M. PERRAGUÈS : « ils iront chercher ailleurs des cellules mieux suivies ») et de réputation. Il est aussi de coût, puisque les trois demandes prennent déjà 15 jours par an et que deux autres sont annoncées pour 2028.

**Le rôle du système d'information** (a-2) :
- **collecte** : les données existent déjà dans trois applications (logiciel de gestion du marché pour l'électricité et l'eau, supervision du froid, pont-bascule). Le système d'information doit les extraire automatiquement et les rattacher à chaque entreprise par un **référentiel des points de mesure** (compteur, cellule, benne) lié aux contrats d'emplacement, au lieu de relevés à l'écran et de tris à la main ;
- **traçabilité** : pour chaque donnée envoyée, il faut savoir d'où elle vient, sur quelle période, avec quelle unité et quelle méthode. Les déchets, mesurés par pavillon et répartis selon la surface, sont une **estimation** et doivent être présentés comme tels. Ce qui a été envoyé doit être conservé, avec ses corrections ; aujourd'hui, rien ne l'est ;
- **fiabilité** : des contrôles automatiques évitent les erreurs de 2026. Une période complète, sans mois compté deux fois, aurait évité le double mois de décembre ; un rattachement exact des cellules aux contrats, le froid de la cellule voisine ; une variation anormale expliquée, la hausse de moitié des déchets. Un rapprochement avec la **refacturation** donne la règle : un chiffre envoyé doit être le chiffre facturé.

**Trois mesures** (a-3) :
1. **Un référentiel unique des points de mesure**, tenu par la direction technique avec le service commercial : chaque compteur, chaque cellule de la supervision du froid et chaque benne ou pavillon est rattaché à une entreprise et à son contrat, et mis à jour à chaque changement d'emplacement (lien avec la question 3.1).
2. **Une extraction contrôlée et documentée**, produite chaque année avant la fin de janvier, puis chaque trimestre : contrôles de complétude, de doublon, de cohérence avec la refacturation et de variation ; une fiche de méthode par donnée ; les estimations signalées ; la mise à disposition **sur le portail**, dans l'espace de chaque entreprise, qui ne voit que ses propres données, avec l'historique des versions. Le tableur envoyé par courriel disparaît.
3. **Un responsable et un format communs** : le directeur technique est désigné propriétaire de ces données. Le même modèle de réponse sert à toutes les entreprises qui en font la demande (cinq en 2028), au besoin en s'appuyant sur la norme volontaire VSME pour structurer les informations (annexe 3.5). Pour les déchets, la mesure par entreprise est améliorée là où c'est possible ; ailleurs, la méthode d'estimation est indiquée avec le chiffre.

*3.4 b) – La sobriété numérique et le projet d'affichage dynamique*

**Définition** (b-1) : la **sobriété numérique** consiste à **interroger d'abord le besoin** (faut-il ce service, pour qui, à quelle échelle, avec quelle qualité ?) avant de chercher à le rendre plus efficace. Elle limite les équipements, les données et l'énergie au juste nécessaire. Elle se distingue du **Green IT**, qui réduit l'empreinte du système d'information à besoin donné, et ne se réduit pas à une économie d'énergie : pour des équipements électroniques, la **fabrication** pèse souvent davantage que la consommation (F14 § 1 et § 3).

**Appréciation du projet** (b-2) :
- **Le besoin** n'est pas démontré : les cours du jour ne changent que deux fois par nuit, et les horaires, le plan et les informations figurent déjà dans l'application des acheteurs. La publicité des grossistes est un objectif commercial, non un besoin d'information. Quelques écrans aux points de passage (péage, entrées des pavillons) peuvent suffire ; 60 écrans neufs ne se justifient pas.
- **La durée d'allumage** : jour et nuit, soit 168 heures par semaine, pour 48 heures d'activité (8 heures, six nuits sur sept) ; les écrans brillent sans public plus des deux tiers du temps.
- **La définition des vidéos** : de la haute définition en boucle pour des cours et des consignes qui sont du texte ; elle accroît les données transférées et stockées, la charge du serveur et la consommation des écrans.
- **La fréquence de rafraîchissement** : toutes les minutes, soit 1 440 fois par jour, pour deux mises à jour par nuit.
- **Le réemploi** : 20 écrans de 2022 qui fonctionnent seraient mis au rebut, et 60 écrans neufs fabriqués. C'est l'impact probablement le plus lourd du projet, et l'inverse de l'allongement de la durée de vie.

Le projet est donc **surdimensionné** au regard du besoin. Il ne faut pas forcément l'abandonner, mais le redimensionner. L'argument « la publicité les paiera » ne dit rien de son empreinte.

**Trois mesures de sobriété** (b-3 ; quatre sont proposées) :
1. **Réemployer** les 20 écrans existants et n'acheter que le complément justifié par des points de lecture réels, en privilégiant des écrans reconditionnés ou réparables, garantis longtemps, avec la reprise des équipements en fin de vie.
2. **N'allumer les écrans que pendant l'activité** (de l'arrivée des premiers acheteurs à la fin du marché, six jours sur sept), avec une extinction automatique ou une mise en veille le reste du temps.
3. **Des contenus sobres** : texte et images fixes pour les cours et les consignes, rafraîchis à chaque mise à jour des cours plutôt que toutes les minutes ; pas de vidéo en haute définition en boucle, au plus des séquences courtes et légères pour la publicité.
4. **Partir du besoin** : publier les cours du jour dans l'application des acheteurs, déjà installée, et réserver les écrans aux lieux où le téléphone ne suffit pas.

*3.4 c) – Une gouvernance du système d'information orientée vers la responsabilité sociétale*

**L'instance** (c-1) : un **comité du numérique responsable**, présidé par vous, directeur(rice) général(e) délégué(e) chargé(e) du système d'information. Il réunit :
- le responsable des systèmes d'information ;
- le directeur technique, pour l'énergie, les déchets et les données de durabilité ;
- le service de la communication et la direction administrative et financière, pour les achats ;
- la déléguée à la protection des données, pour l'éthique et les données personnelles ;
- un représentant de l'Union des grossistes, au nom des entreprises installées.

Il se réunit deux fois par an et **avant toute décision** sur un projet ou un achat d'équipement du système d'information. Il fixe les règles (durée de vie des équipements, critères d'achat), suit les demandes de données de durabilité et rend compte à la direction générale. La durabilité entre ainsi dans les décisions au lieu d'être examinée après coup : aujourd'hui, le projet d'affichage n'a été vu que par la communication et son fournisseur.

**Trois critères de durabilité dans les décisions sur les projets** (c-1) :
1. **Le besoin et le dimensionnement** : besoin démontré, alternatives avec l'existant (application, équipements en place), juste dimensionnement des équipements, des données et des durées de fonctionnement.
2. **Le cycle de vie des équipements** : réemploi de l'existant, durée de vie et réparabilité, reprise et fin de vie des équipements remplacés.
3. **La capacité à produire des données de durabilité fiables et l'éthique des données** : le projet mesure ce qu'il consomme et permet de répondre aux entreprises installées ; il limite les données personnelles et protège les données des entreprises.

**Un indicateur de suivi** (c-2) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Part des projets et des achats du système d'information examinés selon les critères de durabilité avant décision** | nombre de projets et d'achats d'équipements du SI examinés par le comité du numérique responsable avant la décision / nombre total de projets et d'achats d'équipements du SI décidés sur la période × 100 | registre des avis du comité ; bons de commande enregistrés dans le progiciel comptable | semestrielle | 100 % dès le second semestre 2027, contre 0 % aujourd'hui, aucune règle n'existant (annexe 3.4 C) | gouvernance |

**Réponses tolérées**
- Raison des demandes exprimée par les seules notions du cours (fournisseur de la chaîne de valeur, données d'activité nécessaires aux informations environnementales des groupes), si l'idée que BRÉVALIM détient seule les mesures est présente.
- Mesures différentes en a) si elles traitent la collecte, la traçabilité et la fiabilité : contrôle de cohérence avec la refacturation, archivage des envois, compteurs ou pesées par entreprise.
- Mesures de sobriété classées dans un autre ordre, ou quatrième mesure à la place de l'une des trois, si chacune répond à un défaut relevé.
- Instance intégrée à une instance de pilotage du système d'information existante ou à créer, si la durabilité y a un ordre du jour, des critères et un responsable.
- Autre indicateur complet et relié au cas : part des demandes de données de durabilité servies dans le délai sans correction (cible 100 % en 2028) ; heures d'allumage des écrans hors activité (cible zéro) ; part des équipements réemployés lors d'un renouvellement.

**Erreurs fréquentes**
- *Sobriété confondue avec l'économie d'énergie, ou réduite à la mise en veille* (`ET-12`) — juste : interroger le besoin et le nombre d'écrans d'abord, puis l'allumage et les contenus.
- *Empreinte du projet limitée à l'électricité* (`ET-38`) — juste : la fabrication de 60 écrans neufs et la mise au rebut de 20 écrans en état de marche pèsent au moins autant.
- *État de durabilité réduit à un rapport, ou rôle du SI ignoré* (`ET-17`) — juste : collecte automatisée, traçabilité des méthodes et des envois, contrôles de fiabilité.
- *Assujettissement de BRÉVALIM calculé, exigences détaillées des ESRS citées* — non attendus : BRÉVALIM répond à la demande de ses clients ; seule l'architecture des normes est mobilisée.
- *Indicateur incomplet ou générique, durabilité traitée comme un ajout marginal* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe ; critères appliqués avant la décision, dans la gouvernance du SI.
- *Calcul d'empreinte tenté* — non attendu.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Directive (UE) 2022/2464 (CSRD), modifiée en 2025 et en 2026 | état de durabilité, chaîne de valeur, en principe | `csrd` ; F14 § 2 ; fiche commune | en vigueur |
| Règlement délégué (UE) 2026/1563 (ESRS révisées) | double matérialité, architecture des normes | `esrs_2026` ; fiche commune | applicable aux exercices ouverts à compter du 01/01/2027 |
| Règlement délégué (UE) 2026/1560 (norme volontaire VSME) | réponse structurée d'une entreprise hors du champ | `vsme` ; fiche commune | en vigueur |
| Sobriété, Green IT, durée de vie, fabrication | définitions, leviers | F14 § 1 et § 3 | notion de cours |
| Gouvernance du SI orientée vers la responsabilité sociétale | comité du numérique responsable, critères, indicateur | F14 § 0 et § 8 | notion de cours |
