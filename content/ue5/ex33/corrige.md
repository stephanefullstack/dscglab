# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 33 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 audit du SI, F12 sécurité et résilience, F13 intelligence artificielle, F14 numérique responsable, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 L'audit des habilitations aux dossiers des personnes accompagnées | `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ; `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. | 3 |
| 3.2 Les risques pesant sur les données des personnes accompagnées | `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. | 3 |
| 3.3 La politique de cybersécurité et la gestion d'une crise cyber | `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ; `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) (ici, la gestion des identités et des accès du principe 1) | 3,5 |
| 3.4 Une stratégie de numérique responsable, accessible et éthique | `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété ; `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ; `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements | 3,5 |
| **Dossier 3 – Sécuriser l'accès aux données, préparer une crise cyber, rendre le numérique plus responsable** |  | **13** |

Répartition indicative : connaissances (audit du SI et contrôle interne, typologie des risques, nature des référentiels, politique de sécurité et triade CID, gouvernance orientée RSE) 2,5 points (items 3.1 a-1, 3.2 a-1 et b-1, 3.3 a-1, 3.4 a-1) ; analyse des annexes et recommandations 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – L'audit des habilitations aux dossiers des personnes accompagnées (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance » ; `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; l'audit SI suppose une approche multidisciplinaire et une posture critique vis-à-vis de la gouvernance.

**Annexes mobilisées** : annexe 3.1 (comptes, processus actuels, dossier unique, demande du conseil, témoignages), annexe 3.4 (RGPD, guide de la sécurité des données personnelles, guide d'hygiène de l'ANSSI, ISO/IEC 27001:2022) et annexe 1.1 (organigramme, établissements, effectif).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit du SI défini (examen indépendant et méthodique, au regard d'un référentiel, débouchant sur des recommandations) et distingué du contrôle interne (dispositif permanent des opérationnels, que l'audit évalue) | 0,5 |
| a-2 | Démarche appliquée : objectifs, périmètre (trois logiciels, comptes nominatifs, partagés, d'éditeur ; préparation des profils et des droits des familles du dossier unique), étapes de juin à septembre 2027 et livrables, indépendance vis-à-vis de la DSI | 0,5 |
| b-1 | Tableau du processus « arrivée, mobilité, départ » : acteur, risque, contrôle interne attendu pour chaque étape, tiré des constats | 0,5 |
| b-2 | Trois tests de contrôle documentaires (rapprochement paie / comptes, sondage sur les droits par métier, observation des unités et des traces), chacun relié à un constat | 0,5 |
| c-1 | Deux critères (par exemple sécurité et conformité au RGPD) : ce qui est attendu et appréciation de la situation à partir des chiffres de l'annexe 3.1 | 0,5 |
| c-2 | Deux autres critères (par exemple fiabilité et efficacité) : ce qui est attendu et appréciation de la situation | 0,5 |

**Réponse attendue**

*3.1 a) – L'audit et sa démarche*

L'**audit du système d'information** est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel (ici le RGPD, le guide de la sécurité des données personnelles et le guide d'hygiène de l'ANSSI, éventuellement les mesures de contrôle d'accès de l'annexe A de l'ISO/IEC 27001:2022), la gouvernance, la performance, la sécurité et la conformité d'un système ou d'un processus, et qui débouche sur des constats et des recommandations hiérarchisées (F10 § 1). Le **contrôle interne** est l'ensemble des dispositifs permanents mis en œuvre par les responsables opérationnels pour maîtriser leurs activités (demande d'ouverture d'un compte, validation, revue des droits) ; l'audit **évalue** ce dispositif, de façon ponctuelle et indépendante, sans s'y substituer. À la Fondation, il n'existe guère de contrôle interne des habilitations : l'audit doit d'abord le constater, puis dire ce qu'il devrait être avant l'ouverture du dossier unique.

| Élément | Contenu pour la Fondation VERLANDRE |
|---|---|
| Mandant et destinataire | le conseil d'administration, par la directrice générale ; conclusions présentées au conseil de septembre 2027 |
| Objectifs | savoir « qui voit quoi, et pourquoi » ; apprécier la conception et l'effectivité des contrôles sur l'attribution, la modification et le retrait des droits ; mesurer les écarts (comptes partagés, comptes de salariés partis, droits excessifs) ; fixer les règles et les profils qui seront appliqués dans le dossier unique au lieu de « reprendre les droits actuels » |
| Périmètre | les trois logiciels de dossier (1 600 comptes actifs, 32 établissements et services), y compris les 70 comptes d'unité et les 20 comptes d'éditeur ou d'administration ; le processus « arrivée, mobilité, départ » (DRH, directeurs d'établissement, DSI) ; les remplaçants et intérimaires ; la conception des profils et des droits des familles du dossier unique ; hors périmètre : les huit établissements à dossiers papier (sauf leur entrée dans le dossier unique), les autres applications |
| Équipe et indépendance | vous-même, avec la déléguée à la protection des données (conformité) ; l'administrateur de la DSI fournit les extractions mais ne conduit pas l'appréciation, la DSI étant partie au processus audité |
| Étapes | début juin : cadrage (lettre de mission signée par la directrice générale, référentiel retenu, calendrier) ; juin : prise de connaissance (entretiens avec la DRH, la DSI, quatre directeurs d'établissement, des cadres de nuit ; registre des traitements) et cartographie des risques du processus ; fin juin à mi-juillet : tests de contrôle (b) ; fin juillet : constats partagés de façon contradictoire avec les audités ; août : rapport ; septembre : présentation au conseil ; puis suivi du plan d'action avant la mise en service |
| Livrables | lettre de mission ; cartographie du processus et de ses risques ; programme de travail ; fiches de constats (constat, cause, risque, recommandation, priorité, responsable, échéance) ; rapport et présentation au conseil ; matrice des profils par métier proposée pour le dossier unique ; plan d'action |

*3.1 b) – Le processus « arrivée, mobilité, départ », les contrôles attendus et les tests*

| Étape | Acteur aujourd'hui | Fonctionnement constaté | Risque | Contrôle interne attendu |
|---|---|---|---|---|
| **Arrivée** (300 arrivées par an, 150 remplaçants et intérimaires par mois) | directeur d'établissement, par courriel à la DSI ; cadre de l'unité pour les remplaçants | aucun formulaire ; 10 jours en moyenne ; en attendant, mot de passe d'un titulaire ou compte de l'unité | actions non imputables, accès sans autorisation formelle, contournement durable du dispositif | demande formalisée déclenchée par l'embauche (paie), validée par le directeur d'établissement, profil choisi dans une liste par métier ; compte nominatif ouvert en moins de 24 heures, y compris pour un remplacement court (compte temporaire nominatif avec date de fin) |
| **Mobilité** (100 par an) | directeur du nouvel établissement | nouveau compte ouvert, ancien conservé : 60 salariés accèdent à deux établissements ou plus | cumul de droits, accès à des dossiers sans besoin | changement d'affectation dans la paie qui déclenche la modification des droits, retrait des anciens droits à la date de la mobilité |
| **Départ** (250 par an) | DRH (paie), sans transmission ; fermeture à la demande du directeur | 160 comptes de salariés partis (10 % des comptes), dont 30 utilisés après le départ | accès d'anciens salariés, usage du compte par des collègues, violation de données | information automatique ou hebdomadaire de la DSI par la DRH ; fermeture le jour du départ ; contrôle mensuel de rapprochement ; revue semestrielle des droits par chaque directeur d'établissement, tracée |

Trois **tests de contrôle**, documentaires et sans intervention technique sur les systèmes (b-2) :
1. **Rapprochement exhaustif** des comptes des trois logiciels avec la liste des salariés présents et sortis de la paie, puis des dates de dernière connexion avec les dates de départ (constat : 160 comptes de salariés partis, dont 30 utilisés après le départ).
2. **Sondage** sur un échantillon de comptes par métier (agents de cuisine, éducateurs, soignants, secrétariats) : comparaison des dossiers et des rubriques accessibles avec le besoin du métier (constat : droits par établissement, cuisine et entretien qui voient tout le dossier).
3. **Observation** dans des unités de jour et de nuit et revue des traces : usage des comptes d'unité, mots de passe affichés, remise d'identifiants aux remplaçants ; examen du journal des consultations du logiciel de l'ancienne association GERVELLE et des comptes d'éditeur (constat : mot de passe affiché dans 10 unités sur 20, comptes d'éditeur inchangés, traces absentes dans deux logiciels).

*3.1 c) – Quatre critères de performance et de conformité*

| Critère | Ce qui est attendu | Appréciation de la situation (annexe 3.1) |
|---|---|---|
| **Sécurité** (confidentialité et traçabilité) (c-1) | comptes nominatifs, moindre privilège, comptes d'éditeur maîtrisés, consultations tracées | insuffisante : 70 comptes partagés, mots de passe affichés dans la moitié des unités visitées, accès permanent des éditeurs avec des mots de passe jamais changés, consultations tracées dans un seul logiciel, plainte d'une famille impossible à instruire |
| **Conformité au RGPD** (c-1) | accès limité aux personnes autorisées selon leur besoin, protection renforcée des données de santé, registre précisant les destinataires, capacité à démontrer la conformité | non démontrée : droits par établissement et non par métier (cuisine et entretien qui lisent les comptes rendus des médecins et des psychologues), registre de 2020 muet sur les accès par métier, aucune revue des droits depuis 2017 ou 2018, jamais dans un logiciel |
| **Fiabilité** (c-2) | la liste des comptes reflète la réalité des salariés et des affectations ; chaque action est imputable à une personne | faible : 10 % des comptes appartiennent à des salariés partis ; 60 salariés gardent d'anciens accès ; les écrits saisis sous le compte d'un titulaire ou de l'unité ne sont pas attribuables à leur auteur |
| **Efficacité** (c-2) | le processus donne le bon accès au bon moment, notamment la nuit, sans contournement | faible : 10 jours pour ouvrir un compte, ce qui pousse au partage des mots de passe (témoignage de Mme QUILLEVÈRE) ; aucune information de la DSI par la paie ; aucun responsable du processus |

**Réponses tolérées**
- Démarche en cinq à sept étapes (cadrage, prise de connaissance, analyse des risques, programme, collecte, restitution, suivi) si les objectifs, le périmètre, les livrables et le calendrier sont présents ; échéancier présenté en diagramme de Gantt.
- Référence au COSO 2013 pour définir le contrôle interne, ou à l'annexe A de l'ISO/IEC 27001:2022 comme référentiel de l'audit, sans viser autre chose qu'un cadre d'appréciation.
- Autres critères pertinents : efficience (coût du processus, charge de la DSI), continuité d'accès la nuit, gouvernance (existence d'un responsable du processus et d'une validation par le métier).
- Autres tests documentaires : revue des demandes d'ouverture de l'année, vérification de la fermeture des comptes d'un échantillon de salariés sortis.

**Erreurs fréquentes**
- *Audit confondu avec l'audit légal des comptes ou avec le contrôle interne* (`ET-34`, F10 § 7) — juste : un audit interne du SI, mandaté par le conseil, qui évalue le dispositif de contrôle.
- *Méthodologie incomplète* (`JUR-A01`) — juste : objectifs, périmètre, étapes, livrables et échéancier tenant dans juin-septembre 2027.
- *Tests techniques proposés comme diligences de l'audit* (limite du programme 3.2) — juste : rapprochements, sondages, observations, entretiens.
- *Critères récités sans appréciation chiffrée* (`JUR-T01`, `JUR-T08`) — juste : chaque critère est confronté aux 160 comptes de salariés partis, aux 70 comptes partagés, aux 10 jours d'ouverture.
- *Glissement vers la note de synthèse ou les facteurs de succès de l'audit* (périmètre de la question) — juste : démarche, processus, contrôles, tests, critères.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI, contrôle interne, démarche et livrables | définitions, étapes, fiches de constats | F10 § 1 et 2 | notion de cours |
| Guide de la sécurité des données personnelles (autorité de contrôle), édition 2024 | habilitations par métier, retrait des droits, revue, traçabilité | `cnil_guide_securite_2024` ; F15 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | identification nominative, arrivées et départs | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| ISO/IEC 27001:2022, annexe A | contrôle d'accès comme référentiel d'appréciation | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | sécurité adaptée au risque, données de santé, registre | `rgpd` ; F15 | applicable depuis le 25/05/2018 |
| COSO 2013 | définition du contrôle interne (toléré) | `coso_2013` ; F10 § 2 | en vigueur |

---

### 3.2 – Les risques pesant sur les données des personnes accompagnées (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; les méthodes d'analyse de risques sont citées comme démarches, sans les ateliers détaillés.

**Annexes mobilisées** : annexe 3.1 (habilitations), annexe 3.2 (attaque de l'association TERNAVIELLE, situation de la Fondation), annexe 3.4 (RGPD, ISO/IEC 27005:2022, EBIOS Risk Manager, ISO/IEC 27001:2022, LOPMI) et annexe 1.1 (établissements ouverts jour et nuit).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers, définies en une phrase chacune | 0,5 |
| a-2 | Deux premiers risques tirés des annexes 3.1 et 3.2, chacun rattaché à sa catégorie, avec ses conséquences pour les personnes et pour la Fondation | 0,5 |
| a-3 | Deux autres risques, les trois catégories étant couvertes, avec leurs conséquences | 0,5 |
| b-1 | Référentiel choisi dans l'annexe 3.4 et sa nature (ISO/IEC 27005:2022 : lignes directrices ; EBIOS Risk Manager : méthode ; ISO/IEC 27001:2022 : norme d'exigences), distinguée d'une solution | 0,5 |
| b-2 | Démarche appliquée aux quatre risques : contexte et biens essentiels, identification, évaluation de la vraisemblance et de la gravité sur une échelle qualitative, hiérarchisation | 0,5 |
| b-3 | Options de traitement (réduire, conserver, éviter, partager) appliquées à deux risques, dont le transfert partiel à l'assurance cyber, présenté comme complément et sous condition de plainte dans les 72 heures | 0,5 |

**Réponse attendue**

*3.2 a) – Typologie et quatre risques*

Les **cybermenaces** sont des actes malveillants qui visent le système d'information (rançongiciel, hameçonnage, usurpation de comptes) ; les **défaillances opérationnelles** sont des pannes, des erreurs ou des processus défaillants, sans intention de nuire ; les **risques réglementaires et métiers** sont les manquements à une obligation et les atteintes à la mission de l'organisation, à la qualité du service et à la confiance des parties prenantes (F12 § 0 et 5).

| Risque | Catégorie | Faits des annexes | Conséquences pour les personnes accompagnées | Conséquences pour la Fondation |
|---|---|---|---|---|
| **R1 – Rançongiciel qui rend les dossiers indisponibles et publie les données** (a-2) | cybermenace | sauvegardes reliées en permanence au réseau, dans la même salle ; restauration jamais essayée ; attaque de TERNAVIELLE (trois semaines sans dossiers, 2 000 dossiers publiés) | accompagnement de nuit sans consignes (régimes, allergies, traitements), diagnostics exposés publiquement | retour au papier pendant des semaines, ressaisies, coût de l'ordre de celui de TERNAVIELLE (600 k€), perte de confiance des familles et des financeurs |
| **R2 – Usurpation de comptes après un hameçonnage ou par des identifiants partagés** (a-2) | cybermenace | 25 salariés piégés en février 2027 ; authentification à deux facteurs limitée à la DSI ; 70 comptes d'unité, mots de passe affichés dans 10 unités sur 20 ; point d'entrée de l'attaque de TERNAVIELLE | lecture ou modification de leurs dossiers par un tiers | porte d'entrée d'un rançongiciel ; violation de données à notifier ; actions non imputables |
| **R3 – Accès d'anciens salariés et de remplaçants sans compte propre** (a-3) | défaillance opérationnelle (processus « arrivée, mobilité, départ » défaillant) | 160 comptes de salariés partis, dont 30 utilisés après le départ ; remplaçants sur le compte d'un titulaire ; 10 jours pour ouvrir un compte | confidentialité de leur vie et de leur santé atteinte (plainte de janvier 2027) | écrits non attribuables à leur auteur, impossibilité d'instruire une plainte, faute de traces |
| **R4 – Accès aux données au-delà du besoin des métiers et des familles** (a-3) | risque réglementaire et métier | droits par établissement ; cuisine et entretien qui lisent les comptes rendus des médecins et des psychologues ; registre muet ; droits des familles non définis ; projet de « reprendre les droits actuels » dans le dossier unique | atteinte à l'intimité, information d'un proche contre le souhait d'un adulte accompagné | manquement à la sécurité adaptée au risque exigée par le RGPD pour des données de santé ; perte de confiance ; transposition des défauts actuels dans le dossier unique |

Autre risque recevable : **panne de la salle de serveurs** (défaillance opérationnelle : 6 heures sans dossiers un samedi soir de novembre 2026, aucune permanence de la DSI la nuit), ou **risque de dépendance aux éditeurs** (accès permanents à distance, mots de passe inchangés : attaque par un prestataire).

*3.2 b) – Apprécier et traiter les risques selon un référentiel*

On retient par exemple l'**ISO/IEC 27005:2022**, qui fournit des **lignes directrices** (non certifiables) de gestion des risques liés à la sécurité de l'information ; l'**EBIOS Risk Manager** (ANSSI, version 1.5) est une **méthode** d'appréciation compatible avec elle, et l'**ISO/IEC 27001:2022** une **norme d'exigences** dont le système de management repose sur cette appréciation. Aucun de ces référentiels n'est une solution logicielle (b-1).

La démarche (b-2) :
1. **Établir le contexte** : biens essentiels (dossiers des personnes accompagnées, consignes d'accompagnement de nuit, données de santé), biens supports (trois logiciels, salle de serveurs, comptes, postes partagés), parties prenantes (éditeurs, prestataires, remplaçants, familles), critères d'évaluation et d'acceptation fixés par la direction générale. EBIOS Risk Manager y ajoute l'examen des sources de risque (cybercriminels qui visent un secteur peu protégé, ancien salarié) et de l'écosystème (éditeurs avec accès permanent).
2. **Identifier** les scénarios : R1 à R4 formulés comme des événements (« un rançongiciel entré par un compte hameçonné chiffre les serveurs et leurs sauvegardes un samedi »).
3. **Analyser et évaluer** chaque risque par sa **vraisemblance** et sa **gravité** sur une échelle qualitative à quatre niveaux, avec les métiers : R1, vraisemblable (TERNAVIELLE, 25 salariés hameçonnés) et de gravité maximale (sécurité des personnes la nuit, publication de données de santé), vient en tête ; R2, très vraisemblable, est sa cause principale ; R3 et R4, avérés, sont graves pour la confidentialité.
4. **Traiter** : pour chaque risque, choisir une option, une mesure, un responsable et une échéance ; accepter formellement le risque résiduel ; surveiller et revoir les risques chaque année et à chaque changement majeur (l'ouverture du dossier unique en est un).

Options appliquées (b-3) :
- **R1** : **réduire** (sauvegardes déconnectées et restauration essayée, authentification à deux facteurs, procédure de crise : question 3.3) **et partager** une partie de l'impact financier par l'**assurance cyber** en négociation (plafond de 2 000 k€, franchise de 50 k€). Le transfert ne couvre ni la sécurité des personnes ni la confiance des familles ; il ne remplace pas les mesures, que l'assureur exige d'ailleurs avant de signer ; l'indemnisation suppose une plainte au plus tard 72 heures après la connaissance de l'atteinte (LOPMI, annexe 3.4) : c'est ce qui a manqué à TERNAVIELLE (plainte au sixième jour). Le dépôt de plainte devient une étape de la procédure de crise.
- **R4** : **réduire** par des profils de droits par métier et des droits des familles décidés pour chaque personne avant l'ouverture du dossier unique, et **éviter** la reprise telle quelle des droits actuels proposée par l'équipe projet.
- Exemple d'**acceptation** recevable : risque résiduel de quelques heures d'indisponibilité, accepté par la directrice générale si un mode de consultation de secours des consignes existe la nuit.

**Réponses tolérées**
- Choix de l'EBIOS Risk Manager ou de l'ISO/IEC 27001:2022 comme cadre, si sa nature est exacte et la démarche (contexte, identification, évaluation, traitement) appliquée.
- Matrice de vraisemblance et de gravité esquissée sans valeurs chiffrées ; autre hiérarchisation justifiée par les annexes.
- Rattachement de R3 aux risques réglementaires et métiers, de R4 aux défaillances opérationnelles, si la justification est donnée et les trois catégories couvertes.
- Risque lié à l'outil d'intelligence artificielle de l'annexe 3.3 (transmissions inexactes, enregistrements conservés par l'éditeur), en risque réglementaire et métier, s'il est appuyé sur l'annexe.

**Erreurs fréquentes**
- *Norme, méthode et solution confondues* (`ET-01`, `JUR-S06`) — « installer EBIOS » ; juste : lignes directrices, méthode, norme d'exigences.
- *Risques génériques sans faits des annexes* (`JUR-T08`) — juste : 160 comptes, 25 salariés hameçonnés, sauvegardes reliées au réseau.
- *Assurance présentée comme une mesure de sécurité suffisante* (F12 § 7) — juste : transfert partiel, conditionné aux mesures et à la plainte dans les 72 heures.
- *Détermination de l'assujettissement à NIS 2* (périmètre, annexe 3.4) — juste : la situation est donnée.
- *Glissement vers une cotation chiffrée ou les ateliers détaillés* (limite de la question) — juste : une démarche en principe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 27005:2022 | lignes directrices de gestion des risques, options de traitement | `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI) | méthode d'appréciation, sources de risque, écosystème | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| ISO/IEC 27001:2022 | norme d'exigences fondée sur l'appréciation des risques | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Loi n° 2023-22 (LOPMI), C. assur. art. L. 12-10-1 | indemnisation subordonnée à la plainte dans les 72 heures | `lopmi_cyberassurance` ; F12 § 7 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | sécurité adaptée au risque, données de santé, notification | `rgpd` ; F15 § 6 | applicable depuis le 25/05/2018 ; proposition « omnibus numérique » non applicable (`omnibus_numerique_donnees`) |
| Directive (UE) 2022/2555 (NIS 2) | situation de la Fondation donnée, non à discuter | `nis2`, `nis2_transposition_fr` ; F12 § 6 | délai expiré le 17/10/2024 ; loi française non promulguée au 31/12/2026 |

---

### 3.3 – La politique de cybersécurité et la gestion d'une crise cyber (3,5 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) » (ici, la gestion des identités et des accès, sans plans de continuité et de reprise détaillés). Limites : la mise en œuvre technique n'est pas exigée ; la sécurité est envisagée de façon systémique (organisationnelle, humaine, juridique).

**Annexes mobilisées** : annexe 3.2 (TERNAVIELLE, situation de la Fondation, témoignages), annexe 3.4 (NIS 2 comme source d'inspiration, RGPD, guide d'hygiène de l'ANSSI, LOPMI) et annexe 1.1 (organigramme, pôles, établissements ouverts jour et nuit).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Politique de sécurité du SI définie (document approuvé par la direction : objectifs, périmètre, principes, organisation, règles, contrôle ; déclinée en charte) ; objectifs : confidentialité, intégrité, disponibilité, traçabilité, appliqués aux dossiers | 0,5 |
| a-2 | Deux principes, chacun relié à un risque de 3.2 et décliné en une mesure prioritaire | 0,5 |
| a-3 | Deux autres principes, reliés et déclinés de la même façon | 0,5 |
| b-1 | Déclenchement (qui alerte, qui décide, critères) et composition de la cellule de crise | 0,5 |
| b-2 | Rôles du conseil d'administration, de la directrice générale, de la DSI, de la déléguée à la protection des données, de l'assureur et des prestataires (dont la plainte dans les 72 heures et la notification) | 0,5 |
| b-3 | Prise en compte des établissements ouverts jour et nuit : astreinte de direction étendue au numérique, rôle des directeurs d'établissement, consignes de secours, contacts joignables | 0,5 |
| b-4 | Communication auprès des professionnels, des familles et des personnes accompagnées (messages préparés, porte-parole, adaptation aux personnes), exercice annuel et retour d'expérience | 0,5 |

**Réponse attendue**

*3.3 a) – Définition et quatre principes*

La **politique de sécurité du système d'information** est le document de référence, approuvé par la direction, qui fixe les objectifs, le périmètre, les principes, l'organisation, les règles et le dispositif de contrôle de la sécurité ; elle se décline en une charte opposable aux utilisateurs et en procédures (F12 § 1). Ses objectifs sont la **confidentialité** (seules les personnes autorisées lisent un dossier), l'**intégrité** (les consignes et les transmissions sont exactes et non altérées), la **disponibilité** (les dossiers sont consultables à toute heure, y compris la nuit) et la **traçabilité** (chaque consultation et chaque écrit sont imputables à une personne). Elle découle de l'analyse de la question 3.2 : les risques prioritaires orientent les principes et les mesures.

| Principe | Risque traité (3.2) | Mesure prioritaire |
|---|---|---|
| **1. Une identité par personne, des droits selon le besoin du métier** (a-2) | R3, R4, R2 | suppression des comptes d'unité et des remises de mots de passe ; profils par métier dans le dossier unique ; compte temporaire nominatif ouvert en 24 heures pour les remplaçants ; fermeture le jour du départ ; revue semestrielle |
| **2. Une authentification renforcée et des utilisateurs formés** (a-2) | R2, R1 | authentification à deux facteurs pour tous les accès au dossier unique et à la messagerie, à commencer par les accès à distance (exigée par l'assureur) ; sensibilisation à l'hameçonnage de tous les salariés, y compris de nuit, sur leur temps de travail |
| **3. Des données que l'on sait restaurer** (a-3) | R1 | sauvegardes déconnectées du réseau et conservées hors de la salle du siège ; restauration complète essayée au moins une fois par an ; consignes essentielles de nuit consultables en mode de secours |
| **4. Une sécurité gouvernée par la direction et partagée avec les prestataires** (a-3) | R1, R4, risque lié aux éditeurs | politique approuvée par la directrice générale et présentée au conseil d'administration, à l'image de la responsabilité des organes de direction de NIS 2 ; un responsable de la sécurité du SI désigné, rattaché à la directrice générale et distinct des administrateurs qui exploitent les systèmes ; charte commune ; accès des éditeurs encadrés (comptes nominatifs, activés à la demande, tracés) ; procédure de crise (b) |

*3.3 b) – L'organisation de la gestion d'une crise cyber*

**Déclenchement** (b-1) : toute personne qui constate une anomalie (message de rançon, dossiers illisibles, comportement suspect d'un compte) appelle un **numéro unique** affiché dans chaque unité, qui aboutit la nuit et le week-end au **directeur d'établissement d'astreinte de son pôle** ; celui-ci qualifie la situation avec une fiche réflexe et alerte le **cadre d'astreinte de la DSI** (astreinte à créer, par roulement entre les trois administrateurs et le DSI) ; la **directrice générale** décide l'activation de la cellule de crise, au plus tard dans les deux heures, selon des critères écrits (plusieurs établissements touchés, données menacées, indisponibilité au-delà de quelques heures).

**Composition et rôles** (b-1, b-2) :

| Acteur | Rôle dans la crise |
|---|---|
| Conseil d'administration (président) | informé dès l'activation ; approuve en amont la politique et la procédure de crise ; arbitre avec la directrice générale les décisions majeures (réponse à une demande de rançon, communication publique) |
| Directrice générale | dirige la cellule ; décide (isolement des systèmes, mode dégradé, demande de rançon refusée par principe, communication) ; porte-parole auprès des financeurs et de la presse ; ordonne le dépôt de plainte dans les 72 heures |
| Direction des systèmes d'information (DSI et administrateurs) | qualifie l'incident, isole les systèmes touchés, préserve les traces, conduit la restauration avec les éditeurs et le prestataire spécialisé ; tient le journal technique de la crise |
| Directeurs de pôle et d'établissement d'astreinte | relais de terrain : déclenchent les consignes de secours dans les unités, s'assurent que chaque unité de nuit a ses consignes, remontent les besoins, organisent le retour au papier |
| Déléguée à la protection des données | apprécie la violation de données, prépare la notification à l'autorité de contrôle dans les 72 heures et l'information des personnes en cas de risque élevé ; tient le registre des violations |
| Responsable de la sécurité du SI (à désigner) | coordonne la réponse et le lien avec les prestataires ; prépare le retour d'expérience |
| Directeur administratif et financier | déclare le sinistre à l'assureur, suit les frais engagés, garde les justificatifs |
| Assureur | met à disposition, selon le contrat, l'assistance à la réponse à l'incident et la gestion de crise ; indemnise sous condition de plainte dans les 72 heures |
| Éditeurs et prestataires | interviennent selon des engagements de joignabilité prévus à l'avance, y compris le week-end ; prestataire spécialisé dans la réponse aux incidents appelé par la DSI ou par l'assureur |
| Responsable de la communication (ou directrice générale) | prépare et diffuse les messages internes et externes validés par la cellule |

**Établissements ouverts jour et nuit** (b-3) : la procédure d'astreinte de direction existante est **étendue** aux incidents informatiques, ce qui évite de créer une organisation parallèle ; chaque unité de nuit dispose d'une **fiche de consignes essentielles** de chaque résident (régimes, allergies, traitements, conduites à tenir) imprimée et mise à jour chaque semaine, ou d'une consultation de secours ; la **liste des contacts** (astreintes, éditeurs, prestataires, assureur, autorités) est tenue à jour et disponible hors du système d'information ; la réponse de M. BOURDAILLE (« savoir où trouver les consignes et qui appeler ») est le critère de réussite. Le contenu détaillé des plans de continuité et de reprise n'est pas développé ici : la procédure de crise s'y articule.

**Communication** (b-4) : messages préparés à l'avance pour les **professionnels** (consignes, ce qu'il ne faut pas faire : ne pas éteindre ni rallumer les postes, ne pas utiliser de messagerie personnelle), pour les **familles** (information par la Fondation avant la presse, par courrier, téléphone et réunion, comme le demande Mme LANGEVELLE, avec un numéro dédié) et pour les **personnes accompagnées** (explication adaptée par les équipes, en phrases courtes et illustrées) ; un seul porte-parole ; information des financeurs. **Exercice** de crise annuel sur le scénario de TERNAVIELLE (un samedi soir), associant une astreinte de pôle et une unité de nuit, suivi d'un retour d'expérience et de la mise à jour de la procédure.

**Réponses tolérées**
- Principes formulés autrement (moindre privilège, défense en profondeur, sécurité dès la conception du dossier unique, amélioration continue de type PDCA) s'ils sont reliés aux risques et déclinés en mesures.
- Responsable de la sécurité mutualisé ou externalisé à temps partiel, s'il reste distinct de l'exploitation et rattaché à la direction.
- Rôle d'un comité de sécurité réunissant la directrice générale, la DSI, la déléguée et un directeur de pôle, en amont de la crise.
- Refus de la demande de rançon présenté comme une décision de principe de la direction, sans analyse juridique.

**Erreurs fréquentes**
- *Politique de sécurité confondue avec la charte informatique* (`ET-27`) — juste : la charte décline la politique auprès des utilisateurs.
- *Triade CID récitée sans application* (`JUR-S01`, `JUR-T01`) — juste : disponibilité des consignes de nuit, confidentialité des données de santé.
- *Responsable de la sécurité confondu avec un technicien ou subordonné aux administrateurs* (`ET-15`) ; *déléguée à la protection des données présentée comme responsable de la sécurité* (`ET-29`).
- *PCA et PRA confondus ou développés à la place de l'organisation de crise* (`ET-02`, périmètre de la question) — juste : cellule, rôles, astreinte, communication.
- *Mesures techniques ou paramétrages* (limite du programme 4.2) — juste : principes et organisation.
- *Oubli de la nuit et du week-end* (`JUR-T08`) — juste : l'astreinte de pôle existante sert de relais.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Politique de sécurité, CID et traçabilité, acteurs, gestion d'incident | définitions, cellule de crise | F12 § 1 et 5 | notion de cours |
| Directive (UE) 2022/2555 (NIS 2) | responsabilité des organes de direction, gestion des incidents et des crises, comme source d'inspiration | `nis2`, `nis2_transposition_fr` ; F12 § 6 | délai expiré le 17/10/2024 ; loi française non promulguée au 31/12/2026 |
| Guide d'hygiène informatique de l'ANSSI (2017) | sensibilisation, sauvegarde, identification | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Règlement (UE) 2016/679 (RGPD) | notification en 72 heures, information des personnes | `rgpd` ; F15 § 6 | applicable depuis le 25/05/2018 |
| Loi n° 2023-22 (LOPMI), C. assur. art. L. 12-10-1 | plainte dans les 72 heures | `lopmi_cyberassurance` ; F12 § 7 | en vigueur |

---

### 3.4 – Une stratégie de numérique responsable, accessible et éthique (3,5 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété » ; `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) » ; `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements » (prolongation, reconditionnement et recyclage des équipements, mutualisation des serveurs, pages légères). Limites : la durabilité est intégrée dans la gouvernance globale du SI, et non comme un ajout marginal ; approche transversale.

**Annexes mobilisées** : annexe 3.3 (portail et application, outil de rédaction automatique, salle de serveurs, équipements et atelier), annexe 3.4 (règlement sur l'intelligence artificielle, RGPD, loi REEN, RGESN, étude ADEME-Arcep) et annexe 1.1 (projet « Horizon 2030 », parc, établissements d'aide par le travail).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance du SI orientée RSE définie (inclusion, éthique, sobriété intégrées aux décisions du SI, avec des porteurs et des indicateurs) et reliée à l'orientation « numérique responsable, accessible et éthique » d'« Horizon 2030 » | 0,5 |
| a-2 | Trois mesures d'accessibilité et d'inclusion pour le portail et l'application, appuyées sur l'annexe 3.3 (conception avec les personnes, langage simple et pictogrammes, alternative humaine et non numérique) | 0,5 |
| a-3 | Quatre règles éthiques d'usage de l'outil d'IA générative (validation humaine, transparence, données et confidentialité, finalité limitée), appuyées sur l'essai et les témoignages | 0,5 |
| b-1 | Trois conditions d'une transition responsable vers les services en ligne (sobriété avant migration, critères environnementaux et de localisation du fournisseur, fin de vie de la salle), sans comparaison d'options | 0,5 |
| b-2 | Place de l'atelier dans le réemploi (prolongation, reconditionnement, don ou recyclage tracé) et deux conditions de réussite (effacement certifié des données, organisation et valorisation du travail) | 0,5 |
| c-1 | Indicateur d'accessibilité complet (formule, source, fréquence, cible, axe), cible tirée des essais d'avril 2027 | 0,5 |
| c-2 | Indicateur de réemploi complet, cible tirée de l'annexe 3.3 D | 0,5 |

**Réponse attendue**

*3.4 a) – Gouvernance orientée RSE, accessibilité et éthique*

Une **gouvernance du système d'information orientée vers la responsabilité sociétale** intègre l'**inclusion** (personne n'est exclu par le numérique), l'**éthique** (usage des données et des algorithmes respectueux des personnes) et la **sobriété** (questionner le besoin avant d'équiper) dans les décisions du SI : critères dans les choix de projets et d'achats, porteurs nommés, indicateurs suivis par la direction (F14 § 0). À la Fondation, elle traduit l'orientation « numérique responsable, accessible et éthique » d'« Horizon 2030 » : un **comité du numérique responsable**, présidé par la directrice générale et associant la déléguée à la protection des données, la DSI, un directeur de pôle, des représentants des familles et des personnes accompagnées, examine chaque projet (portail, outil d'IA, services en ligne, équipements) avant décision.

Trois **mesures d'accessibilité et d'inclusion** (a-2) :
1. **Concevoir avec les personnes concernées** : exigences d'accessibilité inscrites dans le cahier des charges, essais d'usage avec des personnes accompagnées (troubles de la vue, de la motricité fine, de la compréhension) et des familles avant chaque version, puisque seules 6 personnes sur 20 et 12 familles sur 20 ont trouvé seules le prochain rendez-vous en avril 2027.
2. **Simplifier les contenus et les interactions** : reprendre dans le portail et l'application la pratique des établissements (phrases courtes, pictogrammes), proposer la lecture à voix haute des textes, de grands boutons et peu d'étapes, des pages légères utilisables sur des équipements anciens (RGESN).
3. **Garder une alternative humaine et non numérique** : pour les 30 % de familles qui n'utilisent pas internet ou ont besoin d'aide, maintien du courrier et du téléphone, accompagnement par les équipes des établissements, documents imprimés à la demande ; aucune démarche réservée au numérique.

Quatre **règles éthiques d'usage** de l'outil de SCRIBALEN, qui relève de l'**intelligence artificielle générative** (il produit un texte à partir d'une dictée et peut inventer : 20 transmissions inexactes sur 200, soit 10 %) (a-3) :
1. **Le professionnel reste l'auteur** : chaque transmission rédigée par l'outil est relue, corrigée et validée par le professionnel avant d'entrer dans le dossier ; aucun texte non validé n'est enregistré ; l'outil aide ceux qui sont peu à l'aise avec l'écrit (M. BOURDAILLE) sans remplacer le regard professionnel (l'éducatrice).
2. **Transparence** : les textes produits par l'outil sont signalés comme tels dans le dossier, et les personnes accompagnées et les familles sont informées de son usage. C'est un choix éthique de la Fondation, dans l'esprit des obligations de transparence de l'annexe 3.4, qui visent directement les professionnels qui utilisent l'outil et le marquage des contenus générés ; il répond à Mme LANGEVELLE.
3. **Protection des données et de l'intimité** : pas de conservation des enregistrements par l'éditeur au-delà de la transcription, ni de réutilisation pour « améliorer le service » ; dictée hors de la présence de la personne et des tiers ; analyse d'impact relative à la protection des données, avec l'avis de la déléguée, avant toute généralisation.
4. **Finalité limitée** : l'outil sert à rédiger les transmissions, non à **évaluer les professionnels** (fonction de signalement des écrits « incomplets » désactivée) ni à produire des synthèses du comportement des personnes sans regard professionnel ; essai prolongé et mesuré (taux d'inexactitudes, temps réellement gagné) avant décision, sous le contrôle du comité.

*3.4 b) – Transition vers les services en ligne et réemploi*

Trois **conditions** d'une transition responsable (b-1) :
1. **Sobriété avant migration** : trier les 8 To de fichiers partagés, dont la moitié n'a pas été ouverte depuis trois ans, et supprimer ce qui doit l'être, plutôt que de déplacer et de payer un stockage inutile ; ne migrer que les applications nécessaires.
2. **Critères environnementaux et de localisation du fournisseur** : centres de données situés dans l'Union européenne, informations sur leur efficacité énergétique et l'origine de leur électricité, engagements mesurés ; le fournisseur pressenti, qui ne communique ni sa localisation ni ses consommations, ne remplit pas ces critères en l'état. Le passage aux services en ligne mutualise les serveurs (10 des 25 serveurs sont utilisés à moins de 10 %) mais déplace l'empreinte chez le fournisseur : il n'est pas sobre par nature.
3. **Fin de vie organisée de la salle** : réemploi ou recyclage tracé des serveurs et de la climatisation, effacement certifié des données ; la sécurité suit la transition (sauvegardes hors du fournisseur, responsabilités partagées écrites).

**Place de l'atelier de conditionnement** (b-2) : conformément à la loi REEN (allongement de la durée de vie et réemploi) et à l'étude ADEME-Arcep (fabrication des terminaux, premier poste de l'empreinte), la priorité est de **fabriquer moins** : prolonger les 150 ordinateurs qui peuvent servir deux ans de plus (environ 15 k€ de mémoire et de disques), puis confier à l'atelier le tri, le nettoyage, le reconditionnement et la réaffectation des équipements retirés (dont les 300 ordinateurs et 150 smartphones stockés), le don à des familles ou à des associations, et la remise des équipements irréparables à une filière de recyclage. Conditions de réussite : (1) **aucune donnée ne sort** : effacement certifié de chaque support par la DSI, ou destruction, avant remise à l'atelier, avec un registre des sorties, ce qui répond à la réserve de M. TRÉVENEC ; (2) **une activité organisée et valorisée** : convention interne entre la DSI et le pôle Travail (volumes, délais, contrôle qualité), formation des travailleurs, place dans une politique des équipements de la Fondation (achats centralisés, durée d'usage cible, reconditionné d'abord).

*3.4 c) – Deux indicateurs*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Part des participants qui réalisent sans aide les tâches clés du portail et de l'application (c-1) | nombre de participants aux essais d'usage qui réalisent sans aide les trois tâches clés (trouver le prochain rendez-vous, lire le planning de la semaine, envoyer un message à l'équipe) / nombre de participants aux essais d'usage × 100, calculé séparément pour les personnes accompagnées et pour les familles | grilles d'observation des essais d'usage conduits par la DSI et les équipes des établissements avec un panel de personnes accompagnées et de familles, renouvelé à chaque essai | à chaque nouvelle version du portail ou de l'application, et au moins deux fois par an | au moins 70 % des personnes accompagnées et 90 % des familles avant l'ouverture du portail, contre 30 % (6 sur 20) et 60 % (12 sur 20) en avril 2027 | social |
| Taux de réemploi des équipements retirés du parc (c-2) | nombre d'ordinateurs, de tablettes et de smartphones retirés du parc dans l'année puis réemployés (reconditionnés par l'atelier et réaffectés ou donnés) / nombre d'équipements retirés du parc dans l'année × 100 | inventaire du parc tenu par la DSI ; bons de sortie et certificats d'effacement des données établis par l'atelier de conditionnement | trimestrielle, avec un bilan annuel présenté au comité de direction | au moins 60 % en 2028, contre 0 % en 2026, avec 100 % des supports de données effacés ou détruits et certifiés | environnement |

**Réponses tolérées**
- Autres mesures d'accessibilité appuyées sur l'annexe (application utilisable par commande vocale, aide d'un proche avec des droits définis, formation des familles), sans citer de règles d'accessibilité absentes des fiches.
- Mention d'un référentiel d'accessibilité (RGAA) comme cadre, sans détail de ses critères.
- Règles éthiques formulées autrement (contrôle humain, explicabilité, non-discrimination, sobriété des usages de l'IA), si elles répondent à l'essai et aux témoignages ; décision de ne pas retenir l'outil après un essai mesuré.
- Charte du numérique responsable comme support des règles, si elle a un porteur.
- Indicateurs complets différents : durée d'usage moyenne des ordinateurs retirés (cible 6 ans contre 4 ans), part des transmissions produites par l'outil corrigées avant validation, part des familles utilisant le portail, volume de fichiers partagés stockés.

**Erreurs fréquentes**
- *Sobriété confondue avec l'économie d'énergie* (`ET-12`) ; *empreinte réduite à l'électricité* (`ET-38`) — juste : prolonger et réemployer les équipements d'abord.
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) ; *gouvernance de l'IA purement technique* (`ET-19`) — juste : règles d'usage, transparence, finalité, contrôle humain.
- *Fonctionnement interne des modèles ou calcul d'empreinte* (limites de la question) — juste : règles d'usage et conditions de la transition.
- *Durabilité en ajout marginal* (`JUR-T11`) — juste : comité, critères dans les décisions, indicateurs suivis.
- *Indicateurs sans cible ni source* (`ET-18`, `JUR-A02`) — juste : cinq champs, cibles à partir de 30 %, 60 % et 0 %.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gouvernance orientée RSE, sobriété, Green IT | définitions, comité, indicateurs | F14 § 0, 3 et 5 | notion de cours |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 | obligations de transparence | `ai_act`, `omnibus_numerique_ia` ; F13 § 5 | obligations de transparence applicables depuis le 02/08/2026 |
| IA générative et apprentissage automatique | distinction, risque d'inexactitude, charte d'usage | F13 § 1 et 4 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | analyse d'impact, minimisation | `rgpd` ; F15 § 3 | applicable depuis le 25/05/2018 |
| Loi n° 2021-1485 (REEN) | durée de vie, réemploi, centres de données | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | écoconception, usage sur équipements anciens | `rgesn_2024` ; F14 § 2 | en vigueur |
| Étude ADEME-Arcep sur l'empreinte du numérique | poids des terminaux et de leur fabrication | `etude_ademe_arcep_numerique` ; F14 § 1 | volets de 2022 et de 2023 ; mise à jour du 17/01/2025 |
