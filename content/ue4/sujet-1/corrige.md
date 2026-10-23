# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 1

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F13 (`ue4/fiches/`, à jour au 22 ou 23/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.7 | `exercices/ex03_consolidation` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.8 | `exercices/ex01_restructurations` |
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
| 2.1 Mode de valorisation | `1.2.c` Déterminer le mode de valorisation des apports | 3 |
| 2.2 Parité, titres émis | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 3 |
| 2.3 Apports, prime, mali | `1.2.e` Calculer et analyser le boni ou mali de fusion | 3 |
| 2.4 Analyse du mali | `1.2.e` Calculer et analyser le boni ou mali de fusion | 5 |
| 2.5 Écritures au 01/01/2027 | `1.3.b` Adapter les écritures aux détentions préalables | 5 |
| 2.6 Suivi du mali | `1.3.c` Passer les écritures complémentaires | 2,5 |
| 2.7 Régime de faveur | `1.1.b` Régime fiscal de droit commun et régime de faveur | 2 |
| 2.8 Capitaux propres | `1.4.a` Restituer au dirigeant les impacts de l'opération | 1,5 |
| **Total** | | **25** |

---

### 2.1 Mode de valorisation des apports (3 pts)

**Situation de contrôle (1 pt).** HÉLIOS détient 60 % des droits de vote d'ORION : elle la contrôle de manière exclusive (majorité des droits de vote). Une des sociétés participant à l'opération contrôlant préalablement l'autre, l'opération est réalisée **sous contrôle commun** [V PCG art. 741-1 et 741-2].

**Mode de valorisation (1 pt).** Pour une opération sous contrôle commun, les apports sont évalués à la **valeur comptable**, quel que soit le sens de l'opération [V PCG art. 743-1]. Il n'y a pas lieu de réévaluer des actifs qui restent sous le contrôle du même groupe.

**Sens de l'opération (0,5 pt).** SOLARIS, actionnaire principal de HÉLIOS, détient 63,64 % du capital après l'opération (voir 2.2) : elle conserve le contrôle de l'absorbante. La fusion est **à l'endroit**. Ce point ne modifie pas la conclusion.

**Libération du capital (0,5 pt).** La valeur comptable des apports rémunérés (488 000 €, voir 2.3) excède l'augmentation de capital (100 000 €) : l'actif net comptable apporté permet la libération du capital. La dérogation de l'art. 743-3 (retenir les valeurs réelles) ne s'applique pas [V PCG art. 743-3].

---

### 2.2 Parité, titres émis, répartition du capital (3 pts)

**Valeurs unitaires (0,5 pt)**
- HÉLIOS : 8 000 000 / 50 000 = **160 €**
- ORION : 2 000 000 / 20 000 = **100 €**

**Parité et équité (0,5 pt).** Rapport d'échange : 100 / 160 = 5 / 8, soit **5 actions HÉLIOS pour 8 actions ORION**. La parité est équitable : 8 × 100 = 800 € = 5 × 160 €.

**Fusion-renonciation (0,75 pt).** HÉLIOS ne peut pas recevoir ses propres actions en échange des 12 000 titres ORION qu'elle détient : seules les actions détenues par les **autres associés** sont échangées [V C. com. L. 236-3 II]. Titres à rémunérer : 20 000 – 12 000 = **8 000 titres**.

**Titres émis et augmentation de capital (0,75 pt).** 8 000 × 5 / 8 = **5 000 actions** nouvelles, soit une augmentation de capital de 5 000 × 20 = **100 000 €**.

**Répartition du capital après l'opération (0,5 pt)** — 55 000 actions :

| Actionnaire | Actions | % |
|---|---:|---:|
| SOLARIS | 35 000 | 63,64 % |
| Autres actionnaires historiques de HÉLIOS | 15 000 | 27,27 % |
| Anciens actionnaires minoritaires d'ORION | 5 000 | 9,09 % |
| **Total** | **55 000** | **100 %** |

---

### 2.3 Apports, prime de fusion, mali (3 pts)

**Actif net comptable apporté (1 pt).** 1 650 000 – 230 000 (emprunts) – 200 000 (fournisseurs) = **1 220 000 €**. Il correspond aux capitaux propres d'ORION (1 000 000 + 150 000 + 50 000 + 20 000) : les amortissements dérogatoires sont des provisions réglementées, classées en capitaux propres.

**Répartition (0,5 pt)**

| | % | Montant |
|---|---:|---:|
| Part rémunérée (associés autres que HÉLIOS) | 40 % | 488 000 |
| Part non rémunérée (droits de HÉLIOS) | 60 % | 732 000 |
| **Total** | | **1 220 000** |

**Prime de fusion avant imputation (0,75 pt)** : 488 000 – 100 000 = **388 000 €**.

**Résultat de l'annulation des titres (0,75 pt)** : 732 000 – 1 260 000 = **– 528 000 €**, soit un **mali de fusion** de 528 000 € [V PCG art. 745-3].

---

### 2.4 Analyse du mali (5 pts)

**Plus-values latentes et passif non comptabilisé d'ORION, à 100 % (1,5 pt)**

| Élément | Valeur réelle | Valeur comptable | Écart |
|---|---:|---:|---:|
| Terrain | 420 000 | 300 000 | + 120 000 |
| Constructions | 620 000 | 500 000 | + 120 000 |
| Matériel industriel | 150 000 | 150 000 | 0 |
| Stocks | 260 000 | 260 000 | 0 |
| Engagements de retraite (non comptabilisés) | 40 000 | 0 | – 40 000 |

**Fonds commercial non comptabilisé (1 pt).** Actif net réel identifié : 420 000 + 620 000 + 150 000 + 260 000 + 340 000 + 100 000 – 230 000 – 200 000 – 40 000 = 1 420 000 €. Fonds commercial = 2 000 000 – 1 420 000 = **580 000 €**.
Contrôle : 1 220 000 + 120 000 + 120 000 – 40 000 + 580 000 = 2 000 000 €.

**Décomposition du mali (1 pt + 0,75 pt).** Le mali technique correspond, à hauteur de la participation, aux plus-values latentes sur les actifs (comptabilisés ou non, y compris le fonds commercial), déduction faite des passifs non comptabilisés [V PCG art. 745-4]. Aucun actif n'étant destiné à être cédé à brève échéance, les plus-values sont retenues pour leur montant brut.

| | Calcul | Montant |
|---|---|---:|
| Mali technique | 60 % × (120 000 + 120 000 + 580 000 – 40 000) | **468 000** |
| Vrai mali | 528 000 – 468 000 | **60 000** |
| **Mali total** | | **528 000** |

Le **vrai mali** (60 000 €) traduit une dépréciation de la participation : HÉLIOS a payé 1 260 000 € une participation qui vaut aujourd'hui 60 % × 2 000 000 = 1 200 000 €. Il est comptabilisé dans le **résultat financier** de l'exercice de l'opération [V PCG art. 745-4].

**Affectation du mali technique (0,75 pt).** Le mali technique (468 000 €) est supérieur aux plus-values latentes sur les actifs identifiés hors fonds commercial (60 % × 240 000 = 144 000 €) : il est affecté à ces actifs, et le solde au fonds commercial [V PCG art. 745-5], dans les comptes prévus par l'art. 745-6.

| Actif sous-jacent | Calcul | Mali affecté | Compte |
|---|---|---:|---|
| Terrain | 60 % × 120 000 | 72 000 | 2187 Mali de fusion sur actifs corporels |
| Constructions | 60 % × 120 000 | 72 000 | 2187 Mali de fusion sur actifs corporels |
| Fonds commercial (solde) | 468 000 – 144 000 | 324 000 | 2081 Mali de fusion sur actifs incorporels |
| **Total** | | **468 000** | |

Le solde affecté au fonds commercial (324 000 €) correspond à 60 % × 580 000 – 60 % × 40 000 : la quote-part des engagements de retraite non comptabilisés vient en diminution.

---

### 2.5 Écritures au 1er janvier 2027 chez HÉLIOS (5 pts)

Les écritures complètes (comptes, intitulés, montants) figurent dans `corrige.yaml` (R1 à R6). Toutes sont équilibrées (contrôle `ue4check`). Schémas types : `gabarits/ecritures_types/03_fusion_renonciation.yaml` et `04_mali_technique.yaml`.

**R1 — Augmentation de capital (1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 488 000 | |
| 101 Capital | | 100 000 |
| 1042 Primes de fusion | | 388 000 |

**R2 — Réalisation des apports à la valeur comptable (1,25 pt).** En valeur comptable, HÉLIOS reprend les **valeurs brutes et les amortissements** d'ORION [V BOI-IS-FUS-10-20-40-20 § 170-180, voir F01 § 3.2].

| Compte | Débit | Crédit |
|---|---:|---:|
| 211 Terrains | 300 000 | |
| 2131 Bâtiments | 900 000 | |
| 2154 Matériels industriels | 400 000 | |
| 37 Stocks de marchandises | 260 000 | |
| 411 Clients | 340 000 | |
| 512 Banques | 100 000 | |
| 28131 Amortissements des bâtiments | | 400 000 |
| 28154 Amortissements des matériels industriels | | 250 000 |
| 164 Emprunts auprès des établissements de crédit | | 230 000 |
| 401 Fournisseurs | | 200 000 |
| 4561 Associés – Comptes d'apport en société | | 1 220 000 |

**R3 et R4 — Vrai mali et annulation des titres ORION (1,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| *R3* 6866 Dotations pour dépréciation des éléments financiers | 60 000 | |
| 2961 Dépréciations des titres de participation | | 60 000 |
| *R4* 4561 Associés – Comptes d'apport en société | 732 000 | |
| 2961 Dépréciations des titres de participation | 60 000 | |
| 2187 Mali de fusion sur actifs corporels (terrain) | 72 000 | |
| 2187 Mali de fusion sur actifs corporels (constructions) | 72 000 | |
| 2081 Mali de fusion sur actifs incorporels (fonds commercial) | 324 000 | |
| 261 Titres de participation | | 1 260 000 |

Après R1, R2 et R4, le compte 4561 est soldé (488 000 + 732 000 = 1 220 000).

**R5 — Reconstitution des amortissements dérogatoires (0,75 pt).** Engagement pris au titre du régime de faveur (voir 2.7). L'imputation se fait sur la prime de fusion [V corrigé du sujet zéro, Q 2.6, pour une provision réglementée].

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion | 20 000 | |
| 145 Amortissements dérogatoires | | 20 000 |

**R6 — Extinction par confusion de la dette réciproque (0,5 pt).** HÉLIOS devient à la fois créancière (créance d'ORION reçue par l'apport) et débitrice de la même obligation : la confusion éteint la créance [V C. civ. art. 1349].

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs | 40 000 | |
| 411 Clients | | 40 000 |

---

### 2.6 Suivi du mali au 31/12/2027 (2,5 pts)

**Écriture R7 (1 pt).** Le mali technique suit les règles de l'actif sous-jacent [V PCG art. 745-7]. La quote-part affectée aux constructions s'amortit sur leur durée résiduelle : 72 000 / 20 = **3 600 €**.

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles | 3 600 | |
| 28187 Amortissement du mali de fusion sur actifs corporels | | 3 600 |

**Autres composantes (0,75 pt)**
- Mali affecté au **terrain** : non amorti, puisque le terrain ne s'amortit pas.
- Mali affecté au **fonds commercial** : non amorti, le fonds commercial étant présumé avoir une durée d'utilisation non limitée [V PCG art. 214-3]. Il serait déprécié si la valeur actuelle du fonds devenait inférieure à sa valeur comptable augmentée du mali [V PCG art. 745-8].
- **Vrai mali** : déjà constaté en charge financière au 01/01/2027 (R3). Aucun suivi.

**Traitement fiscal (0,75 pt).** Le mali technique ne peut donner lieu à aucune déduction ultérieure [V CGI art. 210 A-1]. La dotation de 3 600 € est **réintégrée extra-comptablement** au résultat fiscal 2027.

---

### 2.7 Conséquences du régime de faveur (2 pts)

**Amortissements dérogatoires (1 pt).** Sous le régime de faveur, l'absorbante doit reprendre à son passif les provisions constituées par l'absorbée dont l'imposition a été différée [V CGI art. 210 A-3-a ; BOI-IS-FUS-10-20-40-10 § 220]. HÉLIOS reconstitue donc les 20 000 € d'amortissements dérogatoires (R5). Elle les reprendra ensuite dans les mêmes conditions qu'ORION, au rythme de l'amortissement du matériel [V BOI-IS-FUS-30-20 § 10]. Sous le régime de droit commun, cette provision aurait été imposée immédiatement chez ORION, au titre de la cessation d'activité.

**Mali (1 pt).** Le mali technique n'est pas déductible, ni lors de sa constatation ni par la suite : ses amortissements et dépréciations sont réintégrés (voir 2.6) [V CGI art. 210 A-1].

---

### 2.8 Capitaux propres de HÉLIOS juste après l'opération (1,5 pt)

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital | 1 000 000 | + 100 000 | 1 100 000 |
| Primes de fusion | 0 | + 388 000 – 20 000 | 368 000 |
| Réserves | 2 700 000 | | 2 700 000 |
| Résultat de l'exercice 2027 (vrai mali) | 0 | – 60 000 | – 60 000 |
| Provisions réglementées (amortissements dérogatoires) | 0 | + 20 000 | 20 000 |
| **Total** | **3 700 000** | **+ 428 000** | **4 128 000** |

Contrôle : + 428 000 = apports rémunérés (488 000) – vrai mali (60 000).

**Commentaire pour la directrice financière (grille de niveaux)**

| Niveau | 0 | 0,5 | 1 | 1,5 |
|---|---|---|---|---|
| Attendu | Absence ou tableau faux | Tableau juste sans commentaire | Tableau et 1 ou 2 idées pertinentes | Tableau et analyse structurée |

Idées attendues :
- l'augmentation de capital est limitée (9,09 % du capital) et SOLARIS conserve le contrôle ;
- la fusion fait apparaître une perte financière de 60 000 € sur 2027, qui révèle que la participation avait été payée au-dessus de sa valeur actuelle ;
- le mali technique (468 000 €) figure désormais à l'actif. Il est pour l'essentiel non amortissable (terrain, fonds commercial), exposé à un risque de dépréciation, et non déductible fiscalement ;
- la structure financière est renforcée (+ 428 000 € de capitaux propres), ce qui intéresse les prêteurs et les fournisseurs.

---

### Réponses tolérées
- **Vrai mali** : enregistrement direct en une écriture (débit 6866, crédit 261) au lieu du passage par 2961. C'est une présentation abrégée admise [F01 § 9].
- **Amortissements dérogatoires** : un candidat qui les reprend directement dans l'écriture de réalisation (crédit 145) et retient un actif net apporté de 1 200 000 € obtient une prime de 380 000 € et un mali de 540 000 €. La logique est acceptée si elle est cohérente sur l'ensemble du dossier. La méthode du corrigé (actif net = capitaux propres d'ORION, puis reconstitution par la prime) est celle du sujet zéro et du rapport du jury 2025.
- **Boni ou mali en VC** : la décomposition et l'affectation restent exigées. Le mali technique apparaît « généralement pour les opérations à la valeur comptable » [V PCG art. 745-4].

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion mal calculée, souvent sur la totalité des apports au lieu de la seule part rémunérée.
- `JUR-R02` Mali calculé sans être analysé (pas de décomposition technique / vrai mali).
- `JUR-R03` Oubli de l'imputation des provisions réglementées sur la prime de fusion.
- `JUR-R04` Suivi du mali technique mal traité (amortissement du mali affecté au terrain ou au fonds commercial).
- Erreur propre à ce cas : appliquer la valeur réelle au motif que la fusion est « à l'endroit », sans voir que le contrôle commun impose la valeur comptable.

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
