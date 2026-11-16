# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 25 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique, F02 gouvernance et référentiels, F03 architecture et urbanisation, F04 relations avec les ESN et contrats, F05 projets et changement, F13 intelligence artificielle, glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Alignement du système d'information sur le plan « ROCALDÈNE 2030 » | `1.1.b` Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 4 |
| 1.2 Le processus « commande → expédition » et l'urbanisation du système d'information | `1.3.f` Analyse des processus métiers et rôle des architectures SI dans leur rationalisation ; `1.3.a` Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente, en intégrant les technologies émergentes ; `1.3.e` Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers (impacts organisationnels seulement) | 3 |
| 1.3 Gouvernance du programme de refonte | `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 3 |
| 1.4 Méthode, cahier des charges et plan qualité du projet | `1.5.b` Méthodologies de gestion de projet (cycle en V, agile, hybride) ; `1.5.c` Élaboration d'un cahier des charges fonctionnel et technique ; `1.5.f` Mise en œuvre et contrôle du plan qualité | 2,5 |
| 1.5 Contrat d'intégration avec VALTRÉMIS Intégration | `1.4.a` Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques | 1,5 |
| **Dossier 1 – Éclairer la stratégie du système d'information et préparer sa refonte** |  | **14** |

Répartition indicative : connaissances (alignement stratégique et modèle de Henderson et Venkatraman, urbanisation, gouvernance du SI) 1,5 point (items 1.1 a-1, 1.2 b-1, 1.3 a-1) ; analyse des annexes et recommandations 12,5 points, soit environ 89 %. Les définitions demandées en 1.4 et 1.5 (méthodes, formes de contrat) sont notées avec leur application. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – Alignement du système d'information sur le plan « ROCALDÈNE 2030 » (4 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.b` « Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 1.2 (enjeux de la première priorité du plan, état du SI, projets de 2025 et 2026, témoignages), 1.3 (cartographie et chiffres du processus « commande → expédition ») et 1.1 (organisation de l'union et des caves, système d'information, organigramme).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Alignement stratégique défini (mise en cohérence permanente de la stratégie du SI et de la stratégie de l'organisation) ; modèle de Henderson et Venkatraman présenté : deux axes (ajustement stratégique, intégration fonctionnelle), quatre domaines | 0,5 |
| a-2 | Trois désalignements, chacun situé sur un axe ou entre deux domaines du modèle et appuyé sur des faits chiffrés des annexes 1.2 et 1.3 (0,5 par désalignement) | 1,5 |
| a-3 | Pourquoi le remplacement du progiciel ne suffit pas (processus, caves, gouvernance, compétences) ; perspective d'alignement à suivre, justifiée | 0,5 |
| b | Trois orientations de la stratégie du SI, chacune reliée à un enjeu du plan ; l'une intègre une technologie émergente adaptée, avec son apport et une limite (0,5 par orientation) | 1,5 |

**Réponse attendue**

*1.1 a) – Alignement actuel du SI sur la première priorité du plan*

L'**alignement stratégique** est la mise en cohérence permanente entre la stratégie de l'organisation et la stratégie de son système d'information : le SI doit servir les choix stratégiques, et ses possibilités peuvent en retour ouvrir de nouvelles options. Il est **dynamique** (à refaire quand la stratégie change, ici avec le plan de décembre 2026) et **organisationnel** autant que technique (0,5 pt avec le modèle).

Le **modèle d'alignement stratégique** (*Strategic Alignment Model*, SAM) de Henderson et Venkatraman (1993) croise deux axes : l'**ajustement stratégique**, entre le niveau externe (choix de marchés, d'offre, de compétences distinctives) et le niveau interne (structures, processus, compétences) ; l'**intégration fonctionnelle**, entre le domaine des métiers et celui des technologies de l'information. Il en résulte quatre domaines : stratégie de l'organisation, stratégie des technologies de l'information, infrastructure et processus organisationnels, infrastructure et processus du SI. L'alignement suppose que les quatre domaines soient cohérents deux à deux.

**Trois désalignements** (0,5 pt chacun) :
1. **Une stratégie métier sans stratégie du SI** (intégration fonctionnelle au niveau stratégique, entre la stratégie de l'union et la stratégie des technologies de l'information) : le plan, adopté en décembre 2026, fixe l'export à 35 % du chiffre d'affaires en 2030 et une vente en ligne dès 2028, mais aucune stratégie du SI n'en découle ; le responsable du SI « n'a jamais pu présenter un plan » et ne siège pas au comité de direction. Les 160 k€ de projets choisis en 2025 et 2026 (site vitrine sans vente en ligne, bornes du caveau, notes de frais) ne servent pas la priorité 1, et le seul outil de l'export a été souscrit hors du SI. Le SI répond aux demandes au fil de l'eau, pas à la stratégie.
2. **Un SI incapable de porter les marchés visés** (ajustement stratégique côté SI, entre la stratégie des technologies et l'infrastructure du SI) : le progiciel, non maintenu après 2028, ne gère ni plusieurs devises, ni plusieurs langues, ni la vente aux particuliers ; les documents d'export et les fiches techniques sont faits sous tableur et traitement de texte ; l'équipe de six personnes est absorbée par la maintenance et l'assistance aux caves. Les capacités du SI ne correspondent ni à l'export en Amérique du Nord et en Asie ni à la boutique en ligne prévue en 2028.
3. **Des processus de l'union et des caves que le SI ne relie pas** (intégration fonctionnelle au niveau opérationnel, entre infrastructure et processus organisationnels et infrastructure du SI) : les vins disponibles dans les neuf caves sont connus une fois par semaine par neuf fichiers consolidés à la main, « déjà faux le jeudi », alors que les assemblages adaptés exigent une vision à jour ; deux flux sur onze seulement sont automatisés dans le processus « commande → expédition » ; 88 % des commandes de la grande distribution sont livrées complètes et à l'heure contre 98 % exigés, avec 350 k€ de pénalités, et 80 % à l'export, avec un délai de 12 jours ouvrés. L'organisation fédérale de l'union, dont chaque cave code ses cuves à sa manière, n'a pas d'équivalent dans le SI.

**Pourquoi le seul remplacement du progiciel ne suffit pas** (0,5 pt) : l'alignement n'est pas l'adoption d'un logiciel unique. Un progiciel commun reproduirait les ruptures actuelles si les processus (disponibilité des vins, promesse de livraison, documents d'export) ne sont pas repensés avant son paramétrage, si les caves ne l'adoptent pas (« l'union décide sans nous »), si aucune instance ne relie les priorités du plan aux choix du SI et si l'équipe informatique reste cantonnée à l'exploitation. La perspective à suivre est celle de la **transformation technologique** : partir de la stratégie de l'union pour définir d'abord une stratégie du SI (canaux de l'export et de la vente en ligne, partage des informations avec les caves), puis choisir l'infrastructure et le progiciel qui la portent ; elle s'accompagne d'une logique d'**exécution de la stratégie** pour la refonte des processus de l'union et des caves.

*1.1 b) – Trois orientations de la stratégie du système d'information*

1. **Un socle de gestion partagé par l'union et les caves, organisé autour des processus communs** (enjeux : offre adaptée et fiabilité des livraisons ; 0,5 pt) : un référentiel commun des vins et des cuves, une disponibilité des vins des neuf caves connue chaque jour, un processus « commande → expédition » intégré de la réception à la facture. Il est conçu avec les caves et non imposé : chacune y retrouve ses informations et voit ce que deviennent ses vins. C'est l'objet de la refonte, à condition que les processus soient revus avant le paramétrage.
2. **Des canaux numériques pour les nouveaux marchés** (enjeux : export à 35 % et vente en ligne à 3 % du chiffre d'affaires en 2030 ; 0,5 pt) : gestion des commandes et des documents de l'export en plusieurs devises et langues, suivi des importateurs dans un outil relié au socle (fin du logiciel isolé de l'export), boutique en ligne aux particuliers ouverte en 2028 et reliée en temps réel aux stocks, aux prix et à la facturation.
3. **Une prévision des ventes par apprentissage automatique pour piloter les assemblages et le conditionnement** (technologie émergente ; enjeux : assemblages adaptés et livraisons fiables ; 0,5 pt) : l'apprentissage automatique apprend, à partir de l'historique des commandes par cuvée, enseigne, pays et saison, à prévoir les volumes à venir, pour préparer les assemblages et programmer les lignes d'embouteillage plus tôt. **Apport** : sortir de l'assemblage « sur la base des ventes de l'année précédente » (M. SALVERNAC) et réduire les ruptures. **Limite** : le climat et les nouveaux marchés rendent l'historique moins représentatif (nouvelles cuvées sans historique, volumes plus variables) ; les prévisions ne valent que si les données du socle sont fiables, et la décision d'assemblage reste celle de la directrice de la production. L'outil est donc à expérimenter après la mise en service du socle.

Ces orientations supposent une gouvernance qui arbitre les demandes au regard du plan (question 1.3) et une part du budget du SI consacrée aux projets supérieure aux 400 k€ de 2026, alors qu'en 2025 et 2026 les mises à jour imposées ont absorbé 240 k€ et que 160 k€ seulement ont financé des projets demandés, sans lien avec le plan.

**Réponses tolérées**
- Désalignements situés selon les quatre domaines du modèle plutôt que selon ses axes, s'ils sont appuyés sur les annexes ; désalignement tiré du logiciel de l'export souscrit hors du SI (informatique parallèle) ou de la relation entre l'union et les caves, à la place de l'un des trois.
- Perspective d'**exécution de la stratégie** retenue seule, si elle est justifiée par l'existence d'un plan déjà adopté que l'organisation et le SI doivent servir ; perspective du **potentiel concurrentiel** évoquée pour la vente en ligne, si elle reste secondaire.
- Technologie émergente fondée sur l'**IA générative** (rédaction des fiches techniques et des descriptions de la boutique en ligne dans les langues des importateurs, assistance au service clients), si elle est distinguée de l'apprentissage automatique et assortie d'une validation humaine (risque d'erreur sur les données techniques du vin) ; ou sur l'automatisation des échanges avec les importateurs et les transitaires, si son apport métier est démontré.
- Orientation sur la gouvernance du SI (portefeuille unique des projets arbitré au regard du plan), si elle est reliée à un enjeu du plan.
- IT Balanced Scorecard ou chaîne de valeur mobilisés en complément du modèle demandé.

**Erreurs fréquentes**
- *Alignement réduit au choix du progiciel* (`JUR-G02` alignement réduit à un choix technique ou à une standardisation logicielle ; `ET-06`) — « le nouveau progiciel commun rétablira l'alignement » ; juste : processus, caves, gouvernance et compétences avant le logiciel.
- *Modèle récité sans application* (`JUR-T01` contextualiser chaque notion ; `JUR-G03` avis motivé fondé sur la théorie) — quatre domaines décrits sans les faits de l'annexe ; juste : chaque désalignement situé dans le modèle et chiffré.
- *Modèle mal attribué* (`ET-40` réponse sans référence explicite au modèle attendu) — « modèle de Porter » ; juste : Henderson et Venkatraman (1993).
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — « une IA générative prévoit les ventes » ; juste : la prévision relève de l'apprentissage automatique, la rédaction de textes de l'IA générative.
- *Technologie sans enjeu métier ni limite* (`ET-19` opportunités sans risques) — « installer de l'IA » ; juste : apport relié au plan et limite explicite.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle d'alignement stratégique (SAM), Henderson et Venkatraman (1993) | deux axes, quatre domaines, perspectives d'alignement | `henderson_venkatraman_1993` ; F01 § 1 | publié (modèle théorique) |
| Alignement stratégique | mise en cohérence permanente ; erreur de la standardisation logicielle | F01 § 1 et § 8 ; `erreurs_types.md` ET-06 | notion de cours |
| Apprentissage automatique et IA générative | familles distinctes, usages et limites | F13 ; `erreurs_types.md` ET-09 | notion de cours |

---

### 1.2 – Le processus « commande → expédition » et l'urbanisation du système d'information (3 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des SI : `1.3.f` « Analyse des processus métiers et rôle des architectures SI dans leur rationalisation » ; `1.3.a` « Concevoir, cartographier et évaluer l'architecture des systèmes d'information dans une logique d'urbanisation cohérente » ; `1.3.e` « Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers » (seuls les impacts organisationnels sont demandés). Limite : « Ne pas réduire l'urbanisation à une vision strictement technique : elle s'inscrit dans une stratégie globale. »

**Annexes mobilisées** : annexes 1.3 (étapes des deux commandes, cartographie des onze flux, chiffres de 2026), 1.2 (état du SI, témoignages de M. SALVERNAC et de Mme BOUSQUIÉRAN) et 1.1 (caves, effectifs du conditionnement, de la logistique et du service clients).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Trois dysfonctionnements, chacun avec ses effets chiffrés et sa cause dans l'architecture (0,5 pour deux dysfonctionnements complets) | 1 |
| a-2 | Appréciation d'ensemble de l'architecture : silos, flux point à point et manuels, absence de référentiel commun et de zone d'échange, caves hors du SI de l'union, inadaptation aux marchés visés | 0,5 |
| b-1 | Urbanisation définie (découpage en zones, quartiers, îlots faiblement couplés ; une donnée de référence, un propriétaire ; échanges par une zone d'échange ; démarche stratégique) | 0,5 |
| b-2 | Architecture cible appliquée au processus, en schéma ou en tableau : zones, référentiels, échanges, ce qui disparaît | 0,5 |
| c | Impacts organisationnels sur les trois métiers demandés, chacun appuyé sur le cas | 0,5 |

**Réponse attendue**

*1.2 a) – Trois dysfonctionnements et l'architecture actuelle*

1. **Des ressaisies multiples qui créent des erreurs** : une commande est saisie deux fois pour la grande distribution et quatre fois à l'export (flux F1, F2, F3, F5, F6, F8, F9) ; 540 réclamations de la grande distribution (6 % des commandes), surtout des quantités ou des références erronées, et 120 à l'export (10 %), surtout des documents erronés. *Cause* : la plateforme d'échange avec les enseignes, le logiciel de l'export et les tableurs ne sont pas reliés au progiciel ; les échanges sont point à point et manuels (neuf flux sur onze).
2. **Une promesse de livraison impossible à tenir** : la disponibilité des vins dans les caves n'est connue qu'une fois par semaine (F4), le planning du conditionnement est tenu hors du progiciel (F5, F6) et le stock de matières sèches est souvent faux ; 88 % des commandes de la grande distribution sont livrées complètes et à l'heure contre 98 % exigés, 350 k€ de pénalités logistiques, 4 jours ouvrés de délai contre 3 exigés ; le directeur commercial met deux ou trois jours à répondre à un importateur. *Cause* : les neuf logiciels de cave ne sont reliés ni entre eux ni au progiciel, et chaque cave code ses cuves et ses vins à sa manière : il n'existe aucun référentiel commun des vins.
3. **Un aval du processus manuel et dédoublé** : les quantités préparées sont notées sur papier et saisies le lendemain (F7), ce qui retarde d'autant la facture ; à l'export, la facture est établie en moyenne 3 jours ouvrés après l'expédition et deux factures coexistent (en euros dans le progiciel, en devise dans un tableur), avec des documents refaits à la main et 12 jours ouvrés de délai. *Cause* : le progiciel ne gère ni devises ni langues, il n'y a pas de saisie à la source dans l'entrepôt, et les outils bureautiques comblent les manques du progiciel.

**Appréciation d'ensemble** (0,5 pt) : l'architecture est une juxtaposition de **silos** reliés par des flux **point à point** dont la plupart sont des ressaisies, des courriels ou du papier ; les mêmes données (commandes, vins, clients) existent en plusieurs endroits sans propriétaire ni référentiel commun ; le processus dépend de quelques personnes (l'assistante qui consolide les fichiers des caves, l'assistante export) ; les caves sont en dehors du SI de l'union ; un outil métier a été ajouté hors de toute règle (logiciel de l'export). Elle ne peut absorber ni la hausse de l'export ni la vente en ligne, et elle arrive en fin de support : elle doit être urbanisée, et non simplement remplacée.

*1.2 b) – Une architecture cible urbanisée*

**Urbaniser** le SI consiste à l'organiser, par analogie avec l'urbanisme d'une ville, en **zones**, **quartiers** et **îlots** fonctionnels faiblement couplés, reliés par une **zone d'échange**, avec des **référentiels** uniques (une donnée de référence, un propriétaire) et une fonction implantée une seule fois, pour que le SI évolue au rythme de la stratégie sans tout reconstruire. C'est une démarche stratégique, qui part des processus métier et non d'un inventaire des serveurs (0,5 pt).

**Cible proposée** (0,5 pt ; un schéma lisible et légendé vaut ce tableau) :

| Zone | Quartiers et îlots | Support cible | Ce qui disparaît |
|---|---|---|---|
| Relation clients et canaux | commandes de la grande distribution, commandes export, boutique en ligne, suivi des importateurs | progiciel commun (commandes) ; boutique en ligne et outil de relation client reliés au progiciel | ressaisie des commandes (F1, F2, F3) ; logiciel isolé de l'export |
| Production | réception et cuves dans les caves, assemblage et élevage, planning du conditionnement, matières sèches | progiciel commun, partagé par l'union et les neuf caves | tableur des disponibilités (F4), tableur du planning (F5, F6) |
| Logistique | préparation (saisie à la source par lecture de codes-barres), expédition, transport | progiciel commun ; transporteurs et transitaire reliés par la zone d'échange | bons papier et saisie du lendemain (F7) ; réservations ressaisies (F8) |
| Gestion | facturation en plusieurs devises, documents d'export, comptabilité | progiciel commun | tableur des documents d'export (F9), double facture |
| Référentiels | vins et cuves (codification commune aux neuf caves), articles et matières sèches, clients (enseignes, importateurs, particuliers), transporteurs | référentiels uniques du progiciel, chacun avec un propriétaire désigné (production, commercial, logistique) | codifications propres à chaque cave |
| Échanges | plateforme d'échange avec les enseignes, boutique en ligne, transporteurs et transitaire | zone d'échange (interfaces de programmation, ou API, publiées et supervisées) | flux point à point spécifiques |
| Pilotage | suivi des commandes, des délais et des disponibilités | restitutions alimentées par le progiciel | consolidations manuelles |

Commentaire attendu : la cible ne se réduit pas au progiciel commun ; elle fixe les règles (référentiels uniques, zone d'échange, saisie unique à la source) qui permettront d'ajouter la boutique en ligne ou de remplacer un îlot sans tout reprendre. Les objectifs de la cible se mesurent sur les indicateurs du processus :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des commandes de la grande distribution livrées complètes et à l'heure | commandes livrées complètes à la date convenue / commandes livrées | progiciel commun et avis d'expédition | mensuelle | 98 % (88 % en 2026) | client |
| Délai moyen entre la réception d'une commande export et son expédition | somme des délais en jours ouvrés / nombre de commandes export expédiées | progiciel commun | mensuelle | 7 jours ouvrés (12 en 2026) | processus |

*1.2 c) – Impacts organisationnels sur trois métiers* (0,5 pt)

- **Service clients** : il passe de la saisie à la **relation et à la gestion des exceptions** ; les commandes arrivent sans ressaisie, la date de livraison possible est consultée directement, le temps libéré sert le suivi des enseignes et des importateurs. Il faut faire évoluer les fiches de poste, former aux nouveaux outils et aux langues de l'export, et accompagner la crainte de la perte des tâches de saisie.
- **Conditionnement et logistique** : le planning des lignes est construit à partir des commandes, des vins disponibles et des matières sèches du progiciel ; le responsable du conditionnement devient **planificateur** ; les préparateurs saisissent à la source, ce qui exige discipline et formation ; la fiabilité du stock de matières sèches devient l'affaire de tous.
- **Caves** : les directeurs et le personnel des caves quittent leur logiciel pour un outil commun, avec une **codification partagée** et des informations visibles par l'union au fil de l'eau ; ils perdent une part d'autonomie, mais gagnent la fin de la ressaisie du lundi et la visibilité sur ce que deviennent leurs vins (demande de M. MALVEIRAC) ; formation des saisonniers avant chaque campagne et utilisateurs clés dans chaque cave, sans informaticien.

**Réponses tolérées**
- Autres dysfonctionnements tirés de l'annexe 1.3 (arrêt d'une ligne faute d'étiquettes, étiquette d'un pays commandée après confirmation, informations dispersées entre courriel et tableurs), s'ils sont chiffrés ou datés et rattachés à une cause d'architecture.
- Cartographie de processus en couloirs (service clients, production, conditionnement, entrepôt, caves) au lieu d'un tableau, si elle est lisible et légendée ; aucune norme de modélisation n'est exigée.
- Cible en couches (métier, fonctionnelle, applicative, technique) ou fondée sur une approche par meilleure solution dans chaque domaine (*best of breed*) reliée par une zone d'échange, si les référentiels communs et la suppression des ressaisies apparaissent.
- Bus d'intégration ou plateforme d'échange nommés au lieu des interfaces de programmation, sans détail technique.
- Impacts sur les compétences (langues, relation client, rigueur de saisie) ou sur le pouvoir de décision des caves, s'ils sont reliés aux trois métiers.

**Erreurs fréquentes**
- *Urbanisation réduite à un inventaire technique ou au remplacement du progiciel* (`ET-20` urbanisation réduite à une vision technique ; `JUR-G07` le pourquoi puis le comment de l'urbanisation) — juste : zones, référentiels et échanges au service du processus.
- *Interopérabilité seulement technique* (`ET-36`) — oublier la codification commune des vins et les responsabilités des caves ; juste : niveaux sémantique et organisationnel.
- *Dysfonctionnements sans chiffres ni cause* (`JUR-T08` exploiter toutes les annexes) — « le processus est lent » ; juste : 88 % contre 98 %, 350 k€, 540 et 120 réclamations, 2 et 4 saisies.
- *Schéma illisible ou sans légende* (`JUR-T10` schémas et tableaux lisibles).
- *Décrire les modules d'un progiciel de gestion intégré* — acquis du DCG, hors des attentes ; juste : choix d'architecture et effets sur le processus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Urbanisation du SI | zones, quartiers, îlots ; référentiels uniques ; zone d'échange | F03 § 1 et § 6 | notion de cours |
| Cartographies et interopérabilité | flux point à point, interfaces de programmation, niveaux d'interopérabilité | F03 § 2 et § 3 ; `erreurs_types.md` ET-36 | notion de cours |

---

### 1.3 – Gouvernance du programme de refonte (3 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ».

**Annexes mobilisées** : annexes 1.2 (projets sans lien avec le plan, absence de règle d'arbitrage, témoignages) et 1.1 (conseil de l'union, organigramme, rattachement du responsable du SI, comité de direction, réunion trimestrielle des directeurs de cave).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance du SI définie (évaluer, diriger, surveiller ; distincte du management) ; rôle de chaque partie prenante citée, appliqué au cas | 0,5 |
| a-2 | Trois instances (composition, fréquence, rôle) adaptées à l'union et aux caves ; quatre critères d'arbitrage justifiés par le cas (0,5 + 0,5) | 1 |
| b-1 | Trois tensions analysées (SI et direction générale, SI et directions de l'union, union et caves), chacune appuyée sur un témoignage ou un fait | 0,5 |
| b-2 | Trois leviers concrets, chacun relié à une tension (0,5 pour deux leviers pertinents) | 1 |

**Réponse attendue**

*1.3 a) – Gouvernance du programme*

La **gouvernance du SI** est l'ensemble des structures, des processus et des règles par lesquels la direction **évalue** les besoins et les options, **oriente** les décisions et **surveille** la performance et les risques du SI au service de la stratégie (modèle « évaluer, diriger, surveiller » d'ISO/IEC 38500:2024) ; elle se distingue du management, qui exécute. Pour la refonte, elle doit associer une union et neuf caves autonomes.

**Rôle des parties prenantes** (0,5 pt avec la définition) :
- **Conseil de l'union** (présidents des neuf caves, présidé par M. ESCOURBIAC) : valide les orientations et l'enveloppe du programme, tranche les choix qui engagent les caves (logiciel commun, codification partagée), décide de la mise en service ; il est informé à chaque réunion.
- **Directrice générale** : commanditaire (*sponsor*) du programme, préside le comité de pilotage, arbitre et rend compte au conseil.
- **Directions de l'union** (commerciale, production et qualité, administrative et financière) : maîtrise d'ouvrage ; expriment les besoins, désignent les utilisateurs clés, recettent, conduisent le changement dans leurs équipes.
- **Responsable du SI** : maîtrise d'œuvre interne et garant de l'architecture cible ; pilote techniquement l'intégrateur avec le responsable administratif et financier adjoint, chef du programme.
- **Caves** (présidents et directeurs) : représentées au comité de pilotage, elles désignent des utilisateurs clés, participent au cahier des charges et à la recette du module des caves.
- **Adhérents** : informés et consultés par leur cave et par le portail ; représentés par leurs présidents au conseil.

**Trois instances** (0,5 pt) :

| Instance | Composition | Fréquence | Rôle |
|---|---|---|---|
| Conseil de l'union, en formation de comité stratégique du programme | présidents des neuf caves, directrice générale, chef du programme ; responsable du SI invité | à chaque réunion du conseil, au moins trimestrielle | valide les orientations, le périmètre et l'enveloppe ; arbitre les choix qui engagent les caves ; autorise chaque mise en service |
| Comité de pilotage du programme | directrice générale (présidente), trois directeurs de l'union, responsable du SI, chef du programme, deux directeurs de cave et un président de cave représentant les neuf caves, intégrateur pour la partie qui le concerne | mensuelle, hors période de vendanges pour les représentants des caves | suit délais, coûts, risques et qualité ; arbitre les demandes selon les critères ; décide des lots et des fenêtres de mise en service |
| Comité des utilisateurs clés | chef du programme, responsable du SI, utilisateurs clés de chaque direction et un par cave, intégrateur | toutes les deux semaines pendant la conception et la recette, suspendu de mi-août à fin octobre | exprime et valide les besoins, prépare et réalise la recette, relaie l'information dans les équipes et les caves |

**Quatre critères d'arbitrage** (0,5 pt) : contribution au plan « ROCALDÈNE 2030 » (priorité 1 d'abord : export, vente en ligne, assemblages) ; caractère obligatoire ou urgent (fin du support du progiciel en 2028, fenêtres hors vendanges) ; valeur pour les métiers et les caves, mesurée (pénalités de 350 k€, réclamations, ressaisies supprimées) ; risque et capacité (équipe de six personnes, disponibilité des caves, dépendance à l'intégrateur) ; coût dans l'enveloppe validée. Quatre critères suffisent.

*1.3 b) – Tensions et leviers*

**Trois tensions** (0,5 pt) :
1. **SI et direction générale** : le responsable du SI est rattaché au directeur administratif et financier, absent du comité de direction, et n'a « jamais pu présenter un plan » ; le plan a été adopté sans volet SI. Le SI est cantonné à l'exploitation, alors que la direction attend de lui la transformation.
2. **SI et directions de l'union** : « l'informatique ne suit pas » (M. SALVERNAC) contre « on me demande tout en même temps » (M. CAUSSINEL) ; les demandes arrivent directement par courriel, chacune jugée prioritaire, sans liste commune ni règle ; faute de réponse, la direction commerciale a souscrit son propre logiciel, payé hors du budget du SI et découvert après coup. Chacun voit l'autre comme l'obstacle.
3. **Union et caves** : « l'union décide sans nous » (M. MALVEIRAC) ; un logiciel commun est annoncé sans consultation à des caves qui ont choisi le leur et le maîtrisent, qui ressaisissent déjà chaque lundi pour l'union et qui craignent de perdre leur autonomie, tout en se disant prêtes à partager si elles voient ce que deviennent leurs vins.

**Trois leviers** (1 pt) :
1. **Un portefeuille unique des demandes et des projets**, alimenté par toutes les directions et les caves, arbitré par le comité de pilotage selon les critères publiés ; plus de demande directe par courriel ; tout outil métier est souscrit dans ce cadre (réponse aux tensions 1 et 2).
2. **Repositionner le responsable du SI** : participation au comité de direction pour les sujets du SI, rattachement fonctionnel à la directrice générale pour le programme, mission de proposer la stratégie du SI qui découle du plan ; des correspondants dans chaque direction pour traduire les besoins (tensions 1 et 2).
3. **Associer les caves dès la conception** : représentants au comité de pilotage, utilisateurs clés par cave, ateliers du cahier des charges tenus hors vendanges, restitution aux caves des informations sur leurs vins, communication portée par le président du conseil, assistance de proximité par l'union (tension 3).

**Réponses tolérées**
- Instances nommées autrement (comité de programme, comité de projet, club des utilisateurs des caves), si leur composition, leur fréquence et leur rôle sont adaptés à l'union et aux caves.
- Matrice RACI des principales décisions (cahier des charges, recette, mise en service) au lieu d'une liste de rôles.
- Recours à COBIT 2019 (domaine « évaluer, diriger, surveiller ») au lieu d'ISO/IEC 38500 pour définir la gouvernance, si le référentiel est correctement qualifié.
- Levier fondé sur la conduite du changement (ADKAR : comprendre, vouloir, savoir, pouvoir, ancrer) auprès des caves, s'il répond à une tension identifiée.
- Création d'un poste de directeur des systèmes d'information rattaché à la directrice générale, si elle reste un levier de la relation et non une analyse complète du modèle d'organisation de la fonction SI.

**Erreurs fréquentes**
- *Gouvernance confondue avec le management du projet* (`JUR-G06` vocabulaire précis de la gouvernance) — un planning de tâches au lieu des instances et des règles de décision ; juste : qui évalue, oriente, surveille et arbitre.
- *Oublier les caves ou les adhérents* (`JUR-T08` exploiter tous les témoignages) — une gouvernance limitée aux services de l'union ; juste : les caves représentées et associées.
- *Leviers génériques* (`JUR-G05` recommandations réalistes et opérationnelles) — « mieux communiquer » ; juste : portefeuille unique, place du responsable du SI, association des caves.
- *Référentiel présenté comme une norme ou une solution* (`ET-01`) — « installer COBIT » ; juste : COBIT 2019 est un référentiel, ISO/IEC 38500 une norme de lignes directrices.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 38500:2024, gouvernance des technologies de l'information | évaluer, diriger, surveiller ; principes de gouvernance | `iso_38500_2024` ; F02 § 4 | en vigueur |
| Comitologie du SI | comité stratégique, comité de pilotage, comité de projet | F02 § 6 | notion de cours |
| Relations entre DSI, direction générale et métiers | rattachement du responsable du SI, DSI fournisseur ou partenaire | F01 § 4 | notion de cours |

---

### 1.4 – Méthode, cahier des charges et plan qualité du projet (2,5 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de SI : `1.5.b` « Méthodologies de gestion de projet (cycle en V, agile, hybride) » ; `1.5.c` « Élaboration d'un cahier des charges fonctionnel et technique » ; `1.5.f` « Mise en œuvre et contrôle du plan qualité ». Limites : aspect budgétaire détaillé et approfondissement des approches de livraison continue exclus.

**Annexes mobilisées** : annexes 1.4 (objet, calendrier et contrainte des vendanges, deux méthodes, brouillon du cahier des charges, montée de version de 2022), 1.3 (volumes de commandes) et 1.1 (caves sans informaticien, saisonniers).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Les deux méthodes caractérisées et comparées au regard de la contrainte des vendanges, de la disponibilité des caves et de la fin du support | 0,5 |
| a-2 | Méthode recommandée (hybride) et justifiée : ce qui relève d'un cycle séquentiel, ce qui relève d'itérations, déploiement dans les caves | 0,5 |
| b-1 | Trois exigences réécrites, chacune précise, mesurable et assortie d'un critère de recette | 0,5 |
| b-2 | Structure du cahier des charges fonctionnel, appliquée au projet | 0,5 |
| c | Quatre éléments du plan qualité (recette, critères d'acceptation, revues), reliés aux défauts de 2022 | 0,5 |

**Réponse attendue**

*1.4 a) – Méthode de conduite du projet*

Le **cycle en V** enchaîne expression du besoin, spécifications, conception et réalisation, puis des tests en miroir jusqu'à la recette ; il convient à un besoin stable et documenté. Les **méthodes agiles** (Scrum : Product Owner, Scrum Master, Developers ; itérations courtes ou *sprints* ; backlog priorisé) livrent par incréments en impliquant les utilisateurs à chaque itération ; elles conviennent à un besoin évolutif.

**Comparaison** (0,5 pt) :
- *Méthode 1 (cycle en V, bascule unique en mars 2028)* : elle sécurise le socle (comptabilité, stocks, codes communs, reprise des données) et se prête au forfait. Mais les spécifications sont prévues de juin à octobre 2027, quand les caves sont indisponibles de mi-août à fin octobre : leurs besoins seraient mal exprimés. La bascule simultanée de l'union et des neuf caves concentre les risques ; un retard au-delà de juillet ferait perdre la fenêtre de 2028 jusqu'en décembre, c'est-à-dire jusqu'à la fin du support du progiciel.
- *Méthode 2 (agile intégrale)* : elle montre tôt la boutique en ligne et le portail et associe les utilisateurs. Mais elle prévoit des mises en service à l'automne, interdites ; les caves ne peuvent assister aux revues d'itération pendant les vendanges ; le socle doit être complet dès le premier jour (remarque de M. CAUSSINEL) ; elle exige un Product Owner disponible et se contractualise mal au forfait.

**Recommandation : une démarche hybride** (0,5 pt) :
- **le socle** (référentiels communs des vins et des cuves, stocks, commandes, conditionnement, facturation, comptabilité, reprise des données) suit un cycle séquentiel : spécifications rédigées avec les directions de l'union à l'été 2027 et avec les caves en novembre, après les vendanges ; recette formelle ; mise en service à l'union dans une fenêtre du printemps 2028, qui laisse une fenêtre de repli avant la fin du support ;
- **le module des caves** est déployé après les vendanges de 2028, dans l'hiver 2028-2029, après une recette sur une journée de réception simulée ; les logiciels de cave, maintenus jusqu'en 2030, servent encore pour la campagne de 2028 ; une cave pilote volontaire peut ouvrir la voie ;
- **la boutique en ligne, le portail et les outils de l'export** sont construits par itérations, avec un Product Owner désigné par la direction commerciale, et mis en service par incréments hors de la période d'août à novembre, pour une ouverture de la boutique en 2028.

*1.4 b) – Exigences vérifiables et cahier des charges fonctionnel*

Une exigence **vérifiable** est précise, mesurable, non ambiguë, priorisée (méthode MoSCoW : *Must, Should, Could, Won't*) et assortie d'un critère de recette. Trois réécritures parmi les suivantes (0,5 pt) :

| Exigence du brouillon | Réécriture vérifiable | Critère de recette |
|---|---|---|
| E1 « simple à utiliser » | Après une demi-journée de formation, un employé du service clients enregistre une commande de 20 lignes en moins de 3 minutes ; après une heure de formation, un saisonnier de cave enregistre une réception sans assistance (Must) | test chronométré sur 10 utilisateurs, dont 3 saisonniers ; 9 sur 10 atteignent le seuil |
| E2 « gérer les apports » | Chaque réception de vendange est enregistrée au poste de réception de la cave (adhérent, date et heure, poids, cuve de destination) en moins d'une minute et le contenu de la cuve est mis à jour aussitôt dans le logiciel commun, consultable par l'union (Must) | journée de réception simulée dans une cave, avec contrôle des contenus de cuve |
| E3 « traitées rapidement » | Une commande reçue par la plateforme d'échange avec les enseignes est intégrée sans ressaisie en moins de 15 minutes, et la date de livraison possible, calculée à partir des stocks, des vins disponibles dans les caves et du planning du conditionnement, s'affiche en moins d'une minute (Must) | 200 commandes réelles de 2026 rejouées ; aucune ressaisie |
| E4 « permettre l'export » (ambiguë : vente à l'étranger ou extraction de données) | Le logiciel gère les commandes en euros, dollars américains et canadiens et en au moins deux autres devises, et édite sans ressaisie la facture en devise et la liste de colisage en français et en anglais ; il permet par ailleurs d'extraire toutes les données dans un format ouvert et documenté (Must) | 30 commandes export de 2026 traitées de bout en bout ; documents conformes |
| E5 « voir leurs informations » | Chaque directeur de cave consulte, selon ses droits, les volumes de ses vins retenus dans les assemblages et les cuvées dans lesquelles ils ont été vendus, mis à jour chaque jour, sans accès aux données des autres caves (Should) | test des droits sur deux caves |
| E6 « compatible avec la vente en ligne » | Le logiciel met à disposition de la boutique en ligne, par des interfaces de programmation documentées, les stocks disponibles et les prix en temps réel, et intègre les commandes des particuliers sans ressaisie (Must pour 2028) | 50 commandes de test de la boutique intégrées et facturées |

**Structure du cahier des charges fonctionnel** (0,5 pt) : contexte et objectifs (plan « ROCALDÈNE 2030 », fin du support en 2028, objectifs mesurables : livraisons complètes et à l'heure, délais, suppression des ressaisies) ; périmètre (union et neuf caves ; inclus et exclus : licences du progiciel traitées à part) ; acteurs et utilisateurs (220 utilisateurs et les saisonniers) ; processus cibles (commande → expédition, assemblage, réception dans les caves, export, vente en ligne) ; exigences fonctionnelles priorisées et règles de gestion ; volumétrie (9 000 commandes de la grande distribution, 1 200 à l'export, 380 milliers d'hectolitres) ; contraintes (fenêtres hors vendanges, interopérabilité avec les enseignes et la boutique en ligne, réversibilité, sécurité) ; critères de recette ; livrables et modalités de réponse. Il est rédigé par la maîtrise d'ouvrage avec les utilisateurs, dont les caves et le service clients, et non par la seule équipe informatique ; le cahier des charges technique le complète (architecture, interfaces, performances, exploitation).

*1.4 c) – Plan qualité du projet* (0,5 pt)

Le **plan qualité** fixe l'organisation, les règles et les contrôles qui garantissent que le projet livre ce qui est attendu. Quatre éléments, en réponse aux défauts de la montée de version de 2022 :
1. **Une recette par les utilisateurs** : la recette fonctionnelle est conduite par la maîtrise d'ouvrage (service clients, comptabilité, production, utilisateurs clés des caves), après la recette technique de l'intégrateur, et non par l'équipe informatique seule.
2. **Un cahier de recette relié aux exigences** : chaque exigence a ses cas de test ; des scénarios de bout en bout (commande d'une enseigne de la plateforme d'échange à la facture, commande export en devise, journée de réception simulée dans une cave), les conditions tarifaires des douze enseignes, une reprise des données à blanc, sur des volumes réels de 2026 et non sur 30 commandes types.
3. **Des critères d'acceptation écrits et un procès-verbal** : aucune anomalie bloquante, anomalies majeures corrigées ou assorties d'un contournement accepté, toutes les exigences « Must » validées, factures de test conformes pour toutes les enseignes ; procès-verbal signé par la maîtrise d'ouvrage, avec ou sans réserves (jamais une recette tacite).
4. **Des revues et une décision de mise en service** : revues de fin de phase (spécifications, paramétrage, avant recette) ; revue d'aptitude à la mise en service par le comité de pilotage, qui vérifie les critères, la formation et le plan de retour arrière ; mise en service jamais d'août à novembre ni en période de pointe, suivie d'une assistance renforcée.

Critère d'acceptation formulé comme un indicateur :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des cas de test de recette réussis | cas de test réussis / cas de test exécutés, sans anomalie bloquante ouverte | cahier de recette et registre des anomalies | à chaque campagne de recette | au moins 95 % et aucune anomalie bloquante ouverte | processus |

**Réponses tolérées**
- Cycle en V retenu pour l'ensemble, s'il est découpé en lots déployés dans les fenêtres hors vendanges et si les spécifications des caves sont recueillies hors de leur période d'indisponibilité ; méthode agile retenue pour l'ensemble, si les mises en service respectent les fenêtres et si le socle est livré complet.
- Déploiement des caves avant les vendanges de 2028 (juin ou juillet), si le risque d'une première campagne sur un outil nouveau est identifié et traité (cave pilote, assistance renforcée, retour à l'ancien logiciel possible).
- Autres exigences réécrites, ou seuils différents, s'ils sont mesurables et assortis d'un critère de recette.
- Structure du cahier des charges présentée selon un autre plan, si les rubriques essentielles sont appliquées au projet.
- Plan qualité incluant la gestion des versions et des demandes de changement, ou la norme ISO 9001 citée en principe.

**Erreurs fréquentes**
- *Méthodes récitées sans les contraintes du cas* (`JUR-P02` deux méthodes comparées dans le contexte ; `JUR-T01`) — juste : vendanges, disponibilité des caves, fin du support, socle complet.
- *Agile assimilée à l'absence de cahier des charges* (`ET-32` MOA et MOE inversées ; agile « sans cahier des charges ») — juste : backlog priorisé, Product Owner, critères d'acceptation.
- *Exigence reformulée sans mesure* — « le logiciel doit être ergonomique » ; juste : un seuil et un test.
- *Planning détaillé ou chiffrage du projet* — non demandés ; juste : principes et fenêtres de mise en service.
- *Recette confiée à l'intégrateur ou à l'équipe informatique seule* (`JUR-P03` diagnostiquer les erreurs de gestion de projet) — l'erreur de 2022.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cycle en V, méthodes agiles, démarche hybride | critères de choix ; archétype du remplacement d'un progiciel en mode hybride | F05 § 2 | notion de cours |
| The Scrum Guide (novembre 2020) | Product Owner, Scrum Master, Developers ; sprint ; backlog | `scrum_guide_2020` ; F05 § 2.2 | en vigueur |
| Cahier des charges, MoSCoW, plan qualité, recette | exigences vérifiables, cahier de recette, procès-verbal | F05 § 3 et § 6 | notion de cours |

---

### 1.5 – Contrat d'intégration avec VALTRÉMIS Intégration (1,5 point)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.a` « Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques ». Limite : « L'analyse juridique approfondie relève du droit des contrats informatiques et est exclue du programme de l'UE. »

**Annexes mobilisées** : annexes 1.4 E (proposition de VALTRÉMIS Intégration), 1.4 A à D (calendrier, méthodes, brouillon du cahier des charges, montée de version de 2022) et 1.2 (équipe informatique de six personnes absorbée par la maintenance).

**Barème indicatif (1,5 pt)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Régie et forfait caractérisés ; forme recommandée, cohérente avec la méthode hybride, justifiée par les chiffres de l'annexe (1 200, 1 560 et 1 500 k€) et par la faiblesse du cahier des charges de mars 2027, qui reprend le brouillon de janvier | 0,5 |
| b | Trois clauses, chacune reliée à un risque du projet tiré des annexes (0,5 pour deux clauses pertinentes) | 1 |

**Réponse attendue**

*1.5 a) – Forme du contrat*

En **régie**, l'ESN met des consultants à disposition, facturés au temps passé et dirigés par le client : son engagement porte sur les moyens, et le risque de délai et de dépassement reste à l'union. Au **forfait**, l'ESN s'engage à livrer un résultat défini, conforme au cahier des charges, pour un prix et un délai fixés : elle porte le risque de dépassement, mais seulement sur un périmètre précis.

Chez ROCALDÈNE, la régie paraît moins chère (environ 1 200 k€ contre 1 500 k€), mais au rythme de dépassement constaté en 2021 (+30 %), elle coûterait environ 1 560 k€ : elle devient plus chère que le forfait dès que le dépassement dépasse 25 % (1 500 k€ / 600 € = 2 500 jours). Surtout, l'union n'a pas les moyens de diriger 2 000 jours de consultants : l'équipe de six personnes est absorbée par la maintenance. Le forfait est donc préférable, mais pas sur la version de mars 2027, qui reprend le brouillon de janvier et dont les exigences vagues déclencheraient des avenants au tarif de la régie. **Recommandation** : une phase de conception, forfaitaire et plafonnée, qui produit les spécifications validées ; puis un **forfait par lot** pour le socle et le module des caves, avec des jalons alignés sur les fenêtres hors vendanges ; et, pour la boutique en ligne et le portail menés par itérations, un forfait par itération ou une régie plafonnée pilotée par le Product Owner.

*1.5 b) – Trois clauses à négocier* (1 pt ; trois parmi les suivantes)

| Clause | Contenu | Risque du projet couvert |
|---|---|---|
| Jalons datés et pénalités de retard | jalons alignés sur les fenêtres de mise en service (printemps 2028 pour l'union, hiver 2028-2029 pour les caves) ; pénalités croissantes ; paiement échelonné par jalon validé au lieu de 40 % à la signature, avec une retenue jusqu'à la fin de la garantie | manquer une fenêtre fait glisser la mise en service de plusieurs mois, jusqu'à la fin du support du progiciel ; aucun jalon ni pénalité dans la proposition |
| Recette contradictoire | recette prononcée par un procès-verbal signé par l'union selon les critères d'acceptation du plan qualité ; suppression de la recette « réputée prononcée » au bout de dix jours ; délais de recette suspendus pendant les vendanges | une recette bâclée, comme en 2022 (300 factures erronées) ; recette tacite pendant une période où les utilisateurs sont indisponibles |
| Garantie étendue | correction gratuite des anomalies jusqu'à la fin de la première campagne de vendanges et du premier pic de fin d'année vécus sur le nouveau logiciel | trois mois de garantie s'achèvent avant que le module des caves ait servi en vendanges |
| Stabilité de l'équipe de l'intégrateur | chef de projet et consultants clés nommés ; remplacement soumis à l'accord de l'union, avec une période de recouvrement aux frais de l'intégrateur | perte de connaissance du projet en cours de route (« peut être remplacé selon les besoins de l'intégrateur ») |
| Droits sur les développements spécifiques, documentation et transfert de compétences | droits d'utilisation et de modification des interfaces avec les enseignes et la boutique en ligne, ou cession ; documentation des paramétrages ; formation de l'équipe informatique ; code déposé chez un tiers | dépendance à l'intégrateur pour faire évoluer des interfaces critiques, avec une équipe interne qui ne pourrait pas les reprendre |
| Gestion des changements | procédure de demande de changement, prix unitaires négociés, enveloppe et plafond de jours | dérive du périmètre et avenants coûteux à partir d'un cahier des charges flou |

**Réponses tolérées**
- Régie recommandée pour la phase de conception seule, si elle est plafonnée et pilotée par le chef du programme.
- Clause de réversibilité ou de confidentialité, si elle est reliée à un risque du projet d'intégration.
- Pénalités formulées comme une réduction de prix par semaine de retard, plafonnée.

**Erreurs fréquentes**
- *Régie et forfait inversés* (`ET-31` régie, forfait et infogérance confondus) — « en régie, l'ESN garantit le délai » ; juste : en régie, le risque reste au client.
- *Choisir la régie sur le seul prix affiché* — 1 200 k€ sans tenir compte du dépassement de 2021 ni de la capacité de pilotage de l'union.
- *Clauses sans lien avec les risques du projet* (`JUR-A05` contractualisation avec les prestataires) — liste générique ; juste : chaque clause répond à un fait de l'annexe 1.4.
- *Analyse juridique approfondie* (validité des clauses, régime de la responsabilité) — exclue du programme ; juste : principes et effets de gestion.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des contrats (régie, forfait, intégration) | engagement sur les moyens ou sur le livrable, répartition du risque | F04 § 1 ; `erreurs_types.md` ET-31 | notion de cours |
| Clauses critiques et risques de la relation | jalons, pénalités, recette, propriété des développements, dépendance | F04 § 4 et § 6 | notion de cours |
