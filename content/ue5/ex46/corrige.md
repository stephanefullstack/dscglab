# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 46 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique (§ 1, SAM ; § 5, maturité et CMMI ; § 7, gabarit de réponse), F02 gouvernance et référentiels (§ 1, norme, référentiel et solution ; § 5, CMMI), F03 architecture, interopérabilité et service en ligne (§ 3 et § 5), F04 relations avec les ESN et contrats (§ 1, typologie ; § 4, clauses critiques ; § 6, risques de la relation), F05 projets et changement (§ 3, cahier des charges ; § 5, risques ; § 7, conduite du changement), F15 RGPD opérationnel (§ 5, sous-traitance), glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 L'alignement du système d'information sur « ORVANELLE 2030 » | `1.1.b` Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 3 |
| 1.2 La maturité de la gestion des projets du système d'information | `1.2.d` Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) | 2,5 |
| 1.3 Le parcours, de la candidature à la remise des accès | `1.3.f` Analyse des processus métiers et rôle des architectures SI dans leur rationalisation ; `1.3.e` Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers | 2,5 |
| 1.4 Les contrats du projet et les risques d'un progiciel en ligne | `1.4.b` Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle ; `1.4.d` Méthodologie de négociation contractuelle et analyse des risques | 3 |
| 1.5 Le cahier des charges et les risques du projet | `1.5.c` Élaboration d'un cahier des charges fonctionnel et technique ; `1.5.e` Identification et gestion des risques (maintenance, évolutivité, sécurité) ; `1.5.a` Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable | 3 |
| **Dossier 1 – Préparer la stratégie du système d'information et le projet de remplacement du logiciel de gestion locative** |  | **14** |

Répartition indicative : connaissances (modèle SAM, niveaux de CMMI, processus, types de contrats, structure du cahier des charges, démarche de gestion des risques) environ 3 points (items 1.1 a-1, 1.2 a-1, 1.3 a-1 pour moitié, 1.4 a-1, 1.5 a-1, 1.5 b-1 pour moitié) ; analyse des annexes et recommandations environ 11 points, soit environ 79 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – L'alignement du système d'information sur « ORVANELLE 2030 » (3 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.b` « Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 1.2 (témoignages du directeur commercial, d'une responsable de résidence, de la directrice des systèmes d'information et de la présidente), 1.1 (rattachement de la direction des systèmes d'information, système d'information, plan) et 1.6 (référence du modèle SAM).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Alignement défini (mise en cohérence permanente de la stratégie de l'entreprise et de la stratégie du SI) ; modèle SAM présenté : deux axes (ajustement stratégique entre choix externes et organisation interne ; intégration fonctionnelle entre domaine métier et domaine des technologies de l'information), quatre domaines, perspectives d'alignement | 0,5 |
| a-2 | Place de la direction des systèmes d'information : rattachée à la direction financière jusqu'en 2025, absente de la préparation du plan, cantonnée à l'exécution (70 % du temps sur l'existant) ; le domaine « stratégie des technologies de l'information » n'existe pas, l'intégration fonctionnelle est rompue au niveau stratégique | 0,5 |
| a-3 | Rôle du SI dans l'offre (il freine le parcours : la moitié des 18 000 abandons au formulaire papier, sept candidats sur dix venus de l'étranger perdus, ressaisies, attente à l'arrivée, alors que les concurrents signent en quelques minutes) et choix technologiques faits sans la direction des systèmes d'information (clé virtuelle) ; conclusion : au mieux une perspective d'exécution de la stratégie, subie et incomplète, donc un désalignement | 0,5 |
| a-4 | Perspective à adopter, justifiée : transformation technologique (le plan fixe la stratégie de l'entreprise ; il faut en déduire une stratégie des technologies de l'information, puis l'infrastructure, dont le progiciel), avec la direction des systèmes d'information associée ; ouverture vers le potentiel concurrentiel voulu par la présidente | 0,5 |
| b-1 | Deux orientations de la stratégie du SI, chacune justifiée par un objectif d'« ORVANELLE 2030 » et un constat de l'annexe 1.2 | 0,5 |
| b-2 | Troisième orientation, même exigence ; les trois orientations découlent du diagnostic du a) et ne se réduisent pas à des choix techniques | 0,5 |

**Réponse attendue**

*1.1 a) – Le modèle SAM et le diagnostic de l'alignement*

L'**alignement stratégique** est la mise en cohérence permanente de la stratégie de l'entreprise et de la stratégie du système d'information ; il est dynamique (il se refait à chaque changement de stratégie) et organisationnel autant que technique. Le **modèle d'alignement stratégique** (SAM) de Henderson et Venkatraman (1993) le décrit selon **deux axes** : l'**ajustement stratégique**, entre les choix externes (positionnement sur le marché) et l'organisation interne (structures, processus, compétences), et l'**intégration fonctionnelle**, entre le domaine métier et le domaine des technologies de l'information. Ils délimitent **quatre domaines** : stratégie de l'entreprise, stratégie des technologies de l'information, infrastructure et processus organisationnels, infrastructure et processus du SI. Une **perspective d'alignement** est un chemin qui part d'un domaine moteur et en entraîne deux autres : exécution de la stratégie (stratégie de l'entreprise → organisation → infrastructure du SI : le SI suit), transformation technologique (stratégie de l'entreprise → stratégie des technologies de l'information → infrastructure du SI), potentiel concurrentiel (stratégie des technologies de l'information → stratégie de l'entreprise → organisation : la technologie ouvre une offre nouvelle), niveau de service (stratégie des technologies de l'information → infrastructure du SI → organisation) (0,5 pt).

**Diagnostic de l'alignement actuel** (0,5 pt + 0,5 pt) :

| Dimension demandée | Constats de l'annexe 1.2 | Lecture selon le SAM |
|---|---|---|
| Place de la direction des systèmes d'information | rattachée à la direction financière jusqu'en 2025 ; « nous exécutons les demandes » ; 70 % du temps de seize personnes sur l'existant ; non associée à « ORVANELLE 2030 », découvert lors de sa présentation au personnel | le domaine **stratégie des technologies de l'information** n'existe pas : la direction des systèmes d'information n'intervient qu'au niveau de l'infrastructure ; l'**intégration fonctionnelle** est rompue au niveau stratégique (le plan a été construit sans elle) |
| Rôle du SI dans l'offre faite aux étudiants | 30 000 candidatures commencées, 12 000 abouties ; la moitié des 18 000 abandons à l'étape du formulaire papier du garant ; sept candidats sur dix venus de l'étranger abandonnent ; ressaisies par les chargés d'accueil ; état des lieux sur papier ; une heure d'attente à l'arrivée ; concurrents qui signent « en quelques minutes » | le SI ne sert pas le positionnement externe : il **freine** l'offre au lieu de la porter ; l'**ajustement stratégique** fait défaut entre l'ambition (parcours en ligne, international) et les processus et outils internes |
| Choix technologiques faits sans elle | clé virtuelle choisie en 2023 par les services techniques ; contrat signé avant que la direction des systèmes d'information soit informée ; raccordement à l'application des résidents dans l'urgence | des éléments d'**infrastructure** sont choisis hors de toute stratégie des technologies de l'information ; ils deviennent des contraintes (interfaces, sécurité) au lieu d'être des choix cohérents |

**Conclusion** : l'alignement actuel relève, au mieux, d'une **perspective d'exécution de la stratégie** subie et incomplète : le SI suit avec retard des décisions prises ailleurs, sans stratégie des technologies de l'information ni participation de la direction des systèmes d'information. Le SI n'est pas aligné sur « ORVANELLE 2030 » : il contredit l'objectif d'un parcours entièrement en ligne et pèse sur l'occupation.

**Perspective à adopter : la transformation technologique** (0,5 pt). Le plan fixe la stratégie de l'entreprise (parcours en ligne, 12 000 logements, 95 % d'occupation, sécurité) ; il faut en déduire explicitement une **stratégie des technologies de l'information** (quel parcours, quel socle, quelles interfaces, quelles compétences), puis l'**infrastructure** : le progiciel de gestion locative en ligne n'en est qu'une traduction. Cette perspective suppose que la direction des systèmes d'information participe aux décisions numériques, comme le veut la présidente (« je ne veux plus qu'un projet numérique soit décidé sans la direction des systèmes d'information »). Elle prépare la **perspective de potentiel concurrentiel** que vise Mme TRÉVARDIN : une fois le socle en place, la technologie (signature en quelques minutes, accès sur téléphone) peut devenir un argument commercial et ouvrir des offres nouvelles (réservation depuis l'étranger, séjours courts).

*1.1 b) – Trois orientations de la stratégie du système d'information*

La **stratégie du SI** fixe, pour plusieurs années, les orientations du système d'information déduites de la stratégie de l'entreprise ; elle guide les choix d'applications, de données, d'organisation, de compétences et de partenaires. Trois orientations, chacune justifiée par un objectif du plan (0,5 pt pour deux orientations, 0,5 pt pour la troisième ; trois parmi les suivantes) :

| Orientation | Constat de l'annexe 1.2 | Objectif d'« ORVANELLE 2030 » servi |
|---|---|---|
| **Faire du parcours en ligne, de la candidature à la remise des accès, le cœur de l'offre** : dépôt des pièces et engagement du garant en ligne, signature et paiement dans le même parcours, accès remis sans ressaisie ni papier, parcours pensé pour les étudiants qui réservent depuis l'étranger | la moitié des abandons au formulaire papier ; sept candidats sur dix venus de l'étranger perdus ; concurrents en quelques minutes | parcours entièrement en ligne ; occupation d'au moins 95 % (moins de candidatures perdues) |
| **Construire un socle de gestion locative standard, partagé et reproductible**, qui permette d'ouvrir une résidence par paramétrage et non par un projet informatique, et de tenir le pic de la rentrée | logiciel de 2009 à client lourd, non maintenu après 2028 ; parc porté de 9 000 à 12 000 logements | 12 000 logements dans vingt villes en 2030 |
| **Faire de la direction des systèmes d'information un partenaire des directions** : associée à toute décision numérique (clé, portail, progiciel), libérée d'une partie de l'existant, dotée de compétences de pilotage de projets et de prestataires | « nous exécutons les demandes » ; non associée au plan ; clé virtuelle choisie sans elle | tous les objectifs, qui passent par le SI ; en particulier la sécurité des résidents et de leurs données |
| **Intégrer la sécurité des résidents et de leurs données dès la conception** des choix numériques : accès aux logements, données des candidats confiées à un service en ligne, interfaces | clé virtuelle raccordée dans l'urgence ; pièces justificatives envoyées par courriel (annexe 1.4) | sécurité des résidents et de leurs données |
| **Disposer en temps réel de l'occupation de chaque résidence** pour décider vite (relances, offres d'été) | demande de la présidente (annexe 1.5 D) | occupation d'au moins 95 % |

**Réponses tolérées**
- Perspective de **potentiel concurrentiel** retenue comme perspective principale, si elle est justifiée par la volonté de la présidente de faire du SI un atout commercial et si le candidat montre que la stratégie des technologies de l'information doit alors exister et être portée par une direction associée au directoire.
- Diagnostic présenté par les quatre domaines du SAM (un constat par domaine), ou schéma du modèle annoté, s'il est appliqué aux annexes.
- Référence complémentaire à la chaîne de valeur ou au tableau de bord équilibré de l'informatique : valorisée sans être exigée ; elle ne remplace pas le SAM demandé.
- Orientation sur le pilotage de l'énergie des résidences par le SI, si elle est justifiée par l'objectif de réduction de 20 % ; elle n'est pas attendue ici.
- Autres orientations, si elles sont justifiées par un objectif du plan et un constat de l'annexe.

**Erreurs fréquentes**
- *Alignement réduit au remplacement du logiciel* (ET-06, `JUR-G02` alignement réduit à un choix technique ou à une standardisation logicielle) — « acheter un progiciel en ligne » n'aligne pas le SI tant que la stratégie des technologies de l'information n'existe pas et que la direction des systèmes d'information reste exécutante.
- *SAM récité sans être appliqué* (`JUR-T01` contextualiser chaque notion, pas de morceau de cours ; `JUR-G03` avis motivé fondé sur la théorie) — les axes et les domaines n'apportent des points que s'ils servent à lire les témoignages.
- *Perspective nommée sans justification* (`JUR-T03` analyser et argumenter) — la perspective se déduit de ce qui est moteur : ici le plan, déjà adopté.
- *SAM mal attribué ou daté de 1999* (F99 § 2.2) — l'article fondateur est de 1993 ; 1999 est une réimpression.
- *Perspective d'exécution de la stratégie reconduite comme perspective à adopter* (`JUR-T03` analyser et argumenter) — c'est la situation actuelle, où le SI suit sans stratégie des technologies de l'information ; elle n'est admise que si le candidat y ajoute explicitement une stratégie des technologies de l'information portée par une direction des systèmes d'information associée aux décisions.
- *Schéma directeur ou feuille de route construits* (`JUR-T07` répondre à la seule question posée) — non demandés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Henderson et Venkatraman, 1993 (modèle SAM) | deux axes, quatre domaines, perspectives d'alignement | `henderson_venkatraman_1993` ; F01 § 1 | publié |
| Stratégie du SI et alignement | orientations déduites de la stratégie ; pas une adéquation technique | F01 § 1 et § 7 ; `erreurs_types.md` ET-06 | notion de cours |

---

### 1.2 – La maturité de la gestion des projets du système d'information (2,5 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.d` « Méthodologies d'évaluation de la maturité numérique (CMMI, COBIT, etc.) ».

**Annexes mobilisées** : annexes 1.3 (trois projets et pratiques), 1.6 (référence de CMMI et nom des niveaux), 1.5 E (calendrier du projet) et 1.1 (effectif de la direction des systèmes d'information).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Maturité définie (capacité d'une organisation à conduire ses processus de façon maîtrisée et prévisible) ; CMMI présenté comme un référentiel, non comme une norme ; cinq niveaux décrits chacun en une phrase | 0,5 |
| a-2 | Niveau 1 « initial » retenu et justifié : les résultats dépendent des personnes et non d'un processus ; ils sont imprévisibles | 0,5 |
| a-3 | Trois constats de l'annexe 1.3 reliés au niveau (portail sans cahier des charges ni recette par ORVANELLE ; clé virtuelle réussie grâce à une personne puis en retard après son départ ; raccordement du progiciel de gestion intégré arrêté sans décision ; ni méthode, ni revue, ni indicateur) | 0,5 |
| b-1 | Niveau 2 « géré » fixé pour le projet avant son lancement, justifié (planification, suivi, exigences et fournisseurs maîtrisés au niveau du projet ; le niveau 3 suppose un processus commun à toute l'organisation, hors de portée en quelques mois, et devient l'horizon des projets de la croissance) | 0,5 |
| b-2 | Trois actions pour atteindre le niveau 2, chacune reliée à un constat (chef de projet et instances, méthode minimale écrite, indicateurs mensuels, revue de fin de projet, recette par ORVANELLE) | 0,5 |

**Réponse attendue**

*1.2 a) – Les niveaux de CMMI et la situation d'ORVANELLE*

La **maturité** d'une organisation, pour un ensemble de processus, est sa capacité à les conduire de façon maîtrisée, reproductible et prévisible. **CMMI** (*Capability Maturity Model Integration*, CMMI Institute, version 3.0 de 2023) est un **référentiel** de bonnes pratiques, et non une norme : il décrit **cinq niveaux de maturité** (0,5 pt) :

| Niveau | Ce qui le caractérise |
|---|---|
| 1 – Initial | les processus sont improvisés ; les résultats dépendent de l'engagement de quelques personnes ; délais et coûts sont imprévisibles |
| 2 – Géré | chaque projet est planifié, suivi et maîtrisé : exigences écrites, plan, suivi de l'avancement, gestion des fournisseurs, revue des écarts |
| 3 – Défini | un processus commun, écrit et adapté à chaque projet, s'applique à toute l'organisation ; les enseignements sont capitalisés |
| 4 – Quantitativement géré | les processus sont pilotés par des mesures et des objectifs chiffrés de performance |
| 5 – En optimisation | les processus s'améliorent en continu à partir de ces mesures et de l'innovation |

**Situation d'ORVANELLE : niveau 1, initial** (0,5 pt), justifié par trois constats (0,5 pt ; trois parmi les suivants) :
- **Les résultats dépendent d'une personne, non d'un processus** : la clé virtuelle a été déployée dans les délais (deux mois par résidence) tant qu'un chef de projet expérimenté l'a conduite ; après son départ, en juin 2025, chaque résidence a demandé quatre mois et 8 des 30 résidences prévues sont reportées à 2027. Sa méthode (planning, point hebdomadaire, liste de contrôle) n'a été ni écrite ni reprise : c'est la marque du niveau 1, où la réussite ne se reproduit pas.
- **Les exigences et les fournisseurs ne sont pas maîtrisés** : le portail de 2018 a été commandé sans cahier des charges écrit, recetté par l'agence web elle-même ; il a été livré avec huit mois de retard, pour un coût supérieur de moitié au prix convenu, avec 200 anomalies les trois premiers mois.
- **Les projets ne sont ni décidés ni arrêtés formellement** : le raccordement du progiciel de gestion intégré a été arrêté en 2023 après un an de travaux, sans décision ni responsable désigné.
- **Ni méthode commune, ni revue de fin de projet, ni indicateur** : chaque direction pilote « avec ses propres tableaux » ; les dépassements ne sont connus qu'à la clôture des comptes ; aucun chef de projet à temps plein.

ORVANELLE n'atteint donc même pas le niveau 2, puisqu'aucun projet n'est planifié et suivi de façon reproductible.

*1.2 b) – Le niveau à atteindre et les actions*

**Niveau visé avant le lancement : niveau 2, géré, pour le projet de remplacement** (0,5 pt). C'est le niveau qui garantit que **ce** projet sera planifié, suivi et maîtrisé, et le calendrier ne laisse pas davantage : signature des contrats en juin 2027, mise en service en mai 2028, ancien logiciel non maintenu après décembre 2028. Viser le niveau 3 tout de suite serait irréaliste : il suppose une méthode commune, éprouvée sur plusieurs projets, et une organisation qui la fait vivre. Le niveau 3 devient l'**horizon d'ici 2029-2030**, quand ORVANELLE ouvrira des résidences dans cinq villes de plus et conduira plusieurs projets à la fois ; les niveaux 4 et 5 ne sont pas un objectif pour une direction des systèmes d'information de seize personnes.

**Trois actions** (0,5 pt ; trois parmi les suivantes, chacune reliée à un constat) :
1. **Désigner un chef de projet expérimenté à temps plein, un sponsor et un comité de pilotage** : le sponsor est le (la) membre du directoire chargé(e) des opérations ; le comité de pilotage mensuel réunit les directions concernées et la direction des systèmes d'information et prend les décisions formelles (périmètre, arbitrages, arrêt éventuel) ; le chef de projet est recruté ou détaché avant la signature des contrats (réponse au départ du chef de projet de la clé virtuelle et à l'arrêt du raccordement de 2022 sans décision).
2. **Écrire une méthode minimale, appliquée dès le cadrage** : note de cadrage, cahier des charges écrit et validé par les directions (question 1.5), planning à jalons, registre des risques, recette faite par ORVANELLE avec des utilisateurs clés et non par le prestataire (réponse au portail de 2018).
3. **Suivre le projet chaque mois par des indicateurs** présentés au comité de pilotage, pour connaître les écarts quand on peut encore agir et non à la clôture des comptes :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de jalons tenus | jalons franchis à la date prévue / jalons prévus à cette date × 100 | planning du projet tenu par le chef de projet | mensuelle, au comité de pilotage | au moins 90 % | processus |
| Écart de coût du projet à date | (coûts engagés à date − coûts prévus à date) / coûts prévus à date × 100 | suivi des engagements du projet (commandes à l'éditeur et à l'intégrateur, temps des équipes internes) | mensuelle, au comité de pilotage | au plus 5 % | financier |

4. **Conduire dès maintenant la revue de fin de projet de la clé virtuelle** et écrire ses enseignements (planning par résidence, point hebdomadaire, liste de contrôle), puis prévoir une revue à chaque jalon du nouveau projet : c'est le premier pas vers le niveau 3.

**Réponses tolérées**
- Échelle de capacité des processus de COBIT 2019 (0 à 5) ou grille à quatre niveaux, si les niveaux sont différenciés et si la situation est justifiée par les constats.
- Situation « entre le niveau 1 et le niveau 2 », si le candidat montre que la clé virtuelle a approché le niveau 2 pendant un temps, sans que cette pratique devienne celle de l'organisation.
- Niveau 3 fixé comme cible à l'horizon du plan, à condition que le niveau 2 soit exigé avant le lancement du projet.
- Création d'un bureau des projets (PMO) à la direction des systèmes d'information, recours à une assistance à maîtrise d'ouvrage : valorisés.
- Autres indicateurs de suivi complets (formule, source, fréquence, cible, axe).

**Erreurs fréquentes**
- *CMMI présenté comme une norme ou une certification obligatoire* (ET-01, `JUR-S06` confondre référentiels, normes et solutions) — c'est un référentiel ; l'évaluation par le CMMI Institute est facultative.
- *Niveau 2 retenu au vu du succès de la clé virtuelle* (`JUR-T03` analyser et argumenter) — ce succès tenait à une personne et ne s'est pas reproduit : c'est le contraire d'un processus géré.
- *Niveau cible 4 ou 5, ou niveau 3 exigé avant le lancement* (`JUR-T03`) — irréaliste au regard du calendrier et de la taille de la direction des systèmes d'information.
- *Grille de maturité numérique de l'entreprise construite* (`JUR-T07` répondre à la seule question posée) — la question porte sur la seule gestion des projets du SI.
- *Actions sans lien avec les constats* (`JUR-P03` diagnostiquer les erreurs de gestion de projet par étapes) — chaque action répond à une défaillance de l'annexe 1.3.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| CMMI V3.0 (CMMI Institute, ISACA, 2023) | cinq niveaux de maturité | `cmmi_v3` ; F01 § 5 ; F02 § 5 | en vigueur |
| COBIT 2019 (ISACA) | niveaux de capacité de 0 à 5 (réponse tolérée) | `cobit_2019` ; F02 § 3 | en vigueur |
| Norme, référentiel et solution | CMMI est un référentiel | F02 § 1 ; `erreurs_types.md` ET-01 | notion de cours |

---

### 1.3 – Le parcours, de la candidature à la remise des accès (2,5 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des SI : `1.3.f` « Analyse des processus métiers et rôle des architectures SI dans leur rationalisation » ; `1.3.e` « Impacts organisationnels, juridiques et comptables des nouvelles architectures sur la transformation des métiers ». Limite : « Ne pas réduire l'urbanisation à une vision strictement technique : elle s'inscrit dans une stratégie globale. » Seuls les impacts organisationnels sont demandés ici.

**Annexes mobilisées** : annexes 1.4 (parcours actuel, délais, erreurs), 1.5 A et D (fonctions standard du progiciel, interfaces, besoins), 1.2 (témoignage de la responsable de résidence) et 1.1 (effectif des résidences et du centre de relation résidents, système d'information).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Processus défini (enchaînement d'activités conduites par plusieurs acteurs, qui transforme une demande en résultat pour un client) ; quatre ruptures du processus actuel relevées, chacune avec son effet tiré de l'annexe 1.4 (pièces par courriel, échange de nuit et ressaisie, bail recopié, paiements rapprochés à la main, état des lieux sur papier et accès activé à la main) | 0,5 |
| a-2 | Processus cible représenté par acteur, de façon lisible (tableau ou schéma), avec les applications et les interfaces | 0,5 |
| a-3 | Processus cible cohérent avec le progiciel et ses cinq interfaces : saisie unique à la source, contrôle automatique et traitement des seules exceptions, attribution en temps réel, bail produit et signé dans le parcours, paiement rapproché automatiquement, état des lieux sur tablette, accès activé sans passage à l'accueil | 0,5 |
| b-1 | Effets sur le rôle et les compétences des chargés d'accueil (de la saisie à l'accueil et au traitement des exceptions ; usage du progiciel et de la tablette, accompagnement des résidents, qualité de la donnée) et conditions (formation, accompagnement du changement) | 0,5 |
| b-2 | Effets sur l'organisation de la rentrée (arrivées étalées, accueil recentré, centre de relation résidents tourné vers l'assistance, appui renforcé à la première rentrée sur le nouveau progiciel) | 0,5 |

**Réponse attendue**

*1.3 a) – Les ruptures du processus actuel et le processus cible*

Un **processus** est un enchaînement d'activités, conduites par plusieurs acteurs et soutenues par des applications, qui transforme une demande (ici, une candidature) en un résultat pour un client (un résident logé, avec son bail et ses accès). L'architecture du SI le **rationalise** quand chaque donnée est saisie une seule fois, à la source, et circule ensuite d'une application à l'autre en temps réel (0,5 pt avec les quatre ruptures).

**Aide au correcteur : le processus actuel, par acteur** (non demandé au candidat, qui le trouve décrit dans l'annexe 1.4) :

| Étape | Candidat et garant | Portail | Centre de relation résidents | Chargé d'accueil et responsable de résidence | Logiciel de gestion locative | Prestataires de signature et de paiement |
|---|---|---|---|---|---|---|
| 1. Candidature | remplit la candidature ; imprime le formulaire du garant, le fait signer, envoie pièces et formulaire par courriel | enregistre la candidature | — | — | — | — |
| 2. Contrôle | complète après relance | dossier marqué « complet » | reçoit jusqu'à 2 000 courriels par jour en juillet, contrôle à la main, relance (un dossier sur deux incomplet) ; six jours | — | — | — |
| 3. Attribution | — | envoie l'identité des candidats la nuit ; affiche encore le logement comme libre | — | le lendemain, ressaisit la candidature et attribue ; le responsable valide | reçoit le fichier de la nuit | — |
| 4. Bail | signe en ligne | — | — | prépare le bail dans un traitement de texte en recopiant les données, le dépose chez le prestataire ; trois jours, puis deux jours de signature | source des données recopiées | signature électronique |
| 5. Dépôt de garantie | paie en ligne | — | envoie le lien de paiement | rapproche à la main, une fois par semaine | enregistre le rapprochement | liste quotidienne des paiements |
| 6. Arrivée | attend dans le hall | — | — | état des lieux sur papier (trente minutes), active la clé ou remet un badge ; saisit l'état des lieux jusqu'à trois semaines après | reçoit l'état des lieux après coup | — |

Délai entre la candidature commencée et le bail signé : douze jours.

**Quatre ruptures** (quatre parmi les suivantes ; notées avec la définition, item a-1) :

| Rupture | Nature | Effet (annexes 1.4 et 1.2) |
|---|---|---|
| Pièces et formulaire du garant envoyés par courriel, contrôlés à la main | rupture de support (papier, courriel) et délai | six jours pour un dossier complet ; un dossier sur deux incomplet ; jusqu'à 2 000 courriels par jour ; la moitié des 18 000 abandons à cette étape |
| Échange de fichiers chaque nuit, puis ressaisie de la candidature | ressaisie et délai d'un jour ; deux applications non synchronisées | 150 logements promis à deux candidats à l'été 2026 ; la moitié du temps des chargés d'accueil en septembre |
| Bail préparé dans un traitement de texte en recopiant les données | ressaisie et risque d'erreur | un bail sur vingt corrigé et signé de nouveau ; trois jours entre l'attribution et l'envoi |
| Paiements rapprochés à la main, une fois par semaine | rupture entre deux systèmes et risque d'erreur | 300 paiements non rapprochés fin septembre 2026 ; risque de remettre les accès sans dépôt payé, ou de relancer à tort |
| État des lieux sur papier, saisi après coup ; clé activée ou badge remis à l'accueil | ressaisie, délai, goulot à l'arrivée | jusqu'à trois semaines de retard dans le logiciel ; une heure d'attente (jusqu'à 40 arrivées le premier samedi de septembre dans une résidence de 250 logements) |

**Le processus cible permis par le progiciel et ses interfaces, par acteur** (0,5 pt pour la représentation, 0,5 pt pour la cohérence avec le progiciel et ses interfaces) :

| Étape | Ce qui change | Acteurs et applications |
|---|---|---|
| 1. Candidature et pièces | le candidat dépose ses pièces en ligne ; le garant s'engage en ligne, sans impression | candidat et garant ; portail relié au progiciel ; prestataire de signature |
| 2. Contrôle | le progiciel contrôle la complétude à la réception et relance automatiquement ; le centre de relation résidents ne traite que les exceptions (pièce illisible, doute, cas particulier) | progiciel ; centre de relation résidents |
| 3. Attribution | attribution en temps réel selon des règles paramétrées ; le logement est retiré du portail dès qu'il est attribué ; le responsable de résidence ne valide que les cas hors règles | progiciel, interface avec le portail |
| 4. Bail | bail produit automatiquement à partir du modèle et des données de la candidature, envoyé par l'interface au prestataire de signature, signé en quelques minutes | progiciel, interface de signature |
| 5. Dépôt de garantie | paiement dans le même parcours ; le paiement revient par l'interface et se rapproche automatiquement du bail | progiciel, interface de paiement |
| 6. Arrivée et accès | le résident choisit son créneau d'arrivée ; l'état des lieux est fait sur tablette, avec photos, et enregistré aussitôt ; la clé virtuelle est activée par l'interface quand le bail est signé, le dépôt payé et l'état des lieux fait (22 résidences) ; le badge est préparé à l'avance ailleurs | chargé d'accueil ; progiciel ; interface avec la clé virtuelle ; application des résidents |
| 7. Suite | quittancement et transmission au progiciel de gestion intégré par l'interface, sans fichier mensuel | progiciel, interface avec le progiciel de gestion intégré |

Le bail peut être signé le jour même de la candidature, au lieu de douze jours ; chaque donnée n'est saisie qu'une fois.

*1.3 b) – Les effets sur les métiers des résidences*

**Le rôle et les compétences des chargés d'accueil** (0,5 pt) :
- *Rôle* : ils passent de la saisie (candidatures ressaisies, baux recopiés, paiements rapprochés, états des lieux saisis après coup) à l'**accueil**, à l'**accompagnement** des résidents, notamment de ceux qui arrivent de l'étranger, au **traitement des exceptions** signalées par le progiciel et à la **qualité de l'état des lieux**, désormais fait une seule fois. Les responsables de résidence ne valident plus chaque attribution ; ils pilotent leur résidence à partir du tableau de bord d'occupation et arbitrent les cas particuliers.
- *Compétences* : usage du progiciel et de la tablette (photos, état des lieux numérique, activation des accès en cas d'anomalie) ; traitement des alertes et des exceptions ; aide aux résidents dans le parcours en ligne ; attention à la qualité de la donnée, saisie une seule fois et utilisée par tous.
- *Conditions* : la suppression des tâches de saisie peut être vécue comme une perte de repères ou une menace sur l'emploi ; il faut expliquer le sens du changement, associer des utilisateurs clés dans chaque résidence dès le cahier des charges, former au bon moment (lot 4, y compris les saisonniers) et accompagner les premières semaines.

**L'organisation de la rentrée** (0,5 pt) :
- Les arrivées sont **étalées** par créneaux choisis en ligne : les files d'une heure dans le hall disparaissent ; l'accueil peut se concentrer sur les états des lieux et les résidents qui ont besoin d'aide.
- Le **centre de relation résidents** ne trie plus des milliers de courriels de pièces : il se tourne vers l'assistance aux candidats pendant le parcours (questions, exceptions), sept jours sur sept de juin à octobre.
- La charge de saisie de septembre disparaît : les renforts saisonniers peuvent être consacrés à l'accueil et à la vie de la résidence plutôt qu'au traitement administratif.
- La **première rentrée sur le progiciel**, en 2028, doit être préparée : utilisateurs clés désignés dans chaque résidence, appui renforcé de la direction des systèmes d'information et de l'intégrateur pendant la campagne, consignes écrites pour les cas d'anomalie.

**Réponses tolérées**
- Processus cible représenté en schéma à couloirs (BPMN ou format libre lisible) plutôt qu'en tableau.
- Représentation du processus actuel ajoutée par le candidat : acceptée, sans rapporter de points en elle-même.
- Autres ruptures pertinentes tirées de l'annexe 1.4 (validation de chaque attribution par le responsable de résidence, quittances transmises par fichier mensuel au progiciel de gestion intégré).
- Processus cible qui conserve un contrôle par une personne de chaque dossier, à condition que ce contrôle ne bloque pas la signature (contrôle a posteriori, ou limité aux dossiers signalés).
- Effets sur le métier des agents du centre de relation résidents ou des responsables de résidence développés davantage que ceux des chargés d'accueil, si les trois axes demandés sont traités.
- Évolution des effectifs évoquée avec prudence (redéploiement plutôt que suppression, accueil des nouvelles résidences) : acceptée.

**Erreurs fréquentes**
- *Processus cible décrit en texte continu, sans acteurs ni applications* (`JUR-T10` schémas et tableaux lisibles ; `JUR-G07` cartographie de processus) — la représentation du processus cible par acteur est demandée.
- *Processus actuel recopié de l'annexe 1.4 au lieu d'être analysé* (`JUR-T03` analyser et argumenter) — seules les ruptures et leurs effets sont demandés.
- *Ruptures sans effet ni chiffre* (`JUR-T08` exploiter toutes les annexes) — l'annexe 1.4 donne pour chaque rupture un effet mesurable.
- *Processus cible qui numérise le papier sans changer l'enchaînement* (ET-20 urbanisation réduite à une vision technique) — scanner le formulaire ne supprime ni la ressaisie, ni l'échange de nuit, ni les doubles attributions.
- *Effets sur les métiers réduits à des suppressions de postes, ou omis* (`JUR-D03` transformation des métiers et compétences) — trois axes sont demandés.
- *Analyse du contenu du bail ou des pièces exigibles* (`JUR-T07` répondre à la seule question posée) — aucune analyse juridique n'est attendue.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Analyse et rationalisation des processus | représentation par acteur, ruptures, saisie unique, échanges en temps réel | F03 § 3 ; F05 § 7 (conduite du changement) | notion de cours |
| Service en ligne et interfaces | progiciel fourni en service, interfaces publiées par l'éditeur | F03 § 5 | notion de cours |

---

### 1.4 – Les contrats du projet et les risques d'un progiciel en ligne (3 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.b` « Typologie des contrats de prestation informatique (régie, forfait, infogérance, etc.) : méthodes d'intégration dans la stratégie SI et la gouvernance contractuelle » ; `1.4.d` « Méthodologie de négociation contractuelle et analyse des risques ». Limite : « L'analyse juridique approfondie relève du droit des contrats informatiques et est exclue du programme de l'UE. »

**Annexes mobilisées** : annexes 1.5 (lots, conditions de l'offre, besoins, calendrier), 1.3 (projets passés), 1.2 (témoignage de la présidente) et 1.1 (parc, saisonnalité des baux).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Quatre types de contrats présentés : abonnement à un service en ligne (usage d'un logiciel standard exploité par l'éditeur, prix récurrent, niveaux de service standard) ; forfait (livrable, prix et délai fixés, risque de dépassement pour le prestataire) ; régie (compétences au temps passé, dirigées par le client, qui porte le risque) ; unités d'œuvre (prix unitaires fixés à l'avance, facturés selon la consommation) | 0,5 |
| a-2 | Lot 1 : abonnement, justifié (logiciel standard, prix par logement qui suit le parc) ; lot 2 : forfait sur un cahier des charges validé, justifié (250 jours estimés « sur la base des besoins à ce jour », pas de chef de projet capable de diriger une régie), éventuellement précédé d'une courte phase de spécification | 0,5 |
| a-3 | Lot 3 : audit de la qualité des données puis forfait sur le périmètre arbitré ; lot 4 : unités d'œuvre (sessions ou personnes formées, saisonniers et nouvelles résidences) ; lot 5 : unités d'œuvre (corrections avec délais par gravité, évolutions à prix unitaire), justifiés par des prestations récurrentes dont le volume varie (saisonniers, ouvertures de résidences, trois versions par an) | 0,5 |
| b-1 | Dépendance à l'éditeur et réversibilité : causes tirées de l'annexe 1.5 (conditions générales standard, tacite reconduction, intégrateur exclusif, maintenances à toute heure ; format propriétaire, trente jours sans assistance) et traitement dans la négociation (conditions particulières, niveaux de service renforcés pendant la campagne, préavis ; restitution complète dans un format ouvert et documenté, assistance, maintien du service, essai de restitution) | 0,5 |
| b-2 | Évolution du service et du prix : causes (trois versions par an, retrait de fonctions avec six mois de préavis, module de séjours courts en 2029, prix révisable sans plafond) et traitement (plafond et paliers de prix, maintien des fonctions utilisées, information et environnement d'essai avant chaque version, engagement sur la date du module) | 0,5 |
| b-3 | Dérive du périmètre de l'intégration : causes (estimation sur les besoins actuels, devis pour tout besoin nouveau, besoins contradictoires, calcul spécifique, régie proposée) et traitement (forfait sur périmètre écrit, procédure de gestion des changements arbitrée par le comité de pilotage, enveloppe d'évolutions en unités d'œuvre, paiement aux jalons après recette par ORVANELLE, pénalités liées à la date de mai 2028) | 0,5 |

**Réponse attendue**

*1.4 a) – Les types de contrats et le contrat de chaque lot*

Les principaux types de contrats de prestation informatique (0,5 pt) :
- l'**abonnement à un service en ligne** : ORVANELLE paie l'usage d'un logiciel standard, hébergé, exploité et mis à jour par l'éditeur pour tous ses clients ; le prix est récurrent, par unité d'usage ; les niveaux de service et les évolutions sont ceux de l'offre ; ORVANELLE ne possède ni le logiciel ni l'infrastructure ;
- le **forfait** : le prestataire réalise un livrable défini, pour un prix et un délai fixés ; il s'engage sur le livrable et porte le risque de dépassement ; il suppose un besoin précisément écrit, sinon il produit des avenants ;
- la **régie** : le prestataire met à disposition des compétences facturées au temps passé ; il s'engage sur les moyens ; le client dirige les travaux et porte le risque de délai et de dépassement ; elle convient à un besoin évolutif, si le client sait piloter ;
- les **unités d'œuvre** : des prestations répétitives et récurrentes (une correction, une session de formation, un jour d'évolution) ont un prix unitaire fixé à l'avance et sont facturées selon la consommation réelle ; elles conviennent quand l'unité est bien définie et que la prestation revient régulièrement, même si son volume varie d'une année à l'autre.

**Le contrat de chaque lot** (0,5 pt pour les lots 1 et 2, 0,5 pt pour les lots 3 à 5) :

| Lot | Type de contrat recommandé | Justification tirée des annexes |
|---|---|---|
| 1. Abonnement au progiciel | **abonnement à un service en ligne**, négocié | progiciel standard, partagé par une trentaine de gestionnaires ; prix de 4 € par logement et par mois, qui suit le parc de 9 000 à 12 000 logements ; mais les conditions standard (annexe 1.5 C) doivent être complétées par des conditions particulières (b) |
| 2. Paramétrage et intégration | **forfait**, sur un cahier des charges validé ; éventuellement précédé d'une courte phase de spécification des interfaces, elle-même au forfait ou en régie plafonnée | 250 jours estimés « sur la base des besoins exprimés à ce jour » ; une régie dès maintenant laisserait tout le risque de dépassement à ORVANELLE, qui n'a ni chef de projet à temps plein ni pratique du pilotage (niveau 1 de CMMI, question 1.2), comme pour le portail de 2018 ; le forfait fait porter le risque à l'intégrateur et oblige à écrire le besoin |
| 3. Reprise des données | **en deux temps** : audit de la qualité des données (forfait court), puis **forfait** de reprise sur le périmètre arbitré (question 1.5), avec reprises à blanc | qualité jamais mesurée, données antérieures à 2016 sans identifiant ; un forfait sur 100 000 baux de qualité inconnue serait surévalué ou source d'avenants ; une régie serait sans limite |
| 4. Formation | **unités d'œuvre** (prix par session ou par personne formée), pour la vague initiale et les années suivantes | environ 260 utilisateurs en 2028, puis une quarantaine de saisonniers chaque été et les équipes des résidences ouvertes d'ici 2030 : la prestation est récurrente et bien définie, son volume varie |
| 5. Maintenance des interfaces | **unités d'œuvre** : corrections facturées par demande avec un délai de correction selon la gravité ; évolutions au prix unitaire du jour ou de l'unité d'évolution, dans une enveloppe annuelle | des corrections et des évolutions qui reviennent à chaque version (trois par an), mais dont le nombre varie ; une régie ne donnerait aucun engagement de délai, un forfait global serait surévalué |

*1.4 b) – Quatre risques contractuels d'un progiciel en ligne et leur traitement dans la négociation*

| Risque | Ce que révèle l'annexe 1.5 | Traitement dans la négociation |
|---|---|---|
| **Dépendance à l'éditeur** (0,5 pt avec la réversibilité) | tout le parcours et toutes les données de l'entreprise reposent sur un seul service ; conditions générales standard, « identiques pour tous » ; contrat de trois ans reconduit tacitement ; intégrateur partenaire exclusif de l'éditeur, qui réalise 60 % de son activité avec lui ; disponibilité de 99,5 % hors maintenances programmées « à toute heure », alors que 70 % des baux se signent entre juin et septembre | ORVANELLE gère 9 000 logements, puis 12 000 : elle a le poids d'obtenir des **conditions particulières** qui priment sur les conditions générales ; **niveaux de service renforcés pendant la campagne de rentrée**, mesurés et assortis de pénalités ; **maintenances programmées hors des heures et des mois de pointe** ; préavis de non-reconduction suffisant pour changer de solution ; possibilité de recourir à un autre intégrateur et transfert de compétences vers la direction des systèmes d'information |
| **Réversibilité et format de restitution** | restitution en fin de contrat dans un délai de trente jours, « dans un format propriétaire », sans assistance : ORVANELLE ne pourrait ni changer d'éditeur ni réutiliser son historique | données reconnues comme celles d'ORVANELLE ; **restitution complète** (historique, documents, paramétrage) **dans un format ouvert et documenté**, à la fin du contrat et sur demande en cours de contrat ; **plan de réversibilité** écrit : assistance de l'éditeur à prix convenu d'avance, maintien du service pendant la transition, **essai de restitution** chaque année |
| **Évolution du service et du prix décidée par l'éditeur** (0,5 pt) | trois versions par an décidées pour tous les clients ; une fonction peu utilisée peut être retirée avec six mois de préavis ; module de séjours courts annoncé pour 2029, sans engagement ; prix révisable chaque année selon la grille de l'éditeur, sans plafond | **plafond de révision** annuelle et **prix par palier** quand le parc passe de 9 000 à 12 000 logements ; **maintien des fonctions utilisées** par ORVANELLE (états des lieux, interfaces publiées) ou préavis plus long ; **information préalable et environnement d'essai** avant chaque version, pour vérifier les interfaces ; feuille de route communiquée et **engagement daté** sur le module de séjours courts, ou condition de prix s'il est reporté |
| **Dérive du périmètre de l'intégration** (0,5 pt) | 250 jours estimés sur les besoins « à ce jour » ; « tout besoin nouveau fera l'objet d'un devis » ; huit besoins dont certains se contredisent ; calcul spécifique des charges que l'intégrateur propose de développer à côté ; facturation au temps passé proposée « dès maintenant » | **forfait sur un périmètre écrit** (inclus et exclus) issu du cahier des charges arbitré (question 1.5) ; **procédure de gestion des changements** : toute demande est chiffrée par l'intégrateur et arbitrée par le comité de pilotage d'ORVANELLE, jamais acceptée directement par une direction ; **enveloppe d'évolutions** en unités d'œuvre à prix fixé d'avance ; **paiement aux jalons** après recette par ORVANELLE ; pénalités de retard liées à la mise en service de mai 2028 |

**Réponses tolérées**
- Lot 2 en régie pour la seule phase d'ateliers et de spécification, puis au forfait : accepté s'il est justifié par l'instabilité actuelle des besoins.
- Lot 4 au forfait pour la vague initiale de 2028, puis en unités d'œuvre : accepté.
- Lot 5 sous la forme d'un contrat de tierce maintenance applicative avec niveaux de service : accepté, s'il est relié au caractère récurrent des corrections et aux versions de l'éditeur.
- Autres risques pertinents tirés de l'annexe 1.5 (hébergement hors de France : vérifier qu'il reste dans l'Union européenne et que l'éditeur agit en sous-traitant, avec un accord écrit ; défaillance ou rachat de l'éditeur), en plus des quatre demandés.
- Mention de l'accord de sous-traitance prévu par le RGPD (annexe 1.6), en principe : valorisée.

**Erreurs fréquentes**
- *Régie et forfait inversés, ou abonnement confondu avec une licence achetée* (ET-31 régie, forfait et infogérance confondus ; ET-30 SaaS et on premise confondus) — en régie, c'est le client qui dirige et porte le risque.
- *Un seul type de contrat pour tout le projet* (`JUR-T03` analyser et argumenter) — chaque lot appelle un choix justifié par sa nature et par ce que l'on sait de son volume.
- *Conditions générales acceptées parce qu'elles seraient non négociables* (`JUR-G11` forces et faiblesses du SaaS ; `JUR-A05` contractualisation des services externalisés) — la taille d'ORVANELLE permet d'obtenir des conditions particulières.
- *Risques énumérés sans traitement* (`JUR-T03`) — chaque risque appelle une proposition de négociation.
- *Analyse juridique des clauses* (`JUR-T07` répondre à la seule question posée ; limite du programme 1.4) — non attendue.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des contrats de prestation informatique | abonnement à un service en ligne, forfait, régie, unités d'œuvre | F04 § 1 ; `erreurs_types.md` ET-30, ET-31 | notion de cours |
| Clauses critiques et risques de la relation | niveaux de service, réversibilité, évolution des prix, dépendance | F04 § 4 et § 6 | notion de cours |
| RGPD (règlement (UE) 2016/679) | éditeur sous-traitant, accord écrit (réponse tolérée, en principe) | `rgpd` ; F15 § 5 | en vigueur |

---

### 1.5 – Le cahier des charges et les risques du projet (3 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de SI : `1.5.c` « Élaboration d'un cahier des charges fonctionnel et technique » ; `1.5.e` « Identification et gestion des risques (maintenance, évolutivité, sécurité) » ; `1.5.a` « Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ». Limite : « L'aspect budgétaire détaillé ne relève pas du programme de l'UE. »

**Annexes mobilisées** : annexes 1.5 (option, lots, conditions, besoins, calendrier), 1.4 (parcours actuel), 1.3 (projets passés), 1.6 (RGPD) et 1.1 (parc, saisonnalité, effectif de la direction des systèmes d'information).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Structure du cahier des charges fonctionnel (contexte et objectifs reliés au plan, périmètre, acteurs, processus cibles, exigences priorisées, règles de gestion, volumétrie et pic) et technique (interfaces, sécurité et données personnelles, disponibilité, réversibilité, reprise, exploitation), contraintes, organisation et modalités de réponse, appliquée au projet | 0,5 |
| a-2 | Méthode nommée (MoSCoW) et classement des huit besoins, chacun justifié par un objectif du plan ou une contrainte de l'annexe 1.5 | 0,5 |
| a-3 | Arbitrages motivés entre les besoins qui se contredisent : signature en dix minutes et contrôle à la main ; paiement en trois fois et accès après paiement complet ; dix-huit ans d'historique et calendrier ; calcul spécifique et progiciel standard | 0,5 |
| b-1 | Démarche de gestion des risques présentée (identifier, coter la probabilité et l'impact, traiter : éviter, réduire, transférer, accepter ; suivre dans un registre revu en comité) ; risque de maintenance complet (cause, cotation, réponse, responsable) | 0,5 |
| b-2 | Risque d'évolutivité et risque de sécurité complets | 0,5 |
| b-3 | Quatrième risque complet ; cotations cohérentes avec les annexes ; responsables désignés ; risques distincts des risques contractuels de la question 1.4 | 0,5 |

**Réponse attendue**

*1.5 a) – La structure du cahier des charges et la priorisation des besoins*

Le **cahier des charges** est le document, rédigé par ORVANELLE en tant que maître d'ouvrage avec les utilisateurs et validé par le sponsor, qui exprime le besoin à satisfaire et les contraintes à respecter ; il sert de base à la consultation, au contrat au forfait (question 1.4) et à la recette. Sa structure, appliquée au projet (0,5 pt) :

| Partie | Contenu pour le projet de remplacement |
|---|---|
| **Contexte et objectifs** | fin de maintenance de l'ancien logiciel en décembre 2028 ; objectifs reliés à « ORVANELLE 2030 » et mesurables (bail signé le jour de la candidature, aucune ressaisie, parc de 12 000 logements) |
| **Périmètre** | processus couverts, de la candidature à la remise des accès et au quittancement ; ce qui est exclu (séjours courts jusqu'en 2029, calcul spécifique des charges) ; cinq lots |
| **Acteurs et processus cibles** | candidats, garants, centre de relation résidents, résidences, directions ; processus cible de la question 1.3 |
| **Exigences fonctionnelles priorisées et règles de gestion** | huit besoins classés (ci-dessous) ; règles d'attribution des logements et de remise des accès |
| **Volumétrie et pointe** | 9 000 puis 12 000 logements ; environ 7 000 baux par an, dont 70 % entre juin et septembre ; 30 000 candidatures commencées en 2026 |
| **Exigences techniques** | cinq interfaces (portail, signature, paiement, clé virtuelle, progiciel de gestion intégré) sur les interfaces publiées par l'éditeur ; sécurité et données personnelles (hébergement dans l'Union européenne, éditeur sous-traitant, accès de l'intégrateur) ; disponibilité pendant la campagne et maintenances hors pointe ; réversibilité dans un format ouvert ; reprise des données ; exploitation et maintenance |
| **Contraintes et organisation** | calendrier (contrats en juin 2027, mise en service en mai 2028) ; disponibilité des utilisateurs clés hors campagne ; instances du projet ; formation |
| **Modalités de réponse** | cadre de réponse et critères d'évaluation des offres, pour les éléments encore à consulter (intégration, reprise, formation, maintenance) |

**Classement des huit besoins par la méthode MoSCoW** (*Must have*, *Should have*, *Could have*, *Won't have this time*) (0,5 pt) :

| N° | Besoin | Classe | Justification |
|---|---|---|---|
| 1 | Signature du bail en moins de dix minutes | **Must** | cœur du parcours entièrement en ligne ; la moitié des abandons a lieu à l'étape du formulaire papier du garant, que le parcours de signature en ligne supprime ; concurrents « en quelques minutes » |
| 6 | Interface avec la clé virtuelle | **Must** | « remise des accès » de l'objectif ; supprime l'activation à l'accueil dans les 22 résidences équipées |
| 5 | Reprise des données | **Must** pour les données vivantes (logements, résidents en place, baux en cours, dépôts de garantie à restituer, historique récent) ; **Won't** pour la reprise complète de dix-huit ans | sans les données vivantes, pas de mise en service ; la reprise complète ajoute quatre mois et porte sur des données antérieures à 2016 incomplètes |
| 2 | États des lieux sur tablette, avec photos | **Should** | fonction standard, supprime une ressaisie et sert le parcours en ligne ; peut être déployé résidence par résidence si les tablettes ne sont pas prêtes en mai 2028 |
| 3 | Tableau de bord d'occupation en temps réel | **Should** | fonction standard, sert l'objectif de 95 % ; peu de risque |
| 4 | Paiement du dépôt de garantie en trois fois | **Could** | attractivité pour les étudiants venus de l'étranger, option du prestataire de paiement ; contredit la règle de la direction financière |
| 7 | Module de séjours courts d'été | **Won't** (pour la mise en service de 2028) | annoncé par l'éditeur pour 2029 ; les séjours de l'été 2028 restent suivis comme aujourd'hui |
| 8 | Calcul spécifique des charges par propriétaire | **Won't** | le progiciel n'accepte aucun développement spécifique ; un calcul « à côté », à adapter trois fois par an, créerait une maintenance et un risque permanents |

**Arbitrages entre besoins contradictoires** (0,5 pt) :
- *Signature en dix minutes (1) contre contrôle à la main de chaque dossier par le centre de relation résidents* : le contrôle de complétude devient automatique ; le centre de relation résidents ne contrôle plus que les dossiers signalés par le progiciel. Le contrôle humain systématique est incompatible avec l'objectif et explique aujourd'hui six jours de délai.
- *Paiement en trois fois (4) contre accès remis après paiement complet (direction financière)* : la règle de remise des accès relève d'une décision du directoire, pas du projet ; le besoin est classé Could et peut être ajouté après la mise en service, par exemple avec des accès remis dès la première échéance si le directoire l'accepte.
- *Dix-huit ans d'historique (5) contre calendrier* : quatre mois de plus repousseraient la mise en service après mai 2028, en pleine campagne, alors que l'ancien logiciel s'arrête en décembre 2028. Arbitrage : reprise des données vivantes et de l'historique récent ; données anciennes conservées dans une extraction consultable, hors du progiciel.
- *Calcul spécifique (8) contre progiciel standard* : il contredit le choix même d'un progiciel en ligne et l'évolutivité du socle. Arbitrage : paramétrer les règles standard du progiciel, harmoniser les règles de charges avec les propriétaires, à commencer par les nouvelles résidences, et garder provisoirement les cas particuliers hors du progiciel ; décision au directoire, avec M. LORMIÈRE.

*1.5 b) – La démarche de gestion des risques et le registre des risques du projet*

La **gestion des risques d'un projet** consiste à **identifier** les événements incertains qui menaceraient ses objectifs (délai, qualité, coût, sécurité), à les **coter** (probabilité × impact, ici de 1 à 4), à décider d'une **réponse** (éviter, réduire, transférer, accepter) confiée à un **responsable**, puis à les **suivre** dans un registre revu à chaque comité de pilotage (0,5 pt avec le premier risque). Les risques ci-dessous sont ceux de la conduite et du résultat du projet ; les risques contractuels de la question 1.4 n'y sont pas repris.

| Risque | Cause tirée des annexes | P | I | Réponse | Responsable |
|---|---|---|---|---|---|
| **Maintenance** : après le départ de l'intégrateur, ORVANELLE ne sait pas faire vivre le paramétrage et les cinq interfaces (0,5 pt avec la démarche) | seize personnes, dont 70 % du temps sur l'existant ; aucun chef de projet ; savoir concentré chez l'intégrateur ; trois versions du progiciel par an | 3 | 3 | **réduire** : transfert de compétences prévu dans le lot 2 (documentation du paramétrage et des interfaces, travail en binôme), deux administrateurs du progiciel désignés à la direction des systèmes d'information, maintenance des interfaces en unités d'œuvre (lot 5) ; temps libéré par l'arrêt de l'ancien logiciel | Mme VARQUIGNY, directrice des systèmes d'information |
| **Évolutivité** : le socle paramétré pour 60 résidences ne suit pas le passage à 12 000 logements dans vingt villes, ni le pic de la rentrée (0,5 pt avec le risque de sécurité) | parc porté de 9 000 à 12 000 logements ; 70 % des baux entre juin et septembre ; règles propres à chaque propriétaire ; tentation des développements spécifiques, à reprendre à chaque version | 3 | 4 | **éviter** les spécifiques (besoin 8 en Won't) ; **réduire** : paramétrage par modèle de résidence réutilisable pour chaque ouverture ; exigences de volumétrie et de pointe écrites dans le cahier des charges ; références de clients de taille comparable demandées à l'éditeur ; interfaces bâties sur les interfaces publiées par l'éditeur | chef de projet, avec la direction des systèmes d'information |
| **Sécurité** : fuite ou altération des données des résidents pendant le projet | reprise d'environ 100 000 baux et des données des résidents, extraites et transférées entre ORVANELLE, l'intégrateur et l'éditeur ; essais faits sur des données réelles ; accès larges de l'intégrateur ; habitude des envois par courriel (annexe 1.4) | 2 | 4 | **réduire** : transferts par un espace sécurisé et chiffré, jamais par courriel ; données fictives ou anonymisées pour les essais ; accès nominatifs et temporaires de l'intégrateur, retirés à la mise en service ; reprise limitée au périmètre arbitré ; extractions supprimées après contrôle ; accord écrit de sous-traitance avec l'éditeur et l'intégrateur | Mme VARQUIGNY, directrice des systèmes d'information |
| **Calendrier et reprise des données** : mise en service repoussée après mai 2028, en pleine campagne de rentrée (0,5 pt avec la cohérence d'ensemble) | qualité des données jamais mesurée, données antérieures à 2016 sans identifiant ; utilisateurs clés peu disponibles pendant la campagne de 2027 (centre de relation résidents ouvert sept jours sur sept de juin à octobre) ; dérapages des projets passés (huit mois de retard pour le portail) | 3 | 4 | **réduire** : audit de la qualité des données dès l'été 2027, deux reprises à blanc, ateliers avec les utilisateurs clés placés hors de la campagne ; date de décision de mise en service fixée en mars 2028 ; **plan de repli** : campagne de 2028 sur l'ancien logiciel, maintenu jusqu'en décembre 2028, et bascule à l'automne | chef de projet ; décision par le comité de pilotage, présidé par le (la) membre du directoire chargé(e) des opérations |

**Réponses tolérées**
- Autre méthode de priorisation nommée et appliquée (classement par la valeur et l'effort, priorités 1 à 3), si les huit besoins sont classés et les arbitrages justifiés.
- États des lieux sur tablette (2) classés Must, au titre du parcours entièrement en ligne ; tableau de bord (3) classé Could ; reprise de l'historique sur une autre profondeur que celle proposée, si l'arbitrage avec le calendrier est explicite.
- Quatrième risque différent, s'il est tiré des annexes et complet : résistance au changement des chargés d'accueil, indisponibilité des utilisateurs clés, départ du chef de projet, interfaces avec le portail de 2018 plus difficiles que prévu.
- Autres échelles de cotation, ou criticité calculée (P × I), si elles sont cohérentes ; réponses par transfert (assurance, engagement d'un prestataire) acceptées si elles sont justifiées.
- Structure du cahier des charges présentée en deux documents (fonctionnel, technique).

**Erreurs fréquentes**
- *Tous les besoins classés Must, ou classement sans justification* (`JUR-T03` analyser et argumenter) — la méthode sert à arbitrer ; les contradictions de l'annexe 1.5 D doivent être tranchées.
- *Cahier des charges réduit à une liste de fonctions* (F05 § 3) — il comprend contexte, objectifs, périmètre, volumétrie, exigences techniques et contraintes.
- *Risques contractuels de la question 1.4 repris dans le registre* (`JUR-T07` répondre à la seule question posée) — dépendance, réversibilité, évolution des prix et dérive du périmètre relèvent du contrat.
- *Risques sans cotation, sans réponse ou sans responsable* (`JUR-P02` facteurs clés de succès et risques dans le contexte) — chaque risque porte les éléments demandés.
- *Planning ou chiffrage du projet construits* (`JUR-T07` ; limite du programme 1.5) — non demandés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cahier des charges fonctionnel et technique | structure, exigences priorisées, contraintes | F05 § 3 | notion de cours |
| Méthode MoSCoW | *Must, Should, Could, Won't* | F05 § 2.2 | notion de cours |
| Gestion des risques d'un projet | identification, cotation, réponses, registre ; maintenance, évolutivité, sécurité | F05 § 5 | notion de cours |
| RGPD (règlement (UE) 2016/679) | accord de sous-traitance avec l'éditeur et l'intégrateur (en principe) | `rgpd` ; F15 § 5 | en vigueur |
