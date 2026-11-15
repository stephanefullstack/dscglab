# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 24 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F12 sécurité et résilience, F06 gestion des connaissances, F10 audit et fiabilisation, F14 numérique responsable, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les risques du système d'information du réseau | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. | 2,5 |
| 3.2 La politique de sécurité du système d'information du réseau | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 4 |
| 3.3 La transmission des savoir-faire du réseau | `1.6.a` Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle ; `1.6.d` Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums ; `1.6.e` Leviers d'appropriation et de transformation des pratiques professionnelles | 2 |
| 3.4 L'audit de la paie des intérimaires | `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 2 |
| 3.5 Inclusion et numérique responsable | `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété ; `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements | 2,5 |
| **Dossier 3 – Sécuriser le système d'information du réseau, transmettre les savoir-faire et rendre le numérique plus responsable** |  | **13** |

Répartition indicative : connaissances (typologie des risques, nature des référentiels, politique de sécurité et triade CID, architecture de confiance, connaissances tacites et explicites, audit du système d'information, gouvernance orientée vers la responsabilité sociétale) 2 points environ (items 3.1 a-1 et b-2 pour moitié, 3.2 a-1 et b-1 pour moitié, 3.3 a-1 pour moitié, 3.4-1 pour moitié, 3.5 a-1 pour moitié) ; analyse des annexes et recommandations 11 points, soit environ 85 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Les risques du système d'information du réseau (2,5 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » (ici, l'évaluation et le choix du traitement des risques prioritaires) ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; ni plan de continuité ni analyse d'impact sur les états financiers ne sont demandés ici.

**Annexes mobilisées** : annexes 3.1 (composants, acteurs, incidents A et B), 3.2 (constats), 3.6 (référentiels) et 1.1 (chiffres clés).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Trois catégories brièvement définies ; deux cybermenaces précises tirées des annexes | 0,5 |
| a-2 | Deux défaillances opérationnelles précises tirées des annexes | 0,5 |
| a-3 | Un risque réglementaire et un risque métier précis tirés des annexes | 0,5 |
| b-1 | Trois risques prioritaires retenus et justifiés (fréquence ou probabilité, gravité, données ou processus touchés) | 0,5 |
| b-2 | Pour chacun, un référentiel ou une méthode de l'annexe 3.6 adapté, dont la nature est juste (norme, guide, méthode ou texte réglementaire) ; 0,5 dès deux rattachements justes | 0,5 |

**Réponse attendue**

*3.1 a) – Typologie et six risques*

Les risques liés au système d'information se répartissent en trois catégories (F12 § 0) : les **cybermenaces**, actions malveillantes qui visent la confidentialité, l'intégrité ou la disponibilité de l'information (usurpation de compte, hameçonnage, fraude, vol) ; les **défaillances opérationnelles**, pannes, erreurs et dépendances sans intention de nuire ; les **risques réglementaires et métiers**, manquements à une obligation légale ou contractuelle et atteintes à l'activité, aux recettes ou à l'image de l'organisation.

| Catégorie | Risques du réseau (annexes 3.1 et 3.2) |
|---|---|
| Cybermenaces (a-1) | (1) **détournement de la paie par usurpation de compte** sur le portail des intérimaires : authentification par simple mot de passe, coordonnées bancaires de 12 intérimaires modifiées par des tiers en 2026 (constat 3) ; (2) **fraude au changement de coordonnées bancaires** par courriel auprès du centre de services, traité sans rappel (une vingtaine de demandes, constat 4) ; variantes : vol de portables contenant des copies de pièces d'identité non chiffrées (constat 5), intrusion depuis une borne en libre-service vers les dossiers de l'agence (constat 6), compromission du compte d'administration commun du prestataire de maintenance (constat 8), exploitation des 40 postes privés de mises à jour de sécurité (constat 9) |
| Défaillances opérationnelles (a-2) | (3) **indisponibilité du logiciel de gestion un jour de paie** et dépendance envers l'éditeur et son hébergeur (incident A : 10 heures, 4 000 intérimaires payés avec deux jours de retard, opération de maintenance non annoncée, aucun décideur désigné) ; (4) **erreur de manipulation dans le partage de fichiers** (incident B : un lien public créé de bonne foi expose 1 200 dossiers pendant 28 jours ; 300 liens publics actifs, sans expiration, constat 7) ; variantes : comptes partagés qui empêchent de savoir qui a fait quoi (constat 1), service de SMS souscrit par douze agences hors de la direction des systèmes d'information (constat 10) |
| Risques réglementaires et métiers (a-3) | (5) **réglementaire** : violation de données personnelles de 1 200 candidats (copies de pièces d'identité) non consignée et sans décision sur la notification à l'autorité de contrôle ni sur l'information des personnes, alors que le repère de l'annexe 3.6 prévoit une notification dans les 72 heures, et que le délégué à la protection des données n'a pas été informé ; plus largement, absence de mesures de sécurité « adaptées au risque » (article 32) pour 80 000 candidats ; (6) **métier** : perte de confiance et départ d'intérimaires (une soixantaine annoncent qu'ils iront chez un concurrent après l'incident A, une centaine de messages critiques), surcharge du centre de services (3 000 appels en deux jours contre 500, 600 heures de travail supplémentaire), atteinte à l'image auprès des clients si les dossiers ou la paie sont en cause |

*3.1 b) – Trois risques prioritaires et référentiels*

Hypothèse à écrire : la priorité combine la probabilité (risque déjà survenu ou facilité de survenance) et la gravité (nombre de personnes, sensibilité des données, paie).

| Risque prioritaire | Justification | Référentiel ou méthode (annexe 3.6) et nature |
|---|---|---|
| Détournement de la paie par usurpation de compte ou faux changement de coordonnées bancaires (1-2) | déjà survenu (12 cas), facile à reproduire, préjudice direct pour des intérimaires souvent fragiles, atteinte à l'intégrité de la paie | **guide d'hygiène informatique de l'ANSSI (2017)**, guide de 42 bonnes pratiques (authentification, gestion des comptes, sensibilisation) ; mesures de sécurité détaillées par le **guide ISO/IEC 27002:2022** |
| Exposition des données des candidats (incident B, postes non chiffrés, liens publics, bornes) (4-5) | 1 200 dossiers exposés en 2026, 80 000 candidats concernés à terme, données sensibles (pièces d'identité), obligation du RGPD | **RGPD** (texte, règlement européen) pour les obligations de sécurité et de notification ; **ISO/IEC 27001:2022**, **norme d'exigences** d'un système de management de la sécurité fondé sur l'appréciation des risques, comme cadre de la politique |
| Indisponibilité du logiciel de gestion un jour de paie et dépendance envers l'éditeur et son hébergeur (3) | déjà survenue deux fois en 2026, 4 000 intérimaires touchés, aucun pouvoir sur l'hébergeur | **EBIOS Risk Manager (version 1.5)**, **méthode** d'appréciation des risques qui intègre l'écosystème (éditeur, hébergeur, prestataire de maintenance) ; ou **ISO/IEC 27005:2022**, **lignes directrices** de gestion des risques |

Le traitement des risques prioritaires suppose de les inscrire dans une démarche continue : appréciation des risques (EBIOS RM ou ISO/IEC 27005), politique et mesures (question 3.2), revue périodique, conformément à la logique d'amélioration continue d'ISO/IEC 27001:2022, sans viser une certification.

**Réponses tolérées**
- Autres risques pertinents tirés des annexes (variantes du tableau) ; un même fait classé dans deux catégories (l'incident B est à la fois une défaillance et un risque réglementaire), s'il est justifié.
- Cotation sur une échelle annoncée (faible, moyenne, forte) ou matrice probabilité × impact.
- Modèle Zero Trust de l'ANSSI cité pour le risque lié aux bornes et aux accès du prestataire, s'il est présenté comme un modèle d'architecture.
- ISO/IEC 27002:2022 et ISO/IEC 27005:2022 qualifiées de normes (de recommandations, non certifiables) : accepté ; seule l'affirmation qu'elles sont certifiables est fausse.
- Mention de NIS 2 pour dire seulement que QUENTALIS Emploi n'y est pas soumise (donnée de l'annexe 3.6), sans en discuter.

**Erreurs fréquentes**
- *Typologie récitée sans faits du cas* (`JUR-T01`, `ET-39`) — liste générique de menaces ; juste : chaque risque est un événement du réseau, chiffré par les annexes.
- *Norme, guide, méthode et solution confondus* (`ET-01`, `JUR-S06`) — « installer ISO 27001 », « acheter EBIOS » ; juste : ISO/IEC 27001:2022 est une norme d'exigences, ISO/IEC 27002:2022 un guide de mesures, EBIOS RM une méthode, le guide d'hygiène un guide de bonnes pratiques.
- *Dérive vers le plan de continuité ou les comptes* (périmètre de la question) — développer un PCA ou chiffrer l'impact comptable de l'incident A ; juste : identifier, classer et hiérarchiser.
- *Discussion de l'assujettissement à NIS 2* (`ET-41`) — juste : c'est une donnée de l'énoncé.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI | trois catégories | F12 § 0 et 5 | notion de cours |
| ISO/IEC 27001:2022 ; ISO/IEC 27002:2022 ; ISO/IEC 27005:2022 | norme d'exigences ; guide des mesures ; gestion des risques | `iso_27001_2022`, `iso_27002_2022`, `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager (ANSSI, version 1.5) | méthode d'appréciation des risques, écosystème | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | 42 mesures | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| RGPD | sécurité (article 32), notification (article 33) | `rgpd` ; F12 § 5 ; F15 | applicable depuis le 25/05/2018 |
| Directive (UE) 2022/2555 (NIS 2) | QUENTALIS Emploi hors champ (donnée) | `nis2` ; F12 § 6 | en vigueur au niveau européen |

---

### 3.2 – La politique de sécurité du système d'information du réseau (4 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique des solutions n'est pas exigée ; le lien avec les normes se fait sans entrer dans les certifications.

**Annexes mobilisées** : annexes 3.1 (composants, acteurs, incidents), 3.2 (constats), 3.6 (repères) et 1.1 (organigramme).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Politique de sécurité définie (document approuvé par la direction, déclinée en charte), objectifs CID et traçabilité appliqués au cas ; trois principes justifiés | 0,5 |
| a-2 | Quatre règles pour les agences et le centre de services, chacune reliée à un constat | 0,5 |
| a-3 | Deux règles pour les portails et le partage de fichiers, reliées à un constat | 0,5 |
| b-1 | Architecture de confiance expliquée ; Zero Trust présenté comme un modèle d'architecture et non comme un produit | 0,5 |
| b-2 | Trois mesures (authentification renforcée, protection des données des candidats, séparation des réseaux), chacune avec le risque traité et une limite ou condition ; 0,5 dès deux mesures complètes | 1 |
| c-1 | Rôles et responsabilités de la direction générale, du directeur des systèmes d'information et des directeurs d'agence | 0,5 |
| c-2 | Rôles de SOLVÉRANE et de son hébergeur (chaîne de sous-traitance) ; pilote au quotidien (responsable de la sécurité) et rattachement justifié | 0,5 |

**Réponse attendue**

*3.2 a) – Définition, principes et règles prioritaires*

La **politique de sécurité du système d'information** (PSSI) est le document de référence, approuvé par la direction générale, qui fixe les objectifs, le périmètre, les principes, l'organisation (rôles) et les règles de sécurité, ainsi que le dispositif de contrôle ; elle se décline en une **charte informatique** opposable aux utilisateurs et en procédures (F12 § 1). Elle se fonde sur l'analyse des risques (question 3.1). Ses objectifs, appliqués au réseau : **confidentialité** des dossiers de 80 000 candidats (pièces d'identité) et des coordonnées bancaires des intérimaires ; **intégrité** des coordonnées bancaires et des heures, dont dépend la paie ; **disponibilité** du logiciel de gestion le jour de la paie ; **traçabilité** des actions, impossible aujourd'hui avec des comptes partagés.

Trois principes (a-1) :
1. **Une sécurité fondée sur les risques et proportionnée** : priorité aux données des candidats et à la chaîne de paie, mesures simples pour les agences, revue annuelle.
2. **Moindre privilège et imputabilité** : chacun n'accède qu'à ce dont il a besoin, avec un compte personnel, et ses actions sont tracées.
3. **Responsabilités partagées et écrites** : chaque acteur, interne ou externe, connaît ses obligations ; la sécurité est intégrée aux achats, aux projets (dématérialisation) et aux relations avec les prestataires.

Règles prioritaires (a-2 et a-3) :

| Périmètre | Règle | Constat traité |
|---|---|---|
| Agences | **comptes nominatifs** pour tous les collaborateurs ; fin des comptes d'agence et des mots de passe affichés | constat 1 (30 agences sur 46) |
| Agences | **aucun dossier de candidat enregistré sur un poste** : dépôt dans l'espace de l'agence prévu à cet effet ; portables chiffrés ; aucun service numérique souscrit sans validation de la direction des systèmes d'information | constats 5 et 10 (deux portables volés, SMS de douze agences) |
| Centre de services | **aucun changement de coordonnées bancaires sur simple courriel** : demande faite depuis l'espace authentifié de l'intérimaire ou confirmée par un rappel au numéro déjà connu | constats 3 et 4 |
| Centre de services | **procédure de gestion des incidents**, transversale et pilotée par le responsable de la sécurité, appliquée en priorité au centre de services : registre, qualification, information immédiate du délégué à la protection des données en cas de violation de données, décision écrite sur la notification dans les 72 heures, interlocuteur désigné pour l'éditeur en cas d'incident sur le logiciel | incidents A et B, constat 11 |
| Portails | **alerte de l'intérimaire sur un autre canal** et délai de prise en compte avant toute modification de ses coordonnées bancaires sur le portail | constat 3 |
| Partage de fichiers | **liens publics interdits par défaut** ; partage avec un client par lien nominatif, à durée limitée, sur un dossier qui ne contient que les profils transmis ; revue des 300 liens actifs | incident B, constat 7 |

La politique est complétée par la mise à jour de la **charte informatique** de 2016 (portails, partage, postes), remise et expliquée à chaque nouvel arrivant, et par une **sensibilisation** annuelle, interrompue depuis 2022 (constat 11).

*3.2 b) – Architecture de confiance*

Une **architecture de confiance** organise le système d'information pour que chaque accès à une ressource soit authentifié, autorisé et protégé, et pour qu'une compromission reste contenue ; elle combine l'**authentification** (prouver son identité), le **chiffrement** (rendre les données illisibles sans clé) et la **segmentation** (cloisonner les réseaux et les flux). Le **modèle Zero Trust** (avis de l'ANSSI, 2021, annexe 3.6) en est un cadre : il n'accorde aucune confiance implicite liée à la position sur le réseau et vérifie chaque accès selon l'identité, l'état du poste et la sensibilité de la ressource ; ce n'est **ni un produit ni une solution logicielle**, mais une évolution progressive qui ne remplace pas la défense en profondeur (b-1).

| Mesure | Principe | Risque traité | Limite ou condition |
|---|---|---|---|
| **Authentification renforcée du portail des intérimaires** | au moins deux facteurs de nature différente (mot de passe et code reçu sur le téléphone, par exemple), exigés au moins pour les opérations sensibles : modification des coordonnées bancaires, signature d'un contrat | usurpation de compte et détournement de la paie (12 cas en 2026) | 20 % des intérimaires n'ont pas de smartphone ou ne savent pas s'en servir (annexe 3.5) : prévoir un second facteur accessible (code par SMS sur un téléphone simple) ou une vérification en agence ; sinon, la mesure exclut des intérimaires (question 3.5) |
| **Protection des données des candidats** | données conservées dans les espaces prévus (logiciel, dossier de l'agence) et non sur les postes ; **chiffrement** des portables et des espaces de stockage ; accès limité à l'agence et aux personnes qui en ont besoin | vol ou perte d'un poste (deux portables volés), fuite de copies de pièces d'identité | le chiffrement ne protège pas contre un utilisateur autorisé qui partage mal (incident B) : il va avec des droits d'accès et des règles de partage ; la gestion des clés doit être organisée |
| **Séparation entre les bornes en libre-service et les postes des collaborateurs** | les bornes sont placées sur un réseau distinct, qui ne donne accès qu'au service d'inscription des candidats ; aucun flux entre ce réseau et celui des collaborateurs | rebond d'un candidat ou d'un tiers depuis une borne vers les dossiers de l'agence (constat 6) | suppose l'inventaire des équipements et des flux de chaque agence et l'intervention encadrée du prestataire de maintenance ; la décision appartient à la direction des systèmes d'information, la réalisation technique n'est pas à décrire |

*3.2 c) – Rôles et responsabilités*

| Acteur | Responsabilités |
|---|---|
| Direction générale (Mme BRÉQUEMONT) (c-1) | responsable en dernier ressort : approuve la politique et le niveau de risque accepté, arbitre les moyens, désigne le pilote de la sécurité et les décideurs en cas d'incident, en rend compte au président (priorité du plan « QUENTALIS 2030 ») ; préside une revue de la sécurité en comité de direction, au moins deux fois par an |
| Directeur des systèmes d'information (M. ROUVELIN) (c-1) | conçoit et met en œuvre les mesures (comptes, postes, réseaux, outils de partage), tient l'inventaire des équipements et des comptes, pilote le prestataire de maintenance et la relation technique avec SOLVÉRANE, traite les incidents techniques |
| Directeurs d'agence (46) (c-1) | font appliquer la charte dans leur agence (comptes personnels, postes, dossiers de candidats, partage), signalent les incidents, ne souscrivent aucun service numérique sans validation ; chacun désigne un correspondant de la sécurité parmi les assistants |
| SOLVÉRANE, éditeur (c-2) | assure la sécurité et la disponibilité du logiciel qu'il fournit, annonce à l'avance toute maintenance et l'interdit les jours de paie, notifie sans délai tout incident, fournit des éléments de preuve de son niveau de sécurité et de celui de son hébergeur ; il traite des données personnelles pour le compte de QUENTALIS Emploi |
| Hébergeur (c-2) | assure la sécurité physique et l'exploitation des centres de données et des sauvegardes ; il répond à SOLVÉRANE, avec qui QUENTALIS Emploi n'a aucun lien direct : ses engagements doivent donc être obtenus par l'intermédiaire de l'éditeur, qui reste responsable de son sous-traitant |

**Pilote au quotidien** (c-2) : un **responsable de la sécurité des systèmes d'information** (RSSI), éventuellement à temps partagé ou mutualisé avec un prestataire, chargé de faire vivre la politique (risques, règles, sensibilisation, incidents, contrôle des prestataires, veille). Il est **rattaché à la directrice générale** et non au directeur des systèmes d'information, afin de pouvoir contrôler les mesures que celui-ci met en œuvre sans conflit d'intérêts et d'avoir autorité sur les agences ; il travaille avec le délégué à la protection des données, dont le rôle porte sur les données personnelles et qui doit être informé de toute violation (incident B).

**Réponses tolérées**
- Autres principes : défense en profondeur, sécurité dès la conception des projets, sensibilisation de tous.
- Autres règles reliées aux constats : accès à distance du prestataire de maintenance sur demande, nominatif et tracé (constat 8) ; remplacement ou mise à jour des 40 postes sans mises à jour de sécurité (constat 9) ; demande à SOLVÉRANE d'éléments sur la sécurité de son hébergeur (constat 11).
- Comité de sécurité trimestriel (direction générale, RSSI, DSI, directeur du réseau, responsable du centre de services, délégué à la protection des données) proposé comme instance de pilotage.
- RSSI externalisé, s'il est rattaché à la direction générale et doté d'un correspondant interne.

**Erreurs fréquentes**
- *PSSI confondue avec la charte* (`ET-27`) — juste : la PSSI fixe les objectifs, règles et responsabilités ; la charte décline les règles d'usage opposables.
- *Zero Trust présenté comme un produit* (`ET-04`, `JUR-S03`) — proposer d'en faire l'achat comme d'un logiciel ; juste : modèle d'architecture, mis en œuvre progressivement.
- *Mesures techniques détaillées* (`JUR-T12`) — réglages des équipements, configuration du réseau ; juste : principes et règles, sans paramétrage.
- *Authentification renforcée sans regard sur les intérimaires sans smartphone* (`JUR-T01`) — juste : la mesure doit prévoir une solution accessible.
- *RSSI rattaché au DSI ou décrit comme un technicien* (`ET-15`) — juste : pilote de la politique, indépendant de l'exploitation, rattaché à la direction.
- *Responsabilité de l'hébergeur envers QUENTALIS Emploi supposée directe* — juste : il répond à l'éditeur, qui doit en porter les engagements.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| PSSI, triade CID et traçabilité, acteurs | définition, objectifs, rôles | F12 § 1 | notion de cours |
| Le modèle Zero Trust (avis de l'ANSSI, 2021) | modèle d'architecture | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| ISO/IEC 27001:2022 ; ISO/IEC 27002:2022 | système de management fondé sur les risques ; mesures | `iso_27001_2022`, `iso_27002_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | comptes, mises à jour, sensibilisation | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| RGPD | sécurité adaptée au risque, sous-traitant, notification | `rgpd` ; F15 | applicable depuis le 25/05/2018 |

---

### 3.3 – La transmission des savoir-faire du réseau (2 points)

**Référence au programme**
- §1.6 – Mettre en œuvre et piloter la gestion des connaissances au sein du système d'information : `1.6.a` « Mettre en œuvre une stratégie de gestion des connaissances soutenue par les systèmes d'information, en assurant son pilotage, sa gouvernance et son appropriation organisationnelle » ; `1.6.d` « Intégration des outils de KM dans l'environnement SI : GED, intranet, wiki, forums » ; `1.6.e` « Leviers d'appropriation et de transformation des pratiques professionnelles ». Limites : la gestion des connaissances dépasse la seule numérisation de l'information ; le lien avec la gestion des compétences est complémentaire mais distinct.

**Annexes mobilisées** : annexes 3.3 (constat, outils, projet, témoignages) et 1.1 (effectif, organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Connaissances tacites et explicites distinguées et appliquées aux savoir-faire de l'annexe ; deux raisons de l'échec des outils existants | 0,5 |
| a-2 | Deux dispositifs adaptés à la rotation, intégrés à l'environnement de travail (intranet, logiciel de gestion) | 0,5 |
| b-1 | Pilotage et gouvernance : sponsor, animateur, référents, contributeurs, règles de mise à jour | 0,5 |
| b-2 | Trois leviers d'appropriation, chacun en réponse à une réserve d'un témoignage | 0,5 |

**Réponse attendue**

*3.3 a) – Diagnostic et dispositif*

Une **connaissance explicite** est formalisée et transmissible par un document (procédure, fiche, modèle) ; une **connaissance tacite** est incorporée dans les personnes, issue de l'expérience, difficile à formuler (F06 § 1). Au réseau, l'essentiel des savoir-faire critiques est **tacite** : la connaissance des sites des clients, ce qu'un client entend par « cariste confirmé », les règles des grands comptes et le traitement des anomalies de paie sont « dans la tête » des anciens (Mme FOUQUERELLE, M. DUFRESCQ). Avec 35 départs de chargés de recrutement sur 100 en 2026, une ancienneté moyenne de deux ans et environ six mois avant qu'un nouveau chargé de recrutement soit autonome, ces savoirs partent plus vite qu'ils ne se transmettent.

Pourquoi les outils existants n'ont pas suffi (a-1) : ils ont traité la gestion des connaissances comme une **numérisation de documents** : l'intranet n'est ni à jour (40 % des 1 500 documents ont plus de trois ans) ni consulté (15 % des permanents par mois) ni fiable aux yeux des nouveaux (M. SANVOISIN) ; le forum, sans animation ni réponse, a été abandonné ; les documents sont dispersés ; rien n'est intégré au travail quotidien (le lien vers un document depuis la fiche client du logiciel n'est pas utilisé) ; enfin, aucun dispositif ne capte le savoir tacite des anciens, qui ne veulent ou ne peuvent pas « rédiger » (Mme LOMBRECQ).

Dispositif proposé (a-2) :
1. **Communautés de pratique entre agences**, une par secteur (industrie, logistique, bâtiment, tertiaire) et une pour la paie au centre de services, animées par les référents qu'envisage M. HAVERCQ : échanges courts et réguliers sur les cas concrets, binômes entre un nouveau chargé de recrutement et un ancien d'une autre agence, visites de sites de clients en commun ; elles transmettent le tacite par l'échange et la pratique.
2. **Fiches courtes, au format d'un wiki, accessibles depuis le logiciel de gestion** : une fiche par grand compte et par site (accès, équipements de protection, consignes, interlocuteurs), une fiche par métier (définition des qualifications, questions d'entretien), une fiche par cas type d'anomalie de paie ; chaque fiche est reliée à la fiche client du logiciel par la fonction de lien existante et rangée dans un intranet nettoyé, qui devient le point d'entrée unique ; les fiches sont rédigées par le référent ou un assistant à partir d'un entretien ou d'une visite avec l'ancien, qui les valide sans avoir à les écrire.

*3.3 b) – Pilotage, gouvernance et appropriation*

Gouvernance (b-1) : **sponsor** M. HAVERCQ, avec l'appui de la direction générale (priorité du plan « QUENTALIS 2030 ») ; un **animateur de la gestion des connaissances** au sein de la direction du réseau, qui coordonne les communautés et la qualité des fiches ; des **référents** par secteur et un référent au centre de services, qui valident et mettent à jour ; les **contributeurs** (chargés de recrutement, assistants, gestionnaires) ; la **direction des systèmes d'information** pour l'intégration au logiciel et à l'intranet et les droits d'accès ; aucune donnée personnelle de candidat dans les fiches. Règles : chaque fiche a un propriétaire, une date de dernière validation affichée et une revue au moins semestrielle ou à chaque changement chez le client ; gabarit d'une page ; les documents périmés de l'intranet sont archivés ou supprimés.

Trois leviers d'appropriation (b-2) :

| Levier | Réponse au témoignage |
|---|---|
| **Intégrer les fiches au flux de travail et en garantir la fraîcheur** : la fiche s'ouvre depuis la commande ou la fiche client du logiciel, avec le nom du référent et la date de validation | M. SANVOISIN « ne sait pas si c'est à jour » : la date et le référent affichés rendent la fiche fiable ; il n'a plus à « chercher » dans l'intranet |
| **Capter sans faire rédiger, et reconnaître la contribution** : entretiens, visites ou courtes vidéos menés par un référent ou un assistant ; temps dédié pour les référents ; contribution reconnue dans les objectifs des directeurs d'agence et valorisée (auteur cité) | Mme LOMBRECQ : « montrer, oui ; rédiger, non » |
| **Organiser la transmission dans le temps et l'accueil des nouveaux** : binôme désigné et créneaux planifiés avant le départ de M. DUFRESCQ fin 2027 ; parcours d'accueil des nouveaux chargés de recrutement fondé sur les fiches et sur un binôme ; premières fiches sur les grands comptes, pour des gains visibles rapides | M. DUFRESCQ : « à qui, et quand ? » ; Mme FOUQUERELLE : trois mois perdus au départ d'une collègue |

**Réponses tolérées**
- Modèle SECI (Nonaka et Takeuchi, 1995) mobilisé pour structurer le dispositif (socialisation par les binômes, externalisation par les entretiens, combinaison dans les fiches, internalisation par l'usage), s'il est appliqué.
- Relance d'un forum, s'il est animé par les référents et intégré aux communautés.
- Démarche de conduite du changement nommée (ADKAR, huit étapes de Kotter) pour présenter les leviers, si elle est appliquée.
- Autres leviers : exemplarité des directeurs d'agence, mesure de l'usage des fiches, rituel d'équipe hebdomadaire.

**Erreurs fréquentes**
- *Gestion des connaissances réduite à un outil ou à la GED* (`ET-21`) — « refaire l'intranet » ; juste : dispositif systémique (outils, processus, culture).
- *Dérive vers la gestion des compétences ou le recrutement* (limite 1.6) — plan de formation, fidélisation des chargés ; juste : capitaliser et partager les savoirs.
- *Leviers génériques sans lien avec les témoignages* (`JUR-T08`, `JUR-P04`) — juste : chaque levier répond à une réserve exprimée.
- *Cartographie détaillée des savoirs* (hors du périmètre de la question) — juste : les savoirs critiques sont donnés par l'annexe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Connaissances tacites et explicites ; dispositif de gestion des connaissances ; gouvernance ; appropriation | définitions, architecture, rôles, leviers | F06 § 1 et 2 | notion de cours |
| Modèle SECI (Nonaka et Takeuchi) | modes de conversion (toléré) | `nonaka_takeuchi_seci` ; F06 § 1 | publié |

---

### 3.4 – L'audit de la paie des intérimaires (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la conformité financière et comptable n'est pas traitée dans le programme de l'UE 5 ; l'audit suppose une approche multidisciplinaire et une posture critique vis-à-vis de la gouvernance.

**Annexes mobilisées** : annexes 3.4 (demande de la directrice générale), 3.1 (acteurs, SOLVÉRANE), 3.3 (anomalies de paie au centre de services) et 1.1 (organigramme, rôle du contrôleur de gestion).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| 1 | Audit du SI défini et appliqué à la chaîne relevé d'heures – paie – facturation (fiabilité des traitements, non recalcul de la paie) | 0,5 |
| 2 | Quatre facteurs de succès appliqués au cas ; 0,5 dès trois | 0,5 |
| 3 | Trois points de vigilance tirés de l'annexe 3.4 | 0,5 |
| 4 | Option d'auditeur recommandée et justifiée par l'indépendance et les compétences | 0,5 |

**Réponse attendue**

L'**audit du système d'information** est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel (politique interne, bonnes pratiques, réglementation), la fiabilité, la sécurité, la conformité et la performance du système d'information et des processus qu'il supporte, et qui débouche sur des recommandations (F10 § 1). Ici, il porte sur la **fiabilité de la chaîne** relevé d'heures – paie – facturation : modes de transmission et de validation des relevés, saisies et ressaisies, contrôles automatiques du logiciel de gestion, droits d'accès et séparation des tâches, traitement des anomalies au centre de services. Il ne s'agit ni de recalculer la paie, ni de vérifier la conformité sociale ou comptable (1). Les 2 400 bulletins rectificatifs (2 % des 120 000) et les 2 500 avoirs, dont 1 500 pour des grands comptes, en sont les symptômes.

Quatre facteurs de succès (2) :
1. **Un mandat clair, porté par la directrice générale** : objectifs (localiser l'origine des erreurs : logiciel, saisies, agences, clients), périmètre réaliste et réponse attendue, formalisés dans une lettre de mission ; le soutien affiché de Mme BRÉQUEMONT ouvre les portes des agences et de l'éditeur.
2. **L'indépendance et les compétences pluridisciplinaires de l'auditeur** : audit des systèmes d'information, connaissance de la paie et de la facturation du travail temporaire, capacité d'analyse de données.
3. **L'accès aux données et à l'éditeur obtenu avant le démarrage** : demande formelle à SOLVÉRANE, portée par la direction générale, des journaux du logiciel, de la description des contrôles automatiques et des paramètres utiles ; extraction des bulletins rectificatifs et des avoirs de 2026 pour en analyser les causes.
4. **L'implication des métiers et l'adhésion des audités** : présentation de la mission au centre de services, aux agences et aux deux grands comptes qui ont réclamé, entretiens avec les gestionnaires (dont M. DUFRESCQ), validation contradictoire des constats ; les **suites** sont prévues dès le départ (plan d'action avec responsables et échéances, suivi en comité de direction).

Trois points de vigilance (3) :
1. **Le calendrier** : huit semaines environ, en pleine période de forte activité des agences ; le périmètre doit être resserré (quelques agences et grands comptes représentatifs, les causes principales des rectifications) et les entretiens planifiés tôt, sous peine de conclusions superficielles au comité de fin mai.
2. **L'accès aux informations de l'éditeur** : jamais demandé jusqu'ici ; sans les journaux ni la description des contrôles, la part du logiciel dans les erreurs restera inconnue, ou sera attribuée par défaut aux saisies.
3. **Le climat au centre de services** : la mission doit auditer des processus et des contrôles, et non des personnes ; une mise en accusation ferait perdre la coopération des gestionnaires, déjà sous tension, et la confiance dans les recommandations.

Variantes : confidentialité des données personnelles des intérimaires consultées par l'auditeur (accès limité, engagement de confidentialité) ; tentation d'élargir l'audit à la conformité de la paie, qui relève d'autres compétences.

**Option recommandée** (4) : le **cabinet spécialisé dans l'audit des systèmes d'information**, appuyé par des correspondants internes. L'équipe interne n'est pas indépendante : le contrôleur de gestion est chargé du pilotage économique du système d'information et des projets de transformation, et la gestionnaire de paie évaluerait son propre service ; elle n'a pas l'expérience de l'audit et ne pourrait se libérer en période de forte activité. Le cabinet apporte méthode, compétences et regard extérieur, et sera mieux placé pour obtenir les informations de SOLVÉRANE ; le contrôleur de gestion et une gestionnaire de paie lui apportent leur connaissance des processus, comme interlocuteurs et non comme auditeurs. Inconvénients à maîtriser : coût, temps d'appropriation du métier, d'où un cadrage précis.

**Réponses tolérées**
- Option mixte (équipe interne pilotée par le cabinet), si l'indépendance des conclusions est assurée par le cabinet.
- Référentiel d'audit cité (COBIT 2019 pour les processus et les contrôles, politique interne), sans développement.
- Autres facteurs de succès : posture critique vis-à-vis de la gouvernance (absence de propriétaire de la chaîne), restitution adaptée au président.

**Erreurs fréquentes**
- *Démarche complète d'audit récitée* (`JUR-T07`) — étapes, programme de travail et échéancier détaillés ; juste : la question porte sur les facteurs de succès et les points de vigilance.
- *Audit du SI confondu avec un audit légal ou un recalcul de la paie* (`ET-34`) — juste : fiabilité des traitements et des contrôles du système d'information.
- *Facteurs génériques sans lien avec l'annexe* (`JUR-T01`) — juste : calendrier de huit semaines, éditeur jamais sollicité, centre de services sous tension.
- *Oubli de l'indépendance du contrôleur de gestion* (`JUR-T03`) — juste : il est partie prenante du pilotage du système d'information.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du système d'information ; facteurs de succès | définition, types, conditions | F10 § 0 et 1 | notion de cours |
| COBIT 2019 | référentiel d'audit des processus (toléré) | `cobit_2019` ; F02 | en vigueur |

---

### 3.5 – Inclusion et numérique responsable (2,5 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété » ; `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ». Limites : la durabilité est intégrée à la gouvernance globale du SI ; aucun calcul d'empreinte n'est demandé ; l'assujettissement à un cadre de durabilité est une donnée.

**Annexes mobilisées** : annexes 3.5 (dématérialisation, enquête, pilote, parc), 3.6 (loi REEN, RGESN), 3.2 (postes sans mises à jour) et 1.1.

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance orientée vers la responsabilité sociétale expliquée (critères sociaux et environnementaux dans les décisions du SI, instance, charte) ; instance qui décide dans le cas | 0,5 |
| a-2 | Trois mesures d'inclusion (accompagnement, solution de substitution, éthique) appliquées à l'annexe 3.5 | 0,5 |
| b | Trois bonnes pratiques pour le parc et l'application, appuyées sur l'annexe 3.5 et sur les repères, conciliées avec la sécurité ; 0,5 dès deux pratiques justifiées | 1 |
| c | Deux indicateurs complets (formule, source, fréquence, cible, axe) | 0,5 |

**Réponse attendue**

*3.5 a) – Gouvernance orientée vers la responsabilité sociétale et inclusion*

Une **gouvernance du système d'information orientée vers la responsabilité sociétale** intègre, dans les décisions sur le système d'information (projets, achats, règles d'usage), des critères **sociaux** (inclusion, accessibilité, éthique) et **environnementaux** (sobriété, durée de vie), au même titre que les coûts et les risques : instance qui arbitre, charte du numérique responsable, critères d'acceptation des projets, indicateurs suivis (F14 § 0 et 3). Elle n'est pas un ajout marginal : elle conditionne ici le projet de dématérialisation.

Application : 20 % des intérimaires interrogés n'ont pas de smartphone ou ne savent pas s'en servir pour une démarche, 10 % n'ont pas d'adresse électronique, 15 % peinent à lire un document en français ; dans le pilote, 20 % des contrats ont dû être signés en agence et 240 réclamations ont été reçues pour 6 000 contrats ; Mme CAMBRELIN craint que certains renoncent à des missions. Une dématérialisation « exclusive » au 1er septembre 2027 exclurait une partie des intérimaires, souvent les plus fragiles.

Trois mesures (a-2) :
1. **Accompagnement** : aide à l'installation et à la première signature lors de l'inscription en agence, assistants formés comme relais numériques, documents en langage simple avec pictogrammes, assistance téléphonique du centre de services.
2. **Solution de substitution** maintenue sans condition : signature en agence avec l'aide d'un assistant ou document papier sur demande ; aucun intérimaire ne doit perdre une mission faute d'équipement ; même logique pour les petits clients qui n'utilisent pas le portail.
3. **Éthique** : ne pas favoriser, dans les propositions de missions, les intérimaires qui utilisent l'application ; expliquer clairement ce que l'on signe ; ne collecter que les données nécessaires ; vérifier que l'authentification renforcée (question 3.2) reste accessible.

Instance (a-1) : la décision revient au **comité de direction**, présidé par la directrice générale, sur proposition d'un **comité du numérique responsable** (direction des systèmes d'information, centre de services, direction du réseau, ressources humaines, contrôle de gestion, éventuellement des intérimaires volontaires), qui fixe les critères d'inclusion du projet et conditionne la généralisation de septembre 2027 aux résultats du pilote.

*3.5 b) – Trois bonnes pratiques*

Les trois pratiques attendues peuvent porter sur le parc des agences ou sur l'application des intérimaires : les quatre pratiques du tableau se valent, trois suffisent.

| Bonne pratique | Application à l'annexe 3.5 | Lien avec les repères et la sécurité |
|---|---|---|
| **Allonger la durée de vie des équipements** par une politique de renouvellement écrite | ne pas remplacer systématiquement les 120 postes de plus de cinq ans : remplacer à la panne ou quand le poste ne peut plus recevoir de mises à jour ; conserver les 250 écrans, en bon état, au lieu de les changer avec les postes | la fabrication des équipements est le premier poste d'empreinte du numérique ; la loi REEN lutte contre le renouvellement trop fréquent des terminaux ; l'allongement ne vaut que pour des postes encore mis à jour : les 40 postes sans mises à jour de sécurité (constat 9) sont à mettre à jour ou à remplacer en priorité |
| **Recourir au reconditionnement et au réemploi** | acheter des postes reconditionnés garantis trois ans pour les remplacements (0,5 k€ contre 1 k€ pièce : 60 k€ au lieu de 120 k€ pour 120 postes) ; confier les anciens postes à une filière de réemploi, par exemple une structure d'insertion qui équipe des personnes éloignées du numérique | soutien au réemploi et au reconditionnement (loi REEN) ; effacement sécurisé des données des candidats avant toute sortie d'un poste |
| **Mutualiser et sobriété des usages** | remplacer les imprimantes individuelles par une imprimante partagée par agence ; la dématérialisation accompagnée réduit les 5 millions de pages ; éteindre les 46 bornes en dehors des heures d'ouverture | sobriété : questionner le besoin (bornes allumées la nuit et le week-end) avant l'efficacité ; impression sécurisée par badge pour les dossiers de candidats |
| **Écoconcevoir l'application des intérimaires** | rendre l'application utilisable sur des smartphones de plus de cinq ans et alléger sa page d'accueil (images, vidéos) | RGESN, version 2024 (compatibilité avec des terminaux anciens, sobriété des contenus) ; double bénéfice d'inclusion et d'empreinte |

*3.5 c) – Deux indicateurs*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Taux de réclamations liées à la dématérialisation | nombre de réclamations liées à la signature ou à l'accès en ligne / nombre de contrats de mission établis × 1 000 | suivi des réclamations du centre de services ; logiciel de gestion (contrats) | mensuelle | moins de 10 pour 1 000 contrats fin 2027, contre 40 pour 1 000 dans le pilote (240 pour 6 000) | social |
| Part des postes reconditionnés dans les postes acquis | nombre de postes reconditionnés acquis dans l'année / nombre total de postes acquis dans l'année | inventaire du parc tenu par la direction des systèmes d'information ; achats | annuelle | au moins 80 % en 2028 | environnement |

(0,5 pt pour les deux indicateurs complets.) Le taux de réclamations est à lire avec la part des contrats signés par une solution de substitution : il pourrait baisser parce que des intérimaires renoncent à l'application. L'exigence qu'aucun poste ne reste en service sans mises à jour de sécurité relève de la politique de renouvellement (question 3.5 b), et non de cet indicateur.

**Réponses tolérées**
- Autres mesures d'inclusion : borne d'inscription accompagnée en agence, traduction des documents essentiels, délai de bascule progressif par agence.
- Autres bonnes pratiques : critères de durabilité dans les achats, gestes des collaborateurs, réduction du stockage de documents en double.
- Autres indicateurs complets : part des contrats signés par une solution de substitution (suivi de l'inclusion, sans cible de baisse forcée), durée de vie moyenne des postes à leur retrait, nombre de pages imprimées par agence, heures d'allumage des bornes.
- Mention du volet social de la responsabilité sociétale (ISO 26000 citée comme lignes directrices), sans développement.

**Erreurs fréquentes**
- *Dématérialisation présentée comme toujours vertueuse* (`ET-12`, `JUR-T03`) — juste : elle exclut une partie des intérimaires si elle n'est pas accompagnée et peut déplacer l'empreinte vers les terminaux.
- *Sobriété confondue avec l'économie d'énergie* (`ET-12`) — juste : la sobriété questionne le besoin.
- *Allongement de la durée de vie sans regard sur la sécurité* (`JUR-T11`) — garder des postes sans mises à jour ; juste : concilier durée de vie et sécurité.
- *Calcul d'empreinte ou discussion de la CSRD* (`ET-41`) — juste : ni calcul ni assujettissement, qui est une donnée.
- *Indicateurs incomplets* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gouvernance orientée vers la responsabilité sociétale ; Green IT et sobriété | définitions, bonnes pratiques | F14 § 0, 3 et 4 | notion de cours |
| Loi REEN n° 2021-1485 | renouvellement des terminaux, réemploi, écoconception | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | écoconception de l'application | `rgesn_2024` ; F14 § 2 | en vigueur |
| Directive (UE) 2022/2464 (CSRD) | QUENTALIS Emploi hors champ (donnée) | `csrd` ; fiche commune | en vigueur |
| ISO 26000:2010 | lignes directrices de responsabilité sociétale (toléré) | `iso_26000_2010` | en vigueur |
