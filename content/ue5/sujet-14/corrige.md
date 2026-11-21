# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 14

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Préparer la transformation numérique de l'assistance et le projet PASSERELLE | 14 | 1.1 à 1.4 | `exercices/ex40_assistance_connectee_projet_passerelle` |
| 2 – Organiser et exploiter les données des dossiers et du réseau de prestataires | 13 | 2.1 à 2.5 | `exercices/ex41_donnees_dossiers_prestataires` |
| 3 – Renforcer la résilience opérationnelle numérique et fiabiliser les données de durabilité | 13 | 3.1 à 3.4 | `exercices/ex42_resilience_dora_audit_durabilite` |
| **Total** | **40** | | |

---

## DOSSIER 1 – PRÉPARER LA TRANSFORMATION NUMÉRIQUE DE L'ASSISTANCE ET LE PROJET PASSERELLE (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES DOSSIERS ET DU RÉSEAU DE PRESTATAIRES (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le modèle des données des dossiers et des missions | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) | 3 |
| 2.2 Les échanges de données avec les distributeurs, les constructeurs et les prestataires | `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.1.e` Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données | 2,5 |
| 2.3 Les délais d'arrivée des prestataires | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés | 3,5 |
| 2.4 Le registre commun des missions | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.e` Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain | 2 |
| 2.5 Le coût du système d'information des dossiers et son pilotage | `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) | 2 |
| **Dossier 2 – Organiser et exploiter les données des dossiers et du réseau de prestataires** |  | **13** |

Répartition indicative : connaissances (cardinalités, modèles conceptuel et logique et règles de passage, interopérabilité et ses niveaux, dimensions de la qualité, analyses descriptive et exploratoire, chaîne de traitement, fonctionnement d'un registre distribué, inducteur de coût, indicateur à cinq champs) environ 2,5 points (la moitié des items 2.1 b-1, 2.1 b-4, 2.2 a-1, 2.2 b-2, 2.3 a-1, 2.3 b-2, 2.4 a-1, 2.4 a-2, 2.5 a-1 et 2.5 b-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le modèle des données des dossiers et des missions (3 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) ». Modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites ; modèle physique seulement nommé ; aucune requête.

**Annexes mobilisées** : annexe 2.1 (règles de gestion, extrait du modèle logique actuel, précisions du directeur des plateaux, constats de 2026).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux défauts du modèle actuel, chacun rapporté à une règle de gestion et relié à un constat de l'annexe 2.1 C | 0,5 |
| a-2 | Troisième défaut, rapporté à une règle et à un constat ; conclusion : les anomalies viennent de la structure des données | 0,5 |
| b-1 | Cardinalités définies ; sept entités avec identifiant et attributs élémentaires (bénéficiaire, contrat, garantie, dossier, mission, prestataire, spécialité) | 0,5 |
| b-2 | Associations hiérarchiques et leurs cardinalités, justifiées par les règles : contrat du bénéficiaire, garantie du contrat, dossier ouvert au titre d'une garantie, missions du dossier, spécialité de la mission, prestataire qui réalise (0,1) | 0,5 |
| b-3 | Historique des propositions : association n:m entre mission et prestataire, porteuse de la date, de la réponse et du motif du refus, distincte de la réalisation ; habilitations n:m | 0,5 |
| b-4 | Modèle logique de neuf tables déduit par les règles de passage énoncées (clé étrangère côté 0,1 ou 1,1 ; table à clé composée pour chaque association n:m) | 0,5 |

**Réponse attendue**

*2.1 a) – Trois défauts du modèle logique actuel*

Trois défauts parmi les suivants (0,5 pt pour deux défauts, 0,5 pt pour le troisième et la conclusion), chacun rapporté à une règle de gestion et à un constat :

1. **Le prestataire est un texte libre dans le dossier.** La colonne « prestataire » de DOSSIER n'est pas une clé étrangère vers PRESTATAIRE, alors que RG6 confie chaque mission à un prestataire agréé, identifié par son numéro d'agrément (RG7). Rien ne garantit que le nom saisi désigne un prestataire connu : les 3 400 prestataires apparaissent sous **environ 5 000 noms** différents, et l'on ne sait pas dire combien de missions chacun a reçues. Le réseau de prestataires ne peut ni mesurer la charge ni la qualité d'un prestataire, ni rapprocher sûrement ses factures.
2. **Une seule mission par dossier.** Les heures de demande et d'arrivée et le prestataire sont des colonnes du dossier : le modèle confond le dossier et la mission, alors que RG5 prévoit une ou plusieurs missions par dossier. Les missions suivantes sont décrites dans le champ « commentaire » : **180 000 missions** sur 700 000 (700 000 payées pour 520 000 dossiers) échappent au logiciel des dossiers, à la mesure des délais et au contrôle des factures.
3. **Les refus ne sont pas conservés.** Le chargé efface le nom du prestataire qui refuse (RG6 demande d'enregistrer chaque proposition, sa réponse et le motif du refus). Une mission sur cinq a pourtant été refusée au moins une fois : on ne sait ni quels prestataires refusent, ni pourquoi (dépanneuse occupée, zone trop lointaine, heure de nuit), ni le temps perdu avant l'acceptation, qui pèse sur le délai d'arrivée.
4. **La garantie n'est pas reliée au contrat.** GARANTIE est la liste de toutes les garanties de VALMÉRIS, sans lien avec un contrat, et le contrat n'est qu'un groupe de colonnes du bénéficiaire (code du distributeur, référence, date de fin). RG3 rattache chaque garantie à un contrat, et RG4 ouvre le dossier au titre d'une garantie de l'un des contrats du bénéficiaire : rien n'empêche aujourd'hui de choisir une garantie que le contrat ne comporte pas. D'où **environ 5 000 dossiers** (à peu près 1 %) organisés et payés sans être dus.
5. **Un seul contrat par bénéficiaire.** Le contrat étant stocké dans la ligne du bénéficiaire, un bénéficiaire couvert par deux contrats (RG1) est enregistré deux fois : le modèle fabrique des doublons, qui s'ajoutent à ceux des fichiers des distributeurs (annexe 2.2).

Défauts secondaires, acceptés s'ils sont reliés à une règle ; faute de constat dans l'annexe 2.1 C, ils valent au plus 0,5 pt sur les deux items : une seule spécialité par prestataire (RG7) ; zone d'intervention réduite à la commune du dépôt, sans rayon (RG7) ; origine de l'heure d'arrivée absente (RG5).

**Conclusion** : ces anomalies ne sont pas d'abord des erreurs de saisie ; elles viennent de la **structure des données**, qui ne traduit pas les règles de gestion. Le futur logiciel du projet PASSERELLE doit reposer sur un modèle corrigé, faute de quoi la reprise des données reconduira les défauts.

*2.1 b) – Le modèle conceptuel et le modèle logique des données des dossiers et des missions*

**Les cardinalités** (0,5 pt avec les entités) : dans un modèle conceptuel des données, chaque patte d'une association porte une cardinalité minimale et une cardinalité maximale, qui disent combien de fois, au moins et au plus, une occurrence de l'entité participe à l'association (0,1 ; 1,1 ; 0,n ; 1,n). Elles traduisent les règles de gestion : « une mission porte sur une seule spécialité » donne 1,1 du côté de la mission. Le modèle conceptuel est indépendant de toute technique et ne comporte aucune clé étrangère ; le modèle logique le traduit en tables (F07 § 1 à 3).

**Les entités** (identifiant souligné dans la copie, ici en premier) :
- **Beneficiaire** (num_beneficiaire, nom, prenom, telephone) ;
- **Contrat** (num_contrat, ref_distributeur, code_distributeur, date_effet, date_fin) : le code du distributeur est un simple attribut, la liste des distributeurs n'étant pas à modéliser (RG2) ;
- **Garantie** (num_garantie, code_garantie, libelle_garantie, plafond_eur) : la garantie d'un contrat ; son code renvoie à la liste des garanties de VALMÉRIS, qui devient la codification commune (question 2.2) ;
- **Dossier** (num_dossier, date_heure_ouverture, plateau, type_evenement, date_heure_evenement, lieu_evenement) ;
- **Mission** (num_mission, date_heure_creation, date_heure_arrivee, origine_heure_arrivee) : le délai d'arrivée n'est pas stocké, il se calcule à partir des heures enregistrées ;
- **Prestataire** (num_agrement, raison_sociale, telephone, commune_depot, rayon_km) ;
- **Specialite** (code_specialite, libelle_specialite).

**Les associations et leurs cardinalités** (0,5 pt pour les associations hiérarchiques, 0,5 pt pour l'historique des propositions) :

| Association | Entités et cardinalités | Règle de gestion |
|---|---|---|
| *couvrir* | Contrat (1,1) — Beneficiaire (1,n) | RG1 et RG2 : un contrat couvre un seul bénéficiaire ; un bénéficiaire est couvert par un ou plusieurs contrats |
| *comprendre* | Garantie (1,1) — Contrat (1,n) | RG3 : une garantie appartient à un seul contrat ; un contrat en comprend au moins une |
| *etre_ouvert_au_titre_de* | Dossier (1,1) — Garantie (0,n) | RG4 : un dossier est ouvert au titre d'une seule garantie ; une garantie peut n'avoir donné lieu à aucun dossier |
| *donner_lieu* | Mission (1,1) — Dossier (1,n) | RG5 : un dossier donne lieu à au moins une mission ; une mission relève d'un seul dossier |
| *porter_sur* | Mission (1,1) — Specialite (0,n) | RG5 et RG8 : une mission porte sur une seule spécialité |
| *etre_propose* (date_heure_proposition, reponse, date_heure_reponse, motif_refus) | Mission (1,n) — Prestataire (0,n) | RG6 : une mission est proposée à un ou plusieurs prestataires, une fois chacun ; un prestataire nouvellement agréé peut n'avoir reçu aucune proposition ; les dates et heures d'envoi et de réponse, la réponse et le motif dépendent du couple mission-prestataire : ce sont des attributs de l'association |
| *realiser* | Mission (0,1) — Prestataire (0,n) | RG6 : la mission est réalisée par le prestataire qui l'a acceptée, et par aucun tant qu'elle n'est pas acceptée |
| *etre_habilite* | Prestataire (1,n) — Specialite (0,n) | RG7 et RG8 : un prestataire est habilité pour une ou plusieurs spécialités ; une spécialité nouvelle peut n'être exercée par personne |

**L'historique des refus** : chaque proposition, acceptée ou refusée, est une occurrence de l'association *etre_propose*, avec la date et l'heure de son envoi, la réponse, la date et l'heure de cette réponse et le motif : rien n'est plus effacé. On peut alors compter les refus par prestataire, par motif et par zone, et mesurer le temps écoulé entre la création de la mission et son acceptation (heure de la réponse de la proposition acceptée). La réalisation est une association distincte (0,1), car le prestataire qui réalise la mission est le seul qui l'a acceptée.

Le dossier n'est pas relié directement au bénéficiaire : on le retrouve par la garantie, puis le contrat, qui couvre un seul bénéficiaire (RG2). Une association directe serait redondante et permettrait d'ouvrir un dossier pour un bénéficiaire au titre de la garantie d'un autre. Le modèle rend aussi impossible le défaut 4 : un dossier ne peut plus être ouvert qu'au titre d'une garantie qui appartient à un contrat.

**Le modèle logique** (0,5 pt), obtenu par les règles de passage :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire ;
2. pour une association dont l'une des pattes a pour cardinalité maximale 1 (*couvrir*, *comprendre*, *etre_ouvert_au_titre_de*, *donner_lieu*, *porter_sur*, *realiser*), la clé primaire de l'entité du côté « n » migre comme clé étrangère dans la table de l'entité du côté 1 ; elle est obligatoire si la cardinalité minimale est 1, facultative si elle est 0 (le prestataire de la mission, *realiser*) ;
3. une association dont les deux cardinalités maximales sont n (*etre_propose*, *etre_habilite*) devient une table dont la clé primaire est composée des clés des deux entités, chacune clé étrangère, et qui porte les attributs de l'association.

- Beneficiaire (<u>num_beneficiaire</u>, nom, prenom, telephone)
- Contrat (<u>num_contrat</u>, ref_distributeur, code_distributeur, date_effet, date_fin, #num_beneficiaire)
- Garantie (<u>num_garantie</u>, code_garantie, libelle_garantie, plafond_eur, #num_contrat)
- Dossier (<u>num_dossier</u>, date_heure_ouverture, plateau, type_evenement, date_heure_evenement, lieu_evenement, #num_garantie)
- Mission (<u>num_mission</u>, date_heure_creation, date_heure_arrivee, origine_heure_arrivee, #num_dossier, #code_specialite, #num_agrement)
- Prestataire (<u>num_agrement</u>, raison_sociale, telephone, commune_depot, rayon_km)
- Specialite (<u>code_specialite</u>, libelle_specialite)
- Proposition (<u>#num_mission, #num_agrement</u>, date_heure_proposition, reponse, date_heure_reponse, motif_refus)
- Habilitation (<u>#num_agrement, #code_specialite</u>)

La clé composée de Proposition traduit la règle « un même prestataire ne reçoit qu'une proposition pour une mission donnée ». Le numéro d'agrément de Mission est vide tant que la mission n'est pas acceptée. Deux contrôles relèvent du modèle physique ou du logiciel, et non du modèle logique : le prestataire qui réalise la mission doit être celui qui l'a acceptée, et il doit être habilité pour la spécialité de la mission.

**Réponses tolérées**
- Formalisme différent (notation « pattes de corbeau », schéma relationnel dessiné), s'il est lisible et cohérent (`JUR-T10`).
- Garantie modélisée comme une liste commune de garanties, reliée au contrat par une association n:m porteuse du plafond, si le candidat montre comment le dossier reste rattaché à une garantie du contrat (association vers le couple contrat-garantie, ou contrôle explicite).
- Contrat couvrant plusieurs bénéficiaires (association n:m) et association directe entre le dossier et le bénéficiaire, si l'hypothèse est écrite et la redondance discutée.
- Prestataire retenu déduit de la proposition acceptée, sans association *realiser*, si le candidat énonce la contrainte d'une seule acceptation par mission.
- Entité Partenaire ou Distributeur ajoutée, ou zone d'intervention modélisée à part, si le candidat la justifie, malgré RG2.

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dessinées dans le modèle conceptuel, ou modèle logique qui ne découle pas du modèle conceptuel.
- *Mission et dossier confondus* — une seule entité Dossier qui reçoit le prestataire et les heures : c'est le défaut de l'annexe 2.1 B reproduit.
- *Refus perdus* — association mission-prestataire 1:n (le seul prestataire retenu), sans les propositions refusées ni leurs attributs ; ou attributs de la proposition placés dans la table Mission.
- *Garantie flottante* — garantie sans lien avec le contrat, qui laisse possible l'ouverture d'un dossier au titre d'une garantie non souscrite.
- *Morceau de cours ou requête hors attente* (`JUR-T01`, `JUR-T07`) — règles de passage récitées sans les appliquer, ou requêtes écrites alors que la question n'en demande pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, modèle logique, modèle physique ; cardinalités ; règles de passage | définitions et méthode | F07 § 1 à 4 | notion de cours |

---

### 2.2 – Les échanges de données avec les distributeurs, les constructeurs et les prestataires (2,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) », sans détail des échanges techniques ; `2.1.e` « Gouvernance de la donnée : qualité, cycle de vie, dictionnaire de données ». L'interopérabilité est traitée sur le plan technique et sur le plan organisationnel, comme le demande le programme.

**Annexes mobilisées** : annexes 1.1 (quinze distributeurs, deux constructeurs, application des prestataires, progiciel de règlement, organigramme), 2.1 (doublons créés par le modèle), 2.2 (flux, anomalies, définitions, responsabilités) et 2.6 (RGPD : exactitude des données ; DAMA-DMBOK).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Interopérabilité et qualité des données définies ; premier problème rattaché à un niveau d'interopérabilité et à une dimension de la qualité, avec sa conséquence chiffrée | 0,5 |
| a-2 | Deux autres problèmes, chacun rattaché à un niveau et à une dimension, avec sa conséquence | 0,5 |
| b-1 | Formats ouverts et interfaces de programmation : canal cible pour chaque flux, en temps réel quand le service l'exige | 0,5 |
| b-2 | Codification commune des garanties et dictionnaire des données défini et appliqué aux trois notions de l'annexe 2.2 C | 0,5 |
| b-3 | Contrôles à l'entrée (format, code, doublon, rejet tracé) et responsabilités : propriétaire et intendant des données des partenaires, engagements de qualité dans les conventions de distribution | 0,5 |

**Réponse attendue**

*2.2 a) – Trois problèmes d'interopérabilité et de qualité*

**Définitions** (0,5 pt avec le premier problème) : l'**interopérabilité** est la capacité de systèmes et d'organisations hétérogènes à échanger des données et à les utiliser sans intervention manuelle. Elle se joue à quatre niveaux : **technique** (canaux, interfaces de programmation), **syntaxique** (formats : XML, JSON, fichiers à séparateurs), **sémantique** (même sens des données : dictionnaire, codifications communes) et **organisationnel** (processus, responsabilités, engagements entre partenaires) (F07 § 7). La **qualité des données** est leur aptitude à servir l'usage prévu ; elle se mesure selon des dimensions : exactitude, complétude, unicité, cohérence, actualité (fraîcheur) (F07 § 8.3).

Trois problèmes parmi les suivants (0,5 pt pour le premier avec les définitions, 0,5 pt pour les deux autres) :

| Problème (annexe 2.2) | Niveau d'interopérabilité | Dimension de la qualité | Conséquence |
|---|---|---|---|
| **Codes de garanties propres à chaque distributeur et dates sous trois formes** : 1 200 codes pour 40 garanties, traduits à la main ; 3 % de codes inconnus ou mal traduits ; 15 000 dates de fin erronées | sémantique (même garantie, codes différents) et syntaxique (formats de date et de fichier) | exactitude, cohérence | une garantie refusée à un bénéficiaire couvert, ou accordée à tort (les 5 000 dossiers hors contrat de l'annexe 2.1 en sont en partie la suite) ; deux informaticiens mobilisés pour tenir la table de correspondance |
| **Bénéficiaires en double et introuvables** : 300 000 doublons (un sur vingt), 26 000 dossiers ouverts « sous réserve » (5 %) ; « bénéficiaire » n'a pas le même sens pour tous les distributeurs | sémantique (définition du bénéficiaire) et organisationnel (fichier en retard ou rejeté, sans engagement du distributeur) | unicité, actualité, complétude | pour le bénéficiaire en détresse, cinq minutes d'appel en plus et un doute sur sa prise en charge ; pour les plateaux, plus de 2 000 heures d'appel perdues (26 000 × 5 minutes) ; des statistiques par bénéficiaire faussées |
| **Ruptures de la chaîne et ressaisies** : environ 30 000 alertes des constructeurs reçues par interface de programmation mais transmises par courriel et ressaisies ; acceptations et heures d'arrivée renvoyées une fois par nuit, refus restés dans l'application ; 700 000 factures en PDF ou sur papier ressaisies par 25 agents, dont 4 % avec une erreur | technique (le logiciel des dossiers ne sait pas lire les alertes ni recevoir les événements en temps réel) et syntaxique (factures non structurées) | actualité, exactitude | impossible d'informer le bénéficiaire en temps réel ni de déclencher l'assistance sans appel, deux objectifs d'« Assister 2030 » ; erreurs de règlement et réclamations des prestataires ; temps des agents absorbé par la saisie |
| **Absence de dictionnaire et de responsable** : « délai d'arrivée » et « dossier clos » définis autrement selon les plateaux ou les directions ; aucune direction responsable des données reçues ; conventions de distribution sans clause de qualité | sémantique et organisationnel | cohérence | des indicateurs incomparables entre plateaux (question 2.3) ; la DSI corrige chaque nuit les fichiers des autres, sans que la cause soit traitée à la source |

*2.2 b) – L'organisation cible des échanges en quatre mesures*

1. **Des formats ouverts et des interfaces de programmation** (0,5 pt). Une **interface de programmation** (API) est un point d'accès normalisé et documenté par lequel un système met à disposition ou reçoit des données d'un autre, selon un contrat d'interface (données échangées, versions, sécurité) ; un **format ouvert** est un format dont la spécification est publique et qui ne dépend d'aucun éditeur. Appliqué aux flux de VALMÉRIS :
   - contrats et bénéficiaires : un **format d'échange unique**, ouvert et publié par VALMÉRIS (par exemple un fichier XML ou JSON décrit par un schéma), imposé aux quinze distributeurs à la place des neuf formes actuelles ; une interface de programmation pour les distributeurs qui le peuvent, afin qu'un contrat souscrit dans la journée soit connu le jour même ;
   - alertes des véhicules connectés : intégration directe dans le futur logiciel des dossiers (projet PASSERELLE), qui ouvre le dossier sans ressaisie ; un format d'alerte commun, proposé aux deux constructeurs puis aux autres partenaires ;
   - application des prestataires : échange des acceptations, des refus et des positions **en temps réel** par interface de programmation, et non plus par un fichier de nuit, condition de l'information du bénéficiaire en temps réel ;
   - factures : facture structurée déposée dans l'application et rattachée à la mission, au lieu du PDF et du papier ressaisis.
2. **Une codification commune des garanties et un dictionnaire des données** (0,5 pt). La liste des 40 garanties de VALMÉRIS devient la **codification de référence** : chaque distributeur transmet ce code, et non plus le sien, ce qui supprime la table de correspondance de 1 200 codes. Le **dictionnaire des données** décrit chaque donnée échangée : nom, définition, format, valeurs admises, règle de calcul, source, propriétaire. Il tranche les trois notions de l'annexe 2.2 C :
   - *bénéficiaire* : la personne couverte, nommément désignée dans le contrat ;
   - *délai d'arrivée* : durée entre l'ouverture du dossier et l'arrivée géolocalisée du prestataire, la même sur les trois plateaux ;
   - *dossier clos* : fin de la dernière mission, la date de paiement de la dernière facture étant une autre donnée.
   Le DAMA-DMBOK range ces travaux dans les domaines de l'intégration et de l'interopérabilité, des métadonnées et des données de référence (annexe 2.6).
3. **Des contrôles à l'entrée des données** (0,5 pt avec la quatrième mesure). Chaque fichier ou message reçu est contrôlé avant chargement :
   - format des dates et des champs obligatoires ;
   - code de garantie existant dans la codification ;
   - cohérence des dates d'effet et de fin ;
   - rapprochement des bénéficiaires déjà connus selon une règle d'identité écrite (nom, prénom, téléphone, contrat), pour ne pas créer de doublon.
   Les enregistrements rejetés sont renvoyés au distributeur, avec le motif et un délai de correction, et inscrits dans un journal des rejets ; un taux de rejet est suivi par distributeur. L'exactitude des données est d'ailleurs un principe que rappelle le RGPD (annexe 2.6).
4. **Des responsabilités sur les données reçues des partenaires.** Un **propriétaire** métier des données des contrats et des bénéficiaires est désigné, par exemple le service des relations avec les partenaires, qui négocie les conventions de distribution ; un **intendant** (responsable des données des partenaires) tient le dictionnaire et la codification, suit la qualité par distributeur et anime la correction à la source avec les distributeurs et la DSI. Les conventions de distribution comprennent un **engagement de qualité** : format, fréquence, délai de transmission, taux d'erreur maximal et circuit de correction. La DSI exploite les échanges mais ne corrige plus seule les fichiers des autres.

**Réponses tolérées**
- Autres problèmes tirés de l'annexe 2.2 (neuf formes de fichiers, partenaires sans alertes), s'ils sont rattachés à un niveau et à une dimension.
- Niveau d'interopérabilité rattaché autrement, s'il est justifié (dates : syntaxique ou sémantique).
- Plateforme d'échange ou bus d'échange proposés comme canal unique entre les distributeurs et le logiciel des dossiers, sans détail technique.
- Données de référence des garanties présentées comme un petit référentiel, si le rôle des distributeurs est précisé.
- Responsable des données des partenaires rattaché à la DSI, si le propriétaire métier est distinct.

**Erreurs fréquentes**
- *Interopérabilité réduite à la technique* (`ET-36`) — « mettre des API » sans codification commune, sans dictionnaire ni responsabilités.
- *Détail technique hors attente* (`JUR-T07`) — description des échanges techniques, des schémas ou des mécanismes d'authentification, que la question exclut.
- *Qualité sans mesure* — problèmes énoncés sans les chiffres de l'annexe (un sur vingt, 5 %, 3 %, 4 %) ni leur conséquence pour le bénéficiaire.
- *Correction en aval seulement* — nettoyage nocturne renforcé, au lieu de la correction à la source et des engagements des distributeurs.
- *Morceau de cours* (`JUR-T01`) — niveaux d'interopérabilité et dimensions de la qualité récités sans application aux flux de VALMÉRIS.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| DAMA-DMBOK, 2e édition (2017), révision 2024 | domaines intégration et interopérabilité, métadonnées, données de référence, qualité | `dama_dmbok2` / F07 § 8.2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | exactitude des données (annexe 2.6) | `rgpd` / F15 | en vigueur |
| Interopérabilité et ses quatre niveaux, interface de programmation, format ouvert, dictionnaire des données, dimensions de la qualité, propriétaire et intendant | définitions et méthode | F07 § 1, 7, 8.1 et 8.3 | notion de cours |

---

### 2.3 – Les délais d'arrivée des prestataires (3,5 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés ». Aucun calcul statistique ni aucune manipulation d'outil ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexes 2.3 (indicateurs par plateau, missions par zone, affirmation du directeur des plateaux, limites) et 2.2 C (définition du délai propre à Valence) ; « Assister 2030 » (présentation).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Analyses descriptive et exploratoire définies et distinguées ; démarche justifiée par l'annexe 2.3 (descriptive d'abord, exploratoire ensuite) | 0,5 |
| a-2 | Premier constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| a-3 | Deuxième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| a-4 | Troisième constat argumenté et chiffré, avec sa précaution de lecture | 0,5 |
| b-1 | Affirmation appréciée : structure des zones, définition du délai, heures saisies à la main, satisfaction, objectif mal lu ; conclusion nuancée | 0,5 |
| b-2 | Effets pervers de la prime ; deux évolutions de la chaîne de traitement (collecte, nettoyage, structuration) qui rendent la comparaison juste | 0,5 |
| c-1 | Deux représentations adaptées au comité de direction, chacune justifiée par son message et par le piège évité | 0,5 |

**Réponse attendue**

*2.3 a) – La démarche et trois constats*

**La démarche** (0,5 pt) : l'**analyse descriptive** résume ce qui s'est passé (niveaux, évolutions, répartitions, écarts à un objectif) ; l'**analyse exploratoire** croise les données, sans hypothèse arrêtée, pour repérer des profils, des valeurs atypiques et des pistes d'explication ; elle prépare les explications sans les démontrer (F08 § 2). On retient :
- l'**analyse descriptive d'abord** : le comité de direction veut savoir où en sont les délais en 2026 par rapport à 2025 et à l'objectif de − 20 % d'ici 2029 ;
- puis l'**analyse exploratoire**, parce que l'annexe signale des facteurs qui brouillent la comparaison (météo, zones, mode de saisie, définition du délai) : il faut croiser les délais avec la saison, le type de zone, l'origine de l'heure d'arrivée et les refus avant d'en tirer un jugement sur les plateaux.

**Trois constats** parmi les suivants (0,5 pt chacun : le fait chiffré, son interprétation au regard d'« Assister 2030 », la précaution de lecture) :

1. **La légère baisse du délai moyen en 2026 tient à l'hiver doux.** Le délai moyen de l'ensemble passe de 50 à 48 minutes ; mais pendant les trois mois d'hiver, il tombe de 60 à 52 minutes, et de mars à novembre il reste à 47 minutes les deux années. Aucun progrès durable n'est donc acquis ; l'objectif de − 20 % (environ 38 minutes en 2029 si l'on part de 48) reste entier, et un hiver rigoureux le ferait remonter. *Précaution* : deux années seulement, et une base de 2026 favorable : l'année de référence de l'objectif doit être fixée et corrigée de la météo.
2. **La moyenne cache une queue de délais longs, surtout à Metz.** Sur chaque plateau, la moyenne dépasse la médiane (Limoges 47 contre 38, Metz 56 contre 42, Valence 38 contre 30) : quelques attentes très longues, en zone rurale (74 minutes en moyenne, contre 32 en ville), tirent la moyenne vers le haut. Près d'un quart des arrivées (23 %) dépassent encore 60 minutes, 30 % à Metz : ce sont elles qui exposent le bénéficiaire immobilisé au bord d'une route et qui font les réclamations. *Précaution* : on ne peut pas combiner les médianes des plateaux pour obtenir celle de l'ensemble ; il faudrait la distribution des délais par classes.
3. **La dégradation de Metz est d'abord un effet de structure.** Metz passe de 50 à 56 minutes, de 24 % à 30 % d'arrivées au-delà d'une heure et de 82 % à 74 % de satisfaits, alors que sa part de missions rurales passe de 25 % à 40 % avec les quatre départements reçus de Limoges. À zone égale, ses délais (34, 50 et 76 minutes) ne dépassent ceux de Limoges que de 2 à 4 minutes ; avec sa répartition de 2025, son délai moyen tournerait autour de 50 minutes, comme en 2025. En revanche, ses refus bondissent (20 % à 28 %) : le réseau de prestataires y est trop peu dense. *Précaution* : les délais par zone de 2025 ne sont pas donnés ; c'est une hypothèse à vérifier, qui oriente l'action vers le réseau, non vers les chargés de Metz.
4. **Les délais de Valence sont les moins fiables.** Valence affiche les délais les plus courts (38 minutes), mais 70 % de ses heures d'arrivée sont saisies à la main par le prestataire (30 % à 35 % ailleurs), son délai est compté depuis l'acceptation de la mission, une dizaine de minutes après l'ouverture du dossier (annexe 2.2 C), et ses bénéficiaires ne sont pas plus satisfaits du délai (79 % contre 83 % à Limoges). *Précaution* : la satisfaction repose sur 15 % de répondants, qui ne sont pas forcément représentatifs ; l'écart de satisfaction est un signal, pas une preuve.
5. **Les refus augmentent** (18 % à 20 % pour l'ensemble) : chaque refus retarde l'arrivée. Le délai d'acceptation, non mesuré aujourd'hui, est une piste d'amélioration du délai total. *Précaution* : les refus sont lus dans l'application des prestataires, sans motif (annexe 2.1 C).

*2.3 b) – L'affirmation et la proposition du directeur des plateaux*

**L'affirmation de M. CORTHELAY** (0,5 pt) : « Valence est notre meilleur plateau » n'est pas démontré, pour quatre raisons :
- **un effet de structure** : 70 % des missions de Valence sont urbaines, contre 40 % à Limoges et 30 % à Metz. À zone égale et selon sa propre mesure, Valence n'a d'avance qu'en ville (30 minutes contre 32 et 34), et cette avance de 2 à 4 minutes est inférieure à la dizaine de minutes que lui retire sa définition du délai ; il est moins rapide que Limoges en zone périurbaine (48 contre 46) et rurale (74 contre 72). Avec la répartition de Limoges, son délai serait d'environ 47 minutes, comme celui de Limoges : la comparaison des moyennes globales est trompeuse (paradoxe de Simpson) ;
- **une définition différente** : compté depuis l'acceptation, et non depuis l'ouverture du dossier, le délai de Valence est raccourci d'une dizaine de minutes ; à définition commune, il serait de l'ordre de 48 minutes ;
- **une mesure déclarative** : 70 % des heures de Valence sont saisies par le prestataire lui-même, sans contrôle, et la satisfaction de ses bénéficiaires n'est pas meilleure qu'ailleurs ;
- **une lecture erronée de l'objectif** : la cible d'environ 38 minutes vaut pour l'ensemble de VALMÉRIS, à partir de sa base de 2026 ; un plateau urbain qui affiche 38 minutes selon sa propre mesure ne l'« atteint » pas. Retenir le seul chiffre qui conforte sa conviction relève du **biais de confirmation**.

Conclusion : à mesure commune, rien n'indique que Valence soit le plus rapide, même en ville ; il serait plutôt le plus lent. On ne peut ni le classer premier, ni en faire le modèle des autres plateaux, tant que la définition et la mesure ne sont pas communes.

**La prime et la chaîne de traitement** (0,5 pt) : une prime liée au délai moyen, calculé sur des heures saisies à la main et selon des règles propres à chaque plateau, inciterait à **embellir la mesure** plutôt qu'à réduire le délai réel. Elle pénaliserait Metz, qui a reçu des zones rurales, et pousserait à délaisser les missions lointaines. Une prime éventuelle ne se conçoit qu'après la fiabilisation de la mesure, sur un indicateur comparé à zone égale.

Deux évolutions de la chaîne de traitement, parmi :
- **collecte** : heure d'arrivée relevée par la géolocalisation de l'application, la saisie manuelle devenant l'exception justifiée ; heure d'ouverture du dossier, heure de création de la mission et heures d'envoi et de réponse de chaque proposition, donc heure d'acceptation, enregistrées pour chaque mission (modèle de la question 2.1) ; type de zone rattaché à chaque mission ;
- **nettoyage** : marquage de l'origine de chaque heure (géolocalisée ou déclarée) ; repérage des valeurs impossibles (arrivée avant la création de la mission, délai nul) et des valeurs aberrantes, vérifiées plutôt que supprimées ; dédoublonnage des missions ;
- **structuration** : une seule définition du délai d'arrivée, écrite dans le dictionnaire (de l'ouverture du dossier à l'arrivée géolocalisée), et des dimensions communes (plateau, type de zone, mois et saison, spécialité, origine de l'heure), pour comparer les plateaux **à zone et à saison égales**, avec la médiane et la part au-delà de 60 minutes à côté de la moyenne.

*2.3 c) – Deux représentations pour le comité de direction*

Deux représentations parmi (0,5 pt) :
- **Barres groupées du délai médian et de la part des arrivées au-delà de 60 minutes, par plateau et par type de zone.** *Message* : à zone égale, les plateaux sont proches ; les écarts tiennent surtout à la part des zones rurales. *Piège évité* : la moyenne globale par plateau, qui mêle des structures de zones différentes (effet de structure).
- **Courbe mensuelle du délai d'arrivée sur 2025 et 2026**, les mois d'hiver signalés, avec la trajectoire de l'objectif de 2029 tracée depuis l'année de référence. *Message* : la baisse de 2026 vient de l'hiver ; hors hiver, rien n'a changé. *Piège évité* : l'extrapolation d'une année douce et la comparaison de deux chiffres annuels.
- **Histogramme de la distribution des délais**, par classes de 15 minutes, par plateau. *Message* : la queue des attentes longues, que la moyenne et la médiane ne montrent pas. *Piège évité* : la moyenne seule, qui masque la dispersion.
- **Barres empilées à 100 % de l'origine des heures d'arrivée** (géolocalisée ou déclarée), par plateau, à côté des délais. *Message* : la fiabilité de la mesure diffère d'un plateau à l'autre. *Piège évité* : comparer des mesures de fiabilité inégale comme si elles se valaient.

Un classement des trois plateaux sur leur seul délai moyen, ou un histogramme à l'axe tronqué qui grossit l'écart entre Valence et Metz, sont de mauvais choix.

**Réponses tolérées**
- Analyse diagnostique présentée comme une variante de l'analyse exploratoire ; analyse prédictive écartée faute d'historique suffisant.
- Autres constats tirés de l'annexe 2.3 (satisfaction stable pour l'ensemble, hausse des refus à Metz), s'ils sont chiffrés et assortis d'une précaution.
- Effet de structure démontré par la lecture du tableau B sans le calcul de « 47 minutes », qui n'est pas attendu.
- Effets de la zone et de la définition croisés (environ 40 minutes en ville, à définition commune), sans calcul détaillé.
- Évolutions de la chaîne de traitement portant sur l'analyse ou la restitution, si elles rendent la comparaison juste.
- Autres représentations (carte des délais médians par département, petits multiples par plateau, jauge de l'objectif), si le message et le piège évité sont précisés.

**Erreurs fréquentes**
- *Corrélation présentée comme une causalité* (`ET-26`) — délais de Valence attribués à son organisation, sans examiner les zones, la définition du délai et la saisie à la main.
- *Prudence d'interprétation oubliée* (`JUR-D06`) — amélioration de 2026 lue comme un progrès durable, malgré l'hiver doux ; objectif jugé atteint par un plateau.
- *Calcul hors attente* (`JUR-T07`) — moyennes pondérées recalculées en détail ou tests statistiques, alors que la question demande des constats argumentés en chiffres ronds.
- *Moyenne et médiane confondues* — médianes des plateaux additionnées ou moyennées pour obtenir celle de l'ensemble.
- *Morceau de cours* (`JUR-T01`) — définitions des méthodes d'analyse sans application aux plateaux et aux années de l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Analyses descriptive et exploratoire, chaîne de traitement, choix des graphiques, biais de confirmation, effet de structure et paradoxe de Simpson, corrélation et causalité | définitions et méthode | F08 § 1, 2 et 5 | notion de cours |
| Dictionnaire des données, dimensions d'analyse | structuration | F07 § 1 et 6 | notion de cours |

---

### 2.4 – Le registre commun des missions (2 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.e` « Analyse de la valeur ajoutée, des coûts et des limites d'un projet blockchain ». Le fonctionnement est expliqué en principe, sans développement du registre ni du contrat automatisé ; aucun cryptoactif ni jeton, aucune analyse juridique.

**Annexes mobilisées** : annexes 1.1 (3 400 prestataires, progiciel de règlement, application des prestataires), 2.3 (heures d'arrivée saisies à la main), 2.4 (proposition du consortium, coûts, contestations, objections de la DSI, plateforme centralisée) et 2.6 (RGPD, ISO 22739:2024).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Registre partagé répliqué entre les cinq nœuds, blocs chaînés par des empreintes (inaltérabilité pratique), consensus entre membres identifiés | 0,5 |
| a-2 | Clés privée et publique, signature de chaque inscription ; contrat automatisé (« si … alors », règlement en euros) ; différence avec une base de données centralisée | 0,5 |
| b-1 | Valeur ajoutée appliquée (preuve partagée, contestations, paiement rapide) et coûts sur trois ans : 1 000 k€ contre 450 k€ | 0,5 |
| b-2 | Trois limites tirées des annexes (oracle, données personnelles, gouvernance, périmètre, intégration) ; avis motivé et conditions | 0,5 |

**Réponse attendue**

*2.4 a) – Le fonctionnement du registre proposé*

Un **registre distribué** est un registre d'opérations dont chaque participant détient une copie, mise à jour selon une règle de consensus, sans administrateur central unique ; une **chaîne de blocs** est un registre distribué où les opérations sont regroupées en blocs chaînés (F11 § 1 ; vocabulaire de l'ISO 22739:2024, annexe 2.6). Appliqué au projet :
- **un registre partagé** (0,5 pt avec les blocs et le consensus) : les cinq membres (trois assisteurs, deux fédérations) exploitent chacun un nœud qui détient une copie complète du registre ; chacun peut vérifier ce que les autres ont inscrit ;
- **des blocs chaînés par des empreintes** : chaque bloc contient l'empreinte (le résultat du hachage) du bloc précédent. Modifier une mission ou une facture déjà inscrite changerait l'empreinte de son bloc et romprait la chaîne, ce que les autres nœuds verraient aussitôt : le registre est **pratiquement inaltérable** et horodaté, sans l'être absolument (trois membres sur cinq qui s'entendraient pourraient réécrire la chaîne) ;
- **un consensus entre membres identifiés** : un bloc n'est ajouté qu'avec l'accord d'au moins trois des cinq nœuds. C'est une chaîne **privée et permissionnée**, dite de consortium : seuls des membres admis valident, sans minage ; la consommation d'énergie est donc faible, contrairement aux chaînes publiques à preuve de travail ;
- **des clés et des signatures** (0,5 pt avec le contrat automatisé et la distinction) : chaque membre et chaque dépanneur détient une **clé privée**, secrète, avec laquelle il signe ses inscriptions, et une **clé publique**, connue de tous, qui permet de vérifier la signature. On sait ainsi qui a inscrit quoi, et l'auteur ne peut pas le nier : l'assisteur sa mission, le dépanneur son arrivée et sa facture ;
- **un contrat automatisé** (contrat intelligent) : un programme inscrit dans le registre exécute une règle « si … alors » : si la fin de l'intervention est inscrite et si la facture respecte le barème, alors l'ordre de virement est émis. Le règlement se fait **en euros**, par le circuit bancaire habituel de l'assisteur, sans jeton ni cryptoactif.

**La différence avec une base de données centralisée** : une base centralisée, même répartie sur plusieurs serveurs, est tenue par un seul administrateur, qui peut corriger ou supprimer une donnée ; ceux qui la consultent doivent lui faire confiance. Le registre distribué organise la confiance entre des acteurs qui ne se font pas confiance, ici des assisteurs concurrents et des dépanneurs, par la réplication, le consensus et l'inaltérabilité, au prix de la performance, du coût et de la souplesse.

*2.4 b) – Valeur ajoutée, coûts, limites et avis*

**La valeur ajoutée et les coûts** (0,5 pt) :
- *valeur ajoutée* : une **version unique des faits**, horodatée et signée, partagée entre l'assisteur et le dépanneur, qui peut réduire les contestations (15 000 factures en 2026, soit 5 %, qui occupent dix agents, environ 500 k€ par an) ; un **paiement en 48 heures**, argument fort pour attirer et garder les meilleurs dépanneurs ; un seul outil pour les dépanneurs qui travaillent avec plusieurs assisteurs ;
- *coûts sur trois ans, de tête* : registre : 300 (construction) + 250 (raccordement) + 3 × 150 (fonctionnement) = **1 000 k€** ; plateforme centralisée : 300 + 3 × 50 = **450 k€**, soit **550 k€ d'écart**. Or la plateforme apporte l'essentiel du même gain : facture rattachée à la mission, contrôlée par rapport au barème et aux heures géolocalisées, payée sous dix jours, pour tous les prestataires et non pour les seuls dépanneurs.

**Les limites et l'avis** (0,5 pt), en trois limites parmi :
- **le problème de l'oracle** : le registre garantit que l'inscription n'a pas changé, pas qu'elle est vraie. Les contestations portent sur l'heure d'arrivée, la distance et la majoration de nuit ; si l'heure est saisie à la main (38 % des heures en 2026, 70 % à Valence), elle sera inscrite à la main « pour toujours ». C'est la fiabilité de la donnée à la source (géolocalisation) qui réduit les litiges ;
- **les données personnelles** : nom, téléphone, immatriculation, lieu et photos des véhicules seraient copiés chez deux concurrents et ne pourraient plus être effacés, ce qui heurte la minimisation et la limitation de la durée de conservation (annexe 2.6). Il faudrait n'inscrire qu'une **empreinte** des missions et garder les données elles-mêmes hors du registre. S'y ajoute la confidentialité des barèmes face aux concurrents ;
- **la gouvernance du consortium** : décisions à la majorité de cinq membres, dont deux fédérations de dépanneurs, qui pourraient imposer des barèmes à VALMÉRIS ; rien n'est prévu en cas de désaccord, de sortie d'un membre ou d'erreur du contrat automatisé ;
- **le périmètre** : environ 600 des 1 400 dépanneurs du réseau, soit moins de la moitié, et aucune autre spécialité (serruriers, plombiers, aide à domicile) : VALMÉRIS devrait de toute façon tenir un second circuit ;
- **l'intégration** : le raccordement à l'ancien logiciel serait à refaire avec la solution du projet PASSERELLE ;
- **l'automatisme** : un contrat automatisé qui paie une facture inexacte, parce que la donnée inscrite est fausse, rend l'erreur plus difficile à reprendre ; ses règles évoluent lentement, à la majorité des membres.

**Avis motivé** : ne pas adhérer au consortium en 2027. Le problème de VALMÉRIS n'est pas un manque de confiance entre acteurs qu'aucun tiers ne pourrait arbitrer : VALMÉRIS commande et paie ses missions, et peut être lui-même le tiers de confiance de ses échanges. Le problème est la qualité des données à la source. La plateforme centralisée y répond pour 450 k€ sur trois ans, pour tous les prestataires. VALMÉRIS peut rester observateur du consortium et réexaminer le projet après la bascule de PASSERELLE, à des conditions écrites :
- seules des empreintes des missions sont inscrites, les données personnelles restant hors du registre ;
- une charte de gouvernance fixe le vote, les barèmes propres à chaque assisteur, la sortie et le traitement des erreurs ;
- les heures inscrites sont géolocalisées ;
- les coûts sont partagés selon l'usage.

**Réponses tolérées**
- Adhésion conditionnelle au consortium, si les conditions (empreintes seulement, gouvernance, géolocalisation, intégration après PASSERELLE) sont posées et si le coût est comparé à celui de la plateforme.
- Coût sur trois ans qui ajoute aux deux solutions une part de temps interne, si l'hypothèse est écrite.
- Grille d'opportunité (plusieurs acteurs écrivent-ils ? se font-ils confiance ? faut-il une preuve inaltérable ? les données sont-elles partageables ?) appliquée au cas à la place de la liste des limites.
- Consensus décrit comme un vote entre membres ou comme une validation par autorité, sans nom d'algorithme.

**Erreurs fréquentes**
- *Blockchain confondue avec une base de données distribuée* (`ET-08`) — registre présenté comme une simple base partagée, ou inaltérabilité présentée comme absolue.
- *Opportunités sans limites* (`ET-19`) — confiance et fin des litiges reprises du consortium sans examiner l'oracle, les données personnelles et la gouvernance.
- *Cryptoactifs hors sujet* — jetons, règlement sur les marchés de cryptoactifs ou monnaie numérique invoqués, alors que le projet règle en euros, sans jeton.
- *Développement hors attente* (`JUR-T07`) — algorithme de hachage, code du contrat automatisé ou choix d'une technologie détaillés.
- *Avis sans comparaison* — recommandation qui ne confronte pas les 1 000 k€ du registre aux 450 k€ de la plateforme centralisée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO 22739:2024, vocabulaire des chaînes de blocs et des registres distribués (2e édition) | termes : registre distribué, bloc, nœud, consensus, contrat intelligent ; norme de vocabulaire, non d'exigences | `iso_22739_2024` / F11 § 3.4 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), applicable depuis le 25/05/2018 | minimisation et limitation de la conservation face à l'inaltérabilité du registre (annexe 2.6) | `rgpd` / F11 § 2.3 ; F15 | en vigueur |
| Registre distribué, typologie (publique, privée, de consortium), consensus, clés, oracle, grille d'opportunité, limites | fonctionnement et appréciation | F11 § 1 et 2 | notion de cours |

---

### 2.5 – Le coût du système d'information des dossiers et son pilotage (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI » (coût complet, inducteurs, imputation aux activités) ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ». Total de tête en sommes rondes ; aucun calcul actualisé, aucune répartition chiffrée exigée.

**Annexes mobilisées** : annexes 1.1 (520 000 dossiers et leur répartition, 22 M€ de dépenses du SI), 2.3 (part des arrivées au-delà de 60 minutes, heures géolocalisées) et 2.5 (coûts de 2026, dossiers par type, tableau de bord actuel).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Inducteur de coût défini ; 10 400 k€ / 520 000 dossiers = 20 € par dossier et par an | 0,5 |
| a-2 | Deux arguments tirés de l'annexe 2.5 qui montrent la limite du coût moyen unique (appels, missions, durée de suivi, appels sans dossier) | 0,5 |
| b-1 | Indicateur de coût complet, avec ses cinq champs et le risque surveillé | 0,5 |
| b-2 | Indicateur de qualité du service complet, avec ses cinq champs et le risque surveillé ; équilibre avec les appels reçus | 0,5 |

**Réponse attendue**

*2.5 a) – Le coût par dossier et ses limites*

**L'inducteur de coût** (0,5 pt avec le calcul) : un **inducteur** est une grandeur mesurable dont la variation explique celle du coût d'une ressource ou d'une activité, et qui sert à imputer ce coût aux produits ou aux services qui la consomment : nombre d'appels, de missions, de dossiers, durée de suivi (F09 § 2).

**Le calcul, de tête** : 2 400 + 3 200 + 700 + 1 100 + 400 + 2 600 = **10 400 k€** par an, soit près de la moitié des 22 M€ de dépenses du SI ; pour 520 000 dossiers : 10 400 000 € / 520 000 = **20 € par dossier et par an**.

**La limite d'un coût moyen unique** (0,5 pt), en deux arguments parmi :
- **la téléphonie, premier poste (3 200 k€, près d'un tiers du total), est facturée selon le nombre d'appels**, qui varie de 4 par dossier d'habitation à 9 par dossier d'aide aux personnes : un dossier d'aide aux personnes consomme plus de deux fois plus de téléphonie qu'un dossier d'habitation ;
- **l'application des prestataires est facturée selon le nombre de missions**, de 1 par dossier d'habitation à 1,5 par dossier automobile ;
- **la durée de suivi** va d'un jour pour un dossier automobile à quinze jours pour un dossier d'aide aux personnes, qui sollicite davantage le logiciel, le support et les chargés ;
- **environ 100 000 appels ne donnent lieu à aucun dossier** : leur coût est réparti sur les dossiers, alors qu'il relève de l'information des assurés ;
- la **part des autres coûts de la DSI** (2 600 k€) est une répartition, et non une consommation mesurée.

Le coût moyen de 20 € mélange donc des dossiers qui ne consomment pas les mêmes ressources. Il ne permet ni de connaître le coût d'une garantie proposée à un distributeur, ni de mesurer l'économie d'un dossier ouvert sans appel par une alerte de véhicule connecté. Il faut **imputer chaque poste par son inducteur** (appels, missions, dossiers et durée de suivi), selon la logique de la méthode à base d'activités, en principe. À titre d'illustration, non attendue : à 1 € par appel et 1 € par mission, le reste valant 12,5 € par dossier, on obtiendrait environ 20 € pour un dossier automobile, 17,5 € pour un dossier d'habitation et 23 € pour un dossier d'aide aux personnes, avant même de tenir compte de la durée de suivi.

*2.5 b) – Deux indicateurs pour le comité de direction*

Le tableau de bord actuel ne mesure que l'**activité** (appels reçus). Les deux indicateurs proposés y ajoutent le **coût** et la **qualité du service**, chacun associé à un **risque**, pour équilibrer le pilotage comme le demande M. MARVÉJOL (0,5 pt par indicateur complet) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Coût du système d'information des dossiers par dossier, par type de dossier** | coûts annuels du SI des dossiers répartis selon leurs inducteurs (appels pour la téléphonie, missions pour l'application, dossiers et durée de suivi pour le reste) / nombre de dossiers de chaque type | comptabilité analytique (direction administrative et financière), téléphonie en ligne (appels), logiciel des dossiers (dossiers, missions, durée de suivi) | trimestrielle, sur douze mois glissants | coût moyen au plus 20 € par dossier jusqu'à la bascule de PASSERELLE (niveau de 2026), écart entre types expliqué par les inducteurs | financier |
| **Part des arrivées au-delà de 60 minutes, mesurées par géolocalisation** | missions dont l'arrivée géolocalisée intervient plus de 60 minutes après l'ouverture du dossier / missions dont l'heure d'arrivée est géolocalisée × 100 | application des prestataires (heure géolocalisée) et logiciel des dossiers (heure d'ouverture, plateau, zone) | mensuelle, par plateau et par type de zone | au plus 15 % en 2029 (23 % en 2026 selon les relevés actuels), avec au moins 90 % d'heures géolocalisées | client |

**Les risques surveillés** : le premier suit la **dérive des coûts** du SI des dossiers, notamment de la téléphonie, et montre si les dossiers ouverts sans appel ou en ligne réduisent effectivement le coût. Le second mesure le **risque pour le bénéficiaire** : une attente longue, parfois de nuit au bord d'une route, est la première source de réclamations et menace la relation avec les distributeurs. Il repose sur une mesure fiable et commune aux plateaux, ce qui évite les biais relevés à la question 2.3. Il est lu par plateau et par type de zone, pour ne pas pénaliser Metz. Présentés à côté des appels reçus, avec leur tendance et leur cible, ils relient l'activité, le coût et le service rendu.

**Réponses tolérées**
- Coût moyen de 20 € retenu comme indicateur, si le candidat annonce sa décomposition par type.
- Autres arguments tirés de l'annexe 2.5 (part des autres coûts de la DSI imputée par convention, appels sans dossier), s'ils sont expliqués.
- À la place de l'indicateur de qualité du service : délai médian d'arrivée géolocalisé (médiane des durées entre l'ouverture du dossier et l'arrivée géolocalisée ; application et logiciel des dossiers ; mensuelle, par plateau et par zone ; baisse de 20 % entre 2026 et 2029 à définition constante ; axe client). Comme indicateur de risque supplémentaire : taux de dossiers ouverts sous réserve (dossiers ouverts pour un bénéficiaire introuvable / dossiers ouverts × 100 ; logiciel des dossiers ; mensuelle, par distributeur ; au plus 1 % fin 2028, 5 % en 2026 ; axe processus), ou part des missions refusées au moins une fois (missions refusées au moins une fois / missions × 100 ; table des propositions ; mensuelle, par plateau et par zone ; au plus 15 % fin 2028, 20 % en 2026 ; axe processus).

**Erreurs fréquentes**
- *Coût complet réduit à un poste* (`ET-33`) — seul le logiciel interne (2 400 k€) retenu, en oubliant la téléphonie, qui pèse davantage.
- *Calcul hors attente* (`JUR-T07`) — répartition détaillée par type ou calcul actualisé, alors que la question demande un coût par dossier de tête et des arguments.
- *Indicateur incomplet ou générique* (`ET-18`, `JUR-A02`) — « suivre la satisfaction » sans formule, source, fréquence, cible ni axe, ou indicateur de délai moyen calculé sur des heures déclaratives.
- *Indicateurs qui doublent le tableau actuel* — nombre d'appels par chargé ou taux de décroché, qui mesurent encore l'activité sans le coût ni le service rendu.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Contrôle de gestion du SI : coût complet, inducteurs, imputation aux activités (méthode à base d'activités en principe) | définition et calcul de tête | F09 § 2 et 3.1 | notion de cours |
| Indicateur à cinq champs, équilibre performance, risque et coût, axes du tableau de bord prospectif | deux indicateurs du comité de direction | F08 § 3 ; F09 § 4 | notion de cours |

---

## DOSSIER 3 – RENFORCER LA RÉSILIENCE OPÉRATIONNELLE NUMÉRIQUE ET FIABILISER LES DONNÉES DE DURABILITÉ (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 L'analyse d'impact de la panne du 14 janvier 2027 | `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers | 2,5 |
| 3.2 Le cadre de gestion du risque lié aux TIC | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.d` Dispositifs de surveillance et de résilience : IAM, PCA/PRA ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 5 |
| 3.3 L'audit de l'opérateur de téléphonie | `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD | 2 |
| 3.4 Les données de durabilité destinées au groupe | `4.3.b` Cadres réglementaires : CSRD, ESRS (collecte, traçabilité et fiabilité des données de durabilité) ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI | 3,5 |
| **Dossier 3 – Renforcer la résilience opérationnelle numérique et fiabiliser les données de durabilité** |  | **13** |

Répartition indicative : connaissances (typologie des risques, analyse d'impact sur l'activité, piliers de DORA et politique de sécurité fondée sur les risques, CSRD et double matérialité) environ 2 points (items 3.1 a-1, la définition de l'item 3.1 b-1, 3.2 a-1 et la moitié de l'item 3.4 a-1 et de l'item 3.4 a-2) ; analyse des annexes et recommandations environ 11 points, soit environ 85 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – L'analyse d'impact de la panne du 14 janvier 2027 (2,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ». Limite : la quantification des effets sur les états financiers (écritures, évaluations) relève de l'UE 4 ; l'UE 5 identifie les processus et les postes exposés.

**Annexes mobilisées** : annexe 3.1 (chronologie, conséquences, plan de continuité, réactions des partenaires) et annexe 1.1 (trois plateaux jour et nuit, téléphonie en ligne fournie par un opérateur, logiciel des dossiers, distributeurs).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée : cybermenaces (actes malveillants), défaillances opérationnelles (pannes, erreurs, changements mal maîtrisés, dépendance à un prestataire), risques réglementaires et métiers (non-conformité, pénalités, perte de clients, image) | 0,5 |
| a-2 | Quatre causes ou facteurs d'aggravation tirés de l'annexe 3.1, correctement classés, les trois catégories couvertes | 0,5 |
| b-1 | Analyse d'impact sur l'activité définie ; effets sur les processus (appels, ouverture des dossiers, missionnement) et sur la continuité du service aux bénéficiaires, appuyés sur les chiffres de l'annexe | 0,5 |
| b-2 | Effets sur la relation avec les partenaires et sur les états financiers en principe (charges supplémentaires, pénalités, chiffre d'affaires exposé), sans traitement comptable | 0,5 |
| b-3 | Deux enseignements pour le PCA, reliés aux défaillances relevées | 0,5 |

**Réponse attendue**

*3.1 a) – La typologie des risques et les causes de la panne*

Les risques liés aux systèmes d'information se répartissent en trois catégories (F12 § 0 et § 5) : les **cybermenaces**, actes malveillants contre la confidentialité, l'intégrité ou la disponibilité du SI (rançongiciel, saturation d'un service, compromission par un prestataire) ; les **défaillances opérationnelles**, non intentionnelles (panne, erreur humaine, changement mal maîtrisé, absence de redondance, dépendance à un fournisseur) ; les **risques réglementaires et métiers**, qui touchent la conformité et l'activité elle-même (manquement à un règlement, pénalités, perte d'un client, atteinte à l'image).

Classement attendu (quatre éléments au moins, trois catégories couvertes) :

| Cause ou facteur d'aggravation (annexe 3.1) | Catégorie | Commentaire |
|---|---|---|
| Mise à jour du logiciel de distribution des appels installée par CALVÉNIS à 19 h 50, sans préavis, sans retour rapide à la version précédente | défaillance opérationnelle (gestion des changements du prestataire) | cause directe |
| Centre de données unique de l'opérateur, aucun second opérateur ni renvoi automatique ; le logiciel des dossiers n'ouvre pas de dossier sans l'identifiant d'appel | défaillance opérationnelle (point unique de défaillance, dépendance entre composants) | la panne d'un prestataire arrête les trois plateaux et l'ouverture des dossiers |
| Détection à 20 h 35 par une superviseure, faute de surveillance de la téléphonie par VALMÉRIS ; directeur général informé à 22 h 30 ; aucune cellule de crise | défaillance opérationnelle (organisation) | facteur d'aggravation |
| Hypothèse d'une attaque par saturation : l'opérateur isole ses équipements pendant une heure | cybermenace (scénario redouté, écarté ici, mais plausible et aux effets identiques) | facteur d'aggravation : le diagnostic s'allonge ; une attaque aurait produit la même interruption |
| Incident inscrit comme « panne téléphonie, 4 h », sans classification ; PCA de 2019 qui ignore l'opérateur et n'a jamais été exercé, alors que DORA s'applique | risque réglementaire | les piliers « gestion du risque lié aux TIC », « incidents », « tests » et « prestataires tiers » ne sont pas tenus |
| Partenaires informés le lendemain à 10 h par un simple courriel ; l'assureur apprend la cause par la presse | risque métier | facteur d'aggravation : la confiance des partenaires est atteinte et l'accord du loueur est menacé |

*3.1 b) – L'analyse d'impact et les enseignements pour le PCA*

L'**analyse d'impact sur l'activité** (BIA) identifie les activités critiques, mesure les effets de leur interruption dans le temps (opérationnels, financiers, juridiques, d'image) et en déduit la durée maximale d'interruption et la perte de données admissibles ; elle fonde le plan de continuité (F12 § 4 ; ISO 22301:2019, annexe 3.5).

**Effets sur les processus** (b-1) : la **réception des appels** est interrompue sur les trois plateaux à la fois ; l'**ouverture des dossiers** passe au papier (1 200 dossiers) puis à une ressaisie de nuit, source d'erreurs (40 dossiers en double ou incomplets, qui affecteront le suivi, le règlement des prestataires et la facturation aux partenaires) ; le **missionnement des prestataires** prend du retard (600 dépannages sur 900 réalisés plus de trois heures après l'appel) ; le **traitement des réclamations** est submergé (700 en quinze jours, le double de l'ordinaire).

**Effets sur la continuité du service** (b-1) : le service « jour et nuit », cœur de la promesse d'« Assister 2030 », est interrompu au pire moment, un soir de neige où la demande est 2,7 fois plus forte (4 000 appels contre 1 500) ; 1 500 appelants ont raccroché sans laisser de message et ne pouvaient pas être rappelés ; des bénéficiaires immobilisés dans le froid sont exposés (150 ont dû être conduits en taxi ou logés). Le mode dégradé a été improvisé (« personne ne savait qui devait décider quoi »).

**Effets sur la relation avec les partenaires** (b-2) : les engagements de service des accords ne sont pas tenus (moins de 85 % d'appels décrochés) ; les partenaires ont été informés le lendemain à 10 h et l'un d'eux a appris la cause par la presse : la confiance est atteinte ; le loueur menace de réexaminer son accord, qui représente environ 12 M€, près de 4 % du chiffre d'affaires.

**Effets sur les états financiers, en principe** (b-2) : des **charges supplémentaires** (heures supplémentaires et de nuit, environ 50 k€ ; taxis et hôtels, environ 40 k€) ; des **pénalités** réclamées par deux partenaires (60 k€ et 40 k€), qui pèsent sur le résultat et peuvent ouvrir un différend si VALMÉRIS les conteste ; un **chiffre d'affaires futur exposé** si l'accord du loueur n'est pas renouvelé ; la question d'un recours contre l'opérateur. L'ordre de grandeur des coûts immédiats (environ 0,2 M€) est faible au regard des 310 M€ de chiffre d'affaires : l'enjeu principal est commercial et réglementaire. Le traitement comptable n'est pas attendu (UE 4).

**Deux enseignements pour le PCA** (b-3) :
1. **Partir d'une analyse d'impact par activité qui couvre les prestataires critiques et les dépendances.** Le PCA de 2019 prévoit l'incendie d'un plateau, qui serait relayé par les deux autres, mais pas la défaillance d'un prestataire qui les sert tous. Il doit recenser les services dont dépendent les activités critiques (opérateur de téléphonie, infogéreur, application des prestataires) et prévoir pour chacun une solution de repli : second opérateur ou renvoi automatique des appels, mode dégradé formalisé (ouverture d'un dossier sans identifiant d'appel, fiches normalisées, message d'attente qui oriente les urgences), objectif de reprise des appels en quelques dizaines de minutes.
2. **Organiser la détection, l'alerte et la crise, puis exercer le plan.** VALMÉRIS doit surveiller elle-même la disponibilité de la téléphonie, définir des critères de déclenchement, réunir une cellule de crise (directeur général, plateaux, DSI, risques et conformité, relations avec les partenaires), informer les partenaires et les bénéficiaires dans l'heure ; un PCA jamais exercé n'existe pas : exercice annuel sur le scénario « perte de l'opérateur un soir d'hiver ».

**Réponses tolérées**
- Autre répartition de la mise à jour sans préavis (risque lié au prestataire tiers classé en risque métier ou réglementaire), si elle est justifiée.
- Cybermenace illustrée par l'accès à distance du sous-traitant de supervision (annexe 3.3) plutôt que par l'hypothèse d'attaque, si elle est reliée à la panne.
- Mention, au titre des états financiers, des 1 200 dossiers ressaisis comme risque sur l'exhaustivité de la facturation aux partenaires et des règlements aux prestataires.
- Autres enseignements : relier le PCA aux engagements des accords avec les partenaires ; prévoir la communication de crise (presse, réseaux sociaux) ; exiger de l'opérateur l'information préalable de ses changements et son propre plan de continuité.

**Erreurs fréquentes**
- *Analyse d'impact réduite au coût de l'incident* (F10 § 7) — juste : les processus, la continuité, les partenaires et les postes exposés, l'enjeu commercial dominant le coût immédiat.
- *Cause présentée comme une cyberattaque* — juste : l'annexe établit une mise à jour défaillante ; la cybermenace est un scénario plausible, pas la cause.
- *Traitement comptable des pénalités développé* — hors du sujet : postes exposés seulement.
- *PCA et PRA confondus* (`ET-02`, `JUR-S02`) — juste : les enseignements portent sur le maintien de l'activité pendant la panne (PCA).
- *Annexe 3.1 survolée* (`JUR-T08`) — juste : chaque effet appuyé sur un chiffre ou une réaction.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques, analyse d'impact | cybermenaces, défaillances, risques réglementaires et métiers ; BIA | F12 § 0, § 4 et § 5 ; F10 § 4 | notion de cours |
| ISO 22301:2019 | analyse d'impact sur l'activité, plans, exercices | `iso_22301_2019` ; F12 § 4 | en vigueur |
| Règlement (UE) 2022/2554 (DORA) | cinq piliers, applicable depuis le 17/01/2025 | `dora` ; F12 § 7 | en vigueur |

---

### 3.2 – Le cadre de gestion du risque lié aux TIC (5 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM, PCA/PRA » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique n'est pas exigée ; les normes se mobilisent sans entrer dans la certification.

**Annexes mobilisées** : annexe 3.2 (constats, point de vue de la directrice des risques, 600 k€, conseil du 24 juin 2027), annexe 3.1 (panne), annexe 3.5 (DORA, ISO/IEC 27001:2022, ISO/IEC 27005:2022, EBIOS RM, ISO 22301:2019) et annexe 1.1 (organigramme, plateaux jour et nuit, infogéreur à deux centres de données).

**Barème indicatif (5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gestion du risque lié aux TIC située comme premier pilier, socle des quatre autres ; politique de sécurité fondée sur l'analyse des risques définie | 0,5 |
| a-2 | Démarche d'appréciation des risques appliquée au cas, avec la nature du référentiel retenu (méthode EBIOS RM ou lignes directrices ISO/IEC 27005, distinctes de la norme d'exigences ISO/IEC 27001) | 0,5 |
| a-3 | Contenu de la nouvelle politique (objectifs, périmètre, principes, organisation, règles, contrôle et revue), approuvée par le conseil | 0,5 |
| b-1 | Rôles du conseil d'administration, du directeur général et de la direction des risques et de la conformité (fonction indépendante) | 0,5 |
| b-2 | Rôles du RSSI, de la DSI et des prestataires ; les directions métiers, propriétaires des activités critiques, sont valorisées sans être exigées | 0,5 |
| b-3 | Positionnement du RSSI hors de la DSI, justifié par le conflit d'intérêts de l'annexe 3.2 | 0,5 |
| c-1 | Gestion des identités et des accès répondant aux comptes génériques et aux départs | 0,5 |
| c-2 | PCA et PRA distingués ; RTO et RPO définis et justifiés pour deux activités critiques | 0,5 |
| c-3 | Classification et remontée des incidents ; programme de tests de résilience, en principe | 0,5 |
| d | Quatre mesures hiérarchisées pour 2027, rang de la première justifié | 0,5 |

**Réponse attendue**

*3.2 a) – La démarche et la nouvelle politique de sécurité*

Le règlement DORA, d'application directe et applicable à VALMÉRIS depuis le 17/01/2025 (annexe 3.5), repose sur cinq piliers : la **gestion du risque lié aux TIC**, la gestion, la classification et la notification des incidents, les tests de résilience, la gestion des risques liés aux prestataires tiers et le partage d'informations (F12 § 7). Le premier pilier est le **socle** des autres : sans cadre qui identifie les activités critiques, les risques et les responsabilités, on ne sait ni classer un incident, ni choisir quoi tester, ni distinguer les prestataires critiques.

Une **politique de sécurité du système d'information** est le document approuvé par la direction qui fixe les objectifs de sécurité (confidentialité, intégrité, disponibilité, traçabilité), le périmètre, les principes, l'organisation et les règles, ainsi que le dispositif de contrôle (F12 § 1). Elle est **fondée sur l'analyse des risques** quand ses mesures découlent de risques identifiés, évalués et hiérarchisés, et qu'elle est revue quand ils changent : celle de 2018 ne l'est pas, et ignore la téléphonie en ligne, l'application des prestataires et les interfaces avec les constructeurs.

**L'appréciation des risques** (a-2), conduite avec la méthode **EBIOS Risk Manager** (méthode de l'ANSSI en cinq ateliers, compatible avec les lignes directrices ISO/IEC 27005:2022 ; ISO/IEC 27001:2022 est une norme d'exigences, et non une méthode) :
1. **cadrage et socle** : les activités critiques (réception des appels, ouverture et suivi des dossiers, missionnement des prestataires, règlement des prestataires), les biens qui les supportent (téléphonie, logiciel des dossiers, application mobile, interfaces, centres de données de l'infogéreur) et les écarts au socle de sécurité (comptes génériques, sauvegardes jamais restaurées) ;
2. **sources de risque** : erreurs et défaillances des prestataires, cybercriminels, personnes ayant quitté l'entreprise ;
3. **scénarios stratégiques** passant par l'écosystème : l'opérateur et son sous-traitant de supervision, l'infogéreur, les constructeurs ;
4. **scénarios opérationnels** : panne de l'opérateur un soir d'hiver, chiffrement du logiciel des dossiers, accès d'un ancien salarié par un compte resté actif ;
5. **traitement** : plan de traitement priorisé et risques résiduels acceptés par la direction générale, présentés au conseil.

**Le contenu de la nouvelle politique** (a-3) : objectifs hiérarchisés (la **disponibilité** jour et nuit d'abord, puis l'intégrité des dossiers, la confidentialité des données des bénéficiaires et la traçabilité) ; périmètre (tout le SI, services en ligne et prestataires compris) ; principes (comptes nominatifs et moindre privilège, sauvegardes éprouvées, objectifs de reprise par activité, exigences de sécurité et de continuité imposées aux prestataires, sécurité prise en compte dans chaque projet) ; organisation (b) ; règles déclinées en charte des utilisateurs et en procédures ; contrôle et revue annuelle. Elle s'appuie sur les mesures d'ISO/IEC 27001:2022 sans viser de certification, et elle est **approuvée par le conseil d'administration** le 24 juin 2027.

*3.2 b) – Les rôles et le positionnement du RSSI*

| Acteur | Rôle dans la gestion du risque lié aux TIC |
|---|---|
| Conseil d'administration (et son comité d'audit et des risques) | approuve le cadre de gestion du risque lié aux TIC, la politique et le niveau de risque accepté ; reçoit au moins deux fois par an un compte rendu (incidents graves, risques principaux, résultats des tests, prestataires critiques) ; vérifie les moyens ; ses membres sont formés |
| Directeur général (M. MARVÉJOL) | responsable de la mise en œuvre ; préside un comité trimestriel des risques liés aux TIC ; arbitre les priorités et les 600 k€ ; décide en cas de crise |
| Direction des risques et de la conformité (Mme KERDALOU) | **fonction de gestion des risques indépendante** : intègre les risques liés aux TIC à la cartographie de VALMÉRIS, fixe la méthode et les échelles, contrôle et remet en cause l'évaluation de la DSI, suit les incidents graves et la conformité à DORA, tient le registre des prestataires ; rend compte au directeur général et au conseil |
| RSSI (M. BRESTAVIN) | conçoit et pilote la politique, anime l'analyse des risques avec les métiers, veille, sensibilise, coordonne le traitement des incidents de sécurité, contrôle l'application des règles ; n'administre plus les serveurs ni les comptes |
| DSI (Mme FERVIGNAC) | met en œuvre et exploite : gestion technique des accès, sauvegardes et restaurations, PRA, suivi technique des prestataires ; rend compte au RSSI des écarts |
| Directions métiers (plateaux, réseau de prestataires) | propriétaires des activités critiques : fixent les durées d'interruption admissibles, valident le mode dégradé, demandent et revoient les droits de leurs équipes |
| Prestataires (CALVÉNIS, infogéreur, fournisseur de l'application mobile) | respectent les exigences contractuelles : rapports de disponibilité, information préalable des changements, signalement des incidents, participation aux tests, droits d'audit et d'accès, stratégie de sortie |
| Audit interne (Mme VENDROUX) | évalue de façon indépendante le dispositif (question 3.3) |

**Positionnement du RSSI** (b-3) : le rattacher au **directeur général**, ou à la direction des risques et de la conformité, et non plus à la DSI. Aujourd'hui, il administre les serveurs et les comptes qu'il devrait contrôler, avec un budget de la DSI : il est juge et partie, et ne peut ni alerter ni arbitrer contre sa hiérarchie. Il lui faut un accès direct au directeur général et au comité d'audit et des risques, et un budget identifié dans les 600 k€.

*3.2 c) – Les dispositifs de surveillance et de résilience*

1. **Gestion des identités et des accès** (c-1) : supprimer les 80 comptes génériques au profit de comptes **nominatifs**, y compris pour les intérimaires et les chargés en formation (comptes créés à l'arrivée, pour une durée limitée) ; relier les arrivées, mobilités et départs au fichier des ressources humaines, avec désactivation le jour du départ (45 comptes de partis encore actifs) ; demandes de droits par un circuit approuvé par le superviseur ; droits par rôle selon le moindre privilège ; **revue semestrielle** des droits par les responsables ; authentification multifacteur pour les accès à distance et les comptes à privilèges.
2. **PCA et PRA** (c-2) : le **PCA** maintient les activités critiques, en mode dégradé, pendant la crise ; le **PRA** rétablit le SI et ramène à la normale. Le **RTO** est la durée maximale d'interruption admissible ; le **RPO**, la perte de données maximale admissible (âge de la dernière donnée récupérable). L'objectif unique de 24 heures ne convient pas à des activités qui tournent jour et nuit :

| Activité critique | RTO proposé | RPO proposé | Justification (annexes 3.1 et 3.2) |
|---|---|---|---|
| Réception des appels et ouverture des dossiers | environ 30 minutes (bascule vers un second opérateur ou renvoi automatique, mode dégradé immédiat) | sans objet pour les appels ; quelques minutes pour les dossiers ouverts en mode dégradé | en quatre heures, 1 500 appels perdus et 600 dépannages tardifs ; un appel sans réponse laisse un bénéficiaire seul au bord de la route |
| Suivi des dossiers et missionnement (logiciel des dossiers) | 2 heures au plus | 15 minutes au plus (réplication vers le second centre de données de l'infogéreur) | environ 60 dossiers ouverts par heure, davantage les soirs d'hiver ; avec une sauvegarde nocturne, une panne en fin de journée ferait perdre près d'une journée de dossiers (environ 1 400) ; la restauration de 2023 a demandé 30 heures |

Le règlement des prestataires ou la paie peuvent supporter un RTO de quelques jours : le dispositif est proportionné à la criticité.
3. **Classification et remontée des incidents** (c-3) : un outil unique d'enregistrement remplace le tableur ; une **classification par gravité** sur des critères communs (activités critiques touchées, nombre de bénéficiaires et d'appels, durée, partenaires concernés, données atteintes, image, coût) ; un incident grave est **remonté** sans attendre au directeur général et à la direction des risques, déclenche la cellule de crise et l'information des partenaires, puis donne lieu à une analyse des causes et à un compte rendu au conseil ; la notification des incidents majeurs prévue par le deuxième pilier de DORA suit les modalités du règlement, sans qu'il soit demandé ici d'en citer les délais.
4. **Programme de tests de résilience** (c-3) : un programme annuel approuvé par le comité des risques liés aux TIC : exercice du PCA sur le scénario de l'annexe 3.1 et sur la perte d'un plateau ; essais de restauration du logiciel des dossiers chaque trimestre ; essai annuel de bascule entre les deux centres de données de l'infogéreur ; essai de bascule vers la solution de secours de la téléphonie ; participation des prestataires critiques ; retour d'expérience et suivi des actions ; résultats présentés au conseil.

*3.2 d) – Quatre mesures hiérarchisées pour 2027*

1. **Sécuriser la réception des appels avant l'hiver 2027-2028** : solution de secours de la téléphonie (second opérateur ou offre « deux sites » et renvoi automatique), surveillance de la disponibilité par VALMÉRIS, mode dégradé et cellule de crise, exercés avant décembre 2027. **Justification du premier rang** : c'est le risque qui s'est réalisé, dont la probabilité est établie (cinq interruptions en 2026, puis la panne de janvier) et dont l'impact est maximal (trois plateaux à la fois, sécurité des bénéficiaires, accord du loueur, image) ; l'hiver suivant fixe l'échéance.
2. **Faire approuver le cadre de gestion du risque lié aux TIC et la nouvelle politique** par le conseil du 24 juin 2027, avec le repositionnement du RSSI et le rôle de contrôle de la direction des risques.
3. **Fixer les RTO et RPO par activité et éprouver le PRA du logiciel des dossiers** (réplication, essais de restauration), avant l'hiver.
4. **Assainir les accès** : désactivation immédiate des 45 comptes de partis, suppression des comptes génériques et première revue des droits, mesure rapide et peu coûteuse.

La classification des incidents et le programme de tests accompagnent ces mesures au second semestre.

**Réponses tolérées**
- Appréciation des risques fondée sur ISO/IEC 27005:2022 (lignes directrices) plutôt que sur EBIOS RM, ou cadre du NIST CSF 2.0 (six fonctions, dont *Govern*) cité en appui, si la nature du référentiel est juste.
- RSSI rattaché à la direction des risques et de la conformité ; comité des risques liés aux TIC mensuel.
- Autres activités critiques pour les RTO et RPO (application des prestataires, interfaces avec les constructeurs), si les valeurs sont justifiées par les annexes ; valeurs voisines (RTO de 15 minutes à 1 heure pour les appels, de 1 à 4 heures pour les dossiers).
- Désactivation des comptes placée au premier rang, au titre d'une mesure immédiate et peu coûteuse, si la sécurisation des appels est engagée dans la foulée ; audit de l'opérateur intégré aux quatre mesures.

**Erreurs fréquentes**
- *PCA et PRA confondus ; RTO et RPO inversés ou fixés sans justification* (`ET-02`, `ET-03`, `JUR-S02`) — juste : maintien en mode dégradé contre retour à la normale ; durée d'interruption contre perte de données, par activité.
- *RSSI présenté comme un technicien ou laissé sous la DSI* (`ET-15`) — juste : pilote de la politique, indépendant de l'exploitation.
- *Norme, méthode et solution confondues* (`ET-01`, `JUR-S06`) — juste : EBIOS RM est une méthode, ISO/IEC 27005 des lignes directrices, ISO/IEC 27001 une norme d'exigences.
- *Politique de sécurité confondue avec la charte informatique* (`ET-27`) — juste : la charte décline les règles pour les utilisateurs.
- *DORA présenté comme une directive, ou délais de notification inventés* (F12 § 10) — juste : règlement d'application directe ; aucun délai n'est demandé.
- *Mesures techniques ou tests techniques de sécurité détaillés* (`JUR-T12`, limite du programme) — juste : dispositifs organisationnels et de résilience.
- *Gestion du risque confiée à la seule DSI* (`JUR-T11`) — juste : conseil, direction générale, fonction de gestion des risques, métiers et prestataires.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2022/2554 (DORA) | cinq piliers ; prestataires : registre, droits d'audit et d'accès, stratégie de sortie | `dora` ; F12 § 7 | applicable depuis le 17/01/2025 |
| ISO/IEC 27001:2022 | norme d'exigences, appréciation des risques, 93 mesures | `iso_27001_2022` ; F12 § 2 | en vigueur |
| ISO/IEC 27005:2022 | lignes directrices de gestion des risques | `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager, version 1.5 | méthode en cinq ateliers, écosystème | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| ISO 22301:2019 | continuité d'activité, exercices | `iso_22301_2019` ; F12 § 4 | en vigueur |
| NIST CSF 2.0 (toléré) | six fonctions dont *Govern* | `nist_csf_2_0` ; F12 § 2 | en vigueur |
| PSSI, IAM, PCA, PRA, RTO, RPO, rôles | définitions et positionnement du RSSI | F12 § 1, § 3 et § 4 | notion de cours |

---

### 3.3 – L'audit de l'opérateur de téléphonie (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la démarche de certification n'est pas au programme.

**Annexes mobilisées** : annexe 3.3 (fiche du prestataire, demande de l'auditrice interne), annexe 3.1 (panne), annexe 3.5 (DORA, COBIT 2019, ISO/IEC 27001:2022, ISO 22301:2019, RGPD) et annexe 1.1 (audit interne rattaché au directeur général, téléphonie en ligne, logiciel des dossiers).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Objectifs de l'audit et cadrage (exercice de la clause d'audit, périmètre, référentiels, calendrier) ; cartographie du service, de l'appel à l'ouverture du dossier, avec les acteurs | 0,5 |
| a-2 | Principaux risques à couvrir, tirés de l'annexe 3.3 | 0,5 |
| b-1 | Disponibilité et sécurité : contrôle à examiner et preuve à demander pour chacune | 0,5 |
| b-2 | Localisation et confidentialité des données, réversibilité : contrôle et preuve pour chacune | 0,5 |

**Réponse attendue**

*3.3 a) – La démarche, la cartographie et les risques*

L'audit de CALVÉNIS est un **audit d'un prestataire**, conduit par l'audit interne de VALMÉRIS en exerçant la **clause d'audit** du contrat (une fois par an, préavis de 30 jours), comme le prévoient en principe les exigences de DORA sur les prestataires tiers (droits d'audit et d'accès). Il se distingue de l'audit légal des comptes et d'un audit de certification (F10 § 1.1).

**Objectifs** (a-1) : apprécier si le service rendu respecte les engagements (disponibilité de 99,9 % par mois), si l'opérateur maîtrise ses risques (changements, continuité, sécurité, sous-traitance de la supervision, données des appelants) et si VALMÉRIS peut en sortir ; éclairer la décision du directeur général (maintien, renégociation, solution de secours, changement d'opérateur) et le conseil au titre de DORA.

**Cadrage** : lettre de mission validée par le comité d'audit et des risques ; périmètre : plateforme de distribution des appels, centre de données, supervision sous-traitée, gestion des changements, continuité, données ; référentiels : COBIT 2019 (gestion des fournisseurs, des services et de la continuité), ISO/IEC 27001:2022 (mesures de sécurité, dont les relations avec les fournisseurs), ISO 22301:2019 (continuité), RGPD (sous-traitance) ; équipe : l'auditrice interne et un auditeur spécialisé dans les SI ; calendrier : préavis de 30 jours, travaux au deuxième trimestre (25 jours), restitution contradictoire, rapport en septembre 2027, plan d'action et suivi (F10 § 1.2).

**Cartographie du service rendu** :

| Étape | Ce qui se passe | Acteur et composant |
|---|---|---|
| 1. Appel | le bénéficiaire compose le numéro d'assistance de son distributeur | bénéficiaire ; réseau de l'opérateur |
| 2. Distribution | la plateforme identifie le distributeur, la langue et la file, diffuse un message d'attente, ou renvoie vers la messagerie | CALVÉNIS ; centre de données unique |
| 3. Mise en relation | l'appel est présenté au poste d'un chargé disponible sur l'un des trois plateaux | CALVÉNIS ; postes des plateaux |
| 4. Ouverture du dossier | l'identifiant de l'appel est transmis au logiciel des dossiers, qui ouvre le dossier | interface ; logiciel des dossiers chez l'infogéreur ; DSI |
| 5. Enregistrement et statistiques | la conversation est enregistrée et conservée 90 jours ; les statistiques d'appels sont produites | CALVÉNIS |
| En continu | supervision à distance par le sous-traitant hors de l'Union ; mises à jour par CALVÉNIS | sous-traitant ; CALVÉNIS |

**Principaux risques à couvrir** (a-2) : l'indisponibilité du service (centre de données unique, mises à jour installées sans préavis, cinq interruptions inexpliquées en 2026 et la panne de quatre heures) ; une disponibilité qui n'est ni mesurée par VALMÉRIS ni rapportée par l'opérateur ; la rupture du lien avec le logiciel des dossiers ; l'accès non maîtrisé du sous-traitant de supervision aux enregistrements, depuis l'extérieur de l'Union, à l'insu de VALMÉRIS ; une assurance de sécurité limitée à l'hébergement par le périmètre du certificat (« le certificat suffit » : non) ; l'impossibilité de changer d'opérateur faute de restitution des paramétrages et des enregistrements.

*3.3 b) – Quatre critères, avec leurs contrôles et leurs preuves*

| Critère | Contrôle à examiner | Preuve à demander à l'opérateur |
|---|---|---|
| **Disponibilité** (performance) (b-1) | mesure de la disponibilité conforme à la définition contractuelle ; gestion des changements (préavis aux clients, essais, retour arrière rapide) ; redondance et plan de continuité de l'opérateur | rapports mensuels de disponibilité de 2026, journal des incidents (cinq interruptions et panne de janvier) avec leurs causes ; procédure de gestion des changements et dossier de la mise à jour du 14 janvier ; plan de continuité et compte rendu de son dernier exercice. Quatre heures d'arrêt contre environ 43 minutes admises par mois : l'engagement de janvier n'est pas tenu |
| **Sécurité** (b-1) | gestion des accès à la plateforme (comptes nominatifs, privilèges, accès à distance du sous-traitant autorisés et tracés) ; journalisation ; correctifs ; traitement des incidents de sécurité | certificat ISO/IEC 27001:2022 **avec son périmètre et sa déclaration d'applicabilité**, qui montrent ce qui n'est pas couvert (supervision, développement) ; liste des comptes à privilèges ; extrait des journaux d'accès du sous-traitant ; derniers rapports d'audit interne de l'opérateur |
| **Localisation et confidentialité des données** (conformité RGPD) (b-2) | lieux de stockage et d'accès des enregistrements et des statistiques ; autorisation écrite de VALMÉRIS pour le sous-traitant ultérieur et garanties du transfert hors de l'Union ; respect de la conservation de 90 jours ; chiffrement | liste des sous-traitants de CALVÉNIS et contrat avec le sous-traitant de supervision ; documents qui encadrent le transfert ; preuves de l'effacement des enregistrements de plus de 90 jours ; schéma des flux de données |
| **Réversibilité** (b-2) | capacité à restituer, dans un format exploitable, les paramétrages de distribution des appels, les enregistrements et les statistiques, et à assister la transition ; stratégie de sortie de VALMÉRIS (DORA) | description des formats d'export et essai d'extraction des paramétrages ; documentation des files et des règles de distribution ; engagement écrit d'assistance au transfert |

**Réponses tolérées**
- Démarche en cinq à sept étapes (cadrage, prise de connaissance, analyse des risques, programme de travail, collecte, restitution, suivi), si les étapes sont appliquées à CALVÉNIS.
- Cartographie présentée en schéma ; autres découpages du service, si l'interface avec le logiciel des dossiers et la supervision sous-traitée y figurent.
- Critère d'efficacité (délai de prise en charge des incidents par le service d'assistance de l'opérateur : 21 h 10 pour une panne commencée à 20 h) en complément, sans remplacer les quatre critères demandés.
- Visite du centre de données et entretiens comme preuves complémentaires.

**Erreurs fréquentes**
- *Méthodologie incomplète* (`JUR-A01`) — juste : objectifs, périmètre, référentiels, étapes, livrables et calendrier.
- *Audit du SI confondu avec l'audit légal ou avec un audit de certification* (`ET-34`) — juste : audit d'un prestataire, fondé sur la clause d'audit.
- *Certificat présenté comme une preuve suffisante* — juste : il faut en lire le périmètre ; il ne couvre ni la supervision ni le développement.
- *Tests techniques proposés comme diligences* (limite du programme 3.2) — juste : revue documentaire, entretiens, journaux, essais d'extraction.
- *Analyse juridique du contrat ou rédaction de clauses* (`JUR-T07`) — non attendue : l'audit apprécie le service et les risques.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Démarche d'audit du SI, audit d'un prestataire | cadrage, cartographie, risques, programme, restitution, suivi | F10 § 1.1 et § 1.2 | notion de cours |
| COBIT 2019 | gestion des fournisseurs, des services et de la continuité | `cobit_2019` ; F10 § 2 | en vigueur |
| ISO/IEC 27001:2022 | mesures de sécurité, relations avec les fournisseurs, déclaration d'applicabilité | `iso_27001_2022` ; F12 § 2 | en vigueur |
| ISO 22301:2019 | plan de continuité du prestataire | `iso_22301_2019` ; F12 § 4 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | sous-traitant, sous-traitance ultérieure autorisée, transferts encadrés | `rgpd` ; F15 § 5 et § 7 | applicable depuis le 25/05/2018 |
| Règlement (UE) 2022/2554 (DORA) | droits d'audit et d'accès, stratégie de sortie | `dora` ; F12 § 7 | applicable depuis le 17/01/2025 |

---

### 3.4 – Les données de durabilité destinées au groupe (3,5 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.b` « Cadres réglementaires : CSRD, ESRS » (exigences de collecte, de traçabilité et de fiabilité des données de durabilité ; rôle du SI et de la DSI ; champ donné par l'énoncé) ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI ». Limites : ni calcul d'assujettissement, ni codes des normes, ni démarche de vérification (UE 4).

**Annexes mobilisées** : annexe 3.4 (demande du groupe, constats de la direction administrative et financière, informations de 2026), annexe 3.5 (CSRD et ESRS, GHG Protocol) et annexe 1.1 (actionnaire, application mobile des prestataires, infogéreur, effectif).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | État de durabilité consolidé du groupe et place de VALMÉRIS (filiale incluse, qui fournit les informations) ; architecture des ESRS en principe ; vérification par un auditeur de durabilité et conséquence pour VALMÉRIS | 0,5 |
| a-2 | Double matérialité définie et illustrée par deux éléments de l'annexe 3.4, l'un d'impact, l'autre financier | 0,5 |
| b-1 | Sources et collecte automatisée (application des prestataires, données des loueurs et de l'infogéreur), reliées aux constats | 0,5 |
| b-2 | Référentiel des indicateurs ; contrôles et piste d'audit, reliés aux constats | 0,5 |
| b-3 | Gouvernance des données (propriétaires, validation, calendrier, rôle de la DSI), reliée aux constats | 0,5 |
| c-1 | Indicateur d'empreinte des interventions complet (formule, source, fréquence, cible, axe) | 0,5 |
| c-2 | Indicateur de l'impact environnemental du SI complet (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.4 a) – La demande du groupe dans le cadre de la CSRD et des ESRS*

La directive CSRD, modifiée en dernier lieu par la directive (UE) 2026/470, impose aux entreprises et aux groupes qui entrent dans son champ de publier un **état de durabilité**, établi selon les **ESRS** ; un groupe l'établit sur une base **consolidée**, en y intégrant ses filiales (annexe 3.5 ; fiche commune § 1 et § 5). Le groupe TERRANDÈLE y est soumis, ce qui n'est pas à déterminer, et publie depuis l'exercice 2024 un état consolidé qui **inclut VALMÉRIS** : VALMÉRIS ne publie pas son propre état, mais ses informations deviennent celles du groupe. Les ESRS comprennent des normes transversales (exigences générales et informations générales) et des normes thématiques environnementales, sociales et de gouvernance : les informations demandées relèvent du climat, du personnel et de la relation avec les bénéficiaires. L'état est **vérifié par un auditeur de durabilité**, qui peut demander comment chaque information a été obtenue : une donnée que VALMÉRIS ne sait pas reconstituer (le chiffre initial de 9 000 tCO2e) fragilise l'avis porté sur l'état du groupe, qui a déjà dû corriger deux fois son chiffre consolidé (a-1).

La **double matérialité** (a-2) retient une question quand elle est importante par ses **impacts** sur les personnes et l'environnement (matérialité d'impact), par ses **effets sur la situation financière** de l'entreprise (matérialité financière), ou par les deux. Illustrations tirées de l'annexe 3.4 :
- **impact** : les déplacements des prestataires pour environ 700 000 missions, environ 40 millions de kilomètres et 10 000 tCO2e en 2026 ; ce sont des émissions de la chaîne de valeur (scope 3 au sens du GHG Protocol), puisque les dépanneurs sont des entreprises indépendantes ;
- **financière** : les épisodes de neige, de tempête et d'inondation, plus fréquents, font croître les demandes d'assistance et leur coût ; et deux assureurs partenaires demandent l'empreinte des interventions dans leurs consultations : une donnée fiable devient une condition commerciale.

*3.4 b) – Le rôle du SI dans la collecte et la fiabilité des données*

La DSI est l'**architecte de la collecte** et la **garante de la qualité et de la traçabilité** des données de durabilité (F14 § 2) ; la direction administrative et financière en coordonne la production.

| Mesure | Contenu | Constat de l'annexe 3.4 auquel elle répond |
|---|---|---|
| 1. **Sources et collecte automatisée** (b-1) | calculer les kilomètres à partir des positions enregistrées par l'**application mobile des prestataires** (distance entre l'acceptation et l'arrivée, puis retour, ou distance parcourue déclarée), rattachés à la mission du logiciel des dossiers et au type de véhicule connu à l'agrément ; conserver la seule distance et le type de véhicule, et non les trajets détaillés (minimisation des données de localisation) ; obtenir des loueurs le type de motorisation par l'échange de fichiers existant, et de l'infogéreur un relevé trimestriel de la consommation des serveurs ; extraire automatiquement l'effectif et la formation du progiciel de paie et des ressources humaines | kilomètres estimés à partir des factures, forfait de 20 km pour les taxis et les artisans ; positions effacées au bout de 3 mois ; motorisation inconnue ; consommation des serveurs non fournie |
| 2. **Référentiel des indicateurs** (b-2) | un dictionnaire commun avec le groupe : pour chaque information, sa définition, son périmètre (missions de tous les prestataires, taxis compris), son unité, sa méthode et les facteurs d'émission du groupe, sa source, sa fréquence, son propriétaire et son validateur ; méthode constante d'une année à l'autre, changements documentés | cinq services aux méthodes propres ; taxis oubliés en 2025 ; le groupe exige méthode, sources et validateur |
| 3. **Contrôles et piste d'audit** (b-2) | contrôles automatisés à la collecte (exhaustivité : chaque mission a une distance ; unicité par numéro de mission ; vraisemblance des kilomètres par mission ; rapprochement avec les factures ; comparaison avec l'année précédente) ; **journalisation** de chaque correction (auteur, date, motif, valeur d'origine) ; conservation des données sources et des versions transmises, pour reconstituer chaque chiffre de la source à l'envoi | missions comptées deux fois ; tableurs écrasés ; aucune correction tracée ; chiffre initial de 2025 impossible à reconstituer |
| 4. **Gouvernance des données** (b-3) | un propriétaire par donnée (direction du réseau pour les kilomètres, plateaux pour les réclamations, ressources humaines pour la formation, services généraux pour l'électricité) ; une base commune alimentée par les applications, au lieu des tableurs envoyés par courriel ; validation formelle par le propriétaire puis par le directeur administratif et financier avant envoi (séparation entre la saisie et la validation) ; calendrier de clôture compatible avec le 31 mars ; revue annuelle avec la direction des risques et la DSI | cinq tableurs par courriel, un seul salarié pour les rassembler ; chiffre corrigé deux fois après l'envoi |

*3.4 c) – Deux indicateurs environnementaux*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| (c-1) **Émissions moyennes par mission d'intervention** | somme des émissions des déplacements des prestataires pour les missions du mois (kilomètres calculés à partir des positions enregistrées par l'application, selon la règle du référentiel pour le remorquage et le retour, × facteur d'émission du groupe selon le type de véhicule) / nombre de missions du mois, en kgCO2e par mission | application mobile des prestataires, logiciel des dossiers, référentiel des facteurs d'émission du groupe | mensuelle, consolidée chaque année pour l'état de durabilité | − 15 % en 2029 par rapport à 2027, première année calculée à partir des positions de l'application (environ 14 kgCO2e par mission selon l'estimation de 2026) | environnement |
| (c-2) **Consommation d'électricité des serveurs de VALMÉRIS par dossier ouvert** | kWh consommés par les serveurs de VALMÉRIS, déclarés par l'infogéreur / nombre de dossiers ouverts | relevé trimestriel de l'infogéreur, logiciel des dossiers | trimestrielle | mesurée dès 2027 ; − 10 % en 2029 par rapport à 2027, à périmètre comparable | environnement |

L'indicateur c-1 suit l'objectif d'« Assister 2030 » de réduire l'empreinte des interventions : il baisse quand le prestataire missionné est plus proche ou quand le réseau compte plus de véhicules électriques, et non quand l'activité recule. L'indicateur c-2 mesure l'impact environnemental du SI lui-même et répond au constat « électricité des serveurs : non connue » ; il exige que l'infogéreur fournisse ses relevés.

**Réponses tolérées**
- Vocabulaire de 2023 (« double importance », « incidences ») accepté ; illustration financière tirée de la panne de neige du 14 janvier ou du coût croissant des épisodes climatiques.
- Mention de la vérification par l'auditeur de durabilité comme exigence de traçabilité, sans plus.
- Autres sources automatisées pertinentes (enquêtes de satisfaction et réclamations extraites du logiciel des dossiers) ; plateforme de collecte de données de durabilité ou entrepôt de données proposés comme outils, si les contrôles et la gouvernance sont précisés.
- Autres indicateurs de l'impact du SI : consommation des postes et des équipements numériques des plateaux ; empreinte carbone du SI par scope (fabrication des équipements comprise) ; indicateur d'efficacité énergétique (PUE) du centre de données de l'infogéreur. L'électricité totale des plateaux par appel est tolérée, mais ne compte au titre du SI que si la part des équipements numériques est isolée.
- Pénalités et menace du loueur classées en risque métier (3.1 a), si elles sont présentées comme facteurs d'aggravation.
- Autres indicateurs complets : part des kilomètres d'intervention calculés à partir de l'application et non estimés (cible 90 % en 2028) ; part des jours de location de véhicules de remplacement électriques ou hybrides ; émissions totales des interventions rapportées au nombre de dossiers.

**Erreurs fréquentes**
- *CSRD réduite à un rapport annuel, ou rôle de la DSI confondu avec celui de l'auditeur de durabilité* (`ET-17`) — juste : des données fiables, traçables et vérifiables ; la DSI conçoit la collecte, l'auditeur vérifie.
- *Assujettissement calculé, normes citées par leurs codes ou démarche de vérification développée* (fiche commune § 5) — non attendus : le champ est donné, l'architecture suffit.
- *Empreinte des interventions oubliée au profit du seul numérique, ou empreinte réduite à l'électricité* (`ET-38`) — juste : les déplacements des prestataires, de la chaîne de valeur, dominent.
- *Calcul d'empreinte tenté* — non attendu : les émissions sont données.
- *Mesures sans lien avec les constats* (`JUR-T01`, `JUR-T08`) — juste : chaque mesure répond à un constat.
- *Indicateurs incomplets ou génériques* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe, reliés à « Assister 2030 ».

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Directive (UE) 2022/2464 (CSRD), modifiée par les directives (UE) 2025/794 et 2026/470 | état de durabilité consolidé, double matérialité, vérification | `csrd`, `csrd_omnibus` ; fiche commune § 1, § 3 et § 5 | en vigueur ; Omnibus I en vigueur depuis le 18/03/2026, non transposé en France |
| ESRS révisées (règlement délégué (UE) 2026/1563) | normes transversales et thématiques ; choix de version pour 2026 | `esrs_2026` ; fiche commune § 2 | applicables aux exercices ouverts à compter du 01/01/2027 |
| GHG Protocol | scopes 1, 2 et 3 ; chaîne de valeur | `ghg_protocol` ; F14 § 4 | en vigueur |
| Rôle de la DSI dans les données de durabilité, indicateurs | architecte de la collecte, qualité et traçabilité ; indicateurs complets | F14 § 2 et § 4 ; F10 § 3.2 (piste d'audit) | notion de cours |
