# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 18

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 19/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex49_consolidation_anc_conversion_actions_preference_credit_bail` |
| 2 – Opérations de restructuration | 25 | 2.1  à 2.7 | `exercices/ex50_fusion_renonciation_mali_technique_soulte` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.12 | `exercices/ex51_audit_achats_stocks_sarl_definition_reporting` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 1 |
| 1.2 Entité présentant l'information selon le cadre conceptuel | `2.1.a` Cadre conceptuel de l'IASB | 3 |
| 1.3 a Périmètre, actions de préférence sans droit de vote, méthodes | `2.1.c` Périmètre de consolidation | 3 |
| 1.3 b Écart entre contrôle et intérêt chez GAVÉLIS Connect | `2.1.d` Conséquences du référentiel et des méthodes | 1 |
| 1.4 Crédit-bail d'ORTHÉPONT | `2.2.c` Homogénéisation, thèmes communs | 3 |
| 1.5 a Méthode de conversion | `2.2.e` Conversion des comptes établis en devises | 2 |
| 1.5 b Conversion du compte de résultat et du bilan | `2.2.e` Conversion des comptes établis en devises | 3 |
| 1.5 c Écart de conversion : cumul, analyse, répartition, sort | `2.2.e` Conversion ; `2.2.h` Partage des capitaux propres | 4 |
| 1.6 a Dividendes internes | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.6 b Ventes de capteurs et marge interne | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.6 c Comptes réciproques en devises | `2.2.f` Comptes réciproques ; `2.2.e` Conversion | 1,5 |
| 1.7 Acquisition de GAVÉLIS Connect | `2.2.g` Écarts d'évaluation et d'acquisition | 4 |
| 1.8 a Tableaux de partage | `2.2.h` Partage des capitaux propres | 4 |
| 1.8 b Écritures d'élimination des titres et de partage | `2.2.h` Partage des capitaux propres | 3 |
| 1.9 Phases du processus et place de la conversion | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.10 a Extrait du bilan consolidé | `2.3.a` Documents de synthèse consolidés | 4 |
| 1.10 b Notes de l'annexe : périmètre et conversion | `2.3.a` Documents de synthèse consolidés | 3 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires (réserves / résultat) ; `ECV` = écart de conversion de l'entité avant partage ; `ECV_G` / `ECV_M` = écarts de conversion, part du groupe / part des minoritaires (cette dernière est présentée dans les intérêts minoritaires) ; `EA` = écart d'acquisition ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.BALESCAR` : titres détenus par la SAS BALESCAR ; `RSV.CZ` : réserves de BALESCAR CZ).

---

### 1.1 Obligation de consolider et référentiel (1 pt)

- **Obligation (0,5).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. La SAS BALESCAR contrôle exclusivement ORTHÉPONT, BALESCAR CZ et GAVÉLIS Connect (question 1.3 a) : l'obligation est née, et aucun cas d'exemption ne s'applique (hypothèse de l'énoncé). Le fait que BALESCAR CZ soit étrangère ne change rien : la nature du contrôle, et elle seule, fait entrer une entité dans le périmètre [V ANC art. 221-1, p. 18 ; F03 § 3].
- **Référentiel (0,5).** Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que pour les sociétés dont des titres sont admis aux négociations sur un marché réglementé à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Aucun titre de BALESCAR n'étant admis sur un marché, elle applique le règlement ANC n° 2020-01 ou **peut opter** pour les IFRS adoptées [V L. 233-24 ; F03 § 1.2] : le projet de 2028 est donc possible, mais il n'est pas imposé.

---

### 1.2 Entité présentant l'information selon le cadre conceptuel (3 pts)

- **Place de la notion (0,25).** Le cadre conceptuel de l'IASB, révisé en 2018, n'est pas une norme ; il guide l'IASB et aide les entités à définir une méthode quand aucune norme ne s'applique [V page « Conceptual Framework », ifrs.org ; IAS 8 § 11 ; F03 § 7.2]. Son chapitre 3, nouveau en 2018, décrit l'objectif et le champ des états financiers et l'entité présentant l'information [V Project Summary de l'IASB, mars 2018, p. 7 ; F03 § 14].
- **Définition (0,5).** Les états financiers fournissent une information sur les actifs, les passifs, les capitaux propres, les produits et les charges de l'**entité présentant l'information**, c'est-à-dire de l'entité qui est **tenue, ou qui choisit, de préparer des états financiers**. Ce n'est **pas nécessairement une entité juridique** : elle peut être une partie d'une entité ou en comprendre plusieurs [V Project Summary, p. 7 ; F03 § 14]. Le groupe BALESCAR n'a pas de personnalité juridique ; c'est pourtant l'entité que décrivent les comptes consolidés.
- **Trois formes d'états financiers (0,75).** États **consolidés** : actifs, passifs, capitaux propres, produits et charges de la mère **et** de ses filiales, présentés **comme une seule entité** ; états **non consolidés** : ceux de la mère seule ; états **combinés** : ceux de deux entités ou plus qui ne sont pas toutes liées par une relation mère-filiale [V Project Summary, p. 7 ; F03 § 14]. Les comptes individuels de la SAS BALESCAR sont des états non consolidés : ils montrent les titres des trois filiales (7 880 000 €) et les dividendes reçus, non l'usine de Brno ni la plateforme logicielle de GAVÉLIS. Ils ne décrivent donc pas « nos comptes » au sens où l'entend M. BORDENAVE, s'il parle de l'activité du groupe.
- **Périmètre de l'entité (0,5).** Lorsque l'entité n'est pas une entité juridique, son périmètre se détermine d'après les besoins d'information des utilisateurs, qui ont besoin d'une information **pertinente** et qui donne une **image fidèle** ; une entité présentant l'information ne comprend pas un ensemble **arbitraire ou incomplet** d'actifs, de passifs, de capitaux propres, de produits et de charges [V Project Summary, p. 7 ; F03 § 14]. Le périmètre du groupe est celui du contrôle : la mère et les trois sociétés qu'elle contrôle.
- **Application aux minoritaires (1).** BALESCAR **contrôle** l'usine de Brno et la plateforme de GAVÉLIS : elle en dirige l'emploi, et les ressources de ces filiales servent l'activité du groupe. Ne reprendre que 80 % des actifs de Brno ou 52 % de ceux de GAVÉLIS donnerait un ensemble arbitraire, qui n'existe pas (on ne contrôle pas 52 % d'un logiciel) et qui ne représenterait fidèlement ni les ressources que le groupe dirige, ni ses dettes. Les comptes consolidés reprennent donc **100 %** des actifs et des passifs des filiales [V ANC art. 221-2, p. 18-19 ; F03 § 3] ; les droits de VÁHOMER (20 % de BALESCAR CZ), des fondateurs et du fonds (48 % de GAVÉLIS) n'en sont pas retranchés : ils apparaissent comme une **part des capitaux propres de l'ensemble**, les intérêts minoritaires (3 712 200 € au 31/12/2026, question 1.10 a). Le cadre précise que les états financiers sont établis du point de vue de l'entité dans son ensemble, et non de celui d'un groupe particulier d'apporteurs de ressources [S ; F03 § 14]. En IFRS (projet de 2028), ces droits deviendraient des participations ne donnant pas le contrôle, présentées **au sein des capitaux propres** [V IFRS 10 § 22 ; F03 § 3].

**Réponses tolérées.** Le seul exposé de la définition et des trois formes, s'il est appliqué au cas (comptes individuels / consolidés de BALESCAR), obtient 1,5 pt ; l'argument « représentation fidèle des ressources contrôlées » peut être formulé sans la notion de point de vue de l'entité. Il n'est pas attendu de développement sur les états combinés au-delà de leur définition.
**Erreurs fréquentes.** Confondre l'entité présentant l'information avec la société juridique ; proposer d'intégrer les filiales à hauteur du pourcentage d'intérêt (confusion avec l'intégration proportionnelle) ; réciter l'objectif et les caractéristiques qualitatives sans répondre à la question (`JUR-F07`).

---

### 1.3 Périmètre et méthodes (4 pts)

#### a. Tableau et justification (3 pts)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % d'intérêt des minoritaires |
|---|---|---|---|---|---|
| SAS BALESCAR | — | Société consolidante | — | 100 % | — |
| ORTHÉPONT | 100 % | Exclusif | Intégration globale | 100 % | 0 % |
| BALESCAR CZ | 80 % | Exclusif | Intégration globale | 80 % | 20 % |
| GAVÉLIS Connect | 52 000 / 80 000 = **65 %** | Exclusif | Intégration globale | 52 000 / 100 000 = **52 %** | **48 %** |

(ORTHÉPONT et BALESCAR CZ : 0,5 ; ligne GAVÉLIS Connect : 0,5.) La détention de la majorité des droits de vote donne le contrôle exclusif [V ANC art. 211-3, p. 12-13 ; F03 § 2], qui conduit à l'intégration globale [V art. 221-1, p. 18 ; F03 § 3]. Toutes les participations sont directes.

- **Pourcentage de contrôle de GAVÉLIS Connect (1).** Il mesure les **droits de vote** détenus [V art. 211-6, p. 14 ; F03 § 4.1]. Les 20 000 actions de préférence du fonds ne donnent aucun droit de vote : elles ne comptent ni au numérateur ni au dénominateur. Les voix sont celles des 80 000 actions ordinaires, dont BALESCAR détient 52 000, soit **65 %** ; les fondateurs, qui n'agissent pas de concert, en ont 35 %, et aucun pacte ne limite les droits de BALESCAR, qui désigne le président. Le contrôle est **exclusif** [V art. 211-3 ; F03 § 2].
- **Pourcentage d'intérêt (0,75).** Il mesure la part du **capital**, donc des droits sur les résultats et les capitaux propres [S, méthode du corrigé du sujet zéro ; F03 § 4.1]. Les actions de préférence ont les mêmes droits financiers que les actions ordinaires : elles comptent. BALESCAR détient 52 000 actions sur 100 000 : **52 %**. Le corrigé du sujet zéro applique la même règle aux actions de préférence sans droit de vote [V corrigé du sujet zéro, p. imprimée 204 ; F03 § 2].
- **Minoritaires (0,25).** 48 % = fondateurs 28 % (28 000 actions ordinaires) + fonds 20 % (20 000 actions de préférence). Le fonds, sans voix, est un associé minoritaire comme les autres.

**Erreurs fréquentes.** Calculer le contrôle sur les 100 000 actions (52 %, contrôle pourtant exclusif, mais pour une mauvaise raison) ; retenir 65 % comme pourcentage d'intérêt ; exclure le fonds des minoritaires parce qu'il ne vote pas (`JUR-G04`).

#### b. Lecture de l'écart entre contrôle et intérêt (1 pt)

L'intégration globale suit le **contrôle** : 100 % des actifs, des dettes, des produits et des charges de GAVÉLIS Connect entrent dans les comptes consolidés, comme si le groupe la détenait entièrement (0,5). Le **partage** suit l'**intérêt** : le groupe n'a droit qu'à 52 % de son résultat et de ses capitaux propres, les minoritaires à 48 %, alors qu'ils n'ont que 35 % des voix (0,25). Le lecteur voit donc un chiffre d'affaires et des actifs dirigés par le groupe, mais une part importante du résultat et des capitaux propres de cette filiale revient à d'autres que les associés de BALESCAR ; l'écart d'acquisition, lui, ne porte que sur les 52 % achetés (question 1.7) (0,25).

---

### 1.4 Crédit-bail d'ORTHÉPONT (3 pts)

**Justification (0,5).** Dans les comptes consolidés, les contrats de crédit-bail et assimilés sont inscrits chez le preneur au bilan sous forme d'une immobilisation et d'un emprunt, et au compte de résultat sous forme d'une dotation aux amortissements et d'une charge financière [V ANC art. 272-2, p. 53 ; F04 R2] ; le manuel retient ce traitement, et les comptes de la filiale sont retraités [V art. 271-5, p. 52 ; F04 § 1]. Le contrat transfère la propriété à son terme : la machine est amortie sur sa durée d'utilisation (10 ans), non sur la durée du bail. Les redevances ont été déduites fiscalement : la base fiscale de la machine et celle de la dette sont nulles ; la différence entre leurs valeurs consolidées est une différence temporaire, imposable ici, d'où un **impôt différé passif** [V art. 272-8, p. 57 ; F04 § 1].

**Tableau des incidences (1)**

| | 2025 (réserves) | 2026 (résultat) | Clôture |
|---|---:|---:|---:|
| Redevance annulée | + 224 600 | + 224 600 | |
| Amortissement (1 140 000 / 10) | – 114 000 | – 114 000 | |
| Intérêts (tableau du crédit-bailleur) | – 57 000 | – 48 620 | |
| **Effet avant impôt** | **+ 53 600** | **+ 61 980** | 115 580 |
| Impôt différé passif (25 %) | – 13 400 | – 15 495 | **28 895** |
| **Net** | **+ 40 200** | **+ 46 485** | 86 685 |

Contrôle : valeur nette de la machine au 31/12/2026, 1 140 000 – 2 × 114 000 = 912 000 € ; dette restante 796 420 € ; différence 115 580 € = 53 600 + 61 980.

**C1 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2154 Matériels industriels (valeur d'origine) | 1 140 000 | |
| 2815 Amortissements des installations, matériel et outillage industriels | | 228 000 |
| 168 Autres emprunts et dettes assimilées (dette au 31/12/2026) | | 796 420 |
| RSV.ORTHEPONT Réserves ORTHÉPONT (53 600 × 75 %) | | 40 200 |
| RST.ORTHEPONT Résultat ORTHÉPONT (61 980 × 75 %) | | 46 485 |
| IDP Impôt différé passif (115 580 × 25 %) | | 28 895 |
| *Retraitement du crédit-bail de la machine de découpe laser* | **1 140 000** | **1 140 000** |

**C1R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 68112 Dotations aux amortissements des immobilisations corporelles | 114 000 | |
| 6611 Intérêts des emprunts et dettes | 48 620 | |
| CH_ID Charge d'impôt différé (61 980 × 25 %) | 15 495 | |
| RES_CR Résultat | 46 485 | |
| 6122 Crédit-bail mobilier (redevance de 2026) | | 224 600 |
| *Remplacement de la redevance par l'amortissement et les intérêts* | **224 600** | **224 600** |

**Réponses tolérées.** Une dette dont la part remboursable en 2027 (184 779 €) est indiquée à part ; l'amortissement cumulé ventilé entre réserves et résultat dans une écriture en deux temps, si les montants nets sont justes.
**Erreurs fréquentes.** Amortir sur la durée du bail (6 ans) malgré le transfert de propriété ; porter l'effet de 2025 en résultat de 2026 ; retenir la dette d'ouverture (972 400 €) ; oublier l'impôt différé ou l'inverser (`JUR-F05`, `JUR-G06`).

---

### 1.5 Conversion des comptes de BALESCAR CZ (9 pts)

#### a. Méthode de conversion (2 pts)

- **Règles (0,5).** La méthode du **cours de clôture** convertit tous les actifs et passifs au cours de clôture et les produits et charges, dotations comprises, au cours moyen ; celle du **cours historique** convertit les éléments non monétaires et les capitaux propres au cours historique, les éléments monétaires au cours de clôture, les produits et charges au cours du jour (en pratique le cours moyen), les dotations au cours historique des actifs concernés [V ANC art. 272-16 et 272-17, p. 59-60 ; F04 R13]. Dans le cas général, la conversion de la monnaie locale à la monnaie de fonctionnement suit la méthode du cours historique, et celle de la monnaie de fonctionnement à la monnaie de l'entité consolidante la méthode du cours de clôture [V art. 272-18, p. 60 ; F04 R13].
- **BALESCAR CZ est autonome (1).** Une entité n'est pas autonome lorsque son exploitation fait partie intégrante des activités d'une autre, notamment lorsque la monnaie de l'entité consolidante est prépondérante pour ses opérations ou son financement, ou que ses liens commerciaux ou financiers avec elle sont prépondérants ; sa monnaie de fonctionnement est alors celle de l'entité dont elle dépend ; celle d'une entité autonome est sa monnaie locale [V IR3 et IR4 sous art. 272-15, p. 59 ; F04 R13]. BALESCAR CZ achète, paie ses salariés et se finance en couronnes ; 70 % de ses ventes vont à des tiers d'Europe centrale ; son directeur fixe les prix et la production ; ses ventes à BALESCAR (30 %, en euros) se négocient comme avec ses autres grands clients. Ses liens avec BALESCAR ne sont pas prépondérants : elle est **autonome**, sa monnaie de fonctionnement est la couronne, et ses comptes sont convertis directement en euros au **cours de clôture**, comme le prévoit le manuel. L'inflation tchèque, inférieure à 3 % par an, n'appelle aucune règle particulière [V art. 272-22, p. 61].
- **Avec la méthode du cours historique (0,5).** Les immobilisations et les stocks garderaient leur contre-valeur au cours de leur entrée, et les dotations aux amortissements suivraient ces mêmes cours ; seuls les éléments monétaires (créances, disponibilités, emprunts, dettes) suivraient le cours de clôture. L'écart de conversion ne naîtrait que de la position monétaire nette, au lieu de porter sur tous les capitaux propres ; la hausse de la couronne en 2026 ne réévaluerait plus l'usine de Brno en euros. Le règlement place les écarts en capitaux propres sans distinguer les méthodes [V art. 272-21, p. 61 ; F04 R13 et § 6].

#### b. Conversion du compte de résultat et du bilan (3 pts)

**Compte de résultat de 2026 (0,75)** — cours moyen de 24,60 CZK pour 1 €

| Postes | CZK | Cours | € |
|---|---:|---:|---:|
| Chiffre d'affaires | 492 000 000 | 24,60 | 20 000 000 |
| Achats consommés et charges externes | – 285 360 000 | 24,60 | – 11 600 000 |
| Charges de personnel | – 132 840 000 | 24,60 | – 5 400 000 |
| Dotations aux amortissements | – 29 520 000 | 24,60 | – 1 200 000 |
| Charges financières | – 1 968 000 | 24,60 | – 80 000 |
| Impôt sur les bénéfices | – 12 300 000 | 24,60 | – 500 000 |
| **Résultat net** | **30 012 000** | | **1 220 000** |

**Bilan au 31/12/2026 (2,25 : actif et dettes 0,75 ; capital et réserves 0,75 ; résultat et écart cumulé 0,75)**

| Actif | CZK | Cours | € |
|---|---:|---:|---:|
| Immobilisations corporelles nettes | 136 640 000 | 24,40 | 5 600 000 |
| Stocks | 36 112 000 | 24,40 | 1 480 000 |
| Créance sur BALESCAR | 20 496 000 | 24,40 | 840 000 |
| Autres créances clients | 32 208 000 | 24,40 | 1 320 000 |
| Disponibilités | 11 126 400 | 24,40 | 456 000 |
| **Total** | **236 582 400** | | **9 696 000** |

| Passif | CZK | Cours | € |
|---|---:|---:|---:|
| Capital | 80 000 000 | 25,60 (historique) | 3 125 000 |
| Réserves | 59 226 400 | historiques | 2 322 000 |
| Résultat de 2026 | 30 012 000 | 24,60 (moyen) | 1 220 000 |
| **Écart de conversion cumulé** (solde) | — | | **+ 269 000** |
| Emprunts bancaires | 39 040 000 | 24,40 | 1 600 000 |
| Fournisseurs et autres dettes | 28 304 000 | 24,40 | 1 160 000 |
| **Total** | **236 582 400** | | **9 696 000** |

- **Réserves converties** : 1 610 000 € (réserves au 01/01/2026, cours historiques, montant fourni) + 1 200 000 € (résultat de 2025 porté en réserves, au cours moyen de 2025) – 488 000 € (dividende du 15/06/2026 : 12 053 600 / 24,70, cours du jour du paiement) = **2 322 000 €**. En couronnes : 41 280 000 + 30 000 000 – 12 053 600 = 59 226 400 CZK.
- **Écart cumulé** : capitaux propres au cours de clôture, (80 000 000 + 59 226 400 + 30 012 000) / 24,40 = 169 238 400 / 24,40 = 6 936 000 € ; capitaux propres aux cours historiques et moyen, 3 125 000 + 2 322 000 + 1 220 000 = 6 667 000 € ; écart **+ 269 000 €**. Contrôle : actif 9 696 000 – dettes 2 760 000 = 6 936 000 €.

#### c. Écart de conversion : analyse, répartition, place et sort (4 pts)

**Analyse de l'écart né en 2026 (1,5)**

| Origine | Calcul | € |
|---|---|---:|
| Capitaux propres d'ouverture (0,5) | 151 280 000 / 24,40 – 151 280 000 / 24,80 = 6 200 000 – 6 100 000 | + 100 000 |
| Résultat de 2026 (0,25) | 30 012 000 / 24,40 – 30 012 000 / 24,60 = 1 230 000 – 1 220 000 | + 10 000 |
| Dividende versé (0,25) | – (12 053 600 / 24,40 – 12 053 600 / 24,70) = – (494 000 – 488 000) | – 6 000 |
| **Écart né en 2026** | | **+ 104 000** |
| Écart cumulé au 31/12/2025 (annexe 1.5) | | + 165 000 |
| **Écart cumulé au 31/12/2026** (0,5 pour le rapprochement) | | **+ 269 000** |

La couronne s'est appréciée face à l'euro en 2026 (24,80 puis 24,40 CZK pour 1 €) : les capitaux propres d'ouverture, convertis désormais au cours de clôture de 2026, valent plus en euros ; le résultat, acquis au cours moyen, aussi. Le dividende, sorti au cours du 15/06/2026 (24,70), moins favorable que celui de la clôture, réduit le gain de 6 000 €. L'écart antérieur se retrouve : 6 100 000 – (3 125 000 + 1 610 000 + 1 200 000) = + 165 000 €.

**Répartition (1).** L'écart fait partie des capitaux propres convertis de BALESCAR CZ ; il se partage selon les pourcentages d'intérêt : part du groupe 80 % × 269 000 = **215 200 €** (dont 83 200 € nés en 2026 et 132 000 € antérieurs) ; intérêts minoritaires 20 % × 269 000 = **53 800 €** (dont 20 800 € et 33 000 €).

**Place et sort (1).** Les écarts de conversion, tant sur les éléments du bilan d'ouverture que sur le résultat, sont portés dans les capitaux propres consolidés, au poste « Écarts de conversion », pour la part de l'entité consolidante, et dans les intérêts minoritaires pour la part des tiers ; ils sont réintégrés au compte de résultat en cas de cession ou de liquidation de l'entité étrangère, pour la part cédée [V ANC art. 272-21, p. 61 ; F04 R13]. Ils ne transitent pas par le résultat de 2026 : le gain reste latent tant que le groupe garde la filiale. Le manuel n'y attache aucun impôt différé.

**C2 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| ECV.CZ Écart de conversion de BALESCAR CZ (bilan converti) | 269 000 | |
| ECV_G Écarts de conversion – part du groupe (80 %) | | 215 200 |
| ECV_M Écarts de conversion – intérêts minoritaires (20 %) | | 53 800 |
| *Répartition de l'écart de conversion cumulé* | **269 000** | **269 000** |

**Réponses tolérées.** Écart de 2026 analysé en deux lignes (capitaux propres d'ouverture, dividende déduit : + 94 000 € ; résultat : + 10 000 €), si le calcul est juste ; écriture C2 fusionnée avec l'élimination des titres C11.
**Erreurs fréquentes.** Capitaux propres convertis au cours de clôture, résultat au cours de clôture, dotations au cours historique (règle de l'autre méthode) ; dividende au cours moyen ; écart antérieur oublié ; écart attribué au seul groupe ; écart porté en résultat de 2026.

---

### 1.6 Opérations internes (5 pts)

#### a. Dividendes (1,5 pt)

Les dividendes intragroupe sont éliminés en totalité [V ANC art. 251-2, p. 45 ; F04 R14] : ils ne sont qu'un transfert de réserves de la filiale vers la mère, déjà comprises dans les capitaux propres consolidés.
- **BALESCAR CZ (0,75).** BALESCAR a reçu 80 % du dividende, converti au **cours du jour du paiement** : 12 053 600 × 80 % / 24,70 = **390 400 €**, le montant même qu'elle a comptabilisé ; le dividende sorti des réserves converties de la filiale (488 000 €, question 1.5 b) est au même cours, si bien que l'élimination ne laisse aucun écart. Les 97 600 € versés à VÁHOMER ont quitté le groupe : ils ont réduit les réserves de la filiale et n'appellent aucune écriture.
- **ORTHÉPONT (0,25)** : 300 000 €.

**C3 / C3R et C4 / C4R (0,5)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.BALESCAR Résultat SAS BALESCAR | 390 400 | |
| RSV.BALESCAR Réserves SAS BALESCAR | | 390 400 |
| *C3 : élimination du dividende reçu de BALESCAR CZ (bilan)* | **390 400** | **390 400** |
| 7611 Revenus des titres de participation | 390 400 | |
| RES_CR Résultat | | 390 400 |
| *C3R : même élimination (compte de résultat)* | **390 400** | **390 400** |

C4 et C4R : mêmes écritures pour le dividende d'ORTHÉPONT, 300 000 €.

#### b. Ventes de capteurs et marge interne (2 pts)

**Justification (0,5).** Les produits et charges réciproques entre sociétés intégrées sont éliminés en totalité, sans incidence sur le résultat [V ANC art. 251-1, p. 45 ; F04 R14]. Les profits internes compris dans les stocks sont éliminés **à 100 %**, puis répartis entre le groupe et les minoritaires de **la société qui les a réalisés**, le vendeur BALESCAR CZ ; l'impôt est corrigé [V art. 251-2, p. 45 ; F04 R14]. L'impôt différé actif est rattaché à BALESCAR CZ (manuel).

**Calcul (0,5).** Ventes éliminées : 147 600 000 CZK au cours moyen de 24,60 = **6 000 000 €**, égal aux achats de BALESCAR. Marge comprise dans le stock : 720 000 × 25 % (taux exprimé sur le prix de vente) = **180 000 €** ; impôt différé actif 45 000 € ; effet net 135 000 €, réparti entre le groupe (80 %, 108 000 €) et VÁHOMER (20 %, 27 000 €). Aucun stock interne n'existait à l'ouverture.

**Écritures (1)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 701 Ventes de produits finis (BALESCAR CZ) | 6 000 000 | |
| 601 Achats stockés – Matières premières et fournitures (BALESCAR) | | 6 000 000 |
| *C5 : élimination des ventes internes de capteurs (compte de résultat)* | **6 000 000** | **6 000 000** |
| RST.CZ Résultat BALESCAR CZ (180 000 × 75 %) | 135 000 | |
| IDA Impôt différé actif (180 000 × 25 %) | 45 000 | |
| 31 Matières premières et fournitures (stock de BALESCAR) | | 180 000 |
| *C6 : élimination de la marge interne (bilan)* | **180 000** | **180 000** |
| 6031 Variation des stocks de matières premières et fournitures | 180 000 | |
| CH_ID Produit d'impôt différé | | 45 000 |
| RES_CR Résultat | | 135 000 |
| *C6R : même élimination (compte de résultat)* | **180 000** | **180 000** |

**Erreurs fréquentes.** Calculer la marge sur le coût (720 000 × 25/125) ; imputer l'élimination au seul groupe, ou à BALESCAR (l'acheteur) ; éliminer seulement 80 % de la marge (`JUR-G04`, `JUR-F07`).

#### c. Comptes réciproques en devises (1,5 pt)

**Concordance (1).** La dette de BALESCAR est libellée en euros : 840 000 €. Chez BALESCAR CZ, la créance correspondante, libellée en euros, est un élément monétaire ; elle a été convertie dans ses comptes en couronnes au cours de clôture : 840 000 × 24,40 = 20 496 000 CZK. La conversion des comptes de la filiale applique à cette créance le **même cours de clôture** : 20 496 000 / 24,40 = **840 000 €**. Les deux soldes concordent donc exactement, quel que soit le cours du 31/12/2026, parce que la même créance est convertie deux fois au même cours, dans un sens puis dans l'autre. L'écart de change éventuel entre la date des factures et la clôture est un résultat de la filiale, déjà comptabilisé dans ses comptes en couronnes (énoncé) ; il ne crée aucun écart de rapprochement. Une créance qui serait restée au cours historique des factures dans les comptes de la filiale ferait apparaître, après conversion, un écart à analyser avant l'élimination.

**C7 (bilan, 0,5)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4011 Fournisseurs – dette de BALESCAR envers BALESCAR CZ | 840 000 | |
| 4111 Clients – créance de BALESCAR CZ sur BALESCAR (convertie) | | 840 000 |
| *Élimination des comptes réciproques* | **840 000** | **840 000** |

**Erreurs fréquentes.** Éliminer la créance pour son montant en couronnes, ou au cours moyen ; conclure à un écart de rapprochement.

---

### 1.7 Acquisition de GAVÉLIS Connect (4 pts)

- **Coût d'acquisition (0,75).** En ANC, il comprend la rémunération remise au vendeur et les coûts directement imputables, nets de l'économie d'impôt [V ANC art. 231-2, p. 20 ; F05 § 1.1] : 3 380 000 + 160 000 × 75 % = **3 500 000 €**. BALESCAR a passé les frais en charges : le retraitement C9 les incorpore au coût des titres.
- **Actif net réévalué au 01/01/2026 (1).** L'écart d'évaluation est la différence entre la valeur d'entrée d'un élément identifiable et sa valeur comptable [V art. 231-9, p. 22 ; F05 § 1.2] ; les impôts différés sur les écarts d'évaluation sont comptabilisés [V art. 232-1, p. 24]. L'exception pour les actifs incorporels généralement non amortis et non cessibles séparément ne joue pas : la plateforme est amortie et cessible [V art. 272-10, p. 58 ; F05 § 1.2]. Capitaux propres 3 600 000 € + écart 1 000 000 € (1 400 000 – 400 000) – impôt différé 250 000 € = **4 350 000 €**.
- **Écart d'acquisition (1).** Coût d'acquisition – **part de l'acquéreur** dans les actifs et passifs identifiables [V art. 231-9 ; F05 § 1.3]. Cette part est le **pourcentage d'intérêt**, 52 %, et non le pourcentage de contrôle (65 %) : BALESCAR n'a droit qu'à 52 % de l'actif net, les 48 % restants revenant aux minoritaires, dont les droits sont calculés sur l'actif net réévalué [V art. 232-1, p. 24 ; F05 § 1.2]. Écart = 3 500 000 – 52 % × 4 350 000 = 3 500 000 – 2 262 000 = **1 238 000 €**, positif, inscrit à l'actif immobilisé [V art. 231-11, p. 23 ; F05 § 1.3]. Minoritaires à l'acquisition : 48 % × 4 350 000 = 2 088 000 €.
- **Traitement de 2026 (0,5).** La durée d'utilisation de l'écart, déterminée par une analyse documentée, n'est **pas limitée** : il n'est pas amorti ; sa valeur actuelle doit être comparée à sa valeur nette comptable au moins une fois par exercice ; la comparaison faite au 31/12/2026 ne révèle aucune perte de valeur (énoncé) : sa valeur reste de 1 238 000 € [V art. 231-11, p. 23 ; F05 § 1.3 et § 9]. La plateforme réévaluée, elle, est amortie : 1 000 000 / 5 = **200 000 €** d'amortissement complémentaire en 2026 ; l'impôt différé passif diminue de 50 000 € (200 000 € au 31/12/2026).

**Écritures (0,75)**

**C8 / C8R**

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Concessions et droits similaires, brevets, licences, marques, procédés, solutions | 1 000 000 | |
| RST.GAVELIS Résultat GAVÉLIS Connect (200 000 × 75 %) | 150 000 | |
| 2805 Amortissements des concessions, brevets, licences, solutions informatiques | | 200 000 |
| IDP Impôt différé passif (800 000 × 25 %) | | 200 000 |
| RSV.GAVELIS Réserves GAVÉLIS Connect (1 000 000 × 75 %) | | 750 000 |
| *C8 : écart d'évaluation de la plateforme et amortissement de 2026 (bilan)* | **1 150 000** | **1 150 000** |
| 68111 Dotations aux amortissements des immobilisations incorporelles | 200 000 | |
| CH_ID Produit d'impôt différé | | 50 000 |
| RES_CR Résultat | | 150 000 |
| *C8R : amortissement de l'écart d'évaluation (compte de résultat)* | **200 000** | **200 000** |

**C9 / C9R**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation GAVÉLIS Connect (160 000 × 75 %) | 120 000 | |
| RST.BALESCAR Résultat SAS BALESCAR | | 120 000 |
| *C9 : incorporation des frais nets d'impôt au coût des titres (bilan)* | **120 000** | **120 000** |
| 695 Impôts sur les bénéfices (économie d'impôt incorporée) | 40 000 | |
| RES_CR Résultat | 120 000 | |
| 6226 Honoraires | | 160 000 |
| *C9R : annulation des frais et de l'économie d'impôt (compte de résultat)* | **160 000** | **160 000** |

**Erreurs fréquentes.** Écart calculé avec 65 % (3 500 000 – 2 827 500 = 672 500 €) ; coût limité au prix (écart de 1 118 000 €) ou frais retenus bruts (1 278 000 €) (`JUR-G02`) ; écart d'évaluation sans impôt différé ; écart d'acquisition amorti malgré l'analyse, ou amorti sur dix ans « par défaut » ; calcul d'une valeur actuelle non demandée (`JUR-F07`).

---

### 1.8 Partage des capitaux propres (7 pts)

#### a. Tableaux de partage au 31/12/2026 (4 pts)

**ORTHÉPONT (100 %) (1)**

| | Total retraité | Groupe (100 %) |
|---|---:|---:|
| Capital | 2 000 000 | 2 000 000 |
| Réserves : 3 400 000 + 40 200 (crédit-bail) | 3 440 200 | 3 440 200 |
| Élimination des titres (capital souscrit à la création) | | – 2 000 000 |
| **Réserves consolidées** | | **3 440 200** |
| Résultat : 900 000 + 46 485 (crédit-bail) | 946 485 | **946 485** |

**BALESCAR CZ, après conversion (80 % / 20 %) (1,5)**

| | Total | Groupe (80 %) | Intérêts minoritaires (20 %) |
|---|---:|---:|---:|
| Capital (cours historique) | 3 125 000 | 2 500 000 | 625 000 |
| Réserves (cours historiques) | 2 322 000 | 1 857 600 | 464 400 |
| Élimination des titres (souscrits à la création) | | – 2 500 000 | |
| **Réserves consolidées / minoritaires** | | **1 857 600** | **1 089 400** |
| Écart de conversion cumulé | + 269 000 | + 215 200 | + 53 800 |
| Résultat : 1 220 000 – 135 000 (marge interne) | 1 085 000 | 868 000 | 217 000 |
| **Intérêts minoritaires au 31/12/2026** | | | **1 360 200** |

Les titres, souscrits pour 80 % du capital au cours de 25,60, égalent la part du groupe dans le capital converti au même cours : aucun écart d'acquisition. Les intérêts minoritaires représentent 20 % des capitaux propres convertis au cours de clôture et retraités : 20 % × (6 936 000 – 135 000) = 1 360 200 €, écart de conversion compris.

**GAVÉLIS Connect (52 % / 48 %) (1,5)**

| | Total retraité | Groupe (52 %) | Intérêts minoritaires (48 %) |
|---|---:|---:|---:|
| Capital | 1 000 000 | | |
| Prime d'émission | 800 000 | | |
| Réserves : 1 800 000 + 750 000 (écart d'évaluation net) | 2 550 000 | | |
| **Capitaux propres retraités hors résultat** | **4 350 000** | **2 262 000** | **2 088 000** |
| Élimination des titres (coût d'acquisition) | | – 3 500 000 | |
| Écart d'acquisition (inscrit à l'actif) | | + 1 238 000 | |
| **Réserves consolidées** | | **0** | |
| Résultat : 700 000 – 150 000 (amortissement complémentaire net) | 550 000 | 286 000 | 264 000 |
| **Intérêts minoritaires au 31/12/2026** | | | **2 352 000** |

Entrée dans le périmètre le 01/01/2026, sans dividende versé depuis, la société n'apporte aucune réserve consolidée : ses capitaux propres retraités hors résultat égalent l'actif net réévalué d'acquisition. Le fonds, porteur des actions de préférence, reçoit sa part (20 %) dans les intérêts minoritaires avec les fondateurs (28 %) ; il supporte 48 % de l'amortissement de l'écart d'évaluation.

#### b. Écritures (3 pts)

**C10 (0,75)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.ORTHEPONT Capital ORTHÉPONT | 2 000 000 | |
| RSV.ORTHEPONT Réserves retraitées | 3 440 200 | |
| RST.ORTHEPONT Résultat retraité | 946 485 | |
| 261 Titres de participation ORTHÉPONT | | 2 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 3 440 200 |
| RST_G Résultat consolidé – part du groupe | | 946 485 |
| *Élimination des titres ORTHÉPONT (100 %)* | **6 386 685** | **6 386 685** |

**C11 (1)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.CZ Capital BALESCAR CZ (cours historique) | 3 125 000 | |
| RSV.CZ Réserves (cours historiques) | 2 322 000 | |
| RST.CZ Résultat retraité | 1 085 000 | |
| 261 Titres de participation BALESCAR CZ | | 2 500 000 |
| RSV_G Réserves consolidées – part du groupe (80 % × 5 447 000 – 2 500 000) | | 1 857 600 |
| RSV_M Intérêts minoritaires – capital et réserves (20 % × 5 447 000) | | 1 089 400 |
| RST_G Résultat consolidé – part du groupe | | 868 000 |
| RST_M Intérêts minoritaires – résultat | | 217 000 |
| *Élimination des titres BALESCAR CZ et partage (80 / 20)* | **6 532 000** | **6 532 000** |

L'écart de conversion a été partagé par C2 (question 1.5 c).

**C12 (1,25)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.GAVELIS Capital GAVÉLIS Connect | 1 000 000 | |
| 1041 Primes d'émission GAVÉLIS Connect | 800 000 | |
| RSV.GAVELIS Réserves retraitées | 2 550 000 | |
| RST.GAVELIS Résultat retraité | 550 000 | |
| EA Écart d'acquisition GAVÉLIS Connect | 1 238 000 | |
| 261 Titres de participation GAVÉLIS Connect (3 380 000 + 120 000) | | 3 500 000 |
| RSV_M Intérêts minoritaires – capital et réserves (48 % × 4 350 000) | | 2 088 000 |
| RST_G Résultat consolidé – part du groupe (52 % × 550 000) | | 286 000 |
| RST_M Intérêts minoritaires – résultat (48 % × 550 000) | | 264 000 |
| *Élimination des titres GAVÉLIS Connect, écart d'acquisition et partage (52 / 48)* | **6 138 000** | **6 138 000** |

**Erreurs fréquentes.** Partager GAVÉLIS Connect à 65 / 35 ; oublier l'écart d'évaluation dans ses capitaux propres ; partager les capitaux propres de BALESCAR CZ en couronnes ou au seul cours de clôture sans écart ; écritures non équilibrées (`JUR-G01`, `JUR-G04`, `JUR-F04`).

---

### 1.9 Phases du processus et place de la conversion (2 pts)

**Rattachement (1)**

| Phase | Traitements du dossier |
|---|---|
| 1. Périmètre, méthodes, manuel de consolidation | 1.3 (trois intégrations globales ; pourcentages de GAVÉLIS Connect) ; méthodes du manuel (annexe 1.3) |
| 2. Retraitements d'homogénéisation, dans la monnaie de chaque entité | Crédit-bail d'ORTHÉPONT (1.4, C1) ; BALESCAR CZ : comptes déjà établis en couronnes selon les méthodes du groupe ; frais d'acquisition des titres GAVÉLIS (1.7, C9) |
| 3. Conversion des comptes de BALESCAR CZ | 1.5 a et b (cours de clôture, écart de conversion) |
| 4. Évaluation de l'entité acquise | Écart d'évaluation de la plateforme et son suivi (1.7, C8) |
| 5. Cumul des comptes retraités et convertis | Annexe 1.9 + bilan converti de BALESCAR CZ |
| 6. Élimination des opérations internes | Dividendes (1.6 a), ventes et marge (1.6 b), comptes réciproques (1.6 c) |
| 7. Élimination des titres, écart d'acquisition, partage | 1.5 c (répartition de l'écart de conversion, C2), 1.7 (écart d'acquisition), 1.8 |
| 8. Bilan, compte de résultat et annexe consolidés | 1.10 |

**Pourquoi cet ordre pour BALESCAR CZ (1).**
- **Homogénéisation avant la conversion (0,5).** Les retraitements portent sur les opérations de la filiale, enregistrées en couronnes : ils se calculent dans sa monnaie, sur ses propres données (valeurs d'origine, durées, flux de l'exercice), puis sont convertis avec les postes qu'ils modifient, aux cours qui leur sont propres (actif au cours de clôture, charge au cours moyen). Convertir d'abord obligerait à retraiter des montants en euros obtenus à des cours différents, et l'écart de conversion ne porterait pas sur les capitaux propres homogènes de la filiale. On convertit des comptes déjà conformes aux méthodes du groupe [S ; F04 R13].
- **Éliminations et partage après la conversion (0,5).** Les opérations internes opposent des montants de deux sociétés : elles ne s'éliminent qu'exprimées dans la même monnaie, l'euro (créance de 840 000 € convertie contre dette de 840 000 € ; dividende de 390 400 € reçu contre dividende converti au même cours). Le partage porte sur les capitaux propres en euros, **écart de conversion compris**, qui ne naît qu'avec la conversion, et l'élimination des titres compare leur coût en euros à la quote-part des capitaux propres convertis aux cours historiques. L'intégration globale cumule les comptes après retraitements, élimine les opérations internes et partage les capitaux propres [V ANC art. 221-2, p. 18-19 ; F03 § 3].

**Réponses tolérées.** Écart d'évaluation rangé avec les retraitements ; frais d'acquisition rangés avec l'élimination des titres ; autre découpage, si la conversion suit l'homogénéisation en couronnes et précède le cumul, les éliminations et le partage.
**Erreurs fréquentes.** Conversion placée après le partage, ou avant les retraitements ; phases énumérées sans y rattacher les traitements du dossier (`JUR-G01`).

---

### 1.10 Documents de synthèse (7 pts)

#### a. Extrait du bilan consolidé au 31/12/2026 (4 pts)

Modèle du règlement ANC [V art. 281-1, p. 66 ; F14 § 1.2].

**Réserves consolidées et résultat net part du groupe**

| Société | Réserves consolidées | Résultat net part du groupe |
|---|---:|---:|
| SAS BALESCAR | 21 400 000 + 390 400 (C3) + 300 000 (C4) = 22 090 400 | 3 100 000 – 390 400 – 300 000 + 120 000 (C9) = 2 529 600 |
| ORTHÉPONT | 3 440 200 | 946 485 |
| BALESCAR CZ | 1 857 600 | 868 000 |
| GAVÉLIS Connect | 0 | 286 000 |
| **Total** | **27 388 200** | **4 630 085** |

**Extrait du bilan consolidé**

| Poste | Calcul | Montant |
|---|---|---:|
| Immobilisations incorporelles | 1 650 000 + 1 000 000 – 200 000 (plateforme, C8) + 1 238 000 (0,5) | 3 688 000 |
| dont écarts d'acquisition | GAVÉLIS Connect, non amorti (0,25) | 1 238 000 |
| Immobilisations corporelles | 24 800 000 + 5 600 000 (BALESCAR CZ converti) + 912 000 (machine, C1) (0,5) | 31 312 000 |
| Capital (entité consolidante) | SAS BALESCAR (0,25) | 6 000 000 |
| Réserves et résultat consolidés | 27 388 200 + 4 630 085, tableau ci-dessus (réserves 0,5 ; résultat 0,5) | 32 018 285 |
| dont résultat net de l'exercice | | 4 630 085 |
| Autres – écarts de conversion | 80 % × 269 000 (0,25) | 215 200 |
| **Capitaux propres (part du groupe)** | (0,25) | **38 233 485** |
| **Intérêts minoritaires** | 1 360 200 (BALESCAR CZ) + 2 352 000 (GAVÉLIS Connect) (0,5) | **3 712 200** |
| Emprunts et dettes financières | 9 300 000 + 1 600 000 (BALESCAR CZ converti) + 796 420 (crédit-bail, C1) (0,5) | 11 696 420 |

- Les écarts de conversion part du groupe figurent dans les capitaux propres part du groupe, sur la ligne « autres », à détailler dans l'analyse de la variation des capitaux propres de l'annexe [V art. 281-1, p. 66 ; art. 282-26, p. 84 ; F14 § 1.2 et 1.4] ; la part des minoritaires (53 800 €) est comprise dans les intérêts minoritaires, rubrique distincte des capitaux propres part du groupe [V art. 272-21, p. 61 ; art. 281-1].
- **Contrôle** : capitaux propres individuels (30 500 000 + 6 300 000 + 4 300 000) + capitaux propres convertis de BALESCAR CZ (6 936 000) + retraitements nets (86 685 crédit-bail + 120 000 frais – 135 000 marge + 600 000 plateforme) – titres éliminés (8 000 000) + écart d'acquisition (1 238 000) = 41 945 685 € = 38 233 485 + 3 712 200. Résultat de l'ensemble consolidé : 4 630 085 + 217 000 + 264 000 = 5 111 085 €.

**Réponses tolérées.** Écarts de conversion intégrés à la ligne « réserves et résultat consolidés » avec mention de leur montant ; dette de crédit-bail présentée sur une ligne distincte des emprunts.
**Erreurs fréquentes.** Titres de participation laissés à l'actif ; immobilisations de BALESCAR CZ en couronnes ou au cours moyen ; écart de conversion entier dans les capitaux propres part du groupe ; intérêts minoritaires dans les capitaux propres part du groupe ; montants sans calcul (`JUR-F02`).

#### b. Notes de l'annexe (3 pts)

L'annexe énonce les principales méthodes comptables du groupe et identifie celles retenues lorsqu'un choix est possible [V ANC art. 282-2, p. 75 ; F14 § 10] ; elle donne le nom et le siège des entités consolidées, la fraction de leur capital détenue et leur mode de consolidation [V art. 282-3, p. 75], ainsi que les critères retenus pour définir le périmètre [V art. 282-4, p. 75 ; F14 § 10] ; elle présente les chiffres de l'exercice précédent [V art. 282-1, p. 74].

**Note « Périmètre de consolidation » (1,5 ; exemple de rédaction)**
> Les comptes consolidés comprennent les comptes de la SAS BALESCAR et des sociétés qu'elle contrôle de manière exclusive, intégrées globalement ; le contrôle exclusif résulte de la détention de la majorité des droits de vote. Le groupe ne détient aucune participation sous contrôle conjoint ou influence notable.
>
> | Société | Siège | % du capital | % des droits de vote | Méthode |
> |---|---|---:|---:|---|
> | SAS ORTHÉPONT | Orthez (France) | 100 % | 100 % | Intégration globale |
> | BALESCAR CZ s.r.o. | Brno (République tchèque) | 80 % | 80 % | Intégration globale |
> | SAS GAVÉLIS Connect | Pau (France) | 52 % | 65 % | Intégration globale |
>
> GAVÉLIS Connect est entrée dans le périmètre le 01/01/2026, date de l'acquisition de 52 000 actions ordinaires. Son capital comprend 20 000 actions de préférence sans droit de vote, détenues par un fonds régional de capital-investissement, qui ont les mêmes droits financiers que les actions ordinaires : elles sont exclues du calcul des droits de vote (65 %), qui fonde le contrôle exclusif, et comprises dans celui de la fraction du capital (52 %), qui détermine la part du groupe dans le résultat et les capitaux propres. Les intérêts minoritaires de la société (48 %) comprennent la part du fonds.

(Critère du contrôle : 0,25 ; tableau avec capital et méthode : 0,5 ; droits de vote et actions de préférence : 0,5 ; entrée de GAVÉLIS Connect : 0,25.) La justification n'est obligatoire que pour une intégration globale avec 40 % ou moins des droits de vote [V art. 282-4] ; l'écart entre le capital (52 %) et les droits de vote (65 %) gagne cependant à être expliqué [S ; F14 § 10].

**Note « Conversion des comptes des entités étrangères » (1,5 ; exemple de rédaction)**
> BALESCAR CZ, dont l'exploitation ne fait pas partie intégrante des activités d'une autre entité du groupe (achats, salaires et financement en couronnes, clientèle majoritairement extérieure au groupe, direction locale), est une entité autonome dont la monnaie de fonctionnement est la couronne tchèque. Ses comptes sont convertis selon la méthode du cours de clôture : actifs et passifs au cours de clôture (24,40 CZK pour 1 € au 31/12/2026), produits et charges au cours moyen de l'exercice (24,60), capitaux propres aux cours historiques, dividendes au cours du jour de leur paiement (24,70). Les écarts de conversion sont inscrits dans les capitaux propres consolidés, au poste « Écarts de conversion », pour la part du groupe (215 200 € au 31/12/2026, dont 83 200 € nés en 2026) et dans les intérêts minoritaires pour la part des tiers (53 800 €) ; ils ne donnent lieu à aucun impôt différé et seront inscrits en résultat en cas de cession ou de liquidation de la société, pour la part cédée.

(Méthode et justification : 0,5 ; cours : 0,5 ; traitement des écarts et montants : 0,5.) Contenu [S ; F04 R13 ; F14 § 1.4], règles [V art. 272-17 et 272-21].

**Réponses tolérées.** Notes rédigées sous forme de liste structurée plutôt qu'en texte suivi ; cours de 2025 ajoutés (comparatif).
**Erreurs fréquentes.** Note de périmètre limitée aux pourcentages de capital, sans expliquer le contrôle de GAVÉLIS Connect ; écarts de conversion annoncés en résultat ; oubli de la part des minoritaires dans les écarts (`JUR-F07`).

---

### Réponses tolérées (rappel général)
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (erreur non sanctionnée deux fois) ; écritures de bilan et de compte de résultat présentées en une seule écriture, si le résultat et l'impôt différé sont distingués.

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 a) Qualification, modalités, effets, référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2 |
| 2.1 b) Régime de faveur : conditions et conséquences, sort fiscal du mali | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 2 |
| 2.2 Mode d'évaluation des apports | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 1 |
| 2.3 a) Parité exacte, renonciation, nombre d'actions | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 2 |
| 2.3 b) Parité du traité, soulte, équité, plafond légal et condition fiscale | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 3,5 |
| 2.4 a) Actif net apporté, quotes-parts, capital, prime, mali | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 1,5 |
| 2.4 b) Mali technique, vrai mali, affectation | `1.2.e` Calculer et analyser le boni ou mali de fusion | 3 |
| 2.5 a) SOULÉTINE : augmentation de capital, soulte, réalisation des apports | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 2 |
| 2.5 b) SOULÉTINE : annulation des titres et mali | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes | 2 |
| 2.5 c) SOULÉTINE : frais de fusion, dette et créance réciproques | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 1,5 |
| 2.5 d) TOILES DU SAISON : transmission, droits des associés, remise des actions et de la soulte | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 1,5 |
| 2.6 Suivi du mali technique au 31/12/2027 | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes | 1,5 |
| 2.7 Note à Mme LARRALDE | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 1,5 |
| **Total** | | **25** |

---

### 2.1 Qualification, référentiel et régime fiscal (4 pts)

**a) Qualification, modalités et effets (2 pts)**
- *Qualification (0,5 pt).* L'opération est une **fusion par absorption** : TOILES DU SAISON transmet l'**ensemble de son patrimoine**, actif et passif, à une société qui existe déjà, SOULÉTINE, par suite de sa **dissolution sans liquidation** ; c'est une transmission universelle [V C. com. L. 236-1, PCG art. 710-2, F01 § 1]. Comme l'absorbante détient déjà 60 % des actions de l'absorbée, il s'agit d'une **fusion-renonciation** [V F01 § 5.1].
- *Modalités (0,75 pt).* SOULÉTINE reçoit les terrains, l'atelier, les machines, les stocks, les créances, la trésorerie et les dettes de TOILES DU SAISON. En contrepartie, elle **augmente son capital** et remet des actions nouvelles, avec une **soulte en espèces** limitée à 10 % de leur valeur nominale, **aux seuls associés autres qu'elle-même** : elle ne peut recevoir ses propres actions en échange des 7 200 actions TOILES DU SAISON qu'elle détient [V C. com. L. 236-1 et L. 236-3 II 1°, F01 § 4 et § 5.1]. Seules les 4 800 actions de la famille IHARTZABAL sont échangées.
- *Effets (0,5 pt).* TOILES DU SAISON disparaît ; son activité de tissage et de tressage se poursuit dans SOULÉTINE, qui détient désormais l'atelier en direct. Chez SOULÉTINE, les **titres de participation** TOILES DU SAISON sont **annulés** et remplacés par les éléments d'actif et de passif reçus. Les trois membres de la famille IHARTZABAL deviennent **associés de SOULÉTINE** (17,58 % du capital, voir 2.3 b) et reçoivent la soulte ; les associés actuels de SOULÉTINE sont dilués.
- *Référentiel (0,25 pt).* L'opération est enregistrée dans les **comptes individuels** des deux sociétés selon le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe le mode d'évaluation des apports et leur inscription chez l'absorbante pour les valeurs du traité [V PCG art. 710-1, 720-1, F01 § 1].

**b) Régime fiscal de faveur (2 pts)**
- *Conditions (0,75 pt).*
  - Les deux sociétés sont des personnes morales **soumises à l'impôt sur les sociétés** [V CGI art. 210 C-1, F02 § 1].
  - L'opération est une **fusion au sens fiscal** : transmission de l'ensemble du patrimoine par suite et au moment de la dissolution sans liquidation, contre l'attribution aux associés de titres de l'absorbante et, éventuellement, d'une **soulte ne dépassant pas 10 % de la valeur nominale de ces titres** [V CGI art. 210-0 A, I, 1° a, F02 § 1]. L'absence d'échange des actions détenues par l'absorbante ne fait pas sortir l'opération de cette définition [V CGI art. 210-0 A, I, 3°, F02 § 1]. La soulte prévue respecte la limite (2.3 b).
  - L'opération doit répondre à des **motifs économiques valables** et ne pas avoir pour objectif principal la fraude ou l'évasion fiscales [V CGI art. 210-0 A, III, F02 § 1] : intégration de la fabrication des toiles et des semelles, simplification de la gestion, investissements portés par une seule société.
  - SOULÉTINE prend **dans le traité** les engagements de l'art. 210 A-3 ; le régime s'applique de plein droit, sauf option pour le droit commun, sans agrément : TOILES DU SAISON n'a pas de déficit à transférer [V CGI art. 210 A-3, BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1 et § 4].
- *Conséquences pour TOILES DU SAISON (0,5 pt).* Les **plus-values latentes** sur l'atelier (360 000 €) et sur le terrain (120 000 €) **ne sont pas imposées** chez elle [V CGI art. 210 A-1, F02 § 2]. Son **résultat de la période du 1er janvier au 30 avril 2027** est en revanche imposé, quel que soit le régime, dans une déclaration établie pour cette période [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2] : l'impôt figure dans ses dettes fiscales et sera payé par SOULÉTINE.
- *Conséquences pour SOULÉTINE (0,75 pt).*
  - Engagements [V CGI art. 210 A-3, F02 § 4] : reprendre les provisions dont l'imposition est différée et se substituer à l'absorbée pour les résultats différés (sans objet ici) ; calculer la plus-value de cession future du **terrain** d'après sa valeur fiscale chez TOILES DU SAISON (80 000 €) ; inscrire les **stocks** à leur valeur fiscale chez l'absorbée (440 000 €). Les apports étant inscrits à la **valeur comptable**, avec reprise des valeurs brutes et des amortissements [V BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2], aucune plus-value n'est dégagée sur les biens amortissables : il n'y a **rien à réintégrer** sur quinze ou cinq ans [conséquence directe].
  - **Mali** : le mali technique inscrit à l'actif **ne peut donner lieu à aucune déduction ultérieure** ; son amortissement, sa dépréciation ou sa sortie sont réintégrés extra-comptablement, parce qu'il représente des plus-values non imposées chez l'absorbée [V CGI art. 210 A-1, al. 3, BOI-IS-FUS-10-50-20 § 130 et 150, F02 § 2 ter] (voir 2.6). L'annulation des titres ne dégage aucune perte déductible : le mali est entièrement technique (2.4 b).

---

### 2.2 Mode d'évaluation des apports (1 pt)

- *Situation de contrôle (0,5 pt).* SOULÉTINE détient 60 % des droits de vote de TOILES DU SAISON et désigne la majorité de ses dirigeants : elle la **contrôle de manière exclusive** [V PCG art. 741-2, F01 § 2.1]. L'une des sociétés participantes contrôlant préalablement l'autre, l'opération est réalisée **sous contrôle commun** [V art. 741-1, F01 § 2.1].
- *Mode d'évaluation (0,5 pt).* Sous contrôle commun, les apports sont évalués à la **valeur comptable**, quel que soit le sens de l'opération [V art. 743-1, F01 § 2.3] ; la fusion est d'ailleurs à l'endroit (la famille LARRALDE garde 57,69 % des droits de vote de SOULÉTINE, 2.3 b). L'exception de l'art. 743-3 ne joue pas : la quote-part rémunérée de l'actif net comptable (720 000 €) suffit largement à libérer l'augmentation de capital et la soulte (272 000 €) [V art. 743-3, F01 § 2.4]. Valeur des apports : **1 800 000 €**, actif net comptable de TOILES DU SAISON au 30 avril 2027.

---

### 2.3 Parité, renonciation et soulte (5,5 pts)

**a) Parité exacte et renonciation (2 pts)**
- *Parité (0,5 pt).* Rapport des valeurs réelles fournies : 190 / 140 = **19 / 14**, soit 19 actions SOULÉTINE pour 14 actions TOILES DU SAISON (environ 1,357). Les valeurs d'échange restent réelles même si les apports sont comptabilisés à la valeur comptable [V PCG art. 740-1, F01 § 1].
- *Renonciation (0,75 pt).* SOULÉTINE ne peut recevoir ses propres actions : il n'est pas procédé à l'échange des 7 200 actions TOILES DU SAISON qu'elle détient [V C. com. L. 236-3 II 1°, F01 § 5.1]. Seules sont rémunérées les **4 800 actions** de la famille IHARTZABAL (40 % du capital) ; la quote-part de 60 % des apports qui correspond aux droits de SOULÉTINE n'est pas rémunérée et vient en contrepartie de l'annulation de ses titres (2.4).
- *Nombre d'actions et conclusion (0,75 pt).* La parité exacte conduirait à créer 4 800 × 19 / 14 = **6 514,29 actions**, nombre qui n'est pas entier ; chez chaque associé non plus (M. Peio IHARTZABAL : 2 400 × 19 / 14 = 3 257,14 ; Mme Maialen IHARTZABAL : 2 035,71 ; M. Ximun IHARTZABAL : 1 221,43). Elle ne peut donc pas être appliquée telle quelle : il faut arrondir la parité et compenser l'arrondi par une soulte, comme le fait le projet de traité.

**b) Rémunération du projet de traité (3,5 pts)**

| Associé | Actions TOILES DU SAISON | Lots de 3 | Actions SOULÉTINE (× 4 / 3) | Soulte (10 € par lot) | Valeur reçue (× 140 € + soulte) | Valeur remise (× 190 €) |
|---|---:|---:|---:|---:|---:|---:|
| M. Peio IHARTZABAL | 2 400 | 800 | 3 200 | 8 000 | 456 000 | 456 000 |
| Mme Maialen IHARTZABAL | 1 500 | 500 | 2 000 | 5 000 | 285 000 | 285 000 |
| M. Ximun IHARTZABAL | 900 | 300 | 1 200 | 3 000 | 171 000 | 171 000 |
| **Total** | **4 800** | **1 600** | **6 400** | **16 000** | **912 000** | **912 000** |

- *Actions à créer (0,5 pt)* : 4 800 × 4 / 3 = **6 400 actions** de 40 € ; chaque avoir est un multiple de 3, aucun rompu n'est à régler.
- *Soulte (0,5 pt)* : 1 600 lots × 10 € = **16 000 €** ; par lot, 3 × 190 – 4 × 140 = 570 – 560 = 10 €.
- *Détail par associé (0,75 pt)* : tableau ci-dessus.
- *Équité (0,5 pt)* : 6 400 × 140 + 16 000 = 912 000 € = 4 800 × 190 € : la famille IHARTZABAL reçoit exactement la valeur de ses actions ; la soulte compense l'arrondi de la parité (4 / 3 = 1,333 au lieu de 1,357) et l'échange est **équitable** pour les deux groupes d'associés.
- *Limite légale (0,75 pt)* : la soulte ne peut dépasser 10 % de la valeur nominale des actions **attribuées**, c'est-à-dire des actions SOULÉTINE remises [V C. com. L. 236-1, F01 § 4] : 10 % × 6 400 × 40 = **25 600 €**. La soulte de 16 000 € en représente 62,50 % : elle est **légale**. Par lot : 10 € pour un plafond de 10 % × 4 × 40 = 16 €.
- *Condition fiscale (0,5 pt)* : la définition fiscale de la fusion reprend la même limite de 10 % du nominal des titres attribués [V CGI art. 210-0 A, I, 1° a, F02 § 1] : la soulte **ne remet pas en cause le régime de faveur**. L'échange étant équitable, aucun transfert de valeur entre associés n'est organisé [V BOI-IS-FUS-30-20 § 20 et 30, F02 § 1].

---

### 2.4 Valeur des apports et mali (4,5 pts)

**a) Apports, prime et mali (1,5 pt)**

| Élément | Calcul | Montant (€) |
|---|---|---:|
| Actif net comptable apporté (0,25) | 2 290 000 – 490 000 = capitaux propres au 30/04/2027 | 1 800 000 |
| Quote-part rémunérée, 40 % (0,25) | 1 800 000 × 4 800 / 12 000 | 720 000 |
| Quote-part non rémunérée, 60 % | 1 800 000 × 7 200 / 12 000 | 1 080 000 |
| Augmentation de capital (0,25) | 6 400 × 40 | 256 000 |
| Prime de fusion (0,25) | 720 000 – 256 000 – 16 000 (soulte) | 448 000 |
| Valeur comptable des titres annulés | prix d'acquisition de 2021, frais compris | 1 332 000 |
| **Mali de fusion (0,5)** | 1 332 000 – 1 080 000 | **252 000** |

La prime se calcule sur la **valeur comptable** de la quote-part rémunérée, diminuée de la soulte payée par SOULÉTINE [V F01 § 4 et § 5.1]. Le mali est l'écart négatif entre l'actif net reçu à hauteur de la participation et la valeur comptable de cette participation [V PCG art. 745-1 et 745-3, F01 § 5.3].

**b) Analyse et affectation du mali (3 pts)**
- *Plus-values latentes (0,75 pt).* Atelier de tissage : 840 000 – 480 000 = **360 000 €** ; terrain : 200 000 – 80 000 = **120 000 €** ; aucun autre écart et aucun passif non comptabilisé (annexe 2.4). À hauteur de la participation de 60 % : 216 000 + 72 000 = **288 000 €**.
- *Impôt (0,5 pt).* Les plus-values latentes ne sont évaluées nettes d'impôt que pour les actifs destinés à être revendus à brève échéance [V PCG art. 745-4, F01 § 5.3]. SOULÉTINE continue d'exploiter l'atelier et ne veut céder ni l'atelier ni le terrain : les plus-values sont retenues pour leur **montant brut**.
- *Mali technique et vrai mali (0,75 pt).* Mali technique = mali dans la limite des plus-values latentes à hauteur de la participation : 252 000 < 288 000, donc **mali technique = 252 000 €** et **vrai mali = 0** [V art. 745-4, F01 § 5.3]. Le mali s'explique entièrement par la part de SOULÉTINE dans les plus-values de l'atelier et du terrain : il n'y a pas de dépréciation des titres à constater. Contrôle : 60 % de la valeur réelle de TOILES DU SAISON = 60 % × 12 000 × 190 = 1 368 000 € > 1 332 000 €.
- *Affectation (0,75 pt).* Le mali technique est inférieur à la somme des plus-values latentes sur les actifs identifiés : il leur est affecté **au prorata de ces plus-values** [V art. 745-5, F01 § 5.4], soit 252 000 / 288 000 = 87,5 % de chacune ; rien n'est affecté au fonds commercial.

| Actif | Plus-value latente × 60 % | Mali affecté |
|---|---:|---:|
| Atelier de tissage | 216 000 | 252 000 × 360 / 480 = **189 000** |
| Terrain | 72 000 | 252 000 × 120 / 480 = **63 000** |
| **Total** | **288 000** | **252 000** |

- *Compte (0,25 pt).* Les deux actifs sont corporels : le mali est inscrit au compte **2187 Mali de fusion sur actifs corporels**, avec un suivi distinct pour l'atelier et pour le terrain [V art. 745-6, F01 § 5.4], puisque leurs règles d'amortissement diffèrent (2.6).

---

### 2.5 Écritures au 30 avril 2027 (7 pts)

Toutes les écritures ci-dessous sont équilibrées.

**a) SOULÉTINE : augmentation de capital et réalisation des apports (2 pts)**

**A1 — Augmentation de capital et soulte (0,75 pt).** Capital (0,25), prime (0,25), soulte versée (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (40 % × 1 800 000) | 720 000 | |
| 101 Capital (6 400 × 40) | | 256 000 |
| 1042 Primes de fusion | | 448 000 |
| 512 Banques (soulte versée à la famille IHARTZABAL) | | 16 000 |

**A2 — Réalisation des apports à la valeur comptable (1,25 pt).** Actifs pour leur **valeur brute**, amortissements repris (0,75) ; dettes (0,25) ; compte d'apport crédité de la totalité de l'actif net apporté (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 211 Terrains | 80 000 | |
| 2131 Bâtiments (atelier de tissage) | 900 000 | |
| 2154 Matériels industriels (métiers à tisser, machines à tresser) | 1 100 000 | |
| 31 Matières premières et fournitures | 260 000 | |
| 355 Produits finis | 180 000 | |
| 411 Clients (dont créance sur SOULÉTINE 84 000) | 520 000 | |
| 512 Banques | 310 000 | |
| 2813 Amortissements des constructions | | 420 000 |
| 2815 Amortissements des installations, matériel et outillage industriels | | 640 000 |
| 164 Emprunts auprès des établissements de crédit | | 240 000 |
| 401 Fournisseurs | | 150 000 |
| 43 Sécurité sociale et autres organismes sociaux | | 40 000 |
| 44 État et autres collectivités publiques | | 60 000 |
| 4561 Associés – Comptes d'apport en société | | 1 800 000 |
| **Total** | **3 350 000** | **3 350 000** |

**b) SOULÉTINE : annulation des titres et mali (2 pts)**

**A3 — Annulation des 7 200 actions TOILES DU SAISON et mali technique.** Quote-part non rémunérée au débit du compte d'apport (0,5) ; titres annulés pour leur valeur comptable (0,5) ; mali technique affecté à l'atelier et au terrain sur le compte 2187 (0,75) ; aucune dotation pour vrai mali, contrôle d'équilibre (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (60 % × 1 800 000) | 1 080 000 | |
| 2187 Mali de fusion sur actifs corporels (atelier de tissage) | 189 000 | |
| 2187 Mali de fusion sur actifs corporels (terrain) | 63 000 | |
| 261 Titres de participation (TOILES DU SAISON) | | 1 332 000 |

Le compte 4561 est soldé : 720 000 + 1 080 000 = 1 800 000.

**c) SOULÉTINE : écritures complémentaires (1,5 pt)**

**A4 — Frais de fusion (0,75 pt).** Les frais de fusion peuvent être imputés sur la prime de fusion [V PCG art. 212-9, F01 § 7] ; l'imputation se fait pour leur montant **net d'impôt**, comme le prévoit l'annexe 2.5 [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 40 000 × 75 % = **30 000 €** sur la prime (0,25) ; économie d'impôt de 10 000 € (0,25) ; écriture (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion | 30 000 | |
| 444 État – Impôts sur les bénéfices | 10 000 | |
| 512 Banques | | 40 000 |

Les 40 000 € imputés sur la prime ne passent pas par le résultat : ils sont déduits extra-comptablement du résultat fiscal de 2027, ce qui produit l'économie d'impôt de 10 000 €.

Prime de fusion après imputation : 448 000 – 30 000 = **418 000 €**.

**A5 — Dette de SOULÉTINE envers TOILES DU SAISON (0,75 pt).** Avec l'apport, SOULÉTINE reçoit une créance de 84 000 € sur elle-même : elle devient créancière et débitrice de la même obligation, qui **s'éteint par confusion** (0,25) [V C. civ. art. 1349, F01 § 8]. Écriture (0,5) :

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette envers TOILES DU SAISON) | 84 000 | |
| 411 Clients (créance de TOILES DU SAISON reçue avec l'apport) | | 84 000 |

**d) TOILES DU SAISON (1,5 pt)**

**A6 — Transmission du patrimoine (0,5 pt).** Sortie des actifs pour leur valeur brute, de leurs amortissements et des dettes ; créance sur SOULÉTINE pour la valeur d'apport. Les apports étant évalués à la valeur comptable, la valeur d'apport égale l'actif net comptable : **aucun résultat de fusion** chez TOILES DU SAISON.

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – SOULÉTINE, compte d'apport | 1 800 000 | |
| 2813 Amortissements des constructions | 420 000 | |
| 2815 Amortissements des installations, matériel et outillage industriels | 640 000 | |
| 164 Emprunts auprès des établissements de crédit | 240 000 | |
| 401 Fournisseurs | 150 000 | |
| 43 Sécurité sociale et autres organismes sociaux | 40 000 | |
| 44 État et autres collectivités publiques | 60 000 | |
| 211 Terrains | | 80 000 |
| 2131 Bâtiments | | 900 000 |
| 2154 Matériels industriels | | 1 100 000 |
| 31 Matières premières et fournitures | | 260 000 |
| 355 Produits finis | | 180 000 |
| 411 Clients | | 520 000 |
| 512 Banques | | 310 000 |
| **Total** | **3 350 000** | **3 350 000** |

**A7 — Droits des associés (0,5 pt).** Les capitaux propres reviennent aux associés à proportion de leurs actions : 1 800 000 × 60 %, 20 %, 12,5 % et 7,5 %.

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 600 000 | |
| 1061 Réserve légale | 60 000 | |
| 1068 Autres réserves | 1 020 000 | |
| 120 Résultat de l'exercice (période du 01/01 au 30/04/2027) | 120 000 | |
| 456 Associés – Opérations sur le capital (SOULÉTINE) | | 1 080 000 |
| 456 Associés – Opérations sur le capital (Peio IHARTZABAL) | | 360 000 |
| 456 Associés – Opérations sur le capital (Maialen IHARTZABAL) | | 225 000 |
| 456 Associés – Opérations sur le capital (Ximun IHARTZABAL) | | 135 000 |

**A8 — Remise des actions et de la soulte, renonciation (0,5 pt).** SOULÉTINE remet directement les actions nouvelles et la soulte à la famille IHARTZABAL (annexe 2.5) ; ses propres droits (1 080 000 €) s'éteignent par la renonciation, en contrepartie de l'annulation de ses titres. Les droits de chaque associé, en valeur comptable, se retrouvent dans ce qu'il reçoit : chaque action nouvelle correspond à (720 000 – 16 000) / 6 400 = 110 € d'apport comptable (40 € de capital et 70 € de prime) ; M. Peio IHARTZABAL : 3 200 × 110 + 8 000 = 360 000 € ; Mme Maialen IHARTZABAL : 2 000 × 110 + 5 000 = 225 000 € ; M. Ximun IHARTZABAL : 1 200 × 110 + 3 000 = 135 000 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital (Peio IHARTZABAL) | 360 000 | |
| 456 Associés – Opérations sur le capital (Maialen IHARTZABAL) | 225 000 | |
| 456 Associés – Opérations sur le capital (Ximun IHARTZABAL) | 135 000 | |
| 456 Associés – Opérations sur le capital (SOULÉTINE) | 1 080 000 | |
| 467 Divers comptes débiteurs – SOULÉTINE, compte d'apport | | 1 800 000 |

Tous les comptes de TOILES DU SAISON sont soldés. Les comptes 456 et 467 de l'absorbée relèvent d'une convention de rédaction : le PCG ne donne pas d'écriture pour l'absorbée [F01 § 9].

---

### 2.6 Suivi du mali technique au 31 décembre 2027 (1,5 pt)

- *Atelier (0,5 pt).* La quote-part du mali affectée à l'atelier est amortie selon les mêmes règles et au même rythme que l'atelier [V PCG art. 745-7, F01 § 5.5] : en linéaire sur la durée restant à courir du plan de l'atelier, 18 ans, à compter de la réalisation, soit 8 mois en 2027 : 189 000 / 18 × 8 / 12 = **7 000 €**.
- *Terrain et dépréciation (0,25 pt).* La quote-part affectée au terrain (63 000 €) n'est **pas amortie**, comme le terrain. Aucun indice de perte de valeur n'existe au 31 décembre 2027 (annexe 2.4) : aucune dépréciation du mali [V art. 745-8, F01 § 5.5].
- *Écriture (0,25 pt).*

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles | 7 000 | |
| 28187 Amortissement du mali de fusion sur actifs corporels (atelier de tissage) | | 7 000 |

- *Incidence fiscale (0,5 pt).* Sous le régime de faveur, le mali technique ne peut donner lieu à aucune déduction : la dotation de **7 000 €** est **réintégrée extra-comptablement** dans le résultat fiscal de 2027 [V CGI art. 210 A-1, al. 3, BOI-IS-FUS-10-50-20 § 130, F02 § 2 ter]. Au bilan du 31 décembre 2027, le mali figure pour 252 000 € brut, 7 000 € d'amortissements, soit 245 000 € net ; l'annexe en présente le détail par actif [V art. 838-14, F01 § 5.5].

---

### 2.7 Note à Mme LARRALDE, présidente de SOULÉTINE (1,5 pt)

*Objet : effets de l'absorption de TOILES DU SAISON sur les comptes et le capital de SOULÉTINE.*

- *Capitaux propres juste après la fusion (0,5 pt).*

| Poste (en €) | Avant | Fusion et frais | Après |
|---|---:|---:|---:|
| Capital | 1 200 000 | + 256 000 | 1 456 000 |
| Primes de fusion | – | + 448 000 – 30 000 | 418 000 |
| Réserve légale | 120 000 | | 120 000 |
| Autres réserves | 1 680 000 | | 1 680 000 |
| Report à nouveau | 60 000 | | 60 000 |
| **Total** | **3 060 000** | **+ 674 000** | **3 734 000** |

  Les capitaux propres augmentent de 674 000 € (+ 22,03 %) : quote-part de l'actif net revenant à la famille IHARTZABAL (720 000 €), moins la soulte (16 000 €) et les frais nets d'impôt (30 000 €). La quote-part de 60 % qui correspond à vos titres ne change pas les capitaux propres : les titres de 1 332 000 € sont remplacés par l'actif net reçu et par le mali.
- *Capital et place de la famille IHARTZABAL (0,25 pt).* 36 400 actions de 40 € : la famille LARRALDE détient 57,69 % des droits de vote et garde le contrôle de SOULÉTINE ; les autres associés 24,73 % ; la famille IHARTZABAL, qui détenait 40 % de la filiale, devient associée minoritaire de la société absorbante avec **17,58 %** (M. Peio IHARTZABAL 8,79 %, Mme Maialen IHARTZABAL 5,49 %, M. Ximun IHARTZABAL 3,30 %) et a reçu 16 000 € de soulte.
- *Lecture du mali (0,25 pt).* Le mali de 252 000 € inscrit en immobilisations corporelles **n'est pas une perte** : il représente la part des plus-values de l'atelier et du terrain que SOULÉTINE a payée en 2021 et que la valeur comptable ne fait pas apparaître. La part affectée à l'atelier sera amortie (7 000 € en 2027, puis 10 500 € par an), sans déduction fiscale ; celle du terrain ne l'est pas. Aucune dépréciation des titres n'était nécessaire.
- *Banques (0,25 pt).* SOULÉTINE devient débitrice de l'emprunt de TOILES DU SAISON : les emprunts passent de 1 900 000 € à 2 140 000 €, mais, rapportés aux capitaux propres, ils baissent de 0,62 à 0,57. La trésorerie passe de 398 000 € à 652 000 € (+ 310 000 reçus, – 16 000 de soulte, – 40 000 de frais). Les banques regarderont la valeur du mali avec celle de l'atelier et du terrain, sur la base de l'expertise.
- *Salariés de TOILES DU SAISON (0,25 pt).* Ils travaillent désormais pour SOULÉTINE, qui reprend l'atelier, son activité et les dettes sociales (40 000 €) ; l'intention de conserver l'atelier et d'y investir, qui justifie l'absence d'impôt sur les plus-values dans le mali, assure la continuité de leur activité dans la vallée du Saison.

---

### Réponses tolérées
- **2.1 a** : renonciation présentée en 2.3 a seulement, si elle y est justifiée.
- **2.2** : sens de l'opération analysé avant de conclure, si la conclusion repose sur le contrôle commun.
- **2.3 a** : parité exprimée en nombre décimal (1,357 action SOULÉTINE par action TOILES DU SAISON) si le nombre non entier d'actions est relevé.
- **2.3 b** : soulte exprimée par action (3,33 €) si le total de 16 000 € est juste ; plafond vérifié par lot (10 € pour 16 €) plutôt qu'au total.
- **2.4 b** : affectation calculée en appliquant 87,5 % à chaque plus-value à hauteur de 60 % (216 000 × 87,5 % = 189 000 ; 72 000 × 87,5 % = 63 000).
- **2.5 a** : soulte inscrite d'abord au crédit d'un compte 468 puis réglée par le 512 ; dettes fiscales et sociales regroupées sur un compte de la classe 4 ; métiers à tisser en 2151 ou en 215, et amortissements en 28154 ou 2815.
- **2.5 b** : A2 et A3 réunies en une seule écriture, si le compte d'apport est soldé.
- **2.5 c** : créance de 84 000 € retirée dès la réalisation des apports (clients repris pour 436 000 €, dette fournisseurs de SOULÉTINE diminuée directement), sans écriture A5 distincte, si la confusion est expliquée ; le point de justification reste dû.
- **2.5 d** : A7 et A8 réunies ; actions SOULÉTINE inscrites au compte 503 ou 508 avant leur remise, si les deux temps sont cohérents.
- **2.7** : capitaux propres présentés sans détailler l'imputation des frais, si le total est juste.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion calculée sans déduire la soulte (464 000 €), sur la valeur réelle de la quote-part rémunérée (912 000 – 256 000 – 16 000 = 640 000 €), sur la totalité de l'actif net apporté, ou frais imputés pour leur montant brut (40 000 €).
- `JUR-R02` Mali calculé sur la totalité de l'actif net (1 332 000 – 1 800 000), ou sur la valeur réelle ; plus-values latentes prises à 100 % (480 000 €) ou nettes d'impôt (288 000 × 75 % = 216 000 €, ce qui ferait apparaître à tort un vrai mali de 36 000 €) ; mali affecté plus-value par plus-value (216 000 € à l'atelier, puis un solde au terrain) au lieu du prorata.
- `JUR-R04` Suivi du mali mal traité alors que l'annexe donne la règle : amortissement sur une année pleine (10 500 €), amortissement de la part du terrain, ou dotation présentée comme déductible.
- `JUR-R05` Difficulté à s'adapter : actions remises à SOULÉTINE pour ses propres 7 200 actions ; plafond de la soulte calculé sur le nominal des actions TOILES DU SAISON (10 % × 4 800 × 50 = 24 000 €) ou sur la valeur des actions remises.
- `JUR-F07` Annexes mal exploitées : dette réciproque de 84 000 € non éliminée, amortissements non repris chez l'absorbante, intention de conserver l'atelier et le terrain ignorée.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A2, A3 et A6.
- Erreurs propres à ce cas : valeur réelle retenue au motif que la fusion est à l'endroit ; résultat de fusion constaté chez TOILES DU SAISON ; mali présenté comme une perte ou comptabilisé en charge ; date d'effet placée au 1er janvier 2027.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 236-1 | Fusion, dissolution sans liquidation, transmission universelle, soulte limitée à 10 % de la valeur nominale des actions attribuées | [V] Légifrance | F01 § 1 et § 4 |
| C. com. L. 236-3 II 1° ; BOI-IS-FUS-10-20-40-10 § 340 | Pas d'échange des titres de l'absorbée détenus par l'absorbante ; augmentation de capital limitée aux droits des autres associés | [V] | F01 § 5.1 |
| PCG art. 710-1, 710-2, 720-1, 740-1 | Champ du titre VII, définition de la fusion, inscription des apports pour les valeurs du traité, parité sur les valeurs d'échange | [V] p. 81-82 | F01 § 1 |
| PCG art. 741-1, 741-2, 743-1, 743-3 | Contrôle commun, valeur comptable, exception de l'actif net insuffisant | [V] p. 82-85 | F01 § 2 |
| PCG art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170-180 | Valeur comptable ; reprise des valeurs brutes et des amortissements | [V] p. 85 ; BOFiP | F01 § 3.2 |
| PCG art. 745-1, 745-3 à 745-8, 838-14 | Mali, mali technique et vrai mali, plus-values nettes d'impôt pour les seuls actifs revendus à brève échéance, affectation au prorata, compte 2187, amortissement, dépréciation, annexe | [V] p. 86-87 et 125 | F01 § 5.3 à § 5.5 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais de fusion imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion de la dette réciproque | [V] | F01 § 8 |
| CGI art. 210-0 A (I, 1° a et 3° ; III), 210 A, 210 C ; BOI-IS-FUS-10-10-10 § 10 et 20 ; BOI-IS-FUS-10-20-30 § 210 et 330 ; BOI-IS-FUS-30-20 § 20 et 30 | Définition fiscale de la fusion, condition de soulte, absence d'échange des titres détenus, motif économique, régime de plein droit, dernier résultat de l'absorbée, engagements, transferts de valeur | [V] | F02 § 1, § 2 et § 4 |
| CGI art. 210 A-1, al. 3 ; BOI-IS-FUS-10-50-20 § 130 et 150 | Mali technique non déductible : amortissement réintégré extra-comptablement | [V] | F02 § 2 ter |
| Comptes 456 et 467 (absorbée) | Droits des associés, compte d'apport | Convention de rédaction (le PCG ne donne pas d'écriture pour l'absorbée) | F01 § 9 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Inscription sur la liste des commissaires aux comptes et sur la liste « durabilité » ; H2A et ordre ; projet de Mme DUCASSOU | `3.1.a` Cadres d'exercice professionnel | 2 |
| 3.2 Fondement de la désignation, organe, durée ; mandat légal de trois exercices sur demande d'associés | `3.1.b` Nomination et cessation | 1 |
| 3.3 Inventaire tournant et outil de dépréciation (autorévision, immixtion) ; conjoint d'un chef de mission | `3.1.c` Principes déontologiques | 1,5 |
| 3.4 Définition, objectif et limites de l'audit ; portée de la certification pour le stock | `3.2.a` Notion d'audit | 1,5 |
| 3.5 Risques du cycle et assertions ; procédures ; extrait de la NEP estimations appliqué à la dépréciation des collections | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit ; `3.1.d` Référentiel normatif (NEP) | 6 |
| 3.6 Informations auprès des tiers ; pièces détenues par les tiers ; autres moyens | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.7 Remises et dépréciation : calculs, écritures, caractère significatif, opinion selon la correction, parties du rapport | `3.2.e` Portée des opinions | 2 |
| 3.8 Responsabilités civile et disciplinaire au titre de la vérification de durabilité ; comparaison avec la certification des comptes | `3.1.e` Mise en cause de la responsabilité | 2,5 |
| 3.9 Étendue et limites des informations ESRS ; question du gérant ; demandes de la banque | `3.3.a` Contexte et normes de durabilité | 2 |
| 3.10 Définition du reporting de durabilité et situation par rapport aux comptes ; exigences générales appliquées au projet | `3.3.b` Principes de construction du reporting | 4 |
| 3.11 Objectifs, assurance limitée, axes ; étapes de la démarche ; procédures sur deux données | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4,5 |
| 3.12 Conclusion sur les informations selon la correction ; portée | `3.4.c` Portée des avis | 1,5 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Accès à la profession de commissaire aux comptes et à la mission de durabilité (2 pts)

**Conditions et autorités (1,25 pt)**
- **Liste des commissaires aux comptes (0,5 pt)** : la profession est exercée par des personnes inscrites sur une **liste établie par la H2A** [V L. 821-13 I], qui peut déléguer l'inscription à la CNCC [V L. 820-1 II]. Une personne physique doit remplir des conditions de nationalité et d'honorabilité (pas de condamnation ni de radiation pour des faits contraires à l'honneur ou à la probité, pas de faillite personnelle ni d'interdiction), avoir accompli un **stage professionnel** de trois ans chez un commissaire aux comptes habilité, et avoir réussi le **certificat d'aptitude** aux fonctions de commissaire aux comptes **ou** être titulaire du **diplôme d'expertise comptable** [V L. 821-14 ; R. 821-46]. Pour le titulaire du diplôme d'expertise comptable, le stage est réputé accompli si **les deux tiers au moins** de son stage d'expertise comptable l'ont été chez un commissaire aux comptes habilité à recevoir des stagiaires [V R. 821-47]. L'inscrit suit ensuite une formation continue [V L. 821-24].
- **Liste « durabilité » (0,5 pt)** : la H2A tient une seconde liste, celle des commissaires aux comptes habilités à certifier les informations en matière de durabilité [V L. 821-13 II]. Pour y figurer, il faut être déjà inscrit sur la liste des commissaires aux comptes, avoir accompli **au moins huit mois** de stage auprès d'un commissaire aux comptes inscrit sur cette liste (ou d'un auditeur des informations en matière de durabilité), et avoir réussi une **épreuve** portant sur la certification d'informations en matière de durabilité [V L. 821-18 I].
- **Rôle de l'ordre (0,25 pt)** : l'ordre des experts-comptables, par ses conseils régionaux, tient le **tableau** et statue sur l'inscription des experts-comptables ; nul ne peut exercer l'expertise comptable sans y être inscrit [V ord. 45-2138 art. 3, 31, 40]. Il n'a aucune compétence sur les listes de la H2A : l'inscription au tableau ne vaut pas inscription comme commissaire aux comptes [S, distinction des deux textes].

**Appréciation du projet de Mme DUCASSOU (0,75 pt)**
- **Commissariat aux comptes (0,25 pt)** : Mme DUCASSOU est diplômée d'expertise comptable ; 27 des 36 mois de son stage d'expertise comptable ont été accomplis chez ARRAGNÈS, commissaire aux comptes habilité, soit 75 %, plus que les deux tiers exigés (24 mois). Elle remplit les conditions de nationalité et d'honorabilité : elle peut **demander son inscription** sur la liste des commissaires aux comptes, sans nouveau stage. Son inscription au tableau de l'ordre n'y suffit pas : c'est la H2A (ou la CNCC par délégation) qui l'inscrit [V L. 821-13 I, L. 821-14 ; R. 821-47 ; calcul].
- **Durabilité (0,25 pt)** : au 15/04/2027, date prévue des rapports, elle n'aura que six mois et demi de stage sur des missions de durabilité (depuis le 01/10/2026, hypothèse de l'annexe 3.2) ; les huit mois seront atteints le 31/05/2027. Surtout, elle n'a pas réussi l'épreuve, dont la prochaine session a lieu en octobre 2027 : elle ne peut pas être inscrite sur la liste « durabilité » avant cette date, ni donc certifier les informations de durabilité de 2026 [V L. 821-18 I ; calcul].
- **Signature (0,25 pt)** : même inscrite, une **salariée** ne signe pas au nom du cabinet. Dans une société de commissaires aux comptes, la certification des comptes est exercée, au nom de la société, par les commissaires aux comptes personnes physiques **associés, actionnaires ou dirigeants**, qui signent le rapport ; la certification des informations en matière de durabilité, par ceux d'entre eux qui sont inscrits sur la liste « durabilité » [V L. 821-25 al. 1, L. 821-26]. Pour signer, Mme DUCASSOU devrait aussi devenir associée (avec l'agrément prévu par les statuts) ou dirigeante [V L. 821-25 al. 4]. Les deux rapports de 2026 seront signés par Mme BERGOUIGNAN.

**Réponses tolérées**
- La présentation du certificat d'aptitude comme une voie distincte du diplôme d'expertise comptable, sans le calcul des deux tiers, si la conclusion sur l'inscription est juste : 0,5 pt sur 0,75 en appréciation.

**Erreurs fréquentes**
- Confondre le tableau de l'ordre et la liste des commissaires aux comptes, ou attribuer à l'ordre l'inscription des commissaires aux comptes (`JUR-A03`).
- Décrire l'organisation de la H2A, de la CNCC ou de l'ordre, ou les formalités d'inscription, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 820-1 II, L. 821-13, L. 821-14, L. 821-18, L. 821-24 ; R. 821-46, R. 821-47 | Listes de la H2A ; conditions d'inscription ; stage ; durabilité | [V] ; application : [S] | F09 § 3.1-3.2, § 4.1, § 18 |
| C. com. L. 821-25, L. 821-26 | Signature au nom de la société de commissaires aux comptes | [V] | F09 § 15, § 18 |
| Ord. 45-2138 art. 3, 31, 40 | Tableau de l'ordre ; conseils régionaux | [V] | F09 § 2.1-2.2 |

### 3.2 Fondement, organe et durée du mandat (1 pt)

- **Fondement et organe (0,5 pt)** : à la clôture de 2023, ASPÈDE dépassait les trois seuils (total du bilan de 10 100 000 €, chiffre d'affaires de 18 200 000 €, 84 salariés), aussi bien ceux qui étaient en vigueur pour cet exercice que ceux, relevés à 5 000 000 €, 10 000 000 € et 50 salariés, qui s'appliquent aux exercices ouverts à compter du 01/01/2024 : la SARL était **tenue** de désigner un commissaire aux comptes [V L. 223-35 al. 2 ; D. 221-5, applicable par D. 223-27 ; décret n° 2024-152, art. 4]. La désignation relève des **associés**, organe analogue à l'assemblée générale ordinaire, statuant à la majorité de plus de la moitié des parts sociales [V L. 821-40 I ; L. 223-35 al. 1, L. 223-29]. Avec 50 % des parts, le gérant ne peut pas décider seul en première consultation.
- **Durée et premier mandat (0,5 pt)** : la désignation imposée par les seuils est faite pour **six exercices**, de 2024 à 2029 ; les fonctions expirent après la décision des associés qui statue sur les comptes de 2029, en 2030 [V L. 821-44 al. 1]. La réduction à trois exercices n'est ouverte qu'à une désignation **volontaire** ou fondée sur les règles des petits groupes [V L. 821-46] : elle est exclue ici, et une décision des associés ne peut pas raccourcir un mandat en cours. Le premier mandat n'avait duré que trois exercices pour une autre raison : en 2020, ASPÈDE ne dépassait qu'un seuil (61 salariés ; total du bilan de 3 600 000 € et chiffre d'affaires de 7 400 000 €, sous les seuils alors applicables, qui étaient inférieurs aux seuils actuels), et le cabinet avait été désigné sur la **demande motivée d'associés représentant au moins le tiers du capital** (Mme Laure et Mme Hélène ESQUERRÉ, 50 %), cas où la loi fixe elle-même un mandat de **trois exercices** [V L. 223-35 al. 4]. La mission de durabilité, volontaire, a elle aussi été confiée pour trois exercices (annexe 3.10).

**Réponses tolérées**
- La mention que seul un relèvement par décision de justice, en cas de faute ou d'empêchement, pourrait mettre fin au mandat avant son terme, sans développement.

**Erreurs fréquentes**
- Admettre une réduction du mandat à trois exercices pour une désignation imposée par les seuils, ou confondre la faculté de L. 821-46 et le mandat légal de trois exercices sur demande d'associés (`JUR-A05`).
- Développer les formes des décisions collectives ou les formalités de dépôt, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 223-29, L. 223-35 ; D. 221-5 ; D. 223-27 | Seuils ; demande du tiers du capital ; majorité des associés | [V] | F09 § 3.3, § 18 |
| C. com. L. 821-40 I, L. 821-44, L. 821-46 | Organe ; six exercices ; trois exercices sur option | [V] | F09 § 3.4-3.5, § 13, § 18 |

### 3.3 Demande de la gérance et situation de M. CASTAING (1,5 pt)

**Demande de la gérance (0,75 pt)**
- **Qualification (0,5 pt)** : animer l'inventaire tournant, c'est établir les quantités en stock ; concevoir l'outil de dépréciation, c'est produire l'estimation qui fixera la valeur nette du stock dès 2026. Le cabinet se prononcerait ensuite sur des éléments issus de ses propres travaux : **risque d'autorévision** [V code de déontologie art. 5 II]. Il participerait aussi à des tâches de gestion, alors que sa mission s'exerce à l'exclusion de toute **immixtion dans la gestion** [V L. 821-54 I]. ASPÈDE n'est pas une entité d'intérêt public : il n'y a pas de liste fermée de services interdits, mais le cabinet ne peut accepter une prestation qui crée un risque d'autorévision sans sauvegarde possible [V L. 821-28 IV ; A. 821-55 § 23-30]. Le stock (6 480 000 €, près de la moitié du total du bilan) et sa dépréciation sont au cœur des comptes : aucune sauvegarde ne supprime le risque.
- **Conduite (0,25 pt)** : le cabinet **refuse** les deux demandes, y compris par l'intermédiaire de son activité d'expertise comptable, exercée par la même structure. Les comptages et l'estimation restent de la responsabilité de la gérance. Dans le cadre de l'audit, le cabinet peut observer des comptages et faire part de ses constats sur la méthode de dépréciation, sans la concevoir [S, application].

**Situation de M. CASTAING (0,75 pt)**
- **Qualification (0,5 pt)** : les époux ont un **lien personnel** au sens du code [V art. 32 I 3°]. Mme CASTAING siège au comité de direction, négocie les remises de fin d'année et propose les dépréciations : c'est un **cadre dirigeant pouvant influer sur l'établissement des comptes**, donc une **fonction sensible** [V art. 31 al. 2 c) ; S, qualification]. M. CASTAING n'est ni le signataire ni un membre de la direction du cabinet : le lien n'est pas incompatible de plein droit [V art. 32 II], mais il l'est si un tiers objectif, raisonnable et informé conclurait que l'indépendance est compromise malgré les sauvegardes [V art. 32 III]. Le risque est élevé : il est chargé précisément du cycle que dirige son épouse, sur les remises et la dépréciation.
- **Conduite (0,25 pt)** : le cabinet en tire **sans délai** les conséquences [V art. 35] : il retire M. CASTAING de l'équipe d'ASPÈDE (comptes et durabilité) et de l'accès au dossier, fait revoir par un autre membre ses travaux de l'intervention intermédiaire de novembre 2026, documente l'analyse et en informe la gérance [V A. 821-55 § 23-30, § 41-43 ; S, choix des mesures]. Avec ces sauvegardes, la mission peut se poursuivre.

**Réponses tolérées**
- La qualification de Mme CASTAING comme non sensible, si le candidat retient néanmoins une situation à risque et le retrait de M. CASTAING de l'équipe : 0,25 pt sur 0,5 en qualification.

**Erreurs fréquentes**
- Admettre la prestation au motif que le cabinet est aussi expert-comptable, en confondant l'indépendance du commissaire aux comptes et celle de l'expert-comptable (`JUR-A03`).
- Conclure à la démission du cabinet alors qu'une sauvegarde suffit pour un collaborateur (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 5, 31, 32, 35 | Autorévision ; fonctions sensibles ; liens personnels ; survenance | [V] ; application : [S] | F10 § 2.1, § 4.1, § 14 |
| C. com. L. 821-28 IV, L. 821-54 I ; A. 821-55 § 23-30, § 41-43 | Hors entité d'intérêt public ; non-immixtion ; sauvegardes ; documentation | [V] | F10 § 5, § 12 ; F09 § 6 |

### 3.4 Portée de la certification (1,5 pt)

- **Définition et objectif (0,5 pt)** : le cabinet certifie, en justifiant de ses appréciations, que les comptes annuels sont **réguliers et sincères et donnent une image fidèle** du résultat, de la situation financière et du patrimoine ; il formule une **opinion** après un audit des comptes [V L. 821-53 al. 1 ; NEP principes § 01]. L'opinion porte sur les **comptes pris dans leur ensemble**, non sur chaque article.
- **Assurance raisonnable (0,5 pt)** : l'assurance est élevée mais **non absolue** : elle porte sur l'absence d'**anomalies significatives**, appréciées au regard du **seuil de signification** (130 000 € en 2026) [V NEP principes § 04, § 08 ; NEP caractère significatif § 6]. Le cabinet ne compte ni ne valorise les 31 000 références : il collecte des éléments par **sélection d'éléments et sondages**, selon son évaluation des risques [V NEP éléments probants § 8 ; NEP sélection § 04].
- **Limites et responsabilités (0,5 pt)** : les sondages, les limites propres aux procédures de l'entité et des éléments qui conduisent à des présomptions plus qu'à des certitudes empêchent toute garantie [V NEP principes § 09] ; la certification ne garantit pas non plus la qualité de la gestion [V L. 821-55]. Les comptes, donc l'inventaire, sont établis par la gérance : l'**inventaire tournant** est une procédure d'ASPÈDE que le cabinet ne remplace pas ; il s'appuie sur elle et sur les comptages de clôture [S, application]. Le message du gérant à la banque est inexact et devrait être rectifié.

**Erreurs fréquentes**
- Présenter la certification comme une garantie d'exactitude article par article (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-55 ; NEP principes § 01, § 04, § 08-09 | Objectif ; anomalie significative ; assurance raisonnable ; limites | [V] | F11 § 1.1 |
| NEP caractère significatif § 6 ; NEP éléments probants § 8 ; NEP sélection § 04 | Seuil ; sélection et sondages | [V] | F11 § 4.2, § 6.1, § 21 |

### 3.5 Cycle achats, fournisseurs et stocks (6 pts)

**a. Risques et assertions (2,5 pts)**
- **Risque inhérent élevé (0,5 pt)** : stock de 6 480 000 €, soit 46,9 % du total du bilan et près de cinquante fois le seuil de signification ; 31 000 références sur quinze sites, dont un entrepôt tiers ; importations dont le transfert de propriété dépend du contrat ; **estimations** (dépréciation, remises) ; résultat en baisse (515 000 € contre 642 000 €) et négociation d'un prêt, qui incitent la gérance à présenter un résultat favorable [V NEP risques § 02 ; S, application].
- **Six situations (1,5 pt ; 0,25 pt par situation rattachée au bon risque et à la bonne assertion)** :

| Situation | Risque | Assertions |
|---|---|---|
| 1. Transit | Lot HANAM (214 000 €) appartenant à ASPÈDE au 31/12/2026 mais non compté ; commande portugaise (87 000 €) comptabilisée en achats alors qu'elle n'appartient pas encore à ASPÈDE | Stock : **exhaustivité**, **droits et obligations** ; achats : **séparation des exercices** ; dette : **existence** |
| 2. Réceptions non facturées | Charge à payer forfaitaire, sans rapprochement avec les 46 réceptions | Dettes : **exhaustivité**, **évaluation** ; achats : **séparation des exercices** |
| 3. Remises de fin d'année | Remises acquises en 2026 non enregistrées : achats surévalués | Remises obtenues (en déduction des achats) : **exhaustivité**, **séparation des exercices**, **mesure** ; créance : **exhaustivité** |
| 4. Collections passées | Taux forfaitaire inchangé depuis 2019, collection 2025 non dépréciée, dénouement défavorable | Stock : **évaluation et imputation** |
| 5. Stock chez VERDALANE | Comptage par le seul prestataire, marchandises d'autres clients dans l'entrepôt | Stock : **existence**, **droits et obligations** |
| 6. Écarts d'inventaire | Démarque multipliée par plus de deux et supérieure à 6 % dans deux magasins, ajustée sans analyse | Stock : **existence** ; ajustement : **mesure** |

- **Risque lié au contrôle élevé (0,5 pt)** : aucun rapprochement des réceptions et des factures, remises calculées après la clôture et jamais enregistrées, dépréciations arrêtées par le seul gérant sur la proposition d'une responsable des achats nouvellement nommée, comptage de l'entrepôt sans contrôle d'ASPÈDE, écarts non analysés. Le cabinet ne peut pas s'appuyer sur ces procédures : **procédures de substance étendues** à la clôture [V NEP principes § 11, § 13 ; NEP risques § 02].

**b. Procédures (2 pts ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 2 pts)**
- **Inspection du contrat, du document de transport (date de chargement) et des factures** des commandes en transit ; vérification de l'inclusion du lot HANAM dans le stock et de l'annulation de l'achat portugais : droits et obligations, exhaustivité, séparation des exercices.
- **Rapprochement des bons de réception** des derniers jours de décembre et des premiers jours de janvier avec les factures et la charge à payer : séparation des exercices, exhaustivité des dettes.
- **Revue des factures reçues et des règlements de janvier et février 2027** : exhaustivité des dettes fournisseurs.
- **Analyse des remises par fournisseur** : lecture des contrats, rapprochement des achats facturés avec la comptabilité, recalcul, comparaison avec les avoirs reçus en 2027 : exhaustivité, mesure.
- **Revue de l'écoulement des stocks après la clôture** (ventes des soldes par collection, prix pratiqués) : évaluation (question 3.5 c).
- **Demande d'informations à VERDALANE** (quantités au 31/12/2026, procédures de comptage) et **rapprochement de ses états mensuels** avec le logiciel d'ASPÈDE : existence, droits et obligations (question 3.6).
- **Analyse des écarts d'inventaire** par magasin (Bayonne, Tarbes), entretiens avec les chefs de magasin et recomptage d'un échantillon d'articles : existence, mesure.
- **Procédures analytiques** : rotation du stock par collection, marge brute mensuelle autour de la clôture, achats par fournisseur : cohérence, séparation des exercices [V NEP éléments probants § 10].
- **Contrôle du coût d'entrée** des articles en stock (factures, remises attendues) : évaluation.
- **Déclarations écrites** de la gérance sur l'exhaustivité des dettes, les remises et les hypothèses de dépréciation [V NEP déclarations § 1-4].

**c. Application de l'extrait de la NEP estimations à la dépréciation des collections (1,5 pt)**
- **Dénouement et hypothèses (0,5 pt)** : le cabinet examine le **dénouement** de l'estimation antérieure [V NEP estimations § 14] : au 31/12/2025, les collections 2023 et antérieures (300 000 €) étaient dépréciées de 25 % (75 000 €), soit une valeur nette de 225 000 € ; elles ont été vendues pour 132 000 € nets, 44 % de leur coût, soit une perte de 93 000 € au-delà de la dépréciation. Le taux de dépréciation et l'absence de dépréciation de la collection précédente sont des **hypothèses importantes** [V § 09] que ce dénouement contredit.
- **Procédures (0,75 pt)** : le cabinet combine les trois voies de la norme [V § 16] : **événements postérieurs** à la clôture, c'est-à-dire les prix et les quantités vendus pendant les soldes de janvier et de février 2027, collection par collection, qui confirment ou infirment les hypothèses [V § 17] ; **appréciation du processus** : une méthode forfaitaire inchangée depuis 2019 n'est pas appropriée au regard de la règle comptable, qui compare le coût au prix de vente estimé net des coûts de sortie ; fiabilité des données (classement des articles par collection dans le logiciel) ; exactitude des calculs ; **indices de biais**, le gérant refusant de modifier le taux pour ne pas dégrader le résultat présenté à la banque [V § 19, § 26] ; à défaut de révision, **estimation propre** ou fourchette étayée [V § 23-24], fondée ici sur les prix observés depuis la clôture (annexe 3.7).
- **Conclusion (0,25 pt)** : le cabinet tient compte des éléments qui contredisent l'estimation [V § 26] ; l'écart entre son estimation et celle de la gérance est une **anomalie**, quantifiée à la question 3.7 ; il demande des **déclarations écrites** sur les méthodes, les données et les hypothèses [V § 28].

**Réponses tolérées**
- En a., le rattachement de la situation 6 à un risque de fraude (vols), si l'assertion d'existence est retenue.
- En c., une estimation sous forme de fourchette, si les deux bornes sont étayées par les ventes postérieures à la clôture.

**Erreurs fréquentes**
- Recopier l'extrait de norme sans l'appliquer aux collections d'ASPÈDE (`JUR-A06`).
- Confondre existence (solde) et réalité (flux), ou séparation des exercices et exhaustivité (`JUR-A01`).
- Proposer des procédures sans objectif ni assertion (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 11-13 ; NEP risques § 02 | Risque inhérent, risque lié au contrôle ; facteurs | [V] ; application : [S] | F11 § 4.1 |
| NEP éléments probants § 9-10 ; NEP déclarations § 1-4 | Assertions ; techniques ; déclarations écrites | [V] | F11 § 4.3, § 6.2, § 12.3 |
| NEP estimations § 09, § 14, § 16-17, § 19, § 23-24, § 26, § 28 | Hypothèse importante ; dénouement ; procédures ; biais ; estimation du commissaire aux comptes ; déclarations | [V] | F11 § 17.1, § 23.1 |
| PCG 213-31, 214-5, 214-6 | Coût d'acquisition net des remises ; dépréciation ; valeur vénale nette des coûts de sortie | [V] (règles données en annexe) | F11 § 15.3 |

### 3.6 Réponse de VERDALANE Logistique (1,5 pt)

- **Droit d'information (0,5 pt)** : le commissaire aux comptes peut recueillir **toutes informations utiles** à sa mission auprès des **tiers qui ont accompli des opérations pour le compte** de l'entité [V L. 821-61 al. 2]. VERDALANE reçoit, stocke et expédie les marchandises d'ASPÈDE : les quantités détenues et ses procédures de comptage sont des informations que le cabinet peut lui demander. La clause de confidentialité est stipulée au profit d'ASPÈDE, qui en a délié son prestataire par son accord écrit ; ce n'est pas un secret professionnel, et seuls les auxiliaires de justice peuvent opposer un secret au commissaire aux comptes [V L. 821-61 al. 3 ; S, qualification de la clause].
- **Limites (0,5 pt)** : ce droit d'information ne s'étend pas à la **communication des pièces et documents** détenus par le tiers (relevés de comptage, fichiers de mouvements) sans une **autorisation de justice**, donnée par le président du tribunal de commerce statuant en référé [V L. 821-61 al. 2 ; D. 821-175]. Les investigations sur place portent sur l'entité et les entités liées : le cabinet ne peut imposer une visite de l'entrepôt d'un tiers [V L. 821-60, L. 821-61 al. 1 ; S, application].
- **Autres moyens (0,5 pt)** : le cabinet se fait communiquer **sur place, chez ASPÈDE**, le contrat et les états mensuels de VERDALANE [V L. 821-60] ; il demande au gérant d'écrire à VERDALANE pour qu'elle réponde **directement au cabinet** à une demande de confirmation dont le cabinet maîtrise l'envoi et la réception [V NEP éléments probants § 10] ; il accompagne ASPÈDE lors de la visite que le contrat lui permet, pour des comptages par sondages ; il rapproche les états mensuels du logiciel d'ASPÈDE et examine les expéditions et les ventes de janvier 2027 des articles détenus dans l'entrepôt [S, procédures alternatives]. Sans éléments suffisants sur 4 050 000 € de stock (31,15 fois le seuil), la limitation aurait des incidences difficiles à circonscrire : réserve pour limitation, voire impossibilité de certifier [V NEP rapport § 11, § 14 ; calcul].

**Réponses tolérées**
- L'analyse de la clause de confidentialité comme opposable tant qu'ASPÈDE n'en a pas délié VERDALANE, si le candidat en tire la nécessité d'une demande écrite du gérant : points complets en droit d'information.

**Erreurs fréquentes**
- Affirmer que le commissaire aux comptes peut exiger du tiers la communication de ses documents sans décision de justice (`JUR-A01`).
- Traiter le prestataire comme un fournisseur et développer la confirmation des soldes fournisseurs (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-60, L. 821-61 ; D. 821-175 | Communication sur place ; informations des tiers ; pièces sur autorisation ; secret | [V] ; qualification : [S] | F09 § 5 ; F11 § 2, § 23.2 |
| NEP éléments probants § 10 ; NEP rapport § 11, § 14 | Confirmation des tiers ; limitation | [V] | F11 § 6.2-6.3, § 8.1 |

### 3.7 Anomalies, écritures et opinion (2 pts)

**Calcul des anomalies (0,5 pt)**
- **Remises de fin d'année (0,25 pt)** : BRESCALE : 3 % × 1 840 000 = 55 200 € ; ORVALDE : 4 % × (2 450 000 − 1 000 000) = 58 000 € ; SERNALIA : achats de 1 150 000 € inférieurs au palier de 1 200 000 €, aucune remise ; HANAM : 2 % × 1 740 000 = 34 800 €. Total : **148 000 €** de remises acquises en 2026 et non enregistrées.
- **Dépréciation des collections (0,25 pt)** : collection 2025 : (100 % − 85 %) × 640 000 = 96 000 € ; collections 2024 et antérieures : (100 % − 40 %) × 380 000 = 228 000 € ; dépréciation nécessaire 324 000 €, contre 95 000 € comptabilisés : **insuffisance de 229 000 €**.

**Écritures de correction au 31/12/2026 (0,5 pt ; 0,25 pt par écriture)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 4098 | Rabais, remises, ristournes à obtenir et autres avoirs non encore reçus | 148 000 | |
| | 609 | Rabais, remises et ristournes obtenus sur achats | | 148 000 |

Libellé : remises de fin d'année 2026 à obtenir de BRESCALE, ORVALDE et HANAM (écriture X1, équilibrée).

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 68173 | Dotations pour dépréciations des actifs circulants – Stocks et en-cours | 229 000 | |
| | 397 | Dépréciations des stocks de marchandises | | 229 000 |

Libellé : complément de dépréciation des collections 2025 et antérieures (324 000 − 95 000) (écriture X2, équilibrée). Après les deux corrections, le résultat, avant effet d'impôt, est de 515 000 + 148 000 − 229 000 = **434 000 €**, et les capitaux propres de 4 654 000 €.

**Caractère significatif (0,25 pt)** : 148 000 / 130 000 = **1,14** fois le seuil ; 229 000 / 130 000 = **1,76** fois le seuil. Chaque anomalie est significative **à elle seule** ; elles s'apprécient individuellement et en cumul [V NEP anomalies § 14]. Leur effet net sur le résultat (81 000 €, 0,62 fois le seuil) ne les compense pas : elles affectent des postes différents (créances et produits d'un côté, stocks et charges de l'autre), et la dépréciation insuffisante révèle un **biais** de la gérance, significatif aussi par sa nature [V NEP caractère significatif § 9 ; NEP estimations § 26].

**Opinion selon la décision de la gérance (0,5 pt)**
- **Les deux anomalies sont corrigées** : il ne reste que 12 000 € d'anomalies non corrigées, non significatives : **certification sans réserve** ; le cabinet communique ces anomalies à la gérance et obtient une déclaration écrite à laquelle en est joint l'état [V NEP anomalies § 15-17 ; NEP rapport § 08].
- **Seules les remises sont corrigées** : il reste 229 000 + 12 000 = 241 000 € (1,85 fois le seuil) ; le résultat publié (663 000 €) dépasserait de 229 000 € le résultat corrigé : **certification avec réserve pour désaccord**, les incidences étant circonscrites à une estimation quantifiée [V NEP rapport § 09-10].
- **Aucune anomalie n'est corrigée** : deux désaccords significatifs, clairement circonscrits et quantifiables : **certification avec réserve pour désaccord**, motivée par les deux points. Ce n'est pas un refus de certifier : les incidences sont circonscrites et une réserve chiffrée suffit au lecteur [V NEP rapport § 09-10, § 12-13 ; S, qualification].

**Parties du rapport, dernier cas (0,25 pt)** : la partie « **Opinion avec réserve** » indique que, sous ces réserves, les comptes sont réguliers et sincères et donnent une image fidèle ; la partie « **Fondement de l'opinion avec réserve** » expose les deux motifs et leur incidence (remises non enregistrées : créances et résultat sous-évalués de 148 000 € ; dépréciation insuffisante : stocks et résultat surévalués de 229 000 €). Les motifs sont communiqués au préalable à la gérance ; le rapport est destiné aux associés [V NEP rapport § 06, § 18 ; R. 821-180].

**Réponses tolérées**
- L'enregistrement des remises au compte 6097 (subdivision du compte 609 pour les achats de marchandises) : points complets.
- Une seule écriture regroupant les deux corrections, si les comptes et les montants sont justes : points complets en écritures.

**Erreurs fréquentes**
- Compenser les deux anomalies et conclure à une certification sans réserve (`JUR-A02`).
- Calculer une remise SERNALIA alors que le palier n'est pas atteint, ou appliquer le taux d'ORVALDE à la totalité des achats (`JUR-F02`).
- Écriture sans libellé ou sans numéro de compte (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP caractère significatif § 9 ; NEP anomalies § 14-17 ; NEP estimations § 26 | Montant et nature ; appréciation individuelle et cumulée ; biais | [V] | F11 § 4.2, § 14.1, § 17.1 |
| NEP rapport § 06, § 08-10, § 12-13, § 18 ; R. 821-180 | Opinions ; parties du rapport | [V] | F11 § 8 |
| Liste des comptes du PCG | 4098, 609, 68173, 397 | [V] | F11 § 23.3 |

### 3.8 Responsabilités au titre de la vérification de 2025 (2,5 pts)

**Fondement et comparaison (0,5 pt)** : le cabinet a vérifié les informations de 2025 en qualité de **commissaire aux comptes**, dans les conditions de la certification légale (hypothèse), le rapport étant signé par Mme BERGOUIGNAN, inscrite sur la liste « durabilité » [V L. 821-26]. Sa responsabilité civile repose sur le **même texte** que pour la certification des comptes : il répond, envers l'entité **et les tiers**, des conséquences dommageables de ses **fautes et négligences** dans l'exercice de sa profession [V L. 821-37 al. 1] ; un organisme tiers indépendant répondrait dans les mêmes termes [V L. 822-14]. La banque, tiers, doit établir une **faute**, un **préjudice** et un **lien de causalité** [S]. La différence tient au **niveau d'assurance** : la mission de durabilité repose sur une assurance **limitée** (vérifications moindres en nature, en étendue et en durée ; conclusion sous une forme négative), la certification des comptes sur une assurance raisonnable ; la diligence attendue s'apprécie au regard de ce niveau [V LD 2026, « Niveau d'assurance » ; NEP principes § 08 ; S, déduction].

**Faute (0,75 pt)** : la mission est une **obligation de moyens** ; un avis de conformité n'est pas une garantie de l'exactitude de chaque donnée [S]. Mais la part des ventes d'occasion était une donnée « **vérifiée spécifiquement** », en raison des attentes de la banque [V LD 2026 § 8.3.1]. Le dossier montrait que les ventes en ligne représentaient 30 % des ventes d'occasion publiées et qu'une mise à jour du logiciel du site avait modifié le codage des retours : le risque était identifié, et l'échantillon de 30 tickets n'a porté que sur les magasins ; la déclaration écrite de la gérance ne remplace pas un élément probant sur un risque connu. L'erreur est importante : 1 154 520 € de ventes publiées contre 983 480 € réelles, soit 171 040 € d'articles neufs classés en occasion (près de la moitié des 346 356 € de ventes d'occasion en ligne publiées), et un taux qui passe de 5,4 % à 4,6 %, sous le seuil de 5 % fixé par le prêt. Une **négligence** paraît caractérisée, même en assurance limitée [S, application].

**Préjudice et lien de causalité (0,75 pt)** : l'erreur est d'abord celle d'ASPÈDE, qui établit les informations. Surtout, le contrat de prêt prévoit que la diminution de taux cesse à l'échéance suivante et que l'emprunteur **reverse** les intérêts dont il a été dispensé à tort : la banque récupère ces intérêts auprès d'ASPÈDE, et les 42 000 € réclamés (6 000 € par an sur sept ans) correspondent à une perte qu'elle ne subira pas. Cette perte est d'ailleurs hypothétique même sans la clause : la diminution dépend du dernier état vérifié, et elle redeviendrait due si l'état de 2026 atteint 5 % (6,3 % dans le projet, sous réserve des vérifications de la question 3.11). Faute de **préjudice** certain, la demande n'est pas fondée ; seul un préjudice résiduel (insolvabilité de l'emprunteur, frais) pourrait être recherché, dans la mesure où la négligence du cabinet y a contribué [S]. Le cabinet est couvert par l'assurance obligatoire de sa responsabilité civile [V R. 821-85, R. 821-109].

**Responsabilité disciplinaire (0,5 pt)** : comme pour la certification des comptes, la H2A sanctionne le commissaire aux comptes pour un manquement aux conditions légales d'exercice, une **négligence grave** ou un fait contraire à la probité ou à l'honneur, de l'avertissement à la radiation, avec d'éventuelles sanctions pécuniaires ; elle vise la société et la signataire, indépendamment de l'action civile [V L. 821-70 I, L. 821-71]. Un échantillon mal conçu sur une donnée d'une mission d'assurance limitée est une négligence, mais pas nécessairement une négligence grave : une sanction paraît peu probable, sans être exclue si le contrôle révélait d'autres insuffisances [S]. Le cabinet doit en tirer les leçons pour 2026 (question 3.11 b).

**Réponses tolérées**
- La conclusion qu'aucune faute n'est caractérisée, si le candidat motive par le niveau d'assurance limitée et la déclaration écrite : 0,25 pt sur 0,75 en faute ; points complets ailleurs.
- La mention de la responsabilité pénale, réservée aux faits intentionnels et absente ici, en une phrase : ni points ni pénalité.

**Erreurs fréquentes**
- Présenter l'assurance limitée comme une absence de responsabilité, ou à l'inverse comme une garantie des chiffres (`JUR-A01`).
- Retenir le montant réclamé sans examiner la clause du contrat de prêt (`JUR-F07`).
- Développer la procédure de mise en cause, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-26, L. 821-37, L. 822-14 ; R. 821-85, R. 821-109 | Signature ; responsabilité civile du commissaire aux comptes et de l'organisme tiers indépendant ; assurance | [V] ; conditions : [S] | F09 § 7.1, § 13, § 15 |
| C. com. L. 821-70 I, L. 821-71 | Faute disciplinaire ; sanctions | [V] ; application : [S] | F09 § 7.2 |
| LD 2026, « Niveau d'assurance », § 8.3.1 ; NEP principes § 08 | Assurance limitée et raisonnable ; informations vérifiées spécifiquement | [V] | F13 § 2.3, § 7 ; F11 § 1.1 |

---

### Partie B – Durabilité (12 points)

### 3.9 Étendue et limites des informations, question du gérant et demandes de la banque (2 pts)

- **Étendue (0,75 pt)** : l'état de durabilité conforme aux ESRS donne, pris comme un tout, une **image fidèle** de tous les impacts, risques et opportunités **matériels** et de la manière dont l'entreprise les gère [V ESRS 1 (2026) § 3]. Il comprend toujours les **informations générales** (base de préparation, gouvernance, stratégie, processus d'analyse de matérialité) et, pour **chaque thème matériel** retenu par l'analyse de double matérialité, les informations sur les politiques, les actions, les indicateurs et les cibles (ou l'indication qu'il n'en existe pas), complétées par les exigences pertinentes des normes thématiques [V ESRS 1 (2026) § 25, § 29 ; ESRS 2 § 38-39]. Pour ASPÈDE, cela vise les cinq sujets retenus, dont les conditions de travail chez les fabricants et la conduite des affaires.
- **Limites (0,5 pt)** : l'entreprise ne publie pas les informations d'une exigence des ESRS **sans importance matérielle** [V ESRS 1 (2026) § 24] ; les informations peuvent reposer sur des **estimations**, dont les hypothèses sont expliquées [V § 88] ; l'état n'est pas un état financier et sa vérification ne procure qu'une assurance limitée (question 3.11).
- **Question du gérant (0,25 pt)** : publier volontairement permet de choisir le référentiel, non de choisir ses sujets à l'intérieur des ESRS : l'état ne peut se déclarer conforme que s'il traite **tous les thèmes matériels**. Mais il ne doit pas « tout publier » : ce qui n'est pas matériel en est exclu, sauf informations supplémentaires signalées [V § 24, § 29, § 107-109 ; S, application].
- **Demandes de la banque (0,5 pt)** : 1) les informations prévues par le référentiel de la **taxonomie** ne sont exigées que des entreprises tenues de les publier ; ASPÈDE n'y est pas tenue et la mission ne comporte pas cet axe (annexe 3.10) [V L. 821-54 II ; S, application] ; 2) les ESRS portent sur les impacts, risques et opportunités matériels **de l'entreprise** : ils n'imposent pas une empreinte environnementale **article par article** [S, lecture de l'architecture des ESRS] ; 3) le chiffre trimestriel des ventes d'occasion, non matériel, peut figurer dans l'état pour répondre aux **demandes d'un utilisateur spécifique**, à condition d'être **clairement signalé** comme ne résultant pas de l'évaluation de la matérialité, de donner une image fidèle et de ne pas obscurcir les informations matérielles [V ESRS 1 (2026) § 108-109].

**Réponses tolérées**
- La mention des informations de la taxonomie comme informations supplémentaires possibles, signalées comme telles, si l'absence d'obligation est indiquée.
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences », « déclaration relative à la durabilité »).

**Erreurs fréquentes**
- Admettre qu'une entreprise qui publie volontairement peut choisir ses sujets tout en se déclarant conforme aux ESRS, ou à l'inverse exiger la publication d'informations non matérielles (`JUR-A05`).
- Détailler le contenu d'une norme thématique ou calculer une donnée, ce qui n'est pas demandé (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 3, § 24-25, § 29, § 88, § 107-109 ; ESRS 2 § 38-39 | Image fidèle ; informations matérielles ; estimations ; informations supplémentaires | [V] ; application : [S] | F12 § 2, § 5, § 8, § 14, § 17 |
| C. com. L. 821-54 II | Axe taxonomie réservé aux entreprises soumises | [V] ; application : [S] | F13 § 2.1 ; F12 § 11 |

### 3.10 Définition du reporting de durabilité et exigences générales (4 pts)

**a. Définition et situation par rapport aux comptes annuels (1,5 pt)**
- **Définition (0,5 pt)** : le reporting de durabilité réunit les informations qui permettent de comprendre les **impacts** de l'activité de l'entreprise sur les enjeux environnementaux, sociaux et de gouvernance, et la manière dont ces enjeux influent sur l'évolution de ses affaires, de ses résultats et de sa situation [V L. 232-6-3 I, définition de l'objet légal, transposable à une publication volontaire : S]. Il repose sur la **double matérialité** et s'adresse aux investisseurs et prêteurs, comme la banque d'ASPÈDE, et aux autres parties prenantes [V ESRS 1 (2026) § 3-4].
- **Situation (1 pt ; 0,25 pt par élément)** :
  - **entité** : l'état porte sur la même entreprise déclarante que les états financiers [V ESRS 1 (2026) § 60] : ASPÈDE seule, sans filiale ; la base de préparation est conforme ;
  - **période** : celle des états financiers, y compris pour les indicateurs [V § 76] : l'exercice 2026, du 01/01 au 31/12. Les données sociales arrêtées au 30/09/2026 ne respectent pas cette règle : la gérance doit les établir au 31/12/2026 ;
  - **place** : une section distincte du rapport de gestion, où les informations conformes aux ESRS sont clairement distinguées des autres [V § 104 a) ; hypothèse de l'énoncé] ;
  - **liens avec les comptes** : le chiffre d'affaires de 22 640 000 €, dénominateur de la part des ventes d'occasion, et les consommations d'électricité, comptabilisées en charges, se retrouvent dans les comptes ; l'état explique ces liens [V § 112]. Il en diffère par son objet (impacts, risques et opportunités, informations qualitatives et prospectives, chaîne de valeur) et par le niveau d'assurance de sa vérification.

**b. Exigences générales appliquées au projet (2,5 pts)**
- **Caractéristiques qualitatives (1 pt)** : l'image fidèle impose des informations **pertinentes** et une **représentation fidèle** (description complète, neutre et précise), ainsi que des informations **comparables, vérifiables et compréhensibles** [V ESRS 1 (2026) § 19-20 ; appendice B]. Dans le projet : le taux de satisfaction de 97 %, tiré d'un sondage oral sans trace, n'est **pas vérifiable** et, présenté sans réserve, n'est pas **neutre** : la gérance le retire ou le fonde sur une enquête documentée (0,5 pt) ; la baisse de 23,7 % compare un chiffre de 2026 tiré d'un tableau de suivi à celui de 2025, qui couvrait les quatorze magasins : la **comparabilité** et la **complétude** sont à vérifier (question 3.12) (0,25 pt) ; le « mot du gérant » et la charte, de nature promotionnelle, sont distingués des informations établies selon les ESRS [V § 104 a)] (0,25 pt).
- **Horizons de temps (0,5 pt)** : le **court terme** est la durée de la période des états financiers, soit un an ; le moyen terme va jusqu'à cinq ans, le long terme au-delà [V § 79]. Une autre définition n'est admise que pour le moyen ou le long terme, si les horizons de la norme donnent des informations non pertinentes (horizons de gestion, cycles du secteur), et avec une explication [V § 81]. Le court terme de trois ans est contraire à la norme ; la gérance revient aux horizons de la norme ou justifie ses définitions du moyen et du long terme.
- **Estimations et incertitudes (0,5 pt)** : l'entreprise publie ses jugements importants, les principales **incertitudes** et les principales **hypothèses et limites** de ses estimations [V § 88]. Les ventes d'occasion en ligne de l'année (393 600 €, soit 27,6 % des 1 426 320 € publiés) sont extrapolées du seul dernier trimestre, dont la saisonnalité peut fausser le résultat, sans que le projet le dise. Une estimation raisonnable reste utile si ses hypothèses sont expliquées [V AR 42-43] : la gérance décrit la méthode et ses limites, ou utilise des données plus complètes.
- **Structure (0,5 pt)** : l'état est structuré en **quatre parties, dans l'ordre** : informations générales, environnementales, sociales et sur la gouvernance ; une autre structure exige une explication motivée [V § 105]. Le projet ouvre sur le mot du gérant, place le personnel avant l'environnement, mêle fournisseurs et conduite des affaires et relègue les informations générales dans une note finale : la gérance réorganise l'état (ou motive sa structure).

**Réponses tolérées**
- En b., le rattachement du chiffre de 97 % à la complétude ou à la neutralité plutôt qu'à la vérifiabilité, si la correction proposée est adaptée.
- En a., le rattachement de la date du 30/09/2026 aux caractéristiques qualitatives (comparabilité), si la règle de la période est énoncée.

**Erreurs fréquentes**
- Faire de la connectivité ou du périmètre le thème de la réponse, ou réciter les exigences générales sans les appliquer au projet (`JUR-A06`).
- Admettre un court terme de trois ans au motif que l'entreprise publie volontairement (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 232-6-3 I ; ESRS 1 (2026) § 3-4, § 60, § 76, § 104, § 112 | Définition ; utilisateurs ; entité ; période ; présentation ; liens | [V] ; application à une publication volontaire : [S] | F12 § 2, § 9, § 14 |
| ESRS 1 (2026) § 19-20, appendice B, § 79-82, § 88, AR 42-43, § 105 | Caractéristiques qualitatives ; horizons ; estimations ; structure | [V] | F12 § 5, § 14, § 17 |

### 3.11 Mission du cabinet, démarche et procédures (4,5 pts)

**a. Objectifs, assurance et axes (2 pts)**
- **Objectifs (0,75 pt)** : le cabinet émet un **avis** sur la conformité aux ESRS du **processus** mis en œuvre pour déterminer les informations publiées (analyse de double matérialité) et sur la conformité des **informations** publiées [V L. 821-54 II ; LD 2026 § 2]. La mission est volontaire, conduite dans les conditions de la certification légale (hypothèse), confiée pour trois exercices ; le rapport est destiné aux associés. Distincte de la certification des comptes, elle donne lieu à des échanges avec l'équipe d'audit des comptes (charges d'électricité, chiffre d'affaires) [V LD 2026 § 3.2]. Elle ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].
- **Assurance limitée et « garantie » (0,75 pt)** : l'assurance est **limitée** : vérifications moindres en nature, en étendue et en durée qu'une assurance raisonnable, conclusion sous une **forme négative** (le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes) [V LD 2026, « Niveau d'assurance »]. Les chiffres ne sont donc **pas garantis** : ni l'assurance limitée ni même l'assurance raisonnable des comptes ne sont des garanties ; la gérance reste responsable des informations, et l'erreur de 2025 l'illustre (annexe 3.8) [S, application].
- **Axes (0,5 pt)** : **axe 1**, le processus, et **axe 2**, les informations, sont applicables ; l'axe relatif à la **taxonomie** est sans objet, ASPÈDE n'étant pas tenue de publier ces informations et n'en publiant pas ; l'axe relatif au **balisage** est sans objet, aucune règle n'étant applicable [V LD 2026 § 2, § 10 ; L. 821-54 II ; S, application à une mission volontaire]. La consultation du comité social et économique n'entre pas dans la mission (lettre de mission).

**b. Étapes de la démarche et procédures (2,5 pts)**
- **Étapes (1 pt)** : lettre de mission (objectif, étendue, accès aux personnes et aux documents, lettre d'affirmation) ; **prise de connaissance** de l'entité et de son environnement (magasins, atelier, site en ligne, systèmes qui produisent les données : tableau de suivi de l'énergie, logiciels de caisse et du site) ; **planification**, avec la sélection des informations **vérifiées spécifiquement**, celles qui présentent un risque important de non-conformité ou de fortes attentes des utilisateurs : ici l'énergie des magasins et la part des ventes d'occasion, suivies par la banque ; **contrôle du processus** (axe 1, achevé sans anomalie) ; **contrôle de la conformité des informations** aux ESRS (axe 2) ; contrôle des exigences de publication de la taxonomie et du balisage, sans objet ; lecture d'ensemble et cohérence avec les comptes ; communication à la gérance et déclarations écrites ; **rapport** d'assurance limitée, par axe [V LD 2026 § 4-8, § 10-11, § 14, § 17 ; F13 § 3].
- **Procédures (1,5 pt ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 0,75 pt par donnée)** :
  - *Énergie des magasins* : **rapprochement** du tableau de suivi avec la liste des quatorze magasins et l'ensemble des contrats et factures d'électricité au nom d'ASPÈDE (exhaustivité) ; **rapprochement** avec les charges d'électricité comptabilisées et **échange avec l'équipe d'audit des comptes** (cohérence) ; **procédure analytique** de la consommation par magasin et par mètre carré, 2025 contre 2026, et recalcul de l'évolution sur une base comparable (exactitude, comparabilité) [V LD 2026 § 3.2, § 8.3.2].
  - *Part des ventes d'occasion* : **lecture de la définition** et contrôle du classement des articles, retours d'articles neufs exclus, **sur les deux canaux**, magasins et site, par un échantillon de tickets et de commandes, compte tenu de l'erreur de 2025 (exactitude) ; **rapprochement** des extractions des logiciels avec le chiffre d'affaires comptabilisé de 22 640 000 € (exhaustivité, cohérence) ; **examen de l'extrapolation** des ventes en ligne (données du dernier trimestre, saisonnalité, autres données disponibles) et de sa description dans l'état (caractère raisonnable de l'estimation, information sur les incertitudes) [V ESRS 1 (2026) § 88 ; LD 2026 § 8.3.2].

**Réponses tolérées**
- En b., une présentation des étapes dans l'ordre du programme (prise de connaissance, planification, contrôle de la conformité des informations et du processus, contrôle du balisage, contrôle des exigences de publication, rapport) : points complets.

**Erreurs fréquentes**
- Retenir l'axe relatif à la taxonomie pour une entreprise qui n'y est pas tenue, ou présenter l'assurance limitée comme une garantie (`JUR-A05`, `JUR-A01`).
- Proposer des procédures sans lien avec les deux données ni objectif (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; LD 2026 § 2, § 10, « Niveau d'assurance » | Objectifs ; axes ; assurance limitée | [V] ; application à une mission volontaire : [S] | F13 § 2 ; F12 § 11 |
| LD 2026 § 3.2, § 4-8, § 8.3.1-8.3.2, § 11, § 14, § 17 | Étapes ; informations vérifiées spécifiquement ; techniques ; échanges avec les commissaires aux comptes | [V] ; procédures : [S] | F13 § 3, § 7 |

### 3.12 Conclusion sur les informations publiées (1,5 pt)

- **La gérance corrige (0,5 pt)** : consommation de 1 686 + 444 = **2 130 MWh**, soit une baisse de **3,6 %** par rapport aux 2 210 MWh de 2025, et non de 23,7 % ; les autres points étant corrigés (hypothèse de l'annexe 3.10) : **avis de conformité** sur les informations [V LD 2026 § 17]. Le cabinet peut formuler une **observation** renvoyant à la description de l'estimation des ventes d'occasion en ligne [V LD 2026 § 17 ; F13 § 4.4].
- **La gérance ne corrige pas (0,75 pt)** : l'omission de 444 MWh (20,8 % de la consommation réelle) transforme une baisse de 3,6 % en une baisse affichée de 23,7 %, sur un thème matériel suivi par la banque : c'est une erreur non corrigée d'une importance telle qu'elle remet en cause la conformité des informations. Elle porte sur une donnée identifiée et chiffrable : ses incidences sont **clairement circonscrites**, et une réserve qui donne la consommation et l'évolution exactes suffit au lecteur : **avis de conformité assorti d'une réserve motivée** [V LD 2026 § 17 ; F13 § 4.3 ; S, qualification]. Ce n'est ni un avis de non-conformité, l'erreur ne privant pas de sens l'ensemble de l'état, ni une impossibilité, aucune limitation n'ayant empêché les vérifications.
- **Portée (0,25 pt)** : l'avis est émis **axe par axe** : l'avis de conformité sur le processus n'est pas affecté ; le rapport comporte une partie pour le processus et une pour les informations, sans partie sur la taxonomie ni sur le balisage ; la conclusion reste exprimée sous la forme négative de l'assurance limitée, « sous la réserve » décrite [V LD 2026 § 17 ; S, déduction de la structure par axe].

**Réponses tolérées**
- Un avis de non-conformité dans le second cas, si le candidat motive l'impossibilité de circonscrire l'erreur par l'importance de l'énergie dans la partie environnementale : 0,5 pt sur 0,75.

**Erreurs fréquentes**
- Remplacer la réserve par une observation, ou conclure à une impossibilité d'émettre un avis en l'absence de limitation (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 | Avis, réserve, non-conformité, observations, structure par axe | [V] ; qualification : [S] | F13 § 4.1-4.4 |
