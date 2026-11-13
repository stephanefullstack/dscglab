# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 12

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 12/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex31_consolidation_anc_conversion_couts_emprunt` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.6 | `exercices/ex32_fusion_detention_prealable_mali` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.10 | `exercices/ex33_audit_ventes_petit_groupe_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Référentiel et option pour les IFRS | `2.1.b` Contexte réglementaire et légal de la consolidation | 1 |
| 1.2 Cadre conceptuel de l'IASB, coûts d'emprunt et écart d'acquisition | `2.1.a` Cadre conceptuel de l'IASB ; `2.1.d` Conséquences du référentiel | 2,5 |
| 1.3 Processus de consolidation et place de la conversion | `2.2.a` Processus d'élaboration d'une consolidation | 2,5 |
| 1.4 Périmètre et méthodes | `2.1.c` Périmètre ; `2.1.d` Conséquences du référentiel et des méthodes | 3 |
| 1.5 a Méthode de conversion | `2.2.e` Conversion des comptes établis en devises | 1,5 |
| 1.5 b Conversion du bilan et du compte de résultat | `2.2.e` Conversion des comptes établis en devises | 2 |
| 1.5 c Analyse de l'écart de conversion de 2026 | `2.2.e` Conversion des comptes établis en devises | 1,5 |
| 1.5 d Partage de l'écart de conversion | `2.2.e` Conversion ; `2.2.h` Partage des capitaux propres | 1 |
| 1.6 Coûts d'emprunt de la centrale d'ENROBÉS DU VIAUR | `2.2.c` Homogénéisation, thèmes communs | 5 |
| 1.7 a Ventes de granulats et marge interne | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.7 b Comptes réciproques et avoir non enregistré | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.7 c Dividende d'ESCALDÈRE MAROC | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.8 a Actif net réévalué de GRANULATS DU LÉVÉZOU | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.8 b Coût d'acquisition et écart d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 2 |
| 1.8 c Durée d'utilisation de l'écart et écritures | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.9 a Partage des capitaux propres des trois filiales | `2.2.h` Partage des capitaux propres | 3 |
| 1.9 b Mise en équivalence de LIANTS D'OLT | `2.2.h` Partage des capitaux propres | 1,5 |
| 1.9 c Écritures d'élimination des titres et de mise en équivalence | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.10 a Extrait du bilan consolidé | `2.3.a` Documents de synthèse consolidés | 5 |
| 1.10 b Annexe consolidée et différence avec IAS 1 | `2.3.a` Documents de synthèse consolidés ; `2.1.d` Conséquences du référentiel | 2 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires ; `ECV` = écart de conversion de l'entité avant partage ; `ECV_G` / `ECV_M` = écarts de conversion, part du groupe / part des minoritaires (cette dernière est présentée dans les intérêts minoritaires) ; `EA` = écart d'acquisition ; `AMO_EA` = amortissements de l'écart d'acquisition ; `DOT_EA` = ligne « dotations aux amortissements et dépréciations des écarts d'acquisition » du compte de résultat ; `TME` = titres mis en équivalence ; `QP_MEE` = résultat net lié aux entités mises en équivalence ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.ESCALDERE` : titres détenus par la SA ESCALDÈRE ; `RSV.VIAUR` : réserves d'ENROBÉS DU VIAUR).

---

### 1.1 Référentiel et option pour les IFRS (1 pt)

- **Règle (0,5 pt).** Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que pour les sociétés dont des titres sont admis aux négociations sur un marché réglementé d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Les autres sociétés établissent leurs comptes consolidés selon le règlement ANC n° 2020-01, ou **peuvent opter** pour les IFRS adoptées [V C. com. L. 233-24 ; F03 § 1.2].
- **Application (0,5 pt).** Aucun titre de la SA ESCALDÈRE n'est admis aux négociations sur un marché : elle applique le règlement ANC n° 2020-01, et pourrait opter pour les IFRS. La forme de société anonyme à directoire et conseil de surveillance est sans incidence sur ce choix ; l'obligation de consolider elle-même résulte du contrôle exclusif qu'ESCALDÈRE exerce sur trois filiales [V L. 233-16 ; F03 § 1.1] (non noté : la question porte sur le référentiel).

---

### 1.2 Cadre conceptuel de l'IASB, coûts d'emprunt et écart d'acquisition (2,5 pts)

- **Objectif et utilisateurs (0,5 pt).** Le cadre conceptuel énonce les concepts qui guident l'IASB dans l'élaboration des normes et aident à les interpréter ou à définir une méthode lorsqu'aucune norme ne s'applique [V page « Conceptual Framework », ifrs.org ; IAS 8 § 11 ; F03 § 7.2]. L'information financière à usage général doit être **utile aux investisseurs, prêteurs et autres créanciers, actuels et potentiels**, pour leurs décisions relatives à la fourniture de ressources à l'entité [S ; F03 § 7.2]. La famille fondatrice et les membres du conseil de surveillance qui la représentent sont des investisseurs actuels ; la banque qui a évoqué les IFRS et celle qui a financé la centrale sont des prêteurs.
- **Caractéristiques qualitatives (0,5 pt).** Fondamentales : **pertinence** (dont l'importance relative) et **représentation fidèle** ; auxiliaires : **comparabilité**, vérifiabilité, rapidité et compréhensibilité [S ; F03 § 7.2]. Les IFRS limitent les options pour rendre les comptes de groupes différents comparables.
- **Définition d'un actif (0,5 pt).** Ressource contrôlée par l'entité du fait d'événements passés, dont on attend des avantages économiques futurs [V IAS 38 § 8 ; F03 § 9] ; le cadre de 2018 parle d'une ressource économique actuelle contrôlée du fait d'événements passés, c'est-à-dire d'un droit qui a le potentiel de produire des avantages économiques [S ; F03 § 9].
- **Intérêts de la centrale (0,5 pt).** La centrale, construite pendant quinze mois, est un **actif qualifié** : elle exige une longue période de préparation avant de pouvoir être utilisée [V IAS 23 § 5 et 7 ; F04 R6]. En IFRS, les coûts d'emprunt directement attribuables à sa construction sont **obligatoirement** incorporés à son coût [V IAS 23 § 8 ; F04 R6] : ils font partie de ce qu'il a fallu dépenser pour obtenir la ressource dont le groupe attend des avantages, au même titre que les travaux. Le PCG laisse le choix entre les charges et l'incorporation [V PCG art. 213-9, p. 17-18 ; F04 R6 et § 10] ; le manuel retient l'incorporation, si bien que les comptes consolidés en ANC et en IFRS seraient ici identiques (200 000 € incorporés, question 1.6). La différence tient à la contrainte : en IFRS, le groupe ne pourrait pas choisir les charges, ce qui sert la comparabilité.
- **Écart d'acquisition (0,5 pt).** En IFRS, le goodwill n'est **pas amorti** ; sa valeur est examinée chaque année, et à chaque indice de perte de valeur, une perte constatée n'étant jamais reprise [V F05 § 2]. Les comptes consolidés en IFRS ne comporteraient donc pas la dotation de 70 000 € de 2026 (question 1.8 c), alors qu'en ANC la limite légale de l'autorisation d'exploiter impose l'amortissement sur 20 ans. Ils retiendraient en outre un goodwill calculé hors frais d'acquisition, ces frais (120 000 €) allant en charges [V IFRS 3 § 53 ; F05 § 2 et 5] : 6 910 000 – 5 600 000 = 1 310 000 € (goodwill partiel), ou un goodwill complet si les minoritaires étaient évalués à leur juste valeur [V IFRS 3 § 19 ; F05 § 2].

---

### 1.3 Processus de consolidation et place de la conversion (2,5 pts)

**Principe (0,5 pt).** L'intégration globale cumule les comptes des entités consolidées **après retraitements**, puis élimine les opérations internes et partage les capitaux propres et le résultat entre le groupe et les intérêts minoritaires [V ANC art. 221-2, p. 18-19 ; F03 § 3]. Les comptes d'une entité étrangère sont d'abord retraités selon les méthodes du groupe, dans sa monnaie, puis convertis : la conversion porte donc sur des comptes homogènes, et les éliminations et le partage portent sur des montants en euros [S ; F04 R13].

**Phases et opérations du dossier (2 pts : ordre et place de la conversion 1 ; rattachement des opérations 1)**

| Ordre | Phase | Opérations du dossier |
|---|---|---|
| 1 | Périmètre et méthodes, instructions et manuel de consolidation | 1.4 (IG pour trois filiales, MEE pour LIANTS D'OLT) ; choix de méthodes du manuel (annexe 1.3) |
| 2 | Réception des liasses et rapprochement des comptes réciproques | 1.7 b : écart de 30 000 € expliqué par l'avoir non enregistré |
| 3 | Retraitements d'homogénéisation, dans la monnaie de chaque entité | ESCALDÈRE MAROC : retraitements faits en dirhams avant l'envoi de la liasse (annexe 1.4) ; ENROBÉS DU VIAUR : coûts d'emprunt (1.6) ; ENROBÉS DU VIAUR : enregistrement de l'avoir (1.7 b) ; ESCALDÈRE : frais d'acquisition des titres (1.8 c) |
| 4 | Conversion des comptes d'ESCALDÈRE MAROC en euros | 1.5 a à c : cours de clôture, écart de conversion |
| 5 | Évaluation des actifs et passifs identifiables de l'entité acquise | 1.8 a : écarts d'évaluation de GRANULATS DU LÉVÉZOU |
| 6 | Cumul des comptes retraités et convertis des sociétés intégrées globalement | annexe 1.9 + bilan converti d'ESCALDÈRE MAROC |
| 7 | Élimination des opérations internes | 1.7 a (ventes et marge sur stock), 1.7 b (soldes réciproques), 1.7 c (dividende, converti au cours du jour) |
| 8 | Élimination des titres, écart d'acquisition, partage, mise en équivalence | 1.5 d (partage de l'écart de conversion), 1.8 b et c, 1.9 |
| 9 | Bilan, compte de résultat et annexe consolidés | 1.10 |

La conversion se place **après** les retraitements faits en dirhams et **avant** le cumul, les éliminations et le partage : le dividende reçu par ESCALDÈRE et celui que verse ESCALDÈRE MAROC sont éliminés pour le même montant en euros (cours du jour du paiement), et l'écart de conversion fait partie des capitaux propres convertis à partager à 90 % et 10 %.

---

### 1.4 Périmètre et méthodes (3 pts)

**Tableau (1,5 pt : 0,25 par filiale intégrée, soit 0,75 ; 0,75 pour LIANTS D'OLT)**

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % d'intérêt des minoritaires |
|---|---|---|---|---|---|
| SA ESCALDÈRE | — | Société consolidante | — | 100 % | — |
| ENROBÉS DU VIAUR | 100 % | Exclusif | Intégration globale | 100 % | 0 % |
| ESCALDÈRE MAROC | 90 % | Exclusif | Intégration globale | 90 % | 10 % |
| GRANULATS DU LÉVÉZOU | 80 % | Exclusif | Intégration globale | 80 % | 20 % |
| LIANTS D'OLT | 30 % | Influence notable | Mise en équivalence | 30 % | — |

Toutes les participations sont directes : les pourcentages de contrôle et d'intérêt sont égaux à la part du capital détenue, chaque action donnant droit à une voix. La majorité des droits de vote donne le contrôle exclusif [V ANC art. 211-3, p. 12-13 ; F03 § 2], qui conduit à l'intégration globale [V art. 221-1, p. 18 ; F03 § 3].

**LIANTS D'OLT (1 pt).** ESCALDÈRE détient 30 % des droits de vote, au moins 20 % : l'influence notable est présumée [V art. 211-5, p. 13 ; F03 § 2]. Elle n'a pas le contrôle exclusif : BITULANE détient la majorité des voix (60 %) et désigne quatre des six membres du comité de direction ; ni contrôle conjoint : aucun accord ne soumet les décisions à son accord [V art. 211-3 et 211-4, p. 12-13]. Les indices confirment l'influence notable : représentation au comité de direction (deux membres sur six), dépendance technique (formules mises au point par le laboratoire d'ESCALDÈRE), mise à disposition d'un ingénieur comme responsable de la production [V art. 211-5, p. 13]. D'où la mise en équivalence [V art. 221-1, p. 18].

**Société étrangère (0,5 pt).** La nationalité est sans incidence : la nature du contrôle, et elle seule, détermine l'entrée dans le périmètre et la méthode [V art. 221-1, p. 18 ; F03 § 3]. ESCALDÈRE MAROC, contrôlée exclusivement, est intégrée globalement. Une exclusion n'est obligatoire qu'en cas de restrictions sévères et durables [V art. 212-1, p. 17 ; F03 § 2] ; les transferts de fonds vers la France ne font l'objet d'aucune restriction (le dividende de 2026 a été versé). La seule conséquence est technique : ses comptes, tenus en dirhams, sont convertis (question 1.5).

---

### 1.5 Conversion des comptes d'ESCALDÈRE MAROC (6 pts)

#### a. Méthode de conversion (1,5 pt)

- **Règle (0,5 pt).** Deux méthodes existent : celle du **cours historique** (éléments non monétaires et capitaux propres au cours historique, éléments monétaires au cours de clôture, produits et charges au cours du jour, en pratique au cours moyen) et celle du **cours de clôture** (actifs et passifs au cours de clôture, produits et charges au cours moyen) [V ANC art. 272-16 et 272-17, p. 59-60 ; F04 R13], les capitaux propres restant au cours historique [S ; F04 R13 ; manuel, annexe 1.3]. Dans le cas général, la conversion de la monnaie locale à la monnaie de fonctionnement suit la méthode du cours historique, et la conversion de la monnaie de fonctionnement à la monnaie de l'entité consolidante celle du cours de clôture [V art. 272-18, p. 60 ; F04 R13].
- **Entité autonome (0,75 pt).** La monnaie de fonctionnement est la monnaie locale pour une entité autonome, celle de l'entité dont elle dépend pour une entité non autonome ; une entité n'est pas autonome lorsque son exploitation fait partie intégrante des activités d'une autre, notamment lorsque la monnaie de la consolidante est prépondérante pour ses opérations ou son financement, ou que ses liens commerciaux ou financiers avec la consolidante sont prépondérants [V IR3 sous art. 272-15, p. 59 ; F04 R13]. ESCALDÈRE MAROC vend à des clients marocains, achète, paie ses salariés et se finance en dirhams, fixe ses prix, est dirigée sur place et n'a avec ESCALDÈRE que des flux de dividendes : elle est **autonome**, sa monnaie de fonctionnement est le dirham. Ses comptes sont donc convertis directement du dirham à l'euro au **cours de clôture**, comme le prévoit le manuel.
- **Monnaie stable (0,25 pt).** L'inflation marocaine, inférieure à 3 % par an, ne présente aucune des caractéristiques d'une forte inflation (taux cumulé sur trois ans approchant ou dépassant 100 %, prix indexés ou exprimés dans une monnaie étrangère) [V art. 272-22, p. 61] : les règles particulières à ces pays ne s'appliquent pas.

#### b. Conversion du bilan et du compte de résultat (2 pts)

**Compte de résultat de 2026 (0,5 pt)** — cours moyen de 11,00 MAD pour 1 €

| Postes | MAD | Cours | € |
|---|---:|---:|---:|
| Chiffre d'affaires | 57 750 000 | 11,00 | 5 250 000 |
| Achats consommés et charges externes | – 31 900 000 | 11,00 | – 2 900 000 |
| Charges de personnel | – 12 100 000 | 11,00 | – 1 100 000 |
| Dotations aux amortissements | – 6 050 000 | 11,00 | – 550 000 |
| Charges financières | – 1 100 000 | 11,00 | – 100 000 |
| Impôt sur les bénéfices | – 1 650 000 | 11,00 | – 150 000 |
| **Résultat net** | **4 950 000** | | **450 000** |

Avec la méthode du cours de clôture, les dotations aux amortissements suivent elles aussi le cours moyen.

**Bilan au 31/12/2026 (1,5 pt : actif et dettes 0,5 ; réserves 0,5 ; résultat et écart cumulé 0,5)**

| Actif | MAD | Cours | € |
|---|---:|---:|---:|
| Immobilisations corporelles nettes | 40 500 000 | 11,25 | 3 600 000 |
| Stocks | 4 950 000 | 11,25 | 440 000 |
| Clients | 9 000 000 | 11,25 | 800 000 |
| Disponibilités | 2 250 000 | 11,25 | 200 000 |
| **Total** | **56 700 000** | | **5 040 000** |

| Passif | MAD | Cours | € |
|---|---:|---:|---:|
| Capital | 21 500 000 | 10,75 (historique) | 2 000 000 |
| Réserves | 12 497 500 | historiques | 1 185 000 |
| Résultat de 2026 | 4 950 000 | 11,00 (moyen) | 450 000 |
| **Écart de conversion cumulé** (solde) | — | | **– 173 000** |
| Emprunts | 9 000 000 | 11,25 | 800 000 |
| Fournisseurs et autres dettes | 8 752 500 | 11,25 | 778 000 |
| **Total** | **56 700 000** | | **5 040 000** |

- **Réserves converties** : 870 000 € (réserves au 01/01/2026, cours historiques) + 540 000 € (résultat de 2025 porté en réserves, au cours moyen de 2025) – 225 000 € (dividende du 15/06/2026 : 2 452 500 / 10,90, cours du jour du paiement) = **1 185 000 €**. En dirhams : 9 280 000 + 5 670 000 – 2 452 500 = 12 497 500 MAD.
- **Écart cumulé** : capitaux propres convertis au cours de clôture, 38 947 500 / 11,25 = 3 462 000 € ; capitaux propres aux cours historiques et moyen, 2 000 000 + 1 185 000 + 450 000 = 3 635 000 € ; écart **– 173 000 €** (le total de l'actif, 5 040 000 €, moins les dettes, 1 578 000 €, donne bien 3 462 000 €).

#### c. Analyse de l'écart de conversion de 2026 (1,5 pt)

| Origine | Calcul | € |
|---|---|---:|
| Capitaux propres d'ouverture (0,5) | 36 450 000 / 11,25 – 36 450 000 / 10,80 = 3 240 000 – 3 375 000 | – 135 000 |
| Résultat de 2026 (0,25) | 4 950 000 / 11,25 – 4 950 000 / 11,00 = 440 000 – 450 000 | – 10 000 |
| Dividende versé (0,25) | – (2 452 500 / 11,25 – 2 452 500 / 10,90) = – (218 000 – 225 000) | + 7 000 |
| **Écart né en 2026** | | **– 138 000** |
| Écart cumulé au 31/12/2025 (annexe 1.4) | | – 35 000 |
| **Écart cumulé au 31/12/2026** (0,5 pour le rapprochement) | | **– 173 000** |

Le dirham s'est déprécié face à l'euro en 2026 (10,80 puis 11,25 MAD pour 1 €) : les capitaux propres d'ouverture, désormais convertis au cours de clôture de 2026, valent moins en euros ; le résultat, acquis au cours moyen, aussi. Le dividende, sorti des capitaux propres au cours du 15/06/2026 (10,90), plus favorable que le cours de clôture, réduit la perte de 7 000 €. Contrôle : 3 375 000 (ouverture au cours de clôture de 2025) – 225 000 + 450 000 – 138 000 = 3 462 000 €. L'écart cumulé au 31/12/2025, montant fourni, résulte des exercices antérieurs : 3 375 000 – (2 000 000 + 870 000 + 540 000) = – 35 000 €.

#### d. Partage de l'écart de conversion (1 pt)

**Partage (0,5 pt).** Les écarts de conversion, tant sur les éléments du bilan d'ouverture que sur le résultat, sont portés dans les capitaux propres consolidés au poste « Écarts de conversion » pour la part de l'entité consolidante et dans les intérêts minoritaires pour la part des tiers [V ANC art. 272-21, p. 61 ; F04 R13] : part du groupe 90 % × – 173 000 = **– 155 700 €** ; intérêts minoritaires 10 % × – 173 000 = **– 17 300 €** (dont, pour l'écart né en 2026, – 124 200 € et – 13 800 €). Le manuel n'y attache aucun impôt différé.

**C1 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| ECV_G Écarts de conversion – part du groupe | 155 700 | |
| ECV_M Écarts de conversion – intérêts minoritaires | 17 300 | |
| ECV.MAROC Écart de conversion d'ESCALDÈRE MAROC | | 173 000 |
| *Partage de l'écart de conversion cumulé d'ESCALDÈRE MAROC* | **173 000** | **173 000** |

---

### 1.6 Coûts d'emprunt de la centrale d'ENROBÉS DU VIAUR (5 pts)

**Justification (1 pt).** Le PCG autorise deux méthodes : les coûts d'emprunt en charges, ou leur incorporation au coût d'un actif éligible, c'est-à-dire d'un actif qui exige une longue période de préparation ou de construction, pour la période de production de cet actif, jusqu'à sa réception définitive [V PCG art. 213-9, p. 17-18 ; F04 § 10]. ENROBÉS DU VIAUR a choisi les charges ; le manuel retient l'incorporation. Les méthodes du groupe s'appliquent de manière homogène à toutes les entités : les comptes de la filiale sont retraités [V ANC art. 271-5, p. 52 ; F04 § 1 et R6]. La centrale, construite du 01/04/2025 au 30/06/2026, est un actif éligible ; l'emprunt de 4 000 000 €, affecté exclusivement à sa construction, est un emprunt spécifique dont les fonds non dépensés n'ont rien rapporté. Les intérêts ayant été déduits fiscalement à mesure qu'ils couraient, la base fiscale de la centrale ne les comprend pas : la valeur consolidée la dépasse, d'où un **impôt différé passif** [V art. 272-8, p. 57 ; F04 § 10].

**Calculs (1 pt)**

| | Période | Calcul | Montant |
|---|---|---|---:|
| Intérêts de 2025 incorporés (0,25) | 01/04 au 31/12/2025 | 4 000 000 × 4 % × 9/12 | 120 000 |
| Intérêts de 2026 incorporés (0,25) | 01/01 au 30/06/2026 | 4 000 000 × 4 % × 6/12 | 80 000 |
| Intérêts de 2026 maintenus en charges | 01/07 au 31/12/2026 | 160 000 – 80 000 | 80 000 |
| **Intérêts incorporés** | | | **200 000** |
| Amortissement complémentaire de 2026 (0,5) | 6 mois | 200 000 / 20 × 6/12 | 5 000 |

Les intérêts courus après la mise en service ne sont plus incorporables : ils restent en charges [V PCG art. 213-9, p. 17-18]. La dotation des comptes individuels (6 000 000 / 20 × 6/12 = 150 000 €) n'est pas modifiée : seul le complément lié aux intérêts incorporés s'y ajoute.

**Tableau des incidences (1,5 pt)**

| | 2025 (ouverture, réserves) | 2026 (résultat) | Clôture (31/12/2026) |
|---|---:|---:|---:|
| Intérêts incorporés au coût de la centrale | + 120 000 | + 80 000 | + 200 000 |
| Amortissement complémentaire | — | – 5 000 | – 5 000 |
| **Écart de valeur nette (avant impôt)** | **+ 120 000** | **+ 75 000** | **+ 195 000** |
| Impôt différé passif (25 %) | – 30 000 | – 18 750 | **– 48 750** |
| **Net** | **+ 90 000** (réserves) | **+ 56 250** (résultat) | + 146 250 |

(Écarts bruts : 0,5 ; impôt différé : 0,5 ; répartition réserves / résultat : 0,5.) Au 31/12/2025, les 120 000 € auraient figuré en immobilisations en cours ; au 31/12/2026, la centrale mise en service est inscrite au compte 2151.

**C2 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2151 Installations complexes spécialisées (intérêts incorporés) | 200 000 | |
| 2815 Amortissements des installations, matériel et outillage industriels | | 5 000 |
| RSV.VIAUR Réserves ENROBÉS DU VIAUR (120 000 × 75 %) | | 90 000 |
| RST.VIAUR Résultat ENROBÉS DU VIAUR (75 000 × 75 %) | | 56 250 |
| IDP Impôt différé passif (195 000 × 25 %) | | 48 750 |
| *Incorporation des intérêts de la période de construction* | **200 000** | **200 000** |

**C2R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 68112 Dotations aux amortissements des immobilisations corporelles | 5 000 | |
| CH_ID Charge d'impôt différé (75 000 × 25 %) | 18 750 | |
| RES_CR Résultat | 56 250 | |
| 6611 Intérêts des emprunts et dettes (intérêts du premier semestre 2026 incorporés) | | 80 000 |
| *Intérêts de 2026 incorporés et amortissement complémentaire* | **80 000** | **80 000** |

ENROBÉS DU VIAUR étant détenue à 100 %, le retraitement revient en totalité au groupe.

---

### 1.7 Opérations internes (4 pts)

#### a. Ventes de granulats et marge interne (2 pts)

**Justification (0,5 pt).** Les ventes et achats réciproques sont éliminés en totalité, sans incidence sur le résultat [V ANC art. 251-1, p. 45 ; F04 R14]. Le profit interne compris dans le stock d'ENROBÉS DU VIAUR est éliminé en totalité, puis réparti entre le groupe et les minoritaires **de l'entité qui l'a réalisé**, GRANULATS DU LÉVÉZOU ; l'impôt est corrigé [V art. 251-2, p. 45 ; F04 R14]. L'élimination ramène le stock au-dessous de sa base fiscale (prix d'achat payé par ENROBÉS DU VIAUR) : **impôt différé actif**. Aucune marge n'est à éliminer à l'ouverture : GRANULATS DU LÉVÉZOU n'avait rien vendu à ENROBÉS DU VIAUR avant 2026.

**Calcul (0,5 pt).** Marge interne : 320 000 × 25 % = **80 000 €** (taux exprimé sur le prix de vente) ; impôt différé actif : 80 000 × 25 % = **20 000 €** ; incidence nette sur le résultat de GRANULATS DU LÉVÉZOU : **– 60 000 €**.

**Répartition (0,5 pt).** L'élimination réduit le résultat retraité de GRANULATS DU LÉVÉZOU (question 1.9 a) ; elle est donc supportée à 80 % par le groupe (– 48 000 €) et à 20 % par les minoritaires de la société vendeuse (– 12 000 €). Elle n'aurait été supportée par le seul groupe que si la vente avait été faite par ENROBÉS DU VIAUR, détenue à 100 %.

**C4, C5 et C5R (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 701 Ventes de produits finis (GRANULATS DU LÉVÉZOU) | 2 400 000 | |
| 601 Achats stockés – matières premières (ENROBÉS DU VIAUR, après l'avoir) | | 2 400 000 |
| *C4 – Élimination des ventes internes de granulats (compte de résultat)* | **2 400 000** | **2 400 000** |
| RST.LEVEZOU Résultat GRANULATS DU LÉVÉZOU (80 000 × 75 %) | 60 000 | |
| IDA Impôt différé actif | 20 000 | |
| 31 Matières premières (stock d'ENROBÉS DU VIAUR) | | 80 000 |
| *C5 – Élimination de la marge interne sur le stock (bilan)* | **80 000** | **80 000** |
| 6031 Variation des stocks de matières premières | 80 000 | |
| CH_ID Produit d'impôt différé | | 20 000 |
| RES_CR Résultat | | 60 000 |
| *C5R – Élimination de la marge interne (compte de résultat)* | **80 000** | **80 000** |

#### b. Comptes réciproques et avoir non enregistré (1 pt)

**Rapprochement et avoir (0,5 pt).** Dette d'ENROBÉS DU VIAUR 410 000 € – créance de GRANULATS DU LÉVÉZOU 380 000 € = 30 000 €, montant de la facture émise en double et annulée par l'avoir du 30/12/2026, que l'acheteur n'a pas enregistré. L'achat facturé deux fois ne correspond à aucune livraison : il est annulé chez ENROBÉS DU VIAUR, ce qui augmente son résultat de 30 000 €. ENROBÉS DU VIAUR n'enregistrera l'avoir qu'en 2027, année où ce montant sera imposé : la régularisation dégage une différence temporaire imposable, d'où un **impôt différé passif** de 7 500 € [V art. 272-8, p. 57 ; F04 § 1]. Après correction, les achats d'ENROBÉS DU VIAUR auprès de GRANULATS DU LÉVÉZOU (2 400 000 €) égalent les ventes de celle-ci, et les soldes réciproques sont égaux (380 000 €).

**C3 et C3R** (régularisation de l'avoir)

| Compte | Débit | Crédit |
|---|---:|---:|
| 4011 Fournisseurs (dette d'ENROBÉS DU VIAUR) | 30 000 | |
| RST.VIAUR Résultat ENROBÉS DU VIAUR (30 000 × 75 %) | | 22 500 |
| IDP Impôt différé passif | | 7 500 |
| *C3 – Enregistrement de l'avoir du 30/12/2026 (bilan)* | **30 000** | **30 000** |
| CH_ID Charge d'impôt différé | 7 500 | |
| RES_CR Résultat | 22 500 | |
| 601 Achats stockés – matières premières (achat facturé en double) | | 30 000 |
| *C3R – Annulation de l'achat facturé en double (compte de résultat)* | **30 000** | **30 000** |

**C6 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4011 Fournisseurs (dette d'ENROBÉS DU VIAUR : 410 000 – 30 000) | 380 000 | |
| 4111 Clients (créance de GRANULATS DU LÉVÉZOU) | | 380 000 |
| *Élimination des soldes réciproques* | **380 000** | **380 000** |

#### c. Dividende d'ESCALDÈRE MAROC (1 pt)

**Justification et montant (0,5 pt).** Les dividendes reçus des sociétés consolidées sont éliminés en totalité [V ANC art. 251-2, p. 45 ; F04 R14]. ESCALDÈRE a reçu 90 % × 2 452 500 = 2 207 250 MAD, convertis au cours du jour du paiement : 2 207 250 / 10,90 = **202 500 €**. Ce dividende n'est qu'un transfert du résultat de 2025 d'ESCALDÈRE MAROC, déjà compris dans les réserves consolidées : il sort du résultat d'ESCALDÈRE et rejoint ses réserves. Le même cours (10,90) sert à déduire le dividende des réserves converties d'ESCALDÈRE MAROC (225 000 €, question 1.5 b) : l'élimination ne laisse aucun écart. La part de l'associé marocain, 22 500 €, a quitté le groupe : elle réduit les réserves d'ESCALDÈRE MAROC, donc les intérêts minoritaires, sans autre écriture.

**C7 (bilan) et C7R (compte de résultat), 0,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.ESCALDERE Résultat SA ESCALDÈRE | 202 500 | |
| RSV.ESCALDERE Réserves SA ESCALDÈRE | | 202 500 |
| *C7 – Élimination du dividende reçu d'ESCALDÈRE MAROC* | **202 500** | **202 500** |
| 7611 Revenus des titres de participation | 202 500 | |
| RES_CR Résultat | | 202 500 |
| *C7R – Élimination du dividende au compte de résultat* | **202 500** | **202 500** |

---

### 1.8 Acquisition de GRANULATS DU LÉVÉZOU (7 pts)

#### a. Actif net réévalué au 01/01/2026 et suivi des écarts (2,5 pts)

| Élément | Montant |
|---|---:|
| Capitaux propres individuels au 01/01/2026, résultat de 2025 compris (0,25) | 6 265 000 |
| Écart d'évaluation du terrain d'assiette (1 200 000 – 700 000) (0,25) | + 500 000 |
| Écart d'évaluation de l'installation de concassage (1 600 000 – 1 120 000) (0,25) | + 480 000 |
| Impôt différé passif sur les écarts ((500 000 + 480 000) × 25 %) (0,5) | – 245 000 |
| **Actif net réévalué** (0,25) | **7 000 000** |

- **Principe (0,5 pt).** L'écart d'évaluation est la différence entre la valeur d'entrée d'un élément identifiable et sa valeur comptable dans le bilan de l'entité acquise retraité selon les méthodes du groupe [V ANC art. 231-9, p. 22 ; F05 § 1.2] ; la valeur d'entrée est le prix que l'acquéreur aurait accepté de payer pour l'élément pris séparément, et les impôts différés sur les écarts sont comptabilisés [V art. 232-1, p. 24], en contrepartie de l'écart d'acquisition [V art. 272-13, p. 58-59 ; F05 § 1.2]. L'énoncé précise que celui du terrain en donne lieu, lui aussi.
- **Suivi en 2026 (0,5 pt).** Le terrain d'assiette, non amortissable, garde son écart de 500 000 € et son impôt différé passif de 125 000 € tant qu'il reste dans le groupe. L'écart sur l'installation est amorti sur sa durée résiduelle : 480 000 / 8 = **60 000 €** par an ; l'impôt différé correspondant est repris de 15 000 € ; au 31/12/2026, l'impôt différé passif sur l'installation est de (480 000 – 60 000) × 25 % = 105 000 €.

#### b. Coût d'acquisition et écart d'acquisition (2 pts)

- **Frais (0,75 pt).** Dans ses comptes individuels, ESCALDÈRE a comptabilisé les honoraires en charges, option permise par le PCG [V PCG art. 121-5 ; F05 § 1.1], et les a déduits fiscalement. En consolidation, le coût d'acquisition comprend les coûts directement imputables à l'acquisition, dont les honoraires de consultants et d'experts, **nets de l'économie d'impôt** [V ANC art. 231-2 et 231-3, p. 20-21 ; F05 § 1.1] : les frais sont retirés des charges de 2026 et ajoutés, nets d'impôt, au coût des titres.
- **Coût d'acquisition (0,5 pt)** : 6 910 000 + 120 000 × 75 % = **7 000 000 €**.
- **Écart d'acquisition (0,75 pt)** : 7 000 000 – 80 % × 7 000 000 = 7 000 000 – 5 600 000 = **1 400 000 €**, écart **positif**, inscrit à l'actif immobilisé, en immobilisations incorporelles, ligne « dont écarts d'acquisition positifs » [V art. 231-9, p. 22 ; art. 231-11, p. 23 ; art. 281-1, p. 66 ; F05 § 1.3]. Il ne porte que sur la part de l'acquéreur ; les droits des minoritaires sont calculés sur l'actif net réévalué [V art. 232-1, p. 24 ; F05 § 1.3].

#### c. Durée d'utilisation, amortissement et écritures (2,5 pts)

**Durée d'utilisation (1 pt).** L'entité détermine la durée d'utilisation, limitée ou non, de l'écart d'acquisition par une analyse documentée des caractéristiques de l'opération, sur les plans technique, économique et juridique ; cette détermination n'est pas une option ; parmi les critères figurent les raisons légales ou contractuelles qui bornent l'horizon d'exercice de l'activité [V ANC art. 231-11 et IR3, p. 23 ; F05 § 1.3 et 9]. En l'espèce, l'autorisation préfectorale d'exploiter expire le 31/12/2045, le gisement autorisé sera alors épuisé et aucune extension ni aucun renouvellement n'est possible ; les avantages payés au-delà de l'actif net réévalué (position de la carrière, contrats avec les centrales de la région) cesseront avec l'extraction. La durée d'utilisation est donc **limitée**, et déterminée de façon fiable : **20 ans** (2026 à 2045). L'écart est amorti linéairement sur cette durée [V art. 231-11, p. 23] : dotation de 2026 = 1 400 000 / 20 = **70 000 €** ; valeur nette au 31/12/2026 : **1 330 000 €**. La dotation figure au compte de résultat consolidé sur la ligne propre aux écarts d'acquisition, entre le résultat d'exploitation avant et après ces dotations [V IR3 sous art. 231-12, p. 24 ; art. 281-2, p. 67 ; F05 § 1.3] ; l'écart ne portant que sur la part du groupe, son amortissement réduit le seul résultat part du groupe. À chaque clôture, le groupe apprécie en outre s'il existe un indice de perte de valeur [V art. 231-11, p. 23] ; l'énoncé n'en signale aucun.

**C8 (bilan) et C8R (compte de résultat), 0,75 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2112 Terrains aménagés (écart d'évaluation du terrain d'assiette) | 500 000 | |
| 2151 Installations complexes spécialisées (écart d'évaluation de l'installation) | 480 000 | |
| RST.LEVEZOU Résultat GRANULATS DU LÉVÉZOU (60 000 × 75 %) | 45 000 | |
| 2815 Amortissements des installations (480 000 / 8) | | 60 000 |
| IDP Impôt différé passif (125 000 + 105 000) | | 230 000 |
| RSV.LEVEZOU Réserves GRANULATS DU LÉVÉZOU ((500 000 + 480 000) × 75 %) | | 735 000 |
| *C8 – Écarts d'évaluation nets d'impôt et amortissement de 2026* | **1 025 000** | **1 025 000** |
| 68112 Dotations aux amortissements des immobilisations corporelles | 60 000 | |
| CH_ID Produit d'impôt différé (60 000 × 25 %) | | 15 000 |
| RES_CR Résultat | | 45 000 |
| *C8R – Amortissement de l'écart d'évaluation de l'installation* | **60 000** | **60 000** |

**C9 (bilan) et C9R (compte de résultat), 0,25 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation GRANULATS DU LÉVÉZOU (120 000 × 75 %) | 90 000 | |
| RST.ESCALDERE Résultat SA ESCALDÈRE | | 90 000 |
| *C9 – Incorporation des frais nets d'impôt au coût des titres* | **90 000** | **90 000** |
| 695 Impôts sur les bénéfices (économie d'impôt incorporée au coût des titres) | 30 000 | |
| RES_CR Résultat | 90 000 | |
| 6226 Honoraires | | 120 000 |
| *C9R – Annulation des frais d'acquisition des titres* | **120 000** | **120 000** |

**C11 (bilan) et C11R (compte de résultat), 0,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST_G Résultat consolidé – part du groupe | 70 000 | |
| AMO_EA Amortissements de l'écart d'acquisition GRANULATS DU LÉVÉZOU | | 70 000 |
| *C11 – Amortissement de 2026 de l'écart d'acquisition* | **70 000** | **70 000** |
| DOT_EA Dotations aux amortissements et dépréciations des écarts d'acquisition | 70 000 | |
| RES_CR Résultat | | 70 000 |
| *C11R – Dotation de 2026 au compte de résultat* | **70 000** | **70 000** |

(Écriture C11 présentée après l'élimination des titres C10, qui inscrit l'écart d'acquisition à l'actif.)

---

### 1.9 Partage des capitaux propres et mise en équivalence (7 pts)

#### a. Tableaux de partage au 31/12/2026 (3 pts)

**GRANULATS DU LÉVÉZOU (1,25 pt)**

Résultat retraité de 2026 : 900 000 – 45 000 (écart sur l'installation, net) – 60 000 (marge interne, nette) = **795 000 €** (0,25).

| | Total | Groupe (80 %) | Intérêts minoritaires (20 %) |
|---|---:|---:|---:|
| Capital | 2 500 000 | 2 000 000 | 500 000 |
| Réserves (3 125 000 + résultat de 2025 affecté 640 000) | 3 765 000 | 3 012 000 | 753 000 |
| Écarts d'évaluation nets d'impôt différé (à l'acquisition) | 735 000 | 588 000 | 147 000 |
| **Capitaux propres retraités hors résultat** | **7 000 000** | **5 600 000** | **1 400 000** |
| Élimination des titres (coût d'acquisition) | | – 7 000 000 | |
| Écart d'acquisition (inscrit à l'actif) | | + 1 400 000 | |
| **Réserves consolidées** | | **0** | |
| Résultat retraité de 2026 | 795 000 | 636 000 | 159 000 |
| **Intérêts minoritaires au 31/12/2026** | | | **1 559 000** |

(Capitaux propres retraités : 0,25 ; titres, écart d'acquisition et réserves nulles : 0,25 ; résultat et intérêts minoritaires : 0,5.) Acquise le 01/01/2026, la société n'apporte aucune réserve consolidée. Sa contribution au résultat part du groupe est de 636 000 – 70 000 (amortissement de l'écart d'acquisition) = **566 000 €** ; les minoritaires supportent 20 % de l'élimination de la marge interne (12 000 €) et de l'amortissement de l'écart sur l'installation (9 000 €).

**ENROBÉS DU VIAUR (0,5 pt)**

| | Total | Groupe (100 %) |
|---|---:|---:|
| Capital | 4 000 000 | 4 000 000 |
| Réserves retraitées (2 600 000 + 90 000) | 2 690 000 | 2 690 000 |
| Élimination des titres (souscrits à la création) | | – 4 000 000 |
| **Réserves consolidées** | | **2 690 000** |
| Résultat retraité (700 000 + 56 250 + 22 500) | 778 750 | 778 750 |

**ESCALDÈRE MAROC, après conversion (1,25 pt)**

| | Total | Groupe (90 %) | Intérêts minoritaires (10 %) |
|---|---:|---:|---:|
| Capital (cours historique) | 2 000 000 | 1 800 000 | 200 000 |
| Réserves (cours historiques) | 1 185 000 | 1 066 500 | 118 500 |
| Élimination des titres (souscrits à la création) | | – 1 800 000 | |
| **Réserves consolidées** | | **1 066 500** | |
| Écart de conversion cumulé | – 173 000 | – 155 700 | – 17 300 |
| Résultat de 2026 (cours moyen) | 450 000 | 405 000 | 45 000 |
| **Total** | **3 462 000** | | **346 200** |

(Réserves et titres : 0,5 ; écart de conversion : 0,25 ; résultat et intérêts minoritaires : 0,5.) Les titres, souscrits à la création pour 90 % du capital au cours de 10,75, égalent la part du groupe dans le capital converti au même cours : aucun écart d'acquisition. Les intérêts minoritaires représentent 10 % des capitaux propres convertis au cours de clôture (3 462 000 €), écart de conversion compris.

#### b. Mise en équivalence de LIANTS D'OLT (1,5 pt)

| | Montant |
|---|---:|
| Capitaux propres de LIANTS D'OLT au 31/12/2026 (1 500 000 + 2 300 000 + 400 000) | 4 200 000 |
| **Valeur d'équivalence** (30 %) (0,5) | **1 260 000** |
| Quote-part des capitaux propres à l'acquisition : 30 % × 3 000 000 | 900 000 |
| Écart d'acquisition de 2020 : 1 050 000 – 900 000 (0,25), amorti en totalité de 2020 à 2024 | 150 000 |
| Réserves consolidées : 30 % × (3 800 000 – 3 000 000) – 150 000 (0,25) | 90 000 |
| Résultat de 2026 : 30 % × 400 000 (0,25) | 120 000 |

(Absence d'écart d'évaluation justifiée : 0,25.) Les actifs et passifs identifiables de LIANTS D'OLT avaient une valeur d'entrée égale à leur valeur comptable : aucun écart d'évaluation ; le coût des titres dépassait la quote-part des capitaux propres de 150 000 € : un écart d'acquisition, présenté selon les mêmes modalités que pour l'intégration globale [V ANC art. 262-2, p. 49 ; F05 § 4]. Entièrement amorti à la fin de 2024, il n'a plus d'effet sur 2026, mais son amortissement passé a réduit les réserves consolidées (`JUR-G03` : le candidat doit examiner les écarts d'évaluation et d'acquisition, et non les ignorer). Contrôle : 1 260 000 – 1 050 000 = 210 000 = 90 000 + 120 000. LIANTS D'OLT n'ayant ni versé de dividende ni réalisé d'opération avec le groupe, aucune autre élimination n'est nécessaire [V art. 262-3 et 262-4, p. 49-50 ; F05 § 4].

#### c. Écritures (2,5 pts)

**C10 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.LEVEZOU Capital GRANULATS DU LÉVÉZOU | 2 500 000 | |
| RSV.LEVEZOU Réserves retraitées (3 765 000 + 735 000) | 4 500 000 | |
| RST.LEVEZOU Résultat retraité | 795 000 | |
| EA Écart d'acquisition GRANULATS DU LÉVÉZOU | 1 400 000 | |
| 261 Titres de participation (6 910 000 + 90 000) | | 7 000 000 |
| RSV_M Intérêts minoritaires – capital et réserves (20 % × 7 000 000) | | 1 400 000 |
| RST_G Résultat consolidé – part du groupe (80 % × 795 000) | | 636 000 |
| RST_M Intérêts minoritaires – résultat (20 % × 795 000) | | 159 000 |
| *Élimination des titres GRANULATS DU LÉVÉZOU, écart d'acquisition et partage* | **9 195 000** | **9 195 000** |

**C12 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.VIAUR Capital ENROBÉS DU VIAUR | 4 000 000 | |
| RSV.VIAUR Réserves retraitées | 2 690 000 | |
| RST.VIAUR Résultat retraité | 778 750 | |
| 261 Titres de participation ENROBÉS DU VIAUR | | 4 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 2 690 000 |
| RST_G Résultat consolidé – part du groupe | | 778 750 |
| *Élimination des titres ENROBÉS DU VIAUR et partage (100 % groupe)* | **7 468 750** | **7 468 750** |

**C13 (bilan, 0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM.MAROC Capital ESCALDÈRE MAROC (cours historique) | 2 000 000 | |
| RSV.MAROC Réserves (cours historiques) | 1 185 000 | |
| RST.MAROC Résultat (cours moyen) | 450 000 | |
| 261 Titres de participation ESCALDÈRE MAROC | | 1 800 000 |
| RSV_G Réserves consolidées – part du groupe (90 % × 3 185 000 – 1 800 000) | | 1 066 500 |
| RSV_M Intérêts minoritaires – capital et réserves (10 % × 3 185 000) | | 318 500 |
| RST_G Résultat consolidé – part du groupe (90 % × 450 000) | | 405 000 |
| RST_M Intérêts minoritaires – résultat (10 % × 450 000) | | 45 000 |
| *Élimination des titres ESCALDÈRE MAROC et partage des capitaux propres convertis* | **3 635 000** | **3 635 000** |

L'écart de conversion a été partagé par l'écriture C1 (question 1.5 d) ; les intérêts minoritaires d'ESCALDÈRE MAROC s'élèvent à 318 500 + 45 000 – 17 300 = 346 200 €.

**C14 (bilan) et C14R (compte de résultat), 0,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence (30 % × 4 200 000) | 1 260 000 | |
| EA Écart d'acquisition LIANTS D'OLT | 150 000 | |
| AMO_EA Amortissements de l'écart d'acquisition LIANTS D'OLT (2020 à 2024) | | 150 000 |
| 261 Titres de participation LIANTS D'OLT | | 1 050 000 |
| RSV_G Réserves consolidées – part du groupe | | 90 000 |
| RST_G Résultat consolidé – part du groupe | | 120 000 |
| *C14 – Mise en équivalence des titres LIANTS D'OLT* | **1 410 000** | **1 410 000** |
| RES_CR Résultat | 120 000 | |
| QP_MEE Résultat net lié aux entités mises en équivalence | | 120 000 |
| *C14R – Quote-part de résultat de LIANTS D'OLT* | **120 000** | **120 000** |

La quote-part de résultat figure sur la ligne « résultat net lié aux entités mises en équivalence », après le résultat net des entités intégrées [V art. 262-3, p. 49 ; art. 281-2, p. 67 ; F05 § 4].

---

### 1.10 Documents de synthèse (7 pts)

#### a. Extrait du bilan consolidé au 31/12/2026 (5 pts)

Modèle du règlement ANC [V art. 281-1, p. 66 ; F14 § 1.2]. Les impôts différés actifs et passifs d'une même entité fiscale sont présentés pour leur solde net [V ANC art. 272-14, p. 59 ; F04 § 8] ; en l'absence d'intégration fiscale, la compensation se fait société par société, l'impôt différé actif de la marge interne étant rattaché, selon le manuel, à GRANULATS DU LÉVÉZOU, qui l'a réalisée.

**Impôts différés par société**

| Société | Impôts différés passifs | Impôts différés actifs | Solde net |
|---|---:|---:|---:|
| GRANULATS DU LÉVÉZOU | 125 000 + 105 000 (C8) | 20 000 (C5) | **210 000** passif |
| ENROBÉS DU VIAUR | 48 750 (C2) + 7 500 (C3) | — | **56 250** passif |
| **Total** | | | **266 250** passif ; aucun impôt différé actif |

**Réserves consolidées et résultat net part du groupe**

| Société | Réserves consolidées | Résultat net part du groupe |
|---|---:|---:|
| SA ESCALDÈRE | 18 400 000 + 202 500 (C7) = 18 602 500 | 2 600 000 – 202 500 (C7) + 90 000 (C9) = 2 487 500 |
| ENROBÉS DU VIAUR | 2 690 000 | 778 750 |
| GRANULATS DU LÉVÉZOU | 0 | 636 000 – 70 000 (C11) = 566 000 |
| ESCALDÈRE MAROC | 1 066 500 | 405 000 |
| LIANTS D'OLT | 90 000 | 120 000 |
| **Total** | **22 449 000** | **4 357 250** |

Résultat net de l'ensemble consolidé : 4 357 250 + 159 000 + 45 000 (intérêts minoritaires) = 4 561 250 €.

**Extrait du bilan consolidé au 31/12/2026**

| Actif | Calcul | Montant |
|---|---|---:|
| Immobilisations incorporelles | 1 240 000 + 1 330 000 (0,25) | 2 570 000 |
| dont écarts d'acquisition positifs | GRANULATS DU LÉVÉZOU 1 400 000 – 70 000 ; LIANTS D'OLT 150 000 – 150 000 (0,5) | 1 330 000 |
| Immobilisations corporelles | 48 600 000 + 3 600 000 (ESCALDÈRE MAROC converti) + 500 000 + 480 000 – 60 000 (écarts d'évaluation) + 200 000 – 5 000 (coûts d'emprunt) (0,75) | 53 315 000 |
| Immobilisations financières | 14 420 000 – 13 760 000 (titres éliminés ou mis en équivalence) (0,25) | 660 000 |
| Titres mis en équivalence | LIANTS D'OLT (0,25) | 1 260 000 |
| Autres créances – dont impôts différés actifs | néant après compensation par société (0,5 pour les deux lignes d'impôts différés) | 0 |

| Passif | Calcul | Montant |
|---|---|---:|
| Capital (entité consolidante) | SA ESCALDÈRE | 15 000 000 |
| Réserves et résultat consolidés | 22 449 000 + 4 357 250, tableau ci-dessus (réserves 0,75 ; résultat 0,75) | 26 806 250 |
| dont résultat net de l'exercice | | 4 357 250 |
| Écarts de conversion (autres capitaux propres) | 90 % × – 173 000 (0,25) | – 155 700 |
| **Capitaux propres (part du groupe)** | (0,25) | **41 650 550** |
| **Intérêts minoritaires** | 1 559 000 (GRANULATS DU LÉVÉZOU) + 346 200 (ESCALDÈRE MAROC) (0,5) | **1 905 200** |
| Autres dettes – dont impôts différés passifs | solde net par société | 266 250 |

- Les écarts de conversion sont présentés dans les capitaux propres part du groupe, au poste qui leur est propre [V art. 272-21, p. 61], dans la rubrique « autres » du modèle, à détailler dans l'analyse de la variation des capitaux propres de l'annexe [V art. 281-1, p. 66 ; F14 § 1.2] ; la part des minoritaires (– 17 300 €) est comprise dans les intérêts minoritaires.
- Les intérêts minoritaires forment une rubrique distincte des capitaux propres part du groupe, avant les provisions et les dettes [V art. 281-1, p. 66 ; F14 § 1.2].
- **Contrôle** : capitaux propres individuels des sociétés françaises (36 000 000 + 7 300 000 + 7 165 000) + capitaux propres convertis d'ESCALDÈRE MAROC (3 462 000) + retraitements nets (90 000 + 56 250 + 22 500 + 735 000 – 45 000 – 60 000 + 90 000) – titres éliminés ou mis en équivalence (13 760 000 + 90 000) + écart d'acquisition net (1 330 000) + titres mis en équivalence (1 260 000) = 43 555 750 € = 41 650 550 + 1 905 200.

#### b. Annexe consolidée et différence avec IAS 1 (2 pts)

**Annexe (1,5 pt).** L'annexe forme un tout avec le bilan et le compte de résultat ; elle mentionne le règlement ANC n° 2020-01 comme cadre, ne donne que les informations significatives et présente les chiffres de l'exercice précédent [V art. 111-4, p. 8 ; art. 282-1, p. 74 ; F14 § 1.1 et 1.4]. Pour le cas (0,5 pt par thème, trois thèmes au moins sur quatre) :
- **périmètre** : sociétés consolidées, pourcentages détenus et méthodes (intégration globale d'ENROBÉS DU VIAUR, d'ESCALDÈRE MAROC et de GRANULATS DU LÉVÉZOU ; mise en équivalence de LIANTS D'OLT), entrée de GRANULATS DU LÉVÉZOU au 01/01/2026 et ses effets sur les comptes [V art. 282-3 à 282-8, intitulés ; F14 § 1.4] ;
- **conversion** : méthode du cours de clôture appliquée à ESCALDÈRE MAROC, entité autonome dont la monnaie de fonctionnement est le dirham ; cours utilisés ; écart de conversion de l'exercice (– 138 000 €) et cumulé, présenté en capitaux propres et en intérêts minoritaires [V art. 282-2, intitulé ; F14 § 1.4 ; S pour le contenu] ;
- **coûts d'emprunt** : option d'incorporation au coût des actifs éligibles retenue par le groupe ; montant incorporé au coût de la centrale (200 000 €, dont 80 000 € en 2026) ; impôt différé passif correspondant [V art. 282-2, intitulé ; S pour le contenu] ;
- **écart d'acquisition de GRANULATS DU LÉVÉZOU** : calcul (coût de 7 000 000 €, frais nets d'impôt compris ; actif net réévalué de 7 000 000 € ; écarts d'évaluation), durée d'utilisation limitée de 20 ans et analyse qui la fonde (autorisation d'exploiter jusqu'en 2045), amortissement de 70 000 € et valeur nette de 1 330 000 € [V art. 282-19 à 282-30, explication des postes, intitulés ; F14 § 1.4].

**Différence avec IAS 1 (0,5 pt, une seule attendue).**
- Les **participations ne donnant pas le contrôle** seraient présentées **au sein des capitaux propres**, séparément des capitaux propres attribuables aux propriétaires de la société mère [V IAS 1 § 54 q) ; IFRS 10 § 22 ; F14 § 2.2], alors qu'en ANC les intérêts minoritaires forment une rubrique distincte ;
- ou : l'état de la situation financière distinguerait les éléments **courants et non courants** [V IAS 1 § 60 ; F14 § 2.2], là où le modèle ANC distingue l'actif immobilisé et l'actif circulant ;
- ou : les impôts différés figureraient sur des postes distincts [V IAS 1 § 54 ; F14 § 2.2] et ne seraient jamais classés en éléments courants [V IAS 1 § 56] ;
- ou : l'écart de conversion figurerait dans une composante des capitaux propres alimentée par les autres éléments du résultat global, l'état du résultat global présentant sa variation de l'exercice [V IAS 1 § 82A ; F14 § 2.3 et 4].

---

### Réponses tolérées
- **1.1** : réponse qui ajoute l'obligation de consolider, sans points supplémentaires.
- **1.2** : définition de l'actif tirée du seul cadre de 2018 ; argument fondé sur la pertinence plutôt que sur la comparabilité, s'il est relié au cas ; mention du goodwill hors frais non exigée.
- **1.3** : rapprochement des comptes réciproques placé après la conversion, s'il précède les éliminations ; écarts d'évaluation présentés avec les retraitements ; autre découpage en phases, si la conversion suit les retraitements en dirhams et précède le cumul, les éliminations et le partage.
- **1.4** : colonne des minoritaires laissée vide pour LIANTS D'OLT, ou portant 70 % si le candidat précise que la mise en équivalence ne fait apparaître aucun intérêt minoritaire.
- **1.5** : conversion présentée sur un seul tableau ; écart de 2026 analysé en deux lignes (capitaux propres d'ouverture, dividende compris : – 128 000 € ; résultat : – 10 000 €), si le calcul est juste ; écriture C1 fusionnée avec l'élimination des titres C13.
- **1.6** : intérêts incorporés enregistrés d'abord en immobilisations en cours puis virés au compte 2151 ; écriture de compte de résultat portant le crédit sur le compte 722 Production immobilisée – immobilisations corporelles plutôt que sur le compte 6611, si le résultat est le même.
- **1.7 a** : élimination des ventes portée sur 2 430 000 € avec le crédit de 30 000 € au compte 701, si l'avoir est traité ; élimination de la marge enregistrée sur le compte 6031 et le compte 31 en une seule écriture de bilan, si le résultat et l'impôt différé sont distingués.
- **1.7 b** : écriture unique éliminant 410 000 € de dette contre 380 000 € de créance et 30 000 € d'achats, si l'impôt différé est constaté ; candidat qui considère qu'ENROBÉS DU VIAUR corrigera ses comptes individuels et son impôt de 2026 (impôt exigible de 7 500 € au lieu d'un impôt différé), si l'hypothèse est écrite (`JUR-F08`).
- **1.9 c** : écriture de mise en équivalence sans les lignes de l'écart d'acquisition de LIANTS D'OLT (brut et amortissements égaux), si l'écart est expliqué en 1.9 b.
- **1.10 a** : impôts différés non compensés (20 000 € à l'actif, 286 250 € au passif) : 0,25 pt perdu ; écarts de conversion intégrés à la ligne « réserves et résultat consolidés » avec mention de leur montant.
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (erreur non sanctionnée deux fois).

### Erreurs fréquentes
- **Cadre conceptuel** : définitions récitées sans application aux deux traitements du cas ; coûts d'emprunt présentés comme interdits ou facultatifs en IFRS ; goodwill IFRS « amorti sur 20 ans » ; utilisateurs limités aux actionnaires.
- **Processus** : conversion placée après le partage, ou avant les retraitements faits dans la devise ; phases énumérées sans y rattacher les opérations du dossier (`JUR-G01`).
- **Périmètre** : contrôle exclusif retenu sur LIANTS D'OLT au motif d'une dépendance technique ; exclusion d'ESCALDÈRE MAROC parce qu'elle est étrangère.
- **Conversion** : capitaux propres convertis au cours de clôture ; résultat converti au cours de clôture ; dotations aux amortissements converties au cours historique (règle de l'autre méthode) ; dividende converti au cours moyen ; écart antérieur oublié dans le cumul, ou écart de 2026 confondu avec l'écart cumulé ; écart partagé à 100 % au groupe.
- **Coûts d'emprunt** : intérêts du second semestre 2026 incorporés après la mise en service ; amortissement complémentaire calculé sur 12 mois ; intérêts de 2025 portés en résultat de 2026 ; impôt différé oublié ou inversé ; tableau « comptes individuels / comptes consolidés » non présenté (`JUR-F05`, `JUR-G06`).
- **Opérations internes** : marge calculée sur le coût (320 000 × 25/125) au lieu du prix de vente ; élimination de la marge imputée au seul groupe ; avoir ignoré, d'où des soldes réciproques inégaux ; dividende éliminé pour 225 000 € (part des minoritaires comprise).
- **Coût d'acquisition et écart** : frais d'acquisition omis ou retenus pour leur montant brut (`JUR-G02`) ; impôt différé omis sur le terrain malgré l'hypothèse de l'énoncé ; écart d'acquisition jugé non amorti alors que l'autorisation d'exploiter borne la durée ; amortissement de l'écart partagé avec les minoritaires.
- **Partage et mise en équivalence** : minoritaires calculés sur les capitaux propres non réévalués ; capitaux propres d'ESCALDÈRE MAROC partagés en dirhams ; écart d'acquisition de LIANTS D'OLT ignoré dans les réserves consolidées (`JUR-G03`) ; écritures non équilibrées (`JUR-F04`).
- **Bilan consolidé** : titres de participation laissés à l'actif ; immobilisations d'ESCALDÈRE MAROC oubliées ; écarts de conversion de la part des minoritaires laissés dans les capitaux propres part du groupe ; intérêts minoritaires présentés dans les capitaux propres part du groupe ; impôts différés non compensés par société ; bilan présenté sans le calcul de chaque montant (`JUR-F02`).

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, contrôle, sens et mode d'évaluation des apports | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable ; `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 2,5 |
| 2.2 Régime fiscal de faveur | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 1,75 |
| 2.3 a) Parité, actions à rémunérer et à émettre, rompus, répartition du capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1,75 |
| 2.3 b) Soulte, plafond légal et équité | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 1,75 |
| 2.4 a) Actif net apporté, quotes-parts et prime de fusion | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 1 |
| 2.4 b) Mali, décomposition et affectation du mali technique | `1.2.e` Calculer et analyser le boni ou mali de fusion | 4,5 |
| 2.5 a) Écritures chez SABLIÈRES DU CÉLÉ | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 1,5 |
| 2.5 b) Augmentation de capital, soulte et réalisation des apports chez BÉTONS DE BOURIANE | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 2 |
| 2.5 c) Vrai mali, annulation des titres et mali technique | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes | 2,5 |
| 2.5 d) Frais de fusion | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 0,75 |
| 2.5 e) Suivi du mali technique en 2026 et retraitements fiscaux | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes (suivi du mali technique à la clôture de l'année de l'opération) | 3 |
| 2.6 Note au directeur général | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Qualification, contrôle et mode d'évaluation des apports (2,5 pts)

**Qualification et référentiel (1 pt)**
- L'opération est une **fusion-absorption** : SABLIÈRES DU CÉLÉ transmet l'ensemble de son patrimoine, actif et passif, à BÉTONS DE BOURIANE (**transmission universelle**) ; elle est **dissoute sans liquidation** ; ses associés reçoivent des actions BÉTONS DE BOURIANE émises par augmentation de capital, complétées d'une soulte en numéraire [V PCG art. 710-2, renvoi à C. com. L. 236-1, F01 § 1] (0,5 pt).
- L'absorbante détient déjà 70 % du capital de l'absorbée. Elle ne peut pas se remettre ses propres actions : les 14 000 actions SABLIÈRES DU CÉLÉ qu'elle détient ne sont pas échangées, elles sont annulées. Seuls les associés autres que l'absorbante sont rémunérés ; l'apport comprend donc une **quote-part rémunérée (30 %)** et une **quote-part non rémunérée (70 %)** [V C. com. L. 236-3 II 1° ; BOI-IS-FUS-10-20-40-10 § 340, F01 § 5.1] (0,25 pt).
- L'enregistrement relève, dans les comptes individuels des deux sociétés, du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe la valeur d'inscription des apports et le traitement du mali [V art. 710-1 et 720-1, F01 § 1]. La parité, elle, se calcule sur les valeurs d'échange fournies, quelle que soit la valeur d'inscription des apports [V art. 740-1, F01 § 1] (0,25 pt).

**Situation de contrôle (0,5 pt).** BÉTONS DE BOURIANE détient 70 % des droits de vote de SABLIÈRES DU CÉLÉ, sans accord entre actionnaires : elle la contrôle **de manière exclusive** (majorité des droits de vote). L'une des sociétés participantes contrôle l'autre avant l'opération : l'opération est réalisée **sous contrôle commun** [V PCG art. 741-1 et 741-2, F01 § 2.1]. Le contrôle s'apprécie entre les deux personnes morales ; il est indifférent que BÉTONS DE BOURIANE soit elle-même contrôlée par des personnes physiques.

**Sens de l'opération (0,25 pt).** La famille LABORIE détient 65 % de l'absorbante avant la fusion et 62,65 % après (voir 2.3 a) : l'actionnaire principal de l'absorbante, faiblement dilué, **conserve le contrôle** ; la fusion est **à l'endroit** [V art. 742-1, F01 § 2.2]. Les associés de l'absorbée, eux, ne détiennent que 3,61 % de l'absorbante.

**Mode d'évaluation (0,75 pt).** Sous contrôle commun, les apports sont évalués à la **valeur comptable**, que l'opération soit à l'endroit ou à l'envers : il s'agit d'un renforcement du contrôle, sans prise de contrôle, et il convient de ne pas réévaluer [V art. 743-1, cas 1, F01 § 2.3]. Le sens de l'opération ne change donc pas le résultat (0,5 pt). Les apports sont repris pour leurs valeurs au bilan du 30/06/2026 : valeurs brutes, amortissements et provisions [V art. 744-2, F01 § 3.2]. L'actif net comptable apporté (1 200 000 €) est positif et largement supérieur à l'augmentation de capital (225 000 €) : l'exception qui imposerait les valeurs réelles en cas d'actif net comptable insuffisant ne joue pas [V art. 743-3, F01 § 2.4] (0,25 pt).

---

### 2.2 Régime fiscal de faveur (1,75 pt)

- *Conditions (0,25 pt).* Les deux sociétés sont soumises à l'impôt sur les sociétés. Le régime de faveur s'applique à la fusion, sauf option pour le droit commun, si l'absorbante prend dans le traité les engagements de l'art. 210 A-3 du CGI ; BÉTONS DE BOURIANE les prend (annexe 2.4) [V CGI art. 210 A et 210 C-1 ; BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1 et § 4].
- *Chez SABLIÈRES DU CÉLÉ (0,75 pt).*
  - Les plus-values latentes sur les éléments apportés (terrain, installation de traitement, clientèle) ne sont pas soumises à l'impôt [V 210 A-1, F02 § 2] ; l'apport étant comptabilisé à la valeur comptable, aucune plus-value n'est d'ailleurs constatée (0,25 pt).
  - Le bénéfice du premier semestre 2026 (200 000 €) est imposé immédiatement chez l'absorbée, quel que soit le régime : l'impôt correspondant est déjà comptabilisé en dettes fiscales et transmis à l'absorbante [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2] (0,25 pt).
  - La provision pour remise en état, déduite et toujours justifiée, n'est pas réintégrée : son imposition est différée ; BÉTONS DE BOURIANE la reprend à son passif et ne la réintégrera que si elle devient sans objet [V 210 A-2 et 210 A-3-a, F02 § 2 et § 4] (0,25 pt).
- *Chez BÉTONS DE BOURIANE (0,75 pt).*
  - Elle reprend les valeurs fiscales de l'absorbée. Pour le terrain, immobilisation non amortissable, la plus-value d'une cession ultérieure sera calculée d'après sa valeur fiscale chez SABLIÈRES DU CÉLÉ (90 000 €) [V 210 A-3-c, F02 § 2] ; l'installation de traitement continue d'être amortie sur sa valeur d'origine ; aucune plus-value n'est à réintégrer, puisque les biens amortissables sont apportés à leur valeur comptable [V BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2] (0,5 pt).
  - Le **mali technique** ne peut donner lieu à aucune déduction, ni lors de sa constatation ni ultérieurement : ses amortissements et la part qui sort avec un actif cédé sont réintégrés au résultat fiscal [V 210 A-1, F02 § 2]. Le vrai mali n'est pas déductible non plus (hypothèse de l'annexe 2.6) (0,25 pt).

---

### 2.3 Parité, nombre d'actions et soulte (3,5 pts)

**a) Parité, actions à rémunérer et à émettre, répartition du capital (1,75 pt)**
- Valeurs unitaires : BÉTONS DE BOURIANE 14 400 000 / 60 000 = **240 €** ; SABLIÈRES DU CÉLÉ 1 860 000 / 20 000 = **93 €**. Parité exacte : 93 / 240 = **31 / 80**, soit 31 actions BÉTONS DE BOURIANE pour 80 actions SABLIÈRES DU CÉLÉ [V méthode du corrigé du sujet zéro, F01 § 4] (0,5 pt).
- Actions à rémunérer : 20 000 – 14 000 = **6 000**, celles de la famille VIGUIÉ ; les 14 000 actions de l'absorbante sont annulées (voir 2.1) (0,25 pt).
- Rompus (0,25 pt) : à la parité exacte, Mme Odile VIGUIÉ aurait droit à 3 200 × 31 / 80 = 1 240 actions, mais M. Thomas VIGUIÉ et Mme Léa VIGUIÉ à 1 400 × 31 / 80 = **542,5 actions** chacun : leurs droits ne correspondent pas à un nombre entier d'actions (1 400 n'est pas un multiple de 80). Le projet de traité retient une parité arrondie, **3 pour 8**, et compense l'écart par une soulte ; chaque associé détient un multiple de 8 actions : il ne reste aucun rompu.
- Actions à émettre : 6 000 × 3 / 8 = **2 250 actions** (1 200 pour Mme Odile VIGUIÉ, 525 pour chacun de ses enfants) ; augmentation de capital : 2 250 × 100 = **225 000 €** (0,25 pt).
- Répartition du capital après la fusion (60 000 + 2 250 = **62 250 actions**) (0,5 pt) :

| Actionnaire | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| Famille LABORIE | 39 000 | 65,00 % | 39 000 | 62,65 % |
| Autres actionnaires | 21 000 | 35,00 % | 21 000 | 33,73 % |
| Mme Odile VIGUIÉ | – | – | 1 200 | 1,93 % |
| M. Thomas VIGUIÉ | – | – | 525 | 0,84 % |
| Mme Léa VIGUIÉ | – | – | 525 | 0,84 % |
| **Total** | **60 000** | **100 %** | **62 250** | **100 %** |

(Total des pourcentages arrondis : 99,99 %.)

Chaque action donnant une voix, les droits de vote suivent la même répartition. La famille VIGUIÉ détient 3,61 % de BÉTONS DE BOURIANE ; la famille LABORIE garde la majorité.

**b) Soulte, plafond légal et équité (1,75 pt)**
- *Soulte (0,5 pt).* Par action SABLIÈRES DU CÉLÉ rémunérée : 93 – 3 / 8 × 240 = 93 – 90 = **3 €** ; soulte totale : 6 000 × 3 = **18 000 €** (9 600 € pour Mme Odile VIGUIÉ, 4 200 € pour chacun de ses enfants). Elle compense les 75 actions que la parité arrondie ne remet pas : (2 325 – 2 250) × 240 = 18 000 €.
- *Contrainte légale (0,75 pt).* La soulte en espèces ne peut pas dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-1, F01 § 4] : 10 % × 2 250 × 100 = **22 500 €**. La soulte de 18 000 € représente 80 % du plafond : **elle est légale**.
- *Équité (0,5 pt).* Valeur des actions remises + soulte = 2 250 × 240 + 18 000 = 558 000 € = valeur des actions reçues (6 000 × 93) [V méthode du corrigé du sujet zéro, F01 § 4]. Aucun groupe d'actionnaires ne s'enrichit au détriment de l'autre.

---

### 2.4 Apports et mali (5,5 pts)

**a) Actif net apporté, quotes-parts et prime de fusion (1 pt)**
- Actif net apporté à la valeur comptable = actifs – provisions et dettes = 1 780 000 – 580 000 = **1 200 000 €**, égal aux capitaux propres de SABLIÈRES DU CÉLÉ au 30/06/2026 (0,25 pt).
- Quote-part rémunérée (30 %) : **360 000 €** ; quote-part non rémunérée (70 %) : **840 000 €** [V F01 § 5.1] (0,25 pt).
- Prime de fusion = quote-part rémunérée – augmentation de capital – soulte = 360 000 – 225 000 – 18 000 = **117 000 €** [V F01 § 4 et § 9] (0,5 pt).

**b) Mali, décomposition et affectation (4,5 pts)**

**Résultat d'annulation des titres (0,75 pt).** Quote-part non rémunérée de l'actif net reçu – valeur comptable des titres annulés = 840 000 – 1 400 000 = **– 560 000 €**, soit un **mali** de 560 000 € [V PCG art. 745-3, F01 § 5.3]. Il apparaît parce que BÉTONS DE BOURIANE a payé ses titres plus cher que la quote-part de l'actif net comptable qu'elle reçoit.

**Valeur de la clientèle (0,75 pt).** Selon l'expert (annexe 2.3), valeur des actions = actif net comptable + plus-values + clientèle – engagements de retraite. D'où : clientèle (fonds commercial non inscrit) = 1 860 000 – (1 200 000 + 160 000 + 200 000 – 60 000) = 1 860 000 – 1 500 000 = **360 000 €**, avec des plus-values de 250 000 – 90 000 = 160 000 € sur le terrain et de 650 000 – 450 000 = 200 000 € sur l'installation de traitement.

**Mali technique (1 pt).** Il correspond, à hauteur de la participation, aux plus-values latentes sur les actifs apportés, comptabilisés ou non (y compris le fonds commercial), déduction faite des passifs non comptabilisés faute d'obligation comptable [V PCG art. 745-4, F01 § 5.3] :

| Élément | Montant à 100 % | Quote-part de 70 % |
|---|---:|---:|
| Plus-value sur le terrain | 160 000 | 112 000 |
| Plus-value sur l'installation de traitement | 200 000 | 140 000 |
| Fonds commercial (clientèle) | 360 000 | 252 000 |
| Engagements de départ à la retraite non provisionnés | – 60 000 | – 42 000 |
| **Mali technique** | **660 000** | **462 000** |

La plus-value du terrain est retenue pour son montant brut : au 1er juillet 2026, BÉTONS DE BOURIANE entendait le conserver (annexe 2.3) ; l'offre d'achat, reçue en septembre et non sollicitée, est postérieure à l'opération. Le terrain n'était donc pas un actif destiné à être revendu à brève échéance, dont la plus-value aurait été retenue nette d'impôt [V art. 745-4] (0,25 pt, compris). Les engagements de retraite restent un passif non comptabilisé : BÉTONS DE BOURIANE ne provisionne pas les siens, aucun ajustement n'est à faire sur les apports [V art. 744-3, F01 § 3.2].

**Vrai mali (0,75 pt).** Vrai mali = mali – mali technique = 560 000 – 462 000 = **98 000 €**. Contrôle : coût des titres – 70 % de la valeur des actions SABLIÈRES DU CÉLÉ = 1 400 000 – 70 % × 1 860 000 = 1 400 000 – 1 302 000 = **98 000 €**, soit 14 000 × (100 – 93). C'est la **dépréciation de la participation** devenue nécessaire après le refus de prolonger l'autorisation d'exploiter le site de la Combe (mars 2026) ; elle n'avait pas lieu d'être au 31/12/2025, la valeur d'utilité (1 470 000 €) excédant alors le coût. Le vrai mali est comptabilisé **en résultat financier** de l'exercice 2026 [V art. 745-4, F01 § 5.3].

**Affectation du mali technique (1 pt).** Le mali technique (462 000 €) excède la quote-part des plus-values latentes sur les actifs identifiés autres que le fonds commercial (112 000 + 140 000 = 252 000 €) : chacun de ces actifs reçoit sa quote-part de plus-value, et le reste est affecté au fonds commercial [V art. 745-5, F01 § 5.4].

| Actif sous-jacent | Mali affecté | Compte |
|---|---:|---|
| Terrain (parcelle des Cazals) | 112 000 | 2187 Mali de fusion sur actifs corporels |
| Installation de traitement | 140 000 | 2187 Mali de fusion sur actifs corporels |
| Fonds commercial (462 000 – 252 000) | 210 000 | 2081 Mali de fusion sur actifs incorporels |
| **Total** | **462 000** | |

La part du fonds commercial vaut 70 % × (360 000 – 60 000) : la déduction des engagements de retraite s'impute sur le résidu.

**Autre composante (0,25 pt).** Le vrai mali (98 000 €) n'est pas inscrit à l'actif : il est enregistré en charge financière, au compte **6866** Dotations pour dépréciation des éléments financiers, par une dépréciation des titres (compte 2961) annulée avec eux [V art. 745-4, F01 § 9].

---

### 2.5 Écritures (9,75 pts)

**a) Chez SABLIÈRES DU CÉLÉ, le 1er juillet 2026 (1,5 pt)**

L'apport étant évalué à la valeur comptable, la créance sur l'absorbante est égale à l'actif net comptable : la fusion ne dégage **aucun résultat** chez SABLIÈRES DU CÉLÉ.

**A1 — Transmission de l'actif et du passif (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – BÉTONS DE BOURIANE, compte d'apport | 1 200 000 | |
| 28131 Amortissements des bâtiments | 180 000 | |
| 28153 Amortissements des installations à caractère spécifique | 450 000 | |
| 28154 Amortissements des matériels industriels | 360 000 | |
| 1526 Provisions pour remise en état | 60 000 | |
| 164 Emprunts auprès des établissements de crédit | 300 000 | |
| 401 Fournisseurs | 120 000 | |
| 43 Sécurité sociale et autres organismes sociaux | 55 000 | |
| 44 État et autres collectivités publiques | 45 000 | |
| 2111 Terrains nus | | 90 000 |
| 2131 Bâtiments | | 300 000 |
| 2153 Installations à caractère spécifique | | 900 000 |
| 2154 Matériels industriels | | 640 000 |
| 355 Produits finis | | 140 000 |
| 411 Clients | | 420 000 |
| 512 Banques | | 280 000 |
| **Total** | **2 770 000** | **2 770 000** |

**A2 — Droits des associés sur l'actif net (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 400 000 | |
| 1061 Réserve légale | 40 000 | |
| 1068 Autres réserves | 560 000 | |
| 120 Résultat de l'exercice – bénéfice (01/01 au 30/06/2026) | 200 000 | |
| 456 Associés – Opérations sur le capital (BÉTONS DE BOURIANE, 70 %) | | 840 000 |
| 456 Associés – Opérations sur le capital (famille VIGUIÉ, 30 %) | | 360 000 |

**A3 — Partage entre les associés (0,25 pt).** BÉTONS DE BOURIANE remet directement les 2 250 actions nouvelles et la soulte à la famille VIGUIÉ (annexe 2.4) ; ses propres droits s'éteignent par l'annulation de ses titres.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital (famille VIGUIÉ) | 360 000 | |
| 456 Associés – Opérations sur le capital (BÉTONS DE BOURIANE) | 840 000 | |
| 467 Divers comptes débiteurs – BÉTONS DE BOURIANE, compte d'apport | | 1 200 000 |

Après A1 à A3, tous les comptes de SABLIÈRES DU CÉLÉ sont soldés.

**b) Chez BÉTONS DE BOURIANE, le 1er juillet 2026 : augmentation de capital et apports (2 pts)**

**A4 — Augmentation de capital et soulte (1 pt).** Seule la quote-part rémunérée (30 %) passe par l'augmentation de capital.

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (30 % × 1 200 000) | 360 000 | |
| 101 Capital (2 250 × 100) | | 225 000 |
| 1042 Primes de fusion | | 117 000 |
| 512 Banques (soulte : 6 000 × 3) | | 18 000 |

**A5 — Réalisation des apports à la valeur comptable (1 pt).** Valeurs brutes, amortissements et provisions repris de l'absorbée [V art. 744-2, F01 § 3.2].

| Compte | Débit | Crédit |
|---|---:|---:|
| 2111 Terrains nus | 90 000 | |
| 2131 Bâtiments | 300 000 | |
| 2153 Installations à caractère spécifique | 900 000 | |
| 2154 Matériels industriels | 640 000 | |
| 355 Produits finis | 140 000 | |
| 411 Clients | 420 000 | |
| 512 Banques | 280 000 | |
| 28131 Amortissements des bâtiments | | 180 000 |
| 28153 Amortissements des installations à caractère spécifique | | 450 000 |
| 28154 Amortissements des matériels industriels | | 360 000 |
| 1526 Provisions pour remise en état | | 60 000 |
| 164 Emprunts auprès des établissements de crédit | | 300 000 |
| 401 Fournisseurs | | 120 000 |
| 43 Sécurité sociale et autres organismes sociaux | | 55 000 |
| 44 État et autres collectivités publiques | | 45 000 |
| 4561 Associés – Comptes d'apport en société | | 1 200 000 |
| **Total** | **2 770 000** | **2 770 000** |

**c) Vrai mali, annulation des titres et mali technique (2,5 pts)**

**A6 — Vrai mali (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 6866 Dotations pour dépréciation des éléments financiers | 98 000 | |
| 2961 Dépréciations des titres de participation | | 98 000 |

**A7 — Annulation des titres et mali technique (1,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (70 % × 1 200 000) | 840 000 | |
| 2961 Dépréciations des titres de participation | 98 000 | |
| 2187 Mali de fusion sur actifs corporels (terrain) | 112 000 | |
| 2187 Mali de fusion sur actifs corporels (installation de traitement) | 140 000 | |
| 2081 Mali de fusion sur actifs incorporels (fonds commercial) | 210 000 | |
| 261 Titres de participation (14 000 actions SABLIÈRES DU CÉLÉ) | | 1 400 000 |
| **Total** | **1 400 000** | **1 400 000** |

Après A4, A5 et A7, le compte 4561 est soldé (360 000 + 840 000 = 1 200 000). Le capital s'élève à 6 225 000 €, soit 62 250 actions de 100 €.

**d) Frais de fusion (0,75 pt)**

Les frais de fusion peuvent être inscrits à l'actif ou imputés sur la prime de fusion [V PCG art. 212-9, F01 § 7] ; BÉTONS DE BOURIANE choisit l'imputation, pour leur montant net d'impôt [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 40 000 × 75 % = **30 000 €** ; l'économie d'impôt (10 000 €) diminue l'impôt sur les sociétés de 2026. La prime (117 000 €) est suffisante.

**A8 — Frais de fusion**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (40 000 × 75 %) | 30 000 | |
| 444 État – Impôts sur les bénéfices (40 000 × 25 %) | 10 000 | |
| 512 Banques | | 40 000 |

SABLIÈRES DU CÉLÉ n'ayant ni provisions réglementées ni subvention d'investissement, aucune reconstitution n'est à passer ; il n'existe aucune dette réciproque à éteindre (annexe 2.1).

**e) Suivi du mali technique en 2026 et retraitements fiscaux (3 pts)**

Chaque quote-part du mali technique suit le traitement de l'actif sous-jacent [V art. 745-7 et 745-10, annexe 2.5, F01 § 5.5].

**A9 et A10 — Cession du terrain le 16 novembre 2026 (1 pt).** La quote-part du mali affectée au terrain sort avec lui [V art. 745-10].

A9 :

| Compte | Débit | Crédit |
|---|---:|---:|
| 512 Banques | 270 000 | |
| 757 Produits des cessions d'immobilisations incorporelles et corporelles | | 270 000 |

A10 :

| Compte | Débit | Crédit |
|---|---:|---:|
| 657 Valeurs comptables des immobilisations incorporelles et corporelles cédées | 202 000 | |
| 2111 Terrains nus | | 90 000 |
| 2187 Mali de fusion sur actifs corporels (terrain) | | 112 000 |

Résultat comptable de cession : 270 000 – (90 000 + 112 000) = **68 000 €**.

**A11 — Amortissement de la part affectée à l'installation, au 31/12/2026 (0,75 pt).** L'installation est amortie en linéaire, et il lui reste 5 ans d'utilisation au 01/07/2026 : 140 000 / 5 × 6 / 12 = **14 000 €** pour le second semestre. L'amortissement de l'installation elle-même (900 000 / 10 × 6 / 12 = 45 000 €) est déjà comptabilisé.

| Compte | Débit | Crédit |
|---|---:|---:|
| 6811 Dotations aux amortissements sur immobilisations incorporelles et corporelles | 14 000 | |
| 28187 Amortissement du mali de fusion sur actifs corporels | | 14 000 |

**Fonds commercial (0,5 pt).** La part du mali affectée au fonds commercial (210 000 €) suit les règles du fonds commercial, présumé avoir une durée d'utilisation non limitée : elle n'est pas amortie [V PCG art. 214-3, annexe 2.5, F01 § 5.5]. Aucun indice de perte de valeur n'étant relevé au 31/12/2026, aucune dépréciation n'est à comptabiliser.

**Retraitements fiscaux de l'exercice 2026 (0,75 pt)** [V CGI art. 210 A-1 et 210 A-3-c, F02 § 2] :
- réintégration de l'amortissement du mali (14 000 €), non déductible ;
- plus-value fiscale de cession du terrain = 270 000 – 90 000 (valeur fiscale chez l'absorbée) = **180 000 €**, soit le résultat comptable (68 000 €) majoré de la part du mali sortie (112 000 €), réintégrée ; impôt correspondant : 180 000 × 25 % = **45 000 €** ;
- réintégration du vrai mali (98 000 €), non déductible (hypothèse de l'annexe 2.6).

Au total, 14 000 + 112 000 + 98 000 = **224 000 €** sont réintégrés au résultat fiscal de 2026. Les frais de fusion, imputés sur la prime et donc absents du résultat comptable, sont déduits extra-comptablement (40 000 €), d'où l'économie d'impôt de 10 000 € (A8).

---

### 2.6 Note à M. LABORIE, directeur général de BÉTONS DE BOURIANE (2 pts)

**Capitaux propres juste après la fusion (1 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (62 250 actions × 100) | 6 000 000 | + 225 000 | 6 225 000 |
| Primes de fusion | 0 | + 117 000 – 30 000 | 87 000 |
| Réserve légale | 600 000 | | 600 000 |
| Autres réserves | 3 150 000 | | 3 150 000 |
| **Total, hors résultat de l'exercice** | **9 750 000** | **+ 312 000** | **10 062 000** |

Contrôle : + 312 000 = quote-part rémunérée des apports (360 000) – soulte (18 000) – frais nets d'impôt (30 000), soit + 3,20 %. La quote-part non rémunérée (840 000 €) n'augmente pas les capitaux propres : elle remplace les titres annulés. Le vrai mali (98 000 €) diminue en outre le résultat de l'exercice dès le 1er juillet. Barème : capital et prime (0,5), total et contrôle (0,5).

**Effets sur le résultat de l'exercice 2026 (0,5 pt)**
- vrai mali : – 98 000 € en résultat financier, non déductible ;
- amortissement du mali sur l'installation : – 14 000 €, non déductible ;
- cession du terrain : + 68 000 € de résultat comptable, mais une plus-value fiscale de 180 000 €, soit 45 000 € d'impôt, car la part du mali sortie (112 000 €) n'est pas déductible ;
- soit un effet de – 44 000 € avant impôt et de – 89 000 € après l'impôt sur la cession, sans compter l'activité de la sablière, intégrée au résultat de BÉTONS DE BOURIANE à partir du 1er juillet. Il reste à l'actif 336 000 € de mali technique (126 000 € sur l'installation, net d'amortissement, et 210 000 € sur le fonds commercial), exposés à un risque de dépréciation si la sablière perd d'autres sites.

**Répartition du capital (0,5 pt).** Seules les 6 000 actions de la famille VIGUIÉ sont rémunérées ; la sablière pèse peu au regard de BÉTONS DE BOURIANE : la dilution est limitée. La famille LABORIE passe de 65 % à **62,65 %** et garde la majorité ; les autres actionnaires passent de 35 % à 33,73 % ; la famille VIGUIÉ, désormais actionnaire de BÉTONS DE BOURIANE, en détient **3,61 %**. L'échange étant équitable, aucun actionnaire n'est appauvri ; la soulte (18 000 €) ne pèse guère sur la trésorerie.

---

### Réponses tolérées
- **2.1** : sens de l'opération non étudié, si le candidat justifie que le contrôle commun impose la valeur comptable quel que soit le sens (0,25 point perdu).
- **2.3 a** : parité exprimée en nombre décimal (0,3875 action pour une action), si elle est exacte.
- **2.4 b** : présentation du mali technique par différence entre la valeur des actions et l'actif net comptable, à hauteur de 70 % (70 % × (1 860 000 – 1 200 000) = 462 000 €), si la clientèle est ensuite déterminée pour l'affectation.
- **2.5 a** : réception des actions et de la soulte par SABLIÈRES DU CÉLÉ, puis attribution aux associés (comptes 503 ou 508 et 512), si le candidat écrit l'hypothèse ; comptes 431 et 444 ou 447 au lieu de 43 et 44.
- **2.5 b** : soulte portée au crédit d'un compte de tiers (468) puis versée par une écriture distincte.
- **2.5 c** : vrai mali enregistré directement dans A7 (débit 6866, crédit 261) au lieu du passage par 2961 : présentation abrégée admise [F01 § 9].
- **2.5 d** : frais en deux écritures (1042 / 512 pour 40 000 €, puis 444 / 1042 pour 10 000 €), ou passage préalable en 6226 Honoraires puis transfert sur la prime par le crédit du compte de charge, si la prime ne supporte que 30 000 €.
- **2.5 e** : A9 et A10 réunies en une seule écriture.
- **2.6** : toute présentation chiffrée et cohérente des trois points.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion mal calculée : oubli de la soulte (135 000 €), prime calculée sur la valeur d'échange de la quote-part rémunérée (30 % × 1 860 000 – 225 000 – 18 000 = 315 000 €) alors que les apports sont à la valeur comptable, ou prime calculée sur la totalité de l'actif net apporté.
- `JUR-R02` Mali non décomposé ; mali technique calculé à 100 % des plus-values (660 000 €) au lieu de 70 % ; vrai mali non expliqué par la dépréciation des titres.
- `JUR-R04` Suivi du mali mal traité alors que l'annexe 2.5 donne la règle : amortissement du mali sur 12 mois (28 000 €) ou sur la durée d'origine de l'installation ; part du mali affectée au terrain laissée à l'actif après la cession ; mali affecté au fonds commercial amorti.
- `JUR-R05` Difficulté à s'adapter : 7 500 actions émises (20 000 × 3 / 8), comme si l'absorbante pouvait se remettre ses propres actions ; apports évalués à la valeur réelle parce que la fusion est à l'endroit, alors que le contrôle commun impose la valeur comptable.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1, A5 et A7.
- `JUR-F07` Annexes mal exploitées : plus-value du terrain retenue nette d'impôt, alors que la cession n'était pas envisagée au 1er juillet ; engagements de retraite oubliés dans le calcul de la clientèle puis déduits du mali technique (clientèle de 300 000 € et mali technique de 420 000 €, vrai mali de 140 000 €) ; frais imputés pour leur montant brut (prime finale de 77 000 €).
- Erreurs propres à ce cas :
  - plafond de la soulte calculé sur le nominal des actions SABLIÈRES DU CÉLÉ ou sur la valeur des apports, au lieu du nominal des actions BÉTONS DE BOURIANE attribuées ;
  - résultat de fusion constaté chez SABLIÈRES DU CÉLÉ alors que l'apport est à la valeur comptable ;
  - plus-value fiscale de cession calculée sur la valeur comptable du terrain majorée du mali (68 000 €), comme si le mali était déductible.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 710-1, 710-2, 720-1, 740-1 | Champ du titre VII, définition de la fusion, inscription des apports, parité indépendante de leur évaluation | [V] p. 81-82 | F01 § 1 |
| PCG art. 741-1, 741-2, 742-1, 743-1, 743-3 | Contrôle commun, fusion à l'endroit, valeur comptable (cas 1), exception de l'actif net insuffisant | [V] p. 82-85 | F01 § 2 |
| PCG art. 744-2, 744-3 ; BOI-IS-FUS-10-20-40-20 § 170-180 | Apports à la valeur comptable, reprise des valeurs brutes et des amortissements ; ajustement des engagements de retraite | [V] p. 85-86 | F01 § 3.2 |
| C. com. L. 236-1 et L. 236-3 II ; BOI-IS-FUS-10-20-40-10 § 340 | Soulte limitée à 10 % du nominal des actions attribuées ; non-échange des actions détenues par l'absorbante | [V] Légifrance | F01 § 4 et § 5.1 |
| Corrigé du sujet zéro (parité) | Parité réduite ; équité de l'échange | [V] p. imprimée 214 | F01 § 4 |
| PCG art. 745-3, 745-4, 745-5, 745-6 ; comptes 2081, 2187, 6866, 2961 | Mali, mali technique et vrai mali, affectation, comptes spécifiques | [V] p. 86-87, 135-146 | F01 § 5.3, § 5.4 et § 9 |
| PCG art. 745-7, 745-10, 214-3 ; comptes 28187, 657, 757 | Suivi du mali technique : amortissement, sortie avec l'actif cédé ; fonds commercial non amorti | [V] p. 22-23, 87, 137, 145, 148 | F01 § 5.5 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime de fusion, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| CGI art. 210 A-1, 210 A-2, 210 A-3 (a et c), 210 C-1 ; BOI-IS-FUS-10-10-10 § 10 et 20 ; BOI-IS-FUS-10-20-30 § 210 et 330 | Régime de faveur : exonération chez l'absorbée, provisions, valeur fiscale des immobilisations non amortissables, mali technique non déductible, imposition du résultat de la dernière période | [V] | F02 § 1, § 2 et § 4 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Désignation du commissaire aux comptes d'une société contrôlée par une tête de petit groupe ; obligation de la holding ; durée et expiration d'un mandat de trois exercices | `3.1.b` Nomination et cessation | 3 |
| 3.2 Responsabilité civile de l'expert-comptable et du commissaire aux comptes : fondement, conditions, assurance, prescription ; certification et absence de garantie | `3.1.e` Mise en cause de la responsabilité ; `3.1.a` Cadres d'exercice professionnel | 2,5 |
| 3.3 Objectif de la certification et assurance raisonnable ; risque d'anomalies significatives et assertions du cycle ventes et créances | `3.2.a` Notion d'audit et typologie des missions ; `3.2.c` Approche par les risques | 4,5 |
| 3.4 Application d'un extrait de NEP aux estimations comptables ; recalcul d'une dépréciation ; procédures ; refus des demandes de confirmation et procédures alternatives | `3.1.d` Référentiel normatif (NEP) ; `3.2.d` Démarche d'audit ; `3.2.b` Moyens d'action du CAC | 5 |
| 3.5 Récapitulation des anomalies ; écritures ; opinion selon les corrections ; note de synthèse | `3.2.e` Portée des opinions ; `3.2.d` Démarche d'audit (supports) ; `3.2.c` Caractère significatif | 3 |
| 3.6 Définition du reporting de durabilité et place par rapport aux autres reportings ; acteurs et référentiels | `3.3.b` Principes de construction du reporting ; `3.3.a` Contexte et architecture des normes de durabilité | 3 |
| 3.7 Exigences générales et principes de publication : manquements du projet d'état | `3.3.b` Principes de construction du reporting | 3 |
| 3.8 Objectifs de la mission, assurance limitée, axes et axes sans objet | `3.4.a` Objectifs de la mission et nature de l'assurance | 2 |
| 3.9 Étapes de la démarche et procédures sur les manquements | `3.4.b` Démarche | 2,5 |
| 3.10 Conclusions par axe et structure du rapport | `3.4.c` Portée des avis | 1,5 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Désignation du commissaire aux comptes dans un petit groupe (3 pts)

**a. LIGNEVIAL et ORBIPANNEAUX (1,25 pt)**

*Droit commun (0,25 pt)* : une SAS doit désigner au moins un commissaire aux comptes si elle dépasse, à la clôture d'un exercice, deux des trois seuils suivants : total du bilan de 5 000 000 €, chiffre d'affaires hors taxes de 10 000 000 €, 50 salariés en moyenne [V L. 227-9-1 al. 2 ; D. 221-5, rendu applicable par D. 227-1]. LIGNEVIAL n'en dépasse aucun, ni en 2024 (3 870 000 € ; 7 650 000 € ; 43 salariés), ni en 2025, ni en 2026 (4 640 000 € ; 9 200 000 € ; 48 salariés). Le droit commun ne l'obligeait donc pas à désigner un commissaire aux comptes.

*Règle du petit groupe (0,75 pt)*
- AUBRAMONT Participations **contrôle** LIGNEVIAL et ORBIPANNEAUX, dont elle détient toutes les actions [V L. 233-3, auquel renvoie L. 821-43]. Elle n'est pas astreinte à publier des comptes consolidés et n'est pas une entité d'intérêt public (hypothèses de l'énoncé) ; elle est contrôlée par des personnes physiques, qui n'ont pas désigné de commissaire aux comptes. L'exception prévue pour une tête de groupe elle-même contrôlée par une entité dotée d'un commissaire aux comptes ne joue donc pas [V L. 821-43 al. 1-2].
- L'ensemble qu'elle forme avec ses deux filiales dépassait déjà les seuils de droit commun en cumul au 31/12/2024 (annexe 3.1), comme en 2025 et en 2026 (question b). AUBRAMONT est donc une **tête de petit groupe**.
- Une société contrôlée par une telle tête de groupe doit désigner au moins un commissaire aux comptes si elle dépasse deux des trois **seuils réduits** : total du bilan de 2 500 000 €, chiffre d'affaires hors taxes de 5 000 000 €, 25 salariés [V L. 821-43 al. 3 ; D. 821-172 al. 1].
- LIGNEVIAL dépassait les trois seuils réduits en 2024 (3 870 000 € > 2 500 000 € ; 7 650 000 € > 5 000 000 € ; 43 > 25 salariés). La désignation du 26/06/2025, par l'associé unique qui statuait sur les comptes de 2024, était donc **obligatoire**. LIGNEVIAL les dépasse encore en 2025 et en 2026.

*ORBIPANNEAUX (0,25 pt)* : elle reste sous les seuils réduits en 2025 (1 860 000 € ; 3 580 000 € ; 21 salariés) comme en 2026 (2 140 000 € ; 4 060 000 € ; 23 salariés). Elle n'est pas tenue de désigner un commissaire aux comptes ; elle peut le faire volontairement [V L. 227-9-1 al. 1 ; D. 821-172].

**b. AUBRAMONT Participations (1 pt)**
- Prise isolément, la holding reste loin des seuils de droit commun (3 280 000 € ; 450 000 € ; 3 salariés en 2026). Le président raisonne sur ses seuls chiffres : c'est l'erreur.
- La tête d'un petit groupe doit désigner au moins un commissaire aux comptes lorsque **l'ensemble** qu'elle forme avec les sociétés qu'elle contrôle dépasse deux des trois seuils de droit commun, appréciés **en cumul**. Le cumul s'obtient en **additionnant** les chiffres des sociétés de l'ensemble [V L. 821-43 al. 1 ; D. 821-171 al. 1-2].

| Ensemble AUBRAMONT | Total du bilan | Chiffre d'affaires | Salariés | Seuils dépassés |
|---|---:|---:|---:|---:|
| 2025 | 9 130 000 | 12 380 000 | 70 | 3 sur 3 |
| 2026 | 10 060 000 | 13 710 000 | 74 | 3 sur 3 |
| Seuils | 5 000 000 | 10 000 000 | 50 | |

- Le texte prévoit une simple addition, sans élimination des titres de participation ni des redevances facturées aux filiales. La conclusion ne change pas si l'on retranche ces montants : 7 460 000 € de total du bilan et 13 260 000 € de chiffre d'affaires en 2026.
- **Réponse au président** : AUBRAMONT Participations doit désigner un commissaire aux comptes. L'obligation existe depuis la clôture de 2024 : la holding est en situation irrégulière et doit désigner un commissaire aux comptes sans attendre, si possible avant l'approbation des comptes de 2026 afin qu'ils soient certifiés [S]. Ses associés peuvent limiter le mandat à **trois exercices** [V L. 821-46]. Le rapport sur les risques financiers, comptables et de gestion porte alors sur l'**ensemble** formé avec les filiales [V L. 821-57 al. 1]. Un même commissaire aux comptes peut être désigné pour la holding et pour LIGNEVIAL [V L. 821-43 al. 3, dernière phrase]. Le cabinet ORMIÈRES ne pourrait accepter qu'après avoir vérifié son indépendance et ses ressources [V L. 821-4 II]. Les sanctions du défaut de désignation ne sont pas à développer.

**c. Durée et expiration du mandat chez LIGNEVIAL (0,75 pt)**
- **Durée (0,25 pt)** : le mandat de droit commun est de six exercices [V L. 821-44 al. 1]. La société peut le limiter à **trois exercices** lorsque la désignation est volontaire ou fondée sur le premier ou le dernier alinéa de L. 821-43 [V L. 821-46]. C'est le cas de LIGNEVIAL, désignée au titre du dernier alinéa. Le mandat couvre les exercices 2025, 2026 et 2027 ; il expire après la décision de l'associé unique qui statuera sur les comptes de 2027, en 2028 [S, application de L. 821-44 al. 1 à la durée de trois exercices]. Le cabinet remet, outre son rapport sur les comptes, un rapport aux dirigeants sur les risques financiers, comptables et de gestion [V L. 821-57].
- **À l'expiration (0,5 pt)** : LIGNEVIAL ne cessera d'être tenue d'avoir un commissaire aux comptes que si elle n'a pas dépassé deux des trois seuils réduits **pendant les deux exercices précédant l'expiration du mandat**, soit 2026 et 2027 [V D. 821-172 al. 2]. Elle les dépasse en 2026 : l'obligation subsistera en 2028, quels que soient ses chiffres de 2027.
  - Si le budget 2027 **ne se réalise pas** et que LIGNEVIAL reste sous les seuils de droit commun, la désignation restera fondée sur la règle du petit groupe (si AUBRAMONT en reste la tête). L'associé unique pourra de nouveau choisir trois ou six exercices [V L. 821-46].
  - Si le budget **se réalise**, LIGNEVIAL dépassera à la clôture de 2027 deux seuils de droit commun : chiffre d'affaires de 10 400 000 € > 10 000 000 € et 52 salariés > 50 (le total du bilan, 4 950 000 €, restant en deçà). La désignation de 2028 sera alors **imposée par le droit commun** [V L. 227-9-1 al. 2 ; D. 221-5]. Elle n'entrera plus dans les cas de L. 821-46 : le mandat sera de **six exercices**, sans rapport sur les risques et sans la dispense de diligences du mandat de trois exercices [V L. 821-44 al. 1, L. 821-46, L. 821-57 ; S, application].

**Réponses tolérées**
- En 3.1 a, une réponse qui ne vérifie pas expressément l'exception de L. 821-43 al. 2 : 0,5 pt sur 0,75.
- En 3.1 b, un cumul calculé après élimination des opérations réciproques, si la conclusion est exacte.
- En 3.1 c, une analyse qui ne retient que l'un des deux scénarios, si la règle des deux exercices précédant l'expiration est appliquée : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Appliquer à LIGNEVIAL les seuils de droit commun, ou apprécier ceux de la holding sur ses seuls comptes (`JUR-A05`).
- Retenir six exercices pour le mandat en cours, ou trois exercices pour un mandat imposé par le droit commun (`JUR-A05`).
- Croire que l'obligation cesse dès que les seuils ne sont plus dépassés une année (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 227-9-1, D. 221-5, D. 227-1 | Seuils de droit commun d'une SAS | [V] | F09 § 3.3 |
| C. com. L. 821-43, D. 821-171, D. 821-172 ; L. 233-3 | Tête de petit groupe ; cumul ; seuils réduits ; fin de l'obligation ; même commissaire aux comptes | [V] ; application au cas : [S] | F09 § 3.3, § 13 |
| C. com. L. 821-44, L. 821-46, L. 821-57, L. 821-4 II | Durée de six ou trois exercices ; rapport sur les risques ; acceptation | [V] ; application : [S] | F09 § 3.4-3.5, § 13 |

### 3.2 Responsabilité civile de l'expert-comptable et du commissaire aux comptes (2,5 pts)

*Comparaison (1,25 pt : fondement et conditions 0,5 ; assurance 0,25 ; prescription 0,5)*

| | FONTCLAIRE Expertise (expert-comptable) | Cabinet ORMIÈRES (commissaire aux comptes) |
|---|---|---|
| Fondement | Les experts-comptables assument la responsabilité de leurs travaux et activités ; la responsabilité de la société d'expertise comptable laisse subsister celle de l'expert-comptable pour les travaux qu'il exécute [V ord. 45-2138 art. 12 al. 3]. Envers LIGNEVIAL, sa cliente, la responsabilité est **contractuelle** (inexécution de la lettre de mission) ; envers des tiers, elle serait délictuelle [V C. civ. 1231-1 et 1240 ; S, application à l'expert-comptable] | Responsabilité **légale**, envers l'entité **et les tiers**, pour les conséquences dommageables des **fautes et négligences** commises dans l'exercice de la profession [V L. 821-37 al. 1] ; pas de responsabilité du fait des informations données en exécution de la mission, ni des infractions des dirigeants, sauf si, les connaissant, il ne les a pas signalées [V L. 821-37 al. 2-3] |
| Conditions | Une **faute**, un **préjudice** certain et un **lien de causalité** entre les deux [S, droit commun] | Les mêmes [S] ; la faute s'apprécie au regard des diligences que doit accomplir un commissaire aux comptes, et non au regard du seul résultat |
| Assurance | **Obligatoire** ; garantie minimale de 500 000 € par sinistre et de 1 000 000 € par année d'assurance et par assuré [V ord. art. 17 ; décret 2012-432 art. 138] | **Obligatoire** : le commissaire aux comptes inscrit doit être couvert par une assurance garantissant sa responsabilité, dans les limites fixées par arrêté [V R. 821-85 ; R. 821-109 pour les sociétés] |
| Prescription | Droit commun : **cinq ans** à compter du jour où le titulaire du droit a connu ou aurait dû connaître les faits [V C. civ. 2224 ; S, faute de texte spécial] : erreur découverte en juin 2026, action possible jusqu'en juin 2031 | **Trois ans** à compter du fait dommageable ou, s'il a été dissimulé, de sa révélation [V L. 821-38, renvoyant à L. 225-254] : rapport du 14/04/2026, action possible jusqu'au 14/04/2029 [S, application] |

*FONTCLAIRE Expertise (0,5 pt)*
- **Faute** : avoir enregistré deux fois les mêmes factures est un manquement à l'exécution de la mission de tenue et d'établissement des comptes confiée par contrat [S, application].
- **Préjudice** : il est limité.
  - Les 1 800 € HT facturés pour corriger sa propre erreur peuvent être refusés ou réclamés.
  - L'impôt supplémentaire acquitté au titre de 2025 sur 30 000 € de produits fictifs n'est pas une perte définitive : la correction de 2026 réduit d'autant le résultat imposable de 2026. Seul le coût de cette avance de trésorerie est un préjudice [S].
  - Le chantier retiré par GARRIGUE ENROBÉS : les 40 000 € sont un chiffre d'affaires, et non une perte. Le préjudice serait au plus la marge perdue. Encore faut-il prouver le **lien de causalité** entre l'erreur et ce retrait, alors que les relances relevaient de la gestion de LIGNEVIAL : il s'agirait au mieux d'une perte de chance [S].
- **Conclusion** : une action contractuelle est possible, dans les délais ; son enjeu est modeste. Une demande amiable, que FONTCLAIRE transmettra à son assureur, paraît plus adaptée.

*Cabinet ORMIÈRES et portée de la certification (0,75 pt)*
- Le commissaire aux comptes certifie que les comptes sont réguliers et sincères et donnent une image fidèle [V L. 821-53]. Il obtient une **assurance raisonnable**, élevée mais **non absolue**, que les comptes **pris dans leur ensemble** ne comportent pas d'**anomalies significatives**. Ses travaux reposent sur des sondages, et les éléments collectés conduisent davantage à des présomptions qu'à des certitudes [V NEP principes § 04, 08-09]. La certification ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55].
- Les comptes sont établis par FONTCLAIRE et arrêtés par le président ; le commissaire aux comptes ne s'immisce pas dans la gestion [V L. 821-54 I]. Il ne répond pas des travaux de l'expert-comptable.
- L'erreur de 30 000 € représente 66,7 % du seuil de signification de 2025 (45 000 €) : ce n'est pas une anomalie significative. Ne pas l'avoir détectée n'établit pas une faute : il faudrait prouver que le cabinet n'a pas accompli les diligences requises, par exemple sur la séparation des exercices des produits de décembre [S, déduction de NEP principes § 08-09 ; F09 § 7.1].
- **Conclusion** : une action contre le cabinet a très peu de chances d'aboutir. Le cabinet répond avec objectivité, sans conseiller le président sur une action dirigée contre lui-même : le président peut consulter un avocat [S].

**Réponses tolérées**
- L'omission des montants de garantie de l'assurance, si son caractère obligatoire est indiqué pour les deux professionnels.
- Une analyse du préjudice fiscal qui le rejette sans parler de l'avance de trésorerie.

**Erreurs fréquentes**
- Confondre responsabilité civile, pénale et disciplinaire, ou développer des sanctions pénales hors sujet (`JUR-A01`).
- Présenter la certification comme une garantie de l'absence de toute erreur (`JUR-A01`, `JUR-A06`).
- Appliquer au commissaire aux comptes la prescription de cinq ans, ou à l'expert-comptable celle de trois ans (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 12, 17 ; décret 2012-432 art. 138 ; C. civ. 1231-1, 1240, 2224 | Responsabilité de l'expert-comptable ; assurance ; prescription | [V] ; application : [S] | F09 § 7.1 |
| C. com. L. 821-37, L. 821-38, L. 225-254, R. 821-85, R. 821-109 | Responsabilité du commissaire aux comptes ; prescription ; assurance | [V] | F09 § 7.1, § 13 |
| C. com. L. 821-53, L. 821-54 I, L. 821-55 ; NEP principes § 04, 08-09 | Objectif ; non-immixtion ; assurance raisonnable | [V] ; absence de garantie : [S] | F11 § 1.1 ; F09 § 6 |

### 3.3 Notion d'audit et approche par les risques du cycle ventes et créances (4,5 pts)

**a. Objectif de la certification et assurance raisonnable (1 pt)**
- **Objectif (0,5 pt)** : le commissaire aux comptes certifie, en justifiant de ses appréciations, que les comptes annuels sont **réguliers et sincères** et donnent une **image fidèle** du résultat de l'exercice, de la situation financière et du patrimoine. Il exprime une **opinion**, après avoir mis en œuvre un audit des comptes [V L. 821-53 al. 1 ; NEP principes § 01]. C'est une mission légale, distincte des prestations, comme celle que le cabinet réalise sur les informations de durabilité [V L. 821-2 III-IV].
- **Assurance raisonnable (0,5 pt)** : elle est élevée, mais non absolue du fait des limites de l'audit (sondages, limites des procédures de l'entité, éléments qui conduisent à des présomptions plutôt qu'à des certitudes). Elle porte sur les comptes pris dans leur ensemble et sur l'absence d'**anomalies significatives** : une information inexacte, insuffisante ou omise qui, seule ou cumulée, peut influencer le jugement de l'utilisateur [V NEP principes § 04, 08-09]. L'opinion est formulée de manière **positive**.

**b. Risque d'anomalies significatives et assertions (3,5 pts)** [V NEP principes § 10-13 ; NEP risques § 02, 39-41 ; NEP éléments probants § 9]

*Évaluation du risque (0,5 pt)* : le **risque inhérent** est élevé.
- Le cycle repose sur des **estimations** et des jugements de la direction : factures à établir de fin d'année, dépréciation des créances.
- Le contexte crée une **pression sur le résultat** : candidature au contrat-cadre du Département le 30/04/2027, déclaration du président qui refuse de « dégrader » le résultat. Ce sont des indices de biais et des facteurs de risque de fraude.
- Des événements accroissent le risque : redressement judiciaire d'un client le 11/12/2026, chantiers reportés par la pluie, avoirs émis en janvier, erreur de double enregistrement en 2025.
- Les procédures de l'entité sont faibles : les factures à établir sont recensées à partir des tableaux des chefs d'équipe et enregistrées par FONTCLAIRE « sans autre contrôle ». Le risque lié au contrôle est élevé.
- Sans test de l'efficacité des procédures, le risque au niveau des assertions correspond au risque inhérent [V NEP risques § 41]. Le cabinet met en œuvre des **procédures de substance** et privilégie les éléments externes : attachements signés des clients, procès-verbaux, encaissements [V NEP réponses § 03-13].

*Risques et assertions (3 pts : 0,25 pt par couple pertinent, dans la limite de douze)*

| Élément | Risque | Assertion |
|---|---|---|
| Chiffre d'affaires (flux) | Travaux de la zone d'activités du Roc-Blanc, exécutés en janvier 2027, comptabilisés en factures à établir de 2026 | **Séparation des exercices** ; **réalité** |
| | Facture à établir du Département calculée sur le bon de commande (160 000 €) et non sur l'attachement (148 000 €) | **Mesure** ; **réalité** de la section non exécutée |
| | Travaux facturés ou à établir sans attachement signé ni procès-verbal | **Réalité** |
| | Travaux exécutés en décembre non recensés par les chefs d'équipe | **Exhaustivité** |
| | Quantités facturées deux fois (situation de Roquefagne ; erreur de 2025) | **Réalité** ; **mesure** |
| Réductions sur ventes (flux) | Avoirs de janvier 2027 relatifs à des ventes de 2026 non comptabilisés à la clôture | **Exhaustivité** ; **séparation des exercices** |
| | Remise de 2027 rattachée à tort à 2026 | **Séparation des exercices** |
| Créances (soldes) | Factures à établir qui ne correspondent à aucune créance à la clôture | **Existence** |
| | Créances sur TERRALDÈS TP, en redressement judiciaire, insuffisamment dépréciées | **Évaluation et imputation** |
| | Retenues de garantie de TERRALDÈS TP exclues de la dépréciation et maintenues au compte 4117 | **Évaluation et imputation** ; **présentation** (classement en clients douteux) |
| | Créances publiques aux délais de 90 à 150 jours : existence à établir, absence de dépréciation à justifier | **Existence** ; **évaluation** |
| | Dépréciation forfaitaire des créances anciennes sur les entreprises | **Évaluation et imputation** |
| Présentation et annexe | Avoirs à établir et retenues de garantie mal classés ; méthode de dépréciation et échéances des créances non décrites | **Présentation et intelligibilité** ; **exhaustivité** |

**Réponses tolérées**
- D'autres couples risque-assertion pertinents tirés des annexes.
- Le classement de la facture à établir du Roc-Blanc sous la seule réalité, ou sous la seule séparation des exercices.

**Erreurs fréquentes**
- Confondre réalité (flux) et existence (solde), ou exhaustivité et séparation des exercices (`JUR-A01`).
- Lister des risques généraux sans les rattacher aux données du cas (`JUR-A05`, `JUR-F07`).
- Présenter l'assurance raisonnable comme une certitude (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-2, L. 821-53 ; NEP principes § 01, 04, 08-13 | Objectif ; assurance raisonnable ; risque d'audit | [V] | F11 § 1, 4.1 |
| NEP risques § 02, 39-41 ; NEP réponses § 03-13 ; NEP éléments probants § 9 | Facteurs de risque ; assertions ; procédures de substance | [V] | F11 § 4.1, 4.3, 5 |

### 3.4 Estimations comptables, procédures et demandes de confirmation (5 pts)

**a. Application de l'extrait de norme à la dépréciation des créances (1,5 pt)** [V NEP estimations § 01, 05, 07-09, 14, 16-21, 26-28]

*Qualification (0,25 pt)* : la dépréciation est une **estimation comptable**, un montant dont l'évaluation comporte une incertitude. La direction l'établit par une **méthode** (taux forfaitaires par catégorie de clients), des **hypothèses** (0 %, 25 %, 50 %, exclusion des retenues de garantie) et des **données** (balance âgée, situation juridique des clients). Le taux de perte sur TERRALDÈS TP est une **hypothèse importante** : une variation de 10 points modifie la dépréciation de 20 200 € (10 % de 202 000 € HT), soit 40,4 % du seuil de signification. L'incertitude est forte et la direction montre des indices de biais : le risque inhérent est élevé.

*Appréciation par catégorie de clients (1 pt)*

| Catégorie | Méthode et hypothèse de la direction | Éléments collectés | Appréciation |
|---|---|---|---|
| Département et communes | Aucune dépréciation | Encaissements postérieurs : 780 000 € sur 900 000 € (86,7 %) et 270 000 € sur 312 000 € (86,5 %) ; soldes non encaissés non échus au 28/02/2027 | **Raisonnable** : le dénouement confirme l'hypothèse. Des délais longs ne traduisent pas un risque de non-recouvrement de clients publics |
| Entreprises, créances échues depuis plus de 180 jours | 25 % de 40 000 € HT, soit 10 000 € | Dénouement de 2025 : perte de 6 000 € sur 60 000 € HT dépréciés à 25 %, soit 10,0 % ; en 2027, 36 000 € TTC encaissés sur 48 000 €, il reste 12 000 € TTC, soit 10 000 € HT | **Raisonnable**, plutôt prudente : la dépréciation couvre le solde non encaissé |
| TERRALDÈS TP | 50 % des factures HT, retenues exclues : 90 000 € | Redressement judiciaire du 11/12/2026, avant la clôture ; lettre du mandataire du 15/01/2027 : recouvrement espéré de 20 % ; retenues de 22 000 € HT sur le même client | **Non raisonnable** (question b) |

- **Hypothèse** : le taux de 50 % n'a jamais été confronté à un dénouement, puisque aucun client n'était en procédure collective en 2025. Il est **infirmé** par un événement postérieur à la clôture, la lettre du mandataire, qui éclaire une situation existant au 31/12/2026, le redressement du 11/12/2026. La norme prévoit de collecter de tels éléments, et la dépréciation compare la valeur nette à la valeur actuelle **à la clôture** [V NEP estimations § 16-17 ; PCG art. 214-25 ; S, application].
- **Données** : exclure les retenues de garantie n'est pas approprié. Ce sont des créances sur le même client, exposées au même risque (annexe 3.4), et non une garantie au profit de LIGNEVIAL. La totalité des créances sur ce client doit d'ailleurs figurer au compte 416 [V PCG art. 1214-41].
- **Biais** : « notre règle depuis toujours », refus de tenir compte de la lettre, refus de « dégrader » le résultat avant la candidature. Ces jugements présentent des **indices de biais**, que le cabinet apprécie avec esprit critique [V NEP estimations § 07, 19, 26].

*Conséquences (0,25 pt)* : le cabinet demande à la direction de revoir son estimation. À défaut, il établit **sa propre estimation** (question b) et en déduit une anomalie [V NEP estimations § 21, 23, 27]. Il obtient une **déclaration écrite** sur les méthodes, les données et les hypothèses importantes, et communique son appréciation au président [V § 28-29].

**b. Dépréciation de la créance sur TERRALDÈS TP (1 pt)** [V PCG art. 214-25 ; S, application]

| TERRALDÈS TP | Projet de comptes | Estimation du cabinet |
|---|---:|---:|
| Factures échues (HT) | 180 000 | 180 000 |
| Retenues de garantie (HT) | exclues | 22 000 |
| **Base dépréciable (HT)** | **180 000** | **202 000** |
| Taux de perte | 50 % | 80 % (recouvrement espéré de 20 %) |
| **Dépréciation au 31/12/2026** | **90 000** | **161 600** |
| **Insuffisance** | | **71 600** |

- La dépréciation est calculée sur les montants hors taxes (convention de l'énoncé).
- L'insuffisance de **71 600 €** représente **143,2 %** du seuil de signification : c'est, à elle seule, une **anomalie significative**. La dépréciation totale du compte 491 passe de 100 000 € à 171 600 €.

**c. Procédures sur les ventes, les factures à établir et les créances (1,5 pt)** [V NEP éléments probants § 10 ; NEP confirmations § 4-5, 7, 9, 13]
- **Réalité et séparation des factures à établir (0,5 pt)** :
  - rapprochement de chaque facture à établir avec l'attachement signé ou le procès-verbal de réception, le bon de commande et le bordereau de prix ;
  - contrôle des dates d'exécution par les plannings, les relevés d'heures et les bons de sortie des produits. Il fait apparaître que les travaux du Roc-Blanc ont été exécutés en janvier 2027 et que l'attachement du Département ne porte que sur 148 000 € ;
  - test de séparation sur les attachements et les factures de décembre 2026 et de janvier 2027 ;
  - pour l'exhaustivité, recherche des travaux de décembre dans les plannings et vérification qu'ils sont facturés ou inscrits en factures à établir.
- **Avoirs (0,25 pt)** : revue des avoirs émis en janvier et en février 2027, et jusqu'à la date du rapport. L'avoir de Roquefagne (18 000 €) se rattache à 2026 : le cabinet vérifie l'avoir à établir du compte 4198. La remise à VOIRANDE TP (4 000 €) porte sur 2027 : aucune écriture en 2026. Le cabinet vérifie aussi qu'aucune double facturation ne subsiste.
- **Demandes de confirmation (0,25 pt)** : demandes adressées par le cabinet, qui en garde la maîtrise, à l'échantillon d'entreprises (dont TERRALDÈS TP et VOIRANDE TP). Elles portent sur les soldes, les retenues de garantie et les travaux exécutés en décembre non facturés. Une réponse de VOIRANDE TP confirmerait qu'aucun travail n'a été exécuté en 2026. Ces demandes établissent l'**existence** des créances, mais ne permettent généralement pas de conclure sur leur **évaluation**. En l'absence de réponse, le cabinet met en œuvre des procédures alternatives, comme l'examen des encaissements postérieurs.
- **Évaluation (0,25 pt)** : analyse de la balance âgée ; rapprochement des encaissements de janvier et février 2027 avec les relevés bancaires et les avis de paiement ; lecture de la déclaration de créances et de la lettre du mandataire ; recalcul de la dépréciation ; examen du dénouement de 2025.
- **Procédures analytiques et présentation (0,25 pt)** : comparaison du chiffre d'affaires mensuel (pic de décembre), du délai de paiement moyen et de la marge par chantier avec 2025 ; contrôle du classement des créances sur TERRALDÈS TP, retenues comprises, au compte 416, et des informations de l'annexe.

**d. Position du président sur les demandes de confirmation (1 pt)**
- **Moyens d'action (0,25 pt)** : le commissaire aux comptes procède à toute époque aux vérifications qu'il juge opportunes et se fait communiquer sur place toutes les pièces utiles [V L. 821-60]. Il peut recueillir des informations auprès des tiers qui ont accompli des opérations pour le compte de l'entité [V L. 821-61 al. 2] ; des clients n'entrent pas dans ce cas. La demande de confirmation est une technique de collecte d'éléments, dont il garde la **maîtrise** : choix des tiers, rédaction, envoi et réception [V NEP éléments probants § 10 ; NEP confirmations § 9].
- **Appréciation du refus (0,5 pt)** : lorsque la direction s'oppose à une demande, le commissaire aux comptes examine si le refus se fonde sur des **motifs valables** et collecte sur ces motifs des éléments suffisants et appropriés [V NEP confirmations § 10].
  - Le motif invoqué est vérifiable : la consultation a été publiée le 04/01/2027 et les candidatures sont attendues le 30/04/2027.
  - Il ne vise que des clients publics, pour lesquels le risque sur l'existence et sur l'évaluation est faible et des éléments externes de qualité existent.
  - Dans ces circonstances, le cabinet peut le juger **valable** pour le Département et les communes, à condition de documenter son appréciation [S, application].
  - Le refus ne s'étend pas aux entreprises : le cabinet maintient ses demandes, notamment à TERRALDÈS TP et à VOIRANDE TP.
- **Procédures alternatives (0,25 pt)** [V NEP confirmations § 11 ; NEP éléments probants § 6] :
  - inspection des attachements et des procès-verbaux signés par les représentants des clients publics, et des bons de commande : c'est ainsi qu'apparaît l'écart de 12 000 € sur le Département ;
  - rapprochement des encaissements de janvier et février 2027 avec les avis de paiement du comptable public : 780 000 € et 270 000 € ;
  - examen des factures non échues et des contrats.

  Ces éléments sont externes et probants : ils suffisent, et il n'en résulte aucune limitation. Si le cabinet jugeait le motif non valable, ou ces éléments insuffisants, il en tirerait les conséquences dans son rapport : une réserve pour limitation, circonscrite aux créances publiques [V NEP confirmations § 12 ; NEP rapport § 11].

**Réponses tolérées**
- En a, une appréciation globale de la méthode, si le candidat exploite le dénouement de 2025, les encaissements postérieurs et la lettre du mandataire.
- En b, une base qui omet les retenues de garantie (dépréciation de 144 000 €, insuffisance de 54 000 €), si le taux de 80 % est justifié : 0,5 pt sur 1.
- En d, un motif jugé non valable, si le candidat justifie son appréciation et propose les mêmes procédures alternatives ou en tire les conséquences sur l'opinion.

**Erreurs fréquentes**
- Réciter l'extrait de norme sans l'appliquer aux données du cas (`JUR-G09`, `JUR-A06`).
- Calculer la dépréciation sur le montant TTC, ou maintenir la règle forfaitaire malgré la lettre du mandataire (`JUR-A05`).
- Accepter le refus du président sans examiner son motif, ou l'étendre à tous les clients (`JUR-A05`).
- Croire que la confirmation suffit à justifier l'évaluation des créances (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP estimations § 01-03, 05-09, 13-21, 23, 26-29 | Méthode, hypothèses, données ; dénouement ; événements postérieurs ; biais ; estimation propre ; déclarations écrites | [V] ; application : [S] | F11 § 17.1 |
| PCG art. 214-25 (p. 27), 1214-41 (p. 164-165), 1214-49 (p. 172) | Dépréciation des créances ; comptes 4117, 416 et 418 ; comptes 49 | [V] ; application : [S] | F11 § 17.2 |
| C. com. L. 821-60, L. 821-61 ; NEP confirmations § 4-5, 7, 9-13 ; NEP éléments probants § 6, 10 | Moyens d'action ; confirmations ; refus de la direction ; procédures alternatives | [V] ; application : [S] | F11 § 2, 6.1-6.3, 15.2 |

### 3.5 Anomalies, écritures, opinion et note de synthèse (3 pts)

**a. Récapitulation et caractère significatif (0,75 pt)** [V NEP anomalies § 8, 11-12, 14 ; NEP caractère significatif § 9]

| Anomalie | Résultat 2026 | Créances clients nettes | TVA sur factures à établir (passif) |
|---|---:|---:|---:|
| A1 Facture à établir du Roc-Blanc (travaux de janvier 2027) | − 96 000 | − 115 200 | − 19 200 |
| A2 Facture à établir du Département (quantités du bon de commande) | − 12 000 | − 14 400 | − 2 400 |
| A3 Dépréciation insuffisante des créances sur TERRALDÈS TP | − 71 600 | − 71 600 | — |
| **Total** | **− 179 600** | **− 201 200** | **− 21 600** |

- Toutes dépassent le seuil des anomalies manifestement insignifiantes (2 500 €) : elles sont récapitulées. Rapportées au seuil de signification de 50 000 € : 192,0 % (A1), 24,0 % (A2), 143,2 % (A3). A1 et A3 sont significatives à elles seules.
- Le seuil est réapprécié au vu des comptes corrigés [V NEP anomalies § 13] : 5 % du résultat courant corrigé (820 400 €) donnent 41 020 €. A1 (96 000 €) et A3 (71 600 €) restent significatives à elles seules, A2 (12 000 €) reste en deçà : la conclusion ne change pas.
- Leur **cumul**, 179 600 €, représente **359,2 %** du seuil et **18,0 %** du résultat courant avant impôt du projet. Après correction, ce résultat serait de 820 400 €.
- Leur **nature** aggrave le constat. Toutes majorent le résultat, à l'approche d'une candidature, et A3 résulte d'un choix de la direction qui présente des indices de biais.
- L'erreur de 2025 a été corrigée en 2026 et vérifiée : elle ne laisse aucun effet à récapituler.
- Le cabinet communique ces anomalies au président et lui demande de les corriger [V NEP anomalies § 11].

**b. Écritures de correction au 31/12/2026 (0,75 pt : 0,25 pt par écriture)**

X1 – Annulation de la facture à établir de la zone d'activités du Roc-Blanc (travaux exécutés en janvier 2027)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 704 | Travaux | 96 000 | |
| 44587 | Taxes sur le chiffre d'affaires sur factures à établir | 19 200 | |
| 4181 | Clients - Factures à établir | | 115 200 |

X2 – Ramener la facture à établir du Département à l'attachement du 30/12/2026 (160 000 − 148 000)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 704 | Travaux | 12 000 | |
| 44587 | Taxes sur le chiffre d'affaires sur factures à établir | 2 400 | |
| 4181 | Clients - Factures à établir | | 14 400 |

X3 – Dépréciation complémentaire des créances sur TERRALDÈS TP (161 600 − 90 000)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 68174 | Dotations pour dépréciations des créances | 71 600 | |
| 491 | Dépréciations des comptes de clients | | 71 600 |

X4 – Virement des retenues de garantie de TERRALDÈS TP au compte des clients douteux (correction de présentation, sans effet sur le résultat)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| 416 | Clients douteux ou litigieux | 26 400 | |
| 4117 | Clients - Retenues de garantie | | 26 400 |

**c. Opinion sur les comptes annuels de 2026 (1 pt : 0,25 pt par situation, 0,25 pt pour les motifs et la forme)** [V NEP rapport § 06, 08-12 ; C. com. R. 821-180]

| Le président corrige | Anomalies non corrigées | Opinion |
|---|---|---|
| Toutes les anomalies | Aucune, les autres cycles ne présentant que des anomalies manifestement insignifiantes | **Certification sans réserve**, les procédures alternatives sur les clients publics ayant permis de conclure |
| Seulement les factures à établir (A1, A2) | A3 : 71 600 €, soit 143,2 % du seuil | **Certification avec réserve pour désaccord** : anomalie significative, mais circonscrite à une créance identifiée et chiffrée |
| Aucune | A1 à A3 : 179 600 €, soit 359,2 % du seuil et 18,0 % du résultat courant | **Certification avec réserve pour désaccord** : les incidences sont chiffrées et limitées au cycle ventes et créances. Une réserve suffit à éclairer l'utilisateur ; le refus de certifier n'est pas justifié |

- **Motifs et forme** : la réserve est motivée dans la partie « Fondement de l'opinion », avec les incidences chiffrées : résultat et capitaux propres surévalués de 179 600 € (ou de 71 600 €), créances surévaluées de 201 200 € (ou de 71 600 €), dettes de TVA sur factures à établir surévaluées de 21 600 €. Les motifs sont communiqués au préalable au président [V NEP rapport § 06, 09-10 ; L. 821-63 I].
- Dans tous les cas, le cabinet obtient une déclaration écrite du président, avec l'état des anomalies non corrigées [V NEP anomalies § 17 ; NEP déclarations écrites § 6-7]. La justification des appréciations peut porter sur la dépréciation des créances.

**d. Note de synthèse du cycle (0,5 pt)** [S, F11 § 7 ; NEP anomalies § 18]
- Seuils de signification, de planification et des anomalies manifestement insignifiantes ; risques identifiés et assertions ; travaux réalisés : rapprochement des factures à établir, test de séparation, revue des avoirs, demandes de confirmation et procédures alternatives, recalcul de la dépréciation (0,25 pt).
- Anomalies chiffrées, communiquées au président, corrigées ou non ; refus des confirmations publiques, appréciation de son motif et procédures alternatives ; points de jugement : taux de recouvrement, retenues de garantie, indices de biais ; conclusion sur le cycle et incidence sur l'opinion ; points à reprendre dans la déclaration écrite et dans le rapport sur les risques remis au président, comme la faiblesse du recensement des factures à établir (0,25 pt).

**Réponses tolérées**
- Les écritures X1 et X2 présentées en une seule écriture, si les montants sont exacts.
- L'absence de l'écriture X4, si le candidat signale le classement des retenues en clients douteux.
- Un refus de certifier en l'absence de toute correction, si le candidat soutient avec le critère de circonscription que la nature des anomalies (biais, candidature) rend la réserve insuffisante : 0,25 pt sur 0,5 pour les deux dernières situations.

**Erreurs fréquentes**
- Conclure sans apprécier le cumul et la nature des anomalies (`JUR-A02`, `JUR-A06`).
- Ajouter la TVA ou les créances au cumul des anomalies de résultat (`JUR-F06`).
- Écritures sans intitulés ni libellés, ou déséquilibrées ; dépréciation passée au compte 6876 sans justification (`JUR-F03`, `JUR-F04`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP anomalies § 8, 11-12, 14, 17-18 ; NEP caractère significatif § 9 | Récapitulation, cumul, nature, déclaration écrite, documentation | [V] | F11 § 4.2, 14.1 |
| NEP rapport § 06, 08-12 ; C. com. R. 821-180, L. 821-63 I ; NEP déclarations écrites § 6-7 | Opinions ; désaccord ; communication | [V] | F11 § 8, 12.3 |
| Note de synthèse ; rapport sur les risques (L. 821-57) | Contenu | [S] ; L. 821-57 : [V] | F11 § 7 ; F09 § 13 |
| Liste des comptes du PCG 2026 : 704, 4117, 416, 4181, 44587, 491, 68174 | Écritures | [V] | F11 § 17.2 |

---

### Partie B – Durabilité (12 points)

### 3.6 Définition et place du reporting de durabilité ; acteurs (3 pts)

**a. Définition et place par rapport aux autres reportings (2 pts)**
- **Définition (0,5 pt)** : le reporting de durabilité réunit les informations qui permettent de comprendre les **impacts** de l'activité de l'entreprise sur les enjeux environnementaux, sociaux et de gouvernance, ainsi que la manière dont ces enjeux influent sur l'évolution de ses affaires, de ses résultats et de sa situation [V L. 232-6-3 I ; S, application à une publication volontaire]. C'est la **double matérialité** : d'impact et financière [V ESRS 1 (2026) § 35-36]. Selon les ESRS, l'état de durabilité, pris dans son ensemble, donne une **image fidèle** des impacts, risques et opportunités matériels et de la manière dont l'entreprise les gère. Il s'adresse aux investisseurs et aux prêteurs comme aux autres utilisateurs : partenaires commerciaux tels que le Département, salariés, société civile [V ESRS 1 (2026) § 3-4]. Il figure dans une **section distincte du rapport de gestion**, clairement séparée des autres informations [V ESRS 1 (2026) § 104].
- **Reporting financier (0,5 pt)** : les comptes annuels et le rapport de gestion de LIGNEVIAL décrivent l'activité, les résultats, la situation financière et les perspectives : c'est un reporting tourné vers les effets sur l'entreprise. L'état de durabilité y ajoute ses impacts sur les personnes et l'environnement, sécurité des équipes et produits de marquage par exemple. Sa matérialité financière prolonge celle des états financiers sans se limiter aux entités contrôlées [V ESRS 1 (2026) § 46]. Il porte sur la même période [V § 76] et reste **connecté** aux comptes : renvois, cohérence des données et des hypothèses [V § 112-116].
- **Reporting social (0,5 pt)** : le rapport de gestion de LIGNEVIAL donne déjà l'effectif et les heures de formation. Ce sont des données sociales isolées. Le reporting de durabilité couvre les thèmes sociaux (personnel de l'entreprise, travailleurs de la chaîne de valeur, communautés, consommateurs) **lorsqu'ils sont matériels**, avec les politiques, les actions, les indicateurs et les cibles, à côté des thèmes environnementaux et de gouvernance [V F12 § 2 ; ESRS 1 (2026) § 29]. Chez LIGNEVIAL, la sécurité des applicateurs sur des routes circulées en est l'enjeu principal.
- **Comptes consolidés (0,5 pt)** : l'état de durabilité porte sur la **même entreprise déclarante que les états financiers** : un groupe consolidé lorsque la mère établit des comptes consolidés [V ESRS 1 (2026) § 60]. AUBRAMONT n'établit pas de comptes consolidés et le groupe ne publie aucun document d'ensemble. L'état de LIGNEVIAL porte donc sur **LIGNEVIAL seule**, comme ses comptes annuels ; ni la holding ni ORBIPANNEAUX n'entrent dans ses activités propres.

**b. Acteurs et référentiels (1 pt)**
- **EFRAG** : groupe consultatif européen, conseiller technique de la Commission ; il prépare les projets d'ESRS, que la Commission adopte par actes délégués, et a élaboré la norme volontaire pour les PME. Ces normes reposent sur la **double matérialité** [V F12 § 1 ; règl. 2026/1563 consid. 3] (0,25 pt).
- **ISSB** : conseil de normalisation de la Fondation IFRS, créé en 2021 ; il publie les normes IFRS S1 (exigences générales) et S2 (climat), destinées aux investisseurs, selon une approche **financière** [S, F12 § 1] (0,25 pt).
- **GRI** : organisation internationale dont les normes, universelles, sectorielles et thématiques, portent sur les **impacts** sur l'économie, l'environnement et les personnes [S, F12 § 1] (0,25 pt).
- LIGNEVIAL a retenu les ESRS (hypothèse de l'énoncé), que le Département accepte ; elle peut y ajouter des informations issues d'un autre référentiel, comme la GRI, à condition de les identifier [V ESRS 1 (2026) § 107] (0,25 pt).

**Réponses tolérées**
- La mention de la TCFD, intégrée aux normes de l'ISSB, ou de la norme volontaire pour les PME.
- Une définition qui ne cite pas l'article du code de commerce, si les deux angles de la double matérialité sont présents.

**Erreurs fréquentes**
- Réduire le reporting de durabilité aux informations sociales, ou le présenter comme un rapport de groupe consolidé alors que la holding ne consolide pas (`JUR-A05`).
- Traiter l'interopérabilité des référentiels, que la question exclut (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 232-6-3 I ; ESRS 1 (2026) § 3-4, 29, 35-36, 46, 60, 76, 104, 107, 112-116 | Définition ; utilisateurs ; place ; entreprise déclarante ; connectivité | [V] ; application à une publication volontaire : [S] | F12 § 2, 6.2, 9, 17 |
| EFRAG, ISSB, GRI | Acteurs et approches de la matérialité | EFRAG : [V] ; ISSB, GRI : [S] | F12 § 1 |

### 3.7 Exigences générales et principes de publication (3 pts)

| Manquement (annexe 3.8) | Qualification | Ce que LIGNEVIAL doit faire | Points |
|---|---|---|---:|
| « Nos peintures sont 100 % écologiques et sans impact sur l'environnement », alors que 86 tonnes sur 226, soit 38,1 %, sont des peintures à solvant dont les fiches signalent des composés organiques volatils et des dangers pour l'environnement | Affirmation **non fidèle** : elle n'est ni **neutre** (seul l'aspect favorable est présenté), ni **complète**, ni **exacte** ; elle n'est pas **vérifiable** et contredit les données internes [V ESRS 1 (2026) § 19-20 ; appendice B, QC6, QC7, QC14] | Supprimer l'affirmation et décrire l'impact réel des produits, à partir des données disponibles | 0,75 |
| Deux pages de mécénat (club de rugby, plages, ruches) en tête de l'état, « sans autre mention », alors que la biodiversité et les communautés ont été jugées non matérielles | **Information non matérielle publiée sans être signalée** ; placée en tête, elle risque d'**obscurcir** les informations matérielles [V ESRS 1 (2026) § 23-24] | La conserver si elle répond à la demande du Département, en la signalant comme **ne résultant pas de l'évaluation de la matérialité**, sans obscurcir le reste [V § 108-109] | 0,5 |
| Accidents du travail non publiés (7 accidents avec arrêt, 412 jours, un accident grave), parce que « nos concurrents s'en serviraient » | **Omission** d'une information matérielle. L'omission pour préjudice commercial grave n'est admise qu'exceptionnellement et sous conditions cumulatives : ne pas faire obstacle à une compréhension juste et équilibrée des **principaux impacts** ; impossibilité de publier sous une autre forme, **agrégée** par exemple ; indication de l'omission pour chaque donnée omise ; réexamen annuel. Ici, l'omission prive le lecteur de l'indicateur du principal impact social ; une publication agrégée et anonyme reste possible ; rien n'est signalé. Les conditions ne sont **pas remplies** [V ESRS 1 (2026) § 100 a), 101] | Publier les accidents, au besoin sous une forme agrégée, sans identifier la victime [V § 100 d)] | 0,75 |
| Thème matériel des produits de marquage réduit à une phrase : aucune politique, aucune action, aucun indicateur, aucune cible | Manquement aux **principes de publication** : pour chaque thème matériel, l'entreprise applique les exigences générales relatives aux **politiques, actions, indicateurs et cibles**, puis les exigences thématiques pertinentes [V ESRS 1 (2026) § 25, 29 ; F12 § 8]. L'absence de politique écrite ne dispense pas d'informer : l'entreprise le **signale** [V ESRS 2 (2026) § 38-39] | Indiquer qu'elle n'a pas adopté de politique ni de cible, présenter le projet de substitution à l'étude sans le présenter comme décidé, et publier les quantités par type de produit | 0,5 |
| Plan en cinq parties : territoire, collaborateurs, produits et flotte, gouvernance, puis base de préparation et analyse de matérialité en dernier | **Structure** non conforme : quatre parties dans l'ordre (générales, environnementales, sociales, gouvernance), sauf explication motivée d'une autre structure. Les informations générales, dont la base de préparation et la double matérialité, viennent en premier [V ESRS 1 (2026) § 105] | Réorganiser l'état ; corriger la déclaration de conformité, inexacte tant que les manquements subsistent [V ESRS 2 (2026) BP-1] | 0,5 |

La partie relative à la flotte (politique, actions, consommation de deux exercices, cible datée) respecte les principes de publication : elle n'appelle pas de remarque.

**Réponses tolérées**
- Le rattachement de l'affirmation sur les peintures au seul principe de vérifiabilité, ou à la seule représentation fidèle.
- Pour le mécénat, une réponse qui demande de supprimer ces pages, si elle relève qu'elles ne sont pas matérielles et ne sont pas signalées : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Concevoir à la place de LIGNEVIAL des indicateurs ou des cibles, ce qui relève du pilotage, hors programme (`JUR-F01`).
- Développer le contenu des normes thématiques au lieu d'appliquer les principes transversaux (`JUR-F01`).
- Admettre l'omission au seul motif de la concurrence, sans examiner ses conditions (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 19-20, 23-25, 29, 100-101, 105, 107-109 ; appendice B, QC6, QC7, QC14 | Image fidèle et caractéristiques qualitatives ; matérialité de l'information ; omission ; structure ; informations supplémentaires | [V] ; application : [S] | F12 § 5, 8, 17 |
| ESRS 2 (2026) § 38-39, BP-1 | Absence de politique signalée ; déclaration de conformité | [V] | F12 § 14, 17 |

### 3.8 Objectifs de la mission, nature de l'assurance et axes (2 pts)

- **Nature et objectifs (0,5 pt)** : LIGNEVIAL n'est pas tenue de publier : la mission est **contractuelle**, définie par la lettre de mission. Pour un commissaire aux comptes, c'est une **prestation**, distincte de la certification des comptes [V L. 821-2 IV, R. 821-195 ; F12 § 11 ; annexe 3.9]. Le cabinet s'inspire des lignes directrices de la H2A qui organisent la certification légale [S, transposition]. Pour chaque axe, il cherche à conclure qu'il n'a pas relevé d'erreurs, d'omissions ou d'incohérences d'une importance telle qu'elles remettent en cause la conformité aux ESRS [V LD 2026 § 8].
- **Assurance limitée (0,5 pt)** : ses vérifications sont moindres en **nature**, en **étendue** et en **durée** que celles d'un audit des comptes ; sa conclusion est de **forme négative**. La certification des comptes de LIGNEVIAL repose au contraire sur une assurance raisonnable et une opinion positive [V LD 2026, niveau d'assurance ; F13 § 2.3]. Le cabinet ne vérifie spécifiquement que les informations qui présentent un risque important de non-conformité ou des attentes fortes des utilisateurs [V LD 2026 § 8.3.1].
- **Les quatre axes (0,5 pt)** [V LD 2026 § 2] :
  - axe 1 : conformité aux ESRS du **processus** de détermination des informations, l'analyse de double matérialité, y compris la consultation du CSE lorsque l'entité y est soumise ;
  - axe 2 : conformité des **informations** publiées aux ESRS ;
  - axe 3 : respect des exigences de publication de l'article 8 du règlement **taxonomie** ;
  - axe 4, à terme : conformité au **balisage** électronique.
- **Pourquoi deux axes seulement (0,5 pt)** :
  - les obligations de publication de la taxonomie ne visent que les entreprises soumises à l'obligation de publier des informations en matière de durabilité. LIGNEVIAL, qui publie volontairement, n'y est pas soumise et ne publie pas ces informations : l'axe 3 est sans objet [V F13 § 5, point 5] ;
  - le balisage ne concerne lui aussi que les entités soumises, et il n'est exigible pour personne tant que les règles de balisage ne sont pas adoptées : la mission ne peut porter, au plus, que sur trois axes [V LD 2026 § 2, 10] ;
  - restent l'axe 1, retenu sans la consultation du CSE, que la lettre de mission exclut et qui n'est pas obligatoire pour une publication volontaire [V F12 § 11], et l'axe 2.

**Réponses tolérées**
- Une présentation des quatre axes qui n'explique que pour l'un des deux axes écartés pourquoi il est sans objet : 0,25 pt sur 0,5.

**Erreurs fréquentes**
- Qualifier la mission de certification légale, ou l'assurance de raisonnable (`JUR-A01`).
- Retenir l'axe de la taxonomie pour une publication volontaire (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 2, 8, 8.3.1, 10, niveau d'assurance | Axes ; assurance limitée ; informations vérifiées spécifiquement ; balisage | [V] ; transposition à une mission contractuelle : [S] | F13 § 2, 3, 5, 7 |
| C. com. L. 821-2 IV, R. 821-195 | Prestation et lettre de mission | [V] | F11 § 1.2 ; F12 § 11 |

### 3.9 Étapes de la démarche et procédures (2,5 pts)

*Étapes (1 pt)* [V LD 2026, § 4 à 17 ; F13 § 3]
- **Lettre de mission**, signée le 15/10/2026 : objet, axes, calendrier, accès aux personnes et aux documents, lettre d'affirmation, honoraires.
- **Prise de connaissance** de LIGNEVIAL et de son environnement : chantiers sous circulation, produits appliqués, flotte, organisation, manière dont les informations sont produites. Le cabinet tient compte des utilisateurs, au premier rang desquels le Département.
- **Planification** : identification des informations à **risque important de non-conformité** ou à **fortes attentes des utilisateurs** [V LD 2026 § 8.3.1]. Ici : la sécurité des équipes, les produits de marquage et les actions pour le territoire, que le Département cite expressément.
- **Vérification de la conformité** du processus (axe 1), sans anomalie relevée, puis des informations (axe 2) : base de préparation, présentation, informations vérifiées spécifiquement [V LD 2026 § 7-8.3].
- **Fin de mission** : lecture d'ensemble et cohérence avec les comptes annuels, échanges avec l'équipe d'audit des comptes, communication des constats au président, lettre d'affirmation ; puis **rapport** [V LD 2026 § 3.2, 11-17].

*Procédures sur les manquements (1,5 pt : 0,25 pt par procédure pertinente, dans la limite de six)* [V LD 2026 § 8.1-8.3.2]
- **Peintures** : demander au président les éléments qui fondent l'affirmation ; rapprocher les tonnages publiables des achats et des bons de sortie déjà testés lors de l'audit des comptes (226 tonnes, dont 86 à solvant) ; inspecter les fiches de données de sécurité ; demander la suppression de l'affirmation.
- **Accidents du travail** : inspecter le registre des accidents et les déclarations d'accident ; rapprocher les heures travaillées et l'effectif des données de la paie ; s'entretenir avec le responsable de la sécurité ; examiner, avec le président, si une publication agrégée est possible et si les conditions de l'omission sont réunies ; demander la publication.
- **Produits de marquage** : s'entretenir avec le directeur technique ; lire sa note interne de septembre 2026 ; vérifier l'absence de politique, d'action et de cible ; demander que l'état le signale et ne présente pas le projet à l'étude comme une décision.
- **Mécénat** : rapprocher les 24 000 € de la comptabilité et des conventions ; vérifier dans l'analyse de double matérialité que la biodiversité et les communautés ont été jugées non matérielles ; demander que ces pages soient signalées comme informations supplémentaires.
- **Structure et base de préparation** : vérifier l'ordre des quatre parties ou l'explication d'une autre structure, et l'exactitude de la déclaration de conformité.
- **Flotte et cohérence** : rapprocher la consommation de gazole des achats de carburant comptabilisés ; vérifier la cohérence des effectifs avec ceux du rapport de gestion.
- **Fin de mission** : communiquer les constats au président, avec une demande de correction, et obtenir une lettre d'affirmation.

**Réponses tolérées**
- D'autres procédures pertinentes tirées des annexes : observation d'un chantier sous circulation, comparaison avec des données sectorielles.

**Erreurs fréquentes**
- Présenter des étapes générales sans les rattacher au cas, ou omettre la planification fondée sur les risques et les attentes des utilisateurs (`JUR-A05`).
- Ne pas exploiter les données de l'audit des comptes (achats, paie, mécénat) (`JUR-F07`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 3.2, 4-17, 8.1-8.3.2 | Étapes ; sélection des informations ; techniques ; échanges avec le commissaire aux comptes | [V] ; transposition : [S] | F13 § 3, 7 |
| ESRS 1 (2026) § 100, 105, 108-109 ; ESRS 2 (2026) § 39 | Points vérifiés | [V] | F12 § 17 |

### 3.10 Conclusions par axe et structure du rapport (1,5 pt)

- **Si seule l'omission des accidents subsistait (0,5 pt)** : l'omission de l'indicateur du principal impact social est d'une importance telle qu'elle remet en cause la conformité des informations. Elle est toutefois **isolée** et précisément identifiable : ses incidences sont **clairement circonscrites**, et une réserve qui décrit l'information omise suffit à éclairer l'utilisateur. La conclusion sur l'axe 2 serait un **avis de conformité assorti d'une réserve motivée** [V LD 2026 § 17 ; F13 § 4.3].
- **Situation effective (0,5 pt)** :
  - **axe 1, processus** : les travaux n'ont relevé aucune anomalie. **Avis de conformité** : « nous n'avons pas relevé d'erreurs, omissions ou incohérences importantes concernant la conformité du processus mis en œuvre par LIGNEVIAL avec les ESRS » [V LD 2026, annexe 2] ;
  - **axe 2, informations** : à l'omission s'ajoutent l'absence de toute information de gestion sur les produits de marquage et l'affirmation « 100 % écologiques », que le président conserve alors qu'elle est contraire aux données. Deux des trois thèmes matériels, l'impact social et l'impact environnemental principaux, sont touchés : l'état ne donne plus une image fidèle des impacts de LIGNEVIAL, et ses incidences **ne sont pas circonscrites**. **Avis de non-conformité, motivé** : « nous estimons que les informations en matière de durabilité publiées par LIGNEVIAL ne sont pas conformes aux ESRS », avec les deux motifs [V LD 2026 § 17 et annexe 2, formulation adaptée à l'axe 2 ; S, transposition à une mission contractuelle].
- **Structure du rapport (0,5 pt)** [V LD 2026 § 17 ; F13 § 4.1] :
  - titre et destinataire : le président, comme le prévoit la lettre de mission ;
  - partie introductive : qualité du cabinet et de la signataire, inscrite pour cette activité ; informations couvertes et leur localisation dans le rapport de gestion ; responsabilités respectives ; lignes directrices de la H2A et règles de déontologie appliquées ; caractère contractuel de la mission et limites de l'assurance limitée ;
  - une partie par axe retenu, soit deux : nature des vérifications, conclusion, observations (possibles seulement avec un avis de conformité, avec ou sans réserve), éléments qui ont fait l'objet d'une attention particulière ;
  - date et signature de Mme ESTRABAUT, personne physique.
  - Les motifs sont communiqués au préalable au président. Le rapport lui est remis ; c'est lui qui décide de le joindre à la candidature. Tenu au secret, le cabinet ne l'adresse pas lui-même au Département [V L. 821-35 ; S, application]. Ce rapport est distinct du rapport sur les comptes et ne modifie pas l'opinion sur les comptes.

**Réponses tolérées**
- Dans la situation effective, un avis de conformité assorti de réserves, si le candidat soutient avec le critère de circonscription que chaque manquement est identifiable : 0,25 pt sur 0,5.
- L'emploi indifférent des mots « conclusion » et « avis ».

**Erreurs fréquentes**
- Formuler une conclusion positive (« les informations sont conformes ») ou une conclusion unique pour toute la mission (`JUR-A01`, `JUR-A02`).
- Retenir une impossibilité d'émettre un avis, alors que les manquements sont des omissions et des erreurs, et non une limitation des travaux (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 et annexe 2 | Avis par axe ; réserve ; non-conformité ; structure ; formulations | [V] ; transposition : [S] | F13 § 4 |
| C. com. L. 821-35 | Secret professionnel | [V] ; application : [S] | F10 § 7 |
