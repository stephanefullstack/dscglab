# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 14

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 15/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex37_consolidation_anc_frais_etablissement_mee_indirecte` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.5 | `exercices/ex38_fusion_renonciation_filiale_boni_soulte` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.11 | `exercices/ex39_audit_financement_eip_audit_interne_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Obligation de consolider et référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 2 |
| 1.2 Cadre conceptuel de l'IASB, frais d'établissement et variétés protégées | `2.1.a` Cadre conceptuel de l'IASB ; `2.1.d` Conséquences du référentiel | 2 |
| 1.3 a Périmètre, pourcentages et méthodes | `2.1.c` Périmètre de consolidation | 2 |
| 1.3 b Conséquences des méthodes sur l'information financière | `2.1.d` Conséquences du référentiel et des méthodes | 1 |
| 1.4 Frais d'établissement de SEMÉLIANE Recherche | `2.2.c` Homogénéisation, thèmes communs | 4 |
| 1.5 Droits de mutation et frais de l'entrepôt | `2.2.c` Homogénéisation, thèmes communs | 4 |
| 1.6 a Ventes internes et marges sur stocks | `2.2.f` Comptes réciproques et résultats internes | 3,5 |
| 1.6 b Dividendes | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.6 c Comptes réciproques et chèque en transit | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.7 a Actif net réévalué de SEMENCES DU BOISCHAUT | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.7 b Coût d'acquisition et écart d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.7 c Durée d'utilisation de l'écart et écritures | `2.2.g` Écarts d'évaluation et d'acquisition | 3 |
| 1.8 a Partage des capitaux propres de deux filiales | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.8 b Mise en équivalence de BEAUCERONNE | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.8 c Écritures d'élimination des titres et de mise en équivalence | `2.2.h` Partage des capitaux propres | 2 |
| 1.9 Passage aux capitaux propres consolidés | `2.2.a` Processus d'élaboration d'une consolidation | 3 |
| 1.10 a Extrait du compte de résultat consolidé | `2.3.a` Documents de synthèse consolidés | 3 |
| 1.10 b Annexe consolidée | `2.3.a` Documents de synthèse consolidés | 1,5 |
| 1.10 c Deux différences de présentation en IFRS | `2.3.a` Documents de synthèse consolidés ; `2.1.d` Conséquences du référentiel | 1,5 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires (réserves / résultat) ; `EA` = écart d'acquisition ; `AMO_EA` = amortissements de l'écart d'acquisition ; `DOT_EA` = ligne « dotations aux amortissements et dépréciations des écarts d'acquisition » du compte de résultat ; `TME` = titres mis en équivalence ; `QP_MEE` = ligne « résultat net lié aux entités mises en équivalence » ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.GATINAIS` : titres détenus par GRAINES DU GÂTINAIS ; `RSV.RECHERCHE` : réserves de SEMÉLIANE Recherche).

---

### 1.1 Obligation de consolider et référentiel (2 pts)

**Obligation (1 pt).**
- **Principe (0,25).** Les sociétés commerciales établissent et publient des comptes consolidés dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 ; F03 § 1.1]. La SAS SEMÉLIANE, société commerciale, contrôle exclusivement SEMÉLIANE Recherche, SEMÉLIANE Distribution, GRAINES DU GÂTINAIS et SEMENCES DU BOISCHAUT (question 1.3 a) : l'obligation est née.
- **Exemption de la société contrôlée (0,25).** Elle ne joue que si la société est incluse dans les comptes consolidés publiés d'une entité qui la contrôle, et sauf opposition d'actionnaires représentant au moins le dixième du capital [V L. 233-17, 1° ; F03 § 1.1]. SEMÉLIANE est contrôlée par le fonds TALVIÈRE Croissance II (62 %), mais ni le fonds ni sa société de gestion n'établissent de comptes consolidés qui l'incluent : l'exemption est exclue. La famille fondatrice, qui détient 30 % du capital, pourrait au surplus s'y opposer.
- **Exemption des ensembles qui ne sont pas un grand groupe (0,25).** Un grand groupe dépasse, à la clôture, deux des trois seuils (bilan 30 M€, chiffre d'affaires net 60 M€, 250 salariés), sur deux exercices consécutifs [V L. 230-2, 3° et D. 230-2 ; F03 § 1.1]. L'ensemble dépasse les trois seuils en 2025 (196 M€, 214 M€, 790 salariés) et en 2026 (231 M€, 238 M€, 860) : l'exemption du 2° ne joue pas. L'intérêt négligeable des filiales [V L. 233-17-1] est exclu au vu de leur taille.
- **Conclusion (0,25).** SEMÉLIANE doit établir et publier des comptes consolidés de 2026.

**Référentiel (0,5 pt).** Les IFRS adoptées par l'Union européenne ne sont obligatoires, pour les comptes consolidés, que pour les sociétés dont des titres sont admis aux négociations sur un marché réglementé d'un État membre à la date de clôture [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Aucun titre de SEMÉLIANE n'étant admis sur un marché, elle applique le règlement ANC n° 2020-01 ou **peut opter** pour les IFRS adoptées [V L. 233-24 ; F03 § 1.2] ; elle n'a pas exercé cette option.

**Admission des actions (0,5 pt).** Si ses actions étaient admises aux négociations sur un marché réglementé, les IFRS adoptées deviendraient **obligatoires** pour ses comptes consolidés à compter du premier exercice clos alors que les titres sont admis [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2]. Une SAS ne pouvant pas faire admettre ses actions aux négociations sur un marché réglementé, la société serait au préalable transformée en société anonyme, comme le prévoit le fonds [V C. com. L. 227-2] ; ce point de droit des sociétés n'est pas noté. Une admission sur un marché qui n'est pas réglementé laisserait le choix du référentiel ouvert [application, S].

---

### 1.2 Cadre conceptuel de l'IASB, frais d'établissement et variétés protégées (2 pts)

- **Objectif et utilisateurs (0,5 pt).** Le cadre conceptuel énonce les concepts qui guident l'IASB dans l'élaboration des normes et aident les entités à définir une méthode lorsqu'aucune norme ne s'applique [V page « Conceptual Framework », ifrs.org ; IAS 8 § 11 ; F03 § 7.2]. L'information financière à usage général doit être utile aux **investisseurs, prêteurs et autres créanciers, actuels et potentiels**, pour leurs décisions relatives à la fourniture de ressources à l'entité [S ; F03 § 7.2]. Pour SEMÉLIANE : le fonds et la famille fondatrice (investisseurs actuels), les futurs actionnaires si les actions sont admises (investisseurs potentiels), les banques et les fournisseurs (prêteurs et créanciers).
- **Définition d'un actif (0,5 pt).** Ressource contrôlée par l'entité du fait d'événements passés, et dont on attend des avantages économiques futurs [V IAS 38 § 8 ; F03 § 9] ; une immobilisation incorporelle doit en outre être **identifiable**, c'est-à-dire séparable ou issue de droits contractuels ou légaux [V IAS 38 § 12 ; F03 § 11]. Le cadre de 2018 parle d'une ressource économique actuelle, c'est-à-dire d'un droit qui a le potentiel de produire des avantages économiques [S ; F03 § 9].
- **Frais d'établissement (0,5 pt).** Les honoraires de constitution et les frais de démarrage de la station ne donnent à SEMÉLIANE Recherche aucun droit ni aucune ressource contrôlée distincte de la société elle-même : ce ne sont pas des actifs. Les IFRS les passent en charges [V IAS 38 § 69 a) ; F04 R5], tout comme le règlement ANC dans les comptes consolidés [V ANC art. 272-5, p. 54 ; F04 R5] (question 1.4) : le passage aux IFRS ne changerait rien aux comptes consolidés, seule l'option des comptes individuels de la filiale [V PCG art. 212-9, p. 15] en diffère.
- **Variétés protégées (0,5 pt).** Les certificats d'obtention végétale sont des **droits légaux** : ils donnent à SEMENCES DU BOISCHAUT le droit exclusif de produire et de vendre les semences de ces variétés (contrôle et restriction de l'accès des tiers [V IAS 38 § 13]), ils résultent d'événements passés (sélection et obtention des titres), ils procurent des ventes futures et ils peuvent être cédés ou concédés en licence : ils sont identifiables [V IAS 38 § 12 ; F03 § 11]. Bien qu'ils ne figurent pas au bilan de la filiale, ils sont comptabilisés séparément de l'écart d'acquisition dans un regroupement [V IFRS 3 § B31 ; F03 § 11], comme en ANC, où les éléments identifiables comprennent des éléments non comptabilisés par l'entité acquise [V ANC art. 231-7, p. 21 ; F05 § 1.2] (question 1.7 a). Les IFRS ne changeraient donc pas non plus leur traitement. Le savoir-faire de l'équipe de sélectionneurs, en revanche, n'est pas contrôlé [V IAS 38 § 15] : il reste compris dans l'écart d'acquisition.

Les différences tiendraient ailleurs : écart d'acquisition non amorti, frais d'acquisition des titres en charges [V IFRS 3 § 53 ; F05 § 2 et 5], présentation (question 1.10 c).

---

### 1.3 Périmètre et méthodes (3 pts)

#### a. Tableau et justification (2 pts)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % d'intérêt des minoritaires |
|---|---|---|---|---|---|
| SAS SEMÉLIANE | — | Société consolidante | — | 100 % | — |
| SEMÉLIANE Recherche | 100 % | Exclusif | Intégration globale | 100 % | 0 % |
| SEMÉLIANE Distribution | 100 % | Exclusif | Intégration globale | 100 % | 0 % |
| GRAINES DU GÂTINAIS | 70 % | Exclusif | Intégration globale | 70 % | 30 % |
| SEMENCES DU BOISCHAUT | 80 % | Exclusif | Intégration globale | 80 % | 20 % |
| BEAUCERONNE | 20 % + 20 % = **40 %** | Influence notable | Mise en équivalence | 20 % + 70 % × 20 % = **34 %** | 40 % – 34 % = **6 %** |

(Quatre filiales : 0,25 chacune, soit 1 ; BEAUCERONNE : 0,5.) La majorité des droits de vote donne le contrôle exclusif [V ANC art. 211-3, p. 12-13 ; F03 § 2], qui conduit à l'intégration globale ; l'influence notable conduit à la mise en équivalence [V art. 221-1, p. 18 ; F03 § 3].

- **Pourcentages de BEAUCERONNE.** Le pourcentage de contrôle additionne les droits de vote détenus par la consolidante et par les entités qu'elle contrôle exclusivement, sans multiplication : 20 % (SEMÉLIANE) + 20 % (GRAINES DU GÂTINAIS, contrôlée exclusivement) = 40 % [V art. 211-6, p. 14 ; F03 § 4.1]. Le pourcentage d'intérêt fait la somme, sur chaque chaîne, du produit des pourcentages de capital : 20 % + 70 % × 20 % = 34 % [S, méthode du corrigé du sujet zéro ; F03 § 4.1]. Les 6 % restants sont la part des minoritaires de GRAINES DU GÂTINAIS dans la quote-part détenue indirectement (30 % × 20 %), présentée dans les intérêts minoritaires.
- **Nature du contrôle exercé sur BEAUCERONNE (0,5 pt).** Avec 40 % des droits de vote, le groupe n'a pas la majorité. La présomption de contrôle exclusif fondée sur la désignation de la majorité des dirigeants suppose une fraction **supérieure à 40 %** des droits de vote, sans qu'aucun autre associé détienne une fraction supérieure [V art. 211-3, p. 12-13 ; F03 § 2]. Elle ne joue pas ici à double titre : le groupe ne détient que 40 %, et DARNÉVILLE Grains détient 60 % et désigne trois des cinq membres du comité de direction ; c'est elle qui contrôle BEAUCERONNE. Aucun accord ne prévoit un contrôle conjoint [V art. 211-4, p. 13]. Le groupe détient plus de 20 % des droits de vote et deux sièges sur cinq, et BEAUCERONNE traite une partie de ses semences : **influence notable** [V art. 211-5, p. 13 ; F03 § 2].

#### b. Conséquences des méthodes sur l'information financière (1 pt)

- **GRAINES DU GÂTINAIS, intégration globale (0,5).** Ses produits, ses charges, ses actifs et ses dettes sont repris à 100 %, après élimination des opérations internes [V art. 221-2, p. 18-19 ; F03 § 3] : le chiffre d'affaires consolidé comprend toutes ses ventes aux tiers (pas ses ventes à SEMÉLIANE Distribution), l'endettement consolidé toutes ses dettes, bien que le groupe n'en détienne que 70 % ; le résultat est repris en totalité puis partagé, la part de M. PERDRIAUX apparaissant dans les intérêts minoritaires.
- **BEAUCERONNE, mise en équivalence (0,5).** Ni son chiffre d'affaires ni ses dettes n'apparaissent dans les comptes consolidés : une seule ligne à l'actif (titres mis en équivalence, quote-part de ses capitaux propres) et une seule ligne au compte de résultat (résultat net lié aux entités mises en équivalence), après le résultat des entités intégrées [V art. 262-3, p. 49 ; art. 281-2, p. 67 ; F14 § 1.3]. Le chiffre d'affaires et l'endettement du groupe ne traduisent donc que l'activité des sociétés qu'il contrôle ; le résultat comprend sa quote-part du résultat de BEAUCERONNE.

---

### 1.4 Frais d'établissement de SEMÉLIANE Recherche (4 pts)

**Justification (1 pt).** Le PCG permet d'inscrire à l'actif les frais de constitution et de premier établissement, l'inscription en charges étant la méthode de référence [V PCG art. 212-9, p. 15 ; art. 121-5, p. 10-11 ; F04 R5 et § 1] ; SEMÉLIANE Recherche les a activés et les amortit sur cinq ans. Dans les comptes consolidés, ils sont **obligatoirement comptabilisés en charges** de l'exercice au cours duquel ils ont été encourus [V ANC art. 272-5, p. 54 ; F04 R5] ; les comptes de la filiale sont retraités pour appliquer les méthodes du groupe [V art. 271-5, p. 52 ; F04 § 1]. En consolidation, la totalité des 360 000 € est une charge de 2025 ; les dotations de 2025 (dans les réserves) et de 2026 (dans le résultat) sont annulées. Selon l'hypothèse de l'énoncé, les frais sont déduits fiscalement au rythme de leur amortissement : leur base fiscale au 31/12/2026 est la valeur nette restante (216 000 €), leur valeur consolidée est nulle, d'où un **impôt différé actif** [V art. 272-8, p. 57 ; F04 R5], recouvrable selon l'énoncé.

**Tableau des incidences (1,5 pt)**

| | 2025 (ouverture, réserves) | 2026 (résultat) | Clôture (31/12/2026) |
|---|---:|---:|---:|
| Comptes individuels : dotations (360 000 / 5) | 72 000 | 72 000 | VNC 216 000 |
| Comptes consolidés : charges | 360 000 | 0 | VNC 0 |
| **Écart avant impôt** (0,5) | **– 288 000** | **+ 72 000** | **– 216 000** |
| Impôt différé actif (25 %) (0,5) | + 72 000 | – 18 000 | **+ 54 000** |
| **Net** (0,5) | **– 216 000** (réserves) | **+ 54 000** (résultat) | – 162 000 |

Le retraitement augmente le résultat consolidé de 2026, puisque la charge a été constatée en 2025 ; l'impôt différé actif de 72 000 € à l'ouverture est repris de 18 000 € en 2026.

**C1 (bilan, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2801 Amortissements des frais d'établissement (72 000 × 2) | 144 000 | |
| RSV.RECHERCHE Réserves SEMÉLIANE Recherche (288 000 × 75 %) | 216 000 | |
| IDA Impôt différé actif (216 000 × 25 %) | 54 000 | |
| 2011 Frais de constitution | | 60 000 |
| 2012 Frais de premier établissement | | 300 000 |
| RST.RECHERCHE Résultat SEMÉLIANE Recherche (72 000 × 75 %) | | 54 000 |
| *Annulation des frais d'établissement* | **414 000** | **414 000** |

**C1R (compte de résultat, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RES_CR Résultat | 54 000 | |
| CH_ID Charge d'impôt différé (72 000 × 25 %) | 18 000 | |
| 68111 Dotations aux amortissements des immobilisations incorporelles et des frais d'établissement | | 72 000 |
| *Annulation de la dotation de 2026* | **72 000** | **72 000** |

SEMÉLIANE Recherche étant détenue à 100 %, le retraitement revient en totalité au groupe.

---

### 1.5 Droits de mutation et frais de l'entrepôt de SEMÉLIANE Distribution (4 pts)

**Justification (1 pt).** Le PCG laisse le choix entre l'inscription en charges et le rattachement au coût de l'immobilisation des droits de mutation, honoraires, commissions et frais d'actes liés à son acquisition, le rattachement étant la méthode de référence [V PCG art. 213-8, p. 17 ; F04 R4]. SEMÉLIANE Distribution a choisi les charges. Dans les comptes consolidés, ces coûts sont **obligatoirement comptabilisés à l'actif** [V ANC art. 272-6, p. 54-55 ; F04 R4] : les 144 000 € (116 000 + 24 000 + 4 000) sont retirés des charges de 2026 et ajoutés au coût du terrain et du bâtiment. Déduits fiscalement en 2026, ils ne figurent pas dans la base fiscale de l'entrepôt : la valeur consolidée dépasse la base fiscale, d'où un **impôt différé passif** [V art. 272-8, p. 57 ; F04 R4].

**Répartition et amortissement (1 pt)**

| | Calcul | Montant |
|---|---|---:|
| Part du terrain (0,25) | 144 000 × 500 000 / 2 000 000 | 36 000 |
| Part du bâtiment (0,25) | 144 000 × 1 500 000 / 2 000 000 | 108 000 |
| Amortissement complémentaire de 2026 (0,5) | 108 000 / 25 × 9/12 (01/04 au 31/12/2026) | 3 240 |

Le terrain n'est pas amorti : sa part des frais reste à l'actif sans dotation. Le bâtiment est inscrit en consolidation pour 1 608 000 € ; la dotation des comptes individuels (1 500 000 / 25 × 9/12 = 45 000 €) n'est pas modifiée, seul le complément s'y ajoute.

**Tableau des incidences (1 pt)**

| | Comptes individuels | Comptes consolidés | Écart (résultat 2026) |
|---|---:|---:|---:|
| Droits et frais en charges | 144 000 | 0 | + 144 000 |
| Dotation sur la part des frais affectée au bâtiment | 0 | 3 240 | – 3 240 |
| **Écart avant impôt** (0,5) | | | **+ 140 760** |
| Impôt différé passif (25 %) (0,25) | | | – 35 190 |
| **Net** (0,25) | | | **+ 105 570** |

Acheté en 2026, l'entrepôt n'a aucune incidence sur les réserves.

**C2 (bilan) et C2R (compte de résultat), 1 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2115 Terrains bâtis | 36 000 | |
| 2131 Bâtiments | 108 000 | |
| 2813 Amortissements des constructions | | 3 240 |
| IDP Impôt différé passif (140 760 × 25 %) | | 35 190 |
| RST.DISTRIB Résultat SEMÉLIANE Distribution (140 760 × 75 %) | | 105 570 |
| *C2 – Inscription des droits et frais au coût de l'entrepôt* | **144 000** | **144 000** |
| 68112 Dotations aux amortissements des immobilisations corporelles | 3 240 | |
| CH_ID Charge d'impôt différé | 35 190 | |
| RES_CR Résultat | 105 570 | |
| 6354 Droits d'enregistrement et de timbre | | 116 000 |
| 6226 Honoraires | | 24 000 |
| 6227 Frais d'actes et de contentieux | | 4 000 |
| *C2R – Annulation des charges et amortissement complémentaire* | **144 000** | **144 000** |

---

### 1.6 Opérations internes (6 pts)

#### a. Ventes de semences et marges sur stocks (3,5 pts)

**Justification (1 pt).** Les ventes et achats réciproques sont éliminés en totalité, sans incidence sur le résultat [V ANC art. 251-1, p. 45 ; F04 R14]. Les profits internes compris dans les stocks sont éliminés **en totalité**, puis répartis entre le groupe et les minoritaires **de l'entité qui les a réalisés**, ici GRAINES DU GÂTINAIS (70 % / 30 %) ; l'impôt est corrigé [V art. 251-2, p. 45 ; F04 R14]. La marge comprise dans le stock d'ouverture a déjà été éliminée des comptes consolidés de 2025 : elle réduit les réserves, puis, les semences ayant été revendues en 2026, elle est réalisée en 2026 ; celle du stock de clôture réduit le résultat de 2026. L'élimination ramène le stock au-dessous de sa base fiscale (prix payé par SEMÉLIANE Distribution) : **impôt différé actif**, rattaché à GRAINES DU GÂTINAIS selon le manuel.

**Calculs (0,75 pt).** Le taux de 25 % est exprimé sur le coût : la marge représente 25 / 125 = 20 % du prix de vente.

| | Ouverture (31/12/2025) | Clôture (31/12/2026) | Incidence de 2026 |
|---|---:|---:|---:|
| Stock acheté à GRAINES DU GÂTINAIS | 300 000 | 420 000 | |
| Marge comprise (× 25/125) | 60 000 | 84 000 | |
| Incidence avant impôt | – 60 000 (réserves) | – 84 000 | – 24 000 (résultat : + 60 000 – 84 000) |
| Impôt différé actif (25 %) | 15 000 | 21 000 | + 6 000 |
| **Net** | **– 45 000** (réserves) | | **– 18 000** (résultat) |

**Répartition (0,75 pt).** L'élimination réduit les capitaux propres retraités de GRAINES DU GÂTINAIS (question 1.8 a) ; elle est supportée à 70 % par le groupe et à 30 % par M. PERDRIAUX, minoritaire de la société vendeuse : réserves – 31 500 € (groupe) et – 13 500 € (minoritaires) ; résultat – 12 600 € et – 5 400 €. Si SEMÉLIANE Distribution, détenue à 100 %, avait été la société vendeuse, le groupe aurait supporté toute l'élimination.

**C3, C4 et C4R (1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 701 Ventes de produits finis (GRAINES DU GÂTINAIS) | 1 800 000 | |
| 607 Achats de marchandises (SEMÉLIANE Distribution) | | 1 800 000 |
| *C3 – Élimination des ventes internes (compte de résultat)* | **1 800 000** | **1 800 000** |
| RSV.GATINAIS Réserves GRAINES DU GÂTINAIS (60 000 × 75 %) | 45 000 | |
| IDA Impôt différé actif (84 000 × 25 %) | 21 000 | |
| RST.GATINAIS Résultat GRAINES DU GÂTINAIS (24 000 × 75 %) | 18 000 | |
| 37 Stocks de marchandises (stock de SEMÉLIANE Distribution) | | 84 000 |
| *C4 – Élimination des marges internes sur stocks (bilan)* | **84 000** | **84 000** |
| 6037 Variation des stocks de marchandises (84 000 – 60 000) | 24 000 | |
| CH_ID Produit d'impôt différé (24 000 × 25 %) | | 6 000 |
| RES_CR Résultat | | 18 000 |
| *C4R – Variation de la marge interne (compte de résultat)* | **24 000** | **24 000** |

#### b. Dividendes (1,5 pt)

- **GRAINES DU GÂTINAIS (0,5).** Les dividendes reçus des sociétés consolidées sont éliminés en totalité [V art. 251-2, p. 45 ; F04 R14]. SEMÉLIANE a reçu 280 000 € (70 % de 400 000), prélevés sur le résultat de 2025 de GRAINES DU GÂTINAIS déjà compris dans les réserves consolidées : ils sortent du résultat de SEMÉLIANE et rejoignent ses réserves. Les 120 000 € versés à M. PERDRIAUX ont quitté le groupe : ils réduisent les réserves de la filiale, donc les intérêts minoritaires, sans autre écriture.
- **BEAUCERONNE (0,75).** Les dividendes reçus d'une entité mise en équivalence sont éliminés du compte de résultat de l'entité qui détient les titres et portés en augmentation des réserves consolidées [V ANC art. 262-3, p. 49 ; F05 § 4]. Les deux détenteurs sont concernés : SEMÉLIANE (60 000 €) et GRAINES DU GÂTINAIS (60 000 €). L'élimination chez GRAINES DU GÂTINAIS réduit son résultat retraité, partagé à 70 / 30 (question 1.8 a). La quote-part de BEAUCERONNE est ensuite prise sur ses capitaux propres après distribution (question 1.8 b) : le dividende n'est pas compté deux fois.

**C5, C5R, C6 et C6R (0,25)**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.SEMELIANE Résultat SAS SEMÉLIANE | 280 000 | |
| RSV.SEMELIANE Réserves SAS SEMÉLIANE | | 280 000 |
| *C5 – Élimination du dividende reçu de GRAINES DU GÂTINAIS (bilan)* | **280 000** | **280 000** |
| 7611 Revenus des titres de participation | 280 000 | |
| RES_CR Résultat | | 280 000 |
| *C5R – Même élimination au compte de résultat* | **280 000** | **280 000** |
| RST.SEMELIANE Résultat SAS SEMÉLIANE | 60 000 | |
| RST.GATINAIS Résultat GRAINES DU GÂTINAIS | 60 000 | |
| RSV.SEMELIANE Réserves SAS SEMÉLIANE | | 60 000 |
| RSV.GATINAIS Réserves GRAINES DU GÂTINAIS | | 60 000 |
| *C6 – Élimination des dividendes reçus de BEAUCERONNE (bilan)* | **120 000** | **120 000** |
| 7611 Revenus des titres de participation | 120 000 | |
| RES_CR Résultat | | 120 000 |
| *C6R – Même élimination au compte de résultat* | **120 000** | **120 000** |

#### c. Comptes réciproques et chèque en transit (1 pt)

**Explication (0,5).** Créance de GRAINES DU GÂTINAIS 318 000 € – dette de SEMÉLIANE Distribution 246 000 € = 72 000 €, montant du chèque émis le 29/12/2026, enregistré par l'acheteur mais reçu par le vendeur le 05/01/2027. Le chèque est en transit à la clôture : il ne s'agit pas d'une erreur de l'une des sociétés, mais d'un décalage d'enregistrement, sans incidence sur le résultat. Il est enregistré chez GRAINES DU GÂTINAIS en chèque à encaisser, ce qui ramène sa créance à 246 000 €, égale à la dette [V art. 251-1, p. 45 ; F04 R14].

**C7 et C8 (0,5)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 5112 Chèques à encaisser (GRAINES DU GÂTINAIS) | 72 000 | |
| 4111 Clients (créance de GRAINES DU GÂTINAIS) | | 72 000 |
| *C7 – Chèque en transit au 31/12/2026* | **72 000** | **72 000** |
| 4011 Fournisseurs (dette de SEMÉLIANE Distribution) | 246 000 | |
| 4111 Clients (créance de GRAINES DU GÂTINAIS : 318 000 – 72 000) | | 246 000 |
| *C8 – Élimination des soldes réciproques* | **246 000** | **246 000** |

---

### 1.7 Acquisition de SEMENCES DU BOISCHAUT (8 pts)

#### a. Actif net réévalué au 01/01/2026 et suivi des écarts (2,5 pts)

| Élément | Montant |
|---|---:|
| Capitaux propres individuels au 01/01/2026, résultat de 2025 compris (0,25) | 5 200 000 |
| Écart d'évaluation du portefeuille de variétés protégées (1 600 000 – 0) (0,25) | + 1 600 000 |
| Écart d'évaluation des parcelles d'essais (720 000 – 400 000) (0,25) | + 320 000 |
| Impôt différé passif sur les écarts ((1 600 000 + 320 000) × 25 %) (0,5) | – 480 000 |
| **Actif net réévalué** (0,25) | **6 640 000** |

- **Principe (0,5 pt).** Les éléments identifiables de l'entité acquise sont ceux qui peuvent être évalués séparément ; ils peuvent comprendre des éléments qu'elle n'avait pas comptabilisés [V ANC art. 231-7, p. 21 ; F05 § 1.2] : c'est le cas des variétés obtenues par SEMENCES DU BOISCHAUT, dont les dépenses de sélection ont été passées en charges. L'écart d'évaluation est la différence entre la valeur d'entrée et la valeur comptable [V art. 231-9, p. 22] ; les impôts différés sur ces écarts sont comptabilisés [V art. 232-1, p. 24], en contrepartie de l'écart d'acquisition [V art. 272-13, p. 59 ; F05 § 1.2]. L'exception prévue pour les incorporels généralement non amortis qui ne peuvent être cédés séparément de l'entité acquise [V art. 272-10, p. 58] ne vise pas ce portefeuille, amortissable et cessible séparément : il donne lieu à impôt différé, comme le terrain selon l'énoncé.
- **Suivi en 2026 (0,5 pt).** Le portefeuille est amorti sur sa durée résiduelle de commercialisation : 1 600 000 / 8 = **200 000 €** par an ; l'impôt différé passif correspondant est repris de 50 000 € ; au 31/12/2026, il s'élève à (1 600 000 – 200 000) × 25 % = **350 000 €**. Les parcelles d'essais, non amortissables, gardent leur écart de 320 000 € et leur impôt différé passif de **80 000 €** tant qu'elles restent dans le groupe.

#### b. Coût d'acquisition et écart d'acquisition (2,5 pts)

- **Frais (0,75 pt).** Dans ses comptes individuels, SEMÉLIANE a passé les honoraires en charges, ce que permet le PCG [V PCG art. 121-5 ; F05 § 1.1], et les a déduits fiscalement. En consolidation, le coût d'acquisition comprend les coûts directement imputables, dont les honoraires de consultants et d'experts externes, **nets de l'économie d'impôt** [V ANC art. 231-2 et 231-3, p. 20 ; F05 § 1.1] : les 176 000 € sont retirés des charges de 2026 et ajoutés au coût des titres pour 176 000 × 75 % = 132 000 €.
- **Coût d'acquisition (0,75 pt)** : 6 380 000 + 132 000 = **6 512 000 €**.
- **Écart d'acquisition (1 pt)** : 6 512 000 – 80 % × 6 640 000 = 6 512 000 – 5 312 000 = **1 200 000 €**, positif, inscrit à l'actif immobilisé, en immobilisations incorporelles, ligne « dont écarts d'acquisition positifs » [V art. 231-9, p. 22 ; art. 231-11, p. 23 ; F05 § 1.3]. Il ne porte que sur la part de l'acquéreur ; les droits des minoritaires sont calculés sur l'actif net réévalué : 20 % × 6 640 000 = 1 328 000 € [V art. 232-1, p. 24 ; F05 § 1.3]. Il ne donne lieu à aucun impôt différé [V art. 272-10, p. 58].

#### c. Durée d'utilisation, amortissement et écritures (3 pts)

**Durée et amortissement (1 pt).** L'entité détermine la durée d'utilisation, limitée ou non, de l'écart d'acquisition par une analyse documentée de l'opération, sur ses aspects techniques, économiques et juridiques ; ce n'est pas une option ; le cycle de vie des produits issus de l'acquisition et les synergies attendues comptent parmi les critères [V ANC art. 231-11 et IR3, p. 23 ; F05 § 1.3 et 9]. Ici, l'écart rémunère un programme de sélection dont les variétés seront commercialisées jusqu'en 2037 et des économies d'essais ; au-delà, les gammes seront renouvelées par SEMÉLIANE Recherche. La durée est **limitée** et déterminée de façon fiable : **12 ans**. Dotation de 2026 : 1 200 000 / 12 = **100 000 €** ; valeur nette au 31/12/2026 : **1 100 000 €**. La dotation figure sur la ligne propre aux écarts d'acquisition, entre le résultat d'exploitation avant et après ces dotations [V IR3 sous art. 231-12, p. 24 ; art. 281-2, p. 67 ; F05 § 1.3] ; elle ne réduit que le résultat part du groupe. Le groupe apprécie en outre, à chaque clôture, s'il existe un indice de perte de valeur [V art. 231-11, p. 23] ; l'énoncé n'en signale aucun.

**Si la durée n'était pas limitée (0,75 pt).** L'écart ne serait **pas amorti** ; sa valeur nette comptable serait comparée à sa valeur actuelle **au moins une fois par exercice**, qu'il existe ou non un indice de perte de valeur, et une dépréciation serait constatée si la valeur actuelle était inférieure, sans reprise possible [V art. 231-11, p. 23 ; F05 § 1.3 et 9]. Une durée limitée mais impossible à déterminer de façon fiable aurait conduit à un amortissement sur 10 ans [V art. 231-11, p. 23]. Le calcul de la valeur actuelle n'est pas demandé.

**C9 (bilan) et C9R (compte de résultat), 0,75 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Concessions et droits similaires (portefeuille de variétés protégées) | 1 600 000 | |
| 2111 Terrains nus (parcelles d'essais) | 320 000 | |
| RST.BOISCHAUT Résultat SEMENCES DU BOISCHAUT (200 000 × 75 %) | 150 000 | |
| 2805 Amortissements des concessions et droits similaires (1 600 000 / 8) | | 200 000 |
| IDP Impôt différé passif (350 000 + 80 000) | | 430 000 |
| RSV.BOISCHAUT Réserves SEMENCES DU BOISCHAUT ((1 600 000 + 320 000) × 75 %) | | 1 440 000 |
| *C9 – Écarts d'évaluation nets d'impôt et amortissement de 2026* | **2 070 000** | **2 070 000** |
| 68111 Dotations aux amortissements des immobilisations incorporelles | 200 000 | |
| CH_ID Produit d'impôt différé (200 000 × 25 %) | | 50 000 |
| RES_CR Résultat | | 150 000 |
| *C9R – Amortissement de l'écart d'évaluation du portefeuille* | **200 000** | **200 000** |

**C10 (bilan) et C10R (compte de résultat), 0,25 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261 Titres de participation SEMENCES DU BOISCHAUT (176 000 × 75 %) | 132 000 | |
| RST.SEMELIANE Résultat SAS SEMÉLIANE | | 132 000 |
| *C10 – Incorporation des frais nets d'impôt au coût des titres* | **132 000** | **132 000** |
| 695 Impôts sur les bénéfices (économie d'impôt incorporée au coût des titres) | 44 000 | |
| RES_CR Résultat | 132 000 | |
| 6226 Honoraires | | 176 000 |
| *C10R – Annulation des frais d'acquisition des titres* | **176 000** | **176 000** |

**C11 (bilan) et C11R (compte de résultat), 0,25 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| RST_G Résultat consolidé – part du groupe | 100 000 | |
| AMO_EA Amortissements de l'écart d'acquisition SEMENCES DU BOISCHAUT | | 100 000 |
| *C11 – Amortissement de 2026 de l'écart d'acquisition* | **100 000** | **100 000** |
| DOT_EA Dotations aux amortissements et dépréciations des écarts d'acquisition | 100 000 | |
| RES_CR Résultat | | 100 000 |
| *C11R – Dotation de 2026 au compte de résultat* | **100 000** | **100 000** |

(Écriture C11 présentée après l'élimination des titres C12, qui inscrit l'écart d'acquisition à l'actif.)

---

### 1.8 Partage des capitaux propres et mise en équivalence (7 pts)

#### a. Tableaux de partage au 31/12/2026 (2,5 pts)

**GRAINES DU GÂTINAIS (1,25 pt)**

Réserves retraitées : 3 580 000 + 60 000 (dividende de BEAUCERONNE, C6) – 45 000 (marge d'ouverture nette, C4) = **3 595 000 €** ; résultat retraité : 780 000 – 60 000 – 18 000 = **702 000 €** (0,5).

| | Total | Groupe (70 %) | Intérêts minoritaires (30 %) |
|---|---:|---:|---:|
| Capital | 1 500 000 | 1 050 000 | 450 000 |
| Réserves retraitées | 3 595 000 | 2 516 500 | 1 078 500 |
| **Capitaux propres retraités hors résultat** | **5 095 000** | **3 566 500** | **1 528 500** |
| Élimination des titres (prix payé en 2020) | | – 2 660 000 | |
| **Réserves consolidées** | | **906 500** | |
| Résultat retraité de 2026 | 702 000 | 491 400 | 210 600 |
| **Intérêts minoritaires au 31/12/2026** (avant la quote-part de BEAUCERONNE) | | | **1 739 100** |

(Partage et titres : 0,5 ; résultat et minoritaires : 0,25.) Les titres, payés 70 % des capitaux propres de 2020 sans écart d'évaluation, ne laissent aucun écart d'acquisition : les réserves consolidées sont 70 % des réserves retraitées accumulées depuis l'acquisition, 70 % × (3 595 000 – 2 300 000) = 906 500 €. Les titres BEAUCERONNE que détient la filiale font partie de ses capitaux propres partagés ; leur remplacement par une valeur d'équivalence est traité en b.

**SEMENCES DU BOISCHAUT (1,25 pt)**

Réserves retraitées : 3 400 000 + 1 440 000 (écarts d'évaluation nets) = 4 840 000 € ; résultat retraité : 720 000 – 150 000 (amortissement net du portefeuille) = **570 000 €** (0,25).

| | Total | Groupe (80 %) | Intérêts minoritaires (20 %) |
|---|---:|---:|---:|
| Capital | 1 800 000 | 1 440 000 | 360 000 |
| Réserves (2 900 000 + résultat de 2025 affecté 500 000) | 3 400 000 | 2 720 000 | 680 000 |
| Écarts d'évaluation nets d'impôt différé (à l'acquisition) | 1 440 000 | 1 152 000 | 288 000 |
| **Capitaux propres retraités hors résultat** | **6 640 000** | **5 312 000** | **1 328 000** |
| Élimination des titres (coût d'acquisition) | | – 6 512 000 | |
| Écart d'acquisition (inscrit à l'actif) | | + 1 200 000 | |
| **Réserves consolidées** | | **0** | |
| Résultat retraité de 2026 | 570 000 | 456 000 | 114 000 |
| **Intérêts minoritaires au 31/12/2026** | | | **1 442 000** |

(Capitaux propres retraités : 0,25 ; titres, écart et réserves nulles : 0,25 ; résultat et minoritaires : 0,5.) Acquise le 01/01/2026, la société n'apporte aucune réserve consolidée. Sa contribution au résultat part du groupe est de 456 000 – 100 000 = **356 000 €**.

#### b. Mise en équivalence de BEAUCERONNE (2,5 pts)

**Écart d'acquisition de 2020 (0,5).** Chaque détenteur a payé 600 000 € pour 20 % de capitaux propres de 2 400 000 €, soit 480 000 € : écart de 120 000 € chacun, **240 000 €** au total, présenté comme un écart d'acquisition d'intégration globale [V ANC art. 262-2, p. 49 ; F05 § 4], donc reclassé hors des titres avant leur remplacement par la valeur d'équivalence. Amorti sur 10 ans : 24 000 € par an, dont 12 000 € sur l'écart de SEMÉLIANE (groupe) et 12 000 € sur celui de GRAINES DU GÂTINAIS (70 % groupe, 30 % minoritaires). Au 31/12/2026, sept annuités : amortissements cumulés 168 000 €, valeur nette **72 000 €**. Les dotations figurent sur la ligne « résultat net lié aux entités mises en équivalence » [V art. 262-3, p. 49 ; F14 § 1.3].

**Tableau (2 pts : valeur d'équivalence 0,5 ; partage des réserves 0,5 ; partage du résultat 0,5 ; titres par détenteur et part des minoritaires 0,5)**

| | Total (40 %) | Groupe (34 %) | Minoritaires de GRAINES DU GÂTINAIS (6 %) |
|---|---:|---:|---:|
| Capitaux propres au 31/12/2026 hors résultat (1 000 000 + 2 150 000 = 3 150 000) | 1 260 000 | 1 071 000 | 189 000 |
| Titres hors écart d'acquisition : SEMÉLIANE 480 000 (100 % groupe) ; GRAINES DU GÂTINAIS 480 000 (70 % / 30 %) | – 960 000 | – 816 000 | – 144 000 |
| Réserves avant amortissement de l'écart (quote-part de 750 000 de réserves accumulées depuis 2020) | 300 000 | 255 000 | 45 000 |
| Amortissements de l'écart de 2020 à 2025 (6 × 24 000) | – 144 000 | – 122 400 | – 21 600 |
| **Réserves consolidées** | **156 000** | **132 600** | **23 400** |
| Résultat de 2026 (500 000) | 200 000 | 170 000 | 30 000 |
| Dotation de 2026 à l'amortissement de l'écart | – 24 000 | – 20 400 | – 3 600 |
| **Résultat net lié à BEAUCERONNE** | **176 000** | **149 600** | **26 400** |
| **Titres mis en équivalence** : 40 % × 3 650 000 | **1 460 000** | | |
| Écart d'acquisition net (240 000 – 168 000) | 72 000 | | |

La valeur d'équivalence est calculée au pourcentage de **contrôle** (40 %) : les titres de GRAINES DU GÂTINAIS sont remplacés en totalité, et la part du gain qui revient à M. PERDRIAUX (30 % de la participation indirecte, soit 6 %) est portée dans les intérêts minoritaires, selon le manuel. Contrôle : titres mis en équivalence 1 460 000 + écart net 72 000 – titres éliminés 1 200 000 = 332 000 € = réserves 156 000 + résultat 176 000. Les actifs et passifs identifiables de BEAUCERONNE avaient une valeur d'entrée égale à leur valeur comptable : aucun écart d'évaluation ; l'écart d'acquisition, lui, est pris en compte, avec son amortissement passé (`JUR-G03`). Aucun résultat interne n'étant compris dans les actifs du groupe, aucune autre élimination n'est nécessaire [V art. 262-4, p. 49-50 ; F04 R14].

#### c. Écritures (2 pts)

**C12 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM Capital SEMENCES DU BOISCHAUT | 1 800 000 | |
| RSV.BOISCHAUT Réserves retraitées (3 400 000 + 1 440 000) | 4 840 000 | |
| RST.BOISCHAUT Résultat retraité | 570 000 | |
| EA Écart d'acquisition SEMENCES DU BOISCHAUT | 1 200 000 | |
| 261 Titres de participation (6 380 000 + 132 000) | | 6 512 000 |
| RSV_M Intérêts minoritaires – capital et réserves (20 % × 6 640 000) | | 1 328 000 |
| RST_G Résultat consolidé – part du groupe (80 % × 570 000) | | 456 000 |
| RST_M Intérêts minoritaires – résultat (20 % × 570 000) | | 114 000 |
| *Élimination des titres SEMENCES DU BOISCHAUT, écart d'acquisition et partage* | **8 410 000** | **8 410 000** |

**C13 (bilan, 0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM Capital GRAINES DU GÂTINAIS | 1 500 000 | |
| RSV.GATINAIS Réserves retraitées | 3 595 000 | |
| RST.GATINAIS Résultat retraité | 702 000 | |
| 261 Titres de participation GRAINES DU GÂTINAIS | | 2 660 000 |
| RSV_G Réserves consolidées – part du groupe | | 906 500 |
| RSV_M Intérêts minoritaires – capital et réserves (30 % × 5 095 000) | | 1 528 500 |
| RST_G Résultat consolidé – part du groupe (70 % × 702 000) | | 491 400 |
| RST_M Intérêts minoritaires – résultat (30 % × 702 000) | | 210 600 |
| *Élimination des titres GRAINES DU GÂTINAIS et partage (70 % / 30 %)* | **5 797 000** | **5 797 000** |

**C14 à C16R (BEAUCERONNE, 1 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| EA Écart d'acquisition BEAUCERONNE | 240 000 | |
| 261 Titres BEAUCERONNE détenus par SEMÉLIANE | | 120 000 |
| 261 Titres BEAUCERONNE détenus par GRAINES DU GÂTINAIS | | 120 000 |
| *C14 – Reclassement de l'écart d'acquisition compris dans le coût des titres* | **240 000** | **240 000** |
| RSV_G Réserves consolidées – part du groupe ((12 000 + 8 400) × 6) | 122 400 | |
| RSV_M Intérêts minoritaires – réserves (3 600 × 6) | 21 600 | |
| RST_G Résultat consolidé – part du groupe | 20 400 | |
| RST_M Intérêts minoritaires – résultat | 3 600 | |
| AMO_EA Amortissements de l'écart d'acquisition BEAUCERONNE (240 000 × 7/10) | | 168 000 |
| *C15 – Amortissements de l'écart d'acquisition, 2020 à 2026* | **168 000** | **168 000** |
| TME Titres mis en équivalence (40 % × 3 650 000) | 1 460 000 | |
| 261 Titres BEAUCERONNE détenus par SEMÉLIANE (600 000 – 120 000) | | 480 000 |
| 261 Titres BEAUCERONNE détenus par GRAINES DU GÂTINAIS (600 000 – 120 000) | | 480 000 |
| RSV_G Réserves consolidées – part du groupe (34 % × 750 000) | | 255 000 |
| RSV_M Intérêts minoritaires – réserves (6 % × 750 000) | | 45 000 |
| RST_G Résultat consolidé – part du groupe (34 % × 500 000) | | 170 000 |
| RST_M Intérêts minoritaires – résultat (6 % × 500 000) | | 30 000 |
| *C16 – Mise en équivalence des titres BEAUCERONNE* | **1 460 000** | **1 460 000** |
| QP_MEE Résultat net lié aux entités mises en équivalence (dotation 2026) | 24 000 | |
| RES_CR Résultat | | 24 000 |
| *C15R – Dotation de 2026 de l'écart d'acquisition au compte de résultat* | **24 000** | **24 000** |
| RES_CR Résultat | 200 000 | |
| QP_MEE Résultat net lié aux entités mises en équivalence (40 % × 500 000) | | 200 000 |
| *C16R – Quote-part de résultat de BEAUCERONNE* | **200 000** | **200 000** |

La ligne « résultat net lié aux entités mises en équivalence » s'établit à 200 000 – 24 000 = **176 000 €**, dont 26 400 € reviennent aux minoritaires de GRAINES DU GÂTINAIS.

---

### 1.9 Passage aux capitaux propres consolidés (3 pts)

**Principe.** L'intégration globale cumule les comptes des entités consolidées après retraitements, élimine les opérations internes et partage les capitaux propres entre le groupe et les intérêts minoritaires ; la mise en équivalence substitue aux titres la quote-part des capitaux propres [V ANC art. 221-2 et 221-4, p. 18-19 ; F03 § 3]. Le tableau fait ce chemin pour les capitaux propres de l'ensemble.

**Tableau (2 pts : rattachement des opérations aux phases 1 ; montants 1)**

| Phase | Opération (question, écriture) | Effet sur les capitaux propres de l'ensemble |
|---|---|---:|
| 0. Cumul des comptes individuels | Capitaux propres des cinq sociétés intégrées globalement (annexe 1.9) | 65 990 000 |
| 1. Homogénéisation des méthodes | Frais d'établissement de SEMÉLIANE Recherche (1.4, C1) : réserves – 216 000, résultat + 54 000 | – 162 000 |
| | Droits et frais de l'entrepôt de SEMÉLIANE Distribution (1.5, C2) | + 105 570 |
| | Frais d'acquisition des titres SEMENCES DU BOISCHAUT, nets d'impôt (1.7 b, C10) | + 132 000 |
| 2. Évaluation de l'entité acquise | Écarts d'évaluation nets de SEMENCES DU BOISCHAUT (1 440 000) et amortissement net de 2026 (– 150 000) (1.7 a, C9) | + 1 290 000 |
| 3. Élimination des opérations internes | Marges sur stocks (1.6 a, C4) : réserves – 45 000, résultat – 18 000 | – 63 000 |
| | Ventes et achats internes (C3), dividendes (C5, C6 : transfert du résultat aux réserves), soldes réciproques et chèque en transit (C7, C8) | 0 |
| 4. Élimination des titres, écart d'acquisition et partage | Titres des quatre filiales intégrées : 2 000 000 + 3 000 000 + 2 660 000 + 6 512 000 (1.8, C12, C13) | – 14 172 000 |
| | Écart d'acquisition de SEMENCES DU BOISCHAUT net d'amortissement : 1 200 000 – 100 000 (C11, C12) | + 1 100 000 |
| | Partage entre le groupe et les minoritaires | 0 |
| 5. Mise en équivalence | Titres BEAUCERONNE éliminés (C14, C16) | – 1 200 000 |
| | Titres mis en équivalence (C16) | + 1 460 000 |
| | Écart d'acquisition net de BEAUCERONNE : 240 000 – 168 000 (C14, C15) | + 72 000 |
| **Capitaux propres de l'ensemble consolidé** | | **54 552 570** |

**Partage (1 pt)**

| | Montant |
|---|---:|
| Intérêts minoritaires : GRAINES DU GÂTINAIS 1 739 100 + SEMENCES DU BOISCHAUT 1 442 000 + BEAUCERONNE (23 400 + 26 400) 49 800 | **3 230 900** |
| dont résultat : 210 600 + 114 000 + 26 400 | 351 000 |
| **Capitaux propres part du groupe** : 54 552 570 – 3 230 900 | **51 321 670** |

Contrôle par les contributions des sociétés :

| Société | Réserves consolidées | Résultat net part du groupe |
|---|---:|---:|
| SAS SEMÉLIANE | 26 800 000 + 280 000 + 60 000 (C5, C6) = 27 140 000 | 4 260 000 – 340 000 (C5, C6) + 132 000 (C10) = 4 052 000 |
| SEMÉLIANE Recherche | 140 000 – 216 000 (C1) = – 76 000 | 260 000 + 54 000 = 314 000 |
| SEMÉLIANE Distribution | 4 600 000 | 1 150 000 + 105 570 = 1 255 570 |
| GRAINES DU GÂTINAIS | 906 500 | 491 400 |
| SEMENCES DU BOISCHAUT | 0 | 456 000 – 100 000 = 356 000 |
| BEAUCERONNE | 132 600 | 149 600 |
| **Total** | **32 703 100** | **6 618 570** |

Capital de SEMÉLIANE 12 000 000 + réserves consolidées 32 703 100 + résultat 6 618 570 = **51 321 670 €**. Les titres de SEMÉLIANE Recherche et de SEMÉLIANE Distribution, souscrits à la création pour la valeur de leur capital, n'apportent aucun écart ; leurs réserves retraitées reviennent en totalité au groupe. Le cumul ne serait pas un point de départ correct sans les phases 1 et 2 : on partage des capitaux propres **retraités** et **réévalués** (`JUR-G01`).

---

### 1.10 Documents de synthèse (6 pts)

#### a. Extrait du compte de résultat consolidé de 2026 (3 pts)

Modèle par nature du règlement ANC [V art. 281-2, p. 67 ; F14 § 1.3].

| Poste | Calcul | Montant |
|---|---|---:|
| Résultat d'exploitation avant dotations aux amortissements et dépréciations des écarts d'acquisition (0,75) | 9 380 000 + 72 000 (C1R) + 144 000 – 3 240 (C2R) – 24 000 (C4R) – 200 000 (C9R) + 176 000 (C10R) ; ventes internes (C3) sans effet | 9 544 760 |
| Dotations aux amortissements et dépréciations des écarts d'acquisition (0,25) | SEMENCES DU BOISCHAUT (C11R) | – 100 000 |
| Résultat d'exploitation après dotations aux amortissements et dépréciations des écarts d'acquisition | | 9 444 760 |
| Charges et produits financiers (0,25) | 180 000 – 280 000 (C5R) – 120 000 (C6R) | – 220 000 |
| Charges et produits exceptionnels | cumul, sans retraitement | – 40 000 |
| Impôts sur les résultats (0,75) | exigibles : 2 350 000 + 44 000 (C10R) = 2 394 000 ; différés : 18 000 (C1R) + 35 190 (C2R) – 6 000 (C4R) – 50 000 (C9R) = – 2 810 (produit net) | – 2 391 190 |
| **Résultat net des entités intégrées** | | **6 793 570** |
| Résultat net lié aux entités mises en équivalence (0,5) | 200 000 (C16R) – 24 000 (C15R) | 176 000 |
| **Résultat net de l'ensemble consolidé** (0,5 pour les trois dernières lignes) | | **6 969 570** |
| Intérêts minoritaires | 210 600 + 114 000 + 30 000 – 3 600 | – 351 000 |
| **Résultat net (part du groupe)** | | **6 618 570** |

- L'impôt de 44 000 € (économie d'impôt sur les frais d'acquisition) est un impôt exigible : en consolidation, l'économie est incorporée au coût des titres et non au résultat.
- La dotation à l'amortissement de l'écart d'acquisition de BEAUCERONNE ne figure pas sur la ligne des écarts d'acquisition des entités intégrées, mais dans le résultat net lié aux entités mises en équivalence [V art. 262-3, p. 49], ventilé dans l'annexe [V art. 282-29, 2, p. 86 ; F14 § 1.3].
- Contrôle : le résultat part du groupe égale le total des contributions de la question 1.9 (6 618 570 €). Les lignes « résultat par action » sont facultatives pour un groupe dont les titres ne sont pas négociés [V art. 281-2, note (4), p. 67 ; F14 § 1.4] et ne sont pas demandées.

#### b. Annexe consolidée (1,5 pt)

L'annexe forme un tout avec le bilan et le compte de résultat ; elle ne donne que les informations significatives et présente les chiffres de l'exercice précédent [V art. 111-4, p. 8 ; art. 282-1, p. 74 ; F14 § 1.1 et 1.4].
- **Entrée de SEMENCES DU BOISCHAUT dans le périmètre (0,75)** : date (01/01/2026), pourcentage acquis (80 %), méthode (intégration globale), prix et frais, effets de l'entrée sur les principaux postes du bilan et du compte de résultat ; liste des sociétés consolidées, avec les pourcentages de contrôle et d'intérêt et les méthodes, BEAUCERONNE comprise (influence notable à 40 %) [V art. 282-3 à 282-8, intitulés ; F14 § 1.4 ; S pour le contenu].
- **Écart d'acquisition (0,75)** : calcul (coût de 6 512 000 €, frais nets d'impôt compris ; actif net réévalué de 6 640 000 € ; écarts d'évaluation du portefeuille de variétés et des parcelles), durée d'utilisation limitée de 12 ans et analyse qui la fonde, dotation de 100 000 € et valeur nette de 1 100 000 € ; méthode de l'écart d'acquisition de BEAUCERONNE (amorti sur 10 ans, valeur nette 72 000 €, dotation comprise dans le résultat des entités mises en équivalence) [V art. 282-19 à 282-30, intitulés ; art. 282-29, 2, p. 86 ; F14 § 1.4].

#### c. Deux différences de présentation en IFRS (1,5 pt, 0,75 par différence)

Pour l'exercice 2026, la présentation relèverait d'IAS 1 ; IFRS 18 ne s'applique qu'aux exercices ouverts à compter du 01/01/2027 et n'est pas appliquée par anticipation [V règlement (UE) 2026/338 ; F14 § 0]. Deux différences parmi :
- les **participations ne donnant pas le contrôle** (1 739 100 + 1 442 000 + 49 800 €) seraient présentées **au sein des capitaux propres**, séparément des capitaux propres attribuables aux propriétaires de la mère [V IAS 1 § 54 q) ; IFRS 10 § 22 ; F14 § 4], alors qu'en ANC les intérêts minoritaires forment une rubrique distincte ;
- l'écart d'acquisition n'étant pas amorti en IFRS [F05 § 2] (question 1.2), le compte de résultat ne comporterait aucune ligne de dotation aux écarts d'acquisition : aucun poste n'est imposé pour les pertes de valeur du goodwill [V F05 § 5 ; F14 § 4] ;
- le goodwill de BEAUCERONNE serait **inclus dans la valeur de la participation** mise en équivalence [V IAS 28 § 32 a) ; F05 § 5], et non présenté parmi les écarts d'acquisition ;
- aucun produit ni charge ne pourrait être présenté comme extraordinaire [V IAS 1 § 87 ; F14 § 4] : la rubrique « charges et produits exceptionnels » du modèle ANC n'aurait pas d'équivalent ; un état du résultat net et des autres éléments du résultat global serait présenté [V F14 § 4] ; le bilan distinguerait les éléments courants et non courants [V IAS 1 § 60 ; F14 § 4].

---

### Réponses tolérées
- **1.1** : seuils des grands groupes cités sans la condition des deux exercices consécutifs, si le candidat constate qu'ils sont largement dépassés ; transformation de la SAS évoquée sans incidence sur la note.
- **1.2** : définition de l'actif tirée du seul cadre de 2018 ; identifiabilité non mentionnée, si le contrôle des droits légaux est expliqué.
- **1.3 a** : colonne des minoritaires laissée vide pour BEAUCERONNE, si le candidat indique que 6 % de sa quote-part revient indirectement aux minoritaires de GRAINES DU GÂTINAIS.
- **1.4** : écritures de bilan présentées en deux temps (annulation du brut et des amortissements, puis impôt différé), si les montants sont justes.
- **1.5** : frais affectés en totalité au bâtiment, si le candidat l'écrit comme hypothèse : – 0,25 (le manuel impose la répartition) ; amortissement calculé sur 12 mois : – 0,25.
- **1.6 a** : élimination de la marge présentée en deux écritures (ouverture et clôture), si les réserves, le résultat et l'impôt différé sont justes.
- **1.6 c** : chèque enregistré au compte 512 plutôt qu'au compte 5112, ou au crédit d'un compte de dette chez SEMÉLIANE Distribution (annulation de son règlement), si les soldes réciproques éliminés sont égaux et le résultat inchangé (`JUR-F08`).
- **1.8 b** : écart d'acquisition de BEAUCERONNE laissé dans la valeur des titres mis en équivalence (présentation des IFRS), si l'écart et son amortissement sont calculés : – 0,25 ; valeur d'équivalence présentée au seul pourcentage d'intérêt (34 % × 3 650 000 = 1 241 000 €), si le candidat montre la part des minoritaires de GRAINES DU GÂTINAIS dans ses tableaux : – 0,5.
- **1.8 c** : écritures C14 à C16 regroupées en une seule écriture de bilan, si elle est équilibrée.
- **1.9** : frais d'acquisition des titres rattachés à la phase d'élimination des titres ; écarts d'évaluation présentés avec les retraitements d'homogénéisation ; autre découpage en phases, si chaque opération du dossier y figure et que le total est juste.
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (erreur non sanctionnée deux fois).

### Erreurs fréquentes
- **Obligation et référentiel** : exemption du 1° retenue au motif que SEMÉLIANE est contrôlée par le fonds, sans vérifier que celui-ci la consolide ; IFRS présentées comme obligatoires dès aujourd'hui ; anciens seuils de consolidation cités.
- **Cadre conceptuel** : définitions récitées sans application aux deux éléments du cas ; utilisateurs limités aux actionnaires ; variétés protégées confondues avec l'écart d'acquisition (`JUR-F07`).
- **Périmètre** : pourcentage de contrôle de BEAUCERONNE calculé en multipliant (20 % + 14 % = 34 %) ; contrôle exclusif retenu à 40 % alors qu'un associé détient 60 % ; intérêt arrêté à 20 %, la chaîne indirecte étant oubliée.
- **Frais d'établissement** : dotation de 2026 maintenue ; totalité de l'écart portée en résultat de 2026 ; impôt différé omis ou inversé ; tableau des incidences non présenté (`JUR-F05`, `JUR-G06`).
- **Droits de mutation** : frais affectés au seul bâtiment, ou amortis sur le terrain ; amortissement sur une année pleine ; impôt différé actif au lieu de passif.
- **Opérations internes** : marge calculée sur le prix de vente (420 000 × 25 %) au lieu du coût ; marge d'ouverture oubliée ou portée en résultat ; élimination imputée au seul groupe ; dividende de GRAINES DU GÂTINAIS éliminé pour 400 000 € (part du minoritaire comprise) ; dividende reçu par GRAINES DU GÂTINAIS oublié ; écart de 72 000 € traité comme une erreur à corriger en résultat.
- **Acquisition** : frais d'acquisition omis ou retenus pour leur montant brut (`JUR-G02`) ; portefeuille de variétés non réévalué parce qu'il ne figurait pas au bilan ; impôt différé omis sur le portefeuille ou sur le terrain ; amortissement de l'écart d'acquisition partagé avec les minoritaires ; écart non amorti malgré la durée limitée.
- **Mise en équivalence** : écart d'acquisition de 2020 et ses amortissements ignorés (`JUR-G03`) ; titres de GRAINES DU GÂTINAIS oubliés ; part des minoritaires de GRAINES DU GÂTINAIS attribuée au groupe ; dividende de BEAUCERONNE compté à la fois dans le résultat des détenteurs et dans la quote-part ; écritures non équilibrées (`JUR-F04`).
- **Processus et compte de résultat** : partage effectué sur les capitaux propres individuels non retraités (`JUR-G01`) ; dotation de l'écart d'acquisition de BEAUCERONNE portée sur la ligne des entités intégrées ; impôts différés non distingués de l'impôt exigible ; montants sans calcul (`JUR-F02`).

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 a) Qualification, renonciation et référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 1 |
| 2.1 b) Contrôle et mode d'évaluation des apports | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 1,5 |
| 2.1 c) Régime fiscal de faveur | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 1,5 |
| 2.2 a) Actif net apporté, composition, quotes-parts rémunérée et non rémunérée | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 1,5 |
| 2.2 b) Valeurs unitaires, parité et droits du fondateur | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1 |
| 2.2 c) Soulte demandée, plafond légal, conseil et solution retenue | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 3 |
| 2.2 d) Augmentation de capital, prime, répartition du capital, équité | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1,5 |
| 2.3 a) Boni : calcul, décomposition et analyse | `1.2.e` Calculer et analyser le boni ou mali de fusion | 2,5 |
| 2.3 b) Sort fiscal du boni | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 0,5 |
| 2.4 a) Augmentation de capital, soulte et réalisation des apports chez AUTOCARS BRIAMONT | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 2,5 |
| 2.4 b) Annulation des titres ÉTANGLÈRE Voyages et boni | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes | 2 |
| 2.4 c) Frais de fusion et avance en compte courant | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 2 |
| 2.4 d) Écritures chez ÉTANGLÈRE Voyages | `1.3.a` Écritures de base ; `1.3.b` Détentions préalables (renonciation) | 2,5 |
| 2.5 Note à la directrice générale | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Analyse de l'opération (4 pts)

**a) Qualification, renonciation et référentiel (1 pt)**
- *Qualification (0,5 pt).* L'opération est une **fusion-absorption** entre deux sociétés commerciales [V PCG art. 710-2, renvoi à C. com. L. 236-1, F01 § 1] : ÉTANGLÈRE Voyages transmet l'ensemble de son patrimoine, actif et passif, à AUTOCARS BRIAMONT (**transmission universelle**) ; elle est **dissoute sans liquidation** et disparaît ; AUTOCARS BRIAMONT rémunère les apports par une **augmentation de capital**, complétée ici d'une soulte en numéraire.
- *Sort des actions détenues par AUTOCARS BRIAMONT (0,25 pt).* AUTOCARS BRIAMONT ne peut pas se remettre ses propres actions : les 8 500 actions ÉTANGLÈRE Voyages qu'elle détient ne sont pas échangées [V C. com. L. 236-3 II 1°, F01 § 5.1]. C'est une **fusion-renonciation** : seules les 1 500 actions de M. CORBINEAU sont rémunérées ; la fraction des apports qui correspond aux 85 % d'AUTOCARS BRIAMONT n'est pas rémunérée, et sa comparaison avec la valeur comptable des titres annulés dégage un boni ou un mali [V PCG art. 745-1, F01 § 5.1]. La dissolution par confusion de patrimoine n'est pas possible : elle suppose un associé unique, alors qu'AUTOCARS BRIAMONT ne détient que 85 % du capital [V C. civ. art. 1844-5, F02 § 1].
- *Référentiel (0,25 pt).* L'opération est enregistrée dans les comptes individuels des deux sociétés selon le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe la valeur d'inscription des apports [V art. 710-1 et 720-1, F01 § 1] ; la parité se calcule, elle, sur les valeurs d'échange fournies [V art. 740-1, F01 § 1].

**b) Contrôle et mode d'évaluation des apports (1,5 pt)**
- *Situation de contrôle (0,5 pt).* AUTOCARS BRIAMONT détient 85 % des droits de vote d'ÉTANGLÈRE Voyages (une voix par action, aucun pacte) : elle la contrôle **de manière exclusive** [V art. 741-2, renvoi à l'art. 211-3 du règlement ANC 2020-01, F01 § 2.1]. L'une des sociétés participantes contrôlant préalablement l'autre, l'opération est réalisée **sous contrôle commun** [V art. 741-1, F01 § 2.1].
- *Règle (0,5 pt).* Sous contrôle commun, les apports sont évalués à la **valeur comptable**, que l'opération soit à l'endroit ou à l'envers : elle ne fait que renforcer un contrôle existant, il convient de ne pas réévaluer [V art. 743-1, tableau, cas 1 et 2, F01 § 2.3]. AUTOCARS BRIAMONT reprend chaque actif et chaque passif pour sa valeur dans les comptes d'ÉTANGLÈRE Voyages au 30/06/2026, avec ses valeurs brutes et ses amortissements [V art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2].
- *Sens de l'opération (0,25 pt).* La famille BRIAMONT, qui vote ensemble, détient 76 % d'AUTOCARS BRIAMONT avant la fusion et 74,38 % après (voir 2.2 d) : elle garde le contrôle de l'absorbante, la fusion est **à l'endroit** [V art. 742-1, F01 § 2.2]. Le sens est sans incidence sur la conclusion.
- *Exception (0,25 pt).* La valeur réelle ne s'imposerait que si l'actif net comptable apporté ne suffisait pas à libérer l'augmentation de capital [V art. 743-3, F01 § 2.4]. Ici l'actif net comptable (1 380 000 €), et même sa seule part rémunérée (207 000 €), dépasse largement l'augmentation de capital (39 200 €, voir 2.2 d) : l'exception ne joue pas. Les valeurs d'échange (2 112 000 € pour ÉTANGLÈRE Voyages) ne servent qu'au calcul de la parité.

**c) Régime fiscal de faveur (1,5 pt)**
- *Application (0,25 pt).* Les deux sociétés sont passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1] ; la fusion relève du régime de l'art. 210 A, qui s'applique sauf option pour le droit commun, à condition qu'AUTOCARS BRIAMONT prenne dans le traité les engagements du 210 A-3 ; elle les prend (annexe 2.4) [V CGI art. 210 A ; BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1 et § 4]. ÉTANGLÈRE Voyages n'a pas de déficit à transférer.
- *Plus-values latentes (0,5 pt).* La valeur d'échange d'ÉTANGLÈRE Voyages excède son actif net comptable de 2 112 000 – 1 380 000 = **732 000 €**. Sous le régime de faveur, les plus-values et profits dégagés sur les éléments apportés **ne sont pas imposés** chez ÉTANGLÈRE Voyages [V CGI art. 210 A-1, F02 § 2] ; en droit commun, la fusion serait traitée comme une cessation d'entreprise et ces plus-values seraient imposées immédiatement [V BOI-IS-FUS-10-10-10 § 1, F02 § 2]. En contrepartie, AUTOCARS BRIAMONT reprend les valeurs fiscales de l'absorbée : les apports étant inscrits à la valeur comptable, avec les valeurs brutes et les amortissements, aucune plus-value n'est à réintégrer sur les autocars et les agencements (engagement d), les amortissements se poursuivent sur les bases d'ÉTANGLÈRE Voyages, et les créances sont reprises à leur valeur fiscale (engagement e) [V CGI art. 210 A-3, F02 § 4].
- *Résultat de la période du 01/01 au 30/06/2026 (0,25 pt).* Il est **imposé immédiatement au nom d'ÉTANGLÈRE Voyages**, quel que soit le régime, par une déclaration spéciale [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2] : l'impôt de 32 000 € est une dette transmise, qu'AUTOCARS BRIAMONT paiera.
- *Provision pour litiges (0,5 pt).* Sa dotation a été déduite ; sous le régime de faveur, elle n'est pas réintégrée lors de la fusion : les provisions de l'absorbée ne sont imposables que si elles deviennent sans objet [V CGI art. 210 A-2, F02 § 2]. AUTOCARS BRIAMONT la reprend à son passif (engagement a) et la reprendra en résultat imposable si le litige se dénoue sans perte [V CGI art. 210 A-3 a, F02 § 4]. En droit commun, elle serait imposée chez ÉTANGLÈRE Voyages au moment de la fusion [V BOI-IS-FUS-10-10-20 § 10, F02 § 2].

---

### 2.2 Apports, parité, actions attribuées et soulte (7 pts)

**a) Actif net apporté, composition et quotes-parts (1,5 pt)**
- *Actif net apporté (0,5 pt)* = actifs – provision et dettes = 2 238 000 – 858 000 = **1 380 000 €**. Contrôle par les capitaux propres d'ÉTANGLÈRE Voyages : 600 000 + 60 000 + 590 000 + 34 000 + 96 000 = 1 380 000 €.
- *Composition (0,5 pt)* :

| Élément apporté | Valeur brute | Amortissements | Valeur apportée |
|---|---:|---:|---:|
| Autocars de tourisme | 3 120 000 | 1 560 000 | 1 560 000 |
| Agencements de l'agence | 180 000 | 96 000 | 84 000 |
| Matériel de bureau et informatique | 48 000 | 30 000 | 18 000 |
| Clients | 136 000 | | 136 000 |
| Disponibilités | 440 000 | | 440 000 |
| **Total de l'actif apporté** | **3 924 000** | **1 686 000** | **2 238 000** |
| Provision pour litiges | | | – 24 000 |
| Emprunt bancaire | | | – 240 000 |
| Avance en compte courant d'AUTOCARS BRIAMONT | | | – 120 000 |
| Fournisseurs | | | – 154 000 |
| Acomptes reçus des clients | | | – 212 000 |
| Dettes sociales | | | – 54 000 |
| État – TVA à décaisser | | | – 22 000 |
| État – impôt sur les bénéfices de la période | | | – 32 000 |
| **Actif net comptable apporté** | | | **1 380 000** |

- *Quotes-parts (0,5 pt)* : quote-part **rémunérée**, celle de M. CORBINEAU : 15 % × 1 380 000 = **207 000 €** ; quote-part **non rémunérée**, celle d'AUTOCARS BRIAMONT : 85 % × 1 380 000 = **1 173 000 €** [F01 § 5.1].

**b) Valeurs unitaires, parité et droits du fondateur (1 pt)**
- *Valeurs unitaires (0,25 pt)* : AUTOCARS BRIAMONT 14 400 000 / 90 000 = **160 €** ; ÉTANGLÈRE Voyages 2 112 000 / 10 000 = **211,20 €**.
- *Parité (0,25 pt)* : 211,20 / 160 = 1,32 = **33 / 25**, soit 33 actions AUTOCARS BRIAMONT pour 25 actions ÉTANGLÈRE Voyages [V méthode du corrigé du sujet zéro, F01 § 4].
- *Actions à rémunérer (0,25 pt)* : 10 000 – 8 500 = **1 500** actions, celles de M. CORBINEAU (renonciation, voir 2.1 a).
- *Droits du fondateur (0,25 pt)* : 1 500 × 33 / 25 = **1 980 actions** AUTOCARS BRIAMONT, d'une valeur de 1 980 × 160 = 316 800 € = 1 500 × 211,20.

**c) Soulte demandée, plafond légal, conseil et solution retenue (3 pts)**
- *Contrainte légale (0,25 pt).* La soulte en espèces ne peut pas dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-1, F01 § 4].
- *Demande de M. CORBINEAU (0,75 pt).* Pour 1 900 actions, il lui manque 1 980 – 1 900 = 80 actions de droits, payées 80 × 160 = **12 800 €**. Plafond : 10 % × 1 900 × 20 = **3 800 €**. La soulte le dépasse de plus de trois fois : la demande **n'est pas conforme à la loi** et ne peut pas être retenue.
- *Calcul du nombre minimal (1 pt).* Pour n actions, la soulte vaut (1 980 – n) × 160 et le plafond 2 n ; la condition (1 980 – n) × 160 ≤ 2 n donne n ≥ 316 800 / 162 = 1 955,56, soit au moins **1 956 actions**. Le plus petit multiple de 10 qui respecte la contrainte, retenu par le traité (annexe 2.4), est **1 960 actions**.
- *Conseil à Mme BRIAMONT (0,5 pt).* Chaque action attribuée en moins augmente la soulte de sa valeur (160 €) et abaisse en même temps le plafond de 10 % de son nominal (2 €) : il faut attribuer presque toutes les actions auxquelles le fondateur a droit. Mme BRIAMONT doit expliquer à M. CORBINEAU que la loi limite la part en numéraire à 2 € par action attribuée, soit 1,25 % de leur valeur (2 / 160) : il ne peut pas obtenir à la fois un nombre rond à la centaine et un complément important en espèces ; elle lui propose donc 1 960 actions, comme le prévoit le traité.
- *Solution retenue (0,5 pt).* Soulte : (1 980 – 1 960) × 160 = **3 200 €** ; plafond : 10 % × 1 960 × 20 = **3 920 €** ; la soulte est **légale** (81,63 % du plafond). Contrôle : à 1 950 actions, la soulte (4 800 €) dépasserait le plafond (3 900 €).
- *Pour aller plus loin (sans points).* D'autres solutions conformes à la loi existent : appliquer la parité exacte (1 980 actions, sans soulte), ce qui évite tout décaissement ; si M. CORBINEAU veut disposer de trésorerie, céder ensuite une partie de ses actions à la famille BRIAMONT ou aux salariés actionnaires, hors de la fusion.

**d) Augmentation de capital, prime, répartition du capital et équité (1,5 pt)**
- *Augmentation de capital et prime (0,5 pt).* Augmentation de capital : 1 960 × 20 = **39 200 €** ; prime de fusion avant toute imputation = apport rémunéré – augmentation de capital – soulte = 207 000 – 39 200 – 3 200 = **164 600 €** [F01 § 4 et § 9]. La prime se calcule sur la valeur comptable de l'apport rémunéré, valeur d'inscription des apports, et non sur sa valeur d'échange (316 800 €).
- *Répartition du capital (0,5 pt)* — 90 000 + 1 960 = 91 960 actions :

| Actionnaire | Actions avant | % avant | Actions après | % après |
|---|---:|---:|---:|---:|
| Mme Agnès BRIAMONT et sa famille | 68 400 | 76,00 % | 68 400 | 74,38 % |
| Cadres et salariés | 21 600 | 24,00 % | 21 600 | 23,49 % |
| M. Hervé CORBINEAU | – | – | 1 960 | 2,13 % |
| **Total** | **90 000** | **100 %** | **91 960** | **100 %** |

  La famille BRIAMONT garde la majorité des droits de vote, et donc le contrôle.
- *Équité (0,5 pt).* Pour M. CORBINEAU : 1 960 × 160 + 3 200 = 313 600 + 3 200 = **316 800 €** = valeur de ses 1 500 actions (1 500 × 211,20) [V méthode du corrigé du sujet zéro, F01 § 4]. Pour les actionnaires d'AUTOCARS BRIAMONT : sa valeur comprend déjà la participation de 85 % (85 % × 2 112 000 = 1 795 200 €) ; la fusion lui apporte les 15 % restants (316 800 €) contre 1 960 actions et 3 200 € de trésorerie : sa valeur devient 14 400 000 + 316 800 – 3 200 = 14 713 600 €, soit 14 713 600 / 91 960 = **160 €** par action, comme avant. Aucun des deux groupes ne s'enrichit au détriment de l'autre.

---

### 2.3 Boni de fusion (3 pts)

**a) Calcul, décomposition et analyse (2,5 pts)**
- *Quote-part non rémunérée (0,25 pt)* : 85 % × 1 380 000 = **1 173 000 €** [V PCG art. 745-1, F01 § 5.1].
- *Résultat d'annulation (0,5 pt)* : 1 173 000 – 748 000 (valeur comptable des 8 500 actions annulées) = **+ 425 000 €** : l'actif net reçu à hauteur de la participation excède sa valeur comptable, c'est un **boni** [V art. 745-2, F01 § 5.2 ; annexe 2.5].
- *Résultats accumulés depuis l'acquisition et non distribués (0,75 pt).* Depuis le 15 janvier 2019, ÉTANGLÈRE Voyages n'a reçu aucun apport et n'a distribué aucune réserve antérieure à l'acquisition (annexe 2.2) : la variation de ses capitaux propres ne provient que de ses résultats, diminués des dividendes. Résultats accumulés et non distribués = capitaux propres au 30/06/2026 – capitaux propres au 15/01/2019 = 1 380 000 – 960 000 = **420 000 €**. L'incorporation de 200 000 € de réserves au capital en 2022 a déplacé des réserves vers le capital sans changer le total : il ne faut pas comparer les seules réserves (780 000 – 560 000 = 220 000 €), ce qui oublierait les 200 000 € incorporés. Contrôle : les résultats de 2019 au 30/06/2026 ont totalisé 420 000 + 360 000 (dividendes versés) = 780 000 €.
- *Part en résultat financier (0,5 pt)* : 85 % × 420 000 = **357 000 €**. Ce sont les bénéfices dégagés par ÉTANGLÈRE Voyages depuis qu'AUTOCARS BRIAMONT la contrôle, qu'elle a conservés au lieu de les distribuer : AUTOCARS BRIAMONT en a déjà reçu sa part distribuée en dividendes (85 % × 360 000 = 306 000 €) ; la fusion lui fait recueillir le reste.
- *Part en capitaux propres et analyse (0,25 pt)* : 425 000 – 357 000 = **68 000 €**. Elle ne provient pas de l'activité d'ÉTANGLÈRE Voyages depuis 2019 : elle correspond à l'écart entre la quote-part des capitaux propres acquise en 2019 et le prix payé, 85 % × 960 000 – 748 000 = 816 000 – 748 000 = 68 000 €. AUTOCARS BRIAMONT a payé ses actions moins que leur valeur comptable, parce que le prix tenait compte du renouvellement prochain des autocars (annexe 2.2).
- *Comptes (0,25 pt).* Le PCG ne prévoit pas de compte « boni de fusion » [V liste des comptes, F01 § 5.2]. Par convention, la part en résultat est portée au compte **768 Autres produits financiers** et la part en capitaux propres au compte **1042 Primes de fusion** (annexe 2.4) [F01 § 5.2, convention de rédaction]. Écriture A3 en 2.4 b.

La fusion étant comptabilisée à la valeur comptable, le boni ne tient pas compte de l'écart de 732 000 € entre la valeur d'échange d'ÉTANGLÈRE Voyages et son actif net comptable (voir 2.1 c).

**b) Sort fiscal du boni (0,5 pt)**
- *Régime de faveur (0,25 pt).* La plus-value dégagée par l'absorbante lors de l'annulation des titres qui correspondent à ses droits dans l'absorbée **n'est pas soumise à l'impôt sur les sociétés** [V CGI art. 210 A-1, al. 2, F02 § 2 bis]. La part comptabilisée en résultat financier (357 000 €) est **déduite extra-comptablement** du résultat fiscal 2026 d'AUTOCARS BRIAMONT [V BOI-IS-FUS-10-50-20 § 1, F02 § 2 bis] ; la part inscrite en prime de fusion (68 000 €) ne passe pas par le résultat et n'appelle aucun retraitement.
- *Droit commun (0,25 pt).* La plus-value d'annulation serait **imposable** pour sa totalité, soit 1 173 000 – 748 000 (valeur fiscale des titres) = 425 000 €, y compris les 68 000 € inscrits en capitaux propres ; s'agissant de titres de participation détenus depuis plus de deux ans, elle relèverait du régime des plus-values à long terme de ces titres [V BOI-IS-FUS-10-50-20 § 10, F02 § 2 bis], sous réserve de l'exonération des plus-values à long terme sur titres de participation prévue par ce régime [V BOI-IS-FUS-10-50-20 § 20, remarque].

---

### 2.4 Écritures (9 pts)

**a) Chez AUTOCARS BRIAMONT, le 30 juin 2026 : augmentation de capital, soulte et apports (2,5 pts)**

**A1 — Augmentation de capital et soulte (1 pt).** Seule la quote-part de M. CORBINEAU est rémunérée.

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (15 % × 1 380 000) | 207 000 | |
| 101 Capital (1 960 × 20) | | 39 200 |
| 1042 Primes de fusion | | 164 600 |
| 512 Banques (soulte versée à M. CORBINEAU) | | 3 200 |

**A2 — Réalisation des apports à la valeur comptable (1,5 pt).** Valeurs brutes et amortissements repris (0,75 pt) ; provision et dettes reprises (0,5 pt) ; compte d'apport crédité de tout l'actif net (0,25 pt).

| Compte | Débit | Crédit |
|---|---:|---:|
| 2182 Matériel de transport (autocars de tourisme) | 3 120 000 | |
| 2181 Installations générales, agencements, aménagements divers (agence) | 180 000 | |
| 2183 Matériel de bureau et matériel informatique | 48 000 | |
| 411 Clients | 136 000 | |
| 512 Banques | 440 000 | |
| 28182 Amortissements du matériel de transport | | 1 560 000 |
| 28181 Amortissements des installations générales, agencements, aménagements divers | | 96 000 |
| 28183 Amortissements du matériel de bureau et informatique | | 30 000 |
| 1511 Provisions pour litiges | | 24 000 |
| 164 Emprunts auprès des établissements de crédit | | 240 000 |
| 4551 Associés – Comptes courants – Principal (dette d'ÉTANGLÈRE Voyages reçue) | | 120 000 |
| 401 Fournisseurs | | 154 000 |
| 4191 Clients – Avances et acomptes reçus sur commandes | | 212 000 |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | | 54 000 |
| 4455 Taxes sur le chiffre d'affaires à décaisser | | 22 000 |
| 444 État – Impôts sur les bénéfices (impôt d'ÉTANGLÈRE Voyages pour la période) | | 32 000 |
| 4561 Associés – Comptes d'apport en société | | 1 380 000 |
| **Total** | **3 924 000** | **3 924 000** |

**b) Annulation des titres ÉTANGLÈRE Voyages et boni (2 pts)**

*En quoi la détention préalable modifie les écritures (0,75 pt).* Sans détention préalable, tout l'actif net apporté serait rémunéré : le compte d'apport débité de 1 380 000 € dans l'écriture d'augmentation de capital serait soldé par la seule réalisation des apports. Ici, AUTOCARS BRIAMONT renonce à recevoir des actions pour ses 85 % : l'augmentation de capital ne porte que sur 207 000 € (A1), et le compte d'apport crédité de 1 380 000 € par la réalisation des apports (A2) est soldé, pour la quote-part non rémunérée (1 173 000 €), par l'**annulation des titres** ÉTANGLÈRE Voyages, qui sortent de l'actif ; l'écart est le boni [V art. 745-1 et 745-2, F01 § 5]. Après A1 à A3, le compte 4561 est soldé : 207 000 + 1 173 000 = 1 380 000 €.

**A3 — Annulation des titres et boni (1,25 pt).** Quote-part non rémunérée et sortie des titres (0,5 pt) ; boni ventilé entre résultat financier et capitaux propres (0,75 pt).

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (85 % × 1 380 000) | 1 173 000 | |
| 261 Titres de participation (8 500 actions ÉTANGLÈRE Voyages) | | 748 000 |
| 768 Autres produits financiers (boni : 85 % des résultats accumulés et non distribués) | | 357 000 |
| 1042 Primes de fusion (boni, part en capitaux propres) | | 68 000 |

**c) Frais de fusion et avance en compte courant (2 pts)**
- *Frais de fusion : traitement (0,5 pt).* Les frais de fusion peuvent être inscrits à l'actif en frais d'établissement ou imputés sur les primes de fusion ; en cas d'insuffisance de la prime, ils sont comptabilisés en charges [V PCG art. 212-9, F01 § 7]. AUTOCARS BRIAMONT les impute sur la prime (annexe 2.4), **nets d'impôt** [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 36 000 × 75 % = **27 000 €**, inférieurs à la prime disponible (164 600 €). Absents du résultat comptable, les 36 000 € sont déduits extra-comptablement ; l'économie d'impôt (9 000 €) diminue l'impôt de 2026.

**A4 — Frais de fusion (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (36 000 × 75 %) | 27 000 | |
| 444 État – Impôts sur les bénéfices (36 000 × 25 %) | 9 000 | |
| 512 Banques | | 36 000 |

- *Avance en compte courant : traitement (0,5 pt).* Par la fusion, AUTOCARS BRIAMONT reçoit la dette d'ÉTANGLÈRE Voyages envers elle-même : elle devient à la fois créancière (compte 451) et débitrice (compte 4551 reçu dans l'apport) de la même obligation. La confusion éteint la créance [V C. civ. art. 1349, F01 § 8] : les deux comptes sont soldés l'un par l'autre, sans effet sur le résultat.

**A5 — Extinction de l'avance réciproque (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4551 Associés – Comptes courants – Principal (dette reçue d'ÉTANGLÈRE Voyages) | 120 000 | |
| 451 Groupe (avance consentie à ÉTANGLÈRE Voyages) | | 120 000 |

ÉTANGLÈRE Voyages n'ayant ni provisions réglementées ni subvention d'investissement (annexe 2.2), aucune reconstitution n'est à passer sur la prime.

**d) Chez ÉTANGLÈRE Voyages, le 30 juin 2026 (2,5 pts)**

L'apport étant évalué à la valeur comptable, la créance sur l'absorbante est égale à l'actif net comptable : la fusion ne dégage **aucun résultat** chez ÉTANGLÈRE Voyages.

**A6 — Transmission de l'actif et du passif (1,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – AUTOCARS BRIAMONT, compte d'apport | 1 380 000 | |
| 28182 Amortissements du matériel de transport | 1 560 000 | |
| 28181 Amortissements des installations générales, agencements, aménagements divers | 96 000 | |
| 28183 Amortissements du matériel de bureau et informatique | 30 000 | |
| 1511 Provisions pour litiges | 24 000 | |
| 164 Emprunts auprès des établissements de crédit | 240 000 | |
| 4551 Associés – Comptes courants – Principal (AUTOCARS BRIAMONT) | 120 000 | |
| 401 Fournisseurs | 154 000 | |
| 4191 Clients – Avances et acomptes reçus sur commandes | 212 000 | |
| 43 Sécurité sociale et autres organismes sociaux (dettes sociales) | 54 000 | |
| 4455 Taxes sur le chiffre d'affaires à décaisser | 22 000 | |
| 444 État – Impôts sur les bénéfices | 32 000 | |
| 2182 Matériel de transport (autocars de tourisme) | | 3 120 000 |
| 2181 Installations générales, agencements, aménagements divers (agence) | | 180 000 |
| 2183 Matériel de bureau et matériel informatique | | 48 000 |
| 411 Clients | | 136 000 |
| 512 Banques | | 440 000 |
| **Total** | **3 924 000** | **3 924 000** |

**A7 — Droits des associés sur l'actif net (0,75 pt).** Les capitaux propres sont virés aux comptes des associés, au prorata de leurs actions.

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 600 000 | |
| 1061 Réserve légale | 60 000 | |
| 1068 Autres réserves | 590 000 | |
| 110 Report à nouveau – solde créditeur | 34 000 | |
| 120 Résultat de l'exercice – bénéfice (période du 01/01 au 30/06/2026) | 96 000 | |
| 456 Associés – Opérations sur le capital (AUTOCARS BRIAMONT, 85 %) | | 1 173 000 |
| 456 Associés – Opérations sur le capital (M. CORBINEAU, 15 %) | | 207 000 |
| **Total** | **1 380 000** | **1 380 000** |

**A8 — Partage : remise des actions et de la soulte, renonciation (0,5 pt).** AUTOCARS BRIAMONT remet directement à M. CORBINEAU 1 960 actions nouvelles et la soulte de 3 200 € ; pour sa propre quote-part, elle renonce à recevoir des actions : sa dette d'apport s'éteint avec sa créance d'associée.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital (M. CORBINEAU) | 207 000 | |
| 456 Associés – Opérations sur le capital (AUTOCARS BRIAMONT) | 1 173 000 | |
| 467 Divers comptes débiteurs – AUTOCARS BRIAMONT, compte d'apport | | 1 380 000 |

Après A6 à A8, tous les comptes d'ÉTANGLÈRE Voyages sont soldés.

---

### 2.5 Note à Mme BRIAMONT, directrice générale d'AUTOCARS BRIAMONT (2 pts)

**Capitaux propres juste après la fusion (1 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (90 000 → 91 960 actions de 20 €) | 1 800 000 | + 39 200 | 1 839 200 |
| Primes de fusion | 0 | + 164 600 + 68 000 – 27 000 | 205 600 |
| Réserve légale | 180 000 | | 180 000 |
| Autres réserves | 4 650 000 | | 4 650 000 |
| Report à nouveau | 120 000 | | 120 000 |
| Résultat 2026 : boni porté en résultat financier | 0 | + 357 000 | 357 000 |
| **Total** | **6 750 000** | **+ 601 800** | **7 351 800** |

Contrôle : + 601 800 = actif net reçu (1 380 000) – titres annulés (748 000) – soulte (3 200) – frais nets d'impôt (27 000) ; hausse de 8,92 %. Le résultat de 2026 hors fusion n'est pas compris dans ce tableau. Barème : tableau (0,5), total et contrôle (0,5).

**Résultat, capital et parties prenantes (1 pt)**
- *Résultat comptable et fiscal de 2026 (0,25 pt).* Le boni augmente le résultat financier de **357 000 €** : ce produit est non récurrent, ne s'accompagne d'aucun encaissement et n'est pas imposable ; il est déduit extra-comptablement, comme les 36 000 € de frais imputés sur la prime (économie d'impôt de 9 000 €). Il faudra l'isoler pour apprécier la performance de 2026. À compter du 1er juillet 2026, les résultats de l'agence entrent directement dans ceux d'AUTOCARS BRIAMONT.
- *Capital (0,25 pt).* La famille BRIAMONT passe de 76 % à 74,38 % et garde le contrôle ; les cadres et salariés de 24 % à 23,49 % ; M. CORBINEAU entre au capital avec 2,13 %. La parité étant équitable, l'action vaut toujours 160 €.
- *Créanciers des deux sociétés (0,25 pt).* Ceux d'ÉTANGLÈRE Voyages (fournisseurs, organismes sociaux, État, voyageurs qui ont versé 212 000 € d'acomptes) ont désormais pour débiteur une société bien plus importante. Ceux d'AUTOCARS BRIAMONT partagent son patrimoine avec eux : elle reprend 858 000 € de provision et de dettes, dont 738 000 € envers des tiers (l'avance de 120 000 € est éteinte), pour 2 238 000 € d'actifs nets d'amortissements, dont 440 000 € de disponibilités ; les capitaux propres progressent de 601 800 €.
- *Banque (0,25 pt).* L'emprunt d'ÉTANGLÈRE Voyages (240 000 €) est repris : les emprunts bancaires passent de 7 800 000 € à **8 040 000 €** ; leur rapport aux capitaux propres passe de 1,16 à 8 040 000 / 7 351 800 = **1,09**, mais à 1,15 seulement si l'on retire le boni, produit sans trésorerie. La banque d'ÉTANGLÈRE Voyages a désormais pour débiteur une société qui détient toute la flotte des deux sociétés ; celle d'AUTOCARS BRIAMONT voit la trésorerie de l'agence (440 000 €) rejoindre celle de son client.

---

### Réponses tolérées
- **2.1 b** : sens de l'opération non traité, si la règle de la valeur comptable sous contrôle commun « quel que soit le sens » est énoncée.
- **2.2 b** : parité exprimée en nombre décimal (1,32 action AUTOCARS BRIAMONT pour une action ÉTANGLÈRE Voyages).
- **2.2 c** : 1 956 actions (minimum exact) avec une soulte de 3 840 € (plafond 3 912 €), si le candidat justifie le calcul et indique que le traité impose un multiple de 10 ; dans ce cas, l'item « solution retenue » est compté à moitié. L'item « conseil » est accordé à toute explication juste du lien entre nombre d'actions, soulte et plafond.
- **2.3 b** : en droit commun, « plus-value à long terme exonérée, sauf une quote-part imposée », si le caractère imposable de la totalité du boni (425 000 €) est indiqué.
- **2.3 a** : résultats accumulés calculés par différence des capitaux propres hors capital, à condition d'y ajouter les 200 000 € incorporés au capital.
- **2.4 a et b** : A1 et A3 regroupées en une seule écriture (débit 4561 de 1 380 000 €), ou réalisation des apports passée par masses, dès lors que les valeurs brutes et les amortissements sont distingués ; dettes sociales ventilées entre 421 et 431 ; compte 44551 au lieu de 4455.
- **2.4 b** : un autre compte de produits financiers (classe 76) pour la part du boni en résultat.
- **2.4 c** : frais en deux écritures (1042 / 512 pour 36 000 €, puis 444 / 1042 pour 9 000 €), ou passage par 6226 Honoraires puis transfert sur la prime ; avance inscrite chez AUTOCARS BRIAMONT au compte 2671 ou 4551, et chez ÉTANGLÈRE Voyages au compte 451, si l'écriture d'extinction solde les deux comptes.
- **2.4 d** : tout compte de tiers cohérent pour la créance sur AUTOCARS BRIAMONT ou pour les droits des associés ; regroupement de A7 et A8.
- **2.5** : toute présentation chiffrée et cohérente.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion mal calculée : sur la valeur d'échange de l'apport rémunéré (316 800 – 39 200 – 3 200 = 274 400 €), sur tout l'actif net (1 380 000 – 39 200 – 3 200 = 1 337 600 €), ou sans retrancher la soulte (167 800 €).
- `JUR-R05` Difficulté à s'adapter : renonciation oubliée (13 200 actions émises pour les 10 000 actions ÉTANGLÈRE Voyages) ; résultats accumulés calculés sur les seules réserves, sans tenir compte de l'incorporation de 2022 (85 % × 220 000 = 187 000 € en résultat et 238 000 € en capitaux propres) ; boni inscrit en totalité en résultat ou en capitaux propres.
- `JUR-F07` Annexes mal exploitées : dividendes soustraits une seconde fois de la variation des capitaux propres (85 % × 60 000 = 51 000 € en résultat) ; plafond de la soulte calculé sur le nominal des actions ÉTANGLÈRE Voyages (10 % × 1 500 × 60 = 9 000 €), ou sur la valeur des actions attribuées ; nombre d'actions minimal arrondi à l'inférieur (1 955).
- `JUR-F04` Absence de contrôle d'équilibre des écritures A2 et A6.
- `JUR-F06` Hypothèses non écrites (ordre de calcul de la soulte, comptes du boni).
- Erreurs propres à ce cas : valeur réelle retenue au motif que l'associé minoritaire d'ÉTANGLÈRE Voyages est une personne physique ; boni déclaré imposable sous le régime de faveur ; résultat de fusion constaté chez ÉTANGLÈRE Voyages alors que l'apport est à la valeur comptable ; avance en compte courant laissée au bilan d'AUTOCARS BRIAMONT.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 236-1 ; PCG art. 710-1, 710-2, 720-1, 740-1 | Définition de la fusion, champ du titre VII, inscription des apports, parité indépendante de leur évaluation | [V] p. 81-82 | F01 § 1 |
| C. com. L. 236-3 II 1° ; C. civ. art. 1844-5 | Pas d'échange des titres détenus par l'absorbante ; confusion de patrimoine réservée à l'associé unique | [V] | F01 § 5.1 ; F02 § 1 |
| PCG art. 741-1, 741-2, 742-1, 743-1, 743-3 | Contrôle commun, sens de l'opération, valeur comptable, exception de l'actif net insuffisant | [V] p. 82-85 | F01 § 2 |
| PCG art. 744-2 ; BOI-IS-FUS-10-20-40-20 § 170-180 | Reprise des valeurs comptables, valeurs brutes et amortissements | [V] p. 85 | F01 § 3.2 |
| C. com. L. 236-1 ; corrigé du sujet zéro | Soulte limitée à 10 % du nominal des actions attribuées ; parité réduite et équité | [V] Légifrance ; p. imprimée 214 | F01 § 4 |
| PCG art. 745-1, 745-2 | Quote-part non rémunérée ; boni en résultat financier à hauteur des résultats accumulés non distribués, surplus en capitaux propres | [V] p. 86 | F01 § 5.1 et § 5.2 |
| Comptes 768 et 1042 pour le boni | Aucun compte dédié dans le PCG 2026 : convention de rédaction | [V] absence de compte ; choix = convention | F01 § 5.2 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime de fusion, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion des créances réciproques | [V] | F01 § 8 |
| CGI art. 210 A-1, 210 A-2, 210 A-3, 210 C-1 ; BOI-IS-FUS-10-10-10 § 1, 10 et 20 ; BOI-IS-FUS-10-10-20 § 10 ; BOI-IS-FUS-10-20-30 § 210 et 330 | Régime de faveur : plus-values non imposées, provisions, engagements de l'absorbante, imposition du résultat de la dernière période | [V] | F02 § 1, § 2 et § 4 |
| CGI art. 210 A-1, al. 2 ; BOI-IS-FUS-10-50-20 § 1 et 10 | Boni exonéré sous le régime de faveur (déduction extra-comptable de la part en résultat), imposable en droit commun | [V] texte et BOFiP lus le 15/11/2026 | F02 § 2 bis |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Rotation des signataires d'une EIP pour les deux missions ; professionnels habilités à certifier les informations en matière de durabilité ; fin de la mission en cours, désignation et durée du mandat d'un organisme tiers indépendant, levée du secret | `3.1.a` Cadres d'exercice professionnel ; `3.1.b` Nomination et cessation ; `3.1.c` Principes déontologiques | 4,5 |
| 3.2 Certification des comptes annuels, audit interne, revue contractuelle demandée par l'agent ; comptes annuels et comptes consolidés | `3.2.a` Notion d'audit et typologie des missions | 1,5 |
| 3.3 Risque inhérent et risque lié au contrôle du cycle emprunts et dettes financières ; assertions | `3.2.c` Approche par les risques | 3 |
| 3.4 Utilisation des travaux de l'audit interne avec un extrait de NEP ; procédures sur le cycle | `3.1.d` Référentiel normatif (NEP) ; `3.2.d` Démarche d'audit | 3 |
| 3.5 Refus de communication et demande de ne pas interroger les banques : moyens d'action | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.6 Intérêts courus, ratio, écriture, caractère significatif (seuil spécifique, nature), opinion selon les corrections, parties du rapport | `3.2.e` Portée des opinions ; `3.2.c` Caractère significatif | 3 |
| 3.7 Responsabilités civile, pénale et disciplinaire du certificateur des informations en matière de durabilité | `3.1.e` Mise en cause de la responsabilité | 1,5 |
| 3.8 Norme volontaire, ESRS et plafond de la chaîne de valeur | `3.3.a` Contexte et architecture des normes de durabilité | 3 |
| 3.9 Informations comparatives et erreur d'une période antérieure | `3.3.b` Principes de construction du reporting | 3 |
| 3.10 Objectifs de la mission et assurance limitée ; procédures sur la correction et sur les données des fournisseurs | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4,5 |
| 3.11 Avis sur les informations : conformité avec observation ou réserve ; structure du rapport | `3.4.c` Portée des avis | 1,5 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Signataires, certificateur des informations en matière de durabilité, organisme tiers indépendant (4,5 pts)

**a. Rotation de M. TRÉVALLE (1,5 pt)**
- **Comptes (0,5 pt)** : dans une entité d'intérêt public, le commissaire aux comptes personne physique, et dans une société de commissaires aux comptes l'associé qui signe, ne peut certifier les comptes durant plus de **six exercices consécutifs**, dans la limite de sept années. Il ne peut à nouveau participer à la mission qu'à l'expiration d'un délai de **trois ans** à compter de la clôture du sixième exercice certifié [V L. 821-34 I].
- **Application (0,5 pt)** : M. TRÉVALLE a signé les rapports sur les comptes des exercices 2021 à 2026, soit six exercices consécutifs. **Il ne peut pas signer le rapport sur les comptes de 2027**. Un autre associé du cabinet doit le faire. Mme MARNAY n'a signé que trois exercices (2018 à 2020) et ne signe plus depuis six ans : rien ne s'oppose à ce qu'elle signe [S, application]. Le délai de M. TRÉVALLE court jusqu'au 31/12/2029 : il pourrait revenir sur la mission à compter des comptes de **2030** [S, application].
- **Durabilité (0,5 pt)** : la règle est **distincte** pour la certification des informations en matière de durabilité d'une EIP. La personne qui signe ce rapport ne peut y procéder plus de six exercices consécutifs, dans la limite de sept années, avec le même délai de trois ans [V L. 821-34 II ; L. 821-26]. M. TRÉVALLE a signé ce rapport pour 2024 à 2026, soit trois exercices : **il peut continuer à le signer en 2027**, et jusqu'à l'exercice 2029 au plus [S, application]. Il reste inscrit sur la liste des commissaires aux comptes habilités à certifier ces informations, condition pour signer au nom du cabinet [V L. 821-26].
- Réponse au comité d'audit : l'information est exacte pour les comptes, pas pour la durabilité. Les deux décomptes sont séparés.

**b. Professionnels habilités et conditions d'exercice (1,5 pt)**
- Les informations en matière de durabilité sont certifiées soit par un **commissaire aux comptes** inscrit sur la liste spéciale de la H2A, soit par un **organisme tiers indépendant (OTI)** inscrit sur la liste tenue par la H2A [V L. 232-6-3 III ; L. 821-13 II ; L. 822-1]. Le choix appartient à l'entité : commissaire aux comptes des comptes, autre commissaire aux comptes ou OTI [V FAQ H2A, citée par F13 § 1] (0,25 pt).
- **Commissaire aux comptes** (0,5 pt) : il doit d'abord être inscrit comme commissaire aux comptes (conditions d'honorabilité, stage professionnel, certificat d'aptitude ou diplôme d'expertise comptable, serment) [V L. 821-14, L. 821-23]. Pour la durabilité, il doit en outre avoir accompli au moins **huit mois de stage** auprès d'un commissaire aux comptes ou d'un auditeur habilités pour la durabilité et réussi une **épreuve** sur cette mission [V L. 821-18 I]. Dans une société de commissaires aux comptes, le rapport est signé par un associé, actionnaire ou dirigeant inscrit sur cette liste [V L. 821-26].
- **Organisme tiers indépendant** (0,5 pt) : c'est une **personne morale accréditée** par le comité français d'accréditation [V L. 822-3]. La mission est exercée et le rapport signé par un **auditeur des informations en matière de durabilité**, personne physique associée, dirigeante ou salariée de l'OTI, inscrite sur la liste de la H2A. Conditions : honorabilité, absence de faillite ou d'interdiction, **diplôme de master**, stage d'au moins **huit mois**, réussite de la même épreuve [V L. 822-4]. Il n'exerce qu'au nom d'un seul OTI [V L. 822-6]. L'auditeur n'a donc pas à être commissaire aux comptes.
- **Points communs** (0,25 pt) : l'OTI et ses auditeurs appliquent le code de déontologie des commissaires aux comptes pour cette mission [V L. 822-7] ; ils relèvent de la H2A pour l'inscription, les contrôles et les sanctions [V L. 820-1 ; L. 822-37] ; la rotation de l'auditeur dans une EIP suit la même règle de six exercices [V L. 822-12].

**c. Fin de la mission en cours, désignation, durée et coopération (1,5 pt)**
- **Fin de la mission (0,5 pt)** : le cabinet LISÉRAC a été désigné pour les exercices 2024 à 2029. Le Code ne prévoit pas de révocation par l'assemblée. Le commissaire aux comptes ne peut être **relevé** de sa mission de certification des informations en matière de durabilité, avant son terme, que **par décision de justice**, en cas de **faute ou d'empêchement**. La demande émane notamment de l'organe d'administration, d'actionnaires représentant au moins 5 % du capital, du ministère public ou de l'AMF [V L. 821-50]. Le souhait des administrateurs ne suffit pas, et une erreur de l'entité non relevée ne constitue pas, par elle-même, une faute établie (question 3.7) [S]. Le cabinet ne peut démissionner que pour un motif légitime [V code de déontologie art. 28]. Conclusion : **pas d'OTI dès 2027** ; il pourra être désigné à l'expiration du mandat, par l'assemblée de 2030 qui statuera sur les comptes de 2029 [S, application].
- **Désignation (0,25 pt)** : par l'**assemblée générale ordinaire** [V L. 822-17 al. 1], sur **recommandation du comité d'audit**, adressée au conseil d'administration ; le comité s'assure du respect des conditions d'indépendance [V L. 822-19]. Un suppléant (OTI ou commissaire aux comptes) est désigné si l'OTI ne compte qu'un seul auditeur [V L. 822-17 al. 2].
- **Durée (0,25 pt)** : **six exercices**, soit 2030 à 2035. La limitation à trois exercices n'est ouverte qu'à une société qui désigne un OTI sans y être tenue par la loi ; ce n'est pas le cas d'ÉLASTRIVE [V L. 822-20 al. 1 et 4]. Dans une EIP, un OTI unique ne peut exercer plus de **dix ans** (renouvellement soumis à conditions) [V L. 822-21 I].
- **Coopération (0,5 pt)** : la crainte des administrateurs n'est pas fondée. Le commissaire aux comptes qui certifie les comptes est **libéré du secret professionnel** envers l'OTI qui certifie les informations en matière de durabilité [V L. 821-35 al. 2]. L'OTI peut communiquer au commissaire aux comptes les informations strictement nécessaires à la certification des comptes [V L. 822-2 al. 2]. L'OTI est convoqué aux réunions du conseil qui examinent et adoptent le rapport sur les informations en matière de durabilité [V L. 822-18 al. 2]. Les lignes directrices prévoient des échanges avec les commissaires aux comptes des comptes, notamment lors de la lecture finale, au titre de la connectivité [V LD 2026 § 3 et § 11].

**Réponses tolérées**
- En a., une date de retour exprimée comme « pas avant le 31/12/2029 », sans désigner l'exercice 2030.
- En c., une réponse qui retient la démission du cabinet pour motif légitime comme seule voie amiable, si elle conclut que le désaccord ou le souhait du conseil n'en est pas un.

**Erreurs fréquentes**
- Appliquer une seule rotation aux deux missions et conclure que M. TRÉVALLE doit cesser de signer le rapport sur la durabilité, ou qu'il peut continuer à signer les comptes (`JUR-A05`).
- Croire qu'un OTI doit être commissaire aux comptes, ou que l'assemblée peut révoquer le cabinet à tout moment (`JUR-A01`).
- Proposer un mandat de trois exercices pour une certification imposée par la loi (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-34 I et II ; L. 821-26 | Rotation des signataires d'une EIP : comptes et durabilité, décomptes distincts | [V] ; dates : [S] | F10 § 6 ; F09 § 15 |
| C. com. L. 232-6-3 III ; L. 821-13 II, L. 821-14, L. 821-18 ; L. 822-1, L. 822-3, L. 822-4, L. 822-6, L. 822-7, L. 822-12 | Professionnels habilités ; conditions d'exercice | [V] | F09 § 3.1, § 4.1 ; F13 § 1 |
| C. com. L. 821-50 ; code de déontologie art. 28 | Relèvement judiciaire ; démission | [V] ; application : [S] | F09 § 3.7, § 4.2, § 15 |
| C. com. L. 822-17 à L. 822-21 ; L. 821-35 al. 2 ; L. 822-2 al. 2 ; LD 2026 § 3, § 11 | Désignation, durée, levée du secret, convocation, échanges | [V] | F09 § 4.2-4.3, § 15 ; F13 § 1, § 3 |

### 3.2 Certification, audit interne et revue demandée par l'agent (1,5 pt)

**Les trois interventions (1 pt)**

| Intervention | Qualification | Auteur et indépendance | Objet et conclusion | Destinataire |
|---|---|---|---|---|
| Certification des comptes annuels | **Mission légale** du commissaire aux comptes ; audit externe | Deux commissaires aux comptes désignés par l'assemblée, indépendants de la société | Opinion sur la régularité, la sincérité et l'image fidèle des comptes pris dans leur ensemble, sur la base d'une **assurance raisonnable** | Assemblée générale ; utile à tous les utilisateurs des comptes |
| Revue du processus de financement | **Audit interne** | Direction de l'entité, rattachée au directeur financier : elle n'est pas indépendante de la société | Appréciation d'un processus (janvier à septembre 2026), recommandations ; aucune opinion sur les comptes | Direction et comité d'audit |
| Revue de SORBIAN Conseil | **Audit contractuel** externe | Cabinet choisi par l'agent, en application du contrat | Étendue fixée par le contrat (ratio au 30/06/2026, tableaux de bord de trésorerie) | Agent des banques |

- La certification est fondée sur la loi [V L. 821-2 III, L. 821-53 al. 1]. Elle procure une assurance élevée mais non absolue [V NEP principes § 08] (0,5 pt).
- L'audit interne est une fonction de l'entité, dont le commissaire aux comptes prend connaissance et dont il peut utiliser les travaux (question 3.4) [V NEP audit interne § 1] (0,25 pt).
- La revue de SORBIAN est une intervention contractuelle. Confiée à un commissaire aux comptes, elle serait une **prestation**, et non une mission [V A. 821-55 § 08 ; L. 821-2 IV] (0,25 pt).

**Comptes annuels et comptes consolidés (0,5 pt)**
- La certification des **comptes annuels** porte sur la SA ÉLASTRIVE seule : résultat, situation financière et patrimoine de la société [V L. 821-53 al. 1].
- La certification des **comptes consolidés** porte sur l'ensemble constitué par les entités comprises dans la consolidation (ici avec ÉLASTRIVE Iberia et ÉLASTRIVE Polska). Elle est délivrée notamment après examen des travaux des professionnels qui contrôlent les comptes de ces entités, et fait l'objet d'un rapport distinct [V L. 821-53 al. 2-3 ; NEP rapport § 04].
- Le ratio du crédit syndiqué est calculé sur les comptes annuels : le cycle étudié relève de la certification des comptes annuels. Les particularités techniques de la certification des comptes consolidés ne sont pas attendues.

**Réponses tolérées**
- La qualification de la revue de SORBIAN comme « audit externe contractuel » ou « mission contractuelle » est acceptée si son fondement contractuel et son destinataire sont indiqués.

**Erreurs fréquentes**
- Présenter l'audit interne comme une mission indépendante de l'entité ou la revue de l'agent comme une certification (`JUR-A01`).
- Développer la démarche propre à la certification des comptes consolidés (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-2 III-IV, L. 821-53 ; NEP principes § 08 ; NEP rapport § 04 | Mission légale, assurance raisonnable, comptes annuels et consolidés | [V] | F11 § 1.1-1.2 |
| NEP audit interne § 1 ; A. 821-55 § 08 | Audit interne ; audit contractuel comme prestation | [V] | F11 § 1.2, § 13.2, § 19.1 |

### 3.3 Risque d'anomalies significatives du cycle emprunts et dettes financières (3 pts)

**Évaluation du risque (1 pt)**
- **Risque inhérent élevé (0,5 pt)** :
  - **pression du ratio** : 2,98 au 31/12/2026 pour un plafond de 3,00. La dette financière nette (59 600 000 €) ne peut augmenter que de 400 000 € avant le plafond (3,00 × 20 000 000 = 60 000 000 €). Un dépassement permettrait aux banques d'exiger le remboursement de 83 000 000 €. Le plafond descend à 2,75 fin 2027 et une renégociation est en cours. La direction a donc intérêt à présenter favorablement la dette, les disponibilités et l'EBE. C'est un facteur de risque de biais, voire de fraude [V NEP risques § 02] ;
  - **complexité et changements** : contrat à deux tranches, avenant de 2026, nantissement nouveau, tirages renouvelables dont la période d'intérêts chevauche la clôture, frais d'émission répartis sur la durée du crédit.
- **Risque lié au contrôle (0,25 pt)** : le calcul des intérêts courus n'est ni formalisé ni revu, et la recommandation de l'audit interne ne sera mise en œuvre qu'en 2027. Le directeur financier concentre la négociation, la signature des tirages et la relation avec les banques, alors qu'il porte l'enjeu du ratio. Le responsable comptable prépare l'annexe sans suivre les contrats.
- **Conclusion (0,25 pt)** : le risque d'anomalies significatives est **élevé** au niveau des assertions du cycle et de l'annexe. Il justifie le seuil spécifique de 150 000 € [V NEP caractère significatif § 15-16] et des procédures de substance étendues : plus le risque est élevé, plus les éléments probants doivent être nombreux ou de qualité [V NEP principes § 13].

**Principaux risques et assertions (2 pts ; 0,5 pt par risque pertinent rattaché à la bonne assertion et aux faits de l'annexe ; 0,25 pt si l'assertion manque ou est erronée ; dans la limite de 2 pts)**

| Risque | Assertion | Lien avec les annexes |
|---|---|---|
| Intérêts courus non comptabilisés ou mal calculés à la clôture sur le tirage B2 | **Exhaustivité** des dettes ; **séparation des exercices** et exhaustivité des charges financières | Calcul non formalisé ; période d'intérêts du 01/10/2026 au 31/03/2027 |
| Capital restant dû inexact (tirage omis, remboursement mal daté) | **Existence** et **exhaustivité** des dettes ; **mesure** des flux | Deux tirages et deux remboursements en 2026 |
| Nantissement des titres non mentionné, ou autres engagements omis | Annexe : **exhaustivité**, **réalité et droits et obligations** | Avenant du 30/06/2026 ; projet d'annexe muet |
| Ratio ou échéances mal présentés dans l'annexe (2,98 publié ; 23 000 000 € à moins d'un an) | Annexe : **mesure et évaluation** ; **présentation et intelligibilité** | Ratio calculé par le directeur financier |
| Disponibilités ou EBE présentés favorablement à la clôture | **Existence** des disponibilités ; **séparation des exercices** des charges d'exploitation | Pression du ratio |
| Frais d'émission mal répartis | **Évaluation et imputation** du compte 481 ; **mesure** de la dotation | Répartition linéaire sur 60 mois |

**Réponses tolérées**
- Le classement de l'omission du nantissement sous « exhaustivité » seule.
- Une évaluation du risque lié au contrôle comme « moyen », si les faiblesses relevées sont citées.

**Erreurs fréquentes**
- Lister des risques sans les rattacher aux faits de l'annexe (`JUR-A05`).
- Confondre existence (solde) et réalité (flux), ou omettre la séparation des exercices pour des intérêts courus (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 11-13 ; NEP risques § 02 ; NEP caractère significatif § 15-16 | Risque inhérent, risque lié au contrôle ; facteurs ; seuil spécifique | [V] ; application : [S] | F11 § 4.1-4.2 |
| NEP éléments probants § 9 | Assertions | [V] | F11 § 4.3 |

### 3.4 Utilisation des travaux de l'audit interne et procédures sur le cycle (3 pts)

**a. Utilisation de la revue de l'audit interne (1,5 pt)**
- **Conditions posées par l'extrait (0,5 pt)** : prendre connaissance de la place de l'audit interne et des règles qui assurent l'objectivité de ses auditeurs, de la nature et de l'étendue de ses travaux ; apprécier les qualifications, l'organisation, la documentation et la prise en compte des recommandations par la direction. Pour les travaux utilisés, apprécier s'ils répondent aux besoins de l'audit, s'ils ont été revus et documentés, si une solution a été apportée aux problèmes relevés et si le rapport est cohérent avec les travaux. Conclure enfin sur leur caractère suffisant et approprié, sinon en tirer les conséquences [V NEP audit interne § 3-7].
- **Application (0,5 pt)** :
  - points favorables : directrice certifiée et expérimentée, équipe de quatre auditeurs, programme approuvé par le comité d'audit, programmes de travail et feuilles de travail revues ;
  - **objectivité affaiblie** pour ce processus : l'audit interne est rattaché au directeur financier, qui conduit le processus revu, porte l'enjeu du ratio, fixe la rémunération variable de la directrice et valide l'envoi des rapports ;
  - **problème non résolu** : la recommandation sur les intérêts courus n'est pas mise en œuvre à la clôture ;
  - **étendue insuffisante** : la revue couvre janvier à septembre ; ni le dernier trimestre, ni la clôture, ni le nantissement, ni le ratio au 31/12.
- **Conclusion (0,5 pt)** : le cabinet peut utiliser la revue comme **élément collecté** pour les tirages, les remboursements et les intérêts payés de janvier à septembre. Il doit au préalable examiner les feuilles de travail et réexécuter une partie des contrôles, compte tenu de l'objectivité limitée. Il réalise lui-même les travaux sur le dernier trimestre, les intérêts courus, le ratio au 31/12/2026, le nantissement et l'annexe. L'utilisation de ces travaux ne décharge pas le cabinet : il reste seul responsable de son opinion [S, déduction de NEP audit interne § 1 et § 6-7].

**b. Procédures sur le cycle (1,5 pt ; 0,25 pt par procédure justifiée)**
- **Lecture du contrat, de l'avenant, de l'acte de nantissement et du procès-verbal du conseil du 24/06/2026** : identifier les obligations, les sûretés et les engagements (droits et obligations, exhaustivité de l'annexe).
- **Rapprochement des avis de l'agent et des tableaux d'amortissement avec la comptabilité** : capital restant dû de 83 000 000 € (68 000 000 € pour la tranche A, 15 000 000 € pour le tirage B2) et part à moins d'un an de 23 000 000 € (deux échéances de 4 000 000 € et le tirage B2) (existence, exhaustivité, présentation).
- **Recalcul des intérêts** : charges de 2026 (1 482 000 + 1 404 000 + 205 000 = 3 091 000 €) et intérêts courus au 31/12/2026, tirage par tirage (mesure, séparation des exercices, exhaustivité).
- **Demande de confirmation directe aux quatre banques**, envoyée et reçue par le cabinet : soldes, tirages, taux, sûretés, engagements, éventuels accords sur le ratio (existence, exhaustivité, droits et obligations) [V NEP confirmations § 5 et § 9].
- **Recalcul du ratio** avec les montants audités (dette nette, intérêts courus compris, et EBE) et tests de séparation des exercices sur les disponibilités et les charges d'exploitation autour de la clôture (rapprochements bancaires, décaissements de janvier 2027) (mesure de l'information, existence).
- **Recalcul des frais d'émission** (dotation de 360 000 €, solde de 1 260 000 € au compte 481) et appréciation de la répartition linéaire (évaluation). Également admis : lecture de la correspondance avec les banques, revue des événements postérieurs, déclaration écrite de la direction sur l'exhaustivité des engagements.

**Réponses tolérées**
- Une réponse qui refuse toute utilisation de la revue en raison du rattachement au directeur financier, si ce choix est justifié par l'objectivité et que les procédures propres du cabinet sont présentées : 1 pt sur 1,5.

**Erreurs fréquentes**
- Réciter l'extrait de norme sans l'appliquer aux faits (`JUR-A06`).
- Proposer des procédures sans objectif ni assertion (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP audit interne § 1-7 | Prise de connaissance, conditions d'utilisation, conclusion | [V] ; application : [S] | F11 § 19.1 |
| NEP éléments probants § 9-10 ; NEP confirmations § 5, § 9 | Techniques, assertions, confirmation des tiers | [V] | F11 § 4.3, § 6.2-6.3 |
| PCG art. 212-11 | Répartition des frais d'émission d'emprunt | [V] | F11 § 19.2 |

### 3.5 Refus de communication et demande de ne pas interroger les banques (1,5 pt)

**Droit de communication (0,5 pt)**
- Le commissaire aux comptes opère à toute époque les vérifications qu'il juge opportunes et se fait communiquer **sur place toutes les pièces qu'il estime utiles**, notamment les contrats [V L. 821-60]. C'est lui qui apprécie l'utilité, et non le directeur financier : la correspondance est utile, car elle porte sur le ratio mentionné dans l'annexe, sur un risque de remboursement anticipé et sur d'éventuels engagements nouveaux. L'acte de nantissement l'est aussi.
- Le secret professionnel ne peut lui être opposé, sauf par les auxiliaires de justice [V L. 821-61 al. 3]. Un engagement de confidentialité pris envers les banques ne lui est pas opposable. La crainte d'une fuite est sans fondement : le cabinet est lui-même tenu au secret professionnel [V L. 821-35 al. 1].

**Information auprès des banques (0,5 pt)**
- Le cabinet peut recueillir toutes informations utiles auprès des tiers qui ont accompli des opérations pour le compte de la société. La communication de pièces détenues par ces tiers suppose une décision de justice [V L. 821-61 al. 2].
- La **demande de confirmation** est une technique de contrôle que le cabinet maîtrise : sélection, rédaction, envoi et réception [V NEP confirmations § 9]. Si la direction s'y oppose, le cabinet examine ses motifs. S'ils sont fondés, il met en œuvre des procédures alternatives ; sinon, il en tire les conséquences dans son rapport [V NEP confirmations § 10-12]. Vouloir rester le seul interlocuteur des banques n'est pas un motif fondé.

**Maintien du refus (0,5 pt)**
- **Pénal** : délit d'obstacle (5 ans, 75 000 €) pour le dirigeant ou toute personne au service de la société qui refuse la communication sur place des pièces utiles [V L. 821-6 3°].
- **Opinion** : limitation des travaux, conduisant à une **réserve pour limitation** si ses incidences sont circonscrites, ou à une **impossibilité de certifier** dans le cas contraire [V NEP rapport § 11, § 14].
- **Communication** : le cabinet peut d'abord saisir la direction générale, comme l'a fait M. TRÉVALLE (annexe 3.6). Si le refus était maintenu, il porterait la difficulté à la connaissance du conseil d'administration et du comité d'audit, organes auxquels il communique ses travaux et ses constats [S ; L. 821-63 I].

**Erreurs fréquentes**
- Admettre que la confidentialité justifie le refus, ou au contraire que le cabinet peut exiger des banques la copie de la correspondance sans décision de justice (`JUR-A01`).
- Oublier la conséquence sur l'opinion (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-60, L. 821-61, L. 821-35 al. 1, L. 821-6 3°, L. 821-63 I | Communication, tiers, secret, obstacle, communication aux organes | [V] | F11 § 2, § 13.3 ; F09 § 5 |
| NEP confirmations § 9-12 ; NEP rapport § 11, § 14 | Maîtrise de la confirmation ; refus de la direction ; limitation | [V] | F11 § 6.3, § 8.1 |

### 3.6 Anomalies et opinion sur les comptes annuels de 2026 (3 pts)

**Calculs (0,75 pt)**
- Intérêts courus du tirage B2 d'octobre à décembre 2026 : 15 000 000 × 4,40 % × 3/12 = **165 000 €** (0,25 pt).
- Dette financière nette corrigée : 83 000 000 + 165 000 − 23 400 000 = **59 765 000 €** ; ratio : 59 765 000 / 20 000 000 = 2,988, soit **2,99**, contre 2,98 publié. Le plafond de 3,00 reste respecté ; la marge n'est plus que de 235 000 € (0,25 pt).
- Résultat courant avant impôt corrigé : 10 600 000 − 165 000 = 10 435 000 € ; l'EBE n'est pas modifié, les intérêts étant des charges financières (0,25 pt).

**Écriture de correction (0,5 pt)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 6611 | Intérêts des emprunts et dettes | 165 000 | |
| | 1648 | Intérêts courus sur emprunts auprès des établissements de crédit | | 165 000 |

Libellé : intérêts courus du tirage B2, du 01/10 au 31/12/2026 (écriture X1, équilibrée).

**Caractère significatif (0,75 pt)**
- **Intérêts courus** : 165 000 € représentent 11 % du seuil de signification de 1 500 000 €, mais **dépassent le seuil spécifique** de 150 000 € fixé pour les éléments du ratio. L'anomalie est donc **significative** pour les dettes financières. Elle porte en outre sur un ratio clé et réduit la marge du ratio [V NEP caractère significatif § 15-16 ; NEP anomalies § 14] (0,25 pt).
- **Nantissement** : l'annexe doit indiquer les dettes garanties par des sûretés réelles et l'état des sûretés consenties [V PCG art. 832-16, 836-1]. Le nantissement porte sur 46 000 000 € de titres, soit près d'un tiers des capitaux propres, et garantit 83 000 000 € de dettes. L'omission, sans montant au compte de résultat, est **significative par sa nature** : l'information est nécessaire à l'appréciation de la situation financière [V NEP caractère significatif § 9]. L'argument des concurrents ne dispense pas de l'information (0,25 pt).
- **Autres anomalies** : 240 000 €, sans incidence sur le ratio ; même cumulées avec les intérêts courus (405 000 €), elles restent sous le seuil de signification et ne sont pas significatives (0,25 pt).

**Opinion selon les corrections (1 pt ; 0,25 pt par cas, 0,25 pt pour les parties du rapport)**
- **Les deux anomalies sont corrigées** : **certification sans réserve**. Le cabinet communique les anomalies non corrigées (240 000 €) au conseil et obtient une déclaration écrite à laquelle est joint leur état [V NEP anomalies § 15-17 ; NEP rapport § 08].
- **Seuls les intérêts courus sont corrigés** : **certification avec réserve pour désaccord**, motivée par l'omission du nantissement. L'anomalie est significative, mais ses incidences sont **circonscrites** : la réserve décrit l'information omise (titres des deux filiales, 46 000 000 €, en garantie de 83 000 000 €), ce qui suffit à l'utilisateur. Un refus de certifier ne se justifie pas [V NEP rapport § 09-10]. L'annexe doit alors indiquer le ratio corrigé (2,99), et non 2,98.
- **Aucune correction** : **certification avec réserve pour désaccord**, portant sur deux motifs. Le premier est l'omission du nantissement. Le second est l'absence des intérêts courus : dettes financières et charges financières sous-évaluées de 165 000 €, résultat courant surévalué d'autant, ratio de 2,99 et non de 2,98. Les incidences restent circonscrites et le plafond est respecté : ce n'est pas un refus de certifier.
- **Parties du rapport** : la partie « **Opinion avec réserve** » indique que le cabinet certifie, sous cette réserve, que les comptes sont réguliers et sincères et donnent une image fidèle. La partie « **Fondement de l'opinion avec réserve** » expose les motifs et quantifie leurs incidences. Le conseil d'administration est informé des motifs avant l'émission du rapport [V NEP rapport § 06 ; R. 821-180].

**Réponses tolérées**
- Une réponse qui juge l'anomalie d'intérêts non significative en la comparant au seul seuil général n'obtient pas l'item correspondant. Est acceptée une réponse qui fonde le caractère significatif sur l'incidence sur le ratio (marge réduite à 235 000 €) en plus du seuil spécifique.

**Erreurs fréquentes**
- Apprécier les anomalies par leur seul montant, au regard du seuil général (`JUR-A06`).
- Conclure à un refus de certifier sans examiner si les incidences sont circonscrites (`JUR-A02`).
- Créditer le compte du capital emprunté (164 sans subdivision) ou un compte de trésorerie, ou oublier le libellé (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP caractère significatif § 9, § 15-16 ; NEP anomalies § 14-17 | Seuil spécifique ; nature ; ratio clé ; communication ; déclaration écrite | [V] | F11 § 4.2, § 14.1 |
| NEP rapport § 06-10 ; R. 821-180 | Opinions, réserve pour désaccord, parties du rapport | [V] | F11 § 8 |
| PCG art. 832-16, 836-1 | Dettes garanties par des sûretés réelles ; sûretés consenties | [V] | F11 § 19.2 |

### 3.7 Responsabilité du certificateur des informations en matière de durabilité (1,5 pt)

**Responsabilité civile (0,75 pt)**
- Le commissaire aux comptes est responsable, envers l'entité **et les tiers**, des conséquences dommageables des **fautes et négligences** commises dans l'exercice de sa profession, qui comprend la certification des informations en matière de durabilité [V L. 821-37 al. 1 ; S pour l'application à cette mission]. KERSOLIA, actionnaire, agit comme tiers. Il doit prouver une faute, un préjudice et un lien de causalité [S].
- **Faute** : la mission repose sur une **assurance limitée**. Le cabinet ne garantit pas l'absence d'erreur ; il doit mettre en œuvre des vérifications appropriées. Or le taux de fréquence était une information vérifiée spécifiquement et le changement de logiciel de novembre 2025 figurait dans la prise de connaissance, sans procédure particulière sur ces deux mois. Un manquement aux diligences pourrait donc être discuté ; il revient au juge de l'apprécier [S].
- **Préjudice et lien de causalité** : la perte est éventuelle (« si le cours chute »), alors que le préjudice doit être certain. L'erreur provient de la société, qui établit ses informations, et la décision d'investir de KERSOLIA repose sur de nombreux éléments. Le lien de causalité serait difficile à établir [S].
- Conclusion : le risque existe, mais il est limité à ce stade. Le cabinet est couvert par l'assurance obligatoire des commissaires aux comptes [V R. 821-85].

**Responsabilité pénale (0,5 pt)**
- Le délit de L. 821-9 réprime le fait, pour un commissaire aux comptes, de **donner ou confirmer des informations mensongères** sur la situation de la personne morale (5 ans, 75 000 €) [V L. 821-9]. Il vise toute personne exerçant la profession de commissaire aux comptes, au premier chef M. TRÉVALLE, qui a signé le rapport [V L. 821-9] ; la mise en cause du cabinet comme personne morale n'est pas développée [S].
- C'est un délit intentionnel : il suppose que le commissaire aux comptes ait su que l'information était fausse [S]. Rien n'indique que le cabinet connaissait l'erreur : le délit n'est pas constitué.

**Responsabilité disciplinaire (0,25 pt)**
- La H2A peut sanctionner un manquement aux conditions légales d'exercice, une **négligence grave** ou un fait contraire à l'honneur ou à la probité [V L. 821-70 I]. Les sanctions vont de l'avertissement à la radiation, avec d'éventuelles sanctions pécuniaires [V L. 821-71]. Cette responsabilité est indépendante de l'action civile ; une simple insuffisance de diligences sur un indicateur ne suffit pas, sauf négligence grave [S].

**Réponses tolérées**
- Une réponse qui retient la responsabilité de l'OTI (L. 822-14) au lieu de celle du commissaire aux comptes est acceptée pour 0,25 pt sur la partie civile si les trois conditions sont analysées.
- Une réponse qui envisage aussi la responsabilité pénale du cabinet, personne morale, avec la même conclusion (élément intentionnel absent).

**Erreurs fréquentes**
- Confondre les trois responsabilités et leurs sanctions (dommages-intérêts, sanctions pénales, sanctions disciplinaires) (`JUR-A01`).
- Présenter l'assurance limitée comme une absence de responsabilité, ou l'avis de conformité comme une garantie (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-37 ; R. 821-85 | Responsabilité civile ; assurance | [V] ; conditions : [S] | F09 § 7.1, § 13 |
| C. com. L. 821-9 | Informations mensongères | [V] ; élément intentionnel : [S] | F09 § 7.3 |
| C. com. L. 821-70 I, L. 821-71 | Faute disciplinaire ; sanctions | [V] | F09 § 7.2 |

---

### Partie B – Durabilité (12 points)

### 3.8 Norme volontaire, ESRS et plafond de la chaîne de valeur (3 pts)

**Situation de GOMÉLIS (0,5 pt)**
- PME non cotée de 180 salariés, GOMÉLIS n'est pas tenue de publier des informations en matière de durabilité ; elle n'a donc **pas à appliquer les ESRS** [S, F12 § 10-11]. Les ESRS sont les normes des entreprises soumises à la publication, comme ÉLASTRIVE.

**La norme volontaire (1 pt)**
- Le règlement délégué (UE) 2026/1560 a adopté une **norme volontaire**, issue des travaux de l'EFRAG (« VSME »), que les entreprises non soumises à la publication peuvent appliquer pour publier volontairement des informations en matière de durabilité [V 2026/1560 art. 2]. Elle repose sur la directive comptable, qui prévoit de telles normes pour les entreprises de 1 000 salariés au plus [V dir. 2013/34 art. 29 quater bis].
- Elle comprend un **module de base** et un **module complet** [V 2026/1560, annexe I]. GOMÉLIS peut commencer par le module de base et répondre au questionnaire à partir des informations qu'elle aura établies selon cette norme [S, conseil].

**Différences avec les ESRS (0,75 pt)**
- Les ESRS s'imposent aux entreprises soumises. Elles comprennent des normes **transversales** (ESRS 1, ESRS 2) appliquées avec des normes **thématiques** (environnement, social, gouvernance) ; le contenu de l'état de durabilité découle d'une analyse de **double matérialité** des impacts, risques et opportunités. L'état est publié dans le rapport de gestion et certifié [V ESRS 1 (2026) § 8-10, § 25 ; L. 232-6-3 III].
- La norme volontaire est facultative, structurée en modules et proportionnée aux PME. Elle n'impose ni publication dans un rapport de gestion ni certification [S].

**Plafond de la chaîne de valeur (0,75 pt)**
- Une entreprise soumise ne peut exiger d'une **entreprise protégée** de sa chaîne de valeur, qui ne dépasse pas 1 000 salariés, que les **points de données** de l'annexe II du règlement délégué 2026/1560 : c'est le **plafond de la chaîne de valeur** [V 2026/1560 art. 1, 3 et 4 ; ESRS 1 (2026) § 66]. GOMÉLIS en est une.
- Le plafond s'applique aux **exercices commençant à compter du 01/01/2027** [V 2026/1560, F12 § 4]. Pour l'état de 2027, ÉLASTRIVE ne pourra pas exiger de réponse aux 18 questions qui dépassent la norme volontaire ; elle devra revoir son questionnaire [S, application]. Pour 2026, le plafond ne joue pas encore, mais aucun texte n'oblige GOMÉLIS à répondre : la demande relève de la relation commerciale [S].
- Réponse : GOMÉLIS n'a pas à appliquer les ESRS ; elle peut s'appuyer sur la norme volontaire et limiter ses réponses aux informations qu'elle prévoit.

**Réponses tolérées**
- Une réponse qui indique que le plafond peut déjà guider le questionnaire de 2026, si la date d'application de 2027 est donnée.

**Erreurs fréquentes**
- Affirmer que tout fournisseur d'une entreprise soumise doit appliquer les ESRS (`JUR-A05`).
- Développer le calendrier de la directive ou les seuils d'assujettissement au-delà de ce que demande la question (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Règl. délégué 2026/1560 art. 1-4, annexes I et II ; dir. 2013/34 art. 29 quater bis | Norme volontaire ; modules ; plafond ; date d'application | [V] | F12 § 4 |
| ESRS 1 (2026) § 8-10, § 25, § 66 | Architecture des ESRS ; principes ; plafond | [V] | F12 § 3, § 8 |

### 3.9 Informations comparatives et erreur d'une période antérieure (3 pts)

**Exigences des ESRS (1,25 pt)**
- Pour chaque indicateur quantitatif, l'entreprise publie des **informations comparatives** relatives à la période précédente [V ESRS 1 (2026) § 83]. La définition et le calcul des indicateurs restent **cohérents dans le temps** [V § 84].
- Lorsque les montants comparatifs diffèrent significativement de ceux publiés pour la période précédente, elle indique les **raisons** de ces variations et la **différence** entre le montant publié et le montant révisé [V § 87 a)].
- Elle **corrige les erreurs matérielles** concernant des périodes antérieures en **retraitant les montants comparatifs**, sauf impraticabilité ; l'exigence ne remonte pas avant la première année d'application des ESRS [V § 98]. Une erreur matérielle découverte ultérieurement est corrigée dans l'information comparative ; si ses effets ne peuvent être déterminés pour toutes les périodes présentées, le retraitement part de la première date praticable [V § 99].
- Une **erreur** est une omission ou une inexactitude due à la non-utilisation d'informations fiables, disponibles lorsque l'état a été publié et dont on pouvait raisonnablement attendre la prise en compte. Elle se distingue d'un **changement d'estimation**, dû à des informations nouvelles [V ESRS 1 (2026), AR 46].
- L'indicateur étant défini de la même façon depuis 2024, la dispense transitoire d'informations comparatives ne joue pas [V § 124 ; S, application].

**Qualification (1 pt)**
- Les déclarations d'accidents de novembre et décembre 2025 existaient dans les dossiers du service de santé au travail. Elles n'ont pas été reprises dans l'extraction : c'est une **erreur d'une période antérieure** par omission, et non un changement d'estimation (0,5 pt).
- L'erreur est **matérielle** : l'indicateur est matériel pour ÉLASTRIVE ; l'écart est de 2,8 points ; et il inverse la lecture de la tendance. La série publiée suggérait une amélioration en 2025 (11,4 puis 9,8) suivie d'une dégradation en 2026 (11,9). La série corrigée montre l'inverse (11,4, puis 12,6, puis 11,9). Des investisseurs, comme KERSOLIA, ont fondé des décisions sur ce taux (0,5 pt).

**Ce qu'ÉLASTRIVE doit publier (0,75 pt)**
- Dans l'état de 2026 : le taux de 2026 (11,9) et, en comparaison, le **taux de 2025 retraité (12,6)** ; une note qui indique le montant publié en 2025 (9,8), la **différence** (2,8 points) et l'**origine** de l'erreur. La présentation de la direction du développement durable est conforme.
- Il n'est pas nécessaire de publier à nouveau l'état de 2025 : la correction passe par les informations comparatives [V § 98]. La valeur de 2024 n'est pas concernée.
- La présentation du directeur général, qui conserve 9,8 sans commentaire, ne respecte pas les ESRS (question 3.11).

**Erreurs fréquentes**
- Qualifier la correction de changement d'estimation, ou soutenir qu'une erreur passée n'a pas à être corrigée puisqu'elle a déjà été certifiée (`JUR-A01`).
- Recalculer l'indicateur au lieu d'appliquer les exigences de présentation, ce qui n'est pas demandé (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 83-87, § 98-99, AR 46, § 124 | Comparatifs ; cohérence ; raisons et différence ; correction des erreurs ; définition ; disposition transitoire | [V] ; application : [S] | F12 § 19 |

### 3.10 Objectifs de la mission et procédures (4,5 pts)

**a. Réponse à Mme SOLÈRE (2,5 pts)**
- **Objectifs (0,75 pt)** : le cabinet émet un **avis** sur la conformité : du **processus** mis en œuvre pour déterminer les informations publiées (analyse de double matérialité), y compris la consultation du comité social et économique lorsque l'entité y est soumise ; des **informations publiées** aux exigences légales et aux ESRS ; du respect des exigences de publication de la **taxonomie** ; et, à terme, du **balisage** [V L. 821-54 II ; LD 2026 § 2]. Le rapport de certification est destiné à l'assemblée générale.
- **Pas de garantie des objectifs (0,75 pt)** : la mission ne consiste pas à garantir la viabilité ou la qualité de la gestion [V L. 821-55]. Elle porte sur la conformité de la présentation du plan de transition et des informations publiées, non sur la réalisation future de la réduction de 40 %, qui dépend de décisions et d'événements à venir. La société reste responsable de son plan et de ses informations [S].
- **Assurance limitée et différence avec les comptes (1 pt)** :
  - la mission repose sur une **assurance limitée** : vérifications moindres en nature, en étendue et en durée que pour une assurance raisonnable. La conclusion s'exprime donc sous une **forme négative** : le cabinet indique ne pas avoir relevé d'erreurs, d'omissions ou d'incohérences importantes [V LD 2026, « Niveau d'assurance »]. C'est le seul niveau prévu, l'obligation d'adopter des normes d'assurance raisonnable ayant été supprimée [V dir. 2026/470, consid. 4] ;
  - la certification des comptes repose sur une **assurance raisonnable**, élevée mais non absolue. L'opinion est exprimée sous une **forme positive** : le cabinet certifie que les comptes sont réguliers et sincères et donnent une image fidèle [V NEP principes § 08 ; L. 821-53] ;
  - les avis sur la durabilité sont émis **axe par axe**, avec leur propre vocabulaire (conformité, réserve, non-conformité, impossibilité) ; ils figurent dans un rapport distinct du rapport sur les comptes [V LD 2026 § 17].

**b. Procédures (2 pts)**
- **Correction du taux de 2025 (1 pt ; 0,25 pt par procédure justifiée)** :
  - demander les explications de la direction des ressources humaines et vérifier l'origine de l'erreur : comparaison des extractions de l'ancien et du nouveau logiciel ;
  - rapprocher les accidents avec arrêt de novembre et décembre 2025 des sites de Tours et de Chinon des déclarations conservées par le service de santé au travail, puis vérifier le calcul du taux corrigé ;
  - vérifier que l'erreur ne touche pas d'autres informations issues de la même extraction (autres données sociales de 2025) ni les données de 2026 ;
  - vérifier la présentation : comparatif retraité, montant publié, différence et origine indiqués [V ESRS 1 (2026) § 87 a), § 98] ; communiquer l'erreur au comité d'audit et obtenir la confirmation correspondante dans la lettre d'affirmation [V LD 2026 § 4, § 14].
- **Informations établies à partir des réponses des fournisseurs (1 pt ; 0,25 pt par procédure justifiée)** :
  - prendre connaissance du processus de collecte (questionnaire, relances, contrôles de la direction des achats et de la direction du développement durable) [V LD 2026 § 5] ;
  - vérifier l'exhaustivité de la liste des 55 fournisseurs par rapprochement avec les achats de l'exercice ;
  - inspecter, par sondage, des réponses reçues et les pièces qui les étayent, et apprécier leur cohérence avec les volumes achetés ;
  - apprécier la méthode d'estimation retenue pour les 13 fournisseurs qui n'ont pas répondu (moyennes du secteur, sources) et vérifier que l'état décrit les estimations et leurs limites [S ; F12 § 14].

**Réponses tolérées**
- En a., la mention de l'ISSA 5000 ou de la future norme européenne d'assurance limitée, si elle n'est pas présentée comme applicable en France au 31/12/2026.

**Erreurs fréquentes**
- Affirmer que la certification garantit l'atteinte des objectifs, ou présenter l'assurance limitée comme une assurance raisonnable (`JUR-A01`).
- Proposer des procédures de l'audit des comptes sans les adapter à l'indicateur et aux données des fournisseurs (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; LD 2026 § 2, « Niveau d'assurance », § 17 ; dir. 2026/470 consid. 4 | Objectifs, axes, absence de garantie, assurance limitée, forme négative | [V] ; application : [S] | F13 § 2 ; F09 § 6 |
| NEP principes § 08 ; L. 821-53 | Assurance raisonnable ; certification des comptes | [V] | F11 § 1.1 |
| LD 2026 § 4-5, § 14 ; ESRS 1 (2026) § 87, § 98 | Lettre d'affirmation, prise de connaissance, communication ; présentation de la correction | [V] ; procédures : [S] | F13 § 3 ; F12 § 19 |

### 3.11 Avis sur les informations publiées et structure du rapport (1,5 pt)

**Présentation de la direction du développement durable (0,5 pt)**
- Le comparatif est retraité et l'information requise est donnée : aucune erreur non corrigée ne remet en cause la conformité. Le cabinet émet un **avis de conformité** sur les informations [V LD 2026 § 17].
- Il peut formuler une **observation**, qui attire l'attention du lecteur sur la note expliquant la correction du taux de 2025. Une observation n'est possible qu'avec un avis de conformité, avec ou sans réserve ; elle ne constitue pas une réserve [V LD 2026 § 17]. Le sujet peut aussi figurer parmi les éléments ayant fait l'objet d'une attention particulière.

**Présentation du directeur général (0,5 pt)**
- L'erreur matérielle n'est pas corrigée dans les comparatifs et l'information exigée est omise : erreur non corrigée remettant en cause la conformité des informations.
- Ses incidences sont **clairement circonscrites** à un indicateur, et la réserve peut indiquer la valeur corrigée de 2025 (12,6) : **avis de conformité assorti d'une réserve motivée** [V LD 2026 § 17].
- Ce n'est pas un avis de non-conformité : l'erreur est isolée et circonscrite. Ce n'est pas une impossibilité : aucune limitation des travaux. Une observation ne peut pas remplacer la réserve.

**Structure de la partie du rapport (0,5 pt)**
- Le rapport de certification est adressé à l'**organe appelé à statuer sur les comptes**. Il comprend une partie introductive : qualité du cabinet, informations couvertes, responsabilités respectives, règles déontologiques et lignes directrices appliquées, limites de la mission [V LD 2026 § 17].
- Il comprend ensuite **une partie par axe** : processus, informations, taxonomie (le balisage n'étant pas encore exigible). La partie sur les informations présente la **nature des vérifications**, la **conclusion** (avis, et réserve éventuelle avec son motif), les **observations** éventuelles et les **éléments ayant fait l'objet d'une attention particulière**. Le rapport est daté et signé par M. TRÉVALLE [V LD 2026 § 17 ; L. 821-26].

**Erreurs fréquentes**
- Proposer une observation à la place d'une réserve, ou une non-conformité pour une erreur isolée (`JUR-A02`).
- Présenter le rapport sur la durabilité selon la structure du rapport sur les comptes, sans parties par axe (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17 | Avis, réserve, observation, éléments d'attention particulière, structure par axe | [V] ; qualification : [S] | F13 § 4 |
| C. com. L. 821-26 | Signature par l'associé inscrit | [V] | F09 § 4.3 |
