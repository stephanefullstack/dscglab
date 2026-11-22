# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 45 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 audit et fiabilisation, F12 sécurité et résilience, F13 intelligence artificielle, F14 numérique responsable, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les risques de la flotte et de la plateforme, et l'outil de détection | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ; `4.1.f` Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques | 3 |
| 3.2 La politique de sécurité de CIRCÉA et des bornes | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 4 |
| 3.3 L'audit de la tarification variable | `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.e` Facteurs de succès et points de vigilance spécifiques à l'audit SI | 2,5 |
| 3.4 Une recharge plus responsable | `4.3.c` Gouvernance SI orientée RSE : inclusion, éthique, sobriété ; `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements | 3,5 |
| **Dossier 3 – Sécuriser la plateforme et les bornes, auditer la tarification variable et rendre le réseau plus responsable** |  | **13** |

Répartition indicative : connaissances (nature d'une méthode d'analyse des risques, apprentissage automatique et place de la détection, politique de sécurité fondée sur les risques, audit du SI, gouvernance du SI orientée vers la responsabilité sociétale) environ 2 points (la moitié des items 3.1 a-1 et 3.1 b-1, l'item 3.2 a-1, la moitié des items 3.3 a-1 et 3.4 a-1) ; analyse des annexes et recommandations environ 11 points, soit environ 85 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – Les risques de la flotte et de la plateforme, et l'outil de détection (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. » ; `4.1.f` « Apports potentiels de l'intelligence artificielle dans la détection et la prévention des risques ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; le développement d'algorithmes d'apprentissage automatique n'est pas attendu (2.2).

**Annexes mobilisées** : annexe 3.1 (quatre incidents, essai de l'outil, points de vue, échelles), annexe 3.5 (ISO/IEC 27001:2022, ISO/IEC 27005:2022, EBIOS Risk Manager, guide d'hygiène, règlement sur l'IA) et annexe 1.1 (réseau, CIRCÉA, entreprises de maintenance, centre de supervision ouvert jour et nuit).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Méthode retenue, sa nature (méthode, lignes directrices ou norme d'exigences, à distinguer) et la justification de son choix au regard du cas (écosystème des constructeurs, des entreprises de maintenance et du fournisseur de cloud) | 0,5 |
| a-2 | Quatre risques formulés comme des événements redoutés, tirés de l'annexe 3.1, avec une probabilité et un impact justifiés selon les échelles | 0,5 |
| a-3 | Deux risques prioritaires retenus et justifiés par leur criticité et par leur portée sur tout le réseau | 0,5 |
| b-1 | Outil caractérisé (apprentissage automatique, détection d'anomalies, et non IA générative), situé surtout dans la détection, et limites tirées de l'annexe (faux positifs, données d'apprentissage, angles morts, coupure à tort) | 0,5 |
| b-2 | Trois règles d'emploi, dont la décision humaine avant toute coupure, en réponse à M. OLMAREC | 0,5 |
| b-3 | Indicateur complet (formule, source, fréquence, cible, axe) rattaché à l'une des règles | 0,5 |

**Réponse attendue**

*3.1 a) – La méthode, les quatre risques et les deux priorités*

**La méthode** (a-1) : **EBIOS Risk Manager**, version 1.5 (ANSSI, 2024), est une **méthode** d'appréciation et de traitement des risques numériques en cinq ateliers, compatible avec les **lignes directrices** ISO/IEC 27005:2022 ; ISO/IEC 27001:2022 est une **norme d'exigences** de système de management, et non une méthode d'analyse (F12 § 2 ; annexe 3.5). Elle convient à AMPÉRANE pour trois raisons : trois des quatre incidents de 2026 sont passés par l'**écosystème** (un constructeur, une entreprise de maintenance, le fournisseur de cloud), que l'atelier 3 analyse explicitement ; elle part des valeurs métier (recharger, facturer au juste prix, commander les bornes à distance) avant les biens techniques ; elle aboutit à un plan de traitement qui fonde la politique de sécurité demandée par les fonds (question 3.2). Application résumée : cadrage et socle (CIRCÉA, 3 600 bornes et leurs micrologiciels, comptes, hébergement ; écarts au socle d'hygiène : comptes partagés, mots de passe jamais changés, sauvegardes jamais restaurées) ; sources de risque (cybercriminels qui fraudent ou rançonnent, erreur ou défaillance d'un fournisseur, technicien parti) ; scénarios stratégiques par les constructeurs, les entreprises de maintenance et le fournisseur de cloud ; scénarios opérationnels ; traitement.

**Quatre risques, évalués selon les échelles de l'annexe 3.1 D** (a-2) :

| Risque (événement redouté) | Incident de l'annexe 3.1 | Probabilité | Impact | Criticité |
|---|---|---|---|---|
| R1 – Une version de micrologiciel défaillante ou piégée, installée sans essai ni vérification de son origine sur tout un modèle, arrête des centaines de points ou les met sous le contrôle d'un tiers | mai 2026 : 300 points, soit 12,5 % des points rapides, bloqués deux jours ; environ 1 800 sessions et 50 k€ perdus ; fichier reçu par courriel | 3 : déjà survenu, et l'installation en une fois sans essai reste la pratique ; quatre constructeurs, versions fréquentes | 4 : un modèle entier d'un coup ; un fichier piégé donnerait la main sur toutes ces bornes ; deux jours d'arrêt consomment à eux seuls plus du quart de l'indisponibilité annuelle que permet l'objectif de 98 % par point (environ sept jours) | 12 |
| R2 – Un tiers malveillant ou un technicien parti utilise le compte partagé d'une entreprise de maintenance pour redémarrer, couper ou reconfigurer des bornes de tout le réseau | novembre 2026 : 40 bornes redémarrées de nuit depuis un poste infecté ; compte de douze techniciens, mot de passe inchangé depuis 2022, cause comprise en deux jours | 3 : déjà exploité, et les sept comptes sont toujours partagés par environ 120 personnes, jamais revus | 4 : chaque compte commande tout le réseau ; l'intégrité des tarifs n'a pas pu être établie | 12 |
| R3 – Des fraudeurs détournent le paiement des conducteurs par de faux codes collés sur les bornes | septembre 2026 : 30 bornes de huit aires de services, environ 200 conducteurs débités, écho dans la presse | 3 : facile à provoquer, sans aucune compétence technique | 3 : des centaines de conducteurs, atteinte à la confiance ; le fonctionnement des bornes n'est pas touché | 9 |
| R4 – CIRCÉA devient indisponible et le réseau n'est plus ni supervisé ni ouvert à la plupart des paiements, sans mode dégradé ni restauration éprouvée | décembre 2026 : cinq heures, environ 2 500 sessions refusées, 600 appels | 2 : survenu une fois, pour une cause chez le fournisseur de cloud | 4 : tout le réseau, un samedi | 8 |

**Deux risques prioritaires** (a-3) : **R1 et R2** (criticité 12). Ils combinent une probabilité établie et un impact qui peut s'étendre à tout le réseau ; ils touchent l'**intégrité** de la commande des bornes, et pas seulement leur disponibilité ; ils viennent de l'absence de règles simples (vérifier l'origine et essayer une version, attribuer un compte par personne), donc ils peuvent être réduits vite et à faible coût. R4 arrive ensuite : son impact est maximal, mais il ne s'est produit qu'une fois.

*3.1 b) – L'outil de détection dans le traitement des risques et ses règles d'emploi*

**Caractérisation et place** (b-1) : l'outil relève de l'**apprentissage automatique** : il apprend sur des données (journaux de communication, sessions) un fonctionnement normal, puis signale les écarts ; c'est de la **détection d'anomalies**, et non de l'**IA générative**, qui produit des contenus (F13 § 1). Il se situe surtout dans la **détection** : il a signalé en dix minutes les redémarrages de novembre et repéré des bornes sur le point de tomber en panne. Il aide à **réagir** (prioriser les interventions, déclencher la maintenance avant la panne), mais il ne **prévient** rien : il ne remplace ni la vérification des micrologiciels, ni les comptes nominatifs, ni les sauvegardes, qui relèvent de la politique de sécurité (question 3.2).

**Ses limites, tirées de l'annexe 3.1 B** : 1 530 fausses alertes sur 1 800 (85 %), soit près de vingt alertes par jour, que les opérateurs ont cessé de lire : la vraie alerte de novembre n'a été lue que le lendemain ; des **données d'apprentissage** incomplètes : quatre mois seulement, sans aucun jour de grands départs pour l'aire coupée, mise en service en septembre (son affluence d'un samedi de départs a été prise pour une anomalie) et pas de journaux détaillés pour deux constructeurs, qui concentrent les trois quarts des fausses alertes ; des **angles morts** : ni les faux codes, ni l'hébergement ; un **risque propre** : la coupure automatique a privé une aire de services de ses 12 points pendant trois heures, contre l'objectif de disponibilité.

**Trois règles d'emploi** (b-2) :
1. **Décision humaine avant toute coupure ou tout redémarrage** (réponse à M. OLMAREC) : l'outil alerte et propose ; l'opérateur du centre de supervision, ouvert jour et nuit, décide et trace sa décision. La lenteur qu'invoque M. OLMAREC se traite par la règle 2 et par un délai de traitement des alertes graves, et non en retirant l'humain : une coupure à tort coûte plus cher qu'une alerte traitée en quelques minutes. Les opérateurs sont formés à l'outil, dans l'esprit de l'obligation de maîtrise de l'IA du règlement sur l'IA (annexe 3.5).
2. **Revue des faux positifs** : chaque alerte est qualifiée (confirmée ou fausse) par l'opérateur ; une revue hebdomadaire réunit l'équipe données et le centre de supervision pour corriger les seuils ; les alertes sont classées par gravité (commandes à distance inhabituelles et connexions en premier, état de santé des bornes ensuite).
3. **Qualité des données d'apprentissage** : apprendre sur au moins douze mois, vacances et jours de forte affluence compris ; obtenir des deux constructeurs l'accès aux journaux de leurs bornes, ou signaler que l'outil y est moins fiable ; réapprendre après chaque nouvelle version de micrologiciel ; documenter les données et chaque version de l'outil, validée par le centre de supervision avant usage.

**Indicateur rattaché à la règle 2** (b-3) :

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Taux d'alertes confirmées** | nombre d'alertes confirmées après examen / nombre d'alertes émises par l'outil × 100 | journal des alertes de l'outil et qualification saisie par les opérateurs du centre de supervision | hebdomadaire en 2027, puis mensuelle | au moins 50 % fin 2027, contre 15 % pendant l'essai (270 sur 1 800) | processus |

**Réponses tolérées**
- Analyse fondée sur ISO/IEC 27005:2022 (lignes directrices) plutôt que sur EBIOS RM, si la nature du référentiel est juste ; NIST CSF 2.0 (fonctions *Detect* et *Respond*) cité pour situer l'outil.
- Autres formulations des risques, ou risque propre à l'outil (coupure à tort) retenu parmi les quatre ; cotations voisines si elles sont justifiées par les échelles (impact de 2 pour R3, impact de 3 pour R1).
- R4 retenu comme prioritaire au titre de son impact sur tout le réseau et des sauvegardes jamais restaurées, si le choix est justifié.
- Autre indicateur complet : délai moyen entre l'émission d'une alerte grave et sa prise en charge (cible : moins de quinze minutes) ; nombre de coupures décidées à tort (cible 0).

**Erreurs fréquentes**
- *Norme, méthode et solution confondues* (`ET-01`, `JUR-S06`) — juste : EBIOS RM est une méthode, ISO/IEC 27005 des lignes directrices, ISO/IEC 27001 une norme d'exigences ; l'outil de détection est une solution.
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — juste : l'outil classe des comportements, il ne produit pas de contenu.
- *Typologie des risques récitée sans évaluation* (`JUR-T01`, `JUR-T07`) — juste : quatre événements redoutés, cotés selon les échelles de l'annexe, puis deux priorités.
- *Outil présenté comme la réponse à tous les risques, ou automatisation acceptée sans contrôle humain* (`ET-19`) — juste : faux positifs, données d'apprentissage, angles morts ; l'humain décide.
- *Classification de l'outil au titre du règlement sur l'IA* — non attendue (annexe 3.5).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| EBIOS Risk Manager, version 1.5 | méthode en cinq ateliers, écosystème | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| ISO/IEC 27005:2022 | lignes directrices de gestion des risques | `iso_27005_2022` ; F12 § 2 | en vigueur |
| ISO/IEC 27001:2022 | norme d'exigences | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | socle de sécurité : comptes, mises à jour, sauvegardes | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Règlement (UE) 2024/1689 sur l'IA, modifié par le règlement (UE) 2026/1744 | maîtrise de l'IA depuis le 02/02/2025, sans classification | `ai_act`, `omnibus_numerique_ia` ; F13 § 4 et § 5 | en vigueur ; application échelonnée |
| NIST CSF 2.0 (toléré) | six fonctions, dont *Detect* et *Respond* | `nist_csf_2_0` ; F12 § 2 | en vigueur |
| Apprentissage automatique, détection d'anomalies, limites | faux positifs, biais des données, explicabilité | F13 § 1 et § 3 | notion de cours |

---

### 3.2 – La politique de sécurité de CIRCÉA et des bornes (4 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique n'est pas exigée ; les normes se mobilisent sans entrer dans leur démarche de conformité formelle.

**Annexes mobilisées** : annexe 3.2 (constats, position des fonds, trois options), annexe 3.1 (incidents), annexe 3.5 (ISO/IEC 27001:2022, guide d'hygiène, règlement sur la cyberrésilience) et annexe 1.1 (organigramme, comité de surveillance, effectif, CIRCÉA, entreprises de maintenance).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Politique de sécurité fondée sur l'analyse des risques définie et distinguée de la charte ; objectifs hiérarchisés et périmètre de CIRCÉA et des bornes, prestataires compris | 0,5 |
| a-2 | Règles de sécurité du développement et d'inventaire des composants ; règles des mises à jour des micrologiciels (origine, essai, déploiement progressif, retour arrière) | 0,5 |
| a-3 | Règles des comptes des entreprises de maintenance ; règles de supervision et de sauvegarde | 0,5 |
| b-1 | Quatre mesures pour 2027, reliées aux risques et aux constats | 0,5 |
| b-2 | Hiérarchie argumentée et rang de la première justifié | 0,5 |
| c-1 | Option de positionnement choisie et justifiée, les deux autres écartées | 0,5 |
| c-2 | Rôles de la présidente, du comité de surveillance, du RSSI et de la direction technique | 0,5 |
| c-3 | Rôles du centre de supervision, des constructeurs (règlement sur la cyberrésilience, en principe) et des entreprises de maintenance | 0,5 |

**Réponse attendue**

*3.2 a) – La politique de sécurité de CIRCÉA et des bornes*

Une **politique de sécurité du système d'information** est le document approuvé par la direction qui fixe les objectifs de sécurité, le périmètre, les principes, l'organisation, les règles et le dispositif de contrôle ; elle est **fondée sur l'analyse des risques** quand ses règles découlent des risques identifiés et hiérarchisés (question 3.1) et qu'elle est revue quand ils changent (F12 § 1). Elle se distingue de la **charte informatique** de 2020, qui décline des règles d'usage pour les salariés et ne s'applique même pas aux techniciens des entreprises de maintenance (a-1).

**Objectifs**, hiérarchisés pour un opérateur de recharge : la **disponibilité** des points (au moins 98 % par point) et de CIRCÉA ; l'**intégrité** des commandes à distance, des micrologiciels et des tarifs, puisqu'un tiers qui commande les bornes peut arrêter le réseau ou fausser les prix ; la **confidentialité** des comptes des conducteurs et des données de paiement ; la **traçabilité** de toute commande, de toute modification de tarif et de toute mise en production.

**Périmètre** : CIRCÉA et son hébergement ; les quelque 3 600 bornes, leurs micrologiciels, leurs modems et la liaison mobile ; les terminaux de paiement ; l'application des conducteurs ; les logiciels en ligne de gestion des interventions et de relation clients ; toutes les personnes qui agissent sur le réseau, salariés et techniciens externes ; les fournisseurs (quatre constructeurs, sept entreprises de maintenance, fournisseur de cloud, opérateur mobile, prestataire de paiement).

**Règles des quatre domaines** :

| Domaine | Règles | Risque et constat traités |
|---|---|---|
| 1. Sécurité du développement de CIRCÉA et inventaire des composants (a-2) | exigences de sécurité intégrées à chaque évolution ; revue de sécurité avant mise en production, au moins pour les modules sensibles (commande à distance, tarifs, comptes), par une autre personne que l'auteur ; inventaire tenu à jour des environ 400 composants libres et de leurs versions ; veille sur les failles publiées et délai de correction fixé selon leur gravité ; formation des développeurs | deux versions par semaine sans revue ; composants non inventoriés |
| 2. Mises à jour des micrologiciels (a-2) | **origine vérifiée** : versions obtenues par un canal convenu avec chaque constructeur, authenticité contrôlée avant installation, jamais un fichier reçu par courriel ; **essai** sur quelques bornes de référence ; **déploiement progressif** par vagues (quelques bornes, puis une part du modèle, puis le reste), hors jours de forte affluence, avec un critère d'arrêt ; **retour arrière** prévu (version précédente conservée et réinstallable) ; validation du centre de supervision à chaque vague | R1 : 300 points bloqués deux jours |
| 3. Comptes des entreprises de maintenance (a-3) | un **compte nominatif** par technicien (environ 120), demandé par l'entreprise, approuvé par AMPÉRANE et fermé à son départ ; droits limités aux bornes de sa région et aux seules commandes utiles à l'intervention (ni tarifs, ni commandes en série) ; authentification à deux facteurs ; revue trimestrielle des comptes avec chaque entreprise ; engagement de sécurité annexé aux contrats (poste protégé, signalement des incidents, application de la charte) | R2 : compte partagé détourné |
| 4. Supervision et sauvegardes (a-3) | le centre de supervision suit aussi les **événements de sécurité** (connexions, commandes à distance en série, modifications de tarifs), avec l'outil de détection encadré (question 3.1 b) ; journaux conservés plusieurs mois et protégés contre la modification ; procédure de gestion des incidents et registre des incidents ; sauvegardes copiées hors de la région de la plateforme et **restaurées pour essai** chaque trimestre ; mode de fonctionnement dégradé écrit pour une indisponibilité de CIRCÉA | R4 ; journaux de sept jours ; aucune restauration ; aucun registre |

La politique est approuvée par la présidente, présentée au comité de surveillance avant la levée de 2028, déclinée en procédures et en une charte étendue aux techniciens externes, et revue chaque année. Elle s'appuie sur les mesures d'ISO/IEC 27001:2022 et sur le guide d'hygiène, sans viser autre chose qu'un niveau de sécurité adapté aux risques.

*3.2 b) – Quatre mesures hiérarchisées pour 2027*

1. **Remplacer les sept comptes partagés par des comptes nominatifs à droits limités** (deuxième trimestre 2027). **Justification du premier rang** : le risque R2 est actif aujourd'hui (le mot de passe d'un compte qui commande tout le réseau a été utilisé depuis un poste infecté, et aucun mot de passe n'a été changé) ; la mesure est rapide, peu coûteuse et dépend surtout d'une décision et de l'accord des sept entreprises.
2. **Appliquer la procédure de mise à jour des micrologiciels** (origine, essai, vagues, retour arrière) avant la prochaine version de chaque constructeur et avant le remplacement des composants des 1 200 bornes de 2019 (question 3.4).
3. **Nommer le RSSI et faire approuver la politique** par la présidente, puis la présenter au comité de surveillance au second semestre 2027, comme l'attendent les fonds.
4. **Rendre la plateforme supervisable et restaurable** : registre des incidents, suivi des événements de sécurité, journaux conservés plus longtemps, premier essai de restauration de CIRCÉA et mode dégradé écrit.

La sécurité du développement et l'inventaire des composants suivent, sous la conduite du RSSI.

*3.2 c) – Le positionnement de la fonction sécurité et les rôles*

**Choix : option 2, un RSSI rattaché à la présidente** (c-1). La direction technique développe, met en production et exploite CIRCÉA, et elle a la charge de la sécurité : elle serait juge et partie si le RSSI lui était rattaché (option 1), et il ne pourrait ni alerter ni arbitrer contre sa hiérarchie. Le RSSI doit agir sur toute l'entreprise (exploitation, service clients, entreprises de maintenance, constructeurs, équipe données) et rendre compte à la présidente et au comité de surveillance. L'option 3 seule ne suffit pas : deux jours par semaine, partagés entre plusieurs clients, pour un réseau de 3 600 bornes, 120 comptes externes et des alertes jour et nuit ; elle peut servir de **transition** pendant les six mois du recrutement, pour lancer l'analyse des risques et la mesure 1 dès avril 2027.

**Répartition des rôles** (c-2 et c-3) :

| Acteur | Rôle |
|---|---|
| Présidente (Mme SORBADIÈRE) | approuve la politique et les risques résiduels acceptés ; nomme le RSSI et lui donne les moyens ; arbitre les priorités ; décide en cas de crise ; rend compte au comité de surveillance |
| Comité de surveillance (avec les deux fonds) | donne son avis sur la politique et sur les investissements importants ; reçoit au moins deux fois par an un compte rendu (risques principaux, incidents, avancement des mesures) ; ne gère pas la sécurité |
| RSSI | conduit l'analyse des risques avec les directions ; rédige et pilote la politique ; fixe les règles et en contrôle l'application (revues des comptes, procédure des micrologiciels) ; coordonne le traitement des incidents et tient le registre ; sensibilise ; assure la veille (failles, règlement sur la cyberrésilience) ; donne son avis sur les clauses de sécurité des achats ; n'exploite rien lui-même |
| Direction technique (M. QUÉLAVEC) | met en œuvre : sécurité du développement, inventaire des composants, installation des micrologiciels, gestion technique des comptes, journaux, sauvegardes et restaurations ; l'équipe données conçoit l'outil de détection selon les règles de la question 3.1 b |
| Centre de supervision (direction de l'exploitation, Mme FOLCARIAS) | détecte et qualifie les alertes jour et nuit ; décide des coupures ; déclenche la procédure d'incident ; valide chaque vague de mise à jour ; fait contrôler l'état des bornes (faux codes) lors des passages des techniciens |
| Constructeurs | en principe, le règlement sur la cyberrésilience fait peser sur les **fabricants** de produits comportant des éléments numériques la sécurité dès la conception, la gestion des vulnérabilités et la fourniture de mises à jour de sécurité ; ils signalent depuis le 11/09/2026 les vulnérabilités activement exploitées et les incidents graves ; l'application générale est fixée au 11/12/2027 (annexe 3.5). AMPÉRANE en tire des exigences d'achat : versions authentifiées et documentées, information sur les failles, durée de fourniture des correctifs, accès aux journaux des bornes |
| Entreprises de maintenance | demandent et font fermer les comptes nominatifs de leurs techniciens ; protègent leurs postes ; respectent l'engagement de sécurité et la charte ; signalent sans délai tout incident ; participent aux revues trimestrielles |

**Réponses tolérées**
- Option 3 retenue comme transition, puis option 2 ; RSSI rattaché à la présidente avec un lien fonctionnel avec le directeur technique, si son indépendance est préservée.
- Mise à jour des micrologiciels placée au premier rang, au titre de l'impact d'une version piégée sur tout un modèle, si la mesure sur les comptes suit immédiatement.
- Autres règles pertinentes dans chaque domaine (sensibilisation des techniciens externes, contrôle des bornes contre les faux codes, chiffrement des échanges), si elles restent au niveau de la politique ; rôles complémentaires du fournisseur de cloud, du prestataire de paiement ou du délégué à la protection des données.
- Objectifs présentés par les critères de confidentialité, d'intégrité, de disponibilité et de traçabilité, si leur ordre est justifié par le cas.

**Erreurs fréquentes**
- *Politique de sécurité confondue avec la charte informatique* (`ET-27`) — juste : la politique fixe objectifs, périmètre, règles et responsabilités ; la charte décline les règles d'usage.
- *RSSI présenté comme un technicien ou laissé sous la direction technique* (`ET-15`) — juste : pilote de la politique, indépendant de ceux qui développent et exploitent.
- *Règles techniques détaillées, réglages d'équipements ou tests techniques de sécurité* (`JUR-T12`, limite du programme 4.2) — juste : règles organisationnelles et de gestion.
- *Règlement sur la cyberrésilience appliqué à AMPÉRANE comme à un fabricant, ou daté faux* (F12 § 7 et § 10) — juste : il vise les fabricants ; signalement depuis le 11/09/2026, application générale le 11/12/2027 ; AMPÉRANE l'utilise comme levier d'achat.
- *Sécurité confiée à la seule direction technique* (`JUR-T11`) — juste : présidente, comité de surveillance, RSSI, exploitation, fournisseurs.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 27001:2022 | 93 mesures : contrôle d'accès, sécurité du développement, vulnérabilités, journalisation, sauvegarde, fournisseurs | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Guide d'hygiène informatique (ANSSI, 2017) | 42 mesures : comptes, mises à jour, sauvegardes, journalisation | `guide_hygiene_anssi_2017` ; F12 § 2 | en vigueur |
| Règlement (UE) 2024/2847 sur la cyberrésilience (CRA) | obligations des fabricants ; signalement depuis le 11/09/2026 ; application le 11/12/2027 | `cra` ; F12 § 5 et § 7 | applicable le 11/12/2027 ; article 14 depuis le 11/09/2026 |
| Politique de sécurité, charte, rôles, RSSI | définitions et positionnement | F12 § 1 | notion de cours |

---

### 3.3 – L'audit de la tarification variable (2,5 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.e` « Facteurs de succès et points de vigilance spécifiques à l'audit SI ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; la conformité financière et comptable n'est pas traitée.

**Annexes mobilisées** : annexe 3.3 (pilote, constats, réclamations, demande de la présidente, position de M. OLMAREC), annexe 3.5 (COBIT 2019, ISO/IEC 27001:2022) et annexe 1.1 (CIRCÉA, chiffre d'affaires, organigramme sans audit interne).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit du SI défini ; objectifs (exactitude des prix, maîtrise du programme, atteinte des objectifs, décision de juin) et périmètre (chaîne du calcul à la facturation, 600 points, période) | 0,5 |
| a-2 | Étapes de l'audit et preuves à demander : documentation des règles, journal des modifications, rapprochement des prix affichés et facturés | 0,5 |
| a-3 | Quatre critères de performance et de conformité, appliqués aux constats | 0,5 |
| b-1 | Deux facteurs de succès propres à l'audit d'un programme, reliés à l'annexe | 0,5 |
| b-2 | Deux points de vigilance propres à l'audit d'un programme, reliés à l'annexe | 0,5 |

**Réponse attendue**

*3.3 a) – Le cadrage de l'audit et les critères*

L'**audit du système d'information** est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel, la performance, la sécurité, la conformité et la gouvernance d'un système, et formule des recommandations (F10 § 1.1). Il s'agit ici d'un audit externe contractuel, commandé par la présidente, d'un programme développé en interne qui calcule des prix (a-1).

**Objectifs** : vérifier que les prix calculés, affichés et facturés sont **exacts** et conformes aux règles voulues par la direction ; apprécier la **maîtrise** du programme (documentation, gestion des modifications, séparation des tâches, traçabilité) ; apprécier s'il atteint ses objectifs (étaler l'affluence, recettes) et repérer ses effets non voulus (sites ruraux) ; **éclairer la décision de juin 2027** sur la généralisation et ses conditions.

**Périmètre** : le module de tarification variable de CIRCÉA, ses règles et ses données d'entrée (heure, occupation) ; la chaîne complète, du calcul toutes les quinze minutes à l'affichage dans l'application et sur l'écran des bornes rapides, puis à l'enregistrement et à la facturation de la session ; les 600 points des 150 sites du pilote, d'octobre 2026 à avril 2027 ; le processus de modification du programme ; le traitement des réclamations. La sécurité générale et l'hébergement de CIRCÉA en sont exclus (question 3.2).

**Étapes et preuves** (a-2) :
1. **Cadrage** : lettre de mission signée par la présidente (objectifs, périmètre, référentiel, accès garantis, confidentialité, 20 jours en avril et mai, rapport début juin). Préalable : faire écrire et approuver les règles tarifaires (plancher, plafond, poids de l'occupation, jours fériés), qui serviront de référentiel ; COBIT 2019 (gestion des changements) et les mesures d'ISO/IEC 27001:2022 (sécurité du développement, journalisation) en appui.
2. **Prise de connaissance** : entretiens avec l'équipe données, la direction technique et le service clients ; schéma de la chaîne de calcul et des données.
3. **Analyse des risques** : erreur de calcul, écart entre affichage et facturation, modification non autorisée ou non essayée, effet inéquitable selon les sites.
4. **Collecte et examen**, avec les preuves à demander : la **documentation des règles** (aujourd'hui inexistante) et sa comparaison avec le programme ; le **journal des modifications** : les 15 mises en production, avec leur demande, leur description, leur auteur, leur essai et leur validation, rapprochées de l'historique des versions du programme ; le **rapprochement exhaustif** des prix affichés (journaux de l'application et des bornes) et des prix facturés pour les environ 75 000 sessions payées par l'application ou par carte bancaire, pour expliquer les environ 3 000 écarts (4 % de ces sessions, quatre sur cinq au détriment du conducteur) ; le recalcul d'un échantillon de prix ; les 900 réclamations et leurs réponses ; les prix par type de site.
5. **Restitution contradictoire** avec l'équipe données et la direction technique, puis **rapport** à la présidente début juin : constats, risques, recommandations hiérarchisées et conditions à la généralisation.
6. **Suivi** des recommandations avant septembre 2027.

**Quatre critères de performance et de conformité** (a-3) :

| Critère | Ce qu'il vérifie | Constat de l'annexe 3.3 |
|---|---|---|
| **Fiabilité** (exactitude) | le prix facturé est égal au prix affiché au début de la session, pour toutes les sessions | environ 3 000 écarts, 4 % de ces sessions, écart moyen d'environ 2 € |
| **Conformité aux règles approuvées** | chaque prix calculé respecte les règles écrites et validées (plancher, plafond, amplitude, jours fériés), et le programme fait ce que dit la documentation | règles écrites seulement dans le programme, connues de deux personnes |
| **Sécurité et traçabilité des modifications** (intégrité) | toute modification est demandée, décrite, essayée et validée par une autre personne que son auteur avant sa mise en production ; les données d'entrée et la version utilisées pour chaque prix sont conservées | 10 modifications sur 15, soit deux tiers, sans aucune trace ; mises en production par l'équipe données elle-même ; données d'occupation non conservées |
| **Efficacité** | le programme atteint son objectif (déplacer une partie des sessions vers les heures creuses, mieux répartir l'occupation, recettes) sans dégrader la relation avec les conducteurs | 900 réclamations sur 2 000, soit 45 % des réclamations sur les prix pour 7,5 % des points |

*3.3 b) – Facteurs de succès et points de vigilance*

**Deux facteurs de succès** (b-1) :
1. **L'accès au programme, aux données d'entrée et aux journaux**, garanti par la lettre de mission de la présidente. M. OLMAREC veut limiter l'auditeur aux résultats : or, sans lire le programme, on ne peut pas vérifier qu'il applique les règles, ni expliquer les écarts ; la confidentialité du savoir-faire se protège par un engagement de l'auditeur, et non par un refus d'accès.
2. **Des compétences pluridisciplinaires** : un auditeur des systèmes d'information capable de lire le programme et d'exploiter des données en grand nombre (125 000 sessions), et qui comprend le métier de la recharge et les objectifs d'« AMPÉRANE 2030 ».

**Deux points de vigilance** (b-2) :
1. **L'indépendance vis-à-vis de l'équipe données** : elle conçoit le programme, le modifie, le met en production elle-même, et veut fournir seule les extractions ; l'auditeur doit obtenir les données directement (accès en lecture) ou par la direction technique hors de l'équipe données, et rendre compte à la seule présidente.
2. **La reproductibilité des prix** : les données d'occupation qui ont servi au calcul ne sont pas conservées et dix versions du programme ne sont pas tracées ; on ne peut donc pas recalculer un prix passé ni prouver qu'il était juste. Il faut conserver dès maintenant, pour chaque quart d'heure et chaque point, les données d'entrée, la version du programme et le prix calculé, et faire porter les recalculs sur la période où ces traces existent.

**Réponses tolérées**
- Démarche en cinq à sept étapes (cadrage, prise de connaissance, analyse des risques, programme de travail, collecte, restitution, suivi), si elle est appliquée au programme de tarification.
- Critère d'équité (écarts de prix entre types de sites expliqués par les règles approuvées) à la place de l'efficacité, si l'efficacité est évoquée ailleurs ; critère de sécurité limité aux droits sur le programme et à la séparation des tâches.
- Autres facteurs de succès : soutien affiché de la présidente, calendrier compatible avec la décision de juin, adhésion de l'équipe données ; autres points de vigilance : explicabilité des règles, dépendance à deux personnes, périmètre réaliste en 20 jours.
- Mention de la conformité au RGPD comme critère secondaire, si elle est reliée au cas (les prix dépendent de l'heure et de l'occupation, et non de la personne).

**Erreurs fréquentes**
- *Méthodologie incomplète* (`JUR-A01`) — juste : objectifs, périmètre, référentiel, étapes, livrables et calendrier.
- *Audit du SI confondu avec l'audit légal* (`ET-34`) — juste : audit contractuel d'un programme et de sa gouvernance, commandé par la présidente.
- *Critères génériques sans lien avec les constats* (`JUR-T01`, `JUR-T08`) — juste : chaque critère est appliqué aux chiffres de l'annexe 3.3.
- *Audit limité aux résultats, comme le propose M. OLMAREC* — juste : il faut le programme, les données d'entrée et les modifications.
- *Analyse juridique des prix ou des réclamations* — non attendue.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Démarche d'audit du SI | cadrage, prise de connaissance, risques, collecte, restitution, suivi ; facteurs de succès | F10 § 1.1 et § 1.2 | notion de cours |
| COBIT 2019 | gestion des changements | `cobit_2019` ; F10 § 2 | en vigueur |
| ISO/IEC 27001:2022 | sécurité du développement, journalisation | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Séparation des tâches, piste d'audit | développement et mise en production distincts ; traçabilité | F10 § 3.1 et § 3.2 | notion de cours |

---

### 3.4 – Une recharge plus responsable (3,5 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.c` « Gouvernance SI orientée RSE : inclusion, éthique, sobriété » ; `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ». Limites : la durabilité est intégrée à la gouvernance globale du SI et non traitée comme un ajout marginal ; aucun calcul d'empreinte n'est attendu.

**Annexes mobilisées** : annexe 3.4 (recharge sans application, équipements), annexe 3.3 (prix des sites ruraux, réclamation du maire), annexe 3.5 (RGESN, règlement sur la cyberrésilience) et annexe 1.1 (5 600 points normaux, paiement par carte bancaire sur les seules bornes rapides, 650 000 conducteurs dont 120 000 utilisateurs actifs de l'application, objectif « accessible à tous »).

**Barème indicatif (3,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Gouvernance du SI orientée vers la responsabilité sociétale définie et appliquée à AMPÉRANE (principes écrits, porteurs, critères dans les décisions) | 0,5 |
| a-2 | Principe d'équité de la tarification variable, sa traduction (sites ruraux à borne unique) et son porteur | 0,5 |
| a-3 | Principe d'inclusion, sa traduction (recharge et prix sans application, accessibilité) et son porteur | 0,5 |
| b-1 | Allongement de la durée de vie et réparation | 0,5 |
| b-2 | Choix argumenté entre les deux options pour les 1 200 bornes de 2019 | 0,5 |
| b-3 | Sobriété des écrans et fin de vie des équipements déposés | 0,5 |
| b-4 | Classement par priorité justifié | 0,5 |

**Réponse attendue**

*3.4 a) – Une gouvernance du SI orientée vers la responsabilité sociétale*

Une **gouvernance du système d'information orientée vers la responsabilité sociétale** intègre, dans les décisions sur le système d'information (conception de l'application et des algorithmes, achats d'équipements, règles d'exploitation), des critères **sociaux** (inclusion, accessibilité, équité, éthique) et **environnementaux** (sobriété, durée de vie), au même titre que le coût et le risque : principes écrits, porteurs désignés, critères d'acceptation des projets et revue périodique (F14 § 0 et § 3). Pour AMPÉRANE, elle traduit l'objectif d'« AMPÉRANE 2030 » de rendre la recharge accessible à tous : la présidente adopte une charte du numérique responsable qui énonce les principes, et chaque principe a un porteur et un contrôle (a-1).

**Principe 1 – Équité de la tarification variable** (a-2) : « le prix variable rémunère l'affluence là où le conducteur peut choisir ; il ne pénalise pas celui qui n'a pas d'autre choix ». Traduction : sur les 60 sites ruraux qui n'ont qu'une borne rapide, le kilowattheure revient en moyenne à 0,65 € contre 0,52 € sur les sites urbains (25 % de plus), parce que la seule borne est souvent occupée ; il faut donc neutraliser l'effet de l'occupation sur ces sites, ou y plafonner le prix (par exemple au prix moyen du réseau) ; fixer pour tout le réseau des règles écrites (plancher, plafond, amplitude) ; garantir que le prix affiché au début de la session est celui qui est facturé ; expliquer simplement les règles dans l'application. **Porteurs** : la présidente arbitre entre recettes et équité et approuve les règles ; l'équipe données (M. OLMAREC) les traduit dans le programme ; une revue trimestrielle des prix par type de site, avec le service clients et la direction du développement du réseau (sites hôtes, élus), en contrôle l'application.

**Principe 2 – Inclusion des conducteurs** (a-3) : « tout conducteur peut recharger, connaître le prix et bénéficier des prix réduits sans application, et l'application est utilisable par tous ». Traduction : les 5 600 points normaux, soit 70 % des points, n'acceptent que l'application ou une carte d'opérateur de mobilité, alors que plus de huit conducteurs sur dix (environ 530 000 sur 650 000) n'utilisent pas activement l'application ; il faut proposer un badge AMPÉRANE sans téléphone, qui donne accès au tarif réduit des heures creuses, une réservation et une information sur le prix par téléphone ou sur la borne, et un parcours d'assistance plus court que les huit minutes d'appel actuelles ; pour l'application, l'évaluer au regard des règles d'accessibilité numérique, corriger les défauts relevés par les 300 réclamations (agrandissement des caractères, contrastes, taille des boutons, compatibilité avec les lecteurs d'écran), l'essayer avec des conducteurs âgés et malvoyants avant chaque version, et la rendre utilisable sur des téléphones anciens, comme le recommande le RGESN. **Porteurs** : le responsable produit de l'application (direction technique) pour l'accessibilité ; le service clients (M. TÉVENARD), qui porte la voix des conducteurs et suit les appels et les réclamations ; la présidente arbitre les moyens.

*3.4 b) – Quatre bonnes pratiques de Green IT sur le cycle de vie des équipements, par priorité*

1. **Choisir l'option 2 pour les 1 200 bornes de 2019 : remplacer le modem et la carte électronique** (b-2). Leur structure, leurs câbles et leurs connecteurs sont en bon état : remplacer les bornes entières jetterait des équipements qui fonctionnent et ferait fabriquer 1 200 bornes neuves, alors que, pour un équipement électronique, la fabrication pèse souvent davantage dans l'empreinte que sa propre consommation d'électricité (F14 § 1). Le remplacement des composants prolonge la vie des bornes d'au moins cinq ans, coûte environ 2 400 k€ contre environ 12 000 k€ (cinq fois moins) et demande une demi-journée par borne au lieu de douze mois de travaux sur les sites. Conditions : essai sur quelques bornes, installation selon la procédure des micrologiciels (question 3.2), récupération des anciens composants (pratique 4). **Rang 1** : c'est la décision au plus fort volume (un tiers des 3 600 bornes), avec une échéance ferme (fin 2028).
2. **Allonger la durée de vie et réparer** (b-1) : remplacer les 1 200 terminaux de paiement selon leur état et non par série tous les quatre ans (300 en 2026) ; réparer les cartes électroniques et réemployer les pièces en état ; s'appuyer sur l'outil de détection pour intervenir avant la panne ; exiger dans les achats de bornes la disponibilité des pièces et la fourniture des mises à jour pendant toute leur durée de vie, ce que le règlement sur la cyberrésilience rend plus facile à obtenir des fabricants pour la sécurité (annexe 3.5). **Rang 2** : politique durable qui touche tout le parc.
3. **Organiser la fin de vie des équipements déposés** (b-3) : enregistrer chaque équipement déposé dans le logiciel de gestion des interventions (référence, borne, état), le rapporter à un point de collecte, le trier (réparation, réemploi comme pièce, reconditionnement, recyclage par une filière agréée des déchets d'équipements électriques et électroniques, avec justificatif) ; l'imposer aux entreprises de maintenance et au prestataire de paiement. **Rang 3** : rapide et peu coûteux, il conditionne les pratiques 1 et 2, puisqu'on ne réemploie que ce que l'on retrouve (4 000 équipements déposés en 2026 sans inventaire).
4. **Sobriété des écrans** (b-3) : se demander d'abord si un écran allumé jour et nuit est utile : l'éteindre ou le mettre en veille sur les sites fermés la nuit (environ la moitié), le rallumer à l'approche ou au branchement, réduire la luminosité selon l'heure, et l'exiger dans les prochains achats. **Rang 4** : gain d'électricité réel (l'écran représente environ la moitié de la consommation d'une borne au repos), immédiat et sans coût, mais il porte sur l'usage, alors que les trois premières pratiques évitent de fabriquer des équipements.

**Réponses tolérées**
- Autre porteur du principe d'équité (directeur(rice) de cabinet, comité du numérique responsable) ou de l'inclusion (direction de l'exploitation pour les bornes), si le partage entre décision, mise en œuvre et contrôle est clair.
- Autres traductions de l'équité (prix unique sur les sites à borne unique, information préalable des élus) ou de l'inclusion (paiement sur les bornes normales lors de leur renouvellement), si elles répondent aux constats.
- Sobriété des écrans placée au premier rang comme mesure immédiate et gratuite, si le classement est justifié par un critère explicite et si l'enjeu de la fabrication est reconnu.
- Option 1 retenue pour une partie des bornes si une hypothèse explicite le justifie (borne endommagée, besoin de puissance supérieure), l'option 2 restant la règle.

**Erreurs fréquentes**
- *Sobriété réduite à l'économie d'énergie* (`ET-12`) — juste : questionner le besoin (écrans allumés pour personne) et allonger la durée de vie avant d'économiser l'électricité.
- *Option 1 choisie parce qu'elle est « plus moderne »* (`ET-38`) — juste : fabriquer des bornes neuves pèse souvent plus que leur propre consommation ; l'option 2 prolonge des bornes en bon état.
- *Durabilité traitée comme un ajout marginal, sans porteur* (limite du programme 4.3) — juste : principes intégrés aux décisions, chacun porté par un responsable.
- *Inclusion réduite à l'application* (`JUR-T08`) — juste : l'annexe 1.1 montre que 70 % des points exigent l'application ou une carte d'opérateur.
- *Calcul d'empreinte tenté* — non attendu.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Gouvernance du SI orientée vers la responsabilité sociétale | inclusion, accessibilité, éthique, sobriété | F14 § 0 et § 3 | notion de cours |
| RGESN, version 2024 | services utilisables sur des équipements anciens | `rgesn_2024` ; F14 § 2 | en vigueur |
| Green IT, durée de vie, réemploi, fin de vie | allongement de la durée de vie, réparation, reconditionnement, déchets électroniques | F14 § 1 et § 3 | notion de cours |
| Règlement (UE) 2024/2847 sur la cyberrésilience (CRA) | mises à jour de sécurité fournies par les fabricants | `cra` ; F12 § 7 | applicable le 11/12/2027 ; article 14 depuis le 11/09/2026 |
