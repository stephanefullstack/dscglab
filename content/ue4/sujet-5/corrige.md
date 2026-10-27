# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 5

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F13 (`ue4/fiches/`, à jour au 22 ou 23/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.6 | `exercices/ex10_consolidation_ifrs_instruments` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.6 | `exercices/ex11_scission` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.9 | `exercices/ex12_audit_ventes_ec_vsme` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

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

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, référentiel, régime fiscal, date d'effet | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable ; `1.1.b` Régime fiscal de droit commun et régime de faveur | 5 |
| 2.2 Actions émises et répartition du capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 4 |
| 2.3 Mode d'évaluation et valeur des apports | `1.2.c` Déterminer le mode de valorisation des apports ; `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 5 |
| 2.4 Écritures chez VOGALAC | `1.3.a` Écritures de base chez la bénéficiaire ; `1.3.c` Écritures complémentaires (régime fiscal, frais) | 4 |
| 2.5 Écritures chez PRAZALPE, résultat de BELLECOMBE | `1.3.a` Écritures de base chez la bénéficiaire ; `1.3.c` Annulation des opérations réciproques ; `1.1.b` Traitement fiscal des plus-values | 4 |
| 2.6 Capitaux propres et commentaire | `1.4.a` Restituer au dirigeant les impacts de l'opération | 3 |
| **Total** | | **25** |

---

### 2.1 Qualification, référentiel, régime fiscal et date d'effet (5 pts)

**Qualification et modalités (1 pt).** L'opération est une **scission** : BELLECOMBE transmet l'ensemble de son patrimoine à plusieurs sociétés, ici deux sociétés existantes, PRAZALPE et VOGALAC [V PCG art. 710-2 ; C. com. L. 236-18, F01 § 1]. Il s'agit d'une **transmission universelle** : chaque bénéficiaire reçoit tous les actifs et toutes les dettes de la branche qui lui est attribuée, y compris la dette envers PRAZALPE et les arrhes des clients. BELLECOMBE est **dissoute sans liquidation**. Ses actionnaires reçoivent directement des actions émises par chaque bénéficiaire, par augmentation de capital, en échange de leurs actions BELLECOMBE, qui disparaissent. La scission est **totale** : BELLECOMBE ne conserve aucune activité.

**Distinction avec deux apports partiels d'actif suivis d'une liquidation (0,75 pt).** Dans un apport partiel d'actif, c'est la société apporteuse qui reçoit les titres de la bénéficiaire et qui continue d'exister [V PCG art. 710-2, F01 § 1]. Avec deux apports, BELLECOMBE deviendrait une société détenant des actions PRAZALPE et VOGALAC. Pour que ses actionnaires les reçoivent, il faudrait ensuite la dissoudre et la liquider, puis partager l'actif entre eux. La scission réalise en une seule opération la transmission des branches et l'attribution des actions, sans phase de liquidation.

**Référentiel (0,5 pt).** Il s'agit d'une restructuration, non d'une acquisition de titres : les bénéficiaires reçoivent un patrimoine et le rémunèrent par leurs propres actions. Son enregistrement chez PRAZALPE et VOGALAC relève du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié, comptes individuels), qui fixe les valeurs d'inscription des apports [V art. 710-1 et 720-1, F01 § 1]. Ces règles ne servent pas au calcul du nombre d'actions, qui repose sur les valeurs d'échange [V art. 740-1, F01 § 1].

**Régime de faveur : conditions et appréciation (1 pt)**
- *Conditions (0,5 pt).* Les trois sociétés sont passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1]. La scission bénéficie **de plein droit** du régime de l'art. 210 A si la société scindée comporte **au moins deux branches complètes d'activité** et si chaque bénéficiaire reçoit une ou plusieurs de ces branches [V CGI art. 210 B-1, F02 § 1]. Depuis le 01/01/2018, ce régime n'est plus subordonné à un engagement de conservation des titres reçus ; cet engagement ne subsiste que pour la scission soumise à agrément, faute de branches complètes [V BOI-IS-FUS-20-30-10 § 70 ; CGI art. 210 B-3, F02 § 1 et corrections du 22/10/2026]. La branche complète est l'ensemble des actifs et passifs d'une division qui constituent une exploitation autonome, capable de fonctionner par ses propres moyens [V BOI-IS-FUS-20-20 § 10, F02 § 1].
- *Appréciation (0,5 pt).* Les deux conditions sont remplies. Le camping et la base nautique sont deux activités réellement exercées, organisées en divisions distinctes avec leurs installations, leur personnel, leur clientèle et leur site de réservation. Chacune est transmise avec l'ensemble de ses actifs et de ses dettes, et non en éléments isolés. Les services administratifs communs ne font pas obstacle à l'autonomie : ils sont rattachés à chaque branche pour leur quote-part, et les deux salariés qui les assurent se répartissent entre les bénéficiaires [V BOI-IS-FUS-20-20 § 50 à 90, F02 § 1]. Chaque bénéficiaire reçoit une branche complète.

**Effets du régime de faveur (1 pt)**
- *Chez BELLECOMBE (0,25 pt).* La plus-value dégagée sur les éléments transmis (2 270 000 € sur la branche camping, voir 2.5 b) n'est pas imposée [V CGI art. 210 A-1, F02 § 2]. Les amortissements dérogatoires (48 000 €) ne sont pas réintégrés, puisqu'ils sont reconstitués chez VOGALAC [V BOI-IS-FUS-30-20 § 10, F02 § 2], et le solde de la subvention (96 000 €) n'est pas imposé chez BELLECOMBE, VOGALAC ayant opté pour en reprendre l'imposition [V BOI-IS-FUS-10-20-40-10 § 180, F01 § 8]. BELLECOMBE n'a pas de déficit reportable.
- *Chez PRAZALPE (0,5 pt).* Engagements de l'art. 210 A-3 [V F02 § 4] : les plus-values futures sur les éléments non amortissables seront calculées d'après leur valeur fiscale chez BELLECOMBE (terrain 900 000 €, fonds commercial 0), ce qui place en sursis 1 200 000 € sur le terrain et 695 000 € sur le fonds commercial ; les plus-values sur biens amortissables sont réintégrées par parts égales, sur **15 ans** pour les constructions (400 000 / 15 = 26 667 € par an) et sur **5 ans** pour les mobil-homes (160 000 / 5 = 32 000 € par an), les amortissements étant calculés sur la valeur d'apport. La plus-value sur constructions représente 71,43 % de la plus-value nette sur biens amortissables (400 000 / 560 000), en deçà du seuil de 90 % : la durée de 15 ans s'applique [V CGI art. 210 A-3-c et d ; BOI-IS-FUS-10-20-40-20 § 100, F02 § 2]. Ces impositions futures justifient l'impôt différé intégré à l'apport (voir 2.3 b).
- *Chez VOGALAC (0,25 pt).* Apport à la valeur comptable (voir 2.3) : VOGALAC reprend les valeurs fiscales de BELLECOMBE. Elle reprend les amortissements dérogatoires reconstitués dans les mêmes conditions que BELLECOMBE et réintègre le solde de la subvention (96 000 €) selon le plan d'amortissement des bateaux électriques [V BOI-IS-FUS-30-20 § 10, F02 § 2 ; BOI-IS-FUS-10-20-40-10 § 180, F01 § 8].

**Enjeux fiscaux de la date d'effet au 1er janvier 2027 (0,75 pt)**
- *Validité (0,25 pt).* La date d'effet n'est pas antérieure à l'ouverture de l'exercice en cours des trois sociétés (01/01/2027) : elle est opposable à l'administration [V CE, 13/09/2021, n° 451564, SAS Adis ; BOI-IS-FUS-40-10-20 § 40 et 50, F02 § 5]. Elle respecte aussi le droit des sociétés : elle n'est ni antérieure à la clôture du dernier exercice de BELLECOMBE (31/12/2026), ni postérieure à la clôture de l'exercice en cours des bénéficiaires (31/12/2027) [V C. com. L. 236-4, 2°, F02 § 5].
- *Effets (0,5 pt).* Fiscalement, PRAZALPE et VOGALAC se substituent à BELLECOMBE pour les activités reçues à compter du 01/01/2027 [V BOI-IS-FUS-40-10-20 § 10, F02 § 5]. Les résultats des deux branches du 1er janvier au 30 avril 2027 sont compris dans les résultats imposables 2027 de PRAZALPE et de VOGALAC, et non dans ceux de BELLECOMBE. Or les deux sites sont fermés pendant cette période : les **pertes** de cette saison creuse (entretien, salaires des permanents) seront déduites par les bénéficiaires, ce qui réduit leur impôt 2027 (économie de 25 % des pertes). Sans cette date d'effet, ces pertes resteraient dans le dernier résultat de BELLECOMBE ; un déficit éventuel ne passerait aux bénéficiaires que sur agrément, la dispense d'agrément ne s'appliquant pas aux scissions [V CGI art. 209 II, F02 § 3]. Les opérations faites entre BELLECOMBE et PRAZALPE pendant ces quatre mois se neutralisent chez PRAZALPE (enjeux relevés par F02 § 5).

---

### 2.2 Actions émises et répartition du capital (4 pts)

**Valeurs unitaires (0,5 pt).** PRAZALPE : 20 400 000 / 170 000 = **120 €** ; VOGALAC : 400 000 / 2 000 = **200 €**. Valeur d'une action BELLECOMBE : (3 600 000 + 1 200 000) / 20 000 = 240 €, dont 180 € pour la branche camping et 60 € pour la branche nautique.

**Actions émises par PRAZALPE (0,75 pt).** Dans une scission, le nombre d'actions à émettre se calcule directement à partir de la valeur d'échange de l'apport [S guide p. imprimée 163, d'après `programme/perimetre_ue4.yaml`, compétence 1.2.a] : 3 600 000 / 120 = **30 000 actions** ; augmentation de capital 30 000 × 10 = **300 000 €**.

**Actions émises par VOGALAC (0,75 pt).** 1 200 000 / 200 = **6 000 actions** ; augmentation de capital 6 000 × 25 = **150 000 €**.

**Attribution aux actionnaires de BELLECOMBE (0,5 pt).** Les 20 000 actions BELLECOMBE sont toutes échangées : 30 000 / 20 000 = **3 actions PRAZALPE pour 2 actions BELLECOMBE** et 6 000 / 20 000 = **3 actions VOGALAC pour 10 actions BELLECOMBE**. Pour 10 actions BELLECOMBE, un actionnaire reçoit **15 actions PRAZALPE et 3 actions VOGALAC**. Chaque actionnaire détenant un multiple de 10 actions, il n'y a pas de rompus. Valeurs échangées : 15 × 120 + 3 × 200 = 2 400 € = 10 × 240 € ; l'échange se fait sans soulte.

**Répartition du capital de PRAZALPE (0,75 pt)** — 170 000 + 30 000 = 200 000 actions :

| Actionnaire | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| ORÉADE HOLDING | 136 000 | 80,00 % | 136 000 | 68,00 % |
| Autres actionnaires de PRAZALPE | 34 000 | 20,00 % | 34 000 | 17,00 % |
| GAVARD PARTICIPATIONS (15 000 × 3 / 2) | – | – | 22 500 | 11,25 % |
| Actionnaires individuels de BELLECOMBE (5 000 × 3 / 2) | – | – | 7 500 | 3,75 % |
| **Total** | **170 000** | **100 %** | **200 000** | **100 %** |

**Répartition du capital de VOGALAC (0,75 pt)** — 2 000 + 6 000 = 8 000 actions :

| Actionnaire | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| ONDINE PARTICIPATIONS | 1 400 | 70,00 % | 1 400 | 17,50 % |
| Salariés de VOGALAC | 600 | 30,00 % | 600 | 7,50 % |
| GAVARD PARTICIPATIONS (15 000 × 3 / 10) | – | – | 4 500 | 56,25 % |
| Actionnaires individuels de BELLECOMBE (5 000 × 3 / 10) | – | – | 1 500 | 18,75 % |
| **Total** | **2 000** | **100 %** | **8 000** | **100 %** |

Chaque action donnant une voix, les droits de vote suivent la même répartition.

---

### 2.3 Mode d'évaluation et valeur des apports (5 pts)

**a) Mode d'évaluation de chaque apport (1,75 pt)**

Chaque branche est rémunérée par une société différente, dont l'actionnariat évolue différemment : la situation de contrôle et le sens de l'opération s'analysent donc pour chacun des deux apports.

- *Situation de contrôle (0,5 pt).* BELLECOMBE est contrôlée de manière exclusive par GAVARD PARTICIPATIONS (75 % des droits de vote), PRAZALPE par ORÉADE HOLDING (80 %) et VOGALAC par ONDINE PARTICIPATIONS (70 %). Aucune des trois sociétés ne détient d'actions d'une autre, et les trois holdings n'ont aucun lien en capital : il n'y a ni contrôle de l'une par l'autre, ni mère commune. Les deux apports sont réalisés **sous contrôle distinct** [V PCG art. 741-1 et 741-2, F01 § 2.1]. Aucun pacte ne crée de contrôle partagé, avant comme après l'opération.
- *Apport de la branche camping à PRAZALPE (0,5 pt).* Après l'opération, ORÉADE HOLDING détient 68 % de PRAZALPE : l'actionnaire principal de la bénéficiaire, bien que dilué, **conserve le contrôle** ; GAVARD PARTICIPATIONS perd le contrôle de la branche camping et ne détient que 11,25 % de PRAZALPE. L'apport est **à l'endroit** ; PRAZALPE est l'initiatrice, la branche camping la cible [V art. 742-1, F01 § 2.2]. Contrôle distinct et opération à l'endroit : **valeur réelle** [V art. 743-1, cas 4, F01 § 2.3].
- *Apport de la branche nautique à VOGALAC (0,5 pt).* Après l'opération, GAVARD PARTICIPATIONS, actionnaire principal de BELLECOMBE, détient 56,25 % de VOGALAC et en **prend le contrôle** ; ONDINE PARTICIPATIONS tombe de 70 % à 17,5 %. L'apport est **à l'envers** : la cible est VOGALAC, l'initiatrice BELLECOMBE ou sa mère [V art. 742-2, F01 § 2.2]. Contrôle distinct et opération à l'envers : **valeur comptable** [V art. 743-1, cas 3, F01 § 2.3]. Les actifs qui changent de contrôle sont ceux de VOGALAC, qui ne figurent pas dans le traité ; ceux de la branche nautique restent sous le contrôle de la famille GAVARD et ne sont pas réévalués.
- *Exception (0,25 pt).* La valeur comptable s'impose sauf si l'actif net comptable apporté ne permet pas la libération du capital [V art. 743-3, F01 § 2.4] : la vérification est faite en c).

**b) Valeur réelle de la branche camping (2,25 pts)**

*Éléments identifiés figurant au bilan (0,75 pt)*

| Élément | Valeur nette comptable | Valeur réelle | Écart |
|---|---:|---:|---:|
| Terrain | 900 000 | 2 100 000 | + 1 200 000 |
| Constructions | 1 200 000 | 1 600 000 | + 400 000 |
| Mobil-homes | 800 000 | 960 000 | + 160 000 |
| Stocks de marchandises | 40 000 | 40 000 | 0 |
| Disponibilités | 150 000 | 150 000 | 0 |
| **Actifs identifiés** | **3 090 000** | **4 850 000** | **+ 1 760 000** |
| Dettes (1 400 000 + 120 000 + 110 000 + 90 000 + 40 000) | 1 760 000 | 1 760 000 | 0 |

*Élément identifié ne figurant pas au bilan (0,25 pt).* En valeur réelle, l'apport comprend les éléments identifiés figurant ou non au bilan de la société qui transmet, dont les provisions pour retraites et les impôts différés [V art. 744-1, F01 § 3.1] : engagements de retraite de **60 000 €**.

*Impôt différé intégré à l'apport (1 pt).* Le régime de faveur reporte chez PRAZALPE l'imposition des plus-values sur biens amortissables : l'écart entre leur valeur d'apport et leur valeur fiscale est une différence temporaire [V corrigé du sujet zéro, Q 2.4, F01 § 3.3 ; F02 § 6].

| Élément | Base | Impôt différé (25 %) |
|---|---:|---:|
| Plus-value sur constructions | + 400 000 | + 100 000 |
| Plus-value sur mobil-homes | + 160 000 | + 40 000 |
| Engagements de retraite (déductibles au versement) | – 60 000 | – 15 000 |
| **Total net : passif d'impôt différé** | **+ 500 000** | **+ 125 000** |

Pas d'impôt différé sur le terrain (hypothèse de l'annexe 2.3 : non amortissable, aucune cession envisagée), ni sur le fonds commercial, élément résiduel [V F01 § 3.3]. Le solde net (125 000 €) est inscrit en **provision pour impôts (compte 1523)**.

*Actif net identifié et fonds commercial (0,25 pt)*

| | Montant |
|---|---:|
| Actifs identifiés | 4 850 000 |
| – Dettes | – 1 760 000 |
| – Engagements de retraite | – 60 000 |
| – Provision pour impôts (impôt différé net) | – 125 000 |
| **Actif net réel identifié** | **2 905 000** |

Fonds commercial = valeur réelle globale – actif net identifié = 3 600 000 – 2 905 000 = **695 000 €**, inscrit au traité sur la ligne « fonds commercial » et repris au compte 207 [V art. 744-1, F01 § 3.1]. Contrôle : 1 330 000 (actif net comptable) + 1 760 000 – 60 000 – 125 000 = 2 905 000 €.

**c) Valeur de l'apport de la branche nautique et primes (1 pt)**

*Valeur comptable (0,5 pt).* Valeur des éléments dans les comptes de BELLECOMBE à la date d'effet [V art. 744-2, F01 § 3.2] : constructions 350 000 + bateaux 400 000 + disponibilités 50 000 – emprunt 300 000 – fournisseurs 20 000 – dettes sociales 10 000 = **470 000 €**. Ce montant comprend la subvention d'investissement nette (96 000 €) et les amortissements dérogatoires (48 000 €), qui sont des capitaux propres de BELLECOMBE et non des dettes [V F01 § 8]. Il couvre largement l'augmentation de capital de VOGALAC (150 000 €) : la libération du capital est possible et l'exception de l'art. 743-3 ne joue pas.

*Primes de scission (0,5 pt).* PRAZALPE : 3 600 000 – 300 000 = **3 300 000 €**. VOGALAC : 470 000 – 150 000 = **320 000 €**, avant les imputations de la question 2.4. Le nombre d'actions de VOGALAC est fixé sur la valeur d'échange (1 200 000 €), mais l'apport est comptabilisé à la valeur comptable (470 000 €) : la valeur réelle sert à rémunérer, la valeur comptable à enregistrer.

---

### 2.4 Écritures chez VOGALAC au 30 avril 2027 (4 pts)

Les écritures complètes figurent dans `corrige.yaml` (V1 à V5) ; elles sont équilibrées (contrôle `ue4check`). Schéma type : `gabarits/ecritures_types/01_fusion_valeur_comptable.yaml`. Les écritures sont passées à la date de réalisation, pour les éléments au 1er janvier 2027 (annexe 2.1).

**V1 — Augmentation de capital (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 470 000 | |
| 101 Capital (6 000 × 25) | | 150 000 |
| 1042 Primes de fusion (prime de scission) | | 320 000 |

**V2 — Réalisation des apports à la valeur comptable (1,25 pt).** En valeur comptable, la bénéficiaire reprend les **valeurs brutes et les amortissements** de la société qui transmet [V BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2].

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments (club-house, hangar) | 600 000 | |
| 2182 Matériel de transport (flotte de bateaux) | 900 000 | |
| 512 Banques | 50 000 | |
| 28131 Amortissements des bâtiments | | 250 000 |
| 28182 Amortissements du matériel de transport | | 500 000 |
| 164 Emprunts bancaires | | 300 000 |
| 401 Fournisseurs | | 20 000 |
| 431 Sécurité sociale (dettes sociales) | | 10 000 |
| 4561 Associés – Comptes d'apport en société | | 470 000 |

**V3 — Reconstitution des amortissements dérogatoires (0,5 pt).** Engagement pris dans le traité : ces provisions réglementées, comprises dans l'actif net apporté, sont reconstituées par prélèvement sur la prime [V CGI art. 210 A-3-a ; BOI-IS-FUS-30-20 § 10 ; corrigé du sujet zéro, Q 2.6, F01 § 8].

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (prime de scission) | 48 000 | |
| 145 Amortissements dérogatoires | | 48 000 |

**V4 — Reconstitution de la subvention d'investissement (0,75 pt).** VOGALAC a opté dans le traité pour reprendre l'imposition du solde de la subvention : elle la reconstitue à son bilan par prélèvement sur la prime [V BOI-IS-FUS-10-20-40-10 § 180, F01 § 8 ; écriture : convention de rédaction, F01 § 8]. Par cohérence avec la reprise des valeurs brutes et des amortissements, la subvention est reconstituée pour son montant initial, diminué des sommes déjà virées au résultat.

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (160 000 – 64 000) | 96 000 | |
| 139 Subventions d'investissement inscrites au compte de résultat | 64 000 | |
| 131 Subventions d'investissement octroyées | | 160 000 |

VOGALAC continuera de virer la subvention au résultat (débit 139, crédit 747) au rythme de l'amortissement des bateaux électriques.

**V5 — Frais de scission (0,75 pt).** Les frais de fusion et de scission peuvent être imputés sur la prime [V PCG art. 212-9, F01 § 7], pour leur montant net d'impôt [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 24 000 × 75 % = **18 000 €**. L'économie d'impôt (6 000 €) diminue la dette d'impôt sur les sociétés 2027.

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (24 000 × 75 %) | 18 000 | |
| 444 État – Impôts sur les bénéfices (24 000 × 25 %) | 6 000 | |
| 512 Banques | | 24 000 |

Prime de scission restante : 320 000 – 48 000 – 96 000 – 18 000 = **158 000 €**.

---

### 2.5 Écritures chez PRAZALPE au 30 avril 2027 et résultat de BELLECOMBE (4 pts)

**a) Chez PRAZALPE (2,75 pts).** Schéma type : `gabarits/ecritures_types/02_fusion_valeur_reelle.yaml`.

**P1 — Augmentation de capital (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 3 600 000 | |
| 101 Capital (30 000 × 10) | | 300 000 |
| 1042 Primes de fusion (prime de scission) | | 3 300 000 |

**P2 — Réalisation des apports à la valeur réelle (1,5 pt).** Les éléments sont inscrits à leur valeur réelle, sans reprise des amortissements de BELLECOMBE ; les engagements de retraite, l'impôt différé et le fonds commercial sont inscrits [V art. 744-1, F01 § 3.1 et § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 207 Fonds commercial | 695 000 | |
| 211 Terrains | 2 100 000 | |
| 2131 Bâtiments | 1 600 000 | |
| 218 Autres immobilisations corporelles (mobil-homes) | 960 000 | |
| 37 Stocks de marchandises | 40 000 | |
| 512 Banques | 150 000 | |
| 1521 Provisions pour pensions et obligations similaires | | 60 000 |
| 1523 Provisions pour impôts | | 125 000 |
| 164 Emprunts bancaires | | 1 400 000 |
| 404 Fournisseurs d'immobilisations (dette envers PRAZALPE) | | 120 000 |
| 401 Fournisseurs | | 110 000 |
| 4191 Clients – Avances et acomptes reçus (arrhes) | | 90 000 |
| 431 Sécurité sociale (dettes sociales) | | 40 000 |
| 4561 Associés – Comptes d'apport en société | | 3 600 000 |

**P3 — Créance réciproque (0,75 pt).** Par l'apport, PRAZALPE reçoit la dette de 120 000 € que BELLECOMBE avait envers elle : elle devient à la fois créancière et débitrice de la même obligation. La dette et la créance s'éteignent par **confusion** [V C. civ. art. 1349, F01 § 8]. Il s'agit d'une opération réciproque existant à la date d'effet, et non d'une opération de la saison creuse 2027.

| Compte | Débit | Crédit |
|---|---:|---:|
| 404 Fournisseurs d'immobilisations (dette reçue de BELLECOMBE) | 120 000 | |
| 462 Créances sur cessions d'immobilisations | | 120 000 |

**b) Résultat dégagé par BELLECOMBE et traitement fiscal (1,25 pt)**

*Résultat par branche (0,75 pt).* BELLECOMBE transmet chaque branche pour la valeur de l'apport retenue au traité. Le résultat est l'écart entre cette valeur et l'actif net comptable de la branche (annexe 2.2) :

| Branche | Valeur de l'apport au traité | Actif net comptable | Résultat |
|---|---:|---:|---:|
| Camping (valeur réelle) | 3 600 000 | 1 330 000 | **+ 2 270 000** |
| Base nautique (valeur comptable) | 470 000 | 470 000 | **0** |

La branche camping dégage une plus-value de scission de 2 270 000 € (0,5 pt) : plus-values sur le terrain (1 200 000), les constructions (400 000) et les mobil-homes (160 000), fonds commercial (695 000), diminués des engagements de retraite (60 000) et de l'impôt différé (125 000) inscrits dans l'apport. La branche nautique, transmise à sa valeur comptable, ne dégage aucun résultat (0,25 pt).

*Traitement fiscal (0,5 pt).* Sous le régime de faveur, les plus-values nettes et profits dégagés par BELLECOMBE sur les éléments transmis **ne sont pas soumis à l'impôt sur les sociétés** [V CGI art. 210 A-1, F02 § 2]. L'imposition est reportée chez PRAZALPE : sursis pour le terrain et le fonds commercial, réintégration étalée des plus-values sur biens amortissables (voir 2.1). Sous le régime de droit commun, la scission serait assimilée à une cessation d'entreprise et les plus-values seraient imposées immédiatement chez BELLECOMBE [V BOI-IS-FUS-10-10-10 § 1, F02 § 2].

---

### 2.6 Capitaux propres des bénéficiaires et commentaire (3 pts)

**Capitaux propres de PRAZALPE (0,75 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (200 000 actions × 10) | 1 700 000 | + 300 000 | 2 000 000 |
| Primes d'émission | 800 000 | | 800 000 |
| Prime de scission | 0 | + 3 300 000 | 3 300 000 |
| Réserve légale | 170 000 | | 170 000 |
| Autres réserves | 6 330 000 | | 6 330 000 |
| **Total** | **9 000 000** | **+ 3 600 000** | **12 600 000** |

**Capitaux propres de VOGALAC (1 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (8 000 actions × 25) | 50 000 | + 150 000 | 200 000 |
| Prime de scission | 0 | + 320 000 – 48 000 – 96 000 – 18 000 | 158 000 |
| Réserve légale | 5 000 | | 5 000 |
| Autres réserves | 205 000 | | 205 000 |
| Subvention d'investissement (160 000 – 64 000) | 0 | + 96 000 | 96 000 |
| Amortissements dérogatoires | 0 | + 48 000 | 48 000 |
| **Total** | **260 000** | **+ 452 000** | **712 000** |

Contrôle : + 452 000 = apport à la valeur comptable (470 000) – frais nets d'impôt (18 000). Les reconstitutions déplacent 144 000 € de la prime vers la subvention et les provisions réglementées sans modifier le total.

**Commentaire pour M. GAVARD (1,25 pt, grille de niveaux)**

| Niveau | 0 | 0,5 | 1 | 1,25 |
|---|---|---|---|---|
| Attendu | Absence ou idées sans lien avec le cas | Une idée pertinente, pour les actionnaires ou pour les créanciers | Au moins une idée pour chacun | Idées pour chacun, chiffrées et reliées au contrôle |

Idées attendues :
- *Actionnaires de BELLECOMBE.* L'échange est équitable : 10 actions BELLECOMBE (2 400 €) donnent 15 actions PRAZALPE et 3 actions VOGALAC de même valeur totale. GAVARD PARTICIPATIONS atteint l'objectif de la famille : elle **prend le contrôle de VOGALAC** (56,25 %) et conserve, par 11,25 % de PRAZALPE (22 500 actions, 2 700 000 € en valeur d'échange), un intérêt dans le camping, mais sans en garder la direction. Les actionnaires individuels deviennent minoritaires dans deux sociétés non cotées (3,75 % et 18,75 %) : leurs droits de vote pèsent peu, la liquidité de leurs actions est réduite et leurs dividendes dépendront de politiques fixées par ORÉADE HOLDING et par GAVARD PARTICIPATIONS.
- *Créanciers de BELLECOMBE.* Approche financière (les garanties légales des créanciers ne sont pas à traiter, annexe 2.1). Les dettes du camping (1 640 000 € après extinction de la dette envers PRAZALPE) sont reprises au passif de PRAZALPE, dont les capitaux propres atteignent 12,6 M€ : la surface financière du débiteur augmente, même si l'actif comprend un fonds commercial de 695 000 €, non amorti car présumé à durée d'utilisation non limitée [V art. 214-3, F01 § 5.5] et donc exposé à une dépréciation, et une provision pour impôts de 125 000 €. Les dettes de la base nautique (330 000 €) sont reprises par VOGALAC, dont les capitaux propres restent modestes (712 000 €) et la trésorerie est amputée des frais de scission : le remboursement repose surtout sur les flux de la base nautique et sur ses actifs (bateaux, club-house). Les arrhes versées par les clients du camping (90 000 €) figurent au passif de PRAZALPE, qui assurera les séjours.

---

### Réponses tolérées
- **Compte de la prime** : 1043 Primes d'apport au lieu de 1042 Primes de fusion, ou un sous-compte « prime de scission » de l'un ou l'autre.
- **Subvention d'investissement (V4)** : reconstitution pour le seul montant net (débit 1042, crédit 131 pour 96 000 €), si le solde à réintégrer est correctement indiqué.
- **Frais de scission** : présentation en deux écritures (1042 / 512 pour 24 000 €, puis 444 / 1042 pour 6 000 €).
- **Impôts différés** : présentation séparée des impôts différés passifs (140 000 €, base 560 000 €) et actifs (15 000 €, base 60 000 €), si le solde net de 125 000 € est retenu dans l'apport.
- **Créance réciproque (P3)** : présentation de l'extinction dans l'écriture P2 (dette envers PRAZALPE non reprise au passif, créance 462 soldée au crédit de P2), si le raisonnement est explicite.
- **Résultat de BELLECOMBE (2.5 b)** : calcul par les éléments (plus-values identifiées et fonds commercial, moins retraites et impôt différé) au lieu de la différence globale, s'il aboutit à 2 270 000 €.
- **Créanciers (2.6)** : la mention des garanties légales des créanciers n'est pas exigée ; elle n'est pas pénalisée si elle est exacte.
- **2.2** : calcul par la parité (180 / 120 = 3 / 2 ; 60 / 200 = 3 / 10, puis 20 000 × 3 / 2 et 20 000 × 3 / 10).
- **2.6** : la logique du candidat prévaut lorsque ses montants découlent d'une erreur antérieure correctement reportée [`JUR-F08`].

### Erreurs fréquentes
- `JUR-R05` Retenir la **valeur réelle pour les deux apports** au motif que les sociétés sont sous contrôle distinct, sans analyser le sens de chaque apport ; ou retenir un seul mode d'évaluation pour toute la scission. C'est le piège principal du dossier (cas 3 du tableau de l'art. 743-1 pour VOGALAC).
- `JUR-R01` Calculer la prime de VOGALAC sur la valeur d'échange (1 200 000 – 150 000 = 1 050 000 €) alors que l'apport est comptabilisé à la valeur comptable ; oublier de diminuer la prime des reconstitutions et des frais (prime finale de 158 000 €).
- `JUR-R03` Oublier la reconstitution des amortissements dérogatoires, ou les porter au passif dans l'écriture V2 en réduisant l'apport.
- `JUR-F04` Absence de contrôle d'équilibre des écritures V2 et P2.
- Erreurs propres à ce cas :
  - calcul du nombre d'actions sur la valeur comptable de la branche nautique (470 000 / 200 = 2 350 actions) : le nombre d'actions se fixe sur les valeurs d'échange ;
  - nombre d'actions rapporté à la valeur globale de BELLECOMBE (4 800 000 €) pour chaque bénéficiaire ;
  - impôt différé calculé sur le terrain ou sur le fonds commercial, ou provision pour retraite omise ;
  - créance et dette réciproques laissées au bilan de PRAZALPE ;
  - affirmation d'un engagement de conservation des titres pendant trois ans comme condition du régime de faveur de la scission : il n'existe plus depuis 2018 pour une scission portant sur des branches complètes ;
  - inscription des éléments de la branche nautique pour leur valeur nette chez VOGALAC, sans reprise des valeurs brutes et des amortissements.

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Expert-comptable et commissaire aux comptes ; demande du gérant | `3.1.a` Cadres d'exercice des EC, des CAC et des auditeurs de durabilité ; `3.1.b` Nomination et cessation ; `3.1.c` Principes déontologiques | 4 |
| 3.2 Désignation obligatoire et durée du mandat ; lien personnel d'un collaborateur | `3.1.b` Nomination et cessation ; `3.1.c` Principes déontologiques | 3 |
| 3.3 Responsabilités de l'expert-comptable | `3.1.e` Mise en cause de la responsabilité | 2 |
| 3.4 Cycle ventes et trésorerie : risques, assertions, procédures | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit | 3 |
| 3.5 Procédure analytique ; lettre de mission, programme et feuille de travail | `3.2.d` Démarche d'audit (techniques et supports) | 3 |
| 3.6 Opinion | `3.2.e` Portée des opinions | 3 |
| 3.7 Acteurs, normes, interopérabilité ; VSME ou ESRS | `3.3.a` Architecture et champ du reporting de durabilité | 5 |
| 3.8 IRO, double matérialité, connectivité | `3.3.b` Principes de construction du reporting | 4 |
| 3.9 Qui délivre l'assurance ; assurance limitée et raisonnable | `3.4.a` Objectifs de la mission d'audit de durabilité ; `3.1.a` Cadre d'exercice de l'auditeur de durabilité ; `3.1.c` Principes déontologiques (autorévision) | 3 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes annuels (18 points)

### 3.1 Expert-comptable et commissaire aux comptes ; demande du gérant (4 pts)

**Cadre d'exercice de l'expert-comptable (1,5 pt)**
- **Conditions d'exercice (0,5 pt)** : nul ne peut porter le titre d'expert-comptable ni exercer la profession s'il n'est **inscrit au tableau de l'ordre** [V ord. art. 3 I]. L'inscription suppose notamment le **diplôme d'expertise comptable**, la jouissance des droits civils, l'absence de condamnation entachant l'honorabilité et des garanties de moralité [V ord. art. 3 II]. L'expert-comptable prête serment dans les six mois de son inscription [V décret art. 143]. L'exercice illégal et l'usage abusif du titre sont des délits [V ord. art. 20].
- **Instances (0,5 pt)** :
  - l'ordre, qui assure la défense de l'honneur et de l'indépendance de la profession, a à sa tête le **Conseil national (CNOEC)** ; celui-ci peut exercer les droits de la partie civile pour les faits portant atteinte à l'intérêt collectif de la profession [V ord. art. 1, 33, 37] ;
  - les **conseils régionaux (CROEC)** tiennent le tableau, statuent sur les inscriptions, surveillent l'exercice de la profession dans leur circonscription et concilient les différends [V ord. art. 28, 31, 40].
- **Mission (0,5 pt)** : la mission de l'expert-comptable est **contractuelle**. Il tient, centralise, arrête et révise les comptabilités, et peut établir les comptes annuels [V ord. art. 2]. Il passe avec son client un **contrat écrit**, qui peut prendre la forme d'une **lettre de mission**, définissant la mission et les droits et obligations de chaque partie [V décret art. 151]. Les honoraires sont convenus par écrit avant la mission [V ord. art. 24]. Il n'existe pas de durée légale : la durée relève du contrat [V décret art. 151 al. 3]. Avant d'accepter, l'expert-comptable apprécie s'il peut exercer la mission conformément aux règles professionnelles [V décret art. 150].

**Cadre d'exercice du commissaire aux comptes (1 pt)**
- **Conditions d'exercice (0,5 pt)** : inscription sur la **liste tenue par la H2A** [V C. com. L. 821-13 I]. Pour une personne physique : honorabilité, **stage professionnel de trois ans**, **certificat d'aptitude aux fonctions de commissaire aux comptes ou diplôme d'expertise comptable** [V L. 821-14 ; R. 821-46]. Une société de commissaires aux comptes, comme CORVANE, doit être détenue et dirigée majoritairement par des commissaires aux comptes [V L. 821-16]. Serment devant la cour d'appel [V L. 821-23].
- **Instances et mission (0,5 pt)** :
  - la **H2A**, autorité publique indépendante, inscrit les commissaires aux comptes, adopte les normes, contrôle et sanctionne [V L. 820-1] ;
  - la **CNCC** représente la profession auprès des pouvoirs publics ; les **CRCC**, une par ressort de cour d'appel, sont les compagnies régionales auxquelles les commissaires aux comptes sont rattachés [V L. 821-12 ; R. 821-44].
  - La certification est une **mission légale** : le commissaire aux comptes est désigné par l'**assemblée générale ordinaire** pour **six exercices** [V L. 821-40 I, L. 821-44]. La lettre de mission, établie la première année du mandat, en précise les modalités [V NEP lettre de mission § 3] ; elle ne fonde pas la mission, qui résulte de la loi et de la désignation [S].

**Analyse de la demande du gérant (1 pt)**
- **Deux indépendances différentes** : l'indépendance du commissaire aux comptes est une **condition légale** de sa mission, appréciée **en réalité et en apparence** [V L. 821-27, L. 821-31 ; code de déontologie art. 5]. Celle de l'expert-comptable est une **indépendance d'esprit** vis-à-vis de son client : elle est compatible avec la tenue de ses comptes, qui est l'objet même de sa mission [V décret art. 145-146 ; F10 § 3].
- **Autorévision** : le commissaire aux comptes ne peut pas se prononcer sur des éléments qui résultent de ses propres prestations ou de celles de son réseau [V code de déontologie art. 5 II, 19 ; L. 821-28 IV]. ALTIGLISSE n'est pas une EIP : aucune liste fermée de services interdits ne s'applique. Mais établir les comptes qu'il certifie crée un risque d'autorévision qu'aucune mesure de sauvegarde ne peut réduire. La phrase du gérant (« vous n'aurez plus grand-chose à vérifier ») décrit précisément ce risque [S, application de L. 821-28 IV ; F10 § 3].
- Le fait que CORVANE soit inscrit aux deux professions ne change rien : c'est la **mission** qui fixe les règles, pas le titre.

**Conduite à tenir (0,5 pt)**
- Les comptes de **2026**, établis par le cabinet MOLLARD ET ASSOCIÉS, ne sont pas concernés.
- Pour **2027** et les exercices suivants, CORVANE ne peut pas cumuler les deux missions. Le gérant doit choisir :
  - soit CORVANE reste commissaire aux comptes (nouveau mandat en juin 2027, voir 3.2) et **refuse** la tenue de la comptabilité et l'établissement des comptes, qui sont confiés à un **autre expert-comptable**. Celui-ci formalise sa mission par une lettre de mission et informe son prédécesseur avant d'accepter [V décret art. 151, 163] ;
  - soit CORVANE devient l'expert-comptable d'ALTIGLISSE et **n'est pas renouvelé** comme commissaire aux comptes. L'assemblée désigne un autre commissaire aux comptes, qui vérifie son indépendance et prend contact avec CORVANE avant d'accepter ; CORVANE lui donne accès aux informations utiles [V L. 821-4 II, L. 821-44 al. 3 ; code de déontologie art. 26].
- Dans le second cas, CORVANE ne devrait commencer la tenue de la comptabilité de 2027 qu'après la fin de son mandat. À défaut, il doit apprécier, avec la règle de l'apparence, le risque que cette mission fait peser sur son indépendance jusqu'à l'assemblée de juin 2027 [S, jugement professionnel].
- CORVANE répond par écrit au gérant et documente son analyse. Le commissaire aux comptes peut s'appuyer sur les travaux de l'expert-comptable qui établit les comptes, sans s'y substituer [S, NEP relative à l'expert-comptable intervenant dans l'entité, F11 § 3.3].

**Réponses tolérées** : la démission de CORVANE en cours de mandat présentée comme une solution, si le candidat précise qu'elle suppose un motif légitime (événement compromettant l'indépendance) et ne doit pas nuire à l'entité [V code de déontologie art. 28] ; la solution du non-renouvellement à l'échéance de juin 2027 reste la plus simple.

**Erreurs fréquentes**
- Confondre l'indépendance du commissaire aux comptes et celle de l'expert-comptable, ou refuser à l'expert-comptable le droit de tenir les comptes au nom de l'indépendance (`JUR-A03`).
- Accepter la demande au motif qu'ALTIGLISSE n'est pas une EIP (`JUR-A05`).
- Décrire en détail l'organisation ou le fonctionnement des instances, ce qui n'est pas attendu.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 1, 2, 3, 20, 24, 28, 31, 33, 37, 40 | Conditions, mission, CNOEC et CROEC | [V] | F09 § 2 |
| Décret 2012-432 art. 143, 145-146, 150-151, 163 | Serment, indépendance d'esprit, acceptation, lettre de mission, succession | [V] | F09 § 2.3 ; F10 § 2.2 |
| C. com. L. 820-1, L. 821-12 à L. 821-16, L. 821-23, L. 821-40, L. 821-44 | Conditions, H2A, CNCC, CRCC, désignation, durée | [V] | F09 § 3 |
| C. com. L. 821-27, L. 821-28 IV, L. 821-31 ; code de déontologie art. 5, 19, 26, 28 | Indépendance, autorévision, prédécesseur, démission | [V] ; application : [S] | F10 § 3-5 |

### 3.2 Désignation obligatoire, durée du mandat et lien personnel d'un collaborateur (3 pts)

**Obligation de désigner un commissaire aux comptes (1 pt)**
- **Règle (0,5 pt)** : une SARL doit désigner au moins un commissaire aux comptes si elle dépasse, **à la clôture d'un exercice**, deux des trois seuils suivants : total du bilan **5 000 000 €**, chiffre d'affaires hors taxes **10 000 000 €**, nombre **moyen** de salariés **50** [V L. 223-35 al. 2 ; D. 223-27 renvoyant à D. 221-5]. ALTIGLISSE n'est ni une EIP, ni une entité astreinte à publier des comptes consolidés, ni une société d'un petit groupe : seuls ces seuils s'appliquent.
- **Application (0,5 pt)** :

| Critère | Seuil | 2025 | 2026 |
|---|---:|---:|---:|
| Total du bilan | 5 000 000 € | 4 600 000 € (non) | 5 300 000 € (**oui**) |
| Chiffre d'affaires HT | 10 000 000 € | 9 400 000 € (non) | 10 600 000 € (**oui**) |
| Nombre moyen de salariés | 50 | 44 (non) | 47 (non) |
| Seuils dépassés | | 0 sur 3 | **2 sur 3** |

  L'effectif présent en février (130) n'est pas le critère : c'est le nombre **moyen** de salariés qui compte [V D. 123-200, auquel renvoie D. 221-5]. Deux seuils sont dépassés à la clôture de 2026 : l'assemblée de juin 2027, qui statue sur les comptes de 2026, **doit** désigner un commissaire aux comptes (renouveler CORVANE ou en désigner un autre). La correction des anomalies de l'annexe 3.4 ne change pas la conclusion : le chiffre d'affaires corrigé, 10 600 000 − 288 000 − 120 000 = 10 192 000 €, dépasse encore le seuil.

**Durée du mandat (0,5 pt)** : la désignation est désormais **imposée par la loi**. Le mandat est de **six exercices** (2027 à 2032) ; il expirera après l'assemblée qui statuera sur les comptes de 2032 [V L. 821-44]. Le mandat de trois exercices n'est ouvert qu'aux désignations volontaires ou fondées sur le régime des petits groupes [V L. 821-46]. Il était régulier en 2024, puisque la désignation était volontaire. La proposition du gérant (« trois exercices, comme en 2024 ») n'est **pas possible**. À défaut de désignation, les délibérations prises seraient nulles, et le gérant commettrait un délit [V L. 821-5, L. 821-6 1°].

**Situation 2 : lien personnel d'un membre de l'équipe (1,5 pt)**
- **Identification (0,5 pt)** : il s'agit d'un **lien personnel**. La partenaire de PACS de M. BLANC occupe une **fonction sensible** chez ALTIGLISSE : elle centralise les recettes des magasins, prépare les rapprochements bancaires et les pièces à partir desquelles les comptes sont tenus [V code de déontologie art. 31 ; S pour la qualification].
- **Qualification (0,5 pt)** :
  - un tel lien serait **incompatible** avec la mission s'il concernait Mme FAVRE ou un membre de la direction de CORVANE [V code de déontologie art. 32] ;
  - pour un autre membre de l'équipe, comme M. BLANC, il est incompatible si un **tiers objectif, raisonnable et informé** conclurait que l'indépendance est compromise [V code de déontologie art. 32]. C'est le cas ici : M. BLANC contrôle précisément le cycle dont sa partenaire produit les données [S, application]. Il ne détient pas de parts d'ALTIGLISSE : aucun lien financier n'est en cause [V L. 821-31 ; code art. 33].
- **Conduite à tenir (0,5 pt)** : CORVANE doit en tirer **sans délai** les conséquences [V code de déontologie art. 35] et prendre des **mesures de sauvegarde** [V code art. 5] :
  - retirer M. BLANC de l'équipe d'ALTIGLISSE ;
  - faire revoir, et refaire si besoin, par un autre membre de l'équipe ses travaux de novembre 2026 sur les caisses ;
  - documenter l'analyse et les mesures dans le dossier.

  Avec ces mesures, l'indépendance de CORVANE n'est pas compromise : la mission se poursuit. On valorise la remarque que M. BLANC aurait dû signaler ce lien dès le recrutement de sa partenaire, en septembre 2026 [S].

**Réponses tolérées**
- Un candidat qui rattache la responsable comptable aux « préposés » sans employer l'expression « fonction sensible », s'il applique le critère du tiers objectif.
- Un candidat qui juge qu'elle n'occupe pas une fonction sensible et raisonne à partir du principe général d'indépendance en apparence [V code de déontologie art. 5], s'il conclut aux mêmes sauvegardes.

**Erreurs fréquentes**
- Retenir l'effectif de haute saison (130) au lieu du nombre moyen de salariés (`JUR-F07`).
- Exiger le dépassement des seuils pendant deux exercices consécutifs : cette condition ne joue que pour la sortie de l'obligation.
- Accepter un mandat de trois exercices alors que la désignation est obligatoire.
- Conclure à la démission de CORVANE alors qu'une mesure de sauvegarde suffit (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 223-35, D. 223-27, D. 221-5, D. 123-200 | Seuils de la SARL ; mode de calcul | [V] | F09 § 3.3 ; F99 § 2 |
| C. com. L. 821-44, L. 821-46, L. 821-5, L. 821-6 | Durée de six exercices ; mandat de trois exercices ; sanctions | [V] | F09 § 3.3, 3.5 |
| Code de déontologie art. 5, 31, 32, 33, 35 | Liens personnels et financiers ; sauvegardes ; survenance en cours de mission | [V] ; application : [S] | F10 § 4.1 |

### 3.3 Responsabilités du cabinet MOLLARD ET ASSOCIÉS et de M. MOLLARD (2 pts)

**Responsabilité civile (1 pt)**
- **Nature** : responsabilité **contractuelle** envers ALTIGLISSE, puisque l'établissement de la déclaration de résultat relève de la lettre de mission [V C. civ. 1231-1 ; application à l'expert-comptable par défaut de texte spécial, F09 § 7.1]. Elle suppose une **faute** (omission de la réintégration d'une charge non déductible), un **préjudice** et un **lien de causalité**. Elle se traduit par des **dommages-intérêts**.
- **Qui** : la société d'expertise comptable est responsable de ses travaux ; sa responsabilité laisse subsister la responsabilité **personnelle** de M. MOLLARD pour les travaux qu'il a exécutés [V ord. art. 12]. Le départ à la retraite ne fait pas disparaître la responsabilité de la société [S].
- **Préjudice réparable** : le rappel d'impôt s'élève à 72 000 × 25 % = **18 000 €**. Cet impôt était dû en tout état de cause : il n'est pas, en principe, un préjudice [S, droit commun de la responsabilité]. Le préjudice porte sur la **majoration et les intérêts de retard (2 700 €)** et sur les frais éventuels. Le gérant ne peut donc pas obtenir « le remboursement de tout le redressement » (20 700 €).
- **Garanties** : l'expert-comptable doit être assuré ; la garantie minimale est de 500 000 € par sinistre [V ord. art. 17 ; décret art. 138]. Délai pour agir : cinq ans à compter du jour où ALTIGLISSE a connu les faits [V C. civ. 2224].

**Responsabilité pénale (0,5 pt)** : elle suppose une **infraction**. Une erreur involontaire dans une déclaration n'en constitue pas ; les délits propres à la profession visent l'exercice illégal, l'usage abusif du titre ou la violation du secret professionnel [V ord. art. 20, 21]. Seule une participation volontaire à une fraude pourrait engager la responsabilité pénale de M. MOLLARD [S, droit pénal général]. La demande de « condamnation pénale » est **infondée**.

**Responsabilité disciplinaire (0,5 pt)** : l'omission traduit un manquement aux devoirs de compétence et de conscience professionnelle [V décret art. 142, 145]. M. MOLLARD, encore inscrit au tableau, peut faire l'objet de **poursuites disciplinaires** devant les juridictions disciplinaires de l'ordre. Les sanctions vont de la **réprimande** et du **blâme** à la suspension et à la **radiation** [V ord. art. 49-50, 53]. La radiation paraît disproportionnée pour une erreur isolée et reconnue [S]. Le gérant peut signaler les faits au conseil régional, qui surveille l'exercice de la profession [V ord. art. 31], mais il ne décide pas de la sanction. Une sanction disciplinaire ne répare pas le préjudice : seule l'action civile le fait.

On valorise la remarque que la responsabilité de CORVANE n'est pas en cause : la déclaration fiscale ne relève pas de la certification, et le commissaire aux comptes n'est pas garant de l'absence de toute erreur [S, F09 § 7.1].

**Réponses tolérées** : une responsabilité délictuelle évoquée à titre subsidiaire, si la responsabilité contractuelle est retenue en premier.

**Erreurs fréquentes**
- Confondre la radiation (sanction disciplinaire) avec une sanction pénale.
- Accorder la réparation de l'impôt lui-même sans discuter le préjudice (`JUR-A05`).
- Appliquer à l'expert-comptable les règles de responsabilité du commissaire aux comptes (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 12, 17, 20, 21, 31, 49-50, 53 ; décret 2012-432 art. 138, 142, 145 | Responsabilité des travaux ; assurance ; délits ; discipline | [V] | F09 § 7 ; F10 § 2.2 |
| C. civ. 1231-1, 2224 | Responsabilité contractuelle ; prescription de droit commun | [V] ; application : [S] | F09 § 7.1 |
| Préjudice réparable (impôt dû) | Droit commun de la responsabilité | [S] | — |

### 3.4 Cycle ventes et trésorerie : risques, assertions et procédures (3 pts)

**Risque d'anomalies significatives et orientation des travaux (1,5 pt)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41]
- **Composantes (0,5 pt)** : le risque d'anomalies significatives (RAS) est propre à l'entité. Il comprend :
  - le **risque inhérent** : possibilité qu'une anomalie significative se produise, sans tenir compte des contrôles de l'entité ;
  - le **risque lié au contrôle** : risque qu'une anomalie ne soit ni prévenue ni détectée et corrigée par les contrôles de l'entité.

  Le **risque de non-détection**, lui, est propre à la mission : c'est le risque que le commissaire aux comptes ne détecte pas une anomalie significative.
- **Application (0,5 pt)** :
  - risque **inhérent élevé** : forte volumétrie de petites opérations dans cinq magasins ; **espèces**, exposées au détournement ; **produit nouveau** (forfaits « saison » payés d'avance, à cheval sur deux exercices) ; encaissements par un **tiers** (plateforme), nets de commission ; **incitation** à présenter un chiffre d'affaires en hausse à la banque, qui est un facteur de risque de fraude [V NEP risques § 02] ;
  - risque **lié au contrôle élevé** : annulations après encaissement sans validation ; rapprochements de caisse dans trois magasins sur cinq seulement ; relevés de la plateforme non rapprochés ; poste de responsable comptable vacant pendant deux mois ; forfaits comptabilisés à l'encaissement, sans procédure de séparation des exercices. Sans test des contrôles, le RAS au niveau des assertions correspond au risque inhérent évalué [V NEP risques § 41].
- **Orientation (0,5 pt)** : le RAS étant élevé, le risque de non-détection acceptable est **faible** [V NEP principes § 13]. CORVANE renforce ses **procédures de substance** : travaux à la clôture, éléments probants externes, contrôles inopinés (caisses), échantillons élargis, équipe expérimentée [V NEP réponses § 03-13 ; NEP éléments probants § 6]. Il ne s'appuie pas sur des contrôles défaillants.

**Assertions et procédures (1,5 pt, 0,5 pt par risque pertinent avec son assertion et une procédure justifiée)**

| Risque | Assertion | Procédure et justification |
|---|---|---|
| Forfaits « saison » comptabilisés en totalité à l'encaissement | **Séparation des exercices** des ventes (flux) ; **exhaustivité** des produits constatés d'avance (solde) | Extraction du logiciel de la liste des 1 200 forfaits, rapprochée des encaissements (relevés bancaires) ; **inspection** des conditions de vente (période couverte du 07/12/2026 au 10/04/2027) ; **vérification du calcul** du prorata : 360 000 × 25 / 125 = 72 000 € rattachés à 2026, soit 288 000 € de produits constatés d'avance |
| Espèces : annulations sans validation, rapprochements incomplets | **Exhaustivité** des ventes (flux) ; **existence** de la caisse (solde) | **Comptages de caisse inopinés** (inspection physique) ; rapprochement, pour les deux magasins non suivis, du journal de caisse, des espèces comptées et des bordereaux de remise en banque ; **inspection** d'un échantillon de contrats annulés après encaissement ; contrôle des recettes des derniers jours de décembre (séparation) |
| Plateforme : encaissements par un tiers, relevés non rapprochés | **Réalité** et **mesure** des ventes (flux) ; **existence** de la créance de 96 000 € (solde) | **Demande de confirmation** du solde et des commissions à la plateforme (élément externe) ; rapprochement de ses relevés avec les réservations du logiciel et avec le virement reçu le 10/01/2027 ; vérification que les ventes sont enregistrées pour leur montant brut et la commission en charges |

Autres réponses acceptées : vente du lot de skis d'occasion facturée le 28/12/2026 et livrée en avril 2027 (**séparation des exercices** et **réalité** des ventes ; examen des bons de livraison et des conditions de vente, confirmation auprès du revendeur) ; confirmation des soldes bancaires et contrôle des rapprochements bancaires (existence et exhaustivité de la trésorerie) ; procédure analytique (voir 3.5), utile mais insuffisante seule face à un risque élevé.

**Réponses tolérées** : la « réalité » des ventes pour le risque lié à l'incitation de la banque, si elle est rattachée à un fait de l'annexe.

**Erreurs fréquentes**
- Confondre la réalité (flux) et l'existence (solde), ou la séparation des exercices et l'exhaustivité (`JUR-A01`).
- Proposer des procédures génériques, sans lien avec les faits de l'annexe (`JUR-A05`, `JUR-A06`).
- Développer l'organisation des contrôles de l'entité, qui relève de l'UE 3, au lieu de l'évaluer comme composante du risque.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 10-13 | Risque d'audit, RAS, risque de non-détection | [V] | F11 § 4.1 |
| NEP risques § 02, 39-41 | Facteurs de risque inhérent ; évaluation sans test des contrôles | [V] | F11 § 4.1 |
| NEP éléments probants § 6, 9, 10 | Fiabilité ; assertions ; techniques | [V] | F11 § 4.3, 6.1-6.2 |
| NEP réponses § 03-13 ; NEP confirmations § 4-5 | Procédures en réponse ; confirmation d'un solde | [V] | F11 § 5, 6.3 |

### 3.5 Procédure analytique ; lettre de mission, programme et feuille de travail (3 pts)

**Calcul du chiffre d'affaires attendu (1 pt)**

| Élément | Calcul | Résultat |
|---|---|---:|
| Hiver, location à la journée | 3 000 × 130 × 50 % × 32 € | 6 240 000 € |
| Été, location à la journée | 1 000 × 100 × 40 % × 36 € | 1 440 000 € |
| Forfaits « saison » rattachés à 2026 | 1 200 × 300 € × 25 / 125 | 72 000 € |
| **Chiffre d'affaires attendu des locations** | | **7 752 000 €** |

Locations à la journée (0,5 pt) ; forfaits et total (0,5 pt).

**Comparaison, explication et conclusion (0,5 pt)**

| Élément | Calcul | Résultat |
|---|---|---:|
| Écart brut | 8 049 000 − 7 752 000 | **297 000 €**, soit 3,8 % de l'attendu |
| Part expliquée par les forfaits | 360 000 comptabilisés − 72 000 rattachables | 288 000 € |
| Écart résiduel | 297 000 − 288 000 | **9 000 €**, soit 0,1 % |

- L'écart brut dépasse l'écart acceptable de 50 000 € : il faut l'expliquer.
- Il s'explique presque entièrement par les forfaits « saison », comptabilisés à l'encaissement alors que 100 / 125 de la saison concernent 2027. Le chiffre d'affaires des locations est **surévalué de 288 000 €**, et des produits constatés d'avance du même montant manquent : c'est une anomalie de **séparation des exercices**, à communiquer à la direction.
- L'écart résiduel (9 000 €) est inférieur à l'écart acceptable : le chiffre d'affaires des locations à la journée est **plausible**.

**Limites (0,5 pt)**
- Les données (parc, taux d'utilisation, prix moyens) proviennent du **logiciel de location**, élément interne dont la fiabilité dépend des contrôles de l'entité [V NEP éléments probants § 6]. Or ce logiciel permet d'annuler un contrat après encaissement : une recette en espèces détournée réduirait à la fois le chiffre d'affaires et le taux d'utilisation, sans créer d'écart.
- Les taux et les prix sont des **moyennes**, et l'écart acceptable relève du jugement du cabinet [V NEP réponses § 05].
- Face à un RAS élevé sur l'exhaustivité des espèces, la procédure analytique ne suffit pas seule : elle complète les tests de détail de 3.4. On valorise la corroboration du taux d'utilisation par une donnée indépendante, par exemple les encaissements par carte bancaire [S].

**Supports de la mission (1 pt)**
- **Lettre de mission et programme de travail (0,5 pt)** :
  - la **lettre de mission** est établie la **première année du mandat**, avant les travaux. Elle précise l'objectif et l'étendue de la mission, le calendrier, les signataires, les obligations d'information de l'entité, la demande de déclarations écrites et le **budget d'honoraires** ; elle est révisée en cas de changement important [V NEP lettre de mission § 3-8]. Le nouveau mandat de six exercices (3.2) justifie une nouvelle lettre de mission [S, déduction] ;
  - le **programme de travail** décrit la **nature et l'étendue des diligences** et le nombre d'heures affectées ; il découle du plan de mission et traduit ici les procédures de 3.4 et 3.5 pour le cycle ventes et trésorerie [V NEP planification § 10-11 ; D. 821-187].
- **Feuille de travail de la procédure analytique (0,5 pt)** : elle doit permettre à un auditeur expérimenté extérieur à la mission de comprendre les travaux [V NEP documentation § 04-08]. Elle mentionne :
  - l'**objectif** (plausibilité du chiffre d'affaires des locations ; réalité, exhaustivité, séparation des exercices) ;
  - la **source des données** (extraction du logiciel, date) et l'écart acceptable retenu ;
  - les **travaux** (calcul de l'attendu, comparaison) et les **résultats** (écart de 297 000 €, explication, résiduel de 9 000 €) ;
  - la **conclusion** (anomalie de 288 000 € reportée dans la note de synthèse ; résiduel acceptable) ;
  - l'**identité et la date** de l'exécutant et du réviseur [V NEP documentation § 04-08 ; « feuille de travail » : terme de pratique, S, F11 § 7].

**Réponses tolérées**
- Un écart calculé sur le seul chiffre d'affaires des locations à la journée (8 049 000 − 7 680 000 = 369 000 €), si le candidat retire ensuite les forfaits comptabilisés (360 000 €) et retrouve le même résiduel de 9 000 €, puis chiffre l'anomalie de 288 000 €.
- Le plan de mission cité avec le programme de travail.

**Erreurs fréquentes**
- Inclure les forfaits pour 360 000 € dans l'attendu : l'écart tombe à 9 000 € et l'anomalie de séparation disparaît (`JUR-F07`).
- Ne pas justifier les calculs (`JUR-F02`).
- Conclure qu'un écart faible prouve l'exhaustivité des ventes, sans voir que les données viennent du même logiciel (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP éléments probants § 6, 10 ; NEP réponses § 05 | Procédures analytiques ; procédure de substance et écart acceptable | [V] | F11 § 6.1-6.2 |
| NEP lettre de mission § 3-8 | Contenu et révision de la lettre de mission | [V] | F11 § 7 |
| NEP planification § 10-11 ; C. com. D. 821-187 | Plan de mission et programme de travail | [V] | F11 § 7 |
| NEP documentation § 04-08 | Contenu du dossier ; feuille de travail | [V] ; terme : [S] | F11 § 7 |
| Règle de rattachement des forfaits (annexe 3.3) | Prorata de la saison couverte | données de l'énoncé | — |

### 3.6 Opinion sur les comptes 2026 (3 pts)

**Comparaison de chaque anomalie et de leur cumul au seuil (1 pt)**

| Anomalie non corrigée | Postes touchés | Montant | Rapport au seuil (60 000 €) |
|---|---|---:|---|
| 1. Forfaits « saison » | Chiffre d'affaires des locations ; produits constatés d'avance | 288 000 € | 4,8 fois : **significative seule** |
| 2. Lot de skis facturé, non livré | Chiffre d'affaires des ventes ; créances clients | 120 000 € | 2 fois : **significative seule** |
| 3. Écart de caisse inexpliqué | Trésorerie ; charges | 40 000 € | inférieure, mais significative par sa **nature** |
| 4. Facture d'entretien non rattachée | Charges ; dettes | 12 000 € | inférieure ; récapitulée (plus de 3 000 €) |
| **Cumul** | | **460 000 €** | 7,7 fois ; **38,3 %** du résultat avant impôt |

- **Seuil (0,5 pt)** : 5 % × 1 200 000 € = **60 000 €**. Le pourcentage est une hypothèse du cabinet : les NEP n'en fixent aucun [V NEP caractère significatif § 10, 17 ; F11 § 4.2].
- **Anomalies (0,5 pt)** :
  - les anomalies 1 et 2 sont **significatives chacune à elle seule** ;
  - l'anomalie 3 est inférieure au seuil. Mais un manque d'espèces sans explication, dans les deux magasins dont les caisses ne sont pas rapprochées, est significatif par sa **nature** et par les **circonstances** de sa survenance [V NEP caractère significatif § 9] ;
  - l'anomalie 4 dépasse le seuil des anomalies manifestement insignifiantes : elle est récapitulée et entre dans le **cumul** [V NEP anomalies § 8, 14] ;
  - les anomalies corrigées (21 000 € et 30 000 €) n'ont plus d'incidence.

**Arguments du gérant et absence de limitation (0,5 pt)**
- Un encaissement non remboursable ne rattache pas le produit à 2026 : la règle est le prorata de la saison couverte. Une facture ne fait pas la vente : la règle est la livraison, prévue en avril 2027.
- L'écart de caisse a été établi par comptage ; « il se retrouvera » n'est pas un élément probant. L'attente de la banque n'est pas un motif : elle confirme au contraire le facteur de risque de fraude relevé en 3.4.
- **Aucune limitation** ne subsiste : la plateforme a été contrôlée par des procédures alternatives, les travaux de novembre ont été refaits, et le cabinet a pu chiffrer chaque anomalie. Il n'y a pas d'incertitudes multiples.

**Opinion (1 pt)**
- **Une réserve ne suffit plus (0,5 pt)**. Le commissaire aux comptes refuse de certifier lorsque les anomalies significatives non corrigées ont des incidences **non circonscrites**, ou lorsque la formulation d'une réserve est **insuffisante** pour permettre à l'utilisateur de fonder son jugement [V NEP rapport § 12-13 ; F11 § 8.1]. C'est le cas ici :
  - les anomalies touchent **plusieurs postes** : les deux rubriques du chiffre d'affaires, les produits constatés d'avance, les créances clients, la trésorerie, les charges, puis le résultat, l'impôt et les capitaux propres ;
  - elles procèdent de **défaillances communes** du cycle (séparation des exercices des ventes, suivi des espèces) ;
  - elles changent la **lecture d'ensemble** des comptes. Le résultat avant impôt présenté progresse de 20 % (1 200 000 € contre 1 000 000 € en 2025). Le résultat corrigé, 740 000 €, **recule de 26 %**. Le chiffre d'affaires et le résultat sont précisément les éléments sur lesquels la banque fonde sa décision. Une réserve énumérant ces corrections ne permettrait pas à l'utilisateur de juger des comptes pris dans leur ensemble.
- **Conclusion (0,5 pt)** : CORVANE **refuse de certifier** les comptes annuels 2026 d'ALTIGLISSE [V NEP rapport § 12-13 ; R. 821-180]. Il expose les motifs dans la partie « Fondement de l'opinion » et en quantifie les incidences : chiffre d'affaires surévalué de 408 000 € (288 000 + 120 000), résultat avant impôt surévalué de 460 000 €, résultat net surévalué de 345 000 € après impôt au taux de 25 %. Les motifs sont communiqués au préalable au gérant, organe de direction [V NEP rapport § 06 ; L. 821-63 I]. Le gérant remet une déclaration écrite à laquelle est joint l'état des anomalies non corrigées [V NEP anomalies § 15-17].

**Opinions écartées (0,5 pt)**
- **Sans réserve** : impossible, deux anomalies sont significatives à elles seules et leur cumul atteint 7,7 fois le seuil.
- **Certification avec réserve** : elle suppose des incidences clairement circonscrites et une réserve suffisante [V NEP rapport § 09-10]. Ce n'est pas le cas : les anomalies sont dispersées sur plusieurs postes et inversent le sens de l'évolution du résultat.
- **Impossibilité de certifier** : elle suppose une limitation aux incidences non circonscrites ou des incertitudes multiples [V NEP rapport § 14]. Il n'y a ni l'une ni les autres : les anomalies sont connues et chiffrées. Le refus traduit un **désaccord**, pas une impossibilité.

**Réponses tolérées**
- Une réserve pour désaccord reçoit les points de la comparaison au seuil (1 pt), des arguments du gérant (0,5 pt) et le premier point des opinions écartées, si elle décrit et chiffre toutes les anomalies. Le point de l'opinion n'est pas accordé. Le jugement sur le caractère circonscrit n'est fixé par aucun seuil [V NEP rapport § 12-13].
- Le chiffrage limité au résultat avant impôt (460 000 €) ou au résultat net (345 000 €), si les postes touchés sont décrits.

**Erreurs fréquentes**
- S'arrêter à une réserve parce que chaque anomalie, prise seule, porte sur un poste identifié, sans apprécier leur effet sur les comptes pris dans leur ensemble.
- Écarter l'écart de caisse parce qu'il est inférieur au seuil, sans examiner sa nature.
- Conclure à l'impossibilité de certifier, alors qu'aucune limitation ne subsiste.
- Donner l'opinion sans ses motifs ni sa quantification (`JUR-A02`) ; ne pas justifier les calculs (`JUR-F02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP caractère significatif § 6, 9, 10, 17 | Seuil ; nature et circonstances ; critères | [V] | F11 § 4.2 |
| NEP anomalies § 8, 14, 15-17 | Anomalies manifestement insignifiantes ; appréciation individuelle ou cumulée ; déclaration écrite | [V] | F11 § 4.2, 8.2 |
| NEP rapport § 06, 09-14 ; C. com. R. 821-180, L. 821-63 I | Quatre opinions et leurs conditions ; communication préalable | [V] | F11 § 8.1 |
| Caractère non circonscrit en l'espèce | Application de la table de décision | [S, jugement professionnel] | F11 § 8.2 |

---


### Partie B – Durabilité (12 points)

### 3.7 Acteurs, normes, interopérabilité ; choix entre la VSME et les ESRS (5 pts)

**Acteurs, normes et approche de la matérialité (2,5 pts)**

| Acteur | Normes | Approche de la matérialité | Points |
|---|---|---|---:|
| **ISSB** (International Sustainability Standards Board), organe de normalisation créé au sein de la Fondation IFRS (annoncé en novembre 2021) | **IFRS S1** (exigences générales) et **IFRS S2** (climat), publiées en juin 2023, applicables aux exercices ouverts à compter du 01/01/2024 [S] | **Financière** (« simple matérialité ») : risques et opportunités liés à la durabilité susceptibles d'affecter les flux de trésorerie, l'accès au financement ou le coût du capital ; destinataires : investisseurs et prêteurs [S] | 0,5 |
| **TCFD** (groupe de travail créé par le Conseil de stabilité financière) | Recommandations sur les informations climatiques, **intégrées** dans IFRS S1 et S2 ; la TCFD a été dissoute en octobre 2023 et l'ISSB a repris le suivi des publications climatiques [S] | Financière (climat) | 0,5 |
| **EFRAG** (European Financial Reporting Advisory Group), conseiller technique de la Commission européenne | Prépare les projets d'**ESRS**, que la Commission adopte par actes délégués après son avis technique [V] ; **norme volontaire VSME**, adoptée par le règlement délégué (UE) 2026/1560 sur la base d'une recommandation de 2025 [V] | **Double matérialité** : impact et financière [V] | 1 |
| **GRI** (Global Reporting Initiative) | Normes universelles, sectorielles et thématiques [S] | **Impact** : impacts de l'entité sur l'économie, l'environnement et les personnes [S] | 0,5 |

Formule de synthèse : GRI = impact ; ISSB = financier ; ESRS = double matérialité, qui réunit les deux angles [S, cohérent avec ESRS 1 (2026) § 2 et 23].

**Interopérabilité (0,5 pt)**
- **ESRS et GRI** : déclaration commune de l'EFRAG et de la GRI (fin août et début septembre 2023). Les définitions et indicateurs d'impact sont alignés ou étroitement alignés ; une entité qui publie selon les ESRS est considérée comme publiant « with reference to » les normes GRI [V page EFRAG ; F12 § 1].
- **ESRS et ISSB** : guide d'interopérabilité de la Fondation IFRS et de l'EFRAG (mai 2024). La matérialité financière des ESRS est alignée sur celle d'IFRS S1, avec une forte convergence sur le climat [S].
- Les ESRS révisées doivent tenir compte, dans toute la mesure du possible, de l'interopérabilité avec les normes mondiales [V règl. délégué 2026/1563, consid. 2].

**Conseil à ALTIGLISSE : étendue et limites des informations (2 pts)**
- **Situation (0,5 pt)** : ALTIGLISSE n'entre pas dans le champ des entités tenues de publier (hypothèse). Elle choisit librement son référentiel, et sa publication reste **volontaire** : ce n'est pas l'état de durabilité légal de la section du rapport de gestion, et aucune certification légale n'est obligatoire [V L. 232-6-3 I et III ; S pour l'application à une publication volontaire, F12 § 2 et 11].
- **VSME, solution recommandée (1 pt)** :
  - elle est conçue pour les entreprises **non soumises** à l'obligation de publier [V règl. délégué 2026/1560 art. 2] ;
  - elle est structurée en un **module de base** et un **module complet** [V règl. délégué 2026/1560, annexe I]. ALTIGLISSE peut commencer par le module de base et ajouter le module complet si les demandes de la banque le justifient [S, conseil] ;
  - elle est proportionnée à une SARL de 47 salariés en moyenne et répond à la situation d'ALPINE CRÉDIT. Une entreprise tenue de publier ne peut exiger d'une entreprise de sa chaîne de valeur dont l'effectif ne dépasse pas le plafond fixé par le texte (« entreprise protégée ») que les informations prévues par la norme volontaire, pour les exercices commençant à compter du 01/01/2027 [V règl. délégué 2026/1560 art. 1, 3, 4 ; ESRS 1 (2026) § 66] ;
  - **limites** : l'information est celle des modules retenus, sans analyse complète de double matérialité. Elle ne vaut pas état de durabilité au sens légal.
- **ESRS appliquées volontairement (0,5 pt)** :
  - **étendue** : les informations générales (ESRS 2) sont publiées quel que soit le résultat de l'analyse de matérialité. Pour chaque thème matériel **seulement**, l'entité publie les exigences générales (politiques, actions, indicateurs, cibles), les exigences thématiques pertinentes et, si besoin, des informations spécifiques. La chaîne de valeur n'est couverte que pour les informations matérielles, avec des estimations admises [V ESRS 1 (2026) § 11, 24, 29-30, 62-65] ;
  - **limites** : il faut conduire une **analyse complète de double matérialité**, ce qui est lourd pour une entité de cette taille. L'entité ne publie pas d'information non matérielle, sauf informations supplémentaires signalées comme telles [V ESRS 1 (2026) § 108-109]. Elle a intérêt à indiquer clairement qu'elle applique les ESRS volontairement [S, bonne pratique].

**Réponses tolérées**
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences »).
- Le choix motivé des ESRS si le candidat en mesure le coût et l'exigence (double matérialité complète) ; la mention des normes IFRS S, la banque étant un prêteur, comme complément.

**Erreurs fréquentes**
- Présenter la TCFD comme un normalisateur toujours actif, ou l'EFRAG comme l'auteur juridique des ESRS (c'est la Commission qui les adopte).
- Discuter les seuils ou le calendrier d'assujettissement à la publication, alors que l'énoncé les écarte par hypothèse (`JUR-F07`).
- Réciter le panorama sans conseiller ALTIGLISSE (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Pages ISSB et IFRS S1, S2 (ifrs.org) ; FSB | ISSB, IFRS S, intégration de la TCFD | [S] | F12 § 1 |
| Règl. délégué 2026/1563, consid. 2-3 | Rôle de l'EFRAG ; interopérabilité | [V] | F12 § 1 |
| Déclaration EFRAG-GRI (2023) ; guide IFRS-EFRAG (mai 2024) | Interopérabilité | [V] / [S] | F12 § 1 |
| Règl. délégué 2026/1560 art. 1-4, annexe I ; ESRS 1 (2026) § 66 | VSME ; modules ; plafond de la chaîne de valeur | [V] | F12 § 4 |
| ESRS 1 (2026) § 11, 24, 29-30, 62-65, 108-109 | Étendue et limites des informations ESRS | [V] | F12 § 5, 7, 8 |

### 3.8 IRO, double matérialité et connectivité (4 pts)

**Définitions (1 pt)**
- **IRO** :
  - les **impacts** de l'entreprise sur la population ou l'environnement, positifs ou négatifs, réels ou potentiels, liés à ses activités propres et à sa **chaîne de valeur amont et aval** ;
  - les **risques et opportunités** : effets financiers des enjeux de durabilité pour l'entreprise, y compris ceux qui naissent de ses **dépendances** à l'égard de ressources naturelles, humaines ou sociales [V ESRS 1 (2023) § 14 ; ESRS 1 (2026) § 2, 39, 48].
- **Double matérialité** : un enjeu est matériel au titre de la **matérialité d'impact**, de la **matérialité financière**, ou des deux. Les deux dimensions interagissent [V ESRS 1 (2023) § 28 ; ESRS 1 (2026) § 35-36].
  - Un impact négatif s'apprécie selon sa **gravité** (ampleur, étendue, caractère irrémédiable) et, s'il est potentiel, sa **probabilité** [V § 40].
  - Un effet financier s'apprécie selon sa probabilité et son ampleur. Il peut affecter la situation financière, la performance, les flux de trésorerie, l'**accès au financement** ou le **coût du capital**, à court, moyen ou long terme [V § 47, 50].

**Impact dans la chaîne de valeur (1 pt)** : une réponse argumentée suffit.

| Enjeu | Dimension | Analyse |
|---|---|---|
| Fabrication hors d'Europe des skis, snowboards, vélos et batteries de VAE (lithium, cobalt) | **Impact négatif**, réel ou potentiel, dans la **chaîne de valeur amont** | L'extraction des métaux et la fabrication ont des impacts sur l'environnement et sur les populations des zones de production ; s'y ajoutent les émissions de gaz à effet de serre de la fabrication et du transport. ALTIGLISSE y est liée par ses **achats**, relations d'affaires directes avec les fabricants et indirectes avec leurs fournisseurs [V ESRS 1 (2026) § 39, 62-65]. Gravité : ampleur et caractère difficilement réversible des impacts miniers ; probabilité à apprécier faute de données des fabricants, d'où l'usage d'estimations [V § 40, 65] |

Autres réponses acceptées :
- **impact positif** : la location mutualise le matériel (plusieurs dizaines de clients par paire et par saison) et réduit les achats individuels ; il ne se compense pas avec les impacts négatifs [V ESRS 1 (2026) § 44] ;
- **chaîne de valeur aval** : fin de vie du matériel et des batteries (recyclage, collecte), ou déplacements des clients en voiture, si le candidat justifie le lien avec l'activité d'ALTIGLISSE [S].

**Risque financier lié à la baisse de l'enneigement (1 pt)**
- **Nature** : risque **physique** lié au climat, qui s'aggrave progressivement, qui naît de la **dépendance** d'ALTIGLISSE à une ressource naturelle, la neige. Ce risque existe sans impact préalable de l'entreprise [V ESRS 1 (2026) § 36, 48].
- **Effets financiers** : l'hiver procure environ quatre cinquièmes du chiffre d'affaires des locations. Dans les deux magasins de basse altitude, les jours d'ouverture ont baissé de 30 % en dix ans (de 120 à 84), et l'étude prévoit une nouvelle baisse d'ici 2040. D'où des recettes en baisse, un parc sous-utilisé et des conditions de financement plus difficiles : la banque examine précisément ces risques [V § 47].
- **Horizons** : effets déjà visibles à court terme, aggravés à moyen et long terme. L'**opportunité** liée (location de vélos en hausse de 18 % par an, projet de 400 VAE) est valorisée si elle est rattachée au même enjeu climatique.

**Connectivité avec les états financiers (1 pt)** [V ESRS 1 (2026) § 112-116]
- **Parc de skis** : la baisse de l'enneigement et le retrait prévu de 600 paires des magasins de basse altitude (valeur nette comptable de ces magasins : 540 000 €) changent l'utilisation attendue du parc. La **durée d'utilisation** doit être révisée et le plan d'amortissement modifié pour l'avenir. La sous-utilisation est un indice de perte de valeur : on compare la valeur nette comptable à la **valeur actuelle** (prix de revente d'occasion, par exemple) et l'on **déprécie** si elle est inférieure (règles de l'annexe 3.5) [S, application].
- **Chiffre d'affaires saisonnier** : l'hiver représente 81,4 % du chiffre d'affaires attendu des locations ((6 240 000 + 72 000) / 7 752 000, annexe 3.3). C'est l'exposition financière au risque d'enneigement, présentée comme une connexion indirecte avec le compte de résultat [V ESRS 1 (2026) § 115].
- **Cohérence des hypothèses** : le scénario d'enneigement retenu dans les informations de durabilité doit être cohérent avec les hypothèses des comptes (durées d'utilisation, dépréciation) ; les différences significatives sont expliquées [V § 116].
- **Connexion directe** : le prêt de 1 500 000 € et l'achat des VAE figureront dans les deux documents, qui renvoient l'un à l'autre [V § 114].

**Réponses tolérées**
- Le vocabulaire des ESRS de 2023 (« incidences », « double importance »).
- Un risque de transition (évolution de la demande, attentes de la banque) présenté en plus du risque physique.

**Erreurs fréquentes**
- Présenter un impact sans dire qui il affecte, ni où il se situe dans la chaîne de valeur (`JUR-A05`).
- Confondre impact (effet de l'entreprise sur son environnement) et risque (effet de l'environnement sur l'entreprise).
- Ne pas exploiter les chiffres de l'annexe 3.5 pour la connectivité (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2023) § 14, 28 ; ESRS 1 (2026) § 2, 35-36, 39-41, 44, 47-50 | IRO ; double matérialité ; gravité ; effets financiers ; dépendances | [V] | F12 § 6 |
| ESRS 1 (2026) § 62-65 | Chaîne de valeur ; estimations | [V] | F12 § 7 |
| ESRS 1 (2026) § 112-116 | Connectivité : connexions directes et indirectes, cohérence des hypothèses | [V] | F12 § 9 |
| Règles comptables de l'annexe 3.5 | Révision de la durée d'utilisation ; dépréciation | données de l'énoncé | — |

### 3.9 Qui délivre l'assurance ; assurance limitée et assurance raisonnable (3 pts)

**Qui peut délivrer l'assurance (1 pt)**
- **Professionnels habilités (0,5 pt)** : la certification des informations en matière de durabilité est réservée :
  - à un **commissaire aux comptes inscrit sur la liste spéciale** des commissaires aux comptes habilités à certifier ces informations : il a accompli au moins **huit mois** de stage dans ce domaine et réussi une **épreuve** sur la certification de durabilité [V L. 821-13 II, L. 821-18 I] ;
  - ou à un **organisme tiers indépendant (OTI)** accrédité par le comité français d'accréditation, au sein duquel un **auditeur des informations en matière de durabilité** inscrit sur la liste de la H2A (master, stage de huit mois, épreuve) signe le rapport [V L. 822-1 II, L. 822-3, L. 822-4, L. 822-6].

  La H2A inscrit ces professionnels, adopte les normes, contrôle et sanctionne [V L. 820-1]. Un consultant non inscrit ne pourrait pas délivrer cette certification [S]. Par hypothèse, l'assemblée d'ALTIGLISSE désignerait le professionnel ; une désignation non imposée par la loi peut être limitée à trois exercices [V L. 821-40 I, L. 821-46 ; L. 822-17, L. 822-20].
- **CORVANE (0,5 pt)** : Mme FAVRE est inscrite sur la liste spéciale ; le même cabinet peut certifier les comptes et les informations de durabilité, et le rapport est signé par un commissaire aux comptes personne physique inscrit sur cette liste [V L. 821-26]. En revanche, CORVANE ne peut pas **rédiger** le rapport puis en délivrer l'assurance : il se prononcerait sur ses propres travaux (**autorévision**). Le code de déontologie des commissaires aux comptes s'applique à cette mission [V code de déontologie art. 1er II, 5 II ; L. 822-7 ; S, application]. CORVANE doit choisir : aider ALTIGLISSE à préparer son rapport (une autre personne habilitée délivrant alors l'assurance), ou délivrer l'assurance sans participer à la rédaction.

**Nature de l'assurance et différence avec la certification des comptes (2 pts)**
- **Assurance limitée (1 pt)** : la mission repose sur une **assurance limitée** [V LD 2026, niveau d'assurance]. Les vérifications sont moindres en **nature**, en **étendue** et en **durée** que pour une assurance raisonnable. La conclusion est exprimée sous une **forme négative** : le vérificateur n'a pas relevé d'erreurs, omissions ou incohérences importantes [V LD 2026 ; annexe 2, p. 46].
- **Assurance raisonnable de la certification des comptes (0,5 pt)** : l'audit des comptes donne une assurance **élevée, mais non absolue**, que les comptes pris dans leur ensemble ne comportent pas d'anomalies significatives. L'opinion est exprimée sous une **forme positive** : les comptes sont réguliers et sincères et donnent une image fidèle [V L. 821-53 ; NEP principes § 08-09].
- **Distinction des missions (0,5 pt)** : les deux missions sont **distinctes**, même si CORVANE les exerce toutes deux [V LD 2026 § 2]. Aucune ne garantit la viabilité de l'entité ni la qualité de sa gestion [V L. 821-55] : la banque n'obtiendra pas de « garantie ».

**Réponses tolérées** : le vocabulaire « auditeur de durabilité » ou « vérificateur » ; la mention de la consultation du CSE comme sans objet pour une publication volontaire, sans autre développement.

**Erreurs fréquentes**
- Présenter l'assurance limitée comme une assurance raisonnable « allégée » exprimée sous forme positive (`JUR-A01`).
- Admettre que CORVANE rédige le rapport puis le certifie.
- Développer les avis par axe, qui ne sont pas demandés.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 820-1, L. 821-13 II, L. 821-18 I, L. 821-26, L. 822-1 II, L. 822-3, L. 822-4, L. 822-6, L. 822-7 | Professionnels habilités ; H2A ; signature ; déontologie | [V] | F09 § 4 ; F10 § 1 |
| C. com. L. 821-40 I, L. 821-46, L. 822-17, L. 822-20 | Désignation ; mandat de trois exercices | [V] | F13 § 1 |
| LD 2026, niveau d'assurance, § 2 ; annexe 2, p. 46 | Assurance limitée ; forme négative ; mission distincte | [V] | F13 § 2.3, 4.2 |
| C. com. L. 821-53, L. 821-55 ; NEP principes § 08-09 | Assurance raisonnable ; absence de garantie | [V] | F11 § 1.1 |
| Code de déontologie art. 1er II, 5 II | Autorévision | [V] ; application : [S] | F10 § 3 |
