# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 74 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F05 ingénierie financière, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (équilibre du bilan, MEDAF avec primes, CMPC avec et sans primes, réendettement du bêta fourni, business plan et flux de trésorerie disponibles, flux actualisés, valeur terminale, VGE et VCP, sensibilité au taux de croissance, multiple, ANCC et impôt latent, annuité, barème, liste noire, hors-programme ; chiffre d'affaires par activité, BFR et dette financière nette, marges, poids de la valeur terminale, complément de prix, montants à décaisser, couverture de l'annuité et dettes rapportées à l'EBITDA vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VCP calculée avec des flux erronés à la question 2.1 ou un CMPC erroné à la question 2.2).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Business plan 2027-2031 et flux de trésorerie disponibles | `3.1.b` Construire un business plan | 2,5 |
| 2.2 MEDAF, primes de taille et d'illiquidité, CMPC avec et sans primes, modèle à trois facteurs, taux de la cible ou du groupe | `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance ; `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers | 3 |
| 2.3 Valeur terminale, VGE, VCP et sensibilité au taux de croissance | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance ; `3.1.d` Distinguer la valeur globale de l'entreprise (VGE) de la valeur des capitaux propres (VCP) | 3 |
| 2.4 ANCC et impôt latent, plancher des cédants, multiple sectoriel, fourchette | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine ; `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP | 3,5 |
| 2.5 Motifs du rachat ; achat des actions ou des seules plates-formes | `4.2.b` Analyser les motifs des opérations de réorganisation | 2 |
| 2.6 Complément de prix, prix total espéré, partage du risque et asymétrie d'information | `4.2.b` Analyser les motifs des opérations de réorganisation ; `5.1.b` Maîtriser les enseignements des asymétries d'information (Akerlof, 1970) | 1,5 |
| 2.7 Prêt intragroupe ou société d'acquisition endettée | `4.2.d` Décrypter les montages financiers avec et sans levier financier | 1,5 |
| **Total** | | **17** |

Part du calcul : environ 8,5 points (2.1-01 à 2.1-04, 2.2-01 et 2.2-02, 2.3-01 à 2.3-04, 2.4-01, 2.4-02, 2.4-05, 2.5-03, 2.6-01, 2.6-02 et 2.7-01). Part de l'analyse : environ 8,5 points. Le dossier reprend du sujet commun le taux sans risque, la prime de risque du marché, le taux d'IS et le CMPC de 7,50 % de DORVAART, qui ne sert qu'à la comparaison de la question 2.2 : les flux de LORMESSAN sont actualisés à son propre CMPC. Aucun résultat d'un autre dossier n'est utilisé, et le rachat n'est supposé fait dans aucun autre dossier.

---

### 2.1 Business plan 2027-2031 et flux de trésorerie disponibles (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Chiffre d'affaires par activité : redevances **11,02 à 12,93**, granulats **6,09 à 6,72**, métaux **4,93 à 5,44** ; total **22,04 ; 22,98 ; 23,93 ; 24,90 ; 25,09** | 0,5 |
| 2.1-02 | Charges variables **10,15 à 11,20** ; EBITDA **4,69 ; 5,13 ; 5,58 ; 6,05 ; 6,09** | 0,5 |
| 2.1-03 | Résultat d'exploitation (3,24 à 4,45), impôt de 25 % (0,81 à 1,11), résultat d'exploitation après impôt (2,43 à 3,34) ; BFR initial **2,10** et BFR de fin d'année 2,20 à 2,51, variations **0,10 ; 0,10 ; 0,09 ; 0,10 ; 0,02** | 0,5 |
| 2.1-04 | Flux de trésorerie disponibles **1,38 ; 2,22 ; 2,78 ; 3,14 ; 3,26**, présentés en tableau | 0,5 |
| 2.1-05 | Commentaire de la marge d'EBITDA (20,00 % → 24,27 %) et des flux, avec le regard critique qu'appelle un plan des cédants | 0,5 |

**Business plan de LORMESSAN (M€)**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Tonnage reçu (tonnes) | 290 000 | 300 000 | 310 000 | 320 000 | 320 000 |
| Redevances (tonnage × redevance) | 11,02 | 11,58 | 12,15 | 12,74 | 12,93 |
| Granulats (tonnage × 60 % × 35,00 €) | 6,09 | 6,30 | 6,51 | 6,72 | 6,72 |
| Métaux (tonnage × 5 % × 340,00 €) | 4,93 | 5,10 | 5,27 | 5,44 | 5,44 |
| **Chiffre d'affaires** | **22,04** | **22,98** | **23,93** | **24,90** | **25,09** |
| − Charges variables (tonnage × 35,00 €) | − 10,15 | − 10,50 | − 10,85 | − 11,20 | − 11,20 |
| − Charges fixes | − 7,20 | − 7,35 | − 7,50 | − 7,65 | − 7,80 |
| **EBITDA** | **4,69** | **5,13** | **5,58** | **6,05** | **6,09** |
| Marge d'EBITDA | 21,28 % | 22,32 % | 23,32 % | 24,30 % | 24,27 % |
| − Dotations aux amortissements | − 1,45 | − 1,50 | − 1,55 | − 1,60 | − 1,65 |
| **Résultat d'exploitation** | **3,24** | **3,63** | **4,03** | **4,45** | **4,44** |
| − Impôt sur le résultat d'exploitation (25 %) | − 0,81 | − 0,91 | − 1,01 | − 1,11 | − 1,11 |
| **Résultat d'exploitation après impôt** | **2,43** | **2,72** | **3,02** | **3,34** | **3,33** |
| + Dotations aux amortissements | + 1,45 | + 1,50 | + 1,55 | + 1,60 | + 1,65 |
| BFR de fin d'année (CA × 36 / 360) | 2,20 | 2,30 | 2,39 | 2,49 | 2,51 |
| − Variation du BFR | − 0,10 | − 0,10 | − 0,09 | − 0,10 | − 0,02 |
| − Investissements | − 2,40 | − 1,90 | − 1,70 | − 1,70 | − 1,70 |
| **Flux de trésorerie disponible** | **1,38** | **2,22** | **2,78** | **3,14** | **3,26** |

- **Chiffre d'affaires de 2027** : 290 000 × 38,00 € = 11,02 M€ de redevances ; 290 000 × 60 % = 174 000 tonnes de granulats × 35,00 € = 6,09 M€ ; 290 000 × 5 % = 14 500 tonnes de métaux × 340,00 € = 4,93 M€ ; total 22,04 M€. Présentation équivalente : chiffre d'affaires par tonne reçue = 38,00 + 0,60 × 35,00 + 0,05 × 340,00 = 76,00 €, soit 290 000 × 76,00 € = 22,04 M€.
- **BFR du 31 décembre 2026** (annexe 2.4) : 0,90 + 3,60 + 0,40 − 2,10 − 0,70 = **2,10 M€**, soit 36 jours du chiffre d'affaires de 2026 (2,10 / 21,00 × 360). Variation de 2027 : 2,20 − 2,10 = **0,10**, un emploi qui réduit le flux.
- **Flux de 2027** : 3,24 − 0,81 + 1,45 − 0,10 − 2,40 = **1,38 M€**. Présentation équivalente : EBITDA − impôt sur le résultat d'exploitation − variation du BFR − investissements = 4,69 − 0,81 − 0,10 − 2,40 = 1,38. Somme des flux de 2027 à 2031 : 12,78 M€.

**Commentaire (0,5 pt).**
- **Marge** : la marge d'EBITDA passe de **20,00 %** en 2026 (4,20 / 21,00) à **24,30 %** en 2030. Deux effets s'ajoutent : le tonnage croît de 14,29 % de 2026 à 2030 (280 000 à 320 000 tonnes) alors que les charges fixes ne croissent que de 2 % par an environ (levier opérationnel), et la redevance gagne 0,50 € par tonne en 2027, puis 0,60 € par an. En 2031, la capacité est atteinte : le chiffre d'affaires ne croît plus que de 0,76 % (redevance seule) et la marge se stabilise (24,27 %).
- **Flux** : le flux de 2027 est faible (1,38) à cause du remplacement du concasseur mobile (investissements de 2,40) ; les flux montent ensuite à 3,26 en 2031, avec des investissements proches des dotations (1,70 contre 1,65) et un BFR qui ne pèse plus (0,02).
- **Regard critique** : le plan vient du mémorandum des cédants. Il suppose que la société atteint sa capacité dès 2030, que les métaux se vendent 340,00 € la tonne pendant cinq ans, au-dessus du prix de 2026 (330,00 €, soit + 3,03 %), et que la redevance augmente chaque année, alors que 45 % des redevances dépendent de quelques contrats pluriannuels. L'acquéreur doit le confronter à ses propres données (tonnages et prix de ses plates-formes).

**Réponses tolérées** : présentation partant du chiffre d'affaires par tonne reçue (76,00 € en 2027, 76,60 €, 77,19 €, 77,81 €, 78,41 €) si les montants sont arrondis au centième comme l'annexe 2.6 le demande, chaque activité étant alors calculée à part ; écarts d'un centime dus à un arrondi du chiffre d'affaires total au lieu de chaque activité.

**Erreurs fréquentes**
- Retrancher le niveau du BFR (2,20) au lieu de sa variation (flux de 2027 de − 0,72 au lieu de 1,38) (`JUR-E01`).
- Calculer l'impôt sur l'EBITDA, ou déduire des intérêts des flux (`JUR-E01`).
- Appliquer la part de granulats et de métaux au chiffre d'affaires au lieu du tonnage reçu, ou prendre le prix des métaux de 2026 (330,00 €) au lieu de celui du plan.
- Retrancher un loyer du terrain de l'Orne, que l'évaluation traite comme une dette locative.
- `JUR-T07` — business plan non présenté en tableau.

**Références** : F03 § 2.1 (FTD = REX × (1 − t) + dotations − variation du BFR − investissements) [V corrigé 2023 ; guide p. 64 ; S] ; programme 3.1.b « construction des flux prévisionnels à partir d'hypothèses d'exploitation » [V guide p. 64].

---

### 2.2 MEDAF, primes de taille et d'illiquidité, CMPC avec et sans primes, modèle à trois facteurs, taux de la cible ou du groupe (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Coût des fonds propres : MEDAF 4,00 % + 1,00 × 5,00 % = **9,00 %** ; avec les primes : 9,00 % + 2,00 % + 1,50 % = **12,50 %** | 0,5 |
| 2.2-02 | Coût de la dette après impôt **3,75 %** ; **CMPC = 12,50 % × 75 % + 3,75 % × 25 % = 10,31 %** ; sans les primes **7,69 %** | 0,5 |
| 2.2-03 | Ce que mesurent les deux primes et les limites du MEDAF qu'elles traduisent, reliées à LORMESSAN | 0,5 |
| 2.2-04 | Ce qu'en dit le modèle à trois facteurs : fondement de la prime de taille, facteur de valeur, ce que le modèle ne dit pas de l'illiquidité | 0,5 |
| 2.2-05 | Taux de la cible ou CMPC de 7,50 % de DORVAART : raisonnement par le risque des flux, sort de chaque prime pour un acquéreur coté, conclusion | 1 |

- **Coût des fonds propres** : le bêta des fonds propres est fourni par la banque à la structure cible (1,00), sans réendettement à faire. MEDAF : 4,00 % + 1,00 × 5,00 % = **9,00 %** ; avec la prime de taille et la prime d'illiquidité, qui s'ajoutent sans être multipliées par le bêta : **12,50 %**. Les primes représentent 28,00 % du coût des fonds propres (3,50 / 12,50).
- **Coût de la dette après impôt** : 5,00 % × (1 − 25 %) = **3,75 %**.
- **CMPC** = 12,50 % × 75 % + 3,75 % × 25 % = 9,3750 % + 0,9375 % = **10,31 %**.
- **CMPC sans les primes** = 9,00 % × 75 % + 0,9375 % = **7,69 %**, proche du CMPC de 7,50 % que DORVAART retient pour ses activités françaises. Les primes ajoutent 10,31 − 7,69 = 2,62 points au CMPC (3,50 × 75 % = 2,625 avant arrondi).
- Le CMPC, et non le coût des fonds propres, actualise les flux de trésorerie disponibles : ces flux reviennent aux actionnaires et aux prêteurs.

**Ce que mesurent les primes et les limites du MEDAF (0,5 pt).** Plus un placement est incertain, plus la rentabilité exigée est élevée. Le MEDAF (Sharpe, 1964) ne rémunère que le risque systématique, mesuré par le bêta, car il suppose des investisseurs diversifiés, des titres cotés qui se vendent à tout moment et un seul facteur de risque, le marché.
- **Prime de taille** : LORMESSAN est petite (21 M€ de chiffre d'affaires) et concentrée : trois plates-formes, un fondateur qui la dirige, 45 % des redevances tenues par quelques contrats, des débouchés locaux pour les granulats. Le bêta, tiré de recycleurs cotés plus grands, ne capte pas ces fragilités.
- **Prime d'illiquidité** : les actions d'une SAS familiale non cotée n'ont pas de marché ; la famille ne peut les vendre qu'en cherchant un acquéreur, comme aujourd'hui, avec un délai, des frais et une décote. La prime rémunère ce coût de sortie.
- **Limites traduites** : un seul facteur de risque (le bêta) ; un marché supposé liquide, où tout titre se vend sans délai ; un bêta mesuré sur des sociétés cotées et appliqué à une société non cotée. Les primes sont des corrections forfaitaires, fixées par la banque, sans mesure propre à LORMESSAN.

**Ce qu'en dit le modèle à trois facteurs (0,5 pt).** Fama et French (1993) constatent que le bêta seul n'explique pas les rentabilités des actions cotées et ajoutent au marché deux facteurs : la **taille** (les petites sociétés ont obtenu des rentabilités supérieures à celles que prévoit le MEDAF) et la **valeur** (les sociétés dont la valeur comptable est élevée par rapport à la valeur de marché aussi). Le modèle donne un fondement à la prime de taille ; mais il mesure la sensibilité de chaque titre coté aux facteurs, alors que la banque ajoute une prime forfaitaire, sans sensibilité propre à LORMESSAN. Il ne dit rien de l'illiquidité, qui n'est pas l'un de ses facteurs : la prime d'illiquidité est une pratique d'évaluateur, pas un facteur du modèle.

**Taux de la cible ou CMPC du groupe (1 pt).**
- **Le taux doit refléter le risque des flux évalués, pas celui de l'acquéreur.** Le CMPC de 7,50 % mesure le risque moyen des activités françaises de DORVAART, avec sa structure financière : l'appliquer à LORMESSAN supposerait que la cible a le même risque que le groupe. Ici, les deux CMPC du seul MEDAF sont proches (7,69 % et 7,50 %) : le risque d'exploitation d'un recycleur du bâtiment est voisin de celui du groupe. L'écart vient des primes.
- **Prime d'illiquidité** : elle rémunère le détenteur d'actions qu'il ne peut pas vendre. Pour DORVAART, groupe coté dont les actionnaires peuvent vendre leurs titres à tout moment, l'illiquidité des actions de LORMESSAN disparaît avec le rachat : pour l'acquéreur, cette prime n'a plus de raison d'être.
- **Prime de taille** : une partie demeure. Les fragilités d'exploitation de LORMESSAN (quelques contrats, fondateur, trois plates-formes) restent les mêmes dans le groupe ; elles ne disparaissent qu'à mesure que la cible est intégrée au réseau de QUERMANDE. Sans la seule prime d'illiquidité, le CMPC serait de 9,19 % (illustration).
- **Effet sur la valeur** (illustration non exigée) : au CMPC sans les primes, 7,69 %, la VCP serait de **40,81 M€** contre 26,16 M€ à 10,31 % (question 2.3). L'écart majore la valeur que peut créer le passage à un groupe coté : une partie de la prime de taille demeure, et sans la seule prime d'illiquidité (CMPC de 9,19 %) la VCP serait de 31,19 M€, plus proche de 26,16. DORVAART n'a pas à payer cette valeur aux cédants.
- **Conclusion** : DORVAART ne doit pas évaluer LORMESSAN à 7,50 % pour fixer son prix. Elle retient le CMPC de la cible, 10,31 %, pour la négociation : c'est le taux de la banque des cédants, qu'ils ne peuvent pas contester, et une marge de prudence face à un plan optimiste. Un taux plus bas ne sert qu'à mesurer, en interne, la valeur que le rachat peut créer pour le groupe.

**Réponses tolérées** : primes ajoutées au CMPC plutôt qu'au coût des fonds propres si le candidat le signale (CMPC de 11,19 %, résultats suivants notés en cohérence) ; CMPC sans les primes arrondi à 7,70 % ; conclusion différente (retenir un taux intermédiaire, sans la prime d'illiquidité) si elle est argumentée par le risque des flux et si le candidat dit que l'acquéreur n'a pas à rétrocéder aux cédants la valeur ainsi créée.

**Erreurs fréquentes**
- Multiplier les primes par le bêta, ou les ajouter à la prime de risque du marché avant de la multiplier.
- Réendetter de nouveau le bêta de 1,00, ou appliquer le MEDAF au bêta désendetté de 0,80 (coût des fonds propres de 8,00 %).
- Actualiser les flux au coût des fonds propres (12,50 %) ou au CMPC de DORVAART (7,50 %) (`JUR-E01`, `JUR-E02`).
- Présenter le modèle de Fama et French comme une formule à appliquer sans données, ou lui attribuer la prime d'illiquidité.
- `JUR-T14` — rôle de la diversification dans le MEDAF ignoré.

**Références** : F02 § 2 (primes additives, limites du MEDAF) et § 7 (modèle à trois facteurs, principe seulement ; les primes de taille et de liquidité ajoutées au MEDAF en sont la traduction pratique) [V guide p. 74-75 ; programme l. 582 ; S] ; programme 3.1.a « rentabilité exigée par le MEDAF, avec primes complémentaires (prime de liquidité, prime de taille…) à partir de données fournies » [V guide p. 64] ; F10 Sharpe (1964), Fama et French (1993) [V programme 5.2] ; F11 pour le taux sans risque et la prime de marché, posés comme hypothèses d'énoncé.

---

### 2.3 Valeur terminale, VGE, VCP et sensibilité au taux de croissance (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Flux actualisés à 10,31 % : 1,25 ; 1,82 ; 2,07 ; 2,12 ; 2,00, somme **9,26** | 0,5 |
| 2.3-02 | Valeur terminale 3,26 × 1,015 / (0,1031 − 0,015) = **37,56** ; actualisée **23,00** ; **VGE 32,26** | 0,5 |
| 2.3-03 | Dettes retranchées 4,00 + 1,20 + 1,20 × 75 % = **6,10** ; **VCP = 26,16 M€** ; le prix des actions se compare à la VCP | 0,5 |
| 2.3-04 | Sensibilité : VCP **24,82** à 1,00 % (− 1,34, − 5,12 %) et **27,66** à 2,00 % (+ 1,50, + 5,73 %) | 0,5 |
| 2.3-05 | Commentaire : poids de la valeur terminale (71,30 %), sensibilité et cohérence du taux de 1,50 % avec une capacité atteinte | 1 |

**Actualisation au 31 décembre 2026 (CMPC de 10,31 %, flux en fin d'année).**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Flux de trésorerie disponible | 1,38 | 2,22 | 2,78 | 3,14 | 3,26 |
| Facteur 1 / 1,1031^n | 0,906536 | 0,821808 | 0,744998 | 0,675368 | 0,612245 |
| Flux actualisé | 1,25 | 1,82 | 2,07 | 2,12 | 2,00 |

Somme des flux actualisés : **9,26 M€**.

| M€ | g = 1,00 % | **g = 1,50 %** | g = 2,00 % |
|---|---:|---:|---:|
| Valeur terminale à la fin de 2031 : 3,26 × (1 + g) / (0,1031 − g) | 35,37 | **37,56** | 40,01 |
| Valeur terminale actualisée (× 0,612245) | 21,66 | **23,00** | 24,50 |
| Somme des flux actualisés | 9,26 | **9,26** | 9,26 |
| **VGE** | 30,92 | **32,26** | 33,76 |
| − Dette financière nette (5,50 − 1,50) | − 4,00 | − 4,00 | − 4,00 |
| − Dette locative | − 1,20 | − 1,20 | − 1,20 |
| − Provision pour remise en état nette d'impôt (1,20 × 75 %) | − 0,90 | − 0,90 | − 0,90 |
| **VCP** | 24,82 | **26,16** | 27,66 |
| Écart avec la VCP à 1,50 % | − 1,34 (− 5,12 %) | — | + 1,50 (+ 5,73 %) |

**Passage de la VGE à la VCP (0,5 pt).** Les flux de trésorerie disponibles reviennent à tous les apporteurs de capitaux : actualisés au CMPC, ils donnent la VGE, valeur de l'actif économique. QUERMANDE achète des actions et reprend les dettes de la société : la dette financière nette (5,50 − 1,50 = 4,00), la dette locative du terrain de l'Orne, dont le loyer a été exclu des flux (1,20), et la provision pour remise en état, une sortie de trésorerie future qui ne figure pas dans les flux du plan (1,20 réestimée, soit 0,90 après l'économie d'impôt). Le prix des actions se compare à la VCP de **26,16 M€**, pas à la VGE.

**Commentaire (1 pt).**
- **Poids de la valeur terminale** : 23,00 / 32,26 = **71,30 %** de la VGE. Plus des deux tiers de la valeur reposent sur des flux postérieurs à 2031, donc sur la capacité de LORMESSAN à garder ses clients, ses prix et ses sites à long terme.
- **Sensibilité** : un demi-point de croissance à l'infini en plus ou en moins fait varier la VCP d'environ 5 % (− 1,34 et + 1,50 M€). L'effet est asymétrique, car le taux de croissance figure au dénominateur (CMPC − g) ; il serait plus fort avec un CMPC plus bas.
- **Cohérence du taux de croissance** : la capacité est atteinte en 2030. Au-delà de 2031, la croissance ne peut venir que des prix (redevance, granulats, métaux), pas des tonnages, sauf nouveaux investissements de capacité qui ne figurent pas dans le flux normatif (investissements de 1,70 pour 1,65 de dotations). Un taux de 1,00 % à 1,50 % est cohérent avec une croissance par les prix ; 2,00 % supposerait des hausses de prix durables ou de nouvelles capacités.
- **Multiple implicite** (prolongement valorisé, non exigé) : la VGE représente **7,68 fois** l'EBITDA de 2026 (32,26 / 4,20), au-dessus du multiple sectoriel de 6,50 (question 2.4) : le plan des cédants intègre déjà une forte hausse de la marge et des tonnages.
- **Conclusion** : la valeur par les flux est de l'ordre de **25 à 27,5 M€** pour 100 % des actions, sous réserve d'un plan que l'acquéreur doit revoir.

**Réponses tolérées** : valeur terminale actualisée en divisant par 1,1031^5 = 1,633332 (mêmes résultats) ; flux actualisés non arrondis (somme de 9,26) ; provision retranchée pour 1,20 sans l'économie d'impôt si l'hypothèse est écrite (VCP de 25,86 M€), ou pour son montant au bilan (0,80) avec la même justification, alors que l'annexe 2.6 prévoit le montant réestimé net d'impôt ; provision retranchée pour 0,80 + 0,40 × 75 % = 1,10, par cohérence avec l'ANCC où seule la hausse réduit l'impôt latent (VCP de 25,96 M€), si le raisonnement est écrit.

**Erreurs fréquentes**
- Actualiser au coût des fonds propres (12,50 %) des flux qui reviennent à tous les apporteurs (`JUR-E01`).
- Oublier d'actualiser la valeur terminale, l'actualiser sur six ans, ou omettre le facteur (1 + g).
- Retrancher la dette brute (5,50) au lieu de la dette nette, oublier la dette locative ou la provision, ou présenter la VGE comme le prix des actions.
- `JUR-T12` — commentaire du poids de la valeur terminale sans chiffre ; `JUR-T13` — origine du business plan ignorée.

**Références** : F03 § 2.2 (valeur terminale FTD_n × (1 + g) / (CMPC − g), poids de la valeur terminale dans la VGE) [V corrigé 2023 ; guide p. 64] ; F10 Gordon et Shapiro (1956) [V programme 3.1] ; programme 3.1.d « VCP = VGE − dette financière nette » [V guide p. 64] ; programme 3.1.a « interprétation des résultats : cohérence économique, sensibilité aux hypothèses » [V guide p. 64].

---

### 2.4 ANCC et impôt latent, plancher des cédants, multiple sectoriel, fourchette (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Écarts de valeur : terrains **+ 3,00**, matériel **+ 0,80**, provision **− 0,40**, soit **+ 3,40** | 0,5 |
| 2.4-02 | Impôt latent **0,85** ; **ANCC = 10,10 + 3,40 − 0,85 = 12,65 M€** | 0,5 |
| 2.4-03 | Pourquoi l'ANCC est un plancher pour les cédants | 0,75 |
| 2.4-04 | Ce que l'ANCC ne mesure pas pour un recycleur : écart de 13,51 M€ avec la VCP par les flux, éléments non inscrits au bilan | 0,75 |
| 2.4-05 | Multiple : VGE 6,50 × 4,20 = **27,30** ; VCP 27,30 − 6,10 = **21,20 M€** | 0,5 |
| 2.4-06 | Fourchette argumentée de la VCP (21,20 à 26,16 M€, plancher 12,65) | 0,5 |

| Élément (M€) | Montant |
|---|---:|
| Capitaux propres comptables | 10,10 |
| Terrains de Lisieux et du Calvados : 4,50 − 1,50 | + 3,00 |
| Matériel de concassage et de tri : 7,20 − 6,40 | + 0,80 |
| Provision pour remise en état : 1,20 − 0,80 (hausse d'un passif) | − 0,40 |
| Écarts de valeur | + 3,40 |
| − Impôt latent de 25 % sur les écarts (0,75 + 0,20 − 0,10) | − 0,85 |
| **ANCC** | **12,65** |

**Un plancher pour les cédants (0,75 pt).**
- L'ANCC mesure ce que valent, un à un, les actifs de LORMESSAN diminués de ses dettes, avec les terrains à leur valeur vénale, le matériel à sa valeur de marché et la remise en état des sites à son coût estimé. C'est, à peu près, ce que la famille obtiendrait en vendant les terrains et le matériel séparément et en payant ses dettes.
- Les cédants n'ont donc aucune raison d'accepter moins de 12,65 M€ pour leurs actions : ils peuvent obtenir ce montant sans acheteur de l'entreprise, en vendant ses actifs. Pour une société rentable, l'ANCC est une valeur minimale, qui suppose l'arrêt de l'exploitation.
- Ce plancher est même un peu haut : une vente des actifs un à un ferait supporter des frais, des délais et le départ des 85 salariés, que l'ANCC ignore, et le matériel est évalué en état de marche.

**Ce que l'ANCC ne mesure pas (0,75 pt).**
- La VCP par les flux (26,16 M€) dépasse l'ANCC de **13,51 M€** (2,07 fois). Cet écart mesure la capacité de LORMESSAN à dégager, avec ses actifs, une rentabilité supérieure à leur coût : ses contrats de traitement pluriannuels (45 % des redevances), sa clientèle d'entreprises du Calvados et de l'Orne, la place de ses plates-formes près des chantiers, le savoir-faire de ses équipes. Aucun de ces éléments n'est inscrit au bilan.
- En VGE, l'ANCC majoré des dettes retranchées (12,65 + 6,10 = 18,75 M€) ne représente que **4,46 fois** l'EBITDA de 2026, contre 6,50 pour le multiple sectoriel.
- Pour un recycleur rentable en croissance, l'approche patrimoniale ne sert donc pas à fixer le prix. Elle sert de plancher, et elle renseigne l'acquéreur sur le patrimoine qui garantit une partie du prix (terrains de 4,50 M€).

**Multiple sectoriel (0,5 pt).** VGE = 6,50 × 4,20 = **27,30 M€** ; VCP = 27,30 − 4,00 − 1,20 − 0,90 = **21,20 M€**. Le multiple est un multiple de VE : il s'applique à l'EBITDA hors loyer, avant frais financiers, et la VCP s'obtient en retranchant les mêmes dettes que pour les flux. La dette locative est retranchée parce que l'EBITDA est calculé hors loyer et que la VE des sociétés rachetées comprend leurs dettes locatives.

**Fourchette (0,5 pt).**
- **Plancher : 12,65 M€** (ANCC). La négociation ne se joue pas à ce niveau.
- **Fourchette de négociation : 21,20 à 26,16 M€** pour 100 % des actions. Le bas est la valeur que paient des acquéreurs du secteur pour un recycleur régional, sur l'EBITDA réalisé ; le haut est la valeur par les flux du plan des cédants, qui suppose une marge portée de 20 % à 24 % et la capacité atteinte en 2030. La sensibilité (24,82 à 27,66) montre que le haut de la fourchette est fragile.
- Une valeur centrale autour de **22 à 24 M€** tient compte de l'optimisme du plan : c'est l'espace que le complément de prix (question 2.6) peut combler.

**Réponses tolérées** : impôt latent présenté écart par écart (0,75 ; 0,20 ; − 0,10) ; ANCC calculé sans l'effet de la provision sur l'impôt latent (12,55 M€) si l'hypothèse est écrite, alors que l'annexe 2.4 prévoit qu'une hausse de la provision réduit l'impôt latent ; fourchette différente si elle est justifiée par les valeurs calculées (par exemple 21,20 à 24,82 M€, en retenant la valeur par les flux à 1,00 % comme borne haute prudente).

**Erreurs fréquentes**
- Ajouter la valeur vénale des terrains aux capitaux propres sans retrancher leur valeur comptable, ou oublier l'impôt latent.
- Augmenter l'ANCC du fait de la hausse de la provision, ou oublier de retrancher la dette locative et la provision de la VGE par le multiple.
- Additionner ou moyenner une VGE et une VCP.
- `JUR-E03` — valeurs juxtaposées, sans les croiser pour une fourchette.

**Références** : F03 § 3 (multiples de VGE, cohérence de l'inducteur, passage à la VCP) et § 4 (ANCC, retraitements fournis, limites : valeur statique, ignore la rentabilité future et les incorporels) [V corrigé 2023 ; guide p. 64-66 ; S] ; F03 § 8 (fourchette et réconciliation des méthodes) [V guide p. 64 et 66 ; S] ; programme 3.3.a « pertinence de l'approche selon l'activité, la situation financière, le cycle de vie » [V guide p. 66] ; programme 3.2.a « agrégats de l'entreprise évaluée et multiples applicables » fournis [V guide p. 65].

---

### 2.5 Motifs du rachat ; achat des actions ou des seules plates-formes (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Motifs du rachat pour QUERMANDE et pour DORVAART, comparés à la croissance interne | 0,75 |
| 2.5-02 | Comparaison qualitative des deux formes : dettes, provision et litige, contrats, salariés, préférence des cédants | 0,75 |
| 2.5-03 | Montant à décaisser hors complément : actions **27,10** contre plates-formes **29,20** ; conclusion | 0,5 |

**Motifs du rachat (0,75 pt).**
- **Maillage régional et accès aux chantiers** : les entreprises ne transportent pas leurs déchets sur plus de 40 à 50 km ; les chantiers du Calvados et de l'Orne échappent aujourd'hui à QUERMANDE. Le rachat lui donne trois plates-formes sur ce territoire, avec leurs clients et leurs contrats, et un réseau de sept plates-formes en Normandie.
- **Capacité de traitement** : Louviers et Elbeuf sont saturées ; LORMESSAN apporte 320 000 tonnes de capacité, déjà en service.
- **Synergies possibles** (non chiffrées) : vente des métaux par DORVAART Metals Trading, achats regroupés, concassage partagé, offre commune aux entreprises qui travaillent sur toute la Normandie.
- **Pour DORVAART** : croissance externe dans un pays où le groupe veut un réseau complet, sans risque de change (opérations en euros) ; le rachat est un signal stratégique adressé aux clients et aux concurrents.
- **Comparaison avec la croissance interne** : une plate-forme créée dans le Calvados demanderait plusieurs années avant de recevoir sa première tonne, sans clients acquis, et ajouterait une capacité à un marché déjà servi par LORMESSAN et d'autres. Le rachat est plus rapide, achète une clientèle et retire un concurrent, mais il se paie : une prime sur l'actif net (VCP de 26,16 M€ contre 12,65 M€), le risque de surpayer un plan optimiste et un risque d'intégration (départ du fondateur après douze mois, clients attachés à la famille).

**Les deux formes de rachat (0,75 pt).** Les différences sont des faits d'énoncé (annexe 2.5).
- **Achat des actions** : QUERMANDE reprend la société entière, avec ses dettes (dette financière nette, dette locative, provision pour remise en état), son BFR et le litige de 0,60 M€, sans protection ; les contrats de traitement, les salariés et l'organisation continuent sans interruption. Le prix est faible (21,00 M€) parce que QUERMANDE reprend les dettes ; le complément de prix partage le risque du plan.
- **Achat des seules plates-formes** : QUERMANDE ne reprend ni l'emprunt, ni le litige, ni les autres passifs de la société, ce qui la protège contre un passif ancien qu'elle ne connaît pas. Mais elle reprend la remise en état des sites et le bail de l'Orne, doit financer un BFR neuf (2,10 M€), signer de nouveau chaque contrat de traitement, avec le risque de perdre 15 % des redevances, et accueillir les 85 salariés dans une nouvelle organisation. Le prix est fixe, sans lien avec les résultats futurs.
- **Préférence des cédants** : un prix certain, indépendant de la dette et des résultats futurs ; le risque du plan est entièrement reporté sur l'acquéreur.

**Montant à décaisser par QUERMANDE (0,5 pt).**

| M€ | Achat des actions | Achat des plates-formes |
|---|---:|---:|
| Prix (partie fixe pour les actions) | 21,00 | 25,00 |
| Dette financière nette reprise | 4,00 | — |
| BFR à constituer | — | 2,10 |
| Dette locative reprise | 1,20 | 1,20 |
| Provision pour remise en état, nette d'impôt | 0,90 | 0,90 |
| **Montant à décaisser, hors complément de prix** | **27,10** | **29,20** |
| Rapporté à l'EBITDA de 2026 | 6,45 | 6,95 |

- Hors complément de prix (étudié à la question 2.6), l'achat des plates-formes coûte **2,10 M€** de plus que l'achat des actions. Il ne protège que contre le litige (0,60 M€ réclamés) et les passifs inconnus de la société, alors qu'il expose à la perte de 15 % des redevances.
- **Conclusion** : l'achat des actions est préférable pour QUERMANDE. Le litige se traite dans la négociation du prix (le montant réclamé peut être retenu sur la partie fixe ou faire l'objet d'un engagement des cédants, à faire préciser par les conseils juridiques).

**Réponses tolérées** : montant à décaisser présenté sans la dette locative et la provision, communes aux deux formes, si le candidat le signale (25,00 et 27,10 avant complément pour respectivement les actions et les plates-formes, soit 21,00 + 4,00 et 25,00 + 2,10) ; prise en compte du litige dans la comparaison (achat des actions à 27,70 M€ hors complément si le candidat retient le montant réclamé, 0,60) ; conclusion en faveur des plates-formes si le candidat juge le risque de passif inconnu supérieur au risque de perte des clients et le justifie.

**Erreurs fréquentes**
- Comparer le prix des actions (21,00) au prix des plates-formes (25,00) sans ajouter la dette reprise ni le BFR à constituer.
- Exposer les règles de la cession de titres, du transfert des contrats de travail ou des autorisations d'exploiter : les différences entre les deux formes sont des faits d'énoncé.
- `JUR-T13` — motifs cités sans lien avec le cas (distances, capacité, clients) ; `JUR-T01` — conseil non adressé à la direction de QUERMANDE.

**Références** : programme 4.2.b « motifs économiques et financiers : synergies opérationnelles ou financières, croissance externe » et « mécanismes (transfert d'actifs et de passifs, périmètre, structure du capital) », hors considérations juridiques et fiscales [V guide p. 69-70] ; F05 § 5 (logique économique d'un rapprochement : création de valeur si les synergies dépassent la prime payée) [V guide p. 69-70 ; S].

---

### 2.6 Complément de prix, prix total espéré, partage du risque et asymétrie d'information (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Compléments **0 ; 1,50 ; 3,00** (plafond appliqué dans le scénario fort) ; espérance **1,35 M€** | 0,5 |
| 2.6-02 | Valeur actuelle 1,35 / 1,1031³ = **1,01 M€** ; prix total espéré **22,01 M€** | 0,5 |
| 2.6-03 | Partage du risque et réduction de l'écart d'information entre cédants et acquéreur | 0,5 |

| Scénario | Probabilité | EBITDA de 2029 | 3 × (EBITDA − 4,90) | Complément | Probabilité × complément |
|---|---:|---:|---:|---:|---:|
| Faible | 30 % | 4,60 | négatif | 0 | 0 |
| Central | 50 % | 5,40 | 1,50 | 1,50 | 0,75 |
| Fort | 20 % | 6,10 | 3,60 | 3,00 (plafond) | 0,60 |
| **Espérance** | | 5,30 | | | **1,35** |

- **Valeur actuelle au 30 septembre 2027** : 1,35 × 1 / 1,1031³ = 1,35 × 0,744998 = **1,01 M€**. Le complément est actualisé au CMPC de LORMESSAN, car il dépend des résultats de son exploitation.
- **Prix total espéré** = 21,00 + 1,01 = **22,01 M€**, entre la VCP par le multiple (21,20) et la valeur par les flux (26,16), en bas de la zone centrale de la question 2.4. Au maximum, les cédants recevraient 21,00 + 3,00 = 24,00 M€ (montants non actualisés).
- **Retour sur la question 2.5** (prolongement valorisé, non exigé) : complément compris, l'achat des actions représente 27,10 + 1,01 = **28,11 M€** (28,71 avec le litige), contre 29,20 M€ pour les plates-formes, soit 1,09 M€ de moins.
- Si le plan des cédants se réalisait (EBITDA de 2029 de 5,58), le complément serait de 3 × 0,68 = 2,04 M€ (1,52 M€ actualisé) : les cédants qui croient à leur plan peuvent attendre un prix total de 22,52 M€.

**Partage du risque et écart d'information (0,5 pt).**
- **Écart d'information** : la famille connaît ses clients, l'état de son matériel, la solidité de ses contrats ; QUERMANDE découvre la société par un mémorandum préparé par la banque des cédants. Au sens d'Akerlof (1970), l'acheteur moins informé se protège en offrant un prix bas, et un bon vendeur peut renoncer à vendre : les deux parties perdent.
- **Le complément de prix réduit cet écart** : le plan des cédants prévoit un EBITDA de 5,58 M€ en 2029, Mme AUBRINEAU en attend 5,30. Plutôt que de trancher, l'offre paie une partie du prix seulement si l'EBITDA se réalise. Des cédants qui croient à leur plan acceptent ce paiement différé ; des cédants qui le savent trop optimiste préféreraient un prix fixe plus élevé : leur réponse est elle-même une information (signal). La préférence des cédants pour la vente des plates-formes à prix fixe, sans complément (annexe 2.5), en est une : elle peut traduire un doute sur leur propre plan.
- **Partage du risque** : si l'activité déçoit (scénario faible), QUERMANDE ne paie que 21,00 M€ ; si elle réussit, les cédants reçoivent jusqu'à 3,00 M€ de plus. Le plafond limite ce que QUERMANDE paie pour une réussite qui viendrait aussi de ses propres apports (vente des métaux par le groupe, clients de QUERMANDE).
- **Limites** : l'EBITDA de 2029 sera calculé après le rachat, sous la direction de QUERMANDE, qui pourrait le réduire (charges, facturation interne au groupe) : sa définition et son contrôle doivent être précis. Le fondateur, qui ne reste que douze mois, n'influence plus l'EBITDA de 2029, d'où un risque de désaccord. Les cédants supportent aussi un risque de crédit sur QUERMANDE jusqu'en 2030.

**Réponses tolérées** : complément actualisé au coût des fonds propres (12,50 %) si le candidat justifie qu'il revient aux actionnaires cédants (valeur actuelle de 0,95 M€, prix total de 21,95 M€) ; valeur actuelle exprimée au 31 décembre 2026 sur 3,75 ans si l'hypothèse est écrite ; complément calculé sur l'EBITDA espéré (3 × 0,40 = 1,20) si le candidat montre ensuite que l'espérance des compléments (1,35) en diffère à cause du seuil et du plafond.

**Erreurs fréquentes**
- Oublier le plafond dans le scénario fort (3,60 au lieu de 3,00, espérance de 1,47), ou verser un complément négatif dans le scénario faible.
- Ajouter le complément nominal à la partie fixe sans l'actualiser (prix de 22,35).
- `JUR-M01` — asymétrie d'information non mobilisée.

**Références** : F10 Akerlof (1970) [V programme 5.1 ; compétence 5.1.b] ; programme 4.2.b « motifs économiques et financiers » et « effets sur la VGE, la structure financière et la gouvernance » [V guide p. 69] ; F03 § 2 pour l'actualisation [V guide p. 64].

---

### 2.7 Prêt intragroupe ou société d'acquisition endettée (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Annuité 12,00 × 0,05 / (1 − 1,05^−7) = **2,07 M€** ; dividende de 2,20 (couverture 1,06) mais flux disponible de 2028 de 2,22 − 1,35 = **0,87** (0,42) ; dettes servies par les flux de LORMESSAN : **5,20** (1,24 fois l'EBITDA) en voie A, **17,20** (4,10 fois) en voie B | 0,5 |
| 2.7-02 | Comparaison des deux voies : coût, risque, souplesse | 0,5 |
| 2.7-03 | Ce que change la société d'acquisition endettée pour le risque et pour la remontée des flux | 0,5 |

**Calculs (0,5 pt).**
- **Annuité** : 12,00 × 0,05 / (1 − 1,05^−7) = 12,00 × 0,172820 = **2,07 M€** par an, de 2028 à 2034 (intérêts de 0,60 la première année).
- **Dividende** : le résultat de 2027 (2,20 M€), distribué en totalité en 2028, couvre l'annuité **1,06 fois**. La marge est mince.
- **Trésorerie** : le dividende se paie en trésorerie, pas en résultat. LORMESSAN doit d'abord servir son propre emprunt (1,35 M€ par an) ; en 2028, il lui reste 2,22 − 1,35 = **0,87 M€** de flux disponible, soit **0,42 fois** l'annuité. Le flux de 2027 (1,38) suffit à peine à servir son propre emprunt. Distribuer 2,20 M€ en 2028 obligerait LORMESSAN à puiser dans ses disponibilités (1,50) ou à s'endetter.
- **Dettes servies par les flux de LORMESSAN** : voie A, 4,00 + 1,20 = **5,20 M€**, soit **1,24 fois** l'EBITDA de 2026 ; voie B, 12,00 + 4,00 + 1,20 = **17,20 M€**, soit **4,10 fois**.

**Comparaison des deux voies (0,5 pt).**
- **Voie A, prêt intragroupe** : le rachat est financé par les ressources du groupe ; la dette est portée par QUERMANDE et, au-delà, par DORVAART, dont les flux sont diversifiés sur quatre pays. LORMESSAN n'a pas de dette nouvelle ; son flux peut remonter quand le groupe en a besoin, par dividende ou par la centralisation de la trésorerie à Rotterdam. Le taux (Euribor 3 mois + 1,10 %, soit environ 3,75 %) est plus bas que celui de la banque (5,00 %) et la dette se rembourse en une fois, à l'échéance, ce qui laisse les flux de LORMESSAN financer sa croissance. Le risque est variable : il dépend de l'Euribor.
- **Voie B, société d'acquisition endettée** : c'est un montage à effet de levier. QUERMANDE n'apporte que 9,00 M€ et une banque extérieure prête 12,00 M€, garantie seulement par les dividendes de LORMESSAN. L'effet de levier amplifie la rentabilité des 9,00 M€ apportés si LORMESSAN réussit, et les pertes dans le cas contraire. Le groupe garde ses propres capacités d'emprunt, mais paie plus cher (5,00 % contre 3,75 %) une dette dont l'annuité dépasse les flux disponibles des premières années.

**Ce que change la société d'acquisition (0,5 pt).**
- **Risque** : il est concentré sur une seule cible. Le service de la dette (2,07 M€) dépend des seuls résultats et de la seule trésorerie de LORMESSAN, qui porte déjà son propre emprunt : 4,10 fois son EBITDA de dettes au total, contre 1,24 fois. Dans le scénario faible (EBITDA de 4,60 en 2029), la société d'acquisition ne pourrait pas payer ses annuités sans un apport de QUERMANDE.
- **Remontée des flux** : la société d'acquisition ne reçoit que des dividendes, votés une fois par an, après l'arrêté des comptes, dans la limite du résultat distribuable et de la trésorerie de LORMESSAN ; un résultat ne se distribue pas s'il est consommé par des investissements, le BFR ou le remboursement de l'emprunt propre de la cible. Les flux de LORMESSAN ne remontent plus librement au groupe : ils sont réservés en priorité à la banque.
- **Recommandation** : la voie A convient mieux à ce rachat. La cible est petite, ses flux sont faibles en 2027 (investissements) et elle est déjà endettée ; un groupe coté au bilan solide n'a pas besoin d'effet de levier pour un prix de 21 M€. La voie B ne serait raisonnable qu'avec un emprunt plus faible, différé d'un ou deux ans, ou après remboursement de l'emprunt propre de LORMESSAN.

**Réponses tolérées** : annuité de 2,074 ; couverture du dividende calculée avec un dividende inférieur au résultat si le candidat suppose une distribution partielle et l'écrit ; mention de la condition de réussite d'un montage à effet de levier (dividendes reçus supérieurs ou égaux au service de la dette) sans calcul année par année.

**Erreurs fréquentes**
- Comparer l'annuité au résultat net sans voir que le dividende se paie en trésorerie et que la cible sert déjà son propre emprunt.
- Oublier, dans la voie B, la dette propre de LORMESSAN, ou compter le prêt de DORVAART Treasury comme une dette de LORMESSAN dans la voie A.
- `JUR-I02` — conditions de réussite d'un montage à levier non reliées à la capacité de distribution de la cible ; `JUR-I01` — annuité constante mal calculée.

**Références** : F05 § 1 (holding de reprise, dette remboursée par les dividendes de la cible, condition de réussite, effet de levier qui amplifie gains et pertes) [V guide p. 70 ; corrigé du sujet zéro p. 100-101] ; F01 (annuité constante) [V] ; programme 4.2.d « rôle des holdings : centralisation du contrôle, organisation du groupe, remontée de dividendes ; levier financier : endettement pour financer une acquisition, exposition au risque » [V guide p. 70].
