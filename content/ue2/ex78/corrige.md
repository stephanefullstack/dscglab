# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 78 — Dossier 3 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F02 coût du capital, F07 risques de taux et de change, F10 auteurs et théories, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (VAN, TRI, indice de profitabilité et flux actualisés de l'atelier, VAN à 15 % et 16 % ; VAN des trois scénarios, espérance, écart-type, coefficient de variation et probabilité d'une VAN négative ; cours à terme à un an et points de terme ; flux du swap de devises ; coûts actuariels avant et après IS des deux financements ; ratio des prêteurs et endettement net sur capitaux propres avant et pro forma ; valeur de marché de la seconde tranche à 4 %, 5 % et 6 % ; taux garanti, montants et résultats de l'emprunt terme contre terme ; barème, liste noire, hors-programme ; compte d'exploitation, BFR, valeur résiduelle, conversion de la VAN, flux sans swap, marge sous le seuil, écarts de valeur et indemnité vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VAN centrale erronée à la question 3.1, reprise dans les scénarios de la question 3.2, ou un investissement total erroné à la question 3.1, repris dans le ratio pro forma de la question 3.5).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Flux de l'atelier en livres, VAN, TRI, indice de profitabilité, VAN en euros | `7.1.a` Évaluer et classer des projets en milieu certain | 2,5 |
| 3.2 Trois scénarios de volume, espérance, écart-type, coefficient de variation, probabilité d'une VAN négative | `7.1.b` Évaluer et classer des projets en milieu incertain | 2 |
| 3.3 Cours à terme à un an, report et déport ; flux du swap de devises, risque de change supprimé et risques résiduels | `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) ; `6.3.d` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (change) | 3,5 |
| 3.4 Coûts actuariels du prêt en livres et du montage prêt intragroupe et swap, comparaison, recommandation | `7.2.a` Comparer les sources de financement et notamment leurs coûts | 2,5 |
| 3.5 Ratio des prêteurs avant et pro forma, marge sous le seuil, structure financière, refus d'une émission d'actions | `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière et identifier ses déterminants ; `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives | 2,5 |
| 3.6 Valeur de marché de la dette à taux fixe, relation inverse valeur-taux, remboursement anticipé, taux fixe ou variable | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 2 |
| 3.7 Emprunt terme contre terme de la seconde tranche, taux garanti, deux scénarios | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux | 2 |
| **Total** | | **17** |

Répartition par sous-partie : 7.1 : 4,5 points (7.1.a 2,5, 7.1.b 2) ; 6.3 : 3,5 points (6.3.b 1,5, 6.3.d 2) ; 7.2 : 5 points (7.2.a 2,5, 7.2.b 1,5, 7.2.d 1) ; 6.2 : 4 points (6.2.a 2, 6.2.b 2). Part du calcul : environ 10,5 points (3.1-01 à 3.1-04, 3.2-01 à 3.2-03, 3.3-01, 3.3-03, 3.3-04, 3.4-01 à 3.4-03, 3.5-01, 3.5-02, 3.6-01, 3.6-02, 3.7-01 à 3.7-03). Part de l'analyse : environ 6,5 points. Les questions 3.3, 3.6 et 3.7 se traitent sans les résultats des questions 3.1 et 3.2 : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 Flux de l'atelier et critères en avenir certain (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Ventes de machines rénovées **3 000 k£** en 2028 et **4 000 k£** par an de 2029 à 2034 ; EBITDA = marge sur coûts variables (40 k£ par machine) + coûts évités 400 − charges fixes 700 : **900** et **1 300 k£** ; amortissements 2 400 / 20 + 2 100 / 7 = **420 k£** ; résultat d'exploitation **480** et **880 k£** | 0,5 |
| 3.1-02 | Date 0 : − (4 500 + BFR 450) = **− 4 950 k£** ; 2028 : 480 − 120 + 420 − 150 = **630** ; 2029 à 2033 : 880 − 220 + 420 = **1 080** ; 2034 : 1 080 + BFR récupéré 600 + valeur résiduelle nette 2 040 (2 200 − 25 % × (2 200 − 1 560)) = **3 720 k£** | 0,5 |
| 3.1-03 | VAN à 9 % = 6 467 − 4 950 = **1 517 k£** ; indice de profitabilité = 6 467 / 4 950 = **1,31** ; VAN en euros = 1 516,92 / 0,8600 = **1 764 k€** | 0,5 |
| 3.1-04 | TRI **15,77 %** (VAN de 144 k£ à 15 % et de − 42 k£ à 16 % ; interpolation 15 % + 144 / 187 × 1 % = 15,77 %) | 0,5 |
| 3.1-05 | Conclusion : atelier créateur de valeur pour le groupe (VAN positive, TRI supérieur de 6,8 points au CMPC, 1 £ investie rapporte 1,31 £ en valeur actuelle) ; le taux est un CMPC parce que les flux sont avant financement ; la conversion au comptant donne la valeur en euros aujourd'hui, mais la valeur pour le groupe dépend de la livre ; près d'un tiers de la valeur actuelle vient de 2034 (bâtiment et BFR) ; hypothèses centrales à éprouver (question 3.2) | 0,5 |

**Compte d'exploitation de l'atelier (item 3.1-01).**

| k£ | 2028 | Chaque année de 2029 à 2034 |
|---|---:|---:|
| Machines rénovées vendues | 30 | 40 |
| Ventes de machines rénovées (100 k£ × machines) | 3 000 | 4 000 |
| Coûts variables (60 k£ × machines) | − 1 800 | − 2 400 |
| Coûts d'assemblage évités par le groupe | + 400 | + 400 |
| Charges fixes décaissées | − 700 | − 700 |
| **EBITDA** | **900** | **1 300** |
| Amortissements (2 400 / 20 + 2 100 / 7 = 120 + 300) | − 420 | − 420 |
| **Résultat d'exploitation** | **480** | **880** |
| Impôt (25 %) | − 120 | − 220 |

Les coûts d'assemblage évités sont un flux du projet pour le groupe : la rémunération de l'atelier par BRÉVOLAN SA est une recette pour la filiale et une charge pour la mère, sans effet sur les flux du groupe.

**Flux nets de trésorerie (item 3.1-02).** BFR = 15 % des ventes de machines rénovées de l'année, constitué au début de l'année : 450 k£ à la date 0 pour 2028, 600 k£ à partir de 2029, soit une augmentation de 150 k£ à la fin de 2028, et 600 k£ récupérés à la fin de 2034. Valeur nette comptable du bâtiment à la fin de 2034 : 2 400 − 7 × 120 = 1 560 k£ ; plus-value 640 k£, impôt 160 k£, valeur résiduelle nette **2 040 k£**.

| k£ | Date 0 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Investissement | − 4 500 | | | | | | | |
| Résultat d'exploitation après impôt | | 360 | 660 | 660 | 660 | 660 | 660 | 660 |
| + amortissements | | 420 | 420 | 420 | 420 | 420 | 420 | 420 |
| − augmentation du BFR / + récupération | − 450 | − 150 | | | | | | + 600 |
| + valeur résiduelle nette | | | | | | | | + 2 040 |
| **Flux net** | **− 4 950** | **630** | **1 080** | **1 080** | **1 080** | **1 080** | **1 080** | **3 720** |
| Flux actualisé à 9 % | | 578 | 909 | 834 | 765 | 702 | 644 | 2 035 |

**Critères (items 3.1-03 et 3.1-04).**
- Somme des flux actualisés des années 1 à 7 (sans arrondi intermédiaire) : **6 467 k£** ; VAN = 6 467 − 4 950 = **1 517 k£** (1 516,92).
- Indice de profitabilité = 6 467 / 4 950 = **1,31**.
- VAN en euros, convertie au cours au comptant : 1 516,92 / 0,8600 = **1 764 k€** (1 517 / 0,86 = 1 764 avec la VAN arrondie).
- TRI : la VAN vaut 144 k£ à 15 % et − 42 k£ à 16 % ; par interpolation, 15 % + 144 / (144 + 42) × 1 % = 15,77 % ; valeur exacte **15,77 %**.

**Conclusion (item 3.1-05).** Au CMPC de 9,00 % retenu pour les activités britanniques, l'atelier crée de la valeur : VAN de 1 517 k£, soit 1 764 k€ pour le groupe, TRI de 15,77 %, indice de 1,31. Le taux est un CMPC et non un coût des fonds propres, parce que les flux sont des flux d'exploitation, avant financement : ils rémunèrent ensemble les actionnaires et les prêteurs, et le financement est étudié à part (questions 3.4 à 3.7). Actualiser des flux en livres à un taux en livres, puis convertir la VAN au comptant, donne la valeur en euros d'aujourd'hui ; mais les flux futurs seront convertis aux cours futurs : si la livre perd de sa valeur, la valeur de l'atelier en euros baisse, risque que le dossier ne couvre pas et que la dette en livres réduira en partie (questions 3.3 et 3.4). Limites : 2 035 k£ des 6 467 k£ de valeur actuelle (31 %) proviennent de la fin de 2034 (bâtiment et BFR), dont l'estimation est incertaine ; les flux reposent sur un volume central de 40 machines par an, à éprouver par les scénarios.

**Réponses tolérées** : TRI de 15,77 % à 15,78 % selon l'interpolation ; VAN en euros de 1 763 ou 1 764 k€ ; BFR constitué en fin d'année (première constitution en 2028) si l'hypothèse est écrite et appliquée de façon cohérente ; indice de profitabilité de 1,31 calculé comme 1 + VAN / investissement.

**Erreurs fréquentes**
- Retrancher le niveau du BFR chaque année au lieu de sa variation, ou oublier de le récupérer en 2034 (`JUR-E01`).
- Compter la rémunération de l'assemblage par BRÉVOLAN SA comme une recette du groupe, au lieu des coûts évités.
- Oublier l'impôt sur la plus-value du bâtiment, ou ne pas amortir les équipements sur sept ans.
- Déduire des flux les intérêts d'un des financements, alors que le financement est apprécié à part (`JUR-T04`) ; actualiser au taux d'un emprunt ou à un coût des fonds propres (`JUR-T14`).
- Convertir la VAN en multipliant par 0,8600 au lieu de diviser (cotation au certain).

**Références** : F01 § 4 (VAN, TRI, indice de profitabilité, construction des flux) et § 8 (arrondis) [V programme 7.1 ; S] ; programme 7.1.a, guide p. 80-81 (critères en milieu certain ; flux ou éléments permettant de les construire, taux d'actualisation fournis) [V] ; F02 § 5 (CMPC, taux d'actualisation de flux d'exploitation) [S].

---

### 3.2 VAN probabilisée : trois scénarios de volume (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Écart annuel de flux : faible (− 12 machines) × 30 = **− 360 k£**, fort (+ 8) × 30 = **+ 240 k£**, chaque année de 2028 à 2034 ; VAN = 1 516,92 + écart × 5,0330 : faible **− 295 k£**, central **1 517 k£**, fort **2 725 k£** | 0,5 |
| 3.2-02 | Espérance de la VAN = 0,30 × (− 295) + 0,50 × 1 517 + 0,20 × 2 725 = **1 215 k£**, inférieure à la VAN centrale | 0,5 |
| 3.2-03 | Écart-type **1 089 k£** (variance d'environ 1 185 000 k£²) ; coefficient de variation **0,90** ; probabilité d'une VAN négative **30 %** (scénario faible) | 0,5 |
| 3.2-04 | Commentaire : projet créateur de valeur en espérance mais risqué (près d'une chance sur trois de détruire 295 k£) ; VAN nulle vers 30 machines par an à partir de 2029, contre 40 au centre ; distribution asymétrique (faible plus probable que fort) ; limites (une seule variable, trois niveaux, probabilités estimées par la direction, effet sur le BFR négligé) ; leviers : accords de rachat avec les clients de BRÉVOLAN, montée en charge prudente, l'assemblage final (400 k£ par an) ne dépend pas du volume | 0,5 |

**VAN des scénarios (item 3.2-01).** L'écart de flux est constant de 2028 à 2034 ; l'investissement et la valeur résiduelle ne changent pas. La VAN d'un scénario est donc la VAN centrale augmentée de la valeur actuelle de l'écart annuel sur sept ans : facteur d'annuité (1 − 1,09^−7) / 0,09 = **5,0330**.

| Scénario | Probabilité | Machines (2028 ; 2029 à 2034) | Écart annuel (k£) | Flux nets (k£) : date 0 ; 2028 ; 2029 à 2033 ; 2034 | VAN (k£) |
|---|---:|---|---:|---|---:|
| Faible | 30 % | 18 ; 28 | − 360 | − 4 950 ; 270 ; 720 ; 3 360 | **− 295** |
| Central | 50 % | 30 ; 40 | 0 | − 4 950 ; 630 ; 1 080 ; 3 720 | **1 517** |
| Fort | 20 % | 38 ; 48 | + 240 | − 4 950 ; 870 ; 1 320 ; 3 960 | **2 725** |

**Espérance, écart-type, probabilité (items 3.2-02 et 3.2-03).**
- E(VAN) = 0,30 × (− 294,95) + 0,50 × 1 516,92 + 0,20 × 2 724,82 = **1 215 k£** (1 214,94). Contrôle : l'écart annuel espéré vaut 0,30 × (− 360) + 0,20 × 240 = − 60 k£, d'où 1 516,92 − 60 × 5,0330 = 1 215 k£.
- Variance = 0,30 × (− 294,95 − 1 214,94)² + 0,50 × (1 516,92 − 1 214,94)² + 0,20 × (2 724,82 − 1 214,94)² ≈ **1 185 473 k£²** ; écart-type **1 089 k£** ; coefficient de variation 1 089 / 1 215 = **0,90**.
- Probabilité d'une VAN négative, lue sur les scénarios : seul le scénario faible est négatif, **30 %**.

**Commentaire (item 3.2-04).** L'atelier crée de la valeur en espérance (1 215 k£, soit 1 413 k€ au comptant), mais l'espérance est inférieure de 302 k£ à la VAN centrale : le scénario faible est plus probable que le fort, et son écart est plus grand. Le risque est élevé : l'écart-type représente 90 % de l'espérance et la VAN est négative dans 30 % des cas. Le volume est la variable décisive : chaque machine annuelle en moins coûte 30 × 5,0330 = 151 k£ de VAN, et la VAN s'annule vers 30 machines par an à partir de 2029 (40 − 1 516,92 / 151 = 29,95), soit à peine plus que le scénario faible (28). Leviers : sécuriser les rachats de machines usagées (reprise de l'ancienne machine à la vente d'une neuve, accords avec les grands clients britanniques), monter en charge par étapes (une partie des équipements peut attendre), s'appuyer sur l'assemblage final, dont les coûts évités ne dépendent pas des rénovations. Limites : une seule variable réduite à trois niveaux ; probabilités estimées par la direction ; effet du volume sur le BFR négligé ; l'écart-type mesure le risque total du projet, alors que les actionnaires diversifiés d'une société cotée ne demandent à être rémunérés que pour sa part non diversifiable.

**Réponses tolérées** : VAN de chaque scénario calculée en actualisant les sept flux (mêmes résultats à l'unité près) ; écart-type de 1 088 à 1 090 k£ ; variance de 1 185 652 k£² calculée sur les VAN arrondies ; coefficient de variation présenté en % (90 %) ; seuil de VAN nulle non calculé (élément de commentaire, non exigé).

**Erreurs fréquentes**
- Diviser la variance par 3 ou par 2 au lieu de la pondérer par les probabilités.
- Appliquer l'écart de flux à partir de 2029 seulement, ou à la valeur résiduelle.
- Supposer une distribution continue de la VAN pour calculer la probabilité d'une VAN négative : elle se lit sur les scénarios.
- Confondre l'espérance de la VAN avec la VAN centrale de la question 3.1 (`JUR-T12`).

**Références** : F01 § 5 (milieu probabilisable : espérance, variance et écart-type de la VAN pondérés par les probabilités) [S] ; programme 7.1.b, guide p. 81 (analyse de scénarios, espérance et écart-type de la VAN ; probabilités et flux fournis) [V].

---

### 3.3 Cours à terme et swap de devises du prêt intragroupe (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Cours à terme à un an : F = 0,8600 × 1,0400 / 1,0280 = **0,8700** ; points de terme **+ 100** (0,0100) | 0,5 |
| 3.3-02 | Au certain, F > comptant : il faudra plus de livres pour un euro à terme qu'au comptant ; **l'euro est en report, la livre en déport** ; explication : la livre rapporte 1,20 point de plus que l'euro, et l'absence d'arbitrage impose que ce supplément d'intérêts soit compensé par une livre moins chère à terme | 0,5 |
| 3.3-03 | Flux de BRÉVOLAN UK : date 0 : + 5 000 k€ (prêt de BRÉVOLAN SA), − 5 000 k€ et **+ 4 300 k£** (échange initial) ; 2028 à 2032 : − 170 k€ (intérêts dus à la mère), + **170 k€** et − **197,80 k£** (swap) ; 2032 : − 5 000 k€ (remboursement), + 5 000 k€ et − **4 300 k£** (échange final) ; flux nets : **+ 4 300 k£** ; **− 197,80 k£** de 2028 à 2031 ; **− 4 497,80 k£** en 2032, aucun flux net en euros | 1 |
| 3.3-04 | Sans le swap, si 1 EUR = 0,9500 GBP : intérêts d'une année 170 × 0,95 = **161,50 k£** (contre 146,20 k£ au cours de 0,8600) et remboursement 5 000 × 0,95 = **4 750 k£**, soit **450 k£** de plus que les 4 300 k£ reçus | 0,5 |
| 3.3-05 | Taux de la jambe en livres plus élevé : le swap équivaut à un change au comptant et à des achats à terme d'euros ; l'échange final se fait au cours du jour et non au cours à terme (livre en déport) ; l'écart de 1,20 point par an (4,60 % − 3,40 %) compense la banque, qui rend des euros au cours de 0,8600 ; c'est la parité des taux appliquée sur cinq ans | 0,5 |
| 3.3-06 | Risque de change supprimé : tous les euros dus à BRÉVOLAN SA (intérêts et capital) sont reçus du swap aux mêmes dates et pour les mêmes montants ; BRÉVOLAN UK n'a plus qu'une dette en livres, payée avec des recettes en livres ; BRÉVOLAN SA reste en euros des deux côtés ; risques laissés : contrepartie de la banque, coût de sortie du swap si le prêt est remboursé plus tôt ou l'atelier arrêté, remboursement en une fois de 4 300 k£ en 2032, valeur en euros de l'atelier toujours exposée à la livre | 0,5 |

**Cours à terme (items 3.3-01 et 3.3-02).** Cotation au certain (1 EUR = x GBP), taux à un an : F = 0,8600 × (1 + 4,00 %) / (1 + 2,80 %) = 0,870039, soit **0,8700**. Points de terme : 0,8700 − 0,8600 = **+ 0,0100**, 100 points. Un euro vaudra à terme 0,8700 £ au lieu de 0,8600 £ : l'euro est **en report**, la livre **en déport**. Le cours à terme ne prévoit pas la livre : il résulte d'un arbitrage. Une banque qui vend des livres à terme emprunte des euros à 2,80 %, achète des livres au comptant et les place à 4,00 % : le cours à terme rend nul le gain de cet aller-retour, de sorte que la livre, qui rapporte plus, se traite moins cher à terme.

**Flux du prêt intragroupe et du swap pour BRÉVOLAN UK (item 3.3-03).** Nominal en livres : 5 000 × 0,8600 = 4 300 k£ ; intérêts en euros 5 000 × 3,40 % = 170 k€ ; intérêts en livres 4 300 × 4,60 % = 197,80 k£.

| | Date 0 (31/12/2027) | 2028 à 2031 (chaque année) | 2032 |
|---|---:|---:|---:|
| Prêt de BRÉVOLAN SA (k€) | + 5 000 | − 170 | − 5 170 |
| Swap, jambe en euros (k€) | − 5 000 | + 170 | + 5 170 |
| **Solde en euros (k€)** | **0** | **0** | **0** |
| Swap, jambe en livres (k£) | + 4 300 | − 197,80 | − 4 497,80 |
| **Flux nets de BRÉVOLAN UK (k£)** | **+ 4 300** | **− 197,80** | **− 4 497,80** |

**Sans le swap (item 3.3-04).** BRÉVOLAN UK devrait payer 170 k€ par an et 5 000 k€ en 2032 avec ses recettes en livres. Si la livre tombait à 1 EUR = 0,9500 GBP : intérêts d'une année 170 × 0,95 = 161,50 k£ au lieu de 146,20 k£ au cours du jour, et remboursement 5 000 × 0,95 = 4 750 k£, soit 450 k£ de plus que les 4 300 k£ obtenus en 2027. La perte serait celle de la filiale, donc du groupe.

**Le swap (items 3.3-05 et 3.3-06).** Le swap de devises est un contrat de gré à gré qui combine un échange au comptant et des échanges à terme : les deux parties échangent les nominaux au départ, se versent les intérêts de la devise reçue, puis se rendent les nominaux à l'échéance au cours de départ. Comme l'échange final se fait à 0,8600 et non au cours à terme à cinq ans (environ 0,9111 aux taux du swap par la même parité, ordre de grandeur non exigé), la banque, qui rend 5 000 k€ contre 4 300 k£, est compensée par l'écart de taux : BRÉVOLAN UK paie 4,60 % en livres et reçoit 3,40 % en euros. Le swap supprime le risque de change du prêt intragroupe parce que chaque flux en euros dû à BRÉVOLAN SA est reçu de la banque à la même date et pour le même montant (170 k€ par an, 5 000 k€ en 2032) : il ne reste à BRÉVOLAN UK qu'une dette en livres, payée avec ses ventes en livres (couverture naturelle), et BRÉVOLAN SA prête et emprunte en euros. Risques laissés : défaillance de la banque (BRÉVOLAN UK redeviendrait débitrice d'euros sans contrepartie) ; coût de sortie du swap, à sa valeur de marché, si le prêt est remboursé par anticipation ou l'atelier arrêté ; remboursement en une fois de 4 300 k£ en 2032, à préparer ; la valeur en euros de l'atelier et de ses flux, qui reste exposée à la livre (le swap couvre la dette, pas l'exploitation).

**Réponses tolérées** : points de terme exprimés en pips ou en 0,0100 ; tableau présenté du point de vue de la banque si les sens sont cohérents ; explication du report par la comparaison directe des taux (devise au taux le plus élevé en déport) ; cours à terme à cinq ans non calculé.

**Erreurs fréquentes**
- Inverser la formule de parité (taux de l'euro au numérateur avec une cotation au certain) et trouver un cours à terme inférieur au comptant.
- Lire le cours à terme comme une prévision de l'évolution de la livre.
- Oublier l'échange final, ou le faire au cours à terme, ou faire porter les intérêts en livres sur 5 000 au lieu de 4 300 k£.
- Dire que le swap « garantit un gain de change » : il fige les flux et supprime aussi le gain si la livre s'apprécie (`JUR-T13`).

**Références** : F07 § 3.1 (cotation, comptant et terme, position) et § 3.3 (cours à terme par la parité des taux, report et déport, swap de devises pour financer une filiale en devise) [S] ; programme 6.3.b et 6.3.d, guide p. 78-79 (cours comptant, cours à terme, report et déport ; swap de devises ; paramètres fournis) [V].

---

### 3.4 Coût et comparaison des deux financements (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Prêt en livres : frais 43 k£ ; annuités 1 075, 1 032, 989, 946, 903 k£ (860 d'amortissement + 5 % du capital dû) ; coût avant impôt **5,38 %** (taux qui égalise 4 257 et les annuités) | 0,5 |
| 3.4-02 | Coût après impôt **4,02 %** (flux 4 267,75 ; 1 021,25 ; 989 ; 956,75 ; 924,50 ; 892,25 k£), ou 5,38 % × 0,75 = **4,03 %** par l'approximation annoncée | 0,5 |
| 3.4-03 | Montage : frais 25 k€ × 0,86 = 21,50 k£ ; flux 4 278,50 ; − 197,80 de 2028 à 2031 ; − 4 497,80 en 2032 ; coût avant impôt **4,71 %**, après impôt **3,53 %** (3,54 % par l'approximation) ; écart avec le prêt en livres : 0,67 point avant impôt, 0,49 point après | 0,5 |
| 3.4-04 | Comparaison : coût en faveur du montage (signature de BRÉVOLAN SA en euros) ; aucun risque de change résiduel dans les deux cas si le swap va à son terme ; couverture naturelle des flux en livres dans les deux cas ; profil : prêt en livres amorti au rythme des flux de l'atelier, montage remboursé en une fois en 2032 ; simplicité et souplesse en faveur du prêt en livres (un contrat, deux tranches calées sur les paiements, choix du taux variable) ; montage : trois contrats, contrepartie du swap, avance du bâtiment par le groupe | 0,5 |
| 3.4-05 | Recommandation argumentée, par exemple le montage (environ 0,5 point par an après impôt, une dette en livres pour la filiale, risque de change nul), à condition de prévoir le remboursement de 2032 par les flux de l'atelier (1 080 k£ par an) ; le prêt en livres est défendable pour sa simplicité et son amortissement | 0,5 |

**Prêt de CARVELLIN Bank à taux fixe (items 3.4-01 et 3.4-02).** Les deux tranches ont les mêmes conditions et le même profil : le coût est calculé sur les 4 300 k£ comme s'ils étaient tirés en une fois à la date 0.

| k£ | Date 0 | 2028 | 2029 | 2030 | 2031 | 2032 |
|---|---:|---:|---:|---:|---:|---:|
| Capital dû au début de l'année | | 4 300 | 3 440 | 2 580 | 1 720 | 860 |
| Intérêts (5,00 %) | | 215 | 172 | 129 | 86 | 43 |
| Amortissement | | 860 | 860 | 860 | 860 | 860 |
| **Flux avant impôt** (montant − frais 43 ; annuités) | **+ 4 257** | **− 1 075** | **− 1 032** | **− 989** | **− 946** | **− 903** |
| **Flux après impôt** (frais et intérêts × 0,75) | **+ 4 267,75** | **− 1 021,25** | **− 989** | **− 956,75** | **− 924,50** | **− 892,25** |

Coût actuariel avant impôt : **5,38 %** ; après impôt : **4,02 %** (approximation : 5,38 % × 0,75 = 4,03 %).

**Montage prêt de BRÉVOLAN SA et swap (item 3.4-03).** Pour le groupe, les flux en euros se compensent : BRÉVOLAN SA reçoit de sa filiale ce qu'elle doit à ses banques, et BRÉVOLAN UK reçoit du swap ce qu'elle doit à sa mère (question 3.3). Restent les flux en livres de BRÉVOLAN UK et les frais de BRÉVOLAN SA, 0,50 % × 5 000 = 25 k€, soit 21,50 k£.
- Avant impôt : + 4 300 − 21,50 = **+ 4 278,50** ; − 197,80 de 2028 à 2031 ; − 4 497,80 en 2032 ; coût **4,71 %**.
- Après impôt : + 4 300 − 21,50 × 0,75 = + 4 283,88 ; − 148,35 de 2028 à 2031 ; − 4 448,35 en 2032 ; coût **3,53 %** (approximation 4,71 % × 0,75 = 3,54 %).

**Comparaison et recommandation (items 3.4-04 et 3.4-05).**

| Critère | Prêt de CARVELLIN Bank en livres | Prêt de BRÉVOLAN SA et swap |
|---|---|---|
| Coût après impôt | 4,02 % | **3,53 %** (BRÉVOLAN SA emprunte à 3,40 % en euros, et le swap lui donne des livres à 4,60 %, contre 5,00 % à la filiale) |
| Risque de change résiduel | aucun : dette et recettes en livres | aucun si le swap va à son terme ; coût de sortie s'il est rompu |
| Couverture naturelle des flux en livres | oui | oui, par le swap (dette en livres en substance) |
| Profil de remboursement | amortissement constant de 860 k£ par an, au rythme des flux de l'atelier (1 080 k£ par an) | 4 300 k£ en une fois en 2032, à accumuler ou à refinancer |
| Calendrier | deux tranches (2 500 et 1 800 k£), aux dates de paiement du bâtiment et des équipements | une seule mise en place à la date 0 ; bâtiment et acompte avancés six mois par le groupe |
| Simplicité, souplesse | un contrat ; choix entre taux fixe et variable (questions 3.6 et 3.7) | trois contrats à suivre par la trésorerie du groupe ; risque de contrepartie sur la banque du swap |

Le montage coûte environ un demi-point de moins chaque année après impôt, sans risque de change, parce qu'il utilise la signature de la mère, plus forte que celle de la filiale. Il convient si la trésorerie du groupe sait gérer le swap et si le remboursement de 4 300 k£ en 2032 est préparé : les flux de l'atelier (1 080 k£ par an de 2029 à 2033) le permettent dans le scénario central, beaucoup moins dans le scénario faible (720 k£ par an). Le prêt en livres coûte plus, mais il est plus simple et s'amortit au rythme des flux, ce qui limite le risque si les volumes déçoivent (question 3.2). Toute recommandation argumentée sur ces critères est acceptée.

**Réponses tolérées** : coûts après impôt par l'approximation (4,03 % et 3,54 %) annoncée ; coût du prêt en livres calculé sur une tranche (même taux) ; coût du montage avant frais (4,60 %) si l'omission des frais est signalée, avec 0,25 point au plus sur l'item 3.4-03.

**Erreurs fréquentes**
- Comparer les intérêts totaux (645 k£ pour le prêt amorti, 989 k£ pour le montage) au lieu des taux actuariels : le montage paie plus d'intérêts parce que le capital reste dû plus longtemps (`JUR-T04`).
- Mesurer le coût du montage au taux de 3,40 % de l'emprunt de la mère, en oubliant que le swap fait payer des livres à 4,60 %.
- Oublier les frais de dossier, ou ne pas en déduire l'économie d'impôt.
- Mal construire le tableau d'amortissement constant (intérêts calculés sur le capital initial chaque année) (`JUR-I01`).

**Références** : F01 § 3 (tableaux d'amortissement, amortissement constant) [S] ; F02 § 4 (coût de la dette, taux actuariel avant et après IS) [S] ; F07 § 3.3 (swap de devises pour financer une filiale en devise) [S] ; programme 7.2.a, guide p. 81-82 (comparaison des financements par leur coût, taux actuariel, coût net d'IS, frais ; conditions fournies) [V].

---

### 3.5 Structure financière du groupe et refus d'une émission d'actions (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Ratio avant : (20,00 + 5,00) / 22,40 = **1,12** ; pro forma : investissement 4 950 / 0,86 = 5,76 M€, EBITDA de l'atelier 1 300 / 0,86 = 1,51 M€ ; (25,00 + 5,76) / (22,40 + 1,51) = 30,76 / 23,91 = **1,29**, sous le seuil de 1,50 ; marge sous le seuil : 1,50 × 22,40 − 25,00 = **8,60 M€** avant, 1,50 × 23,91 − 30,76 = **5,11 M€** après | 0,5 |
| 3.5-02 | Dette financière nette (dettes locatives comprises) / capitaux propres : 25,00 / 104,00 = **24,04 %** avant, 30,7558 / 104,00 = **29,57 %** après (29,58 % avec la dette pro forma arrondie à 30,76 M€) (hors dettes locatives : 19,23 % et 24,77 %, ratio de 0,89 et 1,08) | 0,5 |
| 3.5-03 | Effet : endettement en hausse mais modéré, capitaux propres inchangés, capacité de remboursement préservée (ratio de 1,29 contre 1,50, marge réduite de 3,49 M€) ; le choix entre les deux financements ne change pas l'effet consolidé à la date 0 (filiale détenue à 100 %, même montant de dette et même trésorerie consommée) ; différences : rythme de désendettement (prêt amorti), endettement porté par la mère avec le montage, dette en livres dont la valeur en euros suit la livre comme l'EBITDA de l'atelier | 0,5 |
| 3.5-04 | Financement hiérarchique (Myers et Majluf, 1984) : asymétrie d'information, l'émission d'actions est perçue comme le signe d'actions surévaluées et fait baisser le cours ; ordre : autofinancement (650 k£ de trésorerie du groupe), dette (4 300 k£), actions en dernier ; la famille applique cet ordre à l'atelier : un projet de 5,76 M€, à signer en juin, ne justifie pas à lui seul les coûts et le signal d'une émission ; l'offre liée au transfert répond à d'autres motifs et ne contredit pas cette hiérarchie pour ce projet | 0,5 |
| 3.5-05 | Signal par l'endettement (Ross, 1977) : s'endetter montre la confiance de la direction dans les flux de l'atelier ; contrôle : une dette ne dilue pas la famille (62 % aujourd'hui) ; théorie du compromis (Myers, 1977) : économie d'impôt sur les intérêts tant que le risque de défaillance reste faible, ce que confirme la marge sous le seuil ; limite : si les volumes déçoivent, la dette pèse, d'où l'intérêt d'un endettement mesuré | 0,5 |

**Ratio des prêteurs (item 3.5-01).**

| M€ | Avant le projet | Atelier (converti à 0,8600) | Pro forma |
|---|---:|---:|---:|
| Dette financière nette hors dettes locatives | 20,00 | + 5,76 (4 950 k£) | 25,76 |
| Dettes locatives | 5,00 | | 5,00 |
| **Dette financière nette, dettes locatives comprises** | **25,00** | | **30,76** |
| EBITDA | 22,40 | + 1,51 (1 300 k£, année pleine) | 23,91 |
| **Ratio (seuil 1,50)** | **1,12** | | **1,29** |
| Marge sous le seuil (1,50 × EBITDA − dette) | 8,60 | | 5,11 |
| Capitaux propres | 104,00 | | 104,00 |
| **Dette financière nette, dettes locatives comprises / capitaux propres** | **24,04 %** | | **29,57 %** |

L'investissement total de l'atelier (bâtiment, équipements et BFR initial, 4 950 k£) augmente la dette nette consolidée de 5,76 M€ quel que soit son financement : 4 300 k£ par l'emprunt, 650 k£ par la trésorerie du groupe (200 k£ du solde des équipements et 450 k£ de BFR initial). Le ratio pro forma (1,2862 avant arrondi) reste sous le seuil de 1,50.

**Effet sur la structure financière (item 3.5-03).** L'atelier fait passer le ratio surveillé par les prêteurs de 1,12 à 1,29 et l'endettement net de 24,04 % à 29,57 % des capitaux propres : la structure reste solide, mais la marge sous le seuil baisse de 8,60 à 5,11 M€, ce qui limite les projets suivants. Dans les comptes consolidés, BRÉVOLAN UK est détenue à 100 % : que la dette soit contractée par la filiale auprès de CARVELLIN Bank ou par la mère auprès de ses banques, la dette nette consolidée augmente du même montant à la date 0, et le ratio ne dépend pas du choix. Les différences viennent ensuite : (1) le prêt en livres s'amortit de 860 k£ par an et fait baisser le ratio plus vite que le montage, remboursé en 2032 ; (2) avec le montage, la dette est portée par BRÉVOLAN SA, dont les prêteurs surveillent le ratio ; (3) en substance, le groupe a une dette en livres dans les deux cas : si la livre perd de sa valeur, la dette et l'EBITDA de l'atelier baissent ensemble en euros, et le ratio bouge peu.

**Refus d'une émission d'actions (items 3.5-04 et 3.5-05).** Selon le financement hiérarchique de Myers et Majluf (1984), les dirigeants connaissent mieux que les investisseurs la valeur de l'entreprise : une émission d'actions est lue comme le signe que l'action est surévaluée, et le cours baisse à l'annonce ; l'entreprise finance donc ses projets d'abord par l'autofinancement, puis par la dette, et n'émet des actions qu'en dernier recours. Le plan de financement de l'atelier suit cet ordre : 650 k£ de trésorerie du groupe, 4 300 k£ d'emprunt, aucune action. Ce refus vise le financement de l'atelier : un projet de 5,76 M€, dont le financement doit être signé en juin, ne justifie pas à lui seul les coûts fixes et le signal d'une émission. L'offre d'actions envisagée avec le transfert répond à d'autres motifs (liquidité de l'action, flottant, autres emplois des fonds) ; elle n'est supposée réalisée dans aucun calcul et ne contredit pas la hiérarchie pour ce projet. Selon Ross (1977), l'endettement est un signal crédible, car coûteux pour une direction qui ne croirait pas à ses flux : il montre la confiance de la direction dans l'atelier. Une dette ne dilue pas non plus la famille (62 % du capital et des voix aujourd'hui), alors qu'une émission pour l'atelier la diluerait. La théorie du compromis (Myers, 1977) éclaire le niveau de dette : l'économie d'impôt sur les intérêts (25 %) justifie l'emprunt tant que le risque de défaillance reste faible, ce que confirme un ratio de 1,29 contre 1,50 ; mais la probabilité de 30 % d'une VAN négative (question 3.2) invite à ne pas pousser plus loin l'endettement.

**Réponses tolérées** : ratio pro forma calculé sans arrondir les montants convertis (1,29) ; rapport dette / capitaux propres pro forma de 29,58 % calculé sur la dette arrondie à 30,76 M€ ; ratio hors dettes locatives présenté en plus (0,89 et 1,08), si la définition des prêteurs est ensuite appliquée ; gearing exprimé en nombre de fois (0,24 et 0,30) ; autonomie financière (capitaux propres / capitaux propres + dette) acceptée à la place du rapport dette / capitaux propres si elle est interprétée.

**Erreurs fréquentes**
- Oublier les dettes locatives, comprises dans la définition des prêteurs, ou n'ajouter que le montant emprunté (5,00 M€) au lieu de l'investissement total.
- Ne pas convertir les montants en livres, ou les multiplier par 0,8600.
- Attribuer le financement hiérarchique à Modigliani et Miller, ou inverser l'ordre (actions avant dette) (`JUR-T14`).
- Citer les théories sans les appliquer au cas (part de la famille, trésorerie du groupe, marge sous le seuil) (`JUR-T13`, `JUR-M01`).

**Références** : F10 (Myers et Majluf, 1984, financement hiérarchique ; Ross, 1977, signal par l'endettement ; Myers, 1977, théorie du compromis, attribution du programme) [V programme 7.2] ; programme 7.2.b et 7.2.d, guide p. 82 (effets sur le levier, la liquidité, l'autonomie et la capacité de remboursement ; théories du choix de financement) [V].

---

### 3.6 Valeur de la dette à taux fixe et choix du taux (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Seconde tranche : annuités 450, 432, 414, 396, 378 k£ (360 d'amortissement + 5 % du capital dû) ; valeur au taux du marché de 5,00 % = **1 800,00 k£** (égale au capital dû) | 0,5 |
| 3.6-02 | Taux du marché à 4,00 % : valeur **1 849,34 k£**, + 49,34 k£ (+ 2,74 %) ; à 6,00 % : **1 752,74 k£**, − 47,26 k£ (− 2,63 %) | 0,5 |
| 3.6-03 | Relation inverse : la valeur est la valeur actuelle de flux fixes ; quand les taux montent, elle baisse, et inversement ; variation non symétrique et plus forte pour une dette longue (duration d'environ 2,82 ans, soit environ 2,7 % par point) ; pour l'emprunteur, une baisse des taux rend sa dette plus chère qu'au marché (coût d'opportunité) ; remboursement anticipé si les taux baissent à 4 % : gain de 49,34 k£ inférieur à l'indemnité de 54,00 k£ (3 % × 1 800), sans compter 18 k£ de nouveaux frais : pas d'intérêt à rembourser | 0,5 |
| 3.6-04 | Taux fixe ou variable : variable aujourd'hui moins cher (4,70 % contre 5,00 %), mais la courbe des taux en livres monte (3,90 %, 4,00 %, 4,20 %) et le marché attend des taux plus élevés (taux implicite de 4,35 % pour 2028, soit 5,05 % marge comprise) ; une hausse d'un point coûterait 18 k£ sur la première période de la seconde tranche (le taux de la première tranche est connu à la signature), puis jusqu'à 34,40 k£ par an sur le capital restant dû (43 k£ par an sur 4 300 k£ en ordre de grandeur) ; flux de l'atelier incertains (question 3.2) et seuil des prêteurs : le taux fixe protège la trésorerie et la VAN ; recommandation : taux fixe | 0,5 |

**Valeur de marché de la seconde tranche au 31 décembre 2027 (items 3.6-01 et 3.6-02).** La valeur de marché d'une dette est la valeur actuelle, au taux du marché, des annuités qui restent à payer.

| k£ | 2028 | 2029 | 2030 | 2031 | 2032 | Valeur | Écart avec 1 800 k£ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Capital dû au début de l'année | 1 800 | 1 440 | 1 080 | 720 | 360 | | |
| Annuité (360 + 5 % du capital dû) | 450 | 432 | 414 | 396 | 378 | | |
| Valeur au taux de 5,00 % | | | | | | **1 800,00** | 0 |
| Valeur au taux de 4,00 % | | | | | | **1 849,34** | **+ 49,34 (+ 2,74 %)** |
| Valeur au taux de 6,00 % | | | | | | **1 752,74** | **− 47,26 (− 2,63 %)** |

**Relation inverse et remboursement anticipé (item 3.6-03).** Les annuités d'une dette à taux fixe sont figées ; leur valeur actuelle baisse quand le taux d'actualisation monte, et monte quand il baisse. La variation n'est pas symétrique (+ 2,74 % pour une baisse d'un point, − 2,63 % pour une hausse) et elle est d'autant plus forte que les flux sont lointains : la duration de la tranche, environ 2,82 ans à 5 %, en donne l'ordre de grandeur (2,82 / 1,05 ≈ 2,7 % par point). Pour BRÉVOLAN UK, le risque d'une dette à taux fixe est un risque de valeur, ou d'opportunité : si les taux baissent à 4 %, elle continue de payer 5 % et sa dette vaut 49,34 k£ de plus que le capital dû. Rembourser par anticipation ne servirait à rien : l'indemnité de 3 % × 1 800 = 54,00 k£ dépasse ce gain (− 4,66 k£), et un nouveau prêt coûterait 18 k£ de frais ; l'indemnité est fixée pour protéger la banque contre ce remboursement. Si les taux montent, la dette vaut moins que le capital dû : le taux fixe joue alors en faveur de BRÉVOLAN UK.

**Taux fixe ou variable (item 3.6-04).** Le taux variable coûte aujourd'hui 4,00 % + 0,70 % = 4,70 %, moins que le taux fixe de 5,00 % : c'est le prix de la protection. Mais la courbe des taux en livres monte avec la durée (3,90 % à six mois, 4,00 % à un an, 4,20 % à dix-huit mois) : le taux implicite de 2028 est de 4,35 %, soit 5,05 % marge comprise (question 3.7), au-dessus du taux fixe. Chaque point de hausse coûterait 1 800 × 1 % = 18 k£ sur la première période de la seconde tranche (le taux de la première période de la première tranche est connu à la signature), puis jusqu'à 3 440 × 1 % = 34,40 k£ par an sur le capital restant dû à partir de 2029 (43 k£ par an sur 4 300 k£ en ordre de grandeur). Le taux variable donne un risque de flux (les intérêts changent chaque année), le taux fixe un risque de valeur (sans effet sur la trésorerie si la dette est gardée jusqu'au terme). Pour un atelier dont les volumes sont incertains (question 3.2) et pour un groupe qui surveille un ratio de dette, la prévisibilité des intérêts compte plus que l'économie de 0,30 point de la première année : le taux fixe est recommandé.

**Réponses tolérées** : valeurs calculées sur la dette totale de 4 300 k£ au 31 décembre 2027 (4 417,86 et 4 187,11 k£, mêmes pourcentages) si l'hypothèse d'un tirage en une fois est écrite ; remboursement anticipé étudié à la première échéance, le 31 décembre 2028 (valeur à 4 % des annuités restantes 1 473,31 k£ pour un capital de 1 440 k£, gain 33,31 k£, inférieur à l'indemnité de 43,20 k£ et aux 14,40 k£ de nouveaux frais : même conclusion) ; duration non calculée (élément de commentaire, non exigé) ; recommandation du taux variable si elle est justifiée par une anticipation de baisse des taux et par la capacité de l'atelier à supporter une hausse.

**Erreurs fréquentes**
- Actualiser au taux fixe du prêt (5 %) dans les trois cas, ou actualiser le seul capital sans les intérêts.
- Affirmer que la valeur de la dette monte quand les taux montent, ou confondre la valeur pour le prêteur et le coût pour l'emprunteur.
- Comparer le gain d'un remboursement anticipé à l'indemnité sans tenir compte des frais du nouveau prêt.
- Dire que le taux fixe « supprime tout risque » : il laisse le risque d'opportunité (`JUR-T13`).

**Références** : F07 § 2.1 (exposition au risque de taux, relation valeur-taux, duration et sensibilité) et § 2.4 (choix d'une couverture de taux) [S] ; programme 6.2.a, guide p. 78 (diagnostic d'une dette à taux fixe ou variable, effet d'une variation de taux sur la valeur) [V].

---

### 3.7 Emprunt terme contre terme de la seconde tranche (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Montant emprunté le 30 juin 2027 pour dix-huit mois : 1 800 / 1,039^0,5 = **1 765,89 k£**, placé six mois à 3,90 % pour obtenir 1 800 k£ le 31 décembre 2027 ; remboursement le 31 décembre 2028 : 1 765,89 × 1,042^1,5 = **1 878,31 k£** ; intérêts garantis de la période : **78,31 k£** | 0,5 |
| 3.7-02 | Taux garanti : (1,042^1,5 / 1,039^0,5) − 1 = **4,35 %** ; taux payé, marge comprise : **5,05 %** | 0,5 |
| 3.7-03 | Taux constaté de 3,60 % : intérêts sans garantie **64,80 k£**, perte de la garantie **− 13,51 k£**, taux payé 4,30 % sans garantie contre 5,05 % ; taux de 5,00 % : intérêts sans garantie **90,00 k£**, gain **+ 11,69 k£**, taux payé 5,70 % sans garantie contre 5,05 % | 0,5 |
| 3.7-04 | Conclusion : la garantie fige le taux de 2028 quoi qu'il arrive (gain si les taux montent, perte s'ils baissent : opération ferme, sans prime) ; elle ne couvre qu'un an et une tranche, gonfle le bilan (emprunt et placement simultanés) et expose au risque de contrepartie sur le placement ; à 5,05 %, elle coûte plus que le taux fixe de 5,00 % pour cinq ans : si BRÉVOLAN UK veut de la sécurité, le taux fixe est préférable ; un FRA donnerait le même taux sans mouvement de capitaux (citation non exigée) | 0,5 |

**Montage (items 3.7-01 et 3.7-02).** Le 30 juin 2027, BRÉVOLAN UK emprunte pour dix-huit mois et place pour six mois la somme qui vaudra 1 800 k£ le 31 décembre 2027 :
- montant emprunté et placé : 1 800 / (1,039)^0,5 = **1 765,89 k£** ;
- le 31 décembre 2027, le placement rend 1 800 k£, qui paient le solde des équipements ;
- le 31 décembre 2028, BRÉVOLAN UK rembourse 1 765,89 × (1,042)^1,5 = **1 878,31 k£**, dont 1 800 k£ de capital, repris par la seconde tranche, et **78,31 k£** d'intérêts pour la période ;
- taux garanti f : (1,042)^1,5 = (1,039)^0,5 × (1 + f), d'où f = 1,063657 / 1,019313 − 1 = **4,35 %** (4,3503 %), soit 78,31 / 1 800 ; taux payé avec la marge de 0,70 % : **5,05 %**.

**Scénarios (item 3.7-03).** Intérêts de la période sans garantie = 1 800 × taux constaté ; gain (ou perte) = intérêts sans garantie − 78,31 k£ ; la marge (0,70 % × 1 800 = 12,60 k£) est due dans les deux cas.

| Taux à un an constaté le 31/12/2027 | 3,60 % | 5,00 % |
|---|---:|---:|
| Intérêts sans garantie (k£) | 64,80 | 90,00 |
| Intérêts garantis (k£) | 78,31 | 78,31 |
| **Gain (+) ou perte (−) de la garantie (k£)** | **− 13,51** | **+ 11,69** |
| Taux payé sans garantie (marge comprise) | 4,30 % | 5,70 % |
| Taux payé avec garantie (marge comprise) | 5,05 % | 5,05 % |

**Conclusion (item 3.7-04).** L'emprunt terme contre terme fixe dès la signature le taux de la première période de la seconde tranche : BRÉVOLAN UK paiera 5,05 % quel que soit le taux du 31 décembre 2027. C'est une couverture ferme et sans prime : elle fait gagner 11,69 k£ si le taux monte à 5,00 %, mais perdre 13,51 k£ s'il baisse à 3,60 %, car elle supprime aussi la baisse. Elle a trois limites : elle ne couvre qu'une période d'un an sur cinq et une tranche sur deux ; elle oblige à emprunter et à placer en même temps 1 765,89 k£ pendant six mois, ce qui alourdit le bilan et expose à la défaillance de la banque sur le placement ; elle coûte plus que le taux fixe proposé (5,05 % contre 5,00 %), qui couvre les cinq années. Elle n'a d'intérêt que si BRÉVOLAN UK garde le taux variable pour les années suivantes et veut seulement figer 2028. Pour un atelier aux flux incertains, le taux fixe de la question 3.6 reste la solution la plus simple et la moins chère pour se protéger. Un accord de taux futur (FRA) donnerait la même protection sans emprunt ni placement, par le seul règlement d'un différentiel.

**Réponses tolérées** : taux garanti calculé par capitalisation simple ((1 + 4,20 % × 1,5) / (1 + 3,90 % × 0,5) − 1 = 4,27 %, soit 4,97 % marge comprise) si la méthode est annoncée, contraire à la convention de l'annexe 3.7 : 0,25 point au plus sur l'item 3.7-02, résultats de 3.7-03 notés en cohérence ; gain et perte comparés sur les taux plutôt que sur les montants ; intérêts garantis calculés comme 1 800 × 4,35 % = 78,30 k£ avec le taux arrondi.

**Erreurs fréquentes**
- Calculer le taux garanti comme une moyenne des taux à six et à dix-huit mois, ou comme leur différence.
- Emprunter 1 800 k£ au lieu de la valeur actuelle de 1 800 k£ à six mois.
- Inverser les rôles : placer pour dix-huit mois et emprunter pour six mois, ce qui garantit un taux de placement et non d'emprunt.
- Présenter la garantie comme une option qui ne joue qu'en cas de hausse (`JUR-T13`).

**Références** : F07 § 2.2 (instruments fermes : emprunt terme contre terme, taux implicite, FRA) [S] ; F01 § 2 et § 6 (capitalisation composée, taux équivalents) [S] ; programme 6.2.b, guide p. 78 (taux garanti d'un emprunt terme contre terme, choix d'une couverture selon le coût, la simplicité et le risque résiduel ; paramètres fournis) [V].
