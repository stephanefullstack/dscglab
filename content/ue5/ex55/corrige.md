# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 55 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique (§ 1, alignement et SAM ; § 3.1, schéma directeur ; § 4, organisation de la DSI et relations avec la direction générale et les métiers), F02 gouvernance et référentiels (§ 1, norme, référentiel et solution ; § 3, COBIT 2019 ; § 5, ITIL ; § 6, comitologie), F03 architecture et urbanisation (§ 1, urbanisation ; § 3, interopérabilité et intégration), F04 ESN et contrats (§ 4, clauses critiques ; § 5, gouvernance de la relation ; § 6, risques de la relation), F05 projets et changement (§ 7, conduite du changement), F06 connaissances (§ 1, connaissances tacites et explicites, SECI ; § 2, dispositif de gestion des connaissances), glossaire, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Les effets du plan sur le système d'information et sa planification stratégique | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.c` Méthodologies de planification stratégique du SI | 3,5 |
| 1.2 Le rapprochement de l'informatique de gestion et de l'informatique de conduite | `1.2.b` Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers ; `1.3.c` Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle | 4 |
| 1.3 La renégociation du contrat de l'ESN | `1.4.d` Méthodologie de négociation contractuelle et analyse des risques ; `1.4.a` Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques ; `1.4.e` Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) | 3 |
| 1.4 La transmission des savoirs du développement des parcs | `1.6.b` Architecture fonctionnelle des systèmes de knowledge management ; `1.6.a` Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle ; `1.6.c` Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) ; `1.6.e` Leviers d'appropriation et de transformation des pratiques professionnelles | 3,5 |
| **Dossier 1 – Préparer l'évolution de la stratégie et de l'organisation du système d'information, la renégociation d'un contrat et la transmission des savoirs** |  | **14** |

Répartition indicative : connaissances (planification stratégique du SI, modèles d'organisation de la fonction SI, urbanisation, connaissances tacites et explicites et modèle SECI) environ 2 points (items 1.1 b-1, 1.2 a-1, 1.2 b-1 pour moitié, 1.4 a-1, et les définitions incluses dans les autres items) ; analyse des annexes et recommandations environ 12 points, soit environ 85 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – Les effets du plan sur le système d'information et sa planification stratégique (3,5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.c` « Méthodologies de planification stratégique du SI ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 1.2 (fin des prix garantis, méthodes actuelles, autres évolutions du plan, absence de plan stratégique du SI, témoignages), 1.1 (plan « ESTRAVENT 2031 », ventes, effectif, système d'information, organigramme) et 1.6 (SAM, COBIT 2019).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Fonctions nouvelles tirées de l'annexe 1.2 : prévision mise à jour plusieurs fois par jour, programme de production envoyé à l'agrégateur, gestion du portefeuille de contrats d'achat direct, facturation horaire et justification des écarts, maintenance en propre (planification, pièces, historique des machines), intégration de nouveaux modèles d'éoliennes, pilotage des batteries | 0,5 |
| a-2 | Données et délais : données horaires par parc (production, comptage, profil, prix), passage du mensuel et du quotidien à l'infra-journalier, voire au temps réel pour les batteries ; changement d'échelle chiffré (3 à 15 contrats, 720 valeurs horaires par contrat et par mois, 10 jours de facturation par mois qui deviendraient 50) ; données de la conduite nécessaires à la gestion | 0,5 |
| a-3 | Deux orientations du SI, chacune justifiée par un objectif du plan et par un constat de l'annexe | 0,5 |
| a-4 | Troisième orientation, même exigence ; orientations formulées comme des choix de stratégie du SI au service du plan, et non comme des achats de logiciels | 0,5 |
| b-1 | Planification stratégique du SI définie (plan pluriannuel, trois à cinq ans, qui traduit la stratégie de l'organisation en orientations, cible, trajectoire et moyens, révisé périodiquement), distinguée d'un plan de projet ; horizon proposé calé sur le plan (2028-2031) | 0,5 |
| b-2 | Étapes de la démarche (cadrage, diagnostic, besoins et orientations, cible, trajectoire, validation et revue) et acteurs du cas (présidente-directrice générale, comité de direction, directions métiers, DSI et cellule supervision, utilisateurs, conseil d'administration informé) | 0,5 |
| b-3 | Arbitrages : instance qui arbitre, critères tirés du plan et des contraintes (contribution aux objectifs, continuité de la conduite, dépendances, capacité à faire), projets lancés par les directions ramenés dans la démarche, revue annuelle | 0,5 |

**Réponse attendue**

*1.1 a) – Les effets du plan sur le système d'information et trois orientations*

Le plan « ESTRAVENT 2031 » transforme un producteur qui vendait 70 % de son électricité à prix garanti, sans avoir à prévoir ni à facturer finement, en un vendeur qui porte lui-même le risque de ses ventes. L'alignement stratégique, mise en cohérence permanente de la stratégie du SI avec celle de l'organisation (modèle SAM, annexe 1.6), oblige à tirer de ce changement ce que le SI devra faire.

**Fonctions nouvelles** (0,5 pt) :
- **prévoir** la production de chaque parc plusieurs fois par jour, et non plus une fois par jour à 10 heures pour le lendemain ;
- **programmer** les ventes : envoyer à l'agrégateur, chaque jour, un programme de production juste, puisque « plus ce programme est juste, mieux nous vendons » et que l'énergie manquante est rachetée aux frais d'ESTRAVENT ;
- **gérer un portefeuille de contrats d'achat direct** : volumes engagés, prix, échéances, écarts entre le profil promis et la production, pour 15 contrats environ en 2031 contre 3 aujourd'hui ;
- **facturer heure par heure** et **justifier** chaque écart auprès de l'industriel : aujourd'hui, deux jours pour répondre à une question ;
- **entretenir les éoliennes** sorties des contrats des constructeurs (60 en 2027, environ 200 en 2031) : planifier les interventions, gérer les pièces de rechange, donner aux techniciens, sur leur tablette, l'historique de la machine et les alarmes du jour, faire travailler des sous-traitants ;
- **accueillir de nouveaux modèles** d'éoliennes, parfois d'un autre constructeur, dans dix parcs renouvelés, sans refaire la supervision ;
- **piloter les batteries** des deux sites à l'essai à partir de 2028, à partir des prévisions et des prix : une fonction qui relie directement la vente de l'électricité et la conduite des installations.

**Données et délais** (0,5 pt) :
- **données** : production horaire de chaque parc, relevés de comptage, profils et prix de chaque contrat, prix du marché, historique des machines, stocks de pièces ; plusieurs de ces données naissent dans l'informatique de conduite (production, alarmes) et servent l'informatique de gestion (facturation, maintenance) : la séparation des deux mondes devient un obstacle ;
- **délais** : le SI passe du rythme mensuel (comptage, facturation) et quotidien (prévision) au rythme **infra-journalier**, voire au quasi temps réel pour les batteries ; la facture doit partir et se justifier vite après la fin du mois ;
- **changement d'échelle** : environ 720 valeurs horaires par contrat et par mois, soit environ 10 800 valeurs par mois pour 15 contrats ; avec la méthode actuelle, deux personnes y passent chacune cinq jours par mois, soit 10 jours pour trois contrats, et il en faudrait environ 50 pour quinze ; deux factures refaites en 2026 montrent déjà les limites des tableurs.

**Trois orientations du SI** (0,5 pt pour deux, 0,5 pt pour la troisième) :

| Orientation | Objectif du plan servi | Constat de l'annexe 1.2 |
|---|---|---|
| **1. Doter ESTRAVENT d'un SI de la vente de l'électricité** : prévision infra-journalière, programme de production transmis à l'agrégateur sans ressaisie, portefeuille des contrats, facturation horaire produite et justifiable à partir de données de référence | 40 % de la production vendue par contrats d'achat direct en 2031 | prévisions reçues une fois par jour ; un tableur par contrat ; factures préparées à la main ; deux factures refaites ; trois contrats aujourd'hui, environ quinze en 2031 |
| **2. Relier la conduite des installations et la maintenance** : logiciel de gestion de la maintenance relié à la supervision, outils mobiles des techniciens, sous-traitants intégrés aux mêmes outils, historique des machines partagé | disponibilité portée de 95 % à 97 % ; maintenance reprise aux constructeurs | maintenance de 60 puis 200 éoliennes ; besoin d'historique, d'alarmes et de pièces sur la tablette du technicien (témoignage de Mme MONTREVIAU) |
| **3. Gouverner et urbaniser un seul système d'information, de la gestion à la conduite**, capable d'accueillir de nouveaux modèles d'éoliennes et les batteries, et dont les données et la sécurité sont maîtrisées | maîtrise des données et de la sécurité des installations ; 2 500 MW en 2031 | aucun plan stratégique du SI ; projets lancés par chaque direction ; batteries qui relient vente et conduite ; renouvellement de dix parcs ; plan adopté « sans un mot sur le système d'information » |

Ces orientations sont des choix de stratégie : elles disent ce que le SI doit permettre à ESTRAVENT de faire, avant tout choix de logiciel.

*1.1 b) – La démarche de planification stratégique du système d'information*

La **planification stratégique du SI** est la démarche par laquelle une organisation traduit sa stratégie en orientations du SI, en architecture et en organisation cibles, en trajectoire de projets et en moyens, sur un horizon de trois à cinq ans ; elle aboutit à un **schéma directeur** ou plan stratégique du SI, révisé chaque année. Elle se distingue d'un plan de projet, qui organise la réalisation d'un seul projet. Pour ESTRAVENT, l'horizon naturel est **2028-2031**, celui du plan « ESTRAVENT 2031 », pour un plan élaboré au second semestre 2027 (0,5 pt).

**Étapes et acteurs** (0,5 pt) :

| Étape | Contenu pour ESTRAVENT | Acteurs |
|---|---|---|
| 1. Cadrage | commanditaire, périmètre (gestion et conduite ensemble), calendrier de six mois environ, instance de pilotage | présidente-directrice générale (commanditaire) ; vous, pilote ; comité de direction |
| 2. Diagnostic de l'existant | applications et échanges des deux mondes, dépendances (constructeurs, ESN), compétences, satisfaction des utilisateurs, coûts en ordre de grandeur, ce qui reste du schéma directeur 2018-2021 | DSI, cellule supervision, contrôle de gestion, utilisateurs clés (chargées de facturation, techniciens, chefs de projet) |
| 3. Besoins et orientations | traduction de chaque objectif du plan en besoins du SI (question a) ; orientations validées | directions de l'énergie, de l'exploitation, du développement, de la construction, financière |
| 4. Cible | architecture urbanisée (question 1.2 b), organisation de la fonction SI (question 1.2 a), principes de données et de sécurité, avec la déléguée à la protection des données | DSI, cellule supervision, directions métiers |
| 5. Trajectoire | grands chantiers ordonnés dans le temps, jalons, moyens en ordre de grandeur, risques ; échéances imposées : fin du contrat de l'ESN au 31/12/2027, sortie des 18 parcs jusqu'en 2029, batteries en 2028 | comité de direction |
| 6. Validation et revue | validation par le comité de direction, présentation au conseil d'administration, qui a adopté le plan ; revue annuelle et indicateurs de suivi | présidente-directrice générale, conseil d'administration |

**Arbitrages** (0,5 pt) : ils sont rendus par une instance unique, un comité stratégique du SI présidé par la présidente-directrice générale, qui réunit les directeurs et vous-même (COBIT 2019 range ce travail dans le domaine « aligner, planifier, organiser », annexe 1.6). Les critères viennent du plan et des contraintes du cas : contribution aux quatre objectifs ; continuité de la conduite des installations, jour et nuit ; dépendances entre chantiers (la facturation horaire suppose des données de production et de comptage fiables, les batteries supposent la prévision) ; échéances imposées ; capacité à faire de 22 personnes à la DSI et 8 à la cellule supervision. Les projets que les directions lancent seules (logiciel des contrats de vente, extension du logiciel de maintenance, nouveau système d'information géographique) entrent dans la démarche au lieu d'être engagés à part. Le comité revoit le plan chaque année, et le conseil d'administration est informé de son avancement.

**Réponses tolérées**
- Orientation sur le développement des projets (système d'information géographique, transmission des savoirs) pour atteindre 2 500 MW, si elle est justifiée par un constat ; orientation « données des installations » ou « sécurité de la conduite », si elle est reliée au quatrième objectif du plan.
- Démarche présentée selon les phases du schéma directeur de F01 (cadrage, diagnostic, orientations, cible, plan d'actions, pilotage), si les acteurs sont ceux du cas.
- Horizon de trois ou cinq ans, s'il est justifié et cohérent avec le plan.
- Référence à TOGAF pour le passage de l'existant à la cible, en principe.

**Erreurs fréquentes**
- *Alignement réduit à l'achat d'un logiciel de gestion des contrats ou de prévision* (ET-06 ; `JUR-G02` alignement réduit à un choix technique) — l'orientation dit ce que le SI doit permettre, au service du plan.
- *Effets décrits sans les chiffres de l'annexe 1.2* (`JUR-T08` exploiter toutes les annexes ; `JUR-T03` analyser, ne pas décrire) — le changement d'échelle (3 à 15 contrats, 10 à 50 jours de facturation) est l'argument central.
- *Schéma directeur confondu avec un plan de projet, ou démarche sans acteurs ni arbitrages* (ET-07 ; `JUR-G08` schéma directeur et jalons usuels) — le plan stratégique couvre tout le SI, gestion et conduite.
- *Analyse des règles de vente de l'électricité ou des contrats d'achat direct* (`JUR-T07` répondre à la seule question posée) — l'énoncé les donne comme des faits commerciaux ; aucun droit de l'énergie n'est attendu.
- *Portefeuille de projets classé ou chiffré* (`JUR-T07`) — non demandé.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle d'alignement stratégique (SAM), Henderson et Venkatraman, 1993 | alignement entre stratégie de l'entreprise, stratégie des TI, organisation et infrastructure du SI | `henderson_venkatraman_1993` ; F01 § 1 | modèle théorique |
| COBIT 2019, ISACA | domaine « aligner, planifier, organiser » ; référentiel, ni norme ni logiciel | `cobit_2019` ; F02 § 3 | en vigueur |
| Schéma directeur, planification stratégique du SI | horizon de trois à cinq ans, démarche, arbitrages | F01 § 3.1 ; F02 § 6 | notion de cours |

---

### 1.2 – Le rapprochement de l'informatique de gestion et de l'informatique de conduite (4 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.b` « Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ».
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.c` « Urbanisation des SI, interopérabilité et cohérence inter-organisationnelle ». Limite : « Ne pas réduire l'urbanisation à une vision strictement technique : elle s'inscrit dans une stratégie globale. »

**Annexes mobilisées** : annexes 1.3 (organisation, frictions, échanges avec l'extérieur), 1.1 (effectif, système d'information, organigramme), 1.2 (évolutions du plan) et 1.6 (ITIL, TOGAF).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Quatre modèles présentés avec leur principe, une force et une limite : centralisé, décentralisé, fédéral, bimodal | 0,5 |
| a-2 | Organisation recommandée et justifiée par le cas (continuité de la conduite jour et nuit, proximité du centre de conduite, cohérence de l'ensemble du SI) ; situation actuelle qualifiée (deux informatiques décentralisées qui s'ignorent) | 0,5 |
| a-3 | Rattachement de la cellule supervision, rôles de la DSI (gouvernance, architecture, référentiels, changements, achats) et de la direction de l'exploitation (besoins, priorités, exploitation de la conduite), instance commune ; relations avec la direction générale et les métiers | 0,5 |
| a-4 | Deux frictions de l'annexe 1.3 traitées par la recommandation, avec une mesure concrète pour chacune | 0,5 |
| a-5 | Troisième friction, même exigence | 0,5 |
| b-1 | Urbanisation définie (découpage en zones, quartiers et îlots faiblement couplés, reliés par des échanges maîtrisés, pour faire évoluer le SI avec la stratégie) ; zones proposées, dont une zone d'échange et une zone des référentiels | 0,5 |
| b-2 | Applications des annexes 1.1 et 1.3 placées de façon cohérente dans les zones (dont l'outil des vibrations, le logiciel de maintenance, la prévision, les futurs outils de vente et de pilotage des batteries) | 0,5 |
| b-3 | Deux règles de cohérence des échanges avec l'extérieur, chacune appliquée à une organisation de l'annexe 1.3 | 0,5 |

**Réponse attendue**

*1.2 a) – L'organisation qui rapproche les deux informatiques*

**Les modèles d'organisation de la fonction SI** (0,5 pt) :

| Modèle | Principe | Force | Limite |
|---|---|---|---|
| **Centralisé** | une seule DSI décide et opère pour toute l'organisation | cohérence, sécurité homogène, économies d'échelle | éloignement des métiers, lenteur |
| **Décentralisé** | chaque entité ou direction gère son informatique | proximité, réactivité | doublons, incohérences, sécurité inégale |
| **Fédéral** | une DSI centrale porte la gouvernance, l'architecture, les référentiels et les services communs ; des équipes proches des métiers portent les besoins et l'exploitation de leur domaine | équilibre entre cohérence et proximité | rôles et coordination à clarifier |
| **Bimodal** | deux modes dans la même fonction SI : un mode stable pour le SI cœur, un mode exploratoire et agile pour l'innovation | innover sans fragiliser le socle | « DSI à deux vitesses », tensions culturelles |

**Recommandation** (0,5 pt) : ESTRAVENT vit aujourd'hui une organisation **décentralisée de fait** : la DSI et la cellule supervision ont chacune leur calendrier, leur astreinte et leurs achats, et ne se réunissent jamais. Une centralisation pure, qui fondrait la cellule dans la DSI, éloignerait la conduite du centre de conduite, qui surveille les installations jour et nuit avec une culture de la continuité que la DSI n'a pas. Le modèle recommandé est **fédéral** : la direction de la performance et des SI porte, pour tout le SI, gestion et conduite, la gouvernance, l'architecture, les référentiels, la gestion des changements, les comptes et les achats ; la cellule supervision, équipe proche du métier, reste à l'exploitation et y porte les besoins et l'exploitation de la conduite. Le plan l'exige : facturation, maintenance et batteries ont besoin des données de la conduite.

**Rôles et instance** (0,5 pt) :
- **rattachement** : la cellule supervision reste dans la direction de l'exploitation, au centre de conduite, pour garder la culture de la continuité, l'astreinte et la proximité avec la conduite ; elle reçoit un lien fonctionnel fort avec la direction de la performance et des SI, qui fixe les règles communes (architecture, référentiels, changements, comptes, achats) et en contrôle l'application : c'est le partage des rôles du modèle fédéral ;
- **DSI** : architecture et urbanisation, référentiels, annuaire des comptes, gestion des changements, achats de solutions, sécurité de l'ensemble ;
- **direction de l'exploitation** : maîtrise d'ouvrage de la conduite et de la maintenance (besoins, priorités, recette), responsable de l'exploitation des installations ;
- **instance commune** : un comité du SI de gestion et de conduite, mensuel, où siègent le responsable de la DSI, la responsable de la cellule supervision, le responsable du centre de conduite et un représentant de l'énergie ; il tient le calendrier commun des changements, l'inventaire et les projets qui touchent les deux mondes ;
- **relations avec la direction générale** : les arbitrages remontent au comité stratégique du SI présidé par la présidente-directrice générale (question 1.1 b), pour que la fonction SI, rattachée au directeur financier, pèse dans les choix de l'exploitation et de l'énergie.

**Trois frictions traitées** (0,5 pt pour deux, 0,5 pt pour la troisième) :

| Friction (annexe 1.3) | Ce que change l'organisation recommandée |
|---|---|
| Mise à jour de la messagerie qui coupe pendant deux heures les alarmes du centre de conduite | **gestion des changements commune** (ITIL, annexe 1.6) : tout changement qui touche un service utilisé par la conduite est évalué avec la cellule et le centre de conduite, planifié hors des périodes sensibles, prévenu, avec retour arrière prévu ; à terme, les alarmes ne dépendent plus de la messagerie de bureautique |
| Outil d'analyse des vibrations souscrit seul par l'exploitation, découvert à la facture, chargé à la main | **achats de solutions passés par la fonction SI** : l'exploitation exprime le besoin, la fonction SI vérifie l'intégration, les données et le contrat ; l'outil est relié au reste du SI au lieu de rester isolé |
| Liste des postes reliés aux installations inconnue (40 postes pour la DSI, 55 pour la cellule) | **un inventaire unique**, tenu par un responsable nommé (la cellule supervision), mis à jour à chaque mouvement et revu au comité commun |
| Doubles comptes et 30 comptes de personnes parties encore actifs ; interventions saisies deux fois | **annuaire unique** des personnes, alimenté par les arrivées et les départs, qui ouvre et ferme les comptes des deux mondes ; échange automatique entre le logiciel de maintenance et la plateforme pour suspendre les alarmes |

*1.2 b) – L'urbanisation et la cohérence des échanges avec l'extérieur*

L'**urbanisation** organise le SI, par analogie avec une ville, en **zones**, **quartiers** et **îlots** faiblement couplés, reliés par des échanges maîtrisés, pour qu'il évolue au rythme de la stratégie sans tout reconstruire ; elle s'appuie sur des règles : une donnée de référence a un seul propriétaire, une fonction n'est implantée qu'une fois, les échanges passent par une zone d'échange plutôt que par des liens directs (0,5 pt avec les zones).

**Découpage proposé** (0,5 pt pour le placement) :

| Zone | Quartiers et applications |
|---|---|
| **Gestion** | finance et achats : progiciel de gestion intégré (comptabilité, achats, immobilisations, facturation) ; ressources humaines : paie |
| **Énergie** (vente de l'électricité) | prévision de la production (outil du prestataire) ; programmes de production envoyés à l'agrégateur ; portefeuille des contrats de vente ; calcul de la facturation horaire, qui alimente la facturation du progiciel ; à terme, décision de charge et de décharge des batteries à partir des prévisions et des prix |
| **Conduite des installations** | systèmes de supervision des constructeurs A, B et C et des centrales solaires ; plateforme de supervision du centre de conduite ; à terme, commande des batteries ; postes du centre de conduite |
| **Maintenance et performance des installations** (quartier de la conduite ou zone propre) | logiciel de gestion de la maintenance en mode SaaS, outils mobiles des techniciens ; outil d'analyse des vibrations ; analyses des ingénieurs de la performance |
| **Développement** | système d'information géographique, gestion électronique des documents des projets, gestion des relations avec les propriétaires et les communes, dispositif de connaissances (question 1.4) |
| **Référentiels** | installations (parcs, éoliennes, centrales), tiers et contrats, personnes et comptes (annuaire unique) |
| **Échanges** | point unique d'entrée et de sortie des échanges entre zones et avec l'extérieur |
| Socle commun | messagerie et bureautique en ligne, base des données de production |

La frontière entre la conduite et la maintenance d'une part, l'énergie d'autre part, est la plus sollicitée par le plan : les batteries et la facturation horaire en vivent.

**Deux règles de cohérence des échanges avec l'extérieur** (0,5 pt) :
1. **Tout échange avec une organisation extérieure passe par la zone d'échange, sans courriel ni ressaisie**, et a un responsable désigné. Pour l'**agrégateur**, le programme de production part chaque jour de la zone énergie, tiré de la prévision, au lieu d'un tableur envoyé par courriel ; pour les **sous-traitants de maintenance**, les ordres de travail sortent du logiciel de maintenance et les comptes rendus y entrent directement, au lieu d'être ressaisis.
2. **Chaque échange suit un contrat d'échange** : contenu, format commun propre à ESTRAVENT, identifiants de référence des parcs et des machines, fréquence, responsable de part et d'autre. Pour les **constructeurs A, B et C**, les données de fonctionnement et les alarmes sont traduites au point d'entrée dans le format commun : la plateforme ne dépend plus du format de chaque constructeur, et un parc renouvelé avec un autre constructeur s'intègre sans refaire la supervision.

**Réponses tolérées**
- Modèle centralisé recommandé, si la proximité du centre de conduite et la continuité jour et nuit sont préservées (équipe dédiée, astreinte) ; modèle fédéral avec une composante bimodale pour les projets d'innovation (batteries, prévision), si les deux modes sont bien définis.
- Rattachement hiérarchique de la cellule supervision à la direction de la performance et des SI, avec un lien fonctionnel avec la directrice de l'exploitation et une implantation au centre de conduite, s'il est justifié (cohérence, sécurité) et si le candidat voit que l'organisation se rapproche alors du modèle centralisé.
- Proposition de rattacher la direction de la performance et des SI à la présidente-directrice générale plutôt qu'au directeur financier, si elle est argumentée.
- Autre découpage (zone « pilotage » distincte, maintenance dans la conduite), s'il respecte les principes de l'urbanisation et place toutes les applications citées.
- Autres règles (une seule source de référence pour chaque donnée échangée, un identifiant commun des installations dans tous les échanges, des formats ouverts), si elles sont appliquées à une organisation de l'annexe.

**Erreurs fréquentes**
- *Modèles récités sans recommandation, ou recommandation sans lien avec les frictions* (`JUR-T01` contextualiser ; `JUR-G05` analyser les déséquilibres organisationnels et recommander de façon réaliste).
- *Bimodal confondu avec l'opposition entre informatique de gestion et informatique de conduite, ou fédéral confondu avec décentralisé* (F01 § 8) — le bimodal oppose stabilité et exploration, pas deux domaines.
- *Urbanisation réduite à des serveurs et à des réseaux, ou échanges décrits par leurs normes techniques* (ET-20 ; ET-36 interopérabilité seulement technique ; `JUR-G07`) — aucun détail technique des échanges n'est attendu.
- *Sécurité des accès distants des tiers développée* (`JUR-T07` répondre à la seule question posée) — les frictions sur les postes et les comptes sont traitées ici par l'organisation, pas par une politique de sécurité.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèles d'organisation de la fonction SI | centralisé, décentralisé, fédéral, bimodal ; rattachement du DSI ; relations avec la direction générale et les métiers | F01 § 4 ; F02 § 6 | notion de cours |
| ITIL 4, PeopleCert (ex-AXELOS), 2019, et ITIL (version 5), 2026 | gestion des changements ; référentiel, ni norme ni logiciel | `itil_4`, `itil_5` ; F02 § 5 | en vigueur |
| Urbanisation et intégration | zones, quartiers, îlots ; zone d'échange ; données de référence | F03 § 1 et § 3 | notion de cours |
| The TOGAF Standard, 10e édition (2022), The Open Group | passage de l'architecture existante à la cible, en principe | `togaf_10` ; F02 § 5 | en vigueur |

---

### 1.3 – La renégociation du contrat de l'ESN (3 points)

**Référence au programme**
- §1.4 – Gérer les relations contractuelles et opérationnelles avec les ESN : `1.4.d` « Méthodologie de négociation contractuelle et analyse des risques » ; `1.4.a` « Concevoir, négocier et sécuriser des relations contractuelles avec des prestataires de services numériques (ESN), en tenant compte des enjeux opérationnels et juridiques » ; `1.4.e` « Gouvernance de la relation client-prestataire (pilotage de la prestation, indicateurs de suivi, clauses d'audit) ». Limites : « L'analyse juridique approfondie relève du droit des contrats informatiques et est exclue du programme de l'UE. »

**Annexes mobilisées** : annexes 1.4 (contrat, suivi, constats, position de l'ESN, options) et 1.1 (dépenses du SI, plateforme de supervision).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux risques de la relation, chacun appuyé sur un constat chiffré ou daté de l'annexe 1.4 | 0,5 |
| a-2 | Deux autres risques, même exigence ; les quatre couvrent dépendance, réversibilité, dérive des coûts et perte des savoirs | 0,5 |
| b-1 | Objectifs prioritaires de la négociation, hiérarchisés et reliés aux risques (réversibilité et code source, rétablissement des niveaux de service, transfert des connaissances, maîtrise des coûts) ; position de l'ESN appréciée (hausse de 15 %, soit environ 225 k€ par an, contre une qualité en baisse) | 0,5 |
| b-2 | Deux concessions possibles, avec leur contrepartie ; solution de repli réaliste, qui ne repose pas sur l'acceptation par l'ESN de nos conditions, et son calendrier (décision avant le 30/09/2027, six mois de transfert, échéance du 31/12/2027) | 0,5 |
| c-1 | Gouvernance de la relation : instances (stratégique, de pilotage, opérationnelle), clause d'audit, plan de sortie testé, mesures vérifiées par ESTRAVENT | 0,5 |
| c-2 | Deux indicateurs de suivi complets (formule, source, fréquence, cible, axe), reliés aux constats | 0,5 |

**Réponse attendue**

*1.3 a) – Quatre risques de la relation avec KALVENTIS Services*

| Risque | Constat de l'annexe 1.4 | Effet pour ESTRAVENT |
|---|---|---|
| **Dépendance** à un seul prestataire (0,5 pt avec le suivant) | seule KALVENTIS Services maintient la plateforme du centre de conduite ; code source chez l'ESN, aucune copie chez ESTRAVENT ; propriété des développements spécifiques non précisée | ESTRAVENT négocie en position de faiblesse : l'ESN propose 15 % de hausse sans nouvel engagement de service |
| **Réversibilité** impossible à court terme | aucun plan de réversibilité ; documentation non tenue à jour depuis 2021 ; une autre ESN demanderait six mois de transfert, alors que la décision doit être notifiée avant le 30/09/2027 et que le contrat finit le 31/12/2027 | changer de prestataire dans le délai est impossible sans préparation ; risque de rupture de la maintenance d'un outil vital pour la conduite |
| **Dérive des coûts et de la qualité** (0,5 pt avec le suivant) | évolutions hors forfait multipliées par trois (100 puis 300 k€) ; hausse demandée de 15 %, soit environ 225 k€ de plus par an (1 725 k€ au lieu de 1 500 k€) et 675 k€, près de 0,7 M€, sur trois ans ; dans le même temps, pannes bloquantes rétablies en 4 heures dans 70 % des cas pour une cible de 95 %, anomalies corrigées à temps dans 60 % des cas pour 90 % ; pénalités jamais réclamées ; aucun comité depuis janvier 2025, chiffres de l'ESN non vérifiés | ESTRAVENT paie plus pour un service qui se dégrade, sans moyen de le mesurer elle-même |
| **Perte des savoirs** | deux ingénieurs seuls connaissent le code, dont l'un quittera l'ESN en 2028 ; la moitié des ingénieurs affectés a été remplacée en 2026 (3 sur 6) | au départ de cet ingénieur, ni l'ESN ni ESTRAVENT ne sauront faire évoluer la plateforme, au moment où arrivent de nouveaux modèles d'éoliennes et les batteries |

*1.3 b) – La préparation de la négociation*

**Objectifs prioritaires**, du plus important au moins important (0,5 pt) :
1. **Retrouver la maîtrise de la plateforme** : remise d'une copie du code source et de la documentation à jour, attribution à ESTRAVENT des droits sur les développements spécifiques (en principe, sans analyse juridique), plan de réversibilité avec un test ; c'est la condition de toute négociation future.
2. **Organiser le transfert des connaissances** avant le départ de l'ingénieur en 2028 : documentation des modules, binôme avec des personnes d'ESTRAVENT ou d'autres ingénieurs de l'ESN, stabilité de l'équipe affectée.
3. **Rétablir les niveaux de service** du contrat (95 % et 90 %) et appliquer les pénalités prévues ; mesures tirées des outils d'ESTRAVENT.
4. **Maîtriser le coût** : limiter la hausse, et faire entrer dans le forfait, ou dans un catalogue de prix unitaires, une part des évolutions facturées aujourd'hui hors forfait (300 k€ en 2026).

La position de l'ESN est faible sur le fond : elle demande environ 225 k€ de plus par an alors que la qualité baisse depuis deux ans ; elle est forte en pratique, parce qu'ESTRAVENT ne peut pas changer de prestataire avant la fin de 2027. La négociation doit donc d'abord réduire cette dépendance.

**Concessions possibles** (0,5 pt avec le repli) :
- accepter une **hausse partielle**, limitée à une revalorisation modérée, en échange de la remise du code, du plan de réversibilité et du retour aux niveaux de service ;
- accepter une **durée de trois ans**, qui donne de la visibilité à l'ESN, si le contrat prévoit une sortie possible en fin d'année et un transfert des connaissances ;
- accepter de **payer les évolutions** liées aux batteries et aux nouveaux modèles, si elles sont chiffrées selon un catalogue connu d'avance.

**Solution de repli** si la négociation échoue : ne pas renouveler pour trois ans aux conditions de l'ESN et préparer la reprise de la maintenance, par l'une des deux autres ESN ou par une équipe mixte (quelques développeurs recrutés progressivement, appuyés par une ESN), sans organiser ici de procédure de choix. Le calendrier contraint ce repli : il faut six mois de transfert, rien n'est prêt, et le contrat finit le 31/12/2027. Il suppose donc une **prolongation transitoire** du contrat actuel, de six à douze mois, à obtenir de l'ESN, qui préfère quelques mois de chiffre d'affaires à une rupture brutale :
- dès **juin 2027** : nommer un responsable du contrat, reprendre le suivi mensuel, demander la documentation et une copie du code, inventorier la plateforme ;
- **avant le 30/09/2027** : notifier le refus du renouvellement aux conditions proposées et la demande de prolongation transitoire ;
- **en 2028** : six mois de transfert vers le repreneur, reprise au plus tard le 31/12/2028.

Ce repli dépend encore en partie de l'ESN : c'est ce qui fait de la réversibilité le premier objectif de la négociation.

*1.3 c) – La gouvernance de la relation et deux indicateurs*

**Dispositif de gouvernance** (0,5 pt) :
- **trois niveaux d'instances** : un comité stratégique annuel (vous, la directrice de l'exploitation et la direction de l'ESN : orientations, évolution du contrat, satisfaction) ; un comité de pilotage mensuel (responsable du contrat chez ESTRAVENT, responsable de la cellule supervision, responsable du centre de conduite, directeur de compte de l'ESN : niveaux de service, pénalités, évolutions, risques, plan de transfert) ; un point opérationnel hebdomadaire (incidents, changements, planning) ;
- **mesures vérifiées par ESTRAVENT** : les indicateurs sont tirés des journaux de la plateforme et du centre de conduite, et non du seul compte rendu de l'ESN ;
- **clause d'audit** : droit pour ESTRAVENT, ou pour un tiers qu'elle mandate, de vérifier la prestation, la tenue du code et de la documentation, la sécurité et les chiffres transmis, avec un préavis et une fréquence fixés ;
- **plan de sortie** (réversibilité) : liste de ce qui est remis (code, documentation, environnements, données), durée d'assistance du prestataire sortant, transfert des connaissances, coût et délai connus d'avance, **test annuel** de remise du code et de reconstruction de la plateforme.

**Deux indicateurs** (0,5 pt ; deux parmi les suivants) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de rétablissement des pannes bloquantes en 4 heures | pannes bloquantes rétablies en 4 heures au plus / pannes bloquantes du mois × 100 | journal horodaté des incidents du centre de conduite et de la plateforme (outils d'ESTRAVENT) | mensuelle | au moins 95 % | processus |
| Part des évolutions facturées hors forfait | montant des évolutions facturées hors forfait / montant total facturé par l'ESN × 100 | devis validés et factures de l'ESN, progiciel de gestion intégré | trimestrielle | au plus 10 % | financier |
| Taux de couverture du transfert des connaissances | modules de la plateforme documentés à jour et maîtrisés par au moins deux personnes, dont une d'ESTRAVENT / modules de la plateforme × 100 | revue semestrielle de la documentation et du plan de transfert, tenue par la cellule supervision | semestrielle | 100 % avant la fin de 2028 | apprentissage |

**Réponses tolérées**
- Autres risques appuyés sur l'annexe (défaillance de l'ESN, dérive du périmètre des évolutions, mesures de la qualité non vérifiées), si les quatre thèmes du risque de dépendance, de réversibilité, de coût et de savoirs sont couverts au total.
- Renouvellement court (un an) présenté comme position de repli dans la négociation, si le candidat voit qu'il suppose l'accord de l'ESN et prépare en parallèle la reprise.
- Repli fondé sur une reprise partielle par une équipe interne, si le candidat mesure la difficulté de recruter quatre développeurs et prévoit un appui extérieur pendant la transition.
- Ordre différent des objectifs, s'il est justifié (par exemple les niveaux de service d'abord, au nom de la disponibilité de 97 %).
- Autres indicateurs complets (rotation des ingénieurs affectés, part des anomalies majeures corrigées en cinq jours ouvrés, résultat du test de réversibilité), s'ils portent les cinq champs.

**Erreurs fréquentes**
- *Risques énumérés sans les constats de l'annexe 1.4* (`JUR-T08` ; `JUR-T01`) — chaque risque s'appuie sur un chiffre ou un fait.
- *Analyse juridique du contrat ou de la propriété du code* (`JUR-T07` ; limite du programme 1.4) — les droits sur les développements et la réversibilité sont traités en principe, comme objectifs de négociation.
- *Rupture immédiate ou changement de prestataire au 01/01/2028* (`JUR-G05` recommander de façon réaliste) — six mois de transfert sont nécessaires et rien n'est prêt.
- *Indicateurs génériques ou mesurés par l'ESN seule* (ET-18 indicateurs génériques ; `JUR-A02` justifier chaque choix) — la faiblesse actuelle vient justement de chiffres non vérifiés.
- *Procédure de choix d'un nouveau prestataire décrite* (`JUR-T07`) — non demandée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Clauses critiques d'un contrat avec une ESN | propriété des développements (principe), audit, réversibilité, durée et évolution des prix | F04 § 4 | notion de cours |
| Gouvernance et risques de la relation avec un prestataire | comités stratégique, de pilotage et opérationnel ; dépendance, dérive de qualité et de coûts ; indicateurs | F04 § 5 et § 6 ; F02 § 6 | notion de cours |

---

### 1.4 – La transmission des savoirs du développement des parcs (3,5 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.b` « Architecture fonctionnelle des systèmes de knowledge management » ; `1.6.a` « Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle » ; `1.6.c` « Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) » ; `1.6.e` « Leviers d'appropriation et de transformation des pratiques professionnelles ». Limites : « La gestion des connaissances dépasse la seule numérisation de l'information. » « Le lien avec la gestion des compétences (RH) est complémentaire mais distinct. »

**Annexes mobilisées** : annexes 1.5 (savoirs, existant, projet abandonné, témoignages), 1.1 (développement, système d'information, organigramme) et 1.6 (SECI, ADKAR).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Connaissances tacites et explicites distinguées ; modèle SECI présenté avec ses quatre conversions (socialisation, externalisation, combinaison, internalisation) | 0,5 |
| a-2 | Trois savoirs critiques de l'annexe 1.5 retenus, criticité justifiée par des critères explicites (rareté des détenteurs, imminence des départs, effet d'une perte, part tacite) | 0,5 |
| a-3 | Un mode de transmission adapté à chacun, rattaché à une conversion du modèle SECI | 0,5 |
| b-1 | Architecture fonctionnelle (capter, organiser, retrouver, partager, mettre à jour) appuyée sur les outils existants (gestion électronique des documents, système d'information géographique, outil de gestion des relations, wiki, réunion des agences), sans se réduire au classement des documents | 0,5 |
| b-2 | Gouvernance : rôles (commanditaire, animateur, référents par savoir, contributeurs, DSI, déléguée à la protection des données) et une règle de mise à jour précise | 0,5 |
| b-3 | Un indicateur de suivi complet (formule, source, fréquence, cible, axe) | 0,5 |
| c-1 | Trois leviers d'appropriation, chacun en réponse à une résistance de l'annexe 1.5 (temps, contacts personnels, primes des agences) | 0,5 |

**Réponse attendue**

*1.4 a) – Les savoirs critiques et leur transmission*

Une **connaissance explicite** est formalisée et transmissible sans son auteur : un rapport de mesures de vent, un modèle de cahier des charges. Une **connaissance tacite** est incorporée dans la personne, faite d'expérience et de jugement, difficile à mettre en mots : savoir qu'un mât de mesure est mal placé, sentir qu'un maire hésite. Le **modèle SECI** de Nonaka et Takeuchi (1995) décrit la création de connaissances comme une spirale de quatre conversions : la **socialisation** fait passer un savoir tacite d'une personne à une autre par l'expérience partagée ; l'**externalisation** met un savoir tacite en mots ou en schémas ; la **combinaison** assemble et organise des savoirs explicites ; l'**internalisation** transforme le savoir explicite en savoir-faire par la pratique (0,5 pt).

**Critères de criticité** : rareté des détenteurs ; imminence de leur départ (12 chefs de projet expérimentés sur 45, plus d'un quart, d'ici 2030) ; effet d'une perte sur un projet de sept à neuf ans ; part tacite du savoir.

**Trois savoirs critiques et leur transmission** (0,5 pt pour la criticité, 0,5 pt pour les modes) :

| Savoir | Pourquoi il est critique | Mode de transmission (conversion SECI) |
|---|---|---|
| **Préparer le raccordement au réseau** | deux détenteurs seulement, à l'agence Grand Est, qui partiront tous deux d'ici 2029 ; une erreur connue de cette agence en 2021 a coûté environ 0,5 M€ d'études à l'agence Hauts-de-France en 2025 | **externalisation** : entretiens d'explicitation des deux détenteurs, conduits par un rédacteur, et une fiche par poste électrique étudié (capacité, difficultés rencontrées, date) ; **combinaison** : fiches rattachées au poste dans le système d'information géographique, consultables par toutes les agences |
| **Choisir un site et lire les mesures de vent** | jugement très tacite, détenu par quelques chefs de projet anciens ; les rapports gardés dans la gestion électronique des documents ne disent pas pourquoi un site a été gardé ou écarté ; une erreur engage des années d'études | **socialisation** : binôme d'un ancien et d'un jeune sur les prochaines campagnes de mesure, revue commune des mesures ; **externalisation** : une note de décision courte jointe à chaque rapport (« site gardé ou écarté, et pourquoi ») |
| **Dialoguer avec les communes et les riverains** | relationnel, tacite, attaché aux personnes ; deux tiers des communes ne sont pas renseignées dans l'outil ; un départ peut faire perdre des années de confiance et un projet | **socialisation** : le partant présente son successeur aux élus et aux riverains avant son départ, sur plusieurs rencontres ; **externalisation** : une carte des acteurs de chaque projet (qui rencontrer, dans quel ordre, points sensibles) dans l'outil de gestion des relations ; **internalisation** : le successeur conduit les réunions suivantes, appuyé par le partant |

*1.4 b) – L'architecture fonctionnelle et la gouvernance du dispositif*

**Architecture fonctionnelle** (0,5 pt) :

| Fonction | Ce qu'elle fait | Outils existants mobilisés |
|---|---|---|
| **Capter** | recueillir les savoirs au fil des projets : notes de décision, retours d'expérience à chaque jalon (choix du site, accord des propriétaires, dépôt de la demande de raccordement, abandon), entretiens des partants, enregistrements courts | outil de gestion des relations (contacts, étapes de l'accord des propriétaires) ; gestion électronique des documents (rapports de mesure, avec une note de décision jointe) ; enregistrements audio ou vidéo courts |
| **Organiser** | plan de classement commun aux quatre agences, métadonnées partagées (projet, commune, poste électrique, étape, savoir concerné), rattachement de chaque contenu à un lieu | gestion électronique des documents réorganisée sur un plan commun ; système d'information géographique comme point d'entrée par le territoire |
| **Retrouver** | rechercher par le contenu et par les métadonnées, et pas seulement par le nom des fichiers ; consulter, sur la carte, tout ce qui est connu d'un site ou d'un poste | moteur de recherche de la gestion électronique des documents, système d'information géographique |
| **Partager** | mettre en relation les chefs de projet des quatre agences : communauté du développement, annuaire des détenteurs de chaque savoir, retours d'expérience présentés à la réunion des agences, désormais consacrée aux difficultés et non aux seules mises en service | wiki relancé comme recueil des fiches de retour d'expérience et des cartes des acteurs ; outil de gestion des relations pour les contacts |
| **Mettre à jour** | réviser chaque contenu à date fixe, retirer les contenus périmés, signaler les savoirs encore non couverts | propriétaire et date de revue sur chaque fiche |

Le dispositif n'est pas une gestion électronique des documents de plus : il relie les documents, les personnes et les lieux, et il fait passer les savoirs tacites des chefs de projet partants dans la pratique des autres.

**Gouvernance** (0,5 pt) :
- **commanditaire** : Mme TRÉMOLLAC, directrice du développement, qui fixe les priorités et porte le dispositif au comité de direction ;
- **animateur** de la gestion des connaissances au sein de la direction du développement, qui tient la cartographie des savoirs critiques et organise les entretiens et les revues ;
- **référents par savoir** (raccordement, vent, dialogue local, études environnementales, propriétaires), choisis parmi les chefs de projet expérimentés, dans des agences différentes, qui valident les contenus ;
- **contributeurs** : tous les chefs de projet ; **DSI** : outils, plan de classement, recherche, droits d'accès ; **déléguée à la protection des données** : les contacts des élus, des propriétaires et des riverains sont des données personnelles, à limiter au nécessaire et à protéger (principe du RGPD, sans analyse juridique) ;
- **règle de mise à jour** : chaque jalon d'un projet donne lieu, dans le mois, à une fiche de retour d'expérience validée par le référent ; chaque fiche a un propriétaire et une date de revue annuelle, après laquelle elle est révisée ou retirée ; aucun chef de projet ne part sans que ses savoirs critiques aient été recueillis.

**Un indicateur** (0,5 pt ; un parmi les suivants) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de couverture des savoirs critiques | savoirs critiques recensés disposant d'une fiche à jour et d'au moins un second détenteur / savoirs critiques recensés × 100 | cartographie des savoirs critiques tenue par l'animateur | semestrielle | 100 % avant chaque départ annoncé ; au moins 80 % à la fin de 2028 | apprentissage |
| Part des nouveaux projets qui s'appuient sur les retours d'expérience | nouveaux projets dont la revue de lancement cite au moins une fiche du dispositif (poste électrique, site voisin) / nouveaux projets lancés × 100 | comptes rendus des revues de lancement, journal de consultation du wiki et du système d'information géographique | trimestrielle | 100 % | processus |

*1.4 c) – Trois leviers d'appropriation*

(0,5 pt)

| Résistance (annexe 1.5) | Levier |
|---|---|
| « Je n'ai pas le temps d'écrire » | **ne pas faire écrire les anciens** : un rédacteur ou un jeune chef de projet conduit l'entretien et rédige la fiche, que l'ancien relit ; captation orale ou vidéo de quelques minutes ; retours d'expérience intégrés aux jalons du projet et temps reconnu dans les objectifs |
| « Mes contacts dans les mairies, c'est mon travail » | **partager la carte, pas la relation** : seule la carte des acteurs utile au projet est partagée, avec un accès réservé ; la relation se transmet par la présentation du successeur par le partant ; le chef de projet reste reconnu comme l'auteur de la relation |
| Primes des agences calculées sur leurs propres mises en service | **récompenser le partage** : une part de la prime liée aux mises en service de l'ensemble du développement ou aux contributions reconnues ; exemplarité de la directrice du développement ; démonstration par un premier gain visible, comme l'erreur de raccordement évitée qui aurait épargné 0,5 M€ d'études |

Le modèle ADKAR (annexe 1.6) éclaire l'ordre de ces leviers : faire comprendre pourquoi partager (le projet abandonné de 2025), donner l'envie (la prime), puis les moyens (le rédacteur, l'outil simple) et ancrer la pratique (les jalons).

**Réponses tolérées**
- Autres savoirs critiques de l'annexe 1.5 (études environnementales, accord des propriétaires), si la criticité est justifiée par des critères explicites et si la transmission est adaptée.
- Architecture présentée selon les fonctions de F06 (identifier, capter, stocker, diffuser, utiliser, mettre à jour), si les outils existants sont mobilisés.
- Communauté de pratique ou réunion des agences transformée en revue des difficultés, présentée comme le cœur du partage.
- Leviers inspirés des huit étapes de Kotter, s'ils répondent aux résistances.

**Erreurs fréquentes**
- *Gestion des connaissances réduite à la gestion électronique des documents ou à un nouveau wiki* (ET-21 ; limite du programme 1.6) — le wiki de 2023 montre qu'un outil sans animation ni temps dédié échoue.
- *Quadrants du modèle SECI inversés ou modèle récité sans application* (F06 § 6 ; `JUR-T01`) — chaque mode de transmission est relié à une conversion.
- *Gestion des compétences, plans de formation ou entretiens de carrière développés* (limite du programme 1.6 ; `JUR-T07`) — la gestion des compétences n'est pas à traiter.
- *Indicateur d'usage sans lien avec les savoirs critiques, ou incomplet* (ET-18) — l'enjeu est la couverture des savoirs avant les départs.
- *Leviers génériques (formation, communication) sans lien avec les résistances* (`JUR-P04` conduite du changement adaptée).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèle SECI, Nonaka et Takeuchi, 1995 (trad. 1997) | connaissances tacites et explicites, quatre conversions en spirale | `nonaka_takeuchi_seci` ; F06 § 1 | modèle théorique |
| Dispositif de gestion des connaissances | architecture fonctionnelle, gouvernance, appropriation | F06 § 2 | notion de cours |
| ADKAR, Prosci | étapes de l'adhésion individuelle au changement | `adkar` ; F05 § 7 | modèle théorique |
| RGPD, règlement (UE) 2016/679, applicable depuis le 25/05/2018 | contacts des élus, des propriétaires et des riverains : données personnelles, en principe | `rgpd` ; F15 | en vigueur |
