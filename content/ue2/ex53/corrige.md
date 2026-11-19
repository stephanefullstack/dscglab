# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 53 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières et conventions, F07 risques de taux, de change, trésorerie, climat et matières premières, F09 éthique, conformité et cybersécurité, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (position de change par trimestre et totale, contre-valeurs et effet d'une baisse de 10 % du dollar, cours à terme, points de terme et montant de la vente à terme, prime, valeur intrinsèque, valeur temps et dénouement de l'option dans trois scénarios, FRA et contrats à terme sur Euribor dans trois scénarios, valeur, duration, sensibilité et variations de valeur de la dette à taux fixe, flux et coûts actuariels avant et après IS de l'emprunt et du crédit-bail, chiffrage de l'incident, indemnité, EBITDA, dette nette et clause financière, barème, liste noire, hors-programme ; clause d'indexation, termaillage, résultats des couvertures de change par rapport à l'absence de couverture et taux de couverture naturelle vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un montant de vente à terme calculé avec un cours à terme erroné à la question 2.3).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Position de change par trimestre et totale, sens du risque, effet d'une baisse de 10 % du dollar, couverture naturelle | `6.3.a` Caractériser la position de change courte ou longue, ouverte ou fermée | 1 |
| 2.2 Clause d'indexation selon trois cours, coût du règlement anticipé, risque résiduel | `6.3.c` Maîtriser les techniques internes et les garanties externes | 1,5 |
| 2.3 Cours à terme, vente à terme et option de vente de dollars selon trois cours, valeur intrinsèque et valeur temps, recommandation | `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) ; `6.3.d` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (change) | 3,5 |
| 2.4 FRA et contrats à terme sur Euribor 3 mois dans trois scénarios, gré à gré et marché organisé | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux ; `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) | 4,5 |
| 2.5 Valeur, duration et sensibilité de la dette à taux fixe, taux fixe ou taux variable couvert | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 1,5 |
| 2.6 Coût actuariel de l'emprunt et du crédit-bail, choix du financement des machines | `7.2.a` Comparer les sources de financement et notamment leurs coûts | 2,5 |
| 2.7 Préjudice du paiement détourné, EBITDA, dette nette et clause financière, acteurs publics, récupération des fonds, gouvernance | `2.2.e` Sensibiliser au risque d'attaque cyber et de récupération des flux financiers internationaux | 2,5 |
| **Total** | | **17** |

Part du calcul : environ 11,5 points (2.1-01, 2.1-03, 2.2-01, 2.2-02, 2.3-01 à 2.3-04, 2.4-01 à 2.4-05, 2.5-01, 2.5-02, 2.6-01, 2.6-02, 2.7-01, 2.7-02). Part de l'analyse : environ 5,5 points. La question 2.7, en fin de dossier, vaut 2,5 points dont la moitié est rédactionnelle : elle ne doit pas être sacrifiée faute de temps (`JUR-T15`).

---

### 2.1 Position de change par trimestre et totale, sens du risque, effet d'une baisse de 10 % du dollar, couverture naturelle (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Positions (M$) : T3 2027 **+ 6,40** ; T4 2027 **− 0,40** ; T1 2028 **+ 7,20** ; T2 2028 **+ 6,80** ; total **+ 20,00 M$** ; contre-valeur au comptant de 1,1200 : 5 714 286 € ; − 357 143 € ; 6 428 571 € ; 6 071 429 € ; total **17 857 143 €** | 0,5 |
| 2.1-02 | Caractérisation : positions **ouvertes** ; **longues** aux T3, T1 et T2 et sur la période (risque : **baisse du dollar**, hausse du cours EUR/USD) ; **courte** au T4 2027, à cause de l'outillage (risque : hausse du dollar sur ce trimestre) | 0,25 |
| 2.1-03 | Baisse de 10 % du dollar : cours 1,1200 / 0,90 = **1,2444** ; effet = **− 1 785 714 €** ; apport des achats en dollars, par exemple : ils ramènent l'exposition de 50,60 M$ à 20,00 M$ (couverture naturelle de 60,47 % des encaissements) | 0,25 |

**Position par trimestre (0,5 pt).** La position de change est la différence entre les encaissements et les décaissements en dollars d'une même échéance (F07 § 3.1). Les dollars encaissés servent d'abord à régler les achats en dollars : seule la position nette est vendue contre euros chaque trimestre et expose LANDRAVEL au risque de change.

| M$ | T3 2027 | T4 2027 | T1 2028 | T2 2028 | Total |
|---|---:|---:|---:|---:|---:|
| Encaissements (HAVERWICK + autres clients) | 11,20 | 12,60 | 13,40 | 13,40 | 50,60 |
| Décaissements (titane + outillage et autres) | 4,80 | 13,00 | 6,20 | 6,60 | 30,60 |
| **Position** | **+ 6,40** | **− 0,40** | **+ 7,20** | **+ 6,80** | **+ 20,00** |
| Contre-valeur au comptant de 1,1200 (€) | 5 714 286 | − 357 143 | 6 428 571 | 6 071 429 | **17 857 143** |

**Caractérisation (0,25 pt).** Aucune position n'est nulle : elles sont toutes **ouvertes**. LANDRAVEL est **longue en dollars** aux T3 2027, T1 et T2 2028 et sur l'ensemble de la période : elle détiendra plus de dollars qu'elle n'en doit et perd si le dollar baisse, c'est-à-dire si le cours EUR/USD (au certain) monte. Au T4 2027, le paiement de l'outillage (7,80 M$) rend la position **courte** de 0,40 M$ : sur ce trimestre seulement, c'est une hausse du dollar qui est défavorable. Ce risque est un risque de transaction, né de flux certains (contrat signé, commandes, contrats d'achat).

**Effet d'une baisse de 10 % du dollar et couverture naturelle (0,25 pt).** Une baisse de 10 % de la valeur du dollar porte le cours à 1,1200 / 0,90 = **1,2444**. La position totale ne vaudrait plus que 20 000 000 / 1,2444 = 16 071 429 €, soit une perte de **1 785 714 €** (10 % de la contre-valeur). Les achats de titane et d'outillage, payés avec les dollars encaissés, forment une **couverture naturelle** : 30,60 M$ sur 50,60 M$ d'encaissements, soit **60,47 %**. Sans eux, la position serait de 50,60 M$ et la même baisse coûterait 4,5 M€ environ. Cette couverture reste partielle : 20,00 M$ demeurent exposés, et l'outillage crée un décalage dans le temps (position courte au T4).

**Réponses tolérées** : contre-valeurs écrites en valeur absolue avec le sens indiqué ; effet calculé trimestre par trimestre puis additionné (même total) ; « position globalement longue » si la position courte du T4 est chiffrée ; l'item 2.1-02 n'est pas accordé si le T4 n'est pas qualifié.

**Erreurs fréquentes**
- Calculer la position sur les seuls encaissements de HAVERWICK (29,40 M$) ou sur les encaissements bruts, en oubliant la couverture naturelle par les achats.
- Inverser le sens du risque : au certain, une hausse du cours est une baisse du dollar ; un exportateur long en dollars craint cette hausse du cours.
- Appliquer la baisse de 10 % en multipliant le cours par 1,10 (cours de 1,2320, effet de − 1 623 377 €) au lieu de diviser par 0,90, comme le demande l'annexe 2.7.
- `JUR-T12` — connaissances de base insuffisantes (vocabulaire de la position) ; `JUR-T07` — absence de tableau.

---

### 2.2 Clause d'indexation selon trois cours, coût du règlement anticipé, risque résiduel (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Clause (facture de 8,00 M$) : cours 1,0080 : écart − 10 %, montant réduit de 2,50 %, **7,80 M$**, **7 738 095 €** (sans clause 7 936 508 €) ; cours 1,1480 : écart + 2,50 %, dans la bande, **8,00 M$**, **6 968 641 €** (identique) ; cours 1,2880 : écart + 15 %, montant relevé de 5 %, **8,40 M$**, **6 521 739 €** (sans clause 6 211 180 €, gain de 310 559 €) | 0,75 |
| 2.2-02 | Règlement à 30 jours : coût annuel = 0,40 % × 360 / 30 = **4,80 %**, contre 3,60 % pour le découvert : sur la facture de 6,00 M$ du T3, escompte de 24 000 $ (21 429 €) pour 16 007 € d'intérêts économisés | 0,25 |
| 2.2-03 | Appréciation et risque résiduel : la clause partage le risque au-delà de ± 5 % mais laisse à LANDRAVEL tout le risque dans la bande et la moitié au-delà, ne joue qu'à partir de 2028 et suppose l'accord de HAVERWICK (contre un geste sur les prix) ; le termaillage déplace l'échéance du risque sans réduire la position de 20,00 M$ et repose sur une anticipation ; une couverture de marché reste nécessaire | 0,5 |

**Clause d'indexation (0,75 pt).** L'indexation monétaire est une technique interne : le contrat prévoit lui-même un partage du risque de change entre le vendeur et l'acheteur (F07 § 3.2). L'écart se mesure par rapport au cours de référence de 1,1200 ; la bande de neutralité correspond aux cours compris entre 1,0640 et 1,1760.

| Cours du jour de la facture | 1,0080 (hausse du dollar) | 1,1480 | 1,2880 (baisse du dollar) |
|---|---:|---:|---:|
| Écart (cours / 1,1200 − 1) | − 10,00 % | + 2,50 % | + 15,00 % |
| Ajustement (moitié de l'écart au-delà de 5 %) | − 2,50 % | 0 | + 5,00 % |
| Montant facturé (M$) | **7,80** | **8,00** | **8,40** |
| Contre-valeur avec la clause (€) | **7 738 095** | **6 968 641** | **6 521 739** |
| Contre-valeur sans la clause (8,00 M$ / cours) (€) | 7 936 508 | 6 968 641 | 6 211 180 |
| Effet de la clause (€) | − 198 413 | 0 | **+ 310 559** |

Au cours de référence, la facture vaudrait 7 142 857 €. Si le dollar baisse fortement (1,2880), la perte de change par rapport à ce montant passe de 931 677 € sans clause à 621 118 € avec la clause : HAVERWICK en supporte un tiers, la partie qui dépasse la bande étant partagée par moitié. En contrepartie, si le dollar monte fortement (1,0080), LANDRAVEL rétrocède à HAVERWICK 198 413 € du gain de change. Dans la bande (1,1480), la clause ne joue pas : la perte de 174 216 € par rapport au cours de référence reste à LANDRAVEL.

**Termaillage (0,25 pt).** Le règlement à 30 jours au lieu de 60 avance l'encaissement de 30 jours ; son coût annuel est 0,40 % × 360 / 30 = **4,80 %**, supérieur au coût du découvert (3,60 %). Sur la facture de 6,00 M$ du troisième trimestre, l'escompte coûte 24 000 $, soit 21 429 € au comptant, alors que les euros obtenus plus tôt n'économisent que 6 000 000 × (1 − 0,40 %) / 1,1200 × 3,60 % × 30 / 360 = 16 007 € d'intérêts : coût net d'environ 5 421 €. Cet avancement ne se justifie que si LANDRAVEL anticipe une baisse du dollar de plus de 0,1 % environ en un mois. Le paiement du titane à 90 jours, sans pénalité, est gratuit : il permet de retarder des sorties de dollars si le dollar est attendu en baisse, ou de rapprocher dans le temps décaissements et encaissements (par exemple pour atténuer la position courte du T4 2027).

**Appréciation et risque résiduel (0,5 pt).**
- La clause transfère une partie du risque à HAVERWICK sans coût financier, mais elle se négocie : HAVERWICK demande un geste sur les prix, qui est le coût caché de la clause. Elle laisse à LANDRAVEL la totalité des variations jusqu'à 5 % (jusqu'à 340 000 € environ par facture de 8,00 M$) et la moitié au-delà ; elle ne couvre ni les factures de 2027, ni la variation du cours entre la facture et son règlement à 60 jours, ni les ventes aux autres clients en dollars ; elle est symétrique et prive LANDRAVEL d'une partie des gains.
- Le termaillage ne réduit pas la position de 20,00 M$ : il en déplace l'échéance de quelques semaines et repose sur une anticipation du cours, ce qui en fait un pari plus qu'une couverture ; il dépend aussi de l'accord des partenaires et peut tendre la relation commerciale.
- Ces techniques internes, peu coûteuses, viennent en premier, mais le risque résiduel appelle une couverture de marché pour les échéances proches (question 2.3), dont le volume diminuera si HAVERWICK accepte la clause.

**Réponses tolérées** : contre-valeurs arrondies au millier d'euros ; coût net du règlement anticipé non calculé si le coût annuel est comparé au découvert ; appréciation de la clause rapportée au chiffre d'affaires en dollars plutôt qu'à une facture.

**Erreurs fréquentes**
- Appliquer la moitié de l'écart total (7,50 % au lieu de 5 % à 1,2880) au lieu de la seule part qui dépasse la bande.
- Relever le montant facturé quand le dollar monte : la clause protège LANDRAVEL d'une baisse du dollar et rétrocède une partie du gain si le dollar monte.
- Présenter le termaillage comme une couverture de la position totale.
- `JUR-T13` — techniques décrites sans lien avec le contrat HAVERWICK ; `JUR-T02` — absence de conclusion opérationnelle.

---

### 2.3 Cours à terme, vente à terme et option de vente de dollars selon trois cours, valeur intrinsèque et valeur temps, recommandation (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Cours à terme = 1,1200 × (1 + 3,84 % × 150 / 360) / (1 + 2,40 % × 150 / 360) = 1,1200 × 1,016 / 1,010 = **1,1267** ; points de terme **+ 67** ; l'euro est en **report** (le dollar en déport) parce que le taux du dollar dépasse celui de l'euro | 0,5 |
| 2.3-02 | Vente à terme de 6,40 M$ : **5 680 305 €** garantis ; sans couverture : 6 095 238 € ; 5 714 286 € ; 5 333 333 € ; résultat de la vente à terme : **− 414 933 €** (1,0500) ; **− 33 980 €** (1,1200) ; **+ 346 972 €** (1,2000) | 0,75 |
| 2.3-03 | Prime = 2,40 % × 6 400 000 = 153 600 $, soit **137 143 €** ; valeur intrinsèque = 6 400 000 / 1,1100 − 6 400 000 / 1,1200 = **51 480 €** ; valeur temps = **85 663 €** ; interprétation | 0,75 |
| 2.3-04 | Option : à 1,0500, **abandon**, 6 095 238 €, net **5 958 095 €**, résultat **− 137 143 €** ; à 1,1200 et 1,2000, **exercice** à 1,1100, 5 765 766 €, net **5 628 623 €**, résultats **− 85 663 €** et **+ 295 290 €** | 0,75 |
| 2.3-05 | Comparaison (minimum garanti 5 628 623 € contre 5 680 305 €, soit 51 682 € de moins ; par exemple : l'option ne fait mieux que si le cours tombe sous **1,1001** ; flux certain) et recommandation : **vente à terme** de la position du T3 | 0,75 |

**Cours à terme (0,5 pt).** Par la parité des taux d'intérêt, un dollar placé 150 jours à 3,84 % et un euro placé à 2,40 % doivent donner le même résultat une fois convertis : le cours à terme compense l'écart de taux (F07 § 3.3).

F = 1,1200 × (1 + 0,0384 × 150 / 360) / (1 + 0,0240 × 150 / 360) = 1,1200 × 1,016 / 1,010 = 1,126653, arrondi à **1,1267**.

Points de terme = (1,1267 − 1,1200) × 10 000 = **+ 67**. Au certain, le cours à terme est supérieur au cours comptant : il faut plus de dollars pour un euro à terme qu'au comptant ; l'euro est en **report** et le dollar en **déport**, parce que le taux d'intérêt du dollar est plus élevé que celui de l'euro.

**Vente à terme (0,75 pt).** LANDRAVEL vend à terme les 6 400 000 $ de la position nette du troisième trimestre (et non les 11,20 M$ d'encaissements bruts, en partie compensés par les achats) : elle recevra 6 400 000 / 1,1267 = **5 680 305 €** le 30 septembre 2027, quel que soit le cours.

| Cours au 30/09/2027 | 1,0500 | 1,1200 | 1,2000 |
|---|---:|---:|---:|
| Sans couverture : 6 400 000 / cours (€) | 6 095 238 | 5 714 286 | 5 333 333 |
| Vente à terme (€) | 5 680 305 | 5 680 305 | 5 680 305 |
| **Résultat de la vente à terme** (€) | **− 414 933** | **− 33 980** | **+ 346 972** |

Le résultat est un manque à gagner si le dollar monte et un gain si le dollar baisse. Par rapport au comptant du jour (5 714 286 €), la vente à terme coûte 33 980 € : ce n'est pas une perte de change, c'est le report, c'est-à-dire l'écart de taux d'intérêt entre le dollar et l'euro sur 150 jours.

**Prime, valeur intrinsèque et valeur temps (0,75 pt).** L'option de vente de dollars (achat d'euros) au prix d'exercice de 1,1100 garantit à LANDRAVEL de vendre ses dollars au moins à ce cours.
- Prime : 2,40 % × 6 400 000 = 153 600 $, soit 153 600 / 1,1200 = **137 143 €**, payée le 3 mai 2027.
- Valeur intrinsèque : exercée aujourd'hui, l'option donnerait 6 400 000 / 1,1100 = 5 765 766 € au lieu de 6 400 000 / 1,1200 = 5 714 286 € au comptant, soit **51 480 €** : l'option est **dans la monnaie**, son prix d'exercice étant plus favorable que le cours comptant.
- Valeur temps : 137 143 − 51 480 = **85 663 €**. Elle rémunère le vendeur de l'option pour la possibilité que le dollar baisse encore d'ici l'échéance ; elle diminue à mesure que l'échéance approche et devient nulle le 30 septembre 2027. La prime est donnée par la banque : elle n'a pas à être calculée.

**Dénouement de l'option (0,75 pt).** LANDRAVEL exerce l'option si le cours constaté est supérieur au prix d'exercice (dollar plus faible que 1,1100) et l'abandonne sinon.

| Cours au 30/09/2027 | 1,0500 | 1,1200 | 1,2000 |
|---|---:|---:|---:|
| Décision | abandon | exercice | exercice |
| Montant encaissé (€) | 6 095 238 | 5 765 766 | 5 765 766 |
| **Montant net de la prime** (€) | **5 958 095** | **5 628 623** | **5 628 623** |
| **Résultat par rapport à l'absence de couverture** (€) | **− 137 143** | **− 85 663** | **+ 295 290** |

**Comparaison et recommandation (0,75 pt).**
- L'option garantit un minimum de 5 628 623 € (cours effectif de 6 400 000 / 5 628 623 = 1,1370), inférieur de **51 682 €** au montant de la vente à terme ; en contrepartie, elle laisse à LANDRAVEL le gain d'une hausse du dollar (5 958 095 € à 1,0500, soit 277 790 € de plus que le terme). Elle ne fait mieux que le terme que si le cours tombe sous 6 400 000 / (5 680 305 + 137 143) = **1,1001**, c'est-à-dire si le dollar s'apprécie de plus de 1,8 % environ.
- La vente à terme est gratuite, simple et ferme ; elle convient à un flux **certain** : la position du troisième trimestre résulte de factures et d'achats déjà engagés. L'option, coûteuse, est adaptée à un flux incertain ou à une direction qui veut garder une chance de gain.
- **Recommandation** : vendre à terme les 6,40 M$ du troisième trimestre. L'option pourrait être réservée aux positions de 2028, tant que la réponse de HAVERWICK sur la clause d'indexation n'est pas connue. Les deux instruments sont négociés de gré à gré avec la Banque SOLVÈDRE : ils l'exposent au risque de défaillance de la banque et ne se revendent pas facilement avant l'échéance.

**Réponses tolérées** : cours à terme non arrondi (1,126653, montant de 5 680 540 €, notés si la convention est rappelée) ; décomposition de la prime en dollars (valeur intrinsèque de 57 658 $ calculée au comptant) si l'idée est juste ; résultats présentés par rapport au comptant du jour plutôt qu'à l'absence de couverture à l'échéance, s'ils sont annoncés comme tels ; recommandation de l'option argumentée par une anticipation explicite de hausse du dollar.

**Erreurs fréquentes**
- Couvrir les encaissements bruts (11,20 M$) au lieu de la position nette (6,40 M$) : sur-couverture.
- Inverser la formule de parité (cours à terme de 1,1134) ou qualifier l'euro de « en déport ».
- Exercer l'option de vente quand le dollar monte : à 1,0500, le marché donne plus que le prix d'exercice.
- Calculer la valeur intrinsèque par rapport au cours à terme, contrairement à la convention de l'annexe 2.7, ou chercher à valoriser l'option : la prime est donnée.
- Oublier la prime dans le montant net, ou la compter deux fois dans la comparaison.
- `JUR-T07` — absence de tableau par scénario ; `JUR-T02` — calculs sans recommandation.

---

### 2.4 FRA et contrats à terme sur Euribor 3 mois dans trois scénarios, gré à gré et marché organisé (4,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Sans couverture : intérêts = 10 000 000 × (taux constaté + 1,20 %) × 90 / 360 = **120 000 €**, **100 000 €** et **80 000 €**, soit un taux de l'emprunt de 4,80 %, 4,00 % et 3,20 % | 0,5 |
| 2.4-02 | FRA acheté ; différentiel réglé le 2 novembre et actualisé : 10 000 000 × (Euribor − 2,90 %) × 90 / 360 / (1 + Euribor × 90 / 360) = **+ 17 343,90 €** (reçu) ; **− 2 482,62 €** et **− 22 388,06 €** (versés) | 0,75 |
| 2.4-03 | Coût net avec le FRA (différentiel capitalisé jusqu'au 31 janvier) : **102 500 €** dans les trois scénarios ; taux effectif **4,10 %** = 2,90 % + 1,20 % | 0,5 |
| 2.4-04 | Contrats à terme : **vente** de **10 contrats** (10 000 000 × 3 / 3 / 1 000 000) ; valeur du point de base = 1 000 000 × 0,01 % × 3 / 12 = **25 €** ; taux garanti 100 − 97,15 = **2,85 %** | 0,5 |
| 2.4-05 | Résultat sur les contrats : **+ 18 750 €** (cours 96,40) ; **− 1 250 €** (97,20) ; **− 21 250 €** (98,00) ; coût net **101 250 €** dans les trois scénarios ; taux effectif **4,05 %** | 0,75 |
| 2.4-06 | Gré à gré et marché organisé : FRA sur mesure (montant, dates), sans décaissement avant le règlement, mais risque de défaillance de la banque et instrument difficile à céder ; contrats standardisés, liquides, chambre de compensation (pas de risque de contrepartie), mais dépôt de garantie (5 000 €), appels de marge quotidiens, montant et échéance imposés, risque de base | 1 |
| 2.4-07 | Recommandation argumentée : par exemple le **FRA** (coût supérieur de 1 250 € seulement, pas d'appels de marge en 2027, dates identiques à celles du prêt), en rappelant que les deux ne couvrent que la première période | 0,5 |

**Sans couverture (0,5 pt).** LANDRAVEL empruntera à taux variable dans six mois : elle craint une **hausse** de l'Euribor 3 mois (F07 § 2.1). Intérêts de la première période (90 jours) :

| Euribor constaté le 2/11/2027 | 3,60 % | 2,80 % | 2,00 % |
|---|---:|---:|---:|
| Intérêts sans couverture (€) | 120 000 | 100 000 | 80 000 |
| Taux de l'emprunt | 4,80 % | 4,00 % | 3,20 % |

**FRA (1,25 pt).** LANDRAVEL **achète** le FRA : elle reçoit le différentiel si l'Euribor constaté dépasse le taux garanti de 2,90 % et le verse dans le cas contraire. Le prêt lui-même reste conclu au taux du marché ; le FRA ne porte que sur la différence de taux (F07 § 2.2). Le différentiel est réglé le 2 novembre 2027, au début de la période : il est actualisé au taux constaté sur 90 jours.

| Euribor constaté | 3,60 % | 2,80 % | 2,00 % |
|---|---:|---:|---:|
| Différentiel en fin de période : 10 000 000 × (Euribor − 2,90 %) × 90 / 360 (€) | + 17 500,00 | − 2 500,00 | − 22 500,00 |
| **Différentiel réglé le 2 novembre**, actualisé (€) | **+ 17 343,90** | **− 2 482,62** | **− 22 388,06** |
| Intérêts du prêt (€) | 120 000 | 100 000 | 80 000 |
| **Coût net** (différentiel capitalisé au 31 janvier) (€) | **102 500** | **102 500** | **102 500** |
| **Taux effectif** | **4,10 %** | **4,10 %** | **4,10 %** |

Le différentiel reçu le 2 novembre, placé (ou venant réduire le découvert) au taux constaté jusqu'au 31 janvier, retrouve sa valeur en fin de période : 17 343,90 × (1 + 3,60 % × 90 / 360) = 17 500 €. Quel que soit l'Euribor, LANDRAVEL paie le taux garanti plus sa marge : 2,90 % + 1,20 % = 4,10 %. Elle ne profite pas d'une baisse des taux : à 2,00 %, elle verse 22 388,06 €.

**Contrats à terme sur Euribor 3 mois (1,25 pt).** Le contrat est coté 100 − taux : son cours baisse quand les taux montent. Pour se protéger d'une hausse, l'emprunteur **vend** des contrats aujourd'hui et les rachète le 2 novembre ; le gain sur les contrats compense le surcoût des intérêts (F07 § 2.2).
- Nombre de contrats : 10 000 000 × (3 / 3) / 1 000 000 = **10 contrats**, sans arrondi.
- Valeur d'un point de base : 1 000 000 × 0,01 % × 3 / 12 = **25 €** par contrat.
- Taux garanti par le cours de 97,15 : 100 − 97,15 = **2,85 %**.

| Euribor constaté | 3,60 % | 2,80 % | 2,00 % |
|---|---:|---:|---:|
| Cours de rachat (100 − Euribor) | 96,40 | 97,20 | 98,00 |
| Variation en points de base (97,15 − cours) × 100 | + 75 | − 5 | − 85 |
| **Résultat sur les 10 contrats** (× 25 € × 10) (€) | **+ 18 750** | **− 1 250** | **− 21 250** |
| **Coût net** = intérêts − résultat (€) | **101 250** | **101 250** | **101 250** |
| **Taux effectif** | **4,05 %** | **4,05 %** | **4,05 %** |

Le taux effectif est 2,85 % + 1,20 % = 4,05 %. Les appels de marge sont réglés au jour le jour pendant six mois : si les taux baissent, LANDRAVEL verse progressivement jusqu'à 21 250 € avant le tirage du prêt, en plus du dépôt de garantie de 10 × 500 = 5 000 €, qui lui est rendu au dénouement.

**Gré à gré et marché organisé (1 pt).**

| Critère | FRA (gré à gré) | Contrats à terme (marché organisé) |
|---|---|---|
| Adaptation | sur mesure : nominal, dates et taux de référence identiques à ceux du prêt | contrats standardisés : 1 000 000 €, échéance de décembre ; le montant tombe juste ici, mais l'échéance diffère du tirage |
| Coût | taux garanti 2,90 % : 4,10 % effectif, soit 1 250 € de plus par période | taux de 2,85 % : 4,05 % effectif |
| Trésorerie | aucun décaissement avant le 2 novembre | dépôt de garantie de 5 000 €, appels de marge quotidiens (jusqu'à 21 250 € si les taux baissent) |
| Risques | défaillance de la banque ; instrument difficile à céder avant l'échéance | pas de risque de contrepartie (chambre de compensation) ; risque de base : avant l'échéance de décembre, le cours du contrat peut s'écarter de 100 − Euribor constaté (l'annexe le néglige) |
| Souplesse | dénouement anticipé à négocier avec la banque | position revendable à tout moment sur un marché liquide |

**Recommandation (0,5 pt).** Les deux couvertures fixent le coût de la première période à 4,05 % ou 4,10 %. Le FRA coûte 1 250 € de plus, mais il épouse exactement le prêt, évite la gestion quotidienne des appels de marge et le risque de base, et n'immobilise pas de trésorerie en 2027, année où LANDRAVEL finance la ligne et supporte le paiement détourné (question 2.7). Pour une opération unique, le **FRA** est la solution la plus simple ; les contrats à terme se justifieraient si LANDRAVEL suivait déjà des positions sur un marché organisé. Dans les deux cas, seule la première période est couverte : les dix-neuf périodes suivantes du prêt restent exposées (question 2.5).

**Réponses tolérées** : différentiel du FRA calculé en fin de période (17 500 €) si l'actualisation est mentionnée ou si le candidat indique explicitement la convention retenue (0,5 sur 0,75 pour 2.4-02) ; taux effectifs présentés comme « taux garanti + marge » sans calcul détaillé, s'ils sont justifiés par un scénario au moins ; recommandation des contrats à terme justifiée par leur coût moindre et l'absence de risque de contrepartie.

**Erreurs fréquentes**
- Acheter les contrats à terme : l'emprunteur qui craint une hausse des taux vend des contrats, dont le cours baisse quand les taux montent.
- Calculer le résultat des contrats sur le nominal (10 000 000 × 0,75 %) sans le prorata de trois mois (75 000 € au lieu de 18 750 €).
- Inverser le sens du différentiel du FRA, ou oublier que le prêt reste conclu au taux du marché.
- Ajouter la marge de 1,20 % au différentiel du FRA ou au résultat des contrats.
- `JUR-T12` — mécanismes mal connus ; `JUR-T07` — absence de tableau par scénario.

---

### 2.5 Valeur, duration et sensibilité de la dette à taux fixe, taux fixe ou taux variable couvert (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Valeur au 2 novembre 2027 = **10 000 000 €** (taux du prêt = taux du marché) ; duration = **4,621 ans** ; sensibilité = − 4,621 / 1,041 = **− 4,439** | 0,5 |
| 2.5-02 | Variation estimée par la sensibilité : **+ 443 934 €** (baisse d'un point) et **− 443 934 €** (hausse) ; variation exacte en cas de baisse : **+ 456 666 €** (valeur 10 456 666 €) ; la variation exacte en cas de hausse (− 431 753 €) est un complément non exigé | 0,5 |
| 2.5-03 | Relation inverse et implications : la valeur de la dette monte quand les taux baissent (perte d'opportunité, indemnité de remboursement anticipé qui reprend la hausse de valeur) ; taux fixe = coût certain de 410 000 € par an, protection de la clause financière, renonciation à une baisse ; taux variable couvert = première période seulement, puis 100 000 € par an (75 000 € après IS) par point de hausse, sauf couverture de toute la durée | 0,5 |

**Valeur, duration et sensibilité (0,5 pt).** La valeur de la dette est la valeur actuelle des flux qui restent à payer, au taux du marché (F07 § 2.1). Flux : 410 000 € d'intérêts par an de 2028 à 2032, plus 10 000 000 € en 2032. Au taux du marché de 4,10 %, égal au taux du prêt, la valeur est de **10 000 000 €**.

| Année | Flux (€) | Flux actualisé à 4,10 % (€) | t × flux actualisé (€) |
|---|---:|---:|---:|
| 1 | 410 000 | 393 852 | 393 852 |
| 2 | 410 000 | 378 340 | 756 680 |
| 3 | 410 000 | 363 439 | 1 090 317 |
| 4 | 410 000 | 349 125 | 1 396 500 |
| 5 | 10 410 000 | 8 515 244 | 42 576 219 |
| **Total** | | **10 000 000** | **46 213 568** |

Duration = 46 213 568 / 10 000 000 = **4,621 ans** ; sensibilité = − 4,621 / 1,041 = **− 4,439** : la valeur de la dette varie d'environ 4,44 % en sens inverse d'une variation d'un point du taux du marché.

**Variations de valeur (0,5 pt).**

| Taux du marché juste après le tirage | 3,10 % (baisse d'un point) | 5,10 % (hausse d'un point) |
|---|---:|---:|
| Variation estimée = − 4,439 × Δr × 10 000 000 (€) | + 443 934 | − 443 934 |
| Valeur recalculée (€) | 10 456 666 | 9 568 247 |
| Variation exacte (€) | **+ 456 666** | − 431 753 (complément, non exigé) |

L'écart entre la variation estimée et la variation exacte vient de ce que la relation entre la valeur et le taux n'est pas linéaire ; la sensibilité n'en donne qu'une approximation, suffisante pour de petites variations.

**Relation inverse et implications pour LANDRAVEL (0,5 pt).**
- **Relation inverse** : quand les taux du marché baissent, les flux fixes de la dette valent plus ; quand ils montent, ils valent moins. Pour un emprunteur, une baisse des taux après la signature est une **perte d'opportunité** : LANDRAVEL paierait 4,10 % alors que le marché offrirait 3,10 %, et rembourser par anticipation pour se refinancer lui coûterait une indemnité égale à cette hausse de valeur des flux restants (456 666 € si le remboursement était possible aussitôt ; il ne l'est qu'aux dates anniversaires : environ 370 823 € au 2 novembre 2028 si le taux reste à 3,10 %), qui annule l'intérêt du refinancement. Une hausse des taux est au contraire un gain d'opportunité (la dette vaut 9 568 247 €).
- **Taux fixe** : coût certain de 410 000 € par an pendant cinq ans (4,10 %, proche des 4,05 % à 4,10 % de la première période couverte), budget et clause financière à l'abri d'une hausse des taux ; LANDRAVEL renonce à une baisse et perd de la souplesse (remboursement anticipé coûteux si les taux baissent).
- **Taux variable couvert par le FRA ou les contrats à terme** : seule la première période de trois mois est couverte ; sur les quatre ans et neuf mois suivants, chaque point de hausse de l'Euribor coûterait 10 000 000 × 1 % = **100 000 €** par an, soit 75 000 € après IS, alors que la marge sous la clause financière est déjà étroite (question 2.7). Pour obtenir la même protection que le taux fixe, il faudrait couvrir toute la durée du prêt (série de FRA ou de contrats à terme, contrat d'échange de taux), ce qui reviendrait, au coût près, à un taux fixe. Le taux variable garde l'avantage de faire profiter LANDRAVEL d'une baisse des taux après la première période ; l'annexe ne prévoit pas pour lui d'indemnité de remboursement anticipé.

**Réponses tolérées** : duration calculée par la formule d'une obligation in fine ; variations exprimées en pourcentage (+ 4,57 % et − 4,32 % pour les variations exactes) ; préférence motivée pour le taux variable si le candidat anticipe une baisse des taux et accepte le risque.

**Erreurs fréquentes**
- Écrire une sensibilité positive ou confondre duration (en années) et sensibilité.
- Présenter la hausse de la valeur de la dette comme un gain pour LANDRAVEL : c'est le prêteur qui gagne quand les taux baissent.
- Croire que le FRA couvre les cinq ans du prêt.
- `JUR-T12` — relation valeur-taux mal maîtrisée ; `JUR-T13` — implications non rapportées au cas.

---

### 2.6 Coût actuariel de l'emprunt et du crédit-bail, choix du financement des machines (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Emprunt : flux après IS 11,91 ; − 2,778 ; − 2,7024 ; − 2,6268 ; − 2,5512 ; − 2,4756 → coût **3,42 %** | 0,75 |
| 2.6-02 | Crédit-bail : loyer net d'IS 2,055 + économie d'IS perdue sur les amortissements 0,60 = 2,655 par an ; 12,00 ; − 2,655 (années 1 à 4) ; − 2,775 → coût **3,76 %** | 0,75 |
| 2.6-03 | Comparaison : l'emprunt coûte 0,34 point de moins après IS ; critères qualitatifs : propriété et nantissement, absence de garantie et simplicité du crédit-bail, même effet sur l'endettement retenu par la clause financière, perte des économies d'IS sur les amortissements | 0,5 |
| 2.6-04 | Recommandation argumentée : par exemple l'**emprunt**, moins coûteux, le nantissement des machines étant acceptable ; le crédit-bail se justifie si LANDRAVEL veut préserver ses garanties | 0,5 |

**Emprunt (0,75 pt).** Le coût actuariel est le taux qui égalise les fonds reçus et la valeur actuelle des décaissements (F01 § 3). Avec des amortissements constants de 12,00 / 5 = 2,40 M€ :

| M€ | 0 (3/04/2028) | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|---:|
| Capital restant dû en début d'année | | 12,00 | 9,60 | 7,20 | 4,80 | 2,40 |
| Intérêts (4,20 %) | | 0,504 | 0,4032 | 0,3024 | 0,2016 | 0,1008 |
| Fonds reçus nets de frais (12,00 − 0,12) | 11,88 | | | | | |
| Échéance (intérêts + 2,40) | | − 2,904 | − 2,8032 | − 2,7024 | − 2,6016 | − 2,5008 |
| Économie d'IS (frais en 0, puis intérêts) | + 0,03 | + 0,126 | + 0,1008 | + 0,0756 | + 0,0504 | + 0,0252 |
| **Flux après IS** | **11,91** | **− 2,778** | **− 2,7024** | **− 2,6268** | **− 2,5512** | **− 2,4756** |

Coût après IS : **3,42 %**. En complément, non exigé : coût avant IS de 4,57 % (flux 11,88 ; − 2,904 ; − 2,8032 ; − 2,7024 ; − 2,6016 ; − 2,5008), les frais de 1 % relevant le taux nominal de 4,20 %.

**Crédit-bail (0,75 pt).** Le crédit-bail évite à LANDRAVEL de décaisser 12,00 M€ : c'est le montant financé. Les loyers sont déductibles, mais LANDRAVEL, qui n'est pas propriétaire, perd les économies d'IS sur les amortissements que l'achat aurait procurées : 12,00 / 5 × 25 % = 0,60 M€ par an.

| M€ | 0 | 1 à 4 | 5 |
|---|---:|---:|---:|
| Montant financé | 12,00 | | |
| Loyers (et option d'achat en année 5) | | − 2,74 | − 2,74 − 0,12 = − 2,86 |
| Économie d'IS sur les loyers (25 %) | | + 0,685 | + 0,685 |
| Économie d'IS perdue sur les amortissements | | − 0,60 | − 0,60 |
| **Flux après IS** | **12,00** | **− 2,655** | **− 2,775** |

Coût après IS : **3,76 %**. En complément, non exigé : coût avant IS de 4,87 % (flux 12,00 ; − 2,74 pendant quatre ans ; − 2,86).

**Comparaison (0,5 pt).**
- **Coût** : l'emprunt est moins cher de **0,34 point** après IS (0,30 point avant IS) ; une part de l'écart vient de la perte des économies d'IS sur les amortissements, qui pèse sur le crédit-bail.
- **Garanties et propriété** : l'emprunt rend LANDRAVEL propriétaire des machines dès 2028, mais elles sont nanties au profit de la banque ; le crédit-bail ne demande ni apport ni garantie, le bailleur restant propriétaire jusqu'à la levée de l'option (0,12 M€). Les deux financent 100 % des machines.
- **Structure financière** : la Banque SOLVÈDRE inclut l'un comme l'autre dans l'endettement financier net retenu par la clause financière : le crédit-bail n'allège pas le ratio surveillé par la banque.
- **Souplesse** : le crédit-bail est simple à mettre en place et attaché au bien ; l'emprunt peut être accompagné d'autres garanties ou renégocié avec la banque principale de LANDRAVEL.

**Recommandation (0,5 pt).** L'emprunt est la solution la moins coûteuse, avec un effet identique sur le ratio de la clause financière ; le nantissement des machines est une contrainte acceptable pour des équipements dédiés au contrat HAVERWICK. Mme ARVÉSIS peut retenir l'**emprunt**. Le crédit-bail ne se justifierait que si LANDRAVEL voulait garder les machines libres de toute garantie pour d'autres financements, en payant 0,34 point de plus.

**Réponses tolérées** : coûts arrondis à 0,1 point près s'ils sont obtenus par interpolation ; économie d'IS sur les frais étalée si l'hypothèse est écrite (coût après IS proche de 3,43 %) ; recommandation du crédit-bail si elle est argumentée par l'absence de garantie et le maintien de la capacité d'emprunt, et si l'écart de coût est reconnu.

**Erreurs fréquentes**
- Oublier la perte des économies d'IS sur les amortissements dans le crédit-bail : les loyers nets d'IS (10,40 M€ au total, option comprise) seraient inférieurs aux 12,00 M€ financés et le coût après IS deviendrait négatif, ce qui doit alerter le candidat.
- Compter les frais de dossier comme un décaissement de fin d'année ou oublier qu'ils réduisent les fonds reçus.
- Calculer des annuités constantes alors que l'emprunt est remboursé par amortissements constants (`JUR-T04`).
- Présenter le crédit-bail comme un financement « hors dette » : l'annexe 2.5 indique que la banque l'inclut dans l'endettement.
- `JUR-T13` — comparaison limitée au coût, sans critère propre au cas.

---

### 2.7 Préjudice du paiement détourné, EBITDA, dette nette et clause financière, acteurs publics, récupération des fonds, gouvernance (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Chiffrage (M€) : détourné 3,30 M$ / 1,1000 = 3,00 ; récupéré 1,00 ; **non récupéré 2,00** (2,20 M$) ; coûts 0,18 + 0,07 + 0,05 + 0,02 = 0,32 ; coût total **2,32** ; base assurée 2,00 + 0,18 = 2,18 ; 2,18 − 0,25 = 1,93 > plafond → **indemnité 1,20** ; **perte nette 1,12** | 0,75 |
| 2.7-02 | Effets : EBITDA − **1,05** (2,32 − 0,05 de temps interne − 0,02 d'intérêts − 1,20), soit **17,35** ; dette nette + **1,07**, soit **45,07** ; ratio **2,39 → 2,60** > 2,50 : la clause n'est plus respectée (marge de 2,00 M€ devenue − 1,695 M€ ; 2,87 sans assurance) ; conséquences : renonciation à négocier avant la clôture, commission et hausse de marge, risque d'exigibilité | 0,75 |
| 2.7-03 | Acteurs : **ANSSI** (sécurité des systèmes d'information, CERT-FR, prestataires qualifiés), **DGSI** (protection du patrimoine économique, ingérence), **SISSE** (sécurité économique des entreprises stratégiques), plainte auprès de la police ou de la gendarmerie (COMCYBER-MI) ; récupération : rappel immédiat du virement par la banque **du payeur** (HAVERWICK), gel par la banque destinataire, rapidité (quelques heures), coopération internationale, d'où 1,10 M$ seulement récupérés après quatre jours | 0,5 |
| 2.7-04 | Gouvernance : procédure écrite de changement de coordonnées bancaires (confirmation par un autre canal, information des clients), suivi quotidien des encaissements attendus, risque cyber dans la cartographie et au comité d'audit, plafond d'assurance à revoir, sensibilisation des équipes, plan de réponse ; sans solution technique détaillée | 0,5 |

**Chiffrage du préjudice (0,75 pt).** L'incident n'est pas un virement frauduleux émis par LANDRAVEL : c'est le règlement d'un client qui a été détourné, après une intrusion dans la messagerie de LANDRAVEL. Comme LANDRAVEL a accepté de tenir la facture pour réglée, la créance non récupérée est une perte pour elle.

| M€ (conversion à 1,1000) | Montant | Dans l'EBITDA | Décaissé ou non encaissé | Garanti par l'assurance |
|---|---:|:---:|:---:|:---:|
| Règlement détourné (3,30 M$) | 3,00 | oui | oui | oui |
| Fonds récupérés par le rappel du virement (1,10 M$) | − 1,00 | oui | oui | oui |
| **Montant non récupéré (2,20 M$)** | **2,00** | | | |
| Enquête du prestataire de réponse aux incidents | 0,18 | oui | oui | oui |
| Conseils juridiques | 0,07 | oui | oui | non (exclus) |
| Temps interne valorisé | 0,05 | non | non | non |
| Intérêts du découvert | 0,02 | non (frais financiers) | oui | non |
| **Coût total de l'incident** | **2,32** | | | |

Assurance cyber : base garantie = 2,00 + 0,18 = 2,18 M€ ; après franchise, 2,18 − 0,25 = 1,93 M€, au-delà du plafond : **indemnité de 1,20 M€**. **Perte nette = 2,32 − 1,20 = 1,12 M€**, dont 0,05 M€ de temps interne sans décaissement. Le plafond de 1,20 M€ est faible au regard d'un seul règlement de HAVERWICK (3,00 M€) : LANDRAVEL reste son propre assureur pour l'essentiel.

**Effets sur l'EBITDA, la dette nette et la clause financière (0,75 pt).**
- EBITDA : 3,00 − 1,00 + 0,18 + 0,07 − 1,20 = **1,05 M€** de moins (le temps interne était déjà compris dans les charges de personnel, les intérêts sont des frais financiers) : 18,40 → **17,35 M€** (− 5,71 %).
- Endettement financier net : 3,00 − 1,00 + 0,18 + 0,07 + 0,02 − 1,20 = **1,07 M€** de plus : 44,00 → **45,07 M€**.
- Ratio endettement financier net / EBITDA : 44,00 / 18,40 = **2,39** avant l'incident ; 45,07 / 17,35 = **2,60** après : le seuil de **2,50** est dépassé. La marge sous le seuil (2,50 × 18,40 − 44,00 = 2,00 M€) devient négative (2,50 × 17,35 − 45,07 = − 1,695 M€). Sans l'assurance, le ratio atteindrait 2,87.
- Conséquences : une perte nette de 1,12 M€, faible au regard du chiffre d'affaires, suffit à faire franchir le seuil parce que la ligne et ses financements laissent peu de marge. La Banque SOLVÈDRE pourrait exiger le remboursement du prêt ; en pratique, LANDRAVEL doit négocier avant la clôture une renonciation temporaire, payée par une commission et une hausse de marge, ou réduire sa dette nette d'environ 1,70 M€ d'ici le 31 décembre (BFR, calendrier des investissements, renforcement des fonds propres). Au-delà de 2027, la confiance de HAVERWICK, des banques et des assureurs (prime et conditions de renouvellement) est en jeu : le risque cyber touche la trésorerie, la solvabilité et la valeur.

**Acteurs publics et récupération des fonds (0,5 pt)** (F09 § 5.2).
- **ANSSI** (Agence nationale de la sécurité des systèmes d'information, créée par le décret n° 2009-834 du 7 juillet 2009) : autorité nationale de sécurité des systèmes d'information ; le CERT-FR alerte et conseille, l'agence qualifie les prestataires de réponse aux incidents et publie des guides de bonnes pratiques.
- **DGSI** (ministère de l'Intérieur) : protection du patrimoine économique et lutte contre les ingérences ; elle sensibilise les entreprises sensibles, dont les sous-traitants de l'aéronautique et du spatial comme LANDRAVEL.
- **SISSE** (Service de l'information stratégique et de la sécurité économiques, direction générale des entreprises) : politique de sécurité économique et accompagnement des entreprises stratégiques menacées.
- La plainte est déposée auprès de la police ou de la gendarmerie (COMCYBER-MI) : elle ouvre l'enquête et permet de solliciter la coopération judiciaire internationale, en complément du rappel du virement et du gel obtenus par les banques.
- **Conditions de la récupération** : ici, c'est le **payeur**, HAVERWICK, qui doit demander à **sa** banque le rappel du virement ; LANDRAVEL dépend donc de la réactivité de son client. Les chances de récupération décroissent en quelques heures : les fonds sont rapidement transférés vers d'autres comptes. Un paiement en dollars vers un pays hors de l'Union européenne passe par des banques correspondantes et suppose la coopération de la banque destinataire et des autorités étrangères. Découvert quatre jours après le paiement, le détournement n'a permis de récupérer qu'un tiers des fonds (1,10 M$ sur 3,30 M$).

**Mesures de gouvernance (0,5 pt).**
- **Procédure des paiements entrants** : écrire à tous les clients que LANDRAVEL ne change jamais ses coordonnées bancaires par simple courriel ; toute modification est confirmée par un autre canal (appel à un interlocuteur connu, courrier signé par deux personnes habilitées) ; inscrire cette règle dans les contrats, dont celui de HAVERWICK.
- **Suivi de la trésorerie** : rapprochement quotidien des encaissements attendus des grands clients, alerte immédiate en cas de retard, procédure de rappel des virements préparée avec les banques et les clients.
- **Pilotage par le conseil** : risque cyber inscrit dans la cartographie des risques et suivi par le comité d'audit, responsable désigné, budget, indicateurs et exercices de crise ; plan de réponse (prestataire, banques, assureur, autorités).
- **Assurance** : revoir le plafond au regard des règlements unitaires de HAVERWICK et de l'exposition de la clause financière.
- **Sensibilisation** des équipes comptables et commerciales aux courriels piégés ; les mesures techniques (authentification renforcée, contrôle des accès) sont confiées aux spécialistes et ne sont pas détaillées ici.
- Ces mesures relèvent d'une approche globale de gouvernance et de performance durable : la fiabilité de LANDRAVEL est un actif immatériel, et le respect de ses engagements bancaires conditionne le financement de sa croissance.

**Réponses tolérées** : perte nette présentée hors temps interne (1,07 M€) si le traitement est justifié ; ratio calculé avec l'indemnité encaissée en 2028 (hypothèse contraire à l'annexe, 0,25 au plus sur 2.7-02) ; mention de Cybermalveillance.gouv.fr, de la CNIL ou de Tracfin en complément des trois acteurs demandés.

**Erreurs fréquentes**
- Retenir les 3,30 M$ détournés comme perte, sans déduire les fonds récupérés, ou oublier de convertir en euros.
- Appliquer la franchise après le plafond, ou retenir l'indemnité calculée sans plafond (1,93 M€).
- Inclure les intérêts dans l'EBITDA ou le temps interne dans la trésorerie.
- Traiter l'incident comme un faux ordre de virement émis par LANDRAVEL, ou analyser l'infraction au regard du droit, ce qui n'est pas demandé.
- Proposer des solutions informatiques détaillées au lieu de mesures de gouvernance et de contrôle des paiements.
- `JUR-T13` — mesures générales sans lien avec le cas ; `JUR-T05` — risque cyber non relié à la gouvernance ; `JUR-T15` — question bâclée en fin de dossier.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 2, parties 2.2, 6.2, 6.3 et 7.2 (arrêté du 4 août 2025, annexe 2) ; guide pédagogique de juillet 2026, p. 63, 77-79 et 81-82 | compétences évaluées ; position de change, techniques internes, terme et option à prime donnée ; FRA, contrats à terme, relation valeur-taux ; coût des financements ; risque cyber et récupération des flux | [V] | `ue2/programme/perimetre_ue2.yaml` |
| Position de change, parité des taux d'intérêt, report et déport, option de change, valeur intrinsèque et valeur temps | questions 2.1 à 2.3 | [S] formules de cours ; [V] programme pour la décomposition de la prime | F07 § 3 |
| FRA, contrats à terme sur Euribor 3 mois, duration et sensibilité | questions 2.4 et 2.5 | [S] formules et caractéristiques usuelles | F07 § 2 |
| Coût actuariel d'un emprunt et d'un crédit-bail | question 2.6 | [S] formules de cours | F01 § 3 |
| ANSSI (décret n° 2009-834 du 7 juillet 2009), DGSI, SISSE, COMCYBER-MI ; rappel des virements ; assurance cyber | question 2.7 | [V] décret ; [S] rôles et pratiques | F09 § 5 |
| Cours EUR/USD de 1,1200, taux d'intérêt de 2,40 % à 4,10 %, Euribor 3 mois de 2,65 % | hypothèses d'énoncé cohérentes avec les données d'octobre 2026 | [V] fourchettes | F11 |
