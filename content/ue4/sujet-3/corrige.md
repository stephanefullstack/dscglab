# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 3

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F13 (`ue4/fiches/`, à jour au 22 ou 23/10/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.6 | `exercices/ex05_consolidation_ifrs` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.8 | `exercices/ex02_apport_partiel` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.12 | `exercices/ex06_audit_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Périmètre IFRS | `2.1.c` Définir le périmètre de consolidation | 5 |
| 1.2 a Monnaie fonctionnelle et méthode | `2.2.e` Convertir des comptes établis en devises | 2 |
| 1.2 b Conversion du bilan et du résultat | `2.2.e` Convertir des comptes établis en devises | 4 |
| 1.2 c Écart de conversion | `2.2.e` Convertir des comptes établis en devises | 2 |
| 1.2 d Élimination des titres KESTREL | `2.2.h` Partage des capitaux propres | 2 |
| 1.3 IFRS 16 | `2.2.c` Homogénéisation, thèmes communs | 7 |
| 1.4 IAS 19 | `2.2.c` Homogénéisation, thèmes communs | 5 |
| 1.5 IAS 20 | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 6 |
| 1.6 a Goodwill CORALIS | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.6 b Tableau de mise en équivalence | `2.2.h` Partage des capitaux propres (MEE) | 4 |
| 1.6 c Écritures CORALIS | `2.2.h` Partage des capitaux propres (MEE) | 3 |
| 1.6 d Évolution des titres mis en équivalence | `2.2.h` Partage des capitaux propres (MEE) | 2 |
| **Total** | | **45** |

---

### 1.1 Périmètre IFRS au 31/12/2026 (5 pts)

**Référentiel (1 pt).** Les actions de NORDAL sont admises sur un marché réglementé d'un État membre : ses comptes consolidés sont obligatoirement établis selon les IFRS adoptées par l'Union européenne [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. NORDAL contrôle KESTREL et ARMOR, elle est donc tenue de consolider [V C. com. L. 233-16 ; IFRS 10 § 4].

**Tableau (4 pts, 1 pt par société, justification comprise)**

| Société | % de contrôle | Nature | Méthode | % d'intérêt |
|---|---|---|---|---|
| NORDAL | — | Mère | — | 100 % |
| KESTREL | 70 % | Contrôle (filiale) | Intégration globale | 70 % (PNC 30 %) |
| ARMOR | 90 % | Contrôle (filiale) | Intégration globale | 90 % (PNC 10 %) |
| CORALIS | 30 % | Influence notable | Mise en équivalence | 30 % |
| VESTA | **12 %** | Aucune | Non consolidée | — |

**Justifications**
- **KESTREL et ARMOR** : la majorité des droits de vote, sans pacte contraire, donne à NORDAL le pouvoir sur les activités, l'exposition aux rendements variables et la capacité d'agir sur eux [V IFRS 10 § 7]. Intégration globale, les participations ne donnant pas le contrôle (PNC) étant présentées séparément dans les capitaux propres [V IFRS 10 § 22]. Le fait que KESTREL soit étrangère et hors zone euro ne change ni le contrôle ni la méthode : seule la conversion de ses comptes s'ajoute.
- **CORALIS** : 30 % des droits de vote, au-delà de la présomption de 20 %, confirmée par la représentation au conseil et la participation aux décisions de politique financière et opérationnelle [V IAS 28 § 5 et 6]. Mise en équivalence [V IAS 28 § 16].
- **VESTA** : seuls comptent les droits détenus directement par NORDAL ou par ses filiales [V IAS 28 § 5, « par exemple par le biais de filiales »]. Les 10 % détenus par CORALIS, entreprise associée, ne s'ajoutent pas, ni pour l'influence ni pour l'intérêt [V IAS 28 § 27 ; F03 § 4.2]. Avec 12 %, sans représentation ni relations significatives, l'influence notable est présumée absente : VESTA est hors périmètre.

---

### 1.2 Conversion des comptes de KESTREL (10 pts)

#### a. Monnaie fonctionnelle et méthode (2 pts)

**Monnaie fonctionnelle (1 pt).** C'est la monnaie de l'environnement économique principal, celui dans lequel l'entité génère et dépense principalement sa trésorerie [V IAS 21 § 9]. Pour KESTREL, tous les indicateurs désignent la **livre sterling** :
- prix de vente libellés en GBP et fixés par la concurrence britannique [V § 9 a)] ;
- personnel et fournisseurs réglés en GBP [V § 9 b)] ;
- financement par emprunt en GBP et trésorerie conservée en GBP [V § 10] ;
- activité autonome, sans transaction avec le groupe [V § 11 a) et b)].

**Méthode (1 pt).** La monnaie fonctionnelle (GBP) diffère de la monnaie de présentation du groupe (euro). Les comptes sont convertis selon la **méthode du cours de clôture** : actifs et passifs au cours de clôture, produits et charges au cours des dates de transaction, approché par le cours moyen puisque les cours ont évolué régulièrement, capitaux propres au cours historique, écarts en autres éléments du résultat global [V IAS 21 § 39 et 40 ; F04 R13]. Il n'y a qu'un exercice à convertir (création le 01/01/2026) : le capital est converti au cours du 01/01/2026.

#### b. Bilan et compte de résultat convertis (4 pts)

**Bilan au 31/12/2026 (2 pts)**

| Poste | GBP | Cours | € |
|---|---:|---:|---:|
| Immobilisations corporelles nettes | 2 600 000 | 1,14 | 2 964 000 |
| Stocks | 500 000 | 1,14 | 570 000 |
| Créances clients | 700 000 | 1,14 | 798 000 |
| Trésorerie | 200 000 | 1,14 | 228 000 |
| **Total actif** | **4 000 000** | | **4 560 000** |
| Capital | 2 000 000 | 1,20 (historique) | 2 400 000 |
| Résultat 2026 | 375 000 | 1,16 (moyen) | 435 000 |
| **Écart de conversion** | — | | **– 127 500** |
| Emprunts | 1 000 000 | 1,14 | 1 140 000 |
| Fournisseurs | 450 000 | 1,14 | 513 000 |
| Dettes fiscales et sociales | 175 000 | 1,14 | 199 500 |
| **Total passif** | **4 000 000** | | **4 560 000** |

**Compte de résultat 2026 (2 pts)**

| Poste | GBP | Cours | € |
|---|---:|---:|---:|
| Chiffre d'affaires | 6 000 000 | 1,16 | 6 960 000 |
| Achats consommés | – 3 300 000 | 1,16 | – 3 828 000 |
| Charges de personnel | – 1 500 000 | 1,16 | – 1 740 000 |
| Autres charges externes | – 360 000 | 1,16 | – 417 600 |
| Dotations aux amortissements | – 300 000 | 1,16 | – 348 000 |
| Charges financières | – 40 000 | 1,16 | – 46 400 |
| Impôt sur les bénéfices | – 125 000 | 1,16 | – 145 000 |
| **Résultat net** | **375 000** | | **435 000** |

Les dotations aux amortissements sont converties au cours moyen, comme les autres charges : la méthode du cours de clôture n'utilise pas de cours historique pour les produits et charges [V IAS 21 § 39 b) ; F04 R13].

#### c. Écart de conversion (2 pts)

**Calcul et origine (1 pt).** Écart = 4 560 000 – 1 852 500 de dettes – 2 400 000 – 435 000 = **– 127 500 €**. Il provient [V IAS 21 § 41] :

| Origine | Calcul | Montant |
|---|---|---:|
| Capital converti au cours historique, actif net correspondant au cours de clôture | 2 000 000 × (1,14 – 1,20) | – 120 000 |
| Résultat converti au cours moyen, actif net correspondant au cours de clôture | 375 000 × (1,14 – 1,16) | – 7 500 |
| **Total** | | **– 127 500** |

La livre s'est dépréciée face à l'euro : l'actif net de KESTREL vaut moins en euros à la clôture qu'aux dates où il a été constitué.

**Traitement (1 pt).** L'écart est comptabilisé en **autres éléments du résultat global**, et non en résultat, puis cumulé dans une composante distincte des capitaux propres (réserve de conversion) jusqu'à la sortie de l'établissement à l'étranger, où il sera reclassé en résultat [V IAS 21 § 39 c), 41 et 48 ; F04 R13]. Il fait partie des éléments recyclables de l'état du résultat global [V IAS 1 § 7 c) et 82A]. <!-- ue4check:ignorer -->
La part des PNC leur est affectée [V IAS 21 § 41 ; IFRS 10 B94] :
- part du groupe : 70 % × – 127 500 = **– 89 250 €** ;
- PNC : 30 % × – 127 500 = **– 38 250 €**.

#### d. Élimination des titres et partage (2 pts)

Titres KESTREL chez NORDAL : 70 % × 2 000 000 GBP × 1,20 = **1 680 000 €**. NORDAL a souscrit à la création au prix de la quote-part du capital : pas de goodwill. Les titres sont éliminés contre la part du groupe dans les capitaux propres [V IFRS 10 B86 b)].

| | Total | Groupe 70 % | PNC 30 % |
|---|---:|---:|---:|
| Capital | 2 400 000 | 1 680 000 | 720 000 |
| – Titres éliminés | | – 1 680 000 | |
| Écart de conversion | – 127 500 | – 89 250 | – 38 250 |
| Résultat | 435 000 | 304 500 | 130 500 |
| **Total** | **2 707 500** | **215 250** | **812 250** |

**K1 (bilan)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.KESTREL Capital KESTREL | 2 400 000 | |
| RST.KESTREL Résultat KESTREL | 435 000 | |
| ECV_G Écart de conversion – part du groupe | 89 250 | |
| ECV_M Écart de conversion – PNC | 38 250 | |
| ECV.KESTREL Écart de conversion KESTREL | | 127 500 |
| 261.NORDAL Titres KESTREL | | 1 680 000 |
| RST_G Résultat consolidé – part du groupe | | 304 500 |
| RSV_M PNC – capital et réserves | | 720 000 |
| RST_M PNC – résultat | | 130 500 |
| **Total** | **2 962 500** | **2 962 500** |

---

### 1.3 Contrat de location d'ARMOR — IFRS 16 (7 pts)

Les comptes de consolidation sont ceux de `comptes_conso.yaml` : `DU` / `AMO_DU` = droit d'utilisation et ses amortissements ; `DL` = dette locative ; `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge d'impôt différé ; `RES_CR` = contrepartie au compte de résultat.

**Principe (1,5 pt).** IFRS 16 ne distingue pas, chez le preneur, location simple et location-financement. À la date de prise d'effet, il comptabilise un **droit d'utilisation** et une **dette locative** [V IFRS 16 § 22], sauf exemption courte durée ou faible valeur, ici écartée [V § 5]. La dette est égale à la valeur actualisée des loyers non versés, au taux implicite ou, à défaut, au taux d'emprunt marginal (4 %) : 1 050 000 € [V § 26]. Le droit d'utilisation est évalué au coût, soit le montant de la dette en l'absence de loyers d'avance, de coûts directs et de coûts de remise en état [V § 23 et 24]. Il est amorti sur la durée du contrat, plus courte que la durée d'utilité de l'entrepôt et sans transfert de propriété : 1 050 000 / 6 = **175 000 €** par an [V § 31 et 32]. La dette augmente des intérêts et diminue des loyers payés [V § 36]. Au compte de résultat, le loyer est remplacé par une dotation aux amortissements et une charge d'intérêts présentées séparément [V § 49]. Les loyers étant déductibles lors du paiement, le droit d'utilisation et la dette ont une base fiscale nulle : un IDP sur le premier et un IDA sur la seconde sont comptabilisés, l'exemption de comptabilisation initiale ne s'appliquant pas [V IAS 12 § 22A et 24 ; F04 R2], puis compensés, car ils concernent la même entité et la même administration fiscale [V IAS 12 § 74].

**Incidence (2 pts)**

| | Réserves (exercice 2025) | Résultat (exercice 2026) | Bilan au 31/12/2026 |
|---|---:|---:|---:|
| Annulation du loyer | + 200 300 | + 200 300 | |
| Dotation aux amortissements | – 175 000 | – 175 000 | DU 1 050 000 – AMO_DU 350 000 = 700 000 |
| Intérêts sur la dette locative | – 42 000 | – 35 668 | DL 727 068 |
| **Avant impôt** | **– 16 700** | **– 10 368** | 700 000 – 727 068 = **– 27 068** |
| Impôt différé (25 %) | + 4 175 | + 2 592 | IDA net 6 767 |
| **Net** | **– 12 525** | **– 7 776** | |

Contrôle de l'impôt différé : IDA sur la dette 727 068 × 25 % = 181 767 ; IDP sur le droit d'utilisation 700 000 × 25 % = 175 000 ; net **6 767** = 4 175 + 2 592.

**L1 (bilan, 2 pts)** : débit DU Droit d'utilisation 1 050 000 ; débit IDA 6 767 ; débit RSV.ARMOR 12 525 ; débit RST.ARMOR 7 776 ; crédit AMO_DU Amortissements du droit d'utilisation 350 000 ; crédit DL Dette locative 727 068. Total 1 077 068.

**L1R (compte de résultat, 1,5 pt)** : débit 6811 Dotations aux amortissements 175 000 ; débit 6611 Intérêts des emprunts et dettes 35 668 ; crédit 6132 Locations immobilières 200 300 ; crédit CH_ID Produit d'impôt différé 2 592 ; crédit RES_CR Résultat 7 776. Total 210 668.

L'impact sur les capitaux propres d'ARMOR (– 20 301) est ensuite partagé avec ses PNC (10 %) lors de l'élimination des titres ARMOR, qui n'est pas demandée.

---

### 1.4 Engagements de retraite de NORDAL — IAS 19 (5 pts)

**Principe (1,5 pt).** Le régime est à prestations définies : l'obligation est évaluée selon la méthode des unités de crédit projetées et comptabilisée au passif, l'option des comptes individuels n'existant pas en IFRS [V IAS 19 § 57 ; F04 R8]. Le coût des services et les intérêts nets vont en **résultat** ; les réévaluations, dont les écarts actuariels, vont en **autres éléments du résultat global** [V IAS 19 § 120 et 127] et ne sont jamais reclassées en résultat [V § 122]. Intérêts nets : 240 000 × 3,5 % = **8 400 €** [V § 123]. L'indemnité n'étant déductible qu'au versement, la provision a une base fiscale nulle et crée un **impôt différé actif** [V IAS 12 § 26 a)], dont la part liée aux écarts actuariels suit les autres éléments du résultat global [V IAS 12 § 61A a) ; F04 R8].

**Incidence (1,5 pt)**

| | Réserves (obligation au 31/12/2025) | Résultat 2026 (30 000 + 8 400) | Autres éléments du résultat global 2026 | Bilan au 31/12/2026 |
|---|---:|---:|---:|---:|
| Avant impôt | – 240 000 | – 38 400 | – 21 600 | Provision 300 000 |
| Impôt différé (25 %) | + 60 000 | + 9 600 | + 5 400 | IDA 75 000 |
| **Net** | **– 180 000** | **– 28 800** | **– 16 200** | |

Contrôle : 240 000 + 30 000 + 8 400 + 21 600 = 300 000.

**Écritures (2 pts)**

**R1 (bilan)** : crédit 1521 Provisions pour pensions et obligations similaires 300 000 ; débit IDA 75 000 ; débit RSV.NORDAL 180 000 ; débit RST.NORDAL 28 800 ; débit RSV.NORDAL (écarts actuariels 2026, autres éléments du résultat global) 16 200.

**R1R (compte de résultat)** : débit 6815 Dotations aux provisions d'exploitation (coût des services) 30 000 ; débit 6865 Dotations aux provisions financières (intérêts nets) 8 400 ; crédit CH_ID 9 600 ; crédit RES_CR 28 800.

**État du résultat global (autres éléments, non recyclables)** : réévaluation du passif au titre des prestations définies – 21 600 ; impôt + 5 400 ; **net – 16 200**. Aucun code de consolidation n'existe pour ces autres éléments : ils ne transitent pas par le compte de résultat (pas de ligne RES_CR) et sont cumulés au bilan dans les réserves, en pratique dans une rubrique distincte, ce que permet IAS 19 § 122.

---

### 1.5 Subvention d'investissement d'ARMOR — IAS 20 (6 pts)

**Principe (1,5 pt).** IAS 20 retient l'approche par le résultat : la subvention est comptabilisée en résultat de façon systématique sur les périodes où sont comptabilisées les charges qu'elle compense, ici les amortissements de la ligne [V IAS 20 § 12, 13 et 17]. Ne provenant pas des actionnaires, elle ne peut pas rester en capitaux propres [V § 15 a)], contrairement au traitement du PCG (comptes 131 et 139) [V F04 R10]. Au bilan, une subvention liée à un actif est présentée soit en produits différés, soit **en déduction de la valeur comptable de l'actif** [V § 24], méthode du groupe : elle est alors reprise en résultat par une **réduction de la dotation aux amortissements** [V § 27].

**Données**

| | Comptes individuels | IFRS (subvention déduite) |
|---|---:|---:|
| Coût de la ligne | 480 000 | 360 000 |
| Dotation annuelle | 60 000 | 45 000 |
| Quote-part de subvention en résultat (747) | 15 000 | — |
| Charge nette annuelle | 45 000 | 45 000 |
| VNC au 31/12/2026 | 360 000 | 270 000 |
| Subvention nette en capitaux propres | 90 000 | — |

**S1 (bilan, 1,5 pt)** : débit 131 Subventions d'investissement octroyées 120 000 ; débit 28154 Amortissements du matériel industriel 30 000 ; crédit 139 Subventions d'investissement inscrites au compte de résultat 30 000 ; crédit 2154 Matériels industriels 120 000. Total 150 000.

**S1R (compte de résultat, 1 pt)** : débit 747 Quote-part des subventions d'investissement virée au résultat 15 000 ; crédit 6811 Dotations aux amortissements 15 000.

**Incidence (2 pts)**
- **Capitaux propres** : la subvention nette de 90 000 € sort des capitaux propres d'ARMOR ; l'actif net diminue d'autant (VNC 270 000 au lieu de 360 000).
- **Réserves et résultat** : aucune incidence. Le résultat 2025 et celui de 2026 supportent chacun 45 000 € de charge nette dans les deux référentiels ; seule la présentation change (dotation réduite au lieu d'un produit 747).
- **Impôt différé** : aucun impôt différé net. La ligne a une valeur IFRS de 270 000 € et une base fiscale de 360 000 € (déductions futures), soit une différence déductible de 90 000 € (IDA 22 500) ; la subvention restant à imposer (90 000 €) est une différence imposable (IDP 22 500) [V IAS 12 § 7 et 9]. Les deux se compensent [V IAS 12 § 74] : produits et charges sont reconnus au même rythme comptablement et fiscalement, conformément à l'hypothèse fiscale de l'énoncé.

---

### 1.6 Mise en équivalence de CORALIS (12 pts)

#### a. Actif net à la juste valeur et goodwill (3 pts)

**Actif net identifiable au 01/01/2025 (2 pts)**

| Élément | Montant |
|---|---:|
| Capitaux propres de CORALIS (1 000 000 + 1 400 000) | 2 400 000 |
| Écart d'évaluation sur le bâtiment (1 000 000 – 600 000) | + 400 000 |
| Impôt différé passif sur l'écart (25 %) | – 100 000 |
| **Actif net à la juste valeur** | **2 700 000** |

L'acquisition d'une participation dans une entreprise associée suit les concepts de l'acquisition d'une filiale [V IAS 28 § 26] : les actifs identifiables sont évalués à la juste valeur et l'impôt différé sur l'écart est constaté [V IFRS 3 § 24 ; IAS 12 § 66 ; F05 § 2].

**Goodwill (1 pt)** : 1 000 000 – 30 % × 2 700 000 = 1 000 000 – 810 000 = **190 000 €**. Il est **inclus dans la valeur des titres mis en équivalence** et n'est pas amorti [V IAS 28 § 32 a) ; F05 § 4]. Aucune perte de valeur n'est signalée par l'énoncé.

#### b. Tableau de mise en équivalence au 31/12/2026 (4 pts)

**Écart d'évaluation au 31/12/2026 (1 pt).** Le bâtiment est amorti sur la base de sa juste valeur : la quote-part du résultat est ajustée de l'amortissement complémentaire de l'écart [V IAS 28 § 32, dernier alinéa].

| | Réserves (2025) | Résultat (2026) | Cumul au 31/12/2026 |
|---|---:|---:|---:|
| Écart d'évaluation brut | + 400 000 | | 400 000 |
| Amortissement complémentaire (400 000 / 10) | – 40 000 | – 40 000 | – 80 000 |
| Impôt différé (25 %) | – 90 000 | + 10 000 | – 80 000 |
| **Net** | **+ 270 000** | **– 30 000** | **240 000** |

**Capitaux propres retraités et valeur des titres (2 pts)**

| | Capital et réserves | Résultat | Total |
|---|---:|---:|---:|
| Comptes individuels | 2 600 000 | 300 000 | 2 900 000 |
| Écart d'évaluation net | + 270 000 | – 30 000 | + 240 000 |
| **Capitaux propres retraités** | **2 870 000** | **270 000** | **3 140 000** |
| Quote-part du groupe (30 %) | 861 000 | 81 000 | **942 000** |
| + Goodwill | | | + 190 000 |
| **Titres mis en équivalence** | | | **1 132 000** |

**Répartition (1 pt)**

| Élément | Montant |
|---|---:|
| Titres CORALIS éliminés (coût) | 1 000 000 |
| Réserves consolidées – part du groupe (861 000 + 190 000 – 1 000 000) | **51 000** |
| Résultat consolidé – part du groupe | **81 000** |
| **Total = titres mis en équivalence** | **1 132 000** |

Contrôle : réserves groupe = 30 % × (2 870 000 – 2 700 000 d'actif net à l'acquisition) = 30 % × 170 000 = 51 000 €.

#### c. Écritures (3 pts)

**Dividende (1 pt).** NORDAL a encaissé 30 % × 80 000 = **24 000 €**, inscrits en produits. En mise en équivalence, les distributions reçues réduisent la valeur des titres [V IAS 28 § 10] : déjà prises en compte dans la valeur d'équivalence (réserves de CORALIS diminuées de 80 000), elles sont éliminées du résultat de NORDAL et reclassées en réserves.

**M1 (bilan)** : débit RST.NORDAL 24 000 ; crédit RSV.NORDAL 24 000.
**M1R (compte de résultat)** : débit 761 Produits de participations 24 000 ; crédit RES_CR 24 000.

**Mise en équivalence (2 pts)**

**M2 (bilan)**

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence (goodwill compris) | 1 132 000 | |
| 261.NORDAL Titres de participation CORALIS | | 1 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 51 000 |
| RST_G Résultat consolidé – part du groupe | | 81 000 |
| **Total** | **1 132 000** | **1 132 000** |

**M2R (compte de résultat)** : débit RES_CR 81 000 ; crédit QP_MEE Quote-part dans le résultat des entreprises mises en équivalence 81 000.

L'impôt différé et l'écart d'évaluation de CORALIS ne figurent pas au bilan consolidé : ils sont compris dans la valeur des titres mis en équivalence.

#### d. Évolution de la valeur des titres mis en équivalence (2 pts)

| Élément | Montant |
|---|---:|
| Coût d'acquisition au 01/01/2025 (dont goodwill 190 000) | 1 000 000 |
| + Quote-part du résultat retraité 2025 : 30 % × (280 000 – 30 000) | + 75 000 |
| **Titres mis en équivalence au 31/12/2025** | **1 075 000** |
| – Dividendes reçus en 2026 | – 24 000 |
| + Quote-part du résultat retraité 2026 : 30 % × 270 000 | + 81 000 |
| **Titres mis en équivalence au 31/12/2026** | **1 132 000** |

La participation suit la quote-part de l'actif net retraité de CORALIS, augmentée du goodwill : comptabilisée au coût, elle augmente de la quote-part du résultat et diminue des distributions [V IAS 28 § 10]. Le goodwill (190 000 €) reste inclus et constant [V IAS 28 § 32 a)]. Les réserves consolidées (51 000 + 24 000 reclassés par M1 = 75 000) correspondent à la quote-part du résultat 2025. En règlement ANC 2020-01, l'écart d'acquisition serait présenté selon les modalités de l'intégration globale [V art. 262-2 ; F05 § 5].

---

### Réponses tolérées
- **1.1** : un « % minoritaires » de 0 % présenté pour CORALIS (contrôle – intérêt), selon la présentation du corrigé du sujet zéro.
- **1.2 b** : écart de conversion présenté parmi les capitaux propres sous l'intitulé « réserve de conversion ».
- **1.2 d** : élimination des titres et partage de l'écart de conversion en deux écritures distinctes, si les montants sont justes.
- **1.3** : IDA (181 767) et IDP (175 000) présentés séparément au lieu du montant net de 6 767 ; écriture de bilan scindée entre l'impact 2025 (réserves) et l'impact 2026 (résultat).
- **1.4** : écarts actuariels nets (16 200) portés sur une ligne « autres éléments du résultat global » ou « réserves – écarts actuariels », si le candidat indique qu'ils ne transitent pas par le résultat.
- **1.5** : constat de l'IDA et de l'IDP de 22 500 chacun, sans compensation, s'ils sont justifiés.
- **1.6 c** : écritures M1 et M2 regroupées (titres mis en équivalence 1 132 000 ; réserves groupe 75 000 ; résultat NORDAL – 24 000 ; résultat groupe 81 000).

### Erreurs fréquentes
- **Tableau de mise en équivalence sans l'écart d'évaluation ou sans le goodwill** : valeur des titres limitée à 30 % × 2 900 000 = 870 000 €, au lieu de 1 132 000 €. C'est l'erreur relevée par le jury en 2025 (`JUR-G03`). L'amortissement complémentaire de l'écart, en réserves pour 2025 et en résultat pour 2026, est aussi souvent oublié.
- **Goodwill d'une entreprise associée présenté à part** (ligne « écart d'acquisition » de l'ANC) au lieu d'être inclus dans les titres mis en équivalence (IAS 28 § 32 a).
- **Dividende CORALIS laissé dans le résultat de NORDAL**, ou titres mis en équivalence non diminués de la distribution.
- **VESTA mise en équivalence** avec 22 % de droits de vote, en ajoutant les 10 % détenus par l'entreprise associée CORALIS.
- **Conversion** : dotations aux amortissements converties au cours historique (méthode du cours historique appliquée à tort), capital converti au cours de clôture, ou écart de conversion porté en résultat. Écart non partagé avec les PNC.
- **Réserves et résultat confondus** (IFRS 16, IAS 19) : impact 2025 porté en résultat 2026. Le jury relève une méthodologie de passage aux comptes consolidés mal maîtrisée et des retraitements peu justifiés (`JUR-G01`, `JUR-G04`, `JUR-G06`). Le gabarit « réserves / résultat / bilan » est recommandé (`JUR-F05`).
- **IAS 19** : écarts actuariels passés en résultat, ou impôt différé sur ces écarts imputé en résultat.
- **IAS 20** : subvention maintenue en capitaux propres, ou impôt différé net constaté alors que les rythmes comptable et fiscal coïncident.
- **Écritures déséquilibrées ou sans libellé** : un contrôle d'équilibre est attendu pour chaque écriture (`JUR-F03`, `JUR-F04`).

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
| 3.1 Expert-comptable et commissaire aux comptes | `3.1.a` Cadres d'exercice (et `3.1.c` indépendance) | 2,5 |
| 3.2 Nomination obligatoire d'un commissaire aux comptes | `3.1.b` Nomination et cessation de fonctions | 3 |
| 3.3 Démission, relèvement | `3.1.b` Nomination et cessation de fonctions | 1,5 |
| 3.4 Responsabilités | `3.1.e` Mise en cause de la responsabilité | 2 |
| 3.5 Approche par les risques | `3.2.c` Approche par les risques | 2,5 |
| 3.6 Assertions, procédures, refus de confirmation | `3.2.d` Démarche d'audit | 3 |
| 3.7 Opinion | `3.2.e` Portée des opinions | 3,5 |
| 3.8 VSME, ESRS, désignation volontaire | `3.3.a` Architecture des normes et champ | 2 |
| 3.9 Double matérialité, chaîne de valeur aval, opportunité | `3.3.b` Principes de construction du reporting | 3 |
| 3.10 Objectif, assurance limitée, axes | `3.4.a` Objectifs de la mission de durabilité | 2 |
| 3.11 Avis par axe | `3.4.c` Portée des avis | 3 |
| 3.12 Observation et élément d'attention particulière | `3.4.c` Portée des avis | 2 |
| **Total** | | **30** |

---

### Partie A – Cadre d'exercice, nomination, cessation et responsabilité (9 points)

### 3.1 Expert-comptable et commissaire aux comptes (2,5 pts)

| Critère | Cabinet FAURE (expert-comptable) | Commissaire aux comptes |
|---|---|---|
| **Cadre (1 pt)** | Mission **contractuelle** : tenir, centraliser, arrêter les comptabilités, établir les comptes [V ord. 45-2138 art. 2]. Durée fixée par le contrat [V décret 2012-432 art. 151 al. 3] ; interruption possible pour « motifs justes et raisonnables » [V décret art. 156] | Mission **légale** : certifier que les comptes sont réguliers et sincères et donnent une image fidèle [V C. com. L. 821-53]. Désignation par l'assemblée générale ordinaire [V L. 821-40 I] pour **six exercices** [V L. 821-44] ; aucune immixtion dans la gestion [V L. 821-54 I] |
| **Lettre de mission (0,5 pt)** | Contrat écrit qui **définit la mission** et les droits et obligations des parties ; honoraires convenus par écrit au préalable [V décret art. 151 ; ord. art. 24] | Établie la première année du mandat, avant les travaux. Elle **précise les modalités** d'une mission dont l'objet est fixé par la loi : étendue, calendrier, signataires, accès aux informations, budget d'honoraires [V NEP 210 § 3-8] |
| **Indépendance (0,5 pt)** | **Indépendance d'esprit** et absence de conflit d'intérêts [V décret art. 145-146]. Produire les comptes **est** sa mission : il n'y a pas d'autorévision au sens du CAC [F10 § 3] | **Condition légale** de la mission, appréciée **en réalité et en apparence** [V code de déontologie art. 5]. Le CAC ne peut se prononcer sur des éléments issus de ses propres prestations (**autorévision**) [V code art. 5, 19, 22 ; L. 821-28 IV] |

**Conclusion (0,5 pt).** LUMIVERT n'est pas une EIP. Il n'existe donc pas de liste fermée de services interdits, mais le CAC ne peut accepter la mission s'il existe un **risque d'autorévision** sans mesure de sauvegarde appropriée [V L. 821-28 IV]. Le cabinet FAURE certifierait des comptes qu'il a lui-même établis depuis 2019 : aucune sauvegarde n'est concevable [S, application de F10 § 3]. Avant d'accepter, il devrait d'ailleurs analyser les prestations antérieures fournies à l'entité [V code art. 22]. **Le projet du président doit être écarté.** Que M. FAURE soit inscrit comme CAC ne change rien : un expert-comptable peut exercer des fonctions de CAC [V ord. art. 22], mais pas auprès d'une entité dont il établit les comptes.

### 3.2 Nomination d'un commissaire aux comptes (3 pts)

**LUMIVERT (SAS) – 1,5 pt.** Seuils applicables : total du bilan **5 000 000 €**, chiffre d'affaires HT **10 000 000 €**, **50** salariés, deux sur trois, appréciés à la clôture d'un exercice [V L. 227-9-1 al. 2 ; D. 227-1 renvoyant à D. 221-5].

| Critère | 2025 | Dépassé ? | 2026 | Dépassé ? |
|---|---:|:---:|---:|:---:|
| Total du bilan | 5 300 000 | oui | 4 800 000 | non |
| CA HT | 9 600 000 | non | 10 400 000 | oui |
| Salariés | 46 | non | 52 | oui |
| **Seuils dépassés** | | **1 sur 3** | | **2 sur 3** |

- **Règle de sortie (0,5 pt)** : la société n'est plus tenue de désigner un CAC si elle n'a pas dépassé deux des trois seuils **pendant les deux exercices précédant l'expiration du mandat** [V D. 221-5 al. 2 ; D. 227-1]. Ici, ces exercices sont 2025 et 2026. Les seuils sont dépassés en 2026 : **l'obligation demeure** (0,5 pt pour le tableau).
- **Mandat (0,5 pt)** : l'assemblée de juin 2027 doit renouveler AUDIVAL ou désigner un autre CAC, pour **six exercices** (2027 à 2032) [V L. 821-44]. La durée de trois exercices n'est pas possible : elle est réservée aux désignations volontaires ou fondées sur le régime des petits groupes [V L. 821-46]. LUMIVERT, tête d'un petit groupe, est de toute façon tenue individuellement : il est inutile d'examiner le cumul de l'ensemble [V L. 821-43 al. 1, D. 821-171]. À défaut de désignation : délibérations nulles [V L. 821-5], délit du dirigeant [V L. 821-6 1°], désignation en justice possible [V L. 821-47].

**OPTIBOX (SARL) – 1,5 pt.**
- **Seuils individuels** (D. 221-5) : 2 100 000 € < 5 M€, 5 300 000 € < 10 M€, 27 < 50. Aucune obligation à ce titre [V L. 223-35, D. 223-27].
- **Régime des petits groupes (0,5 pt)** : LUMIVERT contrôle OPTIBOX ; elle n'est ni astreinte à publier des comptes consolidés, ni EIP, ni contrôlée par une entité ayant désigné un CAC. Une entité qu'elle contrôle doit donc désigner un CAC si elle dépasse deux des trois seuils : **2 500 000 €** de bilan, **5 000 000 €** de CA HT, **25** salariés [V L. 821-43 al. 2-3 ; D. 821-172].
- **Application (0,5 pt)** : en 2025, aucun seuil n'est dépassé (1 900 000 €, 4 700 000 €, 23). En 2026, le CA (5 300 000 € > 5 M€) et l'effectif (27 > 25) dépassent les seuils : **2 sur 3**. OPTIBOX doit désigner un CAC lors de l'assemblée qui statue sur les comptes 2026 [S pour le calendrier : F09 § 8, 1].
- **Durée (0,5 pt)** : six exercices, ou **trois exercices** sur option, puisque la désignation est fondée sur L. 821-43 al. 3 [V L. 821-46]. Dans ce cas, le CAC établit un rapport sur les risques financiers, comptables et de gestion [V L. 821-57].

### 3.3 Démission et fin des fonctions (1,5 pt)

- **Démission de M. ROUX (0,5 pt)** : le CAC exerce sa mission jusqu'à son terme. Il ne peut démissionner que pour un **motif légitime** : cessation d'activité, motif personnel impérieux, difficultés auxquelles il ne peut être remédié, atteinte à l'indépendance ou à l'objectivité. Il lui est **interdit de démissionner pour se soustraire à l'émission de son opinion** [V code de déontologie art. 28]. Les tensions avec le président ne sont pas une difficulté insurmontable : le refus de confirmation se traduit dans l'opinion (3.7). AUDIVAL doit **émettre son rapport sur les comptes 2026**. C'est d'ailleurs le mandat de la société de CAC, et non de M. ROUX personnellement.
- **« Révocation » par l'assemblée (0,5 pt)** : le Code ne prévoit pas la révocation du CAC par l'assemblée. Il prévoit seulement un **relèvement par décision de justice**, en cas de **faute ou d'empêchement**, à la demande notamment de l'organe de direction ou d'actionnaires détenant au moins 5 % du capital [V L. 821-50, R. 821-176]. Demander une confirmation à un tiers relève de l'exercice normal de la mission. Ce n'est pas une faute : le texte précise même qu'une divergence d'appréciation sur une procédure de contrôle ne justifie pas une récusation [V L. 821-49]. L'assemblée de mars 2027 ne peut donc pas mettre fin aux fonctions d'AUDIVAL.
- **Non-renouvellement (0,5 pt)** : la société peut ne pas renouveler AUDIVAL à l'expiration du mandat, en juin 2027. AUDIVAL est alors entendu à sa demande [V L. 821-51]. Le successeur doit s'assurer, auprès d'AUDIVAL, que ce non-renouvellement ne vise pas à contourner les obligations légales [V code art. 26]. Comme LUMIVERT est tenue d'avoir un CAC (3.2), un autre CAC devra être désigné, et ce ne peut pas être le cabinet FAURE (3.1).

### 3.4 Responsabilités d'AUDIVAL envers M. DURAND (2 pts)

- **Responsabilité civile (1 pt)** : le CAC est responsable envers l'entité **et les tiers** des conséquences dommageables de ses **fautes et négligences** [V L. 821-37]. Trois conditions doivent être réunies [S, droit commun] :
  - une **faute** : les stocks étaient significatifs, et AUDIVAL n'a ni assisté à l'inventaire ni mis en œuvre de procédure alternative, alors que la norme l'impose [V NEP 501 § 3-6] ;
  - un **préjudice** : M. DURAND a payé un prix calculé sur un résultat surévalué ;
  - un **lien de causalité** : le prix reposait sur des comptes certifiés sans réserve.

  Le CAC n'est pas garant de l'absence de toute anomalie, puisque l'assurance est raisonnable [V NEP 200 § 08-09]. Mais ici, une diligence essentielle a été omise. L'action se prescrit par **trois ans** à compter du fait dommageable (rapport du 18/05/2026), ou de sa révélation s'il a été dissimulé [V L. 821-38 ; L. 225-254].
- **Responsabilité disciplinaire (0,5 pt)** : omettre une procédure essentielle sur un poste significatif peut constituer une **négligence grave** [V L. 821-70 I]. Les sanctions possibles sont l'avertissement, le blâme, l'interdiction d'exercer pour trois ans au plus, la radiation et une sanction pécuniaire. Elles sont prononcées par la **commission des sanctions de la H2A** [V L. 821-71, L. 821-79].
- **Responsabilité pénale (0,5 pt)** : le délit d'informations mensongères sur la situation de la personne morale [V L. 821-9] n'est pas caractérisé, puisqu'il est établi qu'AUDIVAL ignorait les écritures fictives [S : l'énoncé écarte toute connaissance]. La responsabilité pénale de l'auteur des écritures fictives est une autre question, qui n'est pas demandée.

---

### Partie B – Audit des comptes annuels : le cycle fournisseurs et achats (9 points)

### 3.5 Approche par les risques (2,5 pts)

**Définitions (1 pt)** [V NEP 200 § 10-13 ; NEP 315 § 02]
- **Risque d'audit** : risque d'exprimer une opinion inappropriée. Il est égal au risque d'anomalies significatives (RAS) combiné au risque de non-détection.
- **RAS** : risque propre à l'entité, qui existe indépendamment de l'audit. Il comprend deux composantes :
  - le **risque inhérent** : possibilité qu'une anomalie significative se produise, sans tenir compte des contrôles de l'entité ;
  - le **risque lié au contrôle** : risque qu'une anomalie ne soit ni prévenue ni détectée et corrigée par les contrôles de l'entité.
- **Risque de non-détection** : risque propre à la mission, celui que le CAC ne détecte pas une anomalie significative.

**Application (1 pt)**
- **Risque inhérent élevé**, en particulier sur l'**exhaustivité** des dettes et des achats :
  - le ratio bancaire incite à minorer les charges (facteur de risque de fraude [V NEP 315 § 02]) ;
  - le litige avec BÉTA et la suspension des paiements rendent incertain le montant réellement dû.
- **Risque lié au contrôle élevé** : depuis le départ, non remplacé, de la comptable fournisseurs, les relevés des fournisseurs ne sont plus rapprochés des comptes. Ce contrôle clé n'existe plus.
- **RAS élevé** pour le cycle. Sans test des contrôles, le RAS au niveau des assertions correspond au risque inhérent évalué [V NEP 315 § 41].

**Conséquences (0,5 pt).** Le risque de non-détection acceptable est **faible**. Le CAC renforce donc ses **procédures de substance** [V NEP 200 § 13 ; NEP 330] :
- travaux à la clôture plutôt qu'en cours d'exercice ;
- éléments probants externes, plus fiables [V NEP 500 § 6] ;
- échantillons plus larges ;
- équipe expérimentée.

Il ne s'appuie pas sur des contrôles qui n'existent plus.

### 3.6 Assertions, procédures et refus de confirmation (3 pts)

**Assertions et procédures (2 pts, 0,5 pt par couple pertinent, dans la limite de 2 pts)**

| Assertion | Risque | Procédure |
|---|---|---|
| **Exhaustivité** des dettes fournisseurs (solde) | Factures non comptabilisées pour respecter le ratio | **Demande de confirmation ouverte** (le fournisseur indique lui-même son solde [V NEP 505 § 4]), y compris pour des fournisseurs à solde faible ou nul mais à volume d'achats important [S] ; recherche de passifs non comptabilisés : factures reçues et règlements effectués après la clôture |
| **Séparation des exercices** des achats (flux) | Achats de fin 2026 enregistrés en 2027 | Rapprochement des bons de réception autour du 31/12/2026 avec les factures et leur date d'enregistrement |
| **Existence / obligations** des dettes (solde) | Solde BÉTA contesté (litige qualité) | Confirmation directe ; examen des réclamations, avoirs attendus et correspondances avec BÉTA |
| **Réalité** des achats (flux) | Achats fictifs ou non justifiés | Inspection des factures, bons de commande et bons de réception sur un échantillon |
| Ensemble du cycle | Variations inattendues | Procédures analytiques : taux de marge, délai de paiement des fournisseurs comparé à 2025 |

**Refus du président (1 pt).** La demande de confirmation est une technique dont le CAC **maîtrise** la sélection, l'envoi et la réception [V NEP 505 § 9]. Face au refus de la direction, le CAC procède en trois temps [V NEP 505 § 10-12] :
1. il **examine les motifs** du refus ;
2. si ces motifs sont fondés, il met en œuvre des **procédures alternatives** ;
3. sinon, ou si les procédures alternatives ne fournissent pas d'éléments suffisants, il **en tire les conséquences dans son rapport**.

Ici, le motif invoqué (« raviver le conflit ») est peu convaincant : c'est justement le litige qui rend la confirmation utile. Les procédures alternatives (relevés, règlements et factures postérieurs) ne donnent aucun élément. Le CAC documente sa démarche et communique la difficulté aux dirigeants et aux organes visés par la loi [V L. 821-63 I]. Les motifs d'une éventuelle réserve leur sont communiqués au préalable [V NEP 700 § 06]. Il en tire les conséquences sur son opinion (3.7).

### 3.7 Opinion sur les comptes 2026 (3,5 pts)

**Analyse (1,5 pt)**

| Élément | Calcul | Résultat |
|---|---|---:|
| Seuil de signification | 5 % × 800 000 € | **40 000 €** |
| Solde BÉTA non vérifiable | 410 000 € / 40 000 € | 10,25 fois le seuil |
| Poids dans les dettes fournisseurs | 410 000 € / 1 640 000 € | 25 % |
| Anomalie non corrigée | 12 000 € < 40 000 € | non significative |

- Le CAC n'a pas pu mettre en œuvre toutes les procédures nécessaires sur le solde de BÉTA. C'est une **limitation** de l'étendue de ses travaux, imposée par la direction. Le poste concerné est significatif : 410 000 € dépassent largement le seuil de 40 000 €.
- L'anomalie non corrigée de 12 000 € est inférieure au seuil et ne présente aucune particularité de nature ou de circonstance. Elle n'est pas significative [V NEP 320 § 9 ; NEP 450 § 14]. L'erreur de 25 000 € a été corrigée et n'a pas d'incidence sur l'opinion.

**Opinion (1 pt).** La limitation porte sur un **seul solde identifié** (dette envers BÉTA et achats correspondants). Les autres soldes fournisseurs ont été confirmés. Ses incidences sont donc **clairement circonscrites**, et une réserve qui décrit ce poste et son montant suffit à l'utilisateur. Le CAC **certifie avec réserve pour limitation** [V NEP 700 § 11 ; R. 821-180]. Il expose le motif dans la partie « Fondement de l'opinion » : refus de la direction et impossibilité de vérifier l'exhaustivité du solde de 410 000 € [V NEP 700 § 06].

**Opinions écartées (1 pt)**
- **Sans réserve** : impossible, une limitation significative subsiste.
- **Réserve pour désaccord** ou **refus de certifier** : ces opinions supposent une anomalie significative identifiée et non corrigée. Ici, aucune anomalie n'est établie : le CAC ne sait pas si le solde est faux.
- **Impossibilité de certifier** : elle suppose une limitation aux incidences **non** circonscrites, ou des incertitudes multiples [V NEP 700 § 14]. Ici, il s'agit d'une limitation unique, localisée sur un compte, sans effet diffus sur les comptes pris dans leur ensemble.

---

### Partie C – Durabilité (12 points)

### 3.8 VSME, ESRS et désignation de VERIDIS (2 pts)

**Référentiel alternatif (1 pt).** Une entreprise qui n'est pas tenue de publier peut appliquer la **norme volontaire (VSME)**, adoptée par règlement délégué (UE) 2026/1560 [V art. 2]. Cette norme est destinée aux entreprises qui ne dépassent pas 1 000 salariés [V directive (UE) 2026/470, art. 2, 8)]. Elle est élaborée par l'EFRAG et comporte un **module de base** et un **module complet** [V règl. 2026/1560, annexe I]. Elle est plus légère que les ESRS. Les ESRS reposent sur une **analyse de double matérialité** et sur des normes transversales (ESRS 1 et ESRS 2) appliquées avec des normes thématiques [V ESRS 1 (2026) § 8-10]. En retenant les ESRS, LUMIVERT choisit le référentiel le plus exigeant. Elle doit l'indiquer clairement, ce que fait l'énoncé [F12 § 11, 3-b].

**Désignation de VERIDIS (1 pt).**
- VERIDIS est un CAC inscrit sur la liste des CAC habilités pour la durabilité : il peut certifier ces informations [V L. 821-13 II ; L. 232-6-3 III].
- Il a été désigné par l'**assemblée générale ordinaire**, qui est l'organe compétent [V L. 821-40 I].
- La durée de droit commun est de six exercices [V L. 821-44]. La désignation de LUMIVERT n'est pas imposée par la loi : elle est **volontaire**. Le mandat peut donc être limité à **trois exercices** [V L. 821-46 ; FAQ H2A 11/2024, p. 3].

Le mandat 2025-2027 est **régulier**.

### 3.9 Double matérialité, chaîne de valeur, IRO (3 pts)

**Principe (1 pt)**
- Un enjeu est matériel s'il l'est au titre de la **matérialité d'impact**, de la **matérialité financière**, **ou des deux** [V ESRS 1 (2023) § 28 ; ESRS 1 (2026) § 35].
- **Matérialité d'impact** : impacts positifs ou négatifs, réels ou potentiels, de l'entreprise sur la population ou l'environnement [V ESRS 1 (2026) § 39-41]. Un impact négatif s'apprécie selon sa **gravité** (ampleur, étendue, caractère irrémédiable) et, s'il est potentiel, selon sa **probabilité**.
- **Matérialité financière** : effets financiers réels ou raisonnablement attendus sur la situation financière, la performance, les flux de trésorerie, l'accès au financement ou le coût du capital [V ESRS 1 (2026) § 47, 50]. Ils s'apprécient selon leur probabilité et leur ampleur potentielle.
- **Chaîne de valeur** : l'état de durabilité couvre les activités propres, mais aussi la chaîne **amont** (fournisseurs) et **aval** (clients, utilisation et fin de vie des produits). Il le fait dans la mesure nécessaire à la compréhension des IRO matériels liés aux relations d'affaires directes et indirectes [V ESRS 1 (2026) § 39, 62-65].

**Impact situé dans la chaîne de valeur aval (1 pt)**

| Enjeu | Dimension | Analyse |
|---|---|---|
| Éclairage nocturne riche en bleu et non modulable (gamme vendue jusqu'en 2024) | **Impact négatif** sur la biodiversité (insectes, chauves-souris, oiseaux) | L'impact survient lors de l'**utilisation des produits par les clients** : il se situe dans la chaîne aval, et non dans les activités propres. Gravité : étendue importante (plus de 100 000 luminaires), effets durables tant que les luminaires restent en service. L'impact est **réel**, puisqu'il est dénoncé par des associations |

Autres réponses acceptées pour l'aval :
- économies d'électricité de 60 % chez les communes (**impact positif** réel sur le climat, apprécié selon son ampleur et son étendue) ;
- fin de vie des composants électroniques (impact négatif potentiel, dont la maîtrise dépend de la collecte).

**Opportunité (1 pt)**

| Enjeu | Dimension | Analyse |
|---|---|---|
| Programmes d'aide à la rénovation de l'éclairage public ; appels d'offres en hausse de 25 % ; demande de luminaires réglables à lumière chaude | **Matérialité financière : opportunité** | Effet financier positif probable et d'ampleur significative : croissance du chiffre d'affaires et des marges sur un marché porté par la transition énergétique |

L'**interaction** entre les deux dimensions est valorisée. L'exigence d'intensité réglable et de lumière chaude répond à l'impact sur la biodiversité. La même évolution crée une opportunité pour la gamme récente et un risque pour la gamme ancienne (réputation, perte d'appels d'offres).

### 3.10 Objectif, assurance, axes (2 pts)

**Objectif et assurance (1 pt).**
- VERIDIS émet un **avis** sur la conformité des informations de durabilité aux ESRS, y compris sur le processus de détermination des informations [V L. 821-54 II]. Cet avis figure dans un **rapport de certification** destiné à l'organe qui statue sur les comptes [V L. 821-54 II ; LD 2026 § 17].
- La mission repose sur une **assurance limitée** [V LD 2026, niveau d'assurance]. Les travaux sont moindres en nature, en étendue et en durée que pour une assurance raisonnable.
- La conclusion est exprimée sous une **forme négative** : « nous n'avons pas relevé d'erreurs, omissions ou incohérences importantes… ». L'audit des comptes, lui, repose sur une assurance raisonnable exprimée sous une forme positive [V LD 2026 ; NEP 200 § 08].
- La mission ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].

**Axes (1 pt)** [V LD 2026 § 2]
1. **Processus** de détermination des informations (double matérialité), y compris la **consultation du CSE**. Celle-ci est due ici en vertu de l'accord avec le CSE et de la lettre de mission (hypothèse de l'énoncé).
2. **Informations** publiées dans l'état de durabilité.
3. Exigences de publication liées à la **taxonomie** : **sans objet**, puisque LUMIVERT n'y est pas soumise [F13 § 5, 5].
4. **Balisage** : non exigible tant que les règles ne sont pas adoptées [V LD 2026 § 2, § 10].

La mission porte donc sur **deux axes**.

### 3.11 Avis de VERIDIS (3 pts)

La table de décision est celle des LD 2026 (§ 17). Le vérificateur émet un avis **par axe**.

| Axe | Constat | Avis |
|---|---|---|
| 1. Processus | Analyse de double matérialité conforme (activités propres et chaîne de valeur, dialogue avec les parties prenantes) ; **CSE non consulté**, omission non corrigée | **Avis de conformité assorti d'une réserve motivée** (1,5 pt) |
| 2. Informations | Taux de collecte (82 %) non vérifiable : **limitation** ; autres informations sans remarque | **Avis de conformité assorti d'une réserve motivée** (1,5 pt) |

**Justification de l'axe 1.** LUMIVERT publiant volontairement, la consultation du CSE ne lui est pas imposée par la loi : L. 2312-17 du code du travail ne vise que les entreprises tenues de publier [V, F12 § 11 (b)]. Elle entre ici dans l'axe 1 parce que LUMIVERT s'y est engagée par accord et que la **lettre de mission** de VERIDIS l'inclut dans les vérifications (annexe 3.6). La vérification suit alors, par analogie, le schéma légal [L. 821-54 II 2° ; LD 2026 § 7.3]. L'absence de consultation est une **omission non corrigée** qui remet en cause la conformité du processus. Ses incidences sont toutefois **clairement circonscrites** : l'analyse de double matérialité elle-même est conforme, et le défaut est isolé et précisément identifié. Une réserve motivée suffit à l'utilisateur. Ni les LD 2026 ni la loi ne qualifient le défaut de consultation : la réserve résulte de l'application de la table de décision générale, c'est un jugement professionnel [F13 § 4.3 et 4.5]. On écarte :
- l'avis de conformité, puisque l'omission n'est pas corrigée ;
- l'avis de non-conformité, puisque les incidences sont circonscrites.

Formulation attendue : « nous n'avons pas relevé d'erreurs, omissions ou incohérences importantes concernant la conformité du processus mis en œuvre par LUMIVERT avec les ESRS, sous la réserve décrite ci-après » [V LD 2026, annexe 2, p. 46].

**Justification de l'axe 2.** VERIDIS n'a pu mettre en œuvre aucune vérification sur le taux de collecte : c'est une **limitation**, et non une erreur constatée. Ses incidences sont **circonscrites** : une seule information, clairement identifiée, n'est reprise nulle part ailleurs, et toutes les autres informations vérifiées n'appellent pas de remarque. Selon les LD 2026, une limitation aux incidences circonscrites conduit à un **avis de conformité assorti d'une réserve motivée** [V LD 2026 § 17]. On écarte :
- l'impossibilité d'émettre un avis, qui supposerait des incidences non circonscrites ;
- l'avis de non-conformité, qui supposerait une erreur identifiée et non circonscrite.

Dans les LD 2024, la limitation figurait parmi les motifs de non-conformité : c'est la version 2026 qu'il faut retenir [F13 § 4.3].

### 3.12 Observation et élément d'attention particulière (2 pts)

**Distinction (1 pt)** [V LD 2026 § 17]
- Une **observation** attire l'attention du lecteur sur une information **publiée par l'entité** : méthode de préparation, limite de périmètre ou de mesure, jugement important. Elle n'est possible qu'avec un **avis de conformité, avec ou sans réserve**, et ne modifie pas l'avis. Ce n'est pas une réserve. Si l'information n'était pas acceptable au regard des textes, il faudrait formuler une réserve, voire émettre un avis plus défavorable.
- Un **élément ayant fait l'objet d'une attention particulière** décrit les **risques les plus importants** de non-conformité et/ou les **attentes les plus fortes des utilisateurs**, ainsi que les **principales diligences** mises en œuvre. Sa rédaction est circonstanciée et non standardisée.

**Rattachement (1 pt)**
- **Point (c)**, estimation des économies d'électricité à partir de moyennes sectorielles : **observation** dans la partie relative à l'axe 2. Elle renvoie à la note méthodologique de l'entité, qui porte sur une limite de mesure jugée acceptable. Elle est compatible avec l'avis assorti d'une réserve de cet axe.
- **Point (d)**, évaluation de l'impact de l'éclairage nocturne sur la biodiversité : **élément ayant fait l'objet d'une attention particulière** dans la partie relative à l'axe 1. Il s'agit de l'enjeu qui suscite les plus fortes attentes des utilisateurs, et VERIDIS y a consacré une part importante de ses diligences.

---

### Réponses tolérées
- **3.2** : un candidat qui écrit que le CAC d'OPTIBOX est désigné « à partir de l'exercice 2027 », sans discuter du calendrier.
- **3.3** : l'emploi du mot « révocation » s'il est rattaché au relèvement judiciaire pour faute ou empêchement.
- **3.6** : tout couple risque / assertion / procédure cohérent. Une confirmation « fermée » est acceptée si le candidat note sa moindre efficacité pour l'exhaustivité.
- **3.9** : le vocabulaire des ESRS de 2023 (« double importance », « incidences »).
- **3.11** : sur l'axe 1, un avis de non-conformité reçoit la moitié des points s'il est argumenté avec la table de décision : il faut expliquer pourquoi les incidences ne seraient pas circonscrites. Aucun texte n'impose l'une ou l'autre qualification [F13 § 4.5].

### Erreurs fréquentes
- Confondre l'indépendance d'esprit de l'expert-comptable et l'indépendance du CAC, et ne pas voir l'autorévision (`JUR-A03`).
- Importer la règle des « deux exercices consécutifs » pour l'**entrée** dans l'obligation de désigner un CAC : elle ne joue que pour la **sortie**, appréciée sur les deux exercices précédant l'expiration du mandat.
- Oublier le régime des petits groupes pour OPTIBOX, ou lui appliquer les seuils de D. 221-5.
- Admettre la révocation du CAC par l'assemblée.
- Confondre « exhaustivité » et « existence », ou « réalité » (flux) et « existence » (solde) (`JUR-A01`).
- Conclure à une **réserve pour désaccord** alors qu'aucune anomalie n'est établie, ou à une impossibilité de certifier pour une limitation circonscrite. Donner l'opinion sans son motif (`JUR-A02`).
- Pour la durabilité :
  - émettre un avis unique au lieu d'un avis par axe ;
  - traiter la limitation de l'axe 2 comme une non-conformité, selon la règle des LD 2024 ;
  - présenter une observation comme une réserve.
- Ne pas justifier les calculs ni expliciter les hypothèses (`JUR-F02`, `JUR-F06`).
