# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 8

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22 et le 30/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex19_consolidation_anc_ecart_negatif_secteurs` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.7 | `exercices/ex20_fusion_filiales_controle_commun` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.9 | `exercices/ex21_audit_tresorerie_continuite_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 2 |
| 1.2 a Conséquence de l'émission obligataire | `2.1.b` Contexte réglementaire et légal de la consolidation | 0,75 |
| 1.2 b IASB, IFRIC, EFRAG | `2.1.a` Cadre conceptuel de l'IASB et normalisateurs | 1,25 |
| 1.2 c Cadre conceptuel de l'IASB | `2.1.a` Cadre conceptuel de l'IASB et normalisateurs | 1 |
| 1.3 Processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.4 Périmètre et méthodes | `2.1.c` Périmètre ; `2.1.d` Conséquences du référentiel et des méthodes | 1 |
| 1.5 Provision pour hausse des prix | `2.2.b` Élimination des écritures fiscales | 4 |
| 1.6 Crédit-bail du robot chirurgical | `2.2.c` Homogénéisation, thèmes communs | 5 |
| 1.7 a Redevances de services centraux | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.7 b Compte courant | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.7 c Dividendes | `2.2.f` Comptes réciproques et résultats internes ; `2.2.h` Partage (mise en équivalence) | 2 |
| 1.8 a Actif net réévalué de la BRIOLAYE | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.8 b Coût d'acquisition et écart d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 1,5 |
| 1.8 c Nature, reprise et présentation de l'écart négatif | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.8 d Écritures : écarts d'évaluation et frais | `2.2.g` Écarts d'évaluation et d'acquisition | 1,5 |
| 1.9 a Partage et mise en équivalence | `2.2.h` Partage des capitaux propres | 3 |
| 1.9 b Écritures : titres, écart négatif, mise en équivalence | `2.2.h` Partage des capitaux propres | 3 |
| 1.10 a Compte de résultat consolidé | `2.3.a` Documents de synthèse consolidés | 3 |
| 1.10 b Lignes du bilan consolidé | `2.3.a` Documents de synthèse consolidés | 2 |
| 1.10 c Information sectorielle | `2.3.a` Documents de synthèse consolidés | 3 |
| 1.10 d Ce qui changerait en IFRS | `2.3.a` Documents de synthèse consolidés ; `2.1.d` Conséquences du référentiel et des méthodes | 2 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires ; `EA` = écart d'acquisition (positif) ; `EA_NEG` = écart d'acquisition négatif ; `AMO_EA` = amortissements de l'écart d'acquisition ; `DOT_EA` = ligne « dotations aux amortissements, dépréciations et reprises des écarts d'acquisition » du compte de résultat ; `TME` = titres mis en équivalence ; `QP_MEE` = résultat net lié aux entités mises en équivalence ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.LORMEVAL` : titres détenus par LORMEVAL Santé).

---

### 1.1 Obligation d'établir des comptes consolidés et référentiel (2 pts)

**Principe (0,5 pt).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. LORMEVAL Santé, société par actions simplifiée, est une société commerciale ; elle contrôle exclusivement VERNAUDIÈRE, la BRIOLAYE et ses trois autres filiales (voir 1.4) : elle entre dans le champ de l'obligation.

**Exemptions (1 pt).**
- *Société elle-même contrôlée* (L. 233-17, 1°) : l'exemption suppose que LORMEVAL Santé soit incluse dans les comptes consolidés publiés d'une entité qui la contrôle. Son capital est dispersé entre 68 médecins (2 % au plus chacun), six personnes physiques de la famille fondatrice et un fonds qui détient 12 % et n'établit pas de comptes consolidés ; aucune entité ne l'inclut dans des comptes consolidés : l'exemption est écartée [V L. 233-17 ; F03 § 1.1] (0,5 pt).
- *Ensemble qui n'est pas un « grand groupe »* (L. 233-17, 2°) : un grand groupe dépasse, à la clôture, deux des trois seuils suivants : total du bilan 30 000 000 €, chiffre d'affaires net 60 000 000 €, 250 salariés en moyenne ; les seuils sont réputés franchis à la clôture de **deux exercices consécutifs** [V L. 230-2, 3° ; D. 230-2, 2° et dernier alinéa ; F03 § 1.1]. Les trois seuils sont dépassés au 31/12/2025 (158 M€, 161 M€, 1 380 salariés) et au 31/12/2026 (171 M€, 176 M€, 1 450 salariés) : l'ensemble est un grand groupe et l'exemption ne joue pas (0,5 pt).

**Référentiel (0,5 pt).** Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que pour les sociétés dont les titres sont admis aux négociations sur un marché réglementé d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Les autres sociétés appliquent le règlement ANC n° 2020-01 ou, sur option, les IFRS adoptées [V C. com. L. 233-24 ; F03 § 1.2]. LORMEVAL Santé n'a aucun titre admis sur un marché et n'a jamais exercé l'option : elle applique le règlement ANC n° 2020-01.

---

### 1.2 Projet d'émission obligataire et normalisation internationale (3 pts)

#### a. Conséquence de l'émission (0,75 pt)

Selon l'hypothèse de l'énoncé, les IFRS s'imposent aux comptes consolidés de tout exercice à la clôture duquel des obligations du groupe sont admises sur un marché réglementé. Si l'émission a lieu en 2028, les **comptes consolidés de l'exercice 2028** (clôture au 31/12/2028) seront établis selon les **normes IFRS adoptées par l'Union européenne** ; les comptes individuels resteront établis selon le PCG (0,5 pt). Les comptes consolidés de 2026 et de 2027 restent établis selon le règlement ANC n° 2020-01, sauf option anticipée pour les IFRS [V L. 233-24 ; F03 § 1.2] (0,25 pt). Pour information (non noté) : en 2028, la présentation suivra la norme IFRS 18, qui remplace IAS 1 pour les exercices ouverts à compter du 01/01/2027 [V règlement (UE) 2026/338 ; F14 § 0].

#### b. IASB, IFRIC et EFRAG (1,25 pt)

- **IASB** : groupe indépendant d'experts au sein de l'IFRS Foundation, organisme sans but lucratif ; ses membres élaborent et publient les normes IFRS ; il approuve les interprétations [V page « International Accounting Standards Board », ifrs.org ; F03 § 7.2] (0,5 pt).
- **IFRS Interpretations Committee (IFRIC)** : il élabore les interprétations des normes IFRS, qui en précisent l'application ; ces interprétations sont approuvées par l'IASB [V même source ; F03 § 7.2] (0,25 pt).
- **EFRAG** : il veille à la prise en compte des positions européennes dans les travaux de l'IASB et conseille la Commission européenne sur la conformité des normes nouvelles ou modifiées aux critères du règlement IAS, dont l'intérêt public européen. Une norme ne s'applique dans l'Union qu'après son **adoption par un règlement de la Commission** (par exemple le règlement (UE) 2023/1803) : LORMEVAL appliquera les IFRS **adoptées** [V page « Financial reporting », efrag.org ; intitulé du règlement (UE) 2023/1803 ; F03 § 7.2] (0,5 pt).

#### c. Cadre conceptuel de l'IASB (1 pt)

- **Rôle et objectif (0,5 pt)** : le cadre conceptuel n'est pas une norme. Il énonce les concepts qui guident l'IASB dans l'élaboration des normes, aide les entités à définir leurs méthodes comptables lorsqu'aucune norme ne s'applique et aide toutes les parties à comprendre et interpréter les normes [V page « Conceptual Framework for Financial Reporting », ifrs.org ; IAS 8 § 11 ; F03 § 7.2]. L'information financière à usage général doit être **utile aux investisseurs, prêteurs et autres créanciers**, actuels et potentiels, pour leurs décisions de fourniture de ressources à l'entité [S présentation du cadre de 2018 ; F03 § 7.2]. Les souscripteurs des obligations de 2028 seront des **prêteurs** : les comptes consolidés IFRS leur seront destinés au premier chef, pour apprécier la capacité du groupe à servir les intérêts et à rembourser.
- **Grands principes (0,5 pt)** : caractéristiques qualitatives **fondamentales** de l'information utile, la **pertinence** (dont l'importance relative) et la **représentation fidèle** ; caractéristiques **auxiliaires**, la comparabilité, la vérifiabilité, la rapidité et la compréhensibilité [S présentation du cadre de 2018 ; F03 § 7.2]. Le cadre définit aussi l'entité présentant l'information, les actifs, passifs, capitaux propres, produits et charges, les critères de comptabilisation et de décomptabilisation et les bases d'évaluation [V ifrs.org ; F03 § 7.2].

---

### 1.3 Processus de consolidation (2 pts)

L'intégration globale comprend l'intégration des comptes après retraitements, la répartition des capitaux propres et du résultat entre le groupe et les intérêts minoritaires, et l'élimination des opérations internes ; la mise en équivalence substitue aux titres la quote-part des capitaux propres retraités [V ANC art. 221-2 et 221-4, p. 18-19 ; F03 § 3].

| Ordre | Tâche | Objet | Travaux du dossier |
|---|---|---|---|
| 1 | C | Fixer le cadre commun : périmètre et méthodes, calendrier, règles du manuel, format des données | 1.4 |
| 2 | B | Disposer de comptes individuels arrêtés et d'informations homogènes pour chaque société | — |
| 3 | E | Identifier les opérations entre sociétés du groupe et faire concorder les montants réciproques avant leur élimination | 1.7 (montants de l'annexe 1.5) |
| 4 | D | Passer des comptes individuels aux comptes retraités selon les méthodes du groupe ; évaluer les actifs et passifs identifiables des sociétés acquises | 1.5, 1.6, 1.8 a et d |
| 5 | F | Additionner les comptes retraités des sociétés intégrées globalement (aucun cumul pour RADIOLANE) | réalisé par le service (annexe 1.8) |
| 6 | G | Supprimer les opérations internes : soldes réciproques, flux réciproques, dividendes, résultats internes | 1.7 |
| 7 | A | Éliminer les titres, constater les écarts d'acquisition, partager les capitaux propres, mettre en équivalence | 1.8 b et c, 1.9 |
| 8 | H | Produire les états de synthèse et l'annexe consolidés ; contrôler leur cohérence | 1.10 |

(1 pt pour l'ordre ; 1 pt pour l'objet des tâches et leur rattachement aux questions.)

---

### 1.4 Périmètre et méthodes (1 pt)

**Tableau (0,5 pt : VERNAUDIÈRE et BRIOLAYE 0,25 ; RADIOLANE 0,25)**

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt |
|---|---|---|---|---|
| LORMEVAL Santé | — | Société consolidante | — | 100 % |
| VERNAUDIÈRE | 100 % | Exclusif | Intégration globale | 100 % |
| BRIOLAYE | 80 % | Exclusif | Intégration globale | 80 % (minoritaires 20 %) |
| RADIOLANE | 30 % | Influence notable | Mise en équivalence | 30 % |

**Justification pour RADIOLANE (0,5 pt).** LORMEVAL Santé détient 30 % des droits de vote, plus de 20 % : l'influence notable est présumée [V ANC art. 211-5, p. 13 ; F03 § 2]. Elle n'a pas le contrôle exclusif : pas de majorité des droits de vote, ni plus de 40 % (seuil de présomption de l'art. 211-3), deux membres sur sept au comité de direction [V art. 211-3, p. 12-13]. Aucun accord ne prévoit un partage du contrôle avec les radiologues ni l'unanimité des décisions [V art. 211-4, p. 13]. Les indices confirment l'influence notable : représentation au comité de direction (deux membres sur sept) et liens d'activité étroits avec VERNAUDIÈRE, dont RADIOLANE examine les patients hospitalisés. D'où la mise en équivalence [V art. 221-1, p. 18 ; F03 § 3].

---

### 1.5 Provision pour hausse des prix de VERNAUDIÈRE (4 pts)

**Justification (1 pt).** L'incidence des écritures passées pour la seule application des législations fiscales est éliminée ; la constitution et la reprise de provisions réglementées en sont un exemple [V ANC art. 272-1 et son commentaire IR4, p. 53 ; F04 R1] ; le manuel du groupe le rappelle. La provision pour hausse des prix (compte 143) ne correspond à aucune dépréciation des stocks : elle permet seulement de différer l'imposition d'une partie du résultat. Ses dotations ayant été déduites et ses reprises imposées, son élimination fait apparaître une différence temporaire imposable : les capitaux propres consolidés dépassent la base fiscale. D'où un **impôt différé passif** [V art. 272-8, p. 57 ; F04 R1].

**Tableau des incidences (1 pt)**

| | Ouverture (01/01/2026) | Variation 2026 | Clôture (31/12/2026) |
|---|---:|---:|---:|
| Provision pour hausse des prix (comptes individuels) | 160 000 | + 52 000 – 32 000 = 20 000 | 180 000 |
| Provision pour hausse des prix (comptes consolidés) | 0 | 0 | 0 |
| **Écart (capitaux propres consolidés plus élevés)** | **160 000** | **20 000** | **180 000** |
| Impôt différé passif (25 %) | – 40 000 | – 5 000 | **– 45 000** |
| **Net** | **120 000** (réserves) | **15 000** (résultat) | 135 000 |

(Ouverture et net en réserves : 0,25 pt ; variation, impôt et net en résultat : 0,5 pt ; clôture et impôt différé passif : 0,25 pt.)

**R1 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 143 Provisions réglementées pour hausse de prix | 180 000 | |
| RSV.VERNAUDIERE Réserves VERNAUDIÈRE | | 120 000 |
| RST.VERNAUDIERE Résultat VERNAUDIÈRE | | 15 000 |
| IDP Impôt différé passif | | 45 000 |
| *Élimination de la provision pour hausse des prix de VERNAUDIÈRE* | **180 000** | **180 000** |

**R1R (compte de résultat, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 7873 Reprises sur provisions réglementées (stocks) | 32 000 | |
| CH_ID Charge d'impôt différé | 5 000 | |
| RES_CR Résultat | 15 000 | |
| 6873 Dotations aux provisions réglementées (stocks) | | 52 000 |
| *Élimination de la dotation et de la reprise de 2026* | **52 000** | **52 000** |

Les comptes 687 et 787 relèvent des charges et produits exceptionnels [V liste des comptes du PCG 2026] : l'élimination modifie le résultat exceptionnel consolidé (1.10 a).

**Incidence d'ouverture (0,5 pt).** La consolidation repart chaque année des comptes individuels. Or le solde du compte 143 au 01/01/2026 (160 000 €) a réduit les résultats des exercices 2020 à 2025, qui figurent déjà dans les réserves : son élimination, nette d'impôt (120 000 €), corrige donc les **réserves**, et non le résultat de 2026, qui n'enregistre que la variation de l'exercice (15 000 € nets). VERNAUDIÈRE étant détenue à 100 % depuis sa création, ces réserves reviennent en totalité au groupe.

---

### 1.6 Crédit-bail du robot chirurgical (5 pts)

**Justification (1 pt).**
- Les contrats de crédit-bail sont comptabilisés chez le preneur, au bilan, sous forme d'une immobilisation et d'un emprunt et, au compte de résultat, sous forme d'une dotation aux amortissements et d'une charge financière [V ANC art. 272-2, p. 53 ; F04 R2]. Le contrat de VERNAUDIÈRE, conclu avec une société de financement et assorti d'une option d'achat, est un contrat de crédit-bail : le retraitement s'impose, conformément au manuel (0,5 pt).
- **Durée d'amortissement** : l'option d'achat est faible (50 124 €, 2,5 % de la valeur du robot), VERNAUDIÈRE prévoit de la lever et compte utiliser le robot jusqu'à la fin de 2032. Le transfert de propriété étant probable, le manuel impose la durée d'utilisation du groupe, **8 ans**, et non la durée du contrat (5 ans) : dotation annuelle 2 000 000 / 8 = **250 000 €** (0,25 pt).
- **Impôt différé** : les redevances ont été déduites fiscalement. Les charges consolidées (amortissement et intérêts) étant inférieures aux redevances en 2025 et en 2026, la valeur nette du robot dépasse la dette : la différence temporaire est imposable, d'où un **impôt différé passif** [V art. 272-8, p. 57 ; F04 R2] (0,25 pt).

**Tableau des incidences (1,5 pt)**

| | 2025 (réserves) | 2026 (résultat) | Cumul au 31/12/2026 |
|---|---:|---:|---:|
| Redevance annulée | + 440 000 | + 440 000 | + 880 000 |
| Dotation aux amortissements | – 250 000 | – 250 000 | – 500 000 |
| Intérêts (tableau du crédit-bailleur) | – 80 000 | – 65 600 | – 145 600 |
| **Écart avant impôt** | **+ 110 000** | **+ 124 400** | **+ 234 400** |
| Impôt différé passif (25 %) | – 27 500 | – 31 100 | – 58 600 |
| **Net** | **82 500** | **93 300** | 175 800 |

Contrôle au 31/12/2026 : valeur nette du robot 2 000 000 – 500 000 = 1 500 000 € ; capital restant dû 1 265 600 € ; écart 234 400 €.

(Annulation des redevances et amortissements : 0,5 pt ; intérêts de chaque année : 0,5 pt ; impôt différé et répartition réserves / résultat : 0,5 pt.)

**R2 (bilan, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2154 Matériels industriels (robot chirurgical) | 2 000 000 | |
| 2815 Amortissements des installations, matériel et outillage industriels | | 500 000 |
| 168 Autres emprunts et dettes assimilées (dette de crédit-bail) | | 1 265 600 |
| IDP Impôt différé passif | | 58 600 |
| RSV.VERNAUDIERE Réserves VERNAUDIÈRE | | 82 500 |
| RST.VERNAUDIERE Résultat VERNAUDIÈRE | | 93 300 |
| *Retraitement du crédit-bail du robot chirurgical* | **2 000 000** | **2 000 000** |

**R2R (compte de résultat, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 68112 Dotations aux amortissements des immobilisations corporelles | 250 000 | |
| 6611 Intérêts des emprunts et dettes | 65 600 | |
| CH_ID Charge d'impôt différé | 31 100 | |
| RES_CR Résultat | 93 300 | |
| 6122 Crédit-bail mobilier | | 440 000 |
| *Retraitement de la redevance de 2026* | **440 000** | **440 000** |

---

### 1.7 Opérations internes (4 pts)

#### a. Redevances de services centraux (1 pt)

Les produits et charges réciproques, ainsi que les créances et dettes réciproques, sont éliminés en totalité ; ces éliminations sont sans incidence sur le résultat consolidé [V ANC art. 251-1, p. 45 ; F04 R14]. Les redevances sont des charges de l'exercice pour les cliniques : aucun résultat interne ne reste dans un actif (0,25 pt).

**I1 (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 706 Prestations de services (LORMEVAL Santé) | 2 100 000 | |
| 6228 Divers (VERNAUDIÈRE 1 500 000 ; BRIOLAYE 600 000) | | 2 100 000 |
| *Élimination des redevances de services centraux* | **2 100 000** | **2 100 000** |

**I1B (bilan, 0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4011 Fournisseurs (BRIOLAYE) | 150 000 | |
| 4111 Clients (LORMEVAL Santé) | | 150 000 |
| *Élimination de la créance et de la dette réciproques* | **150 000** | **150 000** |

#### b. Compte courant (1 pt)

Intérêts de 2026 : 800 000 × 2,5 % × 6/12 = **10 000 €**, portés au compte courant, dont le solde atteint **810 000 €** au 31/12/2026 dans les deux sociétés. La créance de LORMEVAL Santé et la dette de la BRIOLAYE, ainsi que le produit et la charge d'intérêts, s'éliminent sans incidence sur le résultat consolidé [V art. 251-1, p. 45] (0,25 pt).

**I2 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 451 Groupe (dette de la BRIOLAYE) | 810 000 | |
| 451 Groupe (créance de LORMEVAL Santé) | | 810 000 |
| *Élimination du compte courant* | **810 000** | **810 000** |

**I2R (compte de résultat, 0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 768 Autres produits financiers (LORMEVAL Santé) | 10 000 | |
| 6615 Intérêts des comptes courants et des dépôts créditeurs (BRIOLAYE) | | 10 000 |
| *Élimination des intérêts du compte courant* | **10 000** | **10 000** |

#### c. Dividendes (2 pts)

- **VERNAUDIÈRE (0,75 pt)** : les dividendes reçus d'une société consolidée sont éliminés en totalité [V ANC art. 251-2, p. 45 ; F04 R14]. Ils ne font que transférer à LORMEVAL Santé une partie du résultat de 2025 de VERNAUDIÈRE, déjà compris dans les réserves consolidées : les laisser dans le résultat de 2026 le compterait deux fois. Le dividende (1 000 000 €) sort du résultat de LORMEVAL Santé et rejoint les réserves.
- **RADIOLANE (0,75 pt)** : LORMEVAL Santé a reçu 30 % × 200 000 = **60 000 €**. Les dividendes reçus des entités mises en équivalence sont éliminés du compte de résultat de l'entité qui détient les titres et portés en augmentation des réserves consolidées [V ANC art. 262-3, p. 49 ; F05 § 4] : la quote-part du groupe dans le résultat de 2025 de RADIOLANE figure déjà dans les réserves par la mise en équivalence, et la distribution réduit d'autant les capitaux propres de RADIOLANE, donc la valeur des titres mis en équivalence.
- **Écritures (0,5 pt)** :

**I3 (bilan)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.LORMEVAL Résultat LORMEVAL Santé | 1 060 000 | |
| RSV.LORMEVAL Réserves LORMEVAL Santé | | 1 060 000 |
| *Élimination des dividendes de VERNAUDIÈRE (1 000 000) et de RADIOLANE (60 000)* | **1 060 000** | **1 060 000** |

**I3R (compte de résultat)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 7611 Revenus des titres de participation | 1 060 000 | |
| RES_CR Résultat | | 1 060 000 |
| *Élimination des dividendes reçus* | **1 060 000** | **1 060 000** |

---

### 1.8 Acquisition de la BRIOLAYE (8 pts)

#### a. Actif net réévalué au 01/01/2026 (2,5 pts)

| Élément | Montant |
|---|---:|
| Capitaux propres individuels au 01/01/2026 (0,25) | 2 000 000 |
| Écart d'évaluation du terrain (500 000 – 200 000) | + 300 000 |
| Écart d'évaluation du bâtiment (1 800 000 – 1 300 000) | + 500 000 |
| Impôt différé passif sur les écarts ((300 000 + 500 000) × 25 %) (écarts et impôt : 0,75) | – 200 000 |
| Marque « Clinique de la BRIOLAYE » (non comptabilisée, voir ci-dessous) (1) | 0 |
| **Actif net réévalué** (0,25) | **2 600 000** |

- **Écarts d'évaluation** : différence entre la valeur d'entrée des actifs identifiables et leur valeur comptable [V ANC art. 231-9, p. 22 ; F05 § 1.2] ; les impôts différés sur ces écarts sont comptabilisés, en contrepartie de l'écart d'acquisition [V art. 232-1, p. 24 ; art. 272-13, p. 59 ; F05 § 1.2].
- **Marque (1 pt)** : une marque peut être un élément identifiable de l'actif de l'entité acquise, même si celle-ci ne l'a pas comptabilisée [V art. 231-7, p. 21-22 ; F05 § 1.2]. Mais les actifs incorporels identifiés qui ne peuvent pas être évalués par référence à un marché actif ne sont pas comptabilisés s'ils conduisent à créer ou à augmenter un écart d'acquisition négatif [V art. 231-12, p. 24 ; F05 § 1.3]. La marque n'a pas de marché actif ; sans elle, l'écart d'acquisition est déjà négatif (– 620 000 €, voir b). La comptabiliser (240 000 €, moins un impôt différé de 60 000 €) l'augmenterait de 80 % × 180 000 = 144 000 €, à – 764 000 €. Elle **n'est donc pas comptabilisée**.
- **Plan de redressement (0,25 pt)** : ses coûts ne réduisent pas l'actif net acquis. Une provision pour restructuration n'est comptabilisée à l'acquisition que si les conditions de comptabilisation sont réunies au plus tard à cette date [V commentaire IR3 sous art. 231-7, p. 22 ; F05 § 8], ce que l'énoncé exclut. Ces coûts pèseront sur les résultats de 2026 et de 2027.

#### b. Frais d'acquisition, coût d'acquisition et écart d'acquisition (1,5 pt)

- **Frais (0,5 pt)** : dans ses comptes individuels, LORMEVAL Santé a comptabilisé les honoraires en charges, option permise par le PCG [V PCG art. 121-5 ; F05 § 1.1], et les a déduits fiscalement. En consolidation, le coût d'acquisition comprend les coûts directement imputables à l'acquisition, dont les honoraires des consultants et experts, **nets de l'économie d'impôt** correspondante [V ANC art. 231-2 et 231-3, p. 20-21 ; F05 § 1.1].
- **Coût d'acquisition (0,5 pt)** : 1 400 000 + 80 000 × 75 % = **1 460 000 €**. Le calcul faux le plus fréquent retient le prix seul (1 400 000 €) ou les frais bruts (1 480 000 €) (`JUR-G02`).
- **Écart d'acquisition (0,5 pt)** : 1 460 000 – 80 % × 2 600 000 = 1 460 000 – 2 080 000 = **– 620 000 €**, soit un **écart d'acquisition négatif** de 620 000 € [V art. 231-9, p. 22].

#### c. Nature, reprise et présentation de l'écart négatif (2,5 pts)

- **Nature (1 pt)** : un écart d'acquisition négatif correspond généralement soit à un gain potentiel, si l'acquisition a été effectuée dans des **conditions avantageuses**, soit à une **rentabilité insuffisante** de l'entité acquise [V commentaire IR4 sous art. 231-12, p. 24 ; F05 § 8]. Les évaluations ont été réexaminées et confirmées : l'écart n'est pas une erreur d'évaluation. Le prix a été fixé d'après la rentabilité de la clinique, en tenant compte des pertes prévues par le plan, coûts de sa mise en œuvre compris (450 000 € en 2026, 325 000 € en 2027). La part du groupe dans ces pertes prévues, 80 % × 775 000 = 620 000 €, est égale à l'écart : il traduit en totalité la rentabilité insuffisante attendue. La hâte du vendeur explique qu'il ait accepté ce prix sans mise en concurrence, mais l'écart traduit d'abord la **rentabilité insuffisante** de la BRIOLAYE pendant le redressement, et non un gain. La reprise immédiate, réservée aux acquisitions dans des conditions avantageuses [V IR3 sous art. 231-12, p. 24], est donc écartée.
- **Durée et reprise de 2026 (0,75 pt)** : l'écart est rapporté au résultat sur une durée qui reflète les hypothèses retenues et les conditions déterminées lors de l'acquisition [V art. 231-12, p. 24 ; F05 § 1.3]. Les pertes attendues portent sur les deux années du plan, 2026 et 2027 : la durée est de **2 ans** et, selon le manuel, la reprise est linéaire à compter du 01/01/2026. Reprise de 2026 : 620 000 / 2 = **310 000 €** ; solde au 31/12/2026 : 310 000 €, repris en 2027. La reprise compense dans le résultat consolidé les pertes que le prix avait anticipées ; la perte réelle de 2026 (300 000 € dans les comptes individuels, part du groupe de la perte retraitée 252 000 €, voir 1.9 a) est moins forte que prévu, ce qui ne modifie ni la durée ni le montant de la reprise, fixés lors de l'acquisition.
- **Présentation (0,75 pt)** : au bilan, l'écart négatif est inscrit **en comptes de régularisation au passif** [V art. 231-12, p. 24], à la rubrique « autres dettes et comptes de régularisation », ligne « dont écarts d'acquisition négatifs » du modèle [V art. 281-1, p. 66 ; F14 § 1.2] ; il ne figure ni dans les capitaux propres, ni dans les provisions. Au compte de résultat, la reprise figure sur la ligne du résultat d'exploitation prévue pour les dotations aux amortissements, dépréciations et reprises des écarts d'acquisition des entités intégrées, entre le résultat d'exploitation « avant » et « après » ces dotations et reprises [V IR3 sous art. 231-12, p. 24 ; art. 281-2, p. 67 ; F05 § 1.3]. L'écart étant calculé sur la seule part de l'acquéreur, sa reprise revient en totalité au **groupe**.

#### d. Écritures : écarts d'évaluation et frais d'acquisition (1,5 pt)

Amortissement de 2026 de l'écart sur le bâtiment : 500 000 / 25 = 20 000 € ; impôt différé passif au 31/12/2026 : (300 000 + 500 000 – 20 000) × 25 % = 195 000 €.

**P1 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2111 Terrains nus | 300 000 | |
| 2131 Bâtiments | 500 000 | |
| RST.BRIOLAYE Résultat BRIOLAYE (20 000 × 75 %) | 15 000 | |
| 2813 Amortissements des constructions | | 20 000 |
| IDP Impôt différé passif | | 195 000 |
| RSV.BRIOLAYE Réserves BRIOLAYE (800 000 × 75 %) | | 600 000 |
| *Écarts d'évaluation de la BRIOLAYE et amortissement de 2026* | **815 000** | **815 000** |

**P1R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 68112 Dotations aux amortissements des immobilisations corporelles | 20 000 | |
| CH_ID Produit d'impôt différé | | 5 000 |
| RES_CR Résultat | | 15 000 |
| *Amortissement de l'écart d'évaluation du bâtiment* | **20 000** | **20 000** |

**P2 (bilan, 0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation BRIOLAYE (80 000 × 75 %) | 60 000 | |
| RST.LORMEVAL Résultat LORMEVAL Santé | | 60 000 |
| *Incorporation des frais d'acquisition nets d'impôt au coût des titres* | **60 000** | **60 000** |

**P2R (compte de résultat, 0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 695 Impôts sur les bénéfices (économie d'impôt incorporée au coût des titres) | 20 000 | |
| RES_CR Résultat | 60 000 | |
| 6226 Honoraires | | 80 000 |
| *Annulation des frais d'acquisition des titres BRIOLAYE* | **80 000** | **80 000** |

---

### 1.9 Partage des capitaux propres et mise en équivalence (6 pts)

#### a. Tableaux au 31/12/2026 (3 pts)

**Partage des capitaux propres de la BRIOLAYE (1,75 pt)**

Résultat retraité de 2026 : – 300 000 – 20 000 + 5 000 = **– 315 000 €** (0,25).

| | Total | Groupe (80 %) | Intérêts minoritaires (20 %) |
|---|---:|---:|---:|
| Capital | 1 500 000 | 1 200 000 | 300 000 |
| Réserves et report à nouveau (900 000 – 400 000) | 500 000 | 400 000 | 100 000 |
| Écarts d'évaluation nets d'impôt différé (au 01/01/2026) | 600 000 | 480 000 | 120 000 |
| **Capitaux propres retraités hors résultat** | **2 600 000** | **2 080 000** | **520 000** |
| Élimination des titres (coût d'acquisition) | | – 1 460 000 | |
| Écart d'acquisition négatif (inscrit au passif) | | – 620 000 | |
| **Réserves consolidées** | | **0** | |
| Résultat retraité de 2026 | – 315 000 | – 252 000 | – 63 000 |
| **Intérêts minoritaires au 31/12/2026** | | | **457 000** |

(Capitaux propres retraités et écarts d'évaluation : 0,5 ; titres et écart négatif : 0,5 ; résultat et intérêts minoritaires : 0,5.)

- Les droits des minoritaires sont calculés sur l'actif net réévalué [V ANC art. 232-1, p. 24 ; F05 § 1.2] : ils reçoivent 20 % des écarts d'évaluation.
- Acquise le 01/01/2026, la BRIOLAYE n'apporte aucune réserve consolidée au groupe : la différence entre la quote-part des capitaux propres acquis et le coût des titres est l'écart d'acquisition négatif.
- Les minoritaires supportent leur part de la perte ; leurs intérêts restant positifs, l'imputation des pertes excédentaires aux majoritaires ne joue pas [V art. 252-1, p. 46 ; F05 § 3].

**Mise en équivalence de RADIOLANE (1,25 pt)**

| | Montant |
|---|---:|
| Écart d'acquisition au 01/01/2024 : 1 050 000 – 30 % × 3 000 000 (0,25) | 150 000 |
| Capitaux propres de RADIOLANE au 31/12/2026 | 3 900 000 |
| **Valeur d'équivalence** (30 %) (0,25) | **1 170 000** |
| Titres éliminés (coût 1 050 000 – écart d'acquisition 150 000) | – 900 000 |
| Écart : réserves consolidées (30 % × (2 400 000 – 2 000 000)) + résultat de 2026 (30 % × 500 000) (0,25) | 120 000 + 150 000 |
| Amortissement de l'écart d'acquisition : 150 000 / 10 = 15 000 par an ; cumul au 31/12/2026 45 000 (2024-2025 : 30 000 en réserves ; 2026 : 15 000 en résultat) (0,25) | – 45 000 |
| **Écart d'acquisition net au 31/12/2026** | **105 000** |
| Quote-part du groupe : réserves 120 000 – 30 000 = 90 000 ; résultat 150 000 – 15 000 = 135 000 (0,25) | |

Les valeurs d'entrée des actifs et passifs de RADIOLANE étant égales à leur valeur comptable, aucun écart d'évaluation n'est à prendre en compte. L'écart d'acquisition d'une entité mise en équivalence est présenté selon les mêmes modalités qu'en intégration globale, et ses dotations figurent sur la ligne du résultat des entités mises en équivalence [V ANC art. 262-2 et 262-3, p. 49 ; F05 § 4] (`JUR-G03`).

#### b. Écritures (3 pts)

**P3 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.BRIOLAYE Capital BRIOLAYE | 1 500 000 | |
| RSV.BRIOLAYE Réserves et report à nouveau BRIOLAYE retraités | 1 100 000 | |
| RST_G Résultat consolidé – part du groupe (80 % × – 315 000) | 252 000 | |
| RST_M Intérêts minoritaires – résultat (20 % × – 315 000) | 63 000 | |
| RST.BRIOLAYE Résultat BRIOLAYE retraité (perte) | | 315 000 |
| 261 Titres de participation BRIOLAYE (1 400 000 + 60 000) | | 1 460 000 |
| EA_NEG Écart d'acquisition négatif | | 620 000 |
| RSV_M Intérêts minoritaires – capital et réserves | | 520 000 |
| *Élimination des titres BRIOLAYE et partage des capitaux propres* | **2 915 000** | **2 915 000** |

**P4 (bilan) et P4R (compte de résultat), 0,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| EA_NEG Écart d'acquisition négatif | 310 000 | |
| RST_G Résultat consolidé – part du groupe | | 310 000 |
| *P4 – Reprise de 2026 de l'écart d'acquisition négatif* | **310 000** | **310 000** |
| RES_CR Résultat | 310 000 | |
| DOT_EA Dotations aux amortissements, dépréciations et reprises des écarts d'acquisition (reprise) | | 310 000 |
| *P4R – Reprise de l'écart négatif au résultat d'exploitation* | **310 000** | **310 000** |

**P5, P6 et P6R (1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| EA Écart d'acquisition RADIOLANE | 150 000 | |
| 261 Titres de participation RADIOLANE | | 150 000 |
| *P5 – Reclassement de l'écart d'acquisition* | **150 000** | **150 000** |
| TME Titres mis en équivalence | 1 170 000 | |
| 261 Titres de participation RADIOLANE (1 050 000 – 150 000) | | 900 000 |
| RSV_G Réserves consolidées – part du groupe | | 120 000 |
| RST_G Résultat consolidé – part du groupe | | 150 000 |
| *P6 – Mise en équivalence des titres RADIOLANE* | **1 170 000** | **1 170 000** |
| RES_CR Résultat | 150 000 | |
| QP_MEE Résultat net lié aux entités mises en équivalence | | 150 000 |
| *P6R – Quote-part de résultat de RADIOLANE* | **150 000** | **150 000** |

**P7 et P7R (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RSV_G Réserves consolidées – part du groupe (2024 et 2025) | 30 000 | |
| RST_G Résultat consolidé – part du groupe (2026) | 15 000 | |
| AMO_EA Amortissements de l'écart d'acquisition | | 45 000 |
| *P7 – Amortissement de l'écart d'acquisition de RADIOLANE* | **45 000** | **45 000** |
| QP_MEE Résultat net lié aux entités mises en équivalence (amortissement) | 15 000 | |
| RES_CR Résultat | | 15 000 |
| *P7R – Dotation de 2026, sur la ligne des entités mises en équivalence* | **15 000** | **15 000** |

---

### 1.10 Documents de synthèse (10 pts)

#### a. Compte de résultat consolidé de 2026, extrait (3 pts)

Modèle par nature du règlement ANC [V art. 281-2, p. 67 ; F14 § 1.3].

| Ligne du modèle | Calcul | Montant |
|---|---|---:|
| Chiffre d'affaires | 178 100 000 – 2 100 000 (redevances, I1) | **176 000 000** (0,25) |
| Résultat d'exploitation avant dotations aux amortissements, dépréciations et reprises des écarts d'acquisition | 9 150 000 + 440 000 (redevance annulée) – 250 000 (amortissement du robot) + 80 000 (frais d'acquisition annulés) – 20 000 (écart sur le bâtiment) ; redevances de services : sans incidence | **9 400 000** (0,5) |
| Dotations aux amortissements, dépréciations et reprises des écarts d'acquisition | reprise de l'écart négatif de la BRIOLAYE (P4R) | **+ 310 000** (0,5) |
| Résultat d'exploitation après dotations aux amortissements, dépréciations et reprises des écarts d'acquisition | | **9 710 000** (0,25) |
| Charges et produits financiers | 420 000 – 65 600 (intérêts du crédit-bail) – 1 060 000 (dividendes, I3R) ; intérêts du compte courant : sans incidence | **– 705 600** (0,25) |
| Charges et produits exceptionnels | – 180 000 + 52 000 – 32 000 (provision pour hausse des prix, R1R) | **– 160 000** (0,25) |
| Impôts sur les résultats | – 2 350 000 – 20 000 (P2R) – 5 000 (R1R) – 31 100 (R2R) + 5 000 (P1R) | **– 2 401 100** (0,25) |
| **Résultat net des entités intégrées** | | **6 443 300** (0,25) |
| Résultat net lié aux entités mises en équivalence | 150 000 – 15 000 (amortissement de l'écart d'acquisition de RADIOLANE) | **135 000** (0,25) |
| **Résultat net de l'ensemble consolidé** | | **6 578 300** |
| Intérêts minoritaires | 20 % × (– 315 000) : quote-part de perte | **– 63 000** |
| **Résultat net (part du groupe)** | 6 578 300 + 63 000 | **6 641 300** |

(0,25 pt pour les trois dernières lignes.)

Contrôle : résultat net cumulé 7 040 000 + 15 000 (R1) + 93 300 (R2) + 60 000 (P2) – 1 060 000 (I3) – 15 000 (P1) + 310 000 (P4) + 135 000 (RADIOLANE) = 6 578 300 €. Les lignes du résultat par action, facultatives pour une société dont aucun instrument n'est négocié sur Euronext Growth, ne sont pas présentées [V art. 281-2, note 4, p. 67 ; F14 § 1.4].

#### b. Lignes du bilan consolidé au 31/12/2026 (2 pts)

Modèle du règlement ANC [V art. 281-1, p. 66 ; F14 § 1.2].

| Élément | Montant | Rubrique |
|---|---:|---|
| Écart d'acquisition de RADIOLANE | 150 000 – 45 000 = **105 000** | Actif immobilisé, immobilisations incorporelles, « dont écarts d'acquisition positifs » (0,25) |
| Titres mis en équivalence | **1 170 000** | Actif immobilisé, titres mis en équivalence (0,25) |
| Écart d'acquisition négatif de la BRIOLAYE | 620 000 – 310 000 = **310 000** | Dettes, autres dettes et comptes de régularisation, « dont écarts d'acquisition négatifs » (0,5) |
| Intérêts minoritaires | **457 000** | Rubrique distincte, après les capitaux propres part du groupe et avant les autres fonds propres, provisions et dettes (0,5) |
| Impôts différés passifs | 45 000 + 58 600 + 195 000 = **298 600** | Dettes, autres dettes et comptes de régularisation, « dont impôts différés passifs » (0,25) |
| Robot chirurgical et dette | **1 500 000** (brut 2 000 000, amortissements 500 000) ; dette **1 265 600** | Immobilisations corporelles ; emprunts et dettes financières (0,25) |

#### c. Information sectorielle (3 pts)

- **Segmentation (0,5 pt)** : un secteur d'activité est un ensemble homogène de produits, services ou métiers individualisé au sein du groupe ; la segmentation devrait être issue de l'organisation interne [V ANC art. 282-9, p. 77 ; F14 § 1.4]. La direction pilote le groupe par pôle, avec un directeur, des tableaux de bord et un budget par pôle : les secteurs sont le **MCO** et le **SSR**. L'annexe doit ventiler au minimum le **chiffre d'affaires net** par secteur d'activité et par zone géographique [V art. 282-10, p. 77] ; aucun instrument de LORMEVAL n'étant négocié sur Euronext Growth, les informations supplémentaires de l'art. 282-11 ne sont pas exigées.
- **Calcul (1,5 pt, dont LORMEVAL Santé et RADIOLANE 0,5)** :

| Secteur | Chiffre d'affaires consolidé | % |
|---|---:|---:|
| MCO : 62 000 000 – 300 000 (analyses facturées à LES CORMIERS) + 21 500 000 + 48 000 000 | **131 200 000** | 74,5 % |
| SSR : 26 000 000 + 18 800 000 | **44 800 000** | 25,5 % |
| **Total = chiffre d'affaires consolidé** | **176 000 000** | 100 % |

(MCO : 0,5 ; élimination des 300 000 € facturés entre pôles : 0,25 ; SSR : 0,25.)
  - Le chiffre d'affaires de LORMEVAL Santé (4 800 000 €) est entièrement facturé aux sociétés du groupe : il est éliminé et ne forme pas un secteur (0,25 pt).
  - RADIOLANE, mise en équivalence, n'est pas intégrée : son chiffre d'affaires (9 000 000 €) ne figure pas dans le chiffre d'affaires consolidé ni dans l'information sectorielle ; le groupe n'en retient que la quote-part de résultat (0,25 pt).
- **Zone géographique (0,5 pt)** : tous les patients sont soignés en France ; l'annexe indique une seule zone, la France, pour 176 000 000 € (100 %).
- **Présentation (0,5 pt)** : un tableau de l'annexe présente ces ventilations ; son total est rapproché du chiffre d'affaires du compte de résultat consolidé.

#### d. Ce qui changerait en IFRS (2 pts)

- **Écart d'acquisition négatif (1 pt)** : avant de constater un profit, l'acquéreur réexamine l'identification et l'évaluation des actifs acquis et des passifs repris [V IFRS 3 § 36 ; F05 § 2] ; l'excédent restant est comptabilisé **en profit dans le résultat à la date d'acquisition**, attribué à l'acquéreur [V IFRS 3 § 34 ; F05 § 2]. Il n'y aurait ni écart négatif au passif ni reprise sur deux ans : le résultat de 2026 enregistrerait la totalité du profit, celui de 2027 rien. Les frais d'acquisition seraient des charges de 2026 [V IFRS 3 § 53 ; F05 § 2] : ils ne réduiraient plus l'écart.
- **Information sectorielle (0,5 pt)** : IFRS 8 s'appliquerait aux états consolidés d'un groupe dont des instruments de dette sont négociés sur un marché [V IFRS 8 § 2 b) ; F14 § 6]. Les secteurs seraient les **secteurs opérationnels** dont les résultats sont régulièrement examinés par le principal décideur opérationnel, présentés selon les montants qui lui sont communiqués (seuils de 10 %, couverture de 75 % des produits) ; l'information porterait aussi sur le résultat sectoriel et, s'ils sont communiqués au décideur, les actifs et passifs [V IFRS 8 § 5, 11, 13, 15, 23, 25 ; F14 § 6].
- **Intérêts minoritaires (0,5 pt)** : les « participations ne donnant pas le contrôle » seraient présentées **au sein des capitaux propres**, séparément des capitaux propres attribuables aux propriétaires de la société mère [V IFRS 10 § 22 ; IAS 1 § 54 q) ; F14 § 2.2], et le résultat net serait attribué aux deux catégories [V IAS 1 § 81B]. En ANC, ils forment une rubrique distincte des capitaux propres part du groupe (1.10 b).

---

### Réponses tolérées
- **1.1** : exemption du 1° écartée au seul motif que le capital est dispersé, si l'absence de comptes consolidés incluant LORMEVAL Santé est relevée.
- **1.2 a** : comptes consolidés IFRS « à compter de 2028 » sans mention des comptes individuels ; mention des informations comparatives de 2027 à présenter en IFRS (non exigée).
- **1.3** : tâche E (rapprochement des réciproques) placée après D ou après F, si elle précède l'élimination des opérations internes (G).
- **1.5** : écritures de bilan et de compte de résultat regroupées si les réserves et le résultat sont distingués ; dotation et reprise éliminées pour leur montant net (20 000 €) au compte 6873.
- **1.6** : emprunt inscrit au compte 164 Emprunts auprès des établissements de crédit ; robot inscrit au compte 2151 ou 218 ; amortissement sur 5 ans retenu par un candidat qui justifie que la levée de l'option n'est pas certaine, si les calculs sont cohérents (dotation 400 000 € ; écart 2025 – 40 000 € et 2026 – 25 600 € ; impôt différé actif de 16 400 € au 31/12/2026 ; 0,25 pt perdu sur la justification).
- **1.7** : élimination des dividendes de VERNAUDIÈRE et de RADIOLANE par deux écritures distinctes.
- **1.8 a** : actif net réévalué présenté à partir des écarts nets d'impôt (300 000 × 75 % + 500 000 × 75 %).
- **1.8 c** : reprise immédiate de l'écart négatif, si le candidat argumente des conditions avantageuses à partir de la hâte du vendeur et en tire des calculs cohérents (logique du candidat, `JUR-F08`) : 1 pt sur 2,5 au plus, l'énoncé décrivant une rentabilité insuffisante chiffrée par le plan.
- **1.9** : partage présenté avec les réserves et le report à nouveau sur des lignes distinctes ; écart d'acquisition de RADIOLANE laissé dans les titres mis en équivalence (1 320 000 € avant amortissement, 1 275 000 € après), si sa dotation figure sur la ligne des entités mises en équivalence (0,25 pt de présentation perdu).
- **1.10 a** : intérêts minoritaires présentés en valeur positive avec la mention « quote-part de perte » et ajoutés au résultat de l'ensemble consolidé.
- **1.10 c** : ventilation géographique par département (Maine-et-Loire), si le candidat indique que le groupe n'opère qu'en France.
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (le jury valorise la logique du candidat, `JUR-F08`).

### Erreurs fréquentes
- **Obligation de consolider** : un seul exercice examiné ou seuils périmés (F99) ; exemption du 1° retenue au motif qu'un fonds détient une partie du capital.
- **Émission obligataire** : IFRS dès 2026 ou application aux comptes individuels ; normes de l'IASB appliquées sans adoption par l'Union ; rôles de l'IASB et de l'EFRAG confondus.
- **Processus** : cumul des comptes avant leurs retraitements ; élimination des titres avant l'élimination des opérations internes ; phases énumérées sans leur objet (`JUR-G01`).
- **Périmètre** : contrôle exclusif retenu pour RADIOLANE parce que les autres associés sont dispersés, alors que LORMEVAL Santé ne désigne que deux membres sur sept.
- **Provision pour hausse des prix** : incidence d'ouverture portée en résultat de 2026 ; impôt différé oublié ou inversé (`JUR-G04`, `JUR-G06`) ; écritures enregistrées au résultat d'exploitation au lieu du résultat exceptionnel ; tableau « comptes individuels / comptes consolidés » non présenté (`JUR-F05`).
- **Crédit-bail** : amortissement sur la durée du contrat malgré l'option d'achat probable ; intérêts de 2025 repris dans le résultat de 2026 ; dette inscrite pour la somme des redevances restant à payer ; impôt différé calculé sur la seule incidence de 2026 (`JUR-F07`).
- **Opérations internes** : redevances éliminées sans la créance de 150 000 € ; dividendes de RADIOLANE éliminés contre les titres mis en équivalence ou laissés en résultat ; intérêts du compte courant oubliés.
- **Coût d'acquisition** : frais d'acquisition omis ou retenus pour leur montant brut (`JUR-G02`).
- **Écart négatif** : marque comptabilisée alors qu'elle augmenterait l'écart négatif ; coûts du plan de redressement provisionnés à l'acquisition ; écart négatif inscrit en capitaux propres ou en provision ; reprise totale en 2026 sans analyse de sa nature ; reprise partagée avec les minoritaires.
- **Partage et mise en équivalence** : minoritaires calculés sur les capitaux propres non réévalués ; écart d'acquisition ou son amortissement oublié dans le tableau de mise en équivalence (`JUR-G03`) ; écritures non équilibrées (`JUR-F04`).
- **Documents de synthèse** : reprise de l'écart négatif placée en résultat exceptionnel ; quote-part de RADIOLANE incluse dans le résultat des entités intégrées ; chiffre d'affaires de RADIOLANE ou de LORMEVAL Santé retenu dans l'information sectorielle ; intérêts minoritaires présentés dans les capitaux propres en ANC.

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, référentiel, régime fiscal de faveur | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable ; `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 2 |
| 2.2 Situation de contrôle et mode d'évaluation des apports | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 2 |
| 2.3 Parité, actions à émettre, apports et prime | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer ; `1.2.d` Calculer et composer les apports | 3 |
| 2.4 Écritures chez PERFADOM | `1.3.a` Passer les écritures de base chez l'absorbante et l'absorbée | 2,5 |
| 2.5 Écritures de base chez RESPIDOM | `1.3.a` Passer les écritures de base chez l'absorbante et l'absorbée | 3,5 |
| 2.6 Écritures complémentaires chez RESPIDOM | `1.3.c` Passer les écritures complémentaires (subvention d'investissement, frais de fusion, opérations réciproques) | 8 |
| 2.7 Note au président | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 4 |
| **Total** | | **25** |

---

### 2.1 Qualification, référentiel et régime fiscal (2 pts)

**Qualification et modalités (0,5 pt).** L'opération est une **fusion-absorption** entre deux sociétés commerciales : PERFADOM transmet l'ensemble de son patrimoine à une société existante, RESPIDOM [V PCG art. 710-2 ; C. com. L. 236-1, F01 § 1]. Ses modalités :
- **transmission universelle** : RESPIDOM reçoit tous les actifs et toutes les dettes de PERFADOM, y compris son emprunt bancaire, sa dette d'impôt de la période et l'emprunt qu'elle avait contracté auprès de RESPIDOM elle-même ;
- PERFADOM est **dissoute sans liquidation** et disparaît ;
- RESPIDOM rémunère les apports par une **augmentation de capital** : elle crée des actions nouvelles qu'elle remet aux associés de PERFADOM (MÉDIOUEST Participations, Mme PENVERN et M. MASSIAC) en échange de leurs actions, selon la parité convenue.

**Référentiel et date (0,25 pt).** La fusion est enregistrée dans les comptes individuels des deux sociétés selon le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe la valeur d'inscription des apports [V PCG art. 710-1 et 720-1, F01 § 1]. La fusion prend effet à la date de sa réalisation : les écritures sont datées du **1er avril 2027**, sur la base de la situation de PERFADOM au 31 mars 2027.

**Régime fiscal de faveur (0,5 pt).** Les deux sociétés participant à la fusion sont des SAS passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1]. La fusion relève du **régime de faveur de l'art. 210 A** du CGI, qui s'applique sauf option pour le droit commun [V CGI art. 210 A ; BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1] ; le traité le retient (annexe 2.1). Ses principaux effets :
- chez PERFADOM, les plus-values latentes sur les éléments transmis (bâtiment, clientèle de prescripteurs) **ne sont pas imposées** [V CGI art. 210 A-1, F02 § 2] ; sous le régime de droit commun, la fusion serait assimilée à une cessation d'entreprise, avec imposition immédiate des bénéfices et des plus-values [V BOI-IS-FUS-10-10-10 § 1, F02 § 2] ;
- en contrepartie, RESPIDOM prend dans le traité les engagements de l'art. 210 A-3 : notamment calculer les plus-values futures sur le terrain d'après sa valeur fiscale chez PERFADOM, et inscrire les stocks à leur valeur fiscale [V CGI art. 210 A-3, F02 § 4]. Les apports étant repris à la valeur comptable, avec les valeurs brutes et les amortissements de PERFADOM, aucune plus-value n'est à réintégrer sur les biens amortissables ;
- PERFADOM n'a pas de déficit reportable : aucun agrément n'est en jeu [V CGI art. 209 II, F02 § 3].

**Résultat de la période du 1er janvier au 31 mars 2027 (0,25 pt).** Le régime de faveur ne porte que sur les plus-values et profits dégagés sur les éléments apportés. Le bénéfice de la dernière période de PERFADOM (160 000 € avant impôt) est **imposé immédiatement au nom de PERFADOM**, quel que soit le régime, par une déclaration spéciale de résultat [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2]. L'impôt correspondant (40 000 €), déjà comptabilisé, fait partie des dettes transmises : RESPIDOM le paiera.

**Solde de la subvention d'investissement (0,5 pt).** Le solde non encore réintégré de la subvention (162 000 €) serait en principe imposé chez PERFADOM lors de la fusion, soit un impôt de 162 000 × 25 % = 40 500 €. Le traité contient l'**option** par laquelle RESPIDOM reprend cette imposition : PERFADOM n'est pas imposée sur ce solde, et RESPIDOM le réintégrera dans ses résultats selon le plan d'amortissement des installations financées [V CGI art. 42 septies ; BOI-IS-FUS-10-20-40-10 § 180, F01 § 8]. Ce report n'est pas un effet automatique du régime de faveur : il résulte de l'option exercée dans le traité.

---

### 2.2 Situation de contrôle et mode d'évaluation des apports (2 pts)

**Absence de lien en capital (0,25 pt).** RESPIDOM ne détient aucune action PERFADOM, ni PERFADOM aucune action RESPIDOM (annexe 2.2). Le prêt de RESPIDOM à PERFADOM est une créance, pas une participation. Il n'y a donc ni boni ni mali, et toutes les actions PERFADOM sont rémunérées.

**Contrôle commun (0,75 pt).** MÉDIOUEST Participations détient 85 % des droits de vote de RESPIDOM et 70 % de ceux de PERFADOM (une voix par action). Elle dispose seule de la majorité des droits de vote dans chacune : elle contrôle les deux sociétés de manière **exclusive** ; aucun pacte ni droit statutaire ne donne de pouvoir particulier aux associés minoritaires [V PCG art. 741-2 ; ANC 2020-01 art. 211-3, F01 § 2.1]. Les deux sociétés sont préalablement sous le contrôle d'une **même entité mère** : l'opération est réalisée **sous contrôle commun** [V PCG art. 741-1, F01 § 2.1]. Le contrôle s'apprécie au niveau des personnes morales : que M. KERDILÈS et sa sœur détiennent MÉDIOUEST est sans incidence. Après la fusion, MÉDIOUEST détient 80,5 % de RESPIDOM (voir 2.7) : le contrôle exclusif demeure.

**Règle (0,5 pt).** En situation de contrôle commun, les apports sont évalués à la **valeur comptable**, que l'opération soit à l'endroit ou à l'envers [V PCG art. 743-1 et tableau, F01 § 2.3]. Le sens est donc sans incidence ; pour information, MÉDIOUEST, actionnaire principal de RESPIDOM, conserve le contrôle de l'absorbante : l'opération est à l'endroit. L'absence de lien en capital entre RESPIDOM et PERFADOM ne fait pas obstacle au contrôle commun : c'est le contrôle par la même mère qui le caractérise.

**Exception et valeurs d'échange (0,5 pt)**
- La valeur réelle ne s'imposerait que si l'actif net comptable apporté était insuffisant pour libérer l'augmentation de capital [V PCG art. 743-3, F01 § 2.4]. Ici, l'actif net comptable apporté (1 950 000 €) excède largement l'augmentation de capital (600 000 €, voir 2.3) : l'exception ne joue pas (0,25 pt).
- Les valeurs d'échange fournies par l'expert (8 400 000 € et 3 600 000 €) servent seulement à calculer la parité : les règles d'évaluation des apports ne visent pas celles du calcul de la parité [V PCG art. 740-1, F01 § 1]. La clientèle de prescripteurs et la plus-value latente sur le bâtiment de PERFADOM ne sont pas inscrites chez RESPIDOM (0,25 pt).

---

### 2.3 Parité, actions à émettre, apports et prime de fusion (3 pts)

**Valeurs unitaires et parité (0,75 pt)**
- RESPIDOM : 8 400 000 / 70 000 = **120 €** par action ;
- PERFADOM : 3 600 000 / 20 000 = **180 €** par action ;
- rapport d'échange : 180 / 120 = 3 / 2, soit **3 actions RESPIDOM pour 2 actions PERFADOM** [F01 § 4].

**Caractère équitable (0,25 pt).** Deux actions PERFADOM valent 2 × 180 = 360 € et trois actions RESPIDOM valent 3 × 120 = 360 € : les valeurs échangées sont égales, sans soulte. Pour l'ensemble : 20 000 × 180 = 30 000 × 120 = **3 600 000 €**. Après la fusion, RESPIDOM vaut 8 400 000 + 3 600 000 = 12 000 000 € pour 100 000 actions, soit toujours 120 € par action : aucun groupe d'associés ne s'enrichit au détriment de l'autre.

**Actions à émettre (0,5 pt).** Toutes les actions PERFADOM sont rémunérées (aucune détention par RESPIDOM) : 20 000 × 3 / 2 = **30 000 actions RESPIDOM**. Les nombres d'actions de chaque associé de PERFADOM sont pairs (14 000, 4 000, 2 000) : il n'y a pas de rompu.

**Augmentation de capital (0,25 pt).** 30 000 × 20 = **600 000 €**.

**Composition des apports (0,5 pt).** RESPIDOM reprend chaque actif et chaque passif pour sa valeur dans les comptes de PERFADOM au 31 mars 2027, en distinguant les **valeurs brutes et les amortissements** [V PCG art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2]. Les deux sociétés ayant les mêmes méthodes comptables, aucun ajustement préalable n'est nécessaire [V PCG art. 744-3, F01 § 3.2].

| Élément apporté | Valeur brute | Amortissements | Valeur apportée |
|---|---:|---:|---:|
| Terrain | 120 000 | | 120 000 |
| Bâtiment (plateforme de Saint-Nazaire) | 900 000 | 270 000 | 630 000 |
| Installations de stockage à température dirigée | 600 000 | 195 000 | 405 000 |
| Matériel de perfusion | 1 500 000 | 700 000 | 800 000 |
| Stocks de consommables | 280 000 | | 280 000 |
| Clients | 760 000 | | 760 000 |
| Disponibilités | 156 000 | | 156 000 |
| **Total de l'actif apporté** | **4 316 000** | **1 165 000** | **3 151 000** |
| Emprunt auprès de RESPIDOM | | | – 400 000 |
| Intérêts courus sur l'emprunt auprès de RESPIDOM | | | – 6 000 |
| Emprunts bancaires | | | – 450 000 |
| Fournisseurs | | | – 210 000 |
| Dettes sociales | | | – 95 000 |
| État – impôt sur les bénéfices de la période | | | – 40 000 |
| **Actif net comptable apporté** | | | **1 950 000** |

**Actif net apporté (0,5 pt).** 3 151 000 – 1 201 000 = **1 950 000 €**. Contrôle par les capitaux propres de PERFADOM : 1 000 000 + 100 000 + 530 000 + 38 000 + 120 000 + 162 000 = 1 950 000 €. La subvention d'investissement figure dans les capitaux propres de PERFADOM, non dans ses dettes : comme les provisions réglementées, elle fait partie de l'actif net apporté [F01 § 8]. La dette envers RESPIDOM fait partie des passifs transmis ; elle ne s'éteindra que chez RESPIDOM (voir 2.6 d).

**Prime de fusion avant toute imputation (0,25 pt).** Toutes les actions étant rémunérées, l'apport rémunéré est l'actif net apporté en totalité : 1 950 000 – 600 000 = **1 350 000 €** [F01 § 4]. La prime se calcule sur la **valeur comptable** des apports, valeur d'inscription, et non sur leur valeur d'échange (3 600 000 €).

---

### 2.4 Écritures chez PERFADOM au 1er avril 2027 (2,5 pts)

Les apports étant évalués à la valeur comptable, PERFADOM ne dégage aucun résultat sur leur transmission.

Une présentation de FP1 par masses (immobilisations brutes, amortissements, actif circulant, dettes) est acceptée (voir les réponses tolérées).

**FP1 — Apport de l'actif et du passif à RESPIDOM (1,25 pt).** PERFADOM sort ses actifs (valeurs brutes et amortissements) et ses dettes ; sa créance sur RESPIDOM représente l'actif net apporté.

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – RESPIDOM, compte d'apport | 1 950 000 | |
| 28131 Amortissements des bâtiments | 270 000 | |
| 28135 Amortissements des installations générales, agencements, aménagements des constructions | 195 000 | |
| 28154 Amortissements des matériels industriels (matériel de perfusion) | 700 000 | |
| 1681 Autres emprunts (emprunt auprès de RESPIDOM) | 400 000 | |
| 1688 Intérêts courus sur autres emprunts et dettes assimilées | 6 000 | |
| 164 Emprunts auprès des établissements de crédit | 450 000 | |
| 401 Fournisseurs | 210 000 | |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | 95 000 | |
| 444 État – Impôts sur les bénéfices | 40 000 | |
| 211 Terrains | | 120 000 |
| 2131 Bâtiments | | 900 000 |
| 2135 Installations générales, agencements, aménagements des constructions | | 600 000 |
| 2154 Matériels industriels (matériel de perfusion) | | 1 500 000 |
| 37 Stocks de marchandises (consommables) | | 280 000 |
| 411 Clients | | 760 000 |
| 512 Banques | | 156 000 |
| **Total** | **4 316 000** | **4 316 000** |

**FP2 — Droits des associés sur l'actif net (0,75 pt).** Les capitaux propres, subvention d'investissement comprise, sont virés aux comptes des associés au prorata de leurs actions ; les comptes 131 et 139 sont soldés.

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 1 000 000 | |
| 1061 Réserve légale | 100 000 | |
| 1068 Autres réserves | 530 000 | |
| 110 Report à nouveau – solde créditeur | 38 000 | |
| 120 Résultat de l'exercice – bénéfice (période du 01/01 au 31/03/2027) | 120 000 | |
| 131 Subventions d'investissement octroyées | 240 000 | |
| 139 Subventions d'investissement inscrites au compte de résultat | | 78 000 |
| 456 Associés – Opérations sur le capital (MÉDIOUEST, 70 %) | | 1 365 000 |
| 456 Associés – Opérations sur le capital (Mme PENVERN, 20 %) | | 390 000 |
| 456 Associés – Opérations sur le capital (M. MASSIAC, 10 %) | | 195 000 |
| **Total** | **2 028 000** | **2 028 000** |

**FP3 — Remise des actions RESPIDOM aux associés (0,5 pt).** RESPIDOM remet directement les 30 000 actions nouvelles aux associés de PERFADOM, en échange de leurs actions : 21 000 à MÉDIOUEST, 6 000 à Mme PENVERN et 3 000 à M. MASSIAC.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital (MÉDIOUEST : 21 000 actions RESPIDOM) | 1 365 000 | |
| 456 Associés – Opérations sur le capital (Mme PENVERN : 6 000 actions) | 390 000 | |
| 456 Associés – Opérations sur le capital (M. MASSIAC : 3 000 actions) | 195 000 | |
| 467 Divers comptes débiteurs – RESPIDOM, compte d'apport | | 1 950 000 |

Après FP3, tous les comptes de PERFADOM sont soldés.

---

### 2.5 Écritures de base chez RESPIDOM au 1er avril 2027 (3,5 pts)

**FR1 — Augmentation de capital rémunérant les apports (1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 1 950 000 | |
| 101 Capital (30 000 actions × 20 €) | | 600 000 |
| 1042 Primes de fusion | | 1 350 000 |

**FR2 — Réalisation des apports à la valeur comptable (2,5 pts).** Valeurs brutes des immobilisations et amortissements repris (1 pt) ; actif circulant (0,25 pt) ; dettes reprises, y compris l'emprunt envers RESPIDOM et ses intérêts courus (1 pt) ; compte d'apport crédité de l'actif net (0,25 pt).

| Compte | Débit | Crédit |
|---|---:|---:|
| 211 Terrains | 120 000 | |
| 2131 Bâtiments | 900 000 | |
| 2135 Installations générales, agencements, aménagements des constructions | 600 000 | |
| 2154 Matériels industriels (matériel de perfusion) | 1 500 000 | |
| 37 Stocks de marchandises (consommables) | 280 000 | |
| 411 Clients | 760 000 | |
| 512 Banques | 156 000 | |
| 28131 Amortissements des bâtiments | | 270 000 |
| 28135 Amortissements des installations générales, agencements, aménagements des constructions | | 195 000 |
| 28154 Amortissements des matériels industriels | | 700 000 |
| 1681 Autres emprunts (emprunt de PERFADOM envers RESPIDOM) | | 400 000 |
| 1688 Intérêts courus sur autres emprunts et dettes assimilées | | 6 000 |
| 164 Emprunts auprès des établissements de crédit | | 450 000 |
| 401 Fournisseurs | | 210 000 |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | | 95 000 |
| 444 État – Impôts sur les bénéfices | | 40 000 |
| 4561 Associés – Comptes d'apport en société | | 1 950 000 |
| **Total** | **4 316 000** | **4 316 000** |

Après FR1 et FR2, le compte 4561 est soldé.

---

### 2.6 Écritures complémentaires chez RESPIDOM (8 pts)

**a. Reconstitution de la subvention d'investissement (2 pts)**

*Justification (0,5 pt).* La subvention nette (162 000 €) est comprise dans l'actif net apporté et donc dans la prime de fusion. Par l'option du traité, RESPIDOM s'est engagée à réintégrer le solde de la subvention selon le plan d'amortissement des installations [V BOI-IS-FUS-10-20-40-10 § 180, F01 § 8]. Elle la reconstitue à son bilan par **prélèvement sur la prime de fusion** [V programme UE 4, compétence 1.3.c ; écriture : convention de rédaction, F01 § 8]. Par cohérence avec la reprise des valeurs brutes et des amortissements, la subvention est reconstituée pour son **montant initial** (240 000 €), diminué des sommes déjà virées au résultat (78 000 €) ; la prime ne supporte que le montant net.

*Écriture (1,5 pt) :*

**FR3 — 1er avril 2027**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (240 000 – 78 000) | 162 000 | |
| 139 Subventions d'investissement inscrites au compte de résultat | 78 000 | |
| 131 Subventions d'investissement octroyées | | 240 000 |

**b. Suivi de la subvention au 31 décembre 2027 et conséquences fiscales (1,5 pt)**

*Écriture (0,75 pt).* RESPIDOM poursuit le plan de PERFADOM : 24 000 € par an, soit pour la période du 1er avril au 31 décembre 2027, 24 000 × 9 / 12 = **18 000 €**. La quote-part du 1er janvier au 31 mars 2027 (6 000 €) a été comptabilisée par PERFADOM et imposée dans son dernier résultat.

**FR6 — 31 décembre 2027**

| Compte | Débit | Crédit |
|---|---:|---:|
| 139 Subventions d'investissement inscrites au compte de résultat | 18 000 | |
| 747 Quote-part des subventions d'investissement virée au résultat de l'exercice | | 18 000 |

Cette quote-part compense, à hauteur de 40 %, la dotation aux amortissements des installations que RESPIDOM comptabilise pour la même période (60 000 × 9 / 12 = 45 000 €).

*Conséquences fiscales (0,75 pt)*
- **2027** : la quote-part de 18 000 € est comprise dans le résultat imposable de RESPIDOM, soit un impôt de 18 000 × 25 % = **4 500 €**. Comme la dotation aux amortissements, elle suit le rythme comptable : aucun retraitement extra-comptable n'est nécessaire.
- **Exercices suivants** : le solde au 31 décembre 2027, 240 000 – 78 000 – 18 000 = **144 000 €**, sera réintégré à raison de 24 000 € par an de 2028 à 2033 (6 × 24 000 = 144 000 €), soit 6 000 € d'impôt par an.
- Au total, l'option fait supporter à RESPIDOM l'imposition différée du solde de 162 000 €, soit **40 500 €** d'impôt étalé de 2027 à 2033, au lieu d'un impôt immédiat de même montant chez PERFADOM. Ni l'une ni l'autre ne comptabilisant d'impôts différés dans ses comptes individuels (annexe 2.1), cette imposition future n'est pas inscrite au bilan.

**c. Frais de fusion (2 pts)**

*Calcul et règle (1 pt).* Les frais de fusion peuvent être inscrits à l'actif en frais d'établissement, imputés sur la prime de fusion ou, à défaut, comptabilisés en charges [V PCG art. 212-9, F01 § 7]. RESPIDOM les impute sur la prime pour leur montant **net d'impôt** [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 48 000 × 75 % = **36 000 €** (0,5 pt). Les frais restant déductibles du résultat fiscal 2027, l'économie d'impôt de 48 000 × 25 % = **12 000 €** diminue la dette d'impôt sur les sociétés de RESPIDOM (0,5 pt).

*Écriture (1 pt) :*

**FR4 — 1er avril 2027**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (48 000 × 75 %) | 36 000 | |
| 444 État – Impôts sur les bénéfices (48 000 × 25 %) | 12 000 | |
| 512 Banques | | 48 000 |

**d. Prêt consenti à PERFADOM (2 pts)**

*Analyse (1 pt).* Par l'apport, RESPIDOM reçoit la dette de PERFADOM envers elle-même : elle devient à la fois créancière (prêt et intérêts courus inscrits à son actif) et débitrice (emprunt et intérêts courus repris en FR2) de la même obligation. La **confusion** éteint la créance et ses accessoires [V C. civ. art. 1349, F01 § 8]. L'extinction porte sur le capital (400 000 €) **et sur les intérêts courus** du 1er octobre 2026 au 31 mars 2027 (6 000 €), soit 406 000 €. Les montants étant identiques des deux côtés, l'extinction ne dégage aucun résultat. Les intérêts de la période du 1er janvier au 31 mars 2027 (3 000 €), comptabilisés en produit par RESPIDOM et en charge par PERFADOM avant la date d'effet, ne sont pas annulés : la fusion prend effet au 1er avril 2027. À compter de cette date, le prêt ne produit plus d'intérêts.

*Écriture (1 pt) :*

**FR5 — 1er avril 2027**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1681 Autres emprunts (emprunt de PERFADOM envers RESPIDOM) | 400 000 | |
| 1688 Intérêts courus sur autres emprunts et dettes assimilées | 6 000 | |
| 2748 Autres prêts (prêt à PERFADOM) | | 400 000 |
| 27684 Intérêts courus sur prêts | | 6 000 |

**e. Prime de fusion après imputations (0,5 pt).** 1 350 000 – 162 000 (subvention) – 36 000 (frais nets d'impôt) = **1 152 000 €**.

---

### 2.7 Note à M. KERDILÈS (4 pts)

**a. Capitaux propres de RESPIDOM juste après la fusion (1,5 pt).** Conformément à l'annexe 2.1, les capitaux propres avant la fusion sont ceux du 31/12/2026 ; le résultat de l'exercice 2027 n'est pas pris en compte.

| Poste | Avant la fusion | Variation | Après la fusion |
|---|---:|---:|---:|
| Capital (100 000 actions de 20 €) (0,25 pt) | 1 400 000 | + 600 000 | 2 000 000 |
| Prime de fusion : 1 350 000 – 162 000 – 36 000 (0,25 pt) | 0 | + 1 152 000 | 1 152 000 |
| Réserve légale | 140 000 | | 140 000 |
| Autres réserves | 2 900 000 | | 2 900 000 |
| Report à nouveau | 60 000 | | 60 000 |
| Subvention d'investissement : 240 000 – 78 000 (0,25 pt) | 0 | + 162 000 | 162 000 |
| **Total (0,5 pt)** | **4 500 000** | **+ 1 914 000** | **6 414 000** |

Contrôle (0,25 pt) : la hausse des capitaux propres (1 914 000 €) est égale à l'actif net comptable reçu (1 950 000 €) diminué des frais de fusion nets d'impôt (36 000 €). La reconstitution de la subvention déplace 162 000 € de la prime vers la subvention sans modifier le total.

**b. Répartition du capital après la fusion (1 pt ; 0,25 par ligne et 0,25 pour le commentaire)** — 70 000 + 30 000 = 100 000 actions :

| Associé | Actions avant | Actions après | % après |
|---|---:|---:|---:|
| SAS MÉDIOUEST Participations | 59 500 RESPIDOM (85 %) et 14 000 PERFADOM (70 %) | 59 500 + 14 000 × 3 / 2 = 80 500 | **80,5 %** |
| M. Erwan TRÉMEUR et Mme Laure GUÉLIN | 7 000 et 3 500 RESPIDOM (10 % et 5 %) | 7 000 et 3 500 | **7 % et 3,5 %** |
| Mme Claire PENVERN et M. Julien MASSIAC | 4 000 et 2 000 PERFADOM (20 % et 10 %) | 6 000 et 3 000 | **6 % et 3 %** |
| **Total** | | **100 000** | **100 %** |

Commentaire : MÉDIOUEST conserve le **contrôle exclusif** de RESPIDOM avec 80,5 % des droits de vote ; sa participation baisse de 85 % à 80,5 % parce que les associés minoritaires de PERFADOM entrent au capital. Les minoritaires de RESPIDOM sont dilués (de 15 % à 10,5 % à eux deux), ceux de PERFADOM passent de 30 % d'une petite société à 9 % de l'ensemble. La parité étant équitable, aucun associé ne perd de valeur : par exemple, les 4 000 actions de Mme PENVERN valaient 720 000 €, ses 6 000 actions RESPIDOM aussi (6 000 × 120 €).

**c. Enjeux pour les parties prenantes (1,5 pt, grille de niveaux)**

| Niveau | 0 | 0,5 | 1 | 1,5 |
|---|---|---|---|---|
| Attendu | Absence de commentaire ou commentaire hors sujet | Une partie prenante traitée, ou idées sans lien avec les chiffres | Deux parties prenantes traitées, chiffres à l'appui | Les trois parties prenantes traitées, chiffres à l'appui, dans une note structurée |

Idées attendues :
- **Créanciers de PERFADOM** (banque, fournisseurs, organismes sociaux, État) : ils deviennent créanciers de RESPIDOM, dont les capitaux propres atteignent 6 414 000 € contre 1 950 000 € pour PERFADOM ; leur gage s'élargit, mais il est désormais partagé avec les créanciers de RESPIDOM. Pour RESPIDOM, le prêt de 400 000 € à PERFADOM et ses intérêts disparaissent : le risque de crédit sur une société du même groupe est remplacé par les actifs de PERFADOM eux-mêmes.
- **Banquier de RESPIDOM** : les emprunts bancaires passent de 1 800 000 € à 1 800 000 + 450 000 = **2 250 000 €**, mais les capitaux propres augmentent davantage ; le rapport emprunts bancaires / capitaux propres passe de 40 % (1 800 000 / 4 500 000) à environ **35 %** (2 250 000 / 6 414 000). Les actifs repris à la valeur comptable ne montrent pas les plus-values latentes de PERFADOM (sa valeur d'échange de 3 600 000 € dépasse de 1 650 000 € son actif net comptable) : le bilan est prudent. Les frais de fusion ont été payés (48 000 €), sans incidence sur le résultat.
- **Administration fiscale** : le régime de faveur reporte l'imposition des plus-values latentes de PERFADOM, que RESPIDOM devra calculer d'après les valeurs fiscales de PERFADOM en cas de cession ; RESPIDOM paie l'impôt de la dernière période de PERFADOM (40 000 €) et réintègre le solde de la subvention, 162 000 €, de 2027 à 2033 (40 500 € d'impôt au total) ; les frais de fusion sont déductibles en 2027 (économie de 12 000 €). Le respect des engagements pris dans le traité conditionne le maintien du régime.

---

### Réponses tolérées
- **Subvention reconstituée pour son montant net** (crédit du compte 131 pour 162 000 € dans FR3, sans mouvement du compte 139) : acceptée pour l'écriture si le montant prélevé sur la prime (162 000 €) est juste ; 0,25 pt de moins sur l'écriture, la reconstitution du montant brut et des quotes-parts déjà virées étant cohérente avec la reprise des valeurs brutes et des amortissements. L'écriture FR6 et la prime finale sont alors inchangées.
- **Frais de fusion** : passage préalable des honoraires en charges (6226 Honoraires) puis imputation sur la prime nette d'impôt par le crédit du compte de charge, dès lors que la prime supporte 36 000 € et que l'économie d'impôt de 12 000 € est constatée.
- **Écritures de RESPIDOM** : présentation de FR1 et FR2 en une seule écriture ; dettes sociales ventilées entre 421 et 431 ; tout compte du 16 ou du 168 cohérent pour l'emprunt de PERFADOM envers RESPIDOM (par exemple 1687), dès lors que FR2 et FR5 utilisent le même ; extinction du prêt présentée directement dans FR2 (créance de RESPIDOM soldée au lieu de reprendre la dette), si la réponse explique la confusion : le point des dettes de FR2 et le point de l'écriture FR5 sont alors accordés ; stocks de consommables enregistrés en 32 (321 ou 322) au lieu de 37 ; installations de stockage à température dirigée enregistrées en 2151, 2154 ou 2181 (amortissements 28151, 28154 ou 28181) au lieu de 2135 / 28135, dès lors que FP1, FR2 et les amortissements utilisent le même compte.
- **Écritures de PERFADOM** : tout compte de tiers cohérent pour la créance sur RESPIDOM (par exemple 458) ou pour les droits des associés ; regroupement de FP2 et FP3 ; passage par un compte de titres RESPIDOM reçus puis remis aux associés ; écriture FP1 passée par masses, dès lors que les comptes d'amortissement sont soldés. Mêmes tolérances que pour RESPIDOM sur les comptes de stocks (32, 321 ou 322) et des installations (2151, 2154 ou 2181).
- **Question 2.6 b** : écriture de la dotation aux amortissements des installations (45 000 €) ajoutée ; elle n'est pas demandée et n'est pas notée.
- **Sens de l'opération** : réponse « sens sans incidence en contrôle commun » sans conclusion sur le sens, acceptée.

### Erreurs fréquentes (rapports du jury)
- `JUR-R05` Difficulté à s'adapter : valeur réelle retenue au motif qu'aucune des deux sociétés ne détient l'autre, ou que les associés minoritaires sont des personnes physiques ; recherche d'un boni ou d'un mali alors qu'il n'y a aucune détention préalable ; parité inversée (2 actions RESPIDOM pour 3 actions PERFADOM, soit 13 333 actions et un rompu).
- `JUR-R01` Prime de fusion calculée sur la valeur d'échange (3 600 000 – 600 000 = 3 000 000 €) au lieu de l'actif net comptable apporté.
- `JUR-R03` Oubli de la reconstitution de la subvention par prélèvement sur la prime, ou subvention reprise au crédit du compte 131 dans l'écriture de réalisation des apports, sans que l'actif net apporté en tienne compte.
- `JUR-F07` Annexes mal exploitées : intérêts courus oubliés dans l'extinction du prêt (seuls 400 000 € annulés), frais imputés pour leur montant brut (prime finale 1 140 000 €), quote-part de subvention 2027 calculée sur douze mois (24 000 €) au lieu de neuf.
- `JUR-F04` Écritures déséquilibrées, notamment FP2 lorsque le compte 139 n'est pas soldé au crédit.
- Erreurs propres à ce cas : résultat de la période du 1er janvier au 31 mars 2027 déclaré non imposable sous le régime de faveur ; reconstitution de la subvention présentée comme un effet automatique du régime de faveur, sans référence à l'option du traité ; écritures datées du 31 mars 2027 ; usage d'un compte de transferts de charges (classe 79), qui ne figure plus dans la liste des comptes du PCG 2026.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 236-1 ; PCG art. 710-1, 710-2, 720-1 | Définition de la fusion, champ du titre VII, inscription des apports | [V] | F01 § 1 |
| PCG art. 740-1, 741-1, 741-2, 743-1, 743-3 ; ANC 2020-01 art. 211-3 | Parité indépendante de l'évaluation des apports ; contrôle commun par une même mère ; valeur comptable ; exception | [V] p. 82-85 | F01 § 1 et § 2 |
| PCG art. 744-2, 744-3 ; BOI-IS-FUS-10-20-40-20 § 170-180 | Reprise des valeurs comptables, valeurs brutes et amortissements | [V] | F01 § 3.2 |
| CGI art. 210 A, 210 C-1 ; BOI-IS-FUS-10-10-10 § 1, 10 et 20 | Champ du régime de faveur, application sauf option, droit commun assimilé à une cessation | [V] | F02 § 1 et § 2 |
| CGI art. 210 A-1, 210 A-3 ; art. 209 II | Exonération des plus-values d'apport ; engagements de l'absorbante ; déficits | [V] | F02 § 2 à § 4 |
| BOI-IS-FUS-10-20-30 § 210 et 330 | Imposition du résultat de la dernière période de l'absorbée | [V] | F02 § 2 |
| CGI art. 42 septies ; BOI-IS-FUS-10-20-40-10 § 180 | Option pour le report de l'imposition du solde de la subvention chez l'absorbante, réintégration selon le plan d'amortissement | [V] | F01 § 8 |
| Reconstitution de la subvention par prélèvement sur la prime (1042 / 131, 139) | Écriture | Convention de rédaction | F01 § 8 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais de fusion imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion de la créance et de ses accessoires | [V] | F01 § 8 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Cadres d'exercice de l'expert-comptable, du commissaire aux comptes et de l'auditeur de durabilité ; comptes prévisionnels et négociation bancaire | `3.1.a` Cadres d'exercice professionnel ; `3.1.c` Principes déontologiques | 4 |
| 3.2 Audit des comptes et niveaux d'assurance ; audit légal et audit contractuel ; confirmations bancaires et communication des pièces | `3.2.a` Notion d'audit et typologie des missions ; `3.2.b` Moyens d'action du CAC | 4 |
| 3.3 Cycle trésorerie et financement : risques, assertions, procédures, anomalies et écritures | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit | 4 |
| 3.4 Ratio du contrat de prêt, continuité d'exploitation, annexe et rapport | `3.1.d` Appliquer la norme pertinente ; `3.2.e` Portée des opinions | 3 |
| 3.5 Responsabilités civile, pénale et disciplinaire du commissaire aux comptes | `3.1.e` Mise en cause de la responsabilité | 3 |
| 3.6 Architecture des ESRS ; publication volontaire | `3.3.a` Contexte et architecture des normes de durabilité | 3 |
| 3.7 Entreprise déclarante et chaîne de valeur ; horizons de temps ; estimations | `3.3.b` Principes de construction du reporting | 6 |
| 3.8 Vérification et recalcul de l'indicateur des déplacements | `3.4.b` Démarche | 2 |
| 3.9 Conclusion sur les informations publiées et portée | `3.4.c` Portée des avis | 1 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes annuels (18 points)

### 3.1 Cadres d'exercice ; comptes prévisionnels et négociation bancaire (4 pts)

**Cadres d'exercice des trois professions (2 pts)**

| | Expert-comptable | Commissaire aux comptes | Auditeur de durabilité | Points |
|---|---|---|---|---:|
| Nature de l'intervention | Mission **contractuelle** : tenir, centraliser, arrêter et réviser les comptabilités, analyser la situation et le fonctionnement des entreprises [V ord. 45-2138 art. 2] ; contrat écrit (lettre de mission), honoraires convenus par écrit [V décret 2012-432 art. 151 ; ord. art. 24] | **Missions** confiées par la loi, dont la certification des comptes, avec une assurance raisonnable, et **prestations** hors mission [V L. 821-2 III-IV, L. 821-53] ; mandat de six exercices [V L. 821-44] | Certification des informations en matière de durabilité, sur la base d'une **assurance limitée** [V L. 821-54 II ; LD 2026] ; ici mission volontaire, conduite dans les conditions de la certification légale, pour trois exercices [V L. 821-46 ; F13 § 1] | 0,5 |
| Conditions d'exercice | Inscription au **tableau de l'ordre** : droits civils, honorabilité, **diplôme d'expertise comptable** [V ord. art. 3] | Inscription sur la **liste tenue par la H2A** : honorabilité, stage professionnel, certificat d'aptitude ou diplôme d'expertise comptable ; serment [V L. 821-13 I, L. 821-14, L. 821-23] | Soit un **CAC** inscrit sur la **liste spéciale** (stage d'au moins huit mois et **épreuve** sur la certification de durabilité) [V L. 821-13 II, L. 821-18 I], soit un **organisme tiers indépendant** accrédité, dont l'auditeur personne physique est inscrit sur une liste de la H2A [V L. 822-3, L. 822-4] | 0,75 |
| Instances | **CROEC** (tableau, surveillance, conciliation) et **CNOEC** [V ord. art. 1, 28, 31, 33] ; sanctions prononcées par les juridictions disciplinaires de l'ordre [V ord. art. 49-50] | **H2A**, autorité publique indépendante (listes, normes, contrôles, sanctions) ; **CNCC** et **CRCC** (représentation de la profession) [V L. 820-1, L. 821-12] | **H2A** [V L. 820-1, L. 822-37] ; même **code de déontologie** que les CAC [V L. 822-7] | 0,5 |

**Les interventions de BRÉVANNE (0,25 pt)** : le cabinet est à la fois une société d'expertise comptable (département de M. GUÉRANDE, missions contractuelles pour d'autres clients) et une société de commissaires aux comptes. Auprès de VALDÉLIA, il n'exerce que deux missions de certification : celle des comptes, légale, et celle de l'état de durabilité, volontaire. Mme VARNIER, associée, commissaire aux comptes inscrite sur la liste spéciale, signe les deux rapports [V L. 821-26]. L'expert-comptable **produit** des comptes pour son client ; le commissaire aux comptes et l'auditeur de durabilité **vérifient**, pour les utilisateurs, une information produite par d'autres : leur indépendance s'apprécie en réalité et en apparence [V code de déontologie art. 5 II ; F10 § 3].

**Demande n° 2 : établir les comptes prévisionnels (0,75 pt)**
- L'établissement de comptes prévisionnels relève des travaux de l'expert-comptable (analyse de la situation de l'entreprise) [V ord. art. 2 ; S, qualification]. Pour VALDÉLIA, ce serait une **prestation** du cabinet, qui en certifie les comptes [V L. 821-2 IV].
- Ces prévisions sont au cœur de l'appréciation de la **continuité d'exploitation** : Mme VARNIER doit en apprécier la démarche et les hypothèses (annexe 3.5). Elle se prononcerait sur un travail de son propre cabinet : c'est un **risque d'autorévision** [V code de déontologie art. 5 II ; NEP continuité d'exploitation § 7].
- VALDÉLIA n'est pas une EIP : aucune liste fermée de services interdits ne s'applique, mais le commissaire aux comptes ne peut ni accepter ni poursuivre une mission de certification en cas de risque d'autorévision sans mesure de sauvegarde appropriée [V L. 821-28 IV]. Confier le travail à un autre département du même cabinet ne supprime pas le risque : aucune sauvegarde n'est possible [S, application]. L'argument de la présidente (« la banque leur fera confiance s'ils portent le nom de votre cabinet ») confirme le risque : un tiers objectif, raisonnable et informé confondrait les prévisions de la direction et le travail du certificateur [V A. 821-55 § 03, 11, 27-30].

**Demande n° 3 : défendre la demande de renonciation devant ARMORINE (0,75 pt)**
- ARMORINE est une **utilisatrice des comptes certifiés** : elle fonde sa décision sur le ratio calculé à partir de ces comptes et sur le rapport de Mme VARNIER. Défendre devant elle les intérêts de VALDÉLIA reviendrait à prendre parti pour l'entité contrôlée, contrairement à l'**impartialité** [V code de déontologie art. 4] et à l'exigence d'éviter toute situation **perçue** comme compromettant l'exercice impartial de la mission [V code art. 5 I].
- Négocier un financement, c'est aussi participer à la gestion, alors que la mission du commissaire aux comptes exclut **toute immixtion dans la gestion** [V L. 821-54 I].
- Aucune mesure de sauvegarde ne rendrait la présence de Mme VARNIER acceptable : « rassurer la banque » est précisément l'effet que doit produire un rapport indépendant, et non une démarche aux côtés de la direction [S, application].

**Réponse de Mme VARNIER (0,5 pt)**
- Refus écrit et motivé des demandes n° 2 et n° 3 ; analyse consignée dans le dossier [V A. 821-55 § 41-43].
- Solutions proposées : les comptes prévisionnels sont établis par la direction de VALDÉLIA, le cas échéant avec un expert-comptable extérieur au cabinet et à son réseau ; la présidente négocie seule ou avec un conseil indépendant de BRÉVANNE. Le cabinet examinera ensuite ces prévisions dans le cadre de sa mission, au titre de la continuité d'exploitation [V NEP continuité d'exploitation § 6-7].

**Réponses tolérées**
- Une comparaison rédigée plutôt qu'un tableau, si les trois critères sont traités pour les trois professions.
- La mention qu'un expert-comptable sans mandat de commissaire aux comptes auprès de VALDÉLIA pourrait établir les prévisions et assister la présidente : points accordés.
- Le rattachement de la demande n° 3 au seul principe d'indépendance, si le candidat montre que l'apparence d'indépendance à l'égard de la banque est compromise.

**Erreurs fréquentes**
- Accepter l'établissement des prévisions au motif que VALDÉLIA n'est pas une EIP ou que le cabinet est aussi expert-comptable (`JUR-A03`).
- Transposer à l'expert-comptable l'exigence d'indépendance du commissaire aux comptes, ou l'inverse (`JUR-A03`).
- Énumérer des principes déontologiques sans les appliquer aux deux demandes (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 1-3, 24, 28, 31, 33, 49-50 ; décret 2012-432 art. 151 | Expert-comptable : mission, conditions, instances | [V] | F09 § 1, 2 |
| C. com. L. 820-1, L. 821-2, L. 821-12 à L. 821-14, L. 821-18, L. 821-23, L. 821-26, L. 821-44, L. 821-46, L. 821-53, L. 821-54, L. 822-3, L. 822-4, L. 822-7, L. 822-37 | CAC et auditeur de durabilité : missions, listes, conditions, instances, immixtion | [V] | F09 § 1, 3, 4, 6 |
| C. com. L. 821-28 IV ; code de déontologie art. 4, 5 ; A. 821-55 § 03, 11, 27-30, 41-43 | Autorévision hors EIP ; impartialité ; apparence ; sauvegardes ; documentation | [V] ; application : [S] | F10 § 2.1, 3, 5, 12 |

### 3.2 Audit des comptes, niveaux d'assurance et audit contractuel ; moyens d'action (4 pts)

**a. Audit des comptes, assurance, audit légal et audit contractuel (2 pts)**
- **Définition et objectif (0,5 pt)** : le commissaire aux comptes certifie, en justifiant de ses appréciations, que les comptes annuels sont réguliers et sincères et donnent une image fidèle du résultat de l'exercice, de la situation financière et du patrimoine ; il formule pour cela une **opinion** après avoir mis en œuvre un **audit des comptes** [V L. 821-53 ; NEP principes § 01]. L'audit ne garantit ni la viabilité de l'entité ni la qualité de sa gestion [V L. 821-55].
- **Niveaux d'assurance (0,5 pt)** : l'audit des comptes procure une **assurance raisonnable**, élevée mais non absolue, que les comptes pris dans leur ensemble ne comportent pas d'anomalies significatives ; ses limites tiennent aux sondages et au caractère souvent présomptif des éléments collectés [V NEP principes § 08-09]. L'opinion est exprimée sous une **forme positive**. La mission sur l'état de durabilité procure une **assurance limitée** : vérifications moindres en nature, en étendue et en durée, conclusion exprimée sous une **forme négative** (aucune erreur, omission ou incohérence importante relevée) [V LD 2026, niveau d'assurance ; F13 § 2.3].
- **Audit légal et audit contractuel (0,5 pt)** : l'audit des comptes annuels est une **mission** que la loi confie au commissaire aux comptes [V L. 821-2 III, L. 821-53]. Les comptes semestriels de VALDÉLIA ne font l'objet d'aucune obligation légale : leur audit, demandé par la banque, serait un **audit contractuel**, c'est-à-dire une **prestation** que le commissaire aux comptes peut fournir à l'entité dont il certifie les comptes [V L. 821-2 IV ; A. 821-55 § 08, qui cite l'audit financier contractuel comme exemple de prestation].
- **Conditions (0,5 pt)** :
  - une **lettre de mission** préalable, qui précise les engagements des parties et des honoraires en rapport avec les diligences [V R. 821-195 ; code de déontologie art. 12] ;
  - une **analyse de l'indépendance** avant l'acceptation : un audit ne conduit pas le cabinet à se prononcer sur son propre travail, et aucun risque d'autorévision n'apparaît [V A. 821-55 § 15, 23-25 ; L. 821-28 IV] ;
  - le **refus d'honoraires conditionnels** : le commissaire aux comptes ne peut accepter aucune rémunération conditionnelle ; facturer la mission seulement si la banque accorde sa renonciation est interdit [V code de déontologie art. 13].

**b. Les deux refus du 11/01/2027 (2 pts)**

*Refus n° 1 : demandes de confirmation aux banques (1 pt)*
- La demande de confirmation des tiers consiste à obtenir d'un tiers une déclaration **adressée directement** au commissaire aux comptes ; elle peut être ouverte (la banque fournit elle-même les soldes, emprunts, autorisations, garanties et engagements) ou fermée [V NEP confirmations § 3-5]. Le commissaire aux comptes **maîtrise** la sélection des tiers, la rédaction et l'envoi des demandes et la réception des réponses [V NEP confirmations § 9]. L'offre de M. KERLOGUEN (« je vous remettrai moi-même les relevés ») ne remplace pas cette technique : un élément obtenu directement d'un tiers est plus fiable qu'un document remis par l'entité [V NEP éléments probants § 6].
- Le cabinet examine les **motifs** du refus [V NEP confirmations § 10] :
  - COUESNON : la clôture d'un compte en cours d'exercice ne justifie pas de l'écarter. La confirmation renseigne sur l'**exhaustivité** des dettes et des engagements (remboursement effectif du prêt de 250 000 €, absence de garantie résiduelle) ;
  - ARMORINE : la crainte d'« inquiéter » la banque n'est pas un motif valable. ARMORINE connaît ses propres créances et la demande est une pratique d'audit courante. C'est au contraire la banque la plus importante (emprunt, découvert, clause du contrat).
- Le refus émane du directeur administratif et financier, qui suit seul les banques et a écrit le courriel du 14/12/2026 : il est lui-même un facteur de risque de fraude, à prendre en compte dans l'évaluation des risques (question 3.3 a) [S].
- Le refus n'étant pas fondé, le cabinet en aurait tiré les conséquences dans son rapport, s'il avait été maintenu [V NEP confirmations § 12] : limitation, donc réserve ou impossibilité de certifier selon que les incidences sont ou non circonscrites [V NEP rapport § 11, 14].

*Refus n° 2 : correspondance avec ARMORINE (0,75 pt)*
- Le commissaire aux comptes se fait communiquer sur place **toutes les pièces qu'il estime utiles**, notamment les contrats, sans limitation aux pièces comptables [V L. 821-60]. La correspondance avec la banque est utile : elle renseigne sur le respect de la clause du contrat, sur le renouvellement du découvert et donc sur la continuité d'exploitation. Le courriel du 14/12/2026 révèle d'ailleurs une intention d'agir sur la trésorerie de fin d'année.
- La confidentialité invoquée est inopposable : le secret professionnel ne peut être opposé au commissaire aux comptes, sauf par les auxiliaires de justice [V L. 821-61 al. 3], et le commissaire aux comptes est lui-même tenu au secret [V L. 821-35].
- Le refus de communiquer une pièce utile est un **délit d'obstacle**, puni de cinq ans d'emprisonnement et de 75 000 € d'amende, qui vise les dirigeants et toute personne au service de l'entité, donc aussi le directeur administratif et financier [V L. 821-6 3°].

*Conduite à tenir (0,25 pt)* : entretien, puis rappel écrit des droits du commissaire aux comptes et des conséquences d'un refus ; saisine de la présidente, organe de direction avec lequel le cabinet communique [V L. 821-63 I] ; documentation des échanges [V NEP documentation § 04-08]. C'est ce qu'a fait Mme VARNIER : la présidente a accepté le 18/01/2027 et la limitation a été levée.

**Réponses tolérées**
- La présentation de l'audit contractuel comme une « autre intervention » du commissaire aux comptes, si la nature de prestation et la lettre de mission sont indiquées.
- L'absence de mention du délit d'obstacle, si la limitation et ses conséquences sur l'opinion sont présentées.
- La distinction de l'examen limité des comptes intermédiaires prévu par certains textes, si le candidat note qu'aucune obligation légale ne vise ici les comptes semestriels.

**Erreurs fréquentes**
- Présenter l'assurance limitée comme une assurance raisonnable « allégée » exprimée sous une forme positive (`JUR-A01`).
- Accepter des honoraires subordonnés à la décision de la banque (`JUR-A03`).
- Accepter le refus de la correspondance au motif qu'elle n'est pas une pièce comptable, ou celui des confirmations sans examiner ses motifs (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-2, L. 821-53, L. 821-55 ; NEP principes § 01, 08-09 ; LD 2026, niveau d'assurance | Audit des comptes ; assurance raisonnable et limitée | [V] | F11 § 1 ; F13 § 2.3 |
| C. com. R. 821-195 ; code de déontologie art. 12-13 ; A. 821-55 § 08, 15, 23-25 | Audit contractuel ; lettre de mission ; honoraires | [V] | F10 § 4.1, 12 ; F11 § 1.2, 13 |
| NEP confirmations § 3-5, 9-12 ; NEP éléments probants § 6 ; NEP rapport § 11, 14 | Confirmation des banques ; refus de la direction ; limitation | [V] | F11 § 6.1, 6.3, 8.1 |
| C. com. L. 821-6 3°, L. 821-35, L. 821-60, L. 821-61, L. 821-63 I | Communication des pièces ; secret ; délit d'obstacle | [V] | F11 § 2, 13 ; F10 § 7 |

### 3.3 Cycle trésorerie et financement (4 pts)

**a. Risque d'anomalies significatives et orientation des travaux (1 pt)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41]
- **Risque inhérent élevé (0,5 pt)** :
  - la clause du contrat de prêt crée une **pression** sur le ratio : selon le projet de comptes, la marge n'est que de 42 000 € (3 150 000 € de dettes financières nettes admises, contre 3 108 000 €). Son dépassement rendrait exigible un emprunt de 3 000 000 €, soit 30,6 % du total du bilan ;
  - l'excédent brut d'exploitation baisse de 37,9 % (de 1 450 000 € à 900 000 €) ;
  - le courriel du 14/12/2026 (« nous ferons le nécessaire sur la trésorerie ») est un **indice de biais** de la direction, donc un facteur de risque de fraude sur les disponibilités et les dettes financières ;
  - certaines opérations de fin d'exercice (encaissements, intérêts) sont sensibles à la **séparation des exercices**.
- **Risque lié au contrôle élevé (0,25 pt)** : M. KERLOGUEN établit et valide seul le rapprochement bancaire et suit seul les relations avec les banques, alors qu'il est directement intéressé au ratio. Sans test des contrôles, le risque d'anomalies significatives au niveau des assertions correspond au risque inhérent évalué [V NEP risques § 41].
- **Orientation (0,25 pt)** : le risque de non-détection acceptable est **faible**. Le cabinet met en œuvre des **procédures de substance** au plus près de la clôture et privilégie les éléments **externes** (banques, relevés de janvier 2027, avis de virement) [V NEP réponses § 03-13 ; NEP éléments probants § 6]. Il renforce l'esprit critique et recalcule le ratio.

**b. Risques, assertions et procédures (1,5 pt : 0,5 pt par risque pertinent, avec son assertion et une procédure justifiée, dans la limite de trois ; tout risque du tableau est accepté)** [V NEP éléments probants § 9-10]

| Risque | Assertion | Procédure et justification |
|---|---|---|
| Dettes financières non recensées (prêt du COUESNON mal remboursé, autre concours, garantie) | **Exhaustivité** et **droits et obligations** des dettes (soldes) | **Demandes de confirmation ouvertes aux trois banques**, y compris le COUESNON ; rapprochement des réponses avec le tableau des emprunts et les contrats ; examen des charges financières (des intérêts payés sans emprunt recensé révéleraient une dette omise). Éléments externes, obtenus directement par le cabinet |
| Disponibilités surévaluées par un encaissement enregistré par anticipation | **Existence** des disponibilités (solde) ; **séparation des exercices** des encaissements | **Examen de l'état de rapprochement** : chaque élément en suspens est rapproché du relevé de janvier 2027 et de sa pièce (avis de virement, chèque) ; confirmation du solde MELVANE. C'est cette procédure qui révèle le virement du département |
| Intérêts courus non rattachés à 2026 | **Séparation des exercices** des charges financières (flux) ; **exhaustivité** des dettes | **Recalcul des intérêts courus** à partir du tableau d'amortissement et du contrat ; procédure analytique de la charge d'intérêts (capital restant dû moyen × 3,6 %) |
| Ratio, clause et échéances mal présentés | **Présentation et intelligibilité**, **exhaustivité** et **mesure** des informations de l'annexe | Lecture de l'article 9 du contrat ; **recalcul du ratio** selon la définition contractuelle ; vérification de l'état des échéances des dettes et des notes 1 et 12 au regard de la méthode de VALDÉLIA |

Autres réponses acceptées : **évaluation** de la créance sur le département (encaissement postérieur) ; **classement** des concours bancaires courants ; procédure analytique sur les agios.

**c. Les deux anomalies et leur correction (1,5 pt)**

*Virement du département et conséquences pour la mission (0,5 pt)*
- Le virement a été émis le 07/01/2027 et crédité le 08/01/2027 : au 31/12/2026, VALDÉLIA détenait une **créance** sur le département (prestations de décembre facturées le 31/12/2026), et non des disponibilités. Les disponibilités sont **surévaluées de 160 000 €** et les créances sous-évaluées du même montant ; le résultat n'est pas affecté. Le chèque n° 7731 (3 600 €) est un suspens normal, débité en janvier 2027.
- Disponibilités corrigées : 409 000 − 160 000 + 3 000 = **252 000 €** ; elles concordent avec le relevé (252 600 − 3 600 + 3 000).
- **Caractère significatif** : 160 000 € représentent 69,6 % du seuil de 230 000 € ; l'anomalie n'est pas significative par son montant. Elle l'est par sa **nature** et ses **circonstances** : elle ramène le ratio sous le plafond du contrat et masque son dépassement (question 3.4), et le courriel du 14/12/2026 laisse penser qu'elle est **volontaire** [V NEP caractère significatif § 9 ; NEP anomalies § 8-17].

*Intérêts courus (0,5 pt)*
- L'échéance du 31/01/2027 rémunère le trimestre du 01/11/2026 au 31/01/2027 (27 000 € = 3 000 000 × 3,6 % × 3/12). Deux mois se rapportent à 2026 : 27 000 × 2/3 = **18 000 €**, qui n'ont pas été comptabilisés alors que les intérêts courus de 2025 avaient été contrepassés en 2026.
- Les charges financières et les dettes sont **sous-évaluées de 18 000 €** et le résultat courant avant impôt **surévalué de 18 000 €** (471 000 € dans le projet, 453 000 € après correction). L'anomalie représente 7,8 % du seuil : elle n'est significative ni par son montant ni par sa nature. Elle reste supérieure au seuil des anomalies manifestement insignifiantes (10 000 €) : elle est donc récapitulée et sa correction demandée. Les intérêts courus étant exclus des dettes financières nettes du contrat, elle ne modifie pas le ratio.

*Écritures de correction au 31/12/2026 (0,5 pt : 0,25 pt par écriture complète)*

E1 – Annulation de l'encaissement du département, reçu le 08/01/2027

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 411 | Clients | 160 000 | |
| 512 | Banques | | 160 000 |

E2 – Intérêts courus du 01/11 au 31/12/2026 sur l'emprunt ARMORINE

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 6611 | Intérêts des emprunts et dettes | 18 000 | |
| 1648 | Intérêts courus sur emprunts auprès des établissements de crédit | | 18 000 |

*Conséquences pour la mission (notées avec le virement)* : demande de correction des deux anomalies, obtenue le 17/02/2027 [V NEP anomalies § 8-17] ; communication à la présidente des modifications apportées aux comptes et de l'irrégularité relevée [V L. 821-63 I] ; esprit critique renforcé sur les autres estimations et sur les déclarations de M. KERLOGUEN ; **déclaration écrite** de la présidente [V NEP déclarations écrites § 6-7].

**Réponses tolérées**
- Une écriture E1 au compte 4111 Clients - Ventes de biens ou de prestations de services, ou à un compte de tiers propre au département.
- Le classement du risque lié au virement sous la seule « séparation des exercices », si l'effet sur l'existence des disponibilités est vu.
- La qualification de fraude présentée comme une hypothèse à confirmer, plutôt qu'établie : points accordés.

**Erreurs fréquentes**
- Confondre existence (solde) et réalité (flux), ou exhaustivité et séparation des exercices (`JUR-A01`).
- Juger le virement non significatif au seul motif qu'il est inférieur au seuil, sans voir son effet sur le ratio (`JUR-F07`).
- Proposer des procédures sans lien avec les risques identifiés ni avec les annexes (`JUR-A05`, `JUR-A06`).
- Oublier le numéro, l'intitulé ou le libellé des écritures (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 10-13 ; NEP risques § 02, 39-41 ; NEP réponses § 03-13 | Composantes du risque ; biais ; procédures de substance | [V] | F11 § 4.1, 5 |
| NEP éléments probants § 6, 9-10 ; NEP confirmations § 3-5 | Assertions ; fiabilité ; techniques | [V] | F11 § 4.3, 6 |
| NEP caractère significatif § 9 ; NEP anomalies § 8-17 ; NEP déclarations écrites § 6-7 ; C. com. L. 821-63 I | Nature et circonstances ; correction ; déclarations ; communication | [V] | F11 § 4.2, 5, 12.3 |
| Données des annexes 3.3 et 3.4 | Rapprochement, tableau d'amortissement | données de l'énoncé | — |

### 3.4 Ratio, continuité d'exploitation, annexe et rapport (3 pts)

**a. Ratio du contrat de prêt (0,75 pt)**

| Élément (en euros) | Projet de comptes | Comptes corrigés |
|---|---:|---:|
| Capital restant dû de l'emprunt ARMORINE | 3 000 000 | 3 000 000 |
| + Concours bancaires courants | 520 000 | 520 000 |
| − Disponibilités (MELVANE et caisse) | 412 000 | 252 000 |
| **= Dettes financières nettes** | **3 108 000** | **3 268 000** |
| Excédent brut d'exploitation | 900 000 | 900 000 |
| **Ratio** | **3,45** | **3,63** |

- Les deux corrections laissent l'excédent brut d'exploitation inchangé : le virement ne touche que le bilan et les intérêts courus sont des charges financières, elles aussi exclues des dettes financières nettes.
- Selon le projet, le ratio respecte le plafond (3,45 ≤ 3,5). Après correction, il le **dépasse** (3,63 > 3,5) : les dettes financières nettes excèdent de 118 000 € le maximum de 3 150 000 € (3,5 × 900 000). ARMORINE peut prononcer l'**exigibilité anticipée** du prêt (3 000 000 € au 31/12/2026), sauf renonciation écrite.

**b. Continuité d'exploitation et notes de l'annexe (1,25 pt)**

*Application de la norme (0,75 pt)* [V NEP continuité d'exploitation § 5-12]
- **Événements et circonstances** : de nature financière, au sens de la norme : dépassement du ratio et exigibilité possible de 3 000 000 € ; renouvellement du découvert au 30/06/2027 subordonné à la décision de la banque (non-reconduction possible de financements nécessaires à l'exploitation) ; baisse de 37,9 % de l'excédent brut d'exploitation.
- **Procédures** : prise de connaissance du plan de trésorerie de la direction ; appréciation de ses hypothèses (renonciation, revalorisation de 3 % non obtenue, réduction de la flotte) et de la période couverte, soit douze mois à compter de la clôture, jusqu'au 31/12/2027 ; rapprochement avec la lettre d'ARMORINE et les demandes adressées aux financeurs ; analyse de sensibilité (excédent brut d'exploitation de 880 000 € sans revalorisation) ; **déclaration écrite** de la présidente sur ses plans d'actions ; suivi jusqu'à la signature du rapport.
- **Conclusion** :
  - l'établissement des comptes dans une perspective de continuité d'exploitation reste **approprié**. ARMORINE ouvre la voie à une renonciation, la direction a un plan d'actions, l'activité est financée pour l'essentiel par des fonds publics, et la présidente n'envisage ni cessation ni procédure collective ;
  - il existe toutefois une **incertitude significative** : aucune décision de la banque ni des financeurs ne sera connue avant le 06/04/2027 et, sans renonciation, VALDÉLIA ne pourrait pas rembourser les 2 850 000 € restant dus, avec 330 000 € de trésorerie disponible. L'ampleur et la probabilité de cette incidence rendent nécessaire une information dans les comptes ;
  - Mme VARNIER communique ces conclusions à la présidente [V NEP continuité d'exploitation § 17 ; L. 821-63 I].

*Notes de l'annexe (0,5 pt)*
- **Note 1** : décrire la situation et ses implications (dépassement du ratio au 31/12/2026 : 3,63 pour un plafond de 3,5 ; exigibilité anticipée possible de 3 000 000 € ; demande de renonciation et ses conditions ; décision attendue au plus tard le 30/04/2027 ; découvert à renouveler au 30/06/2027 ; plan d'actions et hypothèses du plan de trésorerie). Indiquer que ces circonstances créent une **incertitude significative** sur la continuité d'exploitation et que les comptes ont été établis dans cette perspective au vu des plans de la direction [V NEP continuité d'exploitation § 4, 12].
- **Note 12** : supprimer l'affirmation inexacte (« la société respecte ses engagements bancaires ») et remplacer 3,45 par 3,63. Selon la méthode de VALDÉLIA, présenter les **3 000 000 €** à **un an au plus** dans l'état des échéances des dettes, au lieu de 600 000 € à un an au plus et 2 400 000 € à plus d'un an [V PCG art. 832-15 ; annexe 3.6].

**c. Opinion et forme du rapport ; annexe muette (1 pt)**
- **Opinion (0,5 pt)** : les anomalies ont été corrigées, aucune anomalie non corrigée ne subsiste et la limitation du mois de janvier a été levée. Mme VARNIER formule donc une **certification sans réserve** [V NEP rapport § 08 ; R. 821-180]. Son rapport comporte une **partie distincte** intitulée « Incertitude significative liée à la continuité d'exploitation », placée **avant la justification des appréciations**. Elle y attire l'attention sur la note 1 de l'annexe et précise que, **sans remettre en cause son opinion**, ces événements indiquent l'existence d'une incertitude significative susceptible de mettre en cause la continuité d'exploitation [V NEP continuité d'exploitation § 13 ; R. 821-180, 5°]. Cette partie n'est ni une réserve ni une observation facultative : la norme l'impose dès lors que l'incertitude existe et que l'annexe la décrit. La justification des appréciations peut viser la classification de l'emprunt et l'information donnée.
- **Si l'annexe ne disait rien (0,5 pt)** :
  - l'omission d'une information requise serait une anomalie que la présidente refuse de corriger. La partie distincte deviendrait impossible, car elle ne peut que renvoyer à une information de l'annexe et le commissaire aux comptes ne peut pas fournir lui-même une information dont la diffusion relève des dirigeants [V NEP rapport § 07] ;
  - Mme VARNIER formulerait une **certification avec réserve** ou un **refus de certifier**. Elle indiquerait, dans la partie relative au fondement de l'opinion, qu'il existe une incertitude significative et que les comptes ne donnent pas d'information pertinente à son sujet [V NEP continuité d'exploitation § 14]. Le choix dépend de son jugement : la réserve suffit si l'omission, précisément identifiée, peut être décrite de façon suffisante ; le refus s'impose si elle estime que, vu l'ampleur de l'enjeu (exigibilité de 3 000 000 €, 30,6 % du total du bilan, continuité de toute l'activité), l'utilisateur ne pourrait pas fonder son jugement sur les comptes [V NEP rapport § 09-13 ; S, qualification].

**Réponses tolérées**
- Le calcul du ratio sur les seuls comptes corrigés, si le candidat explique que la correction du virement fait passer le ratio au-dessus du plafond.
- Le refus comme la réserve, dans l'hypothèse de l'annexe muette, si le choix est justifié par le critère de suffisance de la réserve.
- La mention, dans la note 1, de l'échéance du 31/01/2027 payée et du capital de 2 850 000 € restant dû à cette date.

**Erreurs fréquentes**
- Formuler une réserve pour l'incertitude alors que l'annexe la décrit, ou confondre la partie sur l'incertitude avec une observation (`JUR-A02`).
- Refuser de certifier au motif que la continuité d'exploitation serait compromise, alors que la convention reste appropriée (`JUR-A02`).
- Citer le résumé de la norme sans l'appliquer aux dates et aux montants du cas (`JUR-A06`, `JUR-F07`).
- Calculer le ratio en incluant les intérêts courus, que le contrat exclut (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP continuité d'exploitation § 1-15, 17 ; C. com. R. 821-180 | Événements, procédures, incertitude significative, rapport, communication | [V] ; application : [S] | F11 § 13 |
| NEP rapport § 07-13, 18 | Opinions ; partie distincte ; limites de l'observation | [V] | F11 § 8, 12.2 |
| PCG art. 832-15 | État des échéances des dettes | [V] | F11 § 13 |
| Données des annexes 3.1, 3.3 à 3.6 | Ratio, plan de trésorerie, lettre de la banque | données de l'énoncé | — |

### 3.5 Responsabilités du commissaire aux comptes (3 pts)

**Responsabilité civile (1,25 pt)**
- **Fondement** : le commissaire aux comptes est responsable, tant à l'égard de l'entité que des **tiers**, des conséquences dommageables des **fautes et négligences** commises dans l'exercice de sa profession [V L. 821-37 al. 1]. ARMORINE, tiers, peut agir sur ce fondement ; la sanction est la réparation du préjudice par des **dommages-intérêts**.
- **Conditions** : une **faute**, un **préjudice** et un **lien de causalité** entre les deux [S, droit commun]. La mission procure une assurance raisonnable : le commissaire aux comptes est tenu d'une obligation de moyens, il ne garantit ni l'absence de toute anomalie [S, déduction de NEP principes § 08-09] ni la viabilité de l'entité [V L. 821-55].
- **Application** :
  - *faute* : rien n'indique de faute sur les comptes de 2025, certifiés sans réserve ni observation. La dégradation résulte d'événements de 2026 (accord de branche, carburants ; excédent brut d'exploitation de 1 450 000 € en 2025, contre 900 000 € en 2026). Sur 2026, le cabinet a détecté et fait corriger l'anomalie qui masquait le dépassement, et son rapport signale l'incertitude ;
  - *préjudice* : il n'est pas réalisé. ARMORINE n'a subi aucune perte et peut encore obtenir le remboursement ou négocier ;
  - *lien de causalité* : la décision de maintenir le découvert en 2026 relève de l'analyse de la banque, qui dispose de ses propres informations. Une éventuelle défaillance de VALDÉLIA viendrait de sa situation économique, et non du rapport sur les comptes de 2025.
- **Prescription** : trois ans à compter du fait dommageable ou de sa révélation s'il a été dissimulé [V L. 821-38, L. 225-254].

**Responsabilité pénale (0,5 pt)**
- Elle sanctionne des **infractions** par des peines d'amende et d'emprisonnement. Le commissaire aux comptes qui donne ou confirme des **informations mensongères** sur la situation de la personne morale encourt cinq ans d'emprisonnement et 75 000 € d'amende [V L. 821-9] ; la violation du secret professionnel est punie par le code pénal [V L. 821-7 dernier al. ; L. 821-35].
- Rien de tel ici : le rapport est exact et aucune information n'a été communiquée à la banque en dehors de ce rapport. Le risque pénal aurait existé si le cabinet avait accepté de « rassurer » ARMORINE sur des informations qu'il savait inexactes, ou s'il avait communiqué à la banque des informations couvertes par le secret.

**Responsabilité disciplinaire (0,5 pt)**
- Constituent une faute disciplinaire tout manquement aux conditions légales d'exercice, toute négligence grave et tout fait contraire à la probité ou à l'honneur [V L. 821-70 I]. Les sanctions (avertissement, blâme, interdiction temporaire d'exercer, radiation, sanctions pécuniaires) sont prononcées par la **commission des sanctions de la H2A** [V L. 821-71, L. 821-79].
- Le risque existerait si le cabinet avait accepté les demandes n° 2 et n° 3 (manquement à l'indépendance, question 3.1) ou des honoraires conditionnels (question 3.2), ou s'il avait certifié sans réserve et sans partie sur l'incertitude des comptes qui masquaient le dépassement du ratio.

**Appréciation du risque réel (0,75 pt)**
- Le risque de mise en cause est **faible**. Les diligences sont conformes aux normes (confirmations directes, examen du rapprochement, recalcul du ratio, application de la norme sur la continuité d'exploitation, déclaration écrite), le rapport informe les utilisateurs et le cabinet a refusé les interventions incompatibles avec sa mission.
- Sa protection repose sur la **documentation** du dossier, qui doit permettre à un auditeur expérimenté de comprendre les procédures, les éléments collectés et les conclusions [V NEP documentation § 04-08], et sur la date du rapport, qui fixe ce que le cabinet pouvait connaître.
- La menace d'ARMORINE ne doit pas influer sur l'opinion : céder à une pression pour éviter une mise en cause porterait atteinte à l'impartialité [V code de déontologie art. 4].

**Réponses tolérées**
- La présentation de la responsabilité disciplinaire sous le nom de « responsabilité professionnelle ».
- L'absence de mention de la prescription, si les trois conditions de la responsabilité civile sont appliquées au cas.

**Erreurs fréquentes**
- Confondre les trois responsabilités ou leurs sanctions (dommages-intérêts, peines, sanctions disciplinaires) (`JUR-A01`).
- Conclure à la responsabilité du commissaire aux comptes du seul fait des difficultés de l'entité, en oubliant que la certification ne garantit pas sa viabilité (`JUR-A05`).
- Énoncer les règles sans les appliquer à la menace d'ARMORINE (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-37, L. 821-38, L. 225-254, L. 821-55 | Responsabilité civile, prescription, viabilité | [V] ; conditions : [S] | F09 § 6, 7.1 |
| C. com. L. 821-7, L. 821-9, L. 821-35 | Responsabilité pénale | [V] | F09 § 7.3 |
| C. com. L. 821-70, L. 821-71, L. 821-79 | Responsabilité disciplinaire | [V] | F09 § 7.2 |
| NEP documentation § 04-08 ; code de déontologie art. 4 | Dossier ; impartialité | [V] | F11 § 7 ; F10 § 2.1 |

---

### Partie B – Durabilité (12 points)

### 3.6 Architecture des ESRS ; publication volontaire (3 pts)

**Architecture (1,5 pt)**
- **Normes transversales (0,5 pt)** : l'ESRS 1 « Exigences générales » fixe les conventions, les exigences de l'analyse de double matérialité et celles de la préparation et de la présentation de l'état de durabilité ; l'ESRS 2 « Informations générales à publier » fixe les informations générales que l'entreprise fournit pour tous les thèmes matériels. Les deux sont appliquées conjointement avec les normes thématiques [V ESRS 1 (2026) § 7-9]. L'ESRS 2 s'applique **toujours** [V ESRS 1 (2026) § 29 ; F12 § 5].
- **Normes thématiques (0,5 pt)** : environnementales (changement climatique, pollution, eau, biodiversité, ressources et économie circulaire), sociales (personnel de l'entreprise, travailleurs de la chaîne de valeur, communautés affectées, consommateurs et utilisateurs finaux) et de gouvernance (conduite des affaires). Elles ne s'appliquent qu'aux thèmes **matériels**, retenus à l'issue de l'analyse de double matérialité (matérialité d'impact et matérialité financière) [V ESRS 1 (2026) § 10, 24, 35 ; F12 § 3.1].
- **Informations propres à l'entreprise et domaines (0,5 pt)** : si un thème matériel n'est pas couvert, ou pas assez, par une norme, l'entreprise fournit des informations qui lui sont spécifiques [V ESRS 1 (2026) § 11]. Les informations sont organisées en domaines : gouvernance, stratégie, gestion des impacts, risques et opportunités, indicateurs et cibles [V ESRS 1 (2026) § 5].

**Ce qu'implique la publication volontaire pour VALDÉLIA (1,5 pt)**
- **Liberté de publier, mais pas de choisir ses règles (0,5 pt)** : aucune obligation ne s'impose à VALDÉLIA (hypothèse). En déclarant son état de durabilité **conforme aux ESRS**, elle s'oblige à respecter toutes leurs exigences applicables, comme une entité tenue de publier. Elle doit le déclarer expressément [V ESRS 2 (2026) BP-1 § 5] et indiquer la version des ESRS qu'elle applique pour l'exercice 2026 [V règl. délégué 2026/1563 art. 2 ; F12 § 3.2].
- **Contenu (0,5 pt)** : l'ESRS 2 en entier ; une analyse de double matérialité documentée, ici sur le climat, le personnel et les bénéficiaires ; pour chaque thème matériel, les exigences thématiques pertinentes. Elle ne publie pas d'information non matérielle tirée d'une exigence des ESRS [V ESRS 1 (2026) § 24, 29]. Le détail des normes thématiques n'est pas attendu.
- **Liens avec les comptes et la certification (0,5 pt)** :
  - même entreprise déclarante et même période que les comptes annuels [V ESRS 1 (2026) § 60, 76] ;
  - section clairement distinguée du rapport de gestion [V ESRS 1 (2026) § 104] ;
  - connectivité avec les états financiers : par exemple, les indemnités kilométriques du compte 6251 et le kilométrage des déplacements [V ESRS 1 (2026) § 112-116 ; F12 § 9] ;
  - la certification volontaire, conduite dans les conditions de la certification légale, ne délivre qu'une assurance limitée et ne porte ici ni sur la taxonomie ni sur le balisage (hypothèse).

**Réponses tolérées**
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences », « déclaration relative à la durabilité »).
- La mention de la norme volontaire destinée aux entreprises non soumises, si le candidat note que VALDÉLIA a retenu les ESRS et que ce choix n'est pas à discuter.

**Erreurs fréquentes**
- Ajouter aux normes transversales et thématiques une troisième catégorie de normes par secteur, que les ESRS révisées ne prévoient plus, ou détailler les exigences d'une norme thématique (`JUR-A01`).
- Croire qu'une publication volontaire permet de n'appliquer qu'une partie des ESRS tout en s'en réclamant (`JUR-A05`).
- Discuter l'obligation de publier ou son calendrier, alors que l'énoncé l'écarte (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 5, 7-11, 24, 29, 35, 60, 76, 104, 112-116 | Architecture ; matérialité ; entreprise déclarante ; présentation ; connectivité | [V] | F12 § 3, 5, 6, 9, 14 |
| ESRS 2 (2026) BP-1 § 5 ; règl. délégué 2026/1563 art. 2 | Déclaration de conformité ; version appliquée | [V] | F12 § 3.2, 14 |

### 3.7 Entreprise déclarante, chaîne de valeur, horizons, estimations (6 pts)

**a. Entreprise déclarante et chaîne de valeur (3 pts)**

*Règles (0,75 pt)*
- L'état de durabilité porte sur la **même entreprise déclarante** que les états financiers : ici VALDÉLIA, siège et agences, comme le retient le projet [V ESRS 1 (2026) § 60].
- Les informations vont au-delà des activités propres : elles couvrent les impacts, risques et opportunités matériels liés à l'entreprise par ses **relations d'affaires directes et indirectes** dans sa **chaîne de valeur amont et aval**, dans la mesure nécessaire à leur compréhension. Elles ne portent que sur les informations **matérielles**, et non sur chaque acteur de la chaîne [V ESRS 1 (2026) § 62-64]. La matérialité peut varier selon les parties de la chaîne [V § 67].
- **Actifs loués** : le preneur déclare dans ses **activités propres** les impacts résultant de l'utilisation de l'actif pendant la location ; le bailleur les déclare dans sa chaîne de valeur aval [V ESRS 1 (2026) § 71, AR 39].
- L'entreprise indique ce que son état de durabilité couvre dans sa chaîne de valeur [V ESRS 2 (2026) BP-1 § 4].

*Chaîne de valeur de VALDÉLIA (1 pt : 0,5 pt pour l'amont, 0,5 pt pour l'aval, avec les impacts concernés)*
- **Amont** : le loueur AUTOLÈNE et les constructeurs des véhicules (fabrication), les fournisseurs de carburant, les fournisseurs de matériel de soins et de protection, l'éditeur de TOURNÉO.
- **Aval** : les 1 900 bénéficiaires et leurs familles (continuité et qualité des soins, maintien à domicile, données de santé), ainsi que les financeurs publics qui paient l'essentiel des prestations.
- Le projet recense correctement ces acteurs, mais il en tire de mauvaises conséquences pour les déplacements.

*Véhicules loués (0,5 pt)* : VALDÉLIA est **preneur** des 140 véhicules, qu'elle utilise seule pour ses tournées et dont elle paie le carburant. Les émissions liées à leur utilisation relèvent de ses **activités propres**, et non de la chaîne de valeur amont du loueur [V ESRS 1 (2026) § 71, AR 39]. Le projet doit être corrigé. Relèvent de la chaîne de valeur amont la fabrication des véhicules et l'activité propre du loueur.

*Véhicules personnels (0,75 pt)*
- L'exclusion n'est pas justifiée. Le critère des ESRS n'est pas la propriété mais la **matérialité** des impacts liés à l'entreprise par ses relations d'affaires [V ESRS 1 (2026) § 62-63]. Or ces déplacements sont effectués pour les tournées de VALDÉLIA, qui les organise et les rembourse (460 000 € d'indemnités kilométriques). Ils concernent environ 90 salariés et 1 150 000 km, soit **230 t éq. CO2, 32,4 %** des émissions corrigées (question 3.8). L'impact est matériel, car il porte sur un thème retenu comme matériel.
- Ces véhicules n'étant ni détenus ni loués par VALDÉLIA, leurs émissions sont présentées dans sa **chaîne de valeur amont**, avec des données collectées ou des estimations [V ESRS 1 (2026) § 65 ; S, classement].

**b. Horizons de temps (1 pt)**
- Les ESRS retiennent, à compter de la fin de la période de reporting : le **court terme**, égal à la durée de la période des états financiers (2027) ; le **moyen terme**, jusqu'à **cinq ans** (2028 à 2031) ; le **long terme**, au-delà de cinq ans (après 2031) [V ESRS 1 (2026) § 79, 82]. Une autre définition du moyen ou du long terme n'est admise que si les horizons des ESRS donnent des informations non pertinentes, par exemple parce que l'entreprise gère ses impacts ou fixe ses cibles sur d'autres horizons [V ESRS 1 (2026) § 81] ; l'entreprise indique alors qu'elle use de cette faculté [V ESRS 2 (2026) BP-1 § 6, AR 2 b)].
- Le moyen terme de VALDÉLIA (2028 et 2029, soit deux ans) n'est **pas conforme** : aucune justification n'est donnée, et ses propres horizons de gestion plaident pour cinq ans (conventions de financement 2026-2030, renouvellement de la flotte en 2028). Elle doit retenir 2028-2031.
- Illustrations : court terme, hausse du prix des carburants et épisodes de canicule de l'été 2027 ; moyen terme, renouvellement de la flotte en 2028 et renégociation des financements en 2030 ; long terme, vieillissement de la population et difficultés durables de recrutement.

**c. Estimations et sources d'incertitude (2 pts)**
- **Conditions (0,5 pt)** : pour la chaîne de valeur, l'entreprise peut utiliser des informations collectées auprès des contreparties ou des **estimations**, selon la possibilité d'obtenir les données et leur fiabilité (données indirectes, moyennes sectorielles, échantillons, données de dépenses, autres données de substitution) [V ESRS 1 (2026) § 65]. Des estimations raisonnables ne retirent pas leur utilité aux informations si leurs principales hypothèses sont expliquées, même en cas d'incertitude de mesure élevée [V ESRS 1 (2026) AR 42].
- **Informations à donner (0,5 pt)** : les **jugements** qui influent le plus sur les informations, les **principales incertitudes**, notamment quand elles reposent sur des estimations, et les **principales hypothèses et limites** des estimations [V ESRS 1 (2026) § 88]. Ces exigences visent les estimations les plus difficiles, subjectives ou complexes [V AR 43].
- **Application (1 pt : 0,25 pt par source d'incertitude décrite, 0,25 pt pour l'omission constatée)** : le projet ne dit rien de tout cela, ce qui est une omission. VALDÉLIA doit décrire :
  - pour la flotte, la source du kilométrage : TOURNÉO calcule une distance théorique, sans les trajets vers le premier bénéficiaire ni les détours ; les relevés de compteurs la remplacent avantageusement (question 3.8) ;
  - pour les véhicules personnels, le caractère déclaratif des kilomètres, tirés des notes de frais validées ;
  - l'emploi d'un **facteur d'émission moyen unique** (0,20 kg éq. CO2 par km), qui ne distingue ni les motorisations ni les âges des véhicules, et sa source.

**Réponses tolérées**
- Le rattachement des déplacements en véhicule personnel aux activités propres, au motif qu'ils sont effectués sous la direction de VALDÉLIA pour son activité, si le candidat conclut à leur inclusion et à la description de l'estimation.
- Le vocabulaire des ESRS de 2023.
- Des exemples d'horizons différents de ceux du corrigé, s'ils sont tirés de l'annexe 3.7 et classés selon les durées des ESRS.

**Erreurs fréquentes**
- Exclure du périmètre ce que l'entreprise ne possède pas, ou rattacher au loueur les émissions des véhicules utilisés par le preneur (`JUR-A01`).
- Détailler les catégories d'émissions d'une norme thématique, qui ne sont pas attendues.
- Citer les règles sans exploiter les données de l'annexe 3.7 (`JUR-F07`, `JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 60, 62-65, 67, 71, AR 39 ; ESRS 2 (2026) BP-1 § 4 | Entreprise déclarante, chaîne de valeur, actifs loués | [V] | F12 § 7, 14 |
| ESRS 1 (2026) § 79-82 | Horizons de temps | [V] | F12 § 14 |
| ESRS 1 (2026) § 88, AR 42, AR 43 | Jugements, incertitudes, hypothèses et limites des estimations | [V] | F12 § 14 |
| Classement des véhicules personnels dans la chaîne de valeur | Application | [S, jugement] | — |

### 3.8 Vérification et recalcul de l'indicateur des déplacements (2 pts)

**Procédures (1 pt : 0,25 pt par procédure justifiée, dans la limite de quatre)** [V LD 2026 § 8, 12 ; F13 § 3]
- **Prise de connaissance du processus** de collecte : fonctionnement de TOURNÉO, validation des notes de frais par les responsables d'agence, choix du facteur d'émission ; entretiens avec les personnes chargées des données.
- **Rapprochement** des kilomètres de TOURNÉO avec les **relevés de compteurs** transmis par le loueur, élément externe : 2 400 000 km parcourus contre 2 060 000 km dans TOURNÉO, soit un écart de **340 000 km**, 14,2 % du kilométrage réel.
- **Procédure analytique** de la consommation de carburant : 156 000 litres pour 2 400 000 km donnent 6,50 litres aux 100 km, conformes à la fiche du constructeur. Sur la base de TOURNÉO, on obtiendrait 7,57 litres, ce qui est incohérent. Les compteurs sont donc fiables et TOURNÉO sous-estime les distances.
- **Rapprochement avec les comptes** (connectivité) : les 460 000 € d'indemnités kilométriques du compte 6251, au taux de 0,40 €, correspondent à 1 150 000 km (460 000 / 0,40), égaux aux kilomètres des notes de frais ; sondage de notes de frais rapprochées des tournées planifiées.
- **Facteur d'émission** : vérification de sa source et de sa cohérence avec la méthode décrite ; **recalcul** de l'indicateur.

**Recalcul et conclusion (1 pt)**

| Composante | Kilomètres | Émissions (km × 0,20 kg / 1 000) |
|---|---:|---:|
| Flotte louée, selon les relevés de compteurs (activités propres) | 2 400 000 | **480 t éq. CO2** (0,25 pt) |
| Véhicules personnels, selon les notes de frais (chaîne de valeur) | 1 150 000 | **230 t éq. CO2** (0,25 pt) |
| **Total recalculé** | 3 550 000 | **710 t éq. CO2** |
| Valeur publiée (2 060 000 km de TOURNÉO) | | 412 t éq. CO2 |
| **Sous-évaluation** | | **298 t éq. CO2** |

- La valeur publiée est sous-évaluée de 298 t, soit **42,0 %** du total recalculé (0,25 pt). L'écart vient de la mesure théorique de TOURNÉO (68 t) et de l'exclusion des véhicules personnels (230 t).
- **Conclusion (0,25 pt)** : il s'agit d'une erreur et d'une omission **importantes**. Elles portent sur un impact matériel et sur près de la moitié de l'indicateur, et un utilisateur en serait trompé. Mme VARNIER en demande la correction, avec la description de la méthode et de ses limites. À défaut, l'erreur, clairement circonscrite à un indicateur dont l'écart est chiffré, justifierait une **réserve motivée** sur l'axe des informations [V LD 2026 § 17 ; F13 § 4.2-4.3 ; S, appréciation de l'importance].

**Réponses tolérées**
- Un recalcul de la flotte sur la base du carburant (156 000 litres / 6,5 litres aux 100 km = 2 400 000 km), qui donne le même résultat.
- Un recalcul limité à la flotte (480 t), si le candidat a classé les véhicules personnels hors du périmètre en le justifiant à la question 3.7 : 0,5 pt sur 1 au recalcul.

**Erreurs fréquentes**
- Reprendre la valeur publiée sans la rapprocher des compteurs ni du carburant (`JUR-F02`, `JUR-F07`).
- Proposer des procédures générales sans lien avec les données de l'annexe 3.8 (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 8, 12, 17 | Vérification des informations ; appréciation ; réserve | [V] | F13 § 3, 4.2-4.3 |
| ESRS 1 (2026) § 65, 112-116 | Estimations ; connectivité avec les comptes | [V] | F12 § 7, 9 |
| Données des annexes 3.7 et 3.8 | Kilomètres, carburant, indemnités, facteur | données de l'énoncé | — |

### 3.9 Conclusion sur les informations publiées et portée (1 pt)

- **Formulation (0,5 pt)** : les informations corrigées ne comportent plus d'erreur, d'omission ou d'incohérence importante. Mme VARNIER émet un **avis de conformité** sur l'axe des informations, sous une **forme négative** : sur la base des travaux mis en œuvre, elle n'a pas relevé d'erreurs, omissions ou incohérences importantes concernant la conformité aux ESRS des informations publiées [V LD 2026 § 17 ; S, transposition à l'axe des informations du modèle de conclusion de l'axe du processus]. L'indicateur des déplacements, qui présentait un risque important et a été corrigé, peut être présenté parmi les **éléments ayant fait l'objet d'une attention particulière**, avec un renvoi à l'information publiée et un résumé des diligences [V LD 2026 § 17 ; F13 § 4.4].
- **Portée (0,5 pt)** :
  - la conclusion repose sur une **assurance limitée**. Elle n'atteste pas, comme une assurance raisonnable exprimée sous une forme positive, que les informations sont exemptes d'erreurs ; elle indique seulement que des vérifications moins étendues n'en ont pas révélé d'importantes ;
  - elle est émise **axe par axe** : une conclusion distincte porte sur le processus de détermination des informations, et le rapport ne couvre ni la taxonomie ni le balisage (hypothèse) ;
  - elle ne garantit ni la viabilité de VALDÉLIA ni la qualité de sa gestion [V L. 821-55], et elle se distingue de la certification des comptes, dont l'opinion repose sur une assurance raisonnable.

**Réponses tolérées**
- Le vocabulaire « auditeur de durabilité » ou « vérificateur ».
- L'absence d'élément d'attention particulière, si la forme négative et l'assurance limitée sont exposées.

**Erreurs fréquentes**
- Formuler une conclusion positive (« les informations sont conformes ») ou un avis global unique au lieu d'un avis par axe (`JUR-A01`, `JUR-A02`).
- Maintenir une réserve alors que l'erreur a été corrigée (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026, niveau d'assurance, § 17 et annexe 2 | Assurance limitée ; forme négative ; avis par axe ; éléments d'attention particulière | [V] ; transposition : [S] | F13 § 2.3, 4 |
| C. com. L. 821-55 | Absence de garantie de viabilité | [V] | F09 § 6 |
