# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 21 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F12 sécurité et résilience, F10 audit et fiabilisation, F14 numérique responsable, fiche commune CSRD, ESRS et Omnibus, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Risques des jours de match | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ; `4.1.d` Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. | 3 |
| 3.2 Gouvernance et résilience des systèmes du stade | `4.2.a` Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques ; `4.2.c` Notions d'architecture de confiance (authentification, chiffrement, segmentation) ; `4.2.d` Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ; `4.2.e` Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques | 2,5 |
| 3.3 Diagnostic d'audit | `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ; `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance | 2,5 |
| 3.4 Empreinte du stade connecté et demande du partenaire | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.b` Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) ; `4.3.d` Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI | 5 |
| **Dossier 3 – Maîtriser les risques des jours de match et l'empreinte du stade connecté** |  | **13** |

Répartition indicative : connaissances (typologie des risques, analyse d'impact sur l'activité, système critique, articulation avec le plan de continuité, audit et contrôle, Green IT et sobriété, outils de mesure, norme volontaire) 2,25 points environ (items 3.1 a pour moitié, b-1 pour moitié, 3.2 a-1 pour moitié, c-1 pour un quart, 3.3 b pour moitié, 3.4 a-1, a-3 pour moitié, c-2 pour un quart) ; analyse des annexes et recommandations 10,75 points, soit environ 83 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Risques des jours de match (3 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers » ; `4.1.d` « Référentiels et cadres réglementaires : RGPD, NEP, ISO 27001, etc. ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; la quantification des incidences sur les comptes relève de l'UE 4.

**Annexes mobilisées** : annexes 3.1 (déroulé, acteurs, réseaux), 3.2 (incidents A et B, repère RGPD) et 1.1 (chiffres clés) ; l'annexe 3.3 peut être utilisée en appui.

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Cybermenaces et défaillances opérationnelles brièvement définies, deux risques précis par catégorie tirés des annexes | 0,5 |
| a-2 | Risques réglementaires et risques métiers brièvement définis, deux risques précis tirés des annexes | 0,5 |
| b-1 | Analyse d'impact sur l'activité définie ; impacts de l'incident A sur au moins trois processus du jour de match | 0,5 |
| b-2 | Continuité du service aux spectateurs (absence de mode dégradé, dépendance au prestataire) et postes des états financiers exposés, sans chiffrage au-delà des montants de l'annexe | 0,5 |
| c-1 | Trois risques prioritaires retenus et justifiés par leur probabilité et leur impact | 0,5 |
| c-2 | Pour chacun, une option de traitement, une mesure précise et un référentiel ou une méthode adaptés ; 0,5 dès deux risques complets | 0,5 |

**Réponse attendue**

*3.1 a) – Typologie et six risques d'un jour de match*

Les risques liés au SI se répartissent en trois catégories (F12 § 0) : les **cybermenaces** (actions malveillantes visant la confidentialité, l'intégrité ou la disponibilité de l'information), les **défaillances opérationnelles** (pannes, erreurs, dépendances, absence de procédure, sans intention de nuire) et les **risques réglementaires et métiers** (manquement à une obligation légale ou contractuelle ; atteinte aux activités, aux recettes et à l'image de l'organisation).

| Catégorie | Risques d'un jour de match (annexes 3.1 et 3.2) |
|---|---|
| Cybermenaces | (1) **fraude aux billets dématérialisés** : copie et revente de billets diffusés hors de tout contrôle (incident B : 400 billets copiés, 1 100 présentations, 550 acheteurs refoulés, annonce reprenant le logo du club) ; (2) **intrusion par une interconnexion** : depuis le réseau du public vers les terminaux de paiement de la tribune Est, par l'accès à distance permanent de PORTALVÈNE Accès (attaque par un prestataire) ou par le poste de supervision relié au réseau administratif et au réseau des systèmes du stade |
| Défaillances opérationnelles | (3) **panne du contrôle d'accès** à l'ouverture des portes, provoquée par une mise à jour non maîtrisée du prestataire (incident A : 35 minutes, 80 lecteurs arrêtés) ; (4) **absence de mode dégradé et dépendance au prestataire** : aucune consigne écrite, liste des billets sur le seul serveur local, astreinte fermée pendant les matchs ; variante : défaillance de l'écran géant ou de la sonorisation qui portent les consignes de sécurité, ou de la messagerie grand public qui relie les 400 intervenants |
| Risques réglementaires et métiers | (5) **réglementaire** : violation de données personnelles (noms et adresses électroniques de 400 invités accessibles en ligne) sans décision de notification, alors que le délai de 72 heures, qui courait depuis la découverte du 16 janvier 2027, est dépassé depuis près de cinq mois (repère de l'annexe 3.2) ; (6) **métier** : atteinte à la sécurité et à l'accueil du public (2 000 spectateurs entrés sans contrôle, nombre d'entrées par tribune inconnu), perte de recettes et de confiance des spectateurs et des partenaires (avoirs, 1 200 réclamations, 200 invités de loge en retard, renouvellement des partenariats) |

(0,5 pt pour les deux premières catégories, 0,5 pt pour la troisième.)

*3.1 b) – Analyse d'impact de l'incident A*

L'**analyse d'impact sur l'activité** (*business impact analysis*) recense les processus critiques, mesure les effets d'une interruption dans le temps (sécurité des personnes, recettes, image, obligations), identifie leurs dépendances (systèmes, données, prestataires, personnes) et en déduit la durée d'interruption tolérable, qui fonde les dispositifs de continuité (F12 § 4). Un jour de match, la tolérance se compte en minutes : les spectateurs arrivent en deux heures et le coup d'envoi est fixé (0,5 pt avec les processus).

Impacts sur les processus :
- **entrée du public** : arrêt total des 80 lecteurs pendant 35 minutes, files de 45 minutes, 3 000 spectateurs, près d'un sur cinq, entrés après le coup d'envoi ;
- **sécurité et comptage du public** : 2 000 entrées sans lecture, jauge par tribune inconnue pour ce match, décision prise oralement, sans règle préétablie ;
- **hospitalités et partenariats** : 200 invités de loge en retard, gestes attendus par les partenaires (11 M€ de partenariats et 4 M€ d'hospitalités en jeu à terme) ;
- **restauration** : ventes d'avant-match perdues ;
- **billetterie et relation avec les supporters** : 1 200 réclamations en trois semaines, 2 000 messages critiques ;
- **information de gestion** : passages non enregistrés, statistiques de fréquentation du match faussées.

Continuité et états financiers (0,5 pt) :
- **Continuité** : le service a été rétabli par chance (un ingénieur joint sur son téléphone personnel) ; il n'existait ni procédure dégradée, ni copie de la liste des billets hors du serveur, ni engagement de délai de rétablissement : le club dépend entièrement d'un prestataire indisponible aux heures des matchs.
- **États financiers**, postes exposés : chiffre d'affaires de la billetterie, diminué des avoirs (45 000 €), et dette envers les spectateurs tant que ces avoirs ne sont pas utilisés ; autres produits (redevance des buvettes, − 10 000 €) ; charges externes (heures supplémentaires des prestataires, 5 000 €) ; aucun recours chiffrable contre PORTALVÈNE Accès faute de pénalité au contrat ; risque de réclamations des partenaires sur leurs contrats. Les 60 000 € représentent 1 % des recettes annuelles de billetterie et d'abonnements (6 M€ en 2025-2026) et environ 0,2 % du chiffre d'affaires, mais l'impact d'image et la répétition du risque pèsent davantage ; l'évaluation des incidences sur les comptes relève de l'UE 4.

*3.1 c) – Trois risques prioritaires et leur traitement*

Échelle retenue (hypothèse à écrire) : probabilité faible, moyenne ou forte ; impact limité, important ou critique.

| Risque prioritaire | Probabilité et impact | Option de traitement | Mesure | Référentiel ou méthode |
|---|---|---|---|---|
| R3-R4 – Panne du contrôle d'accès sans mode dégradé | **forte** (déjà survenue ; mises à jour à distance sans prévenir ; astreinte fermée) × **critique** (16 000 spectateurs, sécurité, recettes, image) | **réduire** le risque et en **partager** une part avec le prestataire | avenant au contrat : gel des mises à jour dans les 48 heures qui précèdent un match, technicien présent ou astreinte joignable chaque jour de match, délai de rétablissement de 15 minutes assorti de pénalités ; procédure dégradée avec liste des billets exportée sur des lecteurs autonomes | analyse d'impact et continuité selon ISO 22301:2019 ; relations avec les fournisseurs parmi les mesures de l'annexe A d'ISO/IEC 27001:2022 |
| R1 – Fraude aux billets dématérialisés | **forte** (fichiers envoyés à chaque match ; incident déjà survenu) × **important** (700 refus, invités refoulés, image, données d'invités diffusées) | **réduire** | billets d'invitation nominatifs, délivrés dans l'espace en ligne de la billetterie plutôt qu'en fichier ; alerte en cas de double présentation ; consignes de diffusion données aux partenaires ; procédure de traitement des violations de données (décision de notification sous 72 heures) | EBIOS Risk Manager (version 1.5), dont les scénarios stratégiques intègrent l'écosystème (partenaires, prestataires) ; RGPD pour la notification |
| R2 – Intrusion par une interconnexion entre réseaux | **moyenne** (aucune attaque constatée, mais trois interconnexions non maîtrisées) × **critique** (systèmes de sécurité du stade, données de paiement, propagation au réseau administratif) | **réduire** ; **éviter** le raccordement des terminaux au réseau du public | séparation des trois réseaux (question 3.2 b) ; accès à distance des prestataires ouvert sur demande, nominatif et tracé ; comptes partagés remplacés par des comptes nominatifs | appréciation des risques selon ISO/IEC 27005:2022 ; mesures de l'annexe A d'ISO/IEC 27001:2022 |

(0,5 pt pour trois risques justifiés par la probabilité et l'impact ; 0,5 pt pour les traitements, dès deux complets.)

Le risque réglementaire R5 appelle une décision immédiate, indépendante de la cotation : examen de la violation avec le partenaire, décision de notifier ou non, consignée.

**Réponses tolérées**
- Autres risques pertinents : défaillance du réseau sans fil ou de la plateforme de paiement (buvettes à l'arrêt), hameçonnage des supporters par de faux sites de billetterie, consignes de sécurité diffusées à 120 anciens intervenants, comptes partagés du logiciel de contrôle d'accès (annexe 3.3).
- Classement d'un même fait dans deux catégories (la fuite de la liste est à la fois une cybermenace et un risque réglementaire), s'il est justifié.
- Cotation numérique (1 à 4) ou matrice de criticité, si l'échelle est annoncée.
- Option « transférer » par une cyberassurance pour le risque résiduel, présentée comme complément et non comme substitut aux mesures.
- Méthode MEHARI ou NIST CSF 2.0 citée à la place d'EBIOS RM ou d'ISO/IEC 27005, si elle est située (méthode d'analyse, cadre).

**Erreurs fréquentes**
- *Typologie récitée sans faits du cas* (`JUR-T01`, `ET-39`) — liste générique de menaces ; juste : chaque risque est formulé comme un événement du jour de match, chiffré par les annexes.
- *Impact réduit au coût de l'incident, ou dérive vers le traitement comptable* (périmètre 4.1, F10 § 0) — juste : processus, continuité, postes exposés, sans écriture ni provision.
- *Norme, méthode et solution confondues* (`ET-01`, `JUR-S06`) — « installer ISO 27001 », « acheter EBIOS » ; juste : ISO/IEC 27001:2022 est une norme d'exigences, EBIOS RM une méthode d'appréciation des risques, ISO/IEC 27005:2022 des lignes directrices.
- *Mesures techniques détaillées* (`JUR-T12`) — réglages des lecteurs ou des équipements de réseau ; juste : mesures organisationnelles et contractuelles, principes d'architecture.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI ; analyse d'impact sur l'activité | catégories de risques ; BIA | F12 § 0, 4 et 5 | notion de cours |
| ISO/IEC 27001:2022 ; ISO/IEC 27005:2022 | norme d'exigences et mesures de l'annexe A ; gestion des risques | `iso_27001_2022`, `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager (ANSSI, version 1.5) | méthode d'appréciation des risques, écosystème | `ebios_rm_1_5` ; F12 § 2 | en vigueur |
| ISO 22301:2019 | management de la continuité d'activité | `iso_22301_2019` ; F12 § 4 | en vigueur |
| RGPD | notification d'une violation dans les 72 heures | `rgpd` ; F12 § 5 | applicable depuis le 25/05/2018 |

---

### 3.2 – Gouvernance et résilience des systèmes du stade (2,5 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.a` « Définir et piloter une politique de sécurité du SI, en intégrant les enjeux de cybersécurité, de résilience organisationnelle et de gouvernance des systèmes critiques » ; `4.2.c` « Notions d'architecture de confiance (authentification, chiffrement, segmentation) » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) » (ici le seul positionnement dans le plan de continuité ; IAM non traitée) ; `4.2.e` « Rôles et responsabilités des acteurs dans la gouvernance des systèmes critiques ». Limites : la mise en œuvre technique des solutions n'est pas exigée ; le lien avec les normes peut être fait sans entrer dans les certifications.

**Annexes mobilisées** : annexes 3.1 (acteurs, réseaux, interconnexions), 3.3 (constats) et 1.1 (organigramme).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Système critique défini et appliqué (systèmes du stade concernés) ; rôles et responsabilités des cinq acteurs | 0,5 |
| a-2 | Document et instance qui formalisent ces responsabilités, avec leur contenu et leur fréquence | 0,5 |
| b | Trois principes de séparation des réseaux, reliés aux constats, sans détail technique ; 0,5 dès trois principes reliés | 0,5 |
| c-1 | Procédure dégradée d'entrée du public (déclenchement, décideur, moyens, retour à la normale), située dans le plan de continuité et distinguée de la reprise | 0,5 |
| c-2 | Exercice de crise : scénario, participants, fréquence, retour d'expérience | 0,5 |

**Réponse attendue**

*3.2 a) – Système critique et responsabilités*

Un **système critique** est un système dont l'indisponibilité, l'altération ou la compromission met en cause la sécurité des personnes ou la poursuite d'une activité essentielle, et dont la gouvernance doit donc désigner sans ambiguïté qui décide, qui exploite et qui contrôle. Au stade, sont critiques le **contrôle d'accès** (entrée et comptage du public), la **sonorisation** et l'**écran géant** (consignes de sécurité), l'**éclairage** et, à un degré moindre, le **paiement des buvettes** (0,5 pt avec les rôles).

| Acteur | Responsabilités |
|---|---|
| Direction générale du club (Mme LAFERRADE) | responsable en dernier ressort : fixe le niveau de risque accepté, approuve la politique de sécurité des systèmes du stade et l'avenant à la convention, arbitre les moyens, préside le comité ; rend compte au conseil d'administration (priorité du plan « MONTALBRET 2030 ») |
| Responsable du stade et de la sécurité (M. DOUMERGAT) | propriétaire des processus du jour de match : exprime les besoins de continuité, pilote les prestataires, déclenche la procédure dégradée, dirige la cellule de crise le jour du match |
| Informatique du club (M. PEYRASTRE, sous l'autorité du responsable administratif et financier) | référent de la sécurité des systèmes : tient l'inventaire, valide toute interconnexion et tout accès d'un prestataire, revoit les comptes, suit les incidents ; à terme, appui d'un responsable de la sécurité à temps partagé, indépendant de l'exploitation |
| Communauté d'agglomération (M. CASTÉRADE) | propriétaire des infrastructures installées en 2026 (réseaux, écran géant, éclairage, bornes) : en assure la maintenance et la sécurité, informe le club de toute intervention, met un agent joignable à disposition chaque jour de match |
| Prestataires (PORTALVÈNE Accès, SOLDÉRIS Paiement, GARDALEINE Sécurité, prestataire d'accueil) | obligations contractuelles : délai de rétablissement et astreinte les jours de match, mises à jour soumises à l'accord du club, comptes nominatifs, notification des incidents, participation aux exercices ; tenue à jour des listes d'intervenants |

Formalisation (0,5 pt) : un **avenant à la convention de mise à disposition** et une **annexe sécurité** commune aux contrats des prestataires, appuyés sur une **politique de sécurité des systèmes du stade** (périmètre, rôles, règles d'accès et de mise à jour, gestion des incidents, continuité), approuvée par la direction générale ; un **comité de sécurité des systèmes du stade** (direction générale, responsable du stade, informatique, agglomération, prestataires selon l'ordre du jour), réuni avant chaque saison puis chaque trimestre, qui suit les incidents, les exercices et le plan d'action de l'audit ; une **cellule de crise** désignée pour chaque jour de match.

*3.2 b) – Trois principes de séparation des réseaux*

1. **Cloisonnement en trois zones de confiance** : le réseau du public, ouvert à des milliers de terminaux inconnus, ne donne accès à aucun système du club ni du stade ; les terminaux de paiement de la tribune Est sont rattachés au réseau des systèmes du stade (constat 5).
2. **Flux limités au nécessaire, autorisés et tracés** : seuls les échanges indispensables sont permis entre zones (transmission de la liste des billets vers le contrôle d'accès, par exemple), sur décision documentée de l'informatique et du propriétaire ; le poste de supervision n'est plus relié aux deux réseaux à la fois (constat 6) ; cette segmentation limite la propagation d'une attaque.
3. **Aucune confiance accordée par défaut** : chaque accès, notamment celui des prestataires à distance, est authentifié (authentification multifacteur), nominatif, limité dans le temps et tracé (constats 1 et 4) ; c'est le principe du cadre Zero Trust, qui est une démarche d'architecture et non un produit.

(0,5 pt pour trois principes reliés aux constats.)

*3.2 c) – Résilience des jours de match*

**Procédure dégradée d'entrée du public** (0,5 pt avec son positionnement) : déclenchement par le responsable du stade dès qu'une entrée ne fonctionne plus pendant plus de cinq minutes ; moyens prêts avant chaque match (liste des billets valides exportée à 17 h, à la fin de la transmission, sur des lecteurs portatifs autonomes, contrôle visuel encadré, ordre d'ouverture des entrées) ; rôle de chaque superviseur et de chaque agent ; message au public par la sonorisation, l'écran et l'application ; enregistrement a posteriori des passages ; fin de la procédure décidée par le responsable du stade. Elle relève du **plan de continuité d'activité**, qui maintient l'activité critique en mode dégradé pendant l'incident ; le rétablissement du logiciel par PORTALVÈNE Accès relève de la **reprise**, distincte. Ces deux dispositifs sont des éléments du plan de continuité, pas un plan complet.

**Exercice de crise** (0,5 pt) : scénario réaliste tiré des incidents (panne du contrôle d'accès à l'ouverture des portes d'un match complet, prestataire injoignable ; ou diffusion de faux billets la veille d'un match) ; participants : direction générale, responsable du stade et de la sécurité, informatique, billetterie, communication, agent de l'agglomération, PORTALVÈNE Accès, GARDALEINE Sécurité et prestataire d'accueil ; fréquence : un exercice complet avant le premier match à domicile de chaque saison (août 2027), puis un exercice partiel à mi-saison, par exemple lors d'un événement sans enjeu ; retour d'expérience écrit et mise à jour de la procédure et de la liste de la cellule de crise.

**Réponses tolérées**
- Instance unique « comité des jours de match » qui traite la sécurité des systèmes avec la sécurité du public, si les systèmes y ont une place explicite.
- Fonction de responsable de la sécurité externalisée ou mutualisée avec la communauté d'agglomération, si elle reste indépendante de l'exploitation.
- Principes formulés autrement (défense en profondeur, moindre privilège), s'ils restent au niveau des principes et sont reliés aux constats.
- Exercice sur table plutôt qu'en situation réelle, s'il associe les prestataires.

**Erreurs fréquentes**
- *PCA et PRA confondus* (`ET-02`, `JUR-S02`) — présenter la procédure dégradée comme la remise en service du logiciel ; juste : la procédure dégradée maintient l'entrée du public, la reprise rétablit le système.
- *Zero Trust présenté comme un produit* (`ET-04`, `JUR-S03`) — Zero Trust décrit comme un équipement que l'on achète ; juste : cadre d'architecture qui vérifie chaque accès.
- *Gouvernance réduite à l'informatique* (`JUR-T11`) — oublier l'agglomération propriétaire et les prestataires ; juste : responsabilités partagées et formalisées.
- *Détail technique* (`JUR-T12`) — réglages des équipements de réseau ; juste : principes de séparation et de contrôle des flux.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Rôles et gouvernance des systèmes critiques ; politique de sécurité | acteurs, comité, politique | F12 § 1 | notion de cours |
| Le modèle Zero Trust (avis de l'ANSSI) | cadre d'architecture | `zero_trust_anssi` ; F12 § 3 | en vigueur |
| ISO 22301:2019 | continuité, exercices | `iso_22301_2019` ; F12 § 4 | en vigueur |

---

### 3.3 – Diagnostic d'audit (2,5 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse » ; `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ». Limite : l'exécution de tests techniques détaillés n'est pas attendue.

**Annexes mobilisées** : annexes 3.3 (périmètre, méthode, onze constats), 3.2 (incidents) et 3.1 (acteurs).

**Barème indicatif (2,5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Forme : destinataire, objet, 20 lignes au maximum, structure visible, vocabulaire accessible | 0,5 |
| a-2 | Constats regroupés en trois ou quatre thèmes et hiérarchisés, chacun relié à son risque | 1 |
| a-3 | Recommandations priorisées, datées et confiées à un responsable | 0,5 |
| b | Audit distingué du contrôle (indépendance, référentiel, appréciation d'ensemble, recommandations) ; suites : plan d'action et suivi | 0,5 |

**Réponse attendue**

*3.3 a) – Note de synthèse*

Note modèle (18 lignes) :

<!-- note -->
**À l'attention de Mme LAFERRADE — Objet : audit des systèmes du jour de match, diagnostic et priorités (juin 2027)**

L'audit confirme que l'entrée du public dépend de systèmes que personne ne pilote.

1. Continuité non assurée (constats 2, 3, 4, 7) : ni procédure dégradée, ni exercice de crise, prestataire injoignable les soirs de match et libre de ses mises à jour. Risque : nouvelle panne d'un match complet.
2. Accès et réseaux mal cloisonnés (1, 5, 6, 9) : comptes partagés, paiement sur le réseau du public, poste relié à deux réseaux. Risque : intrusion jusqu'aux systèmes du stade.
3. Responsabilités floues (8, 11) : convention muette, aucun inventaire. Risque : aucune décision possible en cas d'incident.
4. Billets des partenaires non sécurisés (10). Risque : nouvelle fraude.

Priorités : avant le premier match de 2027-2028, avenant avec PORTALVÈNE Accès (gel des mises à jour, astreinte, délai), procédure dégradée testée en exercice, comptes nominatifs, terminaux retirés du réseau du public (M. DOUMERGAT, M. PEYRASTRE) ; d'ici décembre 2027, avenant à la convention et inventaire avec l'agglomération, billets nominatifs.

Je propose un comité trimestriel pour suivre ce plan.
<!-- /note -->

Éléments d'appréciation :
- **regroupement et hiérarchie** (1 pt) : la continuité vient en premier (incident déjà survenu, impact critique), puis l'exposition des systèmes, puis la gouvernance, qui conditionne la durée des mesures ; un classement différent est accepté s'il est justifié ; 0,5 pt si les constats sont repris un à un sans regroupement ni risque ;
- **recommandations** (0,5 pt) : réalistes pour une informatique de deux personnes, datées par rapport au premier match à domicile de septembre 2027, confiées à un responsable.

*3.3 b) – Audit et contrôle, suites de la mission*

Le **contrôle** vérifie, de façon ponctuelle et souvent par les acteurs eux-mêmes, qu'une opération respecte une règle (un agent vérifie un billet, le responsable compte les entrées). L'**audit** est un examen indépendant (cabinet extérieur au club et aux prestataires), méthodique (entretiens, revue des contrats, observation d'un match) et fondé sur un référentiel (ISO/IEC 27001:2022), qui apprécie la conception et l'efficacité de l'ensemble du dispositif et de sa gouvernance, puis conclut par des recommandations hiérarchisées (F10 § 1.1). Suites : **plan d'action** validé par la directrice générale (mesure, responsable, échéance, indicateur), **suivi** par le comité à chaque trimestre et compte rendu au conseil d'administration, **audit de suivi** après les premiers matchs de la saison 2027-2028 (0,5 pt).

**Réponses tolérées**
- Note en tirets ou avec un court tableau des priorités, dans la limite des 20 lignes.
- Trois thèmes au lieu de quatre (billets rattachés à la continuité ou aux accès), si tous les constats majeurs sont couverts.
- Recommandations datées par rapport au calendrier sportif (« avant le premier match à domicile ») plutôt qu'à une date.

**Erreurs fréquentes**
- *Note trop longue ou non hiérarchisée* (`JUR-S07`, `JUR-T07`) — reprise des onze constats dans l'ordre de l'annexe ; juste : thèmes, risques et priorités.
- *Paraphrase des constats sans risque* (`JUR-T03`) — juste : chaque thème est relié à la conséquence qu'il expose.
- *Audit du SI confondu avec l'audit des comptes* (`ET-34`) — juste : l'audit porte sur la sécurité, la continuité et la gouvernance des systèmes du jour de match.
- *Démarche complète de mission à la place de la note* (`JUR-T07`) — juste : la mission est faite, il s'agit d'en restituer le diagnostic.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI, diagnostic, note de synthèse | constat, risque, recommandation, priorité, suivi | F10 § 1.1 et 1.2 | notion de cours |
| ISO/IEC 27001:2022 | référentiel de l'audit | `iso_27001_2022` ; F12 § 2 | en vigueur |

---

### 3.4 – Empreinte du stade connecté et demande du partenaire (5 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.b` « Cadres réglementaires : CSRD (Corporate Sustainability Reporting Directive), ESRS (European Sustainability Reporting Standards) » ; `4.3.d` « Bonnes pratiques Green IT : éco-conception, mutualisation, cycle de vie des équipements » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI ». Limites : le champ de la CSRD est donné par l'énoncé, jamais déterminé ; aucun calcul d'empreinte ; la durabilité est intégrée à la gouvernance du SI.

**Annexes mobilisées** : annexes 3.4 (équipements, consommations, estimation des émissions, contenus, demande d'ÉNERVALDE, repères au 31/12/2026), 3.1 (acteurs) et 1.1 (chiffres clés).

**Barème indicatif (5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Green IT et sobriété numérique définis et distingués | 0,5 |
| a-2 | Analyse sous les trois angles (fabrication, usage, durée de vie), étayée par les chiffres de l'annexe 3.4, compensation du gain de l'éclairage par le numérique relevée | 0,5 |
| a-3 | Deux outils ou indicateurs de mesure adaptés au cas, chacun avec sa limite | 0,5 |
| b-1 | Quatre mesures sur quatre domaines distincts, chacune avec principe, effet attendu et porteur ; 1 pour trois, 0,5 pour deux | 1 |
| b-2 | Priorisation justifiée (poids de la fabrication, rapidité, coût, dépendance envers l'agglomération) | 0,5 |
| c-1 | Raison de la demande : ÉNERVALDE, dans le champ de la CSRD, rend compte de sa chaîne de valeur, dont le club fait partie ; enjeu du renouvellement | 0,5 |
| c-2 | Réponse du club : norme volontaire (modules, plafond de la chaîne de valeur), données disponibles et réponse commune aux partenaires ; rôle du SI (collecte, traçabilité, fiabilité) | 0,5 |
| d | Deux indicateurs complets (formule, source, fréquence, cible, axe) ; 0,5 par indicateur | 1 |

**Réponse attendue**

*3.4 a) – Analyse de l'empreinte*

Le **Green IT** vise à réduire l'empreinte environnementale du SI lui-même (fabrication, usage et fin de vie des équipements, centres de données, logiciels), notamment par l'efficacité ; la **sobriété numérique** interroge d'abord le besoin : renoncer à un équipement, à une fonction ou à un contenu, ou les dimensionner au juste usage, plutôt que seulement les rendre moins consommateurs (F14 § 3). L'IT for green, distinct, mobilise le numérique pour réduire l'empreinte de l'organisation, comme le pilotage de l'éclairage (0,5 pt).

Analyse (0,5 pt) :
- **Fabrication** : elle représente 75 % des 40 tonnes d'équivalent CO2 émises chaque année par les équipements numériques du stade, soit environ 30 tonnes : 200 écrans de loges au lieu de 60, deux écrans géants, 120 bornes, 80 lecteurs, 60 terminaux. Ce constat rejoint le repère de l'ADEME et de l'Arcep : l'empreinte du numérique tient d'abord à la fabrication des équipements ; selon le volet de 2022 de cette étude, les terminaux, dont ceux des 40 000 utilisateurs de l'application, en concentraient l'essentiel.
- **Usage** : la consommation totale baisse de 25 % (320 à 240 MWh) grâce à l'éclairage à diodes (− 60 %), mais celle des écrans, réseaux et systèmes est multipliée par six (20 à 120 MWh) et représente la moitié du total : le gain de l'éclairage masque la croissance du numérique, due à l'ajout d'équipements ; l'éclairage pilotable, plus efficace, ouvre en outre un usage nouveau, les spectacles lumineux (effet rebond). Les 120 bornes et les 200 écrans des loges restent allumés en permanence pour un stade utilisé 55 jours par an. Les contenus ajoutent un usage non mesuré : 40 To de vidéos dont 70 % ne sont plus regardées après un mois, lecture automatique en très haute définition, application de 180 Mo, page d'accueil notée F, diffusions en très haute définition pour 300 spectateurs.
- **Durée de vie** : 60 écrans jetés à cinq ans, lecteurs remplacés tous les trois ans, à chaque renouvellement du contrat, quelle que soit leur usure ; sans inventaire, le club ne connaît ni l'âge ni l'état de ses équipements.

Outils et indicateurs (0,5 pt, deux attendus) :
- **sous-comptage de l'électricité** par usage (MWh, relevés mensuels de l'agglomération) : mesure fiable de l'usage, mais ignore la fabrication, qui domine, et l'origine de l'électricité ;
- **bilan des émissions de gaz à effet de serre** du numérique par catégories d'émissions (GHG Protocol, méthode Bilan Carbone), qui intègre la fabrication : complet, mais fondé sur des estimations et des facteurs d'émission, avec une incertitude forte (l'estimation de l'annexe est celle d'un bureau d'études) ;
- **EcoIndex** de la page d'accueil du site et des écrans de l'application : indicateur simple et parlant pour le pôle marketing, mais relatif, limité à une page et qui n'est pas une analyse de cycle de vie ;
- **durée de vie moyenne des équipements** tirée d'un inventaire : directement liée à la fabrication, mais suppose un inventaire qui n'existe pas encore.

*3.4 b) – Quatre mesures priorisées*

| Priorité | Domaine | Principe | Effet attendu (annexe 3.4) | Porteur |
|---|---|---|---|---|
| 1 | Durée de vie des équipements | inventaire des équipements numériques du stade ; aucun remplacement d'un équipement en état de fonctionner ; écrans conservés au moins dix ans ; avenant avec PORTALVÈNE Accès pour renouveler les lecteurs selon leur état et non à chaque renouvellement du contrat, tous les trois ans ; réemploi ou reconditionnement, critères de durabilité et de réparabilité dans les achats | agit sur la fabrication, 75 % des émissions ; évite de nouveaux rebuts comme les 60 écrans de 2021 | responsable administratif et financier (achats, informatique) et responsable du stade, avec l'agglomération |
| 1 | Pilotage des écrans, de l'éclairage et du réseau sans fil | mise en veille programmée des 200 écrans des loges ; bornes et écrans allumés seulement pendant les 55 jours d'utilisation ; spectacles lumineux limités aux grands matchs ; programmation horaire de l'écran géant | réduit l'essentiel des 120 MWh d'usage du numérique, rapidement et sans investissement | responsable du stade et de la sécurité, avec l'agglomération propriétaire |
| 2 | Contenus et application | écoconception selon le RGESN : suppression de la lecture automatique, résolution adaptée à l'usage, application allégée, durée de conservation des vidéos et suppression des 70 % qui ne sont plus regardées, diffusions en direct en définition adaptée | réduit le stockage (40 To), les échanges de données et la sollicitation des téléphones des supporters ; amélioration de la note F | responsable du pôle marketing et numérique, avec l'agence de l'application |
| 3 | Mutualisation | avec la stratégie numérique responsable de l'agglomération (2025) : inventaire, sous-comptage et achats communs ; usage partagé des écrans et des bornes avec les autres événements ; une seule collecte des données environnementales du stade pour le club et pour l'agglomération | évite les doublons d'équipements et de collectes ; donne au club les données qu'il n'a pas | directrice générale et M. CASTÉRADE |

(1 pt pour quatre mesures complètes ; 0,5 pt pour la priorisation.)

Priorisation : la durée de vie vient en premier parce que la fabrication domine l'empreinte ; le pilotage est au même rang parce qu'il est immédiat et gratuit ; l'écoconception demande un travail avec l'agence et un changement de pratiques du pôle marketing ; la mutualisation dépend d'un accord avec l'agglomération, à négocier dans l'avenant à la convention (question 3.2).

*3.4 c) – La demande d'ÉNERVALDE*

**Pourquoi** (0,5 pt) : ÉNERVALDE entre dans le champ de la CSRD modifiée par la directive Omnibus I (donnée de l'annexe) ; son état de durabilité, établi selon les normes européennes (ESRS), couvre sa **chaîne de valeur** : ses achats, dont le partenariat de 900 000 € par saison, et les impacts liés à sa marque (écran géant, vidéos) entrent dans les informations qu'elle publie, notamment ses émissions indirectes. Le club doit donc lui fournir des données fiables ; à défaut, ÉNERVALDE recourra à des estimations défavorables, et la durabilité devient un critère du renouvellement de 2028.

**Ce que le club peut fournir** (0,5 pt) : le club n'entre pas dans le champ de la CSRD (donnée) et compte moins de 1 000 salariés : depuis les exercices ouverts au 01/01/2027, ÉNERVALDE ne peut exiger de lui que les informations de la liste prévue pour la chaîne de valeur par le règlement délégué (UE) 2026/1560, qui fixe aussi la **norme volontaire pour les PME** (VSME). Le club peut donc établir volontairement un rapport selon le **module de base** de cette norme, puis le cas échéant son module complet, et le remettre à **tous** ses partenaires au lieu de remplir un questionnaire par partenaire (inquiétude de M. BARRALOU) ; il y joint ses consommations d'énergie (sous-compteurs), l'estimation des émissions du bureau d'études avec ses hypothèses, et sa politique de numérique responsable (mesures de la question b). Le **système d'information** en est la condition : il identifie la source et le responsable de chaque donnée (agglomération pour l'électricité, inventaire pour les équipements, plateforme de vidéos pour le stockage), collecte les données de tiers, conserve la méthode et les hypothèses (traçabilité) et contrôle leur cohérence d'une saison à l'autre (fiabilité).

*3.4 d) – Deux indicateurs*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| Consommation d'électricité des équipements numériques du stade | somme des relevés des sous-compteurs « écrans » et « réseaux et systèmes » sur la saison, en MWh | sous-compteurs de la communauté d'agglomération | relevé mensuel, cumul par saison | 80 MWh au plus en 2028-2029, contre 120 en 2026-2027, soit un tiers de moins | environnement |
| Durée de vie moyenne des équipements numériques du stade à leur retrait | somme des âges des équipements retirés du service / nombre d'équipements retirés, par famille (écrans, lecteurs, bornes, terminaux) | inventaire des équipements numériques du stade, tenu par l'informatique du club avec l'agglomération | annuelle | au moins dix ans pour les écrans, six ans pour les lecteurs ; aucun équipement en état de fonctionner jeté | environnement |

(0,5 pt par indicateur complet.)

**Réponses tolérées**
- Définition de la sobriété accompagnée de l'IT for green, ou distinction Green IT / IT for green, si la sobriété est définie.
- Autres outils : analyse de cycle de vie citée en principe, indicateur d'efficacité énergétique d'un centre de données si le candidat évoque l'hébergement des vidéos.
- Ordre de priorité différent (pilotage en premier, pour sa rapidité), s'il est justifié.
- Autres indicateurs complets : note EcoIndex de la page d'accueil (cible C au moins en 2028), volume de vidéos stockées, part des heures d'allumage des écrans hors événements, part des achats d'équipements comportant des critères de durabilité.
- « Effet rebond » employé au sens large pour la croissance du numérique, s'il est expliqué.
- Mention de la double matérialité pour expliquer la demande d'ÉNERVALDE (impacts de sa chaîne de valeur et risque de réputation), sans détail des normes thématiques.

**Erreurs fréquentes**
- *Sobriété confondue avec l'économie d'énergie* (`ET-12`) — juste : la sobriété questionne le besoin (bornes allumées toute l'année, vidéos jamais regardées).
- *Empreinte réduite à l'électricité* (`ET-38`) — se féliciter de la baisse de 25 % ; juste : la fabrication représente 75 % des émissions et la consommation du numérique a été multipliée par six.
- *Assujettissement discuté ou seuils périmés* (`ET-41`, `ET-17`) — calculer si le club ou ÉNERVALDE entre dans le champ ; juste : le champ est donné par l'annexe ; la CSRD est une obligation d'information sur la chaîne de valeur, pas un simple rapport.
- *Indicateurs génériques ou incomplets* (`ET-18`, `JUR-A02`) — « réduire l'empreinte » sans formule ni cible ; juste : formule, source, fréquence, cible et axe.
- *Calcul d'empreinte* (périmètre 4.3.e) — recalculer des émissions ; juste : lecture des données fournies.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Green IT, sobriété, IT for green ; indicateurs | définitions, mesures, indicateurs | F14 § 1, 3 et 4 | notion de cours |
| Directive (UE) 2022/2464 (CSRD), modifiée par la directive (UE) 2026/470 « Omnibus I » | champ donné, chaîne de valeur | `csrd`, `csrd_omnibus` ; fiche commune | en vigueur ; Omnibus I non transposée en France |
| ESRS révisées, règlement délégué (UE) 2026/1563 | normes de l'état de durabilité d'ÉNERVALDE | `esrs_2026` ; fiche commune | applicable aux exercices ouverts à compter du 01/01/2027 |
| Norme volontaire VSME, règlement délégué (UE) 2026/1560 | modules, plafond de la chaîne de valeur | `vsme` ; fiche commune ; `ue4/fiches/F12` § 4 | en vigueur |
| Loi REEN n° 2021-1485 | axes, stratégie des intercommunalités | `loi_reen` ; F14 § 2 | en vigueur |
| RGESN, version 2024 | écoconception des contenus et de l'application | `rgesn_2024` ; F14 § 2 | en vigueur |
| Étude ADEME-Arcep | poids de la fabrication et des terminaux | `etude_ademe_arcep_numerique` ; F14 § 1 | publiée |
| EcoIndex ; GHG Protocol ; méthode Bilan Carbone | outils de mesure | `ecoindex`, `ghg_protocol`, `methode_bilan_carbone` ; F14 § 4 | en vigueur |
