# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 4

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F13 (`ue4/fiches/`, à jour au 22 ou 23/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.9 | `exercices/ex07_consolidation_ip_contrats` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.6 | `exercices/ex08_fusion_soulte_actions_propres` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.8 | `exercices/ex09_audit_moyens_nep_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Obligation de consolider | `2.1.b` Contexte réglementaire et légal de la consolidation | 3 |
| 1.2 Référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 1 |
| 1.3 Normalisateurs et cadre conceptuel | `2.1.a` Cadre conceptuel de l'IASB | 2,5 |
| 1.4 Processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 1,5 |
| 1.5 Périmètre et méthodes | `2.1.c` Périmètre ; `2.1.d` Conséquences des méthodes | 3 |
| 1.6 Chantier pluriannuel | `2.2.c` Homogénéisation, thèmes communs | 6 |
| 1.7 a Marge interne CLIMESTE | `2.2.f` Comptes réciproques et résultats internes | 3 |
| 1.7 b Comptes réciproques | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.7 c Marge interne VENTÉO | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.8 a Actifs nets réévalués | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.8 b Coût d'acquisition et écart d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 4 |
| 1.8 c Écarts d'évaluation et frais d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.8 d Tableau de partage | `2.2.h` Partage des capitaux propres | 4 |
| 1.8 e Écritures d'élimination | `2.2.h` Partage des capitaux propres | 2 |
| 1.9 Documents de synthèse | `2.3.a` Documents de synthèse consolidés | 5 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires ; `EA` = écart d'acquisition ; `AMO_EA` / `DOT_EA` = amortissements / dotation de l'écart d'acquisition ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat.

---

### 1.1 Obligation d'établir des comptes consolidés (3 pts)

**Principe (1 pt).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1] (0,5 pt). En l'espèce, DRAVENNE, SAS donc société commerciale, contrôle exclusivement CLIMESTE et, par elle, HYDRÉLIA, et conjointement VENTÉO (voir 1.5) : elle entre dans le champ de l'obligation (0,5 pt).

**Exemptions (2 pts).**
- *Société elle-même contrôlée* (L. 233-17, 1°) : l'exemption suppose que la société soit incluse dans les comptes consolidés d'une entité qui la contrôle. Le capital de DRAVENNE est détenu par la famille DRAVENNE, personnes physiques qui ne publient pas de comptes consolidés : cette exemption est écartée (0,5 pt) [V L. 233-17 ; F03 § 1.1].
- *Ensemble qui n'est pas un « grand groupe »* (L. 233-17, 2°) : est un grand groupe l'ensemble formé par la société et les entreprises qu'elle contrôle qui dépasse, à la clôture, deux des trois seuils suivants : total du bilan 30 000 000 €, chiffre d'affaires net 60 000 000 €, 250 salariés en moyenne ; les seuils sont réputés franchis à la clôture de **deux exercices consécutifs** [V L. 230-2, 3° ; D. 230-2, 2° et dernier alinéa ; F03 § 1.1] (0,5 pt).

| Clôture | Bilan > 30 M€ | CA > 60 M€ | Salariés > 250 | Seuils dépassés |
|---|---|---|---|---|
| 31/12/2024 | non (26,8 M€) | non (41,5 M€) | non (238) | 0 sur 3 |
| 31/12/2025 | oui (38,4 M€) | non (54,2 M€) | oui (265) | **2 sur 3** |
| 31/12/2026 | oui (71,5 M€) | oui (86 M€) | oui (420) | **3 sur 3** |

En l'espèce, deux seuils sont dépassés à la clôture de 2025 et les trois à celle de 2026 : les seuils sont franchis à deux clôtures consécutives, l'ensemble DRAVENNE est un grand groupe et l'exemption du 2° ne s'applique pas. En 2025, une seule clôture (2025) dépassait les seuils : l'obligation naît donc avec l'exercice 2026, premier exercice consolidé (0,5 pt).
- *Autres cas* : aucune entité de l'ensemble ne relève de l'art. L. 123-16-2 (établissements de crédit, assurances, sociétés cotées, appel à la générosité du public), ce qui ne joue de toute façon que pour refuser l'exemption du 2° ; les entités contrôlées ne présentent pas un intérêt négligeable (CLIMESTE et HYDRÉLIA représentent une part importante du chiffre d'affaires et de l'effectif de 2026) [V L. 233-17-1 ; L. 123-16-2 ; F03 § 1.1] (0,5 pt).

**Conclusion** : DRAVENNE doit établir et publier des comptes consolidés au 31/12/2026.

---

### 1.2 Référentiel (1 pt)

Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que pour les sociétés dont les titres sont admis aux négociations sur un marché réglementé d'un État membre [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Les autres sociétés établissent leurs comptes consolidés selon le règlement ANC n° 2020-01 ou, sur option, selon les IFRS adoptées [V C. com. L. 233-24 ; F03 § 1.2] (0,5 pt).

En l'espèce, aucun titre de DRAVENNE n'est admis sur un marché réglementé : le groupe applique le règlement ANC n° 2020-01, comme le prévoit son manuel, mais il pourrait opter pour les IFRS adoptées par l'Union européenne, ce que souhaite sa banque (0,5 pt).

---

### 1.3 IASB, IFRIC, EFRAG et cadre conceptuel (2,5 pts)

**Normalisateurs (1,5 pt, 0,5 pt par organisme)**
- **IASB** (International Accounting Standards Board) : organisme de normalisation indépendant, au sein de l'IFRS Foundation, fondation privée d'intérêt public. Il élabore et publie les normes IFRS et approuve les interprétations préparées par le comité d'interprétation [V page « International Accounting Standards Board », ifrs.org, consultée le 27/10/2026].
- **IFRIC** (comité d'interprétation des IFRS, aujourd'hui *IFRS Interpretations Committee*) : il travaille avec l'IASB à l'application cohérente des normes. Il répond aux questions d'application qui lui sont soumises, et ses interprétations (« IFRIC ») sont approuvées par l'IASB [V pages « IFRS Interpretations Committee » et « International Accounting Standards Board », ifrs.org, consultées le 27/10/2026]. Les interprétations adoptées figurent, avec les normes, dans le règlement européen d'adoption (par exemple IFRIC 23) [V règlement (UE) 2023/1803].
- **EFRAG** (European Financial Reporting Advisory Group) : il fait valoir les positions européennes dans les travaux de l'IASB et conseille la Commission européenne sur l'adoption de chaque norme nouvelle ou modifiée : la norme répond-elle aux critères du règlement IAS et sert-elle l'intérêt public européen ? [V page « Financial reporting », efrag.org, consultée le 27/10/2026]. La Commission adopte ensuite les normes par règlement : seules les normes ainsi adoptées s'appliquent dans l'Union [V intitulé du règlement (UE) 2023/1803 « portant adoption de certaines normes comptables internationales conformément au règlement (CE) n° 1606/2002 »].

**Cadre conceptuel (1 pt)**
- **Objectif** : l'information financière à usage général doit être utile aux investisseurs, prêteurs et autres créanciers, actuels et potentiels, pour leurs décisions de fournir des ressources à l'entité. Le cadre guide l'IASB dans l'élaboration de normes cohérentes ; il aide les entités à définir une méthode comptable lorsqu'aucune norme ne s'applique, et les utilisateurs à comprendre les normes [V page « Conceptual Framework for Financial Reporting », ifrs.org, cadre révisé de mars 2018 ; IAS 8 § 10-11] (0,5 pt). La banque, prêteur du groupe, fait partie des destinataires visés.
- **Grands principes** : caractéristiques qualitatives fondamentales, la pertinence et la représentation fidèle ; caractéristiques auxiliaires, la comparabilité, la vérifiabilité, la rapidité et la compréhensibilité [S présentation du cadre conceptuel de 2018, IFRS Foundation et IAS Plus] ; définitions des éléments (actif, passif, capitaux propres, produits, charges), critères de comptabilisation et de décomptabilisation, bases d'évaluation, présentation et informations à fournir [V page « Conceptual Framework », ifrs.org]. Les états financiers sont établis selon l'hypothèse de continuité d'exploitation et la comptabilité d'engagement [V IAS 1 § 25 et 27] (0,5 pt).

---

### 1.4 Processus de consolidation (1,5 pt)

La consolidation part des comptes individuels des entités, après retraitements et éliminations préalables [V ANC art. 222-1, p. 19] ; l'intégration globale comprend l'intégration des comptes après retraitements, le partage des capitaux propres et du résultat et l'élimination des opérations internes [V art. 221-2, p. 19].

| Étape | Contenu | Travaux du dossier |
|---|---|---|
| 1. Cadre et périmètre | Obligation, référentiel, entités consolidées, pourcentages, méthodes | 1.1, 1.2, 1.5 |
| 2. Comptes individuels retraités | Comptes arrêtés à la même date ; retraitements d'homogénéisation selon le manuel ; évaluation des actifs et passifs identifiables des entités acquises | 1.6, 1.8 a et c |
| 3. Cumul des comptes | 100 % pour CLIMESTE et HYDRÉLIA, 50 % pour VENTÉO | Réalisé par le service consolidation |
| 4. Élimination des opérations internes | Comptes réciproques, résultats internes, impôt différé | 1.7 |
| 5. Élimination des titres et partage | Écart d'acquisition, part du groupe et intérêts minoritaires | 1.8 b, d et e |
| 6. États de synthèse | Bilan, compte de résultat, annexe | 1.9 |

(1 pt pour l'enchaînement des étapes ; 0,5 pt pour leur rattachement aux questions.)

---

### 1.5 Périmètre et méthodes (3 pts)

**Tableau (1,5 pt, 0,5 pt par société)**

| Société | % de contrôle | Nature | Méthode | % d'intérêt |
|---|---|---|---|---|
| DRAVENNE | — | Mère | — | 100 % |
| CLIMESTE | 80 % | Exclusif | Intégration globale | 80 % (minoritaires 20 %) |
| HYDRÉLIA | 60 % (via CLIMESTE) | Exclusif | Intégration globale | 80 % × 60 % = **48 %** (minoritaires 52 %) |
| VENTÉO | 50 % | Conjoint | Intégration proportionnelle | 50 % |

**Justifications (1 pt)**
- Le pourcentage de contrôle additionne les droits de vote détenus par la mère et par les entités qu'elle contrôle exclusivement, sans multiplier [V ANC art. 211-6, p. 14]. CLIMESTE est contrôlée exclusivement : ses 60 % d'HYDRÉLIA comptent en totalité pour le contrôle, alors que l'intérêt du groupe n'est que de 48 %. Les minoritaires d'HYDRÉLIA (52 %) regroupent les fondateurs (40 %) et, indirectement, le minoritaire de CLIMESTE (20 % × 60 % = 12 %) (0,5 pt).
- VENTÉO est exploitée en commun par deux associés, en nombre limité ; le pacte impose leur accord unanime pour les dirigeants et les décisions essentielles : contrôle conjoint, d'où l'intégration proportionnelle [V art. 211-4, p. 13 ; art. 221-1, p. 18 ; F03 § 2 et 3] (0,5 pt).

**Conséquences de l'intégration proportionnelle (0,5 pt).** Le groupe n'intègre que 50 % de chaque élément d'actif, de passif, de produit et de charge de VENTÉO ; aucun intérêt minoritaire n'est constaté [V art. 221-3, p. 19 ; art. 261-1, p. 48]. Les opérations entre VENTÉO et les entités intégrées globalement ne sont éliminées qu'à hauteur de 50 % [V art. 261-3 et 261-4, p. 48]. Le chiffre d'affaires et l'endettement consolidés ne reprennent ainsi que la moitié de ceux de VENTÉO. En IFRS, VENTÉO, coentreprise, serait mise en équivalence : une seule ligne au bilan et au compte de résultat [V IFRS 11 § 24 ; F03 § 3].

---

### 1.6 Chantier pluriannuel d'HYDRÉLIA (6 pts)

**Justification (0,5 pt).** Le PCG permet de comptabiliser les contrats à long terme à l'achèvement ou à l'avancement [V PCG art. 622-2, p. 63 ; F04 R9]. HYDRÉLIA applique l'achèvement, alors que le manuel du groupe retient l'avancement : les comptes d'HYDRÉLIA sont retraités pour appliquer la méthode du groupe [V ANC art. 271-5, p. 52 ; F04 § 1]. Le résultat à terminaison est estimé de façon fiable : à l'avancement, le résultat est le résultat à terminaison multiplié par le pourcentage d'avancement [V PCG art. 622-3 et 622-5 ; F04 R9]. Le résultat fiscal suit l'achèvement : le retraitement crée une différence temporaire imposable, donc un **impôt différé passif** [V ANC art. 272-8, p. 57].

**Avancement et chiffre d'affaires à l'avancement (1,5 pt)**

| | 31/12/2025 | 31/12/2026 |
|---|---:|---:|
| Pourcentage d'avancement | 420 000 / 2 100 000 = **20 %** (0,5) | 1 800 000 / 2 250 000 = **80 %** (0,5) |
| Chiffre d'affaires cumulé à l'avancement | 2 500 000 × 20 % = 500 000 | 2 500 000 × 80 % = **2 000 000** (0,5) |
| Coûts engagés cumulés | 420 000 | 1 800 000 |
| Marge cumulée à l'avancement | **80 000** | **200 000** |

Contrôle : 20 % × (2 500 000 – 2 100 000) = 80 000 ; 80 % × (2 500 000 – 2 250 000) = 200 000.

**Tableau des incidences (2 pts)**

| Postes | Ouverture (31/12/2025) | Variation 2026 | Clôture (31/12/2026) |
|---|---:|---:|---:|
| Chiffre d'affaires / créance (comptes consolidés) | 500 000 | 1 500 000 | 2 000 000 |
| Chiffre d'affaires / créance (comptes individuels) | 0 | 0 | 0 |
| Écart (a) | 500 000 | 1 500 000 | 2 000 000 |
| Travaux en cours (comptes consolidés) | 0 | 0 | 0 |
| Travaux en cours (comptes individuels) | 420 000 | 1 380 000 | 1 800 000 |
| Écart (b) | – 420 000 | – 1 380 000 | – 1 800 000 |
| **Écart total (a) + (b)** | **80 000** | **120 000** | **200 000** |
| Impôt différé passif (25 %) | – 20 000 | – 30 000 | **– 50 000** |
| **Net** | **60 000** (réserves) | **90 000** (résultat) | 150 000 |

(Ouverture et net en réserves : 0,5 pt ; variation, impôt et net en résultat : 0,75 pt ; clôture et impôt différé passif : 0,75 pt.)

Les situations facturées (1 900 000 € cumulés) restent sans incidence sur le résultat : elles figurent au compte 4191 dans les comptes individuels. À l'avancement, le chiffre d'affaires cumulé (2 000 000) les excède de 100 000 € : ce solde est une facture à établir.

**C1 (bilan, 1 pt)** — schéma type `gabarits/ecritures_types/11_contrat_long_terme.yaml`

| Compte | Débit | Crédit |
|---|---:|---:|
| 4191 Clients – Avances et acomptes reçus sur commandes | 1 900 000 | |
| 4181 Clients – Factures à établir | 100 000 | |
| 335 Travaux en cours | | 1 800 000 |
| IDP Impôt différé passif | | 50 000 |
| RSV.HYDRELIA Réserves HYDRÉLIA | | 60 000 |
| RST.HYDRELIA Résultat HYDRÉLIA | | 90 000 |
| *Chantier HYDRÉLIA : passage à l'avancement* | **2 000 000** | **2 000 000** |

**C2 (compte de résultat, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 7133 Variation des en-cours de production de biens | 1 380 000 | |
| CH_ID Charge d'impôt différé | 30 000 | |
| RES_CR Résultat | 90 000 | |
| 704 Travaux | | 1 500 000 |
| *Chantier HYDRÉLIA : passage à l'avancement* | **1 500 000** | **1 500 000** |

Le retraitement des exercices antérieurs (60 000 € nets) date d'avant l'entrée d'HYDRÉLIA dans le groupe : il augmente l'actif net acquis le 01/01/2026 (question 1.8 a).

---

### 1.7 Opérations internes (7 pts)

#### a. Marge réalisée par CLIMESTE sur les ventes à HYDRÉLIA (3 pts)

**Justification (0,5 pt).** Les profits internes inclus dans les stocks sont éliminés en totalité, entre deux entités intégrées globalement, et répartis entre le groupe et les minoritaires de l'entité qui les a réalisés, ici CLIMESTE, vendeuse ; l'impôt est corrigé [V ANC art. 251-2, p. 45 ; F04 R14].

**Calcul (1,5 pt)**

| | Montant |
|---|---:|
| Stock d'HYDRÉLIA acheté à CLIMESTE | 140 000 |
| Marge : 140 000 × 25 / 125 (marge de 25 % du coût) | **28 000** (1) |
| Impôt différé actif (25 %) | 7 000 |
| **Incidence nette sur le résultat de CLIMESTE** | **– 21 000** (0,5) |

Aucun stock d'origine interne n'existait au 01/01/2026 : l'incidence porte en totalité sur le résultat 2026. Elle sera partagée à 80 % / 20 % avec le résultat de CLIMESTE (1.8 d).

**C3 (bilan, 0,5 pt)** : débit RST.CLIMESTE 21 000 ; débit IDA 7 000 ; crédit 31 Matières premières et fournitures 28 000.
**C4 (compte de résultat, 0,5 pt)** : débit 6031 Variation des stocks de matières premières et fournitures 28 000 ; crédit CH_ID 7 000 ; crédit RES_CR 21 000.

Schéma type : `gabarits/ecritures_types/09_marge_interne_stocks.yaml`.

#### b. Comptes réciproques (2 pts)

**Principe (0,5 pt).** Les créances et dettes, produits et charges réciproques sont éliminés en totalité entre entités intégrées globalement [V ANC art. 251-1, p. 45] ; avec une entité intégrée proportionnellement, l'élimination est limitée au pourcentage d'intégration, et la différence est traitée comme une créance ou une dette envers les entités extérieures au groupe [V art. 261-3, p. 48]. Ces éliminations n'ont pas d'incidence sur le résultat.

**CLIMESTE / HYDRÉLIA (0,75 pt)**
- C5 (bilan) : débit 401 Fournisseurs 84 000 ; crédit 411 Clients 84 000.
- C6 (compte de résultat) : débit 707 Ventes de marchandises 600 000 ; crédit 601 Achats stockés – Matières premières et fournitures 600 000.

**VENTÉO / CLIMESTE, à 50 % (0,75 pt)**
- C7 (bilan) : débit 401 Fournisseurs 18 000 (36 000 × 50 %) ; crédit 411 Clients 18 000 (créance de VENTÉO, intégrée pour 50 %).
- C8 (compte de résultat) : débit 707 Ventes de marchandises 120 000 (240 000 × 50 %) ; crédit 607 Achats de marchandises 120 000.

Il subsiste dans les comptes consolidés une dette fournisseur de 18 000 € et des achats de 120 000 €, qui correspondent à la part d'AÉROVIA dans VENTÉO, extérieure au groupe.

#### c. Marge réalisée par VENTÉO sur les ventes à CLIMESTE (2 pts)

**Principe (0,5 pt).** Pour une cession entre une entité intégrée proportionnellement et une entité intégrée globalement, l'élimination du résultat interne est limitée au pourcentage d'intégration de l'entité sous contrôle conjoint [V art. 261-4, p. 48]. VENTÉO, vendeuse, n'a pas de minoritaires dans les comptes consolidés : l'incidence revient au groupe seul.

**Calcul (0,75 pt)**

| | Montant |
|---|---:|
| Stock de CLIMESTE acheté à VENTÉO | 60 000 |
| Marge : 60 000 × 30 % (taux de marque) | 18 000 |
| **Marge éliminée (50 %)** | **9 000** |
| Impôt différé actif (25 %) | 2 250 |
| **Incidence nette sur le résultat (VENTÉO, part du groupe)** | **– 6 750** |

**C9 (bilan, 0,5 pt)** : débit RST.VENTEO 6 750 ; débit IDA 2 250 ; crédit 37 Stocks de marchandises 9 000.
**C10 (compte de résultat, 0,25 pt)** : débit 6037 Variation des stocks de marchandises 9 000 ; crédit CH_ID 2 250 ; crédit RES_CR 6 750.

---

### 1.8 Écarts de première consolidation et partage (16 pts)

#### a. Actifs nets réévalués au 01/01/2026 (3 pts)

La valeur d'entrée des actifs et passifs identifiables est comparée à leur valeur comptable dans le bilan retraité aux normes du groupe ; les écarts d'évaluation donnent lieu à impôt différé, dont la contrepartie ajuste l'écart d'acquisition [V ANC art. 231-9, p. 22 ; art. 232-1, p. 24 ; art. 272-13, p. 58-59 ; F05 § 1.2]. HYDRÉLIA entre dans le périmètre le même jour que CLIMESTE, sa mère : la date d'entrée est celle de la prise de contrôle par le groupe [V art. 211-10, p. 16].

**CLIMESTE (1 pt)**

| Élément | Montant |
|---|---:|
| Capitaux propres individuels au 01/01/2026 | 7 000 000 |
| Écart d'évaluation sur terrain (700 000 – 400 000) | + 300 000 |
| Écart d'évaluation sur bâtiment (1 700 000 – 1 100 000) | + 600 000 |
| Impôt différé passif (900 000 × 25 %) | – 225 000 |
| **Actif net réévalué de CLIMESTE** | **7 675 000** |

**HYDRÉLIA (1 pt)**

| Élément | Montant |
|---|---:|
| Capitaux propres individuels au 01/01/2026 | 3 190 000 |
| Retraitement du chantier à l'avancement, net d'impôt (1.6, ouverture) | + 60 000 |
| **Actif net réévalué d'HYDRÉLIA** | **3 250 000** |

**Sous-groupe revenant à DRAVENNE (1 pt).** Dans l'actif net de CLIMESTE, les titres HYDRÉLIA (600 000) sont remplacés par la quote-part de CLIMESTE dans l'actif net d'HYDRÉLIA :

| | Montant |
|---|---:|
| Actif net réévalué de CLIMESTE | 7 675 000 |
| – Titres HYDRÉLIA | – 600 000 |
| + 60 % × actif net réévalué d'HYDRÉLIA (60 % × 3 250 000) | + 1 950 000 |
| **Actif net réévalué du sous-groupe** | **9 025 000** |
| **Quote-part de DRAVENNE (80 %)** | **7 220 000** |

#### b. Coût d'acquisition et écart d'acquisition (4 pts)

**Coût d'acquisition (1,5 pt).** Prix remis au vendeur, augmenté des coûts directement imputables nets de l'économie d'impôt [V ANC art. 231-2, p. 20 ; F05 § 1.1] : 8 000 000 + 120 000 × (1 – 25 %) = **8 090 000 €**.

**Écart d'acquisition (1,5 pt).** Coût d'acquisition – part de l'acquéreur dans les actifs et passifs identifiables [V art. 231-9, p. 22] : 8 090 000 – 7 220 000 = **870 000 €**. Positif, il est inscrit en immobilisations incorporelles [V art. 231-11, p. 23]. Aucun impôt différé n'est calculé sur l'écart d'acquisition [V art. 272-10, p. 58].

Décomposition, utile pour les écritures de partage (1.8 e) :
- sur CLIMESTE : 8 090 000 – 80 % × 7 675 000 = 1 950 000 ;
- sur HYDRÉLIA : 80 % × 600 000 – 48 % × 3 250 000 = 480 000 – 1 560 000 = – 1 080 000 ;
- total : 1 950 000 – 1 080 000 = 870 000.

La quote-part du groupe dans les réserves d'HYDRÉLIA accumulées avant le 01/01/2026 (1 080 000 €) a été payée avec les titres CLIMESTE : elle réduit l'écart d'acquisition et ne constitue pas des réserves consolidées.

**Amortissement 2026 (1 pt).** Le manuel retient une durée d'utilisation limitée de 10 ans : amortissement linéaire [V art. 231-11, p. 23 ; F05 § 1.3] de 870 000 / 10 = **87 000 €**. La dotation, à la charge du seul groupe, figure sur la ligne propre aux écarts d'acquisition, au sein du résultat d'exploitation consolidé [V IR3 sous art. 231-12 ; modèle art. 281-2, p. 67].

#### c. Écritures relatives aux écarts d'évaluation et aux frais d'acquisition (3 pts)

**Écarts d'évaluation au 31/12/2026 (2 pts).** Antérieurs à 2026, ils sont repris en réserves ; l'amortissement du supplément de valeur du bâtiment pour 2026 pèse sur le résultat (tableau : 0,5 pt).

| | Réserves (01/01/2026) | Résultat 2026 | Bilan au 31/12/2026 |
|---|---:|---:|---:|
| Terrain | + 300 000 | — | 211 : + 300 000 |
| Bâtiment | + 600 000 | – 30 000 (600 000 / 20) | 213 : + 600 000 ; 2813 : – 30 000 |
| Impôt différé (25 %) | – 225 000 | + 7 500 | IDP : 217 500 |
| **Net** | **+ 675 000** | **– 22 500** | |

**C11 (bilan, 1 pt)** : débit 211 Terrains 300 000 ; débit 213 Constructions 600 000 ; débit RST.CLIMESTE 22 500 ; crédit 2813 Amortissements des constructions 30 000 ; crédit IDP 217 500 ; crédit RSV.CLIMESTE 675 000.
**C12 (compte de résultat, 0,5 pt)** : débit 6811 Dotations aux amortissements 30 000 ; crédit CH_ID 7 500 ; crédit RES_CR 22 500.

**Frais d'acquisition (1 pt).** DRAVENNE a passé les 120 000 € en charges en 2026 et en a tiré une économie d'impôt de 30 000 €. En consolidation, ces frais sont incorporés, nets d'impôt, au coût des titres [V art. 231-2, p. 20 ; F05 § 1.1] : les titres augmentent de 90 000 €, ainsi que le résultat de DRAVENNE.
**C13 (bilan, 0,5 pt)** : débit 261.DRAVENNE Titres de participation CLIMESTE 90 000 ; crédit RST.DRAVENNE 90 000.
**C13R (compte de résultat, 0,5 pt)** : crédit 6226 Honoraires 120 000 ; débit 695 Impôts sur les bénéfices 30 000 ; débit RES_CR 90 000.

#### d. Tableau de partage au 31/12/2026 (4 pts)

**Capitaux propres retraités (1,5 pt)**

| | CLIMESTE | HYDRÉLIA | VENTÉO (intégré à 50 %) |
|---|---:|---:|---:|
| Capital | 2 000 000 | 1 000 000 | 200 000 |
| Réserves individuelles | 5 000 000 | 2 190 000 | 300 000 |
| + Écarts d'évaluation nets (C11) | + 675 000 | | |
| + Chantier, part antérieure (C1) | | + 60 000 | |
| **Capital et réserves retraités** | **7 675 000** | **3 250 000** | **500 000** |
| Résultat individuel 2026 | 1 100 000 | 500 000 | 120 000 |
| Amortissement de l'écart d'évaluation (C11) | – 22 500 | | |
| Marge interne en stock (C3, C9) | – 21 000 | | – 6 750 (marge éliminée à 50 %, nette d'impôt) |
| Chantier, part 2026 (C1) | | + 90 000 | |
| **Résultat retraité** | **1 056 500** | **590 000** | **113 250** |

Aucun dividende n'ayant été distribué en 2026, le capital et les réserves retraités de CLIMESTE et d'HYDRÉLIA au 31/12/2026 égalent leurs actifs nets réévalués du 01/01/2026.

**Partage (2,5 pts : CLIMESTE 1 pt ; HYDRÉLIA 1 pt ; VENTÉO 0,5 pt)**

| | Groupe | Minoritaires |
|---|---:|---:|
| **CLIMESTE** (groupe 80 %, minoritaires 20 %) | | |
| Capital et réserves retraités (7 675 000) | 6 140 000 | 1 535 000 |
| – Titres CLIMESTE (8 090 000) | – 8 090 000 | |
| + Écart d'acquisition constaté sur CLIMESTE | + 1 950 000 | |
| **Réserves** | **0** | **1 535 000** |
| **Résultat** (1 056 500) | **845 200** | **211 300** |
| **HYDRÉLIA** (groupe 48 %, minoritaires 52 %) | | |
| Capital et réserves retraités (3 250 000) | 1 560 000 | 1 690 000 |
| – Titres HYDRÉLIA détenus par CLIMESTE (600 000 : 80 % / 20 %) | – 480 000 | – 120 000 |
| – Écart d'acquisition constaté sur HYDRÉLIA | – 1 080 000 | |
| **Réserves** | **0** | **1 570 000** |
| **Résultat** (590 000) | **283 200** | **306 800** |
| **VENTÉO** (intégration proportionnelle, 50 %) | | |
| Capital et réserves intégrés (50 % × 1 000 000) | 500 000 | — |
| – Titres VENTÉO | – 200 000 | — |
| **Réserves** | **300 000** | — |
| **Résultat** (50 % × 240 000 – 6 750) | **113 250** | — |

Contrôles :
- réserves consolidées de CLIMESTE et d'HYDRÉLIA nulles, l'acquisition datant du 01/01/2026 ; les réserves de VENTÉO (300 000) proviennent de résultats réalisés depuis sa création par le groupe ;
- intérêts minoritaires en réserves : 20 % × 9 025 000 (actif net réévalué du sous-groupe) + 40 % × 3 250 000 = 1 805 000 + 1 300 000 = 3 105 000 = 1 535 000 + 1 570 000 ; les minoritaires sont évalués sur l'actif net réévalué, sans écart d'acquisition [V art. 232-1, p. 24 ; F05 § 1.3].

#### e. Écritures d'élimination et de partage (2 pts)

**C14 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.CLIMESTE Capital CLIMESTE | 2 000 000 | |
| RSV.CLIMESTE Réserves CLIMESTE retraitées | 5 675 000 | |
| RST.CLIMESTE Résultat CLIMESTE retraité | 1 056 500 | |
| EA Écart d'acquisition | 1 950 000 | |
| 261.DRAVENNE Titres CLIMESTE | | 8 090 000 |
| RST_G Résultat consolidé – part du groupe | | 845 200 |
| RSV_M Intérêts minoritaires – capital et réserves | | 1 535 000 |
| RST_M Intérêts minoritaires – résultat | | 211 300 |
| **Total** | **10 681 500** | **10 681 500** |

**C15 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.HYDRELIA Capital HYDRÉLIA | 1 000 000 | |
| RSV.HYDRELIA Réserves HYDRÉLIA retraitées | 2 250 000 | |
| RST.HYDRELIA Résultat HYDRÉLIA retraité | 590 000 | |
| 261.CLIMESTE Titres HYDRÉLIA | | 600 000 |
| EA Écart d'acquisition | | 1 080 000 |
| RST_G Résultat consolidé – part du groupe | | 283 200 |
| RSV_M Intérêts minoritaires – capital et réserves | | 1 570 000 |
| RST_M Intérêts minoritaires – résultat | | 306 800 |
| **Total** | **3 840 000** | **3 840 000** |

**C16 (bilan, 0,5 pt)** : débit CAP_ELIM.VENTEO 200 000 (50 % du capital) ; débit RSV.VENTEO 300 000 ; débit RST.VENTEO 113 250 ; crédit 261.DRAVENNE Titres VENTÉO 200 000 ; crédit RSV_G 300 000 ; crédit RST_G 113 250. Aucun intérêt minoritaire [V art. 261-1, p. 48].

**C17 (bilan, 0,25 pt)** : débit RST_G 87 000 ; crédit AMO_EA Amortissements de l'écart d'acquisition 87 000.
**C17R (compte de résultat, 0,25 pt)** : débit DOT_EA Dotation aux amortissements des écarts d'acquisition 87 000 ; crédit RES_CR 87 000.

---

### 1.9 Documents de synthèse (5 pts)

**Bilan consolidé ANC, extrait au 31/12/2026 (1,5 pt)** — modèle de l'art. 281-1 [V p. 66]

| Rubrique | Calcul | Montant |
|---|---|---:|
| **Capitaux propres (part du groupe)** | | |
| Capital (de l'entité mère) | | 5 000 000 |
| Réserves et résultat consolidés | 12 400 000 + 300 000 + 2 854 650 | 15 554 650 |
| dont résultat net de l'exercice | 1 610 000 + 90 000 + 845 200 + 283 200 + 113 250 – 87 000 | 2 854 650 |
| **Total capitaux propres (part du groupe)** | | **20 554 650** |
| **Intérêts minoritaires** (rubrique distincte, après les capitaux propres part du groupe) | 3 105 000 + 211 300 + 306 800 | **3 623 100** |
| Immobilisations incorporelles, dont écart d'acquisition positif | 870 000 – 87 000 | 783 000 |
| Autres créances et comptes de régularisation, dont impôts différés actifs | 7 000 + 2 250 | 9 250 |
| Autres dettes et comptes de régularisation, dont impôts différés passifs | 50 000 + 217 500 | 267 500 |

(Capitaux propres part du groupe : 0,75 pt ; intérêts minoritaires : 0,25 pt ; écart d'acquisition et impôts différés : 0,5 pt.)

**Compte de résultat consolidé ANC, lignes propres à la consolidation (1 pt)** — modèle de l'art. 281-2 [V p. 67]
- Résultat d'exploitation avant dotations aux amortissements, dépréciations et reprises des écarts d'acquisition ;
- Dotations aux amortissements et dépréciations des écarts d'acquisition positifs : **87 000** ;
- Résultat d'exploitation après ces dotations et reprises ;
- Impôts sur les résultats (impôt exigible et impôts différés, dont les charges et produits d'impôt différé des retraitements) ;
- Résultat net des entités intégrées ; résultat net lié aux entités mises en équivalence (néant) ;
- **Résultat net de l'ensemble consolidé : 3 372 750** ; **intérêts minoritaires : 518 100** (211 300 + 306 800) ; **résultat net (part du groupe) : 2 854 650**.

**Différences de présentation en IFRS (IAS 1, exercice 2026) (2,5 pts)**
- **Jeu d'états financiers** : état de la situation financière, état du résultat net et des autres éléments du résultat global, état des variations des capitaux propres, état des flux de trésorerie et notes, présentés avec la même importance [V IAS 1 § 10 et 11] (0,5 pt).
- **État de la situation financière** : les participations ne donnant pas le contrôle (intérêts minoritaires) sont présentées **au sein des capitaux propres**, à côté du capital et des réserves attribuables aux propriétaires de la mère [V IAS 1 § 54 q) et r) ; IFRS 10 § 22], alors que le modèle ANC les isole entre les capitaux propres part du groupe et les autres fonds propres. Les actifs et passifs d'impôt différé forment des postes distincts, jamais classés en courant [V IAS 1 § 54 o) et 56], au lieu d'être compris dans les autres créances et dettes. L'écart d'acquisition n'est pas amorti en IFRS : la dotation de 87 000 € disparaîtrait [V F05 § 2 et § 5]. VENTÉO, coentreprise mise en équivalence, figurerait sur la ligne des participations mises en équivalence [V IAS 1 § 54 e) ; IFRS 11 § 24] (1 pt).
- **État du résultat net et des autres éléments du résultat global** : résultat net, autres éléments du résultat global et résultat global de la période, chacun réparti entre les participations ne donnant pas le contrôle et les propriétaires de la mère [V IAS 1 § 81A et 81B] ; quote-part de résultat des entités mises en équivalence sur une ligne [V IAS 1 § 82 c)] ; aucun élément présenté comme extraordinaire [V IAS 1 § 87], alors que le modèle ANC conserve une ligne de charges et produits exceptionnels ; aucune ligne propre à l'amortissement de l'écart d'acquisition [V F05 § 5] (0,5 pt).
- **Tableau des variations des capitaux propres** : état obligatoire, qui rapproche, pour chaque composante, l'ouverture et la clôture en distinguant le résultat net, les autres éléments du résultat global et les transactions avec les propriétaires, et qui sépare la part des propriétaires de la mère de celle des participations ne donnant pas le contrôle [V IAS 1 § 106]. En ANC, l'analyse de la variation des capitaux propres consolidés (part du groupe) est donnée en annexe [V renvoi (3) du modèle de l'art. 281-1] (0,5 pt).

Les montants de 1.9 dépendent des réponses antérieures : ils sont notés en cohérence avec les résultats du candidat.

---

### Réponses tolérées
- **1.1** : seuils appréciés sur les seules années 2025 et 2026, sans mention de 2024, si la règle des deux clôtures consécutives est énoncée.
- **1.6** : facture à établir de 2 000 000 € au débit de 4181, le compte 4191 étant maintenu (présentation du corrigé du sujet zéro) ; écritures de bilan et de compte de résultat regroupées si les réserves et le résultat sont distingués.
- **1.7 a** : stock d'HYDRÉLIA crédité au compte 32 ou 37, compte de variation correspondant.
- **1.8 b et e** : écart d'acquisition de 870 000 € comptabilisé en une seule fois dans l'écriture de CLIMESTE, avec réserves groupe de – 1 080 000 € pour CLIMESTE et de + 1 080 000 € pour HYDRÉLIA, si le total des réserves consolidées du sous-groupe est nul.
- **1.8 c** : frais d'acquisition incorporés par une écriture de bilan seule (C13), ou économie d'impôt annulée par une ligne « impôt sur les résultats » au lieu du compte 695.
- **1.9** : réserves consolidées (12 700 000) et résultat (2 854 650) présentés sur deux lignes.
- **1.9** : montants cohérents avec les erreurs antérieures du candidat (le jury valorise la logique du candidat, `JUR-F08`).

### Erreurs fréquentes
- **Obligation de consolider** : anciens seuils d'exemption des « petits groupes », abrogés par le décret du 30/12/2023, ou un seul exercice examiné (F99) ; exemption du 1° invoquée alors que DRAVENNE n'est contrôlée par aucune société.
- **Contrôle et intérêt confondus** : HYDRÉLIA à 48 % de contrôle, ce qui conduirait à tort à une mise en équivalence ; minoritaires d'HYDRÉLIA limités à 40 %.
- **Intégration proportionnelle** : intérêts minoritaires constatés sur VENTÉO, ou opérations avec VENTÉO éliminées à 100 %.
- **Chantier** : retraitement porté en totalité en résultat 2026, ou impôt différé oublié (`JUR-G04`, `JUR-G06`) ; tableau « comptes individuels / comptes consolidés » non présenté (`JUR-F05`).
- **Marge interne** : marge de 25 % appliquée au prix de vente (35 000 au lieu de 28 000) ; marge imputée à HYDRÉLIA, acheteuse, au lieu de CLIMESTE.
- **Coût d'acquisition** : frais d'acquisition omis ou retenus pour leur montant brut (`JUR-G02`).
- **Écart d'acquisition** : réserves d'HYDRÉLIA antérieures au 01/01/2026 traitées comme des réserves consolidées (écart d'acquisition de 1 950 000 € et réserves groupe de 1 080 000 €) ; impôt différé passif oublié sur les écarts d'évaluation ; supplément d'amortissement du bâtiment oublié.
- **Partage** : titres HYDRÉLIA éliminés en totalité sur la part du groupe au lieu d'être répartis 80 % / 20 % ; méthodologie de passage aux comptes consolidés mal maîtrisée (`JUR-G01`, `JUR-G04`) ; écritures non équilibrées (`JUR-F04`).
- **Présentation** : intérêts minoritaires inclus dans les capitaux propres part du groupe en ANC, ou écart d'acquisition amorti dans une présentation IFRS.

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, mode d'évaluation, régime fiscal | `1.1.a` Définir les opérations de restructuration ; `1.1.b` Régime de droit commun et régime de faveur ; `1.2.c` Déterminer le mode de valorisation des apports | 4 |
| 2.2 Valeur réelle et composition des apports | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 5 |
| 2.3 Parité, soulte et plafond légal | `1.2.a` Parité d'échange et nombre d'actions à créer ; `1.2.b` Soulte simple et légalité | 6 |
| 2.4 Écritures de fusion et actions propres | `1.3.a` Écritures de base chez l'absorbante ; `1.3.b` Écritures adaptées aux détentions préalables | 6 |
| 2.5 Écritures complémentaires | `1.3.c` Écritures complémentaires (régime fiscal, frais de fusion) | 2 |
| 2.6 Capitaux propres et commentaire | `1.4.a` Restituer au dirigeant les impacts de l'opération | 2 |
| **Total** | | **25** |

---

### 2.1 Qualification, mode d'évaluation des apports, régime fiscal (4 pts)

**Qualification et référentiel (1 pt).** L'opération est une **fusion-absorption** : FAÇALINE transmet l'ensemble de son patrimoine (actifs et passifs) à ISOLVÈRE ; elle est dissoute sans liquidation ; ses associés reçoivent des actions ISOLVÈRE émises par augmentation de capital, complétées d'une soulte en numéraire [V PCG art. 710-2, renvoi à C. com. L. 236-1, voir F01 § 1]. Il s'agit d'une restructuration, non d'une acquisition de titres : ISOLVÈRE ne paie pas un prix aux associés de FAÇALINE, elle reçoit un patrimoine et les rémunère par ses propres titres. L'enregistrement chez ISOLVÈRE relève du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié, comptes individuels), qui fixe les valeurs d'inscription des apports [V art. 710-1 et 720-1, F01 § 1]. Ces règles ne régissent pas le calcul de la parité, qui se fait sur les valeurs d'échange [V art. 740-1, F01 § 1].

**Situation de contrôle (0,75 pt).** ISOLVÈRE est contrôlée de manière exclusive par MAZERAT PARTICIPATIONS (70 % des droits de vote), FAÇALINE par BRANDÉLIA CAPITAL (80 %). ISOLVÈRE ne détient aucune action FAÇALINE ; les 5 % d'ISOLVÈRE détenus par FAÇALINE ne lui en donnent pas le contrôle. Aucune des deux sociétés ne contrôle l'autre et elles n'ont pas de mère commune : l'opération est réalisée **sous contrôle distinct** [V PCG art. 741-1 et 741-2, F01 § 2.1].

**Sens de l'opération (0,75 pt).** Après l'opération (voir 2.3 d), MAZERAT PARTICIPATIONS détient 51,4 % du capital et des droits de vote d'ISOLVÈRE : l'actionnaire principal de l'absorbante, bien que dilué, **conserve le contrôle**. BRANDÉLIA CAPITAL perd le contrôle de FAÇALINE et devient actionnaire minoritaire d'ISOLVÈRE (24,2 %). La fusion est **à l'endroit** ; ISOLVÈRE est l'initiatrice, FAÇALINE la cible [V art. 742-1, F01 § 2.2]. La conclusion vaut pour les trois parités envisagées (51,1 % à 51,9 %).

**Mode d'évaluation (0,5 pt).** Contrôle distinct et opération à l'endroit : les apports sont évalués à la **valeur réelle** (prise de contrôle traitée comme une acquisition) [V art. 743-1, cas 4, F01 § 2.3].

**Régime fiscal de faveur (1 pt)**
- *Conditions (0,5 pt).* L'opération ne fait intervenir que des sociétés passibles de l'impôt sur les sociétés (une SA et une SAS) [V CGI art. 210 C-1, F02 § 1]. Pour une fusion, le régime s'applique sauf option pour le droit commun [V BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1], à condition que l'absorbante prenne dans le traité les engagements de l'art. 210 A-3 : reprendre les provisions dont l'imposition est différée, se substituer à l'absorbée pour la réintégration des résultats différés, calculer les plus-values futures sur les immobilisations non amortissables d'après leur valeur fiscale chez l'absorbée, réintégrer les plus-values sur les biens amortissables, inscrire les stocks à leur valeur fiscale ou imposer le profit correspondant [V 210 A-3, a à e, F02 § 4].
- *Effets (0,5 pt).* Chez FAÇALINE, les plus-values dégagées sur les éléments apportés ne sont pas imposées [V 210 A-1] et la provision pour litiges, toujours justifiée, n'est pas reprise [V 210 A-2]. La fusion prenant effet au 1er janvier 2027, il n'y a pas de résultat intercalaire. Chez ISOLVÈRE : sursis d'imposition de la plus-value sur le terrain, dont la valeur fiscale chez FAÇALINE est conservée ; réintégration de la plus-value sur les constructions par parts égales sur 15 ans et de celle sur le matériel sur 5 ans, les amortissements futurs étant calculés sur la valeur d'apport ; imposition du profit sur les stocks (60 000 €), inscrits à leur valeur réelle et non à leur valeur fiscale, dans le résultat de l'exercice 2027 ; reprise des amortissements dérogatoires reconstitués dans les mêmes conditions que chez FAÇALINE [V 210 A-3-c, d, e ; BOI-IS-FUS-30-20 § 10, F02 § 2]. La plus-value sur les constructions représente 82,8 % de la plus-value nette sur biens amortissables (480 000 / 580 000), en deçà du seuil de 90 % : la durée de 15 ans s'applique. Comptablement, ces impositions futures justifient l'**impôt différé** intégré aux apports (voir 2.2).

---

### 2.2 Valeur réelle et composition des apports (5 pts)

**Neutralisation de l'actif fictif (0,5 pt).** Les frais d'établissement (60 000 € nets) n'ont aucune valeur réelle : ils ne sont pas repris dans les apports. Ils restent déductibles fiscalement chez ISOLVÈRE : leur disparition crée une différence déductible, donc un impôt différé actif [V corrigé du sujet zéro, Q 2.4, F01 § 3.3].

**Éléments identifiés figurant au bilan de FAÇALINE (1 pt)**

| Élément | Valeur nette comptable | Valeur réelle | Écart |
|---|---:|---:|---:|
| Frais d'établissement | 60 000 | 0 | – 60 000 |
| Terrain | 600 000 | 900 000 | + 300 000 |
| Constructions | 1 800 000 | 2 280 000 | + 480 000 |
| Matériel industriel | 800 000 | 900 000 | + 100 000 |
| Actions ISOLVÈRE (10 000 × 75) | 450 000 | 750 000 | + 300 000 |
| Stocks de matières premières | 900 000 | 960 000 | + 60 000 |
| Clients | 2 100 000 | 2 100 000 | 0 |
| Disponibilités | 410 000 | 410 000 | 0 |
| **Actifs identifiés** | **7 120 000** | **8 300 000** | |

La valeur unitaire d'échange d'ISOLVÈRE est de 15 000 000 / 200 000 = 75 € (voir 2.3) : les actions ISOLVÈRE détenues par FAÇALINE valent 750 000 €, montant compris dans la valeur d'échange de FAÇALINE.

**Éléments identifiés ne figurant pas au bilan (0,5 pt).** En valeur réelle, les apports comprennent les éléments identifiés, figurant ou non au bilan de l'absorbée, dont les provisions pour retraites et les impôts différés [V art. 744-1, F01 § 3.1] : engagements de retraite de **120 000 €** et impôt différé net (ci-dessous).

**Impôt différé intégré aux apports (1,5 pt).** Le régime de faveur reporte chez ISOLVÈRE l'imposition des plus-values sur biens amortissables et sur stocks et des amortissements dérogatoires reconstitués. L'écart entre valeur d'apport et valeur fiscale est une différence temporaire [V corrigé du sujet zéro, Q 2.4, F01 § 3.3 ; F02 § 6].

| Élément | Base | Impôt différé (25 %) |
|---|---:|---:|
| Plus-value sur constructions | + 480 000 | + 120 000 |
| Plus-value sur matériel industriel | + 100 000 | + 25 000 |
| Plus-value sur stocks | + 60 000 | + 15 000 |
| Amortissements dérogatoires reconstitués | + 72 000 | + 18 000 |
| Engagements de retraite (déductibles au versement) | – 120 000 | – 30 000 |
| Frais d'établissement non amortis (encore déductibles) | – 60 000 | – 15 000 |
| **Total net : passif d'impôt différé** | **+ 532 000** | **+ 133 000** |

Pas d'impôt différé sur le terrain ni sur les actions ISOLVÈRE (hypothèse de l'annexe 2.4 : non amortissables, aucune cession envisagée), ni sur le fonds commercial, qui est un élément résiduel [V F01 § 3.3]. Le solde net (133 000 €) est inscrit en **provision pour impôts (compte 1523)**.

**Actif net réel identifié (0,5 pt)**

| | Montant |
|---|---:|
| Actifs identifiés | 8 300 000 |
| – Provision pour litiges | – 50 000 |
| – Engagements de retraite | – 120 000 |
| – Provision pour impôts (impôt différé net) | – 133 000 |
| – Emprunts bancaires | – 1 300 000 |
| – Fournisseurs | – 1 050 000 |
| – Dettes sociales et fiscales (210 000 + 130 000) | – 340 000 |
| **Actif net réel identifié** | **5 307 000** |

**Fonds commercial et composition des apports (1 pt).** Fonds commercial = valeur globale des apports – actif net identifié = 6 300 000 – 5 307 000 = **993 000 €**. L'écart positif est inscrit au traité sur la ligne « fonds commercial » et repris au bilan d'ISOLVÈRE (compte 207) [V art. 744-1, F01 § 3.1].

Contrôle à partir des capitaux propres de FAÇALINE (provisions réglementées comprises) : 4 380 000 – 60 000 + 300 000 + 480 000 + 100 000 + 300 000 + 60 000 – 120 000 – 133 000 = 5 307 000 € ; 5 307 000 + 993 000 = 6 300 000 €.

Les apports (6 300 000 €) se composent donc des actifs identifiés (8 300 000 €), dont 750 000 € d'actions ISOLVÈRE, et du fonds commercial (993 000 €), diminués des passifs identifiés (2 993 000 €).

---

### 2.3 Parité, soulte et plafond légal (6 pts)

**a) Parité d'échange (1 pt)**
- Valeur unitaire ISOLVÈRE : 15 000 000 / 200 000 = **75 €** ; valeur unitaire FAÇALINE : 6 300 000 / 60 000 = **105 €**.
- Parité exacte : 105 / 75 = 7 / 5, soit **7 actions ISOLVÈRE pour 5 actions FAÇALINE**, sans soulte. Elle conduirait à émettre 60 000 × 7 / 5 = 84 000 actions.
- Les 60 000 actions FAÇALINE sont toutes échangées : ISOLVÈRE n'en détient aucune, il n'y a pas de quote-part non rémunérée [V F01 § 5.1].

**b) Soulte et contrainte légale (2,5 pts).** Les associés peuvent recevoir, en plus des actions, une soulte en espèces dont le montant ne peut pas dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-1, F01 § 4].

| | Projet des dirigeants (4 pour 3) | Solution de la directrice financière (11 pour 8) |
|---|---:|---:|
| Actions ISOLVÈRE à émettre | 60 000 × 4 / 3 = 80 000 | 60 000 × 11 / 8 = 82 500 |
| Valeur des actions FAÇALINE reçues (60 000 × 105) | 6 300 000 | 6 300 000 |
| Valeur des actions ISOLVÈRE remises (× 75) | 6 000 000 | 6 187 500 |
| **Soulte** | **300 000** | **112 500** |
| Soulte par lot échangé | 15 € pour 3 actions FAÇALINE (5 € par action) | 15 € pour 8 actions FAÇALINE (1,875 € par action) |
| Valeur nominale des actions attribuées (× 20) | 1 600 000 | 1 650 000 |
| **Plafond légal (10 %)** | **160 000** | **165 000** |
| Conclusion | **Soulte illégale** (300 000 > 160 000) | **Soulte légale** (112 500 ≤ 165 000) |

Barème : actions émises et soulte du projet des dirigeants (0,75), contrôle du plafond et conclusion (0,75) ; même travail pour la solution de la directrice financière (1). Le contrôle par lot donne la même conclusion : 15 € > 10 % × 4 × 20 = 8 € pour le projet des dirigeants ; 15 € ≤ 10 % × 11 × 20 = 22 € pour la solution de la directrice financière.

**c) Conseil à Mme MAZERAT (1,75 pt)**
- *Nombre minimal d'actions (0,5 pt).* Pour n actions émises, la soulte vaut 6 300 000 – 75 n et le plafond 10 % × 20 n = 2 n. La soulte est légale si 6 300 000 – 75 n ≤ 2 n, soit n ≥ 6 300 000 / 77 = 81 818,2, donc **au moins 81 819 actions** (soulte 163 575 € ≤ plafond 163 638 €). Ramené à une action FAÇALINE, l'échange doit porter sur au moins 15 / 11 = 1,364 action ISOLVÈRE. La parité des dirigeants (4 / 3 = 1,333) est en dessous ; celle de la directrice financière (11 / 8 = 1,375) et la parité exacte (7 / 5 = 1,4) sont au-dessus.
- *Choix d'une parité (0,5 pt).* Le nombre minimal (81 819 actions) ne correspond à aucune parité simple. Il faut retenir une parité au moins égale à 15 / 11 et assez simple pour l'échange : la solution **11 pour 8 avec une soulte de 112 500 €** est légale ; la parité exacte 7 pour 5, sans soulte, l'est aussi. Le gain recherché par les dirigeants est faible : 80 000 actions au lieu de 82 500, pour une participation de MAZERAT PARTICIPATIONS de 51,9 % au lieu de 51,4 %, alors que la soulte décaissée passerait de 112 500 € à 300 000 €. MAZERAT PARTICIPATIONS garde le contrôle dans les deux cas.
- *Rompus (0,25 pt).* Avec la parité 11 pour 8, les deux dirigeants de FAÇALINE dont le nombre d'actions n'est pas un multiple de 8 détiennent des rompus. Ils peuvent acheter ou vendre entre associés les droits formant rompus pour constituer des lots de 8 actions. Une soulte complémentaire pour les rompus reste possible, à condition que la soulte totale respecte le plafond légal (marge disponible : 165 000 – 112 500 = 52 500 €).
- *Équité (0,5 pt).* Dans chaque solution, la valeur des actions remises augmentée de la soulte égale la valeur des actions reçues (80 000 × 75 + 300 000 = 82 500 × 75 + 112 500 = 6 300 000 €) [V méthode du corrigé du sujet zéro, F01 § 4]. Après l'opération, la valeur de l'action ISOLVÈRE reste de 75 € : (15 000 000 + 6 300 000 – 750 000 d'actions annulées – 112 500 de soulte) / 272 500 actions = 75 €. Aucun groupe d'actionnaires ne s'enrichit au détriment de l'autre : l'échange est équitable. Le projet des dirigeants l'est aussi en valeur, mais il est illégal.

**d) Répartition du capital après l'opération (0,75 pt).** Nombre d'actions après l'opération : 200 000 + 82 500 – 10 000 actions propres annulées = **272 500**.

| Actionnaire | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| MAZERAT PARTICIPATIONS | 140 000 | 70,0 % | 140 000 | 51,4 % |
| Salariés et investisseurs individuels | 50 000 | 25,0 % | 50 000 | 18,3 % |
| FAÇALINE (actions annulées) | 10 000 | 5,0 % | – | – |
| BRANDÉLIA CAPITAL (48 000 × 11 / 8) | – | – | 66 000 | 24,2 % |
| Dirigeants de FAÇALINE (12 000 × 11 / 8) | – | – | 16 500 | 6,1 % |
| **Total** | **200 000** | **100 %** | **272 500** | **100 %** |

Chaque action donnant une voix, les droits de vote suivent la même répartition. Sans l'annulation des actions propres, MAZERAT PARTICIPATIONS ne détiendrait que 140 000 / 282 500 = 49,6 % du capital : l'annulation renforce sa position.

---

### 2.4 Écritures de fusion chez ISOLVÈRE au 1er janvier 2027 (6 pts)

Les écritures complètes figurent dans `corrige.yaml` (I1 à I4) ; elles sont équilibrées (contrôle `ue4check`). Schéma type : `gabarits/ecritures_types/02_fusion_valeur_reelle.yaml`.

**I1 — Augmentation de capital et soulte (1,5 pt).** Prime de fusion = valeur des apports – augmentation de capital – soulte = 6 300 000 – 1 650 000 – 112 500 = **4 537 500 €** [V F01 § 4 et § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 6 300 000 | |
| 101 Capital (82 500 × 20) | | 1 650 000 |
| 1042 Primes de fusion | | 4 537 500 |
| 468 Divers comptes créditeurs – soulte due aux associés de FAÇALINE | | 112 500 |

**I2 — Réalisation des apports à la valeur réelle (2 pts).** Les éléments sont inscrits à leur valeur réelle, sans reprise des amortissements de FAÇALINE ; les éléments non comptabilisés par l'absorbée (retraites, impôt différé) et le fonds commercial sont inscrits [V art. 744-1, F01 § 3.1 et § 9]. Les actions ISOLVÈRE reçues sont inscrites au compte 2772 (voir I4).

| Compte | Débit | Crédit |
|---|---:|---:|
| 207 Fonds commercial | 993 000 | |
| 211 Terrains | 900 000 | |
| 2131 Bâtiments | 2 280 000 | |
| 2154 Matériels industriels | 900 000 | |
| 2772 Actions propres ou parts propres en voie d'annulation | 750 000 | |
| 31 Matières premières et fournitures | 960 000 | |
| 411 Clients | 2 100 000 | |
| 512 Banques | 410 000 | |
| 1511 Provisions pour litiges | | 50 000 |
| 1521 Provisions pour pensions et obligations similaires | | 120 000 |
| 1523 Provisions pour impôts | | 133 000 |
| 164 Emprunts auprès des établissements de crédit | | 1 300 000 |
| 401 Fournisseurs | | 1 050 000 |
| 431 Sécurité sociale (dettes sociales) | | 210 000 |
| 44 État et autres collectivités publiques (dettes fiscales) | | 130 000 |
| 4561 Associés – Comptes d'apport en société | | 6 300 000 |

**I3 — Versement de la soulte (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 468 Divers comptes créditeurs – soulte due aux associés de FAÇALINE | 112 500 | |
| 512 Banques | | 112 500 |

**Actions propres reçues : analyse (0,75 pt).** Par la fusion, ISOLVÈRE reçoit 10 000 de ses propres actions. Leur annulation ne dégage **aucun mali** [V art. 745-3, F01 § 5.3 et § 6] : l'écart entre leur valeur d'apport et leur nominal ne correspond à aucun actif ; le traiter comme un mali reviendrait à inscrire à l'actif un incorporel généré en interne. Les actions sont annulées **par capitaux propres**, selon les règles du rachat d'actions propres en vue de leur annulation [V recueil ANC, IR 3 sous l'art. 745-3, F01 § 6]. Elles sont inscrites au compte 2772 ; la **réduction de capital** porte sur leur valeur nominale (10 000 × 20 = 200 000 €) ; l'excédent de leur valeur (750 000 – 200 000 = 550 000 €) est imputé sur un compte distribuable de capitaux propres, ici la prime de fusion [V PCG art. 1212-27, F01 § 6]. Le programme range ce cas parmi les détentions de l'absorbée dans l'absorbante [V guide p. imprimée 166, F01 § 6].

**I4 — Annulation des actions propres (1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital (10 000 × 20) | 200 000 | |
| 1042 Primes de fusion | 550 000 | |
| 2772 Actions propres ou parts propres en voie d'annulation | | 750 000 |

Après I1 à I4, le compte 4561 et le compte 2772 sont soldés ; le capital s'élève à 4 000 000 + 1 650 000 – 200 000 = 5 450 000 €, soit 272 500 actions de 20 €.

---

### 2.5 Écritures complémentaires (2 pts)

**I5 — Frais de fusion (1 pt).** Les frais de fusion peuvent être imputés sur la prime de fusion [V PCG art. 212-9, F01 § 7]. L'imputation se fait nette d'impôt [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 120 000 × 75 % = **90 000 €** sur la prime. Les frais sont déduits du résultat fiscal 2027 ; l'économie d'impôt (30 000 €) diminue la dette d'impôt sur les sociétés au lieu d'être comptabilisée en produit.

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (120 000 × 75 %) | 90 000 | |
| 444 État – Impôts sur les bénéfices (120 000 × 25 %) | 30 000 | |
| 512 Banques | | 120 000 |

**I6 — Reconstitution des amortissements dérogatoires (1 pt).** Engagement pris au titre du régime de faveur (annexe 2.1) : ISOLVÈRE reconstitue à son passif les amortissements dérogatoires de FAÇALINE, qu'elle reprendra dans les mêmes conditions [V CGI art. 210 A-3-a ; BOI-IS-FUS-30-20 § 10, F02 § 2]. Ces provisions réglementées font partie des capitaux propres de FAÇALINE : elles ne figurent pas dans l'écriture de réalisation et sont reconstituées par prélèvement sur la prime de fusion [V corrigé du sujet zéro, Q 2.6, F01 § 8].

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion | 72 000 | |
| 145 Amortissements dérogatoires | | 72 000 |

---

### 2.6 Capitaux propres d'ISOLVÈRE juste après l'opération (2 pts)

**Tableau (1 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (272 500 actions × 20) | 4 000 000 | + 1 650 000 – 200 000 | 5 450 000 |
| Primes d'émission | 600 000 | | 600 000 |
| Primes de fusion | 0 | + 4 537 500 – 550 000 – 90 000 – 72 000 | 3 825 500 |
| Réserve légale | 400 000 | | 400 000 |
| Autres réserves | 5 300 000 | | 5 300 000 |
| Provisions réglementées (amortissements dérogatoires) | 0 | + 72 000 | 72 000 |
| **Total** | **10 300 000** | **+ 5 347 500** | **15 647 500** |

Contrôle : + 5 347 500 = apports (6 300 000) – soulte (112 500) – actions propres annulées (750 000) – frais nets d'impôt (90 000).

**Commentaire pour Mme MAZERAT (1 pt, grille de niveaux)**

| Niveau | 0 | 0,5 | 1 |
|---|---|---|---|
| Attendu | Absence ou idées sans lien avec le cas | Une idée pertinente pour les actionnaires ou pour les créanciers | Au moins une idée pour chacun, chiffrée |

Idées attendues :
- *Actionnaires d'ISOLVÈRE* : la famille, par MAZERAT PARTICIPATIONS, passe de 70 % à 51,4 % mais garde la majorité ; l'annulation des 10 000 actions propres limite la dilution. BRANDÉLIA CAPITAL devient le deuxième actionnaire (24,2 %), sans contrôle ; ses conditions de sortie, propres à une société de capital-investissement, sont à anticiper. L'échange étant équitable, la valeur de l'action reste de 75 €.
- *Créanciers d'ISOLVÈRE* : les capitaux propres augmentent de 5,3 M€ et les créanciers de FAÇALINE deviennent ceux d'ISOLVÈRE. Mais l'actif reçu comprend 993 000 € de fonds commercial, non amortissable et exposé à une dépréciation. La soulte et les frais réduisent la trésorerie de 232 500 €. La provision pour impôts (133 000 €) traduit un impôt qui sera payé à mesure de la réintégration des plus-values.

---

### Réponses tolérées
- **Compte de la soulte** : la soulte due peut être portée au crédit d'un autre compte de tiers des associés, ou directement au crédit du 512 dans l'écriture I1 puisqu'elle est versée le jour même. Le compte 4567, que certains candidats utilisent, est réservé par le PCG aux sommes dues après un amortissement du capital [V art. 1214-45, F01 § 6] : l'accepter sans le valoriser.
- **Imputation de l'excédent sur les actions propres** : sur un autre compte de réserves distribuables (1068 Autres réserves) ou sur la prime d'émission, au lieu de la prime de fusion [V art. 1212-27 : « compte distribuable de situation nette », F01 § 6].
- **Annulation sans passage par 2772** : débit 101 et 1042, crédit 4561, à la place de l'inscription en 2772 suivie de l'annulation, si la réduction de capital au nominal est explicite.
- **Frais de fusion** : présentation en deux écritures (1042 / 512 pour 120 000, puis 444 / 1042 pour 30 000).
- **Conseil sur la parité** : toute parité au moins égale à 15 / 11 et compatible avec un échange simple, avec la soulte et le plafond correctement calculés (par exemple 7 pour 5 sans soulte).
- **Rompus** : toute solution pratique cohérente (achat ou vente de droits entre associés, regroupement, soulte de rompus dans la limite du plafond).
- **Impôts différés** : présentation séparée des impôts différés passifs (178 000 €, base 712 000 €) et actifs (45 000 €, base 180 000 €), si le solde net de 133 000 € est retenu dans les apports.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion mal calculée : oubli de la soulte (prime de 4 650 000 €), ou prime réduite de la valeur des actions propres dans l'écriture I1 au lieu de l'annulation séparée.
- `JUR-R03` Oubli de la reconstitution des amortissements dérogatoires par imputation sur la prime de fusion.
- `JUR-R05` Difficulté à s'adapter à une situation un peu différente : constater un « mali » ou un « boni » sur les actions propres reçues, ou laisser ces actions à l'actif d'ISOLVÈRE.
- `JUR-F04` Absence de contrôle d'équilibre de l'écriture de réalisation des apports.
- Erreurs propres à ce cas :
  - plafond de la soulte calculé sur la valeur d'échange des actions ou sur le nominal des actions FAÇALINE, au lieu du nominal des actions ISOLVÈRE attribuées ;
  - valeur de FAÇALINE retraitée des actions ISOLVÈRE, alors que la valeur d'échange fournie les comprend déjà ;
  - reprise des frais d'établissement dans les apports, ou impôt différé calculé sur le terrain, les actions ISOLVÈRE ou le fonds commercial ;
  - répartition du capital sans déduire les actions annulées (MAZERAT PARTICIPATIONS à 49,6 % du capital).

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Audit des comptes, audit contractuel, prestations | `3.2.a` Notion d'audit des comptes et cadre conceptuel | 3 |
| 3.2 Moyens d'action et honoraires | `3.2.b` Moyens d'action du commissaire aux comptes | 4 |
| 3.3 Élaboration et organisation des NEP ; norme applicable au litige | `3.1.d` Référentiel normatif (NEP) | 3 |
| 3.4 Cycle immobilisations : risques, assertions, procédures | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit | 5 |
| 3.5 Opinion | `3.2.e` Portée des opinions | 3 |
| 3.6 IRO, double matérialité, étendue des informations, périmètre de reporting | `3.3.b` Principes de construction du reporting ; `3.3.a` Architecture et champ | 4 |
| 3.7 Objectifs, assurance, axes et démarche | `3.4.a` Objectifs de la mission ; `3.4.b` Démarche d'audit de durabilité | 4 |
| 3.8 Avis par axe ; élément d'attention particulière | `3.4.c` Portée des avis | 4 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes annuels (18 points)

### 3.1 Audit des comptes, audit contractuel et autres prestations (3 pts)

**Définition, objectif et assurance (1 pt)**
- Le commissaire aux comptes **certifie**, en justifiant de ses appréciations, que les comptes annuels sont **réguliers et sincères** et donnent une **image fidèle** du résultat de l'exercice, de la situation financière et du patrimoine [V L. 821-53 al. 1]. Pour cela, il formule une **opinion** après avoir mis en œuvre un audit des comptes [V NEP principes § 01].
- Cette opinion repose sur une **assurance raisonnable** : une assurance élevée, mais **non absolue**, que les comptes pris dans leur ensemble ne comportent pas d'anomalies significatives. L'assurance n'est pas absolue à cause des limites de l'audit : sondages, limites des dispositifs de contrôle de l'entité, éléments qui conduisent davantage à des présomptions qu'à des certitudes [V NEP principes § 08-09].
- L'audit ne garantit ni la viabilité de l'entité ni la qualité de sa gestion [V L. 821-55]. La mission exclut toute immixtion dans la gestion [V L. 821-54 I].

**Typologie (1 pt)**

| Notion | Contenu |
|---|---|
| **Certification légale** (audit légal) | Mission confiée au commissaire aux comptes **par la loi** ; elle aboutit à une opinion sur les comptes [V L. 821-2 III, L. 821-53] |
| **Audit contractuel** | Audit réalisé **à la demande** de l'entité, hors obligation légale ; pour un commissaire aux comptes, c'est une **prestation** [S, notion doctrinale, F11 § 1.2] |
| **Autres prestations** | Services et attestations qui ne relèvent pas d'une mission légale ; une **lettre de mission** est obligatoire [V L. 821-2 IV, L. 821-3 2°, R. 821-195] |

CALORÈNE n'est pas une EIP : aucune liste fermée de services interdits ne s'applique. VERCLAIR ne peut toutefois accepter une prestation qui créerait un **risque d'autorévision** ou compromettrait son indépendance sans mesure de sauvegarde appropriée [V L. 821-28 IV ; F10 § 5]. On valorise aussi la distinction entre audit **externe** (professionnel indépendant de l'entité) et audit **interne** (fonction de l'entité) [S, F11 § 1.2].

**Réponses à la métropole (1 pt)**
- **Demande (a), « audit complet » pour « garantir » l'absence d'erreur (0,5 pt)** : la certification **est déjà** un audit des comptes 2026, conduit selon les NEP. Un second audit des mêmes comptes n'apporterait pas une assurance d'une autre nature. Surtout, aucun audit ne peut garantir l'absence de toute erreur : l'assurance est raisonnable, et elle porte sur les anomalies **significatives** des comptes pris dans leur ensemble. VERCLAIR explique la portée de son rapport, que la métropole recevra comme actionnaire.
- **Demande (b), plan d'investissement (0,5 pt)** : juger l'**opportunité** de l'investissement relève de la gestion, dans laquelle le commissaire aux comptes ne peut pas s'immiscer [V L. 821-54 I]. Le plan contient des **prévisions**, qu'aucun audit ne peut garantir. VERCLAIR peut seulement proposer une **prestation** distincte de la certification, sous lettre de mission [V R. 821-195]. Elle porterait, par exemple, sur la cohérence des hypothèses avec les comptes et sur leur traduction chiffrée, sans se prononcer sur leur réalisation [S]. VERCLAIR n'a pas élaboré le plan : la prestation ne crée pas d'autorévision [S, application de L. 821-28 IV].

**Réponses tolérées** : un candidat qui présente l'audit contractuel comme une mission confiée à un autre professionnel que le commissaire aux comptes, s'il en explique le caractère contractuel.

**Erreurs fréquentes**
- Promettre une « garantie » ou une assurance absolue ; confondre assurance raisonnable et assurance limitée (`JUR-A01`).
- Accepter de se prononcer sur l'opportunité de l'investissement, au mépris de la non-immixtion (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-54 I, L. 821-55 | Objet de la certification ; non-immixtion ; absence de garantie de viabilité | [V] | F11 § 1.1 |
| C. com. L. 821-2 III-IV, L. 821-3, R. 821-195 | Missions et prestations ; lettre de mission | [V] | F10 § 5 ; F11 § 1.2 |
| C. com. L. 821-28 IV | Entité non EIP : risque d'autorévision | [V] | F10 § 5 |
| NEP principes § 01, 08-09 | Opinion ; assurance raisonnable et ses limites | [V] | F11 § 1.1 |
| Audit contractuel, audit externe et interne | Notions doctrinales | [S] | F11 § 1.2 |

### 3.2 Moyens d'action du commissaire aux comptes et honoraires (4 pts)

**Situation 2 – refus de communiquer le contrat SYLVACOOP (1,5 pt)**
- **Droit d'investigation et de communication (0,5 pt)** : à toute époque, le commissaire aux comptes opère toutes vérifications et tous contrôles. Il peut se faire communiquer sur place toutes les pièces utiles à sa mission, **notamment les contrats**, les livres, les documents comptables et les registres des procès-verbaux [V L. 821-60].
- **Arguments du directeur général (0,5 pt)** :
  - le secret ne peut pas être opposé au commissaire aux comptes, sauf par les auxiliaires de justice [V L. 821-61 dernier al.]. Une clause de confidentialité conclue avec un fournisseur ne fait donc pas obstacle à la communication ;
  - VERCLAIR est lui-même tenu au **secret professionnel** [V L. 821-35] : la confidentialité voulue par le fournisseur est préservée ;
  - le contrat intéresse bien les comptes. Un engagement de volumes sur dix ans est un engagement à décrire dans l'annexe, et il peut révéler un contrat défavorable. Examiner un contrat n'est pas s'immiscer dans la gestion.
- **Conséquences si le refus persiste (0,5 pt)** :
  - mettre obstacle aux vérifications du commissaire aux comptes est, pour les dirigeants, un **délit** (5 ans d'emprisonnement et 75 000 € d'amende) [V L. 821-6 3°]. Un refus persistant de communiquer une pièce utile peut caractériser cet obstacle [S] ;
  - VERCLAIR porte la difficulté à la connaissance du conseil d'administration [S, application de L. 821-63 I] ;
  - faute d'éléments probants, il subit une **limitation** de ses travaux. Il en tire les conséquences dans son opinion : réserve pour limitation si les incidences sont circonscrites, impossibilité de certifier sinon [V NEP rapport § 11 et 14].

  Il peut aussi demander à SYLVACOOP de confirmer les termes du contrat, la confirmation des tiers pouvant porter sur les termes d'un contrat [V NEP confirmations § 5]. Cette démarche ne dispense pas la direction de son obligation de communication.

**Situation 3 – opposition à la confirmation auprès de DÔMHABITAT (1 pt)**
- La demande de confirmation est une technique dont le commissaire aux comptes **maîtrise** la sélection, la rédaction, l'envoi et la réception [V NEP confirmations § 9]. Face à l'opposition de la direction, il **examine les motifs** du refus. S'il les juge fondés, il met en œuvre des **procédures alternatives**. Sinon, ou si les procédures alternatives ne fournissent pas d'éléments suffisants, il en tire les conséquences dans son rapport [V NEP confirmations § 10-12] (0,5 pt).
- En l'espèce, le motif est **documenté** : un protocole signé prévoit la confidentialité des échanges sur le différend. Il peut être jugé fondé, avec esprit critique : VERCLAIR vérifie que le refus ne sert pas à masquer une anomalie [S, jugement professionnel]. Les procédures alternatives sont nombreuses : encaissements postérieurs à la clôture, contrat d'abonnement, relevés des compteurs, factures, documents de la médiation. Pour la partie contestée (380 000 €), la confirmation n'aurait de toute façon pas suffi : elle ne permet généralement pas de conclure sur l'**évaluation** d'une créance [V NEP confirmations § 7]. Il faut apprécier la dépréciation (0,5 pt).

**Situation 4 – honoraires (1,5 pt)**

| Élément | Calcul | Résultat |
|---|---|---:|
| Base du barème (exercice 2026) | 34 200 000 + 15 000 000 + 60 000 | **49 260 000 €** |
| Tranche | 45 735 000 € < 49 260 000 € ≤ 122 000 000 € | **300 à 700 heures** |
| Honoraires correspondants | 300 × 145 € ; 700 × 145 € | 43 500 € à 101 500 € HT |
| Budget de la lettre de mission | 520 × 145 € | **75 400 € HT** |
| Proposition du directeur général | 280 h < 300 h | sous le minimum de la tranche |

- **Calcul (0,5 pt)** : les honoraires sont à la charge de l'entité [V L. 821-66 I]. Le barème fixe un nombre d'heures selon le montant cumulé du total du bilan, des produits d'exploitation et des produits financiers, hors taxes [V D. 821-188]. Les données de 2025 (46 340 000 €) conduisent à la même tranche.
- **Applicabilité (0,5 pt)** : CALORÈNE est une société anonyme. L'énoncé écarte toute règle propre aux sociétés d'économie mixte. Le barème est écarté au-delà de 122 000 000 €, pour les entités dont les titres sont cotés et pour diverses autres entités [V R. 821-194]. Par hypothèse de l'énoncé (aucune règle propre aux sociétés d'économie mixte), CALORÈNE n'entre dans aucune des catégories exclues. La base est de 49 260 000 €, inférieure à 122 000 000 €, et les titres ne sont pas cotés. **Le barème s'applique.** Le budget de 520 heures est compris dans la tranche, et la vacation horaire a été convenue avant la mission, comme l'exige le texte [V R. 821-192].
- **Positions du directeur général (0,5 pt)** :
  - plafonner les travaux à 280 heures n'est pas possible sans **dérogation**, demandée au président de la compagnie régionale [V D. 821-190]. Le nombre d'heures résulte d'ailleurs du programme de travail [V D. 821-187 ; F11 § 7], qui doit tenir compte des risques nouveaux liés à la chaufferie (3.4). Un désaccord sur la rémunération relève de la conciliation du président de la compagnie régionale [V R. 821-196] ;
  - le barème **ne s'applique pas** à la certification des informations en matière de durabilité : ces honoraires sont fixés d'un commun accord [V R. 821-194 ; F11 § 2].

**Réponses tolérées**
- **Situation 3** : un candidat qui juge le motif non fondé, s'il l'argumente (la confirmation peut porter sur la seule partie non contestée) et en tire la conséquence prévue par la norme.
- **Situation 4** : un calcul fondé sur 2025 est accepté s'il est justifié, puisqu'il conduit à la même tranche.

**Erreurs fréquentes**
- Admettre que la clause de confidentialité ou la « gestion » font obstacle à la communication du contrat (`JUR-A05`).
- Oublier le délit d'obstacle, ou l'attribuer au commissaire aux comptes et non aux dirigeants.
- Calculer la base du barème avec le seul chiffre d'affaires, ou ne pas justifier le calcul (`JUR-F02`).
- Appliquer le barème à la mission de durabilité.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-60, L. 821-61 | Droit d'investigation et de communication ; secret non opposable | [V] | F11 § 2 ; F10 § 7 |
| C. com. L. 821-35 | Secret professionnel du commissaire aux comptes | [V] | F10 § 7 |
| C. com. L. 821-6 3° | Délit d'obstacle (dirigeants) | [V] | F11 § 2 ; F09 |
| C. com. L. 821-63 I | Communication aux organes | [V] | F11 § 5 |
| NEP confirmations § 5, 7, 9-12 | Objet, limites, maîtrise de la procédure, refus de la direction | [V] | F11 § 6.3 |
| NEP rapport § 11 et 14 | Limitation : réserve ou impossibilité | [V] | F11 § 8.1 |
| C. com. L. 821-66 I, D. 821-188, D. 821-190, R. 821-192, R. 821-194, R. 821-196 | Honoraires, barème, dérogation, vacation, champ, conciliation | [V] | F11 § 2 |

### 3.3 Les NEP : élaboration, organisation et norme applicable au litige (3 pts)

**Processus d'élaboration (1 pt)** [V F11 § 3.1-3.2]
1. Le commissaire aux comptes applique les normes d'audit internationales adoptées par la Commission européenne. **À défaut**, il applique les normes adoptées par la **H2A** et homologuées par arrêté du garde des Sceaux. Aucune norme internationale n'ayant été adoptée par la Commission, ce sont les NEP qui s'appliquent [V L. 821-11 I].
2. La H2A adopte un **plan d'orientation à trois ans** et un **programme de travail annuel**, selon ses besoins et les demandes notamment du garde des Sceaux, de l'AMF, de l'ACPR, de l'ANC ou de la **CNCC** [V L. 820-23 I-II].
3. Les projets sont élaborés par une **commission de normalisation** placée auprès de la H2A. Celle qui traite de l'audit des comptes comprend deux commissaires aux comptes proposés par la CNCC [V L. 820-4].
4. La **CNCC** rend un **avis** dans le délai d'un mois [V L. 820-23 IV, R. 820-52, D. 820-53].
5. Le **collège de la H2A** adopte la norme [V L. 820-23 IV].
6. Le garde des Sceaux l'**homologue** par arrêté ; elle est codifiée dans la partie « Arrêtés » du Code de commerce [V L. 820-23 V].

**Organisation du corpus (0,5 pt).** Les NEP sont regroupées par familles [V tableau H2A ; regroupement par numérotation : S] :
- principes ;
- acceptation de la mission, documentation et communication ;
- planification et évaluation des risques ;
- éléments probants ;
- utilisation des travaux d'autres professionnels ;
- rapports ;
- petites entreprises et entités particulières ;
- autres interventions légales.

Chaque norme est découpée en **paragraphes numérotés** (introduction, définitions, principes, documentation) [V F11 § 3.4]. Le candidat n'a pas à connaître les numéros.

**Norme applicable et conduite à tenir (1,5 pt)**
- **Identification (0,5 pt)** : le litige relève de la **norme B** (caractère probant des éléments collectés, applications spécifiques : litiges). La demande de 450 000 € représente **trois fois** le seuil de signification (150 000 €, voir 3.5). Elle peut appeler une provision et, au minimum, une information dans l'annexe. Les assertions en jeu sont l'exhaustivité des passifs et l'exhaustivité de l'information de l'annexe.
- **Conduite (0,5 pt)** : VERCLAIR **demande à la direction d'interroger l'avocat** de CALORÈNE [V NEP applications spécifiques § 7-8]. En pratique, l'avocat répond directement au commissaire aux comptes [S]. Le coût de la démarche n'est pas un motif recevable. VERCLAIR examine aussi l'assignation et les correspondances, et il obtient des déclarations écrites de la direction [V F11 § 5].
- **Conséquences d'un refus maintenu (0,5 pt)** : VERCLAIR ne peut pas apprécier le risque. Selon la norme B, il en tire les conséquences dans son rapport. Le poste est identifié : la limitation conduit à une **réserve pour limitation** si ses incidences sont circonscrites [V NEP rapport § 11]. VERCLAIR communique au préalable ses motifs aux organes [V NEP rapport § 06 ; L. 821-63 I]. Si l'avocat confirme un risque probable et que la direction refuse de provisionner ou d'informer, il s'agit d'une **anomalie** à apprécier selon la norme D.

  On valorise le lien avec la durabilité : les rejets dans l'air sont aussi un IRO de l'état de durabilité (3.6) [S].

**Réponses tolérées** : la norme D citée **en complément** de la norme B, si le candidat raisonne sur une provision non comptabilisée.

**Erreurs fréquentes**
- Choisir la norme A (confirmations) : l'avocat n'est pas un débiteur ou un créancier dont on confirme un solde (`JUR-F07`).
- Réciter le corpus sans appliquer la norme à la situation (`JUR-A06`).
- Exiger des numéros de NEP ou en inventer.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-11 I | Normes internationales adoptées, à défaut NEP homologuées | [V] | F11 § 3.1 |
| C. com. L. 820-4, L. 820-23, R. 820-52, D. 820-53 | Programme, commissions, avis de la CNCC, adoption, homologation | [V] | F11 § 3.2 |
| Tableau du référentiel normatif de la H2A | Organisation du corpus | [V] ; familles : [S] | F11 § 3.3 |
| NEP applications spécifiques § 7-8 | Litiges : interroger les avocats ; refus | [V] | F11 § 6.4 |
| NEP rapport § 06, 11 | Communication préalable des motifs ; réserve pour limitation | [V] | F11 § 8.1 |

### 3.4 Cycle immobilisations : risques, assertions et procédures (5 pts)

**Appréciation du risque d'anomalies significatives (1,5 pt)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41]
- **Composantes (0,5 pt)** : le risque d'anomalies significatives (RAS) est propre à l'entité. Il comprend :
  - le **risque inhérent** : possibilité qu'une anomalie significative se produise, sans tenir compte des contrôles de l'entité ;
  - le **risque lié au contrôle** : risque qu'une anomalie ne soit ni prévenue ni détectée et corrigée par les contrôles de l'entité.

  Le **risque de non-détection**, lui, est propre à la mission.
- **Risque inhérent élevé (0,5 pt)** :
  - opération **non courante et significative** : 11 340 000 €, soit 33,2 % du total du bilan (34 200 000 €) ;
  - **jugements** : date de mise en service, coûts incorporables, durées d'utilisation, traitement d'une subvention assortie d'une condition de remboursement ;
  - **démantèlement** de l'ancienne chaufferie ;
  - **incitation** à présenter un résultat flatteur aux banques qui financeront le plan 2027-2031 : c'est un facteur de risque de fraude [V NEP risques § 02].
- **Risque lié au contrôle élevé (0,5 pt)** :
  - poste de comptable chargé des immobilisations vacant ;
  - transferts passés en fin d'exercice à partir d'un tableau de la direction technique ;
  - aucun rapprochement avec le marché de travaux ;
  - information non transmise entre la technique et la comptabilité (chaufferie au fioul).

  Sans test des contrôles, le RAS au niveau des assertions correspond au risque inhérent évalué [V NEP risques § 41].

**Orientation des travaux (0,5 pt).** Le risque de non-détection acceptable est **faible**. VERCLAIR renforce ses **procédures de substance** :
- travaux à la clôture ;
- éléments probants externes, plus fiables que les éléments internes [V NEP éléments probants § 6] ;
- échantillons élargis ;
- équipe expérimentée [V NEP principes § 13 ; NEP réponses § 03-13].

Il ne s'appuie pas sur des contrôles qui n'existent plus.

**Assertions et procédures (3 pts, 1 pt par risque pertinent, dans la limite de 3 pts : 0,5 pt pour l'assertion, 0,5 pt pour une procédure adaptée et justifiée)**

| Risque | Assertion | Procédure et justification |
|---|---|---|
| Amortissement calculé à partir du procès-verbal (01/10) et non de la mise en service (01/07) | **Évaluation** des immobilisations (solde) ; **mesure** et **séparation des exercices** des dotations et de la quote-part de subvention (flux) | **Inspection** des relevés des compteurs et du registre d'exploitation pour dater la mise en service. Ces données internes sont corroborées par des éléments externes : procès-verbal de réception signé par le constructeur, règlements des premiers abonnés (factures de juillet 2026). Puis **vérification du calcul** : annuité 6 000 000 / 25 + 4 800 000 / 20 = 480 000 €, soit 240 000 € pour six mois contre 120 000 € comptabilisés ; quote-part de subvention : 30 % de la dotation |
| Ancienne chaufferie au fioul démantelée mais toujours à l'actif | **Existence** des immobilisations (solde) | **Inspection physique** des actifs (visite du site) et rapprochement du fichier des immobilisations avec l'inventaire physique. L'entretien avec le directeur technique (demande d'information) est corroboré par l'observation directe, plus probante |
| Frais de formation (50 000 €) et d'inauguration (90 000 €) immobilisés | **Classification** (flux) ; **évaluation** du coût d'entrée (solde) | **Inspection des factures** inscrites en immobilisations et rapprochement avec le marché de travaux et ses avenants. Seuls les coûts directement attribuables sont incorporables (règle de l'annexe 3.4) |
| Facture de solde du constructeur non parvenue | **Exhaustivité** des immobilisations et des dettes sur immobilisations (solde) | **Demande de confirmation ouverte** au constructeur (montant dû, retenues de garantie, avenants) et examen des factures reçues après la clôture : ce sont des éléments externes, adaptés à l'exhaustivité |
| Subvention de 3 240 000 €, dont 648 000 € à recevoir, avec condition de remboursement | **Droits et obligations**, **évaluation** (solde) ; **exhaustivité** de l'information de l'annexe | **Inspection de la convention** et confirmation auprès de la région et de l'agence (montant accordé, versé, conditions). Appréciation de la condition des 70 % à partir des données de production, en lien avec l'état de durabilité (connectivité) |

Les procédures analytiques sont acceptées en complément : rapport de la dotation à la base amortissable, rapport de la quote-part de subvention à la dotation. Elles ne suffisent pas seules face à un risque élevé.

**Réponses tolérées**
- Tout couple risque / assertion / procédure cohérent avec l'annexe 3.4.
- La « réalité » des acquisitions (flux) pour les coûts immobilisés, si elle est justifiée.

**Erreurs fréquentes**
- Confondre « existence » (solde) et « réalité » (flux) ; employer « exhaustivité » pour un actif surévalué (`JUR-A01`).
- Proposer des procédures génériques sans lien avec les faits de l'annexe (`JUR-A05`, `JUR-A06`).
- Développer l'organisation des dispositifs de contrôle de l'entité, qui relève de l'UE 3, au lieu de l'évaluer comme composante du risque.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 10-13 | Risque d'audit, RAS, risque de non-détection | [V] | F11 § 4.1 |
| NEP risques § 02, 39-41 | Facteurs de risque inhérent ; évaluation sans test des contrôles | [V] | F11 § 4.1 |
| NEP éléments probants § 3, 6, 9, 10 | Assertions ; fiabilité ; techniques de contrôle | [V] | F11 § 4.3, 6.1-6.2 |
| NEP réponses § 03-13 | Procédures en réponse aux risques | [V] | F11 § 5 |
| NEP confirmations § 4-5 | Confirmation ouverte ; termes d'un contrat | [V] | F11 § 6.3 |
| Règles comptables de l'annexe 3.4 | Coût d'entrée, mise en service, subvention, sortie d'actif | données de l'énoncé | — |

### 3.5 Opinion sur les comptes 2026 (3 pts)

**Analyse (1,5 pt)**

| Élément | Calcul | Résultat |
|---|---|---:|
| Seuil de signification | 1 % × 15 000 000 € | **150 000 €** |
| Anomalie 1 (amortissement et subvention) | 120 000 − 36 000 | 84 000 € < seuil |
| Anomalie 2 (ancienne chaufferie) | valeur nette comptable | 96 000 € < seuil |
| **Cumul des anomalies non corrigées** | 84 000 + 96 000 | **180 000 € > 150 000 €** |
| Poids dans le résultat avant impôt | 180 000 / 860 000 | 20,9 % |

- **Seuil (0,5 pt)** : 150 000 €. Le pourcentage est une hypothèse du cabinet : les NEP n'en fixent aucun [V NEP caractère significatif § 10, 17 ; F11 § 4.2].
- **Cumul (0,5 pt)** : chaque anomalie est inférieure au seuil, mais le commissaire aux comptes apprécie les anomalies non corrigées **individuellement ou cumulées** (norme D) [V NEP anomalies § 14]. Leur cumul, 180 000 €, **dépasse** le seuil. L'argument de la direction est donc inopérant : les anomalies non corrigées sont **significatives**.
- **Autres points (0,5 pt)** :
  - l'anomalie de 140 000 € a été corrigée et n'a plus d'incidence ;
  - le contrat SYLVACOOP a été communiqué ;
  - les procédures alternatives sur DÔMHABITAT ont abouti ;
  - l'avocat a répondu.

  **Aucune limitation** ne subsiste.

**Opinion (1 pt).** Les anomalies significatives non corrigées sont **identifiées et chiffrées**. Elles portent sur deux éléments du cycle immobilisations : l'amortissement de la chaufferie et la sortie de l'ancienne chaufferie. Leurs incidences sont **clairement circonscrites**. Une réserve qui les décrit suffit à l'utilisateur pour fonder son jugement. VERCLAIR **certifie avec réserve pour désaccord** [V NEP rapport § 09-10 ; R. 821-180]. Il quantifie au mieux les incidences dans la partie « Fondement de l'opinion » :
- immobilisations nettes surévaluées de 216 000 € (120 000 + 96 000) ;
- subventions d'investissement surévaluées de 36 000 € ;
- résultat avant impôt surévalué de 180 000 €, soit 135 000 € après impôt au taux de 25 %.

Les motifs sont communiqués au préalable aux organes [V NEP rapport § 06 ; L. 821-63 I]. La direction remet une déclaration écrite sur les anomalies non corrigées [V NEP anomalies § 15-17].

**Opinions écartées (0,5 pt)**
- **Sans réserve** : impossible, les anomalies non corrigées sont significatives en cumul.
- **Refus de certifier** : il suppose des incidences **non** circonscrites ou une réserve insuffisante [V NEP rapport § 12-13]. Ici, deux postes sont identifiés et quantifiés, sans effet diffus. Le résultat corrigé reste positif (680 000 € avant impôt).
- **Impossibilité de certifier** : elle suppose une limitation aux incidences non circonscrites ou des incertitudes multiples [V NEP rapport § 14]. Aucune limitation ne subsiste.

**Réponses tolérées** : une quantification limitée à l'incidence sur le résultat (180 000 € avant impôt, ou 135 000 € après impôt) obtient les points de l'opinion, si le motif est exposé.

**Erreurs fréquentes**
- Conclure à une certification sans réserve en comparant chaque anomalie au seuil sans les cumuler.
- Conclure à une réserve pour limitation alors que les difficultés des situations 2, 3 et du litige sont levées.
- Donner l'opinion sans son motif ni sa quantification (`JUR-A02`).
- Ne pas justifier les calculs (`JUR-F02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP caractère significatif § 6, 9, 10, 17 | Seuil ; nature et circonstances ; critères | [V] | F11 § 4.2 |
| NEP anomalies § 14, 15-17 | Appréciation individuelle ou cumulée ; déclaration écrite | [V] | F11 § 8.2, § 9 |
| NEP rapport § 06, 09-14 ; C. com. R. 821-180 | Quatre opinions et leurs conditions | [V] | F11 § 8.1 |

---

### Partie B – Durabilité (12 points)

### 3.6 IRO, double matérialité et périmètre de reporting (4 pts)

**Définitions (1 pt)**
- **IRO** :
  - les **impacts** de l'entreprise sur la population ou l'environnement, positifs ou négatifs, réels ou potentiels ;
  - les **risques et opportunités**, c'est-à-dire les effets financiers des enjeux de durabilité pour l'entreprise, y compris ceux qui naissent de ses **dépendances** à l'égard de ressources naturelles, humaines ou sociales [V ESRS 1 (2023) § 14 ; ESRS 1 (2026) § 2, 39, 48].
- **Double matérialité** : un enjeu est matériel au titre de la **matérialité d'impact**, de la **matérialité financière**, ou des deux [V ESRS 1 (2023) § 28 ; ESRS 1 (2026) § 35]. On tient compte des interactions entre les deux dimensions [V ESRS 1 (2026) § 35-36].
  - Un impact négatif s'apprécie selon sa **gravité** (ampleur, étendue, caractère irrémédiable) et, s'il est potentiel, selon sa **probabilité** [V § 40].
  - Un effet financier s'apprécie selon sa probabilité et son ampleur potentielle. Il peut affecter la situation financière, la performance, les flux de trésorerie, l'**accès au financement** ou le **coût du capital** [V § 47, 50].

**Impact négatif dans la chaîne de valeur amont (0,5 pt)**

| Enjeu | Dimension | Analyse |
|---|---|---|
| Coupes rases dans des forêts privées pour produire les plaquettes | **Impact négatif** sur les sols et la biodiversité forestière | L'impact survient chez les **propriétaires forestiers**, fournisseurs de SYLVACOOP et de SYLVANOR : il se situe dans la chaîne de valeur amont, à laquelle CALORÈNE est liée par ses achats (relations d'affaires directes et indirectes) [V ESRS 1 (2026) § 39]. Gravité : étendue importante (45 000 tonnes par an, rayon de 100 km), effets difficilement réversibles sur les sols |

**Impact sur les usagers ou les riverains (0,5 pt)** : une réponse suffit.
- **Qualité de l'air** : les particules fines et les oxydes d'azote ont un **impact négatif réel** sur la santé et le cadre de vie des riverains. Il est attesté par des plaintes et par un litige. Respecter les valeurs limites ne suffit pas à écarter l'impact : le simple respect de la loi n'est pas un impact positif [V ESRS 1 (2026) § 44].
- **Précarité énergétique** : la révision de 9 % du prix de la chaleur et la hausse des impayés traduisent un **impact négatif**, réel ou potentiel, sur des usagers modestes (60 % de logements sociaux).

Les impacts positifs sont acceptés en complément : prix inférieur de 15 % au chauffage individuel au gaz, émissions évitées par le remplacement de 6 000 chaudières individuelles. Ils ne se compensent pas avec les impacts négatifs [V § 44].

**Risque ou opportunité financière (1 pt)** : une réponse argumentée suffit, l'interaction entre les deux dimensions est valorisée.
- **Risque lié à une dépendance** : le prix des plaquettes a augmenté de 22 %, alors que le prix de vente n'est révisé qu'une fois par an. La marge et les flux de trésorerie sont exposés.
- **Risque réglementaire** : des valeurs limites plus strictes à partir de 2028 imposeraient un filtre d'environ 1 500 000 €. Le litige des riverains s'y ajoute. Ce risque **naît de l'impact** sur la qualité de l'air.
- **Opportunité** : le raccordement de 4 000 logements supplémentaires, soutenu par des aides publiques, augmenterait le chiffre d'affaires. Il faciliterait aussi l'accès au financement du plan 2027-2031.

La condition de remboursement de la subvention (part renouvelable d'au moins 70 %) relie directement la durabilité aux états financiers (connectivité) [V ESRS 1 (2026) § 112-116].

**Étendue et limites des informations à publier (0,5 pt)**
- Les informations générales (ESRS 2) sont publiées quel que soit le résultat de l'analyse de matérialité [V ESRS 1 (2023) § 29 ; ESRS 1 (2026) § 29].
- Pour chaque thème matériel **seulement**, CALORÈNE publie les exigences générales (politiques, actions, indicateurs, cibles), les exigences thématiques pertinentes et, si besoin, des informations spécifiques à l'entité [V ESRS 1 (2026) § 11, 29-30].
- Elle ne publie pas d'information non matérielle issue d'une exigence ESRS, sauf informations supplémentaires signalées comme telles [V ESRS 1 (2026) § 24, 108-109].
- La chaîne de valeur n'est couverte que pour les informations matérielles, et non acteur par acteur ; des estimations sont admises [V ESRS 1 (2026) § 62-65 ; F12 § 5 et 7].

**Périmètre de reporting et SYLVANOR (0,5 pt)**
- L'état de durabilité porte sur la **même entreprise déclarante que les états financiers** [V ESRS 1 (2026) § 60]. CALORÈNE ne contrôle aucune entité : les **activités propres** sont celles de CALORÈNE seule.
- Il s'étend à la **chaîne de valeur amont** (SYLVACOOP, SYLVANOR, propriétaires forestiers) et **aval** (bailleurs, usagers). Cette extension vaut dans la mesure nécessaire à la compréhension des IRO matériels, et seulement pour les informations matérielles [V § 62-65].
- **SYLVANOR** : CALORÈNE en détient 30 % sans la contrôler. Qu'on la qualifie ou non d'entreprise associée, elle ne fait pas partie des activités propres : elle est traitée comme une **relation d'affaires** de la chaîne de valeur amont, et non comme une activité propre. Comme elle est aussi fournisseur (40 % des plaquettes), l'information **ne se limite pas à la quote-part** de 30 % du capital [V § 69-70 ; S pour l'application à une entité sans comptes consolidés]. CALORÈNE n'en a d'ailleurs pas le contrôle opérationnel, puisque SYLVANOR est exploitée par son associé majoritaire [S, F12 § 7].

**Réponses tolérées**
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences »).
- Les risques sociaux du personnel (poussières de bois, manutention) comme impact sur les activités propres, à la place d'un impact sur les riverains, s'ils sont analysés.

**Erreurs fréquentes**
- Présenter un impact sans dire qui il affecte, ni où il se situe dans la chaîne de valeur (`JUR-A05`).
- Inclure SYLVANOR dans les activités propres à hauteur de 30 %, comme dans une intégration proportionnelle.
- Ne pas exploiter les faits de l'annexe 3.6 (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2023) § 14, 28 ; ESRS 1 (2026) § 2, 35-36, 39-41, 44, 47-50 | IRO ; double matérialité ; gravité et probabilité ; effets financiers | [V] | F12 § 6 |
| ESRS 1 (2026) § 60-65, 69-70 | Activités propres ; chaîne de valeur ; entreprises associées | [V] | F12 § 7 |
| Contrôle opérationnel | Rattachement d'une entité non contrôlée | [S] | F12 § 7 |
| ESRS 1 (2026) § 112-116 | Connectivité avec les états financiers | [V] | F12 § 9 |

### 3.7 Objectifs, assurance, axes et démarche (4 pts)

**Objectifs et assurance (1,5 pt)**
- **Objet (0,5 pt)** : pour une entité tenue de publier, le commissaire aux comptes émet un **avis** sur la conformité des informations de durabilité aux ESRS, y compris sur le **processus** de détermination des informations [V L. 821-54 II]. Cet avis fait l'objet d'un **rapport de certification** destiné à l'organe qui statue sur les comptes, ici l'assemblée. CALORÈNE publie volontairement : la mission est conduite dans les mêmes conditions par hypothèse de l'énoncé. Une désignation non imposée par la loi est admise [V FAQ H2A 11/2024, p. 3 ; F12 § 11].
- **Assurance limitée (0,5 pt)** : la mission repose sur une **assurance limitée** [V LD 2026, niveau d'assurance]. Les vérifications sont moindres en **nature**, en **étendue** et en **durée** que pour une assurance raisonnable. La conclusion est exprimée sous une **forme négative** : le vérificateur n'a pas relevé d'erreurs, omissions ou incohérences importantes. L'audit des comptes, lui, repose sur une assurance raisonnable, exprimée sous une forme positive [V LD 2026 ; NEP principes § 08].
- **Distinction (0,5 pt)** : la mission est **distincte** de la certification des comptes, même si VERCLAIR exerce les deux [V LD 2026 § 2]. Elle ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].

**Axes en l'espèce (1 pt)** [V LD 2026 § 2]

| Axe | Application à CALORÈNE |
|---|---|
| 1. Processus de détermination des informations (double matérialité), y compris la **consultation du CSE** | Retenu. La consultation n'est pas une obligation légale pour une entité qui publie volontairement : elle n'est due qu'aux entités soumises à la publication [V C. trav. L. 2312-17 al. 6 ; F12 § 11 (b)]. Elle entre dans l'axe 1 en vertu de l'**accord** avec le CSE et de la **lettre de mission** (hypothèse de l'énoncé) |
| 2. Conformité des **informations** publiées aux ESRS | Retenu |
| 3. Exigences de publication liées à la **taxonomie** | **Sans objet** : CALORÈNE n'y est pas soumise (lettre de mission) [V F13 § 5, point 5] |
| 4. **Balisage** électronique | **Non exigible** tant que les règles ne sont pas adoptées [V LD 2026 § 2, § 10] |

La mission porte donc sur **deux axes**.

**Démarche et vérifications adaptées (1,5 pt)**
- **Étapes (0,5 pt)** [V LD 2026, § 4 à 17] :
  1. lettre de mission (étendue, accès aux personnes et aux documents, lettre d'affirmation, honoraires) ;
  2. prise de connaissance de l'entité, de son modèle d'affaires et de sa chaîne de valeur ;
  3. **planification**, centrée sur les informations présentant un risque important de non-conformité ou de fortes attentes des utilisateurs ;
  4. vérification du **processus** (axe 1) ;
  5. vérification des **informations** (axe 2) ;
  6. **lecture finale** de cohérence avec le rapport de gestion et les états financiers ;
  7. appréciation des éléments collectés ;
  8. événements postérieurs, communication avec la gouvernance, documentation ;
  9. **rapport** d'assurance limitée.
- **Deux vérifications sur le processus de CALORÈNE (1 pt, 0,5 pt par vérification pertinente)** :
  - vérifier que l'analyse de double matérialité couvre la **chaîne de valeur amont**, en particulier les coupes rases et SYLVANOR, et les usagers. Vérifier qu'elle a associé les **parties prenantes affectées** (riverains, bailleurs, locataires) et que les IRO ont été évalués avec les critères de gravité, de probabilité et d'ampleur financière, seuils documentés [V LD 2026 § 7.1 ; ESRS 1 (2026) § 42] ;
  - vérifier que le **CSE** a été consulté sur les informations 2026 lors de l'une au moins des consultations récurrentes (orientations stratégiques, situation économique et financière, politique sociale), au choix de l'employeur, comme le prévoit l'accord. Le schéma légal s'applique ici par analogie [V LD 2026 § 7.3 ; F12 § 11 (b)] ;
  - autre vérification acceptée : **échanges** avec l'équipe d'audit des comptes (connectivité) sur la subvention et sa condition de 70 %, le plan d'investissement et le litige des riverains [V LD 2026 § 3, § 11].

**Réponses tolérées** : un candidat qui retient l'axe « taxonomie » en le déclarant sans objet obtient les points de l'axe s'il justifie qu'il n'y a pas d'avis à émettre.

**Erreurs fréquentes**
- Présenter l'assurance limitée comme une assurance raisonnable « allégée » exprimée sous forme positive (`JUR-A01`).
- Traiter la consultation du CSE comme une obligation légale de CALORÈNE.
- Décrire la démarche sans l'appliquer à CALORÈNE (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 | Objet de l'avis ; rapport de certification ; absence de garantie | [V] | F13 § 2.1 |
| FAQ H2A, novembre 2024, p. 3 | Désignation non imposée par la loi | [V] | F12 § 11 ; F13 § 1 |
| LD 2026, niveau d'assurance, § 2, § 3, § 4-17 | Assurance limitée ; axes ; étapes ; échanges avec le commissaire aux comptes | [V] | F13 § 2-3 |
| C. trav. L. 2312-17 al. 6 | Consultation du CSE des entités soumises | [V] | F12 § 11 ; F13 § 6 |

### 3.8 Avis de VERCLAIR (4 pts)

La table de décision est celle des LD 2026 (§ 17). VERCLAIR émet un avis **par axe** [V LD 2026 § 17 ; F13 § 4.3].

| Axe | Constat | Avis |
|---|---|---|
| 1. Processus | Analyse documentée, chaîne de valeur couverte, parties prenantes associées, IRO évalués ; CSE consulté comme le prévoit l'accord | **Avis de conformité** (1 pt) |
| 2. Informations | Part d'énergie renouvelable publiée à 88 % au lieu de 80 % ; même omission dans les émissions, les émissions évitées et la trajectoire ; refus de corriger | **Avis de non-conformité, motivé** (2 pts) |

**Axe 1 – avis de conformité (1 pt).** Aucune erreur, omission ou incohérence n'a été relevée :
- l'analyse de double matérialité couvre les activités propres et la chaîne de valeur amont et aval ;
- elle a été menée avec les parties prenantes affectées ;
- les IRO ont été évalués selon les critères des ESRS ;
- le CSE a été consulté sur les informations 2026 lors de l'une des consultations récurrentes (politique sociale), ce que prévoit l'accord inclus dans la lettre de mission.

Formulation, sous forme négative : « nous n'avons pas relevé d'erreurs, omissions ou incohérences importantes concernant la conformité du processus mis en œuvre par CALORÈNE avec les ESRS » [V LD 2026, annexe 2, p. 46].

**Point (c) – élément ayant fait l'objet d'une attention particulière (0,5 pt).** L'impact sur la qualité de l'air suscite les **attentes les plus fortes des utilisateurs**, et VERCLAIR y a consacré une part importante de ses diligences. Il est présenté dans la partie relative à l'axe 1, avec un renvoi aux informations de l'état de durabilité et la description des principales diligences, en termes circonstanciés et non standardisés [V LD 2026 § 17]. Ce n'est **pas une réserve**, puisque aucune anomalie n'a été relevée. Ce n'est pas non plus une **observation** : une observation renvoie à une information publiée par l'entité, par exemple une méthode ou une limite de mesure [V LD 2026 § 17 ; F13 § 4.4].

**Axe 2 – avis de non-conformité (2 pts)**
- **Qualification (1 pt)** : l'omission de 5 000 MWh de production au gaz de décembre est une **erreur non corrigée**. Son importance remet en cause la conformité : la part renouvelable passe de 88 % à 80 %, soit 8 points d'écart. Cet indicateur est central dans la stratégie, présentée comme « presque atteinte » alors que l'écart à la cible de 90 % est en réalité de 10 points. Le motif de la direction (chiffres déjà communiqués à la métropole) est sans portée.
- **Incidences non circonscrites (1 pt)** : la même erreur fausse **plusieurs informations** de l'état de durabilité : part renouvelable, émissions de gaz à effet de serre, émissions évitées, trajectoire et description de la stratégie. Une réserve limitée à un chiffre ne suffirait pas à l'utilisateur pour fonder son jugement. Selon la table de décision, une erreur non corrigée dont les incidences ne sont pas circonscrites conduit à un **avis de non-conformité, motivé** [V LD 2026 § 17]. Par analogie avec le modèle de l'axe 1, VERCLAIR conclut que les informations publiées par CALORÈNE ne sont pas conformes aux ESRS (formulation transposée, sans valeur de citation) [V modèle p. 46 pour l'axe 1 ; S pour la transposition à l'axe 2]. On écarte :
  - l'**avis assorti d'une réserve**, puisque les incidences ne sont pas circonscrites ;
  - l'**impossibilité d'émettre un avis**, puisqu'il n'y a pas de limitation : VERCLAIR a eu accès au registre d'exploitation et a pu établir la part correcte.

**Structure du rapport (0,5 pt).** Le rapport de certification est destiné à l'assemblée. Il comprend :
- une partie introductive (informations couvertes, responsabilités, limites de la mission) ;
- **une partie par axe**, soit deux ici (processus, informations). Chacune expose la nature des vérifications, l'avis et, le cas échéant, les éléments ayant fait l'objet d'une attention particulière ;
- la date et la signature de Mme ROCHE.

Les axes taxonomie et balisage n'appellent pas d'avis [V LD 2026 § 2, § 17].

On valorise la **connectivité** : la part réelle de 80 % reste supérieure au seuil de 70 % de la convention de subvention. L'erreur ne crée donc pas de risque de remboursement dans les comptes, mais elle doit être portée à la connaissance de l'équipe d'audit des comptes [V LD 2026 § 3, § 11 ; S pour l'application].

**Réponses tolérées**
- **Axe 2** : un avis de conformité assorti d'une réserve motivée reçoit les points de la qualification (1 pt) s'il est argumenté avec la table de décision et si la réserve décrit toutes les informations touchées (part renouvelable, émissions, émissions évitées, trajectoire) ; le point des incidences n'est pas accordé. Aucun texte ne fixe le seuil d'importance [F13 § 4.3].
- Le vocabulaire « auditeur de durabilité » au lieu de « vérificateur ».

**Erreurs fréquentes**
- Émettre un avis unique pour l'ensemble de l'état de durabilité au lieu d'un avis par axe.
- Présenter le point (c) comme une réserve ou comme une observation.
- Conclure à l'impossibilité d'émettre un avis alors que VERCLAIR a établi le chiffre correct.
- Donner l'avis sans son motif (`JUR-A02` par analogie avec l'opinion) ; rédaction relâchée (`JUR-F10`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 | Quatre avis, table de décision, observations, éléments d'attention particulière | [V] | F13 § 4.2-4.4 |
| LD 2026, annexe 2, p. 46 | Formulations types de l'axe 1 | [V] | F13 § 4.2 |
| LD 2026 § 7.3 | Vérification de la consultation du CSE | [V] | F13 § 3 |
| Avis de non-conformité sur l'axe 2 | Application de la table de décision | [S, jugement professionnel] | F13 § 4.3 |
