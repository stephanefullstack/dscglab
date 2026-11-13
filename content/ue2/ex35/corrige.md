# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 35 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F03 évaluation, F05 ingénierie financière, F06 marchés et finance comportementale, F10 auteurs et théories et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (VGE et multiples des comparables, médianes, VGE, VCP et valeur par action, émission des actions nouvelles, frais et produit net, répartition après l'émission, produits de l'offre, actions et répartition après l'opération, dette financière nette avant et après, barème, liste noire, hors-programme ; fourchette, sursouscription, cession par le fonds, flottant, manque à gagner et variantes de la note vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une fourchette de prix calculée sur une valeur de référence erronée).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Objectifs et coûts de l'introduction, actions nouvelles et actions cédées | `4.2.e` Analyser les introductions en bourse, les retraits de la cotation et les offres publiques ; `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital | 2,5 |
| 2.2 Multiples des comparables, VGE, VCP et valeur par action | `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP ; `3.2.b` Savoir déterminer le multiple d'un échantillon pour valoriser l'entreprise | 4,5 |
| 2.3 Fourchette, prix, produit de l'offre et partage du capital | `4.2.e` ; `4.2.a` | 4 |
| 2.4 Sous-évaluation des introductions et manque à gagner | `4.2.e` | 2 |
| 2.5 Numérique, algorithmes et nouveaux acteurs | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs | 3 |
| 2.6 Note au président : fourchette et répartition de l'offre | `4.2.e` ; `4.2.a` | 1 |
| **Total** | | **17** |

Part du calcul : environ 8,5 points (2.2-01 à 2.2-04, 2.3-01 à 2.3-06, 2.4-02). Part de l'analyse : environ 8,5 points. Les questions 2.4 à 2.6 sont rédactionnelles et valent 6 points : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 2.1 Objectifs et coûts de l'introduction, actions nouvelles et actions cédées (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Objectifs de chaque partie, reliés à l'annexe 2.1 : le groupe (financer 150 M€ d'acquisitions, désendettement, paiement en actions, notoriété) ; les familles (contrôle, au moins 40 %, aucune cession, valeur de marché et liquidité future) ; les cadres (liquidité future, prix de marché, motivation) ; LORVIAN Capital (sortie du fonds avant 2029, en deux temps, prix de marché pour le solde) | 1 |
| 2.1-02 | Coûts : frais directs (commission, conseils, audit ; chiffrage non exigé ici, noté en 2.3-02), coûts récurrents (1,20 M€ par an), transparence et perte de discrétion (stratégie et marges exposées aux concurrents), exposition aux variations du cours et aux attentes de court terme, sous-évaluation volontaire (décote) et éventuelle (premier cours) | 1 |
| 2.1-03 | Actions nouvelles : augmentation de capital, ressources pour le groupe (fonds propres, désendettement), dilution des actionnaires actuels ; actions cédées : liquidité pour LORVIAN Capital, rien pour le groupe, flottant sans dilution | 0,5 |

**Objectifs de chaque partie (1 pt).** Une introduction en bourse est une décision stratégique d'accès au marché : elle sert à la fois à financer l'entreprise, à diversifier ses sources de financement, à donner une liquidité aux actionnaires et à rendre la société plus transparente (guide, p. 71). Les quatre parties n'en attendent pas la même chose :
- **le groupe** cherche des ressources pour financer les acquisitions des trois prochaines années (quatre à six écoles, 150 M€) sans dépendre du seul crédit bancaire. Les fonds propres levés réduisent la dette financière nette et laissent une capacité d'endettement pour la suite. Le titre coté devient aussi une **monnaie d'échange** : le prix d'une école pourra être payé en partie en actions, ce qui intéresse les fondateurs des écoles acquises. La notoriété d'une société cotée rassure les étudiants, les familles, les entreprises qui accueillent les apprentis et les enseignants recrutés ;
- **les familles des fondateurs** veulent garder le contrôle : elles ne cèdent rien, veulent conserver au moins 40 % du capital et rester le premier actionnaire. Elles obtiennent une valeur de marché de leur patrimoine et une liquidité future pour les membres qui ne travaillent pas dans le groupe ;
- **les cadres dirigeants** conservent leurs actions, mais gagnent la possibilité de les céder plus tard à un prix de marché ; le titre coté permet de futurs plans d'intéressement au capital, qui alignent leurs intérêts sur ceux des actionnaires (Jensen et Meckling, 1976) ;
- **LORVIAN Capital** doit rendre leurs apports à ses investisseurs d'ici 2029 : l'introduction organise sa **sortie en deux temps**. Il cède un peu plus d'un tiers de ses titres dans l'offre (37,50 %), puis le solde sur le marché ou par blocs, à un prix désormais observable. La bourse lui offre une sortie sans chercher un acquéreur unique, qui exigerait le contrôle et heurterait l'objectif des familles.

**Coûts de l'introduction (1 pt).**
- **Frais directs** : commission des banques de 3 % du produit brut et autres frais de 3,60 M€, soit 7,92 M€ pour le groupe (5,50 % des 144,00 M€ levés, question 2.3) ; LORVIAN Capital supporte sa propre commission (3,24 M€).
- **Coûts récurrents de la cotation** : 1,20 M€ par an de communication financière, d'honoraires, d'administrateurs indépendants et de relations avec les investisseurs (annexe 2.1).
- **Transparence et perte de discrétion** : publication semestrielle des comptes et de l'information extra-financière, information immédiate du marché ; la stratégie d'acquisition, les marges par école et les difficultés (abandons, baisse du financement de l'apprentissage) deviennent visibles des concurrents et des écoles que le groupe veut acheter, qui peuvent en tenir compte dans leur prix.
- **Exposition au marché** : le cours dépend aussi de l'humeur du marché ; un chiffre d'affaires de rentrée décevant peut le faire chuter (annexe 2.6) ; la pression du court terme peut peser sur les choix de long terme (investissements pédagogiques, campus).
- **Sous-évaluation** : la décote de 10 % à 15 % accordée volontairement aux souscripteurs, et l'écart éventuel entre le prix et le premier cours (question 2.4), sont un coût indirect supporté par le groupe et par LORVIAN Capital, souvent supérieur aux frais directs.

**Actions nouvelles et actions cédées (0,5 pt).**
- Les **actions nouvelles** (augmentation de capital de 144,00 M€) apportent au groupe des fonds propres et de la trésorerie : c'est la partie « financement » de l'opération, qui sert les acquisitions et réduit la dette. Elles diluent les actionnaires actuels : les familles passent de 51 % à 42,50 % (question 2.3).
- Les **actions cédées** par LORVIAN Capital (6 000 000 actions) ne rapportent rien au groupe : le produit va au fonds. Elles ne modifient pas le nombre d'actions et ne diluent personne ; elles augmentent le flottant et donc la liquidité du titre. Le mélange des deux, décidé par les actionnaires, est un choix de **gestion du capital** (programme 4.2.a).

**Réponses tolérées** : objectifs présentés par thème (financement, liquidité, contrôle, notoriété) plutôt que par partie, si chaque partie est rattachée ; mention de l'effet de signal de la cotation pour les recrutements ; coût d'agence entre actionnaires de contrôle et minoritaires après l'introduction.

**Erreurs fréquentes**
- Écrire que l'introduction en bourse apporte au groupe le produit de la cession de LORVIAN Capital.
- Ne citer que les frais directs, sans la transparence, la perte de discrétion et la sous-évaluation.
- Développer la procédure de l'Autorité des marchés financiers, le contenu du document d'information ou la transformation en société anonyme : hors du champ de l'épreuve.
- `JUR-T13` — objectifs généraux d'une introduction sans les données de l'annexe 2.1.

---

### 2.2 Multiples des comparables, VGE, VCP et valeur par action (4,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | VGE des comparables = capitalisation + DFN + intérêts minoritaires : 1 296,00 ; 528,00 ; 1 624,00 ; 624,00 ; 888,00 M€ | 1 |
| 2.2-02 | Quinze multiples (tableau ci-dessous) | 1 |
| 2.2-03 | Médianes : VGE / CA 2,60 ; VGE / EBITDA 11,20 ; PER 25,00 | 0,5 |
| 2.2-04 | ESTRAVELLE : VGE 972,40 et VCP 725,20 M€ (18,13 €) ; VGE 1 047,20 et VCP 800,00 M€ (20,00 €) ; VCP 750,00 M€ (18,75 €) | 1 |
| 2.2-05 | Pertinence de l'échantillon et des agrégats ; choix argumenté du multiple VGE / EBITDA | 1 |

**Conventions rappelées** (annexe 2.7) : VGE d'un comparable = capitalisation + dette financière nette + intérêts minoritaires ; agrégats de 2027 ; multiples à deux décimales ; médiane des cinq valeurs ; VCP d'ESTRAVELLE = VGE − dette financière nette au 30 juin 2027 (247,20 M€) − intérêts minoritaires (néant) ; 40 000 000 actions.

**VGE et multiples des comparables (2 pts).** Un multiple de VGE se rapporte à un agrégat qui rémunère tous les apporteurs de fonds (chiffre d'affaires, EBITDA) ; un multiple de capitaux propres (PER) se rapporte au résultat qui revient aux seuls actionnaires (guide, p. 65). Les intérêts minoritaires entrent dans la VGE, car le chiffre d'affaires et l'EBITDA consolidés comprennent la part des filiales qui revient aux minoritaires ; le PER utilise le résultat part du groupe, cohérent avec la capitalisation.

| Société | Capitalisation | + DFN | + Minoritaires | = VGE | VGE / CA | VGE / EBITDA | PER |
|---|---:|---:|---:|---:|---:|---:|---:|
| VALCENDRE Éducation | 960,00 | 336,00 | 0,00 | **1 296,00** | 1 296,00 / 540,00 = **2,40** | 1 296,00 / 120,00 = **10,80** | 960,00 / 38,40 = **25,00** |
| OSTREVAL Formation | 357,00 | 159,00 | 12,00 | **528,00** | **2,20** | **9,60** | **21,00** |
| HALDENRATH Bildung | 1 200,00 | 398,00 | 26,00 | **1 624,00** | **2,90** | **11,20** | **24,00** |
| MIRASOLA Educación | 456,00 | 168,00 | 0,00 | **624,00** | **2,60** | **12,00** | **28,50** |
| QUILLBRIDGE Learning | 882,00 | 6,00 | 0,00 | **888,00** | **4,80** | **18,50** | **42,00** |

**Médianes (0,5 pt).** Échantillons classés : VGE / CA : 2,20 ; 2,40 ; **2,60** ; 2,90 ; 4,80. VGE / EBITDA : 9,60 ; 10,80 ; **11,20** ; 12,00 ; 18,50. PER : 21,00 ; 24,00 ; **25,00** ; 28,50 ; 42,00. La médiane est la troisième valeur : **2,60**, **11,20** et **25,00**. Elle n'est pas déformée par QUILLBRIDGE, dont les multiples sont très supérieurs aux autres.

**Valeur d'ESTRAVELLE Éducation avant l'opération (1 pt).**

| Multiple médian | Agrégat 2027 | VGE | − DFN | = VCP | Par action (VCP / 40 000 000) |
|---|---:|---:|---:|---:|---:|
| VGE / CA : 2,60 | 374,00 | 972,40 | − 247,20 | **725,20** | **18,13 €** |
| VGE / EBITDA : 11,20 | 93,50 | 1 047,20 | − 247,20 | **800,00** | **20,00 €** |
| PER : 25,00 | 30,00 | — | — | **750,00** | **18,75 €** |

Les trois méthodes donnent une VCP de 725,20 à 800,00 M€, soit de 18,13 € à 20,00 € par action. Ces valeurs sont **avant l'opération** : le produit de l'augmentation de capital n'est ni ajouté ni retranché (annexe 2.7).

**Pertinence de l'échantillon et des agrégats ; choix de la méthode (1 pt).**
- **Un échantillon homogène, sauf une société.** Quatre sociétés exercent le même métier qu'ESTRAVELLE (écoles et universités privées sur campus), en Europe et en IFRS. **QUILLBRIDGE** s'en écarte : formation entièrement en ligne, sans campus loué (dette financière nette de 6,00 M€), croissance attendue de 22 % par an contre 4 % à 9 % pour les autres. Ses multiples (18,50 fois l'EBITDA, PER de 42,00) paient une croissance qu'ESTRAVELLE n'a pas (+ 10 % en 2027) : c'est une valeur atypique, que la médiane neutralise. La moyenne la retiendrait (VGE / EBITDA moyen de 12,42 : 22,85 € par action). Sans QUILLBRIDGE, la médiane des quatre autres serait de 11,00 fois l'EBITDA : le résultat reste proche.
- **Taille, pays et modèle.** ESTRAVELLE (374,00 M€ de chiffre d'affaires) est dans la moyenne de l'échantillon (185 à 560 M€). Mais les sociétés étrangères ne dépendent pas du financement français de l'apprentissage (36 % des étudiants d'ESTRAVELLE), dont les niveaux de prise en charge ont baissé en 2025 et pourraient encore baisser (annexe 2.2) : ce risque propre peut justifier une prudence. OSTREVAL, très exposée à l'apprentissage, a les multiples les plus bas.
- **Des agrégats cohérents.** Les multiples sont calculés sur des agrégats **de 2027 estimés**, appliqués aux prévisions de 2027 d'ESTRAVELLE : même période, même référentiel IFRS, dettes locatives comprises dans la dette nette des deux côtés, ce qui rend l'EBITDA (avant loyers des campus) comparable. Appliquer ces multiples à l'EBITDA réalisé de 2026 (81,60 M€) mélangerait deux périodes et sous-évaluerait la société (16,67 € par action). Les prévisions de la direction restent à vérifier : elles sont revues par les banques, mais la direction a intérêt à un prix élevé (asymétrie d'information).
- **La dette nette au 30 juin** est proche de son point haut saisonnier, puisque les frais de scolarité sont encaissés de septembre à janvier : la VCP est prudente. Une dette nette moyenne de l'année serait plus juste, mais elle n'est pas fournie.
- **Choix du multiple.** Le **VGE / EBITDA** est le plus adapté : il compare la performance d'exploitation avant amortissements et frais financiers, indépendamment de la structure financière et des politiques d'amortissement, et il tient compte de la marge. Le **VGE / CA** ignore la rentabilité : ESTRAVELLE, avec une marge d'EBITDA de 25,00 % contre 22,92 % pour la médiane de l'échantillon, en est pénalisée (18,13 €). Le **PER** dépend de l'endettement, des amortissements et du coût de la dette de chaque société. Il donne 750,00 M€, soit une VGE implicite de 997,20 M€ (10,67 fois l'EBITDA) : le résultat net d'ESTRAVELLE est encore alourdi par les frais financiers d'avant l'introduction. La valeur de référence de **20,00 €** retenue par les banques est donc défendable, dans une fourchette de 18,13 € à 20,00 €.

**Réponses tolérées** : multiples non arrondis, si les médianes sont justes ; argument selon lequel ESTRAVELLE, qui croît de 10 % en 2027 contre 4 % à 9 % par an pour les quatre comparables sur campus, pourrait justifier un multiple un peu supérieur à la médiane, si le candidat note que la croissance d'ESTRAVELLE au-delà de 2027 n'est pas fournie ; tableau présenté par multiple plutôt que par société ; fourchette fondée sur les trois méthodes ou sur deux d'entre elles, si le choix est justifié ; retrait de QUILLBRIDGE de l'échantillon, avec la médiane des quatre autres (VGE / EBITDA 11,00 : VCP 781,30 M€, 19,53 € par action), si le retrait est justifié ; mention d'une décote d'illiquidité ou de taille, sans calcul.

**Erreurs fréquentes**
- Calculer la VGE des comparables sans les intérêts minoritaires (OSTREVAL : 516,00 ; HALDENRATH : 1 598,00), ou rapporter la capitalisation, et non la VGE, au chiffre d'affaires et à l'EBITDA.
- Retenir la **moyenne** au lieu de la médiane imposée par l'annexe 2.7 : 12,42 fois l'EBITDA, VCP de 914,07 M€, 22,85 € par action, valeur tirée vers le haut par QUILLBRIDGE.
- Oublier de déduire la dette financière nette de la VGE : 1 047,20 M€ présentés comme VCP, soit 26,18 € par action.
- Déduire la dette nette de la valeur obtenue par le PER, qui donne déjà une VCP.
- Ajouter le produit de l'augmentation de capital à la valeur avant l'opération.
- `JUR-E03` — présenter une seule valeur sans la comparer aux autres méthodes ni discuter l'échantillon.
- `JUR-T07` — multiples des comparables présentés sans tableau.

---

### 2.3 Fourchette, prix, produit de l'offre et partage du capital (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Fourchette 20,00 × 0,85 = 17,00 € à 20,00 × 0,90 = 18,00 € ; sursouscription au prix de 18,00 € : 42 000 000 / 14 000 000 = 3,00 fois | 0,5 |
| 2.3-02 | Actions nouvelles 144,00 M€ / 18,00 = 8 000 000 ; produit brut 144,00 ; frais 4,32 + 3,60 = 7,92 ; produit net 136,08 M€ | 1 |
| 2.3-03 | LORVIAN Capital : produit brut 6 000 000 × 18,00 = 108,00 ; commission 3,24 ; produit net 104,76 M€ | 0,5 |
| 2.3-04 | Capitalisation 48 000 000 × 18,00 = 864,00 M€ ; flottant 14 000 000 actions, 29,17 % du capital, 252,00 M€ | 0,5 |
| 2.3-05 | Répartition du capital avant (51 % ; 9 % ; 40 %) et après (42,50 % ; 7,50 % ; 20,83 % ; public 29,17 %), en nombre d'actions et en pourcentage | 1 |
| 2.3-06 | Dette financière nette 247,20 − 136,08 = 111,12 M€ ; DFN / EBITDA 2027 de 2,64 à 1,19 | 0,5 |

**Conventions rappelées** (annexes 2.4 et 2.7) : décote de 10 % (borne haute) à 15 % (borne basse) sur la valeur de référence ; rompus arrondis à l'unité inférieure ; commission de 3,00 % à la charge de chaque vendeur ; autres frais de 3,60 M€ pour le groupe ; flottant = actions nouvelles + actions cédées ; opération supposée réalisée au 30 juin 2027 pour la dette nette.

**Fourchette et sursouscription (0,5 pt).**
- Borne haute = 20,00 × (1 − 10 %) = **18,00 €** ; borne basse = 20,00 × (1 − 15 %) = **17,00 €**.
- Au prix retenu de 18,00 €, l'offre porte sur 8 000 000 actions nouvelles et 6 000 000 actions cédées, soit 14 000 000 actions (252,00 M€). La demande atteint 42 000 000 actions : taux de sursouscription = 42 000 000 / 14 000 000 = **3,00 fois**. La demande restant forte en haut de fourchette, les banques retiennent ce prix : le carnet d'ordres sert à **découvrir le prix** que le marché accepte. La demande diminue quand le prix monte : à 17,00 €, l'offre porterait sur 8 470 588 actions nouvelles et 6 000 000 actions cédées, et la sursouscription atteindrait 58 800 000 / 14 470 588 = 4,06 fois.

**Actions nouvelles et produit pour le groupe (1 pt).**
- Actions nouvelles = 144 000 000 / 18,00 = **8 000 000** actions (pas de rompu à ce prix).
- Produit brut = 8 000 000 × 18,00 = **144,00 M€**.
- Frais = commission 3,00 % × 144,00 = 4,32 M€ + autres frais 3,60 M€ = **7,92 M€** (5,50 % du produit brut).
- Produit net = 144,00 − 7,92 = **136,08 M€**.

**Cession par LORVIAN Capital (0,5 pt).** Produit brut = 6 000 000 × 18,00 = **108,00 M€** ; commission = 3,00 % × 108,00 = **3,24 M€** ; produit net = **104,76 M€**, encaissé par le fonds et non par le groupe. LORVIAN Capital cède 37,50 % de ses 16 000 000 actions et en conserve 10 000 000.

**Capitalisation et flottant (0,5 pt).**
- Actions après l'opération = 40 000 000 + 8 000 000 = 48 000 000. Capitalisation au prix d'introduction = 48 000 000 × 18,00 = **864,00 M€** (720,00 M€ pour les actions existantes au prix d'introduction, plus 144,00 M€ levés).
- Flottant = 8 000 000 actions nouvelles + 6 000 000 actions cédées = **14 000 000 actions**, soit 14 / 48 = **29,17 %** du capital et **252,00 M€** au prix d'introduction. Il dépasse les 25 % souhaités par les banques pour la liquidité, mais reste modeste en valeur : ESTRAVELLE sera une valeur moyenne.

**Répartition du capital avant et après l'opération (1 pt).**

| Actionnaire | Actions avant | % avant | Mouvement | Actions après | % après |
|---|---:|---:|---|---:|---:|
| Familles des fondateurs | 20 400 000 | 51,00 % | — | 20 400 000 | **42,50 %** |
| Cadres dirigeants | 3 600 000 | 9,00 % | — | 3 600 000 | **7,50 %** |
| LORVIAN Capital | 16 000 000 | 40,00 % | − 6 000 000 cédées | 10 000 000 | **20,83 %** |
| Public (flottant) | — | — | + 8 000 000 nouvelles + 6 000 000 achetées | 14 000 000 | **29,17 %** |
| **Total** | **40 000 000** | **100 %** | | **48 000 000** | **100 %** |

L'émission dilue de 16,67 % (8 / 48) les actionnaires actuels : les familles perdent 8,50 points et les cadres 1,50 point, sans rien céder. La cession de LORVIAN Capital réduit sa part de 40 % à 20,83 % sans diluer personne. Les familles restent le premier actionnaire, au-dessus du seuil de 40 % qu'elles se sont fixé, mais perdent la majorité du capital ; avec les cadres, elles détiennent 50,00 %.

**Effet sur la dette financière nette (0,5 pt).** Dette financière nette après l'opération = 247,20 − 136,08 = **111,12 M€**. Le rapport dette financière nette / EBITDA 2027 passe de 247,20 / 93,50 = **2,64** à 111,12 / 93,50 = **1,19**. Le groupe retrouve une large capacité d'endettement pour financer, avec la dette, les 150 M€ d'acquisitions prévues : seules les actions nouvelles produisent cet effet.

**Réponses tolérées** : fourchette exprimée avec la décote appliquée aux autres valeurs de la question 2.2, si elle est cohérente avec l'annexe 2.4 ; frais exprimés en pourcentage ; flottant défini sans les actions des cadres, si l'hypothèse est écrite ; répartition après l'opération présentée en deux étapes (après l'émission, puis après la cession).

**Erreurs fréquentes**
- Appliquer la décote au mauvais sens (borne haute à 15 %) ou à la VCP totale sans la rapporter à l'action.
- Calculer les actions nouvelles sur le produit net (136,08 / 18,00) ou sur l'offre totale (252,00 / 18,00 = 14 000 000 actions nouvelles).
- Compter le produit de la cession de LORVIAN Capital dans le produit pour le groupe, ou dans la baisse de la dette nette.
- Calculer les pourcentages après l'opération sur 40 000 000 actions, ou oublier de retrancher les actions cédées de la part de LORVIAN Capital (33,3 % au lieu de 20,83 %).
- Exclure les actions cédées du flottant (8 000 000 actions, 16,67 %).
- `JUR-I03` — structure de l'actionnariat après l'opération non calculée ou non commentée (contrôle des familles).

---

### 2.4 Sous-évaluation des introductions et manque à gagner (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Explication par les asymétries d'information (Akerlof, 1970), la protection des investisseurs peu informés, la rémunération des investisseurs qui révèlent leur demande, l'intérêt des banques au succès de l'offre ; signal des fondateurs qui ne cèdent rien et de LORVIAN Capital qui conserve 62,50 % de ses titres (Spence, 1973) ; lecture d'une émission d'actions par le marché (Myers et Majluf, 1984) | 1 |
| 2.4-02 | Rendement initial 21,60 / 18,00 − 1 = 20,00 % ; manque à gagner du groupe 8 000 000 × 3,60 = 28,80 M€, de LORVIAN Capital 21,60 M€, total 50,40 M€ ; 3,64 fois les frais directs du groupe (7,92 M€) | 1 |

**Pourquoi les actions sont introduites sous leur valeur (1 pt).**
- **Asymétrie d'information.** Avant l'introduction, la société n'a pas de cours : les dirigeants et les actionnaires connaissent mieux qu'eux la qualité des écoles, la solidité des prévisions et les risques (abandons d'étudiants, baisse du financement de l'apprentissage). Au sens d'Akerlof (1970), l'investisseur qui ne peut distinguer une bonne société d'une mauvaise exige une décote, faute de quoi il ne souscrit pas : le prix d'introduction est fixé en dessous de la valeur estimée (20,00 €) pour attirer une demande suffisante.
- **Des investisseurs inégalement informés.** Les investisseurs les mieux informés ne souscrivent qu'aux bonnes introductions ; les particuliers peu informés reçoivent alors beaucoup de titres dans les mauvaises et peu dans les bonnes. Pour que ces derniers continuent de participer, les introductions doivent leur être, en moyenne, favorables. Dans le cas présent, la demande des particuliers (4 200 000 actions pour environ 1 400 000 offertes) ne sera servie qu'à un tiers environ.
- **Rémunérer la révélation de la demande.** Les investisseurs institutionnels indiquent dans le carnet d'ordres le prix qu'ils sont prêts à payer : la décote les rémunère de cette information, qui permet aux banques de fixer le prix (18,00 €, haut de fourchette).
- **L'intérêt des banques** : une offre qui échoue ou un cours qui baisse dès le premier jour nuit à leur réputation ; elles préfèrent un prix prudent, d'autant que leur commission varie peu avec le prix.
- **Le signal des actionnaires.** Selon Spence (1973), un signal est crédible s'il est coûteux à imiter. Les familles et les cadres ne cèdent **aucune** action et s'engagent à conserver leurs titres 180 jours ; les familles gardent 42,50 % du capital. Elles restent ainsi exposées à la valeur future du groupe : seuls des actionnaires confiants dans les perspectives accepteraient ce risque. LORVIAN Capital conserve 62,50 % de ses titres sous engagement de conservation, ce qui atténue le signal négatif de sa cession. À l'inverse, selon Myers et Majluf (1984), une émission d'actions peut être lue comme le signe que les dirigeants jugent le titre cher : le fait que le produit finance des acquisitions identifiées et que les fondateurs ne vendent pas limite cette lecture.

**Rendement initial et manque à gagner (1 pt).**
- Rendement initial du souscripteur = 21,60 / 18,00 − 1 = **20,00 %** en un jour.
- Manque à gagner = actions vendues × (21,60 − 18,00) :
  - **groupe** : 8 000 000 × 3,60 = **28,80 M€** : à 21,60 €, le groupe aurait levé 172,80 M€ avec le même nombre d'actions, ou environ 144,00 M€ avec 6 666 666 actions nouvelles, soit 1 333 334 actions de moins ;
  - **LORVIAN Capital** : 6 000 000 × 3,60 = **21,60 M€** ;
  - au total, **50,40 M€** ont été « laissés » aux souscripteurs.
- Le manque à gagner du groupe représente **3,64 fois** ses frais directs (28,80 / 7,92) : la sous-évaluation est le premier coût de l'introduction. Il est supporté par les actionnaires actuels, dilués à un prix inférieur au cours. La décote voulue (10 % sous la valeur de référence) explique une partie de l'écart. Au premier cours, la capitalisation atteint 1 036,80 M€, au-dessus de la valeur par les comparables après l'opération (environ 19,50 € par action, produit net compris) : l'engouement des acheteurs, la sursouscription et le faible flottant y contribuent aussi.

**Réponses tolérées** : explication par la « malédiction du vainqueur » des investisseurs peu informés, sans auteur ; mention de l'ancrage sur le prix d'introduction ou de l'engouement des particuliers (Kahneman et Tversky, 1973) ; manque à gagner rapporté au produit brut (20,00 %) ; commentaire sur le fait que le premier cours n'est qu'une hypothèse et peut ne pas se maintenir.

**Erreurs fréquentes**
- Attribuer le manque à gagner du groupe aux actions cédées par LORVIAN Capital, ou calculer le manque à gagner sur les 48 000 000 actions (172,80 M€).
- Présenter la sous-évaluation comme une erreur des banques, sans l'asymétrie d'information.
- Confondre asymétrie d'information (avant le contrat) et aléa moral (après).
- `JUR-M01` — explication sans théorie de l'information ou du signal ; `JUR-T14` — théorie citée sans lien avec les données de l'offre.

---

### 2.5 Numérique, algorithmes et nouveaux acteurs (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Souscription des particuliers par des courtiers en ligne et des applications (accès élargi, coûts faibles, actionnariat de proximité, risques de reventes rapides et de mimétisme) ; carnet d'ordres électronique (rapidité, découverte du prix, allocation) | 1 |
| 2.5-02 | Trading algorithmique et à haute fréquence : apport de liquidité et réduction de l'écart achat-vente en temps normal, retrait brutal en période de tension, volatilité accrue sur une valeur moyenne peu échangée | 1 |
| 2.5-03 | Intelligence artificielle des investisseurs (lecture automatique de l'information, réactions instantanées, biais et mimétisme) ; synthèse des avantages et des risques pour ESTRAVELLE et mesures (communication financière claire, suivi des réseaux, relations avec les investisseurs) | 1 |

**Souscription en ligne et carnet électronique (1 pt).**
- **Les courtiers en ligne et les applications d'investissement** sont des nouveaux acteurs, souvent des fintechs, qui ont baissé le coût et la difficulté de l'accès à la bourse : inscription en quelques minutes, frais faibles ou nuls, document d'information résumé à l'écran, notification de l'offre (annexe 2.6). Plus de huit ordres de particuliers sur dix sont passés en ligne.
- **Pour ESTRAVELLE**, c'est l'occasion d'élargir son actionnariat à des particuliers proches du groupe (anciens élèves, familles d'étudiants, entreprises partenaires), qui connaissent ses marques : diversification des actionnaires, notoriété, demande de titres. Dans le cas présent, la demande des particuliers dépasse largement la part qui leur est réservée.
- **Les risques** : des montants unitaires faibles (2 000 € en moyenne), des souscripteurs qui n'ont pas toujours lu les risques et qui revendent dès le premier jour ; les forums amplifient l'engouement comme la déception (comportement mimétique, biais de disponibilité). Le groupe doit fournir une information compréhensible par tous.
- **Le carnet d'ordres électronique** centralise en temps réel les ordres des investisseurs, avec leur prix limite : il accélère la constitution de la demande, permet aux banques de mesurer la sursouscription à chaque prix (annexe 2.5) et de fixer le prix et les allocations, et réduit les coûts de traitement.

**Trading algorithmique et à haute fréquence (1 pt).**
- Après l'introduction, la plupart des ordres sur le titre passeront par des algorithmes ; les opérateurs à haute fréquence achètent et revendent en quelques microsecondes, en tenant le marché ou en arbitrant entre plateformes.
- **En temps normal**, ils apportent de la liquidité : l'écart entre le prix d'achat et le prix de vente proposés se réduit, ce qui abaisse le coût des transactions et rend le titre plus attractif pour les investisseurs, et le cours intègre plus vite l'information (efficience au sens de Fama, 1970).
- **En période de tension**, ils se retirent : la liquidité disparaît quand on en a besoin. Sur une valeur moyenne au flottant de 252,00 M€ et peu suivie, une publication décevante peut provoquer une chute brutale (− 14 % en vingt minutes dans l'exemple de l'annexe 2.6), sans rapport durable avec la valeur. La période sensible pour ESTRAVELLE est la publication du chiffre d'affaires et des effectifs de la rentrée, chaque automne.

**Intelligence artificielle, avantages et risques pour le groupe (1 pt).**
- **Les investisseurs utilisent l'intelligence artificielle** pour lire en quelques secondes les communiqués, les documents publiés, les avis d'étudiants en ligne et les réseaux sociaux, et en tirer des signaux d'achat ou de vente. Une phrase ambiguë peut déclencher des ventes automatiques avant toute analyse humaine. Ces outils reproduisent les biais de leurs données et peuvent agir dans le même sens au même moment (mimétisme algorithmique).
- **Avantages pour ESTRAVELLE** : un actionnariat plus large et plus diversifié, une notoriété accrue, une souscription rapide et peu coûteuse, une liquidité qui facilite la sortie progressive de LORVIAN Capital et les cessions futures des cadres, un cours qui intègre vite les bonnes nouvelles.
- **Risques** : volatilité accrue d'une valeur moyenne, retournements brutaux à chaque publication ou rumeur, actionnaires de court terme, sensibilité à la réputation en ligne (avis d'étudiants, controverses), cybersécurité de l'information publiée.
- **Mesures** : une communication financière claire, régulière et cohérente (indicateurs suivis d'une année sur l'autre, sans formule ambiguë) ; des relations suivies avec les investisseurs et les analystes, qui élargissent le suivi du titre ; une veille des réseaux sociaux et des avis en ligne ; un calendrier de publication connu à l'avance. Le flottant pourra être élargi par la sortie progressive de LORVIAN Capital, ce qui améliorera la liquidité.

**Réponses tolérées** : mention d'un contrat de liquidité confié à un prestataire pour animer le titre, sans détail juridique ; mention de l'encadrement du trading à haute fréquence par la réglementation européenne des marchés, sans développement ; lien avec la finance comportementale (Kahneman et Tversky, 1973 ; Taleb, 2007, pour un retournement extrême).

**Erreurs fréquentes**
- Décrire la technique des algorithmes ou de l'intelligence artificielle au lieu de leurs effets sur la liquidité et sur le cours.
- Ne présenter que des avantages, ou que des risques, sans les relier à la situation d'une valeur moyenne au flottant limité.
- Confondre les courtiers en ligne avec les plateformes de financement participatif, qui ne servent pas à une introduction sur un marché réglementé.
- `JUR-M02` — rôle des nouveaux acteurs non relié au financement et à l'actionnariat du groupe ; `JUR-T13` — exposé général sans les données de l'annexe 2.6.

---

### 2.6 Note au président : fourchette et répartition de l'offre (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Note structurée : fourchette recommandée et justifiée (17,00 € à 18,00 €, ou toute fourchette cohérente) ; répartition entre actions nouvelles (besoin de 150 M€, désendettement) et actions cédées (sortie de LORVIAN Capital, flottant) ; contrôle des familles (42,50 % au prix haut, 42,09 % au prix bas, au plus 11 000 000 actions nouvelles pour rester à 40 %) ; conditions (engagements de conservation, sortie ordonnée du fonds) | 1 |

**Exemple de note** (une note de dix à quinze lignes reprenant ces éléments obtient la totalité du point)

> **À** : M. Hugues TAVERNOL, président — **De** : cabinet — **Objet** : paramètres de l'introduction en bourse
>
> **1. Fourchette.** Je recommande de retenir la fourchette des banques, **17,00 € à 18,00 €**. Elle applique une décote de 10 % à 15 % à la valeur de 20,00 € obtenue avec le multiple médian de l'EBITDA de sociétés comparables, la méthode la plus pertinente pour le groupe ; les autres méthodes donnent 18,13 € et 18,75 €. Cette décote est le prix de l'asymétrie d'information sur un secteur mal connu des investisseurs ; une fourchette plus haute exposerait l'offre à l'échec. Si le carnet d'ordres le confirme (3 fois l'offre à 18,00 €), le prix doit être fixé en haut de fourchette : à 17,00 €, il faudrait émettre 470 588 actions de plus pour lever les mêmes 144,00 M€ (les familles tomberaient à 42,09 %), et LORVIAN Capital perdrait 6,00 M€.
>
> **2. Répartition de l'offre.** Je recommande de maintenir l'augmentation de capital à **144,00 M€** (8 000 000 actions à 18,00 €) : avec un produit net de 136,08 M€, la dette nette rapportée à l'EBITDA tombe de 2,64 à 1,19, ce qui permet de financer les 150 M€ d'acquisitions prévues avec un appoint de dette. La cession de **6 000 000 actions** par LORVIAN Capital porte le flottant à 29,17 % sans diluer les familles ; le solde de ses titres doit être vendu de façon ordonnée, après l'engagement de conservation de 180 jours.
>
> **3. Contrôle des familles.** Les familles détiendront **42,50 %** du capital à 18,00 €, et encore 42,09 % au bas de la fourchette. Elles restent de loin le premier actionnaire et, avec les cadres, détiennent 50,00 %. Pour rester au-dessus de 40 %, le groupe ne doit pas émettre plus de 11 000 000 actions nouvelles (198,00 M€ à 18,00 €) : il ne faut donc pas augmenter l'émission au-delà de ce que le programme d'acquisitions justifie, ni payer de grosses acquisitions en actions sans vérifier ce seuil.

**Réponses tolérées** : toute fourchette et toute répartition cohérentes avec les calculs du candidat et justifiées (par exemple une fourchette resserrée de 17,50 € à 18,00 €, compte tenu de la sursouscription ; une augmentation de capital réduite et compensée par une cession plus importante de LORVIAN Capital, pour limiter la dilution des familles et élargir le flottant ; une offre à deux temps).

**Erreurs fréquentes**
- Recommander de faire céder des actions aux familles, contraire à leur objectif.
- Proposer une émission qui ferait passer les familles sous 40 % du capital.
- Recommander le prix le plus élevé possible, sans tenir compte du risque d'échec de l'offre.
- `JUR-T01` — note sans posture de conseil (fourchette, montants, conditions) ; `JUR-T02` — recommandation sans lien avec les chiffres (20,00 € ; 42,50 % ; 136,08 M€).

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 64-65 ; programme l. 521-528 | inducteurs de VGE et de VCP, passage de la VGE à la VCP, échantillon de comparables, multiple médian | [V] | F03 § 3 |
| Guide pédagogique DSCG, juillet 2026, p. 68 ; programme l. 549 | gestion du capital : opérations sur le nombre d'actions, dilution | [V] | F05 § 0 |
| Guide pédagogique DSCG, juillet 2026, p. 70-71 ; programme l. 557 | objectifs et mécanismes d'une introduction en bourse (titres nouveaux et cédés, fixation du prix), asymétries d'information, réactions du marché | [V] | F05 § 6 ; F06 § 5 |
| Décote d'introduction et sous-évaluation initiale | explication par l'asymétrie d'information entre investisseurs | [S] | F05 § 6 ; F06 § 2 |
| Programme l. 599-604 ; guide p. 51 | numérique, fintechs, trading à haute fréquence, intelligence artificielle | [V] | F06 § 6 |
| Akerlof (1970) | asymétrie d'information et sélection adverse | [V programme 5.1] | F10 § 1 |
| Fama (1970) | efficience informationnelle | [V programme 5.1] | F10 § 1 |
| Kahneman et Tversky (1973) | biais et comportement mimétique des investisseurs | [V programme 5.1] | F10 § 1 |
| Spence (1973) | théorie du signal | [V programme 4.1] | F10 § 3 |
| Myers et Majluf (1984) | lecture d'une émission d'actions par le marché | [V programme 7.2] | F10 § 3 |
| Jensen et Meckling (1976) | alignement des intérêts des cadres | [V programme 2.1] | F10 § 3 |
| Échantillon, agrégats, dette nette, structure de l'offre, carnet d'ordres, premier cours, articles de presse | hypothèses d'énoncé fictives, à utiliser telles quelles | — | annexes 2.1 à 2.6 |
