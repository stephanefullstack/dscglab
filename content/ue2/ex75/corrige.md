# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 75 — Dossier 3 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F02 coût du capital, F06 marchés et finance comportementale, F07 risques de taux, climat et matières premières, F10 auteurs et théories, F11 données de marché, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (VAN, TRI, indice de profitabilité, délais de récupération et flux actualisés de la plate-forme ; VAN des six combinaisons, espérance, variance, écart-type, coefficient de variation et probabilité d'une VAN négative ; indemnités et pertes nettes des deux crues ; coûts actuariels avant et après IS des trois financements ; FRA dans trois scénarios et différentiels actualisés ; nombre de contrats, valeur du point, taux implicite et résultat des contrats à terme sur l'Euribor ; rentabilité, écart-type, bêta et décomposition du risque du portefeuille ; barème, liste noire, hors-programme ; chiffre d'affaires et EBITDA de la plate-forme, BFR, valeur résiduelle, coût espéré des crues, couverture du cuivre, ratio de dette pro forma, coût net des contrats sur 91 jours et produit de cession vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VAN centrale erronée à la question 3.1, reprise dans les six combinaisons de la question 3.2, ou un montant minimal de cession erroné à la question 3.5, repris dans la comparaison des options de cession de la question 3.7).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Flux de la plate-forme, VAN, TRI, indice de profitabilité, délai de récupération actualisé | `7.1.a` Évaluer et classer des projets en milieu certain | 2,5 |
| 3.2 Six combinaisons du tonnage et du prix des métaux, espérance, écart-type, probabilité d'une VAN négative | `7.1.b` Évaluer et classer des projets en milieu incertain | 2 |
| 3.3 Crues : indemnités, coût espéré et perte maximale, assurance, réassurance et prévention | `6.4.a` Sensibiliser aux instruments de couverture des risques physiques et financiers liés au changement climatique et à la raréfaction des ressources naturelles | 1 |
| 3.4 Vente de contrats à terme sur le cuivre, prix net, risque de base, couverture de prix et assurance de dommages | `6.4.a` Sensibiliser aux instruments de couverture des risques physiques et financiers liés au changement climatique et à la raréfaction des ressources naturelles | 1,5 |
| 3.5 Coûts actuariels des trois financements, ratio de dette pro forma, cession minimale, structure financière, recommandation | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `7.2.b` Estimer l'impact du choix d'une source de financement sur la structure financière et identifier ses déterminants | 3,5 |
| 3.6 FRA et contrats à terme sur l'Euribor 3 mois dans trois scénarios, comparaison | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux ; `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) | 2,5 |
| 3.7 Portefeuille hérité : rentabilité et risque, corrélation, risques systématique et spécifique, produit de cession et ratio | `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres ; `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) ; `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique | 2,5 |
| 3.8 Proposition de la directrice financière : effet de disposition, efficience au sens faible, recommandation | `5.1.d` Maîtriser les grands enseignements de la finance comportementale ; `5.1.c` Maîtriser les grands enseignements de l'efficience informationnelle des marchés (Fama, 1970) | 1,5 |
| **Total** | | **17** |

Répartition par sous-partie : 7.1 : 4,5 points (7.1.a 2,5, 7.1.b 2) ; 6.4 : 2,5 points (6.4.a) ; 7.2 : 3,5 points (7.2.a 2, 7.2.b 1,5) ; 6.2 : 2,5 points (6.2.b 1,5, 6.2.c 1) ; 5.3 : 2,5 points (5.3.a 0,5, 5.3.b 1, 5.3.c 1) ; 5.1 : 1,5 point (5.1.c 0,5, 5.1.d 1). Part du calcul : environ 11 points (3.1-01 à 3.1-04, 3.2-01 à 3.2-03, 3.3-01, 3.4-01, 3.4-02, 3.5-01 à 3.5-03, 3.5-05, 3.6-01 à 3.6-04, 3.7-01, 3.7-02, 3.7-04, 3.7-05). Part de l'analyse : environ 6 points. Les questions 3.3, 3.4 et 3.6 se traitent sans les résultats des questions précédentes : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 Flux de la plate-forme et critères en avenir certain (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Chiffre d'affaires **8,80 M€** en 2028 (redevances 7,04 ; granulats 0,32 ; métaux 1,44) et **11,00 M€** en année pleine (8,80 ; 0,40 ; 1,80) ; EBITDA **2,20** et **3,60 M€** ; amortissements 1,40 M€ ; résultat d'exploitation **0,80** et **2,20 M€** | 0,5 |
| 3.1-02 | Date 0 : 15,60 + BFR 0,88 = **− 16,48 M€** ; flux 2028 : 0,80 − 0,20 + 1,40 − 0,22 = **1,78** ; 2029 à 2034 : 2,20 − 0,55 + 1,40 = **3,05** ; 2035 : 3,05 + valeur résiduelle nette 4,85 (5,00 − 25 % × (5,00 − 4,40)) + BFR récupéré 1,10 = **9,00 M€** | 0,5 |
| 3.1-03 | VAN à 7,50 % = 20,02 − 16,48 = **3,54 M€** ; indice de profitabilité = 20,02 / 16,48 = **1,21** | 0,5 |
| 3.1-04 | TRI **11,91 %** (VAN 0,65 à 11 % et − 0,06 à 12 % ; interpolation 11,92 %) ; délai de récupération actualisé **7,30 ans** (cumul − 1,51 à la fin de 2034, 1,51 / 5,05 = 0,30) | 0,5 |
| 3.1-05 | Conclusion : projet créateur de valeur au taux du groupe (VAN > 0, TRI supérieur de 4,4 points au CMPC, 1 € investi en rapporte 1,21 en valeur actuelle) ; mais récupération tardive, dans la dernière année, qui dépend de la valeur du terrain et du bâtiment et du BFR récupéré (5,95 M€ de flux de fin) ; flux hors crues ; risque à étudier par scénarios (question 3.2) | 0,5 |

**Compte d'exploitation de la plate-forme (item 3.1-01).** Pour 100 tonnes reçues : 25 t de granulats de remblai et 5 t de métaux.

| M€ | 2028 | Chaque année de 2029 à 2035 |
|---|---:|---:|
| Tonnes reçues | 64 000 | 80 000 |
| Redevances (110 € × tonnes) | 7,04 | 8,80 |
| Granulats de remblai (25 % × tonnes × 20 €) | 0,32 | 0,40 |
| Métaux (5 % × tonnes × 450 €) | 1,44 | 1,80 |
| **Chiffre d'affaires** | **8,80** | **11,00** |
| Charges variables (50 € × tonnes) | − 3,20 | − 4,00 |
| Charges fixes décaissées | − 3,40 | − 3,40 |
| **EBITDA** | **2,20** | **3,60** |
| Amortissements (1,60 / 8 + 4,00 / 20 + 8,00 / 8) | − 1,40 | − 1,40 |
| **Résultat d'exploitation** | **0,80** | **2,20** |
| Impôt (25 %) | − 0,20 | − 0,55 |

**Flux nets de trésorerie (item 3.1-02).** BFR = 10 % du chiffre d'affaires de l'année, constitué au début de l'année : 0,88 M€ à la date 0 pour 2028, 1,10 M€ à partir de 2029, soit une augmentation de 0,22 M€ à la fin de 2028, et 1,10 M€ récupérés à la fin de 2035. Valeur nette comptable du terrain et du bâtiment à la fin de 2035 : 2,00 + 4,00 − 8 × 0,20 = 4,40 M€ ; plus-value 0,60 M€, impôt 0,15 M€, valeur résiduelle nette **4,85 M€**.

| M€ | Date 0 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Investissement | − 15,60 | | | | | | | | |
| Résultat d'exploitation après impôt | | 0,60 | 1,65 | 1,65 | 1,65 | 1,65 | 1,65 | 1,65 | 1,65 |
| + amortissements | | 1,40 | 1,40 | 1,40 | 1,40 | 1,40 | 1,40 | 1,40 | 1,40 |
| − augmentation du BFR / + récupération | − 0,88 | − 0,22 | | | | | | | + 1,10 |
| + valeur résiduelle nette | | | | | | | | | + 4,85 |
| **Flux net** | **− 16,48** | **1,78** | **3,05** | **3,05** | **3,05** | **3,05** | **3,05** | **3,05** | **9,00** |
| Flux actualisé à 7,50 % | | 1,66 | 2,64 | 2,46 | 2,28 | 2,12 | 1,98 | 1,84 | 5,05 |
| Cumul des flux actualisés (sans arrondi intermédiaire) | − 16,48 | − 14,82 | − 12,18 | − 9,73 | − 7,45 | − 5,32 | − 3,35 | − 1,51 | + 3,54 |

**Critères (items 3.1-03 et 3.1-04).**
- Somme des flux actualisés (sans arrondi intermédiaire) : **20,02 M€** ; VAN = 20,02 − 16,48 = **3,54 M€** (la somme des flux actualisés arrondis du tableau donne 3,55, toléré).
- Indice de profitabilité = 20,02 / 16,48 = **1,21**.
- TRI : la VAN vaut 0,65 M€ à 11 % et − 0,06 M€ à 12 % ; par interpolation, 11 % + 0,65 / 0,71 × 1 % = 11,92 % ; valeur exacte **11,91 %**.
- Délai de récupération actualisé : le cumul passe de − 1,51 à + 3,54 en 2035 : 7 + 1,51 / 5,05 = **7,30 ans** (délai simple, non demandé : 5,82 ans).

**Conclusion (item 3.1-05).** Au CMPC de 7,50 % retenu par DORVAART pour ses activités françaises, la plate-forme crée de la valeur : VAN de 3,54 M€, TRI de 11,91 %, indice de 1,21. Le taux est un CMPC parce que les flux sont des flux d'exploitation, avant tout financement : ils rémunèrent ensemble les actionnaires et les prêteurs ; il convient si la plate-forme a le risque du métier existant. Deux limites : (1) l'investissement n'est récupéré, en valeur actuelle, qu'au cours de la huitième année, grâce aux 5,95 M€ de la fin de 2035 (valeur du site et BFR), dont l'estimation est incertaine ; sans valeur résiduelle ni BFR récupéré, la VAN tomberait à 3,54 − 5,95 × 0,5607 = 0,20 M€ ; (2) les flux reposent sur des hypothèses centrales de tonnage et de prix des métaux et ne comptent pas le coût des crues : le risque doit être mesuré (questions 3.2 et 3.3).

**Réponses tolérées** : VAN de 3,55 M€ par la somme des flux actualisés arrondis ; TRI de 11,92 % par interpolation ; BFR constitué en fin d'année (première constitution en 2028) si l'hypothèse est écrite et appliquée de façon cohérente ; délai de récupération actualisé de 7,29 à 7,31 ans.

**Erreurs fréquentes**
- Retrancher le niveau du BFR chaque année au lieu de sa variation, ou oublier de le récupérer en 2035 (`JUR-E01`).
- Oublier l'impôt sur la plus-value du site, ou amortir le terrain.
- Actualiser au taux de la dette ou à un coût des fonds propres alors que les flux sont avant financement (`JUR-T14`).
- Déduire les frais financiers des flux du projet, alors que le financement est apprécié à part (question 3.5) (`JUR-T04`).

**Références** : F01 § 4 (VAN, TRI, indice de profitabilité, délai de récupération actualisé, construction des flux) et § 8 (arrondis en cascade) [V programme 7.1 ; S] ; programme 7.1.a, guide p. 80-81 (critères en milieu certain ; flux ou éléments permettant de les construire fournis) [V] ; F02 § 5 (CMPC, taux d'actualisation de flux d'exploitation) [S].

---

### 3.2 VAN probabilisée : six combinaisons de deux variables indépendantes (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Probabilités : 0,30 × 0,50 = **15 %**, 15 %, **25 %**, 25 %, **10 %**, 10 % (total 100 %) ; VAN = 3,54 + écart annuel × 5,8573 : faible-bas **− 2,26**, faible-haut **0,55**, central-bas **2,13**, central-haut **4,95**, fort-bas **5,65**, fort-haut **8,46 M€** | 0,5 |
| 3.2-02 | Espérance de la VAN **2,92 M€** (= 3,54 − 0,105 × 5,8573), inférieure à la VAN centrale | 0,5 |
| 3.2-03 | Variance **9,87** ; écart-type **3,14 M€** ; coefficient de variation **1,08** (1,07 sans arrondi intermédiaire, toléré) ; probabilité d'une VAN négative **15 %** (faible-bas) | 0,5 |
| 3.2-04 | Commentaire : projet en moyenne créateur de valeur mais risqué (écart-type supérieur à l'espérance, 15 % de probabilité de détruire 2,26 M€) ; le tonnage pèse plus que les métaux (écarts plus grands et asymétriques, tonnage faible plus probable que fort) ; la VAN centrale surestime l'espérance ; limites (deux variables, niveaux discrets, indépendance supposée, probabilités subjectives) ; leviers : contrats d'apport pluriannuels avec les entreprises de démolition, montée en charge progressive, couverture du prix des métaux (question 3.4) | 0,5 |

**Combinaisons (item 3.2-01).** Les écarts de flux sont constants de 2028 à 2035 et s'additionnent ; l'investissement et la valeur résiduelle ne changent pas. La VAN d'une combinaison est donc la VAN centrale augmentée de la valeur actuelle de l'écart annuel sur huit ans : facteur d'annuité (1 − 1,075^−8) / 0,075 = **5,8573**.

| Tonnage | Métaux | Probabilité | Écart annuel (M€) | VAN (M€) |
|---|---|---:|---:|---:|
| Faible (30 %) | Bas (50 %) | 15 % | − 0,99 | **− 2,26** |
| Faible | Haut (50 %) | 15 % | − 0,51 | **0,55** |
| Central (50 %) | Bas | 25 % | − 0,24 | **2,13** |
| Central | Haut | 25 % | + 0,24 | **4,95** |
| Fort (20 %) | Bas | 10 % | + 0,36 | **5,65** |
| Fort | Haut | 10 % | + 0,84 | **8,46** |

**Espérance, écart-type, probabilité (items 3.2-02 et 3.2-03).**
- E(VAN) = 0,15 × (− 2,26) + 0,15 × 0,55 + 0,25 × 2,13 + 0,25 × 4,95 + 0,10 × 5,65 + 0,10 × 8,46 = **2,92 M€**. Contrôle : l'écart annuel espéré vaut 0,30 × (− 0,75) + 0,20 × 0,60 = − 0,105 M€ pour le tonnage et 0 pour les métaux, d'où 3,54 − 0,105 × 5,8573 = 2,92 M€.
- Variance = Σ p × (VAN − 2,92)² = 0,15 × 5,18² + 0,15 × 2,37² + 0,25 × 0,79² + 0,25 × 2,03² + 0,10 × 2,73² + 0,10 × 5,54² ≈ **9,87** ; écart-type **3,14 M€** ; coefficient de variation 3,14 / 2,92 = **1,08** avec les résultats arrondis (1,07 sans arrondi intermédiaire).
- Probabilité d'une VAN négative, lue sur les scénarios : seule la combinaison faible-bas est négative, **15 %**.

**Commentaire (item 3.2-04).** Le projet reste créateur de valeur en espérance (2,92 M€), mais l'espérance est inférieure de 0,62 M€ à la VAN centrale : le tonnage faible est plus probable que le tonnage fort et ses écarts sont plus grands, ce que les hypothèses centrales de la direction ne montrent pas. L'écart-type (3,14 M€) dépasse l'espérance : la VAN va de − 2,26 à + 8,46 M€, et le projet détruit de la valeur dans 15 % des cas, quand le bâtiment recule et que les métaux sont bas en même temps. Le tonnage est la variable décisive (écart de 1,35 M€ par an entre faible et fort, contre 0,48 M€ pour les métaux) : sécuriser les apports (contrats pluriannuels avec les entreprises de démolition, redevances révisables) compte plus que couvrir les métaux. Limites : deux variables seulement, chacune réduite à deux ou trois niveaux ; indépendance supposée alors qu'une crise du bâtiment peut faire baisser à la fois le tonnage et les prix des matériaux ; probabilités estimées par la direction ; un écart-type ne dit rien de la valeur de la perte pour DORVAART, groupe coté dont les actionnaires sont diversifiés (seul le risque non diversifiable devrait être rémunéré).

**Réponses tolérées** : VAN de chaque combinaison calculée en actualisant les huit flux (mêmes résultats au centième près) ; variance de 9,86 calculée sur les VAN non arrondies ; coefficient de variation de 1,07 calculé sans arrondi intermédiaire ; écart-type de 3,13 à 3,15 M€ ; coefficient de variation présenté comme écart-type / espérance en % (107 %).

**Erreurs fréquentes**
- Additionner les probabilités des deux variables au lieu de les multiplier, ou étudier les deux variables séparément sans les combiner.
- Diviser la variance par 6 ou par 5 au lieu de la pondérer par les probabilités.
- Supposer une distribution continue de la VAN pour calculer la probabilité d'une VAN négative : elle se lit sur les scénarios.
- Confondre l'espérance de la VAN avec la VAN centrale de la question 3.1 (`JUR-T12`).

**Références** : F01 § 5 (milieu probabilisable : espérance, variance et écart-type de la VAN pondérés par les probabilités) [S] ; programme 7.1.b, guide p. 81 (analyse de scénarios, espérance et écart-type de la VAN ; probabilités et flux fournis) [V].

---

### 3.3 Crues de la Seine : assurance, réassurance et prévention (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Crue moyenne : perte 1,20 M€, indemnité 1,20 − 0,30 = **0,90**, reste **0,30 M€** (franchise) ; crue majeure : perte 6,00 M€, indemnité plafonnée à **4,00**, reste **2,00 M€** ; coût annuel espéré sans assurance 0,10 × 1,20 + 0,02 × 6,00 = **0,24 M€** ; avec l'assurance 0,20 + 0,10 × 0,30 + 0,02 × 2,00 = **0,27 M€** ; perte maximale d'une année **6,00 M€** sans assurance, 0,20 + 2,00 = **2,20 M€** avec | 0,5 |
| 3.3-02 | Analyse : l'assurance coûte plus qu'elle ne rapporte en moyenne (prime 0,20 contre 0,17 d'indemnité espérée) mais transfère la perte rare et lourde (6,00 → 2,20 M€) ; restent à QUERMANDE la franchise, la part au-delà du plafond, les pertes non assurées (clients partis à la concurrence, retard de mise en service) et le risque de contrepartie ; la réassurance protège l'assureur, pas QUERMANDE, qui n'a pas de lien avec le réassureur ; la prévention réduit la probabilité et le coût des sinistres (surélévation, batardeaux, repli vers Elbeuf), abaisse la franchise à 0,15 M€, et vient avant l'assurance, qui ne traite que le risque résiduel | 0,5 |

**Indemnités et coûts espérés (item 3.3-01).**

| M€ | Crue moyenne (10 %) | Crue majeure (2 %) |
|---|---:|---:|
| Perte (dégâts + marge perdue) | 1,20 | 6,00 |
| Indemnité = min(4,00 ; perte − 0,30) | 0,90 | 4,00 |
| Perte restant à la charge de QUERMANDE | 0,30 | 2,00 |

| M€ | Sans assurance | Avec l'assurance |
|---|---:|---:|
| Coût annuel espéré | 0,10 × 1,20 + 0,02 × 6,00 = **0,24** | 0,20 + 0,10 × 0,30 + 0,02 × 2,00 = **0,27** |
| Année sans crue | 0 | 0,20 |
| Perte maximale d'une année (crue majeure) | **6,00** | 0,20 + 2,00 = **2,20** |

**Analyse (item 3.3-02).** L'indemnité espérée vaut 0,10 × 0,90 + 0,02 × 4,00 = 0,17 M€ par an, pour une prime de 0,20 M€ : l'assurance coûte en moyenne 0,03 M€ de plus qu'elle ne rapporte (frais et rémunération de l'assureur). Elle n'est pas un placement : elle sert à transformer une perte possible de 6,00 M€, qui pèserait près de 40 % de l'EBITDA consolidé de 2026 et mettrait en cause le ratio de dette du groupe, en un coût certain et une perte maximale de 2,20 M€.
- *Ce qui est transféré* : la part de chaque sinistre comprise entre la franchise et le plafond, dégâts et marge perdue.
- *Ce qui reste à QUERMANDE* : la franchise (0,30 M€ par crue) ; la part de la crue majeure au-delà du plafond (2,00 M€) ; les pertes que le contrat ne couvre pas (clients qui prennent l'habitude d'aller chez un concurrent, image auprès des donneurs d'ordre) ; le risque que l'assureur ne paie pas ou tarde.
- *Réassurance* : DORNEVAL Assurances cède à un réassureur la part des sinistres qui dépasse 1,00 M€ ; elle protège ainsi ses fonds propres contre une crue qui toucherait en même temps de nombreux assurés de la vallée et renforce sa capacité à payer. QUERMANDE n'a aucun droit envers le réassureur : sa couverture ne change pas, mais le risque de contrepartie sur son assureur diminue.
- *Prévention* : surélever les équipements, poser des batardeaux et organiser le repli vers Elbeuf réduit les dégâts et la durée de l'arrêt, donc la perte avant toute assurance ; l'assureur ramènerait la franchise à 0,15 M€ (coût espéré avec l'assurance : 0,20 + 0,10 × 0,15 + 0,02 × 2,00 = 0,255 M€, non exigé). Dans une politique de gestion des risques, on réduit d'abord le risque (prévention), on assure ensuite le risque résiduel grave, et l'on garde les petits sinistres fréquents. Le risque de crue est un risque physique lié au climat, appelé à s'aggraver : il devrait figurer dans les risques présentés à DORVAART et dans le choix du site lui-même.

**Réponses tolérées** : coût espéré avec l'assurance présenté comme prime + franchises espérées + dépassements espérés (0,20 + 0,03 + 0,04) ; mention du coût de la prévention à mettre en regard de la baisse de franchise, sans chiffrage ; analyse après impôt si elle est cohérente.

**Erreurs fréquentes**
- Appliquer le plafond à la perte brute (indemnité de 4,00 − 0,30 = 3,70 M€) au lieu de la perte nette de franchise plafonnée.
- Conclure que l'assurance est inutile parce que son coût espéré dépasse celui de l'absence d'assurance, sans parler de la perte maximale (`JUR-T12`).
- Croire que la réassurance indemnise directement QUERMANDE.
- Développer les règles de l'indemnisation des catastrophes naturelles ou de l'urbanisme en zone inondable : les conditions sont des faits d'énoncé.

**Références** : F07 § 5 (risques physiques, assurance et réassurance, franchise et plafond) [V guide p. 80 ; S] ; programme 6.4.a, guide p. 79-80 (rôle de l'assurance et de la réassurance dans une politique globale de gestion des risques) [V].

---

### 3.4 Couverture du prix du cuivre par des contrats à terme (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Vente de 250 / 25 = **10 contrats** à 8 400 € ; dépôt 10 × 5 000 = **50 000 €** ; résultat sur les contrats : baisse (8 400 − 7 260) × 250 = **+ 285 000 €**, hausse (8 400 − 9 340) × 250 = **− 235 000 €** | 0,5 |
| 3.4-02 | Recette de la vente : 1 650 000 € et 2 175 000 € ; recette totale **1 935 000 €** et **1 940 000 €** ; prix net **7 740 €** et **7 760 € par tonne**, contre **6 600 €** et **8 700 €** sans couverture | 0,5 |
| 3.4-03 | Risque de base : le prix net = cours à terme de vente − décote + base au rachat (− 60 ou − 40 €) ; la base n'est pas nulle (rachat deux jours avant l'échéance, cuivre de récupération différent du contrat, décote qui peut changer) ; appels de marge à financer en cas de hausse (235 000 € versés avant la vente) ; couverture de prix ferme, sans prime, qui renonce au gain d'une hausse et ne couvre pas la quantité (si une crue empêche de produire, la position devient spéculative), alors que l'assurance indemnise une perte de dommages contre une prime, sans renoncer à rien | 0,5 |

**Calculs (items 3.4-01 et 3.4-02).** QUERMANDE Métaux détient le cuivre à vendre : elle craint une baisse et vend des contrats à terme (couverture vendeuse).

| € | Baisse | Hausse |
|---|---:|---:|
| Vente du cuivre : 250 × (comptant − 600) | 250 × 6 600 = 1 650 000 | 250 × 8 700 = 2 175 000 |
| Résultat sur les 10 contrats : 250 × (8 400 − terme de rachat) | + 285 000 | − 235 000 |
| **Recette totale** | **1 935 000** | **1 940 000** |
| **Prix net par tonne** | **7 740** | **7 760** |
| Prix par tonne sans couverture | 6 600 | 8 700 |
| Base au rachat (comptant − terme) | − 60 | − 40 |

Dépôt de garantie : 10 × 5 000 = **50 000 €**, versé dès la vente des contrats et restitué au dénouement.

**Analyse (item 3.4-03).**
- *Risque de base.* Le prix obtenu n'est pas exactement le cours à terme de 8 400 € diminué de la décote (7 800 €) : il vaut 8 400 − 600 + base au rachat, soit 7 740 € ou 7 760 €. La base (− 150 € le 24 mai 2027) se resserre à l'approche de l'échéance, sans s'annuler, parce que les contrats sont rachetés avant leur dernière cotation. Le cuivre de récupération n'est pas le cuivre du contrat : si la décote de qualité changeait, l'écart s'ajouterait au risque de base. La couverture ramène l'incertitude de 2 100 € par tonne (6 600 à 8 700) à 20 € (7 740 à 7 760).
- *Trésorerie.* Les appels de marge sont quotidiens : en cas de hausse, QUERMANDE Métaux verse 235 000 € avant de vendre son cuivre plus cher ; il faut prévoir ce financement avec DORVAART Treasury.
- *Couverture de prix et assurance de dommages.* Les contrats à terme fixent le prix, dans les deux sens : ils protègent contre la baisse et font renoncer au gain de la hausse (8 700 € perdus contre 7 760 €), sans prime ; ils supposent que les 250 tonnes existent. L'assurance de la question 3.3 indemnise une perte matérielle et une perte de marge quand un sinistre survient, contre une prime payée dans tous les cas, sans faire renoncer à un gain. Elles ne se substituent pas : si une crue détruisait le stock ou arrêtait le tri, QUERMANDE Métaux resterait vendeuse de contrats sans cuivre à livrer, exposée à une hausse du cours. Les dérivés sur matières premières sont des instruments de marché ; l'assurance mutualise des sinistres ; les deux relèvent d'une même politique de gestion des risques.

**Réponses tolérées** : prix net présenté comme 8 400 − 600 + base (7 740 et 7 760 €) sans détailler les recettes ; mention d'une option de vente sur le cuivre (prime à payer, gain d'une hausse conservé) comme alternative, sans chiffrage ; analyse du risque de base comme risque de corrélation entre le cuivre de récupération et le contrat.

**Erreurs fréquentes**
- Acheter des contrats alors que QUERMANDE Métaux est vendeuse de cuivre.
- Calculer le résultat sur les contrats avec le cours au comptant au lieu du cours à terme de rachat.
- Présenter la perte sur contrats de la hausse comme un échec de la couverture : la recette totale est presque la même (`JUR-T12`).
- Oublier la décote de 600 € dans la recette de la vente.

**Références** : F07 § 5 (dérivés sur matières premières, couverture vendeuse, base, appels de marge) et § 6 point 8 (couverture de prix et couverture de volume) [S] ; programme 6.4.a, guide p. 80 (dérivés de couverture sur les prix des matières premières ; tous les paramètres fournis) [V].

---

### 3.5 Coût des financements, ratio de dette du groupe et structure financière (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Prêt de DORVAART Treasury : in fine, sans frais, coût actuariel = taux nominal **4,40 %** avant IS ; **3,30 %** après IS (4,40 % × 0,75) | 0,5 |
| 3.5-02 | Prêt de la Banque HALBRESSE : reçu 12,00 − 0,12 = 11,88 M€ ; annuités 1,974 ; 1,915 ; … ; 1,559 M€ (intérêts à 3,95 % sur le capital dû, amortissement 1,50) ; coût **4,20 %** avant IS (interpolation entre 4 % et 4,5 % : 4,21 %) ; après IS **3,15 %** (approximation 4,20 % × 0,75, ou taux des flux nets d'impôt : 11,91 ; − 1,856 ; …) | 0,5 |
| 3.5-03 | Crédit-bail : 8,00 = 1,18 × facteur d'annuité + 0,40 actualisé → **4,69 %** avant IS ; après IS, flux annuel − (1,18 × 0,75 + 0,25) = − 1,135, option 0,40 en 2035 → **3,81 %** ; l'approximation 4,69 % × 0,75 = 3,52 % est fausse, car QUERMANDE perd l'économie d'impôt sur l'amortissement | 0,5 |
| 3.5-04 | Comparaison des coûts : au taux du jour, prêt bancaire le moins cher (3,15 %), mais à taux variable (chaque hausse de 0,10 point de l'Euribor ajoute environ 0,08 point après impôt) et assorti d'une lettre de soutien ; or le FRA (2,95 %) et les contrats à terme (2,92 %) montrent que le marché attend un Euribor plus élevé : à ce niveau, le prêt bancaire coûterait environ 4,5 % avant IS (3,35 à 3,37 % après), plus que le prêt du groupe ; son avantage de coût n'est pas acquis ; prêt du groupe à taux fixe (3,30 %), in fine ; crédit-bail le plus cher (3,81 %), limité à la chaîne de tri | 0,5 |
| 3.5-05 | Ratio de DORVAART avant l'opération 21,50 / 15,40 = **1,40** ; pro forma sans cession (21,50 + 16,48) / (15,40 + 3,60) = 37,98 / 19,00 = **2,00** > 1,90, pour les trois solutions ; cession minimale 37,98 − 1,90 × 19,00 = **1,88 M€** ; dette financière nette retenue par DORVAART / capitaux propres consolidés **41,35 %** avant, **73,04 %** pro forma sans cession | 0,5 |
| 3.5-06 | Effets sur la structure : le choix de la dette ne change ni le ratio ni le rapport aux capitaux propres (l'investissement est financé par endettement ou par la trésorerie, et le crédit-bail compte comme une dette) ; il change l'échéancier et la liquidité (service 2028 : 0,53 M€ pour le prêt du groupe, 1,97 pour le prêt bancaire, 1,36 pour la solution 3, pour un flux de 1,78 M€ la première année), le risque de taux, la dépendance au groupe (refinancement de 12,00 M€ en 2035) et les garanties (lettre de soutien, propriété de la chaîne) ; remarque valorisée : le ratio du groupe rapporte une dette sans dettes locatives à un EBITDA qui ne supporte plus les loyers des terrains, il flatte donc la situation ; la plate-forme, sur un terrain acheté, n'ajoute pas de loyer | 0,5 |
| 3.5-07 | Recommandation argumentée, dans tous les cas avec la cession d'au moins 1,88 M€ d'actifs, soit le portefeuille (question 3.7) : soit le prêt du groupe (taux fixe, coût voisin du prêt bancaire aux taux anticipés, aucune garantie, service faible pendant la montée en charge, mais remboursement de 2035 à organiser), soit le prêt bancaire (amorti sur la durée de vie de la chaîne, diversification des prêteurs, mais taux variable à couvrir, question 3.6, et avantage de coût incertain) ; les deux recommandations sont également valables si elles sont justifiées ; le crédit-bail est écarté (plus cher, sans effet sur le ratio) | 0,5 |

**Prêt de DORVAART Treasury (item 3.5-01).** Sans frais, remboursé in fine, le prêt coûte son taux nominal : la valeur actuelle à 4,40 % des intérêts de 0,528 M€ et du capital de 12,00 M€ redonne 12,00 M€. Coût avant IS **4,40 %** ; les intérêts réduisent l'impôt de 25 %, d'où **3,30 %** après IS (flux de 12,00, puis − 0,396 par an et − 12,396 en 2035).

**Prêt de la Banque HALBRESSE (item 3.5-02).** Taux du scénario central : 2,65 % + 1,30 % = 3,95 % ; frais de 1 % × 12,00 = 0,12 M€ à la date 0 ; amortissement constant de 1,50 M€.

| M€ | Date 0 | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 | 2034 | 2035 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Capital dû au début | | 12,00 | 10,50 | 9,00 | 7,50 | 6,00 | 4,50 | 3,00 | 1,50 |
| Intérêts (3,95 %) | | 0,474 | 0,415 | 0,356 | 0,296 | 0,237 | 0,178 | 0,119 | 0,059 |
| Flux avant IS | + 11,88 | − 1,974 | − 1,915 | − 1,856 | − 1,796 | − 1,737 | − 1,678 | − 1,619 | − 1,559 |
| Flux après IS | + 11,91 | − 1,856 | − 1,811 | − 1,767 | − 1,722 | − 1,678 | − 1,633 | − 1,589 | − 1,544 |

11,88 M€ moins la valeur actuelle des décaissements (11,976 M€ à 4 %, donnée par l'annexe 3.8) vaut − 0,096 à 4 % et + 0,137 à 4,5 % : par interpolation, 4 % + 0,5 % × 0,096 / 0,233 = 4,21 % ; coût exact **4,20 %** avant IS. Après IS, les frais réduisent l'impôt à la date 0 (11,88 + 0,03 = 11,91) et les intérêts chaque année : **3,15 %**, égal à l'approximation 4,20 % × 0,75.

**Crédit-bail de la chaîne de tri (item 3.5-03).** QUERMANDE évite de payer 8,00 M€ à la date 0 ; elle paie huit loyers de 1,18 M€ puis l'option de 0,40 M€ en 2035.
- Avant IS : 8,00 = 1,18 × [1 − (1 + t)^−8] / t + 0,40 × (1 + t)^−8 ; l'écart vaut − 0,064 à 4,5 % et + 0,103 à 5 %, d'où **4,69 %**.
- Après IS : chaque loyer réduit l'impôt de 0,295 M€, mais QUERMANDE perd l'économie de 25 % × 1,00 = 0,25 M€ que lui aurait procurée l'amortissement de la chaîne achetée ; flux annuel − 1,18 + 0,295 + (− 0,25) = **− 1,135 M€**, et − 1,535 M€ en 2035. L'écart vaut − 0,106 à 3,5 % et + 0,066 à 4 %, d'où **3,81 %**. L'approximation 4,69 % × 0,75 = 3,52 % sous-estime le coût, parce que le crédit-bail prive QUERMANDE de l'économie d'impôt de l'amortissement.

**Comparaison des coûts (item 3.5-04).**

| Solution | Coût avant IS | Coût après IS | Taux | Remboursement | Garanties et conditions |
|---|---:|---:|---|---|---|
| 1. Prêt de DORVAART Treasury (12,00 M€) | 4,40 % | **3,30 %** | fixe | in fine en 2035 | aucune ; dépendance au groupe |
| 2. Prêt de la Banque HALBRESSE (12,00 M€) | 4,20 % | **3,15 %** | variable (Euribor 3 mois + 1,30 %) | constant, 1,50 M€ par an | frais de 1 % ; lettre de soutien de DORVAART |
| 3. Crédit-bail de la chaîne (8,00 M€) | 4,69 % | **3,81 %** | fixe (loyers) | loyers constants | propriété de la chaîne au bailleur jusqu'en 2035 ; bâtiment financé par le groupe à 3,30 % |

Le prêt bancaire est le moins cher au taux du jour, mais son coût suit l'Euribor : une hausse de 0,20 point de l'Euribor suffirait à le porter au niveau du prêt du groupe (environ 4,40 % avant IS). Or l'annexe 3.6 montre que le marché anticipe déjà une hausse d'environ 0,30 point : le FRA garantit 2,95 % et les contrats à terme cotent 97,08 (2,92 %), contre 2,65 % au comptant. Si l'Euribor se maintenait à ce niveau, le prêt bancaire coûterait avant IS **4,48 %** avec le taux implicite des contrats à terme, et **4,51 %** avec le taux garanti du FRA, soit 3,35 % à 3,37 % après IS (non exigé au centième : « environ 4,5 % » suffit) : plus que les 4,40 % du prêt du groupe. Le classement « prêt bancaire le moins cher » ne vaut donc qu'à Euribor constant au niveau du jour ; aux taux anticipés, les deux prêts coûtent à peu près la même chose, et le prêt du groupe a l'avantage du taux fixe. Le prêt du groupe est à taux fixe et sans frais. Le crédit-bail est le plus cher, même avec une option de faible montant. Du point de vue de DORVAART, le prêt du groupe a un coût différent : la marge de DORVAART Treasury reste dans le groupe, qui supporte son propre coût d'emprunt sur les marchés (non donné).

**Ratio de dette du groupe et structure financière (items 3.5-05 et 3.5-06).**

| | Avant l'opération | Pro forma, sans cession | Seuil |
|---|---:|---:|---:|
| Dette financière nette, hors dettes locatives (M€) | 21,50 | 21,50 + 16,48 = 37,98 | |
| EBITDA (M€) | 15,40 | 15,40 + 3,60 = 19,00 | |
| **Dette financière nette / EBITDA** | **1,40** | **2,00** (1,999) | 1,90 au plus |
| **Dette financière nette / capitaux propres** (52,00 M€) | **41,35 %** | **73,04 %** | |

- Le ratio pro forma est le même pour les trois solutions : que la plate-forme soit financée par le prêt du groupe, par le prêt bancaire, par le crédit-bail ou par la trésorerie de QUERMANDE, la dette financière nette augmente de tout l'investissement (16,48 M€), et DORVAART compte le crédit-bail comme une dette. Le crédit-bail n'allège donc pas le ratio. Aucune solution ne respecte le seuil de 1,90 sans cession : il faut que la dette financière nette pro forma ne dépasse pas 1,90 × 19,00 = 36,10 M€, soit une cession d'actifs d'au moins 37,98 − 36,10 = **1,88 M€** net d'impôt.
- *Limite de la définition du groupe.* Le ratio de DORVAART rapporte une dette qui exclut les dettes locatives (6,80 M€) à un EBITDA qui ne supporte plus les loyers des terrains loués : il mélange deux lectures et flatte la situation de QUERMANDE. C'est la règle du groupe, à appliquer telle quelle ; la plate-forme, construite sur un terrain acheté, n'ajoute ni loyer ni dette locative, et le crédit-bail, lui, est compté comme une dette.
- Ce qui change selon la solution :
  - *Échéancier et liquidité* : en 2028, la plate-forme dégage 1,78 M€ ; le prêt du groupe ne demande que 0,53 M€ d'intérêts, la solution 3 1,36 M€ (loyer 1,18 + intérêts du prêt du bâtiment 0,18), le prêt bancaire 1,97 M€ (1,50 de capital + 0,47 d'intérêts), soit plus que le flux de la première année ; à partir de 2029 (3,05 M€), les trois sont couverts par la plate-forme.
  - *Risque de taux* : seul le prêt bancaire y expose QUERMANDE (question 3.6).
  - *Refinancement et dépendance* : le prêt in fine laisse 12,00 M€ à rembourser en 2035, à la fin de la vie de la chaîne : sans amortissement, la dette ne baisse pas avec l'actif, et QUERMANDE dépend du groupe pour refinancer ; le prêt bancaire diversifie les prêteurs et réduit la dette chaque année ; le crédit-bail engage QUERMANDE sur un actif dont elle n'est pas propriétaire.
  - *Garanties* : la lettre de soutien de DORVAART engage le groupe envers la banque ; le bailleur garde la propriété de la chaîne.
- Les capitaux propres ne bougent pas : l'autonomie financière se dégrade (dette nette passant de 41,35 % à 73,04 % des capitaux propres sans cession) quel que soit le financement par dette ; seule une cession d'actifs ou un apport de fonds propres de DORVAART l'améliore.

**Recommandation (item 3.5-07).** Proposer à DORVAART, dans tous les cas, la cession du portefeuille hérité, condition du respect du ratio (question 3.7). Pour la dette, deux réponses sont également valables :
- *le prêt de DORVAART Treasury* : taux fixe de 4,40 % (3,30 % après IS), à peine plus cher que le prêt bancaire au taux du jour et moins cher que lui aux taux anticipés par le marché (environ 4,5 %) ; aucune couverture ni garantie à mettre en place ; service faible pendant la montée en charge (0,53 M€ en 2028) ; en contrepartie, 12,00 M€ à rembourser ou à refinancer en 2035, et une dépendance au groupe ;
- *le prêt de la Banque HALBRESSE* : amorti sur les huit ans de la chaîne de tri, ce qui fait baisser la dette au rythme de l'usure de l'actif, et diversifie les prêteurs du groupe ; mais son avantage de coût (3,15 % au taux du jour) disparaît si l'Euribor monte comme le marché l'anticipe, il expose QUERMANDE au taux (couverture de la première période, question 3.6, puis couverture de plus long terme à étudier) et son service de 1,97 M€ dépasse le flux de la plate-forme en 2028.
Le crédit-bail est écarté : le plus cher après impôt, il n'améliore ni le ratio ni la structure.

**Réponses tolérées** : coût après IS du prêt bancaire par l'approximation × 0,75, annoncée ; taux interpolés (4,21 % ; 3,8 % à 3,82 %) ; ratio pro forma de 1,999 présenté comme « à peine inférieur à 2 mais supérieur au seuil » ; recommandation du prêt du groupe argumentée ; mix prêt du groupe et prêt bancaire s'il est justifié par le ratio, le taux et l'échéancier.

**Erreurs fréquentes**
- Oublier l'économie d'impôt perdue sur l'amortissement dans le coût du crédit-bail, ou lui appliquer l'approximation × 0,75.
- Croire que le crédit-bail ou le financement par la trésorerie n'augmente pas la dette financière nette retenue par le groupe (`JUR-T12`).
- Compter les dettes locatives dans le ratio de DORVAART, qui les exclut (ratio avant l'opération surestimé).
- Comparer les financements par leur seul taux nominal, sans les frais ni l'impôt (`JUR-T04`).

**Références** : F02 § 4 (coût de la dette avant et après impôt) [S] ; F01 § 3 (tableaux d'amortissement, amortissement constant et in fine) [S] ; programme 7.2.a et 7.2.b, guide p. 81-82 (taux actuariel, coût net d'IS, frais ; effets sur le levier, la liquidité, l'autonomie financière et la capacité de remboursement ; conditions et structure avant l'opération fournies) [V].

---

### 3.6 FRA et contrats à terme sur l'Euribor 3 mois pour la première période d'intérêts (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Intérêts de la période : **107 683,33 €**, **119 816,67 €**, **144 083,33 €** ; différentiel du FRA, réglé le 31/12/2027 et actualisé : **− 21 113,25 €** (versé par QUERMANDE), **− 9 039,45 €** (versé), **+ 15 035,54 €** (reçu) | 0,5 |
| 3.6-02 | Coût net au 31/03/2028 = intérêts − différentiel capitalisé = **128 916,67 €** dans les trois scénarios ; taux effectif **4,25 %** (2,95 % + 1,30 %) ; FRA ferme : pas de bénéfice de la baisse | 0,5 |
| 3.6-03 | Vente de **12 contrats** à 97,08 (taux implicite **2,92 %**) ; valeur du point **25 €** ; dépôt **7 200 €** ; résultat : cours 97,75, 97,35, 96,55 → **− 20 100 €**, **− 8 100 €**, **+ 15 900 €** | 0,5 |
| 3.6-04 | Coût net **127 783,33 €**, **127 916,67 €**, **128 183,33 €** ; taux effectif **4,21 %**, **4,22 %**, **4,23 %** : proche de 2,92 % + 1,30 % = 4,22 %, l'écart venant de ce que 12 contrats de trois mois (300 € par point) couvrent une période de 91 jours (303,33 € par point) | 0,5 |
| 3.6-05 | Comparaison : FRA de gré à gré, sur mesure (nominal, dates, 91 jours), sans dépôt ni appels de marge, risque de contrepartie sur la banque, peu cessible ; contrats à terme standardisés (taille, échéance), liquides, chambre de compensation qui supprime le risque de contrepartie, mais dépôt de garantie, appels de marge quotidiens à financer, couverture imparfaite (12 contrats pour 12,13 nécessaires, date de dénouement imposée) ; tous deux fermes ; recommandation : le FRA, adapté à une opération unique de 12 M€, malgré un taux garanti supérieur de 3 points de base | 0,5 |

**FRA acheté (items 3.6-01 et 3.6-02).** Nominal 12 000 000 € ; 91 jours ; base Exact/360 ; taux garanti 2,95 %.

| € | Baisse (2,25 %) | Stabilité (2,65 %) | Hausse (3,45 %) |
|---|---:|---:|---:|
| Intérêts : 12 000 000 × (Euribor + 1,30 %) × 91 / 360 | 107 683,33 | 119 816,67 | 144 083,33 |
| Différentiel brut : 12 000 000 × (Euribor − 2,95 %) × 91 / 360 | − 21 233,33 | − 9 100,00 | + 15 166,67 |
| **Différentiel réglé le 31/12/2027** (brut / (1 + Euribor × 91 / 360)) | **− 21 113,25** | **− 9 039,45** | **+ 15 035,54** |
| Différentiel capitalisé au 31/03/2028 | − 21 233,33 | − 9 100,00 | + 15 166,67 |
| **Coût net** (intérêts − différentiel capitalisé) | **128 916,67** | **128 916,67** | **128 916,67** |
| **Taux effectif** (× 360 / 91 / 12 000 000) | **4,25 %** | **4,25 %** | **4,25 %** |

Le FRA garantit le taux de 2,95 %, soit un coût de 4,25 % marge comprise, quel que soit l'Euribor constaté : il protège de la hausse et fait perdre le bénéfice de la baisse (QUERMANDE verse 21 113,25 € à la banque si l'Euribor tombe à 2,25 %). Le différentiel réglé au début de la période est actualisé : placé ou emprunté jusqu'au 31 mars 2028 au taux constaté, il redonne le différentiel brut.

**Contrats à terme (items 3.6-03 et 3.6-04).** Nombre de contrats : 12 000 000 / 1 000 000 = **12** ; valeur du point : 1 000 000 × 0,01 % × 3 / 12 = **25 €** ; taux implicite du cours de vente : 100 − 97,08 = **2,92 %** ; dépôt de garantie : 12 × 600 = **7 200 €**. Au 29 décembre 2027, le contrat est dénoué au cours de 100 − Euribor.

| € | Baisse | Stabilité | Hausse |
|---|---:|---:|---:|
| Cours de dénouement | 97,75 | 97,35 | 96,55 |
| Résultat : 12 × 25 × (97,08 − cours) × 100 | **− 20 100** | **− 8 100** | **+ 15 900** |
| Intérêts de la période (91 jours) | 107 683,33 | 119 816,67 | 144 083,33 |
| **Coût net** (intérêts − résultat) | **127 783,33** | **127 916,67** | **128 183,33** |
| **Taux effectif** | **4,21 %** | **4,22 %** | **4,23 %** |

Le taux visé est 2,92 % + 1,30 % = 4,22 %. Il n'est pas exactement atteint : chaque point de base de hausse du taux de référence coûte 12 000 000 × 0,01 % × 91 / 360 = 303,33 € d'intérêts, alors que les 12 contrats rapportent 300 € par point ; il faudrait 12,13 contrats. La couverture est légèrement insuffisante : un peu de baisse ou de hausse reste à QUERMANDE (4,21 % à 4,23 %).

**Comparaison (item 3.6-05).**

| Critère | FRA de la Banque HALBRESSE | Contrats à terme sur l'Euribor 3 mois |
|---|---|---|
| Marché | gré à gré | organisé, chambre de compensation |
| Ajustement au besoin | sur mesure : 12 000 000 €, 91 jours, dates du prêt | standardisé : contrats de 1 000 000 € et de trois mois, échéance et date de dénouement imposées ; 12 contrats pour 12,13 nécessaires |
| Trésorerie | aucun versement avant le 31/12/2027 | dépôt de 7 200 € et appels de marge quotidiens (jusqu'à 20 100 € versés si l'Euribor baisse) |
| Risque de contrepartie | sur la banque (atténué : c'est aussi le prêteur) | supprimé par la chambre de compensation |
| Liquidité, sortie | contrat peu cessible ; dénouement à négocier | revente possible chaque jour |
| Taux obtenu | 4,25 % | environ 4,22 % |
| Nature | ferme | ferme |

Les deux instruments fixent le taux sans prime et font perdre la baisse ; aucun n'est une option. Les contrats à terme donnent un taux un peu plus bas (3 points de base, environ 900 € sur la période) mais imposent un suivi quotidien et le financement des appels de marge, pour une couverture imparfaite. Pour une opération unique, à une date précise et sur un montant rond, le FRA, simple et ajusté, convient mieux à QUERMANDE ; il ne couvre que le premier trimestre : la couverture des huit ans du prêt relève d'un autre instrument, à étudier avec la banque.

**Réponses tolérées** : coût net du FRA de 128 916,66 € (intermédiaires arrondis au centime) ; différentiel du FRA calculé en fin de période sans actualisation si le candidat le signale et obtient le même coût net ; taux effectif des contrats à terme calculé sur 3 / 12 (4,22 % dans les trois scénarios, coût net de 126 600 €) si la convention est écrite ; recommandation des contrats à terme justifiée par l'absence de risque de contrepartie et le taux plus bas, avec mention des appels de marge.

**Erreurs fréquentes**
- Acheter des contrats à terme alors que QUERMANDE, emprunteur, craint la hausse des taux : elle doit vendre (le cours baisse quand le taux monte).
- Ajouter la marge de 1,30 % au taux garanti dans le calcul du différentiel : le FRA porte sur l'Euribor seul.
- Oublier d'actualiser le différentiel réglé au début de la période, ou l'actualiser au taux garanti.
- Présenter le FRA comme une option qui laisse profiter de la baisse.

**Références** : F07 § 2.2 (FRA, règlement au début de la période, contrats à terme sur taux, vente par l'emprunteur, valeur du point) et § 2.4 (choix d'une couverture : coût, simplicité, flexibilité, risque résiduel) [V programme 6.2 ; guide p. 78 ; S] ; F01 § 7 (base Exact/360) [S] ; F11 (Euribor 3 mois d'environ 2,65 %, hypothèse d'énoncé) [V].

---

### 3.7 Portefeuille hérité : rentabilité, risque et produit de cession (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Poids : 1,20 / 3,00 = **40 %** (BRESTAVEL), **60 %** (MONTAGRIN) ; rentabilité espérée 0,40 × 10 % + 0,60 × 8 % = **8,80 %** ; variance 0,0144 + 0,0144 + 2 × 0,40 × 0,60 × 0,36 × 0,30 × 0,20 = **0,039168** ; écart-type **19,79 %** | 0,5 |
| 3.7-02 | BRESTAVEL seule : **10,00 %** et **30,00 %** ; par euro investi, garder BRESTAVEL seule ajoute 1,20 point de rentabilité espérée pour 10,21 points d'écart-type ; MONTAGRIN seule : 8,00 % et 20,00 % ; lecture en euros acceptée (écart-type de 0,59 M€ pour le portefeuille, 0,36 M€ pour BRESTAVEL seule comme pour MONTAGRIN seule) | 0,5 |
| 3.7-03 | Effet de la corrélation : écart-type du portefeuille 19,79 % inférieur à la moyenne pondérée des écarts-types (24,00 %, cas d'une corrélation de 1) ; 16,97 % avec une corrélation nulle ; la diversification réduit le risque sans réduire la rentabilité espérée (Markowitz, 1952) ; corrélation positive car les deux sociétés dépendent du bâtiment | 0,5 |
| 3.7-04 | BRESTAVEL : risque systématique 1,20 × 15 % = **18,00 %** (variance 0,0324, **36 %** du risque), spécifique 0,09 − 0,0324 = 0,0576, soit **24,00 %** ; portefeuille : bêta **0,96**, systématique **14,40 %** (0,020736), spécifique 0,018432, soit **13,58 %** ; par euro investi, garder BRESTAVEL seule fait plus que tripler la variance spécifique (0,0576 contre 0,0184), risque que le marché ne rémunère pas ; en euros, le risque spécifique de la part restante (0,29 M€ d'écart-type) est le même que l'on garde BRESTAVEL ou MONTAGRIN | 0,5 |
| 3.7-05 | Produit de cession : BRESTAVEL 1,20 + économie d'impôt 0,12 (moins-value 0,48) = **1,32 M€** ; MONTAGRIN 1,80 − impôt 0,18 (plus-value 0,72) = **1,62 M€** ; total **2,94 M€** ; ratio pro forma : MONTAGRIN seule **1,91**, BRESTAVEL seule **1,93**, les deux **1,84** ; seule la cession des deux lignes respecte le seuil de 1,90 (cession minimale 1,88 M€) | 0,5 |

**Rentabilité et risque (items 3.7-01 et 3.7-02).** Valeur au 24 mai 2027 : 40 000 × 30,00 = 1,20 M€ et 30 000 × 60,00 = 1,80 M€, soit 3,00 M€.

| | BRESTAVEL seule | MONTAGRIN seule | Portefeuille (40 % / 60 %) |
|---|---:|---:|---:|
| Rentabilité espérée | 10,00 % | 8,00 % | **8,80 %** |
| Variance | 0,090000 | 0,040000 | **0,039168** |
| Écart-type | 30,00 % | 20,00 % | **19,79 %** |
| Bêta | 1,20 | 0,80 | **0,96** |
| Risque systématique : variance (écart-type) | 0,032400 (18,00 %) | 0,014400 (12,00 %) | 0,020736 (14,40 %) |
| Risque spécifique : variance (écart-type) | 0,057600 (24,00 %) | 0,025600 (16,00 %) | 0,018432 (13,58 %) |
| Part systématique de la variance | 36 % | 36 % | 52,94 % |

Variance du portefeuille : 0,40² × 0,30² + 0,60² × 0,20² + 2 × 0,40 × 0,60 × 0,36 × 0,30 × 0,20 = 0,0144 + 0,0144 + 0,010368 = 0,039168.

**Effet de la corrélation (item 3.7-03).** Si les deux actions évoluaient exactement ensemble (corrélation de 1), l'écart-type du portefeuille serait la moyenne pondérée des écarts-types, 0,40 × 30 % + 0,60 × 20 % = 24,00 % ; avec une corrélation de 0,36, il n'est que de 19,79 %, et il serait de 16,97 % avec une corrélation nulle. La rentabilité espérée, elle, reste la moyenne pondérée (8,80 %) : selon Markowitz (1952), combiner des titres imparfaitement corrélés réduit le risque sans coûter de rentabilité. La corrélation est pourtant positive et assez forte : un fabricant de tuiles et de briques et une entreprise de travaux publics dépendent tous deux du bâtiment, comme QUERMANDE elle-même, dont ils reproduisent le risque.

**Risques systématique et spécifique (item 3.7-04).** Le risque systématique, lié au marché, se mesure par le bêta : pour BRESTAVEL, 1,20 × 15 % = 18,00 % d'écart-type, soit 0,0324 de variance, 36 % de son risque total. Le reste, 0,0576 de variance (24,00 % d'écart-type), est spécifique à la société : il se réduit par diversification. Dans le portefeuille, le bêta est de 0,96 et la variance spécifique tombe à 0,018432 : la diversification a supprimé plus des deux tiers du risque spécifique de BRESTAVEL. Par euro investi, garder BRESTAVEL seule, c'est supporter une variance spécifique trois fois plus forte, que le marché ne rémunère pas : selon le MEDAF, la rentabilité espérée de 10,00 % ne rémunère que son bêta de 1,20. Le gain de 1,20 point de rentabilité espérée est la contrepartie d'un risque de marché plus élevé (bêta de 1,20 au lieu de 0,96), pas du risque spécifique ajouté.

**Produit de cession et ratio (item 3.7-05).**

| M€ | BRESTAVEL | MONTAGRIN | Total |
|---|---:|---:|---:|
| Valeur au 24 mai 2027 | 1,20 | 1,80 | 3,00 |
| Prix d'achat | 40 000 × 42 € = 1,68 | 30 000 × 36 € = 1,08 | 2,76 |
| Plus-value (+) ou moins-value (−) | − 0,48 | + 0,72 | + 0,24 |
| Impôt (25 %) : économie (−) ou charge (+) | − 0,12 | + 0,18 | + 0,06 |
| **Produit de cession net d'impôt** | **1,32** | **1,62** | **2,94** |
| Dette financière nette pro forma (37,98 − produit) | 36,66 | 36,36 | 35,04 |
| **Ratio pro forma** (/ 19,00) | **1,93** | **1,91** | **1,84** |

Ni la cession de MONTAGRIN seule (proposition de Mme AUBRINEAU, 1,62 M€) ni celle de BRESTAVEL seule (1,32 M€) n'atteint la cession minimale de 1,88 M€ : seule la cession des deux lignes respecte le seuil de 1,90 (ratio de 1,84 ; dette financière nette égale à 67,38 % des capitaux propres). Rapportée à sa valeur, la vente de BRESTAVEL rapporte plus que sa valeur de marché (économie d'impôt sur la moins-value), celle de MONTAGRIN moins (impôt sur la plus-value).

**Ce que la proposition ferait au risque de la part restante.** Par euro investi, la part qui resterait investie serait la ligne la plus risquée (écart-type de 30 %, dont 24 % de risque spécifique), concentrée sur un seul fabricant de matériaux dont l'activité suit celle des clients de QUERMANDE ; la diversification serait perdue. En euros, la proposition réduit au contraire le risque supporté par QUERMANDE, puisque 1,62 M€ passent en trésorerie :

| M€ | Portefeuille actuel (3,00) | BRESTAVEL seule (1,20) | MONTAGRIN seule (1,80) |
|---|---:|---:|---:|
| Écart-type en euros | 3,00 × 19,79 % = 0,59 | 1,20 × 30 % = 0,36 | 1,80 × 20 % = 0,36 |
| dont systématique (bêta × 15 % × montant) | 0,43 | 0,22 | 0,22 |
| dont spécifique (écart-type spécifique × montant) | 0,41 | 0,29 | 0,29 |

Garder BRESTAVEL seule ou MONTAGRIN seule laisse donc le même risque en euros : le risque ne départage pas les deux lignes, il plaide seulement pour céder le tout. La proposition ne respecterait pas non plus le ratio du groupe.

**Réponses tolérées** : écart-type de 19,8 % ; analyse du risque en euros plutôt que par euro investi ; décomposition du risque présentée en écarts-types seulement, avec la remarque que les écarts-types ne s'additionnent pas (18 % + 24 % ≠ 30 %) ; produit de cession avant impôt (3,00 M€ ; 1,20 ; 1,80) si le candidat montre que la cession d'une seule ligne n'atteint pas 1,88 M€ (1,80 < 1,88) ; commentaire sur l'intérêt pour DORVAART, actionnaire diversifié, de ne pas faire porter de risque spécifique à sa filiale.

**Erreurs fréquentes**
- Calculer l'écart-type du portefeuille comme moyenne pondérée des écarts-types, en oubliant la covariance (`JUR-T14`).
- Pondérer les titres par leur prix d'achat ou par le nombre d'actions au lieu de leur valeur de marché.
- Additionner les écarts-types systématique et spécifique au lieu des variances.
- Calculer l'impôt sur la valeur de cession au lieu de la plus-value, ou ignorer l'économie d'impôt de la moins-value.

**Références** : F10 § 2 (Markowitz, 1952 ; Sharpe, 1964) [V programme 5.3 ; S] ; programme 5.3.a, 5.3.b et 5.3.c, guide p. 76-77 (risques spécifique et systématique ; diversification et rôle de la corrélation ; portefeuille de deux titres ; corrélations, espérances, écarts-types et bêtas fournis) [V].

---

### 3.8 La proposition de Mme AUBRINEAU : biais de comportement et efficience (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.8-01 | Effet de disposition : vendre la ligne gagnante (MONTAGRIN) et garder la perdante (BRESTAVEL) « jusqu'à ce qu'elle remonte » ; aversion aux pertes et point de référence (le prix d'achat de 42 €), au sens de la théorie des perspectives de Kahneman et Tversky ; ancrage sur un prix d'achat qui est un coût passé, sans effet sur la décision | 0,5 |
| 3.8-02 | Efficience au sens faible (Fama, 1970) : le cours intègre l'information des cours passés ; la baisse de quatre mois suivie d'un mois de hausse ne dit pas que « le creux est passé », pas plus que la hausse de 20 % de MONTAGRIN ne dit qu'elle va baisser ; la perte de 0,48 M€ existe déjà dans la valeur du portefeuille (1,20 M€) : ne pas vendre ne l'efface pas | 0,5 |
| 3.8-03 | Recommandation : céder les deux lignes (ratio de DORVAART, économie d'impôt de 0,12 M€ sur BRESTAVEL, risque spécifique sans rémunération, absence d'intérêt pour un recycleur et pour son actionnaire diversifié à détenir ces actions) ; décider selon la rentabilité, le risque futurs et l'impôt, non selon le prix d'achat ; si une seule ligne devait être vendue, le choix ne se fait pas sur le risque en euros (identique) : l'impôt plaide pour BRESTAVEL (moins-value déduite), mais sa vente rapporte moins (1,32 contre 1,62 M€) | 0,5 |

**Biais de comportement (item 3.8-01).** Mme AUBRINEAU refuse de « constater une perte » sur BRESTAVEL et veut « encaisser le gain » de MONTAGRIN : c'est l'effet de disposition (Shefrin et Statman, 1985), tendance à vendre trop tôt les titres en plus-value et à garder trop longtemps les titres en moins-value. Il s'explique par la théorie des perspectives de Kahneman et Tversky : les gains et les pertes sont jugés par rapport à un point de référence, ici le prix d'achat de 42 €, et une perte pèse plus qu'un gain de même montant ; constater la perte serait douloureux, la reporter laisse espérer qu'elle disparaisse. S'y ajoute l'ancrage sur le prix d'achat. Or ce prix est un coût passé : il ne change ni les rentabilités futures ni le risque de BRESTAVEL. La seule question utile est : à 30 €, faut-il acheter aujourd'hui 1,20 M€ d'actions BRESTAVEL, sans rien d'autre ? Garder une ligne revient à la racheter chaque jour à son cours.

**Efficience des marchés (item 3.8-02).** Sous l'hypothèse d'efficience au sens faible (Fama, 1970), le cours d'aujourd'hui contient déjà toute l'information des cours passés : la tendance des six derniers mois ne permet pas de prévoir le cours de demain. Le léger rebond de BRESTAVEL depuis avril (29,00 € puis 30,00 €) n'annonce pas la fin de la baisse, et la hausse de MONTAGRIN (50 € à 60 €) n'annonce pas sa baisse ; lire ces séries comme des signaux, c'est chercher des régularités dans le hasard (biais de représentativité). La perte de 0,48 M€ par rapport au prix d'achat n'attend pas la vente pour exister : la ligne vaut 1,20 M€ aujourd'hui. Si le marché n'était pas efficient, rien ne dirait d'ailleurs que l'erreur de cours joue en faveur de BRESTAVEL.

**Recommandation (item 3.8-03).** Céder les deux lignes, pour 2,94 M€ net d'impôt :
- c'est la seule façon de respecter le ratio de 1,90 exigé par DORVAART (question 3.7) ;
- si une seule ligne devait être vendue, le risque laissé en euros serait le même (0,36 M€ d'écart-type) ; le choix ne devrait donc tenir qu'à l'impôt et aux perspectives, jamais au prix d'achat : la vente de BRESTAVEL procure une économie d'impôt de 0,12 M€ alors que celle de MONTAGRIN coûte 0,18 M€ d'impôt, mais elle rapporte moins (1,32 contre 1,62 M€) et laisse un ratio moins bon (1,93 contre 1,91) ; la proposition de Mme AUBRINEAU n'est pas fausse par son résultat, elle l'est par son motif (ancrage sur 42 €) ;
- garder une seule ligne concentre un risque spécifique que le marché ne rémunère pas, sur une société dont l'activité dépend, comme celle de QUERMANDE, du bâtiment ;
- un recycleur n'a pas d'avantage à gérer des actions, et DORVAART, dont les actionnaires sont diversifiés, n'a pas besoin que sa filiale détienne un portefeuille : les fonds sont mieux employés dans la plate-forme, dont la VAN est positive.
La décision doit être prise sur des critères explicites (besoin de financement, rentabilité et risque futurs, impôt), arrêtés avant de regarder les plus et moins-values latentes, ce qui limite le poids des biais dans une décision de trésorerie.

**Réponses tolérées** : biais de « coût irrécupérable » ou comptabilité mentale (Thaler) au lieu de l'effet de disposition, s'ils sont reliés au cas ; citation de la théorie des perspectives avec sa date de publication (1979) ou de Kahneman et Tversky (1973) ; analyse de l'efficience au sens semi-fort (les annonces publiques des deux sociétés sont intégrées dans les cours) en complément de la forme faible.

**Erreurs fréquentes**
- Réciter une liste de biais sans les relier aux propos de Mme AUBRINEAU (`JUR-T13`).
- Présenter l'efficience comme la garantie que le cours est « juste » ou qu'il ne baissera pas (`JUR-M01`).
- Attribuer à Fama (1970) la finance comportementale, ou donner un coefficient chiffré à l'aversion aux pertes.
- Justifier la conservation de BRESTAVEL par sa rentabilité espérée plus élevée, sans le risque qui l'accompagne (`JUR-T14`).

**Références** : F06 § 3 (efficience, formes, implications pour le directeur financier) et § 4.2 (biais : aversion aux pertes, ancrage, effet de disposition, représentativité) [V guide p. 73-74 pour les formes et les biais ; S] ; F10 § 1 (Fama, 1970 ; Kahneman et Tversky, 1973 ; Shefrin et Statman, 1985, et Thaler, références facultatives) [V programme 5.1 ; S] ; programme 5.1.c et 5.1.d, guide p. 73-74 (démonstration des formes d'efficience et approfondissement mathématique exclus) [V].
