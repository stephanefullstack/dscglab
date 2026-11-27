# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 26

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 27/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.12 | `exercices/ex73_consolidation_anc_cours_historique_contrat_ecart_negatif` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.9 | `exercices/ex74_scission_valeur_reelle_engagements_retraite_soulte` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.13 | `exercices/ex75_audit_immobilisations_sarl_blanchisserie_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Obligation de consolider, exemptions écartées, référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 2 |
| 1.2 Objectif, utilisateurs, entité présentant l'information ; réponse à la famille | `2.1.a` Cadre conceptuel de l'IASB | 2 |
| 1.3 Périmètre, pourcentages et méthodes | `2.1.c` Périmètre de consolidation | 1 |
| 1.4 Écart d'acquisition négatif : ANC et IFRS | `2.1.d` Conséquences du référentiel | 1 |
| 1.5 Processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.6 a Amortissements dérogatoires de GIVRELANDE : stock et mouvement | `2.2.b` Retraitements préparatoires (provisions réglementées) | 2 |
| 1.6 b Écritures d'élimination | `2.2.b` Retraitements préparatoires (provisions réglementées) | 2 |
| 1.6 c Incidence sur le résultat et les capitaux propres consolidés | `2.2.b` Retraitements préparatoires (provisions réglementées) | 1 |
| 1.7 a Contrat à long terme : avancement, chiffre d'affaires, résultat, incidences | `2.2.c` Homogénéisation (contrats à long terme) | 2 |
| 1.7 b Écritures de retraitement | `2.2.c` Homogénéisation (contrats à long terme) | 2 |
| 1.7 c Incidence sur les réserves, le résultat et les capitaux propres | `2.2.c` Homogénéisation (contrats à long terme) | 1 |
| 1.8 a Méthode de conversion de l'atelier | `2.2.e` Conversion des comptes établis en devises | 1,5 |
| 1.8 b Bilan et compte de résultat convertis, écart de conversion | `2.2.e` Conversion des comptes établis en devises | 3,5 |
| 1.8 c Incidence sur le résultat ; méthode du cours de clôture | `2.2.e` Conversion des comptes établis en devises | 1 |
| 1.9 a Actif net réévalué, écart d'acquisition, écart d'évaluation | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.9 b Origine, traitement et reprise de l'écart négatif | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.10 Marge interne et comptes réciproques | `2.2.f` Comptes réciproques et résultats internes | 4 |
| 1.11 a Partage des capitaux propres de GIVRELANDE | `2.2.h` Partage des capitaux propres | 4 |
| 1.11 b Élimination des titres de GASTRAVÈNE Inox | `2.2.h` Partage des capitaux propres | 1 |
| 1.11 c Écritures d'élimination des titres et de partage | `2.2.h` Partage des capitaux propres | 1 |
| 1.12 a Compte de résultat consolidé | `2.3.a` Documents de synthèse consolidés | 4 |
| 1.12 b Annexe : conversion et écart négatif | `2.3.a` Documents de synthèse consolidés | 1 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires (réserves / résultat) ; `EA_NEG` = écart d'acquisition négatif (passif) ; `REP_EA_NEG` = reprise de l'écart d'acquisition négatif (compte de résultat) ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`RSV.GIVRELANDE` : réserves de GIVRELANDE ; `261.GASTRAVENE` : titres détenus par la SA). Toutes les écritures ci-dessous sont équilibrées.

---

### 1.1 Obligation de consolider et exemptions (2 pts)

- **Principe (0,5).** Les sociétés commerciales établissent et publient chaque année, à la diligence du directoire dans une SA à directoire, des comptes consolidés et un rapport sur la gestion du groupe dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 I ; F03 § 1.1]. La SA détient la majorité des droits de vote de GIVRELANDE (80 %) et de l'atelier (100 %) : elle les contrôle de manière exclusive [V L. 233-16 II 1°]. Elle est donc tenue de consolider, sauf exemption.
- **Exemption de la société contrôlée (0,75).** La SA pourrait s'en dispenser parce qu'elle est elle-même contrôlée par HALDENBRECK, qui l'inclut dans ses comptes consolidés publiés, et qu'elle n'émet ni valeurs mobilières admises sur un marché réglementé ni titres de créances négociables [V L. 233-17 1°]. Les conditions de forme seraient remplies : comptes de l'ensemble plus grand établis selon la législation d'un État membre prise pour l'application de la directive 2013/34/UE, certifiés et publiés, mis à la disposition des actionnaires de la SA avec leur traduction française ; HALDENBRECK ayant son siège dans l'Union, aucune information complémentaire n'est exigée ; l'exemption serait justifiée dans l'annexe des comptes annuels de la SA [V R. 233-15 ; F03 § 22] (0,25). Mais l'exemption est subordonnée à l'absence d'opposition d'actionnaires représentant **au moins le dixième du capital** : la famille BRÉHAUDIN, qui détient **30 %**, s'y est opposée (annexe 1.2) ; l'exemption est écartée (0,5).
- **Exemption des ensembles qui ne forment pas un grand groupe (0,5).** Un grand groupe dépasse, à la clôture, les seuils d'au moins deux des trois critères (30 M€ de total du bilan, 60 M€ de chiffre d'affaires net, 250 salariés en moyenne), réputés franchis à la clôture de deux exercices consécutifs [V L. 230-2 3° ; D. 230-2 ; F03 § 1.1]. L'ensemble formé par la SA et les sociétés qu'elle contrôle les dépasse tous les trois **en 2025** (520 salariés, 78,4 M€, 58,6 M€), alors même que GIVRELANDE n'en faisait pas encore partie, **et en 2026** (640 salariés, 90,36 M€, 77,9 M€) : c'est un grand groupe, l'exemption ne joue pas [V L. 233-17 2°].
- **Référentiel (0,25).** Aucun titre de la SA n'est admis aux négociations sur un marché réglementé : les IFRS ne lui sont pas imposées ; elle applique le règlement ANC n° 2020-01 et pourrait opter pour les IFRS adoptées, ce qui la dispenserait des règles comptables françaises pour ses comptes consolidés [V règlement (CE) n° 1606/2002, art. 4 ; L. 233-24 ; F03 § 1.2 et § 19.1]. La liasse demandée par HALDENBRECK n'y oblige pas ; mais opter pour les IFRS éviterait de tenir deux jeux de comptes consolidés : c'est la réponse à M. LOUVIGNÉ.

---

### 1.2 Objectif de l'information financière et entité présentant l'information (2 pts)

**Les notions (1,25).**
- **Objectif (0,5).** Selon le cadre conceptuel de 2018, l'information financière à usage général a pour objectif de fournir une information financière utile aux utilisateurs pour prendre des décisions relatives à l'apport de ressources à l'entité : acheter, vendre ou conserver des instruments de capitaux propres ou de dette, accorder ou régler des prêts, voter ou influer d'une autre manière sur les actes de la direction. Pour cela, les utilisateurs apprécient les perspectives de flux nets de trésorerie futurs et la manière dont la direction gère les ressources de l'entité (*stewardship*) ; ils ont besoin d'informations sur les ressources économiques de l'entité, les droits sur celle-ci et leurs variations [V Project Summary, p. 5 ; F03 § 7.2 et § 22].
- **Utilisateurs principaux (0,25).** Les investisseurs, prêteurs et autres créanciers, **actuels et potentiels**, qui doivent s'appuyer sur les rapports financiers pour une grande partie de l'information dont ils ont besoin [V p. 5].
- **Entité présentant l'information et comptes consolidés (0,5).** C'est l'entité qui est tenue, ou qui choisit, d'établir des états financiers ; ce n'est pas nécessairement une entité juridique. Les états financiers **consolidés** présentent les actifs, passifs, capitaux propres, produits et charges de la société mère **et** de ses filiales **comme une seule entité présentant l'information** ; son périmètre se détermine selon les besoins d'information des utilisateurs et ne peut être un ensemble arbitraire ou incomplet [V p. 7 ; F03 § 14].

**Réponse à Mme BRÉHAUDIN (0,75).** Les comptes consolidés d'HALDENBRECK présentent une autre entité, le groupe HALDENBRECK : la SA et ses filiales y sont des filiales parmi d'autres, combinées poste par poste avec elles, et la part de 30 % de la famille n'y figure que dans les participations ne donnant pas le contrôle (application, S). Or la famille est un **investisseur actuel de la SA** : ses décisions (garder ou vendre ses actions, voter en assemblée, apprécier la gestion du directoire) portent sur l'ensemble formé par la SA, GIVRELANDE et l'atelier d'Arad. Ce sont les comptes consolidés de la SA qui présentent cet ensemble comme une seule entité : ils montrent l'acquisition de GIVRELANDE, l'activité de l'atelier, les dettes et le résultat de ce groupe et la part des minoritaires de GIVRELANDE ; les comptes individuels de la SA, qui ne montrent que des titres et d'éventuels dividendes, n'y suffisent pas. C'est pour répondre à ce besoin que la loi permet aux actionnaires représentant au moins le dixième du capital de s'opposer à l'exemption (question 1.1).

---

### 1.3 Périmètre et méthodes (1 pt)

| Société | % de contrôle | Nature du lien | Méthode | % d'intérêt du groupe |
|---|---:|---|---|---:|
| GIVRELANDE | 80 % | Contrôle exclusif (majorité des droits de vote, président et trois sièges sur quatre) | Intégration globale | 80 % (minoritaires 20 %) |
| GASTRAVÈNE Inox | 100 % | Contrôle exclusif | Intégration globale | 100 % |
| ARMELIANE Installations | 15 % | Ni contrôle ni influence notable | Hors du périmètre ; titres de participation | (15 %) |

Tableau : 0,5. HALDENBRECK, qui contrôle la SA, n'entre pas dans le périmètre des comptes consolidés de la SA : ceux-ci partent de la SA et des entités qu'elle contrôle.

**ARMELIANE Installations (0,5).** L'influence notable est le pouvoir de participer aux politiques financière et opérationnelle d'une entité sans la contrôler ; elle est présumée à partir de 20 % des droits de vote et peut résulter notamment d'une représentation dans les organes de direction, de la participation aux décisions stratégiques, d'opérations importantes, d'échanges de dirigeants ou d'une dépendance technique [V ANC 2020-01, art. 211-5, p. 14 ; F03 § 2]. Avec 15 %, la présomption ne joue pas ; le siège au comité stratégique ne donne aucune participation aux politiques, puisque le comité ne rend que des avis et que le président arrête seul le budget, les investissements et les financements ; aucun autre indice n'existe (opérations inférieures à 2 %, pas d'échange de personnel, pas de dépendance). ARMELIANE Installations reste hors du périmètre ; ses titres figurent au bilan consolidé en titres de participation pour 450 000 € [V art. 212-3 par analogie ; F03 § 18.2].

---

### 1.4 Écart d'acquisition négatif : règlement ANC et IFRS (1 pt)

- **Règlement ANC (0,25).** L'écart négatif de 900 000 € (question 1.9) provient d'une rentabilité insuffisante : inscrit au passif, il est repris en résultat sur la durée du plan, 300 000 € par an de 2026 à 2028 [V art. 231-12, p. 24 ; F05 § 1.3 et § 8].
- **IFRS (0,25).** IFRS 3 ne distingue pas selon l'origine : l'excédent de la quote-part de l'actif net identifiable sur la contrepartie transférée est une acquisition à des conditions avantageuses ; après le réexamen de l'identification et de l'évaluation des actifs et passifs (ici fait et confirmé par l'expert), le profit est comptabilisé **en résultat à la date d'acquisition** et attribué à l'acquéreur [V IFRS 3 § 34 et § 36 ; F05 § 5 et § 11]. Les pertes futures prévues ne sont pas un passif de GIVRELANDE à la date d'acquisition et ne permettent pas d'étaler le profit (application, S).
- **Écart chiffré (0,5).** Dans la liasse IFRS, le résultat consolidé de 2026 comprend un profit de **900 000 €**, contre une reprise de 300 000 € en ANC : il est **supérieur de 600 000 €**, entièrement en part du groupe (les participations ne donnant pas le contrôle, évaluées à leur quote-part de l'actif net, ne reçoivent aucune part du profit). Les capitaux propres IFRS au 31/12/2026 sont supérieurs d'autant (plus de passif de 600 000 €) ; en 2027 et en 2028, ce sera l'inverse : le résultat ANC sera supérieur de 300 000 € chaque année.

---

### 1.5 Processus de consolidation (2 pts)

| Étape | Traitements du dossier |
|---|---|
| 1. Retraitements des comptes individuels, société par société : élimination des écritures fiscales et homogénéisation | Dérogatoires de GIVRELANDE (C1, C1R) ; contrat à long terme de la SA à l'avancement (C2, C2R) ; comptes de l'atelier retraités **en lei** par la direction financière |
| 2. Conversion des comptes de l'atelier | Cours historique (question 1.8) |
| 3. Évaluation à la date d'acquisition des actifs et passifs identifiables de GIVRELANDE | Écart d'évaluation de l'usine et son amortissement (C3, C3R) ; écart d'acquisition négatif |
| 4. Cumul des comptes retraités et convertis | SA, GIVRELANDE, atelier à 100 % ; ARMELIANE Installations non cumulée |
| 5. Éliminations des opérations internes | Marge interne (C5, C5R), ventes et dettes réciproques avec GIVRELANDE (C6, C7) ; opérations avec l'atelier (direction financière) |
| 6. Élimination des titres et partage des capitaux propres | GIVRELANDE (C8, 80 / 20) et reprise de l'écart négatif (C4, C4R) ; atelier (C9, 100 %) |

Tableau : 1 pt. Approche directe : chaque filiale est consolidée directement dans les comptes de la SA, avec le pourcentage d'intérêt de la SA [V art. 222-1 ; F03 § 3].

**Retraitements de l'atelier avant la conversion (0,5).** Les retraitements portent sur des montants exprimés dans la monnaie des comptes de l'entité ; faits en lei, ils sont ensuite convertis avec le poste qu'ils corrigent, chacun à son cours (un amortissement retraité suit le cours historique de son immobilisation). Les faire après la conversion obligerait à convertir séparément chaque correction et ferait apparaître un écart de conversion faux.

**Dérogatoires avant l'écart d'acquisition (0,5).** L'écart d'acquisition se calcule sur les actifs et passifs identifiables de GIVRELANDE évalués à la date d'acquisition **selon les méthodes du groupe** [V art. 231-9 ; 232-1 ; F05 § 1.2]. Dans ses comptes individuels, la provision réglementée (510 400 €) figure dans les capitaux propres ; pour le groupe, elle n'existe pas : 75 % sont des capitaux propres acquis (382 800 €) et 25 % un passif d'impôt différé (127 600 €) qui fait partie des passifs identifiables. Calculer l'écart avant cette élimination fausserait l'actif net acquis (de 127 600 € si l'on gardait toute la provision en capitaux propres, de 382 800 € si on l'ignorait), donc l'écart d'acquisition, le partage et les intérêts minoritaires.

---

### 1.6 Amortissements dérogatoires de GIVRELANDE (5 pts)

#### a. Stock au 01/01/2026 et mouvement de 2026 (2 pts)

Plan des comptes individuels (linéaire) : 2 560 000 / 10 = 256 000 € par an. Plan fiscal (dégressif, taux 22,5 % appliqué à la valeur nette fiscale ; le taux linéaire sur la durée restante, 1/8 en 2026, reste inférieur à 22,5 % : pas de passage au linéaire).

| Exercice | Valeur nette fiscale au 1er janvier | Annuité fiscale | Annuité linéaire | Dérogatoire de l'exercice |
|---|---:|---:|---:|---:|
| 2024 | 2 560 000 | 576 000 | 256 000 | + 320 000 |
| 2025 | 1 984 000 | 446 400 | 256 000 | + 190 400 |
| 2026 | 1 537 600 | 345 960 | 256 000 | **+ 89 960** (dotation) |

Annuités fiscales 0,75 ; dérogatoires annuels 0,5. **Stock au 01/01/2026 : 320 000 + 190 400 = 510 400 €** (0,5), date d'acquisition ; **mouvement de 2026 : dotation de 89 960 €** (compte 68725) (0,25) ; stock au 31/12/2026 : 600 360 €, égal à la différence entre la valeur nette comptable (1 792 000) et la valeur nette fiscale (1 191 640) de la ligne.

#### b. Écritures d'élimination (2 pts)

Les écritures passées pour la seule application de la législation fiscale sont éliminées ; la valeur fiscale de la ligne, inférieure à sa valeur consolidée, fait naître un impôt différé passif [V art. 272-1, p. 53 ; art. 272-8, p. 57 ; F04 R1]. Retraitement possible parce que GIVRELANDE est intégrée globalement.

**C1 (bilan) et C1R (compte de résultat), 1,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 145 Amortissements dérogatoires (stock au 31/12/2026) | 600 360 | |
| RSV.GIVRELANDE Réserves GIVRELANDE (510 400 × 75 %) | | 382 800 |
| RST.GIVRELANDE Résultat GIVRELANDE (89 960 × 75 %) | | 67 470 |
| IDP Impôt différé passif (600 360 × 25 %) | | 150 090 |
| *C1 – Élimination des amortissements dérogatoires* | **600 360** | **600 360** |
| CH_ID Charge d'impôt différé (89 960 × 25 %) | 22 490 | |
| RES_CR Résultat | 67 470 | |
| 68725 Dotations aux provisions réglementées – amortissements dérogatoires | | 89 960 |
| *C1R – Annulation de la dotation de 2026 (résultat exceptionnel)* | **89 960** | **89 960** |

**Destination du stock d'ouverture (0,5).** Les 382 800 € crédités aux réserves de GIVRELANDE sont des **capitaux propres existant à la date d'acquisition** : ils augmentent l'actif net acquis et entrent dans le calcul de l'écart d'acquisition (question 1.9) ; ils sont éliminés avec les titres (C8) et ne deviennent pas des réserves consolidées du groupe. Seuls 20 % (76 560 €) reviennent aux minoritaires, dans leurs réserves.

#### c. Incidence (1 pt)

- **Résultat consolidé (0,5)** : + 67 470 €, dont 53 976 € pour le groupe et 13 494 € pour les minoritaires (80 / 20).
- **Capitaux propres consolidés (0,5)** : réserves consolidées part du groupe **inchangées** (la part du groupe du stock d'ouverture, 306 240 €, accroît l'écart d'acquisition négatif) ; intérêts minoritaires + 90 054 € (76 560 en réserves et 13 494 en résultat) ; un impôt différé passif de 150 090 € remplace, au passif, la provision réglementée de 600 360 €.

---

### 1.7 Contrat de la cuisine centrale (5 pts)

#### a. Avancement et incidences (2 pts)

Le manuel retient la méthode à l'avancement, mesurée par les coûts : chiffre d'affaires cumulé = prix × pourcentage ; résultat cumulé = résultat à terminaison × pourcentage [V PCG art. 622-2 et 622-3 ; ANC art. 271-5 ; F04 R9]. Résultat à terminaison : 5 200 000 – 4 160 000 = 1 040 000 €, fiable et bénéficiaire.

| | 31/12/2025 | 31/12/2026 |
|---|---:|---:|
| Pourcentage d'avancement | 624 000 / 4 160 000 = **15 %** | 3 536 000 / 4 160 000 = **85 %** |
| Chiffre d'affaires cumulé | **780 000** | **4 420 000** |
| Résultat cumulé | **156 000** | **884 000** |

Pourcentages 0,5 ; chiffres d'affaires 0,5 ; résultats 0,5. Chiffre d'affaires de 2026 : 4 420 000 – 780 000 = 3 640 000 € ; coûts de 2026 (variation des en-cours à annuler) : 3 536 000 – 624 000 = 2 912 000 €. Comptes individuels à l'achèvement : aucun résultat.

| | Ouverture (réserves) | Exercice 2026 (résultat) | Clôture |
|---|---:|---:|---:|
| Avant impôt | + 156 000 | + 728 000 | 884 000 |
| Impôt différé passif (25 %) | – 39 000 | – 182 000 | IDP 221 000 |
| **Net** | **+ 117 000** | **+ 546 000** | **663 000** |

Tableau : 0,5. La marge à l'avancement n'est imposée qu'à l'achèvement (hypothèse de l'énoncé) : la différence est temporaire et imposable [V art. 272-8 ; F04 R9].

#### b. Écritures (2 pts)

| Compte | Débit | Crédit |
|---|---:|---:|
| 4191 Clients – avances et acomptes reçus sur commandes (situations facturées) | 3 900 000 | |
| 4181 Clients – factures à établir (4 420 000 – 3 900 000) | 520 000 | |
| 335 Travaux en cours | | 3 536 000 |
| IDP Impôt différé passif (884 000 × 25 %) | | 221 000 |
| RSV.GASTRAVENE Réserves SA (156 000 × 75 %) | | 117 000 |
| RST.GASTRAVENE Résultat SA (728 000 × 75 %) | | 546 000 |
| *C2 – Contrat à l'avancement (bilan), 1,25* | **4 420 000** | **4 420 000** |
| 7133 Variation des en-cours de production de biens | 2 912 000 | |
| CH_ID Charge d'impôt différé (728 000 × 25 %) | 182 000 | |
| RES_CR Résultat | 546 000 | |
| 704 Travaux (chiffre d'affaires de 2026) | | 3 640 000 |
| *C2R – Contrat à l'avancement (compte de résultat), 0,75* | **3 640 000** | **3 640 000** |

Le chiffre d'affaires cumulé (4 420 000) est couvert à hauteur de 3 900 000 par les situations déjà facturées, enregistrées en acomptes dans les comptes individuels, et pour le solde par une facture à établir.

#### c. Incidence (1 pt)

Réserves consolidées **+ 117 000 €**, résultat consolidé **+ 546 000 €**, capitaux propres consolidés **+ 663 000 €**, entièrement en part du groupe puisque le contrat est celui de la SA (0,75). Le bilan consolidé ne montre plus d'en-cours ni d'acomptes pour ce contrat, mais une facture à établir de 520 000 € et un impôt différé passif de 221 000 € ; le chiffre d'affaires consolidé de 2026 augmente de 3 640 000 € (0,25).

---

### 1.8 Conversion de GASTRAVÈNE Inox (6 pts)

#### a. Méthode (1,5 pt)

Une entité étrangère est **non autonome** lorsque son exploitation fait partie intégrante des activités d'une autre entité, notamment lorsque la monnaie de l'entité consolidante est prépondérante pour ses opérations ou son financement, ou lorsqu'elle a des liens commerciaux ou financiers prépondérants avec l'entité consolidante [V art. 272-15, commentaires IR3 et IR4, p. 59 ; F04 R13] (0,5). C'est le cas de l'atelier (0,5) : il vend toute sa production à la SA, à des prix fixés en euros par elle ; il achète son inox en euros ; il est financé par une avance en euros de la SA ; son budget, ses plannings et ses investissements sont décidés au siège ; seules ses dépenses locales sont en lei. Sa monnaie de fonctionnement est celle de l'entité dont il dépend, l'euro : ses comptes en lei sont convertis en euros selon la **méthode du cours historique**, comme si la SA avait elle-même réalisé ses opérations [V IR3 sous art. 272-15 ; art. 272-16 et 272-18, p. 59-60] (0,5).

#### b. Conversion et écart de conversion (3,5 pts)

Règles [V art. 272-16, p. 59-60 ; manuel] : éléments non monétaires (immobilisations et leurs amortissements, stocks, capital) au cours historique ; éléments monétaires au cours de clôture (5,20) ; produits et charges au cours moyen (5,10), sauf les dotations aux amortissements et les stocks, convertis au cours historique de l'actif concerné ; réserves converties et écarts de conversion cumulés d'ouverture fournis ; écart de conversion en capitaux propres [V art. 272-21, p. 61 ; F04 R13 ; manuel].

**Bilan au 31/12/2026 (1,5)**

| Actif | RON | Cours | € |
|---|---:|---:|---:|
| Matériel de 2019 | 950 000 | 4,75 | 200 000 |
| Machine laser | 1 485 000 | 4,95 | 300 000 |
| Stocks | 1 040 300 | 5,15 | 202 000 |
| Créance sur la SA | 1 560 000 | 5,20 | 300 000 |
| Autres créances | 104 000 | 5,20 | 20 000 |
| Disponibilités | 1 322 490 | 5,20 | 254 325 |
| **Total** | **6 461 790** | | **1 276 325** |

| Passif | RON | Cours | € |
|---|---:|---:|---:|
| Capital | 1 900 000 | 4,75 | 400 000 |
| Réserves | 759 560 | fournies | 139 600 |
| Écarts de conversion cumulés au 31/12/2025 | | fournis | 12 400 |
| Écart de conversion de l'exercice | | solde | **+ 4 425** |
| Résultat de 2026 converti (tableau suivant) | 292 230 | | 44 900 |
| Avance de la SA | 2 600 000 | 5,20 | 500 000 |
| Fournisseurs | 520 000 | 5,20 | 100 000 |
| Dettes fiscales et sociales | 390 000 | 5,20 | 75 000 |
| **Total** | **6 461 790** | | **1 276 325** |

**Compte de résultat de 2026 (1)**

| | RON | Cours | € |
|---|---:|---:|---:|
| Ventes à la SA | 10 200 000 | 5,10 | 2 000 000 |
| Achats d'inox et de fournitures | – 5 100 000 | 5,10 | – 1 000 000 |
| Stock au 01/01/2026 | – 764 560 | 5,03 | – 152 000 |
| Stock au 31/12/2026 | + 1 040 300 | 5,15 | + 202 000 |
| Charges de personnel | – 3 111 000 | 5,10 | – 610 000 |
| Autres charges externes | – 1 020 000 | 5,10 | – 200 000 |
| Impôts et taxes | – 102 000 | 5,10 | – 20 000 |
| Dotation, matériel de 2019 | – 475 000 | 4,75 | – 100 000 |
| Dotation, machine laser | – 247 500 | 4,95 | – 50 000 |
| Pertes de change nettes | – 30 600 | 5,10 | – 6 000 |
| Impôt sur les bénéfices | – 97 410 | 5,10 | – 19 100 |
| **Résultat converti** | **292 230** | | **44 900** |

**Écart de conversion (1)** : 1 276 325 – 675 000 (dettes) – 400 000 (capital) – 139 600 (réserves) – 12 400 (écarts antérieurs) – 44 900 (résultat) = **+ 4 425 €**, un gain né en 2026. Il naît des seuls éléments monétaires, convertis au cours de clôture alors que leurs variations l'ont été au cours moyen ou à des cours antérieurs : l'atelier a une position monétaire nette **passive** (dettes de 675 000 € contre 574 325 € de créances et de disponibilités) et le lei s'est déprécié. Il est inscrit dans les **capitaux propres consolidés**, au poste « Écarts de conversion » (manuel ; art. 272-21) : écarts cumulés au 31/12/2026, 12 400 + 4 425 = **16 825 €**, entièrement au groupe. Seul l'écart de l'exercice est calculé (un seul exercice converti) ; l'écart antérieur est fourni.

#### c. Incidence et comparaison (1 pt)

- **Incidence (0,5)** : l'atelier, détenu à 100 %, apporte **44 900 €** au résultat consolidé part du groupe (sa perte de change de 6 000 € reste dans le résultat financier) ; les capitaux propres consolidés augmentent de **4 425 €** au poste « Écarts de conversion » (16 825 € cumulés) ; aucun intérêt minoritaire.
- **Méthode du cours de clôture (0,5)** : les éléments non monétaires (immobilisations, stocks) seraient eux aussi convertis au cours de clôture, et toutes les charges, dotations et stocks compris, au cours moyen (résultat converti : 292 230 / 5,10 = 57 300 €) ; l'écart naîtrait alors sur l'actif net d'ouverture et sur le résultat, et non plus sur la seule position monétaire ; dans les deux méthodes, il va en capitaux propres [V art. 272-17 et 272-21, p. 60-61 ; F04 R13].

---

### 1.9 GIVRELANDE : écart d'évaluation et écart d'acquisition négatif (6 pts)

#### a. Actif net réévalué, écart d'acquisition et écart d'évaluation (3 pts)

| Élément au 01/01/2026 | Montant |
|---|---:|
| Capital | 1 800 000 |
| Réserves et report à nouveau | 2 992 200 |
| Amortissements dérogatoires, nets d'impôt différé (510 400 × 75 %, question 1.6) | 382 800 |
| **Capitaux propres retraités à la date d'acquisition** | **5 175 000** |
| Écart d'évaluation de l'usine (1 800 000 – 1 200 000) | + 600 000 |
| Impôt différé passif (600 000 × 25 %) | – 150 000 |
| **Actif net réévalué** | **5 625 000** |

Tableau : 1 (dont dérogatoires 0,25 et impôt différé 0,25) [V art. 231-9, 232-1, 272-13 ; F05 § 1.2]. **Écart d'acquisition (0,5)** : 3 600 000 – 80 % × 5 625 000 = 3 600 000 – 4 500 000 = **– 900 000 €**, un écart **négatif** [V art. 231-9 ; F05 § 1.3]. Aucun frais d'acquisition à ajouter au coût (frais non significatifs, supportés par le vendeur).

**Écart d'évaluation : C3 (bilan) et C3R (compte de résultat), 1,5 pt.** Amortissement de 2026 : 600 000 / 20 = 30 000 € ; impôt différé 7 500 € ; net 22 500 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments (1 800 000 – 1 200 000) | 600 000 | |
| RST.GIVRELANDE Résultat GIVRELANDE (30 000 × 75 %) | 22 500 | |
| 2813 Amortissements des constructions | | 30 000 |
| IDP Impôt différé passif ((600 000 – 30 000) × 25 %) | | 142 500 |
| RSV.GIVRELANDE Réserves GIVRELANDE (600 000 × 75 %) | | 450 000 |
| *C3 – Écart d'évaluation de l'usine* | **622 500** | **622 500** |
| 68112 Dotations aux amortissements des immobilisations corporelles | 30 000 | |
| CH_ID Produit d'impôt différé (30 000 × 25 %) | | 7 500 |
| RES_CR Résultat | | 22 500 |
| *C3R – Amortissement de 2026 de l'écart d'évaluation* | **30 000** | **30 000** |

#### b. Origine, traitement et reprise (3 pts)

**Origine (1).** Un écart d'acquisition négatif correspond généralement soit à un gain potentiel lié à une acquisition dans des **conditions avantageuses**, soit à une **rentabilité insuffisante** de l'entité acquise [V commentaire IR4 sous art. 231-12, p. 24 ; F05 § 8]. Ici, rien n'indique une bonne affaire : le vendeur n'était contraint ni par ses créanciers ni par sa situation, il avait reçu deux autres offres du même ordre, et l'expert a confirmé l'identification et l'évaluation des actifs et passifs. Le prix a été négocié en fonction des **pertes prévues par le plan de redressement** : 4 500 000 – 80 % × (3 × 375 000) = 4 500 000 – 900 000 = 3 600 000 €. L'écart reflète donc la rentabilité insuffisante de GIVRELANDE.

**Traitement (0,5).** L'écart négatif est inscrit au passif (poste « Autres dettes et comptes de régularisation », dont écarts d'acquisition négatifs [V art. 231-12, p. 24 ; art. 281-1, p. 66-67]) et rapporté au résultat sur une durée qui reflète les hypothèses retenues lors de l'acquisition [V art. 231-12, p. 24 ; F14 § 1.2] ; la reprise immédiate est réservée aux acquisitions dans des conditions avantageuses [V IR3 sous art. 231-12]. Le manuel retient une reprise linéaire sur la durée du plan, 2026 à 2028.

**Reprise de 2026 (0,5)** : 900 000 / 3 = **300 000 €**, au seul groupe (l'écart ne porte que sur la part de l'acquéreur). Elle compense la part du groupe dans la perte prévue de 2026 (80 % × 375 000 = 300 000) : c'est le sens de la règle. Elle figure sur la ligne propre aux écarts d'acquisition du résultat d'exploitation [V IR3 sous art. 231-12 ; art. 281-2 ; F14 § 1.3].

**Écritures (1).** L'écart négatif est inscrit par l'écriture d'élimination des titres (C8, question 1.11) ; la reprise :

| Compte | Débit | Crédit |
|---|---:|---:|
| EA_NEG Écart d'acquisition négatif GIVRELANDE | 300 000 | |
| RST_G Résultat consolidé – part du groupe | | 300 000 |
| *C4 – Reprise de 2026 (bilan)* | **300 000** | **300 000** |
| RES_CR Résultat | 300 000 | |
| REP_EA_NEG Reprise de l'écart d'acquisition négatif | | 300 000 |
| *C4R – Reprise de 2026 (compte de résultat)* | **300 000** | **300 000** |

Solde de l'écart négatif au passif au 31/12/2026 : 600 000 €.

---

### 1.10 Marge interne et comptes réciproques (4 pts)

**Marge à éliminer (0,5).** Chambres froides achetées en 2026 et en stock chez la SA : 240 000 × 25 % = **60 000 €** (taux de marge exprimé sur le prix de vente) ; impôt différé actif 15 000 € (la valeur consolidée du stock est inférieure à sa base fiscale) ; effet net – 45 000 € [V art. 251-2, p. 45 ; art. 272-8 ; F04 R14].

**Stock acheté en 2025 (0,5).** Les chambres froides de 96 000 € ont été achetées en novembre 2025, quand GIVRELANDE n'appartenait pas au groupe : sa marge a été réalisée avec un tiers et le coût d'achat de la SA est, pour le groupe, un coût d'acquisition auprès d'un tiers. Le résultat correspondant est compris dans les capitaux propres de GIVRELANDE au 01/01/2026, acquis et éliminés avec les titres : il n'y a aucun résultat interne à éliminer. Aucune marge n'est donc à éliminer à l'ouverture.

**Partage (0,5).** La vente est **montante** (de la filiale vers la mère) : la marge est éliminée en totalité, dans le résultat de GIVRELANDE qui l'a réalisée, puis partagée comme celui-ci : – 36 000 € pour le groupe, – 9 000 € pour les minoritaires (80 / 20) [V art. 251-2 ; manuel].

**C5 (bilan) et C5R (compte de résultat), 1,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.GIVRELANDE Résultat GIVRELANDE (60 000 × 75 %) | 45 000 | |
| IDA Impôt différé actif (60 000 × 25 %) | 15 000 | |
| 31 Matières premières et fournitures (SA) | | 60 000 |
| *C5 – Marge interne sur le stock de la SA* | **60 000** | **60 000** |
| 6031 Variation des stocks de matières premières et fournitures | 60 000 | |
| CH_ID Produit d'impôt différé | | 15 000 |
| RES_CR Résultat | | 45 000 |
| *C5R – Marge interne (compte de résultat)* | **60 000** | **60 000** |

**Ventes et soldes réciproques (1)** [V art. 251-1, p. 45 ; F04 R14]

| Compte | Débit | Crédit |
|---|---:|---:|
| 701 Ventes de produits finis (GIVRELANDE) | 4 200 000 | |
| 601 Achats stockés – matières premières et fournitures (SA) | | 4 200 000 |
| *C6 – Ventes de GIVRELANDE à la SA, 0,5* | **4 200 000** | **4 200 000** |
| 401 Fournisseurs (SA) | 630 000 | |
| 411 Clients (GIVRELANDE) | | 630 000 |
| *C7 – Dette de la SA envers GIVRELANDE, 0,5* | **630 000** | **630 000** |

Ces éliminations sont sans incidence sur le résultat consolidé ; seule la marge comprise dans le stock en a une.

---

### 1.11 Partage des capitaux propres (6 pts)

#### a. GIVRELANDE (4 pts)

Résultat retraité de 2026 : – 340 000 + 67 470 (dérogatoires, C1) – 22 500 (écart d'évaluation, C3) – 45 000 (marge interne, C5) = **– 340 030 €** (0,5).

| | Total retraité | Groupe (80 %) | Minoritaires (20 %) |
|---|---:|---:|---:|
| Capital | 1 800 000 | 1 440 000 | 360 000 |
| Réserves et report à nouveau | 2 992 200 | 2 393 760 | 598 440 |
| Dérogatoires du 01/01/2026, nets d'impôt | 382 800 | 306 240 | 76 560 |
| Écart d'évaluation net à l'entrée | 450 000 | 360 000 | 90 000 |
| **Capitaux propres retraités hors résultat (actif net réévalué)** | **5 625 000** | **4 500 000** | **1 125 000** |
| Élimination des titres | | – 3 600 000 | |
| Écart d'acquisition négatif inscrit au passif | | – 900 000 | |
| **Réserves consolidées** | | **0** | **1 125 000** |
| **Résultat retraité de 2026** | **– 340 030** | **– 272 024** | **– 68 006** |
| Reprise de 2026 de l'écart d'acquisition négatif | | + 300 000 | |
| **Résultat consolidé** | | **27 976** | **– 68 006** |

Tableau : 3 (capitaux propres retraités et parts 1,25 ; titres et écart négatif 0,75 ; résultat et reprise 1). Acquise le 01/01/2026 sans mouvement de capitaux propres depuis, GIVRELANDE n'apporte aucune réserve consolidée au groupe : toutes ses réserves retraitées sont des capitaux propres acquis. **Intérêts minoritaires au 31/12/2026 (0,5)** : 1 125 000 – 68 006 = **1 056 994 €**, écart d'évaluation compris (droits calculés sur l'actif net réévalué [V art. 232-1 ; F05 § 1.2]).

#### b. GASTRAVÈNE Inox (1 pt)

Capitaux propres convertis : capital 400 000 (1 900 000 RON au cours de 4,75), réserves 139 600, écarts de conversion cumulés 16 825 (12 400 + 4 425), résultat 44 900. La SA a souscrit tout le capital à la constitution pour 400 000 € : les titres égalent le capital converti au même cours historique, **aucun écart d'acquisition** (0,5). Le groupe, seul associé, reçoit les réserves converties (**139 600 €** en réserves consolidées), les écarts de conversion (**16 825 €**, au poste « Écarts de conversion ») et le résultat (**44 900 €**) (0,5).

#### c. Écritures (1 pt)

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.GIVRELANDE Capital GIVRELANDE | 1 800 000 | |
| RSV.GIVRELANDE Réserves retraitées (2 992 200 + 382 800 + 450 000) | 3 825 000 | |
| RST_G Résultat consolidé – part du groupe (80 % × – 340 030) | 272 024 | |
| RST_M Intérêts minoritaires – résultat (20 % × – 340 030) | 68 006 | |
| RST.GIVRELANDE Résultat retraité (perte) | | 340 030 |
| 261.GASTRAVENE Titres de participation GIVRELANDE | | 3 600 000 |
| EA_NEG Écart d'acquisition négatif (3 600 000 – 4 500 000) | | 900 000 |
| RSV_M Intérêts minoritaires – capital et réserves (20 % × 5 625 000) | | 1 125 000 |
| *C8 – Élimination des titres GIVRELANDE et partage, 0,75* | **5 965 030** | **5 965 030** |
| CAP_ELIM.INOX Capital converti | 400 000 | |
| RSV.INOX Réserves converties | 139 600 | |
| ECV.INOX Écarts de conversion (12 400 + 4 425) | 16 825 | |
| RST.INOX Résultat converti | 44 900 | |
| 261.GASTRAVENE Titres de participation GASTRAVÈNE Inox | | 400 000 |
| RSV_G Réserves consolidées – part du groupe | | 139 600 |
| ECV_G Écarts de conversion – part du groupe | | 16 825 |
| RST_G Résultat consolidé – part du groupe | | 44 900 |
| *C9 – Élimination des titres de l'atelier, 0,25* | **601 325** | **601 325** |

Pour information, capitaux propres consolidés au 31/12/2026 : capital 12 000 000 ; réserves consolidées 31 400 000 + 117 000 (contrat) + 0 (GIVRELANDE) + 139 600 (atelier) = 31 656 600 ; écarts de conversion 16 825 ; résultat part du groupe 5 478 876 (question 1.12) ; capitaux propres part du groupe **49 152 301 €** ; intérêts minoritaires **1 056 994 €**.

---

### 1.12 Compte de résultat consolidé de 2026 (5 pts)

#### a. Extrait du compte de résultat consolidé (4 pts)

| | Cumul SA et GIVRELANDE | Atelier converti | Retraitements et éliminations | Consolidé | Justification |
|---|---:|---:|---:|---:|---|
| Chiffre d'affaires | 94 560 000 | 2 000 000 | – 2 560 000 | **94 000 000** | + 3 640 000 contrat (C2R) ; – 4 200 000 ventes de GIVRELANDE (C6) ; – 2 000 000 ventes de l'atelier |
| Autres produits d'exploitation | 3 528 000 | — | – 2 912 000 | **616 000** | en-cours du contrat annulés (C2R) |
| Achats consommés | – 45 282 040 | – 950 000 | + 6 140 000 | **– 40 092 040** | + 4 200 000 et + 2 000 000 achats internes ; – 60 000 marge interne (C5R) |
| Charges de personnel | – 32 040 000 | – 610 000 | | **– 32 650 000** | |
| Autres charges d'exploitation | – 9 640 000 | – 200 000 | | **– 9 840 000** | |
| Impôts et taxes | – 1 460 000 | – 20 000 | | **– 1 480 000** | |
| Dotations aux amortissements, dépréciations et provisions | – 3 330 000 | – 150 000 | – 30 000 | **– 3 510 000** | écart d'évaluation de l'usine (C3R) |
| **Résultat d'exploitation avant dotations et reprises des écarts d'acquisition** | | | | **7 043 960** | |
| Reprises des écarts d'acquisition négatifs | — | — | + 300 000 | **300 000** | C4R, ligne propre |
| **Résultat d'exploitation après dotations et reprises des écarts d'acquisition** | | | | **7 343 960** | |
| Charges et produits financiers | – 256 000 | – 6 000 | | **– 262 000** | pertes de change de l'atelier comprises ; l'écart de conversion (+ 4 425) n'y figure pas : il est porté en capitaux propres |
| Charges et produits exceptionnels | 60 040 | — | + 89 960 | **150 000** | dotation aux dérogatoires annulée (C1R) |
| Impôts sur les résultats | – 1 620 000 | – 19 100 | – 181 990 | **– 1 821 090** | dont impôts différés – 181 990 : – 22 490 (C1R), – 182 000 (C2R), + 7 500 (C3R), + 15 000 (C5R) |
| **Résultat net des entités intégrées** | | | | **5 410 870** | |
| Résultat net lié aux entités mises en équivalence | | | | — | aucune |
| **Résultat net de l'ensemble consolidé** | **4 520 000** | **44 900** | **+ 845 970** | **5 410 870** | |
| Intérêts minoritaires | | | | **+ 68 006** | 20 % × – 340 030 : part des minoritaires dans la perte retraitée de GIVRELANDE |
| **Résultat net (part du groupe)** | | | | **5 478 876** | |

Répartition : chiffre d'affaires et éliminations des achats internes 1 ; autres produits, marge et dotations 0,5 ; reprise de l'écart négatif sur sa ligne et sous-totaux d'exploitation 0,5 ; résultat financier, pertes de change de l'atelier comprises, écart de conversion exclu car porté en capitaux propres 0,5 ; exceptionnel et impôts (différés distingués) 0,5 ; résultat de l'ensemble 0,5 ; intérêts minoritaires et part du groupe 0,5 [V art. 281-2, p. 67 ; F14 § 1.3].

Contrôle par les contributions au résultat part du groupe : SA 4 860 000 + 546 000 = 5 406 000 ; GIVRELANDE – 272 024 ; reprise de l'écart négatif + 300 000 ; atelier + 44 900 ; total **5 478 876 €**. Le chiffre d'affaires consolidé, 94 M€, est celui que publie le groupe.

#### b. Annexe consolidée (1 pt)

- **Conversion (0,5)** : l'annexe indique, parmi les méthodes comptables, que l'atelier d'Arad, entité non autonome dont l'activité dépend de la SA, est converti selon la méthode du cours historique et que l'écart de conversion de l'exercice (+ 4 425 €) est inscrit dans les capitaux propres, au poste « Écarts de conversion » (16 825 € cumulés au 31/12/2026) ; elle analyse les écarts de conversion résultant de l'intégration des filiales étrangères [V art. 282-2, p. 75 ; art. 282-21, p. 83 ; F14 § 10 et § 15].
- **Écart d'acquisition négatif (0,5)** : la note sur les écarts d'acquisition donne l'écart négatif de GIVRELANDE (900 000 €), sa méthode et sa durée de reprise (linéaire sur les trois exercices du plan de redressement, 2026 à 2028 ; 300 000 € repris en 2026, 600 000 € restant au passif), et l'origine qui la justifie [V art. 282-22, p. 83 ; F14 § 13].

---

### Réponses tolérées
- **1.1** : grand groupe établi sur deux critères seulement, si les deux exercices consécutifs sont examinés ; exemption de la société contrôlée écartée sans examen de ses conditions de forme, si l'opposition de la famille est relevée : – 0,25.
- **1.2** : objectif présenté sans la notion de gestion des ressources par la direction, si les décisions des utilisateurs sont citées.
- **1.3** : ARMELIANE Installations omise du tableau, si son exclusion est justifiée dans le texte : – 0,25.
- **1.4** : écart présenté pour l'ensemble des trois exercices (+ 600 000 en 2026, – 300 000 en 2027 et en 2028), si celui de 2026 est chiffré.
- **1.5** : évaluation des actifs et passifs de GIVRELANDE placée avant la conversion de l'atelier, ou éliminations placées avant l'évaluation : ces traitements sont indépendants ; l'ordre retraitements, cumul, éliminations, partage doit être respecté.
- **1.6 b** : écriture de bilan sans le stock d'ouverture distingué de la dotation, si la destination du stock d'ouverture (capitaux propres acquis) est expliquée : – 0,5.
- **1.7 b** : chiffre d'affaires cumulé enregistré en totalité en factures à établir, avec une écriture distincte d'annulation des acomptes, si le total est juste.
- **1.8 b** : écart de conversion calculé en ajoutant aux réserves les 12 400 € d'écarts antérieurs (réserves de 152 000 €), si l'écart de l'exercice (4 425 €) est isolé et porté en capitaux propres : – 0,25.
- **1.9 b** : reprise de l'écart négatif écrite dans l'écriture d'élimination des titres (C8), si le montant et la ligne du compte de résultat sont justes.
- **1.10** : marge éliminée au seul groupe, si le candidat signale que la vente est montante : – 0,5.
- **1.11 a** : réserves à l'acquisition et dérogatoires regroupés dans les réserves retraitées (3 825 000), si l'écart négatif est correctement imputé.
- **1.12 a** : présentation sans les colonnes intermédiaires, si chaque écart avec le cumul est justifié.
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (erreur non sanctionnée deux fois).

### Erreurs fréquentes
- **Obligation de consolider** : SA jugée exemptée « parce qu'HALDENBRECK consolide déjà » sans examen du droit d'opposition des minoritaires ; seuils examinés sur le seul exercice 2026, ou 2025 écarté parce que GIVRELANDE n'était pas encore acquise ; IFRS jugées obligatoires à cause de l'actionnaire allemand (`JUR-F06`).
- **Cadre conceptuel** : utilisateurs limités aux actionnaires majoritaires ; comptes consolidés d'HALDENBRECK présentés comme suffisants parce qu'ils comprennent la SA ; confusion entre entité présentant l'information et entité juridique.
- **Périmètre** : ARMELIANE Installations mise en équivalence à cause du siège au comité stratégique ; HALDENBRECK intégrée au périmètre de la SA (`JUR-F07`).
- **Dérogatoires** : stock du 01/01/2026 porté en réserves consolidées alors qu'il entre dans l'actif net acquis ; impôt différé actif au lieu de passif ; stock calculé avec un amortissement fiscal linéaire (`JUR-F05`, `JUR-G06`).
- **Contrat à long terme** : chiffre d'affaires de 2026 confondu avec le chiffre d'affaires cumulé ; effet de 2025 porté au résultat de 2026 ; en-cours ou acomptes oubliés ; impôt différé omis (`JUR-G04`).
- **Conversion** : méthode du cours de clôture retenue malgré la dépendance de l'atelier ; écart de conversion porté au résultat financier ; stocks ou dotations convertis au cours moyen ; réserves recalculées au lieu d'utiliser la contre-valeur fournie ; écart cumulé confondu avec l'écart de l'exercice.
- **Écart négatif** : reprise immédiate « parce que l'écart est négatif » ; écart négatif inscrit en capitaux propres ou en diminution des actifs ; reprise partagée avec les minoritaires ; dérogatoires ou impôt différé de l'écart d'évaluation oubliés dans l'actif net réévalué (`JUR-G01`).
- **Marge interne** : marge des chambres froides achetées en 2025 éliminée ; marge calculée sur le coût (240 000 × 25 / 125) alors qu'elle est exprimée sur le prix de vente ; élimination imputée au seul groupe.
- **Partage et compte de résultat** : partage sur des capitaux propres non retraités (`JUR-G04`) ; écart d'acquisition négatif oublié, laissant 900 000 € de réserves consolidées fictives ; reprise de l'écart négatif placée dans le résultat exceptionnel ou financier ; ventes de l'atelier non éliminées ; intérêts minoritaires négatifs présentés en charge ; montants sans justification (`JUR-F02`), écritures non équilibrées (`JUR-F04`).

### Références
- Code de commerce : L. 233-16 I et II, L. 233-17 1° et 2°, R. 233-15, L. 230-2, D. 230-2, L. 233-24 [V, F03 § 1.1, § 1.2, § 19.1 et § 22] ; règlement (CE) n° 1606/2002, art. 4 [V, F03 § 1.2].
- Cadre conceptuel de l'IASB (2018) : objectif, utilisateurs, entité présentant l'information, états financiers consolidés [V Project Summary, p. 5 et 7, F03 § 7.2, § 14 et § 22].
- IFRS 3 § 34 à 36 [V, F05 § 11].
- PCG : art. 622-2, 622-3 (contrats à long terme) [V, F04 R9].
- Règlement ANC n° 2020-01 : art. 211-5, 212-3, 222-1 [V, F03 § 2, § 3 et § 18.2] ; art. 231-9, 231-12 et commentaires IR3 et IR4, 232-1, 272-13 [V, F05 § 1 et § 8] ; art. 251-1, 251-2, 271-5, 272-1, 272-8, 272-15 et commentaires, 272-16 à 272-18, 272-21 [V, F04 R1, R9, R13, R14] ; art. 281-2, 282-2, 282-21, 282-22 [V, F14 § 1.3, § 10, § 13 et § 15].

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, distinction avec une cession suivie d'une liquidation, référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2 |
| 2.2 Régime fiscal de faveur : conditions, branche incomplète, effets et engagements | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 2 |
| 2.3 Parités, actions émises, répartition du capital après l'opération | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 3 |
| 2.4 Soulte, contrainte légale, équité ; demande de M. MÉNAVRIL et conseil | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 3 |
| 2.5 Contrôle, sens et mode d'évaluation de chaque apport | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 2 |
| 2.6 Valeur et composition des apports, provision pour impôts, fonds commercial, augmentations de capital et primes | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée ; `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 3 |
| 2.7 Écritures de base chez VERDOMÈNE, CHARMILLÉE et ARBORESSE | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 4 |
| 2.8 Écritures complémentaires chez CHARMILLÉE : dérogatoires, frais, créance réciproque | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 4 |
| 2.9 Note à M. FONTALBE | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Qualification, distinction et référentiel (2 pts)

**Qualification et modalités (1 pt).** VERDOMÈNE transmet **tout son patrimoine**, réparti en deux branches, à **deux sociétés qui existent déjà** : c'est une **scission** [V C. com. L. 236-18, al. 1 ; PCG art. 710-2, F01 § 1]. Le PCG définit encore la scission par renvoi à l'ancien alinéa 2 de l'art. L. 236-1 ; depuis l'ordonnance n° 2023-393, cet article ne vise plus que la fusion et la scission est définie à l'art. L. 236-18 [V F01 § 1 et Corrections du 23/10/2026]. Les modalités sont celles de la fusion, rendues applicables à la scission [V C. com. L. 236-19, F01 § 4] :
- **transmission universelle** : CHARMILLÉE reçoit, dans l'état où ils se trouvent le 30 juin 2027, tous les actifs et toutes les dettes de la branche paysage, y compris l'impôt de la période que le traité y rattache et la créance sur elle-même ; ARBORESSE reçoit ceux de la branche pépinière, y compris l'engagement de retraite envers son personnel, qui ne figure pas au bilan [V C. com. L. 236-3, I, F01 § 1] ;
- **dissolution sans liquidation** de VERDOMÈNE : aucun actif n'est vendu, aucune dette n'est payée par la société, aucun partage n'a lieu ;
- **rémunération** : CHARMILLÉE et ARBORESSE **augmentent leur capital** ; les actions nouvelles et la soulte versée par ARBORESSE reviennent aux actionnaires de VERDOMÈNE, qui deviennent associés des deux bénéficiaires en échange de leurs actions, annulées avec la société. La soulte ne peut dépasser 10 % de la valeur nominale des actions attribuées [V C. com. L. 236-18, al. 3, F01 § 4].

**Distinction avec une cession des deux branches suivie d'une liquidation (0,75 pt).**

| | Scission | Cession des deux branches, puis liquidation |
|---|---|---|
| Ce que reçoit VERDOMÈNE | Rien de durable : les actions des bénéficiaires et la soulte vont aux actionnaires | Un prix en numéraire, payé par chaque acquéreur, qui doit le financer |
| Imposition chez VERDOMÈNE | Plus-values en sursis sous le régime de faveur (2.2) | Cessation d'entreprise : plus-values de cession et amortissements dérogatoires imposés immédiatement à l'IS |
| Actionnaires | Deviennent associés de CHARMILLÉE et d'ARBORESSE ; seule la soulte (60 000 €) est payée en numéraire | Reçoivent, après paiement des dettes et de l'impôt, un boni de liquidation en numéraire, imposé chez eux, et ne gardent aucun lien avec les deux branches |
| Formalités | Une seule opération : transmission universelle des contrats, des dettes et du personnel | Cession de chaque élément et de chaque contrat, puis opérations de liquidation et de partage |

La scission permet ainsi à FONTALBE Participations de garder le paysage, réuni à CHARMILLÉE, et de rester associée de la pépinière à travers ARBORESSE, sans sortie de trésorerie chez les bénéficiaires autre que la soulte.

**Référentiel (0,25 pt).** L'enregistrement de l'opération dans les comptes individuels des trois sociétés relève du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe les valeurs d'inscription des apports [V art. 710-1 et 720-1, F01 § 1]. Ces règles ne s'appliquent pas au calcul de la parité, qui repose sur les valeurs d'échange fournies [V art. 740-1, F01 § 1] : ce point sera décisif pour CHARMILLÉE (2.3 et 2.6).

---

### 2.2 Régime fiscal de faveur (2 pts)

**Conditions et appréciation (0,75 pt).** Les trois sociétés sont passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1]. Le régime de l'art. 210 A s'applique **de plein droit**, sans agrément ni engagement de conservation des titres pour les scissions réalisées depuis le 01/01/2018, à la scission d'une société qui comporte **au moins deux branches complètes d'activité** lorsque chaque bénéficiaire reçoit une ou plusieurs de ces branches [V CGI art. 210 B-1 ; BOI-IS-FUS-20-30-10 § 70, F02 § 1 et Corrections du 22/10/2026]. Une branche complète est l'ensemble des éléments d'une division qui constituent une exploitation autonome, capable de fonctionner par ses propres moyens, avec son personnel, sa clientèle et ses installations [V BOI-IS-FUS-20-20 § 10, 60 et 80, F02 § 1]. Ici, chaque branche exerce réellement son activité, avec son responsable, son personnel (22 et 31 salariés), ses installations, ses fournisseurs, ses clients et son propre secrétariat ; tous les éléments de VERDOMÈNE sont rattachés à l'une des deux branches et chaque bénéficiaire en reçoit une : les conditions sont remplies. La définition fiscale de la scission admet une soulte limitée à 10 % de la valeur nominale des titres attribués [V CGI art. 210-0 A, I, 2°, F02 § 1] : condition remplie (2.4). Le motif économique (financer la pépinière, rapprocher les deux entreprises de paysage) rend la présomption de fraude ou d'évasion fiscales difficile à soutenir [V CGI art. 210-0 A, III, F02 § 1].

**Si la branche paysage n'était pas complète (0,5 pt).** VERDOMÈNE n'aurait plus deux branches complètes : le régime de faveur ne s'appliquerait que sur **agrément** de l'administration, accordé si l'opération est justifiée par un motif économique, si ses modalités assurent l'imposition future des plus-values en sursis et si les associés détenant au moins 5 % des droits de vote, ainsi que ceux qui exercent ou ont exercé dans les six mois des fonctions de direction en détenant au moins 0,1 %, s'engagent à **conserver pendant trois ans** les titres reçus [V CGI art. 210 B-3, F02 § 1]. FONTALBE Participations (70 %) et M. MÉNAVRIL (16 %) seraient tenus par cet engagement, ce qui contrarierait le projet de M. MÉNAVRIL (2.4 b) ; chaque salarié détient au plus 2,67 % des droits de vote : aucun ne serait tenu, sauf s'il exerce des fonctions de direction en détenant au moins 0,1 %. Sans agrément, le droit commun s'appliquerait.

**Effets pour VERDOMÈNE (0,25 pt).** Les plus-values sur les éléments transmis ne sont **pas soumises à l'IS** [V CGI art. 210 A-1, F02 § 2] : 410 000 € sur la branche pépinière (2.7), aucun sur la branche paysage, transmise à sa valeur comptable. Les amortissements dérogatoires (64 000 €) ne sont pas imposés chez VERDOMÈNE puisqu'ils sont reconstitués chez CHARMILLÉE et réintégrés dans les mêmes conditions [V BOI-IS-FUS-30-20 § 10, F02 § 2 et § 1]. Le résultat de la période du 1er janvier au 30 juin 2027 reste imposé chez VERDOMÈNE quel que soit le régime : l'impôt de 63 000 € figure dans les dettes reprises par CHARMILLÉE [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2]. Sous le droit commun, la scission serait une cessation d'entreprise et les plus-values comme les dérogatoires seraient imposés immédiatement [V BOI-IS-FUS-10-10-10 § 1, F02 § 2].

**Engagements des bénéficiaires (0,5 pt)** [V CGI art. 210 A-3, F02 § 4] :
- *CHARMILLÉE* reprend à son passif les provisions dont l'imposition est différée : elle **reconstitue les 64 000 € d'amortissements dérogatoires** de la branche paysage et les réintègre comme VERDOMÈNE l'aurait fait [V 210 A-3-a ; BOI-IS-FUS-30-20 § 10, F02 § 1 et § 2] ; recevant la branche à la valeur comptable, elle reprend aussi les valeurs brutes, les amortissements et les valeurs fiscales de VERDOMÈNE [V BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2].
- *ARBORESSE* réintègre la plus-value sur les serres et ombrières sur 15 ans (160 000 / 15 = 10 667 € par an) et celle sur le réseau d'irrigation sur 5 ans (40 000 / 5 = 8 000 € par an), les constructions représentant 80 % de la plus-value nette sur biens amortissables, sous le seuil de 90 % [V 210 A-3-d, F02 § 2] ; elle inscrit fiscalement les plants à leur valeur chez VERDOMÈNE, si bien que le profit de 120 000 € sera imposé à leur vente [V 210 A-3-e] ; elle calculera une plus-value future sur les terrains d'après leur valeur fiscale de 180 000 € [V 210 A-3-c]. En contrepartie, ses amortissements sont calculés sur la valeur d'apport. Ces impositions futures justifient la provision pour impôts intégrée à l'apport (2.6 b).

---

### 2.3 Parités, actions émises et répartition du capital (3 pts)

Dans une scission, chaque bénéficiaire émet un nombre d'actions déterminé par la valeur d'échange de la branche qu'elle reçoit [S guide p. imprimée 163, d'après `programme/perimetre_ue4.yaml`, compétence 1.2.a], et non par la valeur globale de VERDOMÈNE (2 940 000 €).

**a) CHARMILLÉE (1 pt)**
- Valeur unitaire : 1 600 000 / 50 000 = **32 €** ; valeur de la branche paysage par action VERDOMÈNE : 1 440 000 / 30 000 = **48 €** (0,25 pt).
- Parité : 48 / 32 = **3 actions CHARMILLÉE pour 2 actions VERDOMÈNE** (0,25 pt).
- Actions à émettre : 30 000 × 3 / 2 = **45 000 actions** (contrôle : 1 440 000 / 32 = 45 000). FONTALBE Participations (21 000 actions), M. MÉNAVRIL (4 800) et chacun des salariés (multiples de 10) détiennent un nombre pair d'actions : pas de rompus, pas de soulte (0,5 pt).

**b) ARBORESSE (1 pt)**
- Valeur unitaire : 1 920 000 / 12 000 = **160 €** ; valeur de la branche pépinière par action VERDOMÈNE : 1 500 000 / 30 000 = **50 €** (0,25 pt).
- Parité exacte : 50 / 160 = 0,3125 = **5 actions ARBORESSE pour 16 actions VERDOMÈNE**, soit 30 000 × 5 / 16 = 9 375 actions (0,25 pt).
- Motif du traité (0,25 pt) : FONTALBE Participations devrait recevoir 21 000 × 5 / 16 = 6 562,5 actions et les salariés ensemble 1 312,5 ; parmi les trois groupes d'associés, seul M. MÉNAVRIL (4 800 = 300 × 16) recevrait un nombre entier (1 500). Il faudrait traiter des **rompus**, associé par associé. Le traité retient une parité simple, **3 pour 10**, applicable à toutes les actions puisque chaque associé détient un multiple de 10 actions, et compense l'écart par une soulte (2.4).
- Actions émises : 30 000 × 3 / 10 = **9 000 actions** ARBORESSE (0,25 pt).

**c) Répartition du capital et des droits de vote (1 pt)**

CHARMILLÉE — 50 000 + 45 000 = 95 000 actions (0,5 pt) :

| Associé | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| FONTALBE Participations (30 000 + 21 000 × 3 / 2) | 30 000 | 60,00 % | 61 500 | 64,74 % |
| Mme TESSONNIER | 20 000 | 40,00 % | 20 000 | 21,05 % |
| M. MÉNAVRIL (4 800 × 3 / 2) | – | – | 7 200 | 7,58 % |
| Salariés de VERDOMÈNE (4 200 × 3 / 2) | – | – | 6 300 | 6,63 % |
| **Total** | **50 000** | **100 %** | **95 000** | **100 %** |

ARBORESSE — 12 000 + 9 000 = 21 000 actions (0,5 pt) :

| Associé | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| BRÉHALIER Développement | 10 800 | 90,00 % | 10 800 | 51,43 % |
| M. PIERREFEU | 1 200 | 10,00 % | 1 200 | 5,71 % |
| FONTALBE Participations (21 000 × 3 / 10) | – | – | 6 300 | 30,00 % |
| M. MÉNAVRIL (4 800 × 3 / 10) | – | – | 1 440 | 6,86 % |
| Salariés de VERDOMÈNE (4 200 × 3 / 10) | – | – | 1 260 | 6,00 % |
| **Total** | **12 000** | **100 %** | **21 000** | **100 %** |

Chaque action donnant une voix, les droits de vote suivent la même répartition. FONTALBE Participations **renforce** sa majorité chez CHARMILLÉE ; chez ARBORESSE, BRÉHALIER Développement garde la majorité des voix, et donc seule la nomination et la révocation du président, et FONTALBE Participations n'est qu'associée minoritaire. Ces constats fondent l'analyse de 2.5.

---

### 2.4 Soulte et demande de M. MÉNAVRIL (3 pts)

**a) Soulte du projet de traité (1,5 pt)**
- *Montant (0,5 pt).* 1 500 000 – 9 000 × 160 = **60 000 €**, soit 50 – 3 / 10 × 160 = 50 – 48 = **2 € par action VERDOMÈNE**. Par associé : FONTALBE Participations 21 000 × 2 = **42 000 €**, M. MÉNAVRIL 4 800 × 2 = **9 600 €**, salariés 4 200 × 2 = **8 400 €** (chacun à raison de 2 € par action).
- *Contrainte légale (0,5 pt).* La soulte ne peut dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-18, al. 3, F01 § 4] : 10 % × 9 000 × 100 = **90 000 €**, soit 3 € par action VERDOMÈNE. La soulte de 60 000 € (66,67 % du plafond) est **légale** ; elle reste aussi dans la limite de la définition fiscale de la scission, ce qui préserve le régime de faveur [V CGI art. 210-0 A, I, 2°, F02 § 1]. CHARMILLÉE, qui applique la parité exacte, ne verse aucune soulte.
- *Équité (0,5 pt).* Pour une action VERDOMÈNE (48 + 50 = 98 €), l'associé reçoit 3 / 2 action CHARMILLÉE (48 €), 3 / 10 action ARBORESSE (48 €) et 2 € : 48 + 48 + 2 = **98 €** [V méthode du corrigé du sujet zéro, F01 § 4]. Pour la seule pépinière : 9 000 × 160 + 60 000 = 1 500 000 €. Après l'opération, l'action CHARMILLÉE vaut toujours (1 600 000 + 1 440 000) / 95 000 = 32 € et l'action ARBORESSE (1 920 000 + 1 500 000 – 60 000) / 21 000 = 160 € : aucun groupe d'associés ne s'enrichit aux dépens d'un autre.

**b) Demande de M. MÉNAVRIL et conseil (1,5 pt)**
- *Analyse (0,5 pt).* Avec 1 action ARBORESSE pour 4 actions VERDOMÈNE, ARBORESSE émettrait 7 500 actions et la soulte serait de 50 – 160 / 4 = 10 € par action, soit **300 000 €** au total. Le plafond légal tomberait à 10 % × 7 500 × 100 = **75 000 €** (2,50 € par action). La soulte demandée en représente **quatre fois** le montant : elle est **interdite** [V C. com. L. 236-18, al. 3, F01 § 4]. M. MÉNAVRIL a raison sur l'équité (40 + 10 = 50 €), mais l'équité ne suffit pas : la loi limite la part du numéraire.
- *Ce qui ne peut pas être fait (0,5 pt).* Conserver la parité de 1 pour 4 en ramenant la soulte au plafond (2,50 €) rendrait l'échange **inéquitable** : chaque associé de VERDOMÈNE recevrait 42,50 € au lieu de 50 €, soit 225 000 € transférés aux associés d'ARBORESSE ; un tel transfert de valeur exposerait VERDOMÈNE à un produit taxable et l'opération à la perte du régime de faveur [V BOI-IS-FUS-30-20 § 20 et 30, F02 § 1]. Une soulte supérieure au plafond ferait sortir l'opération de la définition fiscale de la scission, et le régime de faveur, qui s'applique à l'ensemble des apports, serait perdu pour les deux branches [V CGI art. 210-0 A, I, 2° ; BOI-IS-FUS-20-30-10 § 10, F02 § 1] : imposition immédiate de la plus-value de 410 000 € et des dérogatoires de 64 000 €. La parité de 1 pour 4 recréerait d'ailleurs des rompus pour tout salarié dont le nombre d'actions n'est pas un multiple de 4 (10, 30, 50…). Avec le nominal de 100 €, la soulte qui égalise les valeurs ne peut d'ailleurs pas dépasser 50 × 10 / 170 = 2,94 € par action : celle du traité (2 €) en est proche.
- *Conseil (0,5 pt).* Maintenir la parité de 3 pour 10 et la soulte de 2 € par action, et répondre autrement au besoin de M. MÉNAVRIL. La scission étant placée de plein droit sous le régime de faveur, **aucun engagement de conservation** ne pèse sur les associés (2.2) : après l'opération, M. MÉNAVRIL pourra céder tout ou partie de ses 1 440 actions ARBORESSE (230 400 € à 160 €) et de ses 7 200 actions CHARMILLÉE (230 400 € à 32 €), par exemple à BRÉHALIER Développement ou à FONTALBE Participations. Cette cession, distincte de la scission, se négocie entre les parties et ne remet en cause ni la légalité de la soulte ni le régime fiscal de l'opération.

Grille de niveaux pour le conseil : 0 (absence, ou demande acceptée) ; 0,25 (refus justifié par le seul plafond) ; 0,5 (refus justifié et solution de remplacement reliée à l'absence d'engagement de conservation).

---

### 2.5 Contrôle, sens et mode d'évaluation de chaque apport (2 pts)

**Situation de contrôle (0,5 pt).** Le contrôle s'apprécie au niveau des personnes morales [V PCG art. 741-1 et 741-2, F01 § 2.1]. FONTALBE Participations contrôle de manière exclusive VERDOMÈNE (70 % des voix) et CHARMILLÉE (60 %, majorité qui lui donne seule la nomination du président) : les deux sociétés sont **sous le contrôle commun** d'une même entité mère. ARBORESSE est contrôlée de manière exclusive par BRÉHALIER Développement (90 %), sans lien avec FONTALBE Participations : VERDOMÈNE et ARBORESSE sont **sous contrôle distinct**. Aucun accord entre actionnaires ne crée de contrôle partagé.

**Branche paysage → CHARMILLÉE (0,75 pt).** Contrôle commun : l'apport est évalué à la **valeur comptable**, quel que soit le sens de l'opération (cas 1 et 2), car il s'agit d'un maintien ou d'un renforcement du contrôle et qu'il convient de ne pas réévaluer [V art. 743-1, F01 § 2.3]. L'opération est d'ailleurs à l'endroit : FONTALBE Participations, actionnaire principal de CHARMILLÉE, garde et renforce son contrôle (60 % → 64,74 %). Des actions sont bien émises, puisque les associés de VERDOMÈNE et ceux de CHARMILLÉE ne sont pas les mêmes dans les mêmes proportions. L'exception de l'art. 743-3 est examinée en 2.6 a.

**Branche pépinière → ARBORESSE (0,75 pt).** BRÉHALIER Développement, actionnaire principal d'ARBORESSE, conserve le contrôle, bien que diluée (90 % → 51,43 %) ; FONTALBE Participations perd le contrôle de la pépinière et ne prend pas celui d'ARBORESSE (30 %). L'apport est **à l'endroit** : ARBORESSE est l'initiatrice, la branche pépinière la cible [V art. 730-1 et 742-1, F01 § 1 et § 2.2]. Contrôle distinct et sens à l'endroit : **valeur réelle** (cas 4), l'opération étant traitée comme une acquisition [V art. 743-1, F01 § 2.3].

Chaque apport s'analyse séparément : une même scission combine ici une évaluation à la valeur comptable et une évaluation à la valeur réelle.

---

### 2.6 Valeur et composition des apports (3 pts)

**a) Branche paysage à la valeur comptable (0,75 pt)**
- *Valeur et composition (0,5 pt).* Valeur d'apport = **actif net comptable** de la branche : 1 250 000 – 510 000 = **740 000 €** [V art. 744-2, F01 § 3.2]. Les amortissements dérogatoires (64 000 €) sont des provisions réglementées, classées dans les capitaux propres : ils ne sont pas déduits, et l'actif net apporté les comprend [V PCG art. 214-8 et 313-1, F01 § 8]. CHARMILLÉE reprend les valeurs brutes et les amortissements de VERDOMÈNE [V BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2] : matériel de transport 520 000 (amorti de 310 000), engins et matériels 680 000 (amortis de 390 000), fournitures 60 000, clients 540 000 (dont 27 600 dus par CHARMILLÉE), disponibilités 150 000 ; à déduire : emprunt 120 000, fournisseurs 180 000, dettes fiscales et sociales 210 000. L'écart de 700 000 € entre la valeur d'échange et l'actif net comptable (1 440 000 – 740 000), qui comprend notamment la valeur des contrats d'entretien et de la clientèle de collectivités, n'est pas inscrit. CHARMILLÉE ne provisionnant pas ses engagements de retraite, aucun ajustement de la provision pour retraites n'est à faire [V art. 744-3, F01 § 3.2].
- *Libération du capital (0,25 pt).* Si l'actif net comptable était insuffisant pour libérer le capital émis, les valeurs réelles devraient être retenues [V art. 743-3, F01 § 2.4]. Le capital émis est de 45 000 × 10 = 450 000 € : l'actif net comptable de 740 000 € le couvre ; la valeur comptable est maintenue.

**b) Branche pépinière à la valeur réelle (1,75 pt)**

*Éléments identifiés (0,5 pt).* En valeur réelle, le traité retient la valeur réelle de chaque élément identifié, qu'il figure ou non au bilan de VERDOMÈNE [V art. 744-1, F01 § 3.1] : l'**engagement d'indemnités de départ à la retraite** (96 000 €), que VERDOMÈNE ne provisionnait pas, est un **passif identifié** de l'apport.

| Élément | Valeur nette comptable | Valeur réelle | Écart |
|---|---:|---:|---:|
| Terrains | 180 000 | 260 000 | + 80 000 |
| Serres et ombrières | 360 000 | 520 000 | + 160 000 |
| Réseau d'irrigation et de brumisation | 100 000 | 140 000 | + 40 000 |
| Tracteurs, rempoteuse et matériels | 120 000 | 120 000 | 0 |
| Plants et arbres en culture | 640 000 | 760 000 | + 120 000 |
| Clients | 310 000 | 310 000 | 0 |
| Disponibilités | 90 000 | 90 000 | 0 |
| **Actifs identifiés** | **1 800 000** | **2 200 000** | **+ 400 000** |
| Dettes (420 000 + 150 000 + 140 000) | 710 000 | 710 000 | 0 |
| Engagement de retraite (hors bilan) | 0 | 96 000 | + 96 000 |

*Provision pour impôts (0,75 pt).* Sous le régime de faveur, l'imposition des plus-values sur biens amortissables (réintégration étalée) et du profit sur les plants (inscrits fiscalement à leur valeur chez VERDOMÈNE) est reportée chez ARBORESSE : ces écarts entre valeur d'apport et valeur fiscale donnent un impôt différé passif ; l'engagement de retraite, déductible seulement à son versement, donne un impôt différé actif [V corrigé du sujet zéro, Q 2.4, F01 § 3.3 ; F02 § 6]. Rien sur les terrains ni sur le fonds commercial (hypothèses de l'annexe 2.3).

| Élément | Base | Impôt différé (25 %) |
|---|---:|---:|
| Serres et ombrières | 160 000 | 40 000 |
| Réseau d'irrigation et de brumisation | 40 000 | 10 000 |
| Plants et arbres en culture | 120 000 | 30 000 |
| Engagement de retraite | – 96 000 | – 24 000 |
| **Base nette : passif d'impôt différé** | **224 000** | **56 000** |

La provision de **56 000 €** est inscrite au compte **1523 Provisions pour impôts** [V F01 § 3.3].

*Fonds commercial et composition (0,5 pt)*

| | Montant |
|---|---:|
| Actifs identifiés | 2 200 000 |
| – Dettes | – 710 000 |
| – Provision pour engagements de retraite | – 96 000 |
| – Provision pour impôts | – 56 000 |
| **Actif net réel identifié** | **1 338 000** |
| Valeur globale retenue par le traité | 1 500 000 |
| **Fonds commercial** | **162 000** |

Contrôle : 1 090 000 (actif net comptable) + 400 000 – 96 000 – 56 000 = 1 338 000 €. L'écart positif entre la valeur globale et la somme des éléments identifiés est inscrit en **fonds commercial** (compte 207) [V art. 744-1, F01 § 3.1]. Composition de l'apport reçu par ARBORESSE : fonds commercial 162 000, terrains 260 000, serres et ombrières 520 000, irrigation 140 000, matériels 120 000, plants 760 000, clients 310 000, disponibilités 90 000 ; à déduire : provision pour retraites 96 000, provision pour impôts 56 000, emprunt 420 000, fournisseurs 150 000, dettes fiscales et sociales 140 000 ; apport net **1 500 000 €**, sans reprise des amortissements de VERDOMÈNE.

**c) Augmentations de capital et primes de scission (0,5 pt)**
- *CHARMILLÉE* : augmentation de capital 45 000 × 10 = **450 000 €** ; le nombre d'actions repose sur la valeur d'échange, mais la prime se calcule sur la **valeur d'apport comptable** [V art. 740-1 et 744-2, F01 § 1] : 740 000 – 450 000 = **290 000 €**, avant la reconstitution des dérogatoires et les frais (2.8).
- *ARBORESSE* : augmentation de capital 9 000 × 100 = **900 000 €** ; prime de scission = 1 500 000 – 900 000 – 60 000 (soulte) = **540 000 €**.

---

### 2.7 Écritures de base au 30 juin 2027 (4 pts)

**a) VERDOMÈNE (1,5 pt)**

VERDOMÈNE sort chaque branche pour ses valeurs comptables (valeurs brutes et amortissements) et constate une créance sur la bénéficiaire égale à la **valeur d'apport retenue au traité** (annexe 2.4).

**A1 — Transmission de la branche paysage à CHARMILLÉE (0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – CHARMILLÉE, compte d'apport | 740 000 | |
| 2818 Amortissements du matériel de transport | 310 000 | |
| 2815 Amortissements des engins et matériels | 390 000 | |
| 164 Emprunts auprès des établissements de crédit | 120 000 | |
| 401 Fournisseurs | 180 000 | |
| 43/44 Dettes fiscales et sociales (sans ventilation dans l'annexe) | 210 000 | |
| 2182 Matériel de transport | | 520 000 |
| 2154 Matériels industriels (engins et matériels) | | 680 000 |
| 31 Matières premières et fournitures | | 60 000 |
| 411 Clients (dont CHARMILLÉE : 27 600) | | 540 000 |
| 512 Banques | | 150 000 |
| **Total** | **1 950 000** | **1 950 000** |

**A2 — Transmission de la branche pépinière à ARBORESSE (0,5 pt : écriture 0,25 ; résultat de 410 000 € et son sort fiscal 0,25)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – ARBORESSE, compte d'apport | 1 500 000 | |
| 2813 Amortissements des constructions (serres et ombrières) | 540 000 | |
| 2815 Amortissements du réseau d'irrigation | 200 000 | |
| 2815 Amortissements des matériels de culture | 290 000 | |
| 164 Emprunts auprès des établissements de crédit | 420 000 | |
| 401 Fournisseurs | 150 000 | |
| 43/44 Dettes fiscales et sociales (sans ventilation dans l'annexe) | 140 000 | |
| 211 Terrains | | 180 000 |
| 2131 Bâtiments (serres et ombrières) | | 900 000 |
| 2151 Installations complexes spécialisées (irrigation) | | 300 000 |
| 2154 Matériels industriels (tracteurs et matériels de culture) | | 410 000 |
| 331 Produits en cours (plants et arbres) | | 640 000 |
| 411 Clients | | 310 000 |
| 512 Banques | | 90 000 |
| 778 Autres produits exceptionnels (résultat de scission) | | 410 000 |
| **Total** | **3 240 000** | **3 240 000** |

*Résultat de l'opération et sort fiscal.* Branche pépinière : 1 500 000 – 1 090 000 = **+ 410 000 €**, présenté en résultat exceptionnel (compte 778), la scission étant pour VERDOMÈNE un événement majeur et inhabituel [V PCG art. 513-5 ; hypothèse de l'annexe 2.4, F01 § 9]. Sous le régime de faveur, ce profit n'est **pas imposé** [V CGI art. 210 A-1, F02 § 2] : il est déduit extra-comptablement du résultat fiscal de la dernière période. L'engagement de retraite, transmis avec la branche, n'a pas à être comptabilisé chez VERDOMÈNE. Branche paysage : valeur d'apport égale à la valeur comptable, **aucun résultat**, bien que sa valeur d'échange dépasse de 700 000 € son actif net comptable.

**A3 — Réception des actions et de la soulte (0,25 pt).** Les actions, détenues seulement le temps de leur attribution, transitent par le compte 503 ; les actions ARBORESSE sont inscrites pour la valeur d'apport diminuée de la soulte : 1 500 000 – 60 000 = 1 440 000 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 503 Actions CHARMILLÉE (45 000 actions) | 740 000 | |
| 503 Actions ARBORESSE (9 000 actions) | 1 440 000 | |
| 512 Banques (soulte versée par ARBORESSE) | 60 000 | |
| 467 CHARMILLÉE, compte d'apport | | 740 000 |
| 467 ARBORESSE, compte d'apport | | 1 500 000 |

**A4 et A5 — Droits des actionnaires et attribution (0,5 pt).** Capitaux propres augmentés du résultat de scission : 1 830 000 + 410 000 = **2 240 000 €** = 740 000 + 1 440 000 + 60 000. Droits : FONTALBE Participations 70 % = 1 568 000 € (31 500 actions CHARMILLÉE pour 518 000, 6 300 actions ARBORESSE pour 1 008 000, soulte 42 000) ; M. MÉNAVRIL 16 % = 358 400 € (118 400 + 230 400 + 9 600) ; salariés 14 % = 313 600 € (103 600 + 201 600 + 8 400). Les amortissements dérogatoires sont soldés avec les autres capitaux propres.

A4 :

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 600 000 | |
| 1061 Réserve légale | 60 000 | |
| 1068 Autres réserves | 917 000 | |
| 120 Résultat de l'exercice (189 000 + 410 000) | 599 000 | |
| 145 Amortissements dérogatoires | 64 000 | |
| 456 Associés – FONTALBE Participations | | 1 568 000 |
| 456 Associés – M. MÉNAVRIL | | 358 400 |
| 456 Associés – salariés | | 313 600 |

A5 :

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – FONTALBE Participations | 1 568 000 | |
| 456 Associés – M. MÉNAVRIL | 358 400 | |
| 456 Associés – salariés | 313 600 | |
| 503 Actions CHARMILLÉE | | 740 000 |
| 503 Actions ARBORESSE | | 1 440 000 |
| 512 Banques (soulte) | | 60 000 |

Tous les comptes de VERDOMÈNE sont alors soldés.

**b) CHARMILLÉE (1 pt)**

**A6 — Augmentation de capital (0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (VERDOMÈNE) | 740 000 | |
| 101 Capital (45 000 × 10) | | 450 000 |
| 1042 Primes de fusion (prime de scission) | | 290 000 |

**A7 — Réalisation de l'apport à la valeur comptable (0,75 pt).** Valeurs brutes d'origine et amortissements repris [V F01 § 3.2] ; les dérogatoires ne figurent pas dans cette écriture (2.8). Barème : valeurs brutes et amortissements (0,5), dettes et compte d'apport (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 2182 Matériel de transport | 520 000 | |
| 2154 Matériels industriels (engins et matériels) | 680 000 | |
| 31 Matières premières et fournitures | 60 000 | |
| 411 Clients (dont créance sur CHARMILLÉE : 27 600) | 540 000 | |
| 512 Banques | 150 000 | |
| 2818 Amortissements du matériel de transport | | 310 000 |
| 2815 Amortissements des engins et matériels | | 390 000 |
| 164 Emprunts auprès des établissements de crédit | | 120 000 |
| 401 Fournisseurs | | 180 000 |
| 43/44 Dettes fiscales et sociales (sans ventilation dans l'annexe) | | 210 000 |
| 4561 Associés – Comptes d'apport en société (VERDOMÈNE) | | 740 000 |
| **Total** | **1 950 000** | **1 950 000** |

**c) ARBORESSE (1,5 pt)**

**A8 — Augmentation de capital et soulte due (0,5 pt).** La soulte fait partie de la rémunération de l'apport : elle diminue la prime [V F01 § 4 et § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (VERDOMÈNE) | 1 500 000 | |
| 101 Capital (9 000 × 100) | | 900 000 |
| 1042 Primes de fusion (1 500 000 – 900 000 – 60 000) | | 540 000 |
| 468 Divers comptes créditeurs – soulte à verser | | 60 000 |

**A9 — Réalisation de l'apport à la valeur réelle (0,75 pt).** Éléments à leur valeur réelle, sans amortissements repris ; engagement de retraite en provision 1521, impôt différé en 1523, fonds commercial en 207 [V art. 744-1, F01 § 3.1 et § 9]. Barème : actifs identifiés à la valeur réelle (0,25), provisions 1521 et 1523 (0,25), fonds commercial, dettes et compte d'apport (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 207 Fonds commercial | 162 000 | |
| 211 Terrains | 260 000 | |
| 2131 Bâtiments (serres et ombrières) | 520 000 | |
| 2151 Installations complexes spécialisées (irrigation) | 140 000 | |
| 2154 Matériels industriels (tracteurs et matériels de culture) | 120 000 | |
| 331 Produits en cours (plants et arbres) | 760 000 | |
| 411 Clients | 310 000 | |
| 512 Banques | 90 000 | |
| 1521 Provisions pour pensions et obligations similaires | | 96 000 |
| 1523 Provisions pour impôts | | 56 000 |
| 164 Emprunts auprès des établissements de crédit | | 420 000 |
| 401 Fournisseurs | | 150 000 |
| 43/44 Dettes fiscales et sociales (sans ventilation dans l'annexe) | | 140 000 |
| 4561 Associés – Comptes d'apport en société (VERDOMÈNE) | | 1 500 000 |
| **Total** | **2 362 000** | **2 362 000** |

**A10 — Versement de la soulte (0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 468 Divers comptes créditeurs – soulte à verser | 60 000 | |
| 512 Banques | | 60 000 |

---

### 2.8 Écritures complémentaires chez CHARMILLÉE (4 pts)

**A11 — Reconstitution des amortissements dérogatoires (1,5 pt).** *Justification (0,75).* Les amortissements dérogatoires de la branche paysage sont des provisions réglementées, comprises dans l'actif net apporté de 740 000 € (2.6 a) ; leur imposition reste différée parce que CHARMILLÉE s'engage à les reprendre à son passif et à les réintégrer comme VERDOMÈNE l'aurait fait [V CGI art. 210 A-3-a ; BOI-IS-FUS-30-20 § 10, F02 § 1 et § 2 ; annexe 2.4]. Ils sont **reconstitués par prélèvement sur la prime de scission** [V corrigé du sujet zéro, p. imprimée 217, F01 § 8] ; leur oubli est une erreur relevée par le jury (`JUR-R03`). La prime (290 000 €) suffit. *Écriture (0,75).*

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (prime de scission) | 64 000 | |
| 145 Amortissements dérogatoires (transport 24 000, engins 40 000) | | 64 000 |

Les dérogatoires de CHARMILLÉE passent de 70 000 € à 134 000 € ; ils continueront d'être dotés ou repris selon les plans fiscal et comptable des biens reçus, dont CHARMILLÉE reprend les valeurs d'origine.

**A12 — Frais de scission (1,25 pt).** *Calcul (0,75).* Les frais de scission peuvent être imputés sur la prime [V PCG art. 212-9, F01 § 7], pour leur montant net d'impôt [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 36 000 × 75 % = **27 000 €** ; l'économie d'impôt de 9 000 € diminue l'IS 2027 de CHARMILLÉE. Prime restante : 290 000 – 64 000 – 27 000 = **199 000 €**. *Écriture (0,5).*

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (36 000 × 75 %) | 27 000 | |
| 444 État – Impôts sur les bénéfices (36 000 × 25 %) | 9 000 | |
| 512 Banques | | 36 000 |

**A13 — Créance réciproque (1,25 pt).** *Justification (0,75).* La branche paysage comprend la créance de 27 600 € de VERDOMÈNE sur CHARMILLÉE, née de la sous-traitance du chantier ; CHARMILLÉE l'avait inscrite en fournisseurs. En recevant la branche, CHARMILLÉE devient **créancière d'elle-même** : la créance et la dette s'éteignent par **confusion** [V C. civ. art. 1349, F01 § 8]. La créance et la dette existent à la date d'effet de la scission, qui est aussi celle de sa réalisation : elles font partie des éléments transmis, puis s'éteignent. *Écriture (0,5).*

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette de CHARMILLÉE envers VERDOMÈNE) | 27 600 | |
| 411 Clients (créance reçue sur CHARMILLÉE) | | 27 600 |

---

### 2.9 Note à M. FONTALBE (2 pts)

**Capitaux propres juste après l'opération (0,75 pt)**

| Poste | CHARMILLÉE avant | CHARMILLÉE après | ARBORESSE avant | ARBORESSE après |
|---|---:|---:|---:|---:|
| Capital | 500 000 | 950 000 | 1 200 000 | 2 100 000 |
| Prime de scission | 0 | 199 000 | 0 | 540 000 |
| Réserve légale | 50 000 | 50 000 | 120 000 | 120 000 |
| Autres réserves | 560 000 | 560 000 | 330 000 | 330 000 |
| Amortissements dérogatoires | 70 000 | 134 000 | – | – |
| **Total** | **1 180 000** | **1 893 000** | **1 650 000** | **3 090 000** |

Contrôles : CHARMILLÉE + 713 000 = 740 000 (apport comptable) – 27 000 (frais nets) ; ARBORESSE + 1 440 000 = 1 500 000 (apport réel) – 60 000 (soulte), ses frais en charges n'étant pas traités. CHARMILLÉE reçoit sa branche sans réévaluation : ses capitaux propres par action baissent de 23,60 € à 19,93 €, alors que l'action vaut toujours environ 32 €. ARBORESSE inscrit la pépinière à sa valeur réelle, avec un fonds commercial de 162 000 €, présumé à durée d'utilisation non limitée et donc non amorti, mais à déprécier si sa valeur actuelle devient inférieure à sa valeur comptable [V PCG art. 214-3, F01 § 5.5].

**Place de FONTALBE Participations et de M. MÉNAVRIL (0,5 pt).** FONTALBE Participations passe de 60 % à **64,74 %** de CHARMILLÉE, dont elle renforce le contrôle, et détient **30 %** d'ARBORESSE, sans en avoir le contrôle : BRÉHALIER Développement garde la majorité (51,43 %). M. MÉNAVRIL détient 7,58 % de CHARMILLÉE et 6,86 % d'ARBORESSE ; il a reçu 9 600 € de soulte et pourra céder ses actions, aucun engagement de conservation ne pesant sur lui.

**Enjeux pour les parties prenantes (0,75 pt)**
- *Créanciers de chaque branche* : les dettes de la branche paysage (emprunt de 120 000 €, fournisseurs, administration fiscale et organismes sociaux, dont l'IS de 63 000 € de la période) sont reprises au passif de CHARMILLÉE, dont les capitaux propres atteignent 1 893 000 € et l'endettement bancaire total 210 000 € ; celles de la pépinière, dont l'emprunt de 420 000 €, au passif d'ARBORESSE, plus grande et plus solide que VERDOMÈNE. Ces créanciers changent de débiteur sans l'avoir choisi : la solidité de la société qui reprend leur créance devient leur premier enjeu.
- *Salariés de la pépinière* : les 22 salariés rejoignent ARBORESSE ; l'engagement d'indemnités de départ à la retraite qui les concerne (96 000 €) est repris dans l'apport et **provisionné** par ARBORESSE, dont la provision passe de 70 000 € à 166 000 € : leurs droits acquis chez VERDOMÈNE sont reconnus au passif de leur nouvel employeur, qui doit financer la modernisation des serres et de l'irrigation dont dépend leur emploi.
- *Banquier d'ARBORESSE* : les emprunts passent de 680 000 € à 1 100 000 €, mais les capitaux propres de 1 650 000 € à 3 090 000 € : l'endettement financier rapporté aux capitaux propres baisse de 41,21 % à 35,60 %. La trésorerie atteint 170 000 € après la soulte (140 000 + 90 000 – 60 000), et les plants inscrits à 760 000 € réduiront la marge dégagée à leur vente ; la provision pour impôts de 56 000 € sera reprise à mesure que les écarts se résorberont : réintégration des plus-values sur biens amortissables (18 667 € par an pendant cinq ans, puis 10 667 € par an, soit 4 667 € puis 2 667 € d'impôt par an), vente des plants (30 000 €) et versement des indemnités de départ (– 24 000 €).

Grille de niveaux pour les enjeux : 0 (absence ou idées sans lien avec le cas) ; 0,25 (une partie prenante, ou idées non chiffrées) ; 0,5 (deux parties prenantes, idées chiffrées) ; 0,75 (trois parties prenantes, idées chiffrées et reliées au cas).

---

### Réponses tolérées
- **2.1** : distinction présentée sans tableau, si elle couvre ce que reçoit la société, l'imposition et la situation des actionnaires ; renvoi du PCG non commenté, si la scission est définie correctement.
- **2.2** : effets du régime présentés sans les durées de réintégration ; engagement de conservation sur agrément décrit sans les seuils de 5 % et de 0,1 %.
- **2.3** : nombre d'actions calculé par la division de la valeur de la branche par la valeur unitaire (1 440 000 / 32 = 45 000) plutôt que par la parité ; parité exacte exprimée sous forme décimale (0,3125).
- **2.4** : plafond de la soulte vérifié par action VERDOMÈNE (2 € pour 3 €, puis 10 € pour 2,50 €) plutôt qu'en total ; équité vérifiée pour la seule branche pépinière (48 + 2 = 50 €) ; autre solution de remplacement réaliste proposée à M. MÉNAVRIL (rachat de ses actions par un associé, organisé dès la signature du traité), si elle reste distincte de la soulte.
- **2.5** : sens de l'apport à CHARMILLÉE non analysé, si le contrôle commun est établi au niveau de FONTALBE Participations et que la valeur comptable en est déduite.
- **2.6** : amortissements dérogatoires déduits de l'actif net apporté (676 000 €) et repris directement au crédit du compte 145 dans l'écriture A7, **sans** l'écriture A11 : la prime est alors de 676 000 – 450 000 = 226 000 €, soit le même montant qu'après A11 ; méthode acceptée si elle est cohérente dans tout le dossier [F01 § 8, réponse tolérée].
- **2.7** : compte 261, 50 ou 508 au lieu de 503 pour les actions reçues ; écritures A3 et A5 remplacées par une seule (débit 456, crédit 467), si le candidat indique que les bénéficiaires remettent les actions et la soulte directement aux actionnaires ; A4 qui solde d'abord le compte 778 vers le résultat ; compte 1043 Primes d'apport au lieu de 1042 ; A8 et A10 regroupées (soulte au crédit du 512) ; comptes 2135 ou 212 pour les serres ou l'irrigation, 355 pour les plants prêts à la vente, s'ils sont justifiés ; comptes 421, 431, 444 ou 447 au lieu de 43/44 ; compte 32 Autres approvisionnements au lieu de 31 pour les fournitures.
- **2.8** : créance éteinte directement dans A7 (fournisseurs de CHARMILLÉE diminués de 27 600 € et clients reçus pour 512 400 €), si la confusion est expliquée ; frais en deux écritures (1042 / 512 pour 36 000 €, puis 444 / 1042 pour 9 000 €).
- **2.9** : mention de la solidarité des sociétés bénéficiaires envers les créanciers de la société scindée, dans la limite de l'actif net que chacune reçoit, sauf stipulation contraire du traité : acceptée, sans être attendue. La logique du candidat prévaut lorsque ses montants découlent d'une erreur antérieure correctement reportée [`JUR-F08`].

### Erreurs fréquentes (rapports du jury)
- `JUR-R05` Difficulté à s'adapter : un seul mode d'évaluation pour toute la scission ; contrôle apprécié au niveau de la famille FONTALBE ou des personnes physiques plutôt que des holdings ; **nombre d'actions CHARMILLÉE calculé sur l'actif net comptable** (740 000 / 32 = 23 125 actions), qui spolierait les associés de VERDOMÈNE ; nombre d'actions calculé sur la valeur globale de VERDOMÈNE (2 940 000 €) au lieu de la valeur de chaque branche ; demande de M. MÉNAVRIL acceptée au motif que l'échange reste équitable.
- `JUR-R03` Reconstitution des amortissements dérogatoires oubliée : prime de CHARMILLÉE laissée à 263 000 € après frais au lieu de 199 000 €.
- `JUR-R01` Prime de scission mal calculée : prime de CHARMILLÉE calculée sur la valeur d'échange (1 440 000 – 450 000 = 990 000 €) ; prime d'ARBORESSE sans déduction de la soulte (600 000 €) ; frais imputés pour leur montant brut (prime finale de 190 000 €).
- `JUR-F07` Annexes mal exploitées : engagement de retraite oublié dans l'apport et dans l'impôt différé (provision pour impôts de 80 000 € et fonds commercial de 90 000 € au lieu de 162 000 €) ou dans le seul impôt différé (provision de 80 000 € et fonds commercial de 186 000 €) ; impôt différé calculé sur les terrains (provision de 76 000 €) ; plus-value sur les plants oubliée ; dérogatoires déduits de l'actif net apporté **et** reconstitués sur la prime ; créance réciproque de 27 600 € non éteinte.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1, A2, A7 et A9.
- Erreurs propres à ce cas :
  - résultat de scission constaté sur la branche paysage (actions CHARMILLÉE inscrites à leur valeur d'échange de 1 440 000 € et produit de 700 000 €), alors que la valeur d'apport est la valeur comptable ;
  - plafond de la soulte calculé sur la valeur de la branche (150 000 €) ou sur le nominal des actions VERDOMÈNE (60 000 €) au lieu du nominal des actions ARBORESSE attribuées ;
  - engagement de conservation des titres pendant trois ans présenté comme une condition de la scission de plein droit ;
  - provision pour retraites ajustée chez CHARMILLÉE, qui ne provisionne pas ses propres engagements ;
  - usage des comptes 675 et 775, supprimés du PCG 2026, pour le résultat de scission chez VERDOMÈNE.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 236-18, L. 236-19, L. 236-3 I ; PCG art. 710-1, 710-2, 720-1, 730-1 | Définition de la scission et renvoi daté du PCG ; transmission universelle et dissolution sans liquidation ; champ du titre VII ; initiatrice et cible | [V] Légifrance (texte relu le 27/11/2026) ; p. 81-82 | F01 § 1 et § 4 |
| PCG art. 740-1 ; guide pédagogique, compétence 1.2.a | Parité indépendante des règles d'évaluation des apports ; actions d'une scission déterminées par la valeur d'échange de chaque branche | [V] p. 82 ; [S] p. imprimée 163 | F01 § 1 ; `programme/perimetre_ue4.yaml` |
| PCG art. 741-1, 741-2, 742-1, 743-1 | Contrôle commun et contrôle distinct, appréciés au niveau des personnes morales ; apport à l'endroit ; valeur comptable (cas 1 et 2) et valeur réelle (cas 4) | [V] p. 82-84 | F01 § 2.1 à 2.3 |
| PCG art. 743-3, 744-2, 744-3 | Libération du capital ; valeur comptable ; ajustement de la provision pour retraites si la bénéficiaire provisionne ses engagements | [V] p. 85-86 | F01 § 2.4 et § 3.2 |
| PCG art. 744-1 ; comptes 207, 1521, 1523 | Éléments identifiés figurant ou non au bilan (engagements de retraite, impôts différés) ; fonds commercial | [V] p. 85, 134-135 | F01 § 3.1 |
| Corrigé du sujet zéro, Q 2.4 | Impôt différé net intégré à l'apport, y compris l'actif sur les engagements de retraite | [V] p. imprimée 216 | F01 § 3.3 |
| BOI-IS-FUS-10-20-40-20 § 170-180 | En valeur comptable, reprise des valeurs brutes et des amortissements | [V] | F01 § 3.2 |
| C. com. L. 236-18 al. 3 ; corrigé du sujet zéro (parité) | Soulte limitée à 10 % de la valeur nominale des actions attribuées ; équité de l'échange | [V] Légifrance ; p. imprimée 214 | F01 § 4 |
| PCG art. 214-8, 313-1 ; corrigé du sujet zéro, p. imprimée 217 ; rapport du jury 2025 | Dérogatoires = provisions réglementées en capitaux propres ; reconstitution par prélèvement sur la prime | [V] p. 24, 32 ; p. imprimée 217 | F01 § 8 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion de la créance et de la dette réciproques | [V] | F01 § 8 |
| PCG art. 513-5, 214-3 ; comptes 778 et 503 | Résultat exceptionnel (hypothèse de l'annexe 2.4) ; actions reçues avant attribution (convention de rédaction) ; fonds commercial non amorti | [V] p. 22-23, 42-43, 148 | F01 § 5.5 et § 9 |
| CGI art. 210 B-1, 210 B-3, 210 C-1, 210-0 A (I, 2°, et III) ; BOI-IS-FUS-20-30-10 § 10 et 70 ; BOI-IS-FUS-20-20 § 10, 60 et 80 | Scission de plein droit (branches complètes, sans engagement de conservation) ; agrément et conservation de trois ans à défaut ; soulte limitée ; motif économique ; application globale | [V] | F02 § 1 |
| CGI art. 210 A-1 et 210 A-3 ; BOI-IS-FUS-30-20 § 10, 20 et 30 ; BOI-IS-FUS-10-10-10 § 1 ; BOI-IS-FUS-10-20-30 § 210 et 330 | Plus-values non imposées chez la société scindée ; dérogatoires reconstitués ; engagements des bénéficiaires ; transferts de valeur ; droit commun ; imposition de la dernière période | [V] | F02 § 1, § 2 et § 4 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Démission d'un commissaire aux comptes : conditions, suite, opportunité | `3.1.b` Nomination et cessation | 2 |
| 3.2 Logiciel de suivi du linge, évaluation du parc, pressions du gérant | `3.1.c` Principes déontologiques | 1,5 |
| 3.3 Conditions d'exercice des commissaires aux comptes et des auditeurs de durabilité ; expert-comptable ; exigence du centre hospitalier | `3.1.a` Cadres d'exercice professionnel | 1,5 |
| 3.4 Norme sur les estimations comptables ; diligences ; élaboration et organisation des NEP | `3.1.d` Référentiel normatif (NEP) | 1,5 |
| 3.5 Objectif de l'audit, assurance raisonnable, écart d'attentes ; responsabilité civile envers la société | `3.2.a` Notion d'audit ; `3.1.e` Mise en cause de la responsabilité | 3 |
| 3.6 Droit de communication et refus d'accès aux données des puces | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.7 Risques et assertions des immobilisations ; procédures et recalculs | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit | 5 |
| 3.8 Anomalies, écritures, caractère significatif, opinion selon les corrections et en cas de limitation, structure du rapport | `3.2.e` Portée des opinions | 2 |
| 3.9 Commission européenne, EFRAG, GRI, ISSB ; interopérabilité ESRS-GRI ; réponse au groupe hôtelier | `3.3.a` Contexte et normes de durabilité | 2 |
| 3.10 Caractéristiques qualitatives de quatre informations ; périmètre et contrôle opérationnel | `3.3.b` Principes de construction du reporting | 3 |
| 3.11 Objectifs de la vérification ; assurance limitée et assurance raisonnable ; forme de la conclusion | `3.4.a` Objectifs de la mission et nature de l'assurance | 2 |
| 3.12 Étapes de la démarche ; procédures sur la consommation d'eau par kilogramme | `3.4.b` Démarche | 3 |
| 3.13 Avis de conformité après correction ; réserve en cas de refus | `3.4.c` Portée des avis | 2 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Démission envisagée (2 pts)

**Conditions de la démission (1 pt ; 0,25 pt par élément)**
- **Principe et motifs légitimes** : le commissaire aux comptes exerce sa mission jusqu'à son terme ; il peut démissionner pour un **motif légitime**, limitativement défini : cessation définitive d'activité ; motif personnel impérieux (santé) ; **difficultés rencontrées dans l'accomplissement de la mission auxquelles il n'est pas possible de remédier** ; survenance d'un **événement de nature à compromettre le respect des règles de la profession**, notamment l'indépendance ou l'objectivité [V code de déontologie art. 28 I]. Ici, les pressions (annexe 3.2) et le refus d'accès (annexe 3.5) relèvent des deux derniers motifs, s'ils ne peuvent être surmontés.
- **Interdictions** : il ne peut démissionner pour **se soustraire à l'émission de son opinion** sur les comptes (ou de son avis sur les informations de durabilité), ni **dans des conditions génératrices de préjudice** pour l'entité ; il doit pouvoir justifier qu'il a analysé la situation [V art. 28 II].
- **Justification et information** : il joint à son dossier les éléments qui justifient la démission et en **informe la H2A**, en indiquant ses motifs [V art. 28 I dernier al., IV] ; il expose aussi ses motifs au gérant [S].
- **Moment** : les textes ne fixent **aucun préavis** ; c'est l'interdiction de démissionner dans des conditions préjudiciables qui commande le moment : pas au cours des travaux de clôture, pas à quelques semaines de la décision des associés sur les comptes, ni pour éviter de signer un rapport défavorable [V art. 28 II ; S, application].

**Ce qui se passe ensuite (0,5 pt)**
- Le mandat est celui du **cabinet**, société de commissaires aux comptes pluripersonnelle : aucun suppléant n'a été désigné, ni n'était requis [V L. 821-40 I al. 3]. La SARL, qui dépasse toujours les trois seuils (13 380 000 € de bilan, 13 150 000 € de chiffre d'affaires, 118 salariés en 2026), reste tenue d'avoir un commissaire aux comptes : les associés en désignent un nouveau [V L. 223-35 al. 2 ; D. 223-27, renvoyant à D. 221-5].
- Le successeur **ne demeure en fonction que jusqu'à l'expiration du mandat de son prédécesseur**, soit jusqu'à la décision des associés qui statuera sur les comptes de **2029** (mandat de six exercices, 2024 à 2029, imposé par les seuils, sans faculté de le réduire à trois) [V L. 821-44 al. 1-2 ; L. 821-46]. Le cabinet démissionnaire lui donne accès à toutes les informations et à tous les documents pertinents [V L. 821-44 al. 3] ; le successeur prend contact avec lui avant d'accepter [S, F09 § 12].

**Opportunité de la démission (0,5 pt)**
- **Pas maintenant** : les travaux sur 2026 sont achevés aux trois quarts et les rapports sont prévus le 02/04/2027 ; démissionner « avant d'avoir à signer » reviendrait à se soustraire à l'émission de l'opinion, alors que des anomalies sont en discussion (question 3.8), et laisserait la SARL sans comptes certifiés pour la décision des associés de juin 2027 et sans vérification pour l'appel d'offres du centre hospitalier : conditions préjudiciables [V art. 28 II ; S].
- **Les difficultés peuvent être surmontées** : les demandes du gérant se refusent (question 3.2) ; l'accès aux données a été obtenu le 25/01/2027 ; la menace de mise en cause ne repose sur aucune faute (question 3.5). Si M. PERCHERAIS ne se sent plus en mesure d'exercer avec objectivité, le cabinet peut confier la signature à un autre associé inscrit et renforcer la revue de la mission [S, sauvegarde].
- Le cabinet achève donc la mission de 2026 et exprime son opinion ; si, ensuite, les pressions ou les obstacles persistent au point de rendre la mission impossible, il pourra démissionner pour motif légitime, à un moment qui laisse aux associés le temps de désigner un successeur, avec justification au dossier et information de la H2A [S].

**Réponses tolérées**
- La démission présentée comme une décision du cabinet, et non de M. PERCHERAIS, sans mention du changement de signataire : points complets si l'opportunité est correctement appréciée.

**Erreurs fréquentes**
- Admettre une démission pour « mauvaise relation » avec le gérant, sans examiner les motifs limitatifs ni le moment (`JUR-A05`).
- Faire remplacer le cabinet par un suppléant, ou donner au successeur un nouveau mandat de six exercices (`JUR-A01`).
- Décrire les formalités de la démission ou de la désignation du successeur, qui ne sont pas demandées (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 28 I, II, IV | Motifs légitimes ; interdictions ; justification ; information de la H2A | [V] ; moment : [S] | F09 § 3.7, § 12, § 19, § 26 |
| C. com. L. 821-40 I, L. 821-44, L. 821-46, L. 223-35, D. 223-27, D. 221-5 | Suppléant ; durée des fonctions du successeur ; accès au dossier ; seuils | [V] ; application : [S] | F09 § 3.3-3.5, § 18, § 19 |

### 3.2 Demandes du gérant et pressions (1,5 pt)

**Appréciation (0,75 pt ; 0,25 pt par point)**
- **Logiciel de suivi du linge** : concevoir et mettre en place le système qui calculerait les mises au rebut, les amortissements et la valeur du parc de linge, puis certifier des comptes qui en sont issus, c'est se prononcer sur des éléments résultant de ses propres prestations : **risque d'autorévision** [V code de déontologie art. 5 II, 19 I 2°]. Hors entité d'intérêt public, il est interdit de poursuivre la certification lorsqu'il existe un risque d'autorévision sans mesure de sauvegarde appropriée [V L. 821-28 IV] ; aucune sauvegarde interne au cabinet ne supprime le fait qu'il contrôlerait son propre système [S].
- **Évaluation du parc de linge au 31/12/2026** : le cabinet établirait lui-même un montant qu'il doit ensuite auditer (risque d'autorévision au plus haut degré) et se substituerait à la direction, qui est responsable de l'établissement des comptes ; la mission s'exerce **à l'exclusion de toute immixtion dans la gestion** [V L. 821-54 I ; art. 5 II ; S].
- **Pressions** : en liant la « suite de la collaboration » à sa réponse, le gérant fait peser sur le cabinet un **intérêt personnel** (conserver le mandat et ses honoraires) et une **pression** sur son jugement. Le commissaire aux comptes conserve une attitude impartiale, évite les situations qui l'exposent à des influences et maintient ses positions quelles que soient les pressions exercées [V code de déontologie art. 4 ; norme principes de comportement § 14, § 16]. La menace est d'ailleurs sans portée juridique : le mandat ne peut prendre fin avant son terme que par un relèvement judiciaire, pour faute ou empêchement [V L. 821-50].

**Mesures (0,75 pt)**
- **Refuser par écrit** les deux demandes, en expliquant qu'elles sont incompatibles avec la mission de certification ; la SARL peut confier le logiciel à un éditeur et l'évaluation du parc à son service comptable, au besoin renforcé, le cabinet auditant ensuite ces travaux [S].
- **Rappeler au gérant** que l'opinion ne dépend ni de la poursuite de la relation ni des honoraires ; **documenter** la situation à risque, l'analyse et les mesures prises [V norme risques et sauvegardes § 41-43 ; code de déontologie art. 19 I 4°].
- **Sauvegardes** si la pression persiste : revue indépendante des travaux sensibles (linge, durée d'utilisation) par un associé extérieur à la mission, saisine de la H2A pour avis en cas de doute sérieux ; si le cabinet ne pouvait plus justifier que son jugement n'est pas affecté, il mettrait fin à la mission (question 3.1) [V art. 5 III, 19 I 5° et II].

**Réponses tolérées**
- L'analyse des deux demandes sous le seul angle de l'autorévision, si la pression est traitée dans les mesures : 1,25 pt sur 1,5.

**Erreurs fréquentes**
- Accepter le logiciel au motif que la SARL n'est pas une entité d'intérêt public et qu'aucune liste de services interdits ne s'applique (`JUR-A03`).
- Énumérer impartialité, indépendance et intégrité sans les appliquer aux deux demandes (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-28 IV, L. 821-50, L. 821-54 I ; code de déontologie art. 4, 5, 19 | Autorévision hors EIP ; relèvement ; non-immixtion ; impartialité ; identification des risques | [V] ; application : [S] | F10 § 2, § 3, § 5, § 12, § 13, § 17, § 22 |
| Norme principes de comportement (A. 821-54) § 14, § 16 ; norme risques et sauvegardes (A. 821-55) § 41-43 | Pressions ; impartialité ; documentation | [V] | F10 § 12, § 22 |

### 3.3 Conditions d'exercice et exigence du centre hospitalier (1,5 pt)

**Commissaires aux comptes et auditeurs de durabilité (0,75 pt)**
- **Commissaire aux comptes** : profession exercée par des personnes ou des sociétés **inscrites sur la liste établie par la H2A** ; pour une personne physique, notamment, honorabilité, **stage professionnel** de trois ans et **certificat d'aptitude** aux fonctions de commissaire aux comptes ou diplôme d'expertise comptable ; formation continue obligatoire [V L. 821-13 I, L. 821-14, L. 821-24 ; R. 821-46]. Une société de commissaires aux comptes est contrôlée et dirigée par des commissaires aux comptes [V L. 821-16].
- **Certification des informations de durabilité** : un commissaire aux comptes inscrit sur une **liste distincte** tenue par la H2A, s'il a accompli **au moins huit mois** de stage sur des missions de durabilité et **réussi une épreuve** sur cette mission [V L. 821-13 II, L. 821-18] ; ou un **organisme tiers indépendant** accrédité par le comité français d'accréditation, au sein duquel exerce un **auditeur des informations en matière de durabilité**, personne physique inscrite sur la liste de la H2A (master, stage de huit mois, épreuve) [V L. 822-1, L. 822-3, L. 822-4].
- **Instances** : la **H2A** inscrit les professionnels, adopte les normes, définit le cadre des contrôles, enquête et sanctionne ; la **CNCC** représente la profession et concourt à son bon exercice ; les **CRCC** regroupent les commissaires aux comptes de chaque ressort de cour d'appel [V L. 820-1, L. 821-12].

**L'expert-comptable (0,25 pt)** : inscrit au **tableau de l'ordre** (diplôme d'expertise comptable), sous l'autorité des conseils régionaux et du conseil national de l'ordre ; il exerce des missions **contractuelles** (tenue, établissement, révision des comptes, conseil) [V ord. art. 1, 2, 3, 31, 33]. L'inscription au tableau ne vaut pas inscription sur les listes de la H2A : un expert-comptable qui n'est pas commissaire aux comptes inscrit sur la liste de durabilité, ou un bureau d'études qui n'est pas un organisme tiers indépendant accrédité, n'est pas habilité à certifier des informations en matière de durabilité [V L. 821-13, L. 822-3 ; F09 § 18 ; S, application à la question du gérant].

**Pourquoi le cabinet peut répondre à l'exigence (0,5 pt)** : MAYENVAL est une société inscrite sur la liste des commissaires aux comptes ; M. PERCHERAIS, associé, est inscrit sur la liste des commissaires aux comptes habilités à certifier les informations en matière de durabilité (annexe 3.1) ; la mission a été confiée par les associés et est conduite, par hypothèse, dans les conditions de la certification légale [V L. 821-13 II, L. 821-26 ; F12 § 11 (b)]. Il répond donc à l'exigence d'un « professionnel habilité », quoique la SARL ne soit pas tenue de publier ; son indépendance est appréciée selon le même code de déontologie (question 3.2) [V code de déontologie art. 1er II].

**Réponses tolérées**
- Une présentation des conditions d'exercice limitée aux listes de la H2A et aux conditions principales (stage, examen, épreuve de durabilité) : points complets si l'expert-comptable est correctement distingué.

**Erreurs fréquentes**
- Présenter l'ordre des experts-comptables comme l'instance des commissaires aux comptes ou des auditeurs de durabilité (`JUR-A01`).
- Admettre qu'un expert-comptable, du seul fait de son diplôme, peut certifier les informations de durabilité (`JUR-A01`).
- Détailler l'organisation des instances ou les formalités d'inscription, qui ne sont pas demandées (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 820-1, L. 821-12 à L. 821-14, L. 821-16, L. 821-18, L. 821-24, L. 821-26, R. 821-46, L. 822-1, L. 822-3, L. 822-4 | Listes ; conditions ; instances ; OTI et auditeurs de durabilité | [V] | F09 § 1, § 3.1-3.2, § 4, § 18 |
| Ord. 45-2138 art. 1, 2, 3, 31, 33 | Tableau de l'ordre ; missions de l'expert-comptable | [V] ; application : [S] | F09 § 2 |

### 3.4 La norme sur les estimations comptables (1,5 pt)

**Norme pertinente (0,25 pt)** : la NEP relative à l'**audit des estimations comptables et des informations y afférentes fournies dans l'annexe** (annexe 3.3). La durée d'utilisation du linge et la valeur actuelle de l'ancien tunnel ne peuvent être mesurées de façon précise : ce sont des estimations, établies par une méthode, des hypothèses et des données [§ 01]. Le passage de trois à quatre ans réduit la dotation de 2026 de **416 000 €** (question 3.7), alors que le résultat net de 486 000 € serait ramené à environ 174 000 € sans ce changement (486 000 − 416 000 × 0,75) : incertitude et subjectivité élevées, risque de **biais** de la direction [§ 01, § 03, § 07 ; S, application].

**Diligences (1 pt ; 0,25 pt par diligence appliquée au cas, dans la limite de 1 pt)**
- **Dénouement des estimations antérieures** [§ 08, § 14] : la durée de trois ans retenue jusqu'en 2025 s'est révélée trop courte : 20 % des pièces du lot 2022 étaient encore en circulation au 31/12/2026, à quatre ans et demi, et l'âge moyen de réforme est de 47 mois ; c'est l'information nouvelle qui justifie un **changement d'estimation**, appliqué de manière prospective, et non la correction d'une erreur [V PCG art. 122-5, 214-14].
- **Méthode, hypothèses et données** [§ 19, tirets 1 et 5] : le cabinet apprécie si la méthode est conforme au PCG (révision prospective, valeur nette comptable de chaque lot au 01/01/2026 répartie sur la durée restante, lots entièrement amortis non concernés) et si les **données** sont pertinentes et fiables : les âges de réforme viennent du fichier des puces, d'où la nécessité d'y accéder (question 3.6) ; il rapproche l'hypothèse sur le nouveau tunnel des données du fabricant.
- **Indices de biais** [§ 19, tiret 2 ; tiret 3, non reproduit ; § 27] : changement décidé l'année d'un fort investissement, qui maintient le résultat ; le cabinet vérifie la cohérence de l'hypothèse avec les autres usages qu'en fait la SARL (plan d'achats de linge, tarifs calculés sur la durée de rotation) et, en cas de doute, renforce ses procédures.
- **Calculs** [§ 19, tiret 7] : recalcul des dotations de chaque lot (question 3.7).
- **Ancien tunnel** : arrêté définitivement et destiné à la vente, il n'a plus de valeur d'usage ; l'estimation de la valeur actuelle (95 000 − 20 000 = **75 000 €**) et la dépréciation (190 000 − 75 000 = **115 000 €**) sont confirmées par un **événement postérieur à la clôture** : la vente du 12/02/2027 au prix de l'offre et le devis de démontage signé [§ 16, § 17 ; V PCG art. 214-15 à 214-17].
- **Annexe et conclusion** [§ 17, § 27] : mention et justification du changement de durée dans l'annexe [V PCG art. 831-2 3°] ; conclusion sur le caractère raisonnable des deux estimations ou sur l'existence d'une anomalie, et conséquences sur l'opinion si les éléments sont insuffisants.

**Élaboration et organisation des NEP (0,25 pt)** : les NEP sont élaborées par une commission placée auprès de la H2A, soumises pour avis à la CNCC, adoptées par la H2A et homologuées par arrêté du garde des sceaux ; elles forment un ensemble ordonné par thèmes : principes, acceptation et planification, évaluation des risques et réponses, éléments probants (dont les estimations), utilisation des travaux d'autres professionnels, rapports, puis normes propres à certaines entités et aux autres interventions [V L. 820-4, L. 820-23 ; F11 § 3.2-3.3 ; S, lecture par familles].

**Réponses tolérées**
- Des diligences présentées dans l'ordre de l'extrait, si elles sont appliquées aux deux estimations : points complets.

**Erreurs fréquentes**
- Citer la norme par son numéro sans l'appliquer au cas (`JUR-A06`).
- Qualifier l'allongement de la durée de correction d'erreur, ou l'appliquer aux exercices antérieurs (`JUR-A05`).
- Accepter la nouvelle durée sur la seule affirmation du gérant, sans examen des données ni des indices de biais (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP estimations § 01, 03, 07, 08, 14, 16, 17, 19, 27 | Estimations ; biais ; dénouement ; procédures ; conclusion | [V] ; application : [S] | F11 § 17.1, § 23.1 |
| PCG art. 122-5, 214-14 à 214-17, 831-2 ; C. com. L. 820-4, L. 820-23 | Changement d'estimation ; perte de valeur ; annexe ; élaboration des NEP | [V] | F11 § 3.2-3.3, § 16, § 31 |

### 3.5 Objectif de l'audit, écart d'attentes et responsabilité civile (3 pts)

**Objectif de l'audit et assurance raisonnable (0,75 pt)**
- Le commissaire aux comptes **certifie**, en justifiant de ses appréciations, que les comptes annuels sont **réguliers et sincères** et donnent une **image fidèle** du résultat, de la situation financière et du patrimoine ; il exprime pour cela une **opinion** après avoir mis en œuvre un audit [V L. 821-53 ; NEP principes § 01].
- Il obtient une **assurance raisonnable**, élevée mais non absolue, que les comptes **pris dans leur ensemble** ne comportent pas d'**anomalies significatives**, résultant d'erreurs ou de fraudes ; les limites de l'audit tiennent aux sondages, aux limites des procédures de l'entité et à des éléments qui conduisent davantage à des présomptions qu'à des certitudes [V NEP principes § 04, § 08-09]. Il prend en considération le risque de fraude, y compris de **détournement d'actifs**, mais le risque de non-détection est plus élevé en cas de fraude, dissimulée par nature [V NEP fraudes § 01, § 03-05].
- L'audit ne consiste **pas à garantir la viabilité ou la qualité de la gestion**, et la mission exclut toute immixtion dans la gestion [V L. 821-55, L. 821-54 I ; NEP principes § 02].

**Écart d'attentes (0,75 pt)** : c'est la différence entre ce que les utilisateurs des comptes, ou les dirigeants, attendent du commissaire aux comptes (une garantie qu'aucune perte, aucun vol, aucune erreur n'existe ; une surveillance continue des actifs ; un avis sur la gestion) et ce que la mission légale procure réellement (une opinion sur les comptes pris dans leur ensemble, fondée sur une assurance raisonnable et sur le seuil de signification) [S, notion doctrinale]. Le courriel du gérant en est un exemple : il confond la certification avec la protection du linge, qui relève des procédures que la SARL met en place et dont le gérant est responsable [S]. Le cabinet le réduit en expliquant sa mission dans la lettre de mission et dans le rapport, qui décrit les responsabilités de la direction et du commissaire aux comptes [V NEP rapport § 18 ; S].

**Conditions de la responsabilité civile envers la SARL (0,75 pt)**
- Le commissaire aux comptes est responsable, envers l'entité comme envers les tiers, des **conséquences dommageables des fautes et négligences** qu'il commet dans l'exercice de sa profession [V L. 821-37 al. 1].
- La SARL devrait prouver : une **faute** du cabinet, appréciée au regard de diligences normales conformes aux NEP (**obligation de moyens**, non de résultat) ; un **préjudice** certain ; un **lien de causalité** entre la faute et ce préjudice [S, droit commun ; F09 § 7.1].

**Appréciation (0,75 pt)**
- **Pas de faute apparente** : en 2025, les pièces non revues étaient peu nombreuses (2 100 pièces, 9 800 € de valeur nette, sorties de l'actif) ; le cabinet a relevé la faiblesse du suivi et **recommandé** un rapprochement mensuel le 04/04/2026 ; c'est l'audit de 2026, en cours, qui a mis les disparitions au jour, au moyen des données des puces.
- **Faute propre de la SARL** : le gérant n'a pas suivi la recommandation, a réduit l'équipe de suivi de trois personnes à une et a suspendu les sorties d'actif prévues par la procédure ; la protection des actifs relève de la direction, et cette faute exonère ou réduit fortement la responsabilité éventuelle du cabinet [S].
- **Préjudice et causalité** : la perte du linge résulte des disparitions chez deux établissements, dans l'entrepôt du transporteur et chez divers clients ; l'audit n'en est pas la cause et ne les aurait pas empêchées ; la SARL dispose d'abord de recours contre VELTRANSE Logistique, qui répond du linge pendant le transport et l'entreposage, et contre les clients [S, application]. La menace du gérant a donc peu de chances d'aboutir.

**Réponses tolérées**
- La responsabilité contractuelle de droit commun invoquée à la place du texte propre au commissaire aux comptes, si les trois conditions sont appliquées au cas : points complets.
- Une présentation de l'écart d'attentes sans le terme, si l'opposition entre attentes et assurance raisonnable est explicite : 0,5 pt sur 0,75.

**Erreurs fréquentes**
- Présenter l'audit comme une garantie de l'absence de fraude ou d'erreur, ou comme une obligation de résultat (`JUR-A01`).
- Retenir la responsabilité du cabinet du seul fait que des pertes existent, sans faute ni lien de causalité (`JUR-A05`).
- Traiter de la procédure de mise en cause, ou d'une responsabilité pénale, qui ne sont pas demandées (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-54 I, L. 821-55 ; NEP principes § 01-02, 04, 08-09 ; NEP fraudes § 01, 03-05 ; NEP rapport § 18 | Objectif ; assurance raisonnable ; fraude ; non-immixtion ; responsabilités dans le rapport | [V] ; écart d'attentes : [S] | F11 § 1.1, § 8.3, § 20.1 |
| C. com. L. 821-37 al. 1 | Responsabilité envers l'entité ; faute, préjudice, lien de causalité | [V] ; conditions et application : [S] | F09 § 7.1, § 20 ; F10 § 18 |

### 3.6 Droit de communication et refus d'accès (1,5 pt)

**Les moyens d'action en cause (0,75 pt)**
- **À toute époque**, le commissaire aux comptes opère toutes vérifications et tous contrôles qu'il juge opportuns et se fait communiquer **sur place toutes les pièces qu'il estime utiles** à sa mission, notamment contrats, livres, documents comptables et registres des procès-verbaux ; il peut se faire assister d'experts ou de collaborateurs nommément désignés, qui ont les mêmes droits [V L. 821-60].
- **Tout support** : les enregistrements et documents qu'il inspecte peuvent être sous forme papier, **sous forme électronique** ou sur d'autres supports [V NEP éléments probants § 10] ; une extraction d'un fichier informatique est une pièce comme une autre.
- C'est lui, et non le gérant, qui juge de l'**utilité** des pièces ; le secret ne peut lui être opposé, sauf par les auxiliaires de justice [V L. 821-61 al. 3], et il est lui-même tenu au **secret professionnel**, ce qui protège les données commerciales de la SARL [V L. 821-35 al. 1].

**Le refus du gérant (0,25 pt)** : le caractère « commercial » des données n'est pas un motif recevable : le fichier des puces est le seul document qui recense les pièces louées, leur lot et leurs mouvements ; le registre des immobilisations et l'état des lots, établis par la SARL, ne le remplacent pas [S, application]. Le cabinet a eu raison de rappeler ses droits par écrit et les conséquences du refus sur son rapport (annexe 3.5) ; un refus maintenu entraverait la mission, ce qui expose aussi le dirigeant à des sanctions pénales (non demandé) [V L. 821-6 3° ; S].

**Ce que le refus empêchait de vérifier (0,5 pt)**
- l'**existence** des 516 000 pièces inscrites à l'actif et l'identification des pièces non revues (anomalie 1, question 3.8) ;
- l'**évaluation** : âge des pièces par lot, recalcul des dotations, et surtout les données qui fondent la durée de quatre ans (âges de réforme, part du lot 2022 encore en circulation), estimation qui réduit la dotation de 416 000 € (question 3.4) ;
- les **droits** : distinction entre le linge de la SARL et les 21 400 pièces « propriété client » du centre hospitalier.
Maintenu, le refus aurait été une **limitation** des travaux, aux conséquences sur l'opinion (question 3.8).

**Réponses tolérées**
- L'absence de mention du secret professionnel, si le droit de communication et ses conséquences sont correctement présentés : 1,25 pt sur 1,5.

**Erreurs fréquentes**
- Admettre que le gérant choisit les documents communiqués, ou que le commissaire aux comptes doit se contenter de l'état des lots (`JUR-A05`).
- Développer la qualification et la procédure pénales, qui ne sont pas demandées (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-60, L. 821-61 al. 3, L. 821-35 al. 1, L. 821-6 3° | Droit de communication ; secret inopposable ; secret du commissaire aux comptes ; obstacle | [V] ; application : [S] | F09 § 5, § 21 ; F11 § 2, § 31 |
| NEP éléments probants § 10 | Documents sous forme électronique | [V] | F11 § 6.2, § 31 |

### 3.7 Immobilisations : risques et procédures (5 pts)

**a. Risques d'anomalies significatives et assertions (2 pts ; 0,25 pt par risque correctement relié à ses assertions, dans la limite de 2 pts)**

Facteurs de risque inhérent : immobilisations importantes (linge : 2 498 000 € de valeur nette au 31/12/2026 ; nouveau tunnel : 1 502 000 € inscrits) ; investissement non courant de l'exercice ; linge dispersé chez quelque 260 clients et chez un transporteur ; estimation à forte incidence (durée portée à quatre ans) ; instruction du gérant de ne plus sortir les pièces perdues ; intérêt du gérant à présenter un résultat favorable [V NEP risques § 02 ; NEP estimations § 01 ; S, application]. Si le cabinet ne teste pas l'efficacité des procédures de l'entité, le risque au niveau des assertions correspond au risque inhérent [V NEP risques § 41].

| Risque | Origine dans les annexes | Assertions |
|---|---|---|
| Pièces perdues ou disparues maintenues à l'actif | 25 200 pièces non revues depuis plus de six mois ; sorties suspendues | Existence |
| Pièces « propriété client » du centre hospitalier comptées dans le linge de la SARL | 21 400 pièces lavées dans sa blanchisserie | Droits et obligations |
| Coût d'entrée du tunnel surévalué (frais non incorporables, option sur la formation non respectée) ou sous-évalué | Tableau des coûts : formation, essais, inauguration, pièces de sécurité | Évaluation (et mesure de l'acquisition) |
| Date de mise en service et dotation du nouveau tunnel erronées | Réception le 01/04/2026, durée de 12 ans | Évaluation ; séparation des exercices (dotation) |
| Dotations du linge erronées : durée de quatre ans non justifiée (biais) ou mal appliquée (lots entièrement amortis, durée restante) | Changement d'estimation, dotation de 872 000 € | Évaluation |
| Ancien tunnel insuffisamment déprécié ou encore inscrit alors qu'il est cédé | Arrêt le 01/04/2026, offre, vente du 12/02/2027 | Évaluation ; existence |
| Achats de linge ou d'équipements de fin d'année mal rattachés, dettes envers les fournisseurs d'immobilisations omises | Lot 2026, paiements du tunnel | Exhaustivité ; séparation des exercices |
| Information insuffisante : changement de durée non justifié, sorties et mises au rebut absentes de l'état de l'actif immobilisé | Projet d'annexe | Présentation ; exhaustivité de l'information |

**b. Procédures en réponse (3 pts ; 0,25 pt par procédure reliée à son objectif, dans la limite de 2,25 pts, et 0,75 pt pour les recalculs)**
- **Rapprochement des factures** du fabricant, du transporteur et de l'installateur avec le registre des immobilisations, la commande et le contrat ; contrôle de la remise — *réalité, mesure, droits* [V NEP éléments probants § 10].
- **Analyse du coût d'entrée** élément par élément au regard du PCG et de l'option de la SARL : formation à exclure, essais avant réception à maintenir, inauguration en charges, pièces de sécurité immobilisables — *évaluation* [V PCG art. 213-8, 213-10 à 213-13, 213-21] ; elle révèle l'anomalie 2.
- **Inspection physique** du nouveau tunnel et de l'ancien, arrêté ; examen du procès-verbal de réception (date de mise en service) — *existence, point de départ de l'amortissement*.
- **Examen de la dépréciation de l'ancien tunnel** : offre du 20/11/2026, acte de vente du 12/02/2027, devis de démontage — *évaluation* (question 3.4).
- **Rapprochement du fichier des puces avec l'état des lots** et le registre (nombre de pièces par lot, exclusion des pièces « propriété client ») — *existence, exhaustivité, droits*.
- **Analyse des pièces non revues** depuis plus de six mois, par lot et par client, et **sondages** : bons de livraison, relevés de lecture, réclamations — *existence* ; elle révèle l'anomalie 1.
- **Contrôle de la durée de quatre ans** : âges de réforme du fichier, dénouement de l'estimation antérieure, données du fabricant (question 3.4) — *évaluation*.
- **Examen des achats de linge de décembre 2026 et des factures de janvier 2027** — *exhaustivité, séparation des exercices*.
- **Lecture du projet d'annexe** (changement d'estimation, état de l'actif immobilisé avec les sorties) et **déclarations écrites** du gérant sur les pièces perdues et les estimations — *présentation* [V PCG art. 831-2, 832-2].

*Recalculs (0,75 pt)*
- **Coût d'entrée du nouveau tunnel** : 1 420 000 − 71 000 + 26 000 + 58 000 + 9 000 + 22 000 = **1 464 000 €** (et non 1 502 000 €) ; dotation de 2026 : 1 464 000 / 12 × 9 / 12 = **91 500 €** (et non 93 875 € ; écart de 2 375 €).
- **Dotation de 2026 du linge sur quatre ans** : lot 2022 entièrement amorti : 0 ; lot 2023 : (1 080 000 − 900 000) / 1,5 = **120 000 €** ; lot 2024 : (1 260 000 − 630 000) / 2,5 = **252 000 €** ; lot 2025 : (1 344 000 − 224 000) / 3,5 = **320 000 €** ; lot 2026 : 1 440 000 / 4 × 6 / 12 = **180 000 €** ; total **872 000 €**, conforme au projet.
- **Effet du changement** (non exigé du candidat ; il éclaire les questions 3.4 et 3.6) : sur trois ans, la dotation aurait été de 180 000 + 420 000 + 448 000 + 240 000 = **1 288 000 €** ; le changement réduit la dotation de **416 000 €**.

**Réponses tolérées**
- En a. et b., d'autres risques ou procédures tirés des annexes, correctement reliés à des assertions ou à des objectifs (par exemple, procédure analytique du nombre de pièces achetées et réformées, demande d'information au transporteur sur les pièces entreposées).
- Un recalcul de la dotation de 2026 limité aux lots 2023 à 2025, si la méthode prospective est correctement appliquée : 0,5 pt sur 0,75.

**Erreurs fréquentes**
- Confondre réalité (flux) et existence (soldes), ou citer des assertions sans les relier à un risque (`JUR-A01`).
- Proposer un inventaire physique du linge au seul siège, alors qu'il est chez les clients et chez le transporteur (`JUR-A06`).
- Appliquer la nouvelle durée depuis l'origine de chaque lot, ou amortir à nouveau le lot 2022 (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP risques § 02, § 41 ; NEP éléments probants § 9-10 ; NEP estimations | Facteurs de risque ; assertions ; techniques | [V] | F11 § 4.1, § 4.3, § 6, § 17.1 |
| PCG art. 122-5, 213-8, 213-10 à 213-13, 213-21, 214-12 à 214-17, 831-2, 832-2 | Coût d'entrée ; pièces de rechange ; amortissement ; changement d'estimation ; dépréciation ; annexe | [V] ; application : [S] | F11 § 16, § 31 |

### 3.8 Anomalies, écritures et opinion (2 pts)

**Anomalies et caractère significatif (0,75 pt)**
- **Anomalie 1 — pièces non revues** : valeur nette des pièces au 31/12/2026, au prorata de chaque lot :

| Lot | Pièces | Valeur brute | Amortissements au 31/12/2026 | Valeur nette |
|---|---:|---:|---:|---:|
| 2023 | 6 000 | 54 000 | 51 000 | 3 000 |
| 2024 | 7 200 | 72 000 | 50 400 | 21 600 |
| 2025 | 8 000 | 84 000 | 34 000 | 50 000 |
| 2026 | 4 000 | 48 000 | 6 000 | 42 000 |
| **Total** | **25 200** | **258 000** | **141 400** | **116 600** |

  (Valeur nette par pièce : 0,50 € ; 3,00 € ; 6,25 € ; 10,50 €.) **116 600 €**, soit **1,67 fois** le seuil de signification (70 000 €) : **significative**. L'argument du gérant ne tient pas : selon la procédure de la SARL, ces pièces sont réputées perdues ; leur disparition est établie ; la SARL n'en a plus la disposition. Les réclamations sont des créances éventuelles, à ne pas compenser avec la sortie des pièces [V NEP caractère significatif § 9 ; S, application].
- **Anomalie 2 — formation** : 38 000 € immobilisés à tort, moins la dotation correspondante de 2 375 € : résultat surévalué de **35 625 €** ; **0,51 fois** le seuil : non significative seule, mais supérieure au seuil des anomalies manifestement insignifiantes (3 500 €), donc récapitulée [V NEP anomalies § 8, § 14]. Ensemble : **152 225 €**, soit **2,17 fois** le seuil.

**Écritures de correction au 31/12/2026 (0,5 pt)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 2815 | Amortissements des installations, matériel et outillage industriels | 141 400 | |
| | 657 | Valeurs comptables des immobilisations incorporelles et corporelles cédées | 116 600 | |
| | 2154 | Matériels industriels | | 258 000 |

Libellé : sortie de l'actif de 25 200 pièces de linge non revues depuis plus de six mois (écriture X1, équilibrée à 258 000 €).

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 6228 | Divers (rémunérations d'intermédiaires et honoraires) | 38 000 | |
| | 2815 | Amortissements des installations, matériel et outillage industriels | 2 375 | |
| | 2151 | Installations complexes spécialisées | | 38 000 |
| | 68112 | Dotations aux amortissements des immobilisations corporelles | | 2 375 |

Libellé : frais de formation des opérateurs portés en charges et dotation correspondante annulée, 38 000 / 12 × 9 / 12 (écriture X2, équilibrée à 40 375 €). Les écritures sont présentées sans leur incidence sur l'impôt, comme le demande l'énoncé.

**Opinion selon les décisions de la SARL (0,5 pt)**
- **Position du gérant (X2 passée, X1 refusée)** : anomalie significative non corrigée de 116 600 € ; ses incidences sont **clairement circonscrites** (le linge à l'actif et le résultat, pour un montant chiffré) et une réserve qui les quantifie suffit à l'utilisateur : **certification avec réserve pour désaccord** [V NEP rapport § 09-10]. Un refus de certifier ne se justifie pas : l'anomalie ne touche pas l'ensemble des comptes [V NEP rapport § 12 ; S].
- **Les deux anomalies corrigées** : **certification sans réserve** [V NEP rapport § 08].

**Refus d'accès maintenu et structure du rapport (0,25 pt)**
- Sans les données des puces, le cabinet n'aurait pu vérifier ni l'existence des pièces ni les données qui fondent la durée de quatre ans : **limitation**. Ses incidences portant sur des postes identifiés (linge à l'actif, dotation de 872 000 €), la réserve pour **limitation** aurait été possible si elle suffisait à l'utilisateur ; sinon, compte tenu de l'importance du linge dans l'actif et dans le résultat, **impossibilité de certifier** [V NEP rapport § 11, § 14 ; NEP estimations § 27]. Le cabinet n'aurait pas détecté l'anomalie 1.
- Structure : opinion ; fondement de l'opinion (avec le motif de la réserve) ; justification des appréciations (dont la durée d'utilisation du linge) ; vérifications du rapport de gestion et des documents adressés aux associés ; responsabilités de la gérance et du commissaire aux comptes ; date et signature [V NEP rapport § 18 ; R. 821-180].

**Réponses tolérées**
- Le compte 6228 remplacé par un autre compte de services extérieurs adapté (604, 6185), si le libellé est clair : points complets.
- En cas de limitation, la réserve ou l'impossibilité retenue avec une justification fondée sur la circonscription des incidences : points complets.
- Le cas où aucune anomalie n'est corrigée, traité en plus (réserve pour désaccord sur 152 225 €) : sans points supplémentaires.

**Erreurs fréquentes**
- Laisser les pièces à l'actif en attendant les réponses aux réclamations, ou les déprécier au lieu de les sortir (`JUR-A05`).
- Écriture sans libellé ou sans numéro de compte, ou passée sur un compte supprimé du PCG 2026 (`JUR-F03`).
- Confondre la réserve pour désaccord et la réserve pour limitation (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Liste des comptes ; PCG art. 213-8 | Comptes 2151, 2154, 2815, 657, 6228, 68112 ; option sur la formation | [V] | F11 § 16, § 31 |
| NEP caractère significatif § 9 ; NEP anomalies § 8, 14 ; NEP rapport § 08-14, 18 ; R. 821-180 | Caractère significatif ; opinions ; structure du rapport | [V] ; qualification : [S] | F11 § 4.2, § 8, § 14.1 |

---

### Partie B – Durabilité (12 points)

La SARL peut s'inspirer de l'une ou l'autre version des ESRS ; le corrigé s'appuie sur ESRS 1 (2026), dont les solutions retenues ici sont aussi celles de 2023 [S].

### 3.9 Acteurs, interopérabilité et demande du groupe hôtelier (2 pts)

**Acteurs et normes (0,75 pt ; 0,25 pt par acteur)**
- **Commission européenne et EFRAG** : l'EFRAG, conseiller technique de la Commission, prépare les projets d'**ESRS**, que la Commission adopte par actes délégués [V règlement 2026/1563, considérant 3]. Les ESRS reposent sur la **double matérialité** : matérialité d'**impact** (impacts de l'entreprise sur les personnes et l'environnement) et matérialité **financière** [V ESRS 1 (2026) § 35].
- **GRI** (Global Reporting Initiative) : organisme international indépendant dont les normes (normes universelles, sectorielles et thématiques) portent sur les **impacts** de l'organisation sur l'économie, l'environnement et les personnes ; elles s'adressent à toutes les parties prenantes [S F12 § 1].
- **ISSB** : créé au sein de la Fondation IFRS, il publie les normes **IFRS S1** (exigences générales) et **IFRS S2** (climat), qui retiennent une approche **financière**, destinée aux investisseurs [S F12 § 1].

**Interopérabilité ESRS-GRI (0,5 pt)** : la déclaration commune de l'EFRAG et de la GRI (fin août / début septembre 2023) indique que les définitions, concepts et informations relatifs aux **impacts** sont pleinement ou étroitement alignés, et qu'une entité qui publie selon les ESRS est considérée comme publiant **« with reference to »** (en se référant aux) normes de la GRI, ce qui lui évite une double publication ; un index d'interopérabilité établi par les deux organismes (novembre 2024) relie les informations de la GRI aux points de données des ESRS [V page de la GRI, publiée le 05/09/2023, consultée le 27/11/2026 ; S pour l'index]. Les ESRS admettent en outre des informations supplémentaires issues d'autres référentiels, « comme la Global Reporting Initiative », signalées comme ne résultant pas de l'évaluation de la matérialité [V ESRS 1 (2026) § 107-109].

**Réponse au groupe hôtelier (0,75 pt)**
- La SARL n'établit pas deux documents : ses informations selon les ESRS lui permettent de se déclarer établies **en se référant aux normes de la GRI** ; elle y joint un **index de contenu** (table de correspondance) qui renvoie, pour chaque information de la GRI, à l'endroit de ses informations où elle figure [S].
- Si le groupe hôtelier demande des informations propres à la GRI que ses informations ne contiennent pas, elle peut les ajouter, **clairement identifiées** par la référence à la GRI [V ESRS 1 (2026) § 107-109].
- Elle ne peut déclarer un rapport **conforme** aux normes de la GRI (« in accordance with ») que si elle en respecte toutes les exigences ; c'est à apprécier avec le groupe hôtelier [S, GRI 1].

**Réponses tolérées**
- La formule « GRI = impact, ISSB = financier, ESRS = double matérialité » comme présentation des perspectives : points complets pour les acteurs si les normes de chacun sont citées.

**Erreurs fréquentes**
- Présenter la GRI comme un organisme européen, ou l'ISSB comme fondé sur la double matérialité (`JUR-A01`).
- Conseiller d'établir un second rapport selon la GRI, sans examiner l'interopérabilité (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règlement 2026/1563 consid. 3 ; ESRS 1 (2026) § 35, 107-109 | EFRAG ; double matérialité ; informations supplémentaires | [V] ; application : [S] | F12 § 1, § 17, § 26 |
| Déclaration commune EFRAG-GRI (2023) ; index d'interopérabilité (11/2024) ; pages ISSB ; GRI 1 | Interopérabilité ; « with reference to » ; IFRS S1-S2 | [V] déclaration ; [S] index, ISSB, GRI 1 | F12 § 1, § 27 |

### 3.10 Caractéristiques qualitatives et périmètre (3 pts)

**Les quatre informations (2 pts ; 0,5 pt par information, dont 0,25 pt pour la caractéristique en cause et 0,25 pt pour son application)** : une information utile est **pertinente**, c'est-à-dire susceptible d'influer sur les décisions des utilisateurs ; elle donne une **représentation fidèle** (complète, neutre, exacte), elle est **comparable**, **vérifiable** et **compréhensible** [V ESRS 1 (2026) § 19-20 ; appendice B, QC1 à QC20]. Les quatre thèmes sont pertinents pour les clients hospitaliers, qui en tiennent compte dans leurs appels d'offres [V QC1-QC2 ; S].

| Information | Appréciation |
|---|---|
| Eau : 6,5 L/kg, – 37,5 % | **Non complète** et **non neutre** : elle exclut la blanchisserie du centre hospitalier (12 600 m³ sur 39 900 m³ en 2026, soit 31,6 % de l'eau), dont les machines de 2009 consomment 12,0 L/kg, et met en avant le seul site qui s'est amélioré [V QC5-QC7]. Comparaison 2025-2026 cohérente pour Évron, mais trompeuse sur l'ensemble de l'activité [V QC10-QC12 ; S]. |
| Énergie : 1,05 kWh/kg | **Exactitude** : l'estimation du gaz de décembre doit être signalée comme telle, avec sa méthode et ses limites [V QC9 c) ; ESRS 1 (2026) § 88] ; **vérifiabilité** : la méthode de calcul doit être fournie [V QC14 b)] ; même omission de la blanchisserie du centre hospitalier que pour l'eau. |
| Lessives : – 9 % par kg | **Non neutre** et **non complète** : elle présente l'aspect favorable et tait la hausse de 35 % des produits de désinfection chlorés, plus préoccupants ; la neutralité exige d'équilibrer aspects favorables et défavorables, sans compensation [V QC6-QC8]. |
| Accidents : taux de fréquence 21 contre 46 | **Non compréhensible** (taux non défini, unité absente) et **non comparable** : les deux taux ne sont pas calculés sur la même base ; recalculé sur la même base, celui de 2025 serait de 29 [V QC10-QC12, QC16, QC20]. Il couvre les quatorze salariés de la blanchisserie du centre hospitalier, que les informations environnementales excluent : périmètre **incohérent** entre les informations [V QC11, QC19]. |

**Périmètre : la blanchisserie du centre hospitalier (1 pt)**
- **Règles (0,5 pt)** : l'état de durabilité porte sur la même entreprise déclarante que les états financiers, ici la SARL, sans filiale [V ESRS 1 (2026) § 60]. Le **contrôle opérationnel** est la possibilité de diriger les activités opérationnelles d'une entité, d'un site, d'une activité ou d'un actif [V ESRS (2023), annexe II]. Pour un actif loué, les impacts de son **utilisation** relèvent des activités propres de celui qui l'utilise (l'énergie et l'eau d'une usine louée sont attribuées au preneur), ceux de sa **propriété** étant répartis selon le contrat [V ESRS 1 (2026) § 71, § 73, AR 39]. La propriété n'est donc pas le critère.
- **Application (0,5 pt)** : la SARL exploite la blanchisserie avec ses salariés, fixe les horaires et les programmes de lavage, achète les lessives et assure l'entretien courant ; l'eau et l'énergie consommées lui sont refacturées au coût réel. Elle en a le **contrôle opérationnel** : les impacts de l'utilisation (eau, énergie, lessives, santé et sécurité de ses salariés) relèvent de ses **propres activités**, alors même que les locaux, les machines et le linge appartiennent au centre hospitalier [S, application de § 71 et AR 39 par analogie : la SARL n'est pas preneuse]. Seuls les impacts liés à la propriété (renouvellement des machines, état des locaux) relèvent, selon le contrat, du centre hospitalier ; la SARL peut les décrire. La blanchisserie **entre dans le périmètre**.

**Réponses tolérées**
- Une autre caractéristique retenue pour une information, si elle est justifiée par les faits de l'annexe (par exemple, vérifiabilité de la donnée sur l'eau, faute de description du périmètre) : points complets.
- Le raisonnement fondé sur le seul contrôle opérationnel, sans la règle des actifs loués, si la conclusion est motivée par les clauses du contrat : points complets.

**Erreurs fréquentes**
- Exclure la blanchisserie au motif que le centre hospitalier possède les murs et les machines (`JUR-A01`).
- Recalculer les données ou proposer d'autres indicateurs, ce qui n'est pas demandé (`JUR-A05`).
- Détailler les exigences d'une norme thématique (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 19-20, § 88, appendice B (QC1 à QC20) | Caractéristiques qualitatives ; estimations | [V] ; application : [S] | F12 § 17, § 24, § 27 |
| ESRS 1 (2026) § 60, § 71, § 73, AR 39 ; ESRS (2023), annexe II | Entreprise déclarante ; actifs utilisés ; contrôle opérationnel | [V] ; application : [S] | F12 § 7, § 14, § 27 |

### 3.11 Objectifs de la vérification et nature de l'assurance (2 pts)

**Objectifs (0,75 pt)** : exprimer, dans un rapport destiné aux associés, un **avis** sur la conformité aux ESRS du **processus** mis en œuvre par la SARL pour déterminer les informations publiées (analyse de double matérialité) et sur la conformité des **informations** publiées [V L. 821-54 II, par analogie ; LD 2026 § 2]. La SARL publiant volontairement, la mission repose sur la décision des associés et sur la lettre de mission, qui en fixent l'étendue (ni taxonomie, ni balisage, ni consultation des représentants du personnel) ; elle est conduite, par hypothèse, dans les conditions de la certification légale [F12 § 11 (b)]. Elle donne au centre hospitalier et aux autres utilisateurs une confiance accrue dans les informations, sans garantir la performance environnementale ni la qualité de la gestion [V L. 821-55].

**Assurance limitée et assurance raisonnable (0,75 pt)**
- Pour **certifier les comptes**, le cabinet obtient une **assurance raisonnable**, élevée mais non absolue, que les comptes pris dans leur ensemble ne comportent pas d'anomalies significatives [V NEP principes § 08].
- Pour les informations de durabilité, l'**assurance est limitée** : les vérifications sont moindres en **nature**, en **étendue** et en **durée** [V LD 2026, « Niveau d'assurance » ; F13 § 2.3] ; les travaux détaillés portent sur des informations sélectionnées (vérifiées spécifiquement) [V LD 2026 § 8.3.1] et font une large place aux demandes d'informations et aux procédures analytiques [S]. Le même cabinet peut ainsi aller plus loin sur les comptes que sur les informations de durabilité, alors même qu'il les rapproche (question 3.12).

**Forme de la conclusion (0,5 pt)** : sur les comptes, une opinion **positive** (le cabinet certifie que les comptes sont réguliers et sincères et donnent une image fidèle) ; sur les informations de durabilité, une conclusion **négative**, axe par axe (le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes concernant la conformité du processus, puis des informations, aux ESRS) [V L. 821-53 ; LD 2026 § 17, annexe 2 ; F13 § 4.2].

**Réponses tolérées**
- Une comparaison limitée à « assurance raisonnable, opinion positive / assurance limitée, conclusion négative », si l'étendue moindre des travaux est mentionnée : 1 pt sur 1,25 pour l'assurance et la forme.

**Erreurs fréquentes**
- Présenter l'assurance limitée comme une garantie, ou comme identique à celle de la certification des comptes (`JUR-A01`).
- Développer les axes de la taxonomie et du balisage, sans objet ici (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-54 II, L. 821-55 ; NEP principes § 08 | Opinion sur les comptes ; objet de l'avis ; absence de garantie ; assurance raisonnable | [V] ; application à une mission volontaire : [S] | F11 § 1.1 ; F12 § 11 ; F13 § 2.1 |
| LD 2026 § 2, § 8.3, § 17, « Niveau d'assurance », annexe 2 | Axes ; assurance limitée ; forme négative | [V] | F13 § 2.2-2.3, § 4 |

### 3.12 Démarche et procédures sur la consommation d'eau (3 pts)

**Étapes de la démarche (1 pt)** : **lettre de mission** (objet, axes, signataire inscrit sur la liste de la durabilité, accès aux personnes et aux documents, déclarations écrites, honoraires) ; **prise de connaissance** de la SARL, de ses deux sites, de sa chaîne de valeur et de la production des informations ; **planification**, avec la sélection des informations **vérifiées spécifiquement** : la consommation d'eau par kilogramme, attendue par le centre hospitalier et exposée à un risque (deux sites, sous-compteurs, refacturations, pesées) ; **contrôle du processus** (analyse de double matérialité) ; **contrôle des informations** (base de préparation et périmètre, présentation, informations sélectionnées) ; **lecture d'ensemble** et **cohérence avec les comptes annuels**, en échange avec l'équipe qui les certifie ; événements postérieurs, déclarations écrites, communication avec le gérant ; **rapport** organisé par axe [V LD 2026 § 3-8, § 11-17 ; F13 § 3].

**Procédures sur la consommation d'eau par kilogramme (2 pts ; 0,25 pt par procédure reliée à son objectif, dans la limite de 2 pts)**
- **Rapprochement du périmètre** retenu avec la liste des sites exploités et les contrats : la blanchisserie du centre hospitalier est absente — *exhaustivité, conformité du périmètre* [V LD 2026 § 8.1].
- **Rapprochement des volumes d'eau** d'Évron avec les relevés mensuels du compteur général et les factures du service des eaux (index du 01/01 et du 31/12) — *exactitude, séparation des périodes*.
- **Rapprochement des volumes** de la blanchisserie du centre hospitalier avec le sous-compteur et les refacturations du centre hospitalier — *exhaustivité, exactitude*.
- **Contrôle des tonnages** : pesées des chariots à la réception et à l'entrée de la blanchisserie, rapprochées des factures au kilogramme et des bons de livraison — *exactitude du dénominateur*.
- **Observation physique** des compteurs et sous-compteurs, de leur relevé et de leur étalonnage — *fiabilité des données*.
- **Procédures analytiques** : consommation mensuelle par tunnel et par site rapprochée des tonnages ; ratio du nouveau tunnel comparé aux données du fabricant et à celui de 2025 (10,4 L/kg) ; ratio de la blanchisserie du centre hospitalier (12,0 L/kg) — *vraisemblance, cohérence* [V LD 2026 § 8.3.2].
- **Recalcul** du ratio publié et de sa variation, par site et au total — *exactitude*.
- **Cohérence avec les comptes** : charges d'eau du compte 6061 et refacturations du centre hospitalier rapprochées des volumes — *connectivité* [V ESRS 1 (2026) § 116 ; LD 2026 § 11].
- **Lecture de la base de préparation** et de la description de l'information (périmètre, définition du kilogramme lavé, méthode) — *présentation, compréhensibilité*.

**Réponses tolérées**
- Les étapes dans l'ordre du programme (prise de connaissance, planification, contrôle du processus et des informations, contrôle du balisage et des exigences de publication, rapport), si le candidat signale que le balisage et la taxonomie sont sans objet : points complets.

**Erreurs fréquentes**
- Proposer des procédures sans lien avec la donnée ou sans objectif (`JUR-A06`).
- Limiter les travaux aux factures d'Évron, sans examiner le périmètre (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 3-8, § 8.1, § 8.3, § 11-17 | Étapes ; périmètre ; informations vérifiées spécifiquement ; techniques ; lecture d'ensemble | [V] ; procédures : [S] | F13 § 3, § 7 |
| ESRS 1 (2026) § 116 | Cohérence avec les états financiers | [V] | F12 § 9 |

### 3.13 Avis sur les informations (2 pts)

**Après la correction : avis de conformité (1 pt)**
- **La correction suffit** : la SARL ne s'est pas bornée à corriger le ratio d'eau. Elle intègre la blanchisserie du centre hospitalier dans **toutes** les informations environnementales concernées (eau, énergie, lessives), pour 2026 et pour 2025, ce qui rend la comparaison cohérente (7,6 L/kg contre 10,8 L/kg, – 29,6 %) ; elle décrit le périmètre dans sa **base de préparation** ; le périmètre des informations environnementales devient cohérent avec celui des accidents du travail. Elle a aussi signalé l'estimation du gaz, mentionné les produits de désinfection et défini le taux de fréquence [V ESRS 1 (2026) § 88, QC6-QC12 ; LD 2026 § 8.1 ; S, appréciation]. Une correction limitée à l'eau aurait laissé subsister l'omission pour l'énergie et les lessives.
- Les autres travaux n'ont relevé ni erreur, ni omission, ni incohérence : **avis de conformité** sur le processus et sur les informations, sous forme négative (« nous n'avons pas relevé d'erreurs, omissions ou incohérences importantes concernant la conformité […] aux ESRS ») [V LD 2026 § 17 ; F13 § 4.2-4.3].

**Si la SARL avait refusé : avis de conformité assorti d'une réserve motivée (1 pt)**
- L'omission d'un site exploité est une **omission non corrigée** qui remet en cause la conformité des informations environnementales : 31,6 % de l'eau consommée et 20 % du tonnage lavé, et une baisse affichée de 37,5 % au lieu de 29,6 % [S, application].
- Ses incidences sont **clairement circonscrites** : un site identifié, des informations précises (eau, énergie, lessives), des montants disponibles ; une réserve qui les décrit et les chiffre permet à l'utilisateur de fonder son jugement : **avis de conformité assorti d'une réserve motivée** sur l'axe des informations, l'avis sur le processus restant de conformité [V LD 2026 § 17 ; F13 § 4.2-4.3].
- Ni non-conformité (l'omission ne touche pas l'ensemble des informations), ni impossibilité (aucune limitation : les données du site sont disponibles) [V F13 § 4.3].

**Réponses tolérées**
- Un avis de conformité accompagné d'une **observation** qui renvoie à la description du périmètre corrigé : points complets.
- Un avis de non-conformité en cas de refus, si le candidat juge que l'omission, cumulée avec les autres défauts de présentation, ne peut être circonscrite : 0,5 pt sur 1.

**Erreurs fréquentes**
- Émettre une réserve alors que les erreurs ont été corrigées (`JUR-A02`).
- Formuler une impossibilité d'émettre un avis, qui sanctionne une limitation et non une omission non corrigée (`JUR-A02`).
- Admettre l'exclusion du site au motif que la publication est volontaire (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 8.1, § 17 ; ESRS 1 (2026) § 88, appendice B | Périmètre ; avis par axe ; réserve ; caractéristiques qualitatives | [V] ; qualification : [S] | F13 § 4.2-4.3, § 7 ; F12 § 17, § 27 |
