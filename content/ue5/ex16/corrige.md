# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 16 — Dossier 1 (14 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F12 sécurité et résilience, F10 fiabilisation des SI comptables, F13 intelligence artificielle, F03 cloud et souveraineté, F07 données de référence et souveraineté, F02 comitologie, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

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
