# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Exercice d'entraînement n° 10 — Dossier 1 (45 points)

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F03 obligation de consolider, périmètre et méthodes (à jour au 22/10/2026) ; F04 retraitements (à jour au 23/10/2026) ; F05 écarts d'acquisition, goodwill et mise en équivalence (à jour au 23/10/2026) ; F99 liste noire (à jour au 22/10/2026). Les règles que les fiches ne reprennent pas (période d'incorporation des coûts d'emprunt, absence de reclassement en résultat des variations de juste valeur des titres à la juste valeur par les autres éléments du résultat global, traitement de leurs dividendes, structure de l'état du résultat global et du tableau des variations des capitaux propres) sont données au candidat par l'extrait du manuel de consolidation (annexe 1.8) ; le corrigé les signale [S]. Le groupe n'appliquant pas IFRS 18 par anticipation, la présentation de 2026 relève d'IAS 1 (voir F99 et F05 § 5). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre IFRS, coût amorti, goodwill complet et partiel, impôts différés, partage, mise en équivalence, variations des capitaux propres, 17 écritures, barème).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 a Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 1,5 |
| 1.1 b Périmètre | `2.1.c` Périmètre ; `2.1.d` Méthodes | 2 |
| 1.1 c Conséquences des qualifications | `2.1.d` Conséquences des méthodes de consolidation | 1 |
| 1.1 d Processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 0,5 |
| 1.2 a Coût amorti et TIE | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 1,5 |
| 1.2 b Tableaux de l'emprunt | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 2,5 |
| 1.2 c Écritures de l'emprunt | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 1,5 |
| 1.2 d Titres THERMALYS | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 3,5 |
| 1.3 Coûts d'emprunt | `2.2.c` Homogénéisation, thèmes communs | 5 |
| 1.4 Opérations internes | `2.2.f` Comptes réciproques et résultats internes | 3 |
| 1.5 a Actif net identifiable | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.5 b Frais d'acquisition | `2.2.g` Goodwill ; `2.2.c` Frais d'acquisition | 1,5 |
| 1.5 c Goodwill complet | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.5 d Écarts d'évaluation et partage | `2.2.g` ; `2.2.h` Partage des capitaux propres | 4 |
| 1.5 e Écritures LACUSTRA | `2.2.h` Partage des capitaux propres | 3 |
| 1.5 f Mise en équivalence d'ALPAGE RÉSIDENCES | `2.2.h` Partage des capitaux propres (MEE) | 3,5 |
| 1.6 a État du résultat net et des autres éléments du résultat global | `2.3.a` Documents de synthèse consolidés | 3,5 |
| 1.6 b Tableau des variations des capitaux propres | `2.3.a` Documents de synthèse consolidés | 2 |
| 1.6 c Différences avec le règlement ANC 2020-01 | `2.3.a` ; `2.1.d` | 1,5 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = participations ne donnant pas le contrôle (PNC) ; `CAP_ELIM` = capital de la filiale éliminé ; `EA` = goodwill ; `TME` = titres mis en équivalence ; `QP_MEE` = quote-part dans le résultat des entreprises mises en équivalence ; `IDP` = impôt différé passif ; `CH_ID` = charge ou produit d'impôt différé ; `AERG` = autres éléments du résultat global cumulés en capitaux propres (ici la réserve de juste valeur) ; `RES_CR` = contrepartie au compte de résultat.

---

### 1.1 Cadre et périmètre de la consolidation (5 pts)

#### a. Obligation de consolider et référentiel (1,5 pt)

**Obligation (1 pt).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. ARVELLE, SA, contrôle exclusivement LACUSTRA et conjointement ALPAGE RÉSIDENCES (voir b) : elle entre dans le champ de l'obligation (0,5 pt). Aucune exemption ne lui est ouverte (0,5 pt) :
- elle n'est contrôlée par aucune société, ce qui écarte l'exemption de la société incluse dans les comptes consolidés d'une entité qui la contrôle ; cette exemption serait d'ailleurs fermée à une société qui émet des valeurs mobilières admises sur un marché réglementé [V L. 233-17, 1° ; F03 § 1.1] ;
- l'exemption des ensembles qui ne sont pas de « grands groupes » est refusée dès qu'une entité de l'ensemble a des titres financiers admis sur un marché réglementé [V L. 233-17, 2° ; L. 123-16-2 ; F03 § 1.1], ce qui est le cas d'ARVELLE depuis l'émission de son emprunt. Au surplus, l'ensemble dépasse les trois seuils (30 M€ de bilan, 60 M€ de chiffre d'affaires, 250 salariés) à la clôture de 2025 comme de 2026 [V L. 230-2, 3° ; D. 230-2 ; F03 § 1.1].

**Référentiel (0,5 pt).** Les comptes consolidés des sociétés dont les titres sont admis aux négociations sur un marché réglementé d'un État membre à la date de clôture sont établis selon les IFRS adoptées par l'Union européenne [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Les titres visés ne se limitent pas aux actions : des obligations admises sur Euronext Paris suffisent [S]. Au 31/12/2026, l'emprunt d'ARVELLE est admis sur un marché réglementé : l'option pour les IFRS, exercée depuis 2024 alors qu'ARVELLE aurait pu appliquer le règlement ANC n° 2020-01 [V L. 233-24 ; F03 § 1.2], devient une obligation.

#### b. Périmètre au 31/12/2026 (2 pts)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % des PNC |
|---|---:|---|---|---:|---:|
| ARVELLE | — | Société mère | — | 100 % | — |
| LACUSTRA | 70 % | Contrôle exclusif (filiale) | Intégration globale | 70 % | 30 % |
| ALPAGE RÉSIDENCES | 50 % | Contrôle conjoint (coentreprise) | Mise en équivalence | 50 % | — |
| THERMALYS | 15 % | Ni contrôle ni influence notable | Non consolidée | — | — |

- **LACUSTRA (0,75 pt)** : avec 70 % des droits de vote, sans pacte contraire, et la nomination du président, ARVELLE a le pouvoir sur les activités pertinentes, est exposée à des rendements variables et peut agir sur eux [V IFRS 10 § 7 ; F03 § 2]. Intégration globale, les PNC (30 %) étant présentées séparément dans les capitaux propres [V IFRS 10 § 22 ; F03 § 3].
- **ALPAGE RÉSIDENCES (0,75 pt)** : le pacte impose l'unanimité des deux associés sur les décisions relatives aux activités pertinentes (budget, investissements, tarifs, dirigeant) : contrôle conjoint [V IFRS 11 § 7 ; F03 § 2]. Le partenariat est structuré en société distincte, les associés ne garantissent pas les dettes, n'achètent pas la production et n'ont de droits que sur l'actif net : c'est une **coentreprise** et non une activité conjointe [V IFRS 11 § 14 et 16]. Mise en équivalence obligatoire [V IFRS 11 § 24 ; F03 § 3].
- **THERMALYS (0,5 pt)** : 15 % des droits de vote, sous le seuil de présomption de 20 % ; aucun représentant au conseil, relations commerciales limitées : l'influence notable est présumée absente et rien ne renverse la présomption [V IAS 28 § 5 et 6 ; F03 § 2]. THERMALYS est hors périmètre.

#### c. Conséquences des qualifications (1 pt)

- **ALPAGE RÉSIDENCES (0,5 pt)** : l'intégration proportionnelle n'existe pas en IFRS pour une coentreprise [V IFRS 11 § 24 ; F03 § 3 ; F99]. Ni les actifs et passifs, ni le chiffre d'affaires d'ALPAGE RÉSIDENCES n'entrent dans les comptes consolidés : les titres sont remplacés par une ligne « titres mis en équivalence » égale à la quote-part de l'actif net (goodwill éventuel compris), et le résultat consolidé comprend une ligne « quote-part dans le résultat des entreprises mises en équivalence » [V IAS 28 § 3 et 10 ; F05 § 4]. Il n'y a pas de PNC ; les dividendes reçus réduisent la valeur des titres au lieu d'être des produits [V IAS 28 § 10].
- **THERMALYS (0,5 pt)** : non consolidée, la participation reste un actif financier, instrument de capitaux propres régi par IFRS 9 et évalué à la juste valeur ; sur option irrévocable, les variations de juste valeur sont présentées dans les autres éléments du résultat global [V IFRS 9 § 4.1.4 et 5.7.5 ; F04 R11]. Seuls les dividendes reçus figurent au résultat (annexe 1.8, point 5).

#### d. Processus de consolidation (0,5 pt)

| Étape | Travaux du dossier |
|---|---|
| 1. Cadre et périmètre : obligation, référentiel, entités, pourcentages, méthodes | 1.1 |
| 2. Comptes individuels retraités aux méthodes du groupe (IFRS), impôts différés compris ; évaluation à la juste valeur des actifs et passifs de l'entité acquise | 1.2, 1.3, 1.5 a et b |
| 3. Cumul des comptes des entités intégrées globalement (ARVELLE, LACUSTRA) | service consolidation |
| 4. Élimination des opérations internes | 1.4, dividende d'ALPAGE RÉSIDENCES en 1.5 f |
| 5. Élimination des titres, goodwill, partage des capitaux propres ; mise en équivalence | 1.5 c à f |
| 6. États de synthèse : état de la situation financière, état du résultat net et des autres éléments du résultat global, tableau des variations des capitaux propres, notes | 1.6 |

(0,25 pt pour l'enchaînement des étapes, 0,25 pt pour le rattachement des questions.)

**Erreurs fréquentes** : ALPAGE RÉSIDENCES intégrée proportionnellement (méthode du règlement ANC, inexistante en IFRS pour une coentreprise) ; THERMALYS mise en équivalence ; référentiel justifié par la cotation des actions, alors qu'elles ne sont pas cotées ; passage des comptes individuels aux comptes consolidés mal compris (`JUR-G01`).

---

### 1.2 Instruments financiers (9 pts)

#### a. Évaluation de l'emprunt et taux d'intérêt effectif (1,5 pt)

| Niveau | Attendu |
|---|---|
| 0 | Absence de réponse ou réponse non pertinente |
| 0,5 | Évaluation initiale nette des coûts de transaction et évaluation ultérieure au coût amorti, sans explication du TIE |
| 1 | En plus, justification du TIE : taux qui égalise le montant net reçu et la valeur actualisée des décaissements futurs |
| 1,5 | En plus, conséquence comptable : les frais sont répartis selon le TIE dans la charge d'intérêts, qui traduit le coût réel de l'emprunt |

**Réponse attendue.** L'emprunt est un passif financier évalué au coût amorti [V IFRS 9 § 4.2.1 ; F04 R11]. À l'origine, il est évalué à sa juste valeur diminuée des coûts de transaction directement attribuables, soit le montant net reçu : 30 000 000 – 449 780 = **29 550 220 €** [V IFRS 9 § 5.1.1 ; F04 R6]. À chaque clôture, il est porté au coût amorti : valeur d'ouverture + intérêts au TIE – coupons payés.

Le TIE est le taux qui égalise le montant net encaissé à l'émission (29 550 220 €) et la valeur actualisée des décaissements futurs : cinq coupons de 1 200 000 € et le remboursement de 30 000 000 € le 31/12/2030. Il est supérieur au taux nominal (4 %) parce qu'il intègre le coût des frais d'émission. Appliqué chaque année au coût amorti d'ouverture, il donne la charge financière réelle de l'emprunt : sur 5 ans, 6 000 000 € de coupons + 449 780 € de frais = 6 449 780 €, répartis selon un rythme actuariel et non linéaire [V corrigé du sujet zéro p. imprimée 210 ; F04 R11]. Le candidat n'a pas à le recalculer (taux fourni) [V programme ; guide p. imprimée 171].

#### b. Tableaux (2,5 pts)

**Ligne 2026 du tableau de suivi au coût amorti (1 pt)**

| Exercice | Coût amorti au 01/01 | Intérêts au TIE (4,34 %) | Coupon payé | Coût amorti au 31/12 |
|---|---:|---:|---:|---:|
| 2026 | 29 550 220 (0,25 pt) | 1 282 480 (0,5 pt) | 1 200 000 | 29 632 700 (0,25 pt) |

Intérêts : 29 550 220 × 4,34 % = 1 282 479,5 arrondi à 1 282 480 €. La différence avec le coupon (82 480 €) est la part des frais d'émission imputée en 2026 au rythme actuariel.

**Comparaison au 31/12/2026 (1,5 pt)**

| Élément | Comptes individuels (PCG) | Comptes consolidés (IFRS) | Écart (IFRS – PCG) |
|---|---:|---:|---:|
| Emprunt (163) | 30 000 000 | 29 632 700 | – 367 300 |
| Frais d'émission à répartir (481) | 359 824 (449 780 – 89 956) | 0 | – 359 824 |
| Dette nette des frais | 29 640 176 | 29 632 700 | **– 7 476** (0,25 pt dette, 0,25 pt 481) |
| Charges financières 2026 | 1 289 956 (1 200 000 + 89 956) | 1 282 480 | **– 7 476** (0,25 pt) |
| Impôt différé passif (25 %) | | | **1 869** (0,25 pt) |
| **Incidence nette** | | | **+ 5 607 sur le résultat 2026** ; aucune sur les réserves (émission en 2026) (0,5 pt) |

La dette nette est plus faible en IFRS que dans les comptes individuels (la répartition actuarielle impute moins de frais en début de vie que la répartition linéaire) ; la base fiscale suivant les comptes individuels (frais déduits au rythme linéaire), la différence de 7 476 € est imposable : impôt différé passif [V IAS 12 § 15 ; F04 R11 ; corrigé du sujet zéro p. imprimées 210-211].

#### c. Écritures (1,5 pt)

**O1 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 163 Autres emprunts obligataires | 367 300 | |
| 481 Frais d'émission des emprunts | | 359 824 |
| IDP Impôt différé passif | | 1 869 |
| RST.ARVELLE Résultat ARVELLE | | 5 607 |
| **Total** | **367 300** | **367 300** |

**O1R (compte de résultat, 0,75 pt)** : débit 6611 Intérêts des emprunts et dettes 82 480 ; débit CH_ID Charge d'impôt différé 1 869 ; débit RES_CR Résultat 5 607 ; crédit 6862 Dotations aux amortissements des frais d'émission des emprunts 89 956. Total 89 956.

#### d. Titres THERMALYS (3,5 pts)

**Catégorie (1 pt).** Les titres THERMALYS sont des instruments de capitaux propres : leurs flux ne sont pas uniquement des remboursements de principal et des intérêts, ils ne peuvent donc être évalués au coût amorti ; ils relèvent par défaut de la juste valeur par le résultat (0,5 pt). Non détenus à des fins de transaction, ils ouvrent droit à l'option irrévocable, exercée à la comptabilisation initiale, de présenter les variations de juste valeur dans les autres éléments du résultat global : catégorie des **actifs financiers à la juste valeur par les autres éléments du résultat global** (0,5 pt) [V IFRS 9 § 4.1.1, 4.1.4 et 5.7.5 ; F04 R11]. Le coût des comptes individuels est remplacé par la juste valeur.

**Incidence (1,5 pt)**

| | Cumul au 31/12/2025 (réserve de juste valeur) | Autres éléments du résultat global 2026 | Bilan au 31/12/2026 |
|---|---:|---:|---:|
| Variation de juste valeur | + 150 000 (1 950 000 – 1 800 000) | + 210 000 (2 160 000 – 1 950 000) | titres 2 160 000 (+ 360 000) |
| Impôt différé (25 %) | – 37 500 | – 52 500 | IDP 90 000 |
| **Net** | **+ 112 500** | **+ 157 500** | réserve de juste valeur **270 000** |

(0,75 pt pour les variations brutes et nettes, 0,5 pt pour l'impôt différé, 0,25 pt pour l'absence de reclassement ultérieur en résultat.) La plus-value latente n'est pas imposée, mais le serait à la cession : la base fiscale reste le coût (1 800 000 €), d'où un impôt différé passif qui suit les autres éléments du résultat global [V IAS 12 § 15 et 58 ; F04 § 1 ; hypothèse fiscale de l'annexe 1.4]. Ces gains ne seront jamais reclassés en résultat, même lors de la cession des titres (annexe 1.8, point 5) [S] : ils figurent parmi les éléments non reclassables de l'état du résultat global.

**Dividende (0,5 pt).** Le dividende reçu (15 % × 360 000 = 54 000 €) reste en résultat : il ne donne lieu à aucun retraitement (annexe 1.8, point 5) [S].

**T1 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 271 Titres immobilisés | 360 000 | |
| IDP Impôt différé passif | | 90 000 |
| AERG Réserve de juste valeur – cumul au 31/12/2025 | | 112 500 |
| AERG Réserve de juste valeur – autres éléments du résultat global 2026 | | 157 500 |
| **Total** | **360 000** | **360 000** |

Aucune écriture au compte de résultat : la variation de 2026 ne transite pas par le résultat net, elle est présentée dans les autres éléments du résultat global (question 1.6).

**Réponses tolérées (1.2)**
- Écriture O1 décomposée (annulation du 481, puis ajustement de l'emprunt) si les montants sont justes.
- Réserve de juste valeur présentée en une seule ligne de 270 000 €, si le candidat distingue dans son tableau la part de 2026 (157 500 €).
- Écriture de compte de résultat O1R présentée en « charges financières » sans distinction 6611 / 6862.

**Erreurs fréquentes (1.2)**
- Recalculer un TIE (non demandé) au lieu d'en expliquer le principe ; définitions IFRS 9 incomplètes (`JUR-G07`, `JUR-G08`).
- Écritures de l'emprunt erronées alors que le taux est fourni : frais d'émission laissés à l'actif, ou charge au TIE calculée sur le nominal (30 000 000 × 4,34 %) au lieu du coût amorti (`JUR-G05`).
- Oubli de l'impôt différé, ou impôt différé des titres THERMALYS porté en résultat ; variation de juste valeur de 2026 portée en résultat ; cumul de 2025 compté dans les autres éléments du résultat global de 2026.
- THERMALYS classée au coût amorti, ou dividende retraité.

**Références normatives (1.2)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 9 § 4.2.1, 5.1.1 | Passif au coût amorti, évaluation initiale nette des coûts de transaction | [V] | F04 R6, R11 |
| IFRS 9 § 4.1.1, 4.1.4, 5.7.5 | Classement des actifs, option irrévocable pour les instruments de capitaux propres | [V] | F04 R11 |
| IFRS 9 (absence de reclassement, dividendes en résultat) | Règle donnée par le manuel (annexe 1.8, point 5) | [S] | — |
| IAS 12 § 15, 58 | Passif d'impôt différé ; impôt suivant l'opération en autres éléments du résultat global | [V] | F04 § 1 |
| Corrigé du sujet zéro p. imprimées 209-211 | Catégories d'instruments financiers, justification du TIE, impôt différé de l'emprunt | [V] | F04 R11 |

---

### 1.3 Coûts d'emprunt de l'espace aquatique (5 pts)

**Justification (1,5 pt).** Dans les comptes individuels, l'incorporation des intérêts au coût des actifs éligibles est une option (PCG art. 213-9), que LACUSTRA n'a pas exercée [V F04 R6]. En IFRS, les coûts d'emprunt directement attribuables à un actif qualifié sont obligatoirement incorporés à son coût [V IAS 23 § 8 ; F04 R6], et le manuel impose cette méthode (annexe 1.8, point 3) : les comptes de LACUSTRA sont retraités pour être homogènes avec les méthodes du groupe [V IFRS 10 § 19 ; F04 § 1] (0,5 pt). L'espace aquatique exige quinze mois de travaux avant sa mise en service : c'est un actif qualifié (0,5 pt). L'emprunt de 3 600 000 € a été contracté spécifiquement pour le chantier : ses intérêts sont directement attribuables (0,5 pt).

**Calcul (1,25 pt).** L'incorporation commence le 01/03/2026, date à laquelle les travaux, les dépenses et les coûts d'emprunt ont commencé, et se poursuit jusqu'à la clôture puisque l'actif n'est pas prêt à être utilisé (annexe 1.8, point 3) [S]. Aucun produit de placement n'est à déduire.
- Intérêts incorporés : 3 600 000 × 4 % × 10/12 = **120 000 €** (0,75 pt).
- Les intérêts ayant été déduits fiscalement en 2026, la base fiscale de la construction en cours ne les comprend pas : impôt différé passif 120 000 × 25 % = **30 000 €** ; incidence nette sur le résultat 2026 de LACUSTRA : **+ 90 000 €** ; aucune incidence sur les réserves (0,5 pt) [V IAS 12 § 15 ; F04 § 1].

**C1 (bilan, 0,75 pt)** : débit 231 Immobilisations corporelles en cours 120 000 ; crédit IDP 30 000 ; crédit RST.LACUSTRA 90 000.

**C1R (compte de résultat, 0,75 pt)** : débit CH_ID Charge d'impôt différé 30 000 ; débit RES_CR Résultat 90 000 ; crédit 6611 Intérêts des emprunts et dettes 120 000.

L'incidence de + 90 000 € sur le résultat de LACUSTRA est partagée entre le groupe (70 %) et les PNC (30 %) à la question 1.5 d.

**Après la mise en service (0,75 pt).** L'incorporation cesse le 01/06/2027, lorsque l'espace aquatique est prêt à être utilisé : les intérêts courus ensuite sont des charges financières. Les intérêts incorporés de 2026 et de janvier à mai 2027 font partie du coût de l'actif et sont amortis avec lui sur 20 ans à compter du 01/06/2027 (annexes 1.5 et 1.8, point 3) ; l'impôt différé passif se reprend à mesure que la différence temporelle se résorbe, au rythme de cet amortissement [V IAS 12 § 15 ; F04 § 1].

**Réponses tolérées** : intérêts incorporés par un crédit au compte 722 « Production immobilisée » au lieu de l'annulation de la charge au compte 6611 ; calcul sur la base des dépenses engagées si le candidat le justifie et reconnaît que l'emprunt est spécifique (la solution attendue reste 120 000 €).

**Erreurs fréquentes** : incorporation sur 12 mois (l'emprunt et les travaux démarrent le 01/03/2026) ; amortissement des intérêts incorporés dès 2026 alors que l'actif n'est pas en service ; oubli de l'impôt différé ou de la répartition de l'incidence entre groupe et PNC ; retraitement non justifié (`JUR-G06`) ; réserves et résultat confondus (`JUR-G04`).

**Références normatives (1.3)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 23 § 8 | Incorporation obligatoire des coûts d'emprunt d'un actif qualifié | [V] | F04 R6 |
| PCG art. 213-9 | Option d'incorporation dans les comptes individuels | [V] | F04 R6 |
| IFRS 10 § 19 | Méthodes comptables uniformes | [V] | F04 § 1 |
| IAS 23 (définition de l'actif qualifié, début et fin de l'incorporation) | Règles données par le manuel (annexe 1.8, point 3) | [S] | — |
| IAS 12 § 15 | Passif d'impôt différé | [V] | F04 § 1 |

---

### 1.4 Opérations internes entre ARVELLE et LACUSTRA (3 pts)

**Identification et justification (1 pt).** LACUSTRA est intégrée globalement : les actifs, passifs, produits et charges réciproques sont éliminés en totalité, quel que soit le pourcentage d'intérêt [V IFRS 10 B86 c) ; F04 R14] (0,5 pt). Sont concernés : la redevance de la centrale de réservation (420 000 €) et la dette correspondante (60 000 €) ; le prêt de 1 500 000 €, les intérêts courus (1 500 000 × 3 % × 9/12 = **33 750 €**) et la créance et la dette d'intérêts correspondantes (0,5 pt).

**I1 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs | 60 000 | |
| 1681 Autres emprunts | 1 500 000 | |
| 1688 Intérêts courus sur autres emprunts et dettes assimilées | 33 750 | |
| 411 Clients | | 60 000 |
| 2748 Autres prêts | | 1 500 000 |
| 27684 Intérêts courus sur prêts | | 33 750 |
| **Total** | **1 593 750** | **1 593 750** |

**I1R (compte de résultat, 0,75 pt)** : débit 706 Prestations de services 420 000 ; débit 7626 Revenus des prêts 33 750 ; crédit 622 Rémunérations d'intermédiaires et honoraires 420 000 ; crédit 6611 Intérêts des emprunts et dettes 33 750. Total 453 750.

**Incidence (0,5 pt).** Le produit de l'une est exactement la charge de l'autre et aucune marge n'est stockée dans un actif : les éliminations ne modifient ni le résultat consolidé, ni la répartition entre groupe et PNC, et ne créent aucun impôt différé. Elles réduisent le chiffre d'affaires consolidé (420 000 €), les charges externes et le résultat financier brut, et évitent de gonfler le bilan (créances et dettes intra-groupe).

**Réponses tolérées** : écritures présentées en une seule écriture par opération (redevances, prêt) ; dettes et créances intra-groupe enregistrées dans les comptes de l'annexe sous des intitulés « groupe ».

**Erreurs fréquentes** : élimination à 70 % seulement ; impôt différé constaté sur une élimination sans incidence sur le résultat ; oubli des intérêts courus.

---

### 1.5 Regroupement d'entreprises et partage des capitaux propres (16 pts)

#### a. Actif net identifiable de LACUSTRA au 01/01/2026 (2 pts)

| Élément | Montant |
|---|---:|
| Capitaux propres de LACUSTRA (4 000 000 + 3 600 000) | 7 600 000 |
| Écart d'évaluation des terrains (4 800 000 – 2 400 000) (0,5 pt) | + 2 400 000 |
| Écart d'évaluation des constructions (3 800 000 – 3 000 000) (0,5 pt) | + 800 000 |
| Impôt différé passif sur les écarts (3 200 000 × 25 %) (0,5 pt) | – 800 000 |
| **Actif net identifiable à la juste valeur** (0,5 pt) | **10 000 000** |

Les actifs identifiables et les passifs repris sont évalués à leur juste valeur à la date d'acquisition ; l'impôt différé sur les écarts est constaté selon IAS 12, y compris sur les terrains non amortissables, la base fiscale restant celle des comptes individuels [V IFRS 3 § 24 ; IAS 12 § 66 ; F05 § 2 et § 5].

#### b. Frais d'acquisition (1,5 pt)

**Principe (0,5 pt).** En IFRS, les frais connexes à l'acquisition (honoraires de conseil, d'audit, d'avocats) sont des charges de l'exercice et n'entrent pas dans la contrepartie transférée [V IFRS 3 § 53 ; F04 R4 ; F05 § 2]. ARVELLE les a inclus dans le coût des titres, comme le permet le PCG : le coût est ramené à 8 400 000 € et les frais de 252 000 € sont portés en charges de 2026, sans impôt différé (hypothèse de l'annexe 1.2). C'est l'inverse du règlement ANC n° 2020-01, qui les inclut dans le coût d'acquisition, nets d'impôt [V art. 231-2 ; F05 § 1.1].

**F1 (bilan, 0,5 pt)** : débit RST.ARVELLE Résultat ARVELLE 252 000 ; crédit 261.ARVELLE Titres de participation LACUSTRA 252 000.

**F1R (compte de résultat, 0,5 pt)** : débit 6226 Honoraires 252 000 ; crédit RES_CR Résultat 252 000.

#### c. Goodwill (2 pts)

| Élément | Goodwill complet (méthode du groupe) | Goodwill partiel (pour comparaison) |
|---|---:|---:|
| Contrepartie transférée (hors frais) | 8 400 000 | 8 400 000 |
| + Participations ne donnant pas le contrôle | 3 450 000 (juste valeur) | 3 000 000 (30 % × 10 000 000) |
| – Actif net identifiable à la juste valeur | – 10 000 000 | – 10 000 000 |
| **Goodwill** | **1 850 000** (0,75 pt) | **1 400 000** |

[V IFRS 3 § 19 et 32 ; F05 § 2.1]

**Répartition (0,5 pt)** : part du groupe 8 400 000 – 70 % × 10 000 000 = **1 400 000 €** ; part des PNC 3 450 000 – 30 % × 10 000 000 = **450 000 €**.

**Explication de l'écart (0,75 pt).** La méthode du goodwill partiel, également permise par IFRS 3 (option ouverte pour chaque regroupement), évalue les PNC à leur quote-part de l'actif net identifiable (3 000 000 €) et ne reconnaît que le goodwill acquis par le groupe (1 400 000 €). Le goodwill complet ajoute la part des minoritaires (450 000 €), qui augmente d'autant les PNC au bilan. Cette part n'est pas proportionnelle à celle du groupe (450 000 / 30 % = 1 500 000 contre 1 400 000 / 70 % = 2 000 000 pour 100 %) : la juste valeur d'une action des minoritaires (3 450 000 / 120 000 = 28,75 €) est inférieure au prix payé par ARVELLE (30 €), qui comprend une prime de contrôle. Le goodwill n'est pas amorti ; aucune perte de valeur n'est à constater [V F05 § 2 ; annexe 1.2].

#### d. Écarts d'évaluation en 2026 et tableau de partage au 31/12/2026 (4 pts)

**Incidence des écarts d'évaluation en 2026 (0,75 pt)**

| | 01/01/2026 | Résultat 2026 | 31/12/2026 |
|---|---:|---:|---:|
| Écart sur terrains (non amortis) | 2 400 000 | — | 2 400 000 |
| Écart sur constructions | 800 000 | – 80 000 (800 000 / 10) | 720 000 |
| Impôt différé passif | – 800 000 | + 20 000 | – 780 000 |
| **Net** | **2 400 000** | **– 60 000** | **2 340 000** |

**Résultat retraité de LACUSTRA (0,5 pt)** : 1 300 000 – 60 000 (amortissement net de l'écart) + 90 000 (coûts d'emprunt, question 1.3) = **1 330 000 €**. Les éliminations de la question 1.4 sont sans incidence.

**Tableau de partage (2,75 pts)**

| Capitaux propres retraités de LACUSTRA au 31/12/2026 | Total | Groupe (70 %) | PNC (30 %) |
|---|---:|---:|---:|
| Capital | 4 000 000 | 2 800 000 | 1 200 000 |
| Réserves (comptes individuels) | 3 600 000 | 2 520 000 | 1 080 000 |
| Écarts d'évaluation nets à l'acquisition | 2 400 000 | 1 680 000 | 720 000 |
| **Sous-total : actif net identifiable à l'acquisition** (0,5 pt) | **10 000 000** | **7 000 000** | **3 000 000** |
| – Titres LACUSTRA éliminés (coût IFRS) | | – 8 400 000 | |
| Goodwill part du groupe (8 400 000 – 7 000 000) (0,5 pt) | | **1 400 000** | |
| + Goodwill revenant aux PNC (0,5 pt) | | | **+ 450 000** |
| Résultat retraité 2026 (0,5 pt) | 1 330 000 | **931 000** | **399 000** |

Répartition au bilan consolidé (0,75 pt) :
- goodwill : 1 400 000 + 450 000 = **1 850 000 €** ;
- réserves consolidées part du groupe : 7 000 000 – 8 400 000 + 1 400 000 = **0** (acquisition au 01/01/2026, aucune réserve postérieure à l'acquisition) ;
- résultat consolidé part du groupe : **931 000 €** ;
- PNC : 3 000 000 + 450 000 + 399 000 = **3 849 000 €**, dont 3 450 000 € de juste valeur à l'acquisition et 399 000 € de résultat.

Contrôle : 10 000 000 + 1 330 000 + 1 850 000 de goodwill = 13 180 000 = titres 8 400 000 + résultat groupe 931 000 + PNC 3 849 000.

#### e. Écritures relatives à LACUSTRA (3 pts)

**L1 (bilan, écarts d'évaluation à l'acquisition, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2111 Terrains nus | 2 400 000 | |
| 2131 Bâtiments | 800 000 | |
| IDP Impôt différé passif | | 800 000 |
| RSV.LACUSTRA Réserves LACUSTRA (écarts d'évaluation nets) | | 2 400 000 |
| **Total** | **3 200 000** | **3 200 000** |

**L2 (bilan, amortissement 2026 de l'écart, 0,5 pt)** : débit RST.LACUSTRA 60 000 ; débit IDP 20 000 ; crédit 28131 Amortissements des bâtiments 80 000.

**L2R (compte de résultat, 0,25 pt)** : débit 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles 80 000 ; crédit CH_ID Produit d'impôt différé 20 000 ; crédit RES_CR Résultat 60 000.

**L3 (bilan, élimination des titres et partage, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.LACUSTRA Capital LACUSTRA | 4 000 000 | |
| RSV.LACUSTRA Réserves LACUSTRA (3 600 000 + 2 400 000) | 6 000 000 | |
| RST.LACUSTRA Résultat LACUSTRA retraité | 1 330 000 | |
| EA Goodwill | 1 850 000 | |
| 261.ARVELLE Titres de participation LACUSTRA | | 8 400 000 |
| RST_G Résultat consolidé – part du groupe | | 931 000 |
| RSV_M PNC – juste valeur à l'acquisition | | 3 450 000 |
| RST_M PNC – résultat | | 399 000 |
| **Total** | **13 180 000** | **13 180 000** |

Le solde de RST.LACUSTRA éliminé (1 330 000 €) est celui que laissent les écritures C1 (+ 90 000) et L2 (– 60 000). Le titre éliminé (8 400 000 €) est celui que laisse l'écriture F1. Au compte de résultat, le résultat net est ensuite attribué au groupe (931 000 €) et aux PNC (399 000 €), sans écriture supplémentaire.

#### f. Mise en équivalence d'ALPAGE RÉSIDENCES (3,5 pts)

**Tableau de mise en équivalence au 31/12/2026 (1,25 pt)**

| | Capital et réserves | Résultat 2026 | Total |
|---|---:|---:|---:|
| Capitaux propres d'ALPAGE RÉSIDENCES (méthodes du groupe) | 6 500 000 | 900 000 | 7 400 000 |
| Quote-part du groupe (50 %) | 3 250 000 | 450 000 | **3 700 000** (0,5 pt) |
| – Titres ALPAGE RÉSIDENCES éliminés | – 3 000 000 | | |
| **Réserves et résultat consolidés, part du groupe** (0,5 pt) | **250 000** | **450 000** | |

Les titres ont été souscrits au pair à la constitution : ni écart d'évaluation, ni goodwill à inclure dans la participation (0,25 pt) [V IAS 28 § 32 ; F05 § 4].

**Dividende (0,75 pt).** Le dividende reçu (50 % × 400 000 = 200 000 €), inscrit en produits par ARVELLE, réduit la valeur de la participation : il est déjà pris en compte dans la valeur d'équivalence (réserves d'ALPAGE RÉSIDENCES diminuées de 400 000 €) [V IAS 28 § 10 ; F05 § 4]. Il est éliminé du résultat d'ARVELLE et reclassé en réserves.

**M1 (bilan)** : débit RST.ARVELLE 200 000 ; crédit RSV.ARVELLE 200 000. **M1R (compte de résultat)** : débit 7611 Revenus des titres de participation 200 000 ; crédit RES_CR 200 000.

**M2 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence | 3 700 000 | |
| 261.ARVELLE Titres de participation ALPAGE RÉSIDENCES | | 3 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 250 000 |
| RST_G Résultat consolidé – part du groupe | | 450 000 |
| **Total** | **3 700 000** | **3 700 000** |

**M2R (compte de résultat, 0,5 pt)** : débit RES_CR 450 000 ; crédit QP_MEE Quote-part dans le résultat des entreprises mises en équivalence 450 000.

**Évolution des titres mis en équivalence (0,25 pt)** : 50 % × 6 900 000 = 3 450 000 € au 31/12/2025 ; – 200 000 de dividende ; + 450 000 de quote-part du résultat 2026 = **3 700 000 €** au 31/12/2026. Les réserves consolidées issues d'ALPAGE RÉSIDENCES (250 000 + 200 000 reclassés par M1 = 450 000) correspondent à 50 % des résultats cumulés de 2024 et 2025 (100 000 + 800 000).

**Réponses tolérées (1.5)**
- Écarts d'évaluation (L1) et élimination des titres (L3) regroupés dans une seule écriture, si les montants sont justes.
- Écarts d'évaluation portés directement dans une écriture d'élimination créditant « écarts d'évaluation » puis repris dans le partage.
- M1 et M2 regroupées (titres mis en équivalence 3 700 000 ; réserves groupe 450 000 ; résultat ARVELLE – 200 000 ; résultat groupe 450 000).
- En 1.5 d, résultat retraité de LACUSTRA calculé sans le retraitement de la question 1.3 si celle-ci n'a pas été traitée : appliquer la cohérence (1 240 000 €, soit 868 000 et 372 000) et ne pénaliser qu'une fois.

**Erreurs fréquentes (1.5)**
- Frais d'acquisition laissés dans le coût des titres (goodwill complet de 2 102 000 € au lieu de 1 850 000 €) : c'est l'erreur symétrique de celle relevée par le jury en ANC, où ils doivent être inclus nets d'impôt (`JUR-G02`).
- Goodwill complet calculé avec 70 % de l'actif net, ou PNC portées à leur quote-part d'actif net malgré l'option du manuel ; part des PNC dans le goodwill oubliée dans les PNC au bilan.
- Impôt différé omis sur l'écart des terrains, ou amortissement de l'écart des terrains.
- Partage des capitaux propres sur les capitaux propres des comptes individuels, sans écarts d'évaluation ni retraitements (`JUR-G04`) ; dans la mise en équivalence, oubli du dividende ou de son élimination (`JUR-G03` pour la logique : la valeur d'équivalence repose sur les capitaux propres retraités).
- Écritures déséquilibrées ou sans libellé (`JUR-F03`, `JUR-F04`).

**Références normatives (1.5)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 19, 24, 32, 53 | Évaluation des PNC (option), impôts différés, goodwill, frais connexes en charges | [V] | F05 § 2 |
| IAS 12 § 66 | Impôts différés d'un regroupement affectant le goodwill | [V] | F05 § 2 |
| IFRS 10 § 22, B86 | PNC présentées dans les capitaux propres, élimination des titres et des opérations internes | [V] | F03 § 3, F04 R14, F05 § 3 |
| IAS 28 § 3, 10, 32 | Mise en équivalence, distributions, goodwill inclus dans la participation | [V] | F05 § 4 |
| ANC 2020-01 art. 231-2 | Frais inclus dans le coût d'acquisition, nets d'impôt (comparaison) | [V] | F05 § 1.1 |

---

### 1.6 Documents de synthèse (7 pts)

#### a. Extrait de l'état du résultat net et des autres éléments du résultat global de 2026 (3,5 pts)

**Résultat net consolidé (1,5 pt)**

| Élément | Montant |
|---|---:|
| Résultat net d'ARVELLE (comptes individuels) | 6 200 000 |
| Résultat net de LACUSTRA (comptes individuels) | 1 300 000 |
| Emprunt obligataire au coût amorti (O1) | + 5 607 |
| Frais d'acquisition des titres LACUSTRA en charges (F1) | – 252 000 |
| Coûts d'emprunt incorporés (C1) | + 90 000 |
| Amortissement de l'écart d'évaluation des constructions (L2) | – 60 000 |
| Élimination du dividende d'ALPAGE RÉSIDENCES (M1) | – 200 000 |
| Quote-part du résultat d'ALPAGE RÉSIDENCES (M2) | + 450 000 |
| Opérations internes (I1) ; dividende THERMALYS conservé | 0 |
| **Résultat net consolidé** | **7 533 607** |
| dont PNC : 30 % × 1 330 000 | 399 000 |
| dont part du groupe | **7 134 607** |

Contrôle de la part du groupe : 6 200 000 + 5 607 – 252 000 – 200 000 + 450 000 + 931 000 = 7 134 607.

**Extrait (2 pts)**

| Rubrique | 2026 |
|---|---:|
| Chiffre d'affaires (140 420 000 + 28 000 000 – 420 000) (0,25 pt) | 168 000 000 |
| … | |
| Quote-part dans le résultat des entreprises mises en équivalence (0,25 pt) | 450 000 |
| … | |
| **Résultat net** | **7 533 607** |
| *Éléments qui ne seront pas reclassés ultérieurement en résultat :* | |
| Variation de juste valeur des titres de capitaux propres à la juste valeur par les autres éléments du résultat global | 210 000 |
| Impôt sur les éléments qui ne seront pas reclassés | – 52 500 |
| *Éléments susceptibles d'être reclassés ultérieurement en résultat* | néant |
| **Autres éléments du résultat global, nets d'impôt** (0,5 pt) | **157 500** |
| **Résultat global** (0,25 pt) | **7 691 107** |
| Résultat net attribuable aux propriétaires de la société mère / aux PNC (0,5 pt) | 7 134 607 / 399 000 |
| Résultat global attribuable aux propriétaires de la société mère / aux PNC (0,25 pt) | 7 292 107 / 399 000 |

Les autres éléments du résultat global reviennent entièrement au groupe : les titres THERMALYS sont détenus par ARVELLE. Le résultat global attribuable aux PNC se limite à leur part du résultat de LACUSTRA. Le chiffre d'affaires consolidé retrouve les 168 M€ annoncés ; il ne comprend pas celui d'ALPAGE RÉSIDENCES, mise en équivalence.

#### b. Extrait du tableau des variations des capitaux propres de 2026 (2 pts)

| | Capital et primes | Réserves et résultats consolidés | Réserve de juste valeur | Total part du groupe | PNC | Total |
|---|---:|---:|---:|---:|---:|---:|
| Capitaux propres au 31/12/2025 (0,25 pt) | 26 000 000 | 31 887 500 | 112 500 | 58 000 000 | 0 | 58 000 000 |
| Résultat net (0,25 pt) | | 7 134 607 | | 7 134 607 | 399 000 | 7 533 607 |
| Autres éléments du résultat global (0,25 pt) | | | 157 500 | 157 500 | | 157 500 |
| **Résultat global** | | 7 134 607 | 157 500 | 7 292 107 | 399 000 | 7 691 107 |
| Dividendes versés (0,25 pt) | | – 2 000 000 | | – 2 000 000 | | – 2 000 000 |
| Acquisition de LACUSTRA (PNC à la juste valeur) (0,5 pt) | | | | | 3 450 000 | 3 450 000 |
| **Capitaux propres au 31/12/2026** (0,5 pt) | **26 000 000** | **37 022 107** | **270 000** | **63 292 107** | **3 849 000** | **67 141 107** |

La réserve de juste valeur (270 000 €) est celle de l'écriture T1 ; les PNC (3 849 000 €) sont celles de l'écriture L3. Le tableau relie les capitaux propres d'ouverture et de clôture en distinguant le résultat global des transactions avec les propriétaires (dividendes, PNC entrées avec LACUSTRA) [S, structure donnée par l'annexe 1.8, point 7].

#### c. Différences avec le règlement ANC n° 2020-01 (1,5 pt, 0,5 pt par thème)

- **ALPAGE RÉSIDENCES** : sous contrôle conjoint, elle serait intégrée proportionnellement [V ANC art. 211-4 et 221-1 ; F03 § 3] : 50 % de ses actifs, passifs, produits et charges (dont son chiffre d'affaires) seraient cumulés poste par poste, sans intérêts minoritaires, au lieu d'une ligne de titres mis en équivalence et d'une quote-part de résultat.
- **Acquisition de LACUSTRA** : les frais d'acquisition seraient inclus, nets d'impôt, dans le coût des titres et non en charges ; seul un écart d'acquisition « partiel » existe : 8 400 000 + 252 000 × 75 % – 7 000 000 = **1 589 000 €** [V art. 231-2 et 231-9 ; F05 § 1 et § 5]. Selon sa durée d'utilisation, il serait amorti (durée limitée) ou non ; ses dotations figureraient sur une ligne dédiée du résultat d'exploitation [V art. 231-11 et IR3 sous art. 231-12 ; F05 § 1.3].
- **Associés minoritaires de LACUSTRA** : les « intérêts minoritaires » seraient calculés sur l'actif net réévalué (3 000 000 € à l'acquisition), sans part de goodwill [V art. 232-1 ; F05 § 1.2 et § 5] ; l'IFRS parle de « participations ne donnant pas le contrôle » [V IFRS 10 § 22 ; F03 § 3].

Accepter toute autre différence de présentation exacte et justifiée, par exemple l'état du résultat net et des autres éléments du résultat global propre aux IFRS (point non couvert par les fiches : à valoriser sans être exigé).

**Erreurs fréquentes (1.6)**
- Résultat net consolidé obtenu en additionnant les résultats individuels sans retraitements, ou en y ajoutant le résultat d'ALPAGE RÉSIDENCES à 100 % ou à 50 % en plus de la quote-part.
- Autres éléments du résultat global de 2026 confondus avec le cumul (270 000 €), ou présentés parmi les éléments reclassables ; impôt omis.
- Autres éléments du résultat global partagés à 30 % avec les PNC, alors qu'ils concernent un titre détenu par ARVELLE.
- Acquisition de LACUSTRA présentée dans la colonne « part du groupe », ou PNC d'entrée portées à 3 000 000 € malgré le goodwill complet.

**Réponses tolérées (1.6)** : cohérence avec les résultats du candidat aux questions 1.2 à 1.5 (la méthode est notée, une erreur reportée n'est pénalisée qu'une fois) ; résultat global présenté avant la répartition entre groupe et PNC ; ligne « Résultat global » du tableau des variations omise si les deux lignes qui la composent sont justes.

**Références normatives (1.6)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 1 (état du résultat net et des autres éléments du résultat global, tableau des variations des capitaux propres) | Structure donnée par le manuel (annexe 1.8, points 6 et 7) ; IFRS 18 applicable aux exercices ouverts à compter du 01/01/2027 | [S] ; date d'application [V] | F05 § 5, F99 |
| ANC 2020-01 art. 211-4, 221-1 | Contrôle conjoint et intégration proportionnelle | [V] | F03 |
| ANC 2020-01 art. 231-2, 231-9, 231-11, IR3 sous 231-12, 232-1 | Coût d'acquisition, écart d'acquisition et présentation de ses dotations, intérêts minoritaires | [V] | F05 |
| IFRS 10 § 22 | Participations ne donnant pas le contrôle | [V] | F03 |
