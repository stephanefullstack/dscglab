# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 5 — Dossier 2 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 gouvernance et référentiels, F10 audit du SI, F12 sécurité et résilience, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Les tests techniques de sécurité, le paramétrage des équipements, la démarche de certification d'une norme, l'analyse juridique du RGPD au-delà du délégué à la protection des données, du registre et de la notification de l'annexe 2.3, ainsi que toute évaluation de l'incidence de l'incident sur les comptes de l'école, sont hors programme et ne sont pas attendus. La répartition par sous-question et par item est une proposition.

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
