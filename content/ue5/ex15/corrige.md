# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 15 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 alignement stratégique et organisation de la DSI, F02 gouvernance et comitologie, F03 cloud, réversibilité et souveraineté, F04 contrats et niveaux de service, F09 performance et coûts du SI, F12 risques et résilience, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Le SI dans la chaîne de valeur de la filiale | `1.1.b` Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 3 |
| 3.2 Choix d'un scénario et feuille de route | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.c` Méthodologies de planification stratégique du SI | 2,5 |
| 3.3 Organisation de la fonction SI entre le groupe et la filiale | `1.2.b` Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 2 |
| 3.4 Risques de l'adhésion au socle | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers | 3,5 |
| 3.5 Coût complet de l'adhésion et refacturation | `3.1.b` Fondamentaux du contrôle de gestion appliqué aux SI ; `3.1.c` Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI | 2 |
| **Dossier 3 – Éclairer la décision d'adhérer au socle SI du groupe** |  | **13** |

Répartition indicative : connaissances (alignement stratégique, chaîne de valeur, modèles d'organisation de la DSI, typologie des risques, rôle du contrôle de gestion du SI) 2,75 points (items 3.1 a-1, 3.3 a-2, 3.4 a-1, 3.5 a-1, la moitié de 3.1 a-2 et de 3.2 b-2) ; analyse des annexes et recommandations 10,25 points, soit environ 79 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Le SI dans la chaîne de valeur de la filiale (3 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.b` « Principes d'alignement stratégique SI/métier (modèle SAM, chaîne de valeur, etc.) » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limite : « Ne pas confondre alignement stratégique et simple adéquation technique. »

**Annexes mobilisées** : annexes 3.2 (activités et applications, équipe, ce que les clients reconnaissent), 3.1 (périmètre du socle), 3.3 (positions de Mme DUCHASTEL et de M. DRAVIGNOL) et 1.1 (activité, plan « ORMESTAL 2030 »).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Alignement stratégique du SI défini (mise en cohérence permanente de la stratégie SI et de la stratégie de l'organisation, au-delà de l'adéquation technique) | 0,5 |
| a-2 | Chaîne de valeur de la filiale : activités principales et de soutien distinguées, chaque application de l'annexe 3.2 B placée, apport du SI précisé ; 0,5 si l'une des deux familles manque ou si l'apport n'est pas précisé | 1 |
| b-1 | Activités où un socle commun est pertinent (activités de soutien), avec la justification | 0,5 |
| b-2 | Activités où le SI propre porte un avantage concurrentiel (réservation des quais, traçabilité des températures, portail), justifiées par l'annexe 3.2 E | 0,5 |
| b-3 | Deux conditions pour que l'adhésion reste alignée sur la stratégie de la filiale | 0,5 |

**Réponse attendue**

*3.1 a) – Alignement stratégique et chaîne de valeur*

L'**alignement stratégique du système d'information** est la mise en cohérence permanente entre la stratégie de l'organisation et la stratégie de son SI : le SI doit servir les choix qui fondent l'avantage concurrentiel et les objectifs de l'organisation, et ses évolutions se décident à partir d'eux, non à partir des seules considérations techniques. Il est dynamique (à refaire à chaque changement de stratégie) et organisationnel autant que technique (F01 § 1) (0,5 pt). Pour une filiale, il se joue à deux niveaux : avec la stratégie de la filiale (différenciation par la réactivité et la traçabilité, annexe 3.2 E) et avec celle du groupe (plan « ORMESTAL 2030 »).

La **chaîne de valeur** (Porter, 1985) décompose l'activité en activités principales, qui créent directement la valeur perçue par le client, et en activités de soutien, qui les rendent possibles ; le SI y automatise, informe ou transforme chaque maillon (F01 § 2). Appliquée à ORMESTAL France (1 pt) :

| Famille | Activité de la filiale | Application(s) (annexe 3.2 B) | Apport du SI |
|---|---|---|---|
| Principale – logistique interne et opérations | réception, stockage, préparation des commandes, expédition dans les 14 entrepôts | logiciel de gestion des entrepôts ; module de réservation des créneaux de quai | automatise les flux, optimise l'occupation des quais ; **transforme** le service : créneau confirmé en moins de 15 minutes |
| Principale – logistique externe | transport et livraison (260 camions) | logiciel de gestion du transport ; télématique des camions | planifie les tournées ; suit la position et la température des caissons, collecte la preuve de livraison |
| Principale – commercialisation et services | relation avec les clients, service après livraison | portail des clients (suivi, alertes, certificats, preuves, réservation) | **transforme** la relation : alerte de température en temps réel, certificat dès la livraison ; premier motif de satisfaction |
| Soutien – infrastructure de l'entreprise | comptabilité, facturation, trésorerie | logiciel de gestion comptable et commerciale | automatise la facturation à partir des tournées et des prestations ; informe la direction |
| Soutien – approvisionnements | achats (pièces des installations frigorifiques, emballages, carburant, sous-traitance) | logiciel de gestion comptable et commerciale | automatise les commandes et leur validation |
| Soutien – gestion des ressources humaines | paie et gestion administrative de 650 salariés | logiciel de paie | automatise un traitement réglementé |
| Soutien – infrastructure de l'entreprise | communication interne, travail collaboratif | messagerie, agenda, partage de fichiers | coordonne les équipes de Mâcon et des entrepôts |
| Soutien – développement technologique | développement du portail et de la réservation des quais, adaptation des progiciels métiers | équipe SI de la filiale (7 personnes sur les applications métiers) | nourrit l'avantage des activités principales |

*3.1 b) – Socle commun ou SI propre, et conditions d'un alignement préservé*

**Un socle commun est pertinent pour les activités de soutien** (0,5 pt) : comptabilité, facturation et trésorerie, paie, messagerie et outils collaboratifs, et, sous réserve, achats. Ces activités ne différencient pas la filiale aux yeux des clients ; leurs besoins sont proches d'une filiale à l'autre et standardisables ; leur mise en commun apporte des économies d'échelle, un pilotage homogène du groupe (cinq filiales tiennent encore leur propre paie et leur propre comptabilité, M. DORMAELS ; clôture ramenée de dix à cinq jours dans les filiales qui ont adhéré, annexe 3.1 B), évite la montée de version de 2028 (annexe 3.2 C) et répond au plan, qui ne vise que les fonctions support. Les achats appellent une réserve : la commande d'une pièce d'une installation frigorifique en panne un samedi « dans l'heure » (M. DRAVIGNOL) touche la continuité des activités principales.

**Le SI propre de la filiale porte un avantage concurrentiel dans les activités principales** (0,5 pt) : la réservation des quais (créneau confirmé en moins de 15 minutes contre deux heures chez les autres prestataires), la traçabilité des températures transmise en temps réel (condition de deux appels d'offres d'enseignes en 2026) et le portail des clients (utilisé chaque semaine par neuf clients sur dix, premier motif de satisfaction, avant le prix) ; selon le directeur des opérations, ces services ont fait gagner trois appels d'offres face à des concurrents moins chers. Ils reposent sur des applications adaptées ou développées par l'équipe de la filiale et sur sa capacité à les faire évoluer vite : les soumettre à un cycle annuel d'évolutions décidé à Rotterdam affaiblirait la différenciation que la directrice générale veut préserver (« je ne veux pas que nos clients paient la standardisation »).

**Deux conditions pour que l'adhésion reste alignée** (0,5 pt, deux conditions précises et reliées au cas) :
1. **Préserver les échanges entre le socle et les activités principales** : la facturation dépend des tournées et des prestations transmises par les logiciels de gestion du transport et des entrepôts ; la refonte de ces échanges (200 k€, annexe 3.2 D) doit être prévue, testée avant la bascule et maintenue par un standard d'échange dont le groupe garantit la stabilité.
2. **Garder la maîtrise et la capacité d'évolution des applications métiers** : les applications qui portent l'avantage restent hors du socle, et l'équipe métier est renforcée par les deux personnes libérées (annexe 3.2 D) ; une procédure rapide permet de traiter hors cycle annuel les besoins métiers urgents qui touchent le socle (achat d'urgence d'une pièce, évolution de la facturation exigée par un client).

D'autres conditions sont admises : un niveau de service du socle adapté au rythme de l'activité (paie, facturation de fin de mois) ; la représentation de la filiale dans les décisions sur le socle.

**Réponses tolérées**
- Référence complémentaire au modèle d'alignement stratégique de Henderson et Venkatraman (1993), valorisée si elle éclaire l'analyse (stratégie de la filiale fondée sur la technologie, perspective de potentiel concurrentiel), sans être attendue.
- Chaîne de valeur présentée sous forme de schéma, ou découpage des activités principales en trois maillons (entrepôts, transport, relation client) au lieu de quatre.
- Facturation classée parmi les activités principales (service rendu au client) si le lien avec les tournées et les prestations est expliqué.
- Achats rangés dans le socle sans réserve, si la condition d'une procédure d'achat urgente apparaît dans b-3, ou rangés hors du socle avec une justification tirée du témoignage de M. DRAVIGNOL.

**Erreurs fréquentes**
- *Alignement réduit à l'adoption d'un logiciel commun* (`JUR-G02` ; `ET-06`) — « adhérer au socle, c'est s'aligner sur le groupe » ; juste : l'alignement porte sur la stratégie de la filiale autant que sur celle du groupe et peut justifier de garder des applications propres.
- *Chaîne de valeur récitée* (`JUR-T01` ; `ET-39`) — liste générique des activités de Porter sans les applications ni les chiffres de l'annexe 3.2.
- *Tout le SI dans le socle, ou rien* — refuser l'adhésion contredit le plan du groupe ; tout y mettre ignore l'avantage reconnu par les clients.
- *Avantage concurrentiel affirmé sans preuve* (`JUR-T08`) — juste : délai de 15 minutes contre deux heures, deux appels d'offres d'enseignes, neuf clients sur dix, trois appels d'offres gagnés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Alignement stratégique : définition | mise en cohérence permanente | F01 § 1 | notion de cours |
| Chaîne de valeur (Porter, 1985) | activités principales et de soutien ; apport du SI | `porter_chaine_valeur_1985` / F01 § 2 | modèle théorique |
| Strategic Alignment Model (Henderson et Venkatraman, 1993) | réponse tolérée | `henderson_venkatraman_1993` / F01 § 1 | modèle théorique |

---

### 3.2 – Choix d'un scénario et feuille de route (2,5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.c` « Méthodologies de planification stratégique du SI ».

**Annexes mobilisées** : annexes 3.1 (scénarios, calendrier, règles de gouvernance), 3.2 (coûts, équipe, avantage reconnu), 3.3 (positions des acteurs) et 1.1 (plan « ORMESTAL 2030 »).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Comparaison des deux scénarios selon les quatre critères, appuyée sur les annexes ; 0,5 pour deux ou trois critères | 1 |
| a-2 | Recommandation argumentée, qui répond aussi à la demande du groupe (client présent dans plusieurs pays) | 0,5 |
| b-1 | Feuille de route en trois étapes jusqu'à fin 2028 : contenu, échéance, responsable de chaque étape | 0,5 |
| b-2 | Indicateur de suivi complet (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.2 a) – Comparaison et recommandation*

| Critère | Scénario 1 – Adhésion complète | Scénario 2 – Adhésion limitée aux fonctions support |
|---|---|---|
| **Alignement sur la stratégie de la filiale** | défavorable : les applications qui fondent l'avantage reconnu par les clients (quais confirmés en 15 minutes, alertes de température, portail) sont retirées d'ici fin 2029 au profit des applications du groupe ; la différenciation qui a fait gagner trois appels d'offres est menacée | favorable : la filiale standardise ce qui ne la différencie pas et garde ce qui la différencie |
| **Respect du plan « ORMESTAL 2030 »** | au-delà du plan, qui ne vise que les fonctions support ; répond au souhait de M. DORMAELS et du client présent dans quatre pays | conforme au plan : fonctions support sur le socle d'ici fin 2028, calendrier tenable (projet d'environ douze mois) |
| **Coûts** | partie logistique non chiffrée et trois ans de projet, qui s'ajoutent au coût du socle ; économies d'échelle possibles mais inconnues | coût complet connu : proche du maintien sur trois ans (2 800 contre 2 700 k€), puis 150 k€ par an réaffectés aux applications métiers (deux personnes redéployées, question 3.5) |
| **Agilité des métiers** | toute évolution des quais, de la traçabilité ou du portail attend le comité d'architecture annuel, où la filiale ne siège pas : perte de réactivité (M. DRAVIGNOL) | agilité conservée sur les métiers ; la contrainte annuelle ne touche que les fonctions support, à aménager pour les achats urgents |

(1 pt.)

**Recommandation : le scénario 2** (0,5 pt). Il respecte le plan du groupe, préserve l'avantage concurrentiel de la filiale et repose sur un coût connu. Il répond à la demande du groupe d'une autre manière : les données de suivi des livraisons et de température de la filiale peuvent alimenter la plateforme de données du groupe, pour offrir au client présent dans plusieurs pays une vue commune sans retirer le portail de la filiale. La convergence des applications métiers pourra être réexaminée après 2028, quand les applications logistiques du groupe auront été chiffrées et comparées au service rendu aujourd'hui. L'adhésion est assortie de conditions négociées avant la signature (questions 3.3 à 3.5).

*3.2 b) – Feuille de route jusqu'à fin 2028 et indicateur de suivi*

| Étape | Contenu | Échéance | Responsable |
|---|---|---|---|
| 1. Cadrage et conditions d'adhésion | décision de la directrice générale présentée à M. DORMAELS ; convention d'adhésion avec la DSI du groupe (niveau de service, réversibilité, clé de refacturation, représentation de la filiale, procédure d'évolution urgente) ; inventaire des échanges entre les applications métiers et le PGI ; demandes d'évolution déposées avant le 30 septembre (circuit d'achat urgent) ; désignation des deux correspondants | avril à septembre 2027 | Mme DUCHASTEL (décision) ; M. BRÉVANNE (pilotage) ; Mme MERCOIRAN (conditions financières) |
| 2. Bascule de la messagerie, de la finance et des achats | messagerie et outils collaboratifs au quatrième trimestre 2027 ; refonte et essais des échanges avec la facturation ; formation ; bascule de la comptabilité, de la facturation, de la trésorerie et des achats au 1er janvier 2028 ; double fonctionnement jusqu'à l'arrêté des comptes de 2027 | octobre 2027 à juin 2028 | M. BRÉVANNE ; Mme MERCOIRAN, propriétaire des processus de gestion |
| 3. Bascule de la paie et bilan | paie au 1er juillet 2028 (début de trimestre, dans les six mois de double fonctionnement chiffrés à l'annexe 3.2 D) ; envoi des données de gestion à la plateforme de données du groupe ; retrait de l'ancien logiciel de gestion comptable et commerciale et du logiciel de paie ; bilan de l'adhésion (coût complet réel, niveau de service obtenu) présenté au comité de direction et à M. DORMAELS | juillet à décembre 2028 | M. BRÉVANNE ; Mme MERCOIRAN ; Mme DUCHASTEL (bilan) |

(0,5 pt.)

Indicateur de suivi de la feuille de route (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Taux de bascule des fonctions support dans les délais** | nombre de fonctions support basculées sur le socle à la date prévue, sans retour à l'ancienne application / 4 fonctions prévues (messagerie, finance et facturation, achats, paie) | comité de pilotage de l'adhésion (jalons validés conjointement par la filiale et la DSI du groupe) | mensuelle | 75 % au 31 mars 2028, 100 % au 31 décembre 2028 | processus |

**Réponses tolérées**
- Recommandation du scénario 1 si elle est argumentée et assortie de conditions fortes (maintien des services différenciants jusqu'à ce que les applications du groupe offrent le même délai de confirmation des quais et les mêmes alertes, représentation de la filiale dans le choix des évolutions) : la démarche est valorisée et l'item a-2 est accordé si les conditions sont précises.
- Critères formulés autrement (valeur pour les clients, faisabilité du calendrier), s'ils couvrent les quatre critères demandés.
- Calendrier différent (finance au 1er janvier 2029 avec dérogation au plan, paie au 1er janvier 2028), s'il respecte les règles de bascule de l'annexe 3.1 B et s'il est justifié ; une bascule de la finance au 1er janvier 2029 oblige à imputer la montée de version au scénario d'adhésion (annexe 3.2 C).
- Autre indicateur complet : coût complet annuel des fonctions support (refacturation et correspondants), cible 650 k€ au plus en 2029 et 2030, axe financier ; délai de clôture mensuelle, cible cinq jours ouvrés, axe processus ; taux de satisfaction des utilisateurs du socle, axe client.

**Erreurs fréquentes**
- *Feuille de route confondue avec un schéma directeur complet* (par analogie avec `ET-07`, schéma directeur confondu avec un plan de projet) — diagnostic, vision cible et portefeuille de tout le SI ; juste : la feuille de route d'un scénario, en trois étapes datées.
- *Recommandation sans tenir compte du plan du groupe* — refuser toute adhésion ; le plan s'impose à la filiale pour les fonctions support : la marge de décision porte sur le périmètre et les conditions.
- *Indicateur incomplet ou sans lien avec la feuille de route* (`JUR-A02` ; `ET-18`) — « respect du planning » sans formule ni cible.
- *Bascule de la finance ou des achats en cours d'exercice* — contraire aux règles de l'annexe 3.1 B.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Planification stratégique du SI : schéma directeur et feuille de route | étapes, échéances, responsables | F01 § 3 | notion de cours |
| Portefeuille applicatif (conserver, faire évoluer, remplacer, retirer) | scénarios | F01 § 3.2 | notion de cours |
| Fiche d'indicateur à cinq champs | indicateur de suivi | F09 § 4 | notion de cours |

---

### 3.3 – Organisation de la fonction SI entre le groupe et la filiale (2 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.b` « Modèles organisationnels de la DSI (centralisée, décentralisée, bimodale, etc.) » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers » (règles de gouvernance, représentation et arbitrage de la question b).

**Annexes mobilisées** : annexes 3.2 A (équipe et rattachement), 3.1 D (règles de gouvernance du socle), 3.3 (positions de Mme DUCHASTEL, de M. KAMPERVELD et de M. BRÉVANNE) et 1.1 (organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Modèle actuel caractérisé (décentralisé), avec les faits de l'annexe 3.2 A et ses effets | 0,5 |
| a-2 | Modèles fédéral et centralisé présentés, avec un avantage et une limite de chacun pour ORMESTAL France | 0,5 |
| b-1 | Positionnement recommandé du responsable des SI : double rattachement explicite, rôle de chaque lien | 0,5 |
| b-2 | Deux règles de gouvernance précises entre la filiale et le groupe | 0,5 |

**Réponse attendue**

*3.3 a) – Modèle actuel, modèles fédéral et centralisé*

**Modèle actuel : décentralisé** (0,5 pt). La filiale dispose de sa propre équipe SI de 20 personnes, choisit seule ses logiciels, ses prestataires et son hébergement et ne soumet pas ses projets au groupe ; la DSI du groupe se limite à animer une réunion mensuelle et à transmettre des règles de sécurité ; le responsable des SI rend compte à la directrice générale, sans lien écrit avec le DSI du groupe (annexe 3.2 A). Effets : réactivité et proximité des métiers, qui ont produit le portail et la réservation des quais ; mais hétérogénéité des SI du groupe (cinq filiales ont encore leur propre paie et leur propre comptabilité, M. DORMAELS), absence de règles sur qui décide de quoi (M. BRÉVANNE, Mme DUCHASTEL).

**Deux modèles cibles** (0,5 pt) :

| Modèle | Principe | Avantage pour ORMESTAL France | Limite pour ORMESTAL France |
|---|---|---|---|
| **Centralisé** | une DSI unique, celle du groupe, décide et opère pour toutes les filiales ; les filiales ne gardent que des correspondants | cohérence et économies d'échelle ; pilotage homogène du groupe ; sécurité homogène | éloignement des métiers de la logistique du froid française ; évolutions décidées une fois par an à Rotterdam ; perte de la réactivité qui fonde l'avantage reconnu par les clients ; dépendance complète au groupe |
| **Fédéral** | la DSI du groupe porte la gouvernance, l'architecture, le socle commun et les règles de sécurité ; chaque filiale garde une équipe SI pour ses métiers, dans le respect de ces règles | équilibre entre un socle commun pour les fonctions support et l'agilité des applications métiers ; cohérent avec le scénario 2 | coordination plus exigeante ; rôles et arbitrages à écrire ; risque de doublons si la frontière entre socle et métiers n'est pas tenue |

*3.3 b) – Positionnement du responsable des SI et règles de gouvernance*

**Positionnement recommandé : un double rattachement explicite, dans un modèle fédéral** (0,5 pt). M. BRÉVANNE reste rattaché **hiérarchiquement à la directrice générale** et membre du comité de direction : il porte l'alignement du SI sur la stratégie de la filiale et le budget des applications métiers. Il est rattaché **fonctionnellement au DSI du groupe** : il applique les règles d'architecture et de sécurité, est le correspondant du socle dans la filiale (avec les deux correspondants) et représente la filiale dans les instances du socle. Ce double lien est écrit dans une fiche de fonction validée par Mme DUCHASTEL et M. KAMPERVELD, qui précise ce qui relève de chacun, et met fin à la situation décrite par M. BRÉVANNE (« sans règle écrite »).

**Deux règles de gouvernance** (0,5 pt, deux règles précises et applicables) :
1. **Répartition écrite des décisions** : le socle relève du groupe, qui décide après avis des filiales ; les applications métiers relèvent de la filiale, qui décide dans le respect des règles d'architecture, de sécurité et des échanges standard définis par le groupe ; chaque filiale reste propriétaire de ses données. Cette répartition prend la forme d'une matrice des responsabilités (décide, est consulté, est informé) annexée à la convention d'adhésion.
2. **Représentation et arbitrage** : la filiale siège au comité d'architecture du groupe, ou à un comité des filiales adhérentes qui le précède, pour les évolutions du socle ; une procédure d'évolution urgente hors cycle annuel est prévue (obligation réglementaire, besoin métier critique comme un achat urgent), avec un délai de réponse fixé ; un désaccord persistant est arbitré par Mme DUCHASTEL et M. DORMAELS.

Règles également admises : convention de service interne entre la DSI du groupe et la filiale (disponibilité, délais d'information et de rétablissement) ; refacturation transparente, arrêtée chaque année avec les filiales (question 3.5) ; revue annuelle du socle par les filiales.

**Réponses tolérées**
- Modèle actuel qualifié de « décentralisé de fait » ou d'« autonomie de la filiale », si les faits de l'annexe 3.2 A sont cités.
- Recommandation d'un modèle bimodal (mode stable pour le socle, mode exploratoire pour les services aux clients), si les règles de coordination entre le groupe et la filiale sont précisées.
- Rattachement hiérarchique au DSI du groupe et fonctionnel à la directrice générale, si le candidat montre comment l'alignement sur la stratégie de la filiale reste garanti (participation au comité de direction, budget des applications métiers arrêté par la directrice générale).

**Erreurs fréquentes**
- *Modèle fédéral confondu avec le modèle décentralisé* (F01 § 8) — juste : le modèle fédéral suppose une gouvernance et un socle communs, absents aujourd'hui.
- *Recommandation irréaliste* (`JUR-G05` déséquilibres organisationnels et recommandations réalistes) — supprimer l'équipe SI de la filiale, ou ignorer le plan du groupe.
- *Gouvernance réduite à un outil ou au seul socle technique* (`JUR-G06` vocabulaire précis de la gouvernance) — juste : rôles, instances, règles de décision et d'arbitrage.
- *Modèles présentés sans application au cas* (`JUR-T01`) — définitions sans avantage ni limite pour ORMESTAL France.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Modèles d'organisation de la DSI (centralisé, décentralisé, fédéral, bimodal, externalisé) ; rôle et rattachement du DSI | modèle actuel, modèles cibles, positionnement | F01 § 4 | notion de cours |
| Comitologie SI (comité d'architecture, comité d'arbitrage) | règles de gouvernance | F02 § 6 | notion de cours |

---

### 3.4 – Risques de l'adhésion au socle (3,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ». Limite : « Une veille réglementaire est indispensable pour maintenir la conformité des pratiques. »

**Annexes mobilisées** : annexes 3.1 (hébergement, règles de gouvernance et de service, sortie, repères au 31/12/2026), 3.3 (positions des acteurs, incident de décembre 2026, échelle de cotation) et 3.2 (équipe, correspondants).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie des risques SI présentée (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers) | 0,5 |
| a-2 | Quatre risques identifiés, formulés comme des événements et rattachés chacun à une catégorie ; 0 en deçà de trois risques | 0,5 |
| b-1 | Cotation de chaque risque avec l'échelle de l'annexe 3.3 C, justifiée par les annexes | 0,5 |
| b-2 | Cartographie probabilité × impact et ordre de priorité | 0,5 |
| c | Option et mesure de traitement précises pour chaque risque ; 1 pour trois risques, 0,5 pour deux | 1,5 |

**Réponse attendue**

*3.4 a) – Typologie et identification*

Un **risque lié au SI** est un événement possible qui, s'il survient, porte atteinte à la disponibilité, à l'intégrité, à la confidentialité ou à la traçabilité de l'information, à la continuité des activités, à la conformité ou à la stratégie de l'organisation ; il s'apprécie par sa probabilité et son impact (F12 § 0). La typologie du programme distingue les **cybermenaces** (rançongiciel, hameçonnage, attaque par un fournisseur), les **défaillances opérationnelles** (panne, erreur, indisponibilité d'un service ou d'un prestataire), les **risques réglementaires** (non-conformité au RGPD, aux obligations sectorielles) et les **risques métiers** ou stratégiques (dépendance, perte d'avantage concurrentiel, inadaptation du SI aux besoins) (0,5 pt).

Quatre risques de l'adhésion (0,5 pt) :

| N° | Risque, formulé comme un événement | Catégorie | Faits des annexes |
|---|---|---|---|
| R1 | **Dépendance à la DSI du groupe et au fournisseur unique** : le groupe ou son fournisseur de cloud impose un tarif, un changement ou une migration que la filiale ne peut ni refuser ni quitter, faute de procédure de sortie et de compétences internes | risque métier (stratégique) : dépendance à un fournisseur | aucune procédure de sortie, tarif fixé chaque année sans détail des coûts, fournisseur unique (annexe 3.1 D) ; deux correspondants seulement ; « personne chez nous ne saura plus faire fonctionner ces applications » (M. BRÉVANNE) |
| R2 | **Souveraineté et localisation des données** : des données de paie et des contrats de clients sont rendus accessibles à une autorité d'un pays tiers, ou leur hébergement n'est pas conforme aux exigences du RGPD | risque réglementaire (conformité, confidentialité) | fournisseur dont le siège est hors de l'Union européenne, données stockées dans l'Union (annexe 3.1 A) ; transferts hors de l'Union soumis à des conditions particulières (annexe 3.1 E) ; « je voudrais savoir ce que le groupe a prévu » (Mme MERCOIRAN) |
| R3 | **Perte d'agilité des métiers** : un besoin urgent touchant le socle (achat d'une pièce un samedi, nouvelle règle de facturation exigée par un client) ne peut être satisfait à temps | risque métier | évolutions décidées une fois par an, demandes avant le 30 septembre, comité sans les filiales, assistance en anglais et en néerlandais de 8 à 18 heures en semaine (annexe 3.1 D) ; M. DRAVIGNOL |
| R4 | **Indisponibilité de la plateforme du groupe** : le socle est indisponible plusieurs jours ; la paie, la facturation et les achats sont bloqués | défaillance opérationnelle (la cause peut être une cybermenace, inconnue ici) | incident des 14 et 15 décembre 2026 dans la filiale belge, information au bout de six heures, cause non communiquée, aucune procédure de secours (annexe 3.3 B) ; disponibilité visée de 99,5 % sans engagement écrit ni compensation ; un seul fournisseur (annexe 3.1) |

*3.4 b) – Évaluation et cartographie*

| Risque | Probabilité | Impact | Criticité | Justification |
|---|---|---|---|---|
| R1 Dépendance | 3 (probable) | 3 (grave) | **9 – élevée** | tarif révisé chaque année et aucune sortie prévue : la situation de dépendance est acquise dès l'adhésion ; perte de maîtrise des données de paie et de facturation |
| R2 Souveraineté | 2 (possible) | 3 (grave) | **6 – moyenne** | données stockées dans l'Union, mais aucune garantie connue sur l'accès depuis un pays tiers ; un manquement porterait sur des données personnelles et sur la confiance des clients |
| R3 Agilité | 3 (probable) | 2 (significatif) | **6 – moyenne** | le cycle annuel est certain, mais le scénario 2 limite le risque aux fonctions support : retards internes, sauf pour les achats urgents |
| R4 Indisponibilité | 3 (probable) | 3 (grave) | **9 – élevée** | l'incident s'est déjà produit en 2026 sur l'une des trois filiales adhérentes ; paie, facturation et achats perturbés deux jours |

(0,5 pt.)

Cartographie (0,5 pt) :

| Impact \ Probabilité | 1 improbable | 2 possible | 3 probable | 4 quasi certain |
|---|---|---|---|---|
| 4 critique | | | | |
| 3 grave | | R2 (6) | **R1 (9), R4 (9)** | |
| 2 significatif | | | R3 (6) | |
| 1 mineur | | | | |

Ordre de priorité : R4 et R1, de criticité élevée, sont traités avant la bascule, R4 d'abord parce qu'il menace la facturation et les achats dès le 1er janvier 2028, la paie à partir de sa bascule, R1 dans la convention d'adhésion avant la signature ; R2 et R3, de criticité moyenne, sont traités dans le plan d'adhésion de l'étape 1.

*3.4 c) – Traitement des quatre risques*

| Risque | Option | Mesure |
|---|---|---|
| R1 Dépendance | réduire | **réversibilité** inscrite dans la convention d'adhésion : export complet et régulier des données de la filiale (paie, comptabilité, facturation, achats) dans un format ouvert et documenté, essai annuel de restitution, délai, assistance et coût de sortie, préavis et plafond des hausses de tarif ; maintien de deux correspondants formés et d'une documentation ; demande au groupe de faire jouer auprès de son fournisseur les droits de changement de fournisseur prévus par le Data Act (annexe 3.1 E) |
| R2 Souveraineté | réduire | garanties écrites demandées au groupe : contrat de sous-traitance avec le fournisseur couvrant les données de la filiale, localisation dans l'Union inscrite au contrat, chiffrement des données avec des clés maîtrisées par le groupe, information de la filiale en cas de demande d'accès d'une autorité ; inscription des traitements au registre ; critère d'un cloud de confiance (référentiel du Cigref, qualification SecNumCloud de l'ANSSI) pour le prochain choix d'hébergeur du groupe |
| R3 Agilité | réduire (et éviter pour les métiers) | **comité d'arbitrage** groupe-filiales et procédure d'évolution urgente hors cycle annuel, avec un délai de réponse fixé ; circuit d'achat d'urgence prévu dans le paramétrage commun (seuil, validation a posteriori) ; le maintien des applications métiers hors du socle (scénario 2) évite le risque là où il serait critique |
| R4 Indisponibilité | réduire | **clauses de niveau de service internes** dans une convention de service avec la DSI du groupe : disponibilité de 99,5 % mesurée et communiquée chaque mois, information de la filiale en moins d'une heure, délai de rétablissement, priorité pendant les périodes de paie et de clôture, minoration de la refacturation en cas de manquement ; **mode dégradé** documenté et exercé une fois par an : virement de la paie sur la base du mois précédent avec régularisation, factures émises dès le rétablissement, bons d'achat d'urgence hors PGI régularisés ensuite |

(1,5 pt pour les quatre risques traités avec une option et une mesure précise ; 1 pour trois, 0,5 pour deux.) Après traitement, la criticité résiduelle est revue en comité de direction ; un risque résiduel faible peut être accepté.

**Réponses tolérées**
- Cotations différentes d'un niveau, si elles sont justifiées par les annexes (R3 à impact 3 en raison des achats urgents ; R2 à probabilité 1 parce que les données sont stockées dans l'Union ; R1 à probabilité 4).
- Autres risques pertinents, à la place de l'un des quatre : échec de la bascule au 1er janvier 2028 (risque de projet), perte des compétences internes, cybermenace visant une plateforme partagée par huit filiales.
- Option « transférer » pour une part de R4 (minoration de la refacturation, assurance du groupe) ou « éviter » pour R2 (données de paie conservées hors du socle), si elle est expliquée.
- Référence à ISO 31000:2018 ou à ISO/IEC 27005:2022 pour les options de traitement, valorisée sans être attendue.

**Erreurs fréquentes**
- *Hébergement « souverain » assimilé à un hébergement dans l'Union européenne* (`ET-37`) — juste : la localisation ne règle pas le droit applicable à un fournisseur dont le siège est hors de l'Union.
- *Plan de continuité ou de reprise développé* (`JUR-S02`) — non demandé ; juste : un mode dégradé et des engagements de service.
- *Risques non formulés comme des événements, ou confondus avec leurs mesures* (`JUR-T03`) — « absence de réversibilité » est une cause ; le risque est l'impossibilité de sortir ou de récupérer ses données.
- *Cotations sans justification ni cartographie* (`JUR-T08`) — juste : chaque note s'appuie sur un fait (incident de décembre, absence de sortie, cycle annuel).
- *Analyse juridique du transfert ou de l'assujettissement à un texte de cybersécurité* — non attendue ; une mention suffit (annexe 3.1 E).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI ; cartographie probabilité × impact | identification, cotation | F12 § 0 ; F10 § 1.2 (cartographie probabilité × impact) | notion de cours |
| ISO 31000:2018 ; ISO/IEC 27005:2022 | options de traitement (réponse tolérée) | `iso_31000_2018`, `iso_27005_2022` / F12 § 2 | en vigueur |
| Réversibilité, portabilité, souveraineté | R1, R2 | F03 § 5.3 ; F04 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | sous-traitant, transferts hors de l'Union (annexe 3.1 E) | `rgpd` / F15 | applicable depuis le 25/05/2018 |
| Règlement (UE) 2023/2854 (Data Act) | changement de fournisseur de cloud | `data_act` / F03 § 5.3 | applicable depuis le 12/09/2025 |
| Proposition « omnibus numérique » (19/11/2025) | non applicable (annexe 3.1 E) | `omnibus_numerique_donnees` | projet |
| Référentiel du cloud de confiance du Cigref ; SecNumCloud 3.2 (ANSSI) | critères d'un cloud de confiance | `cigref_cloud_confiance`, `secnumcloud_3_2` / F03 § 5.3 | publiés |
| Niveaux de service (ITIL) | clauses de niveau de service internes | `itil` / F02 § 5 | en vigueur |

---

### 3.5 – Coût complet de l'adhésion et refacturation (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance (budgets, indicateurs, tableaux de bord) : `3.1.b` « Fondamentaux du contrôle de gestion appliqué aux SI » ; `3.1.c` « Analyse des coûts directs et indirects : TCO, coûts cachés, ROI des projets SI ». Limite : « Le pilotage stratégique par les indicateurs suppose une capacité de recul critique. »

**Annexes mobilisées** : annexes 3.2 C et D (coûts actuels, coûts annoncés et coûts relevés), 3.1 D (refacturation) et 3.3 (position de Mme MERCOIRAN).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Rôle du contrôle de gestion appliqué au SI dans la décision | 0,5 |
| a-2 | Coûts sur trois ans selon les chiffres du groupe : maintien 2 700 k€, adhésion 1 800 k€, économie annoncée de 900 k€ | 0,5 |
| a-3 | Coûts cachés intégrés (1 000 k€, adhésion à 2 800 k€) et conclusion nuancée (régime de croisière sans économie de trésorerie, autres justifications de la décision) | 0,5 |
| b | Deux critiques précises de la refacturation par compte et une clé plus adaptée | 0,5 |

**Réponse attendue**

*3.5 a) – Rôle du contrôle de gestion et coût complet*

Le **contrôle de gestion appliqué au SI** mesure le coût complet des services numériques (coûts directs, indirects et cachés), les impute aux activités qui les consomment par des inducteurs (refacturation interne), rapproche ces coûts de la valeur produite (qualité de service, gains, risques évités) et éclaire les décisions par des comparaisons de scénarios sur un horizon commun, avant d'en suivre la réalisation (F09 § 2). Ici, il doit vérifier l'économie annoncée par le groupe, faire apparaître ce que le chiffrage omet et apprécier la clé de refacturation (0,5 pt).

Coût sur trois ans, de 2028 à 2030, en k€ (0,5 pt) :
- **Maintien de la situation actuelle** : 3 × 800 + 300 (montée de version) = **2 700 k€** ;
- **Adhésion selon les chiffres du groupe** : 3 × 500 (refacturation) + 300 (migration) = **1 800 k€**, soit l'économie annoncée de **900 k€**.

Avec les coûts cachés relevés à l'annexe 3.2 D (0,5 pt) : double fonctionnement 250 + correspondants 3 × 150 = 450 + formation 100 + refonte des échanges 200 = **1 000 k€**, soit un coût complet de l'adhésion de 1 800 + 1 000 = **2 800 k€**, supérieur de **100 k€** à celui du maintien. La baisse de productivité des premiers mois, non chiffrée, accroît encore cet écart.

**Conclusion** : sur trois ans, l'adhésion n'apporte pas d'économie ; l'économie annoncée par le groupe vient de l'oubli des coûts cachés. En régime de croisière, après la bascule, le coût des fonctions support passe de 800 à 500 + 150 = 650 k€ par an. Ces 150 k€ ne sont pas une économie de trésorerie : ils correspondent aux deux personnes redéployées vers le portail et la réservation des quais, que la filiale continue de payer. L'adhésion libère donc une capacité de 150 k€ par an au profit des activités qui la différencient, à dépense constante. La décision ne se justifie donc pas par les coûts sur trois ans, mais par le plan du groupe, le pilotage homogène des filiales, la montée de version évitée et le redéploiement de deux personnes vers les applications qui différencient la filiale ; elle est conditionnée à la révision de la clé de refacturation (b), dont dépend l'essentiel de l'écart.

*3.5 b) – Critique de la refacturation par compte*

Deux critiques attendues parmi les trois suivantes (0,5 pt avec la clé proposée) :
1. **Un inducteur qui ne reflète pas la consommation** : un tarif unique de 1 000 € s'applique à un comptable qui utilise le PGI toute la journée comme à un chef d'équipe qui ne lit que ses courriels. Les 350 comptes de la seule messagerie (70 % des comptes) coûteraient 350 k€ par an, alors que la messagerie revient aujourd'hui à environ 100 € par compte, soit 35 k€ : la filiale, qui compte beaucoup d'utilisateurs de terrain, finance une part du PGI des autres.
2. **Une incitation contraire aux objectifs** : pour réduire la facture, la filiale pourrait limiter le nombre de comptes (comptes partagés, qui nuisent à la sécurité et à la traçabilité) ou garder la messagerie hors du socle, au détriment de la mise en commun recherchée.
3. **Un tarif opaque et sans lien avec le service rendu** : il est fixé chaque année par le groupe, sans détail de ses coûts ni lien avec le niveau de service (aucune minoration après l'incident de décembre 2026) ; la filiale ne peut ni contrôler ce qu'elle paie ni inciter la DSI du groupe à l'efficience.

**Clé plus adaptée** : une refacturation par service, sur la base d'un catalogue de services du socle : le PGI selon des unités d'œuvre représentatives (utilisateurs actifs du PGI, ou nombre de bulletins de paie, de factures et de commandes d'achat), la messagerie et les outils collaboratifs par compte à leur coût propre, la plateforme de données par un forfait par filiale ; des prix standard fixés pour l'exercice et connus à l'avance, une base de coûts communiquée aux filiales, et une minoration en cas de niveau de service non tenu.

**Réponses tolérées**
- Calcul présenté par année ou par poste, s'il aboutit aux mêmes totaux ; comparaison faite en coût annuel moyen sur la période, si le raisonnement est juste.
- Deux personnes redéployées maintenues dans le coût de l'adhésion (2 800 + 3 × 150 = 3 250 k€, soit 550 k€ de plus que le maintien), si le candidat raisonne au niveau de la dépense totale de la filiale et l'écrit.
- Correspondants comptés pour la seule durée de 2029 et 2030 ou montée de version exclue du maintien, si l'hypothèse est écrite et la conclusion reste nuancée.
- Clé fondée sur la seule distinction entre comptes du PGI et comptes de messagerie, avec deux tarifs, si elle est justifiée par l'annexe 3.2 D.
- Mention qualitative du retour sur investissement (gains non financiers : clôture plus rapide, pilotage du groupe), sans calcul.

**Erreurs fréquentes**
- *Coût complet réduit à la refacturation* (`ET-33` ; `JUR-A03` indicateurs de coûts dans une logique ouverte) — oubli du double fonctionnement, des correspondants, de la formation et des échanges.
- *Montée de version imputée au scénario d'adhésion*, alors qu'elle est évitée par la bascule de la finance au 1er janvier 2028, date retenue par le groupe (annexe 3.2 C).
- *Les 150 k€ par an du régime de croisière présentés comme une économie de trésorerie de la filiale* — ils correspondent aux deux personnes redéployées, dont le coût quitte le périmètre des fonctions support mais reste supporté par la filiale, au service des activités principales.
- *Calcul d'actualisation ou analyse fiscale des flux entre le groupe et la filiale* — hors du programme de l'UE 5 et non demandés.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Contrôle de gestion appliqué au SI : coût complet, inducteurs, refacturation interne | rôle, critique de la clé | F09 § 2 | notion de cours |
| Coût total de possession, coûts cachés, CAPEX et OPEX | comparaison sur trois ans | F09 § 3 | notion de cours |
