# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 40 — Dossier 1 (16 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 risques de taux et de change, trésorerie de groupe, climat et matières premières, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (compensation multilatérale : soldes nets, règlements, nombre et montant des virements, frais bancaires ; vente à terme de la livre, avance en livres, contrat d'échange sur le carburant, achat à terme de dollars, swap, tunnel et caps ; barème, liste noire, hors-programme ; marge de change, coût du décalage des recettes, position de change, exposition au risque de taux, coût du carburant par tonne et seuils de comparaison vérifiés par script).

Bien que le corrigé mentionne des textes et des données de marché, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une position en livres erronée à la question 1.2, reprise dans la vente à terme et l'avance de la question 1.3, ou un cours à terme du dollar erroné repris dans le coût par tonne de la question 1.4).

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Compensation multilatérale des flux intragroupe | `6.1.a` Appliquer les mécanismes de centralisation de trésorerie | 3,5 |
| 1.2 Position de change du trimestre en livres et en dollars | `6.3.a` Caractériser la position de change courte ou longue, ouverte ou fermée | 1,5 |
| 1.3 Cours à terme de la livre, vente à terme ou avance en livres, techniques internes | `6.3.b` Comprendre le fonctionnement du marché des changes (comptant et à terme) ; `6.3.c` Maîtriser les techniques internes et les garanties externes | 3 |
| 1.4 Contrat d'échange sur le carburant et achat à terme de dollars | `6.4.a` Sensibiliser aux instruments de couverture des risques physiques et financiers liés au changement climatique et à la raréfaction des ressources naturelles ; `6.3.d` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (change) | 2,5 |
| 1.5 Exposition de l'emprunt du navire au risque de taux | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 1 |
| 1.6 Swap, tunnel et caps sur l'emprunt du navire | `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux ; `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) | 3,5 |
| 1.7 Recommandation de synthèse au directoire | `6.3.d` ; `6.2.b` | 1 |
| **Total** | | **16** |

Part du calcul : environ 10 points (1.1-01 à 1.1-04, 1.2-01, 1.2-03, 1.3-01 à 1.3-04, 1.4-01, 1.4-02, 1.5-01, 1.6-01 à 1.6-04), pour des calculs courts et répétitifs. Part de l'analyse : environ 6 points (1.1-05, 1.1-06, 1.2-02, 1.3-05, 1.4-03, 1.4-04, 1.5-02, 1.6-05, 1.7). Les questions 1.5, 1.6 et 1.7 se traitent sans les résultats des questions 1.1 à 1.4 : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 1.1 Compensation multilatérale des flux intragroupe (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.1-01 | Soldes nets : KERNAVEL SE + 2 300 k€ ; KERNAVEL Ireland − 1 650 k€ ; KERNAVEL UK + 300 k€ (258 k GBP) ; KERNAVEL Iberia − 950 k€ (somme nulle) | 0,5 |
| 1.1-02 | Règlements : Ireland → SE 1 650 ; Iberia → SE 650 ; Iberia → UK 300 (258 k GBP). 20 virements et 10 250 k€ avant, 3 virements et 2 600 k€ après | 0,5 |
| 1.1-03 | Frais bancaires : 5 725 € avant, 1 390 € après par mois ; économie de 4 335 € par mois, 52 020 € par an ; 16 020 € par an nets du coût du centre | 0,5 |
| 1.1-04 | Marge de change : 4 900 k€ convertis avant, 300 k€ après ; 9 200 € par mois, 110 400 € par an ; économie annuelle nette totale 126 420 € | 0,5 |
| 1.1-05 | Prérequis : système d'information, accord des filiales, cours de conversion commun, calendrier et factures validées | 0,5 |
| 1.1-06 | Limites au regard des chiffres et conclusion | 1 |

**Soldes nets (0,5 pt).** Les montants en livres sont convertis au cours de compensation (1 EUR = 0,8600 GBP) : 1 720 k GBP / 0,8600 = 2 000 k€, par exemple. Solde net = montants à recevoir − montants à payer sur le mois.

| k€ | À recevoir | À payer | Solde net |
|---|---:|---:|---:|
| KERNAVEL SE | 2 400 + 2 000 + 1 500 + 300 = 6 200 | 600 + 2 600 + 700 = 3 900 | **+ 2 300** |
| KERNAVEL Ireland | 600 + 150 = 750 | 2 400 | **− 1 650** |
| KERNAVEL UK | 2 600 | 2 000 + 300 = 2 300 | **+ 300** (258 k GBP) |
| KERNAVEL Iberia | 700 | 1 500 + 150 = 1 650 | **− 950** |
| **Total** | **10 250** | **10 250** | **0** |

La somme des soldes est nulle : ce qu'une société paie, une autre le reçoit. La SE, qui reçoit les recettes des billets, est la principale créditrice nette ; KERNAVEL UK est aussi créditrice, parce que les escales anglaises qu'elle refacture dépassent les recettes qu'elle reverse.

**Règlements et virements (0,5 pt).** La plus forte position débitrice (Ireland, 1 650) règle d'abord la plus forte position créditrice (SE, 2 300) ; Iberia (950) règle le reste dû à la SE (650), puis KERNAVEL UK (300 k€, versés en livres : 300 × 0,8600 = 258 k GBP).

| | Nombre de virements | Montant viré (k€) |
|---|---:|---:|
| Avant compensation (un virement par facture) | 4 + 4 + 4 + 1 + 2 + 2 + 2 + 1 = 20 | 10 250 |
| Après compensation | 3 | 2 600 |
| Réduction | − 17 (− 85,00 %) | − 7 650 (− 74,63 %) |

Le montant viré après compensation est la somme des soldes créditeurs (2 300 + 300 = 2 600 k€). Avec quatre sociétés, trois virements au plus suffisent.

**Frais bancaires (0,5 pt).**
- Avant : 20 × 30 € + 0,05 % × 10 250 000 € = 600 + 5 125 = **5 725 €** par mois.
- Après : 3 × 30 € + 0,05 % × 2 600 000 € = 90 + 1 300 = **1 390 €** par mois.
- Économie : **4 335 €** par mois, soit **52 020 €** par an ; nette du coût du centre (36 000 €), **16 020 €** par an.

**Marge de change (0,5 pt).** Aujourd'hui, la SE vend les livres reçues de KERNAVEL UK (2 000 + 300 = 2 300 k€) et achète celles qu'elle lui paie (2 600 k€) : 4 900 k€ convertis par mois, soit 0,20 % × 4 900 000 = **9 800 €**. Après compensation, seul le règlement d'Iberia à KERNAVEL UK est converti (300 k€) : **600 €**. Économie : **9 200 €** par mois, **110 400 €** par an.

| € par an | Montant |
|---|---:|
| Économie de frais bancaires | 52 020 |
| Économie de marge de change | 110 400 |
| − Coût du centre de compensation | − 36 000 |
| **Économie annuelle nette** | **126 420** |

L'essentiel du gain vient des conversions évitées : dans un groupe multidevise, la compensation réduit d'abord les opérations de change.

**Prérequis (0,5 pt).**
- **Système d'information** : un module de compensation dans le logiciel de trésorerie, alimenté par les quatre sociétés, et des factures intragroupe **validées** par le payeur et le bénéficiaire avant la date de coupure (rapprochement des créances et des dettes, traitement des litiges).
- **Accord des filiales** : une convention de compensation signée par les quatre sociétés (périmètre des factures, calendrier, rôle de la SE comme centre, règles de règlement des soldes), étudiée ici sous l'angle financier seulement ; les directions locales perdent la maîtrise de leurs dates de paiement.
- **Cours de conversion commun** : un cours unique et incontestable (le comptant du 31 mars, de la même source pour tous), qui fixe qui supporte le risque de change entre la facturation et la compensation ; un compte en livres pour régler KERNAVEL UK.
- Un **calendrier** commun : date de coupure, date de valeur unique des règlements.

**Limites et conclusion (1 pt).**
- **Décalage de trésorerie** : les recettes des billets, reversées aujourd'hui chaque semaine (12 virements par mois), ne le seraient plus qu'une fois par mois. La SE, créditrice nette, attendrait jusqu'à trois semaines de plus près de 6 M€ de recettes : avec des reversements hebdomadaires réglés en fin de mois, le retard moyen est d'une semaine et demie (10,5 jours) : pour la SE, le coût de ce portage est de l'ordre de 50 k€ par an au taux de 2,60 % (5 900 000 × 2,60 % × 10,5 / 360 × 12 = 53 690 €), soit une part importante de l'économie. Pour le groupe, il est neutre si Ireland et Iberia, débitrices nettes, placent ces fonds au même taux, et défavorable sinon. Une compensation à fréquence plus courte pour les recettes (hebdomadaire ou bimensuelle) ou le maintien de leurs reversements hebdomadaires hors du dispositif répond à cette limite.
- **Le gain est faible au regard des flux** : 126 420 € par an pour 123 M€ de flux intragroupe annuels (12 × 10 250 k€), soit environ 0,10 % ; une grande partie de l'économie de change serait aussi obtenue en gardant sur le compte en livres de la SE les livres reçues pour payer les livres dues (compensation des flux de même devise), sans centre de compensation.
- **La compensation ne supprime ni le risque de change ni le besoin de financement** : elle réduit les flux intragroupe à convertir, mais ne touche pas les flux en devises avec les clients et les fournisseurs (question 1.2) ; elle ne finance rien et ne remplace pas une centralisation des soldes.
- **Coûts et contraintes d'organisation** : 36 000 € par an, discipline de facturation, dépendance au logiciel, risque d'erreur sur le cours de compensation.
- **Intérêt réel** : simplification (17 virements de moins par mois), **visibilité** de la direction financière sur les flux du groupe, base d'une gestion centralisée du change.
- **Conclusion** : le centre de compensation est rentable (126 420 € par an nets), surtout par les conversions évitées ; il est justifié si son calendrier ne retarde pas les recettes des billets.

**Réponses tolérées** : soldes présentés dans une matrice payeurs × bénéficiaires ; règlements organisés autrement (par exemple centralisés par la SE : Ireland et Iberia lui versent 1 650 et 950 k€, elle verse 300 k€ à KERNAVEL UK : 3 virements, 2 900 k€), si les frais sont calculés en cohérence (1 540 € par mois) ; économie de change présentée séparément des frais bancaires ; mention du termaillage pour le décalage des dates.

**Erreurs fréquentes**
- Calculer le montant après compensation comme la somme des valeurs absolues des soldes (5 200 k€) au lieu de la somme des seuls soldes créditeurs.
- Oublier la commission proportionnelle ou la marge de change, ou ne pas déduire le coût du centre.
- Compter les flux en livres pour leur montant en livres dans un total en euros (mélange des unités).
- `JUR-T07` — soldes calculés en ligne, sans tableau ; `JUR-T13` — avantages génériques de la compensation sans constater que le gain vient des conversions évitées ni que le calendrier retarde les recettes de la SE.

---

### 1.2 Position de change du trimestre (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 1.2-01 | Positions par mois et du trimestre : + 5 400 000 GBP (contre-valeur 6 250 000 €) ; − 18 000 000 USD (16 000 000 €) | 0,5 |
| 1.2-02 | Qualification : livre longue et ouverte (risque de dépréciation : hausse du cours EUR/GBP au certain) ; dollar court et ouvert (risque d'appréciation : baisse du cours EUR/USD) ; flux intragroupe hors position du groupe | 0,5 |
| 1.2-03 | Perte dans le scénario défavorable : 250 000 € sur la livre, 666 667 € sur le dollar, 916 667 € au total | 0,5 |

**Positions (0,5 pt).** Position de change d'une devise = encaissements − décaissements dans cette devise, après compensation des flux de même devise sur le compte en livres de la SE.

| Position (devise) | Mai | Juin | Juillet | Trimestre |
|---|---:|---:|---:|---:|
| Encaissements GBP | 2 600 000 | 3 100 000 | 4 300 000 | 10 000 000 |
| Décaissements GBP | − 1 400 000 | − 1 500 000 | − 1 700 000 | − 4 600 000 |
| **Position GBP** | **+ 1 200 000** | **+ 1 600 000** | **+ 2 600 000** | **+ 5 400 000** |
| **Position USD** (10 000 t × 600 USD) | **− 6 000 000** | **− 6 000 000** | **− 6 000 000** | **− 18 000 000** |

Contre-valeurs au comptant du 30 avril : 5 400 000 / 0,8640 = **6 250 000 €** ; 18 000 000 / 1,1250 = **16 000 000 €**. La compensation des flux en livres ferme déjà 46 % des encaissements (4,6 M GBP sur 10 M GBP) : seuls 5,4 M GBP restent à convertir. Les flux intragroupe de l'annexe 1.1 ne créent pas de position pour le groupe : ils s'annulent entre sociétés, et le solde de KERNAVEL UK ne fait que déplacer le risque entre la filiale et la SE.

**Qualification (0,5 pt).**
- **Livre : position longue** (encaissements supérieurs aux décaissements) et **ouverte** (non couverte) : le groupe craint la **dépréciation de la livre**, c'est-à-dire, au certain, une **hausse** du cours EUR/GBP (1 EUR = 0,9000 GBP au lieu de 0,8640) : chaque livre encaissée rapporte moins d'euros.
- **Dollar : position courte** (achats de carburant sans recettes en dollars) et **ouverte** : le groupe craint l'**appréciation du dollar**, c'est-à-dire une **baisse** du cours EUR/USD (1,0800 au lieu de 1,1250) : chaque dollar payé coûte plus d'euros.
- Il s'agit d'un risque de transaction sur des flux certains et datés (29 juillet) ; aucune position n'est fermée, puisque le groupe n'a ni dépenses en livres au-delà des escales ni recettes en dollars.

**Perte dans le scénario défavorable (0,5 pt).**

| € | Au comptant du 30 avril | Au cours du scénario | Perte |
|---|---:|---:|---:|
| Livre : 5 400 000 GBP | 5 400 000 / 0,8640 = 6 250 000 | 5 400 000 / 0,9000 = 6 000 000 | **250 000** |
| Dollar : 18 000 000 USD | 18 000 000 / 1,1250 = 16 000 000 | 18 000 000 / 1,0800 = 16 666 667 | **666 667** (surcoût) |
| **Total** | | | **916 667** |

Le risque principal est celui du dollar : la position est plus de deux fois et demie plus forte en contre-valeur et elle s'ajoute au risque sur le prix du carburant.

**Réponses tolérées** : position cumulée au fil du trimestre ; contre-valeurs arrondies au millier d'euros ; position en dollars mesurée sur la seule part non couverte par le contrat d'échange, si l'hypothèse est écrite ; risque exprimé à l'incertain (la livre passe de 1,1574 € à 1,1111 €), si la cotation est précisée.

**Erreurs fréquentes**
- Prendre les encaissements bruts en livres (10 M GBP) comme position, sans compenser les décaissements.
- Ajouter les flux intragroupe de l'annexe 1.1 à la position du groupe.
- Dire que le groupe craint la « hausse du cours » sans préciser la cotation, ou qualifier de longue la position en dollars d'un acheteur.
- `JUR-T07` — positions sans tableau par devise et par mois.

---

### 1.3 Cours à terme de la livre, vente à terme ou avance en livres, techniques internes (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.3-01 | Cours à terme 0,8674 (points de terme + 34) ; euro en report, livre en déport, parce que le taux de la livre dépasse celui de l'euro | 0,5 |
| 1.3-02 | Vente à terme : 5 400 000 / 0,8674 = 6 225 501 € le 29 juillet | 0,5 |
| 1.3-03 | Avance : emprunt 5 337 287 GBP (intérêts 62 713 GBP) ; 6 177 415 € obtenus le 30 avril ; placement 35 520 € ; valeur acquise 6 212 936 € ; cours implicite 0,8692 | 1 |
| 1.3-04 | Comparaison : la vente à terme rapporte 12 566 € de plus ; explication par les taux et cas où l'avance serait préférable | 0,5 |
| 1.3-05 | Techniques internes encore disponibles pour la livre, appliquées au cas | 0,5 |

**Cours à terme (0,5 pt).** Au certain, par la parité des taux d'intérêt, sur 90 jours en base Exact/360 :

cours à terme = 0,8640 × (1 + 4,20 % × 90 / 360) / (1 + 2,60 % × 90 / 360) = 0,8640 × 1,0105 / 1,0065 = 0,86743, soit **0,8674**.

Points de terme : 0,8674 − 0,8640 = **+ 34 points**. Un euro vaut plus de livres à terme qu'au comptant : l'**euro est en report**, la **livre en déport**. C'est la contrepartie du taux d'intérêt plus élevé de la livre (4,20 % contre 2,60 %) : le cours à terme n'est pas une prévision du cours futur.

**Vente à terme (0,5 pt).** La SE vend aujourd'hui à terme 5 400 000 GBP livrables le 29 juillet : elle recevra **5 400 000 / 0,8674 = 6 225 501 €**, quel que soit le cours du 29 juillet. L'écart avec la contre-valeur au comptant (6 250 000 €, soit 24 499 €) est le coût du différentiel de taux, pas une perte de change.

**Avance en livres placée en euros (1 pt).**

| Étape | Calcul | Résultat |
|---|---|---:|
| Montant emprunté le 30 avril | 5 400 000 / (1 + 4,70 % × 90 / 360) = 5 400 000 / 1,01175 | **5 337 287 GBP** |
| Intérêts de l'avance (payés le 29 juillet) | 5 400 000 − 5 337 287 | 62 713 GBP |
| Euros obtenus au comptant le 30 avril | 5 337 287 / 0,8640 | **6 177 415 €** |
| Intérêts du placement | 6 177 415 × 2,30 % × 90 / 360 | 35 520 € |
| **Valeur acquise le 29 juillet** | 6 177 415,37 + 35 520,14 = 6 212 935,51 | **6 212 936 €** |
| Cours implicite | 5 400 000 / 6 212 936 | **0,8692** |

Le 29 juillet, le solde net du compte en livres (5 400 000 GBP) rembourse exactement l'avance et ses intérêts : la position en livres est fermée, et le groupe dispose des euros dès le 30 avril.

**Comparaison (0,5 pt).** La vente à terme rapporte **6 225 501 €**, l'avance placée **6 212 936 €** : la **vente à terme est meilleure de 12 566 €** (12 565,99 € avant arrondi) (cours de 0,8674 contre 0,8692 : un euro « coûte » moins de livres). L'avance revient à emprunter la livre à 4,70 %, soit 0,50 point au-dessus du taux de marché de la livre, et à placer l'euro à 2,30 %, 0,30 point sous le taux de l'euro qui sert à la parité. L'avance deviendrait avantageuse si les euros obtenus rapportaient ou faisaient économiser plus de **3,11 %** par an, par exemple s'ils remboursaient un découvert ou finançaient un besoin de trésorerie plus coûteux. Ce n'est pas le cas ici : la vente à terme, gratuite et simple, est préférable.

**Techniques internes encore disponibles (0,5 pt).**
- **Compensation des flux de même devise** : déjà appliquée (4,6 M GBP de décaissements payés avec les livres encaissées) ; elle peut être étendue en payant en livres d'autres dépenses du groupe au Royaume-Uni (avitaillement, maintenance, services), ce qui ferme une partie supplémentaire de la position, sans coût.
- **Termaillage** : avancer les encaissements en livres (acomptes des clients du fret, réservations payées plus tôt) et retarder les achats de livres si la dépréciation est anticipée ; c'est un pari sur le cours, limité par les relations commerciales et par la politique du groupe, qui interdit les positions spéculatives.
- **Choix de la monnaie de facturation** : facturer en euros une partie des contrats de fret britanniques reporte le risque sur les clients, au prix d'une moindre compétitivité face aux concurrents qui facturent en livres.
- **Compensation intragroupe** (question 1.1) : elle réduit les conversions internes, pas la position du groupe envers les tiers.
Ces techniques précèdent la couverture externe : elles réduisent le montant à couvrir à moindre coût, mais ne ferment pas toute la position.

**Réponses tolérées** : valeur acquise de 6 212 935 € et écart de 12 565 € si le candidat additionne les montants arrondis ; avance calculée en empruntant 5 400 000 GBP et en remboursant capital et intérêts avec un complément (raisonnement cohérent signalé) ; comparaison exprimée par les cours (0,8674 contre 0,8692) ; mention de la clause monétaire avec les clients, si elle reste brève.

**Erreurs fréquentes**
- Inverser les taux dans la formule (0,8640 × 1,0065 / 1,0105 = 0,8606), ce qui donnerait une livre en report.
- Emprunter 5 400 000 GBP sans actualiser au taux de l'avance, ou convertir les livres au cours à terme au lieu du comptant.
- Comparer l'avance au comptant du jour (6 250 000 €) au lieu de la vente à terme, ou oublier le placement des euros.
- `JUR-T02` — techniques internes énumérées sans lien avec les flux du groupe (escales, fret, filiale britannique).

---

### 1.4 Contrat d'échange sur le carburant et achat à terme de dollars (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.4-01 | Contrat d'échange sur 24 000 t (tableau des deux scénarios) : coût net 14 760 000 USD et prix effectif 615 USD/t dans les deux cas ; gain de 2 040 000 USD (indice 700) ; coût d'opportunité de 1 800 000 USD (indice 540) | 1 |
| 1.4-02 | Cours à terme du dollar 1,1292 (+ 42 points) ; coût en euros 14 760 000 / 1,1292 = 13 071 201 €, soit 544,63 € par tonne | 0,5 |
| 1.4-03 | Complémentarité des deux couvertures et risques qui restent (6 000 t, volume, contrepartie, coût d'opportunité ; absence de risque de base justifiée par l'annexe) | 0,5 |
| 1.4-04 | Risque de transition : ce que la couverture ne règle pas | 0,5 |

**Contrat d'échange (1 pt).** KERNAVEL paie le prix fixe (615 USD/t) et reçoit l'indice moyen ; le fournisseur facture l'indice. Coût net = achats au prix de l'indice − règlement reçu (ou + règlement versé).

| USD, 24 000 t | Indice 700 USD/t | Indice 540 USD/t |
|---|---:|---:|
| Achats au prix de l'indice (sans couverture) | 24 000 × 700 = 16 800 000 | 24 000 × 540 = 12 960 000 |
| Règlement du contrat | reçu : 24 000 × (700 − 615) = + 2 040 000 | versé : 24 000 × (615 − 540) = − 1 800 000 |
| **Coût net** | **14 760 000** | **14 760 000** |
| **Prix effectif** | **615 USD/t** | **615 USD/t** |
| Gain ou coût d'opportunité par rapport à l'absence de couverture | **gain de 2 040 000** | **coût d'opportunité de 1 800 000** |

Le contrat d'échange fixe le prix en dollars de 80 % de la consommation, quel que soit l'indice. Le prix fixe dépasse de 15 USD/t le prix de référence du budget (360 000 USD sur 24 000 t) : c'est le prix de la certitude, rémunération de la banque comprise.

**Achat à terme de dollars (0,5 pt).** Le 29 juillet, KERNAVEL paie l'indice au fournisseur et règle le contrat : dans les deux scénarios, elle débourse au total 14 760 000 USD (24 000 × 615). Elle les achète à terme :

cours à terme = 1,1250 × (1 + 4,10 % × 90 / 360) / (1 + 2,60 % × 90 / 360) = 1,1250 × 1,01025 / 1,0065 = 1,12919, soit **1,1292** (+ 42 points ; euro en report, dollar en déport).

Coût en euros : **14 760 000 / 1,1292 = 13 071 201 €**, soit **544,63 € par tonne** (13 071 201 / 24 000). L'achat à terme est moins cher que la conversion au comptant du jour (13 120 000 €) : acheter à terme une devise en déport est favorable à l'importateur.

**Complémentarité et risques qui restent (0,5 pt).**
- Le contrat d'échange fixe le **prix en dollars** ; l'achat à terme fixe le **cours du dollar** : seul, le contrat d'échange laisserait le coût en euros dépendre du dollar (14 760 000 USD à 1,0800 coûteraient 13 666 667 €) ; seul, l'achat à terme porterait sur un montant de dollars inconnu. Ensemble, ils rendent certain le **coût en euros** du carburant couvert : 13 071 201 €. Le montant en dollars acheté à terme correspond exactement au décaissement net, parce que le règlement du contrat compense l'écart entre l'indice et le prix fixe.
- **Restent exposés** : les 6 000 t non couvertes (20 % de la consommation, 3,6 M USD au prix de référence), au prix de l'indice et au cours du dollar ; le **volume** (une consommation inférieure à 24 000 t, par exemple après des rotations annulées pour tempête, laisserait le contrat porter sur plus que les achats, ce qui deviendrait une position spéculative) ; **pas de risque de base** ici, puisque le fournisseur facture à l'indice même du contrat (annexe 1.4) ; il apparaîtrait si le carburant était acheté à un prix local différent de l'indice ; le **risque de contrepartie** de la banque ; le **coût d'opportunité** si l'indice baisse, face à des concurrents non couverts qui bénéficieraient de la détente.

**Risque de transition (0,5 pt).** La couverture lisse le prix du carburant sur un trimestre ; elle ne réduit pas la dépendance du groupe au carburant fossile, l'un des premiers postes de charges des lignes. Les règles sur les émissions du transport maritime et le prix du carbone, qu'anticipe la direction, renchériront durablement l'énergie : ce surcoût n'est pas couvert par un contrat sur l'indice du carburant, et chaque renouvellement de la couverture se fera au nouveau niveau de prix. Les instruments de marché protègent contre la variabilité, pas contre une hausse structurelle : seule la baisse de la consommation (vitesse, navires plus sobres, énergies moins émettrices) réduit l'exposition de fond. Les risques physiques (tempêtes, rotations annulées) agissent aussi sur le volume consommé et donc sur l'efficacité de la couverture. La politique de couverture doit donc s'articuler avec la stratégie de transition et l'information extra-financière du groupe.

**Réponses tolérées** : montants présentés en M USD à deux décimales ; achat à terme calculé sur toute la consommation estimée (18 M USD), si le candidat signale la sur-couverture possible ; analyse du risque de transition fondée sur la réputation ou l'accès aux financements, si elle est reliée au carburant.

**Erreurs fréquentes**
- Inverser le sens du règlement (KERNAVEL qui recevrait quand l'indice baisse) ou ajouter le règlement au lieu de le retrancher.
- Parler de « perte » sur le contrat dans le scénario à 540 : c'est un coût d'opportunité, le coût net reste 615 USD/t.
- Convertir les dollars au cours comptant du jour au lieu du cours à terme, ou multiplier au lieu de diviser au certain.
- `JUR-T05` et `JUR-T13` — risque de transition réduit à une phrase générale, sans lien avec le poids du carburant dans les charges ni avec les limites de la couverture.

---

### 1.5 Exposition de l'emprunt du navire au risque de taux (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 1.5-01 | Emprunteur à taux variable : risque de hausse ; + 100 points de base = + 960 000 € d'intérêts par an (1,17 % de l'EBITDA 2026), + 720 000 € après IS | 0,5 |
| 1.5-02 | Taux variable : risque sur la charge d'intérêts, valeur de la dette stable ; taux fixe : charge certaine, valeur sensible aux taux (relation inverse) | 0,5 |

**Sens et ampleur (0,5 pt).** KERNAVEL emprunte au taux variable, révisé chaque trimestre : elle craint la **hausse** des taux. Une hausse de 100 points de base renchérit les intérêts annuels de 96 000 000 × 1 % = **960 000 €**, soit 1,17 % de l'EBITDA de 2026 (82 M€) ; après IS à 25 %, **720 000 €**. Pour la prochaine période non encore fixée, les intérêts aux conditions du jour seraient de 96 000 000 × (2,60 % + 1,30 %) × 90 / 360 = 936 000 €. L'exposition est modérée au regard de l'EBITDA, mais elle dure jusqu'en 2037 et s'ajoute aux risques de change et de carburant, qui pèsent sur la même marge.

**Taux variable et taux fixe (0,5 pt).** La valeur d'une dette est la somme de ses flux actualisés au taux du marché : quand les taux montent, la valeur d'une dette à taux fixe baisse, et inversement (relation inverse valeur-taux, d'autant plus forte que la duration est longue). Pour l'emprunt à taux variable, le taux est réajusté chaque trimestre : sa valeur reste proche du capital restant dû, mais sa **charge d'intérêts** varie, ce qui crée un risque sur les flux de trésorerie et le résultat. Les autres dettes du groupe, à taux fixe, ont une charge certaine, mais une valeur qui augmente si les taux baissent : le groupe supporte alors un **coût d'opportunité** (il paie plus que le marché). Le groupe combine donc deux expositions de nature différente.

**Réponses tolérées** : effet calculé sur le capital moyen de l'année suivante, si l'hypothèse est écrite ; effet rapporté au résultat plutôt qu'à l'EBITDA.

**Erreurs fréquentes**
- Dire que l'emprunteur à taux variable craint la baisse des taux, ou que la valeur de sa dette varie fortement avec les taux.
- Calculer l'effet de 100 points de base sur un trimestre seulement (240 000 €) en le présentant comme annuel.
- `JUR-T12` — relation valeur-taux énoncée sans l'appliquer à la dette du groupe.

---

### 1.6 Swap, tunnel et caps sur l'emprunt du navire (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 1.6-01 | Swap : coût net 1 008 000 € et taux effectif 4,20 % dans les trois scénarios (différentiels + 216 000, − 48 000, − 264 000) | 0,5 |
| 1.6-02 | Tunnel : prime nette 9 600 € ; coûts nets 1 137 600 €, 969 600 €, 849 600 € ; taux effectifs 4,74 %, 4,04 %, 3,54 % | 1 |
| 1.6-03 | Bornes du tunnel : 3,54 % et 4,74 % | 0,5 |
| 1.6-04 | Caps : 2,50 % : prime 168 000 €, valeur intrinsèque 24 000 €, valeur temps 144 000 € ; 3,40 % : prime 72 000 €, valeur intrinsèque nulle, valeur temps 72 000 € | 0,5 |
| 1.6-05 | Comparaison selon le coût, la flexibilité et le risque résiduel, et recommandation argumentée | 1 |

**Swap payeur de taux fixe (0,5 pt).** Nominal 96 000 000 € ; période de 90 jours : nominal × 90 / 360 = 24 000 000 €. Intérêts de l'emprunt = 24 000 000 × (taux variable + 1,30 %) ; différentiel du swap = 24 000 000 × (taux variable − 2,90 %).

| € | Scénario 1 : 3,80 % | Scénario 2 : 2,70 % | Scénario 3 : 1,80 % |
|---|---:|---:|---:|
| Intérêts de l'emprunt (taux + 1,30 %) | 1 224 000 | 960 000 | 744 000 |
| Différentiel du swap (+ reçu, − versé) | + 216 000 | − 48 000 | − 264 000 |
| **Coût net** | **1 008 000** | **1 008 000** | **1 008 000** |
| **Taux effectif** | **4,20 %** | **4,20 %** | **4,20 %** |

Le swap transforme l'emprunt en dette à taux fixe : 2,90 % + 1,30 % = 4,20 %, quel que soit le taux constaté.

**Tunnel (1 pt).** Prime nette = (0,30 % − 0,26 %) × 24 000 000 = **9 600 €** par période (0,04 % par an) : le floor vendu finance presque toute la prime du cap.

| € | Scénario 1 : 3,80 % | Scénario 2 : 2,70 % | Scénario 3 : 1,80 % |
|---|---:|---:|---:|
| Intérêts de l'emprunt | 1 224 000 | 960 000 | 744 000 |
| − Versement reçu du cap (taux − 3,40 %) | − 96 000 | 0 | 0 |
| + Versement payé sur le floor (2,20 % − taux) | 0 | 0 | + 96 000 |
| + Prime nette | + 9 600 | + 9 600 | + 9 600 |
| **Coût net** | **1 137 600** | **969 600** | **849 600** |
| **Taux effectif** | **4,74 %** | **4,04 %** | **3,54 %** |

**Bornes du tunnel (0,5 pt).** Taux effectif minimal = plancher + marge + prime nette annuelle = 2,20 % + 1,30 % + 0,04 % = **3,54 %** ; taux effectif maximal = 3,40 % + 1,30 % + 0,04 % = **4,74 %**. Entre les deux, le groupe paie le taux variable + 1,34 %.

**Valeur intrinsèque et valeur temps des caps (0,5 pt).** Au taux du jour (2,60 %), sur la première période (24 000 000 € × écart de taux) :

| € par période | Prime | Valeur intrinsèque | Valeur temps |
|---|---:|---:|---:|
| Cap seul 2,50 % (prime 0,70 % par an) | 0,70 % × 24 000 000 = 168 000 | (2,60 % − 2,50 %) × 24 000 000 = **24 000** | **144 000** |
| Cap 3,40 % du tunnel (prime 0,30 % par an) | 0,30 % × 24 000 000 = 72 000 | **0** (2,60 % < 3,40 %) | **72 000** |

Le cap à 2,50 % est **dans la monnaie** : sa prime comprend le gain d'un exercice immédiat (valeur intrinsèque) et une valeur temps qui rémunère la possibilité d'une hausse sur trois ans. Le cap à 3,40 % est **hors de la monnaie** : toute sa prime est de la valeur temps, qui décroît à l'approche de l'échéance et croît avec l'incertitude sur les taux. Les primes sont fournies par la banque : elles ne se calculent pas, elles se décomposent.

**Comparaison et recommandation (1 pt).**

| Critère | Swap | Tunnel |
|---|---|---|
| Coût | aucune prime ; 4,20 % certain | prime nette faible (0,04 % par an) ; 3,54 % à 4,74 % |
| Protection | complète : taux fixé | taux plafonné à 4,74 %, soit 0,54 point au-dessus du swap |
| Participation à la baisse | aucune : coût d'opportunité de 264 000 € par trimestre au scénario 3 | jusqu'au plancher de 2,20 % : 158 400 € de moins que le swap au scénario 3 |
| Flexibilité | engagement ferme ; débouclage anticipé au prix de sa valeur de marché, négative si les taux ont baissé | engagement ferme aussi (le floor est vendu) ; débouclage également coûteux |
| Risque résiduel | contrepartie ; sur-couverture si l'emprunt est remboursé par anticipation | taux variable entre 3,54 % et 4,74 % ; contrepartie |

- Le tunnel coûte moins que le swap tant que le taux constaté reste sous **2,86 %** (2,90 % − 0,04 %) ; au-delà, le swap est moins cher (écart de 129 600 € au scénario 1). Le taux du swap (2,90 %, au-dessus du taux du jour de 2,60 %) est compatible avec une légère hausse attendue par le marché, rémunération de la banque comprise.
- Le cap seul (taux maximal 2,50 % + 1,30 % + 0,70 % = 4,50 %, sous le plafond du tunnel) conserverait toute la baisse, mais sa prime de 0,70 % par an est payée dans tous les scénarios : 4,50 % aux scénarios 1 et 2, 3,80 % au scénario 3. Il n'est le moins cher dans aucun des trois scénarios : le swap l'emporte au scénario 1, le tunnel aux scénarios 2 et 3.
- **Recommandation** : le **swap**, sur la totalité du capital restant dû et sur trois ans. Il répond à la priorité du directoire (protéger les marges), fixe une charge d'intérêts prévisible pour le fonds CORVANE Infrastructures et le syndicat mixte, est simple et sans prime ; le navire de 2023 n'est pas celui que le groupe veut remplacer, ce qui limite le risque de remboursement anticipé et donc de débouclage. Le coût d'opportunité en cas de baisse est le prix de cette certitude. Le tunnel est une réponse défendable si le directoire veut garder une part de la baisse, en acceptant un plafond plus élevé.

**Réponses tolérées** : recommandation du tunnel, ou d'une combinaison (swap sur au moins 70 % du capital, tunnel ou taux variable sur le reste), si elle est argumentée par le coût, la flexibilité et le risque résiduel et reste conforme à la politique de risque ; taux effectifs présentés en % à une décimale près de l'arrondi demandé ; valeur intrinsèque et valeur temps exprimées en % annuels du nominal (0,10 % et 0,60 % pour le cap seul).

**Erreurs fréquentes**
- Inverser le sens du différentiel du swap (le payeur de fixe reçoit quand le taux variable dépasse le taux fixe) ou oublier la marge de 1,30 %.
- Oublier la prime nette du tunnel, ou la prime annuelle non proratisée (38 400 € au lieu de 9 600 €).
- Calculer une valeur temps « négative » pour le cap hors de la monnaie, ou vouloir recalculer la prime.
- `JUR-T07` — scénarios présentés sans tableau ; `JUR-T13` — recommandation sans lien avec la politique du groupe et la durée de l'emprunt.

---

### 1.7 Recommandation de synthèse au directoire (1 pt)

| Item | Attendu | Points |
|---|---|---:|
| 1.7-01 | Recommandation chiffrée, risque par risque, et vérification de la conformité à la politique du groupe | 0,5 |
| 1.7-02 | Cohérence d'ensemble, mise en œuvre et gouvernance | 0,5 |

**Recommandation et conformité (0,5 pt).**

| Risque | Recommandation | Politique du groupe | Conformité |
|---|---|---|---|
| Flux intragroupe | centre de compensation mensuel pour les refacturations ; reversement des recettes des billets à fréquence plus courte | — | gain net de 126 420 € par an |
| Livre | compensation des flux en livres, puis vente à terme des 5 400 000 GBP nets à 0,8674 (6 225 501 €) | au moins 75 %, au plus 100 % de la position nette | 100 % : conforme |
| Carburant | contrat d'échange sur 24 000 t à 615 USD/t | entre 70 % et 90 % de la consommation | 80 % : conforme |
| Dollar | achat à terme de 14 760 000 USD à 1,1292 (13 071 201 €) | au moins 75 % de la position nette | 82 % de la position de 18 M USD : conforme |
| Taux | swap à 2,90 % sur 96 M€, trois ans (taux de 4,20 %) | au moins 70 % du capital, sur au moins trois ans | 100 %, trois ans : conforme |

**Cohérence, mise en œuvre et gouvernance (0,5 pt).** Les techniques internes viennent d'abord (compensation intragroupe et des flux de même devise), puis des instruments fermes de gré à gré, simples et sans prime, adaptés à des flux certains ; aucune option n'est nécessaire sur le change, puisque les flux sont certains. Le groupe garde une part de risque : 6 000 t de carburant et 3,6 M USD non couverts, et le coût d'opportunité des instruments fermes en cas d'évolution favorable. La mise en œuvre suppose un renouvellement trimestriel glissant des couvertures, la répartition des contrats entre plusieurs banques (risque de contrepartie), un suivi de la consommation pour éviter la sur-couverture, et le compte rendu trimestriel au conseil de surveillance prévu par la politique. La politique protège la marge à court terme ; elle ne dispense pas de réduire l'exposition de fond au prix de l'énergie.

**Réponses tolérées** : toute recommandation cohérente avec les réponses précédentes du candidat (par exemple l'avance en livres ou le tunnel), si la conformité à la politique est vérifiée chiffre par chiffre.

**Erreurs fréquentes**
- Recommander de couvrir les encaissements bruts en livres (10 M GBP), ce qui dépasserait 100 % de la position nette et créerait une position spéculative interdite par la politique.
- `JUR-T01` — synthèse qui reprend les calculs sans s'adresser au directoire ; `JUR-T13` — recommandation générique, sans vérifier les seuils de la politique de risque.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme DSCG UE 2 (arrêté du 4 août 2025), partie 6.1 ; guide pédagogique DSCG, juillet 2026, p. 77 | centralisations de trésorerie, opérations intragroupe (netting) ; intérêt, prérequis et impacts, sans traitement juridique ni fiscal ; conditions bancaires fournies | [V] | F07 § 0 ; `perimetre_ue2.yaml` (6.1.a) |
| Compensation bilatérale et multilatérale | soldes nets, réduction des règlements, des frais et des conversions, centre de compensation | [S] | F07 § 3.2 et 4.1 |
| Programme DSCG UE 2, partie 6.3 ; guide pédagogique DSCG, juillet 2026, p. 78-79 | position de change courte ou longue, ouverte ou fermée ; marché au comptant et à terme ; techniques internes ; avances en devises ; contrats à terme de gré à gré ; choix selon le coût, la souplesse, la simplicité et le risque résiduel | [V] | F07 § 0 et 3 ; `perimetre_ue2.yaml` (6.3.a à 6.3.d) |
| Parité des taux d'intérêt, report et déport, avance en devises | formules usuelles, cotation au certain | [S] | F07 § 3.1 à 3.3 |
| Programme DSCG UE 2, partie 6.4 ; guide pédagogique DSCG, juillet 2026, p. 79-80 | dérivés de couverture sur les prix des matières premières ; risques physiques et de transition ; articulation avec la performance durable | [V] | F07 § 0 et 5 ; `perimetre_ue2.yaml` (6.4.a) |
| Contrat d'échange sur matière (prix fixe contre prix moyen), risque de base | mécanisme et lecture des résultats | [S] | F07 § 5 |
| Programme DSCG UE 2, partie 6.2 ; guide pédagogique DSCG, juillet 2026, p. 77-78 | relation inverse valeur-taux ; diagnostic d'une exposition à taux fixe ou variable ; swap, cap, floor, collar, primes données ; décomposition de la prime en valeur intrinsèque et valeur temps ; exclusion des modèles de valorisation des options | [V] | F07 § 0 et 2 ; `perimetre_ue2.yaml` (6.2.a à 6.2.c) |
| Swap de taux, cap, tunnel, grille de choix | mécanismes et calculs | [S] | F07 § 2.2 à 2.4 |
| Euribor 3 mois de 2,60 % ; 1 EUR = 1,1250 USD | hypothèses d'énoncé dans les fourchettes de la fiche (Euribor 3 mois 2,50 % – 2,90 % ; EUR/USD 1,10 – 1,20) | [V] séries BCE (fourchettes) | F11 § 1 et 3 |
| Cours EUR/GBP, taux de la livre et du dollar, avance, carburant, emprunt, couvertures, politique de risque | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 1.1 à 1.5 |
