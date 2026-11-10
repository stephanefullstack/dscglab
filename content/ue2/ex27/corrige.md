# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 27 — Dossier 3 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F05 ingénierie financière, F09 éthique, conformité et réglementation bancaire, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (bilans d'ouverture, tableaux d'amortissement, annuités, TRI, rapport dette senior / EBITDA, barème, liste noire, hors-programme ; dividendes, service de la dette, marges, trésorerie cumulée, couvertures, structures de financement et valeurs de sortie vérifiés par script).

Bien que le corrigé mentionne des auteurs et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une condition de réussite vérifiée avec un dividende erroné, ou un TRI calculé avec une trésorerie cumulée erronée).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Asymétrie d'information et sélection adverse dans le rachat par les cadres | `5.1.b` Maîtriser les enseignements des asymétries d'information (Akerlof, 1970) | 2 |
| 3.2 Montage proposé : schéma, bilan de la holding, dette senior, dividendes et condition de réussite | `4.2.d` Décrypter les montages financiers avec et sans levier financier | 5 |
| 3.3 Rentabilités exigées par la banque, le prêteur junior et le fonds | `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché | 1,5 |
| 3.4 Limite de la dette senior et réglementation bancaire ; fonds de dette privée | `2.2.b` Mettre en œuvre la déontologie, la conformité et l'organisation déontologique (réglementation bancaire) | 2 |
| 3.5 Variantes de financement : structure et capacité de remboursement | `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière | 2 |
| 3.6 Effet de levier, théories du choix de financement et recommandation | `4.2.d` Décrypter les montages financiers ; `7.2.d` Étudier les arbitrages dans les choix de financement à l'aide des théories explicatives ; `7.2.b` | 3,5 |
| **Total** | | **16** |

Part du calcul : environ 7 points (3.2-02 à 3.2-05, 3.3-01, 3.5-01 à 3.5-03, 3.6-01 et 3.6-02). Part de l'analyse : environ 9 points. Le dossier se termine par une recommandation qui pèse 1,5 point avec les théories : il ne doit pas être bâclé faute de temps (`JUR-T15`).

---

### 3.1 Asymétrie d'information et sélection adverse (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Notion d'asymétrie d'information et identification des parties informées et non informées dans le cas | 0,5 |
| 3.1-02 | Sélection adverse au sens d'Akerlof (1970), appliquée au rachat par les cadres | 0,5 |
| 3.1-03 | Conséquences sur le prix et pour chacune des parties (groupe vendeur, fonds, cadres) | 0,5 |
| 3.1-04 | Moyens de réduire l'asymétrie, adaptés au cas | 0,5 |

**Notion et parties (0,5 pt).** Il y a asymétrie d'information quand une partie à une transaction dispose d'informations que l'autre n'a pas sur la qualité de ce qui est échangé. Dans un rachat d'une entreprise par ses dirigeants, ce sont les **acquéreurs** qui sont les mieux informés :
- Mme ORTAVEL et les cinq cadres dirigent la filiale au quotidien : ils ont **préparé eux-mêmes les prévisions** reprises dans le plan stratégique du groupe et ils connaissent les premières commandes de la gamme de diffuseurs rechargeables, qu'ils jugent « encourageantes » sans les avoir chiffrées (annexe 3.1) ;
- **AURÉVANCE SA**, le vendeur, ne connaît la filiale qu'à travers les informations que lui transmet cette équipe, et n'a ni mis la filiale en concurrence ni fait établir d'évaluation indépendante ;
- **SERVANCE Capital**, associé des cadres mais moins informé qu'eux, a fondé son offre sur les prévisions de la direction et sur un audit limité aux comptes passés, dans un secteur qu'il ne connaît pas.

**Sélection adverse (0,5 pt).** Selon Akerlof (1970), lorsque l'acheteur ne peut pas distinguer la qualité des biens, il propose un prix moyen ; les vendeurs des meilleurs biens se retirent, la qualité moyenne baisse et le marché peut disparaître. Ici, le mécanisme joue en sens inverse du marché des voitures d'occasion, puisque c'est l'**acheteur** qui est informé : les cadres n'ont intérêt à acheter que si la filiale vaut **plus** que le prix qu'ils offrent. Le fait même qu'ils proposent 38,0 M€ est donc une information pour le vendeur : une offre acceptée a plus de chances d'être une offre trop basse. Le groupe risque de céder à bas prix une filiale dont les perspectives sont meilleures que celles qui figurent dans son plan.

**Conséquences (0,5 pt).**
- **Pour AURÉVANCE SA et sa fondation actionnaire** : risque de céder sous la valeur (transfert de valeur vers les acquéreurs) ; à l'inverse, un vendeur qui se sait mal informé réagit en exigeant une prime ou en refusant de vendre, ce qui peut faire échouer une opération créatrice de valeur.
- **Pour SERVANCE Capital** : le fonds est lui aussi moins informé que les cadres ; il peut craindre des prévisions trop optimistes (les cadres ont intérêt à rassurer le fonds pour obtenir son financement) ou trop prudentes (pour obtenir un prix bas du vendeur). Il s'en protège en exigeant une rentabilité élevée (question 3.3), des garanties, et en demandant aux cadres d'investir une part significative de leur patrimoine (5,0 M€), ce qui aligne leurs intérêts sur les siens.
- **Pour les cadres** : ils captent la valeur de leur information, mais doivent convaincre deux partenaires méfiants ; la négociation peut aussi créer un conflit d'intérêts, puisqu'ils restent dirigeants salariés de la filiale du groupe pendant la négociation (question de loyauté envers leur employeur, à mentionner sans développement juridique).
- Plus largement, l'asymétrie renchérit le financement (prime exigée par le fonds et les prêteurs) et peut conduire à un rationnement (la banque limite sa dette senior, question 3.4).

**Moyens de réduire l'asymétrie (0,5 pt).**
- **Information communiquée** : exiger des cadres une mise à jour chiffrée des prévisions, intégrant les commandes de la nouvelle gamme, et ouvrir aux acquéreurs comme au groupe les mêmes données (chiffre d'affaires mensuel, carnet de commandes, conditions des distributeurs).
- **Évaluation indépendante** : faire évaluer la filiale par un expert qui ne dépend ni des acquéreurs ni du vendeur, avec un plan d'affaires établi ou revu par la direction financière du groupe.
- **Mise en concurrence** : solliciter d'autres acquéreurs, industriels ou financiers, à l'issue de la période d'exclusivité (30 avril 2027) ; le prix révélé par la concurrence réduit l'avantage informationnel des cadres.
- **Complément de prix conditionné aux résultats** : prévoir qu'une partie du prix soit versée plus tard si l'EBITDA de la filiale dépasse les prévisions (par exemple celui de 2028 ou de 2029). Si les cadres sont sincères, le complément ne leur coûte rien ; s'ils anticipent mieux, le groupe en partage le bénéfice. C'est un mécanisme d'auto-sélection.

**Réponses tolérées** : référence à la théorie du signal (Spence, 1973) pour l'investissement personnel des cadres, présenté comme un signal coûteux de leur confiance ; mention de l'aléa moral (comportement des dirigeants après l'opération) si elle est distinguée de la sélection adverse ; tout autre moyen pertinent (déclarations et garanties données par les acquéreurs, audit indépendant des prévisions).

**Erreurs fréquentes**
- `JUR-M01` et `JUR-T14` — confondre sélection adverse (avant le contrat) et aléa moral (après) ; présenter le vendeur comme la partie la mieux informée sans le justifier.
- `JUR-T13` — exposé théorique sans lien avec les données du cas (prévisions préparées par les acquéreurs, nouvelle gamme non chiffrée, audit limité).
- Développer les obligations juridiques des dirigeants ou le contenu d'une garantie de passif : hors programme (UE 1).

**Références** : Akerlof (1970), Spence (1973) [V programme 5.1 et 4.1 ; F10] ; périmètre 5.1.b, « mécanismes d'Akerlof : sélection adverse » [V guide p. 73].

---

### 3.2 Montage proposé et condition de réussite (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Schéma du montage | 0,5 |
| 3.2-02 | Bilan d'ouverture de la holding : actif 39,00 (titres 38,00 ; frais 1,00) ; fonds propres 20,00 (cadres 5,00 ; SERVANCE 15,00), dette senior 12,00, dette junior 7,00 | 0,5 |
| 3.2-03 | Annuité de la dette senior : 2,77 ; tableau d'amortissement (intérêts, amortissement, capital restant dû) | 1 |
| 3.2-04 | Résultat net et dividende de la filiale : 2,850 ; 3,180 ; 3,510 ; 3,765 ; 3,945 (intérêts de l'emprunt de la filiale et IS compris) | 1 |
| 3.2-05 | Service de la dette 3,40 ; marges, trésorerie cumulée et taux de couverture de 2027 à 2031 | 1 |
| 3.2-06 | Conclusion : condition non respectée en 2027 et en 2028, trésorerie de la holding négative jusqu'en 2030 ; fragilités du montage (plan des acquéreurs, distribution de 100 % du résultat, endettement total) | 1 |

**Schéma (0,5 pt).**

```
   Six cadres (5,0 M€, 25 %)     SERVANCE Capital (15,0 M€, 75 %)
                 \                     /
                  fonds propres 20,0 M€
                          |
   Banque SOLMIRANE ---> AMBRÉLIA Participations SAS <--- CAVERIA Dette Privée
   dette senior 12,0 M€   (holding de reprise)            dette junior 7,0 M€
   (annuités, 5 ans)              |        ^              (in fine, 9 %)
                       prix 38,0  |        | dividendes = 100 % du résultat net
                       (+ frais 1,0)       |
                                  v        |
          AURÉVANCE SA ---cède 100 %---> AURÉVANCE Maison SAS
          (reçoit 38,0 M€)                 (conserve sa dette financière nette de 3,0 M€)
```

La holding acquiert 100 % des titres ; elle rembourse ses dettes avec les dividendes que lui verse la filiale ; la dette de la filiale reste à la filiale.

**Bilan d'ouverture d'AMBRÉLIA Participations au 1er janvier 2027 (0,5 pt, M€).**

| Actif | M€ | Passif | M€ | % |
|---|---:|---|---:|---:|
| Titres AURÉVANCE Maison SAS | 38,00 | Fonds propres (cadres 5,00 ; SERVANCE Capital 15,00) | 20,00 | 51,28 |
| Frais d'acquisition | 1,00 | Dette senior (Banque SOLMIRANE) | 12,00 | 30,77 |
| | | Dette junior (CAVERIA Dette Privée) | 7,00 | 17,95 |
| **Total** | **39,00** | **Total** | **39,00** | **100,00** |

Les frais d'acquisition peuvent être présentés inclus dans le coût des titres (39,00).

**Dette senior : annuité et tableau d'amortissement (1 pt).** Annuité constante = 12,0 × 0,05 / (1 − 1,05^−5) = **2,77 M€** (2,7717).

| Année | Capital début | Intérêts (5 %) | Amortissement | Annuité | Capital restant dû |
|---|---:|---:|---:|---:|---:|
| 2027 | 12,00 | 0,60 | 2,17 | 2,77 | 9,83 |
| 2028 | 9,83 | 0,49 | 2,28 | 2,77 | 7,55 |
| 2029 | 7,55 | 0,38 | 2,39 | 2,77 | 5,15 |
| 2030 | 5,15 | 0,26 | 2,51 | 2,77 | 2,64 |
| 2031 | 2,64 | 0,13 | 2,64 | 2,77 | 0,00 |

La dette junior ne s'amortit pas : intérêts de 7,0 × 9 % = **0,63 M€** par an, capital de 7,0 M€ remboursé lors de la cession de la filiale (fin 2031), sur le produit de la cession.

**Dividendes remontés (1 pt, M€).** Intérêts de l'emprunt de la filiale : 5 % du capital restant dû au début de l'année (4,0 ; 3,2 ; 2,4 ; 1,6 ; 0,8).

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| EBITDA | 5,40 | 5,80 | 6,20 | 6,50 | 6,70 |
| − Dotations aux amortissements | 1,40 | 1,40 | 1,40 | 1,40 | 1,40 |
| = Résultat d'exploitation | 4,00 | 4,40 | 4,80 | 5,10 | 5,30 |
| − Intérêts de l'emprunt de la filiale | 0,20 | 0,16 | 0,12 | 0,08 | 0,04 |
| = Résultat avant impôt | 3,80 | 4,24 | 4,68 | 5,02 | 5,26 |
| − IS (25 %) | 0,950 | 1,060 | 1,170 | 1,255 | 1,315 |
| **= Résultat net = dividende versé (100 %)** | **2,850** | **3,180** | **3,510** | **3,765** | **3,945** |

Total des dividendes de 2027 à 2031 : 17,250 M€.

**Condition de réussite (1 pt, M€).** Service de la dette = 2,7717 + 0,63 = **3,40 M€** par an.

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Dividende reçu | 2,850 | 3,180 | 3,510 | 3,765 | 3,945 |
| Annuité senior | 2,77 | 2,77 | 2,77 | 2,77 | 2,77 |
| Intérêts junior | 0,63 | 0,63 | 0,63 | 0,63 | 0,63 |
| **Service de la dette** | **3,40** | **3,40** | **3,40** | **3,40** | **3,40** |
| Marge (dividende − service) | −0,55 | −0,22 | 0,11 | 0,36 | 0,54 |
| Trésorerie cumulée de la holding | −0,55 | −0,77 | −0,67 | −0,30 | 0,24 |
| Taux de couverture | 0,84 | 0,93 | 1,03 | 1,11 | 1,16 |

**Conclusion (1 pt).**
- La condition de réussite **n'est pas respectée en 2027 et en 2028** : les dividendes ne couvrent que 84 % puis 93 % du service de la dette. La holding, qui n'a pas d'autre ressource, ne peut pas payer ses échéances : il lui manque 0,55 M€ dès la fin de 2027, et sa trésorerie cumulée reste **négative jusqu'en 2030** (−0,77 M€ au plus bas, fin 2028). Le montage n'est pas finançable en l'état.
- Même les années excédentaires (2029 à 2031), la marge reste faible (couverture de 1,03 à 1,16) : le moindre écart au plan ferait réapparaître un déficit. Le candidat qui relève que la banque exige une couverture d'au moins 1,10 (annexe 3.4, question 3.5) peut le signaler ici, sans que ce soit attendu.
- Le montage est fragile pour d'autres raisons : il suppose la **réalisation intégrale d'un plan préparé par les acquéreurs eux-mêmes** (question 3.1), avec un EBITDA qui passe de 5,2 M€ en 2026 à 6,7 M€ en 2031 (+ 28,8 %) ; il suppose une **distribution de 100 % du résultat net**, alors que la filiale doit aussi rembourser 0,8 M€ par an de son propre emprunt et financer ses investissements et la hausse de son besoin en fonds de roulement avec sa trésorerie : un résultat n'est pas une trésorerie, et le dividende versé risque de priver la filiale des moyens de son développement ; l'endettement total qui pèse sur l'ensemble (19,0 M€ dans la holding et 3,0 M€ dans la filiale, soit 22,0 M€) atteint 4,23 fois l'EBITDA de 2026.
- Pour le groupe, un montage qui échouerait après la cession mettrait en difficulté une filiale qui porte sa marque : le financement doit être ajusté (question 3.5).

**Réponses tolérées** : bilan présenté en pourcentages arrondis à une décimale ; tableau d'amortissement calculé à partir de valeurs arrondies, à 0,01 près ; dividendes arrondis à deux décimales (2,85 ; 3,18 ; 3,51 ; 3,77 ou 3,76 ; 3,95 ou 3,94), à condition que la conclusion soit la même ; trésorerie cumulée obtenue en additionnant les marges arrondies ; rapport 22,0 / 5,2 non demandé (facultatif).

**Erreurs fréquentes**
- `JUR-I01` — annuité de la dette senior mal calculée : calcul faux avec un amortissement constant (12,0 / 5 = 2,40 + intérêts de 0,60 = 3,00 la première année, et une annuité décroissante) ou avec des intérêts constants (2,40 + 0,60 = 3,00 chaque année), au lieu de a = 12,0 × 0,05 / (1 − 1,05^−5) = 2,77.
- `JUR-I02` — confondre le prix (38,0 M€) et la dette ; oublier les frais d'acquisition dans les emplois ; amortir la dette junior, ou inclure son capital (7,0 M€) dans le service de 2031 alors qu'il est remboursé sur le produit de la cession.
- Comparer le dividende à la seule annuité senior (oubli des intérêts junior de 0,63) ; calculer le dividende sur le résultat d'exploitation, sans les intérêts de l'emprunt de la filiale ni l'IS.
- Développer l'imposition de la holding ou des dividendes qu'elle reçoit : hors programme (UE 1) ; l'énoncé pose qu'aucun impôt n'est pris en compte au niveau de la holding.

**Références** : mécanismes du LBO, schéma, bilan de la holding, tableaux d'amortissement, condition de réussite (dividendes reçus ≥ service de la dette) [V guide p. 70 ; sujet zéro p. 85-86 et corrigé p. 100-101 ; F05 § 1.2] ; annuité constante [F01].

---

### 3.3 Rentabilités exigées par les apporteurs de capitaux (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Rentabilités et primes par rapport au taux sans risque : banque 5 % (+ 1,5 point) ; prêteur junior 9 % (+ 5,5 points) ; fonds 15 % au moins (+ 11,5 points) | 0,5 |
| 3.3-02 | Hiérarchie expliquée par le rang de remboursement, les garanties, le calendrier de remboursement et l'incertitude des flux reçus | 0,5 |
| 3.3-03 | Lecture : la rentabilité exigée rémunère le risque supporté ; celle des fonds propres dépend de l'endettement de la holding | 0,5 |

**Calcul (0,5 pt).** Taux sans risque : 3,5 %.

| Apporteur | Rentabilité exigée | Prime de risque | Nature de la rémunération |
|---|---:|---:|---|
| Banque SOLMIRANE (dette senior) | 5,0 % | 1,5 point | taux contractuel, payé chaque année |
| CAVERIA Dette Privée (dette junior) | 9,0 % | 5,5 points | taux contractuel, intérêts annuels, capital à la cession (fin 2031 dans l'hypothèse de sortie) |
| SERVANCE Capital (fonds propres) | 15 % au moins | 11,5 points au moins | rentabilité espérée, aucun revenu avant la sortie |

**Hiérarchie (0,5 pt).** Plus un apporteur supporte d'incertitude sur le montant et la date des flux qu'il recevra, plus la rentabilité qu'il exige est élevée.
- **La banque** est remboursée en premier, chaque année : son exposition diminue dès 2027 (capital restant dû de 9,83 M€ fin 2027, nul fin 2031) ; elle bénéficie de garanties (titres de la filiale, couverture minimale de 1,10, interdiction des distributions). Son risque est faible : prime de 1,5 point.
- **Le prêteur junior** n'est remboursé qu'après la banque, en une seule fois et sur le produit de la cession : son exposition reste de 7,0 M€ pendant cinq ans et dépend de la valeur de sortie. Prime de 5,5 points.
- **Le fonds**, comme les cadres, est **créancier résiduel** : il ne reçoit rien avant la sortie et ne perçoit que ce qui reste après le remboursement de toutes les dettes. Toute variation de la valeur de sortie se reporte d'abord sur lui. C'est le risque le plus élevé, d'où la prime la plus forte.

**Lecture (0,5 pt).** Le taux de la banque est un taux promis, quasi certain si le montage tient ; les 15 % du fonds sont un **objectif** : la rentabilité effective peut être très différente (question 3.6). La prime exigée par les associés dépend aussi de l'**endettement de la holding** : plus la dette est élevée, plus la part résiduelle des associés est risquée, et plus la rentabilité qu'ils doivent exiger est forte. Un montage moins endetté justifie donc, pour un même actif, une rentabilité exigée des fonds propres plus faible.

**Réponses tolérées** : primes exprimées en pourcentage ; référence au MEDAF ou à la relation risque-rentabilité sans calcul ; mention de l'illiquidité des titres d'une société non cotée comme composante de la prime exigée par le fonds.

**Erreurs fréquentes**
- `JUR-T14` — présenter la dette junior comme moins risquée que la dette senior parce qu'elle « rapporte plus » ; confondre le taux d'intérêt promis et la rentabilité espérée des fonds propres.
- Comparer les taux sans les rattacher au rang de remboursement et aux données du cas (`JUR-T13`).

**Références** : lien entre incertitude, risque et rentabilité exigée, interprétation de la prime de risque [V guide p. 74-75 ; périmètre 5.2.a] ; taux sans risque de 3,5 %, hypothèse d'énoncé cohérente avec F11 [S].

---

### 3.4 Limite de la dette senior et réglementation bancaire (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Exigences de fonds propres proportionnées au risque et rôle de la notation de l'emprunteur | 0,5 |
| 3.4-02 | Exigences de liquidité : ressources stables, actifs liquides, durée et amortissement des crédits | 0,5 |
| 3.4-03 | Effets sur le montant (12,0 M€, 2,31 fois l'EBITDA), le taux (5 %, plus de 6,5 % au-delà) et les conditions du crédit (garantie, couverture, distributions) | 0,5 |
| 3.4-04 | Place des fonds de dette privée dans la partie junior | 0,5 |

**Fonds propres et notation (0,5 pt).** Les accords de Bâle III, finalisés en 2017 et appliqués dans l'Union européenne par le règlement CRR3 depuis le 1er janvier 2025, imposent aux banques de détenir des fonds propres en proportion des risques qu'elles prennent. Un crédit consenti à un emprunteur risqué mobilise davantage de fonds propres, ressource rare et coûteuse pour la banque. La **notation** de l'emprunteur (ici la notation interne de la Banque SOLMIRANE) mesure ce risque : une holding qui ne vit que des dividendes de sa filiale et dont le remboursement dépend de la réussite du plan est moins bien notée qu'une entreprise industrielle comparable. Le taux du crédit doit couvrir le coût de ces fonds propres et le **coût du risque**, c'est-à-dire les défauts anticipés sur cette catégorie d'emprunteurs.

**Liquidité (0,5 pt).** Bâle III a aussi introduit des exigences de **liquidité** : la banque doit détenir une réserve d'actifs liquides et financer ses crédits longs par des ressources stables de durée comparable. Elle limite donc la durée de ses crédits les plus risqués (cinq ans au plus) et exige un amortissement régulier, qui réduit rapidement son exposition.

**Effets sur le crédit (0,5 pt).**
- **Montant** : la dette senior est plafonnée à 12,0 M€, soit 12,0 / 5,2 = **2,31 fois l'EBITDA de 2026** ; au-delà, l'opération changerait de catégorie de risque et consommerait beaucoup plus de fonds propres.
- **Taux** : 5 % jusqu'à 12,0 M€, plus de 6,5 % au-delà : le prix du crédit suit la notation.
- **Conditions** : garantie sur les titres de la filiale, couverture du service de toutes les dettes de la holding par les dividendes d'au moins 1,10 chaque année, interdiction de toute distribution aux associés avant le remboursement, remboursement prioritaire. Ces conditions contractuelles ne sont pas des ratios réglementaires : elles traduisent la manière dont la banque protège un crédit qui lui coûte cher en fonds propres.
- Le montage proposé (couverture de 0,84 en 2027) ne respecte pas l'exigence de la banque, qui n'accordera pas son crédit sans ajustement.

**Fonds de dette privée (0,5 pt).** CAVERIA Dette Privée n'est pas une banque : ce fonds, géré par une société de gestion et souscrit par des assureurs et des caisses de retraite, n'est pas soumis aux mêmes exigences de fonds propres et de liquidité que les banques, et ses souscripteurs ont des engagements longs. Il peut accepter un risque plus élevé (remboursement après la banque, in fine, jusqu'à sept ans, échéance 2033) contre une rémunération plus forte (9 %). La réglementation bancaire a ainsi favorisé une **désintermédiation** partielle du financement des rachats à effet de levier : la banque garde la partie la moins risquée, les fonds de dette prennent la partie junior. Pour la holding, cette dette est plus chère mais ne pèse pas sur sa trésorerie avant la sortie, puisque seuls les intérêts sont payés chaque année.

**Réponses tolérées** : mention des trois piliers de Bâle (exigences minimales, surveillance prudentielle, discipline de marché) ; mention des agences de notation ou de la cotation de la Banque de France comme sources de notation ; tout exemple cohérent d'effet de la réglementation sur la relation banque-entreprise (sélectivité, garanties, préférence pour les crédits courts).

**Erreurs fréquentes**
- Calculer un ratio de fonds propres ou de liquidité de la banque, ou citer des pourcentages réglementaires : hors programme (le programme n'attend que les principes, aucun ratio de la banque n'est à établir).
- Confondre la couverture de 1,10 demandée par la banque (condition contractuelle du crédit) et un ratio réglementaire imposé à la banque.
- `JUR-T13` — exposé général sur Bâle III sans lien avec le plafond de 12,0 M€, le taux et les conditions du cas.

**Références** : principes de Bâle III, effets sur l'accès au crédit, influence de la notation [V guide p. 61 ; périmètre 2.2.b] ; chronologie de Bâle III [V page BIS « Basel III », F09 § 2] ; CRR3 applicable au 1er janvier 2025 [V règlement (UE) 2024/1623, art. 2, F09 § 2] ; désintermédiation et rôle des fonds de dette [S, F09 § 2 et F05 § 1].

---

### 3.5 Variantes de financement : structure et capacité de remboursement (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Structure de financement de chaque variante : parts des ressources, dettes / fonds propres (A : 0,95 ; B : 0,56), part des cadres (A : 25 % ; B : 20 %) | 0,5 |
| 3.5-02 | Annuités senior (A : 1,85 ; B : 1,62) et service de la dette (A : 2,64 ; B : 2,25) | 0,5 |
| 3.5-03 | Marges, trésorerie cumulée et taux de couverture de chaque variante | 0,5 |
| 3.5-04 | Lecture : condition respectée par les deux variantes ; couverture de la variante A inférieure à 1,10 en 2027 | 0,5 |

**Structure de financement (0,5 pt, M€).**

| | Montage proposé | Variante A (crédit-vendeur) | Variante B (apport du fonds) |
|---|---:|---:|---:|
| Fonds propres | 20,00 (51,28 %) | 20,00 (51,28 %) | 25,00 (64,10 %) |
| dont cadres / SERVANCE Capital | 5,00 / 15,00 | 5,00 / 15,00 | 5,00 / 20,00 |
| Dette senior | 12,00 (30,77 %) | 8,00 (20,51 %) | 7,00 (17,95 %) |
| Dette junior | 7,00 (17,95 %) | 7,00 (17,95 %) | 7,00 (17,95 %) |
| Crédit-vendeur | — | 4,00 (10,26 %) | — |
| **Total des ressources** | **39,00** | **39,00** | **39,00** |
| Dettes de la holding / fonds propres | 0,95 | 0,95 | 0,56 |
| Part des cadres dans le capital | 25,00 % | 25,00 % | 20,00 % |
| Prix encaissé par AURÉVANCE SA à la réalisation | 38,00 | 34,00 | 38,00 |

**Annuités et service de la dette (0,5 pt).**
- Variante A : annuité = 8,0 × 0,05 / (1 − 1,05^−5) = **1,85** (1,8478) ; intérêts junior 0,63 ; intérêts du crédit-vendeur 4,0 × 4 % = 0,16 ; service = **2,64** (2,6378).
- Variante B : annuité = 7,0 × 0,05 / (1 − 1,05^−5) = **1,62** (1,6168) ; intérêts junior 0,63 ; service = **2,25** (2,2468).

**Capacité de remboursement (0,5 pt, M€).**

| | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Dividende reçu | 2,850 | 3,180 | 3,510 | 3,765 | 3,945 |
| **Variante A** – marge | 0,21 | 0,54 | 0,87 | 1,13 | 1,31 |
| trésorerie cumulée | 0,21 | 0,75 | 1,63 | 2,75 | 4,06 |
| taux de couverture | 1,08 | 1,21 | 1,33 | 1,43 | 1,50 |
| **Variante B** – marge | 0,60 | 0,93 | 1,26 | 1,52 | 1,70 |
| trésorerie cumulée | 0,60 | 1,54 | 2,80 | 4,32 | 6,02 |
| taux de couverture | 1,27 | 1,42 | 1,56 | 1,68 | 1,76 |

**Lecture (0,5 pt).**
- Les deux variantes **respectent la condition de réussite** chaque année : en allégeant l'annuité senior des premières années, elles suppriment le déficit de 2027 et de 2028.
- La **variante A ne satisfait pas l'exigence de la banque en 2027** (couverture de 1,08 < 1,10) : il suffit d'un écart défavorable de quelques pour cent sur le premier exercice pour que la holding ne puisse plus payer (une baisse de 5 % de l'EBITDA de 2027 ramènerait la couverture à 1,00 ; calcul facultatif). Elle ne réduit pas l'endettement de la holding (19,0 M€, 0,95 fois les fonds propres) : elle en **déplace l'échéance**, puisque 4,0 M€ de dette amortissable sont remplacés par 4,0 M€ remboursables à la sortie, qui s'ajoutent aux 7,0 M€ de la dette junior.
- La **variante B réduit réellement le levier** (dettes / fonds propres de 0,95 à 0,56 ; 14,0 M€ de dettes au lieu de 19,0) et offre une marge de sécurité confortable (couverture de 1,27 dès 2027), mais elle **dilue les cadres** (25 % → 20 % du capital), qui ne peuvent pas apporter davantage.

**Réponses tolérées** : trésorerie cumulée de la variante B en 2031 égale à 6,01 (somme des marges arrondies) ; dettes / fonds propres exprimé en pourcentage ; crédit-vendeur présenté comme une quasi-dette du vendeur ; calcul de sensibilité non demandé (facultatif).

**Erreurs fréquentes**
- Oublier les intérêts du crédit-vendeur dans le service de la variante A, ou les 4,0 M€ de crédit-vendeur dans les dettes de la holding.
- Conclure que la variante A « réduit l'endettement » parce que la dette senior baisse.
- `JUR-I01` — annuités mal calculées (voir question 3.2).

**Références** : effets d'un financement sur le levier, l'autonomie financière et la capacité de remboursement [V guide p. 82 ; périmètre 7.2.b] ; condition de réussite [V guide p. 70].

---

### 3.6 Effet de levier, théories du choix de financement et recommandation (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Valeur des titres à la sortie 50,00 (7,5 × 6,7 − 0,25) ; valeur des fonds propres de la holding : A 43,06 ; B 49,02 ; sans dette 67,25 | 0,5 |
| 3.6-02 | Multiples de la mise (A 2,15 ; B 1,96 ; sans dette 1,72) et TRI (A 16,58 % ; B 14,41 % ; sans dette 11,51 %) | 1 |
| 3.6-03 | Analyse de l'effet de levier et des risques pour les associés et pour la filiale | 0,5 |
| 3.6-04 | Théorie du compromis appliquée aux deux variantes | 0,5 |
| 3.6-05 | Financement hiérarchique appliqué aux deux variantes | 0,5 |
| 3.6-06 | Recommandation argumentée à M. PRADEVAL | 0,5 |

**Valeurs de sortie (0,5 pt, M€).** VGE à la sortie = 7,5 × 6,7 = 50,25 ; valeur des titres de la filiale = 50,25 − 0,25 = **50,00**.

| | Variante A | Variante B | Rachat sans dette |
|---|---:|---:|---:|
| Valeur des titres de la filiale | 50,00 | 50,00 | 50,00 |
| + Trésorerie cumulée de la holding au 31/12/2031 | 4,06 | 6,02 | 17,25 |
| − Dettes restant dues (junior ; crédit-vendeur) | 11,00 (7,00 + 4,00) | 7,00 | 0,00 |
| **= Valeur des fonds propres à la sortie** | **43,06** | **49,02** | **67,25** |

**Multiples et TRI (1 pt).** Aucun flux n'est versé aux associés avant la sortie : TRI = multiple^(1/5) − 1.

| | Variante A | Variante B | Rachat sans dette |
|---|---:|---:|---:|
| Fonds propres investis | 20,00 | 25,00 | 39,00 |
| Multiple de la mise | 2,15 | 1,96 | 1,72 |
| **TRI** | **16,58 %** | **14,41 %** | **11,51 %** |
| Valeur revenant aux cadres (25 % ; 20 %) | 10,77 | 9,80 | — |

Comme tous les associés souscrivent au même prix unitaire, les cadres et le fonds obtiennent le même TRI dans chaque variante.

**Effet de levier et risques (0,5 pt).**
- Sans dette, l'opération rapporterait 11,51 % par an aux associés : c'est la rentabilité de l'acquisition elle-même, supérieure au coût de la dette (5 % pour la banque, 9 % pour le prêteur junior, 4 % pour le crédit-vendeur). Tant que cette condition est remplie, remplacer des fonds propres par de la dette accroît la rentabilité des associés : 14,41 % avec un rapport dettes / fonds propres de 0,56 (B), 16,58 % avec 0,95 (A). Seule la variante A atteint l'objectif de 15 % de SERVANCE Capital.
- Le levier fonctionne **dans les deux sens**. Si la filiale était cédée à 6,5 fois l'EBITDA au lieu de 7,5 (calcul facultatif), le TRI tomberait à 12,70 % pour A, 11,10 % pour B et 9,20 % sans dette : la baisse est d'autant plus forte que le montage est endetté. Et si les dividendes manquent une année, la holding ne peut plus payer ses échéances : le risque n'est plus seulement une moindre rentabilité, c'est la défaillance.
- **Pour les associés** : les cadres concentrent sur la filiale leur emploi et une part de leur patrimoine ; ils ne reçoivent rien avant 2031 et dépendent d'une sortie au multiple prévu.
- **Pour la filiale** : la distribution de 100 % du résultat pendant cinq ans, alors qu'elle rembourse aussi son propre emprunt, réduit sa capacité à investir ; une holding très endettée est tentée de renoncer à des investissements rentables pour servir sa dette (sous-investissement), au détriment de la marque et des 260 emplois.

**Théorie du compromis (0,5 pt).** Selon la théorie du compromis (Myers, 1977, dans l'attribution retenue par le programme), il existe un endettement optimal qui équilibre les avantages de la dette (ici, l'effet de levier sur la rentabilité des associés ; l'économie d'impôt, qui est au cœur de la théorie, n'est pas prise en compte au niveau de la holding dans ce cas) et ses coûts : risque de défaillance et coûts de difficultés financières (perte de distributeurs inquiets pour leur fournisseur, départs de cadres, investissements différés). Avec une couverture de 1,08 dès 2027, la **variante A** place la holding au bord de la défaillance : les coûts attendus de difficultés financières l'emportent sur le gain de rentabilité. La **variante B**, moins endettée, se rapproche du compromis : elle conserve un levier (0,56) tout en ménageant une marge de sécurité (couverture d'au moins 1,27).

**Financement hiérarchique (0,5 pt).** Selon Myers et Majluf (1984), en présence d'asymétrie d'information, les dirigeants préfèrent l'autofinancement, puis la dette, et en dernier lieu l'émission de nouvelles actions, que des investisseurs moins informés n'acceptent qu'avec une décote. Les cadres, les mieux informés (question 3.1), et la holding, qui n'a pas d'autofinancement à la date 0, préfèrent donc la **dette** : la variante A leur permet de garder 25 % du capital, alors que dans la variante B le fonds, moins informé, apporte les 5,0 M€ manquants et porte sa part à 80 %. La variante A est d'autant plus attractive pour eux que le crédit-vendeur est **peu cher** : 4 %, alors qu'il serait remboursé après la dette junior, rémunérée 9 %. Pour AURÉVANCE SA, accorder ce crédit revient à consentir une baisse de prix déguisée (environ 4,0 × 5 % = 0,20 M€ d'intérêts en moins chaque année par rapport à une rémunération alignée sur le rang junior), et à garder un risque sur une filiale qu'il cède précisément pour se recentrer.

**Recommandation (0,5 pt).** Le cabinet conseille le vendeur ; il recommande de **privilégier la variante B** :
- le groupe encaisse **38,0 M€ à la réalisation** et ne garde aucune créance de 4,0 M€ remboursable après toutes les autres dettes d'une holding de reprise, créance qui perdrait sa valeur précisément si la filiale rencontrait des difficultés ; le produit de la cession reste disponible pour le plan stratégique ;
- le montage est **robuste** (couverture de 1,27 à 1,76, exigence de la banque respectée), ce qui limite le risque d'un échec après la cession, préjudiciable à la marque AURÉVANCE et aux salariés de la filiale ;
- le TRI de SERVANCE Capital (14,41 %) est légèrement inférieur à son objectif de 15 %, mais pour un risque nettement plus faible (dettes / fonds propres de 0,56 au lieu de 0,95) : un objectif de 15 % fixé pour un montage plus endetté n'est pas transposable tel quel (question 3.3). Le fonds pourra chercher à renégocier le prix : le groupe peut alors proposer un **complément de prix conditionné aux résultats** (question 3.1) plutôt qu'une baisse ferme, ce qui partage le gain si les prévisions des cadres sont dépassées ;
- si le groupe acceptait néanmoins de contribuer au financement, ce ne devrait être que pour un montant réduit, avec une rémunération alignée sur le rang de remboursement (au moins celle de la dette junior), et seulement si la couverture de la banque atteint 1,10 chaque année. L'horizon de long terme de la fondation actionnaire justifie de privilégier la pérennité de la filiale cédée plutôt que le prix le plus élevé à tout prix.

**Réponses tolérées** : TRI calculé à partir des multiples arrondis (A 16,54 % ; B 14,41 % ; sans dette 11,46 %) ; valeur de B fondée sur une trésorerie cumulée de 6,01 (fonds propres de 49,01 M€ ; multiple de 1,96 et TRI de 14,41 %, inchangés) ; TRI obtenu par interpolation ; recommandation de la variante A, ou d'une combinaison des deux (apport du fonds plus faible et crédit-vendeur réduit), si elle est justifiée par les intérêts du groupe vendeur, accompagnée de conditions qui ramènent la couverture au-dessus de 1,10 et d'une rémunération du crédit-vendeur cohérente avec son rang ; référence au signal par l'endettement (Ross, 1977) pour la préférence des cadres pour la dette.

**Erreurs fréquentes**
- Calculer le TRI comme une moyenne simple, (multiple − 1) / 5 : 23,06 % pour A au lieu de 16,58 %.
- Oublier de déduire les dettes restant dues à la sortie (dette junior, crédit-vendeur), ou d'ajouter la trésorerie accumulée par la holding ; dans le rachat sans dette, oublier les dividendes conservés (TRI de 5,10 % au lieu de 11,51 %).
- `JUR-T14` et `JUR-M01` — attribuer le financement hiérarchique à d'autres auteurs que Myers et Majluf, inverser l'ordre (actions avant dette), confondre compromis (endettement cible) et financement hiérarchique (pas de cible).
- `JUR-T13` — recommandation non rattachée au point de vue du client (le vendeur) ni aux chiffres du cas.
- Développer l'accord entre associés, la rémunération ou l'intéressement des cadres, ou le régime d'imposition de la holding : hors programme (aspects juridiques et fiscaux des montages, UE 1).

**Références** : effets du levier sur la rentabilité, la structure financière et le risque, création de valeur conditionnelle [V guide p. 70 ; F05 § 1.3] ; théorie du compromis (Myers, 1977) et financement hiérarchique (Myers et Majluf, 1984) [V programme 7.2 ; F10] ; sous-investissement lié à la dette [F10, Myers (1977)] ; Ross (1977) [V programme 4.1 ; F10].
