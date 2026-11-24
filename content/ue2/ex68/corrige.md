# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 68 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F02 coût du capital, F03 évaluation, F07 risques, climat et matières premières, F10 auteurs et théories, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (espérances, variance du marché, covariance, bêta probabilisé et rentabilité exigée de la ligne de flocons ; bêtas réendettés, coûts des fonds propres et CMPC du groupe et de la ligne ; VAN et annuités équivalentes de la conservation de l'ancienne ligne, de la ligne neuve et de la stratégie sur douze ans ; VAN des trois scénarios, espérance, écart-type, coefficient de variation et probabilité d'une VAN négative ; arbre de décision et VAN espérée de la stratégie ; flux actualisés, valeur terminale, VGE, VCP et valeur par action ; valeurs par le multiple de transactions ; barème, liste noire, hors-programme ; valeurs de cession nettes, valeur créée par le remplacement immédiat, VAN du programme, valeur par action avec le programme, écarts au cours et multiples implicites vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un CMPC du groupe erroné à la question 2.1, repris dans les VAN de la question 2.2 et dans la valeur de l'entreprise de la question 2.5, ou un CMPC de la ligne de flocons erroné, repris dans les VAN de la question 2.4).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Bêta probabilisé et rentabilité exigée de la ligne de flocons, CMPC du groupe et de la ligne, choix du taux | `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance ; `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `7.1.b` Évaluer et classer des projets en milieu incertain ; `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers | 4 |
| 2.2 Renouvellement de la ligne de frites : valeur de cession nette, VAN, annuités équivalentes, valeur créée | `7.1.a` Évaluer et classer des projets en milieu certain ; `7.1.c` Déterminer la création de valeur à travers la décision d'investissement ou de désinvestissement | 3,5 |
| 2.3 Création de valeur par l'arrêt d'un actif | `7.1.c` Déterminer la création de valeur à travers la décision d'investissement ou de désinvestissement | 1 |
| 2.4 Ligne de flocons : scénarios, espérance et écart-type de la VAN, arbre de décision | `7.1.b` Évaluer et classer des projets en milieu incertain | 2,5 |
| 2.5 Valeur de l'entreprise par les flux, VCP et valeur par action sans et avec le programme, comparaison au cours | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `3.1.c` Déterminer une valeur terminale à l'infini avec ou sans taux de croissance ; `3.1.d` Distinguer la valeur globale de l'entreprise (VGE) de la valeur des capitaux propres (VCP) ; `7.1.c` Déterminer la création de valeur à travers la décision d'investissement ou de désinvestissement | 3,5 |
| 2.6 Multiple de transactions, multiples implicites, choix de l'inducteur | `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP | 1,5 |
| 2.7 Réponses aux risques physiques de sécheresse et de raréfaction de l'eau | `6.4.a` Sensibiliser aux instruments de couverture des risques physiques et financiers liés au changement climatique et à la raréfaction des ressources naturelles | 1 |
| **Total** | | **17** |

Part du calcul : environ 11,5 points (2.1-01 à 2.1-04, 2.2-01 à 2.2-05, 2.4-01 à 2.4-03, 2.5-01 à 2.5-04, 2.6-01). Part de l'analyse : environ 5,5 points. Répartition par sous-partie du programme : 7.1 ≈ 8 points (7.1.a ≈ 3 avec 2.2-01 à 2.2-04 ; 7.1.b ≈ 3 avec la question 2.4 et le choix du taux de la ligne ; 7.1.c ≈ 2 avec 2.2-05, la question 2.3 et 2.5-04), 5.2 ≈ 3,5 points (question 2.1, dont le CMPC du groupe, qui relève aussi de 3.1.a), 3.1 ≈ 3 points (question 2.5 hors 2.5-04), 3.2 ≈ 1,5 point, 6.4 ≈ 1 point. La question 2.1 fournit les taux des questions 2.2, 2.4 et 2.5 : un candidat qui ne la réussit pas traite les suivantes avec ses propres taux, notés en cohérence. Les questions 2.3, 2.6 et 2.7 se traitent en partie sans calcul et ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 2.1 Bêta probabilisé, rentabilité exigée et CMPC (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | E(Rp) = 0,20 × (− 6) + 0,50 × 10 + 0,30 × 24 = **11,00 %** ; E(Rm) = 0,20 × (− 6) + 0,50 × 9 + 0,30 × 19 = **9,00 %** ; Var(Rm) = 0,20 × 225 + 0,50 × 0 + 0,30 × 100 = **75 %²** ; Cov = 0,20 × (− 17) × (− 15) + 0,50 × (− 1) × 0 + 0,30 × 13 × 10 = **90 %²** ; bêta = 90 / 75 = **1,20** | 1 |
| 2.1-02 | Rentabilité exigée de l'actif = 4,00 % + 1,20 × 5,00 % = **10,00 %** ; espérance 11,00 % : la ligne rapporte **1,00 point de plus** que la rentabilité exigée pour son risque systématique ; un actif plus sensible à la conjoncture (bêta 1,20 > 1) exige une rentabilité supérieure à celle du marché | 0,5 |
| 2.1-03 | Groupe : bêta réendetté = 0,80 × (1 + 0,75 × 20 / 80) = **0,9500** ; ke = 4,00 % + 0,95 × 5,00 % = **8,75 %** ; kd net = 5,00 % × 0,75 = 3,75 % ; CMPC = 80 % × 8,75 % + 20 % × 3,75 % = **7,75 %** | 1 |
| 2.1-04 | Ligne de flocons : bêta réendetté = 1,20 × 1,1875 = **1,4250** ; ke = 4,00 % + 1,4250 × 5,00 % = **11,13 %** ; CMPC = 80 % × 11,13 % + 20 % × 3,75 % = **9,65 %** | 0,5 |
| 2.1-05 | Taux à retenir : **7,75 %** pour la ligne de frites (risque moyen du groupe) et l'entreprise, **9,65 %** pour la ligne de flocons, dont le risque systématique (bêta de l'actif 1,20) dépasse celui du groupe (0,80) ; un taux unique ferait accepter des projets trop risqués et rejeter des projets peu risqués ; un CMPC, et non un coût des fonds propres, parce que les flux sont des flux d'exploitation avant financement. Limites : probabilités et rentabilités estimées par le cabinet sur trois états seulement, hypothèses du MEDAF (investisseurs diversifiés, un seul facteur), formule de Hamada (dette sans risque, structure cible tenue) ; CORVENNE, actionnaire à 55 % peu diversifié, supporte aussi le risque total | 1 |

**Espérances, variance, covariance et bêta (1 pt).** Avec des probabilités, chaque écart est pondéré par la probabilité de son scénario ; il n'y a ni division par n ni division par n − 1 (annexe 2.7).

| État | p | Rp | Rp − E(Rp) | Rm | Rm − E(Rm) | p × (Rm − E)² | p × (Rp − E)(Rm − E) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Ralentissement | 0,20 | − 6 % | − 17 | − 6 % | − 15 | 45,0 | 51,0 |
| Croissance modérée | 0,50 | 10 % | − 1 | 9 % | 0 | 0,0 | 0,0 |
| Forte croissance | 0,30 | 24 % | 13 | 19 % | 10 | 30,0 | 39,0 |
| **Total** | 1 | **11,00 %** | | **9,00 %** | | **75 %²** | **90 %²** |

Bêta probabilisé de l'actif de la ligne = Cov(Rp, Rm) / Var(Rm) = 90 / 75 = **1,20**. Pour information : Var(Rp) = 0,20 × 289 + 0,50 × 1 + 0,30 × 169 = 109 %², soit un écart-type de 10,44 % (marché : 8,66 %) ; coefficient de corrélation 90 / (10,44 × 8,66) = 0,9954. La part systématique de la variance de la ligne (1,20² × 75 = 108 %² sur 109 %²) est presque totale : son risque est celui de la conjoncture, que la diversification n'élimine pas.

**Rentabilité exigée de l'actif (0,5 pt).** Par le MEDAF (Sharpe, 1964), la rentabilité exigée dépend du seul risque systématique : 4,00 % + 1,20 × 5,00 % = **10,00 %**. L'espérance de rentabilité de l'actif, 11,00 %, la dépasse de **1,00 point** : la ligne rémunère plus que son risque, elle crée de la valeur à ce stade de l'analyse. L'écart entre incertitude et exigence est net : la ligne de flocons, plus sensible que le marché à la conjoncture, exige plus que le marché (9,00 %) et nettement plus que l'activité moyenne du groupe (rentabilité exigée de l'actif du secteur : 4,00 % + 0,80 × 5,00 % = 8,00 %).

**CMPC du groupe (1 pt).** La structure cible donne D / CP = 20 / 80 = 25 %. Formule de Hamada avec impôt (annexe 2.7) : bêta des capitaux propres = 0,80 × [1 + (1 − 0,25) × 0,25] = 0,80 × 1,1875 = **0,9500** ; coût des fonds propres = 4,00 % + 0,95 × 5,00 % = **8,75 %** ; coût net de la dette = 5,00 % × (1 − 0,25) = **3,75 %** ; CMPC = 0,80 × 8,75 % + 0,20 × 3,75 % = 7,00 % + 0,75 % = **7,75 %**.

**CMPC de la ligne de flocons (0,5 pt).** Le bêta probabilisé est un bêta de l'actif, puisque les rentabilités de l'annexe 2.3 sont calculées avant tout financement. Financée selon la structure cible, la ligne a un bêta des capitaux propres de 1,20 × 1,1875 = **1,4250**, un coût des fonds propres de 4,00 % + 1,4250 × 5,00 % = **11,13 %** (11,125 %) et un CMPC de 0,80 × 11,13 % + 0,20 × 3,75 % = **9,65 %**.

**Taux à retenir et limites (1 pt).** Le taux d'actualisation d'un projet doit refléter le risque **du projet**, pas celui de l'entreprise qui le porte. La ligne de frites n° 1 renouvelle une activité qui a le risque moyen du groupe : son taux est le CMPC du groupe, **7,75 %**, qui sert aussi à évaluer l'entreprise (question 2.5). La ligne de flocons a un risque systématique supérieur (bêta de l'actif 1,20 contre 0,80) : son taux est son propre CMPC, **9,65 %**. Actualiser les flocons à 7,75 % surestimerait l'espérance de leur VAN (2,06 M€ au lieu de 1,21 M€, question 2.4) : en appliquant un taux unique, le groupe accepterait trop de projets risqués et rejetterait des projets peu risqués qui créent pourtant de la valeur. Le taux est un CMPC, et non le coût des fonds propres, parce que les flux des deux lignes sont des flux d'exploitation, avant intérêts : ils rémunèrent ensemble actionnaires et prêteurs. Limites : les trois états, leurs probabilités et les rentabilités de la ligne sont des estimations du cabinet ; un écart d'un point sur la rentabilité de la ligne dans un état modifie le bêta ; le MEDAF suppose des investisseurs diversifiés, qui ne rémunèrent que le risque systématique, et un seul facteur de risque (Fama et French, 1993, en ajoutent deux) ; la formule de Hamada suppose une dette sans risque et une structure cible stable. Enfin, CORVENNE, qui détient 55 % du capital et dont les producteurs dépendent déjà de la conjoncture agricole, n'est pas un actionnaire diversifié : le risque total du projet compte aussi pour elle.

**Réponses tolérées** : variances et covariance en décimales (0,0075 et 0,0090) ; CMPC de la ligne calculé avec le coût des fonds propres non arrondi (9,65 % aussi) ; rentabilité exigée de l'actif (10,00 %) présentée comme taux des flocons si le candidat justifie l'absence d'effet de la dette (accordé à moitié sur 2.1-04 : la structure de financement du groupe s'applique à tous ses investissements, annexe 2.4).

**Erreurs fréquentes**
- Poids égaux au lieu des probabilités : bêta 1,19, ou division par n − 1.
- Rentabilité exigée = 4,00 % + 1,20 × 9,00 % = 14,80 % : la prime de risque est E(Rm) − rf = 5,00 %, pas E(Rm).
- Réendetter avec la structure actuelle du marché (31,30 / 88,16) au lieu de la structure cible ; utiliser D / (D + CP) dans la formule de Hamada, qui demande D / CP (`JUR-E02`).
- Actualiser les flux d'exploitation au coût des fonds propres (8,75 % ou 11,13 %).
- `JUR-T13` — limites du MEDAF récitées sans lien avec CORVENNE et les trois états de l'économie.

**Références** : F01 § 5 (milieu probabilisable, bêta probabilisé du sujet 2021) [V programme 7.1.b ; guide p. 81 ; S sujet 2021] ; F02 § 2 (MEDAF et ses limites), § 3 (Hamada avec impôt), § 5 (CMPC) [V programme 5.2.c et 3.1.a ; guide p. 64 et 75] ; F10 Sharpe (1964) [V contexte ; MEDAF au programme 5.2], Fama et French (1993) [V programme 5.2].

---

### 2.2 Renouvellement de la ligne de frites n° 1 (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Cession au 31/12/2026 : plus-value 2,40 − 1,60 = 0,80, impôt 0,20, démontage net 0,40 × 0,75 = 0,30, **valeur de cession nette 1,90** ; fin 2030 : 0,60 − 0,15 − 0,30 = **0,15** ; décaissement net du remplacement immédiat 17,00 − 1,90 = **15,10** | 0,5 |
| 2.2-02 | Conservation : − 1,90 (cession immédiate à laquelle on renonce) puis − 5,15 ; − 5,45 ; − 5,75 ; − 6,05 + 0,15 = − 5,90 ; **VAN à 7,75 % = − 20,35** | 1 |
| 2.2-03 | Ligne neuve : − 17,00 puis − 4,20 × 0,75 + 2,125 × 0,25 = **− 2,62** par an, − 2,62 + 0,75 = − 1,87 en année 8 ; **VAN = − 31,79** | 0,5 |
| 2.2-04 | Annuités équivalentes : conservation − 20,35 / 3,3306 = **− 6,11** ; ligne neuve − 31,79 / 5,8016 = **− 5,48** ; la ligne neuve coûte 0,63 M€ de moins par an : **remplacer maintenant** ; la VAN la moins négative (conservation) porte sur 4 ans contre 8 : les comparer directement ferait conserver à tort | 1 |
| 2.2-05 | Valeur créée par le remplacement immédiat = 0,63 × 3,3306 = **2,10 M€** | 0,5 |

**Valeur de cession nette et décaissement net (0,5 pt).** Au 31 décembre 2026, l'ancienne ligne se revend 2,40 M€ pour une valeur nette comptable de 1,60 M€ : plus-value 0,80, impôt 0,80 × 25 % = 0,20 ; le démontage (0,40) réduit l'impôt de 0,10 et coûte 0,30 net. Valeur de cession nette = 2,40 − 0,20 − 0,30 = **1,90 M€**. À la fin de 2030, la ligne est entièrement amortie : 0,60 − 0,60 × 25 % − 0,30 = **0,15 M€**. Le remplacement immédiat décaisse 17,00 − 1,90 = **15,10 M€** à la date 0.

**Flux et VAN de la conservation pendant quatre ans (1 pt).** Conserver l'ancienne ligne, c'est renoncer à 1,90 M€ aujourd'hui : ce coût d'opportunité est le flux de la date 0. Chaque année, flux = − charges × (1 − 25 %) + amortissement × 25 % (économie d'impôt de 0,40 × 25 % = 0,10).

| Année | 0 | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|---:|
| Cession immédiate à laquelle on renonce | − 1,90 | | | | |
| Charges après impôt | | − 5,25 | − 5,55 | − 5,85 | − 6,15 |
| Économie d'impôt sur l'amortissement | | 0,10 | 0,10 | 0,10 | 0,10 |
| Cession nette en fin de vie | | | | | 0,15 |
| **Flux** | **− 1,90** | **− 5,15** | **− 5,45** | **− 5,75** | **− 5,90** |
| Flux actualisés à 7,75 % | − 1,90 | − 4,78 | − 4,69 | − 4,60 | − 4,38 |

VAN de la conservation = **− 20,35 M€**.

**Flux et VAN de la ligne neuve (0,5 pt).** Amortissement 17,00 / 8 = 2,125 M€ par an ; flux annuel = − 4,20 × 0,75 + 2,125 × 0,25 = − 3,15 + 0,53 = **− 2,62 M€** (− 2,61875). En année 8 s'ajoute la cession nette : 1,40 − 1,40 × 25 % − 0,30 = 0,75, soit un flux de − 1,87. VAN = − 17,00 − 2,62 × 5,8016 + 0,75 × 1,0775^−8 = − 17,00 − 15,20 + 0,41 = **− 31,79 M€**.

**Annuités équivalentes et conclusion (1 pt).** Facteurs d'annuité à 7,75 % : 3,3306 sur 4 ans, 5,8016 sur 8 ans.

| Stratégie | Durée | VAN | Annuité équivalente |
|---|---:|---:|---:|
| Conserver l'ancienne ligne | 4 ans | − 20,35 | − 20,35 / 3,3306 = **− 6,11** |
| Ligne neuve | 8 ans | − 31,79 | − 31,79 / 5,8016 = **− 5,48** |

Les deux lignes produisent les mêmes frites : on compare des coûts. La ligne neuve coûte l'équivalent de 5,48 M€ par an, contre 6,11 M€ pour la conservation de l'ancienne : **il faut remplacer la ligne maintenant**. La VAN de la conservation (− 20,35) est moins négative que celle de la ligne neuve (− 31,79), mais elle ne couvre que quatre années de production, contre huit : comparer les deux VAN reviendrait à préférer la stratégie qui produit le moins longtemps. L'annuité équivalente ramène chaque stratégie à un coût par année de production, sous l'hypothèse que chaque ligne est remplacée à l'identique à la fin de sa vie (annexe 2.7).

**Valeur créée par le remplacement immédiat (0,5 pt).** Dans les deux stratégies, la production est assurée à partir de 2031 par des lignes neuves au même coût annuel équivalent. Seules diffèrent les quatre années 2027 à 2030 : le remplacement immédiat économise 6,11 − 5,48 = 0,63 M€ par an pendant quatre ans, soit 0,63 × 3,3306 = **2,10 M€** à la date 0. Cette valeur est reprise dans la VAN du programme (question 2.5).

**Réponses tolérées** : flux actualisés arrondis un à un pour la ligne neuve (VAN − 31,77 ; annuité − 5,48) ; comparaison des stratégies « remplacer maintenant » (8 ans, annuité − 5,48) et « conserver quatre ans puis remplacer » (12 ans : VAN − 43,93, annuité − 5,75), qui conduit à la même conclusion ; cession immédiate portée en + 1,90 dans les flux de la ligne neuve au lieu de − 1,90 dans ceux de la conservation, à condition que la comparaison soit faite sur un horizon commun ou par une démarche cohérente ; valeur créée calculée par la perpétuité : − 5,48 / 7,75 % − [− 20,35 − 5,48 / 7,75 % × 1,0775^−4] = 2,10.

**Erreurs fréquentes**
- Comparer les deux VAN sans tenir compte de la différence de durée, et conserver l'ancienne ligne.
- Oublier le coût d'opportunité de la cession immédiate : VAN de la conservation − 18,45 et annuité − 5,54, qui réduit l'écart à 0,06 M€ par an.
- Oublier l'impôt sur la plus-value ou le démontage (valeur de cession 2,40 ou 2,20) ; ajouter l'économie d'impôt sur l'amortissement de 2,125 sans la multiplier par 25 %.
- Calculer les flux de la ligne neuve à partir des économies seules sur quatre ans, en oubliant les années 5 à 8.
- `JUR-T04` — VAN et annuités sont des acquis du DCG ; `JUR-T07` — les flux sont présentés en tableau.

**Références** : F01 § 4.2 (VAN, annuité équivalente pour des durées différentes) et § 4.1 (construction des flux, valeur résiduelle nette d'impôt) [V programme 7.1.a ; guide p. 80-81] ; F01 § 5 (désinvestissement : valeur de cession nette d'impôt, flux évités) [V guide p. 81].

---

### 2.3 Créer de la valeur en arrêtant un actif (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Mécanismes, avec les chiffres du cas : **flux évités** (charges de 7,00 à 8,20 M€ par an, 5,25 à 6,15 après impôt, en hausse avec l'usure), **valeur de cession** encaissée tôt (1,90 net maintenant contre 0,15 dans quatre ans), **coûts de sortie** (démontage de 0,30 net, avancé de quatre ans) ; arrêter crée de la valeur si la valeur actuelle des flux évités et de la cession dépasse celle des flux perdus : c'est le sens de la VAN de 2,10 M€ | 0,5 |
| 2.3-02 | Ce qui changerait la conclusion : un coût de la ligne neuve supérieur d'environ **4,46 M€** (0,63 × 5,8016 / 0,8187, le surcoût étant amorti et réduisant l'impôt) annulerait l'avantage ; des économies plus faibles que garanti ; une valeur de revente actuelle plus basse ; un taux plus élevé ; une technologie meilleure attendue à court terme ; il faudrait aussi tester un remplacement en 2027, 2028 ou 2029, avec les valeurs de revente de chaque date | 0,5 |

**Mécanismes (0,5 pt).** Arrêter un actif qui produit encore crée de la valeur quand ce qu'on gagne à l'arrêter vaut plus que ce qu'on perd. En l'espèce, l'arrêt de la ligne n° 1 évite des charges élevées et croissantes (5,25 à 6,15 M€ par an après impôt, contre 3,15 M€ pour la ligne neuve), et il permet d'encaisser aujourd'hui une valeur de cession nette de 1,90 M€, qui ne vaudra plus que 0,15 M€ dans quatre ans. Il a un coût de sortie, le démontage (0,30 M€ net), payé quatre ans plus tôt, et il impose de réinvestir 17,00 M€. La VAN de la décision (2,10 M€) mesure la valeur créée pour les actionnaires et les prêteurs : un actif ne vaut pas sa valeur comptable (1,60 M€), il vaut le plus élevé de sa valeur de cession et de la valeur actuelle des flux qu'il procure encore. L'eau rend le calcul plus favorable à l'arrêt : chaque restriction ou hausse du prix de l'eau alourdit surtout les charges de l'ancienne ligne.

**Données qui changeraient la conclusion (0,5 pt).** L'avantage de la ligne neuve est de 0,63 M€ par an : il disparaîtrait si son coût dépassait d'environ **4,46 M€** les 17,00 M€ prévus, soit **21,46 M€** : l'écart de 0,63 M€ par an vaut 0,63 × 5,8016 = 3,66 M€ de VAN sur huit ans, mais un surcoût X n'enlève que X × (1 − 25 % / 8 × 5,8016) = 0,8187 X à la VAN, puisqu'il est amorti et réduit l'impôt : 0,63 × 5,8016 / 0,8187 = 4,46 (4,47 si l'on part de la VAN arrondie à 3,66, écart toléré) ; si ses économies étaient plus faibles que garanti (une hausse de ses charges de 0,63 / 0,75 = 0,84 M€ par an suffirait), si la valeur de revente actuelle de l'ancienne ligne tombait, ou si le taux d'actualisation montait. Deux limites de la méthode : l'annuité équivalente suppose un renouvellement à l'identique, alors qu'une technologie plus économe pourrait apparaître ; et l'énoncé ne compare que deux dates, alors qu'un remplacement en 2027, 2028 ou 2029 pourrait être meilleur, à condition de connaître les valeurs de revente de ces années.

**Réponses tolérées** : seuil exprimé en hausse relative de l'investissement (environ 26 %) ; seuil de 3,66 M€ si le candidat néglige, en le disant, l'économie d'impôt sur l'amortissement du surcoût ; toute donnée sensible pertinente justifiée par le cas.

**Erreurs fréquentes**
- Raisonner sur la valeur nette comptable (1,60) au lieu de la valeur de cession nette (1,90) : le passé comptable n'est pas un flux.
- Exposé général sur le désinvestissement, sans les charges, la cession ni le démontage de la ligne n° 1 (`JUR-T13`).

**Références** : F01 § 5 (désinvestissement : valeur de cession nette d'impôt, flux évités, coûts de sortie) [V programme 7.1.c ; guide p. 81].

---

### 2.4 Ligne de flocons : scénarios et arbre de décision (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | VAN à 9,65 % = − 13,00 + 3,00 × 1,7437 + F × 3,1940 × 0,8317 : faible **− 4,58** ; centrale **1,26** ; forte **4,98** | 0,5 |
| 2.4-02 | E(VAN) = 0,20 × (− 4,58) + 0,50 × 1,26 + 0,30 × 4,98 = **1,21** ; écart-type **3,31** (variance 10,97) ; probabilité d'une VAN négative **20 %** (scénario faible) | 0,5 |
| 2.4-03 | Arbre, valeurs en fin d'année 2 : demande forte, étendre − 4,80 + 7,20 × 3,1940 = **18,20** contre maintenir 15,33 : **étendre** ; demande centrale, étendre − 4,80 + 4,80 × 3,1940 = **10,53** contre maintenir **10,86** : **maintenir** ; demande faible 3,83 ; valeur espérée en fin d'année 2 : **11,66** ; VAN espérée de la stratégie = − 7,77 + 11,66 × 0,8317 = **1,93** | 1 |
| 2.4-04 | La décision prise au vu de la demande ajoute **0,72 M€** (1,93 − 1,21) : l'extension n'est payée que si elle rapporte ; risque : la perte du scénario faible (− 4,58, probabilité 20 %) reste entière, l'écart-type passe à 4,19 parce que le gain est concentré sur la demande forte ; la ligne est acceptable, l'extension est décidée à deux ans | 0,5 |

**VAN par scénario (0,5 pt).** Au CMPC de la ligne, 9,65 % (question 2.1) : facteur d'annuité sur 2 ans 1,7437 ; facteur d'annuité sur 4 ans 3,1940 ; facteur d'actualisation à 2 ans 0,8317. Les années 1 et 2 sont communes : − 13,00 + 3,00 × 1,7437 = **− 7,77 M€**.

| Scénario | p | Flux années 3 à 6 | Valeur en fin d'année 2 | VAN |
|---|---:|---:|---:|---:|
| Faible | 20 % | 1,20 | 1,20 × 3,1940 = 3,83 | − 7,77 + 3,83 × 0,8317 = **− 4,58** |
| Centrale | 50 % | 3,40 | 10,86 | **1,26** |
| Forte | 30 % | 4,80 | 15,33 | **4,98** |

**Espérance, écart-type, probabilité d'une VAN négative (0,5 pt).** E(VAN) = 0,20 × (− 4,58) + 0,50 × 1,26 + 0,30 × 4,98 = **1,21 M€** ; variance = 0,20 × (− 5,79)² + 0,50 × 0,05² + 0,30 × 3,77² = **10,97** ; écart-type **3,31 M€** (coefficient de variation 2,74). La VAN est négative dans le seul scénario faible : probabilité **20 %**. La ligne crée de la valeur en espérance, mais le risque est élevé au regard de cette espérance.

**Arbre de décision (1 pt).**

```
Date 0 : investir 13,00 → années 1 et 2 : 3,00 par an (certain)
Fin de l'année 2 : la demande est connue
├── Forte (30 %)    ── étendre (− 4,80 ; 7,20 par an)  : 18,20  ← retenu
│                   └─ maintenir (4,80 par an)         : 15,33
├── Centrale (50 %) ── étendre (− 4,80 ; 4,80 par an)  : 10,53
│                   └─ maintenir (3,40 par an)         : 10,86  ← retenu
└── Faible (20 %)   ── maintenir (1,20 par an)         :  3,83
```

On résout l'arbre de droite à gauche. En fin d'année 2, on retient dans chaque état la branche de plus grande valeur : étendre si la demande est forte (18,20 > 15,33), maintenir si elle est centrale (10,86 > 10,53 : le supplément de 1,40 M€ par an ne paie pas les 4,80 M€ du second sécheur), maintenir si elle est faible. Valeur espérée en fin d'année 2 : 0,30 × 18,20 + 0,50 × 10,86 + 0,20 × 3,83 = **11,66 M€** ; VAN espérée de la stratégie = − 7,77 + 11,66 × 0,8317 = **1,93 M€**.

**Commentaire (0,5 pt).** Décider l'extension au vu de la demande, plutôt que de s'engager aujourd'hui sur une ligne fixe, ajoute **0,72 M€** de VAN espérée (1,93 − 1,21) : le second sécheur n'est acheté que dans l'état où il rapporte (demande forte), soit 0,30 × (18,20 − 15,33) × 0,8317. Cette valeur vient de l'information obtenue en deux ans ; elle serait nulle si la décision devait être prise dès aujourd'hui. Le risque ne disparaît pas : la perte du scénario faible (− 4,58 M€, probabilité 20 %) reste entière, et l'écart-type de la stratégie monte à 4,19 M€ (VAN de 7,37 si la demande est forte) parce que le gain est concentré dans le meilleur état ; le coefficient de variation baisse toutefois (environ 2,2 contre 2,74). Recommandation : la ligne crée de la valeur à son taux (VAN espérée positive, rentabilité espérée supérieure à la rentabilité exigée) ; elle est acceptable si le groupe peut supporter la perte du scénario faible, et l'extension doit rester une décision de 2028, préparée dès maintenant (place, raccordements), à prendre au vu des commandes des industriels.

**Réponses tolérées** : VAN de la stratégie calculée comme espérance des VAN par état (0,20 × (− 4,58) + 0,50 × 1,26 + 0,30 × 7,37 = 1,93) ; écarts d'arrondi de 0,01 sur les valeurs de l'arbre ; écart-type de la stratégie non calculé si le commentaire du risque est juste.

**Erreurs fréquentes**
- Actualiser au CMPC du groupe (7,75 %) : espérance 2,06 au lieu de 1,21.
- Retenir l'extension dans l'état central, ou pondérer les deux branches d'un même état par des probabilités.
- Oublier l'actualisation des valeurs de la fin de l'année 2, ou actualiser le coût de l'extension sur quatre ans.
- Diviser la variance par 2 (n − 1) ou par 3 au lieu de pondérer par les probabilités.
- Conclure à un risque nul parce que l'espérance est positive.

**Références** : F01 § 5 (espérance et écart-type de la VAN, arbre de décision simple) [V programme 7.1.b ; guide p. 81] ; F10 Markowitz (1952) pour le couple rendement-risque [V programme 5.3].

---

### 2.5 Valeur de l'entreprise et valeur par action (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Flux actualisés à 7,75 % : 6,50 ; 6,37 ; 6,08 ; 5,71 ; 5,51, somme **30,17** | 0,5 |
| 2.5-02 | Valeur terminale fin 2031 = 8,00 × 1,015 / (7,75 % − 1,5 %) = **129,92** ; actualisée **89,45** ; VGE = 30,17 + 89,45 = **119,62** ; poids de la valeur terminale **74,78 %** | 1 |
| 2.5-03 | VCP = 119,62 − 31,30 = **88,32 M€** ; valeur par action = 88,32 / 5,8 = **15,23 €** | 0,5 |
| 2.5-04 | VAN du programme = 2,10 + 1,93 = **4,03** ; VCP avec le programme **92,35** ; valeur par action **15,92 €** (+ 0,69 €) | 0,5 |
| 2.5-05 | Cours 15,20 € ≈ valeur sans le programme (+ 0,03 €) : le marché valorise le groupe tel qu'il est, sans le programme non encore approuvé ; le programme vaudrait 0,69 € par action, soit 4,74 % au-dessus du cours ; sensibilité forte au CMPC et à la croissance (valeur terminale = 75 % de la VGE) : 13,69 € à 8,25 %, 17,03 € à 7,25 % ; recommandation (approuver et expliquer le programme) | 1 |

**Flux actualisés (0,5 pt).** Au CMPC du groupe, 7,75 % (question 2.1) :

| Année | 2027 | 2028 | 2029 | 2030 | 2031 |
|---|---:|---:|---:|---:|---:|
| Flux de trésorerie disponible | 7,00 | 7,40 | 7,60 | 7,70 | 8,00 |
| Facteur d'actualisation | 0,9281 | 0,8613 | 0,7994 | 0,7419 | 0,6885 |
| Flux actualisé | 6,50 | 6,37 | 6,08 | 5,71 | 5,51 |

Somme des flux actualisés : **30,17 M€**.

**Valeur terminale, VGE et poids de la valeur terminale (1 pt).** Modèle de croissance constante (Gordon et Shapiro, 1956) appliqué aux flux disponibles : valeur terminale à la fin de 2031 = 8,00 × 1,015 / (0,0775 − 0,015) = 8,12 / 0,0625 = **129,92 M€**, actualisée sur cinq ans : 129,92 × 0,6885 = **89,45 M€**. VGE = 30,17 + 89,45 = **119,62 M€**. La valeur terminale représente 89,45 / 119,62 = **74,78 %** de la valeur de l'entreprise.

**VCP et valeur par action sans le programme (0,5 pt).** Les flux disponibles rémunèrent actionnaires et prêteurs : la valeur des capitaux propres est la VGE diminuée de la dette financière nette, 119,62 − 31,30 = **88,32 M€**, soit 88,32 / 5,8 = **15,23 €** par action.

**Avec la VAN du programme (0,5 pt).** VAN du programme = valeur créée par le remplacement immédiat de la ligne n° 1 (2,10) + VAN espérée de la stratégie de la ligne de flocons (1,93) = **4,03 M€**. VCP = 88,32 + 4,03 = **92,35 M€** ; valeur par action **15,92 €**, soit 0,69 € de plus. Le mode de financement du programme ne change pas cette valeur : les deux VAN sont calculées au CMPC, qui intègre déjà le coût de la dette et des fonds propres (Modigliani et Miller, 1958, pour le principe de séparation entre décision d'investissement et décision de financement).

**Comparaison au cours (1 pt).** Au cours de 15,20 €, le marché valorise SOLANÈRE presque exactement à sa valeur sans le programme (15,23 €, écart de 0,03 €) : il semble intégrer les flux du groupe tel qu'il est, sécheresses comprises, mais pas encore le programme, qui n'est ni approuvé ni détaillé publiquement. Si le conseil l'approuve et le présente avec ses chiffres, la valeur par action passerait à 15,92 €, soit **4,74 %** au-dessus du cours : le programme crée de la valeur. Ces valeurs restent fragiles : la valeur terminale pèse 75 % de la VGE, et une variation d'un demi-point du CMPC suffit à les déplacer plus que le programme lui-même (13,69 € à 8,25 %, 17,03 € à 7,25 %) ; une croissance à l'infini de 1,0 % au lieu de 1,5 %, plausible si les sécheresses se répètent, ramènerait la valeur sans programme à 14,02 €. Recommandation : le programme mérite d'être approuvé ; sa communication au marché (VAN, hypothèses sur l'eau) peut réduire l'écart entre cours et valeur, en supposant que le marché intègre l'information publique (efficience semi-forte, Fama, 1970).

**Réponses tolérées** : valeur par action avec le programme calculée par addition (15,23 + 4,03 / 5,8 = 15,92) ; flux actualisés non arrondis (somme 30,17 aussi) ; sensibilités non chiffrées si leur sens est juste (elles ne sont pas exigées).

**Erreurs fréquentes**
- Actualiser la valeur terminale sur six ans, ou oublier de l'actualiser.
- Appliquer la croissance au flux de 2031 sans le facteur (1 + g), ou diviser par le CMPC seul.
- Oublier de déduire la dette financière nette, ou la déduire deux fois en ajoutant la VAN du programme (`JUR-E01`).
- Ajouter au VCP les 30,00 M€ investis au lieu de la VAN du programme.
- `JUR-T13` — comparer au cours sans dire ce que le marché sait et ne sait pas du programme.

**Références** : F03 § 2.1 à 2.2 (flux disponibles, valeur terminale, VGE et VCP) [V programme 3.1.a, 3.1.c et 3.1.d ; guide p. 64] ; F02 § 6 et F10 Gordon et Shapiro (1956) [V programme 3.1] ; F10 Modigliani et Miller (1958) [V programme 4.1], Fama (1970) [V programme 5.1].

---

### 2.6 Multiple de transactions et choix de l'inducteur (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | VGE = 7,80 × 17,40 = **135,72** ; VCP = 135,72 − 31,30 = **104,42** ; **18,00 €** par action ; multiples implicites : cours (88,16 + 31,30) / 17,40 = **6,87** ; flux 119,62 / 17,40 = **6,87** | 0,5 |
| 2.6-02 | Écart (+ 16,10 M€ de VCP, VGE supérieure de 13,46 %) : les transactions paient une **prime de contrôle** et des synergies, que n'obtient pas un actionnaire minoritaire, et CORVENNE (55 %) rend une prise de contrôle peu probable ; échantillon et dates différents ; l'**EBITDA 2026** est abaissé par la sécheresse et ne mesure pas les investissements que l'activité exige (renouvellement des lignes) ; l'évaluation par les flux reste la référence, le multiple sert de recoupement | 1 |

**Calculs (0,5 pt).** Le multiple de transactions s'applique à un inducteur de VGE, l'EBITDA : VGE = 7,80 × 17,40 = **135,72 M€** ; VCP = 135,72 − 31,30 = **104,42 M€** ; valeur par action = 104,42 / 5,8 = **18,00 €**. Le cours donne une capitalisation de 15,20 × 5,8 = 88,16 M€ et une valeur de l'entreprise de 88,16 + 31,30 = 119,46 M€, soit **6,87** fois l'EBITDA 2026 ; l'évaluation par les flux donne 119,62 / 17,40 = **6,87** également.

**Explication de l'écart et choix de l'inducteur (1 pt).** Le multiple de transactions conduit à une VCP supérieure de 16,10 M€ à celle des flux. Il est observé lors de prises de contrôle (51 % à 100 % du capital) : l'acquéreur paie une prime de contrôle, qui rémunère les synergies attendues et le pouvoir de décider de la stratégie et des dividendes. Le cours de bourse est un prix de minoritaire : il n'inclut pas cette prime, et l'actionnaire de contrôle, CORVENNE, avec 55 % du capital et cinq administrateurs sur neuf, rend une offre sur SOLANÈRE peu probable. Les transformateurs cédés en 2025 et 2026 n'ont pas forcément la même exposition à l'eau, la même croissance ni la même dépendance à un fournisseur associé. L'EBITDA est un inducteur adapté à une activité industrielle, puisqu'il ne dépend ni de la structure financière ni des politiques d'amortissement ; mais celui de 2026 est abaissé par la sécheresse, et il ne tient pas compte des investissements lourds qu'exige le renouvellement des lignes, que les flux disponibles intègrent. Le multiple sert donc de recoupement, et la fourchette de 15,23 € (flux, minoritaire) à 18,00 € (transactions, contrôle) se situe au-dessus du cours, qui en touche la borne basse : le marché ne paie aucune prime de contrôle sur une société que CORVENNE contrôle.

**Réponses tolérées** : écart exprimé en euros par action (2,77 €) ou en multiple (7,80 contre 6,87, soit + 13,5 %) ; mention d'un EBITDA « normal » plus élevé qui accroîtrait encore la valeur par le multiple ; recours à un inducteur complémentaire (résultat d'exploitation) justifié.

**Erreurs fréquentes**
- Appliquer le multiple de VGE et oublier de déduire la dette financière nette.
- Présenter la moyenne des méthodes comme « la » valeur sans discuter la prime de contrôle (`JUR-E03`).
- Calculer le multiple implicite du cours avec la seule capitalisation (88,16 / 17,40 = 5,07).

**Références** : F03 § 3 (multiples, inducteurs de VGE et de VCP, décotes et prime de contrôle) et § 8 (réconciliation des méthodes) [V programme 3.2.a ; guide p. 65].

---

### 2.7 Réponses aux risques physiques de sécheresse et de raréfaction de l'eau (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Pour chaque réponse, ce qu'elle couvre et ses limites : **ligne économe** (réduit l'exposition de l'usine à la source, à un risque chronique, mais pas la baisse des rendements des producteurs) ; **clauses de rendement** (partagent le risque de volume et sécurisent la récolte, mais le complément de prix pèse sur la marge les mauvaises années, et le risque reste chez l'actionnaire de contrôle et ses producteurs) ; **diversification des bassins** (réduit la corrélation des approvisionnements, avec un surcoût permanent) ; **stockage de l'eau** (adaptation chez les producteurs, mais soumise aux restrictions, incertaine et créant un risque de crédit sur l'avance) ; **assurance des récoltes** (protège la trésorerie des producteurs, pas l'approvisionnement de SOLANÈRE) | 0,5 |
| 2.7-02 | Politique d'ensemble : réduire d'abord l'exposition (ligne économe, diversification), puis partager ou transférer le reste (clauses, assurance des producteurs), en gardant un risque résiduel suivi ; aucune réponse ne couvre seule un été très sec ; relier ces choix à la performance durable (eau prélevée) et au coût du capital, et ne pas reporter tout le risque sur les producteurs de CORVENNE | 0,5 |

**Ce que couvre chaque réponse (0,5 pt).** Les sécheresses sont un risque physique à la fois aigu (un été sec, des restrictions de prélèvement pendant plusieurs semaines) et chronique (des étés secs plus fréquents, un prix de l'eau en hausse). Elles touchent SOLANÈRE par trois voies : les volumes et les prix des pommes de terre, l'eau de l'usine, l'énergie.

| Réponse | Ce qu'elle couvre | Limites |
|---|---|---|
| Ligne de frites économe | Réduit à la source l'eau prélevée (− 45 % sur une ligne qui en prend un tiers) et le gaz ; rend l'usine moins vulnérable aux restrictions et au prix de l'eau ; crée de la valeur (2,10 M€) | Ne protège pas les rendements des producteurs ; ne couvre qu'une ligne |
| Clauses de rendement | Partagent le risque de volume : les producteurs ne sont pas pénalisés, SOLANÈRE garde toute la récolte sous contrat | Le complément de prix augmente le coût des achats les mauvaises années, quand la marge est déjà basse ; le risque reste concentré sur l'actionnaire de contrôle et ses membres |
| Diversification des bassins | Réduit la corrélation des approvisionnements : un été sec dans le Santerre n'est pas forcément sec dans l'autre bassin | Surcoût de transport et de stockage chaque année ; bassin non à l'abri d'une sécheresse étendue ; moins de volume pour CORVENNE |
| Stockage de l'eau | Adaptation chez les producteurs, qui sécurise l'irrigation | Usage soumis aux restrictions ; acceptation incertaine ; l'avance de SOLANÈRE expose le groupe au risque de non-remboursement |
| Assurance des récoltes | Protège la trésorerie des producteurs et donc leur capacité à continuer | SOLANÈRE n'est pas indemnisée et reste sans pommes de terre ; franchise ; l'assurance ne crée pas de tubercules |

**Place dans la politique de gestion des risques (0,5 pt).** Une politique cohérente commence par réduire l'exposition (ligne économe, puis les autres lignes ; diversification d'une partie des volumes), puis partage ou transfère le risque qui reste (clauses de rendement, assurance des producteurs), et accepte en connaissance de cause un risque résiduel, qu'il faut financer (trésorerie de précaution, lignes de crédit). Aucune réponse ne protège seule le groupe d'un été très sec et prolongé. Ces choix relèvent aussi de la performance durable : réduire l'eau prélevée améliore les indicateurs publiés et l'acceptabilité locale de l'usine, et un risque physique mieux maîtrisé peut réduire la prime de risque exigée par les investisseurs. Enfin, le conseil doit veiller à ne pas reporter l'essentiel du risque sur les producteurs de CORVENNE, actionnaire de contrôle : les intérêts des minoritaires et ceux de la coopérative ne coïncident pas toujours, dans le prolongement de la théorie de l'agence (Jensen et Meckling, 1976).

**Réponses tolérées** : classement des réponses en prévention, réduction, partage et transfert ; toute réponse supplémentaire (assurance de la perte d'exploitation de SOLANÈRE, stock de sécurité) argumentée sans chiffrage.

**Erreurs fréquentes**
- Présenter l'assurance des producteurs comme une couverture de SOLANÈRE.
- Confondre risque physique et risque de transition, ou ignorer le caractère chronique des sécheresses.
- Liste des réponses sans limites ni lien avec les chiffres du dossier (`JUR-T13`, `JUR-T05`).

**Références** : F07 § 5 (risques climatiques physiques et de transition, assurance, articulation avec la performance durable) [V programme 6.4.a ; guide p. 80] ; F10 Jensen et Meckling (1976) [V programme 2.1].
