# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 11

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 11/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.7 | `exercices/ex28_consolidation_ifrs_actifs_financiers_locations` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.7 | `exercices/ex29_scission_soulte_valeur_reelle` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.9 | `exercices/ex30_audit_immobilisations_remplacement_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 a Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 1 |
| 1.1 b IASB, IFRS Interpretations Committee, EFRAG ; adoption d'IFRS 18 | `2.1.a` Cadre conceptuel de l'IASB, normalisateurs | 1 |
| 1.1 c Cadre conceptuel appliqué au bail et aux actions | `2.1.a` Cadre conceptuel ; `2.2.c` Locations ; `2.2.d` Instruments financiers | 2 |
| 1.1 d Phases de l'intégration de CASTELVIEL | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.2 a Tableau du périmètre, qualifications | `2.1.c` Périmètre ; `2.1.d` Méthodes | 2 |
| 1.2 b Participations ne donnant pas le contrôle de la filiale indirecte | `2.1.c` Périmètre ; `2.2.h` Partage des capitaux propres | 1 |
| 1.3 a Classement IFRS 9 des deux actifs | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 2 |
| 1.3 b Obligation : TIE, tableau d'incidence, écritures | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 3 |
| 1.3 c Actions : incidence et écritures | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 1,5 |
| 1.3 d Option de juste valeur par OCI refusée | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 0,75 |
| 1.3 e Pertes de crédit attendues | `2.2.d` Homogénéisation, thèmes spécifiques aux IFRS | 0,75 |
| 1.4 a Bail : comptes individuels, IFRS 16, acquisition | `2.2.c` Homogénéisation, thèmes communs | 1 |
| 1.4 b Bail : calculs et tableau d'incidence | `2.2.c` Homogénéisation, thèmes communs | 2 |
| 1.4 c Bail : écritures | `2.2.c` Homogénéisation, thèmes communs | 2 |
| 1.5 a Rapprochement et élimination des comptes réciproques | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.5 b Marge interne sur stocks | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.5 c Dividende d'ESSENCERIE DU LOUP | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.6 a Actif net identifiable de CASTELVIEL | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.6 b Frais d'acquisition, goodwill partiel | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.6 c Écarts d'évaluation et résultat retraité | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.6 d Tableaux de partage des trois filiales | `2.2.h` Partage des capitaux propres | 3 |
| 1.6 e Mise en équivalence de la FLACONNERIE D'AZUR | `2.2.h` Partage des capitaux propres (MEE) | 1,5 |
| 1.6 f Écritures d'élimination, de partage et de mise en équivalence | `2.2.g` ; `2.2.h` | 2,5 |
| 1.7 a Extrait de l'état de la situation financière consolidée | `2.3.a` Documents de synthèse consolidés | 5 |
| 1.7 b Notes et différence avec le règlement ANC | `2.3.a` Documents de synthèse consolidés | 2 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = participations ne donnant pas le contrôle (PNC) ; `CAP_ELIM` = capital de la filiale éliminé ; `EA` = goodwill ; `TME` = participation mise en équivalence ; `QP_MEE` = quote-part du résultat net des entités mises en équivalence ; `DU` / `AMO_DU` = droit d'utilisation et ses amortissements ; `DL` = dette locative ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat de l'écriture de bilan. Un suffixe désigne la société concernée (`RST.CASTELVIEL`, `261.NEROVALE` : titres détenus par NÉROVALE).

---

### 1.1 Cadre, processus et périmètre (6 pts)

#### a. Obligation de consolider et référentiel (1 pt)

**Obligation (0,5 pt).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. NÉROVALE SE, société européenne soumise aux règles des sociétés anonymes (énoncé), contrôle exclusivement ESSENCERIE DU LOUP, CASTELVIEL et, par ESSENCERIE DU LOUP, la JASMINERAIE DE CABRIS (question 1.2) (0,25 pt). Aucune exemption ne s'applique (0,25 pt) : NÉROVALE n'est contrôlée par aucune société, et l'exemption des ensembles qui ne forment pas un grand groupe est refusée lorsqu'une société de l'ensemble a des titres admis sur un marché réglementé [V L. 233-17 et L. 123-16-2 ; F03 § 1.1]. Avec 310 M€ de chiffre d'affaires et 1 350 salariés, le groupe dépasse d'ailleurs deux des trois seuils du grand groupe.

**Référentiel (0,5 pt).** Les IFRS adoptées par l'Union européenne sont obligatoires pour les comptes consolidés des sociétés dont les titres sont admis aux négociations sur un marché réglementé d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Les actions de NÉROVALE SE sont admises sur Euronext Paris, marché réglementé : le règlement ANC n° 2020-01 ne lui est pas ouvert.

#### b. Normalisateurs et adoption d'IFRS 18 (1 pt)

- **IASB (0,25 pt)** : groupe indépendant d'experts, au sein de l'IFRS Foundation, organisme sans but lucratif ; il élabore et publie les normes IFRS, IFRS 18 comprise [V page « International Accounting Standards Board », ifrs.org ; F03 § 7.2].
- **IFRS Interpretations Committee, anciennement IFRIC (0,25 pt)** : il élabore les interprétations des normes, qui sont approuvées par l'IASB [V même page ; F03 § 7.2].
- **EFRAG (0,25 pt)** : il fait valoir les positions européennes auprès de l'IASB et conseille la Commission européenne sur la conformité de chaque norme nouvelle ou modifiée aux critères du règlement IAS, dont l'intérêt public européen [V page « Financial reporting », efrag.org ; F03 § 7.2]. Une norme de l'IASB ne s'applique dans l'Union qu'après son adoption par un règlement de la Commission [V intitulé du règlement (UE) 2023/1803 ; F03 § 7.2].
- **IFRS 18 (0,25 pt)** : elle a été adoptée par le règlement (UE) 2026/338, qui supprime IAS 1 ; elle s'applique au plus tard au premier exercice ouvert à compter du **01/01/2027**, son application anticipée étant permise [V règlement (UE) 2026/338, art. 1er et 2 ; IFRS 18 C1 ; F14 § 0, F99]. NÉROVALE ne l'anticipe pas : ses états de 2026 suivent IAS 1, ceux de 2027 suivront IFRS 18.

#### c. Cadre conceptuel appliqué au bail et aux actions (2 pts)

| Niveau | Attendu |
|---|---|
| 0 | Absence de réponse ou réponse non pertinente |
| 0,5 à 1 | Objectif, utilisateurs ou définitions récités, sans application au cas |
| 1,25 à 1,5 | Définitions appliquées au bail (droit contrôlé, obligation actuelle) ou à la juste valeur des actions |
| 2 | Les deux situations expliquées, avec les caractéristiques qualitatives et une conclusion sur l'utilité de l'information |

**Objectif et utilisateurs (0,5 pt).** L'information financière à usage général a pour objectif de fournir une information utile aux investisseurs, prêteurs et autres créanciers, actuels et potentiels, pour leurs décisions de fournir des ressources à l'entité [S présentation du cadre de 2018 ; F03 § 7.2]. Pour les actionnaires de NÉROVALE, société cotée, et pour ses prêteurs, les comptes consolidés doivent montrer les ressources que contrôle le groupe, les obligations qui pèsent sur lui et sa performance.

**Le bail (0,75 pt).** Un actif est une ressource contrôlée par l'entité du fait d'événements passés, dont elle attend des avantages économiques futurs [V IAS 38 § 8 ; F03 § 9] : ce n'est pas la propriété juridique qui compte. Par le bail conclu le 01/01/2026 (événement passé), CASTELVIEL a obtenu le droit de contrôler l'utilisation de l'entrepôt pendant neuf ans [V IFRS 16 § 9 ; F04 § 9] : ce **droit d'utilisation** est la ressource qu'elle contrôle et dont elle tire ses avantages (stockage de sa production). Un passif est une obligation actuelle résultant d'événements passés dont l'extinction se traduira par une sortie de ressources [V IAS 37 § 10 ; F03 § 8] : l'obligation de payer neuf loyers de 314 000 € est née du même contrat. IFRS 16 impose donc au preneur un actif au titre du droit d'utilisation et un passif locatif [V IFRS 16 § 22 ; F04 R2], alors que le plan comptable général ne connaît que les loyers en charges (compte 6132). Le bilan consolidé montre ainsi l'endettement réel du groupe, comparable à celui d'un concurrent qui aurait emprunté pour acheter son entrepôt.

**Les actions (0,75 pt).** Les caractéristiques fondamentales de l'information utile sont la **pertinence** et la **représentation fidèle** [S cadre de 2018 ; F03 § 7.2 ; IAS 1 § 15]. Le portefeuille est acquis pour être revendu à court terme : ce qui intéresse l'utilisateur, c'est la somme qu'il peut en tirer aujourd'hui, que donne le cours de bourse d'un marché actif, et non le prix payé en novembre. La juste valeur (1 640 000 €) est donc l'information pertinente, et elle représente fidèlement la ressource : le trésorier peut vendre à tout moment à ce cours, et sa performance se mesure par la hausse de 120 000 €, qu'il ait ou non déjà vendu. Dans les comptes individuels, la plus-value latente n'est pas comptabilisée [V PCG art. 214-20 ; F04 R11] ; en IFRS 9, les actifs détenus à des fins de transaction sont évalués à la juste valeur, et ses variations passent en résultat (question 1.3) [V IFRS 9 § 4.1.4, 5.7.1 ; F04 § 9].

#### d. Phases de l'intégration de CASTELVIEL (2 pts)

**Phases et objet (1 pt, 0,25 pt par phase correctement décrite, dans l'ordre)**

| Phase | Objet pour CASTELVIEL | Travaux du dossier |
|---|---|---|
| 1. Préparation : périmètre, manuel, liasse | Fixer le périmètre et les méthodes ; diffuser le manuel et le format de liasse (février 2026) ; recueillir la liasse PCG de 2026 (22/01/2027) avec le contrat de bail, et le rapport de l'expert sur les justes valeurs au 01/01/2026 | 1.1, 1.2 |
| 2. Retraitements d'homogénéisation et évaluation à la juste valeur | Passer des comptes PCG de CASTELVIEL aux comptes retraités selon le manuel : bail selon IFRS 16 ; réévaluation des actifs identifiables à l'acquisition et amortissement des écarts ; impôts différés compris. Les autres sociétés retraitent aussi leurs comptes (actifs financiers de NÉROVALE, frais d'acquisition des titres) | 1.3, 1.4, 1.6 a à c |
| 3. Cumul (agrégation) des comptes retraités | Additionner ligne à ligne les comptes retraités de CASTELVIEL et des autres sociétés intégrées globalement (la FLACONNERIE D'AZUR n'est pas cumulée) | 1.7 a (les agrégats de l'annexe 1.9 cumulent, pour simplifier, les comptes individuels ; les retraitements y sont ajoutés poste par poste) |
| 4. Éliminations, puis partage | Rapprocher et éliminer les opérations internes (aucune pour CASTELVIEL, qui ne déclare aucune opération avec le groupe) ; éliminer les titres CASTELVIEL contre la quote-part de l'actif net acquis, constater le goodwill et partager les capitaux propres et le résultat retraités entre le groupe et les PNC ; mettre en équivalence la flaconnerie | 1.5 ; 1.6 b, d à f |

Les états financiers consolidés et leurs notes sont ensuite établis à partir des comptes cumulés, retraités et éliminés (question 1.7).

**Rattachement (1 pt)** : 0,25 pt pour les retraitements (1.3, 1.4, frais et écarts de 1.6) placés avant le cumul ; 0,25 pt pour le rapprochement des comptes réciproques placé avant leur élimination (1.5 a) ; 0,25 pt pour l'élimination des titres et le partage placés en dernier, sur des capitaux propres et un résultat **retraités** (1.6 d à f) ; 0,25 pt pour les états de synthèse (1.7).

**Réponses tolérées (1.1)**
- En b, les fonctions de l'IFRS Interpretations Committee décrites plus largement (questions d'application des normes) si elles sont exactes ; IFRS 18 « applicable en 2027 » sans mention du règlement d'adoption : 0,25 pt sur 0,5 pour l'EFRAG et l'adoption.
- En c, les définitions du cadre de 2018 (ressource économique actuelle contrôlée du fait d'événements passés, droit qui a le potentiel de produire des avantages économiques ; obligation actuelle de transférer une ressource économique) sont attendues au même titre que celles d'IAS 38 § 8 et d'IAS 37 § 10.
- En d, retraitements passés par écritures sur la balance cumulée, à condition qu'ils précèdent les éliminations et le partage ; découpage en cinq ou six phases (rapprochement des réciproques distingué de leur élimination, états de synthèse comptés comme une phase).

**Erreurs fréquentes (1.1)**
- IFRS présentées comme une option ; société européenne jugée hors du champ de L. 233-16.
- EFRAG présenté comme l'auteur des normes, IFRS 18 appliquée dès 2026.
- Entrepôt refusé à l'actif « faute de propriété » ; juste valeur justifiée par la seule « prudence inversée », sans pertinence ni représentation fidèle.
- Phases énumérées sans leur objet, élimination des titres placée avant les retraitements (`JUR-G01`).

**Références normatives (1.1)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 233-16, L. 233-17, L. 123-16-2 | Obligation de consolider, exemptions refusées aux sociétés cotées | [V] | F03 § 1.1 |
| Règlement (CE) n° 1606/2002, art. 4 | IFRS obligatoires (marché réglementé) | [V] | F03 § 1.2 |
| Pages ifrs.org et efrag.org ; règlement (UE) 2023/1803 | IASB, IFRS Interpretations Committee, EFRAG, adoption | [V] | F03 § 7.2 |
| Règlement (UE) 2026/338 ; IFRS 18 C1 | Adoption d'IFRS 18, date d'application | [V] | F14 § 0, F99 |
| Cadre conceptuel de 2018 | Objectif, utilisateurs, caractéristiques qualitatives | [S] | F03 § 7.2 |
| IAS 38 § 8 ; IAS 37 § 10 ; IFRS 16 § 9, 22 | Définitions d'un actif et d'un passif ; contrat de location | [V] | F03 § 8, § 9 ; F04 § 9 |
| PCG art. 214-20 ; IFRS 9 § 4.1.4, 5.7.1 | Plus-value latente non comptabilisée ; juste valeur par le résultat | [V] | F04 R11, § 9 |

---

### 1.2 Périmètre et méthodes (3 pts)

#### a. Tableau du périmètre (2 pts)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % des PNC |
|---|---:|---|---|---:|---:|
| NÉROVALE SE | — | Société mère | — | 100 % | — |
| ESSENCERIE DU LOUP (0,25 pt) | 80 % | Contrôle exclusif | Intégration globale | 80 % | 20 % |
| JASMINERAIE DE CABRIS (0,25 pt) | 60 % | Contrôle exclusif (indirect) | Intégration globale | 80 % × 60 % = 48 % | 52 % |
| CASTELVIEL (0,25 pt) | 75 % | Contrôle exclusif | Intégration globale | 75 % | 25 % |
| FLACONNERIE D'AZUR (0,25 pt) | 30 % | Influence notable | Mise en équivalence | 30 % | — |

**JASMINERAIE DE CABRIS (0,5 pt).** Le pourcentage de contrôle additionne les droits de vote détenus par la mère et par les entités qu'elle contrôle exclusivement, sans multiplication [V ANC art. 211-6 ; F03 § 4.1, même raisonnement en IFRS] : ESSENCERIE DU LOUP, contrôlée à 80 %, dispose de 60 % des voix, désigne le président, arrête le plan de culture et achète toute la récolte. Le groupe a donc, par elle, le pouvoir sur la jasmineraie, il est exposé à ses rendements et peut les influencer : c'est le contrôle au sens d'IFRS 10 [V IFRS 10 § 7 ; F03 § 2]. Le pourcentage d'intérêt, produit des pourcentages de capital le long de la chaîne, n'est que de 48 % [S F03 § 4.1] : il sert au partage, pas à la qualification.

**FLACONNERIE D'AZUR (0,5 pt).** NÉROVALE détient 30 % des droits de vote : l'influence notable est présumée à partir de 20 % [V IAS 28 § 5 ; F03 § 2]. Elle est confirmée par les indices de l'annexe 1.1 : représentation au comité stratégique (deux membres sur six), participation aux décisions sur le budget et les investissements, opérations importantes (40 % de la production achetés par NÉROVALE), échanges de personnel technique (designers) [V IAS 28 § 6 ; F03 § 2]. Il n'y a ni contrôle (la holding familiale a 70 % et le contrôle), ni contrôle conjoint (aucun accord exigeant l'unanimité). Entreprise associée, elle est mise en équivalence [V IAS 28 § 16 ; F03 § 3 ; annexe 1.3, point 4].

#### b. PNC de la filiale indirecte (1 pt)

Les 52 % comprennent les 40 % de la famille de cultivateurs (PNC **directes**) et la part des dirigeants fondateurs d'ESSENCERIE DU LOUP dans les 60 % que celle-ci détient : 20 % × 60 % = 12 % (PNC **indirectes**) (0,5 pt). Les capitaux propres de la jasmineraie appartiennent pour 48 % au groupe et pour 52 % aux PNC.

En approche directe, les capitaux propres de la jasmineraie sont partagés directement entre le groupe (48 %) et les PNC (52 %), sans passer par ceux d'ESSENCERIE DU LOUP [S F03 § 3 et § 4.1 ; F05 § 3]. Ses titres, inscrits à 600 000 € dans les comptes d'ESSENCERIE DU LOUP, ont été payés pour 80 % avec les ressources du groupe et pour 20 % avec celles des minoritaires d'ESSENCERIE DU LOUP : leur élimination est répartie de la même façon, 480 000 € sur la part du groupe et 120 000 € sur les PNC (0,5 pt ; question 1.6 d).

**Réponses tolérées (1.2)** : pourcentage des PNC de la flaconnerie noté 0 % ou « sans objet » ; contrôle exclusif de CASTELVIEL justifié par la seule majorité des droits de vote, avec la nomination des dirigeants.

**Erreurs fréquentes (1.2)** : contrôle de la jasmineraie fixé à 48 % et méthode déduite de ce taux (mise en équivalence) ; PNC de la jasmineraie limitées à 40 % ; influence notable retenue sans les indices, ou contrôle conjoint invoqué sans accord d'unanimité (`JUR-F07`).

**Références normatives (1.2)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 7 ; ANC art. 211-6 (même principe) | Contrôle ; droits détenus par les entités contrôlées | [V] | F03 § 2, § 4.1 |
| IAS 28 § 5, 6, 16 | Présomption, indices d'influence notable, mise en équivalence | [V] | F03 § 2, § 3 |
| Pourcentage d'intérêt en approche directe | Produit des pourcentages le long de la chaîne | [S] | F03 § 4.1 |

---

### 1.3 Actifs financiers de NÉROVALE SE (8 pts)

#### a. Classement selon IFRS 9 (2 pts)

Un actif financier est classé au coût amorti, à la juste valeur par OCI ou à la juste valeur par le résultat, en fonction à la fois du **modèle économique** de gestion et des **caractéristiques de ses flux contractuels** [V IFRS 9 § 4.1.1 ; F04 R11, § 9].

**Obligation : coût amorti (1 pt).** NÉROVALE détient les obligations pour en percevoir les coupons et le remboursement, jusqu'à l'échéance, comme elle l'a toujours fait : le modèle économique est la **perception des flux contractuels** (0,5 pt). Les flux, fixés à des dates spécifiées (coupons de 3,25 % au 31 décembre, remboursement au pair le 31/12/2029), ne sont que des remboursements de principal et des intérêts sur le principal restant dû (0,25 pt). Les deux conditions sont réunies : l'obligation est évaluée au **coût amorti** [V IFRS 9 § 4.1.2 ; F04 § 9], soit son coût initial augmenté chaque année des intérêts au taux effectif, diminué des coupons encaissés : 2 888 876 € au 31/12/2026 (0,25 pt).

**Actions : juste valeur par le résultat (1 pt).** Une action ne donne droit ni à un remboursement de principal ni à des intérêts : elle ne peut relever ni du coût amorti ni de la juste valeur par OCI des instruments de dette [V IFRS 9 § 4.1.2 b), 4.1.4 ; F04 § 9] (0,25 pt). Le portefeuille a été acheté pour être revendu dans les mois suivants, il est géré par le trésorier sur la base des plus-values et présente un profil récent de prises de bénéfices à court terme : il est **détenu à des fins de transaction** [V IFRS 9, appendice A ; F04 § 9] (0,5 pt). Il est évalué à la **juste valeur par le biais du résultat net**, soit le cours de clôture de 1 640 000 €, les variations de juste valeur passant en résultat [V IFRS 9 § 4.1.4, 5.7.1] ; c'est un actif courant [V IAS 1 § 66, 68] (0,25 pt).

#### b. Obligation : taux effectif, tableau d'incidence, écritures (3 pts)

**Taux d'intérêt effectif (0,75 pt).** Le TIE est le taux qui égalise le prix payé (2 822 700 €) et la valeur actualisée des flux à recevoir : cinq coupons de 97 500 € et 3 000 000 € au 31/12/2029 (0,25 pt). Il est supérieur au taux nominal (4,60 % contre 3,25 %) parce que l'obligation a été achetée sous le pair : il comprend le coupon et la décote de 177 300 €, répartie sur la durée de détention (0,25 pt). Appliqué au coût amorti d'ouverture, il donne un rendement constant ; la décote vient augmenter chaque année le coût amorti, qui atteint 3 000 000 € à l'échéance (0,25 pt) [V IFRS 9 § 5.4.1 ; F04 § 9 ; annexe 1.4]. Le produit d'intérêts de 2026 n'est plus le coupon (97 500 €) mais 2 855 044 × 4,60 % = **131 332 €**.

**Tableau d'incidence (1,25 pt)**

| | Ouverture au 01/01/2026 (réserves) | Exercice 2026 (résultat) | Clôture au 31/12/2026 |
|---|---:|---:|---:|
| Coût amorti consolidé | 2 855 044 | | 2 888 876 |
| Coût dans les comptes individuels | 2 822 700 | | 2 822 700 |
| **Écart avant impôt** | **+ 32 344** (0,25 pt) | **+ 33 832** (0,25 pt) | **+ 66 176** (0,25 pt) |
| Impôt différé passif, 25 % | – 8 086 | – 8 458 | – 16 544 (0,25 pt) |
| **Incidence nette** | **+ 24 258** | **+ 25 374** (0,25 pt) | **+ 49 632** |

L'écart de 2025 (129 844 – 97 500) a été constaté au résultat consolidé de 2025 : il est repris en réserves ; celui de 2026 (131 332 – 97 500) majore le résultat. La valeur consolidée dépasse la base fiscale (le coût), la décote n'étant imposée qu'au remboursement : différence imposable, **impôt différé passif** [V IAS 12 § 15 ; F04 R11 ; annexe 1.4].

**Écritures (1 pt)**

**C1 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2721 Obligations | 66 176 | |
| RSV.NÉROVALE Réserves NÉROVALE (32 344 × 75 %) | | 24 258 |
| RST.NÉROVALE Résultat NÉROVALE (33 832 × 75 %) | | 25 374 |
| IDP Impôt différé passif (66 176 × 25 %) | | 16 544 |
| **Total** | **66 176** | **66 176** |
| | *Libellé : obligation de NÉROVALE évaluée au coût amorti* | | |

**C1R (compte de résultat, 0,5 pt)** : débit CH_ID Charge d'impôt différé 8 458 ; débit RES_CR Résultat 25 374 ; crédit 7621 Revenus des titres immobilisés 33 832. *Libellé : complément d'intérêts au taux effectif.*

#### c. Portefeuille d'actions : incidence et écritures (1,5 pt)

**Incidence (0,5 pt).** Juste valeur 1 640 000 – coût 1 520 000 = **+ 120 000 €** en résultat de 2026 (produit financier) ; impôt différé passif 30 000 € (la plus-value ne sera imposée qu'à la cession, la base fiscale reste le coût [V IAS 12 § 20 ; F04 § 9 ; annexe 1.4]) ; incidence nette **+ 90 000 €**. Aucune incidence sur les réserves : le portefeuille a été acquis en 2026.

**C2 (bilan, 0,5 pt)** : débit 5031 Titres cotés (actifs financiers à la juste valeur par le résultat) 120 000 ; crédit RST.NÉROVALE 90 000 ; crédit IDP 30 000. *Libellé : portefeuille d'actions évalué à la juste valeur par le résultat.*

**C2R (compte de résultat, 0,5 pt)** : débit CH_ID 30 000 ; débit RES_CR 90 000 ; crédit 768 Autres produits financiers (variation de juste valeur) 120 000.

#### d. Option de juste valeur par OCI (0,75 pt)

L'option irrévocable de présenter en autres éléments du résultat global les variations de juste valeur d'un placement en instruments de capitaux propres n'est ouverte qu'à un placement **qui n'est pas détenu à des fins de transaction**, et elle s'exerce lors de la comptabilisation initiale, titre par titre [V IFRS 9 § 4.1.4, 5.7.5, B5.7.1 ; F04 R11] (0,5 pt). Le portefeuille est détenu à des fins de transaction (question a) : l'option lui est fermée, et elle ne pourrait de toute façon plus être exercée après l'achat de novembre. Les variations de juste valeur passeront en résultat ; ce résultat traduit précisément la stratégie du trésorier (0,25 pt).

#### e. Pertes de crédit attendues (0,75 pt)

L'obligation, évaluée au coût amorti, entre dans le modèle de dépréciation d'IFRS 9 : une correction de valeur est comptabilisée au titre des **pertes de crédit attendues**, sans attendre une défaillance [V IFRS 9 § 5.5.1 ; F04 § 9] (0,25 pt). Tant que le risque de crédit n'a pas augmenté de façon importante depuis l'acquisition, elle est égale aux pertes attendues sur les **douze mois à venir**, et aux pertes attendues sur la durée de vie dans le cas contraire [V § 5.5.5, 5.5.3] (0,25 pt). L'émetteur honore ses engagements et le service trésorerie estime ces pertes négligeables : aucune correction n'est comptabilisée au 31/12/2026. Le portefeuille d'actions, évalué à la juste valeur par le résultat, n'est pas concerné : la juste valeur intègre déjà tous les risques (0,25 pt).

**Réponses tolérées (1.3)**
- En b, écritures de bilan regroupées avec celle du compte de résultat, si réserves et résultat sont distingués ; intérêts complémentaires crédités au compte 762 ou à un compte « produits d'intérêts » de nom différent.
- En c, variation de juste valeur créditée à un compte « gains sur actifs financiers à la juste valeur » ou à un compte de produits financiers suffixé ; actifs inscrits sur un compte de consolidation propre.
- En e, réponse qui cite la seule règle des douze mois, si l'absence de correction est justifiée.

**Erreurs fréquentes (1.3)**
- Obligation classée à la juste valeur parce qu'elle est cotée, ou actions au coût amorti ; détention à des fins de transaction confondue avec l'option de juste valeur (`JUR-G08`).
- TIE présenté comme le taux du coupon ; écart de 2025 porté au résultat de 2026 ; impôt différé omis (`JUR-G05`, `JUR-G07`).
- Plus-value latente portée en OCI ; impôt différé actif au lieu d'un passif.
- Option OCI jugée possible « tant que les titres ne sont pas vendus ».

**Références normatives (1.3)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 9 § 4.1.1, 4.1.2, 4.1.4 ; appendice A | Critères de classement, coût amorti, juste valeur par le résultat, détention à des fins de transaction | [V] | F04 R11, § 9 |
| IFRS 9 § 5.4.1, 5.7.1 | Intérêts au taux effectif ; variations de juste valeur en résultat | [V] | F04 § 9 |
| IFRS 9 § 5.7.5, B5.7.1 | Option OCI des capitaux propres, hors titres de transaction | [V] | F04 R11 |
| IFRS 9 § 5.5.1, 5.5.3, 5.5.5 | Pertes de crédit attendues | [V] | F04 § 9 |
| IAS 12 § 15, 20 | Impôt différé passif sur la réévaluation non imposée | [V] | F04 § 1, § 9 |
| IAS 1 § 66, 68 | Actifs détenus à des fins de transaction : actifs courants | [V] | F04 § 9, F14 § 2.2 |

---

### 1.4 Contrat de location de CASTELVIEL (5 pts)

#### a. Comptes individuels, IFRS 16 et acquisition (1 pt)

**Comptes individuels (0,25 pt).** CASTELVIEL comptabilise le loyer de 314 000 € en charges (compte 6132) à son échéance ; ni l'entrepôt ni l'engagement de payer les loyers futurs ne figurent au bilan.

**IFRS 16 (0,5 pt).** Le contrat confère le droit de contrôler l'utilisation de l'entrepôt pendant neuf ans [V IFRS 16 § 9]. Les exemptions (courte durée, faible valeur) ne s'appliquent pas [V § 5 ; annexe 1.3, point 2]. À la prise d'effet, le preneur comptabilise un **passif locatif**, égal à la valeur actualisée des loyers non versés au taux d'emprunt marginal (taux implicite non déterminable), soit 2 282 400 €, et un **droit d'utilisation** évalué au coût, ici égal au passif (aucun loyer d'avance, aucun coût direct initial ni de remise en état) [V § 22 à 24, 26 ; F04 R2, § 9]. Le droit d'utilisation est amorti sur neuf ans [V § 31, 32] ; la dette augmente des intérêts et diminue des loyers payés [V § 36, 37].

**Acquisition (0,25 pt).** L'acquéreur comptabilise le droit d'utilisation et le passif locatif des contrats dont l'acquise est preneur, le passif étant évalué comme pour un nouveau contrat à la date d'acquisition, et le droit d'utilisation au même montant, ajusté seulement si les conditions sont favorables ou défavorables par rapport au marché [V IFRS 3 § 28A, 28B ; F04 § 9]. Le bail, qui prend effet le 01/01/2026 aux conditions du marché, apporte un actif et un passif égaux (2 282 400 €) : l'actif net identifiable n'est pas modifié.

#### b. Calculs et tableau d'incidence (2 pts)

**Calculs de 2026 (0,75 pt)**
- Amortissement du droit d'utilisation : 2 282 400 / 9 = **253 600 €** (0,25 pt).
- Intérêts : 2 282 400 × 4,5 % = **102 708 €** (0,25 pt).
- Diminution de la dette : 314 000 – 102 708 = **211 292 €** ; dette au 31/12/2026 : 2 282 400 – 211 292 = **2 071 108 €**, dont 220 800 € à rembourser en 2027 (part courante) et 1 850 308 € au-delà (0,25 pt).

**Tableau d'incidence au 31/12/2026 (1,25 pt)**

| Élément | Comptes individuels | Comptes consolidés | Écart |
|---|---:|---:|---:|
| Droit d'utilisation, net (2 282 400 – 253 600) | 0 | 2 028 800 | + 2 028 800 (0,25 pt) |
| Dette locative | 0 | 2 071 108 | – 2 071 108 |
| Charges de 2026 : loyer / amortissement + intérêts | 314 000 | 356 308 | |
| **Résultat avant impôt** | | | **– 42 308** (0,25 pt) |
| Impôt différé passif sur le droit d'utilisation (2 028 800 × 25 %) | | | – 507 200 (0,25 pt) |
| Impôt différé actif sur la dette locative (2 071 108 × 25 %) | | | + 517 777 (0,25 pt) |
| **Résultat net (– 42 308 + 10 577)** | | | **– 31 731** (0,25 pt) |

Le droit d'utilisation et la dette n'ont pas de valeur fiscale, les loyers étant déductibles à leur échéance : le premier crée une différence imposable, la seconde une différence déductible. L'exemption de comptabilisation initiale ne s'applique pas à ces différences d'un montant égal à la prise d'effet ; les deux impôts différés sont comptabilisés [V IAS 12 § 22A ; F04 R2, § 9]. Vu du groupe, le bail est d'ailleurs repris lors du regroupement d'entreprises : l'exemption de comptabilisation initiale ne s'applique pas non plus [V IAS 12 § 15 b), 66 ; F05 § 2, § 5]. Leur solde net (impôt différé actif de 10 577 €) est égal à 25 % de l'écart de charges de 2026. Contrôle : 2 028 800 – 2 071 108 = – 42 308 € = incidence avant impôt sur les capitaux propres, sans effet sur les réserves (bail de 2026).

#### c. Écritures (2 pts)

**C3 (bilan, 1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| DU Droit d'utilisation – entrepôt de Carros | 2 282 400 | |
| IDA Impôt différé actif (2 071 108 × 25 %) | 517 777 | |
| RST.CASTELVIEL Résultat CASTELVIEL (42 308 × 75 %) | 31 731 | |
| AMO_DU Amortissements du droit d'utilisation | | 253 600 |
| DL Dette locative | | 2 071 108 |
| IDP Impôt différé passif (2 028 800 × 25 %) | | 507 200 |
| **Total** | **2 831 908** | **2 831 908** |
| | *Libellé : bail de l'entrepôt de Carros selon IFRS 16* | | |

**C3R (compte de résultat, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements (droit d'utilisation) | 253 600 | |
| 661 Charges d'intérêts (dette locative) | 102 708 | |
| 6132 Locations immobilières (loyer annulé) | | 314 000 |
| CH_ID Produit d'impôt différé (42 308 × 25 %) | | 10 577 |
| RES_CR Résultat | | 31 731 |
| **Total** | **356 308** | **356 308** |

La charge d'intérêts est présentée parmi les charges financières, séparément de l'amortissement [V IFRS 16 § 49 ; F04 § 9].

**Réponses tolérées (1.4)** : écriture d'origine (droit d'utilisation contre dette, 2 282 400 €) passée séparément, puis écritures de l'exercice ; droit d'utilisation inscrit à un compte 213 ou 2181 suffixé ; dette locative inscrite au compte 1687 ou 164 ; impôts différés présentés pour leur solde net (impôt différé actif de 10 577 €), si le calcul par élément est montré.

**Erreurs fréquentes (1.4)** : bail laissé en charges « parce que CASTELVIEL n'est pas propriétaire » ; loyer maintenu en charges en plus de l'amortissement et des intérêts (double comptage) ; dette réduite du loyer entier, sans les intérêts ; intérêts calculés sur la dette de clôture ; impôt différé omis ou calculé sur le loyer ; bail ajouté à l'actif net identifiable à la date d'acquisition (`JUR-G06`, `JUR-F05`).

**Références normatives (1.4)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 16 § 5, 9, 22 à 24, 26, 31, 32, 36, 37, 49 | Définition, exemptions, comptabilisation et évaluation chez le preneur, présentation des intérêts | [V] | F04 R2, § 9 |
| IFRS 3 § 28A, 28B | Contrats de location de l'acquise | [V] | F04 § 9 |
| IAS 12 § 22A | Impôts différés d'un contrat de location | [V] | F04 R2, § 9 |

---

### 1.5 Opérations internes (4 pts)

#### a. Rapprochement et élimination des comptes réciproques (1,5 pt)

**Rapprochement (0,5 pt).** Créance déclarée par ESSENCERIE DU LOUP 1 020 000 € ; dette déclarée par NÉROVALE 870 000 € ; écart 150 000 €, égal à l'écart entre les ventes (4 800 000 €) et les achats (4 650 000 €). Il provient de la facture du 31/12/2026 : les absolues ont quitté ESSENCERIE DU LOUP en 2026, qui a constaté la vente, mais NÉROVALE ne les a reçues et enregistrées qu'en 2027. Pour le groupe, ces marchandises sont un **stock en transit** au 31/12/2026 ; le manuel l'inscrit chez la destinataire [V annexe 1.3, point 5]. On ne peut éliminer des soldes et des flux réciproques qu'après les avoir rendus égaux.

**C4 (bilan, 0,25 pt)** : débit 31 Matières premières 150 000 ; crédit 401 Fournisseurs 150 000. *Libellé : absolues en transit comptabilisées chez NÉROVALE.* **C4R (compte de résultat, 0,25 pt)** : débit 601 Achats stockés 150 000 ; crédit 6031 Variation des stocks de matières premières 150 000 (sans incidence sur le résultat).

**C5 (bilan, 0,25 pt)** : débit 401 Fournisseurs 1 020 000 ; crédit 411 Clients 1 020 000. *Libellé : élimination des dettes et créances réciproques.* **C5R (compte de résultat, 0,25 pt)** : débit 701 Ventes de produits finis 4 800 000 ; crédit 601 Achats stockés 4 800 000. Ces éliminations sont sans incidence sur le résultat [V ANC art. 251-1, principe identique ; IFRS 10 B86 c) ; F04 R14].

#### b. Marge interne sur stocks (1,5 pt)

**Calculs (0,75 pt)**

| Élément | Montant |
|---|---:|
| Extraits d'ESSENCERIE DU LOUP en stock : 450 000 + 150 000 en transit (0,25 pt) | 600 000 |
| **Marge interne : 600 000 × 30 %** (taux sur le prix de vente) (0,25 pt) | **180 000** |
| Impôt différé actif : 180 000 × 25 % | 45 000 |
| **Marge nette d'impôt** | **135 000** |
| dont groupe (80 %) / PNC d'ESSENCERIE DU LOUP (20 %) (0,25 pt) | 108 000 / 27 000 |

Les profits internes compris dans des actifs sont éliminés en totalité, la vendeuse étant intégrée globalement [V IFRS 10 B86 c) ; F04 R14]. La vente étant réalisée par ESSENCERIE DU LOUP, l'élimination réduit son résultat et se partage entre le groupe et ses PNC [V ANC art. 251-2, principe identique ; F04 R14 ; annexe 1.3, point 5]. Le stock est ramené au coût pour le groupe (420 000 €), inférieur à sa base fiscale chez NÉROVALE (600 000 €) : impôt différé actif [V IAS 12 § 24 ; F04 R14]. Aucune marge n'est à éliminer à l'ouverture : NÉROVALE ne détenait aucun extrait au 31/12/2025.

**C6 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.ESSENCERIE Résultat ESSENCERIE DU LOUP (180 000 × 75 %) | 135 000 | |
| IDA Impôt différé actif (180 000 × 25 %) | 45 000 | |
| 31 Matières premières | | 180 000 |
| **Total** | **180 000** | **180 000** |
| | *Libellé : élimination de la marge d'ESSENCERIE DU LOUP comprise dans les stocks* | | |

**C6R (compte de résultat, 0,25 pt)** : débit 6031 Variation des stocks de matières premières 180 000 ; crédit CH_ID Produit d'impôt différé 45 000 ; crédit RES_CR Résultat 135 000. La répartition 108 000 / 27 000 se fait dans le partage du résultat retraité d'ESSENCERIE DU LOUP (question 1.6 d).

#### c. Dividende d'ESSENCERIE DU LOUP (1 pt)

**Justification (0,5 pt).** NÉROVALE a reçu 80 % × 1 000 000 = **800 000 €**, comptabilisés en produits. Pour le groupe, ce n'est pas un revenu : il prélève le résultat de 2025 d'ESSENCERIE DU LOUP, déjà compris dans le résultat consolidé de 2025, puis dans les réserves consolidées. Les dividendes internes sont éliminés en totalité [V ANC art. 251-2, principe identique ; IFRS 10 B86 c) ; F04 R14] : le dividende quitte le résultat de NÉROVALE pour ses réserves, où il compense la baisse des réserves d'ESSENCERIE DU LOUP. Les 200 000 € versés aux fondateurs ont réduit les PNC ; le partage porte sur les capitaux propres après distribution.

**C7 (bilan, 0,25 pt)** : débit RST.NÉROVALE 800 000 ; crédit RSV.NÉROVALE 800 000. **C7R (compte de résultat, 0,25 pt)** : débit 7611 Revenus des titres de participation 800 000 ; crédit RES_CR Résultat 800 000.

**Réponses tolérées (1.5)** : correction du transit et élimination des réciproques regroupées en une écriture (dette éliminée 870 000 €, créance 1 020 000 €, stock 150 000 €), si les flux sont aussi égalisés ; élimination de la marge en compte de résultat par un compte de coût des ventes ; dividende éliminé directement dans l'écriture de partage d'ESSENCERIE DU LOUP, si le résultat consolidé est juste.

**Erreurs fréquentes (1.5)** : écart de 150 000 € « corrigé » en annulant la vente d'ESSENCERIE DU LOUP, ou laissé sans correction ; marge calculée sur le seul stock enregistré (450 000 × 30 % = 135 000 €) en oubliant le transit ; marge calculée sur le coût (600 000 × 30/130) ; élimination limitée à 80 %, ou entièrement imputée au groupe ; impôt différé omis ; dividende éliminé pour 1 000 000 €.

**Références normatives (1.5)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 B86 c) | Élimination complète des opérations intragroupe | [V] | F04 R14 |
| ANC 2020-01 art. 251-1, 251-2 | Comptes réciproques ; répartition selon la société qui a réalisé le résultat ; dividendes internes (principe identique) | [V] | F04 R14 |
| IAS 12 § 24 | Impôt différé actif sur la marge éliminée | [V] | F04 § 1, R14 |

---

### 1.6 Acquisition de CASTELVIEL, partage des capitaux propres et mise en équivalence (12 pts)

#### a. Actif net identifiable de CASTELVIEL au 01/01/2026 (1,5 pt)

| Élément | Montant |
|---|---:|
| Capitaux propres de CASTELVIEL (4 000 000 + 5 200 000) | 9 200 000 |
| Écart d'évaluation du bâtiment (3 800 000 – 2 600 000) (0,25 pt) | + 1 200 000 |
| Relations clientèle, non comptabilisées par l'acquise (0,5 pt) | + 1 600 000 |
| Impôt différé passif sur les écarts (2 800 000 × 25 %) (0,25 pt) | – 700 000 |
| Bail de l'entrepôt : droit d'utilisation et dette égaux | 0 |
| **Actif net identifiable à la juste valeur** (0,5 pt) | **11 300 000** |

Les actifs identifiables acquis et les passifs repris sont évalués à leur juste valeur à la date d'acquisition, y compris des relations clientèle séparables que l'acquise n'avait pas comptabilisées ; les impôts différés des écarts sont constatés selon IAS 12 [V IFRS 3 § 24 ; IAS 12 § 66 ; F05 § 2 ; annexe 1.7]. Le bail n'ajoute rien (question 1.4 a).

#### b. Frais d'acquisition et goodwill partiel (2 pts)

**Frais d'acquisition (1 pt).** En IFRS, les frais connexes à l'acquisition sont des charges de la période où ils sont engagés, exclues de la contrepartie transférée [V IFRS 3 § 53 ; F05 § 2 ; annexe 1.3, point 3]. NÉROVALE les a incorporés au coût des titres (11 040 000 €) : le retraitement les sort des titres et les porte en charges de 2026, sans impôt différé selon le manuel (0,5 pt). (En règlement ANC, au contraire, ils entreraient dans le coût, nets d'impôt [V art. 231-2 ; F05 § 1.1].)

**C8 (bilan, 0,25 pt)** : débit RST.NÉROVALE 240 000 ; crédit 261.NÉROVALE Titres de participation CASTELVIEL 240 000. **C8R (compte de résultat, 0,25 pt)** : débit 6226 Honoraires 240 000 ; crédit RES_CR Résultat 240 000. *Libellé : frais d'acquisition des titres CASTELVIEL passés en charges.*

**Goodwill partiel (0,75 pt)**

| Élément | Montant |
|---|---:|
| Contrepartie transférée (hors frais) | 10 800 000 |
| – Quote-part de l'actif net identifiable : 75 % × 11 300 000 | – 8 475 000 |
| **Goodwill partiel** | **2 325 000** |

[V IFRS 3 § 19, 32 ; F05 § 2.1]

**PNC à la date d'acquisition (0,25 pt)** : 25 % × 11 300 000 = **2 825 000 €** : le groupe a choisi de les évaluer à leur quote-part de l'actif net identifiable [V IFRS 3 § 19 ; annexe 1.3, point 3] ; elles ne comprennent aucune part de goodwill. Le goodwill n'est pas amorti et aucune perte de valeur n'est à constater au 31/12/2026 (annexe 1.3).

#### c. Écarts d'évaluation et résultat retraité de CASTELVIEL (1,5 pt)

**Incidence de 2026 (0,5 pt)** : bâtiment 1 200 000 / 20 = 60 000 € ; relations clientèle 1 600 000 / 8 = 200 000 € ; dotations complémentaires 260 000 €, impôt différé 65 000 €, incidence nette **– 195 000 €**.

**C9 (bilan, constatation des écarts au 01/01/2026)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments (usine de Valbonne) | 1 200 000 | |
| 208 Autres immobilisations incorporelles (relations clientèle) | 1 600 000 | |
| IDP Impôt différé passif (2 800 000 × 25 %) | | 700 000 |
| RSV.CASTELVIEL Réserves CASTELVIEL (écarts d'évaluation nets) | | 2 100 000 |
| **Total** | **2 800 000** | **2 800 000** |

**C10 (bilan, amortissement de 2026)** : débit RST.CASTELVIEL 195 000 ; débit IDP 65 000 ; crédit 28131 Amortissements des bâtiments 60 000 ; crédit 2808 Amortissements des autres immobilisations incorporelles 200 000. **C10R (compte de résultat)** : débit 6811 Dotations aux amortissements 260 000 ; crédit CH_ID Produit d'impôt différé 65 000 ; crédit RES_CR Résultat 195 000.

(0,5 pt pour les trois écritures.)

**Résultat retraité de CASTELVIEL (0,5 pt)**

| Élément | Montant |
|---|---:|
| Résultat individuel de 2026 | 1 426 731 |
| Bail selon IFRS 16, net d'impôt (question 1.4) | – 31 731 |
| Amortissement des écarts d'évaluation, net d'impôt | – 195 000 |
| **Résultat retraité** | **1 200 000** |

#### d. Tableaux de partage au 31/12/2026 (3 pts, 1 pt par société)

**ESSENCERIE DU LOUP (intérêt 80 %)**

| Capitaux propres retraités | Total | Groupe (80 %) | PNC (20 %) |
|---|---:|---:|---:|
| Capital | 2 500 000 | 2 000 000 | 500 000 |
| Réserves (après distribution) | 6 300 000 | 5 040 000 | 1 260 000 |
| – Titres ESSENCERIE DU LOUP éliminés | | – 2 000 000 | |
| **Réserves consolidées / PNC hors résultat** (0,5 pt) | | **5 040 000** | **1 760 000** |
| Résultat retraité : 1 800 000 – 135 000 (marge interne) (0,5 pt) | 1 665 000 | **1 332 000** | **333 000** |

**JASMINERAIE DE CABRIS (intérêt 48 %, PNC 52 %)**

| Capitaux propres | Total | Groupe (48 %) | PNC (52 %) |
|---|---:|---:|---:|
| Capital | 1 000 000 | 480 000 | 520 000 |
| Réserves | 750 000 | 360 000 | 390 000 |
| – Titres JASMINERAIE détenus par ESSENCERIE DU LOUP (600 000), répartis 80 % / 20 % (0,5 pt) | | – 480 000 | – 120 000 |
| **Réserves consolidées / PNC hors résultat** (0,25 pt) | | **360 000** | **790 000** |
| Résultat (0,25 pt) | 250 000 | **120 000** | **130 000** |

Contrôle : les réserves du groupe (360 000 €) sont sa part, 48 %, des réserves accumulées depuis la création (750 000 €) ; les PNC (790 000 €) sont 40 % × 1 750 000 + 12 % × 750 000.

**CASTELVIEL (intérêt 75 %)**

| Capitaux propres retraités | Total | Groupe (75 %) | PNC (25 %) |
|---|---:|---:|---:|
| Capital | 4 000 000 | 3 000 000 | 1 000 000 |
| Réserves (comptes individuels) | 5 200 000 | 3 900 000 | 1 300 000 |
| Écarts d'évaluation nets à l'acquisition | 2 100 000 | 1 575 000 | 525 000 |
| **Actif net identifiable à l'acquisition** (0,25 pt) | **11 300 000** | **8 475 000** | **2 825 000** |
| – Titres CASTELVIEL éliminés (11 040 000 – 240 000) | | – 10 800 000 | |
| + Goodwill partiel (0,25 pt) | | + 2 325 000 | |
| **Réserves consolidées / PNC hors résultat** | | **0** | **2 825 000** |
| Résultat retraité de 2026 (0,5 pt) | 1 200 000 | **900 000** | **300 000** |

Acquise le 01/01/2026, CASTELVIEL n'apporte aucune réserve consolidée. PNC au 31/12/2026 : 2 825 000 + 300 000 = **3 125 000 €**.

#### e. Mise en équivalence de la FLACONNERIE D'AZUR (1,5 pt)

| | Total | Quote-part du groupe (30 %) |
|---|---:|---:|
| Capital | 2 000 000 | 600 000 |
| Réserves | 4 000 000 | 1 200 000 |
| Résultat de 2026 | 700 000 | 210 000 |
| Quote-part des capitaux propres | 6 700 000 | 2 010 000 |
| + Goodwill compris dans le coût : 1 650 000 – 30 % × 4 500 000 (0,25 pt) | | 300 000 |
| **Valeur de la participation mise en équivalence** (0,25 pt) | | **2 310 000** |
| – Titres FLACONNERIE D'AZUR éliminés | | – 1 650 000 |
| **Réserves consolidées : 30 % × (6 000 000 – 4 500 000)** (0,25 pt) | | **450 000** |
| **Quote-part du résultat** (0,25 pt) | | **210 000** |

Le goodwill payé en 2021 n'est pas présenté séparément : il fait partie de la valeur comptable de la participation [V IAS 28 § 32 ; F05 § 4, § 5 ; annexe 1.3, point 4].

**Dividende (0,5 pt).** Les distributions reçues d'une entité mise en équivalence **réduisent la valeur comptable de la participation** [V IAS 28 § 10 ; F05 § 4] : conserver en produit les 60 000 € reçus compterait deux fois le résultat de 2025 de la flaconnerie, déjà compris dans la quote-part de 2025. Le dividende est éliminé du résultat de NÉROVALE et reclassé en réserves (écriture C14) ; la valeur d'équivalence est calculée sur les capitaux propres après distribution. Contrôle : valeur au 31/12/2025, 30 % × 6 200 000 + 300 000 = 2 160 000 ; + 210 000 ; – 60 000 ; = **2 310 000 €**.

#### f. Écritures d'élimination, de partage et de mise en équivalence (2,5 pts)

**C11 (bilan, ESSENCERIE DU LOUP, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.ESSENCERIE Capital ESSENCERIE DU LOUP | 2 500 000 | |
| RSV.ESSENCERIE Réserves ESSENCERIE DU LOUP | 6 300 000 | |
| RST.ESSENCERIE Résultat retraité (1 800 000 – 135 000) | 1 665 000 | |
| 261.NÉROVALE Titres ESSENCERIE DU LOUP | | 2 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 5 040 000 |
| RST_G Résultat consolidé – part du groupe | | 1 332 000 |
| RSV_M PNC – réserves | | 1 760 000 |
| RST_M PNC – résultat | | 333 000 |
| **Total** | **10 465 000** | **10 465 000** |

**C12 (bilan, JASMINERAIE DE CABRIS, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.JASMINERAIE Capital JASMINERAIE DE CABRIS | 1 000 000 | |
| RSV.JASMINERAIE Réserves JASMINERAIE DE CABRIS | 750 000 | |
| RST.JASMINERAIE Résultat JASMINERAIE DE CABRIS | 250 000 | |
| 261.ESSENCERIE Titres JASMINERAIE détenus par ESSENCERIE DU LOUP | | 600 000 |
| RSV_G Réserves consolidées – part du groupe | | 360 000 |
| RST_G Résultat consolidé – part du groupe | | 120 000 |
| RSV_M PNC – réserves | | 790 000 |
| RST_M PNC – résultat | | 130 000 |
| **Total** | **2 000 000** | **2 000 000** |

**C13 (bilan, CASTELVIEL, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.CASTELVIEL Capital CASTELVIEL | 4 000 000 | |
| RSV.CASTELVIEL Réserves CASTELVIEL (5 200 000 + 2 100 000) | 7 300 000 | |
| RST.CASTELVIEL Résultat retraité | 1 200 000 | |
| EA Goodwill partiel | 2 325 000 | |
| 261.NÉROVALE Titres CASTELVIEL (après C8) | | 10 800 000 |
| RST_G Résultat consolidé – part du groupe | | 900 000 |
| RSV_M PNC – quote-part de l'actif net identifiable | | 2 825 000 |
| RST_M PNC – résultat | | 300 000 |
| **Total** | **14 825 000** | **14 825 000** |
| | *Libellé : élimination des titres CASTELVIEL, goodwill partiel et partage* | | |

Le résultat éliminé est celui que laissent les écritures C3 (– 31 731) et C10 (– 195 000) ; les réserves éliminées comprennent les écarts nets de C9 ; les titres sont ceux que laisse C8.

**C14 (bilan, dividende de la flaconnerie, 0,25 pt avec C14R)** : débit RST.NÉROVALE 60 000 ; crédit RSV.NÉROVALE 60 000. **C14R** : débit 7611 Revenus des titres de participation 60 000 ; crédit RES_CR 60 000.

**C15 (bilan, mise en équivalence, 0,5 pt avec C15R)**

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence (FLACONNERIE D'AZUR) | 2 310 000 | |
| 261.NÉROVALE Titres FLACONNERIE D'AZUR | | 1 650 000 |
| RSV_G Réserves consolidées – part du groupe | | 450 000 |
| RST_G Résultat consolidé – part du groupe | | 210 000 |
| **Total** | **2 310 000** | **2 310 000** |

**C15R** : débit RES_CR Résultat 210 000 ; crédit QP_MEE Quote-part du résultat net des entités mises en équivalence 210 000.

**Réponses tolérées (1.6)**
- C9 et C13 regroupées ; écarts d'évaluation crédités à un compte « écarts d'évaluation » repris dans le partage ; frais d'acquisition retraités dans l'écriture d'élimination des titres (titres crédités pour 11 040 000 € et charge de 240 000 € au résultat de NÉROVALE).
- En d, partage de la jasmineraie présenté en deux temps (part d'ESSENCERIE DU LOUP, puis répartition 80 / 20), s'il aboutit aux mêmes montants ; tableau de CASTELVIEL avec le goodwill présenté hors du tableau.
- En e, goodwill de la flaconnerie présenté sur une ligne distincte du tableau, si la valeur de la participation le comprend.
- En c à f, cohérence avec un résultat erroné aux questions 1.4 et 1.5 : l'erreur n'est pénalisée qu'une fois (`JUR-F08`).

**Erreurs fréquentes (1.6)**
- Frais laissés dans le coût des titres en IFRS (goodwill de 2 565 000 €), ou retenus nets d'impôt comme en règlement ANC (goodwill de 2 505 000 €) : erreur symétrique de `JUR-G02`.
- Relations clientèle oubliées ou non amorties ; impôt différé omis sur les écarts ; goodwill complet calculé alors que le manuel retient le goodwill partiel.
- Partage de la jasmineraie à 60 / 40 ; titres de la jasmineraie éliminés en totalité sur la part du groupe ; partage sur les capitaux propres individuels, sans la marge, le bail ni les écarts (`JUR-G04`).
- Goodwill de la flaconnerie oublié dans la valeur d'équivalence (2 010 000 €) ou présenté en goodwill au bilan ; dividende ajouté à la valeur d'équivalence (`JUR-G03`) ; écritures déséquilibrées (`JUR-F04`).

**Références normatives (1.6)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 19, 24, 32, 53 | Option d'évaluation des PNC, impôts différés, goodwill, frais connexes en charges | [V] | F05 § 2 |
| IAS 12 § 66 | Impôts différés d'un regroupement | [V] | F05 § 2 |
| IFRS 10 § 22, B86 | PNC dans les capitaux propres ; élimination des titres | [V] | F03 § 3, F05 § 3 |
| IAS 28 § 10, 32 | Mise en équivalence, distributions, goodwill compris dans la participation | [V] | F05 § 4 |
| ANC 2020-01 art. 231-2 | Frais inclus dans le coût, nets d'impôt (comparaison) | [V] | F05 § 1.1 |

---

### 1.7 Documents de synthèse (7 pts)

#### a. Extrait de l'état de la situation financière consolidée au 31/12/2026 (5 pts)

**Réserves consolidées et résultat net part du groupe (1 pt : 0,5 pt pour chaque total)**

| Société | Réserves consolidées | Résultat net part du groupe |
|---|---:|---:|
| NÉROVALE SE | 54 000 000 + 24 258 (C1) + 800 000 (C7) + 60 000 (C14) = 54 884 258 | 14 500 000 + 25 374 (C1) + 90 000 (C2) – 800 000 (C7) – 240 000 (C8) – 60 000 (C14) = 13 515 374 |
| ESSENCERIE DU LOUP | 5 040 000 | 1 332 000 |
| JASMINERAIE DE CABRIS | 360 000 | 120 000 |
| CASTELVIEL | 0 | 900 000 |
| FLACONNERIE D'AZUR | 450 000 | 210 000 |
| **Total** | **60 734 258** | **16 077 374** |

Contrôle du résultat : somme des résultats individuels 17 976 731 + 25 374 (C1) + 90 000 (C2) – 31 731 (C3) – 135 000 (C6) – 800 000 (C7) – 240 000 (C8) – 195 000 (C10) – 60 000 (C14) + 210 000 (C15) = **16 840 374 €** (résultat net de l'ensemble consolidé) ; PNC 333 000 + 130 000 + 300 000 = 763 000 € ; part du groupe 16 077 374 €.

PNC au 31/12/2026 : ESSENCERIE DU LOUP 2 093 000 + JASMINERAIE 920 000 + CASTELVIEL 3 125 000 = **6 138 000 €**.

**Extrait de l'état de la situation financière consolidée au 31/12/2026**

| Poste | Classement | Calcul | Montant |
|---|---|---|---:|
| Goodwill (0,25 pt) | Actif non courant | CASTELVIEL (C13) | 2 325 000 |
| Immobilisations incorporelles (0,25 pt) | Actif non courant | 6 850 000 + 1 600 000 – 200 000 (relations clientèle) | 8 250 000 |
| Immobilisations corporelles (0,25 pt) | Actif non courant | 61 400 000 + 1 200 000 – 60 000 (bâtiment) | 62 540 000 |
| Droits d'utilisation (0,25 pt) | Actif non courant | 2 282 400 – 253 600 | 2 028 800 |
| Participation mise en équivalence (0,25 pt) | Actif non courant | FLACONNERIE D'AZUR | 2 310 000 |
| Actifs financiers non courants (0,25 pt) | Actif non courant | 3 232 700 + 66 176 : obligation au coût amorti 2 888 876 et dépôts 410 000 | 3 298 876 |
| Actifs financiers à la juste valeur par le résultat (0,25 pt) | Actif courant | 1 520 000 + 120 000 : actions au cours de clôture | 1 640 000 |
| Actifs d'impôt différé (0,25 pt) | Actif non courant | 517 777 (dette locative) + 45 000 (marge interne) | 562 777 |
| Réserves consolidées | Capitaux propres attribuables aux propriétaires de la mère | tableau ci-dessus | 60 734 258 |
| Résultat net part du groupe | Capitaux propres attribuables aux propriétaires de la mère | tableau ci-dessus | 16 077 374 |
| Participations ne donnant pas le contrôle (0,5 pt) | Capitaux propres, séparées | 2 093 000 + 920 000 + 3 125 000 | 6 138 000 |
| Dettes locatives non courantes (0,25 pt avec la part courante) | Passif non courant | 2 071 108 – 220 800 | 1 850 308 |
| Dettes locatives courantes | Passif courant | part remboursable en 2027 | 220 800 |
| Passifs d'impôt différé (0,25 pt) | Passif non courant | 16 544 + 30 000 + 507 200 + (700 000 – 65 000) | 1 188 744 |

(1 pt pour le classement : actifs et passifs courants et non courants, impôts différés jamais courants, PNC au sein des capitaux propres mais séparées de la part du groupe.)

Capitaux propres attribuables aux propriétaires de la mère, pour information : capital 30 000 000 + primes 8 000 000 + 60 734 258 + 16 077 374 = 114 811 632 € ; total des capitaux propres 120 949 632 €.

L'état présente au minimum les postes du § 54 d'IAS 1, dont les participations mises en équivalence, les actifs et passifs d'impôt différé et, au sein des capitaux propres, les PNC séparées des capitaux propres attribuables aux propriétaires de la mère [V IAS 1 § 54 ; IFRS 10 § 22 ; F14 § 2.2] ; il distingue les éléments courants et non courants [V IAS 1 § 60, 66, 69] ; les impôts différés ne sont jamais courants [V IAS 1 § 56]. Les actions, détenues à des fins de transaction, sont un actif courant [V IAS 1 § 66, 68]. Les droits d'utilisation et les dettes locatives figurent sur des lignes distinctes, comme le prévoit le manuel [V IFRS 16 § 47 ; F04 § 9]. Le goodwill peut aussi être compris dans les immobilisations incorporelles : IAS 1 n'impose pas de poste propre [V F14 § 2.2]. La présentation sans compensation des impôts différés est une convention de l'énoncé ; IAS 12 § 74 conduirait à compenser par entité imposable (NÉROVALE : passif net 1 544 € ; CASTELVIEL : passif net 624 423 €), soit 625 967 € d'impôt différé passif net [V F04 § 1].

#### b. Notes et différence avec le règlement ANC (2 pts)

**Notes (1,5 pt).** Les notes présentent la base d'établissement des états, les méthodes comptables et les informations exigées par les IFRS, dans l'ordre des postes, avec des renvois depuis chaque poste [V IAS 1 § 112 à 114 ; F14 § 2.5]. Pour le cas (0,5 pt par thème, trois thèmes sur quatre suffisent) :
- **périmètre et méthodes** : liste des sociétés, pourcentages de contrôle et d'intérêt (JASMINERAIE détenue indirectement, intérêt de 48 %), méthode retenue, et justification de l'influence notable sur la FLACONNERIE D'AZUR ; approche directe ;
- **regroupement d'entreprises** : entrée de CASTELVIEL le 01/01/2026 ; prix de 10 800 000 € ; frais de 240 000 € en charges ; justes valeurs des actifs identifiables (bâtiment, relations clientèle) et actif net de 11 300 000 € ; méthode de la quote-part pour les PNC (2 825 000 €) ; goodwill de 2 325 000 €, non amorti ;
- **instruments financiers** : catégories d'IFRS 9 retenues et critères (modèle économique, flux contractuels) ; obligation au coût amorti (TIE de 4,60 %, 2 888 876 €), actions détenues à des fins de transaction à la juste valeur (1 640 000 €, gain de 120 000 € en résultat) ; traitement du risque de crédit ;
- **contrats de location** : méthode du preneur et exemptions appliquées ; droit d'utilisation (2 028 800 €, amortissement de 253 600 €), dette locative (2 071 108 €, dont 220 800 € à moins d'un an), charge d'intérêts (102 708 €), taux d'emprunt marginal de 4,5 % ; postes où ils figurent [V IFRS 16 § 47, 49 ; F04 § 9].

**Différence avec le règlement ANC (0,5 pt, une seule attendue)**
- en règlement ANC, les **intérêts minoritaires** forment une rubrique distincte des capitaux propres part du groupe [V ANC art. 281-1 ; F14 § 1.2], alors que les PNC sont présentées au sein des capitaux propres en IFRS ;
- ou : le modèle ANC distingue l'**actif immobilisé et l'actif circulant**, et non les éléments courants et non courants [V art. 281-1 ; F14 § 1.2, § 4] ;
- ou : les impôts différés y figurent en « dont » des autres créances et des autres dettes, et non sur des postes distincts [V art. 281-1 ; F14 § 4] ;
- ou, accepté bien qu'il s'agisse d'une différence de comptabilisation plus que de présentation : aucune disposition du règlement ne prévoit l'inscription au bilan des **locations simples** : l'entrepôt de Carros n'y figurerait pas, ni la dette locative [V ANC art. 272-2 ; F04 R2].

**Réponses tolérées (1.7)**
- Goodwill compris dans les immobilisations incorporelles (10 575 000 €), si son montant est indiqué ; droits d'utilisation compris dans les immobilisations corporelles, avec mention [V IFRS 16 § 47].
- Réserves consolidées et résultat présentés sur une seule ligne « réserves et résultat consolidés » (76 811 632 €) ; candidat qui présente aussi d'autres postes (stocks, créances, capitaux propres totaux) : aucun point supplémentaire.
- Impôts différés compensés par société, sans perte de points si le candidat justifie la compensation par entité fiscale ; à défaut de justification, 0,25 pt perdu (l'énoncé demande une présentation sans compensation).
- Cohérence avec les erreurs antérieures du candidat : une erreur reportée n'est pénalisée qu'une fois (`JUR-F08`).

**Erreurs fréquentes (1.7)**
- Titres de participation laissés dans les actifs financiers non courants ; obligation et actions laissées au coût ; réserves et résultat non justifiés société par société (`JUR-F02`, `JUR-G01`).
- PNC présentées hors des capitaux propres ; PNC de la jasmineraie calculées à 40 % ; goodwill de la flaconnerie inscrit en goodwill du groupe.
- Dette locative non ventilée entre courant et non courant ; impôts différés classés en courant ; actions classées en non courant.

**Références normatives (1.7)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 1 § 54, 56, 60, 66, 69, 112 à 114 | Postes minimaux, courant / non courant, impôts différés, notes | [V] | F14 § 2.2, § 2.5 |
| IFRS 10 § 22 | PNC dans les capitaux propres | [V] | F03 § 3, F14 § 2.2 |
| IFRS 16 § 47, 49 | Présentation des droits d'utilisation et des dettes locatives | [V] | F04 § 9 |
| ANC 2020-01 art. 272-2, 281-1 | Locations simples non inscrites ; modèle de bilan consolidé | [V] | F04 R2, F14 § 1.2 |

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, référentiel, contrôle, sens et mode d'évaluation de chaque apport, régime fiscal | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable ; `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur ; `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 4 |
| 2.2 Valeur réelle et composition des apports | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 3 |
| 2.3 Actions émises, parités, soulte et plafond légal, équité, répartition du capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer ; `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 5 |
| 2.4 Écritures chez OLIVALANE | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 3 |
| 2.5 Écritures de base chez CISTRANE et chez CIRÉLANE | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 4,5 |
| 2.6 Écritures complémentaires chez CISTRANE : créance réciproque et frais de scission | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 2,5 |
| 2.7 Note au président de CISTRANE | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 3 |
| **Total** | | **25** |

---

### 2.1 Qualification, mode d'évaluation des apports, régime fiscal (4 pts)

**Qualification et modalités (0,75 pt).** L'opération est une **scission** : OLIVALANE transmet l'ensemble de son patrimoine à **plusieurs sociétés**, ici deux sociétés existantes, CISTRANE et CIRÉLANE [V PCG art. 710-2 ; C. com. L. 236-18, F01 § 1]. Chaque bénéficiaire reçoit, par **transmission universelle**, tous les actifs et toutes les dettes de la branche qui lui est attribuée, y compris la créance sur CISTRANE et les dettes fiscales que le traité rattache à la branche savons. OLIVALANE est **dissoute sans liquidation**. Ses actionnaires reçoivent des actions émises par chaque bénéficiaire, par augmentation de capital, et, pour CIRÉLANE, une soulte en numéraire ; leurs actions OLIVALANE disparaissent. OLIVALANE ne conserve aucune activité : la scission est **totale**.

**Distinction avec deux apports partiels d'actif (0,5 pt).** Dans un apport partiel d'actif, c'est la société apporteuse elle-même qui reçoit les titres de la bénéficiaire, et elle continue d'exister [V PCG art. 710-2, F01 § 1]. Avec deux apports, OLIVALANE survivrait comme société détenant des actions CISTRANE et CIRÉLANE, inscrites en titres de participation ; pour que ses actionnaires les reçoivent, il faudrait ensuite la dissoudre, la liquider et partager l'actif. La scission réalise en une seule opération la transmission des deux branches et l'attribution des actions aux actionnaires.

**Référentiel (0,25 pt).** Ce n'est pas une acquisition de titres : les bénéficiaires reçoivent un patrimoine et le rémunèrent par leurs propres actions. L'enregistrement relève, dans les comptes individuels des trois sociétés, du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe la valeur d'inscription des apports [V art. 710-1 et 720-1, F01 § 1]. Le nombre d'actions se calcule sur les valeurs d'échange fournies, indépendamment de ces règles [V art. 740-1, F01 § 1].

**Contrôle, sens et mode d'évaluation de chaque apport (1,25 pt)**
- *Situation de contrôle (0,25 pt).* OLIVALANE est contrôlée de manière exclusive par AUDIBERNE Participations (70 % des droits de vote), CISTRANE par TÉVERANE Holding (70 %) et CIRÉLANE par ORMELIN Participations (75 %). Aucune des trois sociétés ne détient d'actions d'une autre et les trois holdings n'ont aucun lien en capital : ni contrôle de l'une par l'autre, ni mère commune. Les deux apports sont réalisés **sous contrôle distinct** [V PCG art. 741-1 et 741-2, F01 § 2.1]. Aucun accord entre actionnaires ne crée de contrôle partagé.
- *Apport de la branche savons à CISTRANE (0,5 pt).* Après l'opération, TÉVERANE Holding détient 56 % de CISTRANE (voir 2.3 d) : l'actionnaire principal de la bénéficiaire, bien que dilué, **conserve le contrôle** ; AUDIBERNE Participations perd le contrôle de la branche savons et ne détient que 14 % de CISTRANE. L'apport est **à l'endroit** : CISTRANE est l'initiatrice, la branche savons la cible [V art. 742-1, F01 § 2.2]. Contrôle distinct et opération à l'endroit : **valeur réelle** [V art. 743-1, cas 4, F01 § 2.3].
- *Apport de la branche bougies à CIRÉLANE (0,5 pt).* Après l'opération, ORMELIN Participations détient 56,25 % de CIRÉLANE et en **conserve le contrôle** ; AUDIBERNE Participations n'en détient que 17,50 % et ne prend pas le contrôle. L'apport est **à l'endroit**, lui aussi : **valeur réelle** [V art. 742-1 et 743-1, cas 4, F01 § 2.2 et 2.3]. Chaque apport doit être analysé séparément, car chaque branche est rémunérée par une société dont l'actionnariat évolue différemment ; ici, les deux analyses conduisent au même mode d'évaluation.

**Régime fiscal de faveur (1,25 pt)**
- *Conditions et appréciation (0,5 pt).* Les trois sociétés sont passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1]. La scission bénéficie **de plein droit, c'est-à-dire sans agrément**, du régime de l'art. 210 A si la société scindée comporte **au moins deux branches complètes d'activité** et si chaque bénéficiaire reçoit une ou plusieurs de ces branches ; depuis le 01/01/2018, aucun engagement de conservation des titres n'est exigé dans ce cas [V CGI art. 210 B-1 ; BOI-IS-FUS-20-30-10 § 70, F02 § 1 et corrections du 22/10/2026]. La branche complète est l'ensemble des actifs et passifs d'une division qui constituent une exploitation autonome, capable de fonctionner par ses propres moyens [V BOI-IS-FUS-20-20 § 10, F02 § 1]. Les deux conditions sont remplies : les deux métiers sont réellement exercés dans deux divisions distinctes, avec leurs installations, leur personnel, leurs fournisseurs, leur clientèle et leurs tâches administratives ; chacune est transmise avec tous ses actifs et toutes ses dettes, et non en éléments isolés ; chaque bénéficiaire reçoit une branche.
- *Effets pour OLIVALANE (0,5 pt).* Les plus-values dégagées sur les éléments transmis (946 000 € au total : 740 000 € sur la branche savons et 206 000 € sur la branche bougies, voir 2.4) **ne sont pas soumises à l'impôt sur les sociétés** [V CGI art. 210 A-1, F02 § 2]. Sous le régime de droit commun, l'opération serait traitée comme une cessation d'entreprise et ces plus-values seraient imposées immédiatement [V BOI-IS-FUS-10-10-10 § 1, F02 § 2]. En revanche, le **résultat de la période** du 1er janvier au 30 avril 2027 reste imposé chez OLIVALANE, quel que soit le régime, comme pour une fusion : l'impôt de 20 000 € est déjà compris dans les dettes fiscales [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2]. La date d'effet étant celle de la réalisation, aucune fraction de ce résultat n'est reportée sur les bénéficiaires.
- *Effets pour les bénéficiaires (0,25 pt).* CISTRANE et CIRÉLANE prennent les engagements de l'art. 210 A-3 [V F02 § 4] : plus-values futures sur les éléments non amortissables calculées d'après leur valeur fiscale chez OLIVALANE, réintégration étalée des plus-values sur biens amortissables, inscription fiscale des stocks à leur valeur chez OLIVALANE. Ces impositions futures justifient la **provision pour impôts différés intégrée à l'apport** (voir 2.2) [V F01 § 3.3 ; F02 § 6].

---

### 2.2 Valeur réelle et composition des apports (3 pts)

**a) Branche savons (2,5 pts)**

*Éléments identifiés figurant au bilan (0,75 pt)*

| Élément | Valeur nette comptable | Valeur réelle | Écart |
|---|---:|---:|---:|
| Terrain | 150 000 | 270 000 | + 120 000 |
| Constructions | 700 000 | 980 000 | + 280 000 |
| Matériels industriels | 360 000 | 440 000 | + 80 000 |
| Matières premières | 120 000 | 120 000 | 0 |
| Produits finis | 180 000 | 220 000 | + 40 000 |
| Clients | 260 000 | 260 000 | 0 |
| Disponibilités | 90 000 | 90 000 | 0 |
| **Actifs identifiés** | **1 860 000** | **2 380 000** | **+ 520 000** |
| Dettes (500 000 + 210 000 + 50 000 + 40 000) | 800 000 | 800 000 | 0 |

*Élément identifié ne figurant pas au bilan (0,25 pt).* En valeur réelle, l'apport comprend les éléments identifiés figurant ou non au bilan de la société qui transmet, dont les provisions pour retraites et les impôts différés [V art. 744-1, F01 § 3.1] : engagements de retraite de **40 000 €**.

*Provision pour impôts intégrée à l'apport (1 pt).* Le régime de faveur reporte chez CISTRANE l'imposition des plus-values sur biens amortissables (réintégration étalée) et du profit sur produits finis (inscrits fiscalement à leur valeur chez OLIVALANE) : l'écart entre leur valeur d'apport et leur valeur fiscale est une différence temporaire [V corrigé du sujet zéro, Q 2.4, F01 § 3.3 ; F02 § 6].

| Élément | Base | Impôt différé (25 %) |
|---|---:|---:|
| Plus-value sur constructions | + 280 000 | + 70 000 |
| Plus-value sur matériels industriels | + 80 000 | + 20 000 |
| Plus-value sur produits finis | + 40 000 | + 10 000 |
| Engagements de retraite (déductibles au versement) | – 40 000 | – 10 000 |
| **Total net : passif d'impôt différé** | **+ 360 000** | **+ 90 000** |

Pas d'impôt différé sur le terrain (hypothèse de l'annexe 2.3 : bien non amortissable que CISTRANE n'envisage pas de céder), ni sur le fonds commercial, élément résiduel [V F01 § 3.3]. Le solde net de **90 000 €** est inscrit en **provision pour impôts (compte 1523)**.

*Actif net identifié, fonds commercial et composition de l'apport (0,5 pt)*

| | Montant |
|---|---:|
| Actifs identifiés | 2 380 000 |
| – Dettes | – 800 000 |
| – Engagements de retraite | – 40 000 |
| – Provision pour impôts (impôt différé net) | – 90 000 |
| **Actif net réel identifié** | **1 450 000** |
| Fonds commercial (1 800 000 – 1 450 000) | 350 000 |
| **Valeur réelle globale de l'apport** | **1 800 000** |

Le fonds commercial (clientèle et savoir-faire de la division, non inscrits au bilan d'OLIVALANE) est l'écart positif entre la valeur globale de l'apport et l'actif net identifié ; il figure au traité sur la ligne « fonds commercial » et est repris au compte 207 [V art. 744-1, F01 § 3.1]. Contrôle : 1 060 000 (actif net comptable) + 520 000 – 40 000 – 90 000 = 1 450 000 €.

**b) Branche bougies (0,5 pt).** L'apport étant évalué à la valeur réelle (voir 2.1), CIRÉLANE l'inscrit pour sa **valeur réelle globale, 616 000 €**, égale à sa valeur d'échange (annexe 2.4). L'actif net comptable de la branche est de 630 000 – 220 000 = **410 000 €** : l'écart de **206 000 €** correspond aux plus-values sur les éléments identifiés, diminuées de l'impôt différé correspondant, et au fonds commercial de la branche, dont le détail n'est pas demandé. La valeur d'apport couvre largement l'augmentation de capital de CIRÉLANE (200 000 €, voir 2.3).

---

### 2.3 Actions émises, parités, soulte et répartition du capital (5 pts)

**a) CISTRANE (1,25 pt)**
- Valeur d'échange unitaire : 7 200 000 / 150 000 = **48 €** (0,25 pt).
- Dans une scission, le nombre d'actions se calcule directement à partir de la valeur d'échange de la branche [S guide p. imprimée 163, d'après `programme/perimetre_ue4.yaml`, compétence 1.2.a] : 1 800 000 / 48 = **37 500 actions** (0,25 pt).
- Parité : 37 500 / 40 000 = **15 actions CISTRANE pour 16 actions OLIVALANE** (valeur de la branche savons par action OLIVALANE : 1 800 000 / 40 000 = 45 € ; 45 / 48 = 15 / 16). Les avoirs des trois actionnaires (28 000, 8 000 et 4 000 actions) sont des multiples de 16 : il n'y a pas de rompus. Contrôle : 15 × 48 = 720 € = 16 × 45 € (0,25 pt).
- Augmentation de capital : 37 500 × 10 = **375 000 €** ; prime de scission : 1 800 000 – 375 000 = **1 425 000 €**, avant imputation des frais (voir 2.6) (0,5 pt).

**b) CIRÉLANE : parité exacte, parité du traité et soulte (2 pts)**
- *Valeur unitaire et nombre exact (0,25 pt).* 1 800 000 / 60 000 = **30 €** ; 616 000 / 30 = **20 533,33 actions** : la valeur de la branche ne correspond pas à un nombre entier d'actions.
- *Parité exacte et motif de l'arrondi (0,5 pt).* Valeur de la branche bougies par action OLIVALANE : 616 000 / 40 000 = 15,40 € ; parité exacte 15,40 / 30 = **77 actions CIRÉLANE pour 150 actions OLIVALANE**. Elle est inapplicable : 40 000 × 77 / 150 = 20 533,33 n'est pas entier, et aucun actionnaire ne détient un multiple de 150 actions (AUDIBERNE Participations devrait recevoir 14 373,33 actions) : chacun aurait des **rompus**. Le projet de traité retient une parité simple, 1 pour 2, que chaque actionnaire peut appliquer à toutes ses actions (avoirs pairs), et compense l'arrondi par une soulte.
- *Actions émises et soulte (0,5 pt).* 40 000 × 1 / 2 = **20 000 actions** ; soulte = valeur de la branche – valeur des actions remises = 616 000 – 20 000 × 30 = **16 000 €**, soit 0,40 € par action OLIVALANE (0,80 € pour un lot de 2 actions).
- *Contrainte légale (0,25 pt).* La soulte ne peut dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-18 al. 3 ; même plafond qu'en fusion, L. 236-1 al. 3, F01 § 4] : 10 % × 20 000 × 10 = **20 000 €**. La soulte de 16 000 € (80 % du plafond) est **légale**. Par lot : 0,80 € pour un plafond de 10 % × 10 = 1 €.
- *Équité (0,25 pt).* Valeur des actions remises + soulte = 20 000 × 30 + 16 000 = 616 000 € = valeur de la branche (40 000 × 15,40) [V méthode du corrigé du sujet zéro, F01 § 4]. Après l'opération, l'action CIRÉLANE vaut (1 800 000 + 616 000 – 16 000) / 80 000 = **30 €** : ni les associés de CIRÉLANE ni ceux d'OLIVALANE ne s'enrichissent au détriment des autres.
- *Augmentation de capital et prime (0,25 pt).* Augmentation de capital : 20 000 × 10 = **200 000 €** ; prime de scission = 616 000 – 200 000 – 16 000 = **400 000 €** [V F01 § 4 et § 9].

**c) Proposition de M. ESCOULIN (0,75 pt).** Avec 2 actions CIRÉLANE pour 5 actions OLIVALANE : 40 000 × 2 / 5 = 16 000 actions, soulte = 616 000 – 16 000 × 30 = **136 000 €**, pour un plafond de 10 % × 16 000 × 10 = **16 000 €** : la soulte dépasserait le plafond 8,5 fois, elle est **illégale** et la proposition ne peut pas être retenue (0,5 pt). Conseil (0,25 pt) : la loi limite la part en numéraire à un montant faible. Même en émettant le nombre minimal d'actions compatible avec le plafond (616 000 / (30 + 1) = 19 870,97, soit 19 871 actions), la soulte totale ne dépasserait pas 19 870 €, et ce nombre ne correspond à aucune parité simple. La parité 1 pour 2 du traité, avec 16 000 € de soulte, est à maintenir ; M. ESCOULIN en reçoit 1 600 €. S'il souhaite davantage de liquidités, il devra céder ultérieurement une partie des actions reçues. La solution préserve aussi la trésorerie de CIRÉLANE.

**d) Répartition du capital et contrôle après l'opération (1 pt)**

CISTRANE — 150 000 + 37 500 = 187 500 actions (0,5 pt) :

| Actionnaire | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| TÉVERANE Holding | 105 000 | 70,00 % | 105 000 | 56,00 % |
| Autres actionnaires de CISTRANE | 45 000 | 30,00 % | 45 000 | 24,00 % |
| AUDIBERNE Participations (28 000 × 15 / 16) | – | – | 26 250 | 14,00 % |
| Mme VIGNASSE (8 000 × 15 / 16) | – | – | 7 500 | 4,00 % |
| M. ESCOULIN (4 000 × 15 / 16) | – | – | 3 750 | 2,00 % |
| **Total** | **150 000** | **100 %** | **187 500** | **100 %** |

CIRÉLANE — 60 000 + 20 000 = 80 000 actions (0,5 pt) :

| Actionnaire | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| ORMELIN Participations | 45 000 | 75,00 % | 45 000 | 56,25 % |
| Autres associés de CIRÉLANE | 15 000 | 25,00 % | 15 000 | 18,75 % |
| AUDIBERNE Participations (28 000 × 1 / 2) | – | – | 14 000 | 17,50 % |
| Mme VIGNASSE (8 000 × 1 / 2) | – | – | 4 000 | 5,00 % |
| M. ESCOULIN (4 000 × 1 / 2) | – | – | 2 000 | 2,50 % |
| **Total** | **60 000** | **100 %** | **80 000** | **100 %** |

Chaque action donnant une voix, les droits de vote suivent la même répartition. TÉVERANE Holding garde la majorité des droits de vote de CISTRANE et ORMELIN Participations celle de CIRÉLANE : chacune **conserve le contrôle exclusif** de sa société, ce qui confirme l'analyse de 2.1.

---

### 2.4 Écritures chez OLIVALANE au 30 avril 2027 (3 pts)

**A1 — Transmission de la branche savons à CISTRANE (1 pt).** OLIVALANE sort les éléments de la branche pour leurs valeurs comptables (valeurs brutes et amortissements) et constate sa créance sur CISTRANE pour la valeur de l'apport.

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – CISTRANE, compte d'apport | 1 800 000 | |
| 28131 Amortissements des bâtiments | 500 000 | |
| 28154 Amortissements des matériels industriels | 540 000 | |
| 164 Emprunts auprès des établissements de crédit | 500 000 | |
| 401 Fournisseurs | 210 000 | |
| 43 Sécurité sociale et autres organismes sociaux | 50 000 | |
| 44 État et autres collectivités publiques | 40 000 | |
| 211 Terrains | | 150 000 |
| 2131 Bâtiments | | 1 200 000 |
| 2154 Matériels industriels | | 900 000 |
| 31 Matières premières et fournitures | | 120 000 |
| 355 Produits finis | | 180 000 |
| 411 Clients | | 260 000 |
| 512 Banques | | 90 000 |
| 778 Autres produits exceptionnels (résultat de scission) | | 740 000 |
| **Total** | **3 640 000** | **3 640 000** |

**A2 — Transmission de la branche bougies à CIRÉLANE (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – CIRÉLANE, compte d'apport | 616 000 | |
| 28154 Amortissements des matériels industriels | 220 000 | |
| 164 Emprunts auprès des établissements de crédit | 60 000 | |
| 401 Fournisseurs | 120 000 | |
| 43 Sécurité sociale et autres organismes sociaux | 40 000 | |
| 2154 Matériels industriels | | 400 000 |
| 31 Matières premières et fournitures | | 130 000 |
| 355 Produits finis | | 110 000 |
| 411 Clients | | 150 000 |
| 512 Banques | | 60 000 |
| 778 Autres produits exceptionnels (résultat de scission) | | 206 000 |
| **Total** | **1 056 000** | **1 056 000** |

**Résultat de scission (0,25 pt).** OLIVALANE transmet chaque branche pour la valeur d'apport retenue au traité ; le résultat est l'écart avec l'actif net comptable de la branche : branche savons 1 800 000 – 1 060 000 = **+ 740 000 €** ; branche bougies 616 000 – 410 000 = **+ 206 000 €**. Il est présenté en résultat exceptionnel (compte 778), la scission étant pour OLIVALANE un événement majeur et inhabituel [V PCG art. 513-5 ; hypothèse de l'annexe 2.4, F01 § 9]. Sous le régime de faveur, ces 946 000 € ne sont pas imposés (voir 2.1) : aucune charge d'impôt n'est à constater.

**A3 — Réception des actions et de la soulte (0,5 pt).** Les actions sont reçues pour leur valeur d'échange et ne sont détenues que le temps de leur attribution : elles transitent par le compte 503 Actions.

| Compte | Débit | Crédit |
|---|---:|---:|
| 503 Actions CISTRANE (37 500 × 48) | 1 800 000 | |
| 503 Actions CIRÉLANE (20 000 × 30) | 600 000 | |
| 512 Banques (soulte) | 16 000 | |
| 467 CISTRANE, compte d'apport | | 1 800 000 |
| 467 CIRÉLANE, compte d'apport | | 616 000 |

**A4 et A5 — Droits des actionnaires et attribution (0,5 pt).** Les capitaux propres, augmentés du résultat de scission, représentent les droits des actionnaires : 1 470 000 + 946 000 = 2 416 000 € = 1 800 000 + 616 000.

A4 :

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 1 000 000 | |
| 1061 Réserve légale | 100 000 | |
| 1068 Autres réserves | 310 000 | |
| 120 Résultat de l'exercice (60 000 + 946 000) | 1 006 000 | |
| 456 Associés – AUDIBERNE Participations (70 %) | | 1 691 200 |
| 456 Associés – Mme VIGNASSE (20 %) | | 483 200 |
| 456 Associés – M. ESCOULIN (10 %) | | 241 600 |

A5 : AUDIBERNE Participations reçoit 26 250 actions CISTRANE (1 260 000 €), 14 000 actions CIRÉLANE (420 000 €) et 11 200 € ; Mme VIGNASSE 7 500 actions CISTRANE, 4 000 actions CIRÉLANE et 3 200 € ; M. ESCOULIN 3 750 actions CISTRANE, 2 000 actions CIRÉLANE et 1 600 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – AUDIBERNE Participations | 1 691 200 | |
| 456 Associés – Mme VIGNASSE | 483 200 | |
| 456 Associés – M. ESCOULIN | 241 600 | |
| 503 Actions CISTRANE | | 1 800 000 |
| 503 Actions CIRÉLANE | | 600 000 |
| 512 Banques (soulte) | | 16 000 |

Après ces écritures, tous les comptes d'OLIVALANE sont soldés.

---

### 2.5 Écritures de base chez CISTRANE et chez CIRÉLANE au 30 avril 2027 (4,5 pts)

**a) CISTRANE**

**A6 — Augmentation de capital (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (OLIVALANE) | 1 800 000 | |
| 101 Capital (37 500 × 10) | | 375 000 |
| 1042 Primes de fusion (prime de scission) | | 1 425 000 |

**A7 — Réalisation de l'apport à la valeur réelle (2 pts).** Les éléments sont inscrits à leur valeur réelle, sans reprise des amortissements d'OLIVALANE ; la provision pour retraites, la provision pour impôts et le fonds commercial sont inscrits [V art. 744-1, F01 § 3.1 et § 9]. Barème : actifs identifiés (0,75), fonds commercial (0,25), provisions 1521 et 1523 (0,5), dettes et compte d'apport (0,5).

| Compte | Débit | Crédit |
|---|---:|---:|
| 207 Fonds commercial | 350 000 | |
| 211 Terrains | 270 000 | |
| 2131 Bâtiments | 980 000 | |
| 2154 Matériels industriels | 440 000 | |
| 31 Matières premières et fournitures | 120 000 | |
| 355 Produits finis | 220 000 | |
| 411 Clients (dont créance sur CISTRANE : 48 000) | 260 000 | |
| 512 Banques | 90 000 | |
| 1521 Provisions pour pensions et obligations similaires | | 40 000 |
| 1523 Provisions pour impôts | | 90 000 |
| 164 Emprunts auprès des établissements de crédit | | 500 000 |
| 401 Fournisseurs | | 210 000 |
| 43 Sécurité sociale et autres organismes sociaux | | 50 000 |
| 44 État et autres collectivités publiques | | 40 000 |
| 4561 Associés – Comptes d'apport en société (OLIVALANE) | | 1 800 000 |
| **Total** | **2 730 000** | **2 730 000** |

**b) CIRÉLANE**

**A8 — Augmentation de capital et soulte due (1,25 pt).** La soulte fait partie de la rémunération de l'apport : elle diminue la prime de scission [V F01 § 4 et § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (OLIVALANE) | 616 000 | |
| 101 Capital (20 000 × 10) | | 200 000 |
| 1042 Primes de fusion (616 000 – 200 000 – 16 000) | | 400 000 |
| 468 Divers comptes créditeurs – soulte à verser | | 16 000 |

**A9 — Versement de la soulte (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 468 Divers comptes créditeurs – soulte à verser | 16 000 | |
| 512 Banques | | 16 000 |

La réalisation de l'apport (actifs et passifs de la branche bougies à leur valeur réelle, au crédit du compte 4561 pour 616 000 €) n'est pas demandée.

---

### 2.6 Écritures complémentaires chez CISTRANE (2,5 pts)

**A10 — Créance réciproque (1,25 pt).** La branche savons comprend une créance de 48 000 € sur CISTRANE, que CISTRANE a inscrite en dette fournisseurs. En recevant la branche, CISTRANE devient à la fois créancière et débitrice de la même obligation : la créance et la dette s'éteignent par **confusion** [V C. civ. art. 1349, F01 § 8]. Il s'agit d'une opération réciproque existant à la date de réalisation, qui est aussi la date d'effet. Barème : justification (0,5), écriture (0,75).

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette envers OLIVALANE) | 48 000 | |
| 411 Clients (créance reçue sur CISTRANE) | | 48 000 |

**A11 — Frais de scission (1,25 pt).** Les frais de fusion et de scission peuvent être imputés sur la prime [V PCG art. 212-9, F01 § 7], pour leur montant net d'impôt [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 40 000 × 75 % = **30 000 €** ; l'économie d'impôt de 10 000 € diminue l'impôt sur les sociétés 2027 de CISTRANE. Barème : justification et calcul (0,5), écriture (0,75).

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (40 000 × 75 %) | 30 000 | |
| 444 État – Impôts sur les bénéfices (40 000 × 25 %) | 10 000 | |
| 512 Banques | | 40 000 |

Prime de scission restante : 1 425 000 – 30 000 = **1 395 000 €**.

---

### 2.7 Note au président de CISTRANE (3 pts)

**a) Capitaux propres et effets sur les comptes de CISTRANE (1,5 pt)**

*Capitaux propres juste après la scission (1 pt)*

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (187 500 actions × 10) | 1 500 000 | + 375 000 | 1 875 000 |
| Primes d'émission | 300 000 | | 300 000 |
| Prime de scission | 0 | + 1 425 000 – 30 000 | 1 395 000 |
| Réserve légale | 150 000 | | 150 000 |
| Autres réserves | 2 950 000 | | 2 950 000 |
| Report à nouveau | 100 000 | | 100 000 |
| **Total** | **5 000 000** | **+ 1 770 000** | **6 770 000** |

Contrôle : + 1 770 000 = valeur de l'apport (1 800 000) – frais nets d'impôt (30 000). Barème : capital (0,25), prime (0,5), total et contrôle (0,25).

*Effets sur les comptes (0,5 pt).* Avant le paiement des frais, l'actif s'accroît de 2 682 000 € (2 730 000 – 48 000 éteints par confusion) ; le paiement des frais de scission le diminue de 40 000 €, dont 10 000 € sont compensés par la baisse de l'impôt sur les sociétés 2027. Le fonds commercial de 350 000 € est présumé à durée d'utilisation non limitée et donc non amorti, mais il est à déprécier si sa valeur actuelle devient inférieure à sa valeur comptable [V PCG art. 214-3, F01 § 5.5]. Les constructions et les matériels sont amortis sur leur valeur d'apport (980 000 et 440 000 €), plus élevée que leur valeur chez OLIVALANE : les dotations aux amortissements augmentent. Les produits finis, inscrits pour 220 000 €, réduiront la marge dégagée à leur vente. Les dettes de CISTRANE augmentent de 752 000 € (800 000 € de dettes reçues, dont 500 000 € d'emprunts, moins sa propre dette de 48 000 € envers OLIVALANE, éteinte par confusion) ; s'y ajoutent une provision pour retraites de 40 000 € et une provision pour impôts de 90 000 €, qui sera reprise à mesure que les plus-values seront réintégrées. Contrôle : 2 682 000 – 752 000 – 40 000 – 90 000 – 30 000 de frais nets = 1 770 000 €, variation des capitaux propres.

**b) Enjeux pour les parties prenantes (1,5 pt)**
- *Actionnaires de CISTRANE (0,5 pt).* TÉVERANE Holding passe de 70 % à 56 % des droits de vote : elle reste majoritaire et garde la direction de CISTRANE ; les autres actionnaires passent de 30 % à 24 %, et les anciens actionnaires d'OLIVALANE détiennent 20 % du capital, dont 14 % pour AUDIBERNE Participations. La dilution porte sur les droits de vote, non sur la valeur : les actions nouvelles étant émises à leur valeur d'échange, l'action CISTRANE vaut toujours (7 200 000 + 1 800 000) / 187 500 = **48 €**. Les capitaux propres comptables par action passent de 33,33 € à 36,11 € (6 770 000 / 187 500).
- *Créanciers de la branche savons (0,5 pt).* Approche financière (les aspects juridiques ne sont pas à traiter). Les prêteurs, les fournisseurs, les organismes sociaux et l'administration, créanciers de la branche (800 000 €), ont désormais pour débitrice CISTRANE, dont les capitaux propres atteignent 6 770 000 €, contre 1 470 000 € pour OLIVALANE : leur débiteur a une surface financière bien plus large. CISTRANE supporte en contrepartie 500 000 € d'emprunts supplémentaires et a décaissé 40 000 € de frais ; une partie de l'actif reçu est un fonds commercial de 350 000 €, dont la valeur dépend de la poursuite de l'activité.
- *Administration fiscale (0,5 pt).* CISTRANE s'est engagée dans le traité à respecter les obligations du régime de faveur [V CGI art. 210 A-3, F02 § 2 et § 4] : réintégrer par parts égales la plus-value sur constructions sur **15 ans** (280 000 / 15 = **18 667 €** par an ; elle représente 77,78 % de la plus-value nette sur biens amortissables, en deçà du seuil de 90 %) et celle sur matériels sur **5 ans** (80 000 / 5 = **16 000 €** par an), soit 34 667 € par an pendant 5 ans et environ 8 667 € d'impôt par an ; imposer le profit de 40 000 € sur les produits finis lors de leur vente, puisqu'ils sont inscrits fiscalement à 180 000 € ; calculer les plus-values futures sur le terrain et sur le fonds commercial d'après leur valeur fiscale chez OLIVALANE (150 000 € et zéro). En contrepartie, les amortissements déductibles sont calculés sur la valeur d'apport. CISTRANE acquitte aussi l'impôt de 20 000 € dû par OLIVALANE sur le résultat de sa dernière période, compris dans les dettes fiscales reçues. La provision pour impôts de 90 000 € traduit ces impositions futures, diminuées de l'économie attendue sur les retraites.

Grille de niveaux pour b) : 0 (absence ou idées sans lien avec le cas) ; 0,5 (une partie prenante traitée) ; 1 (deux parties prenantes, ou trois sans chiffres) ; 1,5 (trois parties prenantes, idées chiffrées et reliées au cas).

---

### Réponses tolérées
- **2.1** : sens de l'opération justifié par la seule comparaison des droits de vote de TÉVERANE Holding et d'ORMELIN Participations avant et après, sans recours aux notions d'initiatrice et de cible.
- **2.2** : présentation séparée des impôts différés passifs (100 000 €, base 400 000 €) et actifs (10 000 €, base 40 000 €), si le solde net de 90 000 € est retenu dans l'apport.
- **2.3 a et b** : calcul par la parité (45 / 48 = 15 / 16, puis 40 000 × 15 / 16) plutôt que par le nombre d'actions ; plafond vérifié par lot de 2 actions OLIVALANE (0,80 € pour 1 €) plutôt qu'en total.
- **2.3 c** : conseil qui propose une autre parité simple légale, s'il vérifie le nombre entier d'actions et le plafond ; toute idée pertinente sur la trésorerie de CIRÉLANE ou la liquidité de M. ESCOULIN.
- **2.4** : compte 261, 50 ou 508 au lieu de 503 pour les actions reçues ; écritures A3 et A5 remplacées par une seule écriture (débit 456, crédit 467), si le candidat indique que les bénéficiaires remettent les actions et la soulte directement aux actionnaires ; compte 431 et 444 ou 447 au lieu de 43 et 44 ; écriture A4 qui solde d'abord le compte 778 vers le résultat.
- **2.5** : compte 1043 Primes d'apport au lieu de 1042 Primes de fusion, ou un sous-compte « prime de scission » de l'un ou l'autre ; A8 et A9 regroupées (soulte directement au crédit du 512) ; soulte portée au crédit d'un autre compte de tiers ; compte 431 et 444 ou 447 au lieu de 43 et 44.
- **2.6** : extinction de la créance réciproque présentée dans A7 (clients inscrits pour 212 000 €, fournisseurs de CISTRANE diminués de 48 000 €), si la confusion est expliquée ; frais en deux écritures (1042 / 512 pour 40 000 €, puis 444 / 1042 pour 10 000 €).
- **2.7** : la logique du candidat prévaut lorsque ses montants découlent d'une erreur antérieure correctement reportée [`JUR-F08`].

### Erreurs fréquentes (rapports du jury)
- `JUR-R05` Difficulté à s'adapter : un seul mode d'évaluation retenu pour toute la scission sans analyser chaque apport ; contrôle apprécié au niveau des familles plutôt que des holdings ; nombre d'actions de chaque bénéficiaire calculé sur la valeur globale d'OLIVALANE (2 416 000 €) au lieu de la valeur de la branche reçue ; reprise des amortissements d'OLIVALANE dans A7 malgré l'évaluation à la valeur réelle.
- `JUR-R01` Prime de scission mal calculée : oubli de la soulte chez CIRÉLANE (prime de 416 000 €), prime calculée sur l'actif net comptable de la branche, ou frais imputés pour leur montant brut (prime finale de 1 385 000 €).
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1, A2 et A7.
- `JUR-F07` Annexes mal exploitées : impôt différé calculé sur le terrain ou sur le fonds commercial ; engagements de retraite oubliés, avec leur impôt différé actif (provision pour impôts de 100 000 € et fonds commercial de 320 000 €) ; plus-value sur produits finis oubliée ; créance réciproque de 48 000 € non éliminée.
- Erreurs propres à ce cas :
  - plafond de la soulte calculé sur la valeur de la branche (10 % × 616 000 = 61 600 €), sur la valeur d'échange des actions remises ou sur le nominal des actions OLIVALANE, au lieu du nominal des actions CIRÉLANE attribuées ;
  - nombre d'actions CIRÉLANE arrondi (20 533) sans soulte ni parité applicable par chaque actionnaire ;
  - affirmation d'un engagement de conservation des titres pendant trois ans comme condition du régime de faveur : il n'existe plus depuis 2018 pour une scission portant sur des branches complètes ;
  - résultat de la période du 1er janvier au 30 avril 2027 présenté comme exonéré par le régime de faveur, ou résultat de scission soumis à l'impôt ;
  - usage des comptes 675 et 775, supprimés du PCG 2026, pour le résultat de scission chez OLIVALANE.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 710-1, 710-2, 720-1, 730-1 ; C. com. L. 236-18 | Champ du titre VII, définition de la scission et de l'apport partiel d'actif, inscription des apports, initiatrice et cible | [V] p. 81-82 ; Légifrance | F01 § 1 |
| PCG art. 740-1, 741-1, 741-2, 742-1, 743-1 | Nombre d'actions indépendant de l'évaluation des apports ; contrôle distinct ; apport à l'endroit ; valeur réelle (cas 4) | [V] p. 82-84 | F01 § 1 et § 2 |
| Guide pédagogique, compétence 1.2.a | Scission : nombre d'actions déterminé directement à partir de la valeur d'échange des apports | [S] p. imprimée 163 | `programme/perimetre_ue4.yaml` |
| PCG art. 744-1 ; comptes 207, 1521 et 1523 | Valeurs réelles des éléments identifiés, figurant ou non au bilan ; fonds commercial ; provisions | [V] p. 85, 134-135 | F01 § 3.1 et § 3.3 |
| Corrigé du sujet zéro, Q 2.4 | Méthode de l'impôt différé intégré à l'apport ; aucun impôt différé sur l'écart résiduel | [V] p. imprimée 216 | F01 § 3.3 |
| C. com. L. 236-1 al. 3 et L. 236-18 al. 3 | Soulte limitée à 10 % de la valeur nominale des actions attribuées, en fusion comme en scission | [V] Légifrance | F01 § 4 |
| Corrigé du sujet zéro (parité) | Équité : valeur des titres remis + soulte = valeur des titres reçus | [V] p. imprimée 214 | F01 § 4 |
| PCG art. 513-5 ; compte 778 | Résultat exceptionnel lié à un événement majeur et inhabituel | [V] p. 42-43 ; p. 148 | F01 § 9 |
| Comptes 778 (résultat de scission) et 503 (actions reçues par OLIVALANE) | Écritures chez OLIVALANE | Convention de rédaction (hypothèse de l'annexe 2.4 pour le 778) | F01 § 9 |
| PCG art. 214-3 | Fonds commercial présumé à durée d'utilisation non limitée | [V] p. 22-23 | F01 § 5.5 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion de la créance et de la dette réciproques | [V] | F01 § 8 |
| CGI art. 210 B-1 ; BOI-IS-FUS-20-30-10 § 70 ; BOI-IS-FUS-20-20 § 10 | Scission de plein droit sous le régime de faveur : au moins deux branches complètes, une au moins par bénéficiaire, sans engagement de conservation ; définition de la branche complète | [V] | F02 § 1 |
| CGI art. 210 A-1, 210 A-3 (a à e), 210 C-1 ; BOI-IS-FUS-10-10-10 § 1 ; BOI-IS-FUS-10-20-30 § 210 et 330 | Exonération des plus-values chez la société scindée, engagements des bénéficiaires, réintégration sur 15 et 5 ans, imposition du résultat de la dernière période | [V] | F02 § 2 et § 4 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Démission du prédécesseur ; durée des fonctions du cabinet nommé en remplacement ; démarches auprès du prédécesseur ; demande de la gérante et autorévision | `3.1.b` Nomination et cessation ; `3.1.c` Principes déontologiques | 3,5 |
| 3.2 Cadres d'exercice du commissaire aux comptes et du certificateur des informations de durabilité ; certification et assurance raisonnable, mission contractuelle d'assurance limitée | `3.1.a` Cadres d'exercice professionnel ; `3.2.a` Notion d'audit et typologie des missions | 4 |
| 3.3 Cycle immobilisations : risques et assertions, procédures, refus de communiquer le contrat, coût et dotation de l'unité d'extraction | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit ; `3.2.b` Moyens d'action du CAC | 6 |
| 3.4 Récapitulation des anomalies ; écritures ; opinion selon les corrections et la communication du contrat ; note de synthèse | `3.2.e` Portée des opinions ; `3.2.d` Démarche d'audit (supports) ; `3.2.c` Caractère significatif | 4,5 |
| 3.5 Architecture des ESRS et norme volontaire ; plafond de la chaîne de valeur | `3.3.a` Contexte et architecture des normes de durabilité | 3 |
| 3.6 Périmètre de reporting, coentreprise et contrôle opérationnel ; chaîne de valeur amont et impact matériel | `3.3.b` Principes de construction du reporting | 3 |
| 3.7 Objectifs, axes et nature de l'assurance ; place de l'axe relatif aux informations | `3.4.a` Objectifs de la mission et nature de l'assurance | 2 |
| 3.8 Procédures sur le périmètre et sur la chaîne de valeur | `3.4.b` Démarche | 2,5 |
| 3.9 Conclusion sur la conformité des informations et portée | `3.4.c` Portée des avis | 1,5 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Démission du prédécesseur, remplacement et demande de la gérante (3,5 pts)

**a. Démission, durée des fonctions et démarches auprès du prédécesseur (2 pts)**

*Appréciation de la démission (0,75 pt)*
- Le commissaire aux comptes exerce sa mission jusqu'à son terme. Il ne peut démissionner que pour un **motif légitime**, dont la liste est fermée : cessation définitive d'activité ; motif personnel impérieux ; **difficultés rencontrées dans l'accomplissement de la mission, lorsqu'il n'est pas possible d'y remédier** ; événement de nature à compromettre le respect des règles de la profession, notamment l'indépendance. Il joint à son dossier les éléments qui justifient sa démission et en informe la H2A en indiquant ses motifs [V code de déontologie art. 28 I et IV].
- Il ne peut pas démissionner pour se soustraire à l'émission de son opinion, ni dans des conditions qui causent un préjudice à l'entité ; il doit pouvoir justifier qu'il a analysé la situation [V art. 28 II].
- Application :
  - le motif invoqué n'est pas un simple désaccord sur un traitement comptable. Un désaccord de ce type ne justifie pas une démission : le commissaire aux comptes l'exprime dans son opinion, par une réserve ou un refus de certifier [S, application de l'art. 28 et de NEP rapport § 09-13] ;
  - le motif réel est le **refus répété de communiquer** le contrat et le budget de l'investissement, alors que le commissaire aux comptes peut se faire communiquer sur place toutes pièces utiles, notamment les contrats [V L. 821-60]. S'y ajoutent l'annonce que plus aucun document ne serait communiqué avant l'arrêté des comptes et le rejet du rôle même du commissaire aux comptes. Trois demandes écrites étaient restées sans effet : la difficulté paraît **sans remède**. C'est le motif du c) de l'art. 28 ;
  - les conditions de forme sont remplies : motifs exposés par écrit, H2A informée, justificatifs joints au dossier ;
  - le moment ne pose pas de difficulté : l'opinion sur les comptes de 2025 a été émise le 20/04/2026, avant la démission, et la démission, six mois avant la clôture de 2026, laissait le temps de désigner un successeur, ce qui a été fait le 15/09/2026.
  - Conclusion : la démission est fondée sur un **motif légitime** [S, application]. Les refus de la gérante pourraient d'ailleurs constituer le délit d'obstacle aux vérifications du commissaire aux comptes [V L. 821-6 3°] ; les suites que la loi attache à ce constat ne sont pas à développer.

*Durée des fonctions du cabinet (0,5 pt)*
- ARMÉLINE dépasse les trois seuils (total du bilan 23 900 000 € > 5 000 000 € ; chiffre d'affaires 28 000 000 € > 10 000 000 € ; 140 salariés > 50) : elle est tenue d'avoir un commissaire aux comptes et doit remplacer le démissionnaire [V L. 223-35 al. 2 ; D. 221-5, rendu applicable par D. 223-27]. Aucun suppléant n'ayant été désigné, ce sont les associés, organe analogue à l'assemblée générale ordinaire, qui désignent le successeur [V L. 821-40 I ; S, application à la SARL].
- Le commissaire aux comptes nommé en remplacement ne demeure en fonction que **jusqu'à l'expiration du mandat de son prédécesseur** [V L. 821-44 al. 2]. CALVANÈRE avait été désignée en 2022 pour les exercices 2022 à 2027 : le cabinet MARVEILLAN est en fonction jusqu'à la décision des associés qui statuera sur les comptes de **2027**. Il certifie les comptes de 2026 et de 2027.
- La mention de six exercices (2026 à 2031) du projet de la gérante est contraire à ce texte : la décision ne pouvait conférer que la durée restant à courir [S, application]. Un nouveau mandat de six exercices ne pourra être conféré qu'en 2028, à l'expiration de celui-ci [V L. 821-44 al. 1].
- Un suppléant n'est pas exigé : le cabinet est une société de commissaires aux comptes qui compte quatre associés (présentation) [V L. 821-40 I al. 3].

*Démarches auprès du prédécesseur et accès à ses informations (0,75 pt)*
- **Avant d'accepter**, le cabinet vérifie que la mission est compatible avec les exigences légales et le code. Il vérifie et consigne son indépendance et ses ressources et réunit les informations sur la structure, l'actionnariat, l'activité et le mode de direction de l'entité [V code de déontologie art. 21 ; L. 821-4 II]. Il analyse les prestations qu'il aurait rendues auparavant : il n'en a rendu aucune à ARMÉLINE [V art. 22]. Il apprécie aussi le fait qu'il assiste NÉROVALE, premier client d'ARMÉLINE, dans l'établissement de ses comptes consolidés : ce n'est pas une incompatibilité légale, puisque NÉROVALE n'a aucun lien en capital avec ARMÉLINE, mais le cabinet organise ses équipes et respecte strictement le secret professionnel [V L. 821-35 ; S, application].
- **Contact avec le prédécesseur** : le code impose expressément au successeur d'un commissaire aux comptes non renouvelé, et au suppléant qui succède à un démissionnaire, de s'assurer auprès du prédécesseur que son départ ne vise pas à contourner les obligations légales [V art. 26 I]. Le cabinet, désigné par les associés après une démission, n'est pas visé à la lettre. La démarche s'impose néanmoins au titre de l'acceptation : la lettre de CALVANÈRE révèle des refus de communication qui touchent à l'exercice même de la mission [S, application de l'art. 21]. Le cabinet interroge donc CALVANÈRE sur les motifs de sa démission, sur les documents refusés et sur les points en suspens.
- **Conséquences pour l'acceptation** : le cabinet peut accepter, en connaissance de cause, mais il intègre ces informations à son évaluation du risque, puisque l'attitude de la direction est un facteur de risque, et il précise dans sa lettre de mission les obligations d'information et d'accès de l'entité [V NEP lettre de mission § 3-8 ; NEP risques § 02].
- **Après sa désignation** : le commissaire aux comptes démissionnaire doit permettre à son successeur d'**accéder à toutes les informations et à tous les documents pertinents** concernant l'entité [V L. 821-44 al. 3]. Le cabinet consulte le dossier de travail de CALVANÈRE : dossier de l'exercice 2025, travaux sur l'acompte versé en 2025, demandes écrites relatives au contrat et réponses de la gérante.

**b. Demande de la gérante (1,5 pt)**

*Analyse (1 pt)*
- Pour ARMÉLINE, le cabinet intervient comme **commissaire aux comptes**. Sa qualité d'expert-comptable ne change rien : les règles d'indépendance du commissaire aux comptes s'appliquent à toute prestation qu'il fournirait à ARMÉLINE [V code de déontologie art. 5 ; L. 821-2 IV ; S, application].
- La décomposition de l'unité, les durées d'utilisation et les plans d'amortissement sont des **estimations** qui déterminent le coût, la dotation et la valeur nette de l'unité. Le cabinet devra les auditer à la clôture. S'il aidait à les arrêter, il se prononcerait sur des éléments résultant de sa propre prestation : c'est un **risque d'autorévision** [V code de déontologie art. 5 II, art. 19 I 2°].
- ARMÉLINE n'est pas une entité d'intérêt public. Le commissaire aux comptes ne peut pourtant pas accepter une prestation qui crée un risque d'autorévision sans mesure de sauvegarde appropriée [V L. 821-28 IV ; A. 821-55 § 15, 23-30]. Aucune sauvegarde n'est possible ici : même confiée à une autre équipe, la décomposition resterait l'œuvre du cabinet, et elle porte sur le point le plus risqué des comptes. Aux yeux d'un tiers objectif, raisonnable et informé, le cabinet aurait participé à l'établissement des comptes qu'il certifie [V A. 821-55 § 03, 11 ; S, application].
- La demande méconnaît aussi la répartition des rôles : la gérance arrête les comptes ; le commissaire aux comptes les certifie, sans s'immiscer dans la gestion [V L. 821-54 I]. Le but affiché, « éviter toute discussion à la clôture », revient à obtenir une validation préalable. C'est un nouvel indice du risque que présente l'attitude de la direction, à traiter avec esprit critique [V code de déontologie art. 6 ; S].

*Réponse de Mme CASTAGNIER (0,5 pt)*
- Elle **refuse** la prestation, par écrit, en en donnant les raisons.
- La décomposition et les plans relèvent d'ARMÉLINE : la responsable administrative et financière et le directeur technique disposent de l'annexe technique et des durées du constructeur ; ARMÉLINE peut aussi recourir à un autre professionnel.
- Dans le cadre de sa mission, Mme CASTAGNIER peut rappeler les règles générales du plan comptable général, comme la décomposition et le point de départ de l'amortissement, et faire part de ses observations sur les choix de la société lors de ses travaux, sans les élaborer à sa place [S, application].

**Réponses tolérées**
- Une démission jugée contestable, si le candidat soutient que les refus pouvaient être surmontés autrement (rappel écrit du délit d'obstacle, information des associés, réserve pour limitation) et qu'il applique les conditions de l'art. 28 : 0,5 pt sur 0,75.
- Pour les démarches, l'application directe de l'obligation de s'assurer auprès du prédécesseur, sans relever qu'elle ne vise pas à la lettre ce cas de succession.
- Pour la réponse à la gérante, la seule mention de l'autorévision et de la non-immixtion, sans le raisonnement sur les sauvegardes : 0,75 pt sur 1.

**Erreurs fréquentes**
- Retenir un mandat de six exercices pour le cabinet nommé en remplacement (`JUR-A05`).
- Admettre une démission pour simple désaccord avec la gérance, ou ignorer les conditions de forme et l'information de la H2A (`JUR-A06`).
- Accepter la prestation au motif que le cabinet est aussi expert-comptable, ou parce qu'ARMÉLINE n'est pas une entité d'intérêt public (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 21, 22, 26, 28 | Acceptation ; prestations antérieures ; succession ; démission | [V] ; application à ce cas de succession : [S] | F09 § 3.7, § 12 ; F10 § 5 |
| C. com. L. 223-35, D. 221-5, D. 223-27 ; L. 821-40, L. 821-44 | Obligation de désignation ; organe ; suppléant ; durée ; accès au dossier du prédécesseur | [V] ; application : [S] | F09 § 3.3-3.5, § 12 |
| C. com. L. 821-6 3°, L. 821-35, L. 821-60 | Délit d'obstacle ; secret ; communication des pièces | [V] | F09 § 5 ; F10 § 7 ; F11 § 2, 13.3 |
| Code de déontologie art. 5, 6, 19 ; L. 821-28 IV ; A. 821-55 § 03, 11, 15, 23-30 ; L. 821-2 IV, L. 821-54 I | Autorévision ; sauvegardes ; prestation ; non-immixtion | [V] ; application : [S] | F10 § 2.1, 3, 5, 12 ; F09 § 6 |
| NEP lettre de mission § 3-8 ; NEP risques § 02 | Lettre de mission ; facteurs de risque | [V] | F11 § 4.1, 7 |

### 3.2 Cadres d'exercice et nature des missions (4 pts)

**a. Cadres d'exercice et cabinet de conseil (2,5 pts)**

*Comparaison des cadres d'exercice (1,5 pt)*

| | Commissaire aux comptes (certification des comptes) | Professionnel qui certifie les informations en matière de durabilité |
|---|---|---|
| Qui | Personne physique ou société inscrite sur la **liste tenue par la H2A** [V L. 821-13 I] | Soit un **commissaire aux comptes inscrit sur une liste spéciale** [V L. 821-13 II], soit un **organisme tiers indépendant** (OTI) inscrit sur la liste de la H2A, au sein duquel exerce un **auditeur des informations en matière de durabilité**, personne physique inscrite, qui signe le rapport [V L. 822-1, L. 822-3, L. 822-4, L. 822-6] |
| Conditions d'accès | Honorabilité, **stage** de trois ans, **certificat d'aptitude** aux fonctions de commissaire aux comptes ou diplôme d'expertise comptable ; serment devant la cour d'appel ; formation continue [V L. 821-14, L. 821-23, L. 821-24] | Commissaire aux comptes : être inscrit, avoir accompli un **stage de huit mois** en durabilité et réussi une **épreuve** de certification des informations de durabilité [V L. 821-18 I]. OTI : personne morale **accréditée par le comité français d'accréditation** ; auditeur : honorabilité, master, stage de huit mois, épreuve [V L. 822-3, L. 822-4] |
| Instances | **H2A** : inscription, normes, contrôles, sanctions ; **CNCC** et **CRCC** : représentation et surveillance de la profession [V L. 820-1, L. 821-12] | **H2A** pour l'inscription, les normes, les contrôles et les sanctions ; accréditation des OTI par le comité français d'accréditation [V L. 820-1, L. 822-3] ; les commissaires aux comptes inscrits pour la durabilité relèvent aussi de leur CRCC [S] |
| Déontologie | Code de déontologie de la profession [V L. 821-36] | **Même code de déontologie**, indépendance comprise [V L. 822-7 ; code art. 1er II] |

Le cabinet MARVEILLAN réunit les deux qualités : Mme CASTAGNIER est inscrite sur les deux listes, et le rapport sur la durabilité est signé par un commissaire aux comptes personne physique inscrit sur la liste spéciale [V L. 821-26].

*Le cabinet de conseil (1 pt)*
- Si ARMÉLINE était tenue de faire certifier ses informations, seul un commissaire aux comptes inscrit sur la liste spéciale ou un OTI accrédité pourrait le faire [V L. 232-6-3 III ; L. 822-1 I]. Un cabinet de conseil ne le peut que s'il est lui-même un OTI accrédité, dont les auditeurs sont inscrits auprès de la H2A.
- ARMÉLINE publie volontairement : la vérification est une **mission contractuelle**, qu'aucun texte ne réserve à une profession [S, F12 § 11]. Mais NÉROVALE exige un professionnel **habilité** (annexe 3.6) : un cabinet qui n'est ni commissaire aux comptes inscrit pour la durabilité ni OTI accrédité ne répond pas à cette condition. Ses consultants ne sont soumis ni au code de déontologie ni aux contrôles de la H2A, et le mot « certifier » ne désigne alors aucune mission légale [S].
- Ce cabinet « accompagne » des parfumeurs. S'il a aidé à préparer des informations d'ARMÉLINE, il ne pourrait pas les vérifier sans **autorévision** [S, application du code de déontologie art. 5].
- Réponse : le choix appartient à ARMÉLINE, mais il ne peut se porter sur ce cabinet que s'il justifie de son accréditation d'OTI et de l'inscription de ses auditeurs. Le moindre coût ne compense pas le risque de voir NÉROVALE refuser le rapport.

**b. Certification et assurance raisonnable ; mission sur la durabilité (1,5 pt)**

*Certification des comptes (0,75 pt)*
- **Objectif** : le commissaire aux comptes certifie, en justifiant de ses appréciations, que les comptes annuels sont réguliers et sincères et donnent une image fidèle du résultat, de la situation financière et du patrimoine ; il exprime une **opinion** après un audit des comptes [V L. 821-53 al. 1 ; NEP principes § 01].
- **Assurance raisonnable** : assurance élevée, **mais non absolue**, que les comptes pris dans leur ensemble ne comportent pas d'anomalies significatives. Elle a des limites : sondages, limites des procédures de l'entité, éléments qui conduisent à des présomptions plutôt qu'à des certitudes [V NEP principes § 08-09]. La certification ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55]. Ce n'est donc pas une « garantie », contrairement à ce que croit M. VAUBRESSE.

*Comparaison avec la mission sur la durabilité (0,75 pt)*

| | Certification des comptes | Mission sur les informations de durabilité d'ARMÉLINE |
|---|---|---|
| Fondement | Mission **légale** [V L. 821-2 III, L. 821-53] | **Prestation contractuelle**, définie par la lettre de mission, car ARMÉLINE n'est pas tenue de publier [V L. 821-2 IV, R. 821-195 ; annexe 3.7] |
| Objet | Comptes annuels | Processus de détermination des informations et conformité des informations aux ESRS (annexe 3.7) |
| Assurance | **Raisonnable** ; opinion formulée de façon **positive** | **Limitée** : vérifications moindres en nature, en étendue et en durée ; conclusion de forme **négative** (aucune erreur, omission ou incohérence importante relevée) [V LD 2026, niveau d'assurance ; F13 § 2.3] |
| Rapport | Rapport sur les comptes annuels, destiné aux associés | Rapport distinct, conclusions **axe par axe**, remis à la gérance (annexe 3.7) |

La réponse à M. VAUBRESSE est donc négative : le rapport sur la durabilité donnera une assurance **moindre** que la certification des comptes.

**Réponses tolérées**
- Une comparaison rédigée plutôt qu'un tableau, si les critères sont traités.
- L'omission de la CRCC pour le professionnel de la durabilité.
- Une réponse qui admet le cabinet de conseil pour une mission purement contractuelle, si le candidat relève qu'il ne satisfait pas à l'exigence de NÉROVALE.

**Erreurs fréquentes**
- Présenter l'OTI comme une personne physique, ou ignorer l'accréditation (`JUR-A01`).
- Présenter la certification comme une garantie, ou attribuer la même assurance aux deux missions (`JUR-A01`, `JUR-A06`).
- Qualifier de certification légale la mission confiée par ARMÉLINE (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 820-1, L. 821-12 à L. 821-14, L. 821-18, L. 821-23, L. 821-24, L. 821-26, L. 821-36, L. 822-1, L. 822-3, L. 822-4, L. 822-6, L. 822-7, L. 232-6-3 III | Cadres d'exercice ; listes ; OTI ; instances ; déontologie | [V] | F09 § 1, 3.1-3.2, 4.1-4.3 ; F10 § 1 |
| C. com. L. 821-2, L. 821-53, L. 821-55, R. 821-195 ; NEP principes § 01, 08-09 | Mission légale et prestation ; objectif ; assurance raisonnable | [V] | F11 § 1.1-1.2, 13.2 |
| LD 2026, niveau d'assurance | Assurance limitée ; forme négative | [V] | F13 § 2.3 |

### 3.3 Cycle immobilisations (6 pts)

**a. Risques d'anomalies significatives et assertions (3 pts)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41 ; NEP éléments probants § 9]

*Évaluation du risque (0,5 pt)* : le **risque inhérent** est élevé.
- L'unité est une opération **non courante** et importante : 1 896 000 € de coût, soit 7,9 % du total du bilan ; sa valeur nette représente plus du quart des immobilisations corporelles nettes du projet.
- Son évaluation repose sur des **estimations** et des choix de la direction : coûts incorporés, décomposition, durées d'utilisation, valeur de revente des alambics. La position de la gérante (annexe 3.5) et ses refus montrent des **indices de biais** : ses choix sur les coûts incorporés et sur les alambics majorent le résultat de 190 000 € ; seul le plan unique de dix ans le minore, de 6 420 €.
- Les procédures de l'entité sont faibles : la gérante décide seule des investissements, a signé seule le contrat et en garde l'original ; les plans d'amortissement sont tenus sur tableur et validés par elle.
- Des événements accroissent le risque : livraison en retard d'un mois et négociation des pénalités, prix révisable, solde facturé en 2027, arrêt définitif des alambics, démission du prédécesseur.
- Sans test de l'efficacité des procédures, le risque au niveau des assertions correspond au risque inhérent [V NEP risques § 41] : le cabinet met en œuvre des **procédures de substance** et privilégie les éléments externes [V NEP réponses § 03-13].

*Risques et assertions (2,5 pts : 0,25 pt par couple pertinent, dans la limite de dix)*

| Élément | Risque | Assertion |
|---|---|---|
| Unité d'extraction (solde) | Unité non installée ou non en état de fonctionner | **Existence** |
| | Clause de réserve de propriété ou de transfert différé, inconnue faute de contrat | **Droits et obligations** |
| | Coûts non incorporables inscrits à l'actif : formation, montée en cadence, inauguration | **Évaluation et imputation** |
| | Coûts d'essais, nécessaires pour atteindre le rendement de la réception, qu'il faut maintenir à l'actif | **Évaluation et imputation** |
| | Prix révisé et pénalités de retard non pris en compte | **Évaluation** ; **exhaustivité** |
| | Solde de 5 % non comptabilisé alors que les réserves ont été levées le 18/12/2026 | **Exhaustivité** |
| Dotation aux amortissements (flux) | Plan unique de dix ans au lieu d'un plan par élément ; mauvaise date de départ | **Mesure** ; **séparation des exercices** (date de mise en service) |
| Charges et production immobilisée (flux) | Charges de l'exercice transférées à l'actif par le compte 722 | **Classification** ; **réalité** de la production immobilisée |
| Dettes fournisseurs d'immobilisations | Facture du solde datée de 2027 pour une dette née en 2026 | **Exhaustivité** ; **séparation des exercices** |
| Anciens alambics | Arrêt définitif sans dépréciation : valeur nette supérieure à la valeur de revente | **Évaluation et imputation** |
| | Alambics vendus ou mis au rebut sans être sortis de l'actif | **Existence** |
| Annexe | Méthodes d'amortissement, décomposition, dépréciation et engagement résiduel envers le constructeur non décrits | **Exhaustivité** ; **présentation et intelligibilité** |

**b. Procédures et position de la gérante (2 pts)**

*Procédures sur les immobilisations (1 pt)*
- **Inspection physique** de l'unité : visite de l'atelier, identification des trois éléments (plaques, numéros de série) par rapport à l'annexe technique, constat qu'elle produit ; inspection des alambics : arrêt effectif, état, présence dans l'atelier [V NEP éléments probants § 10].
- **Rapprochement** des factures SOLVÉRAN, de l'échéancier, des procès-verbaux et des relevés bancaires : le procès-verbal de réception du 30/09/2026 fixe la date à laquelle l'unité est en état de fonctionner et prévoit le solde de 5 % exigible à la levée des réserves ; le procès-verbal du 18/12/2026 rend ce solde exigible avant la clôture. L'examen des factures reçues en janvier 2027 fait apparaître la facture n° 4.
- **Production immobilisée** : rapprochement des 114 000 € portés au compte 722 avec les fiches de temps et de consommation, et contrôle de leur date par rapport à la réception. Les essais (32 000 €) sont antérieurs au 30/09/2026 ; la formation, la montée en cadence et l'inauguration sont postérieures.
- **Revue du plan d'amortissement** : comparaison avec la décomposition et les durées du constructeur, date de mise en service, recalcul (question c).
- **Alambics** : recherche d'un indice de perte de valeur, entretien avec M. PÉLISSIER, examen de l'offre de CUIVRERIE ROUSTAN et de l'estimation des frais de démontage ; calcul de la dépréciation.
- **Contrat** : lecture des clauses de prix, de révision, de pénalités, de transfert de propriété et de garantie ; **demande de confirmation** à SOLVÉRAN sur le prix révisé, les sommes facturées, le solde dû et les pénalités [V NEP confirmations § 4-5] ; **déclaration écrite** de la gérante [V NEP déclarations écrites § 6-7].

*Position de la gérante et moyens d'action (0,5 pt)*
- **Contrat** : le commissaire aux comptes se fait communiquer sur place toutes les pièces qu'il estime utiles, **notamment les contrats** [V L. 821-60]. Le secret ne peut lui être opposé, sauf par les auxiliaires de justice [V L. 821-61 al. 3] : une clause de confidentialité entre ARMÉLINE et SOLVÉRAN ne lui est pas opposable, et il est lui-même tenu au secret professionnel [V L. 821-35]. Le refus de communiquer les contrats est un délit d'obstacle [V L. 821-6 3°]. Mme CASTAGNIER le rappelle par écrit à la gérante et documente ses demandes ; si le refus persiste, elle en tire les conséquences dans son rapport aux associés (question 3.4) [S, application].
- **Interdiction de contacter SOLVÉRAN** : le commissaire aux comptes a la maîtrise de la sélection des tiers interrogés, de la rédaction, de l'envoi et de la réception des demandes [V NEP confirmations § 9]. Face à une opposition, il examine si elle repose sur des **motifs valables** et collecte des éléments sur ces motifs [V § 10]. La négociation des pénalités peut justifier de rédiger la demande avec soin, mais pas de l'interdire : c'est justement le montant des pénalités et du prix révisé que la confirmation doit établir. Le motif n'est pas valable [S, application].
- Il recueille, le cas échéant, des informations auprès des tiers qui ont accompli des opérations pour le compte de l'entité ; la communication de pièces détenues par eux suppose une autorisation de justice [V L. 821-61 al. 2]. Un constructeur qui vend une installation à ARMÉLINE n'entre pas clairement dans ce cas : la demande de confirmation reste la voie normale [S].

*Procédures alternatives (0,5 pt)*
- Contrat de prêt : prix de 1 800 000 € HT « révisable », qui confirme le prix de base et l'existence d'une clause de révision ; budget d'investissement approuvé par la gérante ; relevés bancaires (paiements des factures n° 1 à 3, puis de la facture n° 4 en 2027) ; procès-verbaux ; police d'assurance (valeur assurée de l'unité) ; correspondance avec SOLVÉRAN sur la négociation des pénalités.
- Ces procédures établissent le prix de base, les paiements, la date de réception et le solde dû. Elles ne permettent pas de connaître la formule de **révision du prix**, ni le montant des **pénalités** de retard dont ARMÉLINE pourrait bénéficier, ni les éventuelles clauses de propriété. Si le contrat n'est pas communiqué, il en résulte une **limitation** pour l'évaluation de l'unité et de la dette envers SOLVÉRAN [V NEP confirmations § 11-12 ; NEP rapport § 11].

**c. Coût et dotation 2026 de l'unité (1 pt)**

*Coût de l'unité (0,5 pt)* [V PCG art. 213-8, 213-10 à 213-13]

| Coût | Montant | Traitement | Motif |
|---|---:|---|---|
| Prix SOLVÉRAN (factures n° 1 à 4) | 1 800 000 | Incorporé | Prix d'achat, solde compris |
| Transport, levage et montage | 46 000 | Incorporé | Coût directement attribuable à la mise en place |
| Bureau de contrôle | 18 000 | Incorporé | Nécessaire à la mise en état de fonctionner |
| Essais du 01/09 au 29/09/2026 | 32 000 | Incorporé | Nécessaires pour atteindre le rendement attendu à la réception |
| Salaires des opérateurs en formation (octobre) | 28 000 | **Charge** | Frais internes, postérieurs à la réception : l'option ne vise que les frais externes de formation |
| Surconsommations de la montée en cadence | 54 000 | **Charge** | Coûts de l'utilisation effective, après la mise en état de fonctionner |
| Journée d'inauguration | 12 000 | **Charge** | Opération non nécessaire à la mise en état de fonctionner |
| **Coût de l'unité** | **1 896 000** | | contre 1 900 000 au projet de comptes |

*Décomposition et dotation (0,5 pt)* [V PCG art. 214-9, 214-12, 214-13] : les frais accessoires incorporables, soit 96 000 €, sont répartis au prorata du prix ; l'amortissement court à compter de la mise en service, le 01/10/2026, soit trois mois.

| Élément | Prix | Frais accessoires | Coût | Durée | Dotation 2026 |
|---|---:|---:|---:|---:|---:|
| Extracteurs et colonne de distillation | 1 260 000 | 67 200 | 1 327 200 | 15 ans | 22 120 |
| Récupération des solvants | 360 000 | 19 200 | 379 200 | 10 ans | 9 480 |
| Automates et supervision | 180 000 | 9 600 | 189 600 | 5 ans | 9 480 |
| **Total** | **1 800 000** | **96 000** | **1 896 000** | | **41 080** |

- Le projet de comptes retient 1 900 000 € et une dotation de 47 500 € (1 900 000 / 10 × 3/12). Le plan unique est contraire à la règle de décomposition : les trois éléments ont des durées d'utilisation différentes dès l'origine.
- **Anomalies** : coûts non incorporables de **94 000 €** inscrits à l'actif ; solde de **90 000 €** omis ; dotation **surévaluée de 6 420 €** (47 500 − 41 080). La date de départ de l'amortissement, en revanche, est exacte.

**Réponses tolérées**
- D'autres couples risque-assertion pertinents tirés des annexes.
- Une répartition des frais accessoires sur le seul élément principal, si elle est justifiée et que le reste du calcul est exact : 0,25 pt sur 0,5 pour la dotation.
- Le traitement des salaires de formation comme incorporables au titre de l'option, si le candidat ignore qu'elle ne vise que les frais externes : 0,25 pt sur 0,5 pour le coût.
- Le refus de la gérante jugé partiellement fondé pour le seul calendrier de la confirmation, si le candidat maintient la communication du contrat.

**Erreurs fréquentes**
- Confondre existence (solde) et réalité (flux), ou exhaustivité et séparation des exercices (`JUR-A01`).
- Incorporer les essais en charges, ou les coûts de montée en cadence à l'actif au motif qu'ils sont « nécessaires au projet » (`JUR-F07`, `JUR-A05`).
- Retenir la date de la facture pour rattacher le solde à 2027 (`JUR-A05`).
- Accepter l'interdiction de contacter le constructeur sans examiner son motif, ou n'en tirer aucune conséquence (`JUR-A05`, `JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 10-13 ; NEP risques § 02, 39-41 ; NEP réponses § 03-13 ; NEP éléments probants § 9-10 | Risque ; assertions ; techniques | [V] | F11 § 4.1, 4.3, 5, 6 |
| C. com. L. 821-6 3°, L. 821-35, L. 821-60, L. 821-61, L. 821-63 ; NEP confirmations § 4-5, 9-12 ; NEP déclarations écrites § 6-7 | Moyens d'action ; secret ; confirmation ; refus de la direction | [V] ; application : [S] | F09 § 5 ; F11 § 2, 6.3, 12.3, 13.3, 15.2 |
| PCG art. 213-8, 213-10 à 213-13 (p. 17-18) ; 214-9, 214-12, 214-13 (p. 24-25) | Coût d'entrée ; décomposition ; début de l'amortissement | [V] ; application aux coûts du cas : [S] | F11, ajout du 12/11/2026 |

### 3.4 Anomalies, écritures, opinion et note de synthèse (4,5 pts)

**a. Récapitulation et caractère significatif (1 pt)** [V NEP anomalies § 8, 11-12, 14 ; NEP caractère significatif § 9]

*Dépréciation des alambics* [V PCG art. 214-5, 214-6, 214-15 à 214-17] : l'arrêt définitif est un indice de perte de valeur, par changement du mode d'utilisation. Les alambics ne peuvent plus servir : leur valeur d'usage est nulle et leur valeur actuelle est leur valeur vénale nette des coûts de sortie.

| Alambics | Calcul | Montant |
|---|---|---:|
| Valeur nette au 31/12/2026 | 480 000 − 15 × 24 000 | 120 000 |
| Valeur vénale nette | 30 000 − 6 000 | 24 000 |
| **Dépréciation à constater** | 120 000 − 24 000 | **96 000** |

La perte doit être constatée en 2026 : la valeur actuelle s'apprécie à la clôture. Attendre la vente de 2027, comme le propose la gérante, contredit la règle de dépréciation.

*Récapitulation*

| Anomalie | Résultat 2026 | Immobilisations nettes | Dettes | TVA à récupérer |
|---|---:|---:|---:|---:|
| A1 Coûts non incorporables inscrits à l'actif | − 94 000 | − 94 000 | — | — |
| A2 Dotation de l'unité surévaluée | + 6 420 | + 6 420 | — | — |
| A3 Solde du prix non comptabilisé (90 000 € HT, 108 000 € TTC) | — | + 90 000 | + 108 000 | + 18 000 |
| A4 Dépréciation des alambics non constatée | − 96 000 | − 96 000 | — | — |
| **Total des corrections** | **− 183 580** | **− 93 580** | **+ 108 000** | **+ 18 000** |

- Toutes les anomalies dépassent le seuil des anomalies manifestement insignifiantes (6 000 €) : elles sont récapitulées. Prises une à une, elles restent inférieures au seuil de signification : 78,3 % (A1), 5,4 % (A2), 90,0 % pour la dette omise (A3) et 80,0 % (A4).
- Leur **cumul** sur le résultat, 183 580 €, représente **153,0 %** du seuil de 120 000 € et 7,6 % du résultat courant. Les anomalies non corrigées s'apprécient individuellement et en cumulé : elles sont **significatives**.
- Leur nature aggrave le constat : deux d'entre elles, qui majorent le résultat de 190 000 €, résultent de choix de la direction que la gérante refuse de revoir, et l'omission d'une dette de 108 000 € fausse l'endettement.
- Le cabinet communique ces anomalies à la gérance et en demande la correction [V NEP anomalies § 11].

**b. Écritures de correction au 31/12/2026 (1 pt : 0,25 pt par écriture complète)**

X1 – Coûts non incorporables au coût de l'unité d'extraction (28 000 + 54 000 + 12 000)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 722 | Immobilisations corporelles (production immobilisée) | 82 000 | |
| 6257 | Réceptions | 12 000 | |
| 2151 | Installations complexes spécialisées | | 94 000 |

Les salaires et les consommations figurent déjà en charges par nature : la correction annule la production immobilisée correspondante.

X2 – Solde du prix de l'unité (facture SOLVÉRAN n° 4, réserves levées le 18/12/2026)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 2151 | Installations complexes spécialisées | 90 000 | |
| 44586 | Taxes sur le chiffre d'affaires sur factures non parvenues | 18 000 | |
| 4084 | Fournisseurs d'immobilisations - Factures non parvenues | | 108 000 |

X3 – Correction de la dotation aux amortissements de l'unité (47 500 − 41 080)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 28151 | Amortissements des installations complexes spécialisées | 6 420 | |
| 68112 | Dotations aux amortissements des immobilisations corporelles | | 6 420 |

X4 – Dépréciation des anciens alambics (120 000 − 24 000)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 68162 | Dotations pour dépréciations des immobilisations corporelles | 96 000 | |
| 2915 | Dépréciations des installations techniques, matériels et outillages industriels | | 96 000 |

Après correction : résultat courant de 2 216 420 € ; unité inscrite pour 1 896 000 €, amortie de 41 080 €, suivie par élément.

**c. Opinion (1,5 pt)** [V NEP rapport § 06, 08-14 ; C. com. R. 821-180]

| | Contrat communiqué (et sans anomalie nouvelle) | Contrat non communiqué |
|---|---|---|
| **La gérance corrige** | **Certification sans réserve** | **Certification avec réserve pour limitation** : le prix révisé, les pénalités et les clauses de propriété n'ont pu être vérifiés |
| **La gérance ne corrige pas** | **Certification avec réserve pour désaccord** | **Certification avec réserves pour désaccord et pour limitation** |

- **Barème** : 0,25 pt par case justifiée (1 pt) ; 0,5 pt pour les motifs et la portée ci-dessous.
- **Limitation** : faute de contrat, le cabinet ne peut pas mettre en œuvre toutes les procédures nécessaires sur le coût de l'unité et sur la dette envers SOLVÉRAN. Ses incidences sont **circonscrites** à un actif et à une dette identifiés : une réserve suffit, et l'impossibilité de certifier n'est pas justifiée [V NEP rapport § 11, 14].
- **Désaccord** : les anomalies significatives non corrigées sont chiffrées et limitées au cycle des immobilisations. Leurs incidences sont **clairement circonscrites** et une réserve suffit à éclairer l'utilisateur : réserve, et non refus de certifier [V NEP rapport § 09-10, 12].
- **Rédaction** : les motifs figurent dans la partie « Fondement de l'opinion », avec les incidences chiffrées : résultat et capitaux propres surévalués de 183 580 €, immobilisations surévaluées de 93 580 €, dettes sous-évaluées de 108 000 € [V NEP rapport § 06, 10]. Ils sont communiqués au préalable à la gérance [V NEP rapport § 06 ; L. 821-63 I].
- Dans tous les cas, la justification des appréciations peut porter sur le coût et l'amortissement de l'unité. Le cabinet obtient une déclaration écrite de la gérante, avec l'état des anomalies non corrigées [V NEP anomalies § 17 ; NEP déclarations écrites § 6-7].

**d. Note de synthèse du cycle (1 pt)** [S, F11 § 7 ; NEP anomalies § 18]
- Rappel du seuil de signification, du seuil de planification et du seuil des anomalies manifestement insignifiantes (0,25 pt).
- Risques identifiés et assertions concernées ; travaux réalisés : inspection, procès-verbaux, factures et paiements, production immobilisée, recalcul, dépréciation, demande de confirmation (0,25 pt).
- Anomalies relevées, chiffrées, communiquées à la gérance, corrigées ou non ; refus de communiquer le contrat et interdiction de contacter SOLVÉRAN, démarches du cabinet et procédures alternatives ; points de jugement : coûts incorporables, décomposition, durées, valeur vénale (0,25 pt).
- Conclusion sur le cycle et incidence sur l'opinion ; points à mentionner dans la justification des appréciations et dans la déclaration écrite ; points en suspens à suivre en 2027 : vente des alambics, pénalités, révision du prix (0,25 pt).

**Réponses tolérées**
- Une dépréciation des alambics passée au compte 6876, si le candidat justifie un caractère exceptionnel.
- Les écritures X1 et X3 présentées en une seule écriture, si les montants sont exacts.
- Un refus de certifier en l'absence de correction et de contrat, si le candidat soutient que le cumul du désaccord et de la limitation n'est plus circonscrit : 0,25 pt sur 0,5 pour les motifs.

**Erreurs fréquentes**
- Conclure à une certification sans réserve parce que chaque anomalie est inférieure au seuil, sans apprécier leur cumul (`JUR-A02`, `JUR-A06`).
- Ajouter la dette omise au cumul des anomalies de résultat (`JUR-F06`).
- Confondre limitation et désaccord, ou proposer une impossibilité de certifier pour une limitation circonscrite (`JUR-A02`).
- Écritures sans intitulés ni libellés, ou déséquilibrées (`JUR-F03`, `JUR-F04`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 214-5, 214-6 (p. 23), 214-15 à 214-17 (p. 25) | Indice de perte de valeur ; valeur actuelle ; dépréciation | [V] | F11 § 15.3 et ajout du 12/11/2026 |
| NEP anomalies § 8, 11-12, 14, 17-18 ; NEP caractère significatif § 9 | Récapitulation, cumul, nature, déclaration écrite, documentation | [V] | F11 § 4.2, 14.1 |
| NEP rapport § 06, 08-14 ; C. com. R. 821-180, L. 821-63 I ; NEP déclarations écrites § 6-7 | Opinions ; limitation ; désaccord | [V] | F11 § 8, 12.3 |
| Note de synthèse | Contenu | [S] | F11 § 7 |
| Liste des comptes du PCG 2026 : 2151, 2815, 2915, 4084, 44586, 6257, 68112, 68162, 722 | Écritures | [V] | F11, ajout du 12/11/2026 |

---

### Partie B – Durabilité (12 points)

### 3.5 Architecture des normes et plafond de la chaîne de valeur (3 pts)

**a. Architecture des ESRS et norme volontaire (1,5 pt)**
- **Élaboration** : l'EFRAG, conseiller technique de la Commission, prépare les projets ; la Commission adopte les ESRS par actes délégués, après son avis technique ; la version révisée résulte du règlement délégué (UE) 2026/1563 [V F12 § 1, § 3.2].
- **Architecture (0,75 pt)** : deux normes **transversales**, ESRS 1 « Exigences générales » et ESRS 2 « Informations générales à publier », appliquées **conjointement** avec les normes **thématiques** : cinq normes environnementales, quatre normes sociales et une norme de gouvernance [V ESRS 1 (2026) § 7-10]. ESRS 2 s'applique toujours ; les normes thématiques ne s'appliquent qu'aux thèmes matériels, complétées si besoin par des informations spécifiques à l'entité [V § 11, 29]. Les informations portent sur la gouvernance, la stratégie, la gestion des impacts, risques et opportunités, et les indicateurs et cibles [V § 5]. La catégorie sectorielle prévue en 2023 a disparu [V F12 § 3.1].
- **Norme volontaire (0,75 pt)** : le règlement délégué (UE) 2026/1560 permet aux entreprises **non soumises** à l'obligation de publier selon une norme volontaire, issue des travaux de l'EFRAG (« VSME »), organisée en un **module de base** et un **module complet** [V règl. 2026/1560 art. 2, annexe I]. Elle est proportionnée aux petites et moyennes entreprises. ARMÉLINE, non soumise, pouvait l'utiliser ; elle a choisi les ESRS, plus exigeantes, sans doute pour se rapprocher de ce que publie NÉROVALE (hypothèse de l'énoncé). Elle doit alors respecter toutes leurs exigences, chaîne de valeur comprise.

**b. Plafond de la chaîne de valeur (1,5 pt)**
- **Règle (0,5 pt)** : une entreprise soumise ne peut exiger d'une **entreprise protégée** de sa chaîne de valeur, c'est-à-dire d'une entreprise qui ne dépasse pas **1 000 salariés**, que les points de données prévus à l'**annexe II** du règlement délégué 2026/1560. Cette limite s'applique aux exercices commençant à compter du **01/01/2027** [V règl. 2026/1560 art. 1, 3, 4 ; ESRS 1 (2026) § 66 ; F12 § 4].
- **Application à NÉROVALE (0,5 pt)** : ARMÉLINE, avec 140 salariés, est une entreprise protégée. Dans l'hypothèse posée, NÉROVALE ne pourra exiger d'elle, à compter de 2027, que les points de données de l'annexe II. Le questionnaire de 140 questions va au-delà : liste nominative des cultivateurs, rapport d'audit social de chaque exploitation, salaires horaires des cueilleurs. ARMÉLINE peut refuser ce qui excède le plafond, ou le fournir de son plein gré ; NÉROVALE ne peut pas l'exiger, même comme condition de référencement [S, application]. Pour 2026, le plafond ne s'applique pas encore : la demande relève de la seule relation commerciale.
- **Les cultivateurs (0,5 pt)** : ils emploient de 2 à 25 salariés et ne sont pas soumis à l'obligation. La norme volontaire est conçue pour eux, et son module de base leur est accessible. ARMÉLINE n'a besoin, sur sa chaîne de valeur, que des informations **matérielles**, pas d'informations sur chaque acteur, et elle peut recourir à des **estimations** [V ESRS 1 (2026) § 63-65]. Exiger d'eux des informations selon les ESRS serait disproportionné. Enfin, les besoins de NÉROVALE, plafonnés pour ARMÉLINE, n'ont pas vocation à être reportés sur eux au-delà [S].

**Réponses tolérées**
- Une présentation de l'architecture qui cite les trois piliers environnement, social et gouvernance sans dénombrer les normes.
- L'emploi du sigle « VSME » ou de l'expression « norme volontaire ».

**Erreurs fréquentes**
- Présenter la norme volontaire comme une version des ESRS applicable aux entreprises soumises, ou annoncer une catégorie de normes propres à chaque secteur, qui n'a plus de base légale (`JUR-A01`).
- Croire que le plafond s'applique dès 2026, ou qu'il protège NÉROVALE plutôt qu'ARMÉLINE (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règl. délégué 2026/1563 ; ESRS 1 (2026) § 5, 7-11, 29 | Élaboration ; architecture ; normes transversales et thématiques | [V] | F12 § 1, 3, 14 |
| Règl. délégué 2026/1560 art. 1-4, annexes I et II ; ESRS 1 (2026) § 63-66 | Norme volontaire ; modules ; plafond de la chaîne de valeur ; estimations | [V] ; application : [S] | F12 § 4, 7 |

### 3.6 Périmètre de reporting et chaîne de valeur (3 pts)

**a. Périmètre et distillerie (1,5 pt)**
- **Entreprise déclarante (0,25 pt)** : l'état de durabilité porte sur la **même entreprise déclarante que les états financiers** [V ESRS 1 (2026) § 60]. ARMÉLINE n'établit que des comptes annuels et n'a pas de filiale : ses activités propres sont celles d'ARMÉLINE seule.
- **Distillerie (0,75 pt)** :
  - c'est une **coentreprise** : capital partagé à parts égales, décisions importantes à l'unanimité des deux associés (annexe 3.9). Les participations dans des coentreprises sont traitées comme des **relations d'affaires**, et non comme des activités propres [V § 69] ;
  - ce n'est pas une activité conjointe : ARMÉLINE ne comptabilise pas une quote-part des actifs, des passifs, des produits et des charges de la distillerie, mais des titres de participation (200 000 € au compte 261). L'exception de l'AR 36 ne joue donc pas [V AR 36 ; S, application] ;
  - la distillerie est aussi le **fournisseur** d'ARMÉLINE, qui lui achète 80 % de sa production (1 240 000 € sur 1 550 000 €). Elle relève donc de la **chaîne de valeur amont**. Les informations la concernant ne se limitent pas à la part de capital : elles reflètent les impacts liés à ARMÉLINE par cette relation d'approvisionnement [V § 62 ; S, application par analogie du § 70, qui vise les coentreprises mises en équivalence].
- **Contrôle opérationnel (0,5 pt)** :
  - c'est la possibilité de diriger les activités opérationnelles d'une entité, d'un site ou d'un actif [V glossaire des ESRS 2023 ; F12 § 7]. Dans les ESRS révisées, il n'intervient qu'au § 92, pour permettre d'exclure de certains indicateurs environnementaux des **activités conjointes** non contrôlées sur le plan opérationnel [V § 92]. Il ne permet pas de faire entrer une coentreprise dans les activités propres ;
  - en fait, ARMÉLINE n'a même pas ce contrôle : le président de la distillerie la dirige avec son chef de production, et M. PÉLISSIER n'y est mis à disposition que deux jours par mois pour conseiller.
  - Conséquence : les données publiées doivent être ramenées aux activités propres (6 200 MWh, 41 000 m³ d'eau, 140 salariés). Les parts de la distillerie représentent 19,0 % de l'énergie publiée, 26,8 % de l'eau et 6,0 % de l'effectif. Les informations sur la distillerie sont données, si elles sont matérielles, au titre de la chaîne de valeur.

**b. Chaîne de valeur amont et impact matériel (1,5 pt)**
- **Règles (0,75 pt)** :
  - les informations vont au-delà des activités propres dans la mesure nécessaire à la compréhension des impacts, risques et opportunités **matériels** liés à l'entreprise par ses relations d'affaires **directes et indirectes** [V ESRS 1 (2026) § 62-63] ;
  - seules les informations matérielles sont requises, et non des informations sur chaque acteur [V § 64]. La matérialité peut varier selon les parties de la chaîne de valeur [V § 67] ;
  - l'entreprise utilise des données **collectées** auprès des contreparties ou des **estimations** : moyennes sectorielles, échantillons, données fondées sur les dépenses [V § 65]. Elle en indique les principales hypothèses et limites [V § 88] ;
  - la base de préparation indique ce qui est couvert dans la chaîne de valeur [V ESRS 2 (2026) BP-1]. Si l'information n'est pas disponible, la disposition transitoire, que la lettre de mission rend applicable, impose d'**expliquer** les efforts déployés, les raisons pour lesquelles l'entreprise n'a pas pu obtenir l'information et ses plans [V ESRS 1 (2026) § 123 ; annexe 3.7]. L'argument « les cueilleurs ne sont pas nos salariés » est donc sans portée : la matérialité d'impact couvre la chaîne de valeur amont [V § 39].
- **Impact matériel (0,75 pt)** : les **conditions de travail des cueilleurs saisonniers** employés par les cultivateurs. C'est un impact **négatif**, **réel** chez le cultivateur de Seillans, qui assure 12 % des achats de rose, et **potentiel** chez les autres exploitations.
  - Sa **gravité** est élevée : santé et dignité des personnes, avec des journées de onze heures pendant une canicule et un hébergement indigne ; s'agissant de droits de l'homme, la gravité l'emporte sur la probabilité. Son **étendue** est large : environ 1 800 saisonniers dans 64 exploitations. Ses effets sur la santé peuvent être **irrémédiables** [V ESRS 1 (2026) § 40].
  - Il est lié à ARMÉLINE par ses achats, qui représentent 80 % de ses matières (9 600 000 €), dans le cadre de contrats sans aucune clause sociale. Il est donc **matériel d'impact**, quelle que soit sa matérialité financière [V § 35, 39]. Il peut aussi l'être sur le plan financier : référencement par NÉROVALE, réputation.
  - Son exclusion révèle aussi une faiblesse du **processus** de double matérialité, qui relève de l'autre axe de la mission.

**Réponses tolérées**
- Comme impact matériel, les rejets d'eaux de distillation de la distillerie dans l'Asse, qui ont donné lieu à une mise en demeure, s'ils sont rattachés à la chaîne de valeur amont et analysés avec les critères de gravité.
- Une analyse qui admet un contrôle opérationnel d'ARMÉLINE sur la distillerie, si le candidat conclut qu'il ne change pas sa qualification de relation d'affaires : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Admettre l'intégration de la distillerie à 50 %, comme dans une consolidation proportionnelle (`JUR-A05`).
- Exiger des informations sur chaque cultivateur, ou au contraire admettre l'omission de la chaîne de valeur faute de données (`JUR-A06`).
- Développer le contenu des normes thématiques au lieu d'appliquer les principes transversaux (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 60-61, 69-70, AR 36, § 92 | Entreprise déclarante ; coentreprises ; activités conjointes ; contrôle opérationnel | [V] ; application : [S] | F12 § 7, 16 |
| ESRS 1 (2026) § 35, 39-40, 62-65, 67, 88, 123 ; ESRS 2 (2026) BP-1 | Chaîne de valeur ; estimations ; disposition transitoire ; matérialité d'impact ; gravité | [V] | F12 § 6.2, 7, 14, 15, 16 |

### 3.7 Objectifs, axes et nature de l'assurance (2 pts)

- **Nature et objectif (0,5 pt)** : la mission est **contractuelle** : ARMÉLINE n'est pas tenue de publier et la lettre de mission le rappelle. Le cabinet s'inspire des lignes directrices de la H2A, qui organisent la certification légale [V LD 2026 ; F12 § 11 ; annexe 3.7]. Il doit conclure qu'il n'a pas relevé d'erreurs, d'omissions ou d'incohérences d'une importance telle qu'elles remettent en cause la conformité aux ESRS [V LD 2026 § 8].
- **Assurance (0,5 pt)** : elle est **limitée**. Les vérifications sont moindres en nature, en étendue et en durée que dans un audit des comptes, et la conclusion est de **forme négative** [V LD 2026, niveau d'assurance]. Le cabinet ne vérifie spécifiquement que certaines informations [V LD 2026 § 8.3.1].
- **Axes (0,5 pt)** [V LD 2026 § 2] :
  - axe 1 : conformité du **processus** de détermination des informations, c'est-à-dire de l'analyse de double matérialité. Il est retenu par la lettre de mission, mais la consultation du CSE en est exclue ;
  - axe 2 : conformité des **informations** publiées aux ESRS, y compris le périmètre et la chaîne de valeur ;
  - axe 3 : exigences de publication liées à la **taxonomie** ; axe 4, à terme : **balisage**. Ni l'un ni l'autre ne concerne ARMÉLINE.
  - Les conclusions sont émises axe par axe.
- **Pourquoi l'axe 2 est au premier plan (0,5 pt)** :
  - le vérificateur sélectionne les informations qui présentent un **risque important de non-conformité** ou font l'objet d'**attentes fortes des utilisateurs** [V LD 2026 § 8.3.1]. Ici, le risque porte sur la base de préparation : périmètre erroné et chaîne de valeur absente ;
  - la LD 2026 demande précisément de vérifier que la distinction entre activités propres et chaîne de valeur a été appréhendée [V § 8.1] ;
  - l'erreur de périmètre affecte toutes les données quantitatives publiées ;
  - l'utilisateur principal, NÉROVALE, attend des informations sur la chaîne d'approvisionnement : cultivateurs, cueilleurs, distillerie.

**Réponses tolérées**
- Une présentation des quatre axes sans distinguer ceux qui ne concernent pas ARMÉLINE : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Présenter la mission comme une certification légale, ou l'assurance comme raisonnable (`JUR-A01`).
- Ne pas rattacher la place de l'axe 2 aux données du cas (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 2, 8, 8.1, 8.3.1, niveau d'assurance | Axes ; assurance limitée ; périmètre ; sélection des informations | [V] ; transposition à une mission contractuelle : [S] | F13 § 2, 7 |
| F12 § 11 | Entité qui publie volontairement | [S] | F12 § 11 |

### 3.8 Procédures sur le périmètre et la chaîne de valeur (2,5 pts)

- **Planification (0,25 pt)** : à partir de la prise de connaissance, le cabinet identifie comme informations à risque la base de préparation, les données quantitatives et l'absence d'informations sur la chaîne de valeur, en tenant compte des attentes de NÉROVALE et de la controverse de juillet 2026 [V LD 2026 § 8.3.1].
- **Périmètre (1 pt)** :
  - rapprochement avec le périmètre des comptes : comptes annuels d'ARMÉLINE seuls, sans filiale ; titres de la distillerie au compte 261 pour 200 000 € [V ESRS 1 (2026) § 60 ; LD 2026 § 8.1] ;
  - examen des statuts et du pacte de la distillerie (unanimité, nomination du président) et de la convention de mise à disposition de M. PÉLISSIER ; entretiens avec la gérante, M. PÉLISSIER et le président de la distillerie, pour apprécier le contrôle opérationnel invoqué ;
  - recalcul des données des activités propres : retrait des quotes-parts de la distillerie (1 450 MWh, 15 000 m³, 9 salariés) ; rapprochement des 6 200 MWh et des 41 000 m³ avec les factures d'énergie et d'eau et les relevés de compteurs ; rapprochement de l'effectif de 140 salariés avec le registre du personnel et avec l'effectif moyen retenu dans les comptes [V LD 2026 § 8.3.2] ;
  - lecture de la base de préparation : déclaration de conformité, différences de périmètre et indication de ce qui est couvert dans la chaîne de valeur [V ESRS 2 (2026) BP-1].
- **Chaîne de valeur (1 pt)** :
  - rapprochement avec les données de l'audit des comptes : achats de fleurs de 9 600 000 € auprès de 64 cultivateurs, dont 70 % auprès de douze d'entre eux ; achats d'essence de 1 240 000 € à la distillerie, soit 80 % de sa production. Il permet d'identifier les relations d'affaires significatives que l'état ne mentionne pas ;
  - entretiens avec la responsable des achats ; demandes d'informations, avec l'accord de la gérance, auprès d'un échantillon de cultivateurs et des deux prestataires qui fournissent des saisonniers [V LD 2026 § 8.3.2] ;
  - examen des sources externes : article de presse, contrôle de l'inspection du travail, mise en demeure préfectorale de la distillerie ;
  - si ARMÉLINE produit des estimations, revue de leurs méthodes, de leurs sources et de leurs hypothèses, et de leur description [V ESRS 1 (2026) § 65, 88] ; à défaut, vérification que l'état explique les efforts entrepris, les raisons et les plans [V § 123].
- **Cohérence et fin de mission (0,25 pt)** : échanges avec l'équipe d'audit des comptes du cabinet sur les achats de fleurs et sur la distillerie [V LD 2026 § 3.2, 8.3.2] ; lecture d'ensemble du rapport de gestion et des comptes ; communication des constats à la gérance avec une demande de correction ; lettre d'affirmation.

**Réponses tolérées**
- D'autres procédures pertinentes tirées des annexes (comparaison avec des moyennes sectorielles, examen des contrats d'achat, visite d'exploitations pendant la cueillette).

**Erreurs fréquentes**
- Proposer des procédures générales sans exploiter les données du cas, en particulier celles de l'audit des comptes (`JUR-A05`, `JUR-F07`).
- Vérifier la seule exactitude arithmétique des données publiées, sans contrôler le périmètre (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 3.2, 8.1, 8.3.1, 8.3.2 | Périmètre ; sélection ; techniques ; échanges avec le commissaire aux comptes | [V] | F13 § 3, 7 |
| ESRS 1 (2026) § 60, 65, 88, 123 ; ESRS 2 (2026) BP-1 | Entreprise déclarante ; estimations ; disposition transitoire ; base de préparation | [V] | F12 § 7, 14, 16 |

### 3.9 Conclusion sur la conformité des informations (1,5 pt)

- **Si le seul défaut était la distillerie (0,5 pt)** : l'erreur de périmètre est importante, puisqu'elle touche toutes les données quantitatives, jusqu'à 26,8 % de l'eau publiée. Elle est toutefois identifiable et chiffrable : ses incidences sont **clairement circonscrites**, et une réserve suffit à éclairer l'utilisateur. La conclusion serait un **avis de conformité assorti d'une réserve motivée**, qui en chiffre les incidences [V LD 2026 § 17].
- **Situation effective (0,5 pt)** :
  - s'ajoute l'omission, sans explication, de toute la chaîne de valeur amont, qui représente 80 % des achats de matières, et d'un impact matériel. Ce n'est pas une information incomplète et expliquée, que la disposition transitoire permettrait, mais une **omission d'informations matérielles** [V ESRS 1 (2026) § 62-64, 123 ; LD 2026 § 8, 8.1] ;
  - on ne peut pas dire ce que l'état aurait contenu avec une chaîne de valeur couverte : les incidences ne sont **pas circonscrites** ;
  - la conclusion est un **avis de non-conformité, motivé**, qui expose les deux motifs : « nous estimons que les informations en matière de durabilité publiées par ARMÉLINE ne sont pas conformes aux ESRS » [V LD 2026 § 17 et annexe 2, formulation adaptée à l'axe 2 ; S, transposition à une mission contractuelle].
- **Portée (0,5 pt)** :
  - la conclusion repose sur une **assurance limitée** et sur une mission contractuelle : ce n'est pas une certification légale ;
  - elle porte sur le seul axe 2. La conclusion sur le processus est émise séparément ; elle sera affectée par l'exclusion de l'impact sur les cueilleurs ;
  - le cabinet en communique au préalable les motifs à la gérance. Il remet son rapport à la gérance, qui le transmettra à NÉROVALE : tenu au secret, le cabinet ne l'adresse pas lui-même à ce client [V L. 821-35 ; S, application] ;
  - elle ne modifie pas l'opinion sur les comptes et ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].

**Réponses tolérées**
- Dans la situation effective, un avis de conformité assorti de réserves, si le candidat soutient avec le critère de circonscription que chaque défaut est identifiable : 0,25 pt sur 0,5.
- L'emploi indifférent des mots « conclusion » et « avis ».

**Erreurs fréquentes**
- Formuler une conclusion positive (« les informations sont conformes ») ou une conclusion unique pour toute la mission (`JUR-A01`, `JUR-A02`).
- Retenir une impossibilité d'émettre un avis, alors que les défauts sont des erreurs et des omissions, et non une limitation des travaux (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 8, 8.1, 17 et annexe 2 | Avis par axe ; réserve ; non-conformité ; formulations | [V] ; transposition : [S] | F13 § 4, 7 |
| ESRS 1 (2026) § 62-64, 123 | Omission de la chaîne de valeur | [V] | F12 § 7, 16 |
| C. com. L. 821-35, L. 821-55 | Secret professionnel ; absence de garantie de la gestion | [V] ; application : [S] | F10 § 7 ; F09 § 6 |
