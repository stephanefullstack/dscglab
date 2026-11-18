# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 2 – Finance — Exercice d'entraînement n° 50 — Dossier 2 (17 points)

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

Textes intégrés (fiches datées) : F02 coût du capital, F03 évaluation, F08 gouvernance, finance durable et ESG, F10 auteurs et théories, F11 données de marché et F99 liste noire (à jour au 23/10/2026). Données structurées : `corrige.yaml`, vérifié par `outils/dscgcheck` (équilibre du bilan, bêtas désendettés et réendetté, MEDAF avec prime, CMPC, flux actualisés, valeur terminale, VGE, VCP et valeur par action, ANCC et impôt latent, taux de rentabilité interne du fonds sortant, valeur d'une action sur cinq ans et prix de revente de Gordon-Shapiro, rentabilité, variance, écart-type, bêta, Sharpe, Treynor et décomposition du risque du portefeuille, barème, liste noire, hors-programme ; participation et décote, fourchette, multiple et prix nécessaire au fonds vérifiés par script).

Bien que le corrigé mentionne des textes et des auteurs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte sur la pertinence et la cohérence du raisonnement, la justesse des calculs et la qualité de la rédaction. Toute hypothèse explicite et cohérente avec l'énoncé est acceptée. Une erreur n'est sanctionnée qu'une fois : les calculs qui en découlent sont notés en cohérence avec les résultats antérieurs du candidat (par exemple une VCP calculée avec un CMPC erroné à la question 2.1).

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Bêtas, coût des fonds propres, CMPC et limites du MEDAF | `3.1.a` Maîtriser les méthodes d'évaluation par les flux financiers ; `5.2.c` Maîtriser les principaux modèles d'évaluation du risque financier utilisés en finance | 2 |
| 2.2 Flux actualisés, valeur terminale, VGE, VCP et valeur de la participation | `3.1.a` ; `3.1.d` Distinguer la valeur globale de l'entreprise (VGE) de la valeur des capitaux propres (VCP) | 2,5 |
| 2.3 ANCC, écart avec la valeur par les flux, valeur proposée | `3.3.a` Déterminer la valeur de l'entreprise à partir de la valeur économique de son patrimoine | 3,5 |
| 2.4 Rentabilité réalisée par VALDIGNE Capital et rentabilité exigée | `5.2.a` Identifier la relation entre incertitude et rentabilité exigée par le marché ; `5.2.b` Calculer la rentabilité espérée ou la valeur théorique sur une période d'un titre financier | 2 |
| 2.5 Valeur d'une action pour le fonds de pension et prix maximal | `5.2.b` | 1,5 |
| 2.6 Portefeuille du candidat avant et après l'entrée, risques et diversification | `5.3.a` Maîtriser la différence et le lien entre le risque spécifique et le risque systématique ; `5.3.b` Maîtriser les principes de diversification du portefeuille au sens de Markowitz (1952) ; `5.3.c` Mesurer la rentabilité et le risque du portefeuille de titres | 4 |
| 2.7 Informations de durabilité et politique d'exclusion du candidat | `2.1.b` Interpréter le reporting RSE et de durabilité | 1,5 |
| **Total** | | **17** |

Part du calcul : environ 11 points (2.1-01 à 2.1-03, 2.2-01 à 2.2-04, 2.3-01 à 2.3-03, 2.4-01, la moitié de 2.4-02, 2.5-01 à 2.5-03, 2.6-01 à 2.6-05). Part de l'analyse : environ 6 points. Les montants du bilan au 31 décembre 2026 et des dividendes sont ceux du dossier 1 ; aucun résultat de ce dossier n'y est utilisé.

---

### 2.1 Bêtas, coût des fonds propres, CMPC et limites du MEDAF (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.1-01 | Bêtas désendettés : 0,92 / 1,15 = **0,8000** ; 0,91 / 1,30 = **0,7000** ; 1,44 / 1,60 = **0,9000** ; moyenne **0,8000** | 0,5 |
| 2.1-02 | Bêta réendetté 0,80 × (1 + 0,75 × 0,50) = **1,1000** ; MEDAF 4,00 % + 1,10 × 5,00 % = **9,50 %** ; coût des fonds propres avec la prime **11,25 %** | 0,5 |
| 2.1-03 | Coût de la dette après impôt **3,75 %** ; pondérations deux tiers et un tiers ; CMPC = **8,75 %** | 0,5 |
| 2.1-04 | Pertinence et limites du MEDAF pour une société non cotée, reliées au cas | 0,5 |

**Bêtas désendettés (0,5 pt).** Bêta désendetté = bêta des fonds propres / [1 + (1 − 25 %) × D / CP] (annexe 2.1).

| Société | Bêta des fonds propres | D / CP | 1 + 0,75 × D / CP | Bêta désendetté |
|---|---:|---:|---:|---:|
| HALVERN Spirits | 0,92 | 20 % | 1,15 | **0,8000** |
| DOUROVAL Vinhos e Aguardentes | 0,91 | 40 % | 1,30 | **0,7000** |
| CASTELBRAY Distillers | 1,44 | 80 % | 1,60 | **0,9000** |
| **Moyenne** | | | | **0,8000** |

Les bêtas des fonds propres des trois sociétés diffèrent beaucoup (0,91 à 1,44), mais une grande partie de l'écart tient à leur endettement : désendettés, ils ne s'écartent plus que de 0,70 à 0,90. Le bêta de CASTELBRAY reflète surtout sa dette de 80 % de ses capitaux propres.

**Bêta réendetté et coût des fonds propres (0,5 pt).**
- Bêta des fonds propres d'AUBRESSAC à la structure cible : 0,80 × (1 + 0,75 × 0,50) = 0,80 × 1,375 = **1,1000**.
- MEDAF : 4,00 % + 1,10 × 5,00 % = **9,50 %**.
- Avec la prime de taille et d'illiquidité : 9,50 % + 1,75 % = **11,25 %**.

**CMPC (0,5 pt).** D / CP = 50 % : CP / (CP + D) = 1 / 1,5, soit deux tiers ; D / (CP + D) = 0,5 / 1,5, soit un tiers.
- Coût de la dette après impôt : 5,00 % × (1 − 25 %) = **3,75 %**.
- CMPC = 11,25 % × 2/3 + 3,75 % × 1/3 = 7,50 % + 1,25 % = **8,75 %**.

**Pertinence et limites du MEDAF (0,5 pt).**
- **Pertinence.** Le MEDAF (Sharpe, 1964) ne rémunère que le risque systématique, mesuré par le bêta, pour un investisseur diversifié. Il donne une base explicite, la même pour toutes les parties, et le bêta des comparables cotés remplace celui, inobservable, d'AUBRESSAC. C'est la démarche attendue pour une société non cotée (`JUR-E02`).
- **Hypothèse du bêta d'actif commun.** La méthode suppose que les trois sociétés et AUBRESSAC ont le même risque d'exploitation. Or les comparables diffèrent par le produit (whisky, vins mutés), par la taille, par la diversification de leurs marques et de leurs marchés, et par leurs acquisitions (CASTELBRAY). AUBRESSAC réalise 73 % de ses ventes aux États-Unis et en Asie, avec un seul produit et une seule appellation.
- **Investisseurs non diversifiés.** Les associés d'AUBRESSAC ne sont pas diversifiés : dix-sept membres d'une famille, et un fonds dans lequel la participation pèse environ 12 % des montants investis. Ils supportent aussi le risque spécifique, que le MEDAF ne rémunère pas.
- **Prime ajoutée.** Le MEDAF n'a qu'un facteur. La prime de taille et d'illiquidité de 1,75 % est ajoutée sans être mesurée ; Fama et French (1993) montrent qu'un facteur de taille explique une partie des rentabilités que le bêta n'explique pas. Le résultat dépend fortement de cette prime : 0,5 point de prime déplace le CMPC d'environ 0,33 point.
- **Autres limites.** Le bêta des comparables est historique et instable. La structure cible de 50 % n'est pas celle d'aujourd'hui (DFN de 133,65 M€ pour des capitaux propres de 216,75 M€ au bilan). La prime de marché est une estimation.

**Réponses tolérées** : pondérations écrites 0,6667 et 0,3333, ou CMPC calculé à 8,75 % par arrondi ; bêta de l'actif obtenu par la médiane (0,80, identique) ; mention de l'alpha de Jensen ou du modèle de Fama et French comme prolongement, sans calcul.

**Erreurs fréquentes**
- Faire la moyenne des bêtas des fonds propres (1,09) sans les désendetter, ou réendetter avec la structure de l'une des sociétés.
- Utiliser D / (CP + D) au lieu de D / CP dans la formule de Hamada.
- Oublier l'impôt sur le coût de la dette, ou ajouter la prime de taille au CMPC plutôt qu'au coût des fonds propres.
- `JUR-E02` — démarche par comparables mal conduite ; `JUR-T14` — limites du MEDAF ignorées.

---

### 2.2 Flux actualisés, valeur terminale, VGE, VCP et valeur de la participation (2,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.2-01 | Flux actualisés à 8,75 % : 2,02 ; 8,46 ; 11,66 ; 14,30 ; 15,78, somme **52,22** | 0,5 |
| 2.2-02 | Valeur terminale = 24,00 × 1,025 / 0,0625 = **393,60** ; valeur actuelle **258,77** | 0,5 |
| 2.2-03 | VGE **310,99** ; DFN = 42,00 + 88,00 + 8,80 − 5,15 = **133,65** ; VCP **177,34** ; valeur d'une action **88,67 €** | 0,75 |
| 2.2-04 | Participation de 30 % : **53,20 M€** ; après décote de 10 % : **47,88 M€** (79,80 € par action) | 0,25 |
| 2.2-05 | Poids de la valeur terminale **83,21 %** et ce qu'il signifie ; taux = CMPC parce que les flux reviennent à tous les apporteurs de capitaux | 0,5 |

**Actualisation des flux (0,5 pt)** (M€).

| | 2027 | 2028 | 2029 | 2030 | 2031 | Total |
|---|---:|---:|---:|---:|---:|---:|
| Flux de trésorerie disponible | 2,20 | 10,00 | 15,00 | 20,00 | 24,00 | 71,20 |
| Coefficient 1,0875^−n | 0,919540 | 0,845554 | 0,777521 | 0,714962 | 0,657436 | |
| Flux actualisé | 2,02 | 8,46 | 11,66 | 14,30 | 15,78 | **52,22** |

**Valeur terminale (0,5 pt).** Valeur à la fin de 2031 (Gordon-Shapiro appliqué au flux de 2032) : 24,00 × 1,025 / (0,0875 − 0,025) = 24,60 / 0,0625 = **393,60 M€** ; valeur actuelle = 393,60 × 0,657436 = **258,77 M€**.

**VGE, VCP et valeur d'une action (0,75 pt).**
- VGE = 52,22 + 258,77 = **310,99 M€**.
- Dette financière nette au 31 décembre 2026 = 42,00 + 88,00 + 8,80 − 5,15 = **133,65 M€**. Les dettes locatives sont comprises dans la dette nette, ce qui suppose que les loyers des chais loués ne soient pas déduits des flux ; la DFN est retranchée en entier.
- VCP = 310,99 − 133,65 = **177,34 M€** ; valeur d'une action = 177,34 / 2 000 000 actions = **88,67 €**.

**Participation de VALDIGNE Capital (0,25 pt).** 30 % × 177,34 = **53,20 M€** ; après décote de minorité de 10 % : 53,20 × 0,90 = **47,88 M€**, soit 79,80 € par action.

**Commentaire (0,5 pt).**
- La valeur terminale représente 258,77 / 310,99 = **83,21 %** de la VGE. L'essentiel de la valeur tient aux flux après 2031. Or les eaux-de-vie achetées de 2024 à 2027 ne seront vendues, pour l'essentiel, qu'après 2031 (annexe 2.2), et le flux de 2031 supporte encore environ 6 M€ de croissance des stocks. L'évaluation dépend donc du flux de 2031, de la croissance de 2,50 % et du CMPC. À ce poids, un écart de 0,5 point sur le CMPC ou sur la croissance déplace la VCP d'environ 20 à 30 M€ : VCP de 207,28 M€ à 8,25 % et de 151,87 M€ à 9,25 % ; de 157,00 M€ et 201,21 M€ pour une croissance de 2 % et de 3 % (calculs non exigés).
- **Taux** : les flux de trésorerie disponibles sont calculés avant rémunération des prêteurs et des actionnaires ; ils s'actualisent donc au **CMPC**, qui rémunère tous les apporteurs de capitaux. Le coût des fonds propres (11,25 %) servirait à actualiser des flux revenant aux seuls actionnaires (dividendes, question 2.5). Le CMPC est calculé à la structure cible, plus stable que la structure actuelle.
- La VCP par les flux (177,34 M€) reste nettement inférieure à la valeur patrimoniale (question 2.3).
- **Décote** : la décote de minorité traduit l'absence de contrôle de l'acquéreur sur le dividende et la gestion. Elle peut faire double emploi avec la prime d'illiquidité déjà incluse dans le CMPC : c'est un point de négociation.

**Réponses tolérées** : flux actualisés non arrondis un à un (somme de 52,22, identique) ; VGE de 310,98 à 311,00 par les arrondis ; participation calculée par action (88,67 × 600 000 = 53,20 M€) ; décote appliquée à la valeur d'une action, même résultat ; sensibilité commentée sans calcul ; commentaire sur le caractère non normatif du flux de 2031 (environ 6 M€ de croissance des stocks), éventuellement avec un flux normatif chiffré à part, valorisé, le calcul principal restant celui de la convention.

**Erreurs fréquentes**
- Actualiser au coût des fonds propres (11,25 %) des flux de trésorerie disponibles.
- Calculer la valeur terminale sans croissance (24,00 / 0,0875 = 274,29) ou l'actualiser sur six ans.
- Oublier les dettes locatives ou les crédits de campagne dans la DFN, ou ajouter la trésorerie à la VCP en plus de l'avoir déduite.
- Appliquer la décote à la VCP de 100 % puis prendre 30 %, sans le dire (même résultat, mais justification attendue).
- `JUR-E01` — flux de trésorerie disponibles mal compris ; `JUR-T04` — actualisation non maîtrisée.

---

### 2.3 ANCC, écart avec la valeur par les flux, valeur proposée (3,5 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.3-01 | Stocks au prix du vrac : 62,00 ; 72,00 ; 126,00 ; 72,00 ; bouteilles et matières sèches 17,00 ; total **349,00** ; plus-values 2,00 ; 14,00 ; 46,00 ; 41,00, total **103,00** | 0,75 |
| 2.3-02 | Vignoble 210 × 0,10 = **21,00** ; plus-value **8,40** ; plus-values brutes **111,40** ; impôt latent **27,85** | 0,5 |
| 2.3-03 | ANCC = 216,75 + 111,40 − 27,85 = **300,30 M€** ; **150,15 €** par action ; participation 90,09, après décote **81,08 M€** | 0,5 |
| 2.3-04 | Explication de l'écart de 122,96 M€ (VCP par les flux = 59 % de l'ANCC) propre à une maison de cognac | 1 |
| 2.3-05 | Valeur ou fourchette proposée pour la participation, justifiée ; réfutation de l'argument de M. ROUVRAY (valeur brute des stocks, dette nette et impôt latent à déduire, marché du vrac étroit) | 0,75 |

**Réévaluation des stocks (0,75 pt).** Valeur = quantité × prix moyen du vrac de 2026 (M€).

| Classe d'âge | Coût | Quantité (hl AP) | Prix (€/hl AP) | Valeur au prix du vrac | Plus-value | Coût par hl AP |
|---|---:|---:|---:|---:|---:|---:|
| Moins de 2 ans | 60,00 | 40 000 | 1 550 | 62,00 | 2,00 | 1 500 € |
| 2 à 4 ans | 58,00 | 32 000 | 2 250 | 72,00 | 14,00 | 1 813 € |
| 4 à 10 ans | 80,00 | 36 000 | 3 500 | 126,00 | 46,00 | 2 222 € |
| 10 ans et plus | 31,00 | 8 000 | 9 000 | 72,00 | 41,00 | 3 875 € |
| Bouteilles, en-cours et matières sèches | 17,00 | — | — | 17,00 | 0,00 | — |
| **Total** | **246,00** | **116 000** | | **349,00** | **103,00** | |

La plus-value croît avec l'âge : presque nulle sur les eaux-de-vie de moins de deux ans, elle atteint 132 % du coût pour celles de dix ans et plus (41,00 / 31,00). Le coût ne retient que les dépenses de vieillissement ; le prix du vrac paie aussi le temps.

**Vignoble et impôt latent (0,5 pt).**
- Vignoble : 210 ha × 100 000 € = **21,00 M€**, pour une valeur nette comptable de 12,60 M€ : plus-value **8,40 M€**.
- Plus-values brutes : 103,00 + 8,40 = **111,40 M€** ; impôt latent : 25 % × 111,40 = **27,85 M€**.

**ANCC (0,5 pt).**
- ANCC = capitaux propres 216,75 + plus-values 111,40 − impôt latent 27,85 = **300,30 M€**, soit 300,30 / 2 000 000 = **150,15 €** par action.
- Participation de 30 % : **90,09 M€** ; après décote de minorité de 10 % : **81,08 M€** (135,14 € par action).

**Pourquoi l'écart est important pour une maison de cognac (1 pt).** La VCP par les flux (177,34 M€) ne représente que 59,05 % de l'ANCC (300,30 M€) : l'écart est de **122,96 M€**.
- **Le temps crée la valeur du stock.** Les eaux-de-vie prennent de la valeur en vieillissant, sans dépense supplémentaire importante. Une maison de cognac porte un stock de 116 000 hl AP, qui représente plusieurs années de ventes. Le prix du vrac mesure ce que vaut ce stock aujourd'hui, alors que les flux ne l'encaissent qu'à la vente des cognacs, souvent au-delà de 2031.
- **Les flux sont pénalisés par la constitution du stock.** Les achats d'eaux-de-vie et la croissance des stocks réduisent les flux de 2027 à 2031 (2,20 M€ en 2027 ; encore environ 6 M€ de croissance des stocks en 2031). La valeur terminale prolonge un flux de 2031 qui n'est pas normatif. Le plan suppose en outre une reprise lente après la baisse de 2026.
- **L'ANCC surestime ce que l'on peut réaliser.** Le prix du vrac est un prix de transactions entre professionnels, par petits lots : environ 90 000 hl AP échangés en 2026 dans toute l'appellation, moins que le stock d'AUBRESSAC (116 000 hl AP). Vendre une part significative de ce stock ferait baisser les prix. Ces prix ont déjà reculé en 2026 et restent volatils. L'ANCC ignore aussi le coût du portage : financement par crédits de campagne, part évaporée, entretien des chais.
- **Deux logiques différentes.** L'ANCC mesure une valeur de substance, ce que valent les actifs pris un à un ; elle ne tient pas compte de la marque AUBRESSAC, créée par la maison et non inscrite au bilan (aucun goodwill). La valeur par les flux mesure la capacité de l'entreprise à transformer ce stock en trésorerie ; pour un actionnaire minoritaire, qui ne peut pas décider de vendre les stocks, c'est la référence. Il faudrait un CMPC d'environ 7,11 % pour que la VCP par les flux égale l'ANCC (calcul non exigé).

**Valeur proposée (0,75 pt).** Le jury attend une proposition argumentée, pas un chiffre unique.
- **Fourchette de négociation pour la participation** : de **47,88 M€** (flux, après décote) à **81,08 M€** (ANCC, après décote), soit de 79,80 € à 135,14 € par action (`JUR-E03`).
- **Proposition possible** : retenir la valeur par les flux comme référence pour un minoritaire. L'ANCC sert de plafond, parce que le minoritaire ne peut pas réaliser le stock, et d'argument du vendeur. Une valeur centrale, moyenne des deux méthodes, est acceptable si elle est justifiée : VCP de 238,82 M€, participation après décote de **64,48 M€**, soit 107,47 € par action.
- **Argument de M. ROUVRAY.** 30 % de la valeur des eaux-de-vie au prix du vrac (332,00 M€) font bien 99,60 M€, plus que les 84,00 M€ demandés. Mais c'est une valeur brute : l'actionnaire n'a droit qu'à l'actif net. Il faut déduire la dette financière nette, qui finance pour l'essentiel ces stocks (88,00 M€ de crédits de campagne), et l'impôt latent. Sa part d'ANCC est de 90,09 M€, soit 81,08 M€ après décote, sous le prix demandé. La « valeur sûre » est contredite par le recul des prix du vrac en 2026 et par un marché de 90 000 hl AP, plus étroit que le stock d'AUBRESSAC (116 000 hl AP).
- Le prix envisagé par VALDIGNE Capital (84,00 M€, 140,00 € par action) dépasse la valeur de la participation par l'ANCC après décote (81,08 M€). Il revient à valoriser le stock au prix du vrac sans décote, alors que le minoritaire ne contrôle ni la vente des stocks ni le dividende.

**Réponses tolérées** : bouteilles et matières sèches omises du tableau (elles sont retenues au coût, sans effet) ; impôt latent calculé ligne par ligne (même total) ; ANCC présenté comme ANC + plus-values nettes (216,75 + 83,55) ; 135,13 € par action pour l'ANCC après décote (81,08 / 0,6 ; le montant exact 135,135 donne 135,14 en arrondi demi supérieur) ; valeur retenue différente (flux seuls, ANCC décoté, moyenne pondérée) si elle est justifiée par la position de minoritaire, la liquidité du marché du vrac et le poids de la valeur terminale ; mention d'un goodwill (rente) comme prolongement, sans calcul.

**Erreurs fréquentes**
- Appliquer le prix du vrac aux valeurs au coût en M€, ou oublier les quantités.
- Oublier l'impôt latent, ou le calculer sur la valeur totale des stocks plutôt que sur la plus-value.
- Réévaluer les droits d'utilisation ou retrancher deux fois la dette nette de l'ANCC.
- Conclure que l'ANCC est « la vraie valeur » parce qu'il est plus élevé, sans discuter la profondeur du marché du vrac ni la position du minoritaire.
- `JUR-E03` — méthodes non croisées ; `JUR-T13` — commentaire sans les chiffres du cas.

---

### 2.4 Rentabilité réalisée par VALDIGNE Capital et rentabilité exigée (2 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.4-01 | Flux : − 45,00 (date 0) ; 1,20 ; 1,50 ; 1,80 ; 1,95 ; 2,025 (dates 1 à 5) ; 84,00 (date 6) ; TRI = **13,50 %** | 0,75 |
| 2.4-02 | TRI inférieur aux 15 % exigés ; dividendes reçus de 8,475 M€ seulement : le prix de cession fait l'essentiel de la rentabilité | 0,5 |
| 2.4-03 | Lien entre incertitude et rentabilité exigée d'un fonds de capital-investissement, relié au cas | 0,75 |

**Flux et TRI (0,75 pt).** Le dividende reçu chaque année vaut 30 % du dividende total (M€).

| Date | 0 (janv. 2021) | 1 (2022) | 2 (2023) | 3 (2024) | 4 (2025) | 5 (2026) | 6 (2027) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Flux de VALDIGNE Capital | − 45,00 | 1,20 | 1,50 | 1,80 | 1,95 | 2,025 | 84,00 |

TRI : taux t tel que − 45,00 + 1,20 / (1 + t) + 1,50 / (1 + t)² + 1,80 / (1 + t)³ + 1,95 / (1 + t)⁴ + 2,025 / (1 + t)⁵ + 84,00 / (1 + t)⁶ = 0, soit **t = 13,50 %**. À 15 %, la valeur actuelle des flux est négative (− 3,20 M€), ce qui confirme un TRI inférieur.

**Comparaison (0,5 pt).**
- Au prix envisagé, VALDIGNE Capital obtient **13,50 %**, en dessous des **15 %** fixés par son règlement : même au prix qu'il demande, l'investissement n'atteint pas l'objectif.
- Le fonds récupère 8,475 + 84,00 = 92,475 M€ pour 45,00 M€ investis, soit un **multiple de 2,06** (92,475 / 45,00 = 2,055) (calcul non exigé, valorisé). Les dividendes ne pèsent que 8,475 M€ : la rentabilité dépend presque entièrement du prix de cession (le prix seul donnerait 10,96 % par an).
- Pour obtenir 15 %, il faudrait un prix de **91,41 M€** (152,34 € par action), au-dessus de la valeur par l'ANCC après décote (calcul non exigé, valorisé). À la valeur par les flux après décote (47,88 M€), le TRI tomberait à 4,13 %. D'où l'insistance du fonds sur la valeur des stocks.

**Incertitude et rentabilité exigée (0,75 pt).**
- Un investisseur exige une rentabilité d'autant plus élevée que l'incertitude sur les flux qu'il recevra est grande : la **prime de risque** rémunère cette incertitude (programme 5.2.a).
- Le capital-investissement cumule plusieurs incertitudes que le MEDAF ne rémunère pas :
  - un **risque spécifique non diversifié** : onze participations, dont AUBRESSAC pour 12 % des montants investis ;
  - l'**illiquidité** : pas de marché, une sortie qui dépend de la recherche d'un acquéreur, comme ici ;
  - la **position minoritaire** : le fonds ne décide ni du dividende ni de la stratégie ;
  - l'**asymétrie d'information** avec la famille, qui gère.
- Le fonds doit aussi servir à ses propres souscripteurs une rentabilité supérieure à celle des actions cotées, nette de ses frais. Enfin, une partie des participations d'un fonds échoue : les réussites doivent compenser les pertes.
- La rentabilité exigée de 15 % est donc bien supérieure au coût des fonds propres d'AUBRESSAC (11,25 %), calculé pour un investisseur diversifié avec une prime de 1,75 %. La différence reflète le risque que le fonds ne peut pas diversifier. Elle explique aussi pourquoi un acquéreur diversifié et patient, comme un fonds de pension, peut accepter une rentabilité plus faible (questions 2.5 et 2.6).

**Réponses tolérées** : TRI entre 13,49 % et 13,51 % (interpolation) ; multiple de 2,05 ou 2,06 ; flux datés au mois (TRI voisin, si la convention est explicitée) ; mention de l'alpha recherché ou de l'effet de levier absent ici (pas de dette d'acquisition), si elle est reliée au cas.

**Erreurs fréquentes**
- Calculer une rentabilité simple ((92,475 − 45) / 45 = 105,50 %) au lieu d'un taux annuel actuariel.
- Compter le dividende au titre de 2026, que VALDIGNE Capital ne perçoit pas (hypothèse de l'annexe 2.4).
- Prendre 100 % des dividendes au lieu de 30 %.
- `JUR-T04` — TRI non maîtrisé ; `JUR-T02` — notion de prime de risque énoncée sans lien avec le fonds.

---

### 2.5 Valeur d'une action pour le fonds de pension et prix maximal (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.5-01 | Prochain dividende (2033) = 6,50 × 1,03 = **6,695 €** ; prix de revente en 2032 = 6,695 / (0,095 − 0,03) = **103,00 €** | 0,5 |
| 2.5-02 | Dividendes actualisés 4,11 ; 4,17 ; 4,19 ; 4,17 ; 4,13, somme **20,77** ; prix actualisé **65,43** ; valeur théorique **86,20 €** | 0,5 |
| 2.5-03 | Prix maximal **51,72 M€** ; écart de **32,28 M€** avec les 84,00 M€ demandés ; proche de la valeur par les flux ; à 140,00 € par action, prix supérieur à sa valeur théorique de 86,20 €, le candidat n'obtiendrait pas les 9,50 % qu'il exige | 0,5 |

**Prix de revente (0,5 pt).** Par le modèle de Gordon et Shapiro, le prix en 2032 est égal au prochain dividende divisé par l'écart entre la rentabilité exigée et la croissance : prochain dividende = 6,50 × 1,03 = **6,695 €** ; prix de revente = 6,695 / (0,095 − 0,03) = 6,695 / 0,065 = **103,00 €**.

**Valeur théorique d'une action (0,5 pt)** (€ par action, actualisation à 9,50 %).

| Date | 1 (2028) | 2 (2029) | 3 (2030) | 4 (2031) | 5 (2032) | Total |
|---|---:|---:|---:|---:|---:|---:|
| Dividende | 4,50 | 5,00 | 5,50 | 6,00 | 6,50 | |
| Prix de revente | | | | | 103,00 | |
| Coefficient 1,095^−n | 0,913242 | 0,834011 | 0,761654 | 0,695574 | 0,635228 | |
| Dividende actualisé | 4,11 | 4,17 | 4,19 | 4,17 | 4,13 | **20,77** |
| Prix actualisé | | | | | 65,43 | **65,43** |

Valeur théorique d'une action = 20,77 + 65,43 = **86,20 €**.

**Prix maximal et comparaisons (0,5 pt).**
- Prix maximal = 86,20 € × 600 000 actions = **51,72 M€**.
- L'écart avec le prix envisagé par VALDIGNE Capital (84,00 M€) est de **32,28 M€**, soit 53,80 € par action.
- Le prix maximal est proche de la valeur par les flux (88,67 € par action avant décote, 79,80 € après) et loin de l'ANCC (150,15 € ; 135,14 € après décote). Le candidat raisonne en flux reçus : il ne pourra pas vendre les stocks.
- À 140,00 € par action, le candidat obtiendrait une rentabilité de **− 1,51 %** par an avec ses propres hypothèses de dividendes et de revente. À son prix maximal, VALDIGNE Capital n'obtiendrait que **5,35 %** par an (calculs non exigés, valorisés).
- **Réalisme des hypothèses du candidat** (valorisé) : 4,50 € par action en 2028 font 9,00 M€, à peu près le flux de trésorerie disponible de 2028 (10,00 M€) diminué des intérêts après impôt (environ 5 M€ pour une DFN de 133,65 M€ à 5 %) : les premiers dividendes seraient en partie financés par la dette, au détriment des achats d'eaux-de-vie.
- Les deux positions sont éloignées. La négociation portera sur la valeur du stock que le candidat accepte de reconnaître, sur le dividende et sur le prix de revente, très sensible : 75,90 % de la valeur théorique vient du prix de 2032 (65,43 / 86,20).

**Réponses tolérées** : prochain dividende arrondi à 6,70 € et prix de revente de 103,08 € (valeur théorique 86,25 €, prix maximal 51,75 M€), si l'arrondi est signalé ; valeur théorique de 86,19 € à 86,21 € par les arrondis ; actualisation en une seule fois du dividende et du prix de 2032 (109,50 × 0,635228 = 69,56).

**Erreurs fréquentes**
- Calculer le prix de revente avec le dividende de 2032 (6,50 / 0,065 = 100,00) au lieu du prochain dividende.
- Actualiser le prix de revente sur six ans, ou oublier de l'actualiser.
- Utiliser le CMPC ou le coût des fonds propres d'AUBRESSAC au lieu de la rentabilité exigée par le candidat.
- `JUR-T04` — actualisation non maîtrisée.

---

### 2.6 Portefeuille du candidat avant et après l'entrée, risques et diversification (4 pts)

| Item | Attendu | Points |
|---|---|---:|
| 2.6-01 | Avant : Sharpe de P = (8,50 − 4,00) / 14,00 = **0,3214** ; Treynor de P = 4,50 / 0,90 = **5,00 %** ; A seul : Sharpe **0,2708**, Treynor **5,91 %** | 0,5 |
| 2.6-02 | Après : rentabilité espérée 0,9 × 8,50 + 0,1 × 10,50 = **8,70 %** ; bêta 0,9 × 0,90 + 0,1 × 1,10 = **0,9200** | 0,5 |
| 2.6-03 | Variance = 0,81 × 0,0196 + 0,01 × 0,0576 + 2 × 0,9 × 0,1 × 0,45 × 0,14 × 0,24 = **0,019174** ; écart-type **13,85 %** | 0,75 |
| 2.6-04 | Après : Sharpe = 4,70 / 13,85 = **0,3394** ; Treynor = 4,70 / 0,92 = **5,11 %** ; les deux ratios s'améliorent | 0,5 |
| 2.6-05 | Décomposition : A, variance systématique **0,017424** (30,25 %), spécifique **0,040176** (69,75 %) ; P, **0,011664** (59,51 %) et **0,007936** (40,49 %) | 0,75 |
| 2.6-06 | Diversification au sens de Markowitz (1952) : rôle de la corrélation de 0,45, écart-type de 15,00 % si la corrélation était de 1 ; conséquences pour la négociation | 1 |

**Avant l'entrée (0,5 pt).**

| | Portefeuille actuel P | Participation A seule |
|---|---:|---:|
| Rentabilité espérée | 8,50 % | 10,50 % |
| Écart-type | 14,00 % | 24,00 % |
| Bêta | 0,90 | 1,10 |
| Ratio de Sharpe | (8,50 − 4,00) / 14,00 = **0,3214** | (10,50 − 4,00) / 24,00 = **0,2708** |
| Ratio de Treynor | 4,50 / 0,90 = **5,00 %** | 6,50 / 1,10 = **5,91 %** |

**Après l'entrée : rentabilité et bêta (0,5 pt).** Rentabilité espérée = 0,90 × 8,50 % + 0,10 × 10,50 % = **8,70 %** ; bêta = 0,90 × 0,90 + 0,10 × 1,10 = **0,9200**.

**Variance et écart-type (0,75 pt).**
- Covariance = 0,45 × 0,14 × 0,24 = 0,015120.
- Variance = 0,90² × 0,14² + 0,10² × 0,24² + 2 × 0,90 × 0,10 × 0,015120 = 0,015876 + 0,000576 + 0,002722 = **0,019174**.
- Écart-type = √0,019174 = **13,85 %**.

**Ratios après l'entrée (0,5 pt).** Sharpe = (8,70 − 4,00) / 13,85 = **0,3394**, contre 0,3214 ; Treynor = 4,70 / 0,92 = **5,11 %**, contre 5,00 %. La rentabilité espérée par unité de risque total et par unité de risque systématique augmente : la participation améliore le portefeuille.

**Décomposition du risque (0,75 pt).** Variance du marché = 0,12² = 0,0144 ; variance systématique = bêta² × 0,0144.

| | Variance totale | Variance systématique | Variance spécifique | Part systématique | Écart-type spécifique |
|---|---:|---:|---:|---:|---:|
| Participation A | 0,057600 | 1,21 × 0,0144 = **0,017424** | **0,040176** | 30,25 % | 20,04 % |
| Portefeuille actuel P | 0,019600 | 0,81 × 0,0144 = **0,011664** | **0,007936** | 59,51 % | 8,91 % |

- Le **risque systématique** vient du marché (conjoncture, taux, consommation de produits haut de gamme) et ne se diversifie pas : seul le bêta le mesure.
- Le **risque spécifique** tient à l'entreprise : une seule appellation, deux marchés dominants, le gel, la succession, une famille majoritaire. Il se réduit quand on combine des actifs dont les rentabilités ne varient pas ensemble.
- 69,75 % du risque d'AUBRESSAC est spécifique. Pour un fonds diversifié, ce risque s'efface en grande partie ; pour VALDIGNE Capital, il ne s'efface pas.

**Diversification au sens de Markowitz (1952) et négociation (1 pt).**
- Le risque d'un portefeuille ne dépend pas seulement des écarts-types des actifs, mais de leurs **covariances**, donc de leur corrélation. Avec une corrélation de 1, l'écart-type serait la moyenne pondérée des écarts-types : 0,90 × 14,00 % + 0,10 × 24,00 % = **15,00 %**. Avec 0,45, il est de **13,85 %**, inférieur même à celui de P seul (14,00 %), bien que A soit beaucoup plus risquée.
- Ajouter un peu de A réduit le risque parce que la covariance entre A et P (0,015120) est inférieure à la variance de P (0,019600). Autrement dit, la corrélation (0,45) est inférieure au rapport des écarts-types (14 / 24 = 0,58). La diversification élimine une partie du risque spécifique de A ; elle ne réduit pas le risque systématique : le bêta augmente légèrement, de 0,90 à 0,92.
- **Pour la négociation** :
  - ARVENSTAD Pensioenfonds, diversifié et à horizon long, n'a pas à être rémunéré pour le risque spécifique d'AUBRESSAC. Sa rentabilité exigée (9,50 %) est égale au MEDAF pour un bêta de 1,10 (4,00 % + 1,10 × 5,00 %), sans prime de taille ni de risque spécifique. VALDIGNE Capital, peu diversifié, exige 15 %. C'est cette différence qui crée de la valeur dans la cession : la participation vaut plus pour un acheteur diversifié que pour le vendeur.
  - L'amélioration du portefeuille dépend du prix : la rentabilité espérée de A (10,50 %) suppose un achat au prix envisagé par le candidat. Payer plus réduirait cette rentabilité et pourrait annuler le gain sur les ratios.
  - Le candidat peut donc justifier un prix au-dessus de la valeur pour un fonds non diversifié, mais pas au-delà de son prix maximal de 51,72 M€.
- Le choix du poids de la participation n'est pas optimisé : seul le poids envisagé de 10 % est analysé.

**Réponses tolérées** : variance calculée sans arrondi intermédiaire (même résultat) ; écart-type de 13,85 % ou 13,86 % ; ratio de Sharpe après l'entrée de 0,3393 (4,70 / 13,85 = 0,33935) ; Treynor exprimé en fraction (0,0511) ; décomposition présentée en écarts-types (systématique : 13,20 % pour A et 10,80 % pour P) avec l'explication que les parts s'additionnent sur les variances ; remarque que A se situe au-dessus de la droite du MEDAF (10,50 % contre 9,50 %, alpha de 1 point) ; condition d'amélioration du ratio de Sharpe : Sharpe de A (0,2708) supérieur à ρ × Sharpe de P (0,1446).

**Erreurs fréquentes**
- Calculer l'écart-type du portefeuille comme la moyenne pondérée des écarts-types (15,00 %), en ignorant la corrélation.
- Oublier le facteur 2 ou les poids au carré dans la variance.
- Décomposer l'écart-type (et non la variance) en parts systématique et spécifique.
- Utiliser l'écart-type dans le ratio de Treynor ou le bêta dans le ratio de Sharpe.
- Affirmer que la diversification réduit le risque de marché.
- `JUR-T14` — Markowitz non mobilisé ; `JUR-T07` — absence de tableau.

---

### 2.7 Informations de durabilité et politique d'exclusion du candidat (1,5 pt)

| Item | Attendu | Points |
|---|---|---:|
| 2.7-01 | Secteur sensible : AUBRESSAC est exclu par principe (100 % du chiffre d'affaires en boissons alcoolisées > 10 %) ; seule la dérogation est possible ; l'argument de la présidente (produit de dégustation) n'est pas un critère de la politique | 0,5 |
| 2.7-02 | Lecture des cinq conditions avec les indicateurs : marketing 2,1 % < 5 % ; contrôle de l'âge déclaratif ; festival de 2026 ; eau en hausse (3,9 à 4,4 m³ par hl AP) sans objectif ; autres émissions indirectes non mesurées (environ 85 % du total) ; aucune vérification | 0,5 |
| 2.7-03 | Conclusion : la réserve ne peut pas être levée en l'état ; plan d'amélioration crédible et calendrier ; effet sur le prix et sur le dialogue actionnarial | 0,5 |

**Secteur sensible (0,5 pt).**
- La politique d'ARVENSTAD Pensioenfonds relève d'une stratégie d'**exclusion sectorielle**, avec une dérogation possible. AUBRESSAC réalise 100 % de son chiffre d'affaires avec des cognacs, au-delà du seuil de 10 % : la participation est exclue par principe. Seule une dérogation du comité, soumise à cinq conditions cumulatives, peut la rendre possible.
- La politique exprime l'engagement du candidat, signataire des Principes pour l'investissement responsable (ONU, 2006), de tenir compte des enjeux ESG dans ses décisions et de les justifier auprès de ses bénéficiaires, ici des salariés de l'agroalimentaire.
- L'argument de Mme AUBRESSAC (produit de dégustation, vendu cher) peut éclairer le dossier de dérogation, mais il ne remplace aucune des cinq conditions.

**Lecture des indicateurs au regard des conditions (0,5 pt).**

| Condition | Information d'AUBRESSAC | Appréciation |
|---|---|---|
| 1. Pas de pratique visant des mineurs, pas de controverse grave en trois ans | charte de l'interprofession depuis 2023 ; parrainage d'un festival à Singapour (40 % du public de moins de 25 ans), dénoncé par une association, sans procédure, parrainage arrêté | **à apprécier** : pas de pratique établie visant des mineurs, mais une controverse sur la cible jeune ; le comité doit juger sa gravité |
| 2. 5 % du budget de marketing pour la modération et contrôle de l'âge en ligne | 2,1 % en 2026 (1,6 % en 2024) ; âge vérifié par simple déclaration | **non remplie** : progression lente, encore loin des 5 % ; contrôle déclaratif insuffisant |
| 3. Suivi de l'eau et objectif de réduction | suivi existant ; 3,9 puis 4,4 m³ par hl AP (+ 0,5 m³ en deux ans) ; aucun objectif | **non remplie** : indicateur publié, mais tendance défavorable et pas d'objectif |
| 4. Mesure de toutes les émissions et objectif | émissions directes et liées à l'énergie mesurées, en baisse (2 280 à 2 100 t) avec un objectif de − 30 % ; autres émissions non mesurées, environ 85 % du total | **non remplie** : l'objectif ne couvre qu'environ 15 % des émissions ; verre, étuis et transport vers l'Asie et les États-Unis ne sont pas mesurés |
| 5. Vérification par un tiers | publication volontaire, aucune vérification | **non remplie** : crédibilité limitée |

- **Points forts** : certification environnementale de tout le vignoble du groupe depuis 2025 ; baisse des émissions liées à l'énergie ; charte de communication responsable ; réaction rapide au festival.
- **Crédibilité des données** : informations volontaires, non vérifiées, sur trois ans, avec une estimation de la société pour l'essentiel des émissions. Le candidat ne peut pas fonder une dérogation sur ces données sans contrôle. Le risque est double : un risque de réputation pour un fonds de pension qui investit dans l'alcool, et un écart entre les engagements affichés et les indicateurs (`JUR-T05`).

**Conclusion et améliorations (0,5 pt).**
- **En l'état, la réserve ne peut pas être levée** : au moins quatre des cinq conditions ne sont pas remplies (2 à 5), et la première reste discutable.
- **Améliorations à présenter au candidat, avec un calendrier** :
  - porter la part du budget de marketing consacrée à la modération à au moins 5 %, et instaurer un contrôle effectif de l'âge sur le site de vente en ligne ;
  - adopter une règle de choix des parrainages (âge du public) applicable aux filiales ;
  - fixer un objectif de réduction de la consommation d'eau par hl AP ;
  - mesurer les autres émissions indirectes, en commençant par le poids des bouteilles et le transport, puis fixer un objectif ;
  - faire vérifier les indicateurs par un tiers indépendant.
- **Effet sur la cession** :
  - si les conditions ne sont pas réunies avant la cession, le candidat peut renoncer, ce qui réduit le nombre d'acquéreurs possibles et affaiblit VALDIGNE Capital dans la négociation ;
  - il peut aussi subordonner son entrée à un plan suivi en conseil de surveillance, en exerçant ensuite son influence d'actionnaire (dialogue, vote) ;
  - le risque ESG non maîtrisé peut aussi peser sur sa rentabilité exigée et sur son prix.

**Réponses tolérées** : condition 1 jugée remplie (aucune procédure, parrainage arrêté) ou non remplie (controverse sur un public jeune), si le choix est justifié ; mention de SFDR ou du label ISR comme cadres de l'investisseur, sans détail réglementaire ; lien avec la double matérialité (impact du produit sur la santé, risque pour la valeur), s'il reste bref.

**Erreurs fréquentes**
- Calculer une note ou un score : la question demande une lecture et une interprétation.
- Juger les conditions sans citer les chiffres de l'annexe, ou les considérer comme remplies parce que des indicateurs sont publiés.
- Ignorer la crédibilité des données (non vérifiées, estimées).
- Développer la conformité réglementaire d'AUBRESSAC à des obligations de publication, que l'énoncé ne donne pas.
- `JUR-D01` — RSE et ESG confondus ; `JUR-T13` — réponse sans lien avec le cas.
