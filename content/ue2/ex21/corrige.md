# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 21 — Dossier 3 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F05 ingénierie financière, F06 marchés, finance comportementale et fintech, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (Gordon-Shapiro, BPA, barème, liste noire, hors-programme ; taux de distribution, montants distribués et répartition du capital vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Politique de dividende et demande de dividende exceptionnel | `4.1.a` Déchiffrer la politique de dividende et les signaux associés | 4 |
| 3.2 Valeur de l'action par Gordon-Shapiro et offre de rachat | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier | 5 |
| 3.3 Rachat des actions des associés sortants | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital | 2 |
| 3.4 Plateforme de cession et outil de prévision de trésorerie | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs | 4 |
| **Total** | | **15** |

Part du calcul : environ 6 points (3.1-01 et 3.1-02, 3.2-01 à 3.2-04, 3.3-01 et 3.3-02). Part de l'analyse : environ 9 points. Ce dossier, placé en fin d'épreuve, comporte une large part rédactionnelle : il ne doit pas être bâclé faute de temps (`JUR-T15`).

---

### 3.1 Politique de dividende et demande de dividende exceptionnel (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Taux de distribution : 40,0 % (2021) ; 50,0 % (2022) ; 50,0 % (2023) ; 38,0 % (2024) ; 38,5 % (2025) ; proposition A : 40,0 % ; proposition B : 70,0 % | 1 |
| 3.1-02 | Montant distribué et part du résultat conservée : A : 4,80 M€ et 7,20 M€ ; B : 8,40 M€ (dont dividende exceptionnel : 3,60 M€, facultatif) et 3,60 M€ | 0,5 |
| 3.1-03 | Caractérisation : dividende lissé, en hausse de 0,25 € par an quel que soit le BPA, jamais réduit ; effet cliquet | 0,5 |
| 3.1-04 | Neutralité (Modigliani et Miller, 1961) appliquée au cas : pas de « dividende maison » possible sans marché des actions ; politique d'investissement modifiée par la proposition B | 0,5 |
| 3.1-05 | Signal (Spence, 1973 ; Ross, 1977) pour les associés familiaux et pour les futurs porteurs d'obligations | 0,5 |
| 3.1-06 | Coûts d'agence : associés dirigeants / associés non dirigeants ; associés / créanciers | 0,5 |
| 3.1-07 | Recommandation argumentée | 0,5 |

**Calculs (1,5 pt).** Taux de distribution = dividende par action / BPA.

| Exercice | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 A | 2026 B |
|---|---:|---:|---:|---:|---:|---:|---:|
| BPA (€) | 10,00 | 8,50 | 9,00 | 12,50 | 13,00 | 15,00 | 15,00 |
| Dividende par action (€) | 4,00 | 4,25 | 4,50 | 4,75 | 5,00 | 6,00 | 10,50 |
| **Taux de distribution** | **40,0 %** | **50,0 %** | **50,0 %** | **38,0 %** | **38,5 %** | **40,0 %** | **70,0 %** |

| Au titre de 2026 (M€) | Proposition A | Proposition B |
|---|---:|---:|
| Montant distribué (dividende par action × 800 000) | **4,80** | **8,40** (4,80 ordinaire + 3,60 exceptionnel) |
| Part du résultat de 2026 conservée (12,00 − montant distribué) | **7,20** | **3,60** |

**Caractérisation (0,5 pt).**
- De 2021 à 2025, le dividende progresse régulièrement de 0,25 € par an (+ 25 % en quatre ans), indépendamment du BPA : en 2022, le BPA recule de 15 % (coût de l'énergie) et le dividende augmente quand même, ce qui porte le taux de distribution à 50 % ; quand le BPA se redresse (2024-2025), le dividende ne rattrape pas la hausse et le taux revient vers 38 %.
- C'est une politique de **dividende lissé** : la société ne baisse jamais le dividende et ne le relève que modérément, ce qui traduit l'**effet cliquet** (réticence à diminuer un dividende une fois versé ; ajustement progressif décrit par Lintner, 1956).
- La proposition A (6,00 €, + 20 %) rompt avec la hausse de 0,25 € par an mais retrouve un taux de distribution proche de la moyenne de la période (43,3 % de 2021 à 2025, calcul facultatif) et le transforme en règle (40 %). La proposition B double plus que le dividende (+ 110 %) et ne conserve que 3,60 M€ du résultat, deux fois moins que A, au moment où le groupe poursuit son programme d'investissement.

**Neutralité (0,5 pt).** Selon Modigliani et Miller (1961), en marché parfait et à politique d'investissement donnée, la politique de dividende n'affecte pas la valeur de l'action : ce que l'associé reçoit en dividende, il le perd en valeur des actions, et celui qui veut un revenu peut se le procurer en cédant une partie de ses titres (« dividende maison »). Chez HIVERLANE, deux hypothèses manquent :
- **il n'existe aucun marché des actions** : un associé de la troisième génération ne peut pas se créer un dividende maison ; le dividende est son seul revenu tiré des actions, ce qui explique sa demande ;
- **la politique d'investissement n'est pas indépendante** de la distribution : avec la proposition B, le groupe renonce à ouvrir deux entrepôts (annexe 3.2). Distribuer 3,60 M€ de plus détruit de la valeur si ces investissements rapportent plus que la rentabilité exigée (question 3.2).

**Signal (0,5 pt).** Le dividende est informatif parce que les dirigeants en savent plus que les apporteurs de capitaux sur les perspectives du groupe.
- Au sens de Spence (1973), un signal est crédible s'il est coûteux à imiter. Pour les **associés familiaux qui ne travaillent pas dans le groupe**, et qui sont donc moins bien informés que la branche dirigeante, la hausse de 20 % de la proposition A est déjà un signal fort : la direction s'engage sur un dividende qu'elle juge soutenable, avec un BPA en hausse de 15,4 %. Le dividende exceptionnel de B n'apporte aucune information supplémentaire : il est réclamé par des associés et non décidé par la direction au vu de ses prévisions.
- Ross (1977) a construit la théorie du signal sur la structure financière : le niveau d'endettement révèle la confiance des dirigeants dans les flux futurs. Pour les **futurs porteurs d'obligations**, qui deviendront créanciers du groupe, un dividende exceptionnel versé juste avant l'émission se lit en sens inverse : il réduit la trésorerie et les capitaux propres, augmente l'endettement net, et montre que la priorité est donnée aux associés plutôt qu'au service de la dette. Une règle de distribution stable et modérée (40 %) signale au contraire la prudence financière qu'attendent les investisseurs obligataires.

**Coûts d'agence (0,5 pt).** Selon Jensen et Meckling (1976), les conflits d'intérêts entre mandants et mandataires créent des coûts.
- **Entre associés dirigeants et associés non dirigeants** : les associés de la troisième génération, qui ne contrôlent pas l'emploi des résultats conservés, peuvent craindre que la trésorerie serve des projets choisis par la branche dirigeante plutôt que leur intérêt ; le dividende réduit la trésorerie laissée à la discrétion de la direction (idée du *free cash flow*, Jensen, 1986). La demande de B est en partie une demande de contrôle sur l'emploi des résultats.
- **Entre associés et créanciers** : une distribution élevée transfère de la valeur des créanciers vers les associés (moins d'actifs pour garantir la dette). Les porteurs d'obligations s'en protégeront en exigeant une rémunération plus élevée ou des engagements limitant les distributions : la proposition B renchérirait l'émission de 60 M€.

**Recommandation (0,5 pt).**
- Retenir la proposition A : un dividende ordinaire de 6,00 € (4,80 M€) et une règle annoncée de 40 % du résultat net part du groupe, qui donne de la visibilité aux associés et aux investisseurs obligataires et conserve 7,20 M€ pour l'investissement.
- Refuser le dividende exceptionnel de 4,50 € : même qualifié d'exceptionnel, un dividende réclamé pour couvrir un besoin de revenu serait attendu de nouveau l'année suivante (effet cliquet), et la règle de 70 % diviserait par deux la part du résultat conservée par le groupe (3,60 M€ au lieu de 7,20 M€ en 2026).
- Distinguer la **rémunération** des associés (le dividende) de leur **besoin de liquidité** : offrir une solution de sortie aux associés qui veulent céder (rachat, question 3.3 ; plateforme, question 3.4), plutôt que d'augmenter la distribution pour tous.

**Réponses tolérées** : taux de distribution calculés en masse (dividendes / résultat net part du groupe, mêmes résultats) ; taux à deux décimales (38,46 % en 2025) ; dividende exceptionnel analysé comme un moyen d'éviter l'effet cliquet, s'il est ensuite discuté au regard des besoins réguliers des associés ; référence à Lintner (1956) et à Jensen (1986) facultative ; une recommandation intermédiaire (dividende un peu supérieur à 6,00 €, ou dividende exceptionnel limité et explicitement non reconductible) est acceptée si elle est justifiée par les besoins d'investissement et la préparation de l'émission obligataire.

**Erreurs fréquentes**
- `JUR-I04` — ne pas opposer le revenu immédiat des associés et le renforcement des fonds propres du groupe.
- `JUR-T14` et `JUR-M01` — citer Ross pour un signal par le dividende sans préciser qu'il s'agit à l'origine d'un signal par l'endettement ; confondre neutralité et absence d'intérêt du dividende ; oublier que la neutralité suppose un marché sur lequel l'associé peut céder ses titres.
- Développer l'imposition du dividende chez l'associé ou les règles juridiques de distribution : hors programme (UE 1).
- `JUR-T13` — exposé des théories sans lien avec HIVERLANE (associés non dirigeants, absence de marché, émission obligataire de 60 M€).

---

### 3.2 Valeur de l'action par le modèle de Gordon-Shapiro et offre de rachat (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Politique A : P0 = 6,00 / (9 % − 5 %) = 150,00 € | 0,5 |
| 3.2-02 | Politique B : P0 = 10,50 / (9 % − 1,5 %) = 140,00 € | 0,5 |
| 3.2-03 | Valeur sur une période (politique A) : à la valeur théorique dans un an (157,50 €), (6,00 + 157,50) / 1,09 = 150,00 € ; au prix de 126 €, (6,00 + 126,00) / 1,09 = 121,10 € | 1 |
| 3.2-04 | Rentabilité implicite du prix de 120 € : A : 6,00 / 120 + 5 % = 10,00 % ; B : 10,50 / 120 + 1,5 % = 10,25 % | 1 |
| 3.2-05 | Choix entre les politiques : la valeur dépend de la croissance que permet l'investissement, pas du dividende immédiat | 1 |
| 3.2-06 | Intérêt de l'offre pour les associés sortants et limites du modèle | 1 |

**Valeur théorique (1 pt).** Le modèle de Gordon-Shapiro actualise à l'infini un dividende qui croît à un taux constant g, inférieur à la rentabilité exigée k : P0 = prochain dividende / (k − g). Le prochain dividende, au titre de 2026, est perçu dans un an (annexe 3.5).
- Politique A : P0 = 6,00 / (0,09 − 0,05) = 6,00 / 0,04 = **150,00 €** (120,00 M€ pour les 800 000 actions).
- Politique B : P0 = 10,50 / (0,09 − 0,015) = 10,50 / 0,075 = **140,00 €** (112,00 M€).

**Valeur sur une période (1 pt).** L'associé qui conserve ses actions un an perçoit le prochain dividende puis cède ses actions au prix P1 : V0 = (prochain dividende + P1) / (1 + k).
- Cession à la valeur théorique dans un an : P1 = 150,00 × 1,05 = **157,50 €** ; V0 = (6,00 + 157,50) / 1,09 = 163,50 / 1,09 = **150,00 €**. On retrouve la valeur de Gordon-Shapiro : détenir l'action un an puis la revendre à sa valeur vaut autant que la détenir indéfiniment.
- Cession au prix estimé par OSTRALIS : V0 = (6,00 + 126,00) / 1,09 = 132,00 / 1,09 = **121,10 €**.

**Rentabilité implicite du prix de 120 € (1 pt).** Pour un acquéreur qui paie 120 €, dividende au titre de 2026 attaché, la rentabilité implicite est k = prochain dividende / prix + g :
- politique A : 6,00 / 120 + 5 % = 5,00 % + 5 % = **10,00 %** ;
- politique B : 10,50 / 120 + 1,5 % = 8,75 % + 1,5 % = **10,25 %**.
Dans les deux cas, elle dépasse la rentabilité exigée de 9 % : le prix de 120 € est inférieur à la valeur théorique.

**Choix entre les deux politiques (1 pt).**
- La politique B verse 4,50 € de plus dès 2026, mais la valeur de l'action est inférieure de 10,00 € (8,00 M€ pour l'ensemble des associés) : le dividende immédiat plus élevé ne compense pas la croissance perdue (1,5 % au lieu de 5 %), parce que les investissements abandonnés auraient rapporté plus que les 9 % exigés par les associés (les 30 % de résultat conservés en plus sous A apportent 3,5 points de croissance, soit une rentabilité marginale de 3,5 % / 30 % = 11,67 %, calcul facultatif).
- C'est la limite de la neutralité vue à la question 3.1 : la politique de dividende ne crée ni ne détruit de valeur tant qu'elle ne modifie pas l'investissement ; ici, la proposition B réduit l'investissement rentable.
- Le résultat dépend toutefois de l'écart entre les croissances retenues : avec une croissance de 4 % pour la politique A, sa valeur tomberait à 6,00 / 0,05 = 120,00 €, sous celle de B ; les deux politiques s'équivalent pour une croissance de 4,71 % (9 % − 6,00 / 140, calcul facultatif). La conclusion repose sur la crédibilité du plan d'investissement.

**Intérêt de l'offre pour les associés sortants et limites (1 pt).**
- L'offre de 120 € est inférieure de 20 % à la valeur théorique de 150 € (de 14,29 % à celle de 140 € sous la politique B) : c'est une **décote d'illiquidité** et de minorité, qui rémunère la société acheteuse (10 % au lieu de 9 %), donc les associés qui restent.
- Attendre un an et céder par OSTRALIS à 126 € vaut 121,10 € aujourd'hui, à peine plus que 120 € : le prix estimé par la plateforme (126 € = 80 % de 157,50 €) applique la même décote de 20 %. Pour 1,10 € d'écart, l'associé supporterait le risque que le prix ou le volume estimés ne soient pas atteints ; l'offre immédiate et certaine est préférable, ou constitue une base de négociation (une décote plus faible).
- **Limites du modèle** : une croissance de 5 % constante et illimitée dépasse la croissance de long terme de l'économie ; la valeur est très sensible à l'écart k − g (4 points seulement) ; la rentabilité exigée d'une société non cotée intègre une prime d'illiquidité estimée par le cabinet, sans observation de marché ; enfin, le modèle valorise un flux de dividendes, ce qui convient à un associé minoritaire mais ignore la valeur du contrôle.

**Réponses tolérées** : valeur sur une période présentée sans le premier calcul si le candidat explique que la valeur sur une période égale la valeur de Gordon-Shapiro quand P1 = P0 × (1 + g) : 0,5 point sur l'item 3.2-03 ; rentabilité implicite arrondie à 10,3 % pour B ; autres valeurs de sensibilité, si elles sont justes ; rapprochement avec les capitaux propres part du groupe tirés de la présentation (152 − 9 = 143 M€, soit 178,75 € par action, au-dessus de la valeur de 150 €, pour une rentabilité comptable de 12 / 143 = 8,39 %, inférieure à 9 %), présenté comme une limite du modèle ou comme un argument de négociation des sortants.

**Erreurs fréquentes**
- Augmenter le prochain dividende de la croissance alors que l'annexe le donne directement : 6,00 × 1,05 = 6,30 € et une valeur de 157,50 € sous la politique A (10,50 × 1,015 = 10,66 € et 142,10 € sous B). Les items 3.2-01 et 3.2-02 sont perdus ; la suite est notée en cohérence.
- Actualiser le prix de cession dans un an sans le dividende perçu : 126 / 1,09 = 115,60 €.
- Conclure que la politique B est meilleure parce que le dividende est plus élevé, ou que la valeur de 150 € est un prix de marché que les sortants pourraient obtenir.
- `JUR-T13` — calculs sans interprétation, ou interprétation sans lien avec l'offre de 120 € et la situation des associés sortants.

---

### 3.3 Rachat des actions des associés sortants (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | BPA pro forma : 6,00 M€ de rachat ; intérêts nets d'impôt 0,18 M€ ; résultat 11,82 M€ ; 750 000 actions ; BPA 15,76 € (contre 15,00 €, + 5,07 %) | 1 |
| 3.3-02 | Répartition après annulation : branche Agathe 44,80 % ; branche Bernard 32,00 % ; branche Hélène 16,80 % ; cadres 6,40 % | 0,5 |
| 3.3-03 | Commentaire : relution sans création de valeur par elle-même, transfert de valeur des sortants, équilibre entre branches, endettement accru | 0,5 |

**BPA pro forma (1 pt).** Convention de l'annexe 3.5 : rachat au 1er janvier 2026, intérêts de la ligne de crédit nets d'IS à 25 %.
- Montant du rachat : 50 000 × 120 = **6,00 M€**.
- Intérêts nets d'impôt : 6,00 × 4,00 % × (1 − 25 %) = **0,18 M€** ; résultat net part du groupe pro forma : 12,00 − 0,18 = **11,82 M€**.
- Actions après annulation : 800 000 − 50 000 = **750 000**.
- BPA pro forma : 11 820 000 / 750 000 = **15,76 €**, contre 15,00 € (+ 5,07 %).
- Le rachat est relutif parce que le rendement bénéficiaire au prix de rachat (15,00 / 120 = 12,50 %) dépasse le coût après impôt de la dette (4,00 % × 0,75 = 3,00 %).

**Répartition du capital (0,5 pt).**

| Associés | Actions avant | Part avant | Actions après | Part après |
|---|---:|---:|---:|---:|
| Branche de Mme Agathe DELMOURE | 336 000 | 42 % | 336 000 | **44,80 %** |
| Branche de M. Bernard DELMOURE | 240 000 | 30 % | 240 000 | **32,00 %** |
| Branche de Mme Hélène DELMOURE | 176 000 | 22 % | 126 000 | **16,80 %** |
| Cadres dirigeants | 48 000 | 6 % | 48 000 | **6,40 %** |
| **Total** | **800 000** | **100 %** | **750 000** | **100 %** |

La famille détient 94,93 % du capital après l'opération (712 000 / 750 000, calcul facultatif).

**Commentaire (0,5 pt).**
- **Le BPA n'est pas la valeur** : la hausse du BPA est mécanique (moins d'actions, financement peu coûteux après impôt). Le rachat enrichit les associés qui restent parce que le prix (120 €) est inférieur à la valeur (150 €) : les sortants leur transfèrent (150 − 120) × 50 000 = 1,50 M€, soit 2,00 € par action restante (valeur théorique après rachat sous la politique A : (120,00 M€ − 6,00 M€) / 750 000 actions = 152,00 €, calcul facultatif). Racheter à la valeur théorique ne créerait aucune richesse pour eux, quelle que soit la hausse du BPA.
- **Équilibre entre branches** : sans rien débourser, la branche dirigeante passe de 42 % à 44,80 % et la branche Hélène recule de 22 % à 16,80 % ; ce déplacement peut raviver les tensions entre branches et doit être expliqué ; les cadres se renforcent légèrement (6,40 %). Le rachat répond au besoin de liquidité des sortants sans faire entrer d'associé extérieur.
- **Qualité de crédit** : le rachat augmente l'endettement financier net de 6,00 M€ (de 118 M€ à 124 M€) et réduit d'autant les capitaux propres, quelques mois avant l'émission obligataire. Il faut le dimensionner prudemment (rachat étalé, ou financé en partie par la trésorerie de précaution que l'outil TRÉVANOR permettrait de réduire) et l'expliquer aux investisseurs comme une opération ponctuelle de reclassement du capital familial.

**Réponses tolérées** : BPA calculé sans le coût du financement s'il est présenté comme une première approche puis corrigé (16,00 €) : 0,5 point sur l'item 3.3-01 ; répartition arrondie à une décimale ; actions rachetées conservées par la société au lieu d'être annulées, si le candidat calcule les parts sur les 750 000 actions en circulation (mêmes résultats).

**Erreurs fréquentes**
- Oublier le coût du financement : BPA de 16,00 € (12,00 / 0,75), relution surestimée.
- Calculer la nouvelle répartition sur 800 000 actions, ou supposer que la branche Hélène conserve ses 176 000 actions.
- Présenter la hausse du BPA comme une création de valeur, sans la relier au prix de rachat inférieur à la valeur.
- Développer le régime juridique du rachat par une société de ses propres actions (autorisation, plafonds) : hors programme (UE 1).

---

### 3.4 Plateforme de cession et outil de prévision de trésorerie (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Rôle des nouveaux acteurs (fintechs, plateformes, systèmes privés d'échange de titres) pour un groupe non coté | 1 |
| 3.4-02 | Comparaison des deux formules d'OSTRALIS : liquidité, prix, contrôle familial, information, coût | 1 |
| 3.4-03 | Outil de TRÉVANOR : apports pour la stratégie financière, limites et risques | 1 |
| 3.4-04 | Recommandation argumentée | 1 |

**Rôle des nouveaux acteurs (1 pt).**
- Les fintechs sont de jeunes entreprises qui utilisent le numérique pour offrir des services financiers jusqu'ici rendus par les banques ou les marchés (paiement, prêt, gestion de trésorerie, mise en relation d'investisseurs). Les plateformes numériques et les systèmes privés d'échange de titres organisent des échanges hors des marchés réglementés, avec des coûts et des obligations plus légers qu'une introduction en bourse.
- Pour HIVERLANE, ils répondent à deux limites d'un groupe familial non coté : l'**absence de marché** des actions, qui prive les associés minoritaires de liquidité et rend le dividende non neutre (question 3.1) ; une **fonction financière** de taille moyenne, qui peut accéder à des outils de prévision réservés hier aux grands groupes.
- Leur intervention ne supprime pas les problèmes de fond : une plateforme réduit l'asymétrie d'information entre la société et les investisseurs sans la faire disparaître, et le prix y reste soumis à une décote d'illiquidité (question 3.2).

**Les deux formules d'OSTRALIS (1 pt).**

| Critère | « Cercle fermé » | « Marché ouvert » |
|---|---|---|
| Liquidité | faible : 10 000 à 20 000 actions par an ; les 50 000 actions des sortants mettraient de deux ans et demi à cinq ans à trouver preneur (50 000 / 20 000 et 50 000 / 10 000), davantage si d'autres associés vendent en même temps | les 50 000 actions en douze mois |
| Prix | encadré (± 10 % autour d'une valeur d'expert) : stable, mais peu de confrontation entre acheteurs | issu des enchères : 126 € net estimé, soit une valeur actuelle de 121,10 €, proche de l'offre de rachat |
| Contrôle familial | préservé : seuls associés, cadres et salariés achètent ; possibilité de renforcer l'actionnariat salarié | entrée d'associés minoritaires extérieurs, même filtrés ; risque d'attentes divergentes supplémentaires |
| Information | comptes annuels et valeur de référence | comptes semestriels, rapport d'activité, réponses aux questions : charge et diffusion d'informations sensibles, mais discipline utile pour préparer la relation avec les investisseurs obligataires |
| Coût | 15 000 € par an + 1 % par partie | 40 000 € par an + 4 % pour le vendeur |

La formule « cercle fermé » répond à un besoin régulier et limité de liquidité en préservant le contrôle ; la formule « marché ouvert » répond à une sortie importante et rapide, au prix de l'ouverture du capital et d'un coût plus élevé. Dans les deux cas, la valeur de référence ou le prix des séances donneront aux associés un repère de valeur qui leur manque aujourd'hui.

**L'outil de TRÉVANOR (1 pt).**
- **Apports** : des prévisions plus fiables et plus fréquentes réduisent la trésorerie de précaution (12 M€ → 8 M€, soit 4 M€ libérés) ; elles permettent de fixer le dividende et la taille d'un rachat en connaissant la capacité réelle du groupe, et de répondre aux attentes des investisseurs obligataires et de l'agence de notation en matière de prévisions de flux. Coût modeste : 30 000 € puis 48 000 € par an.
- **Limites et risques** : performance annoncée par le vendeur et mesurée chez d'autres clients (transport), à vérifier sur les données du groupe ; outil qui ne justifie pas toujours ses révisions (effet « boîte noire ») alors que le directeur financier reste responsable des prévisions présentées aux associés et aux prêteurs ; dépendance à un prestataire jeune, engagement de trois ans ; confidentialité et sécurité de données bancaires hébergées à distance ; une prévision reste une prévision, et un modèle construit sur le passé peut manquer un choc (prix de l'énergie).
- **La trésorerie libérée n'est pas un revenu** : les 4 M€ ne sont disponibles qu'une fois, alors que le dividende exceptionnel demandé (3,60 M€) se transformerait en attente durable (effet cliquet) ; ils seraient mieux employés à financer en partie le rachat des sortants (6,00 M€) ou à limiter l'endettement avant l'émission.

**Recommandation (1 pt).**
- Pour les **associés sortants** : proposer le rachat par la société (question 3.3), à un prix négocié à partir de la valeur théorique et de la décote, éventuellement en plusieurs tranches ; mettre en place la formule « cercle fermé » pour organiser ensuite la liquidité régulière des associés, des cadres et des salariés, sans ouvrir le capital à des tiers. Écarter la formule « marché ouvert » tant que la famille souhaite conserver la totalité du contrôle, ou la réserver à un besoin de sortie massif.
- Pour la **stratégie financière** : tester l'outil de TRÉVANOR sur une période limitée avant l'engagement de trois ans, garder la validation humaine des prévisions et encadrer la sécurité des données ; utiliser la trésorerie libérée pour l'investissement ou la réduction de l'endettement plutôt que pour un dividende exceptionnel.
- Ces solutions dissocient la **liquidité** des associés de leur **rémunération**, ce qui permet de maintenir la règle de distribution de 40 % (question 3.1).

**Réponses tolérées** : recommandation de la formule « marché ouvert » si le candidat la justifie par le volume à céder et la création d'un repère de prix, en mesurant la perte de confidentialité et l'entrée d'associés extérieurs ; référence à l'efficience (Fama, 1970) ou à l'asymétrie d'information (Akerlof, 1970) pour expliquer la décote sur un marché étroit, si elle est reliée au cas ; mention du cadre européen sur l'intelligence artificielle sans développement.

**Erreurs fréquentes**
- Décrire le fonctionnement technique de l'IA (apprentissage, algorithmes) au lieu de ses effets sur la décision financière : hors programme (UE 5).
- `JUR-M02` — présenter les nouveaux acteurs en général sans comparer les formules au regard du profil du groupe et des associés.
- Considérer que la plateforme fera disparaître la décote, ou que la trésorerie libérée par l'outil peut financer chaque année un dividende plus élevé.
- `JUR-T13` — avantages et inconvénients génériques, sans les chiffres de l'annexe (volumes, frais, trésorerie de précaution).

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 67-69 | politique de dividende (signal, neutralité, effet cliquet, frictions) ; rachats d'actions (effets sur le nombre d'actions, le BPA, les capitaux propres, signal) ; aspects juridiques exclus | [V] | F05 § 0, 2 et 3 |
| Guide pédagogique DSCG, juillet 2026, p. 75 | valeur théorique d'un titre sur une période (Gordon-Shapiro, dividende et prix de revente) | [V] | `perimetre_ue2.yaml` 5.2.b |
| Programme UE 2, l. 599-604 | fintechs, plateformes, systèmes privés d'échange de titres ; IA et finance algorithmique | [V] | F06 § 6 |
| Modigliani et Miller (1961) | neutralité du dividende en marché parfait, « dividende maison » | [V programme 4.1] | F10 § 2 ; F05 § 2 |
| Spence (1973) ; Ross (1977) | signal coûteux ; signal par la structure financière | [V programme 4.1] | F10 § 3 |
| Lintner (1956), facultatif | lissage du dividende, effet cliquet | [S] | F10 § 2 |
| Jensen et Meckling (1976) ; Jensen (1986), facultatif | coûts d'agence ; flux de trésorerie disponibles laissés à la discrétion des dirigeants | [V programme 2.1] ; [S] | F10 § 3 ; F05 § 2 |
| Gordon et Shapiro | valeur d'une action à croissance constante du dividende | [V programme 5.2, sans année] | F10 § 2 |
| Taux sans risque 4 %, prime de risque du marché 5 %, Euribor 3 mois 2,65 % | hypothèses d'énoncé, plausibles fin 2026 | [V] pour l'Euribor de septembre 2026 (2,635 %) ; [S] pour la prime | F11 § 1 et 2 |
