# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 54 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 audit et fiabilisation, F12 sécurité et résilience, F14 numérique responsable, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les conclusions de l'audit de la base des points d'eau d'incendie | `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse | 3 |
| 3.2 Les risques du logiciel de traitement de l'alerte | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. | 3 |
| 3.3 La sécurité des tablettes et la gouvernance du traitement de l'alerte | `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 4 |
| 3.4 Les salles informatiques et la transition numérique responsable | `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 3 |
| **Dossier 3 – Tirer les conclusions d'un audit, maîtriser les risques et la sécurité du système d'information opérationnel et en réduire l'empreinte** |  | **13** |

Répartition indicative : connaissances (critère d'appréciation, typologie des risques, ISO/IEC 27005 et EBIOS Risk Manager, architecture de confiance, transition numérique responsable) environ 3 points (items 3.1 b-1, 3.2 a-1, 3.2 b-1, 3.3 a-1, 3.3 b-1 et 3.4 a-1, chacun en partie appliqué au cas) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – Les conclusions de l'audit de la base des points d'eau d'incendie (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la mission est terminée, ni son cadrage ni sa démarche ne sont demandés ; l'organisation des contrôles des points d'eau est donnée par l'annexe, et aucune règle de droit n'est à connaître.

**Annexes mobilisées** : annexe 3.1 (base, organisation fixée par le SDIS, neuf notes brutes, réactions, demande du directeur) et annexe 1.1 (base des points d'eau et système d'information géographique, logiciel de traitement de l'alerte, 60 centres dont 48 armés par des volontaires seulement, Haut-Aurande).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Note adressée au directeur, tournée vers la décision, bornée à 20 lignes ; appréciation d'ensemble nette (base non fiable, risque opérationnel direct) | 0,5 |
| a-2 | Quatre constats regroupés à partir des notes brutes et hiérarchisés de façon justifiée : la carte de l'alerte et le circuit des indisponibilités en premier, au vu de l'incendie du 12/08/2026 | 0,5 |
| a-3 | Pour chaque constat, le risque et une recommandation concrète, avec un responsable et une échéance réalistes | 0,5 |
| a-4 | Réponse à l'objection du lieutenant-colonel OSSELIN ; suivi du plan d'action | 0,5 |
| b-1 | Critère d'appréciation défini ; fiabilité des données, sécurité et efficacité du processus définies et appliquées à la base et à sa mise à jour | 0,5 |
| b-2 | Deux constats justement rattachés à chacun des trois critères | 0,5 |

**Réponse attendue**

*3.1 a) – La note de synthèse*

La note de synthèse d'audit s'adresse à un décideur : elle tient en une page, donne une appréciation d'ensemble, ne retient que les constats qui appellent une décision, les **hiérarchise**, et assortit chacun du risque, de la recommandation, du responsable et de l'échéance (F10 § 1.2 et § 5). Elle ne recopie pas les notes brutes : elle les **regroupe**.

Regroupement attendu des neuf notes brutes de l'annexe 3.1 B :
- **la carte de l'alerte ne reflète pas l'état réel des points d'eau** : indisponibilités signalées à des interlocuteurs différents et saisies en 12 jours en moyenne, chargement mensuel à la main sans contrôle, chargement de septembre 2026 échoué sans que personne le voie, 600 écarts dont 150 points indisponibles affichés disponibles, incendie du 12/08/2026 ;
- **la base n'est ni protégée ni tracée** : 1 200 comptes ont le droit de la modifier, aucun historique, sauvegarde jamais restaurée et gardée dans la salle où se trouve le serveur ;
- **les données sont périmées ou inexactes** : 3 500 points, un sur quatre, sans contrôle depuis plus de deux ans ; un point sur dix mal placé dans le Haut-Aurande ;
- **la collecte des contrôles est artisanale** : tableurs de formats différents envoyés par 480 communes et 6 gestionnaires, ressaisis par trois agents, 1 500 résultats, un sur quatre, en attente.

Hiérarchie : la **carte de l'alerte** vient en priorité 1, car c'est elle que suivent les équipages et l'incendie du 12/08/2026 montre que le risque s'est déjà réalisé. La **sécurité de la base** vient aussi en priorité 1 : une modification erronée ou malveillante d'un point d'eau serait invisible, et la base peut être perdue avec la salle. Les **données périmées** et la **collecte** viennent en priorité 2 : elles demandent plusieurs mois de rattrapage et un changement de processus, et la note leur donne une échéance plus lointaine.

Note modèle (environ 20 lignes, à la borne) :

<!-- note -->
**Au colonel hors classe GRANVOISE – Audit de la base des points d'eau (comité de direction du 07/06/2027)**
**Appréciation d'ensemble** : base non fiable ; la carte de l'alerte peut envoyer un engin vers un point d'eau hors service.
**1. Carte de l'alerte en retard (priorité 1).** Indisponibilités saisies en 12 jours, carte rechargée chaque mois sans contrôle ; 150 points hors service affichés disponibles. Risque : alimentation en eau retardée. Recommandation : tout signalement adressé au centre de traitement de l'alerte et saisi le jour même ; chargement hebdomadaire contrôlé, puis liaison automatique. Lt-col OSSELIN, Mme VARANGEOT : 30/06/2027.
**2. Base ouverte et sans trace (priorité 1).** 1 200 comptes peuvent la modifier ; aucun historique ; sauvegarde jamais restaurée, gardée sur place. Risque : erreur ou malveillance invisible, base perdue. Recommandation : droits réservés à la cellule cartographie, journal des modifications, copie hors du siège et restauration essayée. Mme VARANGEOT, 30/09/2027.
**3. Données périmées (priorité 2).** 3 500 points sans contrôle depuis deux ans ; un point sur dix mal placé dans le Haut-Aurande. Risque : point d'eau à sec ou introuvable. Recommandation : rattrapage, d'abord dans le Haut-Aurande. Lt-col OSSELIN et chefs de centre, 30/06/2028.
**4. Collecte artisanale (priorité 2).** Tableurs de formats différents, ressaisis par trois agents ; 1 500 en attente. Risque : retards et erreurs durables. Recommandation : modèle unique, puis saisie directe par les communes et les gestionnaires. Lt-col OSSELIN, 2028.
**Objection** : connaître son secteur ne dit pas qu'un poteau est hors service ; le 12/08/2026, l'engin a suivi la carte. La collecte simplifiée (4) soulage les trois agents.
**Suivi** : point trimestriel, audit de suivi en 2028.
<!-- /note -->

**Réponse à l'objection du lieutenant-colonel OSSELIN** (a-4) :
- l'état d'un point d'eau change (poteau en panne, citerne vide, travaux) et ne s'apprend pas par l'expérience du secteur : le 12/08/2026, l'engin a suivi la carte vers un poteau hors service depuis trois semaines. La carte sert aussi aux opérateurs du centre de traitement de l'alerte, qui ne connaissent pas chaque secteur ;
- c'est la ressaisie de 6 000 résultats en tableurs qui absorbe les trois agents de la cellule : le modèle unique et la saisie directe par les communes et les gestionnaires libèrent leur temps, et le rattrapage commence par le Haut-Aurande pour tenir compte de leurs moyens.

La liaison automatique entre la base et le logiciel de l'alerte n'a pas d'échéance ferme : le calendrier de l'éditeur est chargé (réaction de Mme VARANGEOT), deux développeurs seulement connaissent les interfaces et la version actuelle n'est plus maintenue après 2029 (annexe 3.2). Elle est inscrite dans les besoins de la suite du logiciel, ou demandée à l'éditeur avec la documentation des interfaces ; le chargement hebdomadaire contrôlé, dès le 30/06/2027, tient lieu de mesure immédiate.

*3.1 b) – Les trois critères d'appréciation*

**Définition** (b-1) : un **critère d'appréciation** est la référence (objectif, exigence, règle interne, norme) au regard de laquelle l'auditeur compare la situation constatée et qualifie un écart. Il rend le jugement de l'audit explicite, vérifiable et discutable par les audités ; en audit des systèmes d'information, les critères usuels portent sur la fiabilité, l'efficacité et l'efficience, la sécurité et la conformité (F10 § 1.1). Ici, la référence est l'organisation fixée par le SDIS (contrôle tous les deux ans, signalement immédiat des indisponibilités) et le besoin opérationnel : une carte juste au moment de l'alerte.

| Critère | Ce qui est attendu de la base et de sa mise à jour | Deux constats de l'annexe 3.1 (b-2) |
|---|---|---|
| **Fiabilité des données** | les données sont exactes, complètes, à jour et cohérentes entre la base et la carte de l'alerte | 3 500 points sans contrôle depuis plus de deux ans ; 600 écarts entre la base et la carte, dont 150 points indisponibles affichés disponibles ; un point sur dix placé à plus de 100 mètres de sa position |
| **Sécurité** | seules les personnes autorisées modifient la base (intégrité), chaque modification est imputable (traçabilité), la base peut être restaurée après un sinistre (disponibilité) | 1 200 comptes ont le droit de modifier ; aucune trace des modifications ; sauvegarde jamais restaurée, dans la même salle que le serveur |
| **Efficacité du processus** | le processus atteint son objectif, une carte à jour au moment de l'alerte, dans des délais courts et avec des moyens raisonnables | indisponibilités saisies en 12 jours, puis attente du chargement mensuel ; 6 000 résultats reçus en tableurs de formats différents et ressaisis un par un, 1 500 en attente ; chargement manuel sans contrôle, échec de septembre 2026 inaperçu |

**Réponses tolérées**
- Note présentée en tableau (constat, risque, recommandation, responsable, priorité, échéance), si elle tient dans les 20 lignes et commence par une appréciation d'ensemble.
- Trois ou cinq regroupements au lieu de quatre, si chacun rassemble plusieurs notes brutes et si la carte de l'alerte vient en tête ; sécurité de la base en priorité 2, si la priorité 1 donnée à la carte est justifiée par l'incendie.
- Autres responsables plausibles : chef du groupement des opérations seul propriétaire de la base, service des systèmes d'information et de communication pour l'outil, cheffe du centre de traitement de l'alerte pour le circuit des signalements ; échéances différentes si elles sont datées et cohérentes avec la priorité.
- Réponse à l'objection placée en conclusion de la note, ou intégrée au premier constat ; liaison automatique fixée à la fin de 2027, si un chargement contrôlé la précède.
- Efficience à la place de l'efficacité pour la ressaisie, ou critère de conformité à l'organisation fixée par le SDIS ajouté, si les trois critères demandés sont traités ; un constat rattaché à deux critères (l'échec du chargement de septembre relève de la fiabilité et de l'efficacité), si c'est justifié.

**Erreurs fréquentes**
- *Note qui dépasse 20 lignes, recopie les notes brutes dans leur ordre, ou omet le responsable et l'échéance* (`JUR-T07`, `JUR-T04`) — juste : quatre constats regroupés, hiérarchisés, chacun avec son risque, sa recommandation, son responsable et son échéance.
- *Constats sans conséquence opérationnelle* (`JUR-T03`) — juste : le risque d'un point d'eau faux est un retard de l'alimentation en eau sur un feu, déjà constaté.
- *Critères récités sans être reliés aux constats* (`JUR-T01`) — juste : ce qui est attendu de la base, puis deux constats par critère.
- *Démarche ou méthodologie de l'audit exposée* — non demandée : la mission est terminée.
- *Règles de droit sur les points d'eau, répartition légale des contrôles entre le SDIS et les communes* — non attendues : l'organisation est donnée par l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Note de synthèse d'audit | appréciation d'ensemble, constats hiérarchisés, recommandation, responsable, échéance | F10 § 1.2 et § 5 | notion de cours |
| Critères d'audit du SI | fiabilité, efficacité, sécurité, conformité | F10 § 0 et § 1.1 | notion de cours |

---

### 3.2 – Les risques du logiciel de traitement de l'alerte (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; ISO/IEC 27005 et EBIOS Risk Manager sont présentées en principe, sans conduire les ateliers ; aucune analyse d'impact détaillée d'une panne, aucune procédure de choix d'un nouvel éditeur, aucun chiffrage.

**Annexes mobilisées** : annexe 3.2 (logiciel, éditeur, contrat, serveurs, pannes de 2026, échelles), annexe 3.3 (réseau commun, rançongiciel du SDIS voisin), annexe 3.5 (ISO/IEC 27005:2022, EBIOS Risk Manager, guide d'hygiène, RGPD) et annexe 1.1 (logiciel installé en 2012, petit éditeur spécialisé, salle de secours de Montcerneau-Sud, 150 000 appels).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers, dont la dépendance envers un fournisseur) ; risques formulés comme des événements redoutés | 0,5 |
| a-2 | Quatre risques tirés de l'annexe 3.2, chacun avec sa cause et ses chiffres, et classés | 0,5 |
| a-3 | Probabilité et impact cotés de façon justifiée selon les échelles de l'annexe 3.2 C ; les deux risques de niveau 3 × 3 dégagés | 0,5 |
| b-1 | ISO/IEC 27005 (lignes directrices, processus générique, sans méthode imposée) et EBIOS Risk Manager (méthode en cinq ateliers, sources de risque et écosystème) comparées ; choix justifié par le cas, avec sa limite | 0,5 |
| c-1 | Traitement de la fin de maintenance sans solution prête, justifié par la probabilité et l'impact (réduire, ou éviter défini comme l'abandon de la version avant la fin de sa maintenance, justifié ; accepter et transférer écartés) | 0,5 |
| c-2 | Traitement du rançongiciel, justifié (réduire ; transfert discuté et jugé partiel) | 0,5 |

**Réponse attendue**

*3.2 a) – Quatre risques, leur classement et leur cotation*

**Typologie** (a-1) : les risques liés aux systèmes d'information se classent en **cybermenaces** (rançongiciel, hameçonnage, attaque par la chaîne d'approvisionnement, c'est-à-dire par un éditeur ou un prestataire), **défaillances opérationnelles** non intentionnelles (panne, erreur, correctif défectueux), **risques réglementaires** (manquement à une obligation, par exemple la sécurité des données personnelles) et **risques métiers**, qui touchent la mission ou la stratégie, dont la **dépendance envers un fournisseur** (F12 § 0 et § 5). Un risque se formule comme un **événement redouté**, avec sa cause et sa conséquence ; ici, le critère dominant est la **disponibilité** du traitement de l'alerte, mission que le projet d'établissement veut garantir jour et nuit.

**Risques, classement et cotation** (a-2 et a-3 ; quatre sont attendus, cinq sont proposés) :

| Risque (événement redouté) et cause | Nature | Probabilité | Impact |
|---|---|---|---|
| R1 – **Au 01/01/2030, le SDIS exploite un logiciel que l'éditeur ne maintient plus**, sans solution de remplacement en service : plus aucun correctif, fonctionnel ou de sécurité. Causes : fin de maintenance annoncée au 31/12/2029 ; nouvelle version reportée « à partir de 2029 » et utilisée par aucun SDIS ; moins de trois ans pour préparer un changement de logiciel critique | risque métier, dépendance envers l'éditeur | **3** : certain à une date connue si rien n'est fait | **3** : toute panne ou faille deviendrait impossible à corriger, donc impossible à rétablir rapidement |
| R2 – **Un rançongiciel chiffre les serveurs du traitement de l'alerte dans les deux salles.** Causes : système d'exploitation sans correctifs de sécurité depuis 2025 ; serveurs sur le même réseau que la bureautique et les tablettes ; accès de l'éditeur ouvert en permanence avec un compte commun | cybermenace, par la bureautique ou par l'éditeur ; volet réglementaire : violation de données personnelles des appelants (annexe 3.5) | **3** : facile à provoquer en l'état ; scénario réalisé chez le SDIS voisin en février 2027 | **3** : réception des appels et engagement des secours arrêtés dans les deux salles ; une journée chez le voisin |
| R3 – **Une anomalie du logiciel, installée dans les deux salles, bloque une fonction essentielle, et l'éditeur ne peut la corriger vite.** Causes : correctif installé le même soir dans les deux salles ; deux développeurs seulement connaissent les interfaces, dont un part en 2028 ; aucune documentation | défaillance opérationnelle ; dépendance envers les compétences de l'éditeur | **3** : constaté en novembre 2026 | **2** : 2 heures de choix des engins à la main, sans arrêt de la réception des appels ; il deviendrait de niveau 3 si l'éditeur ne pouvait plus corriger |
| R4 – **Les serveurs du siège s'arrêtent** (climatisation de 2008, matériels de 2017) **et la bascule est lente** | défaillance opérationnelle | **3** : constaté en juillet 2026 | **2** : bascule en 45 minutes, une trentaine d'appels sur papier |
| R5 – **L'éditeur cesse son activité ou abandonne le logiciel**, sans remise du code source ni aide à la sortie | risque métier, dépendance envers l'éditeur | **2** : société de 40 salariés dont le SDIS est un des trois principaux clients ; plausible, non constaté | **3** : plus personne ne peut corriger le logiciel |

Les deux risques dont la probabilité et l'impact sont tous deux de niveau 3, à traiter en priorité selon la règle du comité de direction, sont **R1** et **R2**. R3 et R4 sont fréquents mais leur effet reste un mode dégradé ; R5 est grave mais moins probable. Plusieurs risques ont une cause commune : la dépendance envers un petit éditeur, que l'on retrouve dans R1, R3 et R5.

*3.2 b) – ISO/IEC 27005 ou EBIOS Risk Manager*

**Comparaison** (b-1) :
- l'**ISO/IEC 27005:2022** donne des **lignes directrices** internationales : elle décrit le processus de gestion des risques liés à la sécurité de l'information (établir le contexte, identifier, analyser, évaluer, traiter, surveiller) et les options de traitement, dans la logique du système de management de l'ISO/IEC 27001:2022. Elle ne prescrit **aucune méthode** : l'organisation choisit ses échelles et ses techniques. Elle n'est ni une norme d'exigences ni une solution ;
- **EBIOS Risk Manager** (ANSSI, version 1.5 de 2024) est une **méthode** française, compatible avec l'ISO/IEC 27005, qui outille ce processus en cinq ateliers : le cadrage et le **socle de sécurité**, les **sources de risque** et leurs objectifs, les **scénarios stratégiques**, qui passent par l'**écosystème** (éditeurs, prestataires, partenaires), les scénarios opérationnels, puis le traitement (F12 § 2 ; annexe 3.5).

**Choix** : EBIOS Risk Manager, inscrite dans le processus de l'ISO/IEC 27005. Elle convient au SDIS pour trois raisons tirées du cas :
- les risques les plus graves passent par l'**écosystème** : un éditeur dont l'accès est ouvert en permanence et dont dépendent les correctifs, les SDIS voisins, le centre de régulation médicale du SAMU et les hôpitaux qui reçoivent les comptes rendus ;
- la menace est en partie **intentionnelle** : le rançongiciel du SDIS voisin appelle une analyse des sources de risque, que l'ISO/IEC 27005 prévoit sans fournir de démarche détaillée pour la conduire ;
- l'atelier de **socle de sécurité**, appuyé sur le guide d'hygiène de l'ANSSI, fait apparaître tout de suite les écarts évidents (mises à jour, cloisonnement, sauvegardes), et les scénarios sont lisibles pour le conseil d'administration.

**Limite** : la méthode demande du temps et des compétences, alors que le SDIS n'a ni analyse formalisée ni responsable de la sécurité. Il faut donc restreindre le périmètre au traitement de l'alerte et à ses interfaces, se faire accompagner et présenter au conseil du 01/07/2027 un premier résultat (cadrage, socle, scénarios principaux, mesures prioritaires), à compléter ensuite.

*3.2 c) – Le traitement des deux risques les plus graves*

| Risque | Option retenue et justification | Mesures |
|---|---|---|
| **R1 – Logiciel non maintenu au 01/01/2030** (probabilité 3, impact 3) | **Réduire** d'ici 2030, en préparant **l'évitement** : le risque disparaît si le SDIS quitte la version actuelle avant le 31/12/2029, mais aucune solution de remplacement n'est prête (nouvelle version reportée, utilisée par aucun SDIS). Il faut donc d'ici là réduire la probabilité (préparer le remplacement, calendrier ferme) et l'impact (maintenance prolongée, documentation des interfaces). **Accepter** est exclu : le risque est certain et son impact touche une mission que le projet d'établissement veut garantir jour et nuit. **Transférer** est sans objet : aucun contrat ni aucune assurance ne prend en charge un traitement de l'alerte arrêté | lancer dès 2027 la préparation du remplacement, avec une décision en 2028 sur la suite (nouvelle version de l'éditeur ou autre solution), sans organiser ici le choix ; exiger de l'éditeur un calendrier ferme, une période de recouvrement et une maintenance prolongée en filet de sécurité ; obtenir la documentation des interfaces avant le départ du développeur en 2028 ; prévoir, à la prochaine reconduction du contrat, la remise du code source en cas de défaillance et l'aide à la sortie, ce qui réduit aussi R5 ; informer le conseil d'administration du 01/07/2027 de l'échéance |
| **R2 – Rançongiciel dans les deux salles** (probabilité 3, impact 3) | **Réduire** d'abord la probabilité, car elle tient à des faiblesses connues et corrigeables, puis l'impact. **Transférer** n'est que partiel : une assurance peut couvrir des frais de reconstruction et de gestion de crise, jamais l'arrêt de l'alerte ni ses conséquences pour les victimes ; elle complète les mesures, sans les remplacer. **Accepter** est inadmissible pour un système critique ; **éviter** est impossible | séparer le réseau du traitement de l'alerte de celui de la bureautique et des tablettes, en n'ouvrant que les flux nécessaires (question 3.3) ; remplacer le compte commun de l'éditeur par des accès nominatifs, ouverts à la demande, avec une authentification forte et une trace ; tant que le système d'exploitation ne peut être mis à jour, isoler davantage ces serveurs et exiger de l'éditeur une version compatible ; sauvegardes hors ligne dont la restauration est essayée ; procédure de repli sur papier et entraide des centres de traitement de l'alerte voisins, exercées, comme en février 2027 |

Après traitement, le **risque résiduel** est présenté au directeur départemental, qui l'accepte formellement, puis au conseil d'administration.

**Réponses tolérées**
- Autres risques tirés de l'annexe 3.2, si chacun est formulé comme un événement redouté et coté selon les échelles : interfaces arrêtées au départ du développeur ; intervention malveillante par le compte commun de l'éditeur.
- R2 coté 2 en probabilité au titre du « constaté dans un autre SDIS », si le candidat retient ensuite R1 et un autre risque de niveau 3 × 3 qu'il justifie, ou s'il explique pourquoi il traite quand même R2 ; R3 coté 3 en impact si le candidat montre qu'une anomalie plus longue arrêterait l'engagement des secours.
- ISO/IEC 27005 retenue seule, pour sa simplicité et le délai court avant le conseil du 01/07/2027, si la nature des deux référentiels est juste et si l'écosystème est pris en compte.
- « Éviter » seul pour R1, s'il est défini comme l'abandon de la situation à l'origine du risque (exploiter la version actuelle après le 31/12/2029) et si le candidat montre comment le SDIS tient jusqu'au remplacement.

**Erreurs fréquentes**
- *Risques réduits à des constats ou génériques (« risque informatique »)* (`JUR-T01`, `JUR-T03`) — juste : des événements redoutés, avec leur cause et leurs chiffres, cotés selon les échelles de l'annexe.
- *Norme, lignes directrices, méthode et solution confondues ; « installer EBIOS »* (`ET-01`, `JUR-S06`) — juste : ISO/IEC 27005, lignes directrices ; EBIOS Risk Manager, méthode ; ISO/IEC 27001, norme d'exigences.
- *Risque « transféré à l'éditeur » ou à l'assureur* (`JUR-T03`) — juste : la responsabilité du traitement de l'alerte reste au SDIS ; l'assurance ne couvre qu'une part financière.
- *Risque de niveau 3 × 3 accepté* — juste : réduire, et faire accepter le seul risque résiduel par le directeur.
- *Choix d'un nouvel éditeur organisé, analyse d'impact détaillée des pannes, chiffrage* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI, événement redouté | cybermenaces, défaillances, risques réglementaires et métiers, dépendance | F12 § 0 et § 5 | notion de cours |
| ISO/IEC 27005:2022 | lignes directrices de gestion des risques, options de traitement | `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager, version 1.5 (ANSSI) | méthode en cinq ateliers, sources de risque, écosystème | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| ISO/IEC 27001:2022 | système de management fondé sur l'appréciation des risques | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | socle de sécurité : mises à jour, cloisonnement, sauvegardes | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |

---

### 3.3 – La sécurité des tablettes et la gouvernance du traitement de l'alerte (4 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique des solutions de cybersécurité n'est pas exigée ; aucun réglage d'équipement ni aucun essai technique ; le Zero Trust est un cadre d'architecture, non un produit ; aucune démarche de conformité formelle à une norme.

**Annexes mobilisées** : annexe 3.3 (tablettes, comptes rendus, réseau, renouvellement de 2027, pertes et vols, incidents, répartition actuelle des rôles), annexe 3.2 (accès permanent de l'éditeur, correctifs), annexe 3.5 (modèle Zero Trust, guide d'hygiène, ISO/IEC 27001:2022, RGPD) et annexe 1.1 (300 tablettes de 2021, 60 centres, organigramme, déléguée à la protection des données).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Architecture de confiance définie (authentification, chiffrement, segmentation ; Zero Trust comme modèle, non comme produit) ; mesures rattachées à une politique de sécurité fondée sur l'analyse des risques | 0,5 |
| a-2 | Authentification personnelle des équipages et chiffrement du stockage et de la transmission, chacun rattaché au risque traité | 0,5 |
| a-3 | Séparation des réseaux et effacement à distance, chacun rattaché au risque traité ; remplacement des tablettes de la fin de 2027 mis à profit | 0,5 |
| a-4 | Quatre indicateurs d'efficacité complets (formule, source, fréquence, cible, axe) | 0,5 |
| b-1 | Désignation d'un responsable de la sécurité des systèmes d'information, rattaché au directeur et indépendant de l'exploitation du système d'information, avec ses missions | 0,5 |
| b-2 | Rôles du directeur départemental, du (de la) chef(fe) du groupement et de la cheffe du service des systèmes d'information et de communication, distingués | 0,5 |
| b-3 | Rôles de la cheffe du centre de traitement de l'alerte et des chefs de centre | 0,5 |
| b-4 | Rôles de l'éditeur et de la déléguée à la protection des données, distingué du responsable de la sécurité | 0,5 |

**Réponse attendue**

*3.3 a) – L'architecture de confiance et quatre mesures*

**Définition** (a-1) : une **architecture de confiance** organise les identités, les terminaux, les réseaux, les applications et les données de façon que seules des personnes et des équipements **authentifiés** accèdent, selon leurs droits, à des ressources **cloisonnées**, et que les données restent **confidentielles et intègres**, y compris hors des locaux. Elle repose sur l'authentification, le chiffrement et la segmentation. Le **Zero Trust** en est un modèle : aucune confiance n'est accordée d'office à une tablette parce qu'elle est connectée au réseau du siège, chaque accès est vérifié. C'est un **cadre d'architecture**, conduit pas à pas, et non un produit que l'on achète (F12 § 3 ; annexe 3.5). Ces mesures s'inscrivent dans une **politique de sécurité fondée sur l'analyse des risques** : approuvée par le directeur, elle fixe les objectifs (confidentialité des données de santé, intégrité des comptes rendus, disponibilité de l'alerte, traçabilité), le périmètre, les règles, l'organisation et les contrôles ; chaque mesure y répond à un risque apprécié, et la charte d'usage n'en est que la déclinaison pour les utilisateurs (F12 § 1).

Risques à traiter, tirés de l'annexe 3.3 : la **divulgation de données de santé** par une tablette perdue ou volée (10 en 2026 ; plus de 1 000 comptes rendus dans la tablette volée en octobre) ou par un courriel non chiffré ; l'**usage d'une tablette par n'importe qui**, avec un code partagé par centre, inchangé depuis 2021 et connu d'agents partis, et des comptes rendus non imputables ; la **propagation d'une attaque** des tablettes ou de la bureautique vers le traitement de l'alerte, comme chez le SDIS voisin ; des **tablettes sans mises à jour de sécurité** (120 sur 300). Le remplacement des 300 tablettes, de septembre à décembre 2027, est l'occasion d'inscrire ces mesures dans les besoins des nouvelles tablettes, et de traiter les anciennes jusque-là.

| Mesure (a-2 et a-3) | Risque traité | Indicateur d'efficacité (a-4) : formule ; source ; fréquence ; cible ; axe |
|---|---|---|
| **1. Authentification personnelle des équipages** : chaque agent ouvre l'application de comptes rendus avec sa carte professionnelle sans contact et un code personnel, soit deux facteurs de nature différente (ce qu'il possède, ce qu'il sait) ; la tablette, partagée par l'équipage, ne compte pas comme facteur personnel ; fin du code commun à un centre ; fermeture automatique de la session | usage par un tiers d'une tablette perdue ou volée ; compte rendu non imputable (confidentialité, traçabilité) | **Part des comptes rendus rédigés après une authentification personnelle** : nombre de comptes rendus rédigés après authentification personnelle / nombre de comptes rendus rédigés × 100 ; journaux de l'application de comptes rendus ; mensuelle ; 100 % dès la mise en service des nouvelles tablettes à la fin de 2027 ; processus |
| **2. Chiffrement** : stockage des tablettes chiffré ; comptes rendus transmis au centre de régulation médicale du SAMU et aux six hôpitaux par une messagerie ou un espace d'échange chiffrés, et non plus en pièce jointe d'un courriel ordinaire | divulgation des données de santé en cas de vol ou d'interception (confidentialité, intégrité) ; une donnée chiffrée volée reste incompréhensible, ce qui évite d'informer les personnes (annexe 3.5) | **Part des comptes rendus transmis par un canal chiffré** : nombre de comptes rendus transmis par un canal chiffré / nombre de comptes rendus transmis × 100 ; journaux de la messagerie ou de l'espace d'échange ; mensuelle ; 100 % au 31/12/2027 ; processus |
| **3. Séparation des réseaux** : les tablettes n'accèdent qu'à une zone réservée à l'application de comptes rendus et à l'échange avec le logiciel de l'alerte ; les serveurs du traitement de l'alerte forment une zone à part, séparée de la bureautique ; seuls les flux nécessaires sont autorisés entre les zones | propagation d'un rançongiciel de la bureautique ou d'une tablette vers le traitement de l'alerte, comme chez le SDIS voisin (disponibilité, intégrité) | **Part des équipements rattachés à la zone de réseau prévue par la politique de sécurité** : nombre de tablettes, de postes et de serveurs dans leur zone / nombre d'équipements inventoriés × 100 ; inventaire du parc et revue des zones par le service des systèmes d'information et de communication ; trimestrielle ; 100 % au 31/12/2027 ; processus |
| **4. Effacement à distance** : toutes les tablettes inscrites dans un outil de gestion de flotte mobile (MDM, *Mobile Device Management*) qui permet de les localiser, de les bloquer, de les effacer à distance et d'imposer les mises à jour ; copie locale effacée dès que la transmission du compte rendu est confirmée ; toute perte déclarée sans délai au centre de traitement de l'alerte, ouvert jour et nuit, qui fait bloquer et effacer la tablette | divulgation des données d'une tablette perdue ou volée ; tablettes sans mises à jour (confidentialité) | **Part des tablettes perdues ou volées bloquées dans l'heure** : nombre de tablettes perdues ou volées dont le blocage et l'effacement ont été ordonnés moins d'une heure après la déclaration / nombre de tablettes perdues ou volées × 100 ; outil de gestion de flotte et registre des incidents ; mensuelle ; 100 %, contre 0 % aujourd'hui (aucun blocage possible) ; processus. Une tablette hors ligne ne s'efface qu'à sa reconnexion : le SDIS mesure l'ordre qu'il maîtrise |

Chaque indicateur est suivi par le responsable de la sécurité et présenté au comité de sécurité ; une cible manquée déclenche une action.

*3.3 b) – Les rôles et les responsabilités dans la gouvernance du traitement de l'alerte*

**Le responsable de la sécurité des systèmes d'information** (b-1) : le directeur départemental désigne un **responsable de la sécurité des systèmes d'information**, aujourd'hui absent. Il le **rattache directement à la direction départementale**, et non au service des systèmes d'information et de communication ni au groupement « Pilotage et systèmes d'information » qui exploite le système d'information : celui qui contrôle la sécurité ne doit pas contrôler son propre travail, et il doit pouvoir alerter le directeur sans filtre. Ce n'est pas un technicien : il pilote la politique de sécurité, conduit l'analyse des risques, organise la gestion des incidents et des crises, la sensibilisation et le suivi des indicateurs. Le système critique qu'est le traitement de l'alerte justifie un poste à part entière, avec un correspondant au service des systèmes d'information et de communication.

| Acteur | Rôle et responsabilités dans la gouvernance du traitement de l'alerte |
|---|---|
| **Directeur départemental** (colonel hors classe GRANVOISE) (b-2) | responsable de la sécurité de l'établissement : approuve la politique de sécurité et les niveaux de risque acceptables, accepte formellement les risques résiduels, désigne le responsable de la sécurité, donne les moyens, préside un comité de sécurité semestriel, rend compte au conseil d'administration (01/07/2027) |
| **Chef(fe) du groupement « Pilotage et systèmes d'information »** (vous) (b-2) | intègre la sécurité dans les projets (remplacement des tablettes, suite du logiciel de traitement de l'alerte, hébergement des serveurs), veille à ce que le service applique les mesures, suit la relation avec l'éditeur et prépare avec le responsable de la sécurité les décisions du directeur ; n'est pas le contrôleur de la sécurité |
| **Cheffe du service des systèmes d'information et de communication** (Mme VARANGEOT) (b-2) | met en œuvre les mesures : séparation des réseaux, gestion de flotte des tablettes, comptes et accès, mises à jour, sauvegardes ; ouvre et ferme les accès de l'éditeur ; traite les incidents techniques et les signale au responsable de la sécurité |
| **Cheffe du centre de traitement de l'alerte** (commandante TOURNEVAL) (b-3) | propriétaire métier du système critique : exprime les besoins de disponibilité, valide la date et l'ordre d'installation des correctifs (d'abord une salle, puis l'autre, jamais aux heures chargées), décide de la bascule et du mode dégradé, reçoit jour et nuit les déclarations de perte de tablettes et fait déclencher l'effacement |
| **Chefs de centre** (b-3) | correspondants de sécurité dans les 60 centres : font respecter l'authentification personnelle et l'interdiction de partager les codes, déclarent sans délai toute perte ou tout vol, signalent les arrivées et les départs des agents, relaient la sensibilisation |
| **Éditeur du logiciel de traitement de l'alerte** (b-4) | prestataire : livre des correctifs essayés sur sa plateforme et installés à une date validée par le centre de traitement de l'alerte, une salle après l'autre ; intervient par des accès nominatifs, ouverts à la demande et tracés ; signale ses incidents et les failles connues ; remet la documentation des interfaces ; s'engage sur le calendrier de fin de maintenance |
| **Déléguée à la protection des données** (Mme FAVERJON) (b-4) | conseille sur la protection des données de santé (aucune copie durable sur les tablettes, chiffrement) ; est informée sans délai de toute perte, de tout vol et de tout incident ; tient le registre des violations et prépare, si la violation présente un risque, la notification à l'autorité de contrôle dans les meilleurs délais et, si possible, dans les 72 heures (annexe 3.5) ; distincte du responsable de la sécurité, qui protège tous les systèmes, elle veille aux droits des personnes |
| **Responsable de la sécurité des systèmes d'information** (à désigner) (b-1) | rédige et fait vivre la politique de sécurité, conduit l'analyse des risques (question 3.2), contrôle l'application des mesures et les indicateurs, organise la gestion des incidents et des crises et les exercices, alerte le directeur |

**Réponses tolérées**
- Autres mesures de même objet : code personnel seul, carte seule ou reconnaissance biométrique, si l'authentification est personnelle et que le candidat ne la présente pas comme une authentification à deux facteurs ; espace d'échange sécurisé à la place d'une messagerie chiffrée ; gestion des applications seules plutôt que de toute la tablette, si l'effacement à distance des données est assuré.
- Indicateurs différents s'ils mesurent l'efficacité de la mesure et sont complets : part des tablettes dont le stockage est chiffré ; nombre de flux non autorisés constatés vers la zone de l'alerte (cible zéro) ; part des tablettes à jour de leurs correctifs de sécurité.
- Responsable de la sécurité rattaché au (à la) chef(fe) du groupement, avec un accès direct au directeur et une indépendance garantie vis-à-vis du service qui exploite le système d'information ; poste partagé avec un autre établissement public, si la disponibilité qu'exige un système critique est discutée.
- Comité de sécurité, sapeurs-pompiers utilisateurs ou centre de régulation médicale du SAMU et hôpitaux ajoutés au tableau.

**Erreurs fréquentes**
- *Zero Trust présenté comme un produit à acheter* (`ET-04`, `JUR-S03`) — juste : un cadre d'architecture, appliqué pas à pas aux tablettes et au réseau.
- *Code à quatre chiffres « plus long » présenté comme une authentification forte* (`ET-28`) — juste : un moyen personnel, et deux facteurs de nature différente.
- *Mesures sans indicateur, ou indicateurs génériques* (`ET-18`, `JUR-S05`) — juste : un indicateur par mesure, avec sa formule, sa source, sa fréquence, sa cible et son axe.
- *Responsable de la sécurité présenté comme un technicien, ou placé sous la cheffe du service qui exploite le système d'information* (`ET-15`) — juste : rattaché au directeur, il pilote et contrôle.
- *Déléguée à la protection des données confondue avec le responsable de la sécurité* (`ET-29`) — juste : deux rôles distincts, qui travaillent ensemble.
- *Réglage des équipements, essais techniques, analyse juridique de la violation de données* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Architecture de confiance, authentification à deux facteurs, gestion de flotte mobile | authentification, chiffrement, segmentation | F12 § 3 | notion de cours |
| Le modèle Zero Trust, avis de l'ANSSI (2021) | cadre d'architecture, non un produit | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | authentification, cloisonnement, appareils mobiles, mises à jour | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Politique de sécurité, acteurs | objectifs, périmètre, règles, organisation ; responsable de la sécurité, déléguée à la protection des données | F12 § 1 ; F15 § 1 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | sécurité des données de santé, registre et notification des violations, en principe | `rgpd` ; F15 § 6 | applicable depuis le 25/05/2018 |

---

### 3.4 – Les salles informatiques et la transition numérique responsable (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : aucun calcul d'empreinte, aucun chiffre d'étude sur l'empreinte du numérique, aucun assujettissement à un cadre de durabilité ; la durabilité est intégrée à la gouvernance du système d'information.

**Annexes mobilisées** : annexe 3.4 (deux salles, consommations, serveurs peu utilisés, renouvellement, proposition du département, deux avis), annexe 3.3 (remplacement des tablettes à la fin de 2027, données de santé), annexe 3.5 (RGPD : sous-traitant) et annexe 1.1 (salle du siège et salle de secours, financement par le département à 55 %, président du conseil d'administration vice-président du conseil départemental, objectif de baisse de 20 % de l'empreinte).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Transition numérique responsable définie ; apports de la proposition appliqués au cas (30 serveurs utilisés à 10 %, virtualisation, indicateur de 1,3 contre environ 2 au siège, chaleur récupérée, mesure continue) | 0,5 |
| a-2 | Limites appliquées au cas : dépendance envers le département, exploitation sans astreinte alors que la messagerie sert jour et nuit, données de santé et sous-traitance, salle du siège conservée avec sa climatisation de 2008, empreinte déplacée | 0,5 |
| a-3 | Conclusion : proposition recommandée sous conditions précises (périmètre, convention, sécurité, réversibilité, mesure partagée, redimensionnement de la salle du siège) | 0,5 |
| b-1 | Allongement de la durée de vie justifié (900 postes renouvelés tous les quatre ans ; fabrication), avec ses conditions | 0,5 |
| b-2 | Réemploi justifié (équipements détruits aujourd'hui ; tablettes de 2021 et serveurs libérés), avec un effacement sûr des données | 0,5 |
| b-3 | Deux indicateurs complets (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.4 a) – La proposition du département*

**Définition** (a-1) : la **transition numérique responsable** est la trajectoire par laquelle une organisation réduit durablement l'empreinte environnementale de son système d'information sur tout son cycle de vie (fabrication, usage, fin de vie). Elle combine la sobriété, qui interroge d'abord le besoin, les bonnes pratiques du Green IT (mutualisation, virtualisation, centres de données efficaces, durée de vie des équipements) et une gouvernance qui mesure, fixe des cibles et arbitre, sans dégrader le service rendu ni la sécurité (F14 § 3 et § 5). Pour le SDIS, elle sert l'objectif d'une baisse de 20 % de l'empreinte d'ici 2031, que rien ne permet aujourd'hui de suivre, l'empreinte du système d'information n'ayant jamais été mesurée.

**Ce qu'apporte la proposition** :
- la **mutualisation** et la **virtualisation** : 30 serveurs de gestion, dont 8 seulement virtualisés, utilisés en moyenne à 10 % de leur capacité, deviendraient des serveurs virtuels sur des équipements partagés. Moins de machines à fabriquer et à alimenter, à service égal ;
- une **salle plus efficace** : l'indicateur d'efficacité énergétique de la salle du département est de 1,3, contre environ 2 au siège (400 MWh consommés pour 200 MWh d'équipements informatiques). Au siège, la moitié de l'électricité sert à autre chose que l'informatique, surtout à une climatisation de 2008 ;
- la **chaleur récupérée** pour chauffer un collège voisin : l'énergie dissipée par les serveurs remplace une partie du chauffage d'un autre bâtiment ;
- la **mesure continue** de la consommation : elle fournit la donnée de départ qui manque pour suivre l'objectif de 2031.

**Ses limites** (a-2) :
- la **dépendance** envers le département, déjà financeur à 55 % : ses priorités passeraient d'abord, et la convention n'est pas écrite (niveaux de service, retour en arrière, sortie) ;
- l'**exploitation** : les agents du département ne sont présents que les jours ouvrés, de 8 heures à 18 heures, sans astreinte, alors que la messagerie sert jour et nuit à envoyer les comptes rendus de secours. Ces serveurs « de gestion » servent donc aussi l'activité opérationnelle ;
- la **sécurité et la confidentialité** : les comptes rendus contiennent des données de santé. Le département deviendrait un sous-traitant, lié par un contrat qui fixe les mesures de sécurité (annexe 3.5). Ses agents ne doivent pas accéder aux données, et la liaison entre les deux réseaux ne doit pas propager une attaque ;
- le **système critique conservé** dans les salles du SDIS : c'est un bon choix pour la maîtrise de l'alerte, mais la salle du siège garde ses 10 serveurs opérationnels et une climatisation de 2008, déjà tombée en panne en juillet 2026 : il faudra la remplacer, redimensionnée ;
- l'**empreinte déplacée** plutôt que supprimée : la part de la salle du département imputable au SDIS doit être comptée dans son empreinte, et la facilité de créer des serveurs virtuels peut en multiplier le nombre (effet rebond).

**Conclusion** (a-3) : recommander la proposition, **sous conditions** :
1. un **périmètre** limité aux applications de gestion qui peuvent attendre un jour ouvré (ressources humaines et paie, finances, formation, parc, indemnités) ; la messagerie et les comptes rendus de secours ne partent que si une astreinte jour et nuit et le chiffrement des données sont garantis, sinon ils restent dans les salles du SDIS ;
2. une **convention** qui fixe les niveaux de service, l'astreinte, les règles de sécurité, le contrat de sous-traitance, la notification des incidents, la réversibilité, et la communication chaque mois de la consommation imputable au SDIS ;
3. le **démontage** des 30 serveurs physiques, réemployés plutôt que détruits, puis le **redimensionnement** de la salle du siège et de sa climatisation pour les seuls serveurs de l'alerte ;
4. l'inscription de l'opération dans la trajectoire de 2031, avec une mesure de départ en 2027.

*3.4 b) – Deux bonnes pratiques et deux indicateurs*

**Allonger la durée de vie des équipements** (b-1) : passer de quatre à six ans pour les 900 postes de travail, et au-delà de quatre ans pour les serveurs conservés. Les achats de postes tomberaient d'environ 225 à 150 par an, soit un tiers de moins. Or c'est la **fabrication** qui pèse souvent le plus dans l'empreinte d'un équipement, plus que son électricité (F14 § 1 et § 3). Conditions : réparation et remplacement des pièces d'usure (batteries, disques), logiciels qui restent compatibles, choix de matériels réparables et mis à jour longtemps, en particulier pour les nouvelles tablettes de 2027.

**Réemployer plutôt que détruire** (b-2) : aujourd'hui, tous les équipements remplacés sont détruits. Les postes et les tablettes encore utilisables sont réemployés en interne (formation, centres armés par des volontaires), reconditionnés par une entreprise spécialisée ou donnés à des associations ou à des établissements scolaires ; seuls les équipements irréparables vont au recyclage. Les premiers candidats sont les 300 tablettes de 2021, remplacées à la fin de 2027, et les serveurs libérés par l'hébergement. Condition propre au SDIS : un **effacement sûr et attesté** des données avant toute sortie, car les tablettes ont contenu des comptes rendus de secours (question 3.3).

**Deux indicateurs de l'impact environnemental du système d'information** (b-3) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Électricité consommée par l'hébergement du système d'information** | somme des MWh consommés par les deux salles du SDIS et des MWh imputés au SDIS par la salle du département | compteurs des salles du SDIS ; relevé mensuel de la consommation imputée au SDIS par le département | mensuelle, bilan annuel | au moins − 30 % en 2029 par rapport à 2026 (430 MWh pour les deux salles du SDIS) | environnement |
| **Taux de réemploi des équipements retirés** | nombre d'équipements retirés réemployés ou reconditionnés / nombre d'équipements retirés × 100 | inventaire du parc informatique et attestations de reprise et d'effacement | annuelle | 70 % en 2028, contre 0 % aujourd'hui | environnement |

**Réponses tolérées**
- Proposition refusée, ou limitée à quelques applications, si l'argument est la sécurité des données de santé ou l'absence d'astreinte, et si une autre voie de réduction est proposée (virtualisation des 30 serveurs dans la salle du siège, puis remplacement de sa climatisation).
- Durée de vie portée à cinq ans, ou à sept ans pour les serveurs, si elle est justifiée et assortie de conditions.
- Autres indicateurs complets : âge moyen des postes à leur retrait (cible six ans) ; indicateur d'efficacité énergétique de la salle du siège après le remplacement de sa climatisation ; taux d'utilisation moyen des serveurs ; « PUE » employé pour l'indicateur d'efficacité énergétique de la salle ; part des achats d'équipements assortis de critères de durabilité.
- Cible de consommation différente si elle est datée, chiffrée et rapportée à une valeur de départ.

**Erreurs fréquentes**
- *Empreinte du système d'information réduite à l'électricité* (`ET-38`) — juste : la fabrication des équipements renouvelés tous les quatre ans et leur destruction pèsent au moins autant ; d'où la durée de vie et le réemploi.
- *Sobriété ou Green IT confondus avec une simple économie d'énergie* (`ET-12`) — juste : interroger le besoin (30 serveurs à 10 %), mutualiser, allonger la durée de vie.
- *Hébergement chez le département présenté comme sans risque, ou « tout externaliser »* (`ET-30`, `JUR-G11`) — juste : astreinte, données de santé, dépendance, convention.
- *Indicateurs incomplets ou génériques* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe, reliés à l'objectif de 2031.
- *Calcul d'empreinte, chiffres d'études, assujettissement du SDIS à un cadre de durabilité* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Green IT, mutualisation, virtualisation, durée de vie, réemploi | bonnes pratiques et leviers | F14 § 3 | notion de cours |
| Indicateur d'efficacité énergétique d'une salle, consommation, durée de vie | indicateurs de l'impact environnemental du SI | F14 § 4 | notion de cours |
| Centres de données efficaces, chaleur récupérée, hébergement mutualisé | transition numérique responsable | F14 § 5 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | sous-traitant lié par un contrat qui fixe les mesures de sécurité, en principe | `rgpd` ; F15 § 5 | applicable depuis le 25/05/2018 |
