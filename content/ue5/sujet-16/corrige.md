# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 16

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Préparer la stratégie du système d'information et le projet de remplacement du logiciel de gestion locative | 14 | 1.1 à 1.5 | `exercices/ex46_alignement_projet_gestion_locative` |
| 2 – Organiser et exploiter les données des séjours, éclairer deux projets | 13 | 2.1 à 2.4 | `exercices/ex47_entrepot_sejours_attestations` |
| 3 – Sécuriser la campagne de rentrée, auditer le traitement des candidatures et piloter l'énergie des résidences | 13 | 3.1 à 3.4 | `exercices/ex48_rentree_continuite_audit_energie` |
| **Total** | **40** | | |

---

## DOSSIER 1 – PRÉPARER LA STRATÉGIE DU SYSTÈME D'INFORMATION ET LE PROJET DE REMPLACEMENT DU LOGICIEL DE GESTION LOCATIVE (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES SÉJOURS, ÉCLAIRER DEUX PROJETS (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 L'entrepôt des séjours | `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) ; `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 3,5 |
| 2.2 L'analyse de l'occupation et des demandes d'intervention | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation | 4 |
| 2.3 Le retour sur investissement du projet d'entrepôt | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord | 3 |
| 2.4 Les attestations de logement et la chaîne de blocs | `3.3.b` Fonctionnement des technologies de registres distribués (DLT) ; `3.3.c` Typologie des applications : traçabilité, certification, finance décentralisée, NFT ; `3.3.a` Évaluer les opportunités, les risques et le cadre réglementaire associés à la mise en œuvre de solutions fondées sur la blockchain et les cryptoactifs dans les organisations ; `3.3.d` Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO | 2,5 |
| **Dossier 2 – Organiser et exploiter les données des séjours, éclairer deux projets** |  | **13** |

Répartition indicative : connaissances (entrepôt de données, table des faits, dimensions et granularité, règles de passage, chaîne de traitement, analyses descriptive et exploratoire, retour sur investissement, indicateur à cinq champs, chaîne de blocs publique et empreinte, typologie des applications, objet de MiCA) environ 2,5 points (la moitié des items 2.1 a-1, 2.1 b-1, 2.1 b-4, 2.2 a-1, 2.2 c-2, 2.3 a-1, 2.3 c-1, 2.4 a-1, 2.4 a-2 et 2.4 c-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – L'entrepôt des séjours (3,5 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) » ; `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) », dont le schéma en étoile d'un entrepôt (faits, dimensions) fait à la main à partir de règles de gestion écrites ; `2.1.a` « Structurer et organiser les données […] afin d'en garantir la cohérence, la qualité […] ». Aucune requête ; modèle physique seulement nommé.

**Annexes mobilisées** : annexe 2.1 (situation actuelle, questions du directoire, règles de gestion de l'entrepôt) ; annexe 1.1 (logiciel de gestion locative, portail, logiciel de suivi des demandes d'intervention, parc).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Entrepôt de données défini (orienté sujet, intégré, historisé, non volatile, structuré pour l'analyse) ; première raison appliquée à l'annexe 2.1 | 0,5 |
| a-2 | Deuxième raison, tirée de l'annexe 2.1 | 0,5 |
| a-3 | Troisième raison ; conclusion : une seule version des chiffres, à condition d'écrire les règles de calcul, sans données nominatives (RG8) | 0,5 |
| b-1 | Table des faits et granularité justifiée par RG6 (un logement, un mois, un profil de séjour, un canal de réservation) ; faits et dimensions distingués | 0,5 |
| b-2 | Quatre dimensions et leurs attributs, dont la dimension temps ; résidence et ville dénormalisées dans la dimension Logement (étoile) | 0,5 |
| b-3 | Quatre mesures additives (RG7), dont les jours-places ; taux d'occupation calculé à la restitution, non stocké ; profil « aucun séjour » pour la vacance | 0,5 |
| b-4 | Modèle logique de cinq tables, avec la clé composée des quatre clés étrangères de la table des faits, déduit par les règles de passage énoncées | 0,5 |

**Réponse attendue**

*2.1 a) – L'entrepôt de données et les extractions mensuelles*

**Définition** (0,5 pt avec la première raison) : un **entrepôt de données** est une base **orientée sujet** (ici, les séjours et l'occupation), **intégrée** (les données de plusieurs applications y sont rapprochées selon des identifiants et des définitions communes), **historisée** et **non volatile** (les données chargées ne sont ni écrasées ni modifiées, l'historique s'accumule), structurée pour l'analyse, en général selon un schéma en étoile (faits et dimensions). Il est alimenté par des chargements réguliers depuis les applications de gestion, qu'il ne remplace pas (F07 § 1 et 6).

Trois raisons parmi les suivantes (0,5 pt par raison, la troisième avec la conclusion) :

1. **L'intégration des trois sources.** Aujourd'hui, deux personnes rapprochent à la main, chaque mois, le logiciel de gestion locative, le portail et le logiciel des demandes d'intervention, par l'adresse, faute de numéro de logement commun : huit jours-personne par mois, avec des risques d'erreur. L'entrepôt est chargé chaque nuit et rapproche les données par un **numéro unique de logement**, commun à toutes les applications (RG1).
2. **L'historisation.** Chaque extraction remplace la précédente, et l'historique n'existe que dans des tableurs aux colonnes changeantes : comparer 2025 et 2026, ou un été à l'autre, suppose de retraiter les fichiers. L'entrepôt conserve chaque mois, avec la dimension temps, ce qui permet de suivre l'occupation par mois, par saison et par année universitaire.
3. **Des définitions communes, donc un seul chiffre.** Le taux d'occupation de 2026 vaut 93 %, 91 % ou 95 % selon la direction, parce que chacune applique ses propres règles, écrites nulle part. L'entrepôt calcule les indicateurs selon des règles écrites et partagées (RG6 et RG7, documentées dans le dictionnaire des données) : une seule version des chiffres pour le directoire.
4. **Des axes d'analyse croisés.** Les questions du directoire croisent la résidence, la ville, le type de logement, le mois, le profil de séjour, l'origine du résident et le canal : le schéma en étoile en fait des dimensions, sur lesquelles on agrège et on fore (de la ville à la résidence, puis au logement) sans retraitement.
5. **Une diffusion possible sans risque pour les résidents.** L'entrepôt ne contient ni donnée nominative ni donnée sensible (RG8) : il peut être ouvert aux directions et aux responsables de résidence, ce que ne permettent pas des extractions brutes du logiciel de gestion locative.

**Conclusion** : l'entrepôt ne vaut que par ses règles. Le gain tient moins à l'outil qu'à la décision de fixer un identifiant commun, des définitions écrites et un propriétaire de chaque indicateur ; c'est aussi la condition pour suivre l'objectif de 95 % d'« ORVANELLE 2030 » avec un chiffre incontesté.

*2.1 b) – Le schéma en étoile de l'entrepôt des séjours*

**La table des faits et sa granularité** (0,5 pt) : la **table des faits** enregistre les mesures d'un événement ou d'une situation, au **grain** choisi ; les **dimensions** sont les axes d'analyse, avec leurs attributs descriptifs (F07 § 6.1). Ici, la table des faits **Occupation_mensuelle** a pour grain : **un logement, un mois, un profil de séjour et un canal de réservation** (RG6). Un grain « logement × mois » ne suffirait pas : une colocation dont les chambres sont louées à des résidents de profils différents, ou un logement qui passe en juillet de l'année universitaire à un séjour court d'été, demandent une ligne par profil et par canal. Un grain plus fin (le jour, le séjour) n'est pas nécessaire aux questions du directoire.

**Les quatre dimensions** (0,5 pt) :
- **Logement** (num_logement, type_logement, nb_places, code_residence, nom_residence, date_ouverture_residence, ville) : la hiérarchie logement → résidence → ville (RG1 et RG2) est **dénormalisée** dans la dimension, ce qui fait un schéma en **étoile** et permet de forer de la ville au logement ;
- **Mois** (code_mois, annee, numero_mois, saison, annee_universitaire) : la dimension temps, avec la saison (été ou année universitaire) et l'année universitaire, qui ne coïncide pas avec l'année civile (RG3) ;
- **Profil_sejour** (code_profil, type_sejour, origine_resident) : le type de séjour (année universitaire, séjour court d'été, aucun séjour) et l'origine du résident (RG4) ; c'est la seule trace du résident, conformément à RG8 ;
- **Canal_reservation** (code_canal, libelle_canal) (RG5).

**Les mesures** (0,5 pt), toutes **additives** selon chaque dimension : jours_places_ouverts, jours_places_occupes, redevance_facturee, nb_demandes_intervention (RG7). Les jours où un logement pouvait être loué mais est resté libre forment une ligne du profil « aucun séjour », avec des jours-places ouverts et aucun jour-place occupé ; un logement en travaux ou dans une résidence pas encore ouverte n'a pas de jours-places ouverts. Les indicateurs sont calculés à la restitution, par somme puis rapport, à n'importe quel niveau :
- taux d'occupation = somme des jours-places occupés / somme des jours-places ouverts ; taux de vacance = 1 − taux d'occupation ;
- part des séjours courts dans l'été = jours-places occupés par le profil « séjour court d'été » en saison « été » / jours-places occupés en été ;
- part du portail = jours-places occupés par des séjours réservés sur le portail / jours-places occupés ;
- demandes d'intervention par logement, par résidence ou par type.

Un taux ne se stocke pas dans la table des faits : il ne s'additionne pas.

**Le modèle logique** (0,5 pt), obtenu par les règles de passage :
1. chaque dimension devient une table, dont l'identifiant devient la clé primaire ;
2. la table des faits traduit une association entre les quatre dimensions dont toutes les cardinalités maximales valent n : elle devient une table dont la clé primaire est composée des identifiants des quatre dimensions, chacun étant aussi clé étrangère, et qui porte les mesures.

- Logement (<u>num_logement</u>, type_logement, nb_places, code_residence, nom_residence, date_ouverture_residence, ville)
- Mois (<u>code_mois</u>, annee, numero_mois, saison, annee_universitaire)
- Profil_sejour (<u>code_profil</u>, type_sejour, origine_resident)
- Canal_reservation (<u>code_canal</u>, libelle_canal)
- Occupation_mensuelle (<u>#num_logement, #code_mois, #code_profil, #code_canal</u>, jours_places_ouverts, jours_places_occupes, redevance_facturee, nb_demandes_intervention)

Exemple de lecture : une colocation de trois chambres de Rennes, en octobre 2026, dont deux chambres sont louées pour l'année universitaire à des résidents venus de l'étranger, réservées sur le portail, et la troisième reste libre, donne deux lignes : (profil « année universitaire, étranger », canal « portail », 62 jours-places ouverts, 62 occupés) et (profil « aucun séjour », canal « sans objet », 31 ouverts, 0 occupé). Son taux d'occupation d'octobre est de deux tiers, et non de zéro comme dans le tableau actuel.

**Réponses tolérées**
- Schéma en flocon (tables Résidence et Ville, ou Type de logement, reliées à la dimension Logement), s'il est justifié (moins de redondance, plus de jointures) et si les faits restent reliés au logement.
- Cinquième dimension (Résidence ou Type de logement) reliée directement à la table des faits, si la redondance avec la dimension Logement est signalée.
- Grain « logement × mois », avec le profil et le canal du séjour principal du mois, si le candidat signale la perte d'information pour les colocations.
- Identifiant technique de ligne dans la table des faits, en plus des quatre clés étrangères.
- Représentation de type Merise (association porteuse des mesures entre quatre entités) ou dessin de l'étoile, si elle est lisible (`JUR-T10`).
- Autres raisons tirées de l'annexe 2.1 en a), si elles sont appliquées au cas (fraîcheur quotidienne, libre-service des directions).

**Erreurs fréquentes**
- *Entrepôt confondu avec un lac de données ou avec une base de production* (`ET-24`) — entrepôt présenté comme une copie des applications ou comme un stockage de données brutes.
- *Modèle de gestion au lieu d'un schéma en étoile* — entités Résident, Bail, Candidature avec leurs associations : c'est le modèle d'un logiciel de gestion, non celui d'un entrepôt ; un résident nominatif contredit en outre RG8.
- *Granularité absente ou incohérente* — table des faits sans grain énoncé, ou mesures qui ne s'additionnent pas (taux d'occupation stocké).
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères oubliées ou clé de la table des faits non composée.
- *Morceau de cours ou requête hors attente* (`JUR-T01`, `JUR-T07`) — définition de l'entrepôt sans application au cas, ou requêtes écrites alors que la question n'en demande pas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Entrepôt de données ; schéma en étoile et en flocon ; faits, dimensions, grain, mesures additives | définitions et méthode | F07 § 1 et 6 ; F08 § 1 | notion de cours |
| Règles de passage au modèle logique | méthode | F07 § 4 | notion de cours |

---

### 2.2 – L'analyse de l'occupation et des demandes d'intervention (4 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique ». Limites : aucun calcul statistique, aucune manipulation d'outil, aucun développement d'algorithme ; lecture critique des corrélations et des biais, reliée à la stratégie.

**Annexes mobilisées** : annexe 2.2 (occupation par ville et par type, affirmation du directeur commercial, limites) ; annexe 2.3 (demandes d'intervention, extraits, projet de l'équipe données) ; annexes 2.1 (règles de l'entrepôt) et 2.6 (principes du RGPD) ; « ORVANELLE 2030 » (présentation).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Étapes de la chaîne présentées ; résidences de Rennes et logements en travaux de Toulouse : étape où chaque limite est corrigée, et comment | 0,5 |
| a-2 | Colocations comptées par logement et écart entre les taux des directions : étape et correction ; conclusion | 0,5 |
| b-1 | Deux constats argumentés et chiffrés, avec leur portée pour « ORVANELLE 2030 » | 0,5 |
| b-2 | Troisième constat argumenté et chiffré | 0,5 |
| b-3 | Affirmation appréciée (résidences ouvertes en cours d'année et effet de structure, unité de mesure des colocations, été et groupes, canal) ; conclusion nuancée | 0,5 |
| c-1 | Deux apports de l'exploitation du texte des demandes, appliqués au cas (catégories, langues, problèmes récurrents, interventions) | 0,5 |
| c-2 | Méthode d'analyse : descriptive et surtout exploratoire, justifiée ; ni prédiction ni développement | 0,5 |
| c-3 | Deux précautions justifiées par l'annexe 2.3 et les principes de l'annexe 2.6 | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de traitement des indicateurs d'occupation*

**La chaîne de traitement** (0,5 pt avec les limites de Rennes et de Toulouse) transforme des données brutes en information utile à la décision : **collecte** des données à leur source, **nettoyage** (doublons, valeurs manquantes, aberrantes ou incohérentes), **structuration** (règles de gestion et de calcul, rapprochements, chargement dans un entrepôt historisé), **analyse**, puis **restitution** aux décideurs (F08 § 1). Chaque étape peut introduire un biais que les suivantes ne corrigent pas. Pour les indicateurs d'occupation :

| Étape | Ce que fera la chaîne | Limite corrigée (annexe 2.2 D, écart des taux de l'annexe 2.1 A) |
|---|---|---|
| **Collecte** | chargement chaque nuit des trois applications, par le numéro unique de logement ; collecte, en plus des baux, des dates d'ouverture des résidences, des périodes de travaux et des baux par chambre de colocation | le tableau ignore l'ouverture des résidences de Rennes au 1er septembre et la fermeture de 120 logements à Toulouse : l'information n'est pas collectée |
| **Nettoyage** | contrôles de cohérence : aucun jour vacant compté pour un logement fermé ou une résidence pas encore ouverte ; rejets tracés dans un journal | les 120 logements de Toulouse en travaux sont comptés comme vacants pendant six mois, ce qui fait passer Toulouse de 94 % à 88 % |
| **Structuration** | application des règles RG6 et RG7 au chargement : jours-places, une place par chambre de colocation, jours ouverts seulement après l'ouverture et hors travaux | le dénominateur « logements en fin d'année × 365 » compte Rennes sur douze mois, été compris ; une colocation n'est occupée que si toutes ses chambres le sont |
| **Analyse** | taux calculés comme rapports de sommes, à n'importe quel niveau ; comparaison à périmètre constant (résidences ouvertes les deux années) à côté du total | l'ensemble mêle les résidences nouvelles et anciennes : la baisse de 94 % à 91 % est lue comme une dégradation |
| **Restitution** | tableau de bord dans l'outil décisionnel, avec la définition de chaque indicateur, le périmètre et la cible de 95 % ; occupation par chambre pour les colocations | écart entre les taux des directions (93 %, 91 % et 95 %, annexe 2.1 A) : un seul taux, défini une fois, pour tous |

En résumé : Rennes est corrigé à la collecte (date d'ouverture) et à la structuration (jours ouverts) ; Toulouse à la collecte (périodes de travaux) et au nettoyage ; les colocations à la collecte (baux par chambre) et à la structuration (jours-places) ; l'écart entre les directions à la structuration (règles écrites RG6 et RG7) et à la restitution.

**Conclusion** (0,5 pt avec les colocations et l'écart des directions) : les limites du tableau ne sont pas des erreurs de calcul, mais des règles implicites. La chaîne les corrige en amont, par la collecte des bonnes informations et des règles écrites, et non par des retraitements à la main en fin de mois.

*2.2 b) – Trois constats et l'affirmation de M. CALVÉRAC*

**Trois constats** parmi les suivants (0,5 pt pour deux constats, 0,5 pt pour le troisième : le fait chiffré, son interprétation et sa portée) :

1. **La baisse de l'occupation de 94 % à 91 % est surtout un effet de mesure.** Lyon (96 %) et Montpellier (95 %) sont stables, les onze autres villes progressent (de 93 % à 94 %). La baisse vient de Rennes (30 %), dont les 400 logements, ouverts en septembre, sont comptés sur l'année entière, et de Toulouse (de 94 % à 88 %), où 120 logements étaient fermés pour travaux. Rennes pèse à lui seul près de trois points sur l'ensemble ; mesurée sur les seuls jours ouverts, l'occupation de 2026 serait plutôt de l'ordre de 94 à 95 %, proche de l'objectif de 95 %. Le directoire ne doit pas réagir à une baisse qui n'existe pas.
2. **L'été est le vrai creux.** L'occupation tombe à 69 % en juillet et août, contre 91 % sur l'année ; les séjours courts y font de 30 % (studios) à 70 % (colocations) de l'occupation. Atteindre 95 % en moyenne annuelle passera par l'été : offre de séjours courts, accueil de groupes, ce que l'entrepôt permettra de suivre par profil et par canal.
3. **Le portail progresse, sauf pour les colocations.** La part des réservations faites sur le portail passe de 62 % à 65 %, et de 65 % à 70 % pour les studios, mais reste à 30 % pour les colocations : le portail ne permet pas de réserver une chambre seule. C'est un frein commercial, en contradiction avec le parcours entièrement en ligne voulu par « ORVANELLE 2030 ».
4. **Le délai de relocation des colocations est mesuré à la dernière chambre.** 35 jours contre 10 pour les studios, mais une colocation n'est relouée, dans le tableau, que lorsque sa dernière chambre libre l'est : l'indicateur compare des unités différentes.

**L'affirmation de M. CALVÉRAC** (0,5 pt) : « les colocations se louent mal, de plus en plus mal » n'est pas démontré :
- **les résidences ouvertes en cours d'année créent un effet de structure** : 200 des 900 colocations, soit plus d'une sur cinq, sont à Rennes, ouvertes en septembre et comptées sur l'année et sur l'été. La baisse de 84 % à 74 % sur l'année et de 78 % à 61 % en été vient de ce changement de composition : les 200 colocations de Rennes n'existaient pas l'été 2026. Hors Rennes, les colocations anciennes ont plutôt progressé ;
- **l'unité de mesure les pénalise** : une colocation de trois chambres dont deux sont louées est comptée vacante, et n'est relouée qu'avec sa dernière chambre. Comparer ce taux à celui d'un studio, qui n'a qu'une place, compare des unités différentes ; mesurée par chambre, l'occupation des colocations serait plus élevée et leur délai de relocation plus court ;
- **elles sont le meilleur produit de l'été** : 78 % d'occupation en juillet et août 2025, le taux le plus élevé des trois types, avec 70 % de séjours courts, surtout des groupes. Les transformer en studios ferait perdre une partie de ces séjours, qui relèvent des 8 M€ de services et de séjours courts ;
- **le canal explique une partie de la difficulté** : 30 % seulement des colocations sont réservées sur le portail, qui ne vend pas les chambres une à une.

Conclusion : retenir le chiffre qui conforte une conviction, sans examiner la composition ni l'unité de mesure, relève du **biais de confirmation** (F08 § 5). Avant toute transformation, il faut mesurer l'occupation des colocations par chambre, à périmètre constant et par saison, dans l'entrepôt, et d'abord ouvrir la réservation des chambres sur le portail.

*2.2 c) – Le texte des demandes d'intervention*

**Deux apports** parmi les suivants (0,5 pt) :
- **des catégories fiables, quelle que soit la langue** : 40 % des 30 000 demandes de l'application sont classées « autre » et une sur quatre est mal classée, un tiers ne sont pas rédigées en français. Aujourd'hui, aucune statistique par catégorie n'a de sens ;
- **les problèmes récurrents, par résidence** : regrouper les demandes semblables fait apparaître la panne qui revient (le chauffe-eau qui donne vingt demandes, l'eau froide le matin chez plusieurs voisins, la coupure du réseau chaque soir, la moisissure qui revient chaque hiver) ;
- **des interventions mieux ciblées** : traiter la cause une fois (remplacer les chauffe-eau d'une résidence) au lieu d'envoyer vingt fois un plombier, prioriser les résidences, réduire une partie des 2 M€ d'interventions extérieures, et améliorer la satisfaction des résidents ;
- **un enrichissement de l'entrepôt** : le nombre de demandes par logement, déjà prévu, pourrait être analysé par catégorie.

**La méthode d'analyse** (0,5 pt) : l'**analyse descriptive** résume ce qui s'est passé (nombre de demandes par catégorie, par résidence, par mois) ; elle ne devient possible qu'une fois les demandes bien classées. L'**analyse exploratoire** cherche des motifs que l'on ne connaissait pas d'avance, dans des données non structurées : regroupements de demandes semblables, problèmes récurrents, croisements par résidence, par saison ou par type de logement (fouille de textes) (F08 § 2). C'est elle qui est surtout mobilisée ici, puisque personne ne sait quelles pannes reviennent. Le service de l'équipe données repose sur l'**apprentissage automatique** (il apprend, à partir de 3 000 demandes classées à la main, à classer les suivantes), à distinguer de l'IA générative (F13) ; il ne fait aucune prévision, et il n'est demandé ni de le construire ni de le régler.

**Deux précautions** parmi (0,5 pt) :
- **la minimisation des données transmises** : certaines demandes contiennent un nom, un numéro de téléphone ou un problème de santé (« je suis asthmatique »), donnée soumise à des règles plus strictes (annexe 2.6). Avant l'envoi à l'éditeur, masquer ces mentions et ne transmettre que ce qui sert au classement (texte nettoyé, résidence), pour la seule finalité d'amélioration de la maintenance ;
- **l'encadrement de l'éditeur, sous-traitant** : contrat qui limite l'usage des textes à cette finalité, interdit leur réutilisation, fixe la localisation et une durée de conservation plus courte que douze mois ; avis du délégué à la protection des données et mention du traitement au registre des traitements ;
- **le contrôle de la qualité du classement** : les 3 000 demandes d'apprentissage doivent être bien reclassées (une sur quatre l'est mal aujourd'hui) ; vérifier le classement par langue, les langues rares étant moins bien représentées ; garder la validation du responsable de résidence pour les décisions d'intervention, et revoir la liste des huit catégories avec les équipes techniques ;
- **la finalité et la gouvernance** : n'utiliser les demandes ni pour juger les résidents ni pour évaluer les agents ; désigner la direction des résidences comme propriétaire des données.

**Réponses tolérées**
- Chaîne présentée selon les étapes de l'informatique décisionnelle (collecte, extraction-transformation-chargement, entrepôt, restitution), si une limite corrigée est rattachée à chaque étape.
- Chacune des trois limites et l'écart des directions rattachés à une autre étape que celles du corrigé, si le rattachement est justifié.
- Estimation de tête de l'occupation des colocations hors Rennes (environ 87 à 88 % en 2026, en supposant les studios de Rennes presque pleins depuis l'ouverture) ou de l'effet de Rennes sur l'ensemble : non exigée ; la lecture qualitative suffit.
- Autres constats tirés de l'annexe 2.2 (stabilité de Lyon et de Montpellier, délai de relocation des deux pièces), s'ils sont chiffrés et interprétés.
- Analyse diagnostique présentée comme une variante de l'analyse exploratoire.
- Autres précautions justifiées (pilote sur quelques résidences avant la généralisation, mesure du gain sur les interventions).

**Erreurs fréquentes**
- *Corrélation ou composition ignorée* (`ET-26`) — baisse des colocations attribuée au produit sans examiner Rennes, l'unité de mesure et la saison.
- *Prudence d'interprétation oubliée* (`JUR-D06`) — baisse de 94 % à 91 % lue comme une dégradation de l'activité.
- *Analyse prédictive invoquée à tort* — l'outil présenté comme une prévision des pannes ; ou description de son fonctionnement interne (algorithme, paramètres), hors attente (`JUR-T07`) ; confusion entre IA générative et apprentissage automatique (`ET-09`).
- *Informatique décisionnelle réduite à un outil* (`ET-05`, `JUR-D02`) — « l'outil décisionnel corrigera les chiffres », sans règles écrites ni collecte des bonnes informations.
- *Précautions génériques* (`JUR-T01`) — « respecter le RGPD » sans dire quelles données masquer, pourquoi, ni comment encadrer l'éditeur.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement, analyses descriptive et exploratoire, biais de confirmation, effet de composition | définitions et méthode | F08 § 1, 2 et 5 | notion de cours |
| Apprentissage automatique et IA générative distingués | définitions | F13 ; F08 § 2 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) : finalité, minimisation, conservation limitée, sous-traitant | principes donnés en annexe 2.6 | `rgpd` / F15 | applicable depuis le 25/05/2018 |

---

### 2.3 – Le retour sur investissement du projet d'entrepôt (3 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI » ; `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI […] des indicateurs et des leviers d'optimisation via des tableaux de bord ». Limites : total de tête en sommes rondes ; aucun calcul actualisé ; recul critique sur les indicateurs.

**Annexes mobilisées** : annexe 2.4 (coûts, gains annoncés, avis du membre du directoire chargé des finances) ; annexes 2.1 et 2.2 (temps de production du tableau, effets de mesure) ; présentation (remplacement du logiciel de gestion locative avant la rentrée 2028, objectif de 95 %).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Retour sur investissement défini (formule, horizon, délai de récupération ; gains financiers et non financiers ; sans actualisation) | 0,5 |
| a-2 | Calcul de tête : 720 k€ par an, 2 160 k€ sur trois ans ; coût de 600 k€ ; retour annoncé de 260 % | 0,5 |
| b-1 | Attribution discutée et réponse à M. LORMIÈRE : l'entrepôt éclaire des décisions ; autres facteurs ; effet de mesure ; entrepôt en service en 2028 ; redevances et résultat | 0,5 |
| b-2 | Deux coûts cachés tirés du cas | 0,5 |
| c-1 | Premier indicateur de suivi des bénéfices, à cinq champs | 0,5 |
| c-2 | Second indicateur à cinq champs | 0,5 |

**Réponse attendue**

*2.3 a) – Le retour sur investissement annoncé*

**Définition** (0,5 pt) : le **retour sur investissement** d'un projet de système d'information rapporte le gain net qu'il procure à son coût, sur un horizon donné : (gains cumulés − coût total) / coût total. Il se complète du **délai de récupération** (coût / gain annuel). C'est un indicateur simple, sans actualisation ; il suppose des gains mesurables, réellement attribuables au projet, et il ne dit rien des bénéfices non financiers (qualité des décisions, fin des chiffres contradictoires), qui doivent être exposés à côté (F09 § 3.3).

**Le calcul de tête** (0,5 pt) :
- gain annoncé : un point d'occupation sur 9 000 logements = 90 logements ; 90 × 8 k€ = **720 k€ par an**, soit **2 160 k€ sur trois ans** ;
- coût sur trois ans : 300 + 3 × (40 + 60) = 300 + 300 = **600 k€** ;
- retour annoncé : (2 160 − 600) / 600 = 1 560 / 600 = **260 %** ; le gain d'une année (720 k€) dépasse le coût des trois ans, ce que dit la note.

*2.3 b) – Un calcul à apprécier*

**L'attribution du point d'occupation** (0,5 pt). M. LORMIÈRE a raison sur le principe : un entrepôt ne loue aucun logement. Il éclaire des décisions (offre de l'été, vente des chambres de colocation sur le portail, travaux hors de la rentrée), et ce sont ces décisions, avec les prix, les équipes commerciales, les ouvertures de résidences et le marché, qui font l'occupation. Le calcul appelle quatre réserves :
- **le gain est attribué sans référence ni mesure** : il faudrait une situation de départ mesurée selon les mêmes règles, des décisions identifiées qui s'appuient sur l'entrepôt, et le suivi de leur effet ;
- **une partie du point peut n'être qu'un effet de mesure** : avec les règles de l'entrepôt (jours ouverts, chambres), l'occupation mesurée de 2026 remonterait de 91 % vers 94 à 95 % sans un logement loué de plus (question 2.2). Le risque est de compter comme gain la correction d'un chiffre ;
- **le calendrier** : l'entrepôt est construit en 2027 et mis en service en janvier 2028 ; compter un gain dès 2027 est impossible. Sur 2028 et 2029 seulement, le gain annoncé serait de 2 × 720 = 1 440 k€, soit un retour de (1 440 − 600) / 600 = 140 % ;
- **des redevances ne sont pas un résultat** : 720 k€ de redevances supplémentaires portent des charges (énergie, ménage, entretien, accueil) ; le gain se mesure en marge.

Réponse à M. LORMIÈRE : l'entrepôt n'est pas rentable par lui-même ; il se justifie par la fiabilité des chiffres, le temps libéré et les décisions qu'il rend possibles. Le directoire doit l'approuver sur un dossier qui sépare gains mesurables et bénéfices qualitatifs, avec des indicateurs de suivi et un responsable des bénéfices.

**Deux coûts cachés** parmi (0,5 pt) :
- **la reconstruction des chargements** : l'entrepôt est alimenté par le logiciel de gestion locative actuel, qui doit être remplacé avant la rentrée 2028, quelques mois après la mise en service de l'entrepôt : les chargements et les règles de rapprochement seront à refaire ;
- **le temps des directions** : ateliers de définition des indicateurs, recette, formation des utilisateurs, non comptés (annexe 2.4 B) ;
- **la reprise et le nettoyage de l'historique** : tableurs aux colonnes changeantes, numéros de logement différents selon les applications (annexe 2.1 A) ; créer le numéro unique commun (RG1) est un chantier à part entière ;
- **la gouvernance des données** : propriétaires des indicateurs, dictionnaire, contrôles de qualité, dans la durée ;
- **la croissance de l'abonnement** avec le nombre d'utilisateurs et un parc porté à 12 000 logements.

Le temps libéré des deux personnes (huit jours-personne par mois) n'est un gain financier que s'il est redéployé ; sinon, c'est un bénéfice qualitatif.

*2.3 c) – Deux indicateurs de suivi des bénéfices*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Temps de production des indicateurs d'occupation | nombre de jours-personne consacrés chaque mois à produire et rapprocher les indicateurs d'occupation | relevé des temps de la direction commerciale et de l'équipe données | mensuelle | au plus un jour-personne par mois au second semestre 2028 (huit aujourd'hui) | processus |
| Taux d'occupation à périmètre constant | jours-places occupés / jours-places ouverts × 100, pour les résidences ouvertes depuis plus d'un an | entrepôt des séjours (table des faits Occupation_mensuelle) | mensuelle, bilan annuel présenté au directoire | au moins 95 % en 2030 (objectif d'« ORVANELLE 2030 »), avec une référence 2026-2027 recalculée selon les règles de l'entrepôt | financier |

Le second indicateur n'attribue pas à lui seul le gain à l'entrepôt : il se lit avec le registre des décisions prises à partir de l'entrepôt et de leur effet (par exemple, l'occupation de l'été des colocations après l'ouverture de la réservation par chambre).

**Réponses tolérées**
- Délai de récupération calculé (600 / 720, moins d'un an) à la place ou en plus du retour en pourcentage.
- Gain calculé avec 8 160 € par logement (680 € × 12), soit environ 734 k€ par an, si l'arrondi de l'énoncé est signalé.
- Autres coûts cachés justifiés par le cas (conduite du changement, dépendance à l'éditeur de l'outil décisionnel, réversibilité).
- Autres indicateurs à cinq champs : taux d'utilisation de l'outil décisionnel par les directions (axe apprentissage), part des indicateurs du directoire documentés dans le dictionnaire, occupation des chambres de colocation en été.

**Erreurs fréquentes**
- *Calcul hors attente* (`JUR-T07`) — calcul financier élaboré, alors que la question demande un total de tête en sommes rondes.
- *Retour sur investissement et coût total confondus* (`ET-33`) — ou coûts récurrents oubliés dans le coût.
- *Gain repris sans examen* (`JUR-T03`) — chiffre de la direction des systèmes d'information accepté tel quel, sans attribution, calendrier ni distinction entre redevance et marge.
- *Indicateur incomplet ou générique* (`ET-18`) — indicateur sans formule, source, fréquence, cible ou axe, ou sans lien avec les bénéfices annoncés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Retour sur investissement, délai de récupération, coûts cachés | définitions et méthode | F09 § 2 et 3.3 | notion de cours |
| Indicateur à cinq champs, axes du tableau de bord | méthode | F08 § 3 ; F09 § 4 | notion de cours |

---

### 2.4 – Les attestations de logement et la chaîne de blocs (2,5 points)

**Référence au programme**
- §3.3 – Appréhender les usages et les enjeux des technologies de la blockchain et des cryptoactifs : `3.3.b` « Fonctionnement des technologies de registres distribués (DLT) » ; `3.3.c` « Typologie des applications : traçabilité, certification, finance décentralisée, NFT » ; `3.3.a` « Évaluer les opportunités, les risques et le cadre réglementaire […] » ; `3.3.d` « Cadres réglementaires émergents : règlement MiCA (Markets in Crypto-Assets), NEP, normes ISO ». Limites : aucun développement de chaîne de blocs ni de contrat intelligent ; effets énergétiques intégrés ; aucune analyse juridique.

**Annexes mobilisées** : annexe 2.5 (constats, proposition d'ANCRALYS, alternative de la direction des systèmes d'information) ; annexe 2.6 (MiCA, ISO 22739, eIDAS, RGPD) ; annexe 1.1 (un quart de résidents venus de l'étranger).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fonctionnement d'une chaîne de blocs publique : registre répliqué entre nœuds, blocs chaînés par empreintes, consensus (preuve d'enjeu), ouverte à tous, inaltérabilité pratique ; distincte d'une base distribuée | 0,5 |
| a-2 | Empreinte d'un document : preuve d'existence à une date et d'intégrité, ni de l'auteur ni de la véracité ; proposition classée dans la certification de documents | 0,5 |
| b-1 | Deux apports et deux limites de la proposition face au cachet électronique, appliqués aux constats | 0,5 |
| b-2 | Recommandation justifiée (critères de pertinence d'une chaîne de blocs), refus de l'option nominative | 0,5 |
| c-1 | MiCA ne s'applique pas à ORVANELLE : ni émission, ni offre, ni détention, ni service sur crypto-actifs ; frais payés par le prestataire | 0,5 |

**Réponse attendue**

*2.4 a) – Chaîne de blocs publique, empreinte et typologie*

**Le fonctionnement** (0,5 pt) : une **chaîne de blocs** est un registre de transactions **répliqué** entre de nombreux **nœuds**, sans administrateur central. Les transactions sont regroupées en **blocs**, chacun contenant l'**empreinte** du bloc précédent : modifier un bloc passé changerait toutes les empreintes suivantes et serait rejeté par les autres nœuds (**inaltérabilité pratique**, et non absolue). Les nouveaux blocs sont validés selon une règle de **consensus** : ici, la **preuve d'enjeu**, où les validateurs sont choisis selon les crypto-actifs qu'ils immobilisent, bien moins consommatrice d'énergie que la preuve de travail. Une chaîne **publique** est ouverte à tous en lecture et en écriture ; chaque transaction est signée par la clé privée de son émetteur et donne lieu à des frais, payés en crypto-actifs. Elle organise la confiance entre des acteurs qui ne se connaissent pas ; ce n'est pas une base de données distribuée, administrée par un seul acteur qui peut en modifier le contenu (F11 § 1 ; vocabulaire de l'ISO 22739:2024).

**L'empreinte et la typologie** (0,5 pt) : l'**empreinte** (hachage) est une suite de taille fixe calculée à partir d'un document par une fonction à sens unique : la moindre modification du document change l'empreinte, et l'on ne peut pas reconstituer le document à partir d'elle. Inscrire l'empreinte dans une transaction prouve que le document existait à la date du bloc (**horodatage**) et qu'il n'a pas été modifié depuis (**intégrité**) ; le document lui-même n'est pas inscrit. Elle ne prouve ni l'auteur du document, ni la vérité de son contenu : une attestation erronée, une fois inscrite, est « certifiée » erronée (limite de l'« oracle »). La proposition d'ANCRALYS relève de la **certification de documents** (horodatage et preuve d'intégrité), et non de la traçabilité d'une filière, des jetons non fongibles ou de la finance décentralisée (F11 § 2.1).

*2.4 b) – La proposition d'ANCRALYS face au cachet électronique*

**Deux apports et deux limites** (0,5 pt), à choisir dans le tableau suivant. Apports possibles : détection d'un document modifié ou jamais émis ; preuve qui survit au prestataire ; aucune donnée personnelle si seule l'empreinte est inscrite. Limites possibles : émetteur non identifié ; retrait impossible ; vérification peu commode pour les destinataires ; option nominative contraire à la minimisation ; frais en crypto-actifs et énergie.

| Critère | Proposition d'ANCRALYS | Cachet électronique qualifié et page de vérification d'ORVANELLE |
|---|---|---|
| Falsifications | détecte un document modifié ou jamais émis (aucune empreinte inscrite) | détecte un document modifié ou jamais émis ; le cachet identifie l'émetteur |
| Identité de l'émetteur | la transaction est signée par ANCRALYS : la preuve dit qu'ANCRALYS a inscrit une empreinte, et l'organisme doit faire confiance à la page d'ANCRALYS, qu'un faussaire peut imiter par un faux code | le certificat qualifié atteste que le document émane d'ORVANELLE, personne morale ; la page de vérification est sur le site d'ORVANELLE |
| Attestation devenue fausse (départ anticipé) | impossible à retirer : l'inscription est définitive | la page indique que l'attestation n'est plus valable |
| Usage par les destinataires | déposer le PDF sur une page inconnue des banques et des consulats | tout lecteur de PDF courant affiche le cachet ; cadre de confiance européen (eIDAS) |
| Durée de la preuve | l'empreinte reste dans la chaîne même si ANCRALYS disparaît, mais la page de vérification disparaît avec elle | dépend du certificat et du service d'ORVANELLE, à maintenir |
| Données personnelles | sans risque si seule l'empreinte est inscrite ; l'option « nom et adresse en clair » est contraire à la minimisation et impossible à effacer | aucune donnée inscrite hors d'ORVANELLE |
| Coût et énergie | environ 90 k€ sur trois ans ; frais en crypto-actifs et énergie de la chaîne, faible en preuve d'enjeu mais non nulle | environ 70 k€ sur trois ans |

La cause première des falsifications n'est pas l'absence de chaîne de blocs : ce sont des documents produits à partir d'un modèle de traitement de texte, avec une signature scannée, faciles à imiter. Les deux solutions supposent de produire les documents automatiquement à partir du logiciel de gestion locative.

**Recommandation** (0,5 pt) : retenir le **cachet électronique qualifié**, avec la page de vérification d'ORVANELLE, et refuser la proposition d'ANCRALYS, et en tout cas son option nominative. Les critères de pertinence d'une chaîne de blocs ne sont pas réunis (F11 § 2.2) : un seul acteur, ORVANELLE, écrit les attestations, sans besoin d'un registre partagé entre des acteurs qui ne se font pas confiance ; un tiers de confiance reconnu existe (prestataire de services de confiance qualifié) ; il faut identifier l'émetteur et pouvoir retirer une attestation, ce que la chaîne ne fait pas. Le cachet répond aux 40 falsifications signalées et réduit les 1 500 demandes de confirmation et leurs deux jours de délai, puisque l'organisme vérifie seul. ORVANELLE informe les banques, les consulats et les établissements de la façon de vérifier, et ajoute au besoin un horodatage électronique qualifié.

*2.4 c) – MiCA et le projet*

**Non** (0,5 pt) : d'après l'annexe 2.6, MiCA encadre l'offre au public et l'admission à la négociation de crypto-actifs, l'émission de jetons qui visent une valeur stable et l'agrément des prestataires de services sur crypto-actifs (PSCA). Dans ce projet, ORVANELLE n'émet ni n'offre de crypto-actifs, n'en détient aucun et ne rend aucun service sur crypto-actifs : elle achète en euros un service d'horodatage. Les frais de transaction en crypto-actifs sont payés par ANCRALYS, pour son propre compte. Le règlement ne régit pas non plus la certification de documents, et l'ISO 22739 n'est qu'un vocabulaire. Si ORVANELLE achetait un jour elle-même des crypto-actifs pour payer ces frais, le prestataire qui les lui fournirait ou les conserverait devrait être un PSCA agréé : depuis le 02/07/2026, un ancien PSAN ne peut plus exercer sans agrément (annexe 2.6).

**Réponses tolérées**
- Proposition d'ANCRALYS retenue en complément du cachet (horodatage indépendant d'ORVANELLE), si l'identification de l'émetteur et le retrait des attestations sont assurés par le cachet et la page de vérification, et si l'option nominative est refusée.
- Proposition rattachée à l'« horodatage » ou à la « preuve d'antériorité », formes de la certification.
- Réponse à c) qui s'interroge sur la situation d'ANCRALYS au regard de MiCA, si la réponse pour ORVANELLE est donnée ; aucune analyse juridique n'est attendue.
- Signature électronique de la personne habilitée au lieu du cachet, si le candidat signale qu'elle engage une personne physique et non ORVANELLE.

**Erreurs fréquentes**
- *Chaîne de blocs confondue avec une base de données distribuée* (`ET-08`) — ou présentée comme inaltérable sans nuance.
- *Empreinte confondue avec le chiffrement ou avec le document* — croire que le document est stocké dans la chaîne, ou que l'empreinte prouve l'auteur et la vérité du contenu.
- *Opportunités sans risques* (`ET-19`) — chaîne de blocs recommandée parce qu'elle est « infalsifiable », sans examiner l'émetteur, le retrait, les destinataires et les données personnelles.
- *MiCA mal situé* (`ET-35`) — MiCA présenté comme applicable à toute utilisation d'une chaîne de blocs, ou comme un cadre de la certification de documents ; ISO 22739 présentée comme une norme d'exigences.
- *Analyse juridique hors attente* (`JUR-T07`) — valeur probante des documents développée comme un juriste.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Règlement (UE) 2023/1114 (MiCA) | objet : offre au public, jetons visant une valeur stable, PSCA ; fin des anciens PSAN au 02/07/2026 | `mica` / F11 § 3.1 | applicable depuis le 30/12/2024 |
| ISO 22739:2024 | vocabulaire des chaînes de blocs et des registres distribués | `iso_22739_2024` / F11 § 3.4 | en vigueur (2e édition) |
| Règlement (UE) n° 910/2014 (eIDAS), révisé par le règlement (UE) 2024/1183 | services de confiance : cachet électronique, horodatage, registres électroniques | `eidas_910_2014`, `eidas2` / F06 § 5 ; F11 § 3.4 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | minimisation ; données inscrites dans une chaîne de blocs impossibles à effacer | `rgpd` / F11 § 2.3 ; F15 | applicable depuis le 25/05/2018 |
| Chaîne de blocs publique, consensus, empreinte, critères de pertinence, typologie des applications | définitions et méthode | F11 § 1 et 2 ; glossaire (hachage, cachet électronique) | notion de cours |

---

## DOSSIER 3 – SÉCURISER LA CAMPAGNE DE RENTRÉE, AUDITER LE TRAITEMENT DES CANDIDATURES ET PILOTER L'ÉNERGIE DES RÉSIDENCES (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les risques de la rentrée et l'analyse d'impact | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers | 4 |
| 3.2 La continuité et la sécurité de la rentrée 2027 | `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.d` Dispositifs de surveillance et de résilience : IAM, PCA/PRA (plans de continuité et de reprise d'activité) | 3 |
| 3.3 L'audit du traitement des dossiers de candidature | `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ; `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. | 3 |
| 3.4 Le pilotage de l'énergie des résidences | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 3 |
| **Dossier 3 – Sécuriser la campagne de rentrée, auditer le traitement des candidatures et piloter l'énergie des résidences** |  | **13** |

Répartition indicative : connaissances (typologie des risques, analyse d'impact sur l'activité, PCA et PRA, audit de conformité, Green IT et IT for green) environ 2,5 points (items 3.1 a-1, 3.1 b-1, 3.2 a-1, 3.3 a-1 et 3.4 a-1) ; analyse des annexes et recommandations environ 10,5 points, soit environ 80 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – Les risques de la rentrée et l'analyse d'impact (4 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; l'impact sur les états financiers n'est pas demandé ici.

**Annexes mobilisées** : annexe 3.1 (événements de la rentrée 2026, points de vue, échelles), annexe 3.2 (six processus selon la période, dispositif actuel), annexe 3.5 (ISO/IEC 27005:2022, ISO 22301:2019) et annexe 1.1 (7 000 baux dont 70 % de juin à septembre, clé virtuelle dans 22 résidences, badges dans 38, portail relié au logiciel de gestion locative par des échanges de fichiers chaque nuit).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers), avec les critères touchés (confidentialité, intégrité, disponibilité, traçabilité) | 0,5 |
| a-2 | Cinq risques formulés comme des événements redoutés, tirés de l'annexe 3.1, avec leur cause | 0,5 |
| a-3 | Cinq risques classés dans la typologie, le classement justifié | 0,5 |
| b-1 | Analyse d'impact sur l'activité définie (conséquences d'une interruption dans le temps, dépendances, processus critiques, durées admissibles) | 0,5 |
| b-2 | Impact d'une interruption de trois processus, dont la remise des accès, apprécié selon la période, avec les dépendances (bail et dépôt de garantie avant les accès, logiciel de gestion locative) | 0,5 |
| b-3 | Processus critiques et durée maximale d'interruption admissible de chacun, justifiées et différenciées selon la période | 0,5 |
| c-1 | Cinq risques cotés selon les échelles de l'annexe 3.1 C et deux priorités justifiées par la probabilité et l'impact | 0,5 |
| c-2 | Une option de traitement et une mesure pour chacune des deux priorités ; réponse à M. CALVÉRAC | 0,5 |

**Réponse attendue**

*3.1 a) – La typologie et les cinq risques*

**Typologie** (a-1) : les risques liés aux systèmes d'information se classent en quatre familles (F12 § 0 et § 5) :
- les **cybermenaces**, actes malveillants : hameçonnage et usurpation d'identité, compromission de comptes, rançongiciel, attaque par un fournisseur ;
- les **défaillances opérationnelles**, non intentionnelles : panne, saturation, erreur humaine, défaillance d'un prestataire, incohérence des données entre applications ;
- les **risques réglementaires** : manquement à une obligation, ici les principes de protection des données personnelles ;
- les **risques métiers** : effets sur l'activité et la stratégie (candidats perdus, taux d'occupation, image, sécurité des résidents).

Chaque risque porte atteinte à un ou plusieurs critères : confidentialité, intégrité, disponibilité, traçabilité. Une même cause peut relever de plusieurs familles ; le classement retient la famille de la cause et signale l'effet métier.

**Six risques révélés par l'annexe 3.1** (a-2 et a-3 ; cinq sont attendus) :

| Risque (événement redouté) et cause | Famille | Critère touché |
|---|---|---|
| R1 – Des fraudeurs se font passer pour ORVANELLE et détournent les dépôts de garantie des familles : le lien de paiement est envoyé par courriel, et les fraudeurs connaissent le nom des candidats et leur résidence | cybermenace (hameçonnage, usurpation d'identité) ; effet métier : image, presse | intégrité de la relation de paiement, confiance |
| R2 – Un tiers prend la main sur le compte d'un résident et ouvre la porte de son logement avec la clé virtuelle : identifiants réutilisés, mot de passe seul | cybermenace (compromission de comptes) ; effet sur la sécurité des personnes et violation de données | confidentialité, intégrité ; sécurité physique |
| R3 – Le service de clé virtuelle est indisponible un jour d'arrivées et les résidents ne peuvent pas entrer : prestataire sans assistance le week-end ni engagement de rétablissement, aucune clé de secours à l'accueil | défaillance opérationnelle (dépendance à un prestataire) ; effet métier | disponibilité |
| R4 – Le portail sature à l'ouverture des réservations et des candidats partent chez des concurrents : 8 000 connexions pour une capacité de 1 500 | défaillance opérationnelle (capacité) ; risque métier (occupation, image) | disponibilité |
| R5 – Les pièces justificatives de milliers de candidats et de garants, conservées sans limite dans les messageries, sont consultées par un tiers : 1,5 million de pièces jointes, comptes de 40 saisonniers restés ouverts | risque réglementaire (minimisation, conservation, sécurité) et cybermenace | confidentialité |
| R6 – Un logement est promis à deux candidats : portail et logiciel de gestion locative synchronisés une fois par nuit | défaillance opérationnelle (intégrité des données entre deux applications) ; effet métier | intégrité |

*3.1 b) – L'analyse d'impact sur l'activité*

**Définition** (b-1) : l'**analyse d'impact sur l'activité** (BIA) mesure, pour chaque processus, les conséquences d'une interruption selon sa durée (résidents et candidats touchés, pertes, image, sécurité, obligations) et selon la période. Elle recense ses dépendances (applications, prestataires, personnes) et en déduit les processus critiques, leur **durée maximale d'interruption admissible** (RTO) et leur **perte de données maximale admissible** (RPO). Elle fonde le plan de continuité ; ISO 22301:2019 en fait la première étape (F12 § 4 ; annexe 3.5). Chez ORVANELLE, la criticité dépend de la **saison** : 70 % des baux sont signés de juin à septembre, et environ 2 000 arrivées se concentrent sur quatre samedis.

**Impact d'une interruption de trois processus selon la période** (b-2 et b-3) :

| Processus | De juin à septembre | D'octobre à mai | Critique ? | Durée maximale d'interruption admissible |
|---|---|---|---|---|
| Remise des accès (clé virtuelle, 22 résidences) | environ 2 000 arrivées sur quatre samedis, jusqu'à 40 dans une résidence le même jour ; au-delà d'une heure, la file se forme dans le hall avec les bagages, l'accueil ferme à 19 h et chaque résident qui ne peut pas entrer est hébergé aux frais d'ORVANELLE ; sécurité et image en jeu (annexe 3.1 : 120 résidents bloqués six heures, 30 nuits d'hôtel). Dépendances : service en ligne du prestataire, bail signé et dépôt payé | 2 100 arrivées étalées, surtout en semaine, accueil présent : on peut faire patienter le résident ou reporter son arrivée | **critique** en rentrée | **une heure** les jours d'arrivée de la rentrée ; une demi-journée les autres jours de l'été ; une journée d'octobre à mai. Les 38 résidences à badges, programmés sur un poste local, ne dépendent pas du service en ligne |
| Réservation (portail) | 24 000 candidatures ; le jour de l'ouverture, 8 000 connexions en une heure ; un candidat bloqué se tourne vers une autre offre **dans la journée**, au détriment de l'objectif de 95 % d'occupation | 6 000 candidatures ; le candidat réessaie le lendemain | **critique** de juin à septembre, surtout le jour de l'ouverture | **quelques heures** le jour de l'ouverture, une demi-journée le reste de l'été ; un à deux jours le reste de l'année |
| Signature du bail | en moyenne 40 baux par jour, jusqu'à 80 fin août ; le logement n'est réservé que 48 heures : au-delà, il est proposé à un autre candidat (risque de perdre le résident ou de créer une double attribution) ; sans bail, pas d'accès. Dépendances : prestataire de signature, logiciel de gestion locative pour préparer le bail | une dizaine par jour ; un report de deux jours est sans dommage | **critique** en rentrée | **24 heures** en rentrée, pour garder une marge sur les 48 heures de réservation ; deux à trois jours le reste de l'année |

Pour comparaison : l'**encaissement du dépôt de garantie** devient critique par dépendance, puisque les accès ne sont remis qu'après paiement (24 heures en rentrée) ; le **contrôle des pièces** supporte deux à trois jours de retard, rattrapés au prix d'heures supplémentaires ; l'**état des lieux**, déjà fait sur papier et saisi plus tard, n'est pas critique. Les processus critiques dépendent tous du **logiciel de gestion locative**, pour l'attribution, la préparation du bail et le rapprochement des dépôts. Or son hébergeur ne s'engage à intervenir que « dans le jour ouvré suivant », et ses sauvegardes n'ont jamais été restaurées. Cet écart avec des durées admissibles de quelques heures en rentrée fonde le dispositif de la question 3.2.

*3.1 c) – La cotation, les deux priorités et leur traitement*

**Cotation selon les échelles de l'annexe 3.1 C** (c-1) :

| Risque | Probabilité | Impact | Criticité |
|---|---|---|---|
| R2 – Compte pris en main, porte ouverte | 4 : 200 comptes en deux mois, mot de passe seul, toujours le cas | 4 : la clé virtuelle de 15 comptes ouvrait un logement, la sécurité des résidents est en cause ; intrusion impossible à exclure (journaux de sept jours) | **16** |
| R1 – Fraude au dépôt de garantie | 4 : 50 familles en deux mois, facile à provoquer, le lien de paiement part toujours par courriel | 3 : environ 35 k€, 400 appels et courriels, écho dans la presse régionale | **12** |
| R3 – Clé virtuelle indisponible un jour d'arrivées | 3 : survenu le 5 septembre, aucun engagement ni assistance le week-end | 3 : un samedi de pointe (environ 500 arrivées), une panne d'une journée entière dans les 22 résidences équipées toucherait de l'ordre de 200 résidents, et les arrivées de la journée seraient bloquées jusqu'au soir | 9 |
| R4 – Portail saturé à l'ouverture | 3 : survenu, capacité inchangée | 3 : 8 000 candidats touchés, 1 800 appels sans réponse (60 %) | 9 |
| R5 – Pièces des messageries consultées par un tiers | 2 : aucune fuite établie, mais plausible (origine des informations des fraudeurs inconnue, comptes de saisonniers ouverts) | 4 : données de milliers de candidats et de garants | 8 |
| R6 – Logement promis à deux candidats | 4 : 150 fois en un été, la synchronisation reste nocturne | 2 : 150 candidats touchés, relogés, sans écho public | 8 |

**Deux priorités** : **R2 (16)** et **R1 (12)**, les seules qui atteignent le seuil de 12 fixé par le directoire. R2 vient en premier : il touche la **sécurité physique** des résidents, ce que redoute Mme ROUSTAGNE (« une porte qui s'ouvre pour quelqu'un qui n'est pas le résident »). R1 vient ensuite : il se répète et il est facile à reproduire. R3 et R4 suivent (9) ; R3 est traité par le dispositif de continuité de la question 3.2.

**Options de traitement et mesures** (c-2) :
- **R2 – réduire** : exiger une **authentification à deux facteurs** pour tout compte de l'application qui porte une clé virtuelle ; réinitialiser les 200 comptes et réactiver les 15 clés après vérification de l'identité du résident ; prévenir le résident de toute connexion depuis un nouveau téléphone ; conserver les journaux des serrures plusieurs mois. L'option **éviter** peut compléter : lier la clé au seul téléphone enregistré à l'arrivée, et non au compte. **Transférer** est impossible : la sécurité des personnes ne se transfère pas. **Accepter** est exclu : la criticité est maximale.
- **R1 – réduire** : supprimer l'envoi du lien de paiement par courriel. Le dépôt de garantie ne se paie plus que dans l'espace personnel du candidat sur le portail, après connexion. Chaque message d'ORVANELLE et le portail rappellent qu'« ORVANELLE ne communique jamais de coordonnées bancaires par courriel ». Un numéro de contre-appel permet aux familles de vérifier une demande, et les familles sont alertées dès le premier signalement. Le traitement de R5 réduit aussi les fuites d'informations dont se servent les fraudeurs. Le **transfert** à un assureur ne couvrirait au mieux que des frais d'ORVANELLE, pas les pertes des familles.

**Réponse à M. CALVÉRAC** : la fraude n'est pas « l'affaire des familles ». Elle exploite une pratique d'ORVANELLE, le paiement demandé par courriel, et des informations sur ses candidats ; elle atteint sa réputation (écho dans la presse) et la confiance des familles au moment de la décision. **Accepter** ce risque est exclu : sa criticité de 12 atteint le seuil du directoire. La saturation du portail (9) est réelle et doit être traitée, mais après R2 et R1.

**Réponses tolérées**
- Autre typologie (risques internes et externes, accidentels et intentionnels ; ou classement par critère confidentialité, intégrité, disponibilité, traçabilité), si les quatre familles du programme apparaissent dans le classement.
- R5 coté 3 en probabilité (12), puisque l'origine des informations des fraudeurs est inconnue et que les comptes des saisonniers restent ouverts, et retenu comme deuxième priorité à la place de R1, si le choix est justifié ; R3 coté 2 en impact (6) d'après les seuls faits du 5 septembre.
- R3 coté 4 en impact (12), au titre de la sécurité des résidents laissés devant leur porte le soir, quand l'accueil ferme à 19 h (scénario de Mme ROUSTAGNE), et retenu comme deuxième priorité, si le choix est justifié.
- Autres processus analysés en b), comme l'encaissement du dépôt de garantie ou le contrôle des pièces, si la remise des accès y figure et si les durées sont différenciées selon la période ; durées voisines (deux heures pour la remise des accès un jour d'arrivée, 48 heures pour la signature) si elles sont justifiées.
- Démarche fondée sur ISO/IEC 27005:2022 (lignes directrices) ou EBIOS Risk Manager (méthode), si la nature du référentiel est juste.

**Erreurs fréquentes**
- *Typologie récitée sans application, ou risques réduits à des incidents passés* (`JUR-T01`, `JUR-T07`) — juste : des événements redoutés, avec leur cause, classés puis cotés selon les échelles de l'annexe.
- *Analyse d'impact sans la saison* (`JUR-T08`) — juste : la même panne est critique un samedi de septembre et presque indolore en février.
- *Durée maximale d'interruption et perte de données maximale confondues* (`ET-03`, `JUR-S02`) — juste : durée d'interruption (RTO) et perte de données (RPO) sont deux objectifs distincts.
- *Fraude laissée aux familles, comme le propose M. CALVÉRAC* — juste : le risque naît d'un processus d'ORVANELLE ; l'option « accepter » est exclue au-delà du seuil.
- *Droit du dépôt de garantie, du bail ou du logement* — non attendu.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI, critères CID et traçabilité | cybermenaces, défaillances, risques réglementaires et métiers | F12 § 0, § 1 et § 5 | notion de cours |
| Analyse d'impact sur l'activité, RTO, RPO | processus critiques, durées admissibles | F12 § 4 | notion de cours |
| ISO 22301:2019 | norme d'exigences de la continuité d'activité ; analyse d'impact | `iso_22301_2019` ; F12 § 4 | en vigueur |
| ISO/IEC 27005:2022 | lignes directrices de gestion des risques | `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager, version 1.5 (toléré) | méthode en cinq ateliers | `ebios_rm_1_5` ; F12 § 2 | en vigueur |

---

### 3.2 – La continuité et la sécurité de la rentrée 2027 (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ». Limites : la mise en œuvre technique des solutions de cybersécurité n'est pas exigée ; les normes se mobilisent sans entrer dans leur démarche de conformité formelle.

**Annexes mobilisées** : annexe 3.2 (processus, dispositif actuel, options du prestataire de la clé virtuelle), annexe 3.1 (panne du 5 septembre, comptes pris en main, fraude), annexe 3.5 (ISO 22301:2019, ISO/IEC 27001:2022, règlement sur la cyberrésilience) et annexe 1.1 (clé virtuelle, badges, dépenses du système d'information de 4,5 M€).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | PCA et PRA définis et distingués (maintenir en mode dégradé pendant la crise / restaurer et revenir à la normale) | 0,5 |
| a-2 | Mode dégradé de la remise des accès et de la signature des baux, tiré des annexes (activation la veille, clés de secours à l'accueil, liste des arrivées, réservation prolongée) | 0,5 |
| a-3 | Objectifs de durée maximale d'interruption et de perte de données admissibles, justifiés par l'analyse d'impact | 0,5 |
| a-4 | Engagement à obtenir du prestataire de la clé virtuelle et exercices avant la rentrée | 0,5 |
| b-1 | Trois mesures de sécurité, chacune reliée à un risque différent de la question 3.1, dont une contre la fraude au dépôt de garantie | 0,5 |
| b-2 | Hiérarchie et calendrier, rang de la première justifié | 0,5 |

**Réponse attendue**

*3.2 a) – Le dispositif de continuité de la rentrée*

**PCA et PRA** (a-1) : le **plan de continuité d'activité** (PCA) organise le **maintien** des processus critiques pendant la crise, au besoin en **mode dégradé** (procédures de secours, moyens de substitution, organisation de crise). Le **plan de reprise d'activité** (PRA) organise la **restauration** des systèmes et le **retour à la normale** après le sinistre (restauration des sauvegardes, rattrapage des opérations faites en mode dégradé). Les deux reposent sur l'analyse d'impact (question 3.1 b) et ne valent que s'ils sont exercés (F12 § 4). ORVANELLE n'a ni l'un ni l'autre.

**Mode dégradé** (a-2) :

| Processus | Mode dégradé proposé | Constat traité |
|---|---|---|
| Remise des accès | **activer les clés la veille de l'arrivée** (option du prestataire), chaque clé ne fonctionnant qu'à partir du jour prévu : une panne le jour même ne bloque plus les arrivées attendues ; l'état des lieux se fait à l'arrivée, comme aujourd'hui. Pendant la rentrée, placer les **clés mécaniques de secours** dans un coffre à l'accueil de chaque résidence équipée, et non plus dans le local des services techniques fermé le week-end ; les remettre contre signature sur un registre et les récupérer après le rétablissement. Imprimer chaque soir la **liste des arrivées du lendemain** (résident, logement, bail signé, dépôt payé), pour accueillir même si le logiciel de gestion locative ou l'application sont indisponibles. Prévoir une astreinte d'un responsable les samedis de rentrée, l'accueil prolongé les jours de pointe et quelques chambres d'hôtel réservées en dernier recours. Les 38 résidences à badges gardent un stock de badges | 120 résidents bloqués six heures ; aucune clé de secours ; clés activées seulement à l'arrivée |
| Signature du bail | si le prestataire de signature ou le logiciel de gestion locative est indisponible, **prolonger d'office la réservation** de 48 heures du logement et en prévenir le candidat, pour ne perdre ni le candidat ni le logement ; préparer les baux à partir de la liste des attributions extraite chaque soir ; signer dès le rétablissement, en priorité ceux des arrivées les plus proches | jusqu'à 80 baux par jour, logement réservé 48 heures |

**Objectifs de durée d'interruption (RTO) et de perte de données (RPO)** (a-3) :

| Ressource | RTO en rentrée | RTO d'octobre à mai | RPO | Justification |
|---|---|---|---|---|
| Service de clé virtuelle | une heure les jours d'arrivée, tenue grâce au mode dégradé | une journée | aucune perte des clés activées : sauvegarde de la liste des clés à exiger du prestataire (engagement ci-dessous) | analyse d'impact de la remise des accès |
| Signature électronique | 24 heures | deux à trois jours | aucun bail signé perdu : le prestataire conserve les baux | réservation de 48 heures |
| Logiciel de gestion locative | quatre heures | 24 heures | **une heure** en rentrée ; 24 heures hors rentrée, ce que la sauvegarde de la nuit permet | en rentrée, perdre une journée, ce sont jusqu'à 80 attributions et baux à reconstituer, et de nouvelles doubles attributions ; l'hébergeur ne s'engage aujourd'hui qu'au « jour ouvré suivant », ce qu'il faut renégocier pour la rentrée |

**Engagement à obtenir du prestataire de la clé virtuelle** (a-4) : souscrire l'**assistance sept jours sur sept de juin à octobre** avec un **rétablissement en deux heures au plus**. Environ 20 k€ par an représentent moins de 0,5 % des 4,5 M€ de dépenses du système d'information, pour le processus le plus sensible de la rentrée. Ces deux heures dépassent l'heure admissible : seul le mode dégradé (activation la veille, clés de secours) couvre l'écart. Le contrat doit aussi prévoir :
- l'information immédiate d'ORVANELLE en cas d'incident ;
- une disponibilité mesurée et communiquée, avec des pénalités ;
- le plan de continuité du prestataire et la sauvegarde de la liste des clés ;
- la conservation des journaux des serrures pendant plusieurs mois (risque R2) ;
- la fourniture de mises à jour de sécurité des serrures. Le règlement sur la cyberrésilience en fait une obligation des fabricants, en principe, avec une application générale le 11/12/2027 (annexe 3.5), ce qui facilite cette exigence d'achat ;
- un exercice commun chaque année avant la rentrée.

**Exercices** (a-4) :
- avant le 1er juin, **restaurer pour la première fois une sauvegarde** du logiciel de gestion locative chez l'hébergeur, et mesurer le temps réel de reprise (PRA) ;
- fin juin, puis avant le premier samedi de pointe (21 août), un **exercice « panne de la clé virtuelle un samedi »** dans deux ou trois résidences, avec les chargés d'accueil, saisonniers compris : coffre, registre, liste papier, astreinte, hôtel ;
- un exercice de prolongation des réservations quand la signature est indisponible ;
- après chaque exercice, un retour d'expérience et la mise à jour du plan.

Le plan est porté par le membre du directoire chargé des opérations, coordonné par la direction des systèmes d'information et appliqué par la direction des résidences (ISO 22301:2019 en principe).

*3.2 b) – Trois mesures de sécurité hiérarchisées pour la rentrée 2027*

1. **Authentification à deux facteurs pour les comptes de l'application qui portent une clé virtuelle**, avec réinitialisation des comptes compromis, alerte de connexion depuis un nouveau téléphone et journaux des serrures conservés plusieurs mois (risque R2) ; en service avant le premier samedi de pointe, le 21 août 2027. **Justification du premier rang** : criticité maximale (16) ; la clé ouvre un logement, la sécurité physique des résidents est en jeu, et la faille a déjà été exploitée 200 fois en deux mois ; la mesure protège aussi les données des résidents, objectif du plan « ORVANELLE 2030 ».
2. **Paiement du dépôt de garantie dans le seul espace personnel du portail**, rappel systématique qu'aucune coordonnée bancaire n'est envoyée par courriel, contre-appel possible et alerte des familles dès le premier signalement (risque R1) ; avant le 1er juin, puisque les fraudes ont eu lieu en juillet et en août.
3. **Fin de la circulation des pièces par courriel** : dépôt des pièces sur le portail, purge des messageries, fermeture des comptes des saisonniers à la fin de leur contrat et sensibilisation des équipes au hameçonnage (risque R5) ; elle réduit aussi les informations dont se servent les fraudeurs de R1, et l'audit de la question 3.3 en fixera les règles.

**Réponses tolérées**
- Fraude au dépôt de garantie placée au premier rang, au titre de sa fréquence, de son coût faible et de sa rapidité de mise en œuvre, si la mesure sur les comptes suit immédiatement.
- Troisième mesure portant sur la capacité du portail (file d'attente, ouverture des réservations étalée par ville) ou sur la double attribution (attribution validée en temps réel), si elle est reliée à son risque ; la capacité du portail ne relève pas d'un paramétrage attendu de la copie.
- RTO et RPO voisins, s'ils sont justifiés par l'analyse d'impact et différenciés selon la saison ; refus de l'option du prestataire, si l'écart est couvert par un mode dégradé explicite.
- Mention de la notification d'une violation de données pour les 200 comptes, en principe, sans délai ni analyse juridique.

**Erreurs fréquentes**
- *PCA et PRA confondus* (`ET-02`, `JUR-S02`) — juste : le PCA maintient pendant la crise, le PRA restaure ensuite.
- *RTO et RPO inversés ou fixés sans lien avec l'analyse d'impact* (`ET-03`) — juste : une heure pour les accès un samedi de rentrée, une heure de perte de données au plus pour les attributions en rentrée.
- *Plan jamais exercé* (F12 § 4) — juste : sauvegarde restaurée et exercice de panne avant la rentrée.
- *Mesures techniques détaillées, réglages ou tests techniques de sécurité* (`JUR-T12`) — juste : mesures organisationnelles, contractuelles et de gestion des accès.
- *Engagement du prestataire présenté comme suffisant* — juste : deux heures de rétablissement ne tiennent pas l'heure admissible sans mode dégradé, sauf si le candidat a retenu une durée admissible de deux heures et prévoit malgré tout un mode dégradé.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| PCA, PRA, RTO, RPO, exercices | maintien en mode dégradé, reprise, objectifs | F12 § 4 | notion de cours |
| ISO 22301:2019 | norme d'exigences de la continuité d'activité | `iso_22301_2019` ; F12 § 4 | en vigueur |
| ISO/IEC 27001:2022 | mesures de contrôle d'accès, de sauvegarde, de relations avec les fournisseurs | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Authentification à deux facteurs, gestion des identités | au moins deux facteurs de nature différente | F12 § 3 | notion de cours |
| Règlement (UE) 2024/2847 sur la cyberrésilience (CRA) | mises à jour de sécurité fournies par les fabricants ; application générale le 11/12/2027 | `cra` ; F12 § 7 | applicable le 11/12/2027 ; article 14 depuis le 11/09/2026 |

---

### 3.3 – L'audit du traitement des dossiers de candidature (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance » ; `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; le droit des données personnelles (droits des personnes, bases légales) relève de l'UE 1.

**Annexes mobilisées** : annexe 3.3 (traitement, liste des pièces, constats de la déléguée, demande du directoire), annexe 3.1 (pièces conservées dans les messageries, comptes des saisonniers), annexe 3.5 (RGPD en principe, ISO/IEC 27001:2022) et annexe 1.1 (logiciel de gestion locative, effectif des résidences, organigramme sans audit interne).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit de conformité d'un processus du SI défini (examen indépendant, référentiel, écarts, risques, recommandations) ; la distinction avec l'audit légal est un plus, non exigé | 0,5 |
| a-2 | Objectifs (conformité, sécurité, règles pour le nouveau logiciel) et périmètre (de la réception des pièces à leur suppression, messageries, logiciel, prestataire) | 0,5 |
| a-3 | Étapes, livrables et calendrier réaliste sur les six semaines, avant le 1er juin | 0,5 |
| a-4 | Preuves à demander, reliées aux constats | 0,5 |
| b-1 | Quatre critères de conformité et de sécurité, chacun précisé par ce qui est attendu | 0,5 |
| b-2 | Situation actuelle appréciée pour chacun à partir de l'annexe 3.3, avec le risque et la priorité | 0,5 |

**Réponse attendue**

*3.3 a) – Le cadrage de l'audit*

**Définition** (a-1) : l'**audit de conformité d'un processus du système d'information** est un examen indépendant et méthodique qui compare le fonctionnement réel du processus (pratiques, données, accès, prestataires, documentation) à un **référentiel** de règles (texte, norme, politique interne), relève les **écarts**, en apprécie les **risques** et formule des **recommandations** hiérarchisées (F10 § 1.1). Ici, c'est un audit externe contractuel commandé par le directoire. Son référentiel réunit les principes du RGPD (annexe 3.5), les règles internes et les mesures d'ISO/IEC 27001:2022 sur le contrôle d'accès et les fournisseurs. Il ne s'agit ni de l'audit légal des comptes, ni d'un audit de la performance commerciale.

**Objectifs** (a-2) :
- apprécier la **conformité** du traitement aux principes de minimisation, de limitation de la conservation, de sécurité, de tenue du registre et d'encadrement des sous-traitants ;
- apprécier la **sécurité** des dossiers, partout où ils se trouvent ;
- hiérarchiser les écarts et les risques ;
- proposer les **règles à intégrer au paramétrage** du nouveau logiciel de gestion locative en septembre 2027 (pièces demandées, profils d'accès, durées de conservation), et les mesures immédiates à prendre avant l'ouverture des réservations du 1er juin.

**Périmètre** (a-2) : le traitement des dossiers de candidature, de la réception des pièces à leur suppression :
- le portail, les messageries du centre de relation résidents et des chargés d'accueil, le logiciel de gestion locative (dossiers conservés depuis 2009) et la transmission au prestataire de vérification des garants ;
- les candidats et les garants, retenus ou non ;
- la campagne 2026 et le stock de dossiers ;
- les acteurs : centre de relation résidents, chargés d'accueil, direction commerciale et de la relation résidents, direction des systèmes d'information, déléguée à la protection des données.

Sont exclus : la clé virtuelle et l'application des résidents, le paiement, le contenu du bail, le choix du logiciel, l'audit sur place du prestataire, et toute analyse juridique.

**Étapes, calendrier et livrables** (a-3) :

| Semaine | Étape | Livrable |
|---|---|---|
| 1 (12-16 avril) | **cadrage** : lettre de mission signée par la présidente du directoire (objectifs, périmètre, référentiel, accès garantis aux systèmes et aux messageries, confidentialité, interlocuteurs, calendrier) ; réunion de lancement ; collecte des documents | lettre de mission |
| 2 (19-23 avril) | **prise de connaissance** : entretiens avec la déléguée, M. CALVÉRAC, le centre de relation résidents, des chargés d'accueil de deux ou trois résidences et la direction des systèmes d'information ; **cartographie du processus et des lieux où se trouvent les données** ; analyse des risques ; programme de travail | cartographie du processus, programme de travail |
| 3 et 4 (26 avril-7 mai ; semaine de quatre jours du 3 au 7 mai, jeudi 6 mai férié) | **collecte et examen** : revue documentaire, sondage sur un échantillon de dossiers, examen des comptes et des profils, inventaire des messageries, questionnaire au prestataire | dossier de travail |
| 5 (10-14 mai) | **analyse** des écarts, feuilles de constats (constat, cause, risque, recommandation, priorité, responsable, échéance), **validation contradictoire** avec les audités | feuilles de constats validées |
| 6 (18-21 mai ; lundi 17 mai férié) | **rapport**, note de synthèse et **restitution** au directoire le 21 mai ; plan d'action en deux temps : mesures avant le 1er juin, règles pour le paramétrage de septembre | rapport, note de synthèse, plan d'action |

Le suivi du plan d'action revient ensuite à la déléguée et à la direction des systèmes d'information. La mission doit s'achever avant le 1er juin, pour ne pas gêner la campagne et pour que les mesures immédiates s'appliquent dès l'ouverture des réservations.

**Preuves à demander** (a-4) :
- la liste des pièces et, pour chacune, l'étape qui s'en sert ;
- le registre des activités de traitement (version de 2022) et l'inventaire réel des traitements ;
- le bon de commande du prestataire de vérification des garants et ses réponses écrites sur le lieu, la durée de conservation, la protection et les éventuels autres sous-traitants des données ;
- l'extraction des comptes et des profils du logiciel de gestion locative, avec la date de dernière connexion et la date de fin de contrat des 40 saisonniers ;
- les journaux d'accès aux dossiers ;
- un échantillon d'une trentaine de dossiers de 2026, retenus et non retenus ;
- le décompte des dossiers conservés par année et par statut (environ 150 000, dont 60 000 de candidats jamais devenus résidents) et l'inventaire des pièces jointes des messageries ;
- les procédures écrites (départ des saisonniers, revue des comptes) ;
- la liste des projets non soumis à la déléguée depuis 2023.

*3.3 b) – Quatre critères de conformité et de sécurité appréciés* (quatre sont attendus ; cinq sont proposés)

| Critère | Ce qui est attendu | Situation actuelle (annexe 3.3) | Appréciation |
|---|---|---|---|
| **Minimisation des pièces demandées** | chaque pièce sert à une étape identifiée de la décision ou de la gestion du séjour ; la liste est validée avec la déléguée | liste de 2019 fixée sans la déléguée ; trois pièces sur dix types inutiles selon elle (photo, relevés de compte du garant, livret de famille) ; « plus on en demande… » | **non conforme** ; risque réglementaire et d'exposition accrue en cas de fuite ; priorité 1 avant le 1er juin, car corriger la liste ne coûte rien |
| **Registre des activités de traitement à jour** | chaque traitement inscrit avec ses finalités, ses catégories de données et de personnes, ses destinataires, ses durées et ses mesures de sécurité ; revue à chaque projet | dernière mise à jour en 2022 ; ni la clé virtuelle, ni le prestataire de vérification, ni les messageries ; déléguée consultée sur aucun projet depuis 2023 | **non conforme** ; c'est aussi un défaut de gouvernance : la déléguée est tenue à l'écart des projets ; priorité 2 |
| **Encadrement du sous-traitant** | contrat écrit fixant les instructions, la sécurité, la confidentialité, le sort des données en fin de contrat, les audits ; transmission sécurisée | simple bon de commande ; lieu et durée de conservation inconnus ; 3 000 dossiers de garants envoyés par courriel en 2026 | **non conforme**, risque élevé (bulletins de salaire, avis d'imposition) ; priorité 1 : contrat avant la campagne, ou suspension des envois |
| **Accès aux dossiers limités au besoin** | comptes nominatifs, profil limité à la résidence de rattachement, comptes fermés au départ, revue périodique | profil « chargé d'accueil » ouvert aux 60 résidences pour 120 personnes ; 40 comptes de saisonniers ouverts après leur départ ; aucune revue depuis 2021 | **non conforme** ; à fixer dans les profils du nouveau logiciel ; fermeture des 40 comptes immédiate |
| **Durée de conservation définie et appliquée** | une durée par catégorie (candidat non retenu, résident, garant), puis suppression ou archivage | aucune durée ; environ 150 000 dossiers depuis 2009, dont environ 60 000 (40 %) de candidats jamais devenus résidents ; 1,5 million de pièces jointes dans les messageries | **non conforme** ; stock à purger et durées à paramétrer dans le nouveau logiciel |

Appréciation d'ensemble : aucun des critères n'est satisfait. Les deux priorités sont l'encadrement du prestataire et l'arrêt de la circulation des pièces par courriel, qui concentrent les données les plus sensibles hors de tout contrôle.

**Réponses tolérées**
- Démarche en cinq à sept étapes (cadrage, prise de connaissance, analyse des risques, programme, collecte, restitution, suivi), si elle tient dans les six semaines et respecte l'échéance du 1er juin.
- Critère de sécurité des transmissions (courriel non protégé) ou de gouvernance (place de la déléguée) à la place de l'un des cinq thèmes, s'il est appliqué aux constats.
- Appréciation graduée (« partiellement conforme » pour le registre, qui existe), si elle est justifiée.
- Référentiel complété par COBIT 2019 pour la gouvernance, si la distinction avec ISO/IEC 27001 est juste.

**Erreurs fréquentes**
- *Méthodologie incomplète* (`JUR-A01`) — juste : objectifs, périmètre, référentiel, étapes, livrables et calendrier.
- *Audit du SI confondu avec l'audit légal* (`ET-34`) — juste : audit contractuel de conformité d'un processus, commandé par le directoire.
- *Dérive vers le droit des données personnelles* (droits des personnes, bases légales, sanctions de l'autorité de contrôle) (UE 1, F15 § 9) — non attendue : l'audit porte sur l'organisation (registre, sous-traitant, accès, conservation).
- *Déléguée à la protection des données chargée de conduire l'audit* (`ET-29`) — juste : elle est auditée sur le registre et doit être entendue ; l'auditeur externe garantit l'indépendance.
- *Liste légale de pièces exigibles* — non attendue : la minimisation s'apprécie au regard de l'usage de chaque pièce.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Démarche d'audit du SI, livrables | cadrage, prise de connaissance, risques, collecte, restitution, suivi | F10 § 1.1 et § 1.2 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | minimisation, conservation, sécurité, registre, sous-traitant, en principe | `rgpd` ; F15 § 2 et § 5 | applicable depuis le 25/05/2018 |
| ISO/IEC 27001:2022 | contrôle d'accès, relations avec les fournisseurs | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Déléguée à la protection des données, registre | missions, indépendance, tenue du registre | F15 § 1 et § 2 | notion de cours |

---

### 3.4 – Le pilotage de l'énergie des résidences (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : la durabilité est intégrée à la gouvernance globale du SI ; aucun calcul d'empreinte n'est attendu.

**Annexes mobilisées** : annexe 3.4 (consommations 2025 et 2026, écarts entre résidences, projet, choix proposés), annexe 3.5 (RGESN, règlement sur la cyberrésilience, RGPD en principe) et annexe 1.1 (objectif de 20 %, parc porté à 12 000 logements, application des résidents).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Green IT et IT for green définis et distingués ; projet situé (IT for green, avec une empreinte propre) | 0,5 |
| a-2 | Leviers du projet tirés de l'annexe, contribution chiffrée de tête (environ 9 à 15 % du total) et conditions (autres leviers, objectif à préciser, résidents) | 0,5 |
| b-1 | Indicateur complet rapporté à la référence 2025 et à une cible 2030 | 0,5 |
| b-2 | Second indicateur complet, relié au cas | 0,5 |
| c-1 | Empreinte du dispositif appréciée sans calcul (fabrication et renouvellement des boîtiers, volume et conservation des données, hébergement, effet rebond) | 0,5 |
| c-2 | Trois mesures de sobriété sur les choix de l'annexe 3.4 C, justifiées | 0,5 |

**Réponse attendue**

*3.4 a) – Green IT, IT for green et contribution du projet à l'objectif*

**Définitions** (a-1) : le **Green IT** réduit l'empreinte environnementale **du système d'information lui-même** : équipements, centres de données, logiciels, données et usages. L'**IT for green** met le numérique **au service de la réduction de l'empreinte de l'organisation** : capteurs, pilotage, mesure (F14 § 3). Le projet de pilotage de l'énergie relève de l'**IT for green** : il vise la consommation des bâtiments, qui représente environ 7 M€ par an. Mais il ajoute 9 000 boîtiers, des robinets, une plateforme et des données : il a sa propre empreinte, qui relève du Green IT (question c). Une stratégie responsable du système d'information traite les deux ensemble.

**Comment le projet sert l'objectif** (a-2) :
- il **chauffe seulement quand c'est utile** : il baisse le chauffage dans les logements vides, dont les quelque 630 logements vacants, et quand la fenêtre est ouverte, au lieu de deux réglages manuels par an ;
- il **mesure et compare** : les écarts de un à trois entre résidences comparables (de 3 000 à 9 000 kWh par logement) désignent où agir d'abord (résidences C et D) et quels travaux discuter avec les propriétaires ;
- il **informe les résidents**, qui ne connaissent pas aujourd'hui leur consommation.

**Contribution** : le chauffage pèse 60 % de la consommation, et le gain annoncé est de 15 à 25 % du chauffage, soit environ **9 à 15 % de la consommation totale** (de tête : 0,6 × 15 et 0,6 × 25). Le projet ne suffit donc pas seul à atteindre 20 %, et le gain annoncé par le prestataire reste à vérifier. La baisse de 2 % de 2026 tient surtout à la météo.

**Conditions** :
- **Préciser l'objectif.** Avec 12 000 logements en 2030, une baisse de 20 % de la consommation totale (36 000 MWh) exigerait 3 000 kWh par logement, soit 40 % de moins qu'en 2025. La cible doit donc porter sur la **consommation par logement** (4 000 kWh), mesurée à climat comparable, et le directoire doit l'écrire.
- **Agir aussi sur les autres leviers** : l'eau chaude (20 %), les autres usages (20 %) et les travaux, avec les propriétaires.
- **Associer les résidents** : confort, information, transparence sur les capteurs de présence, qui révèlent leur vie quotidienne et sont des données personnelles à limiter au strict besoin.
- **Associer la direction des systèmes d'information** au choix de la plateforme, à son raccordement à l'application et à la sécurité des boîtiers.
- **Mesurer les résultats** et maîtriser l'empreinte du dispositif.

*3.4 b) – Deux indicateurs de suivi*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Consommation d'énergie par logement géré** (b-1) | consommation d'énergie des résidences sur les douze derniers mois (kWh, chauffage, eau chaude et autres usages) / nombre moyen de logements gérés sur la période, présentée aussi à climat comparable | factures et relevés des fournisseurs d'énergie, puis plateforme de données énergétiques ; nombre de logements : logiciel de gestion locative | mensuelle, en cumul sur douze mois glissants ; revue annuelle par le directoire | **4 000 kWh par logement en 2030**, soit 20 % de moins que la **référence 2025 de 5 000 kWh** (4 900 kWh en 2026) ; jalon de 4 400 kWh en 2028 | environnement |
| **Écart de consommation entre résidences comparables** (b-2) | consommation par logement de la résidence la plus consommatrice / consommation par logement de la moins consommatrice, dans chaque groupe de résidences comparables | plateforme de données énergétiques et relevés des fournisseurs, par résidence | trimestrielle | rapport inférieur à 1,5 en 2029, contre 3 en 2026 (9 000 contre 3 000 kWh par logement) | processus |

Le premier indicateur rapporté au logement neutralise la croissance du parc ; présenté à climat comparable, il évite d'attribuer au projet un effet de la météo.

*3.4 c) – L'empreinte du dispositif et trois mesures de sobriété*

**Empreinte du dispositif lui-même** (c-1), sans calcul :
- la **fabrication** de 9 000 boîtiers électroniques, des robinets commandés et des équipements de transmission. Pour des équipements électroniques, la fabrication pèse souvent davantage que leur propre consommation (F14 § 1). Renouvelés entiers tous les cinq ans, les boîtiers à pile non remplaçable obligeraient à en fabriquer 18 000 en dix ans, piles comprises, au lieu de 9 000 ;
- le **volume de données** : environ 40 millions de mesures par jour, conservées au détail pendant dix ans et copiées dans deux centres de données, soit un stockage et des traitements qui ne cessent de croître ;
- l'**hébergement**, dont ni la consommation ni l'origine de l'électricité ne sont connues ;
- l'**effet rebond** : un logement mieux chauffé peut conduire à relever les consignes.

Le dispositif doit rester petit au regard de l'énergie qu'il fait économiser. La plupart de ces choix ne répondent à aucun besoin démontré : la sobriété commence par questionner ce besoin.

**Trois mesures de sobriété** (c-2 ; quatre sont proposées) :
1. **Fréquence** : une mesure par quart d'heure, ou une transmission au changement d'état (fenêtre ouverte, présence), au lieu d'une par minute, soit quinze fois moins de mesures (environ 2,6 millions par jour). C'est largement suffisant pour piloter un chauffage réglé aujourd'hui deux fois par an et pour la comparaison quotidienne.
2. **Conservation** : garder le détail treize mois, pour comparer une saison de chauffe à la précédente, puis seulement des agrégats (journaliers par logement, mensuels par résidence). Les données de présence au détail sont supprimées vite, ce qui sert aussi la minimisation des données personnelles (annexe 3.5).
3. **Durée de vie** : choisir le **boîtier à pile remplaçable garanti dix ans** (9 000 boîtiers en dix ans au lieu de 18 000). Exiger à l'achat la réparabilité, la reprise et le recyclage, et la fourniture de mises à jour de sécurité pendant toute la durée de vie, que le règlement sur la cyberrésilience met à la charge des fabricants, en principe, à compter du 11/12/2027.
4. **Hébergement** : exiger du prestataire la consommation et l'origine de l'électricité de ses centres de données, un hébergement dans l'Union européenne, une seule copie complète des données agrégées et une sauvegarde proportionnée au besoin, conformément au thème « hébergement » du RGESN.

**Réponses tolérées**
- Second indicateur différent, s'il est complet et relié au cas : part des heures de chauffage dans des logements vides ou à fenêtre ouverte ; part des logements équipés et pilotés (avancement) ; volume de données stockées par la plateforme ou consommation de la plateforme (Green IT).
- Cible par logement fixée sans correction climatique, si l'effet de la météo est signalé ; objectif lu en consommation totale, si la conséquence de la croissance du parc est expliquée.
- Gain du projet exprimé en fourchette voisine, ou jugé incertain faute de vérification, si la part du chauffage est utilisée.
- Mesures classées dans un autre ordre, ou quatrième mesure à la place de l'une des trois, si chacune répond à un choix de l'annexe 3.4 C.

**Erreurs fréquentes**
- *Green IT et IT for green confondus, ou sobriété réduite à l'économie d'énergie* (`ET-12`) — juste : le projet réduit l'énergie des bâtiments (IT for green) mais doit lui-même être sobre (Green IT), et la sobriété questionne d'abord le besoin.
- *Empreinte réduite à l'électricité* (`ET-38`) — juste : la fabrication et le renouvellement de 9 000 boîtiers comptent dans l'empreinte au même titre que l'électricité des centres de données, et la fabrication domine souvent pour des équipements électroniques (F14 § 1).
- *Indicateur incomplet ou générique* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe, avec la référence 2025 et la cible 2030.
- *Projet présenté comme suffisant pour atteindre 20 %* (`JUR-T03`) — juste : environ 9 à 15 % du total, à vérifier, et d'autres leviers nécessaires.
- *Calcul d'empreinte tenté, règle de performance énergétique des bâtiments ou cadre de durabilité invoqué* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Green IT, IT for green, sobriété, durée de vie | définitions, fabrication des équipements, effet rebond | F14 § 1 et § 3 | notion de cours |
| Indicateurs d'impact, référence et cible | kWh, trajectoire | F14 § 4 | notion de cours |
| RGESN, version 2024 | thème « hébergement », écoconception | `rgesn_2024` ; F14 § 2 | en vigueur |
| Règlement (UE) 2024/2847 sur la cyberrésilience (CRA) | mises à jour de sécurité fournies par les fabricants | `cra` ; F12 § 7 | applicable le 11/12/2027 ; article 14 depuis le 11/09/2026 |
| Règlement (UE) 2016/679 (RGPD) | minimisation des données de présence, en principe | `rgpd` ; F15 § 4 | applicable depuis le 25/05/2018 |
