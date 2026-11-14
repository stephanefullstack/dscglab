# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Sujet d'entraînement complet n° 6

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue5/fiches/` et `ue5/fiches/referentiels_dates.yaml`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, modèles de données, indicateurs, référentiels datés, barème sur 40, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Sécuriser le système d'information d'un cabinet qui travaille à distance | 14 | 1.1 à 1.5 | `exercices/ex16_securite_cabinet_travail_distance` |
| 2 – Exploiter les données des clients au service du conseil | 13 | 2.1 à 2.5 | `exercices/ex17_donnees_clients_conseil` |
| 3 – Évaluer le pilote de la base de connaissances et conduire sa généralisation | 13 | 3.1 à 3.6 | `exercices/ex18_base_connaissances_pilote` |
| **Total** | **40** | | |

---

## DOSSIER 1 – SÉCURISER LE SYSTÈME D'INFORMATION D'UN CABINET QUI TRAVAILLE À DISTANCE (14 points)

| Question | Compétence visée | Points |
|---|---|---|
| 1.1 Risques et principes de la politique de sécurité | `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers | 3 |
| 1.2 Architecture de confiance et appareils personnels | `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) | 3 |
| 1.3 Gouvernance de la sécurité, souveraineté et sensibilisation | `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers ; `2.3.d` Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique ; `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques | 3 |
| 1.4 Fiabiliser le processus de paiement des fournisseurs | `4.1.e` Fiabilisation des systèmes d'information comptables et décisionnels ; `1.3.f` Analyse des processus métiers et rôle des architectures SI dans leur rationalisation | 3 |
| 1.5 L'intelligence artificielle au service de la détection des fraudes | `4.1.f` Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques ; `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA | 2 |
| **Dossier 1 – Sécuriser le système d'information d'un cabinet qui travaille à distance** |  | **14** |

Répartition indicative : connaissances (politique de sécurité et analyse des risques, modèle Zero Trust, souveraineté numérique, donnée de référence, apprentissage automatique et IA générative) 2,5 points (items 1.1 a-1, 1.2 a-1, 1.3 b-1, 1.4 a-1, 1.5 a) ; analyse des annexes et recommandations 11,5 points, soit environ 82 %. Durée conseillée : 14 points × 4,5 minutes = 63 minutes, soit 1 h 03.

---

### 1.1 – Risques et principes de la politique de sécurité (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ». Limite : « La sécurité doit être envisagée dans une logique systémique (organisationnelle, humaine, juridique). »
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ».

**Annexes mobilisées** : annexes 1.2 (composants, usages constatés, moyens), 1.3 (les deux incidents), 1.1 (secret professionnel, période fiscale, travail à distance) et 1.4 (positions des acteurs).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Politique de sécurité du SI définie (document approuvé par la direction : objectifs, périmètre, principes, organisation, règles, contrôle) et fondement sur l'analyse des risques expliqué (menace, vulnérabilité, impact, traitement priorisé) | 0,5 |
| a-2 | Cinq vulnérabilités tirées des annexes, chacune avec la menace qui peut l'exploiter et le critère de sécurité atteint, menaces rattachées à la typologie des risques SI ; 1 point pour trois ou quatre, 0,5 pour deux | 1,5 |
| b | Quatre principes de la politique de sécurité, chacun justifié par les annexes ; 0,5 pour deux ou trois | 1 |

**Réponse attendue**

*1.1 a) – Politique de sécurité, analyse des risques et vulnérabilités du cabinet*

La **politique de sécurité du système d'information** (PSSI) est le document de référence, approuvé par la direction, qui fixe les objectifs de sécurité de l'organisation — confidentialité, intégrité, disponibilité et traçabilité de l'information —, son périmètre, ses principes, l'organisation et les rôles, les règles applicables et le dispositif de contrôle ; elle se décline en une charte opposable aux utilisateurs et en procédures (F12 § 1). Elle est **fondée sur l'analyse des risques** : un risque naît d'une **menace** (source et action malveillante ou accidentelle) qui exploite une **vulnérabilité** (faiblesse technique, organisationnelle ou humaine) et produit un **impact** sur un actif (ici, les données des clients couvertes par le secret professionnel, la production en période fiscale, les paiements des clients) ; les risques sont évalués (vraisemblance × gravité) puis traités par ordre de priorité, ce qui proportionne les mesures aux enjeux au lieu d'empiler des solutions. Les méthodes ISO/IEC 27005:2022 et EBIOS Risk Manager structurent cette démarche (0,5 pt).

Cinq vulnérabilités attendues parmi les suivantes (1,5 pt) :

| Vulnérabilité (annexe) | Menace qui peut l'exploiter | Critère principalement atteint |
|---|---|---|
| **Smartphones personnels non gérés** : 120 collaborateurs y consultent la messagerie et l'application du portail ; 6 perdus ou volés en 2026, dont un sans code (1.2 B-1) | perte ou vol de l'appareil, accès d'un tiers à la messagerie et aux pièces des clients, application malveillante installée sur un appareil privé | confidentialité |
| **Authentification par mot de passe seul** sur les logiciels de production, de paie et sur le portail ; authentification forte disponible mais non activée (1.2 A et B-5) | hameçonnage des identifiants (incident B : un identifiant saisi sur la fausse page), usurpation de compte | confidentialité et intégrité |
| **Comptes des renforts non désactivés et droits copiés** : 12 comptes actifs neuf mois après le départ, une connexion inexpliquée en septembre 2026, aucune revue des droits (1.2 B-4 et B-5) | accès illégitime d'un ancien renfort ou d'un tiers qui a obtenu le mot de passe ; droits excessifs | confidentialité et traçabilité (l'auteur de la connexion est inconnu) |
| **Pièces des clients déposées sur des stockages personnels** (25 dépôts en février), faute d'outil de partage performant (1.2 B-2 ; Mme BOURGALAT) | fuite par compromission du compte personnel, données conservées après le départ du collaborateur, hors de tout contrôle du cabinet | confidentialité (secret professionnel) |
| **Connexions depuis des réseaux sans fil publics** (environ 30 % des connexions, 1.2 B-3) | interception des échanges, faux point d'accès, vol de session | confidentialité |
| **Processus de modification des coordonnées bancaires sans contrôle** : un seul collaborateur modifie la fiche et prépare le paiement, sans vérification ni trace de l'auteur (1.3 A) | fraude au faux ordre de virement par usurpation d'un fournisseur (30 000 € perdus) | intégrité des données de référence et traçabilité |
| **Facteur humain non préparé** : aucune sensibilisation depuis 2023, aucun canal de signalement (1.2 B-6, 1.3 B) | hameçonnage ciblé en période fiscale, ingénierie sociale | confidentialité (identifiants dérobés), puis intégrité (faux changement de coordonnées) |
| **Journaux du portail conservés 30 jours seulement** (1.3 B) | compromission découverte tardivement, impossible à reconstituer | traçabilité |

Les menaces relevées couvrent la typologie des risques SI : cybermenaces (hameçonnage, vol d'appareil, usurpation d'un fournisseur), défaillances opérationnelles (processus de paiement sans contrôle, comptes non désactivés), risques métiers et réglementaires (violation du secret professionnel, perte de confiance des clients, violation de données à notifier).

Plusieurs de ces vulnérabilités sont propres au travail à distance (appareils, réseaux publics, stockages personnels) ; les autres sont aggravées par l'éloignement des collaborateurs, qui fait sortir les données des bureaux, éloigne les collaborateurs du responsable informatique et multiplie les échanges par courriel, que les attaquants imitent.

*1.1 b) – Quatre principes de la politique de sécurité du cabinet* (1 pt, quatre principes justifiés)

1. **La sécurité est l'affaire de la direction et s'applique à tous les bureaux** : la PSSI est approuvée par le comité des associés, qui fixe les priorités et accepte les risques résiduels, et elle s'impose aux six bureaux. Justification : la présidente veut « que la sécurité devienne l'affaire du comité des associés » ; le responsable informatique n'a aucune autorité sur les bureaux ; M. MONTCLAVEL réduit à tort la sécurité au « travail de l'informatique ».
2. **Aucune confiance implicite : chaque accès est vérifié, quel que soit le lieu ou l'appareil**, avec une authentification forte et des droits limités au besoin (moindre privilège). Justification : connexions depuis des lieux publics, identifiant dérobé par hameçonnage, comptes de renforts encore actifs.
3. **Les données des clients restent dans des espaces maîtrisés par le cabinet**, sur ses applications et dans des espaces cloisonnés des appareils, parce que le secret professionnel l'exige ; le cabinet fournit en contrepartie des outils qui fonctionnent à distance. Justification : 25 dépôts sur des stockages personnels, smartphones personnels perdus, témoignage de Mme BOURGALAT.
4. **Les opérations sensibles sont tracées et contrôlées par une seconde personne** : modifications des données de référence (coordonnées bancaires), création et suppression des accès, avec des journaux conservés assez longtemps pour reconstituer un incident. Justification : incident FALVERGNE, connexion inexpliquée de septembre 2026, journaux de 30 jours.

D'autres principes sont admis s'ils sont justifiés : des règles proportionnées et applicables, construites avec les utilisateurs (« je ne veux pas de règles que personne n'appliquera ») ; la vigilance de chacun et le signalement sans délai (incident B) ; la maîtrise des tiers (éditeurs, prestataire) par le contrat ; la gestion des accès sur tout leur cycle de vie.

**Réponses tolérées**
- Vulnérabilités présentées comme des risques complets (« un collaborateur perd son smartphone et un tiers lit les courriels d'un client »), si la vulnérabilité, la menace et l'impact y sont identifiables.
- Critère « disponibilité » retenu pour la perte d'un appareil ou pour un compte usurpé (blocage, effacement), si la justification est donnée ; « preuve » ou « imputabilité » au lieu de traçabilité.
- Référence au guide d'hygiène informatique de l'ANSSI (2017, 42 mesures) ou à la norme ISO/IEC 27001:2022 pour structurer la politique, sans viser de certification.

**Erreurs fréquentes**
- *PSSI confondue avec la charte informatique* (`ET-27`) — la charte décline les règles d'usage ; la PSSI fixe objectifs, organisation et règles.
- *Morceau de cours sur la triade CID sans application* (`JUR-T01` ; `JUR-S01`) — juste : critère rattaché à chaque vulnérabilité du cas.
- *Appareils personnels réduits à un problème de virus* (`ET-16` ; `JUR-S04`) — juste : perte, mélange des données, absence de maîtrise, sortie du collaborateur.
- *Vulnérabilités techniques détaillées* (failles logicielles, configuration des réseaux) — hors attente : la question porte sur les usages et l'organisation du travail à distance.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Triade CID et traçabilité ; PSSI et charte | définition, critères | F12 § 1 | notion de cours |
| ISO/IEC 27005:2022 ; EBIOS Risk Manager, version 1.5 (2024) | démarche d'analyse des risques | `iso_27005_2022`, `ebios_rm_1_5` / F12 § 2 | en vigueur |
| ISO/IEC 27001:2022 ; guide d'hygiène informatique de l'ANSSI (2017) | réponse tolérée | `iso_27001_2022`, `guide_hygiene_anssi_2017` / F12 § 2 | en vigueur |

---

### 1.2 – Architecture de confiance et appareils personnels (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ». Limite : « La mise en œuvre technique des solutions de cybersécurité n'est pas exigée. »

**Annexes mobilisées** : annexes 1.2 (composants, usages constatés, moyens), 1.3 (incident B), 1.4 (positions de Mme FÉRANDOUX, de M. MONTCLAVEL, de M. QUINTAREL, de Mme BOURGALAT et de la présidente ; coûts) et 1.1 (période fiscale, travail à distance).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Modèle Zero Trust présenté comme un cadre d'architecture (aucune confiance implicite, vérification de chaque accès en contexte, moindre privilège), et non comme un produit | 0,5 |
| a-2 | Quatre dispositifs (authentification, chiffrement, cloisonnement sur les smartphones, gestion des identités et des accès avec arrivées, départs et revue des droits), chacun relié à un constat ; 1 point pour trois, 0,5 pour deux | 1,5 |
| b-1 | Choix entre interdiction et usage encadré, justifié par trois arguments tirés des annexes (dont la comparaison des coûts) | 0,5 |
| b-2 | Deux conditions de réussite de la solution retenue | 0,5 |

**Réponse attendue**

*1.2 a) – Zero Trust et quatre dispositifs*

Le **modèle Zero Trust** est un **cadre d'architecture**, et non un produit : il part du principe qu'aucune confiance n'est accordée par défaut à un utilisateur ou à un appareil du seul fait de sa position (au bureau, à domicile, dans un hôtel) ; chaque accès à une ressource est authentifié, autorisé selon le moindre privilège et évalué en contexte (identité, état de l'appareil, lieu, sensibilité des données), et l'activité est surveillée en continu. Il convient à un cabinet dont les applications sont en mode SaaS et dont les collaborateurs travaillent hors des bureaux : il n'y a plus de « périmètre » à défendre (F12 § 3) (0,5 pt). Il se construit progressivement et ne dispense ni de la politique de sécurité ni de la sensibilisation.

Quatre dispositifs (1,5 pt) :

| Dispositif | Contenu | Constat auquel il répond |
|---|---|---|
| **Authentification forte** | authentification à deux facteurs de nature différente (mot de passe et application ou clé sur un appareil de confiance) sur le logiciel de production comptable, le logiciel de paie, le portail et la messagerie, pour tous ; **accès conditionnel** : le second facteur est exigé à chaque connexion depuis un appareil ou un lieu inhabituel, et de façon périodique sur un appareil de confiance, ce qui répond à la crainte de Mme FÉRANDOUX en période fiscale | mot de passe seul ; authentification forte proposée sans surcoût par les deux éditeurs et non activée (1.2 A) ; identifiant saisi sur la fausse page le 15 mars : avec un second facteur, il n'aurait pas suffi (1.3 B) |
| **Chiffrement** | disques des ordinateurs portables et espace professionnel des smartphones chiffrés ; accès aux applications et au partage de fichiers du cabinet uniquement par des connexions chiffrées, y compris depuis un réseau public ; espace de partage du cabinet chiffré et adapté aux fichiers volumineux | 30 % de connexions depuis des réseaux publics ; appareils perdus ou volés ; dépôts sur des stockages personnels faute d'outil adapté (1.2 B) |
| **Cloisonnement des données du cabinet sur les smartphones** | outil de gestion des terminaux mobiles (ou des seules applications professionnelles) : espace professionnel séparé et chiffré qui contient la messagerie et l'application du portail ; code de verrouillage exigé ; effacement à distance de ce seul espace en cas de perte, de vol ou de départ ; accès à la messagerie et au portail réservé aux appareils enrôlés | 120 smartphones personnels sans aucun outil de gestion, 6 perdus ou volés en 2026, dont un sans code (1.2 B-1) ; proposition de M. QUINTAREL (1.4 A) |
| **Gestion des identités et des accès** | comptes nominatifs ; **profils types** par métier (collaborateur, chef de mission, pôle social, renfort) au lieu de la copie des droits d'un collègue ; **arrivées** : demande transmise par le bureau à l'informatique, avec la date de fin de contrat, avant l'arrivée ; compte du renfort créé avec une **date d'expiration** égale à la fin de son contrat ; **départs** : désactivation le jour du départ, déclenchée par les ressources humaines ; **revue des droits** par chaque associé responsable de bureau deux fois par an, avant et après la période fiscale ; désactivation immédiate des 12 comptes de renforts encore actifs | droits copiés, départs jamais signalés, 12 comptes actifs et connexion inexpliquée en septembre 2026, aucune revue (1.2 B-4 et B-5) ; « je ne suis informé ni des arrivées, ni des départs » (M. QUINTAREL) |

*1.2 b) – Interdire ou encadrer les smartphones personnels*

**Recommandation : un usage encadré des smartphones personnels**, sous condition d'enrôlement dans l'outil de gestion des terminaux mobiles (0,5 pt pour trois arguments) :
1. **Le besoin métier est réel et une interdiction serait contournée** : en période fiscale, les collaborateurs répondent aux clients le soir et en déplacement (Mme FÉRANDOUX) ; les dépôts sur des stockages personnels montrent qu'une règle sans outil adapté est contournée (Mme BOURGALAT), et la présidente ne veut « pas de règles que personne n'appliquera ». Une interdiction sans solution de remplacement déplacerait l'usage vers des outils encore moins maîtrisés.
2. **Le coût est sans commune mesure** : équiper les 120 collaborateurs coûterait, sur trois ans, 50 + 3 × 20 = **110 k€**, contre 3 × 10 = **30 k€** pour l'outil de gestion des terminaux mobiles ; à comparer aux 30 k€ que le cabinet consacre chaque année à toute sa sécurité. L'écart de 80 k€ peut financer un outil de partage adapté et la sensibilisation ; l'authentification forte est déjà sans surcoût.
3. **Le risque est traité par le cloisonnement** : l'espace professionnel chiffré, verrouillé et effaçable à distance protège les données des clients en cas de perte ou de vol, ce qui répond à l'exigence du secret professionnel invoquée par M. MONTCLAVEL ; l'accès refusé aux appareils non enrôlés rend la règle effective.

**Deux conditions de réussite** (0,5 pt) parmi :
- une **charte informatique révisée** (elle date de 2015), qui fixe les règles d'usage des appareils personnels (enrôlement obligatoire pour accéder aux données du cabinet, code de verrouillage, signalement immédiat d'une perte, effacement limité à l'espace professionnel, respect des données privées), validée par le comité des associés et présentée à tous ;
- un **accompagnement** de l'enrôlement (assistance des techniciens, guide simple, période de transition avant le blocage des appareils non enrôlés, de préférence hors période fiscale) ;
- un **smartphone professionnel** pour ceux qui refusent l'enrôlement de leur appareil et dont la fonction l'exige ;
- des **outils officiels performants** à distance (partage de fichiers volumineux), faute de quoi les contournements persisteront.

**Réponses tolérées**
- Choix de l'interdiction, si le candidat prévoit un smartphone professionnel pour les fonctions qui l'exigent (associés, chefs de mission), en chiffre le coût sur trois ans à partir de l'annexe 1.4 et traite le risque de contournement.
- Solution mixte : smartphones professionnels pour les associés et les chefs de mission, usage encadré pour les autres collaborateurs.
- Micro-segmentation ou cloisonnement des accès aux applications proposé au titre du cloisonnement, s'il est relié à un constat ; gestion des seules applications professionnelles (MAM) préférée à la gestion de l'appareil entier (MDM) pour les appareils personnels, si elle est justifiée.
- Tunnel chiffré d'accès aux ressources du siège cité au titre du chiffrement.

**Erreurs fréquentes**
- *Zero Trust présenté comme un produit qu'il suffirait d'acheter*, ou comme une réponse à tous les risques (`ET-04` ; `JUR-S03`) — juste : un cadre d'architecture qui combine plusieurs dispositifs.
- *Authentification forte confondue avec un mot de passe complexe* (`ET-28`) — juste : au moins deux facteurs de nature différente.
- *Sigle MDM non développé, ou gestion des terminaux mobiles confondue avec la gestion des données de référence ou avec la gestion des applications* (`ET-13`).
- *Réglages techniques des équipements* ou *plan de continuité et de reprise* — non demandés (`JUR-T12`).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Le modèle Zero Trust, avis scientifique et technique de l'ANSSI (2021) | cadre d'architecture, pas un produit | `zero_trust_anssi` / F12 § 3 | en vigueur |
| Authentification forte, gestion des identités et des accès, appareils personnels et gestion des terminaux mobiles | dispositifs | F12 § 3 | notion de cours |
| Coût sur trois ans des deux options | 110 k€ contre 30 k€ | annexe 1.4 A ; F09 | calcul de tête |

---

### 1.3 – Gouvernance de la sécurité, souveraineté et sensibilisation (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques » ; `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ».
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ».
- §2.3 – Élaborer et piloter la gouvernance stratégique des données : `2.3.d` « Enjeux du Big Data, cloud computing, datacenters et souveraineté numérique ». Limite : « L'expertise technique des infrastructures (serveurs, réseaux) n'est pas attendue. »

**Annexes mobilisées** : annexes 1.1 (organigramme), 1.2 (composants et hébergement, moyens), 1.3 (incident B), 1.4 (positions, repères).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Rôles et responsabilités des cinq acteurs, appliqués au cas | 0,5 |
| a-2 | Deux mesures d'organisation qui répondent aux tensions de l'annexe 1.4 | 0,5 |
| b-1 | Souveraineté numérique définie (localisation, droit applicable, dépendance, réversibilité) | 0,5 |
| b-2 | Hébergement des données de paie apprécié à partir des annexes, deux mesures | 0,5 |
| c-1 | Programme de sensibilisation en trois actions adaptées au travail à distance et aux deux incidents | 0,5 |
| c-2 | Indicateur d'efficacité complet (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

La question est dense pour 13,5 minutes : un style télégraphique est admis ; pour l'item a-1, un tableau d'une ligne par acteur suffit.

*1.3 a) – Rôles et responsabilités, et réponses aux tensions*

| Acteur | Rôle et responsabilités dans la sécurité du cabinet |
|---|---|
| **Présidente et comité des associés** | approuvent la politique de sécurité et son budget, fixent le niveau de risque acceptable, arbitrent les désaccords entre bureaux (interdiction ou usage encadré des smartphones), suivent chaque trimestre les incidents et les indicateurs, comme le plan « CORLANDEAU 2030 », et se forment ; la directive NIS 2 retient cette responsabilité des organes de direction (annexe 1.4 C), qui est ici une bonne pratique, sans qu'il soit besoin de déterminer l'assujettissement du cabinet. Les **associés responsables de bureau** font appliquer la politique dans leur bureau, déclarent les arrivées et les départs, revoient les droits de leurs équipes. |
| **Responsable informatique** | pilote la sécurité au quotidien (fonction de responsable de la sécurité des systèmes d'information) : rédige la politique et la charte, propose les mesures, gère les incidents et le canal de signalement, organise la sensibilisation, contrôle le prestataire et les éditeurs, rend compte à la présidente. |
| **Prestataire informatique local** | exécute ce que prévoit son contrat (postes, réseau des bureaux, sauvegardes) ; son contrat doit être complété d'engagements de sécurité (chiffrement des postes, délai d'intervention, alerte en cas d'incident), car il « ne s'engage sur rien d'autre ». |
| **Éditeurs** | en mode SaaS, ils répondent de la sécurité de l'infrastructure, de l'application, de l'hébergement et de la disponibilité, et doivent offrir les moyens de sécurité (authentification forte, journaux, notification des incidents) ; le cabinet reste responsable de ses identités, de ses accès, de ses données et de leurs usages (responsabilité partagée, F03 § 5.2) : l'affirmation des éditeurs est donc exacte. |
| **Collaborateurs** | appliquent la charte, protègent leurs appareils, signalent sans délai toute anomalie ; ils sont la première ligne de défense, comme Mme BOURGALAT le 15 mars. |

(0,5 pt si les cinq acteurs sont traités et appliqués au cas.)

**Deux mesures d'organisation** (0,5 pt) parmi :
1. **Un comité de sécurité trimestriel**, présidé par la présidente, réunissant deux associés (dont un responsable de bureau), le responsable informatique et un représentant des collaborateurs : il arbitre les règles avant leur adoption par le comité des associés et suit les incidents. Il répond au désaccord entre M. MONTCLAVEL et Mme FÉRANDOUX, que seule la direction peut trancher, et donne la parole aux utilisateurs (Mme BOURGALAT).
2. **Une autorité fonctionnelle du responsable informatique sur les bureaux en matière de sécurité**, conférée par la politique approuvée par les associés : les procédures d'arrivée et de départ et la revue des droits deviennent obligatoires pour chaque bureau. Elle répond à « je ne peux rien imposer aux bureaux ». Pour éviter que le responsable informatique contrôle seul ce qu'il met en œuvre, un regard extérieur périodique (responsable de la sécurité à temps partagé, revue annuelle par un tiers) peut compléter le dispositif.
3. **Des règles construites et testées avec les utilisateurs** : authentification forte avec appareil de confiance pour limiter les demandes en période fiscale, outil de partage performant mis à disposition avant l'interdiction des stockages personnels ; elles répondent à Mme FÉRANDOUX et à Mme BOURGALAT, et à la présidente qui ne veut pas « de règles que personne n'appliquera ».

*1.3 b) – Souveraineté numérique et hébergement des données de paie*

La **souveraineté numérique** est la capacité d'une organisation (ou d'un État) à garder la maîtrise de ses données et de ses outils numériques : savoir où les données sont hébergées, quel droit s'applique à leur hébergeur (des lois extra-européennes peuvent contraindre un fournisseur à communiquer des données), limiter la dépendance à l'égard des fournisseurs et conserver la possibilité de reprendre ses données (réversibilité) (F07 § 8.5 ; F03 § 5.3) (0,5 pt).

**Appréciation et mesures** (0,5 pt) : les données de paie sont parmi les plus sensibles que le cabinet détienne — salaires, coordonnées bancaires et données personnelles d'environ 15 000 salariés de 900 clients —, et elles sont couvertes par le secret professionnel. Elles sont hébergées hors de l'Union européenne, chez un fournisseur dont le siège est lui-même hors de l'Union européenne, et le contrat ne dit rien du lieu d'hébergement : le cabinet ne maîtrise ni la localisation, ni le droit applicable, ni l'évolution de la situation (« à l'étude »). C'est un risque de confidentialité et d'image, au moment où des clients demandent comment leurs données sont protégées ; il contraste avec la production comptable, hébergée en France. Deux mesures parmi :
- **négocier un avenant** avec l'éditeur de paie : hébergement dans l'Union européenne à une date fixée, interdiction de changer de lieu ou de sous-traitant sans accord préalable, clause de réversibilité (restitution complète des données dans un format exploitable) ;
- **faire de la souveraineté un critère du prochain choix** si l'éditeur ne s'engage pas : offre hébergée dans l'Union européenne par un prestataire soumis au droit européen, en s'appuyant sur des repères reconnus (référentiel SecNumCloud de l'ANSSI, annexe 1.4 C ; référentiel du cloud de confiance du Cigref), avec un calendrier de migration hors période fiscale ;
- **informer les associés et les clients** de la situation et des mesures prises, et tenir à jour la liste des données confiées à chaque éditeur et de leur lieu d'hébergement.

*1.3 c) – Programme de sensibilisation et indicateur*

**Trois actions** (0,5 pt) :
1. **Une formation courte et obligatoire, accessible à distance**, pour chaque collaborateur et pour chaque renfort dès son arrivée, renouvelée chaque année avant la période fiscale : travail sur un réseau public, protection des appareils, stockage interdit hors des espaces du cabinet, reconnaissance de l'hameçonnage et des faux changements de coordonnées bancaires ; les associés la suivent en premier (exemplarité).
2. **Des campagnes d'hameçonnage simulé** chaque trimestre, dont une en période fiscale et une imitant une demande de changement de coordonnées bancaires, avec une explication immédiate pour ceux qui cliquent.
3. **Un canal de signalement unique et simple** (bouton de signalement dans la messagerie, adresse et numéro dédiés), et le partage du retour d'expérience des deux incidents de 2027, en valorisant le réflexe de Mme BOURGALAT, qui ne savait pas à qui s'adresser.

**Indicateur** (0,5 pt) :

| Nom | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de signalement des courriels d'hameçonnage simulé | nombre de destinataires qui ont signalé le courriel simulé par le canal dédié / nombre de destinataires de la campagne × 100 | outil de campagne d'hameçonnage simulé et boîte de signalement | trimestrielle | 70 % ou plus fin 2027 | apprentissage (BSC) |

**Réponses tolérées**
- Matrice de responsabilités (réalise, approuve, consulté, informé) au lieu d'un tableau des rôles, si les cinq acteurs y figurent.
- Recommandation de recruter un responsable de la sécurité distinct du responsable informatique, si elle est proportionnée à la taille du cabinet (180 salariés, équipe de trois personnes) ou remplacée par une fonction à temps partagé.
- Mesure de chiffrement des données de paie par des clés détenues par le cabinet, si elle reste un principe, sans technique.
- Indicateur « taux de clic » aux campagnes d'hameçonnage simulé (nombre de destinataires qui ont cliqué / nombre de destinataires × 100, cible 5 % ou moins fin 2027 ; le 15 mars, 3 destinataires sur 40 ont cliqué) ou « taux de collaborateurs formés » (cible 100 %), s'il est complet.

**Erreurs fréquentes**
- *Responsable de la sécurité décrit comme un technicien* (`ET-15`) ; *sécurité laissée à l'informatique et au prestataire* (`JUR-G05`) — juste : responsabilité de la direction, rôles répartis.
- *« En SaaS, la sécurité est l'affaire de l'éditeur »* (`ET-30` ; F03 § 5.2) — le cabinet reste responsable des accès et des données.
- *Hébergement souverain réduit à l'hébergement en France* (`ET-37`) ; *analyse juridique des transferts de données* — non demandée.
- *Assujettissement du cabinet à NIS 2 déterminé, ou NIS 2 confondue avec le RGPD* (`ET-10` ; `ET-41`) — l'annexe exclut cette analyse ; la directive n'est pas mise en œuvre en droit français au 31/12/2026.
- *Indicateur générique ou incomplet* (`ET-18` ; `JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Directive (UE) 2022/2555 (NIS 2), art. 20 : responsabilité et formation des organes de direction | rôle de la direction, sans assujettissement | `nis2` / F12 § 6.1 | en vigueur ; transposition due au 17/10/2024 |
| Projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité | non promulgué au 31/12/2026 | `nis2_transposition_fr` / F12 § 6.2 | non transposé |
| Comité de sécurité ; acteurs de la sécurité | mesures d'organisation | F02 § 6 ; F12 § 1 | notion de cours |
| Responsabilité partagée en mode SaaS ; souveraineté et réversibilité | rôles des éditeurs ; hébergement de la paie | F03 § 5.2 et 5.3 ; F07 § 8.5 | notion de cours |
| SecNumCloud, version 3.2 (ANSSI) ; référentiel du cloud de confiance du Cigref | repères de souveraineté | `secnumcloud_3_2`, `cigref_cloud_confiance` / F03 § 5.3 | en vigueur ; publié |
| Règlement (UE) 2016/679 (RGPD) | contrainte de sécurité des données de paie, sans analyse juridique | `rgpd` / F15 | en vigueur |

---

### 1.4 – Fiabiliser le processus de paiement des fournisseurs (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.e` « Fiabilisation des systèmes d'information comptables et décisionnels ».
- §1.3 – Diagnostiquer et piloter l'évolution des architectures et de l'urbanisation des systèmes d'information : `1.3.f` « Analyse des processus métiers et rôle des architectures SI dans leur rationalisation ».

**Annexes mobilisées** : annexes 1.3 A (processus en vigueur et incident) et 1.2 (accès à distance aux logiciels des clients, 300 clients concernés).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Donnée de référence définie ; importance du contrôle de sa modification expliquée | 0,5 |
| a-2 | Processus actuel représenté lisiblement (étapes, acteurs, outils, contrôles existants) | 0,5 |
| a-3 | Quatre failles qui ont permis la fraude | 0,5 |
| b | Processus rationalisé et fiabilisé avec les cinq contrôles, chacun attribué au cabinet ou au client ; 1 point pour trois ou quatre contrôles, 0,5 pour deux | 1,5 |

**Réponse attendue**

*1.4 a) – Donnée de référence, processus actuel et failles*

Une **donnée de référence** est une donnée stable et partagée qui décrit les objets de gestion — tiers (clients, fournisseurs) et leurs coordonnées bancaires, plan de comptes, articles — et que réutilisent de nombreuses opérations (F07 § 1). Sa modification est un **point de contrôle clé** d'un système d'information comptable : une seule modification erronée ou frauduleuse se propage à toutes les opérations suivantes (ici, tous les paiements au fournisseur) sans que le contrôle de chaque opération la révèle ; c'est la cible privilégiée de la fraude au faux ordre de virement. Contrôler la modification, à la source, est plus efficace que contrôler chaque paiement (F10 § 2 et § 3) (0,5 pt).

**Processus actuel** (0,5 pt, format libre) :

| Étape | Acteur | Outil | Contrôle existant |
|---|---|---|---|
| 1. Réception d'une demande de changement de coordonnées bancaires | collaborateur du cabinet (ou gérant) | messagerie | aucun : l'expéditeur n'est pas vérifié |
| 2. Modification de la fiche du fournisseur | le collaborateur qui a reçu la demande ; tout collaborateur du bureau peut le faire | logiciel de gestion du client, à distance | aucun : ni validation, ni trace de l'auteur et des anciennes coordonnées |
| 3. Préparation du fichier des paiements et dépôt sur l'espace bancaire | le même collaborateur | logiciel du client, espace bancaire en ligne | aucun état des fiches modifiées |
| 4. Validation du virement global | gérant | espace bancaire en ligne | montant total seulement |
| 5. Lettrage des paiements | collaborateur | comptabilité | a posteriori, sans rapprochement avec les fiches modifiées |

**Quatre failles** (0,5 pt) parmi :
1. **Aucune vérification de l'authenticité de la demande** par un canal indépendant : un courriel dont l'adresse différait d'une lettre a suffi, traité le jour même en télétravail.
2. **Cumul de fonctions incompatibles** : la même personne modifie les coordonnées bancaires et prépare les paiements ; tout collaborateur du bureau peut modifier une fiche (absence de séparation des tâches et de moindre privilège).
3. **Aucune piste d'audit** : le logiciel ne conserve ni l'auteur ni les anciennes coordonnées ; aucun état des modifications n'est produit.
4. **Validation du gérant sur le seul total**, sans la liste des bénéficiaires ni le signalement des coordonnées nouvellement modifiées : le contrôle final ne peut pas détecter la fraude.
5. **Aucun rapprochement détectif** entre fiches modifiées, paiements et relevés des fournisseurs : la fraude n'a été découverte que trois semaines plus tard, par la relance du véritable fournisseur, après deux paiements (30 000 €).
6. **Facteur humain** : aucune sensibilisation à ce type de fraude (annexe 1.2 B-6).

*1.4 b) – Processus rationalisé et fiabilisé* (1,5 pt)

Rationalisation : **un canal unique** pour les demandes de changement de coordonnées bancaires (dépôt sur le portail ou formulaire, jamais un simple courriel), **une procédure commune** aux 300 clients dont le cabinet tient les fiches fournisseurs, et des contrôles intégrés au logiciel plutôt que laissés à la vigilance de chacun.

| Étape du processus cible | Contrôle | Qui l'exerce |
|---|---|---|
| 1. Toute demande de changement est enregistrée « en attente » ; la fiche est bloquée pour les paiements tant que la modification n'est pas validée | **contrôle de la modification des données de référence** : la modification n'est effective qu'après validation par une seconde personne habilitée (contrôle « à quatre yeux » dans le logiciel) | cabinet (collaborateur qui saisit la demande), client (gérant qui valide) |
| 2. Vérification de la demande | **contre-appel** du fournisseur à un numéro déjà connu (fiche existante, contrat), jamais à celui qui figure dans la demande ; date et interlocuteur consignés | client (gérant ou personne qu'il désigne), ou cabinet sur délégation écrite du client |
| 3. Organisation des droits | **séparation des tâches** : le collaborateur qui saisit les modifications de fiches ne prépare pas les paiements ; droits limités au besoin dans le logiciel du client ; le gérant reste seul à valider les virements | cabinet (chef de mission, qui attribue les profils), client (gérant) |
| 4. Traçabilité | **piste d'audit** : journal des modifications de fiches (auteur, date, anciennes et nouvelles coordonnées), conservé et revu chaque mois ; à demander à l'éditeur du logiciel du client s'il n'existe pas | cabinet (chef de mission, revue mensuelle) |
| 5. Avant et après le paiement | **rapprochement** : avant chaque virement, état des bénéficiaires dont les coordonnées ont changé depuis le dernier paiement, présenté au gérant qui valide le détail et non le seul total ; après paiement, rapprochement des paiements et des relevés de comptes des fournisseurs, et revue des fiches modifiées lors de la révision | client (gérant, avant paiement), cabinet (collaborateur et chef de mission, après paiement) |

Ce processus combine des contrôles **préventifs** (blocage, validation, contre-appel, séparation des tâches) et **détectifs** (journal, rapprochements) ; il protège le client et le cabinet, dont les collaborateurs ne peuvent plus être instrumentalisés par un fraudeur.

**Réponses tolérées**
- Processus représenté par un logigramme, un diagramme en couloirs ou une notation BPMN, s'il est lisible (`JUR-T10`).
- Contre-appel confié au collaborateur du cabinet, si la délégation est formalisée et le numéro vérifié.
- Contrôle automatique par le logiciel (alerte sur le changement de coordonnées suivi d'un paiement dans un délai court) proposé en complément du rapprochement.
- Référence au COSO (contrôles préventifs et détectifs, contrôles applicatifs) pour structurer la réponse.

**Erreurs fréquentes**
- *Écritures comptables de la perte, analyse de la responsabilité du cabinet ou des diligences professionnelles* — hors du dossier, explicitement exclues.
- *Recommandations génériques* (« sensibiliser les collaborateurs ») sans contrôle attribué à un acteur (`JUR-T01`).
- *Validation par la même personne que celle qui modifie* — ce n'est pas une séparation des tâches.
- *Contre-appel au numéro figurant dans la demande frauduleuse*.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Données de référence | définition | F07 § 1 | notion de cours |
| Contrôles applicatifs, préventifs et détectifs ; séparation des tâches ; piste d'audit | processus fiabilisé | F10 § 2, § 3.1 et § 3.2 | notion de cours |
| COSO, Internal Control — Integrated Framework (2013) | réponse tolérée | `coso_2013` / F10 § 2 | en vigueur |
| Fraude au faux ordre de virement, contre-appel | menace et parade | F12 § 5 | notion de cours |

---

### 1.5 – L'intelligence artificielle au service de la détection des fraudes (2 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.f` « Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques » ; `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ».
- Limite (§1.3) : « L'usage de l'IA doit notamment être analysé dans ses effets métiers et non uniquement comme outil technique. »

**Annexes mobilisées** : annexes 1.4 B (proposition de l'éditeur) et C (repères), 1.3 (incidents), 1.2 (hébergement, moyens, budget de la sécurité) et 1.1 (secret professionnel, 3 000 clients).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Apprentissage automatique et IA générative distingués ; fonction 1 rattachée à l'apprentissage automatique, fonction 2 à l'IA générative | 0,5 |
| b-1 | Deux apports tirés des annexes | 0,5 |
| b-2 | Trois limites tirées des annexes | 0,5 |
| b-3 | Recommandation justifiée et deux conditions de mise en œuvre | 0,5 |

**Réponse attendue**

*1.5 a) – Deux familles d'IA* (0,5 pt)

L'**apprentissage automatique** regroupe les méthodes par lesquelles un modèle apprend, à partir de données (ici l'historique des écritures), à **classer, prédire ou repérer ce qui s'écarte de la normale** ; il produit un score ou une alerte dont on peut mesurer le taux d'erreur. L'**IA générative**, fondée sur de grands modèles de langage, **produit un contenu nouveau** (texte, image) en langage naturel, plausible mais non garanti exact (F13 § 1). La **fonction 1** (score de risque des écritures et des modifications de fiches) relève de l'apprentissage automatique ; la **fonction 2** (lecture des courriels et rédaction d'une explication) relève de l'IA générative.

*1.5 b) – Évaluation, recommandation et conditions*

**Deux apports** (0,5 pt) parmi :
- un **contrôle détectif systématique** sur les dossiers des 3 000 clients, impossible à réaliser à la main, qui vise précisément le schéma de la fraude FALVERGNE (changement de coordonnées bancaires suivi d'un paiement) ainsi que les factures en double ;
- une **détection de l'hameçonnage fondée sur le contenu** des courriels (urgence, demande de connexion, changement de banque), là où l'incident du 15 mars n'a été arrêté que par la vigilance d'une collaboratrice ; l'explication rédigée pour chaque alerte peut servir de **sensibilisation** au moment où le risque se présente ;
- des résultats annoncés encourageants (9 fraudes sur 10 signalées dans les tests de l'éditeur) pour un coût modéré (5 + 3 × 15 = 50 k€ sur trois ans).

**Trois limites** (0,5 pt) parmi :
- **les faux positifs** : 3 000 alertes par mois, dont neuf sur dix sans anomalie, soit environ **2 700 fausses alertes par mois**, à peu près une alerte par dossier et par mois ; la charge de traitement et la lassitude des alertes risquent de faire ignorer les vraies ;
- **l'explicabilité** : le score de 0 à 100 n'indique pas les critères qui l'ont produit ; le collaborateur ne peut ni vérifier l'alerte, ni la justifier auprès du client ;
- **les données des clients confiées** : les écritures des dossiers serviraient à entraîner un modèle commun à tous les cabinets, et le texte des courriels du cabinet serait lu par un modèle tiers hébergé hors de l'Union européenne ; le secret professionnel et la souveraineté des données (question 1.3 b) sont en jeu, l'anonymisation annoncée n'étant pas démontrée ;
- **les biais et la fiabilité annoncée** : « 9 sur 10 » mesuré dans les tests de l'éditeur, sur des données qui ne sont pas celles du cabinet ; une fraude sur dix échappe, et une fraude d'un type nouveau peut échapper davantage ; l'IA générative peut se tromper dans ses explications ;
- **la fausse promesse d'« alléger les contrôles manuels »** : le module signale mais ne bloque aucun paiement ; il complète les contrôles de la question 1.4, il ne les remplace pas ;
- **la dépendance à l'éditeur**, dont le modèle évolue sans que le cabinet le maîtrise.

**Recommandation et conditions** (0,5 pt) : **ne pas souscrire au module en l'état**. Les mesures prioritaires sont moins coûteuses et plus sûres : authentification forte (sans surcoût), contrôles du processus de paiement (question 1.4), sensibilisation. Le cabinet peut ensuite conduire un **pilote limité à la fonction 1**, sur un bureau et sur les clients dont il prépare les paiements, pour mesurer le taux de fausses alertes sur ses propres dossiers, et **refuser la fonction 2** tant que les courriels seraient traités hors de l'Union européenne. Deux conditions parmi :
- **une supervision humaine organisée** : chaque alerte est traitée par une personne désignée, dans un délai fixé, le seuil de score est ajusté pendant le pilote, et les contrôles de la question 1.4 sont maintenus ;
- **des engagements contractuels** : pas de réutilisation des données des dossiers pour entraîner le modèle sans l'accord du cabinet, hébergement dans l'Union européenne, accès aux critères de chaque alerte, possibilité de sortie si le taux de fausses alertes ne baisse pas à l'issue du pilote ;
- **la formation des utilisateurs** à la lecture des alertes et aux limites de l'outil, qui répond aussi à l'obligation de prendre des mesures pour favoriser la maîtrise de l'IA du personnel (article 4, assouplie par le règlement (UE) 2026/1744, annexe 1.4 C).

**Réponses tolérées**
- Souscription à la fonction 1 sans pilote, si les conditions de supervision humaine, de contrat et de formation sont posées et si le traitement des fausses alertes est organisé.
- Fonction 2 présentée comme mixte (classement des courriels par apprentissage automatique, explication rédigée par l'IA générative), si la distinction des deux familles est juste.
- Autre périmètre de pilote (bureau de Saintes, pôle social), s'il est justifié.

**Erreurs fréquentes**
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`).
- *Apports sans limites, ou l'inverse* (`ET-19`) ; *promesse de l'éditeur reprise sans critique* (`JUR-T03`).
- *Fonctionnement interne des modèles* (couches, entraînement) ou *qualification du module au titre du règlement sur l'IA* — non demandés ; l'annexe exclut cette analyse.
- *IA présentée comme remplaçant les contrôles* — elle signale, elle ne bloque rien.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Apprentissage automatique et IA générative | typologie | F13 § 1 | notion de cours |
| Usages de l'IA pour la fraude et la cybersécurité ; risques (biais, confidentialité, dépendance) | apports et limites | F13 § 2 et § 3 | notion de cours |
| Règlement (UE) 2024/1689 sur l'intelligence artificielle, modifié par le règlement (UE) 2026/1744 : maîtrise de l'IA (art. 4, modifié par le règlement (UE) 2026/1744), depuis le 02/02/2025 | condition de formation, sans qualification | `ai_act`, `omnibus_numerique_ia` / F13 § 5 | en vigueur ; application échelonnée |

---

## DOSSIER 2 – EXPLOITER LES DONNÉES DES CLIENTS AU SERVICE DU CONSEIL (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 2.1 Chaîne de traitement et organisation de la collecte | `2.2.b` Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ; `2.1.d` Normes et standards d'interopérabilité (XML, API, formats ouverts) ; `2.1.a` Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes | 3 |
| 2.2 Méthodes d'analyse et outil d'alerte | `2.2.c` Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model ; `2.2.a` Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique à l'aide d'outils de data visualisation | 3 |
| 2.3 Diagnostic de la production et restitution au comité des associés | `2.2.e` Représentation visuelle des résultats et formulation de diagnostics argumentés ; `2.2.d` Outils décisionnels : Excel avancé, Power BI, Tableau, etc. | 2 |
| 2.4 Indicateurs de pilotage de la transformation de la production | `3.1.d` Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ; `3.1.a` Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord | 2 |
| 2.5 Modèle économique et stratégie du système d'information | `1.1.d` Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques ; `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes | 3 |
| **Dossier 2 – Exploiter les données des clients au service du conseil** |  | **13** |

Répartition indicative : connaissances (chaîne de traitement, interopérabilité, méthodes d'analyse, tableau de bord équilibré, modèle économique, alignement stratégique) 3 points (items 2.1 a-1, 2.1 b-1, 2.2 a-1, 2.4-1, 2.5 a-1, 2.5 b-1) ; analyse des annexes et recommandations 10 points, soit environ 77 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 59 minutes.

---

### 2.1 – Chaîne de traitement et organisation de la collecte (3 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.b` « Chaîne de traitement des données : collecte, nettoyage, structuration, analyse, restitution ».
- §2.1 – Structurer, modéliser et sécuriser les données : `2.1.a` « Structurer et organiser les données dans le système d'information afin d'en garantir la cohérence, la qualité, la circulation fluide et l'interopérabilité avec d'autres systèmes » ; `2.1.d` « Normes et standards d'interopérabilité (XML, API, formats ouverts) ». Limites : « L'interopérabilité doit être abordée à la fois sur le plan technique et sur le plan organisationnel » ; le détail technique des échanges est exclu.

**Annexes mobilisées** : annexes 2.1 (canaux, traitements, offre de l'éditeur), 1.1 (3 000 clients, six bureaux, période fiscale, secret professionnel) et 2.4 (objectifs 2029, repères sur la facturation électronique).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Chaîne de traitement définie (suite organisée d'étapes qui transforme des données brutes de sources hétérogènes en informations fiables restituées pour décider), valeur limitée par le maillon le plus faible | 0,5 |
| a-2 | Cinq étapes appliquées aux données des clients du cabinet (canaux et flux, contrôles, rattachement au dossier, révision et analyse, comptes annuels et situations) | 0,5 |
| a-3 | Quatre faiblesses tirées de l'annexe 2.1, chiffrées et rattachées chacune à la bonne étape ; 0,5 dès trois faiblesses justes | 0,5 |
| b-1 | Interopérabilité définie, avec ses dimensions technique, sémantique et organisationnelle | 0,5 |
| b-2 | Quatre mesures de l'organisation cible (formats structurés et ouverts, API, nommage et rapprochement, accompagnement des clients), chacune reliée à une faiblesse et précisant ce qui change pour les clients ; 0,5 pour deux mesures | 1 |

**Réponse attendue**

*2.1 a) – Définition, chaîne du cabinet et faiblesses*

La **chaîne de traitement des données** est la suite organisée des opérations qui transforment des données brutes, issues de sources hétérogènes, en informations fiables, structurées et restituées à ceux qui décident : collecte, nettoyage, structuration, analyse, restitution. C'est une démarche, et non un outil : chaque étape a ses règles, ses responsables et ses contrôles, et la qualité du résultat se perd au maillon le plus faible (F08 § 1) (0,5 pt). Pour un cabinet, la matière première est la pièce du client : la chaîne va de la pièce déposée au conseil donné au dirigeant.

| Étape | Chaîne des données des clients de CORLANDEAU Expertise | Faiblesse constatée (annexe 2.1) |
|---|---|---|
| **Collecte** | 600 000 pièces par an, environ 200 par client, par quatre canaux (portail 250 000, application mobile 100 000, courriel 150 000, papier 100 000) ; relevés bancaires par flux automatisé pour 1 200 clients, en PDF ou sur papier pour 1 800 ; relevés de ventes des logiciels de caisse ou de facturation | **canaux non maîtrisés** : le papier n'est jamais intégré automatiquement et arrive en 45 jours ; 60 % des clients « papier » et 40 % des clients « courriel » avaient un dossier incomplet à la clôture, contre 20 % par le portail ; 30 % des dossiers incomplets, relances individuelles sans liste des pièces attendues ; **donnée structurée perdue** : les factures électroniques reçues par les clients depuis septembre 2026 arrivent en PDF ou imprimées |
| **Nettoyage** | contrôle des pièces lues automatiquement (date, montant, TVA, fournisseur), repérage des doublons, des pièces illisibles | **une pièce lue sur dix** comporte une erreur, corrigée à la révision, plusieurs semaines plus tard (plusieurs dizaines de milliers de pièces par an) ; **5 % de doublons** (30 000 pièces) repérés à la main |
| **Structuration** | rattachement de chaque pièce au bon dossier, au bon tiers et au bon mouvement bancaire ; classement | **aucune règle de nommage** (« scan_0012.pdf ») ; un même fournisseur sous plusieurs libellés, qui fausse les soldes ; rapprochement manuel pour 1 800 clients sans flux |
| **Analyse** | révision, contrôles de cohérence, préparation des déclarations, analyses pour le conseil | analyse tardive, faite sur des données incomplètes et corrigées tard ; aucune analyse en cours d'année pour 90 % des clients |
| **Restitution** | comptes annuels, déclarations, situations en cours d'année | comptes remis 98 jours après la clôture en moyenne ; situations pour **10 % des clients seulement**, à la main dans un tableur |

(0,5 pt pour la chaîne appliquée ; 0,5 pt pour au moins trois faiblesses chiffrées et bien rattachées.)

La faiblesse de fond est **organisationnelle** : chaque bureau collecte à sa façon (portail exigé à Poitiers, papier accepté sans limite à Saintes et à Châtellerault), et la chaîne s'arrête à la clôture : elle produit des comptes annuels, pas des données fraîches pour conseiller.

*2.1 b) – Interopérabilité et organisation cible de la collecte*

L'**interopérabilité** est la capacité de systèmes hétérogènes à échanger des données et à les utiliser sans intervention manuelle. Elle a une dimension **technique** (connexions, API : interfaces d'accès programmatique à un service), **syntaxique et sémantique** (formats structurés et ouverts, comme XML ou JSON, et sens partagé des données : mêmes libellés, mêmes référentiels de tiers) et **organisationnelle** (processus, responsabilités, engagements des parties) ; le programme exige les plans technique et organisationnel (F07 § 7) (0,5 pt).

| Mesure | Contenu (sans détail technique des échanges) | Faiblesse traitée | Ce qui change pour les clients |
|---|---|---|---|
| 1. **Données structurées plutôt qu'images** | récupérer les factures électroniques reçues par les clients **dans leur format structuré** (Factur-X, UBL ou CII : annexe 2.4 E), avec leur accord, au lieu de PDF relus par la lecture automatique ; demander les relevés de ventes dans un format ouvert et documenté ; réserver la photographie et le PDF aux pièces qui n'existent pas autrement | lecture automatique fautive une fois sur dix, donnée structurée perdue | le client n'envoie plus ses factures d'achat électroniques : il autorise une fois leur transmission ; il en dépose moins, et moins souvent |
| 2. **Connexions par API activées** | activer les connexions déjà comprises dans l'abonnement (annexe 2.1 C) : flux bancaires pour tous les clients qui l'acceptent (objectif 80 % fin 2029, contre 40 %), connexions aux logiciels de caisse et de facturation des clients | 1 800 clients sans flux, rapprochement manuel, données fraîches pour 40 % des clients seulement | le client autorise le flux auprès de sa banque et le renouvelle ; il ne dépose plus ses relevés ; ses données sont disponibles chaque jour pour le tableau de bord mensuel |
| 3. **Règles communes de nommage et de rapprochement** | fichier nommé automatiquement à l'arrivée (client, date, type de pièce), référentiel unique des tiers dans chaque dossier (un fournisseur, un libellé), détection des doublons à l'arrivée, rapprochement automatique pièce – mouvement bancaire ; un propriétaire des règles au pôle technique et un correspondant dans chaque bureau | noms de fichiers libres, tiers en double, 30 000 doublons, rapprochement manuel | le client dépose sans renommer ; il reçoit un accusé de réception et l'alerte « pièce déjà reçue » |
| 4. **Accompagnement des clients et règle commune aux six bureaux** | liste des pièces attendues par client et par mois, visible sur le portail, avec relances automatiques ; portail et application comme canaux normaux dans tous les bureaux, papier réservé à des cas définis et numérisé à l'accueil le jour même ; formation des clients (réunion, tutoriel, premier dépôt accompagné), en commençant par Saintes et Châtellerault ; engagement réciproque inscrit dans la lettre de mission (rythme de dépôt, délai de traitement du cabinet) | 30 % de dossiers incomplets, pratiques différentes selon les bureaux, papier sans limite | le client sait ce qu'il doit déposer et quand ; il est aidé à passer au portail ; il gagne des comptes plus rapides et un suivi en cours d'année |

(0,5 pt pour deux mesures, 1 pt pour quatre, chacune reliée à une faiblesse et à ce qui change pour le client.)

Ces mesures relèvent de l'objectif `2.1.a` : une donnée cohérente (règles, référentiel des tiers), de qualité (contrôle à la source, à l'arrivée) et qui circule sans ressaisie, du client au cabinet. Elles préparent l'offre « Pilotage dirigeant », qui suppose des données mensuelles fraîches. Le secret professionnel reste une contrainte : seules les données utiles à la mission sont collectées, avec l'accord du client pour chaque connexion.

**Réponses tolérées**
- Chaîne présentée selon le vocabulaire décisionnel (collecte, ETL, entrepôt, restitution), ou en six étapes avec la décision du dirigeant comme dernier maillon, si les cinq étapes du programme y figurent.
- Faiblesses qualifiées par les dimensions de la qualité des données (complétude, exactitude, unicité, actualité ; ISO/IEC 25012).
- Doublons ou erreurs de lecture rattachés à la collecte, si le candidat prévoit leur détection à l'arrivée.
- Interopérabilité présentée en quatre niveaux (technique, syntaxique, sémantique, organisationnel) ou en deux (technique et organisationnel), si le sens partagé des données apparaît.
- Rôle du portail public de facturation ou des plateformes agréées mentionné comme contexte, sans analyse des obligations de la réforme.
- Mesures regroupées autrement (une mesure « référentiel des tiers », une mesure « liste des pièces attendues »), si les quatre thèmes de la consigne sont couverts.

**Erreurs fréquentes**
- *Chaîne réduite à un outil* (`JUR-D02` BI réduite à un simple outil ; `ET-05`) — « il suffit d'activer la lecture automatique » ; juste : règles, responsables et contrôles à chaque étape, à commencer par la collecte.
- *Interopérabilité seulement technique* (`ET-36`) — API et formats sans accord du client, sans règle commune aux bureaux ni responsable ; juste : la dimension organisationnelle (clients, bureaux, propriétaire des règles) est demandée.
- *Détail technique des échanges ou modélisation des données* — description des appels d'une API, schéma de tables ; juste : rôle des API et des formats, en principe.
- *Mesures sans le client* (`JUR-T01` contextualiser chaque notion) — organisation pensée pour le cabinet seul ; juste : chaque mesure dit ce que le client fait de différent et ce qu'il y gagne.
- *Analyse juridique de la réforme de la facturation électronique* — obligations, calendrier détaillé, rôle des plateformes ; juste : la réforme est un contexte daté qui rend disponibles des données structurées.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Chaîne décisionnelle : collecte, nettoyage, structuration, analyse, restitution | définition et application | F08 § 1 | notion de cours |
| Interopérabilité : niveaux technique, sémantique, organisationnel ; API, formats ouverts | définition, mesures 1 à 3 | F07 § 7 | notion de cours |
| ISO/IEC 25012 (2008) — Modèle de qualité des données | dimensions de la qualité, à titre d'exemple | `iso_iec_25012` / F07 § 8.3 | en vigueur |
| Généralisation de la facturation électronique (article 91 de la loi de finances pour 2024) | factures structurées reçues par les clients depuis le 01/09/2026 | `facturation_electronique_fr` / annexe 2.4 E | en vigueur ; émission des PME au 01/09/2027 |

---

### 2.2 – Méthodes d'analyse et outil d'alerte (3 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.c` « Méthodologies d'analyse de données (descriptive, exploratoire, prédictive) adaptées au business model » ; `2.2.a` « Maîtriser l'ensemble de la chaîne de valeur des données pour produire des analyses pertinentes et éclairer la décision stratégique ». Limites : « Le développement d'algorithmes de machine learning n'est pas attendu » ; « L'usage des outils ne dispense pas d'une lecture critique des corrélations et biais ».

**Annexes mobilisées** : annexes 2.2 (offre, outil d'alerte, essai, avis) et 2.1 (flux bancaires, rythme des pièces).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Trois méthodes définies et distinguées (que s'est-il passé ? pourquoi ? que va-t-il se passer ?) | 0,5 |
| a-2 | Chaque méthode rattachée au bon service de l'offre, avec les données mobilisées et le résultat pour le dirigeant | 0,5 |
| b | Quatre angles d'analyse de l'essai, appuyés sur les chiffres de l'annexe 2.2 C ; 0,5 pour deux angles | 1 |
| c-1 | Trois conditions pour une aide à la décision (données, validation humaine et explication, gouvernance et suivi des résultats) | 0,5 |
| c-2 | Position argumentée sur la proposition de M. CHAMPEYRAC (refus de l'ouverture générale et de l'alerte automatique, déploiement progressif et encadré) | 0,5 |

**Réponse attendue**

*2.2 a) – Trois méthodes et trois services*

| Méthode | Définition | Service de l'offre | Données et résultat pour le dirigeant |
|---|---|---|---|
| **Descriptive** | que s'est-il passé ? Agrégats, évolutions, écarts à une référence | **tableau de bord mensuel** | trésorerie, marge brute, délais de paiement des clients et des fournisseurs, comparés au mois précédent et au même mois de l'année précédente : le dirigeant voit sa situation chaque mois au lieu de l'apprendre aux comptes annuels |
| **Exploratoire** | pourquoi ? Croisements, comparaisons, recherche de régularités et de valeurs atypiques | **entretien trimestriel** | marge par activité, par client, par saison ; délais de paiement par client : le chef de mission cherche avec le dirigeant les causes d'un écart (un client qui paie de plus en plus tard, une activité dont la marge se dégrade) ; les pistes sont à vérifier, pas des preuves |
| **Prédictive** | que va-t-il se passer ? Estimation d'une probabilité ou d'une tendance à partir de l'historique | **outil d'alerte** | niveau de risque de difficulté de trésorerie à douze mois, établi par apprentissage automatique : le cabinet peut appeler le dirigeant avant que la difficulté survienne ; il doit en apprécier la fiabilité, non construire le modèle |

(0,5 pt pour les trois définitions ; 0,5 pt pour les trois rattachements appliqués.)

Les trois méthodes s'enchaînent : la prévision ne vaut que si la description est fiable (données fraîches, question 2.1) et si l'exploration a confirmé les facteurs. L'analyse descriptive relève de l'informatique décisionnelle ; l'exploratoire et la prédictive mobilisent la science des données (F08 § 2 ; `ET-25`).

*2.2 b) – Analyse de l'essai sous quatre angles*

1. **Fausses alertes et difficultés non détectées.** Sur 400 clients, 100 alertes : 30 justes, **70 fausses** (sept sur dix) ; 40 clients ont connu une difficulté, dont **10 non détectés** (un sur quatre). L'outil détecte bien (trois difficultés sur quatre, l'argument de M. CHAMPEYRAC), mais il se trompe le plus souvent quand il alerte. Les deux erreurs n'ont pas le même coût : une fausse alerte inquiète un dirigeant à tort et fait perdre du temps aux chefs de mission ; une difficulté manquée prive le client du conseil promis et donne une fausse assurance. Le seuil du niveau élevé règle l'arbitrage entre les deux : l'abaisser détecterait plus de difficultés au prix de plus de fausses alertes.
2. **Corrélation et causalité.** Le modèle repère des clients qui **ressemblent** à ceux qui ont connu des difficultés, il n'explique pas pourquoi (Mme MONTÉGRIER). Le retard de déclaration fait monter le niveau de risque même quand il vient de pièces que le cabinet attendait : la variable mesure en partie l'organisation de la collecte, non la santé du client. Le secteur est associé au risque sans en être la cause : un restaurant en pleine forme est signalé parce qu'il est restaurant.
3. **Biais des données.** **Biais de fraîcheur** : 8 des 10 difficultés manquées concernent des clients sans flux bancaire, dont les pièces arrivent par trimestre ou à la clôture ; l'outil voit mal les clients dont les données sont anciennes, soit 60 % du cabinet (1 800 clients sans flux). **Biais de sélection** : modèle établi sur deux bureaux urbains et trois années ; il a peu vu la clientèle d'artisans, d'exploitations agricoles et d'associations de Saintes et de Châtellerault. **Biais sectoriel** : la restauration et le bâtiment font la moitié des fausses alertes (35 sur 70) pour un cinquième de l'échantillon (80 clients sur 400).
4. **Explicabilité au client.** L'écran affiche un niveau de risque sans les éléments qui l'ont déterminé. Or le conseil suppose d'expliquer : le chef de mission ne peut ni vérifier l'alerte, ni dire au dirigeant ce qu'il doit surveiller (« je ne peux pas appeler un dirigeant… », M. ORTELIER). Un niveau de risque inexpliqué, envoyé automatiquement, nuirait à la relation de confiance que l'offre veut créer.

(0,5 pt pour deux angles appuyés sur les chiffres, 1 pt pour les quatre.)

*2.2 c) – Trois conditions et position*

Trois conditions pour faire de l'outil une **aide à la décision**, non une décision automatique (0,5 pt) :
1. **Des données fraîches et représentatives** : n'appliquer l'outil qu'aux clients dont les données sont à jour (flux bancaire, pièces mensuelles, question 2.1) et l'afficher avec cette précision ; ne pas compter comme retard du client un retard dû au cabinet ; réévaluer le modèle sur les six bureaux et sur une nouvelle année avant de l'étendre.
2. **Un chef de mission qui vérifie, explique et décide** : chaque alerte est d'abord examinée par le chef de mission, qui connaît le dossier ; l'écran affiche les trois ou quatre éléments qui ont le plus pesé (trésorerie en baisse, clients qui paient plus tard) pour qu'il puisse les confronter à sa connaissance du client et les expliquer ; c'est lui qui décide d'appeler le dirigeant.
3. **Une gouvernance et un suivi des résultats** : un responsable de l'outil (l'analyste de données, avec l'associé porteur), une règle sur le seuil d'alerte, une revue trimestrielle des alertes justes, fausses et manquées par secteur et par bureau, et un indicateur de fiabilité suivi dans le temps ; l'accord du client pour cet usage de ses données, dans le respect du secret professionnel.

**Position** (0,5 pt) : il ne faut **pas** ouvrir l'outil à tous les clients dès septembre avec une alerte envoyée automatiquement au dirigeant. Dans les mêmes proportions, les 3 000 clients produiraient environ 750 alertes, dont quelque 525 fausses, à expliquer par une seule analyste et des chefs de mission en pleine reprise d'activité ; et l'outil est le moins fiable pour les clients dont les données sont anciennes, majoritaires. Je recommande de lancer en septembre 2027 le **tableau de bord mensuel** (descriptif, fiable dès que les données sont fraîches), de réserver l'outil d'alerte à un **usage interne** des chefs de mission, d'abord pour les clients à données fraîches de deux ou trois bureaux, puis de l'ouvrir aux clients, comme support d'un échange avec le chef de mission, quand la revue des résultats aura montré moins de fausses alertes et que le flux bancaire sera généralisé.

**Réponses tolérées**
- Analyse **diagnostique** citée pour l'entretien trimestriel, à la place de l'exploratoire ou en complément ; analyse **prescriptive** mentionnée comme prolongement.
- Lecture des résultats en termes de « faux positifs » et « faux négatifs », de précision et de rappel, sans calcul au-delà des lectures de tête de l'annexe.
- Biais présentés comme un **biais de confirmation** possible du chef de mission (ne retenir que les alertes qui confirment son opinion), en plus des biais des données.
- Position favorable à une ouverture rapide, si elle est limitée à des clients volontaires à données fraîches, sans alerte automatique et avec validation par le chef de mission.
- Condition de sobriété des données : ne collecter que les données nécessaires à l'outil.

**Erreurs fréquentes**
- *Corrélation présentée comme causalité* (`ET-26` ; `JUR-D06` prudence d'interprétation) — « les restaurants sont en difficulté » ; juste : le secteur est un facteur associé, le niveau de risque désigne des ressemblances.
- *« Trois sur quatre détectées » pris pour la fiabilité de l'outil* — sans voir que sept alertes sur dix sont fausses ; juste : lire les deux erreurs et leur coût.
- *Construction d'un modèle prédictif* — choix d'algorithme, variables à ajouter, paramétrage ; juste : apprécier la fiabilité et les conditions d'usage (limite du programme).
- *Outil d'alerte confondu avec l'IA générative* (`ET-09`) — « l'outil rédige l'alerte » ; juste : apprentissage automatique qui classe les clients par niveau de risque.
- *Analyse juridique* — droit des entreprises en difficulté, procédures, obligations déontologiques ; juste : analyse de la donnée et de son usage pour conseiller.
- *Méthodes récitées sans application* (`JUR-T01`) — descriptive, exploratoire, prédictive définies sans les trois services.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Méthodes d'analyse descriptive, exploratoire, prédictive, prescriptive ; BI et science des données | association aux trois services | F08 § 2 | notion de cours |
| Corrélation et causalité, biais de sélection, de fraîcheur et de confirmation | analyse de l'essai | F08 § 5 | notion de cours |
| Apprentissage automatique : classement par niveau de risque, biais, explicabilité, revue des résultats | outil d'alerte, conditions | F13 § 1 et 3 | notion de cours |

---

### 2.3 – Diagnostic de la production et restitution au comité des associés (2 points)

**Référence au programme**
- §2.2 – Collecter, traiter, analyser et interpréter des données à des fins décisionnelles : `2.2.e` « Représentation visuelle des résultats et formulation de diagnostics argumentés » ; `2.2.d` « Outils décisionnels : Excel avancé, Power BI, Tableau, etc. ». Limites : « L'usage des outils ne dispense pas d'une lecture critique des corrélations et biais » ; « L'interprétation doit être reliée à la stratégie globale ».

**Annexes mobilisées** : annexes 2.3 (indicateurs par bureau, précisions, outils) et 2.4 (honoraires, objectifs 2029).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Deux constats chiffrés, chacun avec une hypothèse d'explication tirée des précisions de l'annexe 2.3 B | 0,5 |
| a-2 | Deux précautions de lecture tirées des annexes et conclusion reliée au plan « CORLANDEAU 2030 », en douze lignes au maximum | 0,5 |
| b-1 | Une représentation adaptée à chaque constat et au comité des associés (message, type de graphique, comparaison et cible) | 0,5 |
| b-2 | Outil de visualisation recommandé et justifié par le cas (sources, rafraîchissement, une seule définition), avec ses conditions (démarche, définitions communes, compétences) | 0,5 |

**Réponse attendue**

*2.3 a) – Diagnostic argumenté (note modèle)*

<!-- note -->
Constat 1 : là où le portail est adopté, la saisie recule. À Poitiers, Niort et La Rochelle, 80 % des clients l'utilisent et la saisie est passée de 12 à 8 h par client ; à Saintes et à Châtellerault, le portail stagne à 25 % et la saisie reste à 15 h. Hypothèse : le portail et la lecture automatique suppriment de la saisie, mais une clientèle d'artisans, d'exploitations et d'associations dépose encore sur papier. Constat 2 : le temps libéré ne devient pas du conseil. Pour le même gain de 4 h, le conseil passe de 7 % à 14 % à La Rochelle, de 7 % à 8 % à Poitiers et à Niort. Hypothèse : seule La Rochelle a réorganisé son travail (cellule dédiée, formation). Précautions : ce sont des associations entre bureaux de taille et de clientèle différentes, pas des causes ; la part du conseil monte aussi quand la tenue baisse (−0,5 M€) : la lire avec son montant ; le délai de Niort tient à des départs et à une autre définition. Conclusion : le portail ne suffit pas, il faut organiser le conseil.
<!-- /note -->

(0,5 pt pour les deux constats et leurs hypothèses ; 0,5 pt pour deux précautions et la conclusion.)

*2.3 b) – Représentations et outil décisionnel*

| Constat | Message pour le comité | Représentation | Pourquoi |
|---|---|---|---|
| 1. Portail et saisie | « là où le portail est utilisé, la saisie recule » | **nuage de points** : taux d'utilisation du portail en abscisse, heures de saisie par client en ordonnée, une bulle par bureau proportionnelle au nombre de clients, une flèche de 2025 à 2026, la cible de 6 h en ligne horizontale ; ou barres triées par bureau | montre la relation entre deux variables et la trajectoire de chaque bureau ; la cible situe l'effort restant ; le titre rappelle qu'il s'agit d'une association |
| 2. Temps libéré et conseil | « le temps libéré ne devient du conseil que là où le bureau s'est organisé » | **barres groupées** par bureau : part des honoraires de conseil en 2025 et 2026, axe partant de zéro, ligne de la cible de 20 % en 2030 ; en appui, le gain d'heures de saisie de chaque bureau | compare des catégories et l'écart à la cible ; l'axe à zéro évite d'amplifier des écarts d'un point |

(0,5 pt pour deux représentations adaptées.)

**Outil recommandé** (0,5 pt) : l'**outil de visualisation** déjà acquis (12 k€ par an, 15 licences, trois utilisateurs), plutôt que les six classeurs de tableur. Il se connecte directement au logiciel de production et au logiciel de temps, rafraîchit les données chaque nuit et publie un même tableau de bord pour tout le comité, au lieu d'une synthèse refaite à la main chaque trimestre à partir de six classeurs aux définitions différentes. Conditions : la décision n'est pas d'acheter un outil mais de conduire une démarche décisionnelle : des définitions communes à tous les bureaux (le délai court jusqu'à l'envoi des comptes partout, y compris à Niort), un responsable des données de production, des utilisateurs formés au-delà de l'analyste et de deux associés. Le tableur reste utile aux analyses ponctuelles d'un bureau.

**Réponses tolérées**
- Constats différents s'ils sont chiffrés et tirés de l'annexe 2.3 : délai des comptes annuels plus court là où la dématérialisation progresse (Poitiers, La Rochelle), écart persistant entre les bureaux urbains et ceux de Saintes et de Châtellerault.
- Hypothèse du constat 1 fondée sur l'activation des flux bancaires ou sur l'obligation du portail pour les nouveaux clients à Poitiers (annexe 2.1 B).
- Précautions différentes : deux années seulement, moyennes par bureau qui masquent la dispersion entre collaborateurs, heures déclarées et non mesurées.
- Une seule représentation de type tableau de bord d'une page réunissant les deux graphiques, ou des petits graphiques identiques par bureau, si chaque constat y trouve sa représentation.
- Tableur avancé retenu pour une phase transitoire, si ses limites sont montrées (classeurs multiples, saisie manuelle, définitions divergentes).

**Erreurs fréquentes**
- *Corrélation présentée comme causalité* (`ET-26` ; `JUR-D06`) — « le portail fait baisser les heures de saisie, donc il suffit de l'imposer » ; juste : association entre bureaux, clientèles différentes.
- *Part du conseil lue sans son dénominateur* — hausse attribuée au seul développement du conseil alors que les honoraires de tenue baissent.
- *Diagnostic sans lien avec la stratégie* (limite du programme) — chiffres commentés sans conclusion sur le plan « CORLANDEAU 2030 ».
- *BI réduite à un outil* (`JUR-D02` ; `ET-05`) — « l'outil de visualisation résoudra le problème » ; juste : définitions communes, responsables, compétences.
- *Manipulation d'outil* — étapes de construction du graphique dans le logiciel ; juste : choix argumenté sur papier.
- *Représentation inadaptée* — secteurs pour comparer six bureaux, axe tronqué pour des écarts d'un point.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Choix du graphique selon le message, biais de lecture, corrélation et causalité | diagnostic, représentations | F08 § 5 | notion de cours |
| Outils décisionnels : fonctions, limites, critères de choix ; BI comme démarche | recommandation de l'outil | F08 § 6 | notion de cours |

---

### 2.4 – Indicateurs de pilotage de la transformation de la production (2 points)

**Référence au programme**
- §3.1 – Concevoir, construire et exploiter des outils de pilotage de la performance : `3.1.a` « Mettre en œuvre des dispositifs de pilotage de la performance SI, en intégrant une analyse fine des coûts, des indicateurs et des leviers d'optimisation via des tableaux de bord » ; `3.1.d` « Construction et suivi de tableaux de bord SI (KPI, équilibrage performance / risques / coûts) ». Limite : « Le pilotage stratégique par les indicateurs suppose une capacité de recul critique ».

**Annexes mobilisées** : annexes 2.4 (objectifs fin 2029, coût horaire, honoraires), 2.1 (canaux, dossiers incomplets, flux bancaires) et 2.3 (heures de saisie, délais).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Tableau de bord équilibré défini (ensemble restreint d'indicateurs reliés à un objectif, équilibrant résultats et leviers, performance, risques et coûts ; Balanced Scorecard) et équilibre du choix justifié | 0,5 |
| 2 | Quatre indicateurs complets (formule, source, fréquence, cible tirée des annexes, axe), pertinents pour la transformation de la production et couvrant performance, risques et coûts ; 1 pour trois, 0,5 pour deux | 1,5 |

**Réponse attendue**

Un **tableau de bord équilibré** est un ensemble restreint d'indicateurs choisis pour piloter un objectif, présentés pour décider (cible, tendance, responsable) ; dans l'esprit du Balanced Scorecard (Kaplan et Norton, 1992), décliné au SI par l'IT Balanced Scorecard (Van Grembergen), il équilibre les résultats et leurs leviers, et, pour un projet de transformation, la performance, les risques et les coûts (F09 § 4) (0,5 pt). Celui de la transformation de la production relie la chaîne de collecte (question 2.1) à l'objectif du plan : libérer du temps pour le conseil.

| Dimension | Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|---|
| Performance (levier) | Taux d'intégration automatique des pièces | pièces intégrées automatiquement dans les dossiers, sans ressaisie / pièces reçues sur la période | logiciel de production comptable (journal de la lecture automatique et des flux) | mensuelle | 80 % fin 2029 (220 000 pièces sur 600 000 en 2026, un peu plus d'une sur trois) | processus |
| Coûts | Coût de saisie et de rapprochement par client | heures de saisie et de rapprochement déclarées sur douze mois × coût horaire moyen chargé (50 €) / nombre de clients en tenue | logiciel de temps ; coût horaire issu de la paie du cabinet | trimestrielle, sur douze mois glissants | 300 € fin 2029 (6 h × 50 €), contre 500 € en 2026 (10 h × 50 €) | financier |
| Risques (qualité des données) | Taux de dossiers incomplets à la clôture | dossiers auxquels manquent des pièces de la liste des pièces attendues à la date de clôture / dossiers en tenue | logiciel de production comptable (liste commune des pièces attendues et suivi des relances) | mensuelle de janvier à mai, bilan annuel | 10 % fin 2029 (30 % à la clôture 2026), suivi par bureau et par canal principal | processus |
| Performance (résultat) | Part des honoraires de conseil dans le chiffre d'affaires | honoraires de conseil aux dirigeants facturés / honoraires totaux du cabinet | facturation et comptabilité du cabinet | trimestrielle, cumul sur douze mois | 20 % en 2030 (7 % en 2025, 9 % en 2026) | financier |

(0,5 pt par indicateur complet et pertinent au-delà du premier : 1,5 pt pour quatre, 1 pt pour trois, 0,5 pt pour deux.)

Les deux premiers mesurent le levier de la transformation et son coût, le troisième le principal risque (des données incomplètes, qui retardent les comptes et faussent le conseil), le quatrième le résultat attendu par le plan. Lu ensemble, le tableau de bord évite le piège du constat 2 de la question 2.3 : des heures de saisie en baisse sans hausse du conseil signalent un temps libéré non réinvesti. Le quatrième indicateur se lit avec le montant des honoraires de conseil, car sa part monte aussi quand les honoraires de tenue baissent.

**Réponses tolérées**
- Part des clients dont les relevés bancaires arrivent par flux automatisé (clients dont le flux est actif / clients en tenue, cible 80 % fin 2029), délai moyen de remise des comptes annuels (cible 75 jours), taux de départ des clients (axe client, cible sous 5 % : 150 TPE parties en 2026), part des chefs de mission formés à l'entretien de conseil (axe apprentissage), à la place d'un des indicateurs du corrigé.
- Heures de saisie par client (cible 6 h) comme indicateur de performance, si le coût est suivi par un autre indicateur.
- Taux d'erreurs de lecture automatique (pièces corrigées / pièces lues automatiquement, une sur dix en 2026) comme indicateur de risque, avec une cible justifiée.
- Taux de dossiers incomplets rattaché à l'axe client ; part du conseil rattachée à l'axe client.

**Erreurs fréquentes**
- *Indicateurs incomplets ou génériques* (`JUR-A02` distinguer et justifier les indicateurs ; `ET-18`) — « taux de dématérialisation » sans formule, source, fréquence ni cible ; juste : cinq champs, cibles du séminaire (annexe 2.4 C).
- *Tableau de bord limité à la performance* (`ET-18`) — aucun indicateur de risque ni de coût, contrairement à la consigne.
- *Indicateurs du SI technique* — disponibilité des serveurs, tickets d'assistance ; juste : indicateurs de la transformation de la production.
- *Calcul d'écarts budgétaires ou tarification* — décomposition d'écarts, prix de l'offre ; juste : rapports simples de deux chiffres ronds.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Balanced Scorecard (Kaplan et Norton, 1992) ; IT Balanced Scorecard (Van Grembergen) | tableau de bord équilibré | `van_grembergen_it_bsc` / F09 § 4.1 | modèle publié |
| Fiche d'indicateur à cinq champs ; tableau de bord restreint | indicateurs | F08 § 3 ; F09 § 4 | notion de cours |

---

### 2.5 – Modèle économique et stratégie du système d'information (3 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.d` « Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques » ; `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ». Limites : « Ne pas confondre alignement stratégique et simple adéquation technique » ; « Ne pas se limiter à une veille passive : intégrer l'analyse prospective dans l'évaluation des opportunités SI ».

**Annexes mobilisées** : annexes 2.4 (honoraires, concurrence, attentes, temps, budget du SI, objectifs, positions, repères), 1.1 (plan « CORLANDEAU 2030 »), 2.1 (offre de l'éditeur), 2.2 (offre « Pilotage dirigeant ») et 2.3 (bureaux).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Modèle économique défini (manière dont l'organisation crée de la valeur pour ses clients, la produit avec ses ressources et en tire ses revenus) | 0,5 |
| a-2 | Effets de l'automatisation et des données analysés sous les trois angles, chacun appuyé sur l'annexe 2.4 ; 0,5 pour deux angles | 1 |
| b-1 | Alignement stratégique défini (mise en cohérence permanente et réciproque de la stratégie du SI et de la stratégie de l'organisation), sans le réduire à un choix d'outil ; la référence au modèle SAM est valorisée sans être exigée | 0,5 |
| b-2 | Trois priorités hiérarchisées, chacune justifiée par les annexes et reliée à l'objectif de développer le conseil ; 0,5 pour deux | 1 |

**Réponse attendue**

*2.5 a) – Effet de l'automatisation et des données sur le modèle économique*

Le **modèle économique** décrit la manière dont une organisation crée de la valeur pour ses clients (proposition de valeur), la produit avec ses ressources et ses activités clés, et en tire ses revenus. Les technologies de l'automatisation et de la donnée le transforment : il s'agit d'en analyser l'impact, dans une démarche de veille active, pour orienter la stratégie (F01 § 0) (0,5 pt).

| Angle | Modèle actuel | Effet de l'automatisation de la saisie | Effet de l'exploitation des données |
|---|---|---|---|
| **Proposition de valeur** | produire des comptes et des déclarations fiables, une fois l'an | la tenue devient une commodité : les plateformes en ligne la proposent pour moins de 100 € par mois ; 150 TPE sont parties en 2026 ; la valeur ne tient plus à la saisie | une valeur nouvelle : aider le dirigeant à décider en cours d'année ; 60 % des clients veulent un point régulier sur leur trésorerie, 45 % jugent que le cabinet intervient trop tard, 30 % paieraient un tableau de bord mensuel |
| **Ressources** | des collaborateurs qui consacrent un quart de leur temps à la saisie, au rapprochement et aux relances ; un SI centré sur la production (80 % du budget pour faire fonctionner l'existant) | du temps libéré : 4 heures de moins par client si l'objectif de 6 h est atteint, soit environ 12 000 heures par an sur 3 000 clients ; mais il ne devient du conseil que là où le bureau s'organise (La Rochelle, annexe 2.3) | de nouvelles ressources clés : des données fraîches et fiables (flux, formats structurés), des compétences d'analyse (une seule analyste aujourd'hui), des chefs de mission formés à l'entretien, la confiance des clients qui confient leurs données, sous la contrainte du secret professionnel |
| **Revenus** | des honoraires de tenue forfaitaires (14 M€, 64 % des honoraires), en baisse (−0,5 M€ en 2026, −10 % sur le forfait d'une TPE en deux ans) | pression continue sur les forfaits : le gain de productivité est capté par les clients si le cabinet ne fait que baisser ses coûts | des revenus de conseil récurrents, sur abonnement (2 M€ en 2026, 9 % ; objectif 20 % en 2030) : moins dépendants du volume de pièces et mieux protégés de la concurrence des plateformes |

(0,5 pt pour deux angles, 1 pt pour les trois, appuyés sur l'annexe 2.4.)

Le débat du séminaire en découle : automatiser pour baisser les coûts (Mme FERNIAC) protège un temps la tenue mais aligne le cabinet sur des concurrents moins chers ; s'appuyer sur les données pour vendre du conseil (M. CHAMPEYRAC) change la proposition de valeur mais suppose des ressources que le cabinet n'a pas encore. Les deux se complètent : l'automatisation finance et libère le temps du conseil.

*2.5 b) – Stratégie du SI alignée et trois priorités*

L'**alignement stratégique** est la mise en cohérence permanente et réciproque de la stratégie du SI avec la stratégie de l'organisation. Le modèle SAM de Henderson et Venkatraman (1993) peut l'éclairer, sans être exigé : la technologie peut aussi ouvrir une stratégie nouvelle. Il ne se réduit ni à un choix d'outil ni à une standardisation logicielle (F01 § 1) (0,5 pt). Ici, la stratégie métier est fixée : faire du conseil un relais de croissance, sans perdre la tenue. Mme VARENNAT ne veut pas « un projet informatique de plus » : le SI doit être réorienté de la production vers la donnée.

Trois priorités, dans l'ordre (1 pt) :
1. **Fiabiliser et fluidifier la collecte des données des clients** (priorité absolue, condition des deux autres) : activer les connexions déjà comprises dans l'abonnement (flux bancaires pour 80 % des clients, factures structurées, logiciels de caisse), règles communes de nommage, de rapprochement et de pièces attendues dans les six bureaux (question 2.1). Justification : sans données fraîches, ni le tableau de bord mensuel ni l'outil d'alerte ne fonctionnent (8 difficultés manquées sur 10 chez des clients sans flux) ; c'est aussi le moyen d'atteindre 6 h de saisie par client et de résister aux plateformes.
2. **Construire un socle décisionnel commun au service du conseil** : un entrepôt de données de production et de clients alimenté automatiquement, des définitions partagées, l'outil de visualisation déjà acquis comme couche de restitution pour le comité et pour les clients (tableau de bord mensuel), des compétences d'analyse renforcées au-delà d'une seule analyste et un responsable des données. Justification : l'offre « Pilotage dirigeant » et le pilotage de la transformation (questions 2.3 et 2.4) reposent sur la même donnée ; aujourd'hui, six classeurs et des définitions divergentes.
3. **Mettre le SI au service d'un nouveau métier de conseil, avec des règles d'usage des données** : outils du chef de mission (préparation de l'entretien trimestriel, alertes expliquées et validées), accord des clients et respect du secret professionnel, revue des résultats de l'outil d'alerte, veille active sur les plateformes concurrentes et les usages des données ; rééquilibrer le budget du SI au profit des projets (20 % aujourd'hui). Justification : le conseil vendu sur la base des données des clients engage la confiance ; l'exemple de La Rochelle montre que le temps libéré ne devient du conseil que s'il est organisé.

Cet ordre répond aux deux positions du séminaire : la première priorité sert l'automatisation de la tenue voulue par Mme FERNIAC, les deux suivantes le conseil voulu par M. CHAMPEYRAC, dans une même trajectoire.

**Réponses tolérées**
- Modèle économique présenté en neuf blocs (proposition de valeur, segments de clients, canaux, relations, flux de revenus, ressources clés, activités clés, partenaires, structure de coûts), si les trois angles demandés sont appliqués au cas.
- Analyse par la chaîne de valeur (Porter, 1985) : l'automatisation fait de la production une activité de commodité, la valeur se déplace vers le conseil.
- Priorités ordonnées autrement (socle décisionnel avant la collecte), si la dépendance entre la qualité des données et l'offre de conseil est explicitée.
- Référence au modèle SAM et à l'une de ses perspectives d'alignement, valorisée si elle est appliquée au cas.
- Une priorité consacrée aux compétences (analystes, formation des chefs de mission au conseil et à la lecture des données), si elle reste une priorité de la stratégie du SI et non un plan de formation détaillé.

**Erreurs fréquentes**
- *Alignement réduit à un choix d'outil* (`ET-06` ; `JUR-G02`) — « la stratégie consiste à généraliser l'outil de visualisation » ; juste : priorités dérivées de l'objectif de développer le conseil.
- *Modèle économique décrit sans effet des technologies* (`JUR-T03` analyser et argumenter) — description du cabinet sans analyse de ce que l'automatisation et les données changent.
- *Opportunités sans risques* (`ET-19`) — conseil fondé sur les données présenté comme acquis, sans les compétences, la qualité des données ni la confiance des clients.
- *Schéma directeur complet* (`ET-07`) — diagnostic, cible, portefeuille et budget de tout le SI ; juste : trois priorités hiérarchisées.
- *Tarification de l'offre ou calcul de rentabilité* — prix de l'abonnement, retour sur investissement ; juste : analyse qualitative appuyée sur les ordres de grandeur de l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Strategic Alignment Model (Henderson et Venkatraman, 1993) | stratégie du SI alignée, référence valorisée sans être exigée | `henderson_venkatraman_1993` / F01 § 1 | modèle publié |
| Chaîne de valeur (Porter, 1985) | réponse tolérée | `porter_chaine_valeur_1985` / F01 § 2 | modèle publié |
| Veille active et analyse de l'impact des technologies sur le modèle économique | effet de l'automatisation et des données | F01 § 0 (1.1.d) | notion de cours |
| DAMA-DMBOK, 2e édition (2017) | gouvernance des données du socle décisionnel, à titre d'exemple | `dama_dmbok2` / F07 § 8.2 | en vigueur |

---

## DOSSIER 3 – ÉVALUER LE PILOTE DE LA BASE DE CONNAISSANCES ET CONDUIRE SA GÉNÉRALISATION (13 points)

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Stratégie de gestion des connaissances et environnement existant | `1.6.a` Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle ; `1.6.b` Architecture fonctionnelle des systèmes de knowledge management (connaissances tacites et explicites) ; `1.6.d` Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums | 2,5 |
| 3.2 Audit post-implémentation du pilote | `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 3 |
| 3.3 Méthode de conduite de la généralisation et cahier des charges | `1.5.b` Méthodologies de gestion de projet (cycle en V, agile, hybride) ; `1.5.c` Élaboration d'un cahier des charges fonctionnel et technique | 2 |
| 3.4 Risques, plan qualité et recette de la généralisation | `1.5.e` Identification et gestion des risques (maintenance, évolutivité, sécurité) ; `1.5.f` Mise en œuvre et contrôle du plan qualité | 2 |
| 3.5 Appropriation et gouvernance du dispositif | `1.6.e` Leviers d'appropriation et de transformation des pratiques professionnelles ; `1.6.c` Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) | 2 |
| 3.6 Choix du service d'IA et transition numérique responsable | `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 1,5 |
| **Dossier 3 – Évaluer le pilote de la base de connaissances et conduire sa généralisation** |  | **13** |

Répartition indicative : connaissances (connaissances explicites et tacites, audit post-implémentation, critères d'appréciation, cycle en V et démarche agile, cahier des charges fonctionnel, plan qualité, transition numérique responsable) 2,5 points (items 3.1 a-1, 3.2 a pour moitié, 3.2 b-1 pour moitié, 3.3 a-1 pour moitié, 3.3 b pour un quart, 3.4 b-1 pour moitié, 3.6-1 pour moitié) ; analyse des annexes et recommandations 10,5 points, soit environ 81 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Stratégie de gestion des connaissances et environnement existant (2,5 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.a` « Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle » ; `1.6.b` « Architecture fonctionnelle des systèmes de knowledge management » (connaissances tacites et explicites) ; `1.6.d` « Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums ». Limites : « La gestion des connaissances dépasse la seule numérisation de l'information » ; « Le pilotage nécessite une approche systémique : outils, processus, culture » ; « Le lien avec la gestion des compétences (RH) est complémentaire mais distinct ».

**Annexes mobilisées** : annexes 3.1 (sources, questions répétées, associés proches de la retraite, outils existants), 3.2 (dispositif du pilote) et 1.1 (plan « CORLANDEAU 2030 », pôle technique).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Connaissances explicites et tacites distinguées et illustrées par le cas (notes, fiches, modèles ; expérience des associés proches de la retraite) | 0,5 |
| a-2 | Trois axes de stratégie, chacun relié à la connaissance visée et à l'apport ou à la limite de la base et de l'assistant ; dispositif systémique (outils, processus, culture) ; 0,5 dès deux axes appliqués | 0,5 |
| b | Quatre éléments (GED, intranet, forum, dossiers partagés), chacun conservé, transformé ou abandonné, avec une justification tirée de l'annexe 3.1 et son articulation avec la base ; 1 pour trois éléments, 0,5 pour deux | 1,5 |

**Réponse attendue**

*3.1 a) – Connaissances explicites et tacites ; trois axes de stratégie*

Une **connaissance explicite** est formalisée et transmissible sans son auteur : document, procédure, modèle ; au cabinet, les 300 notes du pôle technique, les réponses données par courriel, les modèles de lettres de mission et de dossiers de travail, la doctrine des bases des éditeurs. Une **connaissance tacite** est incorporée à la personne, issue de l'expérience, difficile à formaliser et liée au contexte : la manière dont M. VERDALHAC conduit un dossier difficile d'association, ce qu'il vérifie en priorité, ce qui a déjà posé problème chez un client semblable (annexe 3.1 C) (F06 § 1) (0,5 pt).

La stratégie de gestion des connaissances organise la création, le partage, la mise à jour et la réutilisation de ces deux formes de connaissance au service du plan « CORLANDEAU 2030 » (« capitaliser la connaissance technique ») ; elle combine des outils, des processus et une culture du partage, et ne se réduit pas à numériser des documents (0,5 pt pour trois axes appliqués) :

| Axe | Connaissance visée | Ce que la base et l'assistant apportent | Ce qu'ils n'apportent pas |
|---|---|---|---|
| **1. Un référentiel unique et validé de la connaissance explicite** : une fiche par question, avec ses sources, son auteur, son validateur, sa date de validation et sa date de revue ; reprise des notes, des réponses et des modèles des six bureaux | explicite, aujourd'hui dispersée (six arborescences, 300 notes jamais mises à jour, réponses enfermées dans les messageries, une version de chaque modèle par bureau) | un point d'accès unique ; une recherche en langage courant qui cite la fiche ; un temps de recherche déclaré qui passe de 30 à 10 minutes | la qualité du contenu : une fiche périmée produit une réponse fausse (60 fiches à reprendre en mars, 80 % de réponses exactes) ; le contenu dépend du processus de validation et de mise à jour |
| **2. Une boucle de capitalisation entre les bureaux et le pôle technique** : toute question sans fiche est transmise à un expert, et la réponse devient une fiche ; les experts sont libérés des questions répétées pour la validation et la veille | explicite en création continue : six questions sur dix portent sur un sujet déjà traité (300 par mois en période fiscale) | il oriente vers la fiche existante et signale l'absence de fiche ; la base s'enrichit des questions réelles | il ne doit pas répondre à la place de l'expert quand aucune fiche n'existe (20 % de réponses sans fiche en mars) |
| **3. La transmission de l'expérience par les personnes** : binômes entre les trois associés qui partent d'ici 2029 et des chefs de mission, retours d'expérience sur des cas réels, rédigés ensuite en fiches de cas avec leur contexte, annuaire des expertises | tacite, concentrée chez quelques associés et menacée par leurs départs | il diffuse ce qui a été formalisé, avec le contexte et les limites du cas | il ne capte pas le tacite : le jugement se transmet en travaillant ensemble, comme le souhaite M. VERDALHAC |

*3.1 b) – Intégration dans l'environnement existant*

| Élément | Décision | Justification (annexe 3.1) et articulation avec la base |
|---|---|---|
| **GED** | **conservée et transformée** | outil déjà en place depuis 2019 et maîtrisé, mais sans espace pour la documentation technique : y créer un espace « documentation technique » avec un plan de classement par domaine (fiscal, comptable, social, juridique) et des métadonnées (auteur, validateur, date de validation, date de revue, statut) ; les fiches et les modèles communs validés y sont versionnés et archivés ; l'assistant n'interroge que cet espace validé, jamais les dossiers des clients |
| **Intranet** | **transformé** | peu consulté (25 % des salariés par mois), pages techniques à l'abandon depuis 2022 : il devient le point d'entrée unique, avec la recherche de l'assistant sur la page d'accueil, la connexion avec le compte habituel du cabinet (« une connexion de plus » regrettée par M. QUINTAREL), les nouveautés techniques et les fiches mises à jour, l'annuaire des référents ; les pages techniques périmées sont retirées |
| **Forum interne** | **abandonné** | aucun message depuis mars 2023, 40 questions restées sans réponse : un espace d'échange sans animateur ni règle de réponse échoue ; sa fonction est reprise par la transmission des questions sans fiche au pôle technique ou au référent du bureau, avec un engagement de délai, et la réponse devient une fiche |
| **Dossiers partagés des bureaux** | **abandonnés pour la documentation technique, après reprise** | six arborescences, versions multiples sans date ni auteur : les documents sont triés avec chaque bureau (environ 2 000 documents), ce qui mérite d'être conservé devient une fiche ou un modèle commun, avec ses variantes locales validées ; les dossiers sont ensuite figés en lecture seule puis archivés, pour qu'aucune version parallèle ne subsiste ; associer les bureaux répond à la crainte de Mme LEFRANDIER |

(1,5 pt pour les quatre éléments justifiés ; 1 pt pour trois ; 0,5 pt pour deux.)

Les **bases documentaires des éditeurs** sont conservées comme sources de référence citées par les fiches ; l'extension des accès aux bureaux autres que Poitiers est valorisée, non exigée.

**Réponses tolérées**
- Axes formulés autrement (« formaliser, partager, transmettre » ; « référentiel, communauté, transmission »), si l'explicite et le tacite sont tous deux traités et si les limites de l'outil apparaissent.
- Référence au modèle SECI (Nonaka et Takeuchi), si elle reste un appui et est appliquée au cas : externalisation des réponses en fiches, combinaison dans la base, socialisation en binômes.
- Forum transformé plutôt qu'abandonné (espace de questions et réponses animé par les référents, intégré à l'intranet), si la cause de l'échec (absence d'animation et de réponse) est traitée.
- GED « conservée » sans transformation, si le candidat crée ailleurs un espace documentaire validé et versionné et exclut les dossiers des clients du champ de l'assistant.

**Erreurs fréquentes**
- *Gestion des connaissances réduite à la GED ou à l'outil* (`ET-21`) — « installer l'assistant dans les six bureaux suffit » ; juste : un dispositif qui associe outils, processus de validation et de mise à jour, et culture du partage.
- *Tacite traité comme de l'explicite* — « l'assistant capitalisera l'expérience des associés » ; juste : le tacite se transmet d'abord par les personnes, puis se formalise en partie avec son contexte.
- *Dérive vers la gestion des compétences* (limite du programme) — plan de formation ou de recrutement pour remplacer les associés ; juste : la transmission de la connaissance, distincte de la gestion des compétences.
- *Décisions non justifiées par l'annexe* (`JUR-T08`) — « supprimer l'intranet » sans considérer son rôle de point d'entrée ni sa faible consultation.
- *Assistant raccordé aux dossiers des clients* — il élargirait l'exposition de données couvertes par le secret professionnel ; juste : un champ limité à la documentation validée.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Connaissances tacites et explicites | distinction et axes | F06 § 1 | notion de cours |
| Architecture fonctionnelle d'un dispositif de gestion des connaissances ; GED, plan de classement, métadonnées | intégration des outils | F06 § 2.1 et 3 | notion de cours |
| Modèle SECI (Nonaka et Takeuchi, 1995) | réponse tolérée | `nonaka_takeuchi_seci` / F06 § 1 | modèle publié |
| ISO 15489-1 — gestion des documents d'activité | cycle de vie des fiches dans la GED (illustratif) | `iso_15489_1` / F06 § 4 | en vigueur |

---

### 3.2 – Audit post-implémentation du pilote (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; « La conformité financière et comptable n'est pas traitée dans le programme de l'UE 5 » ; « L'audit SI suppose une approche multidisciplinaire et une posture critique vis-à-vis de la gouvernance ».

**Annexes mobilisées** : annexes 3.4 A (demande, durée, interlocuteurs), 3.2 (dispositif, résultats, contenu des questions, journaux), 3.3 (témoignages) et 3.4 C (repères).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Audit post-implémentation défini (évaluation, après la mise en service, de l'atteinte des objectifs, de la qualité et de la conformité, pour décider et tirer des enseignements) et démarche appliquée : objectifs, périmètre (inclus et exclus), étapes sur six semaines jusqu'à la restitution avant le comité du 24 juin, livrables ; 0,5 si la démarche est incomplète (sans périmètre, livrables ni calendrier) | 1 |
| b-1 | Quatre critères définis et appréciés avec les chiffres de l'annexe 3.2 ; 0,5 pour deux ou trois critères | 1 |
| b-2 | Deux limites des résultats présentés (absence d'objectifs et de mesure initiale, contrôle par les auteurs des fiches sur un petit échantillon, temps déclaré par des volontaires, périodes non comparables) | 0,5 |
| c | Deux facteurs de succès et deux points de vigilance propres à l'audit d'un outil fondé sur l'IA générative ; 0,5 dès trois éléments précis | 0,5 |

**Réponse attendue**

*3.2 a) – Définition et démarche*

L'**audit post-implémentation** est l'évaluation indépendante et méthodique d'un système après sa mise en service (ici un pilote) : il compare les résultats obtenus aux objectifs et aux bénéfices attendus, apprécie la qualité, la sécurité et la conformité du système et de l'organisation qui l'accompagne, et conclut par des recommandations qui éclairent la décision (généraliser, corriger, arrêter) et les projets suivants. Il s'inscrit dans la démarche générale de l'audit du SI : examen au regard de critères et d'un référentiel, constats, recommandations hiérarchisées (F10 § 1.1 et 1.2).

Démarche appliquée (0,5 pt pour la définition et les objectifs, 0,5 pt pour le périmètre, les étapes, les livrables et le calendrier) :
- **Mandant et auditeur** : la présidente, qui décidera devant le comité des associés du 24 juin 2027 ; le chargé de mission, arrivé en janvier 2027, n'a pas conduit le pilote ; il s'appuie, pour juger de l'exactitude des réponses, sur un professionnel qui n'a pas rédigé les fiches.
- **Objectifs** : apprécier (1) la fiabilité des réponses et la traçabilité de leurs sources, (2) la protection des données des clients, (3) l'usage réel et les gains, (4) l'organisation de rédaction, de validation et de mise à jour des fiches ; en déduire les conditions de la généralisation.
- **Périmètre** : la base de 400 fiches, l'assistant, le service d'IA et son contrat, l'organisation du pôle technique et l'accompagnement des utilisateurs dans les bureaux de Poitiers et de Niort, depuis septembre 2026 (résultats arrêtés en mars 2027, témoignages d'avril). **Exclus** : le fonctionnement interne du modèle, tout test technique des systèmes du prestataire ou du fournisseur, le contenu doctrinal au-delà d'un échantillon, la situation des quatre autres bureaux (sinon comme référence).
- **Étapes** (six semaines, du 19 avril au 31 mai) : (1) semaine 1, **cadrage** : lettre de mission signée par la présidente (objectifs, périmètre, critères et seuils d'appréciation, référentiels : COBIT 2019 pour la gestion des changements et le suivi des bénéfices, le RGPD pour la sous-traitance, la charte du pilote) ; (2) semaines 1 et 2, **prise de connaissance** : entretiens avec les associés de Poitiers et de Niort, M. DUVERNAIL et les deux experts, M. QUINTAREL, le prestataire, revue du contrat, de la charte, des journaux et des résultats ; (3) semaines 2 à 4, **collecte et tests** : jeu de questions de référence posé à l'assistant et corrigé par un professionnel indépendant des fiches, sondage sur les questions réelles (exactitude, citation des sources, présence de données de clients), revue des dates des fiches, analyse de l'usage par bureau et par profil, questionnaire adressé aux 70 utilisateurs et entretiens avec des non-utilisateurs ; (4) semaine 5, **analyse et validation contradictoire** des constats avec les audités ; (5) semaine 6, **restitution** : note de synthèse à la présidente, sans détail technique, avant le 31 mai, pour préparer le comité du 24 juin ; (6) **suivi** des recommandations retenues dans le projet de généralisation.
- **Livrables** : lettre de mission, grille des critères, programme de travail, feuilles de constats (constat, risque, recommandation, priorité), note de synthèse avec les conditions de la généralisation, plan d'action.

*3.2 b) – Quatre critères d'appréciation et lecture critique*

| Critère | Définition | Appréciation du pilote (annexe 3.2) |
|---|---|---|
| **Fiabilité des réponses** | exactitude et actualité des réponses au regard de la doctrine validée par le cabinet | insuffisante : 90 % de réponses exactes en octobre, 80 % en mars, soit une réponse sur cinq inexacte en pleine période fiscale, quand l'enjeu pour les clients est le plus fort ; 60 des 400 fiches (15 %) devenues inexactes après un changement de règle et non corrigées ; aucune date de revue prévue |
| **Traçabilité des sources** | chaque réponse renvoie à une fiche validée (auteur, date), elle-même fondée sur des sources identifiées, et la question comme la réponse peuvent être retrouvées | partielle : 10 % puis 20 % de réponses ne citent aucune fiche ; les journaux sont effacés au bout de 30 jours et le cabinet n'en garde aucune copie : impossible de savoir quelle réponse a été donnée à qui en cas d'erreur chez un client |
| **Confidentialité des données des clients** | protection des informations couvertes par le secret professionnel et des données personnelles, au regard de la charte et du contrat avec le prestataire | non maîtrisée : 30 des 200 questions relues (15 %) contiennent le nom d'un client ou des montants de son dossier malgré la charte ; questions traitées hors de l'Union européenne selon le prestataire (annexe 3.4 B), usage des données inconnu du responsable informatique ; règle ignorée des utilisateurs (« je ne sais pas si j'ai le droit ») |
| **Usage** | adoption effective par les utilisateurs visés et effet sur le travail (temps, sollicitations du pôle technique) | en recul : 56 utilisateurs sur 70 en octobre (80 %), 35 en mars (50 %) ; 1 500 puis 1 000 recherches, un tiers de moins ; questions au pôle technique en baisse d'un cinquième seulement (250 en mars 2026, 200 en mars 2027) ; gain déclaré de 30 à 10 minutes par recherche |

(1 pt pour les quatre critères définis et appréciés ; 0,5 pt pour deux ou trois.)

Deux limites des résultats (0,5 pt) :
1. **Aucun objectif ni aucune mesure de départ** n'a été fixé au lancement : on ne peut dire si 80 % de réponses exactes ou 50 % d'utilisateurs sont un succès ; l'audit doit d'abord fixer des seuils avec la présidente.
2. **Exactitude jugée par les auteurs des fiches**, sur 50 réponses par mois choisies selon une méthode inconnue : contrôle ni indépendant ni forcément représentatif.
3. **Gain de temps déclaré** par 30 volontaires sur 70 (43 %), sans mesure : biais de sélection (les utilisateurs satisfaits répondent plus volontiers) et de déclaration.
4. **Périodes non comparables** : octobre et mars ne présentent ni les mêmes questions ni la même charge ; la baisse d'usage peut venir de la défiance après des erreurs, du manque de temps en période fiscale ou de la fin de l'effet de nouveauté : corrélation n'est pas cause, les entretiens doivent éclairer l'explication.

*3.2 c) – Facteurs de succès et points de vigilance propres à l'audit d'un outil d'IA générative*

Facteurs de succès (deux attendus) :
- **Accès aux traces et aux informations du prestataire et du fournisseur** : copie des journaux avant leur effacement à 30 jours, contrat, lieu de traitement, version du modèle ; à obtenir dès le cadrage, au besoin par la présidente.
- **Compétences pluridisciplinaires et indépendance** : un professionnel de la doctrine qui n'a pas écrit les fiches, associé au responsable informatique ; une posture non punitive, alors que les experts craignent de « répondre d'une réponse de la machine ».
- **Critères et seuils fixés avant les tests** avec la présidente (par exemple un taux d'exactitude exigé), pour éviter un jugement a posteriori.

Points de vigilance (deux attendus) :
- **Réponses non reproductibles** : la même question peut recevoir des réponses différentes ; l'audit repose sur un jeu de questions de référence posé plusieurs fois, réponses conservées, et sur des échantillons de questions réelles, non sur quelques démonstrations.
- **Distinguer l'erreur de contenu et l'erreur de l'assistant** : une réponse fausse peut venir d'une fiche périmée (gouvernance du contenu) ou d'une réponse produite sans fiche (comportement de l'outil) ; les recommandations diffèrent.
- **Système qui évolue sans préavis** : le fournisseur peut changer de version du modèle pendant l'audit ; dater les tests et noter la version.
- **Pas de données réelles de clients dans les tests** : jeu d'essai fondé sur des cas fictifs ou rendus anonymes.
- **Opacité du modèle** : l'audit porte sur les résultats, les traces, le contrat et l'organisation, pas sur le fonctionnement interne du modèle.

(0,5 pt pour deux facteurs et deux points de vigilance précis ; 0,5 pt dès trois éléments précis.)

**Réponses tolérées**
- Démarche en cinq ou sept étapes, si le cadrage, la collecte, la restitution avant le comité et le suivi y figurent.
- Audit qualifié de « bilan » ou de « revue post-implémentation », s'il compare résultats et objectifs et débouche sur une décision.
- Autre référentiel cité à l'appui (ITIL pour la gestion des changements et des niveaux de service, ISO/IEC 42001:2023 pour le management de l'IA), s'il est utilisé comme référentiel d'appréciation et non comme une certification à obtenir.
- Critère « usage » apprécié sous l'angle de l'efficacité ou de l'efficience, si l'adoption et les gains sont rapprochés.
- Autre limite pertinente : questions au pôle technique comparées d'une année à l'autre sans tenir compte des autres facteurs (nouveautés fiscales, effectifs).

**Erreurs fréquentes**
- *Méthodologie d'audit incomplète* (`JUR-A01` méthodologie structurée : périmètre, objectifs, étapes, livrables, échéancier) — étapes sans périmètre, sans livrables, ou restitution prévue après le comité du 24 juin.
- *Audit technique du modèle* — examen des algorithmes, essais de vulnérabilité ou de charge ; juste : résultats, traces, contrat, organisation ; les tests techniques détaillés ne sont pas attendus.
- *Chiffres lus sans recul* (`JUR-T03` analyser et argumenter) — « 10 minutes au lieu de 30, le pilote est un succès » ; juste : gain déclaré par des volontaires, à rapprocher de la baisse d'usage et de la fiabilité.
- *Audit du SI confondu avec l'audit des comptes* (`ET-34`) — vérification des comptes des clients ou du cabinet ; juste : fiabilité, traçabilité, confidentialité et usage d'un outil.
- *Dérive vers le droit des données personnelles* — bases légales, transferts, droits des personnes ; juste : la confidentialité comme critère d'organisation (charte, contrat, lieu de traitement, conservation), sans analyse juridique, comme l'indique l'annexe 3.4 C.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI : définition, démarche, livrables, facteurs de succès | démarche de l'audit du pilote | F10 § 0, 1.1 et 1.2 | notion de cours |
| COBIT 2019 (ISACA) | référentiel de gestion des changements et de suivi des bénéfices | `cobit_2019` / F02 § 3 | en vigueur |
| Règlement (UE) 2016/679 (RGPD), sous-traitance et sécurité | critère de confidentialité (annexe 3.4 C) | `rgpd` / F15 | en vigueur |
| Risques de l'IA générative (réponses inexactes, confidentialité, dépendance) | critères et points de vigilance | F13 § 3 | notion de cours |
| ISO/IEC 42001:2023 — système de management de l'IA | réponse tolérée | `iso_42001_2023` / F13 § 4 | en vigueur |

---

### 3.3 – Méthode de conduite de la généralisation et cahier des charges (2 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.b` « Méthodologies de gestion de projet (cycle en V, agile, hybride) » ; `1.5.c` « Élaboration d'un cahier des charges fonctionnel et technique ». Limites : « L'aspect budgétaire détaillé ne relève pas du programme de l'UE » ; les approches de livraison continue sont mentionnées mais non approfondies.

**Annexes mobilisées** : annexes 3.2 C (tâches, jalons, contrainte, deux options), 3.2 A et B (pilote), 3.3 (experts, collaborateurs), 3.4 B (service d'IA) et 1.1 (bureaux, période fiscale).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cycle en V et démarche agile caractérisés, puis comparés selon les trois critères appliqués aux options A et B (mise en service de février en pleine période fiscale, livraisons de janvier à mai, expert indisponible deux jours par semaine) | 0,5 |
| a-2 | Recommandation justifiée et compatible avec la période fiscale (démarche hybride avec gel des mises en service, ou option adaptée) | 0,5 |
| b | Rôle du cahier des charges fonctionnel précisé et quatre rubriques, chacune illustrée par un contenu des annexes ; 0,5 pour deux ou trois rubriques | 1 |

**Réponse attendue**

*3.3 a) – Comparaison et recommandation*

Le **cycle en V** est une démarche séquentielle : expression du besoin et spécifications complètes, conception, réalisation, puis tests et recette en miroir de chaque niveau de spécification ; il convient à un besoin stable, se contractualise au forfait, mais découvre tard les écarts (effet tunnel). La **démarche agile** (Scrum) procède par itérations courtes qui livrent chacune un incrément utilisable, à partir d'un carnet de demandes classées par valeur par un responsable du produit ; elle s'adapte au besoin qui évolue mais exige un responsable du produit disponible et des utilisateurs impliqués (F05 § 2).

| Critère | Option A – Cycle en V | Option B – Démarche agile |
|---|---|---|
| **Stabilité du besoin** | adaptée au socle stable et éprouvé par le pilote (raccordement à l'intranet et à la GED, connexion, droits, choix du service d'IA) ; inadaptée au contenu et aux usages, qui évoluent sans cesse et que les quatre autres bureaux n'ont pas exprimés (Mme LEFRANDIER) | adaptée aux besoins découverts bureau par bureau et à l'enrichissement de la base ; risque de dérive du périmètre sans cahier des charges ni critères d'acceptation, d'autant que la facturation est au temps passé |
| **Disponibilité des experts** | sollicitation concentrée sur la validation des spécifications en août et la recette en décembre, hors période fiscale | un expert responsable du produit deux jours par semaine : intenable pour deux experts déjà submergés par la validation des fiches et 300 à 500 questions par mois |
| **Période fiscale** | mise en service simultanée dans six bureaux en février 2028 : en pleine période fiscale, contraire à la règle du comité ; « big bang » sans retour d'expérience, et tout retard repousse la mise en service au 1er juin | mises en service bureau par bureau dès septembre, compatibles ; mais livraisons de nouvelles fonctions de janvier à mai, contraires à la règle du comité |

(0,5 pt.)

**Recommandation : une démarche hybride** (0,5 pt).
- **Cadrage et socle en cycle en V** de juin à août : cahier des charges fonctionnel, choix du service d'IA, raccordement à l'intranet et à la GED, connexion avec le compte du cabinet, droits, conservation des journaux ; recette du socle fin août, au forfait.
- **Mise en service progressive** de septembre à décembre 2027, un bureau par mois (La Rochelle, Angoulême, Saintes, Châtellerault), en itérations courtes pour adapter l'ergonomie et reprendre les contenus de chaque bureau avec son référent ; le responsable du produit est un chef de mission ou le chargé de mission, déchargé en partie, les experts n'intervenant que pour la validation.
- **Gel du 15 janvier au 31 mai** : aucune mise en service ni nouvelle version ; seules la maintenance corrective et la mise à jour des fiches continuent — corriger une fiche après un changement de règle n'est pas un changement de version du logiciel, c'est la condition de la fiabilité.
- Reprise des itérations en juin 2028 ; tout ce qui n'est pas prêt mi-décembre attend juin.

*3.3 b) – Cahier des charges fonctionnel*

Le **cahier des charges fonctionnel** exprime le besoin de la maîtrise d'ouvrage (le « quoi », non le « comment ») : contexte, objectifs, périmètre, fonctions attendues et leur priorité, contraintes et critères d'acceptation ; rédigé avec les utilisateurs et validé par le commanditaire, il fonde le contrat avec le prestataire et la recette (F05 § 3). Quatre rubriques (1 pt) :

| Rubrique | Contenu tiré des annexes |
|---|---|
| **Contexte, objectifs mesurables et périmètre** | priorité « capitaliser la connaissance technique » du plan ; six bureaux, 180 utilisateurs, environ 3 000 questions par mois, 800 fiches à la fin de 2027 ; objectifs chiffrés que le pilote n'avait pas (taux de réponses exactes, part des utilisateurs actifs, baisse des questions répétées au pôle technique) ; exclus : les dossiers des clients, la rédaction de courriers |
| **Exigences fonctionnelles priorisées** (indispensable, souhaitable, facultatif) | indispensable : réponse citant toujours la fiche, son auteur et sa date ; absence de fiche signalée avec transmission de la question au pôle technique ; circuit de rédaction, de relecture et de validation des fiches avec date de revue ; retrait des fiches périmées ; signalement d'une erreur par l'utilisateur ; souhaitable : nouveautés et fiches mises à jour sur l'intranet |
| **Contraintes et exigences non fonctionnelles** | confidentialité (aucune donnée de client, lieu de traitement et absence de conservation des questions par le fournisseur), traçabilité (journaux conservés par le cabinet), accessibilité aux logiciels de lecture d'écran, connexion avec le compte du cabinet, réversibilité des fiches, aucune mise en service du 15 janvier au 31 mai, sobriété du service |
| **Critères d'acceptation et organisation de la recette** | jeu de questions de référence, seuils (taux d'exactitude, citation des sources, absence de fiche périmée citée), recette par le pôle technique et les référents avant chaque mise en service |

**Réponses tolérées**
- Option B retenue, si le candidat la corrige explicitement : gel du 15 janvier au 31 mai, responsable du produit autre qu'un expert, cahier des charges et critères d'acceptation, prix encadré.
- Option A retenue avec une mise en service avancée en décembre ou bureau par bureau à l'automne, si la période fiscale est respectée et l'effet tunnel discuté.
- Autre rubrique illustrée : utilisateurs et profils (collaborateurs, référents, experts, administrateur) ; reprise des contenus existants (2 000 documents) ; jalons (décision du 24 juin, mises en service de septembre à décembre) ; formation et accompagnement.

**Erreurs fréquentes**
- *Récitation des méthodes sans le cas* (`JUR-P02` deux méthodes de projet comparées dans le contexte) — phases du cycle en V et rôles de Scrum sans lien avec la période fiscale ni avec la charge des experts.
- *Agile assimilé à l'absence de cahier des charges* (`ET-32`) — « en agile, pas besoin de spécifier » ; juste : carnet de demandes priorisé, critères d'acceptation, contraintes fixées d'avance.
- *Gel confondu avec l'arrêt de la mise à jour des fiches* — la période fiscale interdit les changements de version du logiciel, pas la correction des contenus, dont dépend la fiabilité.
- *Planning détaillé ou chiffrage du projet* — diagramme de Gantt, budget par lot : non demandés.
- *Cahier des charges technique* — architecture, serveurs, choix du modèle ; juste : le besoin et les contraintes, le « comment » relevant du prestataire.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Cycle en V, démarche agile, démarche hybride ; critères de choix | comparaison et recommandation | F05 § 2 | notion de cours |
| The Scrum Guide (Schwaber et Sutherland, novembre 2020) | itérations, responsable du produit | `scrum_guide_2020` / F05 § 2.2 | en vigueur |
| Cahier des charges fonctionnel ; priorisation des exigences | quatre rubriques | F05 § 3 | notion de cours |
| ITIL, gestion des changements (calendrier des changements) | gel en période fiscale (réponse tolérée) | `itil_4` / F02 § 5 | en vigueur |

---

### 3.4 – Risques, plan qualité et recette de la généralisation (2 points)

**Référence au programme**
- §1.5 – Planifier, organiser et conduire des projets de systèmes d'information : `1.5.e` « Identification et gestion des risques (maintenance, évolutivité, sécurité) » ; `1.5.f` « Mise en œuvre et contrôle du plan qualité ». Limite : « Le suivi post-déploiement (TMA, support) n'est abordé que dans une perspective de maintenance évolutive et curative ».

**Annexes mobilisées** : annexes 3.2 (fiches devenues inexactes, journaux, contenu des questions, projet), 3.3 (experts, responsable informatique, collaborateur malvoyant) et 3.4 B (service d'IA).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Trois risques (maintenance de la base, évolutivité, sécurité et confidentialité), chacun avec sa cause dans les annexes, sa conséquence et une mesure de traitement ; 0,5 pour deux risques complets | 1 |
| b-1 | Plan qualité défini et contenu adapté à la généralisation (organisation et rôles, normes de rédaction des fiches, gestion des versions et des changements, contrôles et revues, indicateurs de qualité) | 0,5 |
| b-2 | Recette décrite : acteurs, jeu d'essai, critères d'acceptation, calendrier compatible avec la période fiscale ; 0,5 dès trois des quatre éléments | 0,5 |

**Réponse attendue**

*3.4 a) – Trois risques*

| Risque | Cause (annexes) | Conséquence | Traitement |
|---|---|---|---|
| **Maintenance de la base** : des fiches deviennent fausses plus vite qu'elles ne sont corrigées | aucune date de revue ; 60 fiches devenues inexactes en début d'année ; deux experts pour valider 400, puis 800 fiches, en plus des questions | réponses inexactes données aux clients, en pleine période fiscale ; perte de confiance (Mme ROUSSELANGE vérifie tout) et retour aux appels aux experts | date de revue obligatoire sur chaque fiche ; fiche retirée des réponses de l'assistant dès sa date dépassée ou dès qu'un changement de règle la vise ; campagne de revue planifiée en décembre et janvier, sur la liste des fiches touchées par les nouveautés fiscales ; validation répartie entre les experts et des référents de domaine ; maintenance corrective et évolutive prévue au contrat du prestataire |
| **Évolutivité** : le dispositif ne suit pas le passage à l'échelle | de 70 à 180 utilisateurs, de 1 500 à environ 3 000 questions par mois, de 400 à 800 fiches, quatre bureaux aux pratiques propres ; coût lié au fournisseur ; modèle modifiable par le fournisseur ; une équipe informatique de trois personnes sans temps pour administrer | lenteurs, coûts en hausse, comportement des réponses modifié sans préavis, dépendance envers un fournisseur | fiches conservées dans la GED du cabinet, dans un format réutilisable, indépendamment du modèle, pour pouvoir changer de service ; contrat : capacité garantie pour le volume prévu, information préalable sur tout changement de version, réversibilité, prix encadré ; mise en service bureau par bureau ; administration confiée à une personne désignée |
| **Sécurité et confidentialité** | 15 % des questions relues contiennent des données de clients ; traitement par un fournisseur dont le lieu et l'usage des données sont inconnus ; journaux effacés à 30 jours ; droits par bureau et par pôle à créer | atteinte au secret professionnel et à la confiance des clients ; impossibilité de reconstituer une réponse contestée | service sans conservation des questions, hébergé dans l'Union européenne (option 2), contrat de sous-traitance précis ; règle claire, rappelée à l'écran, et avertissement lorsqu'une question semble contenir des données d'un client ; connexion avec le compte du cabinet et droits par profil ; journaux conservés par le cabinet pendant une durée fixée |

(1 pt pour trois risques complets ; 0,5 pt pour deux.)

*3.4 b) – Plan qualité et recette*

Le **plan qualité** (plan d'assurance qualité) est le document qui fixe, pour un projet, l'organisation, les règles et les contrôles qui garantissent que les livrables répondent aux exigences : rôles et responsabilités, normes de documentation, gestion des versions et des changements, revues, plan de tests, critères d'acceptation, traitement des anomalies, indicateurs (F05 § 6). Contenu pour la généralisation (0,5 pt) :
- **Organisation** : la présidente commanditaire ; un comité de pilotage mensuel (M. DUVERNAIL, un associé de bureau, M. QUINTAREL, le chargé de mission, chef de projet, le prestataire) ; le pôle technique et les référents comme maîtrise d'ouvrage du contenu ; le prestataire comme maîtrise d'œuvre.
- **Normes** : modèle de fiche obligatoire (question, réponse, contexte et limites, sources, auteur, validateur, date de validation, date de revue, domaine) ; règles de rédaction ; modèles communs avec variantes locales identifiées.
- **Gestion des versions et des changements** : versions des fiches tracées dans la GED ; calendrier des changements du logiciel avec gel du 15 janvier au 31 mai ; toute nouvelle version du modèle soumise à un essai de non-régression.
- **Contrôles et revues** : relecture de chaque fiche par une personne autre que l'auteur ; revue de projet à chaque mise en service de bureau ; contrôle mensuel d'un échantillon de réponses par un expert qui n'en est pas l'auteur.
- **Traitement des anomalies** : classement (bloquante, majeure, mineure), délai de correction.

**Recette** (0,5 pt) :
- **Acteurs** : recette technique par le prestataire et M. QUINTAREL (raccordement à l'intranet et à la GED, connexion, droits, journaux, capacité annoncée) ; recette fonctionnelle par la maîtrise d'ouvrage : les deux experts, les référents de chaque bureau et des utilisateurs, dont des collaborateurs d'un bureau non pilote et le collaborateur qui utilise un logiciel de lecture d'écran ; procès-verbal signé par le commanditaire, avec ou sans réserves.
- **Jeu d'essai** : questions de référence avec leur réponse attendue, couvrant tous les domaines et les règles qui changent en début d'année ; questions sans fiche (transmission au pôle technique attendue) ; questions contenant des données fictives de clients (avertissement attendu) ; aucune donnée réelle.
- **Critères d'acceptation** : un seuil élevé de réponses exactes fixé par la présidente (par exemple 95 %, contre 80 % en mars) ; toute réponse cite une fiche ou signale son absence ; aucune fiche périmée citée ; aucune anomalie bloquante ; utilisation possible avec un logiciel de lecture d'écran.
- **Calendrier** : recette du socle fin août ; recette de chaque bureau avant sa mise en service, de septembre à décembre ; aucune recette ni mise en service du 15 janvier au 31 mai ; recette de non-régression avant toute nouvelle version, hors de cette période.

**Réponses tolérées**
- Risques cotés selon une échelle probabilité × gravité, si les trois catégories demandées sont traitées.
- Autre risque de sécurité pertinent : comptes des salariés partis encore actifs, droits trop larges sur la documentation du pôle social.
- Plan qualité présenté selon les rubriques d'un plan d'assurance qualité ou en référence à ISO 9001 (édition 2026), cité en principe.
- Seuil d'acceptation différent, s'il est justifié par l'enjeu (réponse donnée à un client) et supérieur aux résultats du pilote.

**Erreurs fréquentes**
- *Risques génériques* (`JUR-P02` facteurs clés de succès et risques) — « risque technique, risque humain » sans cause dans les annexes ni mesure.
- *Mesures de sécurité techniques détaillées* — paramétrage des équipements ou essais d'intrusion ; juste : mesures d'organisation et de contrat propres au projet (la politique de sécurité du cabinet n'est pas l'objet du dossier).
- *Recette réduite à un essai du prestataire* — sans la maîtrise d'ouvrage ni critères d'acceptation ; juste : recette fonctionnelle par les experts et les utilisateurs, procès-verbal.
- *Recette sur des données réelles de clients* — contraire à la confidentialité.
- *Maintenance limitée au logiciel* — la maintenance de la base (mise à jour des fiches) est le premier risque de ce projet.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Risques projet : identification, cotation, traitement ; maintenance corrective et évolutive | trois risques | F05 § 5 et 6 | notion de cours |
| Plan d'assurance qualité, recette, procès-verbal | plan qualité et recette | F05 § 6 | notion de cours |
| ISO 9001 — systèmes de management de la qualité (édition 2026) | réponse tolérée, en principe | `iso_9001_2026` / F05 § 6 | en vigueur |

---

### 3.5 – Appropriation et gouvernance du dispositif (2 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.e` « Leviers d'appropriation et de transformation des pratiques professionnelles » ; `1.6.c` « Méthodes de gouvernance des dispositifs (rôles, responsabilités, indicateurs) ». Limites : « Le pilotage nécessite une approche systémique : outils, processus, culture » ; « Le lien avec la gestion des compétences (RH) est complémentaire mais distinct ».

**Annexes mobilisées** : annexes 3.3 (témoignages), 3.2 (résultats, charte, absence de date de revue), 3.1 (organisation du pôle technique), 3.4 C (maîtrise de l'IA) et 1.1 (organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Résistances analysées et classées (fiabilité, habitudes et temps, attachement au bureau, crainte de dépossession, charge et responsabilité des experts, règles floues), chacune rattachée à un témoin | 0,5 |
| a-2 | Quatre leviers, chacun en réponse à une résistance identifiée ; 0,5 dès trois leviers reliés | 0,5 |
| b-1 | Rôles des experts, des référents de bureau et des contributeurs ; règles de validation et de mise à jour des fiches | 0,5 |
| b-2 | Un indicateur complet (formule, source, fréquence, cible, axe), relié au cas | 0,5 |

**Réponse attendue**

*3.5 a) – Résistances et leviers*

Les résistances ne sont pas un refus du principe : la plupart sont rationnelles et désignent un défaut du dispositif (0,5 pt).

| Résistance | Témoin (annexe 3.3) | Nature |
|---|---|---|
| **Défiance envers la fiabilité** | Mme ROUSSELANGE : un seuil faux en mars, depuis « je vérifie tout » et j'appelle l'expert | liée à la qualité du contenu (fiches non corrigées) |
| **Habitudes et manque de temps** | M. BERLANDIN : les anciens préfèrent appeler un expert ; personne n'apprend un outil de janvier à mai | individuelle (habitude, relation) et liée au calendrier |
| **Attachement au bureau et absence de reconnaissance** | Mme LEFRANDIER : « une base conçue à Poitiers », « qui la relira, est-ce que quelqu'un le saura ? » | collective (identité du bureau, crainte d'être dépossédé de ses modèles) |
| **Crainte de voir son savoir sorti de son contexte** | M. VERDALHAC : « tout écrire ? », « une machine […] hors de leur contexte » | liée à la nature tacite de son savoir |
| **Charge et responsabilité des experts** | Mme ESCARBEL et M. PRADONNET : 400 fiches à deux, peur d'être submergés et de répondre d'une réponse non relue | organisationnelle (moyens, responsabilités) |
| **Règles floues et outil inaccessible** | M. BERLANDIN : « ai-je le droit d'y coller un extrait de dossier ? » ; collaborateur malvoyant exclu ; M. QUINTAREL : « une connexion de plus » | liée à l'outil et à l'accompagnement |

Quatre leviers (0,5 pt) :
1. **Rendre la fiabilité visible** (réponse à la défiance et à la crainte des experts) : aucune réponse sans fiche validée, date de validation affichée, question sans fiche transmise à un expert, fiche périmée retirée ; un bouton pour signaler une erreur, corrigée et suivie.
2. **Associer les bureaux et reconnaître les contributions** (réponse à Mme LEFRANDIER) : un référent dans chaque bureau ; reprise des modèles et des notes du bureau dans la base, avec leur auteur cité ; contribution reconnue (nom de l'auteur sur la fiche, présentation au comité des associés).
3. **Transmettre l'expérience par les personnes** (réponse à M. VERDALHAC) : binômes sur de vrais dossiers avec un chef de mission, qui rédige ensuite des fiches de cas avec leur contexte et leurs limites, relues par l'associé ; l'associé décide de ce qui est écrit.
4. **Former au bon moment et clarifier les règles** (réponse aux habitudes, au manque de temps et aux règles floues) : formations courtes en septembre-décembre, jamais en période fiscale ; charte d'usage claire et rappelée à l'écran (aucune donnée de client) ; mesures pour favoriser la maîtrise de l'IA du personnel, que le règlement sur l'IA demande aux déployeurs depuis le 2 février 2025, dans une rédaction assouplie par le règlement (UE) 2026/1744 (annexe 3.4 C) ; accompagnement individuel des moins à l'aise ; outil accessible et intégré à l'intranet ; exemplarité des associés, qui renvoient d'abord vers l'assistant.

*3.5 b) – Gouvernance du dispositif et indicateur*

Rôles (0,5 pt avec les règles) :
- **Commanditaire** : la présidente, qui rend compte au comité des associés de la priorité « capitaliser la connaissance technique » et arbitre les moyens (temps des experts et des référents).
- **Responsable du dispositif** : M. DUVERNAIL, associé animateur du pôle technique, propriétaire du contenu ; le chargé de mission pilote le projet et l'outil avec M. QUINTAREL (droits, journaux, relation avec le prestataire).
- **Experts du pôle technique** : définissent le modèle de fiche et les domaines, **valident** les fiches de leur domaine (second niveau), fixent les dates de revue, conduisent la revue après chaque changement de règle ; ils ne rédigent plus tout eux-mêmes.
- **Référents de bureau** (un chef de mission par bureau, avec un temps dédié) : relaient les questions de leur bureau, **relisent** les fiches proposées (premier niveau), identifient les fiches à écrire, accompagnent les collègues, remontent les erreurs.
- **Contributeurs** (collaborateurs, chefs de mission, associés) : **proposent** des fiches et des fiches de cas, signalent les erreurs, contribuent aux binômes.

Règles :
- circuit rédaction (contributeur) → relecture (référent) → validation (expert) → publication avec auteur, validateur et dates ; aucune fiche publiée sans validation ;
- date de revue sur chaque fiche (douze mois au plus) ; revue immédiate de toute fiche visée par un changement de règle, sur une liste établie par les experts dès la publication des nouveautés de fin d'année ; fiche retirée automatiquement des réponses à sa date de revue dépassée ;
- signalement d'erreur traité dans un délai fixé, plus court pour les erreurs de fond ;
- versions conservées dans la GED ; comité éditorial mensuel (experts, référents) qui fixe les priorités de rédaction à partir des questions sans fiche.

Indicateur (0,5 pt) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Taux de fiches à jour** | nombre de fiches publiées dont la date de revue n'est pas dépassée et qui ne sont visées par aucun changement de règle non traité / nombre de fiches publiées | registre des fiches de la base (dates de validation et de revue, signalements) | mensuelle, hebdomadaire de décembre à février | au moins 98 % (environ 85 % en mars 2027 : 60 fiches inexactes sur 400, approximation faute de dates de revue) ; aucune fiche périmée citée par l'assistant, assuré par le retrait automatique | processus |

Il mesure directement la règle de mise à jour, cause première de la baisse de fiabilité et de la défiance ; il se lit avec le taux de réponses exactes et l'usage dans le compte rendu trimestriel au comité des associés.

**Réponses tolérées**
- Leviers présentés selon le modèle ADKAR (comprendre pourquoi, vouloir, savoir, pouvoir, ancrer) ou les étapes de Kotter, si chacun répond à une résistance des témoignages.
- Validation à un seul niveau (expert) avec des référents de domaine répartis entre les bureaux, si la charge des experts est traitée.
- Autre indicateur complet et relié au cas : taux de réponses exactes de l'assistant (réponses jugées exactes / réponses contrôlées sur un échantillon tiré au hasard, contrôlé par un expert qui n'a pas rédigé la fiche ; journal des questions et réponses ; mensuelle ; au moins 95 % ; axe processus) ; part des collaborateurs actifs (utilisateurs dans le mois / salariés ayant accès ; journal ; mensuelle ; par exemple 80 % hors période fiscale ; axe apprentissage) ; part des questions au pôle technique portant sur un sujet déjà couvert par une fiche (axe processus) ; nombre de fiches proposées par les bureaux (axe apprentissage).

**Erreurs fréquentes**
- *Résistances traitées comme de l'irrationnel* (`JUR-P04` conduite du changement adaptée) — « il faut convaincre les anciens » ; juste : la défiance vient d'erreurs réelles, la première réponse est la fiabilité.
- *Leviers génériques* (`JUR-T08` exploiter les témoignages) — « communiquer, former » sans lien avec un témoin.
- *Obligation imposée comme seul levier* — « interdire d'appeler les experts » ; juste : rendre l'outil plus utile que l'appel, garder l'expert pour ce qui n'a pas de fiche.
- *Gouvernance réduite à l'outil* (`ET-21`) — « paramétrer des droits » ; juste : rôles, circuit de validation, règles de mise à jour.
- *Indicateur incomplet ou d'activité seule* (`JUR-A02` ; `ET-18`) — « nombre de fiches » sans cible ni lien avec la qualité.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gouvernance d'un dispositif de gestion des connaissances : rôles, règles, indicateurs | gouvernance | F06 § 2.2 | notion de cours |
| Leviers d'appropriation | quatre leviers | F06 § 2.3 ; F05 § 7 | notion de cours |
| ADKAR (Prosci ; Hiatt) | réponse tolérée | `adkar` / F05 § 7 | modèle publié |
| Règlement (UE) 2024/1689 sur l'IA, modifié par le règlement (UE) 2026/1744 : maîtrise de l'IA (article 4) | levier de formation (annexe 3.4 C) | `ai_act`, `omnibus_numerique_ia` / F13 § 4 et § 5.2 | en vigueur |
| Fiche d'indicateur à cinq champs | indicateur | F09 § 4 | notion de cours |

---

### 3.6 – Choix du service d'IA et transition numérique responsable (1,5 point)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : « La transformation numérique responsable nécessite une approche transversale et non cloisonnée » ; « La durabilité doit être intégrée dans la gouvernance globale du SI, et non comme ajout marginal ».

**Annexes mobilisées** : annexes 3.4 B (deux options) et C (repères), 3.3 (collaborateur malvoyant, anciens, M. QUINTAREL), 3.2 (réponses sans fiche, données des clients) et 1.1 (secret professionnel).

**Barème indicatif (1,5 pt)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Transition numérique responsable définie et option appréciée sous l'angle de la sobriété du modèle et des usages (consommation estimée cinq fois moindre, à vérifier ; fonctions inutiles au besoin) | 0,5 |
| 2 | Angles de l'éthique et de la transparence envers les clients, et de l'inclusion des collaborateurs, appliqués aux deux options | 0,5 |
| 3 | Recommandation justifiée d'une option et deux règles d'usage de l'assistant | 0,5 |

**Réponse attendue**

Une **stratégie de transition numérique responsable** conduit l'évolution du SI en intégrant, dès les choix, la sobriété (questionner le besoin avant d'optimiser), la réduction de l'empreinte environnementale (modèles et hébergements adaptés, centres de données sobres et transparents), l'éthique et l'inclusion ; elle relève de la gouvernance du SI et non d'un ajout final (F14 § 3 et 5) (0,5 pt avec l'angle de la sobriété).

| Angle | Option 1 – Modèle généraliste hors de l'Union européenne | Option 2 – Modèle plus petit hébergé en France |
|---|---|---|
| **Sobriété du modèle et des usages** | estimée à 10 MWh par an, cinq fois plus que l'option 2, pour la même exactitude (85 %) sur les questions couvertes par une fiche ; fonctions sans lien avec le besoin (courriers, résumés de dossiers, traductions) qui multiplient les usages et l'effet rebond ; aucune donnée publiée sur ses centres de données | modèle dimensionné au besoin réel (rechercher et citer une fiche), environ 2 MWh par an ; données d'énergie et d'origine de l'électricité publiées ; dans les deux cas, estimations du prestataire à faire justifier (méthode non communiquée) et à mesurer |
| **Éthique et transparence envers les clients** | questions conservées 30 jours par un fournisseur hors de l'Union européenne alors que 15 % des questions relues contenaient des données de clients couvertes par le secret professionnel ; réponse produite sans fiche, plausible mais non validée, présentée comme une réponse du cabinet | questions effacées, traitement en France ; absence de fiche dite clairement et transmise à un expert : l'outil n'invente pas ; le cabinet peut expliquer à ses clients qu'il s'appuie sur un assistant de recherche documentaire dont chaque réponse repose sur sa doctrine validée et reste sous la responsabilité d'un professionnel |
| **Inclusion des collaborateurs** | dans les deux options, l'interface doit être utilisable avec un logiciel de lecture d'écran (collaborateur malvoyant de Niort) et les collaborateurs moins à l'aise doivent être formés et accompagnés ; l'expert reste joignable : l'assistant ne doit pas devenir le seul accès à la connaissance | la transmission des questions sans fiche au pôle technique garde un interlocuteur humain, attendu par les plus anciens |

(0,5 pt pour l'éthique et l'inclusion appliquées.)

**Recommandation** (0,5 pt) : l'**option 2**. Elle répond au besoin documentaire avec la même exactitude, une consommation estimée bien moindre, des données qui restent en France sans conservation, un comportement honnête quand la base ne sait pas, et un coût inférieur (120 k€ sur trois ans contre 150 k€). Conditions : clauses du contrat sur la non-conservation des questions, l'information préalable sur les changements de version et la communication annuelle de la consommation mesurée ; accessibilité vérifiée à la recette ; filtrage par le référent du bureau des questions sans fiche avant leur transmission au pôle technique : au taux de mars (20 %), 3 000 questions par mois en produiraient jusqu'à 600, pour deux experts qui en reçoivent déjà 300 à 500 ; le comité éditorial fixe les priorités de rédaction, et la couverture de la base fait baisser ce flux (le candidat qui relève cette charge est valorisé). Deux règles d'usage :
1. **Aucune donnée permettant d'identifier un client** (nom, numéro d'identification, montants tirés d'un dossier) dans une question : la question porte sur la règle, pas sur le dossier.
2. **L'assistant cherche dans la doctrine validée ; il ne rédige pas pour le client** : toute réponse utilisée dans un conseil est vérifiée sur la fiche citée par le collaborateur, qui en répond ; aucun courrier ni document destiné à un client n'est produit par l'assistant.

**Réponses tolérées**
- Option 1 retenue si le candidat exige au contrat l'absence de conservation, la désactivation des fonctions inutiles, la suppression des réponses sans fiche et des données sur la consommation, et justifie le surcoût.
- Autre règle d'usage pertinente : réserver l'assistant aux questions professionnelles et éviter les demandes répétées ; signaler toute erreur ; mentionner au client, si la question est posée, l'usage d'un assistant de recherche.
- Référence au référentiel général d'écoconception de services numériques (RGESN, version 2024), thème de l'algorithmie et de l'IA, ou à la qualification SecNumCloud pour l'hébergement, si elle reste illustrative.

**Erreurs fréquentes**
- *Sobriété réduite à l'économie d'énergie* (`ET-12`) — comparer seulement les MWh ; juste : d'abord le besoin (une recherche documentaire n'exige ni courriers ni résumés), puis la consommation.
- *Chiffres d'un prestataire pris pour des mesures* — 10 et 2 MWh sont des estimations sans méthode connue : les faire justifier et mesurer.
- *Calcul d'empreinte* — conversion en émissions : non demandée.
- *Hébergement « souverain » assimilé à la seule localisation* (`ET-37`) — la nationalité du fournisseur et la conservation des données comptent autant que le lieu.
- *Qualification de l'assistant au regard du règlement sur l'IA* — non attendue (annexe 3.4 C) ; juste : éthique, transparence et responsabilité du professionnel.
- *Inclusion oubliée ou réduite à la formation* — l'accessibilité de l'outil et le maintien d'un interlocuteur humain font partie de la réponse.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Sobriété numérique, Green IT, effet rebond ; IA et modèles adaptés à la tâche | angle de la sobriété | F14 § 1 et 3 ; F13 § 3 | notion de cours |
| Cloud et centres de données, transparence des fournisseurs | choix d'hébergement | F14 § 5 | notion de cours |
| RGESN, version 2024 | réponse tolérée | `rgesn_2024` / F14 § 2 | en vigueur |
| SecNumCloud, version 3.2 (ANSSI) | réponse tolérée | `secnumcloud_3_2` / F12 | en vigueur |
| Gouvernance de l'IA : transparence, validation humaine, charte | règles d'usage | F13 § 4 | notion de cours |
