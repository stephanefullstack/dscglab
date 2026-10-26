# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 9 — Dossier 3 (15 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F01 mathématiques financières, F07 risques de taux et de change et trésorerie de groupe, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (trésorerie de groupe, obligations, FRA, contrats à terme, floor, barème, liste noire, hors-programme).

Bien que le corrigé mentionne des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple un gain de centralisation calculé à partir d'un total sans centralisation erroné à la question 3.1).

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Centralisation de la trésorerie du groupe | `6.1.a` Appliquer les mécanismes de centralisation de trésorerie | 4 |
| 3.2 Placement de l'excédent d'été et financement du creux d'hiver | `6.1.b` Discerner les différents types de financement et de placement | 3 |
| 3.3 Portefeuille obligataire de réserve et exposition au risque de taux | `6.2.a` Maîtriser la relation inverse entre la valeur et les taux d'intérêt | 4 |
| 3.4 Protection du taux du placement de l'été | `6.2.c` Maîtriser les contrats à terme et optionnels sur les marchés organisés et de gré à gré (taux) ; `6.2.b` Maîtriser les principaux instruments de couverture du risque de taux | 4 |
| **Total** | | **15** |

Part du calcul : environ 8,5 points (3.1-01 à 3.1-05, 3.3-01 à 3.3-06, 3.4-02 à 3.4-06). Part de l'analyse : environ 6,5 points. La question 3.2, entièrement rédigée, et les items d'analyse des autres questions ne doivent pas être sacrifiés faute de temps : ce dossier est le dernier de l'épreuve (`JUR-T15`).

---

### 3.1 Centralisation de la trésorerie du groupe (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.1-01 | Intérêts de chaque société et de chaque trimestre sans centralisation (taux débiteur ou créditeur selon le signe du solde) | 1 |
| 3.1-02 | Total sans centralisation : produit net de 23 328 € | 0,5 |
| 3.1-03 | Soldes nets trimestriels du groupe et intérêts du compte centralisateur : produit net de 116 461 € | 0,5 |
| 3.1-04 | Résultat avec centralisation, frais compris (98 461 €) et gain de 75 133 € | 0,5 |
| 3.1-05 | Origine du gain : compensation des soldes de signes contraires et meilleures conditions, illustrées par les chiffres du cas (par exemple, au T1, l'effet des seules conditions) | 0,5 |
| 3.1-06 | Prérequis et limites ; appréciation des conditions internes | 0,5 |
| 3.1-07 | Cash pooling notionnel et netting : alternative ou complément | 0,5 |

**Intérêts sans centralisation (1 pt).** Intérêts d'un trimestre = solde moyen × taux × jours / 360, au taux débiteur si le solde est débiteur, au taux créditeur s'il est créditeur. Les intérêts de la holding sont donnés par l'annexe 3.1. Exemples : Plein Air au T1, − 4 600 000 × 4,15 % × 90 / 360 = − 47 725 € ; Plein Air au T3, 9 000 000 × 1,95 % × 92 / 360 = + 44 850 € ; Atlantique Nord au T2, 2 500 000 × 1,45 % × 91 / 360 = + 9 163 €.

| Intérêts 2027 (€) | T1 (90 j) | T2 (91 j) | T3 (92 j) | T4 (92 j) | Total |
|---|---:|---:|---:|---:|---:|
| SOLVÉRAN Holding (donnés) | − 13 950 | − 14 105 | − 14 260 | − 14 260 | − 56 575 |
| SOLVÉRAN Plein Air | − 47 725 | + 7 394 | + 44 850 | + 12 458 | + 16 977 |
| Atlantique Nord | − 12 125 | + 9 163 | + 25 939 | + 5 558 | + 28 535 |
| Atlantique Sud | − 9 700 | + 7 331 | + 22 233 | − 3 718 | + 16 146 |
| Occitanie | − 7 275 | + 4 398 | + 16 675 | + 4 447 | + 18 245 |
| **Groupe** | **− 90 775** | **+ 14 181** | **+ 95 437** | **+ 4 485** | **+ 23 328** |

**Total sans centralisation (0,5 pt).** Le groupe paie 137 118 € d'agios et reçoit 160 446 € de rémunération : **produit net de 23 328 €** seulement, alors que son solde net moyen sur l'année est créditeur d'environ 6,8 M€. La holding, débitrice toute l'année à 4,65 %, perd 56 575 € pendant que les autres sociétés placent leurs excédents à 1,45 % ou 1,95 %.

**Intérêts du compte centralisateur (0,5 pt).** Le compte centralisateur porte la somme des soldes des cinq sociétés, aux conditions de la banque chef de file (3,90 % débiteur ; 2,20 % créditeur).

| Compte centralisateur | T1 | T2 | T3 | T4 | Total |
|---|---:|---:|---:|---:|---:|
| Solde net du groupe (k€) | − 8 200 | + 6 000 | + 25 300 | + 3 700 | |
| Taux appliqué | 3,90 % | 2,20 % | 2,20 % | 2,20 % | |
| Intérêts (€) | − 79 950 | + 33 367 | + 142 242 | + 20 802 | **+ 116 461** |

**Résultat avec centralisation et gain (0,5 pt).** Résultat financier avec centralisation = 116 461 − 18 000 = **98 461 €**. Gain = 98 461 − 23 328 = **75 133 €** par an, soit plus de quatre fois les frais du dispositif.

**Origine du gain (0,5 pt).** Écart entre le compte centralisateur et la somme des comptes séparés, avant frais : T1 + 10 825 € ; T2 + 19 186 € ; T3 + 46 805 € ; T4 + 16 317 € ; total 93 133 €, dont il faut déduire les 18 000 € de frais.
- **Meilleures conditions** obtenues sur des volumes regroupés : au T1, toutes les sociétés sont débitrices, il n'y a rien à compenser ; le gain de 10 825 € vient seulement du taux débiteur de 3,90 % au lieu de 4,15 % à 4,85 %. L'été, l'excédent est rémunéré à 2,20 % au lieu de 1,45 % à 1,95 %.
- **Compensation des soldes de signes contraires** (fusion des soldes) : aux T2, T3 et T4, des sociétés débitrices (la holding toute l'année, Atlantique Sud au T4) paient 4,65 % ou 4,85 % pendant que les autres placent à 1,45 % ou 1,95 % ; avec la centralisation, l'excédent des unes finance directement le découvert des autres et seul le solde net porte intérêt. Au T4, par exemple, 1 500 k€ de soldes débiteurs et 5 200 k€ de soldes créditeurs se réduisent à un excédent net de 3 700 k€ : le groupe passe d'un produit de 4 485 € à 20 802 €.

**Prérequis, limites et conditions internes (0,5 pt).**
- **Prérequis** : une convention de trésorerie signée par chaque société (avances réciproques, conditions de rémunération, durée, sortie) ; l'ouverture des cinq comptes dans la banque chef de file (les deux autres banques du pool perdent des flux, ce qui peut peser sur la relation) ; un système d'information qui suive au jour le jour la position de chaque société envers le compte centralisateur ; une autorisation de découvert du compte centralisateur suffisante pour la pointe d'hiver (20 M€ pour une moyenne de 8,2 M€ au T1 2027 et une pointe de 17 M€ attendue en février 2028, annexe 3.2).
- **Limites** : la société pilote concentre le risque de liquidité du groupe ; les filiales perdent leur autonomie de gestion de trésorerie et leur relation propre avec leur banque ; chaque société doit conserver son intérêt propre (les aspects juridiques et fiscaux des avances intragroupe ne sont pas développés ici) ; la centralisation ne crée pas de trésorerie : elle réduit le coût du découvert d'hiver mais ne le supprime pas (8,2 M€ de solde net au T1).
- **Conditions internes** : chaque société y gagne par rapport à sa banque (débit à 3,90 % au lieu de 4,15 % à 4,85 % ; crédit à 2,45 % au lieu de 1,45 % à 1,95 %), ce qui facilite l'adhésion des dirigeants des filiales. Mais la société pilote rémunère les excédents à 2,45 % alors que le compte centralisateur ne lui rapporte que 2,20 % : elle perd 0,25 point sur chaque excédent et supporte seule les 18 000 € de frais. Avec ces conditions, les intérêts internes des cinq sociétés seraient au total un produit net de 124 379 €, soit un gain de 101 051 € par rapport à leurs conditions bancaires, tandis que le compte centralisateur perdrait 116 461 − 124 379 − 18 000 = 25 918 €. La holding étant à la fois société participante et pilote, il faut la prendre dans son ensemble : compte propre (− 47 450 €) et compte centralisateur (− 25 918 €), soit − 73 368 € contre − 56 575 € sans centralisation (− 16 793 €) ; les quatre autres sociétés gagnent 91 926 €. Le gain du groupe (75 133 €) va donc aux sociétés d'exploitation, au détriment de la holding. Un taux créditeur interne de 2,20 % (aligné sur celui de la banque) et une refacturation des frais au prorata des flux seraient plus cohérents, tout en restant proches des conditions de marché.

**Cash pooling notionnel et netting (0,5 pt).**
- **Cash pooling notionnel** : la banque calcule les intérêts sur la somme fictive des soldes sans virement entre comptes ; chaque société garde son compte et son solde réel. Il éviterait les avances intragroupe et la convention de prêts réciproques, mais suppose des garanties croisées entre sociétés et reste rare ou plus coûteux pour un groupe de cette taille ; dans un groupe franco-français, entièrement en euros et détenu à 100 %, le cash pooling physique, plus simple et mieux maîtrisé, est adapté.
- **Netting** : la compensation périodique des dettes et créances intragroupe (refacturations de Plein Air, redevances des filiales) remplacerait une vingtaine de virements mensuels par un règlement du solde net de chaque société. Avec un cash pooling physique dans une seule banque et une seule devise, son intérêt est limité (moins de frais de virement, moins de travail administratif) : c'est un **complément** de gestion, pas une alternative. Il serait plus utile si le groupe avait des filiales à l'étranger, dans d'autres devises.

**Réponses tolérées** : intérêts calculés en k€ à une ou deux décimales, ou arrondis en fin de calcul seulement (écart de quelques euros sur les totaux) ; frais déduits trimestriellement (4 500 € par trimestre), même résultat annuel ; gain exprimé en pourcentage des frais financiers actuels ; conditions internes jugées acceptables si le candidat montre qu'elles transfèrent le gain aux filiales et que la holding pilote en supporte le coût ; mention de la théorie de l'agence (Jensen et Meckling, 1976) pour analyser la perte d'autonomie des dirigeants des filiales et le contrôle exercé par la holding.

**Erreurs fréquentes**
- Appliquer le taux débiteur à un solde créditeur (ou l'inverse), ou appliquer les conditions du compte centralisateur à chaque société au lieu de les appliquer au solde net du groupe.
- Calculer en base 365 ou en mois / 12 alors que l'annexe impose Exact/360 et donne le nombre de jours.
- Oublier les 18 000 € de frais dans le résultat avec centralisation.
- `JUR-T07` — présenter seize calculs d'intérêts en ligne, sans tableau par société et par trimestre.
- `JUR-T13` — réciter les avantages du cash pooling sans les relier aux chiffres du cas (découvert de 8,2 M€ au T1, holding débitrice toute l'année, excédents d'été rémunérés à 1,45 %).

---

### 3.2 Placement de l'excédent d'été et financement du creux d'hiver (3 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.2-01 | Diagnostic des horizons : excédent de 3 mois, excédent résiduel jusqu'à la fin de l'année, réserve à un an ; besoin de 4 mois avec une pointe | 0,5 |
| 3.2-02 | Placement de l'excédent : supports retenus et écartés, justifiés par l'horizon, le rendement, le risque et la liquidité | 1 |
| 3.2-03 | Financement du creux : supports retenus et écartés, justifiés | 1 |
| 3.2-04 | Plan d'ensemble cohérent et appliqué au cas | 0,5 |

**Diagnostic des horizons (0,5 pt).** Un placement de trésorerie doit d'abord être **disponible** à la date du besoin : la liquidité et la sécurité du capital priment sur le rendement. Chez SOLVÉRAN :
- 20 M€ sont disponibles **pendant 90 jours** (1er juillet - 29 septembre) : horizon court et connu ;
- environ 6 M€ restent disponibles jusqu'à la mi-novembre, puis 1 à 2 M€ jusqu'au 31 décembre : horizon de quelques semaines, plus incertain (fin de saison, arrière-saison) ;
- la réserve obligataire de 5 M€ servira en 2028 à une acquisition : horizon d'un an environ ;
- l'hiver, le besoin dure **quatre mois** (janvier-avril 2028, après le paiement des échéances annuelles de la dette bancaire début janvier), avec une moyenne de 12 M€ et une pointe de 17 M€ à la fin février : il est saisonnier, récurrent et variable d'un mois à l'autre.

**Placement de l'excédent (1 pt).**
- **20 M€ sur trois mois** : un **compte à terme à 3 mois** (2,40 % aujourd'hui) garantit le capital et un taux fixé à l'ouverture, avec une échéance qui coïncide avec le besoin ; des **NEU CP** à 3 mois rapportent davantage (2,75 %), mais exposent au risque de crédit de l'émetteur et doivent être conservés jusqu'à l'échéance : ils conviennent à une partie de l'excédent, répartie entre plusieurs émetteurs bien notés (au sens de Markowitz, 1952, la diversification réduit le risque propre à chaque émetteur), puisque l'horizon de trois mois est certain. Sur 20 M€ et 90 jours, l'écart entre 2,40 % et 2,75 % représente environ 17 500 € (120 000 € contre 137 500 €).
- **6 M€ jusqu'à la mi-novembre, le reliquat de fin d'année et le volant de sécurité** : un **OPCVM monétaire** (environ 2,35 %, rachat en un jour) ou des comptes à terme à 1 mois (2,30 %) renouvelés : le rendement est un peu plus faible, mais la liquidité est quotidienne, ce qui convient à un horizon incertain.
- **Supports écartés** : les **obligations** à 4 à 7 ans rapportent davantage (3,20 % à 4,00 %), mais leur revente au bout de trois mois expose à une perte en capital si les taux montent (− 3,71 % à − 6,00 % pour + 1 point, question 3.3), qui effacerait plusieurs années d'écart de rendement ; les **OPCVM actions** (rendement espéré d'environ 7 %, mais perte possible de 20 % ou plus sur un an) sont inadaptés à une trésorerie dont le groupe aura besoin dans quelques mois : le couple rendement-risque ne se juge qu'à horizon égal.
- Quel que soit le support, son taux sera fixé au 1er juillet : la protection de ce taux est étudiée à la question 3.4.

**Financement du creux (1 pt).**
- **Ligne de crédit renouvelable confirmée** (15 M€ jusqu'en 2030, 3,75 % pour un tirage à 3 mois, plus 0,35 % l'an sur la partie non tirée) : c'est le support adapté à un besoin saisonnier variable, puisque le groupe ne tire que ce dont il a besoin, quand il en a besoin, et que la banque ne peut pas retirer la ligne tant que la clause DFN / EBITDA ≤ 3,5 est respectée. Elle couvre le besoin moyen de 12 M€ et l'essentiel de la pointe.
- **Découvert** (3,90 % sur le compte centralisateur, autorisation de 20 M€) : il absorbe la pointe de fin février au-delà de 15 M€ (environ 2 M€ pendant quelques semaines) ; c'est le financement le plus souple mais le plus cher, et l'autorisation est révocable : il ne doit pas financer le besoin de fond.
- **Crédit de campagne** (12 M€, 3,65 %) : son taux est le plus faible, mais le groupe paie des intérêts sur 12 M€ pendant six mois, y compris en mai et en juin où le besoin est nul, et en janvier où il est encore inférieur à la pointe ; l'excédent ainsi emprunté serait replacé à un taux inférieur (environ 2,35 %). Il peut se justifier si la ligne de crédit renouvelable risque d'être indisponible (clause bancaire tendue), comme financement de secours ou en complément pour un montant plus faible.
- **Supports écartés** : l'émission de NEU CP par SOLVÉRAN (notation ou garantie bancaire, frais fixes) et la mobilisation de créances (clients particuliers qui paient d'avance) sont sans objet ; vendre la réserve obligataire pour financer l'hiver exposerait à une moins-value si les taux ont monté et la priverait de son objet (acquisition de 2028).

**Plan d'ensemble (0,5 pt).** Une réponse possible : l'été, compte à terme à 3 mois pour l'essentiel des 20 M€ et NEU CP diversifiés pour une partie, OPCVM monétaire pour l'excédent résiduel et le volant de sécurité ; l'hiver, tirages de la ligne de crédit renouvelable ajustés mois par mois, le découvert couvrant la seule pointe. La centralisation (question 3.1) rend ce plan possible : la holding pilote place et emprunte pour le groupe sur la base du solde net, au lieu de cinq décisions séparées. Le groupe doit toutefois surveiller la clause bancaire : une saison dégradée qui ferait dépasser 3,5 fois l'EBITDA priverait le groupe de sa ligne au moment où il en a le plus besoin.

**Réponses tolérées** : placement de tout l'excédent de 20 M€ en compte à terme (sécurité maximale) ou d'une part plus élevée en NEU CP, si le risque de crédit et la diversification sont discutés ; financement de l'hiver par une combinaison de crédit de campagne pour une partie et de ligne renouvelable, si le coût du montant inutilisé est identifié ; tableau de synthèse par support (horizon, rendement, risque, liquidité) à la place d'une rédaction ; ordres de grandeur chiffrés des coûts, s'ils sont cohérents avec les annexes.

**Erreurs fréquentes**
- Choisir le support au seul taux affiché (obligations à 4 %, actions) sans tenir compte de l'horizon de trois mois ni du risque de perte en capital.
- Employer les anciennes appellations des NEU CP comme si elles étaient encore en vigueur.
- `JUR-T12` — confondre le découvert (révocable, sur le montant utilisé) et la ligne de crédit confirmée (engagement de la banque, commission de non-utilisation).
- `JUR-T13` — liste de supports sans lien avec le profil de trésorerie du groupe (20 M€ pendant 90 jours, besoin de 12 M€ en moyenne et de 17 M€ en pointe).

---

### 3.3 Portefeuille obligataire de réserve et exposition au risque de taux (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.3-01 | Prix d'une obligation A : 99,26 € | 0,5 |
| 3.3-02 | Duration de l'obligation A : 3,828 ans | 0,5 |
| 3.3-03 | Sensibilité de l'obligation A : − 3,709 | 0,5 |
| 3.3-04 | Hausse de 100 points de base : variation exacte − 3,60 € (− 3,62 %), estimée − 3,68 € (− 3,71 %) ; explication de l'écart | 0,5 |
| 3.3-05 | Perte estimée du portefeuille : − 218,9 k€ (− 4,40 %) | 0,5 |
| 3.3-06 | Duration du portefeuille : 4,556 ans ; commentaire au regard de l'horizon de la réserve | 0,5 |
| 3.3-07 | Exposition du groupe : positions, sens du risque, compensations et conclusion | 1 |

**Prix et duration de l'obligation A (1 pt).** Flux d'un titre : coupons de 3 € dans 1, 2 et 3 ans ; 103 € dans 4 ans ; taux du marché 3,20 %.

| Année t | Flux (€) | Valeur actuelle à 3,20 % | t × valeur actuelle |
|---:|---:|---:|---:|
| 1 | 3 | 2,9070 | 2,9070 |
| 2 | 3 | 2,8168 | 5,6337 |
| 3 | 3 | 2,7295 | 8,1885 |
| 4 | 103 | 90,8068 | 363,2273 |
| **Total** | | **99,2601** | **379,9565** |

Prix = **99,26 €** (sous le pair, car le coupon de 3,00 % est inférieur au taux du marché de 3,20 %). Duration = 379,9565 / 99,2601 = **3,828 ans** : inférieure à la maturité de 4 ans, puisqu'une partie de la valeur est perçue avant l'échéance.

**Sensibilité (0,5 pt).** S = − 3,828 / 1,032 = **− 3,709** : pour une hausse d'un point des taux, le prix baisse d'environ 3,71 %.

**Effet d'une hausse de 100 points de base (0,5 pt).**
- **Exactement** : au taux de 4,20 %, prix = 3 / 1,042 + 3 / 1,042² + 3 / 1,042³ + 103 / 1,042⁴ = 2,8791 + 2,7630 + 2,6517 + 87,3708 = **95,66 €**, soit une baisse de **3,60 €** (− 3,62 %).
- **Par la sensibilité** : − 3,709 % × 99,26 = **− 3,68 €** (− 3,71 %).
- **Écart** : la sensibilité mesure la pente de la courbe prix-taux au point de départ ; la relation étant convexe (la baisse du prix ralentit à mesure que le taux monte), l'approximation linéaire surestime légèrement la baisse (0,08 € par titre). Elle est d'autant plus fiable que la variation de taux est faible.

**Perte estimée du portefeuille (0,5 pt).**

| Ligne | Valeur (k€) | Sensibilité | Variation estimée (k€) |
|---|---:|---:|---:|
| A : 35 000 × 99,26 € | 3 474,1 | − 3,709 | − 128,9 |
| B : 15 000 × 100,00 € | 1 500,0 | − 6,002 | − 90,0 |
| **Portefeuille** | **4 974,1** | | **− 218,9 (− 4,40 %)** |

La ligne B, plus longue, représente 30 % de la valeur mais 41 % de la perte. (Pour information, la variation exacte serait de − 125,8 k€ pour A et − 86,8 k€ pour B, soit − 212,6 k€ ou − 4,27 %.)

**Duration du portefeuille (0,5 pt).** (3 474,1 × 3,828 + 1 500,0 × 6,242) / 4 974,1 = 22 661,9 / 4 974,1 = **4,556 ans**. La réserve doit être utilisée en 2028, dans environ un an, alors que la duration du portefeuille est de 4,6 ans : les titres devront être vendus bien avant leur échéance, au prix du marché du moment. Le portefeuille n'est pas adossé à son horizon : une hausse de 100 points de base ferait perdre environ 219 k€, soit plus que les coupons d'une année (environ 165 k€). Pour un horizon d'un an, il faudrait une duration proche d'un an (titres courts, comptes à terme, NEU CP) ; la ligne B ajoute en outre un risque de crédit.

**Exposition du groupe au risque de taux (1 pt).**

| Position | Montant | Nature | Effet d'une hausse des taux | Variation redoutée |
|---|---|---|---|---|
| Portefeuille obligataire de réserve | 5,0 M€ de nominal | actif à taux fixe | perte de valeur (risque de prix) | **hausse** |
| Placement de l'été | 20 M€ pendant 90 jours | actif à taux variable (taux fixé au 1er juillet) | produits plus élevés | **baisse** |
| Dette d'acquisition | 104 M€ | passif à taux variable, couvert en partie | charges plus élevées | **hausse** |
| Financements de l'hiver | 12 à 17 M€ pendant 4 mois | passif à taux variable | charges plus élevées | **hausse** |

La **relation inverse** entre la valeur et les taux ne concerne que les positions à taux fixe : une hausse des taux réduit la valeur des obligations détenues (risque de prix, latent si les titres étaient conservés jusqu'à l'échéance) ; les positions à taux variable n'ont pas de risque de valeur, mais un risque sur les flux d'intérêts futurs. Le groupe est globalement **emprunteur net à taux variable** : la hausse des taux est son risque principal (sur la dette d'acquisition, un point de hausse coûte 1,04 M€ d'intérêts par an avant l'effet des couvertures en place). Les placements d'été à taux variable compensent un peu cette exposition, pour des montants et des durées bien plus faibles. Le placement de l'été, lui, craint la **baisse** : c'est une position particulière, couverte à la question 3.4, qui ne doit pas faire oublier le risque global.

**Réponses tolérées** : sensibilité exprimée en valeur absolue (3,709) si le sens de la variation du prix est correctement indiqué ; variation estimée du portefeuille calculée à partir de sa duration et d'un taux moyen explicité, si l'approximation est signalée ; variation exacte de la ligne B calculée en plus ; écarts d'arrondi de 0,01 € sur le prix ou de 0,001 sur la duration.

**Erreurs fréquentes**
- Confondre duration et maturité, ou oublier que le dernier flux comprend le coupon et le remboursement.
- Appliquer la sensibilité au nominal (100 €) au lieu du prix (99,26 €).
- Pondérer la duration du portefeuille par les nominaux sans le dire (résultat très proche ici, mais méthode inexacte en général).
- Conclure que le groupe craint seulement la baisse des taux, parce qu'il place l'été, en oubliant la dette d'acquisition à taux variable.
- `JUR-T07` — calcul de duration sans tableau des flux actualisés.

---

### 3.4 Protection du taux du placement de l'été (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 3.4-01 | Risque de baisse des taux ; sens de chaque couverture : vente du FRA, achat des contrats, achat du floor | 0,5 |
| 3.4-02 | FRA : différentiel reçu de 34 834,54 € ou versé de 24 807,74 € ; produit total de 130 000 € et taux de 2,60 % dans les deux scénarios | 0,5 |
| 3.4-03 | Contrats à terme : résultat de + 35 000 € ou − 25 000 € ; produit total de 130 000 € et taux de 2,60 % | 0,5 |
| 3.4-04 | 20 contrats ; dépôt de garantie de 10 000 € ; appel de marge de 3 500 € ; mécanisme des appels de marge | 0,5 |
| 3.4-05 | Floor : prime de 15 000 € ; valeur intrinsèque de 5 000 € ; valeur temps de 10 000 € | 0,5 |
| 3.4-06 | Floor : produit de 122 500 € (2,45 %) ou 140 000 € (2,80 %) | 0,5 |
| 3.4-07 | Comparaison (ferme / optionnel, gré à gré / marché organisé, point mort) et recommandation | 1 |

**Risque et sens des couvertures (0,5 pt).** SOLVÉRAN placera 20 M€ dans trois mois à un taux encore inconnu : elle craint la **baisse** de l'Euribor d'ici au 1er juillet, que plusieurs économistes anticipent. Elle se couvre en **vendant** le FRA (elle reçoit le différentiel si le taux constaté est inférieur au taux garanti), en **achetant** des contrats à terme (leur cours, 100 − taux, monte quand le taux baisse) et en **achetant** un floor (il verse la différence si le taux passe sous 2,75 %). Sans couverture, le placement rapporterait 20 000 000 × 1,90 % × 90 / 360 = **95 000 €** (1,90 %) dans le scénario de baisse et 155 000 € (3,10 %) dans le scénario de hausse.

**FRA (0,5 pt).** Différentiel (formule de l'annexe, vu de l'acheteur) :
- taux constaté de 1,90 % : 20 000 000 × (1,90 % − 2,60 %) × 90 / 360 / (1 + 1,90 % × 90 / 360) = − 35 000 / 1,00475 = **− 34 834,54 €** : la banque, acheteuse, **verse** 34 834,54 € à SOLVÉRAN le 1er juillet ; placés à 1,90 % pendant 90 jours, ils deviennent 35 000 € ;
- taux constaté de 3,10 % : 20 000 000 × 0,50 % × 90 / 360 / 1,00775 = **24 807,74 €**, que SOLVÉRAN **verse** à la banque ; empruntés à 3,10 %, ils coûtent 25 000 € au 29 septembre.

| FRA vendu à 2,60 % | Euribor 1,90 % | Euribor 3,10 % |
|---|---:|---:|
| Intérêts du placement | 95 000 | 155 000 |
| Différentiel à la fin de la période | + 35 000 | − 25 000 |
| **Produit total** | **130 000** | **130 000** |
| Taux obtenu | 2,60 % | 2,60 % |

**Contrats à terme : résultat (0,5 pt).** SOLVÉRAN achète des contrats à 97,40 (taux implicite de 2,60 %). Au 1er juillet, le cours vaut 100 − Euribor constaté.

| Achat de 20 contrats à 97,40 | Euribor 1,90 % | Euribor 3,10 % |
|---|---:|---:|
| Cours au 1er juillet | 98,10 | 96,90 |
| Variation en points de base | + 70 | − 50 |
| Résultat : 20 × variation × 25 € | + 35 000 | − 25 000 |
| Intérêts du placement | 95 000 | 155 000 |
| **Produit total** | **130 000** | **130 000** |
| Taux obtenu | 2,60 % | 2,60 % |

**Contrats à terme : nombre, dépôt et appels de marge (0,5 pt).** Nombre de contrats = 20 000 000 / 1 000 000 × (3 mois / 3 mois) = **20**. Dépôt de garantie = 20 × 500 = **10 000 €**, versé le 1er avril et restitué au dénouement. À l'issue de la première séance, le cours de compensation est de 97,33 : perte de 7 points de base, soit 20 × 7 × 25 = **3 500 €**, que SOLVÉRAN doit verser le lendemain (appel de marge). Mécanisme : la chambre de compensation, contrepartie de chaque acheteur et de chaque vendeur, réévalue chaque jour les positions au cours de compensation ; les pertes sont appelées et les gains crédités chaque jour, de sorte que la somme des appels de marge jusqu'au dénouement est égale au résultat final (+ 35 000 € ou − 25 000 €). Le risque de contrepartie disparaît, mais le groupe doit disposer de trésorerie pour faire face aux appels en cas de mouvement défavorable des taux, au printemps, alors que sa trésorerie est encore tendue.

**Floor : prime, valeur intrinsèque et valeur temps (0,5 pt).** Prime = 20 000 000 × 0,30 % × 90 / 360 = **15 000 €**. Valeur intrinsèque = 20 000 000 × (2,75 % − 2,65 %) × 90 / 360 = **5 000 €** : le floor est dans la monnaie au taux du jour. Valeur temps = 15 000 − 5 000 = **10 000 €** : elle rémunère la possibilité que l'Euribor baisse encore d'ici au 1er juillet ; elle diminue à mesure que l'échéance approche et s'annule à l'échéance. La prime est donnée par la banque : elle n'a pas à être calculée.

**Floor : résultat (0,5 pt).**

| Achat du floor 2,75 % | Euribor 1,90 % | Euribor 3,10 % |
|---|---:|---:|
| Intérêts du placement | 95 000 | 155 000 |
| Versement du floor : 20 000 000 × (2,75 % − taux) × 90 / 360 | + 42 500 | 0 |
| Prime | − 15 000 | − 15 000 |
| **Produit net** | **122 500** | **140 000** |
| Taux obtenu | 2,45 % | 2,80 % |

**Comparaison et recommandation (1 pt).**

| Euribor au 1er juillet | Sans couverture | FRA | Contrats à terme | Floor |
|---|---:|---:|---:|---:|
| 1,90 % | 1,90 % | 2,60 % | 2,60 % | 2,45 % |
| 3,10 % | 3,10 % | 2,60 % | 2,60 % | 2,80 % |

- **Instruments fermes** (FRA, contrats à terme) : ils fixent le rendement à 2,60 % quel que soit le taux ; sans coût initial, ils font renoncer au gain d'une hausse des taux (25 000 € dans le second scénario).
- **Instrument optionnel** (floor) : il garantit un rendement minimal de 2,75 % − 0,30 % = 2,45 % et laisse profiter d'une hausse, contre une prime de 15 000 € perdue dans tous les cas. Il est préférable au FRA si le taux constaté le 1er juillet dépasse **2,90 %** (taux garanti de 2,60 % augmenté de la prime de 0,30 % l'an), moins bon en dessous.
- **Gré à gré ou marché organisé** : le FRA et le floor sont négociés sur mesure avec la banque (montant, dates exactement alignés sur le placement), sans versement intermédiaire, mais avec un risque de contrepartie sur la banque, faible ici, et une sortie anticipée à négocier. Les contrats à terme sont standardisés (montant de 1 M€, échéances fixes : la coïncidence avec le 1er juillet est une hypothèse, et en pratique un écart de dates crée un risque de base), liquides, sans risque de contrepartie grâce à la chambre de compensation, mais ils immobilisent un dépôt de garantie et exigent de suivre et financer les appels de marge.
- **Recommandation** : compte tenu des anticipations de baisse des taux, d'un trésorier qui cherche d'abord la sécurité du produit et d'une trésorerie encore tendue au printemps, le **FRA** est la solution la plus simple : il garantit 2,60 %, sur mesure, sans prime ni appel de marge. Le floor se justifie si M. PELLEGRIN ne veut pas renoncer à une hausse possible des taux et accepte un rendement minimal plus faible ; les contrats à terme apportent le même résultat que le FRA dans ce cas d'école, avec plus de contraintes pour une ETI.

**Réponses tolérées** : toute recommandation cohérente avec l'analyse (floor si la direction anticipe une remontée des taux ; combinaison d'un FRA sur une partie du montant et d'un floor sur l'autre) ; différentiel du FRA présenté non actualisé (35 000 € et 25 000 €) si le candidat indique qu'il le compare à sa valeur à la fin de la période ; résultat des contrats calculé en une fois (20 × 0,70 % × 1 000 000 × 3 / 12) ; valeur intrinsèque de 7 500 € et valeur temps de 7 500 € si le candidat la mesure, en le disant, par rapport au taux implicite des contrats (2,60 %), alors que l'annexe retient l'Euribor du jour : item 3.4-05 accordé pour moitié.

**Erreurs fréquentes**
- Acheter le FRA ou vendre les contrats, comme un emprunteur : la position de SOLVÉRAN est celle d'un prêteur, qui craint la baisse.
- Croire que le FRA porte sur le prêt lui-même : seul le différentiel est réglé, le placement est fait séparément au taux du marché.
- Confondre le cours du contrat et le taux (le cours monte quand le taux baisse), ou multiplier les points de base par le nominal au lieu de la valeur du point (25 € par contrat).
- Chercher à calculer la prime du floor par un modèle de valorisation d'option : elle est donnée, seule sa décomposition est demandée.
- `JUR-T07` — résultats des trois couvertures sans tableau comparatif par scénario.
- `JUR-T13` — recommandation générale sans lien avec les anticipations, la trésorerie de printemps et la taille du groupe.

---

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Programme DSCG UE 2 (arrêté du 4 août 2025), partie 6.1 | centralisations de trésorerie, mécanismes financiers et bancaires ; opérations intragroupe (netting, cash pooling) ; supports de financement et de placement (actions, obligations, OPCVM) | [V] | F07 § 0 ; `perimetre_ue2.yaml` (6.1) |
| Programme DSCG UE 2, partie 6.2 | relation inverse valeur-taux, duration, sensibilité ; FRA, cap, floor ; futures et options sur taux ; exclusion des modèles de valorisation des options | [V] | F07 § 0 et 2 ; `perimetre_ue2.yaml` (6.2) |
| Guide pédagogique DSCG, juillet 2026, p. 77-78 | centralisation : intérêt, schémas (notionnel, physique, netting), prérequis, sans traitement juridique ni fiscal, conditions bancaires fournies ; choix d'un placement ou d'un financement selon l'horizon, le rendement-risque et la liquidité ; futures de taux (cotation, nombre de contrats, appels de marge en principe) ; valeur intrinsèque et valeur temps de l'option, prime donnée | [V] | F07 § 0 ; `perimetre_ue2.yaml` |
| Cash pooling physique et notionnel, netting, conventions de trésorerie | mécanismes, avantages, limites | [S] | F07 § 4.1 et 3.2 |
| Supports de placement et de financement à court terme ; NEU CP (ex-billets de trésorerie et ex-certificats de dépôt) | horizon, liquidité, risque ; appellations à jour | [S] | F07 § 4.2 ; F99 § 2 |
| Prix, duration de Macaulay, sensibilité, approximation linéaire | formules usuelles | [S] | F07 § 2.1 ; F01 |
| FRA (différentiel actualisé), contrats à terme Euribor 3 mois (cotation 100 − taux, 25 € par point de base), floor (versement, prime, valeur intrinsèque et valeur temps) | mécanismes et calculs | [S] | F07 § 2.2 et 2.3 |
| Euribor 3 mois 2,65 % et €STR 2,45 % | hypothèses plausibles fin 2026, posées par l'énoncé | [V] séries BCE (valeurs arrondies) | F11 § 1 |
| Markowitz (1952) | diversification des émetteurs de NEU CP | [V programme 5.3] | F10 § 2 |
| Jensen et Meckling (1976) | théorie de l'agence (réponse tolérée, autonomie des filiales) | [V programme 2.1] | F10 § 3 |
