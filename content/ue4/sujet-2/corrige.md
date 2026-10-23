# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 2

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F13 (`ue4/fiches/`, à jour au 22 ou 23/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.7 | `exercices/ex03_consolidation` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.8 | `exercices/ex02_apport_partiel` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.10 | `exercices/ex04_audit_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

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

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification | `1.1.a` Définir les opérations de restructuration | 2 |
| 2.2 Titres émis | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 3 |
| 2.3 Mode de valorisation | `1.2.c` Déterminer le mode de valorisation des apports | 4 |
| 2.4 Valeur des apports, prime | `1.2.d` Calculer et composer les apports | 3 |
| 2.5 Écritures BORÉE | `1.3.a` Écritures chez la bénéficiaire et l'apporteuse | 4 |
| 2.6 Écritures ATLAS | `1.3.a` Écritures chez la bénéficiaire et l'apporteuse | 3 |
| 2.7 Régime fiscal | `1.1.b` Régime fiscal de droit commun et régime de faveur | 3 |
| 2.8 Capitaux propres et analyse | `1.4.a` Restituer au dirigeant les impacts de l'opération | 3 |
| **Total** | | **25** |

---

### 2.1 Qualification de l'opération (2 pts)

Il s'agit d'un **apport partiel d'actif** : ATLAS apporte un ensemble d'actifs et de passifs constituant une branche autonome, et reçoit en échange des titres de la bénéficiaire, BORÉE [V PCG art. 710-2] (1 pt).

Différences (1 pt) :
- avec une **fusion** : ATLAS ne disparaît pas. Elle continue d'exploiter ses deux autres divisions, et ce sont ATLAS elle-même, et non ses associés, qui reçoit les titres BORÉE ;
- avec une **cession** : la contrepartie n'est pas du numéraire mais des titres de la bénéficiaire. ATLAS reste ainsi indirectement exposée à l'activité apportée.

---

### 2.2 Titres émis et répartition du capital (3 pts)

**Valeur réelle d'une action BORÉE (0,5 pt)** : 2 400 000 / 40 000 = **60 €**.

**Actions à émettre (1 pt)** : la rémunération est calculée sur la **valeur réelle** de la branche, qui exprime le rapport de valeurs entre les parties : 3 600 000 / 60 = **60 000 actions**.

**Augmentation de capital (0,5 pt)** : 60 000 × 10 = **600 000 €**.

**Répartition du capital après l'opération (1 pt)** — 100 000 actions :

| Actionnaire | Avant | Après | % après |
|---|---:|---:|---:|
| ATLAS | 0 | 60 000 | **60 %** |
| Famille DUVAL | 28 000 | 28 000 | 28 % |
| Autres actionnaires | 12 000 | 12 000 | 12 % |
| **Total** | **40 000** | **100 000** | **100 %** |

---

### 2.3 Mode de valorisation des apports (4 pts)

**Situation de contrôle (1 pt).** Avant l'opération, ATLAS et BORÉE n'ont aucun lien en capital et ne sont pas contrôlées par une même entité : l'opération est réalisée **sous contrôle distinct** [V PCG art. 741-1].

**Sens de l'opération (1,5 pt).** Un apport est **à l'envers** lorsque l'apporteuse prend le contrôle de la bénéficiaire [V PCG art. 742-2]. Avec 60 % du capital après l'opération, ATLAS prend le contrôle de BORÉE, tandis que la famille DUVAL, qui détenait 70 %, n'en a plus que 28 %. L'apport est donc **à l'envers**. Économiquement, l'initiatrice est ATLAS et la cible est BORÉE [V art. 730-1].

**Conclusion (1,5 pt).** Pour une opération sous contrôle distinct à l'envers, les apports sont évalués à la **valeur comptable** [V PCG art. 743-1, cas 3]. La cible étant BORÉE, ce sont ses actifs qui changent de contrôle. Or ils ne figurent pas dans le traité : seuls y figurent les éléments apportés par l'initiatrice, qu'il n'y a pas lieu de réévaluer.

---

### 2.4 Valeur des apports et prime d'apport (3 pts)

**Valeur comptable des apports (1 pt)**

| Élément | Montant |
|---|---:|
| Entrepôts (VNC) | 1 200 000 |
| Camions (VNC) | 400 000 |
| Emballages | 100 000 |
| Créances clients | 300 000 |
| – Provision pour litige | – 20 000 |
| – Dettes fournisseurs | – 180 000 |
| **Actif net comptable apporté** | **1 800 000** |

**Prime d'apport (1 pt)** : 1 800 000 – 600 000 = **1 200 000 €**.

**Libération du capital (1 pt).** L'actif net comptable apporté (1 800 000 €) couvre l'augmentation de capital (600 000 €). La dérogation de l'art. 743-3, qui imposerait les valeurs réelles en cas d'insuffisance, ne joue pas [V PCG art. 743-3].

Le nombre de titres est calculé sur la valeur réelle (3 600 000), mais l'apport est comptabilisé à la valeur comptable (1 800 000). Les deux ne se contredisent pas : la valeur réelle sert à fixer le rapport d'échange, la valeur comptable à enregistrer les apports.

---

### 2.5 Écritures chez BORÉE au 01/01/2027 (4 pts)

Écritures complètes dans `corrige.yaml` (B1, B2), toutes équilibrées. Schéma type : `gabarits/ecritures_types/05_apport_partiel_actif.yaml`.

**B1 — Augmentation de capital (1,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 1 800 000 | |
| 101 Capital | | 600 000 |
| 1043 Primes d'apport | | 1 200 000 |

**B2 — Réalisation de l'apport (2,5 pts).** En valeur comptable, la bénéficiaire reprend les **valeurs brutes et les amortissements** de l'apporteuse [V BOI-IS-FUS-10-20-40-20 § 170-180, voir F01 § 3.2].

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments | 2 000 000 | |
| 2182 Matériel de transport | 1 000 000 | |
| 326 Emballages | 100 000 | |
| 411 Clients | 300 000 | |
| 28131 Amortissements des bâtiments | | 800 000 |
| 28182 Amortissements du matériel de transport | | 600 000 |
| 1511 Provisions pour litiges | | 20 000 |
| 401 Fournisseurs | | 180 000 |
| 4561 Associés – Comptes d'apport en société | | 1 800 000 |

---

### 2.6 Écritures chez ATLAS au 01/01/2027 (3 pts)

**A1 — Sortie de la branche et réception des titres (2 pts).** ATLAS inscrit les titres BORÉE reçus pour la valeur de l'apport retenue au traité, soit la valeur comptable [F01 § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation (60 000 titres BORÉE) | 1 800 000 | |
| 28131 Amortissements des bâtiments | 800 000 | |
| 28182 Amortissements du matériel de transport | 600 000 | |
| 1511 Provisions pour litiges | 20 000 | |
| 401 Fournisseurs | 180 000 | |
| 2131 Bâtiments | | 2 000 000 |
| 2182 Matériel de transport | | 1 000 000 |
| 326 Emballages | | 100 000 |
| 411 Clients | | 300 000 |

**Résultat de l'opération (1 pt).** Aucun résultat n'est dégagé : les titres sont inscrits pour la valeur nette des éléments apportés (1 800 000 €). Les éléments de la division sont simplement remplacés à l'actif d'ATLAS par une participation de même montant.

*Variante admise :* passage par un compte de créance sur la bénéficiaire (compte 46), soldé à la réception des titres. Les comptes 675 et 775 sont à proscrire : ils ont été supprimés du PCG en 2026 [F99].

---

### 2.7 Régime fiscal (3 pts)

**Condition (1 pt).** L'apport bénéficie de plein droit du régime de faveur des fusions (art. 210 A) s'il porte sur une ou plusieurs **branches complètes d'activité** [V CGI art. 210 B-1]. La branche complète est « l'ensemble des éléments d'actif et de passif d'une division d'une société qui constituent, du point de vue de l'organisation, une exploitation autonome, c'est-à-dire un ensemble capable de fonctionner par ses propres moyens » [V BOI-IS-FUS-20-20 § 10]. Son autonomie s'apprécie selon l'organisation de l'apporteuse, à la date de réalisation de l'apport [V même BOI § 20 et 90]. Depuis le 01/01/2018, aucun engagement de conservation des titres n'est exigé [V BOI-IS-FUS-20-40, remarque]. À défaut de branche complète, le régime de faveur n'est possible que sur agrément [V CGI art. 210 B-3].

**Appréciation (0,5 pt).** La condition est remplie [V BOI-IS-FUS-20-20 § 50 à 90] :
- **activité réellement exercée** et organisation distincte des autres divisions (centre de profit autonome) ;
- **installations, clientèle et personnel propres**, le personnel étant transféré avec l'activité ;
- l'apport ne porte pas sur des **éléments isolés** : les entrepôts et les camions sont apportés avec l'exploitation qui les utilise ;
- le recours temporaire aux **services administratifs communs** d'ATLAS ne fait pas obstacle à l'autonomie : ces services sont rattachés aux branches pour leur quote-part.

**Conséquences (1,5 pt)**
- **ATLAS** : la plus-value réalisée lors d'une cession ultérieure des titres BORÉE sera calculée par référence à la **valeur fiscale qu'avaient les biens apportés** dans ses écritures [V CGI art. 210 B-2]. Ici, cette valeur est égale à la valeur comptable des titres (1 800 000 €) : la plus-value latente de 1 800 000 € (3 600 000 – 1 800 000) sera imposée lors de la cession des titres.
- **Provision pour litige** : chez ATLAS, elle n'est pas imposée du fait de l'apport ; elle ne le serait que si elle était devenue sans objet [V BOI-IS-FUS-20-40-30 § 110]. Chez BORÉE, la bénéficiaire reprend les provisions de l'apporteuse afférentes aux éléments apportés [V CGI art. 210 A-3-a, applicable aux APA par renvoi du 210 B-1]. Les 20 000 €, déduits par ATLAS, seront compris dans le résultat imposable de BORÉE lors de leur reprise, si la provision devient sans objet.

---

### 2.8 Capitaux propres de BORÉE et analyse (3 pts)

**Capitaux propres (1 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital | 400 000 | + 600 000 | 1 000 000 |
| Primes d'apport | 0 | + 1 200 000 | 1 200 000 |
| Réserves | 1 100 000 | | 1 100 000 |
| **Total** | **1 500 000** | **+ 1 800 000** | **3 300 000** |

**Explication pour la famille DUVAL (grille de niveaux, 2 pts)**

| Niveau | 0 | 1 | 1,5 | 2 |
|---|---|---|---|---|
| Attendu | Absence ou explication erronée | Rappel de la règle (contrôle distinct, envers, valeur comptable) | Règle et justification économique | Règle, justification et chiffrage de l'alternative |

Idées attendues :
- **Pourquoi la valeur comptable** : économiquement, ce n'est pas BORÉE qui acquiert la division, c'est ATLAS qui prend le contrôle de BORÉE. Les actifs qui changent de contrôle sont ceux de BORÉE ; ceux de la division restent sous le contrôle d'ATLAS et ne sont pas réévalués. Comptabiliser la division à sa valeur réelle reviendrait à constater chez BORÉE une plus-value sur des actifs dont le contrôle ne change pas.
- **Ce qu'aurait changé la valeur réelle** :
  - chez BORÉE, actifs réévalués (entrepôts + 500 000, camions + 100 000) et fonds commercial de 1 200 000 € (3 600 000 – 2 400 000 d'actif net réel identifié), soit des amortissements futurs plus élevés ;
  - prime d'apport de 3 000 000 € au lieu de 1 200 000 € ;
  - chez ATLAS, titres inscrits pour 3 600 000 € et plus-value d'apport de 1 800 000 €.
- **Pour la famille DUVAL** : elle perd le contrôle de BORÉE (de 70 % à 28 %), bien que les capitaux propres comptables passent de 1 500 000 € à 3 300 000 €. C'est la conséquence de la valeur relative des apports, la division valant 1,5 fois BORÉE.

---

### Réponses tolérées
- **2.2** : calcul du nombre de titres par un rapport de valeurs (3 600 000 / 2 400 000 = 1,5 titre émis pour 1 titre existant, soit 40 000 × 1,5 = 60 000).
- **2.6** : passage par un compte de créance (46) sur la bénéficiaire, soldé à la réception des titres.
- **2.7** : tout raisonnement correct sur le sort de la provision, même sans la référence au 210 A-3-a.

### Erreurs fréquentes
- Retenir la **valeur réelle** au motif que les sociétés sont sous contrôle distinct, sans analyser le **sens** de l'opération. C'est le piège principal du sujet (cas 3 du tableau de l'art. 743-1).
- Calculer le nombre de titres sur la valeur comptable (1 800 000 / 60 = 30 000) : la parité se fixe sur les valeurs réelles.
- Calculer la prime sur la valeur réelle alors que l'apport est comptabilisé à la valeur comptable (`JUR-R01`).
- Inscrire les éléments apportés pour leur valeur nette, sans reprendre les valeurs brutes et les amortissements.
- Constater un résultat de cession chez ATLAS, ou utiliser les anciens comptes 675 et 775.

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Signataire, durée, co-commissariat | `3.1.b` Nomination et cessation de fonctions | 3 |
| 3.2 Situations déontologiques | `3.1.c` Principes déontologiques | 3 |
| 3.3 Vérificateur de durabilité | `3.1.b` Nomination et cessation de fonctions | 3 |
| 3.4 Seuils | `3.2.c` Approche par les risques | 2 |
| 3.5 Risques sur les stocks | `3.2.d` Démarche d'audit | 3 |
| 3.6 Opinion | `3.2.e` Portée des opinions | 4 |
| 3.7 Double matérialité | `3.3.b` Principes de construction du reporting | 3 |
| 3.8 Objectif, assurance limitée | `3.4.a` Objectifs de la mission de durabilité | 2 |
| 3.9 Axes et démarche | `3.4.b` Démarche d'audit de durabilité | 3 |
| 3.10 Avis | `3.4.c` Portée des avis | 4 |
| **Total** | | **30** |

---

### Partie A – Cadre d'exercice et déontologie (9 points)

### 3.1 Signataire, durée de la mission, co-commissariat (3 pts)

**Rotation du signataire (1 pt).** Pour une entité d'intérêt public, la personne physique qui signe ne peut certifier les comptes plus de **six exercices consécutifs**, dans la limite de sept années. Elle ne peut y revenir que trois ans après la clôture du sixième exercice certifié [V C. com. L. 821-34 I]. Mme LEROY a signé les comptes 2020 à 2025, soit six exercices : **elle ne peut pas signer les comptes 2026**. Un autre associé d'ARCHE AUDIT doit la remplacer. Elle pourra revenir pour les comptes de 2029 au plus tôt (trois ans après la clôture du 31/12/2025).

**Durée maximale du cabinet (1 pt).** Pour une EIP, la mission d'un même cabinet est limitée à **10 ans**. Un nouveau mandat de six exercices est possible à l'issue d'un **appel d'offres**, et la durée peut atteindre **24 ans** en cas de co-commissariat avec rapport conjoint [V L. 821-45]. Le renouvellement de 2026, décidé après appel d'offres, est régulier : ARCHE AUDIT peut exercer jusqu'aux comptes 2031, soit 12 exercices.

**Co-commissariat (1 pt).** Une entité astreinte à publier des comptes consolidés doit désigner **au moins deux commissaires aux comptes** [V L. 821-41]. Ils doivent appartenir à des structures distinctes, sans lien ni réseau commun [V code de déontologie art. 24]. La désignation d'ARCHE AUDIT comme seul commissaire aux comptes est **irrégulière** : l'assemblée doit désigner un second commissaire aux comptes. À défaut, la désignation peut être demandée en justice [V L. 821-47].

### 3.2 Situations déontologiques (3 pts)

Méthode attendue : identifier le lien en cause, le qualifier, puis conclure [F10 § 8].

**Situation 1 – Attestation sur les ratios bancaires (1,5 pt).** C'est un service autre que la certification des comptes. Pour une EIP, un tel service, s'il n'est pas interdit, doit être **approuvé par le comité spécialisé** (comité d'audit). Le total des honoraires de ces services est plafonné à **70 % de la moyenne des honoraires de certification des trois derniers exercices** [V L. 821-28 II, L. 821-30 I, L. 821-67 II 6°].

| | Montant |
|---|---:|
| Moyenne des honoraires de certification 2023-2025 : (420 000 + 450 000 + 480 000) / 3 | 450 000 |
| Plafond : 70 % × 450 000 | 315 000 |
| Services autres que la certification en 2026 : 120 000 + 60 000 | 180 000 |

Le plafond est respecté. ARCHE AUDIT peut accepter, après **approbation du comité d'audit** et sous réserve de l'absence de risque d'autorévision. Une lettre de mission spécifique est nécessaire [V R. 821-195].

**Situation 2 – PACS de Lucas avec la cheffe comptable (1,5 pt).** La cheffe comptable tient les comptes et prépare les états financiers : elle occupe une **fonction sensible**. Le PACS est un lien personnel visé par le code de déontologie. Lucas n'étant ni le commissaire aux comptes signataire ni un membre de la direction du cabinet, le lien n'est pas automatiquement incompatible. Il l'est si un **tiers objectif, raisonnable et informé** conclurait que l'indépendance est compromise [V code de déontologie art. 31 et 32]. Un assistant qui audite les comptes établis par sa partenaire de PACS crée un risque manifeste d'atteinte à l'indépendance en apparence. Conduite à tenir : **retirer Lucas de l'équipe d'audit de NORDALIS sans délai** (mesure de sauvegarde) et documenter l'analyse [V code art. 35 : en tirer « sans délai les conséquences »].

### 3.3 Vérificateur des informations de durabilité (3 pts)

- **Qui (1 pt)** : un **commissaire aux comptes** inscrit sur la liste des CAC habilités à certifier les informations de durabilité, ou un **organisme tiers indépendant (OTI)** accrédité [V L. 232-6-3 III ; L. 822-1]. L'entité peut choisir son commissaire aux comptes des comptes, un autre commissaire aux comptes ou un OTI [V LD 2026, propos liminaires].
- **Organe et durée (1 pt)** : désignation par l'**assemblée générale ordinaire**, sur recommandation du comité d'audit, pour **six exercices** [V L. 821-40, L. 821-44 ; L. 822-17, L. 822-20 pour l'OTI ; FAQ H2A]. Pour une EIP, la règle de rotation de la personne physique (six exercices consécutifs) s'applique aussi [V L. 821-34 II ; L. 822-12].
- **ARCHE AUDIT (1 pt)** : oui, si le cabinet et la personne qui signe sont inscrits sur la liste des commissaires aux comptes habilités pour la durabilité. Le rapport est alors signé par un commissaire aux comptes personne physique inscrit sur cette liste [V L. 821-26]. Si la mission est confiée à un autre professionnel, le commissaire aux comptes des comptes et le vérificateur de durabilité sont libérés du secret professionnel l'un envers l'autre [V L. 821-35, L. 822-2].

---

### Partie B – Audit des comptes annuels : le cycle stocks (9 points)

### 3.4 Seuils (2 pts)

| Seuil | Calcul | Montant |
|---|---|---:|
| Seuil de signification | 5 % × 26,0 M€ | **1,3 M€** |
| Seuil de planification | 70 % × 1,3 M€ | **0,91 M€** |

(1 pt pour les calculs.) Les pourcentages sont des hypothèses du cabinet : les NEP ne fixent aucun taux [V NEP 320 § 10 et 17].

**Rôle (1 pt)**
- Le **seuil de signification** est le montant au-delà duquel les décisions économiques ou le jugement fondés sur les comptes sont susceptibles d'être influencés [V NEP 320 § 6]. Il sert à apprécier l'incidence des anomalies relevées sur l'opinion.
- Le **seuil de planification**, inférieur, sert à définir la nature et l'étendue des travaux. Il réduit le risque que le cumul des anomalies non détectées et non corrigées dépasse le seuil de signification [V NEP 320 § 7 et 20].
- Le caractère significatif s'apprécie aussi selon la **nature** de l'anomalie et les circonstances, et pas seulement selon son montant [V NEP 320 § 9].

### 3.5 Risques d'anomalies significatives sur les stocks (3 pts, 1,5 pt par risque)

| Risque | Assertions | Procédures |
|---|---|---|
| **Dépréciation insuffisante** des produits périmés, proches de leur date limite ou visés par l'alerte sanitaire | Évaluation et imputation (solde) | Revue des dates limites et de la rotation des stocks ; suivi du lot visé par l'alerte (rapports d'analyse, décisions des autorités, événements postérieurs à la clôture) ; contrôle des ventes postérieures à la clôture et de leurs prix |
| **Existence** des stocks, en particulier ceux de l'entrepôt loué, comptés par un tiers | Existence ; droits et obligations (solde) | Assistance à l'inventaire physique dans les entrepôts de NORDALIS [V NEP 501] ; pour l'entrepôt loué, **confirmation directe** auprès du prestataire et comptages par sondage [V NEP 505 ; NEP 501] |

Autres réponses acceptées : séparation des exercices sur les achats (flux), exhaustivité des stocks.

### 3.6 Opinion sur les comptes 2026 (4 pts)

**Analyse de l'anomalie (1,5 pt).** La contamination existait au 31/12/2026 : la décision de destruction de janvier 2027 confirme une situation qui existait à la clôture. Le lot devait donc être **déprécié en totalité dans les comptes 2026**. L'anomalie non corrigée est de **1,6 M€**, ce qui dépasse le seuil de signification (1,3 M€) : elle est **significative**. Le résultat et les capitaux propres sont surévalués de 1,6 M€ avant impôt. L'erreur de séparation des exercices (0,2 M€) a été corrigée et n'a pas d'incidence sur l'opinion.

**Opinion (1,5 pt).** L'anomalie significative n'est pas corrigée, mais son incidence est **clairement circonscrite** à un poste et à un montant identifiés. Une réserve formulée avec ces éléments suffit à l'utilisateur pour fonder son jugement. Le commissaire aux comptes **certifie avec réserve pour désaccord**. Il expose le motif dans la partie « Fondement de l'opinion » et en quantifie l'incidence [V NEP 700 § 09-10].

**Opinions écartées (1 pt)**
- **Sans réserve** : impossible, une anomalie significative n'étant pas corrigée.
- **Refus de certifier** : l'incidence est circonscrite et une réserve suffit.
- **Réserve pour limitation, ou impossibilité de certifier** : aucune limitation, puisque l'existence des stocks de l'entrepôt loué a pu être vérifiée par des procédures alternatives probantes.

---

### Partie C – Durabilité (12 points)

### 3.7 Double matérialité (3 pts)

**Principe (1 pt).** Un enjeu est matériel s'il l'est au titre de la **matérialité d'impact**, de la **matérialité financière**, ou des deux [V ESRS 1 (2023) § 28 ; ESRS 1 (2026) § 35]. Les deux dimensions s'apprécient en tenant compte de leurs interactions.
- **Matérialité d'impact** : impacts réels ou potentiels de l'entité sur la population ou l'environnement, y compris par sa **chaîne de valeur**. Un impact négatif s'apprécie selon sa **gravité** (ampleur, étendue, caractère irrémédiable) et, s'il est potentiel, sa probabilité [V ESRS 1 (2026) § 39-40].
- **Matérialité financière** : enjeux qui ont, ou peuvent raisonnablement avoir, des effets financiers sur l'entité (performance, situation financière, flux de trésorerie, accès au financement, coût du capital), y compris par ses **dépendances** à l'égard de ressources naturelles [V ESRS 1 (2026) § 47-50].

**Application (2 pts, 1 pt par enjeu)**

| Enjeu | Dimension | Analyse |
|---|---|---|
| Surexploitation des stocks de poissons de l'Atlantique Nord | **Impact** (négatif, sur la biodiversité marine) | Impact situé dans la **chaîne de valeur amont** : NORDALIS ne pêche pas, mais 70 % de ses achats proviennent de pêcheries surexploitées. Gravité élevée (ampleur, étendue, épuisement difficilement réversible des stocks) |
| Réduction des quotas et hausse des prix d'achat (+ 18 %) | **Financière** (risque) | **Dépendance** à une ressource naturelle : hausse du coût d'approvisionnement, risque de rupture, pression sur les marges. Effet financier déjà observé en 2026 |

Autres réponses acceptées :
- émissions des entrepôts et des camions frigorifiques (impact sur le climat) ;
- exigence de certification « pêche durable » des distributeurs, qui crée un risque de déréférencement et une opportunité commerciale (matérialité financière).

L'interaction entre les deux dimensions est valorisée : la surexploitation (impact) est à l'origine de la baisse des quotas (risque financier).

### 3.8 Objectif et niveau d'assurance (2 pts)

**Objectif (1 pt).** Le vérificateur émet un **avis** sur la conformité des informations de durabilité aux dispositions légales et aux ESRS. Cet avis porte notamment sur le processus de détermination des informations et sur le respect des exigences de publication de la taxonomie [V L. 821-54 II]. Il fait l'objet d'un **rapport de certification** destiné à l'assemblée qui statue sur les comptes. La mission ne garantit ni la viabilité ni la qualité de la gestion de l'entité [V L. 821-55].

**Assurance limitée (1 pt).** La mission repose sur une **assurance limitée** [V LD 2026, niveau d'assurance ; directive 2013/34 art. 34 rédaction 2026/470]. Les vérifications sont moindres en nature, en étendue et en durée que dans une mission d'assurance raisonnable. La conclusion est exprimée sous une **forme négative** : le vérificateur n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes. L'audit des comptes repose au contraire sur une **assurance raisonnable**, exprimée sous une **forme positive** : les comptes sont réguliers et sincères et donnent une image fidèle. Depuis 2026, le droit européen ne prévoit plus de normes d'assurance raisonnable pour la durabilité : l'assurance limitée est le seul niveau légal [V directive 2026/470, considérant 4].

### 3.9 Axes et démarche (3 pts)

**Axes de vérification (1,5 pt)** [V LD 2026 § 2]
1. Conformité aux ESRS du **processus** de détermination des informations publiées (analyse de double matérialité), y compris la **consultation du comité social et économique** ;
2. Conformité des **informations** de durabilité publiées dans le rapport de gestion ;
3. Respect des exigences de publication de la **taxonomie** ;
4. **Balisage** électronique : non traité tant que les règles n'ont pas été adoptées. La mission porte donc aujourd'hui sur trois axes.

**Principales étapes (1,5 pt)** [V LD 2026 § 4 à 17]
- lettre de mission et prise de connaissance de l'entité (modèle d'affaires, chaîne de valeur, gouvernance, processus de production des informations) ;
- planification, avec identification des informations présentant un risque important de non-conformité ou de fortes attentes des utilisateurs ;
- vérifications par axe ;
- lecture d'ensemble et cohérence avec les états financiers, en échangeant avec le commissaire aux comptes des comptes ;
- appréciation des éléments collectés et événements postérieurs ;
- communication avec la gouvernance et le comité d'audit ;
- rapport de certification, avec un avis par axe.

### 3.10 Avis du vérificateur (4 pts)

Les avis sont émis **axe par axe** [V LD 2026 § 17].

| Axe | Constat | Avis |
|---|---|---|
| 1. Processus | Analyse de double matérialité documentée, couvrant la chaîne de valeur ; CSE consulté | **Avis de conformité** (1 pt) |
| 2. Informations | Émissions directes sous-évaluées de 7 700 tCO2e (25 700 – 18 000, soit 30 %) ; erreur non corrigée ; incidence limitée à cet indicateur | **Avis de conformité assorti d'une réserve motivée** (2 pts) | <!-- ue4check:ignorer -->
| 3. Taxonomie | Informations conformes | **Avis de respect des exigences** (0,5 pt) |
| 4. Balisage | Règles non adoptées | **Aucun avis** : axe non traité (0,5 pt) |

**Justification de l'axe 2.** L'erreur, non corrigée, est d'une importance telle qu'elle remet en cause la conformité de l'information : elle représente 30 % d'un indicateur clé, sur un enjeu climatique suivi de près par les utilisateurs. Son incidence est toutefois **clairement circonscrite** à un indicateur identifié et chiffré, et une réserve motivée suffit à l'utilisateur. On retient donc un avis de conformité assorti d'une réserve motivée, et non un avis de non-conformité. Celui-ci supposerait des incidences non circonscrites ou une réserve insuffisante [V LD 2026 § 17].

Formulation attendue de l'axe 1 (forme négative) : « nous n'avons pas relevé d'erreurs, omissions ou incohérences importantes concernant la conformité du processus mis en œuvre par NORDALIS avec les ESRS » [V LD 2026, annexe 2].

---

### Réponses tolérées
- **3.1** : retour de Mme LEROY exprimé en « trois ans après la fin de sa sixième année de signature », sans date précise.
- **3.2** : pour la situation 2, conclusion à l'incompatibilité pure et simple, si elle est justifiée par la fonction sensible de la cheffe comptable.
- **3.5** : tout couple risque / assertion / procédure cohérent.
- **3.7** : vocabulaire des ESRS de 2023 (« double importance », « incidences »).

### Erreurs fréquentes
- Confondre la rotation du **signataire** (six exercices) et la durée maximale de mission du **cabinet** (10 ans).
- Oublier l'obligation de **deux** commissaires aux comptes pour une entité qui publie des comptes consolidés.
- Traiter l'alerte sanitaire comme un événement postérieur sans incidence sur les comptes 2026, alors qu'elle révèle une situation qui existait à la clôture.
- Émettre un **refus de certifier** pour une anomalie dont l'incidence est circonscrite.
- Confondre « réalité » (flux) et « existence » (solde) (`JUR-A01`).
- Présenter l'assurance raisonnable comme le futur niveau d'assurance de la mission de durabilité, ou le balisage comme un contrôle déjà exigible.
- Émettre un avis unique pour tout l'état de durabilité au lieu d'un avis par axe.
