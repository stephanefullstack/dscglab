# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 10

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 10/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex25_consolidation_anc_composants_contrat` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.7 | `exercices/ex26_fusion_soulte_deficits` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.10 | `exercices/ex27_audit_achats_stocks_snc_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 1,5 |
| 1.2 a IASB, IFRIC, EFRAG et adoption | `2.1.a` Cadre conceptuel de l'IASB et normalisateurs | 1 |
| 1.2 b Cadre conceptuel et amortissements dérogatoires | `2.1.a` Cadre conceptuel de l'IASB et normalisateurs ; `2.2.b` Élimination des écritures fiscales | 1,5 |
| 1.3 Manuel, liasse et processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.4 Périmètre et méthodes | `2.1.c` Périmètre ; `2.1.d` Conséquences du référentiel et des méthodes | 2 |
| 1.5 a Amortissements dérogatoires | `2.2.b` Élimination des écritures fiscales | 3 |
| 1.5 b Approche par composants | `2.2.c` Homogénéisation, thèmes communs | 3 |
| 1.5 c Impôts différés de la ligne de sciage | `2.2.b` Élimination des écritures fiscales ; `2.2.c` Homogénéisation, thèmes communs | 1 |
| 1.6 Contrat d'agencement des HAUTES-FEIGNES | `2.2.c` Homogénéisation, thèmes communs | 5 |
| 1.7 a Ventes de bois scié et marge interne | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.7 b Comptes réciproques et règlement en transit | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.7 c Dividende de MORTELAN | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.8 a Actif net réévalué de FORTANGE | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.8 b Frais, coût d'acquisition et écart d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 2 |
| 1.8 c Amortissement de l'écart et écritures | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.9 a Partage des capitaux propres de FORTANGE et de MORTELAN | `2.2.h` Partage des capitaux propres | 3 |
| 1.9 b Mise en équivalence de PELLANDE | `2.2.h` Partage des capitaux propres | 1,5 |
| 1.9 c Écritures d'élimination des titres et de mise en équivalence | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.10 a Bilan consolidé | `2.3.a` Documents de synthèse consolidés | 5 |
| 1.10 b Annexe consolidée et différence avec les IFRS | `2.3.a` Documents de synthèse consolidés ; `2.1.d` Conséquences du référentiel et des méthodes | 2 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires ; `EA` = écart d'acquisition ; `AMO_EA` = amortissements de l'écart d'acquisition ; `DOT_EA` = ligne « dotations aux amortissements, dépréciations et reprises des écarts d'acquisition » du compte de résultat ; `TME` = titres mis en équivalence ; `QP_MEE` = résultat net lié aux entités mises en équivalence ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.VORMANCE` : titres détenus par VORMANCE Participations ; `RSV.SCIERIE` : réserves de VORMANCE Scierie).

---

### 1.1 Obligation d'établir des comptes consolidés et référentiel (1,5 pt)

**Principe (0,5 pt).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. VORMANCE Participations, société à responsabilité limitée, est une société commerciale. Elle détient la majorité des droits de vote de VORMANCE Scierie (100 %), de FORTANGE (80 %) et de MORTELAN (70 %) : elle les contrôle de manière exclusive [V ANC art. 211-3, p. 12-13 ; F03 § 2]. Elle entre dans le champ de l'obligation.

**Exemptions (0,5 pt).**
- *Société elle-même contrôlée* (L. 233-17, 1°) : ses parts appartiennent à sept personnes physiques et aucune entité ne l'inclut dans des comptes consolidés ; l'exemption ne joue pas [V L. 233-17 ; F03 § 1.1].
- *Ensemble qui n'est pas un « grand groupe »* (L. 233-17, 2°) : un grand groupe dépasse, à la clôture, deux des trois seuils suivants : total du bilan 30 000 000 €, chiffre d'affaires net 60 000 000 €, 250 salariés en moyenne ; les seuils sont réputés franchis à la clôture de **deux exercices consécutifs** [V L. 230-2, 3° ; D. 230-2, 2° et dernier alinéa ; F03 § 1.1]. Les trois seuils sont dépassés au 31/12/2025 (61,2 M€, 86,4 M€, 438 salariés) et au 31/12/2026 (67,48 M€, 94,7 M€, 460 salariés) : l'ensemble est un grand groupe. L'exemption est écartée ; aucune société de l'ensemble ne relève d'ailleurs des catégories (établissements financiers, assureurs, entités faisant appel à la générosité du public) pour lesquelles elle est refusée en tout état de cause [V L. 123-16-2 ; F03 § 1.1].

**Référentiel et option (0,5 pt).** Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que pour les sociétés dont des titres sont admis aux négociations sur un marché réglementé d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Aucun titre de VORMANCE Participations n'est admis sur un marché : elle applique le règlement ANC n° 2020-01. Elle **pourrait** toutefois opter pour l'établissement de ses comptes consolidés selon les IFRS adoptées [V C. com. L. 233-24 ; F03 § 1.2] ; elle ne l'a jamais fait.

---

### 1.2 Demande du groupe KRALLMÜHL (2,5 pts)

#### a. IASB, IFRIC, EFRAG et normes applicables (1 pt)

- **IASB** (0,25) : groupe indépendant d'experts, au sein de l'IFRS Foundation, organisme sans but lucratif ; ses membres élaborent et publient les normes IFRS ; il approuve les interprétations [V page « International Accounting Standards Board », ifrs.org ; F03 § 7.2].
- **IFRS Interpretations Committee (IFRIC)** (0,25) : il élabore les interprétations des normes IFRS, qui en précisent l'application, et les soumet à l'approbation de l'IASB [V même source ; F03 § 7.2].
- **EFRAG et adoption** (0,5) : l'EFRAG veille à la prise en compte des positions européennes dans les travaux de l'IASB et conseille la Commission européenne sur la conformité des normes nouvelles ou modifiées aux critères du règlement IAS, dont l'intérêt public européen [V page « Financial reporting », efrag.org ; F03 § 7.2]. Une norme ne s'applique dans l'Union qu'après son **adoption par un règlement de la Commission** (par exemple le règlement (UE) 2023/1803) [V intitulé du règlement (UE) 2023/1803 ; F03 § 7.2]. Le groupe appliquerait donc les **IFRS adoptées par l'Union européenne**, comme KRALLMÜHL ; pour l'exercice 2026, la présentation suivrait IAS 1, IFRS 18 ne s'appliquant qu'aux exercices ouverts à compter du 01/01/2027, sauf application anticipée [V règlement (UE) 2026/338, art. 2 ; F14 § 0].

#### b. Cadre conceptuel et amortissements dérogatoires (1,5 pt)

- **Objectif et utilisateurs (0,5 pt)** : selon le cadre conceptuel, l'information financière à usage général doit être **utile aux investisseurs, prêteurs et autres créanciers, actuels et potentiels**, pour leurs décisions relatives à la fourniture de ressources à l'entité [S présentation du cadre de 2018 ; F03 § 7.2]. KRALLMÜHL, qui envisage de souscrire à une augmentation de capital, est un **investisseur potentiel** : elle veut apprécier la performance et la situation du groupe et les comparer à celles d'autres groupes, d'où sa demande d'une information établie selon les mêmes normes que les siennes (comparabilité, caractéristique qualitative auxiliaire de l'information utile [S ; F03 § 7.2]).
- **Les amortissements dérogatoires ne sont pas une dette (0,5 pt)** : un passif est une obligation actuelle de l'entité résultant d'événements passés et dont l'extinction devrait se traduire par une sortie de ressources représentatives d'avantages économiques [V IAS 37 § 10 ; F03 § 8] ; le cadre conceptuel de 2018 le définit comme une obligation actuelle de transférer une ressource économique du fait d'événements passés [S ; F03 § 8]. La scierie ne doit rien à personne au titre des 478 500 € : ce n'est pas un passif.
- **Ni une dépréciation (0,25 pt)** : l'usure de la ligne est déjà traduite par l'amortissement comptable. Le PCG précise que les amortissements dérogatoires ne correspondent pas à l'objet normal d'un amortissement ou d'une dépréciation et qu'ils sont comptabilisés au sein des provisions réglementées [V PCG art. 214-8, p. 24], constituées en application de textes particuliers [V PCG art. 313-1, p. 32] et présentées dans les **capitaux propres** du bilan individuel [V PCG art. 821-1, p. 96-98]. Dans les comptes individuels, ils sont donc une part des capitaux propres que seule la législation fiscale fait apparaître. Les comptes consolidés éliminent l'incidence des écritures passées pour la seule application des législations fiscales [V ANC art. 272-1 et IR4, p. 53 ; F04 R1] ; les IFRS, qui ne connaissent pas les provisions réglementées, conduisent à la même élimination [V F04 R1].
- **L'avantage fiscal dans les comptes consolidés (0,25 pt)** : la déduction anticipée ne fait que **différer** l'impôt ; à mesure que l'amortissement fiscal deviendra inférieur à l'amortissement comptable, la scierie paiera davantage d'impôt. Cette obligation, née d'un événement passé (la déduction déjà obtenue), est un **passif d'impôt différé** : 478 500 × 25 % = **119 625 €** [V ANC art. 272-8, p. 57 ; F04 R1]. Le solde, 358 875 €, figure dans les capitaux propres consolidés (réserves et résultat, voir 1.5 a).

---

### 1.3 Manuel, liasse et processus de consolidation (2 pts)

**Rôle des documents (0,5 pt).**
- Le **manuel de consolidation** fixe les règles communes du groupe : périmètre et méthodes, méthodes comptables à appliquer de manière homogène (composants, avancement, élimination des provisions réglementées, impôts différés), traitement de l'écart d'acquisition, plan de comptes et calendrier. Il permet d'appliquer les méthodes du groupe à toutes les entités [V ANC art. 271-5, p. 52 ; F04 § 1] (0,25).
- La **liasse de consolidation** est le dossier que chaque société remplit selon un format commun : comptes individuels, informations nécessaires aux retraitements (tableaux des immobilisations, contrats en cours) et détail des opérations avec les autres sociétés du groupe. Elle fournit au service consolidation des données homogènes et complètes (0,25).

**Anomalies du calendrier (1 pt).**
- Les **retraitements** (03/02) sont placés après le cumul et après le partage. L'intégration globale cumule les comptes des entités consolidées **après retraitements** [V ANC art. 221-2, p. 18-19 ; F03 § 3], et le partage porte sur les capitaux propres retraités, y compris les écarts d'évaluation de FORTANGE et le contrat de MORTELAN [V art. 232-1, p. 24 ; F05 § 3]. Ils doivent précéder le cumul et le partage (0,5).
- Le **rapprochement des réciproques** (08/02) intervient trop tard et après l'élimination des titres : il doit suivre la réception des liasses, pour que les filiales expliquent et corrigent les écarts (ici le virement de 120 000 € en transit) avant le cumul. L'**élimination des opérations internes** doit, elle aussi, précéder le partage : la marge interne et les dividendes modifient les réserves et les résultats à répartir (0,5).

**Ordre corrigé (0,5 pt).**

| Ordre | Étape | Travaux du dossier |
|---|---|---|
| 1 | Instructions de clôture et manuel à jour (08/01) | 1.4 (périmètre) |
| 2 | Réception des liasses (22/01) | — |
| 3 | Rapprochement des comptes réciproques et correction des écarts | 1.7 b |
| 4 | Retraitements selon le manuel, évaluation des actifs et passifs de FORTANGE | 1.5, 1.6, 1.8 a |
| 5 | Cumul des comptes retraités des sociétés intégrées globalement | annexe 1.10 |
| 6 | Élimination des opérations internes et des dividendes | 1.7 |
| 7 | Élimination des titres, écart d'acquisition, partage, mise en équivalence | 1.8 b et c, 1.9 |
| 8 | Bilan, compte de résultat et annexe consolidés, puis arrêté par la gérance (12/03) | 1.10 |

---

### 1.4 Périmètre et méthodes (2 pts)

**Tableau (1 pt : filiales 0,5 ; PELLANDE 0,5)**

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt |
|---|---|---|---|---|
| VORMANCE Participations | — | Société consolidante | — | 100 % |
| VORMANCE Scierie | 100 % | Exclusif | Intégration globale | 100 % |
| FORTANGE | 80 % | Exclusif | Intégration globale | 80 % (minoritaires 20 %) |
| MORTELAN | 70 % | Exclusif | Intégration globale | 70 % (minoritaires 30 %) |
| PELLANDE | 30 % (par VORMANCE Scierie) | Influence notable | Mise en équivalence | 100 % × 30 % = 30 % |

**Justification pour PELLANDE (0,5 pt).** Les droits de vote détenus par VORMANCE Scierie, contrôlée exclusivement par la société consolidante, s'ajoutent à ceux de la consolidante [V ANC art. 211-6, p. 14 ; F03 § 2] : le groupe dispose de 30 % des voix de PELLANDE, plus de 20 % : l'influence notable est présumée [V art. 211-5, p. 13]. Il n'y a pas de contrôle exclusif (ni majorité des voix, ni désignation de la majorité du conseil : deux membres sur six) ni de contrôle conjoint (aucun accord prévoyant l'unanimité) [V art. 211-3 et 211-4, p. 12-13]. Les indices confirment l'influence notable : représentation au conseil de direction, opérations importantes (70 % des sciures transformées), mise à disposition d'un directeur technique [V art. 211-5, p. 13]. D'où la mise en équivalence [V art. 221-1, p. 18 ; F03 § 3]. Le pourcentage d'intérêt est le produit des pourcentages de capital le long de la chaîne [S ; F03 § 4.1].

**Présentation (0,5 pt).** Les actifs, passifs, produits et charges de PELLANDE ne sont pas cumulés : ses titres sont remplacés par la quote-part du groupe dans ses capitaux propres, présentée à l'actif immobilisé sur la ligne « titres mis en équivalence » (594 000 €, voir 1.9 b), et sa quote-part de résultat figure sur la ligne « résultat net lié aux entités mises en équivalence », après le résultat net des entités intégrées (90 000 €) [V art. 221-4, p. 19 ; art. 281-1 et 281-2, p. 66-67 ; F14 § 1.2-1.3]. Les ventes de sciures (620 000 €) et la créance de 55 000 € de la scierie sur PELLANDE restent dans les comptes consolidés : seules les opérations entre entités intégrées globalement sont éliminées en totalité ; à l'égard d'une entité mise en équivalence, seuls les résultats internes sont éliminés, à hauteur du pourcentage détenu [V art. 262-4, p. 49-50 ; F04 R14], et il n'y en a pas ici (aucune sciure en stock chez PELLANDE).

---

### 1.5 Ligne de sciage de VORMANCE Scierie (7 pts)

#### a. Élimination des amortissements dérogatoires (3 pts)

**Justification (0,75 pt).** L'incidence des écritures passées pour la seule application des législations fiscales est éliminée ; les amortissements dérogatoires en sont l'exemple type [V ANC art. 272-1 et IR4, p. 53 ; F04 R1], et le manuel le rappelle. L'excédent de l'amortissement fiscal dégressif sur l'amortissement comptable n'a pas d'autre objet que de différer l'impôt (1.2 b). Les dotations ayant été déduites, la base fiscale de la ligne est inférieure à sa valeur dans les comptes consolidés : la différence temporaire est imposable, d'où un **impôt différé passif** [V art. 272-8, p. 57 ; F04 R1].

**Tableau des incidences (1 pt)**

| | 2025 (ouverture, réserves) | 2026 (résultat) | Clôture (31/12/2026) |
|---|---:|---:|---:|
| Amortissement fiscal dégressif | 540 000 | 418 500 | 958 500 |
| Amortissement comptable linéaire (comptes individuels) | 240 000 | 240 000 | 480 000 |
| **Amortissements dérogatoires éliminés** | **300 000** | **178 500** | **478 500** |
| Impôt différé passif (25 %) | – 75 000 | – 44 625 | **– 119 625** |
| **Net** | **225 000** (réserves) | **133 875** (résultat) | 358 875 |

(Montants des dotations : 0,25 ; répartition réserves / résultat : 0,5 ; impôt différé : 0,25.)

**C1 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 145 Amortissements dérogatoires | 478 500 | |
| RSV.SCIERIE Réserves VORMANCE Scierie | | 225 000 |
| RST.SCIERIE Résultat VORMANCE Scierie | | 133 875 |
| IDP Impôt différé passif | | 119 625 |
| *Élimination des amortissements dérogatoires* | **478 500** | **478 500** |

**C1R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CH_ID Charge d'impôt différé | 44 625 | |
| RES_CR Résultat | 133 875 | |
| 68725 Dotations aux provisions réglementées – amortissements dérogatoires | | 178 500 |
| *Annulation de la dotation de 2026* | **178 500** | **178 500** |

Le compte 68725 relève des dotations exceptionnelles (compte 687) [V liste des comptes du PCG 2026] : l'élimination augmente le résultat exceptionnel consolidé.

#### b. Approche par composants (3 pts)

**Principe (0,5 pt).** Les modes et durées d'amortissement sont homogénéisés selon les méthodes du groupe [V ANC art. 271-5, p. 52 ; F04 § 1 et R3]. La scierie a retenu une durée d'utilisation commune de 10 ans pour tous les éléments de la ligne. Le manuel fixe des durées différentes pour trois composants : le plan d'amortissement de la scierie est homogénéisé avec celui du groupe. Les amortissements cumulés des exercices antérieurs corrigent les réserves, la dotation de 2026 le résultat ; l'impôt différé porte sur l'écart de valeur nette, la base fiscale suivant les comptes individuels [V art. 272-8, p. 57 ; F04 R3].

**Amortissements par composants (1 pt)**

| Composant | Valeur | Durée | Dotation annuelle (2025 et 2026) |
|---|---:|---|---:|
| Bâti, convoyeurs et charpente métallique | 1 200 000 | 15 ans | 80 000 |
| Scies et têtes de sciage | 900 000 | 6 ans | 150 000 |
| Scanner optique et système de pilotage | 300 000 | 5 ans | 60 000 |
| **Total** | **2 400 000** | | **290 000** |

Dotation des comptes individuels : 2 400 000 / 10 = 240 000 € ; écart annuel : 290 000 – 240 000 = **50 000 €** de dotation supplémentaire.

**Tableau des incidences (0,5 pt)**

| | 2025 (réserves) | 2026 (résultat) | Cumul au 31/12/2026 |
|---|---:|---:|---:|
| Amortissements par composants | 290 000 | 290 000 | 580 000 |
| Amortissements des comptes individuels | 240 000 | 240 000 | 480 000 |
| **Écart (dotation supplémentaire)** | **– 50 000** | **– 50 000** | **– 100 000** |
| Impôt différé actif (25 %) | + 12 500 | + 12 500 | + 25 000 |
| **Net** | **– 37 500** | **– 37 500** | – 75 000 |

**C2 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RSV.SCIERIE Réserves VORMANCE Scierie | 37 500 | |
| RST.SCIERIE Résultat VORMANCE Scierie | 37 500 | |
| IDA Impôt différé actif | 25 000 | |
| 2815 Amortissements des installations, matériel et outillage industriels | | 100 000 |
| *Amortissement de la ligne par composants* | **100 000** | **100 000** |

**C2R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 68112 Dotations aux amortissements des immobilisations corporelles | 50 000 | |
| CH_ID Produit d'impôt différé | | 12 500 |
| RES_CR Résultat | | 37 500 |
| *Complément de dotation de 2026* | **50 000** | **50 000** |

La valeur brute (2 400 000 €) ne change pas : elle est seulement ventilée entre les trois composants dans le fichier des immobilisations du groupe.

#### c. Impôts différés de la ligne de sciage (1 pt)

- **Amortissements dérogatoires : passif (0,25 pt)**. Leur élimination porte la valeur consolidée au-dessus de la base fiscale, qui a déjà supporté l'amortissement dégressif : l'impôt sera payé plus tard, d'où un impôt différé passif de 119 625 €.
- **Composants : actif (0,25 pt)**. La dotation consolidée dépasse la dotation des comptes individuels, que suit la base fiscale : la valeur consolidée est réduite de 100 000 € sans réduction de la base fiscale ; ces amortissements seront déduits plus tard, d'où un impôt différé actif de 25 000 €.
- **Rapprochement au 31/12/2026 (0,5 pt)** :

| | Montant |
|---|---:|
| Valeur nette consolidée : 2 400 000 – 580 000 | 1 820 000 |
| Base fiscale : 2 400 000 – 958 500 | 1 441 500 |
| **Différence temporaire imposable** | **378 500** = 478 500 – 100 000 |
| Impôt différé net (25 %) | **94 625** = 119 625 – 25 000 |

---

### 1.6 Contrat d'agencement de l'hôtel des HAUTES-FEIGNES (5 pts)

**Justification (0,75 pt).** Le PCG permet la méthode à l'achèvement ou à l'avancement [V PCG art. 622-2, p. 63 ; F04 R9] ; le manuel retient l'avancement, à appliquer de manière homogène [V ANC art. 271-5, p. 52 ; F04 R9]. L'avancement suppose une estimation fiable du résultat à terminaison, appréciée sur trois critères : produits du contrat clairement identifiés, coûts imputables clairement identifiés, et existence d'outils de suivi permettant de mesurer l'avancement [V PCG art. 622-5, p. 63 ; F04 R9] ; l'annexe 1.6 les déclare réunis. Le contrat est bénéficiaire : aucune provision pour perte à terminaison n'est en jeu [V PCG art. 622-6 ; F04 R9]. Le résultat fiscal suivant l'achèvement, le résultat dégagé en consolidation sera imposé en 2027 : **impôt différé passif** [V ANC art. 272-8, p. 57 ; F04 R9].

**Calculs (1,25 pt)**

Résultat à terminaison : 1 800 000 – 1 440 000 = **360 000 €** (marge de 20 %).

| | 2025 | 2026 (cumul) | 2026 (exercice) |
|---|---:|---:|---:|
| Coûts engagés cumulés | 432 000 | 1 152 000 | 720 000 |
| Avancement (coûts engagés / 1 440 000) | **30 %** | **80 %** | |
| Chiffre d'affaires à l'avancement (1 800 000 × %) | 540 000 | 1 440 000 | **900 000** |
| Résultat à l'avancement (360 000 × %) | **108 000** | 288 000 | **180 000** |

(Avancement : 0,5 ; chiffre d'affaires : 0,25 ; résultat : 0,5.)

**Tableau des incidences (1 pt)**

| | Comptes individuels (achèvement) | Comptes consolidés (avancement) | Écart |
|---|---:|---:|---:|
| Actif au 31/12/2026 | Travaux en cours 1 152 000 | Factures à établir 1 440 000 | + 288 000 |
| Résultat de 2025 (avant impôt) | 0 | 108 000 | + 108 000 → réserves 81 000 après impôt différé 27 000 |
| Résultat de 2026 (avant impôt) | 0 | 180 000 | + 180 000 → résultat 135 000 après impôt différé 45 000 |
| Impôt différé passif au 31/12/2026 | — | 288 000 × 25 % | **72 000** |

Le chiffre d'affaires cumulé à l'avancement est inscrit en clients – factures à établir, aucune facture n'ayant été émise ; les travaux en cours, qui représentent des coûts désormais couverts par ce chiffre d'affaires, sont annulés [F04 R9].

**C3 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4181 Clients – Factures à établir | 1 440 000 | |
| 335 Travaux en cours | | 1 152 000 |
| RSV.MORTELAN Réserves MORTELAN (108 000 × 75 %) | | 81 000 |
| RST.MORTELAN Résultat MORTELAN (180 000 × 75 %) | | 135 000 |
| IDP Impôt différé passif (288 000 × 25 %) | | 72 000 |
| *Contrat des HAUTES-FEIGNES : passage à l'avancement* | **1 440 000** | **1 440 000** |

**C3R (compte de résultat, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 71335 Variation des en-cours de production de biens – travaux en cours (annulation de la variation de 2026) | 720 000 | |
| CH_ID Charge d'impôt différé | 45 000 | |
| RES_CR Résultat | 135 000 | |
| 704 Travaux (chiffre d'affaires de 2026 à l'avancement) | | 900 000 |
| *Contrat des HAUTES-FEIGNES : 2026* | **900 000** | **900 000** |

Contrôle : 900 000 – 720 000 = 180 000 € de résultat avant impôt en 2026.

**Associé minoritaire (0,25 pt).** Le retraitement modifie les capitaux propres de MORTELAN, et non ceux du seul groupe. Il est partagé avec les autres capitaux propres de MORTELAN (1.9 a) : M. MORTELAN reçoit 30 % de ses effets, soit 30 % × 81 000 = **24 300 €** de réserves et 30 % × 135 000 = **40 500 €** de résultat ; le groupe en garde 70 %.

---

### 1.7 Opérations internes (4 pts)

#### a. Ventes de bois scié et marge interne (2 pts)

**Justification (0,75 pt).**
- Les ventes et les achats réciproques sont éliminés en totalité, sans incidence sur le résultat [V ANC art. 251-1, p. 45 ; F04 R14].
- Le profit interne compris dans le stock de FORTANGE est éliminé en totalité, puis réparti selon l'entité qui l'a réalisé, ici VORMANCE Scierie, détenue à 100 % : il est à la charge du seul groupe ; l'impôt est corrigé [V art. 251-2, p. 45 ; F04 R14]. La marge éliminée rend la valeur consolidée du stock inférieure à sa base fiscale : **impôt différé actif**.
- **Stock d'ouverture** : les 150 000 € en stock au 01/01/2026 ont été achetés en 2025, quand FORTANGE n'appartenait pas au groupe. La marge que la scierie a réalisée sur ces ventes a été dégagée avec un tiers et retenue dans l'actif net acquis à sa valeur d'entrée (égale à la valeur comptable, annexe 1.8) : aucune marge interne à l'ouverture, aucune correction des réserves.

**Calcul (0,25 pt).** Marge interne au 31/12/2026 : 240 000 × 20 % = **48 000 €** (le taux est exprimé sur le prix de vente) ; impôt différé actif : 48 000 × 25 % = **12 000 €** ; incidence nette sur le résultat de la scierie : – 36 000 €.

**C4 (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 701 Ventes de produits finis (VORMANCE Scierie) | 1 600 000 | |
| 601 Achats stockés – matières premières (FORTANGE) | | 1 600 000 |
| *Élimination des ventes internes de bois scié* | **1 600 000** | **1 600 000** |

**C5 (bilan, 0,5 pt) et C5R (compte de résultat, pour information, hors barème : seules les écritures au bilan sont demandées)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.SCIERIE Résultat VORMANCE Scierie (48 000 × 75 %) | 36 000 | |
| IDA Impôt différé actif | 12 000 | |
| 31 Matières premières (stock de FORTANGE) | | 48 000 |
| *C5 – Élimination de la marge interne sur le stock* | **48 000** | **48 000** |
| 6031 Variation des stocks de matières premières | 48 000 | |
| CH_ID Produit d'impôt différé | | 12 000 |
| RES_CR Résultat | | 36 000 |
| *C5R – Élimination de la marge interne au compte de résultat* | **48 000** | **48 000** |

#### b. Comptes réciproques et règlement en transit (1 pt)

**Rapprochement (0,5 pt).** Créance de la scierie 310 000 € – dette de FORTANGE 190 000 € = 120 000 €, montant du virement émis par FORTANGE le 30/12/2026 et crédité le 04/01/2027. Au 31/12/2026, la somme a quitté le compte bancaire de FORTANGE sans figurer encore sur celui de la scierie : pour le groupe, c'est de la trésorerie en transit. On constate d'abord l'encaissement chez la scierie, puis on élimine les soldes devenus égaux. Ces écritures n'ont aucune incidence sur le résultat [V ANC art. 251-1, p. 45 ; F04 R14]. La créance de la scierie sur PELLANDE (55 000 €), entité mise en équivalence, n'est pas éliminée (1.4).

**C6 et C7 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 512 Banques (règlement en transit) | 120 000 | |
| 4111 Clients (créance de la scierie sur FORTANGE) | | 120 000 |
| *C6 – Virement de FORTANGE en transit* | **120 000** | **120 000** |
| 4011 Fournisseurs (dette de FORTANGE) | 190 000 | |
| 4111 Clients (créance de la scierie sur FORTANGE) | | 190 000 |
| *C7 – Élimination des soldes réciproques* | **190 000** | **190 000** |

#### c. Dividende de MORTELAN (1 pt)

**Justification (0,5 pt).** Les dividendes reçus d'une société consolidée sont éliminés en totalité [V ANC art. 251-2, p. 45 ; F04 R14] : le dividende reçu par VORMANCE Participations, 200 000 × 70 % = **140 000 €**, n'est qu'un transfert du résultat de 2025 de MORTELAN, déjà compris dans les réserves consolidées ; il sort du résultat de la holding et rejoint ses réserves. La part versée à M. MORTELAN (60 000 €) a quitté le groupe : elle réduit les réserves de MORTELAN, donc les intérêts minoritaires calculés au 31/12/2026 (1.9 a), sans autre écriture.

**C8 (bilan, 0,5 pt) et C8R (compte de résultat, pour information, hors barème)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.VORMANCE Résultat VORMANCE Participations | 140 000 | |
| RSV.VORMANCE Réserves VORMANCE Participations | | 140 000 |
| *C8 – Élimination du dividende reçu de MORTELAN* | **140 000** | **140 000** |
| 7611 Revenus des titres de participation | 140 000 | |
| RES_CR Résultat | | 140 000 |
| *C8R – Élimination du dividende au compte de résultat* | **140 000** | **140 000** |

---

### 1.8 Acquisition de FORTANGE (7 pts)

#### a. Actif net réévalué au 01/01/2026 (2,5 pts)

| Élément | Montant |
|---|---:|
| Capitaux propres individuels au 01/01/2026, résultat de 2025 compris (0,25) | 2 800 000 |
| Écart d'évaluation du bâtiment (1 400 000 – 900 000) (0,25) | + 500 000 |
| Écart d'évaluation du stock de plateaux (480 000 – 380 000) (0,25) | + 100 000 |
| Impôt différé passif sur les écarts ((500 000 + 100 000) × 25 %) (0,5) | – 150 000 |
| **Actif net réévalué** (0,25) | **3 250 000** |

- **Écarts d'évaluation (0,5 pt)** : différence entre la valeur d'entrée des actifs identifiables et leur valeur comptable dans le bilan de l'entité acquise, retraité selon les méthodes du groupe [V ANC art. 231-9, p. 22 ; F05 § 1.2]. La valeur d'entrée est le prix que l'acquéreur aurait accepté de payer pour chaque élément séparément [V art. 232-1, p. 24]. Les impôts différés sur ces écarts sont comptabilisés, en contrepartie de l'écart d'acquisition [V art. 232-1, p. 24 ; art. 272-13, p. 59 ; F05 § 1.2].
- **Suivi des écarts (0,5 pt)** : l'écart sur le bâtiment est amorti sur la durée d'utilisation résiduelle, 500 000 / 20 = **25 000 €** par an. L'écart sur le stock suit le stock : les plateaux ayant été utilisés en 2026 pour des meubles vendus, l'écart de 100 000 € majore le coût des ventes de 2026 et l'impôt différé correspondant (25 000 €) est repris ; il ne reste rien de cet écart au 31/12/2026.

#### b. Frais d'acquisition, coût d'acquisition et écart d'acquisition (2 pts)

- **Frais (0,75 pt)** : dans ses comptes individuels, VORMANCE Participations a comptabilisé les honoraires en charges, option permise par le PCG [V PCG art. 121-5 ; F05 § 1.1], et les a déduits fiscalement. En consolidation, le coût d'acquisition comprend les coûts directement imputables à l'acquisition, dont les honoraires des consultants et experts, **nets de l'économie d'impôt** correspondante [V ANC art. 231-2 et 231-3, p. 20-21 ; F05 § 1.1] : les frais sont retirés des charges de 2026 et ajoutés, nets d'impôt, au coût des titres.
- **Coût d'acquisition (0,5 pt)** : 3 240 000 + 80 000 × 75 % = **3 300 000 €**. Le calcul faux le plus fréquent retient le prix seul (3 240 000 €) ou les frais bruts (3 320 000 €) (`JUR-G02`).
- **Écart d'acquisition (0,75 pt)** : 3 300 000 – 80 % × 3 250 000 = 3 300 000 – 2 600 000 = **700 000 €**, écart **positif**, inscrit à l'actif immobilisé en immobilisations incorporelles, ligne « dont écarts d'acquisition positifs » [V ANC art. 231-9, p. 22 ; art. 231-11, p. 23 ; art. 281-1, p. 66 ; F05 § 1.3]. Il est calculé sur la seule part de l'acquéreur : les intérêts minoritaires ne portent que sur leur part de l'actif net réévalué [V art. 232-1, p. 24].

#### c. Amortissement de l'écart d'acquisition et écritures (2,5 pts)

**Amortissement (0,75 pt).** Un écart d'acquisition positif dont la durée d'utilisation est limitée est amorti linéairement sur cette durée ; si elle ne peut être déterminée de manière fiable, sur 10 ans ; la durée résulte d'une analyse documentée et n'est pas une option [V ANC art. 231-11 et IR3, p. 23 ; F05 § 1.3]. L'analyse conduite lors de l'acquisition a conclu à 8 ans : dotation de 2026 = 700 000 / 8 = **87 500 €** ; valeur nette au 31/12/2026 : **612 500 €**. La dotation figure au compte de résultat consolidé sur la ligne propre aux écarts d'acquisition, entre le résultat d'exploitation avant et après dotations aux amortissements, dépréciations et reprises des écarts d'acquisition [V IR3 sous art. 231-12, p. 24 ; art. 281-2, p. 67 ; F05 § 1.3]. L'écart ne portant que sur la part du groupe, son amortissement réduit le seul résultat part du groupe.

**C9 (bilan) et C9R (compte de résultat), 1 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments (écart d'évaluation) | 500 000 | |
| RST.FORTANGE Résultat FORTANGE ((25 000 + 100 000) × 75 %) | 93 750 | |
| 2813 Amortissements des constructions (500 000 / 20) | | 25 000 |
| IDP Impôt différé passif ((500 000 – 25 000) × 25 %) | | 118 750 |
| RSV.FORTANGE Réserves FORTANGE ((500 000 + 100 000) × 75 %) | | 450 000 |
| *C9 – Écarts d'évaluation de FORTANGE nets d'impôt, amortissement et consommation de 2026* | **593 750** | **593 750** |
| 68112 Dotations aux amortissements des immobilisations corporelles | 25 000 | |
| 6031 Variation des stocks de matières premières (écart sur les plateaux consommés) | 100 000 | |
| CH_ID Produit d'impôt différé (125 000 × 25 %) | | 31 250 |
| RES_CR Résultat | | 93 750 |
| *C9R – Effet des écarts d'évaluation sur le résultat de 2026* | **125 000** | **125 000** |

Les réserves de FORTANGE reçoivent les écarts nets d'impôt existant à la date d'acquisition (600 000 – 150 000 = 450 000 €) ; leur effet sur 2026 passe par le résultat. Le stock étant consommé, aucun écart ne figure au compte 31 au 31/12/2026.

**C10 (bilan) et C10R (compte de résultat), 0,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation FORTANGE (80 000 × 75 %) | 60 000 | |
| RST.VORMANCE Résultat VORMANCE Participations | | 60 000 |
| *C10 – Incorporation des frais nets d'impôt au coût des titres* | **60 000** | **60 000** |
| 695 Impôts sur les bénéfices (économie d'impôt incorporée au coût des titres) | 20 000 | |
| RES_CR Résultat | 60 000 | |
| 6226 Honoraires | | 80 000 |
| *C10R – Annulation des frais d'acquisition des titres FORTANGE* | **80 000** | **80 000** |

**C13 (bilan) et C13R (compte de résultat), 0,25 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST_G Résultat consolidé – part du groupe | 87 500 | |
| AMO_EA Amortissements de l'écart d'acquisition FORTANGE | | 87 500 |
| *C13 – Amortissement de 2026 de l'écart d'acquisition* | **87 500** | **87 500** |
| DOT_EA Dotations aux amortissements, dépréciations et reprises des écarts d'acquisition | 87 500 | |
| RES_CR Résultat | | 87 500 |
| *C13R – Dotation de 2026 au compte de résultat* | **87 500** | **87 500** |

(Écriture C13 présentée après l'élimination des titres C12, qui inscrit l'écart d'acquisition à l'actif.)

---

### 1.9 Partage des capitaux propres et mise en équivalence (7 pts)

#### a. Tableaux de partage au 31/12/2026 (3 pts)

**FORTANGE (1,5 pt)**

Résultat retraité de 2026 : 360 000 – 93 750 = **266 250 €** (0,25).

| | Total | Groupe (80 %) | Intérêts minoritaires (20 %) |
|---|---:|---:|---:|
| Capital | 1 000 000 | 800 000 | 200 000 |
| Réserves (1 500 000 + résultat de 2025 affecté 300 000) | 1 800 000 | 1 440 000 | 360 000 |
| Écarts d'évaluation nets d'impôt différé (à l'acquisition) | 450 000 | 360 000 | 90 000 |
| **Capitaux propres retraités hors résultat** | **3 250 000** | **2 600 000** | **650 000** |
| Élimination des titres (coût d'acquisition) | | – 3 300 000 | |
| Écart d'acquisition (inscrit à l'actif) | | + 700 000 | |
| **Réserves consolidées** | | **0** | |
| Résultat retraité de 2026 | 266 250 | 213 000 | 53 250 |
| **Intérêts minoritaires au 31/12/2026** | | | **703 250** |

(Capitaux propres retraités et écarts d'évaluation : 0,5 ; titres, écart d'acquisition et réserves nulles : 0,25 ; résultat et intérêts minoritaires : 0,5.)

Acquise le 01/01/2026, FORTANGE n'apporte aucune réserve consolidée : la différence entre le coût des titres et la quote-part des capitaux propres réévalués est l'écart d'acquisition. Les droits des minoritaires sont calculés sur l'actif net réévalué [V ANC art. 232-1, p. 24 ; F05 § 3]. La contribution de FORTANGE au résultat part du groupe est de 213 000 – 87 500 (amortissement de l'écart) = 125 500 €.

**MORTELAN (1,5 pt)**

| | Total | Groupe (70 %) | Intérêts minoritaires (30 %) |
|---|---:|---:|---:|
| Capital | 500 000 | 350 000 | 150 000 |
| Réserves (819 000 + 300 000 – 200 000 distribués) | 919 000 | 643 300 | 275 700 |
| Contrat à l'avancement : part de 2025, nette d'impôt | 81 000 | 56 700 | 24 300 |
| **Capitaux propres retraités hors résultat** | **1 500 000** | **1 050 000** | **450 000** |
| Élimination des titres | | – 350 000 | |
| **Réserves consolidées** | | **700 000** | |
| Résultat retraité de 2026 (265 000 + 135 000) | 400 000 | 280 000 | 120 000 |
| **Intérêts minoritaires au 31/12/2026** | | | **570 000** |

(Réserves après distribution et contrat : 0,5 ; titres et réserves consolidées : 0,5 ; résultat et intérêts minoritaires : 0,5.)

Les titres, souscrits à la création pour 70 % du capital, n'ont fait naître aucun écart d'acquisition. Les réserves de MORTELAN sont prises après la distribution de mai 2026 : la part du dividende revenue au groupe figure dans les réserves de VORMANCE Participations (C8), celle de M. MORTELAN a quitté le groupe.

#### b. Mise en équivalence de PELLANDE (1,5 pt)

**Tableau (1 pt)**

| | Montant |
|---|---:|
| Capitaux propres de PELLANDE au 31/12/2026 (1 200 000 + 480 000 + 300 000) | 1 980 000 |
| **Valeur d'équivalence** (30 %) (0,25) | **594 000** |
| Titres éliminés : souscription de 30 % du capital à la création (0,25) | – 360 000 |
| **Écart** (0,25) | **234 000** |
| dont réserves consolidées : 30 % × 480 000 | 144 000 |
| dont résultat de 2026 : 30 % × 300 000 | 90 000 |

(Absence d'écart d'évaluation et d'écart d'acquisition justifiée : 0,25.) Les titres ayant été souscrits à la valeur nominale lors de la création de PELLANDE, dont les comptes suivent les méthodes du groupe, la valeur d'équivalence ne comporte ni écart d'évaluation ni écart d'acquisition (`JUR-G03` : le candidat doit le vérifier, et non l'ignorer).

**Dividende (0,5 pt).** Les dividendes reçus des entités mises en équivalence sont éliminés du compte de résultat de l'entité qui détient les titres et portés en augmentation des réserves consolidées [V ANC art. 262-3, p. 49 ; F05 § 4]. La scierie a reçu 30 % × 100 000 = **30 000 €**. La quote-part du résultat de 2025 de PELLANDE figure déjà dans les réserves consolidées par la mise en équivalence ; la distribution a réduit d'autant les réserves de PELLANDE, donc la valeur d'équivalence : laisser le dividende en résultat le compterait deux fois.

#### c. Écritures (2,5 pts)

**C11 (bilan, 0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.SCIERIE Capital VORMANCE Scierie | 2 000 000 | |
| RSV.SCIERIE Réserves VORMANCE Scierie retraitées | 3 317 500 | |
| RST.SCIERIE Résultat VORMANCE Scierie retraité | 750 375 | |
| 261 Titres de participation VORMANCE Scierie | | 2 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 3 317 500 |
| RST_G Résultat consolidé – part du groupe | | 750 375 |
| *Élimination des titres VORMANCE Scierie et partage (100 % groupe)* | **6 067 875** | **6 067 875** |

Réserves retraitées : 3 100 000 + 225 000 (C1) – 37 500 (C2) + 30 000 (C15) = 3 317 500 € ; résultat retraité : 720 000 + 133 875 (C1) – 37 500 (C2) – 36 000 (C5) – 30 000 (C15) = 750 375 €. La scierie a été créée par la holding : ses titres égalent son capital, sans écart.

**C12 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.FORTANGE Capital FORTANGE | 1 000 000 | |
| RSV.FORTANGE Réserves FORTANGE retraitées (1 800 000 + 450 000) | 2 250 000 | |
| RST.FORTANGE Résultat FORTANGE retraité | 266 250 | |
| EA Écart d'acquisition FORTANGE | 700 000 | |
| 261 Titres de participation FORTANGE (3 240 000 + 60 000) | | 3 300 000 |
| RSV_M Intérêts minoritaires – capital et réserves (20 % × 3 250 000) | | 650 000 |
| RST_G Résultat consolidé – part du groupe (80 % × 266 250) | | 213 000 |
| RST_M Intérêts minoritaires – résultat (20 % × 266 250) | | 53 250 |
| *Élimination des titres FORTANGE, écart d'acquisition et partage* | **4 216 250** | **4 216 250** |

**C14 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.MORTELAN Capital MORTELAN | 500 000 | |
| RSV.MORTELAN Réserves MORTELAN retraitées (919 000 + 81 000) | 1 000 000 | |
| RST.MORTELAN Résultat MORTELAN retraité (265 000 + 135 000) | 400 000 | |
| 261 Titres de participation MORTELAN | | 350 000 |
| RSV_G Réserves consolidées – part du groupe | | 700 000 |
| RSV_M Intérêts minoritaires – capital et réserves | | 450 000 |
| RST_G Résultat consolidé – part du groupe | | 280 000 |
| RST_M Intérêts minoritaires – résultat | | 120 000 |
| *Élimination des titres MORTELAN et partage* | **1 900 000** | **1 900 000** |

**C15 (bilan, 0,5 pt) et C15R (compte de résultat, pour information, hors barème)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.SCIERIE Résultat VORMANCE Scierie | 30 000 | |
| RSV.SCIERIE Réserves VORMANCE Scierie | | 30 000 |
| *C15 – Élimination du dividende reçu de PELLANDE (bilan)* | **30 000** | **30 000** |
| 7611 Revenus des titres de participation (VORMANCE Scierie) | 30 000 | |
| RES_CR Résultat | | 30 000 |
| *C15R – Élimination du dividende au compte de résultat* | **30 000** | **30 000** |

**C16 (bilan, 0,5 pt) et C16R (compte de résultat, pour information, hors barème)**

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence (30 % × 1 980 000) | 594 000 | |
| 261 Titres de participation PELLANDE (détenus par la scierie) | | 360 000 |
| RSV_G Réserves consolidées – part du groupe (30 % × 480 000) | | 144 000 |
| RST_G Résultat consolidé – part du groupe (30 % × 300 000) | | 90 000 |
| *C16 – Mise en équivalence des titres PELLANDE* | **594 000** | **594 000** |
| RES_CR Résultat | 90 000 | |
| QP_MEE Résultat net lié aux entités mises en équivalence | | 90 000 |
| *C16R – Quote-part de résultat de PELLANDE* | **90 000** | **90 000** |

---

### 1.10 Documents de synthèse (7 pts)

#### a. Bilan consolidé au 31/12/2026 (5 pts)

Modèle du règlement ANC [V art. 281-1, p. 66 ; F14 § 1.2]. Les impôts différés actifs et passifs d'une même entité fiscale sont présentés pour leur solde net [V ANC art. 272-14, p. 59 ; F04 § 1] ; les sociétés étant imposées séparément, la compensation se fait société par société.

**Impôts différés par entité fiscale**

| Société | Impôts différés passifs | Impôts différés actifs | Solde net |
|---|---:|---:|---:|
| VORMANCE Scierie | 119 625 (C1) | 25 000 (C2) + 12 000 (C5) | **82 625** passif |
| FORTANGE | 118 750 (C9) | — | **118 750** passif |
| MORTELAN | 72 000 (C3) | — | **72 000** passif |
| **Total** | | | **273 375** passif ; aucun impôt différé actif |

**Réserves consolidées et résultat net part du groupe**

| Société | Réserves consolidées | Résultat net part du groupe |
|---|---:|---:|
| VORMANCE Participations | 5 600 000 + 140 000 (C8) = 5 740 000 | 410 000 – 140 000 (C8) + 60 000 (C10) = 330 000 |
| VORMANCE Scierie | 3 317 500 | 750 375 |
| FORTANGE | 0 | 213 000 – 87 500 (écart d'acquisition) = 125 500 |
| MORTELAN | 700 000 | 280 000 |
| PELLANDE | 144 000 | 90 000 |
| **Total** | **9 901 500** | **1 575 875** |

Contrôle du résultat : somme des résultats individuels 1 755 000 + 133 875 (C1) – 37 500 (C2) + 135 000 (C3) – 36 000 (C5) – 140 000 (C8) – 93 750 (C9) + 60 000 (C10) – 87 500 (C13) – 30 000 (C15) + 90 000 (C16) = **1 749 125 €** (résultat de l'ensemble consolidé) ; intérêts minoritaires 53 250 + 120 000 = 173 250 € ; part du groupe 1 575 875 €.

**Bilan consolidé au 31/12/2026**

| Actif | Calcul | Montant |
|---|---|---:|
| Immobilisations incorporelles | 1 150 000 + 612 500 | 1 762 500 |
| dont écarts d'acquisition positifs | 700 000 – 87 500 (0,25) | 612 500 |
| Immobilisations corporelles | 24 600 000 + 500 000 – 25 000 (FORTANGE) – 100 000 (composants) (0,25) | 24 975 000 |
| Immobilisations financières | 6 160 000 – 5 950 000 (titres éliminés ou mis en équivalence) (0,25) | 210 000 |
| Titres mis en équivalence | PELLANDE (0,25) | 594 000 |
| **Total actif immobilisé** | | **27 541 500** |
| Stocks et en-cours | 15 840 000 – 1 152 000 (travaux en cours) – 48 000 (marge interne) (0,25) | 14 640 000 |
| Clients et comptes rattachés | 13 900 000 + 1 440 000 (factures à établir) – 120 000 – 190 000 (0,25) | 15 030 000 |
| Autres créances et comptes de régularisation | 1 450 000 ; dont impôts différés actifs : néant, après compensation (0,25) | 1 450 000 |
| Disponibilités | 4 380 000 + 120 000 (règlement en transit) (0,25) | 4 500 000 |
| **Total actif circulant** | | **35 620 000** |
| **Total de l'actif** | | **63 161 500** |

| Passif | Calcul | Montant |
|---|---|---:|
| Capital (entité consolidante) | VORMANCE Participations | 4 000 000 |
| Réserves et résultat consolidés | 9 901 500 + 1 575 875, tableau ci-dessus (réserves 0,75 ; résultat 0,75) | 11 477 375 |
| dont résultat net de l'exercice | | 1 575 875 |
| **Capitaux propres (part du groupe)** | | **15 477 375** |
| **Intérêts minoritaires** | 703 250 (FORTANGE) + 570 000 (MORTELAN) (0,5) | **1 273 250** |
| Provisions | 1 120 000 ; provisions réglementées éliminées (C1) (0,25) | 1 120 000 |
| Emprunts et dettes financières | sans changement | 19 600 000 |
| Fournisseurs et comptes rattachés | 15 200 000 – 190 000 (0,25) | 15 010 000 |
| Autres dettes et comptes de régularisation | 10 407 500 + 273 375 impôts différés passifs (0,25) | 10 680 875 |
| dont impôts différés passifs | solde net par entité fiscale | 273 375 |
| **Total des dettes** | | **45 290 875** |
| **Total du passif** | | **63 161 500** |

Contrôle (0,25 pt) : le total de l'actif égale celui du passif. Les capitaux propres part du groupe et les intérêts minoritaires (16 750 625 €) se comparent aux capitaux propres et provisions réglementées cumulés (20 674 000 + 478 500 = 21 152 500 €). L'écart de – 4 401 875 € est la somme des variations des autres postes : titres de participation éliminés – 5 950 000 ; écart d'acquisition net + 612 500 ; titres mis en équivalence + 594 000 ; immobilisations corporelles + 375 000 ; stocks – 1 200 000 ; clients + 1 130 000 ; disponibilités + 120 000 ; fournisseurs (dette éliminée) + 190 000 ; impôts différés passifs – 273 375.

Les intérêts minoritaires forment une rubrique distincte des capitaux propres part du groupe, avant les provisions et les dettes [V art. 281-1, p. 66 ; F14 § 1.2]. Le résultat de l'exercice figure dans les réserves et résultat consolidés, « dont résultat net de l'exercice » [V art. 281-1, p. 66].

#### b. Annexe consolidée et différence avec les IFRS (2 pts)

**Annexe (1,5 pt).** L'annexe forme un tout avec le bilan et le compte de résultat ; elle mentionne le règlement ANC n° 2020-01 comme cadre et ne donne que les informations significatives, avec les chiffres de l'exercice précédent [V art. 111-4, p. 8 ; art. 282-1, p. 74 ; F14 § 1.1 et 1.4]. Pour le cas (0,5 pt par thème, trois thèmes au moins sur quatre) :
- **périmètre** : liste des sociétés consolidées, pourcentages détenus et méthode (IG pour la scierie, FORTANGE et MORTELAN ; mise en équivalence pour PELLANDE, détenue par la scierie), entrée de FORTANGE au 01/01/2026 et ses effets sur les comptes [V art. 282-3 à 282-8, intitulés ; F14 § 1.4] ;
- **méthodes** : approche directe ; élimination des amortissements dérogatoires ; approche par composants et durées d'amortissement ; méthode à l'avancement pour les contrats à long terme ; impôts différés à 25 %, non actualisés, compensés par entité fiscale [V art. 282-2, intitulé ; F14 § 1.4] ;
- **écart d'acquisition de FORTANGE** : calcul (coût 3 300 000 €, frais nets d'impôt compris ; actif net réévalué ; écarts d'évaluation), durée d'utilisation de 8 ans et analyse qui la fonde, amortissement de 87 500 € et valeur nette de 612 500 € [V art. 282-19 à 282-30, explication des postes, intitulés ; F14 § 1.4] ;
- **contrat des HAUTES-FEIGNES** : méthode à l'avancement et mesure par les coûts engagés, chiffre d'affaires (900 000 € en 2026) et résultat dégagés, montant inscrit en factures à établir, impôt différé passif correspondant.

**Différence avec les IFRS (0,5 pt, une seule attendue).**
- Les **participations ne donnant pas le contrôle** seraient présentées **au sein des capitaux propres**, séparément des capitaux propres attribuables aux propriétaires de la société mère [V IFRS 10 § 22 ; IAS 1 § 54 q) ; F14 § 2.2], alors qu'en ANC les intérêts minoritaires forment une rubrique distincte des capitaux propres part du groupe ;
- ou : l'état de la situation financière distinguerait les éléments **courants et non courants** [V IAS 1 § 60 ; F14 § 2.2], là où le modèle ANC distingue l'actif immobilisé et l'actif circulant ;
- ou : les impôts différés ne seraient jamais classés en éléments courants [V IAS 1 § 56] et figureraient sur des postes distincts [V IAS 1 § 54 ; F14 § 2.2].

---

### Réponses tolérées
- **1.1** : seuils examinés sur la seule clôture de 2026, si la condition des deux clôtures consécutives est rappelée (0,25 pt perdu sinon).
- **1.2 b** : réponse fondée sur la seule définition du passif du cadre conceptuel de 2018, sans référence à IAS 37.
- **1.3** : retraitements passés par écritures après le cumul, si le candidat précise qu'ils précèdent l'élimination des opérations internes et le partage ; rapprochement des réciproques placé après les retraitements, s'il précède le cumul et les éliminations.
- **1.5 a et b** : écritures de bilan et de compte de résultat regroupées si les réserves et le résultat sont distingués ; impôts différés de la ligne présentés en un seul solde (94 625 € passif) si le calcul par retraitement est montré en 1.5 c ; amortissements par composants enregistrés sur des sous-comptes du 2815 par composant ; en 1.5 b, candidat qui relève que la décomposition d'un actif dont les éléments ont des durées d'utilisation différentes s'impose aussi dans les comptes individuels (points du principe accordés).
- **1.6** : variation des en-cours enregistrée au compte 7133 ; créance inscrite en 4181 ou en « clients – produits à recevoir sur contrats » ; tableau présenté en chiffre d'affaires et coûts, s'il conduit aux mêmes résultats.
- **1.7 a** : élimination des ventes internes portée sur le compte 6031 plutôt que sur le compte 601, si l'incidence nulle sur le résultat est relevée.
- **1.7 b** : écriture unique éliminant 310 000 € de créance contre 190 000 € de dette et 120 000 € de disponibilités.
- **1.8 a** : actif net réévalué présenté à partir des écarts nets d'impôt (500 000 × 75 % + 100 000 × 75 %).
- **1.9** : partage présenté en distinguant les réserves de 2025 et le résultat de 2025 affecté ; écart d'acquisition présenté hors du tableau de partage, si le coût des titres et la quote-part sont rapprochés.
- **1.10 a** : réserves consolidées et résultat net part du groupe présentés sur deux lignes ; écritures au compte de résultat ajoutées aux questions 1.7 et 1.9 (sans points supplémentaires) ; impôts différés actifs et passifs non compensés (37 000 € à l'actif, 310 375 € au passif ; total du bilan 63 198 500 €) : 0,25 pt perdu ; écart d'acquisition présenté sur une ligne propre de l'actif immobilisé.
- **1.10 b** : toute autre différence de présentation exacte et justifiée.
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (le jury valorise la logique du candidat, `JUR-F08`).

### Erreurs fréquentes
- **Obligation de consolider** : un seul exercice examiné ou seuils périmés (F99) ; SARL présentée comme dispensée parce qu'elle n'est pas une société par actions ; option pour les IFRS jugée impossible faute de cotation.
- **Cadre conceptuel** : amortissements dérogatoires qualifiés de dette ou de dépréciation ; avantage fiscal ignoré ou porté en capitaux propres sans impôt différé.
- **Processus** : cumul des comptes avant leurs retraitements ; élimination des titres avant l'élimination des opérations internes ; rôle du manuel confondu avec celui de la liasse ; phases énumérées sans leur objet (`JUR-G01`).
- **Périmètre** : participation de la scierie dans PELLANDE oubliée ou multipliée deux fois ; contrôle exclusif retenu parce que les autres associés sont dispersés.
- **Amortissements dérogatoires** : dotation de 2025 portée en résultat de 2026 ; impôt différé oublié ou inversé ; écritures enregistrées au résultat d'exploitation au lieu du résultat exceptionnel (`JUR-G04`, `JUR-G06`) ; tableau « comptes individuels / comptes consolidés » non présenté (`JUR-F05`).
- **Composants** : écart de 2025 oublié dans les réserves ; impôt différé passif au lieu d'un actif ; comparaison des composants à l'amortissement fiscal au lieu de l'amortissement comptable individuel.
- **Contrat à long terme** : avancement mesuré sur le seul exercice ; travaux en cours laissés à l'actif à côté de la créance ; part de 2025 portée en résultat de 2026 ; part des minoritaires oubliée dans le partage.
- **Opérations internes** : marge calculée sur le coût (240 000 × 20/120) au lieu du prix de vente ; marge éliminée sur le stock d'ouverture, acheté avant l'entrée de FORTANGE dans le groupe ; virement en transit oublié, d'où des soldes réciproques inégaux ; créance sur PELLANDE éliminée.
- **Coût d'acquisition et écart** : frais d'acquisition omis ou retenus pour leur montant brut (`JUR-G02`) ; écart sur le stock oublié ou laissé à l'actif au 31/12/2026 ; amortissement de l'écart d'acquisition partagé avec les minoritaires.
- **Partage et mise en équivalence** : minoritaires calculés sur les capitaux propres non réévalués ; réserves de MORTELAN prises avant la distribution ; dividende de PELLANDE laissé en résultat ; écarts d'évaluation et d'acquisition non examinés dans le tableau de mise en équivalence (`JUR-G03`) ; écritures non équilibrées (`JUR-F04`).
- **Bilan consolidé** : provisions réglementées maintenues ; titres de participation laissés à l'actif ; intérêts minoritaires présentés dans les capitaux propres part du groupe ; impôts différés non compensés par entité fiscale ; bilan non équilibré faute de contrôle (`JUR-F02`).

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, contrôle, sens, mode d'évaluation, régime fiscal et déficits | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable ; `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur ; `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 3,5 |
| 2.2 Valeur réelle et composition des apports | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 3 |
| 2.3 Parité, soulte et plafond légal, équité, répartition du capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer ; `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 6 |
| 2.4 Écritures chez LAMÉLIANE | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 3 |
| 2.5 Écritures de base chez ORVALIÈRE | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 3,5 |
| 2.6 Écritures complémentaires : dette réciproque et frais de fusion | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 3 |
| 2.7 Note au président d'ORVALIÈRE | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 3 |
| **Total** | | **25** |

---

### 2.1 Qualification, mode d'évaluation des apports, régime fiscal (3,5 pts)

**Qualification et référentiel (1 pt)**
- L'opération est une **fusion-absorption** : LAMÉLIANE transmet l'ensemble de son patrimoine, actif et passif, à ORVALIÈRE (**transmission universelle**) ; elle est **dissoute sans liquidation** ; ses associés reçoivent des actions ORVALIÈRE émises par augmentation de capital, complétées d'une soulte en numéraire [V PCG art. 710-2, renvoi à C. com. L. 236-1, F01 § 1] (0,5 pt).
- Ce n'est pas une acquisition de titres : ORVALIÈRE n'achète pas les actions LAMÉLIANE, elle reçoit un patrimoine et rémunère les associés de LAMÉLIANE par ses propres actions ; seule la soulte est payée en numéraire (0,25 pt).
- L'enregistrement relève, dans les comptes individuels des deux sociétés, du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe la valeur d'inscription des apports [V art. 710-1 et 720-1, F01 § 1]. La parité, elle, se calcule sur les valeurs d'échange fournies [V art. 740-1, F01 § 1]. Les comptes consolidés de VORMANCE ne sont pas concernés (0,25 pt).

**Situation de contrôle (0,25 pt).** ORVALIÈRE est contrôlée de manière exclusive par JOUVERNEY Participations (70 % des droits de vote), LAMÉLIANE par CHAUMEROT Développement (75 %). Aucune des deux sociétés ne détient d'actions de l'autre et les deux holdings n'ont aucun lien : l'opération est réalisée **sous contrôle distinct** [V PCG art. 741-1 et 741-2, F01 § 2.1].

**Sens de l'opération (0,5 pt).** Après la fusion (voir 2.3 d), JOUVERNEY Participations détient **52,50 %** du capital et des droits de vote d'ORVALIÈRE : l'actionnaire principal de l'absorbante, bien que dilué, **conserve le contrôle**. CHAUMEROT Développement perd le contrôle de LAMÉLIANE et ne détient que 18,75 % d'ORVALIÈRE. La fusion est **à l'endroit** ; ORVALIÈRE est l'initiatrice, LAMÉLIANE la cible [V art. 742-1, F01 § 2.2]. La conclusion vaut pour toutes les parités étudiées : 54,44 % avec le projet de traité, 52,13 % avec la parité exacte.

**Mode d'évaluation (0,25 pt).** Contrôle distinct et opération à l'endroit : les apports sont évalués à la **valeur réelle** ; l'opération est traitée comme une prise de contrôle [V art. 743-1, cas 4, F01 § 2.3].

**Régime fiscal de faveur (1,5 pt)**
- *Conditions et engagements (0,5 pt).* Les deux sociétés sont passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1]. Pour une fusion, le régime de faveur s'applique sauf option pour le droit commun [V BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1], à condition qu'ORVALIÈRE prenne dans le traité les engagements de l'art. 210 A-3 : reprendre à son passif les provisions dont l'imposition est différée ; se substituer à LAMÉLIANE pour la réintégration des résultats dont l'imposition avait été différée ; calculer les plus-values de cession ultérieure des immobilisations non amortissables d'après leur valeur fiscale chez LAMÉLIANE ; réintégrer les plus-values sur biens amortissables ; inscrire les stocks à leur valeur fiscale chez LAMÉLIANE ou imposer le profit correspondant [V 210 A-3, a à e, F02 § 4].
- *Effets pour LAMÉLIANE et pour ORVALIÈRE (0,5 pt).*
  - Chez LAMÉLIANE, la plus-value dégagée par la fusion n'est pas soumise à l'impôt [V 210 A-1] ; la provision pour garanties, toujours justifiée, n'est pas imposée [V 210 A-2] et ORVALIÈRE la reprend à son passif. Le bénéfice de la période du 1er janvier au 31 mars 2027 (60 000 €) est imposé immédiatement chez LAMÉLIANE, quel que soit le régime [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2] ; il est ici entièrement absorbé par ses déficits antérieurs (annexe 2.2) : aucun impôt n'est dû.
  - Chez ORVALIÈRE : sursis d'imposition de la plus-value sur le terrain (160 000 €), dont la valeur fiscale chez LAMÉLIANE est conservée ; il en va de même du fonds commercial (430 000 €), qui n'avait aucune valeur fiscale chez LAMÉLIANE : immobilisation non amortissable, sa plus-value est en sursis et sera calculée, en cas de cession, d'après cette valeur nulle ; réintégration de la plus-value sur les constructions (240 000 €) par parts égales sur 15 ans, soit 16 000 € par an, et de celle sur les matériels (120 000 €) sur 5 ans, soit 24 000 € par an, les amortissements futurs étant calculés sur la valeur d'apport ; produits finis inscrits fiscalement à 380 000 € : le profit de 60 000 € sera imposé lors de leur vente [V 210 A-3-c, d, e, F02 § 2]. La plus-value sur les constructions représente 66,67 % de la plus-value nette sur biens amortissables (240 000 / 360 000), en deçà du seuil de 90 % : la durée de 15 ans s'applique. Comptablement, ces impositions futures justifient la provision pour impôts intégrée aux apports (voir 2.2).
- *Déficits de LAMÉLIANE (0,5 pt).* Pour une fusion placée sous le régime de faveur, les déficits non encore déduits de l'absorbée sont transférés à l'absorbante **sous réserve d'un agrément** [V CGI art. 209 II-1, F02 § 3]. La dispense d'agrément ne joue pas : elle suppose un montant transféré inférieur à 200 000 €, et les déficits atteignent 520 000 € [V 209 II-2]. Conditions de l'agrément, appliquées au cas [V 209 II-1, a à d] :
  - a) opération justifiée économiquement, sans motivation principalement fiscale : sécuriser l'approvisionnement en poutres d'ORVALIÈRE ; les valeurs d'échange n'attribuent d'ailleurs aucune valeur aux déficits ;
  - b) pas de changement significatif de l'activité à l'origine des déficits pendant leur période de constatation : même activité, même site, mêmes moyens, même clientèle depuis 2004 ;
  - c) poursuite de cette activité par ORVALIÈRE pendant au moins trois ans, sans changement significatif : ORVALIÈRE prévoit de la poursuivre au moins jusqu'en 2032 ;
  - d) déficits ne provenant pas de la gestion d'un patrimoine mobilier ou immobilier : ils sont nés de la fabrication, et LAMÉLIANE ne détient ni participation ni immeuble loué.
  
  Les conditions paraissent remplies, mais la décision de l'administration n'est pas connue : c'est pourquoi aucun impôt différé actif n'est retenu au titre des déficits (annexe 2.3).

---

### 2.2 Valeur réelle et composition des apports (3 pts)

**Éléments identifiés figurant au bilan de LAMÉLIANE (0,75 pt)**

| Élément | Valeur nette comptable | Valeur réelle | Écart |
|---|---:|---:|---:|
| Terrain | 250 000 | 410 000 | + 160 000 |
| Constructions | 1 320 000 | 1 560 000 | + 240 000 |
| Matériels industriels | 1 400 000 | 1 520 000 | + 120 000 |
| Matières premières (bois) | 520 000 | 520 000 | 0 |
| Produits finis (poutres) | 380 000 | 440 000 | + 60 000 |
| Clients | 960 000 | 960 000 | 0 |
| Disponibilités | 150 000 | 150 000 | 0 |
| **Actifs identifiés** | **4 980 000** | **5 560 000** | **+ 580 000** |

**Éléments identifiés ne figurant pas au bilan (0,25 pt).** À la valeur réelle, les apports comprennent les éléments identifiés, figurant ou non au bilan de l'absorbée, notamment les provisions pour retraites et les impôts différés [V art. 744-1, F01 § 3.1] : engagements de retraite de **100 000 €**, non provisionnés par LAMÉLIANE, et impôt différé net (ci-dessous).

**Impôt différé intégré aux apports (1 pt).** Le régime de faveur reporte chez ORVALIÈRE l'imposition des plus-values sur biens amortissables et sur produits finis ; l'écart entre valeur d'apport et valeur fiscale est une différence temporaire [V corrigé du sujet zéro, Q 2.4, F01 § 3.3 ; F02 § 6].

| Élément | Base | Impôt différé (25 %) |
|---|---:|---:|
| Plus-value sur constructions | + 240 000 | + 60 000 |
| Plus-value sur matériels industriels | + 120 000 | + 30 000 |
| Plus-value sur produits finis | + 60 000 | + 15 000 |
| Engagements de retraite (déductibles au versement) | – 100 000 | – 25 000 |
| **Total net : passif d'impôt différé** | **+ 320 000** | **+ 80 000** |

Pas d'impôt différé sur le terrain (aucune cession envisagée), sur le fonds commercial, élément résiduel, ni sur les déficits (annexe 2.3) [V F01 § 3.3]. La provision pour garanties, déjà déduite fiscalement et reprise pour le même montant, ne crée aucune différence temporaire. Le solde net (**80 000 €**) est inscrit en **provision pour impôts (compte 1523)**.

**Actif net réel identifié (0,5 pt)**

| | Montant |
|---|---:|
| Actifs identifiés | 5 560 000 |
| – Provision pour garanties données aux clients | – 60 000 |
| – Engagements de retraite | – 100 000 |
| – Provision pour impôts (impôt différé net) | – 80 000 |
| – Emprunts bancaires | – 1 400 000 |
| – Fournisseurs | – 520 000 |
| – Dettes sociales et fiscales (150 000 + 80 000) | – 230 000 |
| **Actif net réel identifié** | **3 170 000** |

**Fonds commercial et composition des apports (0,5 pt).** Fonds commercial = valeur globale des apports – actif net identifié = 3 600 000 – 3 170 000 = **430 000 €**. Cet écart positif, qui correspond à la clientèle et au savoir-faire de LAMÉLIANE, est inscrit au traité sur la ligne « fonds commercial » et repris au bilan d'ORVALIÈRE (compte 207) [V art. 744-1, F01 § 3.1].

Contrôle à partir des capitaux propres de LAMÉLIANE : 2 770 000 + 580 000 – 100 000 – 80 000 = 3 170 000 € ; 3 170 000 + 430 000 = 3 600 000 €.

Les apports (3 600 000 €) se composent des actifs identifiés (5 560 000 €) et du fonds commercial (430 000 €), diminués des passifs identifiés (2 390 000 €).

---

### 2.3 Parité, soulte et plafond légal (6 pts)

**a) Valeurs unitaires et parité exacte (0,5 pt)**
- Valeur unitaire ORVALIÈRE : 10 500 000 / 105 000 = **100 €** ; valeur unitaire LAMÉLIANE : 3 600 000 / 60 000 = **60 €**.
- Parité exacte : 60 / 100 = 3 / 5, soit **3 actions ORVALIÈRE pour 5 actions LAMÉLIANE**, sans soulte : 60 000 × 3 / 5 = 36 000 actions à émettre. Toutes les actions LAMÉLIANE sont rémunérées : ORVALIÈRE n'en détient aucune.

**b) Projet de traité (1,25 pt).** La soulte en espèces ne peut pas dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-1, F01 § 4].

| Projet de traité (1 pour 2, soulte de 10 € par action LAMÉLIANE) | Montant |
|---|---:|
| Actions ORVALIÈRE à émettre (60 000 / 2) | 30 000 |
| Valeur des actions remises (30 000 × 100) | 3 000 000 |
| Soulte (60 000 × 10) | 600 000 |
| Valeur des actions LAMÉLIANE reçues (60 000 × 60) | 3 600 000 |
| Valeur nominale des actions attribuées (30 000 × 40) | 1 200 000 |
| **Plafond légal (10 %)** | **120 000** |

La soulte de 600 000 € représente cinq fois le plafond : **elle est illégale** et le traité ne peut pas être conclu en ces termes. Contrôle par lot : pour 2 actions LAMÉLIANE (120 €), 1 action ORVALIÈRE (100 €) et 20 € de soulte, alors que le plafond est de 10 % × 40 = 4 €. Barème : actions et soulte (0,5), plafond (0,5), conclusion (0,25).

**c) Parité légale et conseil (2,5 pts)**
- *Parité minimale (0,75 pt).* Pour une parité de p actions ORVALIÈRE par action LAMÉLIANE, la soulte par action LAMÉLIANE vaut 60 – 100 p et le plafond 10 % × 40 × p = 4 p. La soulte est légale si 60 – 100 p ≤ 4 p, soit **p ≥ 60 / 104 = 15 / 26 ≈ 0,5769**. Pour que la soulte reste versée aux associés de LAMÉLIANE, il faut aussi p < 3 / 5. En nombre d'actions : au moins 60 000 × 15 / 26 = 34 615,4, soit **34 616 actions**.
- *Proposition (1,25 pt).* Pour un lot de b actions LAMÉLIANE (b ≤ 12), il faut un nombre entier a d'actions ORVALIÈRE tel que 0,5769 b ≤ a < 0,6 b. L'intervalle est étroit (largeur 0,0231 b, au plus 0,28 pour b = 12) : seul b = 12 contient un entier (0,5 pt).

| b | 5 | 7 | 8 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|
| Intervalle de a | 2,88 à 3,00 (exclu) | 4,04 à 4,20 | 4,62 à 4,80 | 5,77 à 6,00 (exclu) | 6,35 à 6,60 | 6,92 à 7,20 |
| Entier possible | aucun | aucun | aucun | aucun | aucun | **7** |

  Les autres valeurs de b (1 à 4, 6 et 9) ne donnent pas davantage d'entier. La parité 4 pour 7 (0,5714), par exemple, est sous le minimum. La parité proposée est donc **7 actions ORVALIÈRE pour 12 actions LAMÉLIANE** (0,75 pt) :

| Solution proposée (7 pour 12) | Montant |
|---|---:|
| Actions ORVALIÈRE à émettre (60 000 × 7 / 12) | 35 000 |
| Valeur des actions remises (35 000 × 100) | 3 500 000 |
| **Soulte** (3 600 000 – 3 500 000) | **100 000** |
| Soulte par lot de 12 actions LAMÉLIANE (12 × 60 – 7 × 100) | 20 € |
| Valeur nominale des actions attribuées (35 000 × 40) | 1 400 000 |
| **Plafond légal (10 %)** | **140 000** |
| Conclusion | **Soulte légale** (100 000 ≤ 140 000) |

  Chaque associé de LAMÉLIANE détient un multiple de 12 actions (45 000, 6 000, 4 800 et 4 200) : il n'y a pas de rompus.
- *Conseil à M. JOUVERNEY (0,5 pt).* La loi limite fortement la part en numéraire : même au nombre minimal de 34 616 actions, la soulte ne dépasserait pas 138 400 €. Avec la parité 7 pour 12, CHAUMEROT Développement reçoit 75 000 € au lieu des 450 000 € du projet ; M. CHAUMEROT ne peut pas obtenir par la soulte la somme qu'il souhaitait. Pour ORVALIÈRE, la solution préserve la trésorerie (100 000 € décaissés au lieu de 600 000 €, alors que LAMÉLIANE n'apporte que 150 000 € de disponibilités). Le coût en dilution est faible : JOUVERNEY Participations détient 52,50 % au lieu de 54,44 % et garde le contrôle. La parité exacte (3 pour 5, sans soulte) est aussi légale ; elle supprime tout décaissement mais ne répond pas au souhait de M. CHAUMEROT. Recommandation : 7 pour 12 avec une soulte de 100 000 €.

**d) Équité, augmentation de capital, prime et répartition du capital (1,75 pt)**
- *Équité (0,5 pt).* Valeur des actions remises + soulte = 35 000 × 100 + 100 000 = 3 600 000 € = valeur des actions reçues (60 000 × 60) [V méthode du corrigé du sujet zéro, F01 § 4]. Après la fusion, l'action ORVALIÈRE vaut toujours (10 500 000 + 3 600 000 – 100 000) / 140 000 = **100 €** : aucun groupe d'actionnaires ne s'enrichit au détriment de l'autre ; l'échange est équitable.
- *Augmentation de capital et prime (0,5 pt).* Augmentation de capital = 35 000 × 40 = **1 400 000 €** ; prime de fusion = valeur des apports – augmentation de capital – soulte = 3 600 000 – 1 400 000 – 100 000 = **2 100 000 €** [V F01 § 4 et § 9].
- *Répartition du capital après l'opération (0,75 pt).* Nombre d'actions : 105 000 + 35 000 = **140 000**.

| Actionnaire | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| JOUVERNEY Participations | 73 500 | 70,00 % | 73 500 | 52,50 % |
| Autres actionnaires d'ORVALIÈRE | 31 500 | 30,00 % | 31 500 | 22,50 % |
| CHAUMEROT Développement (45 000 × 7 / 12) | – | – | 26 250 | 18,75 % |
| Mme BOURDENET (6 000 × 7 / 12) | – | – | 3 500 | 2,50 % |
| M. VALLIÈRE (4 800 × 7 / 12) | – | – | 2 800 | 2,00 % |
| Mme FERLANDE (4 200 × 7 / 12) | – | – | 2 450 | 1,75 % |
| **Total** | **105 000** | **100 %** | **140 000** | **100 %** |

Chaque action donnant une voix, les droits de vote suivent la même répartition. JOUVERNEY Participations garde la majorité : la fusion est à l'endroit (voir 2.1).

---

### 2.4 Écritures chez LAMÉLIANE au 31 mars 2027 (3 pts)

**Résultat de fusion (0,5 pt, compris dans A1).** LAMÉLIANE cède son patrimoine pour sa valeur d'apport (3 600 000 €), alors que son actif net comptable est de 2 770 000 € (capitaux propres) : elle dégage un **résultat de fusion de 830 000 €**. Il correspond aux plus-values sur les éléments identifiés (580 000 €) et au fonds commercial (430 000 €), diminués des engagements de retraite (100 000 €) et de la provision pour impôts (80 000 €) compris dans l'apport. Il est présenté en **résultat exceptionnel** (annexe 2.4), au compte 778, l'opération étant pour LAMÉLIANE un événement majeur et inhabituel [V PCG art. 513-5, F01 § 9]. Sous le régime de faveur, il n'est pas soumis à l'impôt [V CGI art. 210 A-1, F02 § 2] : aucun impôt n'est à constater.

**A1 — Apport de l'actif et du passif (1 pt, plus 0,5 pt ci-dessus).** Les éléments sortent pour leur valeur comptable (valeurs brutes et amortissements) ; la créance sur ORVALIÈRE est inscrite pour la valeur d'apport.

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – ORVALIÈRE, compte d'apport | 3 600 000 | |
| 28131 Amortissements des bâtiments | 1 080 000 | |
| 28154 Amortissements des matériels industriels | 1 700 000 | |
| 1512 Provisions pour garanties données aux clients | 60 000 | |
| 164 Emprunts auprès des établissements de crédit | 1 400 000 | |
| 401 Fournisseurs | 520 000 | |
| 43 Sécurité sociale et autres organismes sociaux | 150 000 | |
| 44 État et autres collectivités publiques | 80 000 | |
| 211 Terrains | | 250 000 |
| 2131 Bâtiments | | 2 400 000 |
| 2154 Matériels industriels | | 3 100 000 |
| 31 Matières premières et fournitures | | 520 000 |
| 355 Produits finis | | 380 000 |
| 411 Clients | | 960 000 |
| 512 Banques | | 150 000 |
| 778 Autres produits exceptionnels (résultat de fusion) | | 830 000 |
| **Total** | **8 590 000** | **8 590 000** |

**A2 — Réception des actions ORVALIÈRE et de la soulte (0,5 pt).** Les actions sont reçues pour leur valeur d'échange (35 000 × 100 = 3 500 000 €) et ne sont détenues que le temps de leur attribution aux associés : elles transitent par le compte 503 Actions.

| Compte | Débit | Crédit |
|---|---:|---:|
| 503 Actions (35 000 actions ORVALIÈRE) | 3 500 000 | |
| 512 Banques (soulte) | 100 000 | |
| 467 Divers comptes débiteurs – ORVALIÈRE, compte d'apport | | 3 600 000 |

**A3 — Droits des associés (0,5 pt).** Le résultat de l'exercice clos par la fusion comprend le bénéfice de la période (60 000 €) et le résultat de fusion (830 000 €), soit 890 000 €, après virement du compte 778 au compte 120 (clôture des comptes de gestion : débit 778, crédit 120 pour 830 000 €). Les capitaux propres ainsi complétés (3 600 000 €) reviennent aux associés à proportion de leurs actions : 75 % pour CHAUMEROT Développement, 25 % pour les trois cadres.

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 1 200 000 | |
| 1041 Primes d'émission | 1 800 000 | |
| 1061 Réserve légale | 120 000 | |
| 120 Résultat de l'exercice – bénéfice (60 000 + 830 000) | 890 000 | |
| 119 Report à nouveau – solde débiteur | | 410 000 |
| 456 Associés – Opérations sur le capital (CHAUMEROT Développement) | | 2 700 000 |
| 456 Associés – Opérations sur le capital (trois cadres) | | 900 000 |

**A4 — Attribution des actions et de la soulte (0,5 pt).** CHAUMEROT Développement reçoit 26 250 actions et 75 000 € ; les cadres reçoivent 8 750 actions et 25 000 € (10 000 €, 8 000 € et 7 000 €).

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital (CHAUMEROT Développement) | 2 700 000 | |
| 456 Associés – Opérations sur le capital (trois cadres) | 900 000 | |
| 503 Actions (ORVALIÈRE) | | 3 500 000 |
| 512 Banques (soulte) | | 100 000 |

Après A1 à A4 et ce virement, tous les comptes de LAMÉLIANE sont soldés.

---

### 2.5 Écritures de base chez ORVALIÈRE au 31 mars 2027 (3,5 pts)

**A5 — Augmentation de capital et soulte due (1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (LAMÉLIANE) | 3 600 000 | |
| 101 Capital (35 000 × 40) | | 1 400 000 |
| 1042 Primes de fusion (3 600 000 – 1 400 000 – 100 000) | | 2 100 000 |
| 468 Divers comptes créditeurs – soulte à verser | | 100 000 |

**A6 — Réalisation des apports à la valeur réelle (1,75 pt).** Les éléments sont inscrits à leur valeur réelle, sans reprise des valeurs brutes ni des amortissements de LAMÉLIANE ; les éléments que l'absorbée ne comptabilisait pas (engagements de retraite, impôt différé) et le fonds commercial sont inscrits [V art. 744-1, F01 § 3.1 et § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 207 Fonds commercial | 430 000 | |
| 211 Terrains | 410 000 | |
| 2131 Bâtiments | 1 560 000 | |
| 2154 Matériels industriels | 1 520 000 | |
| 31 Matières premières et fournitures | 520 000 | |
| 355 Produits finis | 440 000 | |
| 411 Clients | 960 000 | |
| 512 Banques | 150 000 | |
| 1512 Provisions pour garanties données aux clients | | 60 000 |
| 1521 Provisions pour pensions et obligations similaires | | 100 000 |
| 1523 Provisions pour impôts | | 80 000 |
| 164 Emprunts auprès des établissements de crédit | | 1 400 000 |
| 401 Fournisseurs | | 520 000 |
| 43 Sécurité sociale et autres organismes sociaux | | 150 000 |
| 44 État et autres collectivités publiques | | 80 000 |
| 4561 Associés – Comptes d'apport en société (LAMÉLIANE) | | 3 600 000 |
| **Total** | **5 990 000** | **5 990 000** |

**A7 — Versement de la soulte (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 468 Divers comptes créditeurs – soulte à verser | 100 000 | |
| 512 Banques | | 100 000 |

Après A5 à A7, le compte 4561 est soldé ; le capital s'élève à 4 200 000 + 1 400 000 = 5 600 000 €, soit 140 000 actions de 40 €.

---

### 2.6 Écritures complémentaires chez ORVALIÈRE (3 pts)

**Dette réciproque : analyse (0,75 pt).** Avant la fusion, ORVALIÈRE devait 84 000 € à LAMÉLIANE (fournisseurs) et LAMÉLIANE détenait la créance correspondante (clients). Par l'apport, ORVALIÈRE reçoit cette créance, comprise dans les 960 000 € de clients : elle devient à la fois créancière et débitrice de la même obligation. La **confusion** éteint la créance et la dette [V C. civ. art. 1349, F01 § 8]. L'écriture d'annulation de cette opération réciproque, qui existe à la date de réalisation, est donc nécessaire ; elle n'a aucun effet sur le résultat ni sur les capitaux propres.

**A8 — Extinction de la dette et de la créance réciproques (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette envers LAMÉLIANE) | 84 000 | |
| 411 Clients (créance de LAMÉLIANE sur ORVALIÈRE reçue par l'apport) | | 84 000 |

**Frais de fusion : analyse (0,75 pt).** Les frais de fusion peuvent être inscrits à l'actif en frais d'établissement ou imputés sur la prime de fusion [V PCG art. 212-9, F01 § 7] ; ORVALIÈRE a choisi l'imputation. L'imputation se fait pour le montant net d'impôt [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 80 000 × 75 % = **60 000 €** sur la prime. Les frais étant déductibles du résultat fiscal 2027, l'économie d'impôt (80 000 × 25 % = 20 000 €) diminue la dette d'impôt sur les sociétés.

**A9 — Frais de fusion (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (80 000 × 75 %) | 60 000 | |
| 444 État – Impôts sur les bénéfices (80 000 × 25 %) | 20 000 | |
| 512 Banques | | 80 000 |

LAMÉLIANE n'ayant ni provisions réglementées ni subvention d'investissement, aucune reconstitution n'est à passer. La provision pour garanties est reprise dans l'écriture A6.

---

### 2.7 Note au président d'ORVALIÈRE (3 pts)

**a. Capitaux propres d'ORVALIÈRE juste après la fusion (1,25 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (140 000 actions × 40) | 4 200 000 | + 1 400 000 | 5 600 000 |
| Primes de fusion | 0 | + 2 100 000 – 60 000 | 2 040 000 |
| Réserve légale | 420 000 | | 420 000 |
| Autres réserves | 3 060 000 | | 3 060 000 |
| Report à nouveau | 120 000 | | 120 000 |
| **Total** | **7 800 000** | **+ 3 440 000** | **11 240 000** |

Contrôle : + 3 440 000 = apports (3 600 000) – soulte (100 000) – frais nets d'impôt (60 000). Barème : capital (0,25), prime de fusion (0,5), total et contrôle (0,5).

**b. Enjeux de l'opération (1,75 pt)**
- *Actionnaires d'ORVALIÈRE (0,75 pt).* La famille JOUVERNEY, par sa holding, passe de 70 % à 52,50 % mais garde la majorité. CHAUMEROT Développement devient le deuxième actionnaire (18,75 %) et les trois cadres de LAMÉLIANE détiennent 6,25 % : leur intérêt dans la réussite de l'usine de Saint-Claude est préservé. L'échange étant équitable, l'action vaut toujours 100 € et aucun actionnaire n'est appauvri. Les valeurs d'échange ne comprennent aucune valeur pour les déficits : si l'agrément est accordé, l'économie d'impôt profitera à tous les actionnaires d'ORVALIÈRE après la fusion.
- *Créanciers (0,5 pt).* Les capitaux propres augmentent de 3 440 000 € (+ 44,10 %) et les créanciers de LAMÉLIANE ont désormais ORVALIÈRE pour débitrice ; ORVALIÈRE supporte en contrepartie 1 400 000 € d'emprunts supplémentaires. Une partie de l'actif reçu est un fonds commercial de 430 000 €, dont la valeur dépend de la poursuite de l'activité. La trésorerie reçue (150 000 €) ne couvre pas tout à fait la soulte et les frais (180 000 €, dont 20 000 € récupérés en impôt). La dette de 84 000 € envers LAMÉLIANE disparaît par confusion.
- *Administration fiscale (0,5 pt).* Le régime de faveur reporte l'imposition : ORVALIÈRE réintégrera 16 000 € par an pendant 15 ans (constructions) et 24 000 € par an pendant 5 ans (matériels), imposera le profit de 60 000 € sur les produits finis lors de leur vente et conservera la valeur fiscale du terrain et du fonds commercial (nulle pour ce dernier) ; la provision pour impôts de 80 000 € traduit ces impositions futures. Les déficits de 520 000 € ne sont transférés que si l'agrément est accordé ; ORVALIÈRE pourrait alors les imputer en totalité sur son bénéfice fiscal 2027 de 900 000 €, qui n'excède pas 1 000 000 € [V CGI art. 209 I, F02 § 3] (ORVALIÈRE n'a aucun déficit propre et les déficits transférés sont imputables sur son bénéfice 2027 : annexe 2.5), soit une économie d'impôt de 520 000 × 25 % = **130 000 €**. L'administration vérifiera notamment la poursuite de l'activité de lamellé-collé pendant au moins trois ans.

---

### Réponses tolérées
- **2.1** : sens de l'opération justifié par la seule comparaison des droits de vote de JOUVERNEY Participations avant et après, quelle que soit la parité retenue (toutes laissent la majorité à JOUVERNEY Participations).
- **2.2** : présentation séparée des impôts différés passifs (105 000 €, base 420 000 €) et actifs (25 000 €, base 100 000 €), si le solde net de 80 000 € est retenu dans les apports.
- **2.3 c** : toute démarche qui établit que 7 pour 12 est la seule parité possible (essai des dénominateurs de 1 à 12, ou calcul du nombre minimal de 34 616 actions puis recherche d'un lot simple). Proposition de la parité exacte 3 pour 5 sans soulte, si elle est justifiée et que l'impossibilité d'une soulte significative est expliquée : 1,25 point sur 1,75 pour la proposition et le conseil.
- **2.4** : compte 261, 50 ou 508 au lieu de 503 pour les actions reçues ; écritures A2 et A4 remplacées par une seule écriture (débit 456, crédit 467), si le texte indique qu'ORVALIÈRE remet les actions et la soulte directement aux associés ; compte 431 et 444 ou 447 au lieu de 43 et 44.
- **2.5** : écritures A5 et A7 regroupées (soulte directement au crédit du 512) ; soulte portée au crédit d'un autre compte de tiers ; compte 431 et 444 ou 447 au lieu de 43 et 44.
- **2.6** : extinction de la dette réciproque présentée dans A6 (créances inscrites pour 876 000 €, fournisseurs d'ORVALIÈRE diminués de 84 000 €), si la confusion est expliquée ; frais en deux écritures (1042 / 512 pour 80 000 €, puis 444 / 1042 pour 20 000 €), ou passage préalable en 6226 Honoraires puis transfert sur la prime par le crédit du compte de charge, si la prime ne supporte que 60 000 €.
- **2.7 b** : toute idée pertinente et chiffrée pour chacune des trois parties prenantes.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion mal calculée : oubli de la soulte (prime de 2 200 000 €), ou prime calculée sur l'actif net comptable (2 770 000 – 1 400 000 – 100 000 = 1 270 000 €) au lieu de la valeur réelle des apports.
- `JUR-R05` Difficulté à s'adapter : contrôle apprécié au niveau des familles plutôt que des holdings ; reprise des amortissements de LAMÉLIANE dans A6 malgré l'évaluation à la valeur réelle ; dans les écritures de LAMÉLIANE, résultat de fusion omis (A1 déséquilibrée) ou soumis à l'impôt.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1, A3 et A6.
- `JUR-F07` Annexes mal exploitées : impôt différé calculé sur le terrain, le fonds commercial ou les déficits ; engagements de retraite oubliés, avec leur impôt différé actif (provision pour impôts de 105 000 € et fonds commercial de 355 000 €) ; créance réciproque de 84 000 € non éliminée ; frais imputés pour leur montant brut (prime finale de 2 020 000 €).
- Erreurs propres à ce cas :
  - plafond de la soulte calculé sur la valeur des apports (10 % × 3 600 000 = 360 000 €), sur la valeur d'échange des actions remises ou sur le nominal des actions LAMÉLIANE, au lieu du nominal des actions ORVALIÈRE attribuées ;
  - déficits de LAMÉLIANE réputés transférés de plein droit avec le régime de faveur, ou dispense d'agrément invoquée alors que le montant dépasse 200 000 € ;
  - usage des comptes 675 et 775, supprimés du PCG 2026, pour le résultat de fusion chez LAMÉLIANE.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 710-1, 710-2, 720-1, 730-1 | Champ du titre VII, définition de la fusion, inscription des apports, initiatrice et cible | [V] p. 81-82 | F01 § 1 |
| PCG art. 740-1, 741-1, 741-2, 742-1, 743-1 | Parité indépendante de l'évaluation des apports ; contrôle distinct ; fusion à l'endroit ; valeur réelle (cas 4) | [V] p. 82-84 | F01 § 1 et § 2 |
| PCG art. 744-1 ; comptes 207 et 1523 | Valeurs réelles des éléments identifiés, figurant ou non au bilan ; fonds commercial ; provision pour impôts | [V] p. 85, 134-135 | F01 § 3.1 et § 3.3 |
| Corrigé du sujet zéro, Q 2.4 | Méthode de l'impôt différé intégré aux apports ; aucun impôt différé sur l'écart résiduel | [V] p. imprimée 216 | F01 § 3.3 |
| C. com. L. 236-1 | Soulte limitée à 10 % de la valeur nominale des actions attribuées | [V] Légifrance | F01 § 4 |
| Corrigé du sujet zéro (parité) | Équité : valeur des titres remis + soulte = valeur des titres reçus | [V] p. imprimée 214 | F01 § 4 |
| PCG art. 513-5 ; compte 778 | Résultat exceptionnel lié à un événement majeur et inhabituel | [V] p. 42-43 ; p. 148 | F01 § 9 |
| Comptes 778 (résultat de fusion) et 503 (actions reçues par l'absorbée) | Écritures chez LAMÉLIANE | Convention de rédaction (hypothèse de l'annexe 2.4 pour le 778) | F01 § 9 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime de fusion, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion de la créance et de la dette réciproques | [V] | F01 § 8 |
| CGI art. 210 A-1, 210 A-2, 210 A-3 (a à e), 210 C-1 ; BOI-IS-FUS-10-10-10 § 10 et 20 ; BOI-IS-FUS-10-20-30 § 210 et 330 | Régime de faveur : exonération chez l'absorbée, provisions, engagements de l'absorbante, réintégration sur 15 et 5 ans, imposition du résultat de la dernière période | [V] | F02 § 1, § 2 et § 4 |
| CGI art. 209 I et 209 II | Transfert des déficits sur agrément, conditions a à d, dispense sous 200 000 €, imputation dans la limite de 1 000 000 € majorée de 50 % de l'excédent | [V] | F02 § 3 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Désignation d'un commissaire aux comptes dans une SNC ; droits des associés ; cadres d'exercice ; demande d'établissement de la liasse fiscale | `3.1.a` Cadres d'exercice professionnel ; `3.1.b` Nomination et cessation ; `3.1.c` Principes déontologiques | 4 |
| 3.2 Certification et assurance raisonnable ; acceptation et prise de connaissance ; bilan d'ouverture ; seuil de signification | `3.2.a` Notion d'audit et typologie des missions ; `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit ; `3.1.d` Appliquer la norme pertinente | 4 |
| 3.3 Cycle achats, fournisseurs et stocks : risques, assertions, procédures, refus d'une confirmation, dépréciation du lot C-17 | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit ; `3.2.b` Moyens d'action du CAC | 6 |
| 3.4 Évaluation des anomalies et de l'incertitude d'ouverture ; écritures ; opinion | `3.2.e` Portée des opinions ; `3.2.c` Caractère significatif ; `3.1.d` Appliquer la norme pertinente | 2,5 |
| 3.5 Responsabilités civile, pénale et disciplinaire du commissaire aux comptes | `3.1.e` Mise en cause de la responsabilité | 1,5 |
| 3.6 Rôle de l'EFRAG ; place des normes transversales dans une publication volontaire | `3.3.a` Contexte et architecture des normes de durabilité | 1,5 |
| 3.7 Double matérialité et horizons de temps ; faiblesses de l'analyse de la gérance | `3.3.b` Principes de construction du reporting | 4,5 |
| 3.8 Mission contractuelle d'assurance limitée ; objectifs et axes ; axe relatif au processus | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.1.b` Nomination (mission contractuelle du CAC) | 2 |
| 3.9 Procédures sur le processus de détermination des informations | `3.4.b` Démarche | 2,5 |
| 3.10 Conclusion sur l'axe relatif au processus et portée | `3.4.c` Portée des avis | 1,5 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Désignation du commissaire aux comptes ; cadres d'exercice ; liasse fiscale (4 pts)

**a. Obligation, organe, durée, fin de l'obligation ; droits de la holding (2 pts)**

*Obligation (0,75 pt)*
- Les SNC qui dépassent, **à la clôture d'un exercice**, deux des trois seuils (total du bilan 5 000 000 € ; chiffre d'affaires hors taxes 10 000 000 € ; 50 salariés en moyenne) sont tenues de désigner au moins un commissaire aux comptes [V L. 221-9 al. 2 ; D. 221-5 al. 1].
- Application :

| Seuil | 2024 | 2025 | 2026 |
|---|---|---|---|
| Total du bilan > 5 000 000 € | non (4 650 000) | **oui** (5 820 000) | **oui** (6 940 000) |
| CA HT > 10 000 000 € | non (8 920 000) | non (9 860 000) | **oui** (11 480 000) |
| Salariés > 50 | **oui** (71) | **oui** (78) | **oui** (85) |
| Seuils dépassés | 1 | **2** | 3 |

- En 2024, un seul seuil est dépassé : aucune obligation. À la clôture de 2025, deux seuils le sont : TRÉLAMONT doit désigner un commissaire aux comptes. Il est désigné par la décision qui statue sur les comptes de 2025 et certifie donc, pour la première fois, les comptes de **2026** [S, F09 § 8]. La forme de société en nom collectif, avec des associés indéfiniment responsables, ne dispense pas de cette obligation : c'est la réponse à la question n° 1 du gérant.

*Organe, durée et fin de l'obligation (0,5 pt)*
- Le commissaire aux comptes est désigné par l'assemblée générale ordinaire **ou l'organe analogue** [V L. 821-40 I]. Dans une SNC, ce sont les **associés**, par une décision collective prise dans les formes prévues pour leurs décisions [V L. 221-9 al. 1 ; S, F09 § 11]. C'est ce qu'ils ont fait le 10/06/2026, et non le gérant seul.
- Le mandat dure **six exercices**, 2026 à 2031. Il expire après la décision des associés qui statue sur les comptes de 2031 [V L. 821-44 al. 1]. La faculté de le limiter à trois exercices ne vaut pas pour une désignation imposée par le dépassement des seuils [V L. 821-46].
- Un suppléant n'est exigé que si le titulaire est une personne physique ou une société unipersonnelle [V L. 821-40 I al. 3] : HAUTMESNIL est une société qui compte plusieurs associés, dont Mme ROUGEVAL.
- L'obligation ne cessera que si TRÉLAMONT ne dépasse pas deux des trois seuils **pendant les deux exercices précédant l'expiration du mandat**, soit les deux derniers exercices du mandat, 2030 et 2031 [V D. 221-5 al. 2]. Une baisse du chiffre d'affaires ne suffirait pas : en 2026, le total du bilan et l'effectif dépassent à eux seuls les seuils.

*Ce que la holding aurait pu faire en 2025 (0,75 pt)*
- **Demande motivée** à la société : des associés représentant au moins **le tiers du capital** peuvent exiger la désignation d'un commissaire aux comptes, pour un mandat de **trois exercices** [V L. 221-9 al. 4]. La holding détient 7 200 parts sur 12 000, soit **60 %** : elle pouvait l'imposer seule, sans l'accord du gérant.
- **Demande en justice** : même si les seuils ne sont pas atteints, tout associé peut demander la nomination en justice [V L. 221-9 al. 3]. Le commissaire aux comptes est alors désigné par le président du tribunal de commerce, statuant selon la procédure accélérée au fond [V D. 221-5 al. 3].
- Une nomination volontaire par décision des associés était aussi possible [V L. 221-9 al. 1], mais elle supposait l'accord du gérant, qui est associé ; le détail des règles de majorité n'est pas attendu.

**b. Cadres d'exercice et demande n° 2 (2 pts)**

*Cadres d'exercice (0,75 pt)*

| | Expert-comptable | Commissaire aux comptes | Vérificateur des informations en matière de durabilité |
|---|---|---|---|
| Nature de l'intervention | Mission **contractuelle** : tenir, centraliser, arrêter et réviser les comptabilités [V ord. 45-2138 art. 2] ; lettre de mission [V décret 2012-432 art. 151] | Mission **légale** de certification des comptes, avec une **assurance raisonnable** [V L. 821-53 ; L. 821-2 III] ; prestations hors missions, sous lettre de mission [V L. 821-2 IV, R. 821-195] | Certification **légale** pour les entités tenues de publier, avec une **assurance limitée** [V L. 821-54 II ; LD 2026] ; pour une entité qui publie volontairement, mission **contractuelle** [S, F12 § 11] |
| Conditions d'exercice | Inscription au **tableau de l'ordre** : diplôme d'expertise comptable, honorabilité [V ord. art. 3] | Inscription sur la **liste tenue par la H2A** : stage, certificat d'aptitude ou diplôme d'expertise comptable ; serment [V L. 821-13 I, L. 821-14, L. 821-23] | Commissaire aux comptes inscrit sur une **liste spéciale** (stage de huit mois, épreuve de durabilité), ou auditeur d'un **organisme tiers indépendant** accrédité [V L. 821-13 II, L. 821-18, L. 822-1, L. 822-3] |
| Instances | **CROEC** et **CNOEC** [V ord. art. 1, 28, 31, 33] | **H2A**, **CNCC** et **CRCC** [V L. 820-1, L. 821-12] | **H2A** ; accréditation des organismes par le comité français d'accréditation [V L. 820-1, L. 822-3] |
| Indépendance | Indépendance d'esprit, compatible avec la tenue des comptes du client [V décret art. 145-146 ; S] | Condition de la mission, en réalité **et** en apparence ; aucun risque d'autorévision [V code de déontologie art. 5] | Même code de déontologie que le commissaire aux comptes [V L. 822-7] |

*Analyse de la demande n° 2 (0,75 pt)*
- Le gérant raisonne comme si HAUTMESNIL intervenait chez lui comme expert-comptable. Or, pour TRÉLAMONT, le cabinet n'intervient que comme **commissaire aux comptes**. Les règles d'indépendance du commissaire aux comptes s'appliquent à toute prestation qu'il rendrait à la société, même si cette prestation relève par nature du métier d'expert-comptable [V code de déontologie art. 5 ; L. 821-28 IV ; S, application].
- La liasse fiscale reprend le bilan et le compte de résultat que le cabinet certifie. Elle ne modifie pas ces comptes et le cabinet ne se prononce pas sur elle : le **risque d'autorévision** n'est pas direct [V code de déontologie art. 5 II ; S, application]. Il naîtrait si l'établissement de la liasse conduisait le cabinet à prendre des positions qui rejaillissent sur les comptes. L'apparence d'indépendance est aussi en cause : un tiers objectif, raisonnable et informé pourrait croire que le cabinet participe à l'établissement des comptes [V A. 821-55 § 03, 11 ; S, application].
- TRÉLAMONT n'est pas une entité d'intérêt public : aucune liste fermée de services interdits ne s'applique. Mais le cabinet doit vérifier, avant d'accepter une prestation, qu'elle ne compromet pas sa mission de certification. Il ne peut pas l'accepter s'il existe un risque d'autorévision sans mesure de sauvegarde appropriée [V A. 821-55 § 15, 23-30 ; L. 821-28 IV]. Le cabinet doit donc conduire l'analyse des risques et des sauvegardes. Un argument plaide pour la prudence : même confiée à une équipe distincte, la liasse resterait l'œuvre du cabinet [S, application].

*Réponse de Mme ROUGEVAL (0,5 pt)*
- Réponse retenue : elle décline la demande, par prudence. La liasse continue d'être établie par COMBELLE : l'expert-comptable qui tient la comptabilité peut donner des consultations fiscales aux entreprises dans lesquelles il assure des missions comptables permanentes ou habituelles [V ord. 45-2138 art. 22] ; COMBELLE établit déjà les déclarations fiscales de la société (présentation).
- Elle rappelle la répartition des rôles : la gérance arrête les comptes, COMBELLE les établit, HAUTMESNIL les certifie sans s'immiscer dans la gestion [V L. 821-54 I].

**Réponses tolérées**
- Une comparaison rédigée plutôt qu'un tableau, si les critères sont traités.
- L'acceptation de la prestation sous des mesures de sauvegarde précises (liasse établie après l'arrêté des comptes et sans intervention sur ceux-ci, équipe distincte, information des associés), si le candidat conduit l'analyse des risques et des sauvegardes : note entière.
- L'omission du suppléant.

**Erreurs fréquentes**
- Laisser le gérant désigner le commissaire aux comptes, ou retenir un mandat de trois exercices pour une désignation imposée par les seuils (`JUR-A04`).
- Croire qu'une SNC échappe à l'obligation parce que ses associés répondent des dettes sociales, ou que l'obligation cesse dès la première année sous les seuils (`JUR-A05`).
- Confondre l'indépendance du commissaire aux comptes et celle de l'expert-comptable : accepter la liasse au motif que le cabinet est aussi expert-comptable (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 221-9, D. 221-5 | Désignation dans une SNC : seuils, fin de l'obligation, demande d'un associé, tiers du capital | [V] | F09 § 3.3, § 11 |
| C. com. L. 821-40, L. 821-44, L. 821-46 | Organe, suppléant, durée du mandat | [V] ; application à la SNC : [S] | F09 § 3.4-3.5, § 11 |
| Ord. 45-2138 art. 2, 3, 22 ; décret 2012-432 art. 145-146, 151 ; C. com. L. 820-1, L. 821-12 à L. 821-14, L. 821-18, L. 821-23, L. 822-1, L. 822-3, L. 822-7 | Cadres d'exercice des trois professionnels | [V] | F09 § 1-4 ; F10 § 3, 4.3 |
| Code de déontologie art. 5 ; L. 821-28 IV ; A. 821-55 § 03, 11, 15, 23-30 ; L. 821-54 I | Autorévision ; sauvegardes ; non-immixtion | [V] ; application : [S] | F10 § 2.1, 3, 5, 12 ; F09 § 6 |

### 3.2 Certification, premier mandat, bilan d'ouverture et seuil (4 pts)

**a. Objectif et assurance ; différence avec la mission sur la durabilité (1 pt)**
- **Objectif (0,25 pt)** : le commissaire aux comptes certifie, en justifiant de ses appréciations, que les comptes annuels sont réguliers et sincères et donnent une image fidèle du résultat, de la situation financière et du patrimoine ; il formule une **opinion** après un **audit des comptes** [V L. 821-53 al. 1 ; NEP principes § 01].
- **Assurance raisonnable (0,25 pt)** : assurance élevée, mais non absolue, que les comptes pris dans leur ensemble ne comportent pas d'anomalies significatives. Les limites de l'audit tiennent aux sondages et au fait que les éléments collectés conduisent davantage à des présomptions qu'à des certitudes [V NEP principes § 08-09]. L'audit ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].
- **Différences avec la mission sur la durabilité (0,5 pt)** :
  - *fondement* : la certification est une mission légale ; la vérification des informations de TRÉLAMONT est une **prestation contractuelle**, définie par la lettre de mission, car la société n'est pas tenue de publier [V L. 821-2 III-IV ; annexe 3.7] ;
  - *objet* : les comptes annuels d'un côté ; de l'autre, le processus de détermination des informations et leur conformité aux ESRS ;
  - *assurance* : raisonnable, conclusion formulée de façon positive, d'un côté ; **limitée**, conclusion de forme négative, de l'autre [V LD 2026, niveau d'assurance ; F13 § 2.3] ;
  - *rapport* : deux rapports distincts (annexe 3.7).

**b. Acceptation et prise de connaissance (1 pt)**

*Acceptation et lettre de mission (0,5 pt)*
- Le cabinet vérifie et consigne son **indépendance** et les **ressources** nécessaires [V L. 821-4 II]. Il analyse les missions et prestations rendues auparavant à l'entité et aux personnes liées [V code de déontologie art. 22] : HAUTMESNIL n'était jamais intervenu pour TRÉLAMONT, ses associés ou BÂTIVALE (annexe 3.1).
- Il n'a pas de prédécesseur à contacter : les comptes de TRÉLAMONT n'ont jamais été contrôlés. Il devra en revanche contrôler lui-même le bilan d'ouverture (question c).
- Il établit la **lettre de mission** la première année du mandat, avant le début des travaux : objectif et étendue de la mission, calendrier, accès aux informations, déclarations écrites demandées, budget d'honoraires [V NEP lettre de mission § 3-8].

*Prise de connaissance (0,5 pt)*
- Elle a pour objet de comprendre l'entité, son environnement et les procédures qui concourent à l'information financière, afin d'**identifier et d'évaluer le risque d'anomalies significatives** et de planifier la mission [V NEP risques § 21-44 ; NEP planification].
- Application : fabrication de menuiseries en forte croissance (chiffre d'affaires + 16,4 % en 2026) ; dépendance à un fournisseur de chêne (70 % des volumes) ; stocks importants de bois, en partie exposés aux intempéries, mesurés par une seule personne ; sorties de bois saisies à la main jusqu'au 28/02/2026 ; inventaire physique une fois par an ; factures enregistrées à leur date par un expert-comptable extérieur ; gérant associé, seul dirigeant ; premier exercice certifié. Ces éléments orientent la mission vers le cycle achats, fournisseurs et stocks.

**c. Bilan d'ouverture (1,5 pt)**

*Application de la norme (0,5 pt)* [V NEP bilan d'ouverture § 01-11]
- La première année de son mandat, Mme ROUGEVAL doit vérifier que le bilan d'ouverture ne contient pas d'anomalies significatives ayant une incidence sur les comptes de 2026. Un stock d'ouverture erroné fausse la variation des stocks, donc le résultat de 2026.
- Les comptes de 2025 n'ont pas été certifiés : aucune présomption de régularité ne joue, et il n'existe aucun dossier de prédécesseur. Elle s'appuie sur ses travaux de 2026 et sur des procédures complémentaires.
- Pour les autres matières, les en-cours et les produits finis (785 000 €), les procédures de 2026 suffisent : consommations du premier trimestre, fiches de fabrication, ventes de janvier et taux de marge brute.
- Pour le bois de chêne (1 400 000 €), les fiches de comptage du 31/12/2025 n'ont pas été conservées. La norme propose d'observer un inventaire en cours d'exercice et de le rapprocher des soldes d'ouverture : c'est l'inventaire du 30/06/2026.

*Reconstitution (0,5 pt)*

| Stock de bois | Montant |
|---|---:|
| Stock compté au 30/06/2026 (inventaire observé) | 1 296 000 |
| − Entrées du 01/01 au 30/06/2026 | − 1 734 000 |
| + Sorties du 01/01 au 30/06/2026 | + 1 812 000 |
| = Stock théorique au 01/01/2026 | **1 374 000** |
| Stock du bilan d'ouverture | 1 400 000 |
| **Écart non expliqué** | **26 000** |

*Conclusion (0,5 pt)*
- L'écart représente 1,9 % du stock de bois d'ouverture et 41,9 % du seuil de signification. Il peut provenir d'une surévaluation du stock d'ouverture ou de sorties non enregistrées en janvier et février : les bons manuels ne permettent pas de trancher. Il reste donc **non vérifiable** : c'est une limitation partielle [V NEP bilan d'ouverture § 12].
- Si le stock d'ouverture était surévalué de 26 000 €, le résultat de 2025 serait surévalué d'autant, et celui de 2026 **sous-évalué** d'autant, par une variation des stocks trop forte. Le stock de clôture n'est pas touché, puisqu'il a été compté au 31/12/2026.
- La norme demande aussi de vérifier la permanence des méthodes [V § 04] : le taux forfaitaire de 25 % appliqué aux lots déclassés est une méthode « constante », mais il faut en vérifier la conformité au PCG (question 3.3 c).
- L'incidence sur l'opinion est appréciée à la question 3.4. Les comptes de 2025 n'ayant pas été certifiés, le rapport devra le mentionner [V NEP bilan d'ouverture § 15].

**d. Seuil de signification (0,5 pt)**
- Le seuil est le montant au-delà duquel les décisions économiques ou le jugement fondés sur les comptes sont susceptibles d'être influencés. Il relève du jugement professionnel et se détermine à partir de critères pertinents (résultat courant, résultat net, chiffre d'affaires, capitaux propres) choisis selon la structure des comptes et les attentes des utilisateurs. Aucun pourcentage n'est imposé par les normes [V NEP caractère significatif § 6, 10, 17-18].
- Le résultat courant est un critère pertinent :
  - les utilisateurs principaux sont les associés, qui se partagent le résultat et répondent indéfiniment des dettes sociales, ainsi que BÂTIVALE et la banque ;
  - ce résultat est positif et régulier (860 000 €, 1 080 000 € puis 1 240 000 €) : il ne rend pas le seuil instable.
- 5 % de 1 240 000 € donnent 62 000 €, soit 0,5 % du chiffre d'affaires et 2,6 % des stocks nets. Le seuil de planification, plus bas (46 500 €), réduit le risque que les anomalies non détectées et non corrigées dépassent, en cumul, le seuil de signification [V NEP caractère significatif § 7, 20]. Le seuil des anomalies manifestement insignifiantes (3 100 €) fixe le montant à partir duquel une anomalie est récapitulée [V NEP anomalies § 8].

**Réponses tolérées**
- Un seuil spécifique plus bas pour les stocks, s'il est justifié par leur poids (34,7 % du total du bilan) [V NEP caractère significatif § 15-16].
- La présentation de l'écart de 26 000 € comme une « incertitude » plutôt que comme une limitation, si le candidat en tire la même incidence sur l'opinion.

**Erreurs fréquentes**
- Considérer que le bilan d'ouverture n'a pas à être contrôlé parce qu'il n'est pas couvert par le mandat (`JUR-A05`).
- Conclure que l'écart d'ouverture surévalue le résultat de 2026, alors qu'il le sous-évaluerait (`JUR-F02`).
- Présenter le taux de 5 % comme une règle des normes (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-55, L. 821-2 III-IV ; NEP principes § 01, 08-09 ; LD 2026 | Certification ; assurance raisonnable et limitée | [V] | F11 § 1 ; F13 § 2.3 |
| C. com. L. 821-4 II ; code de déontologie art. 22 ; NEP lettre de mission § 3-8 ; NEP risques § 21-44 | Acceptation ; lettre de mission ; prise de connaissance | [V] | F11 § 5, 7 |
| NEP bilan d'ouverture § 01-15 | Bilan d'ouverture d'un premier exercice certifié | [V] | F11 § 15.1 |
| NEP caractère significatif § 6-7, 10, 15-20 ; NEP anomalies § 8 | Seuils | [V] | F11 § 4.2, 14 |

### 3.3 Cycle achats, fournisseurs et stocks (6 pts)

**a. Risques d'anomalies significatives et assertions (2,5 pts)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41 ; NEP éléments probants § 9]

*Évaluation du risque (0,5 pt)* : le **risque inhérent** est élevé.
- Les stocks représentent 34,7 % du total du bilan (2 407 200 € sur 6 940 000 €).
- Leur mesure est difficile : piles en extérieur cubées par une seule personne, séchoirs inaccessibles pendant les cycles, lots déclassés dont l'évaluation relève d'une **estimation** de la direction. Le taux forfaitaire de 25 % et le refus du gérant de modifier ses comptes sont des indices de biais.
- Les achats sont concentrés : VERDELLAT fournit 70 % du chêne et représente 44,0 % des achats.
- Les procédures de l'entité sont faibles : sorties manuelles jusqu'à fin février, un seul inventaire par an, factures enregistrées à leur date par un cabinet extérieur, sans rapprochement avec les réceptions ni factures non parvenues à la clôture.
- S'y ajoutent la croissance et le premier exercice certifié. Sans test de l'efficacité des procédures, le risque au niveau des assertions correspond au risque inhérent [V NEP risques § 41] : procédures de substance et éléments externes [V NEP réponses § 03-13].

*Risques et assertions (2 pts : 0,25 pt par couple pertinent, dans la limite de huit)*

| Élément | Risque | Assertion |
|---|---|---|
| Stocks de bois | Piles absentes ou volumes surestimés (cubage par une seule personne, séchoirs non ouverts) | **Existence** |
| | Bois déposé sur le parc mais appartenant encore au fournisseur, ou bois livré non compté | **Droits et obligations** ; **exhaustivité** |
| | Lots fendus ou bleuis insuffisamment dépréciés (taux forfaitaire) | **Évaluation et imputation** |
| Produits finis et en-cours | Coût de production qui inclut des coûts non attribuables à la production, ou qui omet des frais de production (énergie des séchoirs, frais généraux de production) | **Évaluation et imputation** |
| Stock d'ouverture | Stock du 01/01/2026 non vérifié, qui fausse la variation des stocks de 2026 | **Existence** et **évaluation** à l'ouverture ; **mesure** de la variation des stocks |
| Achats | Réceptions de fin décembre facturées en janvier et enregistrées en 2027 | **Séparation des exercices** |
| | Quantités ou prix facturés différents des volumes reçus et du contrat | **Mesure** |
| Dettes fournisseurs | Factures non parvenues non comptabilisées, en particulier chez VERDELLAT, gros fournisseur au solde faible | **Exhaustivité** |
| Annexe | Méthodes d'évaluation des stocks et de dépréciation non décrites | **Présentation et intelligibilité** |

**b. Procédures et refus du gérant (2,5 pts)**

*Observation de l'inventaire physique (0,5 pt)* [V NEP applications spécifiques § 3-6 ; NEP éléments probants § 10]
- Les stocks étant significatifs, le commissaire aux comptes assiste à l'inventaire pour collecter des éléments sur leur **existence** et leur **état physique**. Il vérifie que les procédures de comptage définies par la direction sont appliquées et apprécie leur fiabilité.
- Apports : le recomptage de huit piles (écarts inférieurs à 1 %) conforte le cubage, malgré l'absence de second compteur. Pour les séchoirs, faute d'accès, le cabinet rapproche les fiches de chargement des sorties du parc et contrôle les volumes au déchargement, en janvier 2027. L'observation a révélé l'**état** du lot C-17 (question c). Elle a permis de relever le dernier bon de réception compté (n° 26-1307), point de départ du test de séparation.

*Test de séparation des exercices (0,75 pt)*
- Objet : vérifier que les achats et les dettes sont rattachés à l'exercice de la réception des biens, puisque la propriété est transférée à la livraison (assertions de **séparation des exercices** et d'**exhaustivité**). Le cabinet rapproche les bons de réception des jours qui encadrent la clôture, l'inventaire et l'enregistrement des factures.

| Bon | Réception | Facture enregistrée en | Conclusion |
|---|---|---|---|
| 26-1296, 26-1302 | Décembre 2026 | Décembre 2026 | Correct |
| **26-1307** | **30/12/2026**, chêne compté dans le stock | **Janvier 2027** (facture du 05/01/2027) | **Anomalie** : charge de 2026 non comptabilisée |
| 27-0002 | 04/01/2027 (profilés encore chez ALUFORM Est le 31/12) | Janvier 2027 | Correct : la facture datée du 31/12/2026 ne rend pas TRÉLAMONT propriétaire avant la réception |
| 27-0005 | 06/01/2027 | Janvier 2027 | Correct |

- Le chêne reçu le 30/12/2026 figure dans le stock de clôture, mais son achat n'est pas comptabilisé : il manque une **facture non parvenue** de 48 × 725 = **34 800 € HT**, soit 41 760 € TTC. Le résultat est surévalué de 34 800 € et les dettes fournisseurs sont sous-évaluées de 41 760 €.
- L'argument du gérant est sans portée : la date de la facture ne détermine pas l'exercice de rattachement. La charge relève de 2026, exercice de la réception, et la dette existe dès cette date.

*Choix des fournisseurs (0,25 pt)*
- Pour tester l'**exhaustivité**, le cabinet choisit les fournisseurs d'après le **volume des achats** et non d'après les soldes. VERDELLAT représente 44,0 % des achats mais 4,1 % des soldes, en raison de son délai de dix jours. Une dette omise y passe facilement inaperçue. Le cabinet utilise une demande de confirmation **ouverte** : le fournisseur indique lui-même le solde et le détail des factures et livraisons [V NEP confirmations § 4-6].

*Refus du gérant (1 pt)*
- **Maîtrise de la procédure et moyens d'action (0,25 pt)** : le commissaire aux comptes a la maîtrise de la sélection des tiers interrogés, de la rédaction, de l'envoi et de la réception des demandes [V NEP confirmations § 9]. Le gérant ne peut pas choisir à sa place les fournisseurs à interroger. Le commissaire aux comptes se fait communiquer sur place toutes les pièces utiles, notamment les contrats et documents comptables [V L. 821-60]. Il peut recueillir des informations auprès des tiers qui ont accompli des opérations pour le compte de l'entité ; la communication de pièces détenues par des tiers suppose une autorisation de justice [V L. 821-61 al. 2]. Un fournisseur qui vend à TRÉLAMONT n'entre pas clairement dans ce cas : la demande de confirmation reste une technique de contrôle, qui suppose la coopération du tiers et l'accord de principe de l'entité [S]. Refuser la communication de pièces serait un délit d'obstacle [V L. 821-6 3°] ; ce n'est pas le cas ici, puisque le gérant offre les factures et le contrat [S].
- **Examen du motif et conséquences (0,5 pt)** : face à une opposition, le commissaire aux comptes examine si le refus se fonde sur des motifs valables et collecte des éléments sur ces motifs [V § 10]. Ici, le motif est faible : une demande de confirmation est une démarche courante de fin d'exercice, qui ne suppose aucune difficulté ni aucune contestation. De plus, le fournisseur visé est celui dont le solde est le plus faible par rapport aux achats. Le cabinet peut proposer au gérant de joindre à la demande une lettre d'accompagnement qui en précise la nature [S].
  Si le refus est jugé fondé, le cabinet met en œuvre des **procédures alternatives** [V § 11]. S'il ne l'est pas, il en tire les conséquences éventuelles dans son rapport [V § 12] : si aucune procédure ne lui apporte des éléments suffisants, il en résulte une limitation [V NEP rapport § 11]. Ici, le motif est jugé faible, donc le refus non fondé.
- **Procédures alternatives (0,25 pt)** :
  - rapprochement des bons de réception de VERDELLAT de 2026 (volumes en m³) avec les factures enregistrées et le prix du contrat (2 860 000 € au prix des livraisons de fin d'année, 725 € par m³, soit environ 3 945 m³) ;
  - examen des factures de VERDELLAT reçues en janvier et en février 2027 et de leur bon de réception : c'est ce contrôle qui fait apparaître la facture du 05/01/2027 pour la livraison du 30/12/2026 ;
  - rapprochement du solde avec le relevé de compte adressé par VERDELLAT à TRÉLAMONT ;
  - lecture du contrat annuel pour identifier les volumes engagés et les conditions de prix.
- Ces procédures apportent néanmoins des éléments suffisants : le rapport ne comporte pas de limitation à ce titre, mais le refus est documenté et signalé à la gérance. Elles confirment l'anomalie de séparation.

**c. Dépréciation du lot C-17 (1 pt)**

*Calcul (0,5 pt)*
- Le chef d'atelier indique que le lot ne peut plus entrer dans la fabrication : il n'a pas de valeur d'usage propre. Sa **valeur actuelle** est sa valeur vénale, nette des coûts de sortie [V PCG art. 214-5, 214-6, rappelés dans l'annexe 3.4].

| Lot C-17 (120 m³) | Calcul | Montant |
|---|---|---:|
| Coût d'acquisition | 120 × 760 | 91 200 |
| Valeur actuelle | 120 × (170 − 20) | 18 000 |
| **Dépréciation nécessaire** | 91 200 − 18 000 | **73 200** |
| Dépréciation comptabilisée | 25 % × 91 200 | 22 800 |
| **Insuffisance** | 73 200 − 22 800 | **50 400** |

*Analyse (0,5 pt)*
- La dépréciation doit ramener le lot à sa valeur actuelle, appréciée lot par lot à la clôture. Un taux forfaitaire, même appliqué de façon constante, ne satisfait pas cette règle dès qu'il s'en écarte : ici, la perte de valeur atteint 80,3 % du coût. La permanence des méthodes ne justifie pas une évaluation erronée [S, application].
- L'hypothèse de « pièces cachées » est contredite par le chef d'atelier et ne repose sur aucun projet. L'offre écrite de BOISSARD, seule offre obtenue, est le meilleur élément sur la valeur du lot dans l'état où il se trouvait au 31/12/2026.
- Incidence : le stock et le résultat sont surévalués de **50 400 €**, soit 81,3 % du seuil. L'anomalie, inférieure au seuil, est supérieure au seuil des anomalies manifestement insignifiantes. Elle est donc récapitulée et le cabinet en demande la correction [V NEP anomalies § 8, 11].

**Réponses tolérées**
- D'autres couples risque-assertion pertinents tirés des annexes, par exemple la **classification** entre matières premières et autres approvisionnements.
- La présentation du test de séparation en partant des factures de janvier 2027 plutôt que des bons de réception, si la conclusion est la même.
- L'acceptation du motif du gérant comme fondé, si le candidat en déduit des procédures alternatives suffisantes : 0,25 pt sur 0,5 pour l'examen du motif et ses conséquences.

**Erreurs fréquentes**
- Confondre réalité (flux) et existence (solde), ou exhaustivité et séparation des exercices (`JUR-A01`).
- Choisir les fournisseurs à interroger d'après les soldes les plus élevés pour tester l'exhaustivité (`JUR-A05`).
- Accepter le refus sans examiner son motif, ou y voir d'emblée un délit d'obstacle (`JUR-A05`).
- Déprécier le lot sur sa valeur brute de revente (170 €) sans déduire les frais d'enlèvement, ou reprendre le taux de 25 % (`JUR-F02`, `JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 10-13 ; NEP risques § 02, 39-41 ; NEP réponses § 03-13 | Composantes du risque ; procédures de substance | [V] | F11 § 4.1, 5 |
| NEP éléments probants § 9-10 ; NEP applications spécifiques § 3-6 | Assertions ; techniques ; inventaire physique | [V] | F11 § 4.3, 6, 15.2 |
| NEP confirmations § 4-6, 9-12 ; C. com. L. 821-6 3°, L. 821-60, L. 821-61 | Confirmation ; refus de la direction ; moyens d'action | [V] ; application : [S] | F11 § 2, 6.3, 13.3, 15.2 ; F09 § 5 |
| PCG art. 213-31 (p. 21), 214-5 et 214-6 (p. 23) | Coût d'acquisition ; dépréciation ; valeur actuelle et valeur vénale | 214-5 et 214-6 : [V] ; 213-31 : [V] pour les fragments lisibles | F11 § 15.3 |
| NEP anomalies § 8, 11 | Récapitulation ; demande de correction | [V] | F11 § 14 |

### 3.4 Anomalies, écritures et opinion (2,5 pts)

**a. Récapitulation et caractère significatif (1 pt)** [V NEP anomalies § 8, 12, 14 ; NEP bilan d'ouverture § 12-14]

| Anomalie | Résultat 2026 | Stocks | Dettes fournisseurs | TVA à récupérer |
|---|---:|---:|---:|---:|
| Dépréciation insuffisante du lot C-17 | − 50 400 | − 50 400 | — | — |
| Facture non parvenue de VERDELLAT omise | − 34 800 | — | + 41 760 | + 6 960 |
| **Total des corrections** | **− 85 200** | **− 50 400** | **+ 41 760** | **+ 6 960** |

- Chaque anomalie est inférieure au seuil (81,3 % et 56,1 %), mais leur **cumul**, 85 200 €, représente **137,4 %** du seuil de 62 000 € et 6,9 % du résultat courant. Les anomalies non corrigées s'apprécient individuellement et en cumulé : elles sont **significatives**.
- Leur nature aggrave le constat : elles vont toutes deux dans le sens d'un résultat plus élevé, et l'une résulte d'une estimation de la direction que le gérant refuse de revoir.
- **Incertitude d'ouverture** : 26 000 €, soit 41,9 % du seuil. Elle n'est pas significative à elle seule. Elle jouerait, si elle se confirmait, dans le sens d'une **sous-évaluation** du résultat de 2026. Une limitation ne se compense pas avec des anomalies relevées : elle s'apprécie à part, et ne remet pas en cause la conclusion sur les deux anomalies [S, application].
- Le cabinet communique les anomalies au gérant et en demande la correction [V NEP anomalies § 11, 15-16].

**b. Écritures de correction au 31/12/2026 (0,5 pt : 0,25 pt par écriture complète)**

X1 – Facture non parvenue de VERDELLAT Chênes (bon de réception n° 26-1307, 48 m³ × 725 €)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 601 | Achats stockés - Matières premières et fournitures | 34 800 | |
| 44586 | Taxes sur le chiffre d'affaires sur factures non parvenues | 6 960 | |
| 408 | Fournisseurs - Factures non parvenues | | 41 760 |

Le stock de clôture comprend déjà les 48 m³ comptés : seule la charge d'achat et la dette manquent.

X2 – Dépréciation complémentaire du lot de chêne C-17 (73 200 − 22 800)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 68173 | Dotations pour dépréciations des actifs circulants - Stocks et en-cours | 50 400 | |
| 391 | Dépréciations des matières premières et fournitures | | 50 400 |

Après correction : résultat courant de 1 154 800 € ; stocks nets de 2 356 800 €.

**c. Opinion (1 pt)**
- **Si la gérance corrige (0,25 pt)** : aucune anomalie significative ne demeure et la seule limitation, de 26 000 €, n'est pas significative. Mme ROUGEVAL formule une **certification sans réserve** [V NEP rapport § 08 ; C. com. R. 821-180]. Elle obtient une **déclaration écrite** du gérant [V NEP déclarations écrites § 6-7].
- **Si la gérance ne corrige pas (0,5 pt)** :
  - les anomalies significatives ne sont pas corrigées ; leurs incidences sont **clairement circonscrites** (deux postes, montants chiffrés) et une réserve suffit à éclairer l'utilisateur. L'opinion est une **certification avec réserve pour désaccord**, et non un refus de certifier [V NEP rapport § 09-10, 12] ;
  - dans la partie relative au fondement de l'opinion, le rapport expose le désaccord et en quantifie les incidences : résultat et capitaux propres surévalués de 85 200 €, dont stocks surévalués de 50 400 € ; dettes fournisseurs sous-évaluées de 41 760 € [V NEP rapport § 06, 10]. Les motifs sont communiqués au préalable au gérant et aux associés [V NEP rapport § 06 ; L. 821-63 I] ;
  - la limitation de 26 000 € ne justifie pas, en elle-même, une réserve pour limitation.
- **Mentions propres au premier exercice certifié (0,25 pt)** : dans les deux cas, le rapport mentionne que les comptes de 2025 n'ont pas été certifiés par un commissaire aux comptes [V NEP bilan d'ouverture § 15]. Mme ROUGEVAL peut faire porter la justification de ses appréciations sur l'évaluation des stocks et sur le contrôle du bilan d'ouverture [V NEP rapport § 15 ; S, application].

**Réponses tolérées**
- Une écriture X1 au compte 4081 « Fournisseurs », sous-compte du 408.
- Une dépréciation globale du lot (reprise de 22 800 € et dotation de 73 200 €), si l'effet net est de 50 400 €.
- Une réserve pour désaccord qui évoque aussi la limitation d'ouverture, si le candidat précise qu'elle n'est pas significative seule.

**Erreurs fréquentes**
- Conclure à une certification sans réserve parce que chaque anomalie est inférieure au seuil, sans apprécier leur cumul (`JUR-A02`, `JUR-A06`).
- Ajouter l'incertitude d'ouverture aux anomalies pour atteindre le seuil, ou l'en déduire (`JUR-A02`).
- Proposer un refus de certifier, ou une réserve sans quantifier les incidences (`JUR-A02`).
- Passer l'achat omis au compte de variation des stocks, alors que le stock compté est exact (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP anomalies § 8, 11-12, 14-16 | Récapitulation, cumul, nature, communication | [V] | F11 § 14 |
| NEP bilan d'ouverture § 12-15 | Incidence d'une limitation sur l'ouverture ; mention des comptes non certifiés | [V] | F11 § 15.1 |
| NEP rapport § 06, 08-12, 15 ; C. com. R. 821-180, L. 821-63 I ; NEP déclarations écrites § 6-7 | Opinions ; réserve pour désaccord ; justification des appréciations | [V] | F11 § 8, 12.3 |
| Liste des comptes du PCG 2026 : 391, 408, 44586, 601, 68173 | Écritures | [V] | F11 § 15.3 |

### 3.5 Responsabilités du commissaire aux comptes (1,5 pt)

- **Responsabilité civile (0,5 pt)** : le commissaire aux comptes répond, à l'égard de l'entité et des tiers, des conséquences dommageables de ses **fautes et négligences**, réparées par des **dommages-intérêts** [V L. 821-37 al. 1]. Il faut une faute, un préjudice et un lien de causalité [S, droit commun].
  - Le commissaire aux comptes ne « garantit » pas les stocks. Il exprime une opinion avec une assurance raisonnable, non absolue, fondée sur des sondages [V NEP principes § 08-09]. L'établissement des comptes et l'évaluation des stocks incombent à la gérance [V L. 821-54 I].
  - La responsabilité indéfinie des associés est la conséquence de la forme sociale, et non un préjudice causé par le cabinet. Un associé qui voudrait agir devrait prouver une faute du cabinet et un préjudice qui en résulte directement [S].
  - Prescription : trois ans à compter du fait dommageable ou, s'il a été dissimulé, de sa révélation [V L. 821-38, L. 225-254].
- **Responsabilités pénale et disciplinaire (0,5 pt)** :
  - la responsabilité pénale sanctionne des infractions par l'amende et l'emprisonnement : par exemple, donner ou confirmer des **informations mensongères** sur la situation de la société (cinq ans, 75 000 €) [V L. 821-9]. Elle supposerait que le cabinet certifie sciemment des stocks qu'il sait surévalués ;
  - la responsabilité disciplinaire sanctionne un manquement aux conditions légales d'exercice, une **négligence grave** ou un fait contraire à l'honneur ou à la probité. Les sanctions vont de l'avertissement à la radiation, avec des sanctions pécuniaires, et sont prononcées par la **commission des sanctions de la H2A** [V L. 821-70 I, L. 821-71, L. 821-79]. Ne pas assister à l'inventaire de stocks significatifs, ou certifier sans réserve des comptes non corrigés, pourrait en relever.
- **Risque réel (0,5 pt)** : il est **faible** si le cabinet maintient sa démarche :
  - il a assisté aux inventaires du 30/06 et du 31/12/2026, reconstitué le stock d'ouverture, recalculé la dépréciation, testé la séparation des exercices et mis en œuvre des procédures alternatives ;
  - il documente ces travaux, ce qui fonde sa défense [V NEP documentation § 04-08] ;
  - il exprime une réserve si les comptes ne sont pas corrigés, et signale que les comptes de 2025 n'ont pas été certifiés.
  
  Le risque deviendrait réel s'il cédait au gérant en certifiant sans réserve. La menace de Mme MOUCHERET ne doit pas influencer l'opinion : l'impartialité l'interdit [V code de déontologie art. 4]. Elle rejoint d'ailleurs l'intérêt de la holding à des comptes corrigés.

**Réponses tolérées**
- La responsabilité disciplinaire présentée sous le nom de « responsabilité professionnelle ».
- L'absence de la prescription, si les trois conditions de la responsabilité civile sont appliquées au cas.

**Erreurs fréquentes**
- Confondre les trois responsabilités ou leurs sanctions (`JUR-A01`).
- Présenter le commissaire aux comptes comme garant de l'exactitude des stocks (`JUR-A05`, `JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-37, L. 821-38, L. 225-254, L. 821-54 I ; NEP principes § 08-09 | Responsabilité civile ; non-immixtion ; assurance raisonnable | [V] ; conditions : [S] | F09 § 6, 7.1 ; F11 § 1 |
| C. com. L. 821-9, L. 821-70, L. 821-71, L. 821-79 | Responsabilités pénale et disciplinaire | [V] | F09 § 7.2-7.3 |
| NEP documentation § 04-08 ; code de déontologie art. 4 | Dossier ; impartialité | [V] | F11 § 7 ; F10 § 2.1 |

---

### Partie B – Durabilité (12 points)

### 3.6 Rôle de l'EFRAG ; normes transversales (1,5 pt)

- **Rôle de l'EFRAG (0,75 pt)** :
  - l'EFRAG est le **conseiller technique** de la Commission européenne. Il prépare les projets d'ESRS et rend des avis techniques ; la Commission **adopte** les ESRS par actes délégués, après cet avis [V règl. délégué 2026/1563, consid. 3 ; dir. 2013/34 art. 29 ter] ;
  - l'EFRAG ne fixe donc pas lui-même de règles obligatoires ; les ESRS valent par leur adoption par la Commission ;
  - les ESRS retiennent une approche de **double matérialité** (impact et financière) [V ESRS 1 (2026) § 35 ; F12 § 1].
- **Normes transversales (0,75 pt)** :
  - l'**ESRS 1** « Exigences générales » fixe les conventions et les exigences générales : double matérialité, horizons de temps, structure, connectivité. L'**ESRS 2** « Informations générales à publier » fixe les informations générales pour tous les thèmes matériels. Elles s'appliquent **conjointement** avec les normes thématiques [V ESRS 1 (2026) § 7-10] ;
  - l'ESRS 2 s'applique **toujours**, quel que soit le résultat de l'analyse de matérialité ; les normes thématiques ne s'appliquent qu'aux thèmes **matériels** [V ESRS 1 (2026) § 24, 29] ;
  - une publication volontaire ne permet pas d'appliquer les ESRS « à la carte » : en déclarant ses informations conformes aux ESRS, TRÉLAMONT s'oblige à respecter toutes leurs exigences applicables, à commencer par l'analyse de double matérialité, et le déclare expressément dans sa base de préparation [V ESRS 2 (2026) BP-1 § 5].

**Réponses tolérées**
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences », « déclaration relative à la durabilité »).

**Erreurs fréquentes**
- Présenter l'EFRAG comme l'auteur de normes obligatoires par elles-mêmes, ou le confondre avec l'ISSB (`JUR-A01`).
- Discuter le champ ou le calendrier de l'obligation de publier, que l'énoncé écarte (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règl. délégué 2026/1563 consid. 3 ; dir. 2013/34 art. 29 ter | Rôle de l'EFRAG ; adoption par la Commission | [V] | F12 § 1 |
| ESRS 1 (2026) § 7-10, 24, 29, 35 ; ESRS 2 (2026) BP-1 § 5 | Normes transversales ; déclaration de conformité | [V] | F12 § 3, 5, 14 |

### 3.7 Double matérialité et analyse de la gérance (4,5 pts)

**a. Définitions, horizons et rattachement (2 pts)**

*Définitions (0,5 pt)*
- **Matérialité d'impact** : un thème est matériel s'il concerne des impacts positifs ou négatifs, réels ou potentiels, de l'entreprise sur la population ou l'environnement, à court, moyen ou long terme, y compris par ses produits. La gravité d'un impact négatif s'apprécie par son ampleur, son étendue et son caractère irrémédiable, et, pour un impact potentiel, aussi par sa probabilité [V ESRS 1 (2026) § 39-40].
- **Matérialité financière** : un thème est matériel s'il a, ou peut raisonnablement avoir, des effets financiers matériels sur le développement, la situation financière, les performances, les flux de trésorerie, l'accès au financement ou le coût du capital. Elle s'apprécie par la probabilité et l'ampleur potentielle de ces effets [V ESRS 1 (2026) § 47, 50]. Les risques peuvent naître des impacts, des **dépendances** à l'égard de ressources naturelles, humaines et sociales, ou d'autres facteurs [V § 48-49].
- Un thème est matériel au titre de l'une des deux dimensions, ou des deux : un impact peut être matériel **exclusivement** en termes d'impact [V § 35].

*Horizons (0,5 pt)* : à compter de la fin de la période de reporting, le **court terme** correspond à la période des états financiers (un an), le **moyen terme** va jusqu'à cinq ans, le **long terme** au-delà de cinq ans [V ESRS 1 (2026) § 79]. Une catégorie supplémentaire de long terme est utilisée si les prévisions d'impacts dépassent cinq ans [V § 80].

*Rattachement (1 pt : 0,5 pt par thème)*

| Thème | Matérialité d'impact | Matérialité financière | Horizon |
|---|---|---|---|
| Approvisionnement en bois | **Impact négatif potentiel** : prélèvements de chêne dans des forêts dont la gestion n'est pas connue pour une partie des volumes | **Risques** : hausse du prix du chêne ; **dépendance** à une ressource naturelle et à un fournisseur qui assure 70 % des volumes ; pertes de bois au stockage (lot C-17) | Court terme pour le prix et les pertes ; moyen et long terme pour la ressource |
| Énergie du séchage | **Impact négatif réel** : émissions de gaz à effet de serre des séchoirs au gaz naturel | **Risque** : hausse du prix du gaz ; **opportunité** : chaudière alimentée par les chutes de bois, qui réduirait la facture et l'impact | Court terme pour le prix ; moyen terme pour la chaudière |

**b. Faiblesses de l'analyse et conséquences (2,5 pts)**

*Faiblesses (2 pts : 0,5 pt par faiblesse justifiée, dans la limite de quatre)*
1. **Règle de la moyenne** : retenir un thème lorsque la moyenne de ses deux notes atteint 3 compense une dimension par l'autre. Or un thème est matériel s'il l'est au titre de l'impact **ou** au titre financier [V ESRS 1 (2026) § 35]. La règle de la gérance n'est pas un seuil approprié au sens des ESRS, qui demandent des considérations qualitatives et des seuils quantitatifs appropriés [V § 37]. Avec un seuil de 3 appliqué à chaque dimension, la grille rend matériels les quatre thèmes, dont deux ont une note d'impact de 4 et deux de 3.
2. **Poussières et santé écartées sur le seul critère financier** :
   - l'impact potentiel est grave : il touche la santé de 46 salariés sur 85 et peut être irrémédiable ; sa probabilité est étayée par les mesures de juin 2026, qui dépassent la valeur de référence sur 3 postes sur 11. Il est matériel au titre de l'impact, quel que soit son coût pour la société [V § 35, 40] ;
   - l'absence d'arrêt de travail ne concerne que l'impact réel de l'année, alors que les effets apparaissent après de nombreuses années ;
   - le futur système d'aspiration ne peut pas être pris en compte, puisqu'il n'est pas encore mis en œuvre ni même commandé [V § 43 b)].
3. **Horizon limité à trois ans** : la durée du plan d'affaires ne couvre pas le long terme, au-delà de cinq ans, que les ESRS imposent d'examiner [V § 39, 47, 79-80]. La fin de vie des fenêtres, dans 30 à 40 ans, est un impact de long terme lié aux produits de l'entreprise : il ne peut pas être écarté pour cette raison.
4. **Parties prenantes affectées non consultées** : la gérance n'a interrogé que des utilisateurs de l'information (client, banque, associée). Les salariés de l'atelier, premiers concernés par les poussières, et leurs représentants n'ont pas été consultés. Or le dialogue avec les parties prenantes affectées est une **contribution essentielle** à l'évaluation de la matérialité d'impact [V § 42]. La phrase du projet selon laquelle l'analyse a « associé l'ensemble de nos parties prenantes » est inexacte.
5. **Note financière de l'approvisionnement sous-estimée** : les pertes au stockage, jugées « négligeables », sont démenties par le lot C-17, qui exige une dépréciation de 73 200 €, soit 5,9 % du résultat courant, par deux autres lots déclassés en 2026 et par les 60 % du parc non couverts. La dépendance à VERDELLAT n'est pas cotée [V § 48-50].

*Conséquences (0,5 pt)*
- Les **poussières et la santé des salariés** et la **fin de vie des menuiseries** doivent être retenues comme thèmes matériels, au moins au titre de l'impact. La note financière de l'approvisionnement doit être revue.
- La gérance doit consulter les parties prenantes affectées, documenter sa méthode et ses seuils, et décrire exactement le processus suivi. Elle publie ensuite, pour chaque thème matériel, les informations requises par l'ESRS 2 et par les normes thématiques pertinentes [V ESRS 1 (2026) § 24-25, 29, 34]. Le détail de ces informations n'est pas attendu.

**Réponses tolérées**
- Un rattachement de la dépendance à VERDELLAT au seul risque économique, si le lien avec la ressource en chêne est fait.
- D'autres faiblesses tirées des annexes, par exemple une analyse conduite par deux personnes sans les responsables de l'atelier.
- Le vocabulaire des ESRS de 2023 (« incidences », « double importance », « parties intéressées touchées »).

**Erreurs fréquentes**
- Confondre impact (effet de l'entreprise sur les personnes et l'environnement) et risque (effet sur l'entreprise) (`JUR-A01`).
- Refaire une analyse complète de double matérialité, ou proposer des actions et des objectifs que la question ne demande pas (`JUR-F07`).
- Accepter l'exclusion des poussières au motif que le système d'aspiration sera installé (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 34-37, 39-44, 47-50 | Double matérialité ; gravité ; parties prenantes affectées ; actions non mises en œuvre ; dépendances | [V] | F12 § 6, 15 |
| ESRS 1 (2026) § 79-80 | Horizons de temps | [V] | F12 § 5, 14, 15 |
| ESRS 1 (2026) § 24-25, 29 | Thèmes matériels et informations à publier | [V] | F12 § 5, 8 |
| Données des annexes 3.1, 3.4, 3.8 et 3.9 | Notes, mesures d'empoussièrement, lots déclassés, consultations | données de l'énoncé | — |

### 3.8 Mission contractuelle d'assurance limitée (2 pts)

- **Nature de la mission (0,5 pt)** :
  - la certification des comptes ne couvre pas les informations en matière de durabilité : elle porte sur les comptes annuels. C'est la réponse à la question n° 3 du gérant ;
  - la certification légale de ces informations ne vise que les entités tenues de les publier [V L. 821-54 II]. TRÉLAMONT ne l'est pas : la mission est une **prestation contractuelle**, définie par une lettre de mission qui en précise l'étendue, le calendrier et les honoraires [V L. 821-2 IV, R. 821-195]. Les honoraires sont forfaitaires et indépendants de la conclusion, comme l'exige l'interdiction des honoraires conditionnels [V code de déontologie art. 12-13] ;
  - avant d'accepter, le cabinet a vérifié que cette prestation ne compromettait pas sa mission de commissaire aux comptes : il vérifie des informations établies par la gérance, sans les produire [V A. 821-55 § 15]. Le rapport ne doit pas être présenté à BÂTIVALE comme une certification légale [S].
- **Objectifs et axes ; place de l'axe 1 (0,75 pt)** :
  - par analogie avec les lignes directrices de la H2A, la vérification porte sur l'**axe 1**, la conformité aux ESRS du **processus** de détermination des informations publiées (analyse de double matérialité), y compris la consultation du CSE, et sur l'**axe 2**, la conformité des **informations** publiées aux ESRS [V LD 2026 § 2 ; S, transposition] ;
  - l'axe relatif à la taxonomie et celui du balisage ne concernent pas TRÉLAMONT ; le balisage n'est d'ailleurs exigible d'aucune entité tant que ses règles ne sont pas adoptées [V LD 2026 § 2, § 10] ;
  - l'axe 1 vient en premier : le processus détermine **quels thèmes** sont publiés. Une analyse défaillante fait omettre des informations, ce qu'aucune vérification de l'axe 2 ne peut corriger. La H2A y voit une « étape cruciale » [V LD 2026 § 2] ;
  - la consultation du CSE n'est pas une obligation légale pour TRÉLAMONT. Elle entre dans la mission parce que la gérance s'y est engagée et que la lettre de mission la vise [S, F12 § 11 ; F13 § 4.5].
- **Nature de l'assurance (0,75 pt)** : l'assurance est **limitée**. Les vérifications sont moindres en nature, en étendue et en durée que celles de l'audit des comptes. La conclusion s'exprime sous une **forme négative** : le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes [V LD 2026, niveau d'assurance ; F13 § 2.3]. La conclusion est formulée **axe par axe**, dans un rapport distinct de celui sur les comptes (annexe 3.7).

**Réponses tolérées**
- La mention d'une désignation volontaire par les associés pour une mission conduite dans les conditions de la certification légale, si le candidat la distingue de la prestation contractuelle retenue par la lettre de mission.

**Erreurs fréquentes**
- Présenter la mission comme la certification légale, ou lui attribuer une assurance raisonnable (`JUR-A01`).
- Faire figurer la taxonomie et le balisage parmi les axes à vérifier chez TRÉLAMONT (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-2 IV, R. 821-195 ; code de déontologie art. 12-13 ; A. 821-55 § 15 | Mission légale ; prestation ; honoraires ; indépendance | [V] ; application : [S] | F12 § 11 ; F13 § 1, 2.1 ; F10 § 12 |
| LD 2026 § 2, § 10, niveau d'assurance | Axes ; balisage ; assurance limitée | [V] ; transposition : [S] | F13 § 2 |

### 3.9 Procédures sur le processus (2,5 pts)

*0,5 pt par procédure justifiée et rattachée au cas, dans la limite de cinq* [V LD 2026 § 2-3, § 7.1, § 7.3, § 12 ; S, transposition à une mission contractuelle]

1. **Documentation du processus** : obtenir l'analyse, la méthode, la grille de cotation, les sources utilisées et les personnes associées ; vérifier qu'elle couvre les activités, les produits et les trois horizons de temps. L'horizon de trois ans apparaît dès ce stade.
2. **Entretiens** avec le gérant, le responsable qualité, le chef d'atelier et le chef de parc, et avec des membres du CSE, pour comprendre comment les notes ont été attribuées et corroborer les affirmations (« coût faible », « pertes négligeables »), avec esprit critique.
3. **Seuils et règle d'agrégation** : comparer la règle de la moyenne aux critères des ESRS, puis recalculer la sélection dimension par dimension. Deux thèmes à forte note d'impact sont écartés à tort.
4. **Corroboration des notes par des éléments probants**, notamment ceux de l'audit des comptes, en échangeant avec l'équipe chargée des comptes au nom de la connectivité :
   - le rapport de mesures d'empoussièrement (3 postes sur 11) et l'absence de commande du système d'aspiration, face à la note financière de 1 et à l'action future invoquée ;
   - la dépréciation du lot C-17 (73 200 € nécessaires), les deux autres lots déclassés et le parc couvert à 40 % seulement, face aux pertes « négligeables » ;
   - la part de VERDELLAT dans les achats (70 % du chêne), face à la dépendance non cotée.
5. **Consultation des parties prenantes** : examiner les comptes rendus et la liste des personnes interrogées. Les salariés de l'atelier n'y figurent pas, ce que la description du projet passe sous silence.
6. **Consultation du CSE** : obtenir l'ordre du jour et le procès-verbal de la réunion du 18/02/2027 et les comparer à l'engagement du 20/10/2026. Les informations n'ont pas été présentées, et la consultation prévue en septembre 2027 interviendrait après la publication.
7. **Description du processus dans le projet d'informations** : vérifier qu'elle reflète exactement la démarche suivie. La H2A demande de vérifier la pertinence de la démarche de double matérialité et sa correcte description.
8. **Communication des constats à la gérance** et demande de correction avant l'émission du rapport, en vue d'une lettre d'affirmation [V LD 2026 § 4, § 14].

**Réponses tolérées**
- Toute autre procédure pertinente rattachée à une donnée des annexes, par exemple la comparaison de la note financière de l'énergie avec les factures de gaz.

**Erreurs fréquentes**
- Proposer des procédures générales sans les rattacher aux annexes (`JUR-A05`, `JUR-F07`).
- Vérifier des données chiffrées des informations publiées (axe 2) au lieu du processus (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 2, § 3, § 4, § 7.1, § 7.3, § 12, § 14 | Processus ; connectivité et échanges avec l'audit des comptes ; consultation du CSE ; appréciation des éléments collectés | [V] intitulés et principes ; transposition : [S] | F13 § 3 |
| ESRS 1 (2026) § 35, 37, 42, 43, 79 | Critères appliqués lors des vérifications | [V] | F12 § 6, 15 |

### 3.10 Conclusion sur l'axe relatif au processus (1,5 pt)

- **Avis (0,75 pt)** :
  - les défauts relevés ne sont pas corrigés : règle de la moyenne, deux thèmes matériels écartés, horizon de trois ans, parties prenantes affectées non consultées, description inexacte du processus ; s'y ajoute l'absence de consultation du CSE, contraire à l'engagement que la lettre de mission fait entrer dans la vérification ;
  - ces erreurs et omissions sont d'une importance telle qu'elles remettent en cause la conformité du processus aux ESRS. Elles sont multiples et touchent le choix même des thèmes publiés : on ne peut pas dire quelles informations l'état de durabilité aurait comportées avec un processus conforme. Leurs incidences ne sont donc **pas clairement circonscrites** ;
  - la conclusion est un **avis de non-conformité, motivé** [V LD 2026 § 17 ; S, convention de F13 § 4.5 et transposition à une mission contractuelle]. Une réserve ne suffirait que si le seul défaut était l'absence de consultation du CSE.
- **Formulation (0,25 pt)** : « nous estimons que le processus mis en œuvre par TRÉLAMONT n'est pas conforme aux ESRS », suivie de l'exposé de chacun des motifs [V LD 2026, annexe 2].
- **Portée (0,5 pt)** :
  - la conclusion repose sur une **assurance limitée** et sur une mission **contractuelle** : ce n'est pas une certification légale ;
  - elle est émise **par axe**. La conclusion sur les informations (axe 2) est formulée séparément ; elle sera vraisemblablement affectée par les omissions de thèmes matériels ;
  - le cabinet en communique au préalable les motifs à la gérance. Il remet son rapport à TRÉLAMONT, qui le transmet à BÂTIVALE : tenu au secret professionnel, le cabinet ne l'adresse pas lui-même au client sans l'accord de la société [V L. 821-35 ; S, application] ;
  - comme toute conclusion de cette nature, elle ne garantit ni la viabilité ni la qualité de la gestion, et se distingue de l'opinion sur les comptes.

**Réponses tolérées**
- Un avis de conformité assorti de réserves, si le candidat soutient, avec le critère de circonscription, que les défauts sont identifiables un à un : 0,25 pt sur 0,75.
- L'emploi du mot « conclusion » ou « avis » indifféremment.

**Erreurs fréquentes**
- Formuler une conclusion positive (« le processus est conforme »), ou un avis unique pour l'ensemble de la mission (`JUR-A01`, `JUR-A02`).
- Présenter l'absence de consultation du CSE comme une violation d'une obligation légale de TRÉLAMONT (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 et annexe 2 | Avis par axe ; non-conformité ; formulations | [V] ; transposition : [S] | F13 § 4 |
| F13 § 4.5 ; F12 § 11 | Défaut de consultation du CSE ; entité qui publie volontairement | [S] convention de corrigé ; [V] pour le caractère non obligatoire de la consultation | F12 § 11 ; F13 § 4.5 |
| C. com. L. 821-35, L. 821-55 | Secret professionnel ; absence de garantie de la gestion | [V] ; application : [S] | F10 § 7 ; F09 § 6 |
