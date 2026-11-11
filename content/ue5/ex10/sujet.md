# DSCG UE 5 — Management des systèmes d'information — Exercice d'entraînement n° 10

**DOSSIER 1 – EXPLOITER LES DONNÉES DE TÉLÉRELÈVE POUR RÉDUIRE LES PERTES ET PILOTER LE PROGRAMME (14 points)**

Durée conseillée : 1 h 03 (14 points sur 40, pour une épreuve de 3 heures, coefficient 1 ; environ 4,5 minutes par point).

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
