# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 69 — Dossier 3 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F05 ingénierie financière, F06 marchés et finance comportementale, F07 risques de taux et de change, trésorerie de groupe, F10 auteurs et théories, F11 données de marché, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (coûts actuariels avant et après IS du prêt, du placement privé et de l'avance ; tableau d'amortissement du prêt ; BPA des trois solutions ; swap dans trois scénarios ; duration, sensibilité et prix des obligations ; coûts et taux effectifs des trois financements du stock de campagne ; centralisation des soldes ; barème, liste noire, hors-programme ; avantage de l'avance, répartition du capital, seuils de contrôle, rentabilités, rapports d'endettement, dette maximale et capitaux-jours vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un montant restant à financer erroné à la question 3.1, repris dans les BPA et les rapports d'endettement de la question 3.3, ou une dette maximale erronée à la question 3.3, reprise dans le plan de financement de la question 3.4).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Montant restant à financer, coûts actuariels du prêt et du placement privé, avantage de l'avance remboursable, aide publique | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `7.2.c` Analyser les nouveaux outils de financement | 3 |
| 3.2 Financement intermédié et financement direct pour SOLANÈRE | `5.1.a` Appréhender le rôle des sources de financement (direct sur les marchés, indirect avec les intermédiaires) et le rôle des banques dans l'économie réelle | 1 |
| 3.3 Actions nouvelles et répartition du capital, BPA, rentabilité des capitaux propres, rapports d'endettement, clauses, effet de levier | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital ; `4.2.d` Décrypter les montages financiers avec et sans levier financier ; `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière et identifier ses déterminants | 4 |
| 3.4 Contrôle de CORVENNE, coût pour les minoritaires, financement hiérarchique et compromis, plan de financement | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital ; `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives ; `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière | 3 |
| 3.5 Swap payeur de fixe sur le prêt, comparaison avec le placement privé, duration, sensibilité et prix des obligations | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt ; `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux | 3 |
| 3.6 Financement du stock de campagne : crédit confirmé, titres négociables à court terme, cession de créances | `6.1.b` Discerner les différents types de financement et de placement | 2 |
| 3.7 Centralisation physique des soldes des trois sociétés | `6.1.a` Appliquer les mécanismes de centralisation de trésorerie | 1 |
| **Total** | | **17** |

Répartition par sous-partie : 7.2 ≈ 6,5 points (7.2.a ≈ 2, 7.2.b ≈ 2, 7.2.c ≈ 1, 7.2.d ≈ 1,5) ; 4.2 ≈ 3,5 points ; 5.1 : 1 point ; 6.2 : 3 points ; 6.1 : 3 points. Part du calcul : environ 9 points (3.1-01 à 3.1-04, 3.3-01 à 3.3-05, 3.4-01, 3.5-01, 3.5-04, 3.6-01 à 3.6-03, 3.7-01). Part de l'analyse : environ 8 points. Les questions 3.6 et 3.7 (3 points) se traitent sans les résultats des questions 3.1 à 3.5 : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 Montant restant à financer, coûts actuariels, avance remboursable et aide publique (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Reste à financer : 30,00 − 2,00 − 3,00 = **25,00 M€** (l'avance est une ressource, même remboursable) ; prêt : flux de SOLANÈRE + 24,75 ; − 6,06 ; − 5,85 ; − 5,64 ; − 5,43 ; − 5,21 ; coût actuariel avant IS **4,62 %** | 0,5 |
| 3.1-02 | Prêt après IS : + 24,81 (frais nets d'impôt) ; − 5,80 ; − 5,64 ; − 5,48 ; − 5,32 ; − 5,16 ; coût après IS **3,46 %** (approximation 4,62 % × 0,75 = 3,46 % admise si elle est signalée) | 0,5 |
| 3.1-03 | Placement privé : + 24,50, coupons − 1,23 (années 1 à 6), − 26,23 en année 7 ; coût avant IS **5,25 %** ; après IS : + 24,63, − 0,92 et − 25,92 ; coût **3,92 %** (approximation 3,94 % admise) | 0,5 |
| 3.1-04 | Avance : coût actuariel nul ; valeur actuelle des remboursements à 3,46 % : **2,62 M€** ; avantage **0,38 M€** (12,69 % de l'avance) ; aide totale en valeur actuelle 2,00 + 0,38 = 2,38 M€ | 0,5 |
| 3.1-05 | Conditions et limites de l'aide : subvention conditionnelle (reversement de 2,00 M€ si la baisse de 40 % de l'eau prélevée par tonne n'est pas atteinte en 2029), avance exigible si l'effectif baisse de plus de 10 %, rapport annuel vérifié, décision attendue en octobre 2027 (après le conseil), aide limitée à la ligne de frites ; avantages : coût nul, financement « vert » qui réduit la dette à lever et améliore le signal de durabilité | 0,5 |
| 3.1-06 | Comparaison : le prêt coûte 0,63 point de moins que le placement privé avant IS (0,46 après IS), mais son taux est variable (risque de hausse) et il est amortissable (5 M€ par an) ; le placement privé fixe le taux sur 7 ans, sans remboursement avant 2034, avec une clause plus souple (3,50) ; le coût apparent du prêt n'est donc pas son coût final | 0,5 |

**Montant restant à financer (item 3.1-01, avec le coût du prêt avant IS).** L'aide du fonds HYDRÉVAL couvre 2,00 M€ de subvention et 3,00 M€ d'avance, soit 5,00 M€ des 17,00 M€ de la ligne de frites économe en eau. Il reste **30,00 − 5,00 = 25,00 M€** à financer, par l'une des trois solutions. L'avance n'est pas un don : elle sera remboursée, mais elle procure les fonds le 1er janvier 2028, comme une dette.

**Coût actuariel du prêt de la Banque ESTRÉVAL (items 3.1-01 et 3.1-02, 1 pt avec le montant restant à financer).** Convention de l'annexe 3.6 : taux de départ supposé constant, 2,65 % + 1,60 % = 4,25 % ; intérêts annuels sur le capital restant dû au début de l'année ; amortissement constant de 25,00 / 5 = 5,00 M€ ; frais de 1 % payés à la date 0.

| Année | Capital restant dû au début | Intérêts | Amortissement | Décaissement avant IS | Économie d'IS | Décaissement après IS |
|---|---:|---:|---:|---:|---:|---:|
| 0 | | | | reçu : 25,00 − 0,25 = **24,75** | + 0,0625 (frais) | reçu net : **24,81** |
| 1 (2028) | 25,00 | 1,06 | 5,00 | 6,06 | 0,27 | 5,80 |
| 2 | 20,00 | 0,85 | 5,00 | 5,85 | 0,21 | 5,64 |
| 3 | 15,00 | 0,64 | 5,00 | 5,64 | 0,16 | 5,48 |
| 4 | 10,00 | 0,43 | 5,00 | 5,43 | 0,11 | 5,32 |
| 5 | 5,00 | 0,21 | 5,00 | 5,21 | 0,05 | 5,16 |

Le coût avant IS est le taux t tel que 24,75 = Σ décaissements / (1 + t)^n. Valeur actuelle nette des flux de SOLANÈRE : − 0,08 à 4,5 % et + 0,05 à 4,7 % ; par interpolation, **t = 4,62 %**. Il dépasse le taux nominal de 4,25 % à cause des frais de 1 %, qui pèsent d'autant plus que la durée moyenne du prêt est courte (le capital est remboursé par cinquièmes). Après IS : 24,8125 = Σ décaissements nets / (1 + t')^n ; VAN − 0,04 à 3,4 % et + 0,03 à 3,5 % ; **t' = 3,46 %**. L'approximation 4,62 % × (1 − 25 %) = 3,46 % donne ici le même résultat ; elle est admise si le candidat l'annonce.

**Coût actuariel du placement privé (0,5 pt).** Coupon 25,00 × 4,90 % = 1,225 M€ ; frais 2 % = 0,50 M€.
- Avant IS : 24,50 = 1,225 × [1 − (1 + t)^−7] / t + 25,00 × (1 + t)^−7 ; VAN − 0,36 à 5,0 % et + 0,35 à 5,5 % ; **t = 5,25 %**.
- Après IS : reçu net 24,50 + 0,50 × 25 % = 24,625 ; coupons nets 1,225 × 0,75 = 0,91875 ; remboursement 25,00 ; VAN − 0,64 à 3,5 % et + 0,11 à 4,0 % ; **t' = 3,92 %** (approximation : 5,25 % × 0,75 = 3,94 %).

Les frais sont plus élevés que ceux du prêt (2 % contre 1 %), mais étalés sur 7 ans et sur un capital qui reste entièrement dû jusqu'à l'échéance : leur effet sur le taux est de 0,35 point, contre 0,37 point pour le prêt.

**Avantage de l'avance remboursable (0,5 pt).** Sans intérêt, l'avance a un coût actuariel nul : 3,00 = 1,00 / (1 + t)^3 + 1,00 / (1 + t)^4 + 1,00 / (1 + t)^5 pour t = 0. Si SOLANÈRE avait emprunté ces 3,00 M€ à la Banque ESTRÉVAL, elle aurait supporté le coût après IS de 3,46 %. La valeur actuelle des remboursements à ce taux est :

1,00 / 1,0346^3 + 1,00 / 1,0346^4 + 1,00 / 1,0346^5 = 0,9030 + 0,8728 + 0,8436 = **2,62 M€**.

L'avantage est de 3,00 − 2,62 = **0,38 M€** (12,69 % de l'avance) : c'est une subvention implicite. Avec la subvention de 2,00 M€, l'aide équivaut à 2,38 M€ donnés le 1er janvier 2028, soit 14 % du coût de la ligne de frites.

**Conditions, avantages et limites de l'aide (0,5 pt).** Le fonds HYDRÉVAL est un financement public d'un investissement durable (programme 7.2.c) : il réduit la dette à lever et son coût, et il donne un signal favorable aux banques, aux assureurs et aux clients de la grande distribution attentifs à l'eau. Ses conditions créent cependant des risques :
- la subvention est conditionnelle : si la ligne ne réduit pas d'au moins 40 % l'eau prélevée par tonne, mesurée en 2029, SOLANÈRE devra reverser 2,00 M€, au moment où la dette sera la plus élevée ; l'objectif est technique et dépend aussi des volumes produits (une année de faibles récoltes réduit les tonnes et peut dégrader le ratio) ;
- l'avance devient immédiatement exigible si l'effectif de Montdidier baisse de plus de 10 % avant 2032 : c'est une contrainte sur l'automatisation et sur l'adaptation de l'emploi en cas de sécheresse ;
- un rapport annuel vérifié est exigé (coût de suivi) ;
- la décision n'est attendue qu'en octobre 2027 : le plan de financement doit prévoir le cas d'un refus (5,00 M€ de plus à financer) ;
- l'aide ne porte que sur la ligne de frites ; la ligne de flocons doit être financée sans elle.

**Comparaison des deux financements par dette (0,5 pt).** Avant IS, le prêt (4,62 %) coûte 0,63 point de moins que le placement privé (5,25 %) ; après IS, l'écart est de 0,46 point (3,46 % contre 3,92 %). Mais les deux coûts ne sont pas de même nature :
- le coût du prêt est calculé au taux variable de départ ; si l'Euribor monte, il monte ; couvert par le swap de la Banque ESTRÉVAL, il serait de 4,50 % par an hors frais, soit un coût actuariel avant IS de 4,87 % (question 3.5), encore inférieur à celui du placement privé ;
- le prêt est amortissable : 5,00 M€ de capital à rembourser chaque année de 2028 à 2032, en plus des dettes existantes, alors que le placement privé est remboursable en 2034, en une fois (risque de refinancement à l'échéance) ;
- la clause du prêt (3,00) est plus stricte que celle du placement privé (3,50).

**Réponses tolérées** : coûts actuariels à ± 0,02 point (interpolation) ; approximation du coût après IS par le coût avant IS × 0,75, signalée ; avance actualisée au coût après IS du placement privé (3,92 % : valeur actuelle 2,57 M€, avantage 0,43 M€) ou au coût avant IS du prêt (4,62 % : avantage 0,49 M€) si le choix est justifié ; frais déduits de l'impôt de l'année 1 plutôt qu'à la date 0, si l'hypothèse est écrite.

**Erreurs fréquentes**
- Ne retrancher que la subvention, ou traiter l'avance comme une subvention (avantage de 3,00 M€).
- Confondre le taux nominal (4,25 % ; 4,90 %) et le coût actuariel, ou oublier les frais.
- Appliquer l'économie d'impôt au remboursement du capital.
- `JUR-T04` — taux actuariel et tableau d'amortissement sont des acquis du DCG.
- `JUR-I01` — amortissement constant confondu avec une annuité constante (le décaissement baisse chaque année).

**Références** : F01 § 2 et § 3 (actualisation, tableaux d'amortissement) [S] ; programme 7.2.a et 7.2.c, guide p. 81-82 (coût actuariel, frais, coût net d'IS ; financements publics, financements durables) [V] ; F07 § 4.2 (supports de financement à moyen et long terme) [S].

---

### 3.2 Financement intermédié et financement direct (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Financement intermédié : la banque collecte des ressources, analyse et supporte le risque de crédit, produit une information privée dans une relation de long terme (crédit de campagne, comptes, centralisation), adapte le contrat (clause, renégociation possible) ; financement direct : SOLANÈRE emprunte auprès d'investisseurs (deux assureurs) qui achètent ses titres ; information à produire (documentation, information périodique), relation contractuelle plus rigide, accès à des durées longues et à des montants sans plafond de risque bancaire | 0,5 |
| 3.2-02 | Pour SOLANÈRE (146 M€ de chiffre d'affaires, cotée, non notée) : la cotation facilite l'information des investisseurs, mais la taille du placement (25 M€) et l'absence de note limitent le marché à quelques assureurs, d'où un coût plus élevé (5,25 % contre 4,62 %) et des frais plus lourds ; avantages : durée de 7 ans in fine, taux fixe, diversification des prêteurs, moindre dépendance au Crédit CAMPÉLIS, qui finance déjà la campagne et tient les comptes des trois sociétés ; le prêt reste adapté à une ETI régionale, mais il concentre le risque bancaire | 0,5 |

**Principe (0,5 pt).** Dans le **financement intermédié** (indirect), la Banque ESTRÉVAL prête des ressources qu'elle a collectées ; elle analyse le risque de SOLANÈRE, le supporte et le suit dans la durée. Elle produit une information privée, que SOLANÈRE ne publie pas, et peut renégocier le contrat si la situation change (dérogation à la clause, différé). Dans le **financement direct**, SOLANÈRE émet des obligations souscrites par des investisseurs finaux, MURÉVIA et OSTRELLE, qui placent l'épargne de leurs assurés à long terme. L'émetteur doit produire une information suffisante (documentation, comptes, rapports périodiques) ; le contrat est standardisé et plus difficile à renégocier, car il lie plusieurs porteurs ; en contrepartie, il donne accès à des durées longues et à des remboursements in fine que les banques accordent rarement.

**Application à SOLANÈRE (0,5 pt).** SOLANÈRE est une ETI cotée : elle publie déjà des comptes consolidés et une information permanente, ce qui réduit le coût d'information d'un placement privé. Elle n'est pas notée, et 25 M€ est un petit montant pour le marché obligataire : seuls quelques assureurs qui analysent eux-mêmes le crédit y souscrivent, d'où une prime (5,25 % contre 4,62 % avant IS) et des frais de 2 %. Le placement privé diversifie les prêteurs (le Crédit CAMPÉLIS finance déjà la campagne et tient les comptes des trois sociétés) et allonge la dette ; le prêt est moins cher, plus souple en cas de difficulté passagère (une banque qui connaît le cycle agricole peut accorder une dérogation), mais il concentre le risque bancaire et s'amortit vite. Pour une société de cette taille, les deux voies sont accessibles ; leur combinaison est fréquente.

**Réponses tolérées** : référence à l'asymétrie d'information (Akerlof, 1970) pour justifier la place des banques auprès des ETI ; mention du marché primaire et du rôle de la cotation dans l'accès au financement direct.

**Erreurs fréquentes**
- Présenter le placement privé comme un financement bancaire, ou les assureurs comme des intermédiaires de crédit qui transforment des dépôts.
- Oublier l'absence de notation et la taille, qui expliquent l'écart de coût (`JUR-T13`).
- Développer les règles de l'émission obligataire : les conditions sont des faits d'énoncé.

**Références** : F06 § 1 (financement direct et indirect, choix selon la taille, la maturité et la notation) [V guide p. 72 ; S] ; F10 (Akerlof, 1970) [V programme 5.1].

---

### 3.3 Capital, BPA, rentabilité des capitaux propres, endettement et clauses (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Actions nouvelles 25 000 000 / 12,50 = **2 000 000** ; 7 800 000 actions après ; CORVENNE 3 190 000 / 7 800 000 = **40,90 %** ; fonds 4,46 % ; autres actionnaires du flottant 29,00 % ; nouveaux actionnaires 25,64 % | 0,5 |
| 3.3-02 | Résultat net 2028 avant le coût des 25,00 M€ : (14,20 − 1,40) × 0,75 = 9,60 M€ ; prêt : 9,60 − 25,00 × 4,25 % × 0,75 = 8,80 M€, **BPA 1,52 €** ; placement privé : 9,60 − 25,00 × 4,90 % × 0,75 = 8,68 M€, **BPA 1,50 €** ; augmentation de capital : 9,60 / 7 800 000 = **1,23 €** | 1 |
| 3.3-03 | Rentabilité des capitaux propres (prévision centrale / sécheresse) : prêt **8,80 % / 5,80 %** ; placement privé **8,68 % / 5,68 %** ; augmentation de capital **7,68 % / 5,28 %** (capitaux propres pro forma 100,00 ou 125,00 M€) | 0,5 |
| 3.3-04 | DFN pro forma : 30,00 + 30,00 − 2,00 = **58,00 M€** avec dette, **33,00 M€** avec l'augmentation de capital ; DFN / capitaux propres **0,58** et **0,26** ; DFN / EBITDA : **2,64** et **1,50** (prévision centrale), **3,22** et **1,83** (sécheresse) | 0,5 |
| 3.3-05 | Clause du prêt (3,00) respectée dans la prévision centrale, **franchie en sécheresse** (3,22) ; clause du placement privé (3,50) respectée dans les deux cas ; seuil du Crédit CAMPÉLIS franchi en sécheresse avec les deux dettes ; dette supplémentaire maximale : 3,00 × 18,00 − 33,00 = **21,00 M€**, soit 4,00 M€ de moins que le besoin | 0,5 |
| 3.3-06 | Effet de levier : la rentabilité économique après IS (6,74 % ; 4,84 % en sécheresse) dépasse le coût net de la nouvelle dette (3,19 % pour le prêt, 3,68 % pour le placement privé) : la dette relève la rentabilité des capitaux propres et le BPA ; mais elle amplifie leur baisse en sécheresse (− 3,00 points contre − 2,40 points), consomme la capacité d'endettement et expose SOLANÈRE à l'exigibilité anticipée et au resserrement du crédit de campagne l'année où le stock coûte le plus cher ; un BPA plus élevé ne prouve pas une création de valeur | 1 |

**Augmentation de capital et répartition du capital (0,5 pt).** Le prix d'émission de 12,50 € donne 25 000 000 / 12,50 = **2 000 000 actions nouvelles**, soit 7 800 000 actions après l'opération. Ni CORVENNE ni le fonds ne souscrivent :

| Actionnaire | Actions | Part avant | Part après |
|---|---:|---:|---:|
| CORVENNE | 3 190 000 | 55,00 % | **40,90 %** |
| Fonds LAVARÈDE Valeurs moyennes | 348 000 | 6,00 % | 4,46 % |
| Autres actionnaires du flottant | 2 262 000 | 39,00 % | 29,00 % |
| Nouveaux actionnaires | 2 000 000 | — | 25,64 % |
| **Total** | **7 800 000** | 100 % | 100 % |

CORVENNE perd la majorité ; les minoritaires historiques passent de 45,00 % à 33,46 %.

**BPA prévu pour 2028 (1 pt).** Convention de l'annexe 3.6 : chaque solution porte sur 25,00 M€, en année pleine, frais négligés.

| Prévision centrale 2028 (M€) | Prêt | Placement privé | Augmentation de capital |
|---|---:|---:|---:|
| Résultat opérationnel | 14,20 | 14,20 | 14,20 |
| Coût de l'endettement des dettes existantes | − 1,40 | − 1,40 | − 1,40 |
| Intérêts des nouvelles dettes | 25,00 × 4,25 % = − 1,06 | 25,00 × 4,90 % = − 1,23 | — |
| Résultat avant impôt | 11,74 | 11,58 | 12,80 |
| Impôt à 25 % | − 2,93 | − 2,89 | − 3,20 |
| **Résultat net** | **8,80** | **8,68** | **9,60** |
| Nombre d'actions | 5 800 000 | 5 800 000 | 7 800 000 |
| **BPA** | **1,52 €** | **1,50 €** | **1,23 €** |

L'augmentation de capital réduit le BPA de 19 % par rapport au prêt : le résultat qu'elle épargne (pas d'intérêts) ne compense pas les 34 % d'actions supplémentaires. Pour information, dans le scénario de sécheresse : 1,00 € (prêt), 0,98 € (placement privé), 0,85 € (augmentation de capital).

**Rentabilité des capitaux propres (0,5 pt).** Capitaux propres pro forma : 100,00 M€ avec une dette, 100,00 + 25,00 = 125,00 M€ avec l'augmentation de capital. Dans le scénario de sécheresse, le résultat net avant le coût du financement est (10,20 − 1,40) × 0,75 = 6,60 M€.

| | Prêt | Placement privé | Augmentation de capital |
|---|---:|---:|---:|
| Résultat net, prévision centrale | 8,80 | 8,68 | 9,60 |
| Rentabilité des capitaux propres, prévision centrale | **8,80 %** | **8,68 %** | **7,68 %** |
| Résultat net, sécheresse | 5,80 | 5,68 | 6,60 |
| Rentabilité des capitaux propres, sécheresse | **5,80 %** | **5,68 %** | **5,28 %** |
| Écart entre les deux scénarios | − 3,00 points | − 3,00 points | − 2,40 points |

**Rapports d'endettement (0,5 pt).** DFN pro forma au 1er janvier 2028 = 30,00 (DFN avant programme) + 30,00 (programme payé) − 2,00 (subvention) − montant levé en capital. L'avance de 3,00 M€ et la nouvelle dette sont des dettes : les fonds qu'elles procurent sont dépensés dans le programme et ne réduisent pas la DFN.

| | Dette (prêt ou placement privé) | Augmentation de capital |
|---|---:|---:|
| DFN pro forma | **58,00** | **33,00** |
| Capitaux propres pro forma | 100,00 | 125,00 |
| DFN / capitaux propres | **0,58** | **0,26** |
| DFN / EBITDA, prévision centrale (22,00) | **2,64** | **1,50** |
| DFN / EBITDA, sécheresse (18,00) | **3,22** | **1,83** |

**Clauses et dette maximale (0,5 pt).** Avec le prêt, la clause de la Banque ESTRÉVAL (3,00) est respectée dans la prévision centrale (2,64) mais **franchie dans le scénario de sécheresse** (3,22) : la banque pourrait exiger le remboursement anticipé. Avec le placement privé, la clause des assureurs (3,50) reste respectée dans les deux cas ; mais le Crédit CAMPÉLIS, qui regarde la dette d'une année sèche, réduirait le crédit de campagne et relèverait sa marge dès 3,00. La dette supplémentaire compatible avec 3,00 en sécheresse est **3,00 × 18,00 − 33,00 = 21,00 M€** : il manque **4,00 M€**, à trouver en fonds propres, en autofinancement ou par un programme réduit. Les clauses sont contractuelles, propres à chaque prêteur, et non des ratios réglementaires. Elles sont testées au 31 décembre, quand la DFN comprend les crédits de campagne qui financent le stock : le ratio est mesuré au plus haut du cycle.

**Effet de levier et risque (1 pt).** La rentabilité économique après IS de 2028 est 14,20 × 0,75 / 158,00 = 6,74 % dans la prévision centrale (actif économique = capitaux propres + DFN = 158,00 M€ dans les trois solutions) et 10,20 × 0,75 / 158,00 = 4,84 % en sécheresse. Le coût net de la nouvelle dette est 4,25 % × 0,75 = 3,19 % (prêt) ou 4,90 % × 0,75 = 3,68 % (placement privé). Tant que la rentabilité économique dépasse ce coût, l'endettement relève la rentabilité des capitaux propres (8,80 % contre 7,68 %) et le BPA (1,52 € contre 1,23 €) : c'est l'effet de levier. Le levier amplifie aussi la variabilité : en sécheresse, la rentabilité des capitaux propres perd 3,00 points avec la dette, contre 2,40 points avec l'augmentation de capital, et l'écart entre les deux solutions se réduit à 0,52 point. Surtout, la dette consomme la capacité d'endettement : le rapport DFN / EBITDA passe de 1,50 à 2,64, et une sécheresse comme celle de 2026 suffit à franchir la clause, l'année même où le stock coûte le plus cher et où le crédit de campagne est le plus nécessaire. Le supplément de BPA rémunère ce risque supplémentaire des actionnaires : il ne prouve pas que la dette crée de la valeur.

**Réponses tolérées** : capitaux propres pro forma augmentés du résultat de 2028, si l'hypothèse est écrite ; rapports calculés sans l'avance (55,00 et 30,00 M€) si le candidat la traite à part en le disant (la conclusion sur la clause change alors : 3,06 en sécheresse, toujours franchie) ; BPA en sécheresse non demandé mais valorisé dans l'item 3.3-06.

**Erreurs fréquentes**
- Diviser le résultat de la solution 3 par 5 800 000 actions, ou ajouter 25,00 M€ à la DFN dans la solution 3.
- Oublier le paiement du programme dans la DFN pro forma, ou retrancher la nouvelle dette (les fonds sont dépensés).
- Calculer les intérêts après impôt deux fois, ou oublier l'impôt sur les intérêts.
- Présenter la clause comme une obligation réglementaire.
- `JUR-T07` — un tableau par solution est attendu ; `JUR-T03` — l'annexe 3.2 et l'annexe 3.6 sont à croiser.

**Références** : F05 § 3 et § 4 (BPA, dilution du contrôle et du BPA) [V guide p. 68 ; S] ; F05 § 1.3 (effet de levier et risque) [V guide p. 70] ; programme 7.2.b, guide p. 82 (levier, capacité de remboursement) [V].

---

### 3.4 Contrôle de CORVENNE, coût pour les minoritaires, théories et plan de financement (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Pour garder 55 % : 55 % × 2 000 000 = 1 100 000 actions, soit **13,75 M€** ; nombre maximal d'actions nouvelles qui ne fait pas passer CORVENNE sous 50 % : 3 190 000 / 50 % − 5 800 000 = **580 000** actions (7,25 M€ ; 579 999 accepté si le candidat vise une majorité stricte) ; décote 1 − 12,50 / 15,20 = **17,76 %** | 0,5 |
| 3.4-02 | Refus de CORVENNE : elle ne peut pas souscrire (13,75 M€) et passerait à 40,90 % ; la majorité garantit aux producteurs le débouché de leurs récoltes et la maîtrise des prix des contrats (stratégie de gestion du capital : contrôle plutôt que croissance du BPA) ; coût pour les minoritaires : dilution de 45,00 % à 33,46 %, BPA réduit de 19 %, actions vendues 17,76 % sous le cours aux nouveaux investisseurs (transfert de valeur aux souscripteurs si le prix est inférieur à la valeur), annonce lue comme un signal défavorable | 0,5 |
| 3.4-03 | Financement hiérarchique (Myers et Majluf, 1984) : à cause de l'asymétrie d'information, l'autofinancement d'abord, puis la dette, et l'émission d'actions en dernier, car elle est lue comme le signe d'une action surévaluée et fait baisser le cours ; ici, la dette et l'aide publique passent avant les actions, et l'émission à prix décoté confirme le coût informationnel | 0,5 |
| 3.4-04 | Théorie du compromis (Myers, 1977) : endettement cible qui équilibre l'économie d'impôt (25 % des intérêts : 0,27 M€ en 2028 pour le prêt) et les coûts de difficultés financières (clause franchie en sécheresse, crédit de campagne réduit, clients et producteurs inquiets) ; pour un transformateur exposé aux sécheresses, l'optimum se situe sous 3,00 fois l'EBITDA d'une année sèche | 0,5 |
| 3.4-05 | Plan recommandé : aide HYDRÉVAL 5,00 M€ ; dette de l'ordre de 20 M€ (prêt de la Banque ESTRÉVAL couvert par le swap, ou placement privé si la durée est préférée) ; augmentation de capital limitée à environ 5 M€ (400 000 actions, CORVENNE à 51,45 %), ou un complément équivalent en autofinancement ; rapport DFN / EBITDA de 2,41 (2,94 en sécheresse) ; conditions : décision du fonds HYDRÉVAL, prix d'émission discuté avec le fonds LAVARÈDE, solution de repli si l'aide est refusée | 1 |

**Calculs (0,5 pt).** Pour garder 55 % du capital, CORVENNE devrait souscrire 55 % des actions nouvelles : 1 100 000 actions × 12,50 € = **13,75 M€**, qu'elle n'a pas. Pour ne pas passer sous 50 % sans souscrire, il faut 3 190 000 / (5 800 000 + n) ≥ 50 %, soit n ≤ 3 190 000 / 0,50 − 5 800 000 = **580 000 actions** (7,25 M€ au prix de 12,50 €) ; à 580 000 actions, elle détiendrait exactement 50,00 % ; une majorité stricte supposerait 579 999 actions au plus. Le prix d'émission de 12,50 € fait ressortir une **décote de 1 − 12,50 / 15,20 = 17,76 %** sur le cours du 30 avril 2027.

**Pourquoi CORVENNE refuse et ce que l'émission coûterait aux minoritaires (0,5 pt).** La gestion du capital est un choix stratégique : CORVENNE détient SOLANÈRE pour assurer un débouché à 80 % des pommes de terre achetées et pour peser sur le prix des contrats de culture, non pour maximiser le BPA. À 40,90 %, elle ne serait plus majoritaire ; un autre actionnaire ou un groupe d'actionnaires pourrait un jour peser sur le conseil et sur les achats. Elle ne peut pas suivre l'émission : après trois sécheresses, sa trésorerie sert à ses silos et à ses adhérents. Pour les minoritaires, l'émission à 12,50 € a un triple coût : leur part passe de 45,00 % à 33,46 % ; le BPA prévu de 2028 baisse de 19 % (1,23 € contre 1,52 €) ; les actions sont vendues 17,76 % sous le cours à de nouveaux investisseurs, ce qui leur transfère de la valeur si ce prix est inférieur à la valeur de l'action. L'émission élargirait certes le flottant et la liquidité du titre, ce que reconnaît le fonds LAVARÈDE, mais celui-ci refuse ce prix.

**Financement hiérarchique (0,5 pt).** Selon Myers et Majluf (1984), les dirigeants en savent plus que les investisseurs sur la valeur de l'entreprise : une émission d'actions est interprétée comme le signe que l'action est surévaluée, et son annonce fait baisser le cours. Les entreprises préfèrent donc l'autofinancement, puis la dette, et n'émettent des actions qu'en dernier recours. En l'espèce, SOLANÈRE commence par l'aide publique (la moins chère), puis la dette ; l'émission à 12,50 €, avec une décote de 17,76 %, illustre le prix que le marché ferait payer à une émission ouverte.

**Théorie du compromis (0,5 pt).** Selon la théorie du compromis (Myers, 1977, attribution retenue par le programme), l'endettement optimal équilibre l'avantage fiscal de la dette (les intérêts réduisent l'impôt : 25,00 × 4,25 % × 25 % = 0,27 M€ en 2028 avec le prêt) et les coûts de difficultés financières : clause franchie, remboursement anticipé, crédit de campagne réduit et plus cher, inquiétude des clients et des producteurs. Pour SOLANÈRE, dont l'EBITDA baisse de 4,00 M€ lors d'un été sec, ces coûts deviennent importants dès que la DFN dépasse 3,00 fois l'EBITDA d'une année sèche : la cible est un endettement supplémentaire d'au plus 21,00 M€, avec une marge de sécurité.

**Plan de financement recommandé (1 pt).** Les deux théories et les contraintes du cas conduisent au même plan :

| Ressource | Montant |
|---|---:|
| Subvention du fonds HYDRÉVAL | 2,00 M€ |
| Avance remboursable du fonds HYDRÉVAL | 3,00 M€ |
| Prêt de la Banque ESTRÉVAL, couvert par le swap | 20,00 M€ |
| Augmentation de capital ouverte au marché (400 000 actions à 12,50 €) | 5,00 M€ |
| **Total** | **30,00 M€** |

Avec ce plan, la DFN pro forma est 30,00 + 30,00 − 2,00 − 5,00 = 53,00 M€, soit 2,41 fois l'EBITDA de la prévision centrale et 2,94 fois celui d'une année de sécheresse : la clause et le critère du Crédit CAMPÉLIS sont respectés, avec une faible marge. CORVENNE garde 3 190 000 / 6 200 000 = 51,45 % du capital ; le BPA prévu de 2028 est de 1,44 € avec le prêt couvert (résultat net 8,93 M€). Le prêt couvert est préféré au placement privé pour son coût (4,50 % fixe hors frais, contre 4,90 %) et pour la relation bancaire, à condition d'en suivre les échéances (4,00 M€ par an). Le plan est soumis à trois conditions : la décision du fonds HYDRÉVAL en octobre 2027 (sinon, 5,00 M€ de plus, à couvrir par un report d'une partie de la ligne de flocons plutôt que par la dette) ; un prix d'émission discuté avec le fonds LAVARÈDE (une petite émission peut être placée avec une décote plus faible) ; une politique de dividende qui laisse un autofinancement suffisant, premier rang du financement hiérarchique.

**Réponses tolérées** : toute combinaison qui respecte à la fois le contrôle de CORVENNE (moins de 580 000 actions nouvelles) et le rapport de 3,00 en sécheresse, justifiée par les théories : par exemple 21,00 M€ de dette et 4,00 M€ de capital (320 000 actions, CORVENNE à 52,12 %, rapport de 3,00 en sécheresse, sans marge) ; placement privé retenu pour sa durée et sa clause plus souple ; financement de 4 à 5 M€ par l'autofinancement ou par un programme réduit plutôt que par des actions, si le candidat l'explique. Une recommandation de tout financer par dette est acceptée seulement si elle traite le risque de franchissement de la clause.

**Erreurs fréquentes**
- Inverser l'ordre du financement hiérarchique (actions avant dette), ou l'attribuer à Modigliani et Miller.
- Confondre la théorie du compromis (endettement cible) et le financement hiérarchique (pas de cible).
- Développer les règles de l'augmentation de capital ou des droits des actionnaires : les conditions sont des faits d'énoncé.
- `JUR-T14` — théories mal maîtrisées ; `JUR-T02` — donnée du cas, théorie et recommandation dans chaque paragraphe.

**Références** : F10 (Myers et Majluf, 1984 ; Myers, 1977, attribution du programme 7.2) [V programme] ; F05 § 4 (dilution du contrôle sans souscription) [V guide p. 68] ; programme 4.2.a, guide p. 68 (gestion du capital, dilution) [V].

---

### 3.5 Swap de taux, prêt couvert et valeur des obligations (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Intérêts du trimestre (91 jours, 25 000 000 €) : 221 180,56 € (1,90 %), 268 576,39 € (2,65 %), 353 888,89 € (4,00 %) ; différentiel du swap : **− 63 194,44 €** (versé), **− 15 798,61 €** (versé), **+ 69 513,89 €** (reçu) ; coût net **284 375,00 €** dans les trois cas ; taux effectif **4,50 %** | 1 |
| 3.5-02 | Le swap transforme le prêt variable en prêt à taux fixe de 2,90 % + 1,60 % = 4,50 % : budget connu, BPA protégé ; il supprime le gain d'une baisse des taux (4,50 % au lieu de 3,50 %) ; il coûte 0,25 point de plus que le taux variable de départ ; risques résiduels : contrepartie, marge du prêt, remboursement anticipé (le swap devrait être dénoué à sa valeur de marché) | 0,5 |
| 3.5-03 | Comparaison : prêt couvert 4,50 % par an hors frais (coût actuariel 4,87 % avant IS, 3,65 % après IS, non exigé) contre 4,90 % pour le placement privé (5,25 % ; 3,92 %) ; le placement privé garde l'avantage de la durée (7 ans in fine) et d'une clause plus souple, le prêt couvert celui du coût ; couverture partielle possible | 0,5 |
| 3.5-04 | Obligations : prix 100,00 % au taux de 4,90 % ; duration **6,09 ans** ; sensibilité **− 5,81** ; variation estimée − 5,81 % pour + 1 point ; prix exact à 5,90 % : **94,40 %** (− 5,60 %) ; perte de valeur de 1,40 M€ sur 25,00 M€ | 0,5 |
| 3.5-05 | Relation inverse taux-valeur : le coupon reste 4,90 % quand le marché offre 5,90 % ; les flux futurs, actualisés à un taux plus élevé, valent moins ; les assureurs qui gardent les titres jusqu'en 2034 ne réalisent pas la perte mais supportent un coût d'opportunité ; pour SOLANÈRE, la dette à taux fixe vaut moins (gain d'opportunité, coût figé) ; à l'inverse, une baisse des taux la renchérit relativement | 0,5 |

**Swap (1 pt).** Base Exact/360, 91 jours, nominal égal au capital restant dû de 25 000 000 €. Intérêts du prêt = 25 000 000 × (taux variable + 1,60 %) × 91 / 360 ; différentiel reçu par SOLANÈRE = 25 000 000 × (taux variable − 2,90 %) × 91 / 360 (négatif : versé).

| Scénario | Baisse | Stabilité | Hausse |
|---|---:|---:|---:|
| Taux variable du trimestre | 1,90 % | 2,65 % | 4,00 % |
| Intérêts du prêt (taux variable + 1,60 %) | 221 180,56 € | 268 576,39 € | 353 888,89 € |
| Différentiel du swap (reçu + / versé −) | − 63 194,44 € | − 15 798,61 € | + 69 513,89 € |
| **Coût net** | **284 375,00 €** | **284 375,00 €** | **284 375,00 €** |
| **Taux effectif** | **4,50 %** | **4,50 %** | **4,50 %** |

Exemple du scénario de hausse : 25 000 000 × 5,60 % × 91 / 360 = 353 888,89 € d'intérêts ; SOLANÈRE reçoit 25 000 000 × (4,00 % − 2,90 %) × 91 / 360 = 69 513,89 € ; coût net 284 375,00 €, soit 284 375,00 / (25 000 000 × 91 / 360) = 4,50 %.

**Ce que le swap change (0,5 pt).** Payeur du taux fixe et receveur de l'Euribor 3 mois, SOLANÈRE transforme son prêt variable en un prêt à taux fixe de 2,90 % + 1,60 % = **4,50 %**, quel que soit l'Euribor : la charge d'intérêts est connue (1,125 M€ en 2028, BPA prévu de 1,51 € au lieu de 1,52 €) et la hausse des taux, que redoute la Banque ESTRÉVAL, ne peut plus menacer le résultat ni la clause. En contrepartie, SOLANÈRE renonce au gain d'une baisse : à 1,90 %, elle paierait 4,50 % au lieu de 3,50 %. Le swap coûte aujourd'hui 0,25 point (2,90 % contre 2,65 %) : c'est le prix de la sécurité, qui reflète la hausse des taux courts attendue par le marché. Aucune prime n'est payée, mais le swap reste un engagement ferme pendant 5 ans : si le prêt était remboursé par anticipation (clause franchie), il faudrait le dénouer à sa valeur de marché, qui dépend des taux du moment. Il reste aussi un risque de contrepartie (la Banque ESTRÉVAL) et la marge du prêt n'est pas couverte (elle pourrait être relevée en cas de difficulté).

**Comparaison avec le placement privé (0,5 pt).** Couvert, le prêt coûte 4,50 % par an hors frais, et son coût actuariel avec les frais de 1 % est de 4,87 % avant IS (3,65 % après IS), contre 5,25 % (3,92 %) pour le placement privé à 4,90 %. Les deux financements deviennent à taux fixe ; le prêt couvert reste moins cher, mais s'amortit en 5 ans et porte la clause la plus stricte ; le placement privé fixe le taux pour 7 ans sans amortissement. Une couverture partielle (par exemple la moitié du nominal) garderait une partie du gain d'une baisse des taux, au prix d'un risque résiduel.

**Valeur des obligations (0,5 pt).** Au taux de marché de 4,90 %, égal au coupon, l'obligation vaut 100,00 % du nominal. Duration (moyenne des dates des flux pondérée par leurs valeurs actuelles) : **6,09 ans** ; sensibilité = − 6,09 / 1,049 = **− 5,81**. Une hausse d'un point fait baisser le prix d'environ 5,81 %. Le prix exact à 5,90 % est :

P = 4,90 × [1 − 1,059^−7] / 0,059 + 100 × 1,059^−7 = **94,40 %**, soit − 5,60 %.

L'écart entre − 5,81 % et − 5,60 % vient de la courbure de la relation prix-taux, que la sensibilité ne mesure pas. Sur 25,00 M€ de nominal, MURÉVIA et OSTRELLE perdraient 1,40 M€ de valeur.

**Pourquoi la valeur baisse et ce que cela signifie pour SOLANÈRE (0,5 pt).** Les flux d'une obligation à taux fixe ne changent pas : quand le marché offre 5,90 % pour un risque comparable, plus personne n'achète un titre qui rapporte 4,90 % au prix de 100 ; son prix baisse jusqu'à ce que son rendement rejoigne celui du marché. La perte est d'autant plus forte que la durée est longue (sensibilité de 5,81 pour 7 ans). MURÉVIA et OSTRELLE, qui veulent garder les titres jusqu'en 2034, ne réalisent pas cette perte, mais ils supportent un coût d'opportunité (placer à 5,90 % aurait été possible) et, s'ils devaient vendre, ils la constateraient. Pour SOLANÈRE, la dette à taux fixe est protégée de la hausse : son coût est figé à 4,90 %, et la valeur de marché de sa dette baisse (gain d'opportunité) ; à l'inverse, si les taux baissaient, elle paierait plus que le marché sans pouvoir rembourser à moindre coût.

**Réponses tolérées** : différentiel exprimé du point de vue de la banque, si le sens est expliqué ; présentation du coût net comme « taux fixe du swap + marge » sans le détail des trois scénarios pour l'item 3.5-02 (pas pour 3.5-01) ; duration à 6,09 ou 6,1 ans, y compris par la formule d'une obligation émise au pair, D = (1 + y) / y × [1 − (1 + y)^−7] = 6,09 ; prix exact de 94,40 % obtenu par les facteurs d'actualisation année par année.

**Erreurs fréquentes**
- Inverser le sens du différentiel : le payeur de fixe **reçoit** quand le variable dépasse le taux fixe.
- Oublier la marge du prêt dans le taux effectif (2,90 % au lieu de 4,50 %), ou calculer en base 365 ou en 3/12 sans le dire.
- Annoncer une hausse de la valeur des obligations quand les taux montent.
- Confondre la perte de valeur des assureurs avec un coût supplémentaire pour SOLANÈRE.

**Références** : F07 § 2.1 (relation inverse, duration, sensibilité) et § 2.2 (swap de taux, sens du différentiel) [V programme 6.2 ; guide p. 77-78 ; S formules] ; F07 § 2.4 (choix d'une couverture : coût, flexibilité, risque résiduel) [V guide p. 78] ; F11 (Euribor 3 mois de 2,65 %, hypothèse d'énoncé cohérente avec la moyenne de septembre 2026) [V].

---

### 3.6 Financement du stock de la campagne 2027-2028 (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Capitaux-jours : 12 × 61 + 24 × 30 + 16 × 91 + 6 × 122 = **3 640 M€ × jours** (besoin moyen 11,97 M€ sur 304 jours) ; offre A : intérêts 3 640 × 3,70 % / 360 = **374,11 k€** ; commission d'engagement 24,00 × 0,30 % × 304 / 360 = **60,80 k€** ; coût **434,91 k€** ; taux effectif **4,30 %** | 0,5 |
| 3.6-02 | Offre B : intérêts 3 640 × 2,90 % / 360 = **293,22 k€** ; garantie 24,00 × 0,40 % × 304 / 360 = 81,07 k€ ; frais fixes 80,00 k€ ; coût **454,29 k€** ; taux effectif **4,49 %** ; 19,38 k€ de plus que l'offre A : l'économie de marge (80,89 k€) est absorbée par la garantie et les frais fixes | 0,5 |
| 3.6-03 | Offre C : encours financé limité à 15,00 M€ : 12 × 61 + 15 × 30 + 15 × 91 + 6 × 122 = 3 279 ; intérêts 3 279 × 3,85 % / 360 = **350,67 k€** ; commission 0,15 % × 100,00 M€ = **150,00 k€** ; coût **500,67 k€** ; taux effectif **5,50 %** ; 9,00 M€ du pic de novembre restent à financer | 0,5 |
| 3.6-04 | Recommandation : crédit de campagne confirmé de 24,00 M€ comme financement principal (le moins cher, tiré au jour le jour, adapté à un besoin saisonnier qui passe de 24 à 6 M€, sans notation ni montant minimal) ; titres négociables à réexaminer si SOLANÈRE est notée (coût de 413,22 k€, 4,09 %, sans garantie) et si le besoin stable augmente ; cession de créances gardée en solution de secours (Crédit CAMPÉLIS qui réduirait son crédit en sécheresse), à cause de son coût et de sa limite | 0,5 |

**Capitaux-jours (base commune).** Les intérêts courent sur l'encours financé, période par période : Σ besoin × jours = 12,00 × 61 + 24,00 × 30 + 16,00 × 91 + 6,00 × 122 = 732 + 720 + 1 456 + 732 = **3 640 M€ × jours**, soit un encours moyen de 3 640 / 304 = 11,97 M€ pendant la campagne.

| Offre | Intérêts | Commissions et frais | **Coût** | Encours financé (Σ encours × jours) | **Taux effectif** |
|---|---:|---:|---:|---:|---:|
| A crédit de campagne confirmé (2,65 % + 1,05 % = 3,70 %) | 3 640 × 3,70 % / 360 = 374,11 k€ | engagement : 24,00 × 0,30 % × 304 / 360 = 60,80 k€ | **434,91 k€** | 3 640 | **4,30 %** |
| B titres négociables à court terme garantis (2,65 % + 0,25 % = 2,90 %) | 3 640 × 2,90 % / 360 = 293,22 k€ | garantie : 24,00 × 0,40 % × 304 / 360 = 81,07 k€ ; frais fixes : 80,00 k€ | **454,29 k€** | 3 640 | **4,49 %** |
| C cession de créances (2,65 % + 1,20 % = 3,85 %), dans la limite de 15,00 M€ | 3 279 × 3,85 % / 360 = 350,67 k€ | commission : 0,15 % × 100,00 M€ = 150,00 k€ | **500,67 k€** | 3 279 | **5,50 %** |

Taux effectif = coût / (Σ encours × jours / 360) ; par exemple, pour l'offre A, 434,91 / (3 640 / 360 × 1 000) = 4,30 %. L'offre C ne couvre pas tout le besoin : 9,00 M€ en novembre et 1,00 M€ de décembre à février restent à financer (361 M€ × jours), en plus de son coût.

**Recommandation (0,5 pt).** Le besoin est **saisonnier** : il quadruple entre juin et novembre, puis décroît au fil des ventes. Il lui faut un financement souple, tiré au jour le jour. Le **crédit de campagne confirmé** du Crédit CAMPÉLIS est le moins cher (434,91 k€, 4,30 %) et le mieux adapté : il ne coûte des intérêts que sur les sommes tirées et sa commission d'engagement rémunère la certitude de disposer de 24 M€ au pic. Les **titres négociables à court terme** sont moins chers en taux (marge de 0,25 % contre 1,05 %), mais pour une société de la taille de SOLANÈRE, non notée, la garantie bancaire obligatoire et les frais fixes absorbent l'économie : 19,38 k€ de plus, pour un financement qui reste adossé à la même banque et qui dépend de l'ouverture du marché (en période de tension, les investisseurs ne renouvellent pas les titres à l'échéance). Ils deviendraient intéressants si SOLANÈRE obtenait une note suffisante (sans garantie : 293,22 + 80,00 + 40,00 = 413,22 k€, soit 4,09 %) ou si son besoin stable augmentait ; la note est incertaine et son coût s'ajoute chaque année. La **cession de créances** est la plus chère (5,50 %), ne couvre que 15,00 M€ et touche la relation avec les clients de la grande distribution et de la restauration ; elle a l'avantage d'un financement qui suit les ventes et transfère le risque d'impayé. Elle peut être gardée en réserve, si le Crédit CAMPÉLIS réduisait son crédit l'année d'une sécheresse (question 3.3), plutôt que retenue d'emblée.

**Réponses tolérées** : capitaux-jours calculés mois par mois (même résultat) ; commission d'engagement ou de garantie calculée sur 10 mois (24,00 × 0,30 % × 10 / 12 = 60,00 k€), si l'écart à la base Exact/360 est signalé ; combinaison crédit de campagne et titres négociables pour la partie stable, si le candidat montre qu'elle n'est rentable qu'avec un besoin stable plus élevé ou une note ; coût de l'offre C augmenté du financement du besoin restant par le crédit de campagne (le coût total dépasse alors celui de l'offre A).

**Erreurs fréquentes**
- Calculer les intérêts sur le pic de 24,00 M€ pendant toute la campagne, ou sur la somme des besoins.
- Oublier la garantie bancaire ou les frais fixes des titres négociables, ou la limite de 15,00 M€ de l'offre C.
- Désigner les NEU CP par leur ancien nom (ex-billets de trésorerie) comme s'il était encore en usage.
- `JUR-T13` — recommandation non reliée à la saisonnalité, à la taille et à la notation.

**Références** : F07 § 4.2 (financements à court terme, critères : coût, souplesse, garanties) [S] ; F01 § 7 (base Exact/360) [S] ; F99 (NEU CP, ex-billets de trésorerie) [S].

---

### 3.7 Centralisation physique des soldes (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Sans centralisation : SOLANÈRE SA − 197,64 k€, Déshydratés + 34,05 k€, Croustilles − 13,84 k€, total **− 177,43 k€** ; soldes nets du groupe 0 (1er semestre) et − 1 800 k€ (2e semestre) ; avec centralisation : − 1 800 × 5,40 % × 184 / 360 = − 49,68 k€, − 61,68 k€ frais compris ; économie **115,75 k€** par an | 0,5 |
| 3.7-02 | Conditions : convention de trésorerie entre les trois sociétés, rémunération des avances aux conditions de marché, compte centralisateur et système d'information, accord de la banque ; limites : l'économie vient de l'écart entre taux débiteur et créditeur et disparaît si les soldes sont de même signe ; elle ne réduit pas le besoin de financement du groupe (stock de campagne) ; dépendance à une seule banque ; autonomie des filiales ; la centralisation ne s'étend pas à CORVENNE, actionnaire extérieur au groupe | 0,5 |

**Économie (0,5 pt).** Intérêts = solde × taux × jours / 360 ; un solde débiteur paie 5,40 %, un solde créditeur reçoit 1,20 %.

| Société (k€) | 1er semestre (181 j) | 2e semestre (184 j) | Total 2026 |
|---|---:|---:|---:|
| SOLANÈRE SA | − 2 400 × 5,40 % × 181 / 360 = − 65,16 | − 4 800 × 5,40 % × 184 / 360 = − 132,48 | − 197,64 |
| SOLANÈRE Déshydratés | + 3 000 × 1,20 % × 181 / 360 = + 18,10 | + 2 600 × 1,20 % × 184 / 360 = + 15,95 | + 34,05 |
| SOLANÈRE Croustilles | − 600 × 5,40 % × 181 / 360 = − 16,29 | + 400 × 1,20 % × 184 / 360 = + 2,45 | − 13,84 |
| **Sans centralisation** | | | **− 177,43** |
| Solde net du groupe | 0 | − 1 800 | |
| Avec centralisation | 0 | − 1 800 × 5,40 % × 184 / 360 = − 49,68 | − 49,68 |
| Frais du service | | | − 12,00 |
| **Avec centralisation, frais compris** | | | **− 61,68** |

Économie annuelle : − 61,68 − (− 177,43) = **115,75 k€**. Au premier semestre, les découverts de SOLANÈRE SA et de SOLANÈRE Croustilles sont entièrement couverts par l'excédent de SOLANÈRE Déshydratés : le groupe cesse de payer 5,40 % sur 3 000 k€ tout en ne recevant que 1,20 % sur un montant égal.

**Conditions et limites (0,5 pt).** La centralisation physique suppose une convention entre les trois sociétés, dont les conditions sont des faits d'énoncé, des avances rémunérées à des conditions de marché (l'excédent de SOLANÈRE Déshydratés finance SOLANÈRE SA), un compte centralisateur, un outil de suivi quotidien et l'accord du Crédit CAMPÉLIS. L'économie ne vient que de l'écart entre le taux débiteur et le taux créditeur (4,20 points) appliqué aux soldes qui se compensent : elle disparaîtrait si les trois sociétés étaient débitrices en même temps, ce qui peut arriver au plus fort de la campagne. Elle ne réduit pas le besoin de financement du groupe, qui reste à couvrir par le crédit de campagne ; elle renforce la dépendance au Crédit CAMPÉLIS ; elle réduit l'autonomie de gestion des filiales, dont les dirigeants doivent accepter de voir leur trésorerie remonter chaque soir. Elle concerne les trois sociétés du groupe, filiales détenues à 100 % ; CORVENNE, actionnaire extérieur au groupe, n'en fait pas partie. Une centralisation notionnelle (sans virements, intérêts calculés sur le solde fusionné) donnerait un résultat voisin, si la banque l'accepte.

**Réponses tolérées** : montants arrondis au millier d'euros (− 198, + 34, − 14, total − 177 ; économie 116 k€) ; économie présentée avant frais (127,75 k€) puis après frais.

**Erreurs fréquentes**
- Calculer les intérêts sur la somme des soldes de l'année sans distinguer les semestres, ou appliquer le taux débiteur aux soldes créditeurs.
- Oublier les frais du service.
- Développer les règles des conventions entre sociétés : elles ne sont pas demandées.

**Références** : F07 § 4.1 (centralisation physique et notionnelle, avantages et prérequis) [V guide p. 77 pour l'exclusion du traitement juridique ; S] ; programme 6.1.a [V].
