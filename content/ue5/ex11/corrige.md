# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 11 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F12 sécurité et résilience, F10 audit et fiabilisation (habilitations, moindre privilège, revue des droits), F02 et F05 (matrice de responsabilités), et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Risques pesant sur le système de supervision | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers | 4 |
| 2.2 Démarche et principes de la politique de cybersécurité | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques | 3 |
| 2.3 Architecture de confiance | `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) | 2 |
| 2.4 Gestion des identités et surveillance des connexions | `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA | 2 |
| 2.5 Gouvernance de la sécurité de la supervision | `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ; `4.2.a` Définir et piloter une politique de sécurité du SI […] de gouvernance des systèmes critiques | 2 |
| **Dossier 2 – Sécuriser le système de supervision des installations et ses accès** |  | **13** |

Répartition indicative : connaissances (typologie des risques, analyse d'impact sur l'activité, politique de sécurité et étapes d'EBIOS Risk Manager, modèle Zero Trust, intérêt d'une matrice de responsabilités) 3 points (items 2.1 a-1, 2.1 b-1, 2.2 a-1, 2.2 a-2 pour moitié, 2.3-1, 2.5 a pour un quart) ; analyse des annexes et recommandations 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Risques pesant sur le système de supervision (4 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ».

**Annexes mobilisées** : annexes 1.1 (120 sites supervisés, organisation), 2.1 (fonctionnement, inventaire des comptes, organisation de la sécurité), 2.2 (chronologie, constats, scénario redouté) et 2.3 (NIS 2 et son statut).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée : quatre catégories définies (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers), un risque étant formulé comme un événement redouté, avec sa cause et sa conséquence | 0,5 |
| a-2 | Six risques tirés des annexes, chacun formulé et rattaché à la bonne catégorie, au moins un par catégorie ; 0,5 pour quatre risques correctement classés | 1 |
| b-1 | Analyse d'impact sur l'activité définie (processus critiques, conséquences dans le temps, interruption tolérable, priorités) | 0,5 |
| b-2 | Conséquences du scénario analysées sur les trois plans (processus, continuité du service, santé des usagers), avec les chiffres et les faits des annexes et une conclusion sur la criticité ; 0,5 pour deux plans | 1 |
| c | Trois constats tirés de l'annexe 2.2 : détection fortuite et tardive, traitement lent et sans procédure, risques connus non traités faute de propriétaire ; 0,5 pour deux constats | 1 |

**Réponse attendue**

*2.1 a) – Typologie et classement de six risques*

Un **risque du système d'information** est un événement possible qui, s'il survient, porte atteinte à la disponibilité, à l'intégrité, à la confidentialité ou à la traçabilité de l'information et des traitements, et par là aux missions de l'organisation ; on le formule par sa cause, l'événement redouté et sa conséquence. Le programme en distingue quatre catégories : les **cybermenaces** (actes malveillants délibérés : usurpation de compte, logiciel malveillant, rançongiciel, attaque par un prestataire), les **défaillances opérationnelles** (erreurs, pannes, obsolescence, procédures absentes ou mal appliquées), les **risques réglementaires** (non-respect d'obligations présentes ou à venir, responsabilité des dirigeants) et les **risques métiers** (atteinte aux missions, à la santé, à la confiance, aux finances) (F12 § 0 et 5) (0,5 pt).

| Catégorie | Risque (cause → événement redouté → conséquence) | Faits des annexes |
|---|---|---|
| **Cybermenace** | 1. Usurpation d'un compte de prestataire ou d'un compte générique, par l'accès à distance protégé par un seul mot de passe → modification des consignes ou désactivation des alarmes d'un site → réservoir vidé, traitement de l'eau altéré | incident du 22 novembre : compte d'un technicien parti fin juin ; 10 des 25 comptes de prestataires (40 %) au nom de techniciens partis ; accès ouverts en permanence ; aucune authentification multifacteur |
| **Cybermenace** | 2. Logiciel malveillant (rançongiciel, pièce jointe piégée) introduit par la messagerie, internet ou un poste de bureautique et propagé jusqu'aux postes de supervision → perte du pilotage à distance des 120 sites | réseau commun aux 300 postes de bureautique et aux six postes de supervision, sans cloisonnement ; messagerie et internet sur les postes de supervision ; quatre postes sans mises à jour de sécurité depuis 2023 ; trois agents d'astreinte sur leur ordinateur personnel |
| **Cybermenace** (chaîne d'approvisionnement) | 3. Compromission d'un des trois prestataires ou de son poste de télémaintenance → accès à la supervision sans contrôle de la régie | KERVALDIS, BRÉMONTAL et PURIMANE se connectent à toute heure sans prévenir ; contrats sans obligation de signaler les départs |
| **Défaillance opérationnelle** | 4. Actions non imputables et droits excessifs → erreur de manipulation ou acte malveillant interne impossible à retrouver | 3 comptes génériques pour environ 45 personnes, mots de passe inchangés de 2019 à novembre 2026 ; 52 des 60 comptes peuvent modifier les consignes ; compte « admin » partagé avec l'éditeur ; un quart des comptes (15) appartiennent à des personnes parties |
| **Défaillance opérationnelle** | 5. Absence de surveillance et de procédure d'incident → attaque détectée tard ou pas du tout, réaction improvisée | journaux conservés 30 jours, jamais consultés, aucune alerte ; connexion du 4 novembre passée inaperçue ; 3 h 30 avant une détection fortuite ; compte désactivé 28 heures après la détection |
| **Risque réglementaire** | 6. Écart entre les pratiques de la régie et les exigences qu'impose la directive NIS 2 aux entités qui entrent dans son champ (analyse des risques, chaîne d'approvisionnement, contrôle d'accès, authentification multifacteur, notification sous 24 heures, responsabilité des organes de direction) → mise en conformité tardive et coûteuse, responsabilité des dirigeants exposée, si la régie y était soumise, ce que le dossier ne demande pas d'apprécier | directive non transposée en droit français au 31/12/2026 (annexe 2.3) : le risque est **à venir** et appelle une anticipation ; conseil d'administration informé 18 jours après l'incident ; aucune procédure de notification |
| **Risque métier** | 7. Interruption de la distribution ou mise en distribution d'une eau impropre → atteinte à la santé des usagers, perte de confiance des abonnés et des élus de la communauté d'agglomération, coûts | réservoir de la Combe-Martel : 12 000 habitants, dont un établissement pour personnes âgées dépendantes, qui auraient manqué d'eau vers 8 h 30 ; scénario redouté (annexe 2.2 C) ; coût direct de 25 000 € pour un incident sans conséquence |

(1 pt pour six risques correctement formulés et classés, au moins un par catégorie ; 0,5 pt pour quatre. Le corrigé en propose sept ; six suffisent.)

*2.1 b) – Analyse d'impact du scénario redouté*

L'**analyse d'impact sur l'activité** (BIA) identifie les processus critiques d'une organisation, mesure, dans le temps, les conséquences de leur interruption ou de leur altération (humaines, opérationnelles, financières, d'image, juridiques) et fixe la durée d'interruption tolérable de chacun ; elle sert à hiérarchiser les mesures de sécurité et de continuité. C'est une démarche, distincte du plan de continuité, qu'elle prépare (F12 § 4) (0,5 pt).

Application au scénario de l'annexe 2.2 C (modification, une même nuit, des consignes de plusieurs réservoirs et du dosage des réactifs d'une usine) (1 pt) :

- **Processus de la régie** : sont atteints à la fois la **production** (dosage des réactifs dans une usine), la **distribution** (remplissage des réservoirs, marche des pompes) et le **contrôle de la qualité de l'eau** : l'alarme des analyseurs remonte par la supervision elle-même, de sorte qu'un attaquant qui la contrôle peut aussi aveugler la détection. La supervision est un **point unique** de pilotage et de détection pour 120 sites ; les interventions d'astreinte, l'accueil et l'information des abonnés sont ensuite saturés. La facturation, elle, n'est pas atteinte : l'impact ne se mesure pas d'abord en euros.
- **Continuité du service** : dans l'incident réel, un seul réservoir dont les pompes ont été arrêtées à 2 h 25 aurait été vide vers 8 h 30, soit en six heures environ, au moment de la pointe du matin ; plusieurs réservoirs modifiés en même temps priveraient d'eau ou de pression des quartiers entiers. Le mode manuel existe, mais il faut environ deux heures pour mobiliser une équipe la nuit, et huit agents d'astreinte ne peuvent pas conduire sur place 120 sites : la durée d'interruption tolérable se compte en heures et dépend de la détection. Le retour à la normale (remise en eau, vérification des installations, reprise du pilotage à distance de confiance) prolongerait l'interruption au-delà de l'attaque elle-même.
- **Santé des usagers** : une eau mal traitée (excès ou insuffisance de réactif) peut être distribuée avant toute détection, puisque l'alarme de qualité passe par le système compromis ; les personnes vulnérables (établissement pour personnes âgées dépendantes de la Combe-Martel) sont les plus exposées ; une perte de pression dans les canalisations aggrave le risque sanitaire ; la régie devrait alors restreindre la consommation et fournir de l'eau autrement.
- **Conclusion** : la gravité est maximale (atteinte possible à la santé de milliers d'habitants), et la vraisemblance n'est pas faible (un quart des comptes appartiennent à des personnes parties, accès à distance par simple mot de passe, incident déjà survenu). La supervision est un **système critique** dont la disponibilité et l'intégrité priment ; la régie a besoin d'une détection qui ne dépende pas de la seule supervision et d'un mode manuel préparé.

*2.1 c) – Ce que l'incident révèle* (1 pt)

1. **Une détection fortuite et tardive** : 3 h 30 entre la connexion et la détection, due au hasard (un agent d'astreinte connecté pour une autre alarme), et 3 h 15 après l'arrêt des pompes, que l'attaquant avait masqué en désactivant l'alarme de niveau bas ; la connexion du 4 novembre est passée inaperçue ; les journaux, conservés 30 jours et jamais consultés, ne permettent pas de savoir si le compte a servi avant le 23 octobre. La régie ne surveille pas ses accès : elle découvre les attaques quand elles produisent un effet visible.
2. **Un traitement lent et improvisé** : faute de procédure, l'agent ne coupe pas les accès ; le directeur de l'exploitation attend le lundi ; le compte est désactivé 28 heures après la détection, le responsable de la sécurité des systèmes d'information informé plus de 29 heures après, la directrice générale à midi le lundi, le conseil d'administration 18 jours plus tard ; les neuf autres comptes de prestataires au nom de techniciens partis ne sont désactivés que le 25 novembre et les mots de passe génériques changés le 27. Personne ne sait qui décide ni qui alerte.
3. **Des risques connus mais non traités, faute de propriétaire** : la supervision est hors du champ de la politique de sécurité de 2021 et n'a jamais fait l'objet d'une analyse des risques ; la recommandation d'authentification multifacteur de 2025 n'a pas été suivie « faute de budget et de responsable désigné » ; les comptes ne sont pas revus depuis 2019 ; les contrats n'obligent pas les prestataires à signaler les départs ; la sécurité représente moins de 3 % du budget du SI. Le risque n'a pas été accepté par une décision : il l'a été par défaut.

L'incident n'est donc pas un accident isolé : il révèle une gouvernance de la sécurité absente pour le système le plus critique de la régie.

**Réponses tolérées**
- Typologie en trois catégories (risques réglementaires et métiers regroupés, comme dans l'intitulé du programme), si les six risques sont correctement formulés.
- Risque d'interception ou d'altération des échanges non chiffrés avec les 80 sites reliés par l'opérateur classé en cybermenace ; obsolescence des quatre postes classée en défaillance opérationnelle.
- Dépendance à l'égard des prestataires (savoir-faire détenu par l'éditeur et l'intégrateur) présentée comme un risque métier.
- Analyse d'impact présentée sous forme de tableau (processus, conséquence à 1 heure, 6 heures, 24 heures) ou accompagnée d'une cotation probabilité × gravité, si elle est justifiée par les annexes.
- Constat sur le partage des responsabilités entre l'exploitation et la DSI (« deux mondes ») au titre de la troisième faiblesse.
- Responsabilité de la régie à l'égard des usagers en cas de distribution d'une eau impropre, présentée sans analyse juridique et classée en risque réglementaire ou en risque métier.

**Erreurs fréquentes**
- *Morceau de cours* (`JUR-T01` contextualiser chaque notion) — typologie récitée sans les comptes, les accès à distance ni la Combe-Martel ; juste : chaque risque porte un fait chiffré des annexes.
- *Annexes survolées* (`JUR-T08` exploiter toutes les annexes) — connexion du 4 novembre, durée de conservation des journaux ou désactivation de l'alarme oubliées ; juste : ce sont les faits qui montrent les faiblesses de détection.
- *Statut de NIS 2 affirmé sans date* (`ET-41`) — présenter NIS 2 comme déjà applicable en droit français à la régie, ou trancher son assujettissement ; juste : directive non transposée au 31/12/2026 (annexe 2.3), risque à anticiper.
- *Analyse d'impact confondue avec le plan de continuité* (`ET-02`) — elle mesure les conséquences et fixe les priorités ; le plan organise le maintien de l'activité.
- *Impact réduit au coût de l'incident* (`JUR-T03` analyser et argumenter) — les 25 000 € ne mesurent pas l'enjeu ; juste : santé des usagers et continuité de la distribution.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques du SI, menaces (chaîne d'approvisionnement, compromission de comptes) | classement des risques | F12 § 0 et 5 | notion de cours |
| Analyse d'impact sur l'activité (BIA) | conséquences du scénario, interruption tolérable | F12 § 4 | notion de cours |
| Directive (UE) 2022/2555 (« NIS 2 ») | risque réglementaire à venir, mesures et responsabilité des organes de direction | `nis2` / F12 § 6.1 | en vigueur ; transposition due au 17/10/2024 |
| Transposition française de NIS 2 | statut au 31/12/2026 | `nis2_transposition_fr` / F12 § 6.2 | non transposée au 31/12/2026 |

---

### 2.2 – Démarche et principes de la politique de cybersécurité (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ».

**Annexes mobilisées** : annexes 2.1 (fonctionnement, comptes, politique de 2021, points de vue), 2.2 (incident, scénario redouté) et 2.3 (EBIOS Risk Manager, ISO/IEC 27001:2022, guide d'hygiène, NIS 2).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Politique de sécurité du SI définie (document approuvé par la direction : objectifs de disponibilité, d'intégrité, de confidentialité et de traçabilité, périmètre, principes, organisation, règles, contrôle), distinguée de la charte | 0,5 |
| a-2 | Les cinq ateliers d'EBIOS Risk Manager présentés dans l'ordre, chacun illustré par un élément du cas ; la formalisation, l'approbation, la déclinaison et la revue de la politique sont valorisées mais non exigées ; 0,5 pour trois ateliers illustrés | 1 |
| b | Quatre principes propres à un système critique, chacun justifié par les annexes ; 1 pour trois, 0,5 pour deux | 1,5 |

**Réponse attendue**

*2.2 a) – Définition et démarche*

La **politique de sécurité du système d'information** (PSSI) est le document de référence, approuvé par la direction, qui fixe les **objectifs** de sécurité (disponibilité, intégrité, confidentialité et traçabilité de l'information), le **périmètre**, les **principes**, l'**organisation** (rôles et responsabilités), les **règles** et le **dispositif de contrôle** ; elle se décline en procédures et en une charte opposable aux utilisateurs, qui n'en est qu'une déclinaison (F12 § 1) (0,5 pt). Fondée sur l'analyse des risques, elle proportionne les mesures aux risques réels au lieu d'empiler des règles.

Étapes, en s'appuyant sur EBIOS Risk Manager, méthode de l'ANSSI (annexe 2.3) (1 pt) :

| Étape | Contenu | Application à la supervision |
|---|---|---|
| 1. Cadrage et socle de sécurité | périmètre, missions et biens à protéger, événements redoutés et leur gravité ; écart au socle de règles de base | périmètre : centre de supervision, 120 sites, liaisons, accès à distance, comptes ; missions : produire et distribuer en continu une eau potable, traiter les eaux usées ; événements redoutés : consignes altérées, alarmes neutralisées, perte du pilotage ; écarts au guide d'hygiène de l'ANSSI et aux mesures de l'ISO/IEC 27002:2022 : pas d'authentification multifacteur, comptes génériques, postes obsolètes, réseau non cloisonné |
| 2. Sources de risque | qui pourrait attaquer et dans quel but | ancien technicien ou ancien agent mécontent, cybercriminel cherchant une rançon, attaquant opportuniste qui trouve un accès à distance ouvert sur internet, acteur cherchant à nuire à une infrastructure |
| 3. Scénarios stratégiques | chemins d'attaque par l'écosystème | trois prestataires à accès permanent, opérateur de téléphonie mobile, agents d'astreinte à domicile dont trois sur un ordinateur personnel : chaque tiers est évalué selon son exposition et la confiance qu'on peut lui accorder |
| 4. Scénarios opérationnels | modes opératoires détaillés et vraisemblance | compte de prestataire inactif → accès à distance → arrêt des pompes d'un réservoir et désactivation de son alarme (scénario réalisé en novembre 2026) ; message piégé ouvert sur un poste de bureautique → rebond vers un poste de supervision |
| 5. Traitement du risque | plan de mesures priorisé, risques résiduels | mesures des questions 2.3 et 2.4, échéancées sur l'enveloppe de 200 000 € par an ; risques résiduels acceptés par décision de la direction générale et présentés au conseil d'administration |

Puis la PSSI est **formalisée** en étendant celle de 2021 à la supervision, **approuvée** par la direction générale et présentée au conseil d'administration, **déclinée** en procédures (gestion des accès, gestion d'incident), en charte pour les agents et en exigences de sécurité dans les contrats des prestataires, enfin **revue** chaque année et après chaque incident, dans une logique d'amélioration continue analogue à celle de l'ISO/IEC 27001:2022 (planifier, réaliser, vérifier, ajuster), sans qu'une certification soit visée.

*2.2 b) – Quatre principes propres à un système critique* (1,5 pt)

1. **Priorité à la disponibilité et à l'intégrité du service** : pour la supervision, l'enjeu premier est que l'eau soit distribuée et correctement traitée, avant la confidentialité ; aucune mesure ne doit empêcher une intervention légitime de nuit, comme le redoute M. SALVANHAC ; chaque mesure est conçue avec l'exploitation et prévoit une procédure de secours. Justification : scénario redouté, réservoir vide en six heures.
2. **Cloisonnement et défense en profondeur** : la supervision est isolée de la bureautique, de la messagerie et d'internet, et protégée par plusieurs barrières successives, de sorte qu'une faille unique ne suffise pas. Justification : réseau commun aux 300 postes de bureautique, messagerie et internet sur les postes de supervision, quatre postes obsolètes.
3. **Moindre privilège et imputabilité** : chacun n'a que les droits nécessaires à son rôle, sur un compte nominatif ; toute action est tracée et attribuable ; les actions les plus sensibles (seuils d'alarme, dosage des réactifs, création de comptes) sont réservées à quelques personnes et enregistrées. Justification : 52 comptes sur 60 peuvent modifier les consignes, trois comptes génériques pour environ 45 personnes, compte « admin » partagé avec l'éditeur.
4. **Maîtrise des tiers** (sécurité de la chaîne d'approvisionnement) : un prestataire n'accède à la supervision que sur demande, pour une durée limitée, sous le contrôle de la régie, avec des obligations contractuelles (signalement des départs, règles d'accès, droit de contrôle). Justification : 25 comptes de prestataires dont 10 au nom de techniciens partis, accès ouverts en permanence, incident venu d'un compte de BRÉMONTAL ; NIS 2 range cette sécurité parmi les mesures attendues (annexe 2.3).

**Réponses tolérées**
- Démarche présentée selon les étapes de l'ISO/IEC 27005:2022 (identification, analyse, évaluation, traitement, acceptation des risques) ou selon les six fonctions du NIST Cybersecurity Framework 2.0 (gouverner, identifier, protéger, détecter, répondre, rétablir), si elle part de l'analyse des risques et est appliquée au cas.
- Principe de **détection et de réaction** (surveiller en continu, alerter, savoir qui décide) ou de **responsabilité** (un propriétaire du risque désigné pour la supervision) à la place de l'un des quatre principes.
- Principe d'un **mode dégradé maîtrisé** (conduite manuelle des sites préparée), s'il reste énoncé comme un principe et n'est pas développé en plan de continuité.

**Erreurs fréquentes**
- *PSSI confondue avec la charte informatique* (`ET-27`) — la charte n'en est qu'une déclinaison destinée aux utilisateurs.
- *Norme, méthode et solution confondues* (`JUR-S06` confondre référentiels, normes et solutions ; `ET-01`) — « installer ISO 27001 », EBIOS Risk Manager présenté comme un logiciel ; juste : ISO/IEC 27001:2022 est une norme d'exigences, EBIOS Risk Manager une méthode, le guide d'hygiène un guide.
- *Objectifs de sécurité oubliés* (`JUR-S01` triade CID) — la politique doit dire ce qu'elle protège : disponibilité et intégrité d'abord, pour la supervision.
- *Principes génériques* (`JUR-T01`) — « sensibiliser le personnel » sans lien avec la supervision ; juste : principes propres à un système qui pilote des installations.
- *Démarche de certification proposée* — hors programme et hors de la demande ; juste : la norme sert de référence.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| EBIOS Risk Manager (ANSSI, version 1.5 de 2024) | cinq ateliers appliqués à la supervision | `ebios_rm_1_5` / F12 § 2 | en vigueur |
| ISO/IEC 27005:2022 | gestion des risques (réponse tolérée) | `iso_27005_2022` / F12 § 2 | en vigueur |
| ISO/IEC 27001:2022 et ISO/IEC 27002:2022 | amélioration continue, mesures de référence | `iso_27001_2022`, `iso_27002_2022` / F12 § 2 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI (2017) | socle de mesures de base | `guide_hygiene_anssi_2017` / F12 § 2 | en vigueur |
| NIST Cybersecurity Framework 2.0 (2024) | six fonctions (réponse tolérée) | `nist_csf_2_0` / F12 § 2 | en vigueur |
| PSSI, triade CID et traçabilité | définition et objectifs | F12 § 1 | notion de cours |

---

### 2.3 – Architecture de confiance (2 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) ».

**Annexes mobilisées** : annexes 2.1 (liaisons, réseau, accès à distance, authentification, points de vue) et 2.3 (modèle Zero Trust).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Modèle Zero Trust présenté comme un modèle d'architecture (aucune confiance implicite, vérification de chaque accès selon l'identité, le terminal et le contexte, démarche progressive), et non comme un produit, et appliqué à la régie (fin de la confiance accordée au réseau commun et aux accès à distance ouverts) | 0,5 |
| 2 | Mesure d'authentification, rattachée à son constat, avec une condition de réussite | 0,5 |
| 3 | Mesure de chiffrement, rattachée à son constat, avec une condition de réussite | 0,5 |
| 4 | Mesure de segmentation entre la bureautique et la supervision, rattachée à son constat, avec une condition de réussite | 0,5 |

**Réponse attendue**

Le **modèle Zero Trust** est un modèle d'architecture fondé sur le principe « ne jamais faire confiance par défaut, toujours vérifier » : aucune confiance n'est accordée à un utilisateur ou à un terminal du seul fait qu'il est connecté au réseau de la régie ; chaque accès à une ressource est authentifié, autorisé et évalué selon le contexte (identité, état du terminal, sensibilité de la ressource, horaire), avec le moindre privilège et une surveillance continue. Ce n'est ni un produit ni un logiciel que l'on achète : c'est une démarche progressive de transformation, qui ne remplace pas la défense en profondeur (avis de l'ANSSI, annexe 2.3). À la régie, il conduit à ne plus considérer comme sûr un poste du simple fait qu'il est sur le réseau commun, et à vérifier chaque connexion à la supervision (0,5 pt).

| Mesure | Constat de l'annexe 2.1 | Condition de réussite |
|---|---|---|
| **Authentification multifacteur** pour tous les accès à distance (agents d'astreinte, prestataires) et pour les comptes d'administration, sur des comptes nominatifs ; accès à distance depuis des terminaux fournis et gérés par la régie (fin des ordinateurs personnels) ; accès d'un prestataire autorisé seulement pendant une intervention demandée (0,5 pt) | identifiant et mot de passe pour tous les comptes ; accès à distance joignable depuis internet ; recommandation de 2025 non suivie ; trois agents d'astreinte sur leur ordinateur personnel ; incident venu d'un mot de passe obtenu on ne sait comment | être utilisable à 3 heures du matin : facteur de possession remis à chaque agent d'astreinte, procédure de secours en cas de perte, essai avec l'exploitation avant généralisation (point de vue de M. SALVANHAC) ; mêmes exigences imposées aux prestataires par contrat |
| **Chiffrement** des échanges entre le centre de supervision et les sites, en priorité les 80 sites reliés par l'opérateur de téléphonie mobile, et des sessions d'accès à distance (0,5 pt) | échanges entre le centre et les sites non chiffrés ; 80 sites reliés par un réseau extérieur | le chiffrement protège surtout l'**intégrité** et l'authenticité des consignes (une consigne ne doit pas pouvoir être modifiée en chemin) ; il suppose de vérifier avec BRÉMONTAL la compatibilité des automates, de commencer par les sites les plus critiques (usines, grands réservoirs) et d'organiser la gestion des clés |
| **Segmentation** : zone réservée à la supervision, séparée de la bureautique ; aucun accès à la messagerie ni à internet depuis les postes de supervision ; tous les flux interdits sauf ceux qui sont explicitement autorisés ; accès à distance par un point d'entrée unique, contrôlé et journalisé ; découpage plus fin par type de site pour limiter les mouvements latéraux (0,5 pt) | réseau commun aux 300 postes de bureautique et aux six postes de supervision, sans cloisonnement ; messagerie et internet sur les postes de supervision ; « deux mondes qui partagent les mêmes câbles » | inventaire préalable des échanges légitimes, conduit ensemble par la DSI et l'exploitation ; remplacement ou isolement des quatre postes sans mises à jour, qui resteraient le maillon faible ; règle de gestion des exceptions validée par le responsable de la sécurité des systèmes d'information |

**Réponses tolérées**
- Gestion des terminaux mobiles (MDM, *Mobile Device Management*) des ordinateurs portables d'astreinte au titre de l'authentification ou d'une condition de réussite.
- Accès conditionnel (refus d'une connexion de prestataire hors d'une fenêtre d'intervention, ou depuis un terminal non conforme) présenté comme application du Zero Trust.
- Mesure de segmentation qui prévoit une passerelle unique d'échange entre la supervision et la bureautique pour les rares données qui doivent circuler (rapports d'exploitation).

**Erreurs fréquentes**
- *Zero Trust présenté comme un produit* (`JUR-S03` Zero Trust cadre architectural et non solution logicielle ; `ET-04`) — « acheter le Zero Trust d'un éditeur » ; juste : modèle et démarche progressive.
- *Authentification multifacteur confondue avec un mot de passe complexe* (`ET-28`) — juste : au moins deux facteurs de nature différente.
- *Micro-segmentation confondue avec une segmentation applicative* (`ET-14`) — juste : cloisonnement des flux entre zones pour limiter les mouvements latéraux.
- *Réponse technique* (`JUR-T12` moins de technique, plus de management) — description du réglage des équipements de sécurité, ligne par ligne : hors programme ; juste : mesure, constat, condition.
- *Mesure sans condition de réussite* (`JUR-T03`) — une authentification forte qui bloque l'astreinte serait contournée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Le modèle Zero Trust (avis de l'ANSSI, 2021) | définition, démarche progressive | `zero_trust_anssi` / F12 § 3 | en vigueur |
| Authentification multifacteur, segmentation, micro-segmentation, chiffrement | trois mesures | F12 § 3 | notion de cours |
| Directive (UE) 2022/2555 (« NIS 2 ») | chiffrement et authentification multifacteur parmi les mesures | `nis2` / F12 § 6.1 | en vigueur ; non transposée en France au 31/12/2026 |

---

### 2.4 – Gestion des identités et surveillance des connexions (2 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ».

**Annexes mobilisées** : annexes 2.1 (inventaire des comptes, accès à distance, journaux, organisation) et 2.2 (chronologie, constats).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Quatre règles de gestion des identités et des accès (cycle de vie, comptes génériques, comptes à privilèges, revue périodique), applicables aux agents et aux prestataires, chacune rattachée à un constat de l'inventaire ; 0,5 pour deux règles | 1 |
| b-1 | Dispositif de surveillance : journaux centralisés et conservés plus longtemps, règles d'alerte propres à la supervision, traitement des alertes à toute heure, revue des connexions des prestataires | 0,5 |
| b-2 | Deux indicateurs d'efficacité complets (formule, source, fréquence, cible, axe) ; 0 si un seul indicateur est complet | 0,5 |

**Réponse attendue**

*2.4 a) – Quatre règles de gestion des identités et des accès* (1 pt)

La gestion des identités et des accès (IAM) organise, pour chaque personne, l'attribution, l'évolution et le retrait des droits sur tout le cycle de vie, selon son rôle et le principe du moindre privilège (F12 § 3 ; F10 § 3.1). Le directeur de l'exploitation, propriétaire de la supervision, décide des droits ; la DSI les met en œuvre ; le responsable de la sécurité des systèmes d'information contrôle.

1. **Cycle de vie des comptes** : tout compte est créé sur demande validée, rattaché à une personne et à un rôle, modifié à chaque mutation et désactivé le jour du départ. Pour les agents, la direction des ressources humaines signale chaque arrivée, mutation et départ ; pour les prestataires, le contrat oblige à signaler le départ d'un technicien sous 24 heures, et les comptes expirent d'eux-mêmes à la fin du contrat ou après une période sans usage. Constat : 15 comptes (un quart) appartiennent à des personnes parties ; le compte utilisé le 22 novembre était actif depuis près de cinq mois après le départ du technicien.
2. **Comptes génériques** : suppression des trois comptes « exploitation », « astreinte » et « maintenance » au profit d'un compte nominatif pour chacune des quelque 45 personnes ; toute exception (poste de consultation du centre) est limitée à la lecture et justifiée. Constat : aucune action n'est attribuable ; mots de passe inchangés de 2019 à novembre 2026.
3. **Comptes à privilèges** : les quatre comptes d'administration deviennent nominatifs, distincts du compte quotidien, protégés par une authentification multifacteur et utilisés par le point d'entrée contrôlé, avec enregistrement des sessions ; suppression du compte « admin » partagé avec l'éditeur ; les prestataires n'obtiennent des droits que sur demande, pour la durée de l'intervention, après validation par l'exploitation ; les droits de modification des consignes sont réservés aux rôles qui en ont besoin (opérateurs, astreinte), les autres en consultation. Constat : 52 comptes sur 60 peuvent modifier les consignes.
4. **Revue périodique des droits** : revue semestrielle des 60 comptes par le directeur de l'exploitation, la liste des comptes de chaque prestataire étant confirmée par celui-ci, sous le contrôle du responsable de la sécurité des systèmes d'information ; tout compte non confirmé est désactivé ; revue supplémentaire après chaque incident. Constat : aucune revue des comptes de prestataires depuis 2019.

*2.4 b) – Surveillance des connexions et indicateurs*

**Dispositif** (0,5 pt) :
- **Journalisation** : les journaux de la supervision, de l'accès à distance et des comptes d'administration sont centralisés hors de la supervision et conservés au moins un an, pour reconstituer un incident (30 jours aujourd'hui, ce qui interdit de savoir si le compte a servi avant le 23 octobre).
- **Règles d'alerte** propres à la supervision : connexion d'un prestataire sans demande d'intervention ouverte ; connexion de nuit d'un compte qui n'est pas d'astreinte ; modification d'une consigne ou désactivation d'une alarme hors des heures d'exploitation ; échecs répétés de connexion ; connexion d'un compte inactif depuis plusieurs semaines. L'incident du 22 novembre aurait déclenché au moins trois de ces alertes.
- **Traitement des alertes à toute heure** : le responsable de la sécurité des systèmes d'information, à mi-temps, ne peut pas veiller seul ; la régie confie la surveillance à un centre opérationnel de sécurité (SOC) externe ou mutualisé, appuyé sur un outil de collecte et de corrélation des journaux (SIEM), qui alerte l'agent d'astreinte et le responsable de la sécurité selon une procédure d'escalade (qui coupe les accès, qui prévient la directrice générale) ; les alarmes critiques de qualité de l'eau sont doublées par une voie qui ne dépend pas de la supervision.
- **Revue hebdomadaire** par l'exploitation de la liste des connexions de prestataires, rapprochée des interventions demandées.

**Indicateurs d'efficacité** (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Délai de détection d'une connexion anormale | moyenne, sur les connexions anormales du mois, de (heure de prise en charge de l'alerte − heure de la connexion) | journaux centralisés et registre des alertes du centre opérationnel de sécurité | mensuelle | moins de 15 minutes (3 h 30, et par hasard, en novembre 2026) | processus |
| Taux de connexions de prestataires autorisées | connexions de prestataires rattachées à une demande d'intervention validée / connexions de prestataires | journaux de l'accès à distance et registre des demandes d'intervention | mensuelle | 100 % (accès aujourd'hui ouverts en permanence, sans demande) | processus |

**Réponses tolérées**
- Rôles (RBAC) définis par métier (opérateur, agent d'astreinte, automaticien, prestataire) en guise de règle sur le cycle de vie ou sur les privilèges.
- Revue trimestrielle des comptes de prestataires et semestrielle des comptes d'agents.
- Indicateur « taux de comptes désactivés dans les 24 heures suivant le départ » (comptes désactivés dans les 24 heures suivant le départ de la personne (ou son signalement par le prestataire) / départs du mois ; source : signalements de la direction des ressources humaines et des prestataires, inventaire des comptes ; mensuelle ; cible 100 % ; axe processus) ou « part des comptes nominatifs » (comptes nominatifs / comptes actifs de la supervision ; source : inventaire des comptes ; trimestrielle ; cible 100 % fin 2027 ; axe processus), s'il est relié au dispositif de surveillance ou de gestion des accès.
- Analyse comportementale des connexions, éventuellement appuyée sur l'intelligence artificielle, pour repérer les écarts aux habitudes d'un compte, avec ses limites (faux positifs, réglage initial).
- Indicateur rattaché à l'axe « apprentissage » ou à l'axe ESG « gouvernance », si le choix est justifié.

**Erreurs fréquentes**
- *Plan de continuité ou de reprise développé à la place de la surveillance* (`ET-02` PCA et PRA ; `JUR-S02`) — la question porte sur l'IAM et la détection ; le PCA et le PRA ne sont pas demandés.
- *Identification, authentification et autorisation confondues* (`ET-28`) — un compte nominatif identifie, l'authentification multifacteur prouve l'identité, la revue des droits règle l'autorisation.
- *IAM réduit à un outil* (`JUR-S05` mesures opérationnelles cohérentes) — l'IAM est d'abord un processus (demande, validation, retrait, revue) avec des responsables.
- *Indicateurs incomplets ou génériques* (`ET-18`) — « nombre d'incidents » sans formule, source ni cible ; juste : cinq champs, point de départ de l'annexe.
- *Surveillance confiée au seul responsable de la sécurité à mi-temps* (`JUR-T03`) — l'incident a eu lieu un samedi à 2 heures du matin.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| IAM : cycle de vie, rôles, comptes à privilèges, revues ; SIEM et SOC en principe | quatre règles, dispositif de surveillance | F12 § 0 et 3 ; glossaire (SIEM) | notion de cours |
| Habilitations, moindre privilège, revue semestrielle des droits | revue périodique | F10 § 3.1 | notion de cours |
| Indicateurs d'efficacité des mesures (délai de détection, délai de révocation des droits) | deux indicateurs | F12 § 3 | notion de cours |
| IA défensive : analyse comportementale (réponse tolérée) | surveillance | F13 ; F12 § 0 | notion de cours |

---

### 2.5 – Gouvernance de la sécurité de la supervision (2 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques » ; `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ».

**Annexes mobilisées** : annexes 1.1 (organigramme), 2.1 (organisation de la sécurité, points de vue), 2.2 (chronologie de l'information des acteurs) et 2.3 (NIS 2 : responsabilité des organes de direction).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Intérêt de la matrice précisé (qui réalise, qui approuve — un seul par activité —, qui est consulté, qui est informé ; éviter les vides et les doublons de responsabilité) et matrice cohérente pour les quatre activités et les six acteurs ; 0,5 pour deux activités correctement réparties | 1 |
| b | Deux évolutions de l'organisation justifiées par les annexes, dont le positionnement du responsable de la sécurité des systèmes d'information ; 0,5 par évolution | 1 |

**Réponse attendue**

*2.5 a) – Matrice de responsabilités* (1 pt)

Une **matrice de responsabilités** (RACI) indique, pour chaque activité, qui la **réalise** (R), qui l'**approuve** et en répond (A, un seul par activité), qui est **consulté** avant la décision (C) et qui est **informé** après (I) (F05 § 1 ; F02 § 0). Elle répond au défaut que révèle l'incident : personne ne savait qui décidait de couper les accès ni qui informait la direction (annexe 2.2), et la supervision n'était sous la responsabilité de sécurité de personne.

| Activité | Conseil d'administration | Directrice générale | Responsable de la sécurité des SI | Directeur de l'exploitation | Responsable de la DSI | Prestataires |
|---|---|---|---|---|---|---|
| Approbation de la politique de sécurité de la supervision | **A** (approuve les orientations et le niveau de risque accepté, suit leur mise en œuvre) | R (porte la politique et arbitre les moyens) | R (élabore) | C | C | I |
| Analyse des risques de la supervision | I | **A** (accepte les risques résiduels) | R (pilote la méthode) | R (missions, événements redoutés, scénarios) | C | C (écosystème, scénarios) |
| Gestion des accès des prestataires | — | I | C (fixe les règles, contrôle la revue) | **A** (valide chaque ouverture d'accès) | R (crée, ouvre, ferme, désactive) | R (demandent les accès, signalent les départs) |
| Traitement d'un incident | I (sans délai si l'incident est grave) | **A** (dirige la cellule de crise, décide de la communication) | R (coordonne la réponse, qualifie l'incident) | R (protège les installations, passe en mode manuel) | R (coupe les accès, conserve les traces) | C (investigation, correction) |

*2.5 b) – Deux évolutions de l'organisation* (1 pt)

1. **Repositionner le responsable de la sécurité des systèmes d'information** : le rattacher à la directrice générale et non plus à la DSI, étendre sa mission à la supervision (droit de regard, accès aux journaux, contrôle des comptes) et en faire une fonction à temps plein, au besoin appuyée par un prestataire. Justification : à mi-temps et rattaché à la DSI dont il gère aussi les infrastructures, il est juge et partie ; il n'a « aucun droit de regard » sur le système le plus critique et a été informé plus de 29 heures après la détection. L'enveloppe de 200 000 € par an permet de financer ce temps et la surveillance externe.
2. **Installer une gouvernance de la sécurité au niveau de la direction et du conseil** : un comité de sécurité trimestriel (directrice générale, responsable de la sécurité, directeur de l'exploitation, responsable de la DSI, directrice des ressources humaines pour le cycle de vie des comptes) qui suit le plan de traitement et les indicateurs ; un examen annuel de la sécurité par le conseil d'administration, une information sans délai en cas d'incident grave (au lieu de 18 jours) et une formation des administrateurs, en anticipation de la responsabilité que NIS 2 donne aux organes de direction, sans préjuger de son application à la régie (annexe 2.3). Justification : avant décembre 2026, le conseil n'avait jamais examiné la sécurité ; Mme ROCHEVAL veut dire « qui en répond et dans quels délais ».

**Réponses tolérées**
- Directrice générale en A pour l'approbation de la politique, le conseil d'administration étant informé et approuvant les orientations et l'enveloppe, si le choix est justifié.
- Directeur de l'exploitation en A pour l'analyse des risques, comme propriétaire de la supervision, la directrice générale arbitrant les risques résiduels les plus graves.
- Évolution portant sur la désignation du directeur de l'exploitation comme **propriétaire du risque** de la supervision, avec un correspondant sécurité parmi les automaticiens, ou sur l'ajout de clauses de sécurité dans les contrats des trois prestataires (signalement des départs, accès sur demande, droit de contrôle), sans analyse juridique des contrats.
- Matrice présentée avec les activités en colonnes et les acteurs en lignes.

**Erreurs fréquentes**
- *Responsable de la sécurité vu comme un technicien ou maintenu sous la DSI sans indépendance* (`ET-15`) — juste : il pilote la politique et contrôle, y compris la DSI.
- *Deux « A » sur une même activité* — la matrice perd son intérêt : une seule personne approuve et répond.
- *Prestataires absents de la matrice* (`JUR-T08`) — alors que l'incident vient d'un compte de prestataire.
- *Conseil d'administration chargé de réaliser* — il approuve et contrôle, il n'exécute pas.
- *Recommandations irréalistes* (`JUR-G05` déséquilibres organisationnels et recommandations réalistes) — créer une direction de la sécurité de dix personnes pour une DSI de 14 agents ; juste : temps plein, rattachement, appui externe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Matrice RACI | répartition des rôles | F05 § 1 ; F02 § 0 ; glossaire | notion de cours |
| Rôles du responsable de la sécurité des SI, de la direction, des prestataires | positionnement, indépendance | F12 § 1 | notion de cours |
| Directive (UE) 2022/2555 (« NIS 2 ») | responsabilité et formation des organes de direction, en anticipation | `nis2` / F12 § 6.1 | en vigueur ; transposition due au 17/10/2024 |
| Transposition française de NIS 2 | statut au 31/12/2026 | `nis2_transposition_fr` / F12 § 6.2 | non transposée au 31/12/2026 |
