# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 60 — Dossier 3 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F06 marchés, finance comportementale et innovations, F07 risques de taux et de change, F10 auteurs et théories, F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (positions de change par trimestre et sur le semestre, contre-valeurs et effet d'une variation de 5 % ; cours à terme, points de terme et montant de la vente à terme ; prime et dénouement de l'option de change ; valeur de marché, duration, sensibilité et variation de valeur de la dette à taux fixe ; montant emprunté, remboursement, taux garanti et gain ou perte de l'emprunt terme contre terme ; nombre d'options, valeur du point, prime, taux maximal et taux effectifs des options sur le contrat à terme de taux ; coût actuariel du paiement à l'usage ; annuité du prêt bancaire ; barème, liste noire, hors-programme ; écarts entre l'option, le terme et l'absence de couverture, cours d'égalité, emprunt en zlotys, paiements selon la production et conditions du partenariat vérifiés par script).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un cours à terme erroné à la question 3.3, repris dans le cours d'égalité, ou un taux garanti erroné à la question 3.5, repris dans la comparaison des couvertures).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Position de change en dollars et en zlotys, sens du risque, effet d'une variation de 5 % | `6.3.a` Caractériser la position de change courte ou longue, ouverte ou fermée | 1,5 |
| 3.2 Techniques internes : facturation en euros, clause d'indexation monétaire, emprunt en zlotys | `6.3.c` Maîtriser les techniques internes et les garanties externes | 2 |
| 3.3 Cours à terme, vente à terme et option de vente de dollars, cours d'égalité, recommandation | `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) ; `6.3.d` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (change) | 2,5 |
| 3.4 Hausse des taux : coût du prêt à taux variable et valeur de la dette à taux fixe | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 1 |
| 3.5 Emprunt terme contre terme et options sur le contrat à terme Euribor 3 mois, comparaison | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux ; `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) | 4 |
| 3.6 Nouvel acteur du financement des éleveurs et notation algorithmique : rôle, apports, risques, place face aux banques | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs | 3 |
| 3.7 Paiement à l'usage : coût pour l'éleveur, effet de la production, coûts et créances pour TRÉVALAC, recommandation | `7.2.c` Analyser les nouveaux outils de financement ; `7.2.a` Comparer les sources de financement et notamment leurs coûts | 2 |
| **Total** | | **16** |

Part du calcul : environ 8 points (3.1-01 et 3.1-03, 3.3-01 à 3.3-04, 3.4-01, 3.5-01 à 3.5-04, 3.7-01 à 3.7-03). Part de l'analyse : environ 8 points. Les questions 3.6 et 3.7 valent 5 points et se traitent sans les calculs des questions 3.1 à 3.5 : elles ne doivent pas être sacrifiées faute de temps en fin d'épreuve (`JUR-T15`).

---

### 3.1 Position de change en dollars et en zlotys (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Positions en dollars : **+ 6,20** (T3), **+ 7,60** (T4), **+ 13,80 M$** sur le semestre, soit 5,39 + 6,61 = **12,00 M€** ; en zlotys : **− 17,20** et **− 16,40**, soit **− 33,60 M PLN** sur le semestre, ou − 4,10 − 3,90 = **− 8,00 M€** | 0,5 |
| 3.1-02 | Positions **ouvertes** (aucune couverture) ; dollar : position **longue**, risque d'une **baisse du dollar** (hausse du cours EUR/USD au certain) ; zloty : position **courte**, risque d'une **hausse du zloty** (baisse du cours EUR/PLN au certain) | 0,5 |
| 3.1-03 | Baisse de 5 % du dollar : cours 1,2105, contre-valeur 11,40 M€, effet **− 0,60 M€** ; hausse de 5 % du zloty : cours 4,0000, contre-valeur − 8,40 M€, effet **− 0,40 M€** ; perte totale **1,00 M€** | 0,5 |

**Positions (0,5 pt).**

| Millions de devises | T3 2027 | T4 2027 | Semestre |
|---|---:|---:|---:|
| Règlements de TRÉVALAC Dairy Inc. | 9,60 | 11,20 | 20,80 |
| Achats de composants en dollars | − 3,40 | − 3,60 | − 7,00 |
| **Position en dollars (M$)** | **+ 6,20** | **+ 7,60** | **+ 13,80** |
| Contre-valeur au cours de 1,1500 (M€) | 5,39 | 6,61 | **12,00** |
| Ventes de TRÉVALAC Polska en zlotys | 14,00 | 16,40 | 30,40 |
| Salaires et charges sociales | − 21,40 | − 22,20 | − 43,60 |
| Sous-traitants et fournisseurs locaux | − 9,80 | − 10,60 | − 20,40 |
| **Position en zlotys (M PLN)** | **− 17,20** | **− 16,40** | **− 33,60** |
| Contre-valeur au cours de 4,2000 (M€) | − 4,10 | − 3,90 | **− 8,00** |

**Caractérisation (0,5 pt).** Aucune couverture n'est en place : les deux positions sont **ouvertes**, à chaque trimestre et sur le semestre. En dollars, les encaissements dépassent les décaissements : la position est **longue** ; le groupe perd si le **dollar baisse**, c'est-à-dire si le cours EUR/USD au certain monte (1 EUR vaut plus de dollars, chaque dollar reçu procure moins d'euros). Les achats de composants en dollars forment déjà une compensation naturelle : ils ramènent l'exposition de 20,80 M$ à 13,80 M$. En zlotys, les coûts de la filiale polonaise dépassent ses ventes locales, le reste de sa production étant vendu en euros à la société de tête : la position est **courte** ; le groupe perd si le **zloty s'apprécie**, c'est-à-dire si le cours EUR/PLN baisse (il faut plus d'euros pour payer les salaires et les sous-traitants polonais).

**Variation défavorable de 5 % (0,5 pt).**

| | Dollar (baisse de 5 %) | Zloty (hausse de 5 %) |
|---|---:|---:|
| Cours modifié | 1,1500 / 0,95 = **1,2105** | 4,2000 / 1,05 = **4,0000** |
| Contre-valeur de la position semestrielle au cours modifié | 13,80 / 1,2105 = 11,40 M€ | − 33,60 / 4,0000 = − 8,40 M€ |
| **Effet sur la contre-valeur** | **− 0,60 M€** | **− 0,40 M€** |

Les deux risques se cumulent : une baisse de 5 % du dollar et une hausse de 5 % du zloty coûteraient **1,00 M€** au groupe sur le seul second semestre. Les deux positions ne se compensent pas, car elles portent sur deux devises différentes et de sens opposés.

**Réponses tolérées** : contre-valeurs en euros à l'unité (12 000 000 € ; − 8 000 000 €) ; effet de la variation exprimé directement comme 5 % de la contre-valeur (0,60 et 0,40 M€) ; cours modifiés présentés comme 1,15 × 1,05 = 1,2075 et 4,20 × 0,95 = 3,99, si la convention est expliquée (effets de − 0,57 et − 0,42 M€) : l'item 3.1-03 est alors acquis pour moitié, l'annexe 3.6 fixant la convention.

**Erreurs fréquentes**
- Oublier les achats de composants en dollars et retenir une position de 20,80 M$ : la compensation naturelle est le premier outil de gestion du risque.
- Inverser le sens du risque au certain : une **hausse** du cours EUR/USD est une **baisse** du dollar.
- Additionner les positions en dollars et en zlotys sans conversion, ou compenser une position longue en dollars par une position courte en zlotys.
- `JUR-T03` — les flux en devises de l'annexe 3.1 et les cours de l'annexe 3.2 sont à croiser.

**Références** : F07 § 3.1 (position longue ou courte, ouverte ou fermée, sens du risque au certain) [V programme 6.3.a ; guide p. 78].

---

### 3.2 Techniques internes : facturation en euros, clause d'indexation, emprunt en zlotys (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | **Facturation en euros des distributeurs** : supprime le risque de transaction sur les ventes nord-américaines en le transférant aux distributeurs ; coût certain de 3 % des prix sur 45 % des achats, bien supérieur au coût d'une vente à terme ; perte de compétitivité face aux concurrents qui facturent en dollars ; variante de la seule facturation de TRÉVALAC Dairy Inc. en euros : le risque reste dans le groupe | 0,5 |
| 3.2-02 | **Clause d'indexation monétaire** : couvre la période entre la signature et la livraison, au-delà d'une franchise de 4 % et dans la limite de 6 % d'ajustement ; partage du risque avec les éleveurs, symétrique (le groupe renonce au gain d'une hausse du dollar) ; risque résiduel dans la franchise et au-delà de 10 % ; acceptation commerciale difficile (concurrent à prix ferme, demande d'extension aux pièces et à la maintenance) | 0,5 |
| 3.2-03 | **Emprunt en zlotys** : adosse la moitié des travaux payée en zlotys et l'actif polonais à une dette en zlotys ; mais ses intérêts (5,124 M PLN par an) et son remboursement (84 M PLN en 2030) accroissent la position courte en zlotys, déjà aggravée par l'extension (− 10 M PLN par an) ; taux de 6,10 % plus élevé qu'en euros, écart compensé seulement si le zloty baisse | 0,5 |
| 3.2-04 | Choix argumenté : refuser la facturation de la seule filiale en euros ; ne retenir la facturation des distributeurs en euros que si la remise demandée est inférieure au coût d'une couverture ; retenir la clause pour les grands contrats à livrer ; limiter l'emprunt en zlotys aux travaux payés en zlotys (42 M PLN) ; compléter par des couvertures de marché | 0,5 |

**Facturation en euros des distributeurs nord-américains (0,5 pt).** Le choix de la monnaie de facturation est la technique interne la plus radicale : si TRÉVALAC Dairy Inc. facture en euros, les règlements qu'elle reçoit et ceux qu'elle verse à la société de tête sont en euros, et le risque de change de transaction sur ces ventes disparaît pour le groupe. Il n'est pas supprimé mais **transféré aux distributeurs**, qui achètent en euros et revendent en dollars aux éleveurs. Ils en demandent le prix : une baisse de 3 % des prix, certaine, alors qu'une vente à terme à six mois ne coûte que (5 217 391 − 5 186 274) / 5 217 391 = 0,60 % du montant couvert (question 3.3). Elle ne serait de plus acceptée que par les deux principaux distributeurs (45 % des achats) : le reste des ventes resterait en dollars. Enfin, les concurrents facturent en dollars : une baisse du dollar rendrait les robots du groupe plus chers pour les éleveurs américains, et le **risque économique** (perte de volumes et de parts de marché) remplacerait le risque de transaction.

La **variante de l'administrateur** ne couvre rien au niveau du groupe : TRÉVALAC Dairy Inc. vendrait toujours en dollars et devrait des euros à la société de tête ; le risque passerait seulement de la société de tête à la filiale, dont la marge en dollars absorberait les variations de change. La position consolidée resterait longue de 13,80 M$.

**Clause d'indexation monétaire (0,5 pt).** Elle couvre le risque né entre la signature d'un contrat et la livraison du robot, quatre à neuf mois plus tard. Le risque est **partagé** : TRÉVALAC garde les variations du cours jusqu'à 4 % autour du cours de référence ; au-delà, l'éleveur supporte l'écart, dans la limite de 6 % d'ajustement du prix ; au-delà de 10 %, le risque revient à TRÉVALAC. La clause est **symétrique** : si le dollar s'apprécie de plus de 4 %, le prix en dollars baisse et TRÉVALAC renonce à une partie du gain de change. Illustration facultative : un robot vendu 200 000 $ au cours de 1,1500 et livré au cours de 1,2190 (écart de 6 %) est facturé 200 000 × 1,02 = 204 000 $, soit 167 350 € au lieu de 164 069 € sans la clause (173 913 € au cours de la signature). Limites : l'éleveur ne connaît plus son prix en dollars, alors qu'un concurrent propose des prix fermes ; la demande d'étendre la clause aux pièces et à la maintenance montre qu'elle se négocie client par client ; son suivi est lourd, et elle laisse un risque dans la franchise. Elle convient aux grands contrats à livraison lointaine, pas aux ventes courantes.

**Emprunt en zlotys de TRÉVALAC Polska (0,5 pt).** S'endetter dans la devise de l'actif financé est un **adossement** : les 42 M PLN de travaux payés aux entreprises polonaises seraient réglés avec des zlotys empruntés, sans conversion, et la dette en zlotys varierait en euros comme l'usine elle-même, ce qui protège la valeur en euros de l'actif net polonais (risque patrimonial). Mais l'adossement n'est efficace que si l'actif produit des recettes dans la devise de la dette. Or TRÉVALAC Polska vend surtout en euros à la société de tête, et sa position en zlotys est déjà courte (− 33,60 M PLN par semestre) ; l'extension l'aggrave de 8 − 18 = **− 10 M PLN par an**. Les intérêts de l'emprunt (84 × 6,10 % = **5,124 M PLN par an**, 1,22 M€ au cours du jour) et son remboursement de **84 M PLN en 2030** seraient de nouveaux décaissements en zlotys : la position courte grandirait, et une hausse du zloty renchérirait la dette en euros. L'emprunt coûte aussi plus cher qu'en euros (6,10 % contre 3,80 % pour le prêt variable au taux du jour) ; selon la parité des taux, cet écart n'est compensé que si le zloty se déprécie (taux du zloty de 5,40 % contre 2,60 % pour l'euro à six mois), ce qui est l'inverse du risque que craint le groupe.

**Choix (0,5 pt).** Les techniques internes viennent en premier parce qu'elles sont en principe gratuites ; ici, deux d'entre elles ont un coût. Recommandation : refuser la facturation de la seule filiale en euros, qui déplace le risque sans le réduire ; ne pas accorder 3 % de baisse de prix aux distributeurs pour un risque qui se couvre à terme pour environ 0,6 % par semestre ; proposer la clause d'indexation aux grands élevages pour les robots à livrer ; limiter l'emprunt en zlotys à la part des travaux payée en zlotys (42 M PLN), en gardant le prêt en euros pour le reste ; couvrir sur le marché la créance en dollars du 30 novembre (question 3.3) et rechercher des achats en dollars ou des recettes en zlotys supplémentaires (compensation naturelle).

**Réponses tolérées** : recommandation d'accepter la facturation en euros des deux principaux distributeurs si elle est présentée comme un choix commercial durable, coût chiffré ; refus de la clause au nom de la compétitivité ; emprunt en zlotys refusé en totalité, ou retenu pour l'ensemble si le candidat le justifie par la protection de l'actif polonais et mentionne l'aggravation de la position courte.

**Erreurs fréquentes**
- Présenter la facturation de TRÉVALAC Dairy Inc. en euros comme une couverture du groupe : le risque ne quitte pas le périmètre.
- Affirmer qu'un emprunt en zlotys « ferme » la position en zlotys : il ajoute des décaissements en zlotys à une position déjà courte.
- Comparer les taux de 6,10 % et 3,80 % sans tenir compte de l'évolution attendue du zloty (parité des taux d'intérêt).
- Développer les clauses contractuelles sous un angle juridique : hors sujet (UE 1).
- `JUR-T13` — techniques présentées en général, sans les chiffres du cas.

**Références** : F07 § 3.2 (choix de la monnaie de facturation, indexation monétaire, compensation des flux) et § 3.3 (parité des taux) [V programme 6.3.c ; guide p. 79].

---

### 3.3 Cours à terme, vente à terme et option de vente de dollars (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | F = 1,1500 × (1 + 3,80 % × 183 / 360) / (1 + 2,60 % × 183 / 360) = **1,1569** ; points de terme **+ 69** ; l'euro est en **report** (le dollar en déport), car le taux du dollar dépasse celui de l'euro | 0,5 |
| 3.3-02 | Vente à terme : 6 000 000 / 1,1569 = **5 186 274 €** (5 217 391 € au comptant du jour) ; prime de l'option : 6 000 000 × 1,84 % = 110 400 $, soit **96 000 €** | 0,5 |
| 3.3-03 | Scénario A (1,1000) : option **abandonnée**, 5 454 545 €, net **5 358 545 €** ; terme 5 186 274 € ; sans couverture 5 454 545 €. Scénario B (1,2200) : option **exercée** à 1,1600, 5 172 414 €, net **5 076 414 €** ; terme 5 186 274 € ; sans couverture 4 918 033 € | 0,5 |
| 3.3-04 | Cours d'égalité : 6 000 000 / (5 186 274 + 96 000) = **1,1359** : l'option procure plus que le terme si le cours du 30 novembre est inférieur à 1,1359 (dollar plus fort) | 0,5 |
| 3.3-05 | Recommandation argumentée : vente à terme pour la créance, certaine et intragroupe, sans prime, d'autant que M. PERRIGOT craint une baisse du dollar ; option réservée aux flux incertains ou si le groupe veut garder le gain d'une hausse du dollar | 0,5 |

**Cours à terme (0,5 pt).** Par la parité des taux d'intérêt, au certain :

F = 1,1500 × (1 + 0,038 × 183 / 360) / (1 + 0,026 × 183 / 360) = 1,1500 × 1,019317 / 1,013217 = **1,1569**.

Points de terme : (1,1569 − 1,1500) × 10 000 = **+ 69**. À terme, 1 euro vaut plus de dollars qu'au comptant : l'euro est en **report** et le dollar en **déport**. L'écart reflète le différentiel de taux : celui qui vend des dollars à terme renonce au taux du dollar (3,80 %) pour le taux de l'euro (2,60 %).

**Vente à terme et prime (0,5 pt).** La vente à terme des 6 000 000 $ garantit **6 000 000 / 1,1569 = 5 186 274 €** le 30 novembre 2027, quel que soit le cours ce jour-là, sans prime. L'écart avec la conversion au comptant du jour (5 217 391 €, soit 31 117 € ou 0,60 %) n'est pas une perte de change : c'est le différentiel de taux d'intérêt sur 183 jours. La prime de l'option vaut 6 000 000 × 1,84 % = 110 400 $, convertie au comptant du 31 mai : 110 400 / 1,1500 = **96 000 €**.

**Dénouement dans les deux scénarios (0,5 pt).** L'option de vente de dollars au prix d'exercice de 1,1600 est exercée si le cours du 30 novembre est supérieur à 1,1600 (le dollar vaut alors moins que le prix garanti).

| Au 30 novembre 2027 | A : 1 EUR = 1,1000 USD (dollar fort) | B : 1 EUR = 1,2200 USD (dollar faible) |
|---|---:|---:|
| Sans couverture : 6 000 000 / cours | 5 454 545 € | 4 918 033 € |
| Vente à terme à 1,1569 | 5 186 274 € | 5 186 274 € |
| Option : décision | **abandon** (vente au comptant à 1,1000) | **exercice** (vente à 1,1600) |
| Option : montant encaissé | 5 454 545 € | 5 172 414 € |
| **Option : montant net de la prime** | **5 358 545 €** | **5 076 414 €** |
| Option − terme | + 172 272 € | − 109 860 € |
| Terme − absence de couverture | − 268 272 € | + 268 241 € |

Dans le scénario A, la vente à terme fait perdre le gain de la hausse du dollar (268 272 € de moins que sans couverture) ; l'option, abandonnée, laisse profiter de ce gain, diminué de la prime. Dans le scénario B, les deux couvertures protègent ; l'option procure 109 860 € de moins que le terme, à cause de la prime et d'un prix d'exercice (1,1600) moins favorable que le cours à terme (1,1569). Le montant net de **5 076 414 €** est le minimum que garantit l'option, quel que soit le cours.

**Cours d'égalité (0,5 pt).** Pour un cours inférieur à 1,1600, l'option est abandonnée et procure 6 000 000 / S − 96 000. Elle égale la vente à terme quand 6 000 000 / S − 96 000 = 5 186 274, soit **S = 6 000 000 / 5 282 274 = 1,1359**. Il faut donc que le dollar s'apprécie de plus de 1,24 % par rapport au comptant du jour (cours de 1,1500 à 1,1359) pour que l'option l'emporte sur le terme.

**Recommandation (0,5 pt).** La créance du 30 novembre est **certaine** : c'est un règlement de la filiale américaine, compris dans une position longue de 7,60 M$ au quatrième trimestre, que les 6 000 000 $ ne dépassent pas (aucun risque de surcouverture). M. PERRIGOT craint une baisse du dollar ; le déport du dollar ne la prévoit pas, il traduit seulement l'écart entre les taux du dollar et de l'euro. La **vente à terme** est la solution adaptée : gratuite, simple, elle fixe 5 186 274 €. L'option coûte 96 000 € (1,84 % du nominal, 1,85 % du montant garanti à terme), garantit moins (5 076 414 €) et n'est gagnante que si le dollar s'apprécie au-delà de 1,1359 : elle se justifie pour des flux **incertains** (contrats de robots encore en négociation) ou si la direction veut garder une chance de gain. Un panachage (terme pour la créance, option pour une partie des flux attendus et non encore facturés) est cohérent.

**Réponses tolérées** : cours à terme non arrondi (montant de 5 186 168 € au lieu de 5 186 274 €) ; recommandation de l'option si elle est argumentée par une anticipation de hausse du dollar et par le coût chiffré ; écarts présentés par rapport à l'absence de couverture seulement.

**Erreurs fréquentes**
- Calculer le cours à terme avec les taux inversés (1,1431) : au certain, le taux de la devise est au numérateur.
- Exercer l'option dans le scénario A : vendre à 1,1600 des dollars qui valent 1,1000 serait absurde.
- Oublier de déduire la prime, ou la convertir au cours du 30 novembre.
- Présenter l'écart entre le terme et le comptant du jour comme une perte de change.
- Évaluer la prime par un modèle : elle est donnée (modèles de valorisation des options exclus du programme).

**Références** : F07 § 3.3 (parité des taux d'intérêt, report et déport, options de change, grille de choix) [V programme 6.3.b et 6.3.d ; guide p. 78-79].

---

### 3.4 Hausse des taux : coût du prêt variable et valeur de la dette à taux fixe (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Valeur de marché de l'emprunt à taux fixe : **22,78 M€** à 3,90 % ; **21,95 M€** à 4,90 % ; baisse de **0,82 M€** (− 3,62 %) ; estimation par la sensibilité (− 3,71) : − 0,84 M€ (facultatif) | 0,5 |
| 3.4-02 | Explications : prêt variable révisé chaque trimestre, + 200 000 € d'intérêts par an pour un point de hausse (taux du jour 3,80 %, soit 760 000 € par an) ; relation inverse valeur-taux ; pour TRÉVALAC, emprunteur, la baisse de valeur de la dette fixe est un gain d'opportunité (elle paie 2,50 % quand le marché exige 3,90 % à 4,90 %) ; c'est le prêteur qui supporte la perte de valeur | 0,5 |

**Valeur de la dette à taux fixe (0,5 pt).** Flux restants : intérêts de 24,00 × 2,50 % = 0,60 M€ les 31 mai 2028 à 2031 et remboursement de 24,00 M€ le 31 mai 2031.

| Taux du marché | Valeur de marché = Σ flux actualisés | |
|---|---:|---:|
| 3,90 % (aujourd'hui) | 0,60 / 1,039 + 0,60 / 1,039² + 0,60 / 1,039³ + 24,60 / 1,039⁴ = **22,78 M€** | |
| 4,90 % (+ 1 point) | 0,60 / 1,049 + … + 24,60 / 1,049⁴ = **21,95 M€** | variation **− 0,82 M€** (− 3,62 %) |

Information : duration 3,852 ans ; sensibilité − 3,852 / 1,039 = − 3,707 ; variation estimée − 3,707 % × 22,78 = − 0,84 M€, proche de la variation exacte.

**Explications (0,5 pt).** Le prêt de l'extension est à **taux variable** : l'Euribor 3 mois est fixé au début de chaque trimestre, si bien que toute hausse se transmet aux intérêts dès la période suivante. Au taux du jour (2,40 % + 1,40 % = 3,80 %), il coûterait 760 000 € par an ; chaque point de hausse ajoute **200 000 € par an** (50 000 € par trimestre). Le risque est celui de l'emprunteur futur, qui craint la hausse.

La valeur d'une dette à taux fixe est la valeur actuelle de ses flux, fixés au contrat : quand le taux du marché monte, ces flux sont actualisés à un taux plus élevé et la valeur baisse (**relation inverse valeur-taux**), d'autant plus que la duration est longue. Pour TRÉVALAC, emprunteur, la baisse de valeur de sa dette n'est pas une perte : elle traduit l'avantage de payer 2,50 % quand le marché exige 3,90 % puis 4,90 % (**gain d'opportunité**, non réalisé tant que la dette n'est pas remboursée). C'est le prêteur qui supporte la perte de valeur. À l'inverse, si les taux baissaient, la valeur de la dette monterait : TRÉVALAC paierait un taux supérieur au marché, et un remboursement anticipé coûterait cher. La dette à taux fixe protège donc le groupe contre la hausse, mais pas le prêt de l'extension, qui reste à couvrir (question 3.5).

**Réponses tolérées** : valeurs en pourcentage du nominal (94,91 et 91,47) ; présentation du risque de la dette fixe comme un « risque d'opportunité » en cas de baisse des taux ; variation estimée par la sensibilité seule, si la relation inverse est expliquée (l'item 3.4-01 est alors acquis pour moitié).

**Erreurs fréquentes**
- Affirmer que la hausse des taux renchérit la dette à taux fixe déjà en place : ses intérêts ne changent pas.
- Actualiser au taux nominal de 2,50 % (valeur de 24,00 M€) ou oublier le dernier coupon.
- Présenter la sensibilité comme positive.

**Références** : F07 § 2.1 (exposition, relation inverse valeur-taux, duration, sensibilité) [V programme 6.2.a ; guide p. 78].

---

### 3.5 Emprunt terme contre terme et options sur le contrat à terme Euribor 3 mois (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Montant à emprunter le 31 mai 2027 : 20 000 000 / 1,025^0,5 = **19 754 592 €** ; remboursement du 30 novembre 2030 : 19 754 592 × 1,0387^3,5 = **22 562 308 €** (intérêts de la période 2 562 308 €) ; taux garanti : (22 562 308 / 20 000 000)^(1/3) − 1 = **4,10 %** | 1 |
| 3.5-02 | Scénario de hausse (5,00 %) : intérêts sans couverture 3 152 500 €, **gain de 590 192 €** ; scénario de baisse (3,50 %) : intérêts sans couverture 2 174 358 €, **perte de 387 951 €** | 0,5 |
| 3.5-03 | **20 options** de vente ; valeur du point de base **25 €** ; prime totale 20 × 0,12 × 100 × 25 = **6 000 €** ; taux maximal de la première période (100 − 97,25) / 100 + 1,40 % + 0,12 % = **4,27 %** | 0,5 |
| 3.5-04 | Hausse : cours 96,60, **exercice**, gain 32 500 €, résultat + 26 500 €, intérêts 240 000 €, coût net 213 500 €, **taux effectif 4,27 %** ; baisse : cours 97,80, **abandon**, résultat − 6 000 €, intérêts 180 000 €, coût net 186 000 €, **taux effectif 3,72 %** | 1 |
| 3.5-05 | Comparaison argumentée (couverture ferme sur trois ans contre couverture optionnelle d'un trimestre ; coût, souplesse, risque résiduel, gré à gré contre marché organisé) et recommandation | 1 |

**Emprunt terme contre terme (1 pt).** TRÉVALAC emprunte aujourd'hui pour trois ans et demi et place les fonds six mois : le placement lui rend 20 000 000 € le jour où elle en a besoin, et elle rembourse l'emprunt en une fois trois ans plus tard.

| | Calcul | Montant |
|---|---|---:|
| Montant à emprunter le 31 mai 2027 | 20 000 000 / 1,025^0,5 | **19 754 592 €** |
| Placement au 30 novembre 2027 | 19 754 592 × 1,025^0,5 | 20 000 000 € |
| Remboursement le 30 novembre 2030 | 19 754 592 × 1,0387^3,5 | **22 562 308 €** |
| Intérêts de la période de trois ans | 22 562 308 − 20 000 000 | 2 562 308 € |
| **Taux garanti** | (1,0387^3,5 / 1,025^0,5)^(1/3) − 1 = (22 562 308 / 20 000 000)^(1/3) − 1 | **4,10 %** |

Le taux garanti (4,10 %) dépasse le taux de l'emprunt (3,87 %) parce que les six premiers mois sont payés 3,87 % et ne rapportent que 2,50 % de placement : le coût de ce portage s'ajoute au taux des trois années. Il dépasse aussi le taux variable du jour (3,80 %) : la courbe des taux croissante intègre la hausse attendue.

**Gain ou perte de l'emprunt terme contre terme (0,5 pt).** Comparaison avec un emprunt de 20 000 000 € à trois ans contracté le 30 novembre 2027, intérêts capitalisés (montants au 30 novembre 2030) :

| Scénario | Intérêts sans couverture : 20 000 000 × [(1 + taux)³ − 1] | Intérêts de l'emprunt terme contre terme | Gain (+) ou perte (−) |
|---|---:|---:|---:|
| Hausse (5,00 %) | 3 152 500 € | 2 562 308 € | **+ 590 192 €** |
| Baisse (3,50 %) | 2 174 358 € | 2 562 308 € | **− 387 951 €** |

Instrument ferme : il protège contre la hausse et fait perdre le bénéfice de la baisse.

**Options de vente sur le contrat à terme (0,5 pt).** L'emprunteur craint la hausse des taux, donc la baisse du cours du contrat (100 − taux) : il achète des **options de vente**. Nombre : 20 000 000 / 1 000 000 = **20** ; valeur du point de base : 1 000 000 × 0,01 % × 3 / 12 = **25 €** ; prime totale : 20 × 0,12 × 100 × 25 = **6 000 €** (0,12 % × 20 000 000 × 3 / 12). Le prix d'exercice de 97,25 garantit un Euribor de 2,75 % au plus : le **taux maximal** de la première période est 2,75 % + 1,40 % + 0,12 % = **4,27 %**.

**Taux effectif de la première période (1 pt).**

| Au 30 novembre 2027 | Hausse : Euribor 3,40 % | Baisse : Euribor 2,20 % |
|---|---:|---:|
| Cours du contrat (100 − Euribor) | 96,60 | 97,80 |
| Décision | **exercice** (96,60 < 97,25) | **abandon** (97,80 > 97,25) |
| Gain : 20 × (97,25 − cours) × 100 × 25 | 20 × 0,65 × 100 × 25 = 32 500 € | 0 € |
| Résultat des options (gain − prime) | + 26 500 € | − 6 000 € |
| Intérêts : 20 000 000 × (Euribor + 1,40 %) × 3 / 12 | 240 000 € | 180 000 € |
| **Coût net** (intérêts − résultat) | **213 500 €** | **186 000 €** |
| **Taux effectif** : coût net / (20 000 000 × 3 / 12) | **4,27 %** | **3,72 %** |

Dans le scénario de hausse, le taux effectif atteint son maximum : 4,27 % au lieu de 4,80 % sans couverture. Dans le scénario de baisse, l'option est abandonnée et TRÉVALAC profite de la baisse, au coût de la prime (3,72 % au lieu de 3,60 %).

**Comparaison et recommandation (1 pt).**

| Critère | Emprunt terme contre terme (Banque DORNÉVAL) | Options de vente sur le contrat à terme Euribor 3 mois |
|---|---|---|
| Durée couverte | les trois ans du financement | la première période d'intérêts seulement (3 mois sur 36) |
| Taux obtenu | 4,10 % fixe, quels que soient les taux | 4,27 % au plus sur le trimestre ; 3,72 % si les taux baissent |
| Coût | pas de prime ; coût du portage de six mois (emprunt à 3,87 %, placement à 2,50 %) inclus dans le taux garanti | prime de 6 000 €, perdue si l'option n'est pas exercée |
| Souplesse | ferme : perte de 387 951 € si les taux baissent ; dénouement anticipé coûteux | conditionnelle : le gain de la baisse est conservé |
| Risque résiduel | contrepartie sur la banque, qui détient le placement ; dette brute et trésorerie gonflées de 19,75 M€ pendant six mois | les 33 mois suivants restent exposés ; risque de base si les dates du contrat et du prêt ne coïncident pas |
| Marché | gré à gré : sur mesure (montant, dates), moins transparent | marché organisé : contrats standardisés, liquides, chambre de compensation qui réduit fortement le risque de contrepartie ; l'acheteur d'options ne risque que sa prime |

Les deux couvertures ne protègent pas la même chose : l'emprunt terme contre terme fixe le coût de **tout** le financement, les options ne couvrent qu'**un trimestre**. Couvrir les trois ans par des options demanderait d'en acheter sur onze autres échéances, plus lointaines et moins liquides, avec une prime à chaque fois, sans connaître aujourd'hui leur prix. Recommandation : M. PERRIGOT craint la hausse, les marchés l'anticipent, et l'extension est un investissement de long terme qu'un financement à taux fixe adosse bien ; l'**emprunt terme contre terme** garantit 4,10 % sur trois ans, à 0,30 point seulement au-dessus du taux variable du jour, et protège de 590 192 € d'intérêts supplémentaires dans le scénario de hausse. Il fait renoncer à la baisse (387 951 € dans le scénario de baisse) : c'est le prix de la certitude. Les options sur le contrat à terme ne se justifieraient que si la direction doutait de la hausse et voulait seulement se protéger à court terme, en attendant de décider.

**Réponses tolérées** : taux garanti calculé avec les montants arrondis (4,10 %) ; remboursement de 22 562 238 € calculé avec le taux garanti arrondi ; gain ou perte calculé avec des intérêts annuels non capitalisés, si l'hypothèse est écrite (l'item 3.5-02 est alors acquis pour moitié) ; prime exprimée comme 0,12 % × 20 000 000 × 3 / 12 ; recommandation des options si elle est argumentée par une anticipation de baisse ou d'incertitude sur les taux et par la courte durée couverte ; taux effectif exprimé hors marge, si la marge est ajoutée ensuite.

**Erreurs fréquentes**
- Calculer le taux garanti en intérêts simples ((1 + 3,87 % × 3,5) / (1 + 2,50 % × 0,5) − 1) / 3 = 4,05 % : au-delà d'un an, l'annexe impose la capitalisation composée.
- Retenir le taux de l'emprunt (3,87 %) comme taux garanti, en oubliant le coût du portage de six mois.
- Acheter des options d'achat : le cours du contrat baisse quand les taux montent ; l'emprunteur achète des options de vente.
- Oublier le facteur 100 (gain de 325 € au lieu de 32 500 €) ou ajouter le résultat de l'option aux intérêts au lieu de le retrancher.
- Comparer un taux garanti de trois ans et un taux effectif d'un trimestre sans dire qu'ils ne couvrent pas la même durée.
- Confondre l'option sur le contrat à terme et la vente de contrats à terme (dans l'énoncé, l'acheteur d'options paie la prime au départ et ne subit pas d'appels de marge).

**Références** : F07 § 2.2 (emprunt terme contre terme : emprunter long et placer court), § 2.3 (options sur contrats à terme de taux, achat de puts par l'emprunteur) et § 2.4 (grille de choix d'une couverture) [V programme 6.2.b et 6.2.c ; guide p. 78] ; F01 (capitalisation composée au-delà d'un an) [V].

---

### 3.6 Nouvel acteur du financement des éleveurs et notation algorithmique (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Rôle : technologie financière qui accorde des crédits en ligne, sans agences ni dépôts, refinancée par un fonds de dette et par des cessions de prêts aux banques ; notation par apprentissage automatique sur les données de traite, de santé du troupeau et de livraison du lait, qui remplace en partie l'analyse des comptes et réduit l'asymétrie d'information (Akerlof, 1970) | 0,5 |
| 3.6-02 | Apports : réponse en 48 heures contre quatre à six semaines, sans apport ni caution ; information plus fraîche et plus fine que les comptes ; accès au crédit pour des éleveurs que les banques financent mal ; pour TRÉVALAC, vente plus rapide et financement intégré à l'offre | 0,5 |
| 3.6-03 | Erreurs et opacité : 27 % de refus, dont 46 % faute de deux ans de données (exploitations récentes, ou équipées par des concurrents) ; impayés de 2,1 % contre 1,4 % pour les banques ; modèle non explicable (pondération inconnue, trois variables seulement communiquées) ; notes procycliques quand le prix du lait baisse | 0,5 |
| 3.6-04 | Dépendance et usage des données : ressources fragiles (cessions de prêts arrêtables avec trois mois de préavis) ; dépendance de TRÉVALAC à un partenaire unique et aux données qu'il contrôle ; données des élevages conservées dix ans, utilisées pour d'autres fins (assureurs, acheteurs de lait), même agrégées ; données des robots de TRÉVALAC transmises chaque mois | 0,5 |
| 3.6-05 | Mise en mode limité du robot à distance : pression sur l'éleveur par le matériel, effet sur le suivi de la santé du troupeau et sur le bien-être animal, risque de réputation pour TRÉVALAC face aux acheteurs de lait ; parties prenantes (Freeman, 1984) ; à refuser ou à encadrer | 0,5 |
| 3.6-06 | Place face aux banques agricoles : complément plus que substitut (rapidité, niche du matériel connecté, données) ; les banques gardent la relation, la connaissance de l'éleveur, des ressources moins chères et la capacité de reporter les échéances en crise ; partenariat possible (les banques achètent déjà des prêts de PRAZELIA) | 0,5 |

**Rôle du nouvel acteur et de la notation (0,5 pt).** PRAZELIA Finance est une **technologie financière** (fintech) qui accorde des crédits en ligne aux exploitations agricoles. Elle n'a ni agences ni dépôts : elle se finance auprès d'un fonds de dette privée (55 %) et en cédant ses prêts à des banques (45 %). Son métier repose sur une **notation algorithmique** : un modèle d'apprentissage automatique attribue une note de 0 à 100 à partir de 240 variables tirées de l'activité réelle de l'élevage (litres par vache, fréquentation du robot, qualité du lait, boiteries, mammites, mortalité des veaux, livraisons et paiements de l'acheteur de lait), là où une banque lit surtout des comptes annuels, connus tard. Le prêteur réduit ainsi l'**asymétrie d'information** qui, selon Akerlof (1970), conduit à la sélection adverse et au rationnement du crédit : il observe presque en continu la capacité de l'exploitation à produire et à être payée.

**Apports (0,5 pt).** Pour l'éleveur : réponse en **48 heures** contre quatre à six semaines, ni apport ni caution personnelle, accès au crédit pour une exploitation bien gérée mais aux comptes peu lisibles. Pour TRÉVALAC : un financement proposé au moment de la vente, qui raccourcit le cycle commercial et peut faire acheter des éleveurs qui n'auraient pas investi ; un paiement en cinq jours (question 3.7). Pour le marché : une concurrence nouvelle pour les banques agricoles, qui peut faire baisser les délais et améliorer le service.

**Erreurs de notation et opacité (0,5 pt).** Un modèle qui apprend sur des données passées se trompe là où elles manquent : 27 % des demandes sont refusées, et 46 % des refus concernent des exploitations ayant moins de deux ans de données de traite, souvent celles qui viennent de s'installer ou qui s'équipent pour la première fois d'un robot, c'est-à-dire précisément les clients de TRÉVALAC. Les éleveurs équipés par des concurrents ou sans robot sont aussi mal notés. Les impayés de PRAZELIA (2,1 % des encours) dépassent ceux des banques (1,4 %) : la rapidité et l'absence de caution se paient par un risque plus élevé, que reflètent des taux de 5,40 % et 6,60 % contre 4,60 %. Le modèle est **opaque** : l'éleveur connaît sa note et trois variables, pas la pondération ; il ne peut ni comprendre un refus ni le contester, et des corrélations sans lien de cause (météo, acheteur de lait) peuvent pénaliser une exploitation saine. Enfin, la notation est **procyclique** : quand le prix du lait baisse, toutes les notes baissent en même temps, et le crédit se resserre au moment où les éleveurs en ont le plus besoin.

**Dépendance et usage des données des élevages (0,5 pt).** Les ressources de PRAZELIA sont fragiles : les banques peuvent cesser d'acheter ses prêts avec trois mois de préavis, et un fonds de dette peut se retirer si les taux montent ; l'offre de financement des clients de TRÉVALAC peut alors s'arrêter brutalement. TRÉVALAC deviendrait dépendante d'un **partenaire unique**, jeune (créé en 2021), dont elle ne maîtrise ni le modèle ni les décisions de refus, et qui détiendrait une partie de la relation avec ses clients. Quant aux données, PRAZELIA les conserve pendant le financement et dix ans après, les utilise pour améliorer son modèle et peut vendre des statistiques à des assureurs et à des acheteurs de lait : même agrégées, elles renseignent sur les performances et les coûts des élevages, ce qui peut se retourner contre les éleveurs dans leurs négociations. TRÉVALAC transmettrait chaque mois les données de ses robots : elle doit savoir à qui appartiennent ces données, pour quel usage elles sont transmises, et obtenir l'accord des éleveurs, sinon leur confiance dans la marque est en jeu.

**Mise en mode limité du robot à distance (0,5 pt).** La clause transforme le robot en instrument de pression sur l'éleveur en impayé. Même si la traite continue, désactiver le suivi de la santé du troupeau et le pilotage de l'alimentation peut retarder la détection des mammites ou des boiteries et dégrader le **bien-être animal**, alors que les acheteurs de lait en demandent des preuves (présentation). Pour TRÉVALAC, qui exécuterait la limitation, le risque de réputation est fort : auprès des éleveurs, des acheteurs de lait et du public. Au sens de la théorie des parties prenantes (Freeman, 1984), la clause sert le prêteur au détriment des éleveurs et des animaux. TRÉVALAC devrait la refuser, ou la limiter à des fonctions sans effet sur les animaux, avec une procédure de dialogue préalable.

**Place face aux banques agricoles (0,5 pt).** PRAZELIA est un **complément** plus qu'un substitut : elle vise une niche (le matériel connecté, qui produit des données) et gagne sur la rapidité et l'absence de garanties. Les banques agricoles gardent des avantages durables : la relation avec l'éleveur et la connaissance de son exploitation, des ressources stables et moins chères (les dépôts), des taux plus bas (4,60 %), et la capacité d'accompagner une crise par des reports d'échéances, comme lors de la dernière baisse du prix du lait. Les deux modèles se rapprochent déjà : deux banques achètent les prêts de PRAZELIA, qui fait l'origination et la notation pendant qu'elles portent le risque. Pour TRÉVALAC, l'enjeu est de ne pas dépendre d'un seul canal : proposer PRAZELIA à côté des banques, et non à leur place.

**Réponses tolérées** : référence à Spence (1973) ou à la théorie du signal pour les données transmises volontairement par l'éleveur ; analyse de la notation comme « boîte noire » ; mention des risques de cybersécurité sur les données des robots ; recommandation de négocier la suppression de la clause plutôt que de la refuser.

**Erreurs fréquentes**
- Confondre la notation algorithmique d'un prêteur avec le trading algorithmique ou à haute fréquence.
- Réciter les apports de l'intelligence artificielle en général, sans les chiffres du cas (délais, refus, impayés, taux) : `JUR-T13`.
- Présenter PRAZELIA comme une plateforme de financement participatif : elle prête sur ses ressources et cède ses prêts, sans collecter auprès du public.
- Développer le cadre juridique de l'usage des données ou des crédits : relève de l'UE 1.
- `JUR-M02` — le rôle des nouveaux acteurs du financement est attendu à partir du cas.

**Références** : F06 § 6 (fintechs, intelligence artificielle et notation de crédit : biais des données, opacité) [S ; programme 5.4.a et 5.4.b V] ; F10 (Akerlof, 1970 ; Freeman, 1984) [V programme 5.1 et 2.1].

---

### 3.7 Paiement à l'usage : coût, effet de la production, conditions pour TRÉVALAC (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.7-01 | Paiement annuel à la production de référence : 1 400 × 44 = **61 600 €** ; coût actuariel : 330 000 = 61 600 × [1 − (1 + t)^−7] / t, soit **t = 7,17 %** ; annuité du prêt bancaire de référence : 330 000 × 4,60 % / (1 − 1,046^−7) = **56 207 €** | 0,5 |
| 3.7-02 | Production − 20 % : 1 120 × 44 = **49 280 €** (au-dessus du minimum de 43 120 €) ; production − 35 % : 910 × 44 = 40 040 €, porté au **minimum de 43 120 €** ; le paiement suit les volumes, pas le prix du lait (10 % du prix à 440 €, 12,94 % à 340 €) | 0,5 |
| 3.7-03 | TRÉVALAC : montants financés 60 × 330 000 = 19 800 000 € ; commission **297 000 €** par an ; garantie maximale **990 000 €** ; baisse des créances clients 19 800 000 × 70 / 360 = **3 850 000 €** ; mise en place 0,40 M€ et six mois | 0,5 |
| 3.7-04 | Appréciation et recommandation : outil de financement qui partage le risque de volume avec l'éleveur, mais cher (7,17 % contre 4,60 %, 37 754 € de plus sur sept ans) et sans effet sur le risque de prix du lait ; pour TRÉVALAC, ventes et trésorerie contre commission, garantie et risque de réputation ; test limité, avec plusieurs financeurs, sans la clause de mise en mode limité | 0,5 |

**Pour l'éleveur (0,5 pt).**

| | Paiement à l'usage (PRAZELIA) | Prêt bancaire de référence |
|---|---:|---:|
| Paiement annuel à la production de référence | 1 400 000 / 1 000 × 44 = **61 600 €** | annuité **56 207 €** |
| Total sur sept ans | 431 200 € | 393 446 € |
| **Coût actuariel** | **7,17 %** | 4,60 % |

Le coût actuariel du paiement à l'usage se lit à la calculatrice : 330 000 / 61 600 = 5,3571 ; le facteur d'annuité de sept ans vaut 5,3893 à 7 % et 5,3519 à 7,20 %, d'où t ≈ 7,17 %. L'éleveur paie 37 754 € de plus sur sept ans qu'avec le prêt bancaire, mais sans apport ni caution.

**Effet de la production (0,5 pt).**

| Production annuelle | Paiement calculé | Paiement dû |
|---|---:|---:|
| 1 400 000 litres (référence) | 61 600 € | 61 600 € |
| 1 120 000 litres (− 20 %) | 49 280 € | **49 280 €** |
| 910 000 litres (− 35 %) | 40 040 € | **43 120 €** (minimum de 70 %) |

Si la production baisse (maladie du troupeau, sécheresse, réduction du cheptel), le paiement baisse avec elle jusqu'au minimum, et le manque n'est pas rattrapé : PRAZELIA porte une partie du **risque de volume**, ce qui explique en partie son coût. Si la production augmente (+ 10 % : 67 760 €), l'éleveur paie davantage, sans plafond. Mais le paiement ne dépend pas du **prix du lait** : à 440 € les 1 000 litres, il absorbe 10 % du produit du lait ; à 340 €, 12,94 %. Le risque principal des éleveurs, la baisse du prix du lait, n'est pas partagé.

**Pour TRÉVALAC (0,5 pt).** Sur 60 installations par an, les montants financés atteignent 19 800 000 €. TRÉVALAC verserait une commission de **297 000 €** par an et supporterait jusqu'à **990 000 €** de pertes sur impayés (garantie de premières pertes de 5 %) : avec un taux d'impayés de 2,1 %, la garantie serait vraisemblablement appelée en partie. En contrepartie, le paiement en cinq jours au lieu de 75 jours réduirait ses créances clients de **3 850 000 €**, soit environ 146 300 € d'intérêts économisés par an au taux du prêt variable du jour, 3,80 % (calcul facultatif), et lui apporterait des ventes que les éleveurs n'auraient pas faites sans ce financement. La mise en place coûte 0,40 M€ et six mois.

**Appréciation et recommandation (0,5 pt).** Le paiement à l'usage est un **nouvel outil de financement** qui adosse le remboursement à l'activité financée, comme les financements fondés sur les flux : il convient aux éleveurs dont la production est variable et qui n'ont ni apport ni caution, mais il est cher (7,17 % contre 4,60 %) et ne protège pas contre la baisse du prix du lait. Pour TRÉVALAC, il accélère les ventes et la trésorerie, mais il crée un risque de crédit (garantie), un coût certain (commission) et un risque de réputation (données, mode limité), et il la rend dépendante de PRAZELIA. Recommandation à Mme VESSONNAZ : tester la formule sur un nombre limité d'installations, en refusant la clause de mise en mode limité et en encadrant l'usage des données ; garder les banques agricoles comme premier financement des éleveurs, et proposer PRAZELIA en complément, pour les éleveurs qu'elles refusent ou qui ont besoin d'une réponse rapide ; demander une variante dans laquelle le montant par 1 000 litres baisserait avec le prix du lait, qui partagerait le vrai risque des éleveurs.

**Réponses tolérées** : coût actuariel encadré entre 7 % et 7,20 % ou obtenu par interpolation (7,17 % à 7,18 %) ; paiements mensuels mentionnés comme plus coûteux pour l'éleveur que des paiements de fin d'année ; baisse des créances exprimée en jours de chiffre d'affaires ; recommandation de refuser le partenariat si elle s'appuie sur le coût pour l'éleveur et sur les risques chiffrés pour TRÉVALAC.

**Erreurs fréquentes**
- Comparer les totaux payés (431 200 € et 393 446 €) sans calculer de taux : il faut un coût actuariel.
- Oublier le minimum annuel dans le scénario de baisse de 35 %.
- Présenter la formule comme un crédit-bail ou une location : l'éleveur est propriétaire des robots dès l'installation.
- Ne retenir pour TRÉVALAC que la commission, sans la garantie ni l'effet sur les créances clients.
- `JUR-T13` — appréciation générale, sans les données de l'exploitation type.

**Références** : F01 (taux actuariel, annuités constantes) [V programme 7.2.a] ; programme 7.2.c (nouveaux outils de financement : conditions d'accès, avantages, limites, coûts) [V guide p. 82] ; F06 § 6 (nouveaux acteurs du financement) [S].

---

**Points d'attention pour le correcteur**
- À la question 3.1, la convention de l'annexe 3.6 fixe la façon de modifier le cours ; un candidat qui applique 5 % à la contre-valeur obtient les mêmes effets et est noté en totalité.
- À la question 3.3, un cours à terme non arrondi donne un montant à terme et un cours d'égalité très proches (5 186 168 € ; 1,1359) : ils sont acceptés.
- À la question 3.4, l'énoncé demande l'effet de la hausse sur la valeur de la dette fixe : la réponse attendue est une baisse de valeur, favorable à l'emprunteur ; un candidat qui la présente comme une perte pour TRÉVALAC n'obtient que la moitié de l'item 3.4-02 (0,25), s'il explique correctement l'effet sur le prêt variable et la relation inverse valeur-taux.
- À la question 3.5, le taux garanti (taux actuariel de trois ans) et le taux effectif des options (taux d'un trimestre) ne couvrent pas la même durée : la comparaison doit le dire pour obtenir l'item 3.5-05 en totalité.
- Aux questions 3.6 et 3.7, aucune règle juridique de l'usage des données ou du crédit n'est attendue ; le raisonnement financier (asymétrie d'information, risque, coût, dépendance) est seul noté.
