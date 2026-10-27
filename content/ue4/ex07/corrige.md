# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Exercice d'entraînement n° 7 — Dossier 1 (45 points)

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F03 obligation de consolider, périmètre et méthodes (à jour au 22/10/2026) ; F04 retraitements (à jour au 23/10/2026) ; F05 écarts d'acquisition et partage (à jour au 23/10/2026) ; F99 liste noire (à jour au 22/10/2026). Textes non repris dans les fiches, vérifiés sur la source le 27/10/2026 : règlement ANC n° 2020-01 consolidé au 01/01/2026, art. 221-2, 221-3, 222-1 (p. 19), 261-1, 261-3, 261-4 (p. 48), modèles des art. 281-1 et 281-2 (p. 66-67) ; IAS 1 § 10, 15, 25, 54, 56, 81A, 81B, 82, 87 et 106 et IAS 8 § 10 et 11 (règlement (UE) 2023/1803 consolidé au 30/07/2025, texte français, CELEX 02023R1803-20250730, obtenu via Cellar) ; pages institutionnelles de l'IFRS Foundation (IASB, IFRS Interpretations Committee, Conceptual Framework) et de l'EFRAG (Financial reporting). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, impôts différés, partage, 19 écritures, barème).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

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
