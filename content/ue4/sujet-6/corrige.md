# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 6

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22 et le 29/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex13_consolidation_anc_conversion_flux` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.7 | `exercices/ex14_tup_mali_technique` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.8 | `exercices/ex15_audit_paie_impossibilite_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 2 |
| 1.2 Périmètre et méthodes | `2.1.c` Périmètre ; `2.1.d` Conséquences des méthodes | 2 |
| 1.3 Processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 1 |
| 1.4 Amortissements dérogatoires | `2.2.b` Élimination des écritures fiscales | 3 |
| 1.5 Frais de premier établissement | `2.2.c` Homogénéisation, thèmes communs | 3 |
| 1.6 Logiciel de gestion de flotte | `2.2.c` Homogénéisation, thèmes communs | 4 |
| 1.7 a Méthode de conversion | `2.2.e` Conversion des comptes en devises | 1,5 |
| 1.7 b Conversion du bilan et du résultat | `2.2.e` Conversion des comptes en devises | 3,5 |
| 1.7 c Écart de conversion | `2.2.e` Conversion des comptes en devises | 2 |
| 1.8 a Affrètements et compte courant | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.8 b Dividendes d'ÉCLUSANE | `2.2.f` Comptes réciproques et résultats internes ; `2.2.h` Partage (mise en équivalence) | 2 |
| 1.9 a Actifs nets réévalués | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.9 b Coût d'acquisition et écarts d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.9 c Écritures : écarts d'évaluation et frais | `2.2.g` Écarts d'évaluation et d'acquisition | 2 |
| 1.9 d Partage et mise en équivalence | `2.2.h` Partage des capitaux propres | 3 |
| 1.9 e Écritures : titres et mise en équivalence | `2.2.h` Partage des capitaux propres | 2 |
| 1.10 a Résultat consolidé | `2.3.a` Documents de synthèse consolidés | 1,5 |
| 1.10 b Extrait du tableau des flux de trésorerie | `2.3.a` Documents de synthèse consolidés | 3 |
| 1.10 c Place du tableau des flux (ANC, IFRS) | `2.3.a` Documents de synthèse consolidés | 1,5 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires ; `EA` = écart d'acquisition ; `AMO_EA` / `DOT_EA` = amortissements / dotation de l'écart d'acquisition ; `TME` = titres mis en équivalence ; `QP_MEE` = résultat net lié aux entités mises en équivalence ; `ECV` / `ECV_G` = écart de conversion avant partage / part du groupe ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.FLUVEOR` : titres détenus par FLUVÉOR).

---

### 1.1 Obligation d'établir des comptes consolidés et référentiel (2 pts)

**Principe (0,5 pt).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. En l'espèce, FLUVÉOR, société en commandite par actions, donc société commerciale, contrôle exclusivement RHÉNOLOG, BARGELIS et ses autres filiales (voir 1.2) : elle entre dans le champ de l'obligation.

**Exemptions (1 pt).**
- *Société elle-même contrôlée* (L. 233-17, 1°) : l'exemption suppose que FLUVÉOR soit incluse dans les comptes consolidés publiés d'une entité qui la contrôle. Son capital est réparti entre des personnes physiques, deux fonds dont aucun ne dépasse 15 % et l'associé commandité, qui détient 2 % du capital et n'établit pas de comptes consolidés. Quelle que soit l'analyse du pouvoir que la gérance donne au commandité, aucune entité n'inclut FLUVÉOR dans des comptes consolidés : l'exemption est écartée [V L. 233-17 ; F03 § 1.1] (0,5 pt).
- *Ensemble qui n'est pas un « grand groupe »* (L. 233-17, 2°) : un grand groupe dépasse, à la clôture, deux des trois seuils suivants : total du bilan 30 000 000 €, chiffre d'affaires net 60 000 000 €, 250 salariés en moyenne ; les seuils sont réputés franchis à la clôture de **deux exercices consécutifs** [V L. 230-2, 3° ; D. 230-2, 2° et dernier alinéa ; F03 § 1.1]. En l'espèce, les trois seuils sont dépassés au 31/12/2025 (171 M€, 196 M€, 605 salariés) et au 31/12/2026 (238 M€, 212 M€, 640 salariés) : l'ensemble est un grand groupe et l'exemption ne joue pas. Aucune entité ne relève de l'art. L. 123-16-2, ce qui ne servirait de toute façon qu'à refuser l'exemption du 2° (0,5 pt).

**Référentiel (0,5 pt).** Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que pour les sociétés dont les titres sont admis aux négociations sur un marché réglementé d'un État membre [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Les autres sociétés appliquent le règlement ANC n° 2020-01 ou, sur option, les IFRS adoptées [V C. com. L. 233-24 ; F03 § 1.2]. Aucun titre de FLUVÉOR n'étant admis sur un marché, le groupe applique le règlement ANC n° 2020-01 ; il n'a pas exercé l'option pour les IFRS.

---

### 1.2 Périmètre et méthodes (2 pts)

**Tableau (1 pt : RHÉNOLOG 0,25 ; BARGELIS 0,25 ; ÉCLUSANE 0,5)**

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt |
|---|---|---|---|---|
| FLUVÉOR | — | Mère | — | 100 % |
| RHÉNOLOG | 80 % | Exclusif | Intégration globale | 80 % (minoritaires 20 %) |
| BARGELIS | 100 % | Exclusif | Intégration globale | 100 % |
| ÉCLUSANE | 25 % + 15 % = **40 %** | Influence notable | Mise en équivalence | 25 % + 80 % × 15 % = **37 %** (minoritaires de RHÉNOLOG : 3 %) |

**Justification pour ÉCLUSANE (1 pt).**
- Le pourcentage de contrôle additionne les droits de vote détenus par la mère et par les entités qu'elle contrôle exclusivement, sans multiplier [V ANC art. 211-6, p. 14 ; F03 § 4.1]. RHÉNOLOG est contrôlée exclusivement : ses 15 % comptent en totalité (0,25 pt).
- 40 % des droits de vote ne donnent pas la majorité et n'atteignent pas le seuil de présomption de l'art. 211-3 (plus de 40 %, sans autre associé détenant une fraction supérieure) [V art. 211-3, p. 12-13] ; en outre, M. ZIMMER détient 60 % et désigne trois des cinq membres du comité stratégique (0,25 pt).
- Le groupe détient plus de 20 % des droits de vote, siège au comité stratégique avec deux membres et réalise des opérations importantes avec ÉCLUSANE : il exerce une influence notable, d'où la mise en équivalence [V art. 211-5, p. 13 ; art. 221-1, p. 18 ; F03 § 2 et 3] (0,25 pt).
- Le pourcentage d'intérêt fait la somme, sur chaque chaîne de détention, du produit des pourcentages de capital : 25 % en direct et 80 % × 15 % = 12 % par RHÉNOLOG, soit 37 % [S méthode du corrigé du sujet zéro ; F03 § 4.1]. Les titres mis en équivalence représentent les 40 % détenus par les sociétés intégrées ; la part des minoritaires de RHÉNOLOG (20 % × 15 % = 3 %) revient aux intérêts minoritaires (0,25 pt).

---

### 1.3 Processus de consolidation (1 pt)

L'intégration globale comprend l'intégration des comptes après retraitements, la répartition des capitaux propres et du résultat entre le groupe et les intérêts minoritaires, et l'élimination des opérations internes [V ANC art. 221-2, p. 18-19 ; F03 § 3]. La mise en équivalence substitue aux titres la quote-part des capitaux propres retraités [V art. 221-4, p. 19].

| Étape | Contenu | Travaux du dossier |
|---|---|---|
| 1. Cadre et périmètre | Obligation, référentiel, entités consolidées, pourcentages, méthodes | 1.1, 1.2 |
| 2. Comptes individuels retraités et convertis | Élimination des écritures fiscales, homogénéisation selon le manuel, conversion en euros des comptes en devises, évaluation des actifs et passifs identifiables des entités acquises | 1.4 à 1.7 b, 1.9 a et c |
| 3. Cumul des comptes | Cumul à 100 % des comptes de RHÉNOLOG et de BARGELIS ; aucun cumul pour ÉCLUSANE | Réalisé par le service consolidation |
| 4. Élimination des opérations internes | Comptes réciproques, résultats internes, dividendes | 1.8 |
| 5. Élimination des titres, partage et mise en équivalence | Écarts d'acquisition, part du groupe, intérêts minoritaires, écart de conversion, valeur d'équivalence | 1.7 c, 1.9 b, d et e |
| 6. États de synthèse | Bilan, compte de résultat, annexe dont le tableau des flux de trésorerie | 1.10 |

(0,5 pt pour l'enchaînement des étapes ; 0,5 pt pour leur rattachement aux questions.)

---

### 1.4 Amortissements dérogatoires de RHÉNOLOG (3 pts)

**Justification (0,5 pt).** L'incidence des écritures passées pour la seule application des législations fiscales est éliminée ; les amortissements dérogatoires en sont l'exemple type [V ANC art. 272-1, p. 53 ; F04 R1]. Les dotations ayant été déduites fiscalement, leur élimination fait apparaître une différence temporaire imposable : la valeur des immobilisations en consolidation dépasse leur valeur fiscale. D'où un **impôt différé passif** [V art. 272-8, p. 57].

**Tableau des incidences (1 pt)**

| | Ouverture (01/01/2026) | Variation 2026 | Clôture (31/12/2026) |
|---|---:|---:|---:|
| Amortissements dérogatoires (comptes individuels) | 180 000 | + 60 000 – 20 000 = 40 000 | 220 000 |
| Amortissements dérogatoires (comptes consolidés) | 0 | 0 | 0 |
| **Écart (capitaux propres consolidés plus élevés)** | **180 000** | **40 000** | **220 000** |
| Impôt différé passif (25 %) | – 45 000 | – 10 000 | **– 55 000** |
| **Net** | **135 000** (réserves) | **30 000** (résultat) | 165 000 |

(Ouverture et net en réserves : 0,25 pt ; variation, impôt et net en résultat : 0,5 pt ; clôture et impôt différé passif : 0,25 pt.)

**R1 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 145 Amortissements dérogatoires | 220 000 | |
| RSV.RHENOLOG Réserves RHÉNOLOG | | 135 000 |
| RST.RHENOLOG Résultat RHÉNOLOG | | 30 000 |
| IDP Impôt différé passif | | 55 000 |
| *Élimination des amortissements dérogatoires de RHÉNOLOG* | **220 000** | **220 000** |

**R1R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 78725 Reprises sur amortissements dérogatoires | 20 000 | |
| CH_ID Charge d'impôt différé | 10 000 | |
| RES_CR Résultat | 30 000 | |
| 68725 Dotations aux amortissements dérogatoires | | 60 000 |
| *Élimination des amortissements dérogatoires de RHÉNOLOG* | **60 000** | **60 000** |

**Incidence d'ouverture (0,5 pt).** Les 135 000 € nets portent sur des exercices antérieurs à l'entrée de RHÉNOLOG dans le groupe, le 01/01/2026. Ils augmentent l'actif net de RHÉNOLOG à la date d'acquisition (1.9 a) et donc réduisent l'écart d'acquisition : ils ne deviennent pas des réserves consolidées. Seul le résultat de 2026 (+ 30 000 €) est partagé entre le groupe (80 %) et les minoritaires (20 %).

---

### 1.5 Frais de premier établissement de FLUVÉOR (3 pts)

**Justification (0,5 pt).** Le PCG permet d'inscrire les frais de premier établissement à l'actif, la comptabilisation en charges étant la méthode de référence [V PCG art. 212-9, p. 15]. En consolidation, ils sont comptabilisés en charges de l'exercice au cours duquel ils sont engagés [V ANC art. 272-5, p. 54 ; F04 R5], ce que rappelle le manuel du groupe. Fiscalement, FLUVÉOR déduit les frais au rythme de leur amortissement (hypothèse de l'énoncé) : leur valeur fiscale est égale à leur valeur nette comptable, alors que leur valeur en consolidation est nulle. La différence est déductible : **impôt différé actif** [V art. 272-8, p. 57 ; F04 R5].

**Calcul et tableau des incidences (1 pt)**
- Amortissement de 2025 : 160 000 / 5 × 3/12 = 8 000 ; dotation de 2026 : 160 000 / 5 = 32 000.
- Valeur nette comptable : 152 000 au 01/01/2026 ; 120 000 au 31/12/2026.

| | Ouverture (01/01/2026) | Variation 2026 | Clôture (31/12/2026) |
|---|---:|---:|---:|
| Frais d'établissement nets (comptes consolidés) | 0 | 0 | 0 |
| Frais d'établissement nets (comptes individuels) | 152 000 | – 32 000 | 120 000 |
| **Écart (capitaux propres consolidés moins élevés)** | **– 152 000** | **+ 32 000** | **– 120 000** |
| Impôt différé actif (25 %) | + 38 000 | – 8 000 | **+ 30 000** |
| **Net** | **– 114 000** (réserves) | **+ 24 000** (résultat) | – 90 000 |

(Ouverture et net en réserves : 0,25 pt ; variation, impôt et net en résultat : 0,5 pt ; clôture et impôt différé actif : 0,25 pt.)

**R2 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2801 Amortissements des frais d'établissement (8 000 + 32 000) | 40 000 | |
| RSV.FLUVEOR Réserves FLUVÉOR | 114 000 | |
| IDA Impôt différé actif | 30 000 | |
| 2012 Frais de premier établissement | | 160 000 |
| RST.FLUVEOR Résultat FLUVÉOR | | 24 000 |
| *Annulation des frais de premier établissement* | **184 000** | **184 000** |

**R2R (compte de résultat, 0,5 pt)** : débit CH_ID Charge d'impôt différé 8 000 ; débit RES_CR 24 000 ; crédit 68111 Dotations aux amortissements des immobilisations incorporelles et frais d'établissement 32 000.

**Portée de l'incidence d'ouverture (0,5 pt).** FLUVÉOR est la société mère : l'incidence de 2025 (– 114 000 € nets) diminue directement les réserves consolidées du groupe. Le retraitement fait en 2025 n'a été passé que dans les comptes consolidés ; la consolidation repartant chaque année des comptes individuels, il est de nouveau enregistré en 2026, sur les réserves pour la part antérieure.

---

### 1.6 Logiciel de gestion de flotte NAVIFLOT (4 pts)

**Principe (0,25 pt).** En consolidation, les frais de développement remplissant les conditions de l'art. 212-3 du PCG et les solutions informatiques visées aux art. 611-1 à 611-8 sont comptabilisés à l'actif [V ANC art. 272-6, p. 54 ; F04 R7]. Les dépenses de la phase de recherche préalable restent en charges [V PCG art. 212-3, p. 14]. Une solution informatique créée en interne est inscrite à l'actif lorsque l'entité démontre notamment sa capacité à l'utiliser, son utilité si elle est destinée à un usage interne, la disponibilité des ressources nécessaires et sa capacité à évaluer de façon fiable les dépenses attribuables [V PCG art. 611-3, p. 44]. Seuls les coûts directement attribués à la solution et nécessaires à sa production entrent dans son coût [V PCG art. 611-6, p. 45] ; elle est amortie selon les règles générales [V PCG art. 611-8, p. 45]. Le manuel du groupe reprend ces règles.

**Analyse des dépenses (1,5 pt)**

| Dépense | Montant | Traitement | Justification |
|---|---:|---|---|
| Étude préalable (janvier-février) | 40 000 | Charges | Phase préalable : les conditions ne sont réunies qu'au 01/03/2026 (0,25) |
| Salaires et charges sociales des ingénieurs (mars-août) | 300 000 | **Actif** | Coûts directement attribuables à la phase de développement, engagés après la réunion des conditions (décision, budget, faisabilité, utilité, suivi par projet) (0,5 pour les deux lignes) |
| Prestations de programmation (mars-août) | 180 000 | **Actif** | Idem |
| Formation des utilisateurs | 25 000 | Charges | Non nécessaire à la production du logiciel ; exclue par le manuel (0,25) |
| Maintenance après mise en service | 15 000 | Charges | Engagée après la mise en service, ne crée pas d'avantage supplémentaire (0,25) |
| **Coût à l'actif consolidé** | **480 000** | | (0,25) |

**Amortissement 2026 (0,5 pt).** À compter de la mise en service, le 01/09/2026 : 480 000 / 4 × 4/12 = **40 000 €**. Valeur nette au 31/12/2026 : 440 000 €.

**Incidence (0,75 pt).** Toutes les dépenses datent de 2026 : le retraitement n'affecte pas les réserves (0,25). Le résultat consolidé augmente de 480 000 – 40 000 = 440 000 € avant impôt. FLUVÉOR a déduit les dépenses fiscalement en 2026 : la base fiscale du logiciel est nulle, sa valeur en consolidation est de 440 000 €. La différence temporaire est imposable : **impôt différé passif de 110 000 €** [V art. 272-8, p. 57 ; F04 R7]. Incidence nette sur le résultat : **+ 330 000 €** (0,5).

**R3 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Concessions et droits similaires, brevets, licences, solutions informatiques | 480 000 | |
| 2805 Amortissements des solutions informatiques | | 40 000 |
| IDP Impôt différé passif | | 110 000 |
| RST.FLUVEOR Résultat FLUVÉOR | | 330 000 |
| *Activation du logiciel NAVIFLOT* | **480 000** | **480 000** |

**R3R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 68111 Dotations aux amortissements des immobilisations incorporelles | 40 000 | |
| CH_ID Charge d'impôt différé | 110 000 | |
| RES_CR Résultat | 330 000 | |
| 721 Production immobilisée – immobilisations incorporelles | | 480 000 |
| *Activation du logiciel NAVIFLOT* | **480 000** | **480 000** |

---

### 1.7 Conversion des comptes de BARGELIS (7 pts)

#### a. Méthode de conversion (1,5 pt)

**Principe (0,5 pt).** La monnaie de fonctionnement est celle de l'environnement économique principal de l'entité. Une entité étrangère autonome a pour monnaie de fonctionnement sa monnaie locale ; une entité non autonome, celle de l'entité dont elle dépend. Une entité est non autonome lorsque son exploitation fait partie intégrante des activités d'une autre entité, notamment lorsqu'elle a des liens commerciaux ou financiers prépondérants avec l'entité consolidante [V ANC art. 272-15 et commentaires IR3 et IR4, p. 59 ; F04 R13].

**Application (0,5 pt).** BARGELIS n'a qu'un client, FLUVÉOR, qui décide des affrètements et en fixe les prix ; elle est financée par FLUVÉOR et par un emprunt garanti par elle, et lui reverse ses excédents de trésorerie. Ses six salariés n'en assurent que la gestion administrative. Son exploitation fait partie intégrante de celle de FLUVÉOR : BARGELIS est **non autonome** et sa monnaie de fonctionnement est l'**euro**.

**Conséquence (0,5 pt).** Le passage de la monnaie locale à la monnaie de fonctionnement se fait par la **méthode du cours historique** [V art. 272-18, p. 60]. La monnaie de fonctionnement étant l'euro, monnaie de FLUVÉOR, la seconde étape (cours de clôture) n'a pas lieu. Selon cette méthode, les éléments non monétaires, y compris les capitaux propres, sont convertis au cours de leur date d'entrée ; les éléments monétaires, au cours de clôture ; les produits et charges, au cours du jour ou, en pratique, au cours moyen ; les amortissements des actifs convertis au cours historique, au même cours historique que ces actifs [V art. 272-16, p. 59-60 ; F04 R13].

#### b. Bilan et compte de résultat convertis (3,5 pts)

**Bilan au 31/12/2026**

| Poste | CHF | Nature | Cours | Euros |
|---|---:|---|---:|---:|
| Barges (brut) | 1 800 000 | Non monétaire | 1,04 (01/04/2026) | 1 872 000 |
| Amortissements | – 135 000 | Non monétaire | 1,04 | – 140 400 |
| **Barges nettes** | **1 665 000** | | | **1 731 600** (0,5) |
| Compte courant FLUVÉOR | 1 500 000 | Monétaire | 1,08 (clôture) | 1 620 000 |
| Disponibilités | 845 000 | Monétaire | 1,08 | 912 600 |
| **Total de l'actif** | **4 010 000** | | | **4 264 200** (0,25) |
| Capital | 2 000 000 | Capitaux propres | 1,05 (01/01/2026) | 2 100 000 (0,25) |
| Résultat 2026 | 337 500 | | compte de résultat | 360 450 |
| Écart de conversion | — | | solde | – 2 550 |
| Emprunt bancaire | 1 000 000 | Monétaire | 1,08 | 1 080 000 |
| Fournisseurs | 560 000 | Monétaire | 1,08 | 604 800 |
| Impôt sur le bénéfice dû | 112 500 | Monétaire | 1,08 | 121 500 |
| **Total du passif** | **4 010 000** | | | **4 264 200** |

(Éléments monétaires de l'actif et des dettes au cours de clôture : 0,5 pt.)

**Compte de résultat de 2026**

| Poste | CHF | Cours | Euros |
|---|---:|---:|---:|
| Affrètements facturés à FLUVÉOR | 9 000 000 | 1,06 (moyen) | 9 540 000 |
| Affrètements auprès des armateurs | – 7 700 000 | 1,06 | – 8 162 000 |
| Charges de personnel | – 450 000 | 1,06 | – 477 000 |
| Autres charges externes | – 250 000 | 1,06 | – 265 000 |
| Dotations aux amortissements des barges | – 135 000 | **1,04 (historique)** | – 140 400 |
| Charges d'intérêts | – 15 000 | 1,06 | – 15 900 |
| Impôt sur le bénéfice | – 112 500 | 1,06 | – 119 250 |
| **Résultat converti** | **337 500** | | **360 450** |

(Produits et charges au cours moyen : 0,5 pt ; dotation au cours historique des barges : 0,5 pt ; résultat : 0,5 pt ; présentation du bilan converti équilibré par l'écart de conversion : 0,5 pt.)

La dotation suit le cours historique des barges : le bilan (amortissements de 140 400 €) et le compte de résultat (dotation de 140 400 €) restent cohérents.

#### c. Écart de conversion (2 pts)

**Calcul (0,5 pt).** Actif converti – dettes converties – capital – résultat converti = 4 264 200 – 1 806 300 – 2 100 000 – 360 450 = **– 2 550 €** (perte de conversion).

**Origine (0,5 pt).** Avec le cours historique, seuls les éléments monétaires changent de valeur en euros quand le cours varie : l'écart mesure l'effet de change sur la position monétaire nette de BARGELIS au cours de l'exercice. Les CHF 2 000 000 reçus au 01/01/2026 (1,05) valent 1,08 à la clôture (+ 60 000 €). Les CHF 1 800 000 décaissés le 01/04/2026 pour les barges sont sortis de cette position au cours de 1,04, et non au cours de clôture (– 72 000 €). Les flux d'exploitation nets, CHF 472 500 (produits – charges décaissées ou dues), sont convertis au cours moyen de 1,06 et non à 1,08 (+ 9 450 €). Total : 60 000 – 72 000 + 9 450 = – 2 550 €. Ce contrôle n'est pas exigé.

**Comptabilisation (0,25 pt).** Les écarts de conversion constatés sur les éléments du bilan d'ouverture et sur le résultat sont portés en capitaux propres, au poste « Écarts de conversion », pour la part de l'entité consolidante, et en intérêts minoritaires pour la part des tiers [V ANC art. 272-21, p. 61 ; F04 R13]. Le texte ne distingue pas les deux méthodes de conversion, et le manuel du groupe applique la règle à toutes ses entités étrangères. BARGELIS étant détenue à 100 %, la perte de 2 550 € est portée en totalité en capitaux propres consolidés, part du groupe, au poste « Écarts de conversion ». Le résultat consolidé reprend le résultat converti de BARGELIS, 360 450 €.

**V1 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.BARGELIS Capital BARGELIS (CHF 2 000 000 × 1,05) | 2 100 000 | |
| RST.BARGELIS Résultat BARGELIS converti | 360 450 | |
| ECV_G Écarts de conversion – part du groupe | 2 550 | |
| 261.FLUVEOR Titres de participation BARGELIS | | 2 100 000 |
| RST_G Résultat consolidé – part du groupe | | 360 450 |
| ECV.BARGELIS Écart de conversion BARGELIS | | 2 550 |
| *Élimination des titres BARGELIS et partage* | **2 463 000** | **2 463 000** |

Les titres (2 100 000 €) et le capital converti au cours historique (2 100 000 €) sont égaux : BARGELIS ayant été créée par FLUVÉOR, il n'y a pas d'écart d'acquisition.

**Méthode du cours de clôture (0,25 pt).** Les barges seraient converties au cours de clôture (1 798 200 € nets au lieu de 1 731 600 €) et toutes les charges, dotation comprise, au cours moyen (résultat de 357 750 €) : l'écart de conversion porterait sur l'ensemble de l'actif net et deviendrait un gain de 66 750 €, également porté en capitaux propres.

---

### 1.8 Opérations internes (4 pts)

#### a. Affrètements et compte courant (2 pts)

**Principe (0,5 pt).** Entre entités intégrées globalement, les créances et dettes réciproques ainsi que les produits et charges réciproques sont éliminés en totalité, sans incidence sur le résultat [V ANC art. 251-1, p. 45 ; F04 R14].

**Vérification en euros (0,5 pt).**
- Affrètements : chez BARGELIS, CHF 9 000 000 × 1,06 = 9 540 000 € de produits après conversion ; chez FLUVÉOR, 9 540 000 € de charges, enregistrés aux cours des dates de facture. Le cours moyen étant représentatif de ces cours, les deux montants sont égaux.
- Compte courant : créance monétaire de BARGELIS convertie au cours de clôture (CHF 1 500 000 × 1,08 = 1 620 000 €) ; dette de FLUVÉOR enregistrée le 31/12/2026, au cours du jour qui est aussi le cours de clôture : 1 620 000 €. Les deux montants s'éliminent sans écart. Si FLUVÉOR avait enregistré l'avance à une date antérieure, sa dette en francs suisses aurait été convertie au cours de clôture dans ses comptes individuels, l'écart étant inscrit dans un compte d'écart de conversion (476 ou 477) [V PCG art. 420-5, p. 39 ; F04 R12] : les deux montants réciproques seraient restés égaux.

**I1 (compte de résultat, 0,5 pt)** : débit 706 Prestations de services 9 540 000 ; crédit 611 Sous-traitance générale 9 540 000.
**I2 (bilan, 0,5 pt)** : débit 451 Groupe (dette de FLUVÉOR) 1 620 000 ; crédit 451 Groupe (compte courant à l'actif de BARGELIS) 1 620 000.

#### b. Dividendes d'ÉCLUSANE (2 pts)

**Principe (0,5 pt).** Les dividendes reçus des entités mises en équivalence sont éliminés du compte de résultat de l'entité qui détient les titres et portés en augmentation des réserves consolidées [V ANC art. 262-3, p. 49 ; F05 § 4]. Le groupe ne doit pas compter deux fois le même bénéfice : la quote-part de résultat d'ÉCLUSANE est déjà constatée par la mise en équivalence.

**Montants (0,5 pt).** FLUVÉOR : 25 % × 200 000 = 50 000 € ; RHÉNOLOG : 15 % × 200 000 = 30 000 €. Le dividende de RHÉNOLOG est reclassé dans ses propres réserves : il sera partagé à 80 % / 20 % avec ses capitaux propres (1.9 d).

**I3 (bilan, 0,5 pt)** : débit RST.FLUVEOR 50 000 ; débit RST.RHENOLOG 30 000 ; crédit RSV.FLUVEOR 50 000 ; crédit RSV.RHENOLOG 30 000.
**I3R (compte de résultat, 0,25 pt)** : débit 7611 Revenus des titres de participation 80 000 ; crédit RES_CR 80 000.

**Lien avec la valeur d'équivalence (0,25 pt).** La distribution a réduit les capitaux propres d'ÉCLUSANE de 200 000 € : la valeur d'équivalence baisse de 40 % × 200 000 = 80 000 €, et les réserves issues de la mise en équivalence baissent d'autant (– 74 000 € pour le groupe, – 6 000 € pour les minoritaires, 1.9 d). Le reclassement des 80 000 € en réserves compense exactement cette baisse.

---

### 1.9 Écarts de première consolidation, partage et mise en équivalence (13 pts)

#### a. Actifs nets réévalués au 01/01/2026 (3 pts)

La valeur d'entrée des actifs et passifs identifiables est comparée à leur valeur comptable dans le bilan retraité selon les méthodes du groupe ; les écarts d'évaluation donnent lieu à impôt différé, dont la contrepartie ajuste l'écart d'acquisition [V ANC art. 231-9, p. 22 ; art. 232-1, p. 24 ; art. 272-13, p. 59 ; F05 § 1.2]. Les mêmes règles valent pour une entité mise en équivalence [V art. 262-2, p. 49].

**ÉCLUSANE (1 pt)**

| Élément | Montant |
|---|---:|
| Capitaux propres individuels au 01/01/2026 | 4 000 000 |
| Écart d'évaluation sur terrain (650 000 – 250 000) | + 400 000 |
| Impôt différé passif (25 %) | – 100 000 |
| **Actif net réévalué d'ÉCLUSANE** | **4 300 000** |

**RHÉNOLOG (2 pts)**

| Élément | Montant |
|---|---:|
| Capitaux propres individuels au 01/01/2026 | 8 000 000 |
| – Provisions réglementées (amortissements dérogatoires) | – 180 000 |
| + Amortissements dérogatoires repris, nets d'impôt (180 000 × 75 %, 1.4) | + 135 000 (0,5 pour les deux lignes) |
| + Écart d'évaluation sur terrain (1 400 000 – 600 000) | + 800 000 |
| + Écart d'évaluation sur grue (1 700 000 – 1 100 000) | + 600 000 |
| – Impôt différé passif ((800 000 + 600 000) × 25 %) | – 350 000 (0,75 pour les trois lignes) |
| + Écart sur titres ÉCLUSANE (645 000 – 300 000), sans impôt différé | + 345 000 (0,5) |
| **Actif net réévalué de RHÉNOLOG** | **9 350 000** (0,25) |

Les titres ÉCLUSANE de RHÉNOLOG sont évalués à 15 % de l'actif net réévalué d'ÉCLUSANE (15 % × 4 300 000 = 645 000) : la tranche détenue par RHÉNOLOG n'a donc pas d'écart d'acquisition propre. La différence entre leur valeur fiscale et leur valeur en consolidation ne donne pas lieu à impôt différé, comme le prévoit le manuel ; c'est aussi la règle de l'ANC, sauf impôt non récupérable sur des distributions décidées ou probables [V art. 272-10, dernier alinéa, et 272-11, p. 58].

#### b. Coût d'acquisition et écarts d'acquisition (3 pts)

**Frais d'acquisition (0,5 pt).** Dans les comptes individuels, les frais d'acquisition des titres peuvent être incorporés au coût des titres, méthode de référence, ou comptabilisés en charges [V PCG art. 121-5, p. 10-11 ; F05 § 1.1]. FLUVÉOR les a passés en charges et déduits fiscalement. En consolidation, le coût d'acquisition comprend les coûts directement imputables, nets de l'économie d'impôt [V ANC art. 231-2 et 231-3, p. 20 ; F05 § 1.1] : ils sont réintégrés pour 160 000 × 75 % = 120 000 €.

**Coût d'acquisition des titres RHÉNOLOG (0,5 pt)** : 9 600 000 + 120 000 = **9 720 000 €**.

**Écart d'acquisition de RHÉNOLOG (0,75 pt).** Coût d'acquisition – part de l'acquéreur dans l'actif net réévalué [V art. 231-9, p. 22] : 9 720 000 – 80 % × 9 350 000 = 9 720 000 – 7 480 000 = **2 240 000 €**. Positif, il est inscrit en immobilisations incorporelles [V art. 231-11, p. 23]. Aucun impôt différé n'est calculé sur l'écart d'acquisition [V art. 272-10, p. 58].

**Écart d'acquisition d'ÉCLUSANE (0,5 pt).** Tranche acquise par FLUVÉOR : 1 300 000 – 25 % × 4 300 000 = 1 300 000 – 1 075 000 = **225 000 €**. Il est présenté selon les mêmes modalités que les écarts d'acquisition des entités intégrées, donc en immobilisations incorporelles, distinct des titres mis en équivalence [V art. 262-2, p. 49 ; F05 § 4]. En IFRS, il serait compris dans la valeur comptable de la participation [V IAS 28 § 32 ; F05 § 4].

**Dotations 2026 (0,75 pt).** Le manuel retient pour les deux écarts une durée d'utilisation limitée de 10 ans, d'où un amortissement linéaire [V art. 231-11, p. 23 ; F05 § 1.3] :
- RHÉNOLOG : 2 240 000 / 10 = **224 000 €**, à la charge du seul groupe, sur la ligne des dotations aux amortissements des écarts d'acquisition, au sein du résultat d'exploitation [V IR3 sous art. 231-12, p. 24 ; modèle de l'art. 281-2, p. 67] ;
- ÉCLUSANE : 225 000 / 10 = **22 500 €**, sur la ligne « Résultat net lié aux entités mises en équivalence » [V art. 262-3, p. 49].

#### c. Écritures : écarts d'évaluation et frais d'acquisition (2 pts)

**Écarts d'évaluation de RHÉNOLOG au 31/12/2026.** Antérieurs au 01/01/2026, ils sont repris en réserves ; le supplément d'amortissement de la grue de 2026 (600 000 / 10 = 60 000 €) pèse sur le résultat.

| | Réserves (01/01/2026) | Résultat 2026 | Bilan au 31/12/2026 |
|---|---:|---:|---:|
| Terrain | + 800 000 | — | 211 : + 800 000 |
| Grue | + 600 000 | – 60 000 | 2154 : + 600 000 ; 2815 : – 60 000 |
| Impôt différé (25 %) | – 350 000 | + 15 000 | IDP : 335 000 |
| Titres ÉCLUSANE | + 345 000 | — | 261 : + 345 000 |
| **Net** | **+ 1 395 000** | **– 45 000** | |

**P1 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 211 Terrains | 800 000 | |
| 2154 Matériels industriels (grue) | 600 000 | |
| 261.RHENOLOG Titres de participation ÉCLUSANE | 345 000 | |
| RST.RHENOLOG Résultat RHÉNOLOG (60 000 × 75 %) | 45 000 | |
| 2815 Amortissements des installations, matériel et outillage industriels | | 60 000 |
| IDP Impôt différé passif ((800 000 + 540 000) × 25 %) | | 335 000 |
| RSV.RHENOLOG Réserves RHÉNOLOG (1 400 000 × 75 % + 345 000) | | 1 395 000 |
| *Écarts d'évaluation de RHÉNOLOG* | **1 790 000** | **1 790 000** |

**P1R (compte de résultat, 0,25 pt)** : débit 68112 Dotations aux amortissements des immobilisations corporelles 60 000 ; crédit CH_ID Produit d'impôt différé 15 000 ; crédit RES_CR 45 000.

**Frais d'acquisition.** FLUVÉOR a passé 160 000 € en charges en 2026 et en a tiré une économie d'impôt de 40 000 €. En consolidation, les titres augmentent de 120 000 € et le résultat de FLUVÉOR aussi.
**P2 (bilan, 0,5 pt)** : débit 261.FLUVEOR Titres de participation RHÉNOLOG 120 000 ; crédit RST.FLUVEOR 120 000.
**P2R (compte de résultat, 0,5 pt)** : débit 695 Impôts sur les bénéfices 40 000 ; débit RES_CR 120 000 ; crédit 6226 Honoraires 160 000.

#### d. Partage de RHÉNOLOG et mise en équivalence d'ÉCLUSANE au 31/12/2026 (3 pts)

**RHÉNOLOG : capitaux propres retraités (0,5 pt)**

| | Capital et réserves | Résultat 2026 |
|---|---:|---:|
| Comptes individuels (hors provisions réglementées) | 3 000 000 + 4 820 000 = 7 820 000 | 1 000 000 |
| Amortissements dérogatoires (R1) | + 135 000 | + 30 000 |
| Écarts d'évaluation nets et titres ÉCLUSANE (P1) | + 1 395 000 | – 45 000 |
| Dividendes d'ÉCLUSANE (I3) | + 30 000 | – 30 000 |
| **Retraité** | **9 380 000** | **955 000** |

Contrôle : actif net réévalué du 01/01/2026 (9 350 000) + dividendes reclassés (30 000) = 9 380 000, RHÉNOLOG n'ayant rien distribué en 2026.

**RHÉNOLOG : partage (1 pt)**

| | Groupe (80 %) | Minoritaires (20 %) |
|---|---:|---:|
| Capital et réserves retraités (9 380 000) | 7 504 000 | 1 876 000 |
| – Titres RHÉNOLOG (9 720 000) | – 9 720 000 | |
| + Écart d'acquisition | + 2 240 000 | |
| **Réserves** | **24 000** | **1 876 000** |
| **Résultat** (955 000) | **764 000** | **191 000** |

Les 24 000 € de réserves du groupe correspondent à 80 % des dividendes d'ÉCLUSANE reclassés ; sans eux, les réserves consolidées de RHÉNOLOG seraient nulles, l'acquisition datant du 01/01/2026. Les minoritaires sont évalués sur l'actif net réévalué, sans écart d'acquisition [V art. 232-1, p. 24 ; F05 § 1.3].

**ÉCLUSANE : tableau de mise en équivalence (1,5 pt)**

| | Montant |
|---|---:|
| Capitaux propres individuels au 31/12/2026 | 4 300 000 |
| + Écart d'évaluation sur terrain, net d'impôt | + 300 000 |
| **Capitaux propres retraités** | **4 600 000** (dont résultat 500 000) |
| **Titres mis en équivalence (40 %)** | **1 840 000** (0,5) |

| Répartition | Groupe (37 %) | Minoritaires de RHÉNOLOG (3 %) |
|---|---:|---:|
| Quote-part des capitaux propres retraités hors résultat (4 100 000) | 1 517 000 | 123 000 |
| – Titres éliminés : FLUVÉOR (1 300 000 – 225 000 = 1 075 000) ; RHÉNOLOG (645 000, réparti 80 % / 20 %) | – 1 075 000 – 516 000 = – 1 591 000 | – 129 000 |
| **Réserves** | **– 74 000** | **– 6 000** |
| **Résultat** (500 000) | **185 000** | **15 000** |

(Répartition et titres éliminés : 0,75 pt ; contrôle ci-dessous : 0,25 pt.)

Contrôle : les réserves négatives (– 74 000 = – 50 000 – 80 % × 30 000 ; – 6 000 = – 20 % × 30 000) sont les quotes-parts du dividende de 2026, prélevé sur des bénéfices antérieurs à l'entrée d'ÉCLUSANE dans le périmètre. Le reclassement des dividendes en réserves (I3) les compense : les réserves consolidées issues d'ÉCLUSANE sont nulles, l'acquisition datant du 01/01/2026. Les écarts d'évaluation entrent dans la valeur d'équivalence, l'écart d'acquisition en est présenté à part [V art. 262-2 et 262-3, p. 49].

#### e. Écritures d'élimination, de mise en équivalence et d'amortissement (2 pts)

**P3 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.RHENOLOG Capital RHÉNOLOG | 3 000 000 | |
| RSV.RHENOLOG Réserves RHÉNOLOG retraitées (9 380 000 – 3 000 000) | 6 380 000 | |
| RST.RHENOLOG Résultat RHÉNOLOG retraité | 955 000 | |
| EA Écart d'acquisition | 2 240 000 | |
| 261.FLUVEOR Titres de participation RHÉNOLOG | | 9 720 000 |
| RSV_G Réserves consolidées – part du groupe | | 24 000 |
| RST_G Résultat consolidé – part du groupe | | 764 000 |
| RSV_M Intérêts minoritaires – capital et réserves | | 1 876 000 |
| RST_M Intérêts minoritaires – résultat | | 191 000 |
| *Élimination des titres RHÉNOLOG et partage* | **12 575 000** | **12 575 000** |

**P4 et P5 (bilan, 0,75 pt)**
- P4 : débit EA Écart d'acquisition 225 000 ; crédit 261.FLUVEOR Titres ÉCLUSANE 225 000 (reclassement de l'écart d'acquisition).
- P5 :

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence | 1 840 000 | |
| RSV_G Réserves consolidées – part du groupe | 74 000 | |
| RSV_M Intérêts minoritaires – réserves | 6 000 | |
| 261.FLUVEOR Titres ÉCLUSANE détenus par FLUVÉOR | | 1 075 000 |
| 261.RHENOLOG Titres ÉCLUSANE détenus par RHÉNOLOG | | 645 000 |
| RST_G Résultat consolidé – part du groupe | | 185 000 |
| RST_M Intérêts minoritaires – résultat | | 15 000 |
| *Mise en équivalence des titres ÉCLUSANE* | **1 920 000** | **1 920 000** |

**P5R (compte de résultat, 0,25 pt)** : débit RES_CR 200 000 ; crédit QP_MEE Résultat net lié aux entités mises en équivalence 200 000 (40 % × 500 000).

**P6 et P6R (0,25 pt)**
- P6 (bilan) : débit RST_G 246 500 ; crédit AMO_EA Amortissements des écarts d'acquisition 246 500 (224 000 + 22 500).
- P6R (compte de résultat) : débit DOT_EA Dotations aux amortissements des écarts d'acquisition 224 000 ; débit QP_MEE Résultat net lié aux entités mises en équivalence 22 500 ; crédit RES_CR 246 500.

---

### 1.10 Tableau des flux de trésorerie (6 pts)

#### a. Résultat consolidé de 2026 (1,5 pt)

| Élément | Groupe | Minoritaires |
|---|---:|---:|
| FLUVÉOR et autres filiales, avant les écritures du dossier | 6 400 000 | |
| Frais de premier établissement (R2) | + 24 000 | |
| Logiciel NAVIFLOT (R3) | + 330 000 | |
| Frais d'acquisition des titres RHÉNOLOG (P2) | + 120 000 | |
| Dividendes d'ÉCLUSANE reçus par FLUVÉOR (I3) | – 50 000 | |
| RHÉNOLOG (P3) | + 764 000 | 191 000 |
| BARGELIS (V1) | + 360 450 | |
| Amortissement de l'écart d'acquisition de RHÉNOLOG (P6) | – 224 000 | |
| ÉCLUSANE : quote-part de résultat (P5) | + 185 000 | 15 000 |
| ÉCLUSANE : amortissement de l'écart d'acquisition (P6) | – 22 500 | |
| **Total** | **7 886 950** (0,75) | **206 000** (0,25) |

- **Résultat net de l'ensemble consolidé** : 7 886 950 + 206 000 = **8 092 950 €** (0,25).
- **Résultat net des entités intégrées** : 8 092 950 – résultat net lié aux entités mises en équivalence (200 000 – 22 500 = 177 500) = **7 915 450 €** (0,25).

#### b. Extrait du tableau des flux de trésorerie consolidé de 2026 (3 pts)

Modèle établi à partir du résultat net des entités intégrées [V ANC art. 282-43, p. 92 ; F14 § 1.5].

| Ligne du modèle | Calcul | Montant |
|---|---|---:|
| **Résultat net des entités intégrées** | 1.10 a | **7 915 450** (0,25) |
| Dotations aux amortissements, dépréciations et provisions nettes de reprises | 9 890 000 – 40 000 (dérogatoires éliminés) – 32 000 (frais d'établissement annulés) + 40 000 (logiciel) + 60 000 (grue) + 224 000 (écart d'acquisition de RHÉNOLOG) | **10 142 000** (1) |
| Variation des impôts différés (charge nette) | 10 000 (R1) + 8 000 (R2) + 110 000 (R3) – 15 000 (P1) | **113 000** (0,5) |
| Plus-values de cession, nettes d'impôt | aucune cession | 0 |
| **Marge brute d'autofinancement des entités intégrées** | | **18 170 450** (0,25) |
| Dividendes reçus des entités mises en équivalence | 50 000 + 30 000 | **80 000** (0,5) |
| *Variation du besoin en fonds de roulement lié à l'activité* | *non demandée* | |
| **Investissement** – incidence de l'acquisition de RHÉNOLOG | – (9 600 000 + 120 000 – 450 000) | **– 9 270 000** (0,5) |

Justifications :
- Le modèle part du résultat net des **entités intégrées** : le résultat lié aux entités mises en équivalence, qui n'est pas encaissé, n'y figure pas. Seuls les dividendes effectivement reçus d'ÉCLUSANE sont des flux de trésorerie, présentés sur leur ligne propre ; ils avaient été éliminés du résultat (1.8 b).
- Les dotations comprennent celles des écarts d'acquisition des entités intégrées (note 1 du modèle) ; celle de l'écart d'acquisition d'ÉCLUSANE est déjà exclue avec le résultat lié aux entités mises en équivalence. Les amortissements dérogatoires et la dotation des frais de premier établissement, éliminés en consolidation, ne sont plus des charges du résultat consolidé : ils sont retirés du cumul des comptes individuels.
- Les impôts différés n'entraînent aucun décaissement : leur charge nette est ajoutée au résultat.
- L'acquisition de RHÉNOLOG figure dans les flux d'investissement pour le prix d'achat diminué de la trésorerie acquise ; la note 3 du modèle impose ce calcul. Selon la convention du groupe, les frais d'acquisition s'y ajoutent nets de l'économie d'impôt (120 000 €), comme dans le coût d'acquisition consolidé. La charge d'impôt de 40 000 € reclassée en consolidation (1.9 c) n'est pas décaissée : la présenter en investissement, nette, évite de la compter deux fois.
- La création de BARGELIS (souscription du capital par FLUVÉOR) et le compte courant sont des flux internes au groupe, sans incidence sur le tableau consolidé. L'acquisition des titres ÉCLUSANE (1 300 000 €) est un flux d'investissement, présenté sur une autre ligne.

#### c. Place du tableau des flux de trésorerie (1,5 pt)

- **Règlement ANC** : les états de synthèse consolidés sont le bilan et le compte de résultat ; avec l'annexe, ils forment un tout indissociable [V art. 111-4, p. 8 ; F14 § 1.1]. Le tableau des flux de trésorerie figure **dans l'annexe** (art. 282-41 à 282-44), avec le choix entre la méthode directe et la méthode indirecte et entre deux modèles, à partir du résultat net ou du résultat d'exploitation des entités intégrées [V art. 282-41 à 282-44, p. 90-93 ; F14 § 1.5] (0,5 pt).
- **IFRS (IAS 1 pour l'exercice 2026)** : l'état des flux de trésorerie est l'un des **états financiers** du jeu complet, avec l'état de la situation financière, l'état du résultat net et des autres éléments du résultat global, l'état des variations des capitaux propres et les notes [V IAS 1 § 10 ; F14 § 2.1]. Il est établi selon IAS 7 [F14 § 3] (0,5 pt).
- **Différences de présentation (0,5 pt ; deux différences suffisent)** : en IFRS, la méthode indirecte part du résultat, ajusté notamment des bénéfices non distribués des entreprises associées [V IAS 7 § 20] ; les intérêts et dividendes reçus ou versés suivent un classement choisi et permanent (activité, investissement ou financement) [V IAS 7 § 31-34] ; les acquisitions de filiales sont présentées en investissement, nettes de la trésorerie acquise [V IAS 7 § 39 et 42] ; la trésorerie peut inclure les découverts remboursables à vue [V IAS 7 § 8 ; F14 § 3 et 4].

---

### Réponses tolérées
- **1.1** : exemption du 1° écartée au seul motif qu'aucune société ne contrôle FLUVÉOR, si l'absence de comptes consolidés incluant FLUVÉOR est relevée.
- **1.2** : pourcentage d'intérêt d'ÉCLUSANE de 37 % sans mention des 3 % des minoritaires de RHÉNOLOG, si la méthode est justifiée.
- **1.4 et 1.5** : écritures de bilan et de compte de résultat regroupées si les réserves et le résultat sont distingués ; amortissements dérogatoires annulés par le compte 68725 pour leur montant net (40 000 €).
- **1.6** : activation au crédit des comptes de charges d'origine (641, 645 et 604) au lieu du compte 721 ; logiciel inscrit au compte 203 Frais de développement, avec le compte 2803.
- **1.7 b** : bilan converti présenté sans le détail brut / amortissements des barges, si la valeur nette (1 731 600 €) est juste.
- **1.7 c** : écart expliqué par une phrase sur la position monétaire nette, sans le calcul de contrôle.
- **1.8 a** : compte 4551 ou 455 pour le compte courant, si les deux montants éliminés sont égaux.
- **1.9 a** : actif net de RHÉNOLOG présenté en deux temps (actif net hors titres ÉCLUSANE, puis remplacement des titres par 15 % de l'actif net réévalué d'ÉCLUSANE).
- **1.9 c** : frais d'acquisition incorporés par une écriture de bilan seule (P2), ou économie d'impôt annulée par une ligne « impôt sur les résultats » au lieu du compte 695.
- **1.9 d et e** : titres mis en équivalence présentés pour la seule part du groupe (37 % × 4 600 000 = 1 702 000 €), si la part des minoritaires de RHÉNOLOG (138 000 €) est portée en intérêts minoritaires ; écriture de mise en équivalence passée en deux temps, titres de FLUVÉOR puis titres de RHÉNOLOG ; écart d'acquisition d'ÉCLUSANE laissé dans les titres mis en équivalence (2 042 500 € après amortissement), si sa dotation figure dans le résultat lié aux entités mises en équivalence (présentation proche des IFRS ; 0,25 pt de présentation perdu).
- **1.10 b** : incidence de l'acquisition calculée avec les frais bruts (– 9 310 000 €), si la charge d'impôt de 40 000 € est ajoutée parmi les éliminations des charges sans incidence sur la trésorerie (MBA de 18 210 450 €).
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (le jury valorise la logique du candidat, `JUR-F08`).

### Erreurs fréquentes
- **Obligation de consolider** : un seul exercice examiné, ou seuils périmés (F99) ; exemption du 1° retenue au motif que le commandité dirige FLUVÉOR.
- **Périmètre** : contrôle d'ÉCLUSANE limité à 25 % (titres de RHÉNOLOG oubliés) ou calculé à 37 % (pourcentages multipliés) ; contrôle exclusif retenu à 40 % alors qu'un autre associé détient 60 %.
- **Amortissements dérogatoires** : incidence d'ouverture portée en réserves consolidées du groupe alors qu'elle est antérieure à l'acquisition ; impôt différé oublié ou inversé (`JUR-G04`, `JUR-G06`) ; tableau « comptes individuels / comptes consolidés » non présenté (`JUR-F05`).
- **Frais d'établissement** : dotation de 2026 laissée en charges, ou impôt différé actif oublié alors que l'énoncé fixe la règle fiscale (`JUR-F07`).
- **Logiciel** : étude préalable, formation ou maintenance activées ; amortissement calculé sur l'année entière (120 000 €) au lieu de 4 mois ; impôt différé passif oublié.
- **Conversion** : barges ou capital convertis au cours de clôture ; dotation convertie au cours moyen, ce qui déséquilibre le bilan converti ; écart de conversion porté en résultat alors que le manuel le place en capitaux propres.
- **Opérations internes** : compte courant éliminé pour son montant en CHF ou au cours historique ; dividendes d'ÉCLUSANE éliminés contre les titres mis en équivalence sans reclassement en réserves, ou laissés en résultat.
- **Coût d'acquisition** : frais d'acquisition omis ou retenus pour leur montant brut (`JUR-G02`).
- **Mise en équivalence** : écart d'évaluation du terrain d'ÉCLUSANE ou écart d'acquisition oublié dans le tableau de mise en équivalence (`JUR-G03`) ; titres de RHÉNOLOG éliminés à leur coût (300 000 €) au lieu de leur valeur d'entrée ; dotation de l'écart d'acquisition d'ÉCLUSANE portée avec celle des entités intégrées.
- **Partage** : méthode de passage aux comptes consolidés mal maîtrisée (`JUR-G01`, `JUR-G04`) ; écritures non équilibrées (`JUR-F04`).
- **Tableau des flux** : quote-part de résultat d'ÉCLUSANE conservée dans le résultat de départ ; dotations reprises sans les retraitements de consolidation ; acquisition de RHÉNOLOG présentée sans déduire la trésorerie acquise ; tableau présenté comme un état de synthèse en ANC.

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, différences avec la fusion, référentiel et date | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 3 |
| 2.2 Régime fiscal et conséquences | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 3 |
| 2.3 Valeur de transmission, actif net, mali | `1.2.c` Déterminer le mode de valorisation des apports ; `1.2.e` Calculer et analyser le boni ou mali de fusion | 4 |
| 2.4 Décomposition et affectation du mali | `1.2.e` Calculer et analyser le boni ou mali de fusion ; `1.3.b` Adapter les écritures aux détentions préalables | 5 |
| 2.5 Écritures au 1er mars 2027 | `1.3.a` Écritures de base ; `1.3.b` Détentions préalables (annulation des titres, mali) ; `1.3.c` Écritures complémentaires (amortissements dérogatoires, opérations réciproques, frais) | 6 |
| 2.6 Suivi du mali technique en 2027 | `1.3.b` Adapter les écritures aux détentions préalables (suivi du mali technique à la clôture de l'année de l'opération) | 2,5 |
| 2.7 Capitaux propres et note à la présidente | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 1,5 |
| **Total** | | **25** |

---

### 2.1 Qualification, différences avec la fusion, référentiel et date (3 pts)

**Qualification et modalités (1 pt).** ARGANEAU détient toutes les actions de TOUALYS. Sa décision de dissoudre TOUALYS sans liquidation entraîne la **transmission universelle du patrimoine** (TUP) de TOUALYS à son associée unique, ou **confusion de patrimoine** [V C. civ. art. 1844-5 ; PCG art. 710-2, F01 § 1 et F02 § 1] :
- tous les actifs et toutes les dettes de TOUALYS passent à ARGANEAU, y compris l'emprunt bancaire, les engagements de retraite et les dettes envers ARGANEAU elle-même ;
- la transmission n'a lieu qu'à l'issue du **délai d'opposition des créanciers** (30 jours), ici expiré le 28 février 2027 sans opposition [V C. civ. art. 1844-5, F02 § 1] ;
- TOUALYS disparaît. ARGANEAU annule les titres TOUALYS qu'elle détenait ; elle n'émet aucune action et n'augmente pas son capital ;
- l'opération suppose un associé unique personne morale : elle est exclue lorsque l'associé unique est une personne physique [V C. civ. art. 1844-5, F02 § 1].

**Différence avec une fusion-absorption de TOUALYS par ARGANEAU (0,75 pt).** Une fusion-absorption d'une filiale détenue en totalité (fusion dite simplifiée) aboutirait au même résultat économique : TOUALYS disparaîtrait et ARGANEAU n'émettrait aucune action, puisqu'elle ne peut pas recevoir ses propres titres en échange des actions TOUALYS qu'elle détient [V C. com. L. 236-3 II, F01 § 5.1]. Mais c'est une fusion : elle repose sur un projet de fusion arrêté par les deux sociétés et peut prévoir une date d'effet antérieure à sa réalisation [V C. com. L. 236-4, F02 § 5]. La TUP résulte de la seule décision de l'associée unique. Elle ne comporte ni traité ni date d'effet conventionnelle : elle produit ses effets à l'expiration du délai d'opposition [V PCG art. 760-3, F01 § 2.4]. Fiscalement, les deux opérations sont des fusions (voir 2.2).

**Différence avec une fusion entre sociétés sans lien en capital (0,5 pt).** Dans une fusion classique, l'absorbante rémunère les apports par des actions remises aux associés de l'absorbée. Il faut donc calculer une parité d'échange, une augmentation de capital et une prime de fusion, et éventuellement une soulte. Les sociétés étant sous contrôle distinct, les apports seraient évalués à la valeur réelle si la fusion est à l'endroit [V PCG art. 743-1, F01 § 2.3]. Aucun boni ni mali n'apparaît, faute de titres détenus par l'absorbante. Dans la TUP, il n'y a ni échange de titres ni prime ; la seule différence à analyser est l'écart entre l'actif net reçu et la valeur des titres annulés.

**Référentiel et date d'enregistrement (0,75 pt)**
- Les confusions de patrimoine entrent dans le champ du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui leur consacre un chapitre particulier : patrimoine toujours transmis à la valeur comptable, boni et mali traités selon les règles générales [V PCG art. 710-1, 760-1 et 760-2, F01 § 1 et § 2.4] (0,25 pt).
- Le code civil ne prévoit pas d'effet antérieur à la transmission : les dispositions du PCG sur la date d'effet et la période qui la suit ne s'appliquent pas. Les écritures sont passées chez ARGANEAU **à l'issue du délai d'opposition**, soit le **1er mars 2027** [V PCG art. 760-3, F01 § 2.4] (0,5 pt).

---

### 2.2 Régime fiscal et conséquences (3 pts)

**Régime applicable (0,75 pt).** ARGANEAU et TOUALYS sont deux sociétés passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1]. La TUP est une **fusion au sens de l'art. 210-0 A** du CGI : la dissolution entraîne la transmission universelle du patrimoine, sans échange des titres détenus par la société qui reçoit le patrimoine [V CGI art. 210-0 A ; BOI-IS-FUS-10-20-10 § 30 à 60, F02 § 1]. Elle relève donc du **régime de faveur de l'art. 210 A**, qui s'applique sauf option pour le droit commun. ARGANEAU n'exerçant pas cette option, le régime de faveur s'applique [V BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1].

**Résultat de la dernière période et plus-values latentes (0,75 pt)**
- *Résultat du 1er janvier au 28 février 2027.* Il est imposé immédiatement au nom de TOUALYS, quel que soit le régime ; une déclaration spéciale de résultat est souscrite [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2]. La période étant déficitaire (perte comptable de 8 000 €), son déficit fiscal s'ajoute au déficit reportable (compris dans les 160 000 €).
- *Plus-values latentes.* Les plus-values latentes de TOUALYS (pousseurs, barges, fonds commercial) ne sont pas imposées chez TOUALYS [V CGI art. 210 A-1, F02 § 2]. Le patrimoine étant transmis à la valeur comptable (voir 2.3), aucune plus-value n'est dégagée et il n'y a rien à réintégrer : ARGANEAU reprend les valeurs fiscales de TOUALYS. Ses amortissements futurs et ses plus-values de cession seront calculés d'après ces valeurs [V CGI art. 210 A-3-c à e, F02 § 2 et § 4]. Exemple : la cession des barges anciennes, de valeur fiscale nulle, dégagera en 2027 une plus-value imposable de 120 000 € (voir 2.6).

**Amortissements dérogatoires (0,5 pt).** Sous le régime de faveur, la reprise des amortissements dérogatoires (120 000 €) n'est pas imposée chez TOUALYS à condition qu'ARGANEAU les **reconstitue** à son bilan et les réintègre ensuite dans les mêmes conditions que TOUALYS, au rythme de l'amortissement des pousseurs [V BOI-IS-FUS-30-20 § 10, F02 § 2]. D'où l'écriture T3 (voir 2.5). Sous le droit commun, l'opération serait traitée comme une cessation d'entreprise de TOUALYS : ses plus-values et ses amortissements dérogatoires seraient imposés immédiatement [V BOI-IS-FUS-10-10-10 § 1 ; BOI-IS-FUS-10-10-20 § 10 et 20, F02 § 2].

**Déficit reportable de TOUALYS (1 pt)**
- *Principe (0,5 pt).* Sous le régime de faveur, les déficits non encore déduits de l'absorbée sont transférés à la société qui reçoit le patrimoine **sur agrément**. L'agrément suppose notamment une opération justifiée économiquement, une activité à l'origine des déficits poursuivie pendant au moins 3 ans sans changement significatif, et des déficits qui ne proviennent pas de la gestion d'un patrimoine mobilier ou immobilier [V CGI art. 209 II-1, F02 § 3]. Sous le droit commun, le déficit ne serait pas transférable [V CGI art. 209 II-1, F02 § 2].
- *Application (0,5 pt).* L'agrément n'est pas requis lorsque le déficit transféré est inférieur à **200 000 €**, qu'il ne provient pas de la gestion d'un patrimoine mobilier ou immobilier et que l'absorbée n'a ni cédé ni cessé d'exploiter un fonds ou un établissement pendant la période déficitaire [V CGI art. 209 II-2, F02 § 3]. Les trois conditions sont remplies : 160 000 € < 200 000 €, activité de transport fluvial, aucune cession ni cessation. Le déficit est transféré sans agrément. ARGANEAU l'imputera sur ses bénéfices dans la limite de 1 000 000 € majorée de 50 % du bénéfice qui excède ce montant [V CGI art. 209 I, F02 § 3], soit une économie d'impôt potentielle de 160 000 × 25 % = **40 000 €**.

---

### 2.3 Valeur de transmission, actif net transmis et mali (4 pts)

**Valeur de transmission (1 pt).** ARGANEAU détient 100 % des droits de vote de TOUALYS : elle la contrôle de manière exclusive et l'opération est réalisée **sous contrôle commun** [V PCG art. 741-1 et 741-2, F01 § 2.1]. Pour une confusion de patrimoine, qui intervient toujours entre entités sous contrôle commun, le PCG impose la **valeur comptable** : ARGANEAU reprend les valeurs de chaque actif et de chaque passif dans les comptes de TOUALYS [V PCG art. 760-1 et 744-2, F01 § 2.4 et § 3.2]. Le sens de l'opération est sans objet. La dérogation qui impose les valeurs réelles lorsque l'actif net comptable ne permet pas de libérer le capital ne s'applique pas aux confusions de patrimoine ; elle serait d'ailleurs sans objet ici, puisqu'aucun capital n'est émis [V PCG art. 743-3, F01 § 2.4].

**Actif net comptable transmis (1,5 pt)**

| Élément | Montant |
|---|---:|
| Total de l'actif (valeurs nettes) | 2 634 000 |
| – Emprunts bancaires | – 640 000 |
| – Emprunt auprès d'ARGANEAU et intérêts courus | – 308 000 |
| – Fournisseurs | – 140 000 |
| – Dettes sociales | – 46 000 |
| **Actif net comptable transmis** | **1 500 000** |

Contrôle par les capitaux propres de TOUALYS : 1 500 000 – 112 000 – 8 000 + 120 000 = **1 500 000 €**. Les amortissements dérogatoires sont des provisions réglementées, classées dans les capitaux propres : ils font partie de l'actif net transmis [V PCG art. 214-8 et 313-1, F01 § 8]. Les dettes et créances entre les deux sociétés sont transmises comme les autres ; leur extinction après la transmission ne modifie pas l'actif net.

**Annulation des titres et mali (1,5 pt).** Aucune action n'est émise : la totalité de l'actif net transmis revient à ARGANEAU, à hauteur de sa participation de 100 %, en contrepartie de l'annulation des titres TOUALYS (0,5 pt). Il n'y a ni augmentation de capital ni prime de fusion.

Résultat d'annulation = 100 % × 1 500 000 – 2 700 000 = **– 1 200 000 €**, soit un **mali** de 1 200 000 € (1 pt) [V PCG art. 745-3 et 760-2, F01 § 5.3]. Il apparaît parce que la valeur comptable des titres excède l'actif net comptable reçu.

---

### 2.4 Décomposition et affectation du mali (5 pts)

**Plus-values latentes et passif non comptabilisé (1,5 pt)**

| Élément | Valeur réelle | Valeur comptable | Écart retenu |
|---|---:|---:|---:|
| Pousseurs | 1 880 000 | 1 400 000 | + 480 000 |
| Barges en service | 1 140 000 | 900 000 | + 240 000 |
| Barges anciennes (cession prévue en 2027) : 120 000 × (1 – 25 %) | 120 000 | 0 | + 90 000 |
| Engagements de retraite (non comptabilisés) | 40 000 | 0 | – 40 000 |

Le mali technique correspond, à hauteur de la participation, aux plus-values latentes sur les éléments d'actif, comptabilisés ou non, déduction faite des passifs non comptabilisés faute d'obligation comptable, comme les engagements de retraite [V PCG art. 745-4, F01 § 5.3]. Les plus-values sur actifs destinés à être revendus à brève échéance sont retenues **nettes d'impôt** : la plus-value des barges anciennes sera imposée à 25 % lors de leur cession en 2027 (0,75 pt pour les deux plus-values brutes, 0,5 pt pour la plus-value nette d'impôt des barges anciennes, 0,25 pt pour les engagements de retraite). Les autres plus-values sont retenues pour leur montant brut (hypothèse de l'annexe 2.4). ARGANEAU ne provisionnant pas ses propres engagements de retraite, l'ajustement de provision prévu par l'art. 744-3 ne s'applique pas : l'engagement de TOUALYS reste un passif non comptabilisé.

**Fonds commercial latent (1 pt)**
- Actif net réel identifié : 1 500 000 + 480 000 + 240 000 + 90 000 – 40 000 = **2 270 000 €**.
- Fonds commercial non comptabilisé : 2 520 000 – 2 270 000 = **250 000 €**.

**Mali technique et vrai mali (1 pt)**

| Composante | Calcul | Montant |
|---|---|---:|
| Mali technique | 100 % × (480 000 + 240 000 + 90 000 + 250 000 – 40 000) | **1 020 000** |
| Vrai mali | 1 200 000 – 1 020 000 | **180 000** |
| **Mali total** | | **1 200 000** |

Contrôles : mali technique = valeur réelle globale – actif net comptable = 2 520 000 – 1 500 000 ; vrai mali = coût des titres – valeur réelle globale = 2 700 000 – 2 520 000.

Le **vrai mali** de 180 000 € est la dépréciation de la participation devenue nécessaire au moment de l'opération. Il est comptabilisé en **résultat financier** de l'exercice 2027, celui de l'opération [V PCG art. 745-4, F01 § 5.3]. Il traduit la perte de valeur de TOUALYS après le départ de son principal client. Ce départ, décidé en janvier 2027 sans lien avec une situation existant au 31/12/2026, n'imposait aucune dépréciation dans les comptes de 2026 : la valeur d'utilité des titres (2 900 000 €) excédait alors leur coût.

**Affectation du mali technique (1,5 pt).** Le mali technique (1 020 000 €) est supérieur à la somme des plus-values latentes sur les actifs identifiés hors fonds commercial (480 000 + 240 000 + 90 000 = 810 000 €). Il est donc affecté à chacun de ces actifs à hauteur de sa plus-value, et le solde au fonds commercial [V PCG art. 745-5, F01 § 5.4], dans un compte spécifique par catégorie d'actif [V PCG art. 745-6, F01 § 5.4].

| Actif sous-jacent | Calcul | Mali affecté | Compte |
|---|---|---:|---|
| Pousseurs | plus-value latente | 480 000 | 2187 Mali de fusion sur actifs corporels |
| Barges en service | plus-value latente | 240 000 | 2187 Mali de fusion sur actifs corporels |
| Barges anciennes | plus-value nette d'impôt | 90 000 | 2187 Mali de fusion sur actifs corporels |
| Fonds commercial (solde) | 1 020 000 – 810 000 | 210 000 | 2081 Mali de fusion sur actifs incorporels |
| **Total** | | **1 020 000** | |

Le solde affecté au fonds commercial (210 000 €) correspond au fonds commercial latent (250 000 €) diminué des engagements de retraite non comptabilisés (40 000 €).

---

### 2.5 Écritures au 1er mars 2027 chez ARGANEAU (6 pts)

**T1 — Vrai mali : dépréciation des titres TOUALYS (1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6866 Dotations pour dépréciation des éléments financiers | 180 000 | |
| 2961 Dépréciations des titres de participation | | 180 000 |

**T2 — Reprise du patrimoine de TOUALYS et annulation des titres (2,5 pts).** Le patrimoine est repris à la valeur comptable, avec les **valeurs brutes et les amortissements** de TOUALYS [V PCG art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2] (1 pt). Les dettes sont reprises à leur montant (0,5 pt). Les titres sont annulés pour leur valeur brute, la dépréciation T1 étant soldée, et le mali technique est inscrit dans ses comptes spécifiques (1 pt).

| Compte | Débit | Crédit |
|---|---:|---:|
| 2182 Matériel de transport (pousseurs et barges, valeur brute) | 4 360 000 | |
| 411 Clients | 210 000 | |
| 44567 Crédit de TVA à reporter | 30 000 | |
| 512 Banques | 94 000 | |
| 2187 Mali de fusion sur actifs corporels (pousseurs) | 480 000 | |
| 2187 Mali de fusion sur actifs corporels (barges en service) | 240 000 | |
| 2187 Mali de fusion sur actifs corporels (barges anciennes) | 90 000 | |
| 2081 Mali de fusion sur actifs incorporels (fonds commercial) | 210 000 | |
| 2961 Dépréciations des titres de participation | 180 000 | |
| 28182 Amortissements du matériel de transport | | 2 060 000 |
| 164 Emprunts auprès des établissements de crédit | | 640 000 |
| 1681 Autres emprunts (emprunt auprès d'ARGANEAU) | | 300 000 |
| 1688 Intérêts courus sur autres emprunts | | 8 000 |
| 401 Fournisseurs | | 140 000 |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | | 46 000 |
| 261 Titres de participation TOUALYS | | 2 700 000 |
| **Total** | **5 894 000** | **5 894 000** |

**T3 — Reconstitution des amortissements dérogatoires (0,75 pt).** Engagement du régime de faveur (voir 2.2). En l'absence de prime, le prélèvement est fait sur les autres réserves (annexe 2.1).

| Compte | Débit | Crédit |
|---|---:|---:|
| 1068 Autres réserves | 120 000 | |
| 145 Amortissements dérogatoires | | 120 000 |

**T4 — Extinction du prêt et des intérêts courus (0,5 pt).** ARGANEAU est désormais à la fois créancière et débitrice de la même obligation : la confusion éteint la créance et ses accessoires [V C. civ. art. 1349, F01 § 8].

| Compte | Débit | Crédit |
|---|---:|---:|
| 1681 Autres emprunts (emprunt auprès d'ARGANEAU) | 300 000 | |
| 1688 Intérêts courus sur autres emprunts | 8 000 | |
| 2671 Créances rattachées à des participations (prêt à TOUALYS) | | 300 000 |
| 2678 Intérêts courus sur créances rattachées | | 8 000 |

**T5 — Extinction des dettes et créances commerciales réciproques (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette d'ARGANEAU envers TOUALYS) | 84 000 | |
| 401 Fournisseurs (dette de TOUALYS envers ARGANEAU, reprise en T2) | 18 000 | |
| 411 Clients (créance de TOUALYS sur ARGANEAU, reprise en T2) | | 84 000 |
| 411 Clients (créance d'ARGANEAU sur TOUALYS) | | 18 000 |

**T6 — Frais de l'opération (0,5 pt).** ARGANEAU n'a pas de prime sur laquelle imputer les frais et ne les inscrit pas à l'actif : ils sont comptabilisés en charges [V PCG art. 212-9, F01 § 7]. Ils sont déductibles du résultat fiscal.

| Compte | Débit | Crédit |
|---|---:|---:|
| 6226 Honoraires | 18 000 | |
| 44566 TVA sur autres biens et services | 3 600 | |
| 401 Fournisseurs | | 21 600 |

---

### 2.6 Suivi du mali technique en 2027 (2,5 pts)

**S1 — Cession des barges anciennes le 30 juin 2027 (0,75 pt).** Le mali affecté à un actif suit le même traitement que cet actif en cas de cession [V PCG art. 745-10, F01 § 5.5] : la quote-part de 90 000 € sort du bilan avec les barges.

| Compte | Débit | Crédit |
|---|---:|---:|
| 512 Banques | 120 000 | |
| 757 Produits des cessions d'immobilisations incorporelles et corporelles | | 120 000 |
| 28182 Amortissements du matériel de transport (barges anciennes) | 360 000 | |
| 2182 Matériel de transport (barges anciennes) | | 360 000 |
| 657 Valeurs comptables des immobilisations incorporelles et corporelles cédées (mali affecté aux barges anciennes) | 90 000 | |
| 2187 Mali de fusion sur actifs corporels (barges anciennes) | | 90 000 |

Les barges étant totalement amorties, ni elles ni le mali qui leur est affecté ne sont amortis avant la cession [V PCG art. 745-7]. Résultat comptable de cession : 120 000 – 0 – 90 000 = 30 000 €.

**S2 — Amortissement du mali au 31 décembre 2027 (1 pt).** Le mali technique est amorti selon les mêmes règles que l'actif sous-jacent [V PCG art. 745-7, F01 § 5.5], sur sa durée résiduelle et à compter du 1er mars 2027, soit 10 mois en 2027 :
- pousseurs : 480 000 / 8 × 10 / 12 = **50 000 €** ;
- barges en service : 240 000 / 10 × 10 / 12 = **20 000 €**.

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles | 70 000 | |
| 28187 Amortissement du mali de fusion sur actifs corporels | | 70 000 |

Aucun indice de perte de valeur n'étant relevé sur les pousseurs et les barges en service, aucune dépréciation n'est constatée [V PCG art. 745-8].

**Fonds commercial (0,25 pt).** La quote-part de 210 000 € n'est pas amortie : le fonds commercial est présumé avoir une durée d'utilisation non limitée [V PCG art. 214-3, F01 § 5.5]. Elle n'est pas dépréciée : la valeur actuelle du fonds commercial (230 000 €) excède sa valeur nette comptable chez ARGANEAU, nulle, majorée du mali affecté (210 000 €) [V PCG art. 745-8].

**Traitement fiscal (0,5 pt).** Le mali technique ne peut donner lieu à aucune déduction ultérieure [V CGI art. 210 A-1, F02 § 2] : ARGANEAU **réintègre** extra-comptablement en 2027 la dotation de 70 000 € et la sortie de 90 000 €, soit 160 000 €. Sur la cession, la plus-value fiscale est calculée d'après la valeur fiscale des barges chez TOUALYS, nulle : 120 000 €, soit l'impôt de 30 000 € déjà déduit dans le calcul du mali (résultat comptable 30 000 + réintégration 90 000 = 120 000).

---

### 2.7 Capitaux propres d'ARGANEAU juste après l'opération et note (1,5 pt)

**Capitaux propres (0,75 pt).** Incidences de l'opération au 1er mars 2027, avant impôt sur les sociétés de l'exercice ; conformément à l'annexe 2.1, le résultat d'ARGANEAU de janvier et février 2027 n'est pas pris en compte :

| Poste | Avant l'opération (31/12/2026) | Variation | Après l'opération |
|---|---:|---:|---:|
| Capital | 2 000 000 | | 2 000 000 |
| Réserve légale | 200 000 | | 200 000 |
| Autres réserves | 1 780 000 | – 120 000 | 1 660 000 |
| Report à nouveau | 200 000 | | 200 000 |
| Résultat de l'opération (vrai mali 180 000, frais 18 000) | 0 | – 198 000 | – 198 000 |
| Amortissements dérogatoires | 0 | + 120 000 | 120 000 |
| **Total** | **4 180 000** | **– 198 000** | **3 982 000** |

Contrôle : la reconstitution des amortissements dérogatoires est un reclassement entre postes de capitaux propres ; seules les charges de l'opération (180 000 + 18 000) diminuent leur total.

**Note à Mme WEISSKOPF (0,75 pt, grille de niveaux)**

| Niveau | 0 | 0,25 | 0,5 | 0,75 |
|---|---|---|---|---|
| Attendu | Absence ou note hors sujet | Une idée pertinente | Deux ou trois idées, comptes et créanciers | Note structurée couvrant les comptes, le résultat et les créanciers |

Idées attendues :
- **Bilan** : les titres TOUALYS (2 700 000 €) sont remplacés par la flotte de TOUALYS, ses créances et sa trésorerie, et par un mali technique de 1 020 000 € inscrit en immobilisations. Le prêt de 300 000 € et les créances réciproques disparaissent ; l'emprunt bancaire de TOUALYS (640 000 €) alourdit l'endettement d'ARGANEAU.
- **Résultat 2027** : le vrai mali (180 000 €) et les frais (18 000 €) diminuent le résultat dès le 1er mars. Le mali technique sur les bateaux s'amortit (70 000 € en 2027) ou sort lors des cessions (90 000 €), sans déduction fiscale. Le mali affecté au fonds commercial (210 000 €) reste exposé à un risque de dépréciation. En contrepartie, le déficit de TOUALYS, transféré sans agrément, peut réduire l'impôt d'ARGANEAU de 40 000 €.
- **Capitaux propres** : ils diminuent de 198 000 € et restent solides (3 982 000 €, près du double du capital).
- **Créanciers** : ceux de TOUALYS, en particulier sa banque, deviennent créanciers d'ARGANEAU ; ils ont pu faire opposition pendant le délai légal et disposent désormais de l'ensemble du patrimoine d'ARGANEAU comme gage. Les créanciers d'ARGANEAU partagent ce gage avec les anciens créanciers de TOUALYS, mais retrouvent dans le bilan d'ARGANEAU les bateaux qui n'y figuraient auparavant qu'à travers les titres.

---

### Réponses tolérées
- **Vrai mali** : enregistrement direct par le débit de 6866 et le crédit de 261 au lieu du passage par 2961. C'est une présentation abrégée admise [F01 § 9].
- **Amortissements dérogatoires** : un candidat qui les reprend directement au crédit du compte 145 dans l'écriture T2, avec un actif net transmis de 1 380 000 €, obtient un mali de 1 320 000 €, un mali technique de 1 140 000 € (dont 330 000 € au fonds commercial) et un vrai mali inchangé de 180 000 €. Cette méthode ne suit pas la convention de l'annexe 2.1 et n'est pas la méthode de référence [F01 § 8]. Elle est acceptée pour l'écriture T2 si elle est cohérente sur l'ensemble du dossier ; les montants de l'actif net et du mali en 2.3 sont alors comptés faux.
- **Écriture T2** : présentation en deux écritures (reprise des actifs et passifs par un compte d'associé, puis annulation des titres), ou dettes sociales ventilées entre 421 et 431.
- **Prêt** : emprunt de TOUALYS inscrit en 1687 ou en compte courant (451 ou 455), à condition que la même écriture d'extinction soit passée.
- **Cession des barges** : présentation en deux écritures (cession des barges, puis sortie de la quote-part de mali par le débit de 657).

### Erreurs fréquentes (rapports du jury)
- `JUR-R02` Mali calculé sans être analysé : pas de décomposition, ou vrai mali oublié alors que la valeur réelle globale est inférieure au coût des titres.
- `JUR-R03` Oubli de la reconstitution des amortissements dérogatoires. Ici, sans prime de fusion, le candidat doit appliquer la convention de l'annexe 2.1.
- `JUR-R04` Suivi du mali mal traité alors que l'annexe 2.6 donne la règle : amortissement du mali affecté au fonds commercial, amortissement sur 12 mois au lieu de 10, oubli de la sortie du mali lors de la cession des barges.
- `JUR-R05` Difficulté à s'adapter à une situation un peu différente : recherche d'une parité, d'une augmentation de capital ou d'une prime de fusion dans une TUP.
- Erreurs propres à ce cas : valeur réelle retenue au motif que TOUALYS a des plus-values latentes ; écritures datées du 1er janvier 2027 ; plus-value des barges anciennes retenue brute (120 000 €), ce qui porte à tort le mali affecté aux barges à 120 000 € et celui du fonds commercial à 180 000 € ; impôt déduit de toutes les plus-values ; engagements de retraite oubliés ; dépréciation des titres rattachée à l'exercice 2026.

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Nature de la mission légale ; moyens d'action face aux données perdues | `3.2.a` Notion d'audit des comptes et cadre conceptuel ; `3.2.b` Moyens d'action du CAC | 4 |
| 3.2 Cycle personnel et paie : risques, assertions, procédures | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit | 3 |
| 3.3 Procédure analytique sur la masse salariale | `3.2.d` Démarche d'audit (techniques) ; `3.2.c` Caractère significatif | 3 |
| 3.4 Demande du directoire : autorévision, immixtion, honoraires | `3.1.c` Principes déontologiques ; `3.1.d` Appliquer la norme pertinente | 4 |
| 3.5 Fin de mission, opinion, responsabilités | `3.2.d` Démarche d'audit (fin de mission, note de synthèse) ; `3.2.e` Portée des opinions ; `3.1.e` Mise en cause de la responsabilité | 4 |
| 3.6 Architecture des ESRS, EFRAG, ISSB et GRI ; version 2026 | `3.3.a` Contexte et architecture des normes de durabilité | 4 |
| 3.7 Double matérialité, IRO, périmètre, connectivité | `3.3.b` Principes de construction du reporting | 5 |
| 3.8 Assurance limitée ; avis sur les axes 1 et 2 | `3.4.a` Objectifs de la mission d'audit de durabilité ; `3.4.c` Portée des avis | 3 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes annuels (18 points)

### 3.1 Nature de la mission légale ; moyens d'action face aux données perdues (4 pts)

**a. Nature et objectif de la mission ; distinction avec un audit contractuel ; réponse à M. STOEBER (2 pts)**

- **Nature et objectif (1 pt)** :
  - la certification est une **mission légale** : elle est confiée au commissaire aux comptes par la loi et par sa désignation par l'assemblée générale ordinaire, ici pour six exercices (2024 à 2029) [V C. com. L. 821-2 III, L. 821-40 I, L. 821-44]. C'est une mission d'intérêt général [V code de déontologie art. 1er] ;
  - le commissaire aux comptes **certifie**, en justifiant de ses appréciations, que les comptes annuels sont **réguliers et sincères** et donnent une **image fidèle** du résultat de l'exercice, de la situation financière et du patrimoine [V L. 821-53]. Il exprime cette **opinion** après avoir mis en œuvre un **audit des comptes** [V NEP principes § 01] ;
  - l'audit procure une **assurance raisonnable** : une assurance élevée, mais non absolue, que les comptes **pris dans leur ensemble** ne comportent pas d'anomalies significatives. Elle n'est pas absolue à cause des limites de l'audit : sondages, limites des contrôles de l'entité, éléments qui conduisent plus à des présomptions qu'à des certitudes [V NEP principes § 08-09] ;
  - la mission est permanente et exercée sans immixtion dans la gestion ; elle ne garantit ni la viabilité de l'entité ni la qualité de sa gestion [V L. 821-54 I, L. 821-55].
- **Distinction avec un audit contractuel (0,5 pt)** : un audit contractuel est réalisé à la demande de l'entité, hors obligation légale. Son objet et son étendue sont fixés par le contrat, et son rapport est destiné à celui qui l'a commandé [S, notion doctrinale, F11 § 1.2]. Réalisé par un commissaire aux comptes, c'est une **prestation**, qui suppose une lettre de mission et le respect des règles d'indépendance [V L. 821-2 IV, R. 821-195 ; L. 821-28 IV]. Il ne remplace pas la certification, qui s'adresse à l'assemblée générale et à tous les utilisateurs des comptes.
- **Réponse à M. STOEBER (0,5 pt)** :
  - la certification n'est pas un simple contrôle par sondages : les sondages sont un moyen, mais l'opinion porte sur les comptes **de tout l'exercice**. Les charges de personnel de janvier à août (12 741 000 €) ne peuvent pas être laissées de côté ;
  - c'est le commissaire aux comptes, et non l'entité, qui détermine la nature et l'étendue de ses travaux : il procède à toute époque à toutes vérifications et contrôles [V L. 821-60 ; NEP réponses § 03-13]. La lettre de mission précise l'objectif, l'étendue et les modalités de la mission [V NEP lettre de mission § 3-8] ; elle ne peut pas restreindre une mission qui résulte de la loi [S] ;
  - une limitation de l'étendue des travaux, qu'elle soit imposée par l'entité ou qu'elle résulte des circonstances, ne disparaît pas : elle est traitée dans le rapport, par une réserve ou par une impossibilité de certifier [V NEP rapport § 11, 14]. HALDÈNE refuse donc de signer une telle lettre.

**b. Moyens d'action et portée dans la situation de RIVÉLINE CROISIÈRES (2 pts)**

| Moyen d'action | Contenu | Portée en l'espèce | Points |
|---|---|---|---:|
| Droit d'investigation et de communication | À toute époque, toutes vérifications et contrôles ; communication **sur place** de toutes pièces utiles : contrats, livres, documents comptables, registres des procès-verbaux [V L. 821-60] | HALDÈNE obtient tout ce qui subsiste : écritures centralisées, relevés bancaires, attestations et accusés de réception des DSN, plannings de la flotte, contrats papier des permanents, procès-verbaux du directoire, rapport de l'expert en sécurité informatique, pièces des litiges prud'homaux | 0,5 |
| Recours à des experts | Assistance d'experts ou de collaborateurs nommément désignés [V L. 821-60] | Un expert informatique choisi par HALDÈNE peut apprécier, indépendamment de l'expert mandaté par la société, si des données sont récupérables | 0,25 |
| Informations auprès des tiers | Investigations auprès des entités contrôlantes ou contrôlées (sans objet : RIVÉLINE n'appartient à aucun groupe) ; informations auprès des **tiers ayant accompli des opérations pour le compte de l'entité** ; la communication de **pièces** détenues par un tiers suppose l'autorisation du président du tribunal de commerce statuant en référé [V L. 821-61 al. 1-2, D. 821-175]. Les demandes de confirmation des tiers sont une technique de contrôle [V NEP éléments probants § 10] | Banque (remises de virements), éditeur PAYRHIN, organismes sociaux, salariés et anciens saisonniers ont été sollicités (annexe 3.2). Une autorisation judiciaire ne servirait à rien : les tiers ne détiennent pas les pièces manquantes | 0,5 |
| Secret et protection des vérifications | Le secret professionnel n'est pas opposable au commissaire aux comptes, sauf par les auxiliaires de justice [V L. 821-61 al. 3] ; l'obstacle aux vérifications est un délit des dirigeants [V L. 821-6 3°] | L'avocat de la société dans les litiges prud'homaux peut opposer son secret : HALDÈNE demande au directoire d'interroger ses avocats [V NEP applications spécifiques § 7-8]. La perte des données résulte d'une attaque, pas d'un obstacle : le délit n'est pas constitué | 0,25 |

**Appréciation (0,5 pt)** : ces moyens donnent accès à l'information qui **existe**, mais ils ne recréent pas des données détruites. Les éléments recueillis établissent les **montants globaux** versés (virements, cotisations), pas l'**existence** de chaque salarié rémunéré, le **montant dû** à chacun ni l'**exhaustivité** des heures et des cotisations. Les réponses des salariés couvrent 41 permanents sur 250 et 6 saisonniers sur 50 interrogés. HALDÈNE ne peut pas non plus reconstituer lui-même la paie, ce qui serait une immixtion dans la gestion (voir 3.4). Si les éléments restent insuffisants, il en tire les conséquences dans son rapport (voir 3.5). On valorise la mention du droit aux honoraires : les diligences supplémentaires justifient un budget complémentaire, convenu avec l'entité [V NEP lettre de mission § 3-8 ; code de déontologie art. 12].

**Réponses tolérées**
- La circularisation des salariés présentée comme une « confirmation des tiers », si le candidat en voit les limites (taux de réponse, salariés partis).
- L'absence du recours à un expert, si les autres moyens sont présentés avec leur portée.

**Erreurs fréquentes**
- Confondre assurance raisonnable et assurance absolue, ou présenter les sondages comme une limite que l'entité peut choisir (`JUR-A01`).
- Énumérer les moyens d'action sans dire ce qu'ils permettent d'obtenir dans le cas (`JUR-A05`, `JUR-A06`).
- Accepter la lettre de mission proposée au motif que la société est de bonne foi.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-2 III-IV, L. 821-40 I, L. 821-44, L. 821-53, L. 821-54 I, L. 821-55, R. 821-195 ; code de déontologie art. 1er | Mission légale, prestation, certification, immixtion, absence de garantie | [V] | F09 § 3, 6 ; F11 § 1 |
| NEP principes § 01, 08-09 ; NEP lettre de mission § 3-8 ; NEP rapport § 11, 14 | Assurance raisonnable ; lettre de mission ; limitation | [V] ; application : [S] | F11 § 1, 7, 8 |
| Audit contractuel | Notion doctrinale | [S] | F11 § 1.2 |
| C. com. L. 821-6 3°, L. 821-60, L. 821-61, D. 821-175 ; NEP applications spécifiques § 7-8 | Moyens d'action ; délit d'obstacle ; litiges | [V] | F09 § 5 ; F11 § 2, 6.4 |

### 3.2 Cycle personnel et paie : risques, assertions et procédures (3 pts)

**Risque d'anomalies significatives et orientation des travaux (1 pt)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41]
- **Appréciation (0,5 pt)** : le risque d'anomalies significatives (RAS), propre à l'entité, comprend le risque inhérent et le risque lié au contrôle.
  - **Risque inhérent élevé** : poste lourd (19 000 000 €, 36,7 % des charges d'exploitation) ; forte volumétrie (jusqu'à 410 salariés) ; main-d'œuvre saisonnière à forte rotation (près d'un saisonnier sur trois part avant la fin de la saison) ; éléments variables (heures supplémentaires, primes de fin de saison) ; **estimations** (congés payés, charges incorporées à la rénovation du MOSELLANE) ; litiges prud'homaux ; **changement de système d'information** en septembre, avec des dossiers recréés ; pression du directoire pour obtenir une certification sans réserve, facteur de risque de fraude [V NEP risques § 02].
  - **Risque lié au contrôle élevé** : sauvegardes stockées sur le même réseau ; pistes d'audit détruites de janvier à août ; contrats des saisonniers uniquement électroniques ; écritures centralisées qui ne distinguent pas les catégories de salariés ; nouveau logiciel récent. Sans test des contrôles, le RAS au niveau des assertions correspond au risque inhérent évalué [V NEP risques § 41].
- **Orientation (0,5 pt)** : le RAS étant élevé, le risque de non-détection acceptable est **faible** : HALDÈNE renforce ses **procédures de substance** (tests de détail, éléments probants externes, travaux à la clôture), élargit ses échantillons et confie le cycle à une équipe expérimentée [V NEP principes § 13 ; NEP réponses § 03-13 ; NEP éléments probants § 6].

**Risques, assertions et procédures (2 pts, 0,5 pt par risque pertinent, avec son assertion et une procédure justifiée, dans la limite de quatre)**

| Risque | Assertion | Procédure et justification |
|---|---|---|
| **Salariés fictifs** ou paiements à des personnes qui ne travaillent pas, ou plus, pour la société (saisonniers en particulier : contrats électroniques, forte rotation) | **Réalité** et **mesure** des rémunérations (flux) | **Test de détail** sur septembre à décembre : échantillon tiré du journal de paie, rapproché du contrat signé, du **planning** (présence à bord), du relevé d'heures et du **fichier de virements** transmis à la banque, dont le total est rapproché de la remise figurant sur le relevé bancaire ; contrôle des sorties de saisonniers (soldes de tout compte d'octobre). Le planning d'exploitation, tenu hors du logiciel de paie, et le relevé bancaire (pour le montant global) sont des sources indépendantes de la paie |
| Cotisations et dettes sociales incomplètes : heures supplémentaires des saisonniers non payées ni déclarées, DSN incomplètes | **Exhaustivité** des cotisations (flux) et des dettes sociales (solde) | **Rapprochement** de la masse salariale comptabilisée (641, 645) avec les DSN de septembre à décembre et les **attestations des organismes sociaux** (éléments externes) ; **vérification du calcul** des cotisations sur un échantillon ; demande au directoire d'interroger ses avocats sur les réclamations prud'homales, pour apprécier la nécessité d'une provision [V NEP applications spécifiques § 7-8] |
| Heures supplémentaires de décembre payées en janvier 2027 | **Séparation des exercices** des charges (flux) ; **exhaustivité** des charges à payer (solde) | Examen de la **paie de janvier 2027** et des relevés d'heures de décembre ; vérification que ces heures et leurs cotisations sont comptabilisées en charges à payer au 31/12/2026 |
| Dettes provisionnées pour congés à payer (1 260 000 €, dont 540 000 € estimés forfaitairement) | **Évaluation** et **exhaustivité** (solde) | **Recalcul** sur un échantillon de salariés à partir des droits acquis et des congés pris (relevés de septembre à décembre) et des taux de cotisations ; examen critique de la méthode d'estimation des 540 000 € (hypothèses, comparaison avec 2025), dont on sait qu'il ne pourra pas être corroboré |

Autres réponses acceptées :
- **charges de personnel incorporées à la rénovation du MOSELLANE** (420 000 €) : **classification** (charges ou production immobilisée) et **évaluation** de l'immobilisation (solde) ; rapprochement des heures avec les plannings d'hivernage et les rapports de chantier ;
- **primes de fin de saison et indemnités de congés payés des saisonniers** versées en octobre : **mesure** ; recalcul sur un échantillon de la paie d'octobre ;
- **procédure analytique** sur la masse salariale (voir 3.3), utile mais insuffisante seule face à un risque élevé.

**Réponses tolérées** : l'« existence » des salariés employée pour la réalité des rémunérations, si le candidat rattache bien le risque aux charges de personnel.

**Erreurs fréquentes**
- Confondre réalité (flux) et existence (solde), ou séparation des exercices et exhaustivité (`JUR-A01`).
- Proposer des procédures sur janvier à août, que l'annexe 3.2 rend impossibles (`JUR-F07`).
- Décrire l'organisation de la paie que l'entité devrait mettre en place, au lieu d'évaluer le risque.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 10-13 ; NEP risques § 02, 39-41 | RAS, risque de non-détection, facteurs de risque inhérent | [V] | F11 § 4.1 |
| NEP éléments probants § 6, 9, 10 ; NEP réponses § 03-13 | Assertions ; techniques ; procédures en réponse | [V] | F11 § 4.3, 5, 6 |
| NEP applications spécifiques § 7-8 | Litiges : interrogation des avocats | [V] | F11 § 6.4 |

### 3.3 Procédure analytique sur la masse salariale (3 pts)

**Salaires mensuels moyens de 2026 (0,5 pt)**
- Permanents : 3 200 × 1,025 = **3 280 €**.
- Saisonniers : 2 700 × 1,02 = **2 754 €**.

**Masse salariale attendue (1 pt : 0,5 pt par période)**

| Élément | Janvier à août | Septembre à décembre |
|---|---:|---:|
| Mois d'emploi : permanents / saisonniers | 8 / 5 (avril à août) | 4 / 2 (septembre et octobre) |
| Rémunérations des permanents (250 ETP × mois × 3 280 €) | 6 560 000 € | 3 280 000 € |
| Rémunérations des saisonniers (160 ETP × mois × 2 754 €) | 2 203 200 € | 881 280 € |
| **Rémunérations brutes attendues** | **8 763 200 €** | **4 161 280 €** |
| Cotisations des permanents (42 %) | 2 755 200 € | 1 377 600 € |
| Cotisations des saisonniers (20 %) | 440 640 € | 176 256 € |
| **Cotisations patronales attendues** | **3 195 840 €** | **1 553 856 €** |
| **Masse salariale attendue** | **11 959 040 €** | **5 715 136 €** |

**Comparaison (0,5 pt)**

| Élément | Janvier à août | Septembre à décembre |
|---|---:|---:|
| Masse comptabilisée (641 + 645) | 12 741 000 € | 5 731 000 € |
| Écart (comptabilisé − attendu) | **781 960 €**, soit 6,5 % | **15 864 €**, soit 0,3 % |
| dont rémunérations | 554 800 € (6,3 %) | 13 720 € (0,3 %) |
| dont cotisations | 227 160 € (7,1 %) | 2 144 € (0,1 %) |
| Écart acceptable (75 000 €) | **dépassé** (10,4 fois) | respecté |
| Seuil de signification (250 000 €) | **dépassé** (3,1 fois) | — |

**Conclusion (0,5 pt)**
- **Septembre à décembre** : l'écart est inférieur à l'écart acceptable. La masse salariale comptabilisée est **plausible**, ce que corroborent les tests de détail réalisables sur cette période (annexe 3.5).
- **Janvier à août** : l'écart de 781 960 € dépasse l'écart acceptable et le seuil de signification ; il représente 15,6 % du résultat courant avant impôt. La procédure de substance impose de l'**expliquer** par des éléments probants [V NEP réponses § 05 pour la définition ; S, application]. Or les bulletins, les relevés d'heures et le journal de paie de la période sont détruits, et les écritures centralisées ne distinguent pas les catégories de salariés : l'écart **ne peut pas être expliqué**. Il peut provenir d'éléments légitimes (heures supplémentaires, primes, remplacements de saisonniers) comme de paiements indus. La procédure ne valide pas les charges de la période : elle **confirme la limitation** relevée dans la note de synthèse.

**Limites (0,5 pt)**
- Les effectifs proviennent des **plannings**, qui indiquent un équipage **prévu**, pas le travail réellement effectué : les réclamations des saisonniers portent précisément sur des heures absentes des plannings.
- Les salaires et les taux sont des **moyennes**, et l'écart acceptable relève du jugement du cabinet [V NEP réponses § 05 pour la définition ; S, application].
- Un écart faible ne prouverait pas l'absence d'anomalie : des anomalies de sens contraire peuvent se compenser, comme ici le risque de paiements indus (charges surévaluées) et le risque d'heures non payées (charges et dettes sous-évaluées). Face à un RAS élevé, une procédure analytique ne suffit pas seule ; elle complète les tests de détail de 3.2.

**Réponses tolérées**
- Un calcul annuel unique (attendu 17 674 176 €, comptabilisé 18 472 000 €, écart 797 824 €, soit 4,5 %), complété par la constatation que l'écart se concentre sur janvier à août : 0,5 pt sur le point des périodes.
- Une conclusion qui qualifie l'écart de janvier à août d'« anomalie » : 0,25 pt sur le point de la conclusion. L'écart n'est pas une anomalie établie, puisqu'il ne peut pas être expliqué.

**Erreurs fréquentes**
- Appliquer l'augmentation des saisonniers à tous les mois de l'année, ou leur attribuer 12 mois d'emploi (`JUR-F07`).
- Conclure qu'il faut corriger les charges de 781 960 €, alors que l'écart n'est ni expliqué ni établi.
- Ne pas justifier les calculs (`JUR-F02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP éléments probants § 10 ; NEP réponses § 05 | Procédure analytique ; procédure de substance et écart acceptable | [V] | F11 § 6.2 |
| NEP caractère significatif § 6 | Seuil de signification | [V] | F11 § 4.2 |
| Données de l'annexe 3.3 | Effectifs, salaires, taux, conventions | données de l'énoncé | — |

### 3.4 Demande du directoire : autorévision, immixtion, honoraires (4 pts)

**Qualification de la demande (0,5 pt)** : les deux travaux demandés sont des **prestations**, services qui ne relèvent pas de la mission de certification [V L. 821-2 IV]. RIVÉLINE CROISIÈRES n'est pas une EIP : aucune liste fermée de services interdits ne s'applique. La question est de savoir si HALDÈNE peut les fournir **sans compromettre son indépendance**, ce qu'il faut apprécier selon les règles de l'annexe 3.4 [V L. 821-28 IV ; code de déontologie art. 5]. Que HALDÈNE soit aussi un cabinet d'expertise comptable ne change rien : c'est la mission de commissaire aux comptes qu'il exerce chez RIVÉLINE CROISIÈRES qui fixe les règles.

**Reconstitution des bulletins de paie : autorévision (1 pt)**
- Les bulletins reconstitués produiraient les montants que HALDÈNE doit ensuite certifier : charges de personnel de janvier à août, dettes sociales, congés payés, coût de la rénovation du MOSELLANE. HALDÈNE se prononcerait sur des éléments **résultant de ses propres prestations** : c'est la définition du **risque d'autorévision** [V code de déontologie art. 5 II ; annexe 3.4].
- Aucune **mesure de sauvegarde** ne peut ramener ce risque à un niveau acceptable : confier les travaux à une autre équipe du cabinet ne change pas le fait que le cabinet certifierait son propre travail, et l'indépendance s'apprécie aussi **en apparence** [V code de déontologie art. 5 ; S, application].
- Le commissaire aux comptes ne peut donc pas accepter ce travail tout en poursuivant sa mission [V L. 821-28 IV].

**Établissement et dépôt des DSN de régularisation : immixtion (0,5 pt)** : déclarer les salaires et les cotisations est une obligation de l'employeur, donc un **acte de gestion**. Le commissaire aux comptes exerce sa mission **à l'exclusion de toute immixtion dans la gestion** [V L. 821-54 I]. S'y ajoute le risque d'autorévision : les régularisations détermineraient les cotisations et les dettes sociales à comptabiliser.

**Honoraires conditionnels (0,75 pt)** : la majoration de 20 000 € « si votre rapport est une certification sans réserve » est une rémunération **conditionnelle**, **interdite** : les honoraires sont en rapport avec les diligences, jamais avec le sens de l'opinion [V code de déontologie art. 12-13]. Cette clause porte atteinte à l'**indépendance** et à l'**impartialité** du commissaire aux comptes, dont les conclusions doivent reposer sur une analyse objective, sans parti pris [V code de déontologie art. 4-5]. Elle doit être refusée quel que soit le sort des travaux demandés.

**Réponse de HALDÈNE (0,75 pt)**
- Mme KIRSCHER **refuse par écrit** les deux travaux et la clause d'honoraires, en expliquant les motifs, et documente son analyse dans le dossier [V NEP documentation § 04-08]. La situation est claire : une demande d'avis à la H2A, réservée au doute sérieux, n'est pas nécessaire [V code de déontologie art. 19 II].
- HALDÈNE informe aussi le conseil de surveillance, organe de contrôle de la gestion, de la demande et de sa réponse, dans le cadre de sa communication avec les organes de la société [V L. 821-63 I ; S, application].
- Le directoire peut confier la reconstitution et les DSN de régularisation à **un autre professionnel**, extérieur au cabinet et à son réseau, par exemple un expert-comptable ou un spécialiste de la paie. HALDÈNE examinera ensuite ces travaux, avec esprit critique, comme un élément parmi d'autres [V code de déontologie art. 6 ; NEP éléments probants § 7].
- HALDÈNE peut facturer ses propres diligences supplémentaires, sur un budget convenu à l'avance et sans lien avec l'opinion [V code de déontologie art. 12-13 ; NEP lettre de mission § 3-8].

**Ces travaux lèveraient-ils les difficultés ? (0,5 pt, mise en œuvre de la norme pertinente, celle des éléments probants)** : **non, pour l'essentiel**. Une reconstitution faite après coup à partir des **plannings**, des contrats et de la **grille de salaires** est une **estimation** : elle donne ce que la société aurait dû payer, pas ce qu'elle a réellement payé, ni à qui. Elle ne prouve ni l'existence des salariés rémunérés ni les heures réellement travaillées, sur lesquelles portent justement les réclamations des saisonniers. Ce sont des éléments internes, établis après coup, dont la fiabilité est faible [V NEP éléments probants § 6]. Pour les permanents, les contrats papier et les 41 réponses pourraient réduire l'incertitude ; pour les saisonniers, contrats et relevés d'heures manquent. Les DSN de régularisation pourraient en revanche révéler des **cotisations supplémentaires** à comptabiliser (exhaustivité des dettes), que HALDÈNE devrait examiner.

**Réponses tolérées**
- La démission de HALDÈNE présentée comme la seule façon d'accepter les travaux, si le candidat ajoute qu'elle serait disproportionnée et qu'un commissaire aux comptes ne peut pas démissionner pour se soustraire à l'émission de son opinion [V code de déontologie art. 28 ; F09 § 3.7].
- L'omission de l'information du conseil de surveillance, si les autres éléments de la réponse sont présents.

**Erreurs fréquentes**
- Accepter la reconstitution au motif que RIVÉLINE CROISIÈRES n'est pas une EIP, ou au motif que HALDÈNE est aussi expert-comptable (`JUR-A03`).
- Ne pas voir la clause d'honoraires conditionnels.
- Croire que la reconstitution, faite par HALDÈNE ou par un tiers, suffit à certifier sans réserve (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-2 IV, L. 821-28 IV, L. 821-54 I, L. 821-63 I | Prestations ; autorévision dans une entité non EIP ; immixtion ; communication avec les organes | [V] ; application : [S] | F10 § 3, 5 ; F09 § 6 ; F11 § 5 |
| Code de déontologie art. 4, 5, 6, 12-13, 19 II, 28 | Impartialité, indépendance, esprit critique, honoraires, avis de la H2A, démission | [V] ; application : [S] | F10 § 2.1, 4.1, 8 |
| NEP éléments probants § 6-7 ; NEP documentation § 04-08 | Fiabilité des éléments ; documentation | [V] | F11 § 6.1, 7 |

### 3.5 Fin de mission, opinion et responsabilités (4 pts)

**a. Travaux de fin de mission et note de synthèse (1 pt)**
- **Travaux restant à réaliser (0,5 pt)** :
  - récapituler et évaluer les anomalies, les communiquer au directoire et demander leur correction, ici la facture de gazole de 38 000 € [V NEP anomalies § 8-17] ;
  - examiner les **événements postérieurs** à la clôture jusqu'à la date du rapport, notamment l'évolution des litiges prud'homaux et d'éventuelles nouvelles réclamations [V NEP événements postérieurs § 01] ;
  - apprécier la **continuité d'exploitation** : aucune incertitude significative n'est relevée [V NEP continuité d'exploitation § 2] ;
  - obtenir les **déclarations écrites** du directoire, notamment sur l'exhaustivité des informations communiquées, avec l'état des anomalies non corrigées [V NEP déclarations écrites § 1-4 ; NEP anomalies § 15-17] ;
  - communiquer au directoire et au conseil de surveillance les modifications à apporter aux comptes, les irrégularités relevées et les conclusions des travaux, dont les **motifs de l'opinion** avant l'émission du rapport [V L. 821-63 I ; NEP rapport § 06].
- **Rôle de la note de synthèse (0,5 pt)** : document de fin de mission qui récapitule le seuil de signification, les anomalies relevées et leur correction ou non, les limitations de l'étendue des travaux et leurs incidences, puis la conclusion qui fonde l'opinion. Elle est revue par l'associée signataire et conservée au dossier : elle permet de comprendre les travaux et la conclusion [S, terme de pratique, F11 § 7 ; V NEP documentation § 04-08].

**b. Opinion (2 pts)**

*Existence d'une limitation (0,5 pt)*
- HALDÈNE n'a pas pu obtenir d'éléments suffisants et appropriés sur la paie de janvier à août, malgré des procédures alternatives (annexes 3.2 et 3.5) : c'est une **limitation de l'étendue des travaux**, due aux circonstances [V NEP rapport § 11, 14 ; NEP éléments probants § 5].
- Les arguments de M. STOEBER ne la font pas disparaître. Les relevés bancaires et les attestations des organismes sociaux prouvent les **montants globaux** versés, et leur concordance avec la comptabilité. Ils ne prouvent ni la **réalité** des rémunérations (qui a été payé, pour quel travail), ni leur **mesure** (montant dû à chacun), ni l'**exhaustivité** des heures et des cotisations. « La perte des fichiers » ne change pas les comptes, mais elle prive le commissaire aux comptes de la possibilité de les vérifier.

*Incidences non circonscrites (0,5 pt)*

| Élément non vérifié | Montant | Rapport au seuil (250 000 €) |
|---|---:|---|
| Masse salariale comptabilisée de janvier à août | 12 741 000 € | 51,0 fois ; 67,1 % des charges de personnel ; 24,6 % des charges d'exploitation |
| dont écart inexpliqué de la procédure analytique | 781 960 € | 3,1 fois ; 15,6 % du résultat courant avant impôt |
| Dettes provisionnées pour congés à payer estimées forfaitairement | 540 000 € | 2,2 fois |
| Charges de personnel incorporées au coût du MOSELLANE | 420 000 € | 1,7 fois |
| Heures supplémentaires et cotisations éventuellement dues | non estimable (96 000 € réclamés à ce jour) | inconnu |

- Les montants en cause sont des **multiples du seuil** et ne peuvent pas être chiffrés, même approximativement : ni le montant ni même le **sens** de l'erreur éventuelle ne sont connus.
- Ils touchent **plusieurs postes** : charges de personnel (premier poste de charges), immobilisations et amortissements (MOSELLANE), dettes sociales, charges à payer et provisions éventuelles, donc le résultat, l'impôt et les capitaux propres.
- Une réserve qui se bornerait à décrire ces éléments ne permettrait pas à l'utilisateur de juger des comptes **pris dans leur ensemble**.

*Conclusion (0,5 pt)* : HALDÈNE déclare qu'elle est dans l'**impossibilité de certifier** les comptes annuels 2026 de RIVÉLINE CROISIÈRES : la limitation a des incidences qui ne peuvent pas être circonscrites [V NEP rapport § 14 ; R. 821-180]. Le rapport expose les motifs dans la partie « Fondement de l'opinion » : destruction des données de paie, diligences mises en œuvre, montants concernés. Ces motifs sont communiqués au préalable au directoire et au conseil de surveillance [V NEP rapport § 06 ; L. 821-63 I]. L'anomalie non corrigée de 38 000 € reste inférieure au seuil et n'est significative ni par sa nature ni par les circonstances ; elle ne modifie pas l'opinion [V NEP caractère significatif § 9 ; NEP anomalies § 14].

*Opinions écartées (0,5 pt)*
- **Sans réserve** : impossible, une limitation significative subsiste.
- **Avec réserve pour limitation** : elle suppose des incidences **clairement circonscrites** et une réserve suffisante [V NEP rapport § 11]. Elle conviendrait si la perte avait porté, par exemple, sur un mois de paie des seuls permanents, pour un montant identifiable et limité. Ici, la limitation touche les deux tiers des charges de personnel et plusieurs postes.
- **Refus de certifier** : il sanctionne un **désaccord** : des anomalies significatives **identifiées** et non corrigées, dont les incidences ne sont pas circonscrites [V NEP rapport § 12-13]. Ici, la seule anomalie identifiée (38 000 €) est inférieure au seuil : le problème n'est pas une anomalie connue, mais l'absence d'éléments probants.

**c. Responsabilités en cas de certification sans réserve (1 pt)**
- **Civile (0,5 pt)** : le commissaire aux comptes est responsable, envers l'entité **et les tiers**, des conséquences dommageables de ses **fautes et négligences** [V L. 821-37]. Certifier sans réserve des comptes dont deux tiers des charges de personnel n'ont pas pu être vérifiés serait une faute : l'opinion ne reposerait pas sur des éléments suffisants et appropriés [V NEP principes § 08 ; NEP rapport § 14]. Les actionnaires, les investisseurs ou les prêteurs qui se fieraient à cette certification, puis subiraient un préjudice si les comptes se révélaient faux, pourraient demander des dommages-intérêts, en prouvant faute, préjudice et lien de causalité [S]. L'action se prescrit par trois ans à compter du fait dommageable ou de sa révélation s'il a été dissimulé [V L. 821-38, L. 225-254]. La demande de M. STOEBER n'exonère pas le cabinet : il est seul responsable de son opinion [S].
- **Disciplinaire (0,25 pt)** : une négligence grave ou un manquement aux normes est une faute disciplinaire, sanctionnée par la commission des sanctions de la H2A : avertissement, blâme, interdiction temporaire d'exercer, radiation, sanctions pécuniaires. Ces sanctions visent la société de commissaires aux comptes comme l'associée signataire [V L. 821-70 I, L. 821-71, L. 821-79].
- **Pénale (0,25 pt)** : les informations mensongères du commissaire aux comptes sur la situation de la personne morale sont un délit (cinq ans d'emprisonnement et 75 000 € d'amende) [V L. 821-9]. Ce délit suppose la conscience du caractère mensonger : certifier sans réserve tout en sachant que la paie n'a pas pu être vérifiée exposerait Mme KIRSCHER à des poursuites si les comptes se révélaient inexacts [S, appréciation de l'élément intentionnel]. La responsabilité pénale est d'abord personnelle [S].

**Réponses tolérées**
- Une réserve pour limitation, si le candidat chiffre toutes les incidences et discute leur caractère circonscrit : 1 pt sur les 2 pts du b (limitation et tableau des incidences). Le point de la conclusion et celui des opinions écartées ne sont pas accordés.
- Un raisonnement par « incertitudes multiples » pour les heures supplémentaires et les cotisations, s'il aboutit à l'impossibilité de certifier [V NEP rapport § 14].

**Erreurs fréquentes**
- Conclure au refus de certifier : il traduit un désaccord, pas une limitation (`JUR-A02`).
- Comparer au seuil la seule anomalie de 38 000 € et certifier sans réserve.
- Donner l'opinion sans ses motifs ni les montants concernés (`JUR-A02`, `JUR-F02`).
- Confondre la responsabilité disciplinaire (H2A) et la responsabilité pénale (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP anomalies § 8-17 ; NEP événements postérieurs § 01 ; NEP continuité d'exploitation § 2 ; NEP déclarations écrites § 1-4 ; C. com. L. 821-63 I | Travaux de fin de mission ; communication aux organes | [V] | F11 § 5 |
| Note de synthèse | Terme de pratique | [S] | F11 § 7 |
| NEP rapport § 06, 08, 11-14 ; C. com. R. 821-180 ; NEP caractère significatif § 9 | Quatre opinions ; limitation ; impossibilité | [V] ; application : [S] | F11 § 8 |
| C. com. L. 821-9, L. 821-37, L. 821-38, L. 225-254, L. 821-70 I, L. 821-71, L. 821-79 | Responsabilités civile, disciplinaire et pénale | [V] ; application : [S] | F09 § 7 |

---

### Partie B – Durabilité (12 points)

### 3.6 Architecture des ESRS, EFRAG, ISSB et GRI ; version applicable à l'exercice 2026 (4 pts)

**Architecture des ESRS (1,25 pt)**
- **Normes transversales (0,5 pt)** : l'**ESRS 1** fixe les **exigences générales** (principes d'établissement de l'état de durabilité, double matérialité, chaîne de valeur, horizons de temps, connectivité) ; l'**ESRS 2** fixe les **informations générales** à publier, quel que soit le résultat de l'analyse de matérialité, sur la gouvernance, la stratégie, la gestion des impacts, risques et opportunités (IRO), les indicateurs et les cibles [V ESRS 1 (2026) § 5, 8-10, 29 ; ESRS 1 (2023) § 29].
- **Normes thématiques (0,75 pt)** : environnement (E1 changement climatique, E2 pollution, E3 eau, E4 biodiversité et écosystèmes, E5 utilisation des ressources et économie circulaire) ; social (S1 personnel de l'entreprise, S2 travailleurs de la chaîne de valeur, S3 communautés affectées, S4 consommateurs et utilisateurs finaux) ; gouvernance (G1 conduite des affaires) [V annexe I du règlement délégué 2026/1563]. Elles s'appliquent **conjointement** avec les normes transversales, et seulement pour les thèmes **matériels**. Si un IRO matériel n'est pas couvert par une norme, l'entreprise publie des **informations spécifiques** [V ESRS 1 (2026) § 8-11, 29-30].

**Rôle de l'EFRAG (0,75 pt)** : l'EFRAG (European Financial Reporting Advisory Group) est le **conseiller technique** de la Commission européenne. Il prépare les projets d'ESRS et rend des avis techniques ; c'est la **Commission** qui adopte les ESRS par **règlements délégués** : règlement délégué (UE) 2023/2772 pour la première version, règlement délégué (UE) 2026/1563 pour les ESRS révisées [V règl. délégué 2026/1563, consid. 3 ; F12 § 1].

**ISSB, GRI et interopérabilité (1 pt)**

| Normalisateur | Normes | Approche de la matérialité |
|---|---|---|
| **ISSB**, au sein de la Fondation IFRS | **IFRS S1** (exigences générales) et **IFRS S2** (climat), publiées en juin 2023 [S] | **Financière** : risques et opportunités liés à la durabilité qui affectent les flux de trésorerie, l'accès au financement ou le coût du capital ; destinataires : investisseurs [S] |
| **GRI** (Global Reporting Initiative) | Normes universelles, normes par secteur et normes par thème [S] | **Impact** : impacts de l'entité sur l'économie, l'environnement et les personnes [S] |
| **EFRAG** / Commission (ESRS) | ESRS transversales et thématiques | **Double matérialité** : impact et financière [V] |

- **Interopérabilité** : déclaration commune de l'EFRAG et de la GRI (fin août et début septembre 2023) : définitions et indicateurs d'impact alignés, une entité qui publie selon les ESRS étant considérée comme publiant « with reference to » les normes GRI [V page EFRAG ; F12 § 1] ; guide d'interopérabilité de la Fondation IFRS et de l'EFRAG (mai 2024), qui aligne la matérialité financière des ESRS sur celle d'IFRS S1 [S]. Les ESRS révisées tiennent compte, dans toute la mesure du possible, de l'interopérabilité [V règl. délégué 2026/1563, consid. 2]. RIVÉLINE CROISIÈRES peut ajouter à son état de durabilité des informations issues d'autres référentiels, comme la GRI, en les signalant [V ESRS 1 (2026) § 107, 109].
- Formule de synthèse : GRI = impact ; ISSB = financier ; ESRS = double matérialité, qui réunit les deux angles [S, cohérent avec ESRS 1 (2026) § 2 et 23].

**Version applicable à l'exercice 2026 (1 pt)**
- Les ESRS révisées (règlement délégué 2026/1563) sont entrées en vigueur le 10/11/2026 ; elles sont **obligatoires pour les exercices commençant à compter du 01/01/2027** [V règl. délégué 2026/1563 art. 3].
- Pour l'exercice 2026, ouvert le 01/01/2026, RIVÉLINE CROISIÈRES peut **choisir** : appliquer les ESRS de 2023 (règlement délégué 2023/2772, tel que modifié en 2025), le cas échéant avec les allègements prévus, ou appliquer par anticipation les ESRS révisées [V règl. délégué 2026/1563 art. 2].
- Ce choix lui impose d'**indiquer clairement** dans l'état de durabilité la version appliquée [V règl. délégué 2026/1563 art. 2 ; S, application par analogie : RIVÉLINE publie volontairement selon les ESRS]. On valorise la remarque que le vocabulaire diffère (« double importance », « incidences », « déclaration relative à la durabilité » en 2023 ; « double matérialité », « impacts », « état de durabilité » en 2026) et que l'architecture est la même en substance [V F12 § 3.1].

**Réponses tolérées**
- Les intitulés des normes de 2023 (« effectifs de l'entreprise », « communautés touchées », « ressources aquatiques et marines »).
- La mention de la TCFD, dont les recommandations ont été intégrées dans IFRS S1 et S2 [S].

**Erreurs fréquentes**
- Présenter l'EFRAG comme l'auteur juridique des ESRS : c'est la Commission qui les adopte.
- Présenter comme à venir une troisième catégorie de normes, propre aux secteurs d'activité : les ESRS de 2023 la prévoyaient, mais sa base légale a été supprimée en 2026 [V F12 § 3.1, § 11].
- Discuter l'obligation de publier ou son calendrier, alors que l'énoncé les écarte par hypothèse (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 5, 8-11, 29-30, 107, 109 ; ESRS 1 (2023) § 29 ; annexe I du règl. délégué 2026/1563 | Architecture ; informations spécifiques ; autres référentiels | [V] | F12 § 3, 5 |
| Règl. délégué 2026/1563, consid. 2-3, art. 2-3 | Rôle de l'EFRAG ; interopérabilité ; version applicable | [V] | F12 § 1, 3.2 |
| Pages ISSB et GRI ; déclaration EFRAG-GRI (2023) ; guide IFRS-EFRAG (mai 2024) | Normalisateurs et interopérabilité | [S] / [V] | F12 § 1 |

### 3.7 Double matérialité, IRO, périmètre et connectivité (5 pts)

**Double matérialité (1 pt)**
- Un enjeu de durabilité est matériel s'il répond aux critères de la **matérialité d'impact**, de la **matérialité financière**, **ou des deux**. Les deux dimensions interagissent ; l'analyse part en général des impacts [V ESRS 1 (2023) § 28 ; ESRS 1 (2026) § 35-36].
- **Matérialité d'impact** : impacts positifs ou négatifs, réels ou potentiels, de l'entreprise sur la population ou l'environnement, liés à ses activités propres et à sa **chaîne de valeur**. Un impact négatif s'apprécie selon sa **gravité** (ampleur, étendue, caractère irrémédiable) et, s'il est potentiel, sa **probabilité** [V ESRS 1 (2026) § 39-40].
- **Matérialité financière** : enjeu qui a, ou dont on peut raisonnablement attendre qu'il ait, des **effets financiers** sur la situation financière, la performance, les flux de trésorerie, l'**accès au financement** ou le **coût du capital**, à court, moyen ou long terme, appréciés selon leur probabilité et leur ampleur. Ces risques et opportunités naissent des impacts, des **dépendances** à l'égard de ressources naturelles, humaines ou sociales, ou d'autres facteurs comme les aléas climatiques et les changements de réglementation [V ESRS 1 (2026) § 47-48, 50].

**Analyse des trois enjeux (1,5 pt, 0,5 pt par enjeu)**

| Enjeu | Nature | Dimension et analyse | Conclusion de la société |
|---|---|---|---|
| Émissions et rejets des bateaux | **Impact négatif réel** sur l'environnement et les populations riveraines : gaz à effet de serre et polluants atmosphériques (3 100 000 litres de gazole non routier ; groupes électrogènes à quai, au cœur des villes) ; eaux grises de deux bateaux rejetées après simple filtration. S'y ajoutent un **risque de transition** (restrictions d'accès de 2032, coût des remotorisations) et une **opportunité** (bateaux hybrides, raccordement à quai, attente des clients) | **Double matérialité** : gravité élevée par l'ampleur et l'étendue (villes d'escale), effets financiers probables et chiffrables | « matériel » : **justifiée** |
| Étiages et restrictions d'accès aux villes | **Risques** : risque **physique** lié au climat, qui naît de la **dépendance** de la société au niveau des fleuves (34 jours sans navigation, 11 croisières annulées ou écourtées, 1 900 000 € de coûts en 2026) ; risque de **transition** réglementaire (quais réservés aux bateaux sans moteur thermique à compter de 2032) | **Matérialité financière** : effets déjà constatés à court terme, aggravés à moyen et long terme | « non matériel, phénomène naturel » : **erronée**. Un risque peut exister sans impact préalable de l'entreprise, et un enjeu peut être matériel au seul titre de la matérialité financière [V ESRS 1 (2026) § 35-36, 48] |
| Conditions de travail des équipages saisonniers | **Impact négatif réel** sur le **personnel de l'entreprise** (thème S1) : accidents du travail en hausse (21 contre 14), journées de dix heures, logement en cabines partagées, heures supplémentaires réclamées ; impact potentiel sur la santé. S'y ajoutent des **risques** : litiges, cotisations, difficultés de recrutement (près d'un saisonnier sur trois part avant la fin de la saison) | **Matérialité d'impact** élevée ; matérialité financière à **réévaluer** | « matériel » : justifiée ; la matérialité financière « faible » est discutable au vu des litiges et du lien avec le cycle personnel et paie (3.2) |

**Périmètre de reporting (1,25 pt)**
- **Entreprise déclarante (0,25 pt)** : l'état de durabilité porte sur la même entité que les états financiers, ici RIVÉLINE CROISIÈRES seule, qui ne contrôle aucune société [V ESRS 1 (2026) § 60]. Ses **activités propres** comprennent le siège et ses neuf bateaux.
- **Bateaux affrétés (0,75 pt)** :
  - ces bateaux n'appartiennent pas à la société. L'armateur DORLAND VAART BV assure leur navigation, leur entretien et leur gestion, et emploie leurs équipages : RIVÉLINE CROISIÈRES n'a pas le **contrôle opérationnel**, c'est-à-dire la possibilité de diriger les activités opérationnelles de ces bateaux [V ESRS 2023, glossaire ; S, application] ;
  - ils relèvent donc de la **chaîne de valeur amont**, par une relation d'affaires directe avec l'armateur. Leur exclusion de l'analyse (« ils relèvent de l'armateur ») n'est pas acceptable : la société doit couvrir les IRO matériels de sa chaîne de valeur, ici les émissions de ces bateaux, qui portent 25 % des nuitées vendues (24 000 sur 96 000), et les conditions de travail de leurs équipages (thème S2, travailleurs de la chaîne de valeur). Faute de données de l'armateur, elle peut utiliser des **estimations** [V ESRS 1 (2026) § 39, 62-65].
- **Chaîne de valeur aval (0,25 pt)** : les déplacements en avion des clients résidant hors de l'Union (environ 60 %), liés à l'activité de la société, sont à examiner au titre de la chaîne de valeur aval [V ESRS 1 (2026) § 62 ; S, application].

**Connectivité avec les comptes annuels (1,25 pt)** [V ESRS 1 (2026) § 112-116]
- **Bateaux thermiques (0,5 pt)** : les restrictions d'accès de 2032 changent l'utilisation attendue des quatre bateaux thermiques que la société ne remotorisera pas (valeur nette comptable de 14 400 000 €, durée résiduelle de 12 ans). Il faut **réviser leur durée d'utilisation** et modifier le plan d'amortissement pour l'avenir, et apprécier si leur **valeur actuelle** est inférieure à leur valeur nette comptable, auquel cas ils sont **dépréciés** (règles de l'annexe 3.6). À titre d'illustration, si leur utilisation devait s'arrêter fin 2031, la dotation annuelle passerait de 1 200 000 € (14 400 000 / 12) à 2 880 000 € (14 400 000 / 5). Les hypothèses retenues dans l'état de durabilité (calendrier de sortie de flotte, plan de remotorisation de 2028 à 2030) doivent être **cohérentes** avec celles des comptes, et les différences expliquées [V § 116].
- **Étiages (0,25 pt)** : les 1 900 000 € de remboursements, transferts et nuits d'hôtel figurent dans le compte de résultat : **connexion indirecte**, à expliquer dans l'état de durabilité [V § 115].
- **Personnel (0,5 pt)** : les effectifs et les rémunérations publiés au titre du personnel de l'entreprise renvoient aux **charges de personnel** des comptes (19 000 000 €) : **connexion directe**, avec renvoi aux comptes [V § 114]. Les deux documents reposent sur les mêmes données de paie, perdues pour janvier à août : la limitation des comptes (3.5) touche aussi les informations sociales issues de la paie de janvier à août (heures travaillées et indicateurs de santé et de sécurité, voir 3.8). Les équipes de HALDÈNE qui vérifient les comptes et l'état de durabilité échangent sur ces points [V LD 2026 § 3.2 ; F12 § 9].

**Réponses tolérées**
- Le vocabulaire des ESRS de 2023 (« incidences », « double importance »).
- L'inclusion des bateaux affrétés dans les activités propres, si le candidat soutient que la société a le contrôle opérationnel parce qu'elle fixe les itinéraires et les escales, et en tire la conséquence (couverture de leurs émissions) : 0,5 pt sur les 0,75 pt du point. La conclusion commune, que ces bateaux ne peuvent pas être exclus, est l'essentiel.
- La connectivité traitée sans le calcul d'illustration, qui n'est pas exigé.

**Erreurs fréquentes**
- Confondre impact (effet de l'entreprise sur son environnement) et risque (effet de l'environnement sur l'entreprise) (`JUR-A01`).
- Accepter la conclusion de la société sur les étiages, faute de voir qu'un risque peut être matériel sans impact préalable.
- Analyser des enjeux sans exploiter les chiffres de l'annexe 3.6 (`JUR-F07`, `JUR-A05`).
- Développer le contenu détaillé des normes thématiques, qui n'est pas attendu.

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2023) § 28 ; ESRS 1 (2026) § 35-36, 39-40, 47-48, 50 | Double matérialité ; gravité ; effets financiers ; dépendances | [V] | F12 § 6 |
| ESRS 1 (2026) § 60, 62-65 ; ESRS 2023, glossaire (contrôle opérationnel) | Entreprise déclarante ; chaîne de valeur ; estimations | [V] ; application : [S] | F12 § 7 |
| ESRS 1 (2026) § 112-116 ; LD 2026 § 3.2 | Connectivité ; échanges avec le commissaire aux comptes | [V] | F12 § 9 ; F13 § 3 |
| Règles comptables de l'annexe 3.6 | Durée d'utilisation ; dépréciation | données de l'énoncé | — |

### 3.8 Assurance limitée ; avis sur les axes 1 et 2 (3 pts)

**Nature de l'assurance et objectifs de la mission (1 pt)**
- **Assurance limitée (0,5 pt)** : HALDÈNE émet son avis sur la base d'une **assurance limitée** [V LD 2026, niveau d'assurance ; dir. 2013/34 art. 34]. Ses vérifications sont moindres en **nature**, en **étendue** et en **durée** que celles d'une assurance raisonnable, et sa conclusion est exprimée sous une **forme négative** : elle n'a pas relevé d'erreurs, omissions ou incohérences importantes. La certification des comptes, elle, repose sur une assurance raisonnable exprimée sous une forme positive [V LD 2026 ; NEP principes § 08].
- **Objectifs (0,5 pt)** : l'avis porte sur quatre axes [V L. 821-54 II ; LD 2026 § 2] :
  1. la conformité aux ESRS du **processus** de détermination des informations publiées (double matérialité) et, lorsque l'entité y est soumise, la consultation du comité social et économique (sans objet ici, par hypothèse : RIVÉLINE publie volontairement) [S, F12 § 11.3 (b)] ;
  2. la conformité des **informations** publiées aux ESRS ;
  3. le respect des exigences de publication liées à la taxonomie ;
  4. à terme, le balisage électronique, non exigible tant que ses règles ne sont pas adoptées.

  Par hypothèse, seuls les deux premiers axes sont en cause. Le rapport est organisé par axe, avec un avis pour chacun [V LD 2026 § 17].

**Axe 1 – processus de détermination des informations (1 pt)**
- **Constat** : le directoire a corrigé l'évaluation des étiages, mais refuse d'étendre l'analyse aux trois bateaux affrétés et à leurs équipages. Cette omission **non corrigée** remet en cause la conformité du processus aux ESRS : la chaîne de valeur doit être couverte pour les IRO matériels (voir 3.7) [V ESRS 1 (2026) § 62-65].
- **Incidences circonscrites** : le défaut est isolé et précisément identifiable (trois bateaux, 25 % des nuitées, deux enjeux : émissions et conditions de travail des équipages). Le reste du processus est conforme : étiages évalués et chaîne de valeur aval couverte après la demande de HALDÈNE, parties prenantes consultées, IRO décrits, seuils justifiés. Une réserve motivée suffit à l'utilisateur pour fonder son jugement.
- **Avis** : **avis de conformité assorti d'une réserve motivée**, qui décrit l'exclusion des bateaux affrétés [V LD 2026 § 17 ; S, jugement professionnel, F13 § 4.3 et 4.5].

**Axe 2 – informations publiées (1 pt)**
- **Constat** : HALDÈNE n'a pu obtenir aucun élément sur les heures réellement travaillées de janvier à août 2026, ni donc sur les indicateurs de santé et de sécurité calculés à partir d'elles : c'est une **limitation** de ses vérifications. Que l'état de durabilité indique la méthode d'estimation ne la supprime pas : les réclamations des saisonniers mettent précisément en doute la fiabilité des plannings.
- **Incidences circonscrites** : la limitation porte sur des indicateurs identifiés d'un seul thème. Les autres informations sociales (effectifs, contrats, départs), et toutes les autres informations, ont été vérifiées sans erreur. Le montant des charges de personnel est repris des comptes annuels (connexion directe) : sa fiabilité relève de l'audit des comptes, et l'impossibilité de certifier peut être rappelée dans un paragraphe d'observation ou de renvoi.
- **Avis** : **avis de conformité assorti d'une réserve motivée** pour limitation [V LD 2026 § 17]. Le contraste avec les comptes annuels est instructif : la même perte de données conduit à une **impossibilité de certifier** les comptes, parce que ses incidences n'y sont pas circonscrites (3.5), mais à une simple **réserve** sur l'état de durabilité, parce qu'elle n'y touche que quelques indicateurs.

**Réponses tolérées**
- Un avis de **non-conformité** sur l'axe 1, si le candidat soutient que l'exclusion d'un quart de l'activité et de toute la chaîne de valeur amont empêche de circonscrire les incidences : 0,5 pt sur 1 pt. Aucun texte n'impose l'une ou l'autre qualification [S, F13 § 4.5].
- Une réserve de l'axe 2 étendue aux charges de personnel reprises des comptes, si l'avis reste une réserve motivée : points accordés.
- Le vocabulaire « auditeur de durabilité » ou « vérificateur ».

**Erreurs fréquentes**
- Transposer l'impossibilité de certifier les comptes à l'état de durabilité, sans apprécier séparément le caractère circonscrit de la limitation.
- Émettre un avis global au lieu d'un avis par axe.
- Présenter l'assurance limitée comme une assurance raisonnable « allégée » exprimée sous une forme positive (`JUR-A01`).
- Accorder une simple observation sur l'axe 2 : une observation n'est possible qu'avec un avis de conformité, en l'absence de limitation non résolue [V LD 2026 § 17 ; F13 § 4.4].

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II ; dir. 2013/34 art. 34 ; LD 2026, niveau d'assurance, § 2 | Objet de l'avis ; axes ; assurance limitée | [V] | F13 § 2 |
| LD 2026 § 17 | Structure par axe ; quatre avis ; observations | [V] | F13 § 4.1-4.4 |
| Table de décision ; qualification du défaut de processus | Application | [S, jugement professionnel] | F13 § 4.3, 4.5 |
| NEP principes § 08 | Assurance raisonnable des comptes | [V] | F11 § 1.1 |
