# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 16 — Dossier 1 (18 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F05 ingénierie financière, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (flux de trésorerie disponibles, CMPC, DCF, parité, augmentation de capital, répartition du capital, barème, liste noire, hors-programme ; part de la métropole et valeur créée vérifiées par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une parité calculée avec une valeur de Valcroze Biométhane erronée à la question 1.3, ou avec la valeur de secours de 70,00 € prévue par l'annexe 1.3).

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Motifs et limites du regroupement | `4.2.b` Analyser les motifs des opérations de réorganisation | 2 |
| 1.2 Flux de trésorerie disponibles de Valcroze Biométhane | `3.1.b` Construire un business plan | 3 |
| 1.3 CMPC, VGE, VCP et valeur par action | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance ; `3.1.d` Distinguer la valeur globale de l'entreprise (VGE) de la valeur des capitaux propres (VCP) | 4 |
| 1.4 Parité d'échange et capital de l'entité fusionnée | `4.2.c` Analyser les opérations de fusions et d'acquisitions | 3 |
| 1.5 Augmentation de capital réservée et dilution | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital | 3 |
| 1.6 Synthèse et recommandation | `4.2.a` ; `4.2.b` ; `4.2.c` | 3 |
| **Total** | | **18** |

Part du calcul : environ 12 points (1.2-01 à 1.2-03, 1.3-01 à 1.3-04, 1.4-01 à 1.4-03, 1.5-01 à 1.5-04, 1.6-01 pour moitié). Part de l'analyse : environ 6 points. Les questions 1.1 et 1.6, rédactionnelles, valent ensemble 5 points : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 1.1 Motifs et limites du regroupement (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Motifs liés au cas : chaîne « boues → énergie » intégrée, synergies de mutualisation, fin des conventions entre les deux sociétés, gouvernance simplifiée avec OSTRALE Infrastructures et déblocage du second méthaniseur | 1 |
| 1.1-02 | Limites : mélange d'une activité de service public au prix encadré et d'une activité exposée au prix du gaz, valorisation contestable, synergies incertaines, dilution du fonds et coûts de l'opération | 1 |

**Motifs (1 pt).** Une fusion regroupe deux patrimoines dans une seule société ; elle se justifie par la création de valeur qu'elle permet (guide, p. 69 : synergies opérationnelles ou financières, organisation du groupe).
- **Intégrer la chaîne de valeur « boues → énergie »** : les boues de la station Sud sont la matière première du méthaniseur, sur le même terrain. Une seule société gère le flux de bout en bout : la station n'a plus de « client » interne, le méthaniseur plus de « fournisseur » interne.
- **Synergies de coûts** : les deux sociétés ont chacune une équipe d'exploitation, une astreinte, des contrats de maintenance et un laboratoire ; la mutualisation et la réutilisation de la chaleur du méthaniseur pour sécher les boues ont une valeur actuelle estimée à 5,40 M€ (annexe 1.3), soit 15 % de la valeur de Valcroze Biométhane (5,40 / 36,00, question 1.3).
- **Fin des conventions entre les deux sociétés** : quatre conventions (boues, terrain, chaleur, réseaux) renégociées chaque année et justifiées devant le fonds. Aujourd'hui, chaque euro facturé par Épuration Sud à Valcroze Biométhane profite à 100 % à ONDÉRIS mais réduit un résultat dont 30 % revient à OSTRALE : ce conflit entre actionnaire majoritaire et minoritaire prolonge la théorie de l'agence (Jensen et Meckling, 1976), formulée pour la relation entre actionnaires et dirigeants : les conventions justifiées chaque année devant le fonds sont des coûts de surveillance. La fusion le supprime.
- **Gouvernance et financement** : OSTRALE détient un droit d'accord sur tout investissement de plus de 5 M€ et a refusé le second méthaniseur (25,20 M€). Après la fusion, le fonds ne détient plus que 10 % d'une entité plus grande (question 1.4) ; le groupe retrouve la maîtrise de ses investissements et peut ouvrir le capital à un partenaire choisi (TRÉVANNE Énergies).
- **Structure financière** : l'entité fusionnée réunit une activité stable (épuration, recettes fixées par la métropole) et une activité de croissance très endettée (26,30 M€ de dette nette pour 12,00 M€ de chiffre d'affaires) : sa capacité d'endettement globale est meilleure que celle de Valcroze Biométhane seule.

**Limites (1 pt).**
- **Deux activités de risques différents** : le prix de l'assainissement doit couvrir les seuls coûts du service, alors que les recettes du biométhane dépendront après 2034 du prix de marché du gaz. Les usagers ne doivent pas supporter les pertes éventuelles de l'activité énergétique : d'où la double comptabilité analytique prévue (annexe 1.1). Le risque de l'entité fusionnée n'est plus celui d'une station d'épuration.
- **Valorisation et équité** : la parité repose sur une valeur par les flux sensible aux hypothèses (question 1.3) et sur une valeur d'expertise d'Épuration Sud ; le fonds peut la contester.
- **Synergies incertaines** et coûts d'intégration (organisation des équipes, systèmes) : les 5,40 M€ sont une estimation.
- **Pour OSTRALE** : sa participation est diluée (10 % au lieu de 30 %), son droit d'accord disparaît, sa sortie prévue vers 2031 porte sur une entité où il est très minoritaire ; il faudra obtenir son accord sur la parité.
- **Signal** : le regroupement peut être lu comme un transfert de risques de l'activité énergétique vers le service public.

**Réponses tolérées** : présentation en tableau motifs / limites ; mention de l'effet de taille pour négocier avec les banques ; pour chaque item, trois arguments liés au cas suffisent pour la totalité des points.

**Erreurs fréquentes**
- Développer le régime juridique ou fiscal de la fusion (droit des sociétés, procédure, imposition) : hors du champ de l'épreuve.
- Développer le statut des sociétés d'économie mixte ou les règles de la délégation de service public au lieu de leurs conséquences financières (prix encadré, actionnaire public).
- `JUR-T13` — liste générale de motifs de fusion sans les données du cas (même site, quatre conventions, refus du fonds, 5,40 M€ de synergies de l'annexe 1.3).
- `JUR-T14` — absence de référence à la théorie de l'agence pour le conflit entre ONDÉRIS et OSTRALE.

---

### 1.2 Flux de trésorerie disponibles de Valcroze Biométhane (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | Résultat d'exploitation (4,56 ; 4,80 ; 4,84 ; 5,08 ; 5,32) et impôt de 25 % calculé sur ce résultat (1,14 ; 1,20 ; 1,21 ; 1,27 ; 1,33), sans les charges financières | 1 |
| 1.2-02 | Variation du BFR : 0,04 M€ par an (BFR de 1,24 ; 1,28 ; 1,32 ; 1,36 ; 1,40 contre 1,20 fin 2026) | 0,5 |
| 1.2-03 | Flux de trésorerie disponibles : 4,18 ; 4,16 ; 2,79 ; 4,37 ; 3,95 M€ | 1 |
| 1.2-04 | Commentaire : creux de 2029 dû au renouvellement de l'unité d'épuration, flux de 2031 normatif, charges financières exclues | 0,5 |

**Conventions rappelées** (annexe 1.5) : FTD = REX − IS sur le REX + dotations − variation du BFR − investissements ; IS 25 % ; M€ à deux décimales.

**Tableau des flux de trésorerie disponibles (M€)**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Chiffre d'affaires | 12,40 | 12,80 | 13,20 | 13,60 | 14,00 |
| − Charges d'exploitation décaissées | − 5,24 | − 5,40 | − 5,56 | − 5,72 | − 5,88 |
| = EBITDA | 7,16 | 7,40 | 7,64 | 7,88 | 8,12 |
| − Dotations aux amortissements | − 2,60 | − 2,60 | − 2,80 | − 2,80 | − 2,80 |
| = Résultat d'exploitation (REX) | 4,56 | 4,80 | 4,84 | 5,08 | 5,32 |
| − IS sur le REX (25 %) | − 1,14 | − 1,20 | − 1,21 | − 1,27 | − 1,33 |
| = REX après impôt | 3,42 | 3,60 | 3,63 | 3,81 | 3,99 |
| + Dotations aux amortissements | 2,60 | 2,60 | 2,80 | 2,80 | 2,80 |
| − Variation du BFR | − 0,04 | − 0,04 | − 0,04 | − 0,04 | − 0,04 |
| − Investissements de renouvellement | − 1,80 | − 2,00 | − 3,60 | − 2,20 | − 2,80 |
| **= Flux de trésorerie disponible** | **4,18** | **4,16** | **2,79** | **4,37** | **3,95** |

BFR (10 % du chiffre d'affaires) : 1,20 fin 2026, puis 1,24 ; 1,28 ; 1,32 ; 1,36 ; 1,40 : la variation est de 0,04 M€ chaque année (10 % × 0,40 M€ de chiffre d'affaires supplémentaire).

**Commentaire (0,5 pt).**
- Les flux sont **élevés et réguliers**, autour de 4 M€ par an : la marge d'EBITDA est stable, proche de 58 % (7,16 / 12,40 = 57,74 % ; 8,12 / 14,00 = 58,00 %), grâce au contrat de vente du gaz à prix indexé et à des boues fournies par la station voisine. Le BFR est faible.
- Le **creux de 2029** (2,79 M€) vient du remplacement de l'unité d'épuration du biogaz (3,60 M€) : un flux bas une année ne traduit pas une baisse de rentabilité.
- Le flux de 2031 (3,95 M€) est **normatif** : investissements égaux aux dotations (2,80 M€), ce qui justifie de l'utiliser pour la valeur terminale.
- Les **charges financières** (1,20 M€ à 0,80 M€) ne sont pas déduites : les FTD reviennent à tous les apporteurs de capitaux, dont les prêteurs, rémunérés par le CMPC (question 1.3).

**Réponses tolérées** : tableau partant de l'EBITDA (EBITDA − IS sur le REX − variation du BFR − investissements), qui donne les mêmes flux ; présentation par la capacité d'autofinancement d'exploitation (REX après impôt + dotations : 6,02 ; 6,20 ; 6,43 ; 6,61 ; 6,79) puis déduction de la variation du BFR et des investissements.

**Erreurs fréquentes**
- Déduire les charges financières et calculer l'impôt sur le résultat courant : flux de 3,28 ; 3,33 (ou 3,34) ; 2,04 ; 3,69 (ou 3,70) ; 3,35, qui mélangent flux des actionnaires et flux de l'entreprise.
- Retrancher le BFR au lieu de sa variation : flux de 2,98 ; 2,92 ; 1,51 ; 3,05 ; 2,59.
- Oublier de réintégrer les dotations, charges non décaissées.
- `JUR-E01` — flux de trésorerie disponibles mal connus (confusion avec la capacité d'autofinancement ou le résultat net).
- `JUR-T07` — flux présentés sans tableau.

---

### 1.3 CMPC, VGE, VCP et valeur par action (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | ke = 4 % + 1,20 × 5 % = 10,00 % ; kd après impôt = 3,75 % ; CMPC = 60 % × 10,00 % + 40 % × 3,75 % = 7,50 % | 1 |
| 1.3-02 | Flux actualisés : 3,89 ; 3,60 ; 2,25 ; 3,27 ; 2,75, soit 15,76 M€ ; valeur terminale 2031 = 3,95 × 1,015 / 0,06 = 66,82 M€, actualisée 46,54 M€ | 1,5 |
| 1.3-03 | VGE = 62,30 M€ ; VCP = 62,30 − 26,30 = 36,00 M€ ; valeur par action = 72,00 € | 1 |
| 1.3-04 | Poids de la valeur terminale : 74,70 % de la VGE (ou 74,71 %) ; commentaire (sensibilité à g et au CMPC, contrat de gaz jusqu'en 2034) | 0,5 |

**Conventions rappelées** (annexes 1.2 et 1.5) : MEDAF ; structure cible 60 % / 40 % ; IS 25 % ; flux en fin d'année ; Gordon-Shapiro avec g = 1,5 % ; VCP = VGE − dette financière nette (26,30 M€) ; coefficients non arrondis, montants à deux décimales.

**CMPC (1 pt).** Le taux d'actualisation des FTD est le coût moyen pondéré des ressources qui les financent.
- Coût des fonds propres (MEDAF, Sharpe, 1964) : ke = 4 % + 1,20 × 5 % = **10,00 %**. Le bêta est donné à la structure financière cible : il n'y a ni désendettement ni réendettement à faire.
- Coût de la dette après impôt : 5 % × (1 − 25 %) = **3,75 %**.
- CMPC = 60 % × 10,00 % + 40 % × 3,75 % = 6,00 % + 1,50 % = **7,50 %**.

**Flux actualisés et valeur terminale (1,5 pt).**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| FTD (M€) | 4,18 | 4,16 | 2,79 | 4,37 | 3,95 |
| Coefficient 1,075^−t | 0,9302 | 0,8653 | 0,8050 | 0,7488 | 0,6966 |
| FTD actualisé | 3,89 | 3,60 | 2,25 | 3,27 | 2,75 |

Somme des flux actualisés : **15,76 M€**.

Valeur terminale au 31/12/2031 (Gordon et Shapiro) : VT = FTD 2031 × (1 + g) / (CMPC − g) = 3,95 × 1,015 / (7,50 % − 1,50 %) = 4,0093 / 0,06 = **66,82 M€**, actualisée : 66,82 × 1,075^−5 = **46,54 M€**.

**VGE, VCP et valeur par action (1 pt).**
- VGE = 15,76 + 46,54 = **62,30 M€**.
- VCP = VGE − dette financière nette = 62,30 − 26,30 = **36,00 M€** : la VGE revient à tous les apporteurs de capitaux ; les actionnaires n'ont droit qu'à ce qui reste après les prêteurs.
- Valeur par action : 36 000 000 / 500 000 = **72,00 €**.

**Poids de la valeur terminale et commentaire (0,5 pt).**
- Poids : 46,54 / 62,30 = **74,70 %** de la VGE (74,71 % avec les valeurs non arrondies, accepté). Les trois quarts de la valeur viennent d'après 2031.
- **Sensibilité** (calculs facultatifs) : avec g = 1 % ou 2 %, la VCP passe à 32,21 ou 40,48 M€ ; avec un CMPC de 7 % ou 8 %, à 41,64 ou 31,23 M€. Un demi-point de taux fait varier la VCP de 10 % à 16 % : l'effet de levier de la dette (26,30 M€) amplifie les écarts de VGE sur la VCP.
- **Hypothèse forte** : le contrat de vente du gaz à prix indexé s'arrête en 2034 ; une croissance de 1,5 % à l'infini suppose que le biométhane se vendra au moins aussi bien ensuite, au prix du marché. Le méthaniseur, mis en service en 2019, devra aussi être renouvelé : un flux normatif où les investissements égalent les dotations est peut-être optimiste.
- La valeur est donc une estimation centrale à présenter avec une fourchette ; elle sert de base à la parité (question 1.4).

**Réponses tolérées** : écarts de 0,01 M€ dus à l'arrondi des coefficients d'actualisation (par exemple 46,55 M€ avec le coefficient arrondi 0,6966, VCP de 36,01 M€) ; valeur terminale actualisée en une seule étape (4,0093 / 0,06 / 1,075^5) ; VGE calculée sans arrondir les flux actualisés (62,30 M€).

**Erreurs fréquentes**
- Actualiser au coût des fonds propres (10 %) des flux qui reviennent à tous les apporteurs de capitaux.
- Oublier de multiplier le flux 2031 par (1 + g) : VT = 65,83 M€, VCP de 35,31 M€.
- Oublier d'actualiser la valeur terminale, ou l'actualiser sur six ans.
- Confondre VGE et VCP en prenant 62,30 M€ comme valeur des actions (124,60 € par action).
- `JUR-E01` — flux de l'entreprise actualisés avec un taux ou une dette incohérents (frais financiers déduits et dette retranchée une seconde fois).
- `JUR-T02` — absence de commentaire sur la fragilité de la valeur terminale.

---

### 1.4 Parité d'échange et capital de l'entité fusionnée (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Valeurs par action sans synergies : Épuration Sud (96,00 − 24,00) / 1 800 000 = 40,00 € ; Valcroze Biométhane 72,00 € ; parité = 72,00 / 40,00 = 1,80, soit 9 actions d'Épuration Sud pour 5 actions de Valcroze Biométhane | 1 |
| 1.4-02 | Actions à créer : 500 000 × 1,80 = 900 000 ; capital de l'entité fusionnée : 2 700 000 actions | 1 |
| 1.4-03 | Répartition : ONDÉRIS 1 800 000 + 70 % × 900 000 = 2 430 000 actions (90,00 %) ; OSTRALE 270 000 actions (10,00 %) ; valeur préservée : 270 000 × 40,00 = 10,80 M€ = 30 % × 36,00 M€ | 1 |

**Conventions rappelées** (annexe 1.3) : valeurs des capitaux propres par action au 31/12/2026, sans les synergies ; Valcroze Biométhane à la valeur par les flux arrondie à l'euro (72,00 €) ; toutes ses actions sont échangées.

**Parité (1 pt).**
- ONDÉRIS Épuration Sud : VCP = 96,00 − 24,00 = **72,00 M€**, soit 72 000 000 / 1 800 000 = **40,00 €** par action.
- Valcroze Biométhane : **72,00 €** par action (question 1.3).
- Parité = valeur d'une action de l'absorbée / valeur d'une action de l'absorbante = 72,00 / 40,00 = **1,80** : une action de Valcroze Biométhane vaut 1,8 action d'Épuration Sud, soit **9 actions nouvelles pour 5 actions** apportées.

**Actions à créer (1 pt).** L'absorbante ne détient aucune action de l'absorbée : toutes les actions de Valcroze Biométhane sont rémunérées, y compris celles d'ONDÉRIS.
- Actions à créer = 500 000 × 1,80 = **900 000** (aucun rompu : 500 000 est un multiple de 5).
- Nombre d'actions de l'entité fusionnée : 1 800 000 + 900 000 = **2 700 000**.

**Répartition du capital et valeur d'OSTRALE (1 pt).**

| Actionnaire | Actions d'Épuration Sud détenues | Actions reçues | Total | Part du capital |
|---|---:|---:|---:|---:|
| ONDÉRIS | 1 800 000 | 70 % × 900 000 = 630 000 | 2 430 000 | **90,00 %** |
| OSTRALE Infrastructures | — | 30 % × 900 000 = 270 000 | 270 000 | **10,00 %** |
| **Total** | 1 800 000 | 900 000 | 2 700 000 | 100,00 % |

Les anciens associés de Valcroze Biométhane reçoivent un tiers du capital (900 000 / 2 700 000), autant que le poids de leur société dans la valeur totale (36,00 / 108,00).

**Valeur préservée** : avant la fusion, OSTRALE détient 30 % × 36,00 = 10,80 M€ ; après, 270 000 × 40,00 € = **10,80 M€**. L'échange est neutre pour le fonds aux valeurs sans synergies : il ne transfère pas de valeur entre ONDÉRIS et OSTRALE. Avec les synergies, OSTRALE en reçoit 10 % (question 1.6).

**Réponses tolérées** : parité exprimée « 5 actions de Valcroze Biométhane contre 9 actions d'Épuration Sud » ; avec la valeur de secours de 70,00 € : parité 1,75, 875 000 actions à créer, 2 675 000 actions, ONDÉRIS 2 412 500 actions (90,19 %), OSTRALE 262 500 (9,81 %), notés en cohérence.

**Erreurs fréquentes**
- Inverser la parité (40,00 / 72,00 = 0,56) et créer 277 778 actions.
- N'échanger que les actions d'OSTRALE (150 000 × 1,80 = 270 000 actions) : ce raisonnement est celui d'une absorption par une société qui détiendrait déjà les 70 % ; ici l'absorbante ne détient pas d'actions de l'absorbée, ONDÉRIS doit aussi être rémunérée.
- Calculer la parité sur les VGE (96,00 / 1 800 000 et 62,30 / 500 000), en oubliant les dettes transmises.
- Développer la comptabilisation de la fusion (augmentation du capital nominal, écritures) : hors du champ de l'épreuve.

---

### 1.5 Augmentation de capital réservée et dilution (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | Prix d'émission = (72,00 + 36,00 + 5,40) / 2 700 000 = 113,40 M€ / 2 700 000 = 42,00 € | 0,5 |
| 1.5-02 | 25 200 000 / 42,00 = 600 000 actions nouvelles ; 3 300 000 actions ; ONDÉRIS 73,64 %, OSTRALE 8,18 %, TRÉVANNE 18,18 % ; pertes de 16,36 et 1,82 points | 1 |
| 1.5-03 | Seuil de 51 % : 2 430 000 / 0,51 = 4 764 705 actions au plus, soit 2 064 705 actions nouvelles et 86,72 M€ au maximum | 1 |
| 1.5-04 | Part de la métropole : 60 % × 73,64 % = 44,18 %, soit 44,18 % × 6,60 = 2,92 M€ du résultat net 2028 | 0,5 |

**Conventions rappelées** (annexes 1.4 et 1.5) : prix = valeur des capitaux propres de l'entité fusionnée, synergies comprises, divisée par 2 700 000 actions ; pourcentages à deux décimales ; nombre maximal d'actions arrondi à l'unité inférieure.

**Prix d'émission (0,5 pt).** Valeur de l'entité fusionnée = 72,00 + 36,00 + 5,40 = **113,40 M€** ; prix = 113 400 000 / 2 700 000 = **42,00 €**. Le prix intègre les synergies : TRÉVANNE paie sa part des économies attendues du regroupement.

**Actions nouvelles, répartition et dilution (1 pt).**
- Actions nouvelles : 25 200 000 / 42,00 = **600 000** ; capital après l'opération : 2 700 000 + 600 000 = **3 300 000** actions ; valeur après l'opération : 113,40 + 25,20 = 138,60 M€, soit toujours 42,00 € par action.

| Actionnaire | Actions | Avant | Après | Perte (points) |
|---|---:|---:|---:|---:|
| ONDÉRIS | 2 430 000 | 90,00 % | **73,64 %** | **16,36** |
| OSTRALE Infrastructures | 270 000 | 10,00 % | **8,18 %** | **1,82** |
| TRÉVANNE Énergies | 600 000 | — | **18,18 %** | — |
| **Total** | 3 300 000 | 100,00 % | 100,00 % | |

- Le taux de dilution est de 600 000 / 3 300 000 = 18,18 % : chaque ancien actionnaire conserve 81,82 % de son pourcentage (90,00 % × 81,82 % = 73,64 %). C'est une **dilution du contrôle**, pas de la valeur : le prix d'émission étant égal à la valeur par action, la participation d'ONDÉRIS vaut 2 430 000 × 42,00 = 102,06 M€ avant comme après.

**Montant maximal sous le seuil de 51 % (1 pt).** ONDÉRIS garde ses 2 430 000 actions ; elle doit détenir au moins 51 % du total :
- 2 430 000 / (2 700 000 + n) ≥ 51 % ⇔ 2 700 000 + n ≤ 2 430 000 / 0,51 = 4 764 705,88 ;
- n ≤ 2 064 705,88, soit **2 064 705 actions nouvelles** au plus ;
- montant maximal = 2 064 705 × 42,00 = **86 717 610 €**, soit **86,72 M€**. ONDÉRIS détiendrait alors 51,00 %, TRÉVANNE 43,33 % et OSTRALE 5,67 %.

Le seuil n'est pas contraignant pour le projet (25,20 M€) : l'entité fusionnée pourrait lever auprès de ce partenaire jusqu'à 3,4 fois le montant du projet sans perdre le contrôle par ONDÉRIS.

**Part du résultat revenant indirectement à Valcroze Métropole (0,5 pt).**
- La métropole détient 60 % d'ONDÉRIS, qui détient 73,64 % de l'entité : elle a droit indirectement à 60 % × 73,64 % = **44,18 %** du résultat de l'entité.
- Sur le résultat net 2028 de 6,60 M€ : 44,18 % × 6,60 = **2,92 M€**.
- Repères : avant les opérations, la métropole avait droit à 42,00 % du résultat de Valcroze Biométhane (60 % × 70 %) et à 60 % de celui d'Épuration Sud ; après la seule fusion, à 54,00 % (60 % × 90 %) ; au seuil de 51 %, à 30,60 %.

**Réponses tolérées** : dilution exprimée en pourcentage du contrôle conservé (81,82 %) plutôt qu'en points ; montant maximal calculé sans arrondir le nombre d'actions (86,72 M€ dans les deux cas) ; part de la métropole calculée sur 2 430 000 / 3 300 000 non arrondi (44,18 %) ; avec la valeur de secours de 70,00 € : valeur de l'entité 72,00 + 35,00 + 5,40 = 112,40 M€ pour 2 675 000 actions, soit un prix de 42,02 € ; 25 200 000 / 42,02 = 599 714 actions nouvelles (3 274 714 actions) ; ONDÉRIS 73,67 %, OSTRALE 8,02 %, TRÉVANNE 18,31 % ; pertes de 16,52 et 1,79 points (1,80 sans arrondir les pourcentages) ; au seuil de 51 % : 2 412 500 / 0,51 = 4 730 392 actions, soit 2 055 392 actions nouvelles et 86,37 M€ ; métropole 44,20 %, soit 2,92 M€ : notés en cohérence.

**Erreurs fréquentes**
- Calculer le prix sur les seules valeurs sans synergies (108,00 / 2 700 000 = 40,00 €) : TRÉVANNE recevrait 630 000 actions et capterait une part des synergies sans les payer.
- Diviser la valeur par le nombre d'actions après l'augmentation (113,40 / 3 300 000), ce qui fait payer à TRÉVANNE un prix inférieur à la valeur.
- Résoudre la contrainte de 51 % sur les actions nouvelles seules (51 % × 600 000) ou appliquer 49 % au capital avant l'opération (49 % × 2 700 000 = 1 323 000 actions).
- Additionner les pourcentages au lieu de les multiplier pour la part de la métropole.
- `JUR-T13` — ne pas tirer les conséquences de la nouvelle structure de détention (contrôle d'ONDÉRIS, part économique de la métropole inférieure à la moitié).

---

### 1.6 Synthèse et recommandation (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.6-01 | Valeur créée : synergies de 5,40 M€ partagées selon le capital après la fusion (ONDÉRIS + 4,86 M€, de 97,20 à 102,06 M€ ; OSTRALE + 0,54 M€, de 10,80 à 11,34 M€) ; augmentation de capital neutre au prix de 42,00 € | 1 |
| 1.6-02 | Contrôle : ONDÉRIS reste majoritaire (73,64 %, marge de 61,52 M€ avant le seuil), la métropole contrôle par la chaîne de détention mais n'a droit qu'à 44,18 % du résultat ; place d'OSTRALE et de TRÉVANNE | 1 |
| 1.6-03 | Industriel plutôt que fonds (débouché, compétence, horizon, risques de conflit d'intérêts) et recommandation argumentée assortie de conditions | 1 |

**Valeur créée (1 pt).**
- **Pour ONDÉRIS** : avant les opérations, Épuration Sud (72,00 M€) et 70 % de Valcroze Biométhane (25,20 M€), soit 97,20 M€ ; après la fusion, 2 430 000 × 42,00 = **102,06 M€**, soit **+ 4,86 M€** (90 % des synergies de 5,40 M€).
- **Pour OSTRALE** : 10,80 M€ avant ; 270 000 × 42,00 = **11,34 M€** après, soit **+ 0,54 M€** (10 % des synergies). La parité, calculée sans synergies, les partage selon la part de chacun dans le capital fusionné.
- **L'augmentation de capital** au prix de 42,00 € ne transfère pas de valeur : chaque action vaut 42,00 € avant et après (138,60 / 3 300 000). Elle créera de la valeur si le second méthaniseur rapporte plus que le CMPC ; TRÉVANNE en recevra 18,18 %. La création de valeur dépend donc de la réalité des synergies et de la rentabilité du second méthaniseur, deux estimations.

**Contrôle (1 pt).**
- ONDÉRIS garde **73,64 %** du capital, au-dessus du seuil de 51 % de l'accord entre associés : elle pourrait encore faire entrer 61,52 M€ de fonds propres (86,72 − 25,20) à ce prix sans le franchir. OSTRALE, passé de 30 % de Valcroze Biométhane à 8,18 % de l'entité, perd son droit d'accord sur les investissements ; TRÉVANNE (18,18 %) obtient un siège au conseil.
- La **métropole** garde le contrôle de l'entité par ONDÉRIS, dont elle détient 60 %, mais n'a plus droit qu'à **44,18 %** du résultat (2,92 M€ sur 6,60 M€) : la part publique du résultat diminue, alors que les investissements sont financés par des partenaires privés. C'est la logique de l'ouverture du capital : céder une part des résultats futurs contre des fonds propres, sans perdre la décision.
- ALVÉDRA (28 % d'ONDÉRIS) et la Banque SORNAY (12 %) voient aussi leur part indirecte diminuer (20,62 % et 8,84 % de l'entité) ; la valeur de leur participation est préservée.

**Industriel plutôt que fonds et recommandation (1 pt).**
- **Intérêt d'un industriel** : TRÉVANNE apporte plus que des capitaux. Le contrat d'achat du biométhane sur quinze ans sécurise les recettes du second méthaniseur, alors que le contrat actuel s'arrête en 2034 et pèse sur la valeur terminale (près de 75 % de la VGE). Son équipe d'ingénierie réduit le risque technique. Son horizon est industriel et long, alors qu'un fonds d'infrastructure vise une sortie à date (OSTRALE vers 2031) et un rendement : il a refusé le projet. Un partenaire informé, qui connaît le métier, réduit l'asymétrie d'information (Akerlof, 1970) : il paie un prix proche de la valeur, sans la décote qu'exigerait un investisseur moins informé . Le financement hiérarchique (Myers et Majluf, 1984) placerait la dette de l'entité fusionnée avant l'augmentation de capital ; le recours à un actionnaire se justifie ici par ce qu'il apporte en plus des fonds (contrat d'achat, ingénierie) et par l'endettement déjà élevé de Valcroze Biométhane.
- **Risques** : TRÉVANNE est à la fois actionnaire et client. Il a intérêt à un prix d'achat du biométhane bas, qui réduit le résultat dont 81,82 % revient aux autres actionnaires : c'est un nouveau conflit d'intérêts entre actionnaires, à analyser avec la théorie de l'agence. Il peut aussi demander plus tard une part plus élevée, voire racheter les titres d'OSTRALE. Les usagers de l'assainissement et la métropole sont des parties prenantes dont les intérêts doivent être protégés (Freeman, 1984).
- **Recommandation** (toute recommandation cohérente avec les calculs est acceptée) : réaliser la fusion à la parité de 9 pour 5 et l'augmentation de capital de 25,20 M€ à 42,00 €, sous conditions :
  - faire valider par un expert indépendant le prix du contrat d'achat du biométhane, aux conditions du marché ;
  - maintenir la séparation analytique des deux activités, pour que le prix de l'assainissement ne supporte pas le risque énergétique ;
  - prévoir dans l'accord entre associés les conditions de sortie d'OSTRALE vers 2031 (rachat par ONDÉRIS ou par TRÉVANNE, à une valeur fixée par expertise) et limiter la part de TRÉVANNE pour garder une marge sous le seuil de 51 % ;
  - présenter la valeur de Valcroze Biométhane en fourchette (31 à 41 M€ selon le taux et la croissance) et suivre la réalisation des synergies.

**Réponses tolérées** : recommandation de conserver le fonds et de financer le second méthaniseur par la dette, si le candidat mesure l'endettement déjà élevé de Valcroze Biométhane ; recommandation d'une part plus faible pour TRÉVANNE, argumentée par la part du résultat revenant à la métropole ; avec la valeur de secours de 70,00 € : ONDÉRIS de 96,50 à 101,37 M€ (+ 4,87), OSTRALE de 10,50 à 11,03 M€ (+ 0,53), notés en cohérence.

**Erreurs fréquentes**
- Confondre dilution du contrôle et perte de valeur : au prix de 42,00 €, l'augmentation de capital n'appauvrit pas les actionnaires existants.
- Conclure à une création de valeur égale à la VCP de Valcroze Biométhane (36,00 M€), qui était déjà détenue.
- `JUR-T02` — recommandation sans lien avec les chiffres calculés (synergies, 73,64 %, 44,18 %).
- `JUR-T05` — ignorer les parties prenantes publiques (usagers, métropole) dans l'appréciation de l'opération.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 64 ; programme l. 509-519 | flux de trésorerie disponibles, CMPC, MEDAF, valeur terminale de Gordon-Shapiro, passage de la VGE à la VCP | [V] | F03 § 2 ; F02 |
| Guide pédagogique DSCG, juillet 2026, p. 68-69 ; programme l. 549-554 | gestion du capital (augmentation de capital, dilution) ; motifs des réorganisations ; parité d'échange et nombre d'actions à créer | [V] | F05 § 0, 4 et 5 |
| Corrigé du sujet 2023 (tableau des FTD, valeur terminale, valeur par action) | structure du calcul de la question 1.3 | [V] | F03 § 2 |
| Gordon et Shapiro (1956) | valeur terminale à croissance constante, k > g | [V programme 3.1] | F10 § 2 |
| Sharpe (1964) | MEDAF | [V contexte] | F10 § 2 |
| Jensen et Meckling (1976) | théorie de l'agence (actionnaires / dirigeants), coûts de surveillance | [V programme 2.1] | F10 § 3 |
| Conflits entre actionnaires majoritaire et minoritaire | prolongement de la théorie de l'agence (fonds minoritaire, actionnaire client) | [S] | F08 |
| Freeman (1984) | parties prenantes publiques | [V programme 2.1] | F10 § 3 |
| Akerlof (1970) | asymétrie d'information entre la société et un investisseur extérieur | [V programme 5.1] | F10 § 1 |
| Myers et Majluf (1984) | financement hiérarchique | [V programme 7.2] | F10 § 3 |
| Taux sans risque 4 %, prime de risque du marché 5 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 |
| Valeur d'Épuration Sud, synergies, résultat 2028, seuil de 51 % | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 1.3 et 1.4 |
