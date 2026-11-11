# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 30 — Dossier 3 (18 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F05 ingénierie financière, F06 marchés financiers et innovations, F10 auteurs et théories et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (augmentation de capital avec droit préférentiel de souscription : actions nouvelles, parité, cours théorique, valeur du droit, décotes, produit net, répartition du capital, neutralité patrimoniale, BPA ; trajectoire de la dette et capacité d'endettement ; ratios avec et sans dettes locatives ; barème, liste noire, hors-programme ; tranche des particuliers vérifiée par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat. Les questions 3.3 et 3.4 donnent les résultats intermédiaires utiles (nombre d'actions nouvelles, parité, produit net, dette de 2029) : elles se traitent sans la question 3.2.

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Capacité d'endettement, choix des fonds propres et asymétrie d'information | `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives ; `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière et identifier ses déterminants ; `5.1.b` Maîtriser les enseignements des asymétries d'information (Akerlof, 1970) | 4 |
| 3.2 Modalités de l'émission, neutralité et dilution | `4.2.a` Repérer les stratégies des groupes dans la gestion de leur capital | 4 |
| 3.3 Répartition du capital, BPA et gestion du capital | `4.2.a` | 2 |
| 3.4 Structure financière avant et après l'opération | `7.2.b` | 2 |
| 3.5 Cours observés et efficience informationnelle | `5.1.c` Maîtriser les grands enseignements de l'efficience informationnelle des marchés (Fama, 1970) | 1,5 |
| 3.6 Plateforme, algorithmes et tranche ouverte aux particuliers | `5.4.b` Comprendre le rôle des nouveaux acteurs ; `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.1.a` Appréhender le rôle des sources de financement (direct sur les marchés, indirect avec les intermédiaires) | 4,5 |
| **Total** | | **18** |

Part du calcul : environ 8 points (3.1-01, 3.2-01 à 3.2-04 et la moitié de 3.2-05, 3.3-01, 3.3-02, 3.4-01, 3.5-01, 3.6-01). Part de l'analyse : environ 10 points. La question 3.6 vaut 4,5 points et se traite sans calcul lourd : elle ne doit pas être sacrifiée faute de temps (`JUR-T15`).

---

### 3.1 Capacité d'endettement, choix des fonds propres et asymétrie d'information (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Sans augmentation de capital, de 2027 à 2030 : dette hors dettes locatives 92,00 / 144,00 / 180,00 / 170,00 M€ ; ratio 2,30 / 3,51 / 3,75 / 2,98 ; capacité restante + 8,00 M€ en 2027, puis dépassements de 41,50 / 60,00 / 27,50 M€ ; fonds propres nouveaux minimaux 60,00 M€ (2029) | 1,5 |
| 3.1-02 | Théorie du compromis et financement hiérarchique appliqués au cas : le choix des fonds propres découle de la contrainte de la clause et de l'insuffisance de l'autofinancement | 1,5 |
| 3.1-03 | Asymétrie d'information (Akerlof, 1970) : réaction négative attendue, baisse observée de 6,50 % le 16 mars, moyens de la limiter (engagement de la holding, garantie, communication) | 1 |

**Capacité d'endettement** (annexe 3.6) : à chaque clôture, dette maximale autorisée par la clause = 2,50 × (EBITDA − loyers décaissés) ; capacité restante = dette maximale − dette hors dettes locatives prévue. Le plan coûte 180,00 M€, alors que le ratio de départ (1,90 fin 2026) ne laisse qu'une marge limitée sous le seuil.

**Trajectoire sans augmentation de capital (M€)**

| | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|
| Dette hors dettes locatives à l'ouverture | 80,00 | 92,00 | 144,00 | 180,00 |
| − Flux disponible avant investissements du plan | − 18,00 | − 18,00 | − 24,00 | − 30,00 |
| + Investissements du plan | + 30,00 | + 70,00 | + 60,00 | + 20,00 |
| **Dette hors dettes locatives à la clôture** | **92,00** | **144,00** | **180,00** | **170,00** |
| EBITDA − loyers décaissés | 40,00 | 41,00 | 48,00 | 57,00 |
| **Ratio de la clause** | 92,00 / 40,00 = **2,30** | 144,00 / 41,00 = **3,51** | 180,00 / 48,00 = **3,75** | 170,00 / 57,00 = **2,98** |
| Dette maximale (2,50 × base) | 100,00 | 102,50 | 120,00 | 142,50 |
| Capacité restante (+) ou dépassement (−) | + 8,00 | − 41,50 | **− 60,00** | − 27,50 |

Le plan (180,00 M€) dépasse de 90,00 M€ les flux disponibles cumulés de 2027 à 2030 (90,00 M€). Financé par le seul crédit syndiqué, il ferait franchir le seuil de 2,50 dès 2028 et jusqu'en 2030. Le dépassement le plus élevé, en 2029, fixe le **montant minimal de fonds propres nouveaux : 60,00 M€ nets de frais**. Le montant brut annoncé (84 M€, soit 81,48 M€ nets) laisse une marge de sécurité d'environ 21,48 M€ en 2029, utile face au recul du marché, à l'incertitude des prévisions et aux effets de la fraude de janvier, que les prévisions n'intègrent pas.

**Théorie du compromis et financement hiérarchique (1,5 pt)** [F10, V programme 7.2].
- **Théorie du compromis** (Myers, 1977, selon l'attribution du programme) : l'entreprise vise un endettement cible qui équilibre l'avantage fiscal de la dette (intérêts déductibles, IS 25 %) et les coûts de la détresse financière et d'agence. Chez ERVIDANE, ces coûts sont concrets : franchir 2,50 permet aux banques d'exiger le remboursement anticipé ou de renégocier (commission, hausse de la marge), dans un marché en recul. Avec 3,75 en 2029, le groupe serait au-delà de l'endettement cible : la théorie recommande de **ramener la dette vers la cible par des fonds propres**. Elle n'impose pas de tout financer en actions : la dette reste utilisée jusqu'à 2,05 en 2029 (question 3.4), près de la limite de la clause mais avec une marge de sécurité.
- **Financement hiérarchique** (Myers et Majluf, 1984) : à cause de l'asymétrie d'information, l'entreprise préfère l'autofinancement, puis la dette, puis en dernier l'émission d'actions. ERVIDANE suit cet ordre : l'autofinancement couvre la moitié du plan (90,00 M€ sur 180,00), la dette est utilisée jusqu'à près de la limite de la clause, avec une marge de sécurité, et l'émission d'actions n'intervient qu'en dernier recours, pour le solde que la dette ne peut pas porter. L'augmentation de capital n'est pas un choix de facilité mais la conséquence d'une capacité d'endettement épuisée.
- **Conclusion** : les deux théories convergent ici. La seconde explique pourquoi l'émission coûte cher, par la réaction du cours ; la première explique pourquoi elle est malgré tout rationnelle, parce qu'elle évite les coûts de la détresse financière.

**Asymétrie d'information et réaction du cours (1 pt)** [F10 ; F06 § 2].
- Au sens d'Akerlof (1970), les dirigeants connaissent mieux que les investisseurs la valeur de l'entreprise et la qualité du plan. Les investisseurs, qui ne savent pas distinguer une bonne émission d'une mauvaise, craignent la **sélection adverse** : une société n'émettrait des actions que lorsqu'elles sont surévaluées (Myers et Majluf, 1984). Ils appliquent donc une décote à toute annonce d'émission. Une **baisse du cours** est attendue, d'autant plus forte que l'émission est importante (84 M€, soit 26,37 % de la capitalisation de 318,60 M€ à la veille de l'annonce, au cours de 10,62 €) et que le marché du vélo recule.
- **Observé** (annexe 3.4) : le cours passe de 10,62 € le 15 mars à 9,93 € le 16 mars, soit **− 6,50 %**, alors que l'indice sectoriel est stable (100,3 puis 100,1). La baisse est concentrée sur le jour de l'annonce, puis le cours se stabilise autour de 9,90 € : l'information a été intégrée en une séance.
- **Moyens de limiter la décote** : l'engagement de la holding familiale à souscrire toute sa quote-part (signal coûteux : la famille, mieux informée, investit 34,44 M€ au même prix que le public) ; la garantie bancaire, qui certifie le succès ; le maintien du droit préférentiel, qui protège les actionnaires en place ; une communication financière détaillée sur le plan (rentabilité des ateliers, calendrier, indicateurs de la mission) ; l'annonce simultanée des résultats, qui réduit l'écart d'information.

**Réponses tolérées** : capacité restante calculée aussi au 31/12/2026 (2,50 × 42,00 − 80,00 = 25,00 M€), en point de départ, sans points supplémentaires ; fonds propres minimaux exprimés en brut (60,00 / 0,97 = 61,86 M€), si le candidat le précise ; citation de Ross (1977) pour le signal négatif d'une moindre dette, ou de Modigliani et Miller (1958, 1963) pour l'avantage fiscal de la dette, en complément.

**Erreurs fréquentes**
- Calculer le besoin de fonds propres sur le seul total du plan (90,00 M€) sans tenir compte de la capacité d'endettement de chaque année, ou retenir la dernière année (27,50 M€) au lieu du dépassement le plus élevé.
- Calculer le ratio de la clause avec les dettes locatives, contrairement à sa définition contractuelle.
- Inverser l'ordre du financement hiérarchique (actions avant dette) ou attribuer le financement hiérarchique à Modigliani et Miller [F10].
- `JUR-T14` — théories récitées sans lien avec la clause et les chiffres ; `JUR-M01` — réaction du cours décrite sans référence à l'asymétrie d'information ; `JUR-T13` — réponse qui ne cite pas la baisse de 6,50 % de l'annexe 3.4.

---

### 3.2 Modalités de l'émission, neutralité et dilution (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Actions nouvelles : 84 000 000 / 7,00 = 12 000 000 ; parité : 30 000 000 / 12 000 000 = 2,5 droits pour une action nouvelle, soit 2 actions nouvelles pour 5 droits | 0,5 |
| 3.2-02 | Cours théorique après détachement 9,00 € ; valeur théorique du droit 0,80 € | 1 |
| 3.2-03 | Décote par rapport au cours théorique 22,22 % (décote faciale 28,57 %) | 0,5 |
| 3.2-04 | Frais 2,52 M€ ; produit net 81,48 M€ | 0,5 |
| 3.2-05 | BRESKANE Capital : patrimoine 17,64 M€ avant et après (16,20 M€ de titres + 1,44 M€ de droits) ; part du capital de 6,00 % à 4,29 % (− 1,71 point) ; actionnaire passif : perte de la valeur du droit | 1 |
| 3.2-06 | La décote n'est pas un cadeau : elle est compensée par le droit, qui revient aux actionnaires en place | 0,5 |

**Nombre d'actions et parité.** Actions nouvelles = 84 000 000 / 7,00 = **12 000 000**. Chaque action ancienne reçoit un droit : 30 000 000 droits pour 12 000 000 actions nouvelles, soit **2,5 droits par action nouvelle**, c'est-à-dire **2 actions nouvelles pour 5 droits**. Après l'opération, le capital compte 42 000 000 d'actions ; les actions nouvelles en représentent 12 / 42 = 28,57 %.

**Cours théorique et valeur du droit** (annexe 3.6)
- Cours théorique après détachement = (30 000 000 × 9,80 + 12 000 000 × 7,00) / 42 000 000 = (294 000 000 + 84 000 000) / 42 000 000 = **9,00 €**.
- Valeur théorique du droit = 9,80 − 9,00 = **0,80 €** ; vérification : (9,80 − 7,00) × 12 / 42 = 2,80 × 2 / 7 = 0,80 €. Acheter 2,5 droits et payer le prix d'émission revient au cours théorique : 2,5 × 0,80 + 7,00 = 9,00 €.

**Décotes.** Décote faciale (donnée) : 1 − 7,00 / 9,80 = 28,57 %. Décote par rapport au cours théorique : 1 − 7,00 / 9,00 = **22,22 %**. C'est la décote pertinente : elle mesure l'écart entre le prix payé et la valeur de l'action une fois l'émission réalisée. Elle protège le succès de l'émission : le cours peut baisser de 22 % avant que le prix d'émission ne dépasse le cours, ce qui rendrait la souscription absurde et ferait jouer la garantie.

**Produit net.** Frais = 3,00 % × 84,00 = **2,52 M€** ; produit net = 84,00 − 2,52 = **81,48 M€**.

**Neutralité et dilution : BRESKANE Capital** (1 800 000 actions, 6,00 % du capital)

| | Avant l'opération | Après l'opération, droits cédés |
|---|---:|---:|
| Actions détenues | 1 800 000 × 9,80 € = 17,64 M€ | 1 800 000 × 9,00 € = 16,20 M€ |
| Produit de cession de 1 800 000 droits à 0,80 € | – | 1,44 M€ |
| **Patrimoine** | **17,64 M€** | **17,64 M€** |
| Part du capital | 1,8 / 30 = 6,00 % | 1,8 / 42 = **4,29 %** |

L'actionnaire qui cède ses droits **ne s'appauvrit pas** : la baisse du cours (0,80 € par action) est exactement compensée par le prix des droits. Il **se dilue** : sa part du capital passe de 6,00 % à 4,29 % (− 1,71 point, soit une baisse relative de 28,57 %, égale à 1 − 30 / 42), et avec elle ses droits de vote et sa part des bénéfices futurs. L'actionnaire qui **n'exerce ni ne cède** ses droits les laisse perdre leur valeur à la clôture de la souscription : il subit la dilution **et** perd 0,80 € par action (1,44 M€ pour une ligne comme celle de BRESKANE). À l'inverse, CORVELLE Participations, qui souscrit, conserve 41 % du capital et un patrimoine inchangé : 12 300 000 × 9,80 = 120,54 M€ avant ; 17 220 000 × 9,00 − 34,44 = 120,54 M€ après.

**La décote n'est pas un cadeau (0,5 pt).** Dans une émission avec droit préférentiel, la décote est offerte aux **actionnaires en place**, à qui reviennent les droits : ce qu'un nouvel actionnaire gagne en souscrivant sous le cours, il le paie en achetant les droits. La richesse n'est transférée que si un actionnaire laisse ses droits perdre leur valeur. C'est la différence avec une émission sans droit préférentiel, où une décote importante transférerait de la valeur des anciens actionnaires vers les nouveaux. Le droit préférentiel permet donc une décote élevée, qui sécurise l'opération, sans spolier les actionnaires [F05 § 4].

**Réponses tolérées** : parité exprimée « 5 pour 2 » ; valeur du droit calculée par la formule (C − E) × n / (N + n) ; démonstration de la neutralité sur une ligne de 5 actions (49,00 € avant ; 45,00 + 4,00 = 49,00 € après) au lieu de la ligne de BRESKANE ; dilution exprimée par le coefficient 30 / 42 = 0,7143.

**Erreurs fréquentes**
- Valeur du droit calculée avec n / N au lieu de n / (N + n) : (9,80 − 7,00) × 12 / 30 = 1,12 € [F05 § 7, piège 6].
- Cours théorique calculé sur le produit net (frais déduits) : la convention de l'annexe 3.6 retient le montant brut.
- Parité inversée (2,5 actions nouvelles par droit).
- Conclure que l'actionnaire qui cède ses droits « perd 0,80 € par action » : il les a encaissés.
- `JUR-T07` — neutralité démontrée sans tableau avant / après ; `JUR-T13` — dilution décrite sans la situation de BRESKANE.

---

### 3.3 Répartition du capital, BPA et gestion du capital (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Répartition après l'opération : CORVELLE Participations 41,00 % ; BRESKANE Capital 4,29 % ; salariés et public 49,21 % ; nouveaux actionnaires 5,50 % | 1 |
| 3.3-02 | BPA 2030 : 1,10 € sans augmentation de capital ; 0,86 € avec (− 21,82 %) | 0,5 |
| 3.3-03 | Commentaire : structure financière, dilution du BPA et du contrôle, signal | 0,5 |

**Répartition du capital** (hypothèse de l'annexe 3.3)

| Actionnaire | Actions avant | Droits exercés | Actions nouvelles | Actions après | Part après |
|---|---:|---:|---:|---:|---:|
| CORVELLE Participations | 12 300 000 | 12 300 000 | 4 920 000 | 17 220 000 | **41,00 %** |
| BRESKANE Capital | 1 800 000 | 0 (cédés) | 0 | 1 800 000 | **4,29 %** |
| Salariés et public | 15 900 000 | 75 % × 15 900 000 = 11 925 000 | 4 770 000 | 20 670 000 | **49,21 %** |
| Nouveaux actionnaires (acheteurs de droits, TALMERIS, garant) | – | 5 775 000 | 2 310 000 | 2 310 000 | **5,50 %** |
| **Total** | **30 000 000** | **30 000 000** | **12 000 000** | **42 000 000** | **100,00 %** |

Les nouveaux actionnaires reçoivent les actions correspondant aux droits cédés par BRESKANE (1 800 000 droits) et aux droits non exercés des salariés et du public (3 975 000 droits) : 5 775 000 / 2,5 = 2 310 000 actions, soit 16,17 M€. La garantie de la Banque VARENTIER porte sur toutes les actions que la holding ne s'est pas engagée à souscrire : 7 080 000 actions, soit 49,56 M€.

**BPA prévu pour 2030** : sans augmentation de capital, 33,00 / 30 = **1,10 €** ; avec, 36,00 / 42 = **0,86 €**, soit **− 21,82 %**. Les économies de frais financiers (3,00 M€ après impôt) ne compensent pas l'augmentation de 40 % du nombre d'actions : l'opération est dilutive pour le BPA.

**Commentaire (0,5 pt)** [F05 § 3 et 4 ; V guide p. 68].
- **Structure financière** : l'opération est d'abord un instrument de gestion du capital au service de la structure financière : elle restaure la capacité d'endettement et permet d'investir sans dépendre d'une renonciation des banques.
- **Dilution du BPA** : le BPA de 2030 baisse de 21,82 %, mais il ne faut pas confondre dilution du BPA et destruction de valeur. Le BPA sans augmentation de capital suppose un financement qui violerait la clause ; le BPA plus faible correspond à un risque financier plus faible, que les actionnaires rémunèrent par une rentabilité exigée moindre (Modigliani et Miller, 1958, enseignements seulement) [F10].
- **Dilution du contrôle** : la famille conserve 41,00 % en souscrivant 34,44 M€ ; BRESKANE, qui refuse de suivre, passe à 4,29 % et voit son influence d'actionnaire activiste diminuer. Le droit préférentiel laisse à chacun le choix entre maintenir sa part et se diluer sans perte.
- **Signal** : la souscription de la famille est un signal positif et coûteux, alors que le refus du fonds et la cession de ses droits sont un signal négatif. L'opération révèle aussi le désaccord entre actionnaires sur la stratégie.

**Réponses tolérées** : BPA de 0,857 € non arrondi ; variation calculée sur les valeurs non arrondies (− 22,08 %), si le candidat le signale ; répartition des nouveaux actionnaires détaillée entre acheteurs de droits, plateforme et garant, si l'hypothèse est explicite.

**Erreurs fréquentes**
- Attribuer à la holding une part en hausse parce qu'elle « souscrit » : elle ne fait que maintenir sa quote-part.
- Oublier que les droits cédés par BRESKANE sont exercés par leurs acheteurs : la somme des parts n'est plus égale à 100 %.
- Diviser le résultat avec augmentation de capital par 30 000 000 d'actions.
- `JUR-T13` — commentaire général sur la dilution sans le conflit entre la famille et le fonds ; `JUR-T14` — dilution du BPA présentée comme une perte de valeur certaine.

---

### 3.4 Structure financière avant et après l'opération (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Tableau : dette, dette / capitaux propres et ratio de la clause, avec et sans dettes locatives, au 31/12/2029 sans et avec augmentation de capital | 1 |
| 3.4-02 | Lecture comparée et conclusion sur l'arbitrage fonds propres / dette, avec le ratio de 1,90 de la fin de 2026 | 1 |

**Structure financière (M€)** (annexes 3.1 et 3.6 ; produit net 81,48 M€)

| | 31/12/2029 sans augmentation de capital | 31/12/2029 avec augmentation de capital |
|---|---:|---:|
| Dette financière nette hors dettes locatives | 180,00 | 180,00 − 81,48 = **98,52** |
| Dettes locatives | 290,00 | 290,00 |
| Dette financière nette totale | **470,00** | **388,52** |
| Capitaux propres consolidés | 420,00 | 420,00 + 81,48 = **501,48** |
| **Sans dettes locatives** : DFN hors dettes locatives / capitaux propres | 42,86 % | **19,65 %** |
| **Sans dettes locatives** : ratio de la clause, DFN hors dettes locatives / (EBITDA − loyers) | 180,00 / 48,00 = **3,75** | 98,52 / 48,00 = **2,05** |
| **Avec dettes locatives** : DFN totale / capitaux propres | 111,90 % | **77,47 %** |
| **Avec dettes locatives** : DFN totale / EBITDA | 470,00 / 112,00 = **4,20** | 388,52 / 112,00 = **3,47** |

- **Sans l'opération**, le ratio de la clause double presque par rapport à la fin de 2026 (3,75 contre 1,90) et dépasse le seuil de 2,50 ; dettes locatives comprises, la dette dépasserait les capitaux propres (111,90 %) et atteindrait 4,20 fois l'EBITDA.
- **Avec l'opération**, la dette hors dettes locatives ne représente plus que 19,65 % des capitaux propres (42,86 % sans l'opération), et 77,47 % dettes locatives comprises (111,90 %) : les fonds propres absorbent l'essentiel de l'effort d'investissement. Le ratio de la clause (2,05) reste supérieur à celui de 2026 (1,90) : le plan est financé pour près de la moitié par la dette et l'autofinancement. La marge sous le seuil est de 2,50 × 48,00 − 98,52 = 21,48 M€.
- Les **dettes locatives** (290,00 M€) représentent près de trois fois la dette hors dettes locatives après l'opération (98,52 M€) ; elles ne sont pas réduites par l'opération et la lecture « avec dettes locatives » reste celle des investisseurs qui assimilent les loyers à une dette.

**Conclusion (1 pt, avec la lecture ci-dessus)** : l'arbitrage ne consiste pas à choisir entre la dette et les fonds propres, mais à les combiner. Les fonds propres absorbent le dépassement de la clause et reconstituent une marge de sécurité ; la dette et l'autofinancement financent le reste, à un coût plus faible. Le montant de 84 M€ est cohérent avec le besoin minimal (60,00 M€ nets) augmenté d'une marge face à un marché en recul. La trésorerie levée en juin 2027 ne sera utilisée qu'en 2028 et 2029 (ratio de 0,26 fin 2027) : le groupe paie dès 2027 le coût des fonds propres pour un besoin futur, ce que justifie la fenêtre ouverte par l'engagement de la famille et la garantie bancaire.

**Réponses tolérées** : ratios hors dettes locatives exprimés aussi en multiple de l'EBITDA publié (180,00 / 112,00 = 1,61 ; 98,52 / 112,00 = 0,88), si le candidat précise qu'ils ne sont pas ceux de la clause ; gearing exprimé en multiple (0,7747).

**Erreurs fréquentes**
- Déduire le montant brut (84,00 M€) au lieu du produit net (81,48 M€) de la dette.
- Mélanger les deux lectures : ratio de la clause calculé avec les dettes locatives, ou dettes locatives rapportées à (EBITDA − loyers).
- Ajouter le produit net à la dette au lieu de le retrancher.
- `JUR-T07` — ratios présentés en texte, sans tableau comparatif ; `JUR-T13` — conclusion qui ne chiffre pas la marge sous le seuil.

---

### 3.5 Cours observés et efficience informationnelle (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Écarts au 14/06 : action 8,70 € contre 9,00 € (− 3,33 %) ; droit 0,68 € contre 0,80 € (− 15,00 %) ; cohérence : 2,5 × 0,68 + 7,00 = 8,70 € | 0,5 |
| 3.5-02 | Interprétation : formes de l'efficience, intégration de l'information publique, pression vendeuse, limites | 1 |

**Écarts** (annexe 3.4) : le 14 juin, l'action cote 8,70 €, soit 8,70 / 9,00 − 1 = **− 3,33 %** par rapport au cours théorique ; le droit cote 0,68 €, soit 0,68 / 0,80 − 1 = **− 15,00 %**. Le droit et l'action restent cohérents : obtenir une action en achetant 2,5 droits et en payant le prix d'émission coûte 2,5 × 0,68 + 7,00 = **8,70 €**, exactement le cours de l'action. Aucune opération d'arbitrage entre le droit et l'action ne rapporte de gain. Cette cohérence se vérifie à chaque date de la période (par exemple le 9 juin : 2,5 × 0,72 + 7,00 = 8,80 €).

**Interprétation (1 pt)** [F10 ; F06 § 3].
- **Le cours théorique n'est pas une prévision** : c'est la valeur mécanique de l'action après l'émission, à information inchangée. Un écart ne prouve pas une inefficience : il traduit des informations nouvelles publiées après le détachement.
- **Efficience semi-forte** (Fama, 1970) : les cours intègrent rapidement l'information publique. Entre le 7 et le 9 juin, période de l'avertissement d'un distributeur européen de vélos, l'action recule de 1,12 % et l'indice sectoriel de 2,10 % (le tableau ne retient que des séances choisies : la variation couvre deux séances). Du 3 au 14 juin, l'indice perd 2,69 % (2,50 % depuis le 2 juin) : la plus grande partie de l'écart de − 3,33 % reflète une information publique nouvelle sur le secteur (baisse des prix, stocks), non une erreur de prix. La baisse propre au titre se concentre sur le 7 juin (− 1,66 % pour un indice à − 0,30 %), jour de l'annonce de BRESKANE Capital. Le droit baisse plus fort que l'action parce qu'il vaut la différence entre le cours et un prix d'émission fixe : il amplifie les variations de l'action (effet de levier du droit).
- **Efficience faible** : rien dans la série ne permet d'exploiter les cours passés ; la baisse du droit et de l'action d'une séance à l'autre suit les informations publiées, non une tendance prévisible. La cohérence permanente entre le cours du droit et celui de l'action (aucun gain d'arbitrage) montre en outre que deux actifs liés intègrent la même information au même instant, comme le suppose un marché efficient où l'arbitrage est possible [F06 § 3.1, conditions].
- **Limites** : la vente de 1 800 000 droits annoncée le 7 juin par BRESKANE crée une pression vendeuse temporaire sur un titre de taille moyenne (− 1,66 % le 7 juin, quand l'indice ne perd que 0,30 %). L'annonce peut aussi être lue comme un signal négatif émis par un actionnaire informé. Sur un marché parfaitement efficient et liquide, une vente sans information nouvelle ne devrait pas peser durablement sur le cours. La forme forte n'est pas vérifiée : la famille et la direction disposent d'informations privées sur le plan.
- **Conséquence pour ERVIDANE** : si le marché est efficient, choisir le « bon moment » pour émettre a un rôle limité ; l'essentiel est la qualité de l'information diffusée. Le cours (8,70 €) reste 24,29 % au-dessus du prix d'émission : la souscription reste intéressante et la garantie ne devrait jouer que pour le solde.

**Réponses tolérées** : lecture comportementale en complément (sur-réaction à l'avertissement du concurrent, mimétisme, aversion aux pertes des petits porteurs, Kahneman et Tversky, 1973) ; écart exprimé en euros (− 0,30 € et − 0,12 €).

**Erreurs fréquentes**
- Conclure à l'inefficience du marché parce que le cours s'écarte du cours théorique, sans tenir compte de l'information publiée après le détachement.
- Calculer une rentabilité anormale ou mener une analyse statistique des cours : la question est qualitative [V guide p. 74].
- Confondre les trois formes d'efficience ou affirmer qu'Euronext est efficient au sens fort [F10].
- `JUR-M01` — efficience présentée sans Fama (1970) ; `JUR-T13` — interprétation qui ne cite ni le 7 ni le 9 juin.

---

### 3.6 Plateforme, algorithmes et tranche ouverte aux particuliers (4,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Tranche : 8 000 × 700 € = 5,60 M€ ; 800 000 actions ; 1,90 % du capital après l'opération | 0,5 |
| 3.6-02 | Rôle des nouveaux acteurs face au syndicat bancaire : coût, accès, protection de l'investisseur, garantie | 1,5 |
| 3.6-03 | Algorithmes et IA : allocation, tenue de marché, échanges à haute fréquence ; risques | 1,5 |
| 3.6-04 | Intérêt pour une société à mission et recommandation | 1 |

**Tranche TALMERIS** (annexe 3.5) : 8 000 souscripteurs × 700 € = **5,60 M€**, soit 5 600 000 / 7,00 = **800 000 actions**, **1,90 %** du capital après l'opération (800 000 / 42 000 000). La tranche représente 6,67 % de l'émission et 34,63 % des actions prises par les nouveaux actionnaires (800 000 sur 2 310 000) : elle réduit d'autant les actions que la banque garante devrait conserver. Elle ne coûte rien de plus à ERVIDANE : la commission de 1,00 % (56 000 €) est prélevée sur celle du syndicat.

**Rôle des nouveaux acteurs face au syndicat bancaire (1,5 pt)** [F06 § 1 et 6 ; V programme l. 599-601].
- **Fonctions du syndicat** : dans un financement direct par le marché, les banques construisent le livre d'ordres, conseillent sur le prix, placent les titres auprès des investisseurs institutionnels et **garantissent** le succès de l'opération ; elles réduisent l'asymétrie d'information par leur réputation et leur engagement financier (49,56 M€ garantis ici). Ce service a un coût : 3,00 % du montant brut, soit 2,52 M€.
- **Ce qu'apporte la plateforme** : un **accès** direct des particuliers au marché primaire, au même prix que les institutionnels, dès une action et sans frais pour l'investisseur, alors qu'ils passaient par leur banque de détail avec des délais et des frais ; un **coût** faible pour l'émetteur ; une diversification de la base d'investisseurs.
- **Limites** : la plateforme **ne garantit rien** et ne remplace pas le syndicat : si la demande manque, les banques achètent les titres invendus. Elle complète le financement direct sans supprimer l'intermédiation.
- **Protection de l'investisseur** : agrément comme prestataire de services d'investissement, questionnaire de connaissances, avertissement sur le risque de perte en capital, contrôles d'identité et de lutte contre le blanchiment. Le risque principal reste la souscription par fidélité à une marque, par des épargnants peu avertis qui investissent une épargne non disponible ou concentrent leur patrimoine sur un seul titre.

**Algorithmes et intelligence artificielle (1,5 pt)** [F06 § 6, S].
- **Allocation des titres** : la plateforme applique un algorithme aux règles publiées à l'avance (50 premières actions servies à chacun, puis prorata), ce qui favorise une allocation large et transparente ; un outil d'IA repère les demandes multiples. Les banques utilisent l'IA pour classer les investisseurs selon leur comportement passé et servir d'abord les investisseurs de long terme. Risques : opacité des critères (« boîte noire »), biais des données, traitement inégal d'investisseurs comparables.
- **Tenue de marché et échanges à haute fréquence** : pendant la négociation des droits, des teneurs de marché et des opérateurs à haute fréquence achètent et vendent en continu l'action et le droit. Ils apportent la liquidité nécessaire aux petits porteurs qui cèdent leurs droits et maintiennent la cohérence des prix entre le droit et l'action (question 3.5 : 2,5 × 0,68 + 7,00 = 8,70 €). Ils accélèrent ainsi l'intégration de l'information.
- **Risques** : retrait brutal de la liquidité si le marché se retourne, amplification des baisses quand des programmes semblables réagissent de la même manière (mimétisme algorithmique, krach éclair), course à la vitesse au détriment des investisseurs lents, risque de manipulation et risque cyber. Ces pratiques sont encadrées et surveillées par les autorités de marché (contrôle des algorithmes) [F06 § 6, S].

**Intérêt pour une société à mission et recommandation (1 pt).**
- **Cohérence avec la mission** : la raison d'être est de « rendre le vélo accessible à chacun ». Ouvrir le capital aux clients et aux cyclistes de la communauté prolonge cette logique : les parties prenantes deviennent actionnaires, ce qui rapproche la valeur actionnariale de la valeur partenariale (Freeman, 1984) [F10].
- **Intérêt financier** : la tranche est modeste (5,60 M€, 1,90 % du capital), mais elle diversifie la base d'actionnaires, crée une communauté plus stable face à un fonds activiste, renforce la fidélité commerciale et réduit l'engagement du garant sans coût supplémentaire.
- **Risques** : un échec visible de la tranche ou une baisse du cours sous 7,00 € ferait perdre de l'argent à des clients, avec un risque d'image fort pour une société à mission ; la communication doit éviter toute incitation commerciale à investir (pas d'avantage en magasin lié à la souscription) et rappeler le risque de perte.
- **Recommandation** : maintenir la tranche, avec une communication sobre et équilibrée sur les risques, un plafond de souscription par personne, des règles d'allocation publiées et une information régulière des actionnaires particuliers sur les indicateurs de la mission. Le comité de mission peut en suivre les effets.

**Réponses tolérées** : comparaison avec le financement participatif (plateformes pour sociétés non cotées), si le candidat la limite à la différence de marché (coté / non coté) ; mention de la blockchain ou de la tokenisation des titres comme évolution possible, si elle reste reliée au cas.

**Erreurs fréquentes**
- Présenter la plateforme comme un substitut au syndicat bancaire, capable de garantir l'émission.
- Développer la technique informatique des algorithmes ou le détail juridique de l'agrément : la question porte sur leur rôle et leurs risques [F06 § 8].
- Ne présenter que des avantages, sans la protection des épargnants peu avertis.
- `JUR-M02` — nouveaux acteurs décrits sans comparaison avec les intermédiaires traditionnels ; `JUR-T05` — intérêt pour la société à mission non relié à la raison d'être ; `JUR-T13` — réponse sans les données de l'annexe 3.5.
