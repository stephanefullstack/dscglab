# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 48 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 audit et fiabilisation, F12 sécurité et résilience, F14 numérique responsable, F15 RGPD opérationnel, et `ue5/fiches/referentiels_dates.yaml` (vérifiés le 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles, des référentiels et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Les risques de la rentrée et l'analyse d'impact | `4.1.a` Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA ; `4.1.b` Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers ; `4.1.c` Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers | 4 |
| 3.2 La continuité et la sécurité de la rentrée 2027 | `4.2.b` Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques ; `4.2.d` Dispositifs de surveillance et de résilience : IAM, PCA/PRA (plans de continuité et de reprise d'activité) | 3 |
| 3.3 L'audit du traitement des dossiers de candidature | `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ; `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ; `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. | 3 |
| 3.4 Le pilotage de l'énergie des résidences | `4.3.a` Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale ; `4.3.e` Outils et indicateurs de mesure de l'impact environnemental des SI ; `4.3.f` Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) | 3 |
| **Dossier 3 – Sécuriser la campagne de rentrée, auditer le traitement des candidatures et piloter l'énergie des résidences** |  | **13** |

Répartition indicative : connaissances (typologie des risques, analyse d'impact sur l'activité, PCA et PRA, audit de conformité, Green IT et IT for green) environ 2,5 points (items 3.1 a-1, 3.1 b-1, 3.2 a-1, 3.3 a-1 et 3.4 a-1) ; analyse des annexes et recommandations environ 10,5 points, soit environ 80 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes.

---

### 3.1 – Les risques de la rentrée et l'analyse d'impact (4 points)

**Référence au programme**
- §4.1 – Identifier, analyser et gérer les risques liés aux systèmes d'information : `4.1.a` « Détecter, évaluer et traiter les risques associés aux systèmes d'information, en intégrant les dimensions réglementaires, éthiques et technologiques, y compris les apports de l'IA » ; `4.1.b` « Typologies des risques SI : cybermenaces, défaillances opérationnelles, risques réglementaires et métiers » ; `4.1.c` « Méthodes d'analyse d'impact sur les processus, la continuité de service et les états financiers ». Limites : l'analyse de sécurité technique n'est pas attendue dans le détail ; l'impact sur les états financiers n'est pas demandé ici.

**Annexes mobilisées** : annexe 3.1 (événements de la rentrée 2026, points de vue, échelles), annexe 3.2 (six processus selon la période, dispositif actuel), annexe 3.5 (ISO/IEC 27005:2022, ISO 22301:2019) et annexe 1.1 (7 000 baux dont 70 % de juin à septembre, clé virtuelle dans 22 résidences, badges dans 38, portail relié au logiciel de gestion locative par des échanges de fichiers chaque nuit).

**Barème indicatif (4 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Typologie présentée (cybermenaces, défaillances opérationnelles, risques réglementaires, risques métiers), avec les critères touchés (confidentialité, intégrité, disponibilité, traçabilité) | 0,5 |
| a-2 | Cinq risques formulés comme des événements redoutés, tirés de l'annexe 3.1, avec leur cause | 0,5 |
| a-3 | Cinq risques classés dans la typologie, le classement justifié | 0,5 |
| b-1 | Analyse d'impact sur l'activité définie (conséquences d'une interruption dans le temps, dépendances, processus critiques, durées admissibles) | 0,5 |
| b-2 | Impact d'une interruption de trois processus, dont la remise des accès, apprécié selon la période, avec les dépendances (bail et dépôt de garantie avant les accès, logiciel de gestion locative) | 0,5 |
| b-3 | Processus critiques et durée maximale d'interruption admissible de chacun, justifiées et différenciées selon la période | 0,5 |
| c-1 | Cinq risques cotés selon les échelles de l'annexe 3.1 C et deux priorités justifiées par la probabilité et l'impact | 0,5 |
| c-2 | Une option de traitement et une mesure pour chacune des deux priorités ; réponse à M. CALVÉRAC | 0,5 |

**Réponse attendue**

*3.1 a) – La typologie et les cinq risques*

**Typologie** (a-1) : les risques liés aux systèmes d'information se classent en quatre familles (F12 § 0 et § 5) :
- les **cybermenaces**, actes malveillants : hameçonnage et usurpation d'identité, compromission de comptes, rançongiciel, attaque par un fournisseur ;
- les **défaillances opérationnelles**, non intentionnelles : panne, saturation, erreur humaine, défaillance d'un prestataire, incohérence des données entre applications ;
- les **risques réglementaires** : manquement à une obligation, ici les principes de protection des données personnelles ;
- les **risques métiers** : effets sur l'activité et la stratégie (candidats perdus, taux d'occupation, image, sécurité des résidents).

Chaque risque porte atteinte à un ou plusieurs critères : confidentialité, intégrité, disponibilité, traçabilité. Une même cause peut relever de plusieurs familles ; le classement retient la famille de la cause et signale l'effet métier.

**Six risques révélés par l'annexe 3.1** (a-2 et a-3 ; cinq sont attendus) :

| Risque (événement redouté) et cause | Famille | Critère touché |
|---|---|---|
| R1 – Des fraudeurs se font passer pour ORVANELLE et détournent les dépôts de garantie des familles : le lien de paiement est envoyé par courriel, et les fraudeurs connaissent le nom des candidats et leur résidence | cybermenace (hameçonnage, usurpation d'identité) ; effet métier : image, presse | intégrité de la relation de paiement, confiance |
| R2 – Un tiers prend la main sur le compte d'un résident et ouvre la porte de son logement avec la clé virtuelle : identifiants réutilisés, mot de passe seul | cybermenace (compromission de comptes) ; effet sur la sécurité des personnes et violation de données | confidentialité, intégrité ; sécurité physique |
| R3 – Le service de clé virtuelle est indisponible un jour d'arrivées et les résidents ne peuvent pas entrer : prestataire sans assistance le week-end ni engagement de rétablissement, aucune clé de secours à l'accueil | défaillance opérationnelle (dépendance à un prestataire) ; effet métier | disponibilité |
| R4 – Le portail sature à l'ouverture des réservations et des candidats partent chez des concurrents : 8 000 connexions pour une capacité de 1 500 | défaillance opérationnelle (capacité) ; risque métier (occupation, image) | disponibilité |
| R5 – Les pièces justificatives de milliers de candidats et de garants, conservées sans limite dans les messageries, sont consultées par un tiers : 1,5 million de pièces jointes, comptes de 40 saisonniers restés ouverts | risque réglementaire (minimisation, conservation, sécurité) et cybermenace | confidentialité |
| R6 – Un logement est promis à deux candidats : portail et logiciel de gestion locative synchronisés une fois par nuit | défaillance opérationnelle (intégrité des données entre deux applications) ; effet métier | intégrité |

*3.1 b) – L'analyse d'impact sur l'activité*

**Définition** (b-1) : l'**analyse d'impact sur l'activité** (BIA) mesure, pour chaque processus, les conséquences d'une interruption selon sa durée (résidents et candidats touchés, pertes, image, sécurité, obligations) et selon la période. Elle recense ses dépendances (applications, prestataires, personnes) et en déduit les processus critiques, leur **durée maximale d'interruption admissible** (RTO) et leur **perte de données maximale admissible** (RPO). Elle fonde le plan de continuité ; ISO 22301:2019 en fait la première étape (F12 § 4 ; annexe 3.5). Chez ORVANELLE, la criticité dépend de la **saison** : 70 % des baux sont signés de juin à septembre, et environ 2 000 arrivées se concentrent sur quatre samedis.

**Impact d'une interruption de trois processus selon la période** (b-2 et b-3) :

| Processus | De juin à septembre | D'octobre à mai | Critique ? | Durée maximale d'interruption admissible |
|---|---|---|---|---|
| Remise des accès (clé virtuelle, 22 résidences) | environ 2 000 arrivées sur quatre samedis, jusqu'à 40 dans une résidence le même jour ; au-delà d'une heure, la file se forme dans le hall avec les bagages, l'accueil ferme à 19 h et chaque résident qui ne peut pas entrer est hébergé aux frais d'ORVANELLE ; sécurité et image en jeu (annexe 3.1 : 120 résidents bloqués six heures, 30 nuits d'hôtel). Dépendances : service en ligne du prestataire, bail signé et dépôt payé | 2 100 arrivées étalées, surtout en semaine, accueil présent : on peut faire patienter le résident ou reporter son arrivée | **critique** en rentrée | **une heure** les jours d'arrivée de la rentrée ; une demi-journée les autres jours de l'été ; une journée d'octobre à mai. Les 38 résidences à badges, programmés sur un poste local, ne dépendent pas du service en ligne |
| Réservation (portail) | 24 000 candidatures ; le jour de l'ouverture, 8 000 connexions en une heure ; un candidat bloqué se tourne vers une autre offre **dans la journée**, au détriment de l'objectif de 95 % d'occupation | 6 000 candidatures ; le candidat réessaie le lendemain | **critique** de juin à septembre, surtout le jour de l'ouverture | **quelques heures** le jour de l'ouverture, une demi-journée le reste de l'été ; un à deux jours le reste de l'année |
| Signature du bail | en moyenne 40 baux par jour, jusqu'à 80 fin août ; le logement n'est réservé que 48 heures : au-delà, il est proposé à un autre candidat (risque de perdre le résident ou de créer une double attribution) ; sans bail, pas d'accès. Dépendances : prestataire de signature, logiciel de gestion locative pour préparer le bail | une dizaine par jour ; un report de deux jours est sans dommage | **critique** en rentrée | **24 heures** en rentrée, pour garder une marge sur les 48 heures de réservation ; deux à trois jours le reste de l'année |

Pour comparaison : l'**encaissement du dépôt de garantie** devient critique par dépendance, puisque les accès ne sont remis qu'après paiement (24 heures en rentrée) ; le **contrôle des pièces** supporte deux à trois jours de retard, rattrapés au prix d'heures supplémentaires ; l'**état des lieux**, déjà fait sur papier et saisi plus tard, n'est pas critique. Les processus critiques dépendent tous du **logiciel de gestion locative**, pour l'attribution, la préparation du bail et le rapprochement des dépôts. Or son hébergeur ne s'engage à intervenir que « dans le jour ouvré suivant », et ses sauvegardes n'ont jamais été restaurées. Cet écart avec des durées admissibles de quelques heures en rentrée fonde le dispositif de la question 3.2.

*3.1 c) – La cotation, les deux priorités et leur traitement*

**Cotation selon les échelles de l'annexe 3.1 C** (c-1) :

| Risque | Probabilité | Impact | Criticité |
|---|---|---|---|
| R2 – Compte pris en main, porte ouverte | 4 : 200 comptes en deux mois, mot de passe seul, toujours le cas | 4 : la clé virtuelle de 15 comptes ouvrait un logement, la sécurité des résidents est en cause ; intrusion impossible à exclure (journaux de sept jours) | **16** |
| R1 – Fraude au dépôt de garantie | 4 : 50 familles en deux mois, facile à provoquer, le lien de paiement part toujours par courriel | 3 : environ 35 k€, 400 appels et courriels, écho dans la presse régionale | **12** |
| R3 – Clé virtuelle indisponible un jour d'arrivées | 3 : survenu le 5 septembre, aucun engagement ni assistance le week-end | 3 : un samedi de pointe (environ 500 arrivées), une panne d'une journée entière dans les 22 résidences équipées toucherait de l'ordre de 200 résidents, et les arrivées de la journée seraient bloquées jusqu'au soir | 9 |
| R4 – Portail saturé à l'ouverture | 3 : survenu, capacité inchangée | 3 : 8 000 candidats touchés, 1 800 appels sans réponse (60 %) | 9 |
| R5 – Pièces des messageries consultées par un tiers | 2 : aucune fuite établie, mais plausible (origine des informations des fraudeurs inconnue, comptes de saisonniers ouverts) | 4 : données de milliers de candidats et de garants | 8 |
| R6 – Logement promis à deux candidats | 4 : 150 fois en un été, la synchronisation reste nocturne | 2 : 150 candidats touchés, relogés, sans écho public | 8 |

**Deux priorités** : **R2 (16)** et **R1 (12)**, les seules qui atteignent le seuil de 12 fixé par le directoire. R2 vient en premier : il touche la **sécurité physique** des résidents, ce que redoute Mme ROUSTAGNE (« une porte qui s'ouvre pour quelqu'un qui n'est pas le résident »). R1 vient ensuite : il se répète et il est facile à reproduire. R3 et R4 suivent (9) ; R3 est traité par le dispositif de continuité de la question 3.2.

**Options de traitement et mesures** (c-2) :
- **R2 – réduire** : exiger une **authentification à deux facteurs** pour tout compte de l'application qui porte une clé virtuelle ; réinitialiser les 200 comptes et réactiver les 15 clés après vérification de l'identité du résident ; prévenir le résident de toute connexion depuis un nouveau téléphone ; conserver les journaux des serrures plusieurs mois. L'option **éviter** peut compléter : lier la clé au seul téléphone enregistré à l'arrivée, et non au compte. **Transférer** est impossible : la sécurité des personnes ne se transfère pas. **Accepter** est exclu : la criticité est maximale.
- **R1 – réduire** : supprimer l'envoi du lien de paiement par courriel. Le dépôt de garantie ne se paie plus que dans l'espace personnel du candidat sur le portail, après connexion. Chaque message d'ORVANELLE et le portail rappellent qu'« ORVANELLE ne communique jamais de coordonnées bancaires par courriel ». Un numéro de contre-appel permet aux familles de vérifier une demande, et les familles sont alertées dès le premier signalement. Le traitement de R5 réduit aussi les fuites d'informations dont se servent les fraudeurs. Le **transfert** à un assureur ne couvrirait au mieux que des frais d'ORVANELLE, pas les pertes des familles.

**Réponse à M. CALVÉRAC** : la fraude n'est pas « l'affaire des familles ». Elle exploite une pratique d'ORVANELLE, le paiement demandé par courriel, et des informations sur ses candidats ; elle atteint sa réputation (écho dans la presse) et la confiance des familles au moment de la décision. **Accepter** ce risque est exclu : sa criticité de 12 atteint le seuil du directoire. La saturation du portail (9) est réelle et doit être traitée, mais après R2 et R1.

**Réponses tolérées**
- Autre typologie (risques internes et externes, accidentels et intentionnels ; ou classement par critère confidentialité, intégrité, disponibilité, traçabilité), si les quatre familles du programme apparaissent dans le classement.
- R5 coté 3 en probabilité (12), puisque l'origine des informations des fraudeurs est inconnue et que les comptes des saisonniers restent ouverts, et retenu comme deuxième priorité à la place de R1, si le choix est justifié ; R3 coté 2 en impact (6) d'après les seuls faits du 5 septembre.
- R3 coté 4 en impact (12), au titre de la sécurité des résidents laissés devant leur porte le soir, quand l'accueil ferme à 19 h (scénario de Mme ROUSTAGNE), et retenu comme deuxième priorité, si le choix est justifié.
- Autres processus analysés en b), comme l'encaissement du dépôt de garantie ou le contrôle des pièces, si la remise des accès y figure et si les durées sont différenciées selon la période ; durées voisines (deux heures pour la remise des accès un jour d'arrivée, 48 heures pour la signature) si elles sont justifiées.
- Démarche fondée sur ISO/IEC 27005:2022 (lignes directrices) ou EBIOS Risk Manager (méthode), si la nature du référentiel est juste.

**Erreurs fréquentes**
- *Typologie récitée sans application, ou risques réduits à des incidents passés* (`JUR-T01`, `JUR-T07`) — juste : des événements redoutés, avec leur cause, classés puis cotés selon les échelles de l'annexe.
- *Analyse d'impact sans la saison* (`JUR-T08`) — juste : la même panne est critique un samedi de septembre et presque indolore en février.
- *Durée maximale d'interruption et perte de données maximale confondues* (`ET-03`, `JUR-S02`) — juste : durée d'interruption (RTO) et perte de données (RPO) sont deux objectifs distincts.
- *Fraude laissée aux familles, comme le propose M. CALVÉRAC* — juste : le risque naît d'un processus d'ORVANELLE ; l'option « accepter » est exclue au-delà du seuil.
- *Droit du dépôt de garantie, du bail ou du logement* — non attendu.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Typologie des risques SI, critères CID et traçabilité | cybermenaces, défaillances, risques réglementaires et métiers | F12 § 0, § 1 et § 5 | notion de cours |
| Analyse d'impact sur l'activité, RTO, RPO | processus critiques, durées admissibles | F12 § 4 | notion de cours |
| ISO 22301:2019 | norme d'exigences de la continuité d'activité ; analyse d'impact | `iso_22301_2019` ; F12 § 4 | en vigueur |
| ISO/IEC 27005:2022 | lignes directrices de gestion des risques | `iso_27005_2022` ; F12 § 2 | en vigueur |
| EBIOS Risk Manager, version 1.5 (toléré) | méthode en cinq ateliers | `ebios_rm_1_5` ; F12 § 2 | en vigueur |

---

### 3.2 – La continuité et la sécurité de la rentrée 2027 (3 points)

**Référence au programme**
- §4.2 – Concevoir, mettre en œuvre et contrôler une politique de sécurité des systèmes d'information : `4.2.b` « Élaboration d'une politique de cybersécurité fondée sur l'analyse des risques » ; `4.2.d` « Dispositifs de surveillance et de résilience : IAM (Identity & Access Management), PCA/PRA (plans de continuité et de reprise d'activité) ». Limites : la mise en œuvre technique des solutions de cybersécurité n'est pas exigée ; les normes se mobilisent sans entrer dans leur démarche de conformité formelle.

**Annexes mobilisées** : annexe 3.2 (processus, dispositif actuel, options du prestataire de la clé virtuelle), annexe 3.1 (panne du 5 septembre, comptes pris en main, fraude), annexe 3.5 (ISO 22301:2019, ISO/IEC 27001:2022, règlement sur la cyberrésilience) et annexe 1.1 (clé virtuelle, badges, dépenses du système d'information de 4,5 M€).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | PCA et PRA définis et distingués (maintenir en mode dégradé pendant la crise / restaurer et revenir à la normale) | 0,5 |
| a-2 | Mode dégradé de la remise des accès et de la signature des baux, tiré des annexes (activation la veille, clés de secours à l'accueil, liste des arrivées, réservation prolongée) | 0,5 |
| a-3 | Objectifs de durée maximale d'interruption et de perte de données admissibles, justifiés par l'analyse d'impact | 0,5 |
| a-4 | Engagement à obtenir du prestataire de la clé virtuelle et exercices avant la rentrée | 0,5 |
| b-1 | Trois mesures de sécurité, chacune reliée à un risque différent de la question 3.1, dont une contre la fraude au dépôt de garantie | 0,5 |
| b-2 | Hiérarchie et calendrier, rang de la première justifié | 0,5 |

**Réponse attendue**

*3.2 a) – Le dispositif de continuité de la rentrée*

**PCA et PRA** (a-1) : le **plan de continuité d'activité** (PCA) organise le **maintien** des processus critiques pendant la crise, au besoin en **mode dégradé** (procédures de secours, moyens de substitution, organisation de crise). Le **plan de reprise d'activité** (PRA) organise la **restauration** des systèmes et le **retour à la normale** après le sinistre (restauration des sauvegardes, rattrapage des opérations faites en mode dégradé). Les deux reposent sur l'analyse d'impact (question 3.1 b) et ne valent que s'ils sont exercés (F12 § 4). ORVANELLE n'a ni l'un ni l'autre.

**Mode dégradé** (a-2) :

| Processus | Mode dégradé proposé | Constat traité |
|---|---|---|
| Remise des accès | **activer les clés la veille de l'arrivée** (option du prestataire), chaque clé ne fonctionnant qu'à partir du jour prévu : une panne le jour même ne bloque plus les arrivées attendues ; l'état des lieux se fait à l'arrivée, comme aujourd'hui. Pendant la rentrée, placer les **clés mécaniques de secours** dans un coffre à l'accueil de chaque résidence équipée, et non plus dans le local des services techniques fermé le week-end ; les remettre contre signature sur un registre et les récupérer après le rétablissement. Imprimer chaque soir la **liste des arrivées du lendemain** (résident, logement, bail signé, dépôt payé), pour accueillir même si le logiciel de gestion locative ou l'application sont indisponibles. Prévoir une astreinte d'un responsable les samedis de rentrée, l'accueil prolongé les jours de pointe et quelques chambres d'hôtel réservées en dernier recours. Les 38 résidences à badges gardent un stock de badges | 120 résidents bloqués six heures ; aucune clé de secours ; clés activées seulement à l'arrivée |
| Signature du bail | si le prestataire de signature ou le logiciel de gestion locative est indisponible, **prolonger d'office la réservation** de 48 heures du logement et en prévenir le candidat, pour ne perdre ni le candidat ni le logement ; préparer les baux à partir de la liste des attributions extraite chaque soir ; signer dès le rétablissement, en priorité ceux des arrivées les plus proches | jusqu'à 80 baux par jour, logement réservé 48 heures |

**Objectifs de durée d'interruption (RTO) et de perte de données (RPO)** (a-3) :

| Ressource | RTO en rentrée | RTO d'octobre à mai | RPO | Justification |
|---|---|---|---|---|
| Service de clé virtuelle | une heure les jours d'arrivée, tenue grâce au mode dégradé | une journée | aucune perte des clés activées : sauvegarde de la liste des clés à exiger du prestataire (engagement ci-dessous) | analyse d'impact de la remise des accès |
| Signature électronique | 24 heures | deux à trois jours | aucun bail signé perdu : le prestataire conserve les baux | réservation de 48 heures |
| Logiciel de gestion locative | quatre heures | 24 heures | **une heure** en rentrée ; 24 heures hors rentrée, ce que la sauvegarde de la nuit permet | en rentrée, perdre une journée, ce sont jusqu'à 80 attributions et baux à reconstituer, et de nouvelles doubles attributions ; l'hébergeur ne s'engage aujourd'hui qu'au « jour ouvré suivant », ce qu'il faut renégocier pour la rentrée |

**Engagement à obtenir du prestataire de la clé virtuelle** (a-4) : souscrire l'**assistance sept jours sur sept de juin à octobre** avec un **rétablissement en deux heures au plus**. Environ 20 k€ par an représentent moins de 0,5 % des 4,5 M€ de dépenses du système d'information, pour le processus le plus sensible de la rentrée. Ces deux heures dépassent l'heure admissible : seul le mode dégradé (activation la veille, clés de secours) couvre l'écart. Le contrat doit aussi prévoir :
- l'information immédiate d'ORVANELLE en cas d'incident ;
- une disponibilité mesurée et communiquée, avec des pénalités ;
- le plan de continuité du prestataire et la sauvegarde de la liste des clés ;
- la conservation des journaux des serrures pendant plusieurs mois (risque R2) ;
- la fourniture de mises à jour de sécurité des serrures. Le règlement sur la cyberrésilience en fait une obligation des fabricants, en principe, avec une application générale le 11/12/2027 (annexe 3.5), ce qui facilite cette exigence d'achat ;
- un exercice commun chaque année avant la rentrée.

**Exercices** (a-4) :
- avant le 1er juin, **restaurer pour la première fois une sauvegarde** du logiciel de gestion locative chez l'hébergeur, et mesurer le temps réel de reprise (PRA) ;
- fin juin, puis avant le premier samedi de pointe (21 août), un **exercice « panne de la clé virtuelle un samedi »** dans deux ou trois résidences, avec les chargés d'accueil, saisonniers compris : coffre, registre, liste papier, astreinte, hôtel ;
- un exercice de prolongation des réservations quand la signature est indisponible ;
- après chaque exercice, un retour d'expérience et la mise à jour du plan.

Le plan est porté par le membre du directoire chargé des opérations, coordonné par la direction des systèmes d'information et appliqué par la direction des résidences (ISO 22301:2019 en principe).

*3.2 b) – Trois mesures de sécurité hiérarchisées pour la rentrée 2027*

1. **Authentification à deux facteurs pour les comptes de l'application qui portent une clé virtuelle**, avec réinitialisation des comptes compromis, alerte de connexion depuis un nouveau téléphone et journaux des serrures conservés plusieurs mois (risque R2) ; en service avant le premier samedi de pointe, le 21 août 2027. **Justification du premier rang** : criticité maximale (16) ; la clé ouvre un logement, la sécurité physique des résidents est en jeu, et la faille a déjà été exploitée 200 fois en deux mois ; la mesure protège aussi les données des résidents, objectif du plan « ORVANELLE 2030 ».
2. **Paiement du dépôt de garantie dans le seul espace personnel du portail**, rappel systématique qu'aucune coordonnée bancaire n'est envoyée par courriel, contre-appel possible et alerte des familles dès le premier signalement (risque R1) ; avant le 1er juin, puisque les fraudes ont eu lieu en juillet et en août.
3. **Fin de la circulation des pièces par courriel** : dépôt des pièces sur le portail, purge des messageries, fermeture des comptes des saisonniers à la fin de leur contrat et sensibilisation des équipes au hameçonnage (risque R5) ; elle réduit aussi les informations dont se servent les fraudeurs de R1, et l'audit de la question 3.3 en fixera les règles.

**Réponses tolérées**
- Fraude au dépôt de garantie placée au premier rang, au titre de sa fréquence, de son coût faible et de sa rapidité de mise en œuvre, si la mesure sur les comptes suit immédiatement.
- Troisième mesure portant sur la capacité du portail (file d'attente, ouverture des réservations étalée par ville) ou sur la double attribution (attribution validée en temps réel), si elle est reliée à son risque ; la capacité du portail ne relève pas d'un paramétrage attendu de la copie.
- RTO et RPO voisins, s'ils sont justifiés par l'analyse d'impact et différenciés selon la saison ; refus de l'option du prestataire, si l'écart est couvert par un mode dégradé explicite.
- Mention de la notification d'une violation de données pour les 200 comptes, en principe, sans délai ni analyse juridique.

**Erreurs fréquentes**
- *PCA et PRA confondus* (`ET-02`, `JUR-S02`) — juste : le PCA maintient pendant la crise, le PRA restaure ensuite.
- *RTO et RPO inversés ou fixés sans lien avec l'analyse d'impact* (`ET-03`) — juste : une heure pour les accès un samedi de rentrée, une heure de perte de données au plus pour les attributions en rentrée.
- *Plan jamais exercé* (F12 § 4) — juste : sauvegarde restaurée et exercice de panne avant la rentrée.
- *Mesures techniques détaillées, réglages ou tests techniques de sécurité* (`JUR-T12`) — juste : mesures organisationnelles, contractuelles et de gestion des accès.
- *Engagement du prestataire présenté comme suffisant* — juste : deux heures de rétablissement ne tiennent pas l'heure admissible sans mode dégradé, sauf si le candidat a retenu une durée admissible de deux heures et prévoit malgré tout un mode dégradé.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| PCA, PRA, RTO, RPO, exercices | maintien en mode dégradé, reprise, objectifs | F12 § 4 | notion de cours |
| ISO 22301:2019 | norme d'exigences de la continuité d'activité | `iso_22301_2019` ; F12 § 4 | en vigueur |
| ISO/IEC 27001:2022 | mesures de contrôle d'accès, de sauvegarde, de relations avec les fournisseurs | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Authentification à deux facteurs, gestion des identités | au moins deux facteurs de nature différente | F12 § 3 | notion de cours |
| Règlement (UE) 2024/2847 sur la cyberrésilience (CRA) | mises à jour de sécurité fournies par les fabricants ; application générale le 11/12/2027 | `cra` ; F12 § 7 | applicable le 11/12/2027 ; article 14 depuis le 11/09/2026 |

---

### 3.3 – L'audit du traitement des dossiers de candidature (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance » ; `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes » ; `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; le droit des données personnelles (droits des personnes, bases légales) relève de l'UE 1.

**Annexes mobilisées** : annexe 3.3 (traitement, liste des pièces, constats de la déléguée, demande du directoire), annexe 3.1 (pièces conservées dans les messageries, comptes des saisonniers), annexe 3.5 (RGPD en principe, ISO/IEC 27001:2022) et annexe 1.1 (logiciel de gestion locative, effectif des résidences, organigramme sans audit interne).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit de conformité d'un processus du SI défini (examen indépendant, référentiel, écarts, risques, recommandations) ; la distinction avec l'audit légal est un plus, non exigé | 0,5 |
| a-2 | Objectifs (conformité, sécurité, règles pour le nouveau logiciel) et périmètre (de la réception des pièces à leur suppression, messageries, logiciel, prestataire) | 0,5 |
| a-3 | Étapes, livrables et calendrier réaliste sur les six semaines, avant le 1er juin | 0,5 |
| a-4 | Preuves à demander, reliées aux constats | 0,5 |
| b-1 | Quatre critères de conformité et de sécurité, chacun précisé par ce qui est attendu | 0,5 |
| b-2 | Situation actuelle appréciée pour chacun à partir de l'annexe 3.3, avec le risque et la priorité | 0,5 |

**Réponse attendue**

*3.3 a) – Le cadrage de l'audit*

**Définition** (a-1) : l'**audit de conformité d'un processus du système d'information** est un examen indépendant et méthodique qui compare le fonctionnement réel du processus (pratiques, données, accès, prestataires, documentation) à un **référentiel** de règles (texte, norme, politique interne), relève les **écarts**, en apprécie les **risques** et formule des **recommandations** hiérarchisées (F10 § 1.1). Ici, c'est un audit externe contractuel commandé par le directoire. Son référentiel réunit les principes du RGPD (annexe 3.5), les règles internes et les mesures d'ISO/IEC 27001:2022 sur le contrôle d'accès et les fournisseurs. Il ne s'agit ni de l'audit légal des comptes, ni d'un audit de la performance commerciale.

**Objectifs** (a-2) :
- apprécier la **conformité** du traitement aux principes de minimisation, de limitation de la conservation, de sécurité, de tenue du registre et d'encadrement des sous-traitants ;
- apprécier la **sécurité** des dossiers, partout où ils se trouvent ;
- hiérarchiser les écarts et les risques ;
- proposer les **règles à intégrer au paramétrage** du nouveau logiciel de gestion locative en septembre 2027 (pièces demandées, profils d'accès, durées de conservation), et les mesures immédiates à prendre avant l'ouverture des réservations du 1er juin.

**Périmètre** (a-2) : le traitement des dossiers de candidature, de la réception des pièces à leur suppression :
- le portail, les messageries du centre de relation résidents et des chargés d'accueil, le logiciel de gestion locative (dossiers conservés depuis 2009) et la transmission au prestataire de vérification des garants ;
- les candidats et les garants, retenus ou non ;
- la campagne 2026 et le stock de dossiers ;
- les acteurs : centre de relation résidents, chargés d'accueil, direction commerciale et de la relation résidents, direction des systèmes d'information, déléguée à la protection des données.

Sont exclus : la clé virtuelle et l'application des résidents, le paiement, le contenu du bail, le choix du logiciel, l'audit sur place du prestataire, et toute analyse juridique.

**Étapes, calendrier et livrables** (a-3) :

| Semaine | Étape | Livrable |
|---|---|---|
| 1 (12-16 avril) | **cadrage** : lettre de mission signée par la présidente du directoire (objectifs, périmètre, référentiel, accès garantis aux systèmes et aux messageries, confidentialité, interlocuteurs, calendrier) ; réunion de lancement ; collecte des documents | lettre de mission |
| 2 (19-23 avril) | **prise de connaissance** : entretiens avec la déléguée, M. CALVÉRAC, le centre de relation résidents, des chargés d'accueil de deux ou trois résidences et la direction des systèmes d'information ; **cartographie du processus et des lieux où se trouvent les données** ; analyse des risques ; programme de travail | cartographie du processus, programme de travail |
| 3 et 4 (26 avril-7 mai ; semaine de quatre jours du 3 au 7 mai, jeudi 6 mai férié) | **collecte et examen** : revue documentaire, sondage sur un échantillon de dossiers, examen des comptes et des profils, inventaire des messageries, questionnaire au prestataire | dossier de travail |
| 5 (10-14 mai) | **analyse** des écarts, feuilles de constats (constat, cause, risque, recommandation, priorité, responsable, échéance), **validation contradictoire** avec les audités | feuilles de constats validées |
| 6 (18-21 mai ; lundi 17 mai férié) | **rapport**, note de synthèse et **restitution** au directoire le 21 mai ; plan d'action en deux temps : mesures avant le 1er juin, règles pour le paramétrage de septembre | rapport, note de synthèse, plan d'action |

Le suivi du plan d'action revient ensuite à la déléguée et à la direction des systèmes d'information. La mission doit s'achever avant le 1er juin, pour ne pas gêner la campagne et pour que les mesures immédiates s'appliquent dès l'ouverture des réservations.

**Preuves à demander** (a-4) :
- la liste des pièces et, pour chacune, l'étape qui s'en sert ;
- le registre des activités de traitement (version de 2022) et l'inventaire réel des traitements ;
- le bon de commande du prestataire de vérification des garants et ses réponses écrites sur le lieu, la durée de conservation, la protection et les éventuels autres sous-traitants des données ;
- l'extraction des comptes et des profils du logiciel de gestion locative, avec la date de dernière connexion et la date de fin de contrat des 40 saisonniers ;
- les journaux d'accès aux dossiers ;
- un échantillon d'une trentaine de dossiers de 2026, retenus et non retenus ;
- le décompte des dossiers conservés par année et par statut (environ 150 000, dont 60 000 de candidats jamais devenus résidents) et l'inventaire des pièces jointes des messageries ;
- les procédures écrites (départ des saisonniers, revue des comptes) ;
- la liste des projets non soumis à la déléguée depuis 2023.

*3.3 b) – Quatre critères de conformité et de sécurité appréciés* (quatre sont attendus ; cinq sont proposés)

| Critère | Ce qui est attendu | Situation actuelle (annexe 3.3) | Appréciation |
|---|---|---|---|
| **Minimisation des pièces demandées** | chaque pièce sert à une étape identifiée de la décision ou de la gestion du séjour ; la liste est validée avec la déléguée | liste de 2019 fixée sans la déléguée ; trois pièces sur dix types inutiles selon elle (photo, relevés de compte du garant, livret de famille) ; « plus on en demande… » | **non conforme** ; risque réglementaire et d'exposition accrue en cas de fuite ; priorité 1 avant le 1er juin, car corriger la liste ne coûte rien |
| **Registre des activités de traitement à jour** | chaque traitement inscrit avec ses finalités, ses catégories de données et de personnes, ses destinataires, ses durées et ses mesures de sécurité ; revue à chaque projet | dernière mise à jour en 2022 ; ni la clé virtuelle, ni le prestataire de vérification, ni les messageries ; déléguée consultée sur aucun projet depuis 2023 | **non conforme** ; c'est aussi un défaut de gouvernance : la déléguée est tenue à l'écart des projets ; priorité 2 |
| **Encadrement du sous-traitant** | contrat écrit fixant les instructions, la sécurité, la confidentialité, le sort des données en fin de contrat, les audits ; transmission sécurisée | simple bon de commande ; lieu et durée de conservation inconnus ; 3 000 dossiers de garants envoyés par courriel en 2026 | **non conforme**, risque élevé (bulletins de salaire, avis d'imposition) ; priorité 1 : contrat avant la campagne, ou suspension des envois |
| **Accès aux dossiers limités au besoin** | comptes nominatifs, profil limité à la résidence de rattachement, comptes fermés au départ, revue périodique | profil « chargé d'accueil » ouvert aux 60 résidences pour 120 personnes ; 40 comptes de saisonniers ouverts après leur départ ; aucune revue depuis 2021 | **non conforme** ; à fixer dans les profils du nouveau logiciel ; fermeture des 40 comptes immédiate |
| **Durée de conservation définie et appliquée** | une durée par catégorie (candidat non retenu, résident, garant), puis suppression ou archivage | aucune durée ; environ 150 000 dossiers depuis 2009, dont environ 60 000 (40 %) de candidats jamais devenus résidents ; 1,5 million de pièces jointes dans les messageries | **non conforme** ; stock à purger et durées à paramétrer dans le nouveau logiciel |

Appréciation d'ensemble : aucun des critères n'est satisfait. Les deux priorités sont l'encadrement du prestataire et l'arrêt de la circulation des pièces par courriel, qui concentrent les données les plus sensibles hors de tout contrôle.

**Réponses tolérées**
- Démarche en cinq à sept étapes (cadrage, prise de connaissance, analyse des risques, programme, collecte, restitution, suivi), si elle tient dans les six semaines et respecte l'échéance du 1er juin.
- Critère de sécurité des transmissions (courriel non protégé) ou de gouvernance (place de la déléguée) à la place de l'un des cinq thèmes, s'il est appliqué aux constats.
- Appréciation graduée (« partiellement conforme » pour le registre, qui existe), si elle est justifiée.
- Référentiel complété par COBIT 2019 pour la gouvernance, si la distinction avec ISO/IEC 27001 est juste.

**Erreurs fréquentes**
- *Méthodologie incomplète* (`JUR-A01`) — juste : objectifs, périmètre, référentiel, étapes, livrables et calendrier.
- *Audit du SI confondu avec l'audit légal* (`ET-34`) — juste : audit contractuel de conformité d'un processus, commandé par le directoire.
- *Dérive vers le droit des données personnelles* (droits des personnes, bases légales, sanctions de l'autorité de contrôle) (UE 1, F15 § 9) — non attendue : l'audit porte sur l'organisation (registre, sous-traitant, accès, conservation).
- *Déléguée à la protection des données chargée de conduire l'audit* (`ET-29`) — juste : elle est auditée sur le registre et doit être entendue ; l'auditeur externe garantit l'indépendance.
- *Liste légale de pièces exigibles* — non attendue : la minimisation s'apprécie au regard de l'usage de chaque pièce.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Démarche d'audit du SI, livrables | cadrage, prise de connaissance, risques, collecte, restitution, suivi | F10 § 1.1 et § 1.2 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) | minimisation, conservation, sécurité, registre, sous-traitant, en principe | `rgpd` ; F15 § 2 et § 5 | applicable depuis le 25/05/2018 |
| ISO/IEC 27001:2022 | contrôle d'accès, relations avec les fournisseurs | `iso_27001_2022` ; F12 § 2 | en vigueur |
| Déléguée à la protection des données, registre | missions, indépendance, tenue du registre | F15 § 1 et § 2 | notion de cours |

---

### 3.4 – Le pilotage de l'énergie des résidences (3 points)

**Référence au programme**
- §4.3 – Intégrer les enjeux de durabilité et de sobriété numérique dans le management des SI : `4.3.a` « Déployer une stratégie SI responsable en intégrant les principes de durabilité, de sobriété numérique et les exigences réglementaires en matière de RSE et de performance environnementale » ; `4.3.e` « Outils et indicateurs de mesure de l'impact environnemental des SI » ; `4.3.f` « Stratégies de transition numérique responsable (cloud éthique, datacenters verts, réduction de l'empreinte carbone) ». Limites : la durabilité est intégrée à la gouvernance globale du SI ; aucun calcul d'empreinte n'est attendu.

**Annexes mobilisées** : annexe 3.4 (consommations 2025 et 2026, écarts entre résidences, projet, choix proposés), annexe 3.5 (RGESN, règlement sur la cyberrésilience, RGPD en principe) et annexe 1.1 (objectif de 20 %, parc porté à 12 000 logements, application des résidents).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Green IT et IT for green définis et distingués ; projet situé (IT for green, avec une empreinte propre) | 0,5 |
| a-2 | Leviers du projet tirés de l'annexe, contribution chiffrée de tête (environ 9 à 15 % du total) et conditions (autres leviers, objectif à préciser, résidents) | 0,5 |
| b-1 | Indicateur complet rapporté à la référence 2025 et à une cible 2030 | 0,5 |
| b-2 | Second indicateur complet, relié au cas | 0,5 |
| c-1 | Empreinte du dispositif appréciée sans calcul (fabrication et renouvellement des boîtiers, volume et conservation des données, hébergement, effet rebond) | 0,5 |
| c-2 | Trois mesures de sobriété sur les choix de l'annexe 3.4 C, justifiées | 0,5 |

**Réponse attendue**

*3.4 a) – Green IT, IT for green et contribution du projet à l'objectif*

**Définitions** (a-1) : le **Green IT** réduit l'empreinte environnementale **du système d'information lui-même** : équipements, centres de données, logiciels, données et usages. L'**IT for green** met le numérique **au service de la réduction de l'empreinte de l'organisation** : capteurs, pilotage, mesure (F14 § 3). Le projet de pilotage de l'énergie relève de l'**IT for green** : il vise la consommation des bâtiments, qui représente environ 7 M€ par an. Mais il ajoute 9 000 boîtiers, des robinets, une plateforme et des données : il a sa propre empreinte, qui relève du Green IT (question c). Une stratégie responsable du système d'information traite les deux ensemble.

**Comment le projet sert l'objectif** (a-2) :
- il **chauffe seulement quand c'est utile** : il baisse le chauffage dans les logements vides, dont les quelque 630 logements vacants, et quand la fenêtre est ouverte, au lieu de deux réglages manuels par an ;
- il **mesure et compare** : les écarts de un à trois entre résidences comparables (de 3 000 à 9 000 kWh par logement) désignent où agir d'abord (résidences C et D) et quels travaux discuter avec les propriétaires ;
- il **informe les résidents**, qui ne connaissent pas aujourd'hui leur consommation.

**Contribution** : le chauffage pèse 60 % de la consommation, et le gain annoncé est de 15 à 25 % du chauffage, soit environ **9 à 15 % de la consommation totale** (de tête : 0,6 × 15 et 0,6 × 25). Le projet ne suffit donc pas seul à atteindre 20 %, et le gain annoncé par le prestataire reste à vérifier. La baisse de 2 % de 2026 tient surtout à la météo.

**Conditions** :
- **Préciser l'objectif.** Avec 12 000 logements en 2030, une baisse de 20 % de la consommation totale (36 000 MWh) exigerait 3 000 kWh par logement, soit 40 % de moins qu'en 2025. La cible doit donc porter sur la **consommation par logement** (4 000 kWh), mesurée à climat comparable, et le directoire doit l'écrire.
- **Agir aussi sur les autres leviers** : l'eau chaude (20 %), les autres usages (20 %) et les travaux, avec les propriétaires.
- **Associer les résidents** : confort, information, transparence sur les capteurs de présence, qui révèlent leur vie quotidienne et sont des données personnelles à limiter au strict besoin.
- **Associer la direction des systèmes d'information** au choix de la plateforme, à son raccordement à l'application et à la sécurité des boîtiers.
- **Mesurer les résultats** et maîtriser l'empreinte du dispositif.

*3.4 b) – Deux indicateurs de suivi*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Consommation d'énergie par logement géré** (b-1) | consommation d'énergie des résidences sur les douze derniers mois (kWh, chauffage, eau chaude et autres usages) / nombre moyen de logements gérés sur la période, présentée aussi à climat comparable | factures et relevés des fournisseurs d'énergie, puis plateforme de données énergétiques ; nombre de logements : logiciel de gestion locative | mensuelle, en cumul sur douze mois glissants ; revue annuelle par le directoire | **4 000 kWh par logement en 2030**, soit 20 % de moins que la **référence 2025 de 5 000 kWh** (4 900 kWh en 2026) ; jalon de 4 400 kWh en 2028 | environnement |
| **Écart de consommation entre résidences comparables** (b-2) | consommation par logement de la résidence la plus consommatrice / consommation par logement de la moins consommatrice, dans chaque groupe de résidences comparables | plateforme de données énergétiques et relevés des fournisseurs, par résidence | trimestrielle | rapport inférieur à 1,5 en 2029, contre 3 en 2026 (9 000 contre 3 000 kWh par logement) | processus |

Le premier indicateur rapporté au logement neutralise la croissance du parc ; présenté à climat comparable, il évite d'attribuer au projet un effet de la météo.

*3.4 c) – L'empreinte du dispositif et trois mesures de sobriété*

**Empreinte du dispositif lui-même** (c-1), sans calcul :
- la **fabrication** de 9 000 boîtiers électroniques, des robinets commandés et des équipements de transmission. Pour des équipements électroniques, la fabrication pèse souvent davantage que leur propre consommation (F14 § 1). Renouvelés entiers tous les cinq ans, les boîtiers à pile non remplaçable obligeraient à en fabriquer 18 000 en dix ans, piles comprises, au lieu de 9 000 ;
- le **volume de données** : environ 40 millions de mesures par jour, conservées au détail pendant dix ans et copiées dans deux centres de données, soit un stockage et des traitements qui ne cessent de croître ;
- l'**hébergement**, dont ni la consommation ni l'origine de l'électricité ne sont connues ;
- l'**effet rebond** : un logement mieux chauffé peut conduire à relever les consignes.

Le dispositif doit rester petit au regard de l'énergie qu'il fait économiser. La plupart de ces choix ne répondent à aucun besoin démontré : la sobriété commence par questionner ce besoin.

**Trois mesures de sobriété** (c-2 ; quatre sont proposées) :
1. **Fréquence** : une mesure par quart d'heure, ou une transmission au changement d'état (fenêtre ouverte, présence), au lieu d'une par minute, soit quinze fois moins de mesures (environ 2,6 millions par jour). C'est largement suffisant pour piloter un chauffage réglé aujourd'hui deux fois par an et pour la comparaison quotidienne.
2. **Conservation** : garder le détail treize mois, pour comparer une saison de chauffe à la précédente, puis seulement des agrégats (journaliers par logement, mensuels par résidence). Les données de présence au détail sont supprimées vite, ce qui sert aussi la minimisation des données personnelles (annexe 3.5).
3. **Durée de vie** : choisir le **boîtier à pile remplaçable garanti dix ans** (9 000 boîtiers en dix ans au lieu de 18 000). Exiger à l'achat la réparabilité, la reprise et le recyclage, et la fourniture de mises à jour de sécurité pendant toute la durée de vie, que le règlement sur la cyberrésilience met à la charge des fabricants, en principe, à compter du 11/12/2027.
4. **Hébergement** : exiger du prestataire la consommation et l'origine de l'électricité de ses centres de données, un hébergement dans l'Union européenne, une seule copie complète des données agrégées et une sauvegarde proportionnée au besoin, conformément au thème « hébergement » du RGESN.

**Réponses tolérées**
- Second indicateur différent, s'il est complet et relié au cas : part des heures de chauffage dans des logements vides ou à fenêtre ouverte ; part des logements équipés et pilotés (avancement) ; volume de données stockées par la plateforme ou consommation de la plateforme (Green IT).
- Cible par logement fixée sans correction climatique, si l'effet de la météo est signalé ; objectif lu en consommation totale, si la conséquence de la croissance du parc est expliquée.
- Gain du projet exprimé en fourchette voisine, ou jugé incertain faute de vérification, si la part du chauffage est utilisée.
- Mesures classées dans un autre ordre, ou quatrième mesure à la place de l'une des trois, si chacune répond à un choix de l'annexe 3.4 C.

**Erreurs fréquentes**
- *Green IT et IT for green confondus, ou sobriété réduite à l'économie d'énergie* (`ET-12`) — juste : le projet réduit l'énergie des bâtiments (IT for green) mais doit lui-même être sobre (Green IT), et la sobriété questionne d'abord le besoin.
- *Empreinte réduite à l'électricité* (`ET-38`) — juste : la fabrication et le renouvellement de 9 000 boîtiers comptent dans l'empreinte au même titre que l'électricité des centres de données, et la fabrication domine souvent pour des équipements électroniques (F14 § 1).
- *Indicateur incomplet ou générique* (`ET-18`, `JUR-A02`) — juste : formule, source, fréquence, cible et axe, avec la référence 2025 et la cible 2030.
- *Projet présenté comme suffisant pour atteindre 20 %* (`JUR-T03`) — juste : environ 9 à 15 % du total, à vérifier, et d'autres leviers nécessaires.
- *Calcul d'empreinte tenté, règle de performance énergétique des bâtiments ou cadre de durabilité invoqué* — non attendus.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Green IT, IT for green, sobriété, durée de vie | définitions, fabrication des équipements, effet rebond | F14 § 1 et § 3 | notion de cours |
| Indicateurs d'impact, référence et cible | kWh, trajectoire | F14 § 4 | notion de cours |
| RGESN, version 2024 | thème « hébergement », écoconception | `rgesn_2024` ; F14 § 2 | en vigueur |
| Règlement (UE) 2024/2847 sur la cyberrésilience (CRA) | mises à jour de sécurité fournies par les fabricants | `cra` ; F12 § 7 | applicable le 11/12/2027 ; article 14 depuis le 11/09/2026 |
| Règlement (UE) 2016/679 (RGPD) | minimisation des données de présence, en principe | `rgpd` ; F15 § 4 | applicable depuis le 25/05/2018 |
