# DSCG UE 5 — Management des systèmes d'information — Sujet d'entraînement complet n° 4

Durée de l'épreuve : 3 heures – Coefficient : 1

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026.

**Document et matériel autorisés** : Aucun document ni aucun matériel n'est autorisé. En conséquence, tout usage d'une calculatrice est interdit et constituerait une fraude.

Le sujet se présente sous la forme de 3 dossiers indépendants :

| Dossier | Intitulé | Points | Durée conseillée |
|---|---|---:|---|
| DOSSIER 1 | EXPLOITER LES DONNÉES DE TÉLÉRELÈVE POUR RÉDUIRE LES PERTES ET PILOTER LE PROGRAMME | 14 points | 1 h 03 |
| DOSSIER 2 | SÉCURISER LE SYSTÈME DE SUPERVISION DES INSTALLATIONS ET SES ACCÈS | 13 points | 59 min |
| DOSSIER 3 | AUDITER LE PORTAIL DES ABONNÉS ET ORIENTER LA STRATÉGIE DE LA RELATION NUMÉRIQUE | 13 points | 58 min |

Le sujet comporte 10 annexes, dont 1 communes aux dossiers.

| Dossier | Annexe | Intitulé |
|---|---|---|
| Tous les dossiers | Annexe 1.1 | Présentation de la Régie des eaux de l'agglomération de MORVÈZE et chiffres clés |
| DOSSIER 1 | Annexe 1.2 | Les données disponibles et leur circulation |
|  | Annexe 1.3 | Premiers chiffres et questions de la direction |
|  | Annexe 1.4 | Le programme « télérelève et réduction des pertes » |
| DOSSIER 2 | Annexe 2.1 | Le système de supervision et ses accès |
|  | Annexe 2.2 | La connexion suspecte de novembre 2026 |
|  | Annexe 2.3 | Repères méthodologiques et réglementaires (au 31/12/2026) |
| DOSSIER 3 | Annexe 3.1 | Le portail des abonnés |
|  | Annexe 3.2 | Constats préalables à l'audit et repères au 31/12/2026 |
|  | Annexe 3.3 | Technologies émergentes signalées |

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

---

## DOSSIER 1 – EXPLOITER LES DONNÉES DE TÉLÉRELÈVE POUR RÉDUIRE LES PERTES ET PILOTER LE PROGRAMME (14 points)

### ANNEXE 1.2 – Les données disponibles et leur circulation

**Note de M. Thierry SALVANHAC, directeur de l'exploitation, à la directrice générale (février 2027)**

**A. Les sources de données**

| Source | Données | Outil et fréquence |
|---|---|---|
| Compteurs en télérelève (60 000 abonnés) | un index de consommation par compteur et par jour, transmis par radio | plateforme de télérelève d'un prestataire, sur abonnement ; export quotidien d'un fichier de 60 000 lignes, soit environ 22 millions de lignes par an |
| Autres compteurs (100 000 abonnés) | index relevé sur place par les releveurs | relevé semestriel, saisi dans le logiciel de facturation ; entre deux relevés, la consommation est estimée à partir de l'année précédente |
| Débitmètres d'entrée des secteurs | volumes entrant dans chacun des cinq secteurs du réseau, mesurés toutes les quinze minutes par 40 débitmètres | système de supervision ; extraction mensuelle par un technicien |
| Casses et réparations | fiche d'intervention saisie par les équipes : date, adresse, matériau et diamètre de la canalisation, cause, durée de la réparation | logiciel des interventions, saisie sur tablette ou, à défaut, sur papier puis ressaisie |
| Caractéristiques des canalisations | tronçons, matériau, diamètre, date de pose, secteur de rattachement | base patrimoniale du réseau, tenue par le bureau d'études |

Chaque compteur est rattaché à un secteur du réseau dans le logiciel de facturation ; les pertes d'un secteur sont estimées en retranchant des volumes entrés dans le secteur les consommations des compteurs qui lui sont rattachés.

**B. Les défauts constatés (relevés de janvier 2027)**

| Défaut | Mesure |
|---|---|
| Compteurs en télérelève qui ne transmettent pas leur index du jour | 3 000 en moyenne chaque jour (5 %), dont 600 muets depuis plus d'un mois (pile usée, émetteur défaillant) ; les jours manquants sont laissés vides dans les exports |
| Index aberrants | environ 2 000 par mois : index inférieur à celui de la veille, consommation journalière d'un particulier supérieure à 10 m³ ; certains correspondent à de vraies fuites après compteur, chez l'abonné |
| Limites de secteurs non mises à jour | le lotissement neuf des Prés-Hauts (2 000 abonnés, environ 0,2 million de m³ consommés par an), mis en service en septembre 2025, est alimenté par le secteur Faubourgs nord ; ses compteurs ont été rattachés par erreur au secteur Plateau est dans le logiciel de facturation |
| Débitmètres en panne | 4 des 40 débitmètres ont été en panne plus d'un mois en 2026 ; les valeurs manquantes ont été remplacées à la main par la moyenne du mois précédent, sans que la correction soit signalée |
| Fiches de casse incomplètes | 30 % des 650 fiches de 2026 n'indiquent ni l'adresse précise ni le matériau de la canalisation (le secteur, lui, est toujours indiqué) ; les fiches papier sont ressaisies avec deux à trois semaines de retard |
| Date de pose des canalisations inconnue | 25 % du linéaire (600 km) ; l'âge moyen des canalisations est calculé sur les seuls tronçons dont la date est connue |

**C. Les outils actuels**

Les exports de la plateforme de télérelève, de la supervision et du logiciel des interventions sont copiés dans une dizaine de classeurs de tableur ; le technicien qui les tient ne conserve que des totaux mensuels, faute de pouvoir manipuler les fichiers quotidiens. Il consacre deux jours par mois au rapport mensuel de l'exploitation, diffusé vers le 20 du mois suivant. Chacun des trois services concernés (exploitation, clientèle, bureau d'études) tient sa propre liste des secteurs.

### ANNEXE 1.3 – Premiers chiffres et questions de la direction

**A. Volumes de l'exercice 2026 (millions de m³)**

| Volumes mis en distribution (sortie des deux usines) | Volumes consommés comptabilisés | dont relevés par télérelève | dont relevés semestriellement ou estimés | Pertes estimées |
|---|---|---|---|---|
| 25 | 20 | 8 | 12 | 5, soit 20 % des volumes mis en distribution |

**B. Les cinq secteurs du réseau en 2026 (chiffres arrondis)**

| Secteur | Longueur de canalisations (km) | Abonnés | Part des abonnés en télérelève | Pertes estimées (millions de m³) | Pertes par km de canalisation (milliers de m³ par an) | Débit nocturne minimal moyen (m³/h) : 2024 → 2026 | Âge moyen des canalisations (ans) | Casses en 2026 (pour 100 km) |
|---|---|---|---|---|---|---|---|---|
| Centre ancien | 200 | 50 000 | 60 % | 1,6 | 8 | 300 → 300 | 55 | 180 (90) |
| Faubourgs nord | 400 | 40 000 | 20 % | 1,6 | 4 | 200 → 260 | 45 | 220 (55) |
| Zone d'activités ouest | 300 | 10 000 | 70 % | 0,3 | 1 | 50 → 50 | 20 | 30 (10) |
| Plateau est | 500 | 30 000 | 40 % | 0,7 | 1,4 | 130 → 130 | 30 | 70 (14) |
| Coteaux sud (communes rurales) | 1 000 | 30 000 | 10 % | 0,8 | 0,8 | 110 → 110 | 40 | 150 (15) |
| **Ensemble** | **2 400** | **160 000** | **37,5 %** | **5** | **2,1** | — | — | **650** |

Le débit nocturne minimal est le plus faible débit entrant dans le secteur entre 2 heures et 5 heures du matin, quand la consommation des abonnés est au plus bas : une hausse durable signale en général une fuite. Dans la zone d'activités ouest, trois usines agroalimentaires consomment de l'eau la nuit.

**C. Évolution du débit nocturne du secteur Faubourgs nord (description du graphique joint au rapport de janvier 2027)**

La courbe mensuelle du débit nocturne minimal reste comprise entre 195 et 205 m³/h de janvier 2024 à août 2025. Elle passe à 250 m³/h en septembre 2025, puis monte lentement jusqu'à 265 m³/h en janvier 2027. L'axe vertical du graphique commence à 180 m³/h.

**D. Les trois questions de la directrice générale**

1. Où et combien perdons-nous d'eau aujourd'hui, secteur par secteur ?
2. Quels facteurs semblent liés aux pertes (âge et matériau des canalisations, casses, densité des abonnés) ?
3. Pouvons-nous anticiper les casses des deux prochaines années, pour programmer le renouvellement des canalisations et l'activité de l'équipe de recherche de fuites ?

**E. Les outils envisagés (note de Mme Nathalie CORVESSE, responsable de la DSI)**

- **Tableur avancé**, dont disposent tous les cadres : solution actuelle ; aucun coût supplémentaire.
- **Outil de visualisation du marché** : connexion directe à la plateforme de télérelève, à la supervision, au logiciel des interventions et à la base patrimoniale du réseau ; rafraîchissement programmé chaque nuit ; tableaux de bord interactifs, cartes des secteurs, consultation sur ordinateur, tablette et téléphone ; abonnement de 25 000 € par an pour 30 utilisateurs et formation de 10 000 € la première année. Un agent de la DSI l'a déjà utilisé dans un emploi précédent.

### ANNEXE 1.4 – Le programme « télérelève et réduction des pertes »

**A. Objectifs à fin 2029 (plan « MORVÈZE EAU 2032 »)**

- Ramener les pertes de 5 millions de m³ (2026) à 3,5 millions de m³ par an, soit 1,5 million de m³ d'eau économisés chaque année ; trajectoire : 4,5 millions en 2027, 4 millions en 2028, 3,5 millions en 2029.
- Équiper en télérelève les 100 000 abonnés qui ne le sont pas encore (160 000 abonnés équipés fin 2029).
- Réparer une fuite signalée en trois jours au plus, contre dix jours en moyenne en 2026.

**B. Coûts annuels prévus de 2027 à 2029 (note de M. Sébastien VELOUZE, responsable du contrôle de gestion)**

| Poste | Coût annuel |
|---|---|
| Pose de 100 000 compteurs en télérelève en trois ans (90 € par compteur posé) | 3 M€ |
| Abonnement à la plateforme de télérelève | 0,3 M€ |
| Équipe de recherche de fuites créée en 2027 (six agents et leur matériel) | 0,6 M€ |
| **Total** | **3,9 M€** |

**C. Extrait du rapport mensuel de l'exploitation (janvier 2027, diffusé le 21 février 2027)**

> Volume produit : 2,1 millions de m³ — Casses réparées : 48 — Compteurs en télérelève posés : 61 200 — Débit de nuit des Faubourgs nord : 265 m³/h.

**D. Attentes exprimées**

**Mme Mathilde ROCHEVAL, directrice générale** : « Ce rapport ne me dit pas si nous sommes sur la trajectoire de 2029. Je veux une page que je lise en cinq minutes avant chaque comité de direction, qui me dise où nous en sommes, ce qui dérape et qui agit. »

**M. Gilles VAUQUIERS, président du conseil d'administration** : « Après l'été 2026, les élus veulent savoir chaque trimestre combien d'eau nous avons cessé de perdre et ce que chaque mètre cube économisé nous coûte. Je ne veux plus découvrir un problème dans la presse. »

**M. Thierry SALVANHAC, directeur de l'exploitation** : « Mes équipes ont besoin de savoir chaque matin où chercher. Mais si les chiffres sont faux, nous enverrons l'équipe de recherche de fuites au mauvais endroit. »

### Travail à faire

Mme ROCHEVAL veut que les données de télérelève et du réseau deviennent l'outil de la réduction des pertes, et que le programme qui leur est consacré soit piloté par un tableau de bord digne de ce nom. Vous mobiliserez pour cela les annexes 1.1 à 1.4 ainsi que vos connaissances professionnelles.

**1.1 – Chaîne de traitement des données de pertes (3 points)**

a) Définissez la chaîne de traitement des données et décrivez ses cinq étapes (collecte, nettoyage, structuration, analyse, restitution) appliquées aux sources de l'annexe 1.2.

b) Pour trois défauts constatés de l'annexe 1.2, indiquez l'étape de la chaîne concernée et le traitement à prévoir, puis montrez en quoi la maîtrise de cette chaîne conditionne les décisions de la régie.

**1.2 – Méthodes d'analyse (3 points)**

a) Associez à chacune des trois questions de la directrice générale (annexe 1.3 D) une méthode d'analyse de données (descriptive, exploratoire ou prédictive), en précisant pour chacune les données mobilisées et le résultat attendu.

b) Montrez deux limites de ces analyses qui ressortent des annexes.

**1.3 – Diagnostic, visualisations et outil décisionnel (4 points)**

a) À partir des annexes 1.2 et 1.3, formulez en quinze lignes au maximum un diagnostic argumenté des pertes du réseau : deux secteurs prioritaires, deux facteurs apparents et deux précautions de lecture.

b) Proposez deux visualisations, l'une destinée au directeur de l'exploitation, l'autre au conseil d'administration. Pour chacune, précisez le message, le type de représentation et l'indicateur représenté (formule, source, fréquence, cible et axe).

c) Recommandez, en le justifiant, l'un des deux outils de l'annexe 1.3 E.

**1.4 – Tableau de bord du programme (4 points)**

a) Proposez le tableau de bord du programme « télérelève et réduction des pertes » destiné à la directrice générale : quatre indicateurs qui équilibrent performance, risques et coûts, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.

b) Montrez, en trois arguments, en quoi ce tableau de bord corrige l'extrait du rapport mensuel de l'annexe 1.4 C.

c) Proposez le dispositif de revue et d'amélioration continue de ce tableau de bord : instance, fréquence, règle d'ajustement des cibles et règle de retrait d'un indicateur.

---

## DOSSIER 2 – SÉCURISER LE SYSTÈME DE SUPERVISION DES INSTALLATIONS ET SES ACCÈS (13 points)

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

---

## DOSSIER 3 – AUDITER LE PORTAIL DES ABONNÉS ET ORIENTER LA STRATÉGIE DE LA RELATION NUMÉRIQUE (13 points)

### ANNEXE 3.1 – Le portail des abonnés

**Note de Mme Élodie FARGEMONT, directrice de la clientèle, à la directrice générale (février 2027)**

**A. Fonctions et organisation**

Ouvert en 2020, le portail des abonnés est une solution en ligne de l'éditeur VELIZANE, utilisée sur abonnement (120 000 € par an). Il propose six fonctions : souscription et résiliation d'un contrat (emménagement, déménagement) ; mensualisation des paiements ; paiement en ligne des factures, par l'intermédiaire du prestataire de paiement de la banque de la régie ; suivi de la consommation (index relevés deux fois par an ou, pour les abonnés équipés en télérelève, consommation mensuelle importée chaque mois de la plateforme de télérelève) ; dépôt et suivi des réclamations ; alertes par courriel ou par SMS (facture disponible, échéance de paiement, travaux, restrictions d'usage de l'eau, conseils d'économie d'eau, lettre d'information, enquêtes).

Le logiciel de facturation, installé dans les locaux de la régie et administré par la DSI, reste la référence des contrats, des index, des factures et des paiements. Chaque nuit, un échange de fichiers transmet au logiciel de facturation les souscriptions, résiliations, changements de coordonnées et paiements saisis sur le portail, et transmet au portail les factures et les situations de compte. Un agent de la DSI suit ces échanges, parmi d'autres tâches.

La direction de la clientèle compte 60 agents, dont 35 agents de l'accueil (ouvert du lundi au vendredi de 8 h 30 à 17 h) et du centre d'appels (de 8 h à 18 h), qui consultent et modifient les comptes du portail pour le compte des abonnés.

**B. Chiffres de l'exercice 2026**

| Donnée | Valeur |
|---|---|
| Comptes ouverts sur le portail (fin 2026) | 82 000 : 70 000 comptes d'abonnés actuels, détenus par 66 000 abonnés, et 12 000 comptes d'anciens abonnés |
| Abonnés qui se sont connectés au moins une fois en 2026 | 64 000, soit 40 % des 160 000 abonnés |
| Démarches en ligne | 90 000 paiements de factures ; 6 000 des 16 000 emménagements et déménagements |
| Réclamations reçues | 12 000 : 6 000 sur le portail, 4 000 par téléphone, 2 000 à l'accueil ou par courrier ; délai moyen de traitement de 18 jours, pour un engagement de 8 jours inscrit dans la charte de service de la régie |
| Disponibilité du portail mesurée par l'éditeur | 99 % de l'année, soit près de 90 heures d'interruption ; le contrat prévoit 99,5 %, soit environ 45 heures au plus |
| Appels reçus par le centre d'appels | 150 000, dont 30 % portent sur une difficulté du portail (mot de passe, facture non visible, paiement non pris en compte) ; aux heures de pointe, un appel sur quatre n'aboutit pas |
| Satisfaction (enquête d'octobre 2026) | 62 % des utilisateurs du portail satisfaits ; 75 % des abonnés reçus à l'accueil ou au téléphone satisfaits |
| Demandes d'évolution du portail adressées par la direction de la clientèle à la DSI | 40 demandes : 12 réalisées, 10 refusées ou reportées, 18 en attente sans décision |

**C. Les relations entre les directions**

Faute d'instance pour trancher, les désaccords entre la direction de la clientèle et la DSI sont remontés à la directrice générale, qui a rendu six arbitrages en 2026, le plus souvent par courriel. En juin 2026, la direction de la clientèle a commandé directement à VELIZANE un module de prise de rendez-vous en ligne (15 000 €), sans associer la DSI ni la déléguée à la protection des données ; ce module n'est pas relié à l'agenda de l'accueil : en janvier 2027, 200 abonnés se sont présentés à un rendez-vous que les agents ne voyaient pas.

**Mme Élodie FARGEMONT, directrice de la clientèle** : « Nos abonnés attendent le service qu'ils trouvent auprès de leur banque. Cela fait deux ans que je demande les alertes de surconsommation ; chaque demande s'enlise à la DSI. »

**Mme Nathalie CORVESSE, responsable de la DSI** : « Chaque fonction nouvelle ajoute un échange avec la facturation que personne ne documente ; les interruptions de mars et de septembre viennent de là. Je ne mettrai rien en service sans recette ni examen de ses effets sur la facturation et sur la protection des données. »

**Mme Hélène BARJOLLE, déléguée à la protection des données** : « Je découvre les nouvelles fonctions du portail quand elles sont déjà en ligne. »

**Mme Mathilde ROCHEVAL, directrice générale** : « Je ne veux plus arbitrer seule, au cas par cas, des sujets dont je ne connais ni les coûts ni les risques, ni découvrir un désaccord le jour de la mise en service. Le conseil d'administration n'a jamais examiné le portail, alors que le plan en fait une priorité. »

### ANNEXE 3.2 – Constats préalables à l'audit et repères au 31/12/2026

**A. Constats relevés en février 2027 auprès de la direction de la clientèle, de la DSI et de la déléguée à la protection des données**

| N° | Constat |
|---|---|
| 1 | **Doublons et échanges avec la facturation** : 4 000 abonnés détiennent deux comptes, ouverts lors d'un emménagement sans rapprochement avec le contrat existant. L'échange de la nuit rejette en moyenne 150 enregistrements, repris à la main par le service de la facturation dans un délai moyen de huit jours ; aucun total n'est comparé entre le portail et la facturation. En 2026, 900 paiements en ligne ont été enregistrés en retard dans la facturation, ce qui a provoqué 600 relances envoyées à tort. |
| 2 | **Interruptions pendant les périodes de facturation** : sur les près de 90 heures d'interruption de 2026, 60 heures se situent pendant les deux vagues de facturation semestrielle (mars et septembre), quand les connexions triplent. La régie ne mesure pas elle-même la disponibilité du portail : elle reçoit chaque année le relevé de l'éditeur. |
| 3 | **Choix des abonnés en matière d'alertes** : 25 000 abonnés reçoivent les alertes facultatives (conseils d'économie d'eau, lettre d'information, enquêtes) ; la case correspondante est cochée d'avance lors de la création du compte ; le portail ne conserve ni la date ni le contenu du choix exprimé ; pour ne plus recevoir ces alertes, l'abonné doit appeler le centre d'appels. |
| 4 | **Comptes des anciens abonnés** : les 12 000 comptes d'anciens abonnés ouverts depuis 2020 restent consultables par les agents, avec les coordonnées, l'historique des consommations et des réclamations et, pour 5 000 d'entre eux, les coordonnées bancaires. Aucune durée de conservation n'est fixée ; le registre des activités de traitement de la régie ne comporte pas de fiche pour le portail, dont les données sont rattachées à la fiche « facturation » ; le contrat conclu avec VELIZANE ne précise pas le sort des données à la fin du contrat. |
| 5 | **Droits des agents de l'accueil et du centre d'appels** : les 35 agents disposent d'un profil unique qui permet de consulter tous les comptes, de modifier les coordonnées bancaires et l'adresse de facturation, de clore un compte et de clôturer une réclamation. Une modification de coordonnées bancaires n'est ni validée par un second agent ni signalée à l'abonné ; les droits n'ont jamais été revus depuis 2020. En 2026, deux abonnés ont signalé une modification de leurs coordonnées bancaires qu'ils n'avaient pas demandée. |
| 6 | **Réclamations non suivies** : 1 500 des 6 000 réclamations déposées sur le portail ont été clôturées automatiquement au bout de 30 jours sans réponse, selon un réglage d'origine de l'éditeur ; les réclamations reçues par téléphone sont suivies dans un tableur ; aucun indicateur de délai n'est produit. |

**B. Repères méthodologiques et réglementaires (au 31/12/2026)**

| Référence | Contenu | Situation au 31/12/2026 |
|---|---|---|
| Règlement (UE) 2016/679 relatif à la protection des données personnelles (RGPD) | Désignation obligatoire d'un délégué à la protection des données par les organismes publics ; il informe et conseille le responsable du traitement et contrôle le respect du règlement. Tenue d'un registre des activités de traitement, qui indique pour chaque traitement ses finalités, les catégories de personnes, de données et de destinataires, les délais prévus pour l'effacement des données et les mesures de sécurité. Protection des données dès la conception et par défaut : seules les données nécessaires sont traitées, durées de conservation comprises. Recours à un sous-traitant (par exemple un éditeur de solution en ligne) encadré par un contrat qui prévoit notamment les instructions, la sécurité, le sort des données à la fin du contrat et les audits. | Applicable depuis le 25/05/2018. Une proposition européenne de simplification (« omnibus numérique », 19/11/2025) modifiant ce règlement est en discussion et n'est pas applicable. |
| COBIT 2019 (ISACA) | Référentiel de gouvernance et de management de l'informatique : 40 objectifs répartis en cinq domaines (évaluer, diriger et surveiller ; aligner, planifier et organiser ; construire, acquérir et mettre en œuvre ; délivrer, servir et soutenir ; surveiller, évaluer et apprécier). | En vigueur |
| ITIL (PeopleCert) | Référentiel de bonnes pratiques de gestion des services informatiques : gestion des niveaux de service, des incidents, des changements, amélioration continue. | En vigueur |

Il n'est demandé aucune analyse juridique des obligations de la régie ni des droits des abonnés.

### ANNEXE 3.3 – Technologies émergentes signalées

**A. Deux propositions reçues par la direction de la clientèle (janvier 2027)**

1. **Assistant conversationnel fondé sur l'IA générative**, proposé par VELIZANE en option du portail : il répondrait jour et nuit, en langage courant, aux questions des abonnés (factures, mensualisation, emménagement et déménagement, restrictions d'usage), à partir de la documentation de la régie et des données du compte de l'abonné connecté, et transmettrait les demandes complexes à un conseiller aux heures d'ouverture. Il repose sur le modèle de langage d'un fournisseur tiers ; l'offre ne précise pas où les échanges sont hébergés. Coût : 60 000 € de mise en place, puis 90 000 € par an. L'éditeur annonce que 40 % des appels pourraient être traités sans conseiller. Une régie d'une autre région, qui l'utilise depuis 2026, indique qu'environ une réponse sur dix a été jugée inexacte pendant les trois premiers mois (démarches de déménagement, dates des restrictions d'usage).
2. **Alertes personnalisées de surconsommation et espace abonné enrichi grâce à la télérelève**, module de VELIZANE : consommation affichée jour par jour, comparaison avec des foyers semblables, alerte en cas de consommation continue pendant la nuit (signe d'une fuite après compteur, chez l'abonné), alerte au dépassement d'un seuil choisi par l'abonné, messages ciblés en période de restriction d'usage. Il suppose de transmettre chaque jour au portail les index de la plateforme de télérelève, au lieu d'un import mensuel. Il concerne les 60 000 abonnés équipés aujourd'hui, et les 160 000 abonnés en 2029. Coût : 80 000 € de mise en place, puis 30 000 € par an. En 2026, 1 200 abonnés ont découvert une fuite après compteur à la réception de leur facture semestrielle, en moyenne quatre mois après son début ; ces fuites sont à l'origine de 1 500 réclamations.

**B. Attentes exprimées**

**Mme Élodie FARGEMONT, directrice de la clientèle** : « Le centre d'appels est saturé. Avec l'assistant, nous pourrions répondre la nuit et le week-end dès cet été. »

**Mme Odile BRESSANDE, présidente du comité des usagers** (instance créée par la régie en 2021, qui réunit des représentants d'associations de consommateurs, de locataires et de quartiers) : « Nous voulons être prévenus d'une fuite avant la facture. Mais beaucoup d'abonnés âgés n'ont pas internet : il faut garder l'accueil et pouvoir toujours parler à un agent, pas à une machine. Et qui verra nos consommations jour par jour ? On saura quand une maison est vide. »

**M. Gilles VAUQUIERS, président du conseil d'administration** : « Après la sécheresse, les élus veulent que chaque abonné puisse suivre sa consommation et soit prévenu à temps d'une restriction. Mais ils ne veulent pas d'un service public déshumanisé, ni de dépenses dont on ne mesure pas l'utilité. »

**Mme Nathalie CORVESSE, responsable de la DSI** : « Un échange quotidien avec la télérelève, sur des échanges avec la facturation qui ne sont pas fiables, c'est fragile. Et si nous empilons les modules d'un seul éditeur, nous ne pourrons plus jamais en changer. »

**C. Les sources de veille aujourd'hui disponibles**

- **Abonnements** : deux revues professionnelles (l'une consacrée aux services d'eau, l'autre aux collectivités), reçues par la direction de l'exploitation et lues selon le temps disponible.
- **Salons** : le congrès annuel de la profession de l'eau, où se rendent le directeur de l'exploitation et la directrice de la clientèle ; aucun compte rendu n'est diffusé.
- **Échanges entre régies** : un réseau informel de régies de l'eau de la région se réunit deux fois par an ; la DSI n'y est pas invitée.
- **Éditeurs** : lettres d'information et démonstrations commerciales de VELIZANE, d'où proviennent les deux propositions.

Personne n'est chargé de la veille ; les informations recueillies ne sont ni conservées dans un espace commun ni présentées à la direction générale.

### Travail à faire

Mme ROCHEVAL veut présenter au conseil d'administration de juin 2027 les conclusions d'un audit du portail des abonnés, les orientations de la relation numérique avec les abonnés et la gouvernance qui la pilotera. Vous mobiliserez pour cela les annexes 1.1, 3.1, 3.2 et 3.3 ainsi que vos connaissances professionnelles.

**3.1 – Démarche de la mission d'audit du portail (2 points)**

a) Après avoir défini l'audit du système d'information, présentez la démarche de la mission d'audit du portail des abonnés : objectifs de performance et de conformité, périmètre et étapes.

b) Représentez sous forme de cartographie le processus « de la souscription au paiement » en cinq étapes, en précisant pour chacune l'acteur et l'application concernés, puis indiquez trois contrôles internes à vérifier, chacun rattaché à une étape.

**3.2 – Appréciation et diagnostic d'audit (3 points)**

a) Définissez les quatre critères d'appréciation du portail (fiabilité, efficacité, sécurité, conformité au RGPD) et rattachez à chacun au moins un constat de l'annexe 3.2.

b) Rédigez le diagnostic d'audit sous forme de tableau (constat, critère, risque, recommandation, priorité) pour quatre constats de l'annexe 3.2, puis justifiez l'ordre de priorité retenu.

**3.3 – Veille technologique et stratégie de la relation numérique (5 points)**

a) Après avoir défini la veille technologique active, proposez un dispositif de veille pour la régie, en précisant ses axes, ses sources, ses outils, ses acteurs, sa fréquence et sa diffusion, au regard de la situation décrite à l'annexe 3.3 C.

b) Analysez l'impact de chacune des deux technologies de l'annexe 3.3 sur le modèle de service de la régie, sous trois angles : la valeur pour les abonnés, les coûts et les risques.

c) Après avoir précisé ce qu'est une stratégie du système d'information alignée sur les objectifs métiers, déduisez-en deux orientations de la stratégie du système d'information de la relation avec les abonnés, alignées sur les priorités du plan « MORVÈZE EAU 2032 », et indiquez pour chacune la suite à donner à l'une des technologies de l'annexe 3.3.

**3.4 – Gouvernance de la relation numérique (3 points)**

a) Analysez, en trois points, les enjeux relationnels entre la DSI, la direction de la clientèle et la direction générale que révèle l'annexe 3.1.

b) Après avoir défini la gouvernance du système d'information, proposez une gouvernance de la relation numérique qui associe les parties prenantes clés (conseil d'administration, comité des usagers, directions concernées, déléguée à la protection des données), en précisant pour chaque instance sa composition, son rôle et sa fréquence.

c) Proposez, pour piloter cette gouvernance, un indicateur de performance et un critère de durabilité, chacun précisé par sa formule, sa source, sa fréquence, sa cible et son axe.
