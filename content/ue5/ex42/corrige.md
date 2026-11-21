# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 42 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 audit et fiabilisation, F12 sécurité et résilience, F14 numérique responsable, F15 RGPD opérationnel, fiche commune CSRD, ESRS et Omnibus, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

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
