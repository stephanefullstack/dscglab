# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 2 — Dossier 2 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F07 risques de taux et de change, trésorerie, climat ; F08 gouvernance et ESG (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (cours à terme, option de change, swap, cap, option climatique, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des instruments et des textes, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat.

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Position de change et achat à terme | `6.3.a` Caractériser la position de change ; `6.3.b` marché comptant et à terme | 3 |
| 2.2 Option de change | `6.3.d` Contrats à terme et optionnels (change) | 3 |
| 2.3 Swap et cap | `6.2.b` Principaux instruments de couverture du risque de taux | 4 |
| 2.4 Option climatique | `6.4.a` Instruments de couverture des risques liés au changement climatique | 3 |
| 2.5 Discussion | `6.4.a` ; `2.1.d` double matérialité | 2 |
| **Total** | | **15** |

---

### 2.1 Position de change et achat à terme (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Position courte en USD, risque d'appréciation du dollar | 1 |
| 2.1-02 | Cours à terme 1,1239 et coût 1 779 518 € | 1 |
| 2.1-03 | Explication par le différentiel de taux (report de l'euro) | 1 |

**Position (1 pt).** ORVANE doit payer 2 000 000 USD dans 90 jours sans détenir de dollars : elle a une **position courte** et **ouverte** en dollars. Elle supporte un **risque de transaction** : si le dollar s'**apprécie**, ce qui correspond au certain à une **baisse** du cours EUR/USD, il lui faudra davantage d'euros pour régler sa dette. À 1,0800, la commande coûterait 2 000 000 / 1,08 = 1 851 852 €, soit 66 138 € de plus qu'au cours du jour [F07 § 3.1].

**Cours à terme (1 pt).**

F = 1,1200 × (1 + 4,00 % × 90/360) / (1 + 2,60 % × 90/360) = 1,1200 × 1,0100 / 1,0065 = 1,123895, soit **1,1239**.

Coût de la commande couverte à terme : 2 000 000 / 1,1239 = **1 779 518 €**, connu dès le 31/12/2026. Au comptant du jour : 2 000 000 / 1,1200 = 1 785 714 €.

**Pourquoi le terme est plus favorable (1 pt).** Le cours à terme se déduit de la parité des taux d'intérêt. Le dollar est mieux rémunéré que l'euro (4,00 % contre 2,60 %) : il cote en **déport**, et l'euro en **report** (F > S, + 39 points). À terme, un euro achète donc davantage de dollars qu'au comptant. Pour livrer des dollars dans trois mois, la banque emprunte des euros à 2,60 %, les convertit au comptant et place les dollars à 4,00 % ; elle répercute ce différentiel dans le cours à terme. L'économie de 6 196 € n'est pas un gain de change : elle traduit le différentiel de taux d'intérêt sur 90 jours.

**Réponses tolérées** : cours à terme non arrondi (1,123895, coût 1 779 526 €) ; raisonnement par les points de swap.

**Erreurs fréquentes**
- Inverser le sens du risque : un importateur craint la hausse de la devise qu'il doit payer, pas sa baisse.
- Inverser les taux dans la formule (euro au numérateur) en cotation au certain : on obtient 1,1161, cours incohérent avec un taux du dollar plus élevé.

---

### 2.2 Option de change (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Prime 21 429 €, VI nulle, VT = prime | 1 |
| 2.2-02 | Coûts dans les deux scénarios et comparaison | 1 |
| 2.2-03 | Recommandation argumentée | 1 |

**Prime et décomposition (1 pt).** Prime = 2 000 000 × 1,2 % = 24 000 USD, soit 24 000 / 1,12 = **21 429 €**. Au 31/12/2026, le prix d'exercice (1,1200) est égal au cours comptant : l'option est **à la monnaie**. Son exercice immédiat ne rapporterait rien : **valeur intrinsèque = 0**. Toute la prime est de la **valeur temps**, dite aussi valeur spéculative (21 429 €) : elle rémunère la possibilité que le dollar s'apprécie d'ici l'échéance [F07 § 3.3]. La prime est donnée : aucun modèle d'évaluation n'est attendu.

**Coût de la commande (1 pt)**

| € | 1 EUR = 1,0800 USD (dollar en hausse) | 1 EUR = 1,1600 USD (dollar en baisse) |
|---|---:|---:|
| Sans couverture | 2 000 000 / 1,08 = 1 851 852 | 2 000 000 / 1,16 = 1 724 138 |
| Achat à terme | 1 779 518 | 1 779 518 |
| Option | exercée : 2 000 000 / 1,12 = 1 785 714 + prime 21 429 = **1 807 143** | abandonnée : 1 724 138 + prime 21 429 = **1 745 567** |

L'option plafonne le coût à 1 807 143 € tout en laissant profiter d'une baisse du dollar. Elle devient plus intéressante que le terme dès que le cours dépasse 2 000 000 / (1 779 518 − 21 429) = 1,1376 au 31/03/2027.

**Recommandation (1 pt).** La commande est **ferme** et son montant est **certain** : l'**achat à terme** est la couverture adaptée. Elle est gratuite, simple, et même favorable ici grâce au report de l'euro. Elle supprime le risque, mais aussi la possibilité de profiter d'une baisse du dollar. L'option ne se justifierait que si la commande pouvait être annulée, ou si la direction anticipait une forte baisse du dollar, au-delà de 1,1376. Les critères du choix sont le coût, la souplesse, la simplicité et le risque résiduel [V guide p. 79].

**Réponses tolérées** : recommandation de l'option si elle est justifiée par une anticipation chiffrée ; couverture partielle (terme pour une partie, option pour le reste).

**Erreurs fréquentes**
- Oublier la prime dans le coût de l'option, ou la retrancher alors qu'ORVANE la paie.
- Exercer l'option dans le scénario 1,1600 : au comptant, l'euro achète plus de dollars qu'au prix d'exercice.
- Tenter de calculer la prime : les modèles de valorisation des options sont hors programme.

---

### 2.3 Swap et cap (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Coûts et taux sans couverture | 0,5 |
| 2.3-02 | Swap : différentiels, coût net 150 000 €, taux 5,00 % | 1,5 |
| 2.3-03 | Cap : versement, prime, coût net, taux 4,75 % et 5,35 % | 1,5 |
| 2.3-04 | Conseil à la direction | 0,5 |

Intérêts du trimestre = 12 000 000 × taux × 90/360. Taux annuel = coût du trimestre / (12 000 000 × 90/360).

| € (90 jours) | Euribor 2,40 % | Euribor 3,40 % |
|---|---:|---:|
| **Sans couverture** : intérêts au taux variable, marge de 2,10 % comprise | 135 000 (4,50 %) | 165 000 (5,50 %) |
| **Swap** : différentiel (2,90 % contre Euribor) | versé : 15 000 | reçu : 15 000 |
| Coût net avec le swap | **150 000 (5,00 %)** | **150 000 (5,00 %)** |
| **Cap** : versement reçu (Euribor − 3 %) | 0 | 12 000 |
| Prime du trimestre (0,25 % × 90/360) | 7 500 | 7 500 |
| Coût net avec le cap | **142 500 (4,75 %)** | **160 500 (5,35 %)** |

Le swap transforme l'emprunt variable en emprunt à **taux fixe de 5,00 %** (2,90 % + 2,10 %), quel que soit l'Euribor. Le cap fixe un **taux maximal de 5,35 %** (3,00 % + 2,10 % + 0,25 %) et laisse profiter d'une baisse, moyennant la prime.

**Conseil (0,5 pt).** Le choix dépend des anticipations de la direction et de son aversion au risque :
- le **swap** est sans prime et donne une visibilité complète sur les frais financiers pendant cinq ans, ce que le fonds appréciera dans le plan d'affaires. En contrepartie, il fait renoncer à toute baisse des taux, et le débouclage avant terme peut être coûteux ;
- le **cap** coûte 0,25 % par an, soit 30 000 € par an, mais conserve le bénéfice d'une baisse ;
- un compromis possible : couvrir une partie du nominal par swap et laisser le reste variable, ou acheter un **tunnel** (cap acheté et floor vendu), dont la prime nette est plus faible.

Si la direction anticipe une stabilité ou une hausse des taux, le swap est la solution la plus prudente pour une ETI qui s'endette sur cinq ans ; si elle anticipe une baisse, le cap ou une couverture partielle se défendent.

**Réponses tolérées** : calcul en mois/12 (3 mois), qui donne ici les mêmes montants ; taux actuariel si la méthode est explicitée ; recommandation du cap justifiée par une anticipation de baisse.

**Erreurs fréquentes**
- Inverser le sens du différentiel de swap : le payeur de fixe reçoit quand l'Euribor dépasse le taux fixe.
- Oublier la marge de 2,10 %, qui reste due dans toutes les solutions.
- Oublier la prime du cap dans le coût net.
- `JUR-T07` — résultats donnés sans tableau.

---

### 2.4 Option climatique (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Indemnités et effets nets dans les trois scénarios | 1,5 |
| 2.4-02 | Nature du risque couvert (volume) | 0,5 |
| 2.4-03 | Limites de la couverture | 1 |

Indemnité = 4 000 € × max(0 ; 2 500 − indice), plafonnée à 800 000 €. Effet de l'hiver sur l'EBITDA = 4 000 € × (indice − 2 600).

| € | 2 600 (normal) | 2 400 | 2 200 |
|---|---:|---:|---:|
| Effet de l'hiver sur l'EBITDA | 0 | − 800 000 | − 1 600 000 |
| Indemnité de l'option | 0 | + 400 000 | + 800 000 (plafond atteint) |
| Prime | − 120 000 | − 120 000 | − 120 000 |
| **Effet net sur le résultat avant impôt** | **− 120 000** | **− 520 000** | **− 920 000** |

**Nature du risque (0,5 pt).** L'option couvre un **risque de volume**, et non de prix : un hiver doux réduit les ventes. Le sous-jacent est un **indice météorologique non livrable** ; le contrat se dénoue en espèces.

**Lecture et limites (1 pt).**
- La couverture laisse à la charge d'ORVANE une **franchise** de 100 degrés-jours entre la normale (2 600) et le prix d'exercice (2 500), soit 400 000 €, plus la prime. Entre 2 500 et 2 300 degrés-jours, la perte nette reste donc limitée à 520 000 €.
- Le **plafond** de 800 000 € est atteint à 2 300 degrés-jours. En dessous, la perte reprend : à 2 200, l'option ne compense que la moitié de la baisse d'EBITDA.
- **Risque de base** : la station est à 30 km, et la sensibilité de 4 000 € par degré-jour est une estimation statistique sur douze ans. La perte réelle peut différer de l'indemnité.
- La prime est perdue si l'hiver est normal ou froid ; un hiver froid augmente toutefois l'EBITDA.
- **Risque de contrepartie** : l'indemnité dépend de la solidité de la banque.

**Erreurs fréquentes**
- Oublier le plafond à 2 200 degrés-jours (indemnité de 1 200 000 €).
- Confondre dérivé climatique et assurance des dommages : l'option indemnise un écart d'indice, sans sinistre ni constat de perte.

---

### 2.5 Discussion : « le risque climatique est réglé » (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Limites de l'affirmation (risques non couverts) | 1 |
| 2.5-02 | Mise en perspective stratégique et recommandation | 1 |

L'affirmation est excessive.
- **L'option transfère un risque financier, elle ne réduit pas l'exposition.** Elle couvre une partie de l'effet d'un hiver doux sur une seule saison. Avec le réchauffement, la « normale » de 2 600, calculée sur le passé, sera de moins en moins atteinte : les vendeurs d'options intégreront cette tendance, et les primes augmenteront. C'est un outil de lissage du résultat, pas une adaptation.
- **D'autres risques climatiques ne sont pas couverts** [F07 § 5] :
  - **risques physiques** : canicule ou inondation sur le site de production, rupture d'approvisionnement des compresseurs ;
  - **risques de transition** : durcissement de la réglementation des fluides frigorigènes, évolution des aides publiques à la rénovation, prix de l'énergie.
- **Le climat crée aussi des opportunités** pour ORVANE : les étés plus chauds augmentent la demande de pompes à chaleur réversibles, qui climatisent. Une offre réversible constitue une **couverture naturelle**, plus durable que l'option.
- **Double matérialité** : il faut analyser l'effet du climat sur ORVANE (matérialité financière), mais aussi l'effet d'ORVANE sur le climat (matérialité d'impact). Ses produits remplacent des chaudières à énergie fossile. C'est un argument fort auprès d'un fonds de la transition énergétique, lui-même tenu à des obligations de transparence sur la durabilité de ses investissements [F08 ; SFDR].

**Recommandation.** Intégrer le risque climatique dans la cartographie des risques et dans le plan d'affaires : diversification vers les pompes à chaleur réversibles, plan d'adaptation du site, sécurisation des approvisionnements. L'option climatique ne doit être qu'un complément de court terme.

**Réponses tolérées** : toute argumentation qui distingue couverture financière et réduction de l'exposition, en s'appuyant sur les données du cas.

**Erreurs fréquentes**
- `JUR-T05` — performance durable traitée à part, sans lien avec les calculs du dossier.
- `JUR-T13` — discussion générale sur le réchauffement, sans référence à ORVANE.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme UE 2, partie 6 ; guide pédagogique, juillet 2026, p. 77-80 | instruments de couverture, critères de choix (coût, simplicité, flexibilité, risque résiduel), exclusion des modèles de valorisation des options | [V] | F07 § 0 |
| Parité des taux d'intérêt | cours à terme | [S] | F07 § 3.3 |
| Corrigé DSCG 2023, dossier 3 | présentation d'un swap en tableau par scénario | [V] | F07 § 2.2 |
| Dérivés climatiques sur degrés-jours | indemnité, risque de base | [S] | F07 § 5 |
