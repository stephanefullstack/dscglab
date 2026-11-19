# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 16

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 17/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex43_consolidation_anc_provisions_reglementees_vote_double_secteurs` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.7 | `exercices/ex44_tup_mali_stock_marque_vrai_mali` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.12 | `exercices/ex45_audit_capitaux_propres_scop_double_materialite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 1,5 |
| 1.2 Définition d'un passif et amortissements dérogatoires | `2.1.a` Cadre conceptuel de l'IASB | 3 |
| 1.3 a Périmètre, droits de vote double et méthodes | `2.1.c` Périmètre de consolidation | 2,5 |
| 1.3 b Conséquences de l'intégration globale de KAOLINS DU CHALARD | `2.1.d` Conséquences du référentiel et des méthodes | 1 |
| 1.4 a Calcul des amortissements dérogatoires | `2.2.b` Élimination des écritures fiscales | 2,5 |
| 1.4 b Incidences et partage | `2.2.b` Élimination des écritures fiscales | 1,5 |
| 1.4 c Écritures | `2.2.b` Élimination des écritures fiscales | 2 |
| 1.5 a Contrat de l'hôtel AUBRIANE : avancement | `2.2.c` Homogénéisation, thèmes communs | 2 |
| 1.5 b Tableau des incidences | `2.2.c` Homogénéisation, thèmes communs | 1,5 |
| 1.5 c Écritures | `2.2.c` Homogénéisation, thèmes communs | 2 |
| 1.6 a Ventes de pâtes et marges internes partagées | `2.2.f` Comptes réciproques et résultats internes | 2,5 |
| 1.6 b Avance en compte courant dépréciée | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.6 c Dividendes et soldes réciproques | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.7 a Actif net réévalué d'ARZELIÈRE et suivi des écarts | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.7 b Coût d'acquisition, écart d'acquisition, minoritaires | `2.2.g` Écarts d'évaluation et d'acquisition | 2 |
| 1.7 c Durée d'amortissement et écritures | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.8 a Partage des capitaux propres de trois filiales | `2.2.h` Partage des capitaux propres | 3 |
| 1.8 b Mise en équivalence d'ÉCRIN DES TABLES | `2.2.h` Partage des capitaux propres | 2 |
| 1.9 Phases du processus, intégration globale et mise en équivalence | `2.2.a` Processus d'élaboration d'une consolidation | 2,5 |
| 1.10 a Information sectorielle (ANC, IFRS 8) | `2.3.a` Documents de synthèse consolidés | 2,5 |
| 1.10 b Notes de l'annexe sur les méthodes | `2.3.a` Documents de synthèse consolidés | 1,5 |
| 1.10 c Minoritaires dans les états IFRS | `2.3.a` Documents de synthèse consolidés | 2 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires (réserves / résultat) ; `EA` = écart d'acquisition ; `AMO_EA` = amortissements de l'écart d'acquisition ; `DOT_EA` = ligne « dotations aux amortissements et dépréciations des écarts d'acquisition » du compte de résultat ; `TME` = titres mis en équivalence ; `QP_MEE` = ligne « résultat net lié aux entités mises en équivalence » ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.VALCHEYRE` : titres détenus par VALCHEYRE ; `RSV.KAOLINS` : réserves de KAOLINS DU CHALARD).

---

### 1.1 Obligation de consolider et référentiel (1,5 pt)

- **Principe (0,25).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. La SA VALCHEYRE contrôle exclusivement KAOLINS DU CHALARD, ARZELIÈRE et ATELIERS DU VINCOU (question 1.3 a) : l'obligation est née. La participation dans ÉCRIN DES TABLES, sous influence notable, ne la créerait pas à elle seule, mais elle entre dans le périmètre une fois l'obligation née [V ANC art. 211-1, IR1 ; F03 § 1.1].
- **Exemption de la société contrôlée (0,25).** Elle suppose que VALCHEYRE soit contrôlée par une entité qui l'inclut dans des comptes consolidés publiés [V L. 233-17, 1° ; F03 § 1.1]. Aucune entité ne contrôle VALCHEYRE : les deux branches familiales détiennent chacune 37 % directement, et le fonds (26 %) ne consolide pas. L'exemption est exclue.
- **Exemption des ensembles qui ne sont pas un grand groupe (0,5).** Un grand groupe dépasse, à la clôture, deux des trois seuils (bilan 30 M€, chiffre d'affaires net 60 M€, 250 salariés), sur deux exercices consécutifs [V L. 230-2, 3° et D. 230-2 ; F03 § 1.1]. L'ensemble dépasse les trois seuils en 2025 (104 M€, 109 M€, 610 salariés) et en 2026 (126 M€, 131 M€, 740) : l'exemption ne joue pas. Aucune filiale n'étant d'un intérêt négligeable [V L. 233-17-1], VALCHEYRE doit établir et publier des comptes consolidés de 2026.
- **Référentiel (0,5).** Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que pour les sociétés dont des titres sont admis aux négociations sur un marché réglementé à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Aucun titre de VALCHEYRE n'étant admis sur un marché, elle applique le règlement ANC n° 2020-01 ou **peut opter** pour les IFRS adoptées [V L. 233-24 ; F03 § 1.2] ; elle a retenu le règlement ANC.

**Erreurs fréquentes.** Fonder l'obligation sur la seule influence notable exercée sur ÉCRIN DES TABLES ; citer les anciens seuils (périmés) ; oublier la condition des deux exercices consécutifs (`JUR-F07`).

---

### 1.2 Définition d'un passif et amortissements dérogatoires (3 pts)

- **Définition (0,75 pt).** Selon le cadre conceptuel de 2018, un passif est une **obligation actuelle** de l'entité de **transférer une ressource économique** du fait d'**événements passés** [S ; F03 § 8]. IAS 37 le définit comme une obligation actuelle de l'entité résultant d'événements passés et dont l'extinction devrait se traduire par une sortie de ressources représentatives d'avantages économiques [V IAS 37 § 10 ; F03 § 8]. Un instrument de capitaux propres fait apparaître un intérêt résiduel dans les actifs de l'entité après déduction de tous ses passifs [V IAS 32 § 11 ; F03 § 8] ; le cadre de 2018 définit ainsi les capitaux propres [S ; F03 § 8].
- **Application aux amortissements dérogatoires (1 pt).** Le solde de 436 800 € au 31/12/2025 est la différence entre l'amortissement fiscal dégressif des broyeurs et leur amortissement linéaire (question 1.4 a). Il n'engage KAOLINS DU CHALARD envers **personne** : aucun tiers ne peut en exiger le paiement, et sa reprise ne fera sortir aucune ressource de l'entreprise. Ce n'est donc **pas un passif**. Ce n'est pas davantage une dépréciation des broyeurs : leur consommation est déjà traduite par l'amortissement linéaire sur leur durée d'utilisation. Le PCG l'admet lui-même : ces amortissements ne correspondent pas à l'objet normal d'un amortissement, sont constitués en application de textes fiscaux et sont classés parmi les **provisions réglementées**, présentées dans le total des **capitaux propres** du bilan individuel [V PCG art. 214-8, 313-1 et 821-1 ; F04 § 8]. Le « passif » dont parle le fonds est la colonne de droite du bilan, qui comprend les capitaux propres ; ce n'est pas une dette.
- **Ce que devient l'avantage fiscal (0,75 pt).** Les dotations dérogatoires ont réduit le résultat imposable des premiers exercices ; leurs reprises l'augmenteront ensuite (la reprise de 82 480 € des broyeurs en 2026 en donne l'exemple). L'avantage est donc un **décalage d'imposition** : l'impôt économisé sera payé lors des reprises. Cette obligation d'acquitter un impôt futur, née des déductions passées, **est un passif** : l'impôt différé passif, 25 % du solde, soit 109 200 € au 31/12/2025 et 103 580 € au 31/12/2026 [V ANC art. 272-8 ; F04 R1]. Le surplus, 75 %, est une part des capitaux propres : il rejoint les réserves (stock d'ouverture) et le résultat (mouvement de l'exercice), partagés entre le groupe et les minoritaires de KAOLINS DU CHALARD [V ANC art. 272-1 ; F04 R1]. Le groupe ne fait donc pas disparaître de passif : il en fait apparaître un, l'impôt différé, que les comptes individuels ne montraient pas.
- **En IFRS (0,5 pt).** Aucune norme ne connaît de provisions réglementées : une provision suppose une obligation actuelle [V IAS 37 § 14 ; F04 R1], et l'amortissement répartit le montant amortissable sur la durée d'utilité [V IAS 16 § 50 ; F04 R1]. L'élimination et l'impôt différé passif [V IAS 12 § 15 ; F04 § 1] sont identiques : la solution ne change pas.

**Réponses tolérées.** Une présentation de l'avantage fiscal comme un « crédit gratuit » de l'État, remboursé lors des reprises, est acceptée si le candidat identifie l'impôt différé passif.
**Erreurs fréquentes.** Qualifier les amortissements dérogatoires de dépréciation, ou laisser le solde entier en passif dans les comptes consolidés ; oublier l'impôt différé (`JUR-G06`).

---

### 1.3 Périmètre et méthodes (3,5 pts)

#### a. Tableau et justification (2,5 pts)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % d'intérêt des minoritaires |
|---|---|---|---|---|---|
| SA VALCHEYRE | — | Société consolidante | — | 100 % | — |
| KAOLINS DU CHALARD | 180 000 / 300 000 = **60 %** | Exclusif | Intégration globale | **45 %** | **55 %** |
| ARZELIÈRE | 80 % | Exclusif | Intégration globale | 80 % | 20 % |
| ATELIERS DU VINCOU | 100 % | Exclusif | Intégration globale | 100 % | 0 % |
| ÉCRIN DES TABLES | 30 % | Influence notable | Mise en équivalence | 30 % | — |

(Quatre lignes : 0,25 chacune, soit 1 pt.) Le contrôle exclusif conduit à l'intégration globale, l'influence notable à la mise en équivalence [V ANC art. 221-1, p. 18 ; F03 § 3].

- **Droits de vote de KAOLINS DU CHALARD (1 pt).** Pour calculer la fraction des droits de vote détenus, il est tenu compte des **actions à droit de vote double** [V ANC art. 211-7, p. 14 ; F03 § 2]. Les 90 000 actions de VALCHEYRE, inscrites au nominatif depuis 2012, portent chacune deux voix depuis 2014 : 180 000 voix sur 300 000, soit **60 %**, alors que VALCHEYRE ne détient que 45 % du capital. La détention de la majorité des droits de vote donne le contrôle exclusif [V art. 211-3, p. 12-13 ; F03 § 2] ; aucun pacte ne le remet en cause, et VALCHEYRE a fait élire cinq des sept administrateurs depuis 2014. Le **pourcentage d'intérêt**, lui, se calcule sur le **capital** : 45 %, soit 55 % pour les minoritaires [S, méthode du corrigé du sujet zéro ; F03 § 4.1] ; c'est ce pourcentage qui partage le résultat et les dividendes.
- **ÉCRIN DES TABLES (0,5 pt).** 30 % des droits de vote : l'influence notable est présumée à partir de 20 % [V art. 211-5, p. 13 ; F03 § 2] ; elle est confirmée par deux sièges sur six au comité stratégique et par l'importance des achats au groupe. Les fondatrices détiennent la majorité : il n'y a pas de contrôle.

**Erreurs fréquentes.** Retenir 45 % comme pourcentage de contrôle et conclure à une influence notable (ou invoquer la présomption de l'art. 211-3 au-delà de 40 %, inutile ici) ; à l'inverse, retenir 60 % comme pourcentage d'intérêt (`JUR-G04`).

#### b. Conséquences de l'intégration globale de KAOLINS DU CHALARD (1 pt)

L'intégration globale reprend **100 %** des actifs, des dettes, des produits et des charges de KAOLINS DU CHALARD, après élimination des opérations internes [V ANC art. 221-2, p. 18-19 ; F03 § 3] : ses équipements, ses stocks et ses dettes figurent en totalité au bilan consolidé, et son chiffre d'affaires réalisé hors du groupe (18 200 000 €, question 1.10 a) en totalité au compte de résultat consolidé (0,5). Le groupe n'a pourtant droit qu'à **45 %** de son résultat et de ses capitaux propres : la part des 55 % d'actionnaires de la région apparaît dans les intérêts minoritaires, au passif et sur la ligne « intérêts minoritaires » du compte de résultat (0,5). Le lecteur doit donc rapprocher le chiffre d'affaires et l'endettement consolidés, qui traduisent l'activité contrôlée, du résultat part du groupe, qui traduit les droits des actionnaires de VALCHEYRE.

---

### 1.4 Amortissements dérogatoires de KAOLINS DU CHALARD (6 pts)

#### a. Calcul (2,5 pts)

**Broyeurs à boulets** (2 560 000 €, 01/04/2024, 5 ans ; 9 mois en 2024)

| Exercice | Amortissement linéaire (comptes individuels) | Amortissement fiscal dégressif (35 %) | Dérogatoires de l'exercice |
|---|---:|---:|---:|
| 2024 | 2 560 000 / 5 × 9/12 = 384 000 | 2 560 000 × 35 % × 9/12 = 672 000 | + 288 000 |
| 2025 | 512 000 | (2 560 000 – 672 000) × 35 % = 660 800 | + 148 800 |
| **Cumul au 31/12/2025** | 896 000 | 1 332 800 | **436 800** |
| 2026 | 512 000 | (1 888 000 – 660 800) × 35 % = 429 520 | **– 82 480** (reprise) |
| **Cumul au 31/12/2026** | 1 408 000 | 1 762 320 | **354 320** |

(Annuités : 1 pt ; stock d'ouverture et reprise : 0,75.) En 2026, l'annuité dégressive (429 520 €) est inférieure à l'annuité linéaire comptable : l'écart se résorbe et le dérogatoire est **repris**. Le passage au linéaire fiscal ne joue pas encore (1 227 200 / 3,25 = 377 600 € < 429 520 €), comme l'indique l'énoncé.

**Filtres-presses** (1 280 000 €, 01/04/2026, 4 ans) (0,5) : linéaire 1 280 000 / 4 × 9/12 = 240 000 € ; dégressif 1 280 000 × 31,25 % × 9/12 = 300 000 € ; **dotation de 60 000 €**, stock d'ouverture nul.

**Total (0,25)** : stock au 31/12/2025, **436 800 €** (le montant cité par le fonds) ; mouvement de 2026, – 82 480 + 60 000 = **– 22 480 €** (reprise nette) ; stock au 31/12/2026, **414 320 €**.

#### b. Justification, incidences et partage (1,5 pt)

**Justification (0,5).** Dans les comptes consolidés, l'incidence des écritures passées pour la seule application des législations fiscales est éliminée, notamment les amortissements dérogatoires [V ANC art. 272-1, p. 53 ; F04 R1]. Le groupe garde l'amortissement linéaire sur la durée d'utilisation. La valeur nette consolidée des équipements dépasse alors leur valeur nette fiscale du montant du dérogatoire : différence temporaire imposable, **impôt différé passif** de 25 % [V art. 272-8, p. 57 ; F04 R1].

**Tableau des incidences (0,5)**

| | Ouverture (réserves) | 2026 (résultat) | Clôture |
|---|---:|---:|---:|
| Élimination des dérogatoires (avant impôt) | + 436 800 | – 22 480 | 414 320 |
| Impôt différé passif (25 %) | – 109 200 | + 5 620 (produit) | **103 580** |
| **Net** | **+ 327 600** | **– 16 860** | 310 740 |

L'élimination **diminue** le résultat consolidé de 2026 : elle annule une reprise nette, qui avait augmenté le résultat individuel.

**Partage (0,5).** Le retraitement modifie les capitaux propres de KAOLINS DU CHALARD, qui sont partagés entre ses actionnaires selon les pourcentages d'intérêt [V ANC art. 221-2 ; F05 § 3] :

| | Groupe (45 %) | Minoritaires (55 %) |
|---|---:|---:|
| Réserves (+ 327 600) | + 147 420 | + 180 180 |
| Résultat (– 16 860) | – 7 587 | – 9 273 |

#### c. Écritures au 31/12/2026 (2 pts)

**C1 (bilan, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 145 Amortissements dérogatoires (354 320 + 60 000) | 414 320 | |
| RST.KAOLINS Résultat KAOLINS DU CHALARD (22 480 × 75 %) | 16 860 | |
| RSV.KAOLINS Réserves KAOLINS DU CHALARD (436 800 × 75 %) | | 327 600 |
| IDP Impôt différé passif (414 320 × 25 %) | | 103 580 |
| *Élimination des amortissements dérogatoires* | **431 180** | **431 180** |

**C1R (compte de résultat, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 78725 Reprises sur amortissements dérogatoires (broyeurs) | 82 480 | |
| 68725 Dotations aux amortissements dérogatoires (filtres-presses) | | 60 000 |
| CH_ID Produit d'impôt différé (22 480 × 25 %) | | 5 620 |
| RES_CR Résultat | | 16 860 |
| *Annulation de la dotation et de la reprise de 2026* | **82 480** | **82 480** |

Le partage entre le groupe et les minoritaires se fait dans l'écriture C13 (question 1.8 a).

**Réponses tolérées.** Une écriture par équipement ; la présentation des seuls soldes nets au compte de résultat (débit 78725 de 22 480 €) si le candidat le justifie.
**Erreurs fréquentes.** Imputer tout le stock en résultat ; traiter la reprise des broyeurs comme une dotation ; partager à 60 / 40 (pourcentage de contrôle) au lieu de 45 / 55 (`JUR-G04`, `JUR-F04`, `JUR-F05`).

---

### 1.5 Contrat de l'hôtel AUBRIANE (5,5 pts)

#### a. Justification et calcul (2 pts)

**Justification (0,5).** Le PCG admet la méthode à l'achèvement et la méthode à l'avancement [V PCG art. 622-2, p. 63 ; F04 R9] ; le manuel retient l'avancement, et les comptes de la filiale sont retraités pour appliquer les méthodes du groupe [V ANC art. 271-5, p. 52 ; F04 § 1]. Le résultat à terminaison pouvant être estimé de façon fiable, le résultat comptabilisé est le résultat à terminaison multiplié par le pourcentage d'avancement [V PCG art. 622-3 ; F04 R9] ; le contrat étant bénéficiaire, aucune perte à terminaison n'est à provisionner [V art. 622-6].

**Calcul (1,5)**

| | 31/12/2025 | 31/12/2026 |
|---|---:|---:|
| Pourcentage d'avancement (coûts engagés / coût total prévisionnel) | 720 000 / 2 880 000 = **25 %** | 2 250 000 / 3 000 000 = **75 %** |
| Chiffre d'affaires cumulé (3 600 000 × %) | **900 000** | **2 700 000** |
| Résultat à terminaison (3 600 000 – coût total prévisionnel) | 720 000 | 600 000 |
| Résultat cumulé (résultat à terminaison × %) | **180 000** | **450 000** |
| Chiffre d'affaires de l'exercice | 900 000 | 2 700 000 – 900 000 = **1 800 000** |
| Résultat de l'exercice | 180 000 | 450 000 – 180 000 = **270 000** |

(2025 : 0,75 ; 2026 : 0,75.) La révision du coût prévisionnel s'applique à la clôture de 2026 sans corriger 2025 : le résultat de 2026 est le cumul à cette date moins le résultat déjà constaté.

#### b. Tableau des incidences (1,5 pt)

Dans les comptes individuels, aucun résultat n'est constaté avant l'achèvement : l'écart avec l'avancement est égal au résultat cumulé à l'avancement. Le résultat fiscal suivant l'achèvement, l'écart donne un **impôt différé passif** [V ANC art. 272-8, p. 57 ; F04 R9].

| | Ouverture (réserves) | 2026 (résultat) | Clôture |
|---|---:|---:|---:|
| Écart avant impôt | + 180 000 | + 270 000 | 450 000 |
| Impôt différé passif (25 %) | – 45 000 | – 67 500 | **112 500** |
| **Net** | **+ 135 000** | **+ 202 500** | 337 500 |

(Lignes : 0,5 chacune.) Au bilan, les travaux en cours (2 250 000 €) sont annulés ; le chiffre d'affaires cumulé (2 700 000 €) est couvert par les acomptes facturés (2 520 000 €) et par une facture à établir de 180 000 €. Au compte de résultat de 2026, le chiffre d'affaires de 1 800 000 € remplace la variation des en-cours de 1 530 000 € (coûts de 2026 : 2 250 000 – 720 000).

#### c. Écritures au 31/12/2026 (2 pts)

**C2 (bilan, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4191 Clients – Avances et acomptes reçus sur commandes | 2 520 000 | |
| 4181 Clients – Factures à établir (2 700 000 – 2 520 000) | 180 000 | |
| 335 Travaux en cours | | 2 250 000 |
| RSV.VINCOU Réserves ATELIERS DU VINCOU (180 000 × 75 %) | | 135 000 |
| RST.VINCOU Résultat ATELIERS DU VINCOU (270 000 × 75 %) | | 202 500 |
| IDP Impôt différé passif (450 000 × 25 %) | | 112 500 |
| *Contrat de l'hôtel AUBRIANE à l'avancement* | **2 700 000** | **2 700 000** |

**C2R (compte de résultat, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 71335 Variation des en-cours – travaux en cours (2 250 000 – 720 000) | 1 530 000 | |
| CH_ID Charge d'impôt différé (270 000 × 25 %) | 67 500 | |
| RES_CR Résultat | 202 500 | |
| 701 Ventes de produits finis (2 700 000 – 900 000) | | 1 800 000 |
| *Chiffre d'affaires à l'avancement de 2026* | **1 800 000** | **1 800 000** |

**Réponses tolérées.** Le maintien des acomptes au passif et l'inscription d'une créance de 2 700 000 € (4181) ; le compte 704 ou 706 pour le chiffre d'affaires, si l'intitulé est cohérent.
**Erreurs fréquentes.** Appliquer le pourcentage de 2026 au résultat à terminaison de 2025 ; porter tout l'écart en résultat de 2026 ; oublier l'impôt différé (`JUR-G06`, `JUR-F05`).

---

### 1.6 Opérations internes (5 pts)

#### a. Ventes de pâtes et marges internes (2,5 pts)

**Justification (0,5).** Les produits et charges réciproques entre sociétés intégrées globalement sont éliminés en totalité, sans incidence sur le résultat [V ANC art. 251-1, p. 45 ; F04 R14] : 12 800 000 € de ventes de KAOLINS DU CHALARD et d'achats de VALCHEYRE et d'ARZELIÈRE (C3). Les profits internes compris dans les stocks sont éliminés **à 100 %**, puis répartis entre le groupe et les minoritaires **de la société qui a réalisé le résultat**, ici le vendeur, KAOLINS DU CHALARD ; l'impôt est corrigé [V art. 251-2, p. 45 ; F04 R14]. Peu importe que le groupe ne détienne que 45 % du vendeur : l'élimination est totale, seul son partage suit le pourcentage d'intérêt.

**Stock d'ouverture d'ARZELIÈRE (0,5).** Les pâtes en stock chez ARZELIÈRE au 01/01/2026 ont été achetées en 2025, quand ARZELIÈRE n'appartenait pas au groupe : la vente était alors faite à un tiers, et ces pâtes font partie des actifs identifiables d'ARZELIÈRE, évalués à leur valeur d'entrée (égale à leur valeur comptable) au 01/01/2026 [V ANC art. 232-1 ; F05 § 1.2]. Leur marge (360 000 × 20/120 = 60 000 €) n'est **pas** une marge interne : elle n'est pas éliminée.

**Calcul (0,5).** Le taux de marge porte sur le coût de revient : marge = prix de vente × 20 / 120.

| | Calcul | Montant |
|---|---|---:|
| Marge dans le stock d'ouverture | 720 000 × 20/120 (VALCHEYRE seulement) | 120 000 |
| Marge dans le stock de clôture | (960 000 + 432 000) × 20/120 = 160 000 + 72 000 | 232 000 |
| Variation de 2026 (résultat) | 232 000 – 120 000 | 112 000 |
| Impôt différé actif à la clôture | 232 000 × 25 % | 58 000 |

**Partage (0,25).** Réserves : – 120 000 × 75 % = – 90 000 €, dont groupe – 40 500 € (45 %) et minoritaires – 49 500 € (55 %) ; résultat : – 112 000 × 75 % = – 84 000 €, dont groupe – 37 800 € et minoritaires – 46 200 €.

**Écritures (0,75)**

**C3 (compte de résultat)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 701 Ventes de produits finis (KAOLINS DU CHALARD) | 12 800 000 | |
| 601 Achats stockés – Matières premières (VALCHEYRE 9 600 000, ARZELIÈRE 3 200 000) | | 12 800 000 |
| *Élimination des ventes internes de pâtes* | **12 800 000** | **12 800 000** |

**C4 (bilan)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RSV.KAOLINS Réserves KAOLINS DU CHALARD (120 000 × 75 %) | 90 000 | |
| IDA Impôt différé actif (232 000 × 25 %) | 58 000 | |
| RST.KAOLINS Résultat KAOLINS DU CHALARD (112 000 × 75 %) | 84 000 | |
| 31 Matières premières et fournitures (marge de clôture) | | 232 000 |
| *Élimination des marges internes sur stocks* | **232 000** | **232 000** |

**C4R (compte de résultat)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6031 Variation des stocks de matières premières | 112 000 | |
| CH_ID Produit d'impôt différé (112 000 × 25 %) | | 28 000 |
| RES_CR Résultat | | 84 000 |
| *Variation de la marge interne* | **112 000** | **112 000** |

**Erreurs fréquentes.** Éliminer la marge à 45 % seulement ; la rattacher aux acheteurs (VALCHEYRE, ARZELIÈRE) ; éliminer la marge du stock d'ouverture d'ARZELIÈRE ; calculer la marge à 20 % du prix de vente (`JUR-G04`, `JUR-F07`).

#### b. Avance en compte courant et dépréciation (1,5 pt)

**Justification (0,5).** La créance de VALCHEYRE et la dette d'ATELIERS DU VINCOU sont réciproques : éliminées en totalité [V ANC art. 251-1, p. 45 ; F04 R14]. Leur dépréciation est un résultat interne : la créance n'existe pas pour le groupe, et les pertes de la filiale, intégrée à 100 %, figurent déjà dans le résultat consolidé ; la conserver les compterait deux fois. Le règlement élimine en totalité les dotations aux dépréciations des titres de participation et les dotations aux provisions constituées en raison des pertes des entités contrôlées de manière exclusive [V art. 251-2, p. 45 ; F04 R14] ; la dépréciation de l'avance, qui a la même cause et porte sur une créance éliminée, suit la même règle [application, S]. La part de 2025 (400 000 €) rétablit les réserves de VALCHEYRE, la dotation de 2026 (300 000 €) son résultat. Les dépréciations ayant été déduites fiscalement, et leur reprise étant imposable, l'élimination crée un **impôt différé passif** de 700 000 × 25 % = 175 000 € [V art. 272-8 ; F04 § 1].

**C6 (bilan, 0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 171 Dettes rattachées à des participations – groupe (ATELIERS DU VINCOU) | 1 500 000 | |
| 2671 Créances rattachées à des participations – groupe (VALCHEYRE) | | 1 500 000 |
| *Élimination de l'avance en compte courant* | **1 500 000** | **1 500 000** |

**C7 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2967 Dépréciations des créances rattachées à des participations | 700 000 | |
| RSV.VALCHEYRE Réserves VALCHEYRE (400 000 × 75 %) | | 300 000 |
| RST.VALCHEYRE Résultat VALCHEYRE (300 000 × 75 %) | | 225 000 |
| IDP Impôt différé passif (700 000 × 25 %) | | 175 000 |
| *Élimination de la dépréciation de l'avance* | **700 000** | **700 000** |

**C7R (compte de résultat, 0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RES_CR Résultat | 225 000 | |
| CH_ID Charge d'impôt différé (300 000 × 25 %) | 75 000 | |
| 68662 Dotations aux dépréciations des immobilisations financières | | 300 000 |
| *Annulation de la dotation de 2026* | **300 000** | **300 000** |

**Erreurs fréquentes.** Éliminer la créance brute et laisser la dépréciation ; porter les 700 000 € en résultat de 2026 ; oublier l'impôt différé, alors que l'énoncé tranche la fiscalité (`JUR-F07`).

#### c. Dividendes et soldes réciproques (1 pt)

- **Dividende de KAOLINS DU CHALARD (0,25 + 0,25).** Les dividendes intragroupe sont éliminés en totalité [V ANC art. 251-2 ; F04 R14]. VALCHEYRE a reçu sa part selon le **nombre de ses actions** (45 %), non selon ses droits de vote : 800 000 × 45 % = **360 000 €**. Les 440 000 € versés aux minoritaires ont quitté le groupe : ils ont déjà réduit les réserves de KAOLINS DU CHALARD et n'appellent aucune écriture.

**C8 / C8R**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.VALCHEYRE Résultat VALCHEYRE | 360 000 | |
| RSV.VALCHEYRE Réserves VALCHEYRE | | 360 000 |
| *C8 : élimination du dividende reçu de KAOLINS DU CHALARD (bilan)* | **360 000** | **360 000** |
| 7611 Revenus des titres de participation | 360 000 | |
| RES_CR Résultat | | 360 000 |
| *C8R : même élimination (compte de résultat)* | **360 000** | **360 000** |

- **Dividende d'ÉCRIN DES TABLES (0,25).** Les dividendes reçus des entités mises en équivalence sont éliminés du résultat de l'entité détentrice et portés en augmentation des réserves consolidées [V ANC art. 262-3, p. 49 ; F05 § 4] : 200 000 × 30 % = **60 000 €** (C9 : débit RST.VALCHEYRE, crédit RSV.VALCHEYRE ; C9R : débit 7611, crédit RES_CR, 60 000 € chacune).
- **Soldes réciproques (0,25).** C5 : débit 4011 VALCHEYRE 1 240 000 € et 4011 ARZELIÈRE 410 000 € ; crédit 4111 KAOLINS DU CHALARD 1 650 000 €. Les ventes de VALCHEYRE à ÉCRIN DES TABLES (1 900 000 €) et la créance de 210 000 € sur celle-ci ne sont **pas** éliminées : ÉCRIN DES TABLES n'est pas intégrée (question 1.9).

---

### 1.7 Acquisition d'ARZELIÈRE (7 pts)

#### a. Actif net réévalué et suivi des écarts (2,5 pts)

**Principe.** L'écart d'évaluation est la différence entre la valeur d'entrée d'un élément identifiable et sa valeur comptable [V ANC art. 231-9, p. 22] ; les impôts différés sur ces écarts sont comptabilisés [V art. 232-1, p. 24], en contrepartie de l'écart d'acquisition [V art. 272-13 ; F05 § 1.2] ; selon l'énoncé, celui du terrain y donne lieu aussi.

**Actif net réévalué au 01/01/2026 (1,5)**

| Élément | Calcul | Montant |
|---|---|---:|
| Capitaux propres individuels | 2 000 000 + 4 400 000 + 600 000 | 7 000 000 |
| Écart d'évaluation du terrain | 500 000 – 300 000 | + 200 000 |
| Écart d'évaluation du bâtiment | 2 400 000 – 1 400 000 | + 1 000 000 |
| Écart d'évaluation du stock de produits finis | 1 040 000 – 800 000 | + 240 000 |
| Impôt différé passif sur les écarts | 1 440 000 × 25 % | – 360 000 |
| **Actif net réévalué** | | **8 080 000** |

**Suivi en 2026 (1)**
- **Terrain** : non amortissable ; l'écart (200 000 €) et son impôt différé (50 000 €) restent inchangés tant que le terrain est détenu.
- **Bâtiment** : amortissement complémentaire de 1 000 000 / 20 = **50 000 €** par an ; l'impôt différé passif diminue de 12 500 € (produit d'impôt différé) ; il vaut 237 500 € au 31/12/2026.
- **Stock** : vendu au premier semestre 2026, il sort au compte de résultat pour sa valeur d'entrée : le coût des ventes consolidé augmente de **240 000 €**, et l'impôt différé de 60 000 € est repris en produit.
- Effet net sur le résultat d'ARZELIÈRE : – (50 000 + 240 000) × 75 % = **– 217 500 €**, partagé 80 / 20.

#### b. Coût d'acquisition, écart d'acquisition et minoritaires (2 pts)

- **Coût d'acquisition (0,75)** : en ANC, les coûts directement imputables à l'acquisition sont inclus dans le coût, nets de l'économie d'impôt [V ANC art. 231-2, p. 20 ; F05 § 1.1] : 7 600 000 + 240 000 × 75 % = **7 780 000 €**. VALCHEYRE les a passés en charges : le retraitement C11 les incorpore au coût des titres.
- **Écart d'acquisition (0,75)** : 7 780 000 – 80 % × 8 080 000 = 7 780 000 – 6 464 000 = **1 316 000 €**, positif, inscrit à l'actif immobilisé, en immobilisations incorporelles [V art. 231-9 et 231-11 ; F05 § 1.3]. Il ne donne lieu à aucun impôt différé [V art. 272-10 ; F05 § 1.2].
- **Minoritaires (0,5)** : les droits des minoritaires sont calculés sur l'actif net réévalué [V art. 232-1, p. 24 ; F05 § 1.2] : 20 % × 8 080 000 = **1 616 000 €** ; l'écart d'acquisition ne porte que sur la part de l'acquéreur.

**Erreurs fréquentes.** Coût limité au prix (écart de 1 136 000 €) ou frais retenus bruts (1 376 000 €) (`JUR-G02`) ; écarts d'évaluation sans impôt différé ; minoritaires calculés sur les capitaux propres comptables.

#### c. Durée d'amortissement et écritures (2,5 pts)

**Durée (1 pt).** L'écart d'acquisition dont la durée d'utilisation est limitée est amorti linéairement sur cette durée ou, si elle ne peut être déterminée de manière fiable, **sur dix ans** ; la durée résulte d'une analyse documentée des caractéristiques de l'opération, ce n'est pas une option [V ANC art. 231-11 et IR3, p. 23 ; F05 § 1.3 et § 9]. L'analyse de la direction établit que les avantages rémunérés (relations avec les chaînes hôtelières, savoir-faire, synergies) s'éteindront, puisque les gammes d'ARZELIÈRE passeront sous la marque VALCHEYRE : la durée est **limitée**. Mais le rythme de renouvellement des hôtels ne peut pas être prévu : la durée ne peut pas être déterminée de manière fiable. L'écart est donc amorti sur **10 ans** à compter du 01/01/2026 : 1 316 000 / 10 = **131 600 €** en 2026, valeur nette de 1 184 400 € au 31/12/2026. Si la durée n'était pas limitée, l'écart ne serait pas amorti, et sa valeur actuelle serait comparée chaque année à sa valeur nette comptable [V art. 231-11 ; F05 § 9].

**Écritures (1,5 pt)**

**C10 (bilan, 0,5)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2115 Terrains bâtis (500 000 – 300 000) | 200 000 | |
| 2131 Bâtiments (2 400 000 – 1 400 000) | 1 000 000 | |
| RST.ARZELIERE Résultat ARZELIÈRE ((50 000 + 240 000) × 75 %) | 217 500 | |
| 2813 Amortissements des constructions (1 000 000 / 20) | | 50 000 |
| IDP Impôt différé passif ((200 000 + 950 000) × 25 %) | | 287 500 |
| RSV.ARZELIERE Réserves ARZELIÈRE (1 440 000 × 75 %) | | 1 080 000 |
| *Écarts d'évaluation d'ARZELIÈRE et suivi de 2026* | **1 417 500** | **1 417 500** |

Le stock réévalué ayant été vendu, aucun écart ne subsiste sur le compte 355 à la clôture ; son écart d'évaluation net (180 000 €) est inscrit en réserves à l'acquisition et sort en résultat de 2026.

**C10R (compte de résultat, 0,25)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 68112 Dotations aux amortissements des immobilisations corporelles | 50 000 | |
| 71355 Variation des stocks de produits finis (écart d'évaluation du stock vendu) | 240 000 | |
| CH_ID Produit d'impôt différé ((50 000 + 240 000) × 25 %) | | 72 500 |
| RES_CR Résultat | | 217 500 |
| *Amortissement complémentaire et sortie du stock réévalué* | **290 000** | **290 000** |

**C11 / C11R (frais d'acquisition, 0,5)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation ARZELIÈRE (240 000 × 75 %) | 180 000 | |
| RST.VALCHEYRE Résultat VALCHEYRE | | 180 000 |
| *C11 : incorporation des frais nets d'impôt au coût des titres (bilan)* | **180 000** | **180 000** |
| 695 Impôts sur les bénéfices (économie d'impôt incorporée au coût) | 60 000 | |
| RES_CR Résultat | 180 000 | |
| 6226 Honoraires | | 240 000 |
| *C11R : annulation des frais et de l'économie d'impôt (compte de résultat)* | **240 000** | **240 000** |

**C12 / C12R (amortissement de l'écart, 0,25)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST_G Résultat consolidé – part du groupe | 131 600 | |
| AMO_EA Amortissements de l'écart d'acquisition ARZELIÈRE | | 131 600 |
| *C12 : amortissement de 2026 (bilan)* | **131 600** | **131 600** |
| DOT_EA Dotations aux amortissements et dépréciations des écarts d'acquisition | 131 600 | |
| RES_CR Résultat | | 131 600 |
| *C12R : même dotation (compte de résultat)* | **131 600** | **131 600** |

La dotation figure sur la ligne dédiée du compte de résultat consolidé, après le résultat d'exploitation avant dotations des écarts d'acquisition [V IR3 sous art. 231-12 ; art. 281-2 ; F05 § 1.3]. L'écart d'acquisition étant celui du groupe, son amortissement est entièrement à la charge du groupe.

**Erreurs fréquentes.** Ne pas amortir l'écart en invoquant une option ; retenir une durée sans justification ; amortir l'écart en partie sur les minoritaires (`JUR-F02`, `JUR-F06`).

---

### 1.8 Partage des capitaux propres et mise en équivalence (5 pts)

#### a. Partage des capitaux propres de trois filiales (3 pts)

**KAOLINS DU CHALARD (45 % / 55 %) (0,5)**

| | Total retraité | Groupe (45 %) | Minoritaires (55 %) |
|---|---:|---:|---:|
| Capital | 3 000 000 | | |
| Réserves : 9 400 000 + 327 600 (dérogatoires) – 90 000 (marge) | 9 637 600 | | |
| Capitaux propres hors résultat | 12 637 600 | 5 686 920 | 6 950 680 |
| Élimination des titres | | – 2 340 000 | |
| **Réserves consolidées / intérêts minoritaires** | | **3 346 920** | **6 950 680** |
| Résultat : 2 100 000 – 16 860 – 84 000 | 1 999 140 | **899 613** | **1 099 527** |

Le coût des titres (2 340 000 €) égalait 45 % des capitaux propres lors de l'entrée dans le périmètre, en 2014 (5 200 000 €) : les réserves du groupe sont sa part des capitaux propres accumulés depuis, 45 % × (12 637 600 – 5 200 000) = 3 346 920 €.

**ARZELIÈRE (80 % / 20 %) (0,5)**

| | Total retraité | Groupe (80 %) | Minoritaires (20 %) |
|---|---:|---:|---:|
| Capital | 2 000 000 | | |
| Réserves : 5 000 000 + 1 080 000 (écarts d'évaluation nets) | 6 080 000 | | |
| Capitaux propres hors résultat | 8 080 000 | 6 464 000 | 1 616 000 |
| Élimination des titres (coût d'acquisition) | | – 7 780 000 | |
| Écart d'acquisition | | + 1 316 000 | |
| **Réserves consolidées / intérêts minoritaires** | | **0** | **1 616 000** |
| Résultat : 900 000 – 217 500 | 682 500 | **546 000** | **136 500** |

Les capitaux propres hors résultat au 31/12/2026 égalent l'actif net réévalué d'acquisition (le résultat de 2025 a été mis en réserves, aucun dividende n'a été versé) : aucune réserve consolidée n'est acquise par le groupe en 2026, hors résultat. L'amortissement de l'écart (131 600 €) réduit ensuite le résultat du groupe.

**ATELIERS DU VINCOU (100 %) (0,5)** : capital 800 000 € éliminé contre les titres (800 000 €) ; réserves retraitées – 420 000 + 135 000 = **– 285 000 €**, résultat retraité – 180 000 + 202 500 = **22 500 €**, entièrement au groupe.

**Écritures (1,5)**

**C13 (0,75)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM Capital KAOLINS DU CHALARD | 3 000 000 | |
| RSV.KAOLINS Réserves retraitées | 9 637 600 | |
| RST.KAOLINS Résultat retraité | 1 999 140 | |
| 261 Titres de participation KAOLINS DU CHALARD | | 2 340 000 |
| RSV_G Réserves consolidées – part du groupe | | 3 346 920 |
| RSV_M Intérêts minoritaires – capital et réserves | | 6 950 680 |
| RST_G Résultat consolidé – part du groupe | | 899 613 |
| RST_M Intérêts minoritaires – résultat | | 1 099 527 |
| *Élimination des titres et partage (45 / 55)* | **14 636 740** | **14 636 740** |

**C14 (0,5)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM Capital ARZELIÈRE | 2 000 000 | |
| RSV.ARZELIERE Réserves retraitées | 6 080 000 | |
| RST.ARZELIERE Résultat retraité | 682 500 | |
| EA Écart d'acquisition ARZELIÈRE | 1 316 000 | |
| 261 Titres de participation ARZELIÈRE (7 600 000 + 180 000) | | 7 780 000 |
| RSV_M Intérêts minoritaires – capital et réserves (20 % × 8 080 000) | | 1 616 000 |
| RST_G Résultat consolidé – part du groupe | | 546 000 |
| RST_M Intérêts minoritaires – résultat | | 136 500 |
| *Élimination des titres, écart d'acquisition et partage (80 / 20)* | **10 078 500** | **10 078 500** |

**C15 (0,25)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM Capital ATELIERS DU VINCOU | 800 000 | |
| RSV_G Réserves consolidées – part du groupe | 285 000 | |
| RST.VINCOU Résultat retraité | 22 500 | |
| RSV.VINCOU Réserves retraitées (solde débiteur) | | 285 000 |
| 261 Titres de participation ATELIERS DU VINCOU | | 800 000 |
| RST_G Résultat consolidé – part du groupe | | 22 500 |
| *Élimination des titres et reprise des capitaux propres (100 %)* | **1 107 500** | **1 107 500** |

**Erreurs fréquentes.** Partager les capitaux propres individuels au lieu des capitaux propres retraités ; partager KAOLINS DU CHALARD à 60 / 40 ; oublier les écarts d'évaluation dans les capitaux propres d'ARZELIÈRE (`JUR-G01`, `JUR-G04`).

#### b. Mise en équivalence d'ÉCRIN DES TABLES (2 pts)

**Tableau (1 pt).** La valeur des titres mis en équivalence est la quote-part des capitaux propres retraités [V ANC art. 262-3, p. 49 ; F05 § 4]. Les titres ont été souscrits pour une valeur égale à 30 % des capitaux propres d'alors, sans écart d'évaluation : il n'y a aucun écart d'acquisition à suivre (`JUR-G03`).

| | Montant | Quote-part (30 %) |
|---|---:|---:|
| Capitaux propres au 31/12/2026 | 2 700 000 | **810 000** (titres mis en équivalence) |
| dont capitaux propres hors résultat | 2 300 000 | 690 000 |
| – Coût des titres | | – 480 000 |
| = Réserves consolidées (part du groupe) | | **210 000** |
| Résultat de 2026 | 400 000 | **120 000** |

**C16 (bilan, 0,5) / C16R (compte de résultat, 0,25)**

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence | 810 000 | |
| 261 Titres de participation ÉCRIN DES TABLES | | 480 000 |
| RSV_G Réserves consolidées – part du groupe | | 210 000 |
| RST_G Résultat consolidé – part du groupe | | 120 000 |
| *C16 : mise en équivalence (bilan)* | **810 000** | **810 000** |
| RES_CR Résultat | 120 000 | |
| QP_MEE Résultat net lié aux entités mises en équivalence | | 120 000 |
| *C16R : quote-part de résultat (compte de résultat)* | **120 000** | **120 000** |

**Dividende (0,25).** Le dividende de 60 000 € reçu en 2026 a été reclassé du résultat de VALCHEYRE vers les réserves (C9) : la quote-part de résultat (120 000 €) n'est pas diminuée du dividende, qui a réduit les capitaux propres d'ÉCRIN DES TABLES, donc la valeur d'équivalence.

---

### 1.9 Phases du processus, intégration globale et mise en équivalence (2,5 pts)

**Phases et traitements du dossier (1,5 pt)**

| Phase | Traitements du dossier |
|---|---|
| 1. Retraitements des comptes individuels des entités consolidées | Élimination des écritures fiscales : amortissements dérogatoires de KAOLINS DU CHALARD (1.4, C1). Homogénéisation : contrat de l'hôtel AUBRIANE à l'avancement (1.5, C2). Évaluation de l'entité acquise : écarts d'évaluation d'ARZELIÈRE et leur suivi (1.7, C10) |
| 2. Cumul des comptes des entités intégrées globalement | Bilans et comptes de résultat de VALCHEYRE, KAOLINS DU CHALARD, ARZELIÈRE et ATELIERS DU VINCOU, retraités, additionnés à 100 % |
| 3. Élimination des opérations internes | Ventes de pâtes et marges en stock (1.6 a, C3, C4), soldes clients-fournisseurs (C5), avance en compte courant et dépréciation (1.6 b, C6, C7), dividendes (1.6 c, C8, C9) |
| 4. Élimination des titres, écart d'acquisition et partage des capitaux propres | Frais d'acquisition des titres ARZELIÈRE (C11), écart d'acquisition et amortissement (C12, C14), partage de KAOLINS DU CHALARD, d'ARZELIÈRE et d'ATELIERS DU VINCOU (1.8 a, C13 à C15) |
| 5. Mise en équivalence | Substitution aux titres ÉCRIN DES TABLES de la quote-part de ses capitaux propres retraités (1.8 b, C16) |

(Phases : 0,5 ; rangement des traitements : 1.) L'intégration globale cumule les comptes après retraitements, élimine les opérations internes et partage les capitaux propres et le résultat [V ANC art. 221-2, p. 18-19 ; F03 § 3] ; la mise en équivalence substitue aux titres la quote-part des capitaux propres [V art. 221-4 ; F03 § 3]. Les retraitements précèdent le cumul : on additionne et on partage des comptes **homogènes** (`JUR-G01`).

**KAOLINS DU CHALARD et ÉCRIN DES TABLES (1 pt)**
- **Ce n'est pas le pourcentage de capital qui décide, c'est la méthode (0,25).** VALCHEYRE contrôle KAOLINS DU CHALARD (60 % des droits de vote) : la société est intégrée globalement, ses comptes sont repris à 100 %. Ils doivent donc être entièrement retraités, et ses opérations avec VALCHEYRE et ARZELIÈRE, autres sociétés intégrées, sont des opérations du groupe avec lui-même, éliminées à 100 % avant le partage à 45 / 55 [V art. 251-1 et 251-2, titre V « autres dispositions pour les intégrations globales », p. 45].
- **Ce qui ne s'applique pas à ÉCRIN DES TABLES (0,25).** Ses comptes ne sont pas cumulés : ses achats à VALCHEYRE (1 900 000 €) et sa dette (210 000 €) n'ont pas de contrepartie à éliminer dans les comptes consolidés. Ses ventes restent un chiffre d'affaires réalisé avec un tiers.
- **Ce qui s'applique aussi à ÉCRIN DES TABLES (0,5 : homogénéisation de ses comptes avant la quote-part, 0,25 ; dividende porté en réserves et absence de résultat interne en stock, 0,25).** Les règles de l'intégration globale servent à évaluer les capitaux propres et les résultats des entités mises en équivalence [V art. 262-1, p. 49] : si ÉCRIN DES TABLES comptabilisait des amortissements dérogatoires, ils seraient éliminés de ses capitaux propres avant le calcul de la quote-part ; elle n'en a pas, et ses comptes suivent déjà les méthodes du groupe. Les résultats internes réalisés avec elle sont éliminés **à hauteur du pourcentage détenu** (30 %) [V art. 262-4, p. 49-50 ; F04 R14] ; il n'y en a aucun au 31/12/2026, toutes les porcelaines ayant été revendues. Son dividende est éliminé du résultat et porté en réserves (C9). La prémisse de la question est donc à corriger : rien n'est « oublié » pour ÉCRIN DES TABLES ; le dossier n'appelle simplement aucun retraitement de ses comptes.

**Réponses tolérées.** L'élimination des résultats internes à hauteur de 30 % n'est pas exigée ; une réponse qui présente les éliminations comme propres à l'intégration globale et indique que les comptes d'ÉCRIN DES TABLES sont mis aux méthodes du groupe avant le calcul de la quote-part obtient les points.

**Erreurs fréquentes.** Lier l'élimination au pourcentage d'intérêt ; éliminer les ventes à ÉCRIN DES TABLES ; affirmer que les retraitements ne concernent jamais une entité mise en équivalence (`JUR-G01`).

---

### 1.10 Documents de synthèse (6 pts)

#### a. Information sectorielle (2,5 pts)

**Exigence ANC (0,25).** L'annexe ventile au minimum le chiffre d'affaires net par secteur d'activité **et** par zone géographique [V ANC art. 282-10, p. 77 ; F14 § 1.4], selon une segmentation issue de l'organisation interne [V art. 282-9, p. 77] : les trois activités suivies par le comité de direction. Elle donne aussi les chiffres de l'exercice précédent [V art. 282-1 ; F14 § 1.4]. Les informations complémentaires de l'art. 282-11 ne valent que pour les entités dont les instruments sont négociés sur Euronext Growth.

**Par secteur d'activité (0,75)**

| Secteur | Calcul | Chiffre d'affaires consolidé 2026 | % |
|---|---|---:|---:|
| Porcelaine de table et décor | 78 000 000 + 3 000 000 + 1 800 000 (contrat AUBRIANE à l'avancement) | 82 800 000 | 63,2 % |
| Porcelaine hôtelière | 10 000 000 + 20 000 000 | 30 000 000 | 22,9 % |
| Pâtes céramiques | 31 000 000 – 12 800 000 (ventes internes) | 18 200 000 | 13,9 % |
| **Total** | 142 000 000 – 12 800 000 + 1 800 000 | **131 000 000** | 100 % |

**Par zone géographique (0,75)**

| Zone | Calcul | Chiffre d'affaires consolidé 2026 | % |
|---|---|---:|---:|
| France | 90 600 000 – 12 800 000 + 1 800 000 | 79 600 000 | 60,8 % |
| Autres pays de l'Union européenne | 37 400 000 | 37 400 000 | 28,5 % |
| Reste du monde | 14 000 000 | 14 000 000 | 10,7 % |
| **Total** | | **131 000 000** | 100 % |

Les ventes internes de pâtes (clients français) sont éliminées ; le contrat de l'hôtel AUBRIANE (Paris) ajoute 1 800 000 € ; les ventes à ÉCRIN DES TABLES, mise en équivalence, sont conservées. Le total égale le chiffre d'affaires consolidé annoncé (131 M€).

**IFRS 8 si des titres étaient négociés sur un marché (0,75).** La norme s'applique aux états consolidés d'un groupe dont des instruments de dette ou de capitaux propres sont négociés sur un marché public [V IFRS 8 § 2 ; F14 § 6]. Elle retient l'**approche de la direction** : les **secteurs opérationnels** sont les composantes dont les résultats sont régulièrement examinés par le principal décideur opérationnel [V § 5 et 7], ici le comité de direction et ses trois activités. Un secteur est présenté s'il atteint 10 % des produits, **internes et externes**, du résultat ou des actifs [V § 13] : les pâtes, avec 31 000 000 € de produits dont 12 800 000 € de ventes au groupe, représentent 21,6 % des produits de tous les secteurs (143 800 000 €). Les produits externes des secteurs présentés doivent couvrir au moins 75 % du chiffre d'affaires [V § 15]. Pour chaque secteur, l'entité indique un résultat et, s'ils sont fournis au décideur, ses actifs et ses passifs [V § 23], **tels qu'ils lui sont présentés** [V § 25] ; elle ajoute des informations par produits, par zones géographiques et sur les clients représentant au moins 10 % des produits [V § 32-34].

**Erreurs fréquentes.** Garder les ventes internes de pâtes ; oublier le chiffre d'affaires à l'avancement ; éliminer les ventes à ÉCRIN DES TABLES ; se limiter à une ventilation par secteur (`JUR-F07`).

#### b. Notes de l'annexe sur les méthodes (1,5 pt)

L'annexe énonce les principales méthodes comptables du groupe et identifie celles retenues lorsqu'un choix est possible et a des incidences significatives [V ANC art. 282-2, p. 75 ; F14 § 10] ; elle explique les postes, dont les écarts d'acquisition et les impôts différés [V art. 282-19 à 282-30, intitulés ; F14 § 1.4].
- **Écritures fiscales (0,5).** Les amortissements dérogatoires et les autres écritures passées pour la seule application de la législation fiscale sont éliminés ; un impôt différé passif est constaté (103 580 € au 31/12/2026 sur les équipements de KAOLINS DU CHALARD).
- **Contrats à long terme (0,5).** Méthode à l'avancement, retenue par le groupe alors que le PCG permet aussi l'achèvement ; mesure de l'avancement par les coûts engagés rapportés au coût total prévisionnel ; perte à terminaison provisionnée en totalité ; incidence sur le contrat de l'hôtel AUBRIANE (chiffre d'affaires de 1 800 000 €).
- **Écart d'acquisition d'ARZELIÈRE (0,5).** Entrée dans le périmètre au 01/01/2026 (80 %, intégration globale) ; écart de 1 316 000 €, de durée d'utilisation limitée mais non déterminable de manière fiable, amorti sur 10 ans ; dotation de 131 600 € et valeur nette de 1 184 400 € ; éléments de l'analyse documentée.

**Réponses tolérées.** Une note sur KAOLINS DU CHALARD : l'annexe donne la fraction du capital détenue (45 %) et le mode de consolidation (intégration globale) [V art. 282-3, p. 75 ; F14 § 10] ; l'indication de la fraction des droits de vote (60 %, actions à droit de vote double) en éclaire la lecture, même si aucune justification n'est exigée au-delà de 40 % des droits de vote [V art. 282-4, p. 75 ; F14 § 10] (bonification dans la limite de la question).

#### c. Minoritaires de KAOLINS DU CHALARD dans des états IFRS (2 pts)

- **En ANC (0,5).** Le bilan consolidé présente les **intérêts minoritaires** dans une rubrique distincte des capitaux propres part du groupe [V art. 281-1, p. 66 ; F14 § 1.2] ; le compte de résultat déduit leur part du résultat de l'ensemble consolidé pour obtenir le résultat part du groupe [V art. 281-2 ; F14 § 1.3]. Au 31/12/2026, ceux de KAOLINS DU CHALARD s'élèvent à 6 950 680 + 1 099 527 = 8 050 207 €.
- **En IFRS (0,75).** Ils deviennent des **participations ne donnant pas le contrôle**, présentées **au sein des capitaux propres**, séparément des capitaux propres attribuables aux propriétaires de la société mère [V IAS 1 § 54 q) ; IFRS 10 § 22 ; F14 § 2.2 et § 4]. Ils sont une part des capitaux propres du groupe, non une dette.
- **Résultat (0,75).** L'état du résultat net et des autres éléments du résultat global attribue le résultat net **et** le résultat global aux propriétaires de la mère et aux participations ne donnant pas le contrôle [V IAS 1 § 81B ; F14 § 2.3] : le résultat net de l'ensemble n'est pas diminué de la part des minoritaires, il est réparti ; au 31/12/2026, la part des minoritaires de KAOLINS DU CHALARD dans le résultat est de 1 099 527 €.
- **Norme applicable (sans point, rappel de l'énoncé).** Pour l'exercice 2026, la présentation relève d'IAS 1 ; IFRS 18 ne s'applique qu'aux exercices ouverts à compter du 01/01/2027 [V règlement (UE) 2026/338 ; F14 § 0].

**Réponses tolérées.** L'indication d'une autre conséquence du passage aux IFRS sur les minoritaires (évaluation possible à la juste valeur lors d'une acquisition, IFRS 3 § 19 ; F05 § 2), si la réponse sur la présentation est donnée.
**Erreurs fréquentes.** Présenter les participations ne donnant pas le contrôle hors des capitaux propres en IFRS ; citer IFRS 18 pour les comptes de 2026 (`JUR-F06`).

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, date de la transmission, fusion simplifiée et référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2,5 |
| 2.2 Régime fiscal et conséquences pour les deux sociétés | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 3 |
| 2.3 a) Valeur de transmission du patrimoine | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 1,5 |
| 2.3 b) Actif net transmis et plus-values latentes | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 2 |
| 2.4 Mali, décomposition et affectation | `1.2.e` Calculer et analyser le boni ou mali de fusion | 5 |
| 2.5 a) Dépréciation des titres, reprise du patrimoine et annulation des titres | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) ; `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes | 3,5 |
| 2.5 b) Opérations entre les deux sociétés et frais | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 2 |
| 2.6 Suivi du mali technique au 31/12/2027 | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes ; `1.2.e` Calculer et analyser le boni ou mali de fusion | 3,5 |
| 2.7 Note à la présidente de MALVÉZIE | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Qualification, date de la transmission et fusion simplifiée (2,5 pts)

- *Qualification (0,75 pt).* MALVÉZIE détient toutes les actions de SÉCHOIRS DU LOYRE et elle est une personne morale. La dissolution d'une société dont toutes les parts ou actions sont réunies en une seule main entraîne la **transmission universelle de son patrimoine** à l'associé unique, **sans liquidation** [V C. civ. art. 1844-5, F02 § 1 ; PCG art. 710-2, F01 § 1]. Tous les actifs et tous les passifs de SÉCHOIRS DU LOYRE passent à MALVÉZIE, y compris ceux qui ne figurent pas au bilan, comme la marque « Jambon du Loyre », et SÉCHOIRS DU LOYRE disparaît. Aucune action n'est émise : MALVÉZIE ne peut se remettre ses propres titres, il n'y a **ni augmentation de capital, ni prime** ; les titres SÉCHOIRS DU LOYRE sont annulés et remplacés à l'actif de MALVÉZIE par les éléments du patrimoine reçu. L'associée de MALVÉZIE (la holding familiale) n'est pas concernée.
- *Date de la transmission et de l'enregistrement (0,75 pt).* Les créanciers de SÉCHOIRS DU LOYRE peuvent faire opposition dans les trente jours de la publication de la dissolution ; la transmission du patrimoine et la disparition de la société n'interviennent qu'**à l'issue de ce délai** [V C. civ. art. 1844-5, F02 § 1]. Le délai expirera le 30 juin 2027 et l'on suppose qu'aucun créancier ne fera opposition (annexe 2.1) : le patrimoine sera transmis le **1er juillet 2027**. Le code civil ne prévoyant pas d'effet antérieur pour cette opération, MALVÉZIE enregistre l'opération à cette date, à l'issue du délai d'opposition, sur la base des comptes de SÉCHOIRS DU LOYRE au 30 juin 2027 [V PCG art. 760-3, F01 § 1 et § 2.4]. Le résultat du premier semestre reste celui de SÉCHOIRS DU LOYRE ; il est compris dans l'actif net transmis.
- *Différence avec une fusion simplifiée, et point commun (0,75 pt).* Si MALVÉZIE absorbait sa filiale par une fusion, la détention permanente de toutes les actions dispenserait l'opération de l'approbation des assemblées et des rapports sur le projet [V C. com. L. 236-11, F01 § 1], et les actions détenues par MALVÉZIE ne seraient pas échangées [V C. com. L. 236-3 II 1°, F01 § 1]. Mais une fusion repose sur un **traité** qui en fixe les conditions et peut fixer une date d'effet antérieure à la réalisation, dans les limites légales [V C. com. L. 236-4, F02 § 5] ; la transmission universelle résulte de la **seule décision de l'associée unique**, sans traité, et sa date est celle de l'expiration du délai d'opposition, sans effet antérieur en comptabilité, le code civil ne le prévoyant pas [V PCG art. 760-3]. En revanche, **dans les comptes de MALVÉZIE, les deux opérations donnent les mêmes écritures** : contrôle commun, donc valeur comptable, aucune action émise, annulation des titres et même mali [V PCG art. 743-1, 760-1, 760-2, F01 § 1 et § 2].
- *Référentiel (0,25 pt).* Les comptes individuels de MALVÉZIE suivent le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui vise expressément les confusions de patrimoine de l'art. 1844-5 du code civil et leur consacre des règles particulières [V PCG art. 710-1 et 760-1 à 760-3, F01 § 1].

---

### 2.2 Régime fiscal (3 pts)

- *Régime applicable (0,75 pt).* Fiscalement, la transmission universelle du patrimoine d'une filiale à son associée unique est une **fusion** [V CGI art. 210-0 A, I, 1° et 3°, F02 § 1]. Les deux sociétés sont soumises à l'impôt sur les sociétés : l'opération relève **de plein droit** du régime de faveur de l'art. 210 A, **sauf option pour le régime de droit commun** [V BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1]. MALVÉZIE n'exerçant aucune option (annexe 2.1), le régime de faveur s'applique. Aucun agrément n'est nécessaire : SÉCHOIRS DU LOYRE n'a pas de déficit à transférer.
- *Conséquences pour SÉCHOIRS DU LOYRE (0,75 pt).*
  - Son **résultat du premier semestre 2027** (48 000 € avant impôt) est imposé immédiatement, dans une déclaration établie pour la période close par l'opération, quel que soit le régime [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2]. L'impôt, 12 000 €, est déjà comptabilisé ; la dette passe à MALVÉZIE avec le patrimoine.
  - Les **plus-values latentes** (jambons 240 000 €, bâtiment 360 000 €, marque 420 000 €, soit 1 020 000 €) **ne sont pas imposées** [V CGI art. 210 A-1, F02 § 2].
  - La **provision pour litige** (30 000 €), déduite et toujours justifiée, n'est pas réintégrée : elle ne serait imposable que si elle devenait sans objet [V CGI art. 210 A-2, F02 § 2].
- *Engagements de MALVÉZIE (0,75 pt)* [V CGI art. 210 A-3, F02 § 4] :
  - reprendre à son passif la provision pour litige (a) ;
  - calculer la plus-value de cession future de la **marque** et du **terrain**, éléments non amortissables, d'après leur valeur fiscale chez SÉCHOIRS DU LOYRE, nulle pour la marque (c) ;
  - **bâtiment et installations** : les plus-values des biens amortissables sont en principe réintégrées sur quinze ou cinq ans (d), mais les biens sont transmis à leur valeur comptable, avec leurs valeurs d'origine et leurs amortissements, valeurs admises fiscalement : il n'y a aucune plus-value à réintégrer, et MALVÉZIE poursuit les plans d'amortissement de sa filiale [V BOI-IS-FUS-10-20-40-20 § 170 et 180, F01 § 3.2] ;
  - inscrire les **jambons** à leur valeur fiscale chez SÉCHOIRS DU LOYRE (720 000 €), ce que fait la valeur comptable (e).
- *Sort fiscal du mali (0,5 pt).* Le **mali technique** (960 000 €, voir 2.4) ne peut donner lieu à aucune déduction ultérieure : la charge constatée lors de la vente des jambons et l'amortissement du mali affecté au bâtiment seront réintégrés extra-comptablement, puisqu'ils représentent des plus-values qui n'ont pas été imposées [V CGI art. 210 A-1, al. 3 ; BOI-IS-FUS-10-50-20 § 130, F02 § 2 ter]. Le **vrai mali** (400 000 €) est en principe une moins-value à long terme, les titres étant des titres de participation détenus depuis plus de deux ans (1er juillet 2023) [V même BOI § 50, F02 § 2 ter] ; selon l'hypothèse de l'annexe 2.6, l'excédent des moins-values de cette catégorie n'est ni déductible ni reportable : la dépréciation est réintégrée [V CGI art. 219, I-a quinquies, F02 § 2 ter].
- *Droit commun (0,25 pt).* SÉCHOIRS DU LOYRE serait imposée comme en cas de cessation d'entreprise : sur ses plus-values latentes (1 020 000 €, soit 255 000 € d'impôt) et sur la provision [V BOI-IS-FUS-10-10-20 § 10 et 20, F02 § 2]. En contrepartie, les charges constatées ensuite par MALVÉZIE sur le mali technique (sortie avec les jambons, amortissement) seraient **déductibles** [V BOI-IS-FUS-10-50-20 § 180, F02 § 2 ter]. Le traitement du vrai mali ne changerait pas.

---

### 2.3 Valeur de transmission et actif net transmis (3,5 pts)

**a) Valeur de transmission du patrimoine (1,5 pt)**
- *Situation de contrôle (0,5 pt).* MALVÉZIE détient 100 % des droits de vote de SÉCHOIRS DU LOYRE : elle la contrôle **de manière exclusive** [V PCG art. 741-2, F01 § 2.1]. L'une des sociétés contrôlant l'autre, l'opération est réalisée **sous contrôle commun** [V art. 741-1, F01 § 2.1].
- *Règle (0,75 pt).* Une confusion de patrimoine est par définition toujours réalisée entre entreprises sous contrôle commun : les actifs et passifs de la société dissoute sont **toujours transmis à leur valeur comptable** [V PCG art. 760-1, 744-2, F01 § 2.3 et § 2.4]. Le sens de l'opération est sans objet, et l'exception de l'actif net comptable insuffisant ne s'applique pas aux confusions de patrimoine, qui ne libèrent aucun capital [V art. 743-3, F01 § 2.4].
- *Conséquences (0,25 pt).* MALVÉZIE reprend chaque élément pour sa valeur dans les comptes de SÉCHOIRS DU LOYRE au 30/06/2027, avec les **valeurs d'origine, les amortissements et les dépréciations** [V art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170 et 180, F01 § 3.2]. La marque, absente du bilan, n'est pas inscrite comme telle ; les valeurs de l'expert (annexe 2.4) ne servent qu'à analyser le mali.

**b) Actif net transmis et plus-values latentes (2 pts)**
- *Actif net comptable transmis (1 pt)* :

| Élément | Valeur brute | Amortissements et dépréciations | Valeur nette |
|---|---:|---:|---:|
| Terrain | 150 000 | | 150 000 |
| Bâtiment du séchoir | 1 600 000 | 800 000 | 800 000 |
| Installations techniques | 1 200 000 | 700 000 | 500 000 |
| Jambons en cours de séchage | 720 000 | | 720 000 |
| Clients | 340 000 | 20 000 | 320 000 |
| Disponibilités | 70 000 | | 70 000 |
| **Total de l'actif transmis** | **4 080 000** | **1 520 000** | **2 560 000** |
| Provision pour litige | | | – 30 000 |
| Emprunt auprès d'un établissement de crédit | | | – 600 000 |
| Compte courant de MALVÉZIE | | | – 150 000 |
| Fournisseurs | | | – 110 000 |
| Dettes fiscales et sociales | | | – 70 000 |
| **Actif net comptable transmis** | | | **1 600 000** |

Il est égal aux capitaux propres de SÉCHOIRS DU LOYRE au 30/06/2027, résultat du semestre compris (400 000 + 40 000 + 1 022 000 + 102 000 + 36 000). Les dettes envers MALVÉZIE (54 000 € et 150 000 €) font partie du patrimoine transmis : elles s'éteindront ensuite par confusion (voir 2.5 b).

- *Plus-values latentes à retenir (1 pt)* :

| Élément | Valeur réelle | Valeur comptable | Plus-value latente | Impôt (25 %) | Plus-value retenue |
|---|---:|---:|---:|---:|---:|
| Jambons en cours de séchage (24 000 × 10 €) | 960 000 | 720 000 | 240 000 | – 60 000 | **180 000** |
| Bâtiment du séchoir | 1 160 000 | 800 000 | 360 000 | – | **360 000** |
| Marque « Jambon du Loyre » (non inscrite) | 420 000 | 0 | 420 000 | – | **420 000** |
| Terrain, installations, autres éléments | | | 0 | | 0 |
| **Total** | | | **1 020 000** | | **960 000** |

  - Les **jambons** seront achevés et vendus dans les douze mois : ce sont des éléments destinés à être revendus à brève échéance, dont la plus-value latente est retenue **nette d'impôt** (240 000 × 75 % = 180 000 €) [V PCG art. 745-4, F01 § 5.3 ; annexe 2.7] (0,5 pt).
  - Le **bâtiment** et la **marque** sont conservés : leurs plus-values sont retenues pour leur **montant brut** (0,25 pt).
  - Le mali technique comprend les plus-values sur des éléments **non comptabilisés** chez l'absorbée, comme la marque ; aucun passif non comptabilisé n'est à déduire et l'expert n'identifie **aucun fonds commercial** (annexe 2.4) (0,25 pt).

---

### 2.4 Mali, décomposition et affectation (5 pts)

- *Résultat de l'annulation des titres (1 pt).* Actif net reçu à hauteur de la participation (100 %) : **1 600 000 €** ; valeur comptable de la participation : prix 2 880 000 + frais d'acquisition inscrits dans le coût 80 000 = **2 960 000 €**, jamais dépréciée. L'écart est négatif : **mali = 2 960 000 – 1 600 000 = 1 360 000 €** [V PCG art. 745-3, F01 § 5.3 ; annexe 2.7]. Il naît de l'inscription des éléments reçus à la valeur comptable, alors que le prix payé en 2023 reflétait leur valeur réelle et la rentabilité attendue du séchoir.
- *Mali technique (1 pt).* Il correspond, à hauteur de la participation, aux plus-values latentes sur les éléments d'actif comptabilisés ou non, nettes des passifs non comptabilisés [V art. 745-4, F01 § 5.3] : **960 000 €** (voir 2.3 b), inférieur au mali. Il n'est pas une perte : il représente la part du coût des titres qui correspond à des plus-values que la valeur comptable ne fait pas apparaître (stock, bâtiment, marque). Il est inscrit à l'actif.
- *Vrai mali (1,5 pt).* Le surplus, **1 360 000 – 960 000 = 400 000 €**, n'est justifié par aucune plus-value : SÉCHOIRS DU LOYRE vaut, au 1er juillet 2027, son actif net comptable augmenté de ses plus-values latentes nettes, soit 1 600 000 + 960 000 = **2 560 000 €**, puisque l'expert n'identifie aucun fonds commercial, alors que les titres figurent pour 2 960 000 €. Les titres ont **perdu 400 000 € de valeur** depuis l'acquisition : le prix de 2023 intégrait le contrat de séchage, qui représentait près de la moitié de l'activité et a pris fin en février 2027 (annexe 2.3). Ce vrai mali est la **dépréciation des titres nécessaire au moment de l'opération**, comptabilisée dans le **résultat financier de 2027** ; il ne peut pas être maintenu à l'actif [V art. 745-4, F01 § 5.3 ; annexe 2.7]. Il n'est pas créé par l'opération : sans elle, la même dépréciation aurait dû être constatée à la clôture de 2027.
- *Affectation du mali technique (1,5 pt).* Le mali technique (960 000 €) est égal à la somme des plus-values latentes estimées de manière fiable sur les actifs identifiés : il n'est pas supérieur à cette somme, donc rien ne va au fonds commercial, et l'affectation au prorata des plus-values donne à chaque actif **la totalité de sa plus-value** [V art. 745-5, F01 § 5.4]. Il est inscrit dans un compte spécifique par catégorie d'actif [V art. 745-6, F01 § 5.4] :

| Actif sous-jacent | Plus-value retenue | Mali affecté | Compte |
|---|---:|---:|---|
| Jambons en cours de séchage | 180 000 | **180 000** | 4781 Mali de fusion sur actif circulant |
| Bâtiment du séchoir | 360 000 | **360 000** | 2187 Mali de fusion sur actifs corporels |
| Marque « Jambon du Loyre » | 420 000 | **420 000** | 2081 Mali de fusion sur actifs incorporels |
| **Total** | **960 000** | **960 000** | |

Barème de l'affectation : règle et absence de fonds commercial (0,5) ; montants (0,5) ; comptes (0,5).

---

### 2.5 Écritures au 1er juillet 2027 chez MALVÉZIE (5,5 pts)

**a) Dépréciation des titres, reprise du patrimoine et annulation des titres (3,5 pts)**

**A1 — Vrai mali : dépréciation des titres (1 pt).** Le vrai mali est une dépréciation de la participation, constatée en résultat financier [V art. 745-4, F01 § 5.3 et § 9 ; compte 6866 Dotations pour dépréciation des éléments financiers, liste des comptes du PCG 2026].

| Compte | Débit | Crédit |
|---|---:|---:|
| 6866 Dotations pour dépréciation des éléments financiers | 400 000 | |
| 2961 Dépréciations des titres de participation (SÉCHOIRS DU LOYRE) | | 400 000 |

**A2 — Reprise du patrimoine à la valeur comptable, annulation des titres et mali technique (2,5 pts).** Actifs à leur valeur brute (0,75) ; amortissements et dépréciations (0,5) ; provision et dettes (0,5) ; mali technique par catégorie (0,5) ; annulation des titres et de leur dépréciation (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 211 Terrains | 150 000 | |
| 2131 Bâtiments (séchoir) | 1 600 000 | |
| 2151 Installations complexes spécialisées (saloirs, chambres, ventilation) | 1 200 000 | |
| 331 Produits en cours (jambons en cours de séchage) | 720 000 | |
| 411 Clients | 340 000 | |
| 512 Banques | 70 000 | |
| 2081 Mali de fusion sur actifs incorporels (marque) | 420 000 | |
| 2187 Mali de fusion sur actifs corporels (bâtiment) | 360 000 | |
| 4781 Mali de fusion sur actif circulant (jambons) | 180 000 | |
| 2961 Dépréciations des titres de participation | 400 000 | |
| 2813 Amortissements des constructions | | 800 000 |
| 2815 Amortissements des installations techniques | | 700 000 |
| 491 Dépréciations des comptes de clients | | 20 000 |
| 1511 Provisions pour litiges | | 30 000 |
| 164 Emprunts auprès des établissements de crédit | | 600 000 |
| 4551 Associés – Comptes courants (avance de MALVÉZIE) | | 150 000 |
| 401 Fournisseurs | | 110 000 |
| 444 État – Impôts sur les bénéfices | | 12 000 |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | | 58 000 |
| 261 Titres de participation SÉCHOIRS DU LOYRE | | 2 960 000 |
| **Total** | **5 440 000** | **5 440 000** |

Contrôle : actif net reçu 1 600 000 + mali technique 960 000 + dépréciation 400 000 = valeur brute des titres 2 960 000.

**b) Opérations entre les deux sociétés et frais (2 pts)**

**A3 — Dette de séchage à façon (0,5 pt).** MALVÉZIE devient à la fois débitrice (dette fournisseur) et créancière (créance client reçue de sa filiale) : la créance et la dette s'éteignent par **confusion** [V C. civ. art. 1349, F01 § 8].

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette envers SÉCHOIRS DU LOYRE) | 54 000 | |
| 411 Clients (créance de SÉCHOIRS DU LOYRE sur MALVÉZIE) | | 54 000 |

**A4 — Avance de trésorerie (0,5 pt).** Même extinction par confusion.

| Compte | Débit | Crédit |
|---|---:|---:|
| 4551 Associés – Comptes courants (dette reprise de SÉCHOIRS DU LOYRE) | 150 000 | |
| 451 Groupe (avance à SÉCHOIRS DU LOYRE) | | 150 000 |

*Prestations de séchage du premier semestre (0,5 pt).* Les 162 000 € facturés du 1er janvier au 30 juin 2027 **ne sont pas éliminés** : ils ont été réalisés entre deux personnes distinctes, avant la transmission. Ils sont compris dans le résultat du semestre de SÉCHOIRS DU LOYRE, donc dans l'actif net transmis, et dans les charges de MALVÉZIE. L'opération n'ayant aucun effet antérieur, MALVÉZIE ne reprend pas les produits et les charges du semestre de sa filiale : seules les **créances et dettes** encore ouvertes au 1er juillet s'éteignent. Le profit éventuel de SÉCHOIRS DU LOYRE sur ces prestations est déjà compris dans ses capitaux propres et a été taxé chez elle.

**A5 — Frais de l'opération (0,5 pt).** Sans augmentation de capital, il n'y a pas de prime sur laquelle imputer les frais ; MALVÉZIE les comptabilise en charges, selon l'annexe 2.5 [V PCG art. 212-9, F01 § 7].

| Compte | Débit | Crédit |
|---|---:|---:|
| 6226 Honoraires | 17 600 | |
| 6231 Annonces et insertions (publication de la dissolution) | 2 400 | |
| 401 Fournisseurs | | 20 000 |

---

### 2.6 Suivi du mali technique au 31 décembre 2027 (3,5 pts)

Le mali technique est amorti ou rapporté au résultat selon les mêmes règles que l'actif auquel il est affecté, et le suit en cas de cession [V PCG art. 745-7 et 745-10, F01 § 5.5 ; annexe 2.7]. Le suivi porte sur le seul second semestre de 2027, première clôture après l'opération.

**A6 — Jambons vendus (1,25 pt).** 16 000 des 24 000 jambons seront vendus d'ici au 31/12/2027 (prévision de l'annexe 2.6) : la part correspondante du mali est rapportée au résultat avec eux, comme une partie de leur coût, soit 180 000 × 16 000 / 24 000 = **120 000 €** (0,75). Les 60 000 € restants suivent les 8 000 jambons encore en séchage, dont la valeur réelle couvre le coût augmenté du mali : aucune dépréciation (0,25). Écriture (0,25) :

| Compte | Débit | Crédit |
|---|---:|---:|
| 7133 Variation des en-cours de production de biens (mali des jambons vendus) | 120 000 | |
| 4781 Mali de fusion sur actif circulant | | 120 000 |

**A7 — Bâtiment (1 pt).** Le mali affecté au bâtiment est amorti comme lui, en linéaire sur sa durée résiduelle de vingt ans, à compter du 1er juillet 2027 : 360 000 / 20 × 6/12 = **9 000 €** ; valeur nette du mali au 31/12/2027 : 351 000 €. (Le bâtiment lui-même est amorti de 1 600 000 / 40 × 6/12 = 20 000 € dans les comptes de MALVÉZIE, écriture courante non demandée.)

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles | 9 000 | |
| 28187 Amortissement du mali de fusion sur actifs corporels | | 9 000 |

*Marque (0,5 pt).* La durée d'utilisation de la marque n'a pas de limite prévisible : comme la marque elle-même, la part du mali qui lui est affectée **n'est pas amortie** (0,25). Elle ne serait dépréciée que si la valeur actuelle de la marque devenait inférieure à la part de mali affectée ; aucun indice de perte de valeur n'existe au 31/12/2027 : **aucune écriture** (0,25) [V art. 745-7 et 745-8, F01 § 5.5].

*Traitement fiscal (0,75 pt).* Les charges des écritures A6 et A7 (120 000 + 9 000 = **129 000 €**) ne sont pas déductibles : elles sont **réintégrées extra-comptablement** dans le résultat fiscal de 2027 [V CGI art. 210 A-1, al. 3 ; BOI-IS-FUS-10-50-20 § 130, F02 § 2 ter] (0,5). La dépréciation de 400 000 € (A1) est elle aussi réintégrée, selon l'hypothèse de l'annexe 2.6 : réintégrations de l'exercice 2027 liées à l'opération, **529 000 €** (0,25).

---

### 2.7 Note à Mme MALVÉZIE, présidente de MALVÉZIE Salaisons (2 pts)

*Objet : effets de la dissolution sans liquidation de SÉCHOIRS DU LOYRE sur les comptes de MALVÉZIE.*

- *Capitaux propres et bilan juste après l'opération (1 pt).* Le capital, les réserves et le report à nouveau ne changent pas : la transmission ne donne lieu à aucune émission d'actions. Le résultat de 2027, de 300 000 € au 30/06/2027, est ramené à **– 120 000 €** juste après l'opération, sous l'effet de la dépréciation des titres (– 400 000 €) et des frais (– 20 000 €), avant impôt. Les capitaux propres passent de 4 250 000 € à **3 830 000 €** (capital 1 500 000 ; réserves 2 300 000 ; report à nouveau 150 000 ; résultat – 120 000). Au bilan, les titres (2 960 000 €) disparaissent et sont remplacés par les actifs et les passifs du séchoir et par le mali technique, inscrit pour 780 000 € dans les immobilisations (marque 420 000, bâtiment 360 000) et pour 180 000 € dans l'actif circulant (jambons). Bilan simplifié (en €) :

| Actif | Avant | Après | Capitaux propres et passif | Avant | Après |
|---|---:|---:|---|---:|---:|
| Immobilisations corporelles nettes | 4 100 000 | 5 550 000 | Capitaux propres | 4 250 000 | 3 830 000 |
| Mali technique (2081, 2187) | – | 780 000 | Provisions pour risques | 60 000 | 90 000 |
| Titres SÉCHOIRS DU LOYRE | 2 960 000 | – | Emprunts bancaires | 3 400 000 | 4 000 000 |
| Stocks | 1 900 000 | 2 620 000 | Fournisseurs | 1 900 000 | 1 976 000 |
| Mali technique (4781) | – | 180 000 | Dettes fiscales et sociales | 1 290 000 | 1 360 000 |
| Clients et autres créances | 1 640 000 | 1 756 000 | | | |
| Disponibilités | 300 000 | 370 000 | | | |
| **Total** | **10 900 000** | **11 256 000** | **Total** | **10 900 000** | **11 256 000** |

- *Banque de MALVÉZIE (0,5 pt).* Le rapport des emprunts aux capitaux propres passe de 3 400 000 / 4 250 000 = **0,80** à 4 000 000 / 3 830 000 = **1,04** : il dépasserait le plafond de 1,00, ce qui permettrait à la banque d'exiger le remboursement anticipé. La seule dépréciation des titres, nécessaire de toute façon, l'aurait porté à 3 400 000 / 3 850 000 = 0,88 ; c'est la reprise de l'emprunt de 600 000 € du séchoir qui fait franchir le seuil. Le rapport ne se calcule que sur les comptes annuels : il faut négocier avec la banque **avant l'opération** (accord sur le dépassement, calcul qui tienne compte de l'emprunt repris) ou envisager le remboursement de l'emprunt du séchoir, et suivre le résultat du second semestre.
- *Créanciers de SÉCHOIRS DU LOYRE et administration fiscale (0,5 pt).* Les créanciers du séchoir (banque, fournisseurs, personnel, organismes sociaux) ont désormais pour débitrice MALVÉZIE, plus solide mais plus endettée ; ils peuvent faire opposition dans les trente jours de la publication pour obtenir le remboursement de leurs créances ou des garanties ; l'hypothèse retenue est qu'ils ne le feront pas. L'administration recevra la déclaration du dernier résultat de SÉCHOIRS DU LOYRE (impôt de 12 000 € payé par MALVÉZIE) ; elle vérifiera les engagements du régime de faveur, la réintégration des charges liées au mali technique (129 000 € en 2027) et celle de la dépréciation de 400 000 € : celle-ci ne serait déductible que par compensation avec des plus-values à long terme sur titres de participation, ce qui supposerait de justifier la réalité de la perte, par exemple par la fin du contrat [V BOI-IS-FUS-10-50-20 § 60, F02 § 2 ter].

---

### Réponses tolérées
- **2.1** : toute formulation qui établit la transmission à l'expiration du délai d'opposition, sans effet antérieur, et la différence de nature entre la décision de l'associée unique et un traité de fusion. La date du 30 juin 2027 (dernier jour du délai) est comptée à moitié sur l'item de la date.
- **2.2** : provision pour litige non citée si l'engagement de reprise des provisions est énoncé ; vrai mali présenté comme une dépréciation de titres de participation non déductible, sans référence au régime des moins-values à long terme, si l'hypothèse de l'annexe 2.6 est appliquée.
- **2.3 b** : plus-value du stock retenue brute (240 000 €) : item du stock à 0, et mali technique de 1 020 000 € accepté pour la suite si la méthode est cohérente (vrai mali 340 000 €) [JUR-F08].
- **2.4** : affectation présentée comme le cas « mali technique supérieur ou égal à la somme des plus-values » (chaque actif reçoit sa plus-value, aucun fonds commercial) : même résultat, accepté.
- **2.5 a** : A1 et A2 réunies, avec 6866 débité directement dans l'écriture d'annulation (présentation abrégée, F01 § 9) ; reprise en deux écritures (constatation d'une créance de transmission sur la filiale, compte 458 ou 4561, puis réalisation) ; dettes fiscales et sociales regroupées sur un compte de la classe 4 ; installations au compte 215 ou 2154.
- **2.5 b** : frais au compte 6227 ; A3 et A4 réunies.
- **2.6** : A6 au débit du compte 71355 (variation des stocks de produits finis), ou d'un compte de charges de la classe 6 si le choix est justifié par la sortie des jambons ; amortissement du mali calculé sur douze mois (18 000 €) : item de calcul à 0.
- **2.7** : capitaux propres après impôt si l'économie d'impôt sur les seuls frais déductibles est retenue (3 835 000 €, rapport 1,04) ; toute présentation chiffrée et cohérente du bilan.

### Erreurs fréquentes (rapports du jury)
- `JUR-R02` Analyse du mali non conduite : mali de 1 360 000 € inscrit en totalité à l'actif (ou en totalité en charges), vrai mali assimilé à un fonds commercial, plus-value du stock retenue brute ; mali calculé sur le prix sans les frais (1 280 000 €).
- `JUR-R04` Suivi du mali mal traité alors que l'annexe 2.7 donne la règle : mali affecté à la marque amorti, mali du stock repris en totalité (180 000 €) alors que 8 000 jambons restent en stock, amortissement du mali du bâtiment calculé sur une année entière.
- `JUR-R05` Difficulté à s'adapter : augmentation de capital ou prime de fusion calculées ; valeur réelle retenue au motif que l'expert a évalué les éléments ; marque inscrite en immobilisation incorporelle (205) au lieu d'un mali affecté ; écritures datées du 12 mai ou du 1er janvier 2027.
- `JUR-F07` Annexes mal exploitées : dettes envers MALVÉZIE (54 000 € et 150 000 €) laissées au bilan ; prestations du semestre éliminées ; impôt du semestre de la filiale oublié dans les dettes reprises ; amortissements et dépréciations compensés avec les valeurs brutes.
- `JUR-F04` Absence de contrôle d'équilibre de l'écriture A2.
- `JUR-F06` Hypothèses non écrites (frais en charges, sort fiscal du vrai mali).
- Erreurs propres à ce cas : opération qualifiée de fusion simplifiée « avec effet au 1er janvier 2027 » ; régime de faveur présenté comme une option ; vrai mali déclaré déductible au taux de 25 % ; charges du mali technique déduites en régime de faveur.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. civ. art. 1844-5 | Dissolution sans liquidation, transmission universelle du patrimoine à l'associé unique personne morale, opposition des créanciers, transmission à l'issue du délai | [V] | F02 § 1 |
| PCG art. 710-1, 710-2 | Champ du titre VII, confusion de patrimoine | [V] p. 81 | F01 § 1 |
| C. com. L. 236-3 II, L. 236-4, L. 236-11 | Absence d'échange des titres détenus par l'absorbante, date d'effet du traité, fusion simplifiée | [V] lus le 17/11/2026 | F01 § 1 ; F02 § 5 |
| PCG art. 741-1, 741-2, 743-1, 743-3, 744-2, 760-1 à 760-3 | Contrôle commun, valeur comptable, confusion de patrimoine toujours à la valeur comptable, aucun effet antérieur, écritures à l'issue du délai d'opposition | [V] p. 82-85 et 90-91 | F01 § 2 et § 3.2 |
| BOI-IS-FUS-10-20-40-20 § 170 et 180 | Reprise des valeurs d'origine, amortissements et dépréciations | [V] BOFiP | F01 § 3.2 |
| PCG art. 745-3 à 745-10 | Mali, mali technique, plus-values nettes d'impôt pour les actifs revendus à brève échéance, vrai mali en résultat financier, affectation, comptes spécifiques, suivi | [V] p. 86-87 | F01 § 5.3 à 5.5 |
| Liste des comptes du PCG 2026 | 2081, 2187, 4781, 28187, 2961, 6866 | [V] p. 135-146 | F01 § 5.4 et § 9 |
| C. civ. art. 1349 | Extinction par confusion des créances réciproques | [V] | F01 § 8 |
| PCG art. 212-9 | Frais de fusion : frais d'établissement, prime ou charges | [V] p. 15-16 | F01 § 7 |
| CGI art. 210-0 A, 210 A-1, 210 A-2, 210 A-3 ; BOI-IS-FUS-10-10-10 § 10 et 20 ; BOI-IS-FUS-10-20-30 § 210 et 330 ; BOI-IS-FUS-10-10-20 § 10 et 20 | TUP traitée comme une fusion, régime de faveur sauf option, dernier résultat de l'absorbée, provisions, engagements, droit commun | [V] | F02 § 1, § 2 et § 4 |
| CGI art. 210 A-1, al. 3 et 4 ; art. 219, I-a quinquies ; BOI-IS-FUS-10-50-20 § 50, 60, 130, 180 | Mali technique non déductible en régime de faveur, déductible en droit commun ; vrai mali, moins-value à long terme sur titres de participation, preuve de la perte | [V] lus le 17/11/2026 | F02 § 2 ter |
| Compte de la sortie du mali avec les jambons (7133) | Écriture | Convention de rédaction : le mali suit l'actif sous-jacent (art. 745-10), le PCG ne désigne pas de compte | F01 § 5.5 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Conditions d'accès et périmètres de l'expert-comptable, du commissaire aux comptes et de l'auditeur de durabilité ; limites de la proposition de l'expert-comptable | `3.1.a` Cadres d'exercice professionnel | 1,5 |
| 3.2 Durée du mandat, impossibilité d'une révocation par l'assemblée, relèvement judiciaire, démission | `3.1.b` Nomination et cessation | 1,5 |
| 3.3 Attestation demandée par la banque ; calcul des remboursements (autorévision) | `3.1.c` Principes déontologiques | 1,5 |
| 3.4 Certification, attestation et audit contractuel ; portée de l'opinion pour la banque | `3.2.a` Notion d'audit et typologie des missions | 1,5 |
| 3.5 Risque du cycle capitaux propres et assertions ; extrait de la NEP sélection ; procédures | `3.2.c` Approche par les risques ; `3.1.d` Référentiel normatif (NEP) ; `3.2.d` Démarche d'audit | 6,5 |
| 3.6 Honoraires et barème ; droit de communication et entretiens | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.7 Parts des associés sortis maintenues en capital ; affectation du résultat ; écriture ; opinion selon la correction ; parties du rapport | `3.2.e` Portée des opinions | 2 |
| 3.8 Responsabilités civile, disciplinaire et pénale ; secret professionnel | `3.1.e` Mise en cause de la responsabilité | 2 |
| 3.9 Norme volontaire (VSME) ou ESRS : place, étendue et limites, conséquence pour la vérification | `3.3.a` Contexte et architecture des normes de durabilité | 2 |
| 3.10 Matérialité d'impact et matérialité financière ; IRO du cas ; correction de la matrice | `3.3.b` Principes de construction du reporting | 4 |
| 3.11 Objectifs, assurance limitée, axes, vérification du processus ; procédures sur le processus | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4,5 |
| 3.12 Avis sur le processus selon la correction ; incidence sur les autres parties du rapport | `3.4.c` Portée des avis | 1,5 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Cadres d'exercice et proposition du cabinet ROCHEVIGNE (1,5 pt)

**Conditions d'accès et périmètres (0,75 pt ; 0,25 pt par profession)**
- **Expert-comptable** : nul ne peut porter le titre ni exercer la profession s'il n'est **inscrit au tableau de l'ordre**, tenu par le **conseil régional de l'ordre** ; l'inscription suppose notamment le **diplôme d'expertise comptable** et des garanties de moralité [V ord. 45-2138 art. 3, art. 31, art. 40]. Il intervient par **mission contractuelle** : tenir, centraliser, arrêter et réviser les comptabilités, analyser la situation de l'entreprise [V ord. art. 2]. C'est le cadre actuel du cabinet ROCHEVIGNE (comptabilité, paie, comptes annuels).
- **Commissaire aux comptes** : personne ou société **inscrite sur la liste tenue par la H2A**, qui peut déléguer l'inscription à la CNCC ; conditions : honorabilité, **stage professionnel** et **certificat d'aptitude aux fonctions de commissaire aux comptes ou diplôme d'expertise comptable** ; serment ; rattachement à une **compagnie régionale** [V L. 821-13 I, L. 820-1 II, L. 821-14, L. 821-23, L. 821-12]. Une société de commissaires aux comptes doit notamment être détenue majoritairement par des commissaires aux comptes [V L. 821-16]. Il exerce des **missions légales**, dont la certification des comptes, et des **prestations** [V L. 821-2 III-IV].
- **Auditeur des informations en matière de durabilité** : soit un **commissaire aux comptes inscrit sur la liste spécifique** de la H2A, après huit mois de stage et une épreuve sur la certification de ces informations, soit un **auditeur exerçant au sein d'un organisme tiers indépendant** accrédité par le comité français d'accréditation et inscrit sur la liste de la H2A [V L. 821-13 II, L. 821-18 I, L. 822-1 II, L. 822-3, L. 822-4]. Dans une société de commissaires aux comptes, le rapport sur la durabilité est signé par un associé inscrit sur cette liste [V L. 821-26].

**Ce que le cabinet ROCHEVIGNE ne peut pas faire (0,75 pt)**
- **Certifier les comptes qu'il tient et prépare** : il se prononcerait sur ses propres travaux. Hors entité d'intérêt public, le commissaire aux comptes ne peut accepter la mission s'il existe un **risque d'autorévision** sans mesure de sauvegarde possible [V L. 821-28 IV ; code de déontologie art. 5 II, art. 22]. Garder la comptabilité, la paie et les comptes « en conservant nos travaux actuels » est donc incompatible avec la certification (0,25 pt).
- **Vérifier les informations en matière de durabilité** : aucun de ses associés n'est inscrit sur la liste spécifique ; l'inscription de Mme ROCHEVIGNE comme commissaire aux comptes ne suffit pas [V L. 821-13 II, L. 821-26] (0,25 pt).
- **Reprendre les mandats dès 2027** et en réduire le coût : le cabinet VERNÉJOUX est en fonction jusqu'à l'assemblée de 2030 pour les comptes et jusqu'à celle de 2029 pour les informations en matière de durabilité (question 3.2) ; les honoraires du commissaire aux comptes sont en rapport avec les diligences nécessaires et ne peuvent compromettre la qualité des travaux [V code de déontologie art. 12] ; l'économie promise repose précisément sur la reprise des travaux comptables, source d'autorévision [S] (0,25 pt).

**Réponses tolérées**
- La mention, pour l'expert-comptable, du conseil national de l'ordre, sans organisation détaillée.
- La remarque que la société ROCHEVIGNE, faute d'être inscrite comme société de commissaires aux comptes (majorité des droits de vote détenue par des commissaires aux comptes), ne peut pas être désignée, et que seule Mme ROCHEVIGNE pourrait l'être à titre personnel [V L. 821-16 ; S, application].

**Erreurs fréquentes**
- Confondre l'indépendance d'esprit de l'expert-comptable, compatible avec la tenue des comptes, et celle du commissaire aux comptes (`JUR-A03`).
- Décrire l'organisation interne des instances, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 2, 3, 31, 40 | Missions et inscription de l'expert-comptable | [V] | F09 § 1, § 2 |
| C. com. L. 820-1, L. 821-12 à L. 821-26, L. 822-1, L. 822-3, L. 822-4 | Inscriptions, conditions, instances, liste spécifique, organisme tiers indépendant | [V] | F09 § 3.1-3.2, § 4.1, § 4.3 |
| C. com. L. 821-28 IV ; code de déontologie art. 5, 12, 22 | Autorévision ; honoraires | [V] ; application : [S] | F10 § 3, § 4.1, § 5 |

### 3.2 Remplacement voulu par le président (1,5 pt)

- **Durée du mandat (0,25 pt)** : le cabinet a été désigné pour **six exercices**, de 2024 à 2029. Ses fonctions expirent après l'assemblée qui statuera sur les comptes de 2029, en 2030 [V L. 821-44 al. 1]. L'assemblée de juin 2027 ne peut pas le « remplacer » : le Code ne prévoit aucune révocation du commissaire aux comptes par l'assemblée [S, lecture de F09 § 3.7].
- **Relèvement judiciaire (0,5 pt)** : le commissaire aux comptes ne peut être relevé de ses fonctions avant leur terme que **par décision de justice**, en cas de **faute ou d'empêchement**, à la demande notamment du conseil d'administration, d'associés représentant au moins 5 % du capital ou du comité social et économique [V L. 821-50]. Un désaccord sur le traitement des parts des associés sortants n'est ni une faute ni un empêchement : c'est l'exercice normal de la mission, qui oblige le cabinet à demander la correction des comptes. Pour la récusation, le texte écarte d'ailleurs expressément la divergence d'appréciation sur un traitement comptable comme motif [V L. 821-49 ; S, application].
- **Démission (0,5 pt)** : le cabinet ne peut démissionner que pour un **motif légitime** (cessation d'activité, motif personnel impérieux, difficultés auxquelles il n'est pas possible de remédier, événement qui compromet son indépendance). Il ne peut pas démissionner **pour se soustraire à l'émission de son opinion** ni dans des conditions préjudiciables à l'entité, et il informe la H2A de ses motifs [V code de déontologie art. 28]. La pression du président n'est pas un motif légitime : le cabinet doit poursuivre sa mission et émettre son opinion sur les comptes de 2026. Les mêmes règles valent pour la mission sur la durabilité, confiée pour trois exercices (2026 à 2028) : elle expire après l'assemblée de 2029, et le relèvement judiciaire vise aussi cette mission [V L. 821-50].
- **Réponse au président (0,25 pt)** : à l'expiration du mandat, l'assemblée pourra désigner un autre commissaire aux comptes ; le cabinet pourra demander à être entendu [V L. 821-51]. Un successeur ne pourrait d'ailleurs pas tenir aussi la comptabilité (question 3.1).

**Erreurs fréquentes**
- Admettre une révocation par l'assemblée, ou un relèvement pour simple désaccord (`JUR-A01`).
- Développer la procédure judiciaire du relèvement, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-44, L. 821-49, L. 821-50, L. 821-51 | Durée ; récusation ; relèvement ; non-renouvellement | [V] ; application : [S] | F09 § 3.5, § 3.7, § 15 |
| Code de déontologie art. 28 | Démission : motifs légitimes, interdictions | [V] | F09 § 3.7, § 12 |

### 3.3 Demandes de la banque et de la directrice financière (1,5 pt)

- **Cadre (0,25 pt)** : la SCOP n'est pas une entité d'intérêt public. Aucune liste fermée de services interdits ne s'applique : le cabinet ne peut fournir un service autre que la certification que s'il n'en résulte ni **risque d'autorévision** ni atteinte à son indépendance sans mesure de sauvegarde possible [V L. 821-2 IV, L. 821-28 IV ; code de déontologie art. 5, 19].
- **Attestation demandée par la banque (0,5 pt)** : c'est une **prestation** [V L. 821-2 IV]. Le cabinet atteste une information établie par la SCOP, sous sa responsabilité (le montant du capital au 30/06/2027), sans la produire lui-même : aucun risque d'autorévision. Elle prolonge naturellement la mission de certification. Elle est **permise**, sous réserve d'une lettre de mission préalable [V R. 821-195 ; S, application].
- **Calcul des remboursements et échéancier (0,5 pt)** : le cabinet établirait lui-même les sommes dues aux associés sortants, qu'il devra ensuite auditer (dettes envers les associés, réduction du capital), et proposerait une décision de gestion que les statuts confient au conseil. C'est un **risque d'autorévision** sans mesure de sauvegarde possible, et une **immixtion dans la gestion** [V code de déontologie art. 5 II ; L. 821-28 IV ; L. 821-54 I].
- **Réponse à la directrice financière (0,25 pt)** : refus motivé. La SCOP, ou le cabinet ROCHEVIGNE qui tient ses comptes, calcule les sommes (parts annulées × 50 €) et le conseil fixe les dates, dans la limite de deux ans ; le cabinet vérifiera ensuite ces éléments dans le cadre de sa mission.

**Réponses tolérées**
- L'acceptation de l'attestation présentée comme subordonnée à une analyse des risques et à une lettre de mission, sans conclure explicitement à l'absence d'autorévision : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Interdire toute attestation au commissaire aux comptes, ou admettre le calcul au motif qu'il serait « simple » (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-2 IV, L. 821-28 IV, L. 821-54 I ; R. 821-195 | Prestation ; autorévision hors EIP ; non-immixtion ; lettre de mission | [V] ; application : [S] | F10 § 5 ; F09 § 6 ; F11 § 13.2 |
| Code de déontologie art. 5, 19 | Indépendance en réalité et en apparence ; identification des risques | [V] | F10 § 2.1, § 13 |

### 3.4 Certification, attestation et audit contractuel (1,5 pt)

- **Certification des comptes annuels (0,5 pt)** : mission **légale**. Le cabinet certifie, en justifiant de ses appréciations, que les comptes sont **réguliers et sincères et donnent une image fidèle** du résultat, de la situation financière et du patrimoine à la fin de l'exercice. Il exprime une **opinion** après un audit qui procure une **assurance raisonnable**, élevée mais non absolue, que les comptes **pris dans leur ensemble** ne comportent pas d'anomalies significatives [V L. 821-53 al. 1 ; NEP principes § 01, § 08-09]. Le rapport est destiné à l'assemblée générale.
- **Attestation (0,25 pt)** : **prestation** demandée pour un tiers, qui porte sur une **information déterminée** (le capital) à une **date donnée** (30/06/2027), dans les limites fixées par la lettre de mission ; elle ne comporte pas d'opinion sur des comptes [V L. 821-2 IV ; S pour le contenu].
- **Audit des comptes semestriels (0,25 pt)** : **audit contractuel**, confié par contrat à un cabinet choisi par la SCOP. Son objet et son étendue sont ceux du contrat ; il ne vaut pas certification légale. Confié au commissaire aux comptes, ce serait une prestation ; confié à un autre expert-comptable, une mission de révision des comptes [V A. 821-55 § 08 ; ord. 45-2138 art. 2 ; S pour la comparaison].
- **Portée de l'opinion pour la banque (0,5 pt)** : le rapport sur les comptes de 2026 couvre le capital au 31/12/2026 **comme élément des comptes pris dans leur ensemble**, apprécié au regard du seuil de signification. Il ne se prononce pas spécifiquement sur le respect de la clause de 400 000 €, ne couvre pas la situation au 30/06/2027 et ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55 ; S, application]. Une réserve sur le capital (question 3.7) renseignerait néanmoins la banque. Pour le 31/12/2026, la banque peut s'appuyer sur les comptes certifiés ; pour le 30/06/2027, l'attestation ou l'audit contractuel est nécessaire.

**Erreurs fréquentes**
- Présenter la certification comme une garantie de chaque montant des comptes (`JUR-A01`).
- Confondre audit légal et audit contractuel (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-55 ; NEP principes § 01, § 08-09 | Objectif, assurance raisonnable, limites | [V] | F11 § 1.1 |
| C. com. L. 821-2 III-IV ; A. 821-55 § 08 ; ord. 45-2138 art. 2 | Missions et prestations ; audit contractuel ; révision par l'expert-comptable | [V] ; comparaison : [S] | F11 § 1.2, § 13.2 ; F09 § 1 |

### 3.5 Risque du cycle capitaux propres, sélection des éléments et procédures (6,5 pts)

**a. Risque d'anomalies significatives et assertions (3 pts)**
- **Risque inhérent élevé (0,5 pt)** : capital variable qui change chaque mois (742 parts souscrites par prélèvement, 214 en numéraire, 13 sorties et 14 admissions en 2026) ; mouvements qui dépendent d'informations venues d'un tiers, le cabinet ROCHEVIGNE ; **changement** de personnel (absence non remplacée de la responsable administrative de juillet à octobre) ; **incitation** à maintenir un capital élevé, que surveille la banque (clause de 400 000 €) ; président qui juge les départs « sans enjeu pour les comptes » ; sorties de 2025 restées en capital (annexe 3.1) et anomalies relevées lors de l'intervention intermédiaire [V NEP risques § 02 ; S, application].
- **Risque lié au contrôle élevé (0,5 pt)** : aucune procédure de transmission des départs ; registre jamais rapproché du fichier du personnel ; souscriptions comptabilisées d'après le registre sans rapprochement avec la paie ; régularisations demandées en octobre non faites. Le cabinet ne peut pas s'appuyer sur ces contrôles : il met en œuvre des **procédures de substance étendues** [V NEP principes § 11, § 13].
- **Principaux risques et assertions (2 pts ; 0,5 pt par risque rattaché à la bonne assertion et aux faits, dans la limite de 2 pts)** :

| Risque | Assertions | Lien avec les annexes |
|---|---|---|
| Parts des associés sortis maintenues en capital au lieu d'une dette envers eux | Capital : **existence**, **droits et obligations** ; dettes (4567) : **exhaustivité** ; flux de réduction du capital : **exhaustivité** | Sorties non portées au registre ; deux cas à l'intervention intermédiaire ; deux cas en 2025 |
| Souscriptions comptabilisées sans prélèvement correspondant (associés sortis encore inscrits, absences sans salaire) | Souscriptions : **réalité**, **mesure** ; capital : **existence** | État mensuel issu du registre, non rapproché de la paie |
| Souscriptions complémentaires comptabilisées sans encaissement | **Réalité** ; capital : **existence** (capital non versé) | Comptabilisation au vu du seul bulletin signé |
| Remboursements erronés ou mal classés (montant autre que le nominal, associé non sorti, imputation directe sur le capital d'un départ ancien) | **Réalité**, **mesure**, **classification**, **séparation des exercices** | Deux sortants de 2025 remboursés en 2026 sur le capital |
| Affectation du résultat non conforme aux statuts | Réserves et rémunération des parts : **mesure**, **classification** ; présentation : **mesure et évaluation** | Affectation de 2025 décidée en juin 2026 |
| Capital variable mal présenté (dette envers les associés sortants, mouvements de parts, minimum statutaire) | Présentation : **exhaustivité**, **présentation et intelligibilité** | Annexe à vérifier [V PCG art. 832-11] |

**b. Application de l'extrait de la norme relative à la sélection des éléments (1,5 pt)**
- **Méthodes (0,25 pt)** : le commissaire aux comptes choisit, par jugement professionnel et selon les caractéristiques de la population, la sélection de **tous les éléments**, d'**éléments spécifiques** ou les **sondages** [V NEP sélection § 03-04].
- **Méthode de l'intervention intermédiaire (0,25 pt)** : la population, 9 sorties, est constituée d'un **petit nombre d'éléments** : la sélection de tous les éléments était la méthode appropriée [V § 05]. Un sondage sur 4 éléments n'apporte presque aucune économie de travail et laisse 5 sorties sans contrôle.
- **Conclusion tirée (0,5 pt)** : deux anomalies sur quatre éléments. Le cabinet devait en apprécier **la nature et la cause**, puis juger si elles étaient isolées ou **représentatives** de la population [V § 09]. La cause n'est pas l'absence de la responsable administrative : le départ du 31/03/2026 est antérieur à cette absence. Elle tient à l'**absence de toute procédure** de transmission et de rapprochement : la situation est représentative. Le cabinet devait étendre le contrôle à toute la population, revoir à la hausse son évaluation du risque sur l'**exhaustivité** des sorties et conclure que les éléments collectés n'étaient pas suffisants [V § 08]. Qualifier les anomalies d'« oublis isolés » sans analyse de leur cause méconnaît la norme.
- **Méthodes à retenir (0,5 pt)** :
  - **sorties** (13 en 2026) : **tous les éléments**, par le rapprochement exhaustif du registre et du fichier du personnel ;
  - **souscriptions mensuelles** (742 parts) : rapprochement des **douze** totaux mensuels avec les prélèvements de la paie (tous les éléments, au niveau du mois), puis **éléments spécifiques** (associés sortis, admis ou absents dans l'année) et, au besoin, sondage sur les autres associés ;
  - **remboursements** : peu nombreux, **tous les éléments**, ceux de 2026 et ceux de janvier à mars 2027.

**c. Procédures (2 pts ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 2 pts)**
- **Rapprochement exhaustif du registre des associés avec le fichier du personnel** (entrées et sorties de 2026, dates de départ) : exhaustivité des sorties, existence du capital.
- **Rapprochement des souscriptions mensuelles avec les prélèvements des bulletins de paie**, mois par mois : réalité et mesure des souscriptions.
- **Inspection des bulletins de souscription complémentaire et des relevés bancaires** : réalité de l'encaissement, existence du capital versé.
- **Recalcul du capital** : nombre de parts du registre corrigé × 50 €, comparé au compte 1013 et au minimum statutaire de 250 000 € : existence, mesure.
- **Lecture des procès-verbaux** du conseil (admissions, dates de remboursement) et de l'assemblée (affectation du résultat de 2025) : réalité, droits et obligations.
- **Recalcul de l'affectation du résultat de 2025** selon les statuts et contrôle du versement de la rémunération des parts : mesure, classification.
- **Contrôle des remboursements** de 2026 et de janvier à mars 2027 (décisions du conseil, virements, valeur nominale) : réalité, mesure, exhaustivité du compte 4567, séparation des exercices.
- **Demandes de confirmation** adressées aux associés sortis sur les sommes qui leur sont dues : exhaustivité, droits et obligations des dettes [V NEP confirmations § 4-5].
- **Entretiens** avec la responsable administrative et le cabinet ROCHEVIGNE sur le circuit des départs et des souscriptions : compréhension des flux, risque lié au contrôle.
- **Lecture de l'annexe** : capital variable, parts émises et annulées, dette envers les associés sortants : présentation [V PCG art. 832-11].

**Réponses tolérées**
- En a., d'autres risques fondés sur les annexes (dépassement du minimum statutaire, information sur la clause bancaire), s'ils sont rattachés à une assertion.
- En b., le choix d'éléments spécifiques pour les remboursements les plus importants, s'il est justifié.

**Erreurs fréquentes**
- Réciter l'extrait de norme sans l'appliquer aux sorties de la SCOP (`JUR-A06`).
- Confondre réalité (flux) et existence (solde) (`JUR-A01`).
- Proposer des procédures sans objectif ni assertion (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 11-13 ; NEP risques § 02 | Risque inhérent, risque lié au contrôle ; facteurs | [V] ; application : [S] | F11 § 4.1 |
| NEP éléments probants § 9-10 ; NEP confirmations § 4-5 | Assertions ; techniques ; confirmation | [V] | F11 § 4.3, § 6.2-6.3 |
| NEP sélection § 03-09 | Population, méthodes de sélection, analyse des résultats | [V] | F11 § 21 |
| PCG art. 832-11 | Annexe : titres émis et composant le capital | [V] | F11 § 14.2 |

### 3.6 Honoraires et accès aux documents (1,5 pt)

- **Honoraires (0,75 pt)** :
  - Les honoraires sont supportés par l'entité et fixés selon des modalités réglementaires [V L. 821-66 I]. Le programme de travail comporte un nombre d'heures fixé selon le total du bilan augmenté des produits d'exploitation et des produits financiers hors taxes [V D. 821-188] : 6 480 000 + 10 950 000 + 20 000 = **17 450 000 €**, dans la tranche de 15 245 000 à 45 735 000 €, soit **180 à 360 heures**. Les 300 heures du cabinet sont dans la tranche (0,25 pt).
  - Le forfait de 16 100 € correspond à 16 100 / 115 = **140 heures**, 40 heures de moins que le minimum (0,25 pt).
  - Le conseil ne peut pas fixer seul les honoraires : la vacation horaire est fixée **d'un commun accord** avant la mission [V R. 821-192]. Si le nombre d'heures paraît excessif ou insuffisant, la partie la plus diligente saisit le **président de la compagnie régionale** d'une demande de dérogation, avant la mission ; en cas de désaccord sur la rémunération, il tente de concilier les parties [V D. 821-190, R. 821-196]. Le cabinet ne peut accepter des honoraires qui compromettraient la qualité de ses travaux [V code de déontologie art. 12]. La vérification des informations en matière de durabilité, hors barème, relève d'un accord entre les parties [V R. 821-194 ; S pour l'application à une mission volontaire] (0,25 pt).
- **Accès aux documents et aux personnes (0,5 pt)** : le cabinet opère à toute époque les vérifications qu'il juge opportunes et se fait communiquer **sur place toutes les pièces qu'il estime utiles** : c'est lui qui en apprécie l'utilité [V L. 821-60]. Le fichier du personnel est la seule source indépendante du registre pour contrôler l'exhaustivité des sorties ; une liste extraite du registre, source des anomalies, n'est pas probante. Le caractère personnel des données ne peut lui être opposé, le secret n'étant opposable que par les auxiliaires de justice, et le cabinet est lui-même tenu au secret [V L. 821-61 al. 3, L. 821-35 al. 1]. Les **demandes d'information** auprès des personnes de l'entité sont une technique de contrôle : le conseil ne peut pas les refuser [V L. 821-60 ; NEP éléments probants § 10].
- **Maintien du refus (0,25 pt)** : **délit d'obstacle** pour le dirigeant qui refuse la communication sur place des pièces utiles ou fait obstacle aux vérifications (cinq ans, 75 000 €) [V L. 821-6 3°]. Sur l'opinion : **limitation**, qui conduit à une réserve pour limitation si ses incidences sont circonscrites, sinon à une **impossibilité de certifier** [V NEP rapport § 11, § 14]. Si les difficultés ne peuvent être levées, une démission pour motif légitime peut être envisagée, jamais pour éviter d'émettre l'opinion [V code de déontologie art. 28].

**Réponses tolérées**
- Le calcul des heures du forfait sur la vacation de 2026 (16 100 / 110 = 146 heures, 34 heures sous le minimum du barème) : points complets.

**Erreurs fréquentes**
- Présenter le barème comme un tarif en euros, ou admettre qu'un forfait peut être imposé par l'entité (`JUR-A01`).
- Admettre la confidentialité des données du personnel comme motif de refus (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-66 I ; D. 821-188, D. 821-190 ; R. 821-192, R. 821-194, R. 821-196 | Honoraires, barème, dérogation, vacation, conciliation | [V] | F11 § 2 |
| Code de déontologie art. 12, 13, 28 | Honoraires et qualité ; démission | [V] | F10 § 4.1, § 12 ; F09 § 3.7 |
| C. com. L. 821-60, L. 821-61 al. 3, L. 821-35 al. 1, L. 821-6 3° ; NEP rapport § 11, § 14 | Communication ; secret ; obstacle ; limitation | [V] | F09 § 5 ; F11 § 2, § 8.1, § 13.3 |

### 3.7 Anomalies et opinion sur les comptes annuels de 2026 (2 pts)

**Anomalies et caractère significatif (0,75 pt)**
- **Parts des neuf associés sortis (0,5 pt)** : ces associés ont perdu leur qualité à leur départ, et leurs parts sont annulées à cette date, quelle que soit la date du remboursement (statuts et convention de l'annexe 3.2). Leurs parts s'élèvent à 148 + 96 + 132 + 74 + 160 + 118 + 88 + 104 + 140 = **1 060 parts**, soit 1 060 × 50 = **53 000 €**. Le capital est surévalué et les dettes sous-évaluées de 53 000 € ; le résultat n'est pas affecté. 53 000 / 45 000 = **1,18 fois** le seuil de signification : l'anomalie est significative par son montant. Elle l'est aussi par sa **nature** : elle porte sur le capital, retenu par la clause du prêt (le capital corrigé de 418 400 € ne dépasse le minimum fixé par la banque que de 18 400 €, contre 71 400 € dans le projet), et sur les droits de neuf anciens associés. Une anomalie de classement s'apprécie notamment au regard de son incidence sur l'application de clauses de contrats de financement [V NEP caractère significatif § 9 ; NEP anomalies § 14]. L'argument du président (délai statutaire de deux ans, clause respectée) est sans portée : le délai concerne le remboursement, non l'annulation des parts.
- **Affectation du résultat de 2025 (0,25 pt)** : selon les statuts, 360 000 × 50 % = 180 000 € aux réserves, 144 000 € aux salariés, 36 000 € au plus pour les parts. La rémunération décidée (43 200 €, soit 12 %) dépasse le plafond de **7 200 €**, et les réserves impartageables sont inférieures d'autant (7 200 / 45 000 = 0,16 fois le seuil). C'est une irrégularité au regard des statuts, sans effet significatif sur les comptes. Le cabinet la communique au conseil d'administration [V L. 821-63 I], qui peut proposer à l'assemblée de 2027 de rétablir la répartition statutaire [S].

**Écriture de correction (0,5 pt)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 1013 | Capital souscrit - appelé, versé | 53 000 | |
| | 4567 | Associés - Capital à rembourser | | 53 000 |

Libellé : annulation des parts des neuf associés sortis en 2026 et non enregistrés (1 060 parts × 50 €) (écriture X1, équilibrée). Le capital corrigé s'élève à 471 400 − 53 000 = **418 400 €** (8 368 parts), au-dessus du minimum statutaire de 250 000 €.

**Opinion selon la correction (0,75 pt)**
- **La SCOP corrige (écriture X1) (0,25 pt)** : il ne subsiste que les anomalies des autres cycles (8 000 €), sous le seuil et sans caractère significatif par leur nature, et l'irrégularité de l'affectation de 2025 (7 200 €), décision d'assemblée correctement enregistrée, non significative et communiquée au conseil : **certification sans réserve**. Le cabinet les communique au conseil d'administration et obtient une déclaration écrite à laquelle est joint l'état des anomalies non corrigées [V NEP anomalies § 15-17 ; NEP rapport § 08].
- **La SCOP retient la position du président (0,25 pt)** : anomalie significative non corrigée de 53 000 €. Ses incidences sont **clairement circonscrites** : un montant identifié, un reclassement du capital vers les dettes, aucun effet sur le résultat. Une réserve qui la décrit et la quantifie suffit à l'utilisateur, notamment à la banque : **certification avec réserve pour désaccord** [V NEP rapport § 09-10]. Un refus de certifier n'est pas justifié.
- **Parties du rapport (0,25 pt)** : la partie « **Opinion avec réserve** » indique que, sous cette réserve, le cabinet certifie que les comptes sont réguliers et sincères et donnent une image fidèle. La partie « **Fondement de l'opinion avec réserve** » expose le motif et quantifie ses incidences (capital surévalué et dettes envers les associés sortants sous-évaluées de 53 000 €). Les motifs sont communiqués au préalable au conseil d'administration ; le rapport est destiné à l'assemblée générale [V NEP rapport § 06, § 18 ; R. 821-180].

**Réponses tolérées**
- Une écriture de reclassement avec un compte 4567 subdivisé par associé : points complets.
- Le signalement de l'irrégularité de l'affectation de 2025 à la prochaine assemblée générale, sans l'exiger.
- L'omission de l'affectation de 2025 dans l'appréciation de l'opinion, si le candidat l'a qualifiée de non significative : 0,25 pt accordé.

**Erreurs fréquentes**
- Conclure à l'absence d'anomalie parce que le résultat n'est pas affecté, ou parce que la clause bancaire reste respectée (`JUR-A06`).
- Proposer un refus de certifier pour une anomalie de classement circonscrite (`JUR-A02`).
- Écriture sans libellé ou sans numéro de compte (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP caractère significatif § 9 ; NEP anomalies § 14-17 | Montant et nature ; anomalie de classement ; communication ; déclaration écrite | [V] | F11 § 4.2, § 14.1 |
| NEP rapport § 06, § 08-10, § 18 ; R. 821-180 ; L. 821-63 I | Opinions ; parties du rapport ; communication | [V] | F11 § 5, § 8 |
| Statuts (annexe 3.2) | Annulation des parts au départ ; répartition du résultat | Donnée de l'énoncé | — |

### 3.8 Responsabilités et demande de M. DUPEYRAT (2 pts)

**Responsabilité civile (1 pt)**
- **Principe (0,25 pt)** : le commissaire aux comptes est responsable, envers l'entité **et les tiers**, des conséquences dommageables des **fautes et négligences** commises dans l'exercice de sa profession [V L. 821-37 al. 1]. M. DUPEYRAT, ancien associé, agit comme tiers : il doit prouver une faute, un préjudice et un lien de causalité [S].
- **Faute (0,25 pt)** : la certification est une obligation de moyens, fondée sur une assurance raisonnable sur les comptes pris dans leur ensemble [V NEP principes § 08-09]. Les deux sorties non enregistrées de 2025 représentaient 210 × 50 = **10 500 €**, soit **0,25 fois** le seuil de 2025 (42 000 €) : même relevées, elles n'auraient pas modifié l'opinion, et le rapport ne mentionne pas les anomalies non significatives. Le sondage de 3 sorties sur 12 pouvait être discuté au regard de la norme, qui privilégie la sélection de tous les éléments pour une petite population [V NEP sélection § 05], mais ce choix relève du jugement professionnel ; une faute est difficile à établir [S].
- **Préjudice et lien de causalité (0,5 pt)** : les statuts permettent de rembourser les parts **au plus tard deux ans** après le départ, à leur valeur nominale, **sans intérêt** ; M. DUPEYRAT a été remboursé de ses 124 parts (6 200 €) au bout de dix-huit mois, dans ce délai : son droit n'a pas été méconnu. Le retard tient à l'absence de procédure de la SCOP, et le commissaire aux comptes n'a pas à gérer les remboursements, sa mission excluant toute immixtion dans la gestion [V L. 821-54 I]. Le lien entre le rapport et le délai de remboursement n'est pas établi : la demande de 1 500 € est infondée [S]. Le cabinet est couvert par l'assurance obligatoire des commissaires aux comptes [V R. 821-85].

**Responsabilité disciplinaire (0,5 pt)**
- La H2A sanctionne les manquements aux conditions légales d'exercice, la **négligence grave** et les faits contraires à la probité ou à l'honneur, de l'avertissement à la radiation, avec d'éventuelles sanctions pécuniaires [V L. 821-70 I, L. 821-71]. Cette responsabilité est indépendante de l'action civile.
- Le contrôle annoncé porte sur l'**activité du cabinet**, non sur la SCOP ; ce n'est pas une sanction [V L. 820-14]. Les contrôleurs pourront relever la méthode de sélection de 2025 ; le cabinet doit avoir documenté son choix. Une méthode discutable sur un risque non significatif ne caractérise pas une négligence grave [S].

**Responsabilité pénale et demande de copie (0,5 pt)**
- Le délit visé est celui du commissaire aux comptes qui **donne ou confirme des informations mensongères** sur la situation de la personne morale (cinq ans, 75 000 €) [V L. 821-9]. C'est un délit intentionnel [S] : certifier sans réserve des comptes qui comportaient une anomalie non significative, ignorée du cabinet, ne le constitue pas.
- Le cabinet doit **refuser** la copie de son dossier de travail : il est tenu au **secret professionnel** pour les faits et renseignements connus dans l'exercice de sa profession, et aucune levée du secret ne vise un ancien associé. Communiquer le dossier exposerait le cabinet aux peines de la violation du secret [V L. 821-35 al. 1 ; L. 821-7 dernier al.]. Le dossier pourra en revanche être examiné par les contrôleurs de la H2A [S].

**Réponses tolérées**
- Une analyse en termes de responsabilité délictuelle de droit commun envers le tiers, si les trois conditions sont examinées.

**Erreurs fréquentes**
- Confondre les trois responsabilités et leurs sanctions (`JUR-A01`).
- Présenter la certification comme une obligation de résultat, ou le contrôle de la H2A comme une sanction (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-37, L. 821-54 I ; R. 821-85 ; NEP principes § 08-09 ; NEP sélection § 05 | Responsabilité civile ; non-immixtion ; assurance ; assurance raisonnable ; sélection | [V] ; conditions : [S] | F09 § 6, § 7.1, § 13 ; F11 § 1.1, § 21 |
| C. com. L. 821-70 I, L. 821-71, L. 820-14 | Faute disciplinaire ; sanctions ; contrôle d'activité | [V] | F09 § 7.2, § 16 |
| C. com. L. 821-9, L. 821-35 al. 1, L. 821-7 | Informations mensongères ; secret professionnel | [V] ; élément intentionnel : [S] | F09 § 7.3 ; F10 § 7 |

---

### Partie B – Durabilité (12 points)

### 3.9 Norme volontaire ou ESRS (2 pts)

- **Place de la norme volontaire (0,5 pt)** : l'**EFRAG**, conseiller technique de la Commission, prépare les projets d'**ESRS**, que la Commission adopte par actes délégués ; elles fondent l'état de durabilité des entreprises tenues de publier, selon une approche de **double matérialité** [V règl. délégué 2026/1563, consid. 3]. La **norme volontaire** (sigle VSME, pour les PME non cotées) a été adoptée par le règlement délégué (UE) 2026/1560, sur la base d'une recommandation de 2025 ; elle est destinée aux entreprises **non soumises** à l'obligation de publier et s'organise en un **module de base** et un **module complet** [V règl. délégué 2026/1560 art. 2, annexe I ; directive 2013/34 art. 29 quater bis]. La SCOP, non cotée, 74 salariés, non soumise, peut l'appliquer.
- **Étendue et limites (0,75 pt)** :
  - **ESRS** : informations générales publiées quel que soit le résultat de l'analyse ; pour chaque thème **matériel** issu de l'analyse de double matérialité, politiques, actions, indicateurs et cibles ; pas d'information non matérielle, sauf informations supplémentaires signalées comme telles ; image fidèle de tous les impacts, risques et opportunités matériels [V ESRS 1 (2026) § 3, § 24-25, § 29, § 108-109] ;
  - **norme volontaire** : informations des modules retenus, proportionnées à une PME ; elles ne permettent plus de déclarer l'état conforme aux ESRS et ne reposent pas sur l'analyse de double matérialité exigée par celles-ci [S] ;
  - Mme BRÉJAUD a raison sur un point : à compter des exercices ouverts le 01/01/2027, une entreprise tenue de publier ne peut exiger d'une entreprise de sa chaîne de valeur qui ne dépasse pas 1 000 salariés que les points de données énumérés à l'annexe II du règlement qui adopte la norme volontaire [V règl. délégué 2026/1560 art. 1, 3, 4 ; ESRS 1 (2026) § 66]. Elle ne pourrait cependant pas écarter les rejets dans la Glane ou la santé des couturières pour ce motif : ces sujets sont matériels (question 3.10) [S].
- **Conséquence pour la vérification (0,5 pt)** : la mission actuelle porte sur la conformité aux **ESRS** du processus de détermination des informations et des informations publiées [V L. 821-54 II ; LD 2026 § 2]. Avec la norme volontaire, ces axes perdent leur objet : la mission conduite dans les conditions de la certification légale ne peut pas continuer à l'identique. L'assemblée et le cabinet devraient redéfinir l'intervention, par exemple une **prestation** d'assurance sur les informations publiées selon la norme volontaire, avec une nouvelle lettre de mission [V R. 821-195 ; S, application].
- **Conclusion (0,25 pt)** : le choix relève du conseil ; il ne dispense pas la SCOP de traiter les sujets matériels identifiés en 2026 et suppose de modifier la lettre de mission pour 2027 et 2028.

**Réponses tolérées**
- Une recommandation de conserver les ESRS, motivée par les attentes des clientes ou la continuité de la vérification, si l'étendue et les limites des deux référentiels sont présentées.
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences »).

**Erreurs fréquentes**
- Présenter la norme volontaire comme une norme de l'ISSB ou de la GRI, ou développer le calendrier de la réglementation européenne (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règl. délégués 2026/1563 consid. 3 et 2026/1560 art. 1 à 4, annexe I ; directive 2013/34 art. 29 quater bis | EFRAG ; norme volontaire ; modules ; plafond de la chaîne de valeur | [V] | F12 § 1, § 4 |
| ESRS 1 (2026) § 3, § 24-25, § 29, § 66, § 108-109 | Étendue et limites des informations ESRS | [V] | F12 § 2, § 5, § 8 |
| C. com. L. 821-54 II ; LD 2026 § 2 ; R. 821-195 | Objet de l'avis ; prestation | [V] ; application : [S] | F13 § 2 ; F12 § 11 |

### 3.10 Double matérialité et matrice de la direction (4 pts)

**Notions (1,5 pt)**
- **Matérialité d'impact (0,5 pt)** : un sujet est matériel lorsqu'il se rapporte à des **impacts**, positifs ou négatifs, réels ou potentiels, de l'entreprise **sur la population ou l'environnement**, à court, moyen ou long terme, liés à ses activités et à sa chaîne de valeur [V ESRS 1 (2026) § 39]. Un impact négatif réel s'apprécie selon sa **gravité** : **ampleur**, **étendue** et **caractère irrémédiable** ; un impact potentiel, selon sa gravité et sa **probabilité** [V § 40]. Les actions qui ne sont pas encore mises en œuvre ne sont pas prises en compte [V § 43].
- **Matérialité financière (0,5 pt)** : un sujet est matériel s'il a, ou peut raisonnablement avoir, des **effets financiers** matériels sur l'entreprise (situation financière, performance, flux de trésorerie, accès au financement, coût du capital), appréciés selon leur **probabilité** et leur **ampleur** [V § 47, § 50]. Ces effets peuvent naître des impacts de l'entreprise et de ses **dépendances** à l'égard de ressources naturelles, humaines ou sociales [V § 48].
- **Règle (0,5 pt)** : un sujet est matériel s'il l'est selon la matérialité d'impact, selon la matérialité financière **ou selon les deux** ; un impact peut être matériel **exclusivement** en termes d'impact [V ESRS 1 (2023) § 28 ; ESRS 1 (2026) § 35]. Les deux dimensions sont évaluées, l'évaluation des impacts étant en général le point de départ [V § 36]. Le dialogue avec les **parties prenantes affectées** est une contribution essentielle à l'évaluation des impacts [V § 42].

**Analyse du cas (1,5 pt)**
- **Erreur de méthode (0,25 pt)** : la direction ne note que les effets financiers ; elle n'évalue **aucun impact**. Le critère « sans effet sur les comptes » est celui de la matérialité financière, et encore entendu trop étroitement. Les notes ont été attribuées après des entretiens avec les seuls acheteurs des clientes, sans les parties prenantes affectées.
- **Rejets dans la Glane (0,5 pt)** : **impact négatif réel** sur l'environnement. Ampleur : trois analyses sur quatre au-dessus de la teneur maximale fixée par l'arrêté préfectoral ; étendue : environ quatre kilomètres de rivière, dans une zone de frayères ; caractère irrémédiable : accumulation dans les sédiments, dont la dépollution demanderait des années. La gravité rend l'impact **matériel**. Le remplacement de la station, non engagé, ne peut pas l'atténuer dans l'analyse [V § 40, § 43 ; S, application]. Le sujet comporte aussi un **risque** de sanction ou de travaux imposés, dont la probabilité et l'ampleur sont à évaluer.
- **Troubles musculosquelettiques des couturières (0,5 pt)** : **impact négatif réel** sur le personnel de l'entreprise. Ampleur : douze maladies professionnelles reconnues en trois ans, en hausse, deux inaptitudes définitives ; étendue : 34 couturières exposées ; caractère irrémédiable : inaptitudes définitives. Le sujet est **matériel** en impact, comme le confirme l'avis du CSE. Il comporte aussi un **risque** financier né d'une **dépendance** à une ressource humaine rare : dix-huit mois de formation, recrutement difficile, capacité de production menacée [V § 48 ; S, application].
- **Sujets retenus (0,25 pt)** : l'approvisionnement en peaux (risque de prix et de disponibilité, dépendance à une ressource) et les exigences des trois clientes (risque de perte de 81 % des débouchés, mais aussi **opportunité** pour une ganterie capable de prouver la traçabilité de ses peaux) sont justement retenus en matérialité financière ; leur dimension d'impact (bien-être animal dans les élevages de la chaîne de valeur amont) reste à évaluer.

**Corrections à apporter (1 pt ; 0,25 pt par correction justifiée, dans la limite de 1 pt)**
- Ajouter une **évaluation de l'impact** de chaque sujet, selon des critères documentés (ampleur, étendue, caractère irrémédiable, probabilité pour les impacts potentiels) et des seuils appropriés, chaque dimension suffisant à elle seule à rendre un sujet matériel, sans compensation entre impacts positifs et négatifs [V § 35, § 37, § 44].
- **Retenir comme matériels** les rejets de l'atelier de teinture et la santé et la sécurité des couturières, et publier sur ces sujets les informations requises.
- **Associer les parties prenantes affectées** : couturières et CSE, syndicat de rivière, riverains et pêcheurs [V § 42].
- **Réévaluer la matérialité financière** de ces deux sujets (risque réglementaire, dépendance aux compétences) et ne pas tenir compte des actions non engagées [V § 43, § 48].
- Décrire fidèlement le processus révisé dans l'état de durabilité.

**Réponses tolérées**
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences », « parties intéressées »).
- Le classement des troubles musculosquelettiques en impact et en risque, ou en impact seulement, s'il est justifié.

**Erreurs fréquentes**
- Exiger qu'un sujet soit matériel selon les deux dimensions à la fois (`JUR-A01`).
- Proposer de nouvelles mesures chiffrées ou des cibles, ce qui n'est pas demandé (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 35-37, § 39-40, § 42-44 | Matérialité d'impact ; gravité ; parties prenantes ; actions ; § 44 : pas de compensation entre impacts positifs et négatifs | [V] ; application : [S] | F12 § 6.2, § 15 |
| ESRS 1 (2026) § 47-50 ; ESRS 1 (2023) § 28 | Matérialité financière ; dépendances ; règle « ou les deux » | [V] | F12 § 6.1-6.2, § 15 |

### 3.11 Mission du cabinet et procédures sur le processus (4,5 pts)

**a. Objectifs, assurance, axes et vérification du processus (2,5 pts)**
- **Objectifs (0,5 pt)** : le cabinet émet un **avis** sur la conformité aux ESRS du **processus** mis en œuvre pour déterminer les informations publiées et sur la conformité des **informations** publiées [V L. 821-54 II ; LD 2026 § 2]. La mission est volontaire, conduite dans les conditions de la certification légale (hypothèse) ; le rapport est destiné à l'assemblée générale. Elle ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].
- **Assurance limitée (0,5 pt)** : vérifications moindres en **nature, étendue et durée** que pour une assurance raisonnable ; conclusion sous une **forme négative** : le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes [V LD 2026, « Niveau d'assurance »]. La certification des comptes procure, elle, une assurance raisonnable, exprimée sous une forme positive [V NEP principes § 08 ; LD 2026, « Niveau d'assurance »].
- **Axes applicables (0,5 pt)** : **axe 1**, le processus de détermination des informations, et **axe 2**, les informations publiées. L'axe relatif aux exigences de l'article 8 du règlement (UE) 2020/852 (taxonomie) est **sans objet** : il ne vise que les entreprises soumises à l'obligation de publier. L'axe relatif au **balisage** n'est pas exigible tant que les règles de balisage ne sont pas adoptées [V LD 2026 § 2, § 10 ; règl. 2020/852 art. 8 § 1 ; S, application].
- **Contenu de l'axe 1 (1 pt)** :
  - le cabinet vérifie que la SCOP a **défini, mis en œuvre et décrit** un processus qui lui permet d'identifier et d'évaluer ses impacts, risques et opportunités : identification des **parties prenantes** (affectées et utilisateurs) ; **matérialité d'impact** en trois étapes (compréhension du contexte, identification des impacts, y compris par le dialogue avec les parties prenantes, évaluation et seuils) ; **matérialité financière** (risques et opportunités, dépendances, probabilité, ampleur, seuils) [V LD 2026 § 7.1] (0,5 pt) ;
  - il n'a pas à refaire l'analyse, mais à évaluer si la démarche prévue par les ESRS a été suivie [V LD 2026 § 7] (0,25 pt) ;
  - **consultation du CSE** : pour une entité soumise, la vérification porte sur la consultation du CSE sur les informations en matière de durabilité lors de l'une des consultations récurrentes [V LD 2026 § 7.3]. Pour la SCOP, qui publie volontairement, cette consultation n'est pas une obligation légale : elle découle de l'accord d'entreprise, et la lettre de mission l'inclut dans la vérification [V F12 § 11 ; S, application]. Le procès-verbal du 25/02/2027 l'établit (0,25 pt).

**b. Procédures sur le processus de double matérialité (2 pts ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 2 pts)**
- **Prise de connaissance** des activités (atelier de teinture, couture), de la chaîne de valeur (mégisseries, élevages, clientes) et des parties prenantes : apprécier si la liste des sujets est complète.
- **Entretiens** avec le président, la directrice financière, le responsable de l'atelier de teinture et des membres du CSE : comprendre la méthode, les notes et les motifs d'exclusion.
- **Revue de la documentation des notations et du seuil** de 3 : critères, auteurs, absence d'évaluation des impacts.
- **Rapprochement avec les analyses des rejets** (rapports du laboratoire agréé, arrêté préfectoral, rapport du syndicat de rivière) : gravité de l'impact écarté.
- **Rapprochement avec les données de la paie et du service de santé au travail** (arrêts, maladies professionnelles reconnues, inaptitudes) : gravité de l'impact sur les couturières.
- **Inspection du procès-verbal du CSE** du 25/02/2027 et de son avis : réalité de la consultation prévue par l'accord, prise en compte des parties prenantes affectées.
- **Échanges avec l'équipe qui certifie les comptes** : cohérence des effets financiers retenus avec les comptes (dépendance aux clientes, coûts des peaux), connaissance des risques réglementaires [V LD 2026 § 3.2].
- **Lecture de la description du processus** dans le projet d'état : description fidèle des parties prenantes consultées, des critères et des seuils.
- **Lettre d'affirmation** de la direction et **communication** des anomalies au conseil d'administration [V LD 2026 § 4, § 14].

**Erreurs fréquentes**
- Décrire les axes d'une entité soumise sans les adapter à la publication volontaire, ou retenir l'axe relatif à la taxonomie (`JUR-A05`).
- Présenter l'assurance limitée comme une garantie de conformité (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; LD 2026 § 2, § 10, « Niveau d'assurance » | Objectifs, axes, assurance limitée | [V] ; application à une mission volontaire : [S] | F13 § 2 ; F12 § 11 |
| LD 2026 § 7, § 7.1.1-7.1.3, § 7.3 | Vérification du processus ; parties prenantes ; matérialités ; CSE | [V] | F13 § 8 |
| LD 2026 § 3.2, § 4, § 14 | Échanges avec les commissaires aux comptes ; lettre d'affirmation ; communication | [V] ; procédures : [S] | F13 § 3 |

### 3.12 Avis sur le processus et incidence sur le rapport (1,5 pt)

- **La direction corrige son analyse (0,5 pt)** : elle évalue les impacts, retient les rejets et la santé des couturières et décrit le processus révisé ; aucune erreur, omission ou incohérence importante ne subsiste : **avis de conformité** sur le processus [V LD 2026 § 17]. Le cabinet peut présenter l'analyse de double matérialité parmi les éléments ayant fait l'objet d'une attention particulière.
- **La direction maintient son analyse (0,5 pt)** : le processus ignore l'une des deux dimensions de la double matérialité, pour tous les sujets ; c'est une erreur non corrigée d'une importance telle qu'elle remet en cause la conformité du processus aux ESRS. Ses incidences ne sont **pas clairement circonscrites** : faute d'évaluation des impacts, on ne sait pas quels autres sujets seraient matériels. **Avis de non-conformité, motivé** [V F13 § 4.3 ; S, qualification]. Ce n'est pas une impossibilité : aucune limitation n'empêche les vérifications.
- **Incidence sur les autres parties du rapport (0,5 pt)** : le rapport comporte une partie par axe [V LD 2026 § 17]. Dans la partie sur les **informations**, l'absence d'informations sur deux sujets matériels est une omission ; le cabinet en apprécie l'importance et le caractère circonscrit pour émettre un avis de conformité avec réserve ou de non-conformité [S]. Les axes relatifs à la taxonomie et au balisage ne donnent lieu à aucun avis.

**Réponses tolérées**
- Un avis de conformité assorti d'une réserve motivée dans le second cas, si le candidat circonscrit l'erreur aux deux sujets écartés et motive la suffisance de la réserve : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Conclure à une impossibilité d'émettre un avis en l'absence de limitation, ou remplacer la réserve par une observation (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 | Avis, réserve, non-conformité, éléments d'attention particulière, structure par axe | [V] ; qualification : [S] | F13 § 4.1-4.4 |
