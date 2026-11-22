# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 62 — Dossier 2 (18 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F05 ingénierie financière, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (équilibre du bilan, bêtas désendettés des comparables et leur moyenne, bêta réendetté, MEDAF avec prime, CMPC, flux de trésorerie disponibles, flux actualisés, valeurs terminales avec et sans croissance, VGE et VCP, multiples, ANCC et impôt latent, valeur actuelle des synergies, barème, liste noire, hors-programme ; dette financière nette, poids de la valeur terminale, marges implicites, prix maximal, paiement en actions, dette pro forma et charges annuelles vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VCP calculée avec un CMPC erroné à la question 2.1, ou un prix maximal calculé avec une VCP erronée à la question 2.3).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Bêtas des comparables, coût des fonds propres, prime de taille et d'illiquidité, CMPC | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance ; `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché | 2,5 |
| 2.2 Flux de trésorerie disponibles tirés du business plan fourni | `3.1.b` Construire un business plan | 1,5 |
| 2.3 Valeur terminale avec et sans croissance, VGE et VCP, poids de la valeur terminale | `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance ; `3.1.d` Distinguer la valeur globale de l'entreprise (VGE) de la valeur des capitaux propres (VCP) | 3 |
| 2.4 Multiples de transactions et multiples boursiers, choix des inducteurs | `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP | 2,5 |
| 2.5 Actif net comptable corrigé et portée de l'approche patrimoniale | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine | 2 |
| 2.6 Risque spécifique et risque systématique : cédants et actionnaires d'ONDAVÈRE | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché | 1,5 |
| 2.7 Synergies, prix maximal, motifs et risques, modes de paiement, fourchette de négociation | `4.2.c` Analyser les opérations de fusions et d'acquisitions ; `4.2.b` Analyser les motifs des opérations de réorganisation ; `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers | 5 |
| **Total** | | **18** |

Part du calcul : environ 10,5 points (2.1-01 à 2.1-04, 2.2-01 à 2.2-03, 2.3-01 à 2.3-04, 2.4-01 et 2.4-02, 2.5-01 à 2.5-03, 2.7-01, 2.7-02 et 2.7-04). Part de l'analyse : environ 7,5 points. Les montants d'ONDAVÈRE de l'annexe 2.6 sont les montants 2026 communs du sujet ; aucun résultat d'un autre dossier n'est utilisé, et le rachat n'est supposé fait dans aucun autre dossier.

---

### 2.1 Bêtas des comparables, coût des fonds propres, prime de taille et d'illiquidité, CMPC (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Bêtas désendettés **1,0000 ; 0,8000 ; 0,6000** ; moyenne **0,8000** | 0,5 |
| 2.1-02 | D / CP cible = 20 / 80 = **25 %** ; bêta des fonds propres 0,80 × (1 + 0,75 × 0,25) = **0,9500** | 0,5 |
| 2.1-03 | MEDAF 4,00 % + 0,95 × 5,00 % = **8,75 %** ; avec la prime : **10,50 %** | 0,5 |
| 2.1-04 | Coût de la dette après impôt **3,90 %** ; **CMPC = 10,50 % × 80 % + 3,90 % × 20 % = 9,18 %** | 0,5 |
| 2.1-05 | Pourquoi une prime s'ajoute au MEDAF pour une petite société non cotée, reliée au cas | 0,5 |

**Bêtas désendettés (formule de l'annexe 2.3, D / CP de chaque comparable).**

| Comparable | Bêta endetté | D / CP | 1 + 0,75 × D / CP | Bêta désendetté |
|---|---:|---:|---:|---:|
| MIRALPE Loisirs | 1,30 | 40 % | 1,30 | **1,0000** |
| HOSTELVAN Hôtels | 1,16 | 60 % | 1,45 | **0,8000** |
| CLIVANDRE Santé | 0,96 | 80 % | 1,60 | **0,6000** |
| **Moyenne** | | | | **0,8000** |

- **Structure cible** : la dette financière nette représente 20 % de la VGE, les capitaux propres 80 % ; D / CP = 20 / 80 = **25 %**.
- **Bêta des fonds propres de Salvèze** : 0,80 × [1 + (1 − 25 %) × 25 %] = 0,80 × 1,1875 = **0,9500**.
- **Coût des fonds propres** : MEDAF 4,00 % + 0,95 × 5,00 % = **8,75 %** ; avec la prime de taille et d'illiquidité : 8,75 % + 1,75 % = **10,50 %**.
- **Coût de la dette après impôt** : 5,20 % × (1 − 25 %) = **3,90 %**.
- **CMPC** = 10,50 % × 80 % + 3,90 % × 20 % = 8,40 % + 0,78 % = **9,18 %**.

Désendetter puis réendetter isole le risque d'exploitation des comparables (bêta de l'actif) de leur endettement, très différent d'une société à l'autre (40 % à 80 %), puis applique à ce risque la structure financière de la station. La moyenne des bêtas endettés (1,1400), prise sans désendettement, mêlerait les deux risques.

**Pourquoi une prime s'ajoute au MEDAF (0,5 pt).**
- **Principe** : plus un placement est incertain, plus la rentabilité exigée est élevée. Le MEDAF (Sharpe, 1964) ne rémunère que le risque systématique, mesuré par le bêta, parce qu'il suppose des investisseurs diversifiés qui peuvent acheter et vendre le titre à tout moment.
- **Illiquidité** : les actions des Thermes de Salvèze ne sont pas cotées. Leur détenteur ne peut les vendre qu'en cherchant un acquéreur, comme le font aujourd'hui les héritiers, avec un délai et un prix incertains. La prime rémunère ce coût de sortie.
- **Taille** : une seule station de 23,80 M€ de chiffre d'affaires dépend de deux forages, d'un seul site, de quelques dirigeants (Mme Élise MERCORAZ) et pèse peu face à ses fournisseurs. Les bêtas viennent de sociétés cotées plus grandes, qui diversifient ces risques sur plusieurs sites. Fama et French (1993) ont relevé que les petites sociétés ont une rentabilité supérieure à celle que leur bêta explique : la prime de taille a un fondement, mais son niveau (1,75 %) reste une hypothèse du cabinet, sans mesure.
- **Effet** : la prime porte le coût des fonds propres de 8,75 % à 10,50 % et le CMPC de 7,78 % à 9,18 %.

**Réponses tolérées** : prime ajoutée au CMPC plutôt qu'au coût des fonds propres si le candidat le signale (CMPC de 9,53 %, résultats suivants notés en cohérence) ; pondérations écrites 0,80 et 0,20 sans calcul du D / CP, à condition que le bêta soit réendetté avec 25 % ; mention du modèle de Fama et French sans calcul.

**Erreurs fréquentes**
- Réendetter avec D / (CP + D) = 20 % (bêta de 0,92) au lieu de D / CP = 25 %.
- Faire la moyenne des bêtas endettés (1,14) ou prendre le bêta d'un seul comparable.
- Réendetter avec la structure d'un comparable au lieu de la structure cible de Salvèze, ou pondérer le CMPC par les montants du bilan (12,40 et 6,00).
- `JUR-E02` — démarche du coût du capital d'une société non cotée par comparables mal conduite ; `JUR-T14` — rôle de la diversification dans le MEDAF ignoré.

**Références** : F02 § 3 (formule de Hamada avec impôt) et § 5 (CMPC) [S ; V sujet 2025 pour la démarche] ; programme 3.1.a « rentabilité exigée par le MEDAF, avec primes complémentaires (prime de liquidité, prime de taille) à partir de données fournies » [V guide p. 64] ; F10 Sharpe (1964), Fama et French (1993) [V programme 5.2] ; F11 pour le taux sans risque et la prime de marché, posés comme hypothèses d'énoncé.

---

### 2.2 Flux de trésorerie disponibles tirés du business plan fourni (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Résultat d'exploitation (**3,72 ; 3,88 ; 4,04 ; 4,16 ; 4,28**), impôt de 25 % (0,93 à 1,07), résultat d'exploitation après impôt (2,79 à 3,21) | 0,5 |
| 2.2-02 | BFR du 31/12/2026 = 0,30 + 1,90 − 0,55 − 0,45 = **1,20** ; variations **0,04** chaque année (emplois) | 0,5 |
| 2.2-03 | Flux de trésorerie disponibles **1,95 ; 2,13 ; 2,63 ; 2,70 ; 2,97** (somme 12,38), présentés en tableau | 0,5 |

**Flux de trésorerie disponibles (M€)**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| EBITDA | 5,62 | 5,84 | 6,08 | 6,28 | 6,48 |
| − Dotations aux amortissements | − 1,90 | − 1,96 | − 2,04 | − 2,12 | − 2,20 |
| **Résultat d'exploitation** | **3,72** | **3,88** | **4,04** | **4,16** | **4,28** |
| − Impôt sur le résultat d'exploitation (25 %) | − 0,93 | − 0,97 | − 1,01 | − 1,04 | − 1,07 |
| **Résultat d'exploitation après impôt** | **2,79** | **2,91** | **3,03** | **3,12** | **3,21** |
| + Dotations aux amortissements | + 1,90 | + 1,96 | + 2,04 | + 2,12 | + 2,20 |
| BFR de fin d'année | 1,24 | 1,28 | 1,32 | 1,36 | 1,40 |
| − Variation du BFR | − 0,04 | − 0,04 | − 0,04 | − 0,04 | − 0,04 |
| − Investissements | − 2,70 | − 2,70 | − 2,40 | − 2,50 | − 2,40 |
| **Flux de trésorerie disponible** | **1,95** | **2,13** | **2,63** | **2,70** | **2,97** |

- **BFR du 31 décembre 2026** (annexe 2.5) : 0,30 + 1,90 − 0,55 − 0,45 = **1,20 M€**. Variation de 2027 : 1,24 − 1,20 = **0,04**, un emploi qui réduit le flux ; de même les années suivantes.
- **Flux de 2027** : 3,72 − 0,93 + 1,90 − 0,04 − 2,70 = **1,95 M€**. Présentation équivalente : EBITDA − impôt sur le résultat d'exploitation − variation du BFR − investissements = 5,62 − 0,93 − 0,04 − 2,70 = 1,95.
- Les flux sont **avant frais financiers** : l'impôt est calculé sur le résultat d'exploitation, comme si la société n'était pas endettée ; l'économie d'impôt sur les intérêts est prise en compte dans le CMPC.
- Le business plan est fourni : le candidat n'a ni à le reconstruire ni à le discuter ici (il le discute à la question 2.3). Les flux progressent avec la fin de la rénovation des cabines de soins (2,70 M€ d'investissements en 2027 et 2028, puis 2,40 à 2,50).

**Réponses tolérées** : présentation partant de l'EBITDA ; impôt arrondi présenté avec trois décimales (0,930…) sans effet sur les flux.

**Erreurs fréquentes**
- Retrancher le niveau du BFR (1,24) au lieu de sa variation (flux de 2027 à 0,75 au lieu de 1,95) (`JUR-E01`).
- Calculer l'impôt sur l'EBITDA (1,41 en 2027), ou déduire des intérêts des flux (`JUR-E01`).
- Oublier le BFR du 31 décembre 2026, ou le prendre égal à celui de 2027.
- `JUR-T07` — flux non présentés en tableau.

**Références** : F03 § 2.1 (FTD = REX × (1 − t) + dotations − variation du BFR − investissements) [V corrigé 2023 ; guide p. 64 ; S] ; programme 3.1.b « flux prévisionnels fournis ou hypothèses du business plan » [V guide p. 64].

---

### 2.3 Valeur terminale avec et sans croissance, VGE et VCP, poids de la valeur terminale (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Flux actualisés à 9,18 % : 1,79 ; 1,79 ; 2,02 ; 1,90 ; 1,91, somme **9,41** | 0,5 |
| 2.3-02 | Avec croissance : valeur terminale 2,97 × 1,015 / (0,0918 − 0,015) = **39,25** ; actualisée **25,30** ; VGE **34,71** | 0,5 |
| 2.3-03 | Sans croissance : valeur terminale 2,97 / 0,0918 = **32,35** ; actualisée **20,85** ; VGE **30,26** | 0,5 |
| 2.3-04 | Dette financière nette = 7,20 − 1,20 = **6,00** ; VCP **28,71** avec croissance et **24,26** sans croissance ; le prix de 100 % des actions se compare à la VCP | 0,5 |
| 2.3-05 | Commentaire : écart de 4,45 M€ (+ 18,34 %), poids de la valeur terminale (72,89 % et 68,90 %), business plan établi par les cédants | 1 |

**Actualisation (annexe 2.7 : évaluation au 31 décembre 2026, flux en fin d'année, CMPC de 9,18 %).**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Flux de trésorerie disponible | 1,95 | 2,13 | 2,63 | 2,70 | 2,97 |
| Facteur 1 / 1,0918^n | 0,915919 | 0,838907 | 0,768371 | 0,703765 | 0,644591 |
| Flux actualisé | 1,79 | 1,79 | 2,02 | 1,90 | 1,91 |

Somme des flux actualisés : **9,41 M€**.

| M€ | Avec croissance de 1,50 % | Sans croissance |
|---|---:|---:|
| Valeur terminale à la fin de 2031 | 2,97 × 1,015 / 0,0768 = **39,25** | 2,97 / 0,0918 = **32,35** |
| Valeur terminale actualisée (× 0,644591) | **25,30** | **20,85** |
| Somme des flux actualisés | 9,41 | 9,41 |
| **VGE** | **34,71** | **30,26** |
| − Dette financière nette au 31/12/2026 | − 6,00 | − 6,00 |
| **VCP** | **28,71** | **24,26** |
| Poids de la valeur terminale dans la VGE | 72,89 % | 68,90 % |
| VGE / EBITDA de 2026 | 6,43 | 5,60 |

**Passage de la VGE à la VCP (0,5 pt avec la dette).** Les flux de trésorerie disponibles reviennent à tous les apporteurs de capitaux : actualisés au CMPC, ils donnent la VGE, valeur de l'actif économique. Les héritiers vendent des actions et l'acquéreur reprend la dette financière nette (7,20 − 1,20 = **6,00 M€**) : le prix se compare à la VCP, VGE − dette financière nette.

**Commentaire (1 pt).**
- **Écart** : la croissance de 1,50 % ajoute **4,45 M€** à la VCP (28,71 contre 24,26, soit + 18,34 %). Elle ne joue que sur la valeur terminale (39,25 contre 32,35 avant actualisation) : la valeur est très sensible à l'écart entre le CMPC et le taux de croissance, qui figure au dénominateur (7,68 points contre 9,18).
- **Poids de la valeur terminale** : **72,89 %** de la VGE avec croissance, **68,90 %** sans croissance. Près des trois quarts de la valeur reposent sur des flux postérieurs à 2031, donc sur la capacité de la station à durer : débit de la source, étés plus chauds, enneigement, état des bâtiments.
- **Origine du business plan** : le plan est établi par le conseil des cédants, qui ont intérêt à un prix élevé. La marge d'EBITDA passe de 22,69 % en 2026 à 24,00 % en 2031, le chiffre d'affaires croît d'environ 2,6 % par an, la fréquentation monte à 9 400 curistes, et le plan ne prévoit **aucune annulation liée à la chaleur**, alors que 160 cures ont été annulées en août 2026 et que le débit d'été du forage principal baisse. Le flux de 2031, base de la valeur terminale, est donc plutôt haut. L'acquéreur doit revoir ces hypothèses avec ses propres données (ses stations de Savoie) et retenir la valeur sans croissance comme lecture prudente.
- **Cohérence du flux normatif** : en 2031, les investissements (2,40) dépassent à peine les dotations (2,20) ; une croissance perpétuelle de 1,50 % suppose de continuer à investir, ce qui est cohérent. Sans croissance, le flux de 2031 garde une hausse du BFR (0,04) et des investissements supérieurs aux dotations (0,20), dont une station de taille constante n'aurait plus besoin : la valeur sans croissance est une lecture prudente, un peu basse.
- **Conclusion** : la station seule vaut entre **24,26 et 28,71 M€** pour 100 % des actions, soit 5,60 à 6,43 fois l'EBITDA de 2026, loin des 37,50 M€ demandés.

**Réponses tolérées** : valeur terminale actualisée en divisant par 1,0918^5 = 1,551370 (mêmes résultats) ; flux actualisés non arrondis (somme de 9,41 et mêmes VGE de 34,71 et 30,26) ; valeur terminale sans croissance calculée avec un flux de 2031 où les investissements sont ramenés au niveau des dotations et la variation du BFR est nulle, si l'hypothèse est écrite et justifiée.

**Erreurs fréquentes**
- Actualiser au coût des fonds propres (10,50 %) des flux qui reviennent à tous les apporteurs (`JUR-E01`).
- Oublier d'actualiser la valeur terminale, l'actualiser sur six ans, ou omettre le facteur (1 + g) dans le calcul avec croissance.
- Comparer le prix demandé à la VGE, ou retrancher la dette brute (7,20) au lieu de la dette nette.
- `JUR-T12` — commentaire du poids de la valeur terminale sans chiffre ; `JUR-T13` — origine du business plan ignorée.

**Références** : F03 § 2.2 (valeur terminale avec croissance FTD_n × (1 + g) / (CMPC − g), sans croissance FTD_n / CMPC ; commenter le poids de la valeur terminale dans la VGE) [V corrigé 2023 ; guide p. 64] ; F10 Gordon et Shapiro (1956) [V programme 3.1] ; programme 3.1.d « VCP = VGE − dette financière nette » [V guide p. 64].

---

### 2.4 Multiples de transactions et multiples boursiers, choix des inducteurs (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Transactions : VGE **41,04** (7,60 × 5,40) et **35,70** (1,50 × 23,80) ; VCP **35,04** et **29,70** | 0,5 |
| 2.4-02 | Sociétés cotées : VGE **34,56** (6,40 × 5,40) et **30,94** (1,30 × 23,80) ; VCP **28,56** et **24,94** | 0,5 |
| 2.4-03 | Écart entre les deux familles : prime de contrôle et synergies payées par les acquéreurs, cours de minoritaires liquides, date et cycle | 0,5 |
| 2.4-04 | Choix des inducteurs : l'EBITDA plutôt que le chiffre d'affaires (marge de 22,69 % contre 19,74 % et 20,31 % implicites), murs détenus ou loués | 0,5 |
| 2.4-05 | Conclusion : valeurs retenues et rapprochement avec la valeur par les flux | 0,5 |

| Multiple (M€) | Agrégat 2026 | Multiple | VGE | − Dette financière nette | VCP |
|---|---:|---:|---:|---:|---:|
| Transactions, VE / EBITDA | 5,40 | 7,60 | **41,04** | − 6,00 | **35,04** |
| Transactions, VE / chiffre d'affaires | 23,80 | 1,50 | **35,70** | − 6,00 | **29,70** |
| Sociétés cotées, VE / EBITDA | 5,40 | 6,40 | **34,56** | − 6,00 | **28,56** |
| Sociétés cotées, VE / chiffre d'affaires | 23,80 | 1,30 | **30,94** | − 6,00 | **24,94** |

Les quatre multiples sont des multiples de VGE (la VE comprend la dette) : ils s'appliquent à des agrégats d'avant frais financiers, et la VCP s'obtient en retranchant la dette financière nette.

**Écart entre les deux familles (0,5 pt).** Le multiple d'EBITDA des transactions dépasse de **18,75 %** celui des sociétés cotées (7,60 contre 6,40), soit 6,48 M€ de VCP.
- **Contrôle et synergies** : une transaction porte sur 100 % du capital, achetée par un exploitant du secteur qui prend le contrôle et attend des synergies ; le prix comprend une prime de contrôle et une partie de ces synergies, payée aux cédants. Le cours de bourse est le prix d'une petite quantité d'actions échangée entre minoritaires, sans contrôle.
- **Concurrence entre acquéreurs** : les stations à vendre sont rares ; quand deux exploitants sont en compétition, comme ici, le prix monte.
- **Liquidité et taille** : les sociétés cotées sont plus grandes et liquides ; les cibles des transactions sont des stations isolées, comme Salvèze. Les deux effets jouent en sens contraires : la prime de contrôle l'emporte.
- **Date** : les transactions s'étalent de 2024 à 2026, les cours datent de mars 2027, après deux étés chauds.

**Choix des inducteurs (0,5 pt).**
- **EBITDA plutôt que chiffre d'affaires** : un multiple de chiffre d'affaires ignore la rentabilité. Salvèze dégage une marge d'EBITDA de **22,69 %**, supérieure à celle que supposent les multiples (1,50 / 7,60 = **19,74 %** pour les transactions, 1,30 / 6,40 = **20,31 %** pour les sociétés cotées) : le chiffre d'affaires la sous-évalue (VCP de 29,70 contre 35,04). Il ne sert que de recoupement, ou pour une activité dont la marge n'est pas encore significative.
- **Murs détenus ou loués** : Salvèze est propriétaire de ses murs, donc ne paie pas de loyer. Les transactions portent sur des stations propriétaires de leurs murs : leur EBITDA est comparable. La plupart des sociétés cotées louent leurs murs : leur VE comprend leurs dettes locatives et leur EBITDA est calculé avant loyers, ce qui les rend comparables en principe, mais leurs dettes locatives sont estimées et leurs actifs sont différents (parcs, hôtels, cliniques).
- **Autres inducteurs** : le résultat d'exploitation dépend de l'âge des bâtiments et du rythme d'amortissement (thermes de 1952 rénovés par étapes) ; le résultat net, inducteur de VCP, dépend en plus de l'endettement de chaque société : ils sont moins adaptés ici.

**Conclusion (0,5 pt).** Les multiples d'EBITDA donnent une VCP de **28,56 M€** (sociétés cotées) à **35,04 M€** (transactions). Le multiple boursier recoupe la valeur par les flux (28,71 M€, soit 6,43 fois l'EBITDA) : les deux mesurent la station seule, pour un investisseur sans contrôle. Le multiple de transactions mesure ce que paient des acquéreurs du secteur, synergies comprises : c'est un repère de prix, pas une valeur de la station seule. Le prix demandé (37,50 M€, soit 43,50 M€ de VGE et **8,06 fois** l'EBITDA de 2026) dépasse même les transactions.

**Réponses tolérées** : multiples appliqués à l'EBITDA de 2027 du business plan si le candidat le justifie (le multiple est alors surestimé, puisqu'il a été calculé sur le dernier exercice réalisé) ; moyenne des quatre valeurs présentée comme une indication, à condition que le candidat explique pourquoi les multiples d'EBITDA pèsent davantage.

**Erreurs fréquentes**
- Présenter la VGE comme la valeur des actions, sans retrancher la dette financière nette.
- Appliquer un multiple de VGE au résultat net, ou retenir le multiple de chiffre d'affaires sans discuter la marge.
- Additionner ou moyenner des VGE et des VCP.
- `JUR-E03` — valeurs juxtaposées, sans les croiser avec la valeur par les flux.

**Références** : F03 § 3 (multiples de VGE et de VCP, cohérence de l'inducteur, prime de contrôle et décote d'illiquidité) [V corrigé 2023 ; sujet 2024 ; guide p. 64-65 ; S] ; programme 3.2.a « choix d'inducteurs adaptés au secteur, au modèle économique » [V guide p. 65].

---

### 2.5 Actif net comptable corrigé et portée de l'approche patrimoniale (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Plus-values sur les murs **4,60** et **5,20** (9,80) ; impôt latent **2,45** | 0,5 |
| 2.5-02 | **ANCC = 12,40 + 9,80 − 2,45 = 19,75 M€** | 0,5 |
| 2.5-03 | Si l'exploitation thermale cessait : écart net 1,80 (− 3,40 + 5,20), impôt latent 0,45, **ANCC = 13,75 M€** | 0,5 |
| 2.5-04 | Portée de l'approche : valeur des murs avec l'exploitation, plancher seulement au sens de 13,75, actif spécialisé ; écart avec les flux | 0,5 |

| Élément (M€) | Avec la poursuite de l'exploitation | Si l'exploitation thermale cessait |
|---|---:|---:|
| Capitaux propres comptables | 12,40 | 12,40 |
| Établissement thermal : valeur vénale − valeur comptable | 11,00 − 6,40 = + 4,60 | 3,00 − 6,40 = − 3,40 |
| Résidence hôtelière : 9,40 − 4,20 | + 5,20 | + 5,20 |
| − Impôt latent de 25 % sur les écarts | − 2,45 | − 0,45 |
| **ANCC** | **19,75** | **13,75** |

**Portée de l'approche patrimoniale (0,5 pt).**
- **Ce que mesure l'ANCC de 19,75 M€** : la valeur des actifs et des passifs, les murs à leur valeur vénale **avec la poursuite de l'exploitation**. Les murs pèsent 20,40 M€, soit 58,77 % de la VGE par les flux : la station est une activité à fort patrimoine, ce qui rend l'approche utile.
- **Pas un vrai plancher** : un établissement thermal est un actif spécialisé (bassins, réseau d'eau thermale, cabines). Sa valeur vénale de 11,00 M€ suppose qu'un exploitant continue d'y donner des soins : elle dépend elle-même de la rentabilité de l'exploitation. Si la source faiblit ou si l'exploitation cesse, le bâtiment ne vaut plus que 3,00 M€ et l'ANCC tombe à **13,75 M€**, avant les coûts de fermeture et de départ des salariés. Le plancher, pour les cédants, est plutôt cette valeur des murs sans l'exploitation, sur laquelle la résidence (9,40 M€, utilisable par un hôtelier) pèse l'essentiel.
- **Ce qu'elle ignore** : la VCP par les flux (28,71 M€) dépasse l'ANCC de 8,96 M€ (1,45 fois). Cet écart correspond à la capacité de l'exploitation à dégager une rentabilité supérieure à celle des actifs pris un à un : le droit d'exploiter la source, qui ne figure pas au bilan et ne se vend pas seul, la clientèle de curistes, l'équipe, la résidence qui travaille l'hiver. Ces éléments n'apparaissent que dans les flux.
- **Usage dans la négociation** : l'ANCC rassure l'acquéreur sur le patrimoine qui garantit le prix (les murs couvrent plus de la moitié de la VGE) ; il ne sert pas à fixer le prix d'une exploitation rentable.

**Réponses tolérées** : impôt latent présenté par bien (1,15 et 1,30) ; ANCC sans exploitation calculé sans l'économie d'impôt sur la moins-value (12,90 M€) si l'hypothèse est écrite, alors que l'annexe 2.5 prévoit qu'elle réduit l'impôt latent.

**Erreurs fréquentes**
- Ajouter la valeur vénale des murs aux capitaux propres sans retrancher leur valeur comptable.
- Oublier l'impôt latent, ou le calculer sur la valeur vénale totale.
- Ajouter une valeur au droit d'exploiter la source, que l'énoncé ne donne pas.
- `JUR-E03` — ANCC présenté comme la valeur de la station, sans le rapprocher des flux.

**Références** : F03 § 4 (ANCC, retraitements fournis, limites : valeur statique, ignore la rentabilité future) [V guide p. 65-66 ; S] ; programme 3.3.a « pertinence de l'approche selon l'activité, la situation financière, le cycle de vie » [V guide p. 66].

---

### 2.6 Risque spécifique et risque systématique : cédants et actionnaires d'ONDAVÈRE (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Distinction entre risque spécifique (diversifiable) et risque systématique, appliquée aux risques de Salvèze | 0,5 |
| 2.6-02 | Les héritiers supportent le risque total ; les actionnaires diversifiés d'ONDAVÈRE n'exigent la rémunération que du risque systématique | 0,5 |
| 2.6-03 | Ce que cela change à la négociation (valeur pour chaque partie, préférence pour le numéraire, ne pas payer la diversification) | 0,5 |

**Deux composantes du risque (0,5 pt).** Le risque total d'une action se décompose en un risque **systématique**, lié aux variations de l'ensemble de l'économie et des marchés, que la diversification ne supprime pas et que mesure le bêta (0,95 pour Salvèze), et un risque **spécifique**, propre à l'entreprise, que la diversification d'un portefeuille élimine (Markowitz, 1952).
- **Risques spécifiques de Salvèze** : baisse du débit du forage principal (− 8 % depuis 2021, forage de secours insuffisant en août) ; épisodes de chaleur locaux (160 cures annulées en août 2026) ; enneigement d'un hiver (occupation de 41 % en 2024-2025 contre 63 %) ; dépendance à la présidente. Ils touchent une seule station.
- **Risques systématiques** : dépenses de loisirs et de santé des ménages selon la conjoncture, taux d'intérêt, coûts de l'énergie.
- **Risque sectoriel** : une baisse de la prise en charge des cures toucherait toutes les stations à la fois. Ni ONDAVÈRE ni les héritiers ne peuvent s'en protéger en détenant plusieurs stations, mais un investisseur qui détient d'autres secteurs le dilue dans son portefeuille : au sens du MEDAF, c'est un risque spécifique au secteur, pas un risque systématique.

**Deux appréciations du risque (0,5 pt).**
- **Les héritiers** ont plus des trois quarts de leur patrimoine dans une seule station, et Mme Élise MERCORAZ y a aussi son emploi : ils supportent le **risque total**, spécifique compris. Ils exigent une rentabilité supérieure à celle du MEDAF, ou, ce qui revient au même, la station vaut moins pour eux que pour un investisseur diversifié. Vendre leur permet de transformer un actif risqué et illiquide en numéraire, qu'ils peuvent diversifier.
- **Les actionnaires d'ONDAVÈRE** (investisseurs institutionnels à 61 %, aucun au-delà de 8 %) détiennent de nombreux titres : le risque d'une station ne pèse presque rien dans leur portefeuille ; ils n'exigent que la rémunération du risque systématique. Le groupe lui-même réduit son propre risque total avec Salvèze (altitude moins exposée à la chaleur que les Pyrénées, résidence ouverte l'hiver), mais cette diversification ne crée pas de valeur pour des actionnaires qui peuvent diversifier eux-mêmes.
- **Illustration non exigée** : sans la prime de taille et d'illiquidité, le CMPC serait de 7,78 % et la VCP de la station de 36,78 M€ (somme des flux actualisés 9,78, valeur terminale 48,00, actualisée 33,00). L'écart avec 28,71 M€ montre le poids de la prime.

**Ce que cela change à la négociation (0,5 pt).**
- Le prix de réserve des héritiers est bas au regard de la valeur pour un acquéreur diversifié : il existe une zone d'accord, et ONDAVÈRE peut négocier un prix proche de la valeur de la station seule, augmenté d'une partie des synergies seulement.
- Les cédants préfèrent le numéraire (souhait du frère et de la sœur) : des actions ONDAVÈRE les laisseraient exposés au thermalisme et aux étés chauds, même avec six stations au lieu d'une. Un paiement en actions vaut donc moins pour eux que sa valeur au cours ; NÉRIDANE, qui offre du numéraire, a un argument.
- ONDAVÈRE ne doit pas payer aux cédants la baisse du taux d'actualisation que permet sa propre structure. La prime de 1,75 % a deux composantes. La part « taille » correspond, selon Fama et French (1993), à un facteur de risque commun que la diversification ne supprime pas, et la station reste petite dans le groupe. La part « illiquidité », elle, disparaît dans un groupe coté : c'est une valeur créée par ONDAVÈRE, qu'elle n'a pas à remettre aux héritiers. Garder la prime est aussi une marge de prudence, puisque les flux du business plan n'ont pas été corrigés de son optimisme. Payer 36,78 M€ reviendrait à remettre aux héritiers la valeur que crée la cotation d'ONDAVÈRE.

**Réponses tolérées** : toute illustration chiffrée cohérente (par exemple la part du prix dans la capitalisation d'ONDAVÈRE, 37,50 / 201,55 = 18,61 %) ; mention de la prime d'illiquidité comme rémunération du risque de ne pas pouvoir vendre ; candidat qui relève que, pour un acquéreur coté et diversifié, la prime d'illiquidité disparaît, et que le prix maximal serait plus élevé : accepté s'il conclut qu'ONDAVÈRE n'a pas à payer cet écart aux cédants.

**Erreurs fréquentes**
- Dire que le MEDAF rémunère le risque total, ou que la diversification supprime le risque systématique.
- Classer la chaleur parmi les seuls risques systématiques sans voir qu'un épisode local ne touche qu'une station.
- `JUR-T14` — théorie du portefeuille non mobilisée ; `JUR-T13` — risques cités sans lien avec Salvèze.

**Références** : F10 Markowitz (1952), Sharpe (1964), Fama et French (1993) [V programme 5.3 et 5.2] ; programme 5.3.a « distinction entre risque spécifique (diversifiable) et risque systématique » [V guide p. 75-76] ; programme 5.2.a « pourquoi un actif plus risqué exige une rentabilité plus élevée » [V guide p. 74-75].

---

### 2.7 Synergies, prix maximal, motifs et risques, modes de paiement, fourchette de négociation (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Flux nets des synergies (− 0,80 ; 0,50 ; 0,80 puis rente) ; valeur actuelle **6,99 M€** | 1 |
| 2.7-02 | **Prix maximal = 28,71 + 6,99 = 35,70 M€** ; le prix demandé le dépasse de **1,80 M€** ; prime demandée 8,79 M€, soit 125,75 % des synergies | 0,5 |
| 2.7-03 | Motifs et risques du rachat pour ONDAVÈRE, reliés au cas | 1 |
| 2.7-04 | Paiement B : titres **14,82 M€**, numéraire **22,68 M€**, **6,85 %** du capital ; DFN / EBITDA **2,08 → 2,88** (A) ou **2,51** (B) ; charges annuelles **1,35** (A) contre **0,82 + 0,48** (B) | 1 |
| 2.7-05 | Partage du risque et coût réel du paiement en actions (cédants, actionnaires d'ONDAVÈRE, signal) | 0,5 |
| 2.7-06 | Fourchette de négociation argumentée (33,00 à 35,70 M€) et mode de paiement recommandé | 1 |

**Valeur actuelle des synergies (1 pt).** Les synergies sont des flux après impôt ; elles s'actualisent au CMPC de 9,18 %, comme les flux de la station.

| M€ | 2027 | 2028 | 2029 et après |
|---|---:|---:|---:|
| Achats regroupés | 0,20 | 0,20 | 0,20 |
| Réservation commune | — | 0,30 | 0,30 |
| Offre de cures en Savoie | — | — | 0,30 |
| Coût de mise en œuvre | − 1,00 | — | — |
| **Flux net** | **− 0,80** | **0,50** | **0,80 par an** |
| Flux actualisé | − 0,73 | 0,42 | 0,61 (2029) |

- À partir de 2030, rente constante de 0,80 : valeur à la fin de 2029 = 0,80 / 0,0918 = **8,71 M€**, actualisée sur trois ans : 8,71 × 0,768371 = **6,69 M€**.
- Valeur actuelle des synergies = − 0,73 + 0,42 + 0,61 + 6,69 = **6,99 M€**.
- Présentation équivalente, synergie par synergie : achats 0,20 / 0,0918 = 2,18 ; réservation 0,30 / 0,0918 / 1,0918 = 2,99 ; cures 0,30 / 0,0918 / 1,0918² = 2,74 ; coût − 1,00 / 1,0918 = − 0,92 ; total **6,99**.

**Prix maximal et prix demandé (0,5 pt).**
- **Prix maximal** = VCP de la station seule + valeur des synergies = 28,71 + 6,99 = **35,70 M€** pour 100 % des actions (égalité fortuite avec la VGE par le multiple de chiffre d'affaires des transactions ; VGE de 41,70 M€, 7,72 fois l'EBITDA de 2026). À ce prix, ONDAVÈRE remet toutes les synergies aux cédants et ne crée aucune valeur pour ses actionnaires.
- **Prix demandé** : 37,50 M€ dépasse le prix maximal de **1,80 M€**. La prime demandée sur la station seule (37,50 − 28,71 = **8,79 M€**) représente **125,75 %** des synergies : les cédants demandent plus que toute la valeur que le rachat peut créer. Au CMPC retenu, payer ce prix détruirait 1,80 M€ de valeur pour les actionnaires d'ONDAVÈRE, même si toutes les synergies se réalisent.

**Motifs et risques du rachat (1 pt).**
- **Motifs** : croissance externe dans une région où le groupe est déjà présent (troisième station de Savoie, à moins d'une heure des deux autres) ; **synergies opérationnelles** de coûts (achats) et de revenus (réservation commune, offre de cures en Savoie) ; diversification de l'exposition à la chaleur (altitude) et des saisons (résidence d'hiver), qui stabilise les flux du groupe et sert ses prêteurs ; motif défensif : empêcher NÉRIDANE de s'installer en Savoie ; rachat d'une station en activité, plus rapide que la création d'un établissement thermal.
- **Risques** : payer trop cher dans une mise en concurrence (le gagnant est souvent celui qui a le plus surestimé la cible) ; business plan des cédants optimiste (aucune annulation liée à la chaleur) ; asymétrie d'information sur l'état de la source et des bâtiments (Akerlof, 1970), que l'acquéreur doit réduire par des vérifications avant de s'engager ; synergies de revenus incertaines et tardives (l'offre de cures en Savoie dépend des places disponibles et ne joue qu'en 2029) ; dépendance à Mme Élise MERCORAZ pendant la transition ; financement : la dette du groupe augmente au moment où il doit rénover plusieurs établissements thermaux.

**Les deux modes de paiement, sur la base du prix demandé (1 pt).**

| M€ | Paiement A, numéraire | Paiement B, en partie en actions |
|---|---:|---:|
| Actions nouvelles remises | — | 600 000 × 24,70 € = **14,82** |
| Numéraire tiré sur la ligne de crédit | **37,50** | 37,50 − 14,82 = **22,68** |
| Part du capital d'ONDAVÈRE remise aux cédants | — | 600 000 / 8 760 000 = **6,85 %** (2,28 % par héritier) |
| Dette financière nette du groupe pro forma (71,80 + numéraire + 6,00) | 115,30 | 100,48 |
| DFN / EBITDA pro forma (EBITDA 34,60 + 5,40 = 40,00) ; avant le rachat : 71,80 / 34,60 = 2,08 | **2,88** | **2,51** |
| Intérêts du tirage après IS (4,80 % × 75 %) | **1,35** | **0,82** |
| Dividendes des actions nouvelles (0,80 € par action) | — | **0,48** |

- Les actions remises représentent 39,52 % du prix. Le paiement B limite la hausse de l'endettement : le ratio passe de 2,08 à 2,51 au lieu de 2,88, ce qui laisse de la capacité d'emprunt pour la rénovation des thermes.
- Les charges annuelles décaissées sont proches (1,35 contre 1,30) ; mais les dividendes ne sont pas déductibles et le coût réel du paiement en actions n'est pas le dividende : c'est la part de 6,85 % de la valeur future du groupe, synergies comprises, cédée aux héritiers.

**Partage du risque (0,5 pt).**
- **Pour les cédants**, recevoir des actions, c'est rester exposés au thermalisme : ils échangent le risque d'une station contre celui de six, mieux diversifié mais toujours sensible aux étés chauds, et ils ne peuvent pas vendre pendant deux ans. En contrepartie, ils participent aux synergies : si le rachat réussit, le cours en profite. Mme Élise MERCORAZ, qui reste deux ans à la tête de la station, est intéressée à la réussite de l'intégration.
- **Pour les actionnaires d'ONDAVÈRE**, le paiement en actions partage avec les cédants le risque de surpayer : si les synergies déçoivent, le cours baisse et les héritiers en supportent 6,85 %. Il dilue leur part (93,15 % du capital après l'opération) ; les héritiers, ensemble, deviendraient un actionnaire de premier plan, aucun institutionnel ne dépassant 7,45 % après l'émission.
- **Signal** : payer en actions quand la direction juge le cours bas (24,70 € après deux étés chauds) coûte cher aux actionnaires actuels ; inversement, le marché peut lire un paiement en actions comme le signe que la direction juge ses actions chères (Myers et Majluf, 1984). Le paiement en numéraire signale au contraire la confiance dans la valeur de la cible et dans la capacité d'endettement du groupe.

**Fourchette de négociation et mode de paiement (1 pt).**
- **Borne basse : environ 33,00 M€**, le prix évoqué par NÉRIDANE. En dessous, les héritiers vendent au concurrent. Ce prix est déjà au-dessus de la valeur de la station seule (28,71 M€, 24,26 sans croissance) et de la VCP par le multiple boursier (28,56) ; il correspond à 7,22 fois l'EBITDA de 2026, sous la médiane des transactions (7,60).
- **Borne haute : 35,70 M€**, le prix maximal, à ne pas dépasser. Il suppose que toutes les synergies se réalisent dans les délais ; il est proche de la VCP par le multiple de transactions (35,04), qui intègre déjà les synergies payées par d'autres acquéreurs.
- **Proposition** : ouvrir vers **33,50 à 34,00 M€** (création de valeur pour ONDAVÈRE de 2,20 à 1,70 M€), en appuyant le prix sur les faiblesses du business plan (chaleur, source, marge qui progresse sans justification) et sur l'écart entre la valeur des actions pour les héritiers et leur valeur pour ONDAVÈRE. Si la concurrence l'impose, monter vers 35,00 M€ en réservant la hausse à la part payée en actions, ce qui fait porter aux cédants une partie du risque des synergies.
- **Mode de paiement** : un paiement mixte, avec une part en actions plus faible que les 600 000 prévues si le frère et la sœur préfèrent le numéraire, et éventuellement réservée à Mme Élise MERCORAZ, qui reste dans l'entreprise. Il limite l'endettement du groupe (2,51 fois l'EBITDA au lieu de 2,88) avant le programme de rénovation, et aligne la présidente de la station sur la réussite du rachat. Un paiement tout en numéraire reste possible si le conseil juge le cours de 24,70 € trop bas pour émettre des actions.

**Conclusion attendue.** La station seule vaut environ 28,71 M€ pour 100 % des actions, 35,70 M€ avec toutes les synergies ; le prix demandé de 37,50 M€ est trop élevé. ONDAVÈRE peut proposer entre 33,00 et 35,70 M€, de préférence en partie en actions, et doit renoncer si les cédants maintiennent un prix supérieur au prix maximal.

**Réponses tolérées** : valeur des synergies de 7,00 M€ (flux actualisés non arrondis) ; fourchette différente si elle est justifiée par les valeurs calculées (par exemple une borne basse à 29,70 ou 30,00 M€ si le candidat estime l'offre de NÉRIDANE peu crédible) ; recommandation d'un paiement tout en numéraire argumentée par les préférences des cédants et le signal ; synergies actualisées à un taux plus élevé que le CMPC pour l'offre de cures, si l'hypothèse est écrite ; candidat qui relève que, pour un acquéreur coté et diversifié, la prime d'illiquidité disparaît, et que le prix maximal serait plus élevé : accepté s'il conclut qu'ONDAVÈRE n'a pas à payer cet écart aux cédants.

**Erreurs fréquentes**
- Ajouter les synergies avant le coût de mise en œuvre, oublier leur décalage dans le temps (valeur de 8,71 M€ prise comme valeur actuelle), ou les actualiser sans tenir compte de leur date de départ.
- Comparer le prix maximal à la VGE, ou ajouter les synergies à la VGE puis la comparer au prix des actions sans retrancher la dette.
- Calculer un rapport d'échange entre les actions des deux sociétés : les actions ONDAVÈRE sont un moyen de paiement d'une partie du prix, valorisées au cours donné.
- Juger le paiement en actions « gratuit » parce qu'il ne coûte qu'un dividende de 0,48 M€.
- `JUR-E03` — fourchette sans croiser les valeurs obtenues ; `JUR-M01` — asymétrie d'information et signal non mobilisés ; `JUR-T01` — conseil non adressé à la direction d'ONDAVÈRE.

**Références** : F05 § 5 (logique économique d'un rapprochement : création de valeur si les synergies dépassent la prime payée) [V guide p. 69-70 ; S] ; programme 4.2.b « motifs économiques et financiers : synergies opérationnelles ou financières, croissance externe » et 4.2.c « création ou destruction de valeur, synergies, prime payée » [V guide p. 69-70] ; F10 Akerlof (1970), Myers et Majluf (1984) [V programme 5.1 et 7.2].
