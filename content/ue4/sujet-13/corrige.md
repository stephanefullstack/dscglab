# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 13

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 13/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.9 | `exercices/ex34_consolidation_ifrs_developpement_change_complement_prix` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.5 | `exercices/ex35_fusion_envers_holding_actions_propres` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.10 | `exercices/ex36_audit_paie_association_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 a Référentiel IFRS obligatoire | `2.1.b` Contexte réglementaire et légal de la consolidation | 0,5 |
| 1.1 b IASB, IFRS Interpretations Committee, EFRAG, adoption | `2.1.a` Cadre conceptuel de l'IASB, normalisateurs | 1 |
| 1.1 c Cadre conceptuel appliqué au projet de VALBOGIE | `2.1.a` Cadre conceptuel ; `2.2.c` Coûts de développement | 1 |
| 1.1 d Exemption de consolider de STRIBEUX Freinage | `2.1.b` Contexte réglementaire et légal de la consolidation | 1,5 |
| 1.2 a Tableau du périmètre | `2.1.c` Périmètre ; `2.1.d` Méthodes | 1 |
| 1.2 b AMÉNORAIL : coentreprise, comparaison avec le règlement ANC | `2.1.c` Périmètre ; `2.1.d` Méthodes et information financière | 1 |
| 1.3 a Coût de la plateforme et amortissement | `2.2.c` Homogénéisation, thèmes communs | 1,5 |
| 1.3 b Tableau d'incidence du développement | `2.2.c` Homogénéisation, thèmes communs | 2 |
| 1.3 c Écritures du développement | `2.2.c` Homogénéisation, thèmes communs | 2 |
| 1.4 a Frais d'acquisition des titres | `2.2.c` Homogénéisation ; `2.2.g` Goodwill | 1,5 |
| 1.4 b Opérations en dollars : traitements et incidence | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 2 |
| 1.4 c Opérations en dollars : impôt différé et écritures | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 2 |
| 1.5 a Comptes réciproques et règlement en transit | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.5 b Résultat interne sur le banc d'essai, répartition | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.5 c Écritures du banc d'essai | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.6 a Contrepartie transférée | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.6 b Actif net identifiable du sous-groupe | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.6 c Goodwill partiel et PNC | `2.2.g` Écarts d'évaluation et goodwill | 1 |
| 1.6 d Révision du complément de prix | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.6 e Écritures des écarts d'évaluation et du complément de prix | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.7 a Tableaux de partage des trois filiales | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.7 b Mise en équivalence d'AMÉNORAIL | `2.2.h` Partage des capitaux propres (MEE) | 1,5 |
| 1.7 c Écritures d'élimination, de partage et de mise en équivalence | `2.2.g` ; `2.2.h` | 3 |
| 1.8 Passage au résultat net consolidé, phase par phase | `2.2.a` Processus d'élaboration d'une consolidation | 3 |
| 1.9 a Tableau des flux de trésorerie selon IAS 7 | `2.3.a` Documents de synthèse consolidés | 4 |
| 1.9 b Présentation, notes, différence avec le règlement ANC | `2.3.a` Documents de synthèse ; `2.1.d` | 2 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = participations ne donnant pas le contrôle (PNC) ; `CAP_ELIM` = capital de la filiale éliminé ; `EA` = goodwill ; `TME` = participation mise en équivalence ; `QP_MEE` = quote-part du résultat net des entités mises en équivalence ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat de l'écriture de bilan. Un suffixe désigne la société concernée (`RST.VALBOGIE`, `261.FERVALIS` : titres détenus par FERVALIS ; `STRIBEUX_F` et `STRIBEUX_S` : STRIBEUX Freinage et STRIBEUX Services).

---

### 1.1 Cadre de la consolidation (4 pts)

#### a. Référentiel (0,5 pt)

Les IFRS adoptées par l'Union européenne sont obligatoires pour les comptes consolidés des sociétés dont les titres sont admis aux négociations sur un marché réglementé d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Les actions de FERVALIS sont admises sur Euronext Paris, marché réglementé : le groupe n'a pas le choix du règlement ANC n° 2020-01, ouvert aux seules sociétés non cotées (0,5 pt).

#### b. Normalisateurs et adoption (1 pt)

- **IASB (0,25 pt)** : groupe indépendant d'experts, au sein de l'IFRS Foundation, organisme sans but lucratif ; il élabore et publie les normes IFRS et approuve les interprétations [V page « International Accounting Standards Board », ifrs.org ; F03 § 7.2].
- **IFRS Interpretations Committee, anciennement IFRIC (0,25 pt)** : il élabore les interprétations des normes, sur les questions d'application qui lui sont soumises ; elles sont ensuite approuvées par l'IASB [V même page ; F03 § 7.2].
- **EFRAG (0,25 pt)** : il fait valoir les positions européennes dans les travaux de l'IASB et conseille la Commission européenne sur la conformité de chaque norme nouvelle ou modifiée aux critères du règlement IAS, dont l'intérêt public européen [V page « Financial reporting », efrag.org ; F03 § 7.2].
- **Adoption (0,25 pt)** : une norme de l'IASB n'est applicable dans l'Union, et donc en France, qu'après son adoption par un règlement de la Commission, d'application directe [V intitulé du règlement (UE) 2023/1803 ; F03 § 7.2]. Exemple : IFRS 18, adoptée par le règlement (UE) 2026/338, ne s'appliquera qu'aux exercices ouverts à compter du 01/01/2027 ; FERVALIS ne l'anticipe pas [V F14 § 0].

#### c. Cadre conceptuel et projet de VALBOGIE (1 pt)

**Objectif (0,25 pt).** L'information financière à usage général doit être utile aux investisseurs, prêteurs et autres créanciers, actuels et potentiels, pour leurs décisions de fournir des ressources à l'entité [S présentation du cadre de 2018 ; F03 § 7.2]. Les actionnaires de FERVALIS, société cotée, doivent voir les ressources que le groupe a constituées pour ses ventes futures, quel que soit le choix comptable d'une filiale dans ses comptes individuels.

**Définition d'un actif appliquée au projet (0,75 pt).** Un actif est une ressource contrôlée par l'entité du fait d'événements passés, dont elle attend des avantages économiques futurs [V IAS 38 § 8 ; F03 § 9].
- Les dépenses engagées depuis le 01/07/2025 (1 400 000 € en 2025, 1 600 000 € en 2026) ont créé une ressource que VALBOGIE contrôle (la conception de la plateforme, son dossier de fabrication, son savoir-faire), du fait d'événements passés (les travaux réalisés), et dont elle attend des avantages : ventes de bogies, dont une commande annoncée. À cette date, la faisabilité, l'intention, les moyens et le marché étaient démontrés : ce sont les critères qu'IAS 38 exige pour qu'un développement soit un actif [V IAS 38 § 57 ; F04 § 11] (0,25 pt).
- Les dépenses du premier semestre 2025 (800 000 €) ont été engagées alors que les critères n'étaient pas réunis et qu'aucun avantage futur n'était démontrable (choix entre plusieurs architectures) : elles ne répondaient pas à la définition et restent en charges, sans pouvoir être inscrites à l'actif par la suite [V IAS 38 § 54, 71 ; F04 § 11] (0,25 pt).
- Les dépenses de formation et de présentation aux salons (150 000 €) ne créent pas de ressource contrôlée distincte de l'activité : ce sont des charges [V IAS 38 § 67, 69 ; F04 § 11] (0,25 pt).

Le bilan consolidé montre ainsi l'investissement réellement constitué ; les comptes individuels de VALBOGIE, qui ont tout passé en charges, le masquent.

#### d. Exemption de STRIBEUX Freinage (1,5 pt)

**Principe (0,25 pt).** Une société commerciale qui contrôle de manière exclusive une ou plusieurs entreprises établit et publie des comptes consolidés [V C. com. L. 233-16 ; F03 § 1.1] : STRIBEUX Freinage, qui détient 100 % de STRIBEUX Services, y est en principe tenue.

**Exemption de la société contrôlée (L. 233-17, 1°) (0,75 pt).** Elle est exemptée si elle est elle-même contrôlée par une entité qui l'inclut dans ses comptes consolidés publiés : c'est le cas, FERVALIS consolidant STRIBEUX Freinage et sa filiale par intégration globale (0,25 pt). Conditions [V L. 233-17 ; R. 233-15 ; F03 § 1.1] : STRIBEUX Freinage n'émet ni titre admis sur un marché réglementé, ni titre de créance négociable (annexe 1.1) ; les comptes consolidés de FERVALIS doivent être établis selon les textes applicables, certifiés, publiés et mis à la disposition des associés de STRIBEUX Freinage, en français ou traduits ; l'exemption est justifiée dans l'annexe de STRIBEUX Freinage (0,25 pt). Surtout, elle tombe en cas d'**opposition d'actionnaires représentant au moins le dixième du capital** : M. STRIBEUX, qui détient 20 %, peut seul l'empêcher (0,25 pt).

**Exemption des ensembles qui ne forment pas un grand groupe (L. 233-17, 2°) (0,5 pt).** Un grand groupe dépasse, à la clôture de deux exercices consécutifs, au moins deux des trois seuils : 30 M€ de total du bilan, 60 M€ de chiffre d'affaires net, 250 salariés [V L. 230-2, 3° ; D. 230-2, 2° et dernier alinéa ; F03 § 1.1] (0,25 pt). L'ensemble STRIBEUX dépasse en 2025 et en 2026 le seuil du bilan (31,4 M€ puis 33,2 M€) et celui des effectifs (262 puis 274), mais pas celui du chiffre d'affaires : c'est un grand groupe, et cette exemption n'est pas ouverte (0,25 pt).

**Conclusion (0,25 pt).** STRIBEUX Freinage peut cesser de publier des comptes consolidés pour 2026 si M. STRIBEUX ne s'y oppose pas ; il faut donc l'interroger avant de décider. (IFRS 10 § 4 a) prévoit une exemption semblable pour une société mère intermédiaire, sous réserve que les autres propriétaires informés ne s'y opposent pas [V F03 § 1.2].)

**Réponses tolérées (1.1)**
- En b, rôle de l'IFRS Interpretations Committee décrit plus largement (questions d'application, projets de décisions), si l'approbation par l'IASB est mentionnée.
- En c, définitions du cadre de 2018 (ressource économique actuelle contrôlée du fait d'événements passés, droit qui a le potentiel de produire des avantages économiques) au même titre que celle d'IAS 38 § 8 ; critères d'IAS 38 cités en partie, s'ils sont appliqués aux faits du 01/07/2025.
- En d, conclusion conditionnelle formulée autrement (« possible tant que le fondateur n'a pas fait opposition »).

**Erreurs fréquentes (1.1)**
- IFRS présentées comme une option ; EFRAG présenté comme l'auteur des normes ; IFRS 18 appliquée dès 2026.
- Dépenses du premier semestre 2025 inscrites à l'actif « puisque le projet a abouti » ; formation inscrite au coût.
- Exemption accordée sans évoquer l'opposition du fondateur, ou refusée au motif que FERVALIS est cotée (c'est la société exemptée qui ne doit pas avoir de titres admis sur un marché réglementé) ; seuils périmés de l'ancien régime des petits groupes (F99) ; seuils appliqués à STRIBEUX Freinage seule.

**Références normatives (1.1)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règlement (CE) n° 1606/2002, art. 4 | IFRS obligatoires (marché réglementé) | [V] | F03 § 1.2 |
| Pages ifrs.org et efrag.org ; règlement (UE) 2023/1803 | IASB, IFRS Interpretations Committee, EFRAG, adoption | [V] | F03 § 7.2 |
| Cadre conceptuel de 2018 | Objectif, utilisateurs | [S] | F03 § 7.2 |
| IAS 38 § 8, 54, 57, 67, 69, 71 | Définition d'un actif ; recherche ; critères du développement ; dépenses exclues ; interdiction de réincorporer | [V] | F03 § 9 ; F04 § 11 |
| C. com. L. 233-16, L. 233-17, R. 233-15, L. 230-2, D. 230-2 | Obligation de consolider, exemptions et leurs conditions, seuils du grand groupe | [V] | F03 § 1.1 |
| IFRS 10 § 4 a) | Exemption de la société mère intermédiaire | [V] | F03 § 1.2 |

---

### 1.2 Périmètre et méthodes (2 pts)

#### a. Tableau du périmètre (1 pt, 0,25 pt par société)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % des PNC |
|---|---:|---|---|---:|---:|
| VALBOGIE | 100 % | Contrôle exclusif | Intégration globale | 100 % | 0 % |
| STRIBEUX Freinage | 80 % | Contrôle exclusif | Intégration globale | 80 % | 20 % |
| STRIBEUX Services | 100 % | Contrôle exclusif (indirect) | Intégration globale | 80 % × 100 % = 80 % | 20 % |
| AMÉNORAIL | 50 % | Contrôle conjoint | Mise en équivalence | 50 % | — |

Le pourcentage de contrôle de STRIBEUX Services additionne les droits de vote détenus par les entités que le groupe contrôle exclusivement : STRIBEUX Freinage en détient 100 % [V ANC art. 211-6 ; F03 § 4.1, même raisonnement en IFRS] ; le pourcentage d'intérêt, produit des pourcentages de capital, n'est que de 80 % : les 20 % du fondateur dans STRIBEUX Freinage portent indirectement sur STRIBEUX Services [S F03 § 4.1].

#### b. AMÉNORAIL (1 pt)

**Qualification (0,5 pt).** Le pacte d'associés exige l'unanimité de FERVALIS et d'ORVELIA Composites pour les décisions sur les activités pertinentes (budget, investissements, financement, dirigeant, grands contrats) : aucun associé ne peut décider seul, le contrôle est **conjoint** [V IFRS 11 § 7 ; F03 § 2]. Constitué sous forme d'une société dont les associés n'ont de droits que sur l'actif net, et non sur les actifs ni d'obligations au titre des passifs, le partenariat est une **coentreprise** [V IFRS 11 § 14, 16 ; F03 § 2], comptabilisée selon la **méthode de la mise en équivalence** [V IFRS 11 § 24 ; annexe 1.2, point 5]. L'intégration proportionnelle n'existe plus en IFRS pour les coentreprises [V F03 § 3 ; F99 : la norme antérieure sur les coentreprises est remplacée par IFRS 11].

**Comparaison avec le règlement ANC (0,5 pt).** Le règlement ANC n° 2020-01 imposerait l'**intégration proportionnelle** des entités sous contrôle conjoint [V art. 221-1 ; F03 § 3] : 50 % de chaque actif, passif, produit et charge d'AMÉNORAIL seraient cumulés ligne à ligne avec ceux du groupe, sans intérêts minoritaires [V art. 221-3]. En IFRS, AMÉNORAIL n'apparaît que sur deux lignes : la participation mise en équivalence à l'actif et la quote-part de résultat au compte de résultat. Le chiffre d'affaires, l'endettement et les actifs consolidés sont donc plus faibles en IFRS ; le résultat net et les capitaux propres part du groupe sont identiques ; les ratios (marge, endettement) et la comparabilité avec un groupe établissant ses comptes selon le règlement ANC en sont modifiés.

**Réponses tolérées (1.2)** : pourcentage des PNC d'AMÉNORAIL noté « sans objet » ou 0 % ; justification du contrôle de STRIBEUX Freinage par la majorité des droits de vote et la nomination du président.

**Erreurs fréquentes (1.2)** : contrôle de STRIBEUX Services fixé à 80 % ; AMÉNORAIL qualifiée d'entreprise associée (influence notable) ou intégrée proportionnellement en IFRS ; contrôle conjoint déduit du seul pourcentage de 50 %, sans l'accord d'unanimité (`JUR-F07`).

**Références normatives (1.2)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ANC 2020-01 art. 211-6, 221-1, 221-3 | Pourcentage de contrôle ; intégration proportionnelle | [V] | F03 § 3, § 4.1 |
| IFRS 11 § 7, 14, 16, 24 | Contrôle conjoint, coentreprise, mise en équivalence | [V] | F03 § 2, § 3 |
| Pourcentage d'intérêt en approche directe | Produit des pourcentages le long de la chaîne | [S] | F03 § 4.1 |

---

### 1.3 Coûts de développement de VALBOGIE (5,5 pts)

#### a. Coût de la plateforme et amortissement (1,5 pt)

Un développement est inscrit à l'actif si, et seulement si, l'entité démontre les six critères d'IAS 38 : faisabilité technique, intention d'achever, capacité à utiliser ou à vendre, avantages économiques futurs probables (marché), ressources disponibles, évaluation fiable des dépenses [V IAS 38 § 57 ; F04 R7, § 11]. Au 01/07/2025, la faisabilité est validée par les essais, l'intention et les ressources par la décision et le budget du conseil, le marché par la lettre d'intention, l'évaluation fiable par le suivi des coûts par projet (0,5 pt).

| Dépenses | Montant | Traitement |
|---|---:|---|
| 01/01/2025 – 30/06/2025 : études de principe, choix entre architectures | 800 000 | Charges : critères non réunis à cette date (recherche, puis travaux antérieurs à la réunion des critères) ; jamais réincorporées [V IAS 38 § 54, 65, 71] |
| 01/07/2025 – 31/12/2025 : développement de la solution retenue | 1 400 000 | **Actif** (coût à partir de la date où les critères sont réunis) |
| 01/01/2026 – 30/06/2026 : fin du développement | 1 600 000 | **Actif** |
| Après le 01/07/2026 : formation, salons | 150 000 | Charges [V IAS 38 § 67 c), 69] |
| **Coût de la plateforme** (0,5 pt) | **3 000 000** | |

**Amortissement de 2026 (0,5 pt)** : il commence à la mise en service, le 01/07/2026 [V IAS 38 § 97] : 3 000 000 / 5 × 6/12 = **300 000 €**. Valeur nette au 31/12/2026 : **2 700 000 €**.

#### b. Tableau d'incidence (2 pts)

| | Ouverture au 01/01/2026 (réserves) | Exercice 2026 (résultat) | Clôture au 31/12/2026 |
|---|---:|---:|---:|
| Frais de développement (brut) | 1 400 000 | + 1 600 000 | 3 000 000 |
| Amortissement | — | – 300 000 | – 300 000 |
| **Écart avant impôt** | **+ 1 400 000** (0,25 pt) | **+ 1 300 000** (0,25 pt) | **+ 2 700 000** (0,25 pt) |
| Impôt différé passif, 25 % | – 350 000 | – 325 000 (0,25 pt) | – 675 000 (0,25 pt) |
| **Incidence nette** | **+ 1 050 000** (0,25 pt) | **+ 975 000** (0,25 pt) | **+ 2 025 000** |

Les dépenses du second semestre 2025 ont réduit le résultat de 2025 dans les comptes de VALBOGIE : leur inscription à l'actif corrige les réserves. **Impôt différé (0,25 pt)** : les dépenses ont été déduites fiscalement lors de leur engagement ; la base fiscale de la plateforme est nulle, inférieure à sa valeur consolidée : différence temporelle imposable, **impôt différé passif** [V IAS 12 § 15 ; F04 R7 ; annexe 1.3].

#### c. Écritures (2 pts)

**C1 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 203 Frais de développement | 3 000 000 | |
| 2803 Amortissements des frais de développement | | 300 000 |
| IDP Impôt différé passif (2 700 000 × 25 %) | | 675 000 |
| RSV.VALBOGIE Réserves VALBOGIE (1 400 000 × 75 %) | | 1 050 000 |
| RST.VALBOGIE Résultat VALBOGIE (1 300 000 × 75 %) | | 975 000 |
| **Total** | **3 000 000** | **3 000 000** |
| | *Libellé : plateforme de bogies inscrite à l'actif selon IAS 38* | | |

**C1R (compte de résultat, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles | 300 000 | |
| CH_ID Charge d'impôt différé (1 300 000 × 25 %) | 325 000 | |
| RES_CR Résultat | 975 000 | |
| 721 Production immobilisée – Immobilisations incorporelles | | 1 600 000 |
| **Total** | **1 600 000** | **1 600 000** |

Les dépenses de 2026 restent dans les charges par nature (achats, personnel) ; la production immobilisée les neutralise pour la part inscrite à l'actif, comme le prévoit le manuel (annexe 1.2, point 1).

**Réponses tolérées (1.3)** : dépenses de 2026 portées au crédit des comptes de charges par nature au lieu du compte 721 (même résultat) ; écriture de bilan scindée (activation, puis amortissement) ; amortissement calculé en jours (01/07 au 31/12), arrondi à 300 000 €.

**Erreurs fréquentes (1.3)** : activation de 3 950 000 € (toutes les dépenses) ou de 3 800 000 € (sans les dépenses de 2025 antérieures aux critères, mais avec la formation) ; dépenses de 2025 portées au résultat de 2026 (`JUR-G07`) ; amortissement sur douze mois ou à compter du 01/07/2025 ; impôt différé omis ou actif (`JUR-G05`).

**Références normatives (1.3)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 38 § 54, 57, 65, 67, 69, 71, 97 | Recherche, critères, coût, exclusions, réincorporation interdite, début de l'amortissement | [V] | F04 R7, § 11 |
| IAS 12 § 15 | Impôt différé passif (dépenses déduites à leur engagement) | [V] | F04 § 1, R7 |

---

### 1.4 Frais d'acquisition et opérations en dollars (5,5 pts)

#### a. Frais d'acquisition des titres STRIBEUX Freinage (1,5 pt)

**Traitement (0,5 pt).** En IFRS, les frais connexes à une acquisition (honoraires de banque d'affaires, d'avocats, d'audit) sont des charges de la période où ils sont engagés ; ils ne font pas partie de la contrepartie transférée [V IFRS 3 § 53 ; F05 § 2 ; annexe 1.2, point 2]. Dus lors de la réalisation, le 01/01/2026, ils sont des charges de 2026.

**Incidence (0,5 pt).** Résultat consolidé de 2026 : **– 360 000 €**, sans impôt différé (manuel) ; titres ramenés à 13 200 000 € avant l'ajout du complément de prix ; le goodwill ne comprend pas les frais (question 1.6). En règlement ANC, ils entreraient au contraire dans le coût d'acquisition, nets d'impôt [V art. 231-2 ; F05 § 1.1].

**C2 (bilan, 0,25 pt)** : débit RST.FERVALIS Résultat FERVALIS 360 000 ; crédit 261.FERVALIS Titres de participation STRIBEUX Freinage 360 000. **C2R (compte de résultat, 0,25 pt)** : débit 6226 Honoraires 360 000 ; crédit RES_CR Résultat 360 000. *Libellé : frais d'acquisition des titres STRIBEUX Freinage passés en charges.*

#### b. Opérations en dollars : traitements et incidence (2 pts)

**Comptes individuels (0,5 pt).** Les créances et dettes en devises sont converties au dernier cours à la clôture ; les écarts sont inscrits en comptes transitoires, 476 pour une perte latente et 477 pour un gain latent ; seule la perte latente est prise en compte en résultat, par une provision pour perte de change [V PCG art. 420-5 ; F04 R12].

**IAS 21 (0,5 pt).** La transaction est enregistrée au cours du jour [V IAS 21 § 21] ; à la clôture, les éléments monétaires (créances, dettes) sont convertis au cours de clôture et tous les écarts de change, gains ou pertes, réalisés ou non, sont comptabilisés en résultat [V § 23 a), 28 ; F04 R12, § 11 ; annexe 1.2, point 3]. Les comptes 476, 477 et la provision n'ont plus d'objet.

**Calculs (0,5 pt)**

| | Cours historique (1,0800) | Cours de clôture (1,1250) | Écart |
|---|---:|---:|---:|
| Solde de la créance : 3 240 000 – 1 296 000 = 1 944 000 USD | 1 800 000 | 1 728 000 | perte latente 72 000 (476, provision 1515) |
| Dette fournisseur : 1 620 000 USD | 1 500 000 | 1 440 000 | gain latent 60 000 (477) |

La perte réalisée sur l'encaissement du 15/12/2026 (1 296 000 / 1,0800 – 1 296 000 / 1,1520 = 1 200 000 – 1 125 000 = 75 000 €) est déjà en résultat (compte 666) dans les deux référentiels : elle n'est pas retraitée.

**Incidence sur le résultat avant impôt (0,5 pt)** : la perte de change latente (72 000 €) remplace la dotation à la provision (72 000 €) : effet nul ; le gain latent entre en résultat : **+ 60 000 €**.

#### c. Impôt différé et écritures (2 pts)

**Impôt différé (1 pt).** Une différence temporelle existe lorsque la base fiscale d'un actif ou d'un passif diffère de sa valeur consolidée [V IAS 12 § 5, 15, 24 ; F04 R12]. Selon l'hypothèse propre au dossier (annexe 1.4), qui déroge expressément à l'hypothèse générale, les écarts de conversion ne sont imposés ou déduits qu'au règlement : la base fiscale reste au cours historique (0,25 pt).
- Créance : valeur IFRS 1 728 000 € < base fiscale 1 800 000 € : différence déductible de 72 000 €, **impôt différé actif de 18 000 €** (la perte sera déduite en 2027) (0,25 pt).
- Dette : valeur IFRS 1 440 000 € < base fiscale 1 500 000 € : le gain sera imposé au paiement, différence imposable de 60 000 €, **impôt différé passif de 15 000 €** (0,25 pt).
- La provision, non déductible, n'avait pas réduit l'impôt exigible de VALBOGIE ; elle disparaît en IFRS sans autre conséquence. Incidence nette sur le résultat : 60 000 + 18 000 – 15 000 = **+ 63 000 €** (0,25 pt).

**C3 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1515 Provisions pour pertes de change | 72 000 | |
| 477 Différences de conversion – Passif | 60 000 | |
| IDA Impôt différé actif (72 000 × 25 %) | 18 000 | |
| 476 Différence de conversion – Actif | | 72 000 |
| IDP Impôt différé passif (60 000 × 25 %) | | 15 000 |
| RST.VALBOGIE Résultat VALBOGIE | | 63 000 |
| **Total** | **150 000** | **150 000** |
| | *Libellé : écarts de change latents portés en résultat selon IAS 21* | | |

La créance et la dette restent inscrites à leur valeur au cours de clôture (1 728 000 € et 1 440 000 €).

**C3R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 666 Pertes de change financières | 72 000 | |
| RES_CR Résultat | 63 000 | |
| 6865 Dotations aux provisions financières | | 72 000 |
| 766 Gains de change financiers | | 60 000 |
| CH_ID Produit net d'impôt différé (18 000 – 15 000) | | 3 000 |
| **Total** | **135 000** | **135 000** |

**Réponses tolérées (1.4)**
- En a, retraitement des frais regroupé avec l'écriture d'élimination des titres (titres crédités pour 13 560 000 € et charge de 360 000 € au résultat de FERVALIS).
- En c, impôts différés présentés pour leur solde net (actif de 3 000 €) si le calcul par élément est montré ; deux écritures distinctes pour la créance et la dette.

**Erreurs fréquentes (1.4)**
- Frais laissés dans le coût des titres en IFRS ou retenus nets d'impôt comme en règlement ANC (`JUR-G02`, erreur symétrique).
- Perte réalisée de 75 000 € retraitée ; perte latente ajoutée à la dotation (double comptage) ; gain latent laissé hors résultat.
- Impôt différé calculé sur la seule incidence en résultat (15 000 € de passif) en oubliant l'actif sur la créance, ou conclusion « aucun impôt différé » reprise d'un autre cas sans lire l'hypothèse fiscale.

**Références normatives (1.4)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 53 ; ANC 2020-01 art. 231-2 | Frais connexes en charges ; comparaison ANC | [V] | F05 § 1.1, § 2 |
| PCG art. 420-5 | Conversion au cours de clôture, comptes 476 et 477, provision | [V] | F04 R12 |
| IAS 21 § 21, 23 a), 28 | Cours du jour, cours de clôture, écarts en résultat | [V] | F04 R12, § 11 |
| IAS 12 § 5, 15, 24 | Différences temporelles imposables et déductibles | [V] | F04 § 1, R12 |

---

### 1.5 Opérations internes (5 pts)

#### a. Comptes réciproques (1,5 pt)

**Rapprochement (0,5 pt).** Créance déclarée par VALBOGIE : 1 200 000 – 500 000 = 700 000 € ; dette déclarée par STRIBEUX Freinage : 1 200 000 – 500 000 – 400 000 = 300 000 € ; écart **400 000 €** : le virement émis le 30/12/2026 n'est arrivé chez VALBOGIE que le 04/01/2027. Pour le groupe, ces fonds sont en transit ; le manuel les inscrit en trésorerie de la destinataire (annexe 1.2, point 4). On ne peut éliminer des soldes réciproques qu'après les avoir rendus égaux.

**C4 (bilan, 0,5 pt)** : débit 512 Banques (fonds en transit) 400 000 ; crédit 411 Clients 400 000. *Libellé : virement de STRIBEUX Freinage en transit, inscrit chez VALBOGIE.*

**C5 (bilan, 0,5 pt)** : débit 404 Fournisseurs d'immobilisations 300 000 ; crédit 411 Clients 300 000. *Libellé : élimination des soldes réciproques.* Ces éliminations sont sans incidence sur le résultat [V IFRS 10 B86 c) ; ANC art. 251-1, principe identique ; F04 R14]. La vente elle-même n'a pas de charge réciproque chez STRIBEUX Freinage, qui l'a immobilisée : son élimination fait l'objet de la question c.

#### b. Résultat interne sur le banc d'essai (1,5 pt)

| Élément | Montant |
|---|---:|
| Plus-value interne : 1 200 000 – 960 000 (0,25 pt) | 240 000 |
| Amortissement de 2026 chez STRIBEUX Freinage : 1 200 000 / 10 × 6/12 | 60 000 |
| Amortissement pour le groupe : 960 000 / 10 × 6/12 | 48 000 |
| Excédent d'amortissement à annuler (0,25 pt) | – 12 000 |
| **Élimination avant impôt** (0,25 pt) | **228 000** |
| Impôt différé actif, 25 % | 57 000 |
| **Élimination nette** | **171 000** |

Pour le groupe, le banc est une immobilisation produite par lui-même, au coût de 960 000 € : la plus-value interne est éliminée en totalité et l'actif ramené à son coût, l'amortissement étant recalculé sur ce coût [V IFRS 10 B86 c) ; F04 R14]. La valeur consolidée (912 000 €) est inférieure à la base fiscale chez STRIBEUX Freinage (1 140 000 €) : **impôt différé actif** [V IAS 12 § 24 ; F04 R14] (0,25 pt).

**Répartition (0,5 pt).** Le résultat interne a été réalisé par VALBOGIE, la vendeuse : l'élimination est imputée à son résultat [V ANC art. 251-2, principe identique ; F04 R14 ; annexe 1.2, point 4]. L'excédent d'amortissement n'est que la réalisation progressive, par l'utilisation du banc, de la plus-value de VALBOGIE : il lui est imputé aussi. VALBOGIE étant détenue à 100 %, l'élimination porte en totalité sur la part du groupe : **aucun effet sur les PNC**, bien que le banc soit utilisé par STRIBEUX Freinage, détenue à 80 % (0,25 pt). Si STRIBEUX Freinage avait été la vendeuse, 20 % de l'élimination auraient réduit les PNC (0,25 pt).

#### c. Écritures (2 pts)

**C6 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.VALBOGIE Résultat VALBOGIE (228 000 × 75 %) | 171 000 | |
| IDA Impôt différé actif (228 000 × 25 %) | 57 000 | |
| 28154 Amortissements des matériels industriels | 12 000 | |
| 2154 Matériels industriels | | 240 000 |
| **Total** | **240 000** | **240 000** |
| | *Libellé : élimination de la plus-value interne sur le banc d'essai* | | |

**C6R (compte de résultat, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 701 Ventes de produits finis (VALBOGIE) | 1 200 000 | |
| 722 Production immobilisée – Immobilisations corporelles | | 960 000 |
| 6811 Dotations aux amortissements (excédent annulé) | | 12 000 |
| CH_ID Produit d'impôt différé | | 57 000 |
| RES_CR Résultat | | 171 000 |
| **Total** | **1 200 000** | **1 200 000** |

La vente interne disparaît du chiffre d'affaires consolidé ; les coûts de production engagés par VALBOGIE, qui restent dans les charges par nature, sont neutralisés par la production immobilisée, comme pour un bien produit par le groupe pour lui-même.

**Réponses tolérées (1.5)** : correction du transit et élimination regroupées (débit 512 400 000 et 404 300 000, crédit 411 700 000) ; C6R présentée en deux écritures (élimination de la vente contre la production immobilisée et le résultat ; correction de l'amortissement) ; excédent d'amortissement imputé au résultat de STRIBEUX Freinage et partagé à 80 / 20, s'il est justifié (effet sur les PNC de 12 000 × 75 % × 20 % = 1 800 €) : 0,25 pt perdu en b seulement, le manuel imputant la correction au vendeur.

**Erreurs fréquentes (1.5)** : écart de 400 000 € corrigé en annulant une partie de la vente, ou laissé sans correction ; plus-value éliminée sans correction de l'amortissement ; élimination partagée à 80 / 20 « parce que l'actif est chez STRIBEUX Freinage » ; vente éliminée contre des achats inexistants ; impôt différé omis (`JUR-G05`).

**Références normatives (1.5)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 B86 c) | Élimination complète des opérations intragroupe | [V] | F04 R14 |
| ANC 2020-01 art. 251-1, 251-2 | Comptes réciproques ; résultat imputé à la société qui l'a réalisé (principe identique) | [V] | F04 R14 |
| IAS 12 § 24 | Impôt différé actif | [V] | F04 § 1, R14 |

---

### 1.6 Acquisition de STRIBEUX Freinage (7 pts)

#### a. Contrepartie transférée (1,5 pt)

| Élément | Montant |
|---|---:|
| Prix payé comptant le 01/01/2026 : 16 000 × 825 € | 13 200 000 |
| Complément de prix à sa juste valeur au 01/01/2026 (0,5 pt) | 800 000 |
| **Contrepartie transférée** (0,5 pt) | **14 000 000** |
| Frais d'acquisition (en charges, question 1.4 a) (0,25 pt) | exclus |

La contrepartie transférée comprend tout passif résultant d'un accord de contrepartie éventuelle : l'acquéreur l'inclut pour sa **juste valeur à la date d'acquisition**, même si le paiement est incertain et lointain ; l'obligation de payer en trésorerie est un passif financier [V IFRS 3 § 37, 39, 40 ; F05 § 10 ; annexe 1.2, point 2] (0,25 pt). FERVALIS ne l'a pas comptabilisé dans ses comptes individuels : il est ajouté aux titres en consolidation (écriture C9).

#### b. Actif net identifiable acquis (1,5 pt)

En acquérant STRIBEUX Freinage, FERVALIS prend aussi le contrôle de STRIBEUX Services : l'actif net acquis est celui de l'ensemble. Les titres STRIBEUX Services inscrits chez STRIBEUX Freinage (500 000 €) sont remplacés par l'actif net de STRIBEUX Services [S F05 § 10] (0,5 pt).

| Élément | Montant |
|---|---:|
| Capitaux propres de STRIBEUX Freinage au 01/01/2026 | 10 900 000 |
| – Titres STRIBEUX Services | – 500 000 |
| + Capitaux propres de STRIBEUX Services au 01/01/2026 | + 1 600 000 |
| Technologie brevetée, non comptabilisée par l'acquise (0,25 pt) | + 2 400 000 |
| Écart d'évaluation du bâtiment : 4 300 000 – 3 100 000 | + 1 200 000 |
| Impôt différé passif : 3 600 000 × 25 % (0,25 pt) | – 900 000 |
| **Actif net identifiable à la juste valeur** (0,5 pt) | **14 700 000** |

Les actifs identifiables sont évalués à leur juste valeur, y compris une technologie séparable que l'acquise n'avait pas inscrite à son bilan ; les impôts différés des écarts sont constatés selon IAS 12 et affectent le goodwill [V IFRS 3 § 24 ; IAS 12 § 66 ; F05 § 2].

#### c. Goodwill partiel et PNC (1 pt)

| Élément | Montant |
|---|---:|
| Contrepartie transférée | 14 000 000 |
| – Quote-part de l'actif net identifiable : 80 % × 14 700 000 | – 11 760 000 |
| **Goodwill partiel** (0,5 pt) | **2 240 000** |

[V IFRS 3 § 19, 32 ; F05 § 2.1]. **PNC à la date d'acquisition (0,5 pt)** : 20 % × 14 700 000 = **2 940 000 €**, évaluées à leur quote-part de l'actif net identifiable selon le choix du groupe [V IFRS 3 § 19 ; annexe 1.2, point 2] ; elles ne comprennent aucune part de goodwill. Le goodwill n'est pas amorti ; aucune perte de valeur n'est à constater en 2026 (annexe 1.2).

#### d. Révision du complément de prix au 31/12/2026 (1,5 pt)

**Règle (0,5 pt).** Les variations de juste valeur d'une contrepartie éventuelle qui résultent d'**événements postérieurs** à la date d'acquisition, comme la réalisation d'un objectif de résultat, ne corrigent pas l'évaluation faite à cette date : une contrepartie payable en trésorerie est évaluée à la juste valeur à chaque clôture, ses variations étant comptabilisées **en résultat** [V IFRS 3 § 58 b) ; F05 § 10].

**Application (1 pt).** La hausse de 800 000 € à 1 000 000 € résulte des performances de 2026, postérieures à l'acquisition (annexe 1.6) (0,25 pt) : le passif est porté à 1 000 000 € et la variation de **200 000 €** est une charge de 2026 (autres charges financières, selon le manuel) (0,25 pt) ; le **goodwill reste de 2 240 000 €** (0,25 pt) ; aucun impôt différé (hypothèse de l'annexe 1.6). Résultat consolidé : **– 200 000 €**, imputé à FERVALIS, acquéreur débiteur du complément (0,25 pt).

#### e. Écritures (1,5 pt)

**C7 (bilan, écarts d'évaluation au 01/01/2026, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Brevets (technologie de freinage à récupération d'énergie) | 2 400 000 | |
| 2131 Bâtiments (usine de Douai) | 1 200 000 | |
| IDP Impôt différé passif (3 600 000 × 25 %) | | 900 000 |
| RSV.STRIBEUX_F Réserves STRIBEUX Freinage (écarts d'évaluation nets) | | 2 700 000 |
| **Total** | **3 600 000** | **3 600 000** |

**C8 (bilan, amortissement de 2026, 0,25 pt)** : débit RST.STRIBEUX_F 270 000 ; débit IDP 90 000 ; crédit 2805 Amortissements des brevets (2 400 000 / 8) 300 000 ; crédit 28131 Amortissements des bâtiments (1 200 000 / 20) 60 000. **C8R (compte de résultat, 0,25 pt)** : débit 6811 Dotations aux amortissements 360 000 ; crédit CH_ID Produit d'impôt différé 90 000 ; crédit RES_CR Résultat 270 000.

**C9 (bilan, complément de prix à la date d'acquisition, 0,25 pt)** : débit 261.FERVALIS Titres STRIBEUX Freinage 800 000 ; crédit 1687 Autres dettes (complément de prix à payer) 800 000.

**C10 (bilan, réévaluation, 0,25 pt)** : débit RST.FERVALIS 200 000 ; crédit 1687 Autres dettes 200 000. **C10R** : débit 668 Autres charges financières 200 000 ; crédit RES_CR Résultat 200 000.

**Réponses tolérées (1.6)**
- En b, actif net calculé en deux temps (STRIBEUX Freinage réévaluée, puis remplacement des titres STRIBEUX Services par sa quote-part de capitaux propres) ; goodwill calculé sur STRIBEUX Freinage seule (2 240 000 + 880 000 = 3 120 000 €), puis diminué de la quote-part du groupe dans les réserves de STRIBEUX Services à l'acquisition, si le goodwill final est de 2 240 000 € : 0,25 pt perdu en b.
- En e, C7 et C9 regroupées avec l'écriture d'élimination des titres ; complément de prix crédité à un compte 404, 467 ou à un compte de consolidation « dette sur acquisition de titres ».

**Erreurs fréquentes (1.6)**
- Complément de prix ignoré (goodwill de 1 440 000 €) ou retenu pour sa valeur de clôture (goodwill de 2 440 000 €) ; frais inclus dans la contrepartie (goodwill de 2 600 000 €).
- Titres STRIBEUX Services laissés dans l'actif net acquis à 500 000 € (actif net de 13 600 000 €, goodwill de 3 120 000 €) ; technologie oubliée ou non amortie ; impôt différé omis sur les écarts (`JUR-G06`).
- Réévaluation du complément portée en goodwill ; goodwill complet calculé alors que le manuel retient le goodwill partiel.

**Références normatives (1.6)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 19, 24, 32, 37, 39, 40 | PNC, impôts différés, goodwill, contrepartie éventuelle à la date d'acquisition | [V] | F05 § 2, § 10 |
| IFRS 3 § 58 b) ; IFRS 9 § 4.2.1 e) | Contrepartie éventuelle réévaluée en résultat | [V] | F05 § 10 |
| IAS 12 § 66 | Impôts différés d'un regroupement | [V] | F05 § 2 |
| Sous-filiale acquise avec sa mère | Actif net de l'ensemble acquis | [S] | F05 § 10 |

---

### 1.7 Partage des capitaux propres et mise en équivalence (7 pts)

#### a. Tableaux de partage au 31/12/2026 (2,5 pts)

**VALBOGIE (intérêt 100 %) (0,5 pt)**

| Capitaux propres retraités | Total | Groupe (100 %) |
|---|---:|---:|
| Capital | 3 000 000 | 3 000 000 |
| Réserves : 14 600 000 + 1 050 000 (développement) | 15 650 000 | 15 650 000 |
| – Titres VALBOGIE éliminés | | – 3 000 000 |
| **Réserves consolidées** | | **15 650 000** |
| Résultat retraité : 3 900 000 + 975 000 + 63 000 – 171 000 | 4 767 000 | **4 767 000** |

**STRIBEUX Freinage (intérêt 80 %) (1 pt)**

| Capitaux propres retraités | Total | Groupe (80 %) | PNC (20 %) |
|---|---:|---:|---:|
| Capital | 2 000 000 | 1 600 000 | 400 000 |
| Réserves (comptes individuels) | 8 900 000 | 7 120 000 | 1 780 000 |
| Écarts d'évaluation nets | 2 700 000 | 2 160 000 | 540 000 |
| **Sous-total** | **13 600 000** | **10 880 000** | **2 720 000** |
| – Titres STRIBEUX Freinage (13 560 000 – 360 000 + 800 000) | | – 14 000 000 | |
| + Goodwill partiel | | + 2 240 000 | |
| **Réserves consolidées / PNC hors résultat** | | **– 880 000** | **2 720 000** |
| Résultat retraité : 1 870 000 – 270 000 | 1 600 000 | **1 280 000** | **320 000** |

**STRIBEUX Services (intérêt 80 %) (1 pt)**

| Capitaux propres | Total | Groupe (80 %) | PNC (20 %) |
|---|---:|---:|---:|
| Capital | 500 000 | 400 000 | 100 000 |
| Réserves (acquises le 01/01/2026) | 1 100 000 | 880 000 | 220 000 |
| – Titres détenus par STRIBEUX Freinage (500 000), répartis 80 % / 20 % | | – 400 000 | – 100 000 |
| **Réserves consolidées / PNC hors résultat** | | **880 000** | **220 000** |
| Résultat | 300 000 | **240 000** | **60 000** |

Les titres STRIBEUX Services ont été payés par STRIBEUX Freinage, qui appartient pour 80 % au groupe et pour 20 % au fondateur : leur élimination se répartit de la même façon. Les réserves de STRIBEUX Services existaient à la date d'acquisition : la quote-part du groupe (880 000 €) fait partie de l'actif net acquis (question 1.6 b) et se compense avec la ligne – 880 000 € de STRIBEUX Freinage. **Le sous-groupe STRIBEUX n'apporte aucune réserve consolidée** au 31/12/2026, ce qui est normal pour une acquisition du 01/01/2026. PNC au 31/12/2026 : 2 720 000 + 220 000 + 320 000 + 60 000 = **3 320 000 €** (= 20 % × 14 700 000 + 380 000).

#### b. Mise en équivalence d'AMÉNORAIL (1,5 pt)

| | Total | Quote-part du groupe (50 %) |
|---|---:|---:|
| Capital | 4 000 000 | 2 000 000 |
| Réserves | 3 200 000 | 1 600 000 |
| Résultat de 2026 | 1 200 000 | 600 000 |
| **Valeur de la participation mise en équivalence** (0,25 pt) | 8 400 000 | **4 200 000** |
| – Titres AMÉNORAIL éliminés | | – 2 000 000 |
| **Réserves consolidées : 50 % × 7 200 000 – 2 000 000** (0,25 pt) | | **1 600 000** |
| **Quote-part du résultat** (0,25 pt) | | **600 000** |

Créée par FERVALIS, AMÉNORAIL ne donne lieu à aucun goodwill ni écart d'évaluation.

**Dividende (0,75 pt).** Les distributions reçues d'une entité mise en équivalence **réduisent la valeur comptable de la participation** [V IAS 28 § 10 ; F05 § 4] : les 400 000 € reçus prélèvent le résultat de 2025 d'AMÉNORAIL, déjà compris pour 700 000 € dans le résultat consolidé de 2025 ; les laisser en produits le compterait deux fois. Le dividende est éliminé du résultat de FERVALIS et reclassé en réserves (C13) ; la valeur d'équivalence est calculée sur les capitaux propres après distribution. Contrôle : 50 % × 8 000 000 = 4 000 000 au 31/12/2025 ; + 600 000 ; – 400 000 ; = **4 200 000 €**.

#### c. Écritures (3 pts)

**C11 (bilan, VALBOGIE, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.VALBOGIE Capital VALBOGIE | 3 000 000 | |
| RSV.VALBOGIE Réserves retraitées | 15 650 000 | |
| RST.VALBOGIE Résultat retraité | 4 767 000 | |
| 261.FERVALIS Titres VALBOGIE | | 3 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 15 650 000 |
| RST_G Résultat consolidé – part du groupe | | 4 767 000 |
| **Total** | **23 417 000** | **23 417 000** |

**C12 (bilan, sous-groupe STRIBEUX, 1,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.STRIBEUX_F Capital STRIBEUX Freinage | 2 000 000 | |
| RSV.STRIBEUX_F Réserves (8 900 000 + 2 700 000) | 11 600 000 | |
| RST.STRIBEUX_F Résultat retraité | 1 600 000 | |
| CAP_ELIM.STRIBEUX_S Capital STRIBEUX Services | 500 000 | |
| RSV.STRIBEUX_S Réserves STRIBEUX Services | 1 100 000 | |
| RST.STRIBEUX_S Résultat STRIBEUX Services | 300 000 | |
| EA Goodwill partiel | 2 240 000 | |
| 261.FERVALIS Titres STRIBEUX Freinage (après C2 et C9) | | 14 000 000 |
| 261.STRIBEUX_F Titres STRIBEUX Services | | 500 000 |
| RST_G Résultat consolidé – part du groupe (1 280 000 + 240 000) | | 1 520 000 |
| RSV_M PNC – quote-part de l'actif net identifiable (20 % × 14 700 000) | | 2 940 000 |
| RST_M PNC – résultat (320 000 + 60 000) | | 380 000 |
| **Total** | **19 340 000** | **19 340 000** |
| | *Libellé : élimination des titres du sous-groupe STRIBEUX, goodwill partiel et partage* | | |

Aucune réserve consolidée n'est créditée : les – 880 000 € et + 880 000 € des deux tableaux se compensent. Le résultat éliminé de STRIBEUX Freinage est celui que laisse C8 ; ses réserves comprennent les écarts nets de C7 ; les titres sont ceux que laissent C2 et C9.

**C13 (bilan, dividende d'AMÉNORAIL, 0,25 pt avec C13R)** : débit RST.FERVALIS 400 000 ; crédit RSV.FERVALIS 400 000. **C13R** : débit 7611 Revenus des titres de participation 400 000 ; crédit RES_CR 400 000.

**C14 (bilan, mise en équivalence, 0,75 pt avec C14R)**

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence (AMÉNORAIL) | 4 200 000 | |
| 261.FERVALIS Titres AMÉNORAIL | | 2 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 1 600 000 |
| RST_G Résultat consolidé – part du groupe | | 600 000 |
| **Total** | **4 200 000** | **4 200 000** |

**C14R** : débit RES_CR Résultat 600 000 ; crédit QP_MEE Quote-part du résultat net des entités mises en équivalence 600 000.

**Réponses tolérées (1.7)**
- C12 présentée en deux écritures (STRIBEUX Freinage avec le goodwill et un débit de RSV_G de 880 000 € ; STRIBEUX Services avec un crédit de RSV_G de 880 000 €), si les montants sont justes.
- Partage de STRIBEUX Services présenté en deux temps (part de STRIBEUX Freinage, puis répartition 80 / 20) ; goodwill présenté hors du tableau de STRIBEUX Freinage.
- Cohérence avec un résultat erroné aux questions 1.3 à 1.6 : l'erreur n'est pénalisée qu'une fois (`JUR-F08`).

**Erreurs fréquentes (1.7)**
- Réserves de STRIBEUX Services (880 000 €) portées en réserves consolidées alors qu'elles sont antérieures à l'acquisition ; titres STRIBEUX Services éliminés en totalité sur la part du groupe (`JUR-G04`).
- Partage sur les capitaux propres individuels, sans les écarts d'évaluation ni les retraitements ; PNC de STRIBEUX Services nulles « parce qu'elle est détenue à 100 % ».
- Dividende d'AMÉNORAIL conservé en produits ou ajouté à la valeur d'équivalence (`JUR-G03`) ; écritures déséquilibrées (`JUR-F04`).

**Références normatives (1.7)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 22, B86 | PNC dans les capitaux propres ; élimination des titres | [V] | F03 § 3, F05 § 3 |
| IFRS 3 § 19, 32 | Goodwill partiel, PNC à la quote-part de l'actif net | [V] | F05 § 2 |
| IAS 28 § 10 | Mise en équivalence, distributions | [V] | F05 § 4 |

---

### 1.8 Passage au résultat net consolidé (3 pts)

| Phase | Élément | Résultat de l'ensemble | Part du groupe | PNC |
|---|---|---:|---:|---:|
| | Somme des résultats individuels des sociétés intégrées : 6 400 000 + 3 900 000 + 1 870 000 + 300 000 (0,25 pt) | 12 470 000 | 12 036 000 | 434 000 |
| 1. Retraitements d'homogénéisation | Développement de VALBOGIE (1.3) | + 975 000 | + 975 000 | 0 |
| | Écarts de change latents de VALBOGIE (1.4 c) | + 63 000 | + 63 000 | 0 |
| | Frais d'acquisition des titres, chez FERVALIS (1.4 a) | – 360 000 | – 360 000 | 0 |
| 2. Éliminations des opérations internes | Comptes réciproques et transit (1.5 a) | 0 | 0 | 0 |
| | Banc d'essai, imputé à VALBOGIE (1.5 b) | – 171 000 | – 171 000 | 0 |
| 3. Élimination des titres et partage (regroupement) | Amortissement des écarts d'évaluation de STRIBEUX Freinage (1.6 e) | – 270 000 | – 216 000 | – 54 000 |
| | Réévaluation du complément de prix, chez FERVALIS (1.6 d) | – 200 000 | – 200 000 | 0 |
| 4. Mise en équivalence | Élimination du dividende d'AMÉNORAIL (1.7 b) | – 400 000 | – 400 000 | 0 |
| | Quote-part du résultat d'AMÉNORAIL (1.7 b) | + 600 000 | + 600 000 | 0 |
| | **Résultat net consolidé** | **12 707 000** | **12 327 000** | **380 000** |

**Barème** : 0,25 pt pour la ligne de départ et sa répartition (les résultats de STRIBEUX Freinage et de STRIBEUX Services sont répartis 80 / 20, ceux de FERVALIS et de VALBOGIE vont au groupe) ; 1,5 pt pour les lignes, montant et phase justes (0,25 pt pour chacun des six groupes : développement et change ; frais d'acquisition ; comptes réciproques et banc d'essai ; écarts d'évaluation ; complément de prix ; dividende et quote-part d'AMÉNORAIL) ; 0,5 pt pour les colonnes du groupe et des PNC (seuls les écarts d'évaluation touchent les PNC : 20 % × 270 000 = 54 000 €, les autres éléments concernent FERVALIS ou VALBOGIE, détenue à 100 %) ; 0,75 pt pour les trois totaux.

Contrôle par les partages : FERVALIS 6 400 000 – 360 000 – 200 000 – 400 000 = 5 440 000 ; VALBOGIE 4 767 000 ; STRIBEUX Freinage 1 280 000 ; STRIBEUX Services 240 000 ; AMÉNORAIL 600 000 ; total **12 327 000 €**. PNC : 320 000 + 60 000 = **380 000 €**.

L'ordre des phases traduit la logique du processus : les comptes individuels sont d'abord rendus conformes aux méthodes du groupe, puis les opérations internes éliminées, avant l'élimination des titres et le partage, qui portent sur des capitaux propres et des résultats **retraités** ; la mise en équivalence substitue enfin à la participation non intégrée sa quote-part de capitaux propres [V IFRS 10 § 19, B86 ; IAS 28 § 10 ; F04 § 1 ; F03 § 3].

**Réponses tolérées (1.8)** : frais d'acquisition et complément de prix rangés tous deux dans la phase du regroupement (élimination des titres) ou tous deux dans les retraitements (ajustements des comptes de FERVALIS selon IFRS 3), ou écarts d'évaluation rangés dans les retraitements (évaluation à la juste valeur des actifs acquis), si la justification est donnée ; dividende d'AMÉNORAIL rangé parmi les éliminations des opérations internes ; tableau partant du résultat de chaque société retraitée, s'il aboutit aux mêmes totaux.

**Erreurs fréquentes (1.8)** : résultat d'AMÉNORAIL cumulé ; quote-part ajoutée sans éliminer le dividende ; part des PNC calculée à 20 % de tous les retraitements, y compris ceux de VALBOGIE ; élimination des titres présentée avant les retraitements (`JUR-G01`).

---

### 1.9 Documents de synthèse (6 pts)

#### a. Tableau des flux de trésorerie (4 pts)

**Incidence de chaque élément (3 pts, 0,5 pt par élément)**

| Élément | Activité | Incidence en 2026 | Justification |
|---|---|---:|---|
| Acquisition de STRIBEUX Freinage | Investissement | – 11 800 000 | Prix payé comptant 13 200 000 – trésorerie des sociétés acquises (1 100 000 + 300 000) : présentée séparément, nette de la trésorerie acquise [V IAS 7 § 39, 42 ; F14 § 3] |
| Frais d'acquisition (payés en janvier 2026) | Opérationnelle | – 360 000 (compris dans le résultat) | Charges selon IFRS 3 : ils n'aboutissent à aucun actif et ne peuvent pas être classés en investissement [V IAS 7 § 16 ; F14 § 9] |
| Complément de prix (800 000 puis 1 000 000) | Aucun flux | 0 | Partie de la contrepartie non payée en trésorerie : opération sans effet de trésorerie, mentionnée en note [V IAS 7 § 40, 43] ; la réévaluation de 200 000 €, sans effet de trésorerie, est réintégrée au résultat dans la méthode indirecte [V IAS 7 § 20] |
| Dépenses de développement de 2026 | Investissement : 1 600 000 ; opérationnelle : 150 000 | – 1 600 000 | Frais de développement inscrits à l'actif [V IAS 7 § 16 a) ; F14 § 9] ; l'amortissement (300 000 €) est réintégré au résultat ; les dépenses laissées en charges restent dans les flux opérationnels |
| Banc d'essai | Investissement | – 960 000 | Coûts payés à des tiers par VALBOGIE pour une immobilisation produite par le groupe pour lui-même [V IAS 7 § 16 a)] ; les règlements de STRIBEUX Freinage à VALBOGIE (900 000 €) sont internes et éliminés |
| AMÉNORAIL | Investissement : dividende + 400 000 | + 400 000 | Seuls les flux entre le groupe et l'entité mise en équivalence figurent au tableau [V IAS 7 § 37, 38] ; la quote-part de résultat (600 000 €), sans effet de trésorerie, est déduite du résultat [V IAS 7 § 20] ; classement du dividende selon le choix permanent du groupe [V IAS 7 § 31, 33 ; annexe 1.2, point 6] |

**Extrait des flux de trésorerie liés aux activités d'investissement de 2026 (1 pt)**

| Flux liés aux activités d'investissement | Montant |
|---|---:|
| Acquisition d'immobilisations incorporelles (développement) | – 1 600 000 |
| Acquisition d'immobilisations corporelles (banc d'essai) | – 960 000 |
| Acquisition de filiale, nette de la trésorerie acquise | – 11 800 000 |
| Dividende reçu de la coentreprise | + 400 000 |
| **Total de l'extrait** | **– 13 960 000** |

Les flux d'investissement sont présentés en montants bruts [V IAS 7 § 21 ; F14 § 3]. Les notes indiqueront, pour l'acquisition, la contrepartie totale (14 000 000 €), la part payée en trésorerie (13 200 000 €), la trésorerie des sociétés acquises (1 400 000 €) et leurs actifs et passifs par grandes catégories [V IAS 7 § 40 ; F14 § 3]. Le paiement du complément, en 2028, sera un flux de cet exercice-là.

#### b. Présentation, notes, différence avec le règlement ANC (2 pts)

**Présentation (0,5 pt).** La participation dans AMÉNORAIL figure sur la ligne des participations comptabilisées selon la méthode de la mise en équivalence, en actif non courant (4 200 000 €) [V IAS 1 § 54 e), 66 ; F14 § 2.2]. Le complément de prix est un passif financier (1 000 000 €), **non courant** puisqu'il sera payé le 30/04/2028, plus de douze mois après la clôture [V IFRS 3 § 40 ; IAS 1 § 69 ; F14 § 2.2].

**Notes (1 pt, 0,5 pt par thème)**
- **Coentreprise** : jugements qui ont conduit à retenir le contrôle conjoint (unanimité du pacte) et la qualification de coentreprise (droits sur l'actif net seulement) [V IFRS 12 § 7 b), c) ; F03 § 10] ; nom, activité, établissement (Maubeuge), pourcentage détenu (50 %), mise en équivalence et informations financières résumées (capitaux propres de 8 400 000 €, résultat de 1 200 000 €, dividende de 800 000 €) [V IFRS 12 § 21 ; F03 § 10].
- **Complément de prix** : montant comptabilisé à la date d'acquisition (800 000 €) dans la contrepartie totale de 14 000 000 € ; description de l'accord (40 % de l'excédent du résultat d'exploitation cumulé de 2026 et 2027 sur 2 500 000 €, payable le 30/04/2028) et fourchette des montants possibles ; pour 2026, variation du montant comptabilisé (+ 200 000 € en résultat) et ses raisons, techniques d'évaluation [V IFRS 3 B64 f), g), B67 b) ; F05 § 10].

**Différence avec le règlement ANC (0,5 pt, une seule attendue)**
- le modèle ANC classe les **dividendes reçus des sociétés mises en équivalence** dans les flux liés à l'activité, alors qu'IAS 7 laisse un choix permanent (ici l'investissement) [V ANC art. 282-43 ; IAS 7 § 31-34 ; F14 § 1.5, § 4] ;
- ou : le modèle ANC part du résultat net des entités intégrées et fait apparaître une marge brute d'autofinancement, IAS 7 du résultat avec des ajustements, ou de la méthode directe, encouragée [V art. 282-43 ; IAS 7 § 18-20 ; F14 § 1.5, § 3] ;
- ou : la trésorerie IFRS peut comprendre les découverts remboursables à vue [V IAS 7 § 8 ; F14 § 4] ;
- ou : en règlement ANC, le tableau des flux figure dans l'annexe et n'est pas un état de synthèse distinct [V art. 282-41 ; F14 § 4].

(Une réponse sur les frais d'acquisition, qui entreraient dans le coût d'acquisition en règlement ANC et suivraient donc le flux d'investissement, est acceptée si elle est présentée comme une conséquence d'une différence de comptabilisation.)

**Réponses tolérées (1.9)**
- En a, dividende d'AMÉNORAIL classé en activités opérationnelles avec mention que le manuel retient l'investissement : 0,25 pt perdu ; frais d'acquisition présentés comme un ajustement nul de la méthode indirecte, s'il est dit qu'ils restent dans les flux opérationnels.
- En b, participation mise en équivalence présentée parmi les actifs financiers non courants, si la ligne distincte est mentionnée.

**Erreurs fréquentes (1.9)**
- Acquisition présentée pour 13 200 000 € ou pour 14 000 000 € (complément compris) ; frais d'acquisition classés en investissement « comme le coût des titres dans les comptes individuels ».
- Complément de prix présenté comme un décaissement de 2026 ; dépenses de développement laissées en flux opérationnels ; règlements internes du banc maintenus dans le tableau.
- Quote-part de résultat d'AMÉNORAIL présentée comme un encaissement ; IFRS 18 appliquée à 2026.

**Références normatives (1.9)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 7 § 16 a), 20, 21, 31, 33, 37, 38, 39, 40, 42, 43 | Investissement, méthode indirecte, dividendes, entités mises en équivalence, acquisition de filiale, opérations sans effet de trésorerie | [V] | F14 § 3, § 9 |
| IAS 1 § 54 e), 66, 69 | Ligne de la participation mise en équivalence ; courant / non courant | [V] | F14 § 2.2 |
| IFRS 12 § 7, 21 ; IFRS 3 B64 f), g), B67 b) | Informations sur la coentreprise et sur la contrepartie éventuelle | [V] | F03 § 10 ; F05 § 10 |
| ANC 2020-01 art. 282-41, 282-43 | Tableau des flux de trésorerie consolidé | [V] | F14 § 1.5, § 4 |

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 a) Qualification et référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 1 |
| 2.1 b) Contrôle, sens de l'opération et mode d'évaluation des apports | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 2,5 |
| 2.1 c) Régime fiscal de faveur | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 2 |
| 2.2 a) Valeurs d'échange, parité, actions attribuées, répartition du capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 3 |
| 2.2 b) Soulte de la première version et soulte de rompus, plafond légal, équité | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 2,5 |
| 2.3 Actif net apporté, composition et prime de fusion | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 2 |
| 2.4 a) Écritures chez HOUBLEVAL | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 2,5 |
| 2.4 b) Augmentation de capital, soulte et réalisation des apports chez la brasserie | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 1,5 |
| 2.4 c) Actions propres reçues : conservation ou annulation, réduction de capital | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes | 4,5 |
| 2.4 d) Frais de fusion | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 1,5 |
| 2.5 Note au directeur général | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Analyse de l'opération (5,5 pts)

**a) Qualification et référentiel (1 pt)**
- L'opération est une **fusion-absorption** : HOUBLEVAL transmet l'ensemble de son patrimoine, actif et passif, à la BRASSERIE VALMONDIÈRE (**transmission universelle**) ; elle est **dissoute sans liquidation** ; ses associés reçoivent des actions de l'absorbante, émises par augmentation de capital, et une soulte en numéraire [V PCG art. 710-2, renvoi à C. com. L. 236-1, F01 § 1] (0,5 pt).
- Particularité : c'est l'**absorbée qui détient 72 % de l'absorbante**. Le patrimoine transmis comprend donc 36 000 actions de la brasserie, que celle-ci reçoit sur elle-même : ses **propres actions**. À l'inverse, la brasserie ne détient aucune action HOUBLEVAL : il n'y a ni quote-part non rémunérée, ni boni, ni mali ; les 24 000 actions HOUBLEVAL sont toutes rémunérées (0,25 pt).
- L'enregistrement relève, dans les comptes individuels des deux sociétés, du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe la valeur d'inscription des apports [V art. 710-1 et 720-1, F01 § 1] ; la parité, elle, se calcule sur les valeurs d'échange, indépendamment de cette valeur d'inscription [V art. 740-1, F01 § 1] (0,25 pt).

**b) Contrôle, sens de l'opération et mode d'évaluation (2,5 pts)**

*Situation de contrôle (0,75 pt).* HOUBLEVAL détient 72 % des droits de vote de la brasserie, et aucun accord ne lie les actionnaires familiaux : elle la contrôle **de manière exclusive** (majorité des droits de vote) [V art. 741-2, renvoi à l'art. 211-3 du règlement ANC 2020-01, F01 § 2.1]. L'une des sociétés participantes contrôle l'autre avant l'opération : la fusion est réalisée **sous contrôle commun** [V art. 741-1, F01 § 2.1]. Le texte vise l'entité qui contrôle l'autre, qu'elle soit l'absorbante ou l'absorbée ; le contrôle s'apprécie entre les deux personnes morales, peu importe que HOUBLEVAL appartienne à des personnes physiques.

*Sens de l'opération (0,75 pt).* Avant la fusion, l'actionnaire principal de l'absorbante est HOUBLEVAL (72 %). La fusion fait disparaître HOUBLEVAL : elle ne conserve pas le contrôle de la brasserie. Ce sont ses associés, liés par leur pacte, qui détiennent directement **65,85 %** du capital et des droits de vote de la brasserie après l'opération (voir 2.2 a), contre 34,15 % aux actionnaires familiaux. Les associés de l'absorbée prennent le contrôle de l'absorbante : la fusion est **à l'envers** [V art. 742-2, F01 § 2.2]. La cible est l'absorbante (la brasserie, société opérationnelle), l'initiatrice est l'absorbée : les dirigeants qui contrôlaient la brasserie par l'intermédiaire de la holding la contrôlent désormais directement.

*Mode d'évaluation (1 pt).* Sous contrôle commun, les apports sont évalués à la **valeur comptable**, que la fusion soit à l'endroit ou à l'envers : l'opération maintient un contrôle existant, il convient de ne pas réévaluer [V art. 743-1, cas 2, F01 § 2.3] (0,5 pt). Le sens ne modifie donc pas la conclusion ; il ne la modifierait pas davantage sous contrôle distinct, puisqu'une fusion à l'envers est alors aussi évaluée à la valeur comptable (cas 3) (0,25 pt). Les apports sont repris pour leurs valeurs au bilan de HOUBLEVAL du 30/09/2026 [V art. 744-2, F01 § 3.2] : les actions de la brasserie pour leur coût historique (5 400 000 €), non pour leur valeur d'échange (7 200 000 €). L'actif net comptable apporté (3 600 000 €, voir 2.3) dépasse l'augmentation de capital (1 079 920 €) : l'exception qui imposerait les valeurs réelles en cas d'actif net comptable insuffisant ne joue pas [V art. 743-3, F01 § 2.4] (0,25 pt).

**c) Régime fiscal de faveur (2 pts)**
- *Conditions (0,5 pt).* Les deux sociétés sont soumises à l'impôt sur les sociétés. Le régime de faveur s'applique à la fusion, sauf option pour le droit commun, si l'absorbante prend dans le traité les engagements de l'art. 210 A-3 du CGI ; la brasserie les prend (annexe 2.3) [V CGI art. 210 A et 210 C-1 ; BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1 et § 4].
- *Chez HOUBLEVAL (0,75 pt).*
  - Le principal élément apporté, les 36 000 actions de la brasserie, porte une plus-value latente de 36 000 × (200 – 150) = **1 800 000 €**. Sous le régime de faveur, les plus-values dégagées sur les éléments apportés **ne sont pas imposées** chez l'absorbée [V 210 A-1, F02 § 2] ; en droit commun, la fusion serait assimilée à une cessation d'entreprise et ces plus-values seraient imposées immédiatement [V BOI-IS-FUS-10-10-10 § 1, F02 § 2] (0,5 pt).
  - Le bénéfice de la période du 01/01 au 30/09/2026 est imposé immédiatement chez HOUBLEVAL, quel que soit le régime : l'impôt correspondant (21 000 €) est une dette transmise à la brasserie, qui le paiera [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2]. HOUBLEVAL n'a ni provision ni déficit reportable : aucun sort particulier n'est à régler (0,25 pt).
- *Chez la brasserie (0,75 pt).* Elle reprend les valeurs fiscales de HOUBLEVAL. Les apports étant comptabilisés à la valeur comptable, aucune plus-value n'est constatée ni à réintégrer [V BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2]. Les actions reçues sont des immobilisations non amortissables de l'absorbée : si la brasserie les cédait au lieu de les annuler, la plus-value serait calculée d'après leur valeur fiscale chez HOUBLEVAL (150 € par action) [V 210 A-3-c, F02 § 4]. Leur annulation est une opération sur le capital, sans incidence sur le résultat comptable. Les frais de fusion sont déductibles de son résultat de 2026 (annexe 2.3).

---

### 2.2 Parité, actions attribuées et soulte (5,5 pts)

**a) Valeurs d'échange, parité, actions attribuées et répartition du capital (3 pts)**
- *Valeur unitaire de la brasserie (0,25 pt)* : 10 000 000 / 50 000 = **200 €**.
- *Valeur d'échange de HOUBLEVAL (0,5 pt)*, selon le traité : 36 000 × 200 + 75 000 – 1 800 000 – 54 000 – 21 000 = 7 200 000 – 1 800 000 = **5 400 000 €**, soit 5 400 000 / 24 000 = **225 €** par action. La dette nette de HOUBLEVAL (emprunt, intérêts courus et impôt, moins les disponibilités) vaut 1 800 000 €.
- *Parité (0,25 pt)* : 225 / 200 = **9 / 8**, soit 9 actions BRASSERIE VALMONDIÈRE pour 8 actions HOUBLEVAL [V méthode du corrigé du sujet zéro, F01 § 4].
- *Actions à rémunérer (0,25 pt)* : la brasserie ne détient aucune action HOUBLEVAL : les **24 000** actions HOUBLEVAL sont rémunérées.
- *Actions attribuées et rompus (0,75 pt)* : 24 000 × 9 / 8 = 27 000 actions en théorie ; mais aucun associé ne détient un multiple de 8 actions, et leurs droits ne tombent pas sur des nombres entiers :

| Associé de HOUBLEVAL | Actions HOUBLEVAL | Droits (× 9 / 8) | Actions attribuées | Rompu |
|---|---:|---:|---:|---:|
| M. Grégoire DUCASTEL | 10 450 | 11 756,25 | 11 756 | 0,25 |
| Mme Claire ROUVELAIN | 3 350 | 3 768,75 | 3 768 | 0,75 |
| M. Hugues TERNISIEN | 5 100 | 5 737,50 | 5 737 | 0,50 |
| Mme Inès MARQUILLE | 5 100 | 5 737,50 | 5 737 | 0,50 |
| **Total** | **24 000** | **27 000** | **26 998** | **2** |

  La brasserie émet **26 998 actions** ; augmentation de capital : 26 998 × 40 = **1 079 920 €**.
- *Répartition du capital après la fusion (0,75 pt)*. Les 36 000 actions reçues de HOUBLEVAL sont annulées (voir 2.4 c) : 50 000 + 26 998 – 36 000 = **40 998 actions**.

| Actionnaire | Avant (détention) | % avant | Après (actions) | % après |
|---|---|---:|---:|---:|
| HOUBLEVAL | 36 000 actions | 72,00 % | – | – |
| M. Grégoire DUCASTEL | indirecte (43,54 % de HOUBLEVAL) | 31,35 % | 11 756 | 28,67 % |
| Mme Claire ROUVELAIN | indirecte (13,96 % de HOUBLEVAL) | 10,05 % | 3 768 | 9,19 % |
| M. Hugues TERNISIEN | indirecte (21,25 % de HOUBLEVAL) | 15,30 % | 5 737 | 13,99 % |
| Mme Inès MARQUILLE | indirecte (21,25 % de HOUBLEVAL) | 15,30 % | 5 737 | 13,99 % |
| *Associés de HOUBLEVAL ensemble* | *indirecte* | *72,00 %* | *26 998* | *65,85 %* |
| Actionnaires familiaux | 14 000 actions | 28,00 % | 14 000 | 34,15 % |
| **Total des actions** | **50 000** | | **40 998** | **100 %** |

  (Total des pourcentages arrondis après l'opération : 99,99 %. Les pourcentages « indirects » d'avant l'opération, 72 % × part dans HOUBLEVAL, sont donnés pour comparaison.) Chaque action donnant une voix, les droits de vote suivent la même répartition ; les associés de HOUBLEVAL, qui votent ensemble, gardent la majorité.
- *Pourquoi moins de 72 % (0,25 pt).* Avant l'opération, les 72 % des associés de HOUBLEVAL étaient grevés de la dette nette de la holding (1 800 000 €) : leur participation valait 7 200 000 – 1 800 000 = 5 400 000 €, soit 75 % de la valeur des 36 000 actions détenues. Ils reçoivent donc environ 27 000 actions pour 36 000 actions annulées. La brasserie reprend la dette ; sa valeur passe à 10 000 000 – 1 800 000 – 400 = 8 199 600 €, soit 8 199 600 / 40 998 = **200 €** par action : la valeur de l'action est inchangée, et la part des actionnaires familiaux augmente (34,15 %) parce qu'ils supportent désormais, eux aussi, la dette d'acquisition.

**b) Soulte, plafond légal et équité (2,5 pts)**
- *Contrainte légale (0,25 pt).* La soulte en espèces ne peut pas dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-1, F01 § 4].
- *Première version du projet (1 pt).* 24 000 actions attribuées et une soulte de 24 000 × 25 = **600 000 €** ; l'échange était équitable (24 000 × 200 + 600 000 = 5 400 000 €), mais le plafond était de 10 % × 24 000 × 40 = **96 000 €** : la soulte le dépassait plus de six fois, elle était **illégale**. Conseil : réduire la soulte en attribuant davantage d'actions. Pour n actions attribuées, la soulte vaut 5 400 000 – 200 n et le plafond 4 n : il faut au moins 5 400 000 / 204 = 26 470,6, soit **26 471 actions**. La solution la plus simple consiste à appliquer la parité exacte (9 pour 8) et à limiter la soulte aux rompus ; elle évite en outre à la brasserie de décaisser 600 000 € au moment où elle reprend la dette de la holding.
- *Soulte du projet de traité (0,5 pt).* Rompus payés à 200 € l'action : M. DUCASTEL 0,25 × 200 = 50 € ; Mme ROUVELAIN 0,75 × 200 = 150 € ; M. TERNISIEN et Mme MARQUILLE 0,5 × 200 = 100 € chacun ; soulte totale : 2 × 200 = **400 €**.
- *Plafond (0,5 pt).* 10 % × 26 998 × 40 = **107 992 €** ; la soulte (400 €) en représente 0,37 % : **elle est légale**. Elle l'est aussi associé par associé (par exemple, Mme ROUVELAIN : 150 € pour un plafond de 10 % × 3 768 × 40 = 15 072 €).
- *Équité (0,25 pt).* Actions remises et soulte : 26 998 × 200 + 400 = 5 400 000 € = valeur des actions HOUBLEVAL reçues (24 000 × 225) [V méthode du corrigé du sujet zéro, F01 § 4].

---

### 2.3 Actif net apporté, composition et prime de fusion (2 pts)

- *Actif net apporté à la valeur comptable (0,75 pt)* = actifs – dettes = 5 475 000 – 1 875 000 = **3 600 000 €**, égal aux capitaux propres de HOUBLEVAL (2 400 000 + 60 000 + 1 077 000 + 63 000).
- *Composition (0,5 pt)* :

| Élément apporté | Valeur comptable |
|---|---:|
| 36 000 actions BRASSERIE VALMONDIÈRE (coût d'acquisition de 2021) | 5 400 000 |
| Disponibilités | 75 000 |
| Emprunt auprès d'un établissement de crédit | – 1 800 000 |
| Intérêts courus sur l'emprunt | – 54 000 |
| État – impôt sur les sociétés de la période | – 21 000 |
| **Actif net apporté** | **3 600 000** |

  Hors les actions de la brasserie, les apports se réduisent à une dette nette de 1 800 000 € : l'apport est positif seulement grâce aux propres actions de la brasserie.
- *Écart avec la valeur d'échange (0,25 pt)* : 5 400 000 – 3 600 000 = 1 800 000 €, la plus-value latente sur les actions de la brasserie, non constatée puisque les apports sont à la valeur comptable.
- *Prime de fusion avant toute imputation (0,5 pt)* = actif net apporté – augmentation de capital – soulte = 3 600 000 – 1 079 920 – 400 = **2 519 680 €** [V F01 § 4 et § 9].

---

### 2.4 Écritures (10 pts)

**a) Chez HOUBLEVAL, le 30 septembre 2026 (2,5 pts)**

L'apport étant évalué à la valeur comptable, la créance sur l'absorbante est égale à l'actif net comptable : la fusion ne dégage **aucun résultat** chez HOUBLEVAL.

**A1 — Transmission de l'actif et du passif (1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – BRASSERIE VALMONDIÈRE, compte d'apport | 3 600 000 | |
| 164 Emprunts auprès des établissements de crédit | 1 800 000 | |
| 1648 Intérêts courus sur emprunts auprès des établissements de crédit | 54 000 | |
| 444 État – Impôts sur les bénéfices | 21 000 | |
| 261 Titres de participation (36 000 actions BRASSERIE VALMONDIÈRE) | | 5 400 000 |
| 512 Banques | | 75 000 |
| **Total** | **5 475 000** | **5 475 000** |

**A2 — Droits des associés sur l'actif net (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 2 400 000 | |
| 1061 Réserve légale | 60 000 | |
| 1068 Autres réserves | 1 077 000 | |
| 120 Résultat de l'exercice – bénéfice (01/01 au 30/09/2026) | 63 000 | |
| 456 Associés – Opérations sur le capital | | 3 600 000 |

**A3 — Partage entre les associés (0,5 pt).** La brasserie remet directement aux associés les 26 998 actions nouvelles et la soulte (annexe 2.3) : leurs droits sont éteints par l'extinction de la créance sur l'absorbante.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital | 3 600 000 | |
| 467 Divers comptes débiteurs – BRASSERIE VALMONDIÈRE, compte d'apport | | 3 600 000 |

Après A1 à A3, tous les comptes de HOUBLEVAL sont soldés.

**b) Chez la brasserie, le 30 septembre 2026 : augmentation de capital et apports (1,5 pt)**

**A4 — Augmentation de capital et soulte de rompus (0,75 pt).** Tout l'apport est rémunéré.

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 3 600 000 | |
| 101 Capital (26 998 × 40) | | 1 079 920 |
| 1042 Primes de fusion | | 2 519 680 |
| 512 Banques (soulte de rompus) | | 400 |

**A5 — Réalisation des apports à la valeur comptable (0,75 pt).** Les propres actions reçues sont inscrites, pour leur valeur d'apport, au compte des actions propres en voie d'annulation [V PCG art. 1212-27, F01 § 6].

| Compte | Débit | Crédit |
|---|---:|---:|
| 2772 Actions propres ou parts propres en voie d'annulation (36 000 actions) | 5 400 000 | |
| 512 Banques | 75 000 | |
| 164 Emprunts auprès des établissements de crédit | | 1 800 000 |
| 1648 Intérêts courus sur emprunts auprès des établissements de crédit | | 54 000 |
| 444 État – Impôts sur les bénéfices (impôt de HOUBLEVAL pour la période) | | 21 000 |
| 4561 Associés – Comptes d'apport en société | | 3 600 000 |
| **Total** | **5 475 000** | **5 475 000** |

**c) Actions propres reçues : conservation ou annulation (4,5 pts)**

*Comparaison des deux solutions (1,5 pt).*

| | Conservation | Annulation (projet de traité) |
|---|---|---|
| Capital de la brasserie | 50 000 + 26 998 = 76 998 actions, dont 36 000 détenues par la société elle-même (46,75 % du capital) | 40 998 actions, toutes détenues par des actionnaires |
| Droits attachés aux actions propres | Ni droit de vote ni dividende (annexe 2.4) : les droits de vote et les dividendes se répartissent de toute façon sur 40 998 actions | Sans objet |
| Contrainte légale | La société possède plus de 10 % de son capital : les actions doivent être cédées dans les deux ans, puis annulées à défaut (annexe 2.4) | Aucune |
| Faisabilité | Aucun acquéreur, ni fonds disponibles pour les racheter (annexe 2.5) : l'annulation serait inévitable au bout de deux ans | Immédiate |
| Bilan | 5 400 000 € d'actions propres à l'actif, sans valeur économique pour la brasserie, et des capitaux propres qui en comprennent la contrepartie | Capitaux propres réduits de la valeur des actions annulées : le bilan traduit la reprise de la dette nette |

Conservées, les actions seraient privées de droits et devraient être cédées dans les deux ans ; personne ne peut les acheter. L'annulation immédiate, retenue par le projet de traité, aboutit à la même répartition du pouvoir (65,85 % / 34,15 %) sans attendre, et donne un capital qui ne compte que des actions détenues par des actionnaires. Barème : conservation analysée avec l'annexe (0,75), annulation et justification du choix (0,75).

*Ni boni ni mali (0,75 pt).* Le boni ou le mali naît de l'annulation des titres de l'**absorbée** que l'absorbante détenait ; ici la brasserie ne détient aucune action HOUBLEVAL. Elle reçoit ses **propres** actions : l'écart entre leur valeur d'apport (150 € l'une) et leur nominal (40 €) ne correspond à aucun actif. L'inscrire en mali reviendrait à comptabiliser un incorporel généré en interne ; le PCG exclut tout mali sur l'annulation des propres titres de l'absorbante, qui s'enregistre **par capitaux propres**, selon les règles de l'annulation d'actions propres rachetées [V art. 745-3 et 1212-27 ; recueil ANC p. 398, F01 § 6].

*Effets sur les capitaux propres (1 pt).*
- Réduction de capital : 36 000 × 40 = **1 440 000 €** ; capital après l'opération : 2 000 000 + 1 079 920 – 1 440 000 = **1 639 920 €**, soit 40 998 actions de 40 € (0,25 pt).
- Excédent de la valeur d'apport sur le nominal : 5 400 000 – 1 440 000 = **3 960 000 €**, à imputer sur un compte distribuable de capitaux propres (annexe 2.4) (0,25 pt).
- Prime de fusion disponible après l'imputation des frais (voir d) : 2 519 680 – 45 000 = 2 474 680 € : elle est **insuffisante** ; elle est soldée, et le surplus, 3 960 000 – 2 474 680 = **1 485 320 €**, est imputé sur les autres réserves, qui passent de 3 100 000 € à 1 614 680 € (0,5 pt).

**A7 — Annulation des actions propres reçues (1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital (36 000 × 40) | 1 440 000 | |
| 1042 Primes de fusion (solde) | 2 474 680 | |
| 1068 Autres réserves (surplus) | 1 485 320 | |
| 2772 Actions propres ou parts propres en voie d'annulation | | 5 400 000 |
| **Total** | **5 400 000** | **5 400 000** |

Le compte 4567 « Associés – Capital à rembourser » ne convient pas : aucune somme n'est due aux associés [V art. 1214-45, F01 § 6]. Après A4, A5 et A7, le compte 4561 et le compte 2772 sont soldés.

**d) Frais de fusion (1,5 pt)**
- *Traitement (0,5 pt).* Les frais de fusion peuvent être inscrits à l'actif en frais d'établissement, ou imputés sur les primes d'émission et de fusion ; en cas d'insuffisance, ils sont comptabilisés en charges [V PCG art. 212-9, F01 § 7]. La brasserie choisit l'imputation sur la prime de fusion, avant toute autre imputation (annexe 2.3) : la prime de 2 519 680 € est alors suffisante.
- *Montant (0,5 pt).* Ils sont imputés **nets d'impôt** [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 60 000 × 75 % = **45 000 €** ; l'économie d'impôt (15 000 €) diminue l'impôt sur les sociétés de 2026. Absents du résultat comptable, les frais sont déduits extra-comptablement.

**A6 — Frais de fusion (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (60 000 × 75 %) | 45 000 | |
| 444 État – Impôts sur les bénéfices (60 000 × 25 %) | 15 000 | |
| 512 Banques | | 60 000 |

HOUBLEVAL n'ayant ni provisions réglementées ni subvention d'investissement, aucune reconstitution n'est à passer ; il n'existe aucune dette ou créance entre les deux sociétés à éteindre (annexe 2.1).

---

### 2.5 Note à M. DUCASTEL, directeur général de la BRASSERIE VALMONDIÈRE (2 pts)

**Capitaux propres juste après la fusion (1 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (nombre d'actions : 50 000 → 40 998) | 2 000 000 | + 1 079 920 – 1 440 000 | 1 639 920 |
| Primes de fusion | 0 | + 2 519 680 – 45 000 – 2 474 680 | 0 |
| Réserve légale | 200 000 | | 200 000 |
| Autres réserves | 3 100 000 | – 1 485 320 | 1 614 680 |
| **Total, hors résultat de l'exercice** | **5 300 000** | **– 1 845 400** | **3 454 600** |

Contrôle : – 1 845 400 = actif net apporté (3 600 000) – actions propres annulées (5 400 000) – soulte (400) – frais nets d'impôt (45 000), soit la dette nette reprise de HOUBLEVAL (– 1 800 000), la soulte et les frais : les capitaux propres baissent de 34,82 %. Barème : tableau (0,5), total et contrôle (0,5).

**Enjeux pour les parties prenantes (1 pt)**
- *Banque (0,25 pt).* Son débiteur n'est plus une holding qui ne vivait que des dividendes de la brasserie (dont elle ne recevait que 72 %), mais la société qui produit la trésorerie : elle a un accès direct aux flux et aux actifs de la brasserie. En contrepartie, l'endettement financier de la brasserie passe de 1 250 000 € à 1 250 000 + 1 800 000 + 54 000 = **3 104 000 €**, et le rapport entre ses emprunts (hors intérêts courus) et ses capitaux propres de 0,24 à (1 250 000 + 1 800 000) / 3 454 600 = **0,88** ; elle devra payer chaque année 300 000 € de capital, plus les intérêts, jusqu'en 2031.
- *Actionnaires familiaux (0,25 pt).* Leur part passe de 28 % à 34,15 % et la valeur de leur action reste de 200 € : l'échange est équitable. Mais la brasserie rembourse désormais elle-même la dette contractée en 2021 pour racheter ses actions : leurs dividendes futurs dépendent de la trésorerie qui restera après le service de cette dette. Les réserves distribuables tombent de 3 100 000 € à 1 614 680 € (la prime de fusion est soldée) : la brasserie peut toujours distribuer, mais sa capacité de distribution est réduite d'autant, alors qu'elle doit aussi rembourser 300 000 € par an. Ils restent minoritaires face aux associés de HOUBLEVAL (65,85 %).
- *Autres créanciers (0,25 pt).* Les fournisseurs et les autres créanciers voient les capitaux propres baisser de 1,85 M€ et le capital ramené à 1 639 920 € : la sécurité qu'ils représentaient diminue, alors que la brasserie reprend 1 875 000 € de dettes pour 75 000 € de disponibilités.
- *Dirigeants (0,25 pt).* Une société de moins (frais de structure, comptes et déclarations de la holding supprimés), des dirigeants qui détiennent directement leurs actions, 40 998 actions en circulation au lieu de 50 000, et un dividende désormais versé à tous les actionnaires sans passer par la holding.

---

### Réponses tolérées
- **2.1 b** : sens de l'opération justifié directement par le contrôle que l'absorbée exerçait sur l'absorbante, si la conclusion (valeur comptable sous contrôle commun, quel que soit le sens) est correcte.
- **2.2 a** : parité exprimée en nombre décimal (1,125 action BRASSERIE VALMONDIÈRE pour une action HOUBLEVAL) ; répartition présentée aussi avant l'annulation, si la répartition après l'annulation est donnée et commentée.
- **2.2 b** : rompus réglés par achat ou vente entre associés, mentionnés comme autre solution, si la soulte prévue par le traité est calculée.
- **2.4 a** : réception des actions et de la soulte par HOUBLEVAL, puis attribution aux associés, si le candidat écrit l'hypothèse ; comptes 44 ou 447 au lieu de 444.
- **2.4 b** : soulte portée au crédit d'un compte de tiers (467 ou 468), puis versée par une écriture distincte.
- **2.4 c** : réception des actions propres et annulation réunies en une seule écriture (débit 101, 1042 et 1068, crédit 4561), si l'absence de mali est justifiée.
- **2.4 d** : frais en deux écritures (1042 / 512 pour 60 000 €, puis 444 / 1042 pour 15 000 €), ou passage préalable en 6226 Honoraires puis transfert sur la prime par le crédit du compte de charge, si la prime ne supporte que 45 000 €.
- **2.5** : toute présentation chiffrée et cohérente ; ratio d'endettement calculé avec les intérêts courus de HOUBLEVAL (3 104 000 / 3 454 600 = 0,90).

### Erreurs fréquentes (rapports du jury)
- `JUR-R05` Difficulté à s'adapter à une situation un peu différente : opération traitée comme une fusion-renonciation (quote-part non rémunérée de 72 %, 7 560 actions émises), alors que c'est l'absorbée qui détient l'absorbante ; « mali » de 3 960 000 € constaté sur l'annulation des actions propres ; actions propres laissées à l'actif ; fusion jugée à l'endroit au vu d'une répartition qui oublie l'annulation (26 998 / 76 998 = 35,06 %).
- `JUR-R01` Prime de fusion mal calculée : oubli de la soulte (2 520 080 €), prime calculée sur la valeur d'échange (5 400 000 – 1 079 920 – 400 = 4 319 680 €), ou prime diminuée dès l'écriture A4 de la valeur des actions propres.
- `JUR-F07` Annexes mal exploitées : valeur de HOUBLEVAL calculée sans les intérêts courus ni l'impôt de la période (5 475 000 €, soit 228,13 € par action) ; actions propres reprises pour leur valeur d'échange (7 200 000 €) au lieu de leur coût ; surplus de l'excédent imputé sur la réserve légale ; frais imputés pour leur montant brut.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1, A5 et A7.
- `JUR-F06` Hypothèses non écrites (ordre d'imputation des frais et de l'excédent sur la prime).
- Erreurs propres à ce cas :
  - plafond de la soulte calculé sur le nominal des actions HOUBLEVAL ou sur la valeur des apports, au lieu du nominal des actions de la brasserie attribuées ;
  - nombre d'actions arrondi au total (27 000) sans tenir compte des droits de chaque associé ;
  - réduction de capital comptabilisée au compte 4567, comme s'il fallait rembourser les associés ;
  - résultat de fusion constaté chez HOUBLEVAL alors que l'apport est à la valeur comptable.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 710-1, 710-2, 720-1, 740-1 | Champ du titre VII, définition de la fusion, inscription des apports, parité indépendante de leur évaluation | [V] p. 81-82 | F01 § 1 |
| PCG art. 741-1, 741-2, 742-2, 743-1, 743-3 | Contrôle commun, fusion à l'envers, valeur comptable (cas 2 et 3), exception de l'actif net insuffisant | [V] p. 82-85 | F01 § 2 |
| PCG art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170-180 | Apports à la valeur comptable, valeurs fiscales reprises | [V] p. 85 | F01 § 3.2 |
| C. com. L. 236-1 ; corrigé du sujet zéro | Soulte limitée à 10 % du nominal des actions attribuées ; parité réduite et équité | [V] Légifrance ; p. imprimée 214 | F01 § 4 |
| PCG art. 745-3, 1212-27, 1214-45 ; recueil ANC p. 398 ; comptes 2772, 4567 | Aucun mali sur les propres actions reçues ; annulation par capitaux propres, excédent sur un compte distribuable | [V] p. 86, 161, 169 | F01 § 6 |
| C. com. L. 225-210 al. 4, L. 225-213 | Actions propres privées de vote et de dividende ; cession dans les deux ans au-delà de 10 % du capital, puis annulation | [V] édition codes.droit.org du 01/10/2026 | F01 § 6 (complément du 14/11/2026) |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime de fusion, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| CGI art. 210 A-1, 210 A-3 (c), 210 C-1 ; BOI-IS-FUS-10-10-10 § 1, 10 et 20 ; BOI-IS-FUS-10-20-30 § 210 et 330 | Régime de faveur : exonération des plus-values chez l'absorbée, imposition du résultat de la dernière période, valeur fiscale des immobilisations non amortissables | [V] | F02 § 1, § 2 et § 4 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Désignation obligatoire du commissaire aux comptes d'une association subventionnée ; seuils des personnes morales non commerçantes ; durée du mandat ; suppléant | `3.1.b` Nomination et cessation | 2 |
| 3.2 Paie et dette de congés payés demandées au commissaire aux comptes : cadres d'exercice, services interdits, autorévision, immixtion | `3.1.a` Cadres d'exercice professionnel ; `3.1.c` Principes déontologiques | 2 |
| 3.3 Secret professionnel opposé à un financeur public : levées, sanctions, informations accessibles | `3.1.e` Mise en cause de la responsabilité ; `3.1.c` Principes déontologiques | 2 |
| 3.4 Certification, contrôle des financeurs et examen interne ; risque et assertions du cycle personnel et paie | `3.2.a` Notion d'audit et typologie des missions ; `3.2.c` Approche par les risques | 4 |
| 3.5 Procédure analytique de substance avec un extrait de NEP ; procédures complémentaires ; refus d'accès aux dossiers et moyens d'action | `3.1.d` Référentiel normatif (NEP) ; `3.2.d` Démarche d'audit ; `3.2.b` Moyens d'action du CAC | 5,5 |
| 3.6 Anomalies, écritures, opinion selon les corrections | `3.2.e` Portée des opinions ; `3.2.c` Caractère significatif ; `3.2.d` Démarche d'audit | 2,5 |
| 3.7 GRI, ISSB, ESRS : objet et interopérabilité | `3.3.a` Contexte et architecture des normes de durabilité | 2 |
| 3.8 Parties prenantes affectées et utilisateurs ; dialogue ; horizons de temps ; faiblesses de l'analyse | `3.3.b` Principes de construction du reporting | 4 |
| 3.9 Objectifs de la mission et assurance limitée ; procédures sur le processus de dialogue | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4 |
| 3.10 Impossibilité d'émettre un avis sur le processus ; comparaison avec la réserve et la non-conformité ; structure | `3.4.c` Portée des avis | 2 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Désignation du commissaire aux comptes d'une association subventionnée (2 pts)

**Fondement de l'obligation (0,75 pt)**
- Toute association qui reçoit annuellement des autorités administratives une ou plusieurs **subventions en numéraire** dont le montant global dépasse **153 000 €** doit établir des comptes annuels, assurer leur publicité et celle du rapport du commissaire aux comptes, et **nommer au moins un commissaire aux comptes** [V L. 612-4 al. 1-2 ; D. 612-5].
- Subventions retenues : le département (400 000 € en 2026, 380 000 € en 2025) et les trois communes (62 000 €, 58 000 €), soit **462 000 €** en 2026 et **438 000 €** en 2025. Le seuil est dépassé sans même compter les aides de l'État au poste (1 128 600 € en 2026), dont la qualification n'a donc pas à être tranchée.
- Montants exclus : les dons de la Fondation OLMARÈDE, fondation de droit privé, qui n'est pas une autorité administrative ; la mise à disposition gratuite des terres et du hangar (42 000 €), subvention en nature et non en numéraire.
- L'obligation est **propre aux associations subventionnées** : elle ne dépend ni de l'effectif ni des ressources.

**Réponse à M. DORMEUIL sur les seuils (0,5 pt)**
- Il invoque les seuils des personnes morales de droit privé non commerçantes ayant une activité économique, qui doivent désigner un commissaire aux comptes lorsqu'elles dépassent deux des trois critères suivants : **50 salariés**, **3 100 000 €** de chiffre d'affaires hors taxes ou de ressources, **1 550 000 €** de total du bilan [V L. 612-1 al. 1-2 ; R. 612-1].
- Seuls comptent les salariés en **contrat à durée indéterminée** (moyenne des effectifs de fin de trimestre) [V R. 612-1 1°] : 18 en 2026. Les 74 salariés en parcours, en contrats à durée déterminée, n'entrent pas dans le calcul. Les ressources (2 378 600 €) restent sous le seuil ; seul le total du bilan (1 645 000 €) le dépasse. Un seul critère sur trois : cette règle n'impose pas, à elle seule, la désignation.
- Son raisonnement est donc exact sur ces seuils, mais il ne vise pas le bon texte : l'obligation résulte des subventions publiques reçues.

**Durée et terme du mandat ; mandat de trois exercices (0,5 pt)**
- Le commissaire aux comptes est nommé pour **six exercices** ; ses fonctions expirent après la délibération de l'organe qui statue sur les comptes du sixième exercice [V L. 821-44 al. 1]. La résolution de 2024 n'avait pas à préciser cette durée légale. Le mandat couvre les exercices **2024 à 2029** ; il expire après l'assemblée générale qui statuera sur les comptes de 2029, en 2030 [S, application].
- La limitation à **trois exercices** est réservée à la désignation faite **par une société**, de manière volontaire ou au titre du premier ou du dernier alinéa de L. 821-43 (petits groupes) [V L. 821-46]. VERTELIS Insertion n'est pas une société, et sa désignation est imposée par la loi : le prochain mandat sera aussi de six exercices.

**Suppléant (0,25 pt)** : il n'est obligatoire que si le titulaire est une personne physique ou une société unipersonnelle [V L. 612-4 al. 2 ; L. 821-40 I al. 3]. CAMBRELLE est une société qui compte quatre associés commissaires aux comptes : aucun suppléant n'est requis.

**Réponses tolérées**
- Une réponse qui retient les aides au poste parmi les subventions des autorités administratives, si le seuil de 153 000 € et l'exclusion des dons de la fondation sont justifiés.
- L'omission de l'exclusion de la mise à disposition en nature, si la condition « en numéraire » est citée.

**Erreurs fréquentes**
- Appliquer les seuils des sociétés commerciales, ou compter les salariés en parcours pour conclure au dépassement de deux critères (`JUR-A05`).
- Proposer un mandat de trois exercices pour une désignation imposée par la loi (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 612-4, D. 612-5 | Associations subventionnées : seuil de 153 000 €, comptes, publicité, commissaire aux comptes | [V] ; application : [S] | F09 § 14 |
| C. com. L. 612-1, R. 612-1 | Personnes morales non commerçantes : trois critères, salariés en contrat à durée indéterminée | [V] | F09 § 14 |
| C. com. L. 821-44, L. 821-46, L. 821-40 I | Six exercices ; trois exercices réservés aux sociétés ; suppléant | [V] ; terme : [S] | F09 § 3.4-3.5, § 14 |

### 3.2 Paie et dette de congés payés demandées au commissaire aux comptes (2 pts)

**Cadres d'exercice (0,5 pt)**
- **Comme cabinet d'expertise comptable**, CAMBRELLE pourrait, dans le cadre d'une mission contractuelle définie par une lettre de mission, établir des bulletins de paie et des déclarations sociales pour un client, comme le font couramment les cabinets [V ord. 45-2138 art. 2 ; décret 2012-432 art. 151 ; S, application à la paie]. L'expert-comptable doit une indépendance d'esprit, compatible avec la production des documents de son client [V décret 2012-432 art. 145-146].
- **Comme commissaire aux comptes** de VERTELIS Insertion, il exerce une **mission légale** de certification. Tout autre service est une **prestation** [V L. 821-2 III-IV], qu'il ne peut fournir qu'en restant indépendant, en réalité et en apparence, et sans risque d'**autorévision** : il ne doit pas se prononcer sur des éléments résultant de ses propres prestations ou de celles de son cabinet [V code de déontologie art. 5 II, 19]. Ici, la qualité de commissaire aux comptes l'emporte.

**Services interdits et autorévision (1 pt)**
- La **liste des services interdits** ne s'applique qu'aux entités d'intérêt public [V L. 821-28 II]. VERTELIS Insertion n'en est pas une.
- Pour une autre entité, le commissaire aux comptes ne peut accepter ni poursuivre la certification s'il existe un **risque d'autorévision** que des mesures de sauvegarde ne peuvent pas traiter [V L. 821-28 IV ; code art. 19 I 2°, 3° et 5°].
- **Paie de 2027** : les bulletins et les déclarations produiraient les rémunérations, les charges sociales, les dettes sociales et les heures qui fondent les aides au poste de 2027. Le cabinet certifiera les comptes de 2027 (mandat jusqu'en 2029). Les rémunérations représentent 76,5 % des produits de 2026 (1 820 000 / 2 378 600). Le cabinet se prononcerait donc sur l'essentiel de son propre travail. Confier la paie à une autre équipe ne suffit pas : le risque vise aussi les prestations fournies par la société à laquelle appartient le commissaire aux comptes [V code art. 19 I 2° ; art. 5 II]. Aucune sauvegarde n'est possible : **refus**.
- **Dette de congés payés de 2026** : c'est un élément des comptes que le cabinet certifie, et une évaluation qui incombe à l'association. La calculer serait à la fois une **autorévision** et une **immixtion dans la gestion** [V L. 821-54 I] : **refus**.

**Ce que le cabinet peut proposer (0,5 pt)**
- Orienter l'association vers un autre cabinet d'expertise comptable ou un prestataire de paie qui n'appartient pas à son réseau [V code art. 5 II, 29-30 ; S, application].
- Pour la dette de congés payés, laisser l'association la calculer à partir des compteurs du logiciel de paie. Le cabinet la vérifiera ensuite dans sa mission : recalcul, rapprochement des bulletins.
- Signaler au conseil d'administration les risques liés au départ de la responsable de la paie [V L. 821-63 I].
- En cas de doute sérieux, saisir la H2A pour avis [V code art. 19 II].

**Réponses tolérées**
- Une réponse qui conclut au refus par la seule menace d'autorévision, sans distinguer les deux demandes : 0,5 pt sur 1.

**Erreurs fréquentes**
- Transposer au commissaire aux comptes l'indépendance d'esprit de l'expert-comptable, ou l'inverse (`JUR-A03`).
- Affirmer qu'une liste de services interdits s'applique à toute entité (`JUR-A01`).
- Accepter la paie en proposant une équipe distincte comme mesure de sauvegarde (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 2 ; décret 2012-432 art. 145-146, 151 | Missions, lettre de mission et indépendance de l'expert-comptable | [V] ; paie : [S] | F09 § 2.3 ; F10 § 2.2, 3 |
| C. com. L. 821-2, L. 821-28 II et IV, L. 821-54 I ; code de déontologie art. 5, 19, 29-30 | Mission et prestation ; services interdits des EIP ; autorévision hors EIP ; non-immixtion | [V] ; application : [S] | F10 § 3, 5 ; F09 § 6 |

### 3.3 Secret professionnel opposé au département (2 pts)

**Réponse au directeur de la solidarité (0,75 pt)**
- Le commissaire aux comptes, ses collaborateurs et ses experts sont astreints au **secret professionnel** pour les faits, actes et renseignements connus dans l'exercice de leur profession [V L. 821-35 al. 1].
- Les cas où il en est délié sont limitativement prévus. Il s'agit notamment du président du tribunal dans le cadre de la prévention des difficultés, des autres commissaires aux comptes ou organismes certificateurs dans les cas prévus par le texte, de la Commission nationale des comptes de campagne et de la H2A [V L. 821-35 ; L. 821-74 1°]. **Un financeur n'y figure pas**, même public.
- Le fait que le département finance l'association n'y change rien. Les honoraires sont à la charge de l'entité contrôlée [V L. 821-66 I], et le commissaire aux comptes certifie pour tous les utilisateurs des comptes, non pour l'un d'eux.
- Mme HERBELOT refuse donc de communiquer ses constats, même partiels, sur les comptes, la situation financière ou la paie. Elle oriente le directeur vers l'association et informe la présidente de cette demande [S].

**Risques en cas de communication (0,75 pt)**
- **Pénal** : délit de violation du secret professionnel [V L. 821-7 dernier al., renvoyant à C. pén. 226-13].
- **Disciplinaire** : manquement aux conditions légales d'exercice et aux règles de déontologie [V L. 821-70 I ; code art. 9]. Sanctions prononcées par la commission des sanctions de la H2A : avertissement, blâme, interdiction temporaire, radiation, sanction pécuniaire [V L. 821-71].
- **Civil** : réparation du préjudice causé à l'association si une faute, un préjudice et un lien de causalité sont établis [V L. 821-37 al. 1 ; S, conditions]. Par exemple, une subvention réduite au vu de constats provisoires.

**Informations accessibles au département (0,5 pt)**
- L'association peut elle-même communiquer ses informations : budget, situation de trésorerie, organisation de la paie.
- Après leur approbation, les comptes annuels et le rapport du commissaire aux comptes font l'objet d'une **publicité** [V L. 612-4 al. 1] ; la convention prévoit en outre leur remise au département dans les six mois de la clôture.
- La convention lui permet aussi d'obtenir un compte rendu de l'emploi de la subvention et de vérifier sur pièces et sur place l'emploi des fonds (annexe 3.3).
- Pour le vote du 05/02/2027, qui intervient avant l'achèvement des travaux du cabinet et la certification des comptes de 2026, le département s'adresse donc à l'association.

**Réponses tolérées**
- L'absence du détail des sanctions disciplinaires, si la nature des trois responsabilités est distinguée.

**Erreurs fréquentes**
- Admettre une communication au motif que le département est un financeur public ou qu'il « paie » le commissaire aux comptes (`JUR-A05`).
- Confondre responsabilité pénale, disciplinaire et civile (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-35, L. 821-74 ; code de déontologie art. 9 | Secret et cas de levée | [V] ; application : [S] | F10 § 2.1, 7 ; F09 § 14 |
| C. com. L. 821-7, L. 821-37, L. 821-70, L. 821-71 | Sanctions pénales, civiles, disciplinaires | [V] | F09 § 7 |
| C. com. L. 612-4 al. 1, L. 821-66 I | Publicité des comptes et du rapport ; honoraires | [V] | F09 § 14 ; F11 § 2 |

### 3.4 Notion d'audit et risque du cycle personnel et paie (4 pts)

**a. Trois interventions à distinguer (1,5 pt : 0,5 pt par intervention)**

| | Certification des comptes | Contrôles de l'État et du département | Examen du comité financier |
|---|---|---|---|
| Qualification | **Audit légal**, externe, imposé par la loi [V L. 612-4 ; L. 821-53] | Contrôle d'un **financeur** sur l'emploi de ses fonds, prévu par les conditions de l'aide et par la convention | Examen **interne**, par l'organe d'administration ; ce n'est pas une fonction d'audit interne indépendante des services [S] |
| Objet | Comptes annuels pris dans leur ensemble : régularité, sincérité, image fidèle | Heures déclarées et aides au poste (État) ; emploi de la subvention (département) | État trimestriel de la masse salariale et de la trésorerie |
| Intervenant et indépendance | Professionnel inscrit, indépendant de l'association et de ses financeurs | Le financeur lui-même, dans son propre intérêt | Deux administrateurs bénévoles, sur un état préparé par la comptable |
| Résultat | **Opinion** fondée sur une **assurance raisonnable**, rapport public | Reversement des aides indues, suite donnée aux financements | Information du conseil |

- Le commissaire aux comptes ne remplace aucun de ces contrôles et ne garantit pas la qualité de la gestion [V L. 821-55].
- Il tient compte de l'examen du comité financier comme d'une procédure de l'entité, pour apprécier le risque lié au contrôle [V NEP risques § 02 ; S, application].
- Le département utilise les comptes certifiés et le rapport du commissaire aux comptes, mais n'a aucun droit sur ses travaux (question 3.3).

**b. Risque d'anomalies significatives et assertions (2,5 pts)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41 ; NEP éléments probants § 9]

*Évaluation du risque (0,5 pt)*
- **Poids** : les rémunérations représentent 76,5 % des produits ; 112 contrats et renouvellements ont été signés pour 96 personnes en 2026.
- **Complexité** : taux réduits de cotisations, revalorisations à des dates différentes, aides proportionnelles aux heures rémunérées et versées par avance.
- **Changement** : départ de la responsable de la paie au 31/12/2026, sans remplaçante.
- **Procédures de l'entité** : une seule personne créait les salariés, saisissait les heures, établissait les bulletins et préparait les virements. Le risque de salariés fictifs ou de paiements indus n'est réduit que par la validation des virements par le directeur et par un examen trimestriel global : le risque lié au contrôle est élevé.
- **Pression** : excédent faible (36 000 €) ; vote des subventions de 2027 ; refus de la présidente de présenter un déficit.
- Sans test de l'efficacité des procédures, le risque au niveau des assertions correspond au risque inhérent [V NEP risques § 41]. Il est **élevé** : le cabinet privilégie les **procédures de substance** [V NEP réponses § 03-13].

*Risques et assertions (2 pts : 0,25 pt par couple pertinent, dans la limite de huit)*

| Élément | Risque tiré des annexes | Assertion |
|---|---|---|
| Rémunérations (flux) | Salarié fictif, ou salarié en parcours payé après la fin de son contrat (contrats successifs mal suivis) | **Réalité** |
| | Renouvellement non saisi : heures travaillées non payées ou non comptabilisées | **Exhaustivité** |
| | Revalorisation appliquée à une mauvaise date, salaires mal calculés | **Mesure** |
| | Heures supplémentaires des encadrants non autorisées ou mal calculées | **Réalité** ; **mesure** |
| | Heures supplémentaires de décembre payées en janvier, non rattachées à 2026 | **Séparation des exercices** |
| Charges sociales (flux) | Taux réduits appliqués à tort, par exemple après la fin d'un contrat ou à un encadrant | **Mesure** |
| Dettes sociales (soldes) | Dette de congés payés des salariés en parcours non comptabilisée | **Exhaustivité** |
| | Dette de congés payés des salariés permanents mal valorisée | **Évaluation et imputation** |
| Aides au poste (flux et soldes) | Aide de 2027, versée en décembre 2026, comptabilisée en produit de 2026 | **Séparation des exercices** |
| | Heures déclarées à l'État supérieures aux heures rémunérées : aide à reverser non comptabilisée | **Réalité** des produits ; **exhaustivité** des dettes |
| Présentation et annexe | Effectifs et aides mal présentés | **Présentation et intelligibilité** |

**Réponses tolérées**
- D'autres couples pertinents tirés des annexes.
- La qualification de l'examen du comité financier comme une forme d'audit interne, si son défaut d'indépendance envers la comptable est relevé.

**Erreurs fréquentes**
- Confondre la certification avec le contrôle des financeurs, ou présenter le commissaire aux comptes comme le contrôleur des aides publiques (`JUR-A01`).
- Développer l'organisation des procédures de l'entité au lieu d'en tirer le risque lié au contrôle (`JUR-F01`).
- Lister des risques généraux de la paie sans les tirer des annexes (`JUR-A05`, `JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 612-4, L. 821-53, L. 821-55 ; NEP principes § 01, 08-13 | Audit légal ; objectif ; assurance raisonnable | [V] ; typologie : [S] | F11 § 1 |
| NEP risques § 02, 39-41 ; NEP réponses § 03-13 ; NEP éléments probants § 9 | Facteurs de risque ; assertions ; procédures de substance | [V] | F11 § 4.1, 4.3, 5 |

### 3.5 Procédure analytique, procédures complémentaires et moyens d'action (5,5 pts)

**a. Recours à une procédure analytique de substance et conditions (1 pt)** [V NEP procédures analytiques § 03-07, 09 ; NEP éléments probants § 6 ; S, conditions de précision]
- Une procédure analytique de substance est une **procédure de substance**, au même titre que les tests de détail. Elle consiste à déterminer un **montant attendu** et un **écart acceptable**, puis à les comparer au montant enregistré.
- Le commissaire aux comptes **peut** l'utiliser pour une catégorie d'opérations significative, en réponse au risque évalué au niveau des assertions, lorsqu'elle est plus efficace, seule ou combinée, que les seuls tests de détail. C'est le cas des rémunérations : de nombreuses opérations homogènes, liées par une relation stable aux effectifs, aux salaires et aux revalorisations.
- **Conditions** pour qu'elle soit probante :
  - une attente **précise** : par catégorie, avec les dates de revalorisation et les heures supplémentaires à part [S] ;
  - des **données fiables**. Les ETP viennent ici d'un tableau de bord interne, établi par la responsable de la paie, qui a quitté l'association ; ce tableau doit être rapproché des déclarations sociales ;
  - un **écart acceptable** fixé à l'avance : 20 000 €, inférieur au seuil de planification de 33 750 € [S].
- Tout écart supérieur doit être **élucidé** par d'autres procédures.
- Le risque étant élevé, notamment de fraude, la procédure analytique ne suffit pas seule : elle est **combinée** à des tests de détail.

**b. Mise en œuvre (1,5 pt : 0,25 pt par catégorie, 0,25 pt pour le total et l'écart, 0,5 pt pour la conclusion)**

| Catégorie | ETP | Salaires mensuels de 2026 | Somme annuelle par ETP | Rémunérations attendues |
|---|---:|---|---:|---:|
| Salariés permanents | 8 | 3 100 × 1,02 = 3 162, douze mois | 37 944 | 303 552 |
| Encadrants techniques | 10 | 2 400 × 1,02 = 2 448, douze mois | 29 376 | 293 760 |
| Salariés en parcours | 52 | 1 800 de janvier à avril ; 1 800 × 1,015 = 1 827 de mai à décembre | 7 200 + 14 616 = 21 816 | 1 134 432 |
| Heures supplémentaires des encadrants | | | | 21 000 |
| **Rémunérations attendues** | | | | **1 752 744** |
| **Rémunérations comptabilisées** (641, hors variation des congés à payer) | | | | **1 820 000** |
| **Écart** | | | | **67 256**, soit 3,8 % de l'attendu |

- L'écart dépasse l'écart acceptable de 20 000 € : la procédure ne **corrobore pas** les rémunérations comptabilisées.
- Le montant comptabilisé dépasse l'attente. Deux explications sont possibles :
  - un risque sur la **réalité** ou la **mesure** des rémunérations : salariés fictifs, doublons, salaires versés après la fin d'un contrat ;
  - une erreur dans les **données** de l'attente, par exemple des ETP sous-estimés. L'écart équivaut à environ 3,1 ETP de salariés en parcours (67 256 / 21 816).
- Le cabinet ne peut pas conclure sans procédures complémentaires [V NEP procédures analytiques § 09-10].

**c. Procédures complémentaires (1,5 pt : 0,25 pt par procédure pertinente, dans la limite de six)**
- **Rapprochement** du compte 641 avec le journal de paie et avec les rémunérations brutes déclarées chaque mois aux organismes sociaux.
- **Rapprochement des effectifs** du tableau de bord avec les déclarations sociales et le registre des contrats et renouvellements (112), pour détecter les contrats renouvelés non reportés.
- **Rapprochement** de la liste des salariés payés avec les contrats en vigueur : salariés sans contrat, paiements après la fin du contrat, doublons, comptes bancaires communs à plusieurs salariés.
- **Sondage** sur des dossiers de salariés en parcours, orienté vers les renouvellements et les entrées récentes : contrat ou avenant signé, relevés d'heures, bulletin, virement sur un compte au nom du salarié.
- **Heures supplémentaires** : relevés signés et visés, rapprochement des plannings de la saison et des collectes du samedi. Pour la séparation des exercices, examen de la paie de janvier 2027.
- **Dette de congés payés** : obtention des compteurs de droits acquis et non pris au 31/12/2026 de chaque salarié présent, y compris les 61 salariés en parcours. Recalcul de la valorisation et des charges sociales, puis examen des congés pris en janvier et février 2027. L'argument du directeur ne tient pas : les droits acquis à la clôture sont une dette de l'exercice [V PCG art. 1214-42 ; S, application].
- **Aides au poste** : rapprochement des aides reçues avec les heures déclarées et les heures payées ; examen du versement du 22/12/2026, qui finance des postes de janvier à mars 2027 ; examen des régularisations notifiées par l'État.

**d. Refus du 12/02/2027 et moyens d'action (1,5 pt)**
- **Droits du commissaire aux comptes (0,5 pt)** :
  - il se fait communiquer **sur place** toutes les pièces qu'il estime utiles, notamment les contrats [V L. 821-60] ;
  - le **secret professionnel** ne peut lui être opposé, sauf par les auxiliaires de justice [V L. 821-61 al. 3]. L'engagement de confidentialité pris envers les salariés n'est donc pas opposable ;
  - le cabinet et ses collaborateurs sont eux-mêmes tenus au secret [V L. 821-35 al. 1] : la confidentialité des salariés reste protégée.
- **Appréciation (0,25 pt)** :
  - les déclarations sociales et les relevés bancaires sont produits à partir de la même paie : ils ne prouvent ni l'existence des contrats, ni les heures travaillées, ni la réalité de chaque salarié. Ils ne répondent pas aux risques identifiés ni à l'écart de la procédure analytique [V NEP éléments probants § 6-7] ;
  - le cabinet limite sa demande aux pièces utiles (contrats, avenants, relevés d'heures, bulletins), sans les documents d'accompagnement social, et les consulte dans les locaux de l'association [S].
- **Démarche (0,25 pt)** : le refus de communiquer les pièces utiles est un **délit d'obstacle** pour le dirigeant, puni de cinq ans d'emprisonnement et de 75 000 € d'amende [V L. 821-6 3°]. Mme HERBELOT le rappelle à la présidente et porte la difficulté devant le conseil d'administration [V L. 821-63 I ; S, application].
- **Si le refus était maintenu (0,5 pt)** : il en résulterait une **limitation** de l'étendue des travaux [V NEP rapport § 11, 14].
  - Les rémunérations des salariés en parcours (1 134 432 € attendus) dépassent largement le seuil de signification. Elles commandent les charges sociales, la dette de congés payés et les aides au poste, qui dépendent des heures rémunérées.
  - Les incidences ne seraient pas clairement circonscrites : **impossibilité de certifier**.
  - Une réserve pour limitation ne conviendrait que si le cabinet pouvait circonscrire les montants non vérifiés.

**Réponses tolérées**
- En b, un calcul en salaires annuels globaux exact à l'euro près, ou une conclusion qui attribue d'emblée l'écart à l'une des deux explications si l'autre est envisagée en c.
- En d, une réserve pour limitation, si le candidat la justifie par une circonscription des incidences aux seules rémunérations des salariés en parcours : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Réciter l'extrait de norme sans l'appliquer, ou conclure qu'un écart supérieur à l'écart acceptable est une anomalie (`JUR-G09`, `JUR-A06`).
- Oublier la revalorisation au 1er mai, ou l'appliquer à l'année entière (`JUR-F06`).
- Accepter le refus au nom de la confidentialité (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP procédures analytiques § 01-10 ; NEP éléments probants § 6-7 | Définition ; recours ; écarts ; fiabilité des données | [V] ; application : [S] | F11 § 6.1, § 18 |
| PCG art. 1214-42 (p. 167) | Dette provisionnée pour congés à payer | [V] | F11 § 18 |
| C. com. L. 821-35, L. 821-60, L. 821-61, L. 821-6 3°, L. 821-63 I ; NEP rapport § 11, 14 | Moyens d'action ; secret non opposable ; délit d'obstacle ; limitation | [V] ; application : [S] | F11 § 2, 8 ; F09 § 5 |

### 3.6 Anomalies, écritures et opinion (2,5 pts)

**Récapitulation et caractère significatif (0,75 pt)** [V NEP anomalies § 8, 11-14 ; NEP caractère significatif § 9]
- **Écart de la procédure analytique** : expliqué par l'effectif réel de 55 ETP. Les 3 ETP non reportés au tableau de bord représentent 65 448 € (3 × 21 816) ; l'écart résiduel est de 1 808 €, inférieur à l'écart acceptable. Les rémunérations concordent avec les déclarations sociales : **aucune anomalie**.

| Anomalie | Effet sur l'excédent | En % du seuil (45 000) |
|---|---:|---:|
| A1 Dette de congés payés des salariés en parcours non comptabilisée : 26 400 + 26 400 × 15 % = 26 400 + 3 960 | − 30 360 | 67,5 % |
| A2 Aide au poste de janvier à mars 2027 comptabilisée en produit de 2026 | − 24 600 | 54,7 % |
| Anomalies non corrigées des autres cycles | − 8 400 | 18,7 % |
| **Total** | **− 63 360** | **140,8 %** |

- Aucune anomalie n'est significative à elle seule, mais leur **cumul** dépasse le seuil.
- Leur **nature** compte aussi. L'excédent présenté (36 000 €) deviendrait, après correction, un **déficit de 27 360 €** : les anomalies changent le signe du résultat, à l'approche du vote des subventions.

**Écritures de correction au 31/12/2026 (0,5 pt)**

X1 – Dette de congés payés des salariés en parcours au 31/12/2026

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 6412 | Congés payés | 26 400 | |
| 645 | Cotisations de sécurité sociale et de prévoyance | 3 960 | |
| 4282 | Dettes provisionnées pour congés à payer | | 26 400 |
| 4382 | Charges sociales sur congés à payer | | 3 960 |

X2 – Aide au poste du chantier d'hiver (janvier à mars 2027), produit constaté d'avance

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 741 | Subventions d'exploitation | 24 600 | |
| 487 | Produits constatés d'avance | | 24 600 |

Fondements : la dette de congés acquis est constatée en fin d'exercice au crédit du compte 428 par le débit du compte 6412 [V PCG art. 1214-42] ; le compte 487 enregistre les produits perçus avant que les prestations qui les justifient aient été effectuées [V PCG art. 1214-48]. Ici, les postes financés sont ceux de 2027.

**Opinion (1,25 pt)** [V NEP rapport § 06, 08-12 ; R. 821-180]

| L'association corrige | Anomalies non corrigées | Opinion |
|---|---|---|
| A1 et A2 (0,25 pt) | 8 400 €, soit 18,7 % du seuil ; déficit présenté de 18 960 € pour un déficit corrigé de 27 360 € | **Certification sans réserve** |
| A2 seulement (0,5 pt) | A1 et autres cycles : 38 760 €, soit 86,1 % du seuil. Mais l'excédent présenté de 11 400 € masquerait un déficit de 27 360 € | **Certification avec réserve pour désaccord**. L'anomalie, inférieure au seuil, est significative par sa **nature** : elle inverse le résultat, que la présidente veut précisément éviter de présenter. Elle reste circonscrite à la dette de congés payés, chiffrée : une réserve suffit |
| Aucune (0,25 pt) | 63 360 €, soit 140,8 % du seuil | **Certification avec réserve pour désaccord** : les incidences sont chiffrées et circonscrites (dettes sociales, produits constatés d'avance). Le refus de certifier n'est pas justifié |

- **Forme (0,25 pt)** : la réserve est motivée dans la partie « Fondement de l'opinion », avec les incidences chiffrées. Exemple pour l'absence de toute correction : excédent surévalué de 63 360 €, dettes sociales sous-évaluées de 30 360 €, produits constatés d'avance omis pour 24 600 €. Les motifs sont communiqués au préalable au conseil d'administration [V NEP rapport § 06 ; L. 821-63 I]. Le cabinet obtient une **déclaration écrite** de la présidente, avec l'état des anomalies non corrigées [V NEP anomalies § 17 ; NEP déclarations écrites § 6-7].
- La limitation née du refus d'accès a été levée le 02/03/2027 : elle n'a pas d'incidence sur l'opinion.

**Réponses tolérées**
- Dans la deuxième situation, une certification sans réserve justifiée par la seule comparaison au seuil : 0,25 pt sur 0,5 si le candidat mentionne la déclaration écrite et l'état des anomalies non corrigées.
- Les écritures X1 en deux écritures distinctes (rémunérations et charges sociales).

**Erreurs fréquentes**
- Conclure sans apprécier le cumul et la nature des anomalies (`JUR-A02`, `JUR-A06`).
- Traiter l'écart de la procédure analytique comme une anomalie à corriger (`JUR-A01`).
- Écritures sans intitulés ni libellés, ou déséquilibrées (`JUR-F03`, `JUR-F04`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP anomalies § 8, 11-14, 17 ; NEP caractère significatif § 9 | Récapitulation, cumul, nature, déclaration écrite | [V] | F11 § 4.2, 14.1 |
| NEP rapport § 06, 08-12 ; C. com. R. 821-180, L. 821-63 I | Opinions ; désaccord ; communication | [V] | F11 § 8 |
| PCG art. 1214-42, 1214-48 ; liste des comptes du PCG 2026 : 6412, 645, 4282, 4382, 741, 487 | Écritures | [V] | F11 § 18 |

---

### Partie B – Durabilité (12 points)

### 3.7 GRI, ISSB, ESRS : objet et interopérabilité (2 pts)

**Objet de chaque référentiel (1 pt)**
- **GRI** : normes universelles, sectorielles et thématiques, centrées sur les **impacts** de l'organisation sur l'économie, l'environnement et les personnes, pour l'ensemble des parties prenantes [S, F12 § 1] (0,25 pt).
- **ISSB** : conseil de normalisation de la Fondation IFRS, qui publie IFRS S1 (exigences générales) et IFRS S2 (climat). Approche **financière**, destinée aux investisseurs : risques et opportunités qui peuvent affecter les flux de trésorerie, l'accès au financement ou le coût du capital [S, F12 § 1] (0,25 pt).
- **ESRS** : préparées par l'EFRAG et adoptées par la Commission, elles reposent sur la **double matérialité**, d'impact et financière [V règl. 2026/1563 consid. 3 ; ESRS 1 (2026) § 35-36] (0,25 pt).
- **Application à VERTELIS Insertion (0,25 pt)** : l'association n'a pas d'investisseurs. Ses utilisateurs sont ses financeurs, ses partenaires et ses salariés, et ses principaux enjeux sont des impacts : insertion, santé et sécurité, réemploi. Les normes de l'ISSB laisseraient de côté l'essentiel de son utilité sociale. Les normes de la GRI couvrent les impacts, mais pas les effets financiers, comme la dépendance aux financements publics.

**Interopérabilité (0,75 pt)**
- **ESRS et GRI** : déclaration commune de l'EFRAG et de la GRI, fin août et début septembre 2023. Les définitions et les indicateurs d'impact sont alignés ou étroitement alignés ; une entité qui publie selon les ESRS est considérée comme publiant « en référence » aux normes de la GRI [S ; date et contenu : V page EFRAG, F12 § 1].
- Les ESRS permettent en outre d'ajouter des informations issues de la GRI, clairement identifiées et signalées comme ne résultant pas de l'évaluation de la matérialité [V ESRS 1 (2026) § 107, 109].
- **ESRS et ISSB** : guide d'interopérabilité de mai 2024. La matérialité financière des ESRS est alignée sur celle d'IFRS S1 [S, F12 § 1]. Les ESRS révisées visent, dans toute la mesure du possible, l'interopérabilité avec les normes mondiales [V règl. 2026/1563 consid. 2].

**Conclusion (0,25 pt)** : les ESRS couvrent les deux angles. Les financeurs qui connaissent la GRI y retrouveront les informations d'impact qu'ils attendent, et l'association ne publie que sur ses thèmes matériels : l'argument du « travail inutile » ne tient pas. Le choix du conseil d'administration est donc cohérent.

**Réponses tolérées**
- La mention de la norme volontaire pour les PME (VSME), élaborée par l'EFRAG, comme autre option possible, si le candidat explique que le conseil d'administration a retenu les ESRS.
- La mention de la TCFD, intégrée aux normes de l'ISSB.

**Erreurs fréquentes**
- Présenter les trois référentiels comme concurrents et incompatibles, ou attribuer la double matérialité à la GRI ou à l'ISSB (`JUR-A01`).
- Développer le champ d'application de la réglementation européenne, exclu de la question (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règl. délégué 2026/1563 consid. 2-3 ; ESRS 1 (2026) § 35-36, 107, 109 | EFRAG ; double matérialité ; interopérabilité ; informations d'autres référentiels | [V] | F12 § 1, 6.2 |
| GRI, ISSB, déclaration EFRAG-GRI, guide d'interopérabilité ISSB-EFRAG | Objet et interopérabilité | [S] ; date de la déclaration EFRAG-GRI : [V] | F12 § 1 |

### 3.8 Parties prenantes affectées, dialogue et horizons de temps (4 pts)

**Parties prenantes affectées et utilisateurs (0,75 pt)**
- Les **parties prenantes affectées** sont les individus ou les groupes dont les intérêts sont ou pourraient être affectés par les activités de l'entreprise et ses relations d'affaires. Le dialogue avec elles est une **contribution essentielle** à l'évaluation de la matérialité d'impact [V ESRS 1 (2026) § 42].
  - Elles relèvent généralement du personnel, des communautés affectées et des consommateurs ou utilisateurs finaux.
  - Une attention particulière est due aux personnes en situation vulnérable [V ESRS 1 (2026) AR 23].
  - Chez VERTELIS Insertion : salariés en parcours, encadrants et permanents, riverains de la ressourcerie, clients de la boutique et des paniers.
- Les **utilisateurs** sont les destinataires des informations : investisseurs et prêteurs, comme la banque, et autres utilisateurs, comme les financeurs publics et la fondation [V ESRS 1 (2026) § 4].
- Un même groupe peut relever des deux catégories (les salariés). Mais consulter les utilisateurs ne remplace pas le dialogue avec les personnes affectées [V ESRS 1 (2026) § 42, AR 24].

**Dialogue avec les parties prenantes affectées (1,5 pt)**
- Le questionnaire (14 réponses) n'a été adressé qu'à des **utilisateurs** : État, département, communes, fondation, banque. Il éclaire leurs attentes et la matérialité financière, mais ne fait pas entendre les personnes affectées.
- **Salariés en parcours**, principale population affectée et vulnérable :
  - quatre entretiens pour 74 salariés, soit 5,4 % ;
  - entretiens conduits par leurs **propres encadrants**, ce qui ne garantit pas une expression libre, par exemple sur la sécurité ou la charge de travail.
- **Riverains et clients** : non consultés, alors que le registre contient six courriers de riverains et qu'une pétition de 38 signatures a été adressée à la mairie.
  - Le thème des nuisances est écarté au motif d'« aucune remontée dans le questionnaire ». Ce questionnaire n'a pas été adressé aux riverains, et la conclusion contredit les données de l'association.
  - Le report de leur consultation « lorsque le questionnaire aura été adapté » laisse le processus inachevé.
- **Méthode de notation** : la gravité (ampleur, étendue, caractère irrémédiable) et la probabilité sont les critères des ESRS pour les impacts négatifs potentiels [V ESRS 1 (2026) § 40]. Les ESRS les adaptent toutefois aux autres impacts : un impact négatif réel s'apprécie par sa seule gravité ; un impact positif s'apprécie par son ampleur et son étendue, et aussi par sa probabilité s'il est potentiel ; pour un impact négatif potentiel sur les droits de l'homme, la gravité l'emporte sur la probabilité [V § 40-41]. La note unique du projet ne fait pas ces distinctions, et les neuf accidents du travail avec arrêt de 2026 sont des impacts négatifs réels, alors que le projet ne les qualifie que de potentiels [S].

**Horizons de temps (1 pt)**
- Les ESRS retiennent trois horizons à compter de la fin de la période : **court terme** (l'exercice), **moyen terme** (jusqu'à cinq ans), **long terme** (au-delà) [V ESRS 1 (2026) § 79].
- L'entreprise ne peut retenir d'autres définitions du moyen ou du long terme que si ces horizons donnent des informations non pertinentes [V § 81]. Ce n'est pas le cas ici, et un horizon d'un an supprime purement et simplement le moyen et le long terme.
- Le **retour durable à l'emploi** est un impact de l'accompagnement de l'association qui se manifeste **après la sortie**, à moyen et long terme. Les données disponibles (19 sorties vers l'emploi ou une formation qualifiante sur 41, sans aucun suivi après la sortie) montrent un enjeu que l'association doit évaluer sur ces horizons, au lieu de l'écarter. Le juger non matériel parce que les salariés ont quitté l'association confond l'horizon de l'impact avec la durée du contrat.
- Les effets durables de la santé et de la sécurité au travail sont également écartés.

**Les deux faiblesses et ce que l'association doit faire (0,75 pt)**
1. **Dialogue insuffisant avec les parties prenantes affectées** : conduire des entretiens avec un échantillon représentatif de salariés en parcours, par une personne indépendante de leur hiérarchie, avec la confidentialité nécessaire ; consulter les riverains et les clients ; exploiter le registre des réclamations ; réexaminer le thème des nuisances.
2. **Horizon limité à un an** : retenir les trois horizons des ESRS et réévaluer la matérialité du retour durable à l'emploi, à partir des informations disponibles sur les sorties.

Dans les deux cas, l'association doit **décrire** le processus réellement suivi.

**Réponses tolérées**
- La critique de la note unique de gravité × probabilité, appliquée aussi aux impacts réels et positifs, valorisée dans les points du dialogue.
- La dépendance aux financements publics présentée comme une dépendance source de risque financier, si elle n'est pas traitée comme une faiblesse de l'analyse.
- Une réponse qui retient comme seconde faiblesse l'exclusion des nuisances pour les riverains, si l'horizon de temps est analysé par ailleurs : 0,5 pt sur 0,75.

**Erreurs fréquentes**
- Confondre parties prenantes affectées et utilisateurs, ou tenir les financeurs pour des parties prenantes affectées (`JUR-A01`).
- Proposer des indicateurs ou des cibles de retour à l'emploi : la conception d'indicateurs relève du pilotage, hors programme (`JUR-F01`).
- Ne pas exploiter le registre des réclamations et le bilan des sorties (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 4, 40-42, AR 23, AR 24 | Utilisateurs ; gravité et probabilité ; parties prenantes affectées ; personnes vulnérables ; dialogue | [V] ; application : [S] | F12 § 2, 6.2, 15, 18 |
| ESRS 1 (2026) § 79-82 | Horizons de temps | [V] ; application : [S] | F12 § 14 |

### 3.9 Objectifs, assurance limitée et procédures sur le processus de dialogue (4 pts)

**a. Objectifs et nature de l'assurance (1,5 pt)**
- **Nature (0,5 pt)** : VERTELIS Insertion publie volontairement. La mission est **contractuelle**, définie par la lettre de mission ; pour un commissaire aux comptes, c'est une **prestation** [V L. 821-2 IV ; R. 821-195]. Le cabinet s'inspire des lignes directrices de la H2A [S, transposition]. Les axes de la taxonomie et du balisage, propres aux entités tenues de publier, ne sont pas retenus [V LD 2026 § 2, 10 ; F13 § 2.2].
- **Objectifs et assurance limitée (0,5 pt)** : sur le processus, puis sur les informations, conclure qu'aucune erreur, omission ou incohérence d'une importance telle qu'elle remette en cause la conformité aux ESRS n'a été relevée. Les vérifications sont moindres en **nature**, en **étendue** et en **durée** que celles d'un audit des comptes, et la conclusion est de **forme négative** [V LD 2026, niveau d'assurance, § 17 ; F13 § 2.3].
- **Différence avec la certification des comptes (0,5 pt)** :
  - la certification est une **mission légale** qui donne une **assurance raisonnable** et une **opinion positive** sur les comptes [V L. 821-53 ; NEP principes § 08] ;
  - ses droits d'investigation sont légaux [V L. 821-60, L. 821-61]. Dans la mission sur la durabilité, le cabinet ne dispose que des engagements pris dans la lettre de mission [S] ;
  - le rapport sur la durabilité, adressé au conseil d'administration, est **distinct** du rapport sur les comptes.

**b. Procédures sur le processus de dialogue complété en février 2027 (2,5 pts : 0,25 pt par procédure pertinente, dans la limite de dix)** [V LD 2026 § 5-7, 12 ; S, transposition]
- Obtenir la description du processus et la liste des parties prenantes, et vérifier que les catégories de personnes affectées sont couvertes : personnel, dont les salariés en parcours ; riverains ; clients.
- **Salariés en parcours** :
  - inspecter les vingt comptes rendus d'entretien et vérifier qu'ils fondent la synthèse de la consultante ;
  - apprécier la sélection : tirage au sort parmi des **volontaires**, 20 sur 74, soit 27,0 %. Les volontaires peuvent ne pas être représentatifs ;
  - vérifier l'indépendance de la consultante envers la direction et les encadrants : contrat, absence de lien hiérarchique ;
  - s'entretenir avec elle sur sa méthode ;
  - rencontrer quelques salariés en parcours, avec leur accord.
- **Riverains** : examiner le compte rendu de la réunion publique signé par l'adjointe au maire ; vérifier que les six courriers et la pétition ont été pris en compte et que le thème des nuisances a été réévalué.
- **Clients** : examiner les 52 réponses au questionnaire de la boutique et leur dépouillement.
- **Traçabilité** : rapprocher les résultats du dialogue des notes de gravité et de probabilité, du seuil de 9 sur 16 et de la liste finale des sept thèmes matériels, en particulier le relèvement de la santé et sécurité et le nouveau thème de la charge mentale.
- **Horizons** : vérifier que les trois horizons redéfinis sont ceux des ESRS et qu'ils ont été appliqués à chaque thème, notamment au retour durable à l'emploi.
- **Cohérence** avec les données de l'audit des comptes : accidents du travail, effectifs, sorties.
- **Description du processus** : vérifier que l'état décrit exactement le processus suivi.
- **Fin de travaux** : communiquer les constats au conseil d'administration et obtenir une lettre d'affirmation.

**Réponses tolérées**
- D'autres procédures pertinentes tirées des annexes : observation d'un entretien avec l'accord du salarié, comparaison avec l'analyse de novembre 2026.

**Erreurs fréquentes**
- Qualifier la mission de certification légale, ou l'assurance de raisonnable (`JUR-A01`).
- Proposer des procédures générales sans les rattacher au processus de dialogue (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 2, 5-7, 10, 12, 17, niveau d'assurance | Axes ; démarche ; processus ; assurance limitée | [V] ; transposition à une mission contractuelle : [S] | F13 § 2, 3 |
| C. com. L. 821-2 IV, R. 821-195, L. 821-53, L. 821-60 ; NEP principes § 08 | Prestation ; lettre de mission ; certification ; droits légaux | [V] ; droits contractuels : [S] | F11 § 1, 2 ; F13 § 2.3 |

### 3.10 Conclusion sur le processus et structure (2 pts)

**Conclusion : impossibilité d'émettre un avis (1 pt)**
- Le refus empêche le cabinet de vérifier les comptes rendus des entretiens. C'est sur eux que reposent la matérialité, la gravité et le choix des informations de **quatre des sept thèmes matériels**, qui forment la plus grande partie des informations publiées.
- Aucune procédure alternative n'est possible : ni version anonymisée, ni entretien avec la consultante, ni rencontre avec des salariés. La synthèse est un document dérivé, tiré de sources inaccessibles.
- Il s'agit d'une **limitation** de l'étendue des vérifications, et non d'une erreur constatée.
- Dans cette mission contractuelle, le cabinet ne peut pas invoquer de droit légal de communication ni de délit d'obstacle, à la différence de la certification des comptes (question 3.5) [S]. La présidente manque à l'engagement de la lettre de mission, mais le cabinet ne peut pas l'y contraindre.
- Ses incidences ne peuvent pas être circonscrites : elles touchent le cœur du processus. La conclusion est une **impossibilité d'émettre un avis, motivée**, sur la conformité aux ESRS du processus [V LD 2026 § 17 ; F13 § 4.2-4.3].

**Pourquoi ni réserve ni non-conformité (0,5 pt)**
- **Réserve** (0,25 pt) : une limitation n'y conduit que si ses incidences sont clairement circonscrites et si la réserve suffit à éclairer l'utilisateur. Ce serait le cas si seul le compte rendu de la réunion avec les riverains manquait, et non quand quatre thèmes matériels sur sept sont en cause.
- **Non-conformité** (0,25 pt) : elle suppose des erreurs, omissions ou incohérences non corrigées et non circonscrites. Les faiblesses relevées en novembre ont été corrigées en février, et les autres travaux n'ont relevé aucune anomalie : le cabinet ne sait pas si le processus est conforme, il ne constate pas qu'il ne l'est pas.

**Structure de la partie du rapport consacrée au processus (0,5 pt)** [V LD 2026 § 17 et annexe 2 ; F13 § 4.1-4.2, 4.4 ; S, transposition]
- Le rapport est distinct du rapport sur les comptes. Il est adressé au conseil d'administration, comme le prévoit la lettre de mission, et comporte une partie introductive : qualité du cabinet et de la signataire, caractère contractuel de la mission, limites de l'assurance limitée.
- **Une partie par axe**. Pour le processus :
  - nature des vérifications réalisées ;
  - **conclusion** : « nous ne sommes pas en mesure de nous prononcer sur la conformité aux ESRS du processus mis en œuvre par VERTELIS Insertion pour déterminer les informations publiées », avec le **motif** : refus de communiquer les comptes rendus, même anonymisés, et de permettre la rencontre de la consultante et des salariés ; portée sur quatre thèmes matériels sur sept ;
  - **aucune observation** : les observations ne sont possibles qu'avec un avis de conformité.
- La partie consacrée aux informations publiées comporte sa propre conclusion, fondée sur ses propres vérifications.
- Les motifs sont communiqués au préalable au conseil d'administration. Le rapport est daté et signé par Mme HERBELOT.

**Réponses tolérées**
- Une conclusion assortie d'une réserve pour limitation, si le candidat soutient avec le critère de circonscription que la limitation ne porte que sur l'expression des salariés et non sur la liste des thèmes : 0,5 pt sur 1.
- L'emploi indifférent des mots « conclusion » et « avis ».

**Erreurs fréquentes**
- Retenir une non-conformité au seul motif du refus, en confondant limitation et erreur (`JUR-A02`).
- Formuler une conclusion positive, ou une conclusion unique pour toute la mission (`JUR-A01`, `JUR-A02`).
- Invoquer le délit d'obstacle dans une mission contractuelle (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 et annexe 2 | Quatre avis ; limitation ; circonscription ; formulations ; structure par axe ; observations | [V] ; transposition : [S] | F13 § 4 |
| C. com. L. 821-6 3°, L. 821-60 | Droits légaux propres à la certification des comptes | [V] ; non-application à la mission contractuelle : [S] | F11 § 2 |
