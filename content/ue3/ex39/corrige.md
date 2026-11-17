# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 3 – Contrôle de gestion et stratégie — Exercice d'entraînement n° 39 — Dossier 2 (7 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F04 pilotage des processus de production (yield management, qualité, cartographie), F10 pilotage stratégique et gestion prévisionnelle, F13 registre des auteurs (toutes à jour au 25/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (taux d'occupation des créneaux en indicateurs ; chiffre d'affaires, marge sur coût variable et résultat du centre en coût-volume-profit ; compte de résultat, budget de trésorerie et bilans en budgets ; détail par créneau, effets marginaux et sensibilité en calculs divers recalculés par script ; barème partiel sur 7 ; liste noire ; hors-programme).

Bien que le corrigé mentionne des auteurs, des textes et des données, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur le choix et la justification des outils, la justesse des calculs, la pertinence de l'analyse au regard du cas et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée (avertissement du sujet) ; pour chaque question, la présentation des concepts et outils avant leur mobilisation puis la conclusion sont notées. Une erreur n'est sanctionnée qu'une fois : les calculs et les analyses qui reprennent un chiffre faux de manière cohérente sont notés.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Cartographie du parcours de l'animal, étapes sans valeur pour le propriétaire, causes de l'attente classées et priorités | `2.1.a` Analyser la situation de gestion ; `2.1.b` Sélectionner des outils de gestion adaptés au contexte | 1 |
| 2.2 Taux d'occupation, demandes perdues, chiffre d'affaires, marge et résultat avec les deux grilles ; effet par créneau ; service non stockable, limites et grille recommandée | `2.1.d` Évaluer les résultats obtenus ; `2.1.e` Élaborer des préconisations en matière de gestion des processus de production | 2 |
| 2.3 Compte de résultat, budget de trésorerie et bilan prévisionnels de 2028 ; point bas de trésorerie, capacité de remboursement, sensibilité au taux d'occupation de nuit | `3.1.b` Élaborer des documents prévisionnels ; `3.1.d` Interpréter les résultats obtenus | 2,5 |
| 2.4 Note au directeur administratif et financier et au directeur du centre (20 lignes au maximum) | `2.1.f` Produire une synthèse sur les décisions concernant les processus de production ; `3.1.a` S'approprier la boucle du pilotage stratégique ; `3.1.f` Produire une synthèse portant sur la gestion prévisionnelle | 1,5 |
| **Dossier 2 – Réorganiser le centre d'urgences** | | **7** |

---

## DOSSIER 2 – RÉORGANISER LE CENTRE D'URGENCES : PROCESSUS, TARIFICATION SELON LES CRÉNEAUX ET ÉTATS PRÉVISIONNELS DE LA FILIALE (7 points)

### 2.1 Représenter le parcours de l'animal, repérer les étapes sans valeur pour le propriétaire, classer les causes de l'attente et dégager les priorités (1 pt)

**Compétences visées :**
- `2.1.a` — Analyser la situation de gestion (cartographie de processus)
- `2.1.b` — Sélectionner des outils de gestion adaptés au contexte (gestion stratégique de la qualité et analyse des dysfonctionnements)

**Barème (1 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Parcours représenté à partir de l'annexe 2.1 : neuf étapes dans l'ordre, acteur de chacune, **cinq files d'attente** (accueil, tri, consultation, examens, guichet de sortie) avec leurs durées, et repérage des étapes sans valeur pour le propriétaire (attentes, questions posées deux fois, paiement au guichet après les soins, compte rendu tardif) ; le temps de présence d'un cas non urgent sans examen (**4 h 08**, dont **3 h 25** d'attente pour **25 minutes** de consultation) ou une autre mesure de la part du temps utile est un plus | 0,5 |
| 2.1-02 | Outil choisi et justifié (diagramme causes-effets d'**Ishikawa**, 5 M), causes de l'annexe 2.1 classées dans les cinq familles, puis **hiérarchie** : causes que le centre maîtrise et peut traiter vite (tri confié à un poste dédié avec une grille écrite, accueil téléphonique séparé, dossier transmis par les cliniques, paiement au lit ou en fin de soins, second échographe ou planning du bloc) ; cause de milieu (pic de demande non urgente de la fin de semaine, cliniques qui ferment le samedi à midi) qui relève de la tarification et du report de la demande (question 2.2) | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Représentation du parcours : une **cartographie du processus** (logigramme ou tableau étapes / acteurs / attentes / valeur pour le propriétaire). C'est l'outil adapté parce que l'annexe décrit un processus de service, étape par étape, et que la question demande de repérer les files d'attente et les étapes sans valeur. Le parcours est le processus de réalisation du centre ; l'accueil, la facturation, l'imagerie et le laboratoire extérieur sont des processus de soutien qui le ralentissent.
- Classement des causes : le **diagramme d'Ishikawa** (diagramme causes-effets, dit « en arêtes de poisson ») range les causes d'un effet, ici l'attente de plus de trois heures, en cinq familles : main-d'œuvre, méthodes, matériel, milieu, matière. Il convient parce que l'annexe ne donne ni fréquence ni coût par cause : un diagramme de Pareto n'est pas constructible.
- Alternatives acceptées : un tableau des causes classées par famille, ou un arbre des causes, s'il hiérarchise ; une lecture par goulots d'étranglement (le tri et le guichet sont les goulots du samedi soir), si elle reste reliée aux faits. Non accepté : un diagramme de Pareto avec des fréquences inventées ; une liste de causes sans classement ni priorité.

**Réponse attendue**

*Concept.* Cartographier un processus, c'est représenter l'enchaînement de ses activités, de l'entrée (l'animal et son propriétaire) à la sortie (l'animal soigné, la facture réglée, la clinique informée), avec les acteurs, les durées et les points d'attente, pour repérer ce qui crée de la valeur pour le bénéficiaire et ce qui n'en crée pas.

*Parcours d'un animal un soir de fin de semaine* (durées moyennes de l'annexe 2.1)

| Étape | Acteur | File d'attente avant l'étape | Durée de l'étape | Valeur pour le propriétaire |
|---|---|---|---|---|
| 1. Appel préalable | auxiliaire de l'accueil (seule) | — | 4 min par appel, 40 appels entre 18 h et 23 h | utile (conseil), mais elle immobilise l'accueil : 160 minutes sur 300, soit **53,33 %** de la soirée de l'auxiliaire |
| 2. Accueil et enregistrement | auxiliaire de l'accueil | **15 min** | 8 min | faible : informations recopiées faute de dossier transmis |
| 3. Tri selon la gravité | vétérinaire de consultation, entre deux consultations | **40 min** | 5 min | forte pour une urgence ; questions déjà posées à l'accueil |
| 4. Attente de la consultation | — | **2 h 10** (cas non urgent), 25 min (urgence) | — | aucune |
| 5. Consultation et devis | vétérinaire | — | 25 min | forte : cœur du service |
| 6. Examens | vétérinaire, auxiliaire ; laboratoire extérieur ; échographe partagé avec le bloc | **50 min** | variable | forte pour le diagnostic ; l'attente n'en a aucune |
| 7. Soins, chirurgie, hospitalisation | vétérinaires, auxiliaires de soins | — | variable | forte |
| 8. Sortie et facturation | auxiliaire de l'accueil (même poste) | **20 min** | 5 min | aucune pour le propriétaire, qui paie alors que l'animal est déjà soigné ou hospitalisé |
| 9. Compte rendu à la clinique traitante | vétérinaire, en fin de garde | envoi le lendemain | — | faible quand il arrive après l'appel du propriétaire (un cas sur quatre) |

Pour un cas non urgent sans examen, le propriétaire reste **4 h 08** au centre (15 + 8 + 40 + 5 + 130 + 25 + 20 + 5 minutes), dont **3 h 25** d'attente, pour **25 minutes** de consultation : c'est ce que décrit le propriétaire du chat (« trois heures et demie »). Les étapes sans valeur pour le propriétaire sont les cinq attentes, le double questionnement (accueil puis tri), le paiement au guichet après les soins et le compte rendu tardif, qui fait perdre de la valeur à la clinique traitante. Un seul poste, l'accueil, cumule trois activités (téléphone, enregistrement, facturation) : il est le premier goulot du parcours.

*Causes de l'attente des soirs de fin de semaine (Ishikawa, 5 M)*

| Famille | Causes relevées dans l'annexe 2.1 |
|---|---|
| Main-d'œuvre | une seule auxiliaire à l'accueil le soir, pour le téléphone, l'enregistrement et le paiement ; un seul vétérinaire de tri, qui trie « quand il le peut », après sa consultation |
| Méthodes | tri sans grille écrite ; cas non urgents vus dans l'ordre d'arrivée, sans rendez-vous ni report proposé ; questions posées deux fois ; paiement à la sortie, au guichet ; compte rendu rédigé en fin de garde |
| Matériel | un seul échographe, partagé avec le bloc de chirurgie ; coursier du laboratoire toutes les deux heures |
| Milieu | pic de la demande en fin de semaine, dont la moitié porte sur des cas non urgents ; cliniques du groupe fermées le samedi à midi qui envoient tout au centre ; salle d'attente commune aux chiens et aux chats |
| Matière (ce qui entre dans le processus) | animaux reçus sans dossier ni historique de la clinique traitante ; appels qui sont des demandes de conseil plutôt que des urgences |

*Priorités.* Le centre peut agir vite, et à faible coût, sur les méthodes et la main-d'œuvre : poste de tri dédié aux heures de pointe, avec une grille écrite qui reprend les informations de l'accueil ; accueil téléphonique séparé de l'enregistrement (ou conseil téléphonique assuré par une auxiliaire de soins), règlement en fin de soins dans la salle de consultation ou à l'hospitalisation ; transmission du dossier par la clinique du groupe qui adresse l'animal. L'échographe partagé appelle un arbitrage d'équipement (planning du bloc ou second appareil). La cause principale reste de milieu : un afflux de cas non urgents concentré sur la fin de semaine, alors que la journée de semaine a de la place. Elle ne se traite pas par l'organisation seule : elle justifie la consultation programmée et la tarification selon les créneaux étudiées à la question 2.2, et une règle commune avec les cliniques du groupe pour le samedi après-midi.

**Réponses tolérées**
- Une cartographie en logigramme, en couloirs par acteur ou en tableau ; un regroupement des neuf étapes en cinq ou six activités.
- Le classement de la salle d'attente commune en « matériel » ou de l'absence de dossier en « méthodes » : les frontières entre familles sont discutables, la cohérence et la hiérarchie comptent.

**Erreurs fréquentes**
- `JUR-T09` — Traiter le centre comme s'il n'avait ni processus ni fournisseurs : le laboratoire extérieur et le coursier font partie du parcours.
- `JUR-T07` — Dessiner un diagramme d'Ishikawa sans en tirer de priorité d'action, ou construire un Pareto sans données de fréquence.
- `JUR-T03` — Recopier l'annexe étape par étape sans repérer les attentes ni les étapes sans valeur.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.1 (« cartographie de processus », « gestion stratégique de la qualité et analyse des dysfonctionnements ») ; guide p. 120 (processus de service, outils classiques de la qualité : Pareto, Ishikawa) | cartographie, diagramme causes-effets | [V] | F04 § 9 |
| Diagramme d'Ishikawa (Kaoru Ishikawa, années 1960 ; 5 M) | classement des causes | [S] | F13 § 8 ; F04 § 9 |

---

### 2.2 Comparer la grille actuelle et la grille différenciée, mesurer l'effet par créneau, expliquer la démarche, en apprécier les limites et recommander une grille (2 pts)

**Compétences visées :**
- `2.1.d` — Évaluer les résultats obtenus (optimisation des capacités : yield management)
- `2.1.e` — Élaborer des préconisations en matière de gestion des processus de production

**Barème (2 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Grille actuelle : capacités (10 000, 5 000, 3 650, 10 350 consultations) ; taux d'occupation **45,00 %**, **80,00 %**, **80,00 %**, **100,00 %** ; **1 650** demandes de fin de semaine dirigées ailleurs ; chiffre d'affaires du centre **6 600,0 k€** (contrôle avec la présentation), marge sur coût variable **4 941,3 k€**, résultat **− 58,7 k€** | 0,5 |
| 2.2-02 | Grille différenciée : demandes reportées (3 500 cas non urgents en journée, 1 760 en soirée, 3 360 consultations programmées), taux d'occupation **88,60 %**, **83,20 %**, **70,14 %**, **86,96 %**, plus aucune demande perdue ; chiffre d'affaires **6 827,9 k€**, marge **5 141,1 k€**, résultat **141,1 k€**, soit **+ 199,8 k€** | 0,5 |
| 2.2-03 | Effet créneau par créneau : fin de semaine **+ 211,5 k€**, nuit **− 28,8 k€**, journée **+ 27,5 k€**, soirée **− 10,4 k€** (somme 199,8 k€) et lecture marginale : la baisse de prix ne paie que là où la capacité est inemployée et la demande sensible au prix (journée), pas en soirée (par exemple : il faudrait + 17,65 % de demande pour compenser la baisse, contre + 10 % attendus) ; la fin de semaine gagne parce que la capacité saturée est rendue aux urgences et que les cas non urgents remplissent la journée | 0,5 |
| 2.2-04 | Service non stockable et capacité fixe par créneau qui justifient une tarification différenciée dans le temps ; limites (acceptation par les propriétaires, image d'un groupe de praticiens déjà critiqué sur les tarifs de nuit, urgences vraies non reportables et fiabilité du tri, cannibalisation des cliniques du groupe et de la demande existante, moindre recette par passage) ; **grille recommandée** : grille différenciée **sans la baisse de soirée** (résultat **151,5 k€**), consultation programmée de nuit conservée pour le service et la charge des nuits malgré son coût, conditions de réussite | 0,5 |

**Choix de l'outil et alternatives acceptées**

- Outil retenu : un **raisonnement marginal par créneau**, sur la capacité de chaque créneau, propre au **yield management** : pour chaque créneau, capacité, passages réalisés dans la limite de la capacité, taux d'occupation, puis chiffre d'affaires et marge sur coût variable ; l'effet d'une mesure est la variation de marge qu'elle provoque. Il convient parce que les coûts fixes ne changent pas d'une grille à l'autre : seule la marge sur coût variable départage les grilles.
- Alternatives acceptées : un tableau différentiel (grille différenciée − grille actuelle) au lieu de deux tableaux complets, s'il donne les totaux demandés ; une présentation par catégorie de passage (urgences, cas non urgents, consultations programmées) plutôt que par créneau. Non accepté : un programme linéaire ou un classement par marge unitaire sans tenir compte de la capacité de chaque créneau.

**Conventions rappelées**

- Capacité = nombre de créneaux × vétérinaires en consultation × consultations par vétérinaire et par créneau ; passages réalisés dans la limite de la capacité, demandes au-delà dirigées vers d'autres structures (des cas non urgents) ; taux d'occupation = passages réalisés / capacité × 100.
- Chiffre d'affaires d'un passage = consultation + actes et soins ; marge sur coût variable = chiffre d'affaires − coûts variables ; résultat = marge du centre − coûts fixes (5 000 k€).
- Montants en k€ à une décimale, taux à deux décimales.

**Réponse attendue**

*Grille actuelle (2026)*

Marge par passage : urgence = tarif + 180 − 70 = tarif + 110 € ; cas non urgent = tarif + 30 − 10 = tarif + 20 €.

| Créneau | Capacité | Demandes | Passages réalisés | Dirigées ailleurs | Taux d'occupation | Chiffre d'affaires (k€) | Coûts variables (k€) | Marge (k€) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Journée de semaine (250 × 2 × 20) | 10 000 | 4 500 | 4 500 | 0 | 45,00 % | 705,0 | 165,0 | 540,0 |
| Soirée de semaine (250 × 2 × 10) | 5 000 | 4 000 | 4 000 | 0 | 80,00 % | 800,0 | 184,0 | 616,0 |
| Nuit (365 × 1 × 10) | 3 650 | 2 920 | 2 920 | 0 | 80,00 % | 768,0 | 161,2 | 606,8 |
| Fin de semaine (115 × 3 × 30) | 10 350 | 12 000 | 10 350 | **1 650** | **100,00 %** | 2 142,0 | 463,5 | 1 678,5 |
| **Passages en urgence** | **29 000** | **23 420** | **21 770** | **1 650** | **75,07 %** | **4 415,0** | **973,7** | **3 441,3** |
| Activité adressée | | | | | | 2 185,0 | 685,0 | 1 500,0 |
| **Centre** | | | | | | **6 600,0** | **1 658,7** | **4 941,3** |

Détail de la fin de semaine : 6 000 urgences × (90 + 180) = 1 620,0 k€ ; 4 350 cas non urgents vus (6 000 − 1 650) × (90 + 30) = 522,0 k€. Le chiffre d'affaires retrouve les 6 600 k€ de la présentation. Résultat du centre = 4 941,3 − 5 000,0 = **− 58,7 k€**. Les 1 650 demandes perdues représentent 1 650 × 110 € = 181,5 k€ de marge.

*Grille différenciée*

Demandes reportées : cas non urgents de journée 2 500 × 1,40 = **3 500** ; de soirée 1 600 × 1,10 = **1 760** ; consultations programmées 50 % × 720 = **360** (nuit) + 50 % × 6 000 = **3 000** (fin de semaine) = **3 360**, vues en journée ; restent 360 cas non urgents la nuit et 3 000 en fin de semaine.

| Créneau | Capacité | Passages réalisés | Dirigées ailleurs | Taux d'occupation | Chiffre d'affaires (k€) | Coûts variables (k€) | Marge (k€) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Journée de semaine : 2 000 urgences, 3 500 cas non urgents à 45 €, 3 360 consultations programmées à 40 € | 10 000 | 8 860 | 0 | 88,60 % | 977,7 | 208,6 | 769,1 |
| Soirée de semaine : 2 400 urgences, 1 760 cas non urgents à 65 € | 5 000 | 4 160 | 0 | 83,20 % | 791,2 | 185,6 | 605,6 |
| Nuit : 2 200 urgences, 360 cas non urgents | 3 650 | 2 560 | 0 | 70,14 % | 714,0 | 157,6 | 556,4 |
| Fin de semaine : 6 000 urgences et 3 000 cas non urgents à 110 € | 10 350 | 9 000 | 0 | 86,96 % | 2 160,0 | 450,0 | 1 710,0 |
| **Passages en urgence** | **29 000** | **24 580** | **0** | **84,76 %** | **4 642,9** | **1 001,8** | **3 641,1** |
| Activité adressée | | | | | 2 185,0 | 685,0 | 1 500,0 |
| **Centre** | | | | | **6 827,9** | **1 686,8** | **5 141,1** |

Journée : 2 000 × 240 = 480,0 ; 3 500 × 75 = 262,5 ; 3 360 × 70 = 235,2 → 977,7 k€. Résultat du centre = 5 141,1 − 5 000,0 = **141,1 k€**, soit **+ 199,8 k€** par rapport à la grille actuelle, pour + 227,9 k€ de chiffre d'affaires et 2 810 passages de plus. Tous les créneaux restent sous le repère de 90 % : l'attente des cas non urgents devrait passer sous une heure, y compris en fin de semaine.

*Effet créneau par créneau* (consultations programmées rattachées au créneau d'où vient la demande)

| Créneau | Calcul | Effet sur la marge (k€) |
|---|---|---:|
| Fin de semaine | majoration des urgences 6 000 × 20 € = + 120,0 ; cas non urgents restés : 3 000 × 130 − 4 350 × 110 = − 88,5 ; consultations programmées 3 000 × 60 € = + 180,0 | **+ 211,5** |
| Nuit | cas non urgents partis 360 × 140 € = − 50,4 ; consultations programmées 360 × 60 € = + 21,6 | **− 28,8** |
| Journée | baisse sur la demande existante 2 500 × (− 15 €) = − 37,5 ; demande nouvelle 1 000 × 65 € = + 65,0 | **+ 27,5** |
| Soirée | baisse sur la demande existante 1 600 × (− 15 €) = − 24,0 ; demande nouvelle 160 × 85 € = + 13,6 | **− 10,4** |
| **Total** | | **+ 199,8** |

Lecture : la fin de semaine porte tout le gain. Le centre y était saturé : chaque cas non urgent déplacé vers la journée libère une place pour une urgence, que l'on ne refuse plus, et la journée de semaine, à moitié vide, absorbe ces passages à un coût presque nul (les vétérinaires y sont déjà présents). La baisse de prix n'est rentable que si la demande nouvelle compense la perte sur la demande existante : il faut + 23,08 % de demande en journée (37,5 / 65 € = 577 passages ; + 40 % attendus) et **+ 17,65 %** en soirée (24,0 / 85 € = 282 passages ; + 10 % attendus seulement). La soirée, déjà occupée à 80 %, n'a pas besoin d'être remplie : la baisse y détruit de la marge. La consultation programmée de nuit coûte 28,8 k€, car un cas non urgent de nuit rapporte 140 € de marge contre 60 € le lendemain ; elle répond pourtant aux plaintes sur les tarifs de nuit et allège les nuits (taux d'occupation de 80,00 % à 70,14 %), ce qui compte pour garder des vétérinaires qui refusent les gardes (axe 1 du plan).

*Pourquoi une tarification selon les créneaux.* Le **yield management** module les prix dans le temps et par segment pour tirer le meilleur revenu d'une capacité fixe et périssable. Le centre réunit ses conditions : son service n'est **pas stockable** (une consultation de journée non vendue est perdue, elle ne peut pas servir le samedi soir) ; sa capacité est fixée par créneau (vétérinaires présents) ; ses coûts sont surtout fixes (5 000 k€ contre 70 € ou 10 € de coût variable par passage) ; sa demande se segmente (urgences vraies, insensibles au prix et non reportables ; cas non urgents, reportables et sensibles au prix) ; le tri permet de classer chaque demande. Moduler les prix déplace la demande non urgente des créneaux saturés vers les créneaux creux, au lieu d'ajouter des vétérinaires qui manquent.

*Limites.*
- **Acceptation par les propriétaires** : la majoration de fin de semaine (+ 22,22 % sur la consultation) touche aussi les urgences, sans alternative ; l'hypothèse d'une acceptation de 50 % de la consultation programmée n'est pas éprouvée ; un propriétaire inquiet préfère être vu tout de suite.
- **Image du groupe** : un groupe de praticiens qui se distingue des groupes adossés à des investisseurs par la proximité et la continuité des soins risque d'apparaître comme « faisant payer l'urgence », alors que les tarifs de nuit sont déjà critiqués ; la grille doit être affichée et expliquée (prix plus bas pour qui peut attendre).
- **Urgences vraies** : elles ne se reportent pas. Tout repose sur la fiabilité du tri : un cas mal classé et renvoyé au lendemain est un risque pour l'animal et pour la réputation ; le tri doit suivre une grille écrite (question 2.1).
- **Cannibalisation** : la baisse de journée profite aussi aux 2 500 propriétaires qui venaient déjà (− 37,5 k€) ; surtout, des consultations non urgentes moins chères au centre en journée concurrencent les cliniques du groupe, ce qui déplace la marge au lieu de la créer au niveau du groupe.
- **Recette moyenne par passage en baisse** (202,80 € à 188,89 €) : le gain vient du volume et de la capacité mieux employée ; il dépend d'hypothèses de report qu'il faudra vérifier.

*Recommandation.* Retenir la grille différenciée **sans la baisse de soirée** : chiffre d'affaires 6 836,7 k€, marge 5 151,5 k€, résultat **151,5 k€** (+ 10,4 k€ par rapport à la grille différenciée complète). Garder la majoration de fin de semaine et la consultation programmée, cœur du dispositif ; garder la consultation programmée de nuit pour le service et la charge des nuits, malgré son coût. Conditions : grille de tri écrite, rendez-vous du lendemain réellement disponibles, tarifs affichés, accord avec les cliniques du groupe sur le samedi après-midi, suivi mensuel du taux d'occupation et de l'attente par créneau.

**Réponses tolérées**
- Les demandes perdues réparties entre urgences et cas non urgents au prorata, si l'hypothèse est écrite : marge et résultat changent, l'ordre des conclusions aussi peu.
- Une recommandation qui garde la grille différenciée complète en justifiant la baisse de soirée par l'attente ou par l'image, ou qui renonce à la consultation programmée de nuit pour sa marge (− 28,8 k€), si elle est argumentée.
- Le revenu par consultation disponible (chiffre d'affaires des passages / capacité), s'il est défini par le candidat : 152,24 € avec la grille actuelle, 160,10 € avec la grille différenciée.

**Erreurs fréquentes**
- `JUR-V02` — Ne pas reconnaître que la capacité de chaque créneau est la contrainte : compter les 12 000 demandes de fin de semaine comme des passages, ou raisonner sur la seule marge unitaire.
- `JUR-P02` — Ne pas appliquer les conventions de l'annexe : oublier les actes et soins dans le chiffre d'affaires d'un passage, oublier les consultations programmées dans la capacité de journée.
- `JUR-T05` — Calculer sans relier la grille à la stratégie : image d'un groupe de praticiens, plaintes sur les tarifs de nuit, manque de vétérinaires.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 2.1 (« optimisation des capacités : gestion des goulots d'étranglement et yield management ») ; guide p. 120 (spécificités des services non stockables et yield management) | tarification selon les créneaux | [V] | F04 § 6 |
| Conditions du yield management (capacité fixe et périssable, coûts fixes élevés, demande segmentable), taux d'occupation, limites (cannibalisation, image) | analyse et limites | [S] | F04 § 6 |
| Guide p. 120 (approche marginale « qui devra servir à l'ensemble de l'UE ») | raisonnement marginal | [V] | F04 § 8 |

---

### 2.3 Établir le compte de résultat, le budget de trésorerie et le bilan prévisionnels de 2028, puis les interpréter (2,5 pts)

**Compétences visées :**
- `3.1.b` — Élaborer des documents prévisionnels (budgets et états financiers prévisionnels) à partir de prévisions
- `3.1.d` — Interpréter les résultats obtenus

**Barème (2,5 pts)**

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Compte de résultat 2028 : chiffre d'affaires **9 012**, charges variables **2 253** (25 %), personnel 4 400, autres charges fixes 1 200, dotations **700** (400 + 300), résultat d'exploitation 459, intérêts 58, résultat **401 k€** | 0,5 |
| 2.3-02 | Budget de trésorerie : encaissements des cliniques avec le décalage d'un mois (760, 784, 744, 776, créance d'ouverture comprise), charges variables (526, 555, 576, 569, dette d'ouverture comprise), emprunt de 1 600 en T1, extension de 1 800 en T1, échéances (capital et intérêts) ; soldes − 54, + 154, + 274, + 134 ; trésorerie de fin **226**, **380**, **654**, **788 k€** | 0,5 |
| 2.3-03 | Bilan au 31/12/2028 : immobilisations nettes 3 500, créances 268, trésorerie 788 ; capital 2 500, réserves 268, résultat 401, emprunt de la société mère **1 200**, fournisseurs 187 ; total **4 556 k€**, équilibré ; un contrôle de la trésorerie (CAF − variation du besoin en fonds de roulement − investissement + emprunt − remboursement = + 508) est un plus | 0,5 |
| 2.3-04 | Interprétation de la trésorerie et du remboursement : point bas au **T1 (226 k€)**, sous le minimum de 250 k€ (− 24 k€), environ dix jours de décaissements d'exploitation, parce que l'extension est payée en janvier et que l'emprunt n'en couvre que 1 600 ; le règlement en deux fois proposé par le fournisseur règle le problème (1 126 puis 380 k€) ; **CAF 1 101 k€**, 2,75 fois le remboursement annuel de 400 k€ : la filiale peut rembourser la mère sur ses propres flux | 0,5 |
| 2.3-05 | Sensibilité au taux d'occupation de nuit : 73 passages et **16,4 k€** de marge par point ; à 45 % : 1 095 passages de moins, − 246,4 k€, résultat **154,6 k€** ; taux qui annule le résultat **35,59 %** ; la demande de nuit de 2026 ne remplirait que 35,07 % : sans les cliniques indépendantes annoncées et sans vétérinaires de nuit recrutés, l'extension ne couvre pas ses coûts | 0,5 |

**Conventions rappelées**

- Le tiers des factures aux cliniques et des charges variables d'un trimestre est réglé au trimestre suivant ; propriétaires au comptant ; personnel et autres charges payés dans le trimestre.
- Pas de stocks, de TVA ni d'impôt sur les bénéfices ; emprunt, échéances et intérêts de l'annexe 2.3 utilisés tels quels.
- Capacité d'autofinancement simplifiée = résultat + dotations. Montants en k€ sans décimale.

**Réponse attendue**

*Compte de résultat prévisionnel de 2028* (k€)

| Produits et charges | Montant |
|---|---:|
| Passages en urgence (propriétaires) | 5 928 |
| Animaux adressés et soins intensifs (cliniques) | 3 084 |
| **Chiffre d'affaires** | **9 012** |
| Charges variables (25 % × 9 012) | − 2 253 |
| **Marge sur coût variable** | **6 759** |
| Charges de personnel (4 × 1 100) | − 4 400 |
| Autres charges fixes (4 × 300) | − 1 200 |
| Dotations aux amortissements (4 000 / 10 + 1 800 / 6 = 400 + 300) | − 700 |
| **Résultat d'exploitation** | **459** |
| Intérêts de l'emprunt (16 + 15 + 14 + 13) | − 58 |
| **Résultat de 2028** | **401** |

*Budget de trésorerie de 2028* (k€)

Charges variables par trimestre : 549, 558, 585, 561. Encaissements des cliniques : T1 = 2/3 × 768 + 248 (factures de décembre 2027) = 760 ; T2 = 2/3 × 792 + 1/3 × 768 = 784 ; T3 = 480 + 264 = 744 ; T4 = 536 + 240 = 776. Charges variables payées : T1 = 2/3 × 549 + 160 = 526 ; T2 = 372 + 183 = 555 ; T3 = 390 + 186 = 576 ; T4 = 374 + 195 = 569.

| | T1 | T2 | T3 | T4 |
|---|---:|---:|---:|---:|
| Trésorerie de début | 280 | 226 | 380 | 654 |
| Propriétaires | 1 428 | 1 440 | 1 620 | 1 440 |
| Cliniques | 760 | 784 | 744 | 776 |
| Emprunt de la société mère | 1 600 | | | |
| **Total des encaissements** | **3 788** | **2 224** | **2 364** | **2 216** |
| Charges variables | 526 | 555 | 576 | 569 |
| Charges de personnel | 1 100 | 1 100 | 1 100 | 1 100 |
| Autres charges fixes | 300 | 300 | 300 | 300 |
| Extension (dette sur immobilisations) | 1 800 | | | |
| Remboursement du capital | 100 | 100 | 100 | 100 |
| Intérêts | 16 | 15 | 14 | 13 |
| **Total des décaissements** | **3 842** | **2 070** | **2 090** | **2 082** |
| Solde | − 54 | + 154 | + 274 | + 134 |
| **Trésorerie de fin** | **226** | **380** | **654** | **788** |

Contrôle : 280 − 54 + 154 + 274 + 134 = 788.

*Bilan prévisionnel simplifié au 31 décembre 2028* (k€)

| Actif | | Passif | |
|---|---:|---|---:|
| Immobilisations brutes | 5 800 | Capital | 2 500 |
| Amortissements (1 600 + 700) | − 2 300 | Réserves et report à nouveau | 268 |
| Immobilisations nettes | 3 500 | Résultat de 2028 | 401 |
| Créances sur les cliniques (1/3 × 804) | 268 | Emprunt de la société mère (1 600 − 400) | 1 200 |
| Trésorerie | 788 | Dettes fournisseurs (1/3 × 561) | 187 |
| **Total** | **4 556** | **Total** | **4 556** |

Contrôle par les flux : CAF 1 101 − hausse du besoin en fonds de roulement (créances + 20, fournisseurs + 27 : − 7) − extension payée 1 800 + emprunt 1 600 − remboursement 400 = + 508 = 788 − 280.

*Interprétation.*
- **Trésorerie au plus bas au 1er trimestre : 226 k€**, sous le minimum de 250 k€ demandé par le groupe. Ce n'est pas l'exploitation qui pèse (elle dégage 246 k€ au T1 après intérêts) mais le calendrier : l'extension (1 800 k€) est payée en janvier, l'emprunt n'en couvre que 1 600, et le solde de 200 k€, plus le premier remboursement de capital (100 k€), sortent de la trésorerie d'ouverture. 226 k€ représentent une dizaine de jours de décaissements d'exploitation (1 926 k€ par trimestre) : un retard d'activité ou d'encaissement suffirait à créer un découvert. Le règlement de l'extension en deux fois, que le fournisseur accepte sans supplément, porte la trésorerie à 1 126 k€ en T1 et 380 k€ en T2 : le minimum est respecté chaque trimestre, sans financement supplémentaire. La trésorerie se reconstitue ensuite (788 k€ fin 2028).
- **Capacité de rembourser la société mère** : la CAF de 1 101 k€ couvre 2,75 fois le remboursement annuel de 400 k€ ; les 1 200 k€ restant dus représentent un peu plus d'un an de CAF. La filiale rembourse sur ses propres flux, comme le demande M. PRUNIÈRES, et redevient bénéficiaire (401 k€, contre un résultat proche de l'équilibre en 2026). Cette capacité dépend toutefois de prévisions ambitieuses : + 36,55 % de chiffre d'affaires par rapport à 2026 (9 012 contre 6 600 k€).
- **Sensibilité au taux d'occupation de nuit** : un point de taux correspond à 73 passages (1 % de 7 300) et à 73 × 225 € = **16,4 k€** de marge (300 € − 25 % = 225 € par passage). À **45 %** au lieu de 60 %, il manque 1 095 passages et 246,4 k€ de marge : le résultat tombe à **154,6 k€** et la CAF à 854,6 k€ (le remboursement reste couvert, mais la trésorerie du T1 baisse encore d'environ 68 k€ si le manque se répartit sur l'année : 82,1 k€ de recettes en moins, pour 13,7 k€ seulement de charges variables payées en moins, puisqu'un tiers est réglé au trimestre suivant). Le résultat s'annule quand il manque 401 000 / 225 = 1 782,2 passages, soit 2 597,8 passages de nuit : un taux de **35,59 %**. Or la demande de nuit de 2026, avec la grille différenciée, ne remplirait que 2 560 / 7 300 = 35,07 % de la nouvelle capacité (résultat de − 8,5 k€) : **le second poste de nuit n'est rentable que si les vingt cliniques indépendantes adressent réellement leurs urgences et si les vétérinaires de nuit sont recrutés** (un poste sur trois ne l'était pas au 1er mars 2027). C'est l'indicateur à suivre en priorité.

**Réponses tolérées**
- Un compte de résultat présenté par nature sans la ligne de marge sur coût variable.
- Une présentation mensuelle ou par moitié de trimestre, si les totaux trimestriels concordent.
- Le flux de trésorerie d'exploitation après intérêts (1 108 k€) au lieu de la CAF pour juger du remboursement.
- Un point de sensibilité arrondi à 16,4 k€ appliqué tel quel (taux d'annulation de 35,55 % au lieu de 35,59 %), si la méthode est juste.

**Erreurs fréquentes**
- `JUR-P02` — Ne pas appliquer les délais de l'annexe : encaisser toutes les factures des cliniques dans le trimestre, oublier la créance et la dette d'ouverture, ou décaisser l'extension sans tenir compte de la dette sur immobilisations du bilan d'ouverture.
- `JUR-T10` — Erreurs de base : porter l'emprunt ou son remboursement dans le compte de résultat, oublier les dotations de l'extension, déduire un impôt.
- `JUR-G02` — Décrire les tableaux sans les interpréter : ne pas comparer le point bas au minimum de 250 k€, ne pas relier la sensibilité à la demande des cliniques indépendantes et au recrutement des vétérinaires de nuit.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 3.1 (« budgets financiers : budget de trésorerie et états financiers prévisionnels ») ; guide p. 125 (budgets opérationnels, puis budget de trésorerie et états financiers prévisionnels simplifiés, amortissements simples) | compte de résultat, trésorerie et bilan prévisionnels | [V] | F10 § 4 |
| Guide p. 146-147 (analyse de la trésorerie, du résultat et du bilan prévisionnels) | interprétation | [V] | F10 § 4 |

---

### 2.4 Note au directeur administratif et financier et au directeur du centre (1,5 pt)

**Compétences visées :**
- `2.1.f` — Produire une synthèse rédigée et structurée portant sur les décisions concernant les processus de production
- `3.1.a` — S'approprier la boucle du pilotage stratégique
- `3.1.f` — Produire une synthèse rédigée et structurée portant sur la gestion prévisionnelle

**Barème (1,5 pt)**

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Mesures de réorganisation du parcours tirées de la question 2.1 et grille recommandée avec ses chiffres (résultat de − 58,7 à 151,5 k€, plus aucune demande perdue, taux d'occupation sous 90 %) et ses conditions (tri écrit, rendez-vous disponibles, affichage, accord avec les cliniques, suivi) | 0,5 |
| 2.4-02 | Situation prévisionnelle de 2028 : résultat 401 k€, point bas de 226 k€ au T1 et règlement de l'extension en deux fois, remboursement couvert par la CAF ; dépendance au taux d'occupation de nuit (35,59 % annule le résultat) | 0,5 |
| 2.4-03 | Boucle du pilotage : les budgets déclinent l'axe 2 du plan « LORVENANCE 2031 » en objectifs chiffrés ; le suivi trimestriel (taux d'occupation par créneau, attente, passages de nuit, trésorerie) compare réel et prévu et permet de confirmer l'extension ou de la réorienter (consultations de nuit ramenées à un poste, soins intensifs gardés) ; note structurée, 20 lignes au maximum, qui prend position | 0,5 |

**Réponse attendue** (exemple de note, 20 lignes)

> **Objet : réorganisation du centre d'urgences et prévisions 2028 de LORVENANCE Urgences**
>
> **1. Le parcours.** Un cas non urgent passe plus de quatre heures au centre un samedi soir pour 25 minutes de consultation. L'attente naît de l'organisation (accueil seul pour le téléphone, l'enregistrement et le paiement ; tri entre deux consultations ; échographe partagé avec le bloc) : tri dédié aux heures de pointe avec une grille écrite, accueil téléphonique séparé, règlement en fin de soins, dossier transmis par la clinique.
>
> **2. La grille.** La moitié des demandes de fin de semaine ne sont pas urgentes, alors que la journée est occupée à 45 %. La grille différenciée, assortie d'une consultation programmée le lendemain matin, supprime les 1 650 demandes perdues, ramène chaque créneau sous 90 % d'occupation et fait passer le résultat de − 58,7 à 141,1 k€. Je recommande de la retenir sans la baisse de soirée, qui coûte 10,4 k€ : résultat de 151,5 k€. Conditions : un tri fiable (les urgences vraies ne se reportent pas), des rendez-vous disponibles, des tarifs affichés, un accord avec nos cliniques sur le samedi après-midi.
>
> **3. 2028.** Avec l'extension, le résultat prévu atteint 401 k€ et la CAF (1 101 k€) couvre 2,75 fois le remboursement annuel dû à la société mère. La trésorerie tombe à 226 k€ au premier trimestre, sous le minimum de 250 k€ : il faut accepter le règlement de l'extension en deux fois proposé par le fournisseur. Le point faible est la nuit : sous 35,59 % d'occupation des consultations de nuit, le résultat devient négatif, et la demande de 2026 n'atteindrait que 35,07 %.
>
> **4. Le pilotage.** Ces budgets traduisent l'axe 2 du plan « LORVENANCE 2031 » en objectifs chiffrés. Je propose un suivi trimestriel du taux d'occupation et de l'attente par créneau, des passages de nuit et de la trésorerie, comparés au budget. Si la nuit reste sous 45 % fin 2028, il faudra revenir à un seul poste de consultation de nuit et garder les soins intensifs ; si elle dépasse 60 %, l'extension sera confirmée.

**Grille de notation de la note**
- Structure (parcours, grille, prévisions, pilotage), chiffres justes repris des questions précédentes, préconisations faisables et prise de position : jusqu'à 1 pt (items 2.4-01 et 2.4-02).
- Boucle du pilotage (stratégie → budget → suivi → adaptation) et forme (20 lignes au maximum, destinataires, objet) : 0,5 pt (item 2.4-03). Une note de plus de 20 lignes perd ce demi-point.

**Réponses tolérées**
- Une recommandation de grille différente de celle du corrigé, si elle est cohérente avec la question 2.2.
- Un autre seuil de réorientation de l'extension (50 %, 40 %), s'il est justifié par la sensibilité calculée.

**Erreurs fréquentes**
- `JUR-G02` — Présenter le budget comme un aboutissement, sans dire comment le suivi des réalisations confirmera ou réorientera l'extension.
- `JUR-T04` — Note sans structure, sans destinataires ni conclusion, ou qui dépasse la longueur demandée.
- `JUR-T05` — Note purement financière, sans lien avec l'attente des propriétaires, l'image du groupe et la charge des nuits pour les vétérinaires.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 3, partie 3.1 (« boucle du pilotage stratégique : articulation stratégie / plans / budgets / écarts / adaptation ») ; guide p. 125 (le contrôle budgétaire doit permettre de confirmer ou de réorienter les choix stratégiques) | boucle du pilotage | [V] | F10 § 2 |
| Guide p. 113 et sujet 2025 q. 1.5 (synthèse bornée à 20 lignes) | forme de la note | [V] | F04 § 0 ; F10 § 0 |
