# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 43 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique (§ 2, chaîne de valeur), F02 gouvernance et référentiels (§ 6, comitologie), F04 relations avec les ESN et contrats (§ 3, TCO comparé ; § 6, dépendance), F06 gestion des connaissances, F09 performance du SI (§ 3, TCO ; § 4, tableau de bord), glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 CIRCÉA dans la chaîne de valeur et la stratégie du système d'information | `1.1.b` Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 4 |
| 1.2 Le coût complet des deux options pour la plateforme | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord | 3 |
| 1.3 La gouvernance et le tableau de bord du système d'information | `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ; `1.2.e` Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) | 3,5 |
| 1.4 La base de connaissances des interventions | `1.6.b` Architecture fonctionnelle des systèmes de knowledge management ; `1.6.c` Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) | 3,5 |
| **Dossier 1 – Préparer les choix stratégiques et le pilotage du système d'information** |  | **14** |

Répartition indicative : connaissances (chaîne de valeur, stratégie du SI, coût complet, gouvernance du SI, architecture fonctionnelle d'un système de gestion des connaissances) environ 2,5 points (items 1.1 a-1, 1.1 b-1, 1.2 a-1, 1.3 a-1, 1.4 a-1) ; analyse des annexes et recommandations environ 11,5 points, soit environ 82 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – CIRCÉA dans la chaîne de valeur et la stratégie du système d'information (4 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.b` « Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 1.2 (activités et apports de CIRCÉA, constats chiffrés, faits complémentaires, témoignages du représentant de VARNEDAL Infrastructures, du directeur technique et de la directrice du développement du réseau) et 1.1 (activité, effectif de la direction technique, système d'information).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de valeur définie (Porter, 1985 : activités principales et de soutien dont l'enchaînement crée la valeur et la marge) ; rôle du SI : il automatise, informe et transforme chaque activité et relie les activités entre elles et avec les partenaires | 0,5 |
| a-2 | CIRCÉA située : présente dans cinq des six activités principales (installation et mise en service, exploitation et maintenance, vente de la recharge, relation avec les conducteurs, services aux sites hôtes), absente de la recherche des sites ; dans les activités de soutien, elle est elle-même le développement technologique de l'opérateur, elle sert les achats (mise en concurrence des constructeurs) et les finances | 0,5 |
| a-3 | Source d'avantage concurrentiel démontrée par les chiffres de l'annexe 1.2 et rattachée aux objectifs du plan : 70 % de pannes résolues à distance contre environ la moitié, un constructeur intégré en deux mois contre six à neuf, tarification variable construite en cinq mois, mise en service en deux jours | 0,5 |
| a-4 | Limites de cet avantage : il ne couvre pas les services aux sites hôtes (accès en ligne attendu depuis un an, client perdu, délai de six mois, 10 % du temps de l'équipe), il est fragile (documentation incomplète, départs, priorités non arbitrées, la moitié des points sous 98 %) ; conclusion nuancée | 0,5 |
| b-1 | Stratégie du SI définie (orientations à moyen terme du SI, déduites de la stratégie de l'entreprise, qui guident les choix d'applications, de données, d'organisation et de partenaires) ; elle n'est pas un choix technique | 0,5 |
| b-2 | Première orientation, justifiée par un objectif d'« AMPÉRANE 2030 » et par un constat des annexes | 0,5 |
| b-3 | Deuxième orientation, même exigence | 0,5 |
| b-4 | Troisième orientation, même exigence ; les trois orientations découlent de l'analyse du a) | 0,5 |

**Réponse attendue**

*1.1 a) – CIRCÉA dans la chaîne de valeur et l'avantage concurrentiel*

La **chaîne de valeur** (Porter, 1985) décompose l'entreprise en **activités principales**, qui concourent directement à produire et à vendre l'offre, et en **activités de soutien** (infrastructure de l'entreprise, ressources humaines, développement technologique, achats), qui les rendent possibles ; l'avantage concurrentiel naît de la manière dont chaque activité est conduite et dont les activités s'enchaînent. Le **système d'information** y joue trois rôles : il **automatise** (productivité), il **informe** (pilotage) et il **transforme** (nouveaux services) chaque activité ; il **relie** les activités entre elles et l'entreprise à ses partenaires (0,5 pt).

**CIRCÉA dans les activités d'AMPÉRANE** (0,5 pt) :

| Activité | Nature | Apport de CIRCÉA (annexe 1.2 A) |
|---|---|---|
| Recherche et contractualisation des sites | principale | aucun : logiciel de relation clients et tableurs |
| Installation et mise en service | principale | configuration et essais à distance, ouverture à la vente deux jours après les travaux |
| Exploitation et maintenance | principale | supervision jour et nuit, commande à distance, codes d'erreur, micrologiciels : 70 % des pannes réglées sans déplacement |
| Vente de la recharge | principale | tarifs, sessions, itinérance ; tarification variable en pilote |
| Relation avec les conducteurs | principale | points libres en temps réel dans l'application, état des bornes pour le service clients |
| Services aux sites hôtes | principale | partage des recettes et rapport standard, mais ni rapports adaptés ni accès en ligne |
| Développement technologique | soutien | CIRCÉA **est** cette activité : 60 des 110 personnes de la direction technique |
| Achats | soutien | mise en concurrence des constructeurs (quatrième constructeur intégré en deux mois) |
| Infrastructure (finances) | soutien | sessions et recettes transmises au progiciel de gestion intégré |

CIRCÉA est donc la **colonne vertébrale** des activités principales situées après la signature du site : elle relie l'installation, l'exploitation, la vente et la relation avec les conducteurs.

**Une source d'avantage concurrentiel, réelle mais incomplète et fragile** (0,5 pt + 0,5 pt) :
- *Ce qui distingue AMPÉRANE.* Une ressource est une source d'avantage quand elle apporte une performance que les concurrents n'obtiennent pas aisément. C'est le cas sur trois points chiffrés, chacun lié à un objectif du plan : 70 % des pannes résolues à distance, contre environ la moitié chez les opérateurs comparables équipés d'une solution du marché, ce qui sert la **disponibilité de 98 %** (un point de disponibilité vaut environ 1 M€ de ventes par an, selon le directeur financier) ; un nouveau constructeur intégré en **deux mois** contre six à neuf, ce qui laisse AMPÉRANE libre de ses achats pour ajouter 12 000 points d'ici 2030 (**20 000 points**) ; un module de **tarification variable** construit en cinq mois (**généralisation en 2027**). Cet avantage repose sur des savoirs difficiles à imiter : la connaissance fine des bornes et des micrologiciels de chaque constructeur.
- *Ce qui le limite.* CIRCÉA ne crée pas d'avantage sur la **recherche des sites** ni sur les **services aux sites hôtes**, qui portent l'objectif de **nouvelles recettes** : l'accès en ligne attendu depuis un an n'existe pas, une chaîne de quarante hôtels est partie chez un concurrent, 45 demandes attendent en moyenne six mois et 10 % seulement du temps de l'équipe leur a été consacré. L'avantage est en outre **fragile** : documentation incomplète, deux départs de développeurs expérimentés, priorités tranchées par le seul directeur technique ; et il ne suffit pas encore, puisque la disponibilité moyenne est de 97 % et que la moitié des points est sous 98 %.

**Conclusion** : CIRCÉA est une source d'avantage concurrentiel sur le **cœur du métier d'opérateur** (exploitation, disponibilité, vente et tarification, intégration des constructeurs), non sur les services aux sites hôtes ; l'avantage tient autant à l'équipe et à son pilotage qu'au logiciel, ce qui prépare la question du choix de la plateforme (1.2) et de sa gouvernance (1.3).

*1.1 b) – Trois orientations de la stratégie du système d'information*

La **stratégie du système d'information** fixe, pour plusieurs années, les orientations du SI déduites de la stratégie de l'entreprise : elle guide les choix d'applications, de données, d'organisation, de compétences et de partenaires, puis se traduit en projets. Elle n'est pas un choix technique : chaque orientation sert un objectif d'« AMPÉRANE 2030 » (0,5 pt).

**Trois orientations** (0,5 pt chacune ; trois parmi les suivantes) :

| Orientation | Constat de l'annexe 1.2 | Objectif d'« AMPÉRANE 2030 » servi |
|---|---|---|
| **Faire de CIRCÉA le socle différenciant de la disponibilité et de la croissance** : renforcer le diagnostic et la commande à distance, garder la capacité d'intégrer vite de nouveaux constructeurs, préparer la plateforme à 20 000 points | 70 % des pannes réglées à distance ; constructeur intégré en deux mois ; moitié des points sous 98 % | disponibilité de 98 % par point ; 20 000 points en 2030 |
| **Généraliser la tarification variable en 2027 sur la plateforme existante**, sans rupture de plateforme pendant l'année | module construit en cinq mois, en pilote depuis fin 2026 | tarification variable généralisée en 2027 |
| **Ouvrir le SI aux sites hôtes** : accès en ligne à leurs chiffres, rapports adaptés à chaque type de site, partage des recettes visible ; outiller aussi la recherche des 450 sites par an | demandes en attente depuis un an ; chaîne d'hôtels perdue ; CIRCÉA absente de la recherche des sites | nouvelles recettes des services aux sites hôtes ; 20 000 points |
| **Concentrer le développement interne sur ce qui distingue et acheter le reste** : solutions du marché pour la relation clients, la gestion et les interventions (déjà le cas), développement interne réservé au cœur ; documenter et sécuriser ce cœur | 60 personnes sur CIRCÉA ; documentation incomplète ; départs | 20 000 points (montée en charge maîtrisée) ; SI « sûr, documenté et piloté » demandé par les fonds |
| **Mesurer et réduire l'énergie consommée par le réseau numérique** (bornes en veille, hébergement), à partir des mesures que CIRCÉA peut remonter | — (annexe 1.4) | réduction de l'empreinte environnementale |

**Réponses tolérées**
- Chaîne de valeur présentée sous forme de schéma, ou activités principales découpées autrement (par exemple « développement du réseau » regroupant recherche, contractualisation et installation), si CIRCÉA y est située et l'analyse appuyée sur les chiffres.
- Conclusion selon laquelle CIRCÉA n'est pas, ou plus, une source d'avantage concurrentiel, si elle est argumentée par les limites de l'annexe 1.2 (fragilité, services aux sites hôtes, disponibilité moyenne de 97 %) et par le témoignage du représentant de VARNEDAL Infrastructures.
- Distinction entre ressources stratégiques, à garder en interne, et ressources banalisées, à acheter : valorisée.
- Référence au modèle SAM (Henderson et Venkatraman, 1993) pour qualifier l'alignement : valorisée sans être exigée ; elle ne remplace pas la chaîne de valeur demandée.
- Autres orientations, si elles sont justifiées par un objectif du plan et un constat de l'annexe.

**Erreurs fréquentes**
- *Chaîne de valeur récitée sans y placer CIRCÉA* (`JUR-T01` contextualiser chaque notion, pas de morceau de cours) — la liste des activités de Porter sans le tableau du cas ne rapporte rien.
- *CIRCÉA rangée dans les seules activités de soutien* (`JUR-T03` analyser et argumenter) — elle porte l'exploitation, la vente et la relation avec les conducteurs, qui sont des activités principales ; elle est aussi le développement technologique.
- *Avantage concurrentiel affirmé sans chiffres ni nuance* (`JUR-T08` exploiter toutes les annexes) — le témoignage du directeur technique est un plaidoyer ; les faits complémentaires (délais, priorités, départs) le nuancent.
- *Orientations réduites à des choix techniques* (ET-06, `JUR-G02` alignement réduit à un choix technique ou à une standardisation logicielle) — « passer au cloud », « acheter un logiciel du marché » ; juste : une orientation qui sert un objectif du plan.
- *Schéma directeur ou feuille de route construits* (`JUR-T07` répondre à la seule question posée) — non demandés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de valeur (Porter, 1985) | activités principales et de soutien ; le SI automatise, informe, transforme et relie les activités | F01 § 1 et § 2 | notion de cours |
| Stratégie du SI et alignement | orientations déduites de la stratégie ; pas une adéquation technique | F01 § 1 ; `erreurs_types.md` ET-06 | notion de cours |
| Henderson et Venkatraman, 1993 (modèle SAM) | réponse tolérée | F01 § 1 | publié |

---

### 1.2 – Le coût complet des deux options pour la plateforme (3 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI » ; `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord ». Limite : « Le pilotage stratégique par les indicateurs suppose une capacité de recul critique. »

**Annexes mobilisées** : annexes 1.3 (hypothèses, coûts des deux options, informations complémentaires), 1.2 (apports de CIRCÉA, valeur d'un point de disponibilité, témoignages) et 1.1 (dépenses du SI, chiffre d'affaires).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Coût complet défini (coût total de possession, TCO : ensemble des coûts d'un système sur sa durée de vie, acquisition, mise en œuvre, exploitation, utilisation, sortie, y compris les coûts cachés) ; il ne se réduit pas au prix d'achat ou de l'abonnement | 0,5 |
| a-2 | Comparaison de tête : option A 28 000 k€ ; option B 20 000 k€ ; écart visible de 8 000 k€ en faveur de B | 0,5 |
| a-3 | Trois coûts cachés pertinents tirés de l'annexe 1.3 D, dont au moins un non chiffrable (perte de compétences, dépendance à l'éditeur, tarifs selon l'affluence reportés à 2029, abonnement qui croît après 2030) | 0,5 |
| a-4 | Chiffrage de la double exploitation en 2027 (20 personnes × 80 k€ + 1 200 k€ d'hébergement = 2 800 k€) et de l'adaptation des deux constructeurs non reconnus (2 × 500 = 1 000 k€) ; coût corrigé de B : 23 800 k€ ; écart ramené à 4 200 k€, environ 1 M€ par an | 0,5 |
| b-1 | Recommandation argumentée qui croise le coût (environ 1 M€ par an d'écart) et l'enjeu stratégique (disponibilité, tarification variable en 2027, intégration des constructeurs, dépendance) | 0,5 |
| b-2 | Réponse à l'argument de M. TREVÉLOC et conditions de l'option retenue (gouvernance des priorités, documentation, achat du marché pour ce qui ne distingue pas, revue du choix) | 0,5 |

**Réponse attendue**

*1.2 a) – Le coût complet des deux options et leurs coûts cachés*

Le **coût complet**, ou **coût total de possession** (TCO, notion popularisée par Gartner), est l'ensemble des coûts qu'entraîne un système d'information sur sa durée de vie : acquisition ou développement, mise en œuvre (migration, interfaces, paramétrage, formation), exploitation (hébergement, maintenance, équipe, sécurité), utilisation (pertes de productivité, indisponibilités) et sortie (réversibilité). Il inclut les **coûts cachés**, ceux qu'un devis ou un tableau ne montre pas. Il ne se confond pas avec le prix de l'abonnement ou de la licence (0,5 pt).

**Comparaison de tête sur 2027-2030** (0,5 pt), en k€ :
- Option A : 19 200 + 2 600 + 5 600 + 600 = **28 000** ;
- Option B : 8 400 + 8 000 + 2 000 + 1 200 + 300 + 100 = **20 000** ;
- écart visible : **8 000 k€** en faveur de B, soit 2 000 k€ par an : c'est l'argument du représentant de VARNEDAL Infrastructures.

**Trois coûts cachés** (0,5 pt ; trois parmi les suivants, dont au moins un non chiffrable) :

| Coût caché | Source (annexe 1.3 D) | Estimation de tête |
|---|---|---|
| **Double exploitation pendant la migration** : l'offre suppose 25 personnes dès janvier 2027, mais CIRCÉA doit rester exploitée, corrigée et sécurisée toute l'année pour les points non migrés | point 1 ; hébergement 2027 (annexe 1.3 B) | 20 personnes de plus × 80 k€ = 1 600 k€, plus 1 200 k€ d'hébergement de CIRCÉA en 2027 : **2 800 k€** |
| **Adaptation des interfaces des constructeurs** non reconnus par la solution | point 2 | 2 × 500 = **1 000 k€** |
| **Tarifs selon l'affluence reportés à 2029** et évolutions gelées pendant la migration | points 3 et 4 | non chiffré : manque à gagner sur l'objectif de 2027 |
| **Dépendance à l'éditeur** : prix révisable chaque année, évolutions décidées pour quarante clients, nouveau modèle de borne intégré en six à neuf mois, export des données dans le format de l'éditeur (une réversibilité à 100 k€ ne couvre pas un changement de plateforme) | points 4 et 5 | non chiffré ; coût de sortie élevé |
| **Perte de compétences** : départ des développeurs qui connaissent les défauts des micrologiciels de chaque constructeur | point 6 ; annexe 1.2 B | non chiffré : risque sur la résolution à distance (70 % contre environ la moitié) |
| **Abonnement qui croît avec le réseau** au-delà de l'horizon | point 7 ; annexe 1.3 C | 20 000 points × 150 € = **3 000 k€ par an** après 2030 |
| Formation probablement sous-estimée (300 k€ pour trois équipes, dont un centre de supervision ouvert jour et nuit) | annexe 1.3 C | non chiffré |

**L'écart qui en résulte** (0,5 pt) : avec les deux coûts chiffrables, le coût de B passe à 20 000 + 2 800 + 1 000 = **23 800 k€** : l'écart avec A tombe à **4 200 k€** sur quatre ans, soit **environ 1 M€ par an** (moins de 1 % du chiffre d'affaires), avant les coûts non chiffrables.

*1.2 b) – La recommandation*

**Recommandation : l'option A, garder et renforcer CIRCÉA, à condition de la gouverner** (0,5 pt). L'écart de coût d'environ 1 M€ par an est du même ordre que la valeur d'**un seul point de disponibilité** (environ 1 M€ de ventes par an, annexe 1.2 B). Or l'option B fait courir un risque sur les trois sources de l'avantage concurrentiel établies au 1.1 : la résolution à distance (70 % contre environ la moitié chez les opérateurs équipés d'une solution du marché), la **tarification variable selon l'affluence**, que le plan veut généraliser en 2027 alors que l'éditeur l'annonce pour 2029 et que la migration gèle toute évolution en 2027, et la **liberté d'achat des bornes** (deux mois contre six à neuf pour un nouveau constructeur, au moment d'ajouter 12 000 points). L'option B concentre en outre la migration de 8 000 points sur l'année où le réseau doit gagner 3 000 points et où la tarification doit être généralisée.

**Réponse à M. TREVÉLOC et conditions** (0,5 pt) : il a raison sur un point, un opérateur n'a pas à tout développer. AMPÉRANE achète déjà des solutions du marché pour la relation clients, la gestion et les interventions ; elle doit réserver le développement interne au **cœur différenciant** (supervision, diagnostic, tarification, intégration des constructeurs) et acheter le reste. Mais l'économie visible de 8 000 k€ est surestimée de près de moitié, et elle se paierait en disponibilité, en recettes et en dépendance. Conditions de l'option A : une **gouvernance des priorités** de l'équipe (question 1.3), une **documentation** complète et la réduction de la dépendance à quelques développeurs, le renforcement de la sécurité prévu au budget, un **suivi des coûts** de la plateforme dans le tableau de bord, et une **revue du choix** en 2029, quand les solutions du marché auront peut-être rattrapé leur retard. Le choix, investissement important, est soumis pour avis au comité de surveillance.

**Réponses tolérées**
- Recommandation de l'option B, si elle est argumentée et conditionnée : migration engagée après la généralisation de la tarification variable, adaptation des constructeurs et équipe de transition budgétées, export des données dans un format ouvert, plafonnement de la révision du prix, maintien d'une compétence interne de pilotage.
- Solution intermédiaire (garder CIRCÉA pour le cœur et acheter une brique du marché pour les rapports et l'accès en ligne des sites hôtes), si elle est justifiée.
- Autres coûts cachés pertinents (indisponibilités pendant la migration, coût de la reprise des données, temps des équipes métiers), s'ils sont tirés des annexes.
- Coûts cachés de l'option A tirés des annexes (dépendance à quelques développeurs après deux départs, documentation à reconstituer, difficulté à recruter les dix renforts), s'ils sont argumentés.
- Distinction entre dépenses d'investissement et de fonctionnement (l'option B transforme l'essentiel du coût en abonnement) : valorisée sans être exigée.

**Erreurs fréquentes**
- *Coût complet réduit au prix de l'abonnement* (ET-33, TCO égal au prix d'achat) — 8 400 k€ d'abonnement ne sont que 42 % du coût visible de B.
- *Comparaison arrêtée aux totaux du tableau* (`JUR-T08` exploiter toutes les annexes) — les informations complémentaires de l'annexe 1.3 D changent l'écart de près de moitié.
- *Calcul financier élaboré ou taux appliqué aux flux* (`JUR-T07` répondre à la seule question posée) — l'énoncé demande une addition de tête ; aucun autre calcul n'est attendu.
- *Recommandation fondée sur le seul coût* (`JUR-A03` indicateurs de coûts dans une logique ouverte, coût d'opportunité compris ; ET-06) — l'enjeu stratégique (disponibilité, tarification, dépendance) doit être mis en regard.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Coût total de possession (TCO) | postes du coût complet, coûts cachés, comparaison de scénarios en sommes rondes | F09 § 3.1 ; F04 § 3 (exemple vérifié « TCO comparé ») | notion de cours |
| Dépendance à un fournisseur | coûts de sortie, formats propriétaires, compétences perdues | F04 § 6 | notion de cours |

---

### 1.3 – La gouvernance et le tableau de bord du système d'information (3,5 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité » ; `1.2.e` « Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) ». Limite : « Le pilotage ESG est à comprendre dans une logique d'indicateurs intégrés, non isolés. »

**Annexes mobilisées** : annexes 1.4 (tableau mensuel, constats, questionnaire ESG des fonds, demande de la présidente), 1.2 (demandes en attente, répartition du temps de l'équipe, disponibilité) et 1.1 (organigramme, comité de surveillance, effectif).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance du SI définie (instances, rôles et règles par lesquels la direction s'assure que le SI sert la stratégie, alloue les ressources et surveille la performance et les risques : évaluer, diriger, surveiller), distinguée de la gestion courante ; appliquée aux trois constats de l'annexe 1.4 | 0,5 |
| a-2 | Instance d'arbitrage : composition (présidente, cinq responsables de direction et de service, directeur(rice) de cabinet), fréquence (mensuelle pour les demandes, trimestrielle pour la revue), décisions (priorités selon des critères liés au plan, répartition de la capacité de l'équipe de CIRCÉA, préparation des décisions majeures) ; fin des demandes directes aux développeurs | 0,5 |
| a-3 | Information du comité de surveillance (point SI trimestriel, tableau de bord, avis sur le choix de la plateforme) et rôles : présidente (arbitre en dernier ressort, rend compte), directions (expriment et priorisent, valident), direction technique (propose et éclaire, ne tranche plus seule), fonds (avis par le comité de surveillance, sans pilotage direct) | 0,5 |
| b-1 | Deux indicateurs complets hors ESG, reliés au plan et aux constats (par exemple part des points à 98 % de disponibilité, délai de réalisation des évolutions arbitrées) | 0,5 |
| b-2 | Deux indicateurs ESG complets tirés du questionnaire des fonds (par exemple consommation d'électricité du SI par point, part de femmes dans les équipes techniques) | 0,5 |
| b-3 | Limites du tableau mensuel actuel (moyenne qui masque les points sous 98 %, dépenses sans lien avec la valeur, ni demandes ni ESG) ; tableau de bord défini et structuré : axes du tableau de bord équilibré avec les indicateurs ESG intégrés et non isolés, deux destinataires (comité de direction chaque mois, comité de surveillance chaque trimestre) | 0,5 |
| b-4 | Trois mesures pour fiabiliser les réponses au questionnaire, chacune reliée à une réponse de l'annexe 1.4 | 0,5 |

**Réponse attendue**

*1.3 a) – La gouvernance du système d'information*

La **gouvernance du SI** est l'ensemble des instances, des rôles et des règles par lesquels la direction s'assure que le système d'information sert la stratégie, que ses ressources sont allouées aux priorités et que sa performance et ses risques sont surveillés. Selon l'ISO/IEC 38500 (édition 2024), les dirigeants **évaluent**, **dirigent** et **surveillent** ; COBIT 2019 distingue de même la gouvernance (fixer les objectifs, arbitrer, contrôler) de la gestion (planifier, construire, exploiter). Chez AMPÉRANE, les trois fonctions manquent : personne n'arbitre (le directeur technique tranche seul « selon l'urgence »), la présidente ne dispose que de deux chiffres, le comité de surveillance ne reçoit rien (0,5 pt).

**L'instance d'arbitrage : un comité du numérique** (0,5 pt) :

| Élément | Proposition |
|---|---|
| Composition | présidée par Mme SORBADIÈRE ; M. QUÉLAVEC (direction technique), Mme FOLCARIAS (exploitation et maintenance), Mme ESCARDINE (développement du réseau), M. TÉVENARD (service clients), M. MANTRELLE (direction administrative et financière) ; le (la) directeur(rice) de cabinet prépare les séances et tient le portefeuille des demandes ; les responsables de la sécurité ou des données sont invités selon l'ordre du jour |
| Fréquence | mensuelle pour l'arbitrage des demandes ; trimestrielle pour une revue stratégique, deux semaines avant chaque comité de surveillance |
| Décisions | classe les 45 demandes en attente et les nouvelles selon des critères annoncés (contribution aux cinq objectifs du plan, effet sur la disponibilité et sur les recettes, risque, coût) ; répartit la capacité de l'équipe de CIRCÉA entre le plan, l'exploitation et la sécurité, et le développement du réseau (au lieu de 10 % subis en 2026) ; suit le tableau de bord ; prépare les décisions majeures (choix de la plateforme, dépenses annuelles du SI) |
| Règle de fonctionnement | toute demande passe par le portefeuille ; seuls les incidents d'exploitation urgents vont directement à l'équipe, et ils sont rapportés au comité suivant |

**L'information du comité de surveillance et les rôles** (0,5 pt) :
- **Comité de surveillance** : un point « système d'information » à chacune de ses quatre séances annuelles, avec le tableau de bord (b), l'avancement des orientations (1.1 b), les principaux risques et les décisions majeures ; **avis préalable** sur le choix de la plateforme, qui est un investissement important, comme l'a demandé M. TREVÉLOC.
- **La présidente** : sponsor du SI, elle arbitre en dernier ressort, valide les priorités et rend compte au comité de surveillance.
- **Les directions** : elles expriment et justifient leurs demandes, les priorisent dans leur périmètre et valident ce qui est livré ; elles sont propriétaires de leurs processus et de leurs données.
- **La direction technique** : elle propose l'architecture, éclaire la faisabilité, le coût et le risque de chaque demande, répond de l'exploitation et de la sécurité de CIRCÉA ; elle ne tranche plus seule les priorités.
- **La direction administrative et financière** : elle suit les coûts du SI et fiabilise les indicateurs, dont ceux du questionnaire ESG.
- **Les fonds** : ils donnent leur avis au comité de surveillance sur la stratégie et les investissements importants et reçoivent une information régulière ; ils ne pilotent pas les équipes. Leur demande d'un SI « sûr, documenté et piloté » devient un critère d'arbitrage.

*1.3 b) – Le tableau de bord du système d'information et la fiabilité des réponses aux fonds*

Un **tableau de bord du SI** est un ensemble limité d'indicateurs, reliés aux objectifs de l'entreprise et assortis de cibles, qui permet à ses destinataires de piloter le SI et d'agir. Le tableau actuel est trop pauvre : une **moyenne** de 97 % masque la moitié des points sous 98 %, alors que le plan vise 98 % **par point** ; les dépenses sont suivies sans lien avec la valeur produite ; rien sur les demandes, ni sur l'ESG. Le tableau de bord proposé suit les axes du **tableau de bord équilibré** appliqué au SI (finances, clients et utilisateurs, processus, apprentissage), auxquels les indicateurs **ESG sont intégrés** et reliés aux objectifs du plan, et non ajoutés en liste séparée. Il sert deux destinataires : le **comité de direction** chaque mois (une dizaine d'indicateurs au plus) et le **comité de surveillance** chaque trimestre (une sélection, les mêmes données). Il alimente directement le questionnaire des fonds (0,5 pt).

**Quatre indicateurs** (0,5 pt pour deux indicateurs hors ESG, 0,5 pt pour deux indicateurs ESG) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des points de recharge à au moins 98 % de disponibilité | points dont la disponibilité du mois atteint 98 % / points en service × 100 | CIRCÉA (états des bornes enregistrés par la supervision) | mensuelle au comité de direction, trimestrielle au comité de surveillance | au moins 75 % fin 2027, 100 % en 2030 (environ la moitié en 2026) | processus |
| Délai moyen de réalisation des évolutions arbitrées | somme des jours entre la décision du comité du numérique et la mise en service / nombre d'évolutions mises en service | portefeuille des demandes du comité du numérique | mensuelle | au plus trois mois fin 2027 (six mois entre la demande et la réalisation en 2026) | client (directions et sites hôtes) |
| Consommation d'électricité du système d'information par point de recharge | (énergie consommée par les bornes en veille, mesurée par les bornes + électricité de l'hébergement déclarée par l'hébergeur) / points en service | mesures des bornes remontées par CIRCÉA ; relevé de l'hébergeur, à exiger | trimestrielle | mesure de référence en 2027, puis baisse de 10 % par point d'ici 2030 | environnement |
| Part de femmes dans les équipes techniques | femmes de la direction technique et techniciennes / effectif de ces équipes × 100 | logiciel de paie | semestrielle | 25 % en 2030 (18 % en 2026) | social |

**Trois mesures pour fiabiliser les réponses au questionnaire** (0,5 pt ; trois parmi les suivantes) :
- **Un responsable et une fiche de définition par question** (formule, périmètre, source, méthode, date de mesure) : aujourd'hui les réponses sont rassemblées à la main, en trois semaines, à partir de tableurs, sans définition écrite ni responsable désigné par question.
- **Mesurer à la source plutôt qu'estimer** : l'énergie des bornes en veille mesurée par les bornes et remontée par CIRCÉA (au lieu des fiches techniques) ; un relevé de consommation exigé de l'hébergeur ; un inventaire daté des équipements pour leur durée de vie ; un registre des incidents de sécurité ; le comptage de toutes les demandes des personnes sur leurs données, y compris celles reçues par l'application ; une évaluation de l'accessibilité de l'application.
- **Garder la preuve** : conserver chaque extraction (date, source, calcul) dans un dossier de preuves, afin que les fonds puissent vérifier ce qui leur paraît aujourd'hui « non vérifiable ».
- **Contrôler avant l'envoi** : revue par la direction administrative et financière, puis validation par le comité du numérique et la présidente ; les réponses reprennent les mêmes données que le tableau de bord, ce qui garantit leur cohérence.

**Réponses tolérées**
- Instance nommée autrement (comité stratégique du SI, comité d'arbitrage), ou deux instances (un comité d'arbitrage mensuel et une revue stratégique trimestrielle), si la composition, la fréquence et les décisions sont précisées.
- Comité de surveillance informé par un rapport écrit plutôt que par une présentation, s'il est régulier.
- Autres indicateurs pertinents et complets (bloc des indicateurs tolérés du corrigé : part des réponses au questionnaire issues d'une source tracée, part des pannes résolues à distance, part du temps de l'équipe conforme aux arbitrages), ou indicateurs ESG sur la durée de vie des équipements, les incidents de sécurité ou l'accessibilité de l'application, s'ils portent les cinq champs.
- Référence au tableau de bord équilibré (Kaplan et Norton, 1992) ou à sa déclinaison pour l'informatique (Van Grembergen, 2001) : valorisée.

**Erreurs fréquentes**
- *Gouvernance confondue avec l'organisation de la direction technique* (`JUR-G06` vocabulaire précis de la gouvernance) — la question porte sur les instances, les rôles et les règles d'arbitrage, pas sur l'organigramme de la direction technique.
- *Fonds présentés comme pilotes du SI* (`JUR-T03` analyser et argumenter) — ils siègent au comité de surveillance, qui donne un avis ; la présidente arbitre.
- *Indicateurs génériques ou incomplets* (ET-18, `JUR-A02` distinguer performance et qualité, justifier chaque choix) — chaque indicateur porte formule, source, fréquence, cible et axe, et s'appuie sur une donnée de l'annexe.
- *Indicateurs ESG isolés dans une liste séparée* (limite du programme 1.2) — ils sont intégrés au même tableau de bord et alimentent le questionnaire.
- *Assujettissement à un cadre de publication de durabilité discuté* (`JUR-T07` répondre à la seule question posée) — AMPÉRANE ne publie pas d'état de durabilité ; la question porte sur la fiabilité des réponses aux fonds.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 38500 (édition 2024) | gouvernance des TI : évaluer, diriger, surveiller | `iso_38500_2024` ; F02 | en vigueur |
| COBIT 2019 (ISACA) | distinction gouvernance et gestion (réponse tolérée) | `cobit_2019` ; F02 | en vigueur |
| Comitologie du SI | comité stratégique et comité d'arbitrage : composition, fréquence, rôle | F02 § 6 | notion de cours |
| Tableau de bord équilibré (Kaplan et Norton, 1992) ; tableau de bord équilibré de l'informatique (Van Grembergen, 2001) | axes et indicateurs à cinq champs, ESG intégrés | F09 § 4 ; F01 § 6 | notion de cours |

---

### 1.4 – La base de connaissances des interventions (3,5 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.b` « Architecture fonctionnelle des systèmes de knowledge management » ; `1.6.c` « Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) ». Limites : « La gestion des connaissances dépasse la seule numérisation de l'information. » « Le pilotage nécessite une approche systémique : outils, processus, culture. » « Le lien avec la gestion des compétences (RH) est complémentaire mais distinct. »

**Annexes mobilisées** : annexes 1.5 (constats, savoirs dispersés, deux options, réserves) et 1.1 (techniciens, centre de supervision, entreprises de maintenance, logiciel de gestion des interventions) ; lien avec l'annexe 1.4 (arbitrage des demandes de l'exploitation).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Architecture fonctionnelle d'un système de gestion des connaissances définie (organisation des fonctions qui font passer les savoirs, tacites et explicites, de leurs sources à leur usage : capter, structurer et valider, stocker, rechercher et diffuser, utiliser dans le travail, mettre à jour) ; elle dépasse la numérisation de documents | 0,5 |
| a-2 | Comparaison des deux options selon trois critères explicités (par exemple intégration au travail du technicien, qualité et actualité des contenus, maîtrise des accès, coût et délai), appuyée sur l'annexe 1.5 | 0,5 |
| a-3 | Recommandation justifiée (base intégrée, de préférence) avec sa condition (trois mois de l'équipe de CIRCÉA à faire arbitrer ; démarrage par les pannes les plus fréquentes) | 0,5 |
| a-4 | Parcours du technicien d'une entreprise de maintenance, de l'alerte à la clôture, avec les fonctions mobilisées à chaque étape | 0,5 |
| b-1 | Rôles : propriétaire (directrice de l'exploitation et de la maintenance), référents par constructeur (techniciens expérimentés, temps dédié), contributeurs (techniciens internes et des entreprises de maintenance, centre de supervision) ; direction technique pour la liaison avec CIRCÉA | 0,5 |
| b-2 | Trois règles, dont une qui répond à la crainte des entreprises de maintenance (périmètre limité au diagnostic des bornes d'AMPÉRANE, réciprocité, cloisonnement entre entreprises, contribution reconnue, accès fermé en fin de contrat) | 0,5 |
| b-3 | Un indicateur complet (formule, source, fréquence, cible, axe) relié aux constats | 0,5 |

**Réponse attendue**

*1.4 a) – L'architecture fonctionnelle, le choix de l'option et le parcours du technicien*

L'**architecture fonctionnelle** d'un système de gestion des connaissances décrit les fonctions qui font passer les savoirs de leurs **sources** (personnes, documents, données des applications) à leur **usage** dans le travail, et leurs liens avec le reste du système d'information : **capter** les savoirs, y compris tacites ; les **structurer et les valider** (un référentiel commun, des fiches relues) ; les **stocker** ; permettre de les **rechercher** et les **diffuser** au bon moment ; les **utiliser** dans le flux de travail ; les **mettre à jour** et retirer ce qui est périmé. Elle dépasse la numérisation de documents : chez AMPÉRANE, les savoirs sont tacites (une douzaine de techniciens expérimentés), explicites mais épars (notices), ou produits puis perdus (messagerie, diagnostics du centre de supervision, comptes rendus vides une fois sur deux). Dans les termes du modèle SECI (Nonaka et Takeuchi, 1995), l'**externalisation** des savoirs tacites et la **combinaison** des savoirs explicites font défaut (0,5 pt).

**Comparaison selon trois critères** (0,5 pt ; trois critères explicités parmi les suivants) :

| Critère | Option 1 – wiki autonome | Option 2 – base intégrée au logiciel de gestion des interventions |
|---|---|---|
| Intégration au travail du technicien | outil de plus, à ouvrir et à interroger par mots ; rédaction libre, que les techniciens n'ont « pas le temps » de faire | fiches poussées à l'ouverture de l'intervention à partir du code d'erreur ; clôture par listes, photo ou dictée : répond à la réserve du technicien |
| Qualité et actualité des contenus | pages libres, sans structure commune ni validation ; même dérive possible que la messagerie | fiches rangées par constructeur, modèle et code d'erreur ; diagnostics du centre de supervision conservés ; version du micrologiciel connue, donc fiches à revoir repérables |
| Maîtrise des accès | mêmes droits pour tous : les notices réservées à des techniciens habilités et le savoir des entreprises de maintenance sont exposés | droits par profil, par entreprise et par constructeur |
| Coût et délai | 20 + 4 × 30 = 140 k€ sur quatre ans ; deux mois | 150 + 3 × 60 = 330 k€ sur quatre ans ; six mois, dont trois mois de l'équipe de CIRCÉA |

**Recommandation : l'option 2** (0,5 pt). L'écart de coût, environ 190 k€ sur quatre ans, est faible au regard de l'enjeu : près de 9 000 seconds déplacements par an, avec trois jours de panne supplémentaires chacun, pèsent sur l'objectif de 98 % de disponibilité par point ; le taux de résolution dès la première intervention des entreprises de maintenance (60 % contre 80 %) est le premier levier. Seule l'option 2 relie le savoir au moment où il sert (le code d'erreur) et capte le savoir sans demander d'écrire. Conditions : faire **arbitrer par le comité du numérique** (1.3) les trois mois de travail de l'équipe de CIRCÉA ; commencer, pendant ces six mois, par rédiger les fiches des pannes les plus fréquentes de chaque constructeur à partir des notices et des messages utiles, pour que la base ne soit pas vide à son ouverture ; fermer ensuite la messagerie de groupe comme canal des astuces.

**Le parcours d'un technicien d'une entreprise de maintenance** (0,5 pt) :

| Étape | Ce qui se passe | Fonction du dispositif mobilisée |
|---|---|---|
| 1. Alerte | CIRCÉA signale un code d'erreur ; le centre de supervision tente un redémarrage à distance, échoue et enregistre son diagnostic dans l'intervention, au lieu d'une ligne de résumé | capter (savoir du centre de supervision) |
| 2. Affectation | l'intervention est confiée à l'entreprise de maintenance ; le technicien la reçoit dans l'application mobile avec le modèle de borne, la version du micrologiciel, le code d'erreur, le diagnostic à distance et l'historique de la borne | diffuser, de façon contextualisée |
| 3. Préparation | les fiches du modèle et du code d'erreur s'affichent, classées par taux de réussite ; il consulte la partie de la notice à laquelle il est habilité et emporte la bonne pièce | rechercher ; contrôle des accès |
| 4. Sur site | il suit la fiche ; s'il bloque, il pose sa question au référent du constructeur depuis l'outil, et la réponse reste attachée à l'intervention | utiliser dans le travail ; partager avec un expert |
| 5. Clôture | il choisit la cause et la solution dans les listes, ajoute une photo ou dicte un commentaire, en deux minutes | capter (externalisation du savoir tacite) |
| 6. Après | le référent valide ou complète la fiche ; la fiche qui a résolu la panne gagne en rang ; une mise à jour du micrologiciel signale les fiches à revoir | valider, mettre à jour |

*1.4 b) – La gouvernance du dispositif*

**Les rôles** (0,5 pt) :
- **Propriétaire** : Mme FOLCARIAS, directrice de l'exploitation et de la maintenance ; elle fixe les objectifs, porte le dispositif au comité du numérique, arbitre les litiges et rend compte de l'indicateur.
- **Référents par constructeur** : quatre techniciens expérimentés, un par constructeur, choisis parmi la douzaine que les autres appellent ; ils valident et rédigent les fiches à partir des clôtures, répondent aux questions et revoient les fiches après chaque mise à jour de micrologiciel ; une part de leur temps y est réservée, ce qui remplace les vingt appels par jour.
- **Contributeurs** : tous les techniciens d'AMPÉRANE et des entreprises de maintenance, et les opérateurs du centre de supervision, qui enregistrent leurs diagnostics.
- **Appui** : la direction technique pour la liaison avec CIRCÉA et les droits d'accès ; la direction administrative et financière pour l'adaptation des contrats de maintenance (en principe).

**Trois règles** (0,5 pt ; trois parmi les suivantes, dont la première) :
1. **Règle de périmètre et de réciprocité, en réponse à la crainte des entreprises de maintenance** : la base ne recueille que le diagnostic et la réparation des bornes du réseau d'AMPÉRANE, jamais les méthodes d'organisation, les outils ou les prix des entreprises ; chaque entreprise accède à **toute** la base, donc au savoir d'AMPÉRANE et à ses diagnostics, ce qui améliore son propre taux de résolution ; aucune entreprise ne voit les volumes ni les résultats des autres ; les contributions sont attribuées à leur auteur et à son entreprise et comptent positivement dans l'évaluation de la qualité de la prestation ; l'accès est fermé à la fin du contrat.
2. **Règle de validation et de péremption** : aucune fiche n'est publiée sans la validation du référent du constructeur, sous cinq jours ouvrés ; chaque fiche indique la version de micrologiciel à laquelle elle s'applique ; toute mise à jour de micrologiciel déclenche la revue des fiches concernées (réponse au technicien expérimenté).
3. **Règle de saisie minimale** : la clôture d'une intervention exige la cause et la solution choisies dans des listes, en deux minutes au plus ; le texte libre est facultatif ; ce sont les référents qui écrivent les fiches (réponse au technicien itinérant).
4. **Règle d'accès** : les notices réservées par deux constructeurs ne sont ouvertes qu'aux techniciens qu'ils ont habilités.

**Un indicateur** (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de résolution dès la première intervention | interventions sur site non suivies d'un second déplacement pour la même borne et le même code d'erreur dans les trente jours / interventions sur site × 100, par entreprise et par constructeur | logiciel de gestion des interventions, relié aux codes d'erreur de CIRCÉA | mensuelle, présentée chaque trimestre aux entreprises de maintenance | 85 % pour chaque entreprise fin 2028 (80 % en interne et 60 % chez les entreprises de maintenance en 2026) | processus |

**Réponses tolérées**
- Recommandation du wiki autonome, si elle est argumentée (coût, délai de deux mois, indépendance vis-à-vis de l'équipe de CIRCÉA) et assortie de règles de structure, de validation et de droits d'accès ; ou démarrage par le wiki puis passage à la base intégrée.
- Architecture présentée sous forme de schéma, ou par couches (sources, référentiel, accès, enrichissement), si les fonctions sont reliées au cas.
- Fonction « identifier » (cartographie des savoirs critiques : la douzaine de techniciens expérimentés, les notices réservées, les diagnostics perdus) ajoutée à l'architecture : valorisée.
- Lecture du coût du wiki comme 20 + 3 × 30 = 110 k€ sur quatre ans : acceptée, la conclusion ne change pas.
- Un référent par constructeur venant d'une entreprise de maintenance : valorisé, car il associe les entreprises au dispositif.
- Autres indicateurs complets (bloc des indicateurs tolérés du corrigé) : part des codes d'erreur fréquents couverts par une fiche validée, part des interventions clôturées avec une cause et une solution renseignées, part des fiches revues après une mise à jour de micrologiciel.
- Lecture selon le modèle SECI (socialisation par le référent, externalisation à la clôture, combinaison dans les fiches, internalisation par l'usage) : valorisée.

**Erreurs fréquentes**
- *Gestion des connaissances réduite à un outil de stockage des notices* (ET-21, gestion des connaissances confondue avec la GED ; limite du programme 1.6) — le problème est le savoir tacite et le savoir produit puis perdu, pas seulement les fichiers.
- *Options comparées sans critères ou sans les données de l'annexe 1.5* (`JUR-T08` exploiter toutes les annexes) — les réserves des techniciens et des entreprises de maintenance sont des critères.
- *Crainte des entreprises de maintenance ignorée ou traitée par l'obligation* (`JUR-T03` analyser et argumenter) — une règle de périmètre et de réciprocité est attendue, pas seulement « une clause du contrat ».
- *Gestion des compétences ou plan de formation des 60 recrues traités* (`JUR-T07` répondre à la seule question posée ; limite du programme 1.6) — hors du sujet demandé.
- *Indicateur sans cible ni source* (ET-18) — l'indicateur porte les cinq champs.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Architecture fonctionnelle d'un dispositif de gestion des connaissances | fonctions, outils, intégration au flux de travail | F06 § 2.1 | notion de cours |
| Gouvernance d'un dispositif de gestion des connaissances | rôles, règles de validation et de mise à jour, indicateurs | F06 § 2.2 | notion de cours |
| Modèle SECI (Nonaka et Takeuchi, 1995) | connaissances tacites et explicites, conversions (réponse valorisée) | F06 § 1 | publié |
