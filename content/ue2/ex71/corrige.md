# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 71 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F06 marchés financiers, finance comportementale et fintech, F10 auteurs et théories, F11 données de marché, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (équilibre du bilan et compositions de la VSB et des CPNE ; ANCC, impôt latent, rentes du goodwill, goodwill, valeur patrimoniale par action ; coûts des fonds propres et rentabilités exigées de l'action et du portefeuille ; valeurs de rendement avec et sans croissance ; multiples de l'échantillon, médiane, VGE et VCP ; décomposition du risque de l'action FERVANNE ; rentabilité espérée, bêta, variance et écart-type de la poche de revenus et du portefeuille, décomposition de son risque ; barème, liste noire, hors-programme ; décote d'illiquidité, valeurs du bloc de la famille, fourchette, frais et rentabilités nettes vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un ANCC erroné à la question 2.1, repris dans la valeur patrimoniale de la question 2.2 et dans la comparaison des valeurs de la question 2.4, ou un bêta du portefeuille erroné à la question 2.6, repris dans les rentabilités nettes de la question 2.7).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Actif net comptable corrigé, impôt latent, valeur par action, portée et limites | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine | 2,5 |
| 2.2 ANCC, VSB et CPNE ; rente du goodwill sur les CPNE, goodwill, valeur patrimoniale ; nature du goodwill | `3.3.b` Savoir calculer la survaleur de l'entreprise à partir de ses actifs intangibles (goodwill) | 3 |
| 2.3 Rentabilité exigée et valeur de rendement avec et sans croissance | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance | 1,5 |
| 2.4 Multiples de l'échantillon, sociétés atypiques, médiane, décote, choix de l'inducteur, fourchette de négociation | `3.2.b` Savoir déterminer le multiple d'un échantillon pour valoriser l'entreprise ; `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP | 2 |
| 2.5 Risque systématique et risque spécifique de l'action FERVANNE ; risque non rémunéré d'un patrimoine concentré | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 2 |
| 2.6 Portefeuille de trois fonds en deux poches : rentabilité, bêta, écart-type, diversification, MEDAF, risque avant et après la cession | `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) ; `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 3 |
| 2.7 Frais et rentabilités nettes ; conseil automatisé ou gérant dédié ; nouveaux acteurs ; recommandation | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs | 3 |
| **Total** | | **17** |

Part du calcul : environ 9 points (2.1-01, 2.1-02, 2.2-02 à 2.2-04, 2.3-01, 2.3-02, 2.4-01, 2.4-02, 2.5-01, 2.6-01, 2.6-02, 2.6-04, 2.6-05, 2.7-01). Part de l'analyse : environ 8 points. Répartition par sous-partie du programme : 3.3 = 5,5 points (3.3.a = 2,5 ; 3.3.b = 3), 3.2 = 2 points (3.2.b = 1,5 ; 3.2.a = 0,5), 3.1 = 1,5 point, 5.3 = 3,5 points (5.3.a = 1,5 avec 2.5-01 et 2.5-02 ; 5.3.b = 1 avec 2.6-03 et 2.6-05 ; 5.3.c = 1 avec 2.6-01 et 2.6-02), 5.2 = 1,5 point (5.2.c : 2.5-03, 2.6-04, 2.6-06), 5.4 = 3 points (5.4.a = 1,5 ; 5.4.b = 1,5). Les questions 2.1 à 2.4 forment l'évaluation ; les questions 2.5 à 2.7 se traitent indépendamment d'elles, et la question 2.7, en grande partie rédactionnelle, vaut autant de points que la question 2.6 : elle ne doit pas être sacrifiée faute de temps (`JUR-T15`).

Frontière du programme. Le calcul de la VSB et des CPNE par le candidat est exclu (programme 3.3.b) : l'annexe 2.2 les fournit, et la question 2.2 demande seulement d'expliquer ce qui les distingue. L'écart-type d'un portefeuille est étudié au programme sur deux titres (5.3.c) : celui des trois fonds se calcule en deux étapes de deux composantes (la poche de revenus, puis le fonds A et la poche), avec les deux corrélations fournies.

---

### 2.1 Actif net comptable corrigé (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Retraitements bruts : bâtiments 17,00 − 14,20 = **+ 2,80** ; machines 28,20 − 24,60 = **+ 3,60** ; brevets et dessins **+ 2,80** ; stock de prêt **− 1,20** ; complément de provision **− 0,80** ; terrain 1,30 − 0,50 = **+ 0,80** ; placements : aucun ; total **+ 8,00 M€** ; impôt latent 25 % × 8,00 = **2,00 M€** (la moins-value et la provision le réduisent) | 1 |
| 2.1-02 | ANCC = 68,00 + 8,00 − 2,00 = **74,00 M€** ; par action 74,00 M€ / 1 600 000 = **46,25 €** | 0,5 |
| 2.1-03 | L'ANCC mesure le patrimoine réévalué revenant aux actionnaires, actifs hors exploitation compris (terrain 1,30 M€, placements 3,00 M€) : c'est un plancher de négociation pour la famille ; limites : valeur statique, sans la rentabilité future, sans le savoir-faire, la qualification des ancillaires et la relation avec les clients ; dépend des estimations du cabinet extérieur et de la convention d'impôt latent | 1 |

**Retraitements et impôt latent (1 pt).** On part des capitaux propres consolidés, qui sont l'actif net comptable du groupe (aucun actif fictif à éliminer en normes internationales ; les droits d'utilisation et les dettes locatives y sont déjà inscrits).

| Élément | Valeur retenue | Valeur comptable | Retraitement brut | Impôt latent (25 %) |
|---|---:|---:|---:|---:|
| Bâtiments de l'usine de Vesoul | 17,00 | 14,20 | + 2,80 | − 0,70 |
| Machines d'usinage et de polissage | 28,20 | 24,60 | + 3,60 | − 0,90 |
| Brevets et dessins (non inscrits) | 2,80 | 0,00 | + 2,80 | − 0,70 |
| Stock d'instruments prêtés aux hôpitaux | | | − 1,20 | + 0,30 |
| Complément de provision pour indemnités de départ | | | − 0,80 | + 0,20 |
| Terrain non utilisé | 1,30 | 0,50 | + 0,80 | − 0,20 |
| Placements de trésorerie (déjà à leur valeur liquidative) | | | 0,00 | 0,00 |
| **Total** | | | **+ 8,00** | **− 2,00** |

**ANCC et valeur par action (0,5 pt).** ANCC = 68,00 + 8,00 − 2,00 = **74,00 M€**, soit 74 000 000 / 1 600 000 = **46,25 € par action**. Pour information (non exigé), les 640 000 actions de la famille vaudraient 29,60 M€ sur cette base.

**Portée et limites (1 pt).** L'ANCC répond à la question « que vaut ce que possède la société, une fois ses dettes payées ? ». Il comprend des actifs dont l'exploitation n'a pas besoin, le terrain voisin (1,30 M€) et les placements de trésorerie (3,00 M€), qui appartiennent à tous les actionnaires : la famille peut légitimement demander qu'ils soient comptés dans le prix, ou qu'ils soient distribués avant la cession. Pour une entreprise industrielle rentable comme FERVANNE, l'ANCC est un **plancher** : il ignore la capacité bénéficiaire (le bénéfice économique de 2027, 9,60 M€, représente 11,29 % des CPNE de 85,00 M€, quand une rémunération normale serait de 6 %), et il ne valorise ni la formation des polisseurs (environ trois ans, annexe 2.3), ni la qualification des ancillaires chez les fabricants d'implants, ni les relations avec les hôpitaux : ces éléments font le goodwill (question 2.2). Il dépend aussi des estimations du cabinet extérieur (valeur d'usage des machines, valeur des brevets) et de la convention d'impôt latent : sans cession des actifs envisagée, l'impôt sur les plus-values n'est jamais payé, et un acquéreur pourrait discuter sa déduction (ANCC sans impôt latent : 76,00 M€). L'approche patrimoniale convient surtout aux sociétés de patrimoine et aux entreprises en difficulté ; ici, elle sert de référence basse (`JUR-E03`).

**Réponses tolérées** : présentation en partant de l'actif réévalué moins les dettes, si elle conduit à 74,00 M€ ; impôt latent calculé ligne à ligne ; commentaire qui présente l'ANCC comme une « valeur de liquidation » s'il précise que les actifs sont évalués en valeur d'usage, donc dans l'hypothèse de la poursuite de l'activité (accordé à moitié sur 2.1-03).

**Erreurs fréquentes**
- Oublier l'impôt latent (ANCC 76,00 M€, 47,50 € par action) ou l'appliquer aux seules plus-values (ANCC 73,50 M€).
- Ajouter une seconde fois les placements de trésorerie, déjà compris dans les capitaux propres.
- Déduire la dette financière nette de l'ANCC (64,50 M€) : les dettes sont déjà retranchées dans les capitaux propres.
- `JUR-T13` — limites de l'ANCC récitées sans lien avec le savoir-faire et les qualifications de FERVANNE.

**Références** : F03 § 4 (ANC, ANCC, retraitements fournis, impôt latent selon la convention de l'énoncé) [V programme 3.3.a ; guide p. 65-66 ; S manuels] ; F03 § 8 (rôle de chaque méthode dans une fourchette) [V guide p. 66].

---

### 2.2 VSB, CPNE et rente du goodwill (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | ANCC : patrimoine net, toutes dettes déduites, hors exploitation compris ; VSB (119,00) : valeur brute de tout l'outil d'exploitation, possédé ou non (biens loués non inscrits, outillages mis à disposition par les clients), sans déduction des dettes ; CPNE (85,00) : capitaux à financer durablement pour exploiter (immobilisations d'exploitation et BFR normatif, hors exploitation exclu) ; la rente compare le bénéfice d'exploitation après impôt, qui rémunère actionnaires et prêteurs, à la rémunération normale de ces capitaux : base et bénéfice sont associés | 0,5 |
| 2.2-02 | Rémunération normale 6 % × 85,00 = **5,10** ; rentes **4,50 ; 4,80 ; 5,10 ; 5,40 ; 5,70** | 0,5 |
| 2.2-03 | Goodwill = 4,50 / 1,10 + 4,80 / 1,10² + 5,10 / 1,10³ + 5,40 / 1,10⁴ + 5,70 / 1,10⁵ = 4,09 + 3,97 + 3,83 + 3,69 + 3,54 = **19,12 M€** | 0,5 |
| 2.2-04 | Valeur des capitaux propres = 74,00 + 19,12 = **93,12 M€** ; **58,20 € par action** | 0,5 |
| 2.2-05 | Le goodwill est un superprofit (11,29 % sur les CPNE contre 6 %) dû au savoir-faire, à la qualification des ancillaires, aux brevets et aux relations clients ; il repose en grande partie sur des compétences que détiennent les salariés, dont les cadres acheteurs : il est fragile (départs, rotation) et sa propriété est discutée dans la négociation (les cadres ne veulent pas payer la valeur qu'ils produisent, la famille fait valoir qu'il est attaché à l'entreprise) ; durée courte de la rente, lecture partenariale, asymétrie d'information | 1 |

**ANCC, VSB et CPNE (0,5 pt).** Les trois montants mesurent des choses différentes.
- L'**ANCC** (74,00 M€) est un patrimoine **net** : actifs réévalués moins toutes les dettes, y compris les actifs hors exploitation. Il revient aux actionnaires.
- La **VSB** (119,00 M€) mesure l'outil de travail **brut** : tous les biens utilisés par l'exploitation, en valeur d'usage, qu'ils appartiennent ou non à l'entreprise (matériels loués non inscrits, 1,40 M€ ; outillages mis à disposition par les clients, 3,00 M€), sans déduire aucune dette, ni financière ni d'exploitation, et hors actifs non utilisés. Elle est indépendante de la façon dont l'outil est financé.
- Les **CPNE** (85,00 M€) sont les capitaux qu'il faut financer durablement, par les fonds propres et par la dette, pour exploiter : immobilisations d'exploitation en valeur d'usage (60,20 M€) et besoin en fonds de roulement normatif (24,80 M€), c'est-à-dire après déduction du crédit des fournisseurs et des autres dettes d'exploitation.

La rente compare un bénéfice à la rémunération normale des capitaux qui l'ont produit : la base et le bénéfice doivent être **associés**. Le bénéfice économique de l'annexe 2.3, résultat d'exploitation après impôt, rémunère ensemble les actionnaires et les prêteurs qui financent les CPNE : il s'associe naturellement aux CPNE. La VSB comprend des actifs financés par les fournisseurs, par des loueurs ou par les clients eux-mêmes, dont le coût est déjà compris dans le résultat (loyers, prix des ancillaires) : la rémunérer à 6 % compterait deux fois leur coût (la rente de 2027 ne serait que de 9,60 − 7,14 = 2,46 M€). Les actifs hors exploitation sont exclus des CPNE parce qu'ils ne produisent pas le bénéfice économique : ils sont déjà dans l'ANCC, auquel le goodwill s'ajoute.

**Rentes du goodwill (0,5 pt).** Rémunération normale des CPNE = 6 % × 85,00 = **5,10 M€** par an.

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Bénéfice économique | 9,60 | 9,90 | 10,20 | 10,50 | 10,80 |
| Rémunération normale des CPNE | − 5,10 | − 5,10 | − 5,10 | − 5,10 | − 5,10 |
| **Rente du goodwill** | **4,50** | **4,80** | **5,10** | **5,40** | **5,70** |
| Facteur d'actualisation à 10 % | 0,909091 | 0,826446 | 0,751315 | 0,683013 | 0,620921 |
| Rente actualisée | 4,09 | 3,97 | 3,83 | 3,69 | 3,54 |

**Goodwill (0,5 pt).** Goodwill = somme des rentes actualisées = **19,12 M€** (19,117 sans arrondi).

**Valeur patrimoniale (0,5 pt).** Valeur des capitaux propres = ANCC + goodwill = 74,00 + 19,12 = **93,12 M€**, soit **58,20 € par action** ; pour information (non exigé), les 640 000 actions de la famille vaudraient 37,25 M€. Le goodwill s'ajoute à l'ANCC, et non aux CPNE ou à la VSB : les CPNE ne servent qu'à mesurer la rémunération normale.

**Ce que représente le goodwill de FERVANNE (1 pt).** Le goodwill est la valeur actuelle du **superprofit** : FERVANNE gagne en 2027 un bénéfice économique de 11,29 % des capitaux engagés dans l'exploitation, contre 6 % pour un placement peu risqué de même montant. Ce superprofit vient d'actifs que le bilan ne montre pas (au-delà des brevets et dessins déjà valorisés dans l'ANCC, qu'il ne faut pas compter deux fois) : le savoir-faire des polisseurs, des régleurs et des affûteurs, qu'il faut environ trois ans pour former ; la qualification des ancillaires chez les fabricants d'implants, qui prend de douze à dix-huit mois et protège FERVANNE de concurrents nouveaux ; les relations avec les hôpitaux.

Ce goodwill repose pour une large part sur des **compétences détenues par des personnes**, et non par la société. Or ces personnes sont aussi actionnaires : les 52 cadres de FERVANNE Associés, candidats au rachat, et 430 salariés porteurs de parts du fonds d'épargne salariale. Deux conséquences :
- **la fragilité du goodwill** : le départ de quelques cadres ou de polisseurs qualifiés le réduirait rapidement ; c'est pourquoi le cabinet limite la rente à cinq ans, et pourquoi la rente perpétuelle (4,50 / 10 % = 45,00 M€ sur la base de 2027) n'aurait pas de sens ;
- **un enjeu de négociation** : les cadres peuvent faire valoir qu'ils ne doivent pas payer à la famille une valeur qu'ils produisent eux-mêmes, et qu'une partie du superprofit leur revient déjà par l'intéressement et la participation ; la famille répond que le goodwill est attaché à l'entreprise (qualifications obtenues au nom de FERVANNE, organisation, clients) et qu'il a été construit avec les fonds propres qu'elle a laissés dans l'entreprise depuis 1962.

Dans une lecture partenariale de la valeur (Freeman, 1984), le superprofit se partage entre les parties prenantes qui le créent, salariés compris, et pas seulement entre actionnaires. La négociation est aussi marquée par l'**asymétrie d'information** (Akerlof, 1970) : les cadres acheteurs connaissent mieux que la famille les perspectives de l'entreprise, ce qui justifie que les prévisions soient établies par le cabinet et puissent être discutées. Conclusion : le goodwill est réel mais fragile ; il justifie une valeur supérieure à l'ANCC, dans la limite d'une durée courte, et il plaide pour que les compétences restent motivées après la reprise.

**Réponses tolérées** : goodwill calculé en actualisant chaque rente sans arrondi (19,12) ; discussion sur la VSB qui mentionne la méthode des praticiens ou la rente calculée sur la valeur de l'entreprise elle-même (méthode de l'Union européenne des experts comptables), sans calcul ; mention d'une partie du prix payée selon les résultats futurs, sans développement juridique (bonifiée dans 2.2-05).

**Erreurs fréquentes**
- Ajouter le goodwill aux CPNE (85,00 + 19,12 = 104,12) ou à la VSB au lieu de l'ANCC.
- Actualiser les rentes au taux de rémunération normale de 6 % (goodwill 21,34) ; prendre l'ANCC comme base de la rente (goodwill 21,62), contrairement à la convention de l'annexe 2.2.
- Calculer une rente perpétuelle alors que la durée est de cinq ans.
- Valoriser de nouveau les brevets et dessins dans le goodwill.
- `JUR-T13` — définition générale du goodwill sans lien avec les compétences des cadres actionnaires.

**Références** : F03 § 5 (rente abrégée, cohérence base / bénéfice, goodwill ajouté à l'ANCC) [V programme 3.3.b, l. 531-532 ; guide p. 66 ; S manuels pour les variantes] ; F10 Freeman (1984) [V programme 2.1], Akerlof (1970) [V programme 5.1].

---

### 2.3 Valeur de rendement (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Rentabilité exigée = 4,0 % + 1,10 × 5,0 % + 2,5 % = 9,50 % + 2,50 % = **12,00 %** ; c'est un coût des fonds propres, puisque le bénéfice net revient aux seuls actionnaires | 0,5 |
| 2.3-02 | Avec croissance : 9,00 / (12,00 % − 2,00 %) = **90,00 M€**, **56,25 € par action** ; sans croissance : 9,00 / 12,00 % = **75,00 M€**, **46,88 € par action** | 0,5 |
| 2.3-03 | Commentaire : la valeur de rendement (90,00) dépasse l'ANCC (74,00) de 16,00 M€, du même ordre que le goodwill (19,12) : FERVANNE crée de la valeur ; sans croissance, elle retombe au niveau de l'ANCC ; forte sensibilité à g et à la prime de 2,5 points (120,00 M€ sans elle) ; le bénéfice normatif (9,00) n'est pas le résultat de 2026 (8,00, perte de change et charges non récurrentes, 80,00 M€) | 0,5 |

**Rentabilité exigée (0,5 pt).** Par le MEDAF, la rentabilité exigée par un actionnaire diversifié est 4,0 % + 1,10 × 5,0 % = **9,50 %**. Le cabinet ajoute une prime de taille et d'illiquidité de 2,5 points, parce que les actions de FERVANNE ne sont pas cotées et que la société est petite au regard des comparables : **12,00 %**. Le bénéfice capitalisé est un bénéfice net, après frais financiers : il revient aux seuls actionnaires et s'actualise au coût des fonds propres, non au CMPC.

**Valeurs de rendement (0,5 pt).** Le bénéfice normatif de 2027 croît ensuite de 2 % par an : la valeur est celle d'une rente croissante à l'infini (Gordon et Shapiro), 9,00 / (0,12 − 0,02) = **90,00 M€**, soit **56,25 € par action** (36,00 M€ pour le bloc de la famille). Sans croissance, 9,00 / 0,12 = **75,00 M€**, soit **46,88 € par action**.

**Commentaire (0,5 pt).** La valeur de rendement avec croissance dépasse l'ANCC de 16,00 M€ : le marché paierait pour la capacité bénéficiaire de FERVANNE plus que pour son patrimoine, ce qui confirme l'existence d'un goodwill (19,12 M€ par la rente). Sans croissance, la valeur de rendement (75,00 M€) ne dépasse l'ANCC que de 1,00 M€ : tout l'écart vient de la croissance attendue, ce qui rend la méthode très sensible à l'hypothèse de 2 % par an, qui doit rester inférieure à la croissance de long terme de l'économie. Elle est aussi sensible au taux : sans la prime de 2,5 points, la valeur atteindrait 9,00 / 7,50 % = 120,00 M€. La famille contestera cette prime, qui pénalise le vendeur ; les cadres, qui ne pourront pas revendre facilement leurs actions, la défendront. Enfin, le cabinet a raison de partir d'un bénéfice normatif : le résultat de 2026 (8,00 M€) est diminué par une perte de change et des charges non récurrentes et conduirait à 80,00 M€.

**Réponses tolérées** : valeur sans croissance présentée comme une capitalisation « au taux de 12 % » et valeur avec croissance « au taux de capitalisation de 10 % » ; valeurs par action arrondies au centime supérieur.

**Erreurs fréquentes**
- Oublier la prime de taille et d'illiquidité (9,50 %, 120,00 M€) ou l'ajouter au bêta.
- Capitaliser le résultat de 2026 (8,00 M€) sans le commenter.
- Actualiser un bénéfice net au CMPC, ou retrancher la dette financière nette d'une valeur qui est déjà celle des capitaux propres (80,50 M€).
- `JUR-E01` — confondre le bénéfice net capitalisé et un flux de trésorerie disponible.

**Références** : F02 § 2 (MEDAF, primes additionnelles fournies) [V programme 3.1.a et l. 509-511 ; guide p. 64] ; F03 § 2 et F10 Gordon et Shapiro (1956) (valeur à croissance constante) [V programme 3.1.c ; S référence] ; F03 § 8 (sensibilité des méthodes) [V guide p. 64].

---

### 2.4 Échantillon de comparables et fourchette de négociation (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Multiples : A **7,50** ; B **6,90** ; C **7,80** ; D **7,20** ; E **8,40** ; F **16,80** ; G **10,00** ; écarter F (profil de forte croissance, EBITDA encore faible : le multiple paie une croissance future que FERVANNE n'a pas) et G (cours aligné sur une offre d'achat : il comprend une prime de contrôle et n'est pas un prix de marché ordinaire) | 0,5 |
| 2.4-02 | Médiane de 6,90 ; 7,20 ; 7,50 ; 7,80 ; 8,40 = **7,50** ; VGE = 7,50 × 18,20 = **136,50** ; VCP = 136,50 − 9,50 = **127,00** ; après décote de 25 % : **95,25 M€**, **59,53 € par action** | 0,5 |
| 2.4-03 | L'EBITDA est un inducteur de VGE, indépendant de la structure financière, de l'amortissement et de l'impôt de chaque société ; VE et EBITDA traitent les locations de la même façon chez FERVANNE et chez les comparables ; le résultat net (PER, inducteur de VCP) dépend de la dette de chacun et, chez FERVANNE en 2026, d'une perte de change et de charges non récurrentes | 0,5 |
| 2.4-04 | Comparaison : ANCC 46,25 € (plancher), rendement 56,25 €, patrimoniale 58,20 €, multiples 59,53 € ; les trois méthodes de continuité d'exploitation convergent ; fourchette proposée **56 € à 60 € par action**, soit **35,84 M€ à 38,40 M€** pour 640 000 actions, argumentée (minorité de 40 % sans contrôle, contrôle obtenu par FERVANNE Associés, absence d'autre acheteur, fragilité du goodwill) | 0,5 |

**Multiples et sociétés atypiques (0,5 pt).**

| Société | VE | EBITDA 2026 | VE / EBITDA | Décision |
|---|---:|---:|---:|---|
| A | 315,00 | 42,00 | 7,50 | conservée |
| B | 172,50 | 25,00 | 6,90 | conservée |
| C | 499,20 | 64,00 | 7,80 | conservée |
| D | 108,00 | 15,00 | 7,20 | conservée |
| E | 252,00 | 30,00 | 8,40 | conservée |
| F | 151,20 | 9,00 | 16,80 | écartée |
| G | 310,00 | 31,00 | 10,00 | écartée |

F est une société de croissance (chiffre d'affaires en hausse de 40 % par an, EBITDA encore faible) : son multiple rémunère des bénéfices futurs bien supérieurs à l'EBITDA actuel ; FERVANNE, entreprise mature, ne lui est pas comparable. G n'est pas atypique par son activité, mais par son prix : son cours s'est aligné sur une offre d'achat de la totalité des actions, qui comprend une prime de contrôle et les synergies attendues par l'acquéreur ; c'est un prix de transaction, pas un prix de marché ordinaire.

**Multiple retenu et valeur (0,5 pt).** Médiane des cinq multiples conservés, rangés (6,90 ; 7,20 ; 7,50 ; 7,80 ; 8,40) : **7,50**. VGE de FERVANNE = 7,50 × 18,20 = **136,50 M€** ; VCP = 136,50 − 9,50 = **127,00 M€** ; après la décote d'illiquidité de 25 % : 127,00 × 0,75 = **95,25 M€**, soit **59,53 € par action** (38,10 M€ pour la famille). La médiane est préférée à la moyenne parce qu'elle n'est pas tirée par une valeur extrême ; ici, même après exclusion, la moyenne (7,56) est proche de la médiane.

**Choix de l'inducteur (0,5 pt).** Le rapport VE / EBITDA relie une valeur de l'entreprise, qui revient aux actionnaires et aux prêteurs, à un résultat avant frais financiers : il neutralise les écarts de structure financière entre les comparables (de la trésorerie nette de F à l'endettement de C) et les différences d'amortissement et d'impôt. Les valeurs d'entreprise comprennent les dettes locatives, comme la dette financière nette de FERVANNE, et les EBITDA sont calculés hors loyers : l'inducteur et la dette sont traités de la même façon des deux côtés. Le PER (capitalisation / résultat net) est un inducteur de VCP : il dépend de la dette et de la fiscalité de chaque société et, pour FERVANNE, d'un résultat de 2026 diminué par une perte de change et des charges non récurrentes. Pour information, la médiane des PER des cinq sociétés conservées (13,91) appliquée au résultat de 2026 donnerait, après décote, 83,46 M€ (52,16 € par action), et 93,89 M€ (58,68 €) appliquée au bénéfice normatif de 9,00 M€ : l'écart montre la fragilité du PER sur un résultat non récurrent.

**Comparaison et fourchette (0,5 pt).**

| Méthode | Valeur des capitaux propres (M€) | Par action (€) | 640 000 actions (M€) |
|---|---:|---:|---:|
| ANCC (question 2.1) | 74,00 | 46,25 | 29,60 |
| Valeur de rendement avec croissance (question 2.3) | 90,00 | 56,25 | 36,00 |
| Méthode patrimoniale, ANCC + goodwill (question 2.2) | 93,12 | 58,20 | 37,25 |
| Comparables après décote (question 2.4) | 95,25 | 59,53 | 38,10 |

L'ANCC est un plancher, qui ignore la capacité bénéficiaire. Pour comparer les méthodes à périmètre égal, on pourrait ajouter à la valeur de rendement et à celle des comparables la valeur nette d'impôt latent du terrain non utilisé (1,30 − 0,25 × 0,80 = 1,10 M€, soit environ 0,69 € par action), qui ne produit aucun bénéfice ni aucun EBITDA, comprise dans l'ANCC et dans la valeur patrimoniale ; l'écart ne change pas la fourchette. Les trois méthodes qui tiennent compte de la rentabilité donnent des valeurs proches, de 56,25 € à 59,53 € : leur convergence renforce la crédibilité de la fourchette. Une fourchette de négociation de **56 € à 60 € par action**, soit **35,84 M€ à 38,40 M€** pour les 640 000 actions, est raisonnable :
- la borne basse, voisine de la valeur de rendement, correspond à ce que les cadres peuvent défendre : un bloc de 40 % ne donne pas le contrôle et ne se revend pas facilement, et le goodwill dépend de leurs propres compétences ;
- la borne haute, voisine des comparables, correspond à ce que la famille peut défendre : ce bloc permet à FERVANNE Associés de passer de 40 % à 80 % du capital et d'obtenir le contrôle, ce qui justifie de ne pas appliquer de décote de minorité.

La famille n'a pas d'autre acheteur naturel que les cadres, et les cadres ont besoin de l'accord de la famille pour obtenir le contrôle : le prix se fixera dans cette fourchette selon le rapport de force et le financement que les cadres réuniront (`JUR-E03`).

**Réponses tolérées** : écarter seulement F ou seulement G avec une justification économique (médiane de six valeurs, 7,65 dans les deux cas ; accordé à moitié sur 2.4-01) ; décote appliquée au multiple avec un commentaire (VCP 92,88 M€, 58,05 € ; accordé à moitié sur 2.4-02, l'annexe imposant la décote sur la valeur des capitaux propres) ; fourchette différente si elle est justifiée par les valeurs du candidat, par exemple 56,25 € à 59,53 € ou une valeur centrale proche de 58 €.

**Erreurs fréquentes**
- Garder les sept sociétés (médiane 7,80, 62,09 € par action) ou prendre leur moyenne (9,23, 74,29 €).
- Oublier la dette financière nette (VGE prise pour la VCP) ou la décote d'illiquidité (79,38 € par action).
- Faire la moyenne des quatre méthodes, ANCC compris, sans justifier les poids.
- `JUR-E03` — juxtaposer les valeurs sans proposer de fourchette argumentée.

**Références** : F03 § 3 (multiples de VGE et de VCP, médiane, décote d'illiquidité de 20 à 30 % en pratique) [V corrigé 2023 ; sujet 2024 ; guide p. 64-65 ; S] ; F03 § 8 (fourchette et réconciliation des méthodes) [V guide p. 64 et 66] ; F11 § 3 (multiples sectoriels plausibles) [V].

---

### 2.5 Risque systématique et risque spécifique de l'action FERVANNE (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Variance totale 32² = **1 024 %²** ; systématique 1,10² × 16² = **309,76 %²** ; spécifique 1 024 − 309,76 = **714,24 %²** ; part systématique **30,25 %**, spécifique **69,75 %** ; écart-type systématique 1,10 × 16 % = **17,60 %**, spécifique √714,24 = **26,73 %** | 1 |
| 2.5-02 | Le risque spécifique (un seul site, quelques grands clients, savoir-faire de quelques équipes, franc suisse) s'élimine en détenant de nombreux titres (Markowitz, 1952) ; un investisseur diversifié ne le supporte pas, donc le marché ne le paie pas ; la famille, concentrée sur FERVANNE, porte près de 70 % de variance non rémunérée | 0,5 |
| 2.5-03 | Selon le MEDAF (Sharpe, 1964), seule la prime du risque systématique est payée : 4,0 % + 1,10 × 5,0 % = 9,50 % ; la prime de taille et d'illiquidité n'est pas une rémunération du risque spécifique ; limite du modèle pour un actionnaire non diversifié, pour qui c'est le risque total qui compte : raison économique de la sortie, indépendante du prix | 0,5 |

**Décomposition (1 pt).** Selon le modèle de marché, la variance de la rentabilité d'un titre se partage entre une part liée au marché, bêta² × variance du marché, et une part propre à l'entreprise.

| | Variance (%²) | Part de la variance | Écart-type |
|---|---:|---:|---:|
| Risque total | 32² = 1 024,00 | 100 % | 32,00 % |
| Risque systématique | 1,10² × 256 = 309,76 | 30,25 % | 1,10 × 16 % = 17,60 % |
| Risque spécifique | 1 024,00 − 309,76 = 714,24 | 69,75 % | √714,24 = 26,73 % |

Les écarts-types ne s'additionnent pas (17,60 + 26,73 ≠ 32) : ce sont les variances qui s'additionnent. La part systématique est aussi le carré du coefficient de corrélation entre FERVANNE et le marché (0,55² = 0,3025).

**Pourquoi le risque spécifique n'est pas rémunéré (0,5 pt).** Les sept dixièmes du risque de l'action viennent de FERVANNE elle-même : une usine principale, des ancillaires vendus aux seuls fabricants d'implants, un savoir-faire porté par quelques équipes, des ventes en francs suisses. Ce risque est **diversifiable** : dans un portefeuille de nombreux titres, les aléas propres à chaque entreprise se compensent et la variance du portefeuille tend vers la seule covariance avec le marché (Markowitz, 1952). Comme les investisseurs peuvent l'éliminer presque sans coût, le marché ne leur paie aucune prime pour le porter. La famille, dont tout le patrimoine financier est constitué des actions de FERVANNE, supporte donc un risque de 714,24 %² que personne ne lui rémunère.

**MEDAF et conséquences pour la famille (0,5 pt).** Le MEDAF (Sharpe, 1964) traduit ce raisonnement : la rentabilité exigée ne dépend que du bêta, 4,0 % + 1,10 × 5,0 % = **9,50 %**, que l'action soit très ou peu risquée par ailleurs. La prime de 2,5 points de la question 2.3 rémunère la taille et l'illiquidité (on rapproche l'effet taille du modèle de Fama et French, 1993), non le risque spécifique. Le MEDAF suppose des investisseurs diversifiés ; la famille ne l'est pas, et pour elle c'est le risque total qui compte : elle peut tout perdre si FERVANNE perd un grand client, sans en être compensée. Diversifier son patrimoine est donc rationnel quel que soit le prix obtenu : c'est la raison financière de la sortie, au-delà du fait qu'aucun petit-enfant ne travaille dans l'entreprise.

**Réponses tolérées** : calcul en décimales (0,1024 ; 0,030976 ; 0,071424) ; part systématique obtenue par le carré du coefficient de corrélation.

**Erreurs fréquentes**
- Décomposer les écarts-types (32 % − 17,60 % = 14,40 % de risque spécifique) au lieu des variances.
- Prendre bêta × variance du marché au lieu de bêta² × variance du marché (281,60 %²).
- Affirmer que le risque spécifique est rémunéré par une prime supplémentaire, ou que la diversification supprime aussi le risque systématique.
- `JUR-T14` — explication sans référence au principe de diversification ni au MEDAF.

**Références** : F10 Markowitz (1952) [V programme 5.3], Sharpe (1964) [V contexte ; MEDAF au programme 5.2], Fama et French (1993) [V programme 5.2] ; F02 § 2 (MEDAF et ses limites) [V programme 5.2.c ; guide p. 75].

---

### 2.6 Portefeuille proposé par la Banque SAULVANE (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | E(Rp) = 0,50 × 9,20 % + 0,30 × 4,80 % + 0,20 × 8,00 % = **7,64 %** ; βp = 0,50 × 1,00 + 0,30 × 0,10 + 0,20 × 0,70 = **0,67** | 0,5 |
| 2.6-02 | Poche de revenus : 0,6² × 36 + 0,4² × 400 + 2 × 0,6 × 0,4 × 0,40 × 6 × 20 = 12,96 + 64,00 + 23,04 = **100,00 %²**, σ = **10,00 %** ; portefeuille : 0,5² × 324 + 0,5² × 100 + 2 × 0,5 × 0,5 × 0,42 × 18 × 10 = 81,00 + 25,00 + 37,80 = **143,80 %²**, σ = **11,99 %** | 0,5 |
| 2.6-03 | Moyenne pondérée des écarts-types : 14,80 % (poche : 11,60 %) contre 11,99 % (poche : 10,00 %) : la diversification retire **2,81 points**, parce que les corrélations sont inférieures à 1 (Markowitz, 1952) | 0,5 |
| 2.6-04 | Rentabilité exigée = 4,0 % + 0,67 × 5,0 % = **7,35 %** ; espérance 7,64 % : **0,29 point** de plus, avant frais | 0,5 |
| 2.6-05 | Variance systématique 0,67² × 256 = **114,92 %²** ; spécifique 143,80 − 114,92 = **28,88 %²** ; part systématique **79,92 %** ; écarts-types **10,72 %** et **5,37 %** | 0,5 |
| 2.6-06 | Avant / après : écart-type 32 % → 11,99 % ; risque spécifique 26,73 % → 5,37 % ; part systématique 30,25 % → 79,92 % ; bêta 1,10 → 0,67 ; rentabilité exigée 9,50 % → 7,35 % ; le patrimoine devient liquide et son risque est désormais presque entièrement rémunéré ; réserve : poche d'actions de 50 % et besoin de liquidité de l'aînée | 0,5 |

**Rentabilité espérée et bêta (0,5 pt).** Les deux grandeurs sont des moyennes pondérées par les parts des fonds : E(Rp) = 4,60 + 1,44 + 1,60 = **7,64 %** ; βp = 0,50 + 0,03 + 0,14 = **0,67**. Le portefeuille est moins sensible que le marché à la conjoncture.

**Écart-type en deux étapes (0,5 pt).** Le portefeuille se compose du fonds A (50 %) et de la poche de revenus (50 %), elle-même composée des fonds O (60 %) et I (40 %) : on applique deux fois la formule de la variance d'un ensemble de deux composantes (annexe 2.7).
- Poche de revenus : variance = 0,36 × 36 + 0,16 × 400 + 2 × 0,6 × 0,4 × 0,40 × 6 × 20 = 12,96 + 64,00 + 23,04 = **100,00 %²**, écart-type **10,00 %** ; rentabilité espérée 0,6 × 4,80 + 0,4 × 8,00 = 6,08 % ; bêta 0,6 × 0,10 + 0,4 × 0,70 = 0,34.
- Portefeuille : variance = 0,25 × 324 + 0,25 × 100 + 2 × 0,25 × 0,42 × 18 × 10 = 81,00 + 25,00 + 37,80 = **143,80 %²**, écart-type **11,99 %**.

**Effet de la diversification (0,5 pt).** Si les fonds évoluaient parfaitement ensemble (corrélations égales à 1), l'écart-type du portefeuille serait la moyenne pondérée des écarts-types : 0,50 × 18 + 0,30 × 6 + 0,20 × 20 = **14,80 %**. Il n'est que de 11,99 % : la diversification retire **2,81 points** de risque, sans rien retirer à la rentabilité espérée, parce que les corrélations sont inférieures à 1 (0,40 entre les obligations et l'immobilier coté, 0,42 entre les actions et la poche de revenus). Dans la poche, l'effet est le même : 10,00 % au lieu de 0,6 × 6 + 0,4 × 20 = 11,60 %. C'est l'enseignement de Markowitz (1952) : le risque d'un portefeuille dépend des corrélations entre ses composantes, et pas seulement de leurs risques propres.

**Rentabilité exigée (0,5 pt).** Selon le MEDAF, le portefeuille doit rapporter 4,0 % + 0,67 × 5,0 % = **7,35 %** pour rémunérer son risque systématique. Son espérance avant frais (7,64 %) la dépasse de **0,29 point** : les fonds proposés paraissent correctement rémunérés pour leur risque, mais cet avantage est faible, il repose sur les prévisions de la banque et il est calculé avant les frais (question 2.7).

**Décomposition du risque du portefeuille (0,5 pt).** Variance systématique = 0,67² × 256 = **114,92 %²** (écart-type 0,67 × 16 % = **10,72 %**) ; variance spécifique = 143,80 − 114,92 = **28,88 %²** (écart-type √28,88 = **5,37 %**) ; part systématique 114,92 / 143,80 = **79,92 %**. Avec seulement trois fonds, déjà diversifiés chacun, les quatre cinquièmes du risque restant sont du risque de marché.

**Risque du patrimoine avant et après la cession (0,5 pt).**

| Patrimoine financier de la famille | Avant : actions FERVANNE | Après : portefeuille de trois fonds |
|---|---:|---:|
| Écart-type | 32,00 % | 11,99 % |
| Risque systématique (écart-type) | 17,60 % | 10,72 % |
| Risque spécifique (écart-type) | 26,73 % | 5,37 % |
| Part systématique de la variance | 30,25 % | 79,92 % |
| Bêta | 1,10 | 0,67 |
| Rentabilité exigée (MEDAF) | 9,50 % | 7,35 % |

La cession et le placement divisent le risque total par près de trois et le risque spécifique par cinq. La rentabilité espérée baisse, mais le risque qui subsiste est désormais presque entièrement du risque systématique, celui que le marché rémunère : le patrimoine est mieux rémunéré par unité de risque, il devient liquide et ne dépend plus d'une seule entreprise. Deux réserves : la poche d'actions représente la moitié du portefeuille, qui peut perdre une part importante de sa valeur une mauvaise année ; et la comparaison porte sur les 28,00 M€ placés, non sur la totalité du produit de la cession. Les besoins des petits-enfants diffèrent (l'aînée veut acheter un logement dans les trois ans) : une même allocation pour les trois n'est pas forcément adaptée (question 2.7).

**Réponses tolérées** : écart-type de la poche et du portefeuille calculés en décimales (0,0100 ; 0,01438) ; écart-type 12,0 % si le candidat arrondit à une décimale ; part systématique 79,94 % obtenue avec l'écart-type arrondi à 11,99 % ; rentabilité exigée comparée à l'espérance nette de frais (accordé sur 2.6-04 si le calcul de 7,35 % figure).

**Erreurs fréquentes**
- Calculer l'écart-type du portefeuille comme la moyenne pondérée des écarts-types (14,80 %), en oubliant les corrélations.
- Utiliser la corrélation au lieu de la covariance dans le terme croisé (oublier σ₁ σ₂), ou oublier le facteur 2.
- Rentabilité exigée = 4,0 % + 0,67 × 9,0 % : la prime de risque est E(Rm) − rf = 5,0 %, pas E(Rm).
- `JUR-T13` — comparer les risques sans en tirer de conséquence pour la famille.

**Références** : F10 Markowitz (1952) [V programme 5.3], Sharpe (1964) [V contexte] ; F02 § 2 (MEDAF) [V programme 5.2.c] ; programme 5.3.c (variance et écart-type d'un portefeuille de deux titres, corrélations fournies) [V programme l. 589-590 ; guide p. 76-77].

---

### 2.7 Conseil automatisé ou gérant dédié (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Frais : Banque SAULVANE 1,50 % × 28,00 M€ = **420 k€** par an ; TALMESSE 0,60 % × 28,00 M€ = **168 k€** ; écart **252 k€** par an ; rentabilité nette **6,14 %** contre **7,04 %**, toutes deux inférieures à la rentabilité exigée de 7,35 % : les frais absorbent l'avantage de 0,29 point | 0,5 |
| 2.7-02 | Rôle de l'algorithme : profil déduit du questionnaire, allocation par une règle, rééquilibrage automatique et discipliné (contre les biais comportementaux), fonds indiciels à faibles frais (cohérent avec l'efficience des marchés) ; pas de conseil personnalisé ni de produit complexe | 0,5 |
| 2.7-03 | Limites : biais des données (allocation calibrée sur 2005-2025), questionnaire rempli par une seule personne pour trois profils différents, opacité de l'algorithme, comportements simultanés de nombreux clients ; responsabilité : la société de gestion répond de l'adéquation de l'allocation, mais la preuve d'une erreur est difficile si le questionnaire est mal rempli ; la banque engage la responsabilité d'un gérant identifié, mais avec des conflits d'intérêts (fonds maison, produits structurés, crédit) | 0,5 |
| 2.7-04 | Nouveaux acteurs : fintech de la gestion d'actifs, désintermédiation partielle de la banque privée, baisse des frais, gestion à grande échelle (2,4 Md€ pour 61 000 clients, environ 39 k€ par client : un modèle conçu pour une clientèle large), pression sur les banques (offres hybrides, partenariats, rachats), mêmes règles de protection que les banques ; fragilités : modèle économique qui exige du volume, risque cyber | 1 |
| 2.7-05 | Profil de l'indivision : 28 M€, trois horizons différents, besoin de liquidité de l'aînée ; ni l'algorithme seul (un seul profil) ni la gestion actuelle de la banque (frais, conflits d'intérêts) ne conviennent en l'état ; recommandation argumentée : allocation propre à chaque petit-enfant, gestion à faibles frais par fonds indiciels, négociation des frais de la banque ou conseil rémunéré séparément, refus des titres non cotés et des produits structurés | 0,5 |

**Frais et rentabilités nettes (0,5 pt).** Sur 28,00 M€, la gestion de la Banque SAULVANE coûte 1,50 % × 28,00 = **420 k€** par an, celle de TALMESSE 0,60 % × 28,00 = **168 k€** : l'écart est de **252 k€** par an, soit environ 2,52 M€ sur dix ans avant même l'effet de la capitalisation. Rentabilités espérées nettes de frais : 7,64 − 1,50 = **6,14 %** pour la banque, 7,64 − 0,60 = **7,04 %** pour TALMESSE. Toutes deux sont inférieures à la rentabilité exigée pour le risque systématique du portefeuille (7,35 %) : les frais absorbent les 0,29 point d'avance des fonds et, avec la banque, la famille perd 1,21 point par rapport à ce que le marché devrait lui rapporter pour ce risque.

**Rôle de l'algorithme (0,5 pt).** TALMESSE remplace l'entretien par un questionnaire : l'algorithme déduit un profil de risque des réponses et lui associe une allocation type ; il rééquilibre ensuite le portefeuille dès qu'une part s'écarte de plus de 5 points de sa cible. Cette discipline protège l'investisseur de ses propres biais : vendre après une baisse par aversion aux pertes, garder trop longtemps les titres qui ont monté, suivre le marché (Kahneman et Tversky, 1973). L'utilisation de fonds indiciels à faibles frais est cohérente avec l'efficience des marchés (Fama, 1970) : il est difficile de battre durablement un marché efficient une fois les frais payés. L'automatisation permet de servir beaucoup de clients à un coût faible ; en contrepartie, l'offre exclut le conseil personnalisé et les placements hors des fonds proposés.

**Biais des données et responsabilité (0,5 pt).** L'allocation est calibrée sur les rentabilités de 2005 à 2025 : un algorithme reproduit les régularités de la période qui a servi à l'établir, et rien ne garantit qu'elles se répètent ; un événement rare à fort impact (un cygne noir, Taleb, 2007) n'y figure pas. Le questionnaire a été rempli par M. Arnaud OSMONDIER seul, pour trois personnes de 34 à 46 ans aux projets différents : un profil « équilibré » unique est une moyenne qui ne correspond à aucun des trois. La logique de l'algorithme reste opaque pour le client (« boîte noire »), et des milliers de portefeuilles rééquilibrés en même temps selon la même règle peuvent amplifier les mouvements de marché. En cas d'allocation inadaptée, TALMESSE, agréée et soumise aux mêmes règles de protection que la banque (fait d'énoncé), répond de l'adéquation de son conseil, mais il est plus difficile de démontrer une erreur quand le client a lui-même répondu, imparfaitement, au questionnaire. À la Banque SAULVANE, la responsabilité est portée par une gérante identifiée qui connaît la famille depuis 2019 ; mais la relation est une relation d'agence (Jensen et Meckling, 1976) : la gérante place les fonds de sa banque et propose des produits structurés, des titres non cotés et un crédit, qui rapportent à la banque autant qu'à la famille.

**TALMESSE parmi les nouveaux acteurs (1 pt).** TALMESSE est une fintech de la gestion d'actifs : une société de gestion entièrement en ligne qui utilise un algorithme pour faire, à grande échelle et à bas coût, ce que la banque privée fait par des entretiens. Elle opère une **désintermédiation partielle** : le client ne passe plus par un conseiller, mais l'épargne reste placée dans des fonds, par un professionnel agréé. Son modèle repose sur le volume : 2,4 Md€ pour 61 000 clients, soit en moyenne environ 39 k€ par client, montre qu'elle est conçue pour une clientèle large, non pour un patrimoine de 28 M€ aux besoins particuliers. Ces acteurs exercent une **pression sur les frais** des banques, qui répondent par des offres hybrides (algorithme et conseiller), par des partenariats ou par le rachat de fintechs. Leurs fragilités sont celles des fintechs : un modèle économique qui exige une croissance rapide des encours pour couvrir ses coûts, une exposition au risque cyber et l'obligation d'appliquer les mêmes règles de connaissance du client et de lutte contre le blanchiment que les acteurs traditionnels. Pour la famille, l'arrivée de ces acteurs est surtout un levier de négociation face à la banque.

**Profil de la famille et recommandation (0,5 pt).** Le patrimoine à placer est important (28,00 M€), les trois petits-enfants ont des horizons différents (logement dans trois ans pour l'aînée, aucun revenu souhaité avant longtemps pour le cadet) et ils décident ensemble. Ni l'une ni l'autre offre ne convient telle quelle : l'algorithme ne connaît qu'un profil moyen ; la banque est chère et ses propositions de titres non cotés et de produits structurés réintroduiraient l'illiquidité et la complexité dont la cession doit libérer la famille. Recommandation : définir une allocation pour chaque petit-enfant (une réserve en obligations ou en placements monétaires pour l'aînée, une part d'actions plus forte pour le cadet) ; confier l'essentiel du portefeuille à une gestion à faibles frais par fonds indiciels, chez TALMESSE avec un questionnaire par personne ou chez la banque si elle aligne ses frais ; rémunérer séparément, si la famille le souhaite, un conseil patrimonial global ; renoncer aux titres non cotés et aux produits structurés. Sur 28 M€, un point de frais en moins vaut 280 k€ par an.

**Réponses tolérées** : frais exprimés en M€ (0,42 et 0,17) ; recommandation inverse (gérant dédié) si elle est argumentée par l'ampleur et la complexité du patrimoine et assortie d'une négociation des frais ; références à d'autres biais comportementaux reliés au cas.

**Erreurs fréquentes**
- Présenter l'algorithme comme objectif et sans risque, ou la banque comme seule responsable par nature.
- Oublier que les deux offres appliquent la même allocation : leur différence porte sur les frais, l'adaptation au profil et les conflits d'intérêts.
- Développer les règles juridiques de la gestion pour compte de tiers ou de l'indivision, hors du champ de l'épreuve.
- `JUR-M02` — décrire les fintechs en général sans situer TALMESSE ni relier son modèle au patrimoine de la famille.

**Références** : F06 § 6 (fintechs, IA en finance, conseil automatisé, biais des données, opacité, responsabilité) [S ; programme 5.4.a et 5.4.b, l. 599-604 V] ; F10 Fama (1970), Kahneman et Tversky (1973), Taleb (2007) [V programme 5.1], Jensen et Meckling (1976) [V programme 2.1] ; synthèse du jury `JUR-M02` (nouveaux acteurs) [V R2025 p. 25].
