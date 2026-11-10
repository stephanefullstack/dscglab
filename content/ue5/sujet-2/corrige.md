# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 2

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Aligner la stratégie du SI et refonder la gouvernance de la fonction informatique | 15 | 1.1 à 1.4 | `exercices/ex04_alignement_gouvernance_dsi` |
| 2 – Auditer la sécurité du SI et fonder une politique de sécurité | 14 | 2.1 à 2.4 | `exercices/ex05_audit_securite_continuite` |
| 3 – Conduire le projet de plateforme pédagogique et piloter les coûts du SI | 11 | 3.1 à 3.4 | `exercices/ex06_projet_plateforme_pedagogique` |
| **Total** | **40** | | |

---

## DOSSIER 1 – ALIGNER LA STRATÉGIE DU SI ET REFONDER LA GOUVERNANCE DE LA FONCTION INFORMATIQUE (15 points)

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

---

## DOSSIER 2 – AUDITER LA SÉCURITÉ DU SI ET FONDER UNE POLITIQUE DE SÉCURITÉ (14 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Méthodologie de la mission d'audit | `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ; `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 4 |
| 2.2 Analyse des risques révélés par l'incident | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. | 3 |
| 2.3 Politique de sécurité et continuité | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.d` Dispositifs de surveillance et de résilience : IAM, PCA/PRA | 4 |
| 2.4 Note de synthèse au conseil d'administration | `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 3 |
| **Dossier 2 – Auditer la sécurité du SI et fonder une politique de sécurité** |  | **14** |

Répartition indicative : connaissances (définitions de l'audit du SI, de l'analyse d'impact sur l'activité, des objectifs de sécurité, du PCA et du PRA : items 2.1 a-1, 2.2 b-1, 2.3 a-1 et c-1) 2 points, la typologie des risques et les notions de RTO et de RPO étant notées avec leur application au cas ; analyse des annexes et recommandations 12 points. Durée conseillée : 14 points × 4,5 minutes ≈ 1 h 05.

---

### 2.1 – Méthodologie de la mission d'audit (4 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance » ; `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ».

**Annexes mobilisées** : annexes 1.1 (organisation de l'école et de la fonction informatique), 2.1 (incident et témoignages), 2.2 (audit flash, lettre de mission) et 2.3 (référentiels).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit du SI défini : examen indépendant et méthodique, au regard d'un référentiel, de la gouvernance, de la performance, de la sécurité et de la conformité du SI, conclu par des recommandations | 0,5 |
| a-2 | Périmètre (siège et trois campus, domaines retenus) et objectifs tirés de la lettre de mission | 0,5 |
| a-3 | Trois référentiels de l'annexe 2.3, chacun avec son apport distinct (gouvernance, sécurité, risques ou continuité, conformité) | 0,5 |
| a-4 | Étapes ordonnées et livrables, calés sur les huit semaines et la restitution du 24 juin 2027 | 0,5 |
| b-1 | Quatre critères de performance ou de conformité, chacun illustré par un point de contrôle tiré des annexes (0,5 par paire de critères) | 1 |
| c-1 | Deux facteurs de succès propres à la mission | 0,5 |
| c-2 | Deux points de vigilance propres à la mission | 0,5 |

**Réponse indicative**

*2.1 a) – Définition et méthodologie de la mission*

L'audit du système d'information est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel (norme, référentiel de bonnes pratiques, texte, politique interne), la gouvernance, la performance, la sécurité et la conformité du SI, et qui débouche sur des constats étayés et des recommandations hiérarchisées. Ici, il s'agit d'un audit externe contractuel, commandé par la directrice générale, à distinguer de l'audit légal (0,5 pt).

Périmètre et objectifs (0,5 pt) :
- **périmètre** : le siège et les trois campus, puisque l'audit flash montre que les faiblesses de Besançon (comptes partagés, sauvegardes accessibles, absence de cloisonnement) existent partout (annexe 2.2) ; domaines retenus : gouvernance de la sécurité (rôles, politique, charte), gestion des identités et des accès, authentification, cloisonnement, sauvegardes et continuité, conformité au RGPD (délégué, registre, procédure de violation), inventaire des applications et services en ligne souscrits hors validation ; processus critiques étudiés : examens et jurys, scolarité, paie, facturation de l'apprentissage ;
- **objectifs** (lettre de mission) : évaluer la gouvernance de la sécurité, le niveau de sécurité et la capacité de continuité ; proposer une politique de sécurité et un plan d'action priorisé ; répondre à la demande du conseil d'administration sur « qui est responsable de quoi ».

Trois référentiels de l'annexe 2.3, d'utilité distincte (0,5 pt) :
- **COBIT 2019** (référentiel de gouvernance) : il sert à apprécier la gouvernance de la sécurité et de la continuité (qui évalue, dirige et surveille : domaine « évaluer, diriger et surveiller » ; organisation et processus des domaines « aligner, planifier et organiser » et « délivrer, servir et soutenir ») et à poser la question des responsabilités soulevée par le conseil ;
- **ISO/IEC 27001:2022** (norme d'exigences d'un système de management de la sécurité) et ses 93 mesures détaillées par ISO/IEC 27002:2022 : elle fournit la grille d'évaluation des mesures de sécurité (contrôle d'accès, authentification, sauvegardes, sensibilisation, gestion des incidents) et la logique d'amélioration continue sur laquelle fonder la future politique, sans viser une certification à ce stade ;
- **EBIOS Risk Manager** (méthode d'appréciation des risques de l'ANSSI) : elle structure l'analyse des scénarios de risque (sources de risque, scénarios, traitement) qui fondera les priorités ; à défaut, le **guide d'hygiène informatique de l'ANSSI** (42 mesures de base) donne un socle rapide à confronter aux constats, et **ISO 22301:2019** la référence pour la continuité ; le **RGPD** est le référentiel de conformité pour les données personnelles.

Étapes et livrables, sur huit semaines du 12 avril au 4 juin 2027 (0,5 pt) :

| Étape | Semaines | Contenu à LORVANNE | Livrable |
|---|---|---|---|
| 1. Cadrage | 1 | réunion de lancement avec Mme FERRIOL, comité de pilotage (directrice générale, directeurs de campus, M. DELORMEAU, M. CORNAVIN, déléguée à la protection des données), confirmation du périmètre et des référentiels, calendrier des entretiens | note de cadrage validée |
| 2. Prise de connaissance | 1 à 2 | entretiens (directeurs de campus, responsables de scolarité, paie, apprentissage, informaticiens), revue des documents existants (charte de 2015, registre de 2021, rapport du prestataire de réponse à incident, audit flash), inventaire des applications | cartographie des processus critiques et des applications |
| 3. Analyse des risques | 3 | scénarios de risque et cotation sur l'échelle de l'annexe 2.3 | cartographie des risques |
| 4. Programme de travail | 3 | points de contrôle par domaine : désactivation des comptes, comptes d'administration, authentification, sauvegardes et restauration, procédure de violation, registre | programme de travail |
| 5. Collecte et évaluation | 4 à 6 | revue documentaire, entretiens, revue des comptes actifs sur échantillon, observation d'une restauration et d'un exercice de crise, contrôle du registre | feuilles de constats (constat, cause, risque, recommandation, priorité, responsable, échéance) |
| 6. Restitution | 7 à 8 | validation contradictoire des constats avec les audités, puis restitution à la direction générale | rapport détaillé, note de synthèse au conseil, plan d'action priorisé |
| 7. Suivi | après le 24 juin | revue de l'avancement du plan d'action, audit de suivi à six mois | tableau de suivi du plan d'action |

*2.1 b) – Critères de performance et de conformité*

Quatre critères parmi les suivants, chacun illustré (1 pt, 0,5 par paire) :

| Critère | Point de contrôle tiré des annexes |
|---|---|
| Sécurité, volet confidentialité | les comptes sont-ils désactivés à la fin d'une vacation ? (1 200 comptes de vacataires actifs pour 450 vacataires en activité) |
| Sécurité, volet traçabilité | chaque opération d'administration est-elle attribuable à une personne ? (neuf comptes génériques partagés) |
| Disponibilité et efficacité des mesures de résilience | les sauvegardes sont-elles isolées et restaurables dans le délai requis ? (aucun test sur les campus ; sauvegarde en ligne chiffrée avec les serveurs) |
| Fiabilité et intégrité des données | les notes et les copies sont-elles protégées contre la perte ? (9 000 notes et 2 600 copies perdues) |
| Conformité au RGPD | registre à jour et complet, délégué disposant des moyens nécessaires, procédure de notification des violations dans les 72 heures (registre de 2021, logiciel des relations entreprises absent, notification le 20 novembre pour une découverte le 16) |
| Conformité aux règles internes | la charte est-elle signée par tous les utilisateurs ? (ni vacataires ni étudiants) |
| Efficience | les moyens consacrés à la sécurité sont-ils proportionnés aux risques ? (0,3 M€ de coût direct de l'incident, environ 10 % du budget annuel du SI, à mettre en regard du coût des mesures ; M. DELORMEAU veut « savoir ce que nous achetons ») |
| Gouvernance | les responsabilités sont-elles définies ? (aucun responsable de la sécurité, aucune politique écrite) |

*2.1 c) – Facteurs de succès et points de vigilance*

Deux facteurs de succès parmi (0,5 pt) :
- un **commanditaire** au plus haut niveau : Mme FERRIOL et le conseil, qui attend une réponse sur les responsabilités, donnent à la mission l'autorité qui manque à M. CORNAVIN sur les campus ;
- l'**adhésion des audités** : présenter l'audit comme une démarche d'amélioration et non comme la recherche de coupables, comme le craint Mme MARCOIRE ; valider les constats de façon contradictoire ;
- l'**accès** aux personnes, aux documents et aux sites des trois campus, prévu par la lettre de mission ;
- des **compétences pluridisciplinaires** : sécurité, continuité, métiers de la scolarité et de l'apprentissage, protection des données ;
- un **plan d'action** suivi après la restitution, avec responsables et échéances.

Deux points de vigilance parmi (0,5 pt) :
- l'**indépendance** : M. CORNAVIN, interlocuteur désigné, « compte bien participer à l'audit » alors que la mission évalue aussi son périmètre ; il facilite l'accès mais ne peut ni conduire les entretiens ni valider seul les constats ; même vigilance à l'égard du prestataire de réponse à incident, auteur de l'audit flash ;
- un **périmètre réaliste** : quatre sites et huit semaines imposent de concentrer la collecte sur les processus critiques et sur les sauvegardes ;
- la **confidentialité** des constats : le rapport décrit des faiblesses exploitables ; diffusion restreinte et version de synthèse pour le conseil ;
- la **posture critique sur la gouvernance** : ne pas réduire l'audit à une liste de défauts techniques ; l'incident révèle d'abord l'absence de responsable et de règles communes ;
- le **respect du programme** : l'audit s'appuie sur des entretiens, des revues documentaires et des observations ; il ne prévoit pas de tests techniques de sécurité, qui seraient confiés si nécessaire à un prestataire spécialisé.

**Réponses tolérées**
- Choix d'autres référentiels de l'annexe 2.3 (guide d'hygiène informatique de l'ANSSI à la place d'EBIOS Risk Manager, ISO 22301:2019 pour la continuité, RGPD pour la conformité) dès lors que leurs apports sont distingués ; mention d'ITIL pour la gestion des incidents, si elle est justifiée.
- Découpage en cinq ou six étapes, ou échéancier présenté sous forme de diagramme de Gantt, s'il tient dans les huit semaines et respecte la restitution du 24 juin.
- Critère de « conformité aux engagements contractuels des prestataires » (contrat du logiciel de relations entreprises en mode SaaS) en remplacement d'un critère attendu.

**Erreurs types**
- *Méthodologie d'audit incomplète* (`JUR-A01`) — périmètre, livrables ou échéancier absents ; juste : périmètre, objectifs, référentiels, étapes, livrables et calendrier de huit semaines.
- *Référentiel de gouvernance confondu avec un référentiel de sécurité* (`JUR-G04`, `ET-11`) — « COBIT 2019 pour la sécurité, ISO 27001 pour la gouvernance » ; juste : COBIT 2019 évalue la gouvernance et les processus, ISO/IEC 27001:2022 les exigences de sécurité.
- *Norme, référentiel, méthode et solution confondus* (`JUR-S06`, `ET-01`) — « installer ISO 27001 » ou présenter EBIOS Risk Manager comme un logiciel ; juste : ISO/IEC 27001:2022 est une norme d'exigences, COBIT 2019 un référentiel, EBIOS Risk Manager une méthode.
- *Audit du SI confondu avec l'audit légal* (`ET-34`) — mission présentée comme un contrôle des comptes ; juste : audit externe contractuel de gouvernance, de sécurité et de conformité du SI.
- *Tests techniques proposés comme diligences* (F10, piège 3) — hors programme (partie 3.2) ; juste : entretiens, revues documentaires, revue de comptes sur échantillon, observation.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI : définition, démarche, livrables | étapes, feuilles de constats, note de synthèse | F10 § 1 | guide p. 266 ; rapport du jury 2025 p. 35 |
| COBIT 2019 (ISACA) | gouvernance et management, cinq domaines | `cobit_2019` ; F02 § 3 | en vigueur |
| ISO/IEC 27001:2022 ; ISO/IEC 27002:2022 | SMSI, 93 mesures de l'annexe A | `iso_27001_2022`, `iso_27002_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager (ANSSI, v1.5, 2024) | méthode d'appréciation des risques en cinq ateliers | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | 42 mesures de base | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| ISO 22301:2019 | management de la continuité d'activité | `iso_22301_2019` ; F12 § 4 | en vigueur |
| RGPD, règlement (UE) 2016/679 | registre, délégué, notification des violations | `rgpd` ; F15 § 1, 2, 6 | applicable depuis le 25/05/2018 |

---

### 2.2 – Analyse des risques révélés par l'incident (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers » ; `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ».

**Annexes mobilisées** : annexes 2.1 (chronologie, conséquences, témoignages), 2.2 (audit flash) et 2.3 (RGPD, échelle de cotation).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cybermenaces et défaillances opérationnelles, illustrées par les annexes | 0,5 |
| a-2 | Risques réglementaires et risques métiers, illustrés par les annexes | 0,5 |
| b-1 | Analyse d'impact sur l'activité définie (processus critiques, effets d'une interruption dans le temps, délais tolérables) | 0,5 |
| b-2 | Impacts sur quatre processus critiques et sur la continuité, étayés par les chiffres de l'annexe 2.1 | 0,5 |
| c-1 | Cinq risques cotés, probabilité et gravité justifiées par les annexes | 0,5 |
| c-2 | Priorités déduites de l'échelle (risques critiques puis élevés) | 0,5 |

**Réponse indicative**

*2.2 a) – Typologie des risques*

| Catégorie | Risques révélés à LORVANNE |
|---|---|
| Cybermenaces | hameçonnage d'un compte de la scolarité (60 salariés sur 610 ont encore saisi leur mot de passe lors de l'exercice simulé de février 2027) ; rançongiciel avec copie des données puis publication d'un échantillon (double extorsion) ; mouvements de l'attaquant vers le siège ; risque d'usurpation des 750 comptes d'anciens vacataires encore actifs |
| Défaillances opérationnelles | sauvegardes accessibles avec les comptes d'administration ordinaires et chiffrées avec les serveurs, jamais testées ; sauvegarde hebdomadaire seulement de la scolarité de Besançon ; mot de passe d'administration conservé dans un tableur ; absence de surveillance (onze jours de présence de l'attaquant sans alerte) ; absence de procédure de crise |
| Risques réglementaires | violation de données personnelles (1 400 étudiants, 420 entreprises, relevés bancaires des vacataires) notifiée le 20 novembre pour une découverte le 16, soit au-delà des 72 heures ; registre des traitements non tenu à jour depuis 2021 et incomplet ; délégué à la protection des données disposant d'un dixième de son temps |
| Risques métiers | jurys de diplôme reportés de trois semaines, épreuves à repasser, relevés et attestations impossibles à délivrer, rémunération des vacataires retardée, facturation de l'apprentissage retardée de cinq semaines, perte de confiance des entreprises employeuses et des étudiants, alors que le plan « LORVANNE 2030 » vise à développer l'apprentissage et l'expérience des étudiants et des entreprises |

*2.2 b) – Analyse d'impact sur l'activité*

L'analyse d'impact sur l'activité (*business impact analysis*) recense les processus critiques de l'organisation, mesure les effets d'une interruption ou d'une perte de données dans le temps (pédagogiques, financiers, réglementaires, d'image), identifie leurs dépendances (applications, données, personnes, prestataires) et en déduit la durée d'interruption et la perte de données tolérables, qui fondent le PCA et le PRA (0,5 pt).

Impacts de l'incident sur quatre processus critiques (0,5 pt, avec la continuité) :
- **examens et jurys** : perte des 2 600 copies numérisées (600 irrécupérables, épreuves repassées en janvier 2027) et report de trois semaines des jurys de 180 diplômés de mastère spécialisé ; l'impact dépend du calendrier : maximal en période de jurys ;
- **scolarité** : perte de 9 000 notes, soit environ six semaines de saisies, parce que la seule copie intacte datait du 30 septembre ; neuf jours sans attestation ni relevé, au détriment des apprentis et des échanges internationaux (témoignage de Mme QUERVEL) ;
- **paie** : paie des salariés préservée parce qu'elle est traitée au siège, mais rémunération des 130 vacataires du campus versée avec dix jours de retard, les états d'heures étant tenus dans des tableurs locaux ;
- **facturation des contrats d'apprentissage** : facturation d'environ 1,3 M€ émise avec cinq semaines de retard, faute d'accès aux justificatifs d'assiduité ; relation avec 420 entreprises employeuses fragilisée.

Continuité : aucun processus critique ni délai tolérable n'avait été défini ; il n'existait ni mode dégradé (listes papier improvisées, sans priorités), ni sauvegarde isolée permettant une reprise, ni cellule de crise. L'impact a été contenu au campus de Besançon par la coupure des liaisons le 16 novembre ; mais le réseau non cloisonné et les comptes d'administration communs exposent le siège et les autres campus, notamment la paie centralisée, à un incident de portée générale.

*2.2 c) – Cotation de cinq risques*

| Risque | Probabilité | Gravité | Niveau | Justification |
|---|---|---|---|---|
| R1 – Compromission d'un compte par hameçonnage suivie d'un rançongiciel étendu à plusieurs campus | 4 | 4 | 16, critique | incident déjà survenu ; 10 % des salariés saisissent leur mot de passe ; aucune authentification multifacteur ; réseau non cloisonné et comptes d'administration communs : plusieurs campus touchés plus d'une semaine |
| R2 – Accès illégitime aux données par un compte d'ancien vacataire ou un compte d'administration partagé | 3 | 3 | 9, élevé | probabilité 3 : 750 comptes d'anciens vacataires actifs, mots de passe inchangés hors de Besançon depuis l'incident, comptes génériques ; gravité 3 : divulgation de données personnelles |
| R3 – Perte définitive de données faute de sauvegarde isolée et restaurable | 3 | 4 | 12, critique | probabilité 3 : sauvegardes en ligne accessibles avec les comptes ordinaires, jamais testées sur les campus ; une panne, une erreur ou une attaque suffit ; gravité 4 : les mêmes comptes donnent accès aux sauvegardes de tous les campus ; sans copie restaurable, la reprise de la scolarité et des jurys de plusieurs campus dépasse une semaine |
| R4 – Manquement aux obligations du RGPD (registre, délai de notification, traitements inconnus) | 3 | 3 | 9, élevé | probabilité 3 : délai de 72 heures déjà dépassé en 2026, registre de 2021 incomplet, 17 applications hors inventaire ; gravité 3 : manquements portant sur les données personnelles d'étudiants, de vacataires et d'entreprises, qui entament la confiance des entreprises employeuses, sans interruption d'activité |
| R5 – Indisponibilité ou fuite d'une application souscrite sans validation | 2 | 3 | 6, modéré | services en ligne souscrits par les campus ou par des enseignants, inconnus de l'informatique du siège et du registre |

(0,5 pt pour cinq risques justifiés ; une cotation qui s'écarte d'un point est acceptée si elle est argumentée.)

Priorités (0,5 pt) : les risques critiques R1 et R3 appellent un traitement immédiat, suivi par la direction générale : authentification multifacteur, comptes d'administration nominatifs, sauvegardes déconnectées et testées. Les risques élevés R2 et R4 sont à traiter dans les six mois : revue et désactivation des comptes, procédure de violation, mise à jour du registre. R5 est traité dans l'année par l'inventaire et une règle d'acquisition des services en ligne.

**Réponses tolérées**
- Autres risques cotés de façon cohérente : défaillance d'une liaison ou d'un serveur, départ d'un informaticien clé, fraude au faux ordre de virement, attaque par un prestataire.
- Probabilité 4 pour R4, au motif que les manquements sont déjà constatés (registre non tenu) : admise si elle est justifiée (niveau 12, critique).
- Classement d'un même risque dans deux catégories (la publication des données est à la fois une cybermenace et un risque réglementaire), s'il est justifié.
- Mention des apports de l'intelligence artificielle à la détection (analyse comportementale des connexions inhabituelles depuis l'étranger), non attendue.
- Mention d'un coût direct de 0,3 M€, environ 10 % du budget annuel du SI, pour mesurer l'enjeu : admise ; aucune évaluation de l'incidence sur les comptes n'est attendue (UE 4).

**Erreurs types**
- *Typologie récitée sans faits du cas* (`JUR-T01`, `ET-39`) — liste générique de menaces ; juste : chaque catégorie est illustrée par des faits datés et chiffrés des annexes.
- *Impact réduit au coût de l'incident ou dérive comptable* (F10, pièges 2 et 7 ; quantification exclue : périmètre 4.1) — chiffrage de pertes ou traitement comptable ; juste : impacts sur les processus, les délais, les étudiants, les partenaires et la continuité.
- *Cotation sans justification ni échelle* (`JUR-T03`) — notes attribuées sans lien avec les définitions de l'annexe 2.3 ; juste : probabilité et gravité justifiées par les constats.
- *Continuité confondue avec la seule restauration informatique* (`ET-02`) — oublier le mode dégradé des métiers pendant la crise.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI, analyse d'impact sur l'activité | cybermenaces, défaillances, risques réglementaires et métiers ; BIA | F12 § 0, 4 et 5 | programme l. 1445-1449 |
| ISO/IEC 27005:2022 ; EBIOS Risk Manager | appréciation des risques (citées comme démarches) | `iso_27005_2022`, `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| RGPD, articles 30 et 33 | registre ; notification dans les 72 heures | `rgpd` ; F15 § 2 et 6 | applicable depuis le 25/05/2018 |

---

### 2.3 – Politique de sécurité et continuité (4 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ».

**Annexes mobilisées** : annexes 2.1 (conséquences de l'incident), 2.2 (constats de l'audit flash) et 2.3 (ISO/IEC 27001:2022, ISO 22301:2019, guide d'hygiène informatique).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Objectifs de sécurité (confidentialité, intégrité, disponibilité, traçabilité) définis et illustrés à LORVANNE | 0,5 |
| a-2 | Principes d'une politique fondée sur les risques et adaptée à l'école | 0,5 |
| b-1 | Gestion des identités et des accès : principe, pertinence (annexe 2.2), indicateur complet | 0,5 |
| b-2 | Authentification multifacteur : principe, pertinence, indicateur complet | 0,5 |
| b-3 | Segmentation : principe, pertinence, indicateur complet | 0,5 |
| b-4 | Sauvegardes isolées et testées : principe, pertinence, indicateur complet | 0,5 |
| c-1 | PCA et PRA distingués | 0,5 |
| c-2 | RTO et RPO définis et justifiés pour deux processus | 0,5 |

**Réponse indicative**

*2.3 a) – Objectifs et principes de la politique de sécurité*

Objectifs (0,5 pt) : la sécurité de l'information vise la **confidentialité** (seules les personnes autorisées accèdent aux données des étudiants, des vacataires et des entreprises, divulguées en novembre), l'**intégrité** (les notes et les copies sont exactes et complètes, ce qui fonde les diplômes), la **disponibilité** (la scolarité, les jurys, la paie et la facturation fonctionnent quand l'école en a besoin, et non après neuf jours d'arrêt) et la **traçabilité** (toute opération est attribuable à une personne, ce que les comptes d'administration partagés empêchent).

Principes de la politique de sécurité du système d'information (PSSI) (0,5 pt) :
- **fondée sur l'analyse des risques** : les mesures sont choisies et hiérarchisées à partir de la cotation (2.2 c) selon une méthode reconnue (EBIOS Risk Manager), et révisées chaque année ou après tout incident ;
- **portée par la direction** : approuvée par le conseil d'administration et la direction générale, qui fixent le niveau de risque accepté et les moyens ;
- **un périmètre unique** : la même politique pour le siège et les trois campus, pour tous les utilisateurs (salariés, vacataires, étudiants) et pour les prestataires ;
- **des rôles définis** : RSSI, déléguée à la protection des données, propriétaires des processus, directeurs de campus, équipes informatiques ;
- **une déclinaison opérationnelle** : charte informatique opposable à tous les utilisateurs, procédures (gestion des comptes, sauvegardes, gestion des incidents et des violations), plan de sensibilisation, à partir des 93 mesures de l'annexe A d'ISO/IEC 27001:2022 ou des 42 mesures du guide d'hygiène informatique ;
- **une approche systémique** : mesures organisationnelles, humaines et techniques, et non une liste d'équipements ;
- **un contrôle et une amélioration continue** (logique PDCA) : indicateurs, revues, exercices, audit de suivi.

Un indicateur accompagne la sensibilisation : taux de saisie du mot de passe lors des exercices d'hameçonnage simulé (60 salariés sur 610 en février 2027, environ 10 %), à ramener sous 2 %.

*2.3 b) – Quatre mesures prioritaires*

| Mesure (0,5 pt chacune) | Principe | Pertinence au regard de l'annexe 2.2 | Indicateur d'efficacité |
|---|---|---|---|
| Gestion des identités et des accès sur tout le cycle de vie des comptes | annuaire commun à l'école ; création, modification et désactivation des comptes déclenchées par les événements de gestion (contrat de vacation, embauche, départ) ; droits attribués par rôle selon le moindre privilège ; revue semestrielle des comptes et des droits par les responsables | 750 comptes d'anciens vacataires actifs, trois annuaires distincts, aucune procédure de départ (constat 1) | taux de comptes de vacataires désactivés dans les sept jours suivant la fin de leur vacation ; cible 100 % |
| Authentification multifacteur | preuve de l'identité par au moins deux facteurs de nature différente (mot de passe et téléphone ou clé, par exemple), en commençant par les comptes d'administration, la messagerie en ligne et l'accès à distance ; comptes d'administration nominatifs, réservés aux tâches d'administration | le compte hameçonné et le compte d'administration volé ne demandaient qu'un mot de passe ; neuf comptes d'administration partagés (constats 2 et 3) | taux de comptes protégés par une authentification multifacteur ; cible 100 % des comptes d'administration et d'accès à distance en septembre 2027, puis de tous les comptes |
| Segmentation | cloisonnement du réseau en zones (postes des étudiants, postes administratifs, serveurs de chaque campus, serveurs du siège), avec des échanges limités à ceux qui sont nécessaires, pour contenir la propagation d'une attaque | l'attaquant a pu explorer les serveurs du siège depuis Besançon ; postes des étudiants et serveurs sur le même réseau (constat 4) | part des serveurs des processus critiques placés dans une zone cloisonnée ; cible 100 % fin 2027 |
| Sauvegardes isolées et testées | au moins une copie déconnectée ou non modifiable, inaccessible avec les comptes ordinaires ; fréquence adaptée au RPO de chaque processus ; tests de restauration programmés, avec procès-verbal | sauvegarde en ligne chiffrée avec les serveurs ; aucun test sur les campus ; scolarité sauvegardée chaque semaine (constat 5) ; six semaines de notes perdues (annexe 2.1) | taux de réussite des tests de restauration dans le délai fixé par le RTO ; cible 100 % |

Les cinq indicateurs proposés (les quatre mesures et la sensibilisation) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Désactivation des comptes de vacataires | comptes de vacataires désactivés dans les sept jours suivant la fin de la vacation / vacations terminées | annuaire commun et contrats de vacation | mensuelle | 100 % (point de départ : 750 comptes d'anciens vacataires actifs en février 2027) | processus |
| Couverture de l'authentification multifacteur | comptes protégés par une authentification multifacteur / comptes actifs | annuaire commun | mensuelle | 100 % des comptes d'administration et d'accès à distance en septembre 2027 ; 100 % de tous les comptes fin 2027 (0 % en février 2027) | processus |
| Cloisonnement des serveurs critiques | serveurs des processus critiques placés dans une zone cloisonnée / serveurs des processus critiques recensés | inventaire et cartographie des zones | trimestrielle | 100 % fin 2027 | processus |
| Réussite des tests de restauration | restaurations réussies dans le délai du RTO / tests de restauration programmés | procès-verbaux de tests | trimestrielle | 100 % (aucun test sur les campus avant 2027) | processus |
| Résistance à l'hameçonnage | salariés ayant saisi leur mot de passe lors de l'exercice / salariés destinataires de l'exercice | résultats des exercices d'hameçonnage simulé | semestrielle | < 2 % (environ 10 % en février 2027) | apprentissage |

*2.3 c) – PCA, PRA, RTO et RPO*

Le **plan de continuité d'activité** (PCA) organise le maintien des activités critiques pendant la crise, au besoin en mode dégradé : priorités entre processus, procédures manuelles (listes d'émargement, relevés de notes papier, états d'heures sur formulaire), moyens de secours, cellule de crise et communication. Le **plan de reprise d'activité** (PRA) organise la reprise des systèmes et le retour à la normale après le sinistre : ordre de restauration, sauvegardes isolées, serveurs de remplacement, vérification de l'intégrité des données. Ils découlent de la PSSI et de l'analyse d'impact, et ne valent que s'ils sont testés ; en novembre 2026, l'école n'avait ni l'un ni l'autre (0,5 pt).

Le **RTO** (*Recovery Time Objective*) est la durée maximale d'interruption admissible d'un processus ; le **RPO** (*Recovery Point Objective*) est la perte de données maximale admissible, exprimée par l'ancienneté de la dernière sauvegarde exploitable. Pour deux processus (0,5 pt) :

| Processus | RTO | RPO | Justification |
|---|---|---|---|
| Scolarité, examens et jurys, en période d'examens et de jurys | 48 heures | 24 heures | un jury reporté retarde les diplômes et l'insertion (25 diplômés attendus par un employeur) ; au-delà d'une journée, les notes ne sont plus ressaisissables sans perte, alors que la seule copie disponible en 2026 avait six semaines ; hors période d'examens, un RTO de cinq jours ouvrés peut être admis |
| Paie, dans les cinq jours ouvrés qui précèdent le versement | 24 heures | 24 heures | le versement des rémunérations ne peut pas être différé (dix jours de retard pour les vacataires en 2026) ; les éléments variables saisis dans la journée restent ressaisissables à partir des états d'heures |

**Réponses tolérées**
- Toute valeur de RTO et de RPO cohérente et justifiée par le calendrier des processus ; RTO et RPO fixés pour la facturation des contrats d'apprentissage (par exemple cinq jours ouvrés et 24 heures).
- Présentation des mesures dans une démarche Zero Trust, si elle est décrite comme un cadre d'architecture (aucune confiance implicite, vérification de chaque accès) et non comme un produit.
- Indicateurs d'efficacité différents mais complets (stock de comptes de vacataires actifs sans vacation en cours, cible 0 ; délai moyen de désactivation, nombre de comptes d'administration partagés, cible 0 ; délai réel de restauration constaté lors d'un test), de même que le chiffrement des données sensibles ou la journalisation centralisée des accès, proposés en complément.
- Mention de NIS2, non attendue (absente de l'annexe 2.3) : admise si le candidat précise que la directive n'est pas transposée en France au 31/12/2026 et que son applicabilité à l'école n'est pas établie.

**Erreurs types**
- *PCA et PRA confondus ; RTO et RPO inversés ou omis* (`JUR-S02`, `ET-02`, `ET-03`) — « le PRA est le plan pendant la crise », « le RPO est le délai de reprise » ; juste : PCA pendant la crise, PRA pour le retour à la normale ; RTO = durée d'interruption, RPO = perte de données.
- *PSSI confondue avec la charte informatique* (`ET-27`) — juste : la PSSI fixe les objectifs, les règles et les responsabilités ; la charte décline les règles d'usage opposables aux utilisateurs.
- *Authentification multifacteur confondue avec un mot de passe complexe* (`ET-28`) — juste : au moins deux facteurs de nature différente.
- *Zero Trust présenté comme un produit* (`JUR-S03`, `ET-04`) — juste : un cadre d'architecture qui combine gestion des identités, authentification forte, cloisonnement et surveillance.
- *Mesures techniques détaillées ou indicateurs génériques* (`JUR-S05`, `ET-18`) — paramétrage d'équipements, ou « taux de sécurité » sans formule ni cible ; juste : mesures organisationnelles et d'architecture, chacune reliée à un constat et à un indicateur complet.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 27001:2022 ; ISO/IEC 27002:2022 | PSSI fondée sur les risques, mesures de l'annexe A, PDCA | `iso_27001_2022`, `iso_27002_2022` ; F12 § 1-2 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | comptes, authentification, cloisonnement, sauvegardes | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| ISO 22301:2019 | PCA, analyse d'impact | `iso_22301_2019` ; F12 § 4 | en vigueur |
| Modèle Zero Trust (avis de l'ANSSI, 2021) | cadre d'architecture (réponses tolérées) | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| Directive (UE) 2022/2555 (NIS 2) ; transposition française | mention tolérée, statut daté | `nis2`, `nis2_transposition_fr` ; F12 § 6 | non transposée au 31/12/2026 |

---

### 2.4 – Note de synthèse au conseil d'administration (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ».
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ».

**Annexes mobilisées** : annexes 1.1 (organigramme), 2.1 (incident et témoignages) et 2.2 (audit flash, demande du conseil).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| f-1 | Forme : destinataire, objet, 20 lignes au maximum, structure hiérarchisée, vocabulaire accessible à des administrateurs | 0,5 |
| f-2 | Diagnostic : appréciation globale et trois constats majeurs étayés par les annexes | 1 |
| f-3 | Priorités d'action assorties d'une échéance réaliste | 0,5 |
| f-4 | Rôles et responsabilités des six acteurs, dont le positionnement du RSSI et l'indépendance de la déléguée à la protection des données | 1 |

**Réponse indicative**

Note modèle (environ 18 lignes) :

<!-- note -->
**À l'attention du conseil d'administration — Objet : sécurité du système d'information, diagnostic et priorités (24 juin 2027)**

Appréciation globale : la sécurité n'est ni gouvernée ni pilotée ; l'incident de Besançon (neuf jours d'arrêt, données de 1 400 étudiants dérobées, dont un échantillon publié) en est la conséquence et peut toucher toute l'école.

Constats majeurs : 1) des accès non maîtrisés : 750 comptes d'anciens vacataires actifs, aucune authentification multifacteur, neuf comptes d'administration partagés ; 2) des sauvegardes jamais testées ni isolées, sans plan de continuité : six semaines de notes perdues ; 3) aucun responsable de la sécurité, aucune politique écrite, un registre des traitements non tenu depuis 2021.

Priorités : dès juillet 2027, désigner un RSSI ; d'ici septembre, authentification multifacteur des comptes sensibles, revue de tous les comptes, sauvegardes déconnectées testées chaque trimestre ; d'ici décembre, cloisonnement des réseaux, politique de sécurité adoptée, plan de continuité testé avant les jurys de novembre.

Rôles : le conseil fixe le niveau de risque accepté, approuve la politique et suit un tableau de bord semestriel ; la direction générale porte la politique, arbitre et finance ; le RSSI, rattaché à la directrice générale et indépendant des équipes informatiques, pilote les risques, les mesures et les incidents ; la déléguée à la protection des données, dotée du temps nécessaire, tient le registre et conseille ; les propriétaires des processus fixent les délais tolérables et valident les accès ; les directeurs de campus appliquent la politique et en rendent compte.
<!-- /note -->

Éléments d'appréciation :
- **diagnostic** (1 pt) : appréciation globale et trois constats parmi les accès, l'authentification, les sauvegardes et la continuité, la gouvernance, la conformité au RGPD ; chacun chiffré ;
- **priorités** (0,5 pt) : cohérentes avec la cotation (risques critiques d'abord), datées, réalistes au regard des 21 informaticiens et du budget ;
- **rôles** (1 pt) : le conseil d'administration fixe l'appétence au risque et contrôle ; la direction générale est responsable de la politique ; le RSSI, positionné auprès de la directrice générale avec une autorité fonctionnelle sur les trois campus, est distinct des équipes qu'il contrôle ; la déléguée à la protection des données informe, conseille et contrôle la conformité au RGPD, sans être responsable du traitement ni cumuler la fonction de RSSI ; les propriétaires des processus (scolarité, paie, apprentissage) expriment les besoins de continuité et valident les droits ; les directeurs de campus déploient la politique et font remonter les incidents.

**Réponses tolérées**
- Note rédigée en paragraphes ou en tirets, ou priorités présentées en tableau, dans la limite des 20 lignes.
- RSSI externalisé ou mutualisé à temps partiel dans l'attente d'un recrutement, s'il reste rattaché à la direction générale.
- Mention d'un comité de sécurité réunissant la direction générale, le RSSI, la déléguée et les directeurs de campus, ou d'un budget de sécurité à arbitrer par le conseil.

**Erreurs types**
- *Note trop longue, technique ou non hiérarchisée* (`JUR-S07`, `JUR-T07`) — dépasser 20 lignes, détailler des réglages techniques devant le conseil ; juste : appréciation, constats, priorités, rôles.
- *RSSI présenté comme un technicien ou subordonné aux équipes qu'il contrôle* (`ET-15`) — juste : rattachement à la direction générale, autorité fonctionnelle transverse.
- *Délégué à la protection des données confondu avec le RSSI* (`ET-29`) — juste : deux fonctions distinctes, la déléguée portant la conformité au RGPD.
- *Responsabilités attribuées à l'informatique seule* (`JUR-T11`) — juste : la sécurité engage le conseil, la direction, les métiers et les campus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Note de synthèse d'audit | appréciation, constats, recommandations, échéances | F10 § 5 | guide p. 266 |
| Acteurs de la sécurité | conseil et direction, RSSI, délégué à la protection des données | F12 § 1 ; F15 § 1 | guide p. 336 ; corrigé du sujet zéro p. 353 |
| RGPD | missions du délégué à la protection des données ; registre | `rgpd` ; F15 § 1-2 | applicable depuis le 25/05/2018 |

---

## DOSSIER 3 – CONDUIRE LE PROJET DE PLATEFORME PÉDAGOGIQUE ET PILOTER LES COÛTS DU SI (11 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Méthode de conduite du projet et cahier des charges | `1.5.a` Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ; `1.5.b` Méthodologies de gestion de projet (cycle en V, agile, hybride) ; `1.5.c` Élaboration d'un cahier des charges fonctionnel et technique | 3 |
| 3.2 Coût complet des deux options et souveraineté des données | `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `2.3.d` Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique | 3 |
| 3.3 Plan qualité du projet | `1.5.f` Mise en œuvre et contrôle du plan qualité ; `1.5.a` Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable | 1,5 |
| 3.4 Pilotage des coûts et tableau de bord du SI | `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord ; `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ; `1.2.e` Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) | 3,5 |
| **Dossier 3 – Conduire le projet de plateforme pédagogique et piloter les coûts du SI** |  | **11** |

Répartition indicative : connaissances (méthodes de projet, rubriques du cahier des charges, TCO, plan qualité, contrôle de gestion du SI, structure d'un tableau de bord : items 3.1 a-1, 3.2 a-1, 3.4 a-1, et pour moitié 3.1 b, 3.3 a et 3.4 b-1) environ 2,5 points ; analyse des annexes et recommandations environ 8,5 points. Durée conseillée : 11 points × 4,5 minutes ≈ 50 minutes.

---

### 3.1 – Méthode de conduite du projet et cahier des charges (3 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.a` « Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable » ; `1.5.b` « Méthodologies de gestion de projet (cycle en V, agile, hybride) » ; `1.5.c` « Élaboration d'un cahier des charges fonctionnel et technique ».

**Annexes mobilisées** : annexes 3.1 (situation actuelle, calendrier, besoins exprimés, options, témoignages) et 1.1 (organisation de l'école et de la fonction informatique).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cycle en V, méthodes agiles (Scrum) et approche hybride caractérisés et comparés (principe, atouts, limites) | 0,5 |
| a-2 | Trois contraintes du projet tirées de l'annexe 3.1 | 0,5 |
| a-3 | Recommandation justifiée d'une approche hybride, avec ce qui relève du cycle en V, ce qui relève des itérations, et les rôles | 1 |
| b-1 | Cahier des charges fonctionnel : rubriques et deux exigences fonctionnelles du cas | 0,5 |
| b-2 | Cahier des charges technique : rubriques et deux exigences techniques du cas | 0,5 |

**Réponse indicative**

*3.1 a) – Choix de la méthode*

Trois familles de méthodes (0,5 pt) :
- le **cycle en V** enchaîne l'expression du besoin, les spécifications, la conception et la réalisation, puis remonte par des tests en miroir de chaque niveau jusqu'à la recette ; il convient à un besoin stable et bien connu, se contractualise facilement au forfait et documente la recette, mais il expose à l'effet tunnel : les écarts au besoin apparaissent tard ;
- les **méthodes agiles**, dont Scrum, livrent le produit par incréments au cours d'itérations courtes (sprints d'un mois au plus), à partir d'un carnet de produit priorisé par la valeur ; le *Product Owner* porte le besoin, le *Scrum Master* garantit le cadre, les développeurs réalisent l'incrément. Elles conviennent à un besoin évolutif, mais exigent des utilisateurs disponibles et un responsable du produit qui décide ;
- l'**approche hybride** conduit le cadrage et le socle en cycle en V (architecture, interfaces, reprise des données, recette d'ensemble) et les modules dont le besoin se découvre à l'usage en itérations.

Contraintes du projet (0,5 pt pour trois) :
- **une date impossible à déplacer** : mise en service pour tous les programmes à la rentrée de septembre 2028, contrat signé en septembre 2027 ; la directrice des programmes veut en outre un premier parcours vendable dès janvier 2028 ;
- **des besoins de deux natures** : un socle connu et stable (cours en ligne, intégration avec la scolarité, examens surveillés, accessibilité, reprise des 2 500 espaces de cours), à côté d'une offre aux entreprises dont les besoins « se découvriront avec les premiers clients » (Mme ROUVIÈRE) ;
- **une solution existante à paramétrer**, non un développement complet : progiciel en mode SaaS (A) ou solution libre complétée de quelques développements (B), avec un prestataire sous contrat ;
- **des ressources rares** : enseignants indisponibles pendant les examens et l'été, équipe du siège de six personnes qui « n'a jamais conduit un projet de cette taille » et doit faire tourner l'existant, aucun directeur des systèmes d'information (annexe 1.1).

Recommandation (1 pt) : une **approche hybride**.
- En **cycle en V**, avec des jalons fixes : cadrage et cahier des charges (avant le choix de juin 2027), contrat (septembre 2027), paramétrage et interface avec le progiciel de scolarité, reprise des espaces de cours (à vérifier par les enseignants entre février et avril 2028, hors des sessions d'examen et avant l'été), recette d'ensemble au printemps 2028, bascule en août 2028. Ce socle conditionne la rentrée : il doit être spécifié, contractualisé et recetté de façon complète.
- En **itérations courtes** : l'espace des entreprises clientes et les parcours de la formation des cadres, construits avec un premier parcours pilote dès le début de 2028, puis enrichis sprint après sprint à partir des retours des entreprises ; le *Product Owner* est désigné par la directrice des programmes, qui priorise le carnet de produit.
- Un **comité de pilotage** mensuel, présidé par Mme FERRIOL (sponsor), arbitre entre les deux volets ; la date de septembre 2028 est un jalon ferme, le contenu des itérations est la variable d'ajustement.

Un cycle en V intégral ne permettrait pas de livrer le parcours de janvier 2028 ni d'ajuster l'offre aux entreprises ; un projet entièrement agile laisserait sans engagement contractuel ni recette d'ensemble l'interface avec la scolarité et la reprise des contenus, dont dépend la rentrée.

*3.1 b) – Contenu du cahier des charges*

Le cahier des charges exprime le besoin de l'école (maîtrise d'ouvrage), indépendamment de la solution, et sert de base au choix, au contrat et à la recette ; chaque exigence est priorisée (par exemple selon la méthode MoSCoW) et assortie d'un critère d'acceptation vérifiable.

- **Partie fonctionnelle** (ce que la plateforme doit permettre) : contexte et objectifs mesurables (plan « LORVANNE 2030 », fin de vie de la plateforme de 2014), périmètre (programmes, formation des cadres, environ 6 000 utilisateurs), profils d'utilisateurs, processus cibles, exigences fonctionnelles priorisées, volumétrie, contraintes (calendrier, protection des données, accessibilité), critères d'acceptation. Exigences du cas, deux attendues : espace réservé à chaque entreprise cliente pour suivre l'assiduité et les résultats de ses cadres ; examens surveillés à distance avec enregistrement et visionnage des signalements par un surveillant ; application automatique du temps majoré ; inscription automatique de chaque étudiant aux cours de son programme (0,5 pt).
- **Partie technique** (contraintes d'environnement et de service) : mode d'hébergement et localisation des données, interfaces avec le progiciel de scolarité et les annuaires des comptes, performances et disponibilité, compatibilité avec les outils d'accessibilité et les téléphones mobiles, exigences de sécurité et de protection des données, reprise des données, réversibilité et formats, niveaux de service et assistance. Exigences du cas, deux attendues : création et suppression automatiques des comptes et transfert des notes vers le progiciel de scolarité, sans ressaisie ; 600 étudiants composant en même temps sans interruption ; disponibilité mesurée sur les plages d'usage et pendant les examens ; restitution des données dans des formats ouverts en fin de contrat ; navigation au clavier seul et avec un lecteur d'écran (0,5 pt).

**Réponses tolérées**
- Recommandation d'un **cycle en V** pour l'ensemble du projet, si le candidat organise un pilote de la formation des cadres avant la rentrée et justifie le choix par la date fixe et le contrat au forfait : 0,5 point sur l'item a-3.
- Kanban mentionné pour le suivi des demandes d'évolution après la mise en service : valorisé.
- Une exigence classée dans l'autre partie (l'accessibilité, fonctionnelle ou technique selon la formulation) : acceptée si elle est vérifiable.

**Erreurs types**
- *Agile confondu avec l'absence de méthode ou de cahier des charges* (`ET-32`) — « en agile, pas besoin de cahier des charges » ; juste : les itérations partent d'un carnet de produit priorisé, avec un responsable du produit et des critères d'acceptation.
- *Méthodes récitées sans lien avec le cas* (`JUR-T01`, `JUR-P02`) — phases du cycle en V décrites sans les contraintes de LORVANNE ; juste : le choix découle de la date fixe, de la nature des besoins et des ressources disponibles.
- *Rôles Scrum faux ou maîtrise d'ouvrage et maîtrise d'œuvre inversées* (`ET-32`) — « le Scrum Master est le chef de projet », « le fournisseur rédige le cahier des charges » ; juste : l'école, maîtrise d'ouvrage, exprime le besoin et recette ; le fournisseur, maîtrise d'œuvre, réalise.
- *Cahier des charges réduit à une liste de fonctions* — exigences sans priorité ni critère d'acceptation, ou cahier des charges qui décrit une solution ; juste : besoin exprimé, priorisé et vérifiable.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| *The Scrum Guide* (Schwaber et Sutherland, novembre 2020) | rôles, sprint d'un mois au plus, carnet de produit | `scrum_guide_2020` / F05 § 2.2 | en vigueur |
| Cycle en V, approche hybride, MoSCoW, cahier des charges | méthodes et critères de choix | F05 § 2 et § 3 | notions de cours |

---

### 3.2 – Coût complet des deux options et souveraineté des données (3 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ».
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.d` « Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique ».

**Annexes mobilisées** : annexes 3.1 (offres, caractéristiques des options, témoignages) et 3.3 (RGPD, décision d'adéquation, Data Act, SecNumCloud, référentiel du Cigref).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | TCO défini : coût complet sur le cycle de vie, postes, horizon, coûts cachés | 0,5 |
| a-2 | Offres (420 et 480 k€) puis TCO complets (810 et 750 k€) comparés et interprétés : le classement s'inverse | 0,5 |
| b | ROI discuté qualitativement : deux gains attendus et leurs conditions | 0,5 |
| c-1 | Localisation et droit applicable au fournisseur analysés (adéquation n'est pas immunité ; option irlandaise) | 0,5 |
| c-2 | Réversibilité et dépendance analysées (formats, assistance, Data Act, évolutions décidées par l'éditeur) | 0,5 |
| c-3 | Recommandation argumentée et assortie de conditions | 0,5 |

**Réponse indicative**

*3.2 a) – TCO des deux options*

Le coût total de possession (TCO) est le coût complet d'une solution sur son cycle de vie : acquisition, mise en œuvre (intégration, reprise des données, formation, conduite du changement), exploitation (hébergement, maintenance, assistance, administration interne), utilisation (temps des utilisateurs, indisponibilités) et sortie (réversibilité). Il se calcule sur un horizon donné, ici trois ans, sans actualisation, et inclut les **coûts cachés**, absents des offres mais supportés par l'organisation (0,5 pt).

| En k€, sur trois ans | Option A (SaaS) | Option B (libre, ARDÉVAL) |
|---|---|---|
| Total des offres | 420 | 480 |
| Reprise des contenus (prestation) | 60 | 20 |
| Temps des enseignants (5 000 h ou 1 250 h à 40 €) | 200 | 50 |
| Maintien de l'ancienne plateforme | 40 | 20 |
| Temps de l'équipe du siège (0,5 ou 1 poste à 60 k€ par an) | 90 | 180 |
| Coûts cachés | 390 | 270 |
| **TCO complet** | **810** | **750** |

Sur les seules offres, l'option A paraît moins chère de 60 k€ ; une fois les coûts cachés intégrés, l'option B l'est de 60 k€ : **le classement s'inverse**. Les coûts cachés représentent près de la moitié du TCO de A, dont 200 k€ de temps d'enseignants : c'est un coût d'opportunité plutôt qu'un décaissement, mais aussi un risque de calendrier, puisque les enseignants ne sont disponibles ni pendant les examens ni en été. L'hébergement en Irlande ajouterait 30 k€ à l'option A (840 k€). L'option A est presque entièrement en charges de fonctionnement (abonnement) ; l'option B comporte davantage de dépenses de mise en place (intégration, développements), puis des coûts récurrents proches de ceux de A : environ 150 k€ par an pour A et 160 k€ pour B, temps de l'équipe compris. L'écart tient donc surtout à la reprise des contenus (0,5 pt).

*3.2 b) – Retour sur investissement*

Le retour sur investissement rapporte les gains nets attendus au coût du projet. Il ne peut être chiffré ici : les gains principaux ne sont ni mesurés ni attribuables au seul projet, et les marges de la formation des cadres ne sont pas connues. Deux gains attendus, avec leurs conditions (0,5 pt) :
- **la croissance de la formation des cadres en ligne** (0,3 M€ en 2025-2026, 5 M€ visés en 2029-2030) : la plateforme en est une condition nécessaire mais non suffisante ; le gain dépend de l'offre de parcours, de l'effort commercial et de l'espace des entreprises clientes ;
- **des coûts et des risques évités** : renouvellement de serveurs hors garantie et d'une version qui n'est plus maintenue, interruptions pendant les examens (une dizaine d'heures en janvier 2027, dont la moitié pendant une session), ressaisie des notes et création hebdomadaire des comptes ; à condition que l'interface avec la scolarité fonctionne dès la rentrée ;
- autres gains qualitatifs : accessibilité pour 160 étudiants, satisfaction des étudiants et des enseignants, usage mobile, image de l'école face à ses concurrents.

Le projet se justifie donc comme un investissement stratégique au service du plan, dont les bénéfices seront suivis par des indicateurs (chiffre d'affaires en ligne, disponibilité pendant les examens, saisies supprimées) plutôt que par un ratio calculé a priori.

*3.2 c) – Informatique en nuage, souveraineté et recommandation*

La souveraineté numérique désigne la capacité de l'école à garder la maîtrise de ses données : où elles sont, quel droit s'applique au fournisseur qui les détient, et si elle peut en changer.

- **Localisation et droit applicable** (0,5 pt) : avec l'option A, les données d'environ 6 000 utilisateurs, leurs notes et les enregistrements vidéo des examens sont hébergés aux États-Unis. Le transfert est aujourd'hui permis, puisque l'éditeur adhère au cadre couvert par la décision d'adéquation du 10/07/2023 (annexe 3.3), mais ce cadre succède à un cadre invalidé en 2020 et peut l'être à son tour. Surtout, l'éditeur, de droit américain, reste soumis aux lois de son pays, y compris lorsqu'elles ont une portée extraterritoriale : l'option d'hébergement en Irlande améliore la localisation, pas l'immunité au droit étranger. L'option B, hébergée en France par une société française, y est beaucoup moins exposée ; seule une qualification SecNumCloud l'attesterait. L'absence de qualification SecNumCloud n'est pas rédhibitoire pour des données pédagogiques ; la grille du Cigref (sécurité, immunité, dépendance) peut servir à comparer les offres. Dans les deux cas, le fournisseur est sous-traitant de l'école, qui reste responsable de ses données et de leurs usages : un contrat conforme à l'article 28 du RGPD est nécessaire, et l'analyse d'impact s'impose pour la surveillance filmée des examens.
- **Réversibilité et dépendance** (0,5 pt) : l'option A limite la sortie à un export des notes au format tableur pendant 30 jours et à des cours dans le format propre de l'éditeur, l'assistance étant facturée en sus ; l'éditeur décide seul des évolutions. Changer de fournisseur reproduirait la reprise manuelle de 5 000 heures. Le Data Act, applicable depuis le 12/09/2025, facilite le changement de fournisseur d'informatique en nuage, mais la portabilité doit être organisée par le contrat. L'option B repose sur des formats ouverts, une restitution complète avec assistance et une licence libre : l'école peut changer d'hébergeur sans changer de plateforme. Sa dépendance tient aux développements propres d'ARDÉVAL (espace des entreprises, transfert des notes), à documenter et à livrer sous licence libre.
- **Recommandation** (0,5 pt) : retenir l'**option B**, moins chère en coût complet, plus réversible et plus souveraine, sous trois conditions : un pilote sur un parcours de la formation des cadres dès février 2028 (un mois après le souhait de la directrice des programmes), sur un environnement où les espaces de cours sont repris à blanc, pour que les enseignants vérifient les 1 250 heures de reprise entre février et avril 2028, hors des sessions d'examen et avant l'été, avec une décision de poursuite au printemps 2028 ; des jalons contractuels fermes, car la mise en service complète de mai 2028 ne laisse que quatre mois, qui coïncident avec les examens et l'été ; un poste à temps plein affecté au pilotage d'ARDÉVAL au siège, sans quoi l'existant en pâtira. Les coûts de l'option A ne couvrent ni l'hébergement dans l'Union européenne ni une réversibilité réelle.

**Réponses tolérées**
- Recommandation de l'**option A**, si le candidat la justifie par le calendrier (marge de huit mois, toutes les fonctions en standard, application mobile, ou relève que la marge de B coïncide avec les périodes où les enseignants ne sont pas disponibles) et l'assortit de conditions sur la souveraineté (hébergement en Irlande, export des cours dans un format ouvert, assistance à la sortie comprise) : 0,5 point sur l'item c-3.
- Temps des enseignants exclu du TCO et traité comme un coût d'opportunité, si le candidat le signale et en tire la conséquence sur le calendrier (offres 420 et 480, autres coûts cachés 190 et 220, TCO 610 et 700) : accepté sur l'item a-2.
- Données des 160 étudiants bénéficiant d'un aménagement : le candidat qui demande de n'enregistrer que l'aménagement (temps majoré), sans son motif, et d'inclure ce point dans l'analyse d'impact est valorisé.
- Temps de l'équipe du siège pendant l'année de mise en place (2027-2028) ajouté au TCO, posé comme hypothèse : accepté, l'annexe comptant trois années d'utilisation.
- Mention du modèle de responsabilité partagée de l'informatique en nuage et de la distinction SaaS / hébergement d'une solution libre (IaaS ou PaaS chez l'hébergeur) : valorisée.
- Délai de récupération évoqué en principe, sans chiffrage : valorisé.

**Erreurs types**
- *TCO réduit au prix des offres* (`ET-33`, `JUR-A03`) — comparer 420 et 480 k€ et conclure en faveur de A ; juste : intégrer la reprise des contenus, le temps des enseignants et de l'équipe, et le maintien de l'ancienne plateforme.
- *TCO et ROI confondus, ou TCO actualisé* (`ET-33`) — « le ROI de l'option B est de 60 k€ » ; juste : le TCO est un coût complet non actualisé, le ROI rapporte des gains à un coût.
- *Hébergement souverain confondu avec hébergement en Europe ou en France* (`ET-37`) — « avec l'option irlandaise, l'option A devient souveraine » ; juste : le droit applicable au fournisseur compte autant que la localisation.
- *En SaaS, la responsabilité des données est celle du fournisseur* (`ET-30`, `JUR-G11`) — juste : l'école reste responsable de ses données, des comptes et des usages ; le fournisseur est sous-traitant.
- Hors sujet : analyser le contrat comme un juriste ou développer le droit des transferts de données (UE 1) ; le dossier attend l'enjeu de maîtrise des données.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| TCO, coûts cachés, CAPEX / OPEX, ROI | coût complet sur trois ans | F09 § 3 | notions de cours |
| RGPD, règlement (UE) 2016/679 | transferts hors de l'Union, sous-traitant (art. 28), analyse d'impact | `rgpd` / F15 | en vigueur |
| Décision d'adéquation UE-États-Unis du 10/07/2023 | transferts vers les organisations adhérentes | `dpf_ue_usa_2023` / F15 | en vigueur |
| Règlement (UE) 2023/2854 (Data Act) | changement de fournisseur d'informatique en nuage | `data_act` / F03 § 5.3 | applicable depuis le 12/09/2025 |
| SecNumCloud, version 3.2 (ANSSI) | qualification des offres de confiance | `secnumcloud_3_2` / F03 § 5.3 | en vigueur |
| Référentiel du cloud de confiance du Cigref | sécurité, immunité, maîtrise de la dépendance | `cigref_cloud_confiance` / F03 § 5.3 | publié |

---

### 3.3 – Plan qualité du projet (1,5 point)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.f` « Mise en œuvre et contrôle du plan qualité » ; `1.5.a` « Piloter un projet de système d'information, depuis la rédaction du cahier des charges jusqu'à l'analyse des risques et du plan qualité, dans une logique de performance durable ».

**Annexes mobilisées** : annexe 3.1 (besoins exprimés, calendrier, témoignages).

**Barème indicatif (1,5 pt)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Responsabilités du projet réparties (sponsor, comité de pilotage, maîtrise d'ouvrage et utilisateurs clés, maîtrise d'œuvre), appliquées aux acteurs du cas | 0,5 |
| b | Recette organisée (technique, fonctionnelle, accessibilité, examen blanc, procès-verbal) et trois critères d'acceptation vérifiables | 0,5 |
| c | Un indicateur de qualité complet (formule, source, fréquence, cible, axe), relié à un critère d'acceptation | 0,5 |

**Réponse indicative**

Le plan qualité du projet fixe l'organisation, les règles et les contrôles qui garantissent que la plateforme livrée répond au cahier des charges : rôles, revues, gestion des changements, plan de tests et recette, critères d'acceptation et indicateurs.

- **Responsabilités** (0,5 pt) : Mme FERRIOL, sponsor, arbitre et préside le comité de pilotage mensuel (directrice des programmes, directeur administratif et financier, directeurs de campus, chef de projet, fournisseur) ; la directrice des programmes porte la maîtrise d'ouvrage et désigne le responsable du produit pour l'offre aux entreprises ; les utilisateurs clés rédigent et exécutent les cas de test : M. TERVILLAC pour les enseignants, la scolarité pour l'interface et les notes, Mme FAVRIGNY pour l'accessibilité, une ou deux entreprises clientes pour le pilote ; le fournisseur, maîtrise d'œuvre, réalise et conduit la recette technique ; M. CORNAVIN et l'équipe du siège pilotent l'interface avec le progiciel de scolarité ; la personne chargée de la protection des données est consultée sur la surveillance filmée des examens. Un tableau RACI formalise ces rôles.
- **Recette et critères d'acceptation** (0,5 pt) : recette technique par le fournisseur, puis recette fonctionnelle par l'école sur un cahier de recette dont chaque cas de test est relié à une exigence ; recette d'accessibilité menée par la référente handicap avec des étudiants concernés ; examen blanc en conditions réelles ; reprise des contenus à blanc puis vérifiée par chaque enseignant ; anomalies classées (bloquante, majeure, mineure) ; procès-verbal de recette, avec ou sans réserves, et décision de mise en service par le comité de pilotage avant l'été 2028. Trois critères d'acceptation parmi : toutes les exigences essentielles validées et aucune anomalie bloquante ouverte ; un examen blanc de 600 étudiants simultanés sans interruption, avec transfert automatique des notes au progiciel ; des parcours types utilisables au clavier seul et avec un lecteur d'écran, validés par Mme FAVRIGNY ; tous les espaces de cours repris validés par leur enseignant.
- **Indicateur de qualité** (0,5 pt pour un indicateur complet, relié à un critère d'acceptation) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de réussite des cas de test des exigences essentielles | cas de test réussis des exigences essentielles / cas de test des exigences essentielles | cahier de recette et outil de suivi des anomalies | hebdomadaire pendant la recette | 100 % et aucune anomalie bloquante ouverte avant le procès-verbal de recette (printemps 2028) | processus |

**Réponses tolérées**
- Autres indicateurs complets : taux d'espaces de cours repris et validés par leur enseignant (espaces repris et validés / 2 500 espaces actifs ; tableau de suivi de la reprise des contenus ; hebdomadaire ; 100 % fin avril 2028 ; processus), nombre d'anomalies bloquantes ouvertes (cible 0 à la mise en service), taux de disponibilité pendant l'examen blanc (cible 100 %), part des parcours types validés en accessibilité (cible 100 %), taux de notes transférées sans ressaisie (cible 100 %) ; axe « client » accepté pour un indicateur tourné vers les utilisateurs.
- Mention de la norme ISO 9001 (édition 2026) comme cadre de management de la qualité : valorisée sans être exigée.
- Mention de la maintenance corrective et évolutive après la mise en service : valorisée.

**Erreurs types**
- *Recette confondue avec les tests du fournisseur* — laisser au seul prestataire la validation de la plateforme ; juste : la recette fonctionnelle appartient à la maîtrise d'ouvrage et se conclut par un procès-verbal.
- *Indicateurs génériques* (`ET-18`, `JUR-A02`) — « taux de satisfaction » sans formule, source ni cible ; juste : indicateur relié à un critère d'acceptation du projet.
- *Plan qualité réduit à une norme* (`ET-01`) — « appliquer ISO 9001 » ; juste : rôles, recette, critères et indicateurs propres au projet ; la norme n'en est qu'un cadre possible.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Plan qualité, recette, procès-verbal, RACI | organisation de la qualité du projet | F05 § 1 et § 6 | notions de cours |
| ISO 9001:2026 — Systèmes de management de la qualité | cadre de management de la qualité (réponse tolérée) | `iso_9001_2026` / F05 § 6 | en vigueur |

---

### 3.4 – Pilotage des coûts et tableau de bord du SI (3,5 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ».
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.e` « Construction et pilotage de tableaux de bord SI intégrant des dimensions ESG (environnementales, sociales, de gouvernance) ».

**Annexes mobilisées** : annexes 3.2 (tableau de bord, budget du SI par nature et par entité, consommation électrique), 1.1 (chiffres clés, fonction informatique) et 3.1 (plateforme, options).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fondamentaux du contrôle de gestion du SI : coût complet, centres de coûts, inducteurs, répartition ou refacturation, lien entre coût et valeur | 0,5 |
| a-2 | Trois critiques du tableau de bord actuel, chacune fondée sur l'annexe 3.2 | 0,5 |
| a-3 | Méthode de répartition des coûts entre les campus et inducteurs justifiés | 0,5 |
| b-1 | Structure du tableau de bord : destinataire, fréquence, axes, équilibre performance / risques / coûts, ESG intégré | 0,5 |
| b-2 | Cinq indicateurs complets couvrant les quatre dimensions (voir la gradation) | 1,5 |

**Gradation de la notation** (item b-2) : 0,5 point pour deux ou trois indicateurs complets et pertinents ; 1 point pour quatre, ou pour cinq qui ne couvrent pas les quatre dimensions ; 1,5 point pour cinq indicateurs complets couvrant la performance, les risques, les coûts et l'ESG. Un indicateur auquel manque la formule, la source, la fréquence, la cible ou l'axe n'est pas compté.

**Réponse indicative**

*3.4 a) – Contrôle de gestion du SI, critique et répartition*

Le contrôle de gestion appliqué au système d'information vise à connaître le coût complet des services informatiques (coûts directs, indirects et cachés), à le rattacher aux services rendus et aux entités qui les consomment au moyen de centres de coûts et d'inducteurs, éventuellement à le répartir ou à le refacturer, et à le rapprocher de la valeur produite (niveau de service, contribution à la stratégie), au moyen d'indicateurs assortis de cibles. Le budget du SI de LORVANNE, 2,9 M€, représente environ 4 % des produits, dont 0,4 M€ seulement (14 %) pour des projets nouveaux (0,5 pt).

Critiques du tableau de bord actuel, trois attendues (0,5 pt) :
- **des indicateurs techniques, d'activité et sans cible** : tickets, postes, serveurs et téraoctets décrivent un volume, pas une performance ; aucun ne mesure la satisfaction, le délai de résolution ou la contribution au plan « LORVANNE 2030 », et aucun n'a de cible ;
- **des mesures qui masquent les problèmes** : une disponibilité de 98,6 % mesurée 24 heures sur 24 en janvier correspond à une dizaine d'heures d'interruption, dont la moitié pendant les examens en ligne ; mesurée sur les plages d'usage et les sessions d'examen, la performance serait jugée tout autrement ;
- **un périmètre incomplet et aucune donnée de coût** : les demandes traitées par les campus ne figurent pas dans le tableau de bord ; les dépenses des campus ne sont consolidées qu'à la clôture ; le 1,7 M€ du siège (près de 60 % du budget) n'est rattaché à aucun service ni réparti ; aucun indicateur de risque ni d'environnement, alors que la consommation des salles est connue (200 MWh) ;
- **un destinataire unique** : adressé au seul directeur administratif et financier, le tableau de bord ne sert ni la direction générale ni les directeurs de campus, qui ignorent ce que l'informatique leur coûte.

Méthode de répartition (0,5 pt) : regrouper les dépenses du SI, siège et campus, en **centres de coûts par service** (postes de travail et assistance, applications de gestion, plateforme pédagogique, réseau et liaisons entre campus), consolidés chaque trimestre ; répartir le coût de chaque service entre les campus et la formation des cadres selon un **inducteur** représentatif de sa consommation :
- plateforme pédagogique : nombre d'utilisateurs actifs, ou à défaut d'étudiants (2 900, 1 400 et 600), les cadres en formation étant imputés à la formation des cadres ;
- postes de travail et assistance : nombre de postes (800, 400 et 200), puis nombre de demandes lorsqu'un outil commun les comptera ;
- applications de gestion : nombre d'étudiants ou d'utilisateurs.

Les campus n'étant pas des entités juridiques distinctes, il s'agit d'une **répartition analytique** plutôt que d'une facturation ; elle se fait à un coût standard fixé en début d'exercice, pour ne pas reporter sur les campus les inefficacités de l'informatique, et elle est validée par le comité de direction. Elle rend visibles des écarts aujourd'hui ignorés : avant toute répartition du siège, le SI du campus de Chalon-sur-Saône coûte environ 330 € par étudiant, contre 200 € environ à Dijon (0,2 M€ pour 600 étudiants, contre 0,6 M€ pour 2 900).

*3.4 b) – Structure et indicateurs du tableau de bord du SI*

Structure (0,5 pt) : un tableau de bord stratégique du SI, présenté chaque trimestre au comité de direction, limité à une douzaine d'indicateurs, organisé selon les axes du tableau de bord prospectif adaptés au SI (IT Balanced Scorecard de Van Grembergen, d'après Kaplan et Norton) : contribution financière, utilisateurs, processus, orientation future ; les indicateurs ESG sont intégrés à ces axes et non isolés. Chaque indicateur porte une cible, un seuil d'alerte et un responsable ; le tableau équilibre performance, risques et coûts. Les indicateurs techniques actuels restent dans le tableau de bord opérationnel des équipes. Dans le tableau ci-dessous, la colonne « Axe » emploie les noms usuels du tableau de bord prospectif (financier, client, processus) ou, pour les indicateurs de risque et d'ESG, la dimension ESG qu'ils portent : l'indicateur de risque relève de l'axe processus (dimension gouvernance), l'indicateur ESG de l'axe orientation future ou processus (dimension environnement). Les deux façons de nommer les axes sont acceptées.

Indicateurs (1,5 pt selon la gradation) :

| Dimension | Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|---|
| Coûts | Coût complet du SI par étudiant | dépenses du SI consolidées (siège et campus) / nombre d'étudiants inscrits | comptabilité analytique, centres de coûts du SI | trimestrielle | au plus 600 € par étudiant en 2028-2029 (environ 590 € en 2025-2026), malgré la nouvelle plateforme | financier |
| Performance | Disponibilité de la plateforme pédagogique sur les plages d'usage | heures de disponibilité sur les plages d'usage (7 h – 23 h et sessions d'examen) / heures des plages d'usage | rapports de niveau de service du fournisseur, contrôlés par l'école | mensuelle | au moins 99,5 % et aucune interruption pendant une session d'examen | processus |
| Performance | Taux de demandes résolues dans le délai convenu, tous campus | demandes résolues dans le délai convenu / demandes closes au siège et sur les campus | outil commun de suivi des demandes, à mettre en place | mensuelle | au moins 90 % à la rentrée 2028 | client |
| Risques | Part des applications critiques réversibles et hébergées dans l'Union européenne | applications critiques dotées d'une clause de réversibilité et dont les données sont hébergées dans l'Union / applications critiques inventoriées | inventaire des applications et registre des contrats | semestrielle | 100 % en 2029 | gouvernance |
| ESG | Consommation électrique du SI, hébergement externe compris | consommation relevée dans les salles informatiques de l'école + consommation déclarée par les hébergeurs pour les services de l'école (MWh) | compteurs des salles et déclarations contractuelles des hébergeurs | trimestrielle | au plus 150 MWh en 2029-2030 (200 MWh en 2025-2026) | environnement |

La part du budget consacrée aux projets nouveaux (14 % en 2025-2026) et le chiffre d'affaires de la formation des cadres en ligne peuvent compléter l'axe « orientation future ».

**Réponses tolérées**
- Autres indicateurs complets et contextualisés : part du budget du SI consacrée aux projets nouveaux (cible 25 % en 2029-2030), satisfaction des étudiants et des enseignants à l'égard de la plateforme (enquête annuelle), part des parcours en ligne conformes aux exigences d'accessibilité (axe social, cible 100 %), durée moyenne d'usage des postes remplacés (axe environnement), coût de la plateforme par utilisateur actif.
- Un indicateur de risque lié à la sécurité (part des comptes désactivés au départ de leur titulaire, par exemple) : accepté pour la dimension « risques ».
- Refacturation interne à un coût standard proposée au lieu d'une répartition analytique, si le candidat en montre l'effet sur la responsabilisation des campus : accepté.
- Axes « parties prenantes » ou « ESG » nommés comme un cinquième axe, si les indicateurs y restent reliés aux autres axes.

**Erreurs types**
- *Tableau de bord limité aux indicateurs techniques ou indicateurs génériques* (`ET-18`, `JUR-A02`) — reprendre tickets et serveurs en ajoutant des cibles ; juste : indicateurs de performance, de qualité de service, de coût et de risque, reliés aux objectifs de l'école.
- *Indicateurs ESG isolés* (`ET-18`) — une liste « verte » séparée du tableau de bord ; juste : indicateurs ESG intégrés aux axes et suivis par le même comité.
- *Empreinte déplacée prise pour une empreinte réduite* — se féliciter de la baisse de consommation des salles de l'école après le départ des serveurs de la plateforme ; juste : l'externalisation déplace la consommation chez l'hébergeur, qui doit être mesurée.
- *Contrôle de gestion du SI réduit au suivi du budget* (`ET-33`) — juste : coût complet par service, inducteurs, lien entre coût et valeur ; le calcul d'écarts n'est pas attendu dans cette UE.
- *Répartition sans inducteur ou à parts égales* (`JUR-A03`) — « chaque campus paie un tiers » ; juste : un inducteur qui reflète la consommation (étudiants, postes, demandes).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| IT Balanced Scorecard (Van Grembergen, 2001) | axes du tableau de bord du SI | `van_grembergen_it_bsc` / F09 § 4.1 | modèle théorique |
| Balanced Scorecard (Kaplan et Norton, 1992) | tableau de bord prospectif | F09 § 4.1 | modèle théorique |
| Contrôle de gestion du SI : centres de coûts, inducteurs, refacturation | fondamentaux | F09 § 2 | notions de cours |
