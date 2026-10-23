# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Exercice d'entraînement n° 5 — Dossier 1 (45 points)

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F03 périmètre et méthodes (à jour au 22/10/2026) ; F04 retraitements (à jour au 23/10/2026) ; F05 écarts d'acquisition, goodwill et mise en équivalence (à jour au 23/10/2026). Paragraphes non repris dans les fiches, vérifiés sur le texte officiel français des IFRS (règlement (UE) 2023/1803 consolidé au 30/07/2025, CELEX 02023R1803-20250730, obtenu via Cellar le 23/10/2026) : IAS 21 § 9 à 12, 39 à 41 ; IAS 20 § 12, 13, 15, 17, 24, 27 ; IAS 19 § 57, 120, 122, 123 ; IAS 28 § 5, 10, 27, 32 ; IFRS 16 § 22 à 26, 31, 32, 36, 49 ; IAS 12 § 7 à 9, 22A, 24, 26, 61A, 74 ; IFRS 10 B94. Le groupe n'appliquant pas IFRS 18 par anticipation, la présentation 2026 relève encore de la norme de présentation en vigueur (voir F99). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre IFRS, conversion, goodwill, impôts différés, partage et mise en équivalence, 13 écritures, barème).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

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
