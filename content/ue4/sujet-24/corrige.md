# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 24

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 25/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.10 | `exercices/ex67_consolidation_anc_holding_reprise_frais_titres_mee` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.8 | `exercices/ex68_fusion_valeur_reelle_detention_prealable_mali_soulte` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.13 | `exercices/ex69_audit_capitaux_propres_sa_directoire_durabilite` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 Entité tenue d'établir les comptes consolidés ; référentiel | `2.1.b` Contexte réglementaire et légal de la consolidation | 2 |
| 1.2 Prudence et neutralité ; réponse au fondateur | `2.1.a` Cadre conceptuel de l'IASB | 2 |
| 1.3 Périmètre, pourcentages et méthodes | `2.1.c` Périmètre de consolidation | 1 |
| 1.4 Mise en équivalence et intégration globale de NOCTAMBRE | `2.1.d` Conséquences des méthodes de consolidation | 1 |
| 1.5 a Règle fiscale, dotations et stock des amortissements dérogatoires | `2.2.b` Retraitements préparatoires (provisions réglementées) | 1,5 |
| 1.5 b Tableau des incidences et écritures d'élimination | `2.2.b` Retraitements préparatoires (provisions réglementées) | 2,5 |
| 1.5 c Incidence sur les capitaux propres ; titres MOUSSES DE L'AVANCE | `2.2.b` Retraitements préparatoires (provisions réglementées) | 1 |
| 1.6 Processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.7 a Coût d'acquisition des titres CASTALÈNE | `2.2.g` Écarts d'évaluation et d'acquisition | 1 |
| 1.7 b Actif net réévalué et écart d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 2,5 |
| 1.7 c Traitement de l'écart d'acquisition ; amortissements de 2025 et 2026 | `2.2.g` Écarts d'évaluation et d'acquisition | 1,5 |
| 1.7 d Écritures : frais, écart d'évaluation, amortissement de l'écart d'acquisition | `2.2.g` Écarts d'évaluation et d'acquisition | 4 |
| 1.8 a Dividendes de 2026 | `2.2.f` Comptes réciproques et résultats internes | 3 |
| 1.8 b Frais de gestion, intérêts et soldes réciproques | `2.2.f` Comptes réciproques et résultats internes | 2 |
| 1.9 a Partage des capitaux propres de CASTALÈNE et écriture | `2.2.h` Partage des capitaux propres | 6 |
| 1.9 b Mise en équivalence de NOCTAMBRE | `2.2.h` Partage des capitaux propres | 4 |
| 1.9 c Partage des capitaux propres de VELDRANE Literie et écriture | `2.2.h` Partage des capitaux propres | 3 |
| 1.10 a Bilan consolidé simplifié | `2.3.a` Documents de synthèse consolidés | 4 |
| 1.10 b Note de l'annexe sur les écarts d'acquisition | `2.3.a` Documents de synthèse consolidés | 1 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `CAP_ELIM` = capital de l'entité, à éliminer ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = intérêts minoritaires (réserves / résultat) ; `EA` = écart d'acquisition ; `AMO_EA` = amortissements de l'écart d'acquisition ; `DOT_EA` = dotations aux amortissements des écarts d'acquisition (compte de résultat) ; `TME` = titres mis en équivalence ; `QP_MEE` = résultat net lié aux entités mises en équivalence ; `IDP` = impôt différé passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat. Le suffixe d'un compte désigne l'entité (`261.HOLDING` : titres détenus par VELDRANE Holding ; `RSV.LITERIE` : réserves de VELDRANE Literie). Toutes les écritures ci-dessous sont équilibrées.

---

### 1.1 Entité tenue d'établir les comptes consolidés (2 pts)

- **VELDRANE Holding (1).** Les sociétés commerciales établissent et publient chaque année des comptes consolidés et un rapport sur la gestion du groupe dès lors qu'elles contrôlent de manière exclusive ou conjointe une ou plusieurs autres entreprises [V C. com. L. 233-16 I ; F03 § 1.1 et § 20.1]. La holding est une SAS, société commerciale par la forme ; elle détient la majorité des droits de vote de VELDRANE Literie (100 %) et de CASTALÈNE (75 %) : elle les contrôle de manière exclusive [V L. 233-16 II 1°] (0,25). Aucune exemption ne joue : l'ensemble qu'elle forme avec ses filiales est un **grand groupe**, puisqu'il dépasse, aux clôtures de deux exercices consécutifs (2025 et 2026), au moins deux des trois seuils (250 salariés, 60 M€ de chiffre d'affaires, 30 M€ de total du bilan) : il les dépasse tous les trois (690 salariés, 124 M€, 135,9 M€ en 2026 ; 655, 117 M€, 128 M€ en 2025) [V L. 233-17 2°, L. 230-2, D. 230-2 ; F03 § 1.1] (0,5) ; et elle n'est pas elle-même incluse dans les comptes consolidés publiés d'une entreprise qui la contrôle (le fonds n'en établit pas ; hypothèse de l'annexe 1.1 pour la société de gestion) [V L. 233-17 1°] (0,25).
- **Le fonds (0,25).** Il détient 64 % de la holding, mais c'est une copropriété de valeurs mobilières sans personnalité morale (annexe 1.1) : ce n'est pas une société commerciale, il n'entre pas dans le champ de l'obligation [V L. 233-16 I ; F03 § 20.1, application S]. C'est donc au niveau de la holding que se situe la tête du groupe consolidé.
- **VELDRANE Literie (0,5).** Elle ne contrôle aucune entreprise : ses 15 % de MOUSSES DE L'AVANCE ne lui donnent ni contrôle ni même influence notable (question 1.3), et la seule influence notable ne ferait pas naître l'obligation [V L. 233-16 I ; F03 § 1.1]. Ancienne société de tête de l'entreprise familiale, elle est aujourd'hui une filiale comprise dans les comptes consolidés de la holding. Même si elle contrôlait une entreprise, elle serait exemptée : contrôlée par la holding qui l'inclut dans ses comptes consolidés publiés, elle n'émet aucun titre admis sur un marché, et aucun associé minoritaire ne peut s'y opposer (holding associée unique) [V L. 233-17 1°].
- **Référentiel (0,25).** Aucun titre du groupe n'est admis aux négociations sur un marché réglementé : les IFRS ne sont pas obligatoires ; le groupe applique le règlement ANC n° 2020-01 et pourrait opter pour les IFRS adoptées par l'Union [V règlement (CE) n° 1606/2002, art. 4 ; L. 233-24 ; F03 § 1.2]. Le choix figure dans le manuel (annexe 1.4).

---

### 1.2 Prudence et neutralité (2 pts)

**Les notions (1,25).**
- Selon le cadre conceptuel révisé en 2018, une information financière utile est pertinente et donne une **image fidèle** de ce qu'elle prétend représenter ; l'image fidèle suppose une information, dans toute la mesure du possible, **complète, neutre et exempte d'erreurs** [V Project Summary, p. 6 ; F03 § 17 et § 20.2]. La **neutralité** est l'absence de parti pris dans le choix ou la présentation de l'information : des états financiers neutres ne sont pas orientés vers un résultat recherché [V IAS 8 § 10 b) iii), « neutres, c'est-à-dire sans parti pris » ; F03 § 12] (0,5).
- La **prudence** est l'exercice de la précaution lorsque des jugements sont portés dans des conditions d'incertitude ; elle **soutient la neutralité** ; elle ne permet **ni de surévaluer ni de sous-évaluer** les actifs, les passifs, les produits ou les charges [V Project Summary, p. 6 ; F03 § 20.2] (0,75 : définition 0,25 ; lien avec la neutralité 0,25 ; symétrie 0,25). En 2018, l'IASB a clarifié le rôle de la prudence [V p. 6]. Puisqu'elle interdit toute sous-évaluation, elle ne permet pas de constituer des réserves de précaution (application, F03 § 20.2).

**Réponse à M. VELDRANE (0,75).** Les amortissements dérogatoires de VELDRANE Literie ne traduisent aucune perte de valeur des titres ni aucune obligation : ils résultent de la seule application de la législation fiscale (déduction en cinq ans des frais d'acquisition des titres MOUSSES DE L'AVANCE) [V F04 R1, § 15]. Les maintenir dans les comptes consolidés « pour les mauvaises années » minorerait délibérément le résultat : c'est un parti pris, contraire à la neutralité, que la prudence n'autorise pas. Le manuel les élimine [V ANC 2020-01, art. 272-1, p. 53] : le stock, net d'impôt, rejoint les réserves consolidées (il reste donc dans les capitaux propres, qui sont la véritable « réserve » du groupe), et seul l'**impôt différé passif** (14 000 € au 31/12/2026, question 1.5), qui représente l'impôt réellement dû lorsque l'avance fiscale se retournera, figure au passif. Les prêteurs et le fonds comparent ainsi les résultats du groupe à ceux d'autres groupes sans biais fiscal.

---

### 1.3 Périmètre et méthodes (1 pt)

| Société | % de contrôle | Nature du lien | Méthode | % d'intérêt du groupe |
|---|---:|---|---|---:|
| VELDRANE Literie | 100 % | Contrôle exclusif | Intégration globale | 100 % |
| CASTALÈNE | 75 % | Contrôle exclusif | Intégration globale | 75 % (minoritaires 25 %) |
| NOCTAMBRE | 35 % | Influence notable | Mise en équivalence | 35 % |
| MOUSSES DE L'AVANCE | 15 % (par VELDRANE Literie) | Ni contrôle ni influence notable | Hors du périmètre ; titres de participation | (15 %) |

Tableau : 0,5.

- **NOCTAMBRE (0,25).** Avec 35 % des droits de vote, l'influence notable est présumée (seuil de 20 %) ; elle est confirmée par la représentation au comité de direction (deux sièges sur six) et par des opérations importantes (60 % des matelas vendus par NOCTAMBRE viennent de VELDRANE Literie) [V ANC 2020-01, art. 211-5 ; F03 § 2]. Il n'y a ni contrôle exclusif (les fondatrices détiennent 65 % et quatre sièges ; aucune majorité ni influence dominante pour la holding) ni contrôle conjoint (aucun accord exigeant l'unanimité : décisions à la majorité simple, sans veto) [V art. 211-3, 211-4]. Mise en équivalence [V art. 221-1, 221-4].
- **MOUSSES DE L'AVANCE (0,25).** 15 % des droits de vote, détenus par une filiale contrôlée exclusivement (on en fait masse : art. 211-6) : en dessous du seuil de présomption, et aucun indice d'influence notable (aucun siège, pas de participation aux décisions, transactions non significatives pour les deux sociétés, pas de dirigeant commun ni de dépendance technique). Elle reste hors du périmètre ; ses titres figurent au bilan consolidé en titres de participation (manuel, annexe 1.4), et son dividende reste dans le résultat consolidé (question 1.8).

---

### 1.4 NOCTAMBRE : mise en équivalence ou intégration globale (1 pt)

**Principe (0,5).** La mise en équivalence substitue à la valeur comptable des titres la quote-part des capitaux propres de NOCTAMBRE, résultat compris [V art. 221-4, p. 19 ; F03 § 3] : ses actifs, ses dettes, ses produits et ses charges ne sont **pas cumulés** avec ceux du groupe. NOCTAMBRE apparaît sur **une ligne de l'actif** (« titres mis en équivalence ») et sur **une ligne du compte de résultat** (« résultat net lié aux entités mises en équivalence ») [V art. 262-3, p. 49 ; art. 281-1, 281-2 ; F14 § 1.2-1.3]. L'intégration globale, réservée au contrôle exclusif, cumulerait chaque poste à 100 % et ferait apparaître des intérêts minoritaires [V art. 221-2]. C'est pourquoi le chiffre d'affaires et la dette bancaire de NOCTAMBRE n'apparaissent pas : le groupe n'en a pas le contrôle.

**Chiffres (0,5).**

| Dans les comptes consolidés de 2026 | Mise en équivalence (retenue) | Intégration globale (pour comparaison) |
|---|---:|---:|
| Actif | une ligne : 1 575 000 (35 % × 4 500 000), au lieu des titres de 1 050 000 | + 18 000 000 d'actifs, poste par poste, diminués de la créance réciproque de VELDRANE Literie (900 000) et des titres NOCTAMBRE éliminés (1 050 000) |
| Emprunts bancaires | 0 | 6 000 000 |
| Chiffre d'affaires | 0 (les ventes de VELDRANE Literie à NOCTAMBRE, 7 400 000, restent dans le chiffre d'affaires consolidé) | + 38 000 000 – 7 400 000 de ventes internes éliminées = + 30 600 000 |
| Résultat | une ligne : 420 000 (35 % × 1 200 000) | 1 200 000, dont 780 000 aux minoritaires |
| Part du groupe dans les capitaux propres de NOCTAMBRE | 1 575 000 | 1 575 000, plus 2 925 000 d'intérêts minoritaires |

Les deux méthodes donnent la **même part du groupe** dans les capitaux propres et dans le résultat ; elles diffèrent par la taille du bilan, l'endettement et le chiffre d'affaires affichés. Les comptes de NOCTAMBRE n'étant pas cumulés, ses achats à VELDRANE Literie n'ont pas de contrepartie à éliminer dans le cumul : seuls les résultats internes compris dans ses actifs le seraient, à hauteur de 35 % [V art. 262-4, p. 49-50 ; application S], et elle n'en détient aucun (annexe 1.7). L'annexe consolidée indique l'activité de NOCTAMBRE et sa contribution aux postes consolidés [V art. 282-24, p. 84 ; F14 § 13].

---

### 1.5 Amortissements dérogatoires sur les frais d'acquisition des titres MOUSSES DE L'AVANCE (5 pts)

#### a. Règle, dotations et stock (1,5 pt)

**Pourquoi des dérogatoires (0,5).** Les frais d'acquisition de titres de participation (droits de mutation, honoraires, commissions, frais d'actes) ne sont pas déductibles l'année où ils sont engagés : ils sont incorporés au prix de revient des titres, et cette fraction **peut être amortie sur cinq ans** à compter de l'acquisition [V CGI art. 209, VII ; F04 § 15]. Les titres de participation ne sont pas amortis dans les comptes : la déduction fiscale n'a pas d'objet comptable, elle est enregistrée en amortissements dérogatoires, provision réglementée [V PCG art. 214-8 ; F04 § 8 et § 15 ; annexe 1.5]. VELDRANE Literie a d'ailleurs retenu la méthode de référence (frais incorporés au coût des titres).

**Calcul (1).** Annuité : 160 000 / 5 = 32 000 €.

| | 2025 (9 mois, depuis le 01/04/2025) | 2026 |
|---|---:|---:|
| Dotation aux amortissements dérogatoires (68725) | 32 000 × 9/12 = **24 000** | **32 000** |
| Stock au 31/12 (compte 145) | **24 000** | **56 000** |

#### b. Incidences de l'élimination et écritures (2,5 pts)

Les écritures passées pour la seule application de la législation fiscale sont éliminées [V ANC 2020-01, art. 272-1, p. 53 ; F04 R1 ; manuel]. Le stock, déduit fiscalement mais non comptabilisé en charges par le groupe, fait apparaître une différence temporaire imposable : impôt différé passif [V art. 272-8, p. 57]. Autre lecture, équivalente : la valeur fiscale des titres (3 000 000 – 56 000) est inférieure à leur valeur consolidée (3 000 000).

| | Ouverture (réserves) | Exercice 2026 (résultat) | Clôture |
|---|---:|---:|---:|
| Avant impôt | + 24 000 | + 32 000 | 56 000 (stock annulé) |
| Impôt différé passif (25 %) | – 6 000 | – 8 000 | IDP 14 000 |
| **Net** | **+ 18 000** | **+ 24 000** | **42 000** |

Tableau : 1 pt.

**C1 (bilan) et C1R (compte de résultat), 1,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 145 Amortissements dérogatoires (stock au 31/12/2026) | 56 000 | |
| RSV.LITERIE Réserves VELDRANE Literie (24 000 × 75 %) | | 18 000 |
| RST.LITERIE Résultat VELDRANE Literie (32 000 × 75 %) | | 24 000 |
| IDP Impôt différé passif (56 000 × 25 %) | | 14 000 |
| *C1 – Élimination des amortissements dérogatoires* | **56 000** | **56 000** |
| CH_ID Charge d'impôt différé (32 000 × 25 %) | 8 000 | |
| RES_CR Résultat | 24 000 | |
| 68725 Dotations aux provisions réglementées – amortissements dérogatoires | | 32 000 |
| *C1R – Annulation de la dotation de 2026* | **32 000** | **32 000** |

#### c. Capitaux propres et titres au bilan consolidé (1 pt)

- **Capitaux propres (0,5).** Dans le bilan individuel, les provisions réglementées (56 000 €) figurent dans les capitaux propres [V PCG art. 821-1 ; F04 § 8]. En consolidation, elles sont réparties entre les réserves (+ 18 000), le résultat (+ 24 000) et un passif d'impôt différé (14 000) : les capitaux propres consolidés sont **inférieurs de 14 000 €** aux capitaux propres individuels de VELDRANE Literie (provisions réglementées comprises), et supérieurs de 42 000 € à ses seuls capital, réserves et résultat. Entièrement détenue, VELDRANE Literie n'a pas de minoritaires : tout revient au groupe.
- **Titres (0,5).** MOUSSES DE L'AVANCE n'est pas consolidée : ses titres restent au bilan consolidé en titres de participation pour **3 000 000 €**, frais compris, valeur des comptes individuels (manuel ; art. 212-3 par analogie, F03 § 2) ; seule l'écriture fiscale est éliminée, les titres ne sont ni amortis ni réévalués.

---

### 1.6 Processus de consolidation (2 pts)

| Étape | Traitements du dossier |
|---|---|
| 1. Retraitements préparatoires : élimination des écritures fiscales | Dérogatoires de VELDRANE Literie (C1, C1R) |
| 2. Homogénéisation et évaluation à l'entrée | Frais d'acquisition des titres CASTALÈNE incorporés au coût, nets d'impôt (C2) ; écart d'évaluation sur l'atelier et son amortissement (C3, C3R) |
| 3. Cumul des comptes retraités | Holding, VELDRANE Literie, CASTALÈNE à 100 % ; NOCTAMBRE non cumulée |
| 4. Éliminations des opérations internes | Dividendes (C5, C5R), frais de gestion, intérêts et soldes réciproques (C6 à C8) |
| 5. Élimination des titres et partage | VELDRANE Literie (C11, 100 %), CASTALÈNE (C9, 75 / 25), écart d'acquisition de CASTALÈNE et son amortissement (C4, C4R) |
| 6. Mise en équivalence | NOCTAMBRE (C10, C10R) |

Tableau : 1 pt. Approche directe : chaque société est consolidée directement dans les comptes de la holding, à partir de ses comptes individuels retraités, avec les pourcentages d'intérêt de la holding [V art. 222-1 ; F03 § 3].

**Dérogatoires avant le partage (0,5).** Le partage répartit des capitaux propres **retraités** entre le groupe et les minoritaires et entre réserves et résultat ; il doit porter sur des comptes débarrassés des écritures fiscales et établis selon les méthodes du groupe. Éliminer après le partage obligerait à corriger chaque part ; ici VELDRANE Literie est à 100 %, mais la même règle vaut pour une filiale à 75 %.

**Les traitements de 2025 de nouveau enregistrés (0,5).** Chaque année, la consolidation repart des comptes individuels, qui ignorent les écritures de consolidation des exercices précédents. Les incidences de 2025 sont donc reprises dans les réserves d'ouverture : stock de dérogatoires de 2025 (C1), frais d'acquisition de CASTALÈNE comptabilisés en charges en 2025 (C2), amortissements de 2025 de l'écart d'évaluation (C3) et de l'écart d'acquisition (C4) ; seules les incidences de 2026 passent en résultat.

---

### 1.7 Acquisition de CASTALÈNE (9 pts)

#### a. Coût d'acquisition (1 pt)

Rémunération remise au vendeur augmentée des coûts directement imputables, nets de l'économie d'impôt [V ANC 2020-01, art. 231-2, 231-3, p. 20 ; F05 § 1.1 ; manuel] : 9 000 000 + 240 000 × (1 – 25 %) = **9 180 000 €** (0,5 pour la règle, 0,5 pour le montant). Hypothèse de l'énoncé : l'économie d'impôt (60 000 €) a été obtenue en 2025 (annexe 1.6 ; F04 § 15).

#### b. Actif net réévalué et écart d'acquisition (2,5 pts)

| Élément au 01/01/2025 | Montant |
|---|---:|
| Capital | 2 000 000 |
| Réserves | 7 600 000 |
| **Capitaux propres à la date d'acquisition** | **9 600 000** |
| Écart d'évaluation de l'atelier (3 800 000 – 2 600 000) | + 1 200 000 |
| Impôt différé passif (1 200 000 × 25 %) | – 300 000 |
| **Actif net réévalué** | **10 500 000** |

Tableau : 1,5 (dont impôt différé 0,5) [V art. 231-9, 232-1, 272-13 ; F05 § 1.2]. **Écart d'acquisition (1)** : 9 180 000 – 75 % × 10 500 000 = 9 180 000 – 7 875 000 = **1 305 000 €** [V art. 231-9 ; F05 § 1.3]. L'ANC ne retient que la part de l'acquéreur : les minoritaires n'ont pas de part de l'écart d'acquisition.

#### c. Traitement de l'écart d'acquisition et amortissements (1,5 pt)

L'analyse documentée conclut à une durée d'utilisation **limitée**, estimée de manière fiable à 9 ans : l'écart est amorti linéairement sur cette durée [V art. 231-11 et IR3, p. 23 ; F05 § 1.3 ; manuel] ; ce n'est pas une option (0,5). Aucun impôt différé sur l'écart d'acquisition [V art. 272-10].

| | 2025 (réserves au 31/12/2026) | 2026 (résultat) | Cumul au 31/12/2026 |
|---|---:|---:|---:|
| Écart d'acquisition : 1 305 000 / 9 | 145 000 | 145 000 | 290 000 (valeur nette 1 015 000) |
| Écart d'évaluation de l'atelier : 1 200 000 / 15 | 80 000 | 80 000 | 160 000 (valeur nette 1 040 000) |
| Impôt différé sur l'amortissement de l'écart d'évaluation | – 20 000 | – 20 000 | IDP restant : 1 040 000 × 25 % = 260 000 |
| Amortissement de l'écart d'évaluation net d'impôt | 60 000 | 60 000 | |

Montants : 1 (0,5 par écart). L'amortissement de l'écart d'acquisition revient au seul groupe ; celui de l'écart d'évaluation, qui réduit le résultat de CASTALÈNE, est partagé à 75 / 25. CASTALÈNE étant acquise le 1er janvier, il n'y a ni prorata ni résultat antérieur à l'entrée à isoler.

#### d. Écritures (4 pts)

**Frais d'acquisition (C2), 1 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| 261.HOLDING Titres de participation CASTALÈNE (240 000 × 75 %) | 180 000 | |
| RSV.HOLDING Réserves VELDRANE Holding | | 180 000 |
| *C2 – Frais de 2025 incorporés au coût des titres, nets d'impôt* | **180 000** | **180 000** |

Les honoraires ont réduit le résultat de 2025 de la holding de 180 000 € net d'impôt (240 000 – 60 000) : la correction porte sur les **réserves** ; aucune écriture de compte de résultat en 2026. Les titres retraités (9 180 000) sont éliminés en C9.

**Écart d'évaluation (C3, C3R), 2 pts**

| Compte | Débit | Crédit |
|---|---:|---:|
| 2131 Bâtiments (3 800 000 – 2 600 000) | 1 200 000 | |
| RST.CASTALENE Résultat CASTALÈNE (80 000 × 75 %) | 60 000 | |
| 2813 Amortissements des constructions (2 × 80 000) | | 160 000 |
| IDP Impôt différé passif ((1 200 000 – 160 000) × 25 %) | | 260 000 |
| RSV.CASTALENE Réserves CASTALÈNE (900 000 – 60 000) | | 840 000 |
| *C3 – Écart d'évaluation de l'atelier* | **1 260 000** | **1 260 000** |
| 68112 Dotations aux amortissements des immobilisations corporelles | 80 000 | |
| CH_ID Produit d'impôt différé (80 000 × 25 %) | | 20 000 |
| RES_CR Résultat | | 60 000 |
| *C3R – Amortissement de 2026 de l'écart d'évaluation* | **80 000** | **80 000** |

**Amortissement de l'écart d'acquisition (C4, C4R), 1 pt.** L'écart est inscrit par l'écriture d'élimination des titres (C9, question 1.9).

| Compte | Débit | Crédit |
|---|---:|---:|
| RSV_G Réserves consolidées – part du groupe (amortissement de 2025) | 145 000 | |
| RST_G Résultat consolidé – part du groupe (amortissement de 2026) | 145 000 | |
| AMO_EA Amortissements de l'écart d'acquisition CASTALÈNE | | 290 000 |
| *C4 – Amortissements de l'écart d'acquisition* | **290 000** | **290 000** |
| DOT_EA Dotations aux amortissements des écarts d'acquisition | 145 000 | |
| RES_CR Résultat | | 145 000 |
| *C4R – Dotation de 2026* | **145 000** | **145 000** |

La dotation figure sur la ligne dédiée du résultat d'exploitation consolidé [V IR3 sous art. 231-12, art. 281-2 ; F05 § 1.3].

---

### 1.8 Opérations internes (5 pts)

#### a. Dividendes (3 pts)

Les dividendes intragroupe sont éliminés en totalité [V art. 251-2, p. 45 ; F04 R14] ; ceux d'une société mise en équivalence sont éliminés du résultat de la société qui les reçoit et portés en réserves consolidées [V art. 262-3, p. 49 ; manuel]. Dividendes reçus par la holding : 4 000 000 + 600 000 + 140 000 = **4 740 000 €**.

| Compte | Débit | Crédit |
|---|---:|---:|
| RST.HOLDING Résultat VELDRANE Holding | 4 740 000 | |
| RSV.HOLDING Réserves VELDRANE Holding | | 4 740 000 |
| *C5 – Dividendes reçus des sociétés consolidées (bilan)* | **4 740 000** | **4 740 000** |
| 7611 Revenus des titres de participation | 4 740 000 | |
| RES_CR Résultat | | 4 740 000 |
| *C5R – Même élimination au compte de résultat* | **4 740 000** | **4 740 000** |

Écritures : 1,5. Le dividende provient des résultats de 2025 des filiales, déjà compris dans les réserves consolidées : le laisser dans le résultat de 2026 de la holding le compterait deux fois.

**Ce qui n'est pas éliminé (1,5 : 0,5 par point).**
- **Part de la famille fondatrice (200 000 €).** Elle est versée à des associés extérieurs au groupe : c'est une sortie de trésorerie réelle de l'ensemble consolidé, sans produit correspondant dans une société du groupe. Elle a réduit les réserves de CASTALÈNE, donc les intérêts minoritaires (25 % des réserves), et ne donne lieu à aucune élimination. Seuls les 600 000 € reçus par la holding sont internes.
- **Dividende de MOUSSES DE L'AVANCE (60 000 €).** MOUSSES DE L'AVANCE n'est pas consolidée : ce dividende est un produit reçu d'un tiers, qui reste dans le résultat consolidé (revenu des titres de participation non consolidés).
- **Dividende de NOCTAMBRE (140 000 €).** Il est éliminé du résultat de la holding (C5) et porté en réserves ; dans le même temps, il a diminué les capitaux propres de NOCTAMBRE, donc sa valeur d'équivalence, de 140 000 € (question 1.9 b) : le groupe ne retient que sa quote-part du résultat de NOCTAMBRE.

#### b. Frais de gestion, intérêts et soldes réciproques (2 pts)

Les produits et charges réciproques et les créances et dettes réciproques entre sociétés intégrées globalement sont éliminés en totalité [V art. 251-1, p. 45 ; F04 R14].

| Compte | Débit | Crédit |
|---|---:|---:|
| 706 Prestations de services (VELDRANE Holding) | 1 560 000 | |
| 628 Divers – frais de gestion (VELDRANE Literie) | | 1 200 000 |
| 628 Divers – frais de gestion (CASTALÈNE) | | 360 000 |
| *C6 – Frais de gestion facturés aux filiales, 0,5* | **1 560 000** | **1 560 000** |
| 7617 Revenus des créances rattachées à des participations (holding, 1 500 000 × 3 %) | 45 000 | |
| 6615 Intérêts des comptes courants et des dépôts créditeurs (CASTALÈNE) | | 45 000 |
| *C7 – Intérêts du compte courant, 0,5* | **45 000** | **45 000** |
| 4551 Associés – comptes courants – principal (CASTALÈNE) | 1 500 000 | |
| 401 Fournisseurs (VELDRANE Literie) | 300 000 | |
| 2671 Créances rattachées à des participations – groupe (holding) | | 1 500 000 |
| 411 Clients (holding) | | 300 000 |
| *C8 – Compte courant et créance de frais de gestion, 0,5* | **1 800 000** | **1 800 000** |

**Incidence (0,5).** Aucune sur le résultat consolidé : produit et charge de même montant disparaissent ensemble, et la répartition du résultat entre le groupe et les minoritaires n'est pas modifiée (opération sans incidence sur le résultat, art. 251-1). Les frais de gestion et les intérêts, comme les dividendes, déplacent des ressources des filiales vers la holding pour le service de la dette de reprise, sans rien créer pour l'ensemble. Le compte courant de 1 500 000 € disparaît des créances et des dettes financières consolidées ; la dette bancaire de CASTALÈNE (1 200 000 €) reste.

---

### 1.9 Partage des capitaux propres et mise en équivalence (13 pts)

#### a. CASTALÈNE (6 pts)

Résultat retraité de 2026 : 1 400 000 – 60 000 (amortissement net de l'écart d'évaluation) = **1 340 000 €** (0,5).

| | Total retraité | Groupe (75 %) | Minoritaires (25 %) |
|---|---:|---:|---:|
| Capital | 2 000 000 | 1 500 000 | 500 000 |
| Réserves à l'acquisition | 7 600 000 | 5 700 000 | 1 900 000 |
| Réserves postérieures à l'acquisition (8 000 000 – 7 600 000) | 400 000 | 300 000 | 100 000 |
| Écart d'évaluation net à l'entrée | 900 000 | 675 000 | 225 000 |
| Amortissement de 2025 de l'écart d'évaluation, net | – 60 000 | – 45 000 | – 15 000 |
| **Capitaux propres retraités hors résultat** | **10 840 000** | **8 130 000** | **2 710 000** |
| Élimination des titres (coût d'acquisition) | | – 9 180 000 | |
| Écart d'acquisition inscrit à l'actif | | + 1 305 000 | |
| Amortissement de 2025 de l'écart d'acquisition | | – 145 000 | |
| **Réserves consolidées** | | **110 000** | **2 710 000** |
| **Résultat retraité de 2026** | **1 340 000** | **1 005 000** | **335 000** |
| Amortissement de 2026 de l'écart d'acquisition | | – 145 000 | |
| **Résultat consolidé** | | **860 000** | **335 000** |

Tableau : 3,5 (capitaux propres retraités et parts 1,5 ; titres et écart d'acquisition 1 ; résultat et amortissements 1). Contrôle : la part du groupe dans les réserves postérieures à l'acquisition, nettes de l'amortissement de 2025 de l'écart d'évaluation, est 75 % × (400 000 – 60 000) = 255 000 ; diminuée de l'amortissement de 2025 de l'écart d'acquisition, elle donne 110 000 €. Intérêts minoritaires au 31/12/2026 : 2 710 000 + 335 000 = **3 045 000 €**, écart d'évaluation compris (l'ANC calcule leurs droits sur l'actif net réévalué [V art. 232-1 ; F05 § 1.2]).

**C9 – Élimination des titres et partage (2 pts)**

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM Capital CASTALÈNE | 2 000 000 | |
| RSV.CASTALENE Réserves CASTALÈNE retraitées (8 000 000 + 840 000) | 8 840 000 | |
| RST.CASTALENE Résultat CASTALÈNE retraité (1 400 000 – 60 000) | 1 340 000 | |
| EA Écart d'acquisition CASTALÈNE | 1 305 000 | |
| 261.HOLDING Titres de participation CASTALÈNE (9 000 000 + 180 000) | | 9 180 000 |
| RSV_G Réserves consolidées – part du groupe (8 130 000 – 9 180 000 + 1 305 000) | | 255 000 |
| RSV_M Intérêts minoritaires – capital et réserves (25 % × 10 840 000) | | 2 710 000 |
| RST_G Résultat consolidé – part du groupe (75 % × 1 340 000) | | 1 005 000 |
| RST_M Intérêts minoritaires – résultat (25 % × 1 340 000) | | 335 000 |
| *C9* | **13 485 000** | **13 485 000** |

Avec C4 (amortissements de l'écart d'acquisition), les réserves consolidées issues de CASTALÈNE ressortent à 255 000 – 145 000 = 110 000 € et son résultat part du groupe à 1 005 000 – 145 000 = 860 000 €.

#### b. Mise en équivalence de NOCTAMBRE (4 pts)

**Absence d'écart d'acquisition (0,5).** La holding a souscrit 35 % du capital à sa valeur nominale à la constitution : le coût des titres (1 050 000) égale sa quote-part des capitaux propres à l'entrée (35 % × 3 000 000), sans écart d'évaluation ni d'acquisition [V art. 262-2 ; F05 § 4].

| | 100 % | Quote-part du groupe (35 %) |
|---|---:|---:|
| Capital | 3 000 000 | 1 050 000 |
| Réserves (– 200 000 + 900 000 – 400 000) | 300 000 | 105 000 |
| Résultat de 2026 | 1 200 000 | 420 000 |
| **Capitaux propres au 31/12/2026 / valeur d'équivalence** | **4 500 000** | **1 575 000** |
| Titres éliminés | | – 1 050 000 |
| **Quote-part des réserves** | | **105 000** |
| **Quote-part du résultat** | | **420 000** |

Tableau : 1,5.

**C10 (bilan) et C10R (compte de résultat), 1,5 pt**

| Compte | Débit | Crédit |
|---|---:|---:|
| TME Titres mis en équivalence (35 % × 4 500 000) | 1 575 000 | |
| 261.HOLDING Titres de participation NOCTAMBRE | | 1 050 000 |
| RSV_G Réserves consolidées – part du groupe (35 % × 3 300 000 – 1 050 000) | | 105 000 |
| RST_G Résultat consolidé – part du groupe (35 % × 1 200 000) | | 420 000 |
| *C10 – Mise en équivalence de NOCTAMBRE* | **1 575 000** | **1 575 000** |
| RES_CR Résultat | 420 000 | |
| QP_MEE Résultat net lié aux entités mises en équivalence | | 420 000 |
| *C10R – Quote-part du résultat* | **420 000** | **420 000** |

**Effet du dividende (0,5).** La distribution de 400 000 € a réduit les réserves de NOCTAMBRE, donc la valeur d'équivalence, de 35 % × 400 000 = 140 000 € : sans elle, la valeur serait de 1 715 000 €. Le groupe a reçu ces 140 000 € en trésorerie ; ils sont éliminés du résultat de la holding et portés en réserves (C5). Au total, depuis la constitution, le groupe a retenu 35 % des résultats cumulés de NOCTAMBRE (35 % × 1 900 000 = 665 000 € = 105 000 de réserves + 140 000 de dividende devenu réserves de la holding + 420 000 de résultat), une seule fois [V art. 262-3 ; F05 § 4].

#### c. VELDRANE Literie (3 pts)

Capitaux propres retraités : réserves 36 500 000 + 18 000 = 36 518 000 ; résultat 5 200 000 + 24 000 = 5 224 000 (dérogatoires éliminés, question 1.5). Écart d'acquisition de 2023 : 46 000 000 – 100 % × 34 000 000 = **12 000 000 €**, à durée non limitée : non amorti (manuel, art. 231-11).

| | Total retraité = groupe (100 %) |
|---|---:|
| Capital | 4 000 000 |
| Réserves à l'acquisition (01/07/2023) | 30 000 000 |
| Réserves postérieures (36 500 000 – 30 000 000) | 6 500 000 |
| Stock de dérogatoires d'ouverture, net d'impôt | 18 000 |
| **Capitaux propres retraités hors résultat** | **40 518 000** |
| Élimination des titres | – 46 000 000 |
| Écart d'acquisition inscrit à l'actif | + 12 000 000 |
| **Réserves consolidées** | **6 518 000** |
| **Résultat consolidé** | **5 224 000** |

Tableau : 1,5.

| Compte | Débit | Crédit |
|---|---:|---:|
| CAP_ELIM Capital VELDRANE Literie | 4 000 000 | |
| RSV.LITERIE Réserves VELDRANE Literie retraitées | 36 518 000 | |
| RST.LITERIE Résultat VELDRANE Literie retraité | 5 224 000 | |
| EA Écart d'acquisition VELDRANE Literie | 12 000 000 | |
| 261.HOLDING Titres de participation VELDRANE Literie | | 46 000 000 |
| RSV_G Réserves consolidées – part du groupe | | 6 518 000 |
| RST_G Résultat consolidé – part du groupe | | 5 224 000 |
| *C11 – Élimination des titres VELDRANE Literie et partage, 1,5* | **57 742 000** | **57 742 000** |

Aucun intérêt minoritaire. Les réserves consolidées issues de VELDRANE Literie sont ses réserves accumulées depuis l'acquisition, retraitées.

---

### 1.10 Bilan consolidé et annexe (5 pts)

#### a. Bilan consolidé simplifié au 31/12/2026 (4 pts)

**Capitaux propres part du groupe (préalable)**

| | Réserves consolidées | Résultat part du groupe |
|---|---:|---:|
| VELDRANE Holding, comptes individuels | 3 120 000 | 4 500 000 |
| Frais d'acquisition des titres CASTALÈNE (C2) | + 180 000 | |
| Dividendes reçus éliminés (C5) | + 4 740 000 | – 4 740 000 |
| **Holding retraitée** | **8 040 000** | **– 240 000** |
| VELDRANE Literie (après titres et écart d'acquisition) | + 6 518 000 | + 5 224 000 |
| CASTALÈNE (après titres et écart d'acquisition amorti) | + 110 000 | + 860 000 |
| NOCTAMBRE (mise en équivalence) | + 105 000 | + 420 000 |
| **Total** | **14 773 000** | **6 264 000** |

Capitaux propres part du groupe : 30 000 000 + 14 773 000 + 6 264 000 = **51 037 000 €** ; intérêts minoritaires : **3 045 000 €**, dont résultat 335 000 € ; capitaux propres de l'ensemble 54 082 000 € ; résultat de l'ensemble 6 599 000 €.

| Actif | Montant | Justification (écart avec le cumul) |
|---|---:|---|
| Écarts d'acquisition | 13 015 000 | VELDRANE Literie 12 000 000 (non amorti) + CASTALÈNE 1 305 000 – 290 000 |
| Immobilisations corporelles | 35 540 000 | 34 500 000 + écart d'évaluation de l'atelier 1 200 000 – 160 000 |
| Titres mis en équivalence | 1 575 000 | NOCTAMBRE |
| Titres de participation | 3 000 000 | 59 050 000 – titres éliminés 46 000 000, 9 000 000 et 1 050 000 : reste MOUSSES DE L'AVANCE |
| Créances rattachées à des participations | 0 | compte courant éliminé (1 500 000) |
| Stocks | 11 800 000 | inchangé |
| Clients et comptes rattachés | 19 300 000 | 19 600 000 – 300 000 (frais de gestion dus par VELDRANE Literie) |
| Autres créances | 1 400 000 | inchangé (aucun impôt différé actif) |
| Disponibilités | 8 006 000 | inchangé |
| **Total** | **93 636 000** | |

| Passif | Montant | Justification |
|---|---:|---|
| Capital | 30 000 000 | celui de la holding (capitaux des filiales éliminés) |
| Réserves consolidées | 14 773 000 | tableau ci-dessus |
| Résultat consolidé – part du groupe | 6 264 000 | tableau ci-dessus |
| **Capitaux propres – part du groupe** | **51 037 000** | |
| Intérêts minoritaires | 3 045 000 | CASTALÈNE (dont résultat 335 000) |
| Provisions réglementées | — | éliminées (question 1.5) |
| Emprunts et dettes financières | 25 000 000 | 26 500 000 – compte courant 1 500 000 |
| Fournisseurs et comptes rattachés | 8 580 000 | 8 880 000 – 300 000 |
| Autres dettes (dont impôts différés passifs 274 000) | 5 974 000 | 5 700 000 + IDP 14 000 (dérogatoires) + 260 000 (atelier) |
| **Total** | **93 636 000** | |

Répartition : capitaux propres part du groupe et intérêts minoritaires 1,25 ; écarts d'acquisition 0,5 ; immobilisations corporelles 0,25 ; titres mis en équivalence et titres de participation 0,5 ; éliminations réciproques (créances, clients, dettes) 0,5 ; impôts différés passifs 0,5 ; présentation ANC (intérêts minoritaires hors capitaux propres part du groupe, impôts différés en « dont ») et équilibre 0,5. Le modèle ANC présente les écarts d'acquisition parmi les immobilisations incorporelles (« dont écarts d'acquisition »), les titres mis en équivalence dans l'actif immobilisé et les intérêts minoritaires dans une rubrique distincte des capitaux propres part du groupe [V art. 281-1, p. 66 ; F14 § 1.2].

#### b. Note de l'annexe sur les écarts d'acquisition (1 pt)

D'après l'art. 282-22 [V p. 83 ; F14 § 13] :
- ventilation : écart **amorti** de CASTALÈNE, montant brut 1 305 000, amortissements cumulés 290 000, valeur nette 1 015 000 ; écart **non amorti** de VELDRANE Literie, 12 000 000 ; aucun écart attaché à NOCTAMBRE, entité mise en équivalence (0,5) ;
- **durées d'utilisation** : 9 ans pour CASTALÈNE ; durée non limitée pour VELDRANE Literie, avec les raisons qui la fondent (0,25) ;
- modalités d'affectation des écarts aux actifs ou groupes d'actifs au niveau desquels leur valeur est examinée, modalités de cet examen, principales hypothèses et sensibilité ; aucune perte de valeur constatée (0,25). Les méthodes retenues (frais d'acquisition inclus nets d'impôt, durée déterminée par analyse documentée) figurent aussi parmi les méthodes comptables du groupe [V art. 282-2 ; F14 § 10].

---

### Réponses tolérées
- **1.1** : grand groupe établi sur deux des trois critères seulement, si le candidat cite les deux exercices consécutifs ; exemption de VELDRANE Literie présentée seule, sans relever qu'elle ne contrôle aucune entreprise : – 0,25.
- **1.2** : neutralité présentée comme « composante de l'image fidèle » sans définition développée, si l'absence de parti pris est rattachée à la réponse au fondateur.
- **1.3** : MOUSSES DE L'AVANCE omise du tableau, si son exclusion est justifiée dans le texte : – 0,25 ; pourcentage d'intérêt de MOUSSES DE L'AVANCE non indiqué (entité hors périmètre).
- **1.4** : comparaison avec l'intégration globale faite avant élimination des ventes internes (chiffre d'affaires + 38 000 000), si le candidat signale que les ventes de VELDRANE Literie seraient alors éliminées.
- **1.5 b** : écriture de bilan sans le stock d'ouverture distingué de la dotation (crédit unique « réserves et résultat »), si le compte de résultat est corrigé : – 0,5.
- **1.6** : autre découpage en étapes, si l'ordre retraitements, cumul, éliminations, partage, mise en équivalence est justifié ; mise en équivalence présentée avant le partage.
- **1.7 d** : écart d'évaluation et élimination des titres regroupés dans une seule écriture, si elle est équilibrée ; amortissement de l'écart d'acquisition inscrit dans l'écriture C9.
- **1.8 a** : dividende de NOCTAMBRE éliminé par imputation sur les titres mis en équivalence plutôt qu'en réserves, si la valeur d'équivalence de clôture reste de 1 575 000 € et le résultat consolidé n'est pas modifié.
- **1.9 a** : tableau présenté avec les réserves à l'acquisition et postérieures regroupées (8 000 000), si l'écart d'acquisition et son amortissement de 2025 sont correctement imputés.
- **1.10 a** : impôts différés passifs présentés sur une ligne distincte, si le total est juste.
- **Tous** : montants cohérents avec les erreurs antérieures du candidat (erreur non sanctionnée deux fois).

### Erreurs fréquentes
- **Obligation de consolider** : le fonds présenté comme société consolidante parce qu'il détient 64 % ; VELDRANE Literie tenue de consolider MOUSSES DE L'AVANCE ; seuils examinés sur un seul exercice ; IFRS jugées obligatoires à cause de la dette bancaire (`JUR-F06`).
- **Prudence** : prudence présentée comme une permission de minorer les résultats ou de constituer des réserves de précaution ; dérogatoires présentés comme un passif ; IDP oublié (`JUR-F01`).
- **Périmètre** : NOCTAMBRE intégrée globalement « parce que le groupe lui vend 60 % de ses matelas » ; MOUSSES DE L'AVANCE mise en équivalence ; titres de MOUSSES DE L'AVANCE supprimés du bilan consolidé (`JUR-F07`).
- **Dérogatoires** : prorata de 2025 oublié (32 000 au lieu de 24 000) ; stock d'ouverture porté en résultat ; impôt différé actif au lieu de passif ; titres MOUSSES DE L'AVANCE ramenés à 2 840 000 € dans le bilan consolidé (`JUR-F05`, `JUR-G06`).
- **CASTALÈNE** : coût d'acquisition retenu pour 9 000 000 (frais omis) ou 9 240 000 (frais bruts) (`JUR-G02`) ; correction des frais portée au résultat de 2026 ; impôt différé omis sur l'écart d'évaluation ; amortissement de 2025 de l'écart d'acquisition oublié ou porté en résultat ; amortissement de l'écart d'acquisition partagé avec les minoritaires ; impôt différé calculé sur l'écart d'acquisition.
- **Opérations internes** : dividende de CASTALÈNE éliminé pour 800 000 € ; dividende de MOUSSES DE L'AVANCE éliminé ; frais de gestion éliminés « en partie » pour la part des minoritaires ; incidence sur le résultat consolidé attribuée aux éliminations de frais de gestion.
- **Partage et mise en équivalence** : partage sur des capitaux propres non retraités (`JUR-G01`, `JUR-G04`) ; minoritaires calculés sans l'écart d'évaluation ; dividende de NOCTAMBRE compté deux fois (dans le résultat de la holding et dans la valeur d'équivalence) ; écart d'acquisition calculé sur NOCTAMBRE alors que les titres ont été souscrits au nominal (`JUR-G03`) ; capital des filiales ajouté au capital consolidé.
- **Bilan** : intérêts minoritaires inclus dans les capitaux propres part du groupe ; titres de participation laissés pour leur montant cumulé ; compte courant ou créance de frais de gestion non éliminés ; écart d'acquisition de VELDRANE Literie oublié ; montants sans justification (`JUR-F02`), écritures non équilibrées (`JUR-F04`).

### Références
- Code de commerce : L. 233-16 I et II, L. 233-17, L. 230-2, D. 230-2, L. 233-24 [V, F03 § 1.1, § 1.2, § 19.1 et § 20.1] ; règlement (CE) n° 1606/2002, art. 4 [V, F03 § 1.2].
- Cadre conceptuel de l'IASB (2018) : image fidèle, neutralité, prudence [V Project Summary, p. 6, F03 § 17 et § 20.2] ; IAS 8 § 10 b) [V, F03 § 12].
- Code général des impôts : art. 209, VII [V, F04 § 15] ; PCG : art. 214-8, 821-1 (provisions réglementées) [V, F04 § 8].
- Règlement ANC n° 2020-01 : art. 211-3 à 211-6, 221-1, 221-2, 221-4, 222-1 [V, F03 § 2 et § 3] ; art. 231-2, 231-3, 231-9, 231-11, 232-1, 262-2, 262-3, 272-10, 272-13 [V, F05] ; art. 251-1, 251-2, 262-4, 272-1, 272-8 [V, F04] ; art. 281-1, 281-2, 282-2, 282-22, 282-24 [V, F14 § 1.2, § 10 et § 13].

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, modalités, effet de la participation, référentiel | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable | 2 |
| 2.2 Régime de faveur : conditions, conséquences, dérogatoires, sort fiscal du mali | `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 2 |
| 2.3 a) Parité exacte, actions à rémunérer, actions à créer | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1 |
| 2.3 b) Rémunération initiale : équité, plafond légal après renonciation, condition fiscale, conseil, variante | `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 3 |
| 2.3 c) Actions créées, augmentation de capital, attribution par associé, répartition du capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 1 |
| 2.4 Mode d'évaluation des apports | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 1,5 |
| 2.5 Actif net réel apporté, provision pour impôts, composition, quotes-parts | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée | 1,5 |
| 2.6 Mali, absence de mali technique, nature, traitement, prix de 2021 | `1.2.e` Calculer et analyser le boni ou mali de fusion | 3 |
| 2.7 a) COQUES DE LA LÈDE : augmentation de capital et réalisation des apports | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 2 |
| 2.7 b) COQUES DE LA LÈDE : complément de dépréciation et annulation des titres | `1.3.b` Adapter les écritures aux détentions préalables entre sociétés participantes | 2,5 |
| 2.7 c) BASSINS DE L'ADOUR : transmission, droits des associés, remise des actions et de la soulte | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 1,5 |
| 2.7 d) COQUES DE LA LÈDE : soulte, amortissements dérogatoires, frais de fusion | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 2 |
| 2.8 Note à M. FAUBERNET | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 2 |
| **Total** | | **25** |

---

### 2.1 Qualification, modalités et référentiel (2 pts)

- *Qualification (0,5 pt).* L'opération est une **fusion par absorption** : BASSINS DE L'ADOUR transmet l'**ensemble de son patrimoine**, actif et passif, à COQUES DE LA LÈDE, société qui existe déjà ; elle est **dissoute sans liquidation** et la transmission est **universelle**, dans l'état où se trouve le patrimoine à la réalisation [V C. com. L. 236-1 et L. 236-3 I, PCG art. 710-2, F01 § 1]. Ce n'est pas un rachat d'actions : les biens et les dettes de BASSINS DE L'ADOUR passent directement dans le patrimoine de COQUES DE LA LÈDE, et ses associés deviennent associés de COQUES DE LA LÈDE.
- *Modalités (0,5 pt).* COQUES DE LA LÈDE reçoit l'atelier, le terrain, les véhicules, les stocks, les créances, la trésorerie, la clientèle et les dettes de BASSINS DE L'ADOUR. En contrepartie, elle **augmente son capital** et remet des actions nouvelles, complétées d'une **soulte en espèces** limitée à 10 % de leur valeur nominale, aux associés de BASSINS DE L'ADOUR [V C. com. L. 236-1, F01 § 4] : la rémunération est en titres et en numéraire. La fusion prend effet le 30 avril 2027, date des assemblées qui l'approuvent, sans effet antérieur [V C. com. L. 236-4, 2°, F01 § 1].
- *Effet de la participation de 35 % (0,75 pt).* COQUES DE LA LÈDE ne peut pas recevoir ses propres actions en échange des 5 600 actions BASSINS DE L'ADOUR qu'elle détient : ces actions **ne sont pas échangées** [V C. com. L. 236-3 II 1°, F01 § 5.1]. Seules les **10 400 actions** de la famille CASTÉRAGUE (65 %) sont rémunérées. La part de l'apport qui correspond aux 35 % n'est pas rémunérée : elle remplace dans le bilan de COQUES DE LA LÈDE les titres BASSINS DE L'ADOUR, qui sont **annulés**, et la comparaison des deux montants fait apparaître un boni ou un mali (2.6). C'est une fusion avec détention préalable, ou fusion-renonciation. Inversement, BASSINS DE L'ADOUR ne détient aucune action COQUES DE LA LÈDE : aucune réduction de capital n'est à prévoir.
- *Référentiel (0,25 pt).* L'opération est enregistrée dans les **comptes individuels** des deux sociétés selon le **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe le mode d'évaluation des apports et leur inscription chez l'absorbante pour les valeurs du traité [V PCG art. 710-1, 720-1, F01 § 1].

---

### 2.2 Régime fiscal de faveur (2 pts)

- *Conditions (0,5 pt).*
  - Les deux sociétés sont des personnes morales **soumises à l'impôt sur les sociétés** [V CGI art. 210 C-1, F02 § 1].
  - L'opération doit être une **fusion au sens fiscal** : transmission de l'ensemble du patrimoine par suite et au moment de la dissolution sans liquidation, contre des titres de l'absorbante et, éventuellement, une **soulte ne dépassant pas 10 % de la valeur nominale de ces titres** [V CGI art. 210-0 A, I, 1° a, F02 § 1]. L'absence d'échange des actions détenues par COQUES DE LA LÈDE ne fait pas sortir l'opération de cette définition [V même art., I, 3°, F02 § 1]. La soulte initiale ne respecte pas cette limite (2.3 b) : seule une rémunération adaptée (la variante, ou la parité exacte sans soulte) permet le régime de faveur.
  - **Motifs économiques valables** [V même art., III, F02 § 1] : intégration de l'installation et de l'entretien, réseau de pose propre dans un marché en recul, transmission de l'entreprise du fondateur.
  - COQUES DE LA LÈDE prend **dans le traité** les engagements de l'art. 210 A-3 ; le régime s'applique sans agrément, BASSINS DE L'ADOUR n'ayant aucun déficit à transférer [V CGI art. 210 A-3, BOI-IS-FUS-10-10-10 § 10 et 20, F02 § 1, § 3 et § 4].
- *Conséquences pour BASSINS DE L'ADOUR (0,5 pt).* Les **plus-values** dégagées sur les éléments apportés (fonds commercial 770 000 €, atelier 240 000 €, véhicules 80 000 €, stocks 40 000 €) et le résultat de fusion qu'elle constate (1 017 500 €, 2.7 c) **ne sont pas soumis à l'IS** [V CGI art. 210 A-1, F02 § 2]. Son **résultat de la période du 1er janvier au 30 avril 2027** est en revanche imposé, quel que soit le régime [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2] : l'impôt figure dans ses dettes fiscales et sera payé par COQUES DE LA LÈDE.
- *Engagements de COQUES DE LA LÈDE (0,5 pt)* [V CGI art. 210 A-3, F02 § 2 et § 4] :
  - **réintégrer** les plus-values sur les **biens amortissables** dans ses bénéfices imposables, par parts égales sur **15 ans** pour l'atelier (240 000 / 15 = 16 000 € par an) et sur **5 ans** pour les véhicules (80 000 / 5 = 16 000 € par an) ; la plus-value sur la construction (75 % de la plus-value nette sur biens amortissables) ne dépasse pas 90 % : la durée moyenne pondérée ne joue pas. Les amortissements sont calculés sur les valeurs d'apport ;
  - calculer la plus-value de cession future du **fonds commercial** d'après sa valeur fiscale chez BASSINS DE L'ADOUR, nulle puisqu'il a été créé par elle ;
  - les **stocks** étant inscrits à leur valeur réelle et non à leur valeur fiscale, comprendre le profit correspondant (40 000 €) dans son résultat imposable de 2027.
- *Dérogatoires et mali (0,5 pt).*
  - Les **amortissements dérogatoires** sont des provisions réglementées, en principe imposées lors de la fusion [V BOI-IS-FUS-10-20-30 § 320, F02 § 2]. L'administration admet, pour une fusion aux valeurs comptables, que leur reprise ne soit pas imposée chez l'absorbée lorsqu'ils sont **reconstitués** chez l'absorbante et réintégrés dans les mêmes conditions [V BOI-IS-FUS-30-20 § 10, F02 § 2]. Pour cette fusion à la valeur réelle, le traité retient la même solution, que l'annexe 2.3 pose en hypothèse. COQUES DE LA LÈDE reconstitue les 90 000 € (2.7 d) et les reprendra au rythme de l'amortissement des véhicules.
  - Le **mali** (78 400 €, 2.6) est un vrai mali : il n'y a pas de mali technique, dont l'inscription à l'actif ne pourrait donner lieu à aucune déduction [V CGI art. 210 A-1, al. 3, F02 § 2 ter]. Le vrai mali est en principe une **moins-value à long terme** sur titres de participation détenus depuis plus de deux ans (juin 2021) [V BOI-IS-FUS-10-50-20 § 50, F02 § 2 ter] ; elle ne peut s'imputer que sur des plus-values à long terme de la même catégorie, absentes en 2027 (annexe 2.2) : la dotation de 78 400 € est **réintégrée extra-comptablement** [V CGI art. 219, I-a quinquies, F02 § 2 ter]. Sur le plan fiscal, la dépréciation de 2026 ayant été réintégrée, les titres ont une valeur fiscale de 1 120 000 € : la moins-value d'annulation est de 1 120 000 – 929 600 = 190 400 €, elle aussi non imputable. Le régime de faveur ne change rien à ce traitement.

---

### 2.3 Parité, soulte et répartition du capital (5 pts)

**a) Parité exacte (1 pt)**
- *Parité (0,5 pt).* Rapport des valeurs d'échange fournies : 166 / 80 = **83 / 40**, soit 83 actions COQUES DE LA LÈDE pour 40 actions BASSINS DE L'ADOUR (2,075). Les valeurs d'échange servent à la parité quel que soit le mode d'évaluation des apports [V PCG art. 740-1, F01 § 1].
- *Actions à rémunérer et à créer (0,5 pt).* Les 5 600 actions de COQUES DE LA LÈDE ne sont pas rémunérées (2.1) : **10 400 actions** sont à rémunérer. La parité exacte conduirait à créer 10 400 × 83 / 40 = **21 580 actions**, nombre entier pour chaque associé (M. CASTÉRAGUE : 13 280 ; Mme CASTÉRAGUE : 8 300), sans aucune soulte.

**b) Rémunération initiale, conseil et variante (3 pts)**
- *Équité de la rémunération initiale (0,5 pt).* Par action BASSINS DE L'ADOUR : 2 × 80 + 6 = 166 €. Au total : 10 400 × 2 = **20 800 actions** et 10 400 × 6 = **62 400 €** de soulte ; 20 800 × 80 + 62 400 = 1 726 400 € = 10 400 × 166 € : l'échange est **équitable** [F01 § 4]. La soulte remplace 780 actions (62 400 / 80) que la parité exacte aurait créées.
- *Limite légale (1 pt).* La soulte ne peut dépasser 10 % de la valeur nominale des actions **attribuées** [V C. com. L. 236-1, al. 3, F01 § 4]. Or COQUES DE LA LÈDE n'attribue d'actions que pour les 10 400 actions de la famille CASTÉRAGUE : 10 % × 20 800 × 25 = **52 000 €**. La soulte de 62 400 € **dépasse le plafond de 10 400 €** (par action : 6 € pour un plafond de 10 % × 2 × 25 = 5 €). Le calcul du projet (80 000 €) est faux : il compte les 11 200 actions qui correspondraient aux 5 600 actions de COQUES DE LA LÈDE, actions qui ne seront jamais émises puisque COQUES DE LA LÈDE renonce à se les attribuer [V C. com. L. 236-3 II 1°, F01 § 5.1]. La renonciation réduit d'autant le plafond. La rémunération initiale est **illégale**.
- *Condition fiscale (0,25 pt).* La définition fiscale de la fusion reprend la même limite [V CGI art. 210-0 A, I, 1° a et 3°, F02 § 1] : avec la soulte initiale, l'opération perdrait le régime de faveur ; les plus-values de BASSINS DE L'ADOUR (1 130 000 €) et ses amortissements dérogatoires seraient imposés immédiatement.
- *Conseil aux dirigeants (0,75 pt).*
  - Ramener la soulte à 52 000 € **sans créer d'actions supplémentaires** n'est pas une solution : la famille CASTÉRAGUE perdrait 10 400 € de valeur au profit des associés de COQUES DE LA LÈDE, ce qui rend l'échange inéquitable et constitue un transfert de valeur qui exclut le régime de faveur [V BOI-IS-FUS-30-20 § 20 et 30, F02 § 1].
  - Il faut donc **réduire la soulte et remettre des actions en plus**, à valeur égale : c'est l'objet de la variante. La parité exacte, sans soulte (21 580 actions), est aussi conforme, mais elle ne donne pas de numéraire à M. CASTÉRAGUE.
  - Autre voie : relever d'abord la **valeur nominale** des actions COQUES DE LA LÈDE par incorporation de réserves, ce qui relève le plafond sans changer la valeur des actions ni la parité ; avec un nominal de 30 € (600 000 € de réserves incorporées et rendues indisponibles), le plafond serait de 10 % × 20 800 × 30 = 62 400 €, atteint sans marge [V C. com. L. 225-130 et L. 227-1, F01 § 4].
  - L'argument de la dilution est faible : avec la soulte initiale, FAUBERNET Participations détiendrait 68,18 % du capital, contre 67,93 % avec la variante (2.3 c).
- *Vérification de la variante (0,5 pt).* 10 400 / 20 = 520 lots ; **21 320 actions** (520 × 41) et **20 800 €** de soulte (520 × 40). Équité : 21 320 × 80 + 20 800 = 1 726 400 € = 10 400 × 166 € (par lot : 41 × 80 + 40 = 3 320 = 20 × 166). Plafond : 10 % × 21 320 × 25 = **53 300 €** ; la soulte en représente 39,02 % (par lot : 40 € pour 102,50 €). La variante respecte la loi et le régime de faveur : **elle doit être retenue**, avec 20 800 € de numéraire pour la famille CASTÉRAGUE.

**c) Rémunération retenue et répartition du capital (1 pt)**
- *Actions créées et augmentation de capital (0,25 pt).* 21 320 actions de 25 € : augmentation de capital de **533 000 €** ; le capital passe à 3 533 000 € (141 320 actions).
- *Attribution par associé (0,25 pt).* M. Régis CASTÉRAGUE : 320 lots, **13 120 actions et 12 800 €** (13 120 × 80 + 12 800 = 1 062 400 € = 6 400 × 166) ; Mme Laure CASTÉRAGUE : 200 lots, **8 200 actions et 8 000 €** (664 000 € = 4 000 × 166).
- *Répartition du capital après la fusion (0,5 pt).*

| Associé | Actions | % du capital et des droits de vote |
|---|---:|---:|
| SAS FAUBERNET Participations | 96 000 | 67,93 % |
| Autres associés de COQUES DE LA LÈDE | 24 000 | 16,98 % |
| M. Régis CASTÉRAGUE | 13 120 | 9,28 % |
| Mme Laure CASTÉRAGUE | 8 200 | 5,80 % |
| **Total** | **141 320** | **100 %** |

  (Total des pourcentages arrondis : 99,99 %.) FAUBERNET Participations passe de 80 % à 67,93 % : diluée, elle **garde le contrôle** de COQUES DE LA LÈDE ; la famille CASTÉRAGUE, même en votant ensemble, ne détient que 15,09 %. Cette conclusion sert à déterminer le sens de l'opération (2.4).

---

### 2.4 Mode d'évaluation des apports (1,5 pt)

- *Situation de contrôle (0,75 pt).* COQUES DE LA LÈDE ne détient que 35 % des droits de vote de BASSINS DE L'ADOUR : elle n'en a pas la majorité, elle ne désigne aucun de ses dirigeants et ne dispose d'aucun droit particulier, alors que la famille CASTÉRAGUE détient 65 % des voix et désigne seule les dirigeants. COQUES DE LA LÈDE ne **contrôle** donc pas BASSINS DE L'ADOUR de manière exclusive [V PCG art. 741-2, F01 § 2.1]. BASSINS DE L'ADOUR ne détient aucune action COQUES DE LA LÈDE, et FAUBERNET Participations, qui contrôle COQUES DE LA LÈDE, ne détient aucune action BASSINS DE L'ADOUR : les deux sociétés ne sont pas sous le contrôle d'une même entité. L'opération est réalisée **sous contrôle distinct** [V art. 741-1, F01 § 2.1].
- *Sens de l'opération (0,5 pt).* L'actionnaire principal de COQUES DE LA LÈDE avant l'opération, la personne morale FAUBERNET Participations, conserve le contrôle de l'absorbante (67,93 % des droits de vote après la fusion, 2.3 c), alors que la famille CASTÉRAGUE perd le contrôle de BASSINS DE L'ADOUR et ne prend pas celui de COQUES DE LA LÈDE (15,09 %) : la fusion est réalisée **à l'endroit** [V art. 742-1, F01 § 2.2]. BASSINS DE L'ADOUR est la cible, COQUES DE LA LÈDE l'initiatrice.
- *Mode d'évaluation (0,25 pt).* Opération **à l'endroit sous contrôle distinct** : les apports sont évalués à la **valeur réelle** [V art. 743-1, F01 § 2.3] ; COQUES DE LA LÈDE prend le contrôle de BASSINS DE L'ADOUR, l'opération est traitée comme une acquisition.

---

### 2.5 Actif net apporté à la valeur réelle et quotes-parts (1,5 pt)

- *Plus-values et provision pour impôts (0,5 pt).* Fonds commercial, absent du bilan : **770 000 €** ; atelier : 760 000 – 520 000 = **240 000 €** ; véhicules : 500 000 – 420 000 = **80 000 €** ; stocks : 600 000 – 560 000 = **40 000 €**. Base d'impôt différé, éléments dont l'imposition est reportée chez COQUES DE LA LÈDE (annexe 2.5) : 240 000 + 80 000 + 40 000 + 90 000 (amortissements dérogatoires reconstitués) = 450 000 € ; **provision pour impôts : 450 000 × 25 % = 112 500 €**, élément identifié non comptabilisé chez BASSINS DE L'ADOUR [V PCG art. 744-1, F01 § 3.1 et § 3.3, F02 § 6]. Aucun impôt différé sur le fonds commercial (annexe 2.5).
- *Actif net réel et composition (0,5 pt).* Actif net réel = 1 638 500 + 770 000 + 240 000 + 80 000 + 40 000 – 112 500 = **2 656 000 €**, égal à la valeur d'échange de BASSINS DE L'ADOUR (166 × 16 000) : le fonds commercial de 770 000 € est bien l'écart entre la valeur globale et les éléments identifiés (2 656 000 – 1 886 000) [V art. 744-1, F01 § 3.1].

| Élément (en €) | Valeur d'apport |
|---|---:|
| Fonds commercial | 770 000 |
| Terrain | 110 000 |
| Atelier et entrepôt de Dax | 760 000 |
| Véhicules | 500 000 |
| Stocks de marchandises | 600 000 |
| Clients | 938 500 |
| Disponibilités | 330 000 |
| **Total des actifs** | **4 008 500** |
| Provision pour impôts | – 112 500 |
| Emprunts | – 520 000 |
| Fournisseurs | – 430 000 |
| Dettes sociales et fiscales | – 290 000 |
| **Actif net apporté** | **2 656 000** |

  Les amortissements dérogatoires (90 000 €) font partie des capitaux propres de BASSINS DE L'ADOUR (1 638 500 €) : ils sont compris dans l'actif net apporté et seront reconstitués par prélèvement sur la prime (2.7 d) [V PCG art. 214-8 et 313-1, F01 § 8].
- *Quotes-parts (0,5 pt).* Quote-part **rémunérée** (65 %) : 2 656 000 × 10 400 / 16 000 = **1 726 400 €**, égale à la valeur des actions de la famille CASTÉRAGUE ; quote-part **non rémunérée** (35 %) : 2 656 000 × 5 600 / 16 000 = **929 600 €** [F01 § 5.1].

---

### 2.6 Mali de fusion (3 pts)

- *Calcul (0,75 pt).* Quote-part non rémunérée de l'actif net reçu – valeur comptable **nette** des titres annulés = 929 600 – 1 008 000 = **– 78 400 €** : écart négatif, c'est un **mali de 78 400 €** [V PCG art. 745-1 et 745-3, F01 § 5.1 et § 5.3]. La valeur comptable retenue est la valeur nette (1 120 000 – 112 000), et non le coût d'acquisition.
- *Pourquoi il n'y a pas de mali technique (1 pt).* Le mali technique représente, à hauteur de la participation, les **plus-values latentes** de l'absorbée que l'apport ne fait pas apparaître : c'est pourquoi le plan comptable le rattache aux opérations évaluées à la valeur comptable, où l'actif net reçu est un actif net comptable (annexe 2.7) [V art. 745-4, F01 § 5.3]. Ici, les apports sont évalués à la **valeur réelle** (2.4) : l'actif net reçu comprend déjà toutes les plus-values, sur les éléments identifiés (360 000 €) comme sur le fonds commercial (770 000 €), nettes de l'impôt différé (112 500 €). Il ne reste **aucune plus-value latente** à hauteur des 35 % : le mali technique est nul. Inscrire les 78 400 € à l'actif compterait une seconde fois des plus-values déjà inscrites et surévaluerait le bilan de COQUES DE LA LÈDE.
- *Nature et traitement (0,75 pt).* Le mali est donc en totalité un **vrai mali** : le **complément de dépréciation** de la participation nécessaire au moment de la fusion, comptabilisé dans le **résultat financier** de COQUES DE LA LÈDE de 2027 (dotation 6866) et non inscrit à l'actif [V art. 745-4, F01 § 5.3 et § 9]. Après ce complément, les titres valent 1 008 000 – 78 400 = 929 600 €, soit 166 € par action, la valeur d'échange que COQUES DE LA LÈDE a elle-même acceptée dans le traité : elle ne peut pas garder dans ses comptes l'estimation de 180 € retenue au 31 décembre 2026. Le recueil ANC rappelle, sous l'art. 745-4, que le mali technique se détermine à partir des mêmes hypothèses de plus-values latentes que celles qui ont présidé à la dépréciation des titres [V recueil ANC 2026, p. 399] : ici, ces hypothèses sont celles du traité, qui ne laissent aucune plus-value latente. La fusion ne crée pas cette perte : elle la constate.
- *Ce qu'il révèle sur le prix de 2021 (0,5 pt).* COQUES DE LA LÈDE a payé 200 € par action en 2021 ; la participation n'en vaut plus que 166. La perte totale atteint 5 600 × 34 = **190 400 €** (17 % du prix), dont 112 000 € constatés fin 2026 et 78 400 € révélés par la fusion. Le prix de 2021 rémunérait une croissance attendue du marché des piscines, alors au plus haut, qui ne s'est pas réalisée : COQUES DE LA LÈDE a surpayé sa participation au regard de la valeur que BASSINS DE L'ADOUR a aujourd'hui, fonds commercial compris.

---

### 2.7 Écritures au 30 avril 2027 (8 pts)

Toutes les écritures ci-dessous sont équilibrées.

**a) COQUES DE LA LÈDE : augmentation de capital et réalisation des apports (2 pts)**

**A1 — Augmentation de capital (0,75 pt).** Compte d'apport débité de la seule quote-part rémunérée (0,25) ; capital (0,25) ; prime de fusion avant soulte (0,25) : 1 726 400 – 533 000 = 1 193 400 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (65 % × 2 656 000) | 1 726 400 | |
| 101 Capital (21 320 × 25) | | 533 000 |
| 1042 Primes de fusion | | 1 193 400 |

**A2 — Réalisation des apports à la valeur réelle (1,25 pt).** Actifs inscrits pour leur **valeur réelle**, qui devient leur valeur brute chez COQUES DE LA LÈDE, sans reprise des amortissements de BASSINS DE L'ADOUR, et fonds commercial inscrit bien qu'absent du bilan de l'absorbée (0,5) ; provision pour impôts (0,25) ; dettes (0,25) ; compte d'apport crédité de la **totalité** de l'actif net apporté (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 207 Fonds commercial | 770 000 | |
| 211 Terrains | 110 000 | |
| 2131 Bâtiments (atelier et entrepôt de Dax) | 760 000 | |
| 2182 Matériel de transport (véhicules) | 500 000 | |
| 37 Stocks de marchandises | 600 000 | |
| 411 Clients | 938 500 | |
| 512 Banques | 330 000 | |
| 1523 Provisions pour impôts | | 112 500 |
| 164 Emprunts auprès des établissements de crédit | | 520 000 |
| 401 Fournisseurs | | 430 000 |
| 43 Sécurité sociale et autres organismes sociaux | | 120 000 |
| 44 État et autres collectivités publiques | | 170 000 |
| 4561 Associés – Comptes d'apport en société | | 2 656 000 |
| **Total** | **4 008 500** | **4 008 500** |

**b) COQUES DE LA LÈDE : mali et annulation des titres (2,5 pts)**

**A3 — Complément de dépréciation des titres (1 pt).** Le vrai mali est une dépréciation de la participation, constatée en résultat financier avant l'annulation des titres [V art. 745-4, F01 § 5.3 et § 9 ; compte 6866, liste des comptes du PCG 2026] (compte de charge 0,5 ; compte de dépréciation et montant 0,5).

| Compte | Débit | Crédit |
|---|---:|---:|
| 6866 Dotations pour dépréciation des éléments financiers | 78 400 | |
| 2961 Dépréciations des titres de participation (BASSINS DE L'ADOUR) | | 78 400 |

**A4 — Annulation des 5 600 actions BASSINS DE L'ADOUR (1,5 pt).** Quote-part non rémunérée au débit du compte d'apport (0,5) ; dépréciations cumulées soldées, 112 000 + 78 400 = 190 400 € (0,5) ; titres annulés pour leur valeur brute, sans mali inscrit à l'actif (0,5).

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (35 % × 2 656 000) | 929 600 | |
| 2961 Dépréciations des titres de participation (112 000 + 78 400) | 190 400 | |
| 261 Titres de participation (BASSINS DE L'ADOUR) | | 1 120 000 |

Le compte 4561 est soldé : 1 726 400 + 929 600 = 2 656 000.

**c) BASSINS DE L'ADOUR (1,5 pt)**

**A5 — Transmission du patrimoine (0,75 pt).** Sortie des actifs pour leur valeur brute, de leurs amortissements et des dettes ; créance sur COQUES DE LA LÈDE pour la valeur d'apport ; **résultat de fusion** de 2 656 000 – 1 638 500 = 1 017 500 €, présenté en résultat exceptionnel (annexe 2.6), non imposé (2.2).

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – COQUES DE LA LÈDE, compte d'apport | 2 656 000 | |
| 2813 Amortissements des constructions | 300 000 | |
| 2818 Amortissements des autres immobilisations corporelles (véhicules) | 540 000 | |
| 164 Emprunts auprès des établissements de crédit | 520 000 | |
| 401 Fournisseurs | 430 000 | |
| 43 Sécurité sociale et autres organismes sociaux | 120 000 | |
| 44 État et autres collectivités publiques | 170 000 | |
| 211 Terrains | | 110 000 |
| 2131 Bâtiments | | 820 000 |
| 2182 Matériel de transport | | 960 000 |
| 37 Stocks de marchandises | | 560 000 |
| 411 Clients | | 938 500 |
| 512 Banques | | 330 000 |
| 778 Autres produits exceptionnels (résultat de fusion) | | 1 017 500 |
| **Total** | **4 736 000** | **4 736 000** |

**A6 — Droits des associés (0,5 pt).** Les capitaux propres, amortissements dérogatoires et résultat de fusion compris (1 638 500 + 1 017 500 = 2 656 000 €), reviennent aux associés à proportion de leurs actions : 35 %, 40 % et 25 %.

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 480 000 | |
| 1061 Réserve légale | 48 000 | |
| 1068 Autres réserves | 882 000 | |
| 120 Résultat de l'exercice (138 500 + 1 017 500) | 1 156 000 | |
| 145 Amortissements dérogatoires | 90 000 | |
| 456 Associés – Opérations sur le capital (COQUES DE LA LÈDE, 35 %) | | 929 600 |
| 456 Associés – Opérations sur le capital (Régis CASTÉRAGUE, 40 %) | | 1 062 400 |
| 456 Associés – Opérations sur le capital (Laure CASTÉRAGUE, 25 %) | | 664 000 |

**A7 — Remise des actions et de la soulte, renonciation de COQUES DE LA LÈDE (0,25 pt).** COQUES DE LA LÈDE remet directement les actions nouvelles et la soulte à la famille CASTÉRAGUE (annexe 2.6) ; les droits de COQUES DE LA LÈDE (929 600 €) s'éteignent en contrepartie de l'annulation de ses titres.

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – Opérations sur le capital (Régis CASTÉRAGUE : 13 120 actions et 12 800 €) | 1 062 400 | |
| 456 Associés – Opérations sur le capital (Laure CASTÉRAGUE : 8 200 actions et 8 000 €) | 664 000 | |
| 456 Associés – Opérations sur le capital (COQUES DE LA LÈDE) | 929 600 | |
| 467 Divers comptes débiteurs – COQUES DE LA LÈDE, compte d'apport | | 2 656 000 |

Tous les comptes de BASSINS DE L'ADOUR sont soldés. Les comptes 456, 467 et 778 de l'absorbée relèvent d'une convention de rédaction : le PCG ne donne pas d'écriture pour l'absorbée [F01 § 9].

**d) COQUES DE LA LÈDE : écritures complémentaires (2 pts)**

**A8 — Soulte versée (0,5 pt).** La soulte rémunère une partie des actions de la famille CASTÉRAGUE : elle diminue la prime de fusion [F01 § 4].

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion | 20 800 | |
| 512 Banques (soulte : 520 lots × 40 €) | | 20 800 |

**A9 — Reconstitution des amortissements dérogatoires (0,75 pt).** Engagement pris dans le traité au titre du régime de faveur (2.2) : ces provisions réglementées, comprises dans l'actif net apporté, sont reconstituées **en totalité** par prélèvement sur la prime de fusion, et non à hauteur des seuls 65 % rémunérés [V corrigé du sujet zéro, Q 2.6 ; BOI-IS-FUS-30-20 § 10, F01 § 8].

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion | 90 000 | |
| 145 Amortissements dérogatoires (véhicules reçus de BASSINS DE L'ADOUR) | | 90 000 |

**A10 — Frais de fusion (0,75 pt).** Les frais de fusion peuvent être imputés sur la prime de fusion [V PCG art. 212-9, F01 § 7], pour leur montant **net d'impôt**, comme le prévoit l'annexe 2.6 [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 32 000 × 75 % = **24 000 €** sur la prime, économie d'impôt de 8 000 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion | 24 000 | |
| 444 État – Impôts sur les bénéfices | 8 000 | |
| 512 Banques | | 32 000 |

Prime de fusion après l'opération : 1 193 400 – 20 800 – 90 000 – 24 000 = **1 058 600 €**.

---

### 2.8 Note à M. FAUBERNET, président de COQUES DE LA LÈDE (2 pts)

*Objet : effets de l'absorption de BASSINS DE L'ADOUR sur les comptes et le capital de COQUES DE LA LÈDE.*

- *Capitaux propres juste après la fusion (0,75 pt).*

| Poste (en €) | Avant | Fusion, soulte et frais | Après |
|---|---:|---:|---:|
| Capital | 3 000 000 | + 533 000 | 3 533 000 |
| Primes de fusion | – | + 1 193 400 – 20 800 – 90 000 – 24 000 | 1 058 600 |
| Réserve légale | 300 000 | | 300 000 |
| Autres réserves | 4 400 000 | | 4 400 000 |
| Report à nouveau | 158 000 | | 158 000 |
| Résultat de 2027 (complément de dépréciation des titres) | – | – 78 400 | – 78 400 |
| Provisions réglementées (amortissements dérogatoires) | – | + 90 000 | 90 000 |
| **Total** | **7 858 000** | **+ 1 603 200** | **9 461 200** |

  Les capitaux propres augmentent de 1 603 200 € (+ 20,40 %) : apport rémunéré de la famille CASTÉRAGUE (1 726 400 €), moins la soulte (20 800 €), les frais nets d'impôt (24 000 €) et le mali (78 400 €). Les 90 000 € de dérogatoires passent de la prime aux provisions réglementées, sans changer le total.
- *Répartition du capital (0,25 pt).* 141 320 actions : FAUBERNET Participations 67,93 %, autres associés 16,98 %, famille CASTÉRAGUE 15,09 %. Votre famille garde le contrôle ; la famille CASTÉRAGUE devient minoritaire.
- *Effet du mali sur le résultat de 2027 (0,5 pt).* Le résultat financier de 2027 supporte une dotation de **78 400 €**, qui ne correspond à aucune sortie de trésorerie et ne se renouvellera pas, mais qui n'est pas déductible (2.2) : elle diminue le résultat net de 78 400 € sans économie d'impôt. Elle traduit la baisse de valeur de la participation achetée en 2021 (190 400 € au total depuis l'acquisition) ; il faudra l'isoler pour apprécier la rentabilité courante.
- *Effet de la soulte et des frais sur la trésorerie (0,5 pt).* La trésorerie passe de 1 250 000 € à **1 527 200 €** : + 330 000 € de disponibilités reçues de BASSINS DE L'ADOUR, – 20 800 € de soulte, – 32 000 € de frais (l'économie d'impôt de 8 000 € viendra en diminution de l'IS de 2027). La variante limite la sortie de trésorerie à 20 800 €, contre 62 400 € pour la soulte initiale, qui était de toute façon illégale. COQUES DE LA LÈDE reprend aussi les dettes de BASSINS DE L'ADOUR, dont 520 000 € d'emprunts (2 620 000 € au total, soit 0,28 fois les capitaux propres, contre 0,27), et une provision pour impôts de 112 500 €, qui correspond à l'impôt qu'elle paiera en réintégrant les plus-values, le profit sur stocks et les dérogatoires.

---

### Réponses tolérées
- **2.1** : effet de la participation présenté en 2.3 a seulement, s'il y est justifié.
- **2.2** : vrai mali présenté comme une dépréciation de titres de participation non déductible, sans référence au régime des moins-values à long terme, si l'hypothèse de l'annexe 2.2 est appliquée ; stocks traités dans la provision pour impôts sans mention de l'imposition du profit en 2027.
- **2.3 a** : parité exprimée en nombre décimal (2,075 actions COQUES DE LA LÈDE par action BASSINS DE L'ADOUR).
- **2.3 b** : plafond vérifié par action (6 € pour 5 €) ou par lot (40 € pour 102,50 €) plutôt qu'au total ; toute autre adaptation conforme et équitable proposée par le candidat (parité exacte sans soulte, autre combinaison d'actions et de soulte, relèvement du nominal) si la variante est ensuite vérifiée et retenue pour la suite. Un candidat qui retient à tort la rémunération initiale est noté sur la suite selon la logique de son calcul (20 800 actions, capital 520 000 €, prime 1 144 000 € après soulte) [JUR-F08].
- **2.4** : sens de l'opération apprécié par la position de la famille FAUBERNET, si la conclusion repose sur FAUBERNET Participations comme actionnaire principal.
- **2.5** : impôt différé calculé élément par élément ou sur le total.
- **2.6** : mali calculé directement par action ((180 – 166) × 5 600).
- **2.7 a** : A1 et A2 réunies ; dettes fiscales et sociales regroupées sur un compte de la classe 4 ; soulte comprise dans A1 (crédit 512 de 20 800 € et prime de 1 172 600 €) au lieu d'une écriture A8 distincte.
- **2.7 b** : A3 et A4 réunies, avec 6866 débité directement dans l'écriture d'annulation et 2961 soldé pour 112 000 € (présentation abrégée, F01 § 9).
- **2.7 c** : A6 et A7 réunies ; amortissements dérogatoires d'abord repris en produits exceptionnels (78725), le résultat de l'exercice étant alors augmenté d'autant dans A6 ; résultat de fusion inscrit dans un sous-compte du 778.
- **2.8** : capitaux propres présentés sans le résultat de 2027, si le candidat le signale et chiffre à part l'effet du mali.

### Erreurs fréquentes (rapports du jury)
- `JUR-R01` Prime de fusion mal calculée : sur la totalité de l'actif net apporté (2 656 000 – 533 000), sans déduire la soulte, les dérogatoires reconstitués ou les frais nets, ou frais imputés pour leur montant brut (32 000 €).
- `JUR-R02` Analyse du mali non conduite : mali calculé sur le coût d'acquisition (1 120 000 – 929 600 = 190 400 €) au lieu de la valeur nette ; mali inscrit à l'actif en mali technique (2081, 207) alors que les apports sont déjà à la valeur réelle ; dépréciation complémentaire oubliée, l'écart étant imputé sur la prime de fusion.
- `JUR-R03` Reconstitution des amortissements dérogatoires oubliée, ou limitée à 65 % ; dérogatoires oubliés dans la base d'impôt différé.
- `JUR-R05` Difficulté à s'adapter à la détention préalable : actions remises à COQUES DE LA LÈDE pour ses propres 5 600 actions (33 200 actions émises) ; plafond de la soulte repris du projet (80 000 €) sans voir l'effet de la renonciation, ou calculé sur le nominal des actions BASSINS DE L'ADOUR (10 % × 10 400 × 30 = 31 200 €).
- `JUR-F07` Annexes mal exploitées : fonds commercial non inscrit parce qu'absent du bilan de BASSINS DE L'ADOUR, impôt différé calculé sur le fonds commercial, variante non vérifiée.
- `JUR-F04` Absence de contrôle d'équilibre des écritures A2, A4 et A5.
- Erreurs propres à ce cas : soulte initiale ramenée au plafond sans actions supplémentaires ; amortissements de BASSINS DE L'ADOUR repris chez COQUES DE LA LÈDE alors que les apports sont à la valeur réelle ; mali déclaré déductible au taux de 25 % ; fusion datée du 1er janvier 2027.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 236-1, L. 236-3 I et II 1°, L. 236-4 | Fusion, dissolution sans liquidation, transmission universelle, soulte limitée à 10 % de la valeur nominale des actions attribuées, pas d'échange des titres détenus par l'absorbante, date d'effet | [V] | F01 § 1, § 4 et § 5.1 |
| C. com. L. 225-130, L. 227-1 | Élévation du nominal par incorporation de réserves | [V] | F01 § 4 |
| PCG art. 710-1, 710-2, 720-1, 740-1 | Champ du titre VII, définition de la fusion, inscription des apports, parité sur les valeurs d'échange | [V] p. 81-82 | F01 § 1 |
| PCG art. 741-1, 741-2, 742-1, 743-1 | Contrôle distinct, fusion à l'endroit, valeur réelle | [V] p. 82-84 | F01 § 2 |
| PCG art. 744-1 | Valeur réelle des éléments identifiés, figurant ou non au bilan (impôts différés), fonds commercial | [V] p. 85 | F01 § 3.1 et § 3.3 |
| PCG art. 745-1, 745-3, 745-4 ; recueil ANC 2026, IR sous l'art. 745-4 | Mali (sous-section des opérations à la valeur comptable), valeur nette des titres, mali technique et complément de dépréciation en résultat financier ; mêmes hypothèses que pour la dépréciation des titres | [V] p. 86-87 ; recueil p. 398-399, lu le 25/11/2026 | F01 § 5.3 |
| PCG art. 214-8, 313-1 ; corrigé du sujet zéro, Q 2.6 | Dérogatoires, provisions réglementées dans les capitaux propres ; reconstitution par la prime | [V] | F01 § 8 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais de fusion imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| Liste des comptes du PCG 2026 | 1523, 207, 2961, 6866 | [V] | F01 § 3.3 et § 9 |
| CGI art. 210-0 A (I, 1° a et 3° ; III), 210 A-1 et 210 A-3, 210 C ; BOI-IS-FUS-10-10-10 § 10 et 20 ; BOI-IS-FUS-10-20-30 § 210, 320 et 330 ; BOI-IS-FUS-30-20 § 10, 20 et 30 | Définition fiscale de la fusion et condition de soulte, absence d'échange des titres détenus, motif économique, exonération des plus-values, dernier résultat de l'absorbée, engagements et réintégration sur 15 et 5 ans, provisions réglementées, reconstitution des dérogatoires, transferts de valeur | [V] | F02 § 1, § 2 et § 4 |
| CGI art. 210 A-1, al. 3 ; art. 219, I-a quinquies ; BOI-IS-FUS-10-50-20 § 50 | Mali technique non déductible ; vrai mali, moins-value à long terme sur titres de participation | [V] | F02 § 2 ter |
| Comptes 456, 467 et 778 (absorbée) | Droits des associés, compte d'apport, résultat de fusion | Convention de rédaction (le PCG ne donne pas d'écriture pour l'absorbée) | F01 § 9 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Conditions d'exercice de l'expert-comptable et du commissaire aux comptes ; signature du rapport par une salariée non inscrite | `3.1.a` Cadres d'exercice professionnel | 1,5 |
| 3.2 Fin normale et renouvellement du mandat ; second commissaire aux comptes facultatif ; structures distinctes | `3.1.b` Nomination et cessation | 2 |
| 3.3 Actions de l'entité reçues par succession par l'associé signataire | `3.1.c` Principes déontologiques | 1,5 |
| 3.4 Norme sur l'audit réalisé par plusieurs commissaires aux comptes ; élaboration des NEP | `3.1.d` Référentiel normatif (NEP) | 1,5 |
| 3.5 Responsabilités civile, pénale et disciplinaire ; plan d'affaires | `3.1.e` Mise en cause de la responsabilité | 1,5 |
| 3.6 Audit légal, audit contractuel et autres prestations ; ce que la certification ne couvre pas | `3.2.a` Notion d'audit | 1,5 |
| 3.7 Informations auprès des tiers et demandes de confirmation ; refus du président du directoire | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.8 Risques et assertions des capitaux propres ; procédures et recalculs | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit | 5 |
| 3.9 Anomalies, écritures, caractère significatif, opinion selon les corrections, parties du rapport | `3.2.e` Portée des opinions | 2 |
| 3.10 Pourquoi la SA n'est pas tenue de publier ; étendue et limites d'une publication volontaire selon les ESRS ; EFRAG | `3.3.a` Contexte et normes de durabilité | 2 |
| 3.11 Activités propres, chaîne de valeur et contrôle opérationnel ; connectivité avec les comptes annuels | `3.3.b` Principes de construction du reporting | 3 |
| 3.12 Objectifs, axes, consultation du CSE et assurance limitée ; étapes ; procédures sur le processus et sur une donnée | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 5 |
| 3.13 Impossibilité d'émettre un avis sur le processus ; comparaison avec une réserve pour limitation | `3.4.c` Portée des avis | 2 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Conditions d'exercice et signature du rapport (1,5 pt)

**L'expert-comptable (0,5 pt)**
- Nul ne peut porter le titre d'expert-comptable ni en exercer la profession s'il n'est **inscrit au tableau de l'ordre** ; l'inscription suppose notamment le **diplôme d'expertise comptable** et des garanties de moralité [V ord. art. 3 I-II].
- Instances : les **conseils régionaux de l'ordre** tiennent le tableau, statuent sur les inscriptions et surveillent l'exercice de la profession dans leur circonscription ; le **Conseil national** est à la tête de l'ordre et défend l'honneur et l'indépendance de la profession [V ord. art. 1, 28, 31, 33, 40]. L'expert-comptable exerce des missions **contractuelles** (tenue, révision, établissement des comptes) [V ord. art. 2].

**Le commissaire aux comptes (0,5 pt)**
- La profession est exercée par des personnes physiques ou des sociétés **inscrites sur la liste établie par la H2A** [V C. com. L. 821-13 I] ; une personne physique doit notamment avoir accompli un **stage** professionnel et réussi le certificat d'aptitude ou obtenu le **diplôme d'expertise comptable** [V L. 821-14]. Une liste distincte, tenue par la H2A, recense les commissaires aux comptes habilités à certifier les informations en matière de durabilité [V L. 821-13 II].
- Instances : la **H2A**, autorité publique indépendante, inscrit les commissaires aux comptes, adopte les normes, contrôle et sanctionne [V L. 820-1 I] (elle peut déléguer l'inscription à la CNCC [V L. 820-1 II]) ; la **CNCC** représente la profession auprès des pouvoirs publics et concourt à son bon exercice ; les **CRCC**, une par ressort de cour d'appel, regroupent les commissaires aux comptes de leur ressort [V L. 821-12].
- L'inscription au tableau de l'ordre **ne vaut pas** inscription sur la liste des commissaires aux comptes [V ord. art. 3 ; L. 821-13 ; F09 § 18].

**Réponse à Mme DARTIGOLLES (0,5 pt)**
- Dans une société de commissaires aux comptes, la mission de certification est exercée, au nom de la société, par les **commissaires aux comptes personnes physiques associés, actionnaires ou dirigeants** de cette société, **qui signent le rapport** [V L. 821-25 al. 1]. Mme DARTIGOLLES n'est ni inscrite sur la liste des commissaires aux comptes, ni associée, ni dirigeante : elle ne peut signer, même « par délégation ». Signer serait exercer illégalement la profession, ce qui constitue un délit [V L. 821-7 2°] ; un rapport ainsi signé ne serait pas une certification régulière [S].
- **Solution** : le rapport est signé par **Mme LABARTHÈRE**, associée inscrite sur la liste (et sur celle de la durabilité pour le second rapport), après avoir pris connaissance du dossier et revu les travaux et les conclusions, avec l'appui de Mme DARTIGOLLES, qui conserve la direction des travaux [S, application] ; à défaut, la date du rapport est reportée au retour de M. PICHEYRE, dans un délai compatible avec l'assemblée du 24/06/2027 [S]. Si M. PICHEYRE devait de toute façon cesser d'intervenir (question 3.3), c'est la même solution.

**Réponses tolérées**
- Une présentation des instances limitée à leur rôle principal (tableau de l'ordre et conseils régionaux ; liste de la H2A, CNCC, CRCC) : points complets si la conclusion est juste.
- La mention que Mme DARTIGOLLES, diplômée d'expertise comptable, pourrait demander son inscription sur la liste si elle remplit la condition de stage, sans développement : sans points supplémentaires (l'accès à la profession n'est pas demandé).

**Erreurs fréquentes**
- Admettre qu'un expert-comptable peut signer un rapport de certification parce qu'il est diplômé (`JUR-A03`).
- Présenter l'ordre des experts-comptables comme l'instance des commissaires aux comptes (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 1, 2, 3, 28, 31, 33, 40 | Inscription au tableau ; conseils régionaux et Conseil national | [V] | F09 § 2.1-2.2 |
| C. com. L. 820-1, L. 821-12, L. 821-13, L. 821-14, L. 821-25, L. 821-7 2° | Liste de la H2A ; CNCC et CRCC ; signature au nom de la société ; exercice illégal | [V] ; solution : [S] | F09 § 3.1-3.2, § 7.3, § 18 |

### 3.2 Fin du mandat, renouvellement et second commissaire aux comptes (2 pts)

**Fin normale et renouvellement (0,75 pt)**
- Le cabinet a été désigné pour **six exercices**, de 2021 à 2026 ; ses fonctions **expirent après l'assemblée qui statue sur les comptes du sixième exercice**, celle du 24/06/2027 [V L. 821-44 al. 1].
- La SA reste **tenue** d'avoir un commissaire aux comptes : elle dépasse les trois seuils de la société anonyme (total du bilan de 19 600 000 € puis 23 900 000 €, pour 5 000 000 € ; chiffre d'affaires de 26 400 000 € puis 29 800 000 €, pour 10 000 000 € ; 158 puis 165 salariés, pour 50) ; l'obligation ne cesserait que si deux des trois seuils n'avaient pas été dépassés pendant les deux exercices précédant l'expiration du mandat [V L. 225-218 al. 2 ; D. 225-164-1 ; D. 221-5 ; S, application].
- L'assemblée peut **renouveler** le cabinet ou désigner un autre commissaire aux comptes ; le nouveau mandat est de **six exercices** (2027 à 2032), sans faculté de le limiter à trois exercices, la désignation étant imposée par les seuils [V L. 821-40 I, L. 821-44, L. 821-46]. Le cabinet, société à plusieurs associés, n'a pas besoin de suppléant [V L. 821-40 I al. 3]. S'il est proposé de ne pas le renouveler, il est entendu à sa demande [V L. 821-51].
- **Avant d'accepter le renouvellement**, le cabinet vérifie que les exigences légales et déontologiques sont toujours respectées [V code de déontologie art. 25] : la situation de M. PICHEYRE (question 3.3) doit être réglée.

**Le second commissaire aux comptes (1,25 pt)**
- **La SA n'y est pas tenue** : la désignation d'au moins deux commissaires aux comptes n'est imposée qu'aux entités astreintes à publier des comptes consolidés [V L. 821-41 al. 1] ; la SA ne contrôle aucune société (hypothèse) et n'est pas une entité d'intérêt public ; les seuils lui imposent **au moins un** commissaire aux comptes [V L. 225-218 al. 2].
- **Les textes le permettent** : l'assemblée générale ordinaire « peut désigner **un ou plusieurs** commissaires aux comptes » [V L. 225-218 al. 1 ; L. 821-40 I al. 2]. La décision appartient à l'assemblée, à la majorité : le fonds, avec 20 % du capital, ne peut l'imposer seul ; il peut la proposer et obtenir l'accord de la famille [S]. Ce second commissaire aux comptes étant désigné **volontairement**, son mandat de six exercices peut être limité à trois exercices [V L. 821-46 ; S, application].
- **Les règles du co-commissariat s'appliqueraient** dès la désignation de deux commissaires aux comptes, même volontaire : examen contradictoire des conditions d'établissement des comptes et répartition des diligences selon une NEP [V L. 821-62] ; **rapport commun**, qui indique les opinions divergentes [V D. 821-184] ; les commissaires aux comptes appartiennent à des **structures d'exercice distinctes** : pas de dirigeants communs, **pas de liens capitalistiques ou financiers**, pas de réseau commun [V code de déontologie art. 24 I].
- **Le candidat proposé** : le cabinet ESCAUDE détient 30 % du capital de BRASSENX Audit : ce **lien capitalistique** interdit que les deux cabinets partagent la mission [V code de déontologie art. 24 I]. Le fonds doit proposer un autre cabinet, sans lien avec ESCAUDE. Enfin, un second commissaire aux comptes ne « protège » pas l'investissement du fonds : il certifie les comptes pour tous leurs utilisateurs et ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55 ; S].

**Réponses tolérées**
- Un raisonnement qui ne cite pas l'option de trois exercices pour le second commissaire aux comptes : points complets si le reste est juste.
- La mention que le fonds pourrait négocier la désignation dans un accord avec la famille, sans développement : sans points supplémentaires.

**Erreurs fréquentes**
- Affirmer que toute SA d'une certaine taille doit avoir deux commissaires aux comptes, ou que le co-commissariat est interdit hors comptes consolidés (`JUR-A04`).
- Admettre BRASSENX Audit au motif qu'il s'agit d'une autre société, sans examiner le lien capitalistique (`JUR-A05`).
- Décrire la procédure de désignation (ordre du jour, résolution, formalités), qui n'est pas demandée (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 225-218 al. 1-2, D. 225-164-1, D. 221-5 | Un ou plusieurs commissaires aux comptes ; seuils ; fin de l'obligation | [V] ; application : [S] | F09 § 3.3, § 24 |
| C. com. L. 821-40 I, L. 821-41, L. 821-44, L. 821-46, L. 821-51, L. 821-55, L. 821-62, D. 821-184 ; code de déontologie art. 24 I, 25 | Durée, renouvellement, co-commissariat, rapport commun, structures distinctes | [V] ; application : [S] | F09 § 3.4-3.7, § 10, § 24 |

### 3.3 Les actions reçues par M. PICHEYRE (1,5 pt)

**Appréciation (0,75 pt)**
- Le commissaire aux comptes ne peut **prendre, recevoir ou conserver**, directement ou indirectement, un intérêt auprès de l'entité dont il certifie les comptes [V L. 821-31 I]. Le code de déontologie déclare **incompatible** avec la mission de certification la **détention, directe ou indirecte, d'actions** de l'entité certifiée par le commissaire aux comptes, sa société de commissaires aux comptes et **les associés et salariés qui participent à la mission** [V code de déontologie art. 33 I 1°] ; seule échappe à cette règle une détention par l'intermédiaire d'organismes de placement collectif diversifiés [V art. 33 I, dernier alinéa].
- M. PICHEYRE, associé **signataire**, détient directement 600 actions depuis le 12/10/2026. La règle ne prévoit **aucun seuil** : le faible pourcentage (1,2 %), l'absence d'influence et l'origine successorale (il les a **reçues** sans les acheter) ne l'écartent pas, puisque le texte vise aussi le fait de recevoir ou de conserver [V ; S, application]. Un tiers informé douterait de son objectivité : il a un intérêt personnel à la valeur des actions, donc aux comptes qu'il certifie, et vient d'entrer au capital au moment où la SA ouvre celui-ci à un investisseur [V code de déontologie art. 5 I-II ; S].
- Survenue **en cours de mission**, cette situation oblige à en tirer **sans délai** les conséquences [V code de déontologie art. 35]. Son intention de conserver les actions et de continuer à signer est inacceptable.

**Mesures (0,75 pt)**
- **Céder les actions sans délai**, par exemple aux actionnaires familiaux qui proposent de les racheter, avant toute nouvelle intervention sur la mission ; ou, s'il refuse, **retirer M. PICHEYRE de la mission** et confier la signature et la supervision à un autre associé, Mme LABARTHÈRE [V art. 33, 35 ; S, mesures].
- **Revue** par un associé qui n'est pas intervenu des travaux et des conclusions dirigés par M. PICHEYRE depuis le 12/10/2026 (intervention intermédiaire de novembre 2026, travaux de fin d'exercice), complétés si nécessaire ; **documentation** de la situation et des mesures [V code de déontologie art. 5 III ; S].
- La situation doit être réglée **avant les rapports** du 07/04/2027 et avant l'acceptation du renouvellement [V code de déontologie art. 25] ; à défaut de mesures suffisantes, le cabinet ne pourrait poursuivre la mission [V art. 5 III]. Le maintien de la détention exposerait M. PICHEYRE à des sanctions disciplinaires [V L. 821-70 II 1°].

**Réponses tolérées**
- La cession présentée comme seule mesure possible pour M. PICHEYRE, avec son retrait de la mission jusqu'à la cession : points complets.

**Erreurs fréquentes**
- Admettre la détention parce qu'elle est faible ou héritée (`JUR-A05`).
- Réciter des principes déontologiques sans les appliquer à la détention d'actions (`JUR-A06`).
- Confondre avec l'indépendance de l'expert-comptable, appréciée autrement (`JUR-A03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-31 I, L. 821-70 II 1° | Interdiction de recevoir ou de conserver un intérêt ; sanction des associés participants | [V] | F10 § 4.1, § 20 |
| Code de déontologie art. 5, 25, 33 I, 35 | Indépendance et sauvegardes ; renouvellement ; liens financiers ; survenance en cours de mission | [V] ; application : [S] | F10 § 2.1, § 4.1, § 20 |

### 3.4 La norme sur l'audit réalisé par plusieurs commissaires aux comptes (1,5 pt)

**Norme pertinente (0,25 pt)** : la NEP relative à l'**audit des comptes réalisé par plusieurs commissaires aux comptes** (annexe 3.5), qui met en œuvre l'examen contradictoire et la répartition des diligences prévus par la loi [V L. 821-62 ; NEP plusieurs commissaires § 01-02]. Elle s'appliquerait dès la désignation du second commissaire aux comptes, même volontaire : elle vise tout audit réalisé par plusieurs commissaires aux comptes [§ 01 ; S].

**Conséquences sur la proposition du fonds (1 pt)**
- Les deux commissaires aux comptes forment ensemble l'**organe de contrôle légal** [§ 01] ; **chacun** met en œuvre les travaux qui lui permettent de formuler **son** opinion [§ 04] : un second commissaire aux comptes ne peut se borner à revoir les travaux d'ESCAUDE en fin de mission.
- Chacun prend connaissance de la SA, évalue le risque et détermine les seuils ; ils définissent **ensemble** l'approche, le plan de mission et le programme de travail [§ 05], puis **répartissent** les procédures [§ 06].
- La répartition est **équilibrée**, selon des critères **quantitatifs** (heures) et **qualitatifs** (expérience des équipes) [§ 07] : 40 heures face à un programme de 420 heures seraient disproportionnées ; une répartition par cycles (par exemple, capitaux propres et immobilisations pour l'un, ventes et achats pour l'autre) serait nécessaire [S, application].
- Chacun **revoit** les travaux de l'autre, apprécie s'ils sont conformes à la répartition, suffisants et appropriés, et si les conclusions sont pertinentes, documente cette revue et décide d'éventuelles procédures supplémentaires [§ 10-13] : la revue est **réciproque**, pas unilatérale.
- Ils communiquent **ensemble** avec le directoire et le conseil de surveillance [§ 17] ; le rapport est **signé par chacun** et mentionne leurs éventuelles divergences [§ 19-20] ; c'est un **rapport commun** [V D. 821-184], destiné à l'assemblée générale : le second commissaire aux comptes ne peut remettre au fonds un rapport séparé, qui méconnaîtrait en outre le **secret professionnel** [V L. 821-35 al. 1 ; S].

**Élaboration des NEP (0,25 pt)** : la NEP est élaborée par une commission de normalisation placée auprès de la H2A, soumise à l'avis de la CNCC, adoptée par le collège de la H2A puis **homologuée par arrêté du garde des sceaux** [V L. 820-4, L. 820-23 ; F11 § 3.2].

**Réponses tolérées**
- Une phrase sur l'élaboration limitée à « adoptée par la H2A après avis de la CNCC et homologuée par arrêté » : points complets.

**Erreurs fréquentes**
- Citer la norme par son numéro sans en appliquer le contenu à la proposition (`JUR-A06`).
- Admettre qu'un co-commissaire puisse ne faire qu'une revue des travaux de l'autre (`JUR-A04`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP plusieurs commissaires § 01-07, 10-13, 17, 19-20 ; L. 821-62 ; D. 821-184 ; L. 821-35 al. 1 | Exercice collégial ; répartition ; revue réciproque ; rapport commun ; secret | [V] ; application : [S] | F09 § 3.6, § 10 |
| L. 820-4, L. 820-23 | Élaboration des NEP | [V] | F11 § 3.2 |

### 3.5 Les trois responsabilités et le plan d'affaires (1,5 pt)

**Distinction (0,75 pt)**

| | Civile | Pénale | Disciplinaire |
|---|---|---|---|
| Objet | Réparer le dommage causé par une **faute ou une négligence** dans l'exercice de la profession, envers l'entité **et les tiers** [V L. 821-37 al. 1] | Punir une **infraction** pénale ; pour le commissaire aux comptes, notamment le fait de **donner ou de confirmer des informations mensongères** sur la situation de la personne morale [V L. 821-9], infraction intentionnelle [S] | Sanctionner une **faute disciplinaire** : manquement aux conditions légales d'exercice, négligence grave, fait contraire à la probité ou à l'honneur [V L. 821-70 I] |
| Conditions | Faute, préjudice, lien de causalité ; obligation de moyens : l'audit procure une assurance raisonnable, non absolue [S ; V NEP principes § 08-09] | Élément matériel et élément intentionnel (connaissance du caractère mensonger) [S] | Faute disciplinaire établie [V L. 821-70 I] |
| Sanctions | Dommages-intérêts [S] | Emprisonnement et amende (cinq ans et 75 000 € pour l'infraction citée) [V L. 821-9] | Avertissement, blâme, interdiction temporaire, radiation, sanction pécuniaire, prononcés par la **commission des sanctions de la H2A**, non par la CNCC ou les CRCC [V L. 821-71, L. 821-79] |

**Appréciation du risque (0,75 pt)**
- **Comptes de 2025** : le fonds, entré au capital au vu de ces comptes, est un tiers qui pourrait invoquer une faute [V L. 821-37 ; S]. Aucune anomalie n'a été relevée depuis la certification et le dossier documente les procédures : aucune faute, ni a fortiori aucune information mensongère donnée sciemment, n'apparaît ; le risque est **faible**, tant au civil qu'au pénal [S, application].
- **Plan d'affaires** : la certification porte sur les comptes historiques et **ne garantit ni la viabilité ni la qualité de la gestion** [V L. 821-55] ; le plan a été établi par le directoire, sans le cabinet. Un chiffre d'affaires de 2027 inférieur aux prévisions ne peut engager la responsabilité du cabinet : **aucun risque** à ce titre [S].
- **Risque réel** : il tient à la détention d'actions par M. PICHEYRE (question 3.3) : manquement aux conditions légales d'exercice et aux règles sur les liens financiers, passible de sanctions disciplinaires s'il n'y est pas mis fin [V L. 821-70 I-II ; S]. La réponse au fonds rappelle ces principes, sans lui communiquer d'information couverte par le secret [V L. 821-35 al. 1].

**Réponses tolérées**
- La mention de la prescription de trois ans de l'action civile, sans développement : sans points supplémentaires.

**Erreurs fréquentes**
- Présenter le commissaire aux comptes comme garant de la réalisation des prévisions ou de la rentabilité de l'investissement (`JUR-A01`).
- Confondre les trois responsabilités ou attribuer le pouvoir disciplinaire à la CNCC (`JUR-A01`).
- Développer la procédure (saisine, juridiction, délais), qui n'est pas demandée (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-37, L. 821-9, L. 821-70, L. 821-71, L. 821-79, L. 821-55, L. 821-35 al. 1 ; NEP principes § 08-09 | Trois responsabilités ; absence de garantie ; secret | [V] ; conditions et appréciation : [S] | F09 § 6, § 7 ; F11 § 1.1 |

### 3.6 Audit légal, audit contractuel et autres prestations (1,5 pt)

**Distinction (1 pt)**
- **Audit légal** : mission confiée au commissaire aux comptes par la loi, qui aboutit à la **certification** que les comptes annuels sont réguliers et sincères et donnent une image fidèle [V L. 821-2 III, L. 821-53 al. 1]. L'opinion repose sur une **assurance raisonnable**, élevée mais non absolue, que les comptes pris dans leur ensemble ne comportent pas d'**anomalies significatives** [V NEP principes § 01, 04, 08]. Le rapport est destiné à l'assemblée générale.
- **Audit contractuel** : audit demandé hors obligation légale, par exemple sur une situation intermédiaire ; pour le commissaire aux comptes de l'entité, c'est une **prestation** (« audit financier contractuel »), fournie à l'entité selon une **lettre de mission** qui en fixe l'objet, l'étendue et le destinataire [V L. 821-2 IV ; A. 821-55 § 08 ; R. 821-195].
- **Autres prestations** : services et attestations qui ne relèvent pas d'une mission ; pour une entité qui n'est pas d'intérêt public, le commissaire aux comptes ne peut les fournir s'ils créent un risque d'**autorévision** ou compromettent son indépendance sans sauvegarde possible [V L. 821-2 IV ; L. 821-28 IV].

**Réponse au fonds (0,5 pt)**
- **Situation au 30/06/2027** : un audit contractuel est possible, mais comme prestation **commandée par la SA** (directoire), qui en recevrait les conclusions et pourrait les transmettre au fonds ; le cabinet ne peut les adresser directement au fonds, tiers tenu hors du secret [V L. 821-35 al. 1 ; S].
- **Plan d'affaires** : il comporte des **prévisions** ; ni la certification ni un audit ne garantissent sa réalisation [V L. 821-55]. La certification des comptes de 2026 ne couvre ni le plan, ni la rentabilité de l'investissement, ni la qualité de la gestion ; toute intervention du cabinet sur la cohérence des hypothèses serait une prestation distincte, à examiner au regard de son indépendance [S ; L. 821-28 IV].

**Réponses tolérées**
- La distinction audit externe et audit interne, ajoutée sans être demandée : sans points supplémentaires.

**Erreurs fréquentes**
- Confondre l'audit contractuel avec la certification, ou admettre que le cabinet « certifie » le plan d'affaires (`JUR-A01`).
- Accepter d'adresser les conclusions directement au fonds (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-2 III-IV, L. 821-28 IV, L. 821-35, L. 821-53, L. 821-55, R. 821-195 ; A. 821-55 § 08 ; NEP principes § 01, 04, 08 | Missions et prestations ; audit contractuel ; assurance raisonnable ; limites | [V] ; réponse : [S] | F11 § 1.1-1.2, § 13.2 ; F10 § 5 |

### 3.7 Informations auprès des tiers et demandes de confirmation (1,5 pt)

**Le droit et la technique (1 pt)**
- **Droit d'information auprès des tiers** : le commissaire aux comptes peut recueillir **toutes informations utiles** auprès des **tiers qui ont accompli des opérations pour le compte** de l'entité ; ce droit ne s'étend pas à la communication des **pièces, contrats et documents** détenus par ces tiers, sauf **décision de justice** ; le secret professionnel ne peut lui être opposé, sauf par les auxiliaires de justice [V L. 821-61 al. 2-3 ; D. 821-175].
- **Demande de confirmation** : déclaration d'un tiers **directement adressée** au commissaire aux comptes, fermée ou ouverte [V NEP confirmations § 3-4] ; le commissaire aux comptes a la **maîtrise** de la sélection des tiers, de la rédaction, de l'envoi et de la réception [§ 9]. Un élément obtenu d'une source externe et directement par le commissaire aux comptes est plus fiable qu'un document fourni par l'entité [V NEP éléments probants § 6].
- **Limites** : le tiers n'est pas tenu de répondre (procédures alternatives en cas d'absence de réponse) [§ 13] ; les pièces des tiers ne sont pas exigibles sans décision de justice ; le **fonds** a souscrit pour son propre compte et n'a pas accompli d'opérations pour le compte de la SA : sa réponse est une confirmation volontaire, non l'exercice du droit légal [S, lecture de L. 821-61] ; la **banque**, dépositaire des fonds et teneur des comptes de la SA, relève du droit d'information [S].

**Réponse au président du directoire (0,5 pt)**
- Si la direction s'oppose aux demandes, le cabinet examine si le refus repose sur des **motifs valables** [§ 10]. La nouveauté des relations n'en est pas un : une confirmation ne met en cause ni le fonds ni la banque.
- Les copies remises par la SA (bulletin, certificat, relevés) sont utiles mais **moins probantes** que des réponses adressées directement au cabinet, sur une opération de 3 000 000 € qui modifie le capital [V NEP éléments probants § 6 ; S].
- Le cabinet maintient ses demandes ; si le refus, non fondé, persiste, il en tire les **conséquences dans son rapport** (limitation) [§ 12] ; si un motif valable était établi, il mettrait en œuvre des procédures alternatives [§ 11]. L'annexe 3.8 montre que l'opposition a été levée.

**Réponses tolérées**
- Une réponse qui ne distingue pas la situation du fonds et celle de la banque, si le droit, sa limite (pièces des tiers) et la réponse sont exacts : 1,25 pt sur 1,5.

**Erreurs fréquentes**
- Laisser la SA envoyer ou recevoir les confirmations (`JUR-A01`).
- Accepter les documents de la direction comme équivalents, sans apprécier le refus (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-61 al. 2-3, D. 821-175 | Informations auprès des tiers ; pièces sur décision de justice ; secret inopposable | [V] ; application au fonds et à la banque : [S] | F11 § 2, § 23.2, § 29 |
| NEP confirmations § 3-4, 9-13 ; NEP éléments probants § 6 | Maîtrise de la demande ; refus de la direction ; fiabilité | [V] | F11 § 6.1, § 6.3 |

### 3.8 Capitaux propres : risques et procédures (5 pts)

**a. Risques d'anomalies significatives et assertions (2 pts ; 0,25 pt par risque correctement relié à ses assertions, dans la limite de 2 pts)**

Facteurs de risque inhérent : opérations **non courantes** et d'un montant élevé (augmentation de capital de 3 000 000 €, subvention de 540 000 €), frais à répartir entre capitaux propres et TVA, estimation de la durée de reprise de la subvention, nouvel actionnaire attentif aux comptes, intérêt de la direction à présenter un résultat élevé la première année après l'entrée du fonds [V NEP risques § 02 ; S, application]. Si le cabinet ne teste pas l'efficacité des procédures de l'entité, l'évaluation du risque au niveau des assertions correspond au risque inhérent [V NEP risques § 41].

| Risque | Origine dans les annexes | Assertions |
|---|---|---|
| Augmentation de capital enregistrée sans décision régulière ou pour un montant différent de la décision, de la souscription et de la libération | AGE du 22/06/2026, constatation du 22/09/2026 | Réalité et mesure des opérations ; existence et droits et obligations du capital |
| Capital et prime mal ventilés (nominal, prime de 275 € par action) | 10 000 actions à 300 € | Mesure ; classification ; évaluation |
| Frais imputés sur la prime pour un montant erroné (TVA déductible imputée) | Frais toutes taxes comprises (annexe 3.6) | Mesure et classification ; évaluation de la prime ; exhaustivité des créances de TVA |
| Dividende non conforme à la décision de l'assemblée ou affectation erronée | 8 € × 40 000 actions ; solde en réserves | Réalité et mesure ; conformité de la répartition des réserves (évaluation) |
| Reprise de la subvention mal calculée | Reprise sur cinq ans, presse amortie sur dix ans | Mesure et séparation des exercices du produit ; évaluation de la subvention au bilan |
| Subvention sujette à une condition non respectée | Engagement de maintien pendant dix ans | Droits et obligations ; exhaustivité des dettes (reversement) |
| Amortissements dérogatoires mal calculés | Plan fiscal dégressif, prorata de neuf mois | Mesure ; évaluation des provisions réglementées |
| Information incomplète dans l'annexe | Actions émises, frais imputés, subvention, tableau de variation | Exhaustivité ; présentation et intelligibilité ; mesure et évaluation des informations [V PCG art. 832-11] |

**b. Procédures en réponse (3 pts ; 0,25 pt par procédure reliée à son objectif, dans la limite de 2,25 pts, et 0,75 pt pour les recalculs)**
- **Lecture des procès-verbaux** de l'AGO et de l'AGE du 22/06/2026, du directoire du 22/09/2026 et des **statuts modifiés** : nombre d'actions, nominal, prix, bénéficiaire, délégation au directoire, montant du dividende — *réalité, conformité aux décisions des organes* [V NEP éléments probants § 10, inspection].
- **Rapprochement** du bulletin de souscription, du **certificat de la banque** et du relevé bancaire (3 000 000 € reçus le 16/09/2026, mis à disposition le 25/09/2026) avec les comptes 1013 et 1041 — *réalité, mesure*.
- **Rapprochement avec le registre des mouvements de titres** : 10 000 actions inscrites au nom du fonds le 22/09/2026 ; 50 000 actions au 31/12/2026, dont les 600 de M. PICHEYRE inscrites le 20/10/2026 (question 3.3) — *existence, exhaustivité*.
- **Demandes de confirmation** au fonds et à la banque, préparées, envoyées et reçues par le cabinet — *réalité de la souscription et de la libération, existence des soldes* [V NEP confirmations § 9].
- **Contrôle des frais imputés** : inspection des deux factures et de leur lien avec l'opération (avocat, conseil financier), contrôle du montant hors taxes imputé et de la TVA déductible inscrite en créance — *mesure, classification* [V PCG art. 212-9] ; il révèle l'anomalie 2.
- **Contrôle de l'affectation** : rapprochement du procès-verbal, des comptes 120, 1068 et 457 et du paiement du 15/07/2026 ; vérification que la réserve légale atteignait le dixième du capital, de sorte qu'aucune dotation n'était due — *mesure, réalité*.
- **Lecture de la convention de subvention** et inspection des deux versements ; demande d'information sur le respect de l'engagement de maintien — *droits et obligations, exhaustivité*.
- **Recalcul de la reprise de la subvention** et des **dérogatoires** (ci-dessous) — *mesure, évaluation* ; il révèle l'anomalie 1.
- **Contrôle de l'annexe** et du tableau de variation des capitaux propres : rapprochement avec les mouvements de l'exercice — *exhaustivité, présentation*.
- **Déclarations écrites** de la direction sur l'exhaustivité des décisions des organes et des engagements liés à l'opération — *exhaustivité* [V NEP déclarations].

*Recalculs (0,75 pt)*
- Capital : 10 000 × 25 = **250 000 €** ; prime : 10 000 × (300 − 25) = **2 750 000 €** ; total versé : **3 000 000 €** ; capital au 31/12/2026 : 50 000 × 25 = **1 250 000 €**.
- Dividende : 40 000 × 8 = **320 000 €** ; autres réserves : 1 120 000 − 320 000 = **800 000 €** ; réserve légale : 100 000 € = 1 000 000 × 10 %.
- Frais : 54 000 + 60 000 = **114 000 €** hors taxes ; TVA : 114 000 × 20 % = **22 800 €** ; montant imputé par la SA : 136 800 €.
- Amortissement comptable de la presse : 1 800 000 / 10 × 9/12 = **135 000 €** ; dérogatoires : 303 750 − 135 000 = **168 750 €**, conformes ; reprise de la subvention : 540 000 × 135 000 / 1 800 000 = **40 500 €**, contre 81 000 € comptabilisés.
- Variation des capitaux propres du projet : 9 718 950 − 5 330 000 = 4 388 950 € = 3 000 000 − 136 800 − 320 000 + 1 260 000 + 459 000 + (168 750 − 42 000).

**Réponses tolérées**
- En a. et b., d'autres risques ou procédures tirés des annexes, correctement reliés à des assertions ou à des objectifs (par exemple, procédure analytique sur la variation des capitaux propres).
- La mention de la dotation à la réserve légale qui sera due sur le résultat de 2026 (le dixième du capital passe à 125 000 €), sans points supplémentaires.

**Erreurs fréquentes**
- Confondre réalité (flux) et existence (soldes), ou citer des assertions sans les relier à un risque (`JUR-A01`).
- Proposer des procédures générales, sans lien avec les opérations de l'exercice (`JUR-A06`).
- Traiter les interventions particulières de la loi sur les opérations en capital, qui ne sont pas demandées (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP risques § 02, § 41 ; NEP éléments probants § 9-10 ; NEP confirmations § 9 ; NEP déclarations | Facteurs de risque ; assertions ; techniques ; confirmation | [V] | F11 § 4.1, § 4.3, § 6 |
| PCG art. 212-9, 312-1, 832-11 | Frais d'augmentation de capital ; reprise des subventions ; information sur le capital | [V] ; application : [S] | F11 § 14.2, § 29 |

### 3.9 Anomalies, écritures et opinion (2 pts)

**Anomalies et caractère significatif (0,75 pt)**
- **Anomalie 1 — reprise de la subvention** : 81 000 − 40 500 = **40 500 €**. Le produit et le résultat sont surévalués de 40 500 € (résultat de 1 260 000 € au lieu de 1 219 500 €, avant impôt) et la subvention au bilan sous-évaluée d'autant (459 000 € au lieu de 499 500 €) ; le total des capitaux propres est inchangé. Elle représente **1,16 fois** le seuil de signification (35 000 €) : **significative**. L'argument de la direction ne tient pas : la règle lie la reprise au rythme de l'amortissement de la presse, amortie sur dix ans. Le PCG admet une dérogation à la durée et au rythme de reprise si des circonstances particulières le justifient, par exemple les conditions posées ou les engagements demandés par l'organisme qui a alloué la subvention ; elle est écartée ici : la convention ne fixe aucune modalité de reprise, l'engagement de maintien de dix ans coïncide avec la durée d'utilisation, et l'horizon du plan d'affaires n'est pas une circonstance particulière au sens du PCG [V PCG art. 312-1 ; NEP caractère significatif § 9 ; S, application].
- **Anomalie 2 — frais toutes taxes comprises** : 136 800 − 114 000 = **22 800 €** de TVA déductible imputés sur la prime ; la prime d'émission est sous-évaluée (2 613 200 € au lieu de 2 636 000 €) et la créance de TVA omise. **0,65 fois** le seuil, sans incidence sur le résultat : **non significative** seule ; supérieure au seuil des anomalies manifestement insignifiantes (1 750 €), elle est récapitulée [V NEP anomalies § 8, § 14]. Les deux anomalies, de nature différente, ne se cumulent pas sur le résultat.

**Écritures de correction au 31/12/2026 (0,5 pt)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 747 | Quote-part des subventions d'investissement virée au résultat de l'exercice | 40 500 | |
| | 139 | Subventions d'investissement inscrites au compte de résultat | | 40 500 |

Libellé : annulation de la reprise excédentaire de la subvention de la Région, 81 000 − 540 000 × 135 000 / 1 800 000 (écriture X1, équilibrée à 40 500 €).

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 44566 | TVA sur autres biens et services | 22 800 | |
| | 1041 | Primes d'émission | | 22 800 |

Libellé : TVA déductible sur les frais de l'augmentation de capital imputée à tort sur la prime d'émission, 114 000 × 20 % (écriture X2, équilibrée à 22 800 €). Les écritures sont présentées hors impôt sur les bénéfices, selon les hypothèses de l'énoncé.

**Opinion selon les décisions de la SA (0,5 pt)**
- **Frais corrigés, reprise maintenue (position de Mme MOUSTIÉ)** : anomalie significative non corrigée ; ses incidences sont **clairement circonscrites** (un poste, un montant chiffré) et une réserve qui les quantifie suffit à l'utilisateur : **certification avec réserve pour désaccord** ; un refus de certifier ne se justifie pas [V NEP rapport § 09-10, § 12].
- **Les deux anomalies sont corrigées** : **certification sans réserve** [V NEP rapport § 08].

**Parties du rapport, cas d'une réserve (0,25 pt)** : la partie « **Opinion avec réserve** » indique que, sous cette réserve, les comptes sont réguliers et sincères et donnent une image fidèle ; la partie « **Fondement de l'opinion avec réserve** » expose le motif et le chiffre (reprise de la subvention surévaluée de 40 500 €, résultat surévalué d'autant) ; viennent ensuite la justification des appréciations, les responsabilités de la direction et des organes et celles du commissaire aux comptes, la date et la signature. Les motifs sont communiqués au préalable au directoire et au conseil de surveillance ; le rapport est destiné à l'assemblée générale [V NEP rapport § 06, § 18 ; L. 821-63 I ; R. 821-180].

**Réponses tolérées**
- Les deux autres cas, traités en plus : reprise corrigée et frais non corrigés, **certification sans réserve**, l'anomalie figurant à l'état des anomalies non corrigées joint aux déclarations écrites [V NEP anomalies § 17] ; aucune correction, **réserve pour désaccord** au titre de la reprise, l'anomalie sur les frais ne changeant pas l'opinion [V NEP anomalies § 14] : sans points supplémentaires.
- Pour l'anomalie 2, une correction présentée par une écriture qui reprend l'imputation entière (contre-passation de 136 800 € et nouvelle imputation de 114 000 €), si le résultat est le même : points complets.
- L'anomalie 1 appréciée aussi au regard de l'incidence fiscale (30 375 € net d'impôt, sous le seuil) si le candidat retient l'appréciation avant impôt imposée par l'énoncé : points complets ; une conclusion fondée sur le seul montant net d'impôt : 0,25 pt sur 0,75.

**Erreurs fréquentes**
- Juger la reprise acceptable parce qu'elle suit l'horizon du plan d'affaires (`JUR-A06`).
- Conclure à un refus de certifier pour une anomalie circonscrite (`JUR-A02`).
- Écriture sans libellé ou sans numéro de compte, ou passée en résultat exceptionnel (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Liste des comptes ; PCG art. 212-9, 312-1 | Comptes 747, 139, 44566, 1041 ; frais imputés ; reprise | [V] | F11 § 14.2, § 29 |
| NEP caractère significatif § 9 ; NEP anomalies § 8, 14, 17 ; NEP rapport § 06-10, 12, 18 ; R. 821-180 ; L. 821-63 I | Caractère significatif ; opinions ; parties du rapport | [V] ; qualification : [S] | F11 § 4.2, § 8, § 14.1 |

---

### Partie B – Durabilité (12 points)

La SA peut appliquer pour 2026 l'une ou l'autre version des ESRS ; le corrigé s'appuie sur ESRS 1 (2026), dont les solutions retenues ici sont aussi celles de 2023 [S].

### 3.10 Champ d'application et étendue d'une publication volontaire (2 pts)

**Pourquoi la SA n'est pas tenue de publier (0,75 pt)**
- Au 31/12/2026, le Code de commerce vise les **grandes entreprises** : deux des trois seuils (bilan de 25 000 000 €, chiffre d'affaires net de 50 000 000 €, 250 salariés), franchis à la clôture de deux exercices consécutifs [V L. 232-6-3 I ; L. 230-1 ; D. 230-1 3°]. La SA ne dépasse **aucun** de ces seuils, ni en 2025 ni en 2026 (bilan de 23 900 000 €, chiffre d'affaires de 29 800 000 €, 165 salariés) : elle n'est pas une grande entreprise [S, application].
- Elle n'est pas non plus une petite ou moyenne entreprise cotée, ses actions n'étant admises sur aucun marché ; et, sous les seuils de la directive du 24/02/2026 (450 000 000 € de chiffre d'affaires et 1 000 salariés), elle resterait hors du champ après la transposition [V annexe 3.9 ; F12 § 10 ; S].

**Étendue et limites de la publication volontaire selon les ESRS (1 pt)**
- **Ce qu'elle couvre** : en déclarant ses informations établies selon les ESRS, la SA s'oblige à en respecter les exigences : analyse de **double matérialité** (impacts sur les personnes et l'environnement ; risques et opportunités financiers), informations générales sur la base de préparation, la gouvernance, la stratégie et la gestion des impacts, risques et opportunités, puis informations sur chaque sujet **matériel** ; informations portant sur la même entreprise que les comptes annuels et, dans la mesure nécessaire, sur sa **chaîne de valeur** amont et aval ; objectif d'image fidèle des impacts, risques et opportunités matériels [V ESRS 1 (2026) § 3, § 25, § 60, § 62-63 ; F12 § 2, § 5, § 8].
- **Ce qu'elle ne couvre pas** : les sujets **non matériels** (pas d'exhaustivité sur tous les thèmes) ; chaque acteur de la chaîne de valeur, seules les informations matérielles étant requises, au besoin par estimation [V ESRS 1 (2026) § 64-65] ; les informations de la taxonomie, que la SA ne publie pas ; aucune obligation légale de certification, la vérification reposant sur la décision de l'assemblée et la lettre de mission [F12 § 11 (b)]. Les informations, souvent prospectives ou estimées, ne garantissent pas les performances futures [S].
- La publication volontaire répond aux attentes du fonds et des négociants clients, qui doivent eux-mêmes publier des informations sur leur chaîne de valeur [S, application].

**L'EFRAG (0,25 pt)** : organisme européen, conseiller technique de la Commission, qui prépare les projets d'ESRS ; la Commission les adopte par actes délégués [V règlement 2026/1563, considérant 3 ; F12 § 1].

**Réponses tolérées**
- La mention de la norme volontaire des PME élaborée par l'EFRAG, que la SA aurait pu choisir, sans développement : sans points supplémentaires (le choix n'est pas demandé).
- Une analyse fondée sur les seuils de la directive seule, si le candidat conclut juste : 0,5 pt sur 0,75.

**Erreurs fréquentes**
- Développer le calendrier ou la transposition de la directive, au-delà de la conclusion (`JUR-A06`).
- Présenter la publication volontaire comme limitée aux sujets que l'entreprise choisit librement, sans analyse de matérialité (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 232-6-3, L. 230-1, D. 230-1 ; directive (UE) 2026/470 | Champ au 31/12/2026 ; seuils de la directive | [V] ; état de la transposition au 25/11/2026 : [V] | F12 § 10, § 25 |
| ESRS 1 (2026) § 3, 25, 60, 62-65 ; règlement 2026/1563 consid. 3 | Objectif, double matérialité, entreprise déclarante, chaîne de valeur ; EFRAG | [V] ; application : [S] | F12 § 1-2, § 5-8, § 11 |

### 3.11 Périmètre, chaîne de valeur et connectivité (3 pts)

**Situer les éléments du cas (1,25 pt)**

| Élément | Place | Justification |
|---|---|---|
| Site de Libourne | **Activités propres** | Actifs, passifs, produits et charges de la SA, même entreprise déclarante que les comptes annuels [V ESRS 1 (2026) § 60-61] |
| Entrepôt de Coutras | **Activités propres** | Actif **loué** et exploité par la SA : le preneur déclare dans ses activités propres les impacts liés à son utilisation (énergie, par exemple) [V ESRS 1 (2026) § 71, AR 39] |
| Atelier BRUNESCAU | **Chaîne de valeur amont** | Ni détenu, ni loué, ni exploité par la SA : elle ne peut diriger ses activités opérationnelles (pas de **contrôle opérationnel**) ; c'est une **relation d'affaires** directe, fournisseur d'une prestation [V ESRS 1 (2026) § 62 ; glossaire ESRS 2023 ; F12 § 7 ; S] |
| Papetiers, fabricants d'encres et de vernis | **Chaîne de valeur amont** | Relations d'affaires directes ; impacts sur les forêts, les ressources, les émissions de leur production [V § 62-63] |
| Domaines viticoles | **Chaîne de valeur aval** | Clients : utilisation des étiquettes, fin de vie des supports siliconés (210 tonnes) [V § 62-63] |

**Appréciation du périmètre retenu (0,5 pt)** : le projet est **erroné** sur trois points : il inclut l'atelier dans le champ comme s'il faisait partie des activités propres (ses consommations d'énergie ne doivent pas être agrégées à celles de la SA, mais il doit être traité dans la chaîne de valeur s'il est matériel, ce qui est probable pour la pollution par les vernis à solvants) ; il exclut l'entrepôt loué, qui relève des activités propres ; il exclut toute la chaîne de valeur, alors que les sujets retenus (utilisation des ressources pour le papier, pollution de l'air) portent pour une large part sur les papetiers et l'atelier. La base de préparation doit indiquer ce qui est couvert dans la chaîne de valeur ; les informations peuvent reposer sur des estimations [V ESRS 1 (2026) § 62-65 ; ESRS 2 BP-1 ; F12 § 14].

**Connectivité avec les comptes annuels (1,25 pt)**
- **Principe** : la SA fournit des informations qui permettent de comprendre les connexions entre l'état de durabilité et ses autres documents, dont les états financiers [V ESRS 1 (2026) § 112] ; un montant présent aussi dans les états financiers fait l'objet d'un **renvoi** (connexion directe) ; un montant qui est une somme ou une partie de montants des états financiers est **expliqué** (connexion indirecte) ; les données et hypothèses concordent dans la mesure du possible, les différences significatives étant expliquées ; même monnaie [V § 114-116, AR 50].
- **Presse numérique** : l'investissement de 1 800 000 € correspond à une immobilisation des comptes annuels (matériels industriels) : **connexion directe**, avec renvoi à la note sur les immobilisations ; la durée d'utilisation de dix ans retenue en comptabilité doit concorder avec les hypothèses de réduction des consommations [V § 114, § 116 ; S].
- **Subvention** : 540 000 € figurent dans les capitaux propres (subvention d'investissement), avec une reprise au résultat : renvoi à la note de l'annexe ; la reprise doit suivre la même durée de dix ans, ce qui rejoint l'anomalie 1 [V § 114, § 116 ; S].
- **Augmentation de capital** : 3 000 000 € figurent dans les capitaux propres (250 000 € de capital et 2 750 000 € de prime d'émission, diminuée des frais imputés) ; la part affectée à la décarbonation (1 260 000 € pour la presse, 900 000 € prévus pour la pompe à chaleur) est une **partie** de ce montant : **connexion indirecte**, à expliquer ; la phrase du projet, « financés par la subvention de la Région et par l'augmentation de capital », sans montants ni renvoi, ne suffit pas [V § 115 ; S]. Le projet, qui ne comporte **aucun renvoi** aux comptes annuels, doit être complété.

**Réponses tolérées**
- La notion de contrôle opérationnel tirée des ESRS de 2023 (glossaire), présentée comme critère de rattachement : points complets.
- L'atelier présenté comme élément de la chaîne de valeur « dont les informations peuvent être estimées », sans le mot « relation d'affaires » : points complets.

**Erreurs fréquentes**
- Rattacher l'atelier aux activités propres parce qu'il travaille pour la SA, ou exclure l'entrepôt parce qu'il est loué (`JUR-A01`).
- Définir la connectivité sans l'appliquer aux trois éléments du cas (`JUR-A06`).
- Détailler les exigences d'une norme thématique sur les émissions, qui ne sont pas demandées (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 60-65, § 71, AR 39 ; ESRS 2 BP-1 ; glossaire ESRS 2023 | Activités propres, actifs loués, chaîne de valeur, contrôle opérationnel | [V] ; application : [S] | F12 § 7, § 14, § 16 |
| ESRS 1 (2026) § 112, 114-116, AR 50 | Connexions directes et indirectes ; cohérence des hypothèses | [V] ; application : [S] | F12 § 9 |

### 3.12 Mission, axes, assurance, démarche et procédures (5 pts)

**a. Objectifs, axes et assurance (2 pts)**
- **Objectifs (0,5 pt)** : exprimer un **avis** sur la conformité aux ESRS du **processus** mis en œuvre pour déterminer les informations publiées et sur la conformité des **informations** publiées, dans un rapport destiné à l'assemblée générale [V L. 821-54 II, par analogie ; LD 2026 § 2]. La SA publiant volontairement, la mission est conduite par hypothèse dans les conditions de la certification légale [F12 § 11 (b)] ; elle ne garantit pas la qualité de la gestion [V L. 821-55].
- **Axes applicables (1 pt)** :
  - **axe 1, processus** : le cabinet vérifie que la SA a défini, mis en œuvre et décrit un processus d'identification et d'évaluation des impacts, risques et opportunités, comprenant l'identification des **parties prenantes** (affectées et utilisatrices), la définition de la **matérialité d'impact** (gravité, probabilité) et de la **matérialité financière** (probabilité, ampleur des effets financiers), et les **seuils** retenus [V LD 2026 § 7.1 ; F13 § 8] ;
  - **consultation du CSE** : la loi ne l'impose pas à une entité qui publie volontairement ; elle entre ici dans l'axe 1 parce que l'accord d'entreprise du 14/11/2025 l'impose à la SA et que la lettre de mission étend la vérification à cette consultation ; le cabinet vérifie que le CSE a été consulté sur ces informations, par analogie avec la vérification prévue par les lignes directrices [V LD 2026 § 7.3 ; F12 § 11 (b) ; F13 § 4.5 ; S, fondement contractuel] ;
  - **axe 2, informations** : conformité des informations publiées aux ESRS (base de préparation et périmètre, présentation, informations vérifiées spécifiquement) [V LD 2026 § 8] ;
  - **taxonomie et balisage** : sans objet (aucune information de taxonomie publiée ; aucune règle de balisage applicable) [V LD 2026 § 2, § 10].
- **Assurance limitée (0,5 pt)** : vérifications moindres en **nature**, en **étendue** et en **durée** que pour une assurance raisonnable ; conclusion exprimée sous une **forme négative** (le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes), à la différence de l'opinion positive de la certification des comptes, fondée sur une assurance raisonnable [V LD 2026, « Niveau d'assurance » ; NEP principes § 08 ; F13 § 2.3].

**b. Étapes et procédures (3 pts)**
- **Étapes (1 pt)** : lettre de mission (objet, étendue dont la consultation du CSE, signataire inscrit sur la liste de la durabilité, accès aux documents et aux personnes, déclarations écrites) ; **prise de connaissance** de la SA, de sa chaîne de valeur et de ses processus de production des données ; **planification**, avec la sélection des informations **vérifiées spécifiquement** (risque important de non-conformité, attentes fortes des utilisateurs : le fonds et les négociants ; ici la part du papier certifié) ; **contrôle du processus** (axe 1) ; **contrôle des informations** (axe 2) ; lecture d'ensemble et cohérence avec les comptes annuels, en échange avec l'équipe qui les certifie ; événements postérieurs, déclarations écrites, communication avec la direction ; **rapport** organisé par axe [V LD 2026 § 3-8, § 11-17 ; F13 § 3].
- **Procédures prévues sur le processus d'analyse de double matérialité (1 pt ; 0,25 pt par procédure reliée à son objectif, dans la limite de 1 pt)** :
  - inspection de la description de la démarche dans le projet et de la documentation du consultant (liste des impacts, risques et opportunités, grilles de notation, seuils) — *existence et description fidèle du processus* ;
  - vérification de l'identification des **parties prenantes** (salariés, clients, papetiers, riverains) et des comptes rendus des ateliers et des réponses au questionnaire — *dialogue avec les parties prenantes* ;
  - examen des critères de **gravité** et de **probabilité** des impacts et des critères financiers, et des **seuils** retenus ; contrôle par sondage des notations — *conformité de la méthode aux ESRS* ;
  - vérification de la prise en compte de la **chaîne de valeur** (atelier, papetiers, domaines) et des activités propres (entrepôt loué) — *exhaustivité des impacts, risques et opportunités* ;
  - rapprochement de la liste des sujets matériels avec les informations publiées, et lecture du procès-verbal du directoire du 08/12/2026 — *cohérence entre le processus et les informations* ;
  - inspection du procès-verbal de consultation du CSE du 18/02/2027 — *respect de l'accord d'entreprise et de la lettre de mission*.
- **Procédures sur la part du papier et du carton certifiés (1 pt ; 0,25 pt par procédure reliée à son objectif, dans la limite de 1 pt)** :
  - vérification de la **définition** publiée (papier et carton achetés en 2026, issus de forêts gérées durablement et couverts par un certificat de chaîne de contrôle) — *conformité de la méthode, clarté de l'information* ;
  - **rapprochement** du fichier des réceptions (1 650 tonnes) avec les factures des trois papetiers et contrôle de la séparation des périodes (réceptions de fin décembre) — *exhaustivité et exactitude du dénominateur* ;
  - **inspection des certificats** de chaîne de contrôle et de la mention « certifié » sur les factures, en tenant compte du certificat **expiré le 30/09/2026** : les livraisons de ce papetier postérieures à cette date ne peuvent être comptées comme certifiées — *exactitude du numérateur* ;
  - **connectivité** : rapprochement des quantités et des prix des factures avec les achats de papier et de carton comptabilisés (2 970 000 €) — *cohérence avec les comptes annuels* ;
  - **demande d'information** aux papetiers (chaîne de valeur) sur les quantités certifiées livrées ; **recalcul** du rapport publié et procédure analytique par fournisseur — *exactitude* [V LD 2026 § 8.3.2 ; S, procédures].

**Réponses tolérées**
- En b., les étapes dans l'ordre du programme (prise de connaissance, planification, contrôle de conformité du processus et des informations, contrôle du balisage, contrôle des exigences de publication, rapport), si le candidat signale que le balisage et la taxonomie sont sans objet : points complets.
- En a., une consultation du CSE présentée comme hors du champ légal mais vérifiée en vertu de la lettre de mission, sans le mot « analogie » : points complets.

**Erreurs fréquentes**
- Affirmer que la loi impose à la SA de consulter son CSE (`JUR-A01`).
- Présenter l'assurance limitée comme identique à celle de la certification, ou comme une garantie (`JUR-A01`).
- Proposer des procédures sans lien avec le processus ou la donnée, ou sans objectif (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; NEP principes § 08 | Objet de l'avis ; absence de garantie ; assurance raisonnable | [V] ; application à une mission volontaire : [S] | F13 § 2 ; F12 § 11 |
| LD 2026 § 2-8, § 10-17, « Niveau d'assurance » | Axes ; processus et CSE ; informations vérifiées spécifiquement ; techniques ; étapes | [V] ; procédures : [S] | F13 § 2-3, § 4.5, § 7-8 |

### 3.13 Impossibilité d'émettre un avis sur le processus (2 pts)

**Qualification de la situation (0,75 pt)** : le cabinet n'a pu mettre en œuvre **aucune des vérifications nécessaires** sur le processus : les impacts, risques et opportunités identifiés, les notations, les seuils et les échanges avec les parties prenantes sont perdus et ne peuvent être reconstitués, et aucun autre élément ne permet de vérifier la démarche ; le procès-verbal du directoire ne reproduit pas la matrice. C'est une **limitation** de ses travaux, imposée par les circonstances et non corrigible avant l'arrêté des informations [V LD 2026 § 7, § 12, § 17 ; S, application].

**Avis (0,75 pt)** : la limitation porte sur **l'ensemble du processus**, qui fonde le choix de tous les sujets publiés : ses incidences ne peuvent être **circonscrites** (on ignore si les trois sujets retenus sont les seuls matériels, si la chaîne de valeur a été prise en compte, si les seuils sont pertinents) et une réserve ne permettrait pas à l'utilisateur de fonder son jugement : **impossibilité d'émettre un avis, motivée**, sur l'axe 1 (« nous ne sommes pas en mesure de nous prononcer sur la conformité aux ESRS du processus ») [V LD 2026 § 17 ; F13 § 4.2-4.3]. Le rapport en expose les motifs (perte de la documentation et absence d'autre élément) ; la seule vérification réalisée, la consultation du CSE, peut être décrite dans la nature des travaux sans rendre possible un avis sur le processus [S].

**Comparaison avec une réserve pour limitation (0,5 pt)** : la **réserve** suppose une limitation dont les incidences sont **clairement circonscrites** et qu'une réserve motivée suffit à exposer : par exemple, la perte des seules réponses au questionnaire, les grilles et les seuils restant vérifiables, ou la perte de la notation d'un seul sujet ; l'avis resterait un avis de conformité, assorti de cette réserve [V LD 2026 § 17 ; F13 § 4.2-4.4]. Ici, l'étendue de la limitation exclut la réserve. Une **observation** ne conviendrait pas non plus : elle ne s'emploie qu'avec un avis de conformité et ne remplace pas des vérifications impossibles [V F13 § 4.4].

**Réponses tolérées**
- La mention que le cabinet devra apprécier l'incidence de cette limitation sur son avis relatif aux informations publiées, dont l'exhaustivité dépend de l'analyse : sans points supplémentaires (l'avis sur les informations n'est pas demandé).
- Une réserve pour limitation retenue en circonscrivant la limitation à la description de la démarche, avec la table de décision : 0,75 pt sur 2.

**Erreurs fréquentes**
- Formuler un avis de non-conformité, qui sanctionne une erreur relevée et non une impossibilité de vérifier (`JUR-A02`).
- Formuler une réserve sans examiner si les incidences sont circonscrites (`JUR-A02`).
- Confondre avis exprimé sous forme négative et opinion sur les comptes (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 7, § 12, § 17 | Vérification du processus ; éléments suffisants et appropriés ; avis par axe, réserve, impossibilité | [V] ; qualification : [S] | F13 § 4.2-4.4, § 8 |
