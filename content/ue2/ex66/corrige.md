# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 66 — Dossier 3 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F06 marchés, finance comportementale et innovations, F07 risques de taux et de change, F10 auteurs et théories, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (positions de change et contre-valeurs ; cours à terme, points de terme et vente à terme ; avance en couronnes et cours implicite ; prime, valeur intrinsèque, valeur temps et dénouement de l'option de change ; primes, bornes et dénouement des deux tunnels de change ; floor et tunnel de taux du placement ; duration, sensibilité et variation de valeur des obligations ; espérances, écarts-types, bêtas, ratios de Sharpe et de Treynor, décomposition du risque du fonds d'actions ; barème, liste noire, hors-programme ; montants sans couverture, écarts au terme, cours d'égalité, coûts des conversions, dépôt de garantie, taux sans couverture, diversification et perte possible vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un cours à terme erroné à la question 3.2, repris dans la comparaison des couvertures de la question 3.3 et dans le dépôt de garantie de la question 3.4, ou un écart-type erroné à la question 3.7, repris dans les ratios de Sharpe et dans la perte possible).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Position de change en couronnes et en dollars, contre-valeur, sens du risque | `6.3.a` Caractériser la position de change courte ou longue, ouverte ou fermée | 1 |
| 3.2 Cours à terme, report, vente à terme, avance en couronnes, technique interne pour les dollars | `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) ; `6.3.c` Maîtriser les techniques internes et les garanties externes | 2 |
| 3.3 Option de vente de couronnes et tunnel de change : prime, bornes, trois scénarios, recommandation | `6.3.d` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (change) | 2,5 |
| 3.4 Plateforme de change en ligne et cotation algorithmique : coût, dépôt, apports, risques | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs | 2 |
| 3.5 Placement des acomptes : floor et tunnel de taux dans trois scénarios | `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) ; `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux | 3 |
| 3.6 Obligations à taux fixe : duration, sensibilité, perte en cas de hausse des taux, choix du placement | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt ; `6.1.b` Discerner les différents types de financement et de placement | 1,5 |
| 3.7 Trésorerie structurelle : deux fonds, diversification, Sharpe et Treynor, risque systématique et spécifique, politique du conseil | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) ; `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres | 5 |
| **Total** | | **17** |

Part du calcul : environ 9,5 points (3.1-01, 3.2-01 et 3.2-02, 3.3-01 à 3.3-03, 3.4-01, 3.5-01 à 3.5-04, 3.6-01 et 3.6-02, 3.7-01 à 3.7-03, 3.7-05 et 3.7-07). Part de l'analyse : environ 7,5 points. La question 3.7 vaut 5 points et se traite sans les calculs des questions 3.1 à 3.6 : elle ne doit pas être sacrifiée faute de temps (`JUR-T15`).

---

### 3.1 Position de change en couronnes et en dollars (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Couronnes : **+ 180,00 M NOK** (17/11/2027) et **+ 60,00 M NOK** (17/05/2028), soit **+ 240,00 M NOK**, contre-valeur 15,65 + 5,22 = **20,87 M€** ; l'acompte d'avril, déjà converti, est exclu ; dollars : − 2,40, − 2,80 et − 2,00, soit **− 7,20 M$**, contre-valeur − 2,14 − 2,50 − 1,79 = **− 6,43 M€** | 0,5 |
| 3.1-02 | Positions **ouvertes** (aucune couverture) ; couronnes : position **longue**, risque d'une **baisse de la couronne**, soit une **hausse** du cours EUR/NOK au certain ; dollars : position **courte**, risque d'une **hausse du dollar**, soit une **baisse** du cours EUR/USD ; les deux positions ne se compensent pas (devises et échéances différentes) | 0,5 |

**Positions (0,5 pt).**

| Devise | Échéance | Encaissements | Décaissements | Position | Contre-valeur au 17/05/2027 |
|---|---|---:|---:|---:|---:|
| NOK (M NOK) | 17 novembre 2027 | 180,00 | — | **+ 180,00** | 180,00 / 11,5000 = 15,65 M€ |
| | 17 mai 2028 | 60,00 | — | **+ 60,00** | 5,22 M€ |
| | **Total** | 240,00 | — | **+ 240,00** | **20,87 M€** |
| USD (M$) | 16 août 2027 | — | 2,40 | **− 2,40** | − 2,40 / 1,1200 = − 2,14 M€ |
| | 15 septembre 2027 | — | 2,80 | **− 2,80** | − 2,50 M€ |
| | 15 octobre 2027 | — | 2,00 | **− 2,00** | − 1,79 M€ |
| | **Total** | — | 7,20 | **− 7,20** | **− 6,43 M€** |

L'acompte de 60 000 000 NOK du 20 avril 2027 est encaissé et converti : il ne crée plus de risque.

**Caractérisation et sens du risque (0,5 pt).** Aucune couverture n'est en place : les deux positions sont **ouvertes**. En couronnes, KERVÉOL détient une créance : la position est **longue**, et le risque est une **dépréciation de la couronne**. Au certain, une baisse de la couronne se lit comme une **hausse** du cours EUR/NOK (1 EUR vaut plus de couronnes, chaque couronne reçue procure moins d'euros) : à 12,30, les 180 M NOK ne valent plus que 14,63 M€ contre 15,65 M€ au cours du jour. En dollars, KERVÉOL doit payer son fournisseur : la position est **courte**, et le risque est une **appréciation du dollar**, soit une **baisse** du cours EUR/USD (il faut plus d'euros pour payer les mêmes dollars). Les deux positions portent sur des devises différentes, à des échéances différentes : la position courte en dollars ne couvre pas la position longue en couronnes. La deuxième échéance en couronnes est, en outre, incertaine quant à sa date (mise en service du parc).

**Réponses tolérées** : contre-valeurs à l'euro (15 652 174 € ; 5 217 391 € ; − 6 428 571 €) ; position nette « en euros » présentée à titre d'information (20,87 − 6,43 = 14,44 M€) si le candidat précise qu'elle ne mesure pas un risque compensé.

**Erreurs fréquentes**
- Inclure l'acompte déjà converti dans la position, ou retenir le prix total de 300 M NOK.
- Inverser le sens du risque au certain : une **hausse** du cours EUR/NOK est une **baisse** de la couronne.
- Compenser la position longue en couronnes par la position courte en dollars.
- `JUR-T03` — les flux de l'annexe 3.1 et les cours de l'annexe 3.2 sont à croiser.

**Références** : F07 § 3.1 (position longue ou courte, ouverte ou fermée, sens du risque au certain) [V programme 6.3.a ; guide p. 78].

---

### 3.2 Cours à terme, vente à terme, avance en couronnes, technique interne (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | F = 11,5000 × (1 + 4,30 % × 184 / 360) / (1 + 2,40 % × 184 / 360) = **11,6103** ; points de terme **+ 1 103** (0,1103 NOK) ; F > comptant : l'**euro est en report** (la couronne en déport), parce que le taux de la couronne dépasse celui de l'euro ; vente à terme : 180 000 000 / 11,6103 = **15 503 475 €** | 0,5 |
| 3.2-02 | Avance : montant prêté 180 000 000 / (1 + 4,60 % × 184 / 360) = **175 865 213 NOK** (intérêts 4 134 787 NOK) ; après la commission de 175 865 NOK, **15 277 335 €** obtenus le 17/05/2027 ; valeur le 17/11/2027 : × (1 + 2,40 % × 184 / 360) = **15 464 737 €** ; cours implicite 180 000 000 / 15 464 737 = **11,6394** | 0,5 |
| 3.2-03 | L'avance procure **38 739 € de moins** que le terme (cours implicite 11,6394 > 11,6103) : taux de l'avance (4,60 %) supérieur au taux de marché de la couronne (4,30 %) et commission ; elle serait préférée si KERVÉOL avait besoin de financement en euros à un coût supérieur à **2,90 %** environ (taux d'équilibre), car elle couvre et finance à la fois ; ici, trésorerie excédentaire : vente à terme | 0,5 |
| 3.2-04 | Technique interne pour les dollars : **termaillage** (avancer les paiements si le dollar risque de monter, contre escompte éventuel), ou négociation d'une facturation en euros, ou achat en dollars adossé à des recettes en dollars ; limites (accord du fournisseur, coût de l'avance de trésorerie, absence de recettes en dollars) | 0,5 |

**Cours à terme (0,5 pt).** Par la parité des taux d'intérêt, au certain :

F = 11,5000 × (1 + 0,0430 × 184 / 360) / (1 + 0,0240 × 184 / 360) = 11,5000 × 1,021978 / 1,012267 = **11,6103 NOK pour 1 EUR**.

Les points de terme valent (11,6103 − 11,5000) × 10 000 = **+ 1 103**. Le cours à terme est supérieur au comptant : l'**euro est en report** et la couronne en **déport**. Le taux de la couronne (4,30 %) dépasse celui de l'euro (2,40 %) : la banque qui achète les couronnes à terme emprunte des couronnes chères et place des euros moins rémunérés ; le différentiel de taux se retrouve dans le cours. La vente à terme procure **15 503 475 €** le 17 novembre 2027, soit 148 699 € (0,95 %) de moins qu'une conversion au comptant du jour : ce n'est pas une perte, mais le prix du différentiel de taux, que l'on ne peut pas éviter en se couvrant.

**Avance en couronnes (0,5 pt).**

| Étape | Calcul | Montant |
|---|---|---:|
| Couronnes empruntées le 17/05/2027 | 180 000 000 / (1 + 4,60 % × 184 / 360) | 175 865 213 NOK |
| Intérêts payés le 17/11/2027 | 180 000 000 − 175 865 213 | 4 134 787 NOK |
| Commission (0,10 %) | 175 865 NOK, soit 15 293 € | |
| Euros obtenus le 17/05/2027 | 175 865 213 × 0,999 / 11,5000 | **15 277 335 €** |
| Intérêts du placement en euros | 15 277 335 × 2,40 % × 184 / 360 | 187 402 € |
| **Valeur le 17/11/2027** | | **15 464 737 €** |
| Cours à terme implicite | 180 000 000 / 15 464 737 | **11,6394** |

Le 17 novembre 2027, les 180 000 000 NOK d'HALVØRA Vind AS remboursent exactement le capital et les intérêts de l'avance : comme la vente à terme, l'avance fixe dès aujourd'hui la contre-valeur en euros.

**Comparaison (0,5 pt).** Le cours implicite de l'avance (11,6394) est moins favorable que le cours à terme (11,6103) : l'avance procure 15 464 737 € contre 15 503 475 €, soit **38 739 € de moins**. L'écart vient du taux de l'avance (4,60 %, contre 4,30 % sur le marché) et de la commission, que la rémunération des euros à 2,40 % ne compense pas. L'avance a un avantage que le terme n'a pas : elle met les euros à disposition **dès aujourd'hui**. Elle deviendrait préférable si KERVÉOL devait se financer en euros : les euros obtenus remplaceraient alors un découvert ; avec un coût du découvert supérieur à 2,90 % environ ((15 503 475 / 15 277 335 − 1) × 360 / 184 = 2,90 %), l'avance procurerait plus que le terme. KERVÉOL a de la trésorerie à placer (annexe 3.5) : la **vente à terme** est préférable. Dans les deux cas, le risque de retard de paiement demeure : si HALVØRA payait en retard, il faudrait rembourser l'avance ou livrer les couronnes vendues à terme (le paiement du 17 novembre est garanti par une banque, ce qui limite ce risque).

**Technique interne pour les achats en dollars (0,5 pt).** KERVÉOL n'a pas de recettes en dollars : aucune compensation n'est possible. Le **termaillage** consiste à avancer (ou retarder) les paiements selon l'anticipation : si la direction craint une hausse du dollar, elle peut payer le fournisseur dès la livraison plutôt qu'à 60 jours, en convertissant ses euros au cours du jour et en demandant un escompte pour paiement anticipé ; le coût est la trésorerie mobilisée plus tôt, et la décision repose sur une anticipation, sans certitude. Autre technique interne : négocier la **facturation en euros** de la fibre de carbone (le risque passe au fournisseur, qui le facturera dans son prix). Pour 7,20 M$, un achat à terme de dollars (couverture externe) reste simple et peu coûteux.

**Réponses tolérées** : points de terme exprimés en couronnes (0,1103) ; montant à terme avec le cours non arrondi (15 503 443 €), si l'arrondi de l'annexe 3.7 n'est pas appliqué : item acquis ; taux d'équilibre de l'avance non calculé si le raisonnement (financement en euros plus cher que le placement) est donné ; compte en devises pour les dollars si le candidat précise qu'il faudrait l'alimenter.

**Erreurs fréquentes**
- Inverser les taux dans la parité (F = 11,3907 : euro faussement en déport) : au certain, le taux de la devise est au numérateur.
- Présenter l'écart entre le terme et le comptant du jour comme une « perte » de la couverture.
- Calculer l'avance sur 180 000 000 NOK empruntés, au lieu du montant actualisé que remboursent les 180 000 000 NOK.
- Oublier la commission ou le placement des euros, puis comparer des montants à des dates différentes (euros du 17 mai contre euros du 17 novembre).
- `JUR-T04` — capitalisation et actualisation sur une durée en jours, acquis du DCG.

**Références** : F07 § 3.2 (avance en devises, termaillage) et § 3.3 (parité des taux, report et déport) [V programme 6.3.b et 6.3.c ; guide p. 78-79] ; F01 § 7 (base Exact/360).

---

### 3.3 Option de vente de couronnes et tunnel de change (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Prime de l'option : 180 000 000 × 1,40 % = 2 520 000 NOK, soit **219 130 €** ; au 17/05/2027, exercer au prix de 11,8000 donnerait 15 254 237 € contre 15 652 174 € au comptant : option **en dehors de la monnaie**, **valeur intrinsèque nulle**, **valeur temps 219 130 €** (durée de six mois, volatilité de la couronne) | 0,5 |
| 3.3-02 | Tunnel : prime de l'option vendue 140 870 €, **prime nette 78 261 €** ; montant minimal 180 000 000 / 11,80 = 15 254 237 €, soit **15 175 976 €** net ; montant maximal 180 000 000 / 11,20 = 16 071 429 €, soit **15 993 168 €** net ; tunnel à prime nulle : bornes **15 254 237 €** et **15 789 474 €** | 0,5 |
| 3.3-03 | Tableau des trois scénarios, nets de prime : sans couverture 14 634 146 / 15 517 241 / 16 513 761 € ; terme 15 503 475 € ; option **15 035 107** (exercée) / **15 298 111** / **16 294 631 €** ; tunnel **15 175 976** (put exercé) / **15 438 981** / **15 993 168 €** (call exercé par la banque) | 0,5 |
| 3.3-04 | Comparaison : terme gratuit, ferme, meilleur en A, et en B devant l'option et le tunnel payant ; option : plancher 15 035 107 €, coût 219 130 €, garde tout le gain (meilleure en C, dès que le cours passe sous 11,4485) ; tunnel : plancher plus élevé que l'option (15 175 976 €), coût réduit, mais gain plafonné à 15 993 168 € ; prime nulle : aucun coût, fourchette plus étroite | 0,5 |
| 3.3-05 | Recommandation argumentée : flux certain (garanti par une banque) et trésorerie excédentaire : vente à terme, ou tunnel à prime nulle si la direction veut garder une partie du gain ; l'option convient mieux à un flux incertain (échéance de mai 2028) ; objectif : protéger la marge du contrat, dont les coûts sont en euros et en dollars | 0,5 |

**Prime et décomposition de l'option (0,5 pt).** La prime vaut 1,40 % × 180 000 000 = 2 520 000 NOK, soit 2 520 000 / 11,5000 = **219 130 €**, payés le 17 mai 2027. Si l'option était exercée ce jour, KERVÉOL vendrait ses couronnes à 11,8000 et obtiendrait 15 254 237 €, alors que le comptant (11,5000) en donne 15 652 174 € : l'option de vente est **en dehors de la monnaie** ; sa **valeur intrinsèque est nulle** et toute la prime est **valeur temps** (219 130 €). Cette valeur temps rémunère la possibilité que la couronne baisse au-delà de 11,80 d'ici six mois : elle dépend de la durée restante et de la volatilité de la couronne, et tend vers zéro à l'échéance. La prime est donnée par la banque : aucun modèle ne la calcule ici.

**Tunnel de change (0,5 pt).**

| | Tunnel 11,2000 – 11,8000 | Tunnel à prime nulle 11,4000 – 11,8000 |
|---|---:|---:|
| Prime de l'option de vente achetée (1,40 %) | 219 130 € | 219 130 € |
| Prime de l'option d'achat vendue | 0,90 %, soit 140 870 € | 219 130 € |
| **Prime nette payée** | **78 261 €** | **0** |
| Montant minimal (cours au-delà de 11,80) | 15 254 237 €, soit **15 175 976 €** net | **15 254 237 €** |
| Montant maximal (cours en deçà du prix d'exercice de l'option vendue) | 16 071 429 €, soit **15 993 168 €** net | **15 789 474 €** |

Les deux options vendues sont aussi en dehors de la monnaie (valeur intrinsèque nulle, valeur temps de 140 870 € pour la première). Pour annuler la prime, l'option vendue doit valoir autant que l'option achetée : son prix d'exercice se rapproche du cours à terme (11,40 au lieu de 11,20), et KERVÉOL renonce au gain plus tôt.

**Trois scénarios, nets de prime (0,5 pt).**

| Cours au 17/11/2027 | A : 12,3000 | B : 11,6000 | C : 10,9000 |
|---|---:|---:|---:|
| Sans couverture | 14 634 146 € | 15 517 241 € | 16 513 761 € |
| Vente à terme (11,6103) | 15 503 475 € | 15 503 475 € | 15 503 475 € |
| Option : décision | exercée (11,80) | abandonnée | abandonnée |
| Option, net de la prime | **15 035 107 €** | **15 298 111 €** | **16 294 631 €** |
| Tunnel : cours appliqué | 11,80 (option de vente exercée) | 11,60 (aucune) | 11,20 (option vendue exercée par la banque) |
| Tunnel, net de la prime | **15 175 976 €** | **15 438 981 €** | **15 993 168 €** |
| Tunnel à prime nulle (complément, non noté) | 15 254 237 € | 15 517 241 € | 15 789 474 € |

**Comparaison (0,5 pt).**
- **Vente à terme** : gratuite, simple, elle fixe 15 503 475 € quel que soit le cours ; c'est la meilleure solution dans le scénario A ; en B, elle fait mieux que l'option et que le tunnel payant, mais le tunnel à prime nulle (comme l'absence de couverture) procure 13 766 € de plus, la couronne finissant un peu au-dessus de son cours à terme ; elle renonce à tout gain (− 1 010 286 € par rapport à l'absence de couverture dans le scénario C).
- **Option** : elle garantit un plancher de 15 035 107 € net, inférieur au terme de 468 368 €, à cause de la prime (219 130 €) et d'un prix d'exercice moins favorable que le cours à terme ; elle conserve tout le gain si la couronne monte et dépasse le terme dès que le cours passe sous **11,4485** (180 000 000 / (15 503 475 + 219 130)). C'est la plus souple, mais la plus chère.
- **Tunnel** : la prime reçue réduit le coût à 78 261 € ; le plancher (15 175 976 €) est meilleur que celui de l'option ; en contrepartie, KERVÉOL renonce au gain au-delà de 11,20 (maximum 15 993 168 €). Il dépasse le terme si le cours final est inférieur à 11,5520 (180 000 000 / (15 503 475 + 78 261)).
- **Tunnel à prime nulle** : aucun décaissement, plancher le plus élevé des solutions optionnelles (15 254 237 €), mais fourchette étroite (gain plafonné à 15 789 474 €).

**Recommandation (0,5 pt).** Le paiement du 17 novembre 2027 est **certain** dans son montant et sa date (garanti par une banque) : la couverture n'a pas à payer de souplesse. Les coûts de KERVÉOL sont en euros (et en dollars pour la fibre de carbone) : l'objectif est de protéger la marge du contrat, pas de spéculer sur la couronne. Nous recommandons la **vente à terme** pour la plus grande partie des 180 000 000 NOK, ou, si Mme TALMORVAN souhaite garder une partie du gain en cas d'appréciation de la couronne, le **tunnel à prime nulle** (perte maximale de 249 238 € par rapport au terme, gain maximal de 286 000 € environ). L'option, chère, conviendrait mieux à l'échéance de mai 2028, dont la date dépend de la mise en service du parc. Toute recommandation argumentée sur le coût, le plancher, le renoncement au gain et la certitude du flux est acceptée.

**Réponses tolérées** : primes converties au cours à terme, si l'hypothèse est écrite (item 3.3-01 acquis pour moitié, l'annexe fixant le comptant) ; valeur intrinsèque exprimée en couronnes par euro (nulle) ; recommandation de l'option si le candidat la justifie par une anticipation d'appréciation de la couronne et une acceptation du coût.

**Erreurs fréquentes**
- Lire les bornes à l'incertain : au certain, le plancher en euros correspond au cours **le plus élevé** (11,80) et le plafond au cours **le plus bas** (11,20).
- Exercer l'option de vente en C (10,90) : elle procurerait moins d'euros que le comptant.
- Oublier de déduire la prime, ou déduire la prime de l'option achetée sans ajouter celle de l'option vendue dans le tunnel.
- Calculer la prime par un modèle d'évaluation : elle est donnée.
- `JUR-T07` — un tableau par scénario est attendu.

**Références** : F07 § 3.3 (options de change, valeur intrinsèque et valeur temps, grille de choix) [V programme 6.3.d ; guide p. 79] ; F07 § 2.3 (tunnel, prime nulle, par analogie avec le tunnel de taux) [S].

---

### 3.4 Plateforme de change en ligne et cotation algorithmique (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Coût annuel : banque 36 000 000 × 0,35 % = **126 000 €** ; plateforme 36 000 000 × 0,10 % + 6 000 = **42 000 €** ; économie **84 000 €** ; volume d'équilibre 6 000 / 0,25 % = **2 400 000 €** ; vente à terme par la plateforme : dépôt 5 % × 15 503 475 = **775 174 €**, complément exigé au-delà d'une perte latente de 465 104 € | 0,5 |
| 3.4-02 | Rôle et apports : fintech de paiement et de change, qui met en concurrence onze fournisseurs par un algorithme ; prix plus bas et transparent, exécution automatique et ordres à cours limite, raccordement au logiciel de trésorerie, rapidité ; désintermédiation partielle de la banque | 0,5 |
| 3.4-03 | Risques : **contrepartie** sur les opérations à terme (capitaux propres de 38 M€, couverture propre auprès des banques) ; **protection des fonds** par cantonnement, sans garantie des dépôts ; **liquidité** (dépôt de 775 174 € et appels quand la couronne monte, alors que la créance gagne) ; **dépendance à l'outil** (panne de cinq heures, erreur d'algorithme, cybersécurité) ; pas d'options | 0,5 |
| 3.4-04 | Place à côté de la banque : plateforme pour les conversions au comptant courantes ; banque pour les couvertures à terme et optionnelles, sans dépôt grâce aux lignes de crédit, et pour la relation d'ensemble (ligne de trésorerie confirmée, comptes, dépôt à terme des acomptes) ; négocier avec la banque à l'aide de l'offre ; double fournisseur, contrôle des ordres | 0,5 |

**Coûts (0,5 pt).**

| Conversions au comptant sur douze mois (36 000 000 €) | Banque MARVÉLIS | Plateforme CAMBRELIS |
|---|---:|---:|
| Écart de cours | 0,30 % × 36 000 000 = 108 000 € | 0,10 % × 36 000 000 = 36 000 € |
| Commission | 0,05 % × 36 000 000 = 18 000 € | — |
| Abonnement | — | 6 000 € |
| **Coût annuel** | **126 000 €** | **42 000 €** |

La plateforme économise **84 000 €** par an, soit 0,23 % du volume. Elle devient moins chère dès que le volume annuel dépasse 6 000 / (0,35 % − 0,10 %) = **2 400 000 €** : KERVÉOL en est très au-dessus. Pour les couvertures à terme, l'avantage s'inverse : la plateforme ajoute un écart de 0,10 % au cours de parité, la banque aucun, et la plateforme exige un dépôt de garantie de 5 % × 15 503 475 = **775 174 €** pour une vente à terme des 180 000 000 NOK, avec un dépôt complémentaire si la perte latente dépasse 465 104 € (soit une appréciation de la couronne d'environ 3 %).

**Rôle et apports du nouvel acteur (0,5 pt).** CAMBRELIS est une **fintech** de paiement et de change, établissement de paiement (fait d'énoncé) qui ne prête pas et ne collecte pas de dépôts. Sa **cotation algorithmique** compare en continu les prix de onze banques et fournisseurs de liquidité et retient le meilleur : elle réduit l'asymétrie d'information entre la banque, qui connaît le prix de marché, et l'entreprise, qui accepte souvent un écart opaque. Apports pour KERVÉOL : un coût divisé par trois, un prix lisible, une exécution immédiate et automatisée, des ordres à cours limite qui évitent de surveiller le marché, un raccordement au logiciel de trésorerie qui supprime des saisies. Le nouvel acteur exerce aussi une **pression concurrentielle** sur les banques, qui doivent justifier leurs écarts.

**Risques (0,5 pt).**
- **Contrepartie** : sur une vente à terme, la plateforme est la contrepartie de KERVÉOL ; avec 38 M€ de capitaux propres, sa défaillance obligerait KERVÉOL à se recouvrir au cours du jour. Une banque présente une contrepartie plus solide et surveillée comme telle.
- **Protection des fonds** : les fonds en attente de conversion sont cantonnés sur des comptes séparés des fonds propres de la plateforme ; ils ne sont pas des dépôts bancaires. Le risque porte sur la durée pendant laquelle ils y restent et sur la solidité des banques teneuses de comptes : limiter les montants en transit et les délais.
- **Liquidité** : le dépôt de 775 174 € et les appels de dépôt sont exigés justement quand la couronne s'apprécie, alors que la créance sur HALVØRA, payée seulement en novembre, gagne en valeur sans procurer de trésorerie.
- **Dépendance à l'outil** : la panne de cinq heures de mars 2027 montre le risque opérationnel ; un ordre automatique mal paramétré, une erreur de l'algorithme ou un mouvement brutal du marché peuvent déclencher une conversion à un mauvais cours ; la connexion au logiciel de trésorerie ouvre un risque de cybersécurité (fraude au virement, faux ordres).
- **Offre incomplète** : pas d'options, couvertures limitées à douze mois.

**Place à côté de la banque (0,5 pt).** La plateforme est un **complément** : elle convient aux conversions au comptant courantes, nombreuses et de petit montant, où l'économie est certaine. Les couvertures du contrat norvégien (terme ou tunnel) restent mieux placées à la Banque MARVÉLIS : pas de dépôt grâce aux lignes de crédit, options disponibles, contrepartie solide. Surtout, la banque apporte à KERVÉOL une **relation d'ensemble** : ligne de crédit de trésorerie confirmée, tenue des comptes, dépôt à terme des acomptes ; la fragiliser pourrait coûter plus que 84 000 € par an. KERVÉOL peut utiliser l'offre de CAMBRELIS pour **renégocier** l'écart de la banque, ou confier à la plateforme une partie des conversions, avec des plafonds par ordre, une double validation et une solution de repli en cas de panne.

**Réponses tolérées** : coût de la banque exprimé par opération (3 150 € en moyenne contre 1 050 €) ; référence à la désintermédiation ou à l'asymétrie d'information (Akerlof, 1970) ; mention du risque de mimétisme des algorithmes de prix en période de crise.

**Erreurs fréquentes**
- Développer les règles de l'agrément des établissements de paiement ou du règlement européen sur les crypto-actifs : le statut de CAMBRELIS est un fait d'énoncé, et la plateforme ne traite aucun crypto-actif.
- Comparer les seuls écarts de cours sans la commission de la banque ni l'abonnement de la plateforme.
- Réciter les apports du numérique sans les chiffres du cas (coût, dépôt, panne) : `JUR-T13`.
- `JUR-M02` — le rôle des nouveaux acteurs est attendu à partir du cas.

**Références** : F06 § 6 (fintechs, algorithmes, risques) [S ; programme 5.4.a et 5.4.b V] ; F07 § 3.3 (grille de choix des couvertures) ; F10 (Akerlof, 1970).

---

### 3.5 Placement des acomptes : floor et tunnel de taux (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Prime du floor : 30 000 000 × 0,20 % × 183 / 360 = **30 500 €** ; Euribor du jour 2,10 % < 2,25 % : floor **dans la monnaie**, **valeur intrinsèque 22 875 €**, **valeur temps 7 625 €** ; tunnel : prime nette (0,20 % − 0,12 %) × 30 000 000 × 183 / 360 = **12 200 €** (0,08 % par an) | 0,5 |
| 3.5-02 | Sans couverture : 228 750 € (**1,50 %**), 335 500 € (**2,20 %**), 503 250 € (**3,30 %**) ; avec le floor : versements 129 625 €, 22 875 € et 0 ; produit net **327 875 €** (**2,15 %**), **327 875 €** (**2,15 %**), **472 750 €** (**3,10 %**) | 0,5 |
| 3.5-03 | Avec le tunnel : produit net **346 175 €** (**2,27 %**) dans les scénarios de baisse et de stabilité ; en hausse, versement du cap à la banque 30 500 €, produit net **460 550 €** (**3,02 %**) | 0,5 |
| 3.5-04 | Taux garantis : floor, minimum **2,15 %** (2,25 % + marge − 0,20 %), sans maximum ; tunnel, minimum **2,27 %**, maximum **3,02 %** (3,00 % + marge − 0,08 %) | 0,5 |
| 3.5-05 | Comparaison : le tunnel donne un plancher plus élevé et coûte moins, mais plafonne le rendement ; le floor garde toute la hausse ; en stabilité, le tunnel fait mieux que l'absence de couverture (2,27 % contre 2,20 %, le floor étant dans la monnaie), le floor un peu moins bien (2,15 %, soit 7 625 €, sa valeur temps) ; risque de contrepartie faible (banque dépositaire) | 0,5 |
| 3.5-06 | Choix argumenté : direction qui craint la baisse, horizon court, Euribor de 2,10 % loin du cap de 3,00 % : **tunnel de taux** ; floor si l'on veut garder la hausse | 0,5 |

**Primes et décomposition (0,5 pt).** La durée est de 183 jours, soit 183 / 360 = 0,5083 année. Prime du floor : 30 000 000 × 0,20 % × 0,5083 = **30 500 €**. Avec l'Euribor de 2,10 %, inférieur au prix d'exercice de 2,25 %, le floor est **dans la monnaie** : il procurerait dès aujourd'hui 30 000 000 × 0,15 % × 0,5083 = **22 875 €** (valeur intrinsèque) ; la **valeur temps** vaut 30 500 − 22 875 = **7 625 €** : elle rémunère la possibilité d'une baisse plus forte de l'Euribor d'ici le second trimestre. Prime du cap vendu : 0,12 % × 30 000 000 × 0,5083 = 18 300 € ; **prime nette du tunnel** : 30 500 − 18 300 = **12 200 €**, soit 0,08 % par an.

**Trois scénarios (1 pt pour 3.5-02 et 3.5-03).**

| Euribor 3 mois | Baisse : 1,40 % | Stabilité : 2,10 % | Hausse : 3,20 % |
|---|---:|---:|---:|
| Intérêts (Euribor + marge) | 228 750 € | 335 500 € | 503 250 € |
| **Sans couverture : taux** | **1,50 %** | **2,20 %** | **3,30 %** |
| Versement du floor reçu | 129 625 € | 22 875 € | 0 |
| Prime du floor | − 30 500 € | − 30 500 € | − 30 500 € |
| **Floor : produit net** | **327 875 €** | **327 875 €** | **472 750 €** |
| **Floor : taux** | **2,15 %** | **2,15 %** | **3,10 %** |
| Versement du floor reçu | 129 625 € | 22 875 € | 0 |
| Versement du cap payé à la banque | 0 | 0 | − 30 500 € |
| Prime nette | − 12 200 € | − 12 200 € | − 12 200 € |
| **Tunnel : produit net** | **346 175 €** | **346 175 €** | **460 550 €** |
| **Tunnel : taux** | **2,27 %** | **2,27 %** | **3,02 %** |

Taux de rendement = produit net / (30 000 000 × 183 / 360) ; par exemple 327 875 / 15 250 000 = 2,15 %.

**Taux garantis (0,5 pt).** Le floor garantit un minimum de 2,25 % + 0,10 % − 0,20 % = **2,15 %**, sans plafond : au-dessus de 2,25 %, le rendement suit l'Euribor, diminué de la prime. Le tunnel garantit un minimum de 2,25 % + 0,10 % − 0,08 % = **2,27 %** et un maximum de 3,00 % + 0,10 % − 0,08 % = **3,02 %**.

**Comparaison (0,5 pt).** Les deux protections jouent leur rôle en cas de baisse : 2,15 % ou 2,27 % au lieu de 1,50 %, soit 99 125 € ou 117 425 € de plus que sans couverture. Dans le scénario de stabilité, le tunnel fait mieux que l'absence de couverture (2,27 % contre 2,20 %, + 10 675 €), parce que le floor est dans la monnaie ; le floor rapporte un peu moins (2,15 %, − 7 625 €, soit sa valeur temps). Le **tunnel** coûte 18 300 € de moins que le floor et relève le plancher, mais KERVÉOL abandonne à la banque la hausse au-delà de 3,00 % : dans le scénario de hausse, elle obtient 3,02 % contre 3,10 % avec le floor et 3,30 % sans couverture. Le **floor** est l'assurance pure : plus chère, elle garde toute la hausse. La contrepartie est la banque dépositaire : le risque est faible. La marge et la durée sont identiques dans les trois solutions.

**Choix (0,5 pt).** La direction craint une baisse, l'Euribor est à 2,10 % et un cap à 3,00 % suppose une hausse de plus de 0,90 point en six mois, qu'elle n'anticipe pas ; les acomptes doivent surtout rapporter un minimum connu : le **tunnel de taux** est le mieux adapté (rendement compris entre 2,27 % et 3,02 %). Le floor serait préféré si la direction voulait garder la possibilité d'une hausse des taux.

**Réponses tolérées** : calcul trimestre par trimestre (deux périodes de 92 et 91 jours) avec le même Euribor, qui donne les mêmes totaux ; taux de rendement présentés sur une base 365 si la conversion est expliquée (item acquis pour moitié, l'annexe fixant la base 360) ; choix du floor justifié par une anticipation de hausse.

**Erreurs fréquentes**
- Raisonner comme un emprunteur (achat du cap) : un placeur à taux variable craint la **baisse** et achète le floor.
- Oublier que, dans le tunnel, KERVÉOL **paie** le versement du cap à la banque quand l'Euribor dépasse 3,00 %.
- Appliquer les primes annuelles sans les proratiser sur 183 jours.
- Dire que le floor est en dehors de la monnaie : l'Euribor du jour (2,10 %) est sous le prix d'exercice.
- `JUR-T07` — tableau par scénario attendu.

**Références** : F07 § 2.1 (qui craint quoi), § 2.3 (floor, tunnel, valeur intrinsèque et valeur temps) et § 2.4 (grille de choix) [V programme 6.2.b et 6.2.c ; guide p. 78] ; F01 § 7.

---

### 3.6 Obligations à taux fixe : duration, sensibilité, choix du placement (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Flux pour 100 € : 2,90 ; 2,90 ; 102,90, actualisés à 2,90 % (prix 100) ; **duration 2,916 ans** ; **sensibilité − 2,834** | 0,5 |
| 3.6-02 | Perte estimée : − 2,83406 × 1 % × 30 000 000 = **− 850 218 €** ; par actualisation à 3,90 % : prix 97,22, valeur 29 165 890 €, perte **− 834 110 €** ; écart de 16 108 € dû à l'approximation linéaire | 0,5 |
| 3.6-03 | Relation inverse : coupons fixes moins attractifs que ceux des nouvelles émissions, prix qui baisse jusqu'à offrir le taux du marché ; acomptes à rendre disponibles dans six mois : capital garanti nécessaire, donc **dépôt à terme à taux variable** (avec protection) plutôt que des obligations à trois ans revendues avant l'échéance | 0,5 |

**Duration et sensibilité (0,5 pt).**

| Année t | Flux (pour 100 €) | Flux actualisé à 2,90 % | t × flux actualisé |
|---:|---:|---:|---:|
| 1 | 2,90 | 2,8183 | 2,8183 |
| 2 | 2,90 | 2,7388 | 5,4777 |
| 3 | 102,90 | 94,4429 | 283,3287 |
| **Total** | | **100,00** | **291,6246** |

Duration = 291,6246 / 100 = **2,916 ans** ; sensibilité = − 2,916 / 1,029 = **− 2,834** : une hausse d'un point du taux fait baisser la valeur d'environ 2,83 %.

**Perte (0,5 pt).** Perte estimée, avec la sensibilité non arrondie : − 2,83406 × 1 % × 30 000 000 = **− 850 218 €**. Par actualisation des flux à 3,90 % : prix 97,22 € pour 100 €, soit 29 165 890 €, et une perte de **834 110 €**. L'écart (16 108 €) vient de ce que la sensibilité est une approximation linéaire : elle surestime légèrement la perte. En six mois, cette perte effacerait à elle seule plus de deux fois les intérêts du dépôt à terme (335 500 € dans le scénario de stabilité).

**Relation inverse et choix du placement (0,5 pt).** Une obligation à taux fixe verse des coupons de 2,90 % jusqu'à l'échéance. Si les taux du marché montent à 3,90 %, les nouvelles obligations rapportent davantage ; l'ancienne ne trouve preneur qu'à un prix plus bas, tel que son taux actuariel égale celui du marché : sa valeur, somme des flux actualisés au taux du marché, baisse. Les acomptes appartiennent économiquement aux commandes en cours : ils serviront à payer les matières et la production à partir de décembre 2027. KERVÉOL ne peut pas courir le risque de devoir revendre des obligations en perte à ce moment. Le placement adapté est un **placement sans risque en capital et à échéance de six mois** : le dépôt à terme à taux variable, protégé par le tunnel de taux (question 3.5). Les obligations à taux fixe conviennent à une trésorerie durable, détenue jusqu'à l'échéance.

**Réponses tolérées** : perte estimée de 850 200 € avec la sensibilité arrondie à − 2,834 ; duration calculée sur 30 000 000 € plutôt que pour 100 € ; sensibilité donnée en valeur absolue (2,834) si le sens de la variation est dit ; sensibilité recalculée sur une durée restante de 2,5 ans à la revente, si l'hypothèse est écrite.

**Erreurs fréquentes**
- Confondre duration et maturité (3 ans) ou oublier de diviser par (1 + taux) pour la sensibilité.
- Croire qu'une obligation à taux fixe est sans risque parce que son coupon est fixe : le risque porte sur la valeur avant l'échéance.
- Proposer les obligations parce qu'elles rapportent un peu plus (2,90 % contre 2,20 %), sans tenir compte de l'horizon des acomptes.
- `JUR-T13` — relier la réponse à l'usage des acomptes dans six mois.

**Références** : F07 § 2.1 (relation inverse valeur-taux, duration, sensibilité) et § 4.2 (supports de placement selon l'horizon) [V programme 6.2.a ; guide p. 77-78].

---

### 3.7 Trésorerie structurelle : deux fonds et politique du conseil (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Espérances : **5,50 %**, **6,50 %**, **7,50 %** ; variances 0,002781, 0,006451, 0,012611 ; écarts-types **5,27 %**, **8,03 %**, **11,23 %** (formule avec la corrélation de 0,20) | 1 |
| 3.7-02 | Diversification : écart-type inférieur à la moyenne pondérée des écarts-types (5,27 % contre 6,80 % ; 8,03 % contre 9,60 % ; 11,23 % contre 12,40 %), car la corrélation (0,20) est inférieure à 1 (Markowitz, 1952) ; la répartition à 20 % rapporte plus que le fonds O pour un risque à peine plus élevé | 0,5 |
| 3.7-03 | Sharpe : fonds O **0,25** ; fonds A **0,33** ; indice **0,34** ; répartitions **0,38**, **0,37**, **0,36** : les mélanges sont plus efficaces que chaque fonds seul | 0,5 |
| 3.7-04 | Treynor : fonds O **10,00 %** ; fonds A **6,67 %** ; indice **5,50 %** ; Treynor ne retient que le risque systématique (bêta) : il flatte le fonds O, dont le risque est surtout étranger au marché des actions, et convient à un investisseur déjà diversifié, alors que Sharpe retient le risque total, pertinent pour KERVÉOL, qui ne détient que deux fonds | 0,5 |
| 3.7-05 | Fonds A : variance 0,0324 ; systématique 0,90² × 0,16² = **0,020736 (64 %)** ; spécifique **0,011664 (36 %)** ; écarts-types correspondants 14,40 % et 10,80 % | 0,5 |
| 3.7-06 | KERVÉOL supporte les deux risques : le systématique, non diversifiable, et le spécifique, qu'elle ne diversifie pas avec deux fonds ; le fonds A est concentré sur la transition énergétique, secteur de KERVÉOL : double exposition au même risque | 0,5 |
| 3.7-07 | Politique : rentabilité défavorable − 5,05 %, − 9,56 %, − 14,96 % ; pertes possibles **1 009 332 €**, **1 912 775 €** et **2 991 984 €** ; seules les répartitions à 20 % et 40 % respectent les deux limites (40 % d'actions au plus, 2 000 000 € de perte au plus) | 0,5 |
| 3.7-08 | Recommandation : **40 %** selon la règle du conseil (espérance la plus élevée, 1 300 000 € par an) ; réserves : marge de 87 225 € seulement sous la limite de perte, concentration sectorielle, caractère durable de la trésorerie à vérifier (acomptes susceptibles d'être restitués, placement non disponible sans risque de perte avant cinq ans) ; 20 % ou un fonds d'actions plus large acceptés s'ils sont argumentés | 0,5 |
| 3.7-09 | Réponse à l'administrateur : la répartition à 60 % viole les deux limites ; l'argument de la dilution du risque dans le temps est fragile (la perte possible en montant ne disparaît pas, la trésorerie peut être nécessaire avant cinq ans) ; biais d'excès de confiance possible | 0,5 |

**Espérances et écarts-types (1 pt).** Avec wO et wA les parts des fonds O et A :

E = wO × 4,50 % + wA × 9,50 % ; σ² = wO² × 0,04² + wA² × 0,18² + 2 × wO × wA × 0,20 × 0,04 × 0,18.

| Part du fonds A | 20 % | 40 % | 60 % |
|---|---:|---:|---:|
| Espérance de rentabilité | **5,50 %** | **6,50 %** | **7,50 %** |
| wO² σO² | 0,001024 | 0,000576 | 0,000256 |
| wA² σA² | 0,001296 | 0,005184 | 0,011664 |
| 2 wO wA ρ σO σA | 0,000461 | 0,000691 | 0,000691 |
| **Variance** | **0,002781** | **0,006451** | **0,012611** |
| **Écart-type** | **5,27 %** | **8,03 %** | **11,23 %** |
| Moyenne pondérée des écarts-types | 6,80 % | 9,60 % | 12,40 % |
| Réduction du risque par la diversification | 1,53 point | 1,57 point | 1,17 point |
| Bêta de la répartition | 0,26 | 0,42 | 0,58 |

**Effet de la diversification (0,5 pt).** Au sens de Markowitz (1952), le risque d'un portefeuille dépend des covariances et pas seulement des risques de chaque titre. La corrélation entre les deux fonds (0,20) est faible : leurs mauvaises années ne coïncident pas souvent, et l'écart-type de chaque répartition est inférieur à la moyenne pondérée des écarts-types (5,27 % au lieu de 6,80 % pour la répartition à 20 %). Ajouter 20 % d'actions au fonds obligataire porte l'espérance de 4,50 % à 5,50 % alors que l'écart-type ne passe que de 4,00 % à 5,27 %. Avec une corrélation de 1, il n'y aurait aucun gain de diversification.

**Ratios de Sharpe (0,5 pt).** Sharpe = (espérance − 3,50 %) / écart-type.

| | Fonds O | Fonds A | Indice M | 20 % d'actions | 40 % d'actions | 60 % d'actions |
|---|---:|---:|---:|---:|---:|---:|
| Prime de rentabilité | 1,00 % | 6,00 % | 5,50 % | 2,00 % | 3,00 % | 4,00 % |
| **Sharpe** | **0,25** | **0,33** | **0,34** | **0,38** | **0,37** | **0,36** |

Les trois répartitions rémunèrent mieux chaque unité de risque total que chacun des fonds et que l'indice : c'est l'effet de la diversification. Le fonds A seul fait un peu moins bien que l'indice.

**Ratios de Treynor et classement (0,5 pt).** Treynor = (espérance − 3,50 %) / bêta : fonds O 1,00 % / 0,10 = **10,00 %** ; fonds A 6,00 % / 0,90 = **6,67 %** ; indice **5,50 %** (la prime de marché). Treynor classe le fonds O premier, Sharpe le classe dernier. Treynor (1965) ne retient que le risque **systématique** : il convient à un investisseur qui détient déjà un portefeuille diversifié, où seul le bêta compte. Le risque du fonds O vient surtout des taux d'intérêt, presque sans lien avec le marché des actions (bêta 0,10) : Treynor ignore ce risque et flatte le fonds. Le fonds A bat l'indice selon Treynor (6,67 % contre 5,50 %) mais pas selon Sharpe (0,33 contre 0,34) : il rémunère bien son risque de marché, mais porte un risque spécifique que Sharpe pénalise. KERVÉOL ne détiendra que ces deux fonds : c'est son **risque total** qui compte, et le **ratio de Sharpe** est le critère pertinent.

**Décomposition du risque du fonds A (0,5 pt).**

| Fonds A | Variance | Part | Écart-type |
|---|---:|---:|---:|
| Risque total | 0,18² = 0,032400 | 100 % | 18,00 % |
| Risque systématique : bêta² × σM² = 0,81 × 0,0256 | **0,020736** | **64 %** | 0,90 × 16 % = 14,40 % |
| Risque spécifique : 0,032400 − 0,020736 | **0,011664** | **36 %** | 10,80 % |

Les variances s'additionnent, pas les écarts-types (14,40 % + 10,80 % ≠ 18,00 %). La part systématique (64 %) est le carré de la corrélation entre le fonds et l'indice (0,90 × 16 / 18 = 0,80).

**Le risque que supporte KERVÉOL (0,5 pt).** Le risque systématique n'est pas diversifiable : c'est le seul que le MEDAF rémunère. Le risque spécifique se diversifie, mais à condition de détenir de nombreux actifs ; avec deux fonds, KERVÉOL le garde presque en entier. Le fonds A est un fonds **thématique**, concentré sur les sociétés de la transition énergétique : ses 36 % de risque spécifique sont un risque sectoriel. Or KERVÉOL fabrique des pales d'éoliennes : les chocs qui pèsent sur ce secteur (hausse des taux qui renchérit les parcs, retards d'autorisation, concurrence asiatique) frapperaient en même temps son activité et son placement. Elle se diversifierait mieux avec un fonds d'actions large, moins corrélé à son propre métier.

**Politique de risque du conseil (0,5 pt).**

| Part du fonds A | 20 % | 40 % | 60 % |
|---|---:|---:|---:|
| Part en actions ≤ 40 % | oui | oui | **non** |
| Rentabilité défavorable : E − 2 σ | − 5,05 % | − 9,56 % | − 14,96 % |
| Perte possible sur 20 000 000 € | 1 009 332 € | 1 912 775 € | **2 991 984 €** |
| Perte possible ≤ 2 000 000 € | oui | oui (marge 87 225 €) | **non** |
| Gain espéré par an | 1 100 000 € | 1 300 000 € | 1 500 000 € |

**Recommandation (0,5 pt).** Les répartitions à 20 % et à 40 % respectent les deux limites ; selon la règle du conseil, la répartition à **40 %** est retenue, car son espérance est la plus élevée (6,50 %, soit 1 300 000 € par an, contre 1 100 000 €). Trois réserves méritent d'être soumises au conseil : la perte possible n'est inférieure à la limite que de 87 225 € ; le fonds d'actions est concentré sur le secteur de KERVÉOL ; et le conseil doit s'assurer que ces 20 000 000 € sont vraiment durables : les acomptes peuvent devoir être restitués et le placement ne sera pas disponible sans risque de perte avant cinq ans. La répartition à 20 % offre d'ailleurs le meilleur ratio de Sharpe (0,38). Une recommandation de 20 % à 40 %, ou de 40 % avec un fonds d'actions européennes large à la place du fonds thématique, est acceptée si elle est argumentée.

**Réponse à l'administrateur désigné par NORDVÅG (0,5 pt).** La répartition à 60 % dépasse les deux limites que le conseil a lui-même fixées (part en actions et perte possible de 2 991 984 €) : elle ne peut pas être retenue sans changer la politique. L'idée que « le risque se dilue dans le temps » est fragile : la rentabilité moyenne varie moins sur cinq ans que sur un an, mais la perte possible en montant ne disparaît pas, et une mauvaise année peut tomber au moment où le groupe a besoin de sa trésorerie (baisse des commandes, restitution d'acomptes). L'argument peut traduire un **excès de confiance**. Si le conseil voulait plus d'actions, il devrait d'abord modifier sa politique de risque, explicitement.

**Réponses tolérées** : écarts-types calculés par la covariance (0,20 × 0,04 × 0,18 = 0,00144) ; ratios de Treynor exprimés en fraction (0,10 ; 0,0667 ; 0,055) ; Treynor des répartitions (7,69 %, 7,14 %, 6,90 %) donné en complément ; rentabilité attendue du fonds A selon le MEDAF (8,45 %) et comparaison avec ses 9,50 % (alpha de 1,05 point), en complément ; recommandation à 20 % fondée sur le ratio de Sharpe et la concentration sectorielle.

**Erreurs fréquentes**
- Calculer l'écart-type d'une répartition comme la moyenne pondérée des écarts-types, sans le terme de covariance.
- Recalculer la corrélation : elle est fournie.
- Additionner les écarts-types systématique et spécifique.
- Retenir la répartition au meilleur ratio de Sharpe sans vérifier les limites du conseil, ou l'inverse.
- Rechercher le portefeuille de variance minimale : il n'est pas demandé.
- `JUR-T14` — Markowitz, Sharpe et Treynor sont attendus pour justifier la diversification et le choix des ratios.

**Références** : F10 (Markowitz, 1952 ; Sharpe, 1964 et ratio de Sharpe ; Treynor, 1965) [V programme 5.3 ; S pour Treynor] ; F06 § 4.2 (excès de confiance) [S] ; F07 § 4.2 (supports de placement) [S].
