# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 22

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 23/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.11 | `exercices/ex61_consolidation_anc_ip_derogatoires_retraites_flux` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.8 | `exercices/ex62_tup_boni_deficit_valeur_comptable` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.11 | `exercices/ex63_audit_tresorerie_association_rup_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Contexte légal des comptes consolidés d'une SAS | `2.1.b` Contexte réglementaire et légal de la consolidation | 2 |
| 1.2 Importance relative et filiale laissée hors du périmètre | `2.1.a` Cadre conceptuel de l'IASB | 1,5 |
| 1.3 Périmètre, contrôle conjoint et date d'entrée | `2.1.c` Périmètre de consolidation | 2,5 |
| 1.4 Effets de l'intégration proportionnelle ; la carrière en IFRS | `2.1.d` Conséquences des méthodes de consolidation | 2 |
| 1.5 a Stock et mouvement des amortissements dérogatoires | `2.2.b` Retraitements préparatoires (provisions réglementées) | 1,5 |
| 1.5 b Tableau des incidences et écritures d'élimination | `2.2.b` Retraitements préparatoires (provisions réglementées) | 2 |
| 1.5 c Résultat de cession de la presse | `2.2.b` Retraitements préparatoires (provisions réglementées) | 1,5 |
| 1.6 a Engagements de retraite : règle de l'ANC et motif du retraitement | `2.2.c` Homogénéisation, thèmes communs | 1 |
| 1.6 b Tableau des incidences et écritures | `2.2.c` Homogénéisation, thèmes communs | 3 |
| 1.6 c Impôt différé actif | `2.2.c` Homogénéisation, thèmes communs | 1 |
| 1.7 a Marge interne sur le stock d'argile (50 %) | `2.2.f` Comptes réciproques et résultats internes | 2,5 |
| 1.7 b Ventes et créance réciproques (50 %) | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.7 c Dividende de la carrière | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.8 a Coût d'acquisition, actif net réévalué et écart d'acquisition de PARELIS | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.8 b Durée d'utilisation et amortissement de l'écart d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 1,5 |
| 1.8 c Écritures : frais, résultat antérieur à l'entrée, écarts d'évaluation, amortissement | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.9 a Partage des capitaux propres de PARELIS | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.9 b Partage des capitaux propres des GLAISIÈRES | `2.2.h` Partage des capitaux propres | 1,5 |
| 1.9 c Écritures d'élimination des titres et de partage | `2.2.h` Partage des capitaux propres | 1,5 |
| 1.9 d Réserves et résultat consolidés, intérêts minoritaires | `2.2.h` Partage des capitaux propres | 2 |
| 1.10 Processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.11 a Flux d'investissement et de financement (ANC) | `2.3.a` Documents de synthèse consolidés | 4 |
| 1.11 b Dividende de la carrière et tableau des flux | `2.3.a` Documents de synthèse consolidés | 1 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires (réserves / résultat) ; `EA` = écart d'acquisition ; `AMO_EA` = amortissements de l'écart d'acquisition ; `DOT_EA` = dotations aux amortissements des écarts d'acquisition (compte de résultat) ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.CORVALLIER` : titres détenus par CORVALLIER SAS ; `RSV.GLAISIERES` : réserves des GLAISIÈRES, intégrées à 50 %). Les écritures portant sur les GLAISIÈRES sont passées sur les comptes cumulés à 50 %. Toutes les écritures ci-dessous sont équilibrées.

---

### 1.1 Contexte légal des comptes consolidés de CORVALLIER SAS (2 pts)

- **Qui les établit et les arrête (0,5).** Les sociétés commerciales établissent et publient chaque année, à la diligence de leur organe d'administration ou de direction, des comptes consolidés **et un rapport sur la gestion du groupe** [V C. com. L. 233-16 I ; F03 § 18.1]. Dans une SAS, les attributions du conseil d'administration sont exercées par le président ou par les dirigeants que désignent les statuts [V L. 227-1, 3e al.] ; les statuts de CORVALLIER les confient à la présidente (annexe 1.2). C'est donc **la présidente** qui établit et arrête les comptes consolidés et le rapport sur la gestion du groupe, préparés par la direction financière avec l'aide du cabinet ; le comité stratégique n'a qu'un rôle consultatif. Le rapport sur la gestion du groupe peut former un seul document avec le rapport de gestion de la société [V L. 233-26].
- **Les associés (0,5).** La loi impose une décision collective des associés de la SAS sur les **comptes annuels** et l'**affectation du résultat** [V L. 227-9 ; statuts, annexe 1.2]. La règle de la SA qui fait « délibérer et statuer » l'assemblée sur les comptes consolidés [V L. 225-100 I] ne s'applique pas à la SAS (L. 227-1 l'écarte) : ce sont les statuts qui organisent l'information des associés. Ceux de CORVALLIER prévoient une **présentation** des comptes consolidés et du rapport sur la gestion du groupe à l'assemblée qui statue sur les comptes annuels, **sans vote** : M. FOURNERAY en prendra connaissance, mais les associés ne les approuveront pas.
- **Publication (0,25).** Société par actions, CORVALLIER SAS dépose au greffe, dans le mois qui suit l'approbation des comptes annuels (deux mois par voie électronique), avec ses comptes annuels, les comptes consolidés, le rapport sur la gestion du groupe et le rapport des commissaires aux comptes sur les comptes consolidés [V L. 232-23 I 1°].
- **Certification (0,5).** Les commissaires aux comptes certifient, en justifiant de leurs appréciations, que les comptes consolidés sont réguliers et sincères et donnent une image fidèle du patrimoine, de la situation financière et du résultat de l'ensemble consolidé, notamment après examen des travaux des commissaires aux comptes des sociétés consolidées [V L. 821-53] ; ils vérifient la sincérité et la concordance avec les comptes consolidés des informations du rapport sur la gestion du groupe [V L. 821-54]. Astreinte à publier des comptes consolidés, CORVALLIER SAS doit avoir **au moins deux** commissaires aux comptes [V L. 821-41 ; F09] : c'est le cas. Le cabinet SAULNERON, qui assiste la direction financière, n'est pas l'un d'eux.
- **Dividende (0,25).** Le bénéfice distribuable est celui de **l'exercice de la société**, diminué des pertes antérieures et des dotations aux réserves obligatoires, augmenté du report bénéficiaire ; les associés fixent le dividende **après approbation des comptes annuels** [V L. 232-11, L. 232-12]. Le groupe n'a pas la personnalité juridique : seule CORVALLIER SAS distribue, sur ses propres résultats et réserves. Le résultat consolidé comprend des résultats que la société n'a pas reçus (70 % du résultat de PARELIS, la moitié de celui de la carrière, non distribués) : les distribuer reviendrait à prélever des sommes dont elle ne dispose pas, au détriment de ses créanciers.

---

### 1.2 Importance relative et PATINÉA (1,5 pt)

**La notion (0,75 pt).** Une information est **significative** lorsqu'on peut raisonnablement s'attendre à ce que son omission, son inexactitude ou son obscurcissement influence les décisions que les principaux utilisateurs des états financiers (investisseurs, prêteurs, autres créanciers) prennent sur la base de ces états [V IAS 1 § 7 ; F03 § 18.2]. Elle dépend de la **nature ou de l'ampleur** de l'information, ou des deux, et s'apprécie au regard des états financiers **pris dans leur ensemble**, l'information étant considérée isolément ou avec d'autres [V IAS 1 § 7]. Le cadre conceptuel de 2018 en fait un aspect de la **pertinence propre à l'entité** : il ne fixe aucun seuil uniforme [S, F03 § 7.2 et § 18.2].

**La règle de l'ANC et PATINÉA (0,75 pt).**
- Une entité contrôlée entre dans le périmètre lorsque sa consolidation présente, **seule ou avec d'autres**, un caractère significatif par rapport aux comptes consolidés [V ANC 2020-01, art. 211-1, p. 12]. Une filiale **peut** être laissée hors de la consolidation lorsqu'elle ne représente, seule ou avec d'autres, qu'un **intérêt négligeable** au regard de l'image fidèle de l'ensemble, à condition de le **justifier dans l'annexe** [V L. 233-19 II 2°, repris par l'art. 212-1, p. 17]. C'est l'application de l'importance relative au périmètre : l'exclusion ne doit pas pouvoir modifier l'appréciation des utilisateurs.
- PATINÉA représente 0,67 % du chiffre d'affaires (640 000 / 96 000 000), 0,35 % du total du bilan et 0,30 % du résultat de l'ensemble ; par sa nature, elle ne présente pas de risque particulier : aucune opération avec le groupe, aucun emprunt, aucune garantie de CORVALLIER ; c'est la seule entité contrôlée non consolidée. La proposition peut être retenue.
- Conditions : justification dans l'annexe consolidée ; titres maintenus en **titres de participation** (150 000 €) dans le bilan consolidé [V art. 212-3, p. 18] ; réexamen à chaque clôture (le seuil de 1 % de la note n'est pas une règle) ; si PATINÉA devenait significative, elle serait consolidée comme si elle l'avait été depuis sa prise de contrôle, ses résultats accumulés depuis cette date passant en résultat [V art. 211-11, p. 16].

---

### 1.3 Périmètre, contrôle conjoint et date d'entrée (2,5 pts)

**Tableau (1,5 pt)**

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % d'intérêt des minoritaires |
|---|---:|---|---|---:|---:|
| CORVALLIER SAS | — | Société consolidante | — | 100 % | — |
| PARELIS | 70 % | Contrôle exclusif | Intégration globale (depuis le 01/04/2026) | 70 % | 30 % |
| GLAISIÈRES DU BOURBONNAIS | 50 % | Contrôle conjoint | Intégration proportionnelle (50 %) | 50 % | aucun |
| PATINÉA | 100 % | Contrôle exclusif | Laissée hors du périmètre (intérêt négligeable, question 1.2) ; titres de participation | (100 %) | — |

PARELIS : majorité des droits de vote (70 %), donc contrôle exclusif [V art. 211-3 ; L. 233-16 II 1°], confirmé par la désignation du président et de quatre des cinq membres du comité de direction.

**Contrôle conjoint des GLAISIÈRES (0,5 pt).** Avec 50 %, CORVALLIER n'a pas la majorité ; la carrière est exploitée en commun par **deux** associées (nombre limité), un **accord contractuel** (statuts et pacte) organise le partage du pouvoir (deux membres chacune au comité, présidence alternée), et les décisions essentielles (budget, plan d'extraction, investissements, emprunts, prix, dividendes) exigent l'**unanimité** : aucune associée ne peut imposer seule ses décisions [V art. 211-4, p. 13 ; L. 233-16 III ; F03 § 2]. Contrôle conjoint, donc intégration proportionnelle [V art. 221-1, 221-3 ; F03 § 3].

**Date d'entrée de PARELIS (0,5 pt).** Une entité entre dans le périmètre à la date de prise de contrôle ; c'est en principe la date d'acquisition des titres, sauf contrat transférant le contrôle à une autre date [V art. 211-10, p. 16]. Les titres ont été acquis et le contrôle obtenu le **01/04/2026** : PARELIS est consolidée à compter de cette date. Seuls ses produits et charges d'avril à décembre entrent dans le résultat consolidé ; son résultat du premier trimestre (200 000 €) fait partie des capitaux propres acquis.

---

### 1.4 Effets de la méthode de consolidation (2 pts)

**Comparaison chiffrée (1,5 pt).** Montants des comptes de 2026 de la carrière, avant éliminations et retraitements :

| Dans les comptes consolidés | Intégration globale (100 %) | **Intégration proportionnelle (50 %, retenue)** | Mise en équivalence |
|---|---:|---:|---:|
| Actifs de la carrière, poste par poste | 9 400 000 | **4 700 000** | une ligne « titres mis en équivalence » : 3 100 000 |
| Emprunts auprès des établissements de crédit | 2 400 000 | **1 200 000** | 0 |
| Chiffre d'affaires | 6 400 000 | **3 200 000** | 0 |
| Résultat | 800 000, dont 400 000 aux minoritaires | **400 000, en totalité au groupe** | quote-part de 400 000 sur une ligne distincte |
| Quote-part du groupe dans les capitaux propres de la carrière | 3 100 000 | **3 100 000** | 3 100 000 |
| Intérêts minoritaires | 3 100 000 (50 % de 6 200 000) | **aucun** | aucun |

L'intégration proportionnelle reprend **la moitié de chaque actif, de chaque dette, de chaque produit et de chaque charge** de la carrière, sans intérêts minoritaires [V art. 221-3, 261-1 ; F03 § 18.3] ; après élimination des ventes à CORVALLIER (question 1.7), la carrière apporte 1 800 000 € au chiffre d'affaires consolidé. Les trois méthodes donnent les **mêmes capitaux propres et le même résultat part du groupe** ; elles diffèrent par la taille du bilan, l'endettement et le chiffre d'affaires affichés. Réponse au partenaire : l'intégration globale suppose un **contrôle exclusif**, que CORVALLIER n'a pas (unanimité) ; elle ferait figurer dans les comptes du groupe la totalité d'une dette et d'actifs dont la moitié revient à TUILERIE ORVAINE, qui apparaîtrait en intérêts minoritaires. L'intégration proportionnelle traduit le partage du contrôle ; TUILERIE ORVAINE intègre de même l'autre moitié dans ses propres comptes consolidés.

**En IFRS (0,5 pt).** La carrière serait un **partenariat** (contrôle conjoint, consentement unanime) ; il faudrait le classer en **coentreprise** ou en **activité conjointe** [V IFRS 11, appendice A ; F03 § 3, § 18.4]. Elle est exploitée dans une société, dont les actifs et les passifs sont les siens ; l'accord ne donne aux associées aucun droit sur ces actifs ni obligation au titre de ces dettes (emprunts sans caution) ; la carrière vend environ un cinquième de son argile à des tiers, aux prix du marché, et porte les risques de ses ventes et de ses stocks : les associées ont des droits sur son **actif net**. Coentreprise, donc **mise en équivalence** (l'intégration proportionnelle n'existe pas en IFRS) [V B22, B23, B29 à B32 ; IFRS 11 § 24]. Si la carrière vendait toute sa production à ses deux associées, qui seraient en fait sa seule source de flux de trésorerie, ce serait une activité conjointe : chacune comptabiliserait sa quote-part des actifs, des passifs, des produits et des charges [V B31, B32 ; IFRS 11 § 20].

---

### 1.5 Amortissements dérogatoires (5 pts)

#### a. Stock et mouvement (1,5 pt : four 0,75 ; presse 0,75)

| | Four tunnel n° 2 | Presse P4 | Total |
|---|---:|---:|---:|
| Amortissement fiscal cumulé au 31/12/2025 | 837 000 + 648 675 + 502 723 + 389 610 = 2 378 008 | 224 000 + 145 600 + 94 640 = 464 240 | |
| Amortissement des comptes cumulé au 31/12/2025 | 4 × 372 000 = 1 488 000 | 3 × 128 000 = 384 000 | |
| **Stock au 31/12/2025** (compte 145) | **890 008** | **80 240** | **970 248** |
| Annuité fiscale de 2026 | 301 948 | 96 000 (9 mois, égale à l'annuité des comptes) | |
| Annuité des comptes de 2026 | 372 000 | 96 000 | |
| **Mouvement de 2026** | **reprise 70 052** (annuité fiscale inférieure) | **reprise du stock à la cession : 80 240** | **reprises 150 292** |
| **Stock au 31/12/2026** | **819 956** | **0** | **819 956** |

Plan fiscal de la presse : 640 000 × 35 % = 224 000 ; 416 000 × 35 % = 145 600 ; 270 400 × 35 % = 94 640 (aucun passage au linéaire : 270 400 / 3 = 90 133 < 94 640).

#### b. Incidences et écritures (2 pts)

Les amortissements dérogatoires résultent de la seule application de la législation fiscale : ils sont éliminés [V ANC 2020-01, art. 272-1, p. 53 ; F04 R1]. Le stock, déduit fiscalement et imposable lors de sa reprise, donne un **impôt différé passif** [V art. 272-8, p. 57].

| | Ouverture (réserves) | Exercice 2026 (résultat) | Clôture |
|---|---:|---:|---:|
| Avant impôt | + 970 248 (stock annulé) | – 150 292 (reprises annulées) | 819 956 |
| Impôt différé passif (25 %) | – 242 562 | + 37 573 | IDP 204 989 |
| **Net** | **+ 727 686** | **– 112 719** | **614 967** (819 956 – 204 989) |

**C1 (bilan) et C1R (compte de résultat), 1 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 145 Amortissements dérogatoires (solde du four) | 819 956 | |
| RST.CORVALLIER Résultat CORVALLIER SAS (150 292 × 75 %) | 112 719 | |
| RSV.CORVALLIER Réserves CORVALLIER SAS (970 248 × 75 %) | | 727 686 |
| IDP Impôt différé passif (819 956 × 25 %) | | 204 989 |
| *C1 – Élimination des amortissements dérogatoires* | **932 675** | **932 675** |
| 78725 Reprises sur provisions réglementées – amortissements dérogatoires (70 052 + 80 240) | 150 292 | |
| CH_ID Produit d'impôt différé (150 292 × 25 %) | | 37 573 |
| RES_CR Résultat | | 112 719 |
| *C1R – Annulation des reprises de 2026* | **150 292** | **150 292** |

Tableau : 1 pt.

#### c. Résultat de cession de la presse (1,5 pt)

Valeur nette comptable au 30/09/2026 : 640 000 – (384 000 + 96 000) = 160 000 ; valeur nette fiscale : 640 000 – (464 240 + 96 000) = 79 760.

| | Comptes individuels | Comptes consolidés |
|---|---:|---:|
| Prix de cession (757) | 200 000 | 200 000 |
| Valeur nette comptable (657) | – 160 000 | – 160 000 |
| Reprise des dérogatoires de la presse (78725) | + 80 240 | éliminée |
| **Incidence avant impôt** | **120 240** (= prix – valeur nette fiscale) | **40 000** |
| Impôt exigible sur la plus-value fiscale (120 240 × 25 %) | – 30 060 | – 30 060 |
| Reprise de l'impôt différé passif de la presse (80 240 × 25 %) | — | + 20 060 |
| **Incidence nette** | **90 180** | **30 000** (= 40 000 × 75 %) |

La plus-value comptable (757 – 657) est la même dans les deux comptes : 40 000 €. Dans les comptes individuels s'ajoute la reprise du stock de dérogatoires, qui restitue au résultat l'avance d'amortissement fiscal pratiquée de 2023 à 2025 : elle est imposée (l'impôt exigible porte sur la plus-value fiscale). En consolidation, ces dérogatoires n'ont jamais été des charges : leurs dotations ont été éliminées chaque année, et le stock d'ouverture figure en réserves (net de son impôt différé). La reprise est donc éliminée, et l'impôt différé passif de la presse, devenu sans objet, est repris en produit : l'impôt du groupe sur la cession se ramène à 25 % de la plus-value comptable (30 060 – 20 060 = 10 000). L'écart entre les deux incidences nettes, 60 180 €, est exactement la reprise éliminée, nette d'impôt (80 240 × 75 %).

Tableau : 1 pt ; explication de l'écart : 0,5 pt.

---

### 1.6 Indemnités de fin de carrière (5 pts)

#### a. Règle de l'ANC et motif du retraitement (1 pt)

Le provisionnement des engagements de retraite est la **méthode de référence** du PCG, que CORVALLIER SAS n'applique pas dans ses comptes individuels (elle mentionne l'engagement dans son annexe) [V PCG art. 324-1, 121-5 ; F04 R8]. Les méthodes de référence du PCG sont des méthodes de référence pour les comptes consolidés, sauf disposition contraire [V ANC 2020-01, art. 271-3, p. 51 ; F03 § 18.3] : le règlement **n'impose pas** la provision, il la recommande (0,5). Le manuel du groupe l'a retenue ; or les méthodes du groupe s'appliquent de manière homogène à toutes les sociétés consolidées [V art. 271-5, p. 52 ; F04 § 1] : les comptes de CORVALLIER SAS sont retraités ; ceux de PARELIS, qui provisionne déjà selon la même méthode, ne le sont pas (0,5).

#### b. Incidences et écritures (3 pts)

Charge du groupe en 2026 : variation de l'engagement augmentée des indemnités versées, qui sont imputées sur la provision : 1 960 000 – 1 840 000 + 140 000 = 260 000 €. Les comptes individuels ont supporté 140 000 € : l'écart avant impôt est de – 120 000 €.

| | Ouverture (réserves) | Exercice 2026 (résultat) | Clôture |
|---|---:|---:|---:|
| Provision (avant impôt) | – 1 840 000 | – 120 000 (260 000 – 140 000) | provision 1 960 000 |
| Impôt différé actif (25 %) | + 460 000 | + 30 000 | IDA 490 000 |
| **Net** | **– 1 380 000** | **– 90 000** | |

Tableau : 1,5 pt (dont 0,5 pour la charge de 260 000 et le reclassement des indemnités).

**C2 (bilan) et C2R (compte de résultat), 1,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| RSV.CORVALLIER Réserves CORVALLIER SAS (1 840 000 × 75 %) | 1 380 000 | |
| IDA Impôt différé actif (1 960 000 × 25 %) | 490 000 | |
| RST.CORVALLIER Résultat CORVALLIER SAS (120 000 × 75 %) | 90 000 | |
| 1521 Provisions pour pensions et obligations similaires | | 1 960 000 |
| *C2 – Provision pour indemnités de fin de carrière* | **1 960 000** | **1 960 000** |
| 6815 Dotations aux provisions d'exploitation (120 000 + 140 000) | 260 000 | |
| 6414 Indemnités et avantages divers (indemnités imputées sur la provision) | | 140 000 |
| CH_ID Produit d'impôt différé (120 000 × 25 %) | | 30 000 |
| RES_CR Résultat | | 90 000 |
| *C2R – Charge de l'exercice* | **260 000** | **260 000** |

#### c. Pourquoi un impôt différé actif (1 pt)

La provision est un passif du bilan consolidé dont la **base fiscale est nulle** : sa dotation n'est pas déductible ; les indemnités le seront lors de leur versement (hypothèse de l'annexe 1.7). La différence temporaire est **déductible** : les paiements futurs, déjà comptés en charges par le groupe, réduiront l'impôt des exercices où ils interviendront [V art. 272-8, p. 57, qui cite la provision pour indemnités de départ en retraite ; F04 R8]. Le groupe a donc une créance d'impôt future, inscrite à l'actif parce que sa récupération est probable (hypothèse de l'énoncé) [V art. 272-9 ; F04 § 1].

---

### 1.7 Opérations avec la carrière (5 pts)

#### a. Marge interne sur le stock d'argile (2,5 pts)

**Pourcentage retenu (0,5).** Pour une vente entre une entité intégrée proportionnellement et une entité intégrée globalement, l'élimination est **limitée au pourcentage d'intégration** de l'entité contrôlée conjointement [V ANC 2020-01, art. 261-4, p. 48 ; F03 § 18.3]. Seule la moitié des produits et de la marge de la carrière entre dans les comptes du groupe ; l'autre moitié revient à TUILERIE ORVAINE, à l'égard de laquelle elle est réalisée. Marge éliminée : 50 %.

**Calcul (1 pt).** Taux de marge sur le prix de vente : la marge représente 25 % du prix d'achat payé par CORVALLIER.

| | Ouverture (31/12/2025) | Clôture (31/12/2026) | Incidence de 2026 |
|---|---:|---:|---:|
| Stock acheté à la carrière | 400 000 | 560 000 | |
| Marge comprise (× 25 %) | 100 000 | 140 000 | |
| **Marge éliminée (× 50 %)** | **50 000** | **70 000** | – 20 000 (résultat) |
| Impôt différé actif (25 %) | 12 500 | 17 500 | + 5 000 |
| **Net** | **– 37 500** (réserves) | | **– 15 000** (résultat) |

L'élimination est imputée sur les réserves et le résultat de la carrière (la société qui a réalisé la marge) ; en l'absence d'intérêts minoritaires, elle revient en totalité au groupe.

**C4 (bilan) et C4R (compte de résultat), 1 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| RSV.GLAISIERES Réserves GLAISIÈRES (50 000 × 75 %) | 37 500 | |
| IDA Impôt différé actif (70 000 × 25 %) | 17 500 | |
| RST.GLAISIERES Résultat GLAISIÈRES (20 000 × 75 %) | 15 000 | |
| 31 Matières premières et fournitures (stock de CORVALLIER SAS) | | 70 000 |
| *C4 – Marge interne sur le stock d'argile* | **70 000** | **70 000** |
| 6031 Variation des stocks de matières premières et fournitures (70 000 – 50 000) | 20 000 | |
| CH_ID Produit d'impôt différé (20 000 × 25 %) | | 5 000 |
| RES_CR Résultat | | 15 000 |
| *C4R – Variation de la marge interne* | **20 000** | **20 000** |

#### b. Ventes et créance réciproques (1,5 pt)

Les produits et charges réciproques et les créances et dettes réciproques sont éliminés **dans la limite du pourcentage d'intégration** [V art. 261-3, p. 48] : ventes 2 800 000 × 50 % = 1 400 000 € ; créance 480 000 × 50 % = 240 000 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 701 Ventes de produits finis (GLAISIÈRES, intégrées à 50 %) | 1 400 000 | |
| 601 Achats stockés – Matières premières et fournitures (CORVALLIER SAS) | | 1 400 000 |
| *C3 – Ventes d'argile à CORVALLIER SAS, 0,5* | **1 400 000** | **1 400 000** |
| 401 Fournisseurs (dette de CORVALLIER SAS) | 240 000 | |
| 411 Clients (créance des GLAISIÈRES, intégrée à 50 %) | | 240 000 |
| *C5 – Créance réciproque, 0,5* | **240 000** | **240 000** |

**Part non éliminée (0,5).** Les 1 400 000 € d'achats et les 240 000 € de dette fournisseur que CORVALLIER conserve correspondent à la moitié de la carrière qui appartient à TUILERIE ORVAINE et n'est pas intégrée : ils sont traités comme des achats et une dette envers une entité extérieure au groupe [V art. 261-3].

#### c. Dividende de la carrière (1 pt)

Les dividendes intra-groupe sont éliminés [V art. 251-2, p. 45 ; F04 R14]. La carrière a versé 600 000 € ; ses réserves, intégrées à 50 %, en ont été diminuées de 300 000 €, exactement le montant reçu par CORVALLIER, qui est éliminé en totalité. Les 300 000 € versés à TUILERIE ORVAINE concernent la moitié non intégrée : ils n'apparaissent nulle part.

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.CORVALLIER Résultat CORVALLIER SAS | 300 000 | |
| RSV.CORVALLIER Réserves CORVALLIER SAS | | 300 000 |
| *C6 – Dividende reçu des GLAISIÈRES (bilan)* | **300 000** | **300 000** |
| 7611 Revenus des titres de participation | 300 000 | |
| RES_CR Résultat | | 300 000 |
| *C6R – Même élimination au compte de résultat* | **300 000** | **300 000** |

---

### 1.8 Acquisition de PARELIS et écart d'acquisition (7,5 pts)

#### a. Coût, actif net réévalué et écart d'acquisition (3 pts)

**Coût d'acquisition (1 pt).** Rémunération remise au vendeur augmentée des coûts directement imputables, nets de l'économie d'impôt [V ANC 2020-01, art. 231-2, 231-3, p. 20 ; F05 § 1.1 ; manuel] : 4 200 000 + 160 000 × 75 % = **4 320 000 €**.

**Actif net réévalué au 01/04/2026 (1,5 pt)**

| Élément | Montant |
|---|---:|
| Capital | 1 500 000 |
| Réserves | 2 300 000 |
| Résultat du 01/01 au 31/03/2026 | 200 000 |
| **Capitaux propres à la date d'acquisition** | **4 000 000** |
| Écart d'évaluation du bâtiment (1 900 000 – 1 100 000) | + 800 000 |
| Écart d'évaluation du stock de produits finis (680 000 – 600 000) | + 80 000 |
| Impôt différé passif (880 000 × 25 %) | – 220 000 |
| **Actif net réévalué** | **4 660 000** |

**Écart d'acquisition (0,5 pt).** 4 320 000 – 70 % × 4 660 000 = 4 320 000 – 3 262 000 = **1 058 000 €** [V art. 231-9 ; F05 § 1.3].

#### b. Traitement en 2026 (1,5 pt)

La durée d'utilisation de l'écart est déterminée par l'analyse documentée de l'acquisition ; elle est ici **limitée** (les avantages décroissent avec le renouvellement des gammes), mais ne peut pas être estimée de manière fiable : l'écart est alors amorti linéairement sur **10 ans** [V art. 231-11, p. 23 ; F05 § 1.3 ; manuel] (0,75). Amortissement au prorata du temps la première année, à compter de l'entrée dans le périmètre : 1 058 000 / 10 × 9/12 = **79 350 €**, inscrit sur la ligne des dotations aux amortissements des écarts d'acquisition, dans le résultat d'exploitation [V IR3 sous art. 231-12 ; F05 § 1.3] (0,75). Aucun impôt différé sur l'écart d'acquisition.

#### c. Écritures (3 pts)

**Frais d'acquisition (C7, C7R), 0,75 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation PARELIS (160 000 × 75 %) | 120 000 | |
| RST.CORVALLIER Résultat CORVALLIER SAS | | 120 000 |
| *C7 – Frais incorporés au coût des titres* | **120 000** | **120 000** |
| 695 Impôts sur les bénéfices (économie d'impôt incorporée au coût, 160 000 × 25 %) | 40 000 | |
| RES_CR Résultat | 120 000 | |
| 6226 Honoraires | | 160 000 |
| *C7R – Annulation des honoraires* | **160 000** | **160 000** |

**Résultat antérieur à l'entrée (C8), 0,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.PARELIS Résultat PARELIS (1er trimestre 2026) | 200 000 | |
| RSV.PARELIS Réserves PARELIS | | 200 000 |
| *C8 – Résultat acquis le 01/04/2026* | **200 000** | **200 000** |

Ce résultat fait partie des capitaux propres acquis et éliminés avec les titres : au compte de résultat consolidé, seuls les produits et les charges de PARELIS du 01/04 au 31/12/2026 sont cumulés (d'après la situation intermédiaire au 31/03/2026).

**Écarts d'évaluation (C9, C9R), 1,25 pt.** Bâtiment : amortissement complémentaire 800 000 / 20 × 9/12 = 30 000 € ; stock : vendu, son écart d'évaluation entre dans le coût des ventes de 2026 (80 000 €). Effet sur le résultat de PARELIS : – 110 000 × 75 % = – 82 500 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments | 800 000 | |
| RST.PARELIS Résultat PARELIS (110 000 × 75 %) | 82 500 | |
| 2813 Amortissements des constructions | | 30 000 |
| IDP Impôt différé passif ((800 000 – 30 000) × 25 %) | | 192 500 |
| RSV.PARELIS Réserves PARELIS (écarts nets à l'entrée, 880 000 × 75 %) | | 660 000 |
| *C9 – Écarts d'évaluation* | **882 500** | **882 500** |
| 68112 Dotations aux amortissements des immobilisations corporelles | 30 000 | |
| 71355 Variation des stocks de produits finis (écart du stock vendu) | 80 000 | |
| CH_ID Produit d'impôt différé (110 000 × 25 %) | | 27 500 |
| RES_CR Résultat | | 82 500 |
| *C9R – Écarts d'évaluation au compte de résultat* | **110 000** | **110 000** |

**Amortissement de l'écart d'acquisition (C11, C11R), 0,5 pt.** L'écart est inscrit par l'écriture d'élimination des titres (C10, question 1.9).

| Compte | Débit | Crédit |
|---|---:|---:|
| RST_G Résultat consolidé – part du groupe | 79 350 | |
| AMO_EA Amortissements de l'écart d'acquisition PARELIS | | 79 350 |
| *C11 – Amortissement de 2026 (bilan)* | **79 350** | **79 350** |
| DOT_EA Dotations aux amortissements des écarts d'acquisition | 79 350 | |
| RES_CR Résultat | | 79 350 |
| *C11R – Dotation de 2026* | **79 350** | **79 350** |

---

### 1.9 Partage des capitaux propres (7,5 pts)

#### a. PARELIS (2,5 pts)

Résultat retraité de la période d'avril à décembre : 720 000 – 30 000 × 75 % – 80 000 × 75 % = **637 500 €** (0,5).

| | Total retraité | Groupe (70 %) | Minoritaires (30 %) |
|---|---:|---:|---:|
| Capital | 1 500 000 | 1 050 000 | 450 000 |
| Réserves à l'entrée (2 300 000 + 200 000 du 1er trimestre) | 2 500 000 | 1 750 000 | 750 000 |
| Écarts d'évaluation nets à l'entrée | 660 000 | 462 000 | 198 000 |
| **Capitaux propres retraités hors résultat** | **4 660 000** | **3 262 000** | **1 398 000** |
| Élimination des titres (coût d'acquisition) | | – 4 320 000 | |
| Écart d'acquisition inscrit à l'actif | | + 1 058 000 | |
| **Réserves consolidées** | | **0** | **1 398 000** |
| **Résultat retraité d'avril à décembre** | **637 500** | **446 250** | **191 250** |

Tableau : 2 pts.

L'acquisition datant de l'exercice, les réserves de PARELIS sont toutes antérieures à l'entrée : elles sont acquises, éliminées avec les titres, et ne laissent aucune réserve consolidée au groupe. Le résultat part du groupe de PARELIS se réduit à 446 250 – 79 350 = 366 900 € après l'amortissement de l'écart d'acquisition, qui revient au seul groupe.

#### b. GLAISIÈRES DU BOURBONNAIS (1,5 pt)

| | 100 % | Intégré (50 %) = part du groupe | Minoritaires |
|---|---:|---:|---:|
| Capital | 2 000 000 | 1 000 000 | — |
| Réserves | 3 400 000 | 1 700 000 | — |
| Marge interne d'ouverture, nette d'impôt (question 1.7 a) | – 75 000 | – 37 500 | — |
| **Capitaux propres retraités hors résultat** | **5 325 000** | **2 662 500** | — |
| Élimination des titres (souscrits au nominal) | | – 1 000 000 | — |
| **Réserves consolidées** | | **1 662 500** | **0** |
| Résultat 800 000 – marge de 2026 nette 30 000 | 770 000 | **385 000** | **0** |

Seule la fraction de 50 % est intégrée : il n'y a rien à partager avec TUILERIE ORVAINE, dont la part ne figure pas dans les comptes du groupe [V art. 221-3, 261-1]. Les réserves consolidées représentent la moitié des réserves accumulées depuis la création, au nominal.

#### c. Écritures (1,5 pt)

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM Capital PARELIS | 1 500 000 | |
| RSV.PARELIS Réserves PARELIS retraitées (2 300 000 + 200 000 + 660 000) | 3 160 000 | |
| RST.PARELIS Résultat PARELIS retraité (920 000 – 200 000 – 82 500) | 637 500 | |
| EA Écart d'acquisition PARELIS | 1 058 000 | |
| 261 Titres de participation PARELIS (4 200 000 + 120 000) | | 4 320 000 |
| RSV_M Intérêts minoritaires – capital et réserves (30 % × 4 660 000) | | 1 398 000 |
| RST_G Résultat consolidé – part du groupe (70 % × 637 500) | | 446 250 |
| RST_M Intérêts minoritaires – résultat (30 % × 637 500) | | 191 250 |
| *C10 – Élimination des titres PARELIS et partage, 1* | **6 355 500** | **6 355 500** |
| CAP_ELIM Capital GLAISIÈRES intégré (50 %) | 1 000 000 | |
| RSV.GLAISIERES Réserves GLAISIÈRES intégrées et retraitées | 1 662 500 | |
| RST.GLAISIERES Résultat GLAISIÈRES intégré et retraité | 385 000 | |
| 261 Titres de participation GLAISIÈRES | | 1 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 1 662 500 |
| RST_G Résultat consolidé – part du groupe | | 385 000 |
| *C12 – Élimination des titres GLAISIÈRES, 0,5* | **3 047 500** | **3 047 500** |

Dans C10, la part du groupe dans les réserves de PARELIS (70 % × 4 660 000 = 3 262 000) est entièrement compensée par les titres, déduction faite de l'écart d'acquisition : aucune ligne RSV_G n'est nécessaire.

#### d. Agrégats (2 pts)

| | Réserves consolidées | Résultat part du groupe |
|---|---:|---:|
| CORVALLIER SAS, comptes individuels | 31 500 000 | 5 400 000 |
| Amortissements dérogatoires éliminés (C1) | + 727 686 | – 112 719 |
| Indemnités de fin de carrière (C2) | – 1 380 000 | – 90 000 |
| Dividende des GLAISIÈRES (C6) | + 300 000 | – 300 000 |
| Frais d'acquisition des titres PARELIS (C7) | | + 120 000 |
| **CORVALLIER SAS retraitée** | **31 147 686** | **5 017 281** |
| PARELIS (part du groupe, après titres et écart d'acquisition) | 0 | + 446 250 |
| Amortissement de l'écart d'acquisition | | – 79 350 |
| GLAISIÈRES (part du groupe) | + 1 662 500 | + 385 000 |
| **Total** | **32 810 186** | **5 769 181** |

Capitaux propres part du groupe : 8 000 000 + 32 810 186 + 5 769 181 = **46 579 367 €** (1,5 pour les réserves et le résultat). Intérêts minoritaires au 31/12/2026 : 1 398 000 + 191 250 = **1 589 250 €**, dont résultat 191 250 € (0,5) ; capitaux propres de l'ensemble 48 168 617 € ; résultat de l'ensemble 5 960 431 €.

---

### 1.10 Processus de consolidation (2 pts)

| Phase | Traitements du dossier |
|---|---|
| 1. Retraitements préparatoires : élimination des écritures fiscales | Amortissements dérogatoires du four et de la presse (C1, C1R) |
| 2. Homogénéisation selon le manuel | Provision pour indemnités de fin de carrière (C2, C2R) ; PARELIS déjà homogène |
| 3. Cumul des comptes retraités | CORVALLIER et PARELIS à 100 % (PARELIS : bilan au 31/12, produits et charges depuis le 01/04) ; GLAISIÈRES à 50 %, poste par poste |
| 4. Éliminations des opérations internes | Ventes, marge, créance et dividende de la carrière, dans la limite de 50 % (C3 à C6) |
| 5. Écarts d'évaluation et écart d'acquisition | Frais incorporés au coût des titres (C7), résultat acquis (C8), écarts d'évaluation (C9), écart d'acquisition et son amortissement (C10, C11) |
| 6. Élimination des titres et partage | C10 (PARELIS, 70 / 30), C12 (GLAISIÈRES, sans minoritaires) |

Tableau : 1 pt.

**Pourquoi les dérogatoires avant le partage (0,5).** Le partage répartit des capitaux propres **retraités** entre réserves et résultat, groupe et minoritaires ; il doit porter sur des comptes débarrassés des écritures fiscales et établis selon les méthodes du groupe. Éliminer après le partage obligerait à corriger chaque part ; et la frontière réserves / résultat n'est juste que si le stock d'ouverture est déjà porté en réserves et la reprise de l'exercice retirée du résultat.

**Ce que change l'intégration proportionnelle (0,5).** Le cumul ne reprend que **50 % de chaque poste** de la carrière (actifs, dettes, produits, charges), après ses retraitements ; il ne fait apparaître aucun intérêt minoritaire ; les éliminations avec la carrière sont limitées à ce pourcentage, et l'élimination des titres porte sur 50 % de son capital.

---

### 1.11 Tableau des flux de trésorerie (5 pts)

#### a. Flux d'investissement et de financement de 2026 (4 pts)

Principes : en intégration globale, les flux de PARELIS ne sont repris qu'à compter de son entrée (01/04/2026) ; les flux de la carrière sont repris à 50 % ; les flux entre sociétés consolidées sont éliminés ; l'acquisition d'une filiale figure sur une ligne d'investissement, pour son prix d'achat **diminué de la trésorerie acquise** [V ANC 2020-01, art. 282-43, note 3, p. 92 ; F14 § 1.5] ; les honoraires, compris dans le coût d'acquisition en consolidation [V art. 231-2, 231-3], y sont rattachés (application, S).

| Flux de trésorerie liés aux opérations d'investissement | Montant |
|---|---:|
| Acquisitions d'immobilisations : – (3 100 000 + 420 000 + 50 % × 640 000) | – 3 840 000 |
| Produit de cession d'immobilisations, net d'impôt : 200 000 – 25 % × 120 240 | + 169 940 |
| Incidence de l'acquisition de PARELIS (ligne du modèle consacrée aux entrées et sorties du périmètre) : – (4 200 000 + 160 000) + 380 000 | – 3 980 000 |
| **Flux net de trésorerie lié aux opérations d'investissement** | **– 7 650 060** |
| **Flux de trésorerie liés aux opérations de financement** | |
| Dividendes versés aux actionnaires de l'entité consolidante | – 1 500 000 |
| Dividendes versés aux minoritaires des sociétés intégrées | 0 |
| Augmentations de capital en numéraire | 0 |
| Émissions d'emprunts | + 2 500 000 |
| Remboursements d'emprunts : – (900 000 + 160 000 + 50 % × 400 000) | – 1 260 000 |
| **Flux net de trésorerie lié aux opérations de financement** | **– 260 000** |

Répartition : acquisitions d'immobilisations 0,75 ; cession nette d'impôt 0,75 ; acquisition de PARELIS 1 ; financement 1,25 (dividendes 0,5 ; emprunts 0,75) ; totaux 0,25.

- **Cession** : le modèle présente le produit de cession **net d'impôt** ; le manuel retient l'impôt exigible sur la plus-value fiscale (120 240 × 25 % = 30 060), retiré des flux liés à l'activité.
- **PARELIS** : les honoraires, inclus dans le coût d'acquisition en consolidation, sont rattachés à l'acquisition ; leur économie d'impôt reste dans les flux liés à l'activité. Les 380 000 € de disponibilités de PARELIS entrent dans la trésorerie du groupe à l'acquisition. Les 420 000 € d'investissements et les 160 000 € de remboursements de PARELIS sont postérieurs au 01/04/2026.
- **Dividendes** : en ANC, les dividendes versés figurent en financement [V art. 282-43] ; PARELIS n'a rien distribué depuis son entrée ; la carrière a versé à CORVALLIER la totalité de sa quote-part intégrée (question b).

#### b. Le dividende de la carrière (1 pt)

La carrière a versé 600 000 € ; le tableau consolidé n'en reprend que **50 %**, soit 300 000 € versés, qui sont précisément les 300 000 € **reçus par CORVALLIER** : décaissement et encaissement sont internes au groupe et s'annulent (0,5). Les 300 000 € versés à TUILERIE ORVAINE relèvent de la moitié non intégrée : ils ne figurent pas plus dans le tableau que dans le bilan ou le résultat consolidés. Pour une filiale intégrée globalement, au contraire, 100 % de ses flux sont repris : la part de son dividende versée aux associés minoritaires sort du groupe et figure en financement, sur la ligne « dividendes versés aux minoritaires des sociétés intégrées » (0,5).

---

### Réponses tolérées
- **1.1** : comptes consolidés « soumis à l'approbation des associés », si le candidat écrit que la loi ne l'impose pas à la SAS et qu'il s'agit d'une disposition des statuts : – 0,25 ; nombre de commissaires aux comptes non précisé : – 0,25.
- **1.2** : définition de l'importance relative présentée à partir du seul cadre conceptuel, sans IAS 1, si les deux critères (nature et ampleur) et le contexte d'ensemble sont donnés.
- **1.3** : PATINÉA omise du tableau, si son exclusion est justifiée à la question 1.2 : – 0,25 ; colonne des minoritaires portant « 0 % » ou « 50 % non intégrés » pour la carrière, si l'absence d'intérêts minoritaires est expliquée.
- **1.4** : comparaison faite après élimination des ventes internes (chiffre d'affaires de 3 600 000, 1 800 000 et 0), si elle est cohérente.
- **1.5 b** : élimination présentée en deux écritures (four et presse), si réserves, résultat et impôt différé sont justes.
- **1.5 c** : incidence individuelle présentée sans la reprise, en deux lignes (plus-value comptable 40 000 et reprise 80 240), si l'écart avec le consolidé est expliqué.
- **1.6 b** : charge de 2026 présentée en dotation de 260 000 et reprise de 140 000 (7815), en conservant le 6414, si le résultat (– 120 000 avant impôt) est juste.
- **1.7 a** : marge éliminée à 100 % puis « répartie » pour moitié, si le candidat conclut que seule la moitié est éliminée.
- **1.8 c** : écarts d'évaluation et élimination des titres regroupés dans une seule écriture, si elle est équilibrée ; écart du stock vendu porté au compte 603 ou au coût des ventes, si l'effet en résultat est juste.
- **1.9 a** : tableau présenté avec les titres à 4 320 000 et l'écart d'acquisition sur une ligne distincte, ou avec les titres diminués de l'écart d'acquisition (3 262 000), si les réserves consolidées sont nulles.
- **1.10** : frais d'acquisition rattachés à l'élimination des titres ; autre découpage en phases, si chaque traitement y figure et si l'ordre retraitements, cumul, éliminations, partage est justifié.
- **1.11 a** : produit de cession présenté pour 200 000 € avec un renvoi à l'impôt dans les flux liés à l'activité, si le candidat signale que le modèle retient le produit net d'impôt : – 0,25 ; honoraires présentés en flux liés à l'activité : – 0,25.
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (erreur non sanctionnée deux fois).

### Erreurs fréquentes
- **Contexte légal** : comptes consolidés « approuvés par l'assemblée » par analogie avec la SA ; dividende fixé sur le résultat consolidé ; un seul commissaire aux comptes ; le cabinet qui établit les comptes présenté comme leur certificateur (`JUR-F06`).
- **Importance relative** : seuil de 1 % présenté comme une règle ; exclusion justifiée par la seule taille, sans la nature de l'entité ni l'appréciation « avec les autres entités » ; titres de PATINÉA supprimés du bilan consolidé (`JUR-F07`).
- **Périmètre** : carrière mise en équivalence ou intégrée globalement ; intérêts minoritaires de 50 % sur la carrière ; PARELIS consolidée depuis le 01/01/2026, résultat de 920 000 € pris en totalité.
- **Effets de la méthode** : capitaux propres part du groupe présentés comme différents selon la méthode ; intégration proportionnelle présentée comme possible en IFRS (`JUR-F01`).
- **Dérogatoires** : reprise de 2026 laissée dans le résultat consolidé ; stock d'ouverture porté en résultat ; impôt différé actif au lieu de passif ; stock de la presse oublié parce que la presse est sortie ; plus-value consolidée calculée sur la valeur nette fiscale (`JUR-F05`, `JUR-G06`).
- **Retraites** : provision dite obligatoire en ANC ; variation seule (120 000) portée en dotation sans traiter les indemnités versées, ou indemnités déduites deux fois ; impôt différé passif ; provision d'ouverture passée en résultat (`JUR-G06`).
- **Carrière** : marge, ventes ou créance éliminées à 100 % ; marge calculée sur le coût (560 000 × 25 / 125) alors que le taux porte sur le prix de vente ; dividende éliminé pour 600 000 € ; impôt différé omis.
- **PARELIS** : frais d'acquisition omis ou retenus bruts (`JUR-G02`) ; résultat du premier trimestre laissé dans le résultat consolidé ; écart du stock oublié dans le résultat de la période ; écart d'acquisition amorti sur 12 mois, ou non amorti malgré la durée limitée ; impôt différé calculé sur l'écart d'acquisition.
- **Partage** : partage effectué sur des capitaux propres non retraités (`JUR-G01`, `JUR-G04`) ; amortissement de l'écart d'acquisition imputé en partie aux minoritaires ; intérêts minoritaires calculés sur la carrière ; capital de PARELIS ajouté au capital consolidé.
- **Flux de trésorerie** : prix de PARELIS porté sans déduire la trésorerie acquise ; flux de PARELIS repris depuis le 01/01 ; flux de la carrière repris à 100 % ; dividende de la carrière laissé en financement ; plus-value portée en investissement à la place du prix ; montants sans calcul (`JUR-F02`) ; écritures non équilibrées (`JUR-F04`).

### Références
- Code de commerce : L. 227-1, L. 227-9, L. 233-16, L. 233-20, L. 233-21, L. 233-26, L. 232-11, L. 232-12, L. 232-23 [V, F03 § 18.1] ; L. 225-100 (non applicable à la SAS) [V] ; L. 821-41, L. 821-53, L. 821-54 [V, F03 § 18.1, F09, F11] ; L. 233-19 II 2° [V, F03 § 18.2].
- Règlement ANC n° 2020-01 : art. 211-1, 211-4, 211-10, 211-11, 212-1, 212-3 [V, F03 § 2 et § 18.2] ; art. 221-1, 221-3, 261-1, 261-3 à 261-5 [V, F03 § 3 et § 18.3] ; art. 231-2, 231-3, 231-9, 231-11, 272-13 [V, F05] ; art. 251-2, 271-3, 271-5, 272-1, 272-8, 272-9 [V, F04] ; art. 282-41 à 282-43 [V, F14 § 1.5].
- PCG : art. 121-5, 324-1 (méthode de référence des engagements de retraite) [V, F04 R8].
- IFRS : IAS 1 § 7 [V, F03 § 18.2] ; IFRS 11, appendice A, § 20, 24, B19 à B32 [V, F03 § 3 et § 18.4] ; cadre conceptuel de 2018, importance relative [S, F03 § 7.2 et § 18.2].

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, différence avec une liquidation, date de la transmission, référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2 |
| 2.2 Régime fiscal, déficit de TUFTÉO, agrément, projet de 2029, sort du boni | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 3 |
| 2.3 Valeur de transmission et rôle des valeurs estimées | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 1,5 |
| 2.4 Actifs et passifs reçus, actif net transmis, absence de provision pour impôts | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 3 |
| 2.5 Boni et sa décomposition | `1.2.e` Calculer et analyser le boni ou mali de fusion | 5 |
| 2.6 a) Réception des actifs et des passifs | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 3 |
| 2.6 b) Annulation des titres et boni | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes ; `1.2.e` | 2,5 |
| 2.7 Dettes et créances réciproques, stock et ventes de la période, frais | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 3 |
| 2.8 Note à M. VERDALÈNE | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Qualification, différence avec une liquidation, date et référentiel (2 pts)

- *Qualification (0,75 pt).* VERDALÈNE, personne morale, détient les 8 000 actions de TUFTÉO. La dissolution d'une société dont toutes les parts ou actions sont réunies en une seule main entraîne, lorsque l'associé unique est une personne morale, la **transmission universelle du patrimoine** de la société dissoute à cet associé, **sans liquidation** [V C. civ. art. 1844-5, F02 § 1 ; PCG art. 710-2, F01 § 1]. C'est pourquoi VERDALÈNE peut décider seule l'opération : la décision de l'associée unique suffit, sans traité ni accord d'une autre société. La règle ne s'appliquerait pas si l'associé unique était une personne physique. Aucune action n'est émise : VERDALÈNE ne peut pas se rémunérer elle-même ; il n'y a **ni parité, ni augmentation de capital** ; les titres TUFTÉO disparaissent et sont remplacés par les éléments du patrimoine reçu.
- *Différence avec une liquidation amiable (0,5 pt).* Une liquidation amiable aurait conduit à vendre les actifs de TUFTÉO, à payer ses dettes, puis à verser le solde à VERDALÈNE : l'atelier aurait été cédé ou démantelé. Ici, rien n'est réalisé ni payé : le patrimoine de TUFTÉO passe **en bloc**, actif et passif, à VERDALÈNE, qui poursuit l'activité de Felletin et devient débitrice des dettes de sa filiale. M. VERDALÈNE économise ainsi le traité d'une fusion, mais l'opération a malgré tout un coût (honoraires et publication, annexe 2.6).
- *Date de la transmission (0,5 pt).* Les créanciers de TUFTÉO peuvent faire opposition dans les trente jours de la publication ; la transmission du patrimoine et la disparition de la société n'interviennent qu'**à l'issue de ce délai** [V C. civ. art. 1844-5, F02 § 1]. Le délai expire le 30 avril 2027, sans opposition attendue (annexe 2.1) : le patrimoine passe à VERDALÈNE le **1er mai 2027**. L'opération n'a **aucun effet antérieur**, le code civil ne le prévoyant pas : VERDALÈNE l'enregistre à cette date, sur la base du bilan de TUFTÉO au 30 avril 2027 [V PCG art. 760-3, F01 § 1 et § 2.4 ; annexe 2.7]. Le résultat de janvier à avril 2027 reste celui de TUFTÉO ; il est compris dans l'actif net transmis.
- *Référentiel (0,25 pt).* Les comptes individuels de VERDALÈNE suivent le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui vise les confusions de patrimoine de l'article 1844-5 du code civil et leur consacre des règles propres [V PCG art. 710-1 et 760-1 à 760-3, F01 § 1].

---

### 2.2 Régime fiscal, déficit et agrément (3 pts)

- *Régime applicable (0,5 pt).* Fiscalement, la transmission universelle du patrimoine d'une filiale à son associée unique est une **fusion** pour laquelle les titres détenus par la société qui reçoit le patrimoine ne sont pas échangés [V CGI art. 210-0 A, I, 1° a et 3°, F02 § 1]. Les deux sociétés sont soumises à l'impôt sur les sociétés : l'opération relève **de plein droit** du régime de faveur de l'art. 210 A, **sauf option pour le droit commun** [V BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1]. Aucune option n'est envisagée (annexe 2.1) : le régime de faveur s'applique.
- *Principales conséquences (0,5 pt).*
  - **TUFTÉO** : les plus-values latentes sur l'immeuble et les machines (400 000 + 80 000 = 480 000 €, annexe 2.4) **ne sont pas imposées** [V CGI art. 210 A-1, F02 § 2] ; la provision pour garanties, déduite et toujours justifiée, n'est pas réintégrée [V art. 210 A-2] ; le **bénéfice de janvier à avril 2027** (20 000 €) est imposé dans la dernière déclaration de TUFTÉO, quel que soit le régime [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2], mais il est entièrement couvert par les déficits antérieurs : aucun impôt n'est dû [V CGI art. 209 I, F02 § 3].
  - **VERDALÈNE** s'engage à reprendre la provision pour garanties, à calculer la plus-value future du terrain d'après sa valeur fiscale chez TUFTÉO, et à inscrire les stocks à leur valeur fiscale [V CGI art. 210 A-3, a, c et e, F02 § 4] ; les biens amortissables étant repris à leur valeur comptable, avec leurs valeurs d'origine et leurs amortissements, il n'y a aucune plus-value à réintégrer et VERDALÈNE poursuit les plans d'amortissement de TUFTÉO [V BOI-IS-FUS-10-20-40-20 § 170 et 180, F01 § 3.2].
- *Déficit transférable (0,5 pt).* Déficits de 2024 et 2025 : 260 000 + 180 000 = 440 000 € ; imputation sur le bénéfice de 2026 : – 50 000 € ; déficit reportable au 31/12/2026 : **390 000 €** ; imputation sur le bénéfice de la dernière période (janvier-avril 2027) : – 20 000 € ; déficit susceptible d'être transféré : **370 000 €** [V CGI art. 209 I : le déficit s'impute sur les bénéfices suivants ; aucune option pour le report en arrière, annexe 2.5].
- *Conditions et procédure (0,75 pt).* Les déficits d'une société dont le patrimoine est transmis dans une opération placée sous le régime de l'art. 210 A ne passent à la société bénéficiaire que **sur agrément**, ce qui vise expressément les dissolutions sans liquidation [V CGI art. 209 II-1 ; BOI-SJ-AGR-20-30-10-10 § 10 et 60, F02 § 3]. L'agrément est délivré si [V art. 209 II-1, a à d ; BOI § 120 à 220] :
  - a) l'opération est justifiée économiquement et obéit à des motivations principales autres que fiscales : regroupement de la gestion, des achats de laine et de la vente des deux gammes ;
  - b) l'activité à l'origine des déficits n'a pas changé de manière significative pendant la période où ils sont nés : même activité, même personnel, mêmes machines, même clientèle (annexe 2.5) ;
  - c) VERDALÈNE poursuit cette activité **pendant au moins trois ans** à compter de la transmission, soit **jusqu'au 30 avril 2030**, sans changement significatif (clientèle, emplois, moyens d'exploitation, lieux d'exploitation, nature et volume d'activité) ; elle s'y engage dans la demande [V BOI § 180 et 190] ;
  - d) les déficits ne viennent pas de la gestion d'un patrimoine mobilier ou immobilier : ils viennent d'une activité industrielle.
  - La **dispense d'agrément** ne joue pas : elle suppose des déficits transférés inférieurs à 200 000 € [V art. 209 II-2, F02 § 3]. La demande, établie par VERDALÈNE et contresignée par le représentant légal de TUFTÉO, doit être déposée **avant la date de transmission du patrimoine**, et non seulement avant la décision : avant le **1er mai 2027**, faute de quoi la forclusion lui serait opposée [V CGI art. 1649 nonies, I ; BOI § 250, 260 et 280, F02 § 3].
- *Projet de regroupement de 2029 (0,25 pt).* Transférer les machines à Aubusson, fermer l'atelier de Felletin et ne plus vendre qu'aux clients de VERDALÈNE changerait les lieux d'exploitation, les emplois et la clientèle **avant le 30 avril 2030** : la condition c) ne serait pas respectée. L'agrément serait retiré, l'impôt économisé grâce au déficit deviendrait exigible avec l'intérêt de retard [V CGI art. 1649 nonies A, 1, F02 § 3]. Si M. VERDALÈNE tient à ce projet, il doit le reporter après le 30 avril 2030 ou renoncer au transfert du déficit.
- *Absence d'agrément (0,25 pt).* Si la demande n'est pas déposée à temps ou si l'agrément est refusé, les 370 000 € de déficit sont **définitivement perdus** : TUFTÉO disparaît et VERDALÈNE ne peut pas les imputer sur ses bénéfices, soit une économie d'impôt perdue de 370 000 × 25 % = **92 500 €** [V BOI § 1, F02 § 3]. Le régime de faveur de l'opération n'est pas remis en cause : l'agrément ne conditionne que le transfert des déficits.
- *Sort fiscal du boni (0,25 pt).* Sous le régime de faveur, le profit dégagé par VERDALÈNE lors de l'annulation des titres TUFTÉO n'est pas imposé : la part inscrite en résultat financier (340 000 €, voir 2.5) est déduite extra-comptablement, la part inscrite en capitaux propres ne passe pas par le résultat [V CGI art. 210 A-1, al. 2 ; BOI-IS-FUS-10-50-20 § 1, F02 § 2 bis].

---

### 2.3 Valeur de transmission et valeurs estimées (1,5 pt)

- *Situation de contrôle (0,5 pt).* VERDALÈNE détient 100 % des droits de vote de TUFTÉO : elle la contrôle **de manière exclusive** [V PCG art. 741-2, F01 § 2.1]. L'une des sociétés contrôlant l'autre, l'opération est réalisée **sous contrôle commun** [V art. 741-1, F01 § 2.1].
- *Règle (0,5 pt).* Une confusion de patrimoine est toujours réalisée entre entités sous contrôle commun : les actifs et passifs de la société dissoute sont **transmis à leur valeur comptable** [V PCG art. 760-1 et 744-2, F01 § 2.4 ; annexe 2.7]. Le sens de l'opération est sans objet, et l'exception de l'actif net comptable insuffisant ne s'applique pas aux confusions de patrimoine [V art. 743-3, F01 § 2.4]. Retenir les valeurs des experts reviendrait à **réévaluer** l'immeuble et les machines lors d'une opération qui ne change pas le contrôle, ce que le PCG écarte [V art. 743-1, F01 § 2.3] : VERDALÈNE reprend les valeurs du bilan de TUFTÉO au 30 avril 2027.
- *Utilité des valeurs estimées (0,5 pt).* Elles informent M. VERDALÈNE de ce que la valeur comptable ne montre pas : l'immeuble et les machines valent **480 000 €** de plus que leur valeur nette comptable, de sorte que le patrimoine reçu vaut nettement plus que le coût des titres (1 200 000 €) et qu'aucune perte de valeur des titres n'est à craindre. Elles lui donnent aussi une mesure de l'impôt latent : ces plus-values ne sont pas imposées lors de l'opération, mais VERDALÈNE, qui reprend les valeurs fiscales de TUFTÉO, les paierait si elle vendait un jour l'immeuble ou les machines (480 000 × 25 % = 120 000 €). Elles sont utiles pour décider du sort de l'atelier de Felletin. Elles ne sont inscrites nulle part.

---

### 2.4 Actifs et passifs reçus, actif net transmis (3 pts)

- *Actif net comptable transmis (1,5 pt)* :

| Élément | Valeur brute | Amortissements et dépréciations | Valeur nette |
|---|---:|---:|---:|
| Terrain de l'atelier de Felletin | 80 000 | | 80 000 |
| Bâtiment de l'atelier | 1 200 000 | 660 000 | 540 000 |
| Machines à tufter et matériel de finition | 1 640 000 | 1 020 000 | 620 000 |
| Fils et toiles de fond | 290 000 | 34 000 | 256 000 |
| Tapis tuftés | 344 000 | | 344 000 |
| Clients (dont 84 000 dus par VERDALÈNE) | 560 000 | 24 000 | 536 000 |
| Banques | 214 000 | | 214 000 |
| **Total de l'actif transmis** | **4 328 000** | **1 738 000** | **2 590 000** |
| Provision pour garanties données aux clients | | | – 28 000 |
| Emprunt auprès d'un établissement de crédit | | | – 420 000 |
| Fournisseurs (dont 52 000 dus à VERDALÈNE) | | | – 236 000 |
| Dettes sociales | | | – 142 000 |
| Dettes fiscales, hors impôt sur les sociétés | | | – 44 000 |
| **Actif net comptable transmis** | | | **1 720 000** |

Contrôle : il est égal aux capitaux propres de TUFTÉO au 30 avril 2027 (400 000 + 40 000 + 1 650 000 – 390 000 + 20 000). Les dettes et créances entre les deux sociétés font partie du patrimoine transmis ; elles s'éteignent ensuite (voir 2.7). Barème : actifs (0,5), provision et dettes (0,5), actif net et contrôle (0,5).

- *Ce que VERDALÈNE reprend (0,75 pt).* En valeur comptable, VERDALÈNE inscrit chaque actif pour sa **valeur brute d'origine**, et reprend séparément ses **amortissements** et ses **dépréciations** (fils de coloris abandonnés, clients douteux) ; elle poursuit les plans d'amortissement de TUFTÉO [V PCG art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170 et 180, F01 § 3.2]. Elle reprend la **provision pour garanties**, qui couvre un passif de TUFTÉO, ce qu'exige aussi le régime de faveur [V CGI art. 210 A-3 a, F02 § 4]. TUFTÉO n'a **aucune provision réglementée** (annexe 2.2) : il n'y a rien à reconstituer ; si elle en avait, elles seraient comprises dans l'actif net transmis, puisqu'elles font partie des capitaux propres [V PCG art. 214-8 et 313-1, F01 § 8].
- *Aucune provision pour impôts (0,75 pt).* Dans une opération à la valeur réelle placée sous le régime de faveur, une provision pour impôts est intégrée aux apports parce que les valeurs d'apport dépassent les valeurs fiscales : les plus-values comptabilisées seront imposées plus tard chez la société qui reçoit les biens [V F01 § 3.3 ; F02 § 6]. Ici, chaque élément est repris à sa valeur comptable, **égale à sa valeur fiscale** (annexe 2.5) : aucune plus-value n'est comptabilisée, il n'existe aucun écart entre valeur comptable et valeur fiscale, donc aucun impôt futur à provisionner. Les plus-values latentes de 480 000 € ne figurent pas au bilan ; leur imposition éventuelle à la cession des biens n'est pas provisionnée. Aucun impôt différé actif n'est non plus constaté pour le déficit : les comptes individuels n'en comptabilisent pas.

---

### 2.5 Boni et sa décomposition (5 pts)

- *Valeur comptable des titres (0,75 pt).* Prix 1 160 000 + frais d'acquisition inscrits dans le coût 40 000 = **1 200 000 €**, jamais dépréciés (annexe 2.2).
- *Résultat de l'annulation (1 pt).* Actif net reçu à hauteur de la participation (100 %) : 1 720 000 € ; valeur comptable de la participation : 1 200 000 €. L'écart est positif : **boni = 1 720 000 – 1 200 000 = 520 000 €** [V PCG art. 745-2, F01 § 5.2 ; annexe 2.7]. Il n'y a pas de mali, donc rien à affecter aux actifs.
- *Résultats accumulés depuis l'acquisition et non distribués (1,5 pt).* Ils sont déterminables de manière fiable : les capitaux propres de TUFTÉO à l'acquisition et à la date de l'opération sont connus, et ils n'ont varié que par les résultats et les dividendes (annexe 2.2). Deux calculs concordants (0,75 chacun) :
  - par les capitaux propres : 1 720 000 – 1 380 000 = **340 000 €** ;
  - par les résultats : bénéfices de 2018 à 2023 1 010 000 – pertes de 2024 et 2025 440 000 + bénéfice de 2026 50 000 + bénéfice de janvier-avril 2027 20 000 – dividendes versés 300 000 = **340 000 €**.
  Les dividendes sont déduits : VERDALÈNE les a déjà comptabilisés en produits financiers de 2019, 2022 et 2023 ; les compter une seconde fois dans le boni ferait apparaître deux fois les mêmes résultats.
- *Décomposition (0,75 pt)* [V art. 745-2, F01 § 5.2] :

| Part du boni | Montant | Inscription |
|---|---:|---|
| 100 % des résultats accumulés depuis le 2 janvier 2018 et non distribués | **340 000** | Résultat financier (768) |
| Surplus | **180 000** | Capitaux propres (1042) |
| **Boni** | **520 000** | |

- *Effet des pertes et origine de la part en capitaux propres (1 pt).*
  - Les pertes de 2024 et de 2025 (440 000 €) ont diminué les capitaux propres de TUFTÉO, donc l'actif net reçu : sans elles, les résultats accumulés et non distribués seraient de 780 000 € et le boni de 960 000 €. Elles réduisent **du même montant** le boni et sa part en résultat (780 000 → 340 000) : VERDALÈNE ne peut présenter comme un produit de 2027 que les bénéfices que sa filiale a réellement conservés depuis qu'elle la détient, pertes déduites (0,5).
  - La part inscrite en capitaux propres, **180 000 €**, est égale à l'écart entre les capitaux propres de TUFTÉO à l'acquisition et le coût des titres (1 380 000 – 1 200 000) : VERDALÈNE a payé TUFTÉO en 2018 moins que ses capitaux propres, compte tenu de l'âge des machines et de la faible rentabilité de l'atelier. Cette part correspond à des capitaux propres achetés, non à un résultat dégagé depuis l'acquisition : elle ne passe pas en résultat, et les pertes ne l'ont pas modifiée (0,5).

---

### 2.6 Écritures du 1er mai 2027 chez VERDALÈNE (5,5 pts)

**a) Réception des actifs et des passifs de TUFTÉO (3 pts)**

**A1 — Réception du patrimoine à la valeur comptable.** Actifs à leur valeur brute (1) ; amortissements et dépréciations repris (1) ; provision et dettes (0,5) ; contrepartie de l'actif net reçu et contrôle d'équilibre (0,5).

| Compte | Débit | Crédit |
|---|---:|---:|
| 211 Terrains (atelier de Felletin) | 80 000 | |
| 2131 Bâtiments (atelier de Felletin) | 1 200 000 | |
| 2154 Matériels industriels (machines à tufter et de finition) | 1 640 000 | |
| 31 Matières premières et fournitures (fils et toiles) | 290 000 | |
| 355 Produits finis (tapis tuftés) | 344 000 | |
| 411 Clients | 560 000 | |
| 512 Banques | 214 000 | |
| 2813 Amortissements des constructions | | 660 000 |
| 2815 Amortissements des installations, matériel et outillage industriels | | 1 020 000 |
| 391 Dépréciations des matières premières et fournitures | | 34 000 |
| 491 Dépréciations des comptes de clients | | 24 000 |
| 1512 Provisions pour garanties données aux clients | | 28 000 |
| 164 Emprunts auprès des établissements de crédit | | 420 000 |
| 401 Fournisseurs | | 236 000 |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | | 142 000 |
| 44 État et autres collectivités publiques (dettes fiscales) | | 44 000 |
| 4561 Associés – Comptes d'apport en société (actif net reçu de TUFTÉO) | | 1 720 000 |
| **Total** | **4 328 000** | **4 328 000** |

**b) Annulation des titres et boni (2,5 pts)**

**A2 — Annulation des 8 000 actions TUFTÉO.** Annulation des titres pour leur valeur comptable (0,75) ; part du boni en résultat financier (0,75) ; part en capitaux propres (0,5) ; comptes conformes à la convention de l'annexe 2.7, le PCG ne prévoyant aucun compte de boni [F01 § 5.2] (0,25) ; contrôle : 1 200 000 + 340 000 + 180 000 = 1 720 000 (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 1 720 000 | |
| 261 Titres de participation (TUFTÉO) | | 1 200 000 |
| 768 Autres produits financiers (boni, part en résultat) | | 340 000 |
| 1042 Primes de fusion (boni, part en capitaux propres) | | 180 000 |
| **Total** | **1 720 000** | **1 720 000** |

---

### 2.7 Dettes et créances réciproques, stock, ventes de la période, frais (3 pts)

Après la transmission, VERDALÈNE est à la fois créancière et débitrice des mêmes obligations : les créances et les dettes s'éteignent par **confusion** [V C. civ. art. 1349, F01 § 8].

**A3 — Tapis tuftés dus par VERDALÈNE (0,75 pt).**

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette de VERDALÈNE envers TUFTÉO) | 84 000 | |
| 411 Clients (créance de TUFTÉO sur VERDALÈNE, reçue avec le patrimoine) | | 84 000 |

**A4 — Prestations administratives dues par TUFTÉO (0,75 pt).**

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette de TUFTÉO envers VERDALÈNE, reçue avec le patrimoine) | 52 000 | |
| 411 Clients (créance de VERDALÈNE sur TUFTÉO) | | 52 000 |

*Stock et ventes de la période (0,75 pt).* Les tapis tuftés en stock chez VERDALÈNE (126 000 €) restent inscrits à leur **coût d'achat** : ils ont été achetés à une autre personne avant la transmission, et les comptes individuels n'éliminent aucune marge interne, ce que seuls des comptes consolidés feraient ; VERDALÈNE n'en établit pas. La marge de TUFTÉO sur ces tapis est déjà comprise dans son résultat, donc dans l'actif net transmis et dans le boni. De même, les **ventes de TUFTÉO à VERDALÈNE de janvier à avril 2027** (210 000 €) ne sont pas éliminées : l'opération n'ayant aucun effet antérieur, VERDALÈNE ne reprend ni les produits ni les charges de la période de sa filiale ; seules les **dettes et créances encore ouvertes** au 30 avril s'éteignent (A3 et A4).

**A5 — Frais de l'opération (0,75 pt).** Le PCG permet d'inscrire les frais de fusion à l'actif en frais d'établissement ou de les imputer sur une prime, à défaut de les comptabiliser en charges [V PCG art. 212-9, F01 § 7] ; aucune action n'étant émise, VERDALÈNE les comptabilise en charges, comme l'indique l'annexe 2.6 (déductibles fiscalement).

| Compte | Débit | Crédit |
|---|---:|---:|
| 6226 Honoraires | 26 000 | |
| 6231 Annonces et insertions (publication et formalités) | 1 800 | |
| 401 Fournisseurs | | 27 800 |

---

### 2.8 Note à M. VERDALÈNE, président de la MANUFACTURE VERDALÈNE (2 pts)

*Objet : effets de la dissolution sans liquidation de TUFTÉO sur les comptes de VERDALÈNE (situation au 1er mai 2027, avant impôt et hors autres opérations de 2027).*

- *Bilan, résultat et capitaux propres (1 pt).* Les titres TUFTÉO (1 200 000 €) disparaissent ; VERDALÈNE inscrit à leur place l'immeuble et les machines de Felletin, les stocks, les créances et la trésorerie de sa filiale, et reprend sa provision et ses dettes, dont l'emprunt de 420 000 €. Le total du bilan passe de 8 600 000 € à **9 854 000 €**. Le résultat de 2027, de 180 000 € au 30 avril, est porté à **492 200 €** (+ 340 000 de boni en résultat financier – 27 800 de frais). Les capitaux propres passent de 4 980 000 € à **5 472 200 €** (capital 2 000 000 ; primes de fusion 180 000 ; réserves 2 640 000 ; report à nouveau 160 000 ; résultat 492 200), soit + 492 200 €. Le capital ne change pas : aucune action n'est émise.

| Actif | Avant | Après | Capitaux propres et passif | Avant | Après |
|---|---:|---:|---|---:|---:|
| Immobilisations corporelles nettes | 3 860 000 | 5 100 000 | Capitaux propres | 4 980 000 | 5 472 200 |
| Titres TUFTÉO | 1 200 000 | – | Provisions pour risques | 90 000 | 118 000 |
| Stocks | 1 740 000 | 2 340 000 | Emprunts bancaires | 1 850 000 | 2 270 000 |
| Clients et autres créances | 1 380 000 | 1 780 000 | Fournisseurs | 960 000 | 1 087 800 |
| Disponibilités | 420 000 | 634 000 | Dettes fiscales et sociales | 720 000 | 906 000 |
| **Total** | **8 600 000** | **9 854 000** | **Total** | **8 600 000** | **9 854 000** |

- *Enjeux fiscaux (0,5 pt).* Le boni de 340 000 € accroît le résultat comptable mais **n'est pas imposé** ; les frais sont déductibles. Le déficit de TUFTÉO (370 000 €) ne passera à VERDALÈNE que si la **demande d'agrément est déposée avant le 1er mai 2027** et acceptée : il réduirait alors l'impôt de VERDALÈNE, bénéficiaire, de **92 500 €** au plus sur ses prochains exercices ; sans agrément, il est perdu.
- *Atelier de Felletin (0,5 pt).* L'atelier devient un établissement de VERDALÈNE, qui y poursuit la fabrication avec le même personnel, les mêmes machines et la même clientèle. Ce maintien est aussi la condition de l'agrément pendant trois ans : un transfert des machines à Aubusson et une fermeture de l'atelier en 2029 feraient perdre l'économie d'impôt (92 500 € et l'intérêt de retard) ; si ce projet est envisagé, il faut le reporter après avril 2030 ou y renoncer.

---

### Réponses tolérées
- **2.1** : la date du 30 avril 2027 (dernier jour du délai) est comptée à moitié sur l'item de la date ; une comparaison brève avec une fusion simplifiée (traité, possibilité d'une date d'effet conventionnelle) à la place de la liquidation est acceptée si la transmission sans liquidation est bien établie.
- **2.2** : conditions de l'agrément résumées sans les lettres a) à d), si l'activité poursuivie trois ans et l'absence de changement significatif sont appliquées au cas ; déficit de 390 000 € (sans imputation du bénéfice de la dernière période) : item du calcul compté à moitié.
- **2.3** : toute justification fondée sur la confusion de patrimoine, toujours à la valeur comptable, même sans l'analyse du contrôle.
- **2.5** : un seul des deux calculs des résultats accumulés, s'il est juste et justifié : 1 pt sur 1,5.
- **2.6** : A1 et A2 réunies en une seule écriture, sans compte de liaison (actifs, amortissements, provision et dettes, annulation des titres et boni) ; compte de liaison 458 ou 467 au lieu de 4561 ; dettes fiscales et sociales sur un compte de la classe 4 détaillé autrement ; machines au compte 215 ou 2151.
- **2.7** : A3 et A4 réunies ; frais au compte 6227 ; dettes et créances réciproques soldées dans l'écriture A1 (créance et dette de VERDALÈNE non reprises), si l'actif net transmis reste de 1 720 000 €.
- **2.8** : capitaux propres après l'économie d'impôt sur les frais (5 479 150 €) ou après l'impôt de la période, si l'hypothèse est écrite ; toute présentation chiffrée et cohérente du bilan.

### Erreurs fréquentes (rapports du jury)
- `JUR-R02` Boni mal calculé ou non analysé : frais d'acquisition oubliés (boni de 560 000 €) ; totalité du boni en résultat ou en capitaux propres ; résultats accumulés calculés sans les dividendes (640 000 €) ou sans les pertes (780 000 €).
- `JUR-R05` Difficulté à s'adapter : parité, augmentation de capital ou prime calculées ; valeurs des experts retenues ; provision pour impôts intégrée à l'apport ; écritures datées du 29 ou du 31 mars 2027 ou du 1er janvier 2027.
- `JUR-F07` Annexes mal exploitées : dettes et créances réciproques laissées au bilan, ventes de la période éliminées, marge sur le stock de tapis tuftés éliminée ; amortissements et dépréciations compensés avec les valeurs brutes ; projet de 2029 ignoré.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1 et A2.
- `JUR-F06` Hypothèses non écrites (convention des comptes du boni, frais en charges).
- Erreurs propres à ce cas : déficit présenté comme transféré de plein droit avec le régime de faveur ; dispense d'agrément invoquée ; demande d'agrément jugée possible après la transmission ; perte du déficit présentée comme une perte du régime de faveur.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. civ. art. 1844-5 | Dissolution sans liquidation, associé unique personne morale, transmission universelle à l'issue du délai d'opposition | [V] | F02 § 1 |
| PCG art. 710-1, 710-2 | Champ du titre VII, confusion de patrimoine | [V] p. 81 | F01 § 1 |
| PCG art. 741-1, 741-2, 743-1, 743-3, 744-2, 760-1 à 760-3 | Contrôle commun, valeur comptable, pas de réévaluation, confusion de patrimoine toujours à la valeur comptable, aucun effet antérieur | [V] p. 82-85 et 90-91 | F01 § 2 et § 3.2 |
| BOI-IS-FUS-10-20-40-20 § 170 et 180 | Reprise des valeurs d'origine, amortissements et dépréciations | [V] BOFiP | F01 § 3.2 |
| PCG art. 214-8, 313-1 | Provisions réglementées classées en capitaux propres | [V] p. 24 et 32 | F01 § 8 |
| PCG art. 745-2 | Boni : part en résultat financier (résultats accumulés depuis l'acquisition et non distribués), surplus en capitaux propres | [V] p. 86 | F01 § 5.2 |
| Liste des comptes du PCG 2026 ; 768, 1042 pour le boni | Comptes ; absence de compte de boni | [V] p. 133-148 ; choix des comptes : convention de rédaction | F01 § 5.2 |
| C. civ. art. 1349 | Extinction par confusion des créances réciproques | [V] | F01 § 8 |
| PCG art. 212-9 | Frais de fusion : frais d'établissement, prime ou charges | [V] p. 15-16 | F01 § 7 |
| CGI art. 210-0 A, 210 A-1, 210 A-2, 210 A-3 ; BOI-IS-FUS-10-10-10 § 10 et 20 ; BOI-IS-FUS-10-20-30 § 210 et 330 | Transmission universelle traitée comme une fusion, régime de faveur sauf option, dernier résultat, provisions, engagements | [V] | F02 § 1, § 2 et § 4 |
| CGI art. 210 A-1, al. 2 ; BOI-IS-FUS-10-50-20 § 1 | Boni non imposé sous le régime de faveur, déduction extra-comptable | [V] | F02 § 2 bis |
| CGI art. 209 I et II ; art. 1649 nonies, I ; art. 1649 nonies A ; BOI-SJ-AGR-20-30-10-10 § 1, 10, 60, 120 à 220, 250, 260, 280 | Report en avant, transfert des déficits sur agrément, conditions, dispense sous 200 000 €, demande préalable à la transmission, retrait de l'agrément | [V] lus le 23/11/2026 | F02 § 3 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Désignation du commissaire aux comptes d'une association subventionnée, sort du mandat quand la condition cesse ; commissaire aux comptes, expert-comptable et contrôles des financeurs publics | `3.1.b` Nomination et cessation ; `3.1.a` Cadres d'exercice professionnel | 3,5 |
| 3.2 Associé du cabinet élu administrateur bénévole de l'association | `3.1.c` Principes déontologiques | 1,5 |
| 3.3 Responsabilité civile du commissaire aux comptes et infractions des dirigeants | `3.1.e` Mise en cause de la responsabilité | 2 |
| 3.4 Certification des comptes et contrôle de l'emploi des ressources collectées auprès du public | `3.2.a` Notion d'audit | 1,5 |
| 3.5 Convocation aux réunions du conseil d'administration et à l'assemblée générale | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.6 Risques et assertions du cycle trésorerie et dons ; procédures ; déclarations écrites de la direction | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit ; `3.1.d` Référentiel normatif (NEP) | 6 |
| 3.7 Anomalies, écritures, caractère significatif, opinion selon la correction et la déclaration écrite, parties du rapport | `3.2.e` Portée des opinions | 2 |
| 3.8 Champ de la publication obligatoire ; norme volontaire et ESRS ; choix du référentiel | `3.3.a` Contexte et normes de durabilité | 3 |
| 3.9 Vigilance raisonnable ; impacts, risques et opportunités ; matérialité d'impact et matérialité financière | `3.3.b` Principes de construction du reporting | 3 |
| 3.10 Objectifs, axes et assurance limitée ; étapes ; procédures sur deux données | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4 |
| 3.11 Avis sur une erreur non corrigée ; différences avec l'opinion sur les comptes | `3.4.c` Portée des avis | 2 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Le commissaire aux comptes de l'association (3,5 pts)

**a. Désignation et sort du mandat (2 pts)**

*Raison de la désignation (0,5 pt)*
- Toute association qui a reçu **annuellement** des autorités administratives ou des établissements publics à caractère industriel et commercial des **subventions en numéraire** dont le montant global dépasse **153 000 €** établit des comptes annuels, en assure la publicité avec le rapport du commissaire aux comptes et **nomme au moins un commissaire aux comptes** [V C. com. L. 612-4 al. 1-2 ; D. 612-5].
- En 2025, la Région, les deux départements et les communes ont versé **184 500 €** (annexe 3.2) : la condition était remplie ; d'où la désignation du 14/06/2025.
- L'association n'était pas tenue à un autre titre : une personne morale de droit privé non commerçante ayant une activité économique doit nommer un commissaire aux comptes si elle dépasse **deux des trois** critères (50 salariés en contrat à durée indéterminée ; 3 100 000 € de chiffre d'affaires ou de ressources ; 1 550 000 € de total du bilan) [V L. 612-1 ; R. 612-1 al. 1]. Avec 11 salariés en contrat à durée indéterminée, 792 000 € puis 837 900 € de produits et un bilan de 2 290 000 € puis 2 380 000 €, elle ne dépasse que le critère du bilan [S, application].

*Conditions de la désignation (0,75 pt)*
- **Organe** : en dehors d'une nomination statutaire, l'assemblée générale ordinaire ou « l'organe exerçant une fonction analogue » selon les règles propres à l'entité [V L. 821-40 I al. 2] : ici l'**assemblée générale** des membres, compétente selon les statuts (annexe 3.1).
- **Durée** : **six exercices** (2025 à 2030) ; les fonctions expirent après l'assemblée qui statue sur les comptes du sixième exercice, en 2031 [V L. 821-44 al. 1]. La limitation à trois exercices n'est ouverte qu'à une désignation faite « par une société », volontaire ou fondée sur les règles des petits groupes [V L. 821-46] : elle ne concernait pas l'association.
- **Suppléant** : exigé seulement si le titulaire est une personne physique ou une société unipersonnelle [V L. 612-4 al. 2 ; L. 821-40 I al. 3] ; SAULNERON est une société de quatre associés : aucun suppléant n'était requis.

*Fin de la condition et sort du mandat (0,75 pt)*
- En 2026, les subventions publiques en numéraire ne sont plus que de **127 500 €**, inférieures à 153 000 € : la condition n'est plus remplie pour 2026. Le mécénat de la Fondation VALCHAUME (fondation privée, non autorité administrative) et la mise à disposition gratuite de locaux (subvention en nature) n'entrent pas dans ce montant [V L. 612-4 al. 1, lecture ; S, application] ; les ajouter (177 100 €) serait une erreur.
- Mais le mandat **en cours ne prend pas fin** : il est donné pour six exercices [V L. 821-44 al. 1] ; un commissaire aux comptes ne peut être écarté avant l'expiration normale de ses fonctions qu'en cas de **faute ou d'empêchement**, par décision de justice (pour une association, notamment à la demande du cinquième des membres de l'assemblée) [V L. 821-50 al. 1-2] ; la baisse d'une subvention n'est ni l'un ni l'autre. L. 612-4 ne prévoit aucune règle de sortie : la règle qui permet à l'organe délibérant de mettre fin au mandat après deux exercices sous les seuils ne vise que les personnes morales de L. 612-1 [V R. 612-1 al. 2 ; S, déduction des textes].
- **Réponse à la trésorière** : l'association ne peut pas « se passer » du cabinet dès 2026 ; les comptes de 2026 seront certifiés, et le mandat court jusqu'à l'assemblée qui statuera sur les comptes de 2030. À cette date, elle appréciera si une obligation subsiste. En tout état de cause, la convention de la Région exige jusqu'en 2027 la transmission du rapport du commissaire aux comptes (annexe 3.2) [S].

**b. Le commissaire aux comptes parmi les autres intervenants (1,5 pt)**

| | ARDILLAT Expertise (expert-comptable) | SAULNERON (commissaire aux comptes) | Financeurs publics |
|---|---|---|---|
| Fondement | Mission **contractuelle** définie par une lettre de mission [V décret 2012-432 art. 151] | Mission **légale**, d'intérêt général, confiée par l'assemblée [V L. 612-4 ; code de déontologie art. 1er] | Contrôle de l'emploi de leurs subventions [V CGCT L. 1611-4] |
| Objet | Tenir, centraliser, arrêter les comptabilités, établir le projet de comptes et la paie [V ord. 45-2138 art. 2] | **Certifier** que les comptes sont réguliers, sincères et donnent une image fidèle [V L. 821-53 al. 1] | Contrôle par les délégués de la collectivité ; copie certifiée des budgets et des comptes [V CGCT L. 1611-4] ; contrôle possible par les juridictions financières au-delà de 1 500 € de concours : chambre régionale des comptes, ou Cour des comptes lorsque l'organisme relève de plusieurs chambres, comme ici (Allier et Creuse) [V CJF L. 211-8, L. 111-8] |
| Cadre | Inscription au tableau de l'ordre ; conseils régionaux et conseil national [V ord. art. 3, 28, 33] ; indépendance d'esprit, compatible avec la tenue des comptes [V décret art. 145] | Inscription sur la liste de la H2A ; CNCC et compagnies régionales ; indépendance en réalité et en apparence ; NEP [V L. 821-13, L. 821-12 ; code de déontologie art. 5] | Pouvoirs administratifs, sans opinion sur les comptes [S] |

- **Expert-comptable (0,5 pt)** : ARDILLAT produit les comptes ; il ne peut pas les « certifier ». Une vérification par celui qui les a établis n'apporterait aucune assurance indépendante [V ord. art. 2 ; S, application].
- **Commissaire aux comptes (0,5 pt)** : SAULNERON exprime, pour l'assemblée et les tiers (Région, Fondation, donateurs), une opinion sur les comptes pris dans leur ensemble ; il ne participe pas à leur établissement et ne s'immisce pas dans la gestion [V L. 821-54 I].
- **Financeurs (0,5 pt)** : la demande de la Région de consulter les factures de son chantier relève du contrôle de l'emploi de **sa** subvention [V CGCT L. 1611-4] ; il ne remplace pas la certification, que la convention exige d'ailleurs (annexe 3.2) [S].

**Réponses tolérées**
- Un raisonnement qui retient que le mandat se poursuit jusqu'à son terme sans citer les cas de relèvement, s'il écarte toute « résiliation » par l'association : 0,5 pt sur 0,75.
- L'omission de L. 612-1, si la désignation est correctement fondée sur les subventions : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Compter le mécénat privé ou les locaux mis à disposition dans le seuil, ou appliquer à l'association les seuils de 5 000 000 € et 10 000 000 € des sociétés (`JUR-F07`).
- Conclure que le mandat cesse dès que la condition n'est plus remplie, ou appliquer la règle de sortie des personnes morales ayant une activité économique (`JUR-A05`).
- Confondre la mission de l'expert-comptable et celle du commissaire aux comptes, ou présenter le contrôle de la Région comme une certification (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 612-1, L. 612-4, R. 612-1, D. 612-5, L. 821-40 I, L. 821-44, L. 821-46, L. 821-50 | Obligation, seuil, organe, durée, suppléant ; relèvement | [V] ; poursuite du mandat : [S] | F09 § 3.4-3.5, § 14, § 22 |
| Ord. 45-2138 art. 2, 3 ; décret 2012-432 art. 145, 151 ; L. 821-53, L. 821-54 I ; CGCT L. 1611-4 ; CJF L. 111-8, L. 211-8 | Expert-comptable, commissaire aux comptes, contrôles des financeurs | [V] | F09 § 1, § 2, § 22 ; F10 § 3 |

### 3.2 M. FOURNOUX, associé et administrateur (1,5 pt)

**Cadre (0,5 pt)**
- Le commissaire aux comptes est la **société** SAULNERON. Son indépendance s'apprécie **en réalité et en apparence** ; elle exclut toute influence liée à des liens personnels, financiers ou professionnels, directs ou indirects, **y compris entre ses associés** et l'entité ; toute personne en mesure d'influer, même indirectement, sur le résultat de la mission y est soumise [V code de déontologie art. 5 I-II]. La profession est incompatible avec tout acte de nature à porter atteinte à l'indépendance [V L. 821-27 1°].

**Analyse (0,5 pt)**
- Administrateur, M. FOURNOUX est **mandataire social** de l'association : il occupe une **fonction sensible** [V code de déontologie art. 31 al. 2 a)]. Il siège dans le **conseil qui arrête les comptes** que son cabinet certifie, et il prépare le budget des chantiers, dont les dépenses entrent dans ces comptes.
- Le code juge incompatible le seul **lien familial** entre une personne en fonction sensible et le commissaire aux comptes ou un membre de la direction de son cabinet [V art. 32 II] ; ici, c'est un associé du cabinet qui occupe lui-même la fonction. Un tiers objectif, raisonnable et informé douterait de l'indépendance du cabinet [S, application].
- Ses arguments ne changent rien : l'indépendance ne dépend ni de la rémunération (bénévolat) ni de la participation à la mission ; l'abstention lors du vote des comptes ne supprime ni sa place dans l'organe collégial ni l'apparence de parti pris [S]. La loi interdit d'ailleurs aux personnes qui exercent les fonctions de commissaire aux comptes de devenir administrateurs de l'entité moins de trois ans après la fin de leur mission [V L. 821-32] : *a fortiori* pendant la mission.

**Mesure à prendre (0,5 pt)**
- Le cabinet doit prendre **immédiatement** les mesures de sauvegarde appropriées ; si elles sont insuffisantes, il met fin à la mission [V code de déontologie art. 5 III] (par analogie avec l'art. 35, qui impose de tirer sans délai les conséquences des liens personnels, financiers ou professionnels survenus en cours de mission [S]). Aucune sauvegarde ne suffit tant que M. FOURNOUX reste administrateur : il doit **quitter le conseil** et la commission des chantiers ; à défaut, le cabinet met fin à ses missions [V art. 5 III ; S, application]. Le cabinet documente la situation et sa résolution [V A. 821-55 § 41-43].
- Son bénévolat sur les chantiers, sans fonction de gouvernance, reste une situation à apprécier, avec des sauvegardes (aucun rôle dans l'établissement des comptes ni dans les données de durabilité vérifiées par le cabinet, ses propres heures de bénévolat étant comptées dans l'annexe 3.11) [S].

**Réponses tolérées**
- La démission du cabinet présentée comme l'issue, si le candidat indique d'abord la démission de M. FOURNOUX du conseil comme mesure préférable : points complets.

**Erreurs fréquentes**
- Réciter les principes du code sans les appliquer à la fonction d'administrateur, ou retenir que l'abstention suffit (`JUR-A05`).
- Raisonner sur l'indépendance d'esprit de l'expert-comptable, parce que M. FOURNOUX n'est pas commissaire aux comptes (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 5, 31, 32 (art. 35 par analogie) ; L. 821-27 1°, L. 821-32 ; A. 821-55 § 41-43 | Indépendance, fonction sensible, survenance en cours de mission, viduité, documentation | [V] ; application : [S] | F10 § 4.1, § 12, § 14, § 18 |

### 3.3 Le cabinet « répond-il » des dépenses de l'ancien trésorier ? (2 pts)

**Responsabilité civile du commissaire aux comptes (0,75 pt)**
- Le commissaire aux comptes est responsable, envers l'entité et les tiers, des conséquences dommageables des **fautes et négligences** qu'il commet dans l'exercice de sa profession [V L. 821-37 al. 1]. L'association doit établir une **faute** du cabinet, un **préjudice** et un **lien de causalité** entre les deux [S, droit commun].
- Le commissaire aux comptes est tenu d'une **obligation de moyens** [S, qualification doctrinale] : l'audit donne une assurance **raisonnable**, et non absolue, que les comptes ne comportent pas d'anomalies **significatives** ; il repose sur des sondages [V NEP principes § 08-09]. La certification ne garantit pas la qualité de la gestion [V L. 821-55].

**Infractions des dirigeants (0,5 pt)**
- Le commissaire aux comptes n'est **pas civilement responsable des infractions commises par les dirigeants**, sauf si, en ayant eu connaissance, il ne les a pas signalées dans son rapport à l'assemblée générale [V L. 821-37 al. 3].
- M. LAMOTHIER, membre du bureau et trésorier, était un dirigeant de l'association [S, qualification]. Le cabinet n'a eu connaissance des faits que le 16/07/2026, après son rapport du 22/04/2026 et l'assemblée du 13/06/2026 (annexe 3.4) : l'exception ne joue pas.

**Une faute propre du cabinet ? (0,75 pt)**
- Les 6 840 € représentent **0,46 fois** le seuil de signification de 2025 (15 000 €). Par leur nature (dépenses personnelles réglées par un dirigeant avec les fonds de l'association), ils auraient pu être jugés significatifs s'ils avaient été détectés [V NEP anomalies § 14]. Mais l'audit, fondé sur des sondages et sur une assurance raisonnable, n'a pas pour objet de déceler toute fraude : l'absence de ces dépenses dans un échantillon de 35 pièces ne révèle pas, à elle seule, un manquement, si le cabinet a évalué le risque de fraude et mis en œuvre les procédures que les normes requièrent [S, application ; NEP fraudes § 16-19].
- Les dépenses ont été faites de février à novembre 2025 et la carte a été supprimée le 15/01/2026, **avant** les travaux d'audit (février à avril 2026) : l'audit ne pouvait pas les empêcher. Le préjudice résulte des actes de l'ancien trésorier ; le lien de causalité avec l'audit fait défaut [S].
- **Réponse au conseil** : le cabinet n'a pas à rembourser les 6 840 € ; l'association peut agir contre l'ancien trésorier (non traité).

*Remarque, sans points* : le cabinet tient compte de ces faits dans son évaluation du risque de fraude sur les encaissements et les paiements de 2026 [V NEP fraudes § 16-19].

**Réponses tolérées**
- Une réponse qui retient une faute possible du cabinet mais nie le lien de causalité : points complets si la règle sur les infractions des dirigeants est présentée.

**Erreurs fréquentes**
- Considérer que la certification « garantit » l'absence de fraude (`JUR-A01`).
- Décrire la procédure de mise en cause ou qualifier pénalement les faits, ce qui n'est pas demandé (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-37 al. 1-3, L. 821-55 ; NEP principes § 08-09 ; NEP anomalies § 14 ; NEP fraudes § 16-19 | Responsabilité civile ; infractions des dirigeants ; assurance raisonnable ; fraude | [V] ; faute, lien de causalité : [S] | F09 § 7.1 ; F10 § 18 ; F11 § 1.1, § 20.1 |

### 3.4 Certification et contrôle de l'emploi des dons (1,5 pt)

**Objectif de la certification (0,5 pt)** : le cabinet certifie, en justifiant de ses appréciations, que les comptes annuels sont **réguliers et sincères** et donnent une **image fidèle** du résultat, de la situation financière et du patrimoine [V L. 821-53 al. 1]. Il exprime une **opinion** après un audit qui lui donne une **assurance raisonnable**, élevée mais non absolue, que les comptes pris dans leur ensemble ne comportent pas d'**anomalies significatives**, appréciées au regard d'un seuil de signification (16 000 € en 2026) [V NEP principes § 01, 08 ; F11 § 1.1].

**Limites (0,5 pt)** : la certification couvre l'annexe, donc l'information sur l'emploi des ressources collectées auprès du public (hypothèse de l'énoncé), mais à ce même niveau d'assurance et de signification : elle ne vérifie pas que chaque don a financé le projet annoncé et ne juge ni l'opportunité des dépenses ni la qualité de la gestion [V L. 821-54 I, L. 821-55 ; S, application]. Pour les souscripteurs, elle donne l'assurance que les 86 500 € de la souscription figurent dans les comptes et que l'information sur leur emploi est sincère, non que les travaux du moulin seront conformes à l'appel [S].

**Contrôle de l'emploi des ressources (0,5 pt)** : la **Cour des comptes** peut contrôler le **compte d'emploi des ressources collectées auprès du public** par les organismes qui font appel à la générosité du public, afin de vérifier la **conformité des dépenses aux objectifs** de l'appel ; ses observations sont adressées à la présidente, qui les communique au conseil d'administration et à l'assemblée ; une non-conformité donne lieu à une déclaration rendue publique [V CJF L. 111-9, L. 143-2] (hypothèse de l'énoncé : l'association relève des organismes soumis à la déclaration préalable). **Réponse à la présidente** : la garantie de l'emploi des dons relève d'abord de l'association elle-même ; leur conformité à l'appel peut être contrôlée par la Cour des comptes ; le cabinet, lui, certifie les comptes.

**Réponses tolérées**
- La mention du contrôle des collectivités sur leurs subventions, à titre de comparaison : sans points supplémentaires.

**Erreurs fréquentes**
- Présenter la certification comme une garantie de l'emploi des dons, ou confondre assurance raisonnable et assurance absolue (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-54 I, L. 821-55 ; NEP principes § 01, 08 | Objectif ; assurance raisonnable ; limites | [V] ; application à l'information sur l'emploi des ressources : [S] | F11 § 1.1 |
| CJF L. 111-9, L. 143-2 | Contrôle du compte d'emploi des ressources collectées auprès du public | [V] | F09 § 22 |

### 3.5 Convocation aux réunions (1,5 pt)

**Le droit d'être convoqué (0,75 pt)**
- Les commissaires aux comptes sont convoqués à toutes les réunions du conseil d'administration ou de l'**organe collégial d'administration** qui examinent ou arrêtent des comptes annuels ou intermédiaires, et à toutes les assemblées ou réunions de l'organe compétent [V L. 821-65]. Le texte vise toute personne ou entité qui a un commissaire aux comptes, quelle que soit sa forme : le conseil d'administration de l'association, qui arrête les comptes, est un tel organe. La présidente se trompe : la règle ne vaut pas « que dans les sociétés » [S, application].
- La convocation est faite par **lettre recommandée avec demande d'avis de réception**, en même temps que les administrateurs pour le conseil, au plus tard lors de la convocation des membres pour l'assemblée [V D. 821-185]. L'invitation par simple courriel, trois jours avant l'assemblée du 13/06/2026, n'est pas régulière.
- La convocation permet au cabinet de porter à la connaissance du conseil, **avant l'arrêté**, son programme de travail, les **modifications à apporter aux comptes** et les irrégularités relevées [V L. 821-63 I].

**Ce que fait le cabinet (0,75 pt)**
- Il écrit à la présidente pour lui rappeler la règle et demander à être convoqué, dans les formes, au conseil du **30/03/2027** qui arrêtera les comptes de 2026 et à l'assemblée du 12/06/2027 [S].
- Avant ce conseil, il lui communique par écrit ses observations, notamment les corrections demandées (question 3.7), pour qu'elles soient examinées avant l'arrêté des comptes [V L. 821-63 I 2° ; NEP anomalies § 11, 15].
- Il documente le manquement dans son dossier ; le défaut de convocation de 2026 n'empêche pas, à lui seul, la certification des comptes de 2026 [S].

**Erreurs fréquentes**
- Limiter le droit de convocation à l'assemblée, ou le réserver aux sociétés commerciales (`JUR-A05`).
- Décrire en détail la procédure de convocation des membres, qui n'est pas demandée (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-65, D. 821-185, L. 821-63 I | Convocation ; forme ; communications | [V] ; application à l'association : [S] | F09 § 5, § 22 ; F11 § 2 |

### 3.6 Trésorerie et dons ; déclarations écrites (6 pts)

**a. Risques d'anomalies significatives et assertions (2 pts ; 0,25 pt par risque correctement relié à ses assertions, dans la limite de 2 pts)**

Les faits de 2025, les encaissements en espèces recueillis par des bénévoles seuls et l'absence de séparation des tâches sur la boutique sont des **facteurs de risque de fraude** (opportunités) [V NEP fraudes § 16-18]. Faute de tests de l'efficacité des procédures de l'entité, l'évaluation du risque au niveau des assertions correspond au risque inhérent [V NEP risques § 41].

| Risque | Origine dans l'annexe 3.7 | Assertions |
|---|---|---|
| Dons en ligne de fin décembre non rattachés à 2026 | Reversement à J + 5 ; enregistrement à la date du reversement | Séparation des exercices et exhaustivité des dons ; existence et exhaustivité de la créance sur la plateforme |
| Dons en espèces non enregistrés | Troncs relevés par un bénévole seul ; urnes des journées du patrimoine comptées par une seule personne | Exhaustivité des dons (et réalité des encaissements enregistrés) |
| Ventes de la boutique non enregistrées, espèces manquantes | Cahier sans ticket, bénévoles en roulement, versements mensuels | Exhaustivité des ventes ; existence de la caisse |
| Chèques de dons égarés ou rattachés au mauvais exercice | Cahier tenu par une bénévole, remise hebdomadaire, 4 260 € remis le 31/12 | Exhaustivité ; séparation des exercices ; existence des chèques à l'encaissement |
| Comptes à terme : titulaire et pouvoirs | Compte n° 2 ouvert par l'ancien trésorier, banque non informée du changement | Existence ; droits et obligations ; exhaustivité des comptes ouverts |
| Fonds de la souscription | Compte dédié de 86 500 €, affecté au moulin, travaux en 2027 | Présentation et intelligibilité (fonds affectés) ; réalité et exhaustivité des dons de la souscription |
| Rapprochement bancaire | Chèques émis non débités (7 220 €), remises non créditées | Existence et exhaustivité des disponibilités ; séparation des exercices |
| Paiements | Carte supprimée ; virements signés par deux membres du bureau | Réalité des décaissements (risque réduit depuis le 15/01/2026) |

**b. Procédures en réponse (2,5 pts ; 0,25 pt par procédure reliée à son objectif, dans la limite de 2,5 pts)**
- **Demande de confirmation** aux deux banques : soldes des quatre comptes, titulaire, **personnes habilitées et procurations** (l'ancien trésorier en a-t-il encore ?), moyens de paiement en vigueur, autres comptes, nantissements — *existence, droits et obligations, exhaustivité* [V NEP éléments probants § 10].
- **Contrôle du rapprochement bancaire** : solde du relevé (41 380 €), débit en janvier 2027 des chèques émis, crédit le 04/01/2027 de la remise du 31/12 (41 380 − 7 220 + 4 260 = 38 420 €) — *existence, séparation*.
- **Rapprochement du relevé de la plateforme** (41 840 € de dons) avec les **reçus fiscaux** émis et avec les reversements du relevé bancaire — *exhaustivité et réalité des dons en ligne*.
- **Test de séparation des exercices** sur les dons des derniers jours de décembre et les reversements de janvier — *séparation* (il révèle l'anomalie 1).
- **Chèques** : rapprochement du cahier, des reçus fiscaux (suite numérique) et des remises en banque — *exhaustivité*.
- **Comptage de la caisse** de la boutique et de la billetterie à la clôture (observation physique) et rapprochement avec le solde comptable — *existence de la caisse* (il révèle l'anomalie 2) ; observation inopinée d'un relevé de tronc — *exhaustivité*.
- **Billetterie** : contrôle de la suite des billets numérotés et rapprochement avec les recettes et la fréquentation — *exhaustivité*.
- **Boutique** : rapprochement des ventes avec les achats et la variation du stock (procédure analytique) — *exhaustivité*.
- **Comptes à terme** : inspection des contrats (titulaire, échéance), recalcul des intérêts courus — *droits, évaluation, classement*.
- **Souscription** : relevés du compte dédié, conditions de l'appel publié, information donnée dans l'annexe — *présentation*.
- **Paiements** : vérification de la suppression de la carte et de la double signature sur un échantillon de virements de 2026 — *réalité des décaissements*.

**c. Déclarations écrites de la direction (1,5 pt)**
- **Objet (0,5 pt)** : les déclarations de la direction sont des **éléments collectés** qui fondent l'opinion [V NEP déclarations § 1, annexe 3.8]. Le cabinet demande à la présidente, **représentante légale**, une formulation écrite de celles qu'il estime nécessaires pour conclure sur une assertion [§ 6] : ici l'**exhaustivité des encaissements en espèces**, pour lesquels il n'existe pas d'élément externe. Une déclaration ne remplace pas les autres éléments : le cabinet cherche à la **corroborer** et vérifie la compétence de son auteur [§ 4].
- **Refus (0,5 pt)** : le cabinet s'enquiert des **raisons** du refus [§ 13]. La présidente les donne : les espèces sont recueillies par des bénévoles, sans procédure qui lui permette d'attester qu'elles ont toutes été enregistrées. Son refus est **cohérent** avec les faiblesses relevées et avec l'écart de caisse ; il ne fait pas douter de ses autres déclarations, qu'elle signe [§ 5 ; S, application].
- **Conséquences (0,5 pt)** : selon l'annexe 3.8, les autres procédures ne suffisent pas sans cette déclaration : le cabinet ne peut pas conclure sur l'exhaustivité de ces encaissements. C'est une **limitation** de ses travaux, qu'il traduit dans son opinion [§ 13 ; NEP rapport § 11] (question 3.7). Il en informe le conseil d'administration et recommande des procédures de comptage à deux et l'émission de tickets [S] ; il conserve la réponse dans son dossier [§ 14].

**Réponses tolérées**
- En a. et b., d'autres risques ou procédures tirés de l'annexe, correctement reliés à des assertions ou à des objectifs.
- En c., la qualification du refus comme une incertitude sur l'exhaustivité, si la conséquence (réserve pour limitation) est tirée : points complets.

**Erreurs fréquentes**
- Confondre réalité (flux) et existence (soldes), ou citer des assertions sans les relier à un risque (`JUR-A01`).
- Traiter la lettre d'affirmation comme une formalité, ou comme un élément suffisant à lui seul (`JUR-A06`).
- Appliquer les règles comptables des associations (fonds dédiés) au lieu de traiter la présentation des fonds de la souscription comme une assertion à vérifier (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP risques § 41 ; NEP fraudes § 16-18 ; NEP éléments probants § 9-10 | Risque inhérent ; facteurs de risque de fraude ; assertions ; techniques | [V] | F11 § 4.1, § 4.3, § 6, § 20.1 |
| NEP déclarations § 1, 4-6, 13-14 ; NEP rapport § 11 | Déclarations écrites ; refus ; limitation | [V] ; application : [S] | F11 § 8.1, § 12.3, § 27 |

### 3.7 Anomalies, écritures et opinion (2 pts)

**Anomalies et caractère significatif (0,5 pt)**
- **Anomalie 1 — dons en ligne** : dons faits du 27 au 31/12/2026 et reversés du 01 au 05/01/2027 : 2 960 + 3 480 + 4 120 + 4 870 + 4 410 = **19 840 €**. Le don est acquis à l'association à la date où le donateur paie sur la plateforme, qui émet le reçu à cette date : il relève de 2026 [S, application]. Contrôle : 22 000 + 19 840 = 41 840 €, total du relevé de la plateforme. Produits, créances et résultat sont **sous-évalués** de 19 840 € : **1,24 fois** le seuil de signification (16 000 €), anomalie significative à elle seule.
- **Anomalie 2 — caisse de la boutique** : 4 445 − 1 405 = **3 040 €** de caisse inexistante ; actif et résultat **surévalués** : **0,19 fois** le seuil, non significative par son montant, mais à apprécier par sa **nature** (espèces manquantes après les faits de 2025, possible indice de fraude) [V NEP anomalies § 14 ; NEP fraudes § 23-26].
- Les deux anomalies jouent en sens contraire ; elles s'apprécient individuellement et en cumul, sans que l'une efface l'autre (effet net de 16 800 €) [V NEP anomalies § 14 ; S, application].

**Écritures de correction au 31/12/2026 (0,5 pt)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 467 | Divers comptes débiteurs et produits à recevoir | 19 840 | |
| | 7582 | Libéralités reçues | | 19 840 |

Libellé : dons en ligne des 27 au 31/12/2026, reversés par la plateforme en janvier 2027 (écriture X1, équilibrée à 19 840 €).

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 658 | Pénalités et autres charges | 3 040 | |
| | 53 | Caisse | | 3 040 |

Libellé : écart de caisse non expliqué de la boutique, 4 445 − 1 405 (écriture X2, équilibrée à 3 040 €). Charge de gestion courante, selon la convention de l'annexe 3.9, et non exceptionnelle : l'écart n'est pas lié à un événement majeur et inhabituel [V PCG art. 513-5]. Après corrections, le résultat de 2026 est de 42 600 + 19 840 − 3 040 = **59 400 €**.

**Opinion selon la décision de l'association (0,75 pt)**
- **Les deux anomalies sont corrigées et la présidente signe toutes les déclarations** : aucune anomalie non corrigée, aucune limitation : **certification sans réserve** [V NEP rapport § 08].
- **La directrice laisse les dons en ligne en 2027 (seul l'écart de caisse est corrigé), la présidente signe** : anomalie non corrigée de 19 840 € (1,24 fois le seuil), significative, circonscrite à une rubrique et chiffrée : **certification avec réserve pour désaccord** ; un refus de certifier ne se justifie pas [V NEP rapport § 09-10, § 12]. Si, à l'inverse, seul l'écart de caisse restait non corrigé (0,19 fois le seuil), la certification serait **sans réserve**, l'écart figurant à l'état des anomalies non corrigées joint à la déclaration écrite [V NEP anomalies § 17].
- **Les deux anomalies sont corrigées, mais la présidente maintient son refus** : limitation portant sur l'exhaustivité des dons en espèces (troncs et journées du patrimoine, 6 400 € enregistrés) et des ventes de la boutique (74 200 €, dont la moitié environ en espèces), soit 80 600 € de flux concernés (5,04 fois le seuil, 9,6 % des produits) ; ses incidences sont **circonscrites** à ces flux identifiés : **certification avec réserve pour limitation** [V NEP rapport § 11 ; NEP déclarations § 13].
- **Les dons ne sont pas corrigés et la présidente refuse** : **certification avec deux réserves** (désaccord et limitation), chacune circonscrite [V NEP rapport § 09-11 ; S, qualification].

**Parties du rapport, cas d'une réserve (0,25 pt)** : la partie « **Opinion avec réserve** » indique que, sous cette réserve, les comptes sont réguliers et sincères et donnent une image fidèle ; la partie « **Fondement de l'opinion avec réserve** » expose le motif et son incidence (produits et résultat sous-évalués de 19 840 € ; impossibilité d'obtenir des éléments suffisants sur l'exhaustivité des encaissements en espèces). Les motifs sont communiqués au préalable au conseil d'administration ; le rapport est destiné à l'assemblée générale [V NEP rapport § 06, § 18 ; L. 821-63 I ; R. 821-180].

**Réponses tolérées**
- En cas de refus de la présidente, une impossibilité de certifier, si le candidat soutient que le refus prive de valeur l'ensemble des déclarations : 0,25 pt sur 0,75 pour l'opinion.
- Le compte 511 « Valeurs à l'encaissement » à la place du compte 467 pour les fonds détenus par la plateforme : points complets si le libellé est juste.

**Erreurs fréquentes**
- Laisser les dons en 2027 au motif que les fonds sont arrivés en janvier (`JUR-F07`).
- Compenser les deux anomalies, ou ignorer la nature de l'écart de caisse (`JUR-A06`).
- Écriture sans libellé ou sans numéro de compte (`JUR-F03`).
- Conclure à une certification sans réserve lorsque la déclaration nécessaire est refusée (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 513-5 ; liste des comptes | Comptes 467, 7582, 658, 53 ; résultat exceptionnel | [V] | F11 § 20.2 |
| NEP anomalies § 14, § 17 ; NEP fraudes § 23-26 ; NEP déclarations § 13 ; NEP rapport § 06, § 08-12, § 18 ; R. 821-180 ; L. 821-63 I | Anomalies ; limitation ; opinions ; parties du rapport | [V] ; qualification : [S] | F11 § 8, § 14.1, § 27 |

---

### Partie B – Durabilité (12 points)

### 3.8 Pourquoi publier, et selon quel référentiel ? (3 pts)

**L'association n'est pas tenue de publier (0,75 pt)** : la publication obligatoire vise, en principe, des **sociétés de grande taille** et des groupes, au-delà de seuils élevés de bilan, de chiffre d'affaires et d'effectifs ; le droit français la fait figurer dans le rapport de gestion des sociétés qui sont des « grandes entreprises », et le droit européen la réserve désormais aux entreprises de plus de 1 000 salariés et de plus de 450 M€ de chiffre d'affaires [V L. 232-6-3 ; F12 § 10]. L'association, qui n'est pas une société, emploie 14 salariés et dispose de 837 900 € de produits : elle en est très loin [S, application].

**La norme volontaire (0,75 pt)** : le règlement délégué (UE) 2026/1560 permet aux entreprises **non soumises** à l'obligation de publier selon une **norme volontaire** (VSME), issue des travaux de l'EFRAG et proportionnée aux petites et moyennes entreprises, organisée en un **module de base** et un **module complet** [V règl. 2026/1560 art. 2, annexe I]. L'association aurait pu s'en tenir au module de base et ajouter des informations du module complet selon les attentes de ses financeurs [S].

**Les ESRS (0,75 pt)** : normes **transversales** (ESRS 1, exigences générales ; ESRS 2, informations générales, toujours publiées) appliquées avec les normes **thématiques** pour les sujets matériels, et **informations spécifiques à l'entité** quand un sujet matériel n'est pas couvert ; détermination des informations par une **analyse de double matérialité** ; un état de durabilité qui donne une image fidèle des impacts, risques et opportunités matériels [V ESRS 1 (2026) § 3, § 8-11, § 29 ; F12 § 3, § 5, § 6].

**Appréciation du choix (0,75 pt)** : les ESRS sont plus exigeantes pour une association de quatorze salariés ; le choix est néanmoins justifié par la convention de la Fondation VALCHAUME, qui les exige et dont dépendent 40 000 € par an et un éventuel complément de 15 000 € (annexe 3.10). L'association doit le **dire explicitement** et appliquer **toutes** leurs exigences, sans choisir celles qui l'arrangent [V F12 § 11 (b) ; S]. Le choix a une conséquence pour la mission du cabinet : il vérifiera le processus d'analyse de double matérialité (question 3.10). La norme volontaire aurait suffi pour la Région.

**Réponses tolérées**
- La mention des informations spécifiques à l'association (heures de bénévolat, part du réemploi) comme application des ESRS : sans points supplémentaires.

**Erreurs fréquentes**
- Détailler les seuils et le calendrier de la publication obligatoire, qui ne sont pas demandés (`JUR-A06`).
- Présenter la norme volontaire comme une version des ESRS, ou réciter l'architecture des ESRS sans apprécier le choix (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 232-6-3 ; règl. 2026/1560 art. 2, annexe I ; ESRS 1 (2026) § 3, § 8-11, § 29 | Champ ; norme volontaire ; architecture et double matérialité | [V] ; application : [S] | F12 § 3-6, § 10, § 11 |

### 3.9 Vigilance raisonnable, impacts, risques et opportunités (3 pts)

**La vigilance raisonnable (1 pt)**
- C'est le processus par lequel l'entreprise **identifie, prévient, atténue, fait cesser, réduit à un minimum et remédie** à ses impacts **négatifs**, réels ou potentiels, sur les personnes et l'environnement, en lien avec ses activités ; c'est une **pratique constante**, qui peut conduire à modifier la stratégie, les activités, les relations d'affaires et les achats [V ESRS 1 (2026) § 56]. Les ESRS n'imposent aucune conduite en la matière : elles demandent d'en rendre compte [V § 57].
- **Lien avec la matérialité d'impact** : les **résultats** de la vigilance sont pris en compte pour évaluer les impacts négatifs matériels ; son étape d'identification et d'évaluation des impacts, y compris dans la chaîne de valeur, sert à l'évaluation de la matérialité ; elle aide à identifier les risques et opportunités, qui en découlent souvent, et à **prioriser** les actions selon la **gravité** et la **probabilité** des impacts [V § 58-59]. Le dialogue avec les parties prenantes affectées en est une contribution essentielle [V § 42].
- **Application** : le calendrier des chantiers établi avec des naturalistes depuis 2026, après la disparition d'une colonie en 2025, est une mesure de prévention ; l'association doit en suivre l'efficacité et en rendre compte [S].

**Impacts, risques et opportunités (1,5 pt : deux impacts à 0,5 pt ; un risque ou une opportunité à 0,5 pt)**

| Élément du contexte | Matérialité d'impact | Matérialité financière |
|---|---|---|
| Chauves-souris et hirondelles | Impact négatif réel (2025) et potentiel sur la biodiversité, lié aux activités propres : destruction de gîtes pendant les travaux | Risque de retard et de surcoût des chantiers si le calendrier est contraint |
| Sécurité des chantiers | Impact négatif réel sur la santé des bénévoles et des salariés : quatre accidents, dont une chute | **Risque** : hausse de 18 % de la prime d'assurance en 2027 ; difficulté à recruter des bénévoles |
| Réemploi des tuiles et des ardoises | Impact positif : réemploi de tuiles et d'ardoises issues de démolitions de tiers (déchets évités) ; la moindre extraction pour ses propres chantiers est une atténuation de ses impacts, et non un impact positif | Opportunité : économies d'achats, attentes des financeurs |
| Pierre importée du Portugal | Impact négatif potentiel dans la chaîne de valeur amont (extraction, transport) | Économie de 35 % ; risque d'image auprès des donateurs |
| Visiteurs en voiture, prairie humide | Impact négatif dans la chaîne de valeur aval : émissions, dégradation d'une zone humide | — |
| Accessibilité | Impact négatif sur les personnes à mobilité réduite (deux sites sur neuf accessibles) | Risque de perte de visiteurs et de financements |
| Legs de la maison | — | **Risque** : 48 000 € de travaux avant toute location ; opportunité de revenus locatifs |
| Convention de la Fondation | — | Opportunité ou risque : complément de 15 000 € si 9 500 heures de bénévolat sont atteintes |

**Distinction (0,5 pt)** : la **matérialité d'impact** porte sur les effets de l'association sur les personnes et l'environnement, appréciés par leur gravité (ampleur, étendue, caractère irrémédiable) et leur probabilité ; la **matérialité financière** sur les effets attendus sur sa situation, ses performances, ses flux de trésorerie ou son accès au financement, appréciés par leur probabilité et leur ampleur [V ESRS 1 (2026) § 39-40, § 47-48]. Un même sujet peut être matériel des deux points de vue (sécurité des chantiers) ; un impact positif (réemploi) ne compense pas un impact négatif [V § 35-36, § 44].

**Réponses tolérées**
- « Diligence raisonnable » ou « devoir de diligence » à la place de « vigilance raisonnable » : points complets.
- D'autres éléments tirés du contexte, s'ils sont correctement qualifiés.

**Erreurs fréquentes**
- Présenter la vigilance raisonnable comme une obligation de conduite imposée par les ESRS (`JUR-A01`).
- Ne retenir que des risques financiers, ou conduire l'analyse de double matérialité (notation, seuils), qui n'est pas demandée (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 42, § 56-59 | Vigilance raisonnable ; dialogue avec les parties prenantes | [V] ; application : [S] | F12 § 5, § 23 |
| ESRS 1 (2026) § 35-36, § 39-40, § 44, § 47-48 | Impacts ; risques et opportunités ; dépendances | [V] ; application : [S] | F12 § 6 |

### 3.10 Mission, assurance, démarche et procédures (4 pts)

**a. Objectifs, axes et assurance (2 pts)**
- **Objectifs (0,5 pt)** : un **avis** sur la conformité aux ESRS du **processus** mis en œuvre pour déterminer les informations publiées (analyse de double matérialité) et sur la conformité des **informations** publiées, dans un rapport destiné à l'assemblée générale [V L. 821-54 II, par analogie ; LD 2026 § 2]. L'association publie volontairement : la mission est conduite dans les conditions de la certification légale par hypothèse, les textes s'appliquant par analogie [S]. Elle ne garantit pas la qualité de la gestion [V L. 821-55].
- **Axes (0,75 pt)** : axe 1 (processus) et axe 2 (informations) ; l'axe de la taxonomie est sans objet, l'association n'y étant pas tenue, et celui du balisage aussi, faute de règles applicables ; la consultation du comité social et économique, qui n'est pas obligatoire pour une publication volontaire, est hors de la lettre de mission [V LD 2026 § 2, § 10 ; F12 § 11 (b)].
- **Assurance limitée (0,75 pt)** : vérifications moindres, en **nature**, en **étendue** et en **durée**, que pour une assurance raisonnable ; conclusion exprimée sous une **forme négative** (le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes), alors que l'opinion sur les comptes, fondée sur une assurance raisonnable, est exprimée sous une forme positive [V LD 2026, « Niveau d'assurance » ; NEP principes § 08].

**b. Étapes et procédures (2 pts)**
- **Étapes (0,75 pt)** : lettre de mission ; **prise de connaissance** de l'association (chantiers, bénévoles, financeurs) et des processus qui produisent les données (feuilles d'émargement et tableur, registre de tri, factures) ; **planification**, avec la sélection des informations **vérifiées spécifiquement**, celles qui présentent un risque important de non-conformité ou de fortes attentes des utilisateurs : ici les heures de bénévolat, attendues par la Fondation ; **contrôle du processus** (axe 1, achevé sans anomalie) ; **contrôle des informations** (axe 2) ; lecture d'ensemble et cohérence avec les comptes annuels (achats de matériaux, mécénat), en lien avec l'équipe qui les certifie ; communication avec la direction, déclarations écrites ; **rapport** d'assurance limitée par axe [V LD 2026 § 3-8, § 11-14, § 17 ; F13 § 3, § 7].
- **Procédures (1,25 pt ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 0,75 pt par donnée)** :
  - *Heures de bénévolat* : vérification de la **définition** (heures de présence, chantiers de l'année) ; **rapprochement** des feuilles d'émargement des onze chantiers avec le tableur (exhaustivité, absence de double saisie : il révèle les 720 heures du lavoir de Chambonnet) ; contrôle des **signatures** des chefs de chantier et rapprochement avec le planning des chantiers et la liste des bénévoles assurés (réalité) ; **procédure analytique** des heures par chantier et par rapport à 2025 ; **recalcul** du total (9 420 heures) [V LD 2026 § 8, § 12 ; S, procédures].
  - *Part des matériaux de réemploi* : vérification de la **définition** (poids, matériaux de couverture et de maçonnerie) ; **rapprochement** des 75,9 tonnes de matériaux neufs avec les factures et les bons de livraison, et avec les achats comptabilisés (exhaustivité du dénominateur, connectivité) ; **test** du registre de tri (pesées, origine des matériaux) et **observation** d'un chantier (réalité des 46,5 tonnes) ; **recalcul** : 46,5 / (46,5 + 75,9) = 46,5 / 122,4 = 38,0 % [V LD 2026 § 8 ; S, procédures].

**Réponses tolérées**
- En b., les étapes dans l'ordre du programme (prise de connaissance, planification, contrôle de la conformité des informations et du processus, contrôle du balisage, contrôle des exigences de publication, rapport) : points complets.

**Erreurs fréquentes**
- Retenir les axes de la taxonomie et du balisage pour une entité qui n'y est pas tenue, ou présenter l'assurance limitée comme une garantie (`JUR-A05`, `JUR-A01`).
- Proposer des procédures sans lien avec les deux données ni objectif (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; NEP principes § 08 | Objet de l'avis ; absence de garantie ; assurance raisonnable | [V] ; application à une mission volontaire : [S] | F13 § 2 ; F11 § 1.1 ; F12 § 11 |
| LD 2026 § 2-8, § 10-14, § 17, « Niveau d'assurance » | Axes ; assurance limitée ; étapes ; informations vérifiées spécifiquement | [V] ; procédures : [S] | F13 § 2-3, § 7 |

### 3.11 Avis sur les informations et comparaison avec l'opinion sur les comptes (2 pts)

**Avis si l'association maintient 10 140 heures (1,25 pt)**
- Les feuilles d'émargement représentent 9 420 heures : la donnée publiée comporte une **erreur** de 720 heures (7,6 % du nombre exact), que la direction refuse de corriger [S, calcul].
- Son importance ne tient pas qu'à son pourcentage : la donnée conditionne le versement complémentaire de la Fondation, fixé à **9 500 heures** ; publiée à 10 140 heures, elle franchit ce seuil, alors que le nombre exact (9 420) ne l'atteint pas. L'erreur peut influencer la décision d'un utilisateur, la Fondation : elle est d'une importance telle qu'elle **remet en cause la conformité** des informations [V LD 2026 § 17 ; S, qualification].
- Elle porte sur une donnée identifiée et chiffrée : ses incidences sont **clairement circonscrites**, et une réserve qui indique le nombre exact suffit à l'utilisateur : **avis de conformité assorti d'une réserve motivée** sur l'axe 2 ; sur l'axe 1, le processus ayant été vérifié sans anomalie, **avis de conformité** [V LD 2026 § 17 ; F13 § 4.2-4.3]. Ni avis de non-conformité, l'erreur étant circonscrite, ni impossibilité d'émettre un avis, aucune limitation n'existant. Une simple observation ne suffirait pas [V F13 § 4.4].
- Si l'association publie 9 420 heures, aucune erreur ne subsiste : avis de conformité sur les deux axes.

**Différences avec l'opinion sur les comptes (0,75 pt ; 0,25 pt par différence, dans la limite de 0,75 pt ; le niveau d'assurance, noté en 3.10 a., n'est pas noté de nouveau)**
- **Objet et référentiel** : conformité aux ESRS d'un processus et d'informations en partie non financières, contre la régularité, la sincérité et l'image fidèle des comptes au regard du plan comptable général [V L. 821-53 ; L. 821-54 II].
- **Structure** : un avis par axe, avec d'éventuelles observations et des éléments ayant fait l'objet d'une attention particulière, contre une opinion unique sur les comptes pris dans leur ensemble, avec la justification des appréciations [V LD 2026 § 17 ; NEP rapport § 18].
- **Vocabulaire** : avis de conformité, avec réserve, de non-conformité, impossibilité d'émettre un avis, contre certification sans réserve, avec réserve, refus et impossibilité de certifier [V LD 2026 § 17 ; R. 821-180].
- **Indépendance des conclusions** : l'erreur sur les heures de bénévolat n'affecte pas les comptes annuels, qui ne comportent aucune information chiffrée sur le bénévolat (hypothèse de l'énoncé) ; à l'inverse, une réserve sur les comptes n'entraîne pas de réserve sur les informations de durabilité [S].

**Réponses tolérées**
- Un avis de non-conformité sur l'axe 2, si le candidat soutient que la donnée est la plus attendue par la Fondation et que l'erreur affecte l'ensemble des informations sur les bénévoles : 0,25 pt sur 1,25.

**Erreurs fréquentes**
- Juger l'erreur négligeable au seul vu de son pourcentage, sans tenir compte du seuil de la convention (`JUR-F07`).
- Remplacer la réserve par une observation, ou appliquer à l'avis le vocabulaire de la certification des comptes (`JUR-A02`, `JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 12, § 17 | Importance des erreurs ; avis, réserve motivée, observations, structure par axe | [V] ; qualification : [S] | F13 § 3, § 4.1-4.4 |
| C. com. L. 821-53, L. 821-54 II ; NEP rapport § 18 ; R. 821-180 | Certification des comptes ; structure du rapport ; opinions | [V] | F11 § 1.1, § 8 |
