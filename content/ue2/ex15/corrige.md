# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 15 — Dossier 3 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F06 marchés financiers et finance comportementale, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (rentabilités espérées, variances, écarts types, covariances, bêtas, portefeuilles, ratios de Sharpe et de Treynor, MEDAF, Gordon-Shapiro, barème, liste noire, hors-programme ; décompositions du risque, résultats de 2022 et frais vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple des ratios de Sharpe calculés à la question 3.4 avec un écart type erroné à la question 3.1).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Rentabilité et risque des fonds, de l'indice et du portefeuille actuel | `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres ; `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier ; `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) | 4 |
| 3.2 Diversification et choix de l'allocation | `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) | 2,5 |
| 3.3 Risque systématique et risque spécifique ; MEDAF et panier agroalimentaire | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance ; `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier | 3,5 |
| 3.4 Ratios de Sharpe et de Treynor | `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres ; `5.2.b` | 2 |
| 3.5 Gestion active ou indicielle ; biais du conseil d'administration | `5.1.c` Maîtriser les grands enseignements de l'efficience informationnelle des marchés (Fama, 1970) ; `5.1.d` Maîtriser les grands enseignements de la finance comportementale | 3 |
| **Total** | | **15** |

Part du calcul : environ 8,5 points (3.1-01 à 3.1-05, 3.2-01, 3.2-02, 3.3-01 à 3.3-05, 3.4-01, 3.4-02, 3.5-01). Part de l'analyse : environ 6,5 points. Les questions 3.2 à 3.5 se terminent toutes par une recommandation au conseil : elles ne doivent pas être sacrifiées faute de temps, ce dossier étant le dernier de l'épreuve (`JUR-T15`).

---

### 3.1 Rentabilité et risque des fonds, de l'indice et du portefeuille actuel (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Rentabilités espérées : fonds actions 8,00 %, fonds obligataire 5,00 %, indice 9,00 % | 0,5 |
| 3.1-02 | Écarts types sur n − 1 : fonds actions 18,09 % (variance 0,032726), fonds obligataire 5,27 % (0,002774), indice 16,00 % (0,025600) ; 0,5 par série | 1,5 |
| 3.1-03 | Covariance des deux fonds : 0,51 × 18,09 % × 5,27 % = 0,004859 | 0,5 |
| 3.1-04 | Rentabilité espérée du portefeuille actuel : 6,80 % | 0,5 |
| 3.1-05 | Écart type du portefeuille actuel : 12,07 % (variance 0,014558) | 0,5 |
| 3.1-06 | Commentaire : le fonds actions rapporte moins que l'indice pour un risque plus élevé ; le fonds obligataire, moins rentable, est beaucoup moins risqué | 0,5 |

**Conventions rappelées.** Rentabilité espérée = moyenne arithmétique des cinq rentabilités annuelles ; variance et covariance sur n − 1 = 4 ; calculs sans arrondi intermédiaire ; pourcentages à deux décimales, variances à six décimales.

**Rentabilités espérées (0,5 pt).**
- Fonds actions : (− 12,1 + 19,4 − 11,3 + 19,7 + 24,3) / 5 = 40,0 / 5 = **8,00 %**.
- Fonds obligataire : (− 4,2 + 5,8 + 8,4 + 8,4 + 6,6) / 5 = 25,0 / 5 = **5,00 %**.
- Indice : (− 12 + 23 − 4 + 16 + 22) / 5 = 45 / 5 = **9,00 %**.

**Variances et écarts types (1,5 pt).** Calcul en pourcentage (variances en %²) :

| Écart à la moyenne (points de %) | 2022 | 2023 | 2024 | 2025 | 2026 | Somme des carrés | Variance (÷ 4) | Écart type |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Fonds actions | − 20,1 | 11,4 | − 19,3 | 11,7 | 16,3 | 1 309,04 | 327,26 %² = 0,032726 | **18,09 %** |
| Fonds obligataire | − 9,2 | 0,8 | 3,4 | 3,4 | 1,6 | 110,96 | 27,74 %² = 0,002774 | **5,27 %** |
| Indice | − 21,0 | 14,0 | − 13,0 | 7,0 | 13,0 | 1 024,00 | 256,00 %² = 0,025600 | **16,00 %** |

**Covariance des deux fonds (0,5 pt).** Le coefficient de corrélation est fourni (0,51) : cov(A, O) = ρ × σA × σO = 0,51 × 18,0903 × 5,2669 = 48,59 %², soit **0,004859**.

**Portefeuille actuel (1 pt).** Poids 60 % / 40 %.
- Rentabilité espérée : 0,60 × 8,00 % + 0,40 × 5,00 % = **6,80 %**.
- Variance : 0,60² × 327,26 + 0,40² × 27,74 + 2 × 0,60 × 0,40 × 48,59 = 117,81 + 4,44 + 23,32 = 145,58 %², soit 0,014558. Écart type : √0,014558 = **12,07 %**.

**Commentaire (0,5 pt).**
- Le fonds actions a rapporté en moyenne 8,00 % par an, **un point de moins que l'indice** (9,00 %), avec un risque **plus élevé** (18,09 % contre 16,00 %) : sur la période, il fait moins bien que l'indice sur les deux plans, premier signal défavorable pour le mandat de gestion active.
- Le fonds obligataire rapporte moins (5,00 %), mais il est plus de trois fois moins risqué (5,27 %).
- Remarque facultative, non notée ici (voir question 3.2) : le portefeuille offre 6,80 % pour un écart type de 12,07 %, inférieur à la moyenne pondérée des écarts types (12,96 %) : la combinaison des deux fonds, imparfaitement corrélés, réduit le risque (question 3.2).

**Réponses tolérées** : calcul en fraction (variance 0,025600, écart type 0,1600) ; covariance calculée avec les écarts types arrondis (48,62 %², soit 0,004862) ; écart type du portefeuille de 12,07 % dans les deux cas ; covariance des deux fonds calculée directement à partir des séries (0,004857), si la démarche est indiquée.

**Erreurs fréquentes**
- Diviser par n (5) au lieu de n − 1 (4) : écarts types de 16,18 %, 4,71 % et 14,31 %, contraires à la convention de l'annexe.
- Confondre variance et écart type, ou oublier le facteur 2 du terme de covariance dans la variance du portefeuille.
- Additionner les écarts types pondérés (12,96 %) au lieu de calculer la variance du portefeuille : c'est ignorer la corrélation.
- `JUR-T07` — calculs présentés sans tableau des écarts à la moyenne.

---

### 3.2 Diversification et choix de l'allocation (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Allocations proposées : prudente 30 / 70 : 5,90 % et 7,97 % ; dynamique 80 / 20 : 7,40 % et 15,04 % | 0,5 |
| 3.2-02 | Résultat en 2022 : actuelle − 8,94 % (− 3 755 k€) ; prudente − 6,57 % (− 2 759 k€) ; dynamique − 10,52 % (− 4 418 k€) | 0,5 |
| 3.2-03 | Rôle de la corrélation au sens de Markowitz (1952), illustré par le portefeuille actuel (12,07 % < 12,96 %) | 0,5 |
| 3.2-04 | Recommandation : confrontation aux deux contraintes, à l'horizon et à la finalité de la réserve ; maintien de l'allocation 60 / 40 | 1 |

**Rentabilité et risque des deux propositions (0,5 pt).** Même méthode qu'à la question 3.1, avec ρ = 0,51.

| Allocation (actions / obligations) | Rentabilité espérée | Variance | Écart type | Moyenne pondérée des écarts types |
|---|---:|---:|---:|---:|
| Prudente 30 / 70 | 0,3 × 8 + 0,7 × 5 = **5,90 %** | 29,45 + 13,59 + 20,41 = 63,45 %² (0,006345) | **7,97 %** | 9,11 % |
| Actuelle 60 / 40 | 6,80 % | 145,58 %² (0,014558) | 12,07 % | 12,96 % |
| Dynamique 80 / 20 | 0,8 × 8 + 0,2 × 5 = **7,40 %** | 209,45 + 1,11 + 15,55 = 226,11 %² (0,022611) | **15,04 %** | 15,53 % |

**Résultat en 2022 (0,5 pt).** Rentabilités de 2022 : fonds actions − 12,1 %, fonds obligataire − 4,2 % ; encours de 42 000 k€.

| Allocation | Rentabilité 2022 | Résultat sur 42 000 k€ | Contrainte de 4 000 k€ | Objectif de 6 % |
|---|---:|---:|---|---|
| Prudente 30 / 70 | 0,3 × (− 12,1) + 0,7 × (− 4,2) = **− 6,57 %** | **− 2 759 k€** | respectée | non atteint (5,90 %) |
| Actuelle 60 / 40 | 0,6 × (− 12,1) + 0,4 × (− 4,2) = **− 8,94 %** | **− 3 755 k€** | respectée | atteint (6,80 %) |
| Dynamique 80 / 20 | 0,8 × (− 12,1) + 0,2 × (− 4,2) = **− 10,52 %** | **− 4 418 k€** | **dépassée** | atteint (7,40 %) |

**Rôle de la corrélation (0,5 pt).** Selon Markowitz (1952), le risque d'un portefeuille ne dépend pas seulement du risque de chacun de ses titres, mais aussi de leurs covariances : tant que la corrélation est inférieure à 1, l'écart type du portefeuille est inférieur à la moyenne pondérée des écarts types, sans que la rentabilité espérée (moyenne pondérée des rentabilités) soit réduite. En l'espèce, l'écart type du portefeuille actuel (12,07 %) est inférieur de 0,90 point à la moyenne pondérée (12,96 %), qui serait atteinte avec une corrélation de 1 ; avec une corrélation nulle, il tomberait à 11,06 % (calcul facultatif). Plus la corrélation est faible, plus le gain de diversification est fort. La corrélation de 0,51 limite ce gain : les deux fonds dépendent tous deux de la conjoncture de la zone euro et ont baissé ensemble en 2022, année de forte remontée des taux ; ils ont en revanche évolué en sens contraire en 2024 (− 11,3 % et + 8,4 %).

**Recommandation (1 pt).**
- Aucune allocation ne domine les autres : la rentabilité espérée augmente avec le poids des actions, mais le risque aussi. Le choix dépend donc des objectifs et des contraintes de l'investisseur ; les ratios de Sharpe des trois allocations sont d'ailleurs très proches (0,24 pour la prudente, 0,23 pour les deux autres, calcul facultatif).
- La proposition **dynamique** est la plus rentable (7,40 %), et un horizon d'au moins huit ans plaide en faveur des actions. Mais elle aurait fait perdre 4 418 k€ en 2022 : elle **viole la contrainte de perte** fixée par la charte.
- La proposition **prudente** respecte largement cette contrainte (− 2 759 k€) mais **n'atteint pas l'objectif de rentabilité** (5,90 % < 6 %).
- L'allocation **actuelle 60 / 40** est la seule qui respecte les deux conditions (6,80 % ; − 3 755 k€) : il est recommandé de la **maintenir**.
- Cette contrainte de perte est essentielle pour une coopérative : la réserve doit pouvoir être mobilisée en cas de crise laitière, qui peut coïncider avec une baisse des marchés ; l'horizon long ne suffit donc pas à justifier une allocation plus risquée. La présidente le rappelle (annexe 3.3). La marge restante est faible (245 k€), ce qui invite à réexaminer l'allocation chaque année.

**Réponses tolérées** : calcul des résultats de 2022 en M€ (− 3,75 ; − 2,76 ; − 4,42) ; recommandation différente (par exemple une allocation proche de 60 / 40, ou l'allocation prudente au nom de la sécurité de la réserve) si elle est confrontée explicitement aux deux contraintes de la charte ; mention de l'instabilité des corrélations en période de crise.

**Erreurs fréquentes**
- Recommander l'allocation dynamique au seul motif de sa rentabilité, sans vérifier la contrainte de perte.
- Croire que la diversification supprime tout risque : elle réduit le risque, mais ne supprime pas le risque commun aux deux fonds.
- `JUR-T13` — recommandation générale, sans lien avec la finalité de la réserve et les chiffres de l'annexe 3.2.
- `JUR-T14` — Markowitz cité sans expliquer le rôle de la corrélation.

---

### 3.3 Risque systématique et risque spécifique ; MEDAF et panier agroalimentaire (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Covariance du fonds actions et de l'indice : 0,028160 ; bêta = 0,028160 / 0,025600 = 1,10, conforme à la donnée de la société de gestion | 0,5 |
| 3.3-02 | Fonds actions : risque systématique 0,030976, soit 94,65 % de la variance ; risque spécifique 0,001750, soit 5,35 % | 0,5 |
| 3.3-03 | Rentabilités exigées (MEDAF) : fonds actions 9,50 % (contre 8,00 % obtenus) ; panier 8,00 % | 0,5 |
| 3.3-04 | Rentabilité espérée du panier (Gordon-Shapiro) : 2,4 % + 3,6 % = 6,00 % | 0,5 |
| 3.3-05 | Panier : variance 0,062500 ; risque systématique 0,016384, soit 26,21 % ; risque spécifique 0,046116, soit 73,79 % | 0,5 |
| 3.3-06 | Distinction des deux risques et conclusion sur le panier : risque spécifique non rémunéré, rentabilité espérée inférieure à la rentabilité exigée, concentration sur le secteur de la coopérative ; projet à écarter | 1 |

**Covariance et bêta du fonds actions (0,5 pt).** Produits des écarts à la moyenne (fonds actions × indice) : (− 20,1 × − 21) + (11,4 × 14) + (− 19,3 × − 13) + (11,7 × 7) + (16,3 × 13) = 422,1 + 159,6 + 250,9 + 81,9 + 211,9 = 1 126,4. Covariance : 1 126,4 / 4 = 281,6 %², soit **0,028160**. Bêta = cov(A, M) / var(M) = 0,028160 / 0,025600 = **1,10** : le bêta communiqué par KERLÉVAN Gestion est vérifié. Le fonds amplifie de 10 % les variations de l'indice.

**Décomposition du risque du fonds actions (0,5 pt).**
- Risque systématique : β² × var(M) = 1,10² × 0,025600 = **0,030976**, soit 0,030976 / 0,032726 = **94,65 %** de la variance (écart type 17,60 %).
- Risque spécifique : 0,032726 − 0,030976 = **0,001750**, soit **5,35 %** (écart type 4,18 %).

**Rentabilités exigées par le MEDAF (0,5 pt).** E(Ri) = rf + βi × prime de risque du marché.
- Fonds actions : 4 % + 1,10 × 5 % = **9,50 %**, contre 8,00 % obtenus en moyenne : le fonds se situe 1,50 point sous la rentabilité que justifie son risque systématique.
- Panier agroalimentaire : 4 % + 0,80 × 5 % = **8,00 %**.

**Rentabilité espérée du panier (0,5 pt).** Avec une croissance constante et illimitée du dividende, le modèle de Gordon-Shapiro donne P0 = prochain dividende / (k − g), d'où la rentabilité espérée k = prochain dividende / P0 + g = 2,40 / 100 + 3,6 % = 2,4 % + 3,6 % = **6,00 %**.

**Décomposition du risque du panier (0,5 pt).** Variance totale : 0,25² = 0,062500. Risque systématique : 0,80² × 0,025600 = **0,016384**, soit **26,21 %** (écart type 12,80 %). Risque spécifique : 0,062500 − 0,016384 = **0,046116**, soit **73,79 %** (écart type 21,47 %).

**Analyse et conclusion (1 pt).**
- **Deux risques.** Le risque systématique (de marché) provient des facteurs qui affectent toutes les entreprises (croissance, taux, inflation) ; il ne peut pas être éliminé par la diversification et il est le seul que le marché rémunère, comme l'exprime le MEDAF par le bêta. Le risque spécifique est propre à chaque entreprise ou à chaque secteur (prix des matières premières agricoles, négociations avec la distribution, crise sanitaire) ; il se diversifie et n'est donc pas rémunéré.
- **Fonds actions.** Bien diversifié, il ne porte presque plus que du risque systématique (94,65 %) : il se comporte presque comme l'indice, avec un bêta de 1,10. Son risque est donc rémunérable, mais il n'a pas obtenu la rentabilité exigée (8,00 % contre 9,50 %).
- **Panier.** Concentré sur cinq valeurs d'un même secteur, il porte surtout du risque spécifique (73,79 %), qui ne serait pas rémunéré. Sa rentabilité espérée (6,00 %) est inférieure de 2 points à la rentabilité exigée (8,00 %) : au prix actuel, le panier serait trop cher (valeur théorique de 54,55 € pour 100 € investis au taux de 8 %, calcul facultatif). Les 12 % évoqués par un administrateur décrivent les trois dernières années, pas une espérance.
- **Spécificité coopérative.** Ces sociétés sont des concurrents et des clients d'ORNELAC : leurs résultats dépendent des mêmes facteurs que ceux de la coopérative (prix du lait, demande de produits laitiers, relations avec la distribution). En cas de crise laitière, le panier perdrait probablement de la valeur au moment où la réserve doit être mobilisée. Le risque spécifique du panier est aussi celui de l'activité de la coopérative : pour ORNELAC, il ne se diversifie pas, il s'ajoute.
- **Conclusion** : il est recommandé de ne pas investir 8 M€ (19,05 % de la réserve) dans le panier. Si le conseil tient à une exposition au secteur, elle doit rester marginale et passer par un fonds diversifié.

**Réponses tolérées** : une conclusion courte obtient tous les points si elle est reliée aux chiffres du cas (le développement ci-dessus va au-delà de l'attendu) ; part systématique calculée par le carré du coefficient de corrélation entre le fonds et l'indice (0,9729² = 94,65 %) ; parts exprimées en écarts types (17,60 % et 4,18 % pour le fonds) si la décomposition porte bien sur les variances ; conclusion fondée sur l'écart entre rentabilité espérée et rentabilité exigée (alpha de − 2 points), présentée par le candidat sous un autre nom.

**Erreurs fréquentes**
- Décomposer les écarts types au lieu des variances (17,60 % + 4,18 % ≠ 18,09 %).
- Appliquer le MEDAF avec la rentabilité du marché à la place de la prime (4 % + 0,80 × 9 % = 11,20 %).
- Prendre le rendement du dividende (2,4 %) pour la rentabilité espérée du panier, en oubliant la croissance.
- Juger le panier sur son écart type total sans distinguer le risque rémunéré du risque diversifiable.
- `JUR-T13` — conclusion sans lien avec la situation de la coopérative, déjà exposée au secteur agroalimentaire par son activité.

---

### 3.4 Ratios de Sharpe et de Treynor (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Ratios de Sharpe : fonds actions 0,22 ; portefeuille 0,23 ; indice 0,31 | 0,5 |
| 3.4-02 | Bêta du portefeuille 0,74 ; ratios de Treynor : fonds actions 3,64 % ; portefeuille 3,78 % ; indice 5,00 % | 0,5 |
| 3.4-03 | Interprétation : le fonds actions et le portefeuille font moins bien que l'indice par unité de risque total comme de risque systématique | 0,5 |
| 3.4-04 | Limites : mesures passées sur cinq ans, sensibles à la période et au taux sans risque ; choix du ratio selon la diversification ; portefeuille mixte comparé à un indice d'actions | 0,5 |

**Calculs (1 pt).** Bêta du portefeuille : 0,60 × 1,10 + 0,40 × 0,20 = **0,74**.

| Placement | Rentabilité espérée | Écart type | Bêta | Sharpe = (E − 4 %) / σ | Treynor = (E − 4 %) / β |
|---|---:|---:|---:|---:|---:|
| Fonds actions | 8,00 % | 18,09 % | 1,10 | 4,00 / 18,09 = **0,22** | 4,00 / 1,10 = **3,64 %** |
| Portefeuille actuel | 6,80 % | 12,07 % | 0,74 | 2,80 / 12,07 = **0,23** | 2,80 / 0,74 = **3,78 %** |
| Indice | 9,00 % | 16,00 % | 1,00 | 5,00 / 16,00 = **0,31** | 5,00 / 1,00 = **5,00 %** |
| Fonds obligataire (facultatif) | 5,00 % | 5,27 % | 0,20 | 0,19 | 5,00 % |

**Interprétation (0,5 pt).** Le ratio de Sharpe (1966) mesure la prime de rentabilité obtenue par unité de risque total ; le ratio de Treynor (1965), par unité de risque systématique. Le fonds actions obtient 0,22 contre 0,31 pour l'indice selon le premier, et 3,64 % contre 5,00 % selon le second : quelle que soit la mesure du risque, la gestion active a rémunéré moins bien le risque pris que le simple placement dans l'indice. Le portefeuille actuel fait à peine mieux que le fonds actions (0,23 ; 3,78 %), grâce à la diversification apportée par le fonds obligataire, mais reste nettement derrière l'indice.

**Limites (0,5 pt).**
- Mesures **passées**, sur cinq années seulement : elles dépendent fortement de la période retenue (une seule année comme 2022 ou 2024 pèse lourd) et ne préjugent pas de la performance future.
- Le taux sans risque de 4 % est une hypothèse simplificatrice pour 2022-2026 : un taux plus bas changerait le niveau des ratios, mais guère leur classement.
- Le **ratio de Treynor** suppose un portefeuille bien diversifié, dont le seul risque est systématique : il convient au fonds actions, pas au fonds obligataire, dont le bêta très faible lui donne un ratio flatteur (5,00 %). Pour une réserve qui constitue l'essentiel des placements de la coopérative, c'est le risque total qui compte : le **ratio de Sharpe** est le critère le plus pertinent.
- Le portefeuille mixte est comparé à un indice d'actions : la référence équitable serait une combinaison indicielle 60 / 40 (question 3.5). Les deux ratios reposent enfin sur un bêta et des écarts types estimés, instables dans le temps.

**Réponses tolérées** : ratios de Sharpe à trois décimales (0,221 ; 0,232 ; 0,313) ; ratio de Treynor en fraction (0,0364) ; indice à 0,3125 ; ratios du portefeuille calculés avec un écart type ou un bêta erronés, notés en cohérence.

**Erreurs fréquentes**
- Inverser les dénominateurs : Sharpe sur l'écart type, Treynor sur le bêta.
- Oublier de retrancher le taux sans risque (8 / 18,09 = 0,44).
- Juger un portefeuille mixte au seul ratio de Treynor.
- `JUR-T02` — ratios calculés sans interprétation ni lien avec le renouvellement du mandat.

---

### 3.5 Gestion active ou indicielle ; biais du conseil d'administration (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Frais : 462 k€ par an pour le mandat contre 84 k€ en gestion indicielle, économie de 378 k€ par an (0,90 point) ; fonds actions avant frais : 8,00 % + 1,50 % = 9,50 %, égal à la rentabilité exigée par le MEDAF | 0,5 |
| 3.5-02 | Efficience informationnelle (Fama, 1970) : définition, trois formes, conséquence pour la gestion active | 0,5 |
| 3.5-03 | Conclusion argumentée en faveur de la gestion indicielle, avec ses limites | 0,5 |
| 3.5-04 | Deux biais identifiés, chacun relié à un extrait et aux chiffres du cas (0,5 par biais, dans la limite de 1) | 1 |
| 3.5-05 | Règles de prémunition pour le conseil | 0,5 |

**Frais et rentabilité avant frais (0,5 pt).**
- Frais du mandat : 25 200 × 1,50 % + 16 800 × 0,50 % = 378 + 84 = **462 k€** par an (1,10 % de l'actif).
- Gestion indicielle : 42 000 × 0,20 % = **84 k€** par an. Économie : **378 k€ par an**, soit 0,90 point de rentabilité chaque année (environ 3 M€ sur l'horizon de huit ans, sans capitalisation, calcul facultatif).
- Fonds actions avant frais : 8,00 % + 1,50 % = **9,50 %**, exactement la rentabilité exigée par le MEDAF compte tenu de son bêta (question 3.3). Avant frais, le gérant n'a rien obtenu de plus que la rémunération du risque systématique qu'il a pris ; les frais expliquent à eux seuls l'écart de 1,50 point. Un fonds indiciel aurait rapporté 9,00 % − 0,20 % = 8,80 %.

**Efficience informationnelle (0,5 pt).** Selon Fama (1970), un marché est efficient si les prix reflètent à tout instant toute l'information disponible. La forme faible porte sur les prix passés, la forme semi-forte sur toute l'information publique, la forme forte sur toute l'information, y compris privée. Sur un marché efficient au sens semi-fort, ce qu'est raisonnablement le marché des grandes actions de la zone euro, très suivies par les analystes, aucun gérant ne peut, avec l'information publique, obtenir durablement une rentabilité supérieure à celle que justifie son risque : la gestion active coûte des frais sans garantir de surcroît de rentabilité, et le choix du moment d'achat ou de vente a un rôle limité.

**Conclusion (0,5 pt).** Les résultats du mandat confirment cette lecture : rentabilité avant frais égale à celle qu'exige le MEDAF, rentabilité nette inférieure à l'indice, ratios de Sharpe et de Treynor inférieurs à ceux de l'indice, risque à 94,65 % systématique (le fonds suit presque l'indice tout en facturant une gestion active). Il est recommandé de **passer à une gestion indicielle** pour l'essentiel de la réserve, en conservant l'allocation 60 / 40 : la coopérative garde le même risque systématique et économise 378 k€ par an. Limites : cinq années ne suffisent pas à juger un gérant ; l'efficience est discutable pour certains compartiments (petites valeurs, obligations peu liquides), où une gestion active peut se justifier ; un fonds indiciel suit l'indice dans les baisses et n'offre aucune protection en 2022.

**Biais comportementaux (1 pt).** Deux biais pertinents, appliqués au cas, suffisent (finance comportementale, Kahneman et Tversky, 1973) :
- **Excès de confiance et extrapolation (représentativité)** — le vice-président : deux années favorables (2025 et 2026) suffisent à conclure que les « choix de valeurs commencent à payer ». Il néglige les trois années précédentes (− 0,1 point, − 3,6 points et − 7,3 points par rapport à l'indice) et le fait qu'avec un bêta de 1,10, le fonds fait mécaniquement mieux que l'indice quand le marché monte fortement. Sur cinq ans, le fonds a gagné 38,51 % contre 47,05 % pour l'indice (calcul facultatif).
- **Préférence pour le familier, renforcée par l'excès de confiance** — l'administrateur : « nous connaissons le lait et l'agroalimentaire mieux que n'importe quel gérant ». Connaître un secteur comme industriel ne donne pas d'avantage pour en évaluer les actions, dont les cours intègrent déjà l'information publique. Ce biais conduit à concentrer la réserve sur le risque que la coopérative porte déjà (question 3.3), sur la foi des 12 % des trois dernières années (extrapolation).
- **Effet de disposition et choix du moment** — le trésorier : vendre la moitié du fonds actions « pour mettre ce gain à l'abri », c'est raisonner sur la plus-value acquise (près de 40 %) plutôt que sur les perspectives : les investisseurs tendent à vendre trop tôt leurs placements gagnants (Shefrin et Statman, 1985). Racheter « quand le marché aura baissé » suppose de prévoir les cours, ce que l'efficience rend illusoire ; cette vente ramènerait en outre les actions à 30 % du portefeuille (12 600 k€ sur 42 000 k€), en dehors de l’allocation retenue.
- La présidente, enfin, exprime une aversion aux pertes compréhensible ; elle est ici traduite en règle explicite (contrainte de 4 000 k€), ce qui la rend légitime.

**Règles de prémunition (0,5 pt).** Fixer par écrit, dans la charte de placement, l'allocation cible et la règle de rééquilibrage annuel, pour éviter les décisions d'opportunité ; mesurer la performance sur longue période, après frais et par rapport à un indice de référence ajusté du risque (ratios de Sharpe et de Treynor), et non sur les dernières années ; interdire ou plafonner les placements dans le secteur de la coopérative ; confier l'examen des placements à un comité financier comprenant un expert indépendant, qui présente au conseil des analyses chiffrées avant toute décision.

**Réponses tolérées** : une réponse courte obtient tous les points si elle est reliée aux chiffres du cas (les développements ci-dessus vont au-delà de l'attendu) ; autres biais pertinents s'ils sont reliés à un extrait (ancrage sur le gain de 40 % ou sur les 12 %, biais de confirmation, illusion de contrôle, comptabilité mentale) ; recommandation d'une gestion mixte (cœur indiciel et petite part active) si elle est argumentée par les frais et l'efficience ; efficience présentée sans les trois formes si son implication pour la gestion active est correcte.

**Erreurs fréquentes**
- Présenter les biais comme une liste de cours, sans les relier aux extraits ni aux chiffres du mandat (orientation « présentation psychologique générale », exclue par le programme).
- Attribuer à Fama la finance comportementale, ou commettre une erreur d'attribution signalée dans F99 et F10 (Kahneman a reçu le prix Nobel en 2002 ; son coauteur, décédé en 1996, ne l'a pas reçu).
- Conclure que la gestion indicielle supprime le risque : elle supprime le risque de mauvaise gestion et une partie des frais, pas le risque de marché.
- `JUR-T14` — efficience évoquée sans en tirer la conséquence pour le choix du mode de gestion.
- `JUR-T06` — réponse sans auteur ni théorie.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 73-77 | efficience (trois formes, rôle limité du timing) ; finance comportementale ; rentabilité espérée et bêta ; portefeuille de deux titres, corrélation fournie, Sharpe et Treynor ; vérifications statistiques des théories et optimisation de portefeuille exclues | [V] | F06 § 0, 3 et 4 ; `perimetre_ue2.yaml` |
| Markowitz (1952) | diversification, rôle de la corrélation | [V programme 5.3] | F10 § 2 |
| MEDAF (Sharpe, 1964) ; ratio de Sharpe (1966) ; ratio de Treynor (1965) | seul le risque systématique est rémunéré ; mesures de performance | [S] | F10 § 2 ; F02 |
| Gordon et Shapiro | rentabilité espérée d'une action à croissance constante du dividende | [V programme 5.2, sans année] | F10 § 2 |
| Fama (1970) | efficience informationnelle, trois formes | [V programme 5.1] | F10 § 1 ; F06 § 3 |
| Kahneman et Tversky (1973) | heuristiques et biais, représentativité | [V programme 5.1 pour la référence ; S pour le contenu] | F10 § 1 ; F06 § 4 |
| Shefrin et Statman (1985), facultatif | effet de disposition | [S] | F10 § 1 ; F06 § 4.2 |
| Préférence pour le familier | biais décrit sans attribution d'auteur | [S] | — |
| Taux sans risque 4 % et prime de risque du marché 5 % | hypothèses d'énoncé, plausibles fin 2026 | [S] | F11 § 1 et 2 |
