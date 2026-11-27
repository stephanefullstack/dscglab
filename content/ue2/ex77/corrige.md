# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 77 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F05 ingénierie financière, F06 marchés financiers, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (moyennes, variances, covariance, corrélation et bêta des séries, MEDAF, Gordon-Shapiro et sensibilités, rentabilité et croissance implicites, PER, actions nouvelles, produit net, répartition du capital et dilution, BPA, méthode du capital-risque, proposition des fondateurs, rachat de 100 %, barème, liste noire, hors-programme ; liquidité, coûts de l'offre, décotes, actions aux bornes de la fourchette, nombre maximal d'actions cessibles, résultat supplémentaire et rendement requis vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une valeur de Gordon-Shapiro calculée avec une rentabilité exigée erronée à la question 2.2).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Liquidité, coûts, motifs et contraintes du transfert | `4.2.e` Analyser les introductions en bourse, les retraits de la cotation et les offres publiques | 2 |
| 2.2 Bêta calculé sur les séries, MEDAF, prime de risque, fragilité du bêta et limite du MEDAF | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier ; `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 2,5 |
| 2.3 Gordon-Shapiro, rentabilité espérée au cours, PER des comparables, comparaison au cours et à la fourchette | `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier ; `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP | 2,5 |
| 2.4 Décote, asymétrie d'information et signal de la cession du holding | `5.1.b` Maîtriser les enseignements des asymétries d'information (Akerlof, 1970) ; `4.2.e` Analyser les introductions en bourse, les retraits de la cotation et les offres publiques | 1,5 |
| 2.5 Actions nouvelles, produit net, capital et voix, dilution, majorité, BPA | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital ; `4.2.e` Analyser les introductions en bourse, les retraits de la cotation et les offres publiques | 3,5 |
| 2.6 Méthode du capital-risque, cycle de vie, participation minoritaire ou rachat | `3.3.c` Savoir calculer la valeur d'une entreprise en fonction de son cycle de vie ; `4.2.b` Analyser les motifs des opérations de réorganisation | 4 |
| 2.7 Recommandation : prix, quantité cédée, conditions de réussite | `4.2.e` Analyser les introductions en bourse, les retraits de la cotation et les offres publiques | 1 |
| **Total** | | **17** |

Part du calcul : environ 10 points (2.1-01, 2.1-02, 2.2-01 à 2.2-03, 2.3-01 à 2.3-03, 2.4-01, 2.5-01 à 2.5-05, 2.6-01 à 2.6-03 et 2.6-05). Part de l'analyse : environ 7 points. Le dossier reprend du sujet commun le capital et sa répartition, le cours du 30 avril 2027, le résultat net de 2026, le taux sans risque, la prime de risque du marché et le taux d'IS. Il calcule lui-même le bêta et la rentabilité exigée de l'action : aucun taux d'actualisation du groupe n'est donné en commun, et la rentabilité de 8,00 % n'est pas un CMPC ; elle ne sert qu'à évaluer l'action et à juger le rendement des fonds levés pour les actionnaires. Aucun résultat d'un autre dossier n'est utilisé, et l'offre n'est supposée réalisée dans aucun autre dossier.

---

### 2.1 Liquidité, coûts, motifs et contraintes du transfert (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Capitaux échangés **97 200 €** par séance (0,05 % du capital) ; rotation annuelle du flottant **35,71 %** ; séances pour acheter 1 % du capital : **100** aujourd'hui, **25** selon la banque | 0,5 |
| 2.1-02 | Coût direct **1,50 M€**, soit **5,00 %** du montant brut ; coût annuel après impôt **0,30 M€**, soit **2,78 %** du résultat net de 2026 | 0,5 |
| 2.1-03 | Motifs pour BRÉVOLAN, pour la famille et pour les investisseurs, reliés au cas | 0,5 |
| 2.1-04 | Coûts et contraintes ; ce que change la liquidité (prix plus fiable, décote de liquidité réduite, accès futur au marché) | 0,5 |

**Calculs.**
- Capitaux échangés par séance : 6 000 × 16,20 € = **97 200 €**, soit 6 000 / 12 000 000 = **0,05 %** du capital.
- Rotation annuelle du flottant : 6 000 × 250 / 4 200 000 = **35,71 %** : il faut près de trois ans pour que les actions du public changent une fois de mains.
- Séances pour acheter 1 % du capital (120 000 actions) en restant à 20 % des volumes : 120 000 / (20 % × 6 000) = 120 000 / 1 200 = **100 séances**, près de cinq mois de bourse ; avec 24 000 actions par séance : 120 000 / 4 800 = **25 séances**, environ cinq semaines.
- Coût direct de l'offre : commissions 3,00 % × 30,00 = 0,90 M€ + frais fixes 0,60 M€ = **1,50 M€**, soit **5,00 %** du montant brut. Les commissions sur les actions cédées sont payées par le holding, pas par BRÉVOLAN.
- Coût annuel supplémentaire après impôt : 0,40 × (1 − 25 %) = **0,30 M€** par an, soit 0,30 / 10,80 = **2,78 %** du résultat net de 2026. Ce coût est récurrent : le coût direct de l'offre n'est payé qu'une fois.

**Motifs (0,5 pt).**
- **Pour BRÉVOLAN** : lever 30,00 M€ de fonds propres pour financer l'extension de Nevers et la participation dans VISTRAMÉO sans alourdir la dette ; diversifier ses sources de financement en ouvrant l'accès à des investisseurs institutionnels qui, selon la banque, ne peuvent pas acheter des actions non admises sur un marché réglementé ; gagner en visibilité auprès des clients et des analystes (de deux à six), ce qui compte pour un groupe qui vend 80 % de ses machines hors de France ; disposer d'une action plus liquide, utilisable plus tard pour d'autres opérations.
- **Pour la famille** : rendre une partie de son patrimoine liquide pour les deux branches qui ne travaillent pas dans le groupe, par la cession du holding, sans perdre le contrôle ; faire mieux valoriser les actions qu'elle garde si la décote de liquidité se réduit (PER de 18 contre 20 pour les comparables du marché réglementé : question 2.3).
- **Pour les investisseurs** : pouvoir entrer et sortir à un coût raisonnable (écart entre prix d'achat et de vente de 1,10 % aujourd'hui), suivre la société grâce à une information plus riche et plus régulière, et acheter un titre qui entre dans les indices suivis par les fonds indiciels.

**Coûts, contraintes et liquidité (0,5 pt).**
- **Coûts** : 1,50 M€ une fois, puis 0,30 M€ après impôt chaque année ; à ces coûts directs s'ajoute la décote du prix de l'offre (question 2.4), coût indirect supporté par les actionnaires actuels.
- **Contraintes** : information financière plus abondante et plus fréquente, gouvernance renforcée (comité d'audit, relations suivies avec les investisseurs), exposition plus forte aux variations du marché et aux attentes de court terme des investisseurs ; une famille qui ne garderait qu'une majorité étroite verrait son contrôle plus exposé (question 2.5). Les conditions du transfert et le contrôle de l'AMF sont des faits d'énoncé : l'AMF veille à la qualité de l'information donnée aux investisseurs.
- **Ce que change la liquidité** : aujourd'hui, un investisseur institutionnel mettrait 100 séances à constituer une ligne de 1 % du capital ; il ne le fait pas, ou il exige une décote. Une action liquide se vend vite et à un prix proche de sa valeur : la prime de liquidité exigée baisse, le cours reflète mieux l'information disponible (efficience informationnelle au sens de Fama, 1970), et le bêta calculé devient plus fiable (question 2.2). La liquidité ne crée pas de flux ; elle réduit le coût d'entrée et de sortie des actionnaires, ce qui peut rapprocher le PER de celui des comparables.

**Réponses tolérées** : rotation calculée sur le capital total (6 000 × 250 / 12 000 000 = 12,50 %) si le candidat le signale ; séances arrondies en semaines ou en mois ; coût annuel rapporté au résultat net prévu pour 2027 (2,50 %).

**Erreurs fréquentes**
- Ajouter les commissions sur les actions cédées au coût de BRÉVOLAN : le produit et les frais de la cession reviennent au holding.
- Confondre le produit de l'offre pour la société et le produit de la cession pour l'actionnaire familial.
- Énumérer des motifs généraux d'introduction en bourse sans les rattacher à une société déjà cotée qui change de marché (`JUR-T13`).
- Développer les règles boursières du transfert, qui sont des faits d'énoncé.

**Références** : F05 § 6 (objectifs et mécanismes d'une introduction : financement, liquidité, notoriété, diversification de l'actionnariat ; coûts directs et indirects) [V guide p. 70-71 ; S] ; F06 § 1 (Euronext, Euronext Growth, rôle de l'AMF comme garant de l'information) et § 5 (accès au marché vu du marché) [S ; V guide p. 71] ; F10 Fama (1970) [V programme 5.1] ; programme 4.2.e « objectifs d'une IPO : financement, diversification des sources, liquidité, transparence » [V guide p. 71].

---

### 2.2 Bêta calculé sur les séries, MEDAF, prime de risque, fragilité du bêta et limite du MEDAF (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Rentabilités moyennes : action **9,00 %**, indice **6,00 %** ; variance de l'indice **100 %²**, soit **0,0100** (écart-type 10,00 %) | 0,5 |
| 2.2-02 | Covariance **80 %²**, soit **0,0080** ; **bêta = 0,0080 / 0,0100 = 0,80**, interprété | 0,5 |
| 2.2-03 | Rentabilité exigée : 4,00 % + 0,80 × 5,00 % = **8,00 %** | 0,5 |
| 2.2-04 | Ce que mesure la prime de risque du marché et ce que rémunère le MEDAF | 0,5 |
| 2.2-05 | Fragilité du bêta d'une action peu échangée sur six observations ; une limite du MEDAF | 0,5 |

**Calculs (rentabilités en %, convention de population : division par 6).**

| Année | Action (A) | Indice (M) | A − 9 | M − 6 | (M − 6)² | (A − 9) × (M − 6) |
|---|---:|---:|---:|---:|---:|---:|
| 2021 | 27 | 21 | 18 | 15 | 225 | 270 |
| 2022 | 12 | 15 | 3 | 9 | 81 | 27 |
| 2023 | − 9 | − 4 | − 18 | − 10 | 100 | 180 |
| 2024 | 0 | 9 | − 9 | 3 | 9 | − 27 |
| 2025 | 21 | 2 | 12 | − 4 | 16 | − 48 |
| 2026 | 3 | − 7 | − 6 | − 13 | 169 | 78 |
| **Total** | **54** | **36** | **0** | **0** | **600** | **480** |

- Rentabilités moyennes : action 54 / 6 = **9,00 %** ; indice 36 / 6 = **6,00 %**.
- Variance de l'indice : 600 / 6 = **100 %²**, soit **0,0100** ; écart-type 10,00 %.
- Covariance : 480 / 6 = **80 %²**, soit **0,0080**.
- **Bêta** = 0,0080 / 0,0100 = **0,80** : sur la période, l'action a varié en moyenne de 0,80 % quand l'indice variait de 1 % ; elle apparaît moins sensible au marché que la moyenne des actions.
- **Rentabilité exigée** (MEDAF) : 4,00 % + 0,80 × 5,00 % = **8,00 %**.
- Pour aller plus loin (non exigé) : variance de l'action 918 / 6 = 153 %², écart-type 12,37 % ; corrélation 0,0080 / (0,1237 × 0,10) = 0,6468 ; le risque lié au marché (0,80² × 0,0100 = 0,0064) ne représente que 41,83 % de la variance de l'action, le reste étant propre à BRÉVOLAN et éliminable par la diversification.

**Ce que mesure la prime de risque (0,5 pt).** Plus un placement est incertain, plus la rentabilité exigée est élevée. La prime de risque du marché (5,0 %) est le supplément de rentabilité que les investisseurs exigent pour détenir le portefeuille de marché plutôt qu'un placement sans risque. Le MEDAF (Sharpe, 1964) ne rémunère que le risque systématique, celui que la diversification n'élimine pas : la prime exigée de BRÉVOLAN est la prime du marché multipliée par son bêta, soit 0,80 × 5,00 % = 4,00 %. Le risque propre à BRÉVOLAN (dépendance aux États-Unis, change, famille) n'est pas rémunéré, puisqu'un investisseur diversifié peut l'éliminer.

**Fragilité du bêta et limite du MEDAF (0,5 pt).**
- **Six observations seulement** : une seule année atypique change fortement le bêta. Sans 2025 (+ 21 % pour l'action contre + 2 % pour l'indice), le bêta calculé sur les cinq autres années serait de 0,93 au lieu de 0,80 (illustration) ; l'estimation est peu précise.
- **Action peu échangée** : certains jours sans échange, un cours qui suit le marché avec retard ; une partie des mouvements de l'indice ne se retrouve dans le cours qu'à la période suivante, ce qui affaiblit la covariance mesurée. L'analyste estime que le bêta tend alors à sous-estimer la sensibilité réelle au marché : pour un fabricant de biens d'équipement dont les commandes suivent l'investissement industriel, un bêta proche de 1, ou supérieur, serait plus vraisemblable. Avec un bêta de 1,00, la rentabilité exigée serait de 9,00 % (illustration). Le bêta mesure aussi le passé : le groupe a changé (exportations, services) et changera avec l'offre.
- **Une limite du MEDAF** (une suffit) : un seul facteur de risque, le marché, alors que la taille ou la valeur expliquent aussi une partie des rentabilités observées (Fama et French, 1993) ; des investisseurs supposés tous diversifiés, alors que la famille détient 62 % du capital et n'est pas diversifiée ; un marché supposé liquide et efficient ; un portefeuille de marché qui n'est pas observable et que l'on remplace par un indice ; une prime de risque et un taux sans risque qui sont des estimations.

**Réponses tolérées** : rentabilités et variances en fraction (0,09 ; 0,0100 ; 0,0080) ; variance et covariance calculées sur n − 1 si le candidat le signale (120 %² et 96 %², même bêta de 0,80, car le diviseur est le même) ; formule équivalente de la covariance par la moyenne des produits moins le produit des moyennes ; rentabilité exigée notée en cohérence avec un bêta erroné.

**Erreurs fréquentes**
- Diviser la covariance par la variance de l'action au lieu de celle de l'indice (0,0080 / 0,0153 = 0,52).
- Écrire la rentabilité exigée comme taux sans risque + bêta × rentabilité du marché, ou additionner la prime sans la multiplier par le bêta.
- Ajouter une prime de taille ou d'illiquidité au MEDAF, ce que l'énoncé exclut.
- Appeler la rentabilité de 8,00 % un CMPC : c'est le coût des fonds propres.
- `JUR-T14` — rôle de la diversification dans le MEDAF ignoré.

**Références** : F02 § 1 (convention de variance et de covariance écrite dans l'énoncé) et § 2 (MEDAF, bêta = covariance / variance, limites, instabilité du bêta) [V corrigé 2023 ; guide p. 74-75 ; S] ; F10 Sharpe (1964), Fama et French (1993) [V programme 5.2] ; programme 5.2.b « indicateurs de risque : variance, écart-type, bêta (covariance / variance du marché) » [V programme l. 584-586] ; F11 pour le taux sans risque et la prime de marché, posés comme hypothèses d'énoncé.

---

### 2.3 Gordon-Shapiro, rentabilité espérée au cours, PER des comparables, comparaison au cours et à la fourchette (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Valeur de Gordon-Shapiro : 0,42 / (8,00 % − 5,00 %) = **14,00 €** | 0,5 |
| 2.3-02 | Rentabilité espérée au cours : 0,42 / 16,20 + 5,00 % = 2,59 % + 5,00 % = **7,59 %**, inférieure aux 8,00 % exigés | 0,5 |
| 2.3-03 | PER : 20,0 × 10,80 = **216,00 M€** ; **18,00 €** par action | 0,5 |
| 2.3-04 | Comparaison au cours et à la fourchette ; sensibilité du modèle ; ce que mesure l'écart de PER ; conclusion sur le prix | 1 |

**Calculs.**
- **Gordon-Shapiro** : 0,42 / (0,08 − 0,05) = 0,42 / 0,03 = **14,00 €**.
- **Rentabilité espérée au cours** : rendement du prochain dividende 0,42 / 16,20 = 2,59 % ; rentabilité espérée 2,59 % + 5,00 % = **7,59 %**. Autre lecture : pour justifier le cours avec une rentabilité exigée de 8,00 %, il faudrait une croissance à l'infini de 8,00 % − 2,59 % = 5,41 %.
- **PER des comparables** : valeur des capitaux propres 20,0 × 10,80 = **216,00 M€** ; par action 216,00 / 12 000 000 = **18,00 €** (20,0 × BPA de 2026 de 0,90 €). Le PER s'applique au résultat net, un agrégat après frais financiers : il donne directement une valeur des capitaux propres, sans passer par la dette.

**Comparaison (1 pt).**

| Valeur par action | € | Écart au cours de 16,20 € |
|---|---:|---:|
| Gordon-Shapiro | 14,00 | − 13,58 % |
| Fourchette de l'offre | 14,50 à 15,50 | − 10,49 % à − 4,32 % |
| Prix central de l'offre | 15,00 | − 7,41 % |
| Cours du 30 avril 2027 (PER de 18,0) | 16,20 | — |
| PER des comparables du marché réglementé (20,0) | 18,00 | + 11,11 % |

- **Gordon-Shapiro** donne une valeur inférieure au cours et à la fourchette. Le modèle est très sensible à l'écart entre la rentabilité exigée et la croissance, ici de 3 points seulement : avec une croissance de 4,00 %, la valeur tombe à 10,50 € ; avec 6,00 %, elle monte à 21,00 € ; avec une rentabilité exigée de 9,00 % (bêta de 1,00), elle est de 10,50 €. Une croissance de 5,00 % à l'infini est déjà élevée pour une société mature, au-dessus de la croissance probable de l'économie à long terme. Le modèle suppose aussi un taux de distribution stable, alors que BRÉVOLAN distribue peu (0,30 € pour un BPA de 0,90 € en 2026) pour financer sa croissance : la valeur ne vient pas seulement des dividendes prévus.
- **Le cours** laisse espérer 7,59 %, un peu moins que les 8,00 % exigés : au cours actuel, l'action n'est pas bon marché selon les prévisions de l'analyste, ce qui justifie que de nouveaux investisseurs demandent un prix inférieur.
- **Le PER des comparables** donne 18,00 €. L'écart entre le PER de BRÉVOLAN (18,0) et celui des comparables (20,0) mesure en partie la décote de liquidité et de visibilité d'une action d'Euronext Growth. Si le transfert ramenait le PER à 20, la capitalisation gagnerait (20 − 18) × 10,80 = 21,60 M€, montant à comparer aux coûts de la question 2.1. Mais un PER unique, fourni sans échantillon, ne dit pas si les comparables ont la même croissance, le même risque et la même exposition au dollar.
- **Ce qu'en tirer pour le prix** : la fourchette (14,50 € à 15,50 €) se situe entre la valeur de Gordon-Shapiro et le cours, au-dessous de la valeur par le PER. Elle est défendable pour des investisseurs qui ne connaissent pas la société : le prix central de 15,00 € reste supérieur à la valeur la plus prudente et inférieur au cours. Aucune méthode ne justifie un prix au-dessus du cours avant que la liquidité et la visibilité nouvelles ne soient acquises.

**Réponses tolérées** : rentabilité espérée calculée à partir d'un dividende de 0,42 € pris comme dernier dividende versé, s'il est signalé ; PER appliqué au résultat prévu pour 2027 (20,0 × 1,00 = 20,00 €) si le candidat signale que le PER des comparables est calculé sur 2026 et qu'il le corrige ; comparaison ordonnée sans tableau, si elle est complète.

**Erreurs fréquentes**
- Faire croître une fois le dividende de 0,42 € (0,441) alors que l'énoncé donne le prochain dividende.
- Utiliser une rentabilité exigée inférieure à la croissance, ou un taux qui n'est pas celui des actionnaires.
- Retrancher la dette financière nette d'une valeur obtenue par le PER : le résultat net est déjà un agrégat des actionnaires.
- Retenir une seule valeur sans discuter la sensibilité de Gordon-Shapiro (`JUR-E03`).

**Références** : F02 § 6 (Gordon-Shapiro, valeur et rentabilité implicite, prochain dividende ou dernier dividende, sensibilité à l'écart entre k et g) [V programme 5.2 ; guide p. 75 ; S] ; F03 § 3 (multiples, PER inducteur de VCP) et § 8 (fourchette) [V guide p. 65 ; S] ; programme 3.2.a « inducteurs de VCP : RN » [V programme l. 524-525].

---

### 2.4 Décote, asymétrie d'information et signal de la cession du holding (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Décotes : prix central **7,41 %**, borne basse **10,49 %**, borne haute **4,32 %** ; coût de la décote du prix central pour les actionnaires actuels : (16,20 − 15,00) × 2 000 000 = **2,40 M€** | 0,5 |
| 2.4-02 | Décote et asymétrie d'information (Akerlof, 1970) appliquées à la famille et aux nouveaux investisseurs | 0,5 |
| 2.4-03 | Signal de la cession du holding pendant l'offre (financement hiérarchique, Myers et Majluf, 1984) et moyens de le limiter | 0,5 |

**Calculs.**
- Décote du prix central : 1 − 15,00 / 16,20 = **7,41 %** ; borne basse : 1 − 14,50 / 16,20 = **10,49 %** ; borne haute : 1 − 15,50 / 16,20 = **4,32 %**.
- Coût de la décote pour les actionnaires actuels : 30 000 000 / 15,00 = 2 000 000 actions nouvelles (question 2.5), d'où (16,20 − 15,00) × 2 000 000 = **2,40 M€** ; il est supporté à 62 % par la famille (1,49 M€), qui cède aussi ses propres actions 1,20 € au-dessous du cours. Ce coût s'ajoute aux 1,50 M€ de coût direct.

**Décote et asymétrie d'information (0,5 pt).** La famille dirige BRÉVOLAN depuis 1972 et connaît son carnet de commandes, ses marges et ses risques mieux que des investisseurs qui découvrent la société. Au sens d'Akerlof (1970), l'acheteur moins informé ne sait pas distinguer une bonne société d'une société qui cherche à vendre ses actions trop cher : il se protège en offrant un prix moyen, inférieur à la valeur des bonnes sociétés. Sans décote, les investisseurs prudents s'abstiendraient et l'offre risquerait de ne pas trouver preneur (sélection adverse). La décote de 7,41 % rémunère ce manque d'information et le faible volume des échanges actuels ; elle réduit le risque d'échec de l'offre. Les moyens de la réduire sont de réduire l'écart d'information : documents d'information de l'offre, présentation aux investisseurs, réputation de la banque conseil, suivi de six analystes.

**Signal de la cession du holding (0,5 pt).**
- Une émission d'actions est souvent lue comme le signe que les dirigeants jugent l'action chère : c'est le financement hiérarchique de Myers et Majluf (1984), où l'entreprise préfère l'autofinancement, puis la dette, et n'émet des actions qu'en dernier. Quand l'actionnaire le mieux informé vend en même temps une partie de ses actions, le signal est plus défavorable : les investisseurs se demandent pourquoi la famille vend si elle croit à la croissance qu'elle annonce.
- Le signal est atténué si la cession est **limitée** (400 000 actions, 5,38 % des actions du holding, contre 600 000), **expliquée** (besoin de liquidité de deux branches qui ne travaillent pas dans le groupe, et non doute sur l'avenir) et **encadrée** par l'engagement de ne rien céder d'autre pendant douze mois. La famille garde la majorité et l'essentiel de son patrimoine dans BRÉVOLAN : ses intérêts restent alignés sur ceux des nouveaux actionnaires.

**Réponses tolérées** : décote calculée sur le prix (1,20 / 15,00 = 8,00 %) si la base est indiquée ; coût de la décote rapporté à la capitalisation (1,23 %) ; transfert de valeur vers les nouveaux actionnaires de 2,06 M€, s'il est justifié (valeur après émission (194,40 + 30,00) / 14 000 000 = 16,03 €, puis (16,03 − 15,00) × 2 000 000) ; nombre d'actions nouvelles calculé dans l'une ou l'autre des questions 2.4 et 2.5 ; théorie du signal présentée avec Spence (1973) ou Ross (1977), si elle est appliquée correctement à la cession du holding.

**Erreurs fréquentes**
- Confondre sélection adverse (avant l'achat) et aléa moral (après le contrat).
- Calculer un droit préférentiel de souscription : l'offre est faite sans droit préférentiel.
- Analyser une réaction du cours à l'annonce, que l'énoncé ne fournit pas.
- `JUR-M01` — décote expliquée sans théorie de l'asymétrie d'information ni du signal.

**Références** : F10 Akerlof (1970) et Myers et Majluf (1984) [V programme 5.1 et 7.2] ; F06 § 2 (application aux introductions : décote, signal d'une émission d'actions) [V guide p. 73 ; S] ; F05 § 6 (décote d'introduction, engagements de conservation) [V guide p. 70-71 ; S].

---

### 2.5 Actions nouvelles, produit net, capital et voix, dilution, majorité, BPA (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Actions nouvelles : **2 000 000** à 15,00 €, **2 068 965** à 14,50 €, **1 935 483** à 15,50 € ; produit net au prix central 30,00 − 1,50 = **28,50 M€** | 0,5 |
| 2.5-02 | Répartition du capital et des voix sur 14 000 000 actions : holding **50,29 %** (400 000 cédées) ou **48,86 %** (600 000 cédées) ; salariés 2,57 % ; public 47,14 % ou 48,57 % | 1 |
| 2.5-03 | Dilution d'un actionnaire qui ne participe pas : **14,29 %** (1 % devient 0,86 % ; salariés 3 % → 2,57 %) | 0,5 |
| 2.5-04 | Nombre maximal d'actions cédées en gardant plus de la moitié des voix : **439 999** | 0,5 |
| 2.5-05 | BPA 2027 **1,00 €** sans l'opération et **0,86 €** avec ; résultat supplémentaire **2,00 M€**, soit **7,02 %** du produit net, à comparer aux 8,00 % exigés | 1 |

**Actions nouvelles et produit net.**
- Au prix central : 30 000 000 / 15,00 = **2 000 000** actions. À 14,50 € : 30 000 000 / 14,50 = 2 068 965,5, arrondi à l'unité inférieure **2 068 965** ; à 15,50 € : 1 935 483,9, soit **1 935 483**. Plus le prix est bas, plus il faut émettre d'actions pour lever le même montant, et plus la dilution est forte.
- Produit net pour BRÉVOLAN au prix central : 30,00 − 0,90 − 0,60 = **28,50 M€**. Le produit de la cession (400 000 × 15,00 = 6,00 M€, 5,82 M€ après commissions) revient au holding.

**Répartition du capital et des voix au prix central (une action = une voix ; 12 000 000 + 2 000 000 = 14 000 000 actions).**

| Actionnaire | Avant | Après, 400 000 actions cédées | | Après, 600 000 actions cédées | |
|---|---:|---:|---:|---:|---:|
| | % | actions | % | actions | % |
| BRÉVOLAN Participations | 62,00 | 7 040 000 | **50,29** | 6 840 000 | **48,86** |
| Salariés | 3,00 | 360 000 | 2,57 | 360 000 | 2,57 |
| Public (anciens et nouveaux actionnaires) | 35,00 | 6 600 000 | 47,14 | 6 800 000 | 48,57 |
| **Total** | **100** | **14 000 000** | **100** | **14 000 000** | **100** |

Dans le public, les acquéreurs des actions nouvelles détiennent 2 000 000 / 14 000 000 = 14,29 % du capital ; les acquéreurs des actions cédées 2,86 % ou 4,29 % ; les anciens actionnaires du public, 30,00 %. Avec 400 000 actions cédées, la famille garde la majorité des voix ; avec 600 000, elle la perd et ne détient plus que 48,86 % : elle reste le premier actionnaire, mais ne décide plus seule en assemblée. Avec 400 000 actions cédées, le flottant (47,14 %) est proche de la moitié du capital souhaitée par la banque ; sa valeur passe de 68,04 M€ (4 200 000 × 16,20) à 99,00 M€ au prix de l'offre.

**Dilution d'un actionnaire qui ne participe pas.** Sa part est multipliée par 12 000 000 / 14 000 000 : elle baisse de 2 000 000 / 14 000 000 = **14,29 %**. Un actionnaire qui détenait 1 % n'en détient plus que **0,86 %** (0,8571 %) ; les salariés passent de 3,00 % à 2,57 %. Sans cession, le holding lui-même passerait de 62,00 % à 53,14 %.

**Nombre maximal d'actions cédées.** Plus de la moitié des 14 000 000 voix, c'est au moins 7 000 001 voix. Le holding peut céder au plus 7 440 000 − 7 000 001 = **439 999** actions. À 440 000 actions, il détiendrait exactement 50,00 %, ce qui n'est pas plus de la moitié. Cette limite suppose que les 2 000 000 actions nouvelles soient toutes émises au prix central : à 14,50 €, l'émission de 2 068 965 actions la ramènerait à 405 517 actions ; à 15,50 €, elle la porterait à 472 258.

**BPA de 2027 et résultat supplémentaire.**
- Sans l'opération : 12,00 / 12 000 000 = **1,00 €**. Avec l'opération (actions au 31 décembre 2027, fonds sans résultat en 2027) : 12,00 / 14 000 000 = **0,86 €**, soit une baisse de 14,29 % (14,00 % sur les BPA arrondis).
- Pour que le BPA revienne à 1,00 € avec 14 000 000 actions, il faut un résultat de 14,00 M€, soit un résultat net supplémentaire de 1,00 × 2 000 000 = **2,00 M€** par an, après impôt. Rapporté au produit net : 2,00 / 28,50 = **7,02 %** (6,67 % du montant brut, soit l'inverse du PER de 15 au prix de l'offre ; soit 2,00 / 0,75 = 2,67 M€ et 9,37 % avant impôt). Ce calcul ne tient pas compte du coût annuel d'information (convention de l'annexe 2.6).
- **Commentaire** : la baisse du BPA de 2027 est mécanique, puisque les fonds arrivent en octobre et que l'extension de Nevers et VISTRAMÉO ne produiront de résultat qu'après. Le BPA n'est pas le bon critère : il suffit que les fonds rapportent 7,02 % après impôt pour le rétablir, alors que les actionnaires exigent 8,00 % (question 2.2). Un emploi des fonds qui rétablit le BPA sans atteindre 8,00 % détruit de la valeur. Le coût d'information de 0,30 M€ par an après impôt, dû au transfert, relève encore ce que les fonds doivent rapporter : il faudrait 2,30 M€, soit 8,07 % du produit net, pour rétablir le BPA en le comptant. L'opération crée de la valeur si l'extension et la participation rapportent au moins la rentabilité exigée.

**Réponses tolérées** : nombre d'actions aux bornes arrondi au plus proche si le candidat le signale (2 068 966 à 14,50 €) ; répartition présentée en deux tableaux ou dans le texte ; BPA calculé sur un nombre moyen d'actions pondéré sur l'année (12 416 667 actions en comptant les actions nouvelles pour deux mois et demi, BPA de 0,97 €) si le candidat écarte la convention de l'énoncé en le disant ; résultat supplémentaire exprimé avant impôt (2,67 M€) s'il est signalé ; résultat supplémentaire de 2,30 M€ (8,07 % du produit net) si le candidat ajoute le coût annuel de 0,30 M€ après impôt en le signalant : il conclut alors que les fonds doivent rapporter plus que la rentabilité exigée.

**Erreurs fréquentes**
- Compter les actions cédées par le holding comme des actions nouvelles (14 400 000 actions) : la cession ne change pas le nombre d'actions.
- Calculer la part du holding sur 12 000 000 actions après l'émission.
- Retenir 440 000 actions, qui donnent exactement la moitié des voix, ou oublier l'effet de l'émission sur le dénominateur (1 440 000 − 1 = 1 439 999 sur 12 000 000 actions).
- Calculer les actions nouvelles sur le produit net au lieu du montant brut.
- `JUR-I03` — nouvelle structure d'actionnariat calculée sans en tirer les conséquences sur le contrôle.
- `JUR-T07` — répartition du capital non présentée en tableau.

**Références** : F05 § 4 (dilution du contrôle sans souscription : part × N / (N + n) ; dilution du BPA) et § 3 (BPA, relution si le rendement des fonds dépasse l'inverse du PER) [V guide p. 68-69 ; S] ; F05 § 6 (titres nouveaux et cession de titres existants) [V guide p. 70-71] ; programme 4.2.a « objectifs : structure financière, indicateurs par action (BPA), gestion de la dilution » [V guide p. 68] ; programme 4.2.e « données de l'opération : prix, nombre de titres, structure de l'actionnariat avant et après » [S sujet 2024].

---

### 2.6 Méthode du capital-risque, cycle de vie, participation minoritaire ou rachat (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Valeur de sortie 15 × 2,95 = **44,25 M€** ; facteur 1,25⁵ = 3,05176 ; post-money **14,50 M€** ; pre-money **10,15 M€** | 0,5 |
| 2.6-02 | Part à obtenir **30,00 %** ; prix **29,00 €** par action ; **150 000** actions nouvelles (500 000 actions après) | 0,5 |
| 2.6-03 | Proposition des fondateurs (25 %) : participation à la sortie 11,06 M€, **TRI 20,52 %** < 25 % ; pre-money implicite 13,05 M€ | 0,5 |
| 2.6-04 | Pourquoi l'actif net et les flux actualisés se prêtent mal à VISTRAMÉO (cycle de vie) | 1 |
| 2.6-05 | Rachat écarté : sortie **27,00 M€**, valeur actuelle **8,85 M€** contre 16,00 M€ demandés, **TRI 11,03 %** | 0,5 |
| 2.6-06 | Participation minoritaire plutôt que rachat : risque, montant engagé, fondateurs, clients, contrôle et suite | 1 |

**Méthode du capital-risque.**
- Valeur de sortie : 15 × 2,95 = **44,25 M€**.
- Valeur post-money : 44,25 / 1,25⁵ = 44,25 / 3,05176 = **14,50 M€**.
- Valeur pre-money : 14,50 − 4,35 = **10,15 M€**.
- Part à obtenir : 4,35 / 14,50 = **30,00 %**.
- Prix par action : 10,15 M€ / 350 000 = **29,00 €** ; actions nouvelles 4 350 000 / 29,00 = **150 000** ; 500 000 actions après l'apport, dont 150 000 pour BRÉVOLAN (30,00 %), 245 000 pour les fondateurs (49,00 %) et 105 000 pour les investisseurs particuliers (21,00 %).
- Vérification : participation à la sortie 30,00 % × 44,25 = 13,28 M€, soit 3,05 fois la mise : le TRI exigé de 25 % est atteint, à l'arrondi près, si le plan se réalise.

**Proposition des fondateurs.** Pour 25 % du capital, la participation vaudrait 25 % × 44,25 = 11,06 M€ à la sortie : TRI = (11,06 / 4,35)^(1/5) − 1 = **20,52 %**, inférieur aux 25 % exigés. La proposition revient à une post-money de 4,35 / 25 % = 17,40 M€ et une pre-money de 13,05 M€ (contre 10,15 M€). BRÉVOLAN doit demander 30 % pour le même apport, ou n'apporter que 25 % × 14,50 = 3,63 M€ pour 25 %.

**Cycle de vie (1 pt).**
- **Actif net** : les capitaux propres de VISTRAMÉO (0,90 M€, surtout de la trésorerie et des logiciels développés en interne) ne mesurent pas sa valeur : la pre-money en vaut plus de onze fois (10,15 / 0,90 = 11,28). Ce qui a de la valeur (compétences des ingénieurs, algorithmes, clients en cours de conquête) figure peu ou pas au bilan ; une approche patrimoniale convient à une société dont la valeur tient à ses actifs, ou en déclin, pas à une société en création.
- **Flux actualisés** : VISTRAMÉO perd de l'argent (perte de 0,60 M€ en 2026 pour 1,10 M€ de chiffre d'affaires) ; ses flux des premières années seront négatifs, et presque toute la valeur viendrait d'une valeur terminale fondée sur un plan des fondateurs très incertain. Le taux à retenir pour une telle société, sans historique ni bêta mesurable, serait lui-même difficile à fixer.
- **Méthode du capital-risque** : elle part de la valeur de sortie, le seul point du plan qui intéresse l'investisseur, et l'actualise à un TRI élevé (25 %) qui intègre le risque d'échec et le fait que le plan des fondateurs est optimiste. Elle reste fragile : la valeur dépend du résultat dans cinq ans et du multiple de sortie. Avec un résultat de 2,00 M€ au lieu de 2,95 M€, la sortie ne vaudrait que 30,00 M€ (illustration).

**Rachat écarté.**
- Valeur de sortie avec le plan revu par M. BRÉVOLAN : 15 × 1,80 = **27,00 M€** ; valeur actuelle de 100 % du capital : 27,00 / 3,05176 = **8,85 M€**, contre 16,00 M€ demandés, soit 7,15 M€ de trop.
- TRI au prix demandé : (27,00 / 16,00)^(1/5) − 1 = **11,03 %**, très loin des 25 % exigés. Même si le plan des fondateurs se réalisait, 100 % du capital vaudrait 44,25 / 3,05176 = 14,50 M€, moins que 16,00 M€ (TRI de 22,56 %).

**Participation minoritaire plutôt que rachat (1 pt).**
- **Montant engagé et risque** : 4,35 M€ au lieu de 16,00 M€, pour une société jeune et déficitaire : BRÉVOLAN limite sa perte en cas d'échec.
- **Ce que le rachat détruirait** : les fondateurs partiraient, alors qu'ils portent le savoir-faire, et les trois concurrents de BRÉVOLAN cesseraient d'acheter à une société contrôlée par un concurrent. Le résultat dans cinq ans tomberait de 2,95 à 1,80 M€. Avec 30 %, les fondateurs gardent 49 % du capital et restent motivés, et VISTRAMÉO garde ses clients.
- **Ce que la participation apporte à BRÉVOLAN** : un accès à une technologie de contrôle qualité qu'elle peut intégrer à ses lignes (argument commercial auprès des laboratoires, vigilants sur la qualité), un siège au conseil pour suivre la société, la possibilité de monter au capital plus tard si le plan se confirme, et une participation valorisée si la société est cédée.
- **Limites** : sans contrôle, BRÉVOLAN ne décide pas de la stratégie ni de la date de sortie ; ses concurrents profiteront aussi de la technologie ; la participation sera financée par l'offre, et son rendement doit atteindre la rentabilité exigée par les actionnaires de BRÉVOLAN (question 2.5).
- **Conclusion** : la participation de 30 % pour 4,35 M€, au prix de 29,00 € par action, est cohérente avec le TRI exigé ; la proposition des fondateurs (25 %) doit être renégociée, et le rachat de 100 % à 16,00 M€ a eu raison d'être écarté.

**Réponses tolérées** : facteur 1,25⁵ arrondi à 3,0518 ou non arrondi (post-money 14,50) ; TRI de la proposition des fondateurs mesuré par le multiple de la mise (2,54 contre 3,05 exigé) ; part à obtenir de 30 % énoncée comme une condition de la négociation.

**Erreurs fréquentes**
- Calculer la part à obtenir sur la pre-money (4,35 / 10,15 = 42,86 %).
- Diviser la post-money, au lieu de la pre-money, par le nombre d'actions existantes pour obtenir le prix.
- Actualiser la valeur de sortie au taux de 8,00 % de l'action BRÉVOLAN, qui ne correspond pas au risque d'une jeune société.
- Évaluer VISTRAMÉO par son actif net ou par un autre procédé d'évaluation des jeunes sociétés que la méthode du capital-risque.
- `JUR-T13` — choix de la participation minoritaire discuté sans les données du cas (fondateurs, concurrents clients).

**Références** : F03 § 7 (méthode du capital-risque : post-money, pre-money, part de l'investisseur) et § 8 (méthode adaptée au cycle de vie : création, croissance, maturité, déclin) [V guide p. 67 ; S] ; programme 3.3.c « méthode de la venture capital : valeur de sortie actualisée au TRI cible, post-money, pre-money, part du fonds » [V guide p. 67] ; programme 4.2.b « motifs économiques et financiers : synergies, croissance externe, création de valeur » [V guide p. 69].

---

### 2.7 Recommandation : prix, quantité cédée, conditions de réussite (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Prix recommandé et quantité cédée par le holding, justifiés par les résultats | 0,5 |
| 2.7-02 | Conditions de réussite reliées au cas | 0,5 |

**Recommandation (0,5 pt).**
- **Prix** : le prix central de **15,00 €** (décote de 7,41 %) est défendable : il est supérieur à la valeur la plus prudente (Gordon-Shapiro, 14,00 €) et inférieur au cours et à la valeur par le PER des comparables (18,00 €). La borne basse (14,50 €) coûterait davantage aux actionnaires actuels et réduirait la quantité que le holding peut céder (405 517 actions au plus). Un prix plus proche de 15,50 € n'est envisageable que si la demande des investisseurs est forte.
- **Quantité cédée** : **400 000 actions** au plus, sous la limite de 439 999 : la famille garde 50,29 % des voix, le flottant atteint 47,14 % du capital et le signal négatif de la cession reste limité. La proposition de la banque (600 000 actions) ferait perdre la majorité (48,86 %), ce que la famille refuse.

**Conditions de réussite (0,5 pt).**
- Une communication claire sur l'emploi des fonds (extension de Nevers, VISTRAMÉO) et sur leur rentabilité attendue, au moins égale à la rentabilité exigée de 8,00 %, pour compenser la baisse du BPA de 2027.
- Un engagement de conservation du holding de douze mois, et des raisons de la cession expliquées aux investisseurs.
- Une liquidité effective après l'offre (volumes proches des 24 000 actions par séance attendues, entrée dans les indices, suivi des analystes), sans quoi la décote de PER ne se réduira pas et le coût annuel de 0,30 M€ ne sera pas compensé.
- Un marché favorable à l'automne 2027, et une marge de contrôle à surveiller : avec 50,29 % des voix, la famille ne pourra presque plus céder d'actions (39 999 au plus) ni laisser émettre de nouvelles actions sans y souscrire, sauf à perdre la majorité.

**Réponses tolérées** : recommandation d'un prix à la borne basse ou d'une cession inférieure à 400 000 actions, si elle est justifiée par les résultats du candidat et par la majorité des voix.

**Erreurs fréquentes**
- Recommander la cession de 600 000 actions sans constater la perte de la majorité.
- Conclure sans chiffre, ou par une recommandation qui contredit les calculs (`JUR-T01`).

**Références** : F05 § 6 (fixation du prix, engagements de conservation) [V guide p. 70-71 ; S] ; F03 § 8 (chaque calcul débouche sur une conclusion opérationnelle) [V guide] ; programme 4.2.e « mécanismes d'une IPO : ouverture du capital, titres nouveaux et/ou cession de titres existants, fixation du prix » [V guide p. 71].
