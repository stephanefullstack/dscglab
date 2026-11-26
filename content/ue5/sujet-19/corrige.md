# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 19

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Préparer l'évolution de la stratégie et de l'organisation du système d'information, la renégociation d'un contrat et la transmission des savoirs | 14 | 1.1 à 1.4 | `exercices/ex55_strategie_conduite_esn_savoirs` |
| 2 – Organiser et exploiter les données des installations, en garder la maîtrise | 13 | 2.1 à 2.4 | `exercices/ex56_installations_pertes_souverainete_sobriete` |
| 3 – Maîtriser les coûts, la fiabilité et la sécurité du système d'information de conduite | 13 | 3.1 à 3.4 | `exercices/ex57_couts_comptage_acces_distants_audit` |
| **Total** | **40** | | |

---

## DOSSIER 1 – PRÉPARER L'ÉVOLUTION DE LA STRATÉGIE ET DE L'ORGANISATION DU SYSTÈME D'INFORMATION, LA RENÉGOCIATION D'UN CONTRAT ET LA TRANSMISSION DES SAVOIRS (14 points)

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

---

## DOSSIER 2 – ORGANISER ET EXPLOITER LES DONNÉES DES INSTALLATIONS, EN GARDER LA MAÎTRISE (13 points)

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

---

## DOSSIER 3 – MAÎTRISER LES COÛTS, LA FIABILITÉ ET LA SÉCURITÉ DU SYSTÈME D'INFORMATION DE CONDUITE (13 points)

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
