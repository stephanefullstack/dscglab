# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 27 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F12 sécurité et résilience, F13 intelligence artificielle, F10 audit et fiabilisation, F09 performance du SI, F14 numérique responsable, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Analyse d'impact de la campagne de vendanges | `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers (ici, les processus et la continuité) | 2 |
| 3.2 Le dispositif de continuité et de reprise de la campagne 2027 | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.d` Dispositifs de surveillance et de résilience : IAM, PCA/PRA ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 3 |
| 3.3 Le module de détection des apports anormaux | `4.1.f` Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques | 1,5 |
| 3.4 L'audit du module des apports | `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. | 2 |
| 3.5 Le tableau de bord du système d'information de la campagne | `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) | 1,5 |
| 3.6 Le choix d'un hébergement responsable | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 3 |
| **Dossier 3 – Assurer la continuité du système d'information pendant les vendanges, fiabiliser les apports et choisir un hébergement responsable** |  | **13** |

Répartition indicative : connaissances (analyse d'impact, durée et perte de données maximales admissibles, PCA et PRA, familles de l'IA, audit du système d'information, tableau de bord équilibré, sobriété numérique et stratégie responsable) 2,5 points environ (items 3.1-1, 3.2 a-1, 3.3-1 pour moitié, 3.4 a pour moitié, 3.5-1 pour moitié, 3.6 a-1) ; analyse des annexes et recommandations 10,5 points, soit environ 80 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Analyse d'impact de la campagne de vendanges (2 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ». L'énoncé exclut le volet des états financiers : seuls les processus et la continuité sont attendus. Limite : l'analyse de sécurité technique n'est pas attendue dans le détail.

**Annexes mobilisées** : annexe 3.1 (applications et volumes, incident, fiches des adhérents et des parcelles, acteurs) et annexe 1.1 (calendrier des vendanges, organisation en caves).

**Barème indicatif (2 pts)**

| Item | Attendu | Points |
|---|---|---|
| 1 | Analyse d'impact sur l'activité définie (processus critiques, conséquences d'une interruption selon sa durée, priorités de reprise) ; durée maximale d'interruption admissible (DMIA, ou RTO) et perte de données maximale admissible (PDMA, ou RPO) définies sans inversion | 0,5 |
| 2 | Réception et pesée : processus touchés, criticité maximale, DMIA très courte pour la réception (bascule en mode dégradé), PDMA nulle pour les pesées, justifiées par l'annexe 3.1 | 0,5 |
| 3 | Laboratoire et progiciel de l'union : processus, criticité, DMIA et PDMA justifiées (résultats attendus le lendemain à 8 h, échantillons conservés 48 heures ; commandes et pénalités, sauvegarde de nuit) | 0,5 |
| 4 | Variation de la criticité selon la période (caves et laboratoire en vendanges, progiciel en fin d'année) et conséquence pour le dispositif (calendrier des tests, des maintenances et des priorités de reprise) | 0,5 |

**Réponse attendue**

*Définitions (item 1)*

L'**analyse d'impact sur l'activité** (BIA) identifie les processus critiques d'une organisation et mesure, pour chacun, les conséquences d'une interruption selon sa durée (opérationnelles, financières, d'image, relationnelles) ; elle en déduit les ressources du système d'information dont ils dépendent, leur ordre de reprise et deux objectifs : la **durée maximale d'interruption admissible** (DMIA, en anglais RTO), délai au-delà duquel l'interruption devient inacceptable, et la **perte de données maximale admissible** (PDMA, en anglais RPO), quantité de données, exprimée en durée, que l'on accepte de perdre depuis la dernière copie exploitable (F12 § 4). Elle fonde le plan de continuité et le plan de reprise (question 3.2) et constitue la première étape d'un système de management de la continuité au sens d'ISO 22301:2019 (annexe 3.4). L'incident de GRAUSSELLE montre qu'elle n'a jamais été faite : la dernière copie exploitable avait 78 jours, et personne ne savait qui décidait.

*Trois applications pendant la campagne (items 2 et 3)*

| Application | Processus de l'union ou des caves touchés | Criticité en campagne | DMIA proposée | PDMA proposée |
|---|---|---|---|---|
| Logiciel de réception et de pesée (chaque cave) | réception des apports (pesée, degré, bon remis au viticulteur), affectation de la vendange aux cuves, suivi des cuves, relevés et rémunération des adhérents par leur cave, confiance des adhérents | **maximale** : jusqu'à 900 apports par jour pour les neuf caves, 120 pour la seule cave de CAUSSELAC ; une remorque ne peut attendre longtemps au soleil ; une vendange versée ne peut plus être pesée | pour le **processus** de réception : aucune interruption au-delà d'une heure environ, d'où une bascule en mode dégradé décidée dans les 30 minutes (l'attente habituelle est de 20 minutes, elle a atteint 3 heures) ; pour l'**application** : remise en service dans la journée, 24 heures au plus, car chaque heure en mode dégradé alourdit la ressaisie (385 bons ressaisis en deux jours, 25 erreurs) | **nulle** pour les pesées : aucune pesée ne peut être refaite ; chaque apport doit laisser une trace hors du serveur au moment même de la pesée (double du bon, copie continue des données) ; les fiches des adhérents et des parcelles tolèrent au plus une journée, et non les 78 jours écoulés depuis le 15 juin |
| Logiciel du laboratoire (union) | analyse des moûts, conduite des fermentations et des cuves par les œnologues | **forte** : environ 22 000 analyses, jusqu'à 1 000 par jour ; résultats attendus le lendemain à 8 h | environ **12 heures** : les analyses de la journée peuvent être reportées sur la nuit, pas au-delà du lendemain matin | environ **24 heures** : les échantillons, conservés 48 heures au froid, permettent de refaire les analyses perdues, à condition de conserver leur rattachement au bon d'apport |
| Progiciel de gestion de l'union | commandes, conditionnement, expéditions, facturation | **moyenne** en septembre et octobre (environ 40 commandes par jour), **forte** en novembre et décembre (environ 80 commandes par jour, pénalités de retard des enseignes) | **une journée ouvrée** pendant les vendanges : les commandes reçues peuvent être saisies le lendemain ; **quelques heures** en fin d'année | **24 heures** : la sauvegarde de nuit suffit, les commandes de la journée pouvant être reconstituées à partir des messages reçus ; mais la copie est conservée dans la même salle (annexe 3.3), ce qui fait de cette PDMA une promesse fragile |

*Variation de la criticité au cours de l'année (item 4)*

La criticité n'est pas une propriété fixe de l'application : elle dépend du calendrier des processus. Le logiciel de réception est vital de fin août à mi-octobre et presque secondaire le reste de l'année (suivi des cuves, relevés) ; le laboratoire suit le même rythme ; le progiciel de l'union est au contraire le plus critique en novembre et décembre, au pic des commandes de fin d'année. Conséquences : (1) les objectifs de reprise et les moyens de secours se fixent **par période** ; (2) les tests de restauration, l'exercice et les changements de version se placent **avant** la campagne (au printemps et en juillet), jamais pendant les vendanges, et la maintenance lourde du progiciel avant novembre ; (3) en cas de crise simultanée pendant les vendanges, la réception des caves passe avant le progiciel de l'union, alors que l'organisation actuelle (équipe informatique tournée vers le progiciel, caves sans informaticien) fait l'inverse. L'analyse est à revoir chaque année avec les directeurs de cave et la directrice de la production.

**Réponses tolérées**
- DMIA et PDMA différentes de celles du tableau, si elles sont justifiées par les données de l'annexe 3.1 (une DMIA de quelques heures pour l'application de réception, à condition que le mode dégradé couvre le processus).
- Échelle de criticité annoncée par le candidat (faible, moyenne, forte, vitale) ou cotation de 1 à 4.
- Messagerie ou suivi des cuves analysés en plus des trois applications demandées.
- Vocabulaire RTO et RPO employé à la place de DMIA et PDMA.

**Erreurs fréquentes**
- *RTO et RPO inversés ou confondus* (`ET-03`, `JUR-S02`) — « la PDMA est le délai de reprise » ; juste : la DMIA mesure une durée d'arrêt, la PDMA l'âge de la dernière copie exploitable.
- *Criticité unique pour toute l'année* (`JUR-T01`) — juste : la criticité suit le calendrier des vendanges et des ventes.
- *Analyse d'impact récitée sans les chiffres de l'annexe* (`JUR-T08`, `ET-39`) — juste : 900 apports par jour, 3 heures d'attente, 385 bons ressaisis, 48 heures de conservation des échantillons.
- *Dérive vers les états financiers ou la rémunération des adhérents* (périmètre de la question) — juste : processus et continuité seulement.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Analyse d'impact sur l'activité, DMIA (RTO), PDMA (RPO) | définitions et application | F12 § 4 | notion de cours |
| ISO 22301:2019 | système de management de la continuité d'activité, analyse d'impact | `iso_22301_2019` ; F12 § 4 | en vigueur |

---

### 3.2 – Le dispositif de continuité et de reprise de la campagne 2027 (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » (ici, le pilotage par la direction) ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique n'est pas exigée ; le lien avec les normes se fait sans entrer dans les certifications.

**Annexes mobilisées** : annexe 3.1 (incident, acteurs, pilotage), annexe 3.4 (ISO 22301, guide d'hygiène de l'ANSSI, EBIOS Risk Manager) et annexe 1.1 (organigramme, conseil de l'union, directeurs de cave).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | PCA (maintenir l'activité, au besoin en mode dégradé) et PRA (rétablir le système d'information et revenir à la normale) distingués et articulés, appuyés sur l'analyse d'impact | 0,5 |
| a-2 | Mode dégradé de la réception (documents numérotés en double, décision de bascule, affectation aux cuves, ressaisie contrôlée), relié à l'incident | 0,5 |
| a-3 | Règles de sauvegarde (fréquence en campagne, copie hors ligne et hors site) et tests de restauration avant la campagne, reliés à l'incident | 0,5 |
| a-4 | Exercice avant les vendanges : scénario, participants, date, mesures et retour d'expérience | 0,5 |
| b-1 | Rôles et responsabilités de l'union, des caves, du prestataire local et de l'éditeur, sans doublon ni vide (chaîne d'alerte, décision en crise) | 0,5 |
| b-2 | Pilotage par la direction : instance, décisions (validation du dispositif, décision avant la campagne, décisions de crise), compte rendu au conseil | 0,5 |

**Réponse attendue**

*3.2 a) – PCA, PRA et dispositif de la réception*

Le **plan de continuité d'activité** (PCA) organise le **maintien** des activités critiques pendant une crise, au besoin en **mode dégradé** : pendant que le serveur d'une cave est indisponible, la réception des apports continue. Le **plan de reprise d'activité** (PRA) organise le **rétablissement** du système d'information et le **retour à la normale** : restaurer le serveur à partir d'une sauvegarde saine, ressaisir et contrôler les données, revenir au fonctionnement courant. Les deux découlent de l'analyse d'impact (question 3.1) : le PCA tient la DMIA du processus de réception (une heure), le PRA la DMIA de l'application (24 heures) et la PDMA (nulle pour les pesées). Un plan non testé n'offre aucune garantie (F12 § 4).

| Élément du dispositif | Contenu proposé pour la campagne 2027 | Enseignement de septembre 2026 |
|---|---|---|
| **Mode dégradé de la réception** (a-2) | dans chaque cave, un kit de réception prêt avant la campagne : carnets de bons pré-numérotés en double exemplaire (un pour le viticulteur), fiche de pesée et de degré à remplir, consignes d'affectation aux cuves affichées, fiche réflexe ; bascule décidée par le directeur de cave dans les 30 minutes ; saisonniers formés au mode dégradé ; ressaisie à deux (saisie et contrôle) dès le retour du logiciel, avec rapprochement des doubles et relevé envoyé à l'adhérent pour vérification | feuilles volantes sans numérotation, 3 heures d'attente, 385 bons ressaisis et 25 erreurs relevées par les adhérents |
| **Sauvegardes et tests des restaurations** (a-3) | pendant la campagne, sauvegarde au moins quotidienne des données de chaque cave, et copie des pesées en fin de journée ; le double de chaque bon, imprimé et conservé par la cave, garantit qu'aucune pesée ne se perd entre deux copies (PDMA nulle) ; une copie **déconnectée** (hors ligne) et une copie **hors du site** de la cave (à l'union ou chez un hébergeur), conformément au guide d'hygiène de l'ANSSI (annexe 3.4) ; test de restauration complet de chaque cave avant fin juillet, puis vérification quotidienne de la sauvegarde pendant la campagne ; mises à jour des serveurs et des postes faites avant la campagne | disque de sauvegarde branché en permanence et chiffré avec le serveur ; dernière copie du 15 juin ; aucune restauration jamais essayée ; trois autres caves dans la même situation |
| **Exercice avant les vendanges** (a-4) | en juillet 2027, avant l'ouverture des quais fin août : scénario « serveur de la cave chiffré à 6 h 30 un jour de pointe » ; participants : directeur et chef de quai, saisonniers déjà recrutés, équipe informatique de l'union, prestataire, éditeur ; déroulé : alerte, bascule en mode dégradé chronométrée, restauration réelle sur un serveur de secours, ressaisie d'un lot de bons ; au moins une cave par éditeur, toutes les caves sur deux ans ; mesures : délai de bascule, délai de restauration, erreurs de ressaisie ; retour d'expérience écrit et mise à jour du plan | aucune procédure écrite ; décision de payer ou non la rançon prise le lendemain ; union prévenue à 10 h ; assistance de l'éditeur fermée avant 9 h |

L'ensemble suit la logique d'amélioration continue d'ISO 22301:2019 (analyse d'impact, stratégie, plans, exercices, revue), sans viser une certification ; EBIOS Risk Manager peut éclairer les scénarios de menace impliquant les prestataires et les éditeurs.

*3.2 b) – Rôles, responsabilités et pilotage*

| Acteur | Rôles et responsabilités dans le dispositif (b-1) |
|---|---|
| **Union** (direction générale et responsable du système d'information) | porte la politique de continuité commune, conduit l'analyse d'impact, fournit le modèle de PCA et de kit dégradé, organise la copie hors site des sauvegardes des caves et leur vérification quotidienne, assure une permanence informatique de 7 h à 21 h pendant les vendanges, tient le registre des incidents et le tableau de bord (question 3.5), coordonne la cellule de crise |
| **Caves** (directeur, avec le président informé) | appliquent le PCA local, tiennent le kit dégradé prêt, forment les saisonniers, déclenchent le mode dégradé, alertent l'union dans les 15 minutes, participent à l'exercice ; le directeur de cave reste responsable de la réception de sa cave |
| **Prestataire informatique local** (TRAMONTEL Informatique et les autres prestataires) | met en place les sauvegardes et leur copie déconnectée, contrôle leur bon déroulement, restaure en cas d'incident avec un délai d'intervention garanti pendant les vendanges, tient un serveur de secours prêt ; rend compte à l'union, et pas seulement à la cave |
| **Éditeur du logiciel de cave** (MOUSTERAL Logiciels et les trois autres) | assistance étendue pendant les vendanges (dès 7 h, week-end compris), procédure documentée de réinstallation et de restauration de son logiciel, participation aux tests et à l'exercice, information sur les mises à jour à faire avant la campagne |

Le **pilotage** (b-2) relève de la direction de l'union, parce que la réception est un système critique pour toutes les caves et pour la troisième priorité du plan « ROCALDÈNE 2030 » :
- **instance** : un comité de campagne présidé par Mme MAZERANDE (directrice de la production et de la qualité, directeur administratif et financier, responsable du système d'information, deux ou trois directeurs de cave), mensuel de mai à août, puis point quotidien pendant les vendanges à partir du tableau de bord ;
- **décisions** : adopter la politique de continuité et les règles communes (sauvegardes, kit dégradé, chaîne d'alerte) ; décider fin juillet, au vu des tests et de l'exercice, si chaque cave est prête et, sinon, des mesures d'appoint ; arbitrer les moyens (permanence, serveur de secours) ; en crise, la cellule de crise décide selon des règles fixées à l'avance, dont la position de principe sur le paiement d'une rançon, arrêtée par le conseil de l'union et reprise par le conseil de chaque cave, ce qui évite le flottement de septembre 2026 ;
- **compte rendu** : Mme MAZERANDE présente au conseil, à chaque réunion, l'état de préparation (caves testées, exercice réalisé), puis le bilan de la campagne (incidents, indicateurs), comme le prévoit le plan ; le conseil approuve la politique de continuité.

**Réponses tolérées**
- Site de secours ou poste de réception de secours fourni par l'union, version hors ligne du logiciel demandée à l'éditeur, impression autonome des tickets du pont-bascule : acceptés comme éléments du mode dégradé.
- Règle 3-2-1 des sauvegardes citée.
- Désignation d'un responsable de la continuité ou d'un responsable de la sécurité des systèmes d'information rattaché à la direction générale.
- Instance confiée au comité de direction élargi aux directeurs de cave.

**Erreurs fréquentes**
- *PCA et PRA confondus* (`ET-02`, `JUR-S02`) — « le PRA est le mode dégradé » ; juste : le PCA maintient l'activité, le PRA rétablit le système et ramène à la normale.
- *Dispositif purement technique* (`JUR-T12`, `JUR-S06`) — paramétrage des sauvegardes ou des serveurs ; juste : organisation, rôles, décisions, tests.
- *Plan non testé* (`JUR-S08`) — juste : exercice et restaurations réelles avant la campagne.
- *Rôles flous ou sans les prestataires* (`JUR-T08`) — juste : prestataire et éditeur ont des engagements pendant les vendanges et rendent compte à l'union.
- *Politique de sécurité complète ou gestion des identités développées* (périmètre de la question) — juste : continuité et reprise de la réception.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| PCA, PRA, exercices, rôles | définitions, gouvernance des systèmes critiques | F12 § 1 et 4 | notion de cours |
| ISO 22301:2019 | management de la continuité, exercices et tests | `iso_22301_2019` ; F12 § 4 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | sauvegardes, copie hors ligne, restaurations testées | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager, version 1.5 | scénarios impliquant prestataires et éditeurs (toléré) | `ebios_rm_1_5` ; F12 § 2 | en vigueur |

---

### 3.3 – Le module de détection des apports anormaux (1,5 point)

**Référence au programme**
- §4.1 : `4.1.f` « Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques ». Limites : l'IA s'analyse dans ses effets métiers ; le développement d'algorithmes d'apprentissage automatique n'est pas attendu.

**Annexes mobilisées** : annexe 3.2 (constats, proposition et test du module) et annexe 3.1 (volumes, incident de GRAUSSELLE).

**Barème indicatif (1,5 pt)**

| Item | Attendu | Points |
|---|---|---|
| 1 | Module situé dans l'apprentissage automatique (détection d'anomalies), distingué de l'IA générative ; deux apports pour la détection et la prévention, appliqués au cas | 0,5 |
| 2 | Trois limites, sur les données d'apprentissage, les faux positifs et le contrôle humain, chacune appuyée sur l'annexe 3.2 | 0,5 |
| 3 | Recommandation motivée sur l'adoption pour 2027 et deux conditions au moins | 0,5 |

**Réponse attendue**

*Famille d'IA et apports (item 1)*

Le module relève de l'**apprentissage automatique** : il apprend, à partir des apports passés, un profil d'apport « normal » et attribue à chaque nouvel apport un signal d'écart (**détection d'anomalies**) ; il produit une alerte, non un contenu, et ne relève donc pas de l'**IA générative**, qui génère du texte ou des images (F13 § 1). Deux apports :
1. **Un examen exhaustif et immédiat** : aujourd'hui, aucun des environ 20 000 apports n'est contrôlé après la pesée ; le module examine chaque apport au moment de la pesée, quand une erreur peut encore être corrigée avant que la vendange soit versée (nouvelle mesure du degré, vérification de l'adhérent ou de la parcelle).
2. **Un ciblage des contrôles humains et un effet dissuasif** : le test a fait apparaître, à GRAUSSELLE, 20 erreurs ou anomalies réelles que personne n'avait vues ; savoir que les écarts sont repérés décourage les manipulations.

*Trois limites (item 2)*

- **Données d'apprentissage** : le module a appris sur trois caves seulement, sur trois vendanges (2023 à 2025), avec un seul logiciel ; les six autres caves ont d'autres logiciels et d'autres pratiques ; il ignore les situations nouvelles (pluies de la mi-septembre 2026, première récolte d'un cépage planté en 2023) ; surtout, il apprend sur des données dont la fiabilité est en cause (600 bons modifiés après la pesée sans trace, bons ressaisis après l'incident) : il risque d'apprendre comme « normal » ce qui est anormal. Le chiffre de « 9 apports anormaux sur 10 » n'est pas vérifié sur les données de l'union.
- **Faux positifs** : sur 300 apports signalés, 20 seulement étaient de vraies anomalies, soit environ 7 % ; à l'échelle des neuf caves, un taux de 15 % représenterait environ 3 000 alertes par campagne, jusqu'à 135 par jour de pointe (15 % de 900 apports), qu'aucune équipe ne peut examiner pendant les vendanges : les alertes seraient ignorées, ou bien elles retarderaient la réception.
- **Contrôle humain** : le blocage automatique de tout bon signalé arrêterait la réception, ce qui recrée le problème de continuité de la question 3.1, et retirerait la décision à un humain ; personne n'est désigné pour examiner les alertes ni pour en répondre auprès des adhérents, qui voudront comprendre pourquoi leur apport est bloqué ; enfin, le module ne voit que la valeur finale du degré : les six bons modifiés à la main n'ont pas été signalés. Il ne remplace donc pas les contrôles de base (accès nominatifs, séparation des tâches, journal des modifications : question 3.4).

*Recommandation (item 3)*

Ne pas déployer le module dans les neuf caves pour la campagne 2027, ni avec le blocage automatique. Priorité aux contrôles de base, dont l'audit de juin 2027 dira l'état. Un pilote est possible en 2027 dans les trois caves équipées par MOUSTERAL Logiciels, à quatre conditions : (1) **alerte sans blocage**, examinée par une personne désignée (œnologue ou directrice de la production), dont la décision est tracée ; (2) **mesure** du taux de vraies anomalies parmi les signalements, avec un seuil d'alerte réglé pour rester examinable ; (3) **apprentissage** sur des données fiabilisées et représentatives des neuf caves avant toute généralisation ; (4) **explication** aux adhérents de ce que fait le module. Le coût affiché (20 k€ puis 15 k€ par an) est modeste, mais le temps d'examen des alertes est un coût caché à prévoir.

**Réponses tolérées**
- Apprentissage supervisé ou non supervisé évoqué sans erreur, sans développement.
- Adoption immédiate recommandée, si elle est assortie de l'absence de blocage, d'un examen humain désigné et de la mise en place préalable des contrôles de base.
- Autres apports : repérage des tares de remorques anciennes, des parcelles ou des adhérents incohérents.

**Erreurs fréquentes**
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — juste : le module classe et signale, il ne génère pas de contenu.
- *Opportunités sans limites* (`ET-19`, `JUR-T03`) — reprendre la plaquette (« 9 sur 10 ») ; juste : le test montre environ 7 % de vraies anomalies parmi les signalements.
- *Fonctionnement interne du modèle décrit* (hors programme) — juste : effets métiers, données, supervision.
- *IA présentée comme un substitut aux contrôles* (`JUR-T11`) — juste : elle complète les accès nominatifs, la séparation des tâches et la journalisation.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie de l'IA, apprentissage automatique, IA générative | familles, distinction | F13 § 1 | notion de cours |
| Risques de l'IA (biais, données, dépendance), supervision humaine | limites et conditions | F13 § 3 et 4 | notion de cours |

---

### 3.4 – L'audit du module des apports (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la conformité financière et comptable n'est pas traitée.

**Annexes mobilisées** : annexe 3.2 (constats, demande de la directrice générale), annexe 3.1 (éditeurs, acteurs), annexe 3.4 (ISO/IEC 27001:2022 et 27002:2022) et annexe 1.1 (neuf caves, organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Audit du système d'information défini (examen indépendant et méthodique, au regard d'un référentiel, recommandations) ; quatre étapes appliquées au cas, de la cartographie du processus à la restitution | 0,5 |
| b | Trois risques tirés de l'annexe 3.2, chacun avec le contrôle attendu et la manière d'en vérifier le fonctionnement ; 0,5 dès deux risques complets | 1 |
| c | Trois critères de performance et de conformité, chacun illustré par un point de contrôle du module des apports | 0,5 |

**Réponse attendue**

*3.4 a) – Définition et démarche*

L'**audit du système d'information** est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel (normes, règles internes, engagements), la performance, la sécurité, la fiabilité et la conformité d'un système ou d'un processus, et formule des recommandations (F10 § 1.1). Ici, il porte sur un processus applicatif, de la pesée au relevé adressé à l'adhérent, dans les neuf caves.

| Étape | Objet dans le cas |
|---|---|
| 1. Cadrage et prise de connaissance | objectifs fixés par Mme MAZERANDE (confiance des adhérents et du conseil dans les chiffres des apports) ; périmètre : le module des apports des quatre logiciels dans les neuf caves ; référentiel : mesures d'ISO/IEC 27001:2022 sur les droits d'accès, la journalisation et la séparation des tâches, détaillées par le guide ISO/IEC 27002:2022, et règles de réception de l'union ; calendrier : conclusions en juin 2027 ; interlocuteurs : directrice de la production, directeurs de cave, éditeurs |
| 2. Cartographie du processus de réception | étapes (identification de l'adhérent et de la parcelle, pesée, déduction du poids à vide de la remorque, mesure du degré, impression du bon, affectation à la cuve, modifications éventuelles, relevé adressé à l'adhérent), acteurs (agent de réception, chef de quai, directeur), logiciel et paramètres de chaque cave, points où une donnée peut être créée ou modifiée |
| 3. Évaluation des risques et des contrôles | cotation des risques de chaque étape, puis vérification des contrôles attendus (sous-question b) dans un échantillon de caves couvrant les quatre logiciels, puis dans les neuf caves pour les points les plus graves |
| 4. Restitution et suivi | constats validés avec les directeurs de cave, recommandations priorisées à appliquer avant l'ouverture des quais fin août, plan d'action (responsable, échéance), éléments utiles à la décision sur le module de MOUSTERAL Logiciels |

*3.4 b) – Risques, contrôles attendus et vérification*

| Risque du processus de réception (annexe 3.2) | Contrôle attendu | Vérification par l'auditeur |
|---|---|---|
| **Actions non imputables** : compte unique « PESÉE » partagé par les agents et les saisonniers dans six caves, mot de passe affiché | **accès nominatifs** : un compte par personne, saisonniers compris, ouvert à l'embauche et fermé en fin de campagne, mot de passe personnel ou badge | rapprochement de la liste des comptes de chaque logiciel avec la liste du personnel et des saisonniers de 2026 ; observation du poste de pesée ; contrôle que chaque connexion de la campagne est rattachée à une personne |
| **Cumul de fonctions incompatibles** : le chef de quai crée l'adhérent ou la parcelle, pèse et modifie le bon ; trois directeurs modifient eux-mêmes les paramètres, dont le poids à vide des remorques | **séparation des tâches** : la création des adhérents, des parcelles et des poids à vide, la pesée, et la correction d'un bon validé relèvent de personnes différentes ; toute correction est validée par une seconde personne | extraction de la matrice des droits de chaque logiciel et repérage des conflits (cible : aucun) ; revue des changements de paramètres de 2026 et de leur autorisation |
| **Modification non tracée du degré ou du poids après la pesée** : environ 600 bons modifiés après leur impression, sans motif ni valeur d'origine conservée ; écarts de plus de 0,5 % vol. constatés sur des bons papier ; journal absent ou désactivé dans huit caves | **journalisation des modifications** : un bon validé ne se modifie qu'avec un motif ; le journal enregistre l'auteur, la date, l'ancienne et la nouvelle valeur ; il est revu chaque semaine pendant la campagne par la direction de la production | vérification, cave par cave, que le journal existe et est activé (VALCROZIÈRES) ; rapprochement d'un échantillon de doubles de bons conservés par les viticulteurs avec les données du logiciel et les relevés ; examen des modifications de 2026 et de leurs motifs |

*3.4 c) – Critères de performance et de conformité*

| Critère | Point de contrôle propre au module des apports |
|---|---|
| **Fiabilité** (exactitude, exhaustivité, intégrité des données) | numérotation continue des bons sans rupture ; concordance entre le bon remis, la base et le relevé de l'adhérent ; poids à vide des remorques à jour |
| **Sécurité** (accès, traçabilité) | comptes nominatifs, droits revus avant chaque campagne, journal des modifications actif dans les neuf caves |
| **Conformité** (aux règles de réception de l'union et des caves, au référentiel retenu) | procédure de correction d'un bon écrite et appliquée ; mesures d'ISO/IEC 27001:2022 retenues effectivement en place |

**Réponses tolérées**
- Démarche en cinq ou six étapes, si les quatre éléments demandés y figurent.
- Démarche cartographie – évaluation des risques – évaluation des contrôles – restitution, le cadrage (objectifs, périmètre, référentiel, calendrier) étant intégré à la première étape.
- Quatrième risque : absence de contrôle a posteriori (rapprochement des bons et des relevés) ; contrôle de cohérence à la saisie (degré hors des valeurs plausibles).
- Critère d'**efficacité** (durée moyenne d'une pesée, disponibilité du module) à la place de l'un des trois.
- Conformité au RGPD pour les données des adhérents, personnes physiques, citée sans développement.
- COSO cité comme cadre du contrôle interne, sans développement.

**Erreurs fréquentes**
- *Méthodologie incomplète ou générique* (`JUR-A01`) — étapes sans objet propre au cas ; juste : périmètre, référentiel, cartographie, restitution datée.
- *Audit du SI confondu avec l'audit légal des comptes* (`ET-34`) — juste : l'audit porte sur un processus applicatif et ses contrôles.
- *Contrôle cité sans moyen de le vérifier* (`JUR-T03`) — juste : extraction des droits, rapprochement d'échantillons, examen du journal.
- *Tests techniques de sécurité proposés comme diligence* (hors programme) — juste : revue des droits, des journaux et des paramètres.
- *Norme et référentiel confondus* (`ET-01`, `JUR-S06`) — juste : ISO/IEC 27001:2022 est une norme d'exigences, ISO/IEC 27002:2022 un guide de mesures.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI, démarche, critères | définition, étapes, critères | F10 § 1.1 et 1.2 | notion de cours |
| Séparation des tâches, piste d'audit | contrôles attendus | F10 § 3.1 et 3.2 | notion de cours |
| ISO/IEC 27001:2022 ; ISO/IEC 27002:2022 | référentiel de l'audit : droits d'accès, journalisation, séparation des tâches | `iso_27001_2022`, `iso_27002_2022` ; F12 § 2 | en vigueur |
| RGPD | données des adhérents (toléré) | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.5 – Le tableau de bord du système d'information de la campagne (1,5 point)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ». Limites : les méthodes classiques de suivi des budgets ne sont pas approfondies ; recul critique sur les indicateurs.

**Annexes mobilisées** : annexe 3.1 (incidents, coûts de la campagne 2026, demande de la directrice générale), annexe 1.1 (vendange de 380 milliers d'hectolitres, organigramme).

**Barème indicatif (1,5 pt)**

| Item | Attendu | Points |
|---|---|---|
| 1 | Principe d'un tableau de bord équilibré du SI (peu d'indicateurs reliés aux objectifs, équilibre performance, risques et coûts, cibles et seuils d'alerte) ; destinataires et fréquence adaptés à la campagne | 0,5 |
| 2 | Trois indicateurs (performance, risque, coût), chacun avec formule, source, fréquence, cible et axe, justifiés par l'annexe 3.1 ; 0,5 dès deux indicateurs complets | 1 |

**Réponse attendue**

*Principe, destinataires et fréquence (item 1)*

Un tableau de bord du système d'information réunit un petit nombre d'indicateurs reliés aux objectifs, chacun assorti d'une cible et d'un seuil d'alerte, pour décider et non pour décrire ; inspiré du tableau de bord prospectif adapté aux SI (Van Grembergen, F09 § 4.1), il **équilibre** la **performance** (le service rendu aux caves et aux adhérents), les **risques** (ce qui pourrait arrêter la réception) et les **coûts** (ce que coûte ce service), pour éviter qu'un indicateur ne s'améliore au détriment des autres (réduire le soutien informatique au prix d'une campagne plus exposée, par exemple). Pour la campagne : **destinataires** : Mme MAZERANDE et le comité de campagne (la « page quotidienne » demandée), chaque directeur de cave pour sa cave, le conseil pour le bilan ; **fréquence** : quotidienne pendant les vendanges, avec une synthèse hebdomadaire et un bilan en fin de campagne ; établi par le responsable du système d'information à partir du registre des incidents, qui n'existe pas aujourd'hui.

*Trois indicateurs (item 2)*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Performance** : taux de disponibilité de la réception informatisée | (heures d'ouverture des quais − heures d'interruption de la réception informatisée) / heures d'ouverture des quais, par cave et pour l'union | registre des incidents de campagne tenu par l'équipe informatique de l'union, horaires d'ouverture des quais | quotidienne pendant la campagne | au moins 99,5 % par cave, soit environ 3 heures d'arrêt au plus sur les 630 heures d'ouverture, et aucune interruption de plus de 30 minutes sans bascule en mode dégradé (4 interruptions de plus d'une heure en 2026) | processus |
| **Risque** : part des caves dont la sauvegarde de la veille est vérifiée et copiée hors ligne | nombre de caves dont la sauvegarde de la nuit a été vérifiée et dont une copie est conservée hors ligne et hors site / 9 | rapports quotidiens des prestataires des caves, vérifiés par l'équipe informatique de l'union | quotidienne pendant la campagne | 100 % chaque jour (en 2026, l'état des sauvegardes des caves était inconnu de l'union) | processus |
| **Coût** : coût du soutien informatique de la campagne par millier d'hectolitres reçus | (factures des prestataires des caves et des éditeurs liées à la campagne + heures supplémentaires de l'équipe informatique) / volume reçu en milliers d'hectolitres | comptabilité de l'union et des caves (factures, paie), logiciels de cave (volumes reçus) | hebdomadaire pendant la campagne, bilan à la clôture de la campagne | 200 € au plus par millier d'hectolitres en 2027, contre environ 250 € en 2026 (95 k€ pour 380 milliers d'hectolitres) | financier |

Lecture critique : la cible de coût ne doit pas conduire à réduire la permanence ou les tests, qui protègent la disponibilité ; à l'inverse, un taux de disponibilité élevé sans sauvegarde vérifiée masquerait le risque, d'où l'équilibre des trois indicateurs.

**Réponses tolérées**
- Autres indicateurs complets et justifiés : délai moyen d'attente des remorques (axe client, cible 20 minutes au plus), délai de bascule en mode dégradé, nombre d'incidents interrompant la réception plus d'une heure (cible 0 contre 4), part des bons corrigés après la pesée avec motif (lien avec la question 3.4), coût de l'incident évité.
- Axe « risques » proposé en plus des axes du tableau de bord prospectif, s'il est justifié.

**Erreurs fréquentes**
- *Indicateurs génériques ou incomplets* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe, reliés à l'annexe 3.1.
- *Tableau de bord limité à la technique* (`ET-18`) — juste : performance pour les caves, risques et coûts.
- *Calcul ou décomposition d'écarts budgétaires* (hors programme) — juste : un indicateur de coût lu par rapport à une cible.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Tableau de bord du SI, indicateurs à cinq champs | structure, axes | F09 § 4 | notion de cours |
| IT Balanced Scorecard (Van Grembergen) | tableau de bord prospectif adapté aux SI | `van_grembergen_it_bsc` ; F09 § 4.1 | publié |

---

### 3.6 – Le choix d'un hébergement responsable (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : normes environnementales techniques mobilisées à titre illustratif ; durabilité intégrée à la gouvernance globale du SI.

**Annexes mobilisées** : annexe 3.3 (salle, options, positions), annexe 3.4 (loi REEN, RGESN, champ de la CSRD donné), annexe 3.1 (continuité) et annexe 1.1 (plan « ROCALDÈNE 2030 », budget du SI).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Sobriété numérique définie (questionner le besoin avant l'efficacité, distincte de l'économie d'énergie) ; stratégie responsable du SI précisée (durabilité intégrée aux choix et à la gouvernance, trajectoire mesurée) et appliquée au cas | 0,5 |
| a-2 | Quatre critères d'impact environnemental, chacun avec un indicateur et sa limite | 0,5 |
| b-1 | Comparaison des trois options sur les critères, le coût sur trois ans (480, 390 et 550 k€) et la continuité | 0,5 |
| b-2 | Lecture critique des données des prestataires (PUE estimé, mesuré ou mondial ; neutralité par compensation ; capacités facturées à l'usage et effet rebond) | 0,5 |
| b-3 | Option recommandée et justifiée ; deux conditions de réussite | 0,5 |
| c | Deux indicateurs complets (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.6 a) – Sobriété, stratégie responsable et critères*

La **sobriété numérique** consiste à interroger le besoin avant de chercher l'efficacité : ne garder que les équipements, les capacités et les données utiles, au juste niveau ; elle ne se réduit pas à économiser l'énergie, qui relève de l'efficacité (Green IT) (F14 § 3). Une **stratégie responsable du système d'information** intègre la durabilité environnementale et sociale dans les choix du SI (achats, hébergement, durée de vie, usages) et dans sa gouvernance, avec une trajectoire, des indicateurs et des arbitrages entre valeur et empreinte, au lieu d'en faire un ajout marginal (F14 § 0). Dans le cas, elle sert la troisième priorité du plan « ROCALDÈNE 2030 », dont Mme MAZERANDE doit pouvoir montrer au conseil « des progrès mesurés, pas des promesses » ; elle commence par un geste de sobriété commun aux options A et B : retirer les 12 serveurs anciens et regrouper les applications sur les 8 serveurs récents, puisque la plupart des serveurs sont utilisés à moins de 20 % de leurs capacités. La loi REEN (annexe 3.4) vise d'ailleurs des centres de données moins énergivores et l'allongement de la durée de vie des équipements.

| Critère (a-2) | Indicateur de mesure | Limite de l'indicateur |
|---|---|---|
| Efficacité énergétique de l'hébergement | **PUE** = énergie totale / énergie des équipements informatiques (2,0 aujourd'hui) | ne dit rien de l'utilité des serveurs, de l'origine de l'électricité ni de la fabrication ; sa valeur dépend du mode de mesure (estimée, mesurée sur un site, moyenne mondiale) |
| Consommation d'énergie | **MWh par an** consommés pour héberger les applications de l'union (130 MWh en 2026) | dépend du périmètre ; non communiquée dans un cloud mutualisé ; ne dit rien des émissions |
| Contenu carbone de l'électricité | part d'électricité renouvelable attestée (garanties d'origine), émissions par kWh du lieu d'implantation | les garanties d'origine attestent une production, pas une consommation heure par heure ; la « neutralité » par compensation ne réduit pas les émissions |
| Cycle de vie des équipements | nombre de serveurs retirés, réemployés ou recyclés, durée de vie moyenne à leur retrait, serveurs achetés | la fabrication des équipements du fournisseur (cloud) n'est pas visible ; une mesure complète supposerait une analyse du cycle de vie |

Autres critères acceptés : réutilisation de la chaleur (part de la chaleur récupérée), consommation d'eau du refroidissement.

*3.6 b) – Comparaison et recommandation*

| | Option A – rénover la salle | Option B – centre de données régional | Option C – cloud public |
|---|---|---|---|
| Efficacité énergétique | PUE 1,5, estimé | PUE 1,3, **mesuré et publié** | PUE 1,2, **moyenne mondiale**, rien pour le site |
| Consommation | environ 45 MWh | environ 39 MWh, soit environ 70 % de moins qu'en 2026 | non communiquée |
| Électricité | réseau national | renouvelable régionale, garanties d'origine | « neutralité » par certificats et compensation ; mix du pays plus carboné que celui de la France |
| Chaleur | perdue | récupérée (piscine intercommunale) | non communiquée |
| Équipements | 8 serveurs conservés, 12 retirés ; climatiseurs et onduleurs neufs | 8 serveurs conservés, 12 retirés | serveurs retirés à mesure du transfert, sauf ceux du progiciel, qui restent dans la salle actuelle ; capacités du fournisseur |
| Coût sur trois ans | 300 + 3 × 60 = **480 k€** | 150 + 3 × 80 = **390 k€** | 250 + 3 × 100 = **550 k€**, variable, et la salle de Pézenas reste nécessaire pour le progiciel jusqu'à son remplacement |
| Continuité | salle toujours exposée aux canicules ; pas de second site | second site distinct de Pézenas, personnel jour et nuit, copies des sauvegardes de l'union et des caves possibles ; dépend des deux liaisons réseau | infrastructure résiliente, mais dépendance au réseau et au fournisseur ; progiciel toujours à Pézenas |

Lecture critique (b-2) : les données ne se valent pas. Le PUE de A est une estimation, celui de B une mesure publiée, celui de C une moyenne mondiale qui ne dit rien du centre qui hébergerait les données ; la « neutralité carbone » de C repose sur la compensation et non sur une réduction, alors que l'électricité du pays d'implantation est plus carbonée ; la facturation à l'usage et l'ajout de capacités « en quelques minutes » exposent à un **effet rebond** contraire à la sobriété. L'argument de M. VERDAGNOL (« on ne paie que ce qu'on consomme ») ne tient pas ici : l'option C est la plus chère sur trois ans, son coût est variable, et elle laisse le progiciel à Pézenas.

Recommandation (b-3) : l'**option B**. Elle combine la meilleure performance environnementale vérifiable (PUE mesuré de 1,3, électricité renouvelable attestée, chaleur réutilisée, consommation divisée par plus de trois), le coût le plus bas sur trois ans (390 k€, soit environ 130 k€ par an, à rapprocher d'un budget du SI de 2 200 k€) et un apport décisif à la continuité : un second site pour les sauvegardes de l'union et des caves (question 3.2), et la fin de l'exposition aux canicules. Conditions de réussite (deux attendues) :
1. **Sobriété d'abord** : retirer les 12 serveurs anciens et regrouper les applications **avant** le transfert, faire réemployer ou recycler les serveurs retirés de manière tracée, et allonger la durée de vie des 8 serveurs récents.
2. **Données environnementales vérifiables** : obtenir de LIMBRÈZE Data un relevé régulier du PUE, de la consommation des équipements de l'union et des garanties d'origine, pour alimenter les indicateurs (sous-question c) et le compte rendu au conseil.
3. **Continuité** : deux liaisons effectivement indépendantes, mode dégradé maintenu à Pézenas et dans les caves, et restauration testée depuis le second site.
4. **Réversibilité** : ne pas s'enfermer, et réexaminer l'hébergement avec les mêmes critères lors du choix du futur progiciel de l'union.

L'option A reste défendable si la dépendance au réseau est jugée inacceptable ; l'option C pourrait être reconsidérée après le remplacement du progiciel, si le fournisseur communique des données propres au site.

*3.6 c) – Deux indicateurs de suivi*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Indicateur d'efficacité énergétique (PUE) de l'hébergement des serveurs de l'union | énergie totale consommée par l'hébergement / énergie consommée par les équipements informatiques de l'union | relevés du centre de données LIMBRÈZE Data, transmis chaque trimestre | trimestrielle | 1,3 au plus dès 2028, contre environ 2,0 en 2026 | environnement |
| Consommation d'électricité annuelle de l'hébergement des serveurs de l'union | somme des relevés mensuels de consommation de l'hébergement (équipements et part du bâtiment), en MWh | relevés mensuels du centre de données ; inventaire des serveurs de l'équipe informatique | annuelle, à partir des relevés mensuels | 40 MWh au plus en 2028, contre 130 MWh en 2026 | environnement |

(0,5 pt pour les deux indicateurs complets.) Le PUE seul pourrait s'améliorer alors que la consommation augmente : les deux indicateurs se lisent ensemble.

**Réponses tolérées**
- Option A recommandée si le candidat la justifie par la maîtrise et l'absence de dépendance au réseau, en reconnaissant son PUE et son exposition aux canicules ; option C recommandée seulement avec des exigences de données propres au site et une réponse au cas du progiciel.
- Autres indicateurs complets : part d'électricité renouvelable attestée (cible 100 %), part des serveurs retirés réemployés ou recyclés de manière tracée (cible 100 %), durée de vie moyenne des serveurs à leur retrait, part de la chaleur réutilisée.
- Mention de l'étude ADEME-Arcep pour rappeler le poids de la fabrication des équipements, sans calcul.
- Mention de la CSRD pour dire seulement que l'union n'y est pas soumise (donnée de l'annexe 3.4).

**Erreurs fréquentes**
- *Sobriété confondue avec l'économie d'énergie* (`ET-12`) — juste : d'abord réduire le nombre de serveurs et les capacités, puis chercher l'efficacité.
- *Empreinte réduite à l'électricité ou au PUE* (`ET-38`) — juste : origine de l'électricité, fabrication et durée de vie, chaleur.
- *Données des prestataires prises pour argent comptant* (`JUR-T03`) — juste : distinguer estimation, mesure et moyenne mondiale, compensation et réduction.
- *Cloud présenté comme toujours plus vert ou moins cher* (`ET-30`, `JUR-G11`) — juste : il déplace l'empreinte, peut favoriser l'effet rebond, et coûte ici le plus cher.
- *Calcul d'empreinte ou discussion du champ de la CSRD* (`ET-41`) — juste : ni calcul ni assujettissement, qui est une donnée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Sobriété numérique, Green IT, stratégie responsable, PUE, cloud et centres de données | définitions, critères, indicateurs | F14 § 0, 3, 4 et 5 | notion de cours |
| Loi REEN n° 2021-1485 | centres de données moins énergivores, durée de vie des équipements | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | famille de critères sur l'hébergement | `rgesn_2024` ; F14 § 2 | en vigueur |
| Étude ADEME-Arcep sur l'empreinte du numérique | poids de la fabrication (toléré) | `etude_ademe_arcep_numerique` ; F14 § 1 | en vigueur |
| Directive (UE) 2022/2464 (CSRD) | union hors champ (donnée) | `csrd` ; fiche commune | en vigueur |
| Directive (UE) 2022/2555 (NIS 2) | union hors champ (donnée) | `nis2` ; F12 § 6 | en vigueur au niveau européen |
