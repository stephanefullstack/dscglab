# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 18 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F06 gestion des connaissances, F10 audit et fiabilisation, F05 projets et changement, F13 intelligence artificielle, F14 numérique responsable, F09 fiche d'indicateur, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Stratégie de gestion des connaissances et environnement existant | `1.6.a` Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle ; `1.6.b` Architecture fonctionnelle des systèmes de knowledge management (connaissances tacites et explicites) ; `1.6.d` Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums | 2,5 |
| 3.2 Audit post-implémentation du pilote | `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 3 |
| 3.3 Méthode de conduite de la généralisation et cahier des charges | `1.5.b` Méthodologies de gestion de projet (cycle en V, agile, hybride) ; `1.5.c` Élaboration d'un cahier des charges fonctionnel et technique | 2 |
| 3.4 Risques, plan qualité et recette de la généralisation | `1.5.e` Identification et gestion des risques (maintenance, évolutivité, sécurité) ; `1.5.f` Mise en œuvre et contrôle du plan qualité | 2 |
| 3.5 Appropriation et gouvernance du dispositif | `1.6.e` Leviers d'appropriation et de transformation des pratiques professionnelles ; `1.6.c` Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) | 2 |
| 3.6 Choix du service d'IA et transition numérique responsable | `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 1,5 |
| **Dossier 3 – Évaluer le pilote de la base de connaissances et conduire sa généralisation** |  | **13** |

Répartition indicative : connaissances (connaissances explicites et tacites, audit post-implémentation, critères d'appréciation, cycle en V et démarche agile, cahier des charges fonctionnel, plan qualité, transition numérique responsable) 2,5 points (items 3.1 a-1, 3.2 a pour moitié, 3.2 b-1 pour moitié, 3.3 a-1 pour moitié, 3.3 b pour un quart, 3.4 b-1 pour moitié, 3.6-1 pour moitié) ; analyse des annexes et recommandations 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Stratégie de gestion des connaissances et environnement existant (2,5 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.a` « Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle » ; `1.6.b` « Architecture fonctionnelle des systèmes de knowledge management » (connaissances tacites et explicites) ; `1.6.d` « Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums ». Limites : « La gestion des connaissances dépasse la seule numérisation de l'information » ; « Le pilotage nécessite une approche systémique : outils, processus, culture » ; « Le lien avec la gestion des compétences (RH) est complémentaire mais distinct ».

**Annexes mobilisées** : annexes 3.1 (sources, questions répétées, associés proches de la retraite, outils existants), 3.2 (dispositif du pilote) et 1.1 (plan « CORLANDEAU 2030 », pôle technique).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Connaissances explicites et tacites distinguées et illustrées par le cas (notes, fiches, modèles ; expérience des associés proches de la retraite) | 0,5 |
| a-2 | Trois axes de stratégie, chacun relié à la connaissance visée et à l'apport ou à la limite de la base et de l'assistant ; dispositif systémique (outils, processus, culture) ; 0,5 dès deux axes appliqués | 0,5 |
| b | Quatre éléments (GED, intranet, forum, dossiers partagés), chacun conservé, transformé ou abandonné, avec une justification tirée de l'annexe 3.1 et son articulation avec la base ; 1 pour trois éléments, 0,5 pour deux | 1,5 |

**Réponse attendue**

*3.1 a) – Connaissances explicites et tacites ; trois axes de stratégie*

Une **connaissance explicite** est formalisée et transmissible sans son auteur : document, procédure, modèle ; au cabinet, les 300 notes du pôle technique, les réponses données par courriel, les modèles de lettres de mission et de dossiers de travail, la doctrine des bases des éditeurs. Une **connaissance tacite** est incorporée à la personne, issue de l'expérience, difficile à formaliser et liée au contexte : la manière dont M. VERDALHAC conduit un dossier difficile d'association, ce qu'il vérifie en priorité, ce qui a déjà posé problème chez un client semblable (annexe 3.1 C) (F06 § 1) (0,5 pt).

La stratégie de gestion des connaissances organise la création, le partage, la mise à jour et la réutilisation de ces deux formes de connaissance au service du plan « CORLANDEAU 2030 » (« capitaliser la connaissance technique ») ; elle combine des outils, des processus et une culture du partage, et ne se réduit pas à numériser des documents (0,5 pt pour trois axes appliqués) :

| Axe | Connaissance visée | Ce que la base et l'assistant apportent | Ce qu'ils n'apportent pas |
|---|---|---|---|
| **1. Un référentiel unique et validé de la connaissance explicite** : une fiche par question, avec ses sources, son auteur, son validateur, sa date de validation et sa date de revue ; reprise des notes, des réponses et des modèles des six bureaux | explicite, aujourd'hui dispersée (six arborescences, 300 notes jamais mises à jour, réponses enfermées dans les messageries, une version de chaque modèle par bureau) | un point d'accès unique ; une recherche en langage courant qui cite la fiche ; un temps de recherche déclaré qui passe de 30 à 10 minutes | la qualité du contenu : une fiche périmée produit une réponse fausse (60 fiches à reprendre en mars, 80 % de réponses exactes) ; le contenu dépend du processus de validation et de mise à jour |
| **2. Une boucle de capitalisation entre les bureaux et le pôle technique** : toute question sans fiche est transmise à un expert, et la réponse devient une fiche ; les experts sont libérés des questions répétées pour la validation et la veille | explicite en création continue : six questions sur dix portent sur un sujet déjà traité (300 par mois en période fiscale) | il oriente vers la fiche existante et signale l'absence de fiche ; la base s'enrichit des questions réelles | il ne doit pas répondre à la place de l'expert quand aucune fiche n'existe (20 % de réponses sans fiche en mars) |
| **3. La transmission de l'expérience par les personnes** : binômes entre les trois associés qui partent d'ici 2029 et des chefs de mission, retours d'expérience sur des cas réels, rédigés ensuite en fiches de cas avec leur contexte, annuaire des expertises | tacite, concentrée chez quelques associés et menacée par leurs départs | il diffuse ce qui a été formalisé, avec le contexte et les limites du cas | il ne capte pas le tacite : le jugement se transmet en travaillant ensemble, comme le souhaite M. VERDALHAC |

*3.1 b) – Intégration dans l'environnement existant*

| Élément | Décision | Justification (annexe 3.1) et articulation avec la base |
|---|---|---|
| **GED** | **conservée et transformée** | outil déjà en place depuis 2019 et maîtrisé, mais sans espace pour la documentation technique : y créer un espace « documentation technique » avec un plan de classement par domaine (fiscal, comptable, social, juridique) et des métadonnées (auteur, validateur, date de validation, date de revue, statut) ; les fiches et les modèles communs validés y sont versionnés et archivés ; l'assistant n'interroge que cet espace validé, jamais les dossiers des clients |
| **Intranet** | **transformé** | peu consulté (25 % des salariés par mois), pages techniques à l'abandon depuis 2022 : il devient le point d'entrée unique, avec la recherche de l'assistant sur la page d'accueil, la connexion avec le compte habituel du cabinet (« une connexion de plus » regrettée par M. QUINTAREL), les nouveautés techniques et les fiches mises à jour, l'annuaire des référents ; les pages techniques périmées sont retirées |
| **Forum interne** | **abandonné** | aucun message depuis mars 2023, 40 questions restées sans réponse : un espace d'échange sans animateur ni règle de réponse échoue ; sa fonction est reprise par la transmission des questions sans fiche au pôle technique ou au référent du bureau, avec un engagement de délai, et la réponse devient une fiche |
| **Dossiers partagés des bureaux** | **abandonnés pour la documentation technique, après reprise** | six arborescences, versions multiples sans date ni auteur : les documents sont triés avec chaque bureau (environ 2 000 documents), ce qui mérite d'être conservé devient une fiche ou un modèle commun, avec ses variantes locales validées ; les dossiers sont ensuite figés en lecture seule puis archivés, pour qu'aucune version parallèle ne subsiste ; associer les bureaux répond à la crainte de Mme LEFRANDIER |

(1,5 pt pour les quatre éléments justifiés ; 1 pt pour trois ; 0,5 pt pour deux.)

Les **bases documentaires des éditeurs** sont conservées comme sources de référence citées par les fiches ; l'extension des accès aux bureaux autres que Poitiers est valorisée, non exigée.

**Réponses tolérées**
- Axes formulés autrement (« formaliser, partager, transmettre » ; « référentiel, communauté, transmission »), si l'explicite et le tacite sont tous deux traités et si les limites de l'outil apparaissent.
- Référence au modèle SECI (Nonaka et Takeuchi), si elle reste un appui et est appliquée au cas : externalisation des réponses en fiches, combinaison dans la base, socialisation en binômes.
- Forum transformé plutôt qu'abandonné (espace de questions et réponses animé par les référents, intégré à l'intranet), si la cause de l'échec (absence d'animation et de réponse) est traitée.
- GED « conservée » sans transformation, si le candidat crée ailleurs un espace documentaire validé et versionné et exclut les dossiers des clients du champ de l'assistant.

**Erreurs fréquentes**
- *Gestion des connaissances réduite à la GED ou à l'outil* (`ET-21`) — « installer l'assistant dans les six bureaux suffit » ; juste : un dispositif qui associe outils, processus de validation et de mise à jour, et culture du partage.
- *Tacite traité comme de l'explicite* — « l'assistant capitalisera l'expérience des associés » ; juste : le tacite se transmet d'abord par les personnes, puis se formalise en partie avec son contexte.
- *Dérive vers la gestion des compétences* (limite du programme) — plan de formation ou de recrutement pour remplacer les associés ; juste : la transmission de la connaissance, distincte de la gestion des compétences.
- *Décisions non justifiées par l'annexe* (`JUR-T08`) — « supprimer l'intranet » sans considérer son rôle de point d'entrée ni sa faible consultation.
- *Assistant raccordé aux dossiers des clients* — il élargirait l'exposition de données couvertes par le secret professionnel ; juste : un champ limité à la documentation validée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Connaissances tacites et explicites | distinction et axes | F06 § 1 | notion de cours |
| Architecture fonctionnelle d'un dispositif de gestion des connaissances ; GED, plan de classement, métadonnées | intégration des outils | F06 § 2.1 et 3 | notion de cours |
| Modèle SECI (Nonaka et Takeuchi, 1995) | réponse tolérée | `nonaka_takeuchi_seci` / F06 § 1 | modèle publié |
| ISO 15489-1 — gestion des documents d'activité | cycle de vie des fiches dans la GED (illustratif) | `iso_15489_1` / F06 § 4 | en vigueur |

---

### 3.2 – Audit post-implémentation du pilote (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; « La conformité financière et comptable n'est pas traitée dans le programme de l'UE 5 » ; « L'audit SI suppose une approche multidisciplinaire et une posture critique vis-à-vis de la gouvernance ».

**Annexes mobilisées** : annexes 3.4 A (demande, durée, interlocuteurs), 3.2 (dispositif, résultats, contenu des questions, journaux), 3.3 (témoignages) et 3.4 C (repères).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Audit post-implémentation défini (évaluation, après la mise en service, de l'atteinte des objectifs, de la qualité et de la conformité, pour décider et tirer des enseignements) et démarche appliquée : objectifs, périmètre (inclus et exclus), étapes sur six semaines jusqu'à la restitution avant le comité du 24 juin, livrables ; 0,5 si la démarche est incomplète (sans périmètre, livrables ni calendrier) | 1 |
| b-1 | Quatre critères définis et appréciés avec les chiffres de l'annexe 3.2 ; 0,5 pour deux ou trois critères | 1 |
| b-2 | Deux limites des résultats présentés (absence d'objectifs et de mesure initiale, contrôle par les auteurs des fiches sur un petit échantillon, temps déclaré par des volontaires, périodes non comparables) | 0,5 |
| c | Deux facteurs de succès et deux points de vigilance propres à l'audit d'un outil fondé sur l'IA générative ; 0,5 dès trois éléments précis | 0,5 |

**Réponse attendue**

*3.2 a) – Définition et démarche*

L'**audit post-implémentation** est l'évaluation indépendante et méthodique d'un système après sa mise en service (ici un pilote) : il compare les résultats obtenus aux objectifs et aux bénéfices attendus, apprécie la qualité, la sécurité et la conformité du système et de l'organisation qui l'accompagne, et conclut par des recommandations qui éclairent la décision (généraliser, corriger, arrêter) et les projets suivants. Il s'inscrit dans la démarche générale de l'audit du SI : examen au regard de critères et d'un référentiel, constats, recommandations hiérarchisées (F10 § 1.1 et 1.2).

Démarche appliquée (0,5 pt pour la définition et les objectifs, 0,5 pt pour le périmètre, les étapes, les livrables et le calendrier) :
- **Mandant et auditeur** : la présidente, qui décidera devant le comité des associés du 24 juin 2027 ; le chargé de mission, arrivé en janvier 2027, n'a pas conduit le pilote ; il s'appuie, pour juger de l'exactitude des réponses, sur un professionnel qui n'a pas rédigé les fiches.
- **Objectifs** : apprécier (1) la fiabilité des réponses et la traçabilité de leurs sources, (2) la protection des données des clients, (3) l'usage réel et les gains, (4) l'organisation de rédaction, de validation et de mise à jour des fiches ; en déduire les conditions de la généralisation.
- **Périmètre** : la base de 400 fiches, l'assistant, le service d'IA et son contrat, l'organisation du pôle technique et l'accompagnement des utilisateurs dans les bureaux de Poitiers et de Niort, depuis septembre 2026 (résultats arrêtés en mars 2027, témoignages d'avril). **Exclus** : le fonctionnement interne du modèle, tout test technique des systèmes du prestataire ou du fournisseur, le contenu doctrinal au-delà d'un échantillon, la situation des quatre autres bureaux (sinon comme référence).
- **Étapes** (six semaines, du 19 avril au 31 mai) : (1) semaine 1, **cadrage** : lettre de mission signée par la présidente (objectifs, périmètre, critères et seuils d'appréciation, référentiels : COBIT 2019 pour la gestion des changements et le suivi des bénéfices, le RGPD pour la sous-traitance, la charte du pilote) ; (2) semaines 1 et 2, **prise de connaissance** : entretiens avec les associés de Poitiers et de Niort, M. DUVERNAIL et les deux experts, M. QUINTAREL, le prestataire, revue du contrat, de la charte, des journaux et des résultats ; (3) semaines 2 à 4, **collecte et tests** : jeu de questions de référence posé à l'assistant et corrigé par un professionnel indépendant des fiches, sondage sur les questions réelles (exactitude, citation des sources, présence de données de clients), revue des dates des fiches, analyse de l'usage par bureau et par profil, questionnaire adressé aux 70 utilisateurs et entretiens avec des non-utilisateurs ; (4) semaine 5, **analyse et validation contradictoire** des constats avec les audités ; (5) semaine 6, **restitution** : note de synthèse à la présidente, sans détail technique, avant le 31 mai, pour préparer le comité du 24 juin ; (6) **suivi** des recommandations retenues dans le projet de généralisation.
- **Livrables** : lettre de mission, grille des critères, programme de travail, feuilles de constats (constat, risque, recommandation, priorité), note de synthèse avec les conditions de la généralisation, plan d'action.

*3.2 b) – Quatre critères d'appréciation et lecture critique*

| Critère | Définition | Appréciation du pilote (annexe 3.2) |
|---|---|---|
| **Fiabilité des réponses** | exactitude et actualité des réponses au regard de la doctrine validée par le cabinet | insuffisante : 90 % de réponses exactes en octobre, 80 % en mars, soit une réponse sur cinq inexacte en pleine période fiscale, quand l'enjeu pour les clients est le plus fort ; 60 des 400 fiches (15 %) devenues inexactes après un changement de règle et non corrigées ; aucune date de revue prévue |
| **Traçabilité des sources** | chaque réponse renvoie à une fiche validée (auteur, date), elle-même fondée sur des sources identifiées, et la question comme la réponse peuvent être retrouvées | partielle : 10 % puis 20 % de réponses ne citent aucune fiche ; les journaux sont effacés au bout de 30 jours et le cabinet n'en garde aucune copie : impossible de savoir quelle réponse a été donnée à qui en cas d'erreur chez un client |
| **Confidentialité des données des clients** | protection des informations couvertes par le secret professionnel et des données personnelles, au regard de la charte et du contrat avec le prestataire | non maîtrisée : 30 des 200 questions relues (15 %) contiennent le nom d'un client ou des montants de son dossier malgré la charte ; questions traitées hors de l'Union européenne selon le prestataire (annexe 3.4 B), usage des données inconnu du responsable informatique ; règle ignorée des utilisateurs (« je ne sais pas si j'ai le droit ») |
| **Usage** | adoption effective par les utilisateurs visés et effet sur le travail (temps, sollicitations du pôle technique) | en recul : 56 utilisateurs sur 70 en octobre (80 %), 35 en mars (50 %) ; 1 500 puis 1 000 recherches, un tiers de moins ; questions au pôle technique en baisse d'un cinquième seulement (250 en mars 2026, 200 en mars 2027) ; gain déclaré de 30 à 10 minutes par recherche |

(1 pt pour les quatre critères définis et appréciés ; 0,5 pt pour deux ou trois.)

Deux limites des résultats (0,5 pt) :
1. **Aucun objectif ni aucune mesure de départ** n'a été fixé au lancement : on ne peut dire si 80 % de réponses exactes ou 50 % d'utilisateurs sont un succès ; l'audit doit d'abord fixer des seuils avec la présidente.
2. **Exactitude jugée par les auteurs des fiches**, sur 50 réponses par mois choisies selon une méthode inconnue : contrôle ni indépendant ni forcément représentatif.
3. **Gain de temps déclaré** par 30 volontaires sur 70 (43 %), sans mesure : biais de sélection (les utilisateurs satisfaits répondent plus volontiers) et de déclaration.
4. **Périodes non comparables** : octobre et mars ne présentent ni les mêmes questions ni la même charge ; la baisse d'usage peut venir de la défiance après des erreurs, du manque de temps en période fiscale ou de la fin de l'effet de nouveauté : corrélation n'est pas cause, les entretiens doivent éclairer l'explication.

*3.2 c) – Facteurs de succès et points de vigilance propres à l'audit d'un outil d'IA générative*

Facteurs de succès (deux attendus) :
- **Accès aux traces et aux informations du prestataire et du fournisseur** : copie des journaux avant leur effacement à 30 jours, contrat, lieu de traitement, version du modèle ; à obtenir dès le cadrage, au besoin par la présidente.
- **Compétences pluridisciplinaires et indépendance** : un professionnel de la doctrine qui n'a pas écrit les fiches, associé au responsable informatique ; une posture non punitive, alors que les experts craignent de « répondre d'une réponse de la machine ».
- **Critères et seuils fixés avant les tests** avec la présidente (par exemple un taux d'exactitude exigé), pour éviter un jugement a posteriori.

Points de vigilance (deux attendus) :
- **Réponses non reproductibles** : la même question peut recevoir des réponses différentes ; l'audit repose sur un jeu de questions de référence posé plusieurs fois, réponses conservées, et sur des échantillons de questions réelles, non sur quelques démonstrations.
- **Distinguer l'erreur de contenu et l'erreur de l'assistant** : une réponse fausse peut venir d'une fiche périmée (gouvernance du contenu) ou d'une réponse produite sans fiche (comportement de l'outil) ; les recommandations diffèrent.
- **Système qui évolue sans préavis** : le fournisseur peut changer de version du modèle pendant l'audit ; dater les tests et noter la version.
- **Pas de données réelles de clients dans les tests** : jeu d'essai fondé sur des cas fictifs ou rendus anonymes.
- **Opacité du modèle** : l'audit porte sur les résultats, les traces, le contrat et l'organisation, pas sur le fonctionnement interne du modèle.

(0,5 pt pour deux facteurs et deux points de vigilance précis ; 0,5 pt dès trois éléments précis.)

**Réponses tolérées**
- Démarche en cinq ou sept étapes, si le cadrage, la collecte, la restitution avant le comité et le suivi y figurent.
- Audit qualifié de « bilan » ou de « revue post-implémentation », s'il compare résultats et objectifs et débouche sur une décision.
- Autre référentiel cité à l'appui (ITIL pour la gestion des changements et des niveaux de service, ISO/IEC 42001:2023 pour le management de l'IA), s'il est utilisé comme référentiel d'appréciation et non comme une certification à obtenir.
- Critère « usage » apprécié sous l'angle de l'efficacité ou de l'efficience, si l'adoption et les gains sont rapprochés.
- Autre limite pertinente : questions au pôle technique comparées d'une année à l'autre sans tenir compte des autres facteurs (nouveautés fiscales, effectifs).

**Erreurs fréquentes**
- *Méthodologie d'audit incomplète* (`JUR-A01` méthodologie structurée : périmètre, objectifs, étapes, livrables, échéancier) — étapes sans périmètre, sans livrables, ou restitution prévue après le comité du 24 juin.
- *Audit technique du modèle* — examen des algorithmes, essais de vulnérabilité ou de charge ; juste : résultats, traces, contrat, organisation ; les tests techniques détaillés ne sont pas attendus.
- *Chiffres lus sans recul* (`JUR-T03` analyser et argumenter) — « 10 minutes au lieu de 30, le pilote est un succès » ; juste : gain déclaré par des volontaires, à rapprocher de la baisse d'usage et de la fiabilité.
- *Audit du SI confondu avec l'audit des comptes* (`ET-34`) — vérification des comptes des clients ou du cabinet ; juste : fiabilité, traçabilité, confidentialité et usage d'un outil.
- *Dérive vers le droit des données personnelles* — bases légales, transferts, droits des personnes ; juste : la confidentialité comme critère d'organisation (charte, contrat, lieu de traitement, conservation), sans analyse juridique, comme l'indique l'annexe 3.4 C.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI : définition, démarche, livrables, facteurs de succès | démarche de l'audit du pilote | F10 § 0, 1.1 et 1.2 | notion de cours |
| COBIT 2019 (ISACA) | référentiel de gestion des changements et de suivi des bénéfices | `cobit_2019` / F02 § 3 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), sous-traitance et sécurité | critère de confidentialité (annexe 3.4 C) | `rgpd` / F15 | en vigueur |
| Risques de l'IA générative (réponses inexactes, confidentialité, dépendance) | critères et points de vigilance | F13 § 3 | notion de cours |
| ISO/IEC 42001:2023 — système de management de l'IA | réponse tolérée | `iso_42001_2023` / F13 § 4 | en vigueur |

---

### 3.3 – Méthode de conduite de la généralisation et cahier des charges (2 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.b` « Méthodologies de gestion de projet (cycle en V, agile, hybride) » ; `1.5.c` « Élaboration d'un cahier des charges fonctionnel et technique ». Limites : « L'aspect budgétaire détaillé ne relève pas du programme de l'UE » ; les approches de livraison continue sont mentionnées mais non approfondies.

**Annexes mobilisées** : annexes 3.2 C (tâches, jalons, contrainte, deux options), 3.2 A et B (pilote), 3.3 (experts, collaborateurs), 3.4 B (service d'IA) et 1.1 (bureaux, période fiscale).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cycle en V et démarche agile caractérisés, puis comparés selon les trois critères appliqués aux options A et B (mise en service de février en pleine période fiscale, livraisons de janvier à mai, expert indisponible deux jours par semaine) | 0,5 |
| a-2 | Recommandation justifiée et compatible avec la période fiscale (démarche hybride avec gel des mises en service, ou option adaptée) | 0,5 |
| b | Rôle du cahier des charges fonctionnel précisé et quatre rubriques, chacune illustrée par un contenu des annexes ; 0,5 pour deux ou trois rubriques | 1 |

**Réponse attendue**

*3.3 a) – Comparaison et recommandation*

Le **cycle en V** est une démarche séquentielle : expression du besoin et spécifications complètes, conception, réalisation, puis tests et recette en miroir de chaque niveau de spécification ; il convient à un besoin stable, se contractualise au forfait, mais découvre tard les écarts (effet tunnel). La **démarche agile** (Scrum) procède par itérations courtes qui livrent chacune un incrément utilisable, à partir d'un carnet de demandes classées par valeur par un responsable du produit ; elle s'adapte au besoin qui évolue mais exige un responsable du produit disponible et des utilisateurs impliqués (F05 § 2).

| Critère | Option A – Cycle en V | Option B – Démarche agile |
|---|---|---|
| **Stabilité du besoin** | adaptée au socle stable et éprouvé par le pilote (raccordement à l'intranet et à la GED, connexion, droits, choix du service d'IA) ; inadaptée au contenu et aux usages, qui évoluent sans cesse et que les quatre autres bureaux n'ont pas exprimés (Mme LEFRANDIER) | adaptée aux besoins découverts bureau par bureau et à l'enrichissement de la base ; risque de dérive du périmètre sans cahier des charges ni critères d'acceptation, d'autant que la facturation est au temps passé |
| **Disponibilité des experts** | sollicitation concentrée sur la validation des spécifications en août et la recette en décembre, hors période fiscale | un expert responsable du produit deux jours par semaine : intenable pour deux experts déjà submergés par la validation des fiches et 300 à 500 questions par mois |
| **Période fiscale** | mise en service simultanée dans six bureaux en février 2028 : en pleine période fiscale, contraire à la règle du comité ; « big bang » sans retour d'expérience, et tout retard repousse la mise en service au 1er juin | mises en service bureau par bureau dès septembre, compatibles ; mais livraisons de nouvelles fonctions de janvier à mai, contraires à la règle du comité |

(0,5 pt.)

**Recommandation : une démarche hybride** (0,5 pt).
- **Cadrage et socle en cycle en V** de juin à août : cahier des charges fonctionnel, choix du service d'IA, raccordement à l'intranet et à la GED, connexion avec le compte du cabinet, droits, conservation des journaux ; recette du socle fin août, au forfait.
- **Mise en service progressive** de septembre à décembre 2027, un bureau par mois (La Rochelle, Angoulême, Saintes, Châtellerault), en itérations courtes pour adapter l'ergonomie et reprendre les contenus de chaque bureau avec son référent ; le responsable du produit est un chef de mission ou le chargé de mission, déchargé en partie, les experts n'intervenant que pour la validation.
- **Gel du 15 janvier au 31 mai** : aucune mise en service ni nouvelle version ; seules la maintenance corrective et la mise à jour des fiches continuent — corriger une fiche après un changement de règle n'est pas un changement de version du logiciel, c'est la condition de la fiabilité.
- Reprise des itérations en juin 2028 ; tout ce qui n'est pas prêt mi-décembre attend juin.

*3.3 b) – Cahier des charges fonctionnel*

Le **cahier des charges fonctionnel** exprime le besoin de la maîtrise d'ouvrage (le « quoi », non le « comment ») : contexte, objectifs, périmètre, fonctions attendues et leur priorité, contraintes et critères d'acceptation ; rédigé avec les utilisateurs et validé par le commanditaire, il fonde le contrat avec le prestataire et la recette (F05 § 3). Quatre rubriques (1 pt) :

| Rubrique | Contenu tiré des annexes |
|---|---|
| **Contexte, objectifs mesurables et périmètre** | priorité « capitaliser la connaissance technique » du plan ; six bureaux, 180 utilisateurs, environ 3 000 questions par mois, 800 fiches à la fin de 2027 ; objectifs chiffrés que le pilote n'avait pas (taux de réponses exactes, part des utilisateurs actifs, baisse des questions répétées au pôle technique) ; exclus : les dossiers des clients, la rédaction de courriers |
| **Exigences fonctionnelles priorisées** (indispensable, souhaitable, facultatif) | indispensable : réponse citant toujours la fiche, son auteur et sa date ; absence de fiche signalée avec transmission de la question au pôle technique ; circuit de rédaction, de relecture et de validation des fiches avec date de revue ; retrait des fiches périmées ; signalement d'une erreur par l'utilisateur ; souhaitable : nouveautés et fiches mises à jour sur l'intranet |
| **Contraintes et exigences non fonctionnelles** | confidentialité (aucune donnée de client, lieu de traitement et absence de conservation des questions par le fournisseur), traçabilité (journaux conservés par le cabinet), accessibilité aux logiciels de lecture d'écran, connexion avec le compte du cabinet, réversibilité des fiches, aucune mise en service du 15 janvier au 31 mai, sobriété du service |
| **Critères d'acceptation et organisation de la recette** | jeu de questions de référence, seuils (taux d'exactitude, citation des sources, absence de fiche périmée citée), recette par le pôle technique et les référents avant chaque mise en service |

**Réponses tolérées**
- Option B retenue, si le candidat la corrige explicitement : gel du 15 janvier au 31 mai, responsable du produit autre qu'un expert, cahier des charges et critères d'acceptation, prix encadré.
- Option A retenue avec une mise en service avancée en décembre ou bureau par bureau à l'automne, si la période fiscale est respectée et l'effet tunnel discuté.
- Autre rubrique illustrée : utilisateurs et profils (collaborateurs, référents, experts, administrateur) ; reprise des contenus existants (2 000 documents) ; jalons (décision du 24 juin, mises en service de septembre à décembre) ; formation et accompagnement.

**Erreurs fréquentes**
- *Récitation des méthodes sans le cas* (`JUR-P02` deux méthodes de projet comparées dans le contexte) — phases du cycle en V et rôles de Scrum sans lien avec la période fiscale ni avec la charge des experts.
- *Agile assimilé à l'absence de cahier des charges* (`ET-32`) — « en agile, pas besoin de spécifier » ; juste : carnet de demandes priorisé, critères d'acceptation, contraintes fixées d'avance.
- *Gel confondu avec l'arrêt de la mise à jour des fiches* — la période fiscale interdit les changements de version du logiciel, pas la correction des contenus, dont dépend la fiabilité.
- *Planning détaillé ou chiffrage du projet* — diagramme de Gantt, budget par lot : non demandés.
- *Cahier des charges technique* — architecture, serveurs, choix du modèle ; juste : le besoin et les contraintes, le « comment » relevant du prestataire.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cycle en V, démarche agile, démarche hybride ; critères de choix | comparaison et recommandation | F05 § 2 | notion de cours |
| The Scrum Guide (Schwaber et Sutherland, novembre 2020) | itérations, responsable du produit | `scrum_guide_2020` / F05 § 2.2 | en vigueur |
| Cahier des charges fonctionnel ; priorisation des exigences | quatre rubriques | F05 § 3 | notion de cours |
| ITIL, gestion des changements (calendrier des changements) | gel en période fiscale (réponse tolérée) | `itil_4` / F02 § 5 | en vigueur |

---

### 3.4 – Risques, plan qualité et recette de la généralisation (2 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.e` « Identification et gestion des risques (maintenance, évolutivité, sécurité) » ; `1.5.f` « Mise en œuvre et contrôle du plan qualité ». Limite : « Le suivi post-déploiement (TMA, support) n'est abordé que dans une perspective de maintenance évolutive et curative ».

**Annexes mobilisées** : annexes 3.2 (fiches devenues inexactes, journaux, contenu des questions, projet), 3.3 (experts, responsable informatique, collaborateur malvoyant) et 3.4 B (service d'IA).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Trois risques (maintenance de la base, évolutivité, sécurité et confidentialité), chacun avec sa cause dans les annexes, sa conséquence et une mesure de traitement ; 0,5 pour deux risques complets | 1 |
| b-1 | Plan qualité défini et contenu adapté à la généralisation (organisation et rôles, normes de rédaction des fiches, gestion des versions et des changements, contrôles et revues, indicateurs de qualité) | 0,5 |
| b-2 | Recette décrite : acteurs, jeu d'essai, critères d'acceptation, calendrier compatible avec la période fiscale ; 0,5 dès trois des quatre éléments | 0,5 |

**Réponse attendue**

*3.4 a) – Trois risques*

| Risque | Cause (annexes) | Conséquence | Traitement |
|---|---|---|---|
| **Maintenance de la base** : des fiches deviennent fausses plus vite qu'elles ne sont corrigées | aucune date de revue ; 60 fiches devenues inexactes en début d'année ; deux experts pour valider 400, puis 800 fiches, en plus des questions | réponses inexactes données aux clients, en pleine période fiscale ; perte de confiance (Mme ROUSSELANGE vérifie tout) et retour aux appels aux experts | date de revue obligatoire sur chaque fiche ; fiche retirée des réponses de l'assistant dès sa date dépassée ou dès qu'un changement de règle la vise ; campagne de revue planifiée en décembre et janvier, sur la liste des fiches touchées par les nouveautés fiscales ; validation répartie entre les experts et des référents de domaine ; maintenance corrective et évolutive prévue au contrat du prestataire |
| **Évolutivité** : le dispositif ne suit pas le passage à l'échelle | de 70 à 180 utilisateurs, de 1 500 à environ 3 000 questions par mois, de 400 à 800 fiches, quatre bureaux aux pratiques propres ; coût lié au fournisseur ; modèle modifiable par le fournisseur ; une équipe informatique de trois personnes sans temps pour administrer | lenteurs, coûts en hausse, comportement des réponses modifié sans préavis, dépendance envers un fournisseur | fiches conservées dans la GED du cabinet, dans un format réutilisable, indépendamment du modèle, pour pouvoir changer de service ; contrat : capacité garantie pour le volume prévu, information préalable sur tout changement de version, réversibilité, prix encadré ; mise en service bureau par bureau ; administration confiée à une personne désignée |
| **Sécurité et confidentialité** | 15 % des questions relues contiennent des données de clients ; traitement par un fournisseur dont le lieu et l'usage des données sont inconnus ; journaux effacés à 30 jours ; droits par bureau et par pôle à créer | atteinte au secret professionnel et à la confiance des clients ; impossibilité de reconstituer une réponse contestée | service sans conservation des questions, hébergé dans l'Union européenne (option 2), contrat de sous-traitance précis ; règle claire, rappelée à l'écran, et avertissement lorsqu'une question semble contenir des données d'un client ; connexion avec le compte du cabinet et droits par profil ; journaux conservés par le cabinet pendant une durée fixée |

(1 pt pour trois risques complets ; 0,5 pt pour deux.)

*3.4 b) – Plan qualité et recette*

Le **plan qualité** (plan d'assurance qualité) est le document qui fixe, pour un projet, l'organisation, les règles et les contrôles qui garantissent que les livrables répondent aux exigences : rôles et responsabilités, normes de documentation, gestion des versions et des changements, revues, plan de tests, critères d'acceptation, traitement des anomalies, indicateurs (F05 § 6). Contenu pour la généralisation (0,5 pt) :
- **Organisation** : la présidente commanditaire ; un comité de pilotage mensuel (M. DUVERNAIL, un associé de bureau, M. QUINTAREL, le chargé de mission, chef de projet, le prestataire) ; le pôle technique et les référents comme maîtrise d'ouvrage du contenu ; le prestataire comme maîtrise d'œuvre.
- **Normes** : modèle de fiche obligatoire (question, réponse, contexte et limites, sources, auteur, validateur, date de validation, date de revue, domaine) ; règles de rédaction ; modèles communs avec variantes locales identifiées.
- **Gestion des versions et des changements** : versions des fiches tracées dans la GED ; calendrier des changements du logiciel avec gel du 15 janvier au 31 mai ; toute nouvelle version du modèle soumise à un essai de non-régression.
- **Contrôles et revues** : relecture de chaque fiche par une personne autre que l'auteur ; revue de projet à chaque mise en service de bureau ; contrôle mensuel d'un échantillon de réponses par un expert qui n'en est pas l'auteur.
- **Traitement des anomalies** : classement (bloquante, majeure, mineure), délai de correction.

**Recette** (0,5 pt) :
- **Acteurs** : recette technique par le prestataire et M. QUINTAREL (raccordement à l'intranet et à la GED, connexion, droits, journaux, capacité annoncée) ; recette fonctionnelle par la maîtrise d'ouvrage : les deux experts, les référents de chaque bureau et des utilisateurs, dont des collaborateurs d'un bureau non pilote et le collaborateur qui utilise un logiciel de lecture d'écran ; procès-verbal signé par le commanditaire, avec ou sans réserves.
- **Jeu d'essai** : questions de référence avec leur réponse attendue, couvrant tous les domaines et les règles qui changent en début d'année ; questions sans fiche (transmission au pôle technique attendue) ; questions contenant des données fictives de clients (avertissement attendu) ; aucune donnée réelle.
- **Critères d'acceptation** : un seuil élevé de réponses exactes fixé par la présidente (par exemple 95 %, contre 80 % en mars) ; toute réponse cite une fiche ou signale son absence ; aucune fiche périmée citée ; aucune anomalie bloquante ; utilisation possible avec un logiciel de lecture d'écran.
- **Calendrier** : recette du socle fin août ; recette de chaque bureau avant sa mise en service, de septembre à décembre ; aucune recette ni mise en service du 15 janvier au 31 mai ; recette de non-régression avant toute nouvelle version, hors de cette période.

**Réponses tolérées**
- Risques cotés selon une échelle probabilité × gravité, si les trois catégories demandées sont traitées.
- Autre risque de sécurité pertinent : comptes des salariés partis encore actifs, droits trop larges sur la documentation du pôle social.
- Plan qualité présenté selon les rubriques d'un plan d'assurance qualité ou en référence à ISO 9001 (édition 2026), cité en principe.
- Seuil d'acceptation différent, s'il est justifié par l'enjeu (réponse donnée à un client) et supérieur aux résultats du pilote.

**Erreurs fréquentes**
- *Risques génériques* (`JUR-P02` facteurs clés de succès et risques) — « risque technique, risque humain » sans cause dans les annexes ni mesure.
- *Mesures de sécurité techniques détaillées* — paramétrage des équipements ou essais d'intrusion ; juste : mesures d'organisation et de contrat propres au projet (la politique de sécurité du cabinet n'est pas l'objet du dossier).
- *Recette réduite à un essai du prestataire* — sans la maîtrise d'ouvrage ni critères d'acceptation ; juste : recette fonctionnelle par les experts et les utilisateurs, procès-verbal.
- *Recette sur des données réelles de clients* — contraire à la confidentialité.
- *Maintenance limitée au logiciel* — la maintenance de la base (mise à jour des fiches) est le premier risque de ce projet.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Risques projet : identification, cotation, traitement ; maintenance corrective et évolutive | trois risques | F05 § 5 et 6 | notion de cours |
| Plan d'assurance qualité, recette, procès-verbal | plan qualité et recette | F05 § 6 | notion de cours |
| ISO 9001 — systèmes de management de la qualité (édition 2026) | réponse tolérée, en principe | `iso_9001_2026` / F05 § 6 | en vigueur |

---

### 3.5 – Appropriation et gouvernance du dispositif (2 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.e` « Leviers d'appropriation et de transformation des pratiques professionnelles » ; `1.6.c` « Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) ». Limites : « Le pilotage nécessite une approche systémique : outils, processus, culture » ; « Le lien avec la gestion des compétences (RH) est complémentaire mais distinct ».

**Annexes mobilisées** : annexes 3.3 (témoignages), 3.2 (résultats, charte, absence de date de revue), 3.1 (organisation du pôle technique), 3.4 C (maîtrise de l'IA) et 1.1 (organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Résistances analysées et classées (fiabilité, habitudes et temps, attachement au bureau, crainte de dépossession, charge et responsabilité des experts, règles floues), chacune rattachée à un témoin | 0,5 |
| a-2 | Quatre leviers, chacun en réponse à une résistance identifiée ; 0,5 dès trois leviers reliés | 0,5 |
| b-1 | Rôles des experts, des référents de bureau et des contributeurs ; règles de validation et de mise à jour des fiches | 0,5 |
| b-2 | Un indicateur complet (formule, source, fréquence, cible, axe), relié au cas | 0,5 |

**Réponse attendue**

*3.5 a) – Résistances et leviers*

Les résistances ne sont pas un refus du principe : la plupart sont rationnelles et désignent un défaut du dispositif (0,5 pt).

| Résistance | Témoin (annexe 3.3) | Nature |
|---|---|---|
| **Défiance envers la fiabilité** | Mme ROUSSELANGE : un seuil faux en mars, depuis « je vérifie tout » et j'appelle l'expert | liée à la qualité du contenu (fiches non corrigées) |
| **Habitudes et manque de temps** | M. BERLANDIN : les anciens préfèrent appeler un expert ; personne n'apprend un outil de janvier à mai | individuelle (habitude, relation) et liée au calendrier |
| **Attachement au bureau et absence de reconnaissance** | Mme LEFRANDIER : « une base conçue à Poitiers », « qui la relira, est-ce que quelqu'un le saura ? » | collective (identité du bureau, crainte d'être dépossédé de ses modèles) |
| **Crainte de voir son savoir sorti de son contexte** | M. VERDALHAC : « tout écrire ? », « une machine […] hors de leur contexte » | liée à la nature tacite de son savoir |
| **Charge et responsabilité des experts** | Mme ESCARBEL et M. PRADONNET : 400 fiches à deux, peur d'être submergés et de répondre d'une réponse non relue | organisationnelle (moyens, responsabilités) |
| **Règles floues et outil inaccessible** | M. BERLANDIN : « ai-je le droit d'y coller un extrait de dossier ? » ; collaborateur malvoyant exclu ; M. QUINTAREL : « une connexion de plus » | liée à l'outil et à l'accompagnement |

Quatre leviers (0,5 pt) :
1. **Rendre la fiabilité visible** (réponse à la défiance et à la crainte des experts) : aucune réponse sans fiche validée, date de validation affichée, question sans fiche transmise à un expert, fiche périmée retirée ; un bouton pour signaler une erreur, corrigée et suivie.
2. **Associer les bureaux et reconnaître les contributions** (réponse à Mme LEFRANDIER) : un référent dans chaque bureau ; reprise des modèles et des notes du bureau dans la base, avec leur auteur cité ; contribution reconnue (nom de l'auteur sur la fiche, présentation au comité des associés).
3. **Transmettre l'expérience par les personnes** (réponse à M. VERDALHAC) : binômes sur de vrais dossiers avec un chef de mission, qui rédige ensuite des fiches de cas avec leur contexte et leurs limites, relues par l'associé ; l'associé décide de ce qui est écrit.
4. **Former au bon moment et clarifier les règles** (réponse aux habitudes, au manque de temps et aux règles floues) : formations courtes en septembre-décembre, jamais en période fiscale ; charte d'usage claire et rappelée à l'écran (aucune donnée de client) ; mesures pour favoriser la maîtrise de l'IA du personnel, que le règlement sur l'IA demande aux déployeurs depuis le 2 février 2025, dans une rédaction assouplie par le règlement (UE) 2026/1744 (annexe 3.4 C) ; accompagnement individuel des moins à l'aise ; outil accessible et intégré à l'intranet ; exemplarité des associés, qui renvoient d'abord vers l'assistant.

*3.5 b) – Gouvernance du dispositif et indicateur*

Rôles (0,5 pt avec les règles) :
- **Commanditaire** : la présidente, qui rend compte au comité des associés de la priorité « capitaliser la connaissance technique » et arbitre les moyens (temps des experts et des référents).
- **Responsable du dispositif** : M. DUVERNAIL, associé animateur du pôle technique, propriétaire du contenu ; le chargé de mission pilote le projet et l'outil avec M. QUINTAREL (droits, journaux, relation avec le prestataire).
- **Experts du pôle technique** : définissent le modèle de fiche et les domaines, **valident** les fiches de leur domaine (second niveau), fixent les dates de revue, conduisent la revue après chaque changement de règle ; ils ne rédigent plus tout eux-mêmes.
- **Référents de bureau** (un chef de mission par bureau, avec un temps dédié) : relaient les questions de leur bureau, **relisent** les fiches proposées (premier niveau), identifient les fiches à écrire, accompagnent les collègues, remontent les erreurs.
- **Contributeurs** (collaborateurs, chefs de mission, associés) : **proposent** des fiches et des fiches de cas, signalent les erreurs, contribuent aux binômes.

Règles :
- circuit rédaction (contributeur) → relecture (référent) → validation (expert) → publication avec auteur, validateur et dates ; aucune fiche publiée sans validation ;
- date de revue sur chaque fiche (douze mois au plus) ; revue immédiate de toute fiche visée par un changement de règle, sur une liste établie par les experts dès la publication des nouveautés de fin d'année ; fiche retirée automatiquement des réponses à sa date de revue dépassée ;
- signalement d'erreur traité dans un délai fixé, plus court pour les erreurs de fond ;
- versions conservées dans la GED ; comité éditorial mensuel (experts, référents) qui fixe les priorités de rédaction à partir des questions sans fiche.

Indicateur (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Taux de fiches à jour** | nombre de fiches publiées dont la date de revue n'est pas dépassée et qui ne sont visées par aucun changement de règle non traité / nombre de fiches publiées | registre des fiches de la base (dates de validation et de revue, signalements) | mensuelle, hebdomadaire de décembre à février | au moins 98 % (environ 85 % en mars 2027 : 60 fiches inexactes sur 400, approximation faute de dates de revue) ; aucune fiche périmée citée par l'assistant, assuré par le retrait automatique | processus |

Il mesure directement la règle de mise à jour, cause première de la baisse de fiabilité et de la défiance ; il se lit avec le taux de réponses exactes et l'usage dans le compte rendu trimestriel au comité des associés.

**Réponses tolérées**
- Leviers présentés selon le modèle ADKAR (comprendre pourquoi, vouloir, savoir, pouvoir, ancrer) ou les étapes de Kotter, si chacun répond à une résistance des témoignages.
- Validation à un seul niveau (expert) avec des référents de domaine répartis entre les bureaux, si la charge des experts est traitée.
- Autre indicateur complet et relié au cas : taux de réponses exactes de l'assistant (réponses jugées exactes / réponses contrôlées sur un échantillon tiré au hasard, contrôlé par un expert qui n'a pas rédigé la fiche ; journal des questions et réponses ; mensuelle ; au moins 95 % ; axe processus) ; part des collaborateurs actifs (utilisateurs dans le mois / salariés ayant accès ; journal ; mensuelle ; par exemple 80 % hors période fiscale ; axe apprentissage) ; part des questions au pôle technique portant sur un sujet déjà couvert par une fiche (axe processus) ; nombre de fiches proposées par les bureaux (axe apprentissage).

**Erreurs fréquentes**
- *Résistances traitées comme de l'irrationnel* (`JUR-P04` conduite du changement adaptée) — « il faut convaincre les anciens » ; juste : la défiance vient d'erreurs réelles, la première réponse est la fiabilité.
- *Leviers génériques* (`JUR-T08` exploiter les témoignages) — « communiquer, former » sans lien avec un témoin.
- *Obligation imposée comme seul levier* — « interdire d'appeler les experts » ; juste : rendre l'outil plus utile que l'appel, garder l'expert pour ce qui n'a pas de fiche.
- *Gouvernance réduite à l'outil* (`ET-21`) — « paramétrer des droits » ; juste : rôles, circuit de validation, règles de mise à jour.
- *Indicateur incomplet ou d'activité seule* (`JUR-A02` ; `ET-18`) — « nombre de fiches » sans cible ni lien avec la qualité.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gouvernance d'un dispositif de gestion des connaissances : rôles, règles, indicateurs | gouvernance | F06 § 2.2 | notion de cours |
| Leviers d'appropriation | quatre leviers | F06 § 2.3 ; F05 § 7 | notion de cours |
| ADKAR (Prosci ; Hiatt) | réponse tolérée | `adkar` / F05 § 7 | modèle publié |
| Règlement (UE) 2024/1689 sur l'IA, modifié par le règlement (UE) 2026/1744 : maîtrise de l'IA (article 4) | levier de formation (annexe 3.4 C) | `ai_act`, `omnibus_numerique_ia` / F13 § 4 et § 5.2 | en vigueur |
| Fiche d'indicateur à cinq champs | indicateur | F09 § 4 | notion de cours |

---

### 3.6 – Choix du service d'IA et transition numérique responsable (1,5 point)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : « La transformation numérique responsable nécessite une approche transversale et non cloisonnée » ; « La durabilité doit être intégrée dans la gouvernance globale du SI, et non comme ajout marginal ».

**Annexes mobilisées** : annexes 3.4 B (deux options) et C (repères), 3.3 (collaborateur malvoyant, anciens, M. QUINTAREL), 3.2 (réponses sans fiche, données des clients) et 1.1 (secret professionnel).

**Barème indicatif (1,5 pt)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Transition numérique responsable définie et option appréciée sous l'angle de la sobriété du modèle et des usages (consommation estimée cinq fois moindre, à vérifier ; fonctions inutiles au besoin) | 0,5 |
| 2 | Angles de l'éthique et de la transparence envers les clients, et de l'inclusion des collaborateurs, appliqués aux deux options | 0,5 |
| 3 | Recommandation justifiée d'une option et deux règles d'usage de l'assistant | 0,5 |

**Réponse attendue**

Une **stratégie de transition numérique responsable** conduit l'évolution du SI en intégrant, dès les choix, la sobriété (questionner le besoin avant d'optimiser), la réduction de l'empreinte environnementale (modèles et hébergements adaptés, centres de données sobres et transparents), l'éthique et l'inclusion ; elle relève de la gouvernance du SI et non d'un ajout final (F14 § 3 et 5) (0,5 pt avec l'angle de la sobriété).

| Angle | Option 1 – Modèle généraliste hors de l'Union européenne | Option 2 – Modèle plus petit hébergé en France |
|---|---|---|
| **Sobriété du modèle et des usages** | estimée à 10 MWh par an, cinq fois plus que l'option 2, pour la même exactitude (85 %) sur les questions couvertes par une fiche ; fonctions sans lien avec le besoin (courriers, résumés de dossiers, traductions) qui multiplient les usages et l'effet rebond ; aucune donnée publiée sur ses centres de données | modèle dimensionné au besoin réel (rechercher et citer une fiche), environ 2 MWh par an ; données d'énergie et d'origine de l'électricité publiées ; dans les deux cas, estimations du prestataire à faire justifier (méthode non communiquée) et à mesurer |
| **Éthique et transparence envers les clients** | questions conservées 30 jours par un fournisseur hors de l'Union européenne alors que 15 % des questions relues contenaient des données de clients couvertes par le secret professionnel ; réponse produite sans fiche, plausible mais non validée, présentée comme une réponse du cabinet | questions effacées, traitement en France ; absence de fiche dite clairement et transmise à un expert : l'outil n'invente pas ; le cabinet peut expliquer à ses clients qu'il s'appuie sur un assistant de recherche documentaire dont chaque réponse repose sur sa doctrine validée et reste sous la responsabilité d'un professionnel |
| **Inclusion des collaborateurs** | dans les deux options, l'interface doit être utilisable avec un logiciel de lecture d'écran (collaborateur malvoyant de Niort) et les collaborateurs moins à l'aise doivent être formés et accompagnés ; l'expert reste joignable : l'assistant ne doit pas devenir le seul accès à la connaissance | la transmission des questions sans fiche au pôle technique garde un interlocuteur humain, attendu par les plus anciens |

(0,5 pt pour l'éthique et l'inclusion appliquées.)

**Recommandation** (0,5 pt) : l'**option 2**. Elle répond au besoin documentaire avec la même exactitude, une consommation estimée bien moindre, des données qui restent en France sans conservation, un comportement honnête quand la base ne sait pas, et un coût inférieur (120 k€ sur trois ans contre 150 k€). Conditions : clauses du contrat sur la non-conservation des questions, l'information préalable sur les changements de version et la communication annuelle de la consommation mesurée ; accessibilité vérifiée à la recette ; filtrage par le référent du bureau des questions sans fiche avant leur transmission au pôle technique : au taux de mars (20 %), 3 000 questions par mois en produiraient jusqu'à 600, pour deux experts qui en reçoivent déjà 300 à 500 ; le comité éditorial fixe les priorités de rédaction, et la couverture de la base fait baisser ce flux (le candidat qui relève cette charge est valorisé). Deux règles d'usage :
1. **Aucune donnée permettant d'identifier un client** (nom, numéro d'identification, montants tirés d'un dossier) dans une question : la question porte sur la règle, pas sur le dossier.
2. **L'assistant cherche dans la doctrine validée ; il ne rédige pas pour le client** : toute réponse utilisée dans un conseil est vérifiée sur la fiche citée par le collaborateur, qui en répond ; aucun courrier ni document destiné à un client n'est produit par l'assistant.

**Réponses tolérées**
- Option 1 retenue si le candidat exige au contrat l'absence de conservation, la désactivation des fonctions inutiles, la suppression des réponses sans fiche et des données sur la consommation, et justifie le surcoût.
- Autre règle d'usage pertinente : réserver l'assistant aux questions professionnelles et éviter les demandes répétées ; signaler toute erreur ; mentionner au client, si la question est posée, l'usage d'un assistant de recherche.
- Référence au référentiel général d'écoconception de services numériques (RGESN, version 2024), thème de l'algorithmie et de l'IA, ou à la qualification SecNumCloud pour l'hébergement, si elle reste illustrative.

**Erreurs fréquentes**
- *Sobriété réduite à l'économie d'énergie* (`ET-12`) — comparer seulement les MWh ; juste : d'abord le besoin (une recherche documentaire n'exige ni courriers ni résumés), puis la consommation.
- *Chiffres d'un prestataire pris pour des mesures* — 10 et 2 MWh sont des estimations sans méthode connue : les faire justifier et mesurer.
- *Calcul d'empreinte* — conversion en émissions : non demandée.
- *Hébergement « souverain » assimilé à la seule localisation* (`ET-37`) — la nationalité du fournisseur et la conservation des données comptent autant que le lieu.
- *Qualification de l'assistant au regard du règlement sur l'IA* — non attendue (annexe 3.4 C) ; juste : éthique, transparence et responsabilité du professionnel.
- *Inclusion oubliée ou réduite à la formation* — l'accessibilité de l'outil et le maintien d'un interlocuteur humain font partie de la réponse.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Sobriété numérique, Green IT, effet rebond ; IA et modèles adaptés à la tâche | angle de la sobriété | F14 § 1 et 3 ; F13 § 3 | notion de cours |
| Cloud et centres de données, transparence des fournisseurs | choix d'hébergement | F14 § 5 | notion de cours |
| RGESN, version 2024 | réponse tolérée | `rgesn_2024` / F14 § 2 | en vigueur |
| SecNumCloud, version 3.2 (ANSSI) | réponse tolérée | `secnumcloud_3_2` / F12 | en vigueur |
| Gouvernance de l'IA : transparence, validation humaine, charte | règles d'usage | F13 § 4 | notion de cours |
