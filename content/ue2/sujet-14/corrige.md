# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Sujet d'entraînement complet n° 14

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : `ue2/fiches/`. Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (investissement, emprunts, coût du capital, DCF, multiples, portefeuille, LBO, BPA, équilibre des bilans, couvertures, barème sur 50, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Risques financiers d'un armateur : compensation des flux intragroupe, position de change multidevises, carburant et taux du financement d'un navire | 16 | 1.1 à 1.7 | `exercices/ex40_risques_armateur_netting_couvertures` |
| 2 – Filialiser le terminal portuaire et l'ouvrir à un opérateur : diagnostic par secteur, évaluation de la concession et entrée d'un partenaire à 40 % | 18 | 2.1 à 2.8 | `exercices/ex41_filialisation_terminal_portuaire` |
| 3 – Remplacer un navire : information extra-financière, propulsion bas carbone sous incertitude et obligation verte enregistrée sur une blockchain | 16 | 3.1 à 3.6 | `exercices/ex42_navire_bas_carbone_obligation_verte` |
| **Total** | **50** | | |

---

## DOSSIER 1 – RISQUES FINANCIERS D'UN ARMATEUR : COMPENSATION DES FLUX INTRAGROUPE, POSITION DE CHANGE MULTIDEVISES, CARBURANT ET TAUX DU FINANCEMENT D'UN NAVIRE (16 points)

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

---

## DOSSIER 2 – FILIALISER LE TERMINAL PORTUAIRE ET L'OUVRIR À UN OPÉRATEUR : DIAGNOSTIC PAR SECTEUR, ÉVALUATION DE LA CONCESSION ET ENTRÉE D'UN PARTENAIRE À 40 % (18 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Diagnostic par secteur : marges, ROCE, flux de trésorerie, endettement ; forces et faiblesses | `1.c` Apprécier la performance opérationnelle et financière d'un groupe ; `1.a` Réaliser une analyse financière des comptes consolidés | 3,5 |
| 2.2 Lecture des comptes en IFRS | `1.b` Interpréter les états financiers des groupes en normes comptables internationales (IFRS) | 1,5 |
| 2.3 Motifs et risques de la filialisation ; rôle de holding de la SE | `4.2.b` Analyser les motifs des opérations de réorganisation ; `4.2.d` Décrypter les montages financiers avec et sans levier financier | 2 |
| 2.4 Valeur du terminal par les flux jusqu'au terme de la concession ; VGE et VCP | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `3.1.d` Distinguer la valeur globale de l'entreprise (VGE) de la valeur des capitaux propres (VCP) | 2,5 |
| 2.5 Transactions comparables | `3.2.a` Maîtriser et calculer les inducteurs de comparaison permettant de déterminer la VGE et la VCP ; `3.2.b` Savoir déterminer le multiple d'un échantillon pour valoriser l'entreprise | 2 |
| 2.6 ANCC et portée de l'approche patrimoniale | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine | 1,5 |
| 2.7 Entrée de l'opérateur : augmentation de capital réservée ou cession | `4.2.c` Analyser les opérations de fusions et d'acquisitions ; `4.2.d` | 3 |
| 2.8 Effets sur la structure financière, intérêts minoritaires et recommandation | `4.2.b` ; `4.2.d` | 2 |
| **Total** | | **18** |

Part du calcul : environ 10,5 points (2.1-01 à 2.1-04, 2.4-01 à 2.4-03, 2.5-02 et 2.5-03, 2.6-01, 2.7-01 à 2.7-04 pour l'essentiel, 2.8-01 et 2.8-02). Part de l'analyse : environ 8 points. Les questions 2.2, 2.3 et la recommandation de la question 2.8 se traitent sans les calculs des autres questions : elles ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 2.1 Diagnostic par secteur : marges, ROCE, flux de trésorerie, endettement ; forces et faiblesses (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Croissance 2026 : groupe 7,31 %, lignes 6,80 %, terminal 12,20 % ; marges d'EBITDA : groupe 16,44 % et 17,45 %, lignes 12,50 % et 13,41 %, terminal 50,00 % les deux années | 0,5 |
| 2.1-02 | Capitaux employés du groupe 598,50 et 598,00 M€ ; ROCE après impôt : groupe 3,58 % et 4,70 %, lignes 2,43 % et 3,45 %, terminal 8,15 % et 9,69 % | 1 |
| 2.1-03 | Flux disponible 33,95 et 32,40 M€ ; couverture des investissements 1,89 et 1,70 ; flux disponible après loyers 19,15 et 17,60 M€ | 0,5 |
| 2.1-04 | DFN 289,30 et 276,80 M€ ; DFN / EBITDA 4,02 et 3,38, sous les plafonds de 4,25 et 3,50 (la marge de 10,20 M€ en 2026, non demandée, est valorisée dans l'item 2.1-05) | 0,5 |
| 2.1-05 | Forces et faiblesses hiérarchisées, reliées aux chiffres et aux références sectorielles | 1 |

**Croissance et marges (0,5 pt).**

| | Lignes 2025 | Lignes 2026 | Terminal 2025 | Terminal 2026 | Groupe 2025 | Groupe 2026 |
|---|---:|---:|---:|---:|---:|---:|
| Chiffre d'affaires (M€) | 412,00 | 440,00 | 41,00 | 46,00 | 438,00 | 470,00 |
| Croissance 2026 | | **+ 6,80 %** | | **+ 12,20 %** | | **+ 7,31 %** |
| EBITDA (M€) | 51,50 | 59,00 | 20,50 | 23,00 | 72,00 | 82,00 |
| **Marge d'EBITDA** | **12,50 %** | **13,41 %** | **50,00 %** | **50,00 %** | **16,44 %** | **17,45 %** |

Le périmètre étant constant, la croissance est organique. Le chiffre d'affaires du terminal réalisé avec les clients extérieurs progresse de 15,38 % (26,00 → 30,00 M€). L'EBITDA du groupe croît de 13,89 %, presque deux fois plus vite que le chiffre d'affaires.

**Capitaux employés et ROCE (1 pt).**

| M€, au 31 décembre | 2025 | 2026 |
|---|---:|---:|
| Navires en propriété | 432,00 | 446,00 |
| Autres immobilisations des lignes | 18,00 | 18,00 |
| Droits d'utilisation | 60,00 | 48,00 |
| Droit de concession | 48,00 | 46,00 |
| Installations et engins du terminal | 70,50 | 72,00 |
| **Immobilisations** | **628,50** | **630,00** |
| Stocks + clients et autres créances | 36,00 | 41,00 |
| − Fournisseurs et autres dettes − produits constatés d'avance | − 66,00 | − 73,00 |
| **BFR** | **− 30,00** | **− 32,00** |
| **Capitaux employés** | **598,50** | **598,00** |
| Capitaux propres | 309,20 | 321,20 |
| **DFN** = emprunts + dettes locatives − trésorerie | 286,00 + 64,40 − 61,10 = **289,30** | 268,00 + 52,80 − 44,00 = **276,80** |
| **Ressources** | **598,50** | **598,00** |

Les capitaux employés des secteurs (annexe 2.2) s'additionnent : 478,00 + 120,50 = 598,50 et 478,00 + 120,00 = 598,00.

| ROCE après impôt = RO × 0,75 / capitaux employés | 2025 | 2026 |
|---|---:|---:|
| Lignes maritimes | 15,50 × 0,75 / 478,00 = **2,43 %** | 22,00 × 0,75 / 478,00 = **3,45 %** |
| Terminal | 13,10 × 0,75 / 120,50 = **8,15 %** | 15,50 × 0,75 / 120,00 = **9,69 %** |
| Groupe | 28,60 × 0,75 / 598,50 = **3,58 %** | 37,50 × 0,75 / 598,00 = **4,70 %** |

Décomposition (information) : ROCE = marge opérationnelle × (1 − 25 %) × rotation des capitaux employés. Lignes 2026 : 5,00 % × 0,75 × 0,92 ; terminal 2026 : 33,70 % × 0,75 × 0,38. Le terminal immobilise beaucoup de capital par euro de chiffre d'affaires, mais sa marge le compense largement.

**Flux de trésorerie (0,5 pt).**

| M€ | 2025 | 2026 |
|---|---:|---:|
| Flux net lié à l'activité | 71,95 | 78,40 |
| Investissements (dont flotte) | − 38,00 (− 30,00) | − 46,00 (− 36,00) |
| **Flux de trésorerie disponible** | **33,95** | **32,40** |
| **Couverture des investissements** = 71,95 / 38,00 ; 78,40 / 46,00 | **1,89** | **1,70** |
| − Loyers des navires affrétés (11,05 + 3,75 ; 11,60 + 3,20) | − 14,80 | − 14,80 |
| **Flux disponible après loyers** | **19,15** | **17,60** |
| − Intérêts bancaires (12,65 ; 11,90), dividendes (3,60 ; 4,80), remboursements nets d'emprunts (30,00 ; 18,00) | − 46,25 | − 34,70 |
| = Variation de la trésorerie | − 27,10 | − 17,10 |

L'exploitation finance largement les investissements (couverture de 1,70 à 1,89), mais le flux disponible après loyers (17,60 M€) ne couvre ni les intérêts bancaires, ni les dividendes, ni le remboursement des emprunts : la trésorerie a baissé de 44,20 M€ en deux ans (88,20 → 44,00 M€). La flotte absorbe 78,26 % des investissements de 2026.

**Endettement (0,5 pt).** DFN / EBITDA = 289,30 / 72,00 = **4,02** en 2025 et 276,80 / 82,00 = **3,38** en 2026. Le ratio baisse, surtout grâce à l'EBITDA, mais reste au-dessus de la médiane des armateurs (3,00). Il respecte le plafond (4,25 puis 3,50), avec en 2026 une marge de 3,50 × 82,00 − 276,80 = **10,20 M€** de dette, ou une baisse de l'EBITDA de 3,55 % seulement (EBITDA minimal de 79,09 M€).

**Forces et faiblesses, hiérarchisées (1 pt).**

| Forces | Faiblesses et risques |
|---|---|
| **Un terminal très rentable** : marge d'EBITDA de 50,00 % (panel : 45,00 %), ROCE de 9,69 % (panel : 8,00 %), en hausse ; il réalise 6,38 % du chiffre d'affaires consolidé mais 28,05 % de l'EBITDA et 41,33 % du résultat opérationnel, avec 20,07 % des capitaux employés | **Des lignes peu rentables** : ROCE de 3,45 % (panel : 5,00 %), marge d'EBITDA de 13,41 % (panel : 15,00 %) ; rotation faible (0,92) d'un métier à forte intensité capitalistique, dont les capitaux employés ne baissent pas |
| **Une croissance organique et un levier opérationnel** : chiffre d'affaires + 7,31 %, EBITDA + 13,89 % ; la baisse du carburant (22,37 % → 20,43 % du chiffre d'affaires) y contribue | **Un endettement élevé et une marge de sécurité étroite** : DFN / EBITDA de 3,38 pour un plafond de 3,50 ; un recul de 3,55 % de l'EBITDA (prix du carburant, trafic) suffirait à dépasser le plafond |
| **Un BFR négatif** (− 32,00 M€, environ 25 jours de chiffre d'affaires) : les clients paient leurs billets avant la traversée (produits constatés d'avance de 25,00 M€) | **Des flux insuffisants pour le service de la dette** : flux disponible après loyers de 17,60 M€, trésorerie en baisse de 44,20 M€ en deux ans |
| **Un autofinancement des investissements** (couverture de 1,70) | **Un besoin de capitaux à venir** : remplacement du plus ancien navire, affrètements qui expirent fin 2030, programme d'extension du terminal ; rentabilité de l'ensemble (4,70 %) faible pour un fonds d'infrastructure, à peine supérieure au coût net de la dette (15,10 × 0,75 / 276,80 = 4,09 % ; en 2025, 3,58 % contre 4,25 %) |

**Réponses tolérées** : capitaux employés obtenus en additionnant ceux des secteurs ; ROCE calculé sur des capitaux employés moyens s'il est annoncé (groupe 2026 : 4,70 %) ; croissance du terminal calculée sur le seul chiffre d'affaires extérieur (15,38 %) si le choix est annoncé ; flux disponible après loyers présenté comme « flux disponible comparable à celui d'un armateur propriétaire de ses navires ».

**Erreurs fréquentes**
- Calculer la marge du terminal sur son seul chiffre d'affaires extérieur (76,67 %) alors que son EBITDA comprend les redevances facturées aux lignes.
- Additionner les chiffres d'affaires des secteurs (486,00 M€) sans éliminer l'intersectoriel.
- Classer les produits constatés d'avance dans la dette financière ou oublier les droits d'utilisation dans les capitaux employés.
- Oublier les loyers des navires affrétés, classés en financement, et conclure que le groupe dégage 32,40 M€ de trésorerie libre.
- `JUR-T13` — diagnostic sans comparaison des secteurs entre eux ni avec les panels ; `JUR-T07` — ratios présentés en texte plutôt qu'en tableau.

Références : F04 § 2, § 3 et § 5 (bilan économique, ROCE, tableau des flux) [V guide p. 57-58] ; programme l. 469-473 (périmètre constant, analyse par les flux) [V].

---

### 2.2 Lecture des comptes en IFRS (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Navires affrétés au bilan : droits d'utilisation (48,00 M€) et dettes locatives (52,80 M€) ; loyers (14,80 M€) hors EBITDA et classés en financement ; conséquences pour la comparaison et pour les prêteurs (les parts de 19,08 % de la DFN et de 18,05 % de l'EBITDA sont des exemples, non exigés) | 0,5 |
| 2.2-02 | Droit de concession amorti linéairement jusqu'en 2049 : valeur comptable (46,00 M€) sans rapport avec la valeur économique, actif qui s'éteint ; horizon fini pour l'évaluation | 0,5 |
| 2.2-03 | Information sectorielle : elle révèle la rentabilité du terminal, masquée dans les comptes consolidés ; limites (redevances intersectorielles, capitaux affectés par la direction, dette non affectée) | 0,5 |

**Navires affrétés coque nue (0,5 pt).** Les comptes en IFRS privilégient la substance sur la forme : KERNAVEL contrôle l'usage des deux navires pendant huit ans et s'est engagée à payer les loyers. Ses comptes portent donc un actif (droits d'utilisation : 48,00 M€) et une dette (dettes locatives : 52,80 M€, soit 19,08 % de la DFN). Pour un investisseur ou un prêteur :
- l'EBITDA ne supporte pas les loyers (14,80 M€ par an, 18,05 % de l'EBITDA de 2026), remplacés par 12,00 M€ de dotations et 3,20 M€ d'intérêts : il faut comparer KERNAVEL à des armateurs présentés de la même façon (c'est le cas des panels) ;
- le flux lié à l'activité ne supporte pas non plus les loyers, classés en financement : le flux disponible doit être lu après loyers (17,60 M€ en 2026) ;
- la dette locative est une dette à part entière, à servir jusqu'en 2030 ; le ratio du contrat de prêt l'inclut ;
- à l'échéance des contrats, fin 2030, le groupe devra renouveler deux navires sur sept : la dette locative va disparaître, mais le besoin de navires demeure.

**Droit de concession (0,5 pt).** Le droit payé en 2010 (80,00 M€) est amorti linéairement sur quarante ans (2,00 M€ par an) : sa valeur comptable (46,00 M€) correspond aux 23 années restantes et tombera à zéro le 31 décembre 2049. Ce coût historique amorti ne dit rien de la valeur économique de la concession, qui dépend des flux restant à percevoir (question 2.4). Le résultat opérationnel du terminal supporte cette dotation, ce qui pèse sur son résultat opérationnel et donc sur son ROCE. Surtout, la concession est un actif à **durée finie** : les installations fixes reviendront sans indemnité au syndicat mixte. Un investisseur ne peut pas raisonner sur une valeur à l'infini.

**Information par secteur (0,5 pt).** Sans elle, le terminal disparaîtrait dans les comptes consolidés (6,38 % du chiffre d'affaires) : elle montre qu'il porte 28,05 % de l'EBITDA et le meilleur ROCE du groupe, ce qui fonde le projet d'ouverture de son capital. Ses limites :
- 34,78 % du chiffre d'affaires du terminal (16,00 sur 46,00 M€) provient des lignes du groupe : sa marge dépend du tarif interne, ici aligné sur les tarifs publics, mais qu'un partenaire voudra vérifier ;
- les capitaux employés sont affectés par la direction et les dettes financières ne le sont pas : le terminal porte un emprunt de 30,00 M€, non affecté au secteur, qui n'apparaît qu'au moment de l'apport ;
- les secteurs suivent l'organisation interne et ne sont pas audités comme des comptes de filiale.

**Réponses tolérées** : toute formulation qui interprète l'effet de la présentation sur l'EBITDA, la dette et les flux, sans la justifier techniquement ; mention de la juste valeur comme élément absent ici (les actifs sont au coût amorti).

**Erreurs fréquentes**
- Recalculer la dette locative ou le droit d'utilisation : le retraitement est fourni et n'a pas à être refait.
- Citer des numéros de normes ou justifier techniquement le classement des contrats : hors du champ de l'épreuve (UE 4).
- Développer le droit des concessions ou le régime des biens de la concession : seul compte l'effet sur la valeur (actif à durée finie).
- `JUR-T13` — exposé général sur les normes IFRS sans les montants de KERNAVEL.

Références : F04 § 0 et § 6 (adapter l'analyse aux spécificités IFRS, interpréter sans justifier) [V guide p. 58].

---

### 2.3 Motifs et risques de la filialisation ; rôle de holding de la SE (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Motifs reliés au cas : faire apparaître et valoriser un actif d'infrastructure très rentable ; partenaire spécialisé ; financement sans alourdir la dette des lignes ; recentrage du directoire sur les lignes et préparation du renouvellement de la flotte | 1 |
| 2.3-02 | Risques : perte de 40 % des flux de l'activité la plus rentable, conflits d'intérêts sur les tarifs et le programme (droit de veto), gouvernance partagée, dépendance à l'autorité concédante, coûts et complexité | 0,5 |
| 2.3-03 | Rôle de la SE : holding mixte (exploitation des lignes, participation de 60 % dans le terminal, filiales commerciales à 100 %) ; contrôle, remontée des dividendes, centralisation de la trésorerie et des financements, arbitrage entre les filiales | 0,5 |

**Motifs (1 pt).** L'apport partiel d'actif transfère une branche complète d'activité (actifs, BFR, salariés et dette de 30,00 M€) à une société nouvelle, contre des actions de celle-ci ; il ne fait sortir aucune trésorerie du groupe. C'est une réorganisation qui prépare l'ouverture du capital (guide, p. 69 : organisation du groupe, recentrage, création de valeur) :
- **Valoriser un actif d'infrastructure** : le terminal dégage une marge d'EBITDA de 50,00 % et un ROCE de 9,69 %, mais sa valeur est masquée dans un groupe dont le ROCE est de 4,70 %. Isolé dans une filiale, il peut être évalué et vendu en partie à un investisseur qui recherche des flux réguliers et plafonnés, typiques des infrastructures concédées.
- **Un partenaire spécialisé** : VELDRAMAR Terminals exploite onze terminaux ; il apporte des clients (autres armateurs, trafic roulier), des méthodes d'exploitation et l'expérience de l'électrification des quais. La croissance du chiffre d'affaires extérieur (+ 15,38 %) montre que le terminal peut se développer au-delà du groupe, mais il atteindra sa capacité vers 2031 : l'extension demande un savoir-faire et des capitaux que le groupe n'a pas.
- **Financer sans alourdir la dette** : le groupe est endetté (DFN / EBITDA de 3,38 pour un plafond de 3,50) et doit renouveler sa flotte. L'opérateur apporte 100,00 M€ à la filiale ou paie 60,00 M€ à la SE : des fonds propres plutôt qu'une dette nouvelle.
- **Recentrage** : le directoire concentre ses moyens et son attention sur les lignes, dont la rentabilité est insuffisante (ROCE de 3,45 %), et sur le remplacement du plus ancien navire.

**Risques (0,5 pt).**
- **Partage des flux** : la SE ne garde que 60 % des résultats et des dividendes de son activité la plus rentable (13,80 M€ d'EBITDA en quote-part, contre 23,00 M€).
- **Conflits d'intérêts** : le terminal facture 16,00 M€ par an aux lignes du groupe ; l'opérateur voudra des tarifs élevés, la SE des tarifs bas. L'accord exigé des deux associés sur les tarifs et sur le programme donne à l'opérateur un droit de blocage ; l'opérateur est aussi le concurrent possible du groupe pour d'autres concessions. Par transposition de la théorie de l'agence (Jensen et Meckling, 1976), qui porte sur les relations entre actionnaires et dirigeants, chaque associé doit surveiller l'usage que l'autre fait de la filiale : la règle d'accord des deux associés est un mécanisme de contrôle, mais elle a un coût (blocages, négociations).
- **L'autorité concédante** est aussi actionnaire de la SE à 30 % : son accord est indispensable, et ses objectifs (service public, emploi local, transition énergétique du port) ne coïncident pas toujours avec ceux du fonds CORVANE (Freeman, 1984).
- **Coûts et complexité** : frais de l'opération, structure de gouvernance à deux niveaux, perte de flexibilité dans l'usage de la trésorerie du terminal.

**Rôle de la SE (0,5 pt).** Après l'opération, KERNAVEL Lignes Atlantiques SE devient une **holding mixte** : elle exploite toujours les lignes et détient 60 % de KERNAVEL Terminaux SAS et 100 % de ses trois filiales commerciales. Son rôle :
- **contrôler** la filiale (trois membres sur cinq du comité de surveillance), condition posée par l'autorité concédante, ce qui maintient sa consolidation pour la totalité ;
- **faire remonter les dividendes** : la filiale distribuerait 80 % de son résultat, dont 60 % à la SE ;
- **centraliser** les financements et la trésorerie des filiales détenues à 100 %, la filiale du terminal ayant désormais sa propre politique financière, négociée avec l'opérateur ;
- **arbitrer** l'allocation des capitaux entre les lignes et le terminal, en associant un partenaire minoritaire au risque du terminal sans perdre le contrôle de la concession.

**Réponses tolérées** : présentation de la filialisation comme une étape de « valorisation par la séparation » ; mention du signal envoyé aux prêteurs et aux actionnaires (un opérateur spécialisé accepte de payer 150,00 M€ pour les capitaux propres) ; pour l'item 2.3-01, trois motifs reliés aux chiffres du cas suffisent pour la totalité des points.

**Erreurs fréquentes**
- Développer le régime juridique ou fiscal de l'apport partiel d'actif, le traitement de l'apport dans les comptes de la SE, ou le droit des concessions : hors du champ de l'épreuve.
- Confondre l'apport (aucune trésorerie) et la cession ou l'augmentation de capital (étape 2).
- Présenter la SE comme une holding pure : elle continue d'exploiter les lignes.
- `JUR-T13` — liste de motifs sans les chiffres du cas ; `JUR-T14` — conflit d'intérêts présenté sans cadre théorique (agence, parties prenantes).

Références : F05 § 0 (motifs des restructurations, holdings) [V guide p. 69-70] ; programme l. 552-555 [V].

---

### 2.4 Valeur du terminal par les flux jusqu'au terme de la concession ; VGE et VCP (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Flux 2027 à 2030 actualisés à 7,00 % : 13,08 ; 12,66 ; 12,24 ; 11,82, soit 49,82 M€ | 0,5 |
| 2.4-02 | Flux constants de 2031 à 2049 : 16,00 × 10,3356 = 165,37 M€ au 31/12/2030, actualisés : 165,37 × 0,762895 = 126,16 M€ | 1 |
| 2.4-03 | VGE = 49,82 + 126,16 = 175,98 M€ ; VCP = 175,98 − 30,00 = 145,98 M€ (24,33 € par action) | 0,5 |
| 2.4-04 | Absence de valeur terminale justifiée (fin de la concession, retour des installations sans indemnité, engins sans valeur, activité arrêtée) ; FTD revenant aux apporteurs de capitaux, actualisés au CMPC | 0,5 |

**Conventions rappelées** (annexes 2.4 et 2.7) : flux en fin d'année ; CMPC de 7,00 % ; formule de l'annuité pour les 19 flux de 2031 à 2049 ; VCP = VGE − 30,00 M€.

**Flux 2027 à 2030 (0,5 pt).**

| | 2027 | 2028 | 2029 | 2030 |
|---|---:|---:|---:|---:|
| FTD (M€) | 14,00 | 14,50 | 15,00 | 15,50 |
| Coefficient 1,07^−t | 0,934579 | 0,873439 | 0,816298 | 0,762895 |
| FTD actualisé | 13,08 | 12,66 | 12,24 | 11,82 |

Somme : **49,82 M€** (49,80 en additionnant les valeurs arrondies, accepté).

**Flux constants de 2031 à 2049 (1 pt).** Les 19 flux de 16,00 M€ forment une suite d'annuités constantes :
- valeur au 31 décembre 2030 : 16,00 × [1 − 1,07^−19] / 0,07 = 16,00 × (1 − 0,276508) / 0,07 = 16,00 × **10,3356** = **165,37 M€** ;
- valeur au 31 décembre 2026 : 165,37 × 1,07^−4 = 165,37 × 0,762895 = **126,16 M€**.

**VGE et VCP (0,5 pt).**
- **VGE** = 49,82 + 126,16 = **175,98 M€** : valeur de l'actif économique du terminal, qui revient aux actionnaires et aux prêteurs. Elle représente 7,65 fois l'EBITDA de 2026 et 1,47 fois les capitaux employés (120,00 M€) : le terminal crée de la valeur, puisque son ROCE (9,69 %) dépasse son CMPC (7,00 %).
- **VCP** = VGE − dette financière nette de la filiale = 175,98 − 30,00 = **145,98 M€**, soit 24,33 € par action (145,98 M€ / 6 000 000).

**Absence de valeur terminale (0,5 pt).** La méthode des flux actualise les flux de trésorerie disponibles, après impôt sur le résultat d'exploitation et investissements, qui reviennent à tous les apporteurs de capitaux : on les actualise au CMPC, puis on retranche la dette pour obtenir la VCP. Ici, l'horizon n'est pas infini : la concession prend fin le 31 décembre 2049, les installations fixes reviennent sans indemnité au syndicat mixte, les engins sont alors sans valeur et l'activité s'arrête. Aucun flux n'est perçu après 2049 : une valeur terminale de Gordon-Shapiro supposerait une exploitation perpétuelle et surévaluerait le terminal. La valeur dépend donc fortement de la durée restante et d'un éventuel renouvellement de la concession, qui n'est pas acquis.

Sensibilité (information, sans arrondi intermédiaire) : VCP de 153,91 M€ à 6,50 % et de 138,57 M€ à 7,50 %.

**Réponses tolérées** : actualisation année par année des 23 flux (même résultat) ; écarts de 0,01 à 0,02 M€ dus aux arrondis des coefficients ; flux 2031-2049 actualisés en une seule étape par la différence entre une annuité de 23 ans et une annuité de 4 ans.

**Erreurs fréquentes**
- Ajouter une valeur terminale perpétuelle (16,00 / 0,07 actualisée) : VGE de 224,19 M€ et VCP de 194,19 M€, qui ignorent la fin de la concession.
- Compter vingt flux constants au lieu de dix-neuf (VCP de 149,13 M€), ou actualiser la valeur de l'annuité sur cinq ans au lieu de quatre.
- Oublier de retrancher la dette apportée de 30,00 M€, ou retrancher la DFN du groupe (276,80 M€).
- `JUR-E01` — flux disponibles confondus avec le résultat net ou avec l'EBITDA ; `JUR-T07` — actualisation sans tableau.

Références : F03 § 2 (FTD, VGE, VCP) et F01 § 2 et § 3 (valeur actuelle d'une suite d'annuités constantes) [V guide p. 64 ; programme l. 515-519] ; Gordon et Shapiro (1956) pour la valeur terminale écartée [V programme 3.1], F10 § 2.

---

### 2.5 Transactions comparables (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Transaction F écartée (17,20, concession de 58 ans et terrains constructibles payés dans le prix) | 0,5 |
| 2.5-02 | Multiples des cinq transactions retenues : médiane 9,00 ; moyenne 9,20 | 0,5 |
| 2.5-03 | VGE 207,00 à 211,60 M€ ; VCP 177,00 à 181,60 M€ | 0,5 |
| 2.5-04 | Pertinence limitée de l'inducteur pour une concession à durée finie : multiple croissant avec la durée restante ; prime de contrôle ; part minoritaire ; comparaison avec la valeur par les flux | 0,5 |

**Exclusion de la valeur aberrante (0,5 pt).** La plateforme F (17,20 fois l'EBITDA) n'est pas comparable : sa concession court encore 58 ans, et le prix comprend 40 hectares de terrains constructibles qui ne produisent pas encore d'EBITDA. Son multiple rapporte donc à l'EBITDA une valeur qui ne vient pas de l'exploitation actuelle. Avec elle, la moyenne passerait à 10,53 et la médiane à 9,60.

**Multiples (0,5 pt).** Transactions retenues, classées : 7,40 ; 8,20 ; **9,00** ; 10,20 ; 11,20.
- Médiane (troisième valeur sur cinq) : **9,00**.
- Moyenne : (7,40 + 8,20 + 9,00 + 10,20 + 11,20) / 5 = 46,00 / 5 = **9,20**.

**Fourchette de valeur (0,5 pt).**

| Multiple | VGE = multiple × 23,00 (M€) | VCP = VGE − 30,00 (M€) | Par action |
|---|---:|---:|---:|
| Médiane 9,00 | **207,00** | **177,00** | 29,50 € |
| Moyenne 9,20 | **211,60** | **181,60** | 30,27 € |

**Pertinence de l'inducteur (0,5 pt).**
- L'EBITDA est un inducteur de VGE, avant frais financiers et indépendant de la structure financière : il convient à des terminaux financés différemment, et l'on retranche ensuite la dette de 30,00 M€.
- Mais un multiple d'EBITDA suppose que l'agrégat se maintient longtemps. Pour une **concession à durée finie**, la valeur dépend du nombre d'années restantes : dans l'échantillon, le multiple croît avec la durée (7,40 pour 14 ans, 11,20 pour 41 ans). Avec 23 ans restants, le terminal de Kervalan se situe entre B (20 ans, 8,20) et C (26 ans, 9,00) : un multiple de 8,20 donnerait une VCP de 158,60 M€.
- Les transactions portent souvent sur le contrôle (100 % ou 60 %) et intègrent une **prime de contrôle** et des synergies ; VELDRAMAR Terminals n'achètera que 40 %, une part minoritaire, même si elle est assortie d'un droit de blocage.
- Les multiples situent la valeur que le marché accorde aujourd'hui aux terminaux ; la méthode des flux (145,98 M€, soit 7,65 fois l'EBITDA) tient compte de la durée restante, des tarifs plafonnés et de la capacité atteinte en 2031. L'écart (+ 31,02 M€, + 21,25 %) s'explique par ces différences : pour une concession, la valeur par les flux est la référence principale, les multiples une valeur haute (`JUR-E03`).

**Réponses tolérées** : exclusion de la transaction A (14 ans) en plus de F, si elle est justifiée par la durée, avec les calculs cohérents ; fourchette construite à partir des transactions B et C (158,60 à 177,00 M€) si le choix est expliqué par la durée restante.

**Erreurs fréquentes**
- Garder la plateforme F : moyenne de 10,53 et VCP de 212,19 M€.
- Prendre la moyenne des deux valeurs centrales alors que l'échantillon retenu compte cinq transactions.
- Ne pas retrancher la dette (VGE de 207,00 M€ présentée comme valeur des titres).
- Appliquer le multiple à l'EBITDA prévisionnel de 2027 alors que l'annexe 2.7 retient celui de 2026.
- `JUR-E03` — valeurs juxtaposées sans fourchette ni confrontation avec la valeur par les flux.

Références : F03 § 3 (inducteurs, multiple d'un échantillon, médiane, primes et décotes) [V guide p. 65 ; programme l. 521-528].

---

### 2.6 ANCC et portée de l'approche patrimoniale (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | ANCC = 90,00 + 6,00 − 2,00 − 25 % × 4,00 = 93,00 M€, soit 15,50 € par action | 1 |
| 2.6-02 | Portée limitée : la valeur d'une concession est celle de ses flux ; actifs de retour sans valeur de revente, droit non cessible séparément ; l'ANCC (93,00 M€) est un plancher, très inférieur à la valeur par les flux (145,98 M€) | 0,5 |

**ANCC (1 pt).**

| M€ | Montant |
|---|---:|
| Capitaux propres comptables (actif net comptable) : 125,00 − 30,00 − 5,00 | 90,00 |
| + Plus-value sur les engins mobiles : 20,00 − 14,00 | + 6,00 |
| − Remise en état des passerelles, non provisionnée | − 2,00 |
| − Impôt latent : 25 % × (6,00 − 2,00) | − 1,00 |
| **= ANCC** | **93,00** |
| **Valeur par action** : 93,00 M€ / 6 000 000 | **15,50 €** |

Le droit de concession et les installations fixes restent à leur valeur nette comptable (annexe 2.6) ; aucun actif fictif n'est à retrancher.

**Portée limitée (0,5 pt).**
- L'approche patrimoniale évalue l'entreprise par la valeur de ses actifs diminuée de ses dettes. Elle convient aux sociétés dont les actifs sont séparables et ont un marché (sociétés immobilières, holdings, entreprises en difficulté).
- La valeur d'une concession tient au **droit d'exploiter** pendant 23 ans et aux flux qu'il procure, pas à des actifs revendables : les installations fixes reviendront sans indemnité au syndicat mixte, et le droit, inscrit au coût historique amorti, ne se cède pas séparément de l'exploitation. Seuls les engins (20,00 M€) ont une valeur de marché.
- L'ANCC (93,00 M€) ignore la rentabilité du terminal et les éléments non inscrits au bilan (clientèle des autres armateurs, contrat de services portuaires, savoir-faire des équipes) : la valeur par les flux le dépasse de 52,98 M€ (1,57 fois). C'est une **valeur plancher**, utile pour vérifier que le prix proposé (150,00 M€, 1,61 fois l'ANCC) ne brade pas les actifs, et qui diminuera mécaniquement avec l'amortissement du droit jusqu'en 2049.

**Réponses tolérées** : ANCC sans impôt latent (94,00 M€) : 0,5 point sur 1, l'annexe 2.7 imposant l'impôt latent ; ANC calculé comme total de l'actif moins dettes.

**Erreurs fréquentes**
- Ajouter la valeur de marché des engins (20,00 M€) au lieu de la plus-value (6,00 M€).
- Appliquer l'impôt latent à la seule plus-value et pas à la charge de remise en état (ANCC de 92,50 M€).
- Calculer un goodwill par la rente : il n'est pas demandé et aucune donnée ne le permet.
- `JUR-T13` — portée de l'approche patrimoniale exposée sans référence à la concession et à sa durée.

Références : F03 § 4 (ANC, ANCC, limites) [V guide p. 65-66 ; corrigé du sujet zéro p. 106].

---

### 2.7 Entrée de l'opérateur : augmentation de capital réservée ou cession (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Valeur de 150,00 M€ située : + 2,75 % (+ 4,02 M€) par rapport à la valeur par les flux (145,98 M€), sous les multiples (177,00 à 181,60 M€), au-dessus de l'ANCC (93,00 M€) ; valeur acceptable (par exemple : VGE implicite de 180,00 M€, 7,83 fois l'EBITDA, non exigée) | 0,5 |
| 2.7-02 | Augmentation de capital réservée : prix d'émission 25,00 € ; 6 000 000 × 40 / 60 = 4 000 000 actions nouvelles ; montant levé 100,00 M€ reçu par la filiale ; 10 000 000 actions et valeur de 250,00 M€ après l'opération ; SE 60 %, opérateur 40 % | 1 |
| 2.7-03 | Cession : 2 400 000 actions cédées à 25,00 €, soit 60,00 M€ reçus par la SE, 54,00 M€ après impôt ; la SE garde 3 600 000 actions sur 6 000 000 (60 %) ; la filiale ne reçoit rien | 0,5 |
| 2.7-04 | Valeur détenue par la SE : 147,59 M€ (+ 1,61) avec l'augmentation de capital ; 141,59 M€ (− 4,39 ; + 1,61 avant impôt) avec la cession ; interprétation (prime payée par l'opérateur, neutralité d'une émission au prix de marché, coût de l'impôt) | 1 |

**Situer la valeur proposée (0,5 pt).**

| Méthode | VCP (M€) | Par action |
|---|---:|---:|
| ANCC (question 2.6) | 93,00 | 15,50 € |
| Flux actualisés jusqu'en 2049 (question 2.4) | 145,98 | 24,33 € |
| **Offre de VELDRAMAR Terminals** | **150,00** | **25,00 €** |
| Transactions comparables, médiane et moyenne (question 2.5) | 177,00 à 181,60 | 29,50 à 30,27 € |

L'offre dépasse la valeur par les flux de 4,02 M€ (+ 2,75 %) et l'ANCC de 61 % (1,61 fois) ; elle est inférieure de 15,25 % à la valeur par la médiane des transactions, qui portent sur des concessions plus longues et sur le contrôle. Elle correspond à une VGE de 150,00 + 30,00 = 180,00 M€, soit 7,83 fois l'EBITDA de 2026, un peu moins que la transaction B (8,20 ; 49 %, 20 ans). Pour une part de 40 %, sans le contrôle, elle est acceptable : elle se situe au-dessus de la valeur de référence pour une concession.

**Augmentation de capital réservée (1 pt).**
- Prix d'émission : 150,00 M€ / 6 000 000 = **25,00 €** par action.
- Nombre d'actions nouvelles n tel que n / (6 000 000 + n) = 40 % : n = 6 000 000 × 40 / 60 = **4 000 000 actions**.
- Montant levé : 4 000 000 × 25,00 € = **100,00 M€**, reçus par **la filiale** (pour rembourser l'emprunt de 30,00 M€ puis financer le programme de 70,00 M€).
- Après l'opération : 10 000 000 actions ; valeur des capitaux propres de 150,00 + 100,00 = **250,00 M€** ; KERNAVEL détient 6 000 000 actions (**60 %**), VELDRAMAR Terminals 4 000 000 (**40 %**).

**Cession d'actions existantes (0,5 pt).**
- Actions cédées : 40 % × 6 000 000 = **2 400 000** ; prix : 2 400 000 × 25,00 € = **60,00 M€**, reçus par **la SE** ; après l'impôt de 6,00 M€ : **54,00 M€**.
- Le nombre d'actions reste de 6 000 000 : KERNAVEL en garde 3 600 000 (**60 %**), VELDRAMAR Terminals en détient 2 400 000 (**40 %**). La filiale ne reçoit aucune trésorerie et doit emprunter 70,00 M€ pour son programme.

| | Augmentation de capital réservée | Cession |
|---|---:|---:|
| Actions de la filiale après l'opération | 10 000 000 | 6 000 000 |
| Actions de VELDRAMAR Terminals | 4 000 000 (40 %) | 2 400 000 (40 %) |
| Prix par action | 25,00 € | 25,00 € |
| Somme payée par l'opérateur | 100,00 M€ | 60,00 M€ |
| Trésorerie reçue | filiale : 100,00 M€ | SE : 60,00 M€ (54,00 M€ après impôt) |

**Valeur détenue par la SE (1 pt).** Avant l'opération, la SE détient 100 % de la VCP par les flux, 145,98 M€.
- **Augmentation de capital** : 60 % × (145,98 + 100,00) = **147,59 M€**, soit **+ 1,61 M€**. L'émission au prix de 25,00 € (supérieur à la valeur par les flux de 24,33 €) fait profiter la SE d'une part de la prime payée par l'opérateur. Au prix proposé, la dilution de la SE est de 40 points en pourcentage, mais pas en valeur : 60 % de 250,00 M€ valent 150,00 M€, ce que valaient ses 100 % avant l'opération.
- **Cession** : 60 % × 145,98 + 54,00 = **141,59 M€**, soit **− 4,39 M€** ; avant impôt, le gain serait le même (+ 1,61 M€ : 60,00 − 40 % × 145,98). L'impôt sur le résultat de cession (6,00 M€) est un coût que l'augmentation de capital évite.
- L'opérateur paie 1,61 M€ de plus que 40 % de la valeur par les flux dans les deux cas : c'est la prime qu'il accepte pour ses synergies (réseau, clients, électrification). Il préfère l'augmentation de capital, qui finance le programme qu'il demande sans endetter la filiale.

**Réponses tolérées** : écart de l'offre de 2,75 % ou 2,76 % selon que la VCP est prise arrondie (145,98) ou non (145,978) ; valeur détenue par la SE calculée avec la valeur de 150,00 M€ au lieu de la valeur par les flux (neutralité exacte : 150,00 M€ dans les deux cas avant impôt, 144,00 M€ après impôt pour la cession) si l'hypothèse est annoncée ; nombre d'actions nouvelles obtenu par 100,00 M€ / 25,00 € une fois le montant déduit de la part visée ; présentation du gain en pourcentage.

**Erreurs fréquentes**
- Émettre 40 % de 6 000 000, soit 2 400 000 actions nouvelles : l'opérateur ne détiendrait que 2 400 000 / 8 400 000 = 28,57 % du capital.
- Calculer le prix d'émission sur la valeur après l'opération (250,00 / 6 000 000), ou appliquer 40 % à la valeur de 150,00 M€ pour le montant levé (60,00 M€) dans la modalité 1.
- Oublier l'impôt sur le résultat de cession, ou le calculer soi-même au lieu d'utiliser le montant fourni.
- Conclure que l'augmentation de capital « dilue » la SE sans distinguer la part du capital (− 40 points) et la valeur détenue.
- `JUR-T13` — comparaison sans les chiffres (100,00 et 60,00 M€, 147,59 et 141,59 M€) ; `JUR-T07` — modalités comparées sans tableau.

Références : F05 § 4 et § 5 (augmentation de capital, nombre d'actions à créer, répartition du capital, prime payée) [V guide p. 69] ; F03 § 8 (réconciliation des méthodes) [V guide p. 64-66].

---

### 2.8 Effets sur la structure financière, intérêts minoritaires et recommandation (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.8-01 | Juste après l'opération : DFN 176,80 M€ et ratio 2,16 (augmentation de capital) ; DFN 222,80 M€ et ratio 2,72 (cession) | 0,5 |
| 2.8-02 | Après le programme : DFN 246,80 M€ et ratio 3,01 (marge de 40,20 M€ sous le plafond de 287,00 M€) ; DFN 292,80 M€ et ratio 3,57, au-dessus du plafond de 3,50 (dépassement de 5,80 M€) | 0,5 |
| 2.8-03 | Intérêts minoritaires : 76,00 ou 36,00 M€ dans les capitaux propres consolidés ; part de l'opérateur dans le résultat de 2027 : 4,80 ou 4,40 M€ ; EBITDA consolidé inchangé alors que la SE ne détient plus que 60 % du terminal | 0,5 |
| 2.8-04 | Recommandation argumentée et conditions | 0,5 |

**Dette nette et ratio pro forma (1 pt).** EBITDA consolidé : 82,00 M€ dans tous les cas ; plafond : 3,50 × 82,00 = 287,00 M€ de DFN.

| M€ | Augmentation de capital réservée | Cession |
|---|---:|---:|
| DFN consolidée au 31/12/2026 | 276,80 | 276,80 |
| − Trésorerie reçue par le groupe | − 100,00 (filiale) | − 54,00 (SE, après impôt) |
| **DFN juste après l'opération** | **176,80** | **222,80** |
| **Ratio DFN / EBITDA** | **2,16** | **2,72** |
| + Programme d'investissement du terminal | + 70,00 (trésorerie) | + 70,00 (emprunt de la filiale) |
| **DFN après le programme** | **246,80** | **292,80** |
| **Ratio DFN / EBITDA** | **3,01** | **3,57** |
| Marge sous le plafond (287,00 − DFN) | 40,20 | − 5,80 |

- Les deux modalités réduisent d'abord la DFN consolidée : la filiale restant consolidée pour la totalité, la trésorerie qu'elle reçoit compte dans la dette nette du groupe. Le remboursement de l'emprunt de 30,00 M€ par la filiale ne change pas la DFN (moins de trésorerie, moins de dette).
- Une fois le programme réalisé, l'écart vient de l'origine des fonds : avec l'augmentation de capital, l'opérateur finance le programme par des fonds propres ; avec la cession, l'opérateur paie la SE et le programme est financé par la dette. Le ratio (3,57) dépasserait alors le plafond de 3,50, en attendant les effets du programme sur l'EBITDA (à partir de 2030). Ce pro forma est statique : il ignore les flux de 2027 à 2029, qui réduiraient la dette (− 12,50 M€ en 2026 ; à ce rythme, environ 255 M€ et un ratio d'environ 3,11 fin 2029 avec la cession), et le financement du navire neuf, qui l'augmenterait.
- La trésorerie de 100,00 M€ appartient toutefois à la filiale et sert au terminal : la SE ne peut pas l'utiliser pour ses navires, sauf par les dividendes, dont 40 % reviennent à l'opérateur. Les 54,00 M€ de la cession, eux, sont à la libre disposition de la SE.

**Intérêts minoritaires (0,5 pt).** La filiale reste contrôlée : ses actifs, ses dettes et son résultat restent consolidés pour la totalité, et la part de VELDRAMAR Terminals apparaît en **intérêts minoritaires** : 76,00 M€ (modalité 1) ou 36,00 M€ (modalité 2) dans les capitaux propres consolidés, et 40 % du résultat de la filiale, soit 40 % × 12,00 = **4,80 M€** ou 40 % × 11,00 = **4,40 M€** en 2027. Pour les actionnaires de la SE :
- l'EBITDA consolidé (82,00 M€) et le ratio DFN / EBITDA comptent encore 100 % du terminal, alors que la SE n'en détient plus que 60 % (13,80 M€ d'EBITDA en quote-part) : le ratio consolidé améliore l'apparence de l'endettement plus que la capacité de remboursement de la SE ;
- le résultat net part du groupe et les dividendes remontés diminuent (60 % de 80 % du résultat de la filiale, soit 5,76 M€ en 2027 avec la modalité 1) ; la rentabilité des capitaux propres doit désormais distinguer la part du groupe et celle des minoritaires ;
- les capitaux propres consolidés augmentent, mais une partie appartient à l'opérateur.

**Recommandation (0,5 pt).** Toute recommandation cohérente avec les calculs est acceptée. Exemple :
- **Privilégier l'augmentation de capital réservée** à 25,00 € par action : elle respecte le plafond des prêts après le programme (3,01, marge de 40,20 M€), finance l'électrification des quais et l'extension par des fonds propres, crée un peu de valeur pour la SE (+ 1,61 M€) sans impôt, et répond à la préférence de l'opérateur, ce qui facilite la négociation. Elle s'écarte du financement hiérarchique (Myers et Majluf, 1984), qui ferait passer la dette avant l'émission d'actions. Mais la capacité d'endettement du groupe est presque épuisée (3,38 pour un plafond de 3,50), et les actions sont souscrites par un opérateur informé, qui paie une prime : le coût lié à l'asymétrie d'information, qui fonde cette hiérarchie, est ici limité.
- **Limites** : la SE ne reçoit pas de trésorerie pour remplacer son navire ; elle devra le financer autrement (dette adossée au navire, une fois le ratio redescendu, ou cession ultérieure d'une partie de ses actions de la filiale). La cession, qui apporte 54,00 M€ à la SE, ne se justifierait que si le programme était différé ou réduit.
- **Conditions** : tarifs du contrat de services portuaires fixés pour dix ans et indexés, pour limiter les conflits d'intérêts ; maintien du contrôle (trois membres sur cinq) exigé par le syndicat mixte ; droit de blocage de l'opérateur limité au budget du programme ; politique de distribution de la filiale (80 %) inscrite dans les statuts ; suivi de la VAN du programme, supposée nulle mais incertaine.

**Réponses tolérées** : recommandation de la cession si le candidat montre qu'elle finance la SE et propose de différer ou de réduire le programme pour rester sous le plafond ; solution mixte (une augmentation de capital plus petite et une cession), si elle est chiffrée ou argumentée ; ratios calculés après remboursement de l'emprunt de 30,00 M€ (identiques) ; candidat qui relève que le pro forma ignore les flux de 2027 à 2029 et le financement du navire neuf, si la recommandation reste argumentée.

**Erreurs fréquentes**
- Ne retenir aucun effet de l'augmentation de capital sur la DFN consolidée, au motif que les fonds restent dans la filiale.
- Retirer le terminal de l'EBITDA consolidé ou n'en garder que 60 % : la filiale reste contrôlée et consolidée pour la totalité.
- Omettre l'impôt sur le résultat de cession dans la trésorerie reçue par la SE (DFN de 216,80 M€).
- Confondre intérêts minoritaires et dette financière.
- `JUR-T01` — recommandation sans conditions ni posture de conseil au directoire ; `JUR-T05` — ignorer le syndicat mixte et l'électrification des quais.

Références : F04 § 4 (DFN / EBITDA, plafond bancaire) [V corrigé du sujet zéro p. 104] ; F05 § 0 (holdings, structure du capital) [V guide p. 70] ; Myers et Majluf (1984) [V programme 7.2], F10 § 3.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 57-58 ; programme l. 465-473 | diagnostic consolidé à périmètre constant, bilan économique, ROCE, analyse par les flux, lecture des comptes en IFRS sans justification technique | [V] | F04 § 0, § 2, § 3, § 5 et § 6 |
| Guide pédagogique DSCG, juillet 2026, p. 64 ; programme l. 509-519 | flux de trésorerie disponibles, CMPC, passage de la VGE à la VCP | [V] | F03 § 2 |
| Guide pédagogique DSCG, juillet 2026, p. 65 ; programme l. 521-528 | inducteurs de VGE, multiple d'un échantillon, médiane, moyenne, fourchette | [V] | F03 § 3 |
| Guide pédagogique DSCG, juillet 2026, p. 65-66 ; programme l. 531 | ANC, ANCC, limites de l'approche patrimoniale | [V] | F03 § 4 |
| Guide pédagogique DSCG, juillet 2026, p. 69-70 ; programme l. 552-555 | motifs des réorganisations, apport partiel d'actif, augmentation de capital, holdings | [V] | F05 § 0 |
| Corrigé du sujet zéro, p. 104 | DFN / EBITDA et seuil bancaire | [V] | F04 § 4 |
| Jensen et Meckling (1976) | théorie de l'agence, transposée à la surveillance entre associés de la filiale | [V programme 2.1] | F10 § 3 |
| Freeman (1984) | parties prenantes (autorité concédante, salariés, port) | [V programme 2.1] | F10 § 3 |
| Myers et Majluf (1984) | financement hiérarchique, dont l'augmentation de capital s'écarte | [V programme 7.2] | F10 § 3 |
| Gordon et Shapiro (1956) | valeur terminale à croissance constante, écartée ici | [V programme 3.1] | F10 § 2 |
| Comptes, secteurs, panels, prévisions, CMPC, transactions, bilan de la filiale, offre, impôt sur la cession, intérêts minoritaires | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 2.1 à 2.6 |

---

## DOSSIER 3 – REMPLACER UN NAVIRE : INFORMATION EXTRA-FINANCIÈRE, PROPULSION BAS CARBONE SOUS INCERTITUDE ET OBLIGATION VERTE ENREGISTRÉE SUR UNE BLOCKCHAIN (16 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Enjeux extra-financiers, intensités carbone, communication et double matérialité du prix du carbone | `2.1.a` Identifier les éléments extra-financiers pour le diagnostic, dans la lignée du modèle d'affaires de l'entreprise ; `2.1.b` Interpréter le reporting RSE et de durabilité ; `2.1.d` Maîtriser le principe de double matérialité | 3 |
| 3.2 Note extra-financière de HALVARÈNE Gestion, portée et limites | `2.1.c` Utiliser les outils de notation financière et extra-financière | 1,5 |
| 3.3 Bêta, rentabilité exigée des fonds propres et CMPC du projet | `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 2 |
| 3.4 VAN, TRI, VAN probabilisée et choix de la propulsion | `7.1.a` Évaluer et classer des projets en milieu certain ; `7.1.b` Évaluer et classer des projets en milieu incertain | 5 |
| 3.5 Coût actuariel des deux obligations vertes, conditions de l'appellation | `7.2.a` Comparer les sources de financement et notamment leurs coûts ; `7.2.c` Analyser les nouveaux outils de financement | 1,5 |
| 3.6 Émission enregistrée sur une blockchain, nouveaux acteurs et recommandation | `5.4.a` Repérer le rôle du numérique et des algorithmes (IA) dans la finance ; `5.4.b` Comprendre le rôle des nouveaux acteurs ; `7.2.c` | 3 |
| **Total** | | **16** |

Part du calcul : environ 7,5 points (3.1-02, la moitié de 3.1-04, 3.2-01, 3.3-01, 3.3-02, 3.4-01 à 3.4-04, 3.5-01 et le tiers de 3.6-02). Part de l'analyse : environ 8,5 points. Le dossier est le dernier de l'épreuve : les questions 3.4 et 3.6, qui demandent une recommandation, ne doivent pas être sacrifiées faute de temps (`JUR-T15`).

---

### 3.1 Enjeux extra-financiers, intensités carbone, communication et double matérialité du prix du carbone (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Enjeux reliés au modèle d'affaires d'un armateur de ferries : E (émissions et prix du carbone, pollution de l'air dans les ports, biodiversité marine) ; S (sécurité des passagers et des navigants, conditions de travail et recrutement des navigants, desserte des territoires) ; G (actionnaire majoritaire et collectivité concédante, conseil de surveillance, rémunération du directoire sans critère climatique) ; liens avec la rentabilité, les risques et l'accès au financement | 0,75 |
| 3.1-02 | Intensités (tableau) : passagers **150,00 ; 152,00 ; 150,00** g par passager-km ; fret **50,00 ; 51,00 ; 52,00** g par tonne-km | 0,75 |
| 3.1-03 | Commentaire : intensité des passagers stable (0,00 %), intensité du fret en hausse (+ 4,00 %), émissions totales en hausse (+ 6,23 %) ; affirmation trop flatteuse : la baisse de 10 % par passager (63,00 → 56,70 kg) vient de la baisse de 10 % de la distance moyenne, pas d'un progrès de la flotte ; « trajectoire d'une flotte décarbonée » non étayée (aucun navire remplacé, flotte de 21 ans) ; risque d'écoblanchiment | 0,75 |
| 3.1-04 | Double matérialité du prix du carbone : impact (380 950 t de CO2 en 2026) et effet financier (quotas **17,10 M€**, soit **20,85 %** de l'EBITDA ; surcharge de 6,84 M€, 40 % du coût ; coût net **10,26 M€**, **12,51 %** de l'EBITDA) ; le classement « faible » de la matérialité financière n'est pas défendable : l'enjeu est élevé sur les deux plans | 0,75 |

**Les enjeux extra-financiers d'un armateur de ferries (0,75 pt).** L'information extra-financière complète le diagnostic financier : elle éclaire les risques et les opportunités qui pèseront sur les flux futurs et sur l'accès au financement. Les enjeux se lisent à partir du modèle d'affaires de KERNAVEL : des navires lourds en capitaux, à longue durée de vie, qui brûlent du carburant pour transporter des passagers (62 % du chiffre d'affaires) et du fret.
- **Environnement** : le **climat** est l'enjeu central (380 950 t de CO2 en 2026, coût des quotas, exigences des chargeurs et des financeurs, risque d'actifs dépréciés pour des navires de vingt ans) ; la **pollution de l'air** dans les ports (soufre, oxydes d'azote, particules) touche les riverains de Kervalan et des ports d'escale ; la **biodiversité marine** (bruit, collisions avec les cétacés).
- **Social** : la **sécurité** des passagers et des navigants (le taux de fréquence baisse de 24,5 à 20,5, mais reste élevé), enjeu humain, de réputation et d'assurance ; les **conditions de travail** des 1 450 navigants (rotations longues, officiers difficiles à recruter), qui conditionnent la capacité à armer les navires ; la desserte des territoires et l'emploi local, attendus par le syndicat mixte du port.
- **Gouvernance** : un fonds majoritaire (65 %) et une collectivité concédante (30 %), aux horizons différents ; un conseil de surveillance où siège un seul membre indépendant ; une rémunération variable du directoire fondée sur l'EBITDA et le flux de trésorerie, sans critère climatique, alors que la décarbonation conditionne la valeur à long terme. Dans la lecture de Jensen et Meckling (1976), la rémunération est un mécanisme d'alignement : elle oriente ici les dirigeants vers la performance de court terme. La lecture partenariale de Freeman (1984) rappelle que chargeurs, passagers, salariés et collectivités sont aussi des parties prenantes du choix du navire.

**Intensités carbone (0,75 pt).** Convention de l'annexe 3.6 : intensité = émissions (t) / activité (millions de passagers-km ou de tonnes-km), soit des grammes par passager-km ou par tonne-km ; deux décimales.

| | 2024 | 2025 | 2026 | Variation 2024-2026 |
|---|---:|---:|---:|---:|
| Passagers : 138 600 / 924 ; 142 880 / 940 ; 141 750 / 945 (g par passager-km) | **150,00** | **152,00** | **150,00** | 0,00 % |
| Fret : 220 000 / 4 400 ; 229 500 / 4 500 ; 239 200 / 4 600 (g par tonne-km) | **50,00** | **51,00** | **52,00** | + 4,00 % |
| Émissions par passager transporté (kg) : 138 600 / 2,20 ; … | 63,00 | 60,80 | 56,70 | − 10,00 % |
| Émissions totales (t) | 358 600 | 372 380 | 380 950 | + 6,23 % |

**Commentaire et affirmation trop flatteuse (0,75 pt).**
- L'intensité carbone des **passagers** ne baisse pas : 150 g par passager-km en 2024 comme en 2026, après une hausse en 2025. Celle du **fret** augmente de 4,00 %. Les émissions totales progressent de 6,23 %, plus vite que l'activité de fret (+ 4,55 % de tonnes-km) et autant que la consommation de carburant (+ 6,28 %).
- L'affirmation « nos émissions par passager ont baissé de 10 % » est **exacte mais trompeuse** : la baisse (63,00 kg à 56,70 kg) s'explique entièrement par la **baisse de 10 % de la distance moyenne** (420 km à 378 km), parce que la croissance du trafic vient de la ligne la plus courte. Rapportées au passager-km, seule mesure de l'efficacité de la flotte, les émissions sont stables. L'indicateur choisi dans la communication mesure le mix des lignes, pas la performance environnementale.
- La « trajectoire d'une flotte décarbonée » n'est étayée par aucun indicateur : aucun navire n'a été remplacé depuis 2023, les navires en propriété ont 21 ans en moyenne, et la part des escales branchées à quai ne dépasse pas 9 %.
- Le choix d'un indicateur flatteur expose le groupe à un reproche d'**écoblanchiment**, au moment même où il veut convaincre des chargeurs et des investisseurs de financer un navire bas carbone. L'information extra-financière doit être cohérente avec les indicateurs publiés (2.1.b).

**Double matérialité du prix du carbone (0,75 pt).** Selon le principe de double matérialité (fiche commune § 1), un enjeu est matériel s'il l'est par ses **impacts** (effets de l'entreprise sur les personnes et l'environnement) ou par ses **effets financiers** (sur la performance, les flux de trésorerie, l'accès au financement ou le coût du capital), ou par les deux.
- **Matérialité d'impact** : les navires de KERNAVEL ont émis 380 950 t de CO2 en 2026, en hausse ; le groupe contribue au changement climatique. Le classement « élevée » est justifié.
- **Matérialité financière** : le prix du carbone touche directement la marge. Coût des quotas 2026 = 228 000 × 75 € = **17,10 M€**, soit 17,10 / 82 = **20,85 %** de l'EBITDA. La surcharge carbone n'en couvre que 6,84 / 17,10 = **40 %** : le coût net est de **10,26 M€**, soit **12,51 %** de l'EBITDA et 2,18 points de marge d'EBITDA (17,45 % en 2026). Une hausse de 10 € du quota coûterait 2,28 M€ de plus par an (2,78 % de l'EBITDA). S'y ajoutent les effets sur l'accès au financement : les chargeurs, les banques et les investisseurs (HALVARÈNE Gestion) demandent des preuves de décarbonation.
- Le classement « faible » retenu pour la matérialité financière n'est donc **pas défendable** : la surcharge ne couvre pas le coût, les passagers n'en paient aucune, et le prix du quota est appelé à augmenter (annexe 3.3). L'enjeu climatique est matériel sur les deux plans, et c'est précisément ce qui justifie d'étudier la propulsion du navire de remplacement.

**Réponses tolérées** : intensités exprimées en kg par millier de passagers-km ; variation des émissions par passager calculée sur 2025-2026 si le candidat compare aussi à la distance ; enjeux présentés sans le classement E, S, G s'ils sont reliés au modèle d'affaires ; coût net rapporté au chiffre d'affaires (2,18 %) plutôt qu'à l'EBITDA.

**Erreurs fréquentes**
- Recalculer les émissions à partir de la consommation de carburant : elles sont fournies.
- Valider l'affirmation au motif que le chiffre de 10 % est exact, sans voir l'effet de la distance moyenne.
- Rapporter les émissions du fret aux passagers-km, ou additionner passagers-km et tonnes-km.
- `JUR-D01` — confondre la démarche RSE de l'entreprise et les critères ESG des investisseurs ; `JUR-T05` — traiter l'extra-financier sans lien avec la marge ; `JUR-T13` — enjeux génériques, sans les données du cas.

---

### 3.2 Note extra-financière de HALVARÈNE Gestion, portée et limites (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Points des critères (2 ; 2 ; 2 ; 3 ; 4 ; 3 ; 1) ; scores des piliers : E **2,00**, S **3,50**, G **2,00** ; score global **2,45**, note **C** | 0,75 |
| 3.2-02 | Portée : note inférieure au seuil B des fonds de HALVARÈNE Gestion, effet sur l'accès aux investisseurs verts et sur le coût ; faiblesses à corriger (intensités, branchement à quai, rémunération) ; limites : grille propre à un investisseur, pondérations et appréciations subjectives, indicateurs d'une année passée, intensités et non émissions totales, divergence entre agences, règlement européen de 2024 sur la notation ESG | 0,75 |

**Calcul de la note (0,75 pt).** Règles de l'annexe 3.2 : borne incluse ; score global = Σ poids × points ; échelle A ≥ 4,00, B ≥ 3,00, C ≥ 2,00, D.

| Pilier | Critère | Valeur 2026 | Points | Poids | Poids × points |
|---|---|---:|---:|---:|---:|
| E | Intensité carbone des passagers | 150,00 g (≤ 170) | 2 | 20 % | 0,40 |
| E | Intensité carbone du fret | 52,00 g (≤ 60) | 2 | 20 % | 0,40 |
| E | Escales branchées à quai | 9 % (≥ 5 %) | 2 | 10 % | 0,20 |
| S | Taux de fréquence des navigants | 20,5 (≤ 25) | 3 | 15 % | 0,45 |
| S | Conditions de travail à bord | analyste | 4 | 15 % | 0,60 |
| G | Équilibre du conseil de surveillance | analyste | 3 | 10 % | 0,30 |
| G | Rémunération variable liée au climat | aucun critère | 1 | 10 % | 0,10 |
| | **Score global** | | | 100 % | **2,45** |

- Scores des piliers : E = (0,40 + 0,40 + 0,20) / 0,50 = **2,00** ; S = (0,45 + 0,60) / 0,30 = **3,50** ; G = (0,30 + 0,10) / 0,20 = **2,00**.
- Score global 2,45 : note **C** (de 2,00 à moins de 3,00).

**Portée et limites (0,75 pt).**
- **Portée pour le groupe** : avec la note C, KERNAVEL n'atteint pas le seuil B que retiennent les fonds de HALVARÈNE Gestion ; une obligation verte ne leur serait proposable qu'à la condition dérogatoire de l'annexe 3.5 (actif qui réduit d'au moins 80 % les émissions). Une note faible restreint le cercle des investisseurs et peut renchérir le financement. La grille montre aussi où agir : les deux intensités carbone et le branchement à quai (pilier E à 2,00) et la rémunération du directoire (critère à 1 point), qu'un critère climatique d'au moins 20 % de la part variable porterait à 5 points (+ 0,40 point de score global, non exigé). Le social est le point fort (3,50).
- **Limites** : la note dépend d'une grille propre à un investisseur (choix des critères, pondérations, paliers) ; deux critères sur sept reposent sur l'appréciation d'un analyste ; elle mesure l'année 2026 et ne voit pas le navire de remplacement, qui entrera en service en 2030 ; les intensités ne disent rien de la hausse des émissions totales ; les notations ESG des différents fournisseurs divergent souvent. Parce qu'elle publie ses notes, HALVARÈNE Gestion entre dans le champ du règlement européen sur la notation ESG : depuis le 2 juillet 2026, les fournisseurs de notations ESG exerçant dans l'Union doivent être agréés par l'AEMF, qui les surveille (les fournisseurs déjà actifs relèvent d'un régime transitoire le temps de leur demande d'agrément) : publication des méthodes, notes E, S et G distinctes ou information sur la pondération (ici, les trois scores de pilier sont publiés), information de l'entité notée avant publication pour corriger une erreur de fait (F08 § 3.2). La note éclaire la décision ; elle ne remplace pas l'analyse.

**Réponses tolérées** : score global calculé pilier par pilier (0,50 × 2,00 + 0,30 × 3,50 + 0,20 × 2,00 = 2,45) ; scores des piliers non calculés si le score global et la note sont justes (0,5 sur 0,75 à l'item 3.2-01) ; limites présentées sans référence au règlement européen.

**Erreurs fréquentes**
- Placer l'intensité carbone des passagers (150) dans le palier « ≤ 140 », ou noter 9 % d'escales branchées dans le palier inférieur.
- Faire la moyenne simple des points (2,43) au lieu de la moyenne pondérée.
- `JUR-T10` — commenter la note sans la calculer, ou l'inverse ; `JUR-T13` — limites générales des notations, sans les critères de la grille.

---

### 3.3 Bêta, rentabilité exigée des fonds propres et CMPC du projet (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Bêta d'actif moyen (0,64 + 0,70 + 0,76) / 3 = **0,70** ; bêta des capitaux propres = 0,70 × (1 + 0,75 × 40 / 60) = **1,05** | 0,5 |
| 3.3-02 | Rentabilité exigée des fonds propres = 4,0 % + 1,05 × 5,0 % = **9,25 %** ; coût net de la dette 5,00 % × 0,75 = 3,75 % ; CMPC = 60 % × 9,25 % + 40 % × 3,75 % = **7,05 %** | 0,75 |
| 3.3-03 | Lien risque / rentabilité : seul le risque systématique (bêta) est rémunéré ; risque d'exploitation des armateurs et risque financier de la dette ; taux propre au projet : le CMPC du groupe mêle le terminal et les lignes ; l'incertitude sur le prix du quota est traitée par les scénarios, pas par le taux ; les flux d'exploitation s'actualisent au CMPC | 0,75 |

**Bêta et rentabilité exigée (1,25 pt).** Formule de l'annexe 3.4 (Hamada, avec impôt, dette sans risque) ; structure cible en valeur : dette / capitaux propres = 40 / 60.
- Bêta de l'actif économique retenu : (0,64 + 0,70 + 0,76) / 3 = **0,70**.
- Bêta des capitaux propres du projet : 0,70 × [1 + (1 − 0,25) × 40 / 60] = 0,70 × 1,50 = **1,05**.
- MEDAF (Sharpe, 1964) : rentabilité exigée des fonds propres = 4,0 % + 1,05 × 5,0 % = **9,25 %**.
- Coût de la dette après impôt : 5,00 % × (1 − 0,25) = 3,75 %.
- **CMPC du projet** = 0,60 × 9,25 % + 0,40 × 3,75 % = 5,55 % + 1,50 % = **7,05 %**.

**Lien entre le risque du projet et la rentabilité exigée (0,75 pt).**
- Un investisseur n'accepte un risque plus élevé que contre une rentabilité espérée plus élevée. Dans le MEDAF, seul le **risque systématique**, mesuré par le bêta, est rémunéré : le risque propre à une entreprise peut être éliminé par la diversification. Le bêta d'actif de 0,70 mesure la sensibilité de l'activité d'armateur de ferries à la conjoncture (tourisme, échanges de marchandises), amplifiée par des coûts fixes élevés.
- Sans dette, les actionnaires exigeraient 4,0 % + 0,70 × 5,0 % = 7,50 % (non exigé). La dette (40 %) ajoute un **risque financier** : le bêta des capitaux propres passe à 1,05 et la rentabilité exigée à 9,25 %. Le CMPC (7,05 %) est inférieur à 7,50 % parce que les intérêts sont déductibles.
- **Pourquoi un taux propre au navire** : le taux d'actualisation doit refléter le risque du projet, pas celui de l'entreprise qui l'entreprend. Le CMPC du groupe mêle les lignes maritimes et le terminal, exploité en concession jusqu'en 2049 avec des recettes plus régulières : un taux unique sous-estimerait le risque des navires et ferait accepter des projets maritimes trop risqués (et rejeter à tort des projets peu risqués). D'où le recours au bêta d'armateurs comparables, réendetté à la structure financière cible du navire.
- Les flux du navire sont des flux d'exploitation, avant rémunération des prêteurs et des actionnaires : ils s'actualisent au **CMPC**, pas à la rentabilité exigée des fonds propres (9,25 %). L'incertitude sur le prix du quota, propre au projet, est traitée par les **scénarios** de la question 3.4 et non par une prime ajoutée au taux, ce qui la compterait deux fois.

**Réponses tolérées** : bêta réendetté écrit 0,70 × (1 + 0,75 × 0,6667) ; CMPC de 7,05 % présenté directement comme 9,25 % × 0,6 + 5 % × 0,75 × 0,4.

**Erreurs fréquentes**
- Réendetter avec dette / valeur totale (0,40) au lieu de dette / capitaux propres (0,6667) : bêta de 0,91 et rentabilité exigée de 8,55 %.
- Pondérer le CMPC par 40 / 60 au lieu de 40 % et 60 %, ou oublier l'impôt sur le coût de la dette (CMPC de 7,55 %).
- Actualiser les flux du navire à 9,25 %.
- `JUR-E02` — coût du capital d'un projet sans cotation par comparables : bêtas d'actif, réendettement, MEDAF, CMPC, avec la formule donnée ; `JUR-T04` — acquis du DCG.

---

### 3.4 VAN, TRI, VAN probabilisée et choix de la propulsion (5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Flux nets annuels (EBITDA × 0,75 + 0,25 × amortissement) : A **17,85 ; 16,35 ; 14,10** M€ ; B **21,02 ; 20,90 ; 20,72** M€ (scénarios bas, central, haut) ; valeur résiduelle ajoutée en année 20 | 1 |
| 3.4-02 | VAN au CMPC de 7,05 %, scénario central : A **32,23 M€** ; B **35,42 M€** | 0,75 |
| 3.4-03 | TRI, scénario central : A **9,73 %** ; B **9,30 %** (9,75 % et 9,31 % par interpolation entre 9 % et 10 %) | 0,75 |
| 3.4-04 | VAN par scénario : A 48,06 ; 32,23 ; 8,48 ; B 36,69 ; 35,42 ; 33,52 ; espérance A **30,25**, B **35,26** ; écart-type A **14,13**, B **1,13** | 1 |
| 3.4-05 | Classement et conflit : la VAN classe B, le TRI classe A ; causes (tailles différentes, mesure absolue ou relative, hypothèse de réinvestissement) ; résolution par les flux différentiels B − A : 46,00 M€ de plus, VAN **3,19 M€** > 0 (TRI de 7,90 % > 7,05 %) | 0,75 |
| 3.4-06 | Recommandation : B, plus forte espérance de VAN et risque bien plus faible (B domine A) ; B ne perd que dans le scénario bas ; risques non chiffrés (prix du méthanol après dix ans, prime des chargeurs après cinq ans, technologie nouvelle) | 0,75 |

**Conventions rappelées** (annexes 3.3 et 3.6) : date 0 = 1er janvier 2030 ; investissement payé à la date 0 ; vingt flux de fin d'année ; amortissement linéaire sur 20 ans (A : 7,20 M€, B : 9,50 M€) ; IS de 25 % ; valeur résiduelle nette d'impôt ajoutée au flux de l'année 20 ; CMPC de 7,05 % ; coefficients non arrondis, flux et VAN au centième.

**Flux nets de trésorerie (1 pt).** EBITDA du navire = recettes − charges − énergie − quotas ; flux = EBITDA − IS, avec IS = 25 % × (EBITDA − amortissement), soit EBITDA × 0,75 + 0,25 × amortissement.

| M€ par an | A bas (60 €) | A central (100 €) | A haut (160 €) | B bas (60 €) | B central (100 €) | B haut (160 €) |
|---|---:|---:|---:|---:|---:|---:|
| Recettes − charges − énergie | 24,40 | 24,40 | 24,40 | 25,10 | 25,10 | 25,10 |
| − Quotas (50 000 t ou 4 000 t × prix) | − 3,00 | − 5,00 | − 8,00 | − 0,24 | − 0,40 | − 0,64 |
| = EBITDA du navire | 21,40 | 19,40 | 16,40 | 24,86 | 24,70 | 24,46 |
| − IS : 25 % × (EBITDA − amortissement de 7,20 ou 9,50) | − 3,55 | − 3,05 | − 2,30 | − 3,84 | − 3,80 | − 3,74 |
| **= Flux net (années 1 à 20)** | **17,85** | **16,35** | **14,10** | **21,02** | **20,90** | **20,72** |
| Flux de l'année 20, valeur résiduelle comprise (14,4 ou 19,0) | 32,25 | 30,75 | 28,50 | 40,02 | 39,90 | 39,72 |

**VAN du scénario central (0,75 pt).** Les flux étant constants, VAN = − I + F × [1 − 1,0705^−20] / 0,0705 + VR × 1,0705^−20, avec un facteur d'annuité de 10,5530 et un coefficient de 0,2560 (valeurs non arrondies dans le calcul).
- A : − 144,00 + 16,35 × 10,5530 + 14,4 × 0,2560 = − 144,00 + 172,54 + 3,69 = **32,23 M€** ;
- B : − 190,00 + 20,90 × 10,5530 + 19,0 × 0,2560 = − 190,00 + 220,56 + 4,86 = **35,42 M€**.

Les deux propulsions créent de la valeur au CMPC du projet.

**TRI du scénario central (0,75 pt).**
- A : VAN à 9 % = 7,82 ; à 10 % = − 2,66 ; TRI = 9 % + 1 % × 7,82 / (7,82 + 2,66) = 9,75 % par interpolation (**9,73 %** pour la valeur exacte).
- B : VAN à 9 % = 4,18 ; à 10 % = − 9,24 ; TRI = 9 % + 1 % × 4,18 / (4,18 + 9,24) = 9,31 % par interpolation (**9,30 %**).

Les deux TRI dépassent le CMPC de 7,05 %.

**VAN probabilisée (1 pt).** VAN de chaque scénario, même méthode ; espérance = Σ probabilité × VAN ; variance = Σ probabilité × (VAN − espérance)².

| | Bas (p = 0,25) | Central (p = 0,50) | Haut (p = 0,25) | Espérance | Écart-type | Coefficient de variation |
|---|---:|---:|---:|---:|---:|---:|
| VAN de A (M€) | 48,06 | 32,23 | 8,48 | **30,25** | **14,13** | 0,47 |
| VAN de B (M€) | 36,69 | 35,42 | 33,52 | **35,26** | **1,13** | 0,03 |

- A : espérance = 0,25 × 48,06 + 0,50 × 32,23 + 0,25 × 8,48 = **30,25 M€** ; variance = 0,25 × 17,81² + 0,50 × 1,98² + 0,25 × (− 21,77)² = 199,74 ; écart-type **14,13 M€**.
- B : espérance = 0,25 × 36,69 + 0,50 × 35,42 + 0,25 × 33,52 = **35,26 M€** ; variance = 1,28 ; écart-type **1,13 M€**.
- La VAN de A dépend fortement du prix du quota (chaque euro de plus par tonne retire 0,05 × 0,75 × 10,5530 = 0,40 M€ de VAN) ; celle de B, qui émet 92 % de moins, y est presque insensible.

**Classement et conflit entre la VAN et le TRI (0,75 pt).**

| Critère (scénario central) | A : gazole marin | B : méthanol et batteries | Classement |
|---|---:|---:|---|
| VAN (M€) | 32,23 | 35,42 | B |
| TRI | 9,73 % | 9,30 % | A |
| Espérance de la VAN (M€) | 30,25 | 35,26 | B |
| Écart-type de la VAN (M€) | 14,13 | 1,13 | B (moins risqué) |

- **Le conflit** : la VAN, mesure **absolue** de la valeur créée, classe B en tête ; le TRI, mesure **relative** (rentabilité par euro investi), classe A. Les deux projets n'ont pas la même taille (190,00 contre 144,00 M€). Le TRI suppose en outre que les flux sont réinvestis au TRI du projet, la VAN qu'ils le sont au CMPC, hypothèse plus prudente et commune aux deux projets.
- **La résolution** : choisir B revient à investir **46,00 M€ de plus** pour obtenir des flux supplémentaires de 4,55 M€ par an (9,15 M€ en année 20, valeur résiduelle comprise). Ce supplément a une VAN de 35,42 − 32,23 = **3,19 M€** et un TRI de 7,90 %, supérieur au CMPC : il crée de la valeur. Les deux VAN sont égales pour un taux de 7,90 % (taux d'indifférence) ; au CMPC de 7,05 %, B l'emporte. Les projets étant exclusifs et le groupe pouvant financer l'une ou l'autre propulsion (annexe 3.3), il n'y a pas de rationnement du capital : on retient la plus forte VAN.

**Recommandation (0,75 pt).** Exemple de réponse : retenir la **propulsion B**.
- B a la plus forte **espérance de VAN** (35,26 contre 30,25 M€) et un risque beaucoup plus faible (écart-type de 1,13 contre 14,13 M€) : au sens de la relation rentabilité-risque, B domine A. Elle ne perd que dans le scénario bas (VAN de 36,69 contre 48,06 M€) ; à 160 €, l'écart atteint 25,04 M€ en sa faveur. Les VAN sont égales pour un prix moyen du quota de 91,23 € (non exigé) : B l'emporte dès que le prix dépasse ce niveau, soit avec une probabilité de 0,75 selon les scénarios.
- B réduit l'exposition du groupe au prix du carbone, priorité du directoire (protéger les marges), et rend le navire éligible à un financement vert (questions 3.5 et 3.6) ; elle répond aux attentes des chargeurs et améliorera les intensités carbone notées par HALVARÈNE Gestion.
- **Réserves**, qui ne sont pas dans les scénarios : le prix du méthanol n'est garanti que dix ans et un seul des deux producteurs européens est sous contrat ; la prime bas carbone (2,5 M€ par an, soit 2,5 × 0,75 × 10,5530 = 19,79 M€ de VAN, non exigé) n'est assurée que cinq ans ; la technologie est nouvelle pour les équipages (formation, entretien des batteries) ; le prix du contrat d'énergie, environ 48 % au-dessus de celui du gazole à énergie égale (14,0 M€ pour l'équivalent de 12 000 t, contre 12,6 M€ pour 16 000 t), est favorable au regard des prix actuels du méthanol renouvelable. Le directoire devrait sécuriser l'approvisionnement et allonger les engagements des chargeurs avant de commander le navire.

**Réponses tolérées** : TRI de 9,75 % et 9,31 %, résultats de l'interpolation prévue par l'annexe 3.6 ; TRI par interpolation entre d'autres taux encadrants ; VAN différentielle calculée directement sur les flux B − A ; écart-type calculé sur les VAN arrondies (mêmes résultats) ; recommandation de A si le candidat la fonde sur une anticipation explicite d'un prix du quota inférieur à 91 € ou sur le risque technologique, en reconnaissant que B a la plus forte espérance de VAN (0,25 sur 0,75 à l'item 3.4-06).

**Erreurs fréquentes**
- Déduire l'amortissement des flux, ou oublier l'économie d'impôt qu'il procure (flux de A de 14,55 M€ au lieu de 16,35 M€ dans le scénario central).
- Oublier la valeur résiduelle, ou l'actualiser comme un flux annuel.
- Calculer la variance avec n − 1, ou sans les probabilités.
- Retenir A au motif que son TRI est le plus élevé, sans voir la différence de taille.
- `JUR-I05` — calculer la VAN et le TRI sans analyser leur divergence ; `JUR-T04` — actualisation ou interpolation non maîtrisées ; `JUR-T07` — flux présentés sans tableau.

---

### 3.5 Coût actuariel des deux obligations vertes, conditions de l'appellation (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 3.5-01 | Flux de l'émetteur : offre 1 + 75,088 puis − 3,774 par an et − 79,774 en année 7, coût **5,17 %** ; offre 2 + 75,62 puis − 3,69 et − 79,69, coût **4,94 %** ; l'offre 2 coûte 0,23 point de moins | 0,75 |
| 3.5-02 | Obligation verte : fonds affectés à des projets environnementaux, sélection des projets, gestion des fonds, rapport d'affectation et d'impact revu par un examinateur externe ; appellation européenne facultative (taxonomie comme grille de lecture, examinateur enregistré auprès de l'AEMF) ; conditions pour KERNAVEL : fonds affectés au navire B, qui réduit les émissions de 92 % (≥ 80 %), d'où l'accès aux fonds de HALVARÈNE Gestion malgré la note C ; avec la propulsion A, pas d'obligation verte | 0,75 |

**Coût actuariel (0,75 pt).** Annexe 3.6 : flux de l'émetteur, montant net reçu positif ; coupons et frais annuels en fin d'année ; remboursement in fine en année 7.

| M€ | Année 0 | Années 1 à 6 | Année 7 |
|---|---:|---:|---:|
| Offre 1 : 76 × (1 − 1,20 %) ; − (76 × 4,90 % + 0,05) ; − 76 | + 75,088 | − 3,774 | − 79,774 |
| Offre 2 : 76 × (1 − 0,50 %) ; − (76 × 4,75 % + 0,08) ; − 76 | + 75,620 | − 3,690 | − 79,690 |

- Offre 1 : valeur actuelle des flux à 5 % = − 0,7616 ; à 6 % = + 3,4758 ; par interpolation 5,18 % (**5,17 %** pour la valeur exacte).
- Offre 2 : à 4 % = − 4,2813 ; à 5 % = + 0,2565 ; par interpolation **4,94 %**.
- L'offre 2 est moins chère de **0,23 point** : coupon plus bas (4,75 % contre 4,90 %) et frais initiaux plus faibles (0,38 contre 0,912 M€), malgré 0,03 M€ par an de tenue du registre. Après impôt, le classement est le même : tous les frais et les coupons sont déductibles (non exigé). Les deux coûts sont proches du coût de la dette retenu dans le CMPC (5,00 %).

**Ce qui fait une obligation verte (0,75 pt).**
- Une obligation verte est une obligation classique dont les fonds sont **affectés** à des projets ayant un bénéfice environnemental. Les standards de marché (Green Bond Principles de l'ICMA) en retiennent quatre composantes : **utilisation des fonds**, **sélection** des projets, **gestion** des fonds jusqu'à leur affectation, **rapport** (reporting) d'affectation et d'impact, avec une revue externe (F08 § 5.1). Elle se distingue d'une obligation liée à la durabilité, dont les fonds sont libres et le coupon indexé sur des objectifs.
- L'**obligation verte européenne** est une appellation facultative mais protégée : fonds affectés à des activités conformes à la taxonomie (qui sert de grille de lecture de la « part verte »), fiche d'information et rapports d'affectation revus par un examinateur externe enregistré auprès de l'AEMF (règlement (UE) 2023/2631, F08 § 5.2).
- **Conditions pour KERNAVEL** : les 76 M€ financeraient le seul navire à propulsion au méthanol, qui réduit les émissions donnant lieu à restitution de 50 000 à 4 000 t par an, soit **− 92 %** par rapport au navire de référence ; le groupe publierait chaque année l'affectation des fonds et les émissions évitées, revues par un examinateur externe. Noté C par HALVARÈNE Gestion (question 3.2), le groupe reste admis dans ses fonds grâce à la règle dérogatoire (réduction d'au moins 80 %). Avec la propulsion A, l'émission ne pourrait pas être présentée comme verte : le choix de la question 3.4 conditionne aussi l'accès à ces investisseurs.

**Réponses tolérées** : coût de l'offre 1 de 5,18 % par interpolation ; coûts estimés par la formule approchée (coupon + frais annuels / nominal + frais initiaux / durée), si le classement est juste et la méthode signalée comme approchée (0,5 sur 0,75 à l'item 3.5-01) ; coûts après impôt calculés en plus.

**Erreurs fréquentes**
- Oublier les frais annuels (coûts de 5,11 % et 4,84 %) ou les frais initiaux.
- Confondre obligation verte (fonds affectés) et prêt ou obligation indexés sur la durabilité.
- `JUR-T04` — taux actuariel non maîtrisé ; `JUR-T12` — définition approximative du financement vert.

---

### 3.6 Émission enregistrée sur une blockchain, nouveaux acteurs et recommandation (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.6-01 | Principe : les obligations sont émises et inscrites sur un registre partagé et infalsifiable (blockchain) sous forme de jetons ; elles restent des obligations ; règlement et paiement des coupons automatisés par un programme ; cadre expérimental européen (régime pilote) | 0,75 |
| 3.6-02 | Apports, chiffrés : règlement le jour même au lieu de cinq jours ouvrés ; coût plus bas (0,532 M€ de frais initiaux et 0,084 M€ par an en moins ; 4,94 % contre 5,17 %) ; accès à de nouveaux investisseurs (souscription minimale de 100 000 €, gestionnaires d'actifs européens dont HALVARÈNE Gestion) ; préparation plus courte | 0,75 |
| 3.6-03 | Risques : placement non garanti (annulation sous 60 M€, aucune émission de plus de 50 M€ sur la plateforme) ; liquidité réelle faible ; risque opérationnel et cyber (programme, portefeuilles numériques, dépendance à la plateforme) ; cadre encore expérimental ; risque de réputation | 0,75 |
| 3.6-04 | Rôle des nouveaux acteurs (plateforme de négociation et de règlement, banque agent, teneurs de portefeuilles numériques, supervision de l'AMF) et recommandation argumentée | 0,75 |

**Principe (0,75 pt).** Une blockchain est un registre partagé entre plusieurs participants, dont les inscriptions, validées selon des règles communes, ne peuvent pas être modifiées après coup ; elle permet de se passer d'un teneur de registre central. La **tokenisation** consiste à émettre et à inscrire sur ce registre des titres financiers sous forme de **jetons** : ici, chaque jeton représente une obligation de KERNAVEL. Les droits des investisseurs ne changent pas : il s'agit toujours d'une obligation verte à 4,75 %, remboursable in fine dans sept ans ; seuls le registre, la livraison et le paiement changent. Le règlement-livraison est simultané (les jetons contre les euros, le jour même) et les coupons sont versés automatiquement par un programme inscrit sur la blockchain (« contrat intelligent »). TALMERAN Titres Numériques opère dans le cadre du **régime pilote européen**, cadre d'expérimentation des infrastructures de marché fondées sur ces registres (F06 § 6). L'approche reste celle des principes et des enjeux financiers, sans technique informatique.

**Apports (0,75 pt).**
- **Règlement plus rapide** : le jour même, contre cinq jours ouvrés ; les fonds sont disponibles plus tôt et le risque de défaut d'une contrepartie entre la signature et le paiement disparaît.
- **Coût** : moins d'intermédiaires (pas d'arrangeur, registre et paiements automatisés) ; frais initiaux de 0,38 M€ contre 0,912 M€ (**0,532 M€** de moins), coupon plus bas de 0,15 point ; au total **0,084 M€** par an de moins malgré la tenue du registre, et un coût actuariel de **4,94 %** contre **5,17 %**.
- **Nouveaux investisseurs** : la souscription minimale de 100 000 € et l'accès des gestionnaires d'actifs européens, des banques privées et des trésoreries d'entreprises élargissent la base d'investisseurs au-delà de quelques assureurs français ; HALVARÈNE Gestion n'est présente que dans l'offre 2. La possibilité de revendre les jetons sur le système de TALMERAN explique en partie le coupon plus bas.
- **Délai** de préparation plus court (6 semaines contre 10) et, non exigé, **traçabilité** : le registre pourrait porter l'affectation des fonds et les données du rapport vert, ce qui rend l'engagement environnemental plus vérifiable et réduit l'asymétrie d'information avec les investisseurs (Akerlof, 1970).

**Risques (0,75 pt).**
- **Risque de placement** : l'offre 2 n'est pas garantie ; l'émission est annulée si les souscriptions n'atteignent pas 60 M€, alors que TALMERAN n'a jamais placé plus de 50 M€. Or le financement du navire doit être certain. Les investisseurs de l'offre 1 sont déjà engagés sur la totalité.
- **Liquidité** : la négociation est possible mais les échanges sont encore peu nombreux ; un investisseur pourrait ne pas trouver d'acheteur, ce qui limitera la demande ou le prix lors d'une prochaine émission.
- **Risque opérationnel et cyber** : erreur dans le programme qui paie les coupons, perte ou vol des accès aux portefeuilles numériques, panne ou attaque de la plateforme ; **dépendance** à un acteur jeune, qui concentre des fonctions habituellement séparées ; si TALMERAN cessait son activité, il faudrait transférer le registre.
- **Cadre encore expérimental** : le régime pilote est un cadre d'expérimentation, limité, dont les règles peuvent évoluer pendant les sept ans de l'obligation. Une difficulté sur une première émission « verte et numérique » serait aussi un **risque de réputation** pour le groupe.

**Les nouveaux acteurs et la recommandation (0,75 pt).**
- **Rôle des nouveaux acteurs** : TALMERAN Titres Numériques, fintech autorisée par l'AMF, réunit l'émission, la tenue du registre, le règlement-livraison et la négociation, fonctions que se partagent d'ordinaire l'arrangeur, le dépositaire central, la banque teneur de comptes et le marché ; la **banque agent** fait le lien avec les paiements en euros ; des banques ou des prestataires agréés tiennent les **portefeuilles numériques** des investisseurs ; l'**AMF** autorise et surveille la plateforme. Ces acteurs désintermédient en partie le financement obligataire et le rendent accessible à des émetteurs de taille moyenne non cotés comme KERNAVEL. Les banques traditionnelles ne disparaissent pas : elles deviennent agents, conservateurs ou investisseurs.
- **Recommandation** (exemple de réponse) : retenir l'**offre 2**, moins chère de 0,23 point et seule à ouvrir l'accès à HALVARÈNE Gestion et à de nouveaux investisseurs, **à condition** de sécuriser le montant : obtenir de la banque VAUNOIRE ou d'une autre banque un engagement de prendre la part non souscrite, ou prévoir de lancer l'offre 1 si les souscriptions n'atteignent pas 76 M€. L'avantage de coût (0,084 M€ par an et 0,532 M€ de frais initiaux) est réel mais modeste à l'échelle d'un navire de 190 M€ : il ne justifie pas de prendre un risque sur le financement. Une émission verte, transparente et vérifiable, est aussi un signal de l'engagement climat du groupe, crédible parce qu'il est coûteux (Spence, 1973). À défaut d'une solution de repli, l'offre 1, plus chère mais certaine, est préférable.

**Réponses tolérées** : recommandation de l'offre 1 pour la certitude du placement et la simplicité, si elle est justifiée par les risques et chiffrée (écart de 0,23 point) ; recommandation de l'offre 2 sans solution de repli, si le risque de placement est reconnu (0,5 sur 0,75 à l'item 3.6-04) ; présentation de la blockchain comme « registre distribué » ou « technologie des registres partagés ».

**Erreurs fréquentes**
- Présenter les jetons comme des crypto-actifs spéculatifs : ce sont des obligations, avec les droits d'un créancier ; leur statut juridique n'est pas à analyser (UE 1).
- Développer la technique informatique (consensus, cryptographie, clés) au lieu des enjeux financiers (UE 5).
- Retenir l'offre 2 sur le seul coût, sans voir que le placement n'est pas garanti.
- `JUR-M02` — nouveaux acteurs du financement à comparer selon le profil de l'entreprise et des investisseurs ; `JUR-T01` — recommandation sans posture de conseil ; `JUR-T15` — dernière question bâclée faute de temps.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Guide pédagogique DSCG, juillet 2026, p. 59-61 ; programme l. 475-490 | information extra-financière du diagnostic, lecture des indicateurs ESG, cohérence entre engagements et indicateurs, score sur une grille fournie, double matérialité | [V] | F08 § 0, 2 et 3 |
| Fiche commune CSRD, ESRS et double matérialité, § 1 et 5 | matérialité d'impact et matérialité financière (accès au financement, coût du capital) ; état de durabilité publié volontairement | [V dans la fiche commune] | fiche commune |
| Règlement (UE) 2024/3005, art. 2, 15, 23 et 51 à 53 | notation ESG réglementée depuis le 2 juillet 2026 (agrément par l'AEMF, régime transitoire pour les fournisseurs déjà actifs), notes E, S, G distinctes, information de l'entité notée avant publication | [V] | F08 § 3.2 |
| Guide pédagogique DSCG, juillet 2026, p. 74-75 ; F02 § 2, 3 et 5 | lien entre risque et rentabilité exigée, MEDAF, réendettement du bêta (Hamada avec IS), CMPC | [V] | F02 |
| Guide pédagogique DSCG, juillet 2026, p. 80-81 ; programme l. 643-647 | VAN, TRI, projets mutuellement exclusifs, conflit de classement, espérance et écart-type de la VAN | [V] | F01 § 4 et 5 |
| Guide pédagogique DSCG, juillet 2026, p. 81-82 ; programme l. 653-666 | coût actuariel des financements, financements durables et verts | [V] | F01 § 3 ; F08 § 5 |
| Green Bond Principles (ICMA) | quatre composantes d'une obligation verte | [S] | F08 § 5.1 |
| Règlement (UE) 2023/2631, art. 1, 3, 4, 10, 11 et 22 | obligation verte européenne : appellation protégée, fonds conformes à la taxonomie, examinateur externe enregistré auprès de l'AEMF | [V] | F08 § 5.2 |
| Programme l. 599-604 | numérique, blockchain, systèmes privés d'échange de titres, nouveaux acteurs | [V] | F06 § 0 et 6 |
| Régime pilote européen des infrastructures de marché fondées sur la blockchain (règlement (UE) 2022/858) | cadre d'expérimentation de la négociation et du règlement de titres tokenisés | [S] | F06 § 6 |
| Jensen et Meckling (1976) | théorie de l'agence, alignement des dirigeants par la rémunération | [V programme 2.1] | F10 § 3 |
| Freeman (1984) | parties prenantes, valeur partenariale | [V programme 2.1] | F10 § 3 |
| Sharpe (1964) | MEDAF | [S] | F10 § 2 |
| Akerlof (1970) ; Spence (1973) | asymétrie d'information ; signal coûteux et crédible | [V programme 5.1 et 4.1] | F10 § 1 et 3 |
| Taux sans risque de 4,0 % et prime de risque du marché de 5,0 % ; bêtas d'actif de 0,64 à 0,76 ; coût de la dette de 5,00 % | hypothèses d'énoncé, dans les fourchettes de F11 | [S] | F11 § 1 à 3 |
| Indicateurs, quotas et prix du quota, grille de notation, propulsions, scénarios, offres d'obligation | hypothèses d'énoncé, à utiliser telles quelles | — | annexes 3.1 à 3.5 |
