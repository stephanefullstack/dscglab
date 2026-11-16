# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 9

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Éclairer la stratégie du système d'information et préparer sa refonte | 14 | 1.1 à 1.5 | `exercices/ex25_strategie_refonte_si_union` |
| 2 – Organiser et exploiter les données des parcelles et des apports ; authentifier les bouteilles | 13 | 2.1 à 2.5 | `exercices/ex26_donnees_parcelles_apports_authenticite` |
| 3 – Assurer la continuité du système d'information pendant les vendanges, fiabiliser les apports et choisir un hébergement responsable | 13 | 3.1 à 3.6 | `exercices/ex27_continuite_vendanges_hebergement` |
| **Total** | **40** | | |

---

## DOSSIER 1 – ÉCLAIRER LA STRATÉGIE DU SYSTÈME D'INFORMATION ET PRÉPARER SA REFONTE (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES PARCELLES ET DES APPORTS ; AUTHENTIFIER LES BOUTEILLES (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Modèle conceptuel des données des parcelles et des apports | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) | 2 |
| 2.2 Cohérence, interopérabilité et qualité des données | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données | 3 |
| 2.3 Rôles et responsabilités sur les données | `2.3.c` Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) | 1 |
| 2.4 Chaîne de valeur des données et analyse des apports de la vendange 2026 | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model | 4,5 |
| 2.5 Le projet d'authentification des cuvées exportées | `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.a` Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ; `3.3.d` Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO | 2,5 |
| **Dossier 2 – Organiser et exploiter les données des parcelles et des apports ; authentifier les bouteilles** |  | **13** |

Répartition indicative : connaissances (formalisme du MCD, interopérabilité, dictionnaire de données, DAMA-DMBOK, chaîne de valeur des données, méthodes d'analyse, blockchain, champ de MiCA) environ 3 points (la moitié des items 2.1 a-1 à a-4, et la moitié des items 2.2 a-1, 2.2 b-1, 2.3-1, 2.4 a-1, 2.4 c-1, 2.5 a et 2.5 c) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Modèle conceptuel des données des parcelles et des apports (2 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) ». Seul le modèle conceptuel est demandé.

**Annexes mobilisées** : annexe 2.1 (règles de gestion RG1 à RG8 ; constats 3 et 4 de la partie B pour la justification de l'adhésion et du rattachement de l'apport à la parcelle).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Six entités avec identifiant souligné et attributs élémentaires correctement placés (Adhérent, Cave, Parcelle, Cépage, Apport, Prélèvement), sans clé étrangère ni attribut répété | 0,5 |
| a-2 | Association n:m *adhérer* entre Adhérent et Cave, porteuse de la date d'adhésion (1,n / 1,n, RG3) ; association *exploiter* (Adhérent 1,n / Parcelle 1,1, RG4) | 0,5 |
| a-3 | Association *planter* (Parcelle 1,1 / Cépage 0,n, RG5) et associations de l'apport *livrer*, *recevoir*, *provenir* (Apport 1,1 / 0,n, RG6) | 0,5 |
| a-4 | Association *donner lieu* (Prélèvement 1,1 / Apport 1,n, RG7) et justification de chaque cardinalité par une règle de gestion ; la justification du lien direct *livrer* et la contrainte sur la cave d'adhésion sont valorisées, non exigées | 0,5 |

**Réponse attendue**

Le modèle conceptuel des données (MCD) représente les objets de gestion (entités), leurs propriétés (attributs) et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique (F07 § 1).

Entités (identifiant en premier, souligné sur la copie) (0,5 pt) :
- ADHÉRENT (<u>num_adherent</u>, nom, prenom, commune, telephone, courriel) – RG1 ;
- CAVE (<u>code_cave</u>, nom_cave, departement) – RG2 ;
- PARCELLE (<u>num_parcelle</u>, commune_parcelle, lieu_dit, surface_ha, annee_plantation) – RG4 ;
- CÉPAGE (<u>code_cepage</u>, libelle_cepage, couleur) – RG5 ;
- APPORT (<u>num_apport</u>, date_apport, heure_pesee, poids_kg, degre_potentiel, etat_sanitaire) – RG6 ;
- PRÉLÈVEMENT (<u>num_prelevement</u>, date_analyse, acidite_totale, ph) – RG7.

Associations et cardinalités :

```
ADHÉRENT    (1,n) ──── adhérer [date_adhesion] ──── (1,n) CAVE
ADHÉRENT    (1,n) ──── exploiter ────────────────── (1,1) PARCELLE
PARCELLE    (1,1) ──── planter ──────────────────── (0,n) CÉPAGE
APPORT      (1,1) ──── livrer ───────────────────── (0,n) ADHÉRENT
APPORT      (1,1) ──── recevoir ─────────────────── (0,n) CAVE
APPORT      (1,1) ──── provenir ─────────────────── (0,n) PARCELLE
PRÉLÈVEMENT (1,1) ──── donner_lieu ──────────────── (1,n) APPORT
```

Sur la copie, chaque entité n'est dessinée qu'une fois : APPORT au centre, relié à ADHÉRENT, CAVE, PARCELLE et PRÉLÈVEMENT ; ADHÉRENT relié aussi à CAVE et à PARCELLE ; PARCELLE reliée à CÉPAGE.

- *adhérer*, association n:m porteuse de la date d'adhésion : un adhérent adhère à une ou plusieurs caves (environ 40 viticulteurs livrent deux caves, constat 3) ; chaque cave compte au moins un adhérent (1,n de part et d'autre) ; la date d'adhésion ne dépend ni de l'adhérent seul ni de la cave seule, mais du couple – RG3 ;
- *exploiter* : une parcelle est exploitée par un et un seul adhérent (1,1) ; un adhérent exploite au moins une parcelle (1,n) – RG4 (0,5 pt pour ces deux associations) ;
- *planter* : une parcelle est plantée d'un seul cépage (1,1) ; un cépage peut n'être planté sur aucune parcelle, s'il est retenu pour les replantations (0,n) – RG5 ;
- *livrer*, *recevoir*, *provenir* : un apport est livré par un seul adhérent, à une seule cave, et porte sur une seule parcelle (1,1) ; un adhérent, une cave ou une parcelle peut n'avoir aucun apport (0,n) – RG6 (0,5 pt pour ces quatre associations) ;
- *donner_lieu* : un prélèvement concerne un seul apport (1,1) ; un apport donne lieu à au moins un prélèvement (1,n) – RG7.

Justification du lien direct *livrer* (valorisée, non exigée : RG6 impose déjà ce lien) : on pourrait retrouver l'adhérent par la parcelle, mais RG4 n'enregistre que l'exploitant **actuel** ; si une parcelle change d'exploitant, les apports passés doivent rester attribués à celui qui les a livrés. Le lien direct permet en outre un contrôle de cohérence (l'adhérent qui livre est l'exploitant de la parcelle déclarée), utile au constat 4. De même, la cave qui reçoit l'apport ne se déduit pas de l'adhérent, qui peut adhérer à deux caves : *recevoir* est indispensable.

RG8 ne crée ni entité ni association. Une contrainte non représentable par les cardinalités peut être signalée : l'apport ne peut être reçu que par une cave à laquelle l'adhérent qui livre adhère. Le modèle logique, non demandé, comporterait sept tables, dont une table Adhesion à clé composée (#num_adherent, #code_cave) portant la date d'adhésion.

**Réponses tolérées**
- Noms d'entités, d'associations ou d'attributs différents s'ils restent explicites (« Viticulteur », « Livraison », « Analyse ») ; notation « pattes de corbeau » ou UML lisible (format libre, `JUR-T10`).
- Omission de l'association *livrer* si le candidat la justifie explicitement (l'adhérent se déduit de la parcelle) et signale la limite liée au changement d'exploitant.
- Adhésion modélisée comme une entité ADHÉSION à identifiant propre reliée par deux associations 1,1 à Adhérent et à Cave, si le candidat signale l'unicité du couple adhérent × cave.
- Entité supplémentaire justifiée (COMMUNE, STATION) si elle ne contredit pas RG8 ; pas de pénalité pour une commune modélisée en entité, pas de bonification non plus.

**Erreurs fréquentes**
- *MCD et MLD confondus* (`ET-23`, `JUR-T06`) — clés étrangères (num_adherent dans PARCELLE, num_apport dans PRÉLÈVEMENT) dessinées dans le MCD ; juste : le MCD ne comporte ni clé étrangère ni table.
- *Attribut d'association mal placé* — date d'adhésion portée par l'adhérent ou par la cave, ce qui interdit de décrire l'adhérent qui livre deux caves ; juste : elle dépend du couple.
- *Adhérent rattaché à une seule cave* (1,1) — le modèle reproduit les doublons du constat 3 ; juste : association n:m.
- *Cardinalités non justifiées* (`JUR-T01`) — liste d'entités sans renvoi aux règles ; juste : chaque cardinalité est rattachée à une règle de gestion.
- *Hors sujet technique* — modèle logique détaillé, requêtes ou scripts de création de tables, que la question exclut.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Formalisme Merise (MCD, cardinalités, association porteuse) | entités, associations, cardinalités | F07 § 1 à 3 | manuels |

---

### 2.2 – Cohérence, interopérabilité et qualité des données (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ».

**Annexes mobilisées** : annexes 1.1 (neuf logiciels de cave de quatre éditeurs, aucun informaticien dans les caves, équipe informatique de 6 personnes), 2.1 (sources, constats 1 à 7, règles de gestion) et 2.2 (notes du tableau : conversions, échelles sanitaires).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Interopérabilité définie ; référentiel commun des données de référence (adhérents, caves, parcelles, cépages) tenu par l'union et alimentant les neuf logiciels de cave et le laboratoire | 0,5 |
| a-2 | Identifiants uniques attribués par l'union, non signifiants et stables, avec table de correspondance des anciens numéros ; reprise (fusion des doublons, mise à jour des surfaces) | 0,5 |
| a-3 | Circulation des données sur les trois plans : technique (échanges automatisés, formats ouverts, lecture du numéro de bon), sémantique (nomenclature des cépages, unités, échelle sanitaire), organisationnel (qui crée, qui valide, calendrier, engagement des éditeurs) | 0,5 |
| b-1 | Dictionnaire de données défini et quatre rubriques choisies et justifiées | 0,5 |
| b-2 | Entrées du degré potentiel et de l'état sanitaire cohérentes avec les constats (unité unique, échelle commune définie note par note, source, propriétaire) | 0,5 |
| c | Trois règles de qualité, chacune rattachée à une dimension (unicité, complétude, cohérence, exactitude, actualité, validité) et à un constat de l'annexe 2.1 B | 0,5 |

**Réponse attendue**

*2.2 a) – Référentiel commun, identifiants uniques et circulation des données*

L'**interopérabilité** est la capacité de systèmes hétérogènes à échanger des données et à les utiliser sans intervention manuelle ; elle est à la fois **technique** (échanges, formats), **sémantique** (même sens des données) et **organisationnelle** (processus, responsabilités) (F07 § 7 ; le niveau syntaxique, celui des formats, est ici rattaché au plan technique). À ROCALDÈNE, neuf logiciels de quatre éditeurs, des tableurs et un laboratoire décrivent les mêmes objets sans langage commun : neuf extractions envoyées chaque lundi et des tableaux établis à la main.

**Référentiel commun** (0,5 pt avec la définition) : l'union tient un référentiel des **données de référence** (gestion des données de référence) : adhérents, caves, parcelles et cépages, selon le modèle de la question 2.1. Il est la **seule source** de ces données : les logiciels de cave, le laboratoire et les outils d'analyse s'y alimentent au lieu de tenir chacun leur fichier. Les caves restent maîtresses de la réception de la vendange dans leur logiciel ; elles cessent de créer chacune leurs parcelles et leurs adhérents.

**Identifiants uniques** (0,5 pt) : numéro d'adhérent et numéro de parcelle attribués par l'union (RG1, RG4), **non signifiants** (ni la cave, ni la commune, qui peuvent changer), **stables** et jamais réattribués ; code de cépage commun (RG5) ; numéro de bon unique pour l'union (préfixé par le code de la cave, par exemple « SBZ-2026-01877 » : ce préfixe est acceptable pour un bon, car la cave qui reçoit un apport ne change jamais, mais non pour une parcelle ou un adhérent). Une **table de correspondance** conserve les anciens numéros de chaque cave pendant la transition (« P-0123 » de sept caves devient sept numéros distincts). La **reprise** fusionne les 40 adhérents en double (une fiche, deux adhésions), rapproche les 11 000 parcelles et corrige l'écart de 150 hectares (6 650 contre 6 500) avec les caves avant la vendange 2027.

**Circulation des données sur les trois plans** (0,5 pt) :
- *technique* : les logiciels de cave reçoivent du référentiel les listes d'adhérents, de parcelles et de cépages et renvoient chaque jour de vendange les apports à l'union par des échanges automatisés (interfaces de programmation ou fichiers dans un format ouvert décrit par le dictionnaire), au lieu des neuf extractions du lundi ; le laboratoire lit le numéro du bon (code imprimé sur l'échantillon) au lieu de le ressaisir ; les relevés des stations sont récupérés dans le même format ;
- *sémantique* : nomenclature unique des 12 cépages (fin des 31 codes), degré potentiel toujours en % vol., échelle sanitaire commune définie note par note, définitions du dictionnaire (b) partagées par les neuf caves et le laboratoire ;
- *organisationnel* : règles de création et de validation (la cave déclare une parcelle nouvelle, l'union la valide et lui attribue son numéro), calendrier (mise à jour des parcelles chaque hiver, hors vendanges), engagement des quatre éditeurs à lire et à transmettre les données au format commun, formation des agents de réception et des saisonniers, appui de l'équipe informatique aux caves, qui n'ont pas d'informaticien.

*2.2 b) – Dictionnaire de données*

Le **dictionnaire de données** est le référentiel qui décrit chaque donnée de façon unique et partagée : nom, définition, unité ou format, valeurs admises, règle de mesure ou de calcul, source, propriétaire, fréquence de mise à jour ; il fixe le sens commun des données, ce qui le distingue du MCD, qui décrit les relations entre les données (F07 § 1). Pour l'union, il met fin aux mesures hétérogènes du constat 6 : sans lui, deux caves qui écrivent « 3 » ne disent pas la même chose.

Quatre rubriques suffisent (0,5 pt avec la définition) ; le tableau en propose six, parmi lesquelles le candidat en retient quatre : **définition** (sens partagé), **unité et valeurs admises** (contrôle à la saisie, comparabilité), **règle de mesure** (qui mesure, quand, comment), **source de référence**, **propriétaire**, **fréquence de mise à jour**.

| Rubrique | Degré potentiel de l'apport | État sanitaire de l'apport |
|---|---|---|
| Définition | teneur en alcool que donnerait la vendange de l'apport si tous ses sucres étaient transformés, mesurée à la réception | proportion de raisins atteints par des maladies ou des altérations dans l'apport, appréciée à la réception |
| Unité et valeurs admises | % vol., une décimale ; valeurs plausibles de 8,0 à 16,0, toute valeur hors de cette plage étant bloquée et vérifiée ; jamais en grammes de sucres par litre (la conversion de LAURADEL et de CABRISSAC disparaît) | échelle commune de 1 (sain) à 4 (très dégradé), chaque note étant définie par une part de raisins atteints et illustrée par des photographies de référence ; « dégradé » = notes 3 et 4 dans les neuf caves |
| Règle de mesure | mesure à la pesée sur l'échantillon de l'apport, avec un appareil étalonné selon une procédure commune | note attribuée par un agent de réception formé, et non laissée aux seuls saisonniers ; note contrôlée sur un échantillon d'apports par le laboratoire |
| Source de référence | logiciel de cave, transmis au référentiel le jour même | logiciel de cave, transmis au référentiel le jour même |
| Propriétaire | directrice de la production et de la qualité de l'union | directrice de la production et de la qualité de l'union |
| Fréquence de mise à jour | à chaque apport ; définition revue chaque hiver | à chaque apport ; échelle revue chaque hiver avec les directeurs de cave |

(0,5 pt pour les deux entrées.) Sont valorisées : l'unité imposée et la fin des conversions ; l'échelle commune définie note par note, qui répond directement aux critiques de Mme TARASCOUL ; la formation des agents.

*2.2 c) – Trois règles de qualité* (0,5 pt)

| Règle | Dimension | Constat de l'annexe 2.1 B |
|---|---|---|
| Un viticulteur, un seul numéro d'adhérent : recherche obligatoire dans le référentiel avant toute création ; les 40 doublons sont fusionnés | unicité | 3 (adhérents en double) |
| Aucun apport sans parcelle du référentiel : la pesée exige un numéro de parcelle existant, choisi dans la liste des parcelles de l'adhérent qui livre, et non une déclaration orale | complétude et cohérence | 4 (plus d'un tiers des volumes sans parcelle) |
| Cépage choisi dans la nomenclature commune ; degré en % vol. et état sanitaire sur l'échelle commune, valeurs hors plage bloquées | validité (conformité) | 2 et 6 (31 codes pour 12 cépages, mesures non homogènes) |
| Surfaces revues chaque hiver avec les adhérents ; arrachages et cessions enregistrés dans le mois | exactitude et actualité | 5 (6 650 ha dans les fichiers pour 6 500 ha en production) |
| Tout prélèvement rattaché à un apport existant, par lecture du numéro du bon et non par ressaisie | cohérence (intégrité des liens) | 7 (1 100 prélèvements orphelins, 5 %) |
| Identifiant de parcelle unique pour l'union | unicité | 1 (même numéro dans sept caves) |

Trois règles sont attendues, chacune avec sa dimension et son constat.

**Réponses tolérées**
- Plateforme d'échange ou bus d'intégration cité, si le principe (référentiel unique, fin des fichiers du lundi) reste au premier plan ; référentiel placé dans le futur progiciel commun, si son rôle de source unique est préservé.
- Échelle sanitaire commune de 1 à 3 ou de 1 à 5, si elle est définie note par note et appliquée dans les neuf caves.
- Rubriques différentes du dictionnaire (type, exemple, sensibilité, durée de conservation) si elles sont justifiées.
- Dimensions de la qualité nommées autrement (intégrité, conformité, fraîcheur) ou citées d'après ISO/IEC 25012 ; un indicateur de suivi proposé en plus n'est pas exigé.

**Erreurs fréquentes**
- *Interopérabilité seulement technique* (`ET-36`) — interfaces proposées sans nomenclature commune ni règles de création ; juste : technique, sémantique et organisationnelle ensemble.
- *Sigle employé seul* (`ET-13`) — « mettre en place un MDM » sans dire qu'il s'agit de la gestion des données de référence ; juste : écrire en toutes lettres.
- *Identifiant signifiant* — numéro de parcelle construit avec le code de la cave ou de la commune : il change quand la parcelle change d'exploitant ou de cave ; juste : identifiant non signifiant et stable.
- *Dictionnaire confondu avec le MCD* — liste des entités au lieu de la description de chaque donnée ; juste : le dictionnaire décrit le sens, l'unité, la mesure et la source.
- *Qualité laissée à l'informatique* (`JUR-T03`) — « l'équipe informatique corrigera les fichiers » ; juste : la règle est fixée par le métier et appliquée à la saisie dans les caves.
- *Détail technique hors attente* (`JUR-T12`) — description de formats ou de serveurs ; la question l'exclut.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 25012 (2008) — Modèle de qualité des données | dimensions de la qualité, à titre d'exemple | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| Interopérabilité (niveaux technique, sémantique, organisationnel) ; données de référence ; dictionnaire | définitions, principes | F07 § 1, 6.2 et 7 | notion de cours |

---

### 2.3 – Rôles et responsabilités sur les données (1 point)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.c` « Gouvernance de l'information : rôles, responsabilités, référentiels (ex. : DAMA-DMBOK) ».

**Annexes mobilisées** : annexes 1.1 (organigramme, directeurs de cave, aucun informaticien dans les caves), 2.1 (sources, agents de réception, laboratoire, techniciens) et 2.4 (DAMA-DMBOK, RGPD).

**Barème indicatif (1 pt)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | DAMA-DMBOK présenté comme un référentiel de bonnes pratiques (et non une norme ni un logiciel), qui place la gouvernance au centre et décrit les rôles de propriétaire et d'intendant | 0,5 |
| 2 | Trois rôles avec missions et titulaires, répartis entre l'union et les caves (propriétaire à l'union, intendants dans les caves et au laboratoire, troisième rôle : instance commune, dépositaire technique ou délégué à la protection des données) | 0,5 |

**Réponse attendue**

Le **DAMA-DMBOK** (2e édition, 2017, révision 2024) est un **référentiel** de bonnes pratiques de gestion des données, organisé en onze domaines de connaissance autour de la gouvernance des données ; il distingue notamment le **propriétaire** des données, responsable métier qui en fixe les définitions, les règles et la qualité attendue, et l'**intendant**, qui les applique au quotidien. Ce n'est ni une norme ni un logiciel, et ses rôles sont illustratifs, non normatifs (annexe 2.4 ; F07 § 8.1-8.2) (0,5 pt). Pour l'union, les domaines prioritaires sont les données de référence, la qualité et les métadonnées (dictionnaire).

Répartition proposée entre l'union et les caves (0,5 pt pour trois rôles avec missions et titulaires) :

| Rôle | Missions | Titulaire |
|---|---|---|
| **Propriétaire** des données des parcelles et des apports | fixe les définitions et les règles (dictionnaire, échelle sanitaire), arbitre les désaccords entre caves, valide les données qui serviront au conseil | Mme Claire BOUSQUIÉRAN, directrice de la production et de la qualité de l'union |
| **Intendants** des données | appliquent les règles à la saisie, contrôlent les apports sans parcelle et les valeurs hors plage, mettent à jour les parcelles chaque hiver, signalent les anomalies | dans chaque cave, un agent de réception ou l'adjoint du directeur, désigné par le directeur de cave ; au laboratoire, un technicien pour le rattachement des prélèvements |
| **Comité des données** des parcelles et des apports | réunit la propriétaire, les neuf directeurs de cave et le responsable du système d'information ; adopte le dictionnaire et l'échelle sanitaire, suit la qualité chaque trimestre, prépare ce qui sera présenté au conseil | instance présidée par la directrice de la production et de la qualité, avant chaque vendange et chaque trimestre |
| **Dépositaire technique** | met en œuvre le référentiel, les échanges, les droits d'accès et la sécurité, sans décider du contenu | M. Sébastien CAUSSINEL, responsable du système d'information |
| **Délégué à la protection des données** | conseille sur les données des adhérents exploitants en nom propre, qui sont des données personnelles (annexe 2.4) : finalités, minimisation, durée de conservation, mise à jour du registre des traitements | délégué de l'union s'il en a été désigné un (désignation facultative ici, mais recommandée), mutualisable avec les caves |

Sont valorisés : la responsabilité métier à l'union, la saisie et le contrôle là où naît la donnée (les caves), et la place des directeurs de cave dans les décisions, qui conditionne l'acceptation des données par les présidents (annexe 2.2 D).

**Réponses tolérées**
- Propriété des données d'apport confiée à chaque directeur de cave pour ses apports, l'union restant propriétaire des données de référence et des définitions communes, si la répartition est justifiée.
- Administrateur des données (CDO) proposé à titre illustratif, sans être présenté comme obligatoire.
- Le candidat peut s'attribuer la coordination du dispositif, comme responsable du projet de refonte.

**Erreurs fréquentes**
- *Norme / référentiel / solution* (`ET-01`, `JUR-S06`) — « installer DAMA-DMBOK » ou « certifier l'union DAMA » ; juste : référentiel de bonnes pratiques.
- *Qualité confiée à l'informatique* — le responsable du système d'information désigné propriétaire des données ; juste : il est dépositaire technique, la propriété est métier.
- *Rôles sans titulaire ni application au cas* (`JUR-T01`) — liste de rôles récitée ; juste : qui, dans l'union ou dans les caves, fait quoi.
- *Organisation normative* — présenter un organigramme de gouvernance comme imposé par le référentiel ; le programme la veut illustrative.
- *Délégué confondu avec un responsable informatique* (`ET-29`) — le délégué ne tient pas les outils et ne décide pas des moyens.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines de connaissance, rôles de propriétaire et d'intendant (repères de l'annexe 2.4) | `dama_dmbok2` / F07 § 8.1-8.2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | données personnelles des adhérents exploitants en nom propre, registre, délégué (repères de l'annexe 2.4) | `rgpd` / F15 | en vigueur |

---

### 2.4 – Chaîne de valeur des données et analyse des apports de la vendange 2026 (4,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ».

**Annexes mobilisées** : annexes 1.1 (plan « ROCALDÈNE 2030 », neuf caves), 2.1 (sources, constats, établissement manuel des tableaux) et 2.2 (tableau par cave, pluies, projet du conseil, positions de M. SOULAGNET et de Mme TARASCOUL, prévision proposée par le prestataire).

**Barème indicatif (4,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de valeur des données définie et appliquée au cas, de la parcelle au conseil : collecte, préparation et rapprochement, stockage et structuration, analyse, restitution, décision | 0,5 |
| a-2 | Apport de la chaîne à la décision de mieux rémunérer la qualité : critères objectivés, comparables entre caves, traçables jusqu'à la parcelle et acceptés par les caves | 0,5 |
| b-1 | Premier constat argumenté, avec sa précaution de lecture | 0,5 |
| b-2 | Deuxième constat argumenté, avec sa précaution de lecture | 0,5 |
| b-3 | Troisième constat argumenté, avec sa précaution de lecture | 0,5 |
| b-4 | Appréciation des deux positions (biais de confirmation de M. SOULAGNET ; critiques fondées mais hypothèse météorologique invérifiable de Mme TARASCOUL) et conséquence pour le conseil | 0,5 |
| c-1 | Méthode recommandée et justifiée : analyse exploratoire, après une analyse descriptive fiabilisée | 0,5 |
| c-2 | Prévision par parcelle prématurée : deux arguments tirés des annexes | 0,5 |
| d | Deux représentations visuelles, l'une pour le conseil, l'autre pour les directeurs de cave, chacune avec son message et le piège de lecture à éviter | 0,5 |

**Réponse attendue**

*2.4 a) – La chaîne de valeur des données, de la parcelle au conseil*

La **chaîne de valeur des données** décrit les étapes par lesquelles une donnée brute devient une information utile à la décision : collecte, préparation (nettoyage, rapprochement), stockage et structuration, analyse, restitution, puis décision et action ; la valeur se crée à chaque étape et se perd au maillon le plus faible (F08 § 1). Appliquée au cas (0,5 pt) :
1. **Collecte** : à la parcelle (fichier des parcelles, sondes, stations, observations des techniciens), à la réception (bon d'apport : poids, degré, état sanitaire, parcelle), au laboratoire (acidité, pH) et aux assemblages (part retenue pour les cuvées haut de gamme) ;
2. **Préparation** : rapprochement par les identifiants uniques du référentiel (question 2.2), conversion supprimée par l'unité commune, fusion des doublons, rattachement des prélèvements orphelins, traitement des apports sans parcelle ;
3. **Stockage et structuration** : base d'analyse de l'union organisée selon le modèle de la question 2.1, historisée vendange après vendange ;
4. **Analyse** : comparaisons par cave, par cépage, par secteur et par parcelle, croisements entre état sanitaire, pluie, rendement et destination des vins ;
5. **Restitution** : représentations commentées pour le conseil et pour chaque cave (d), avec leurs précautions ;
6. **Décision** : choix par le conseil des critères de qualité communs et de leur calendrier.

**Apport à la décision** (0,5 pt) : aujourd'hui, la chaîne est rompue dès la collecte (mesures non homogènes, un tiers des volumes sans parcelle) et la préparation est manuelle (neuf extractions, tableaux établis à la main) ; toute rémunération de la qualité serait contestée, comme le montre Mme TARASCOUL. Une chaîne maîtrisée permet au conseil de fonder les critères de qualité sur des données **définies en commun, comparables entre les neuf caves, traçables jusqu'à la parcelle et acceptées** par les caves qui les produisent ; elle permet d'apprécier à l'avance l'effet de chaque critère sur chaque cave et de suivre ensuite ses effets, au service de la deuxième priorité du plan « ROCALDÈNE 2030 ». Les modalités de calcul ne relèvent pas de la question.

*2.4 b) – Trois constats argumentés et leurs précautions* (0,5 pt par constat avec sa précaution ; trois constats parmi les quatre suivants)

1. **L'état sanitaire paraît nettement plus dégradé dans l'Aude** : 15 % à 25 % des apports dans trois caves de l'Aude (PECHAUROUX 25 %, CABRISSAC 20 %, LAURADEL 15 %), 10 % à VALCROZIÈRES, contre 3 % à 6 % dans les cinq caves de l'Hérault ; les deux stations de l'Aude ont relevé 70 et 110 mm de pluie du 10 au 25 septembre, contre 20 et 30 mm dans l'Hérault. *Hypothèse* : les pluies de septembre ont favorisé les maladies. *Précaution* : les échelles diffèrent (« dégradé » couvre les notes 3 à 5 sur cinq dans l'Aude, la seule note 3 sur trois dans l'Hérault), les notes sont souvent posées par des saisonniers sans définition écrite, et les deux caves les plus touchées (PECHAUROUX, CABRISSAC) n'ont pas de station : l'écart est en partie un **effet de mesure**, et la pluie une hypothèse non vérifiée pour elles.
2. **Les caves aux rendements les plus faibles fournissent le plus de vins haut de gamme** : SAINT-BRÉZIAN (45 hl/ha, 14,0 % vol., 30 % en haut de gamme), TERRAGOUSSE et VALCROZIÈRES (50 hl/ha, 20 %), contre CAUSSELAC (70 hl/ha, 5 %). *Hypothèse* : des rendements plus faibles donnent des raisins plus concentrés, mieux valorisés. *Précaution* : c'est une **corrélation**, non une causalité ; un **facteur commun** (situation des vignes, âge des vignes, cépages) peut expliquer à la fois le faible rendement et la qualité ; surtout, la part haut de gamme est **décidée par l'union** selon la qualité des cuves et ses besoins commerciaux (environ 44 milliers d'hl, soit environ 12 % de la vendange) : elle mesure aussi les choix de l'union, comme le dit Mme TARASCOUL ; enfin, les fichiers des parcelles n'étant pas à jour (constat 5), aucun rendement ne peut encore être calculé par parcelle.
3. **La traçabilité jusqu'à la parcelle est inégale et faible là où l'état sanitaire est le plus dégradé** : environ 62 % des volumes sont rattachés à une parcelle, de 95 % à SAINT-BRÉZIAN à 30 % à PECHAUROUX et 40 % à CABRISSAC ; dans l'Aude, moins de la moitié des volumes l'est. *Conséquence* : une reconnaissance de la qualité **par parcelle** est impossible aujourd'hui pour plus d'un tiers de la vendange. *Précaution* : les données manquantes **ne sont pas réparties au hasard** (biais de sélection) : les moyennes calculées sur les seuls apports rattachés représentent mal les caves les moins renseignées.
4. **Le degré, critère actuel de rémunération, est un indicateur ambigu de la qualité** : il va de 12,5 à 14,0 % vol. et suit la part haut de gamme, mais le plan « ROCALDÈNE 2030 » veut adapter l'offre au changement climatique, ce qui ne pousse pas à récompenser toujours plus de degré. *Précaution* : les degrés de LAURADEL et de CABRISSAC sont convertis à partir des sucres, et une moyenne par cave masque la dispersion entre parcelles et entre cépages.

Précautions communes, valorisées si elles sont citées : **une seule vendange** (aucune tendance), données **agrégées par cave** (rien sur les parcelles ni les viticulteurs), tableau **établi à la main** pour la première fois.

**Appréciation des deux positions** (0,5 pt) : M. SOULAGNET lit le tableau dans le sens qui favorise sa cave (**biais de confirmation**) et en tire une conclusion que les données ne portent pas : la part haut de gamme dépend des choix de l'union, et l'état sanitaire n'est pas mesuré de la même façon partout. Mme TARASCOUL relève à juste titre deux défauts de comparabilité (échelles, part haut de gamme décidée par l'union), mais son explication par la pluie n'est pas vérifiable pour sa cave, sans station, et ne vaut pas preuve. Conclusion pour le conseil : ce tableau peut ouvrir le débat, il ne peut pas fonder une rémunération ; il faut d'abord des mesures communes (dictionnaire, échelle, parcelle obligatoire) dès la vendange 2027, puis décider sur des données comparables, éventuellement après une année d'observation.

*2.4 c) – Méthode d'analyse et prévision par parcelle*

**Méthode** (0,5 pt) : l'annexe 2.2 relève de l'analyse **descriptive** (moyennes et parts par cave, ce qui s'est passé), encore fragile. L'étape suivante est une analyse **exploratoire** : au niveau de l'apport et de la parcelle, rechercher les profils et les facteurs associés à la qualité (cépage, âge des vignes, secteur, pluie, rendement, date d'apport), repérer les valeurs aberrantes, et tester les hypothèses du b) (rôle de la pluie, effet de l'échelle, effet du rendement). Elle sert la question du conseil (quels critères de qualité retenir et sont-ils équitables entre caves) et reste explicable aux présidents. Elle suppose les données harmonisées de la question 2.2 ; sur la vendange 2026, elle se limite aux caves et aux apports rattachés.

**Prévision par parcelle prématurée** (0,5 pt pour deux arguments, parmi les suivants) :
1. **Pas d'historique fiable au niveau de la parcelle** : une seule vendange rassemblée, à la main ; identifiants de parcelle non uniques ; plus d'un tiers des volumes sans parcelle ; un modèle de prévision apprend sur des exemples passés, qui n'existent pas.
2. **Des données de qualité non comparables** : la variable à prévoir (l'état sanitaire, le degré) est mesurée sur des échelles et dans des unités différentes ; le modèle apprendrait les différences de notation entre caves plutôt que la qualité.
3. **Une couverture météorologique trop partielle** : quatre stations pour neuf secteurs, des sondes dans 30 parcelles sur 11 000, des observations dispersées dans trois tableurs personnels.
4. **Un usage à fort enjeu et peu explicable** : fixer des primes avant les vendanges sur une prévision opaque, pour 1 400 adhérents, serait contesté par les caves dès la première erreur ; la décision doit rester humaine et fondée sur des critères compris.
La prévision pourra être reconsidérée après plusieurs vendanges de données propres, comme aide aux techniciens plutôt que comme base de rémunération.

*2.4 d) – Deux représentations visuelles* (0,5 pt)

| Destinataire | Représentation | Message | Piège à éviter |
|---|---|---|---|
| Conseil de l'union | barres horizontales triées par cave de la part des apports à l'état sanitaire dégradé (à partir de la vendange 2027, sur l'échelle commune ; pour 2026, en séparant les deux échelles), avec la part des volumes rattachés à une parcelle affichée à côté (ou nuage de points rendement / part haut de gamme, une bulle par cave proportionnelle au volume) | où sont les écarts de qualité et quelle confiance leur accorder | comparer des notes d'échelles différentes ; axe tronqué qui grossit les écarts ; lire une corrélation comme une causalité ; volumes absolus au lieu de taux |
| Directeurs de cave | carte des parcelles de la cave colorée selon l'état sanitaire moyen des apports (ou histogramme de la répartition des apports de la cave par note, comparé à celle de l'union) | quelles parcelles et quels secteurs améliorer ou mieux renseigner | carte en valeurs brutes, qui fait ressortir les grandes parcelles ; couleurs non signifiantes ; parcelles sans apport rattaché laissées vides sans le signaler |

**Réponses tolérées**
- Chaîne de valeur présentée selon les étapes de la chaîne décisionnelle (collecte, extraction, transformation et chargement, entrepôt, restitution), si la décision du conseil la termine.
- Autres constats tirés de l'annexe 2.2 (CAUSSELAC, première cave en volume, la moins valorisée ; écart de structure entre Hérault et Aude) s'ils sont assortis d'une précaution.
- Position recommandant une rémunération limitée à un critère déjà fiable (par exemple l'apport rattaché à une parcelle), si elle est argumentée.
- Analyse descriptive fiabilisée recommandée pour la vendange 2027, avant l'exploratoire, si le candidat le justifie par la qualité des données.
- Autres représentations adaptées (barres empilées à 100 % par note sanitaire, carte choroplèthe en taux), si le message et le piège sont précisés.

**Erreurs fréquentes**
- *Corrélation = causalité* (`ET-26`) — « les faibles rendements font la qualité » ou « la pluie explique l'état sanitaire de l'Aude » ; juste : hypothèses à vérifier, facteurs communs et effets de mesure examinés.
- *Extrapolation sans précaution* (`JUR-D06`) — conclusions tirées d'une seule vendange ; juste : une année ne fait pas une tendance.
- *Interprétation isolée de la décision* (`JUR-T03`) — constats décrits sans conséquence pour le conseil ; juste : chaque constat dit ce que le conseil peut ou ne peut pas décider.
- *Science des données = BI* (`ET-25`) — confondre l'analyse descriptive du tableau et la prévision du prestataire ; juste : finalités et exigences de données différentes.
- *Calculs inutiles ou hors sujet* (`JUR-T07`) — moyennes pondérées recalculées, barème de primes construit ; juste : interpréter les écarts lus, sans calcul de rémunération.
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — le service de prévision présenté comme un assistant conversationnel ; juste : une prévision apprend des régularités sur des données passées.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne décisionnelle et chaîne de valeur des données | étapes, points de vigilance | F08 § 1 | notion de cours |
| Analyses descriptive, exploratoire, prédictive | finalités, prérequis, limites | F08 § 2 | notion de cours |
| Choix des représentations, biais de lecture, corrélation et causalité | graphiques adaptés, pièges | F08 § 5 | notion de cours |

---

### 2.5 – Le projet d'authentification des cuvées exportées (2,5 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.a` « Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain » ; `3.3.d` « Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO ».

**Annexes mobilisées** : annexes 1.1 (export 25 % du chiffre d'affaires, budget du SI de 2 200 k€, plan « ROCALDÈNE 2030 » et empreinte environnementale), 2.3 (problème signalé, proposition de SCELLAVIN, coûts, alternative, avis) et 2.4 (MiCA, RGPD, ISO 22739).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Blockchain définie (registre distribué, consensus, inaltérabilité pratique, confiance sans tiers) et distinguée d'une base centralisée ; projet situé dans la typologie : certification d'authenticité et traçabilité, au moyen de jetons non fongibles | 0,5 |
| b-1 | Deux opportunités et trois risques ou limites tirés de l'annexe 2.3 (dont l'oracle : la chaîne garantit l'enregistrement, pas la bouteille) | 0,5 |
| b-2 | Comparaison avec l'alternative : coûts de tête sur trois ans (930 k€ contre 330 k€), apports et limites du code signé | 0,5 |
| b-3 | Recommandation argumentée et conditionnée | 0,5 |
| c | Condition d'exclusion du champ de MiCA (jetons réellement uniques et non fongibles) et respect du RGPD pour les prénoms et les villes des consommateurs ; la remarque sur la revente séparée est valorisée | 0,5 |

**Réponse attendue**

*2.5 a) – Blockchain et typologie* (0,5 pt)

Une **blockchain** est un registre distribué, répliqué entre plusieurs nœuds, dont les blocs de transactions sont chaînés par des empreintes cryptographiques et validés par un mécanisme de consensus (ici la preuve d'enjeu) ; elle permet à des acteurs qui ne se font pas confiance de partager une information horodatée et pratiquement inaltérable, **sans tiers de confiance**. Une **base de données centralisée** est tenue par un administrateur unique (ici l'union), qui peut la modifier et en qui les utilisateurs doivent avoir confiance ; elle est plus simple, moins coûteuse et plus rapide (F11 § 1 ; ISO 22739:2024 pour le vocabulaire).

Le projet de SCELLAVIN relève de deux usages de la typologie : la **certification d'authenticité** (preuve que la bouteille vient de l'union) et la **traçabilité** (historique des détenteurs successifs), au moyen d'un **jeton non fongible (NFT)** par bouteille, sorte de double numérique de l'objet physique. Il ne relève ni de la finance décentralisée ni de la tokenisation d'un actif financier ; la revente envisagée des jetons sur une place de marché le ferait glisser vers un usage spéculatif.

*2.5 b) – Opportunités, risques et comparaison avec l'alternative*

**Deux opportunités** (parmi les suivantes) :
1. une **preuve d'origine vérifiable par des tiers** sans compte chez l'union ni confiance dans son site, ce que demande le distributeur canadien ;
2. un **historique horodaté des détenteurs**, qui permettrait de repérer des bouteilles sorties du circuit prévu ;
3. une **étiquette connectée** qui se détruit au décollage, plus difficile à copier qu'une étiquette imprimée ;
4. une **image de modernité** auprès des importateurs asiatiques (M. SALVERNAC), à ne pas surestimer.

**Trois risques ou limites** (0,5 pt avec les opportunités, parmi les suivants) :
1. **Le problème de l'oracle** : la blockchain garantit que l'enregistrement n'a pas été modifié, non qu'il est vrai, ni que la bouteille est celle qui a été enregistrée (« si nos données de départ sont fausses, la blockchain les gardera fausses pour toujours ») ; la protection contre la copie tient à l'étiquette, non à la blockchain.
2. **Un seul acteur écrit l'origine** : l'union est la seule source des informations de départ ; selon la grille d'opportunité (plusieurs acteurs qui écrivent et ne se font pas confiance), une base centralisée tenue par l'union, propriétaire de la marque, suffit (F11 § 2.2).
3. **Des données personnelles inscrites sur une blockchain publique** : prénoms et villes des consommateurs ne pourraient plus être effacés, ce qui heurte la minimisation et l'effacement prévus par le RGPD (annexe 2.4).
4. **Coût et proportionnalité** : environ 2 000 bouteilles contrefaites signalées, soit environ 0,3 % des 600 000 bouteilles exportées, pour un projet de 930 k€ sur trois ans.
5. **Dépendance** envers une jeune entreprise qui choisit seule la blockchain et tient la place de marché ; avenir des jetons et de la vérification si elle disparaît.
6. **Empreinte environnementale** : la preuve d'enjeu consomme peu d'énergie, mais une puce électronique jetable sur 600 000 bouteilles par an produit des déchets électroniques, à rebours de la priorité du plan « ROCALDÈNE 2030 » sur l'empreinte environnementale.

**Comparaison avec l'alternative** (0,5 pt) : estimation de tête, sans actualisation :
- SCELLAVIN : 120 + 90 + 3 × (180 + 60) = 210 + 720 = **930 k€** sur trois ans, soit environ 310 k€ par an (environ 14 % du budget annuel du SI de 2 200 k€) ;
- alternative : 150 + 3 × (30 + 30) = 150 + 180 = **330 k€** sur trois ans, soit environ 110 k€ par an (environ 5 % du budget du SI) ; écart : 600 k€.

L'alternative répond au besoin principal (prouver l'origine, lire le code avec un téléphone, signaler un code déjà lu ailleurs), garde les données et la maîtrise à l'union, n'inscrit aucune donnée personnelle dans un registre inaltérable et ne met pas de puce sur chaque bouteille. Ses limites : un code imprimé peut être **copié** sur une fausse bouteille (d'où la détection des lectures multiples, et éventuellement une capsule ou une étiquette inviolable), et les tiers doivent faire confiance au site de l'union, ce qui est acceptable puisque l'union est le producteur et le propriétaire de la marque.

**Recommandation** (0,5 pt) : retenir l'alternative centralisée, en pilote d'une campagne sur le marché de Hong Kong, complétée si besoin par un dispositif inviolable sur la capsule ; mesurer les lectures multiples et les retours des importateurs ; ne pas inscrire de données de consommateurs. Reconsidérer une blockchain, plutôt **permissionnée et partagée avec les importateurs et distributeurs**, seulement si plusieurs acteurs doivent écrire dans le registre sans se fier à l'union et si le coût se justifie. Refuser en tout état de cause la revente séparée des jetons.

*2.5 c) – Cadre réglementaire* (0,5 pt)

D'après les repères de l'annexe 2.4, le règlement (UE) 2023/1114 « MiCA », applicable depuis le 30/12/2024, exclut de son champ les crypto-actifs **uniques et non fongibles** (article 2 § 3) : les jetons de SCELLAVIN y échappent **à condition d'être réellement uniques et non fongibles** : un jeton par bouteille, non interchangeable et non fractionné. La revente des jetons séparément des bouteilles ne relève pas de cette condition, mais elle détacherait la preuve d'authenticité de la bouteille et donnerait au projet un caractère spéculatif ; un avis spécialisé serait utile avant de l'envisager (remarque valorisée, non exigée). Le projet doit en revanche respecter le **RGPD** (applicable depuis le 25/05/2018) pour les prénoms et villes des consommateurs, comme pour les données des adhérents : finalités, minimisation, durée de conservation, effacement, ce qu'une inscription sur une blockchain publique rend impossible. ISO 22739:2024 n'est qu'une norme de vocabulaire : elle ne crée aucune exigence ni certification.

**Réponses tolérées**
- Projet situé seulement dans la traçabilité ou seulement dans la certification, si le rôle du jeton non fongible est expliqué.
- Recommandation de l'étiquette connectée sans blockchain, adossée au registre centralisé de l'union, si le coût et l'empreinte des puces sont discutés.
- Pilote limité du projet de SCELLAVIN sur une cuvée, si le candidat exige l'absence de données personnelles sur la chaîne, la réversibilité et l'abandon de la revente séparée.
- Coûts estimés par an plutôt que sur trois ans, si la comparaison reste juste.

**Erreurs fréquentes**
- *Blockchain = base de données distribuée* (`ET-08`) — « la blockchain est une base partagée plus sûre » ; juste : registre de confiance entre acteurs qui ne se font pas confiance, au prix de la performance.
- *Opportunités sans risques* (`ET-19`) — reprendre l'enthousiasme de M. SALVERNAC sans l'oracle, le coût ni le RGPD.
- *Inaltérabilité = vérité* — croire que l'inscription prouve l'authenticité de la bouteille ; juste : la chaîne garantit l'intégrité de l'enregistrement, pas l'exactitude des données saisies.
- *MiCA appliqué à tout jeton* (`ET-35`) — affirmer que les jetons de SCELLAVIN exigent un agrément ; juste : exclusion des crypto-actifs uniques et non fongibles, sous condition.
- *Analyse juridique, fiscale ou comptable* (`JUR-T07`) — développements sur le statut juridique des jetons ou leur traitement dans les comptes ; juste : s'en tenir aux repères fournis.
- *Énergie oubliée ou exagérée* — preuve d'enjeu confondue avec la preuve de travail ; juste : consommation modérée, mais déchets des puces à prendre en compte.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2023/1114 « MiCA », applicable depuis le 30/12/2024 | définition du crypto-actif, exclusion des crypto-actifs uniques et non fongibles (article 2 § 3) (repères de l'annexe 2.4) | `mica` / F11 § 3 ; `commun/fiches/sapin2_lcbft_mica.md` § 3.1 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | minimisation, effacement, données des consommateurs | `rgpd` / F15 | en vigueur |
| ISO 22739:2024 | vocabulaire des chaînes de blocs et des registres distribués | `iso_22739_2024` / F11 § 3.4 | en vigueur |
| Typologie des usages, grille d'opportunité, limites (oracle, énergie, gouvernance) | analyse du projet | F11 § 1 et 2 | notion de cours |

---

## DOSSIER 3 – ASSURER LA CONTINUITÉ DU SYSTÈME D'INFORMATION PENDANT LES VENDANGES, FIABILISER LES APPORTS ET CHOISIR UN HÉBERGEMENT RESPONSABLE (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Analyse d'impact de la campagne de vendanges | `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers (ici, les processus et la continuité) | 2 |
| 3.2 Le dispositif de continuité et de reprise de la campagne 2027 | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.d` Dispositifs de surveillance et de résilience : IAM, PCA/PRA ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 3 |
| 3.3 Le module de détection des apports anormaux | `4.1.f` Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques | 1,5 |
| 3.4 L'audit du module des apports | `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. | 2 |
| 3.5 Le tableau de bord du système d'information de la campagne | `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) | 1,5 |
| 3.6 Le choix d'un hébergement responsable | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 3 |
| **Dossier 3 – Assurer la continuité du système d'information pendant les vendanges, fiabiliser les apports et choisir un hébergement responsable** |  | **13** |

Répartition indicative : connaissances (analyse d'impact, durée et perte de données maximales admissibles, PCA et PRA, familles de l'IA, audit du système d'information, tableau de bord équilibré, sobriété numérique et stratégie responsable) 2,5 points environ (items 3.1-1, 3.2 a-1, 3.3-1 pour moitié, 3.4 a pour moitié, 3.5-1 pour moitié, 3.6 a-1) ; analyse des annexes et recommandations 10,5 points, soit environ 80 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Analyse d'impact de la campagne de vendanges (2 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ». L'énoncé exclut le volet des états financiers : seuls les processus et la continuité sont attendus. Limite : l'analyse de sécurité technique n'est pas attendue dans le détail.

**Annexes mobilisées** : annexe 3.1 (applications et volumes, incident, fiches des adhérents et des parcelles, acteurs) et annexe 1.1 (calendrier des vendanges, organisation en caves).

**Barème indicatif (2 pts)**

| Item | Attendu | Points |
|---|---|---|
| 1 | Analyse d'impact sur l'activité définie (processus critiques, conséquences d'une interruption selon sa durée, priorités de reprise) ; durée maximale d'interruption admissible (DMIA, ou RTO) et perte de données maximale admissible (PDMA, ou RPO) définies sans inversion | 0,5 |
| 2 | Réception et pesée : processus touchés, criticité maximale, DMIA très courte pour la réception (bascule en mode dégradé), PDMA nulle pour les pesées, justifiées par l'annexe 3.1 | 0,5 |
| 3 | Laboratoire et progiciel de l'union : processus, criticité, DMIA et PDMA justifiées (résultats attendus le lendemain à 8 h, échantillons conservés 48 heures ; commandes et pénalités, sauvegarde de nuit) | 0,5 |
| 4 | Variation de la criticité selon la période (caves et laboratoire en vendanges, progiciel en fin d'année) et conséquence pour le dispositif (calendrier des tests, des maintenances et des priorités de reprise) | 0,5 |

**Réponse attendue**

*Définitions (item 1)*

L'**analyse d'impact sur l'activité** (BIA) identifie les processus critiques d'une organisation et mesure, pour chacun, les conséquences d'une interruption selon sa durée (opérationnelles, financières, d'image, relationnelles) ; elle en déduit les ressources du système d'information dont ils dépendent, leur ordre de reprise et deux objectifs : la **durée maximale d'interruption admissible** (DMIA, en anglais RTO), délai au-delà duquel l'interruption devient inacceptable, et la **perte de données maximale admissible** (PDMA, en anglais RPO), quantité de données, exprimée en durée, que l'on accepte de perdre depuis la dernière copie exploitable (F12 § 4). Elle fonde le plan de continuité et le plan de reprise (question 3.2) et constitue la première étape d'un système de management de la continuité au sens d'ISO 22301:2019 (annexe 3.4). L'incident de GRAUSSELLE montre qu'elle n'a jamais été faite : la dernière copie exploitable avait 78 jours, et personne ne savait qui décidait.

*Trois applications pendant la campagne (items 2 et 3)*

| Application | Processus de l'union ou des caves touchés | Criticité en campagne | DMIA proposée | PDMA proposée |
|---|---|---|---|---|
| Logiciel de réception et de pesée (chaque cave) | réception des apports (pesée, degré, bon remis au viticulteur), affectation de la vendange aux cuves, suivi des cuves, relevés et rémunération des adhérents par leur cave, confiance des adhérents | **maximale** : jusqu'à 900 apports par jour pour les neuf caves, 120 pour la seule cave de CAUSSELAC ; une remorque ne peut attendre longtemps au soleil ; une vendange versée ne peut plus être pesée | pour le **processus** de réception : aucune interruption au-delà d'une heure environ, d'où une bascule en mode dégradé décidée dans les 30 minutes (l'attente habituelle est de 20 minutes, elle a atteint 3 heures) ; pour l'**application** : remise en service dans la journée, 24 heures au plus, car chaque heure en mode dégradé alourdit la ressaisie (385 bons ressaisis en deux jours, 25 erreurs) | **nulle** pour les pesées : aucune pesée ne peut être refaite ; chaque apport doit laisser une trace hors du serveur au moment même de la pesée (double du bon, copie continue des données) ; les fiches des adhérents et des parcelles tolèrent au plus une journée, et non les 78 jours écoulés depuis le 15 juin |
| Logiciel du laboratoire (union) | analyse des moûts, conduite des fermentations et des cuves par les œnologues | **forte** : environ 22 000 analyses, jusqu'à 1 000 par jour ; résultats attendus le lendemain à 8 h | environ **12 heures** : les analyses de la journée peuvent être reportées sur la nuit, pas au-delà du lendemain matin | environ **24 heures** : les échantillons, conservés 48 heures au froid, permettent de refaire les analyses perdues, à condition de conserver leur rattachement au bon d'apport |
| Progiciel de gestion de l'union | commandes, conditionnement, expéditions, facturation | **moyenne** en septembre et octobre (environ 40 commandes par jour), **forte** en novembre et décembre (environ 80 commandes par jour, pénalités de retard des enseignes) | **une journée ouvrée** pendant les vendanges : les commandes reçues peuvent être saisies le lendemain ; **quelques heures** en fin d'année | **24 heures** : la sauvegarde de nuit suffit, les commandes de la journée pouvant être reconstituées à partir des messages reçus ; mais la copie est conservée dans la même salle (annexe 3.3), ce qui fait de cette PDMA une promesse fragile |

*Variation de la criticité au cours de l'année (item 4)*

La criticité n'est pas une propriété fixe de l'application : elle dépend du calendrier des processus. Le logiciel de réception est vital de fin août à mi-octobre et presque secondaire le reste de l'année (suivi des cuves, relevés) ; le laboratoire suit le même rythme ; le progiciel de l'union est au contraire le plus critique en novembre et décembre, au pic des commandes de fin d'année. Conséquences : (1) les objectifs de reprise et les moyens de secours se fixent **par période** ; (2) les tests de restauration, l'exercice et les changements de version se placent **avant** la campagne (au printemps et en juillet), jamais pendant les vendanges, et la maintenance lourde du progiciel avant novembre ; (3) en cas de crise simultanée pendant les vendanges, la réception des caves passe avant le progiciel de l'union, alors que l'organisation actuelle (équipe informatique tournée vers le progiciel, caves sans informaticien) fait l'inverse. L'analyse est à revoir chaque année avec les directeurs de cave et la directrice de la production.

**Réponses tolérées**
- DMIA et PDMA différentes de celles du tableau, si elles sont justifiées par les données de l'annexe 3.1 (une DMIA de quelques heures pour l'application de réception, à condition que le mode dégradé couvre le processus).
- Échelle de criticité annoncée par le candidat (faible, moyenne, forte, vitale) ou cotation de 1 à 4.
- Messagerie ou suivi des cuves analysés en plus des trois applications demandées.
- Vocabulaire RTO et RPO employé à la place de DMIA et PDMA.

**Erreurs fréquentes**
- *RTO et RPO inversés ou confondus* (`ET-03`, `JUR-S02`) — « la PDMA est le délai de reprise » ; juste : la DMIA mesure une durée d'arrêt, la PDMA l'âge de la dernière copie exploitable.
- *Criticité unique pour toute l'année* (`JUR-T01`) — juste : la criticité suit le calendrier des vendanges et des ventes.
- *Analyse d'impact récitée sans les chiffres de l'annexe* (`JUR-T08`, `ET-39`) — juste : 900 apports par jour, 3 heures d'attente, 385 bons ressaisis, 48 heures de conservation des échantillons.
- *Dérive vers les états financiers ou la rémunération des adhérents* (périmètre de la question) — juste : processus et continuité seulement.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Analyse d'impact sur l'activité, DMIA (RTO), PDMA (RPO) | définitions et application | F12 § 4 | notion de cours |
| ISO 22301:2019 | système de management de la continuité d'activité, analyse d'impact | `iso_22301_2019` ; F12 § 4 | en vigueur |

---

### 3.2 – Le dispositif de continuité et de reprise de la campagne 2027 (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » (ici, le pilotage par la direction) ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique n'est pas exigée ; le lien avec les normes se fait sans entrer dans les certifications.

**Annexes mobilisées** : annexe 3.1 (incident, acteurs, pilotage), annexe 3.4 (ISO 22301, guide d'hygiène de l'ANSSI, EBIOS Risk Manager) et annexe 1.1 (organigramme, conseil de l'union, directeurs de cave).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | PCA (maintenir l'activité, au besoin en mode dégradé) et PRA (rétablir le système d'information et revenir à la normale) distingués et articulés, appuyés sur l'analyse d'impact | 0,5 |
| a-2 | Mode dégradé de la réception (documents numérotés en double, décision de bascule, affectation aux cuves, ressaisie contrôlée), relié à l'incident | 0,5 |
| a-3 | Règles de sauvegarde (fréquence en campagne, copie hors ligne et hors site) et tests de restauration avant la campagne, reliés à l'incident | 0,5 |
| a-4 | Exercice avant les vendanges : scénario, participants, date, mesures et retour d'expérience | 0,5 |
| b-1 | Rôles et responsabilités de l'union, des caves, du prestataire local et de l'éditeur, sans doublon ni vide (chaîne d'alerte, décision en crise) | 0,5 |
| b-2 | Pilotage par la direction : instance, décisions (validation du dispositif, décision avant la campagne, décisions de crise), compte rendu au conseil | 0,5 |

**Réponse attendue**

*3.2 a) – PCA, PRA et dispositif de la réception*

Le **plan de continuité d'activité** (PCA) organise le **maintien** des activités critiques pendant une crise, au besoin en **mode dégradé** : pendant que le serveur d'une cave est indisponible, la réception des apports continue. Le **plan de reprise d'activité** (PRA) organise le **rétablissement** du système d'information et le **retour à la normale** : restaurer le serveur à partir d'une sauvegarde saine, ressaisir et contrôler les données, revenir au fonctionnement courant. Les deux découlent de l'analyse d'impact (question 3.1) : le PCA tient la DMIA du processus de réception (une heure), le PRA la DMIA de l'application (24 heures) et la PDMA (nulle pour les pesées). Un plan non testé n'offre aucune garantie (F12 § 4).

| Élément du dispositif | Contenu proposé pour la campagne 2027 | Enseignement de septembre 2026 |
|---|---|---|
| **Mode dégradé de la réception** (a-2) | dans chaque cave, un kit de réception prêt avant la campagne : carnets de bons pré-numérotés en double exemplaire (un pour le viticulteur), fiche de pesée et de degré à remplir, consignes d'affectation aux cuves affichées, fiche réflexe ; bascule décidée par le directeur de cave dans les 30 minutes ; saisonniers formés au mode dégradé ; ressaisie à deux (saisie et contrôle) dès le retour du logiciel, avec rapprochement des doubles et relevé envoyé à l'adhérent pour vérification | feuilles volantes sans numérotation, 3 heures d'attente, 385 bons ressaisis et 25 erreurs relevées par les adhérents |
| **Sauvegardes et tests des restaurations** (a-3) | pendant la campagne, sauvegarde au moins quotidienne des données de chaque cave, et copie des pesées en fin de journée ; le double de chaque bon, imprimé et conservé par la cave, garantit qu'aucune pesée ne se perd entre deux copies (PDMA nulle) ; une copie **déconnectée** (hors ligne) et une copie **hors du site** de la cave (à l'union ou chez un hébergeur), conformément au guide d'hygiène de l'ANSSI (annexe 3.4) ; test de restauration complet de chaque cave avant fin juillet, puis vérification quotidienne de la sauvegarde pendant la campagne ; mises à jour des serveurs et des postes faites avant la campagne | disque de sauvegarde branché en permanence et chiffré avec le serveur ; dernière copie du 15 juin ; aucune restauration jamais essayée ; trois autres caves dans la même situation |
| **Exercice avant les vendanges** (a-4) | en juillet 2027, avant l'ouverture des quais fin août : scénario « serveur de la cave chiffré à 6 h 30 un jour de pointe » ; participants : directeur et chef de quai, saisonniers déjà recrutés, équipe informatique de l'union, prestataire, éditeur ; déroulé : alerte, bascule en mode dégradé chronométrée, restauration réelle sur un serveur de secours, ressaisie d'un lot de bons ; au moins une cave par éditeur, toutes les caves sur deux ans ; mesures : délai de bascule, délai de restauration, erreurs de ressaisie ; retour d'expérience écrit et mise à jour du plan | aucune procédure écrite ; décision de payer ou non la rançon prise le lendemain ; union prévenue à 10 h ; assistance de l'éditeur fermée avant 9 h |

L'ensemble suit la logique d'amélioration continue d'ISO 22301:2019 (analyse d'impact, stratégie, plans, exercices, revue), sans viser une certification ; EBIOS Risk Manager peut éclairer les scénarios de menace impliquant les prestataires et les éditeurs.

*3.2 b) – Rôles, responsabilités et pilotage*

| Acteur | Rôles et responsabilités dans le dispositif (b-1) |
|---|---|
| **Union** (direction générale et responsable du système d'information) | porte la politique de continuité commune, conduit l'analyse d'impact, fournit le modèle de PCA et de kit dégradé, organise la copie hors site des sauvegardes des caves et leur vérification quotidienne, assure une permanence informatique de 7 h à 21 h pendant les vendanges, tient le registre des incidents et le tableau de bord (question 3.5), coordonne la cellule de crise |
| **Caves** (directeur, avec le président informé) | appliquent le PCA local, tiennent le kit dégradé prêt, forment les saisonniers, déclenchent le mode dégradé, alertent l'union dans les 15 minutes, participent à l'exercice ; le directeur de cave reste responsable de la réception de sa cave |
| **Prestataire informatique local** (TRAMONTEL Informatique et les autres prestataires) | met en place les sauvegardes et leur copie déconnectée, contrôle leur bon déroulement, restaure en cas d'incident avec un délai d'intervention garanti pendant les vendanges, tient un serveur de secours prêt ; rend compte à l'union, et pas seulement à la cave |
| **Éditeur du logiciel de cave** (MOUSTERAL Logiciels et les trois autres) | assistance étendue pendant les vendanges (dès 7 h, week-end compris), procédure documentée de réinstallation et de restauration de son logiciel, participation aux tests et à l'exercice, information sur les mises à jour à faire avant la campagne |

Le **pilotage** (b-2) relève de la direction de l'union, parce que la réception est un système critique pour toutes les caves et pour la troisième priorité du plan « ROCALDÈNE 2030 » :
- **instance** : un comité de campagne présidé par Mme MAZERANDE (directrice de la production et de la qualité, directeur administratif et financier, responsable du système d'information, deux ou trois directeurs de cave), mensuel de mai à août, puis point quotidien pendant les vendanges à partir du tableau de bord ;
- **décisions** : adopter la politique de continuité et les règles communes (sauvegardes, kit dégradé, chaîne d'alerte) ; décider fin juillet, au vu des tests et de l'exercice, si chaque cave est prête et, sinon, des mesures d'appoint ; arbitrer les moyens (permanence, serveur de secours) ; en crise, la cellule de crise décide selon des règles fixées à l'avance, dont la position de principe sur le paiement d'une rançon, arrêtée par le conseil de l'union et reprise par le conseil de chaque cave, ce qui évite le flottement de septembre 2026 ;
- **compte rendu** : Mme MAZERANDE présente au conseil, à chaque réunion, l'état de préparation (caves testées, exercice réalisé), puis le bilan de la campagne (incidents, indicateurs), comme le prévoit le plan ; le conseil approuve la politique de continuité.

**Réponses tolérées**
- Site de secours ou poste de réception de secours fourni par l'union, version hors ligne du logiciel demandée à l'éditeur, impression autonome des tickets du pont-bascule : acceptés comme éléments du mode dégradé.
- Règle 3-2-1 des sauvegardes citée.
- Désignation d'un responsable de la continuité ou d'un responsable de la sécurité des systèmes d'information rattaché à la direction générale.
- Instance confiée au comité de direction élargi aux directeurs de cave.

**Erreurs fréquentes**
- *PCA et PRA confondus* (`ET-02`, `JUR-S02`) — « le PRA est le mode dégradé » ; juste : le PCA maintient l'activité, le PRA rétablit le système et ramène à la normale.
- *Dispositif purement technique* (`JUR-T12`, `JUR-S06`) — paramétrage des sauvegardes ou des serveurs ; juste : organisation, rôles, décisions, tests.
- *Plan non testé* (`JUR-S08`) — juste : exercice et restaurations réelles avant la campagne.
- *Rôles flous ou sans les prestataires* (`JUR-T08`) — juste : prestataire et éditeur ont des engagements pendant les vendanges et rendent compte à l'union.
- *Politique de sécurité complète ou gestion des identités développées* (périmètre de la question) — juste : continuité et reprise de la réception.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| PCA, PRA, exercices, rôles | définitions, gouvernance des systèmes critiques | F12 § 1 et 4 | notion de cours |
| ISO 22301:2019 | management de la continuité, exercices et tests | `iso_22301_2019` ; F12 § 4 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | sauvegardes, copie hors ligne, restaurations testées | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager, version 1.5 | scénarios impliquant prestataires et éditeurs (toléré) | `ebios_rm_1_5` ; F12 § 2 | en vigueur |

---

### 3.3 – Le module de détection des apports anormaux (1,5 point)

**Référence au programme**
- §4.1 : `4.1.f` « Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques ». Limites : l'IA s'analyse dans ses effets métiers ; le développement d'algorithmes d'apprentissage automatique n'est pas attendu.

**Annexes mobilisées** : annexe 3.2 (constats, proposition et test du module) et annexe 3.1 (volumes, incident de GRAUSSELLE).

**Barème indicatif (1,5 pt)**

| Item | Attendu | Points |
|---|---|---|
| 1 | Module situé dans l'apprentissage automatique (détection d'anomalies), distingué de l'IA générative ; deux apports pour la détection et la prévention, appliqués au cas | 0,5 |
| 2 | Trois limites, sur les données d'apprentissage, les faux positifs et le contrôle humain, chacune appuyée sur l'annexe 3.2 | 0,5 |
| 3 | Recommandation motivée sur l'adoption pour 2027 et deux conditions au moins | 0,5 |

**Réponse attendue**

*Famille d'IA et apports (item 1)*

Le module relève de l'**apprentissage automatique** : il apprend, à partir des apports passés, un profil d'apport « normal » et attribue à chaque nouvel apport un signal d'écart (**détection d'anomalies**) ; il produit une alerte, non un contenu, et ne relève donc pas de l'**IA générative**, qui génère du texte ou des images (F13 § 1). Deux apports :
1. **Un examen exhaustif et immédiat** : aujourd'hui, aucun des environ 20 000 apports n'est contrôlé après la pesée ; le module examine chaque apport au moment de la pesée, quand une erreur peut encore être corrigée avant que la vendange soit versée (nouvelle mesure du degré, vérification de l'adhérent ou de la parcelle).
2. **Un ciblage des contrôles humains et un effet dissuasif** : le test a fait apparaître, à GRAUSSELLE, 20 erreurs ou anomalies réelles que personne n'avait vues ; savoir que les écarts sont repérés décourage les manipulations.

*Trois limites (item 2)*

- **Données d'apprentissage** : le module a appris sur trois caves seulement, sur trois vendanges (2023 à 2025), avec un seul logiciel ; les six autres caves ont d'autres logiciels et d'autres pratiques ; il ignore les situations nouvelles (pluies de la mi-septembre 2026, première récolte d'un cépage planté en 2023) ; surtout, il apprend sur des données dont la fiabilité est en cause (600 bons modifiés après la pesée sans trace, bons ressaisis après l'incident) : il risque d'apprendre comme « normal » ce qui est anormal. Le chiffre de « 9 apports anormaux sur 10 » n'est pas vérifié sur les données de l'union.
- **Faux positifs** : sur 300 apports signalés, 20 seulement étaient de vraies anomalies, soit environ 7 % ; à l'échelle des neuf caves, un taux de 15 % représenterait environ 3 000 alertes par campagne, jusqu'à 135 par jour de pointe (15 % de 900 apports), qu'aucune équipe ne peut examiner pendant les vendanges : les alertes seraient ignorées, ou bien elles retarderaient la réception.
- **Contrôle humain** : le blocage automatique de tout bon signalé arrêterait la réception, ce qui recrée le problème de continuité de la question 3.1, et retirerait la décision à un humain ; personne n'est désigné pour examiner les alertes ni pour en répondre auprès des adhérents, qui voudront comprendre pourquoi leur apport est bloqué ; enfin, le module ne voit que la valeur finale du degré : les six bons modifiés à la main n'ont pas été signalés. Il ne remplace donc pas les contrôles de base (accès nominatifs, séparation des tâches, journal des modifications : question 3.4).

*Recommandation (item 3)*

Ne pas déployer le module dans les neuf caves pour la campagne 2027, ni avec le blocage automatique. Priorité aux contrôles de base, dont l'audit de juin 2027 dira l'état. Un pilote est possible en 2027 dans les trois caves équipées par MOUSTERAL Logiciels, à quatre conditions : (1) **alerte sans blocage**, examinée par une personne désignée (œnologue ou directrice de la production), dont la décision est tracée ; (2) **mesure** du taux de vraies anomalies parmi les signalements, avec un seuil d'alerte réglé pour rester examinable ; (3) **apprentissage** sur des données fiabilisées et représentatives des neuf caves avant toute généralisation ; (4) **explication** aux adhérents de ce que fait le module. Le coût affiché (20 k€ puis 15 k€ par an) est modeste, mais le temps d'examen des alertes est un coût caché à prévoir.

**Réponses tolérées**
- Apprentissage supervisé ou non supervisé évoqué sans erreur, sans développement.
- Adoption immédiate recommandée, si elle est assortie de l'absence de blocage, d'un examen humain désigné et de la mise en place préalable des contrôles de base.
- Autres apports : repérage des tares de remorques anciennes, des parcelles ou des adhérents incohérents.

**Erreurs fréquentes**
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — juste : le module classe et signale, il ne génère pas de contenu.
- *Opportunités sans limites* (`ET-19`, `JUR-T03`) — reprendre la plaquette (« 9 sur 10 ») ; juste : le test montre environ 7 % de vraies anomalies parmi les signalements.
- *Fonctionnement interne du modèle décrit* (hors programme) — juste : effets métiers, données, supervision.
- *IA présentée comme un substitut aux contrôles* (`JUR-T11`) — juste : elle complète les accès nominatifs, la séparation des tâches et la journalisation.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie de l'IA, apprentissage automatique, IA générative | familles, distinction | F13 § 1 | notion de cours |
| Risques de l'IA (biais, données, dépendance), supervision humaine | limites et conditions | F13 § 3 et 4 | notion de cours |

---

### 3.4 – L'audit du module des apports (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la conformité financière et comptable n'est pas traitée.

**Annexes mobilisées** : annexe 3.2 (constats, demande de la directrice générale), annexe 3.1 (éditeurs, acteurs), annexe 3.4 (ISO/IEC 27001:2022 et 27002:2022) et annexe 1.1 (neuf caves, organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Audit du système d'information défini (examen indépendant et méthodique, au regard d'un référentiel, recommandations) ; quatre étapes appliquées au cas, de la cartographie du processus à la restitution | 0,5 |
| b | Trois risques tirés de l'annexe 3.2, chacun avec le contrôle attendu et la manière d'en vérifier le fonctionnement ; 0,5 dès deux risques complets | 1 |
| c | Trois critères de performance et de conformité, chacun illustré par un point de contrôle du module des apports | 0,5 |

**Réponse attendue**

*3.4 a) – Définition et démarche*

L'**audit du système d'information** est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel (normes, règles internes, engagements), la performance, la sécurité, la fiabilité et la conformité d'un système ou d'un processus, et formule des recommandations (F10 § 1.1). Ici, il porte sur un processus applicatif, de la pesée au relevé adressé à l'adhérent, dans les neuf caves.

| Étape | Objet dans le cas |
|---|---|
| 1. Cadrage et prise de connaissance | objectifs fixés par Mme MAZERANDE (confiance des adhérents et du conseil dans les chiffres des apports) ; périmètre : le module des apports des quatre logiciels dans les neuf caves ; référentiel : mesures d'ISO/IEC 27001:2022 sur les droits d'accès, la journalisation et la séparation des tâches, détaillées par le guide ISO/IEC 27002:2022, et règles de réception de l'union ; calendrier : conclusions en juin 2027 ; interlocuteurs : directrice de la production, directeurs de cave, éditeurs |
| 2. Cartographie du processus de réception | étapes (identification de l'adhérent et de la parcelle, pesée, déduction du poids à vide de la remorque, mesure du degré, impression du bon, affectation à la cuve, modifications éventuelles, relevé adressé à l'adhérent), acteurs (agent de réception, chef de quai, directeur), logiciel et paramètres de chaque cave, points où une donnée peut être créée ou modifiée |
| 3. Évaluation des risques et des contrôles | cotation des risques de chaque étape, puis vérification des contrôles attendus (sous-question b) dans un échantillon de caves couvrant les quatre logiciels, puis dans les neuf caves pour les points les plus graves |
| 4. Restitution et suivi | constats validés avec les directeurs de cave, recommandations priorisées à appliquer avant l'ouverture des quais fin août, plan d'action (responsable, échéance), éléments utiles à la décision sur le module de MOUSTERAL Logiciels |

*3.4 b) – Risques, contrôles attendus et vérification*

| Risque du processus de réception (annexe 3.2) | Contrôle attendu | Vérification par l'auditeur |
|---|---|---|
| **Actions non imputables** : compte unique « PESÉE » partagé par les agents et les saisonniers dans six caves, mot de passe affiché | **accès nominatifs** : un compte par personne, saisonniers compris, ouvert à l'embauche et fermé en fin de campagne, mot de passe personnel ou badge | rapprochement de la liste des comptes de chaque logiciel avec la liste du personnel et des saisonniers de 2026 ; observation du poste de pesée ; contrôle que chaque connexion de la campagne est rattachée à une personne |
| **Cumul de fonctions incompatibles** : le chef de quai crée l'adhérent ou la parcelle, pèse et modifie le bon ; trois directeurs modifient eux-mêmes les paramètres, dont le poids à vide des remorques | **séparation des tâches** : la création des adhérents, des parcelles et des poids à vide, la pesée, et la correction d'un bon validé relèvent de personnes différentes ; toute correction est validée par une seconde personne | extraction de la matrice des droits de chaque logiciel et repérage des conflits (cible : aucun) ; revue des changements de paramètres de 2026 et de leur autorisation |
| **Modification non tracée du degré ou du poids après la pesée** : environ 600 bons modifiés après leur impression, sans motif ni valeur d'origine conservée ; écarts de plus de 0,5 % vol. constatés sur des bons papier ; journal absent ou désactivé dans huit caves | **journalisation des modifications** : un bon validé ne se modifie qu'avec un motif ; le journal enregistre l'auteur, la date, l'ancienne et la nouvelle valeur ; il est revu chaque semaine pendant la campagne par la direction de la production | vérification, cave par cave, que le journal existe et est activé (VALCROZIÈRES) ; rapprochement d'un échantillon de doubles de bons conservés par les viticulteurs avec les données du logiciel et les relevés ; examen des modifications de 2026 et de leurs motifs |

*3.4 c) – Critères de performance et de conformité*

| Critère | Point de contrôle propre au module des apports |
|---|---|
| **Fiabilité** (exactitude, exhaustivité, intégrité des données) | numérotation continue des bons sans rupture ; concordance entre le bon remis, la base et le relevé de l'adhérent ; poids à vide des remorques à jour |
| **Sécurité** (accès, traçabilité) | comptes nominatifs, droits revus avant chaque campagne, journal des modifications actif dans les neuf caves |
| **Conformité** (aux règles de réception de l'union et des caves, au référentiel retenu) | procédure de correction d'un bon écrite et appliquée ; mesures d'ISO/IEC 27001:2022 retenues effectivement en place |

**Réponses tolérées**
- Démarche en cinq ou six étapes, si les quatre éléments demandés y figurent.
- Démarche cartographie – évaluation des risques – évaluation des contrôles – restitution, le cadrage (objectifs, périmètre, référentiel, calendrier) étant intégré à la première étape.
- Quatrième risque : absence de contrôle a posteriori (rapprochement des bons et des relevés) ; contrôle de cohérence à la saisie (degré hors des valeurs plausibles).
- Critère d'**efficacité** (durée moyenne d'une pesée, disponibilité du module) à la place de l'un des trois.
- Conformité au RGPD pour les données des adhérents, personnes physiques, citée sans développement.
- COSO cité comme cadre du contrôle interne, sans développement.

**Erreurs fréquentes**
- *Méthodologie incomplète ou générique* (`JUR-A01`) — étapes sans objet propre au cas ; juste : périmètre, référentiel, cartographie, restitution datée.
- *Audit du SI confondu avec l'audit légal des comptes* (`ET-34`) — juste : l'audit porte sur un processus applicatif et ses contrôles.
- *Contrôle cité sans moyen de le vérifier* (`JUR-T03`) — juste : extraction des droits, rapprochement d'échantillons, examen du journal.
- *Tests techniques de sécurité proposés comme diligence* (hors programme) — juste : revue des droits, des journaux et des paramètres.
- *Norme et référentiel confondus* (`ET-01`, `JUR-S06`) — juste : ISO/IEC 27001:2022 est une norme d'exigences, ISO/IEC 27002:2022 un guide de mesures.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI, démarche, critères | définition, étapes, critères | F10 § 1.1 et 1.2 | notion de cours |
| Séparation des tâches, piste d'audit | contrôles attendus | F10 § 3.1 et 3.2 | notion de cours |
| ISO/IEC 27001:2022 ; ISO/IEC 27002:2022 | référentiel de l'audit : droits d'accès, journalisation, séparation des tâches | `iso_27001_2022`, `iso_27002_2022` ; F12 § 2 | en vigueur |
| RGPD | données des adhérents (toléré) | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.5 – Le tableau de bord du système d'information de la campagne (1,5 point)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ». Limites : les méthodes classiques de suivi des budgets ne sont pas approfondies ; recul critique sur les indicateurs.

**Annexes mobilisées** : annexe 3.1 (incidents, coûts de la campagne 2026, demande de la directrice générale), annexe 1.1 (vendange de 380 milliers d'hectolitres, organigramme).

**Barème indicatif (1,5 pt)**

| Item | Attendu | Points |
|---|---|---|
| 1 | Principe d'un tableau de bord équilibré du SI (peu d'indicateurs reliés aux objectifs, équilibre performance, risques et coûts, cibles et seuils d'alerte) ; destinataires et fréquence adaptés à la campagne | 0,5 |
| 2 | Trois indicateurs (performance, risque, coût), chacun avec formule, source, fréquence, cible et axe, justifiés par l'annexe 3.1 ; 0,5 dès deux indicateurs complets | 1 |

**Réponse attendue**

*Principe, destinataires et fréquence (item 1)*

Un tableau de bord du système d'information réunit un petit nombre d'indicateurs reliés aux objectifs, chacun assorti d'une cible et d'un seuil d'alerte, pour décider et non pour décrire ; inspiré du tableau de bord prospectif adapté aux SI (Van Grembergen, F09 § 4.1), il **équilibre** la **performance** (le service rendu aux caves et aux adhérents), les **risques** (ce qui pourrait arrêter la réception) et les **coûts** (ce que coûte ce service), pour éviter qu'un indicateur ne s'améliore au détriment des autres (réduire le soutien informatique au prix d'une campagne plus exposée, par exemple). Pour la campagne : **destinataires** : Mme MAZERANDE et le comité de campagne (la « page quotidienne » demandée), chaque directeur de cave pour sa cave, le conseil pour le bilan ; **fréquence** : quotidienne pendant les vendanges, avec une synthèse hebdomadaire et un bilan en fin de campagne ; établi par le responsable du système d'information à partir du registre des incidents, qui n'existe pas aujourd'hui.

*Trois indicateurs (item 2)*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Performance** : taux de disponibilité de la réception informatisée | (heures d'ouverture des quais − heures d'interruption de la réception informatisée) / heures d'ouverture des quais, par cave et pour l'union | registre des incidents de campagne tenu par l'équipe informatique de l'union, horaires d'ouverture des quais | quotidienne pendant la campagne | au moins 99,5 % par cave, soit environ 3 heures d'arrêt au plus sur les 630 heures d'ouverture, et aucune interruption de plus de 30 minutes sans bascule en mode dégradé (4 interruptions de plus d'une heure en 2026) | processus |
| **Risque** : part des caves dont la sauvegarde de la veille est vérifiée et copiée hors ligne | nombre de caves dont la sauvegarde de la nuit a été vérifiée et dont une copie est conservée hors ligne et hors site / 9 | rapports quotidiens des prestataires des caves, vérifiés par l'équipe informatique de l'union | quotidienne pendant la campagne | 100 % chaque jour (en 2026, l'état des sauvegardes des caves était inconnu de l'union) | processus |
| **Coût** : coût du soutien informatique de la campagne par millier d'hectolitres reçus | (factures des prestataires des caves et des éditeurs liées à la campagne + heures supplémentaires de l'équipe informatique) / volume reçu en milliers d'hectolitres | comptabilité de l'union et des caves (factures, paie), logiciels de cave (volumes reçus) | hebdomadaire pendant la campagne, bilan à la clôture de la campagne | 200 € au plus par millier d'hectolitres en 2027, contre environ 250 € en 2026 (95 k€ pour 380 milliers d'hectolitres) | financier |

Lecture critique : la cible de coût ne doit pas conduire à réduire la permanence ou les tests, qui protègent la disponibilité ; à l'inverse, un taux de disponibilité élevé sans sauvegarde vérifiée masquerait le risque, d'où l'équilibre des trois indicateurs.

**Réponses tolérées**
- Autres indicateurs complets et justifiés : délai moyen d'attente des remorques (axe client, cible 20 minutes au plus), délai de bascule en mode dégradé, nombre d'incidents interrompant la réception plus d'une heure (cible 0 contre 4), part des bons corrigés après la pesée avec motif (lien avec la question 3.4), coût de l'incident évité.
- Axe « risques » proposé en plus des axes du tableau de bord prospectif, s'il est justifié.

**Erreurs fréquentes**
- *Indicateurs génériques ou incomplets* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe, reliés à l'annexe 3.1.
- *Tableau de bord limité à la technique* (`ET-18`) — juste : performance pour les caves, risques et coûts.
- *Calcul ou décomposition d'écarts budgétaires* (hors programme) — juste : un indicateur de coût lu par rapport à une cible.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Tableau de bord du SI, indicateurs à cinq champs | structure, axes | F09 § 4 | notion de cours |
| IT Balanced Scorecard (Van Grembergen) | tableau de bord prospectif adapté aux SI | `van_grembergen_it_bsc` ; F09 § 4.1 | publié |

---

### 3.6 – Le choix d'un hébergement responsable (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : normes environnementales techniques mobilisées à titre illustratif ; durabilité intégrée à la gouvernance globale du SI.

**Annexes mobilisées** : annexe 3.3 (salle, options, positions), annexe 3.4 (loi REEN, RGESN, champ de la CSRD donné), annexe 3.1 (continuité) et annexe 1.1 (plan « ROCALDÈNE 2030 », budget du SI).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Sobriété numérique définie (questionner le besoin avant l'efficacité, distincte de l'économie d'énergie) ; stratégie responsable du SI précisée (durabilité intégrée aux choix et à la gouvernance, trajectoire mesurée) et appliquée au cas | 0,5 |
| a-2 | Quatre critères d'impact environnemental, chacun avec un indicateur et sa limite | 0,5 |
| b-1 | Comparaison des trois options sur les critères, le coût sur trois ans (480, 390 et 550 k€) et la continuité | 0,5 |
| b-2 | Lecture critique des données des prestataires (PUE estimé, mesuré ou mondial ; neutralité par compensation ; capacités facturées à l'usage et effet rebond) | 0,5 |
| b-3 | Option recommandée et justifiée ; deux conditions de réussite | 0,5 |
| c | Deux indicateurs complets (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.6 a) – Sobriété, stratégie responsable et critères*

La **sobriété numérique** consiste à interroger le besoin avant de chercher l'efficacité : ne garder que les équipements, les capacités et les données utiles, au juste niveau ; elle ne se réduit pas à économiser l'énergie, qui relève de l'efficacité (Green IT) (F14 § 3). Une **stratégie responsable du système d'information** intègre la durabilité environnementale et sociale dans les choix du SI (achats, hébergement, durée de vie, usages) et dans sa gouvernance, avec une trajectoire, des indicateurs et des arbitrages entre valeur et empreinte, au lieu d'en faire un ajout marginal (F14 § 0). Dans le cas, elle sert la troisième priorité du plan « ROCALDÈNE 2030 », dont Mme MAZERANDE doit pouvoir montrer au conseil « des progrès mesurés, pas des promesses » ; elle commence par un geste de sobriété commun aux options A et B : retirer les 12 serveurs anciens et regrouper les applications sur les 8 serveurs récents, puisque la plupart des serveurs sont utilisés à moins de 20 % de leurs capacités. La loi REEN (annexe 3.4) vise d'ailleurs des centres de données moins énergivores et l'allongement de la durée de vie des équipements.

| Critère (a-2) | Indicateur de mesure | Limite de l'indicateur |
|---|---|---|
| Efficacité énergétique de l'hébergement | **PUE** = énergie totale / énergie des équipements informatiques (2,0 aujourd'hui) | ne dit rien de l'utilité des serveurs, de l'origine de l'électricité ni de la fabrication ; sa valeur dépend du mode de mesure (estimée, mesurée sur un site, moyenne mondiale) |
| Consommation d'énergie | **MWh par an** consommés pour héberger les applications de l'union (130 MWh en 2026) | dépend du périmètre ; non communiquée dans un cloud mutualisé ; ne dit rien des émissions |
| Contenu carbone de l'électricité | part d'électricité renouvelable attestée (garanties d'origine), émissions par kWh du lieu d'implantation | les garanties d'origine attestent une production, pas une consommation heure par heure ; la « neutralité » par compensation ne réduit pas les émissions |
| Cycle de vie des équipements | nombre de serveurs retirés, réemployés ou recyclés, durée de vie moyenne à leur retrait, serveurs achetés | la fabrication des équipements du fournisseur (cloud) n'est pas visible ; une mesure complète supposerait une analyse du cycle de vie |

Autres critères acceptés : réutilisation de la chaleur (part de la chaleur récupérée), consommation d'eau du refroidissement.

*3.6 b) – Comparaison et recommandation*

| | Option A – rénover la salle | Option B – centre de données régional | Option C – cloud public |
|---|---|---|---|
| Efficacité énergétique | PUE 1,5, estimé | PUE 1,3, **mesuré et publié** | PUE 1,2, **moyenne mondiale**, rien pour le site |
| Consommation | environ 45 MWh | environ 39 MWh, soit environ 70 % de moins qu'en 2026 | non communiquée |
| Électricité | réseau national | renouvelable régionale, garanties d'origine | « neutralité » par certificats et compensation ; mix du pays plus carboné que celui de la France |
| Chaleur | perdue | récupérée (piscine intercommunale) | non communiquée |
| Équipements | 8 serveurs conservés, 12 retirés ; climatiseurs et onduleurs neufs | 8 serveurs conservés, 12 retirés | serveurs retirés à mesure du transfert, sauf ceux du progiciel, qui restent dans la salle actuelle ; capacités du fournisseur |
| Coût sur trois ans | 300 + 3 × 60 = **480 k€** | 150 + 3 × 80 = **390 k€** | 250 + 3 × 100 = **550 k€**, variable, et la salle de Pézenas reste nécessaire pour le progiciel jusqu'à son remplacement |
| Continuité | salle toujours exposée aux canicules ; pas de second site | second site distinct de Pézenas, personnel jour et nuit, copies des sauvegardes de l'union et des caves possibles ; dépend des deux liaisons réseau | infrastructure résiliente, mais dépendance au réseau et au fournisseur ; progiciel toujours à Pézenas |

Lecture critique (b-2) : les données ne se valent pas. Le PUE de A est une estimation, celui de B une mesure publiée, celui de C une moyenne mondiale qui ne dit rien du centre qui hébergerait les données ; la « neutralité carbone » de C repose sur la compensation et non sur une réduction, alors que l'électricité du pays d'implantation est plus carbonée ; la facturation à l'usage et l'ajout de capacités « en quelques minutes » exposent à un **effet rebond** contraire à la sobriété. L'argument de M. VERDAGNOL (« on ne paie que ce qu'on consomme ») ne tient pas ici : l'option C est la plus chère sur trois ans, son coût est variable, et elle laisse le progiciel à Pézenas.

Recommandation (b-3) : l'**option B**. Elle combine la meilleure performance environnementale vérifiable (PUE mesuré de 1,3, électricité renouvelable attestée, chaleur réutilisée, consommation divisée par plus de trois), le coût le plus bas sur trois ans (390 k€, soit environ 130 k€ par an, à rapprocher d'un budget du SI de 2 200 k€) et un apport décisif à la continuité : un second site pour les sauvegardes de l'union et des caves (question 3.2), et la fin de l'exposition aux canicules. Conditions de réussite (deux attendues) :
1. **Sobriété d'abord** : retirer les 12 serveurs anciens et regrouper les applications **avant** le transfert, faire réemployer ou recycler les serveurs retirés de manière tracée, et allonger la durée de vie des 8 serveurs récents.
2. **Données environnementales vérifiables** : obtenir de LIMBRÈZE Data un relevé régulier du PUE, de la consommation des équipements de l'union et des garanties d'origine, pour alimenter les indicateurs (sous-question c) et le compte rendu au conseil.
3. **Continuité** : deux liaisons effectivement indépendantes, mode dégradé maintenu à Pézenas et dans les caves, et restauration testée depuis le second site.
4. **Réversibilité** : ne pas s'enfermer, et réexaminer l'hébergement avec les mêmes critères lors du choix du futur progiciel de l'union.

L'option A reste défendable si la dépendance au réseau est jugée inacceptable ; l'option C pourrait être reconsidérée après le remplacement du progiciel, si le fournisseur communique des données propres au site.

*3.6 c) – Deux indicateurs de suivi*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Indicateur d'efficacité énergétique (PUE) de l'hébergement des serveurs de l'union | énergie totale consommée par l'hébergement / énergie consommée par les équipements informatiques de l'union | relevés du centre de données LIMBRÈZE Data, transmis chaque trimestre | trimestrielle | 1,3 au plus dès 2028, contre environ 2,0 en 2026 | environnement |
| Consommation d'électricité annuelle de l'hébergement des serveurs de l'union | somme des relevés mensuels de consommation de l'hébergement (équipements et part du bâtiment), en MWh | relevés mensuels du centre de données ; inventaire des serveurs de l'équipe informatique | annuelle, à partir des relevés mensuels | 40 MWh au plus en 2028, contre 130 MWh en 2026 | environnement |

(0,5 pt pour les deux indicateurs complets.) Le PUE seul pourrait s'améliorer alors que la consommation augmente : les deux indicateurs se lisent ensemble.

**Réponses tolérées**
- Option A recommandée si le candidat la justifie par la maîtrise et l'absence de dépendance au réseau, en reconnaissant son PUE et son exposition aux canicules ; option C recommandée seulement avec des exigences de données propres au site et une réponse au cas du progiciel.
- Autres indicateurs complets : part d'électricité renouvelable attestée (cible 100 %), part des serveurs retirés réemployés ou recyclés de manière tracée (cible 100 %), durée de vie moyenne des serveurs à leur retrait, part de la chaleur réutilisée.
- Mention de l'étude ADEME-Arcep pour rappeler le poids de la fabrication des équipements, sans calcul.
- Mention de la CSRD pour dire seulement que l'union n'y est pas soumise (donnée de l'annexe 3.4).

**Erreurs fréquentes**
- *Sobriété confondue avec l'économie d'énergie* (`ET-12`) — juste : d'abord réduire le nombre de serveurs et les capacités, puis chercher l'efficacité.
- *Empreinte réduite à l'électricité ou au PUE* (`ET-38`) — juste : origine de l'électricité, fabrication et durée de vie, chaleur.
- *Données des prestataires prises pour argent comptant* (`JUR-T03`) — juste : distinguer estimation, mesure et moyenne mondiale, compensation et réduction.
- *Cloud présenté comme toujours plus vert ou moins cher* (`ET-30`, `JUR-G11`) — juste : il déplace l'empreinte, peut favoriser l'effet rebond, et coûte ici le plus cher.
- *Calcul d'empreinte ou discussion du champ de la CSRD* (`ET-41`) — juste : ni calcul ni assujettissement, qui est une donnée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Sobriété numérique, Green IT, stratégie responsable, PUE, cloud et centres de données | définitions, critères, indicateurs | F14 § 0, 3, 4 et 5 | notion de cours |
| Loi REEN n° 2021-1485 | centres de données moins énergivores, durée de vie des équipements | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | famille de critères sur l'hébergement | `rgesn_2024` ; F14 § 2 | en vigueur |
| Étude ADEME-Arcep sur l'empreinte du numérique | poids de la fabrication (toléré) | `etude_ademe_arcep_numerique` ; F14 § 1 | en vigueur |
| Directive (UE) 2022/2464 (CSRD) | union hors champ (donnée) | `csrd` ; fiche commune | en vigueur |
| Directive (UE) 2022/2555 (NIS 2) | union hors champ (donnée) | `nis2` ; F12 § 6 | en vigueur au niveau européen |
