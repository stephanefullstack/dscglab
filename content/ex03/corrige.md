# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Exercice d'entraînement n° 3 — Dossier 1 (45 points)

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F03 périmètre et méthodes (à jour au 22/10/2026) ; F04 retraitements (à jour au 23/10/2026) ; F05 écarts d'acquisition, goodwill et partage (à jour au 23/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre ANC et IFRS, goodwill, impôts différés, partage, 11 écritures, barème).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Périmètre ANC | `2.1.c` Définir le périmètre de consolidation | 9 |
| 1.2 Différences IFRS | `2.1.d` Conséquences du référentiel et des méthodes | 3 |
| 1.3 Écart d'acquisition ANC | `2.2.g` Écarts d'évaluation et d'acquisition | 4 |
| 1.4 Goodwill IFRS | `2.2.g` Écarts d'évaluation et d'acquisition | 4 |
| 1.5 a Écart d'évaluation | `2.2.g` Écarts d'évaluation et d'acquisition | 2 |
| 1.5 b Amortissements dérogatoires | `2.2.b` Retraitements préparatoires | 4 |
| 1.5 c Crédit-bail | `2.2.c` Homogénéisation, thèmes communs | 6 |
| 1.5 d Cession interne | `2.2.f` Résultats internes | 6 |
| 1.6 Dividendes | `2.2.f` Résultats internes | 2 |
| 1.7 Partage | `2.2.h` Partage des capitaux propres | 5 |
| **Total** | | **45** |

---

### 1.1 Périmètre ANC au 31/12/2026 (9 pts)

**Règles (2 pts)**
- **Pourcentage de contrôle** : somme des droits de vote détenus par la mère et par les entités qu'elle contrôle **exclusivement** ; on additionne sans multiplier [V ANC 2020-01 art. 211-6].
- **Nature du contrôle et méthode** [V art. 211-3 à 211-5 et 221-1] :
  - contrôle exclusif, présumé au-delà de 50 % : intégration globale (IG) ;
  - contrôle conjoint, qui suppose un accord entre un nombre limité d'associés : intégration proportionnelle (IP) ;
  - influence notable, présumée à partir de 20 % : mise en équivalence (MEE).
- **Pourcentage d'intérêt** : somme, sur toutes les chaînes de détention, des produits des pourcentages de capital [méthode directe, F03 § 4.1].

**Tableau (5 pts, 1 pt par société)**

| Société | % de contrôle | Nature | Méthode | % d'intérêt |
|---|---|---|---|---|
| ARGOS | — | Mère | — | 100 % |
| CALYPSO | 80 % | Exclusif | IG | 80 % |
| DELTA | 30 + 25 = **55 %** | Exclusif | IG | 30 + 80 % × 25 = **50 %** |
| FARO | 50 % (via CALYPSO) | Conjoint | IP | 80 % × 50 = **40 %** |
| ERIS | 15 + 10 = **25 %** | Influence notable | MEE | 15 + 50 % × 10 + 40 % × 5 = **22 %** |
| GAÏA | 8 % | Aucune | Non consolidée | — |

**Justifications (2 pts)**
- **DELTA** : les 25 % détenus par CALYPSO, contrôlée exclusivement, s'ajoutent aux 30 % d'ARGOS. Le groupe contrôle DELTA (55 %), bien qu'il n'y détienne que 50 % d'intérêt.
- **FARO** : le pacte impose l'unanimité de CALYPSO et de HÉRA pour les décisions stratégiques, financières et opérationnelles, ce qui caractérise un **contrôle conjoint** [V art. 211-4].
- **ERIS** : seuls comptent pour le contrôle les droits détenus par ARGOS et par DELTA, contrôlée exclusivement. Les 5 % de FARO, sous contrôle conjoint, ne s'y ajoutent pas (25 % et non 30 %). L'influence notable, présumée à 20 %, est confirmée par le siège au conseil. Pour l'intérêt, la chaîne via FARO est retenue en ANC, comme dans le corrigé du sujet zéro pour une chaîne via une entité non intégrée globalement [F03 § 4.2 ; aucune règle chiffrée dans l'ANC 2020-01].
- **GAÏA** : moins de 20 %, sans représentation ni relations significatives, donc ni contrôle ni influence notable.

---

### 1.2 Modifications en IFRS (3 pts)

- **FARO (1,5 pt)** : c'est une société distincte et le pacte ne donne aux associés aucun droit direct sur ses actifs ni d'obligation directe sur ses passifs. FARO est donc une **coentreprise** au sens d'IFRS 11, qui doit être **mise en équivalence** [V IFRS 11 § 24]. L'intégration proportionnelle n'existe pas pour les coentreprises en IFRS.
- **ERIS (1,5 pt)** : la part du groupe dans une entreprise associée ne tient pas compte des participations détenues par d'autres entreprises associées ou coentreprises [V IAS 28 § 27]. La chaîne via FARO est coupée : intérêt = 15 + 50 % × 10 = **20 %** (au lieu de 22 %).
- CALYPSO, DELTA et GAÏA : aucun changement.

---

### 1.3 Coût d'acquisition et écart d'acquisition ANC (4 pts)

**Coût d'acquisition (1,5 pt).** Prix + coûts directement imputables nets de l'économie d'impôt [V ANC art. 231-2] : 2 400 000 + 80 000 × (1 – 25 %) = **2 460 000 €**.

**Actif net identifiable réévalué au 01/01/2024 (1,5 pt)**

| Élément | Montant |
|---|---:|
| Capitaux propres de CALYPSO (1 000 000 + 1 200 000) | 2 200 000 |
| Écart d'évaluation sur terrain (900 000 – 500 000) | + 400 000 |
| Impôt différé passif sur l'écart (25 %) | – 100 000 |
| **Actif net réévalué** | **2 500 000** |

Un impôt différé passif est constaté sur l'écart d'évaluation du terrain : l'exception de l'art. 272-10 ne vise que certains actifs incorporels [V ANC art. 232-1 et 272-10].

**Écart d'acquisition (1 pt)** : 2 460 000 – 80 % × 2 500 000 = **460 000 €**. Il est non amorti (durée non limitée) et sans dépréciation [V art. 231-11].

---

### 1.4 Goodwill IFRS (4 pts)

Les frais d'acquisition sont comptabilisés en **charges** [V IFRS 3 § 53] : la contrepartie transférée est de 2 400 000 €.

| | Calcul | Goodwill |
|---|---|---:|
| Goodwill partiel (PNC à la quote-part d'actif net) | 2 400 000 – 80 % × 2 500 000 | **400 000** |
| Goodwill complet (PNC à la juste valeur) | 2 400 000 + 640 000 – 2 500 000 | **540 000** |

(1 pt par calcul ; 1 pt pour la règle [V IFRS 3 § 19 et 32].)

**Commentaire (1 pt).** L'écart de 140 000 € (640 000 – 20 % × 2 500 000) correspond au goodwill attribuable aux minoritaires. Le goodwill complet augmente l'actif et les intérêts minoritaires. Le choix se fait regroupement par regroupement. L'écart avec l'ANC (460 000) s'explique par les frais d'acquisition, inclus dans le coût en ANC et passés en charges en IFRS.

---

### 1.5 Retraitements de CALYPSO au 31/12/2026

Les écritures complètes sont dans `corrige.yaml`. Comptes de consolidation : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge d'impôt différé ; `RES_CR` = contrepartie au compte de résultat.

#### a. Écart d'évaluation (2 pts)

Comptabilisé lors de la première consolidation, il est repris à chaque clôture en réserves, puisqu'il est antérieur à l'exercice [V ANC art. 231-9 et 272-13].

**C1 (bilan)** : débit 211 Terrains 400 000 ; crédit IDP 100 000 ; crédit RSV.CALYPSO 300 000.

#### b. Amortissements dérogatoires (4 pts)

Les écritures passées pour la seule application de la législation fiscale sont éliminées [V ANC art. 272-1]. La provision ayant été déduite fiscalement, son élimination crée une différence temporaire imposable, d'où un **impôt différé passif**.

| | Réserves (solde au 31/12/2025) | Résultat (dotation 2026) | Bilan au 31/12/2026 |
|---|---:|---:|---:|
| Avant impôt | + 45 000 | + 15 000 | 145 : – 60 000 |
| Impôt différé 25 % | – 11 250 | – 3 750 | IDP : 15 000 |
| **Net** | **+ 33 750** | **+ 11 250** | |

**C2 (bilan)** : débit 145 Amortissements dérogatoires 60 000 ; crédit IDP 15 000 ; crédit RSV.CALYPSO 33 750 ; crédit RST.CALYPSO 11 250.
**C2R (compte de résultat)** : crédit 6872 Dotations aux provisions réglementées 15 000 ; débit CH_ID 3 750 ; débit RES_CR 11 250.

#### c. Crédit-bail (6 pts)

Le groupe inscrit à l'actif le bien pris en crédit-bail et au passif l'emprunt correspondant. Au résultat, la redevance est remplacée par une dotation aux amortissements et une charge financière [V ANC art. 272-2].

**Tableau d'emprunt 2026 (1,5 pt)**

| Capital au 01/01/2026 | Intérêts 5 % | Redevance | Remboursement du capital | Capital au 31/12/2026 |
|---:|---:|---:|---:|---:|
| 410 000 | 20 500 | 94 700 | 74 200 | **335 800** |

**Impact (1,5 pt).** Le contrat ayant été signé en 2026, il n'y a pas d'impact sur les réserves.

| | Montant |
|---|---:|
| Dotation aux amortissements (410 000 / 5) | – 82 000 |
| Intérêts | – 20 500 |
| Annulation de la redevance | + 94 700 |
| Impact avant impôt sur le résultat | **– 7 800** |
| Impôt différé actif (25 %) | + 1 950 |
| **Impact net sur le résultat** | **– 5 850** |

Contrôle : VNC de la machine (410 000 – 82 000 = 328 000) – dette (335 800) = – 7 800.

**C3 (bilan, 1,5 pt)** : débit 2154 Matériels industriels 410 000 ; débit IDA 1 950 ; débit RST.CALYPSO 5 850 ; crédit 28154 Amortissements 82 000 ; crédit 164 Emprunts 335 800.
**C3R (compte de résultat, 1,5 pt)** : débit 6811 Dotations aux amortissements 82 000 ; débit 6611 Intérêts 20 500 ; crédit 6122 Crédit-bail mobilier 94 700 ; crédit CH_ID 1 950 ; crédit RES_CR 5 850.

#### d. Cession interne de la machine (6 pts)

La plus-value interne est éliminée en totalité et attribuée à l'entité qui l'a réalisée, CALYPSO, donc partagée entre le groupe et ses minoritaires. Le bien est ramené à sa valeur historique et l'impôt est corrigé [V ANC art. 251-2].

**Calcul (2 pts)**

| | Montant |
|---|---:|
| Plus-value de cession chez CALYPSO (140 000 – 80 000) | 60 000 |
| Dotation 2026 chez ARGOS (140 000 / 4) | 35 000 |
| Dotation sur la valeur historique (80 000 / 4, soit 200 000 / 10) | 20 000 |
| Excédent de dotation à annuler | – 15 000 |
| **Plus-value non réalisée au 31/12/2026 (impact avant impôt)** | **45 000** |
| Impôt différé actif (25 %) | 11 250 |
| **Impact net sur le résultat** | **– 33 750** |

Contrôle : VNC chez ARGOS (140 000 – 35 000 = 105 000) – VNC consolidée (200 000 – 140 000 = 60 000) = 45 000.

**C4 (bilan, 2 pts)** : débit 2154 Matériels industriels 60 000 (retour à 200 000) ; débit IDA 11 250 ; débit RST.CALYPSO 33 750 ; crédit 28154 Amortissements 105 000 (retour à 140 000).
**C4R (compte de résultat, 2 pts)** : débit 757 Produits des cessions d'immobilisations 140 000 ; crédit 657 Valeurs comptables des immobilisations cédées 80 000 ; crédit 6811 Dotations aux amortissements 15 000 ; crédit CH_ID 11 250 ; crédit RES_CR 33 750.

Les comptes 675 et 775, supprimés du PCG 2026, ne doivent plus être utilisés [F99]. En PCG 2026, les cessions d'immobilisations passent par les comptes 757 et 657.

---

### 1.6 Dividendes (2 pts)

Les dividendes intra-groupe sont éliminés en totalité [V ANC art. 251-2]. ARGOS a reçu 80 % × 200 000 = **160 000 €**. Ce montant est retiré de son résultat et reclassé en réserves. La part versée aux minoritaires (40 000 €) est sortie du groupe et n'est pas éliminée.

**C5 (bilan)** : débit RST.ARGOS 160 000 ; crédit RSV.ARGOS 160 000.
**C5R (compte de résultat)** : débit 761 Produits de participations 160 000 ; crédit RES_CR 160 000.

---

### 1.7 Partage des capitaux propres de CALYPSO (5 pts)

**Incorporation des frais d'acquisition (1 pt).** Pour éliminer les titres à leur coût consolidé (2 460 000 €), on y ajoute les frais d'acquisition nets d'impôt, passés en charges par ARGOS en 2024 [V art. 231-2].
**C6** : débit 261.ARGOS Titres CALYPSO 60 000 ; crédit RSV.ARGOS 60 000.

**Capitaux propres retraités de CALYPSO (1,5 pt)**

| | Capital | Réserves | Résultat | Total |
|---|---:|---:|---:|---:|
| Comptes individuels | 1 000 000 | 1 500 000 | 400 000 | 2 900 000 |
| a. Écart d'évaluation net | | + 300 000 | | + 300 000 |
| b. Amortissements dérogatoires | | + 33 750 | + 11 250 | + 45 000 |
| c. Crédit-bail | | | – 5 850 | – 5 850 |
| d. Plus-value interne | | | – 33 750 | – 33 750 |
| **Retraités** | **1 000 000** | **1 833 750** | **371 650** | **3 205 400** |

La provision de 60 000 € figurant dans les capitaux propres individuels est absorbée par le retraitement b : 45 000 nets (en réserves et résultat) et 15 000 en impôt différé passif.

**Partage (1,5 pt)**

| | Total | Groupe 80 % | Minoritaires 20 % |
|---|---:|---:|---:|
| Capital et réserves (2 833 750) | 2 833 750 | 2 267 000 | 566 750 |
| – Titres éliminés | | – 2 460 000 | |
| + Écart d'acquisition | | + 460 000 | |
| **Réserves consolidées** | | **267 000** | **566 750** |
| **Résultat** (371 650) | 371 650 | **297 320** | **74 330** |

Contrôle : réserves groupe = 80 % × (1 833 750 – 1 500 000 de réserves réévaluées à l'acquisition) = 267 000.

**C7 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.CALYPSO Capital CALYPSO | 1 000 000 | |
| RSV.CALYPSO Réserves CALYPSO retraitées | 1 833 750 | |
| RST.CALYPSO Résultat CALYPSO retraité | 371 650 | |
| EA Écart d'acquisition | 460 000 | |
| 261.ARGOS Titres CALYPSO | | 2 460 000 |
| RSV_G Réserves consolidées – groupe | | 267 000 |
| RST_G Résultat consolidé – groupe | | 297 320 |
| RSV_M Intérêts minoritaires – capital et réserves | | 566 750 |
| RST_M Intérêts minoritaires – résultat | | 74 330 |
| **Total** | **3 665 400** | **3 665 400** |

---

### Réponses tolérées
- **1.1** : un « % minoritaires » présenté pour FARO et ERIS (contrôle – intérêt), selon la présentation du corrigé du sujet zéro.
- **1.5** : écritures de bilan et de compte de résultat regroupées, si le candidat distingue clairement l'impact sur les réserves de l'impact sur le résultat.
- **1.5 d** : imputation de la plus-value éliminée au résultat consolidé sans la rattacher explicitement à CALYPSO, à condition que le partage (1.7) en tienne compte.
- **1.7** : sans l'écriture C6, titres éliminés à 2 400 000 € et réserves groupe de 327 000 € (267 000 + 60 000). L'écart d'acquisition doit rester de 460 000 €.

### Erreurs fréquentes
- **Contrôle et intérêt confondus** : ERIS à 30 % de contrôle, en ajoutant les droits de FARO, ou DELTA à 50 % de contrôle, en multipliant les pourcentages.
- **Frais d'acquisition** : coût d'acquisition sans les frais nets d'impôt (`JUR-G02`, rapport 2025), ou frais inclus dans le coût en IFRS.
- **Écart d'évaluation** : impôt différé passif oublié, ce qui fausse à la fois l'actif net réévalué et l'écart d'acquisition.
- **Réserves et résultat confondus** : amortissements dérogatoires antérieurs portés en résultat 2026. Le jury relève une méthodologie de passage aux comptes consolidés mal maîtrisée et des retraitements peu justifiés (`JUR-G01`, `JUR-G04`, `JUR-G06`).
- **Plus-value interne** : la correction des amortissements (15 000 €) est oubliée, ou la plus-value est attribuée à ARGOS alors que CALYPSO, vendeuse, l'a réalisée.
- **Dividendes** : élimination de la totalité des 200 000 € au lieu de la seule quote-part reçue par ARGOS.
