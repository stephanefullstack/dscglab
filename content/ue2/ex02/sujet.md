# DSCG UE 2 — Finance — Exercice d'entraînement n° 2

**DOSSIER 2 – GESTION DES RISQUES DE CHANGE, DE TAUX ET CLIMATIQUE D'ORVANE (15 points)**

Durée conseillée : 55 minutes (sur une épreuve de 3 heures, coefficient 1, notée sur 50).

Le sujet et son corrigé ont été construits sur la base de la réglementation applicable au 31/12/2026, sauf mention contraire.

**Document autorisé** : aucun.

**Matériel autorisé** : calculatrice avec mode examen actif, ou calculatrice sans mémoire « type collège ».

### AVERTISSEMENT

Si le texte du sujet, de ses questions ou de ses annexes vous conduit à formuler une ou plusieurs hypothèses, il vous est demandé de la (ou les) mentionner explicitement dans votre copie. Toutes les réponses devront être justifiées.

Il vous est demandé d'apporter un soin particulier à la présentation de votre copie et à la qualité rédactionnelle.

---

## Présentation

La SAS ORVANE conçoit et fabrique des pompes à chaleur pour l'habitat collectif et les bâtiments tertiaires. Installée dans la région lyonnaise, elle emploie 410 salariés et a réalisé en 2026 un chiffre d'affaires de 80 000 k€ pour un EBITDA de 9 600 k€. Sa présidente, Mme Hélène VARENNE, prépare l'entrée au capital d'un fonds d'investissement spécialisé dans la transition énergétique et souhaite présenter à celui-ci une politique de gestion des risques maîtrisée.

Trois expositions inquiètent la direction financière au 31 décembre 2026 :
- les compresseurs à haut rendement sont achetés à un fournisseur américain et facturés en dollars ;
- la nouvelle ligne de production sera financée par un emprunt bancaire à taux variable ;
- une partie de l'activité dépend de la rigueur de l'hiver : lors d'un hiver doux, les gestionnaires d'immeubles reportent le remplacement de leurs installations de chauffage.

Collaborateur du cabinet d'expertise comptable qui accompagne ORVANE, vous êtes chargé d'analyser ces risques et de proposer des couvertures. Les entreprises citées sont fictives.

### Travail à faire

**Base documentaire : annexes 2.1 à 2.3**

**2.1.** Caractériser la position de change d'ORVANE et le risque qu'elle supporte. Calculer le cours à terme proposé par la banque et le coût en euros de la commande s'il est retenu. Expliquer pourquoi ce coût est inférieur à celui obtenu au cours comptant du jour. *(3 points)*

**2.2.** Convertir en euros la prime de l'option et la décomposer en valeur intrinsèque et en valeur temps au 31/12/2026. Déterminer le coût en euros de la commande, prime comprise, dans chacun des deux scénarios de l'annexe 2.1, et le comparer à celui de la couverture à terme et à celui de l'absence de couverture. Recommander une couverture à la direction. *(3 points)*

**2.3.** Pour le premier trimestre de l'emprunt, calculer dans chacun des deux scénarios de l'annexe 2.2 le coût des intérêts et le taux annuel correspondant (coût du trimestre / [12 000 000 × 90/360]) sans couverture, avec le swap et avec le cap. Présenter les résultats dans un tableau et conseiller la direction. *(4 points)*

**2.4.** Calculer, pour chacun des trois scénarios de l'annexe 2.3, l'indemnité versée par l'option climatique et l'effet net de l'hiver et de la couverture sur le résultat avant impôt d'ORVANE pour la saison 2027-2028. Expliquer la nature du risque couvert et les limites de cette couverture. *(3 points)*

**2.5.** Mme VARENNE estime qu'avec l'option climatique, « le risque climatique d'ORVANE est réglé ». Discuter cette affirmation. *(2 points)*

### ANNEXE 2.1 – Commande de compresseurs en dollars

ORVANE a passé commande le 31/12/2026 de compresseurs pour **2 000 000 USD**, payables le **31/03/2027**, soit dans 90 jours.

| Donnée au 31/12/2026 | Valeur |
|---|---|
| Cours comptant EUR/USD (cotation au certain : 1 EUR = x USD) | 1,1200 |
| Taux d'intérêt de l'euro à 3 mois (annuel) | 2,60 % |
| Taux d'intérêt du dollar à 3 mois (annuel) | 4,00 % |

Couvertures proposées par la banque :
- **achat à terme** de 2 000 000 USD à échéance du 31/03/2027, au cours à terme calculé par la parité des taux d'intérêt : F = S × (1 + r USD × j/360) / (1 + r EUR × j/360), arrondi à quatre décimales ;
- **option** d'achat de 2 000 000 USD contre euros (call USD / put EUR), européenne, échéance 31/03/2027, prix d'exercice 1 EUR = 1,1200 USD, prime de **1,2 % du nominal en dollars**, payée le 31/12/2026 et convertie au cours comptant du jour.

Pour simplifier, on néglige le coût de financement de la prime entre le 31/12/2026 et le 31/03/2027.

Scénarios de cours comptant au 31/03/2027 retenus par la direction : **1 EUR = 1,0800 USD** et **1 EUR = 1,1600 USD**.

### ANNEXE 2.2 – Emprunt de la nouvelle ligne de production

| Caractéristique | Valeur |
|---|---|
| Montant emprunté le 01/01/2027 | 12 000 000 € |
| Durée | 5 ans, remboursement in fine |
| Taux | Euribor 3 mois + 2,10 %, payé chaque trimestre |
| Premier trimestre | du 01/01/2027 au 01/04/2027, soit 90 jours |

Intérêts calculés en base Exact/360 sur l'Euribor 3 mois constaté au début du trimestre.

Couvertures proposées par la banque, sur le nominal et la durée de l'emprunt :
- **swap de taux** : ORVANE paie un taux fixe de 2,90 % et reçoit l'Euribor 3 mois ; seul le différentiel est réglé chaque trimestre ;
- **cap** au taux plafond de 3,00 % sur l'Euribor 3 mois. Sa prime, de 0,25 % par an du nominal, est payée chaque trimestre au prorata du nombre de jours.

Scénarios d'Euribor 3 mois retenu pour le trimestre débutant le 01/01/2027 : **2,40 %** et **3,40 %**.

### ANNEXE 2.3 – Sensibilité de l'activité à l'hiver et option climatique

L'étude interne de la direction financière (données de 2015 à 2026) établit que l'EBITDA d'ORVANE varie de **4 000 € par degré-jour de chauffage** d'écart à la normale de **2 600 degrés-jours** sur la saison d'octobre à avril : il diminue lors d'un hiver plus doux, augmente lors d'un hiver plus froid.

Le nombre de degrés-jours de chauffage d'une saison est la somme, sur chaque jour, de l'écart entre 18 °C et la température moyenne du jour lorsque celle-ci est inférieure à 18 °C. Il est mesuré à une station météorologique de référence située à 30 km du siège.

La banque propose une **option de vente (put) sur l'indice de degrés-jours** de la saison d'octobre 2027 à avril 2028 :

| Caractéristique | Valeur |
|---|---|
| Prix d'exercice | 2 500 degrés-jours |
| Montant par degré-jour (tick) | 4 000 € |
| Indemnité maximale | 800 000 € |
| Prime | 120 000 € |

Scénarios d'indice retenus : **2 600** (hiver normal), **2 400** et **2 200** degrés-jours.
