# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 4 — Dossier 1 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique, F02 gouvernance et référentiels, F03 architecture et urbanisation, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Alignement stratégique du système d'information | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.b` Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) | 3,5 |
| 1.2 Schéma directeur et veille technologique | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.c` Méthodologies de planification stratégique du SI ; `1.1.d` Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques | 3,5 |
| 1.3 Organisation et gouvernance de la fonction informatique | `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ; `1.2.b` Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 4,5 |
| 1.4 Urbanisation et rationalisation du processus d'admission | `1.3.b` Cartographie applicative et fonctionnelle des SI ; `1.3.c` Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle ; `1.3.f` Analyse des processus métiers et rôle des architectures SI dans leur rationalisation | 3,5 |
| **Dossier 1 – Aligner la stratégie du SI et refonder la gouvernance de la fonction informatique** |  | **15** |

Répartition indicative : connaissances (définitions, modèles) 3,5 points (items 1.1 a-1, 1.2 a-1 et c-1, 1.3 b-1, 1.4 a-1 et a-2, et la présentation du modèle en 1.1 a-2 pour moitié) ; analyse des annexes et recommandations 11,5 points. Durée conseillée : 15 points × 4,5 minutes ≈ 1 h 10.

---

### 1.1 – Alignement stratégique du système d'information (3,5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.b` « Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) ».

**Annexes mobilisées** : annexes 1.1 (organisation, fonction informatique), 1.2 (objectifs du plan, constats, budget), 1.3 (cartographie applicative, processus d'admission) et 1.4 (témoignages).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Alignement stratégique défini : cohérence permanente, réciproque et organisationnelle entre stratégie de l'organisation et stratégie du SI | 0,5 |
| a-2 | Modèle SAM présenté (deux axes, quatre domaines) et les quatre domaines caractérisés à LORVANNE par des faits des annexes (0,5 pour deux domaines) | 1 |
| b-1 | Trois zones de désalignement, chacune avec l'objectif menacé et les faits qui la révèlent (0,5 par zone) | 1,5 |
| b-2 | Perspective d'alignement justifiée (stratégie de l'organisation en point de départ) | 0,5 |

**Réponse indicative**

*1.1 a) – Définition et modèle d'alignement stratégique appliqué*

L'alignement stratégique du système d'information est la mise en cohérence permanente de la stratégie du SI avec la stratégie de l'organisation : le SI (applications, données, organisation de la fonction informatique, compétences) doit servir les objectifs métiers, et la stratégie peut à son tour tirer parti des possibilités technologiques. Il est dynamique (il se refait à chaque changement de stratégie) et organisationnel autant que technique (0,5 pt).

Le modèle d'alignement stratégique (*Strategic Alignment Model*, SAM) de Henderson et Venkatraman (1993) croise deux axes : l'**ajustement stratégique**, entre le niveau externe (positionnement de l'organisation sur son marché) et le niveau interne (structures et processus), et l'**intégration fonctionnelle**, entre le domaine métier et le domaine des technologies de l'information. Il en résulte quatre domaines qu'il faut mettre en cohérence :

| Domaine du SAM | Situation de l'Institut LORVANNE | Appréciation |
|---|---|---|
| Stratégie de l'organisation (externe, métier) | plan « LORVANNE 2030 » explicite et chiffré : formation des cadres de 5 à 10 M€ dont 5 M€ en ligne, 2 000 apprentis, 120 universités partenaires, 85 % d'étudiants satisfaits (annexe 1.2) | définie, ambitieuse, fondée sur des services numériques |
| Stratégie des TI (externe, SI) | aucune : dernier schéma directeur 2016-2019, plan sans volet SI, plus de DSI depuis 2025 ; les choix technologiques naissent d'un salon (IA générative) ou d'initiatives de campus (annexes 1.2 et 1.4) | absente |
| Infrastructure et processus organisationnels (interne, métier) | trois campus autonomes aux processus d'admission différents ; formation des cadres gérée par formulaire et tableur ; dix commandes saisies pour dix cadres d'une même entreprise (annexes 1.3 et 1.4) | hétérogène, non industrialisée |
| Infrastructure et processus SI (interne, SI) | doublons (trois outils de candidature, deux installations du progiciel de scolarité), quatre saisies de l'identité d'un étudiant, trois annuaires, plateforme pédagogique en fin de vie ; 15 informaticiens sur 21 dans le support local ; 2,5 M€ sur 2,9 M€ pour faire fonctionner l'existant (annexes 1.1 à 1.3) | fragmentée, tournée vers le maintien de l'existant |

(0,5 pt pour la présentation du modèle avec deux domaines caractérisés, 0,5 pt pour les deux autres.)

Conclusion : seul le domaine « stratégie de l'organisation » est défini ; ni l'ajustement stratégique côté SI (pas de stratégie des TI) ni l'intégration fonctionnelle (stratégie de l'école sans traduction dans le SI) ne sont assurés.

*1.1 b) – Zones de désalignement et perspective à suivre*

Trois zones attendues, parmi :
- **Formation des cadres en ligne** (objectif : 10 M€ dont 5 M€ en ligne, contre 0,3 M€ aujourd'hui) : la plateforme pédagogique, hébergée au siège depuis 2014, arrive en fin de vie ; aucune inscription ni aucun paiement en ligne pour les entreprises, chaque cadre inscrit donnant lieu à une saisie (témoignage de Mme ROUVIÈRE, annexe 1.3) : le canal sur lequel repose la croissance n'existe pas (0,5 pt).
- **Apprentissage** (objectif : de 1 450 à 2 000 apprentis, soit plus d'un tiers en plus) : relations avec les entreprises suivies dans des tableurs à Dijon et à Chalon-sur-Saône, logiciel propre à Besançon, cinquième saisie de l'identité pour chaque apprenti ; aucune vue commune des employeurs, dont la satisfaction n'est pas mesurée (annexes 1.2 et 1.3) : la montée en charge multipliera les ressaisies et les erreurs (0,5 pt).
- **Expérience des étudiants** (objectif : 85 % de satisfaits, 41 % seulement pour les démarches de candidature et d'inscription) : trois modes de dépôt, 900 dossiers déposés en double, réponse en 5 semaines, candidats qui s'inscrivent ailleurs avant la réponse (M. SADOUNI), 6 % de fiches en double ou erronées en scolarité (annexes 1.2 à 1.4) : la première expérience du futur étudiant dégrade l'image et fait perdre des inscriptions (0,5 pt).
- **Pilotage et gouvernance du SI** (condition de tous les objectifs, en premier lieu l'offre en ligne de formation des cadres) : budget dispersé et consolidé à la clôture seulement, 0,4 M€ sur 2,9 M€ pour les projets nouveaux, achats décidés campus par campus, responsable informatique sans autorité rattaché au directeur financier, qui « ne peut pas porter une stratégie » (annexes 1.2 à 1.4) : aucune capacité à financer et arbitrer les projets du plan (0,5 pt, en remplacement d'une zone précédente).

Perspective d'alignement (0,5 pt) : la stratégie de l'école est fixée et le SI doit la servir ; la perspective à suivre part donc de la stratégie de l'organisation. La **transformation technologique** (stratégie de l'organisation → stratégie des TI → infrastructure et processus SI) convient : elle impose d'abord de formuler une stratégie du SI (schéma directeur, question 1.2), puis de transformer applications et organisation informatique ; elle se combine avec l'**exécution de la stratégie** (stratégie → organisation → SI) pour l'harmonisation des processus d'admission des trois campus. À l'inverse, adopter l'IA générative parce que les concurrents l'affichent reviendrait à partir de la technologie (logique de **potentiel concurrentiel**) sans besoin établi, alors que la stratégie existe déjà.

**Réponses tolérées**
- Perspective d'**exécution de la stratégie** retenue seule, si le candidat montre que la réorganisation des processus des campus précède les choix applicatifs.
- Analyse complémentaire par la **chaîne de valeur** (Porter) : admissions et formation comme activités principales mal soutenues par le SI ; valorisée si elle reste appliquée au cas.
- Intitulés des quatre domaines ou des perspectives formulés différemment, si les deux axes du modèle sont présents.
- Zone de désalignement sur l'**international** (aucune application ne gère les partenariats, objectif de 120 universités partenaires) : acceptée si le candidat la formule comme hypothèse, l'annexe 1.3 ne décrivant pas ce domaine.

**Erreurs types**
- *Alignement réduit à un choix technique ou à un logiciel unique* (`JUR-G02`, `ET-06`) — « aligner, c'est installer un ERP commun aux trois campus » ; juste : l'alignement porte sur la stratégie, l'organisation et la gouvernance ; une convergence applicative n'en est qu'un moyen.
- *Définition sans application au cas* (`JUR-T01`, `JUR-G01`) — modèle SAM récité sans caractériser les domaines de LORVANNE ; juste : chaque domaine est renseigné par des faits des annexes.
- *Absence de modèle théorique* (`JUR-G03`, `ET-40`) — avis sur l'alignement sans référence au SAM ; juste : le modèle est nommé, ses axes expliqués et appliqués.
- *Désalignement confondu avec un dysfonctionnement technique* — l'incident de Besançon présenté comme la cause du désalignement ; juste : l'incident est un symptôme d'une fonction informatique non gouvernée, non l'écart entre stratégie et SI.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Henderson et Venkatraman (1993), *Strategic Alignment Model* | deux axes, quatre domaines, perspectives d'alignement | F01 § 1 | modèle théorique |
| Chaîne de valeur (Porter, 1985) | activités soutenues par le SI | F01 § 2 | modèle théorique |

---

### 1.2 – Schéma directeur et veille technologique (3,5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.c` « Méthodologies de planification stratégique du SI » ; `1.1.d` « Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques ».

**Annexes mobilisées** : annexes 1.2 (objectifs, constats, technologies signalées), 1.3 (organisation, cartographie, processus) et 1.4 (témoignages).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Schéma directeur défini (planification du SI à trois à cinq ans, distinct d'un plan de projet) | 0,5 |
| a-2 | Démarche en étapes ordonnées et adaptées au cas (cadrage, diagnostic, orientations, cible, feuille de route, pilotage) | 0,5 |
| b | Trois axes prioritaires, chacun relié à un objectif du plan et à des constats (0,5 par axe ; un axe transversal de gouvernance est accepté s'il est relié aux objectifs qu'il conditionne) | 1,5 |
| c-1 | Veille technologique active définie (organisée, orientée décision, prospective) | 0,5 |
| c-2 | Évaluation d'une technologie au regard du besoin réel (besoin, apport, conditions et limites) avec une conclusion | 0,5 |

**Réponse indicative**

*1.2 a) – Schéma directeur et démarche d'élaboration*

Le schéma directeur du système d'information est le document de planification qui fixe, pour trois à cinq ans et à partir de la stratégie de l'organisation, les orientations du SI, la cible (applications, données, organisation, compétences), le portefeuille de projets priorisé et les moyens ; il se distingue d'un plan de projet, qui organise les tâches, les ressources et les délais d'un seul projet (0,5 pt).

Démarche proposée pour 2027 (0,5 pt) :
1. **Cadrage** : mandat de la directrice générale, comité de pilotage réunissant les directeurs de campus, la directrice des programmes et le directeur financier, horizon 2027-2030 calé sur « LORVANNE 2030 » ;
2. **Diagnostic de l'existant** : cartographies (annexe 1.3), coûts consolidés des quatre entités, satisfaction des usagers, compétences de l'équipe informatique ;
3. **Orientations et besoins** : traduction de chaque objectif du plan en besoins du SI, entretiens avec les campus et les programmes, résultats de la veille technologique ;
4. **Cible et scénarios** : architecture et organisation cibles, deux ou trois scénarios comparés (coût, risque, délai) ;
5. **Feuille de route** : portefeuille de projets priorisé, jalons, enveloppes budgétaires en ordre de grandeur, risques ;
6. **Validation et pilotage** : adoption par le comité de direction puis par le conseil d'administration, revue annuelle, indicateurs de suivi.

*1.2 b) – Trois axes prioritaires pour 2027-2030*

| Axe | Objectif du plan servi | Constats justificatifs | Contenu |
|---|---|---|---|
| 1. Gouverner et organiser la fonction SI (2027) | condition de tous les objectifs, en premier lieu l'offre en ligne de formation des cadres, que 0,4 M€ de projets nouveaux ne peuvent financer | pas de DSI depuis 2025, projets décidés par campus, budget consolidé à la clôture, 0,4 M€ de projets sur 2,9 M€ (annexes 1.2 et 1.4) | recrutement d'un DSI rattaché à la direction générale, budget SI consolidé, comités d'arbitrage (question 1.3), règle commune d'achat de logiciels |
| 2. Unifier le parcours du candidat, de l'étudiant et des entreprises (2027-2029) | expérience des étudiants (85 % de satisfaits) et apprentissage (2 000 apprentis) | trois outils de candidature, 5 semaines de délai, quatre saisies de l'identité, deux installations du progiciel de scolarité, outils de relations entreprises différents (annexe 1.3) | référentiel unique de l'étudiant, plateforme de candidature commune, installation unique de la scolarité, outil commun de relations avec les entreprises et les employeurs d'apprentis (question 1.4) |
| 3. Construire le socle de l'offre en ligne de formation des cadres (2027-2030) | formation des cadres : 10 M€ dont 5 M€ en ligne | plateforme pédagogique en fin de vie, inscriptions par formulaire et tableur, commandes saisies une à une (annexes 1.2 à 1.4) | remplacement de la plateforme pédagogique (projet distinct), inscription et paiement en ligne pour les entreprises, catalogue en ligne, attestations numériques des compétences |

(0,5 pt par axe relié à un objectif et à des constats.)

*1.2 c) – Veille technologique active et évaluation d'une technologie*

La veille technologique active est un dispositif organisé et continu de surveillance de l'environnement technologique (sources identifiées, axes de veille définis, analyse et diffusion aux décideurs), orienté vers la décision et prospectif : il évalue l'effet d'une technologie sur le modèle économique et les processus de l'organisation, au lieu de collecter passivement des nouveautés. À LORVANNE, la veille est « informelle » (annexe 1.2) : propositions de salons ou d'éditeurs, sans critères ni responsable (0,5 pt).

Évaluation attendue pour **une** technologie (0,5 pt) ; éléments par technologie :
- **Plateforme de candidature en ligne** : besoin réel et documenté (trois modes de dépôt, 900 doublons, 5 semaines de délai, 41 % de satisfaits des démarches, candidats perdus selon M. SADOUNI ; demande des trois services des admissions) ; apport : dossier unique, suivi par le candidat, réponse plus rapide, fin des ressaisies ; conditions : intégration au référentiel unique de l'étudiant et à la scolarité, choix commun aux trois campus, harmonisation préalable des règles d'admission. **Conclusion : opportunité forte, à inscrire en priorité dans l'axe 2.**
- **Badges numériques** : besoin réel exprimé par les entreprises clientes de la formation des cadres (Mme ROUVIÈRE), cohérent avec l'objectif de 5 M€ en ligne ; apport : différenciation de l'offre en ligne, visibilité des participants ; conditions : définir les compétences attestées par module, garantir la vérifiabilité, relier les badges à la plateforme pédagogique et à la scolarité. **Conclusion : opportunité réelle mais seconde, à expérimenter sur quelques formations courtes une fois la plateforme remplacée (axe 3).**
- **IA générative dans la pédagogie** : la demande vient d'un salon et de l'affichage des concurrents (effet de mode), aucun besoin d'usagers n'est mesuré ; le besoin réel révélé par l'annexe 1.4 est de **cadrer** les usages existants (enseignants utilisant leurs comptes personnels sans règle : confidentialité des contenus, fiabilité des réponses, intégrité des évaluations) ; un assistant de tutorat suppose une plateforme pédagogique rénovée. **Conclusion : pas de projet d'équipement en 2027 ; une charte d'usage et une expérimentation limitée, évaluée sur des critères pédagogiques, après le remplacement de la plateforme.**

**Réponses tolérées**
- Démarche structurée selon une autre présentation (diagnostic, cible, trajectoire), si le diagnostic précède la cible et si la validation par la direction est prévue.
- Quatrième axe pertinent : sécurisation et mutualisation des infrastructures et des identités des trois campus (annuaire unique), en lien avec l'incident de Besançon cité comme constat ; accepté en remplacement d'un axe si relié au plan.
- Conclusion favorable à l'IA générative si elle est conditionnée à un besoin mesuré, à une gouvernance des usages (charte, validation humaine) et à une expérimentation évaluée.
- Évaluation de deux ou trois technologies : seule la meilleure est notée.

**Erreurs types**
- *Schéma directeur confondu avec un plan de projet* (`ET-07`, F01 § 8, piège 5) — liste de tâches et de dates sur douze mois, ou chiffrage ligne à ligne d'un seul projet ; juste : orientations à trois ou quatre ans, axes, portefeuille priorisé et pilotage.
- *Veille passive et effet de mode* (`ET-19`) — retenir l'IA générative « parce que les concurrents l'ont », ou une technologie sans limites ni conditions ; juste : évaluer l'apport au regard d'un besoin établi, des risques et des prérequis.
- *Axes génériques sans lien avec le cas* (`JUR-T01`) — « moderniser le SI », « passer au cloud » ; juste : chaque axe sert un objectif chiffré du plan et répond à des constats des annexes.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Schéma directeur et portefeuille de projets | démarche, horizon, axes | F01 § 3 | notion de cours |
| Veille technologique active | dispositif, critères d'évaluation | F01 § 0 (1.1.d) | notion de cours |

---

### 1.3 – Organisation et gouvernance de la fonction informatique (4,5 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité » ; `1.2.b` « Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ».

**Annexes mobilisées** : annexes 1.1 (organigramme), 1.2 (budget, constats), 1.3 (organisation de la fonction informatique) et 1.4 (témoignages).

**Barème indicatif (4,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Modèle actuel caractérisé (décentralisé, sans pilotage central) et deux effets tirés des annexes | 0,5 |
| a-2 | Deux modèles cibles comparés dans le contexte de LORVANNE (principe, forces, limites) | 1 |
| a-3 | Recommandation argumentée, avec le rattachement du DSI et le rôle des équipes de campus | 0,5 |
| b-1 | Gouvernance du SI définie (évaluer, diriger, surveiller ; distincte du management), parties prenantes du cas | 0,5 |
| b-2 | Deux instances : composition, fréquence, décisions (0,5 par instance) | 1 |
| b-3 | Deux leviers d'apaisement contextualisés (0,5 par levier ; un levier qui reprend seulement le rattachement du DSI ou les correspondants SI déjà notés en a-3, ou la composition d'une instance notée en b-2, ne rapporte des points que s'il y ajoute un dispositif nouveau) | 1 |

**Réponse indicative**

*1.3 a) – Modèle actuel, modèles cibles et recommandation*

La fonction informatique de LORVANNE relève d'un **modèle décentralisé** : chaque campus dispose de son équipe (7, 5 et 3 personnes), de son budget, de son annuaire et d'une partie de ses applications, sous l'autorité hiérarchique de son directeur ; l'équipe du siège (6 personnes) n'a ni autorité ni mandat, et son responsable, intérimaire, est rattaché au directeur financier, ce qui fait de l'informatique un centre de coûts plutôt qu'un levier stratégique. Effets (deux attendus) : doublons d'applications (trois outils de candidature, deux installations de la scolarité), plus des deux tiers des informaticiens (15 sur 21) absorbés par le support local et aucune capacité projet à Chalon-sur-Saône, budget connu à la clôture seulement, pratiques hétérogènes (trois annuaires, aucune règle d'achat) qui fragilisent la sécurité de l'école (l'incident de Besançon, cité comme constat, en est un signal) (0,5 pt).

Comparaison de deux modèles cibles (1 pt) :

| Modèle | Principe | Forces pour LORVANNE | Limites pour LORVANNE |
|---|---|---|---|
| **Centralisé** | une DSI unique, au siège, décide et opère pour les trois campus ; toutes les équipes lui sont rattachées | cohérence des choix, fin des doublons, sécurité homogène, économies d'échelle | éloignement des campus, crainte d'un support « lointain » (M. VERCLOS), rejet probable par des campus habitués à l'autonomie (Mme MARCOIRE) |
| **Fédéral (fédéré)** | une DSI centrale porte la stratégie, l'architecture, les applications et référentiels communs, la sécurité et les achats ; des équipes de proximité restent sur chaque campus pour le support et les besoins locaux, avec un double lien, hiérarchique et fonctionnel, entre la DSI et la direction du campus | équilibre entre cohérence et proximité : le dépannage « dans l'heure » est préservé, les choix applicatifs deviennent communs | rôles et doubles rattachements à clarifier, coordination exigeante, risque de reconstitution de baronnies si la DSI centrale manque d'autorité |

Recommandation (0,5 pt) : le **modèle fédéral**, qui répond à la fois au besoin de cohérence du plan (applications communes, référentiel unique, budget consolidé) et à l'attachement des campus à la proximité. Conditions : recruter un DSI **rattaché à la directrice générale** et membre du comité de direction ; rattacher hiérarchiquement les quinze informaticiens des campus à la DSI, avec un lien fonctionnel avec le directeur du campus et un engagement de service local ; désigner un correspondant SI par campus ; confier à l'équipe du siège les applications communes et les projets du schéma directeur. Le rattachement hiérarchique des équipes de campus à la DSI tire la leçon de la situation actuelle (un responsable sans autorité sur les campus) ; le schéma inverse, où les équipes restent sous l'autorité du directeur de campus avec un lien fonctionnel fort avec la DSI, relève aussi du modèle fédéral.

*1.3 b) – Gouvernance du SI, instances et leviers d'apaisement*

La gouvernance du SI est le système par lequel l'organe de direction **évalue** les besoins et les options, **dirige** (priorités, décisions, responsabilités) et **surveille** la performance, les risques et la conformité du SI, au service de la stratégie ; elle se distingue du management, qui planifie et exécute (ISO/IEC 38500 ; domaine EDM de COBIT 2019). Elle associe les parties prenantes : conseil d'administration, direction générale, directions de campus et des programmes, direction financière, DSI, et, par leurs représentants, enseignants, étudiants et entreprises partenaires (0,5 pt).

| Instance | Composition | Fréquence | Décisions |
|---|---|---|---|
| **Comité stratégique du SI** | directrice générale (présidente), directeurs des trois campus, directrice des programmes, directeur financier, DSI ; le président du conseil d'administration informé chaque année | semestrielle (trimestrielle la première année) | valide le schéma directeur et le budget SI consolidé, arbitre les grands choix (modèle d'organisation, plateforme, référentiel unique), suit l'avancement du plan sous l'angle du SI |
| **Comité d'arbitrage du portefeuille de projets** | DSI, un représentant de chaque campus, directrice des programmes, contrôle de gestion ; correspondants SI invités | mensuelle | examine toute demande de projet ou d'achat de logiciel sur une fiche commune (objectif du plan servi, coût, risque, charge, effet environnemental), priorise, lance ou arrête les projets, met fin aux achats isolés |

(0,5 pt par instance complète.)

Leviers d'apaisement (deux attendus, 0,5 pt chacun) :
- **Placer le DSI à la direction générale et au comité de direction** : il cesse d'être un gestionnaire de budget rattaché au directeur financier (M. DELORMEAU) et devient l'interlocuteur des directeurs de campus, avec un mandat clair (M. CORNAVIN : « personne n'arbitre »).
- **Garantir la proximité par un engagement de service** : délai d'intervention en salle de cours inscrit dans un accord de service interne avec chaque campus, suivi au comité ; il répond à la crainte de M. VERCLOS.
- **Associer les campus aux décisions** : représentants au comité d'arbitrage, droit de proposition, reconnaissance de leurs solutions quand elles sont bonnes (l'outil de relations entreprises de Besançon peut devenir l'outil commun si l'analyse le justifie), ce qui répond au sentiment de Mme MARCOIRE de n'être « jamais écoutée ».
- **Rendre le budget lisible** : budget SI consolidé, avec une enveloppe par campus pour les besoins locaux et une enveloppe commune pour les projets du schéma directeur, présenté chaque trimestre.
- **Correspondants SI dans chaque campus et dans les programmes** : relais des besoins vers la DSI, logique de partenaire plutôt que de fournisseur.

Un levier qui reprend seulement le rattachement du DSI ou les correspondants SI déjà notés en a-3, ou la composition d'une instance notée en b-2, ne rapporte des points que s'il y ajoute un dispositif nouveau (mandat écrit, engagement de service, budget lisible…).

**Réponses tolérées**
- Recommandation d'un **modèle centralisé avec antennes de proximité**, si le candidat traite la crainte d'éloignement (engagement de service, techniciens maintenus sur place) : acceptée.
- **Modèle fédéral dans lequel les équipes de campus restent rattachées hiérarchiquement au directeur de campus**, avec un lien fonctionnel avec la DSI : accepté si la DSI décide des choix communs (applications, référentiels, sécurité, achats) et si le candidat montre comment ce lien corrige l'absence d'arbitrage actuelle (M. CORNAVIN : « Personne n'arbitre »).
- Évocation d'une organisation **bimodale** pour l'offre en ligne de formation des cadres (petite équipe agile dédiée à côté du socle stable), en complément du modèle fédéral : valorisée.
- Mention d'un responsable de la sécurité des systèmes d'information rattaché à la direction et distinct du DSI : valorisée, sans être exigée dans ce dossier.
- Autres instances pertinentes : comité d'architecture, comité de pilotage d'un projet ; acceptées si leur rôle de gouvernance est expliqué.

**Erreurs types**
- *Modèles d'organisation confondus* (F01 § 8, piège 6) — « fédéral » présenté comme synonyme de « décentralisé », ou « bimodal » compris comme un mélange d'interne et d'externe ; juste : le fédéral centralise la gouvernance et le commun en gardant la proximité, le bimodal sépare un mode stable et un mode exploratoire.
- *Gouvernance confondue avec le management ou avec un logiciel* (`JUR-G06`, `ET-01`) — « la gouvernance, c'est COBIT » ou « installer un outil de suivi des demandes » ; juste : décisions, rôles et instances ; COBIT 2019 et ISO/IEC 38500 sont des référentiels qui les structurent.
- *Recommandation irréaliste ou non contextualisée* (`JUR-G05`, `JUR-T01`) — supprimer les équipes de campus ou externaliser toute l'informatique sans analyser les témoignages ; juste : recommandation réaliste, qui traite les craintes exprimées.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 38500:2024 — Gouvernance des technologies de l'information pour l'organisation | évaluer, diriger, surveiller ; principes de gouvernance | `iso_38500_2024` / F02 § 4 | en vigueur |
| COBIT 2019 (ISACA) | domaine EDM, distinction gouvernance et management | `cobit_2019` / F02 § 3 | en vigueur |
| Modèles d'organisation de la DSI, comitologie | centralisé, décentralisé, fédéral, bimodal ; instances | F01 § 4 ; F02 § 6 | notion de cours |

---

### 1.4 – Urbanisation et rationalisation du processus d'admission (3,5 points)

**Référence au programme**
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.b` « Cartographie applicative et fonctionnelle des SI » ; `1.3.c` « Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle » ; `1.3.f` « Analyse des processus métiers et rôle des architectures SI dans leur rationalisation ».

**Annexes mobilisées** : annexes 1.2 (satisfaction, technologies signalées), 1.3 (cartographie applicative, processus « candidature – admission – inscription ») et 1.4 (témoignages).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Urbanisation définie (démarche stratégique, zones, quartiers, îlots, règles d'urbanisme) | 0,5 |
| a-2 | Quatre couches présentées et illustrées par la situation de LORVANNE | 0,5 |
| b-1 | Couche métier : acteurs et étapes du processus cible, sans étape en double | 0,5 |
| b-2 | Couche applicative : applications cibles et référentiel unique de l'étudiant | 0,5 |
| b-3 | Échanges entre applications par une zone d'échange, ressaisies supprimées, schéma légendé | 0,5 |
| c | Deux effets de rationalisation, chacun assorti d'un indicateur complet (formule, source, fréquence, cible, axe) (0,5 par effet) | 1 |

**Réponse indicative**

*1.4 a) – Principes de l'urbanisation et couches de la cartographie*

Urbaniser le SI consiste, par analogie avec l'urbanisme d'une ville, à le découper en **zones** (grands domaines : pilotage, cœur de métier, support, référentiels, échanges), **quartiers** (sous-domaines : admissions, scolarité, relations entreprises…) et **îlots** (ensembles cohérents de fonctions), faiblement couplés, pour qu'il évolue au rythme de la stratégie sans tout reconstruire. Règles d'urbanisme : une fonction n'est implantée qu'une fois ; une donnée de référence (l'étudiant, l'entreprise) a un référentiel et un propriétaire uniques ; les échanges passent par une zone d'échange plutôt que par des liens point à point. C'est une démarche stratégique, au service des processus, et non un inventaire technique (0,5 pt).

La cartographie se lit en quatre couches, dont l'urbanisation travaille les correspondances (0,5 pt) :
- **métier** : processus, acteurs et événements ; à LORVANNE, le processus « candidature – admission – inscription » existe en trois variantes, une par campus ;
- **fonctionnelle** : fonctions et informations, indépendamment des logiciels (gérer une candidature, évaluer, décider, encaisser, inscrire, ouvrir les accès) ; la fonction « gérer une candidature » est implantée trois fois ;
- **applicative** : applications et flux ; application interne de Dijon, courriel et tableur à Besançon, formulaire gratuit à Chalon-sur-Saône, deux installations de la scolarité, fichier hebdomadaire vers la plateforme ; aucun référentiel de l'étudiant ;
- **infrastructure** (technique) : serveurs, réseaux, hébergement ; serveurs propres à chaque campus, dont celui de Besançon qui porte la seconde installation de la scolarité, trois annuaires.

*1.4 b) – Cartographie cible du processus « candidature – admission – inscription »*

Format libre (diagramme en couloirs, schéma en couches ou tableau), légendé ; exemple :

```
COUCHE MÉTIER (acteurs et étapes)
Candidat     : dépose UN dossier en ligne (un ou plusieurs campus) -> suit son dossier -> paie l'acompte en ligne -> s'inscrit
Admissions   : contrôle les pièces -> planifie épreuves et entretiens (campus choisi)
Jury         : statue -> décision notifiée automatiquement
Scolarité    : valide l'inscription (sans ressaisie)
Relations ent.: rattache l'apprenti à son employeur

COUCHE APPLICATIVE (cible commune aux trois campus)
[Plateforme de candidature en ligne, SaaS] --(dossier admis)--> [ZONE D'ÉCHANGE : interfaces programmables / bus]
                                                                      |
                     [RÉFÉRENTIEL UNIQUE DE L'ÉTUDIANT : identifiant unique créé à la candidature]
                                                                      |
     +-------------------+------------------------+-----------------------+---------------------+
     v                   v                        v                       v                     v
[Scolarité,       [Plateforme            [Annuaire unique       [Progiciel comptable :   [Outil commun des
 installation      pédagogique :          des comptes]            acompte payé en          relations avec les
 unique]           compte créé]                                   ligne, rapproché]        entreprises : apprenti]

Légende : --> échange automatique ; aucune ressaisie ; une seule fiche par étudiant, propriétaire : service de scolarité (à désigner)
```

(0,5 pt pour la couche métier, 0,5 pt pour les applications cibles et le référentiel unique, 0,5 pt pour les échanges et la légende.)

*1.4 c) – Rationalisation du processus et indicateurs*

- **Un dossier unique et un circuit commun réduisent le délai de réponse** : le candidat dépose un seul dossier pour un ou plusieurs campus (fin des 900 doublons), suit son avancement en ligne et reçoit une décision notifiée par l'application ; les services d'admission travaillent sur un outil commun. L'effet attendu est une réponse plus rapide et moins de candidats perdus (M. SADOUNI) (0,5 pt).
- **Le référentiel unique et la zone d'échange suppriment les ressaisies** : l'identité est saisie une fois par le candidat, puis diffusée automatiquement à la scolarité, à la plateforme pédagogique, à l'annuaire, à la comptabilité et, pour les apprentis, à l'outil des relations entreprises ; l'installation de Besançon est retirée. L'effet attendu est la disparition des fiches en double ou erronées (6 % aujourd'hui) et l'interopérabilité entre applications, sur le plan technique (échanges automatisés) comme sémantique (un identifiant et des définitions communs) et organisationnel (un propriétaire de la donnée) (0,5 pt).

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Délai moyen de réponse au candidat | somme des délais entre le dépôt du dossier complet et la notification de la décision / nombre de dossiers ayant reçu une décision | plateforme de candidature (horodatage du dépôt et de la décision) | mensuelle pendant la campagne | 2 semaines au plus pour la campagne 2029 (5 semaines en 2026) | client |
| Taux de fiches d'étudiants en double ou erronées | fiches en double ou erronées / fiches d'étudiants actives du référentiel | référentiel unique de l'étudiant (contrôle mensuel de dédoublonnage) | mensuelle | moins de 0,5 % à la rentrée 2029 (6 % en 2026) | processus |

**Réponses tolérées**
- Diagramme en couloirs inspiré de BPMN 2.0.2, ou représentation inspirée d'ArchiMate, si la légende est lisible (format libre, `JUR-T10`).
- Plateforme de candidature intégrée au progiciel de scolarité plutôt qu'en SaaS distinct, si le référentiel unique est maintenu.
- Autres indicateurs à cinq champs : nombre de saisies de l'identité d'un nouvel étudiant (cible : une), part des admis qui s'inscrivent (60 % en 2026), part des étudiants satisfaits des démarches de candidature et d'inscription (41 % en 2026), part des dossiers déposés en double.
- Cibles différentes si elles sont justifiées et cohérentes avec les mesures de 2026.

**Erreurs types**
- *Urbanisation réduite à un inventaire technique* (`ET-20`, `JUR-G07`) — liste des serveurs et des logiciels sans processus ni règles ; juste : le pourquoi (évolutivité, cohérence) puis le comment (zones, référentiels, échanges).
- *Confondre « définir » et « schématiser »* (`JUR-T06`) — description en prose sans schéma, ou schéma sans légende ni flux ; juste : schéma lisible, légendé, commenté.
- *Interopérabilité seulement technique* (`ET-36`) — « il suffit de relier les applications » ; juste : référentiel et définitions communs, propriétaire de la donnée, processus harmonisé entre campus.
- *Indicateurs génériques* (`JUR-A02`, `ET-18`) — « taux de satisfaction » sans formule, source ni cible ; juste : chaque indicateur mesure un effet de la rationalisation, avec sa valeur de départ.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Urbanisation, couches de cartographie, architecture cible | zones, quartiers, îlots ; règles d'urbanisme | F03 § 1, 2 et 6 | notion de cours |
| BPMN 2.0.2 (OMG) | notation des processus, à titre d'exemple | `bpmn_2_0_2` / F03 § 2 | en vigueur |
| ArchiMate 3.2 (The Open Group) | langage de modélisation en couches, à titre d'exemple | `archimate_3_2` / F02 § 5 | en vigueur |
