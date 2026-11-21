# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 40 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique, F04 relations avec les ESN et contrats, F05 projets et changement, F12 sécurité et résilience (§ 7, DORA), F13 intelligence artificielle, F15 RGPD opérationnel (§ 5, sous-traitance), glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Les effets des évolutions de l'assistance et la stratégie du système d'information | `1.1.d` Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 4 |
| 1.2 L'IA d'aide aux chargés d'assistance | `1.3.d` Fonctionnement et usages des technologies émergentes : blockchain, registres distribués, IA, … | 2 |
| 1.3 La planification et le pilotage du projet PASSERELLE | `1.5.d` Planification des ressources, délais, coûts et qualité ; `1.5.a` Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 5 |
| 1.4 Le contrat avec l'ESN et la gouvernance de la relation | `1.4.c` Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD ; `1.4.a` Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques ; `1.4.e` Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) | 3 |
| **Dossier 1 – Préparer la transformation numérique de l'assistance et le projet PASSERELLE** |  | **14** |

Répartition indicative : connaissances (modèle économique, stratégie du SI, IA générative et apprentissage automatique, chemin critique, sponsor et comité de pilotage, niveaux de service et réversibilité) environ 3 points (items 1.1 a-1, 1.1 b-1, 1.2 a-1, la moitié de 1.3 a-2, la moitié de 1.3 c-1, la moitié de 1.4 a-1) ; analyse des annexes et recommandations environ 11 points, soit environ 79 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – Les effets des évolutions de l'assistance et la stratégie du système d'information (4 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.d` « Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limites : « Ne pas confondre alignement stratégique et simple adéquation technique. » « Ne pas se limiter à une veille passive : intégrer l'analyse prospective dans l'évaluation des opportunités SI. »

**Annexes mobilisées** : annexes 1.2 (six évolutions chiffrées, témoignages du constructeur VIRANDOR, du directeur des plateaux, de la directrice du réseau et d'un assureur partenaire) et 1.1 (distributeurs, réseau de 3 400 prestataires, 520 000 dossiers dont 60 % automobile, système d'information).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Modèle économique défini (manière dont l'entreprise crée de la valeur pour ses clients et en capte une partie : proposition de valeur, clients, partenaires, ressources et activités clés, revenus et coûts) ; appliqué à VALMÉRIS : intermédiaire payé par les distributeurs, au service des bénéficiaires, qui s'appuie sur des prestataires ; sa valeur tient à la relation au moment de l'urgence et à l'orchestration du réseau | 0,5 |
| a-2 | Première évolution : effet sur la place de VALMÉRIS, appuyé sur les chiffres de l'annexe 1.2 (menace ou opportunité qualifiée) | 0,5 |
| a-3 | Deuxième évolution, même exigence ; au moins une des trois évolutions traite du risque de désintermédiation | 0,5 |
| a-4 | Troisième évolution, même exigence ; au moins une évolution débouche sur un nouveau service ; conclusion (le modèle passe d'un plateau qui reçoit des appels à une plateforme qui reçoit des signaux et orchestre un réseau) | 0,5 |
| b-1 | Stratégie du SI définie (orientations à moyen terme du système d'information, déduites de la stratégie de l'entreprise et des opportunités technologiques, qui guident les choix d'applications, de données, d'organisation et de partenariats) ; elle n'est pas un choix technique | 0,5 |
| b-2 | Première orientation, justifiée par une évolution et rattachée à un objectif d'« Assister 2030 » | 0,5 |
| b-3 | Deuxième orientation, même exigence | 0,5 |
| b-4 | Troisième orientation, même exigence ; lien avec PASSERELLE (socle de ces orientations) | 0,5 |

**Réponse attendue**

*1.1 a) – Les effets de trois évolutions sur le modèle économique de VALMÉRIS*

Le **modèle économique** décrit la manière dont une entreprise crée de la valeur pour ses clients et en capte une partie : sa proposition de valeur, ses clients, ses partenaires, ses ressources et activités clés, la formation de ses revenus et de ses coûts. Celui de VALMÉRIS est celui d'un **intermédiaire** : les 15 distributeurs (le groupe TERRANDÈLE et 14 partenaires) lui paient l'assistance de leurs assurés ; les bénéficiaires reçoivent le service, jour et nuit ; 3 400 prestataires agréés l'exécutent. Sa valeur tient à trois atouts : la **relation avec le bénéficiaire au moment où tout va mal** (« la voix humaine », dit le directeur des plateaux), l'**orchestration d'un réseau** de prestataires de qualité, et la **capacité de traiter** 520 000 dossiers par an (0,5 pt).

**Trois évolutions** (0,5 pt chacune ; trois parmi les suivantes) :

| Évolution (annexe 1.2) | Effet sur le modèle économique | Menace ou opportunité |
|---|---|---|
| Véhicules connectés (A1 et témoignage de VIRANDOR) | Le **premier contact** passe au constructeur : l'alerte arrive chez lui, le conducteur déclare sa panne dans son application ; VALMÉRIS ne reçoit qu'une partie des alertes (30 000, un dossier automobile sur dix), par courriel, ressaisi. L'autre constructeur partenaire montre la **désintermédiation** possible : sa propre filiale d'assistance se passe d'assisteur. VIRANDOR ne gardera qu'un assisteur en 2028 : c'est près de 10 % des dossiers (50 000) et du chiffre d'affaires (30 M€) qui se jouent. VALMÉRIS risque de devenir un simple exécutant, sans relation avec le conducteur ni maîtrise des données. | menace forte à court terme ; opportunité si VALMÉRIS sait recevoir les alertes en temps réel et déclencher l'assistance sans appel (premier objectif du plan) |
| Détecteurs de fuite d'eau (A2) | L'assistance habitation (25 % des dossiers) peut passer de la **réparation** à la **prévention** : envoyer un plombier sur alerte, avant que le dégât ne s'étende. C'est un **nouveau service** à proposer aux partenaires assureurs, qui y trouvent une baisse de leurs sinistres ; l'assureur partenaire menace d'aller ailleurs. | opportunité, à condition de traiter des alertes d'objets connectés ; menace de perte du partenaire sinon |
| Attentes de suivi en temps réel (A3) | La **référence** des bénéficiaires n'est plus un autre assisteur mais la livraison de colis : huit réclamations sur dix portent sur l'absence de nouvelles ; les rappels pendant l'attente chargent les plateaux ; 10 % des dossiers sont ouverts en ligne (contre 2 % en 2022). La proposition de valeur doit intégrer l'**information en temps réel** (deuxième objectif du plan) ; la géolocalisation de l'application des prestataires le permet. | opportunité de différenciation et de baisse des appels ; menace pour la satisfaction et la fidélité des partenaires |
| Plateformes de mise en relation (A4 et témoignage de la directrice du réseau) | Les plateformes s'adressent **directement** aux particuliers et aux assureurs : désintermédiation par l'aval ; près d'un prestataire sur dix (300 sur 3 400) y est inscrit, et les meilleurs choisissent l'assisteur qui donne des missions claires et paie vite. Le **réseau**, ressource clé, devient disputé. | menace sur le réseau et sur les partenaires ; incite à traiter les prestataires comme des clients (missions claires, règlement rapide) |
| Assistants conversationnels et transcription (A5) | Les concurrents automatisent les demandes simples et la saisie : la **productivité** et la disponibilité de nuit deviennent un facteur de compétitivité. | opportunité (IA d'aide aux chargés : question 1.2) ; menace si VALMÉRIS reste en retard |
| Pénurie de chargés (A6) | Plus d'un chargé sur cinq est parti en 2026 (120 sur 560), 25 postes de nuit sont vacants, alors qu'un appel sur cinq arrive la nuit : la capacité de traitement, ressource clé, est fragile ; la continuité jour et nuit est menacée. | menace interne ; l'automatisation de la saisie et des demandes simples libère du temps de chargé |

**Conclusion** : le modèle d'un plateau qui **reçoit des appels** évolue vers celui d'une **plateforme qui reçoit des signaux** (véhicules, objets, applications) et **orchestre un réseau** ; la valeur se déplace vers celui qui reçoit l'alerte le premier, informe le bénéficiaire et fidélise les prestataires.

*1.1 b) – Trois orientations de la stratégie du système d'information*

La **stratégie du système d'information** fixe, pour plusieurs années, les orientations du système d'information déduites de la stratégie de l'entreprise et des opportunités technologiques : elle guide les choix d'applications, de données, d'organisation et de partenariats, et se traduit ensuite en projets. Elle n'est pas un choix technique : chaque orientation doit servir un objectif d'« Assister 2030 » (0,5 pt).

**Trois orientations** (0,5 pt chacune ; trois parmi les suivantes) :

| Orientation | Évolution qui la justifie | Objectif d'« Assister 2030 » servi |
|---|---|---|
| **Ouvrir le SI aux signaux en temps réel** : interfaces de programmation avec les constructeurs, les objets connectés des partenaires et les applications, ouverture automatique du dossier sans appel et retour d'information au distributeur (heure d'arrivée) ; PASSERELLE en est le socle | véhicules connectés, échéance de VIRANDOR ; détecteurs de fuite | déclencher l'assistance sans appel ; conserver les partenaires |
| **Construire le parcours numérique du bénéficiaire** : suivi du prestataire sur une carte, notifications, ouverture et suivi du dossier en ligne, en s'appuyant sur la géolocalisation de l'application des prestataires | attentes de suivi en temps réel ; 10 % de dossiers en ligne | informer en temps réel ; réduire les rappels et le délai d'arrivée |
| **Outiller les chargés par l'IA sous contrôle humain** : transcription, résumé, qualification et proposition de prestataires, demandes simples en libre-service, pour absorber la nuit et la pénurie de chargés | assistants conversationnels ; pénurie de chargés | continuité jour et nuit ; réduction du délai |
| **Faire du réseau de prestataires un partenaire numérique** : missions claires et complètes dans l'application, acceptation et suivi en ligne, règlement plus rapide | plateformes de mise en relation ; témoignage de la directrice du réseau | réduire le délai d'arrivée (prestataires fidèles et disponibles) |
| **Sécuriser les dépendances numériques** : contrats avec les ESN et les fournisseurs de services en ligne conformes aux exigences de DORA, continuité jour et nuit | dépendance accrue aux interfaces et aux services en ligne | continuité et respect durable de DORA |

Ces orientations sont **liées** : PASSERELLE n'est pas seulement le remplacement d'un logiciel de 2008, c'est le socle sans lequel ni les alertes, ni le suivi en temps réel, ni l'IA ne peuvent être intégrés au dossier.

**Réponses tolérées**
- Modèle économique présenté à l'aide d'une grille en neuf blocs (proposition de valeur, segments de clients, canaux, relation, revenus, ressources, activités, partenaires, coûts) ou de la chaîne de valeur (Porter, 1985), si elle est appliquée au cas.
- Lecture de VALMÉRIS comme une plateforme à plusieurs faces (distributeurs, bénéficiaires, prestataires), si elle est justifiée.
- Autres évolutions ou orientations tirées de l'annexe 1.2, si elles sont rattachées à un objectif du plan et appuyées sur les chiffres.
- Analyse de l'alignement selon le modèle de Henderson et Venkatraman (1993) : valorisée sans être exigée.

**Erreurs fréquentes**
- *Évolutions décrites sans effet sur le modèle économique* (`JUR-T03` analyser et argumenter, ne pas décrire) — « les véhicules sont connectés » ; juste : qui capte le premier contact et la valeur, ce que VALMÉRIS risque de perdre ou peut gagner.
- *Orientations réduites à des choix techniques* (`JUR-G02` alignement réduit à un choix technique ou à une standardisation logicielle) — « passer au cloud », « acheter une IA » ; juste : une orientation qui sert un objectif du plan.
- *Veille passive ou dispositif de veille construit* (`JUR-T07` répondre à la seule question posée) — la question demande l'analyse des effets, pas l'organisation de la veille.
- *Désintermédiation oubliée* (`JUR-T08` exploiter toutes les annexes) — le témoignage de VIRANDOR et la filiale de l'autre constructeur en sont le cœur ; près de 10 % de l'activité en dépend.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Stratégie du SI et alignement | orientations déduites de la stratégie et des opportunités technologiques ; pas une adéquation technique | F01 § 1 et § 3 ; `erreurs_types.md` ET-06 | notion de cours |
| Chaîne de valeur (Porter, 1985) | grille admise pour situer le SI (réponse tolérée) | F01 § 1 | notion de cours |
| Henderson et Venkatraman, 1993 (modèle SAM) | réponse tolérée | F01 § 1 | publié |

---

### 1.2 – L'IA d'aide aux chargés d'assistance (2 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures : `1.3.d` « Fonctionnement et usages des technologies émergentes : blockchain, registres distribués, IA, … ». Limite : « L'usage de l'IA doit notamment être analysé dans ses effets métiers et non uniquement comme outil technique. »

**Annexes mobilisées** : annexe 1.3 (fonctionnement de l'outil, résultats du pilote, données d'entraînement, réactions des chargés, proposition de la DSI, repère sur le règlement sur l'IA).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fonctionnement : la transcription et le résumé relèvent de l'**IA générative** (un modèle de langage produit un texte nouveau, plausible mais non garanti exact) ; la qualification et la proposition de prestataires relèvent de l'**apprentissage automatique** (un modèle a appris sur 3 millions de dossiers passés à reproduire les choix faits dans des situations comparables) ; les deux ne sont pas confondues | 0,5 |
| a-2 | Deux limites appuyées sur les chiffres du pilote, dont une qui tient aux données d'entraînement (véhicules électriques sous-représentés, règles de codage changées en 2021) ; l'autre parmi : résumés inexacts, erreurs de qualification, confiance aveugle | 0,5 |
| b-1 | Appréciation : gains réels (− 20 % de temps de traitement) mais extension « tel quel » prématurée (erreurs restées en hausse, 40 % de propositions inadaptées pour les véhicules électriques, plateaux non associés) ; condition du **contrôle humain** précisée (le chargé reste décideur, vérification obligatoire des propositions et du résumé, signalement des erreurs) | 0,5 |
| b-2 | Seconde condition, précisée et appliquée : qualité et actualisation des données d'entraînement et suivi des erreurs, ou formation et maîtrise de l'IA du personnel, ou gouvernance de l'outil (responsable, règles de correction), ou extension progressive après association des plateaux | 0,5 |

**Réponse attendue**

*1.2 a) – Le fonctionnement de l'outil et ses limites*

L'outil associe deux familles d'IA qu'il ne faut pas confondre (0,5 pt) :
- **La transcription et le résumé** : la parole est transcrite, puis un **modèle de langage**, fourni par un éditeur sous forme de service en ligne, **génère** un résumé. C'est de l'**IA générative** : le modèle produit un texte nouveau en prédisant la suite la plus probable ; ce texte est plausible, mais **non garanti exact**.
- **La qualification et la proposition de prestataires** : un modèle a été **entraîné** par la DSI sur environ 3 millions de dossiers de 2018 à 2025 ; il a appris, à partir de ces exemples, quelle qualification et quels prestataires avaient été retenus dans des situations comparables, et reproduit ces choix. C'est de l'**apprentissage automatique** (supervisé) : il **classe et prédit**, sans rien inventer, mais il ne sait que ce que contiennent les dossiers passés.

**Deux limites** (0,5 pt ; deux parmi les suivantes, dont une qui tient aux données) :
- **Les biais des données d'entraînement** : les véhicules électriques représentaient 2 % des dossiers d'entraînement, mais 12 % des dossiers du pilote, six fois plus ; le modèle propose donc des dépanneurs non équipés (40 % de propositions inadaptées pour ces véhicules, contre 15 % en moyenne). De même, les règles de codage des garanties ont changé en 2021 : une partie des exemples enseigne des règles périmées.
- **Les erreurs du résumé** : 4 % des résumés contiennent une information qui n'a pas été dite (« autoroute » au lieu de « parking »), davantage quand l'appel est bruyant ; versée au dossier, l'erreur peut envoyer le prestataire au mauvais endroit.
- **Les erreurs de qualification** : une qualification proposée sur dix est erronée ; les erreurs restées dans le dossier validé passent de 2 % à 3 % : le gain de temps se paie en partie en qualité.
- **La confiance aveugle** : le chargé recruté en 2026 valide la nuit « sans regarder » ; l'outil, conçu comme une aide, devient de fait le décideur au moment où les chargés sont les plus chargés.

*1.2 b) – L'extension de l'outil aux trois plateaux*

Les gains sont réels : − 20 % de temps de traitement (de 10 à 8 minutes), trois minutes de saisie économisées par appel, utiles face à la pénurie de chargés. Le temps total ne baisse toutefois que de deux minutes : le temps passé en conversation et en relecture passe de 6 à 7 minutes, ce qui montre que la vérification du résumé a un coût, qu'il faut préserver (nuance valorisée). Mais étendre l'outil **« tel quel »** en janvier 2028 serait prématuré : la qualité baisse (3 % d'erreurs restées au lieu de 2 %), les propositions sont mauvaises pour une part croissante du parc (véhicules électriques), personne ne corrige l'outil, et Limoges et Metz, qui représentent 470 des 560 chargés, ne l'ont jamais vu (0,5 pt avec la première condition).

**Deux conditions** (dont le contrôle humain, obligatoire) :
- **Le contrôle humain** : le chargé reste le décideur ; le résumé et les propositions sont présentés comme des suggestions à vérifier, avec les éléments qui les justifient (distance, équipement, horaires du prestataire) ; certaines situations imposent une vérification renforcée (véhicule électrique, nuit, garantie incertaine) ; la validation et les corrections sont tracées ; les chargés signalent les erreurs, qu'une équipe désignée analyse. Une validation « sans regarder » n'est pas un contrôle humain (0,5 pt, au sein de l'item b-1).
- **La qualité et l'actualisation des données d'entraînement** : réentraîner le modèle sur des dossiers récents et recodés selon les règles en vigueur, compléter les caractéristiques des prestataires (équipement pour véhicules électriques, horaires de nuit, zone), mesurer les erreurs par type de véhicule et par plateau, et fixer un seuil d'erreurs à ne pas dépasser avant l'extension (0,5 pt).
- *Autres conditions admises* : **formation et maîtrise de l'IA** des chargés et des superviseurs des trois plateaux, que le règlement sur l'IA demande déjà aux déployeurs de favoriser par des mesures (article 4, dans sa rédaction issue du règlement (UE) 2026/1744 ; repère donné par l'annexe 1.3 D) ; **gouvernance de l'outil** (un responsable métier, un circuit de correction, un suivi mensuel des erreurs) ; **extension progressive** après association des plateaux de Limoges et de Metz ; **intégration à PASSERELLE**, plutôt qu'à un logiciel appelé à disparaître.

**Réponses tolérées**
- Transcription présentée comme une reconnaissance de la parole par apprentissage automatique, distincte de la génération du résumé, si l'IA générative est bien identifiée pour le résumé.
- Mention de la transparence envers les bénéficiaires (information sur la transcription de l'appel), si elle reste une condition de principe, sans analyse juridique.
- Extension par étapes (Valence, puis un autre plateau), si elle est justifiée par les limites du pilote.

**Erreurs fréquentes**
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — « l'outil génère les prestataires » ou « le résumé est appris sur les dossiers » ; juste : un modèle de langage génère le résumé, un modèle entraîné sur les dossiers passés classe et propose.
- *Opportunités sans risques, ou l'inverse* (`ET-19`) — ne retenir que les − 20 % de temps, ou rejeter l'outil ; juste : gains mis en regard des erreurs et des biais, conditions d'extension.
- *Analyse technique du modèle* (`JUR-T12` de moins en moins de technique) — architecture du modèle, algorithmes : hors attente ; juste : effets sur le métier des chargés et sur le service.
- *Classification au titre du règlement sur l'IA* (`JUR-T07` répondre à la seule question posée) — la situation de l'outil est donnée comme examinée ; elle n'est pas à analyser.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| IA générative et apprentissage automatique | typologie, limites (erreurs, biais), contrôle humain | F13 § 1 à § 4 ; `erreurs_types.md` ET-09, ET-19 | notion de cours |
| Règlement (UE) 2024/1689 sur l'IA, modifié par le règlement (UE) 2026/1744 | mesures pour favoriser la maîtrise de l'IA du personnel (art. 4, modifié par le règlement (UE) 2026/1744), depuis le 02/02/2025 (repère donné par l'annexe 1.3 D) | `ai_act`, `omnibus_numerique_ia` ; F13 § 5 | en vigueur, application échelonnée |

---

### 1.3 – La planification et le pilotage du projet PASSERELLE (5 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de SI : `1.5.d` « Planification des ressources, délais, coûts et qualité » ; `1.5.a` « Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ». Limite : « L'aspect budgétaire détaillé ne relève pas du programme de l'UE. »
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ».

**Annexes mobilisées** : annexes 1.4 (tâches, durées, antériorités, ressources, contraintes, coûts, leviers, tensions), 1.2 (témoignage de VIRANDOR : 50 000 dossiers et 30 M€) et 1.1 (organigramme, 560 chargés sur trois plateaux).

**Barème indicatif (5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gantt ou tableau lisible : sept tâches, dates au plus tôt de début et de fin, antériorités respectées, jalons (choix des spécifications, fin de recette, bascule) | 0,5 |
| a-2 | Durée sans contrainte de 42 semaines (fin en février 2028) et chemin critique A-D-E-G défini (suite de tâches sans marge, dont tout retard décale la fin du projet) ; marges de B, C et F | 0,5 |
| a-3 | Effet de la contrainte des superviseurs : recette (semaines 31 à 36) et formation (27 à 34) se chevauchent ; en les enchaînant, le projet passe à 50 semaines (fin en avril 2028) ; le chemin critique devient A-D-E-F-G | 0,5 |
| a-4 | Ordre justifié : la recette avant la formation, pour former sur la version recettée (la formation d'abord donnerait 46 semaines, mais sur une version non recettée et loin de la bascule) | 0,5 |
| b-1 | Échéance appréciée : tenue sur le papier (10 semaines de marge), mais recette et formation tombent de décembre à février ; si le refus est maintenu, recette en semaines 45 à 50, formation 51 à 58, bascule 59 à 64 : fin juillet 2028, quatre semaines après le 30 juin ; l'arrêt de l'ancien logiciel avant la fin de 2028 reste possible | 0,5 |
| b-2 | Leviers évalués : chacun fait finir la recette en semaine 32, avant l'hiver ; formation en mars-avril, bascule en mai-juin (semaines 53 à 58), deux semaines de marge ; levier 1 sans coût mais avec un risque de qualité, levier 2 à 150 k€ (environ 4 % du projet) sans perte de qualité ; les deux ensemble avancent la recette à la semaine 28 sans changer la fin | 0,5 |
| b-3 | Arbitrage recommandé et justifié par les enjeux (près de 10 % des dossiers et du chiffre d'affaires ; 150 k€ face à 30 M€ par an), avec les précautions de qualité et la décision renvoyée au comité de pilotage | 0,5 |
| c-1 | Sponsor (le directeur général) et comité de pilotage : composition (directions des plateaux, des SI, du réseau, des risques, administrative et financière, directeur de projet, ESN invitée), fréquence mensuelle, décisions (calendrier, disponibilité des superviseurs, leviers et réserve, écarts au standard, décision de bascule) | 0,5 |
| c-2 | Rôles : plateaux maîtres d'ouvrage et utilisateurs clés, DSI et ESN maîtres d'œuvre, réseau de prestataires pour l'application, partenaires associés à la validation des interfaces à un jalon fixé, chef de projet animateur ; réponse à chacune des tensions | 0,5 |
| c-3 | Deux règles d'arbitrage explicites et applicables (par exemple : le jalon du 30 juin 2028 et la continuité jour et nuit priment ; le standard de la solution est adopté sauf exigence justifiée ; la disponibilité des superviseurs est planifiée avec les plateaux et toute dérogation est décidée en comité) | 0,5 |

**Réponse attendue**

*1.3 a) – Les dates au plus tôt, le chemin critique et la contrainte des superviseurs*

**Sans tenir compte des superviseurs** (dates en fin de semaine ; semaine 1 = première semaine d'avril 2027 ; quatre semaines par mois) :

| Tâche | Durée | Antériorités | Début au plus tôt (semaine) | Fin au plus tôt (semaine) | Mois | Marge |
|---|---|---|---|---|---|---|
| A – Cadrage et spécifications | 16 | — | 1 | 16 | avril à juillet 2027 | 0 |
| B – Paramétrage | 10 | A | 17 | 26 | août à octobre 2027 | 2 |
| C – Reprise des données | 10 | A | 17 | 26 | août à octobre 2027 | 4 |
| D – Interfaces | 14 | A | 17 | 30 | août à novembre 2027 | 0 |
| E – Recette | 6 | B, C, D | 31 | 36 | novembre à décembre 2027 | 0 |
| F – Formation | 8 | B | 27 | 34 | octobre à décembre 2027 | 2 |
| G – Bascule des trois plateaux | 6 | E, F | 37 | 42 | janvier à février 2028 | 0 |

Le projet dure **42 semaines** (16 + 14 + 6 + 6) et s'achève en février 2028. Le **chemin critique** est la suite de tâches sans marge, dont tout retard décale d'autant la fin du projet : **A-D-E-G**, les interfaces étant la tâche la plus longue après le cadrage. B et F ont deux semaines de marge (16 + 10 + 8 + 6 = 40), C en a quatre (0,5 pt pour le tableau ou le Gantt, 0,5 pt pour la durée et le chemin critique).

**Avec la contrainte des superviseurs** : les trente superviseurs conduisent la recette (semaines 31 à 36) et la formation (semaines 27 à 34) ; ces deux tâches se chevauchent pendant quatre semaines et ne peuvent pas être menées ensemble. En faisant la recette d'abord, la formation occupe les semaines 37 à 44 et la bascule les semaines 45 à 50 : le projet dure **50 semaines** (fin en avril 2028), soit huit semaines de plus ; le chemin critique devient **A-D-E-F-G** (0,5 pt).

**L'ordre retenu : la recette avant la formation** (0,5 pt). Former d'abord (semaines 27 à 34, recette 35 à 40, bascule 41 à 46) raccourcirait le projet à 46 semaines, mais les 560 chargés seraient formés sur une version non recettée, que la recette fera encore changer, et plusieurs semaines avant la bascule ; c'est d'ailleurs la règle de l'annexe 1.4 B. Former sur la version recettée, juste avant la bascule, sert la qualité de service des plateaux.

*1.3 b) – L'échéance du 30 juin 2028 et l'arbitrage*

**Sur le papier**, le projet finit en avril 2028 (semaine 50), dix semaines avant l'échéance de VIRANDOR (semaine 60). **Mais** la recette (semaines 31 à 36) déborde sur décembre et la formation (37 à 44) occupe janvier et février, la saison d'hiver où le directeur des plateaux refuse de libérer les superviseurs. Si ce refus est maintenu, la recette ne peut commencer qu'en mars 2028 : recette en semaines 45 à 50, formation 51 à 58, bascule 59 à 64. Le projet s'achève fin **juillet 2028**, **quatre semaines après** le 30 juin : VALMÉRIS ne pourrait pas présenter à VIRANDOR des alertes reçues sur tous ses plateaux. L'ancien logiciel serait encore arrêté avant la fin de 2028 ; c'est l'échéance du constructeur qui est en jeu (0,5 pt).

**Les leviers** (0,5 pt) :

| Option | Effet sur le calendrier | Coût | Qualité et risques |
|---|---|---|---|
| Accepter le retard | fin en juillet 2028 | aucun surcoût direct | perte probable de VIRANDOR : près de 10 % des dossiers (50 000) et environ 30 M€ de chiffre d'affaires par an, pour cinq ans |
| Levier 1 : spécifier les exigences clés et les écarts (A : 16 → 12 semaines) | recette en semaines 27 à 32, achevée avant décembre ; formation 45 à 52 (mars-avril 2028) ; bascule 53 à 58 (mai-juin 2028) : deux semaines de marge | aucun surcoût | plus d'ajustements de paramétrage découverts en recette : si la recette glisse d'une seule semaine, elle tombe en hiver et le retard revient |
| Levier 2 : renfort de l'ESN sur les interfaces (D : 14 → 10 semaines) | même calendrier : recette achevée en semaine 32, bascule en semaines 53 à 58 | 150 k€, environ 4 % des 4 000 k€ du projet | qualité préservée ; aucune marge avant l'hiver pour la recette |
| Leviers 1 et 2 ensemble | recette en semaines 23 à 28 : quatre semaines de marge avant l'hiver ; la fin reste en semaine 58, car la formation attend de toute façon mars | 150 k€ | marge qui protège la recette ; risque du levier 1 à maîtriser |

**Arbitrage recommandé** (0,5 pt) : combiner les deux leviers. Le renfort de l'ESN agit sur la tâche critique la plus exposée, les interfaces, qui sont justement ce que VIRANDOR exige ; 150 k€ sont peu au regard de 30 M€ de chiffre d'affaires annuel en jeu (0,5 % d'une année). Le levier 1 redonne à la recette quatre semaines de marge avant l'hiver ; pour en limiter le risque de qualité, on garde des spécifications détaillées là où la DSI a raison, c'est-à-dire pour les interfaces avec les constructeurs et les partenaires, et l'on adopte ailleurs le fonctionnement standard de la solution, ce qui est l'intérêt même d'une solution du marché. Le refus du directeur des plateaux est respecté : formation en mars-avril et bascule en mai-juin, hors saison d'hiver. Le surcoût de 150 k€ est décidé par le comité de pilotage, sans puiser dans la réserve pour aléas de 200 k€, qui reste disponible.

*1.3 c) – L'organisation du pilotage du projet*

Les tensions de l'annexe 1.4 E ont une cause commune : chaque direction défend son point de vue, et **personne n'arbitre**. Le pilotage proposé :

| Acteur ou instance | Rôle | Tension traitée |
|---|---|---|
| **Sponsor : M. MARVÉJOL, directeur général** | porte le projet, préside le comité de pilotage, tranche les conflits entre directions, valide le surcoût et les dates clés ; le projet est un projet de l'entreprise (plateaux, partenaires, constructeurs), pas un projet informatique | « aucun comité ne tranche » ; le directeur général n'a pas réuni les directeurs |
| **Comité de pilotage** (mensuel, puis tous les quinze jours avant la bascule) | membres : sponsor, directeur(rice) de la stratégie et des projets (directeur de projet), directeur des plateaux, DSI, directrice du réseau de prestataires, directrice des risques et de la conformité, directeur administratif et financier, chef de projet ; directeur de compte de l'ESN invité. Décisions : calendrier et jalons, disponibilité des superviseurs, leviers et surcoût, écarts au standard, décision de bascule de chaque plateau | absence d'arbitrage ; tensions entre la DSI et les plateaux |
| **Plateaux** (maître d'ouvrage) | le directeur des plateaux est maître d'ouvrage : il valide les exigences, le calendrier des superviseurs et la recette ; les trente superviseurs sont utilisateurs clés | « personne ne m'a demandé mon avis » ; superviseurs en hiver |
| **DSI** (maître d'œuvre avec l'ESN) | architecture, interfaces, reprise des données, exploitation ; spécifications détaillées des interfaces | « tout spécifier » : rôle reconnu là où il est décisif |
| **ESN** | intégration au forfait, engagements de délai, renfort sur les interfaces | — |
| **Réseau de prestataires** | adaptation de l'application des prestataires, information des prestataires | — |
| **Partenaires et constructeurs** | comité des partenaires associé dès le cadrage ; validation des interfaces dans une fenêtre fixée de la recette ; information régulière | partenaires informés par « une lettre circulaire » |
| **Comité de projet** (hebdomadaire) | chef de projet, DSI, ESN, superviseurs référents : avancement, risques, anomalies | — |

(0,5 pt pour le sponsor et le comité de pilotage ; 0,5 pt pour les rôles et la réponse aux tensions.)

**Deux règles d'arbitrage** (0,5 pt ; deux parmi les suivantes) :
- le **jalon du 30 juin 2028** et la **continuité du service jour et nuit** priment : toute décision qui les met en cause est portée au comité de pilotage ;
- le **standard de la solution** est adopté par défaut ; tout écart doit être justifié par une exigence d'un partenaire, d'un constructeur ou de la réglementation, et chiffré en délai et en coût ;
- la **disponibilité des superviseurs** est planifiée avec les plateaux un an à l'avance, hors saison d'hiver ; toute dérogation est décidée en comité de pilotage, avec un renfort pour les plateaux ;
- les **partenaires** valident les interfaces dans la fenêtre prévue ; au-delà, la validation est portée au comité des partenaires puis au comité de pilotage.

**Réponses tolérées**
- Gantt dessiné à la main plutôt que tableau, s'il porte les semaines, les antériorités, le chemin critique et les jalons.
- Dates exprimées en dates calendaires plutôt qu'en semaines, si la convention de l'annexe est appliquée de façon cohérente.
- Formation placée avant la recette, si le candidat en voit et en assume le risque de qualité (46 semaines). De même, avec le levier 1 (seul ou avec le levier 2), former d'abord (semaines 23 à 30, avant l'hiver), puis recetter en semaines 45 à 50 et basculer en semaines 51 à 56, ferait finir en semaine 56, avec quatre semaines de marge ; mais les chargés seraient formés sur une version non recettée, près de six mois avant la bascule, contre la règle de l'annexe 1.4 B : ce calendrier n'est pas recommandé, et n'est admis que si le candidat en assume explicitement le risque.
- Autre arbitrage justifié : un seul levier (le levier 2 de préférence) en assumant l'absence de marge avant l'hiver ; une dérogation obtenue du sponsor pour libérer une partie des superviseurs en hiver, avec un renfort des plateaux ; une négociation avec VIRANDOR, si le risque de perte du contrat est évalué.
- RACI présenté à la place du tableau des rôles, s'il fait apparaître un seul approbateur par décision.

**Erreurs fréquentes**
- *Gantt illisible ou sans contrainte de ressource* (`JUR-P01` Gantt lisible et pertinent) — tâches E et F menées ensemble ; juste : les superviseurs ne peuvent pas mener deux tâches en même temps.
- *Échéance jugée tenue sans l'hiver* (`JUR-T08` exploiter toutes les annexes) — 50 semaines, « dix semaines de marge » ; juste : la recette et la formation tombent dans la saison où les superviseurs ne sont pas libérés.
- *Arbitrage sans chiffres* (`JUR-T03` analyser et argumenter) — « il faut accélérer » ; juste : effet de chaque levier en semaines, coût, risque de qualité.
- *DSI désignée comme sponsor ou maître d'ouvrage* (`ET-32` MOA et MOE inversées) — juste : le sponsor est le directeur général, la maîtrise d'ouvrage revient aux plateaux.
- *Chiffrage détaillé du projet* (`JUR-T07` répondre à la seule question posée) — l'aspect budgétaire détaillé n'est pas au programme ; seules les sommes de l'annexe sont interprétées.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gantt, dates au plus tôt, chemin critique, contrainte de ressource | méthode à l'examen | F05 § 4 ; `ue3/fiches/F05_projets.md` (renvoi) | notion de cours |
| Sponsor, maîtrise d'ouvrage, maîtrise d'œuvre, comités, RACI | acteurs et organisation du projet | F05 § 1 ; F02 § 6 | notion de cours |
| Relations entre DSI, direction générale et directions métiers | instances et arbitrages | F01 ; F02 | notion de cours |

---

### 1.4 – Le contrat avec l'ESN et la gouvernance de la relation (3 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.c` « Cadre juridique applicable : responsabilité, confidentialité, SLA, RGPD » ; `1.4.a` « Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques » ; `1.4.e` « Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) ». Limite : « L'analyse juridique approfondie relève du droit des contrats informatiques et est exclue du programme de l'UE. »

**Annexes mobilisées** : annexes 1.5 (objet du contrat, extraits et commentaires de la direction juridique, rappel des exigences de DORA) et 1.1 (plateaux jour et nuit, 560 chargés, système d'information).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Première faiblesse et sa clause (en général les niveaux de service et les pénalités : engagement jour et nuit, délais de prise en charge et de rétablissement, mesure par VALMÉRIS, pénalités incitatives) ; niveau de service défini | 0,5 |
| a-2 | Deuxième faiblesse et sa clause (par exemple la sous-traitance des données personnelles et la sous-traitance de l'ESN) | 0,5 |
| a-3 | Troisième faiblesse et sa clause (par exemple l'audit et l'accès, exigés par DORA) | 0,5 |
| a-4 | Quatrième faiblesse et sa clause (par exemple la réversibilité et la stratégie de sortie, exigées par DORA, avec la propriété des interfaces) | 0,5 |
| b-1 | Instances de gouvernance (participants, fréquence, objet) à deux ou trois niveaux, avec un responsable du contrat chez VALMÉRIS et l'inscription du contrat au registre des accords | 0,5 |
| b-2 | Un indicateur complet (formule, source, fréquence, cible, axe), relié à une faiblesse du contrat | 0,5 |

**Réponse attendue**

*1.4 a) – Quatre faiblesses et les clauses qui sécurisent la relation*

La future solution de gestion des dossiers soutient l'activité principale de VALMÉRIS, jour et nuit, et l'ESN l'intégrera puis la maintiendra trois ans (2 700 k€ au total). Le projet de contrat, rédigé par l'ESN, la protège elle et laisse VALMÉRIS sans moyen de pilotage, de contrôle ni de sortie, alors que la direction des risques rappelle les exigences données de DORA pour les prestataires de services TIC : registre des accords, droits d'audit et d'accès, stratégie de sortie.

**Quatre faiblesses et leurs clauses** (0,5 pt chacune ; quatre parmi les suivantes) :

| Faiblesse (annexe 1.5) | Risque pour VALMÉRIS | Clause qui sécurise la relation |
|---|---|---|
| **Niveaux de service et pénalités** (art. 6 et 7) : prise en charge en quatre heures ouvrées, du lundi au vendredi de 8 h à 18 h ; aucun délai de rétablissement ; pénalités plafonnées à 3 % de la redevance, soit 9 k€ par an ; mesure par le seul rapport de l'ESN | une anomalie bloquante un samedi soir de neige attend lundi matin ; un appel sur cinq arrive la nuit ; la pénalité ne pèse rien face au coût d'une interruption | **convention de niveau de service** (SLA : engagement contractuel sur des niveaux mesurables) couvrant **jour et nuit, week-end et jours fériés**, avec, par priorité, un délai de **prise en charge** et un délai de **rétablissement** ; mesure à partir des outils de VALMÉRIS ; pénalités automatiques, proportionnées et plafonnées à un niveau réellement incitatif ; droit de résiliation en cas de manquements répétés |
| **Données des bénéficiaires** (art. 11) : copie des dossiers (nom, adresse, position géolocalisée, immatriculation, contrat) sans clause de sous-traitance des données personnelles | VALMÉRIS, responsable du traitement, ne peut prouver qu'elle a choisi un sous-traitant offrant des garanties ; aucune règle sur la sécurité ni sur le sort des données | **accord de sous-traitance** au sens du RGPD (art. 28) : traitement sur instructions documentées, confidentialité, mesures de sécurité, sous-traitants ultérieurs autorisés, assistance, notification des violations, suppression ou restitution des données en fin de contrat ; recette sur des données anonymisées ou fictives plutôt que sur une copie complète |
| **Sous-traitance de l'ESN** (art. 9) : travaux confiés à des filiales et partenaires, en France ou à l'étranger, sans information ni autorisation | VALMÉRIS ne sait ni qui intervient sur son logiciel le plus critique, ni où sont ses données ; la chaîne des prestataires échappe au registre des accords | **autorisation écrite préalable** de chaque sous-traitant, liste tenue à jour, **lieux de traitement et d'accès** aux données précisés, mêmes obligations (sécurité, audit, réversibilité) imposées aux sous-traitants |
| **Aucune clause d'audit ni d'accès** | VALMÉRIS ne peut vérifier ni la sécurité, ni le respect des niveaux de service, ni la conformité ; DORA demande des droits d'audit et d'accès | **clause d'audit et d'accès** : droit pour VALMÉRIS, son audit interne ou un tiers qu'elle mandate, d'auditer la prestation et d'accéder aux locaux, aux systèmes et aux documents, avec préavis, fréquence et suites des constats ; étendue aux sous-traitants |
| **Aucune réversibilité** (art. 14) et interfaces propriété de l'ESN | VALMÉRIS ne pourrait changer de prestataire ni réinternaliser sans rupture ; dépendance totale, contraire à la stratégie de sortie demandée par DORA | **plan de réversibilité** : restitution des données et des paramétrages dans un format ouvert et documenté, transfert de compétences, assistance de l'ESN sortante avec maintien du service pendant la transition, délais et coût fixés, **test** périodique ; **cession ou licence** des interfaces développées pour VALMÉRIS ; cette clause soutient la **stratégie de sortie** |
| **Aucune instance de suivi** (« un point annuel ») | la qualité de service n'est pas pilotée | comités prévus au contrat (question 1.4 b), reporting mensuel contre-vérifié |

*1.4 b) – La gouvernance de la relation avec LOMBREVAL Intégration*

VALMÉRIS désigne un **responsable du contrat** (au sein de la DSI), qui garde la compétence pour contrôler l'ESN, et inscrit le contrat au **registre des accords** avec les prestataires de services TIC tenu par la direction des risques. Trois niveaux d'instances (0,5 pt) :

| Instance | Participants | Fréquence | Objet |
|---|---|---|---|
| Comité stratégique | directeur général ou directeur(rice) de la stratégie et des projets, DSI, directrice des risques et de la conformité ; direction de l'ESN | annuel | évolution du contrat, satisfaction des plateaux, résultat de l'audit et du test de réversibilité, revue des risques liés au prestataire |
| Comité de pilotage du contrat | responsable du contrat, représentant des plateaux, directeur de compte de l'ESN | mensuel | niveaux de service mesurés, pénalités appliquées, plan d'amélioration, demandes d'évolution et priorités |
| Comité opérationnel | équipes de la DSI, superviseurs référents, équipe de maintenance de l'ESN | hebdomadaire | anomalies en cours, corrections, mises en production |

**Indicateur de suivi** (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de rétablissement dans le délai contractuel des anomalies bloquantes signalées hors heures ouvrées | nombre d'anomalies bloquantes signalées avant 8 h ou après 18 h en semaine, le week-end ou un jour férié, rétablies dans le délai contractuel / nombre d'anomalies bloquantes signalées sur ces plages | outil de gestion des tickets de VALMÉRIS (horodatage du signalement par le plateau et de la clôture), et non le seul rapport de l'ESN | mensuelle, présentée au comité de pilotage du contrat | ≥ 95 % | processus |

**Réponses tolérées**
- Autre indicateur complet relié à une faiblesse du contrat : délai de restitution constaté au dernier test de réversibilité (cible : 30 jours au plus, sans anomalie bloquante ; axe gouvernance), taux de pénalités effectivement appliquées, part des sous-traitants de l'ESN autorisés et inscrits au registre.
- Faiblesse portant sur la propriété des interfaces traitée à part de la réversibilité, si la clause proposée est précise.
- Gouvernance à deux niveaux seulement, si le pilotage mensuel des niveaux de service et la revue annuelle sont présents.
- Référence aux accords de niveau de service d'ITIL 4, si elle est appliquée au cas.

**Erreurs fréquentes**
- *Analyse juridique des clauses* (`JUR-T07` répondre à la seule question posée) — discussion du régime de responsabilité de l'ESN : hors programme ; juste : clauses de gestion qui sécurisent la relation.
- *Externalisation vue comme un transfert de responsabilité* (`JUR-A05` externalisation, sécurité, confidentialité, contractualisation) — VALMÉRIS reste responsable de son système d'information et des données des bénéficiaires.
- *SLA confondu avec un OLA* (`ET-22`) — le SLA engage l'ESN envers VALMÉRIS ; l'OLA est un accord interne.
- *DORA présenté comme une directive ou comme un texte transposé, ou assujettissement discuté* (`JUR-T07`) — c'est un règlement, applicable depuis le 17 janvier 2025 ; son application à VALMÉRIS est donnée.
- *Indicateur incomplet ou mesuré par l'ESN seule* (`ET-18`) — sans cible ni source contrôlée par VALMÉRIS, l'indicateur ne permet pas de piloter.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2022/2554 (DORA) | applicable depuis le 17/01/2025 ; cinq piliers ; prestataires tiers de services TIC : registre des accords, audit et accès, stratégie de sortie (exigences données par l'annexe 1.5 C) | `dora` ; F12 § 7 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), art. 28 | contrat de sous-traitance | `rgpd` ; F15 § 5 | en vigueur |
| Clauses critiques et gouvernance de la relation | niveaux de service, pénalités, audit, réversibilité, comités | F04 § 3 à § 5 | notion de cours |
| ITIL 4 | accords de niveau de service (réponse tolérée) | `itil_4` ; F04 § 3 | en vigueur |
