# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 57 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F09 performance du SI, F10 audit et fiabilisation, F12 sécurité et résilience, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les coûts du système d'information et leur refacturation aux sociétés de projet | `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI ; `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord ; `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ; `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ; `3.1.e` Revue et amélioration continue des dispositifs de pilotage | 3,5 |
| 3.2 La fiabilité de la chaîne du comptage au chiffre d'affaires | `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels | 3,5 |
| 3.3 La sécurité de l'informatique de conduite et des accès à distance | `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) | 3,5 |
| 3.4 La réponse au comité d'audit | `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 2,5 |
| **Dossier 3 – Maîtriser les coûts, la fiabilité et la sécurité du système d'information de conduite** |  | **13** |

Répartition indicative : connaissances (contrôle de gestion du SI, typologie des risques, fiabilisation, politique de sécurité fondée sur les risques, Zero Trust, critère d'appréciation et élément probant) environ 3 points (items 3.1 a-1, 3.2 a-1, 3.2 b-1, 3.3 a-1, 3.3 b-1 et 3.4 a-1, chacun en partie appliqué au cas) ; analyse des annexes et recommandations environ 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – Les coûts du système d'information et leur refacturation aux sociétés de projet (3,5 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI » ; `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) » ; `3.1.e` « Revue et amélioration continue des dispositifs de pilotage ». Limites : les méthodes classiques de calcul et de décomposition des écarts ne sont pas approfondies ; aucun calcul de répartition n'est demandé ; les règles comptables, fiscales et juridiques de la refacturation entre ESTRAVENT et ses sociétés de projet ne sont pas à traiter (UE 4, UE 1).

**Annexes mobilisées** : annexe 3.1 (dépenses par ensemble de services, refacturation au chiffre d'affaires, inducteurs, coûts non suivis, reporting annuel, avis de M. ORLANCOURT et de Mme MONTREVIAU) et annexe 1.1 (102 sociétés de projet sans salarié, 1 000 MW éoliens et 400 MW solaires, dépenses du SI de 9 M€, 250 M€ de chiffre d'affaires, objectif de 2 500 MW en 2031).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fondamentaux définis et appliqués : centre de coûts et centre de services, refacturation interne, inducteur distingué d'une clé conventionnelle ; situation d'ESTRAVENT qualifiée | 0,5 |
| a-2 | Trois arguments tirés de l'annexe : absence de lien entre chiffre d'affaires et usage du SI (parc arrêté, parcs voisins), subvention des centrales solaires à la supervision des éoliennes, périmètre refacturé trop large | 0,5 |
| a-3 | Un inducteur (ou l'absence de refacturation) pour chaque ensemble de services ; deux choix justifiés par la causalité, la mesurabilité et la stabilité ; nombre d'utilisateurs écarté pour les sociétés de projet | 0,5 |
| b-1 | Trois coûts cachés relevés (temps des techniciens, tableurs et ressaisies du centre de conduite, achats informatiques de l'exploitation), avec la raison pour laquelle chacun échappe au suivi | 0,5 |
| b-2 | Pour chacun, un moyen de mesure réaliste ; lecture en coût complet du SI de conduite | 0,5 |
| c-1 | Trois améliorations : comparaisons (par service, dans le temps, coûts unitaires), objectifs reliés au plan, revue périodique en amélioration continue | 0,5 |
| c-2 | Deux indicateurs complets (formule, source, fréquence, cible, axe), reliés à un constat de l'annexe | 0,5 |

**Réponse attendue**

*3.1 a) – Les fondamentaux, la critique de la clé actuelle et les inducteurs*

**Définitions** (a-1) : le contrôle de gestion appliqué au système d'information mesure le **coût complet** des services numériques (coûts directs, indirects et cachés), l'**impute** aux entités qui les consomment et le rapproche de la valeur et de la qualité rendues (F09 § 2). Une fonction SI **centre de coûts** reçoit un budget et n'est jugée que sur son respect ; un **centre de services** facture ses services aux entités utilisatrices, au coût complet ou à un coût standard, selon des règles connues à l'avance : c'est la **refacturation interne**, qui rend visible ce que chaque entité consomme et la responsabilise. Un **inducteur** est une grandeur dont la variation explique celle du coût d'un service (nombre de machines supervisées, de sites raccordés) ; une clé conventionnelle comme le chiffre d'affaires répartit un total sans lien avec la consommation.

Application : ESTRAVENT refacture bien ses dépenses du SI à ses sociétés de projet, mais en totalité et au prorata du chiffre d'affaires : c'est une **répartition conventionnelle**, pas une refacturation de services ; elle ne dit rien de ce que coûte la supervision d'une éolienne ou d'une centrale.

**Trois arguments contre la refacturation actuelle** (a-2) :
1. **Le chiffre d'affaires ne mesure pas l'usage du SI.** Il dépend du vent, du soleil et du prix de vente, pas des services consommés. Le parc du Centre-Val de Loire arrêté quatre mois a vu sa part divisée par deux (chiffre d'affaires de 4 à 2 M€) alors que ses alarmes ont été multipliées par trois (de 2 000 à 6 000) et que le centre de conduite l'a suivi de près : la clé évolue à l'inverse de la consommation. Deux parcs voisins de même puissance paient des montants différents selon que leur électricité est vendue à prix garanti ou sur le marché.
2. **Les centrales solaires paient pour les éoliennes.** Avec 20 % du chiffre d'affaires (50 M€ sur 250 M€), elles supportent 20 % des 9 M€, soit 1 800 k€, dont 20 % de la supervision des éoliennes (environ 520 k€ sur 2 600 k€), qu'elles n'utilisent pas ; elles ne représentent que 10 % des alarmes (20 000 sur 200 000). Le coût de chaque filière est faussé, et les comparaisons entre parcs avec lui.
3. **Le périmètre refacturé est trop large.** Les 9 M€ sont refacturés en entier, y compris les outils des projets en développement (système d'information géographique, documents des projets) et les services de la DSI aux directions d'ESTRAVENT ; seuls 1 500 k€ de dépenses de la DSI sont des services rendus aux sociétés de projet. Les installations en service portent ainsi le coût du développement de futurs parcs.

La simplicité invoquée par M. ORLANCOURT est réelle, mais elle a un prix : personne ne voit le coût des services, aucune entité n'est incitée à les utiliser mieux, et la clé masquera le coût des nouvelles machines quand la puissance passera de 1 400 à 2 500 MW.

**Une répartition fondée sur des inducteurs** (a-3) :

| Ensemble de services (annexe 3.1 A) | Inducteur proposé | Pourquoi |
|---|---|---|
| DSI – services rendus aux sociétés de projet (1 500 k€) | nombre de sites (une société de projet par site), ou nombre de factures émises | la facturation, les contrats de vente et la comptabilité se tiennent par société de projet |
| DSI – autres services (3 500 k€) | pas de refacturation aux sociétés de projet ; répartition entre les directions d'ESTRAVENT selon le nombre d'utilisateurs | ces services servent les salariés d'ESTRAVENT et le développement ; les sociétés de projet n'ont aucun salarié |
| Supervision des éoliennes (2 600 k€) | nombre d'éoliennes supervisées (420) | **justifié ci-dessous** |
| Supervision des centrales solaires (400 k€) | nombre d'onduleurs supervisés (2 000), ou puissance installée | le système de chaque centrale suit ses onduleurs |
| Liaisons de télécommunication (800 k€) | nombre de sites raccordés (102) | **justifié ci-dessous** |
| Centre de conduite (200 k€) | nombre de sites raccordés, ou puissance installée | ces postes et équipements servent à suivre l'ensemble des sites ; le temps des opérateurs n'est pas dans ces dépenses |

Justification de deux inducteurs :
- **Nombre d'éoliennes supervisées** pour la supervision des éoliennes : le coût de la plateforme, du contrat de l'ESN et des liens avec les systèmes des constructeurs croît avec le nombre de machines raccordées (**causalité**) ; le nombre est connu, stable dans l'année et vérifiable dans les systèmes de supervision et l'inventaire des installations (**mesurabilité**) ; il ne dépend ni du vent ni du prix ; il supprime la charge indue des centrales solaires et suivra le renouvellement des parcs.
- **Nombre de sites raccordés** pour les liaisons : chaque parc et chaque centrale a sa liaison avec le centre de conduite ; le coût est presque proportionnel au nombre de sites, quels que soient leur production et leur prix de vente.

Le **nombre d'utilisateurs** ne peut servir à refacturer les sociétés de projet, qui n'ont aucun salarié : il sert seulement à répartir les services de la DSI entre les directions d'ESTRAVENT. Le **nombre d'alarmes** suit la charge de travail de la supervision, mais l'objection de Mme MONTREVIAU est fondée : il ferait payer aux parcs anciens les défauts de leurs machines et varierait fortement d'une année à l'autre. On peut le combiner à une part fixe par machine ; montrer le coût réel des parcs anciens éclaire d'ailleurs leur renouvellement.

*3.1 b) – Trois coûts cachés du système d'information de conduite*

Un **coût caché** est un coût réel, lié au système d'information, qui n'apparaît pas dans ses dépenses : temps passé par les utilisateurs, ressaisies, outils achetés hors de la fonction SI, interruptions. Il fait partie du coût complet (TCO) et signale souvent un défaut d'intégration du SI (F09 § 2 et § 3.1).

| Coût caché (annexe 3.1 D) | Pourquoi il échappe au suivi | Comment le mesurer |
|---|---|---|
| **Temps des techniciens** à exporter et recopier les données des portails des constructeurs et des centrales : 150 techniciens × 3 heures, soit 450 heures par semaine, environ 20 000 heures par an, l'équivalent de plus de dix postes | ce temps est payé dans la masse salariale de l'exploitation, et non dans les dépenses du SI ; il vient de systèmes non intégrés | rubrique « préparation des données » dans le temps déclaré de chaque intervention du logiciel de gestion de la maintenance, ou relevé sur un échantillon de semaines, valorisé au coût horaire moyen |
| **Tableurs et ressaisies du centre de conduite** : deux opérateurs deux heures chaque matin (environ 1 500 heures par an), une trentaine de tableurs dont personne ne tient la liste | l'outil paraît gratuit et le temps se perd dans le travail des équipes ; le risque d'erreur n'est mesuré nulle part | inventaire des tableurs (propriétaire, usage, fréquence, temps passé), temps de ressaisie relevé, puis valorisé ; les tableurs critiques sont signalés |
| **Achats informatiques de l'exploitation** sur ses frais généraux : environ 350 k€ en 2026, près d'un dixième des 4 M€ de l'informatique de conduite | ils sont enregistrés comme frais de la direction, hors des dépenses du SI ; c'est de l'informatique fantôme, qui comprend des boîtiers de connexion (annexe 3.3) | revue annuelle des factures par fournisseur et par nature d'achat avec la direction financière ; règle selon laquelle tout achat informatique est déclaré au contrôle de gestion et validé par la direction de la performance et des SI |

Le coût complet de l'informatique de conduite dépasse donc nettement les 4 M€ affichés.

*3.1 c) – Trois améliorations du reporting annuel*

1. **Comparer** (c-1) : présenter les dépenses par ensemble de services et par monde (gestion, conduite), et non par seule nature comptable ; les comparer à l'année précédente ; ajouter des coûts unitaires (coût de la supervision par éolienne ou par MW) et le poids du SI dans le chiffre d'affaires, qui seul permet de suivre le passage de 1 400 à 2 500 MW ; intégrer les coûts cachés recensés en b).
2. **Fixer des objectifs** reliés au plan « ESTRAVENT 2031 » : une cible par indicateur, des seuils d'alerte et un responsable ; ajouter, à côté des coûts, quelques indicateurs de service et de risque, pour ne pas réduire le pilotage à la dépense.
3. **Revoir périodiquement** : un point trimestriel au comité de direction, et non une seule lecture au budget, puis une revue annuelle des inducteurs, des cibles et des indicateurs eux-mêmes, dans une logique d'amélioration continue (planifier, faire, vérifier, agir) ; les sociétés de projet connaissent à l'avance les règles de refacturation.

**Deux indicateurs** (c-2) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Poids du système d'information dans le chiffre d'affaires** | dépenses du SI de l'exercice / chiffre d'affaires × 100 | progiciel de gestion intégré et reporting du contrôle de gestion | trimestrielle en cumul, bilan annuel | au plus 3,6 % chaque année jusqu'en 2031 (niveau de 2026 : 9 M€ sur 250 M€), alors que la puissance passe de 1 400 à 2 500 MW | financier |
| **Part des achats informatiques passés hors de la fonction SI** | achats informatiques engagés par les directions sans validation de la direction de la performance et des SI / total des dépenses informatiques × 100 | revue des factures par fournisseur et par nature d'achat | semestrielle | 0 % en 2028, contre près de 4 % en 2026 (350 k€) | gouvernance |

**Réponses tolérées**
- ESTRAVENT présentée comme un centre de services sans refacturation véritable, ou comme un centre de coûts qui répartit son budget : la qualification compte moins que la distinction entre clé conventionnelle et inducteur.
- Autres arguments justes : la clé ne responsabilise personne ; elle empêche de comparer le coût de supervision des parcs ; elle ne prépare pas la croissance du parc. Trois arguments suffisent.
- Puissance installée retenue pour la supervision des éoliennes ou des centrales, si elle est justifiée (stable, connue, proche de la taille des installations) et si ses limites sont dites (une grande éolienne ne coûte pas plus à superviser qu'une petite) ; nombre d'alarmes retenu pour la supervision ou pour le centre de conduite, s'il est assorti d'une réponse à l'objection de Mme MONTREVIAU.
- Unités d'œuvre au lieu d'inducteurs, ou méthode ABC citée en principe, si le lien de causalité est expliqué.
- Autre coût caché justifié : temps des ingénieurs ou de la cellule supervision consacré à la correspondance des données, coût des pannes de la supervision ; trois coûts suffisent.
- Autres indicateurs complets : coût de l'informatique de conduite par MW installé (près de 3 k€ en 2026, cible en baisse en 2031) ; coût de la supervision par éolienne ; heures de ressaisie des techniciens par semaine (cible : division par deux en 2029) ; axe processus admis pour ce dernier.

**Erreurs fréquentes**
- *Fondamentaux récités sans être appliqués à la refacturation aux sociétés de projet* (`JUR-T01`, `ET-39`) — juste : définir, puis montrer que la clé actuelle est une répartition conventionnelle.
- *Répartition chiffrée société par société, ou calcul d'écarts* — non demandés : le choix et la justification des inducteurs suffisent ; l'analyse d'écarts est hors du programme de l'UE 5.
- *Nombre d'utilisateurs retenu pour les sociétés de projet* — elles n'ont aucun salarié.
- *Coût du SI limité aux dépenses affichées* (`ET-33`, `JUR-A03`) — juste : coût complet, avec le temps des utilisateurs et l'informatique achetée hors de la fonction SI.
- *Indicateurs sans cible ni source, ou génériques* (`ET-18`, `JUR-A02`) — juste : cinq champs, reliés au constat.
- *Règles comptables ou fiscales de la refacturation entre sociétés d'un même groupe* — hors sujet (UE 4, UE 1).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Contrôle de gestion du SI | centre de coûts, centre de services, refacturation, inducteurs, coûts directs, indirects et cachés | F09 § 0 et § 2 | notion de cours |
| TCO et coûts cachés | coût complet, temps des utilisateurs, informatique fantôme | F09 § 3.1 | notion de cours |
| Tableau de bord et revue | indicateurs à cinq champs, critique d'un reporting, amélioration continue | F09 § 4.1 à 4.3 | notion de cours |

---

### 3.2 – La fiabilité de la chaîne du comptage au chiffre d'affaires (3,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels ». Limites : ni règle comptable, ni écriture, ni contrôle des comptes ; aucune analyse d'impact détaillée ; l'ISO/IEC 27005 est mobilisée pour ses seules options de traitement.

**Annexes mobilisées** : annexe 3.2 (chaîne en cinq étapes, incidents de 2026, échelles), annexe 3.5 (options de traitement de l'ISO/IEC 27005:2022) et annexe 1.1 (trois contrats d'achat direct, 10 % de l'électricité vendue, objectif de 40 %, facturation de l'électricité dans des tableurs et le module du progiciel).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers) ; risques formulés comme des événements redoutés | 0,5 |
| a-2 | Quatre risques tirés de l'annexe, situés chacun à une étape de la chaîne et classés | 0,5 |
| a-3 | Probabilité et impact cotés selon les échelles de l'annexe 3.2 C, de façon justifiée ; les deux risques de niveau 3 × 3 dégagés | 0,5 |
| b-1 | Fiabilisation définie ; traitement choisi et justifié pour les deux risques | 0,5 |
| b-2 | Deux contrôles pour le risque sur les données de comptage, avec nature, responsable et garantie | 0,5 |
| b-3 | Deux contrôles pour le risque sur le calcul et le chiffre d'affaires, avec nature, responsable et garantie | 0,5 |
| b-4 | Traçabilité des corrections et réduction de la dépendance envers une seule personne | 0,5 |

**Réponse attendue**

*3.2 a) – Quatre risques de la chaîne, classés et cotés*

**Typologie** (a-1) : les risques liés aux systèmes d'information se classent en **cybermenaces** (attaques et malveillances, internes ou externes), **défaillances opérationnelles** (pannes, erreurs humaines, défauts de traitement ou de données), **risques réglementaires** (manquement à une obligation) et **risques métiers** (atteinte à l'activité, à la relation avec les clients, dépendance envers une personne ou un fournisseur) (F12 § 0 et § 5). Un risque se formule comme un **événement redouté**, avec sa cause et sa conséquence, et non comme un constat.

| Risque (événement redouté) | Étape de la chaîne | Catégorie | Probabilité | Impact |
|---|---|---|---|---|
| **R1 – Des données de comptage fausses, en double ou manquantes entrent dans le calcul sans être détectées** (fichier copié deux fois en avril, compteur remplacé non reconnu, volumes repris de la supervision pendant trois mois) | comptage (données d'entrée) | défaillance opérationnelle | **3** : constaté deux fois en 2026 | **3** : factures fausses envoyées, deux contestées |
| **R2 – Une erreur de calcul dans un tableur non contrôlé fausse l'énergie facturée et le chiffre d'affaires** (formule recopiée, 150 k€ sous-facturés en six mois, découverte après la publication) | calcul et chiffre d'affaires | défaillance opérationnelle | **3** : constaté en 2026 | **3** : facture fausse et chiffre d'affaires publié inexact |
| **R3 – La seule personne qui sait construire et modifier les tableurs s'absente ou part, et la facturation est bloquée**, alors que les contrats doivent passer de trois à une quinzaine | calcul et facturation | risque métier (dépendance envers une personne clé) | **2** : plausible, jamais constaté | **2** : factures retardées |
| **R4 – ESTRAVENT ne peut plus justifier une facture ou son chiffre d'affaires**, faute de trace des corrections et parce que chaque chargée prépare, vérifie et envoie ses propres factures | facturation et chiffre d'affaires | défaillance opérationnelle (contrôle interne), à dimension réglementaire | **3** : certain en l'état | **2** : justification impossible sans recherches longues |
| R5 – Un tableur est modifié par erreur ou par malveillance, ou rendu illisible par une attaque, depuis le dossier partagé ouvert aux 25 salariés de la direction de l'énergie | calcul | cybermenace (malveillance interne ou externe) | 2 | 3 |

Quatre risques sont attendus. Les deux risques prioritaires, de niveau **3 × 3**, sont **R1** et **R2** : ils se sont déjà réalisés et ils touchent la facture et le chiffre d'affaires publié.

*3.2 b) – Le traitement des deux risques les plus graves*

**Définition** (b-1) : fiabiliser un système d'information de gestion, c'est mettre en place les dispositifs qui garantissent que les données qu'il produit sont **exhaustives, exactes, autorisées, traçables** et rattachées à la bonne période : contrôles généraux informatiques (accès, changements, exploitation), contrôles applicatifs (à la saisie, au traitement, aux interfaces, en sortie), séparation des tâches et piste d'audit (F10 § 2 et § 3). Ici, chaque passage de la chaîne est à contrôler : fichier du gestionnaire du réseau, tableur, saisie dans le progiciel, chiffre d'affaires.

**Traitement** : **réduire** les deux risques. On ne peut ni les **accepter** (niveau 3 × 3, factures contestées, chiffre d'affaires publié), ni les **éviter** (les contrats d'achat direct sont au cœur du plan, de 10 % à 40 % des ventes), ni les **transférer** (aucune assurance ne rend une facture juste ni ne restaure la confiance d'un industriel). La réduction passe, à terme, par un calcul hors des tableurs, dans un outil de gestion des contrats ou dans le progiciel, alimenté par des fichiers intégrés automatiquement ; d'ici là, par un tableur modèle unique, aux formules protégées, versionné et éprouvé sur un mois connu avant toute modification.

**R1 – Données de comptage** (b-2) :

| Contrôle | Nature | Responsable | Ce qu'il garantit |
|---|---|---|---|
| **Contrôle à l'intégration des fichiers de comptage** : un seul fichier par parc et par mois (doublon rejeté), numéro de compteur reconnu dans une table des points de livraison tenue à jour des changements signalés par le gestionnaire du réseau, nombre de valeurs égal au nombre d'heures du mois ; tout rejet est signalé, et aucune donnée de la supervision ne remplace le comptage sans accord écrit et sans mention sur la facture | préventive, automatisée | direction de l'énergie, avec la DSI pour l'outil | exhaustivité, unicité et bon rattachement des données d'entrée : il aurait arrêté le double import d'avril et le compteur non reconnu de juin |
| **Rapprochement formalisé, mensuel, de la supervision et du comptage, parc par parc, avant toute facture** : aujourd'hui, les deux sources sont posées côte à côte, sans seuil ni blocage ; l'écart normal est d'environ 2 % ; au-delà d'un seuil fixé (par exemple deux fois l'écart normal), la facture est bloquée jusqu'à ce que la cause soit expliquée et notée | détective, semi-automatisée | chargée de facturation, avec la cellule supervision pour expliquer l'écart | cohérence entre deux sources indépendantes : l'écart de 8 % aurait été vu dès juin, et non trois mois plus tard |

**R2 – Calcul et chiffre d'affaires** (b-3) :

| Contrôle | Nature | Responsable | Ce qu'il garantit |
|---|---|---|---|
| **Bouclage des volumes et validation par une seconde personne avant l'émission** : les volumes facturés, heure par heure et sur le mois, sont rapprochés des volumes comptés des parcs du contrat, selon les règles du contrat (profil horaire, énergie manquante achetée par l'agrégateur) ; tout écart non expliqué bloque la facture ; le montant est recalculé à partir des volumes et du prix du contrat ; la facture est validée par une autre personne que celle qui l'a préparée | détective, semi-automatisée puis manuelle | l'autre chargée de facturation ou le directeur de l'énergie | exactitude de chaque facture et séparation entre préparation, validation et envoi : les heures omises auraient fait apparaître un écart avec le comptage dès le premier mois |
| **Rapprochement semestriel avant la publication du chiffre d'affaires** : chiffre d'affaires des contrats dans le progiciel = factures émises = volumes facturés × prix, et volumes facturés comparés aux volumes comptés du semestre ; tout écart est expliqué avant la publication | détective, manuelle | direction financière | exactitude et exhaustivité du chiffre d'affaires publié : l'erreur de 150 k€ aurait été vue avant la publication du chiffre d'affaires de 2026 |

**Traces et dépendance** (b-4) :
- **traçabilité** : les fichiers de comptage reçus sont conservés tels quels ; chaque correction d'un calcul ou d'une facture est enregistrée (qui, quand, quoi, pourquoi, validée par qui) ; la facture initiale reste conservée avec la facture refaite et le motif ; on reconstitue ainsi le chemin de chaque facture, du compteur au chiffre d'affaires (**piste d'audit**) ;
- **dépendance** : la méthode de calcul est écrite (règles de partage entre parcs, cas du fichier manquant) ; la seconde chargée et une personne de la direction financière sont formées à construire et à modifier un calcul ; la validation croisée des factures entretient cette double compétence ; l'outil standard visé à terme réduit la dépendance ; l'accès au dossier des tableurs est restreint aux deux chargées et à leur responsable.

**Réponses tolérées**
- Autres formulations des risques, si ce sont des événements redoutés tirés de l'annexe, par exemple « une facture contestée fait perdre la confiance d'un industriel » classée en risque métier ; R3 coté en impact 3, si le candidat suppose que la seconde chargée, sans les tableurs, enverrait des factures fausses.
- R4 classé en risque réglementaire (obligation de justifier les factures), sans analyse juridique.
- Remplacement du tableur par un outil présenté comme une manière d'**éviter** la source du risque de calcul, si la réduction des autres causes est traitée.
- Autres contrôles justes : contrôle de vraisemblance du volume facturé par rapport au profil horaire du contrat ; rapprochement entre le montant saisi dans le progiciel et le tableur ; interface automatique entre le calcul et le module de facturation pour supprimer la saisie à la main. Deux contrôles par risque suffisent.
- Seuil d'écart différent de deux fois l'écart normal, s'il est fixé et justifié.

**Erreurs fréquentes**
- *Risques formulés comme des constats ou des causes* (« pas de trace ») — juste : événement redouté avec sa conséquence (`JUR-T03`).
- *Contrôles sans nature, sans responsable ou sans lien avec un incident de l'annexe* (`JUR-T01`, `JUR-T08`).
- *Réponse réduite au remplacement du logiciel* — juste : contrôles, séparation des tâches et traces, puis outil (`JUR-T09`).
- *Fiabilisation confondue avec l'audit légal des comptes* (`ET-34`) — juste : la fiabilité des données de facturation est un objet de l'UE 5 ; ni écriture, ni règle comptable, ni opinion sur les comptes ne sont attendues.
- *Traitement « accepter » ou « transférer » retenu pour un risque de niveau 3 × 3, sans justification* — juste : réduire, au vu de la probabilité, de l'impact et de la place des contrats d'achat direct dans le plan.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI | cybermenaces, défaillances opérationnelles, risques réglementaires et métiers | F12 § 0 et § 5 | notion de cours |
| ISO/IEC 27005:2022 | options de traitement : réduire, accepter, éviter, transférer | `iso_27005_2022` ; F12 § 2 | en vigueur |
| Fiabilisation des SI de gestion | contrôles applicatifs, interfaces, séparation des tâches, piste d'audit | F10 § 2, § 3.1 et § 3.2 | notion de cours |

---

### 3.3 – La sécurité de l'informatique de conduite et des accès à distance (3,5 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) ». Limites : la mise en œuvre technique n'est pas exigée ; aucun paramétrage d'équipement ni aucun essai technique ; ni démarche de conformité formelle à une norme, ni assujettissement à déterminer ; l'organisation de la DSI et le rattachement de la cellule supervision ne sont pas à traiter.

**Annexes mobilisées** : annexe 3.3 (huit entreprises extérieures, outils, boîtiers et comptes, accès permanents, réseau commun avec la bureautique, systèmes non modifiables, incident de septembre 2026, attaque d'un autre producteur, organisation actuelle, avis), annexe 3.5 (ISO/IEC 27001:2022, ISO/IEC 27005:2022, guide d'hygiène, Zero Trust) et annexe 1.1 (organigramme, cellule supervision rattachée à l'exploitation, plateforme maintenue par l'ESN, centre de conduite jour et nuit, objectif de disponibilité de 97 %).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Politique de sécurité fondée sur l'analyse des risques définie (objectifs, périmètre, principes, organisation, règles, contrôle ; mesures proportionnées aux risques) et appliquée à la conduite, qui n'a ni politique ni analyse des risques | 0,5 |
| a-2 | Quatre principes propres à la conduite, chacun distingué de la gestion et justifié par l'annexe | 0,5 |
| a-3 | Rôle des six acteurs demandés, cohérent avec l'organigramme | 0,5 |
| b-1 | Zero Trust présenté comme un modèle d'architecture, non un produit, et appliqué à la confiance implicite d'aujourd'hui | 0,5 |
| b-2 | Mesures sur l'authentification et les comptes, et sur le point d'accès unique, chacune avec son constat et le risque traité | 0,5 |
| b-3 | Mesures sur la séparation de la conduite et de la bureautique, et sur l'ouverture à la demande et la traçabilité, chacune avec son constat et le risque traité | 0,5 |
| b-4 | Réponse argumentée à la crainte de Mme MONTREVIAU | 0,5 |

**Réponse attendue**

*3.3 a) – La politique de sécurité de l'informatique de conduite*

**Définition** (a-1) : la politique de sécurité du système d'information est le document de référence, approuvé par la direction, qui fixe les **objectifs** de sécurité (confidentialité, intégrité, disponibilité et traçabilité), le **périmètre**, les **principes**, l'**organisation** et les responsabilités, les **règles** et le **dispositif de contrôle** ; elle se décline en procédures et en chartes (F12 § 1). Elle est **fondée sur l'analyse des risques** quand ses mesures découlent de risques identifiés, analysés et hiérarchisés (ISO/IEC 27005:2022), au lieu d'un catalogue appliqué partout ; elle s'améliore en continu, dans la logique d'un système de management de la sécurité de l'information (ISO/IEC 27001:2022). Application : l'informatique de conduite d'ESTRAVENT n'a ni politique, ni analyse des risques, et la politique de la DSI ne la couvre pas ; la première étape est l'analyse des risques de la conduite, qui fera apparaître les accès des tiers, le réseau partagé avec la bureautique et les systèmes qui ne reçoivent plus de correctifs.

**Quatre principes propres à la conduite** (a-2) :

| Principe | En quoi il se distingue de l'informatique de gestion | Ce qui le justifie (annexe 3.3) |
|---|---|---|
| **La disponibilité et l'intégrité des commandes passent en premier** ; aucune mesure de sécurité ne doit arrêter une installation, et tout changement est préparé avec le centre de conduite | en gestion, la confidentialité des données pèse souvent autant ; en conduite, une commande malveillante ou un arrêt touchent la production, les machines et la sécurité des techniciens | parcs d'un autre producteur arrêtés deux jours ; objectif de 97 % de disponibilité |
| **Cloisonner et protéger autour des systèmes qu'on ne peut pas corriger** (défense en profondeur) | en gestion, on applique les correctifs ; en conduite, les constructeurs interdisent toute modification : la protection vient des zones, des points d'entrée et de la surveillance | systèmes anciens sans correctifs ; postes et plateforme reliés à la bureautique |
| **Les accès des entreprises extérieures restent sous le contrôle d'ESTRAVENT** : chaque tiers s'engage par contrat (comptes nominatifs, départs signalés, incidents notifiés, audit accepté) | en gestion, les tiers sont peu nombreux et passent par la DSI ; en conduite, huit entreprises entrent dans les installations par leurs propres outils | huit outils, 110 boîtiers dont 20 sans entreprise connue, contrats muets sur la sécurité |
| **Moindre privilège, imputabilité et traçabilité de chaque action sur une installation**, avec des journaux conservés par ESTRAVENT et surveillés jour et nuit | en gestion, les journaux servent surtout après coup ; en conduite, le centre de conduite doit voir en temps réel qui agit sur une machine | 50 comptes partagés, 9 000 connexions sans trace, connexion d'un dimanche à 3 heures découverte par le constructeur |

**Rôle des acteurs** (a-3) :

| Acteur | Rôle dans la politique de sécurité de la conduite |
|---|---|
| Présidente-directrice générale, Mme VARLAMBERT | approuve la politique, arbitre les moyens et accepte les risques résiduels ; en rend compte au conseil d'administration et au comité d'audit |
| Vous, directeur (directrice) de la performance et des SI | faites conduire l'analyse des risques, élaborez la politique et la tenez cohérente avec celle de l'informatique de gestion ; pilotez sa mise en œuvre et ses indicateurs ; veillez à ce qu'une personne soit chargée de la sécurité de la conduite, ce qui n'est pas le cas aujourd'hui |
| Directrice de l'exploitation, Mme MONTREVIAU | propriétaire des risques de la conduite : exprime les besoins de disponibilité, valide les règles qui touchent l'exploitation, les fait appliquer par ses équipes et dans les contrats des sous-traitants |
| Responsable de la cellule supervision, Mme QUILLEBRAND | met en œuvre les mesures sur la plateforme et les liens avec les installations, tient l'inventaire des accès, des comptes et des boîtiers, traite les incidents avec la DSI |
| Responsable du centre de conduite, M. FERRASSOT | autorise et ouvre les accès à la demande, jour et nuit ; surveille les connexions ; donne l'alerte et décide d'isoler ou d'arrêter une installation en cas d'incident |
| Entreprises extérieures | respectent les engagements de sécurité de leur contrat : comptes nominatifs, liste des intervenants tenue à jour, accès par le seul point d'ESTRAVENT, incidents signalés, audits acceptés |

*3.3 b) – Quatre mesures d'architecture de confiance pour les accès à distance*

**Le modèle Zero Trust** (b-1) est un **modèle d'architecture, et non un produit** : aucune confiance n'est accordée d'office à un utilisateur ou à un équipement en raison de sa place sur le réseau ; chaque accès est authentifié, autorisé et vérifié selon le contexte (identité, équipement, moment, besoin), avec le moindre privilège, le cloisonnement et une surveillance continue ; c'est une démarche progressive, qui ne remplace pas la défense en profondeur (annexe 3.5 ; F12 § 3). Chez ESTRAVENT, la confiance est aujourd'hui implicite : quiconque connaît un mot de passe partagé et atteint l'un des 110 boîtiers entre dans une installation, à toute heure.

| Mesure | Constat de l'annexe 3.3 | Risque traité |
|---|---|---|
| **Authentification forte et comptes nominatifs** (b-2) : un compte par technicien de chaque entreprise, avec authentification à plusieurs facteurs ; droits limités aux seules installations sur lesquelles l'entreprise intervient (moindre privilège) ; création et suppression liées à la liste des intervenants que chaque entreprise tient à jour et à la date de fin de son contrat ; revue trimestrielle des comptes | 50 comptes partagés sur 60, mots de passe inchangés depuis la mise en service, compte d'un sous-traitant parti, qui n'intervenait que sur les postes électriques, utilisé en septembre 2026 sur le système d'un constructeur | usurpation d'un compte et accès non autorisé ; impossibilité de savoir qui a agi |
| **Point d'accès unique et contrôlé** (b-2) : tous les accès à distance passent par une passerelle exploitée par ESTRAVENT, à l'entrée de la zone de conduite ; les huit outils et les 110 boîtiers sont retirés, en commençant par les 20 boîtiers sans entreprise connue | huit outils, 110 boîtiers, dont 20 sans entreprise connue | entrée dérobée inconnue, accès qui échappe à tout contrôle ; attaque passant par l'accès d'un prestataire, comme chez l'autre producteur |
| **Séparation entre l'informatique de conduite et la bureautique** (b-3) : la plateforme et les postes du centre de conduite forment une zone séparée ; la messagerie et internet se consultent sur d'autres postes ; les seuls échanges entre zones sont ceux qui sont nécessaires, décrits et surveillés (données de production envoyées vers la gestion, par exemple) | postes du centre de conduite et serveurs de la plateforme reliés au réseau de bureautique ; systèmes anciens sans correctifs | propagation vers la conduite d'une attaque partie de la bureautique (courriel piégé, rançongiciel), jusqu'à l'arrêt de parcs |
| **Accès ouverts à la demande, limités dans le temps et tracés** (b-3) : l'entreprise demande l'accès pour une intervention liée à un ordre de travail ; le centre de conduite le valide et l'ouvre pour la durée utile ; la session est enregistrée et ses journaux sont conservés par ESTRAVENT ; toute connexion hors demande déclenche une alerte | accès ouverts en permanence, centre de conduite non prévenu, 9 000 connexions en 2026 sans trace chez ESTRAVENT, connexion de 40 minutes un dimanche à 3 heures | connexion malveillante non détectée ; absence de preuve en cas d'incident |

**Réponse à Mme MONTREVIAU** (b-4) : il ne s'agit pas de fermer les accès, mais de les **mettre sous contrôle**. Le centre de conduite fonctionne jour et nuit : il peut ouvrir un accès en quelques minutes à 3 heures du matin, et une procédure d'urgence, préautorisée pour les pannes qui arrêtent une machine et revue après coup, garde la réactivité des constructeurs. L'objectif de 97 % est bien plus menacé par une attaque comme celle de l'autre producteur, qui a arrêté plusieurs parcs pendant deux jours, que par une validation de quelques minutes. Les nouvelles règles s'appliquent progressivement, constructeur par constructeur, sans interrompre les dépannages.

**Réponses tolérées**
- Autres principes justes : sensibilisation des opérateurs et des techniciens ; gestion des incidents propre à la conduite, avec le centre de conduite ; inventaire des installations et des accès comme préalable ; amélioration continue. Quatre principes suffisent, s'ils sont distingués de la gestion.
- Politique de la conduite présentée comme un chapitre d'une politique unique de l'entreprise, plutôt qu'un document séparé.
- Rôles complétés par la DSI (réseau, annuaire), la déléguée à la protection des données (journaux nominatifs des techniciens, en principe) ou le comité d'audit (surveillance) ; désignation d'un responsable de la sécurité des systèmes d'information couvrant les deux mondes, si elle n'occupe pas toute la réponse.
- Chiffrement des sessions à distance ajouté aux mesures, si les quatre mesures demandées sont traitées.
- « Bastion » ou « passerelle d'administration » pour le point d'accès unique ; « micro-segmentation » pour la séparation, si elle est expliquée.

**Erreurs fréquentes**
- *Politique de sécurité confondue avec une charte d'usage, ou réduite à une liste de mesures techniques* (`ET-27`, `JUR-S01`).
- *Zero Trust présenté comme un produit à acheter* (`ET-04`, `JUR-S03`) — juste : modèle d'architecture et démarche progressive.
- *Norme, guide et solution confondus* (« installer l'ISO/IEC 27001 ») (`ET-01`, `JUR-S06`).
- *Mot de passe complexe présenté comme une authentification forte* (`ET-28`) — juste : au moins deux facteurs de nature différente.
- *Fermeture pure et simple des accès des constructeurs*, sans égard pour la disponibilité — juste : accès sous contrôle, ouverts à la demande jour et nuit.
- *Paramétrage d'équipements ou essais techniques détaillés* — hors programme.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 27001:2022 | système de management de la sécurité de l'information fondé sur l'appréciation des risques, amélioration continue | `iso_27001_2022` ; F12 § 2 | en vigueur |
| ISO/IEC 27005:2022 | gestion des risques liés à la sécurité de l'information | `iso_27005_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique de l'ANSSI, version de 2017 | authentification, mises à jour, cloisonnement des réseaux | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Le modèle Zero Trust, avis de l'ANSSI (2021) | modèle d'architecture, non un produit | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| Politique de sécurité, CID et traçabilité, acteurs | objectifs, principes, organisation | F12 § 1 | notion de cours |

---

### 3.4 – La réponse au comité d'audit (2,5 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : l'exécution d'essais techniques détaillés n'est pas attendue ; ni la démarche détaillée de l'audit, ni son calendrier, ni le choix de l'auditeur ne sont demandés ; aucune conformité financière.

**Annexes mobilisées** : annexe 3.4 (demande du comité d'audit et contraintes), annexe 3.3 (situation des accès, que les nouvelles règles doivent corriger), annexe 3.5 (COBIT 2019, ISO/IEC 27001:2022) et annexe 1.1 (comité d'audit présidé par M. ESCOLIÈRE, 102 sites dans quatre régions, constructeurs A, B et C).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Critère d'appréciation et élément probant définis ; référentiel de l'audit indiqué (politique de sécurité de la conduite, appuyée sur ISO/IEC 27001 ou COBIT 2019) | 0,5 |
| a-2 | Sécurité et fiabilité des traces : ce qui est attendu, et un élément probant pertinent et fiable pour chacune | 0,5 |
| a-3 | Conformité à la politique : ce qui est attendu et un élément probant ; réponse adressée au comité | 0,5 |
| b-1 | Deux premiers points de vigilance propres à des installations en production, avec la manière d'y répondre | 0,5 |
| b-2 | Troisième point de vigilance (étendue et échantillon raisonné), avec la manière d'y répondre | 0,5 |

**Réponse attendue**

*3.4 a) – Trois critères et leurs éléments probants*

**Définitions** (a-1) : un **critère d'appréciation** est la référence (objectif, exigence, règle interne, norme) à laquelle l'auditeur compare la situation constatée pour qualifier un écart ; il rend le jugement de l'audit explicite et discutable (F10 § 1.1). Un **élément probant** est une information que l'auditeur recueille pour fonder sa conclusion (document, journal, observation, entretien recoupé, échantillon) ; il doit être pertinent et fiable : une preuve produite par le système ou par un tiers vaut mieux qu'une déclaration de l'audité. Le référentiel de l'audit sera la **politique de sécurité de la conduite**, une fois approuvée, appuyée sur les mesures de l'ISO/IEC 27001:2022 ; COBIT 2019 peut structurer l'audit du point de vue de la gouvernance (annexe 3.5).

| Critère | Ce qui sera attendu | Élément probant que l'auditeur demandera |
|---|---|---|
| **Sécurité des accès** (a-2) | seules des personnes autorisées accèdent aux installations, avec un compte nominatif et une authentification forte, par le seul point d'accès d'ESTRAVENT ; plus aucun compte d'une entreprise dont le contrat est terminé ; plus aucun boîtier hors de ce point | rapprochement de la liste des comptes actifs de la passerelle avec la liste des intervenants habilités et des contrats en cours à la date de l'audit ; inventaire des boîtiers retirés, comparé à l'inventaire de 2027 (110 boîtiers) |
| **Fiabilité des traces** (a-2) | chaque connexion est enregistrée (qui, quand, quelle installation, quelle action), les journaux sont complets, horodatés, protégés contre la modification et conservés par ESTRAVENT | échantillon de connexions du semestre, rapproché des demandes validées par le centre de conduite et des ordres de travail, puis des journaux des systèmes des constructeurs : une connexion présente chez un constructeur et absente de la passerelle révèle un contournement |
| **Conformité à la politique** (a-3) | la politique est approuvée et appliquée : procédure de demande et de validation suivie, revue trimestrielle des comptes faite, engagements de sécurité inscrits dans les contrats des huit entreprises, incidents enregistrés et traités | politique approuvée par la présidente-directrice générale ; comptes rendus des revues des comptes ; contrats ou avenants des huit entreprises ; registre des incidents ; échantillon de demandes d'accès |

*3.4 b) – Trois points de vigilance propres à des installations en production*

| Point de vigilance | Manière d'y répondre |
|---|---|
| **Aucune installation ne doit être arrêtée ni perturbée** (b-1) | l'audit travaille sur les documents, les journaux exportés, les entretiens et l'observation des sessions au centre de conduite, sans intervention sur les systèmes en service ; toute visite de site ou consultation d'un système se fait en lecture seule, accompagnée, et après accord du centre de conduite et de la directrice de l'exploitation ; aucun essai technique |
| **Les preuves sont en partie chez les tiers, et leurs systèmes ne peuvent pas être modifiés** (b-1) | obtenir dès maintenant, dans les contrats ou par avenant, l'engagement des huit entreprises de remettre leurs journaux et de coopérer à l'audit ; demander tôt les exports des constructeurs ; juger les mesures qui entourent les systèmes non modifiables plutôt que reprocher l'absence de correctifs |
| **L'étendue : 102 sites dans quatre régions, huit entreprises, trois systèmes de constructeurs** (b-2) | un échantillon raisonné plutôt qu'un examen exhaustif : chaque constructeur, chaque région, les sous-traitants et l'ESN, et les sites des anciens boîtiers sans entreprise connue ; vérifier de loin, à partir des journaux centralisés, et ne se déplacer que sur quelques sites ; un auditeur qui connaît à la fois l'informatique de gestion et les systèmes industriels |

**Réponses tolérées**
- Autres points de vigilance justes : compétences et indépendance de l'auditeur (connaissance des systèmes industriels ; indépendance vis-à-vis de l'ESN, des constructeurs et de ceux qui ont conçu les mesures, y compris votre direction ; compte rendu direct au comité d'audit) ; adhésion de l'exploitation, qui craint pour la disponibilité ; suites données aux recommandations, avec un plan d'action suivi par le comité. Trois points suffisent.
- Critères complétés par l'efficacité (délai d'ouverture d'un accès la nuit), si les trois critères demandés sont traités.
- Référentiel de l'audit limité à l'ISO/IEC 27001:2022, ou au guide d'hygiène de l'ANSSI, s'il est distingué de la politique interne.

**Erreurs fréquentes**
- *Méthodologie ou calendrier de l'audit exposés* — non demandés (`JUR-T07`).
- *Essais techniques sur les installations proposés comme diligences* — hors programme, et contraires à la contrainte de production.
- *Critères cités sans ce qui est attendu ni élément probant* (`JUR-T01`) ; *élément probant réduit à une déclaration de l'audité*.
- *Audit des accès confondu avec l'audit légal des comptes* (`ET-34`).
- *Gouvernance et sécurité confondues* (`ET-11`, `JUR-G04`) — juste : COBIT 2019 pour la gouvernance, ISO/IEC 27001:2022 pour la sécurité.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Critères d'audit du SI | sécurité, fiabilité, conformité | F10 § 0 et § 1.1 | notion de cours |
| Facteurs de succès et points de vigilance de l'audit SI | indépendance, compétences, accès aux données, adhésion des audités | F10 § 0 | notion de cours |
| COBIT 2019 (ISACA) | cadre de gouvernance et de management, référentiel d'audit possible | `cobit_2019` ; F09 § 5 | en vigueur |
| ISO/IEC 27001:2022 | mesures de sécurité de référence pour l'audit des accès | `iso_27001_2022` ; F12 § 2 | en vigueur |
