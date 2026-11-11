# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 5 – Management des systèmes d'information — Exercice d'entraînement n° 12 — Dossier 3 (13 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F10 audit et fiabilisation, F15 RGPD opérationnel, F01 alignement stratégique et veille, F02 gouvernance et comitologie, F13 intelligence artificielle, F14 numérique responsable, et `ue5/fiches/referentiels_dates.yaml` (vérifiés les 25 et 26/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (structure et traçabilité des questions, indicateurs, référentiels datés, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des modèles et des référentiels, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la justesse des définitions, leur application aux annexes, la pertinence et la priorisation des recommandations, et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet). Le corrigé officiel du sujet zéro ne donne les points que par question : la répartition par sous-question et par item est une proposition.

| Question | Compétence visée | Points |
|---|---|---|
| 3.1 Démarche de la mission d'audit du portail | `3.2.a` Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance ; `3.2.b` Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes | 2 |
| 3.2 Appréciation et diagnostic d'audit | `3.2.c` Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. ; `3.2.d` Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse | 3 |
| 3.3 Veille technologique et stratégie de la relation numérique | `1.1.a` Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes ; `1.1.d` Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques | 5 |
| 3.4 Gouvernance de la relation numérique | `1.2.a` Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité ; `1.2.c` Enjeux relationnels entre DSI, direction générale et directions métiers | 3 |
| **Dossier 3 – Auditer le portail des abonnés et orienter la stratégie de la relation numérique** |  | **13** |

Répartition indicative : connaissances (audit du SI, critères d'appréciation, veille technologique active, stratégie du SI alignée, principes de gouvernance) 2,25 points (items 3.1 a-1, 3.2 a pour moitié, 3.3 a-1, 3.3 c-1, 3.4 b pour un quart) ; analyse des annexes et recommandations 10,75 points, soit environ 83 %. Durée conseillée : 13 points × 4,5 minutes = 58,5 minutes, soit 58 minutes (le temps restant de l'épreuve, après 1 h 03 et 59 min pour les dossiers 1 et 2).

---

### 3.1 – Démarche de la mission d'audit du portail (2 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.a` « Conduire des missions d'audit et de contrôle des systèmes d'information afin d'évaluer leur performance, leur conformité réglementaire et la qualité de leur gouvernance » ; `3.2.b` « Méthodologies d'audit SI : cartographie des processus, évaluation des risques, contrôles internes ». Limites : l'exécution de tests techniques détaillés n'est pas attendue ; « La conformité financière et comptable n'est pas traitée dans le programme de l'UE 5 » ; « L'audit SI suppose une approche multidisciplinaire et une posture critique vis-à-vis de la gouvernance ».

**Annexes mobilisées** : annexes 3.1 (fonctions, organisation, échanges avec la facturation, chiffres), 3.2 (constats, repères) et 1.1 (organigramme).

**Barème indicatif (2 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Audit du SI défini (examen indépendant et méthodique, au regard d'un référentiel, de la gouvernance, de la performance, de la sécurité et de la conformité du SI, conclu par des recommandations) | 0,5 |
| a-2 | Démarche appliquée au portail : objectifs de performance et de conformité, périmètre (inclus et exclus), étapes de la mission jusqu'au suivi, avec référentiels et livrables | 0,5 |
| b-1 | Cartographie du processus en cinq étapes, avec l'acteur et l'application de chaque étape (les échanges entre portail et facturation sont valorisés, non exigés) | 0,5 |
| b-2 | Trois contrôles internes précis, chacun rattaché à une étape ; 0,5 dès deux contrôles précis et rattachés | 0,5 |

Une copie qui énonce les étapes de la mission en une ligne chacune, avec au moins un livrable, obtient l'item a-2 : le détail de la réponse ci-dessous est indicatif, au regard des neuf minutes que laisse la question.

**Réponse attendue**

*3.1 a) – Définition et démarche de la mission*

L'**audit du système d'information** est un examen indépendant et méthodique qui apprécie, au regard d'un référentiel (COBIT 2019, RGPD, contrat, engagements internes), la gouvernance, la performance (efficacité, efficience), la sécurité et la conformité d'un système ou d'un processus, et qui conclut par des recommandations hiérarchisées (F10 § 1.1). Il évalue le dispositif de contrôle interne sans s'y substituer (0,5 pt).

Appliqué au portail (0,5 pt) :
- **Mandant et auditeur** : la directrice générale, qui veut présenter les conclusions au conseil d'administration de juin 2027 ; le chargé de mission, rattaché à elle et indépendant de la direction de la clientèle et de la DSI, appuyé par la déléguée à la protection des données pour le volet RGPD.
- **Objectifs de performance** : fiabilité des données et des échanges entre le portail et la facturation (doublons, rejets, paiements enregistrés en retard) ; disponibilité au regard de l'engagement contractuel de 99,5 % ; efficacité du traitement des réclamations au regard de l'engagement de 8 jours ; satisfaction des utilisateurs (62 %, contre 75 % à l'accueil).
- **Objectifs de conformité** : RGPD (fiche du registre, durées de conservation, protection des données par défaut dans les choix d'alertes, contrat de sous-traitance avec VELIZANE) ; respect du contrat de l'éditeur et de la charte de service ; qualité de la gouvernance du portail (qui décide des évolutions).
- **Périmètre** : les six fonctions du portail, le module de prise de rendez-vous, les échanges de la nuit avec le logiciel de facturation et l'import des données de télérelève ; les processus « de la souscription au paiement » et de traitement des réclamations ; les acteurs (direction de la clientèle, accueil et centre d'appels, DSI, déléguée à la protection des données, VELIZANE) ; l'exercice 2026 et le début de 2027. **Exclus** : la sécurité technique de la solution de l'éditeur (aucune diligence technique sur ses serveurs), la supervision des installations, la tenue de la comptabilité.
- **Étapes** (six semaines environ, de mars à mi-avril 2027) : (1) **cadrage** : lettre de mission signée par la directrice générale (objectifs, périmètre, référentiels — COBIT 2019 pour la gouvernance et les services, ITIL pour les niveaux de service et les changements, RGPD, contrat VELIZANE, charte de service —, calendrier) ; (2) **prise de connaissance** : entretiens avec Mmes FARGEMONT, CORVESSE et BARJOLLE, des agents de l'accueil et l'agent de la DSI chargé des échanges, revue du contrat, du registre, des comptes rendus d'arbitrage ; (3) **analyse des risques** : cartographie du processus (question b) et des points de contrôle ; (4) **programme de travail et collecte** : revue documentaire, examen de la matrice des droits du portail, rapprochement sur échantillon des fichiers de plusieurs nuits avec la facturation, sondage sur les réclamations clôturées et sur les comptes d'anciens abonnés, analyse des relevés de disponibilité ; (5) **restitution** : constats validés contradictoirement avec les directions, diagnostic d'audit et note de synthèse à la directrice générale ; (6) **suivi** : plan d'action (responsable, échéance), point d'étape à six mois.
- **Livrables** : lettre de mission, cartographie du processus et des risques, programme de travail, feuilles de constats, diagnostic et note de synthèse, plan d'action.

*3.1 b) – Cartographie du processus « de la souscription au paiement » et contrôles internes*

| Étape | Acteur | Application | Échanges et points de risque |
|---|---|---|---|
| 1. Souscription du contrat | abonné (en ligne) ou agent de l'accueil | portail VELIZANE, puis logiciel de facturation | création du compte et transmission nocturne du contrat à la facturation ; risque de doublon (4 000 abonnés à deux comptes), de rejet |
| 2. Gestion du contrat (mensualisation, coordonnées bancaires, choix des alertes) | abonné ou agent de l'accueil et du centre d'appels | portail, puis facturation | modification des coordonnées bancaires par un profil unique de 35 agents ; choix d'alertes coché d'avance |
| 3. Relevé de la consommation | releveurs ou plateforme de télérelève ; service de la facturation | logiciel de facturation (index), portail (consommation affichée) | index relevés deux fois par an ou importés chaque mois |
| 4. Facturation et mise à disposition de la facture | service de la facturation | logiciel de facturation, puis portail (facture, alerte) | transmission nocturne au portail ; pics de connexion lors des deux vagues de facturation |
| 5. Paiement et suivi du compte | abonné ; prestataire de paiement ; service de la facturation | portail et prestataire de paiement, puis facturation | paiement transmis la nuit à la facturation ; rejets repris à la main en huit jours ; relances envoyées à tort |

La réclamation (portail, téléphone, accueil) peut intervenir à chaque étape ; la résiliation ferme la boucle et ouvre la question de la conservation des données (0,5 pt pour la cartographie).

Trois contrôles internes à vérifier (0,5 pt) :
1. **Étape 1 — contrôle d'unicité à la souscription** : avant la création d'un compte, rapprochement automatique avec les contrats existants (numéro de contrat, adresse du point de comptage) ; l'auditeur vérifie son existence et son effectivité sur un échantillon d'emménagements de 2026 (constat 1).
2. **Étape 5 (et 1, 2) — contrôle des échanges entre le portail et la facturation** : comptage des enregistrements et totaux de contrôle de chaque fichier, journal des rejets, délai et responsable de leur traitement, rapprochement des paiements reçus sur le portail et enregistrés dans la facturation ; l'auditeur rapproche les fichiers de quelques nuits (constat 1).
3. **Étape 2 — contrôle des habilitations** : profils séparés selon le moindre privilège, validation par un second agent de toute modification de coordonnées bancaires, confirmation à l'abonné, revue périodique des droits ; l'auditeur examine la matrice des droits et le journal des modifications (constat 5).

**Réponses tolérées**
- Démarche en cinq ou sept étapes (fusion de l'analyse des risques et du programme de travail, ou étape distincte de validation contradictoire), si le cadrage, la collecte, la restitution et le suivi y figurent.
- Cartographie en schéma (couloirs par acteur, flèches) ou dans une notation de processus, si les cinq étapes, les acteurs et les applications apparaissent.
- Étapes découpées autrement (création du compte distinguée de la souscription ; relevé et facturation regroupés, paiement et relance distingués), si le processus va de la souscription au paiement.
- Autre contrôle pertinent : suivi des réclamations sans clôture automatique (constat 6), traçabilité des choix d'alertes (constat 3), purge des comptes clos (constat 4).
- Référentiel d'audit autre que COBIT 2019, s'il est adapté à l'objet (engagements de la charte de service, contrat de l'éditeur).

**Erreurs fréquentes**
- *Méthodologie d'audit incomplète* (`JUR-A01` méthodologie structurée : périmètre, objectifs, étapes, livrables, échéancier) — étapes sans périmètre, sans livrables ni calendrier.
- *Audit de sécurité ou diligences techniques* — examen des vulnérabilités de la solution, essais d'intrusion ou de montée en charge ; juste : les diligences portent sur les processus, les contrôles et les documents ; la sécurité n'est appréciée qu'au travers des habilitations et de la traçabilité.
- *Audit du SI confondu avec l'audit des comptes* (`ET-34`) — vérification de la régularité des encaissements ou des comptes de la régie ; juste : fiabilité des échanges et du service.
- *Contrôle interne confondu avec l'audit* — « l'auditeur contrôle chaque paiement » ; juste : l'audit apprécie la conception et l'effectivité des contrôles mis en place par les directions.
- *Cartographie sans acteurs ni applications* (`JUR-G07` cartographie de processus) — liste d'activités qui ne montre ni qui agit ni où transitent les données.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Audit du SI : définition, démarche, livrables | démarche de la mission | F10 § 1.1 et 1.2 | notion de cours |
| Contrôles applicatifs et contrôles des interfaces, habilitations | trois contrôles internes | F10 § 2 et 3.1 | notion de cours |
| COBIT 2019 (ISACA) | référentiel de gouvernance et de management | `cobit_2019` / F02 § 3 | en vigueur |
| ITIL (PeopleCert) | niveaux de service, changements | `itil` / F02 § 5 | en vigueur |

---

### 3.2 – Appréciation et diagnostic d'audit (3 points)

**Référence au programme**
- §3.2 – Auditer, contrôler et évaluer la performance et la conformité des systèmes d'information : `3.2.c` « Critères de performance et de conformité : fiabilité, efficacité, sécurité, conformité RGPD, etc. » ; `3.2.d` « Techniques de rédaction d'un diagnostic d'audit et d'une note de synthèse ».

**Annexes mobilisées** : annexes 3.2 (constats, repères au 31/12/2026) et 3.1 (chiffres, engagements, appels, satisfaction).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Quatre critères définis et chacun rattaché à au moins un constat de l'annexe 3.2 ; 0,5 pour deux ou trois critères | 1 |
| b-1 | Tableau de diagnostic pour quatre constats : critère juste, risque précis, recommandation opérationnelle, priorité ; 1 pour trois lignes, 0,5 pour deux | 1,5 |
| b-2 | Ordre de priorité justifié par des critères explicites (gravité, probabilité, nombre d'abonnés concernés, coût et délai de la mesure, caractère préalable aux projets du plan) | 0,5 |

**Réponse attendue**

*3.2 a) – Quatre critères d'appréciation*

| Critère | Définition | Constats rattachés (annexe 3.2) |
|---|---|---|
| **Fiabilité** | exactitude, complétude et cohérence des données et des traitements : une même information est juste et identique dans le portail et dans la facturation | 1 (4 000 abonnés à deux comptes, 150 rejets par nuit repris en huit jours, 900 paiements enregistrés en retard, 600 relances à tort) |
| **Efficacité** | atteinte des objectifs de service assignés au portail : disponibilité, délais, satisfaction (l'efficience rapporte en outre ces résultats aux moyens) | 2 (près de 90 heures d'interruption contre 45 au plus, dont 60 pendant les vagues de facturation) ; 6 (1 500 des 6 000 réclamations du portail, soit 25 %, clôturées sans réponse ; 18 jours pour un engagement de 8) |
| **Sécurité** | protection de la confidentialité, de l'intégrité et de la disponibilité des données, et traçabilité des actions | 5 (profil unique de 35 agents autorisés à modifier les coordonnées bancaires, sans validation ni revue ; deux modifications non demandées) |
| **Conformité au RGPD** | respect, démontrable, des obligations d'organisation du règlement : registre à jour, délais d'effacement définis, protection des données par défaut, contrat de sous-traitance, consultation du délégué à la protection des données | 4 (12 000 comptes d'anciens abonnés sans durée de conservation, dont 5 000 avec coordonnées bancaires ; pas de fiche au registre ; contrat muet sur le sort des données) ; 3 (case cochée d'avance, choix non tracé) |

(1 pt pour les quatre critères définis et rattachés ; 0,5 pt pour deux.)

*3.2 b) – Diagnostic d'audit*

| Constat | Critère | Risque | Recommandation | Priorité |
|---|---|---|---|---|
| **5 – Droits des agents** : profil unique pour 35 agents, modification des coordonnées bancaires sans validation ni information de l'abonné, aucune revue depuis 2020, deux modifications non demandées en 2026 | sécurité | détournement de prélèvements ou de remboursements par une modification frauduleuse ou erronée (déjà survenu deux fois) ; consultation abusive des données de 82 000 comptes ; actions sensibles non contrôlées | profils différenciés selon le moindre privilège (consultation pour tous ; modification des coordonnées bancaires réservée à quelques agents, validée par un second agent et confirmée à l'abonné par message ; clôture d'un compte ou d'une réclamation par un responsable) ; journal nominatif des modifications ; revue semestrielle des droits par la directrice de la clientèle avec la DSI | **1** — fin avril 2027 ; directrice de la clientèle et DSI |
| **1 – Doublons et échanges avec la facturation** : 4 000 abonnés à deux comptes, 150 rejets par nuit repris en huit jours, aucun total comparé, 900 paiements enregistrés en retard, 600 relances à tort | fiabilité | factures, paiements et relances erronés pour des milliers d'abonnés ; perte de confiance dans le portail (30 % des appels portent sur une de ses difficultés) ; toute fonction nouvelle (alertes quotidiennes de télérelève) bâtie sur des échanges non fiables | contrôles des échanges (comptages et totaux de contrôle, rapprochement quotidien des paiements, rejets traités sous 48 heures par un responsable désigné) ; contrôle d'unicité à la souscription et fusion des 4 000 doublons ; documentation de chaque échange avant toute évolution | **1** — fin juin 2027 ; DSI et service de la facturation |
| **4 – Comptes des anciens abonnés** : 12 000 comptes conservés sans durée, dont 5 000 avec coordonnées bancaires ; portail absent du registre ; contrat muet sur le sort des données | conformité au RGPD | conservation de données personnelles au-delà de ce que justifie la finalité ; exposition de ces données en cas de violation ; impossibilité de démontrer la conformité ; dépendance envers l'éditeur à la fin du contrat | fiche « portail des abonnés » au registre ; durées de conservation fixées par la régie, avec l'avis de la déléguée à la protection des données, pour chaque catégorie (compte, consommation, coordonnées bancaires, réclamations) ; suppression ou archivage des comptes clos au-delà de ces durées, puis purge automatique ; masquage immédiat des coordonnées bancaires des comptes clos ; avenant au contrat VELIZANE sur le sort des données | **2** — fin septembre 2027 (masquage immédiat) ; déléguée à la protection des données, directrice de la clientèle, DSI |
| **2 – Interruptions pendant les périodes de facturation** : près de 90 heures d'interruption, dont 60, soit les deux tiers, pendant les vagues de mars et de septembre ; disponibilité mesurée par le seul éditeur | efficacité | service indisponible quand les abonnés en ont le plus besoin, report des demandes sur un centre d'appels déjà saturé ; engagement de 99,5 % non tenu (deux fois plus d'interruption qu'admis) sans que la régie puisse le démontrer | mesure de la disponibilité par la régie elle-même et revue mensuelle des niveaux de service avec VELIZANE ; application des engagements du contrat ; calendrier des mises en service excluant les vagues de facturation (gestion des changements) ; envoi des factures étalé sur plusieurs jours ; plan de capacité demandé à l'éditeur | **2** — avant la vague de septembre 2027 ; DSI |

(1,5 pt pour quatre lignes complètes ; 1 pt pour trois ; 0,5 pt pour deux.)

**Ordre de priorité** (0,5 pt) : il croise la **gravité** de l'atteinte aux abonnés, la **probabilité** (le risque s'est-il déjà réalisé ?), l'**étendue** (nombre d'abonnés concernés), le **coût et le délai** de la mesure et son caractère **préalable** aux projets du plan. Les droits des agents viennent en premier : risque de fraude déjà réalisé deux fois, mesure rapide et peu coûteuse (paramétrage des profils et procédure de validation). Les échanges avec la facturation suivent : ils touchent des milliers d'abonnés et conditionnent toute fonction nouvelle, dont les alertes de télérelève. La conservation des données relève d'une décision à préparer avec la déléguée à la protection des données (priorité 2, avec une mesure conservatoire immédiate), et les interruptions ont une échéance naturelle, la vague de facturation de septembre 2027.

**Réponses tolérées**
- Constats 3 ou 6 retenus à la place d'un des quatre constats du corrigé : choix des alertes coché d'avance et non tracé (conformité au RGPD : case non cochée par défaut, historique daté de chaque choix, désinscription en ligne) ; réclamations non suivies (efficacité : suppression de la clôture automatique, outil unique pour tous les canaux, délai suivi chaque mois).
- Constat 5 rattaché aussi à la conformité au RGPD (accès aux données limité au nécessaire), ou constat 2 rattaché à la sécurité (disponibilité, volet de la triade confidentialité, intégrité, disponibilité), si le rattachement est justifié.
- Échelle de priorité différente (élevée, moyenne, faible ; court, moyen terme), et ordre différent s'il est justifié par des critères explicites.
- Diagnostic présenté sous forme de feuilles de constats (constat, cause, risque, recommandation, responsable, échéance).

**Erreurs fréquentes**
- *Constat sans risque ni recommandation opérationnelle* (`JUR-T03` analyser et argumenter) — « les droits sont trop larges, il faut les réduire » ; juste : risque concret pour les abonnés et la régie, mesure précise, responsable et échéance.
- *Recommandations non hiérarchisées* — toutes en priorité 1, ou ordre non justifié.
- *Dérive vers le droit des données personnelles* — bases légales, droits des abonnés, pouvoirs de l'autorité de contrôle ; juste : l'organisation de la conformité (registre, durées de conservation, protection par défaut, contrat de sous-traitance, rôle du délégué), le reste relevant de l'UE 1 (F15 § 9).
- *Délégué à la protection des données présenté comme responsable de la conformité* (`ET-29`) — c'est la régie, responsable du traitement, qui fixe les durées de conservation ; le délégué conseille et contrôle.
- *Critères confondus* — l'efficacité (atteinte des objectifs) prise pour l'efficience (rapport aux moyens), ou la fiabilité réduite à la disponibilité.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Critères d'audit ; feuille de constats (constat, risque, recommandation, priorité, responsable, échéance) | appréciation et diagnostic | F10 § 0, 1.2 et 5 | notion de cours |
| Règlement (UE) 2016/679 (RGPD) : registre, délais d'effacement, protection par défaut, sous-traitance | critère de conformité | `rgpd` / F15 § 2, 4 et 5 | en vigueur |
| Proposition « omnibus numérique » COM(2025) 837 | non applicable au 31/12/2026 | `omnibus_numerique_donnees` / F15 § 8 | projet |
| Séparation des tâches, moindre privilège, revue des droits | constat 5 | F10 § 3.1 | notion de cours |

---

### 3.3 – Veille technologique et stratégie de la relation numérique (5 points)

**Référence au programme**
- §1.1 – Élaborer et aligner la stratégie des SI : `1.1.a` « Définir une stratégie des systèmes d'information alignée sur les objectifs métiers, en intégrant les opportunités offertes par les technologies émergentes » ; `1.1.d` « Outils et méthodes de veille technologique et analyse de l'impact des nouvelles technologies sur les modèles économiques ». Limites : « Ne pas confondre alignement stratégique et simple adéquation technique » ; « Ne pas se limiter à une veille passive : intégrer l'analyse prospective dans l'évaluation des opportunités SI ».

**Annexes mobilisées** : annexes 3.3 (technologies, attentes, sources de veille), 3.1 (chiffres du portail, appels, réclamations, satisfaction), 3.2 (constats 1 et 4) et 1.1 (plan « MORVÈZE EAU 2032 », télérelève).

**Barème indicatif (5 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a-1 | Veille technologique active définie (organisée, continue, orientée vers la décision, prospective) et opposée à la situation de la régie (veille passive, dépendante de l'éditeur) | 0,5 |
| a-2 | Dispositif complet appliqué au cas : axes, sources, outils, acteurs, fréquence, diffusion ; 0,5 pour trois ou quatre des six composantes | 1 |
| b-1 | Assistant conversationnel : valeur pour les abonnés, coûts (330 000 € sur trois ans et coûts internes), risques, effet sur le modèle de service | 1 |
| b-2 | Alertes et espace enrichi : valeur pour les abonnés, coûts (170 000 € sur trois ans et prérequis), risques, effet sur le modèle de service | 1 |
| c-1 | Stratégie du SI alignée définie (mise en cohérence permanente avec les objectifs métiers, technologies émergentes comprises ; modèle SAM) | 0,5 |
| c-2 | Deux orientations reliées aux priorités du plan et aux annexes, chacune avec la suite donnée à une technologie de l'annexe 3.3 ; 0,5 par orientation | 1 |

**Réponse attendue**

*3.3 a) – Veille technologique active et dispositif proposé*

La **veille technologique active** est un dispositif organisé et continu qui recherche, sélectionne, analyse et diffuse les informations sur les technologies susceptibles de modifier les services, les processus ou le modèle de l'organisation, pour éclairer ses décisions ; elle est prospective (elle évalue l'effet probable d'une technologie au regard des besoins et des risques) et s'oppose à la veille passive, qui reçoit les nouveautés au fil de l'eau (F01 § 0). À la régie, la veille est passive et fragmentée : revues lues « selon le temps disponible », congrès sans compte rendu, réseau de régies sans la DSI, et les deux propositions viennent des démonstrations commerciales de l'éditeur déjà en place, faute de responsable et d'espace commun (0,5 pt).

Dispositif proposé (1 pt) :
- **Axes de veille**, tirés du plan : relation numérique avec les abonnés (assistants, espaces personnalisés, canaux) ; valorisation des données de télérelève pour les abonnés ; inclusion et accessibilité des services en ligne ; protection des données et réglementation du numérique (avec la déléguée à la protection des données).
- **Sources** : les sources existantes, mieux exploitées (deux revues, congrès annuel, réseau des régies, que la DSI rejoint) ; des retours d'expérience organisés avec d'autres régies et services publics (dont la régie qui utilise l'assistant depuis 2026) ; plusieurs éditeurs et non le seul VELIZANE ; les publications des organismes professionnels et de l'autorité de contrôle ; les besoins exprimés par le comité des usagers et les motifs d'appels et de réclamations.
- **Outils** : un espace partagé de veille ; une fiche de veille type (technologie, besoin auquel elle répond, maturité, retours d'expérience, coûts, risques, prérequis du SI, conformité) ; une grille d'évaluation commune qui permet de comparer les opportunités ; des alertes thématiques et lettres d'information agrégées.
- **Acteurs** : un pilote de la veille (le chargé de mission ou un agent de la DSI) ; des correspondants dans la direction de la clientèle, la DSI et la direction de l'exploitation ; la déléguée à la protection des données pour la veille réglementaire ; la directrice générale comme commanditaire ; le comité des usagers comme source des besoins.
- **Fréquence** : collecte continue ; point mensuel des correspondants ; synthèse trimestrielle présentée au comité de la relation numérique (question 3.4) ; bilan annuel au conseil d'administration, avec le compte rendu du plan.
- **Diffusion et décision** : lettre de veille trimestrielle d'une page ; fiches d'opportunité soumises au comité, qui décide d'écarter, de surveiller ou d'expérimenter, avec des critères d'évaluation fixés à l'avance ; compte rendu des salons et des réunions du réseau versé dans l'espace commun.

*3.3 b) – Impact des deux technologies sur le modèle de service*

| Angle | Assistant conversationnel fondé sur l'IA générative | Alertes de surconsommation et espace enrichi par la télérelève |
|---|---|---|
| **Valeur pour les abonnés** | réponses jour et nuit aux questions courantes (factures, mensualisation, déménagement, restrictions), quand le centre d'appels ne décroche pas un appel sur quatre aux heures de pointe ; agents recentrés sur les cas complexes. Mais la valeur dépend de l'exactitude des réponses ; les abonnés âgés sans internet n'en tirent aucun bénéfice et le comité des usagers demande de pouvoir toujours parler à un agent | fuite après compteur signalée en quelques jours au lieu d'environ quatre mois (1 200 abonnés en 2026, 1 500 réclamations) ; consommation suivie jour par jour et messages ciblés lors des restrictions d'usage, attendus par les élus après la sécheresse ; service de conseil qui prolonge le plan ; valeur limitée aux 60 000 abonnés équipés jusqu'à la généralisation de 2029 |
| **Coûts** | 330 000 € sur trois ans (60 000 € + 3 × 90 000 €), auxquels s'ajoutent la mise à jour de la documentation, la supervision des réponses et la formation des agents ; gain incertain : les 40 % d'appels évités sont annoncés par l'éditeur, non démontrés, alors que 30 % des appels portent sur des difficultés du portail lui-même | 170 000 € sur trois ans (80 000 € + 3 × 30 000 €), plus l'échange quotidien avec la plateforme de télérelève (charge de la DSI, dont un seul agent suit les échanges) et les envois de SMS ; gains en réclamations évitées et en eau économisée chez l'abonné |
| **Risques** | réponses inexactes mais plausibles (environ une sur dix dans la régie qui l'utilise : démarches, dates de restriction), engageant la parole du service public ; données du compte transmises au modèle d'un fournisseur tiers dont l'hébergement n'est pas précisé (contrat de sous-traitance, analyse d'impact à envisager avec la déléguée à la protection des données) ; image d'un service « déshumanisé » redoutée par les élus ; dépendance accrue envers VELIZANE ; consommation d'énergie | alertes fausses ou manquées si les index sont incomplets ou si les échanges restent peu fiables (constat 1) ; consommations quotidiennes qui révèlent la présence ou l'absence au domicile (inquiétude du comité des usagers) : minimisation, accès restreint, durées de conservation courtes, comparaison avec d'autres foyers soumise au choix de l'abonné ; écart de service entre abonnés équipés ou non ; dépendance envers l'éditeur |
| **Effet sur le modèle de service** | du guichet et du téléphone vers le libre-service en ligne avec renvoi vers un agent : le rôle des agents évolue (supervision, cas complexes), ce qui suppose un accompagnement du changement | d'un service qui facture deux fois par an à un service qui accompagne l'abonné en continu : la régie devient conseillère de la consommation, en cohérence avec sa mission de service public après la sécheresse |

(1 pt par technologie analysée sous les trois angles, appliquée aux annexes ; 0,5 pt si un angle manque.)

*3.3 c) – Stratégie du SI alignée et deux orientations*

Une **stratégie du système d'information alignée** est un ensemble de choix (applications, données, organisation, compétences, partenaires) mis en cohérence de façon permanente avec les objectifs de l'organisation ; selon le modèle SAM de Henderson et Venkatraman (1993), l'alignement combine l'ajustement entre les choix externes et l'organisation interne et l'intégration entre domaine métier et domaine SI ; il intègre les opportunités des technologies émergentes sans se réduire à l'achat d'un outil (F01 § 1). Pour la relation avec les abonnés, l'objectif métier est fixé par le plan : moderniser la relation (40 % d'utilisateurs du portail), en valorisant les données de télérelève (0,5 pt).

Deux orientations (0,5 pt chacune) :
1. **Faire des données de télérelève un service de conseil à l'abonné, sur un socle fiabilisé et protecteur des données** (priorité « moderniser la relation avec les abonnés », en valorisant pour l'abonné les données des compteurs en télérelève que le plan déploie d'abord pour réduire les pertes du réseau ; les fuites après compteur, comptées dans les consommations, ne sont pas des pertes du réseau, mais leur détection répond à l'attente de sobriété exprimée après la sécheresse) : fiabiliser d'abord les échanges entre le portail, la facturation et la plateforme de télérelève et le compte unique de l'abonné (constat 1) ; protéger les données dès la conception (minimisation, choix de l'abonné, durées de conservation : constats 3 et 4). **Suite** : retenir le module d'alertes ; l'expérimenter au second semestre 2027 auprès d'abonnés volontaires équipés, une fois les échanges fiabilisés, avec la déléguée à la protection des données et le comité des usagers ; l'étendre au rythme de la généralisation de la télérelève jusqu'en 2029.
2. **Construire une relation multicanal inclusive, où le numérique libère du temps pour l'accompagnement humain** (priorité « moderniser la relation avec les abonnés », attentes des élus et des usagers) : même information et même suivi des réclamations sur le portail, au téléphone et à l'accueil (outil unique, constat 6), simplification des parcours du portail qui suscitent 30 % des appels, maintien d'un agent joignable et de l'accueil ; maîtrise de la dépendance envers l'éditeur (échanges documentés, données récupérables). **Suite** : ne pas généraliser l'assistant en 2027 ; traiter d'abord les causes des appels ; puis une expérimentation limitée aux questions générales (documentation publique, sans données du compte), avec renvoi visible vers un agent et des critères d'évaluation fixés à l'avance (exactitude des réponses, appels évités, satisfaction), après clarification de l'hébergement et du contrat de sous-traitance ; décision du comité de la relation numérique au vu des résultats, présentée au conseil d'administration.

**Réponses tolérées**
- Dispositif de veille piloté par la DSI seule, ou par un comité de veille, si les métiers et la déléguée à la protection des données y contribuent et si la diffusion vers la décision est organisée.
- Cycle de veille présenté en étapes (définir les besoins, collecter, analyser, diffuser, décider), si les cinq composantes demandées y figurent.
- Analyse d'une technologie sous la forme forces, faiblesses, opportunités, menaces, si la valeur, les coûts et les risques ressortent.
- Assistant retenu pour 2027 si le candidat le conditionne à une expérimentation limitée, à la validation des réponses, au maintien d'un agent joignable et à la clarification de l'hébergement des données.
- Orientations formulées autrement (« un portail fiable avant d'être riche », « la donnée au service de la sobriété des usages »), si chacune est reliée à une priorité du plan et indique la suite donnée à une technologie.
- Référence à la chaîne de valeur (Porter) ou à une perspective du modèle SAM (la technologie de télérelève ouvre un service nouveau), si elle est appliquée au cas.

**Erreurs fréquentes**
- *Veille passive ou réduite aux éditeurs* (`ET-19`) — « s'abonner à des revues » ou « suivre les propositions de VELIZANE » ; juste : axes, sources diversifiées, analyse, diffusion et décision.
- *Opportunités sans risques* (`ET-19`) — assistant présenté comme une économie certaine de 40 % des appels ; juste : gains annoncés à vérifier, réponses inexactes, données, inclusion, dépendance.
- *IA générative confondue avec l'apprentissage automatique* (`ET-09`) — l'assistant « prédit les fuites » ; juste : il produit des réponses en langage courant, d'exactitude non garantie ; les alertes de télérelève reposent sur des règles de détection.
- *Alignement réduit à un choix d'outil* (`ET-06` ; `JUR-G02`) — « la stratégie consiste à acheter les deux modules » ; juste : orientations dérivées des objectifs du plan, technologies au service de ces orientations.
- *Schéma directeur complet* (`ET-07`) — diagnostic, cible, portefeuille et budget du SI de toute la régie ; juste : deux orientations de la relation numérique.
- *Analyse juridique de l'assistant* — qualification au regard de la réglementation de l'IA ; juste : risques de service, de données et de dépendance.
- *Fuites après compteur confondues avec les pertes du réseau* — « les alertes réduisent les pertes du réseau » ; juste : elles réduisent l'eau perdue chez l'abonné et les réclamations, et réutilisent les données du programme de télérelève.

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| Veille technologique active et analyse prospective | dispositif de veille | F01 § 0 (1.1.d) | notion de cours |
| Strategic Alignment Model (Henderson et Venkatraman, 1993) | stratégie du SI alignée | `henderson_venkatraman_1993` / F01 § 1 | modèle publié |
| Risques de l'IA générative (hallucination, confidentialité, dépendance, énergie) | analyse de l'assistant | F13 § 3 | notion de cours |
| Protection des données dès la conception, analyse d'impact, sous-traitance | conditions des deux technologies | `rgpd` / F15 § 3 à 5 | en vigueur |

---

### 3.4 – Gouvernance de la relation numérique (3 points)

**Référence au programme**
- §1.2 – Concevoir et piloter la gouvernance des SI : `1.2.a` « Mettre en œuvre une gouvernance des systèmes d'information intégrant les parties prenantes clés, des indicateurs de performance et des critères de durabilité » ; `1.2.c` « Enjeux relationnels entre DSI, direction générale et directions métiers ». Limite : « Le pilotage ESG est à comprendre dans une logique d'indicateurs intégrés, non isolés ».

**Annexes mobilisées** : annexes 3.1 (relations entre les directions, demandes d'évolution, arbitrages, module de rendez-vous), 3.3 (attentes, comité des usagers) et 1.1 (organigramme, conseil d'administration).

**Barème indicatif (3 pts)**

| Sous-question / item | Attendu | Points |
|---|---|---|
| a | Trois enjeux relationnels tirés de l'annexe 3.1 (logiques opposées mais légitimes, absence d'instance et escalade vers la directrice générale, contournement de la DSI et dépendance envers l'éditeur) ; 0,5 pour deux enjeux | 1 |
| b | Gouvernance du SI définie (évaluer, diriger, surveiller ; distincte du management) et gouvernance à plusieurs niveaux associant le conseil d'administration, la directrice générale, les directions, la déléguée à la protection des données et le comité des usagers, chaque instance avec sa composition, son rôle et sa fréquence (les règles de décision sont valorisées, non exigées) | 1 |
| c | Un indicateur de performance et un critère de durabilité complets (formule, source, fréquence, cible, axe), reliés au cas ; 0,5 par indicateur | 1 |

**Réponse attendue**

*3.4 a) – Trois enjeux relationnels*

1. **Deux logiques légitimes mais opposées, sans lieu pour les concilier** : la direction de la clientèle porte la valeur pour les abonnés et la rapidité (« le service qu'ils trouvent auprès de leur banque ») ; la DSI porte la stabilité, la sécurité et la protection des données (« rien sans recette »). Chacune voit l'autre comme l'obstacle ou le risque : 40 demandes, 12 réalisées (30 %), 18 sans décision, et des interruptions que la DSI attribue à des échanges ajoutés sans documentation. La relation est de type client-fournisseur plutôt que partenaire.
2. **Une escalade vers la directrice générale, faute d'instance et de critères** : six arbitrages en 2026, au cas par cas et par courriel, sans connaissance des coûts ni des risques, que Mme ROCHEVAL ne veut plus rendre seule ; les décisions ne sont ni tracées ni expliquées ; le conseil d'administration n'a jamais examiné le portail, alors que le plan en fait une priorité.
3. **Un contournement qui ruine la confiance et renforce la dépendance envers l'éditeur** : le module de rendez-vous commandé directement à VELIZANE, sans la DSI ni la déléguée à la protection des données (informatique parallèle), n'est pas relié à l'agenda de l'accueil (200 abonnés concernés) ; la déléguée découvre les fonctions une fois en ligne ; l'éditeur, qui propose aussi les deux nouveaux modules, devient l'arbitre de fait des évolutions, ce que redoute la responsable de la DSI.

La réponse est donc une gouvernance partagée, non le choix d'un camp ni d'un outil (1 pt pour trois enjeux ; 0,5 pt pour deux).

*3.4 b) – Gouvernance de la relation numérique*

La gouvernance du SI est le système par lequel l'organe de direction **évalue**, **dirige** et **surveille** l'usage du SI au service de la stratégie (ISO/IEC 38500 ; domaine « évaluer, diriger et surveiller » de COBIT 2019) ; elle se distingue du management, qui planifie et exécute (F02 § 2).

| Instance | Composition | Rôle | Fréquence |
|---|---|---|---|
| **Conseil d'administration** | M. VAUQUIERS et les administrateurs ; présentation par la directrice générale | approuve les orientations de la relation numérique et leur enveloppe, examine le compte rendu (indicateurs, suites de l'audit, risques), décide des engagements significatifs (généralisation d'un module, assistant) | deux fois par an, dont la séance de juin 2027 |
| **Comité de la relation numérique** (niveau stratégique) | directrice générale (présidente), directrice de la clientèle, responsable de la DSI, déléguée à la protection des données (avis), directeur administratif et financier ; responsable de la sécurité des systèmes d'information invité ; chargé de mission (secrétariat) | arbitre le portefeuille des évolutions selon des critères partagés (valeur pour les abonnés, contribution au plan, coût, risques, capacité de la DSI), suit le plan d'action de l'audit et les indicateurs, décide des expérimentations issues de la veille ; décisions écrites et motivées, qui remplacent les arbitrages par courriel | trimestrielle |
| **Comité des usagers** (consultation) | Mme BRESSANDE et les représentants des associations ; directrice de la clientèle et déléguée à la protection des données | donne son avis sur les évolutions qui changent la relation (alertes, assistant, canaux non numériques, conservation des données) ; un panel d'usagers participe aux expérimentations et à leur évaluation ; avis transmis au comité et au conseil d'administration | deux fois par an et avant toute mise en service majeure |
| **Comité du portail** (niveau opérationnel) | responsable fonctionnel du portail (direction de la clientèle), agent de la DSI chargé des échanges, représentant de l'accueil ; VELIZANE selon l'ordre du jour ; déléguée à la protection des données consultée | file unique et priorisée des demandes d'évolution, recette conjointe, calendrier des mises en service hors périodes de facturation, revue des niveaux de service de l'éditeur | mensuelle |

**Règles et rôles** : la directrice de la clientèle est **propriétaire** du portail (elle porte le besoin, la valeur et la recette) ; la DSI est **garante** de l'architecture, des échanges, de la sécurité et de la relation technique avec l'éditeur ; la déléguée à la protection des données est consultée dès la conception ; aucune commande à l'éditeur sans passage par le comité du portail ; tout désaccord persistant remonte au comité de la relation numérique, non à la directrice générale seule (1 pt).

*3.4 c) – Un indicateur de performance et un critère de durabilité*

| Indicateur | Formule | Source | Fréquence | Cible | Axe |
|---|---|---|---|---|---|
| **Délai moyen de traitement des réclamations** (performance) | somme des délais entre l'enregistrement de chaque réclamation et la réponse apportée à l'abonné / nombre de réclamations ayant reçu une réponse dans le mois ; les clôtures sans réponse sont comptées à part | outil unique de suivi des réclamations (module du portail étendu au téléphone et à l'accueil) | mensuelle | 8 jours au plus fin 2027, engagement de la charte de service (18 jours en 2026), et aucune réclamation close sans réponse | client |
| **Taux de satisfaction des abonnés reçus à l'accueil ou au téléphone** (durabilité : inclusion) | abonnés satisfaits / abonnés interrogés parmi ceux qui ont contacté l'accueil ou le centre d'appels | enquête de satisfaction de la direction de la clientèle | semestrielle | au moins 75 % (niveau de 2026), maintenu pendant toute la modernisation | social (ESG) |

(0,5 pt par indicateur complet et pertinent.)

Le premier mesure le résultat attendu des abonnés, sur lequel la clientèle et la DSI doivent coopérer (outil unique, fin de la clôture automatique). Le second traduit un critère de durabilité sociale : la modernisation ne doit pas dégrader le service rendu aux abonnés qui n'utilisent pas le portail, comme le demandent le comité des usagers et les élus (inclusion numérique, F14 § 4). Les deux figurent dans le même compte rendu au comité et au conseil d'administration, sans liste ESG isolée.

**Réponses tolérées**
- Instances nommées autrement (comité stratégique du numérique, comité de pilotage du portail), ou comité stratégique et comité du portail réunis en une instance pour une régie de cette taille, si les niveaux de décision et la place des usagers sont distingués.
- Organisation présentée en modèle bimodal (un mode stable pour la facturation, un mode exploratoire pour les services en ligne), si les règles de coordination sont précisées.
- Matrice de responsabilités (réalise, approuve, consulté, informé) en complément des instances.
- Indicateur fondé sur l'engagement de la charte, réclamation par réclamation : part des réclamations traitées en 8 jours au plus (cible 90 %, axe client), à la place du délai moyen ou en complément, une moyenne de 8 jours pouvant cacher des dépassements.
- Autre indicateur de performance complet : taux de disponibilité du portail mesuré par la régie (cible 99,5 %, axe processus) ; part des abonnés utilisant le portail (cible tirée du plan, axe client) ; délai de décision sur une demande d'évolution (axe processus).
- Autre critère de durabilité complet : part des démarches du portail également réalisables à l'accueil ou par téléphone (cible 100 %, axe social) ; volume d'eau des fuites après compteur détectées par alerte (axe environnement), si la formule et la source sont précisées.

**Erreurs fréquentes**
- *Prise de parti pour une direction* (`JUR-G05` déséquilibres organisationnels et recommandations réalistes) — « la DSI freine, il faut la contourner » ou « la clientèle doit attendre » ; juste : reconnaître deux logiques légitimes et organiser leur arbitrage.
- *Gouvernance sans les parties prenantes externes* — ni conseil d'administration ni comité des usagers, alors que la consigne et l'annexe 3.3 les désignent.
- *Gouvernance réduite à un outil ou à un comité informatique* (`ET-06`) — « un logiciel de gestion des demandes » ; juste : instances, rôles, règles de décision.
- *Indicateur incomplet ou générique* (`JUR-A02` ; `ET-18`) — « satisfaction » sans formule, source ni cible.
- *Critère de durabilité isolé* — un indicateur environnemental sans lien avec la relation numérique, présenté dans une liste à part (limite du programme : indicateurs intégrés).

**Références**

| Référence | Contenu mobilisé | Id `referentiels_dates.yaml` / fiche | Statut |
|---|---|---|---|
| ISO/IEC 38500:2024 — gouvernance des technologies de l'information | évaluer, diriger, surveiller | `iso_38500_2024` / F02 § 4 | en vigueur |
| COBIT 2019 (ISACA), domaine « évaluer, diriger et surveiller » | gouvernance distincte du management | `cobit_2019` / F02 § 3 | en vigueur |
| Comitologie SI ; relations DSI, direction générale, métiers | instances et rôles | F02 § 6 ; F01 § 4 | notion de cours |
| Indicateurs d'inclusion (volet social de l'ESG) | critère de durabilité | F14 § 4 | notion de cours |
| Fiche d'indicateur à cinq champs | indicateurs | F09 § 4 | notion de cours |
