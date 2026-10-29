# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 17 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et critères d'investissement, F02 coût du capital, F07 risques climatiques et matières premières, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (bêtas, MEDAF, CMPC, VAN, TRI, indices de profitabilité, annuités équivalentes, VAN et TRI globaux, option climatique, barème, liste noire, hors-programme ; seuils de volume et de prix vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple des VAN calculées à un CMPC erroné à la question 2.1, ou un choix de projet à la question 2.3 cohérent avec des VAN fausses).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Rentabilité exigée et CMPC du projet | `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance ; `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `7.1.a` Évaluer et classer des projets en milieu certain (taux d'actualisation d'un projet) | 5 |
| 2.2 VAN, TRI, indice de profitabilité et conflit de classement | `7.1.a` Évaluer et classer des projets en milieu certain | 4 |
| 2.3 Durées inégales : annuité équivalente, VAN et TRI globaux, recommandation | `7.1.a` | 3 |
| 2.4 Seuils de volume et de prix du projet A | `7.1.b` Évaluer et classer des projets en milieu incertain | 2 |
| 2.5 Risque de sécheresse, option climatique, assurance et prix de l'électricité | `6.4.a` Sensibiliser aux instruments de couverture des risques physiques et financiers liés au changement climatique et à la raréfaction des ressources naturelles | 3 |
| **Total** | | **17** |

Part du calcul : environ 10,5 points (2.1-03 à 2.1-06, 2.2-01 à 2.2-05, 2.3-01 à 2.3-03, 2.4-01, 2.4-02, 2.5-02, 2.5-03). Part de l'analyse : environ 6,5 points (2.1-01, 2.1-02, 2.1-07, 2.2-06, 2.3-04, 2.4-03, 2.5-01, 2.5-04). Les commentaires et la recommandation valent plus du tiers du dossier : ils ne doivent pas être sacrifiés faute de temps (`JUR-T15`).

---

### 2.1 Rentabilité exigée et CMPC du projet (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Relation entre incertitude et rentabilité exigée ; critique argumentée des deux propositions (4,60 % et 4 %) | 0,75 |
| 2.1-02 | Risque spécifique et risque systématique ; seul le second est rémunéré ; choix d'Hydrévia plutôt qu'AMBRELIS justifié | 1 |
| 2.1-03 | Bêta désendetté d'Hydrévia : 0,5200 | 0,5 |
| 2.1-04 | Bêta des fonds propres du projet : 0,9100 | 0,5 |
| 2.1-05 | Coût des fonds propres du projet (MEDAF) : 8,55 % | 0,5 |
| 2.1-06 | Coût net de la dette 3,45 % (0,25) ; CMPC du projet 6,00 % (0,75) | 1 |
| 2.1-07 | Le CMPC actualise des flux d'exploitation qui rémunèrent tous les apporteurs ; deux limites du MEDAF | 0,75 |

**Incertitude et rentabilité exigée (0,75 pt)**

Les apporteurs de capitaux ont de l'aversion pour le risque : ils n'acceptent de supporter l'incertitude d'un investissement que contre une rentabilité espérée supérieure à celle d'un placement sans risque. La rentabilité exigée est donc la somme du taux sans risque (rémunération du temps) et d'une prime de risque (rémunération de l'incertitude), d'autant plus élevée que le risque est fort. C'est un **coût d'opportunité** : la rentabilité que les apporteurs obtiendraient sur un placement de même risque. Un projet ne crée de la valeur que s'il rapporte plus que ce coût.

- **Proposition de M. CASTÉRAN (4,60 %, taux du prêt)** : elle confond le coût d'une source de financement et la rentabilité exigée de l'actif. Le taux d'actualisation dépend du risque du projet, non de la façon dont il est financé. Le prêt ne finance que la moitié du projet, et la dette accroît le risque supporté par les actionnaires (leur rentabilité exigée augmente, question ci-dessous). Actualiser à 4,60 % (voire 3,45 % après impôt) surestimerait les VAN et conduirait à accepter des projets qui détruisent de la valeur.
- **Proposition de l'administrateur de la métropole (4 %, taux sans risque)** : les flux des deux projets ne sont pas certains (volumes, prix renégociés, procédé nouveau, sécheresse). L'actionnaire public supporte ce risque comme les autres : il renonce à d'autres emplois de ses fonds (désendettement, autres équipements publics). Les partenaires privés, ALVÉDRA Environnement (28 %) et la Banque SORNAY (12 %), attendent une rémunération de marché. Le taux sans risque surévaluerait les projets et répartirait mal un capital rare (95 M€ de programme, projets exclusifs). La mission de service public peut justifier d'accepter un projet peu rentable, mais ce choix doit être fait en connaissant son coût, c'est-à-dire sa VAN au bon taux.

**Risque spécifique, risque systématique et choix de la société de référence (1 pt)**

- Le risque total d'un actif se décompose en **risque systématique** (ou de marché), lié à la conjoncture générale (taux d'intérêt, inflation, prix de l'énergie, activité économique), qui touche tous les actifs et ne se diversifie pas, et en **risque spécifique**, propre à l'entreprise ou au projet (panne de l'unité, refus d'autorisation sanitaire, défaillance du syndicat voisin), que l'investisseur élimine en diversifiant son portefeuille.
- Selon Markowitz (1952), la diversification réduit le risque spécifique, non le risque systématique. Le MEDAF (Sharpe, 1964) en tire la conséquence : un investisseur diversifié n'est rémunéré que pour le risque systématique, mesuré par le bêta. Le risque spécifique n'entre donc pas dans le taux : il se traite dans les flux et par l'analyse de sensibilité (question 2.4).
- **Hydrévia** n'exerce que le métier de l'eau : son bêta mesure le risque systématique de cette activité, peu cyclique (demande de première nécessité, tarifs encadrés). **AMBRELIS** est diversifiée vers les déchets et l'énergie, plus sensibles à la conjoncture (bêta 1,12) ; son bêta mêle des risques étrangers au projet. La diversification d'AMBRELIS réduit son risque spécifique, pas son risque systématique, qui est celui de son portefeuille d'activités : retenir son bêta surestimerait la rentabilité exigée du projet.
- Nuance : Valcroze Métropole, actionnaire à 60 %, n'est pas un investisseur diversifié ; le risque spécifique de ses projets la concerne directement, ce qui plaide pour l'analyse de sensibilité et la couverture du risque de sécheresse.

**Calculs (2,5 pts)**

Hydrévia : D / CP = 1 600 / 2 400 = 2/3.

| Étape | Calcul | Résultat |
|---|---|---:|
| Bêta désendetté d'Hydrévia | 0,78 / [1 + 0,75 × 2/3] = 0,78 / 1,5 | **0,5200** |
| Structure cible du projet | 50 % de dette, 50 % de fonds propres : D / CP = 1 | 1 |
| Bêta des fonds propres du projet | 0,52 × [1 + 0,75 × 1] = 0,52 × 1,75 | **0,9100** |
| Coût des fonds propres (MEDAF) | 4 % + 0,91 × 5 % | **8,55 %** |
| Coût net de la dette | 4,60 % × (1 − 0,25) | **3,45 %** |
| CMPC du projet | 50 % × 8,55 % + 50 % × 3,45 % = 4,275 % + 1,725 % | **6,00 %** |

La prime de risque exigée par les actionnaires du projet est de 0,91 × 5 % = 4,55 points : le risque systématique du projet, une fois tenu compte de l'endettement, est un peu inférieur à celui du marché (bêta 0,91 < 1).

**Pourquoi le CMPC du projet, et limites du MEDAF (0,75 pt)**

- Les flux des projets sont des **flux d'exploitation** calculés avant frais financiers (annexe 2.4) : ils servent à rémunérer à la fois les prêteurs et les actionnaires. Il faut donc les actualiser au coût moyen de l'ensemble des capitaux, pondéré selon la structure cible, soit le CMPC. Le coût des fonds propres (8,55 %) ne s'appliquerait qu'à des flux revenant aux actionnaires après service de la dette ; le taux du prêt ne rémunère que les prêteurs.
- Il s'agit du CMPC **du projet**, construit à partir du risque de l'activité eau et de la structure de financement propre au projet, et non du coût du capital moyen du groupe, qui ne vaut que pour des projets de même risque et de même financement. Retenir un taux unique pour A et B suppose que les deux projets ont le même risque systématique, celui du métier de l'eau ; les risques propres à A (procédé nouveau, clientèle agricole) sont spécifiques et traités par l'analyse de sensibilité de la question 2.4.
- **Limites du MEDAF** (deux attendues) : hypothèses fortes (marchés efficients, investisseurs rationnels et diversifiés, une seule période) ; bêta mesuré sur des données passées, instable, et emprunté ici à une société cotée de taille et de marché différents ; un seul facteur de risque, alors que Fama et French (1993) montrent que la taille et le rapport valeur comptable / valeur de marché expliquent aussi les rentabilités ; prime de risque du marché estimée, et sensibilité du résultat à cette estimation (une prime de 6 % donnerait un coût des fonds propres de 9,46 % et un CMPC de 6,455 %, soit près d'un demi-point de plus).

**Réponses tolérées** : bêtas à deux décimales (0,52 ; 0,91), sans effet sur les résultats ; CMPC présenté comme 6 % ; bêta réendetté calculé avec D / V au lieu de D / CP si l'erreur est isolée (sanctionnée en 2.1-04 seulement, suite notée en cohérence).

**Erreurs fréquentes**
- Moyenne des bêtas d'Hydrévia et d'AMBRELIS, ou bêta d'AMBRELIS retenu sans justification.
- Réendetter avec la structure d'Hydrévia (D / CP = 2/3) au lieu de la structure cible du projet ; oublier le facteur (1 − t) de la formule donnée.
- Actualiser les flux d'exploitation au coût des fonds propres ou au taux du prêt.
- Prime de marché prise pour la rentabilité du marché (4 % + 0,91 × 9 %).
- `JUR-E02` — démarche par comparables incomplète (désendettement puis réendettement, MEDAF, CMPC avec la formule donnée) ; `JUR-T14` — risque spécifique et risque systématique confondus ; `JUR-T13` — critique des deux propositions sans les données du cas.

---

### 2.2 VAN, TRI, indice de profitabilité et conflit de classement (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Flux du projet A : 4,35 M€ par an de 2028 à 2041, 5,85 M€ en 2042 | 0,5 |
| 2.2-02 | Flux du projet B : 4,20 M€ par an de 2028 à 2031, 4,95 M€ en 2032 | 0,5 |
| 2.2-03 | VAN au CMPC de 6,00 % : A 6,87 M€ ; B 3,25 M€ (0,5 par projet) | 1 |
| 2.2-04 | TRI : A 8,76 % (8,77 % par interpolation) ; B 13,48 % (13,49 % par interpolation) | 0,75 |
| 2.2-05 | Indices de profitabilité : A 1,19 ; B 1,22 | 0,5 |
| 2.2-06 | Conflit de classement et son origine (taille, durée, hypothèse de réinvestissement implicite) | 0,75 |

**Flux nets de trésorerie (1 pt)** (M€)

| | Projet A (2028 à 2042) | Projet B (2028 à 2032) |
|---|---:|---:|
| Chiffre d'affaires (volume × prix) | 6,0 × 1,20 = 7,20 | 4,0 × 1,50 = 6,00 |
| − Charges variables | 6,0 × 0,20 = − 1,20 | 4,0 × 0,20 = − 0,80 |
| − Charges fixes décaissées | − 1,00 | − 0,60 |
| **EBE** | **5,00** | **4,60** |
| − Amortissement | 36,00 / 15 = − 2,40 | 15,00 / 5 = − 3,00 |
| Résultat d'exploitation | 2,60 | 1,60 |
| − IS à 25 % | − 0,65 | − 0,40 |
| **Flux annuel (EBE − IS)** | **4,35** | **4,20** |
| Valeur résiduelle nette d'IS (dernière année) | 2,00 × 0,75 = 1,50 | 1,00 × 0,75 = 0,75 |
| **Flux de la dernière année** | **5,85** (2042) | **4,95** (2032) |
| Investissement à la date 0 | − 36,00 | − 15,00 |

**VAN au CMPC de 6,00 % (1 pt)**

- A : 4,35 × [1 − 1,06^−15] / 0,06 + 1,50 × 1,06^−15 − 36,00 = 4,35 × 9,712249 + 1,50 × 0,417265 − 36,00 = 42,25 + 0,63 − 36,00 = **6,87 M€**.
- B : 4,20 × [1 − 1,06^−5] / 0,06 + 0,75 × 1,06^−5 − 15,00 = 4,20 × 4,212364 + 0,75 × 0,747258 − 15,00 = 17,69 + 0,56 − 15,00 = **3,25 M€**.

Les deux VAN sont positives : chaque projet, pris isolément, crée de la valeur. Les projets étant exclusifs, la VAN classe **A devant B**.

**TRI (0,75 pt)**

| | Taux 1 | VAN au taux 1 | Taux 2 | VAN au taux 2 | TRI interpolé | TRI exact |
|---|---:|---:|---:|---:|---:|---:|
| A | 8 % | + 1,71 | 9 % | − 0,52 | 8 % + 1 % × 1,71 / (1,71 + 0,52) = **8,77 %** | **8,76 %** |
| B | 13 % | + 0,18 | 14 % | − 0,19 | 13 % + 1 % × 0,18 / (0,18 + 0,19) = **13,49 %** | **13,48 %** |

Détail : à 8 %, 4,35 × 8,559479 + 1,50 × 0,315242 − 36,00 = 1,71 ; à 9 %, 4,35 × 8,060688 + 1,50 × 0,274538 − 36,00 = − 0,52 ; à 13 %, 4,20 × 3,517231 + 0,75 × 0,542760 − 15,00 = 0,18 ; à 14 %, 4,20 × 3,433081 + 0,75 × 0,519369 − 15,00 = − 0,19.

Les deux TRI dépassent le CMPC de 6,00 % ; le TRI classe **B devant A**.

**Indices de profitabilité (0,5 pt)** : IP = flux actualisés / investissement = 1 + VAN / investissement.
- A : 42,87 / 36,00 = **1,19** ; B : 18,25 / 15,00 = **1,22**. L'IP classe **B devant A** : chaque euro investi dans B rapporte un peu plus de valeur actuelle.

**Conflit de classement et origine (0,75 pt)**

- La VAN place A en tête (6,87 M€ contre 3,25 M€) ; le TRI (13,48 % contre 8,76 %) et l'IP (1,22 contre 1,19) placent B en tête.
- Origines :
  - **taille** : A demande 36,00 M€, B 15,00 M€ ; la VAN mesure une création de valeur en euros, le TRI et l'IP une rentabilité relative ;
  - **durée et profil des flux** : B dure cinq ans, A quinze ; un TRI élevé sur une courte durée crée moins de valeur qu'un TRI plus faible sur un montant plus important et une durée longue ;
  - **hypothèse de réinvestissement implicite** : la VAN suppose que les flux intermédiaires sont réinvestis au CMPC (6 %), le TRI qu'ils le sont au TRI lui-même, soit 13,48 % pour B, rendement peu réaliste pour un groupe dont les projets courants rapportent autour de 6 %.
- Les profils de VAN se croisent : A a la VAN la plus forte pour un taux d'actualisation inférieur à environ 7,70 % (taux d'indifférence, où les deux VAN valent 2,42 M€), B au-delà. Au taux de 6,00 %, la VAN, cohérente avec l'objectif de création de valeur, est le critère de référence pour des projets exclusifs ; mais la comparaison est faussée par l'écart de durée, ce qu'examine la question 2.3.

**Réponses tolérées** : TRI de A de 8,76 % à 8,77 % et de B de 13,48 % à 13,49 % ; interpolation entre d'autres taux encadrants (par exemple 8 % et 10 %) si elle est annoncée, avec l'écart d'approximation qui en résulte ; VAN à ± 0,01 M€ près (facteurs arrondis) ; taux d'indifférence non demandé.

**Erreurs fréquentes**
- Oublier la valeur résiduelle ou ne pas l'imposer ; imposer l'EBE au lieu du résultat d'exploitation ; retrancher l'amortissement du flux.
- Déduire des frais financiers du prêt dans les flux alors qu'ils sont pris en compte par le CMPC.
- Conclure sur le seul TRI pour des projets exclusifs de tailles différentes.
- `JUR-I05` — VAN et TRI calculés sans analyse de leur divergence ; `JUR-T04` — acquis du DCG (VAN, TRI) mal maîtrisés ; `JUR-T07` — flux présentés sans tableau.

---

### 2.3 Durées inégales : annuité équivalente, VAN et TRI globaux, recommandation (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Annuités équivalentes : A 0,71 M€ ; B 0,77 M€ ; hypothèse de renouvellement à l'identique | 0,75 |
| 2.3-02 | Valeurs acquises en 2042 (A 91,91 M€ ; B 36,85 M€) et VAN globales : A 2,35 M€ ; B 0,38 M€ | 0,75 |
| 2.3-03 | TRI globaux : A 6,45 % ; B 6,17 % | 0,5 |
| 2.3-04 | Recommandation argumentée, reliée aux deux hypothèses et aux données du cas | 1 |

**Annuité équivalente (0,75 pt)** : AE = VAN / [(1 − (1 + k)^−n) / k], VAN répartie en annuités constantes sur la durée du projet.
- A : 6,87 / 9,712249 = **0,71 M€ par an** ; B : 3,25 / 4,212364 = **0,77 M€ par an**.
- B l'emporte, mais ce critère suppose que B puisse être **renouvelé à l'identique** (même investissement, mêmes flux, même taux) jusqu'à l'horizon de A et au-delà. Contrôle : B renouvelé deux fois sur 15 ans a une VAN de 3,25 × (1 + 1,06^−5 + 1,06^−10) = 7,50 M€ (= 0,77 × 9,712249), supérieure aux 6,87 M€ de A.

**VAN globale et TRI global sur 15 ans, B non renouvelé (1,25 pt)** : les flux sont capitalisés au taux de réinvestissement de 4,5 % jusqu'en 2042, puis la valeur acquise est actualisée au CMPC.

| | Projet A | Projet B |
|---|---:|---:|
| Valeur acquise en 2042 | 4,35 × (1,045^15 − 1) / 0,045 + 1,50 = 4,35 × 20,784054 + 1,50 = **91,91** | [4,20 × (1,045^5 − 1) / 0,045 + 0,75] × 1,045^10 = (4,20 × 5,470710 + 0,75) × 1,552969 = 23,73 × 1,552969 = **36,85** |
| Valeur actuelle à 6 % | 91,91 × 1,06^−15 = 91,91 × 0,417265 = 38,35 | 36,85 × 0,417265 = 15,38 |
| **VAN globale** | 38,35 − 36,00 = **2,35 M€** | 15,38 − 15,00 = **0,38 M€** |
| **TRI global** | (91,91 / 36,00)^(1/15) − 1 = **6,45 %** | (36,85 / 15,00)^(1/15) − 1 = **6,17 %** |

Avec un réinvestissement explicite à 4,5 %, inférieur au CMPC, les deux VAN globales sont inférieures aux VAN mais restent positives, et les deux TRI globaux dépassent 6 %. Les deux critères placent **A devant B** : le conflit de la question 2.2 disparaît quand on abandonne l'hypothèse irréaliste d'un réinvestissement au TRI de 13,48 %.

**Recommandation (1 pt)** : le choix dépend de l'hypothèse retenue pour l'après-2032. B n'est préférable que s'il peut être renouvelé à l'identique ; s'il ne l'est pas, A l'emporte. Le cas conduit à recommander **le projet A** :
- le renouvellement de B à l'identique est peu probable : la convention avec le syndicat voisin sera renégociée à un prix inconnu, les pompes et équipements du forage devront être remplacés, et la nappe profonde comme le syndicat voisin sont exposés aux mêmes sécheresses que le groupe ; B fournit de l'eau précisément quand elle risque de manquer aussi chez ses fournisseurs (risque corrélé) ;
- A crée une ressource qui dépend peu de la pluie, et la demande des irrigants augmente les années sèches : le projet réduit l'exposition du groupe au risque de sécheresse (lien avec la question 2.5) et sécurise la ressource sur quinze ans, ce qui est l'objet du programme d'investissement ;
- A crée le plus de valeur sur l'horizon commun (VAN globale 2,35 M€ contre 0,38 M€) et a la plus forte VAN ;
- réserves : A mobilise 36,00 M€, soit plus du tiers du programme de 95 M€, dans un procédé nouveau pour le groupe ; sa marge de sécurité doit être mesurée (question 2.4) et les contrats de quinze ans avec la métropole et les irrigants doivent être signés avant l'engagement.

**Grille de l'item 2.3-04**

| Note | Descripteur |
|---|---|
| 0 | Absence de choix ou choix sans justification |
| 0,5 | Choix fondé sur un seul critère chiffré, ou arguments généraux sans données du cas |
| 1 | Choix relié à l'hypothèse de renouvellement et à au moins deux éléments du cas (durée de la convention, exposition du syndicat et de la nappe à la sécheresse, résilience de A, montant investi) |

**Réponses tolérées** : choix de B accepté (au plus 0,5 point sur 2.3-04) s'il est explicitement fondé sur la possibilité de renouveler B à l'identique et discute ce risque ; comparaison sur 15 ans par la VAN de B renouvelé deux fois (7,50 M€) à la place de l'annuité équivalente ; VAN globale et TRI global de B calculés sur 5 ans seulement, si le candidat explique ensuite la nécessité d'un horizon commun (0,25 point sur 2.3-02 et 2.3-03).

**Erreurs fréquentes**
- Comparer directement les VAN de projets de durées différentes sans annuité équivalente ni horizon commun.
- Capitaliser au CMPC au lieu du taux de réinvestissement, ou actualiser la valeur acquise au taux de réinvestissement.
- Calculer le TRI global de B sur 5 ans, puis le comparer à celui de A sur 15 ans.
- `JUR-I05` — divergence des critères constatée sans être résolue ; `JUR-T13` — recommandation sans lien avec le cas ; `JUR-T01` — absence de posture de conseil (pas de recommandation au conseil d'administration).

---

### 2.4 Seuils de volume et de prix du projet A (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Volume annuel qui annule la VAN : 5,06 millions de m³, soit 15,73 % sous la prévision | 0,75 |
| 2.4-02 | Prix du m³ qui annule la VAN : 1,04 €, soit 13,11 % sous la prévision | 0,75 |
| 2.4-03 | Commentaire relié aux risques propres au projet et aux limites de l'analyse | 0,5 |

**Démarche** : la VAN est une fonction linéaire du volume et du prix. Un million de m³ de plus ou de moins modifie chaque flux annuel de la marge sur coût variable après IS, et la VAN de ce montant multiplié par le facteur d'annuité sur 15 ans.

**Volume d'équilibre (0,75 pt)**
- Effet d'un million de m³ sur la VAN : (1,20 − 0,20) × 0,75 × 9,712249 = 7,28 M€.
- Volume d'équilibre : 6,0 − 6,87 / 7,28 = **5,06 millions de m³** par an (5,0563 sans arrondi), soit une baisse de 0,94 million de m³ ou **15,73 %** de la prévision.

**Prix d'équilibre (0,75 pt)**
- Effet d'1 € par m³ sur la VAN : 6,0 × 0,75 × 9,712249 = 43,71 M€.
- Prix d'équilibre : 1,20 − 6,87 / 43,71 = **1,04 € par m³** (1,0427 sans arrondi), soit une baisse de **13,11 %**.
- Contrôle : dans les deux cas, le flux annuel d'équilibre est de 3,64 M€ (3,6422 sans arrondi, au lieu de 4,35 M€) : 3,6422 × 9,712249 + 1,50 × 0,417265 − 36,00 = 0.

**Commentaire (0,5 pt)**
- La marge de sécurité est réelle mais limitée : la VAN devient nulle si les volumes vendus sont inférieurs de 16 % aux prévisions, ou le prix de 13 %. Le projet est plus sensible au prix qu'au volume, mais le prix est fixé par des contrats de quinze ans, ce qui réduit ce risque ; le risque principal porte sur les volumes : démarrage d'un procédé nouveau pour le groupe, autorisation sanitaire des usages, acceptation de l'eau recyclée par les agriculteurs, durée effective des contrats.
- Ces risques sont propres au projet (risque spécifique) : ils ne sont pas dans le CMPC, d'où l'intérêt de cette analyse. À l'inverse, la sécheresse augmente la demande des irrigants : sur ce point, le volume de A varie dans le sens favorable au groupe.
- Les charges variables (électricité surtout) devraient passer de 0,20 € à 0,36 € par m³ (+ 79 %) pour annuler la VAN : le risque sur le prix de l'électricité pèse moins sur ce projet.
- Limites : un seul paramètre varie à la fois ; une sécheresse ou une hausse des coûts combinée à un retard de démarrage réduirait la marge de sécurité ; l'analyse ne donne pas de probabilité. Recommandation : engager le projet après signature des contrats avec des volumes minimaux garantis.

**Réponses tolérées** : volume à 5,05 ou 5,06 millions de m³ et baisse de 15,7 % à 15,8 % selon les arrondis ; baisse du prix calculée à partir du prix arrondi (13,33 %) ; raisonnement par le flux annuel d'équilibre (3,64 M€) puis le volume ou le prix correspondant.

**Erreurs fréquentes**
- Oublier l'IS sur la variation de marge, ou faire varier aussi l'amortissement.
- Faire varier le chiffre d'affaires sans les charges variables pour le volume.
- Confondre seuil de rentabilité comptable (résultat nul) et seuil de VAN nulle.
- `JUR-T13` — sensibilité calculée sans commentaire sur les risques du cas ; `JUR-T02` — calcul non relié à la notion de risque spécifique.

---

### 2.5 Risque de sécheresse, option climatique, assurance et prix de l'électricité (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Risques physiques et de transition liés à la sécheresse et leurs effets sur la trésorerie, appliqués au cas | 0,75 |
| 2.5-02 | Indemnités : 0 ; 1,60 M€ ; 3,20 M€ (plafond) | 0,5 |
| 2.5-03 | Effets nets sur l'EBITDA : + 0,15 ; − 1,25 ; − 1,75 M€, comparés à l'absence de couverture et commentés | 0,75 |
| 2.5-04 | Assurance paramétrique et réassurance ; couverture du prix de l'électricité | 1 |

**Risques et effets sur la trésorerie (0,75 pt)**
- **Risques physiques** : aigus (sécheresses de 2022 et de 2025, canicules) et chroniques (baisse durable des nappes, étiages plus longs, hausse des températures qui accroît la demande de pointe). Effets : restrictions d'usage et baisse des volumes vendus, alors que les charges sont surtout fixes (réseaux, stations, personnel) ; achats d'eau d'appoint, pompage plus profond et traitement plus coûteux ; investissements anticipés (programme de 95 M€).
- **Risques de transition** : réglementation plus stricte des prélèvements et objectifs de sobriété qui réduisent durablement les volumes vendus ; hausse du prix de l'énergie et du carbone ; procédés nouveaux à maîtriser (réutilisation des eaux usées) ; réputation et acceptabilité des usages.
- **Effets sur la trésorerie** : moindres encaissements et décaissements accrus, d'autant plus marqués que les tarifs, fixés avec la métropole, ne répercutent pas immédiatement les hausses de coûts ; besoin de financement accru pour un groupe déjà endetté. L'annexe chiffre la sensibilité : 0,03 M€ d'EBITDA par millimètre de pluie.

**Option climatique (1,25 pt)** : indemnité = 0,04 × max(0 ; 280 − indice), plafonnée à 3,20 M€ (plafond atteint dès 200 mm) ; effet de la pluviométrie sur l'EBITDA = 0,03 × (indice − 320) ; prime de 0,45 M€.

| Scénario (M€) | Humide, 340 mm | Sécheresse modérée, 240 mm | Sécheresse sévère, 170 mm |
|---|---:|---:|---:|
| Effet de la pluviométrie sur l'EBITDA | 0,03 × 20 = + 0,60 | 0,03 × (− 80) = − 2,40 | 0,03 × (− 150) = − 4,50 |
| Indemnité de l'option | 0 (option non exercée) | 0,04 × 40 = **1,60** | min(0,04 × 110 = 4,40 ; 3,20) = **3,20** |
| − Prime | − 0,45 | − 0,45 | − 0,45 |
| **Effet net avec couverture** | **+ 0,15** | **− 1,25** | **− 1,75** |
| Effet sans couverture | + 0,60 | − 2,40 | − 4,50 |

Lecture :
- l'option réduit fortement la perte en cas de sécheresse (− 1,25 au lieu de − 2,40 ; − 1,75 au lieu de − 4,50) ; en année humide, la prime est perdue mais compensée par des ventes plus fortes : c'est le coût certain de la protection ;
- la couverture est imparfaite : aucune indemnité entre 320 et 280 mm (perte non couverte jusqu'à 40 × 0,03 = 1,20 M€, qui joue comme une franchise) ; plafond de 3,20 M€ au-delà de 200 mm ; entre 280 et 200 mm, l'option verse 0,04 M€ par millimètre pour une perte de 0,03 M€ : l'indemnité rattrape progressivement la franchise, et à 200 mm la perte non couverte n'est plus que de 0,40 M€ (3,60 − 3,20) avant prime ;
- **risque de base** : l'indice relevé à une seule station, d'avril à septembre, ne reproduit pas exactement les pertes du groupe (les nappes se rechargent surtout l'hiver) ;
- **risque de contrepartie** sur la Banque SORNAY, qui est déjà actionnaire et prêteur du groupe : concentration des relations ;
- l'option couvre un **risque de volume** pour une saison ; elle ne réduit pas le risque physique, que seuls les investissements de sécurisation (projet A) traitent durablement.

**Assurance paramétrique, réassurance et électricité (1 pt)**
- **Assurance paramétrique** : même logique d'indice (indemnité forfaitaire dès qu'un seuil est franchi, versée rapidement, sans expertise des pertes), mais sous la forme d'un contrat d'assurance. Les assurances classiques couvrent mal une perte de chiffre d'affaires sans dommage matériel, d'où l'intérêt de ces solutions indicielles. Le choix entre option et assurance se fait sur le coût (prime), le seuil et le plafond, le risque de base et la solidité de la contrepartie.
- **Réassurance** : l'assureur mutualise les risques de ses assurés et en cède une partie à un réassureur (traités en quote-part ou en excédent de sinistre), qui peut lui-même les transférer aux marchés financiers par des obligations catastrophe ; une sécheresse touchant toute une région frappe en même temps de nombreux assurés, ce qui rend la réassurance indispensable à l'assureur et pèse sur le prix de la protection.
- **Prix de l'électricité** : 7,40 M€ d'achats à prix indexé sur le marché de gros, sans répercussion immédiate dans les tarifs. Le groupe peut fixer son prix d'achat : contrat de fourniture à prix fixe sur plusieurs années, achat à terme d'électricité (contrats à terme sur les marchés de l'énergie ou de gré à gré), échange d'un prix variable contre un prix fixe, contrat d'achat de long terme auprès d'un producteur d'électricité renouvelable ; il peut aussi réduire son exposition par la sobriété énergétique et la production propre (biométhane, solaire sur ses sites). Il s'agit d'une couverture de **prix**, complémentaire de la couverture de **volume** apportée par l'option climatique.

**Grille de l'item 2.5-04**

| Note | Descripteur |
|---|---|
| 0 | Absence de réponse ou réponse non pertinente |
| 0,5 | Deux des trois points traités (assurance paramétrique, réassurance, électricité), ou réponse générale sans le cas |
| 1 | Les trois points traités, avec au moins un instrument précis de couverture du prix de l'électricité et un lien avec le cas |

**Réponses tolérées** : présentation en résultat avant impôt ou après impôt (effets nets × 0,75) si elle est annoncée ; prime traitée comme une charge de l'exercice 2027 ; mention du régime des catastrophes naturelles en complément, sans développement juridique.

**Erreurs fréquentes**
- Oublier le plafond de l'indemnité (4,40 M€ au lieu de 3,20 M€) ou la prime dans le résultat net.
- Calculer l'indemnité à partir de l'année normale (320 mm) au lieu du prix d'exercice (280 mm).
- Présenter l'option comme une couverture du prix de l'eau ou de l'électricité, ou chercher à calculer sa valeur (la prime est donnée).
- `JUR-T05` — risque climatique traité sans lien avec la performance durable et les projets du groupe ; `JUR-T13` — liste générale de risques sans les données du cas.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 74-76 ; programme l. 578-592 | relation incertitude et rentabilité exigée, prime de risque, MEDAF et ses limites, Fama-French pour interpréter le risque, risque spécifique et systématique | [V] | F02 § 0, 2 et 7 ; `perimetre_ue2.yaml` |
| Formule de Hamada avec IS | désendettement et réendettement du bêta, donnée dans l'énoncé | [S] | F02 § 3 |
| CMPC | pondération en valeurs de marché, coût de la dette net d'IS, taux d'actualisation des flux d'exploitation | [V] | F02 § 5 |
| Markowitz (1952) | diversification : réduction du risque spécifique, non du risque systématique | [V programme 5.3] | F10 § 2 |
| Sharpe (1964) | MEDAF : seul le risque systématique, mesuré par le bêta, est rémunéré | [V contexte ; MEDAF au programme 5.2] | F10 § 2 |
| Fama et French (1993) | modèle à trois facteurs (marché, taille, valeur), limite du MEDAF | [V programme 5.2] | F10 § 2 ; F02 § 7 |
| Guide pédagogique DSCG, juillet 2026, p. 80-81 ; programme l. 642-647 | VAN, VANG, TRI, IP, projets mutuellement exclusifs, analyse de sensibilité | [V] | F01 § 0, 4 et 5 |
| VAN globale, TRI global, annuité équivalente, conflit VAN / TRI | formules et hypothèses de réinvestissement et de renouvellement | [S] | F01 § 4 |
| Guide pédagogique DSCG, juillet 2026, p. 79-80 ; programme l. 635-639 | risques physiques et de transition, effets sur la trésorerie, assurance et réassurance, dérivés climatiques et sur matières premières, prime donnée | [V] | F07 § 5 |
| Dérivés climatiques, risque de base, réassurance, obligations catastrophe | mécanismes de place | [S] | F07 § 5 |
| Taux sans risque 4 %, prime de risque du marché 5 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 § 1 et 2 |
| Données des projets, sociétés de référence, sensibilité à la pluviométrie, option climatique | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 2.1 à 2.3 |
