# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 56 — Dossier 2 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 données, modélisation et gouvernance (§ 1 à 4, modèle conceptuel, cardinalités et règles de passage ; § 1 et 6.2, entrepôt, lac et données de référence ; § 8.1 et 8.3, rôles et qualité ; § 8.5, souveraineté et portabilité), F08 décisionnel et visualisation (§ 1, chaîne décisionnelle ; § 2, méthodes d'analyse ; § 5, représentations et biais), F03 architecture et cloud (§ 5.3, réversibilité, portabilité, souveraineté), F14 numérique responsable (§ 3, sobriété ; § 4, PUE et indicateurs ; § 5, cloud et centres de données), glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèle logique exécuté, indicateur, référentiels datés, calculs de tête, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Le référentiel des installations et l'architecture des données | `2.1.b` Modélisation des données (modèles conceptuels, logiques et physiques) ; `2.1.c` Architectures orientées données (datawarehouse, datalake, etc.) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 4 |
| 2.2 L'analyse de l'énergie non produite | `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation ; `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model | 4 |
| 2.3 Les données des éoliennes et la souveraineté d'ESTRAVENT | `2.3.d` Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique | 2,5 |
| 2.4 La sobriété des données de mesure | `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `2.3.b` Étapes du cycle de vie des données : création, stockage, usage, archivage, suppression | 2,5 |
| **Dossier 2 – Organiser et exploiter les données des installations, en garder la maîtrise** |  | **13** |

Répartition indicative : connaissances (modèle conceptuel, règles de passage, entrepôt, lac et données maîtres, chaîne de traitement, analyse prédictive, choix d'une représentation, Big Data, souveraineté, sobriété, transition numérique responsable, PUE et indicateur) environ 2,5 points (la moitié des items 2.1 a-1, 2.1 a-4, 2.1 b-1, 2.2 a-1, 2.2 c-1, 2.2 c-2, 2.3 a-1, 2.3 b-1, 2.4 a-1 et 2.4 b-1, qui mêlent définition et application) ; analyse des annexes et recommandations environ 10,5 points, soit environ 80 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Le référentiel des installations et l'architecture des données (4 points)

**Référence au programme**
- §2.1 – Concevoir l'organisation des données et assurer leur interopérabilité : `2.1.b` « Modélisation des données (modèles conceptuels, logiques et physiques) », modèle conceptuel et modèle logique faits à la main à partir de règles de gestion écrites (six entités, deux associations vers la même entité, une association plusieurs à plusieurs) ; `2.1.c` « Architectures orientées données (datawarehouse, datalake, etc.) », entrepôt, lac, « lakehouse » et référentiel de données maîtres comparés ; `2.1.a` « Structurer et organiser les données […] afin d'en garantir la cohérence, la qualité […] et l'interopérabilité ». Aucune requête ; modèle physique seulement nommé ; aucun chiffrage du projet.

**Annexes mobilisées** : annexe 2.1 (éoliennes et données aujourd'hui, usages attendus, deux options d'architecture, règles de gestion RG1 à RG6) ; annexe 1.1 (trois constructeurs, plateforme de supervision, logiciel de gestion de la maintenance, base de données relationnelle du siège).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Six entités, avec leur identifiant et des attributs élémentaires tirés de RG1 à RG6 ; code unique de l'éolienne et désignation du constructeur distingués ; commune et constructeur traités en attributs, avec une justification | 0,5 |
| a-2 | Associations comporter, relever et équiper, avec leurs cardinalités lues dans les deux sens ; cardinalité 0,1 du composant dans équiper (composant en stock ou en réparation) | 0,5 |
| a-3 | Remplacement relié à l'éolienne (concerner) et deux fois au composant (déposer, poser), avec ses cardinalités ; association plusieurs à plusieurs réaliser avec les intervenants ; rôle de l'historique expliqué | 0,5 |
| a-4 | Règles de passage énoncées ; modèle logique de sept tables, clés primaires, clés étrangères (#), clé étrangère facultative dans Composant, deux clés étrangères vers Composant dans Remplacement, table Realisation à clé composée | 0,5 |
| b-1 | Entrepôt, lac (et « lakehouse ») et référentiel de données maîtres définis et appliqués au cas | 0,5 |
| b-2 | Comparaison des deux options selon trois critères justifiés par les usages de l'annexe 2.1 B | 0,5 |
| b-3 | Recommandation argumentée (option 2, référentiel d'abord, zone structurée pour le reporting) et ses conditions | 0,5 |
| b-4 | Problèmes de nommage et de qualité réglés : code unique et correspondances, liste commune des alarmes, composants mis à jour au remplacement, propriétaire et intendant ; dimensions de la qualité nommées | 0,5 |

**Réponse attendue**

*2.1 a) – Le modèle conceptuel et le modèle logique*

**Le modèle conceptuel** (0,5 pt pour les entités, 0,5 pt pour les associations hiérarchiques, 0,5 pt pour le remplacement) représente les objets de gestion (entités), leurs propriétés et leurs liens (associations), avec des cardinalités qui traduisent les règles de gestion, indépendamment de toute technique (F07 § 1 et 2). Les identifiants sont soulignés.

Entités et attributs :
- **Parc** (<u>code_parc</u>, nom_parc, commune, region, date_mise_service) (RG1) ;
- **Modele** (<u>code_modele</u>, designation_modele, constructeur, puissance) (RG3) ;
- **Eolienne** (<u>code_eolienne</u>, num_position, designation_constructeur) (RG2) ;
- **Composant** (<u>num_serie</u>, type_composant) (RG4) ;
- **Remplacement** (<u>id_remplacement</u>, date_remplacement, motif) (RG5) ;
- **Intervenant** (<u>code_intervenant</u>, nom_intervenant, categorie) (RG6).

Le **code de l'éolienne** est attribué par ESTRAVENT et vaut pour toutes ses applications ; la **désignation du constructeur** (« 41207 », « CSV-T03 », « C-7731 ») n'en est qu'un attribut : c'est la réponse aux cinq systèmes de nommage de l'annexe 2.1 A. La commune et la région restent des attributs du parc, et le constructeur un attribut du modèle : les règles de gestion ne leur donnent aucune propriété propre (F07 § 2).

| Association | Entités et cardinalités | Lecture (règle de gestion) |
|---|---|---|
| comporter | Parc **1,n** — Eolienne **1,1** | un parc compte au moins une éolienne ; une éolienne appartient à un seul parc (RG1, RG2) |
| relever | Eolienne **1,1** — Modele **0,n** | une éolienne relève d'un seul modèle ; un modèle peut n'équiper aucune éolienne d'ESTRAVENT (RG3) |
| equiper | Composant **0,1** — Eolienne **1,n** | à un moment donné, un composant est monté sur une seule éolienne, ou sur aucune (stock, réparation) ; une éolienne comporte au moins un composant majeur (RG4) |
| concerner | Remplacement **1,1** — Eolienne **0,n** | un remplacement concerne une seule éolienne ; une éolienne peut n'avoir connu aucun remplacement (RG5) |
| deposer | Remplacement **1,1** — Composant **0,n** | un remplacement retire un seul composant ; un composant peut être déposé lors de plusieurs remplacements, ou d'aucun (RG5) |
| poser | Remplacement **1,1** — Composant **0,n** | un remplacement installe un seul composant ; un composant peut être posé lors de plusieurs remplacements, ou d'aucun (RG5) |
| realiser | Remplacement **1,n** — Intervenant **0,n** | un remplacement est réalisé par au moins un intervenant ; un intervenant peut n'en avoir réalisé aucun (RG6) |

Deux points font la qualité du modèle. D'abord, le **remplacement** est relié **deux fois** au composant, par deux associations distinctes, car un même remplacement met en jeu deux composants qui jouent des rôles différents : le déposé et le posé. Ensuite, l'association **equiper** ne dit que l'état présent (où est monté le composant aujourd'hui), alors que les remplacements en gardent l'**historique** : c'est pourquoi le remplacement est relié directement à l'éolienne (concerner), puisque le composant déposé n'est plus monté sur elle après les travaux. Le modèle n'exprime pas, par ses seules clés, que le composant posé est du même type que le composant déposé, ni que le remplacement met à jour l'éolienne du composant posé : ce sont des règles applicatives (valorisé, non exigé).

**Le modèle logique** (0,5 pt) s'obtient par les règles de passage (F07 § 4) :
1. chaque entité devient une table, dont l'identifiant devient la clé primaire et dont les attributs deviennent des colonnes ;
2. pour une association binaire dont une patte a une cardinalité maximale 1 (comporter, relever, equiper, concerner, deposer, poser), l'identifiant de l'entité du côté n migre comme clé étrangère dans la table de l'entité du côté 1 ; elle est toujours renseignée si la cardinalité est 1,1, et peut rester vide si elle est 0,1 (equiper) ;
3. une association dont toutes les pattes ont une cardinalité maximale n (realiser) devient une table dont la clé primaire est composée des identifiants des entités reliées, chacun clé étrangère.

- Parc (<u>code_parc</u>, nom_parc, commune, region, date_mise_service)
- Modele (<u>code_modele</u>, designation_modele, constructeur, puissance)
- Eolienne (<u>code_eolienne</u>, num_position, designation_constructeur, #code_parc, #code_modele)
- Composant (<u>num_serie</u>, type_composant, #code_eolienne)
- Intervenant (<u>code_intervenant</u>, nom_intervenant, categorie)
- Remplacement (<u>id_remplacement</u>, date_remplacement, motif, #code_eolienne, #num_serie, #num_serie_poser)
- Realisation (<u>#id_remplacement, #code_intervenant</u>)

Dans Composant, `#code_eolienne` est **facultative** : elle reste vide pour un composant en stock ou en réparation. Dans Remplacement, les deux associations vers Composant donnent deux clés étrangères vers la même table, qu'il faut nommer différemment : `#num_serie` désigne le composant déposé, `#num_serie_poser` le composant posé. Le modèle physique (types, index sur les clés étrangères, liste fermée des types de composants et des motifs) se déduirait du modèle logique ; il n'est pas demandé. Les noms des intervenants peuvent être des données personnelles (techniciens) : le référentiel s'en tient à ce qui sert à la traçabilité des travaux (minimisation).

*2.1 b) – Entrepôt, lac, données maîtres : comparer et recommander*

**Les définitions** (0,5 pt), appliquées au cas (F07 § 1 et 6.2) :
- un **entrepôt de données** est une base orientée sujet, intégrée, historisée et non volatile, structurée pour l'analyse ; ses données sont contrôlées et transformées au chargement, selon un schéma défini à l'avance : il servirait le reporting mensuel de la disponibilité et de l'énergie non produite ;
- un **lac de données** stocke des données brutes et hétérogènes (mesures, alarmes, documents, photos), dont le schéma n'est défini qu'à la lecture, pour l'exploration et l'analyse ; sans gouvernance, il devient un « marécage » où personne ne retrouve ni ne croit les données. Le **« lakehouse »** de l'option 2 lui ajoute une zone de données structurées et contrôlées, interrogeable comme un entrepôt ;
- un **référentiel de données maîtres** (MDM, *Master Data Management*, à ne pas confondre avec la gestion des terminaux mobiles) gère, dans un référentiel unique et gouverné, les données partagées et stables que toutes les applications utilisent : ici les parcs, les éoliennes, les modèles, les composants et la liste des alarmes ; c'est le référentiel modélisé en a).

**Comparaison selon trois critères** (0,5 pt), parmi les suivants :

| Critère (usage de l'annexe 2.1 B) | Option 1 : entrepôt | Option 2 : lac et référentiel de données maîtres |
|---|---|---|
| **Couverture des usages et variété des données** | sert le reporting (usage 3) et une partie des analyses de la performance (usage 1), sur les moyennes à dix minutes ; ne sert pas la maintenance prédictive (usage 2), qui exige les mesures à la seconde, ni les rapports et les photos | couvre les quatre usages : mesures à la seconde pour la maintenance prédictive, historique long pour le renouvellement (usage 4), documents et photos pour l'analyse des pannes |
| **Volume et évolutivité** | volume faible ; mais chaque nouveau modèle ou constructeur (renouvellement d'ici 2031) oblige à revoir les traitements de chargement | absorbe les volumes à la seconde et des formats nouveaux sans refonte ; en contrepartie, il grossit vite si rien ne limite la conservation (question 2.4) |
| **Qualité et gouvernance** | contrôles au chargement, définitions partagées, chiffres fiables pour le comité de direction ; mais aucun référentiel n'est prévu : l'entrepôt hériterait des cinq systèmes de nommage et des trois listes d'alarmes | le référentiel de données maîtres, tenu par un responsable désigné, traite la cause des problèmes ; la zone structurée garde la fiabilité de l'entrepôt ; la zone brute exige un catalogue et des règles, faute de quoi elle devient un marécage |
| **Délai et compétences** | 12 mois ; compétences décisionnelles classiques | 18 mois ; compétences d'analyse des données à renforcer chez les ingénieurs de la performance |

**Recommandation** (0,5 pt) : l'**option 2**, parce qu'elle seule sert la maintenance prédictive et le renouvellement, deux objectifs du plan « ESTRAVENT 2031 », et parce qu'elle traite la cause des problèmes par le référentiel. Le lac ne remplace pas l'entrepôt : sa zone structurée en joue le rôle pour le reporting mensuel. Il est conseillé de commencer par le **référentiel de données maîtres** et la zone structurée, qui fiabilisent vite le reporting, puis d'ouvrir la zone des mesures à la seconde quand ESTRAVENT en aura obtenu l'accès (question 2.3) et fixé les règles de conservation (question 2.4). Conditions : un propriétaire et des intendants désignés, un catalogue des données du lac, des droits d'accès.

**Les problèmes de nommage et de qualité** (0,5 pt) se règlent dans le référentiel, à la source, plutôt qu'à chaque export :
1. **Les cinq systèmes de nommage – unicité et cohérence.** Chaque éolienne reçoit le code d'ESTRAVENT (RG2) ; le référentiel garde la correspondance avec la désignation de chaque constructeur, de la plateforme de supervision et du logiciel de gestion de la maintenance ; toute donnée qui entre dans le lac y est rattachée par cette correspondance. Les mesures de deux constructeurs deviennent comparables (interopérabilité sémantique, F07 § 7).
2. **Les trois listes d'alarmes – cohérence.** Une liste commune de familles d'alarmes (surchauffe du multiplicateur, survitesse…) est définie, et les 2 500, 1 800 et 3 000 codes des constructeurs y sont rattachés ; elle remplace le tableur des 200 alarmes les plus fréquentes, tenu à la main.
3. **Les composants – exactitude et actualité.** Le référentiel devient la seule source des numéros de série ; chaque remplacement est enregistré dans le logiciel de gestion de la maintenance, numéro de série lu sur la pièce, et met à jour le référentiel (RG5) ; les quatre tableurs disparaissent. Les 30 écarts sur 200 composants contrôlés (15 %) sont corrigés, puis le taux d'écart est suivi à chaque visite.
4. **Les rôles.** La directrice de l'exploitation est propriétaire des données des installations ; les ingénieurs de la performance en sont les intendants ; la DSI exploite le référentiel et le lac.

**Réponses tolérées**
- Constructeur traité en entité (Constructeur, reliée au modèle), si le candidat le justifie, par exemple par les données d'accès et les contrats de l'annexe 2.3 ; commune ou région traitées en entités, avec une justification.
- Un seul intervenant par remplacement (Remplacement 1,1 — Intervenant 0,n, clé étrangère dans Remplacement) si le candidat suppose, et le dit, qu'il ne retient que le responsable des travaux : RG6 prévoit cependant plusieurs intervenants.
- Remplacement modélisé sans l'association concerner, si le candidat retrouve l'éolienne par un autre moyen qu'il explique (attribut historique) ; noms différents pour les deux clés étrangères vers Composant (#num_serie_depose, #num_serie_pose), dès lors qu'elles sont distinguées.
- Notation Merise ou « pattes de corbeau », si elle est lisible (`JUR-T10`).
- Recommandation de l'option 1 complétée d'un référentiel de données maîtres, si le candidat montre qu'elle renonce à la maintenance prédictive ou la reporte, et le justifie par le délai.
- Autres critères justifiés (sobriété, sécurité, coût complet sans chiffrage).

**Erreurs fréquentes**
- *Modèle conceptuel et modèle logique confondus* (`ET-23`) — clés étrangères dans le modèle conceptuel, ou clé étrangère placée du mauvais côté (#num_serie dans Eolienne).
- *Une seule association entre le remplacement et le composant* — on ne sait plus quel composant a été retiré et lequel a été posé ; ou historique perdu, faute de relier le remplacement à l'éolienne.
- *Cardinalité 1,1 du composant dans equiper* — elle interdit le stock et la réparation (RG4) et rend la clé étrangère obligatoire.
- *Entrepôt et lac confondus* (`ET-24`), ou présentés comme des substituts : le « lakehouse » les combine ; *MDM non précisé* (`ET-13`).
- *Architecture choisie sans référence aux usages* (`JUR-T01`, `JUR-T03`) — comparaison générale sans les quatre usages ni les problèmes de l'annexe 2.1 A.
- *Requêtes écrites* (`JUR-T07`) — la question n'en demande aucune.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle conceptuel, cardinalités, règles de passage, modèle logique | définitions et méthode | F07 § 1 à 4 | notion de cours |
| Entrepôt, lac de données, données de référence et MDM | définitions et choix | F07 § 1 et 6.2 | notion de cours |
| Dimensions de la qualité, propriétaire et intendant, interopérabilité sémantique | définitions | F07 § 7, 8.1 et 8.3 | notion de cours |

---

### 2.2 – L'analyse de l'énergie non produite (4 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique […] » ; `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution » ; `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ». Limites : aucun calcul statistique, aucun développement d'algorithme ; lecture critique des biais, reliée au plan « ESTRAVENT 2031 ».

**Annexes mobilisées** : annexe 2.2 (énergie non produite par cause et par constructeur, disponibilité, multiplicateurs, définition revue en 2025, données manquantes de C, arrêts mal saisis à Castelvérune, affirmation de Mme MONTREVIAU) ; annexe 2.1 (noms des éoliennes, listes d'alarmes, exports à la main, âge des flottes) ; annexe 2.3 (accès aux données à la seconde) ; annexe 1.1 (disponibilité de 95 %, objectif de 97 %).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de traitement présentée ; collecte et nettoyage, chacun avec une limite (données de C manquantes ; arrêts mal saisis, codes d'alarme) | 0,5 |
| a-2 | Structuration et analyse, chacune avec une limite (définition revue en 2025 ; flottes de tailles différentes, causes internes et externes) | 0,5 |
| a-3 | Restitution et décision, avec une limite (ruptures non signalées) ; conclusion | 0,5 |
| b-1 | Deux constats argumentés et chiffrés, avec leur portée | 0,5 |
| b-2 | Troisième constat argumenté et chiffré | 0,5 |
| b-3 | Affirmation appréciée : part réelle de B, bridages et faune, correction des limites, accès aux données, âge et constructeur confondus ; conclusion | 0,5 |
| c-1 | Analyse prédictive définie et appliquée aux multiplicateurs (anticiper, planifier la pièce et la grue) ; deux conditions de réussite | 0,5 |
| c-2 | Deux limites appliquées au cas ; représentation visuelle choisie et justifiée (barres empilées par constructeur, rapportées à l'éolienne) | 0,5 |

**Réponse attendue**

*2.2 a) – La chaîne de traitement de l'énergie non produite*

**La chaîne de traitement des données** (0,5 pt avec la collecte et le nettoyage) est la suite des étapes par lesquelles des données brutes deviennent une information utile à la décision : collecte, nettoyage, structuration, analyse, restitution (F08 § 1). La valeur se perd à chaque étape mal tenue : une donnée manquante à la collecte n'est pas rattrapée par l'analyse. Pour l'énergie non produite :

| Étape | Ce que fera la chaîne | Limite traitée |
|---|---|---|
| **Collecte** | chargement automatique, dans le lac, des moyennes à dix minutes, des alarmes, des interventions du logiciel de gestion de la maintenance et des données météorologiques ; contrôle d'exhaustivité (chaque éolienne a ses 144 valeurs par jour), avec une alerte en cas de trou | les données de C de janvier et février 2026 n'ont jamais été reçues, sans que personne ne s'en aperçoive : environ 10 GWh manquent ; les exports à la main de l'annexe 2.1 A disparaissent |
| **Nettoyage** | chaque arrêt reçoit une cause selon des règles écrites : rapprochement des codes d'alarme de la liste commune, contrôle des arrêts « pannes » par le calendrier des arrêts pour la faune et des demandes de bridage ; journal des corrections | à Castelvérune, environ 10 GWh d'arrêts pour les chauves-souris sont saisis comme des pannes depuis 2025 ; les trois listes d'alarmes ne permettent pas de comparer les pannes des constructeurs |
| **Structuration** | rattachement de chaque donnée au référentiel (éolienne, parc, modèle, constructeur, âge) ; nomenclature des causes écrite et datée ; table de correspondance qui recalcule 2024 selon la définition de 2025 | la définition revue en 2025 déplace environ 5 GWh de la maintenance programmée vers les pannes : 2024 n'est pas comparable aux années suivantes |
| **Analyse** | comparaisons par éolienne ou par MW, et non en valeur totale ; séparation des causes internes (pannes, maintenance, qui pèsent sur la disponibilité) et externes (bridages, faune, givre) ; comparaison des machines d'âge voisin | les flottes n'ont ni la même taille (180, 140, 100 éoliennes) ni le même âge (9, 14 et 6 ans) ; la disponibilité ne mesure pas les arrêts pour bridage ou pour la faune |
| **Restitution et décision** | tableau de bord mensuel du comité de direction, annoté des ruptures et des corrections, avec une note de méthode ; décisions sur la maintenance et sur les autres causes | des chiffres publiés sans ces annotations ont conduit à l'affirmation de Mme MONTREVIAU |

**Conclusion** (0,5 pt avec la restitution) : les limites de l'annexe 2.2 ne sont pas des erreurs de calcul, mais des défauts de collecte, de saisie et de définition, non documentés. La chaîne les traite par des contrôles et des règles écrites, une fois pour toutes, plutôt que par les exports et les tableurs des ingénieurs ; c'est la condition pour que le comité de direction décide sur des chiffres fiables.

*2.2 b) – Trois constats et l'affirmation de Mme MONTREVIAU*

**Trois constats** parmi les suivants (0,5 pt pour deux constats, 0,5 pt pour le troisième : le fait chiffré, son interprétation et sa portée) :
1. **La hausse des pertes vient des contraintes extérieures.** L'énergie non produite passe de 145 à 200 GWh (+ 55 GWh, environ + 40 %). Les bridages demandés par le réseau sont multipliés par 2,5 (de 20 à 50 GWh) ; les arrêts pour la faune passent de 15 à 25 GWh, et de 15 à 35 GWh une fois les arrêts de Castelvérune reclassés. Une fois les limites corrigées, bridages et faune expliquent 50 des 55 GWh de hausse (hors les 10 GWh manquants de C, qui portent le total de 2026 à environ 210 GWh et la hausse à environ 65 GWh ; les deux lectures sont acceptées).
2. **Les pannes et la maintenance sont presque stables, mais le multiplicateur pèse de plus en plus.** À définition constante et après correction de Castelvérune, les pannes passent de 75 à 70 puis 80 GWh, et la maintenance programmée reste à 25 GWh. Pannes et maintenance pèsent 115 GWh en 2026 selon les chiffres publiés, environ 105 GWh corrigés : la moitié environ des pertes. En revanche, la part du multiplicateur dans les pannes passe de 30 % à 40 %, et les remplacements de 6 à 12 par an, dont 8 sur des éoliennes de B ; chaque casse immobilise l'éolienne 30 jours, dont 25 d'attente.
3. **L'écart du constructeur B est réel mais grossi.** B pèse 80 GWh sur 200 (40 %) avec un tiers des éoliennes, soit environ 570 MWh par éolienne contre 420 pour A. Mais 10 GWh de ses pannes sont des arrêts pour la faune : ses pannes réelles sont d'environ 30 GWh, et sa disponibilité d'environ 95 %, comme C. Et C est sous-estimé : avec les 10 GWh manquants, il perd environ 550 MWh par éolienne, presque autant que B.
4. **La disponibilité stagne à 95 % depuis 2025** : l'objectif de 97 % du plan ne porte que sur les pannes et la maintenance, c'est-à-dire sur la moitié environ des pertes ; il ne dit rien des bridages ni des arrêts pour la faune.

**L'affirmation de Mme MONTREVIAU** (0,5 pt) n'est que partiellement fondée, et sa conclusion ne suit pas :
- elle a un fondement : la flotte de B est la plus ancienne (14 ans), et même corrigées, ses pannes rapportées au nombre d'éoliennes restent un peu plus élevées que celles de A ; 8 des 12 multiplicateurs remplacés en 2026 étaient sur des éoliennes de B ;
- « nos pertes viennent de B » est faux : B ne pèse que 40 % des pertes, et une partie de ce chiffre vient des bridages, de la faune et des arrêts mal saisis ; ses pannes et sa maintenance, corrigées, représentent environ 40 GWh, soit environ 20 % des 200 GWh ;
- la hausse des pertes vient des bridages et des arrêts pour la faune, que la maintenance ne réduit pas : ils appellent d'autres analyses, par exemple vérifier que les arrêts ne durent pas plus que prévu, ou mieux anticiper les bridages ;
- l'âge et le constructeur vont de pair : les éoliennes de B sont aussi les plus anciennes, et rien ne prouve que la cause soit le constructeur ou sa maintenance plutôt que l'âge (`ET-26`) ; il faudrait comparer des machines d'âge voisin ;
- « il suffit » ignore les conditions : B refuse de transmettre les mesures à la seconde à l'entreprise de maintenance indépendante (annexe 2.3), et les numéros de série des composants sont faux dans 15 % des cas contrôlés (annexe 2.1 A) ; reprendre la maintenance sans ces données, c'est l'exercer à l'aveugle.

Conclusion : la reprise de la maintenance des éoliennes de B peut faire partie de la réponse, à condition d'obtenir leurs données et de fiabiliser le référentiel des composants, et d'en mesurer l'effet avant et après, sur des machines comparables ; mais la moitié des pertes, et l'essentiel de leur hausse, relèvent d'autres causes.

*2.2 c) – L'analyse prédictive des multiplicateurs et la représentation*

**L'analyse prédictive** (0,5 pt avec les deux conditions) estime ce qui va probablement se produire à partir de l'historique et de facteurs explicatifs, avec une marge d'incertitude ; elle se distingue de l'analyse descriptive, qui dit ce qui s'est passé, et de l'analyse exploratoire, qui recherche des profils ou des anomalies (F08 § 2). Pour les multiplicateurs, elle repérerait, à partir des vibrations, des températures et de la pression d'huile mesurées à la seconde, les signes de dégradation quelques semaines avant la casse. ESTRAVENT pourrait alors commander la pièce et la grue à l'avance, faire les travaux par vent faible, et ramener l'immobilisation de 30 jours vers les cinq jours de travaux ; elle éviterait aussi des dégâts en chaîne sur l'éolienne. C'est un levier direct de l'objectif de disponibilité de 97 %.

**Deux conditions** parmi : l'accès aux mesures à la seconde de toutes les éoliennes, dans un format commun (question 2.3) ; un historique fiable des remplacements et des pannes, pour savoir quelles mesures ont précédé une casse (référentiel de la question 2.1, numéros de série exacts) ; des données propres et bien horodatées ; des compétences d'analyse chez les ingénieurs de la performance et une validation humaine par les techniciens, qui décident de l'intervention.

**Deux limites** parmi (0,5 pt avec la représentation) : les casses sont rares (12 multiplicateurs en 2026), ce qui donne peu d'exemples pour apprendre, d'autant qu'ils se répartissent entre plusieurs modèles ; un modèle construit sur les 60 éoliennes de A de l'essai ne vaut pas forcément pour B et C ; les fausses alertes coûtent une intervention inutile, et les casses non prévues restent possibles ; l'avenir ne reproduit pas forcément le passé (vieillissement, nouveaux modèles, `JUR-D06`). Aucun développement d'algorithme n'est attendu.

**La représentation** : un **graphique en barres horizontales empilées**, une barre par constructeur, dont la longueur est l'énergie non produite **par éolienne** (ou par MW), découpée selon les cinq causes, les causes internes (pannes, maintenance) d'un côté et les causes externes (bridages, faune, givre) de l'autre, avec des couleurs distinctes et une légende. Il montre d'un seul coup d'œil la comparaison entre constructeurs et la composition de leurs pertes, ce que le comité de direction doit voir pour apprécier l'affirmation de Mme MONTREVIAU ; le rapport à l'éolienne évite l'effet de taille des flottes. Il est complété par des colonnes empilées par année, de 2024 à 2026, à définition constante, et annoté des corrections (C, Castelvérune). À éviter : trois graphiques en secteurs, la 3D, les valeurs totales.

**Réponses tolérées**
- Autres étapes (stockage distinct de la structuration, décision et action en étape propre), si chacune porte une limite des annexes.
- Constats différents (givre, disponibilité de A stable), s'ils sont chiffrés et interprétés ; ordres de grandeur arrondis (« environ un tiers », « la moitié »).
- Appréciation plus ou moins sévère de l'affirmation, si elle s'appuie sur les chiffres corrigés et distingue les causes internes et externes.
- Représentation en petits graphiques juxtaposés (un par cause) ou en tableau à cellules colorées, si le choix est justifié par le message et rapporté à l'éolienne.
- Analyse prescriptive évoquée en complément (proposer la date d'intervention), si elle reste une aide à la décision des techniciens.

**Erreurs fréquentes**
- *Corrélation présentée comme causalité* (`ET-26`) — « B a plus de pannes, donc sa maintenance est mauvaise », sans tenir compte de l'âge des machines.
- *Chiffres lus sans leurs limites* (`JUR-D06`) — hausse des pannes de 70 à 90 GWh prise telle quelle ; disponibilité de B lue sans les arrêts mal saisis.
- *Valeurs totales comparées* — 80 GWh pour B contre 45 pour C, sans rapporter au nombre d'éoliennes.
- *Disponibilité confondue avec l'énergie non produite* — les bridages et les arrêts pour la faune ne réduisent pas la disponibilité.
- *Chaîne réduite à un outil* (`ET-05`, `JUR-D02`) — « il suffit d'un logiciel de tableaux de bord ».
- *Calcul statistique ou algorithme* (`JUR-T07`) — régression, coefficients ou modèle à programmer : hors attente.
- *Droit de l'énergie ou de l'environnement* (`JUR-T07`) — discussion des obligations liées aux bridages ou aux arrêts pour la faune : ce sont des faits du cas.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne de traitement et chaîne décisionnelle (collecte, nettoyage, structuration, analyse, restitution) | définitions et méthode | F08 § 1 | notion de cours |
| Analyses descriptive, exploratoire, prédictive | définitions | F08 § 2 | notion de cours |
| Choix d'une représentation, effet de taille, corrélation et causalité | méthode | F08 § 5 | notion de cours |

---

### 2.3 – Les données des éoliennes et la souveraineté d'ESTRAVENT (2,5 points)

**Référence au programme**
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.d` « Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique ». Limites : ni expertise des infrastructures (serveurs, réseaux), ni analyse juridique du Data Act ou des contrats ; repères donnés par l'annexe 2.5, datés.

**Annexes mobilisées** : annexe 2.3 (données à la seconde, conditions des trois constructeurs, extraits des contrats, faits récents) ; annexe 2.1 (base du siège, usages) ; annexe 2.5 (Data Act, référentiel du cloud de confiance) ; annexe 1.1 (systèmes des constructeurs et leurs nuages, plan « ESTRAVENT 2031 »).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Big Data caractérisé (volume, vélocité, variété, véracité, valeur) et appliqué aux données à la seconde, avec les chiffres de l'annexe 2.3 | 0,5 |
| a-2 | Limites de la base relationnelle du siège (saturation, schéma fixe, volumes sans commune mesure) et ce qu'il faut à la place | 0,5 |
| b-1 | Enjeux de localisation et d'accès (nuage hors de l'Union européenne pour C, moyennes à dix minutes seulement, formats propres), souveraineté distinguée de la seule localisation | 0,5 |
| b-2 | Enjeux de coût et de liberté de choisir la maintenance (abonnement de A, refus de B, fin des contrats), reliés au plan | 0,5 |
| b-3 | Trois mesures précises, mobilisant en principe le Data Act et le référentiel du cloud de confiance | 0,5 |

**Réponse attendue**

*2.3 a) – Le Big Data et les données à la seconde*

**Le Big Data** (0,5 pt avec l'application) désigne des ensembles de données dont le volume, la vitesse de production et la variété dépassent les capacités des outils de gestion classiques ; on le caractérise par cinq « V » : volume, vélocité, variété, véracité, valeur (F07 § 0). Les données à la seconde des éoliennes en relèvent :
- **volume** : environ 150 To par an, soit plus de dix fois tout le contenu de la base du siège (12 To), chaque année ;
- **vélocité** : 300 variables à la seconde pour 420 éoliennes, soit plus de 100 000 valeurs par seconde, en continu, jour et nuit ;
- **variété** : mesures, alarmes codées différemment par chaque constructeur, formats propres aux trois constructeurs, auxquels s'ajoutent rapports, photos et données météorologiques ;
- **véracité** : capteurs défaillants, trous de transmission (données de C de janvier et février 2026), horloges à synchroniser ;
- **valeur** : maintenance prédictive, analyses de la performance, études de renouvellement, c'est-à-dire la disponibilité et la production futures d'ESTRAVENT.

**La base relationnelle du siège ne peut pas les accueillir** (0,5 pt) : conçue pour des données structurées selon un schéma fixé à l'avance, sur un serveur unique, elle est déjà occupée à 95 % avec 12 To, et l'extraction d'une année de mesures d'un parc prend une nuit ; les seules mesures à la seconde de 60 éoliennes de A l'ont fait tripler en deux ans. Les données à la seconde des 420 éoliennes exigent un stockage réparti, extensible, qui accepte des données brutes dont le schéma est défini à la lecture : c'est le lac de la question 2.1. Le Big Data ne justifie pas pour autant de tout garder (question 2.4).

*2.3 b) – Souveraineté, dépendance et trois mesures*

**La souveraineté numérique** est la capacité d'une organisation à maîtriser ses données : leur localisation, le droit qui s'applique à qui les héberge, l'accès qu'elle en a et sa dépendance envers ses fournisseurs (F07 § 8.5 ; F03 § 5.3). Les données des éoliennes sont produites par les machines d'ESTRAVENT, sur ses parcs, mais elle ne les détient pas :

- **localisation** (0,5 pt avec l'accès) : les données de C sont stockées, hors de l'Union européenne, chez un fournisseur dont le siège est hors de l'Union européenne, dans des pays que le contrat ne précise pas, et le contrat permet à C de les héberger n'importe où ; elles peuvent être soumises à des lois extra-européennes qui permettent à des autorités étrangères d'y accéder. La localisation dans l'Union européenne des données de A et de B ne suffit pas : la souveraineté tient aussi au droit applicable et à la dépendance (`ET-37`) ;
- **accès** : ESTRAVENT ne reçoit que les moyennes à dix minutes de 80 des 300 variables ; les mesures à la seconde lui sont inaccessibles chez B, consultables sans export chez C, extraites en quinze jours, dans des formats propres à chaque constructeur et impossibles à comparer ;
- **coût** (0,5 pt avec la maintenance) : A fait payer l'accès aux données des machines d'ESTRAVENT, 500 € par éolienne et par an, soit 30 k€ par an pour l'essai sur 60 éoliennes et 90 k€ par an pour ses 180 éoliennes : une rente sur des données qu'ESTRAVENT produit ;
- **liberté de choisir la maintenance** : B refuse de transmettre les données à un prestataire de maintenance concurrent, alors que 40 de ses éoliennes sortent en 2027 de son contrat et que le plan prévoit qu'ESTRAVENT en assure l'entretien ; à la fin du contrat, B ferme l'accès au portail sans rien prévoir pour la restitution des données, et C ne prévoit rien : l'historique des machines, qui est un patrimoine d'ESTRAVENT, peut être perdu. La détention des données verrouille ainsi le choix du mainteneur et contrarie deux objectifs du plan, la disponibilité de 97 % et la maîtrise des données.

**Trois mesures** parmi (0,5 pt) :
1. **Des clauses de données dans les contrats** : à chaque renouvellement ou avenant, et dans les contrats d'achat des éoliennes du renouvellement, exiger l'accès à toutes les données à la seconde, sans frais, dans un format ouvert et documenté, leur transmission au prestataire de maintenance désigné par ESTRAVENT, leur localisation dans l'Union européenne et leur restitution à la fin du contrat. Le Data Act, applicable depuis le 12/09/2025, donne en principe à l'utilisateur d'un produit connecté l'accès aux données que génère son utilisation et la possibilité de les faire transmettre à un tiers de son choix ; pour les éoliennes mises sur le marché après le 12/09/2026, ces données doivent être accessibles par défaut : c'est un levier de négociation, dont la portée exacte est à faire vérifier par les juristes, sans analyse juridique ici.
2. **Collecter les données à la source** : dans chaque parc, un équipement de collecte appartenant à ESTRAVENT lit les données de l'automate et les envoie directement au lac d'ESTRAVENT, sans passer par le nuage du constructeur, en accord avec les constructeurs pour ne pas compromettre la garantie des machines et en sécurisant cette connexion (sans détail technique).
3. **Héberger le lac selon les critères du cloud de confiance** : un hébergeur dans l'Union européenne qui réponde aux trois piliers du référentiel du Cigref, la sécurité, l'immunité aux lois extra-européennes et la maîtrise de la dépendance (réversibilité et portabilité exigibles par contrat, le Data Act facilitant en principe le changement de fournisseur) ; et demander à C de rapatrier ses données dans l'Union européenne, ou les rapatrier par la mesure 2.
4. **Garder la main sur le sens des données** : le référentiel de données maîtres (question 2.1) et la liste commune des alarmes appartiennent à ESTRAVENT et ne dépendent d'aucun constructeur ; un inventaire des données détenues par des tiers, avec leur propriétaire, et un indicateur de la part des éoliennes dont ESTRAVENT reçoit les données à la seconde.

**Réponses tolérées**
- Trois « V » seulement (volume, vélocité, variété), s'ils sont appliqués aux chiffres de l'annexe ; ou une autre caractéristique pertinente, justifiée.
- Une offre qualifiée SecNumCloud évoquée pour l'hébergement du lac, si le candidat la présente comme une exigence possible, non obligatoire, et la relie à l'immunité aux lois extra-européennes.
- D'autres mesures précises et rattachées à l'annexe 2.3 (clause de réversibilité testée, comité de suivi des données avec les constructeurs).

**Erreurs fréquentes**
- *Souveraineté réduite à la localisation* (`ET-37`) — « les données de A et B sont en Europe, donc il n'y a pas de problème ».
- *Analyse juridique* (`JUR-T07`) — discussion de la validité des clauses de B ou de la portée exacte du Data Act : non demandée.
- *Big Data défini sans les chiffres* (`JUR-T01`) — les cinq « V » récités sans les 150 To, les 300 variables à la seconde ni les formats des constructeurs.
- *Mesures d'infrastructure détaillées* (`JUR-T12`) — équipements de collecte ou hébergement décrits techniquement : hors attente.
- *Monétisation des données* (`JUR-T07`) — la question porte sur la maîtrise des données, pas sur leur vente.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Big Data (volume, variété, vélocité, véracité, valeur) | définition | F07 § 0 | notion de cours |
| Souveraineté numérique, réversibilité, portabilité | définitions | F07 § 8.5 ; F03 § 5.3 | notion de cours |
| Règlement (UE) 2023/2854 (Data Act) : accès aux données des produits connectés, transmission à un tiers, changement de fournisseur de services en nuage | principe donné en annexe 2.5 | `data_act` / F07 § 8.5 | applicable depuis le 12/09/2025 |
| Référentiel du cloud de confiance du Cigref | trois piliers, en principe | `cigref_cloud_confiance` / F03 § 5.3 | publié (V1 du 27/05/2021 ; V2 disponible) |

---

### 2.4 – La sobriété des données de mesure (2,5 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété », politique de sobriété des données décidée et contrôlée dans la gouvernance du SI ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) », choix d'un centre de données ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI », un indicateur à cinq champs ; §2.3 `2.3.b` « Étapes du cycle de vie des données […] », durées de conservation, stockage lent et purges. Limites : aucun calcul d'empreinte, aucun cadre de durabilité ; durabilité intégrée à la gouvernance, et non ajoutée.

**Annexes mobilisées** : annexe 2.4 (stockage actuel, journaux de consultation, projet de lac, deux offres de centre de données) ; annexe 2.1 (usages attendus, option 2) ; annexe 2.3 (150 To par an à la seconde) ; annexe 1.1 (organigramme, plan « ESTRAVENT 2031 »).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Sobriété définie ; granularité et durées fixées pour chaque catégorie de données, justifiées par les usages et les journaux de consultation | 0,5 |
| a-2 | Copies proportionnées ; qui décide et qui fait respecter (propriétaire, instance de gouvernance, DSI) ; effet sur les volumes | 0,5 |
| b-1 | Stratégie de transition numérique responsable définie ; offres comparées selon au moins trois critères (efficacité énergétique et PUE, eau et chaleur, renouvellement du matériel, origine de l'électricité, transparence) | 0,5 |
| b-2 | Conclusion argumentée : offre 1, sobriété d'abord, exigences contractuelles | 0,5 |
| c-1 | Un indicateur complet (formule, source, fréquence, cible, axe), relié au lac et à la politique de sobriété | 0,5 |

**Réponse attendue**

*2.4 a) – La politique de sobriété des données de mesure*

**La sobriété numérique** (0,5 pt avec la granularité et les durées) consiste à interroger le besoin avant de chercher l'efficacité : ne produire, ne garder et ne copier que les données qui servent un usage, pendant le temps où elles le servent ; elle ne se réduit pas à une économie d'énergie (F14 § 3 ; `ET-12`). Le projet de lac va à l'inverse : 450 To par an copies comprises, soit 2 250 To en cinq ans, contre 36 To aujourd'hui, pour des mesures dont 90 % des consultations portent sur les deux dernières années.

| Données | Granularité conservée | Durée | Copies |
|---|---|---|---|
| Référentiel des installations | complet | vie de l'éolienne, historique des remplacements compris | trois, sur des sites distincts : petit volume, donnée critique |
| Moyennes à dix minutes (80 variables) | dix minutes | vie du parc, pour les études de renouvellement (usage 4) ; au-delà de deux ans, stockage lent et peu consommateur | deux, sur deux sites distincts (et non deux salles du même siège) |
| Mesures à la seconde | la trentaine de variables utiles à la maintenance prédictive, et non les 300 | treize mois glissants, pour couvrir toutes les saisons ; au-delà, seules sont gardées les semaines qui précèdent chaque panne ou alarme majeure, pour apprendre les modèles, pendant la vie du composant | une seule pour les mesures récentes, dont la perte n'empêcherait que des analyses ; deux pour les extraits liés aux pannes |
| Exports des ingénieurs | — | supprimés : les ingénieurs travaillent directement dans le lac | aucune |

Ordre de grandeur : une trentaine de variables sur 300 représente environ 15 To par an au lieu de 150 ; gardées treize mois en une copie, elles occupent de l'ordre de 15 To, au lieu des 450 To ajoutés chaque année.

**Qui décide et qui fait respecter** (0,5 pt avec les copies) : la politique est proposée par la direction de la performance et des systèmes d'information, avec la directrice de l'exploitation, propriétaire des données des installations, puis validée par le comité de direction, qui l'inscrit dans la gouvernance du SI et dans sa démarche de durabilité, et non comme un ajout. Les ingénieurs de la performance, intendants des données, justifient toute exception (une étude qui demande de garder davantage) ; la DSI applique les règles (purges automatiques et journalisées, passage au stockage lent) et publie chaque trimestre les volumes et la consommation ; la politique est revue chaque année au regard des usages réels (journaux de consultation).

*2.4 b) – Les deux offres de centre de données*

**Une stratégie de transition numérique responsable** (0,5 pt avec la comparaison) est une démarche planifiée qui inscrit la réduction de l'empreinte environnementale du SI dans sa stratégie et sa gouvernance : la sobriété d'abord, puis l'efficacité des équipements et des centres de données, des choix d'hébergement fondés sur l'énergie, l'eau, la chaleur et la durée de vie du matériel, et une mesure suivie dans le temps (F14 § 3 et 5). Au regard de cette stratégie :

| Critère | Offre 1 | Offre 2 |
|---|---|---|
| **Efficacité énergétique** | PUE de 1,2 : 360 MWh pour le même besoin | PUE de 1,5 : 450 MWh, soit 90 MWh de plus (un quart) |
| **Origine de l'électricité** | réseau | réseau, et électricité solaire achetée pour la moitié : un point favorable, mais qui ne réduit pas la consommation, sur un réseau français déjà peu émetteur ; à ne pas surestimer |
| **Eau et chaleur** | refroidissement par l'air ; chaleur cédée à un réseau de chaleur | environ 5 000 m³ d'eau par an ; chaleur perdue |
| **Matériel** | serveurs renouvelés tous les sept ans : moins de fabrication, souvent le premier poste de l'empreinte (`ET-38`) | tous les quatre ans |
| **Soutien à la sobriété** | stockage à deux niveaux, adapté aux données anciennes peu consultées ; son économie d'énergie s'ajoute aux 360 MWh, estimés sans elle | tout sur disques rapides |
| **Transparence** | consommation et PUE mensuels, propres aux équipements d'ESTRAVENT : de quoi construire l'indicateur de c) | PUE annuel de l'ensemble du centre, inutilisable pour suivre le lac |

Le PUE ne mesure que l'efficacité du bâtiment : il ne dit rien de l'origine de l'électricité, de l'eau ni de la fabrication des serveurs (F14 § 4).

**Conclusion** (0,5 pt) : l'offre 1 l'emporte sur presque tous les critères, pour un prix voisin et une même localisation en France. Mais le premier levier reste la politique de sobriété de a) : héberger 450 To par an dans le meilleur centre de données accroît encore l'empreinte. Il est recommandé de retenir l'offre 1 avec la politique de sobriété, et d'inscrire dans le contrat la communication mensuelle de la consommation et du PUE, la durée de renouvellement des serveurs et les conditions de réversibilité.

*2.4 c) – Un indicateur de l'impact environnemental du lac*

**L'indicateur** (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Consommation électrique du lac | somme des consommations mensuelles des équipements du lac × PUE du mois (en MWh par an) | rapport mensuel de l'hébergeur (offre 1) | mensuelle, cumul annuel présenté au comité de direction | en baisse chaque année, et jamais au-dessus de la consommation de la première année, malgré l'arrivée des nouveaux parcs | environnement (ESG) |

Il mesure directement ce que la politique de sobriété cherche à réduire, et il est disponible chaque mois grâce à l'offre 1 ; il ne couvre ni la fabrication des serveurs ni l'eau, que d'autres indicateurs pourraient suivre.

**Réponses tolérées**
- Autres durées justifiées par les usages (deux ans pour la seconde, si le candidat le justifie par les journaux de consultation) ; mesures à la seconde agrégées à la minute au lieu d'être supprimées.
- Politique décidée par un comité des données ou un comité du numérique responsable, si le propriétaire des données y est associé et si l'application est contrôlée.
- Offre 2 recommandée, si le candidat le justifie par un critère qu'il explicite et qu'il discute les autres (rare).
- Autre indicateur complet : consommation par téraoctet stocké, volume stocké copies comprises, part des données en stockage lent, durée moyenne de renouvellement des serveurs ; PUE accepté s'il en dit les limites.

**Erreurs fréquentes**
- *Sobriété confondue avec l'économie d'énergie* (`ET-12`) — choisir le centre de données le plus efficace sans réduire les volumes.
- *Empreinte réduite à l'électricité* (`ET-38`) — oubli de la fabrication des serveurs et de leur durée de vie, ou de l'eau.
- *PUE présenté comme la mesure de l'empreinte* — il ne mesure que l'efficacité du bâtiment.
- *Durabilité en ajout marginal* — politique sans propriétaire, sans instance ni contrôle.
- *Calcul d'empreinte ou chiffre non sourcé* (`JUR-T07`) — tonnes de CO2 calculées ou ordres de grandeur nationaux inventés : non demandés.
- *Indicateur incomplet* (`ET-18`) — indicateur sans formule, sans source ou sans cible.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Sobriété numérique, Green IT | définitions | F14 § 3 | notion de cours |
| PUE et indicateurs de mesure ; limites du PUE | définitions | F14 § 4 | notion de cours |
| Cloud et centres de données, chaleur, eau, renouvellement du matériel | méthode | F14 § 5 | notion de cours |
| Fiche d'indicateur à cinq champs | méthode | F08 § 3 | notion de cours |
