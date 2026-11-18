# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 17

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 17/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.8 | `exercices/ex46_consolidation_ifrs_droits_potentiels_cout_amorti_location` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.6 | `exercices/ex47_fusion_endroit_valeur_reelle_soulte_plafond` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.12 | `exercices/ex48_audit_litiges_provisions_sem_perimetre` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 a Obligation de consolider, IFRS sur option et conséquences | `2.1.b` Contexte réglementaire et légal de la consolidation | 1,5 |
| 1.1 b Bases d'évaluation du cadre conceptuel | `2.1.a` Cadre conceptuel de l'IASB | 3 |
| 1.2 a Périmètre et droits de vote potentiels de PHYCOLIS | `2.1.c` Périmètre de consolidation | 2,5 |
| 1.2 b Lecture des comptes : intégration globale de PHYCOLIS | `2.1.d` Méthodes et information financière | 1 |
| 1.3 a Location du séchoir : PCG, IFRS 16, mesure initiale | `2.2.c` Homogénéisation, thèmes communs (locations) | 1,5 |
| 1.3 b Location : calculs de 2026 et tableau d'incidence | `2.2.c` Homogénéisation, thèmes communs (locations) | 2,5 |
| 1.3 c Location : écritures | `2.2.c` Homogénéisation, thèmes communs (locations) | 2 |
| 1.4 a Emprunt obligataire : évaluation, principe du TIE, ligne 2026 | `2.2.d` Instruments financiers | 1,5 |
| 1.4 b Emprunt : comparaison PCG / IFRS, impôt différé | `2.2.d` Instruments financiers | 1,5 |
| 1.4 c Emprunt : écritures | `2.2.d` Instruments financiers | 2 |
| 1.4 d Classement et évaluation de trois actifs financiers | `2.2.d` Instruments financiers | 2 |
| 1.5 a Comptes réciproques, mise en concordance, éliminations | `2.2.f` Comptes réciproques et résultats internes | 1,75 |
| 1.5 b Marge interne sur les stocks d'ARGUÉNOR | `2.2.f` Comptes réciproques et résultats internes | 1,75 |
| 1.5 c Obligations convertibles internes et dividende | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.6 a Frais d'acquisition des titres ARGUÉNOR | `2.2.g` Goodwill ; `2.2.c` Frais d'acquisition | 1 |
| 1.6 b Actif net identifiable, goodwill partiel, PNC, goodwill complet | `2.2.g` Écarts d'évaluation et goodwill | 2,5 |
| 1.6 c Écritures des écarts d'évaluation, résultat retraité | `2.2.g` Écarts d'évaluation et goodwill | 1,5 |
| 1.7 a Tableaux de partage | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.7 b Écritures d'élimination des titres et de partage | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.8 a Phases du processus ; concordance avant élimination | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.8 b Extrait de l'état de la situation financière | `2.3.a` Documents de synthèse consolidés | 3 |
| 1.8 c Résultat de base par action ; absence de dilution | `2.3.a` Documents de synthèse consolidés | 2,5 |
| 1.8 d Deux différences de présentation en ANC | `2.3.a` Documents de synthèse consolidés | 1,5 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = participations ne donnant pas le contrôle (PNC) ; `CAP_ELIM` = capital de la filiale éliminé ; `EA` = goodwill ; `DU` / `AMO_DU` = droit d'utilisation et ses amortissements ; `DL` = obligation locative ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat de l'écriture de bilan. Un suffixe désigne la société concernée (`RST.GOEMONS`, `261.KERVALGUE` : titres détenus par KERVALGUE).

---

### 1.1 Référentiel et bases d'évaluation (4,5 pts)

#### a. Obligation de consolider et IFRS sur option (1,5 pt)

**Obligation (0,5 pt).** KERVALGUE, société commerciale, contrôle de manière exclusive GOËMONS DU TRIEUX (100 %), ARGUÉNOR (70 %) et PHYCOLIS (question 1.2) : elle établit et publie des comptes consolidés [V C. com. L. 233-16 ; F03 § 1.1].

**Référentiel (0,5 pt).** Les IFRS adoptées par l'Union ne sont obligatoires que pour les comptes consolidés des sociétés dont les titres sont admis aux négociations sur un **marché réglementé** d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Euronext Growth est un système multilatéral de négociation, non un marché réglementé (annexe 1.1) : KERVALGUE pouvait appliquer le règlement ANC n° 2020-01 ; elle a choisi les IFRS, ce que le droit lui permet [V F03 § 1.2 ; C. com. L. 233-24].

**Ce que l'option implique (0,5 pt).** Le groupe applique l'ensemble des IFRS adoptées, sans pouvoir en écarter une, et des méthodes uniformes pour toutes les sociétés consolidées [V IFRS 10 § 19 ; F04 § 1] ; il s'y tient d'un exercice à l'autre, un changement n'étant admis que s'il donne une information fiable et plus pertinente [V IAS 8 § 14 ; F03 § 12]. Les comptes individuels de KERVALGUE et de ses filiales restent établis selon le PCG, qui sert de base à leur résultat imposable : chaque liasse est retraitée (location IFRS 16, coût amorti, frais d'acquisition en charges…), et chaque retraitement crée un écart avec la base fiscale, donc un impôt différé.

**Réponses tolérées** : référence au « règlement IAS » sans numéro ; option justifiée par « Euronext Growth n'est pas un marché réglementé » sans mention de l'article.

**Erreurs fréquentes** : IFRS présentées comme obligatoires « parce que la société est cotée » (Euronext Growth confondu avec un marché réglementé) ; IFRS présentées comme applicables aux comptes individuels ; IFRS 18 appliquée à 2026.

#### b. Bases d'évaluation (3 pts)

**Les bases d'évaluation du cadre conceptuel (1 pt).** Le cadre conceptuel de 2018 distingue deux familles de bases d'évaluation [S cadre de 2018 ; F03 § 7.2, § 13] :
- le **coût historique**, fondé sur le prix de la transaction qui a fait naître l'actif ou le passif, mis à jour pour sa consommation (amortissement), ses règlements et, pour les instruments financiers, par le **coût amorti**, qui étale au taux d'intérêt effectif l'écart entre le montant initial et le montant à l'échéance [V définition du coût amorti, IFRS 9, appendice A ; F03 § 13] (0,5 pt) ;
- la **valeur actuelle**, fondée sur des conditions de la date d'évaluation : **juste valeur**, prix qui serait reçu pour la vente d'un actif ou payé pour le transfert d'un passif lors d'une transaction normale entre des participants de marché [V définition reprise d'IFRS 13, IAS 16 § 6 ; F03 § 13] ; **valeur d'utilité** pour un actif ou **valeur d'exécution** pour un passif, valeurs actuelles des flux propres à l'entité ; **coût actuel** [S] (0,5 pt).

**Rattachement des trois éléments (1,25 pt)**

| Élément | Base | Montant au 31/12/2026 | Justification |
|---|---|---:|---|
| Emprunt obligataire | Coût historique : **coût amorti** | 6 972 200 | Passif financier évalué au coût amorti [V IFRS 9 § 4.2.1] : montant reçu net des frais (6 925 940), majoré chaque année des intérêts au taux effectif et diminué des coupons ; il rejoindra 7 175 000 € à l'échéance. Le nominal (7 000 000 €) n'est ni ce que le groupe a reçu, ni ce qu'il remboursera |
| Participation de 9 % dans KELPÉNIA | Valeur actuelle : **juste valeur** | 610 000 | Instrument de capitaux propres : il n'a pas de flux contractuels, il est à la juste valeur ; le groupe a choisi d'en présenter les variations en autres éléments du résultat global [V IFRS 9 § 4.1.4, 5.7.5 ; F04 R11] |
| Séchoir de GOËMONS DU TRIEUX | Coût historique : **coût du droit d'utilisation**, amorti | 1 390 500 | Ce n'est pas le séchoir qui est inscrit, mais le droit de l'utiliser pendant dix ans, évalué au coût (valeur actualisée des loyers et loyer payé d'avance), puis amorti [V IFRS 16 § 23, 24, 30, 31 ; F04 § 9] ; il a pour contrepartie l'obligation de payer les loyers (1 417 800 €) |

(0,5 pt pour l'emprunt, 0,5 pt pour la participation, 0,25 pt pour le séchoir.)

**Pertinence (0,75 pt).** Le cadre fait dépendre le choix de la base des caractéristiques de l'élément et de la manière dont il contribuera aux flux de trésorerie futurs, l'objectif étant une information **pertinente**, qui représente fidèlement la situation, au regard du coût de son obtention [S cadre de 2018 ; F03 § 7.2, § 13]. Le séchoir et l'emprunt produisent ou absorbent des flux **contractuels ou d'exploitation** connus : le coût (amorti) répartit sur les bons exercices le coût de l'usage et le coût réel de la dette, frais et prime compris, ce qui éclaire la performance de chaque exercice. Pour la participation, dont la valeur ne dépend que des perspectives de KELPÉNIA, le prix payé en 2023 ne dit plus rien de ce que vaut aujourd'hui l'investissement : la juste valeur est la seule mesure utile, et la présentation de ses variations hors du résultat net évite de mêler à la performance opérationnelle un placement que le groupe ne compte pas vendre. Employer plusieurs bases dans un même état est donc voulu ; IAS 1 en tient compte en présentant séparément les catégories évaluées selon des bases différentes [V IAS 1 § 59 ; F03 § 13], et les notes indiquent la base retenue pour chaque catégorie d'instruments financiers [V IFRS 7 § 21 ; F03 § 13].

**Réponses tolérées**
- Bases présentées en trois catégories (coût historique, juste valeur, valeur d'utilité ou d'exécution), si le coût amorti est rattaché au coût historique.
- Séchoir rattaché au « coût » sans le mot « droit d'utilisation », si la réponse dit que le groupe inscrit une ressource dont il contrôle l'usage (0,25 pt conservé).

**Erreurs fréquentes**
- Emprunt dit « à la juste valeur » ; participation dite « au coût amorti » ou « réévaluée par prudence » ; dépréciation invoquée pour la participation.
- Réponse limitée à la définition d'un actif et d'un passif, sans bases d'évaluation (`JUR-F07`) ; réponse « parce que la norme l'impose », sans lien avec la pertinence (`JUR-F02`).

**Références normatives (1.1)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 233-16, L. 233-24 ; règlement (CE) n° 1606/2002, art. 4 | Obligation de consolider ; IFRS obligatoires sur un marché réglementé, sur option sinon | [V] | F03 § 1.1, § 1.2 |
| IFRS 10 § 19 ; IAS 8 § 14 | Méthodes uniformes ; permanence | [V] | F04 § 1 ; F03 § 12 |
| Cadre conceptuel de 2018 | Bases d'évaluation et critères de choix | [S] | F03 § 7.2, § 13 |
| IFRS 9, appendice A, § 4.1.4, 4.2.1, 5.7.5 ; IAS 16 § 6 | Coût amorti, TIE ; juste valeur ; option OCI | [V] | F03 § 13 ; F04 R11 |
| IFRS 16 § 23, 24, 30, 31 | Droit d'utilisation au coût, amorti | [V] | F04 § 9 |
| IAS 1 § 59 ; IFRS 7 § 21 | Bases différentes, postes distincts ; information sur les bases | [V] | F03 § 13 |

---

### 1.2 Périmètre et méthodes (3,5 pts)

#### a. Tableau du périmètre (2,5 pts)

| Société | % de contrôle (droits actuels) | Nature du contrôle | Méthode | % d'intérêt du groupe | % des PNC |
|---|---:|---|---|---:|---:|
| GOËMONS DU TRIEUX | 100 % | Contrôle exclusif | Intégration globale | 100 % | 0 % |
| ARGUÉNOR Extraits | 70 % | Contrôle exclusif | Intégration globale | 70 % | 30 % |
| PHYCOLIS Biotech | 40 % | Contrôle exclusif (droits de vote potentiels substantiels) | Intégration globale | 40 % | 60 % |
| KELPÉNIA Recherche | 9 % | Aucun (ni contrôle ni influence notable) | Non consolidée : actif financier (question 1.4 d) | — | — |

(1 pt : 0,25 pt par ligne.) GOËMONS et ARGUÉNOR : majorité des droits de vote et nomination du président, sans pacte contraire [V IFRS 10 § 7 ; F03 § 2]. KELPÉNIA : moins de 20 % des droits de vote, ni représentation ni opérations, l'influence notable n'est pas présumée [V IAS 28 § 5, 6 ; F03 § 2].

**PHYCOLIS : nature du contrôle (1 pt).** Avec 40 % des droits de vote, KERVALGUE n'a pas la majorité ; mais l'investisseur tient compte de ses **droits de vote potentiels** s'ils sont **substantiels** [V IFRS 10 B47 ; F03 § 7.1], c'est-à-dire si son détenteur a la capacité pratique de les exercer [V B22] :
- aucun obstacle : conversion à tout moment, au seul choix de KERVALGUE, organisée par les statuts ; le prix de conversion (20 €) est **inférieur** à la valeur de l'action (34 €) et ne crée aucune barrière financière [V B23 a) ii) et iv), B24] ;
- KERVALGUE **profiterait** de la conversion : l'instrument est dans le cours et des synergies sont attendues (programme commun, coproduits destinés à PHYCOLIS) [V B23 c)] ;
- combinés à ses droits actuels, ces droits lui donneraient **62 %** des voix face à des associés dispersés (aucun fondateur au-delà de 12 %, fonds à 26 %) : ils lui confèrent le pouvoir de diriger les activités pertinentes [V B49, B50 ; F03 § 7.1].

KERVALGUE contrôle donc PHYCOLIS, intégrée globalement depuis sa constitution en 2024.

**PHYCOLIS : pourcentage d'intérêt (0,5 pt).** Les quotes-parts du résultat et des capitaux propres de la mère et des PNC sont déterminées sur la seule base des **participations actuelles**, sans refléter la conversion possible [V IFRS 10 B89 ; F03 § 7.1] : **40 %** pour le groupe, **60 %** pour les PNC. Les obligations ne donnent pas aujourd'hui accès aux rendements des actions (intérêt fixe, pas de dividende) : l'exception de B90 ne joue pas.

**Réponses tolérées** : contrôle de PHYCOLIS noté « 40 % (62 % après conversion) » ; KELPÉNIA mentionnée seulement comme « hors périmètre » ; % de contrôle indiqué en « droits potentiels compris : 62 % », si l'intérêt est fixé à 40 %.

**Erreurs fréquentes** : PHYCOLIS mise en équivalence au motif que 40 % donnent une influence notable (droits potentiels ignorés, `JUR-F07`) ; intérêt de 62 % ; PNC de 38 % ; KELPÉNIA mise en équivalence.

#### b. Ce que montre l'intégration globale de PHYCOLIS (1 pt)

**Lecture des comptes (0,5 pt).** Les actifs, les dettes envers les tiers, les produits et les charges de PHYCOLIS sont repris **à 100 %** dans les états consolidés, comme si elle était une filiale majoritaire : le chiffre d'affaires et la marge des biostimulants entrent en totalité dans ceux du groupe. Mais le groupe n'a droit qu'à 40 % de son résultat et de son actif net : le résultat net de PHYCOLIS (640 000 €) se partage en 256 000 € pour les propriétaires de KERVALGUE et 384 000 € pour les PNC, qui détiennent 60 % de ses capitaux propres (1 680 000 € au 31/12/2026, question 1.7) [V IFRS 10 § 22, B94 ; F03 § 3]. Le lecteur doit donc lire le résultat attribuable à la mère, et non le résultat de l'ensemble, pour apprécier ce qui revient aux actionnaires de KERVALGUE.

**Obligations convertibles (0,5 pt).** Créance de KERVALGUE et dette de PHYCOLIS sont **réciproques** : elles sont éliminées, ainsi que leurs intérêts et intérêts courus (question 1.5 c) [V IFRS 10 B86 c) ; F04 R14] ; l'endettement consolidé ne comprend pas ces 2 200 000 €. Leur seul effet est de fonder le contrôle.

**Références normatives (1.2)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 7, 22, B22 à B24, B47, B49, B50, B89, B90, B94 | Contrôle ; droits substantiels ; droits de vote potentiels ; intérêt sur les participations actuelles ; PNC | [V] | F03 § 2, § 3, § 7.1 |
| IAS 28 § 5, 6 | Présomption d'influence notable | [V] | F03 § 2 |
| IFRS 10 B86 c) | Élimination des opérations intragroupe | [V] | F04 R14 |

---

### 1.3 Location du séchoir de GOËMONS DU TRIEUX (6 pts)

#### a. Traitements et mesure initiale (1,5 pt)

**Comptes individuels (0,25 pt).** Le PCG enregistre le loyer en charges à son échéance (compte 6132, 185 000 € en 2026) ; ni le séchoir ni l'engagement de loyers n'apparaissent au bilan [S ; F03 § 9].

**IFRS 16 (0,5 pt).** Le contrat confère le droit de contrôler l'utilisation d'un actif identifié pendant dix ans moyennant contrepartie : c'est un contrat de location [V IFRS 16 § 9]. Ni courte durée (dix ans) ni faible valeur (séchoir de 3 400 000 €) : aucune exemption [V § 5, 6]. À la prise d'effet, le preneur comptabilise un **droit d'utilisation** et une **obligation locative** [V § 22].

**Mesure au 01/01/2026 (0,75 pt).**
- Obligation locative = valeur actualisée des loyers **non encore versés**, au taux d'emprunt marginal, le taux implicite ne pouvant être déterminé facilement [V § 26] : les neuf loyers de 2027 à 2035, soit **1 360 000 €** (annexe 1.4).
- Droit d'utilisation = obligation initiale + loyers versés à la prise d'effet ou avant [V § 23, 24] : 1 360 000 + 185 000 = **1 545 000 €**. Il est amorti linéairement sur dix ans, durée du contrat inférieure à la durée d'utilité du séchoir et sans option d'achat [V § 31, 32 ; annexe 1.2, point 1].

#### b. Calculs de 2026 et tableau d'incidence (2,5 pts)

**Calculs (1 pt)**
- Amortissement : 1 545 000 / 10 = **154 500 €** ; valeur nette au 31/12/2026 : **1 390 500 €**.
- Intérêts : 1 360 000 × 4,25 % = **57 800 €** [V § 36, 37].
- Obligation locative au 31/12/2026 : 1 360 000 + 57 800 = **1 417 800 €** : le loyer de 2027 n'est payé que le 01/01/2027.
- **Part courante : 185 000 €** (loyer du 01/01/2027, réglé dans les douze mois) ; part non courante : **1 232 800 €** [V IAS 1 § 69 ; F14 § 2.2].

**Tableau d'incidence au 31/12/2026 (1,5 pt)**

| | Comptes individuels | Comptes consolidés | Incidence |
|---|---:|---:|---:|
| Droit d'utilisation, valeur nette | — | 1 390 500 | + 1 390 500 |
| Obligation locative | — | 1 417 800 | – 1 417 800 |
| Charges de 2026 : loyer / amortissement + intérêts | 185 000 | 154 500 + 57 800 = 212 300 | – 27 300 |
| Impôt différé passif (droit d'utilisation, base fiscale nulle) : 1 390 500 × 25 % | | 347 625 | – 347 625 |
| Impôt différé actif (obligation, base fiscale nulle) : 1 417 800 × 25 % | | 354 450 | + 354 450 |
| **Incidence nette sur le résultat de 2026** (– 27 300 + 6 825) | | | **– 20 475** |

(0,5 pt pour la charge et l'écart ; 0,5 pt pour les impôts différés ; 0,5 pt pour l'incidence nette.) Le contrat crée une différence imposable (droit d'utilisation) et une différence déductible (obligation) ; l'exemption de la comptabilisation initiale ne s'applique pas : les deux impôts différés sont comptabilisés [V IAS 12 § 22A ; F04 § 9]. Leur solde (actif net de 6 825 €) égale 25 % de l'écart de résultat. Contrôle : 1 390 500 – 1 417 800 = – 27 300 €, aucun retraitement n'affectant les réserves (contrat de 2026).

#### c. Écritures (2 pts)

**C1 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| DU Droit d'utilisation du séchoir (1 360 000 + 185 000) | 1 545 000 | |
| IDA Impôt différé actif (1 417 800 × 25 %) | 354 450 | |
| RST.GOEMONS Résultat GOËMONS DU TRIEUX (27 300 net d'impôt) | 20 475 | |
| AMO_DU Amortissements du droit d'utilisation | | 154 500 |
| DL Obligation locative | | 1 417 800 |
| IDP Impôt différé passif (1 390 500 × 25 %) | | 347 625 |
| **Total** | **1 919 925** | **1 919 925** |
| | *Libellé : séchoir pris en location : droit d'utilisation et obligation locative (IFRS 16)* | | |

**C1R (compte de résultat, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles | 154 500 | |
| 6618 Intérêts des autres dettes (obligation locative) | 57 800 | |
| 6132 Locations immobilières (loyer annulé) | | 185 000 |
| CH_ID Produit d'impôt différé | | 6 825 |
| RES_CR Résultat | | 20 475 |
| **Total** | **212 300** | **212 300** |

Les intérêts sont présentés en charges financières, séparément de l'amortissement [V IFRS 16 § 49 ; annexe 1.2, point 1].

**Réponses tolérées (1.3)**
- Écriture à l'ouverture (01/01/2026) puis écritures de 2026 séparées, si elles aboutissent aux mêmes soldes ; paiement du 01/01/2026 présenté comme « réduction de l'obligation » (obligation initiale de 1 545 000 € aussitôt diminuée de 185 000 €).
- Intérêts au compte 661 ou 6611 ; impôts différés compensés (IDA net de 6 825 €) s'il est indiqué que la norme permet la compensation pour une même entité fiscale : 0,25 pt perdu au tableau, les écritures cohérentes étant acceptées.

**Erreurs fréquentes**
- Obligation calculée sur dix loyers ou droit d'utilisation sans le loyer payé d'avance ; intérêts calculés sur 1 545 000 € ; obligation du 31/12/2026 diminuée du loyer de 2027 non encore payé.
- Loyer laissé en charges en plus de l'amortissement et des intérêts (double charge) ; part courante calculée comme la « part en capital » d'un loyer à terme échu ; impôt différé omis (`JUR-G06`).

**Références normatives (1.3)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 16 § 5, 6, 9, 22 à 24, 26, 31, 32, 36, 37, 47, 49 | Contrat de location ; exemptions ; mesure initiale ; amortissement ; intérêts ; présentation | [V] | F04 R2, § 9 |
| IAS 12 § 22A | Impôts différés d'un contrat de location | [V] | F04 § 9 |
| IAS 1 § 69 | Passif courant | [V] | F14 § 2.2 |

---

### 1.4 Instruments financiers (7 pts)

#### a. Évaluation de l'emprunt et taux d'intérêt effectif (1,5 pt)

**Évaluation (0,5 pt).** L'emprunt est un passif financier évalué ultérieurement au **coût amorti** [V IFRS 9 § 4.2.1 ; annexe 1.2, point 2]. À l'origine, il est comptabilisé à sa juste valeur **diminuée des coûts de transaction** directement attribuables à l'émission [V § 5.1.1 ; F04 R11] : 7 000 000 – 74 060 = **6 925 940 €**.

**Principe du taux d'intérêt effectif (0,5 pt).** C'est le taux qui actualise exactement les décaissements futurs (cinq coupons de 210 000 € et le remboursement de 7 175 000 €) de manière à obtenir le montant initial net de 6 925 940 € ; il inclut les frais, la prime et toutes les surcotes ou décotes [V IFRS 9, appendice A ; F03 § 13]. Supérieur au taux nominal de 3 %, il mesure le **coût réel** de la ressource : coupon, prime de remboursement et frais sont répartis sur cinq ans de façon actuarielle, à taux constant sur le capital restant dû, et non de façon linéaire.

**Ligne 2026 du tableau (0,5 pt)**

| Exercice | Coût amorti au 1er janvier | Intérêts au taux effectif (3,70 %) | Coupon payé | Coût amorti au 31 décembre |
|---|---:|---:|---:|---:|
| 2026 | 6 925 940 | **256 260** | 210 000 | **6 972 200** |

6 925 940 × 3,70 % = 256 259,78, arrondi à 256 260 €. Contrôle : la charge totale au taux effectif sur cinq ans, 1 299 060 €, égale 5 × 210 000 + 175 000 + 74 060.

#### b. Comparaison PCG / IFRS et impôt différé (1,5 pt)

| Au 31/12/2026 | Comptes individuels | Comptes consolidés | Écart |
|---|---:|---:|---:|
| Emprunt (163) | 7 175 000 | 6 972 200 | – 202 800 |
| Prime de remboursement non répartie (169) : 175 000 – 35 000 | – 140 000 | — | + 140 000 |
| Frais d'émission non répartis (481) : 74 060 – 14 812 | – 59 248 | — | + 59 248 |
| **Dette nette** | **6 975 752** | **6 972 200** | **– 3 552** |
| Charges financières de 2026 : 210 000 + 35 000 + 14 812 / intérêts au TIE | 259 812 | 256 260 | – 3 552 |

(1 pt.) La base fiscale de l'emprunt est sa valeur nette dans les comptes individuels (6 975 752 €), supérieure à sa valeur consolidée : pour un passif, c'est une **différence temporelle imposable**, **impôt différé passif** de 3 552 × 25 % = **888 €** [V IAS 12 § 15 ; F04 R11 ; annexe 1.5] (0,25 pt). **Incidence nette** : résultat consolidé de 2026 augmenté de 3 552 – 888 = **2 664 €** ; la répartition actuarielle allège la charge des premiers exercices et alourdit celle des derniers (0,25 pt).

#### c. Écritures (2 pts)

**C2 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 163 Autres emprunts obligataires (7 175 000 – 6 972 200) | 202 800 | |
| 169 Primes de remboursement des emprunts | | 140 000 |
| 481 Frais d'émission des emprunts | | 59 248 |
| IDP Impôt différé passif | | 888 |
| RST.KERVALGUE Résultat KERVALGUE (3 552 net d'impôt) | | 2 664 |
| **Total** | **202 800** | **202 800** |
| | *Libellé : emprunt obligataire au coût amorti (IFRS 9)* | | |

**C2R (compte de résultat, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6611 Intérêts des emprunts et dettes (256 260 – 210 000) | 46 260 | |
| CH_ID Charge d'impôt différé | 888 | |
| RES_CR Résultat | 2 664 | |
| 6861 Dotations aux amortissements des primes de remboursement des emprunts | | 35 000 |
| 6862 Dotations aux amortissements des frais d'émission des emprunts | | 14 812 |
| **Total** | **49 812** | **49 812** |

#### d. Trois actifs financiers (2 pts)

L'entité classe ses actifs financiers selon son **modèle économique** de gestion et les **caractéristiques des flux contractuels** [V IFRS 9 § 4.1.1 ; F04 § 9].

| Actif | Catégorie | Montant au 31/12/2026 | Variations de valeur |
|---|---|---:|---|
| Participation de 9 % dans KELPÉNIA | Juste valeur par les autres éléments du résultat global, **sur option** | 610 000 | Variation de 2026 (+ 90 000 €, cumul + 160 000 € par rapport au coût) en autres éléments du résultat global, **jamais reclassée en résultat**, même à la cession ; dividendes éventuels en résultat ; pas de dépréciation |
| Parts du fonds monétaire | **Juste valeur par le résultat** | 1 812 600 | Plus-value latente de 12 600 € en résultat de 2026 |
| Prêt au fabricant de bateaux | **Coût amorti** | 496 320 | Intérêts au taux effectif en résultat ; la juste valeur (481 000 €) n'est pas retenue ; correction de valeur pour pertes attendues (négligeable ici) |

**Justifications (0,5 pt par actif, 0,5 pt pour le principe).**
- **KELPÉNIA** : une action ne donne droit ni à un remboursement de principal ni à des intérêts : elle relève de la juste valeur [application des § 4.1.2 b) et 4.1.4, S ; F04 § 9]. Détenue durablement et non à des fins de transaction, elle ouvre l'option irrévocable, exercée à la comptabilisation initiale, de présenter ses variations en autres éléments du résultat global [V § 4.1.4, 5.7.5, B5.7.1 ; F04 R11 ; annexe 1.2, point 2]. Aucune dépréciation : le modèle des pertes attendues ne vise pas ces titres [V § 5.5.1].
- **Fonds monétaire** : les flux d'une part de fonds dépendent de la valeur des titres détenus par le fonds ; ce ne sont pas uniquement des remboursements de principal et des intérêts sur le principal restant dû : ni coût amorti, ni juste valeur par les autres éléments du résultat global [V § 4.1.2, 4.1.2A ; application, S] ; elles relèvent de la juste valeur par le résultat, catégorie résiduelle [V § 4.1.4, 5.7.1], le groupe n'ayant désigné aucun autre actif sur option.
- **Prêt** : détenu pour en percevoir les flux contractuels jusqu'au remboursement ; flux composés uniquement de remboursements de principal et d'intérêts : **coût amorti** [V § 4.1.2], frais de dossier compris dans le taux effectif [V § 5.4.1 ; IFRS 9 B5.4.2 a)] ; il entre dans le modèle des pertes de crédit attendues, ici sur douze mois et négligeables [V § 5.5.1, 5.5.5 ; F04 § 9].

**Réponses tolérées (1.4)**
- En a, explication du taux effectif comme « taux de revient actuariel » ou « taux qui égalise le montant net reçu et la valeur actuelle des flux à payer ».
- En b et c, écriture unique présentant les comptes 169 et 481 annulés et la dette ramenée au coût amorti, avec les mêmes montants ; prime et frais regroupés dans une ligne « charges à répartir ».
- En d, fonds monétaire présenté comme « équivalent de trésorerie à la juste valeur par le résultat » ; KELPÉNIA justifiée par la seule option du manuel, si l'absence de flux contractuels est dite.

**Erreurs fréquentes**
- Emprunt maintenu au nominal (7 000 000 €) ou au montant de remboursement ; frais d'émission laissés à l'actif ; prime « annulée » sans être reprise dans le coût amorti (`JUR-G05`).
- Impôt différé actif au lieu de passif (sens de l'écart sur un passif) ; charge au taux effectif calculée sur 7 000 000 €.
- Prêt évalué à sa juste valeur ; participation à la juste valeur par le résultat malgré l'option ; recyclage annoncé de la plus-value de KELPÉNIA à la cession (`JUR-G08`).

**Références normatives (1.4)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 9 § 4.1.1, 4.1.2, 4.1.2A, 4.1.4, 4.2.1, 5.1.1, 5.4.1, 5.5.1, 5.5.5, 5.7.1, 5.7.5, B5.4.2, B5.7.1, appendice A | Classement ; coût amorti ; TIE ; juste valeur ; option OCI ; pertes attendues | [V] | F04 R11, § 9 ; F03 § 13 |
| IAS 12 § 15 | Différence imposable sur un passif | [V] | F04 R11 |
| Hypothèse fiscale de l'annexe 1.5 | Base fiscale = valeur nette individuelle | — | F04 R11 |

---

### 1.5 Opérations internes (5 pts)

#### a. Comptes réciproques (1,75 pt)

**Rapprochement (0,5 pt).** Créance de GOËMONS sur KERVALGUE : 512 000 € ; dette de KERVALGUE : 416 000 € ; écart **96 000 €** : le lot facturé et expédié le 30/12/2026, retenu par la tempête, n'a été enregistré par KERVALGUE qu'à sa réception, le 04/01/2027. Pour le groupe, la vente est réalisée avant la clôture : selon le manuel, le lot figure dans les stocks de KERVALGUE (annexe 1.2, point 4). Les soldes avec ARGUÉNOR (286 000 €) concordent.

**Mise en concordance (0,5 pt).** **C3** : débit 31 Matières premières et fournitures (KERVALGUE) 96 000 ; crédit 401 Fournisseurs 96 000. **C3R** : débit 601 Achats stockés – Matières premières et fournitures 96 000 ; crédit 6031 Variation des stocks de matières premières et fournitures 96 000 (sans effet sur le résultat). *Libellé : lot en transit inscrit chez KERVALGUE.* Vendu sans marge, le lot n'appelle aucune élimination de résultat.

**Élimination (0,75 pt).** **C4** : débit 401 Fournisseurs 512 000 (KERVALGUE) et 286 000 (ARGUÉNOR) ; crédit 411 Clients 798 000. **C4R** : débit 701 Ventes de produits finis 6 440 000 (3 840 000 + 2 600 000) ; crédit 601 Achats stockés 6 440 000 (KERVALGUE 3 744 000 + 96 000 ; ARGUÉNOR 2 600 000). *Libellé : élimination des soldes et des ventes de GOËMONS DU TRIEUX.* Ces éliminations sont sans incidence sur le résultat [V IFRS 10 B86 c) ; F04 R14].

#### b. Marge interne (1,75 pt)

**Calcul (0,75 pt)** : 420 000 × 20 % = **84 000 €** ; impôt différé actif : 84 000 × 25 % = **21 000 €** ; élimination nette : **63 000 €**. Le stock est ramené au coût du groupe (336 000 €), inférieur à sa base fiscale chez ARGUÉNOR (420 000 €) : différence déductible [V IFRS 10 B86 c) ; IAS 12 § 24 ; F04 R14].

**Répartition (0,5 pt).** Le résultat interne est imputé à la société qui l'a réalisé, GOËMONS DU TRIEUX, la vendeuse (annexe 1.2, point 4 ; principe identique en ANC, art. 251-2) ; détenue à 100 %, elle supporte l'élimination **en totalité pour le groupe**. Les 30 % de PNC d'ARGUÉNOR n'en supportent rien, bien que le stock soit chez ARGUÉNOR : son résultat n'est pas modifié. Aucune marge n'est à éliminer à l'ouverture : ARGUÉNOR ne détenait aucun stock acheté au groupe avant son entrée dans le périmètre.

**Écritures (0,5 pt).** **C5** : débit RST.GOEMONS 63 000 ; débit IDA 21 000 ; crédit 31 Matières premières et fournitures (ARGUÉNOR) 84 000. **C5R** : débit 6031 Variation des stocks de matières premières et fournitures 84 000 ; crédit CH_ID Produit d'impôt différé 21 000 ; crédit RES_CR 63 000. *Libellé : élimination de la marge de GOËMONS DU TRIEUX sur les stocks d'ARGUÉNOR.*

#### c. Obligations convertibles et dividende (1,5 pt)

**Obligations (0,75 pt).** **C6** : débit 161 Emprunts obligataires convertibles 2 200 000 ; débit 1618 Intérêts courus sur emprunts obligataires convertibles 44 000 ; crédit 2721 Obligations 2 200 000 ; crédit 2768 Intérêts courus 44 000. **C6R** : débit 7621 Revenus des titres immobilisés 88 000 ; crédit 6611 Intérêts des emprunts et dettes 88 000. *Libellé : élimination des obligations convertibles de PHYCOLIS détenues par KERVALGUE.* Créance, dette, produit et charge internes au groupe sont éliminés en totalité, sans incidence sur le résultat [V IFRS 10 B86 c) ; F04 R14] : le résultat de PHYCOLIS, partagé à 40 / 60, reste diminué des intérêts versés à KERVALGUE, et celui de KERVALGUE en reste augmenté.

**Dividende (0,75 pt).** **C7** : débit RST.KERVALGUE 600 000 ; crédit RSV.KERVALGUE 600 000. **C7R** : débit 7611 Revenus des titres de participation 600 000 ; crédit RES_CR 600 000. *Libellé : élimination du dividende reçu de GOËMONS DU TRIEUX.* Le dividende est un transfert interne de résultats déjà compris dans les réserves consolidées ; le laisser en produits le compterait deux fois [V IFRS 10 B86 c) ; F04 R14]. GOËMONS étant détenue à 100 %, aucune part ne sort du groupe.

**Réponses tolérées (1.5)**
- C3 et C4 regroupées (débit 31 96 000 et 401 702 000 ; crédit 411 798 000) ; ventes à KERVALGUE éliminées pour 3 744 000 € si le lot est porté directement en stock sans passer par les achats.
- Marge calculée comme si le taux de 20 % portait sur le coût (420 000 × 20 / 120 = 70 000 €) : 0,25 pt perdu en b, les écritures cohérentes étant acceptées (`JUR-F08`).

**Erreurs fréquentes**
- Écart de 96 000 € « éliminé » en annulant une partie de la vente de GOËMONS ; marge calculée sur le lot en transit vendu sans marge.
- Marge répartie 70 / 30 « parce que le stock est chez ARGUÉNOR » ; impôt différé omis (`JUR-G06`).
- Obligations convertibles laissées en dettes consolidées ; intérêts courus oubliés ; dividende porté en diminution des capitaux propres consolidés.

**Références normatives (1.5)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 B86 c) | Élimination complète des actifs, passifs, produits, charges et flux intragroupe | [V] | F04 R14 |
| ANC 2020-01 art. 251-2 | Résultat interne imputé à la société qui l'a réalisé (principe repris par le manuel) | [V] | F04 R14 |
| IAS 12 § 24 | Impôt différé actif | [V] | F04 § 1 |

---

### 1.6 Acquisition d'ARGUÉNOR (5 pts)

#### a. Frais d'acquisition (1 pt)

**Traitement (0,5 pt).** Les frais connexes (avocats, banque d'affaires, audit d'acquisition) sont des **charges** de la période où ils sont engagés ; ils n'entrent pas dans la contrepartie transférée [V IFRS 3 § 53 ; F05 § 2 ; annexe 1.2, point 3]. Ce sont des charges de 2026 ; titres ramenés à 7 280 000 €. Selon le règlement ANC, ils auraient été inclus dans le coût d'acquisition, nets d'impôt [V art. 231-2 ; F05 § 1.1].

**C8 (0,25 pt)** : débit RST.KERVALGUE 196 000 ; crédit 261.KERVALGUE Titres de participation ARGUÉNOR 196 000. **C8R (0,25 pt)** : débit 6226 Honoraires 196 000 ; crédit RES_CR 196 000. Aucun impôt différé (hypothèse de l'annexe 1.7).

#### b. Actif net identifiable et goodwill (2,5 pts)

**Actif net identifiable à la juste valeur au 01/01/2026 (1 pt)**

| Élément | Montant |
|---|---:|
| Capitaux propres d'ARGUÉNOR au 01/01/2026 | 6 900 000 |
| Marque « Gélarmor » : 1 600 000 – 0 | + 1 600 000 |
| Bâtiment : 2 600 000 – 1 800 000 | + 800 000 |
| Impôt différé passif : 2 400 000 × 25 % | – 600 000 |
| **Actif net identifiable à la juste valeur** | **8 700 000** |

Les actifs identifiables sont évalués à leur juste valeur à la date d'acquisition [V IFRS 3 § 18 ; F05 § 11] ; la marque déposée, non inscrite chez ARGUÉNOR, résulte d'un droit légal : elle est identifiable et comptabilisée séparément du goodwill [V IAS 38 § 12 ; IFRS 3 B31 ; F03 § 11]. Les impôts différés des écarts affectent le goodwill [V IFRS 3 § 24 ; IAS 12 § 66 ; F05 § 2].

**Goodwill partiel et PNC (1 pt)**

| Élément | Montant |
|---|---:|
| Contrepartie transférée : 56 000 × 130 € | 7 280 000 |
| PNC : 30 % × 8 700 000 | 2 610 000 |
| – Actif net identifiable | – 8 700 000 |
| **Goodwill** | **1 190 000** |

Formulation équivalente : 7 280 000 – 70 % × 8 700 000 = 1 190 000 € [V IFRS 3 § 19, 32 ; F05 § 2.1]. Les PNC sont évaluées à leur quote-part de l'actif net identifiable selon le manuel : **2 610 000 €**. Le goodwill n'est pas amorti ; en l'absence d'indice de perte de valeur, il reste à 1 190 000 € au 31/12/2026 [V F05 § 2 ; annexe 1.2, point 3].

**Goodwill complet (0,5 pt).** Avec des PNC à leur juste valeur (2 960 000 €), le goodwill aurait été de 7 280 000 + 2 960 000 – 8 700 000 = **1 540 000 €**, dont 350 000 € attribuables aux PNC, et les PNC à l'entrée de 2 960 000 € au lieu de 2 610 000 € [V IFRS 3 § 19 ; F05 § 2.1].

#### c. Écarts d'évaluation (1,5 pt)

**C9 (bilan, écarts au 01/01/2026, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Concessions et droits similaires, brevets, licences, marques (Gélarmor) | 1 600 000 | |
| 2131 Bâtiments | 800 000 | |
| IDP Impôt différé passif | | 600 000 |
| RSV.ARGUENOR Réserves ARGUÉNOR – écarts d'évaluation nets | | 1 800 000 |
| **Total** | **2 400 000** | **2 400 000** |

**C10 (bilan, 2026, 0,25 pt)** : débit RST.ARGUENOR 30 000 ; débit IDP 10 000 ; crédit 28131 Amortissements des bâtiments 40 000 (800 000 / 20). **C10R (0,25 pt)** : débit 6811 Dotations aux amortissements 40 000 ; crédit CH_ID 10 000 ; crédit RES_CR 30 000.

**Résultat retraité d'ARGUÉNOR (0,25 pt)** : 1 340 000 – 30 000 = **1 310 000 €**. La marque, à durée d'utilité indéterminée, n'est pas amortie [V IAS 38 § 88, 107 ; F05 § 11] ; son impôt différé passif (400 000 €) demeure.

**Réponses tolérées (1.6)**
- Retraitement des frais regroupé avec l'élimination des titres ; C9 et C10 regroupées en une écriture nette au 31/12/2026 si réserves et résultat sont distingués.
- Goodwill complet présenté sous forme de tableau.

**Erreurs fréquentes**
- Frais inclus dans le coût selon le raisonnement de l'ANC (goodwill de 1 386 000 €) (`JUR-G02`, erreur symétrique) ; écarts d'évaluation retenus avant impôt (goodwill de 770 000 €) (`JUR-G06`).
- Goodwill calculé sur 100 % de l'actif net ; PNC évaluées à 30 % de la contrepartie ; marque amortie ; dotation aux amortissements pratiquée sur le goodwill, qui n'est pas amortissable en IFRS.

**Références normatives (1.6)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 18, 19, 24, 32, 53, B31 | Juste valeur ; PNC ; impôts différés ; goodwill ; frais ; marque | [V] | F05 § 2, § 11 ; F03 § 11 |
| IAS 12 § 66 ; IAS 38 § 12, 88, 107 | Impôts différés du regroupement ; marque identifiable, non amortie | [V] | F05 § 2, § 11 ; F03 § 11 |
| ANC 2020-01 art. 231-2 | Frais dans le coût, nets d'impôt | [V] | F05 § 1.1 |

---

### 1.7 Partage des capitaux propres (5 pts)

#### a. Tableaux de partage (2,5 pts)

**Résultat retraité de GOËMONS DU TRIEUX (0,5 pt)** : 1 180 000 – 20 475 (location, question 1.3) – 63 000 (marge interne, question 1.5) = **1 096 525 €**. Les éliminations sans incidence sur le résultat (ventes, soldes) ne le modifient pas.

**GOËMONS DU TRIEUX (intérêt 100 %) (0,5 pt)**

| Capitaux propres retraités | Total | Groupe (100 %) |
|---|---:|---:|
| Capital et réserves : 1 500 000 + 4 200 000 | 5 700 000 | 5 700 000 |
| – Titres GOËMONS DU TRIEUX | | – 1 500 000 |
| **Réserves consolidées** | | **4 200 000** |
| Résultat retraité | 1 096 525 | **1 096 525** |

**PHYCOLIS (intérêt 40 %) (0,75 pt)**

| Capitaux propres | Total | Groupe (40 %) | PNC (60 %) |
|---|---:|---:|---:|
| Capital | 1 900 000 | 760 000 | 1 140 000 |
| Réserves | 260 000 | 104 000 | 156 000 |
| **Sous-total** | **2 160 000** | **864 000** | **1 296 000** |
| – Titres PHYCOLIS | | – 760 000 | |
| **Réserves consolidées / PNC hors résultat** | | **104 000** | **1 296 000** |
| Résultat de 2026 | 640 000 | **256 000** | **384 000** |

Souscription au pair à la constitution : ni goodwill ni écart d'évaluation. L'élimination des obligations convertibles ne modifie pas les capitaux propres de PHYCOLIS.

**ARGUÉNOR (intérêt 70 %) (0,75 pt)**

| Capitaux propres retraités | Total | Groupe (70 %) | PNC (30 %) |
|---|---:|---:|---:|
| Capital | 2 000 000 | 1 400 000 | 600 000 |
| Réserves | 4 900 000 | 3 430 000 | 1 470 000 |
| Écarts d'évaluation nets | 1 800 000 | 1 260 000 | 540 000 |
| **Sous-total = actif net identifiable au 01/01/2026** | **8 700 000** | **6 090 000** | **2 610 000** |
| – Titres ARGUÉNOR (7 476 000 – 196 000) | | – 7 280 000 | |
| **Goodwill (– 1 190 000) / PNC à l'entrée** | | **– 1 190 000** | **2 610 000** |
| Résultat retraité | 1 310 000 | **917 000** | **393 000** |

ARGUÉNOR, entrée dans le périmètre le 01/01/2026, n'apporte aucune réserve consolidée : le solde négatif de la part du groupe (– 1 190 000 €) est le goodwill, inscrit à l'actif [V IFRS 10 B86 b) ; F05 § 3]. PNC au 31/12/2026 : 2 610 000 + 393 000 = **3 003 000 €** ; PHYCOLIS : 1 296 000 + 384 000 = **1 680 000 €** ; total **4 683 000 €**.

#### b. Écritures (2,5 pts)

**C11 (GOËMONS DU TRIEUX, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.GOEMONS Capital | 1 500 000 | |
| RSV.GOEMONS Réserves | 4 200 000 | |
| RST.GOEMONS Résultat retraité | 1 096 525 | |
| 261.KERVALGUE Titres GOËMONS DU TRIEUX | | 1 500 000 |
| RSV_G Réserves consolidées – part du groupe | | 4 200 000 |
| RST_G Résultat consolidé – part du groupe | | 1 096 525 |
| **Total** | **6 796 525** | **6 796 525** |

**C12 (PHYCOLIS, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.PHYCOLIS Capital | 1 900 000 | |
| RSV.PHYCOLIS Réserves | 260 000 | |
| RST.PHYCOLIS Résultat | 640 000 | |
| 261.KERVALGUE Titres PHYCOLIS | | 760 000 |
| RSV_G Réserves consolidées – part du groupe | | 104 000 |
| RST_G Résultat consolidé – part du groupe | | 256 000 |
| RSV_M PNC – réserves | | 1 296 000 |
| RST_M PNC – résultat | | 384 000 |
| **Total** | **2 800 000** | **2 800 000** |

**C13 (ARGUÉNOR, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.ARGUENOR Capital | 2 000 000 | |
| RSV.ARGUENOR Réserves (4 900 000 + écarts nets 1 800 000) | 6 700 000 | |
| RST.ARGUENOR Résultat retraité | 1 310 000 | |
| EA Goodwill | 1 190 000 | |
| 261.KERVALGUE Titres ARGUÉNOR (après C8) | | 7 280 000 |
| RST_G Résultat consolidé – part du groupe | | 917 000 |
| RSV_M PNC – quote-part de l'actif net identifiable | | 2 610 000 |
| RST_M PNC – résultat | | 393 000 |
| **Total** | **11 200 000** | **11 200 000** |
| | *Libellé : élimination des titres ARGUÉNOR, goodwill et partage* | | |

**Compte de résultat (0,5 pt).** Le partage n'appelle aucune écriture au compte de résultat : celui-ci présente le **résultat net de l'ensemble consolidé**, puis sa répartition entre les propriétaires de la société mère et les PNC (384 000 + 393 000 = 777 000 € pour les PNC au titre de PHYCOLIS et d'ARGUÉNOR) [V IAS 1 § 81B ; F14 § 2.3]. Les PNC sont présentées dans les capitaux propres, séparément [V IFRS 10 § 22].

**Réponses tolérées (1.7)**
- Goodwill présenté hors du tableau de partage ; partage de GOËMONS limité à l'élimination des titres contre les réserves consolidées, si le résultat retraité est attribué au groupe.
- Cohérence avec un résultat erroné aux questions 1.3 à 1.6 : l'erreur n'est pénalisée qu'une fois (`JUR-F08`).

**Erreurs fréquentes**
- Partage de PHYCOLIS à 62 / 38 (`JUR-G04`) ; goodwill d'ARGUÉNOR porté en réserves consolidées ; titres ARGUÉNOR éliminés pour 7 476 000 € (frais oubliés) ; résultat de GOËMONS partagé sans les retraitements.
- Écritures déséquilibrées (`JUR-F04`).

**Références normatives (1.7)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 22, B86 b), B89 | PNC en capitaux propres ; élimination des titres ; intérêt actuel | [V] | F03 § 3, § 7.1 ; F05 § 3 |
| IAS 1 § 81B | Répartition du résultat | [V] | F14 § 2.3 |

---

### 1.8 Processus et documents de synthèse (9 pts)

#### a. Phases du processus (2 pts)

| Phase | Traitements du dossier |
|---|---|
| 1. Retraitements d'homogénéisation (comptes individuels mis aux méthodes du groupe) | Location du séchoir (1.3) ; emprunt obligataire au coût amorti (1.4) ; frais d'acquisition des titres ARGUÉNOR (1.6 a) |
| 2. Éliminations des opérations internes | Lot en transit, soldes et ventes réciproques (1.5 a) ; marge interne (1.5 b) ; obligations convertibles et intérêts, dividende (1.5 c) |
| 3. Regroupement d'entreprises | Écarts d'évaluation d'ARGUÉNOR et leur suivi (1.6 c), goodwill et PNC à l'entrée (1.6 b) |
| 4. Élimination des titres et partage | Partage de GOËMONS, PHYCOLIS et ARGUÉNOR (1.7) |

(1,25 pt : 0,25 pt par groupe correctement classé et 0,25 pt pour l'ordre.) Les comptes sont d'abord rendus conformes aux méthodes du groupe [V IFRS 10 § 19 ; F04 § 1], puis les opérations internes éliminées, avant l'élimination des titres et le partage, qui portent sur des capitaux propres **retraités** [V IFRS 10 B86 ; F03 § 3].

**Concordance avant élimination (0,75 pt).** L'élimination annule des montants égaux et de sens contraires ; si la dette de KERVALGUE (416 000 €) restait inférieure à la créance de GOËMONS (512 000 €), l'élimination laisserait un solde de 96 000 € sans réalité pour le groupe, et les achats et les stocks de KERVALGUE seraient incomplets. La mise en concordance corrige d'abord l'enregistrement en retard (achat et stock du lot en transit) ; les soldes, devenus égaux, s'éliminent ensuite sans écart [V IFRS 10 B86 c) ; F04 R14].

#### b. Extrait de l'état de la situation financière au 31/12/2026 (3 pts)

| Rubrique | Montant |
|---|---:|
| Capitaux propres attribuables aux propriétaires de KERVALGUE | 66 450 000 |
| Participations ne donnant pas le contrôle (1 680 000 + 3 003 000) | 4 683 000 |
| **Total des capitaux propres** | **71 133 000** |
| *Passifs non courants* | |
| Emprunt obligataire (coût amorti) | 6 972 200 |
| Obligations locatives, part non courante | 1 232 800 |
| Emprunt bancaire, part non courante (2 700 000 – 540 000) | 2 160 000 |
| Passifs d'impôt différé | 1 320 000 |
| **Total des passifs non courants** | **11 685 000** |
| *Passifs courants* | |
| Obligations locatives, part courante | 185 000 |
| Emprunt bancaire, part courante | 540 000 |
| Fournisseurs et autres créditeurs | 9 860 000 |
| Passif d'impôt exigible | 410 000 |
| **Total des passifs courants** | **10 995 000** |

(1,5 pt pour les montants, dont 0,5 pt pour les PNC.) **Justification (1,5 pt).**
- Les PNC figurent **dans les capitaux propres**, séparément des capitaux propres attribuables aux propriétaires de la mère [V IAS 1 § 54 q) et r) ; IFRS 10 § 22 ; F14 § 2.2] ; les actions propres du contrat de liquidité sont déduites des capitaux propres [V IAS 32 § 33 ; F14 § 11].
- Un passif est **courant** s'il doit être réglé dans le cycle normal d'exploitation, ou dans les douze mois, ou si l'entité n'a pas le droit d'en différer le règlement d'au moins douze mois [V IAS 1 § 69 ; F14 § 2.2] : fournisseurs (cycle d'exploitation inférieur à douze mois), impôt exigible, fraction de 540 000 € de l'emprunt bancaire due le 30/06/2027, loyer du 01/01/2027.
- L'emprunt obligataire, remboursable en 2030 et dont le coupon de 2026 a été payé, est entièrement non courant ; les montants à moins et à plus de douze mois d'un même passif sont distingués [V IAS 1 § 61].
- Les impôts différés ne sont **jamais** classés en courant [V IAS 1 § 56 ; F14 § 2.2].
- Les droits d'utilisation et les obligations locatives sont présentés sur des lignes distinctes [V IFRS 16 § 47 ; annexe 1.2, point 1].

#### c. Résultat par action (2,5 pts)

**Champ (0,25 pt).** IAS 33 s'applique aux états consolidés d'un groupe dont les actions ordinaires sont négociées sur un marché public ; Euronext Growth, système ouvert au public, en est un même s'il n'est pas réglementé [V IAS 33 § 2 b) ; S pour la qualification d'Euronext Growth ; F14 § 5].

**Dénominateur (0,75 pt)** : nombre moyen pondéré d'actions **en circulation**, les actions nouvelles étant prises en compte à compter de leur émission et les actions propres exclues [V IAS 33 § 19 à 21 ; IAS 32 § 33 ; F14 § 5, § 11] :
- actions émises : 4 800 000 + 400 000 × 3/12 = 4 900 000 ;
- actions propres (moyenne pondérée du relevé) : – 36 000 ;
- **nombre moyen pondéré : 4 864 000**.

**Résultat de base par action (0,5 pt)** : résultat attribuable aux porteurs d'actions ordinaires de la mère / nombre moyen pondéré [V IAS 33 § 10] : 7 248 000 / 4 864 000 = **1,49 €**. Le numérateur est le résultat attribuable aux propriétaires de KERVALGUE, non le résultat de l'ensemble consolidé.

**Absence de dilution (1 pt).** La dilution est une réduction du résultat par action résultant de l'hypothèse de conversion d'instruments convertibles ; des actions potentielles ne sont retenues que si leur conversion réduit le résultat par action, et sont écartées si elle l'augmente (antidilution) [V IAS 33 § 5, 41, 43 ; F14 § 11]. Les obligations de PHYCOLIS sont convertibles en actions de **PHYCOLIS**, non de KERVALGUE : elles entrent dans le résultat dilué par action de PHYCOLIS, puis dans celui du groupe à proportion des instruments de PHYCOLIS que détient le groupe [V IAS 33, appendice A, § A11 a) ; F14 § 11]. Or c'est KERVALGUE qui détient toutes ces obligations : leur conversion supposée ne créerait aucune action KERVALGUE (le dénominateur ne change pas) et porterait de 40 % à 62 % la part du groupe dans le résultat de PHYCOLIS, en contrepartie de la disparition d'intérêts que le groupe se verse à lui-même. Le résultat attribuable aux propriétaires de KERVALGUE augmenterait (de 0,62 × (640 000 + 66 000) – 0,40 × 640 000 – 66 000 = 115 720 €, les intérêts de 88 000 € étant pris nets d'impôt) : la conversion serait antidilutive et n'est pas retenue [S, application des § 41, 43 et A11 a) ; F14 § 11]. KERVALGUE n'ayant émis aucun instrument donnant accès à son capital, le **résultat dilué par action est égal au résultat de base, 1,49 €**, et peut figurer sur la même ligne [V IAS 33 § 66, 67 ; F14 § 5].

#### d. Différences de présentation en règlement ANC (1,5 pt)

- **Capitaux propres (0,75 pt).** Le modèle de bilan de l'ANC présente les « capitaux propres (part du groupe) », puis les **intérêts minoritaires** dans une rubrique distincte, hors des capitaux propres part du groupe [V ANC art. 281-1 ; F14 § 1.2, § 4] ; en IFRS, les PNC sont une composante des capitaux propres (71 133 000 € au total).
- **Classement des passifs (0,75 pt).** Le modèle de l'ANC classe les dettes par nature (emprunts et dettes financières, fournisseurs, autres dettes), sans distinction courant / non courant [V art. 281-1 ; F14 § 1.2, § 4]. Les impôts différés passifs y figurent parmi les autres dettes (« dont »), au lieu d'une ligne distincte non courante.

**Réponses tolérées (1.8)**
- En a, frais d'acquisition rangés dans la phase du regroupement ; obligations convertibles rangées avec le périmètre, si leur élimination est située avant le partage.
- En b, obligation locative présentée sur une ligne unique avec la ventilation courant / non courant en note [V IFRS 16 § 47] ; passifs d'impôt différé intégrés à une ligne « autres passifs non courants ».
- En c, nombre moyen d'actions propres recalculé à partir du seul solde de clôture si l'hypothèse est écrite : 0,25 pt perdu ; en d, différence tirée de la location (en ANC, contrat qui n'est ni un crédit-bail ni assimilé : loyers en charges, ni droit d'utilisation ni obligation locative [V art. 272-2 ; F04 R2]), acceptée à la place de l'une des deux.

**Erreurs fréquentes**
- PNC classées en passifs non courants ; emprunt obligataire scindé en une part courante « des intérêts de 2027 » ; impôt différé classé en courant.
- Résultat par action calculé sur le résultat de l'ensemble ou sur le nombre d'actions de clôture (5 200 000) ; actions propres non déduites ; obligations de PHYCOLIS ajoutées au dénominateur (« 110 000 actions potentielles ») (`JUR-F07`).
- Présentation selon IFRS 18 pour 2026 (`JUR-G01`).

**Références normatives (1.8)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 19, 22, B86 | Méthodes uniformes ; PNC ; procédures de consolidation | [V] | F04 § 1 ; F03 § 3 |
| IAS 1 § 54, 56, 61, 69 ; IFRS 16 § 47 | Postes ; impôts différés non courants ; passifs courants ; lignes locatives | [V] | F14 § 2.2 |
| IAS 32 § 33 | Actions propres déduites des capitaux propres | [V] | F14 § 11 |
| IAS 33 § 2, 5, 10, 19 à 21, 41, 43, 66, 67, A11 | Champ ; dilution et antidilution ; résultat de base ; nombre moyen pondéré ; instruments d'une filiale | [V] ; Euronext Growth « marché public » [S] ; antidilution des obligations détenues par la mère [S] | F14 § 5, § 11 |
| ANC 2020-01 art. 272-2, 281-1 | Locations en ANC ; modèle de bilan consolidé | [V] | F04 R2 ; F14 § 1.2, § 4 |
| Règlement (UE) 2026/338 ; IFRS 18 § C1 | IFRS 18 applicable à compter de 2027 | [V] | F14 § 0 |

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, distinction avec un achat d'actions, référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2 |
| 2.1 Régime de faveur : conditions, effets, engagements | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 2 |
| 2.2 Contrôle, sens et mode d'évaluation des apports | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 1,5 |
| 2.3 a) Parité exacte | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1 |
| 2.3 b) Projet des familles : soulte et contrainte légale | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 1,5 |
| 2.3 c) Pistes d'adaptation et conseil | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 3 |
| 2.3 d) Piste retenue : capital, prime, répartition du capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 2 |
| 2.4 Valeur réelle et composition des apports | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 3 |
| 2.5 a) Écritures de base chez PROVENDES DU LIÉ | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 3 |
| 2.5 b) Créances et dettes réciproques, frais de fusion | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 2 |
| 2.5 c) Écritures chez MOUTURES DE L'OUST | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 2 |
| 2.6 Note à Mme LE GOFF-RIOU | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Qualification, référentiel et régime fiscal (4 pts)

**Qualification et référentiel (2 pts)**
- *Qualification et modalités (1 pt).* L'opération est une **fusion par absorption** : MOUTURES DE L'OUST transmet l'**ensemble de son patrimoine**, actif et passif, à une société qui existe déjà, PROVENDES DU LIÉ, par suite de sa **dissolution sans liquidation** ; c'est une transmission universelle, qui comprend aussi les éléments absents de son bilan (clientèle d'éleveurs, marque, engagements de retraite envers son personnel) [V C. com. L. 236-1, PCG art. 710-2, F01 § 1]. En contrepartie, PROVENDES DU LIÉ **augmente son capital** et attribue des actions nouvelles **directement aux associés** de MOUTURES DE L'OUST, avec éventuellement une **soulte en espèces** qui ne peut dépasser 10 % de la valeur nominale des actions attribuées [V C. com. L. 236-1, F01 § 4]. MOUTURES DE L'OUST disparaît ; les trois membres de la famille KERHERVÉ deviennent associés de PROVENDES DU LIÉ.
- *Différence avec un achat des actions (0,5 pt).* Si PROVENDES DU LIÉ achetait les 30 000 actions MOUTURES DE L'OUST, elle les paierait en numéraire, sans augmenter son capital ; MOUTURES DE L'OUST subsisterait comme **filiale**, avec son propre patrimoine, et PROVENDES DU LIÉ inscrirait seulement des **titres de participation** à son actif. Les KERHERVÉ quitteraient le groupe avec le prix de cession. Dans la fusion, ils restent associés (28,57 % du capital, voir 2.3 d) et les deux patrimoines sont réunis dans une seule société.
- *Référentiel (0,5 pt).* L'opération est enregistrée dans les **comptes individuels** des deux sociétés selon le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe le mode d'évaluation des apports et leur inscription chez l'absorbante pour les valeurs du traité [V PCG art. 710-1, 720-1, F01 § 1].

**Régime fiscal de faveur (2 pts)**
- *Conditions (0,75 pt).*
  - Les deux sociétés sont des personnes morales **soumises à l'impôt sur les sociétés** [V CGI art. 210 C-1, F02 § 1].
  - L'opération doit être une **fusion au sens fiscal** : transmission de l'ensemble du patrimoine par suite et au moment de la dissolution sans liquidation, moyennant l'attribution aux associés de titres de l'absorbante et, éventuellement, d'une **soulte ne dépassant pas 10 % de la valeur nominale de ces titres** [V CGI art. 210-0 A, I, 1° a, F02 § 1, complément du 18/11/2026]. La condition de soulte reprend celle du code de commerce : une soulte trop élevée ferait perdre le régime (voir 2.3 b).
  - L'opération ne doit pas avoir pour objectif principal la fraude ou l'évasion fiscales ; elle doit être faite pour des **motifs économiques valables** [V CGI art. 210-0 A, III, F02 § 1] : rapprochement industriel de deux fabricants voisins, utilisation de la ligne de granulation, retrait de M. KERHERVÉ sans repreneur familial.
  - PROVENDES DU LIÉ prend **dans le traité** les engagements de l'art. 210 A-3 [V F02 § 4]. Le régime s'applique de plein droit, sauf option pour le droit commun [V BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1] ; aucun agrément n'est nécessaire, MOUTURES DE L'OUST n'ayant pas de déficit à transférer.
- *Effets pour MOUTURES DE L'OUST (0,5 pt).* Les **plus-values latentes** (terrain 210 000 €, usine 450 000 €, ligne de granulation 250 000 €, matières premières 60 000 €, clientèle et marque) **ne sont pas imposées** chez elle [V CGI art. 210 A-1, F02 § 2] : son résultat de fusion (1 490 000 €, voir 2.5 c) est déduit de son résultat fiscal. En revanche, son **résultat de la période du 1er janvier au 31 mars 2027** est imposé immédiatement, quel que soit le régime, dans une déclaration établie pour cette période [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2] ; l'impôt correspondant figure déjà dans ses dettes fiscales et sera payé par PROVENDES DU LIÉ.
- *Engagements de PROVENDES DU LIÉ (0,75 pt)* [V CGI art. 210 A-3, F02 § 4] :
  - reprendre les provisions dont l'imposition est différée et se substituer à l'absorbée pour les résultats dont l'imposition a été différée (a et b) : sans objet ici ;
  - calculer la plus-value de cession future du **terrain** et du **fonds commercial**, non amortissables, d'après leur **valeur fiscale** chez MOUTURES DE L'OUST (210 000 € pour le terrain, rien pour le fonds commercial) (c) ;
  - **réintégrer** dans ses bénéfices les plus-values des **biens amortissables** : usine, construction, sur **quinze ans** (450 000 / 15 = 30 000 € par an) ; ligne de granulation sur **cinq ans** (250 000 / 5 = 50 000 € par an) ; les plus-values sur constructions (450 000 €) ne représentent que 64,29 % de la plus-value nette sur biens amortissables, sous le seuil de 90 % qui conduirait à retenir leur durée moyenne d'amortissement ; en contrepartie, les amortissements sont calculés sur les valeurs d'apport (d) ;
  - inscrire les **matières premières** à leur valeur fiscale chez MOUTURES DE L'OUST (640 000 €), comme le prévoit l'annexe 2.4 : le profit de 60 000 € sera imposé quand elles seront consommées (e).
  Ces impositions futures justifient la provision pour impôts intégrée à l'apport (2.4).

---

### 2.2 Contrôle, sens et mode d'évaluation (1,5 pt)

- *Situation de contrôle (0,5 pt).* LE GOFF-RIOU Participations détient 80 % des droits de vote de PROVENDES DU LIÉ : elle la contrôle **de manière exclusive** [V PCG art. 741-2, F01 § 2.1]. MOUTURES DE L'OUST est détenue par trois personnes physiques. Aucune des deux sociétés ne détient d'actions de l'autre et aucune personne morale ne contrôle les deux : l'opération est réalisée **sous contrôle distinct** [V art. 741-1, F01 § 2.1]. Le contrôle s'apprécie au niveau des personnes morales.
- *Sens de l'opération (0,5 pt).* Avec 20 000 à 21 000 actions nouvelles, LE GOFF-RIOU Participations détiendra entre 40 000 / 71 000 = **56,34 %** et 40 000 / 70 000 = **57,14 %** des droits de vote : l'actionnaire principal de l'absorbante en **conserve le contrôle exclusif**, bien que dilué. La famille KERHERVÉ détiendra au plus 21 000 / 71 000 = 29,58 % des droits de vote et M. Yann KERHERVÉ au plus 11 550 / 71 000 = 16,27 % ; aucun pacte ne les lie. Les associés de MOUTURES DE L'OUST perdent le contrôle de leur société : la fusion est réalisée **à l'endroit** ; PROVENDES DU LIÉ est l'initiatrice et MOUTURES DE L'OUST la cible [V art. 742-1, F01 § 2.2].
- *Mode d'évaluation (0,5 pt).* Opération à l'endroit sous contrôle distinct : les apports sont évalués à la **valeur réelle** [V art. 743-1, cas 4, F01 § 2.3], c'est-à-dire pour la valeur globale de 3 270 000 €, répartie entre les éléments identifiés et le fonds commercial (2.4).

---

### 2.3 Parité, soulte et adaptations (7,5 pts)

**a) Parité exacte (1 pt)**
- Valeurs unitaires (0,25) : PROVENDES DU LIÉ 8 000 000 / 50 000 = **160 €** ; MOUTURES DE L'OUST 3 270 000 / 30 000 = **109 €**.
- Parité (0,25) : 109 / 160, soit **109 actions PROVENDES DU LIÉ pour 160 actions MOUTURES DE L'OUST** (fraction irréductible : 109 est premier).
- Conclusion (0,5) : elle conduirait à émettre 30 000 × 109 / 160 = **20 437,5 actions**, nombre qui n'est pas entier ; chez chaque associé, le calcul ne tombe pas juste non plus (M. Yann KERHERVÉ : 16 500 × 109 / 160 = 11 240,625 actions). La parité exacte ne peut donc pas être appliquée telle quelle : il faut arrondir la parité et compenser l'arrondi par une soulte, ou régler des rompus. C'est ce que proposent les familles.

**b) Projet des familles (1,5 pt)**

| Élément | Calcul | Montant |
|---|---|---:|
| Actions PROVENDES DU LIÉ à émettre | 30 000 × 2 / 3 | 20 000 |
| Valeur des actions remises | 20 000 × 160 | 3 200 000 |
| Soulte | 10 000 lots × 7 € = 3 270 000 – 3 200 000 | 70 000 |
| **Plafond légal (nominal de 20 €)** | 10 % × 20 000 × 20 | **40 000** |

- Actions et soulte (0,5) ; plafond (0,5) : la soulte ne peut dépasser 10 % de la valeur nominale des actions **attribuées**, c'est-à-dire des actions PROVENDES DU LIÉ [V C. com. L. 236-1, F01 § 4]. Par lot de 3 actions MOUTURES DE L'OUST : 2 actions de 160 € et 7 €, pour un plafond de 10 % × 2 × 20 = 4 €.
- Conclusion (0,25) : la soulte représente **175 % du plafond** : elle est **illégale** et le traité ne peut pas être conclu en ces termes.
- Conséquence fiscale (0,25) : la soulte dépasse aussi la limite de la définition fiscale de la fusion [V CGI art. 210-0 A, I, 1° a, F02 § 1] : l'opération ne pourrait pas bénéficier du régime de faveur, et MOUTURES DE L'OUST serait imposée comme en cas de cessation d'entreprise sur toutes ses plus-values latentes, y compris sur sa clientèle et sa marque [V BOI-IS-FUS-10-10-20 § 10 et 20, F02 § 2] ; aucune provision pour impôts ne serait alors intégrée à l'apport [V F02 § 6].

**c) Pistes d'adaptation et conseil (3 pts)**

| | Piste A | Piste B | Piste C |
|---|---|---|---|
| Parité ; nominal | 2 pour 3 ; 20 € | 17 pour 25 ; 20 € | 2 pour 3 ; 40 € |
| Actions émises | 20 000 | 30 000 × 17 / 25 = 20 400 | 20 000 |
| Valeur des actions remises | 3 200 000 | 20 400 × 160 = 3 264 000 | 3 200 000 |
| Soulte | 40 000 (4 € par lot de 3) | 6 000 (5 € par lot de 25) | 70 000 (7 € par lot de 3) |
| Plafond légal | 10 % × 20 000 × 20 = 40 000 | 10 % × 20 400 × 20 = 40 800 | 10 % × 20 000 × 40 = 80 000 |
| Légalité | légale (100 % du plafond) | légale (14,71 %) | légale (87,50 %) |
| Valeur reçue par les associés de MOUTURES DE L'OUST | 3 240 000 (– 30 000) | 3 270 000 | 3 270 000 |
| Numéraire reçu par Mme Nolwenn KERHERVÉ (25 %) | 10 000 | 1 500 | 17 500 |
| LE GOFF-RIOU Participations après l'opération | 57,14 % | 56,82 % | 57,14 % |

- *Piste A (0,75 pt).* La soulte est ramenée au plafond sans action supplémentaire : la loi est respectée, mais les associés de MOUTURES DE L'OUST reçoivent **30 000 € de moins** que la valeur de leurs actions (1 € par action, 0,92 %), au profit des associés actuels de PROVENDES DU LIÉ, qui reçoivent un patrimoine de 3 270 000 € contre 3 240 000 € : l'échange est **inéquitable**. Mme Nolwenn KERHERVÉ n'obtiendrait que 10 000 €. Sur le plan fiscal, le régime de faveur ne s'applique pas aux opérations qui organisent entre associés et sociétés des transferts de valeurs non représentatives des apports ; lorsque la valeur réelle des titres remis est inférieure à celle de l'apport, la différence est un produit taxable qui correspond à une libéralité [V BOI-IS-FUS-30-20 § 20 et 30, F02 § 1]. Piste **à écarter**.
- *Piste B (0,75 pt).* Arrondi plus fin de la parité : 20 400 actions, dans la fourchette de la lettre d'intention ; soulte de 6 000 €, très en dessous du plafond ; échange **équitable** (3 264 000 + 6 000 = 3 270 000) et régime de faveur préservé. Les avoirs de chaque associé étant des multiples de 25, il n'y a pas de rompus. Mais la parité de 17 pour 25, à laquelle les familles ne tiennent pas, est moins lisible, et Mme Nolwenn KERHERVÉ ne recevrait que 1 500 €.
- *Piste C (1 pt).* Valeur nominale minimale (0,25) : la soulte de 70 000 € est légale si 10 % × 20 000 × N ≥ 70 000, soit **N ≥ 35 €** ; à 40 €, le plafond est de **80 000 €** et la soulte légale (0,25). L'élévation du nominal par incorporation de réserves est une augmentation de capital [V C. com. L. 225-130, F01 § 4, complément du 18/11/2026] ; elle ne change ni la valeur de PROVENDES DU LIÉ (8 000 000 €), ni la valeur unitaire de ses actions (160 €), ni la répartition de son capital : l'échange reste **équitable** et la parité du projet est conservée (0,25). La soulte reste sous 10 % du nominal des actions attribuées : le **régime de faveur est préservé**. Coûts : 1 000 000 € d'autres réserves deviennent du capital, qui ne peut plus être distribué ; la trésorerie verse 70 000 € au lieu de 6 000 € ; la marge sous le plafond est plus étroite (10 000 €) si les valeurs devaient être revues avant la signature du traité (0,25).
- *Conseil (0,5 pt).* Conseiller la **piste C** : c'est la seule qui respecte à la fois la loi et la condition fiscale, l'équité entre les deux familles, la parité à laquelle elles tiennent, la limite de 21 000 actions et le souhait de Mme Nolwenn KERHERVÉ (17 500 € ≥ 15 000 €). Son coût reste supportable : il resterait 2 600 000 € d'autres réserves, et un capital plus élevé renforce la garantie des créanciers. La piste B est une solution de repli si LE GOFF-RIOU Participations refuse de rendre des réserves indisponibles et si Mme KERHERVÉ renonce au numéraire ; la piste A est à écarter.

**d) Piste retenue (2 pts)**
- Incorporation de réserves (0,25) : 50 000 × (40 – 20) = **1 000 000 €** ; capital avant la fusion : 50 000 × 40 = 2 000 000 €.
- Augmentation de capital (0,5) : 20 000 × 40 = **800 000 €**.
- Prime de fusion (0,5) : valeur des apports – augmentation de capital – soulte = 3 270 000 – 800 000 – 70 000 = **2 400 000 €**. Contrôle : 20 000 × 160 + 70 000 = 3 270 000 = 30 000 × 109.
- Répartition du capital après l'opération (0,75) :

| Associé | Actions | % du capital et des droits de vote | Soulte reçue (€) |
|---|---:|---:|---:|
| LE GOFF-RIOU Participations | 40 000 | 57,14 % | |
| Autres associés de PROVENDES DU LIÉ | 10 000 | 14,29 % | |
| M. Yann KERHERVÉ (16 500 × 2 / 3) | 11 000 | 15,71 % | 38 500 |
| Mme Nolwenn KERHERVÉ (7 500 × 2 / 3) | 5 000 | 7,14 % | 17 500 |
| M. Erwan KERHERVÉ (6 000 × 2 / 3) | 4 000 | 5,71 % | 14 000 |
| **Total** | **70 000** | **100 %** | **70 000** |

Capital après l'opération : 70 000 × 40 = 2 800 000 €. LE GOFF-RIOU Participations garde le contrôle exclusif ; la famille KERHERVÉ détient 28,57 % des droits de vote, ce qui confirme le sens de l'opération (2.2).

---

### 2.4 Valeur réelle et composition des apports (3 pts)

- *Éléments identifiés à la valeur réelle (1 pt).*

| Élément | Valeur nette comptable | Valeur réelle | Écart | Base d'impôt différé |
|---|---:|---:|---:|---:|
| Terrain | 210 000 | 420 000 | 210 000 | 0 (pas de cession envisagée) |
| Usine (bâtiments) | 1 150 000 | 1 600 000 | 450 000 | 450 000 |
| Ligne de granulation | 720 000 | 970 000 | 250 000 | 250 000 |
| Matériel de transport | 260 000 | 260 000 | | |
| Matières premières | 640 000 | 700 000 | 60 000 | 60 000 |
| Produits finis, clients, disponibilités | 1 500 000 | 1 500 000 | | |
| Engagements de retraite (passif hors bilan) | 0 | – 200 000 | – 200 000 | – 200 000 |

  Les engagements de retraite, que MOUTURES DE L'OUST ne provisionnait pas, sont un **passif identifié** qui figure dans l'apport à la valeur réelle [V PCG art. 744-1, F01 § 3.1] ; PROVENDES DU LIÉ, qui provisionne ses propres engagements, les inscrit en provision.
- *Provision pour impôts (1 pt).* Base nette : 450 000 + 250 000 + 60 000 – 200 000 = 560 000 € ; impôt différé : 560 000 × 25 % = **140 000 €** (passifs de 190 000 € sur les plus-values imposées plus tard, actif de 50 000 € sur les engagements de retraite, déductibles au versement), inscrit en **provision pour impôts** [V art. 744-1 ; méthode du corrigé du sujet zéro, F01 § 3.3]. Rien sur le terrain ni sur le fonds commercial (hypothèses de l'annexe 2.4).
- *Fonds commercial et composition (1 pt).*

| Composition de l'apport | Montant (€) |
|---|---:|
| Actifs identifiés : 420 000 + 1 600 000 + 970 000 + 260 000 + 700 000 + 150 000 + 1 120 000 + 230 000 | 5 450 000 |
| – Dettes reprises (1 320 000 + 960 000 + 180 000 + 240 000) | – 2 700 000 |
| – Provision pour engagements de retraite | – 200 000 |
| – Provision pour impôts | – 140 000 |
| **Actif net identifié** | **2 410 000** |
| **Fonds commercial** (3 270 000 – 2 410 000) | **860 000** |
| **Valeur globale des apports** | **3 270 000** |

L'écart positif entre la valeur globale et l'actif net identifié est inscrit en **fonds commercial** (compte 207) [V art. 744-1, F01 § 3.1] ; il représente la clientèle et la marque, non inscrites au bilan de MOUTURES DE L'OUST.

---

### 2.5 Écritures au 31 mars 2027 (7 pts)

Toutes les écritures ci-dessous sont équilibrées.

**a) PROVENDES DU LIÉ : écritures de base (3 pts)**

**A1 — Élévation du nominal (0,5 pt).** Incorporation de 20 € par action, décidée avant la fusion (piste C).

| Compte | Débit | Crédit |
|---|---:|---:|
| 1068 Autres réserves | 1 000 000 | |
| 101 Capital | | 1 000 000 |

**A2 — Augmentation de capital et soulte due (0,75 pt).** Capital (0,25), prime nette de la soulte (0,25), soulte au passif (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société | 3 270 000 | |
| 101 Capital (20 000 × 40) | | 800 000 |
| 1042 Primes de fusion | | 2 400 000 |
| 468 Divers comptes créditeurs – soulte due aux associés de MOUTURES DE L'OUST | | 70 000 |

**A3 — Réalisation des apports à la valeur réelle (1,5 pt).** Actifs identifiés à leur valeur réelle, **sans amortissements** (0,5) ; dettes, provision pour engagements de retraite et provision pour impôts (0,5) ; fonds commercial (0,25) ; solde du compte d'apport (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 207 Fonds commercial | 860 000 | |
| 211 Terrains | 420 000 | |
| 2131 Bâtiments (usine de Rostrenen) | 1 600 000 | |
| 2154 Matériels industriels (ligne de granulation) | 970 000 | |
| 2182 Matériel de transport | 260 000 | |
| 31 Matières premières et fournitures | 700 000 | |
| 355 Produits finis | 150 000 | |
| 411 Clients (dont créance sur PROVENDES DU LIÉ 72 000) | 1 120 000 | |
| 512 Banques | 230 000 | |
| 1521 Provisions pour pensions et obligations similaires | | 200 000 |
| 1523 Provisions pour impôts | | 140 000 |
| 164 Emprunts auprès des établissements de crédit | | 1 320 000 |
| 401 Fournisseurs (dont dette envers PROVENDES DU LIÉ 45 000) | | 960 000 |
| 43 Sécurité sociale et autres organismes sociaux | | 180 000 |
| 44 État et autres collectivités publiques | | 240 000 |
| 4561 Associés – Comptes d'apport en société | | 3 270 000 |
| **Total** | **6 310 000** | **6 310 000** |

**A4 — Versement de la soulte (0,25 pt).**

| Compte | Débit | Crédit |
|---|---:|---:|
| 468 Divers comptes créditeurs – soulte due | 70 000 | |
| 512 Banques | | 70 000 |

**b) PROVENDES DU LIÉ : écritures complémentaires (2 pts)**

PROVENDES DU LIÉ reçoit avec l'apport une créance sur elle-même (72 000 €) et une dette envers elle-même (45 000 €) : devenue à la fois créancière et débitrice de chacune de ces obligations, elle les voit **s'éteindre par confusion** [V C. civ. art. 1349, F01 § 8].

**A5 — Dette de PROVENDES DU LIÉ envers MOUTURES DE L'OUST (0,5 pt).**

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette envers MOUTURES DE L'OUST) | 72 000 | |
| 411 Clients (créance reçue de MOUTURES DE L'OUST) | | 72 000 |

**A6 — Créance de PROVENDES DU LIÉ sur MOUTURES DE L'OUST (0,5 pt).**

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette reçue de MOUTURES DE L'OUST) | 45 000 | |
| 411 Clients (créance sur MOUTURES DE L'OUST) | | 45 000 |

**A7 — Frais de fusion (1 pt).** Les frais de fusion peuvent être imputés sur la prime de fusion [V PCG art. 212-9, F01 § 7] ; l'imputation se fait pour le montant **net d'impôt**, comme le prévoit l'annexe 2.5 [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 52 000 × 75 % = **39 000 €** sur la prime (0,5) ; l'économie d'impôt de 13 000 € diminue l'impôt de 2027 (0,25) ; écriture (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion | 39 000 | |
| 444 État – Impôts sur les bénéfices | 13 000 | |
| 512 Banques | | 52 000 |

Prime de fusion après imputation : 2 400 000 – 39 000 = **2 361 000 €**.

**c) MOUTURES DE L'OUST (2 pts)**

**A8 — Transmission du patrimoine et résultat de fusion (1 pt).** Sortie des actifs à leur valeur brute et de leurs amortissements, et des dettes (0,5) ; créance sur PROVENDES DU LIÉ pour la valeur d'apport et résultat de fusion, 3 270 000 – 1 780 000 = **1 490 000 €**, présenté en résultat exceptionnel selon l'annexe 2.5 (0,5) [V PCG art. 513-5 ; choix du compte 778 : convention de rédaction, F01 § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – PROVENDES DU LIÉ, compte d'apport | 3 270 000 | |
| 2813 Amortissements des constructions | 1 450 000 | |
| 2815 Amortissements des installations, matériel et outillage industriels | 1 080 000 | |
| 2818 Amortissements des autres immobilisations corporelles (matériel de transport) | 340 000 | |
| 164 Emprunts auprès des établissements de crédit | 1 320 000 | |
| 401 Fournisseurs | 960 000 | |
| 43 Sécurité sociale et autres organismes sociaux | 180 000 | |
| 44 État et autres collectivités publiques | 240 000 | |
| 211 Terrains | | 210 000 |
| 2131 Bâtiments | | 2 600 000 |
| 2154 Matériels industriels | | 1 800 000 |
| 2182 Matériel de transport | | 600 000 |
| 31 Matières premières et fournitures | | 640 000 |
| 355 Produits finis | | 150 000 |
| 411 Clients | | 1 120 000 |
| 512 Banques | | 230 000 |
| 778 Autres produits exceptionnels (résultat de fusion) | | 1 490 000 |
| **Total** | **8 840 000** | **8 840 000** |

En régime de faveur, ce résultat n'est pas imposé (2.1) : il est déduit extra-comptablement.

**A9 — Droits des associés sur l'actif net (0,5 pt).** Les capitaux propres, résultat de fusion compris, reviennent aux associés à proportion de leurs actions : 3 270 000 × 55 %, 25 % et 20 %.

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 300 000 | |
| 1061 Réserve légale | 30 000 | |
| 1068 Autres réserves | 1 330 000 | |
| 120 Résultat de l'exercice (120 000 + 1 490 000) | 1 610 000 | |
| 456 Associés – Opérations sur le capital (Yann KERHERVÉ) | | 1 798 500 |
| 456 Associés – Opérations sur le capital (Nolwenn KERHERVÉ) | | 817 500 |
| 456 Associés – Opérations sur le capital (Erwan KERHERVÉ) | | 654 000 |

**A10 — Remise des actions et de la soulte aux associés (0,5 pt).** PROVENDES DU LIÉ remet directement les actions et la soulte aux associés (annexe 2.5) : leurs droits sont réglés et la créance sur PROVENDES DU LIÉ est soldée. Contrôle par associé : M. Yann KERHERVÉ reçoit 11 000 × 160 + 38 500 = 1 798 500 € ; Mme Nolwenn KERHERVÉ 5 000 × 160 + 17 500 = 817 500 € ; M. Erwan KERHERVÉ 4 000 × 160 + 14 000 = 654 000 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital (Yann KERHERVÉ) | 1 798 500 | |
| 456 Associés – Opérations sur le capital (Nolwenn KERHERVÉ) | 817 500 | |
| 456 Associés – Opérations sur le capital (Erwan KERHERVÉ) | 654 000 | |
| 467 Divers comptes débiteurs – PROVENDES DU LIÉ, compte d'apport | | 3 270 000 |

Tous les comptes de MOUTURES DE L'OUST sont soldés.

---

### 2.6 Note à Mme LE GOFF-RIOU, présidente de PROVENDES DU LIÉ (2 pts)

*Objet : effets de l'absorption de MOUTURES DE L'OUST sur les comptes et sur le capital de PROVENDES DU LIÉ.*

- *Capitaux propres juste après la fusion (0,75 pt).*

| Poste (en €) | Avant | Élévation du nominal | Fusion et frais | Après |
|---|---:|---:|---:|---:|
| Capital | 1 000 000 | + 1 000 000 | + 800 000 | 2 800 000 |
| Primes de fusion | – | | + 2 400 000 – 39 000 | 2 361 000 |
| Réserve légale | 100 000 | | | 100 000 |
| Autres réserves | 3 600 000 | – 1 000 000 | | 2 600 000 |
| Report à nouveau | 200 000 | | | 200 000 |
| **Total** | **4 900 000** | **0** | **+ 3 161 000** | **8 061 000** |

  Les capitaux propres augmentent de 3 161 000 € (+ 64,51 %) : valeur des apports (3 270 000 €) moins la soulte (70 000 €) et les frais nets d'impôt (39 000 €). L'élévation du nominal ne change pas leur total, mais elle rend 1 000 000 € de réserves indisponibles.
- *Capital et contrôle (0,25 pt).* 70 000 actions de 40 € : LE GOFF-RIOU Participations détient 57,14 % des droits de vote et garde le contrôle exclusif ; la famille KERHERVÉ en détient 28,57 %, dont 15,71 % pour M. Yann KERHERVÉ, et les autres associés 14,29 %.
- *Banques (0,5 pt).* Les emprunts passent de 3 600 000 € à 4 920 000 € avec ceux de MOUTURES DE L'OUST, dont les banques ont désormais PROVENDES DU LIÉ pour débitrice ; rapportés aux capitaux propres, ils baissent de 0,73 à 0,61. Le capital, porté à 2 800 000 €, est un gage plus durable que des réserves distribuables. Les banques noteront aussi que 860 000 € de l'actif reçu sont un fonds commercial, dont la valeur dépend de la conservation de la clientèle, et que la trésorerie passe de 900 000 € à 1 008 000 € (+ 230 000 reçus, – 70 000 de soulte, – 52 000 de frais).
- *Personnel venu de MOUTURES DE L'OUST (0,25 pt).* Ses indemnités de fin de carrière, que MOUTURES DE L'OUST ne provisionnait pas, figurent désormais au bilan de PROVENDES DU LIÉ en provision (200 000 €), à côté de celles de son propre personnel (260 000 €) : ses droits sont reconnus dans les comptes de son nouvel employeur.
- *Administration fiscale (0,25 pt).* Elle recevra la déclaration du résultat de MOUTURES DE L'OUST du 1er janvier au 31 mars 2027 et vérifiera que la soulte reste sous 10 % du nominal des actions attribuées (70 000 € pour 80 000 €), condition du régime de faveur, puis le respect des engagements de PROVENDES DU LIÉ : réintégration de 80 000 € par an pendant cinq ans (30 000 € pour l'usine, 50 000 € pour la ligne de granulation), puis de 30 000 € par an jusqu'à la quinzième année ; valeur fiscale du terrain, du fonds commercial et des matières premières. La provision pour impôts de 140 000 € traduit ces impositions futures dans les comptes.

---

### Réponses tolérées
- **2.1** : régime de faveur présenté sans la condition de motif économique, si la condition de soulte est énoncée ; réintégration des plus-values non chiffrée si les durées de quinze et cinq ans sont données.
- **2.2** : sens de l'opération justifié par la répartition du capital de la piste C (57,14 %) plutôt que par la fourchette de la lettre d'intention.
- **2.3 a** : parité exprimée en nombre décimal (0,68125 action PROVENDES DU LIÉ par action MOUTURES DE L'OUST) si le nombre non entier d'actions est relevé.
- **2.3 c** : étude, en plus ou à la place de l'une des pistes, de la réduction de la soulte avec émission d'actions supplémentaires au nominal de 20 € : au moins 3 270 000 / (160 + 2) = 20 185,2, soit **20 186 actions**, soulte 40 240 € pour un plafond de 40 372 € ; solution légale et équitable, mais sans parité simple (rompus chez chaque associé) et avec 10 060 € seulement pour Mme Nolwenn KERHERVÉ. Un conseil en faveur de la piste B est accepté s'il est justifié par le coût de l'indisponibilité des réserves et s'il constate que le souhait de Mme KERHERVÉ n'est pas satisfait ; l'item du conseil est alors compté à moitié [JUR-F08].
- **2.5 a** : A2 et A4 réunies (soulte créditée directement en 512) ; soulte inscrite au crédit du compte 4567 ou d'un compte 467 justifié ; dettes fiscales et sociales regroupées sur un compte de la classe 4 ; ligne de granulation en 2151 ou en 215.
- **2.5 c** : inscription des actions PROVENDES DU LIÉ reçues en 503 ou en 508, puis remise aux associés (présentation en deux temps) ; résultat de fusion au compte 757 avec mention de l'hypothèse ; A9 et A10 réunies.
- **2.6** : capitaux propres présentés sans la colonne de l'élévation du nominal, si le total et chaque poste sont justes.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion calculée sans déduire la soulte (2 470 000 €), ou avec l'ancien nominal (3 270 000 – 400 000 – 70 000 = 2 800 000 €) ; frais imputés pour leur montant brut (52 000 €).
- `JUR-R05` Difficulté à s'adapter : plafond calculé sur le nominal des actions MOUTURES DE L'OUST (10 % × 30 000 × 10 = 30 000 €), sur la valeur des actions remises ou sur la valeur des apports ; piste A jugée satisfaisante parce qu'elle est légale, sans voir la perte de 30 000 € pour la famille KERHERVÉ ; élévation du nominal présentée comme un changement de la valeur unitaire ou de la parité.
- `JUR-F07` Annexes mal exploitées : engagements de retraite oubliés dans l'apport ou dans l'impôt différé, impôt différé calculé sur le terrain ou sur le fonds commercial, une seule des deux créances réciproques éliminée, amortissements repris chez l'absorbante.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A3 et A8.
- `JUR-F02` Calculs non détaillés : soulte et plafond donnés sans le calcul par lot ou au total, nombre minimal de nominal non justifié.
- Erreurs propres à ce cas : fusion qualifiée d'acquisition de titres ; contrôle commun retenu au motif que les deux sociétés sont familiales ; valeur comptable retenue ; date d'effet placée au 1er janvier 2027 ; résultat de fusion de MOUTURES DE L'OUST déclaré imposable sous le régime de faveur.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 236-1 | Fusion, dissolution sans liquidation, transmission universelle, attribution d'actions aux associés, soulte limitée à 10 % de la valeur nominale des actions attribuées | [V] Légifrance | F01 § 1 et § 4 |
| C. com. L. 225-130 et L. 227-1 | Augmentation de capital par majoration du nominal des actions existantes, par incorporation de réserves ; règles de la société anonyme applicables à la SAS | [V] lus le 18/11/2026 | F01 § 4 |
| PCG art. 710-1, 710-2, 720-1 | Champ du titre VII, définition de la fusion, inscription des apports pour les valeurs du traité | [V] p. 81 | F01 § 1 |
| PCG art. 741-1, 741-2, 742-1, 743-1 | Contrôle distinct, sens à l'endroit, valeur réelle | [V] p. 82-84 | F01 § 2 |
| PCG art. 744-1 ; corrigé du sujet zéro | Valeurs réelles des éléments figurant ou non au bilan (engagements de retraite, impôts différés), fonds commercial ; méthode de la provision pour impôts | [V] p. 85 ; p. imprimée 216 | F01 § 3.1 et § 3.3 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais de fusion imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion des créances et dettes réciproques | [V] | F01 § 8 |
| PCG art. 513-5 ; compte 778 | Résultat de fusion de l'absorbée en résultat exceptionnel (hypothèse de l'énoncé) | [V] p. 42-43 ; choix du compte : convention de rédaction | F01 § 9 |
| CGI art. 210-0 A, 210 A, 210 C ; BOI-IS-FUS-10-10-10 § 10 et 20 ; BOI-IS-FUS-10-20-30 § 210 et 330 ; BOI-IS-FUS-10-10-20 § 10 et 20 | Définition fiscale de la fusion et condition de soulte, motif économique, régime de plein droit, dernier résultat de l'absorbée, plus-values, engagements, droit commun | [V] | F02 § 1, § 2 et § 4 |
| BOI-IS-FUS-30-20 § 20 et 30 | Rémunération sur la base des valeurs réelles ; transferts de valeur entre associés incompatibles avec le régime de faveur ; produit taxable correspondant à la libéralité | [V] BOFiP | F02 § 1 |
| Comptes 456, 467 et 468 (absorbée et absorbante) | Droits des associés, compte d'apport, soulte due | Convention de rédaction (le PCG ne donne pas d'écriture pour l'absorbée) | F01 § 9 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Détention du capital et des droits de vote, direction et inscription des sociétés de commissaires aux comptes et d'expertise comptable ; projet du fonds | `3.1.a` Cadres d'exercice professionnel | 2 |
| 3.2 Fin normale du mandat, renouvellement exprès, durée de six exercices | `3.1.b` Nomination et cessation | 1 |
| 3.3 Associé élu à l'agglomération actionnaire ; chiffrage de la provision (autorévision) | `3.1.c` Principes déontologiques | 1,5 |
| 3.4 Certification, audit contractuel et examen de la gestion ; portée de l'opinion pour les élus | `3.2.a` Notion d'audit et typologie des missions | 1,5 |
| 3.5 Risque du cycle litiges et provisions et assertions ; extrait de la NEP applications spécifiques ; procédures | `3.2.c` Approche par les risques ; `3.1.d` Référentiel normatif (NEP) ; `3.2.d` Démarche d'audit | 5,5 |
| 3.6 Droit de communication, secret des avocats, circuit de la demande, conséquences d'un refus | `3.2.b` Moyens d'action du CAC | 2 |
| 3.7 Jugement et tempête après la clôture ; écriture ; opinion selon la correction ; parties du rapport | `3.2.e` Portée des opinions | 2 |
| 3.8 Responsabilités civile, pénale et disciplinaire envers la banque | `3.1.e` Mise en cause de la responsabilité | 2,5 |
| 3.9 Architecture des ESRS ; étendue et limites ; publication limitée au climat | `3.3.a` Contexte et architecture des normes de durabilité | 2,5 |
| 3.10 Entreprise déclarante, actifs exploités, contrôle opérationnel, chaîne de valeur ; périmètre de la direction | `3.3.b` Principes de construction du reporting | 3,5 |
| 3.11 Objectifs, assurance limitée, axes, consultation du CSE ; procédures sur le périmètre et les données | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4,5 |
| 3.12 Avis sur les informations selon la correction ; portée | `3.4.c` Portée des avis | 1,5 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Ouverture du capital du cabinet à un fonds (2 pts)

**Conditions et autorités (1 pt)**
- **Société de commissaires aux comptes (0,5 pt)** : pour être inscrite sur la **liste des commissaires aux comptes tenue par la H2A**, qui peut déléguer l'inscription à la CNCC, une société doit remplir trois conditions : la **majorité des droits de vote** est détenue par des commissaires aux comptes ou des sociétés de commissaires aux comptes inscrits ; les fonctions de **direction** (président, directeur général, directeur général délégué…) sont assurées par des commissaires aux comptes ; la **majorité au moins des membres** des organes de gestion, d'administration ou de surveillance sont des commissaires aux comptes [V L. 821-13 I, L. 820-1 II, L. 821-16].
- **Société d'expertise comptable (0,5 pt)** : elle est **inscrite au tableau de l'ordre**, tenu par le **conseil régional de l'ordre** ; les experts-comptables y détiennent, directement ou par une société inscrite à l'ordre, **plus des deux tiers des droits de vote** ; aucune personne ou groupement d'intérêts extérieur ne peut détenir une part des droits de vote de nature à mettre en péril l'exercice de la profession ; les **représentants légaux** sont des experts-comptables associés ; la liste des associés est communiquée chaque année à l'ordre [V ord. 45-2138 art. 7 I-II, art. 31, art. 40]. Le cabinet TRÉGOREL, inscrit sur les deux listes, doit respecter **les deux séries de conditions** [S].

**Appréciation du projet (0,75 pt)**
- **Droits de vote (0,25 pt)** : après la cession, les quatre associés commissaires aux comptes détiennent 8 800 × 60 % = 5 280 voix, soit **52,8 %** : la majorité exigée pour la société de commissaires aux comptes est respectée. Les experts-comptables (les cinq associés) détiennent 5 280 + 720 = 6 000 voix, soit **60 %**, moins des deux tiers exigés : le cabinet **ne pourrait plus rester inscrit au tableau** [V ord. art. 7 II 1° ; calcul].
- **Directeur général non professionnel (0,25 pt)** : M. LE DUFF n'est ni commissaire aux comptes ni expert-comptable ; un directeur général doit être commissaire aux comptes pour la liste de la H2A et expert-comptable associé pour le tableau [V L. 821-16 2° ; ord. art. 7 II 4°].
- **Veto sur le budget et sur les honoraires (0,25 pt)** : un investisseur extérieur qui contrôlerait les honoraires des principaux dossiers pourrait peser sur les diligences et sur les opinions : c'est une part des droits « de nature à mettre en péril l'exercice de la profession » et une atteinte à l'**indépendance** des commissaires aux comptes, dont les honoraires doivent être en rapport avec les diligences [V ord. art. 7 II 2° ; L. 821-27 1° ; code de déontologie art. 12 ; S, application].

**Conditions de réalisation (0,25 pt)** : le fonds peut entrer au capital s'il détient **moins du tiers des droits de vote** (par exemple 30 % : experts-comptables 70 %, commissaires aux comptes 61,6 %), **sans fonction de direction** ni droit de veto sur l'activité professionnelle ; le cabinet informe l'ordre de la modification de ses associés [V ord. art. 7 II 5° ; S, application].

**Réponses tolérées**
- La mention d'une augmentation de capital réservée au fonds plutôt qu'une cession, si les pourcentages sont recalculés.
- La seule conclusion « projet impossible en l'état », sans proposition chiffrée, si les trois obstacles sont identifiés : 0,5 pt sur 0,75 en appréciation et 0 en conditions.

**Erreurs fréquentes**
- Appliquer à la société d'expertise comptable la majorité simple des sociétés de commissaires aux comptes, ou l'inverse (`JUR-A05`).
- Décrire l'organisation interne de l'ordre, de la H2A ou de la CNCC, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 820-1 II, L. 821-13 I, L. 821-16 | Liste de la H2A ; conditions des sociétés de commissaires aux comptes | [V] | F09 § 3.1-3.2, § 17 |
| Ord. 45-2138 art. 3, 7, 31, 40 | Sociétés d'expertise comptable : deux tiers des droits de vote, représentants légaux, tableau | [V] ; application : [S] | F09 § 2, § 17 |
| C. com. L. 821-27 1° ; code de déontologie art. 12 | Indépendance ; honoraires en rapport avec les diligences | [V] | F10 § 4.1, § 12 |

### 3.2 Terme et renouvellement du mandat (1 pt)

- **Fin normale (0,25 pt)** : le cabinet a été nommé pour **six exercices**, de 2021 à 2026 ; ses fonctions expirent après la délibération de l'assemblée générale qui statuera sur les comptes de 2026, en juin 2027 (le 24/06/2027 selon le calendrier de l'annexe 3.7) [V L. 821-44 al. 1].
- **Pas de prolongation automatique (0,25 pt)** : le mandat ne se renouvelle pas tacitement. La SEM dépasse deux des trois seuils (total du bilan de 6 480 000 € et 6 120 000 € > 5 000 000 € ; 64 et 63 salariés > 50 ; chiffre d'affaires inférieur à 10 000 000 €) au cours des deux exercices précédant l'expiration du mandat : elle reste tenue d'avoir un commissaire aux comptes [V L. 225-218 al. 2, D. 221-5, D. 225-164-1]. L'**assemblée générale ordinaire** doit donc désigner, par une décision expresse, le cabinet ou un autre commissaire aux comptes [V L. 821-40 I]. S'il est proposé de ne pas le renouveler, le cabinet est entendu à sa demande [V L. 821-51].
- **Durée du nouveau mandat (0,5 pt)** : six exercices, de 2027 à 2032. Le mandat de trois exercices n'est ouvert qu'aux désignations volontaires ou à celles fondées sur les règles des petits groupes ; une désignation imposée par les seuils ne peut pas être limitée à trois exercices [V L. 821-44, L. 821-46]. Rien n'impose de changer d'associé signataire : la rotation ne vise que certaines entités (entités d'intérêt public notamment), dont la SEM ne fait pas partie [V L. 821-34 I ; S, application]. Pour remettre la mission en concurrence, l'assemblée peut choisir un autre commissaire aux comptes à l'expiration de chaque mandat de six exercices.

**Réponses tolérées**
- La mention que la mission sur la durabilité, volontaire et confiée pour trois exercices (2026 à 2028), suit son propre calendrier.

**Erreurs fréquentes**
- Admettre une reconduction tacite ou un mandat de trois exercices pour une désignation imposée (`JUR-A01`).
- Développer la procédure de convocation ou les formalités de greffe, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-40 I, L. 821-44, L. 821-46, L. 821-51 | Désignation, durée, trois exercices, non-renouvellement | [V] | F09 § 3.4-3.5, § 13, § 17 |
| C. com. L. 225-218 ; D. 221-5 ; D. 225-164-1 ; L. 821-34 I | Seuils, fin de l'obligation ; rotation | [V] ; application : [S] | F09 § 3.3 ; F10 § 6 |

### 3.3 Situation de M. PRIGENT et demande de chiffrage (1,5 pt)

**M. PRIGENT (1 pt)**
- **Qualification (0,5 pt)** : l'indépendance s'apprécie **en réalité et en apparence**, et s'impose à toute personne en mesure d'influer, même indirectement, sur la mission [V code de déontologie art. 5 I-II]. M. PRIGENT ne participe pas à la mission, mais il siège au comité de direction qui fixe la rémunération et les promotions des collaborateurs : c'est un **membre de la direction** du cabinet [V art. 31]. Son mandat au conseil de l'agglomération, qui contrôle la SEM avec 60 % du capital, et sa place dans la commission qui examine le rapport d'activité de la SEM le placent dans une position d'influence sur l'entité certifiée. Ce n'est ni un lien personnel au sens du code (liens familiaux) ni un lien professionnel (contrat de travail, relation d'affaires) [V art. 32, 34] : c'est une **situation à risque**, qu'un tiers objectif, raisonnable et informé pourrait juger de nature à compromettre l'impartialité du cabinet [V A. 821-55 § 11, § 23 ; S, application].
- **Sauvegardes (0,25 pt)** : tenir M. PRIGENT à l'écart de la mission (aucun accès au dossier, aucune intervention sur l'équipe, ses évaluations et ses promotions) ; qu'il ne prenne part à aucune délibération ni à aucun examen de la SEM à l'agglomération ; documenter l'analyse et en informer la SEM [V A. 821-55 § 23-30, § 41-43 ; S, choix des mesures].
- **Représentant au conseil d'administration (0,25 pt)** : s'il devenait administrateur de la SEM, M. PRIGENT exercerait lui-même une **fonction sensible** (mandataire social) dans l'entité certifiée, alors qu'un simple lien familial entre un membre de la direction du cabinet et un mandataire social est déjà incompatible [V art. 31-32 II]. Aucune sauvegarde n'est possible : il doit refuser ce mandat, ou le cabinet devrait mettre fin à sa mission [V L. 821-27 1° ; art. 5 III, art. 35 ; S, application].

**Chiffrage de la provision (0,5 pt)** : le cabinet se prononcerait sur une provision qu'il aurait lui-même évaluée : **risque d'autorévision**, interdit hors entité d'intérêt public lorsqu'aucune sauvegarde n'est possible, et immixtion dans une décision de la direction [V code de déontologie art. 5 II ; L. 821-28 IV ; L. 821-54 I]. Le cabinet **refuse** : l'estimation relève de la direction, qui peut s'appuyer sur son avocat (annexe 3.5) ; le cabinet appréciera ensuite la méthode, les hypothèses et le montant retenus.

**Réponses tolérées**
- La conclusion qu'un mandat électif à l'agglomération est en soi incompatible, si elle est motivée par l'apparence d'indépendance : 0,25 pt sur 0,5 en qualification.

**Erreurs fréquentes**
- Conclure à l'absence de risque parce que M. PRIGENT ne signe pas les comptes (`JUR-A05`).
- Admettre le chiffrage au motif que le cabinet connaît le dossier, ou confondre l'indépendance du commissaire aux comptes et celle de l'expert-comptable (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 5, 31, 32, 34, 35 ; C. com. L. 821-27 1° | Influence sur la mission ; membres de la direction ; fonctions sensibles ; survenance | [V] ; application : [S] | F10 § 4.1, § 14 |
| A. 821-55 § 11, § 23-30, § 41-43 | Tiers objectif ; sauvegardes ; documentation | [V] | F10 § 12 |
| C. com. L. 821-28 IV, L. 821-54 I | Autorévision hors entité d'intérêt public ; non-immixtion | [V] | F10 § 5 ; F09 § 6 |

### 3.4 Demande de l'agglomération (1,5 pt)

- **Certification des comptes (0,5 pt)** : mission **légale** ; le cabinet certifie que les comptes annuels sont **réguliers et sincères et donnent une image fidèle** du résultat, de la situation financière et du patrimoine ; il exprime une **opinion** fondée sur une **assurance raisonnable**, élevée mais non absolue, que les comptes **pris dans leur ensemble** ne comportent pas d'anomalies significatives ; le rapport est destiné à l'assemblée générale [V L. 821-53 al. 1 ; NEP principes § 01, § 08-09].
- **Audit contractuel et examen de la gestion (0,5 pt)** : un **audit contractuel** est une **prestation** (la norme cite l'audit financier contractuel en exemple), définie par une lettre de mission [V A. 821-55 § 08 ; R. 821-195] ; il porte sur des informations financières déterminées par le contrat [S]. L'« audit de la gestion du parc » demandé est autre chose : un **examen de la gestion** (taux d'occupation, rentabilité des salons, tarifs, qualité des choix de la direction) qui conduit à juger les décisions de gestion [S]. Pour le commissaire aux comptes de la SEM, il est exclu : sa mission s'exerce **à l'exclusion de toute immixtion dans la gestion**, et il se prononcerait, pour l'actionnaire majoritaire, sur les choix des dirigeants qu'il contrôle, au risque de son impartialité [V L. 821-54 I ; code de déontologie art. 4-5 ; S, application]. L'agglomération peut le confier à un autre professionnel.
- **Portée de l'opinion pour les élus (0,5 pt)** : la certification couvre les comptes de 2026, au regard du seuil de signification ; elle **ne garantit ni la viabilité ni la qualité de la gestion** et ne porte ni sur l'opportunité d'agrandir le centre de congrès ni sur la rentabilité de chaque salon [V L. 821-55]. Les élus peuvent s'appuyer sur les comptes certifiés pour les données financières, mais non sur l'opinion pour apprécier la gestion.

**Réponses tolérées**
- L'acceptation d'une prestation limitée à des informations financières déterminées (attestation sur des chiffres d'occupation tirés de la comptabilité), si l'absence de jugement sur la gestion est motivée : points complets.
- L'acceptation d'une prestation après analyse des risques (immixtion, autorévision, conflit d'intérêts), limitée à des constats chiffrés sans jugement sur les choix de la direction : points complets.

**Erreurs fréquentes**
- Présenter la certification comme une garantie de bonne gestion (`JUR-A01`).
- Confondre audit légal, audit contractuel et examen de la gestion (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53, L. 821-55 ; NEP principes § 01, § 08-09 | Objectif, assurance raisonnable, limites | [V] | F11 § 1.1 |
| C. com. L. 821-2 IV, L. 821-54 I ; A. 821-55 § 08 ; R. 821-195 | Prestation ; audit contractuel ; non-immixtion ; lettre de mission | [V] ; qualification : [S] | F11 § 1.2, § 13.2 ; F09 § 6 |

### 3.5 Cycle litiges et provisions, extrait de la norme et procédures (5,5 pts)

**a. Risque d'anomalies significatives et assertions (2,5 pts)**
- **Risque inhérent élevé (0,5 pt)** : provisions qui reposent sur des **estimations** et sur l'issue incertaine de procédures ; enjeux élevés au regard du seuil (640 000 € réclamés par KERLÉVEN, plus de cinq fois les 120 000 € du seuil) ; dirigeant qui juge seul de l'issue (« la clause nous protège », « sa faute est évidente », « elle paiera ») ; incidents techniques en série (panne de climatisation, infiltrations), honoraires d'avocats multipliés par quatre (74 000 € contre 18 000 €), litige KERVÉNOC dont la provision de 2025 s'est révélée insuffisante en appel ; résultat modeste (186 000 €), qu'une provision supplémentaire suffirait à rendre négatif [V NEP risques § 02 ; S, application].
- **Risque lié au contrôle élevé (0,5 pt)** : aucun registre des réclamations ; état des litiges établi d'après les seules informations du directeur général ; provisions estimées sans procédure écrite ni consultation des avocats ; conseil d'administration non informé. Le cabinet ne peut pas s'appuyer sur ces contrôles : **procédures de substance étendues** [V NEP principes § 11, § 13].
- **Principaux risques et assertions (1,5 pt ; 0,25 pt par dossier rattaché à la bonne assertion, et 0,25 pt pour l'information de l'annexe, dans la limite de 1,5 pt)** :

| Dossier | Risque | Assertions |
|---|---|---|
| 1. KERLÉVEN | Provision limitée au plafond contractuel alors que la clause peut être écartée et que la réclamation est de 640 000 € | Provision : **évaluation** |
| 2. Prud'hommes | Litige ni provisionné ni mentionné | Provisions : **exhaustivité** ; annexe : **exhaustivité** (passif éventuel) |
| 3. TOITURES KERVAZIC | Produit à recevoir sur un recours contesté, soumis à expertise : créance non acquise | Créance : **existence**, **droits et obligations** ; produit : **réalité** |
| 4. Cotisations | Redressement notifié non provisionné au motif d'une contestation | Provisions : **exhaustivité**, **évaluation** |
| 5. KERVÉNOC | Reprise de la provision et charge de 330 000 € mal classées ou mal rattachées à 2026 | Charges : **mesure**, **classification**, **séparation des exercices** |
| Annexe | Description incomplète des litiges, du recours et de leurs incertitudes | **Exhaustivité**, **présentation et intelligibilité**, **mesure et évaluation** |

**b. Application de l'extrait de la norme (1,5 pt)**
- **Identification (0,5 pt)** : la norme impose d'abord d'**identifier** les litiges susceptibles d'engendrer un risque d'anomalies significatives [V NEP applications spécifiques § 7 al. 1]. L'état de la direction n'est pas exhaustif par construction (aucun registre) : le cabinet le complète par la lecture des procès-verbaux, des comptes d'honoraires d'avocats et des courriers (question 3.5 c). Les dossiers 1 à 4 présentent un risque : montants supérieurs au seuil de signification (dossiers 1 et 3) ou au seuil de planification de 84 000 € (dossier 2), ou cumulés avec les autres (dossier 4, 58 000 €). Le dossier 5, dénoué par un arrêt et payé en 2026, relève d'un simple contrôle de pièces.
- **Circuit et contenu (0,5 pt)** : le cabinet **demande à la direction d'obtenir de ses avocats** des informations sur ces litiges et de **les lui communiquer** [V § 7 al. 2] ; en pratique, la direction signe une lettre rédigée avec le cabinet et demande la réponse directement à celui-ci. La lettre porte sur l'état de chaque procédure, l'appréciation de son issue probable, le montant de la condamnation ou du recouvrement possible, les autres litiges connus de l'avocat et les honoraires restant dus [S, contenu d'usage].
- **Usage des réponses (0,5 pt)** : les réponses sont des éléments **externes**, à rapprocher de l'assignation, du jugement, de la lettre d'observations et des estimations de la direction ; elles fondent la conclusion sur le caractère **probable** de la sortie de ressources, la **meilleure estimation** et l'information de l'annexe, sans dispenser des autres procédures [V § 2 ; NEP éléments probants § 6 ; S, application]. Un refus de la direction a des conséquences sur le rapport (question 3.6) [V § 8].

**c. Autres procédures (1,5 pt ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 1,5 pt)**
- **Lecture des procès-verbaux** du conseil d'administration de 2026 et de 2027 (« difficultés techniques au hall B ») : exhaustivité des litiges.
- **Analyse du compte 6226** et des factures d'honoraires d'avocats, et identification des trois cabinets : exhaustivité des litiges, avocats à interroger.
- **Inspection des assignations, de la lettre d'observations, du contrat de location des halls et du contrat de travaux** de la toiture : réalité des réclamations, évaluation (clause limitative, montants).
- **Entretiens** avec le directeur général, la directrice administrative et financière et le service commercial (réclamations reçues par courriel) : exhaustivité, compréhension des estimations.
- **Revue des courriels de réclamation** reçus par le service commercial, notamment autour du salon annulé : exhaustivité (exposants mécontents, autres organisateurs).
- **Contrôle du dénouement** du litige KERVÉNOC (arrêt, paiement du 30/11/2026, reprise de la provision) : mesure, classification.
- **Revue des événements postérieurs à la clôture** (jugements, décisions de la commission de recours amiable, expertise judiciaire) jusqu'à une date proche de la signature du rapport : évaluation, exhaustivité [V NEP événements postérieurs § 06-07].
- **Déclaration écrite** de la direction sur l'exhaustivité des litiges communiqués : exhaustivité [V NEP déclarations § 6].
- **Lecture de l'annexe** (provisions, passifs éventuels, recours) : présentation.

**Réponses tolérées**
- En a., le classement du dossier 2 en passif éventuel, à mentionner dans l'annexe, si la probabilité de condamnation est discutée.
- En b., l'inclusion du dossier 5 dans la demande aux avocats (confirmation de la clôture du dossier et des honoraires dus) : points complets.

**Erreurs fréquentes**
- Recopier l'extrait de norme sans l'appliquer aux dossiers de la SEM (`JUR-A06`).
- Confondre existence (solde) et réalité (flux) pour le produit à recevoir (`JUR-A01`).
- Proposer des procédures sans objectif ni assertion (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 11-13 ; NEP risques § 02 | Risque inhérent, risque lié au contrôle ; facteurs | [V] ; application : [S] | F11 § 4.1 |
| NEP éléments probants § 6, § 9-10 | Fiabilité des éléments externes ; assertions ; techniques | [V] | F11 § 4.3, § 6.1-6.2 |
| NEP applications spécifiques § 1, 2, 7, 8 | Identification des litiges ; demande aux avocats par la direction ; refus | [V] | F11 § 12.4, § 22 |
| NEP événements postérieurs § 06-07 ; NEP déclarations § 6 | Identification des événements postérieurs ; déclaration écrite | [V] | F11 § 12.1, § 12.3 |
| PCG 211-1, 321-1, 322-2, 322-5, 323-2, 513-3 | Actif ; passif ; provision ; passif éventuel ; meilleure estimation ; bénéfices réalisés | [V] (règles données en annexe) | F11 § 12.5, § 20.2 |

### 3.6 Refus du directeur général (2 pts)

- **Droit de communication (0,5 pt)** : le cabinet opère à toute époque les vérifications qu'il juge opportunes et se fait communiquer **sur place toutes les pièces qu'il estime utiles** [V L. 821-60]. Les courriers échangés avec les avocats et leurs factures d'honoraires, détenus par la SEM, en font partie : c'est le cabinet, non le directeur général, qui en apprécie l'utilité.
- **Secret (0,5 pt)** : le secret professionnel ne peut être opposé au commissaire aux comptes, **sauf par les auxiliaires de justice** [V L. 821-61 al. 3]. La SEM n'est pas un auxiliaire de justice : elle ne peut opposer ce secret pour refuser des documents qu'elle détient. Me TANGUY, avocate, peut en revanche opposer son secret à une demande directe du cabinet [S, qualification de l'avocat]. C'est pourquoi la norme fait passer la demande **par la direction**, qui interroge ses avocats et communique leurs réponses [V NEP applications spécifiques § 7]. Le cabinet n'a pas à « contacter » l'avocate contre la volonté de la SEM, mais le directeur général ne peut pas refuser de l'interroger sans conséquence. Le cabinet est lui-même tenu au secret [V L. 821-35 al. 1].
- **Conséquences d'un refus maintenu (1 pt)** :
  - **sur l'opinion (0,5 pt)** : sans réponse des avocats, le cabinet ne peut pas apprécier l'issue probable ni le montant des dossiers 1 à 4 ; il en tire les conséquences dans son rapport [V § 8]. C'est une **limitation** : **certification avec réserve pour limitation** si ses incidences sont circonscrites et la réserve suffisante, **impossibilité de certifier** sinon [V NEP rapport § 11, § 14]. Avec des réclamations qui dépassent plusieurs fois le seuil et un résultat de 186 000 €, l'impossibilité est à envisager si aucune procédure alternative (jugement, pièces de procédure) ne permet de conclure [S] ;
  - **pénal et communication (0,5 pt)** : refuser la communication sur place des pièces utiles (courriers, factures) ou faire obstacle aux vérifications est un **délit** pour le dirigeant (cinq ans, 75 000 €) [V L. 821-6 3°]. Le cabinet porte le refus à la connaissance du **conseil d'administration**, parmi les irrégularités relevées, avant de conclure [V L. 821-63 I 5° ; S, application]. Une démission pour échapper à l'émission de l'opinion est exclue [V code de déontologie art. 28].

**Réponses tolérées**
- La qualification de « limitation imposée par la direction » avec une impossibilité de certifier présentée comme conclusion probable, si le caractère non circonscrit est motivé : points complets.

**Erreurs fréquentes**
- Admettre que l'entité peut opposer au commissaire aux comptes le secret de ses avocats, ou affirmer à l'inverse que l'avocat ne peut jamais l'opposer (`JUR-A01`).
- Conclure à un refus de certifier, qui sanctionne un désaccord, pour une limitation (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-60, L. 821-61 al. 3, L. 821-35 al. 1, L. 821-6 3°, L. 821-63 I | Communication ; secret des auxiliaires de justice ; obstacle ; communication au conseil | [V] ; qualification de l'avocat : [S] | F09 § 5 ; F11 § 2, § 13.3, § 22 |
| NEP applications spécifiques § 7-8 ; NEP rapport § 11, § 14 ; code de déontologie art. 28 | Circuit de la demande ; refus ; limitation ; démission | [V] | F11 § 8.1, § 22 ; F09 § 3.7 |

### 3.7 Événements postérieurs, écriture et opinion (2 pts)

**Traitement des deux événements (0,5 pt)**
- **Jugement KERLÉVEN (0,25 pt)** : le jugement du 16/02/2027, antérieur à l'arrêté des comptes du 18/03/2027, **éclaire une situation qui existait à la clôture** (la panne et l'obligation d'indemniser sont de juin 2026). Il doit être pris en compte : la provision est la **meilleure estimation** à la date d'établissement des comptes [V PCG 322-2, 323-2, 323-10 ; NEP événements postérieurs § 02, § 08]. Selon l'avocate, un appel aurait peu de chances d'aboutir : la meilleure estimation est le montant du jugement, 395 000 + 15 000 = **410 000 €**. L'intention de faire appel ne justifie pas de maintenir 150 000 €, montant d'une clause écartée par le tribunal.
- **Tempête (0,25 pt)** : les dommages du 13/01/2027 n'ont **pas de lien avec une situation existant à la clôture** (rien ne les laissait prévoir) : aucune provision au 31/12/2026, mais une **information dans l'annexe**, l'événement étant important par sa nature : 210 000 € de réparations (1,75 fois le seuil), dont 150 000 € pris en charge par l'assureur, soit un coût net de 60 000 € (0,50 fois le seuil), et surtout la fermeture jusqu'en mai 2027 du parking qui sert aux deux tiers des visiteurs, qui pèsera sur l'activité de 2027, et une mention dans le rapport de gestion [V PCG 831-1 4° ; NEP événements postérieurs § 02-03, § 10].

**Écriture de correction au 31/12/2026 (0,5 pt)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 6815 | Dotations aux provisions d'exploitation | 260 000 | |
| | 1511 | Provisions pour litiges | | 260 000 |

Libellé : ajustement de la provision pour le litige KERLÉVEN au montant du jugement du 16/02/2027 (410 000 − 150 000) (écriture X1, équilibrée). La provision s'élève à 410 000 € ; le résultat corrigé, avant effet d'impôt, est de 186 000 − 260 000 = **− 74 000 €** (perte) et les capitaux propres de 2 940 000 − 260 000 = 2 680 000 €.

**Caractère significatif (0,25 pt)** : 260 000 / 120 000 = **2,17 fois** le seuil de signification ; l'anomalie transforme en outre un bénéfice en perte, ce qui la rend significative par sa **nature** [V NEP caractère significatif § 9 ; NEP anomalies § 14]. L'absence d'information sur la tempête est une **omission** dans l'annexe, significative par sa **nature** (fermeture pendant quatre mois du parking principal, réparations de 210 000 €), bien que son coût net d'assurance (60 000 €) reste sous le seuil. Les 9 000 € des autres cycles restent sous le seuil.

**Opinion (0,75 pt)**
- **La SEM corrige (écriture X1 et note sur la tempête) (0,25 pt)** : il ne subsiste que 9 000 € d'anomalies non corrigées, non significatives : **certification sans réserve**. Le cabinet les communique au conseil d'administration et obtient une déclaration écrite à laquelle est joint l'état des anomalies non corrigées [V NEP anomalies § 15-17 ; NEP rapport § 08].
- **La SEM retient la position du directeur général (0,25 pt)** : deux anomalies significatives non corrigées (269 000 € avec les autres cycles, soit 2,24 fois le seuil, et l'omission de l'annexe). Leurs incidences sont **clairement circonscrites** : un montant identifié sur une provision, une information précise à donner ; une réserve qui quantifie la provision manquante et décrit l'événement permet au lecteur de corriger lui-même le résultat : **certification avec réserve pour désaccord**, motivée par les deux points [V NEP rapport § 09-10]. Le passage d'un bénéfice à une perte renforce le caractère significatif, sans empêcher de circonscrire l'incidence [S].
- **Parties du rapport (0,25 pt)** : la partie « **Opinion avec réserve** » indique que, sous ces réserves, les comptes sont réguliers et sincères et donnent une image fidèle ; la partie « **Fondement de l'opinion avec réserve** » expose les motifs et quantifie leur incidence (provision et résultat surévalué de 260 000 €, résultat qui serait, avant effet d'impôt, une perte de 74 000 € ; absence d'information sur la tempête). Les motifs sont communiqués au préalable au conseil d'administration ; le rapport est destiné à l'assemblée générale [V NEP rapport § 06, § 18 ; R. 821-180].

**Réponses tolérées**
- Un refus de certifier dans le second cas, s'il est motivé par l'insuffisance d'une réserve pour un lecteur qui croirait la SEM bénéficiaire : 0,25 pt sur 0,5 pour l'opinion et les parties du rapport.
- Une omission de l'information sur la tempête jugée non significative au motif que son coût net d'assurance (60 000 €) reste sous le seuil, si ce motif est exposé : points complets en caractère significatif ; une réserve fondée sur la seule provision KERLÉVEN reçoit alors les points de l'opinion et des parties du rapport.
- Le classement de la condamnation en dette (charges à payer) plutôt qu'en provision, si le candidat retient que le montant est fixé par le jugement : points complets pour l'écriture si le compte et le montant de 260 000 € sont cohérents.

**Erreurs fréquentes**
- Provisionner la tempête au 31/12/2026, ou ne retenir aucun traitement de cet événement (`JUR-A06`).
- Écriture sans libellé ou sans numéro de compte (`JUR-F03`).
- Opinion sans motif ni partie du rapport (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG 322-2, 323-2, 323-10, 831-1 4° ; C. com. L. 123-20 | Passif à la date d'établissement ; meilleure estimation ; événement sans lien | [V] | F11 § 12.5 |
| NEP événements postérieurs § 02-03, § 08-10 | Traitement comptable ou information ; demande de modification | [V] | F11 § 12.1 |
| NEP caractère significatif § 9 ; NEP anomalies § 14-17 ; NEP rapport § 06, § 08-10, § 18 ; R. 821-180 | Montant et nature ; communication ; opinions ; parties du rapport | [V] | F11 § 4.2, § 8, § 14.1 |

### 3.8 Responsabilités envers la banque (2,5 pts)

**Responsabilité civile (1,5 pt)**
- **Principe (0,25 pt)** : le commissaire aux comptes est responsable, envers l'entité **et les tiers**, des conséquences dommageables des **fautes et négligences** commises dans l'exercice de sa profession [V L. 821-37 al. 1]. La banque, tiers, doit prouver une **faute**, un **préjudice** et un **lien de causalité** [S].
- **Faute (0,5 pt)** : la certification est une **obligation de moyens**, fondée sur une assurance raisonnable sur les comptes pris dans leur ensemble [V NEP principes § 08-09]. Pour 2025, le cabinet avait appliqué la norme : demande d'informations à l'avocat par l'intermédiaire de la direction, réponse reçue directement, rapprochement avec le jugement et l'assignation, déclaration écrite [V NEP applications spécifiques § 7]. La provision de 80 000 € était la meilleure estimation **à la date d'établissement des comptes de 2025** : elle reprenait le jugement de première instance, que l'avocat jugeait très probablement confirmé [V PCG 323-2, 323-10]. L'écart de 250 000 € (2,27 fois le seuil de 2025 de 110 000 €) n'est apparu qu'avec l'arrêt du 08/10/2026, postérieur au rapport : ce n'est pas une anomalie des comptes de 2025 au sens des textes, et le cabinet ne pouvait pas le prévoir. Aucune faute n'est caractérisée [S, application].
- **Préjudice et lien de causalité (0,5 pt)** : la SEM a payé les quatre échéances de 2026 à bonne date ; la banque ne subit aucune perte, et l'absence de garantie de l'agglomération n'est pas un dommage tant que le prêt est remboursé. Elle avait accordé le prêt au vu de l'ensemble de la situation de la SEM et de son projet : rien n'établit qu'une provision plus élevée l'aurait conduite à refuser le prêt ou à exiger une garantie. La demande n'est pas fondée [S].
- **Couverture (0,25 pt)** : le cabinet est couvert par l'assurance obligatoire de sa responsabilité civile [V R. 821-85, R. 821-109]. Il conserve dans son dossier de travail les éléments qui établissent ses diligences.

**Responsabilité pénale (0,5 pt)** : le délit invoqué est celui du commissaire aux comptes qui **donne ou confirme des informations mensongères** sur la situation de la personne morale (cinq ans, 75 000 €) [V L. 821-9]. C'est un délit **intentionnel** : il suppose que le commissaire aux comptes ait su que les comptes étaient inexacts [S, F09 § 7.3]. Mme GUÉGAN a certifié une provision fondée sur le jugement et sur l'avis de l'avocat : aucune connaissance d'une inexactitude, donc aucun délit.

**Responsabilité disciplinaire (0,5 pt)** : la H2A sanctionne les manquements aux conditions légales d'exercice, la **négligence grave** et les faits contraires à la probité ou à l'honneur, de l'avertissement à la radiation, avec d'éventuelles sanctions pécuniaires ; cette responsabilité est indépendante des actions civile et pénale [V L. 821-70 I, L. 821-71]. Des diligences conformes à la norme sur un litige dont l'issue a changé en appel ne constituent pas une négligence grave : le signalement de la banque ne devrait pas conduire à une sanction [S].

**Réponses tolérées**
- Une analyse en termes de responsabilité délictuelle de droit commun envers le tiers, si les trois conditions sont examinées.
- La mention de la responsabilité personnelle de Mme GUÉGAN aux côtés de celle de la société de commissaires aux comptes, sans développement.

**Erreurs fréquentes**
- Juger la provision de 2025 avec les informations de 2026, ou présenter la certification comme une obligation de résultat (`JUR-A05`).
- Confondre les trois responsabilités et leurs sanctions, ou développer la procédure de mise en cause, hors programme (`JUR-A01`, `JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-37 ; R. 821-85, R. 821-109 ; NEP principes § 08-09 ; NEP applications spécifiques § 7 | Responsabilité civile ; assurance ; obligation de moyens ; diligences sur les litiges | [V] ; conditions : [S] | F09 § 7.1, § 13 ; F11 § 1.1, § 22 |
| PCG 323-2, 323-10 | Meilleure estimation à la date d'établissement des comptes | [V] | F11 § 12.5 |
| C. com. L. 821-9, L. 821-70 I, L. 821-71 | Informations mensongères ; faute disciplinaire ; sanctions | [V] ; élément intentionnel : [S] | F09 § 7.2-7.3 |

---

### Partie B – Durabilité (12 points)

### 3.9 Architecture des ESRS et proposition de M. LE FLOCH (2,5 pts)

- **Architecture (1 pt)** : les ESRS, adoptées par la Commission sur avis technique de l'EFRAG, comprennent des **normes transversales**, ESRS 1 (exigences générales) et ESRS 2 (informations générales à publier), appliquées conjointement avec des **normes thématiques** : cinq pour l'environnement (dont le changement climatique, la pollution, l'eau, la biodiversité, les ressources et l'économie circulaire), quatre pour le social (personnel de l'entreprise, travailleurs de la chaîne de valeur, communautés affectées, consommateurs et utilisateurs finaux) et une pour la gouvernance (conduite des affaires) [V ESRS 1 (2026) § 7-10 ; règl. délégué 2026/1563 consid. 3 ; ESRS (2023) : mêmes catégories, sous d'autres intitulés]. L'état de durabilité est présenté en quatre parties : informations générales, environnementales, sociales et de gouvernance [V ESRS 1 (2026) § 105], comme le sommaire de la SEM.
- **Étendue et limites (0,75 pt)** : les **informations générales** d'ESRS 2 sont publiées quel que soit le résultat de l'analyse de double matérialité ; pour chaque thème **matériel**, l'entreprise publie ses politiques, actions, indicateurs et cibles, ou signale qu'elle n'en a pas défini, ainsi que les exigences des normes thématiques pertinentes [V ESRS 1 (2026) § 25, § 29 ; ESRS 2 § 38-39]. Elle ne publie pas les informations d'une exigence sans importance matérielle, sauf informations supplémentaires signalées comme ne résultant pas de l'analyse de matérialité [V § 24, § 107-109]. L'état, pris comme un tout, donne une **image fidèle** de tous les impacts, risques et opportunités matériels [V § 3].
- **Réponse à M. LE FLOCH (0,75 pt)** : la SEM a retenu comme matériels l'énergie et le climat, mais aussi les déchets, les déplacements des visiteurs, la santé et la sécurité, la conduite des affaires. Ne publier que sur le climat omettrait des thèmes matériels : l'état ne pourrait plus se déclarer **conforme aux ESRS**, qui ne permettent ni de choisir les thèmes a priori ni de renvoyer les autres sur un site internet sans les intégrer à l'état [V § 3, § 29 ; S, application]. La SEM, qui publie volontairement, peut changer de référentiel, mais elle devrait alors retirer la mention de conformité aux ESRS, et la mission du cabinet, qui porte sur cette conformité, serait à redéfinir [S]. La lourdeur peut être réduite autrement : seules les informations matérielles sont requises, et des estimations sont admises [V § 24, § 64-65].

**Réponses tolérées**
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences », « déclaration relative à la durabilité ») et leurs intitulés de normes.
- La mention de la norme volontaire pour les PME comme autre référentiel possible, sans développement : points complets si la perte de la mention de conformité aux ESRS est indiquée.

**Erreurs fréquentes**
- Présenter une troisième catégorie de normes, propres à chaque secteur, comme en vigueur, ou détailler le contenu d'une norme thématique (`JUR-F01`).
- Admettre qu'un état limité au climat reste conforme aux ESRS (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 3, § 7-10, § 24-25, § 29, § 64-65, § 105, § 107-109 ; ESRS 2 § 38-39 | Architecture ; image fidèle ; thèmes matériels ; informations supplémentaires ; structure | [V] ; application : [S] | F12 § 3, § 5, § 8, § 14, § 17 |
| Règl. délégué 2026/1563 consid. 3 | EFRAG, adoption par la Commission | [V] | F12 § 1 |

### 3.10 Périmètre de reporting (3,5 pts)

**Règles (1,5 pt)**
- **Entreprise déclarante (0,25 pt)** : l'état de durabilité porte sur la **même entreprise déclarante que les états financiers** ; pour la SEM, sans filiale, ce sont ses propres activités, telles qu'elles figurent dans ses comptes [V ESRS 1 (2026) § 60-61].
- **Actifs exploités sans être détenus (0,5 pt)** : pour un actif loué, le **preneur**, qui l'utilise, déclare dans ses **propres activités** les impacts de cette utilisation (par exemple l'énergie consommée ou la pollution d'une usine louée) ; le bailleur les déclare dans sa chaîne de valeur aval ; l'imputation des autres impacts et des risques dépend des clauses du contrat [V ESRS 1 (2026) § 71, § 73, AR 39]. La **propriété** n'est donc pas le critère.
- **Contrôle opérationnel (0,25 pt)** : c'est la possibilité de diriger les activités opérationnelles et les relations d'une entité, d'un site, d'une activité ou d'un actif [V ESRS (2023), annexe II]. Il rattache aux activités propres un site que l'entreprise exploite sans le posséder [S, synthèse de F12 § 7].
- **Chaîne de valeur (0,5 pt)** : l'information couvre la chaîne de valeur **amont et aval** dans la mesure nécessaire à la compréhension des impacts, risques et opportunités matériels, au moyen de données collectées auprès des contreparties ou d'**estimations** (moyennes sectorielles, données indirectes) ; seules les informations matérielles sont attendues, pas chaque acteur [V ESRS 1 (2026) § 62-65].

**Appréciation du périmètre de la direction (2 pts)**
- **Énergie (0,75 pt)** : la SEM exploite les halls, le centre de congrès et les parkings pendant dix ans, contre une redevance ; elle souscrit en son nom les contrats d'électricité et de gaz, et décide des événements, des horaires et de la climatisation : elle les utilise comme un preneur et en a le **contrôle opérationnel**. L'énergie qu'elle y consomme relève de ses **propres activités** [V § 71, AR 39 ; S, qualification du contrat]. En ne retenant que les bureaux et l'atelier (185 MWh sur 4 600 MWh d'électricité et de gaz facturés, soit 4,0 %), le projet omet 96,0 % de l'électricité et du gaz consommés et affiche une baisse de 9 % alors que la consommation facturée a augmenté de 6 % : l'information n'est ni complète ni neutre [V ESRS 1 (2026) § 19-20 ; S, application]. Seuls les impacts liés à la propriété (travaux de structure et d'isolation, à la charge de l'agglomération) relèvent, selon le contrat, de l'agglomération ; la SEM peut le décrire [V § 71].
- **Déchets (0,75 pt)** : les 362 tonnes collectées après les événements (86,6 % des 418 tonnes) sont produites **sur un site que la SEM exploite**, pendant des événements qu'elle organise ou accueille, et collectées par le prestataire avec lequel elle a contracté, au vu de bordereaux à son nom ; le règlement des salons interdit aux exposants de les évacuer et les organisateurs lui payent un forfait de collecte. Elle a le contrôle opérationnel de leur gestion : ces déchets relèvent de ses propres activités, quel que soit l'auteur matériel de la production [S, application de § 60-61 et du contrôle opérationnel]. Les déchets que les exposants remporteraient, ou ceux produits par les activités des organisateurs hors du site, relèveraient de la chaîne de valeur aval.
- **Déplacements des visiteurs et des exposants (0,5 pt)** : ils ne sont pas des activités propres, mais ils sont **directement liés** à l'activité de la SEM, qui attire 310 000 visiteurs et 2 900 exposants : c'est la **chaîne de valeur aval** (clients et usagers). L'analyse de la direction les a jugés matériels : ils doivent être décrits, au besoin par **estimation** à partir des codes postaux de la billetterie et de l'enquête de 2025 [V § 62-65 ; S, application]. Le projet ne peut pas les écarter au motif qu'ils « ne relèvent pas de l'activité » de la SEM.

**Réponses tolérées**
- Le raisonnement fondé sur le seul contrôle opérationnel, sans la règle des actifs loués, ou l'inverse, si la conclusion est motivée par les clauses du contrat : points complets en énergie.
- Le rattachement d'une partie des déchets à la chaîne de valeur aval, si le candidat distingue les déchets collectés par la SEM sur son site de ceux que les exposants remportent.

**Erreurs fréquentes**
- Retenir la propriété des bâtiments comme critère du périmètre (`JUR-A01`).
- Calculer des émissions ou proposer des indicateurs et des cibles, ce qui n'est pas demandé (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 19-20, § 60-65, § 71, § 73, AR 39 | Entreprise déclarante ; chaîne de valeur ; estimations ; actifs loués ; représentation fidèle | [V] ; application : [S] | F12 § 7, § 14, § 16, § 17 |
| ESRS (2023), annexe II | Contrôle opérationnel | [V] | F12 § 7 |

### 3.11 Mission du cabinet et procédures (4,5 pts)

**a. Objectifs, assurance et axes (2,5 pts)**
- **Objectifs (0,75 pt)** : le cabinet émet un **avis** sur la conformité aux ESRS du **processus** mis en œuvre pour déterminer les informations publiées (analyse de double matérialité) et sur la conformité des **informations** publiées [V L. 821-54 II ; LD 2026 § 2]. La mission est volontaire, conduite dans les conditions de la certification légale (hypothèse), confiée pour trois exercices ; le rapport est destiné à l'assemblée générale. Elle ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55]. Elle est distincte de la certification des comptes, avec laquelle elle échange des informations (cohérence des factures d'énergie, de la redevance et des charges de collecte avec la comptabilité) [V LD 2026 § 3.2].
- **Assurance limitée (0,5 pt)** : vérifications moindres en **nature, étendue et durée** que pour une assurance raisonnable ; conclusion sous une **forme négative** : le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes [V LD 2026, « Niveau d'assurance »]. La certification des comptes repose, elle, sur une assurance raisonnable, exprimée sous une forme positive [V NEP principes § 08].
- **Axes (0,75 pt)** : **axe 1**, le processus de détermination des informations, et **axe 2**, les informations publiées, y compris le **périmètre** et les informations sur la **chaîne de valeur** [V LD 2026 § 2, § 8.1]. L'axe relatif à la **taxonomie** est **sans objet** : il ne vise que les entreprises soumises à l'obligation de publier [V L. 821-54 II ; S, application]. L'axe relatif au **balisage** n'est pas exigible tant que les règles de balisage ne sont pas adoptées [V LD 2026 § 2, § 10].
- **Consultation du CSE (0,5 pt)** : pour une entité soumise, l'axe 1 comprend la vérification de la consultation du CSE sur ces informations [V L. 821-54 II 2° ; LD 2026 § 7.3]. Pour la SEM, qui publie volontairement, cette consultation n'est pas une obligation légale ; la lettre de mission ne la vise pas : le cabinet ne la vérifie pas, et son rapport ne s'en prononce pas [V F12 § 11 (b) ; S, application].

**b. Procédures sur le périmètre et les données (2 pts ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 2 pts)**
- **Prise de connaissance du contrat d'exploitation** (objet, durée, contrats souscrits au nom de la SEM, répartition des travaux) : qualifier l'utilisation des bâtiments et la répartition des impacts avec l'agglomération.
- **Lecture de la base de préparation** du projet : vérifier que le périmètre retenu et ce qui est couvert dans la chaîne de valeur sont décrits, et qu'ils sont conformes aux ESRS [V LD 2026 § 8.1].
- **Rapprochement des consommations publiées avec les factures d'électricité et de gaz** au nom de la SEM, compteur par compteur : exhaustivité des données d'énergie, mesure de la part exclue.
- **Rapprochement des tonnages avec les bordereaux de suivi** et le contrat du prestataire de collecte : exhaustivité des déchets, origine (halls et centre de congrès, bureaux).
- **Lecture du règlement des salons et des contrats de location** (forfait de collecte, interdiction d'évacuation) : rattachement des déchets à la SEM.
- **Procédures analytiques** : évolution de l'énergie facturée (+ 6 %) au regard de l'affirmation d'une baisse de 9 %, des jours d'occupation et des fortes chaleurs : cohérence et neutralité de l'information [V LD 2026 § 8.3.2].
- **Entretiens** avec la directrice administrative et financière et le responsable technique : compréhension des compteurs, du sous-compteur et des méthodes.
- **Revue des estimations** sur les déplacements (codes postaux de la billetterie, enquête de 2025 : représentativité, hypothèses publiées) : caractère raisonnable et explication des estimations [V ESRS 1 (2026) § 64-65, § 88].
- **Échanges avec l'équipe chargée de la certification des comptes** : cohérence avec les charges d'énergie et de collecte comptabilisées [V LD 2026 § 3.2].
- **Lettre d'affirmation** de la direction et **communication** des anomalies au conseil d'administration [V LD 2026 § 4, § 14].

**Réponses tolérées**
- En a., la mention de la vérification du processus comme achevée et sans anomalie (annexe 3.10), sans développement.

**Erreurs fréquentes**
- Retenir l'axe relatif à la taxonomie, ou la consultation du CSE comme obligation légale de la SEM (`JUR-A05`).
- Présenter l'assurance limitée comme une garantie de conformité (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; LD 2026 § 2, § 10, « Niveau d'assurance » | Objectifs, axes, assurance limitée | [V] ; application à une mission volontaire : [S] | F13 § 2 ; F12 § 11 |
| LD 2026 § 3.2, § 4, § 7.3, § 8.1, § 8.3.2, § 14 | Échanges avec la certification des comptes ; CSE ; périmètre ; techniques ; communication | [V] ; procédures : [S] | F13 § 3, § 7, § 8 |
| ESRS 1 (2026) § 64-65, § 88 | Estimations ; jugements et incertitudes | [V] | F12 § 7, § 14 |

### 3.12 Avis sur les informations publiées (1,5 pt)

- **La direction rétablit les données (0,5 pt)** : énergie des halls et du centre de congrès, déchets des événements et description estimée des déplacements, avec ses hypothèses ; aucune autre erreur n'est relevée : **avis de conformité** sur les informations [V LD 2026 § 17]. Le cabinet peut formuler une **observation** renvoyant à l'explication des estimations relatives aux déplacements, ou présenter le périmètre parmi les éléments ayant fait l'objet d'une attention particulière [V LD 2026 § 17 ; F13 § 4.4].
- **La direction maintient son projet (0,75 pt)** : l'omission de 96,0 % de l'électricité et du gaz et de 86,6 % des déchets, et l'absence des déplacements, portent sur trois des thèmes matériels identifiés par la SEM elle-même, et l'affirmation d'une baisse de 9 % de la consommation donne une image trompeuse de l'évolution réelle (+ 6 %). Ce sont des omissions et des incohérences non corrigées d'une importance telle qu'elles remettent en cause la conformité des informations. Leurs incidences ne sont **pas circonscrites** : elles privent de sens l'essentiel de la partie environnementale, et une réserve ne suffirait pas au lecteur : **avis de non-conformité, motivé** [V F13 § 4.2-4.3 ; S, qualification]. Ce n'est pas une impossibilité d'émettre un avis : aucune limitation n'a empêché les vérifications.
- **Portée (0,25 pt)** : l'avis est émis **axe par axe** : l'avis de conformité sur le processus (annexe 3.10) n'est pas affecté, la direction ayant bien identifié ces thèmes comme matériels ; le rapport comporte une partie par axe, et ne se prononce ni sur la taxonomie ni sur le balisage [V LD 2026 § 17 ; S, déduction de la structure par axe]. L'avis reste une conclusion d'assurance limitée.

**Réponses tolérées**
- Un avis de conformité assorti d'une réserve motivée dans le second cas, si le candidat circonscrit les omissions à des données identifiées et chiffrées par la réserve : 0,5 pt sur 0,75.

**Erreurs fréquentes**
- Conclure à une impossibilité d'émettre un avis en l'absence de limitation, ou remplacer la réserve ou la non-conformité par une observation (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 | Avis, réserve, non-conformité, observations, éléments d'attention particulière, structure par axe | [V] ; qualification : [S] | F13 § 4.1-4.4 |
