# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 11

**DOSSIER 2 – SÉCURISER LE SYSTÈME DE SUPERVISION DES INSTALLATIONS ET SES ACCÈS (13 points)**

Durée conseillée : 59 min (13 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

Réglementation applicable au 31/12/2026, sauf mention contraire.

**Document et matériel autorisés** : aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Ce dossier est l'un des trois dossiers indépendants du sujet d'entraînement complet n° 4, construits sur un même cas : la présentation et l'annexe 1.1 sont communes aux trois dossiers ; chaque dossier comporte en outre ses propres annexes.

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

Nous sommes en mars 2027. La Régie des eaux de l'agglomération de MORVÈZE est un établissement public local à caractère industriel et commercial, créé en 2016 par la communauté d'agglomération de Morvèze (32 communes, 310 000 habitants) pour gérer en direct le service public de l'eau potable et de l'assainissement. Elle emploie 380 agents et dessert 160 000 abonnés. Elle exploite deux usines de production d'eau potable, cinq stations de traitement des eaux usées et 2 400 kilomètres de canalisations ; 120 sites (réservoirs, stations de pompage, usines) sont pilotés à distance par un système de supervision centralisé. Ses recettes de l'exercice 2026 s'élèvent à 70 millions d'euros, dont 38 millions pour l'eau potable et 32 millions pour l'assainissement ; 3,5 millions d'euros sont consacrés au système d'information. Les organisations, les personnes et les données de ce cas sont fictives.

Après l'été 2026, marqué par une sécheresse et par des restrictions d'usage de l'eau, le conseil d'administration de la régie a adopté en décembre 2026 le plan stratégique « MORVÈZE EAU 2032 ». Il fixe trois priorités : réduire les pertes du réseau grâce aux données des compteurs en télérelève, qui équipent 60 000 abonnés et seront généralisés d'ici 2029 ; renforcer la sécurité des installations, après une connexion suspecte détectée en novembre 2026 sur le système de supervision ; moderniser la relation avec les abonnés, dont 40 % utilisent déjà le portail en ligne de la régie. La directrice générale, Mme Mathilde ROCHEVAL, rend compte de la mise en œuvre du plan au conseil d'administration, présidé par M. Gilles VAUQUIERS, vice-président de la communauté d'agglomération.

Vous venez de rejoindre la régie comme chargé(e) de mission auprès de la directrice générale. Mme ROCHEVAL vous confie trois travaux : exploiter les données de télérelève pour réduire les pertes et piloter le programme qui leur est consacré (dossier 1) ; sécuriser le système de supervision des installations et les accès à celui-ci (dossier 2) ; auditer le portail des abonnés et orienter la stratégie de la relation numérique (dossier 3). L'annexe 1.1 est commune aux trois dossiers, qui sont indépendants ; chaque dossier comporte en outre ses propres annexes. Pour conduire ce travail, vous vous appuierez sur les annexes fournies ainsi que sur vos connaissances professionnelles.

### ANNEXE 1.1 – Présentation de la Régie des eaux de l'agglomération de MORVÈZE et chiffres clés

La Régie des eaux de l'agglomération de MORVÈZE est un établissement public local à caractère industriel et commercial, créé en 2016 par la communauté d'agglomération de Morvèze, qui lui a confié la gestion directe du service public de l'eau potable et de l'assainissement sur ses 32 communes. Elle est administrée par un conseil d'administration, présidé par M. Gilles VAUQUIERS, vice-président de la communauté d'agglomération, et dirigée par une directrice générale. Ses abonnés sont des particuliers, des entreprises et des collectivités. Son exercice coïncide avec l'année civile.

**Chiffres clés de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Activité | production et distribution d'eau potable ; collecte et traitement des eaux usées |
| Territoire desservi | communauté d'agglomération de Morvèze : 32 communes, 310 000 habitants |
| Abonnés | 160 000 (particuliers, entreprises, collectivités) |
| Agents | 380 |
| Recettes | 70 M€ : eau potable 38 M€, assainissement 32 M€ |
| Budget du système d'information | 3,5 M€ (5 % des recettes) |
| Installations | deux usines de production d'eau potable ; cinq stations de traitement des eaux usées ; 2 400 km de canalisations |
| Supervision | 120 sites (réservoirs, stations de pompage, usines) pilotés à distance par un système de supervision centralisé |
| Télérelève | 60 000 abonnés équipés de compteurs en télérelève fin 2026 ; généralisation aux 160 000 abonnés d'ici 2029 |
| Plan « MORVÈZE EAU 2032 » (adopté en décembre 2026) | réduire les pertes du réseau grâce aux données de télérelève ; renforcer la sécurité des installations après la connexion suspecte de novembre 2026 sur la supervision ; moderniser la relation avec les abonnés (40 % utilisent le portail en ligne) |

**Organigramme simplifié (mars 2027)**

| Niveau | Fonction | Titulaire |
|---|---|---|
| Conseil d'administration | président, vice-président de la communauté d'agglomération | M. Gilles VAUQUIERS |
| Direction générale | directrice générale, qui rend compte au conseil d'administration de la mise en œuvre du plan « MORVÈZE EAU 2032 » | Mme Mathilde ROCHEVAL |
| Rattaché(e) à la directrice générale | chargé(e) de mission (poste créé en 2027) | vous |
| Rattachée à la directrice générale | déléguée à la protection des données | Mme Hélène BARJOLLE |
| Comité de direction | directeur de l'exploitation (usines, stations de traitement des eaux usées, réseaux, équipes d'intervention, centre de supervision) | M. Thierry SALVANHAC |
| Comité de direction | directrice de la clientèle (accueil, facturation, relève des compteurs, portail des abonnés) | Mme Élodie FARGEMONT |
| Comité de direction | responsable de la direction des systèmes d'information (DSI, 14 agents) | Mme Nathalie CORVESSE |
| Rattaché à la responsable de la DSI | responsable de la sécurité des systèmes d'information (fonction exercée à mi-temps) | M. Yannick LORBEL |
| Comité de direction | directeur administratif et financier (budget, comptabilité, contrôle de gestion) | M. Laurent CHAZELON |
| Rattaché au directeur administratif et financier | responsable du contrôle de gestion | M. Sébastien VELOUZE |
| Comité de direction | directrice des ressources humaines | Mme Claire AUBRESPIN |

### ANNEXE 2.1 – Le système de supervision et ses accès

**Note de Mme Nathalie CORVESSE, responsable de la DSI, à la directrice générale (janvier 2027)**

**A. Fonctionnement**

Le système de supervision, renouvelé en 2019, permet de surveiller et de piloter à distance les 120 sites de la régie : deux usines de production d'eau potable, cinq stations de traitement des eaux usées, 70 réservoirs et 43 stations de pompage. Sur chaque site, des automates appliquent les consignes envoyées par la supervision (niveaux de remplissage des réservoirs, marche et arrêt des pompes, dosage des réactifs de traitement dans les usines) et lui renvoient les mesures et les alarmes.

- **Centre de supervision** : situé à l'usine de production principale, il compte six postes de supervision, occupés par les opérateurs de 7 heures à 19 heures en semaine. Le logiciel de supervision est fourni et maintenu par l'éditeur KERVALDIS ; l'intégrateur BRÉMONTAL a programmé les automates des sites et en assure la maintenance ; le fabricant PURIMANE maintient les équipements de traitement des deux usines.
- **Liaisons avec les sites** : 40 sites sont reliés au centre par les liaisons de la régie, 80 par le réseau d'un opérateur de téléphonie mobile ; les échanges entre le centre et les sites ne sont pas chiffrés.
- **Réseau** : les postes de supervision sont reliés au même réseau que les 300 postes de bureautique des agents, sans cloisonnement : depuis un poste de bureautique, on peut joindre un poste de supervision. Les postes de supervision ont accès à la messagerie et à internet ; quatre des six fonctionnent avec un système d'exploitation dont l'éditeur ne fournit plus de mises à jour de sécurité depuis 2023.
- **Accès à distance** : un logiciel de prise en main à distance, installé sur les postes de supervision et joignable depuis internet, est utilisé la nuit et le week-end par les huit agents d'astreinte depuis leur domicile (trois d'entre eux avec leur ordinateur personnel), et à toute heure par les techniciens des trois prestataires, qui n'ont pas à prévenir la régie. Les accès des prestataires sont ouverts en permanence.
- **Authentification** : un identifiant et un mot de passe pour tous les comptes ; aucune authentification multifacteur, y compris pour les accès à distance.
- **Journaux** : le logiciel de supervision enregistre les connexions et les modifications de consignes ; les journaux sont conservés 30 jours et ne sont consultés qu'après un incident ; aucune alerte n'est émise en cas de connexion inhabituelle.

**B. Inventaire des comptes d'accès à la supervision (état au 20 novembre 2026, avant l'incident)**

| Type de compte | Nombre | Constats |
|---|---|---|
| Comptes nominatifs d'agents (opérateurs, automaticiens, agents d'exploitation) | 28 | 5 appartiennent à des agents partis ou mutés : la direction des ressources humaines ne signale pas les départs et les mutations à la direction de l'exploitation |
| Comptes génériques partagés (« exploitation », « astreinte », « maintenance ») | 3 | utilisés par environ 45 personnes ; mots de passe inchangés de 2019 à novembre 2026 ; aucune action ne peut être attribuée à une personne |
| Comptes de télémaintenance des prestataires | 25 : KERVALDIS 12, BRÉMONTAL 8, PURIMANE 5 | 10 sont au nom de techniciens qui ne travaillent plus chez le prestataire ; aucune revue depuis 2019 ; les contrats de maintenance n'obligent pas les prestataires à signaler le départ de leurs techniciens |
| Comptes d'administration (droits complets : consignes, seuils d'alarme, création des comptes) | 4 | dont un compte générique « admin » partagé par les trois automaticiens et l'éditeur |
| **Ensemble** | **60 comptes** | un quart des comptes (15) appartiennent à des personnes parties ; 52 comptes peuvent modifier les consignes des sites, seuls 8 sont limités à la consultation |

**C. Organisation de la sécurité**

- Le directeur de l'exploitation, M. Thierry SALVANHAC, est responsable des installations et du système de supervision, qu'administre une équipe de trois automaticiens de sa direction.
- La DSI (14 agents) gère le réseau, la bureautique, les applications de gestion et les comptes de messagerie, mais pas les comptes de la supervision.
- M. Yannick LORBEL exerce la fonction de responsable de la sécurité des systèmes d'information à mi-temps ; il consacre l'autre moitié de son temps aux infrastructures de la DSI, dont il relève. La politique de sécurité des systèmes d'information adoptée en 2021 couvre la bureautique et les applications de gestion : la supervision n'y figure pas et n'a jamais fait l'objet d'une analyse des risques.
- En 2025, un audit de l'éditeur KERVALDIS avait recommandé une authentification multifacteur pour les accès à distance ; la recommandation n'a pas été suivie, faute de budget et de responsable désigné.
- Budget de la sécurité en 2026 : 100 000 €, soit moins de 3 % du budget du système d'information. Le plan « MORVÈZE EAU 2032 » prévoit 200 000 € par an de 2027 à 2029 pour la sécurité des installations.
- Avant décembre 2026, le conseil d'administration n'avait jamais examiné la sécurité du système d'information.

**D. Points de vue recueillis en janvier 2027**

**M. Thierry SALVANHAC, directeur de l'exploitation** : « La supervision, c'est l'eau au robinet. Si un agent d'astreinte ne peut pas se connecter à 3 heures du matin parce qu'une règle informatique l'en empêche, c'est un réservoir vide au réveil. Je veux de la sécurité, mais pas au détriment de nos interventions. »

**Mme Nathalie CORVESSE, responsable de la DSI** : « Notre réseau transporte les échanges de la supervision sans que nous sachions qui s'y connecte. La supervision et la bureautique sont deux mondes qui partagent les mêmes câbles. »

**M. Yannick LORBEL, responsable de la sécurité des systèmes d'information** : « Je n'ai aucun droit de regard sur la supervision. J'ai appris la connexion suspecte le lundi à 11 heures, plus d'un jour après les faits. »

**Mme Mathilde ROCHEVAL, directrice générale** : « Je veux pouvoir dire au conseil d'administration quels risques nous réduisons, lesquels nous acceptons, qui en répond et dans quels délais. »

### ANNEXE 2.2 – La connexion suspecte de novembre 2026

**Compte rendu établi par M. Yannick LORBEL (décembre 2026)**

**A. Chronologie**

| Date et heure | Faits |
|---|---|
| Fin juin 2026 | Un technicien de l'intégrateur BRÉMONTAL quitte l'entreprise. Son compte de télémaintenance reste actif : ni BRÉMONTAL ni la régie ne le désactivent. |
| Nuit du mardi 3 au mercredi 4 novembre, 1 h 50 | Connexion de ce compte à la supervision pendant vingt minutes, sans modification ; personne ne la remarque (elle sera retrouvée dans les journaux après l'incident). |
| Nuit du samedi 21 au dimanche 22 novembre, 2 h 10 | Nouvelle connexion du même compte, par l'accès à distance. |
| 2 h 25 | Les pompes qui alimentent le réservoir de la Combe-Martel, rempli à 80 % de sa capacité, sont mises à l'arrêt et l'alarme de niveau bas de ce réservoir est désactivée. Le réservoir dessert environ 12 000 habitants de trois communes, dont un établissement d'hébergement pour personnes âgées dépendantes. |
| 5 h 40 | Un agent d'astreinte, connecté depuis son domicile pour une alarme sur une autre station de pompage, remarque par hasard que le réservoir n'est plus rempli qu'à 45 %. |
| 5 h 50 | L'agent remet les pompes en marche et rétablit l'alarme ; le remplissage reprend. Faute de procédure, il ne sait pas s'il doit couper les accès à distance et ne le fait pas. |
| 6 h 10 | Il prévient M. SALVANHAC, qui décide d'attendre le lundi. |
| Lundi 23 novembre, 8 h 30 | M. SALVANHAC informe Mme CORVESSE. |
| 9 h 40 | Le compte est désactivé, 28 heures après la détection. |
| 11 h | M. LORBEL est informé. |
| 12 h | La directrice générale est informée. |
| Mercredi 25 novembre | Les neuf autres comptes de prestataires au nom de techniciens partis sont désactivés. |
| Vendredi 27 novembre | Les mots de passe des trois comptes génériques sont changés. |
| Jeudi 10 décembre | Le conseil d'administration est informé, lors de l'adoption du plan « MORVÈZE EAU 2032 ». |

**B. Conséquences et constats**

- Aucune conséquence sur la distribution ni sur la qualité de l'eau. Selon la direction de l'exploitation, sans l'intervention fortuite de l'agent d'astreinte, le réservoir aurait été vide vers 8 h 30, au moment de la pointe de consommation du matin.
- Entre la connexion et la détection, 3 h 30 se sont écoulées ; la détection est due au hasard, non à une alerte.
- Les journaux, conservés 30 jours et extraits le 22 novembre, ne permettent pas de savoir si le compte a été utilisé avant le 23 octobre 2026. Les investigations n'ont établi ni qui a utilisé le compte, ni comment son mot de passe a été obtenu.
- Coût direct de l'incident : 25 000 € (investigation par un prestataire spécialisé dans la réponse aux incidents, 20 000 € ; heures supplémentaires, 5 000 €).
- Aucune procédure ne précise qui doit être alerté, qui décide de couper les accès ni qui informe la direction générale.

**C. Le scénario redouté par la direction de l'exploitation**

« Un attaquant qui, une même nuit, modifierait les consignes de plusieurs réservoirs et le dosage des réactifs de traitement d'une usine pourrait priver d'eau des quartiers entiers et mettre en distribution une eau impropre à la consommation. Les analyseurs des usines déclenchent une alarme en cas d'anomalie de la qualité de l'eau, mais cette alarme remonte par la supervision elle-même. Les usines et les principales stations peuvent être conduites sur place, en mode manuel, mais il faut environ deux heures pour mobiliser une équipe la nuit. »

### ANNEXE 2.3 – Repères méthodologiques et réglementaires (au 31/12/2026)

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| EBIOS Risk Manager (ANSSI, version 1.5 de 2024) | Méthode d'appréciation et de traitement des risques numériques, en cinq ateliers : 1. cadrage et socle de sécurité ; 2. sources de risque et objectifs qu'elles visent ; 3. scénarios stratégiques, qui examinent l'écosystème de l'organisation (prestataires, partenaires) ; 4. scénarios opérationnels ; 5. traitement du risque (plan de mesures, risques résiduels). Compatible avec les lignes directrices ISO/IEC 27005:2022 sur la gestion des risques. | En vigueur |
| ISO/IEC 27001:2022 et ISO/IEC 27002:2022 (à titre de référence) | ISO/IEC 27001:2022 : norme d'exigences, certifiable, d'un système de management de la sécurité de l'information fondé sur l'appréciation et le traitement des risques, l'engagement de la direction et l'amélioration continue ; son annexe A comporte 93 mesures (organisationnelles, liées aux personnes, physiques et technologiques), détaillées par le guide ISO/IEC 27002:2022. | En vigueur |
| Guide d'hygiène informatique de l'ANSSI (version de 2017) | Guide de 42 mesures de sécurité de base, de niveau standard ou renforcé, destiné à toute organisation. | En vigueur |
| Le modèle Zero Trust (avis de l'ANSSI, 2021) | Modèle d'architecture : aucune confiance implicite n'est accordée à un utilisateur ou à un terminal du fait de sa position sur le réseau ; chaque accès à une ressource est authentifié, autorisé et évalué selon le contexte. L'ANSSI le présente comme une évolution progressive, qui ne remplace pas la défense en profondeur. | Avis publié |
| Directive (UE) 2022/2555 (« NIS 2 ») | Cybersécurité d'entités dites essentielles ou importantes, selon leur secteur et leur taille. Les organes de direction approuvent les mesures de gestion des risques, en supervisent la mise en œuvre, peuvent être tenus pour responsables et suivent une formation. Les mesures couvrent notamment l'analyse des risques, la gestion des incidents, la continuité des activités, la sécurité de la chaîne d'approvisionnement (relations avec les prestataires), le contrôle d'accès, le chiffrement et l'authentification multifacteur. Les incidents importants sont notifiés : alerte précoce sous 24 heures, notification sous 72 heures, rapport final sous un mois. | Transposition en droit français due au 17/10/2024, non promulguée au 31/12/2026 : le projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité, adopté par le Sénat le 12/03/2025, est en cours d'examen à l'Assemblée nationale. |

Il n'est pas demandé d'apprécier si la régie entre dans le champ de la directive NIS 2.

### Travail à faire

Mme ROCHEVAL veut présenter au conseil d'administration de juin 2027 une politique de sécurité du système de supervision et une organisation claire des responsabilités, qui tirent les leçons de la connexion suspecte de novembre 2026. Vous mobiliserez pour cela les annexes 1.1, 2.1, 2.2 et 2.3 ainsi que vos connaissances professionnelles.

**2.1 – Risques pesant sur le système de supervision (4 points)**

a) Après avoir présenté la typologie des risques du système d'information, identifiez six risques pesant sur le système de supervision, tirés des annexes 2.1 et 2.2, et classez-les en cybermenaces, défaillances opérationnelles, risques réglementaires et risques métiers, avec au moins un risque par catégorie.

b) Après avoir défini l'analyse d'impact sur l'activité, analysez les conséquences du scénario redouté par la direction de l'exploitation (annexe 2.2 C) sur trois plans : les processus de la régie, la continuité du service aux abonnés et la santé des usagers.

c) Montrez, en trois constats tirés de l'annexe 2.2, ce que l'incident de novembre 2026 révèle des faiblesses de la régie dans la détection et dans le traitement de ses risques.

**2.2 – Démarche et principes de la politique de cybersécurité (3 points)**

a) Après avoir défini la politique de sécurité du système d'information, présentez les étapes de son élaboration à partir d'une analyse des risques, en vous appuyant sur la méthode EBIOS Risk Manager (annexe 2.3) et en illustrant chaque étape par un élément du cas.

b) Proposez quatre principes de cette politique propres à un système critique comme la supervision, en justifiant chacun par les annexes.

**2.3 – Architecture de confiance (2 points)**

Après avoir présenté le modèle Zero Trust, proposez trois mesures d'architecture de confiance — l'une d'authentification, l'une de chiffrement, l'une de segmentation entre la bureautique et la supervision —, en précisant pour chacune le constat de l'annexe 2.1 auquel elle répond et une condition de sa réussite.

**2.4 – Gestion des identités et surveillance des connexions (2 points)**

a) Proposez quatre règles de gestion des identités et des accès à la supervision, applicables aux agents et aux prestataires, portant respectivement sur le cycle de vie des comptes, les comptes génériques, les comptes à privilèges et la revue périodique des droits.

b) Proposez un dispositif de surveillance des connexions à la supervision et deux indicateurs de son efficacité, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

**2.5 – Gouvernance de la sécurité de la supervision (2 points)**

a) Après avoir précisé l'intérêt d'une matrice de responsabilités, construisez celle qui répartit les rôles (réalise, approuve, consulté, informé) entre le conseil d'administration, la directrice générale, le responsable de la sécurité des systèmes d'information, le directeur de l'exploitation, la responsable de la DSI et les prestataires pour quatre activités : l'approbation de la politique de sécurité de la supervision, l'analyse des risques, la gestion des accès des prestataires et le traitement d'un incident.

b) Justifiez deux évolutions de l'organisation actuelle de la sécurité, dont le positionnement du responsable de la sécurité des systèmes d'information.
