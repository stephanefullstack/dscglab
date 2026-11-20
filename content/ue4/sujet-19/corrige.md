# ÉLÉMENTS INDICATIFS DE CORRIGÉ ET DE BARÈME

## UE 4 – Comptabilité et audit — Sujet d'entraînement complet n° 19

Le sujet et son corrigé ont été construits sur la base d'une réglementation au 31/12/2026.

Textes intégrés (fiches datées) : F01 à F05 et F09 à F14 (`ue4/fiches/`, à jour entre le 22/10 et le 20/11/2026). Données structurées et écritures : `corrige.yaml`, vérifié par `outils/ue4check` (périmètre, goodwill, fusion, impôts différés, partage, écritures, barème 45/25/30, liste noire, hors-programme).

Bien que le corrigé mentionne des textes juridiques et normatifs, il n'est pas attendu des candidats qu'ils en citent précisément les références. L'évaluation porte avant tout sur la pertinence et la cohérence des réponses.

| Dossier | Points | Questions | Exercice d'origine |
|---|---:|---|---|
| 1 – Comptes de groupe | 45 | 1.1 à 1.9 | `exercices/ex52_consolidation_ifrs_coentreprise_hausse_prix_couts_emprunt_flux` |
| 2 – Opérations de restructuration | 25 | 2.1 à 2.8 | `exercices/ex53_scission_apport_envers_soulte` |
| 3 – Audit (dont durabilité : 12 pts) | 30 | 3.1 à 3.12 | `exercices/ex54_audit_paie_securite_privee_gri_issb` |
| **Total** | **100** | | |

---

## DOSSIER 1 – COMPTES DE GROUPE (45 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 1.1 a Obligation de consolider et IFRS obligatoires | `2.1.b` Contexte réglementaire et légal de la consolidation | 1,5 |
| 1.1 b IASB, IFRS Interpretations Committee, EFRAG ; adoption dans l'Union | `2.1.a` Normalisateurs internationaux et leurs rôles | 3 |
| 1.2 a Tableau du périmètre ; VALOTHÈSE hors périmètre | `2.1.c` Périmètre de consolidation | 1,5 |
| 1.2 b MOUSSÉLIA : contrôle conjoint, coentreprise, mise en équivalence | `2.1.c` Périmètre ; nature du contrôle | 1,5 |
| 1.2 c MOUSSÉLIA en règlement ANC : intégration proportionnelle | `2.1.d` Méthodes et information financière | 1,5 |
| 1.3 a Provision pour hausse des prix : motif et tableau d'incidence | `2.2.b` Retraitements préparatoires (écritures fiscales) | 2 |
| 1.3 b Provision pour hausse des prix : écritures | `2.2.b` Retraitements préparatoires (écritures fiscales) | 2 |
| 1.4 a Coûts d'emprunt : IAS 23, montants, amortissement | `2.2.c` Homogénéisation, thèmes communs (coûts d'emprunt) | 2 |
| 1.4 b Coûts d'emprunt : tableau d'incidence, impôt différé | `2.2.c` Homogénéisation, thèmes communs (coûts d'emprunt) | 1,5 |
| 1.4 c Coûts d'emprunt : écritures | `2.2.c` Homogénéisation, thèmes communs (coûts d'emprunt) | 1,5 |
| 1.5 a Machine cédée en interne : incidence | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.5 b Machine cédée en interne : écritures | `2.2.f` Comptes réciproques et résultats internes | 1 |
| 1.5 c Dividende interne, prestations et soldes réciproques | `2.2.f` Comptes réciproques et résultats internes | 1,5 |
| 1.6 a Contrepartie transférée ; honoraires et frais d'émission | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.6 b Actif net identifiable, goodwill partiel, PNC, résultat retraité | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.6 c Écritures du coût des titres et de l'écart d'évaluation | `2.2.g` Écarts d'évaluation et goodwill | 2 |
| 1.7 a Tableaux de partage de CORDELANE Tricotage et de PODALIS | `2.2.h` Partage des capitaux propres | 2,5 |
| 1.7 b Mise en équivalence de MOUSSÉLIA | `2.2.h` Partage des capitaux propres (mise en équivalence) | 1,5 |
| 1.7 c Écritures d'élimination des titres, de partage et de mise en équivalence | `2.2.h` Partage des capitaux propres | 2 |
| 1.7 d Capitaux propres consolidés | `2.2.h` Partage des capitaux propres | 2 |
| 1.8 Phases du processus de consolidation | `2.2.a` Processus d'élaboration d'une consolidation | 2 |
| 1.9 a Extrait du tableau des flux de trésorerie (investissement, financement) | `2.3.a` Documents de synthèse consolidés | 5 |
| 1.9 b Coentreprise dans le tableau des flux ; intégration proportionnelle | `2.3.a` Documents de synthèse ; `2.1.d` Méthodes | 2 |
| **Total** | | **45** |

Comptes de consolidation utilisés dans les écritures : `RSV` / `RST` = réserves / résultat de l'entité avant partage ; `RSV_G` / `RST_G` = réserves / résultat consolidés, part du groupe ; `RSV_M` / `RST_M` = participations ne donnant pas le contrôle (PNC) ; `CAP_ELIM` = capital de la filiale éliminé ; `EA` = goodwill ; `TME` = titres mis en équivalence ; `QP_MEE` = quote-part du résultat net des entités mises en équivalence ; `IDA` / `IDP` = impôt différé actif / passif ; `CH_ID` = charge ou produit d'impôt différé ; `RES_CR` = contrepartie au compte de résultat de l'écriture de bilan. Un suffixe désigne la société concernée (`RST.TRICOTAGE`, `261.CORDELANE` : titres détenus par CORDELANE).

---

### 1.1 Référentiel et normalisateurs (4,5 pts)

#### a. Obligation de consolider et référentiel (1,5 pt)

**Obligation (0,5 pt).** CORDELANE, société commerciale, contrôle de manière exclusive CORDELANE Tricotage (100 %) et PODALIS (75 %), et de manière conjointe MOUSSÉLIA (question 1.2) : elle établit et publie des comptes consolidés [V C. com. L. 233-16 ; F03 § 1.1]. Aucune exemption ne joue : CORDELANE n'est contrôlée par aucune société, et l'exemption des ensembles qui ne forment pas un grand groupe est refusée aux sociétés dont les titres sont admis sur un marché réglementé [V L. 233-17 ; L. 123-16-2 ; F03 § 1.1] ; le groupe dépasse d'ailleurs largement les seuils (238 M€ de chiffre d'affaires, 1 640 salariés).

**IFRS obligatoires (0,5 pt).** Les actions de CORDELANE sont admises aux négociations sur Euronext Paris, marché réglementé : depuis les exercices ouverts en 2005, ses comptes consolidés doivent être établis selon les normes comptables internationales **adoptées par l'Union européenne** [V règlement (CE) n° 1606/2002, art. 4 ; F03 § 1.2, § 15]. Le règlement ANC n° 2020-01 ne lui est pas ouvert : il ne s'applique qu'aux sociétés dont aucun titre n'est admis sur un marché réglementé, lesquelles peuvent d'ailleurs opter pour les IFRS [V L. 233-24 ; F03 § 1.2].

**Comptes individuels (0,5 pt).** L'obligation ne vise que les comptes consolidés. Les comptes individuels de CORDELANE et de ses filiales restent établis selon le plan comptable général (hypothèses générales), qui sert aussi de base à leur résultat imposable. Chaque liasse est donc retraitée pour la consolidation (provision pour hausse des prix, coûts d'emprunt, honoraires d'acquisition…), et chaque retraitement qui écarte la valeur consolidée de la base fiscale crée un impôt différé.

**Réponses tolérées** : référence au « règlement IAS » sans numéro ; justification de l'obligation de consolider par le seul contrôle des filiales, sans examen des exemptions (0,25 pt perdu au plus).

**Erreurs fréquentes** : IFRS présentées comme un choix de CORDELANE ; IFRS présentées comme applicables aux comptes individuels ; IFRS 18 appliquée à 2026 ; normes « publiées par l'IASB » présentées comme directement applicables, sans adoption (`JUR-F07`).

#### b. Normalisateurs et adoption des normes (3 pts)

**IASB (0,5 pt).** Groupe indépendant d'experts, au sein de l'IFRS Foundation, organisme sans but lucratif dont les administrateurs (Trustees) veillent au respect de la procédure d'élaboration ; ses membres élaborent et publient les normes IFRS et approuvent les interprétations [V page « International Accounting Standards Board », ifrs.org ; F03 § 7.2]. Sa procédure est publique : programme de travail arrêté après consultation, document de discussion soumis à commentaires, **exposé-sondage** soumis à consultation publique, analyse des commentaires, publication de la norme, revue après quelques années d'application [V page « How we set IFRS Standards », ifrs.org ; F03 § 15].

**IFRS Interpretations Committee, anciennement IFRIC (0,5 pt).** Il travaille avec l'IASB au maintien et à l'application cohérente des normes : il répond aux questions d'application qui lui sont soumises et peut élaborer une **interprétation IFRIC** ou recommander une modification de portée limitée d'une norme ; ses 14 membres votants sont nommés par les administrateurs de l'IFRS Foundation ; l'interprétation est approuvée par l'IASB [V pages « IFRS Interpretations Committee » et « How we set IFRS Standards », ifrs.org ; F03 § 7.2, § 15].

**EFRAG (0,5 pt).** Organisme européen qui veille à ce que les positions européennes soient prises en compte dans les travaux de l'IASB et qui **conseille la Commission européenne** sur la conformité de chaque norme nouvelle ou modifiée aux critères du règlement IAS, y compris l'intérêt public européen [V page « Financial reporting », efrag.org ; F03 § 7.2, § 15] ; le règlement prévoit qu'un comité technique comptable apporte ainsi ses compétences à la Commission [V règlement (CE) n° 1606/2002, considérant 10].

**Procédure d'adoption (1 pt).** Une norme publiée par l'IASB ne s'applique pas d'elle-même dans l'Union :
- la **Commission européenne** décide de son applicabilité, assistée d'un **comité de réglementation comptable** [V art. 3, 1 et art. 6, 1 ; F03 § 15] (0,25 pt) ;
- elle ne peut l'adopter que si la norme n'est pas contraire au principe d'image fidèle, répond à l'**intérêt public européen** et satisfait aux critères d'intelligibilité, de pertinence, de fiabilité et de comparabilité [V art. 3, 2] ; l'avis de l'EFRAG porte sur ces critères (0,25 pt) ;
- la norme adoptée est publiée intégralement, dans toutes les langues officielles, sous la forme d'un **règlement de la Commission** au Journal officiel, directement applicable en France ; elle s'impose alors aux comptes consolidés des sociétés cotées sur un marché réglementé à la date d'application qu'elle prévoit [V art. 3, 4 et art. 4] (0,25 pt) ;
- la même procédure vaut pour les **interprétations**, que le règlement range parmi les « normes comptables internationales » [V art. 2] (0,25 pt).

**Réponse à l'administrateur (0,5 pt).**
- La nouvelle norme ne s'appliquera aux comptes consolidés de CORDELANE qu'après son adoption par un règlement de la Commission, à la date d'application qu'elle fixe ; avant, le groupe ne peut l'appliquer par anticipation que si elle a été adoptée et si elle le permet (c'est ce que fait le groupe pour IFRS 18, adoptée mais obligatoire seulement pour les exercices ouverts à compter du 01/01/2027, l'application anticipée étant permise, qu'il n'anticipe pas : F14 § 0). L'interprétation en préparation n'est encore qu'un projet : elle ne s'imposera, elle aussi, qu'une fois approuvée par l'IASB puis adoptée par l'Union.
- Le groupe peut faire entendre sa voix : répondre aux consultations publiques de l'IASB (document de discussion, exposé-sondage) ou de l'IFRS Interpretations Committee, soumettre à ce dernier une question d'application, et faire valoir sa position auprès de l'EFRAG, qui la porte dans les débats avec l'IASB et dans son avis à la Commission [V F03 § 7.2, § 15 ; application, S].

**Réponses tolérées** : mention de l'ARC (Accounting Regulatory Committee) pour le comité de réglementation comptable ; mention du contrôle du Parlement européen et du Conseil sur le projet de règlement (non exigée, non pénalisée) ; IFRS Interpretations Committee appelé « IFRIC ».

**Erreurs fréquentes** : EFRAG présenté comme l'auteur des normes ou comme l'organe qui les adopte ; interprétation présentée comme applicable dès sa publication ; confusion entre l'IASB et l'IFRS Foundation ; ANC présentée comme l'autorité qui adopte les IFRS en France ; réponse générale sans application aux deux textes cités par l'administrateur (`JUR-F07`).

**Références normatives (1.1)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 233-16, L. 233-17, L. 123-16-2 | Obligation de consolider, exemptions et leurs exclusions | [V] | F03 § 1.1 |
| Règlement (CE) n° 1606/2002, considérant 10, art. 2, 3, 4, 6 | Champ (normes et interprétations), procédure et critères d'adoption, obligation des sociétés cotées | [V] | F03 § 1.2, § 15 |
| Pages ifrs.org (IASB ; IFRS Interpretations Committee ; « How we set IFRS Standards ») et efrag.org (« Financial reporting ») | Rôles et procédures des normalisateurs | [V] | F03 § 7.2, § 15 |
| Règlement (UE) 2026/338 ; IFRS 18 § C1 | Date d'application d'IFRS 18 | [V] | F14 § 0 |

---

### 1.2 Périmètre et méthodes (4,5 pts)

#### a. Tableau du périmètre (1,5 pt)

| Société | % de contrôle | Nature du contrôle | Méthode | % d'intérêt du groupe | % des PNC |
|---|---:|---|---|---:|---:|
| CORDELANE Tricotage | 100 % | Exclusif | Intégration globale | 100 % | 0 % |
| PODALIS | 75 % | Exclusif | Intégration globale | 75 % | 25 % |
| MOUSSÉLIA | 50 % | Conjoint (coentreprise) | Mise en équivalence | 50 % | – |
| VALOTHÈSE Distribution | 12 % | Aucun (ni contrôle, ni influence notable) | Hors périmètre | – | – |

(1 pt pour le tableau : 0,25 pt par ligne.)

Toutes les participations sont directes : pourcentages de contrôle et d'intérêt sont égaux [V F03 § 4.1]. CORDELANE contrôle PODALIS par la majorité des droits de vote, et elle en nomme le président ; M. FERNOUX n'a aucun droit particulier [V IFRS 10 § 7 ; F03 § 2].

**VALOTHÈSE (0,5 pt).** Avec 12 % des droits de vote, l'investisseur est présumé ne pas exercer d'influence notable, sauf à la démontrer clairement [V IAS 28 § 5 ; F03 § 2] : CORDELANE n'est représentée dans aucun organe et ses ventes à VALOTHÈSE sont des opérations courantes, aux conditions du marché, sans dépendance [V IAS 28 § 6]. La participation reste hors du périmètre ; elle figure à l'actif consolidé parmi les actifs financiers, selon IFRS 9 (annexe 1.1).

#### b. MOUSSÉLIA : nature du contrôle, qualification, méthode (1,5 pt)

**Contrôle conjoint (0,5 pt).** Le pacte d'associés impose l'**unanimité** de CORDELANE et d'ALCÉMOUSSE pour les décisions sur les activités pertinentes (budget, investissements, financement, gamme, président) : le contrôle est partagé contractuellement, aucun associé ne peut décider seul [V IFRS 11 § 7 ; F03 § 2]. Le pourcentage de 50 % ne suffit pas, à lui seul, à le démontrer.

**Coentreprise (0,5 pt).** Un partenariat est soit une activité conjointe, soit une coentreprise, selon les droits et obligations des parties [V IFRS 11 § 14] : MOUSSÉLIA est une société distincte, propriétaire de ses actifs, qui contracte seule ses emprunts sans garantie des associés et vend sa production à des tiers ; les associés n'ont de droits que sur son **actif net** : c'est une **coentreprise** [V IFRS 11 § 16 ; F03 § 2].

**Mise en équivalence (0,5 pt).** Le coentrepreneur comptabilise sa participation selon la méthode de la mise en équivalence [V IFRS 11 § 24 ; F03 § 3] : les titres sont remplacés par la quote-part des capitaux propres de MOUSSÉLIA, augmentée de la quote-part de son résultat et diminuée des distributions reçues [V IAS 28 § 10 ; F03 § 15]. L'intégration proportionnelle n'existe pas en IFRS pour une coentreprise [V F03 § 3].

#### c. MOUSSÉLIA en règlement ANC (1,5 pt)

**Méthode (0,5 pt).** Le règlement ANC n° 2020-01 impose l'**intégration proportionnelle** des entités sous contrôle conjoint : 50 % de chaque actif, passif, produit et charge de MOUSSÉLIA seraient cumulés ligne à ligne avec ceux du groupe, sans intérêts minoritaires [V art. 221-1, 221-3 ; F03 § 3].

**Lecture des comptes (1 pt).**
- **Chiffre d'affaires** : il comprendrait 50 % des ventes de MOUSSÉLIA ; en IFRS, il n'en comprend rien (0,25 pt).
- **Endettement et actifs** : 50 % des emprunts bancaires de MOUSSÉLIA, de son usine et de ses stocks figureraient dans les comptes du groupe ; en IFRS, ils sont absents, et l'endettement du groupe paraît plus faible (0,25 pt).
- **Présentation** : en IFRS, MOUSSÉLIA n'apparaît que sur deux lignes, la participation mise en équivalence à l'actif (2 680 000 €) et la quote-part de résultat au compte de résultat (480 000 €) ; en règlement ANC, elle se fondrait dans tous les postes (0,25 pt).
- **Résultat net et capitaux propres attribuables au groupe** : **identiques** dans les deux méthodes (quote-part de 50 % dans les deux cas) ; seuls les agrégats et les ratios (marge, endettement, rentabilité des actifs) diffèrent, ce qui gêne la comparaison avec un groupe établissant ses comptes selon le règlement ANC (0,25 pt).

**Réponses tolérées (1.2)** : pourcentage des PNC de MOUSSÉLIA noté 0 % ou « sans objet » ; VALOTHÈSE présentée comme « participation non consolidée évaluée selon IFRS 9 » sans référence à IAS 28, si l'absence d'influence notable est justifiée.

**Erreurs fréquentes (1.2)** : contrôle conjoint déduit du seul pourcentage de 50 %, sans l'unanimité (`JUR-F07`) ; MOUSSÉLIA intégrée proportionnellement en IFRS ou qualifiée d'activité conjointe ; MOUSSÉLIA qualifiée d'entreprise associée ; VALOTHÈSE mise en équivalence ; résultat consolidé présenté comme différent selon la méthode.

**Références normatives (1.2)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 7 | Contrôle | [V] | F03 § 2 |
| IFRS 11 § 7, 14, 16, 24 | Contrôle conjoint, coentreprise, mise en équivalence | [V] | F03 § 2, § 3 |
| IAS 28 § 5, 6, 10 | Présomption d'influence notable, indices ; méthode de la mise en équivalence | [V] | F03 § 2, § 15 |
| ANC 2020-01 art. 221-1, 221-3 | Intégration proportionnelle | [V] | F03 § 3 |

---

### 1.3 Provision pour hausse des prix de CORDELANE Tricotage (4 pts)

#### a. Motif de l'élimination et tableau d'incidence (2 pts)

**Motif (0,75 pt).** La provision pour hausse des prix est une **provision réglementée** (compte 143), constituée en application de la législation fiscale pour différer l'imposition d'une partie du résultat ; elle ne correspond ni à une dépréciation des stocks, évalués à leur coût, ni à une obligation envers un tiers [V F04 R1]. En IFRS, aucune norme ne prévoit de provisions réglementées : une provision suppose une obligation actuelle résultant d'un événement passé [V IAS 37 § 14 ; F04 R1]. Écriture passée pour la seule application de la législation fiscale, elle est **éliminée** des comptes consolidés : son solde d'ouverture en réserves, la dotation de 2026 en résultat. C'est un retraitement préparatoire ; le programme ne l'envisage que dans le cadre d'une intégration globale (2.2.b).

**Tableau d'incidence au 31/12/2026 (1 pt)**

| | Ouverture (réserves) | Exercice 2026 (résultat) | Clôture (bilan) |
|---|---:|---:|---:|
| Provision éliminée (avant impôt) | + 96 000 | + 64 000 | 160 000 |
| Impôt différé passif (25 %) | – 24 000 | – 16 000 | 40 000 |
| **Incidence nette** | **+ 72 000** | **+ 48 000** | **+ 120 000** |

(0,25 pt par ligne de l'ouverture et de l'exercice, 0,25 pt pour la clôture, 0,25 pt pour l'incidence nette.)

**Impôt différé passif (0,25 pt).** Les dotations ont été déduites fiscalement et leur reprise sera imposée : l'élimination augmente les capitaux propres consolidés d'un montant qui sera imposé plus tard ; il s'agit d'une différence temporelle imposable, qui donne un passif d'impôt différé de 25 % du solde de la provision [V F04 R1 ; IAS 12 § 15].

#### b. Écritures au 31/12/2026 (2 pts)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| **C1 – Bilan** | | | |
| 143 | Provisions réglementées pour hausse de prix | 160 000 | |
| IDP | Impôt différé passif | | 40 000 |
| RSV.TRICOTAGE | Réserves CORDELANE Tricotage | | 72 000 |
| RST.TRICOTAGE | Résultat CORDELANE Tricotage | | 48 000 |
| **C1R – Compte de résultat** | | | |
| CH_ID | Charge d'impôt différé | 16 000 | |
| RES_CR | Résultat | 48 000 | |
| 6873 | Dotations aux provisions réglementées (stocks) | | 64 000 |

(1 pt par écriture.)

**Réponses tolérées (1.3)** : écriture unique au bilan avec un compte « résultat » ; impôt différé présenté globalement sur le solde de clôture avec la décomposition réserves / résultat.

**Erreurs fréquentes (1.3)** : dotation de 2026 éliminée au crédit des réserves, ou cumul porté en totalité au résultat ; impôt différé actif au lieu de passif ; impôt différé oublié ; provision traitée comme une dépréciation des stocks à maintenir ; débit du compte 7873 alors qu'aucune reprise n'a eu lieu (`JUR-G06`, `JUR-F04`, `JUR-F05`).

**Références normatives (1.3)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 37 § 14 ; ANC 2020-01 art. 272-1 (pour comparaison) | Absence d'obligation ; élimination des écritures fiscales | [V] | F04 R1 |
| IAS 12 § 15 | Différence temporelle imposable | [V] | F04 R1 |
| PCG, comptes 143, 6873 | Provision réglementée pour hausse de prix, dotation | [V] | liste des comptes du PCG |

---

### 1.4 Coûts d'emprunt de la plateforme logistique (5 pts)

#### a. Traitement IAS 23 et montants (2 pts)

**Principe (0,5 pt).** Les coûts d'emprunt directement attribuables à la construction d'un **actif qualifié** sont **obligatoirement** incorporés à son coût [V IAS 23 § 8 ; F04 R6] ; il n'y a pas d'option, contrairement au plan comptable général, où CORDELANE les a passés en charges. La plateforme exige une longue période de construction (dix-sept mois) avant de pouvoir être utilisée : c'est un actif qualifié [V IAS 23 § 5, 7] (0,25 pt pour l'obligation et la qualification). Pour un **emprunt spécifique**, le montant incorporé est le coût réel de l'emprunt pendant la période, **diminué des produits du placement temporaire** des fonds empruntés [V IAS 23 § 12 ; F04 R6] (0,25 pt pour l'emprunt spécifique).

**Période d'incorporation (0,25 pt).** Du 01/04/2025, date à laquelle les dépenses, les coûts d'emprunt et les travaux ont commencé [V IAS 23 § 17], au 31/08/2026, les travaux s'étant poursuivis sans interruption jusqu'à la mise en service du 01/09/2026, date à laquelle la plateforme est prête à être utilisée [V § 22] : 9 mois en 2025, 8 mois en 2026.

**Montants (1 pt)**

| | 2025 | 2026 |
|---|---:|---:|
| Intérêts de la période de construction | 6 000 000 × 3,6 % × 9/12 = 162 000 | 6 000 000 × 3,6 % × 8/12 = 144 000 |
| Produits du placement temporaire | – 12 000 | – |
| **Coûts d'emprunt incorporés** | **150 000** | **144 000** |

Total incorporé : 294 000 € ; coût de la plateforme dans les comptes consolidés : 9 000 000 + 294 000 = 9 294 000 € (0,25 pt par montant annuel, 0,25 pt pour le total). Les intérêts de septembre à décembre 2026, 216 000 – 144 000 = **72 000 €**, restent en charges : la plateforme est en service (0,25 pt).

**Amortissement complémentaire de 2026** (0,25 pt) : 294 000 / 25 × 4/12 = **3 920 €** (dotation des comptes individuels : 9 000 000 / 25 × 4/12 = 120 000 € ; dotation consolidée : 123 920 €).

#### b. Tableau d'incidence et impôt différé (1,5 pt)

| | Réserves (2025) | Résultat 2026 | Clôture |
|---|---:|---:|---:|
| Coûts d'emprunt incorporés | + 150 000 | + 144 000 | 294 000 |
| Amortissement complémentaire | – | – 3 920 | – 3 920 |
| **Avant impôt** | **+ 150 000** | **+ 140 080** | **290 080** |
| Impôt différé passif (25 %) | – 37 500 | – 35 020 | 72 520 |
| **Incidence nette** | **+ 112 500** | **+ 105 060** | **+ 217 560** |

(1 pt pour le tableau.)

**Impôt différé (0,5 pt).** Les intérêts ont été déduits fiscalement à mesure qu'ils couraient, et les produits du placement imposés en 2025 : la base fiscale de la plateforme est sa valeur nette dans les comptes individuels (8 880 000 €), inférieure à sa valeur consolidée (9 170 080 €). La différence de 290 080 € sera imposée au rythme de l'amortissement : différence temporelle imposable, **passif** d'impôt différé de 72 520 € [V IAS 12 § 15 ; F04 R6].

#### c. Écritures au 31/12/2026 (1,5 pt)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| **C2 – Bilan** | | | |
| 2131 | Bâtiments (coûts d'emprunt incorporés à la plateforme) | 294 000 | |
| 28131 | Amortissements des bâtiments | | 3 920 |
| IDP | Impôt différé passif | | 72 520 |
| RSV.CORDELANE | Réserves CORDELANE | | 112 500 |
| RST.CORDELANE | Résultat CORDELANE | | 105 060 |
| **C2R – Compte de résultat** | | | |
| 6811 | Dotations aux amortissements sur immobilisations incorporelles et corporelles | 3 920 | |
| CH_ID | Charge d'impôt différé | 35 020 | |
| RES_CR | Résultat | 105 060 | |
| 6611 | Intérêts des emprunts et dettes (part de 2026 incorporée) | | 144 000 |

(1 pt pour C2, 0,5 pt pour C2R.)

**Réponses tolérées (1.4)** : produits du placement imputés en déduction des intérêts dans une écriture distincte ; présentation de l'incorporation de 2026 par le crédit d'un compte 722 « Production immobilisée » (avec une justification), si l'incidence sur le résultat est la même.

**Erreurs fréquentes (1.4)** : incorporation présentée comme une option ; intérêts de toute l'année 2026 incorporés (216 000 €) ; produits du placement ignorés ; intérêts de 2025 portés au résultat de 2026 ; amortissement complémentaire calculé sur 12 mois ; impôt différé actif (`JUR-G06`, `JUR-F05`, `JUR-F07`).

**Références normatives (1.4)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 23 § 5, 7, 8, 12, 17, 22 | Actif qualifié ; incorporation obligatoire ; emprunt spécifique et produits de placement ; début et fin de l'incorporation | [V] | F04 R6 |
| IAS 12 § 15 | Différence temporelle imposable | [V] | F04 R6 |

---

### 1.5 Opérations internes (4 pts)

#### a. Machine à tricoter : incidence de l'élimination (1,5 pt)

**Analyse (0,5 pt).** Le 01/07/2025, la machine avait chez CORDELANE une valeur nette de 960 000 – 960 000 / 8 × 4 = 480 000 € ; cédée 600 000 €, elle a dégagé une **plus-value interne de 120 000 €**, comprise depuis dans la valeur de la machine chez CORDELANE Tricotage. Pour le groupe, la machine n'a pas changé de mains : elle reste à son coût d'origine, amortie sur le plan initial (120 000 € par an), alors que CORDELANE Tricotage l'amortit 600 000 / 4 = 150 000 € par an. L'élimination porte sur la plus-value restante, et l'**excédent d'amortissement** (30 000 € par an) la réduit progressivement [V F04 R14 ; annexe 1.2, point 3]. Elle est imputée à **CORDELANE**, société qui a réalisé la plus-value (l'acquéreuse, CORDELANE Tricotage, étant détenue à 100 %, ce choix est sans effet sur les montants).

**Incidence au 31/12/2026 (1 pt)**

| | Ouverture (réserves) | Exercice 2026 (résultat) | Clôture (bilan) |
|---|---:|---:|---:|
| Plus-value éliminée | – 120 000 | – | – 120 000 |
| Excédent d'amortissement annulé (2025 : 30 000 × 6/12) | + 15 000 | + 30 000 | + 45 000 |
| **Avant impôt** | **– 105 000** | **+ 30 000** | **– 75 000** |
| Impôt différé actif (25 %) | + 26 250 | – 7 500 | 18 750 |
| **Incidence nette** | **– 78 750** | **+ 22 500** | **– 56 250** |

Contrôle : valeur nette chez CORDELANE Tricotage 600 000 – 150 000 × 18/12 = 375 000 € ; pour le groupe 960 000 – 120 000 × 66/12 = 300 000 € ; écart 75 000 €. La base fiscale (375 000 €) dépasse la valeur consolidée : différence temporelle déductible, **actif** d'impôt différé [V F04 R14 ; IAS 12].

#### b. Écritures relatives à la machine (1 pt)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| **C3 – Bilan** | | | |
| RSV.CORDELANE | Réserves CORDELANE | 78 750 | |
| IDA | Impôt différé actif | 18 750 | |
| 28154 | Amortissements des matériels industriels (15 000 + 30 000) | 45 000 | |
| 2154 | Matériels industriels (600 000 – 480 000) | | 120 000 |
| RST.CORDELANE | Résultat CORDELANE | | 22 500 |
| **C3R – Compte de résultat** | | | |
| CH_ID | Charge d'impôt différé | 7 500 | |
| RES_CR | Résultat | 22 500 | |
| 6811 | Dotations aux amortissements (150 000 – 120 000) | | 30 000 |

(0,5 pt par écriture.)

#### c. Dividende interne, prestations et soldes réciproques (1,5 pt)

**Dividende (0,75 pt).** Le dividende de 900 000 € versé par CORDELANE Tricotage à CORDELANE est un transfert interne de résultats déjà compris dans les réserves consolidées : il est éliminé en totalité du résultat de CORDELANE et rendu aux réserves [V F04 R14 ; IFRS 10 B86 c)].

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| **C4 – Bilan** | | | |
| RST.CORDELANE | Résultat CORDELANE | 900 000 | |
| RSV.CORDELANE | Réserves CORDELANE | | 900 000 |
| **C4R – Compte de résultat** | | | |
| 7611 | Revenus des titres de participation | 900 000 | |
| RES_CR | Résultat | | 900 000 |

**Prestations et soldes réciproques (0,75 pt).** Les prestations facturées par CORDELANE à ses deux filiales intégrées et les soldes correspondants, concordants, sont éliminés en totalité, sans incidence sur le résultat : le produit de l'une est la charge de l'autre [V F04 R14 ; IFRS 10 B86 c)].

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| **C5 – Bilan** | | | |
| 401 | Fournisseurs (CORDELANE Tricotage 70 000 ; PODALIS 30 000) | 100 000 | |
| 411 | Clients (CORDELANE) | | 100 000 |
| **C5R – Compte de résultat** | | | |
| 706 | Prestations de services (CORDELANE : 420 000 + 180 000) | 600 000 | |
| 628 | Divers (CORDELANE Tricotage 420 000 ; PODALIS 180 000) | | 600 000 |

Aucune élimination ne concerne MOUSSÉLIA ni VALOTHÈSE : aucune opération n'a été réalisée avec MOUSSÉLIA en dehors du dividende, traité avec la mise en équivalence (question 1.7), et VALOTHÈSE est hors périmètre ; ses ventes au groupe sont des opérations avec un tiers.

**Réponses tolérées (1.5)** : machine rétablie à son coût d'origine (débit 2154 360 000 € ; crédit 28154 435 000 €, soit 660 000 € d'amortissements du plan d'origine – 225 000 € chez CORDELANE Tricotage) avec la même incidence nette ; écritures de prestations sans distinction bilan / compte de résultat si les deux éliminations figurent.

**Erreurs fréquentes (1.5)** : plus-value éliminée en résultat de 2026 ; excédent d'amortissement de 2025 calculé sur douze mois ; impôt différé passif ; élimination imputée à CORDELANE Tricotage avec un effet présenté sur des minoritaires inexistants ; dividende éliminé sans contrepartie en réserves ; élimination du solde du prix de la machine, réglé le 15/01/2026 et absent des bilans au 31/12/2026 (`JUR-G01`, `JUR-F04`, `JUR-F07`).

**Références normatives (1.5)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 B86 c) | Élimination des actifs, passifs, produits, charges et flux intragroupe, et des profits internes | [V] | F04 R14 |
| ANC 2020-01 art. 251-1, 251-2 (pour comparaison) | Comptes réciproques ; plus-values internes, dividendes, impôt | [V] | F04 R14 |

---

### 1.6 Acquisition de PODALIS (6 pts)

#### a. Contrepartie transférée ; honoraires et frais d'émission (2 pts)

**Contrepartie transférée (1 pt).** Elle est évaluée à la **juste valeur à la date d'acquisition** : somme des actifs transférés et des **parts de capitaux propres émises** par l'acquéreur [V IFRS 3 § 37 ; F05 § 12]. Les actions CORDELANE remises sont cotées : leur juste valeur est le cours de bourse de la date d'acquisition, 26 €, et non la valeur d'échange fixée en octobre 2025 (24 €), qui reflète les cours d'avant la signature (0,5 pt).

| Élément | Montant |
|---|---:|
| Numéraire versé le 01/01/2026 | 4 200 000 |
| 100 000 actions CORDELANE × 26 € | 2 600 000 |
| **Contrepartie transférée** | **6 800 000** |

(0,25 pt.) Dans les comptes individuels, les titres sont inscrits pour 6 780 000 € : 4 200 000 + 2 400 000 + 180 000 € d'honoraires. Les comptes consolidés en retirent les honoraires (– 180 000 €) et portent les actions remises à leur juste valeur (+ 200 000 €, en contrepartie de la prime d'émission) : 6 780 000 – 180 000 + 200 000 = 6 800 000 € (0,25 pt).

**Honoraires (0,5 pt).** Les frais connexes à l'acquisition (avocats, banque d'affaires, audit d'acquisition) sont des **charges** de 2026 [V IFRS 3 § 53 ; annexe 1.2, point 4] : le résultat consolidé de 2026 diminue de 180 000 €, sans impôt différé (hypothèse de l'énoncé), et le goodwill ne les comprend pas.

**Frais d'émission (0,5 pt).** Les coûts marginaux directement attribuables à l'émission des actions nouvelles (frais juridiques, frais d'admission) sont portés **en déduction des capitaux propres**, l'impôt correspondant suivant IAS 12 [V IAS 32 § 35, 35A, 37 ; F05 § 12] : CORDELANE les a déjà imputés sur la prime d'émission pour leur montant net d'impôt (36 000 €), comme le permet le plan comptable général [V F01 § 7] ; **aucun retraitement**. Ils ne se traitent pas comme les honoraires parce qu'ils sont le coût d'une opération avec les actionnaires, qui augmente les capitaux propres (l'émission d'actions), alors que les honoraires rémunèrent des services rendus pour l'acquisition, sans actif ni capitaux propres en contrepartie : IFRS 3 § 53 exclut expressément des charges les frais d'émission de titres, régis par IAS 32 [V IFRS 3 § 53 ; F05 § 2, § 12].

#### b. Actif net identifiable, goodwill, PNC et résultat retraité (2 pts)

**Actif net identifiable à la juste valeur au 01/01/2026 (0,75 pt)**

| Élément | Montant |
|---|---:|
| Capitaux propres de PODALIS au 01/01/2026 | 3 600 000 |
| Brevet : écart d'évaluation | 1 600 000 |
| Impôt différé passif (1 600 000 × 25 %) | – 400 000 |
| **Actif net identifiable** | **4 800 000** |

Le brevet, actif identifiable (il est déposé et peut être cédé), est comptabilisé à sa juste valeur même s'il ne figurait pas au bilan de PODALIS ; sa base fiscale étant nulle, l'écart donne un impôt différé passif [V IFRS 3 § 18 ; F05 § 2, § 11].

**Goodwill partiel (0,5 pt)** = 6 800 000 – 75 % × 4 800 000 = 6 800 000 – 3 600 000 = **3 200 000 €** [V IFRS 3 § 19, 32 ; F05 § 2.1]. Il n'est pas amorti ; aucun indice de perte de valeur n'existe au 31/12/2026 (annexe 1.2) : il reste à 3 200 000 €.

**PNC à la date d'acquisition (0,25 pt)** = 25 % × 4 800 000 = **1 200 000 €** (quote-part de l'actif net identifiable, méthode retenue par le groupe).

**Résultat retraité de PODALIS en 2026 (0,5 pt)** : amortissement du brevet 1 600 000 / 8 = 200 000 € ; net d'impôt 150 000 € ; résultat retraité 640 000 – 150 000 = **490 000 €**.

#### c. Écritures au 31/12/2026 (2 pts)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| **C6 – Bilan : honoraires d'acquisition** | | | |
| RST.CORDELANE | Résultat CORDELANE (aucun impôt différé) | 180 000 | |
| 261.CORDELANE | Titres de participation PODALIS | | 180 000 |
| **C6R – Compte de résultat** | | | |
| 6226 | Honoraires | 180 000 | |
| RES_CR | Résultat | | 180 000 |
| **C7 – Bilan : actions remises à la juste valeur** | | | |
| 261.CORDELANE | Titres de participation PODALIS (100 000 × (26 – 24)) | 200 000 | |
| 1041 | Primes d'émission | | 200 000 |
| **C8 – Bilan : écart d'évaluation au 01/01/2026** | | | |
| 205 | Concessions et droits similaires, brevets – procédé d'impression | 1 600 000 | |
| IDP | Impôt différé passif | | 400 000 |
| RSV.PODALIS | Réserves PODALIS (écart d'évaluation net) | | 1 200 000 |
| **C9 – Bilan : amortissement de 2026** | | | |
| RST.PODALIS | Résultat PODALIS | 150 000 | |
| IDP | Impôt différé passif | 50 000 | |
| 2805 | Amortissements des brevets (1 600 000 / 8) | | 200 000 |
| **C9R – Compte de résultat** | | | |
| 6811 | Dotations aux amortissements sur immobilisations incorporelles et corporelles | 200 000 | |
| CH_ID | Produit d'impôt différé | | 50 000 |
| RES_CR | Résultat | | 150 000 |

(0,5 pt par écriture ou couple d'écritures : C6 et C6R ; C7 ; C8 ; C9 et C9R.)

**Réponses tolérées (1.6)** : écriture C7 portée directement dans l'écriture d'élimination des titres (titres éliminés pour 6 800 000 € et prime majorée de 200 000 €) ; frais d'émission décrits comme « déjà traités en capitaux propres dans les comptes individuels » sans référence à IAS 32 ; contrepartie évaluée au cours de 26 € avec l'hypothèse explicite que ce cours vaut juste valeur au 01/01/2026.

**Erreurs fréquentes (1.6)** : honoraires maintenus dans le coût des titres, comme en règlement ANC (règle inverse de `JUR-G02`) ; actions remises évaluées à 24 € ; actions remises oubliées dans la contrepartie ; frais d'émission passés en charges ou ajoutés au coût des titres ; écart d'évaluation retenu brut d'impôt dans l'actif net ; goodwill calculé sur 100 % de l'actif net ; dotation aux amortissements constatée sur le goodwill (`JUR-G04`, `JUR-F07`).

**Références normatives (1.6)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 3 § 18, 19, 32, 37, 53 | Juste valeur des actifs acquis ; PNC ; goodwill ; contrepartie transférée, actions émises ; frais connexes | [V] | F05 § 2, § 12 |
| IAS 32 § 35, 35A, 37 | Coûts de transaction sur capitaux propres | [V] | F05 § 12 |
| PCG art. 212-9 ; avis CU CNC 2000-D | Frais d'augmentation de capital imputés sur la prime, nets d'impôt | [V] | F01 § 7 |
| IAS 12 § 15, 66 | Impôt différé sur l'écart d'évaluation ; effet sur le goodwill | [V] | F05 § 2 |

---

### 1.7 Partage des capitaux propres et mise en équivalence (8 pts)

#### a. Tableaux de partage au 31/12/2026 (2,5 pts)

**CORDELANE Tricotage (1 pt)** — capitaux propres retraités de la provision pour hausse des prix (question 1.3) ; la plus-value interne sur la machine est imputée à CORDELANE (question 1.5).

| Poste | Montant retraité | Groupe (100 %) | PNC (0 %) |
|---|---:|---:|---:|
| Capital | 4 000 000 | 4 000 000 | – |
| Réserves (11 400 000 + 72 000) | 11 472 000 | 11 472 000 | – |
| Résultat (2 300 000 + 48 000) | 2 348 000 | 2 348 000 | – |
| Total | 17 820 000 | 17 820 000 | – |
| Élimination des titres | | – 4 000 000 | |
| **Réserves consolidées** | | **11 472 000** | |
| **Résultat consolidé** | | **2 348 000** | |

**PODALIS (1,5 pt)** — capitaux propres retraités de l'écart d'évaluation (question 1.6).

| Poste | Montant retraité | Groupe (75 %) | PNC (25 %) |
|---|---:|---:|---:|
| Capital | 1 000 000 | 750 000 | 250 000 |
| Réserves | 2 600 000 | 1 950 000 | 650 000 |
| Écart d'évaluation net | 1 200 000 | 900 000 | 300 000 |
| Capitaux propres hors résultat (= actif net identifiable au 01/01/2026) | 4 800 000 | 3 600 000 | 1 200 000 |
| Résultat retraité | 490 000 | 367 500 | 122 500 |
| Élimination des titres (6 780 000 – 180 000 + 200 000) | | – 6 800 000 | |
| Goodwill inscrit à l'actif | | + 3 200 000 | |
| **Réserves consolidées** | | **0** | **1 200 000** |
| **Résultat** | | **367 500** | **122 500** |

PODALIS étant entrée dans le périmètre le 01/01/2026, ses réserves à cette date appartiennent au prix payé : elles n'entrent pas dans les réserves consolidées ; seul le résultat de 2026 revient au groupe pour 75 %. PNC au 31/12/2026 : 1 200 000 + 122 500 = **1 322 500 €**.

#### b. Mise en équivalence de MOUSSÉLIA (1,5 pt)

| Poste | Capitaux propres au 31/12/2026 | Quote-part du groupe (50 %) |
|---|---:|---:|
| Capital | 3 000 000 | 1 500 000 |
| Réserves (après distribution) | 1 400 000 | 700 000 |
| Résultat de 2026 | 960 000 | 480 000 |
| **Valeur d'équivalence** | **5 360 000** | **2 680 000** |
| Titres éliminés | | – 1 500 000 |
| **Réserves consolidées** | | **700 000** |
| **Résultat (quote-part)** | | **480 000** |

(0,75 pt.) Ni écart d'évaluation ni goodwill : MOUSSÉLIA a été constituée au pair par ses deux associés.

**Évolution de la participation en 2026 (0,5 pt)** : valeur d'équivalence au 31/12/2025, 50 % × (3 000 000 + 1 400 000 + 800 000) = 2 600 000 € ; + quote-part du résultat de 2026, 480 000 € ; – dividende reçu, 400 000 € ; = 2 680 000 € au 31/12/2026 [V IAS 28 § 10].

**Dividende (0,25 pt).** Le dividende de 400 000 € comptabilisé en produit par CORDELANE n'est pas un résultat du groupe : il fait partie de la quote-part de résultats de MOUSSÉLIA déjà reconnue les années précédentes, et sa distribution **réduit la valeur de la participation** [V IAS 28 § 10 ; F03 § 15]. Il est éliminé du résultat de CORDELANE et rendu aux réserves ; la mise en équivalence, calculée sur les capitaux propres après distribution, en tient compte.

#### c. Écritures au 31/12/2026 (2 pts)

| Compte | Intitulé | Débit | Crédit |
|---|---|---:|---:|
| **C10 – Bilan : CORDELANE Tricotage** | | | |
| CAP_ELIM.TRICOTAGE | Capital CORDELANE Tricotage | 4 000 000 | |
| RSV.TRICOTAGE | Réserves CORDELANE Tricotage retraitées | 11 472 000 | |
| RST.TRICOTAGE | Résultat CORDELANE Tricotage retraité | 2 348 000 | |
| 261.CORDELANE | Titres CORDELANE Tricotage | | 4 000 000 |
| RSV_G | Réserves consolidées – part du groupe | | 11 472 000 |
| RST_G | Résultat consolidé – part du groupe | | 2 348 000 |
| **C11 – Bilan : PODALIS** | | | |
| CAP_ELIM.PODALIS | Capital PODALIS | 1 000 000 | |
| RSV.PODALIS | Réserves PODALIS (2 600 000 + 1 200 000) | 3 800 000 | |
| RST.PODALIS | Résultat PODALIS retraité | 490 000 | |
| EA | Goodwill | 3 200 000 | |
| 261.CORDELANE | Titres PODALIS | | 6 800 000 |
| RST_G | Résultat consolidé – part du groupe | | 367 500 |
| RSV_M | Participations ne donnant pas le contrôle – réserves | | 1 200 000 |
| RST_M | Participations ne donnant pas le contrôle – résultat | | 122 500 |
| **C12 – Bilan : dividende de MOUSSÉLIA** | | | |
| RST.CORDELANE | Résultat CORDELANE | 400 000 | |
| RSV.CORDELANE | Réserves CORDELANE | | 400 000 |
| **C12R – Compte de résultat** | | | |
| 7611 | Revenus des titres de participation | 400 000 | |
| RES_CR | Résultat | | 400 000 |
| **C13 – Bilan : mise en équivalence de MOUSSÉLIA** | | | |
| TME | Titres mis en équivalence | 2 680 000 | |
| 261.CORDELANE | Titres de participation MOUSSÉLIA | | 1 500 000 |
| RSV_G | Réserves consolidées – part du groupe | | 700 000 |
| RST_G | Résultat consolidé – part du groupe | | 480 000 |
| **C13R – Compte de résultat** | | | |
| RES_CR | Résultat | 480 000 | |
| QP_MEE | Quote-part du résultat net des entités mises en équivalence | | 480 000 |

(0,5 pt pour C10, 0,75 pt pour C11, 0,75 pt pour C12 à C13R.) Au compte de résultat consolidé, les produits et charges de CORDELANE Tricotage et de PODALIS sont repris à 100 % ; la part des PNC (122 500 €) est présentée en répartition du résultat net. MOUSSÉLIA n'y apparaît que par sa quote-part de 480 000 €.

#### d. Capitaux propres consolidés au 31/12/2026 (2 pts)

**Réserves consolidées et résultat attribuable aux propriétaires de CORDELANE (1 pt)**

| | Réserves | Résultat 2026 |
|---|---:|---:|
| CORDELANE (comptes individuels) | 41 300 000 | 9 850 000 |
| Coûts d'emprunt de la plateforme (C2) | + 112 500 | + 105 060 |
| Plus-value interne sur la machine (C3) | – 78 750 | + 22 500 |
| Dividende de CORDELANE Tricotage (C4) | + 900 000 | – 900 000 |
| Honoraires d'acquisition de PODALIS (C6) | – | – 180 000 |
| Dividende de MOUSSÉLIA (C12) | + 400 000 | – 400 000 |
| CORDELANE Tricotage (C10) | + 11 472 000 | + 2 348 000 |
| PODALIS : élimination des titres et goodwill (C11) | – 3 200 000 + 3 200 000 = 0 | + 367 500 |
| MOUSSÉLIA (C13) | + 700 000 | + 480 000 |
| **Total** | **54 805 750** | **11 693 060** |

**Capitaux propres (1 pt)**

| Capitaux propres consolidés au 31/12/2026 | Montant |
|---|---:|
| Capital (3 100 000 actions de 5 €) | 15 500 000 |
| Primes d'émission (8 064 000 + 200 000) | 8 264 000 |
| Réserves consolidées | 54 805 750 |
| Résultat de 2026 attribuable aux propriétaires de CORDELANE | 11 693 060 |
| **Capitaux propres attribuables aux propriétaires de CORDELANE** | **90 262 810** |
| Participations ne donnant pas le contrôle (dont résultat 122 500) | 1 322 500 |
| **Total des capitaux propres** | **91 585 310** |

Le capital et les primes consolidés sont ceux de la mère : le capital des filiales est éliminé avec les titres. Les primes comprennent l'augmentation de capital du 01/01/2026 à la juste valeur des actions remises (500 000 € de capital, 1 900 000 + 200 000 € de prime), diminuée des frais d'émission nets d'impôt (36 000 €). Les participations ne donnant pas le contrôle font partie des capitaux propres [V IAS 1 § 54 q) ; IFRS 10 § 22 ; F14 § 2.2]. Résultat net de l'ensemble consolidé : 11 693 060 + 122 500 = 11 815 560 €.

**Contrôle** : capitaux propres individuels des trois sociétés intégrées (74 714 000 + 17 700 000 + 4 240 000 = 96 654 000) + retraitements nets (provision 120 000, coûts d'emprunt 217 560, machine – 56 250, brevet 1 050 000, honoraires – 180 000, juste valeur des actions 200 000) – titres éliminés (4 000 000 + 6 800 000) + goodwill 3 200 000 + (valeur d'équivalence 2 680 000 – titres MOUSSÉLIA 1 500 000) = 91 585 310 €.

**Réponses tolérées (1.7)** : présentation du goodwill dans la colonne des réserves de PODALIS (– 3 200 000 €) puis réintégration à l'actif ; tableau de mise en équivalence présenté à partir de la valeur au 31/12/2025 ; capitaux propres présentés sans détail des réserves de la mère si le calcul est justifié par le contrôle global.

**Erreurs fréquentes (1.7)** : réserves de PODALIS au 01/01/2026 comptées en réserves consolidées ; titres PODALIS éliminés pour 6 780 000 € ; PNC calculées sur les capitaux propres sans l'écart d'évaluation ; dividende de MOUSSÉLIA laissé en résultat ou déduit deux fois de la valeur d'équivalence ; capital des filiales ajouté à celui de la mère ; PNC présentées hors des capitaux propres ; primes oubliées (`JUR-G03`, `JUR-G04`, `JUR-F04`).

**Références normatives (1.7)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IFRS 10 § 22, B86 | Participations ne donnant pas le contrôle ; procédures de consolidation | [V] | F03 § 3 ; F04 R14 |
| IAS 28 § 10 | Méthode de la mise en équivalence ; distributions reçues | [V] | F03 § 15 |
| IAS 1 § 54 | Postes minimaux de l'état de la situation financière | [V] | F14 § 2.2 |

---

### 1.8 Processus de consolidation (2 pts)

**Rattachement des traitements (1,25 pt)**

| Phase | Traitements du dossier |
|---|---|
| Retraitements préparatoires et d'homogénéisation | Élimination de la provision pour hausse des prix (1.3, préparatoire : écriture fiscale) ; incorporation des coûts d'emprunt (1.4, homogénéisation avec IAS 23) ; honoraires d'acquisition en charges et actions remises à la juste valeur (1.6 a et c, mise aux normes IFRS du coût des titres) ; écart d'évaluation du brevet et son amortissement (1.6, évaluation à la juste valeur de l'actif net acquis) |
| Éliminations des opérations internes | Plus-value interne sur la machine ; dividende de CORDELANE Tricotage ; prestations et soldes réciproques (1.5) ; dividende de MOUSSÉLIA (1.7 c) |
| Élimination des titres, partage des capitaux propres et mise en équivalence | Goodwill de PODALIS, partage de CORDELANE Tricotage et de PODALIS, mise en équivalence de MOUSSÉLIA (1.6 b, 1.7) |
| Établissement des documents de synthèse | Capitaux propres consolidés (1.7 d) ; tableau des flux de trésorerie (1.9) |

(0,25 pt par phase, 0,25 pt pour la cohérence d'ensemble.)

**Ordre des phases (0,75 pt).** Le partage répartit entre le groupe et les participations ne donnant pas le contrôle les capitaux propres **retraités** de chaque filiale, et la mise en équivalence porte sur des capitaux propres établis selon les méthodes du groupe [V F03 § 3 ; F04 § 1]. La provision pour hausse des prix augmente, une fois éliminée, les réserves et le résultat de CORDELANE Tricotage (+ 120 000 € nets) ; les coûts d'emprunt augmentent ceux de CORDELANE (+ 217 560 € nets). Si le partage précédait ces retraitements, il porterait sur des montants faux, et les réserves consolidées, le résultat du groupe et, pour une filiale détenue avec des minoritaires, les participations ne donnant pas le contrôle seraient mal calculés ; l'impôt différé de chaque retraitement doit aussi être connu avant le partage, puisqu'il est compris dans les capitaux propres partagés.

**Réponses tolérées (1.8)** : écart d'évaluation du brevet, honoraires d'acquisition et évaluation des actions remises rattachés à la phase d'élimination des titres (détermination de la contrepartie et du goodwill), si le rattachement est justifié ; dividende de MOUSSÉLIA rattaché à la mise en équivalence, puisqu'il réduit la valeur de la participation (question 1.7 b).

**Erreurs fréquentes (1.8)** : dividende de MOUSSÉLIA rangé parmi les retraitements d'homogénéisation ; documents de synthèse omis ; ordre justifié par la seule habitude, sans lien avec les capitaux propres partagés (`JUR-G01`).

---

### 1.9 Tableau des flux de trésorerie consolidé (7 pts)

#### a. Extrait des flux d'investissement et de financement de 2026 (5 pts)

**Traitement des éléments (3 pts)**

| Élément | Classement et montant | Justification |
|---|---|---|
| Acquisition de PODALIS : part en numéraire | Investissement : – 4 200 000 + 540 000 = **– 3 660 000** | L'obtention du contrôle d'une filiale est un flux d'investissement présenté sur une ligne distincte, **net de la trésorerie de la filiale acquise** [V IAS 7 § 39, 42 ; F14 § 3] (0,75 pt) |
| Acquisition de PODALIS : 100 000 actions remises (2 600 000 €) | **Aucun flux** | Opération sans effet de trésorerie : l'acquisition d'une entité au moyen d'une émission d'actions est exclue du tableau et décrite dans les notes [V IAS 7 § 43, 44 b) ; F14 § 12] (0,5 pt) |
| Plateforme logistique : dépenses de construction | Investissement : **– 3 750 000** | Dépenses qui aboutissent à un actif comptabilisé [V IAS 7 § 16 ; F14 § 3] (0,25 pt) |
| Plateforme : intérêts incorporés (144 000 €) | Financement, avec les **intérêts versés** : – 310 000 au total | Le tableau présente le total des intérêts versés, y compris ceux incorporés au coût d'un actif [V IAS 7 § 32] ; le groupe les classe en financement [V IAS 7 § 33 ; annexe 1.2, point 5] : ils ne s'ajoutent pas aux dépenses d'investissement (0,5 pt) |
| Solde du prix de la machine (300 000 €) | **Aucun flux** | Règlement entre deux sociétés intégrées : il est éliminé, en décaissement chez CORDELANE Tricotage comme en encaissement chez CORDELANE [V IFRS 10 B86 c) ; F14 § 9] ; autres acquisitions 2 860 000 – 300 000 = 2 560 000 ; cessions 385 000 – 300 000 = 85 000 (0,5 pt) |
| Dividendes reçus | Investissement : MOUSSÉLIA **+ 400 000** ; CORDELANE Tricotage : aucun flux | Flux entre le groupe et la coentreprise mise en équivalence [V IAS 7 § 37, 38], classés en investissement par choix permanent du groupe [V IAS 7 § 31, 33 ; annexe 1.2] ; le dividende de CORDELANE Tricotage est interne (0,25 pt) |
| Honoraires d'acquisition (180 000 €) et frais d'émission (48 000 €) | Honoraires : activités **opérationnelles** ; frais d'émission : **financement – 48 000** | Les honoraires, passés en charges, n'aboutissent à aucun actif et ne peuvent être classés en investissement [V IAS 7 § 16 ; F14 § 9] ; les frais d'émission se rattachent à l'émission d'actions, activité de financement [V IAS 7 § 6, 17 ; F14 § 12 ; annexe 1.2] (0,25 pt) |

**Extrait du tableau des flux de trésorerie consolidé de 2026 (1,5 pt)**

| Flux liés aux activités d'investissement | Montant |
|---|---:|
| Acquisition de PODALIS, nette de la trésorerie acquise | – 3 660 000 |
| Construction de la plateforme logistique | – 3 750 000 |
| Autres acquisitions d'immobilisations corporelles et incorporelles | – 2 560 000 |
| Cessions d'immobilisations | + 85 000 |
| Dividende reçu de MOUSSÉLIA (coentreprise) | + 400 000 |
| **Flux nets liés aux activités d'investissement** | **– 9 485 000** |

| Flux liés aux activités de financement | Montant |
|---|---:|
| Encaissement d'emprunts | + 600 000 |
| Remboursements d'emprunts | – 1 250 000 |
| Intérêts versés (dont 144 000 incorporés au coût de la plateforme) | – 310 000 |
| Frais d'émission des actions remises aux vendeurs de PODALIS | – 48 000 |
| Dividendes versés aux propriétaires de CORDELANE | – 3 410 000 |
| Dividendes versés aux participations ne donnant pas le contrôle | 0 |
| **Flux nets liés aux activités de financement** | **– 4 418 000** |

(0,75 pt par partie.) Les flux sont présentés en montants bruts [V IAS 7 § 21] ; l'emprunt affecté n'a donné lieu, en 2026, qu'au paiement de ses intérêts (216 000 €), son remboursement commençant en 2027. Le dividende versé par CORDELANE Tricotage à CORDELANE (900 000 €) est interne.

**Notes sur l'acquisition de PODALIS (0,5 pt).** Contrepartie totale de 6 800 000 €, dont 4 200 000 € en trésorerie ; trésorerie de PODALIS à la date d'acquisition, 540 000 € ; actifs et passifs acquis par grandes catégories, dont le brevet de 1 600 000 € [V IAS 7 § 40 ; F14 § 3] ; description de la part payée par l'émission de 100 000 actions (2 600 000 €), opération sans effet de trésorerie [V IAS 7 § 43]. Les notes indiquent aussi le montant des coûts d'emprunt incorporés en 2026 (144 000 €) [V IAS 23 § 26 ; F04 R6].

#### b. Coentreprise et intégration proportionnelle (2 pts)

**Pourquoi le seul dividende (0,75 pt).** Mise en équivalence, MOUSSÉLIA n'est pas intégrée : ni sa trésorerie, ni ses flux ne figurent dans ceux du groupe. Le tableau ne retient que les flux entre le groupe et la coentreprise, ici le dividende reçu [V IAS 7 § 37, 38 ; F14 § 3]. La quote-part de résultat (480 000 €) n'est pas un flux de trésorerie : dans les flux opérationnels présentés selon la méthode indirecte, elle serait déduite du résultat [V IAS 7 § 20].

**Intégration proportionnelle (1,25 pt).** Le tableau reprendrait 50 % des flux de MOUSSÉLIA, et 50 % de sa trésorerie, après élimination des flux internes :

| Flux de 2026 | Mise en équivalence (IFRS) | Intégration proportionnelle |
|---|---:|---:|
| Activités opérationnelles | – | + 620 000 (50 % × 1 240 000) |
| Activités d'investissement | + 400 000 (dividende reçu) | – 260 000 (50 % × 520 000 ; le dividende reçu, interne, disparaît) |
| Activités de financement | – | – 80 000 (50 % × 160 000 de remboursement ; la moitié du dividende versé, soit 400 000 € reçus par CORDELANE, est éliminée) |
| **Effet sur la variation de la trésorerie du groupe** | **+ 400 000** | **+ 280 000** |

L'écart (– 120 000 €) est la quote-part du groupe dans la diminution de la trésorerie de MOUSSÉLIA (50 % × 240 000 €). Les flux opérationnels du groupe seraient plus élevés et les investissements de MOUSSÉLIA apparaîtraient, alors qu'en IFRS la coentreprise ne se lit qu'à travers ce qu'elle reverse au groupe (0,5 pt pour le principe, 0,75 pt pour les montants).

**Réponses tolérées (1.9)** : plateforme et autres acquisitions réunies sur une ligne de – 6 310 000 € ; acquisition de PODALIS présentée en deux lignes (– 4 200 000 € et + 540 000 €) si le total net est donné ; réponse qui signale que, selon le règlement ANC, le tableau des flux figure dans l'annexe et que les dividendes reçus des entités mises en équivalence y sont classés en activité (F14 § 1.5), en complément du chiffrage ; en b, effet présenté sans le tableau si les trois flux et la variation sont chiffrés.

**Erreurs fréquentes (1.9)** : acquisition présentée pour 6 800 000 € ou pour 4 200 000 € sans la trésorerie acquise ; actions remises présentées comme une augmentation de capital encaissée ; intérêts incorporés comptés deux fois (dans les dépenses de la plateforme et dans les intérêts versés) ; règlement du solde de la machine maintenu ; quote-part de résultat de MOUSSÉLIA présentée comme un flux ; honoraires classés en investissement ; dividende de CORDELANE Tricotage maintenu (`JUR-F07`, `JUR-F02`).

**Références normatives (1.9)**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| IAS 7 § 6, 16, 17, 20, 21, 31 à 33, 37 à 40, 42 à 44 | Activités ; investissement et financement ; intérêts et dividendes ; entités mises en équivalence ; obtention du contrôle ; opérations sans effet de trésorerie | [V] | F14 § 3, § 12 |
| IAS 23 § 26 | Informations sur les coûts d'emprunt incorporés | [V] | F04 R6 |
| IFRS 10 B86 c) | Élimination des flux intragroupe | [V] | F04 R14 |
| ANC 2020-01 art. 282-41, 282-43 (pour comparaison) | Tableau des flux dans l'annexe ; dividendes des entités mises en équivalence | [V] | F14 § 1.5 |

---

## DOSSIER 2 – OPÉRATIONS DE RESTRUCTURATION (25 points)

| Question | Compétence visée | Points |
|---|---|---:|
| 2.1 Qualification, distinction avec deux apports partiels d'actif, référentiel, régime fiscal de faveur | `1.1.a` Définir les opérations de restructuration et identifier le référentiel comptable applicable ; `1.1.b` Maîtriser le régime fiscal de droit commun et le régime de faveur | 4 |
| 2.2 Parités, actions émises, soulte, contrainte légale et condition fiscale, équité, répartition du capital | `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer ; `1.2.b` Déterminer une soulte simple et vérifier sa légalité | 5,5 |
| 2.3 Contrôle, sens et mode d'évaluation de chaque apport | `1.2.c` Déterminer le mode de valorisation des apports (valeur comptable ou réelle) | 2,5 |
| 2.4 Valeur et composition des apports, libération du capital, augmentations de capital et primes | `1.2.d` Calculer et composer les apports, y compris la fiscalité différée ; `1.2.a` Déterminer la parité d'échange et le nombre d'actions à créer | 4 |
| 2.5 Écritures chez CHAMBELLE Industrie | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 2,5 |
| 2.6 Écritures de base chez VERRÉMONT et chez PRESSOLINE | `1.3.a` Passer les écritures de base chez l'absorbante (bénéficiaire) et l'absorbée (apporteuse) | 3 |
| 2.7 Écritures complémentaires chez PRESSOLINE : opération réciproque et frais de scission | `1.3.c` Passer les écritures complémentaires (régime fiscal, situations particulières) | 2 |
| 2.8 Note au président de PRESSOLINE | `1.4.a` Restituer au dirigeant les impacts de l'opération sur les documents de synthèse | 1,5 |
| **Total** | | **25** |

---

### 2.1 Qualification, référentiel et régime fiscal (4 pts)

**Qualification et modalités (1,25 pt).** CHAMBELLE Industrie transmet la totalité de son patrimoine, réparti en deux branches, à deux sociétés qui existent déjà : c'est une **scission** [V C. com. L. 236-18 ; PCG art. 710-2, F01 § 1]. Chaque bénéficiaire reçoit, par transmission universelle, l'ensemble des actifs et des dettes de sa branche : VERRÉMONT reçoit l'usine, le brevet, les stocks, les créances et les dettes de la division « muselets », dont l'impôt sur les sociétés de la période que le traité y rattache ; PRESSOLINE reçoit ceux de la division « matériel de cave », dont la dette de 36 000 € envers elle-même. CHAMBELLE Industrie est **dissoute sans liquidation** : il n'y a ni réalisation des actifs ni partage entre les associés. Les apports sont rémunérés par des **augmentations de capital** des deux bénéficiaires ; les actions nouvelles VERRÉMONT et PRESSOLINE et la soulte versée par PRESSOLINE reviennent aux associés de CHAMBELLE Industrie, en échange de leurs actions, qui disparaissent. Aucune activité ne reste à CHAMBELLE Industrie : la scission est **totale**, forme seule visée par le programme.

**Distinction avec deux apports partiels d'actif (0,75 pt).** Dans un apport partiel d'actif, la société qui apporte une branche **reçoit elle-même** les titres de la bénéficiaire et **continue d'exister** [V PCG art. 710-2, F01 § 1]. Deux apports transformeraient CHAMBELLE Industrie en société détenant 50 000 actions VERRÉMONT et 48 000 actions PRESSOLINE, inscrites en titres de participation ; CHAMBELLE Participations ne détiendrait les actions PRESSOLINE qu'indirectement, et il faudrait une seconde opération (dissolution et liquidation, ou distribution) pour que les associés les reçoivent. La scission transmet les deux branches, attribue les actions aux associés et fait disparaître la société scindée en une seule opération.

**Référentiel (0,5 pt).** L'opération n'est pas un achat de titres : les bénéficiaires reçoivent un patrimoine et le paient en émettant leurs propres actions. Son enregistrement dans les comptes individuels des trois sociétés relève du **PCG, livre II, titre VII** (règlement ANC n° 2014-03 modifié), qui fixe les valeurs d'inscription des apports [V art. 710-1 et 720-1, F01 § 1]. Ces règles ne s'appliquent pas au calcul de la parité, qui repose sur les valeurs d'échange fournies [V art. 740-1, F01 § 1] : ce point sera décisif pour PRESSOLINE (2.2 et 2.4).

**Régime fiscal de faveur (1,5 pt)**
- *Conditions et appréciation (0,75 pt).* Les trois sociétés sont passibles de l'impôt sur les sociétés [V CGI art. 210 C-1, F02 § 1]. Le régime de l'art. 210 A s'applique **de plein droit**, sans agrément ni engagement de conservation des titres depuis 2018, à la scission d'une société qui comporte **au moins deux branches complètes d'activité** lorsque chaque bénéficiaire reçoit une ou plusieurs de ces branches [V CGI art. 210 B-1 ; BOI-IS-FUS-20-30-10 § 70, F02 § 1]. Une branche complète est l'ensemble des éléments d'une division qui constituent une exploitation autonome, capable de fonctionner par ses propres moyens ; les services administratifs communs sont rattachés à chaque branche pour leur quote-part [V BOI-IS-FUS-20-20 § 10 et 80, F02 § 1]. Ici, chaque division exerce réellement son activité, avec son responsable, son personnel, ses installations, ses fournisseurs et sa clientèle ; le traité répartit le service administratif commun entre les deux branches et aucun élément ne reste hors des branches : les deux conditions sont remplies. La définition fiscale de la scission admet une **soulte** qui ne dépasse pas **10 % de la valeur nominale des titres attribués** [V CGI art. 210-0 A, I, 2°, F02 § 1] : condition remplie (2.2 c). L'opération répond enfin à un motif économique valable (recentrage de la famille, reprise de chaque métier par un industriel du secteur) [V CGI art. 210-0 A, III, F02 § 1].
- *Effets pour CHAMBELLE Industrie (0,5 pt).* Les plus-values dégagées sur les éléments transmis ne sont **pas soumises à l'impôt sur les sociétés** : 870 000 € sur la branche « muselets » (2.5) [V CGI art. 210 A-1, F02 § 2] ; la branche « matériel de cave », transmise à sa valeur comptable, ne dégage aucune plus-value. Sous le régime de droit commun, la scission serait traitée comme une cessation d'entreprise et ces plus-values seraient imposées immédiatement [V BOI-IS-FUS-10-10-10 § 1, F02 § 2]. Le **résultat de la période** du 1er janvier au 31 mars 2027 reste imposé chez CHAMBELLE Industrie quel que soit le régime : l'impôt de 80 000 € est déjà compris dans les dettes fiscales, reprises par VERRÉMONT [V BOI-IS-FUS-10-20-30 § 210 et 330, F02 § 2].
- *Effets pour les bénéficiaires (0,25 pt).* Elles prennent les engagements de l'art. 210 A-3 [V F02 § 4]. VERRÉMONT réintègre les plus-values sur biens amortissables (constructions sur 15 ans, matériels et brevet sur 5 ans), inscrit fiscalement les produits finis à leur valeur chez CHAMBELLE Industrie et calculera une plus-value future sur le terrain d'après sa valeur fiscale : ces impositions futures justifient la provision pour impôts intégrée à l'apport [V F01 § 3.3 ; F02 § 6]. PRESSOLINE, qui reçoit sa branche à la valeur comptable, reprend les valeurs brutes, les amortissements et les valeurs fiscales de CHAMBELLE Industrie [V BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2] : la valeur non comptabilisée de la branche n'est imposée ni chez CHAMBELLE Industrie ni à la réalisation.

---

### 2.2 Parités, actions émises, soulte et répartition du capital (5,5 pts)

Dans une scission, chaque bénéficiaire émet un nombre d'actions déterminé directement par la valeur d'échange de la branche qu'elle reçoit [S guide p. imprimée 163, d'après `programme/perimetre_ue4.yaml`, compétence 1.2.a], et non par la valeur globale de la société scindée (8 325 000 €).

**a) VERRÉMONT (1,25 pt)**
- Valeur d'échange unitaire : 21 600 000 / 200 000 = **108 €** ; valeur de la branche « muselets » par action CHAMBELLE Industrie : 5 400 000 / 24 000 = **225 €** (0,5 pt).
- Parité : 225 / 108 = **25 actions VERRÉMONT pour 12 actions CHAMBELLE Industrie** (0,25 pt).
- Actions à émettre : 24 000 × 25 / 12 = **50 000 actions** (contrôle : 5 400 000 / 108 = 50 000). Les avoirs des trois associés (18 000, 3 600 et 2 400 actions) sont des multiples de 12 : il n'y a pas de rompus, et aucune soulte n'est nécessaire (0,5 pt).

**b) PRESSOLINE : parité exacte, parité du traité et soulte (1,75 pt)**
- *Valeurs unitaires (0,25 pt).* 1 200 000 / 20 000 = **60 €** ; valeur de la branche « matériel de cave » par action CHAMBELLE Industrie : 2 925 000 / 24 000 = **121,875 €**.
- *Parité exacte (0,25 pt).* 121,875 / 60 = 2,03125 = **65 actions PRESSOLINE pour 32 actions CHAMBELLE Industrie**, soit 24 000 × 65 / 32 = 48 750 actions.
- *Motif de l'arrondi (0,5 pt).* Le total est entier, mais CHAMBELLE Participations (18 000 actions) et Mme VAUCHERIN (3 600) ne détiennent pas un multiple de 32 actions : ils devraient recevoir 18 000 × 65 / 32 = 36 562,5 et 7 312,5 actions ; seul M. DROUILLARD (2 400 = 75 × 32) recevrait un nombre entier (4 875). Il faudrait traiter des **rompus**. Le traité retient une parité simple, **2 pour 1**, applicable à toutes les actions de chaque associé, et compense l'écart par une soulte en numéraire.
- *Actions émises (0,25 pt).* 24 000 × 2 = **48 000 actions** PRESSOLINE.
- *Soulte (0,5 pt).* 2 925 000 – 48 000 × 60 = **45 000 €**, soit 121,875 – 2 × 60 = **1,875 €** par action CHAMBELLE Industrie. Par associé : CHAMBELLE Participations 18 000 × 1,875 = **33 750 €**, Mme VAUCHERIN 3 600 × 1,875 = **6 750 €**, M. DROUILLARD 2 400 × 1,875 = **4 500 €** (total 45 000 €).

**c) Contrainte légale, condition fiscale et équité (1,25 pt)**
- *PRESSOLINE (0,5 pt).* La soulte ne peut dépasser **10 % de la valeur nominale des actions attribuées** [V C. com. L. 236-18 al. 3 ; même plafond qu'en fusion, L. 236-1 al. 3, F01 § 4] : 10 % × 48 000 × 20 = **96 000 €**. La soulte de 45 000 € (46,88 % du plafond) est **légale**. Par action CHAMBELLE Industrie : 1,875 € pour un plafond de 10 % × 2 × 20 = 4 €.
- *VERRÉMONT (0,25 pt).* La parité exacte est appliquée sans soulte : la contrainte est respectée sans calcul (plafond théorique : 10 % × 50 000 × 15 = 75 000 €).
- *Condition fiscale (0,25 pt).* La soulte de chaque bénéficiaire reste dans la limite de 10 % du nominal des titres qu'elle attribue : l'opération entre dans la définition fiscale de la scission et conserve le régime de faveur [V CGI art. 210-0 A, I, 2°, F02 § 1]. Une soulte supérieure à la limite l'en aurait fait sortir, en plus d'être interdite par le Code de commerce.
- *Équité (0,25 pt).* Pour une action CHAMBELLE Industrie (346,875 €), l'associé reçoit 25 / 12 action VERRÉMONT (25 / 12 × 108 = 225 €), 2 actions PRESSOLINE (120 €) et 1,875 € : 225 + 120 + 1,875 = **346,875 €** [V méthode du corrigé du sujet zéro, F01 § 4]. Après l'opération, l'action VERRÉMONT vaut toujours (21 600 000 + 5 400 000) / 250 000 = 108 € et l'action PRESSOLINE (1 200 000 + 2 925 000 – 45 000) / 68 000 = 60 € : aucun groupe d'associés ne s'enrichit aux dépens d'un autre.

**d) Répartition du capital et des droits de vote après l'opération (1,25 pt)**

VERRÉMONT — 200 000 + 50 000 = 250 000 actions (0,5 pt) :

| Actionnaire | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| TALVERGNE Holding | 132 000 | 66,00 % | 132 000 | 52,80 % |
| Autres actionnaires de VERRÉMONT | 68 000 | 34,00 % | 68 000 | 27,20 % |
| CHAMBELLE Participations (18 000 × 25 / 12) | – | – | 37 500 | 15,00 % |
| Mme VAUCHERIN (3 600 × 25 / 12) | – | – | 7 500 | 3,00 % |
| M. DROUILLARD (2 400 × 25 / 12) | – | – | 5 000 | 2,00 % |
| **Total** | **200 000** | **100 %** | **250 000** | **100 %** |

PRESSOLINE — 20 000 + 48 000 = 68 000 actions (0,5 pt) :

| Associé | Avant | % avant | Après | % après |
|---|---:|---:|---:|---:|
| MARGUEVILLE Participations | 16 000 | 80,00 % | 16 000 | 23,53 % |
| Cadres de PRESSOLINE | 4 000 | 20,00 % | 4 000 | 5,88 % |
| CHAMBELLE Participations (18 000 × 2) | – | – | 36 000 | 52,94 % |
| Mme VAUCHERIN (3 600 × 2) | – | – | 7 200 | 10,59 % |
| M. DROUILLARD (2 400 × 2) | – | – | 4 800 | 7,06 % |
| **Total** | **20 000** | **100 %** | **68 000** | **100 %** |

Droits de vote (0,25 pt) : chaque action donnant une voix, ils suivent la même répartition. TALVERGNE Holding garde la majorité des voix de VERRÉMONT ; chez PRESSOLINE, la majorité passe à **CHAMBELLE Participations**, qui peut seule prendre les décisions collectives, dont la nomination et la révocation du président (annexe 2.1). Ces constats fondent l'analyse de 2.3.

---

### 2.3 Contrôle, sens et mode d'évaluation de chaque apport (2,5 pts)

**Situation de contrôle (0,5 pt).** CHAMBELLE Industrie est contrôlée de manière exclusive par CHAMBELLE Participations (75 % des voix), VERRÉMONT par TALVERGNE Holding (66 %) et PRESSOLINE par MARGUEVILLE Participations (80 %). Aucune des trois sociétés ne détient d'actions d'une autre et les trois holdings n'ont aucun lien en capital : aucune ne contrôle l'autre et elles n'ont pas de mère commune. Le contrôle s'apprécie au niveau des personnes morales, sans remonter aux familles ou aux personnes physiques [V PCG art. 741-1 et 741-2, F01 § 2.1]. Les deux apports sont réalisés **sous contrôle distinct** ; aucun accord entre actionnaires ne crée de contrôle partagé.

**Branche « muselets » → VERRÉMONT (0,75 pt).** Après l'opération, TALVERGNE Holding, actionnaire principal de VERRÉMONT, détient 52,80 % des droits de vote : bien que diluée, elle **conserve le contrôle** ; CHAMBELLE Participations perd le contrôle de la branche et n'obtient que 15 % de VERRÉMONT. L'apport est **à l'endroit** : VERRÉMONT est l'initiatrice, la branche « muselets » la cible [V art. 730-1 et 742-1, F01 § 1 et § 2.2]. Contrôle distinct et sens à l'endroit : **valeur réelle** (cas 4), l'opération étant traitée comme une acquisition [V art. 743-1, F01 § 2.3].

**Branche « matériel de cave » → PRESSOLINE (1 pt).** Avant l'opération, MARGUEVILLE Participations détient 80 % de PRESSOLINE ; après, elle n'en a plus que 23,53 %, et **CHAMBELLE Participations**, actionnaire principal de la société scindée, en détient 52,94 % : elle **prend le contrôle** de la bénéficiaire. L'apport est **à l'envers** : l'initiatrice est le groupe CHAMBELLE (la société scindée et sa mère), la cible est PRESSOLINE [V art. 742-2, F01 § 2.2]. Contrôle distinct et sens à l'envers : **valeur comptable** (cas 3) [V art. 743-1, F01 § 2.3]. Justification donnée par le texte : la société qui passe sous un nouveau contrôle est PRESSOLINE, dont les actifs et les passifs ne figurent pas dans le traité ; ceux de l'initiatrice, ici la branche apportée, n'ont pas à être réévalués [V p. 83, F01 § 2.3]. Réévaluer la branche reviendrait à faire constater par PRESSOLINE, désormais contrôlée par CHAMBELLE Participations, une plus-value sur des actifs que ce même actionnaire contrôlait déjà.

**Analyse par apport (0,25 pt).** Chaque apport s'analyse séparément : une même scission peut combiner une évaluation à la valeur réelle et une évaluation à la valeur comptable, selon que l'actionnaire principal de la société scindée prend ou non le contrôle de chaque bénéficiaire. L'exception de l'art. 743-3 est examinée en 2.4 b.

---

### 2.4 Valeur et composition des apports (4 pts)

**a) Branche « muselets » à la valeur réelle (2 pts)**

*Éléments identifiés (0,5 pt).* En valeur réelle, le traité retient la valeur réelle de chaque élément identifié, qu'il figure ou non au bilan de CHAMBELLE Industrie [V art. 744-1, F01 § 3.1] : le **brevet** du muselet à ouverture facilitée, absent du bilan parce que ses dépenses de mise au point ont été passées en charges, est un actif identifié apporté.

| Élément | Valeur nette comptable | Valeur réelle | Écart |
|---|---:|---:|---:|
| Brevet (non inscrit) | 0 | 260 000 | + 260 000 |
| Terrain | 220 000 | 220 000 | 0 |
| Constructions | 1 380 000 | 1 900 000 | + 520 000 |
| Matériels industriels | 1 260 000 | 1 560 000 | + 300 000 |
| Matières premières | 560 000 | 560 000 | 0 |
| Produits finis | 740 000 | 820 000 | + 80 000 |
| Clients | 1 680 000 | 1 680 000 | 0 |
| Disponibilités | 410 000 | 410 000 | 0 |
| **Actifs identifiés** | **6 250 000** | **7 410 000** | **+ 1 160 000** |
| Dettes (900 000 + 520 000 + 300 000) | 1 720 000 | 1 720 000 | 0 |

*Provision pour impôts intégrée à l'apport (0,75 pt).* Sous le régime de faveur, l'imposition des plus-values sur biens amortissables (réintégration étalée) et du profit sur produits finis (inscrits fiscalement à leur valeur chez CHAMBELLE Industrie) est reportée chez VERRÉMONT ; l'écart entre leur valeur d'apport et leur valeur fiscale est une différence temporaire, qui donne un impôt différé passif intégré à l'apport [V corrigé du sujet zéro, Q 2.4, F01 § 3.3 ; F02 § 6]. Le brevet, de valeur fiscale nulle et amortissable du point de vue fiscal (annexe 2.3), entre dans la base pour toute sa valeur.

| Élément | Base | Impôt différé (25 %) |
|---|---:|---:|
| Constructions | 520 000 | 130 000 |
| Matériels industriels | 300 000 | 75 000 |
| Brevet | 260 000 | 65 000 |
| Produits finis | 80 000 | 20 000 |
| **Total : passif d'impôt différé** | **1 160 000** | **290 000** |

Le terrain n'a pas de plus-value : aucune base. La provision de **290 000 €** est inscrite au compte **1523 Provisions pour impôts** [V F01 § 3.3].

*Actif net réel identifié et conséquence (0,5 pt)*

| | Montant |
|---|---:|
| Actifs identifiés | 7 410 000 |
| – Dettes | – 1 720 000 |
| – Provision pour impôts | – 290 000 |
| **Actif net réel identifié** | **5 400 000** |
| Valeur globale retenue par le traité | 5 400 000 |
| **Écart (fonds commercial)** | **0** |

Contrôle : 4 530 000 (actif net comptable) + 1 160 000 – 290 000 = 5 400 000 €. La valeur globale de l'apport est égale à la somme algébrique des valeurs réelles des éléments identifiés : **aucun fonds commercial** n'est à inscrire, conformément au traité [V art. 744-1, F01 § 3.1].

*Composition de l'apport reçu par VERRÉMONT (0,25 pt).* Brevet 260 000, terrain 220 000, constructions 1 900 000, matériels 1 560 000, matières premières 560 000, produits finis 820 000, clients 1 680 000, disponibilités 410 000 ; à déduire : provision pour impôts 290 000, emprunts 900 000, fournisseurs 520 000, dettes fiscales et sociales 300 000 ; apport net **5 400 000 €**. Les éléments sont inscrits à leur valeur réelle, sans reprise des amortissements de CHAMBELLE Industrie.

**b) Branche « matériel de cave » à la valeur comptable (1 pt)**
- *Valeur et composition (0,5 pt).* L'apport est inscrit pour l'**actif net comptable** de la branche : 2 045 000 – 440 000 = **1 605 000 €** [V art. 744-2, F01 § 3.2]. PRESSOLINE reprend les valeurs brutes et les amortissements de CHAMBELLE Industrie [V BOI-IS-FUS-10-20-40-20 § 170-180, F01 § 3.2] : outillages 640 000 (amortis de 380 000), matériel de transport 360 000 (amorti de 210 000), marchandises 780 000, clients 640 000, disponibilités 215 000 ; à déduire : fournisseurs 290 000 (dont 36 000 dus à PRESSOLINE) et dettes fiscales et sociales 150 000. La clientèle et le savoir-faire de la division (valeur d'échange 2 925 000 €, soit 1 320 000 € de plus que l'actif net comptable) ne sont pas inscrits.
- *Libération du capital (0,5 pt).* Lorsque la valeur comptable s'impose, les valeurs réelles doivent être retenues si l'actif net comptable apporté est insuffisant pour libérer le capital émis [V art. 743-3, F01 § 2.4]. L'augmentation de capital de PRESSOLINE est de 48 000 × 20 = 960 000 € : l'actif net comptable de 1 605 000 € la couvre largement, et couvre aussi la soulte (960 000 + 45 000 = 1 005 000 €). L'exception ne joue pas : la valeur comptable est maintenue.

**c) Augmentations de capital et primes de scission (1 pt)**
- *VERRÉMONT (0,5 pt).* Augmentation de capital : 50 000 × 15 = **750 000 €** ; prime de scission : 5 400 000 – 750 000 = **4 650 000 €**.
- *PRESSOLINE (0,5 pt).* Le nombre d'actions repose sur les valeurs réelles (2.2), mais la prime se calcule sur la **valeur d'apport comptable** [V art. 740-1 et 744-2, F01 § 1 et § 4] : augmentation de capital **960 000 €** ; prime de scission = 1 605 000 – 960 000 – 45 000 (soulte) = **600 000 €**, avant imputation des frais (2.7).

---

### 2.5 Écritures chez CHAMBELLE Industrie au 31 mars 2027 (2,5 pts)

CHAMBELLE Industrie sort chaque branche pour ses valeurs comptables (valeurs brutes et amortissements) et constate une créance sur la bénéficiaire égale à la **valeur d'apport retenue au traité** (annexe 2.4).

**A1 — Transmission de la branche « muselets » à VERRÉMONT (0,75 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – VERRÉMONT, compte d'apport | 5 400 000 | |
| 28131 Amortissements des bâtiments | 920 000 | |
| 28154 Amortissements des matériels industriels | 1 890 000 | |
| 164 Emprunts auprès des établissements de crédit | 900 000 | |
| 401 Fournisseurs | 520 000 | |
| 44 État et autres collectivités publiques (dettes fiscales et sociales) | 300 000 | |
| 211 Terrains | | 220 000 |
| 2131 Bâtiments | | 2 300 000 |
| 2154 Matériels industriels | | 3 150 000 |
| 31 Matières premières et fournitures | | 560 000 |
| 355 Produits finis | | 740 000 |
| 411 Clients | | 1 680 000 |
| 512 Banques | | 410 000 |
| 778 Autres produits exceptionnels (résultat de scission) | | 870 000 |
| **Total** | **9 930 000** | **9 930 000** |

**A2 — Transmission de la branche « matériel de cave » à PRESSOLINE (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 467 Divers comptes débiteurs – PRESSOLINE, compte d'apport | 1 605 000 | |
| 28155 Amortissements des outillages industriels | 380 000 | |
| 28182 Amortissements du matériel de transport | 210 000 | |
| 401 Fournisseurs (dont PRESSOLINE : 36 000) | 290 000 | |
| 44 État et autres collectivités publiques (dettes fiscales et sociales) | 150 000 | |
| 2155 Outillages industriels | | 640 000 |
| 2182 Matériel de transport | | 360 000 |
| 37 Stocks de marchandises | | 780 000 |
| 411 Clients | | 640 000 |
| 512 Banques | | 215 000 |
| **Total** | **2 635 000** | **2 635 000** |

**Résultat de scission (0,5 pt).** Branche « muselets » : 5 400 000 – 4 530 000 = **+ 870 000 €**, présenté en résultat exceptionnel (compte 778), la scission étant pour CHAMBELLE Industrie un événement majeur et inhabituel [V PCG art. 513-5 ; hypothèse de l'annexe 2.4, F01 § 9] ; non imposé sous le régime de faveur (2.1). Branche « matériel de cave » : la valeur d'apport est la valeur comptable, **aucun résultat** (1 605 000 – 1 605 000 = 0), bien que la valeur d'échange de la branche dépasse de 1 320 000 € son actif net comptable.

**A3 — Réception des actions et de la soulte (0,25 pt).** Les actions, détenues seulement le temps de leur attribution, transitent par le compte 503. Les actions PRESSOLINE sont inscrites pour la valeur d'apport diminuée de la soulte : 1 605 000 – 45 000 = 1 560 000 €.

| Compte | Débit | Crédit |
|---|---:|---:|
| 503 Actions VERRÉMONT (50 000 actions) | 5 400 000 | |
| 503 Actions PRESSOLINE (48 000 actions) | 1 560 000 | |
| 512 Banques (soulte) | 45 000 | |
| 467 VERRÉMONT, compte d'apport | | 5 400 000 |
| 467 PRESSOLINE, compte d'apport | | 1 605 000 |

**A4 et A5 — Droits des associés et attribution (0,5 pt).** Capitaux propres augmentés du résultat de scission : 6 135 000 + 870 000 = **7 005 000 €** = 5 400 000 + 1 560 000 + 45 000. Droits : CHAMBELLE Participations 75 % = 5 253 750 € (37 500 actions VERRÉMONT pour 4 050 000, 36 000 actions PRESSOLINE pour 1 170 000, soulte 33 750) ; Mme VAUCHERIN 15 % = 1 050 750 € (810 000 + 234 000 + 6 750) ; M. DROUILLARD 10 % = 700 500 € (540 000 + 156 000 + 4 500).

A4 :

| Compte | Débit | Crédit |
|---|---:|---:|
| 101 Capital | 1 200 000 | |
| 1061 Réserve légale | 120 000 | |
| 1068 Autres réserves | 4 575 000 | |
| 120 Résultat de l'exercice (240 000 + 870 000) | 1 110 000 | |
| 456 Associés – CHAMBELLE Participations | | 5 253 750 |
| 456 Associés – Mme VAUCHERIN | | 1 050 750 |
| 456 Associés – M. DROUILLARD | | 700 500 |

A5 :

| Compte | Débit | Crédit |
|---|---:|---:|
| 456 Associés – CHAMBELLE Participations | 5 253 750 | |
| 456 Associés – Mme VAUCHERIN | 1 050 750 | |
| 456 Associés – M. DROUILLARD | 700 500 | |
| 503 Actions VERRÉMONT | | 5 400 000 |
| 503 Actions PRESSOLINE | | 1 560 000 |
| 512 Banques (soulte) | | 45 000 |

Tous les comptes de CHAMBELLE Industrie sont alors soldés.

---

### 2.6 Écritures de base chez VERRÉMONT et chez PRESSOLINE au 31 mars 2027 (3 pts)

**a) VERRÉMONT**

**A6 — Augmentation de capital (0,5 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (CHAMBELLE Industrie) | 5 400 000 | |
| 101 Capital (50 000 × 15) | | 750 000 |
| 1042 Primes de fusion (prime de scission) | | 4 650 000 |

**A7 — Réalisation de l'apport à la valeur réelle (1,25 pt).** Éléments à leur valeur réelle, sans amortissements repris ; brevet inscrit au compte 205 ; provision pour impôts au compte 1523 ; pas de fonds commercial [V art. 744-1, F01 § 3.1 et § 9]. Barème : actifs identifiés dont le brevet (0,5), provision pour impôts (0,25), dettes et compte d'apport (0,25), absence de fonds commercial et d'amortissements repris (0,25).

| Compte | Débit | Crédit |
|---|---:|---:|
| 205 Concessions et droits similaires, brevets | 260 000 | |
| 211 Terrains | 220 000 | |
| 2131 Bâtiments | 1 900 000 | |
| 2154 Matériels industriels | 1 560 000 | |
| 31 Matières premières et fournitures | 560 000 | |
| 355 Produits finis | 820 000 | |
| 411 Clients | 1 680 000 | |
| 512 Banques | 410 000 | |
| 1523 Provisions pour impôts | | 290 000 |
| 164 Emprunts auprès des établissements de crédit | | 900 000 |
| 401 Fournisseurs | | 520 000 |
| 44 État et autres collectivités publiques (dettes fiscales et sociales) | | 300 000 |
| 4561 Associés – Comptes d'apport en société (CHAMBELLE Industrie) | | 5 400 000 |
| **Total** | **7 410 000** | **7 410 000** |

**b) PRESSOLINE**

**A8 — Augmentation de capital et soulte due (0,5 pt).** La soulte fait partie de la rémunération de l'apport : elle diminue la prime [V F01 § 4 et § 9].

| Compte | Débit | Crédit |
|---|---:|---:|
| 4561 Associés – Comptes d'apport en société (CHAMBELLE Industrie) | 1 605 000 | |
| 101 Capital (48 000 × 20) | | 960 000 |
| 1042 Primes de fusion (1 605 000 – 960 000 – 45 000) | | 600 000 |
| 468 Divers comptes créditeurs – soulte à verser | | 45 000 |

**A9 — Réalisation de l'apport à la valeur comptable (0,5 pt).** Valeurs brutes d'origine et amortissements repris [V F01 § 3.2].

| Compte | Débit | Crédit |
|---|---:|---:|
| 2155 Outillages industriels | 640 000 | |
| 2182 Matériel de transport | 360 000 | |
| 37 Stocks de marchandises | 780 000 | |
| 411 Clients | 640 000 | |
| 512 Banques | 215 000 | |
| 28155 Amortissements des outillages industriels | | 380 000 |
| 28182 Amortissements du matériel de transport | | 210 000 |
| 401 Fournisseurs (dont dette envers PRESSOLINE : 36 000) | | 290 000 |
| 44 État et autres collectivités publiques (dettes fiscales et sociales) | | 150 000 |
| 4561 Associés – Comptes d'apport en société (CHAMBELLE Industrie) | | 1 605 000 |
| **Total** | **2 635 000** | **2 635 000** |

**A10 — Versement de la soulte (0,25 pt)**

| Compte | Débit | Crédit |
|---|---:|---:|
| 468 Divers comptes créditeurs – soulte à verser | 45 000 | |
| 512 Banques | | 45 000 |

---

### 2.7 Écritures complémentaires chez PRESSOLINE (2 pts)

**A11 — Opération réciproque (1 pt).** La branche reçue comprend la dette fournisseur de 36 000 € de CHAMBELLE Industrie envers PRESSOLINE, que PRESSOLINE a inscrite en clients. En recevant la branche, PRESSOLINE devient débitrice de sa propre créance : créance et dette s'éteignent par **confusion** [V C. civ. art. 1349, F01 § 8]. L'opération réciproque existe à la date de réalisation, qui est aussi la date d'effet. Barème : justification (0,5), écriture (0,5).

| Compte | Débit | Crédit |
|---|---:|---:|
| 401 Fournisseurs (dette reçue envers PRESSOLINE) | 36 000 | |
| 411 Clients (créance sur CHAMBELLE Industrie) | | 36 000 |

**A12 — Frais de scission (1 pt).** Les frais de scission peuvent être imputés sur la prime [V PCG art. 212-9, F01 § 7], pour leur montant net d'impôt [V avis CU CNC n° 2000-D, recueil ANC p. 103, F01 § 7] : 52 000 × 75 % = **39 000 €** ; l'économie d'impôt de 13 000 € diminue l'impôt sur les sociétés 2027 de PRESSOLINE. Prime restante : 600 000 – 39 000 = **561 000 €**. Barème : justification et calcul (0,5), écriture (0,5).

| Compte | Débit | Crédit |
|---|---:|---:|
| 1042 Primes de fusion (52 000 × 75 %) | 39 000 | |
| 444 État – Impôts sur les bénéfices (52 000 × 25 %) | 13 000 | |
| 512 Banques | | 52 000 |

---

### 2.8 Note au président de PRESSOLINE (1,5 pt)

**Capitaux propres juste après la scission (0,5 pt)**

| Poste | Avant | Variation | Après |
|---|---:|---:|---:|
| Capital (68 000 actions × 20) | 400 000 | + 960 000 | 1 360 000 |
| Prime de scission | 0 | + 600 000 – 39 000 | 561 000 |
| Réserve légale | 40 000 | | 40 000 |
| Autres réserves | 380 000 | | 380 000 |
| Report à nouveau | 30 000 | | 30 000 |
| **Total** | **850 000** | **+ 1 521 000** | **2 371 000** |

Contrôle : + 1 521 000 = valeur d'apport (1 605 000) – soulte (45 000) – frais nets d'impôt (39 000). Les capitaux propres sont presque triplés, mais la branche étant reçue à sa valeur comptable, la valeur de sa clientèle et de son savoir-faire (1 320 000 €) n'apparaît pas au bilan : les capitaux propres par action passent de 42,50 € à 34,87 €, alors que l'action vaut toujours environ 60 € ((4 080 000 – 39 000) / 68 000 = 59,43 € après les frais nets d'impôt).

**Perte du contrôle (0,5 pt).** MARGUEVILLE Participations passe de 80 % à 23,53 % des droits de vote ; CHAMBELLE Participations obtient 52,94 % et décide seule des décisions collectives, dont la nomination et la révocation du président. M. MARGUEVILLE dirige désormais PRESSOLINE avec l'accord de ce nouvel associé majoritaire. C'est ce changement de contrôle qui impose la valeur comptable : l'opération est économiquement l'entrée de PRESSOLINE dans le giron de la famille CHAMBELLE, et non l'acquisition d'une branche par PRESSOLINE.

**Enjeux pour les parties prenantes (0,5 pt)**
- *Créanciers de la branche reçue* : fournisseurs, administration et organismes sociaux (404 000 € après extinction des 36 000 € réciproques) ont désormais pour débitrice PRESSOLINE, dont les capitaux propres atteignent 2 371 000 € ; la branche n'apporte aucun emprunt.
- *Salariés* : les 31 salariés de la division et la personne du service administratif rattachée à la branche rejoignent les 14 de PRESSOLINE, dont l'effectif passe à 46 personnes : leur emploi dépend du maintien de l'activité de la branche (vente de matériel et entretien), que PRESSOLINE doit intégrer à son organisation.
- *Banque* : l'endettement financier reste de 120 000 € (5,06 % des capitaux propres) ; la trésorerie atteint 428 000 € (310 000 + 215 000 – 45 000 de soulte – 52 000 de frais), mais le besoin en fonds de roulement augmente avec 780 000 € de marchandises et 640 000 € de créances clients. La banque intégrera à son analyse le changement d'associé majoritaire : la solidité de CHAMBELLE Participations compte désormais autant que celle du fondateur.

Grille de niveaux pour les enjeux : 0 (absence ou idées sans lien avec le cas) ; 0,25 (une ou deux parties prenantes, sans chiffres) ; 0,5 (trois parties prenantes, idées chiffrées et reliées au cas).

---

### Réponses tolérées
- **2.1** : distinction avec deux apports partiels d'actif présentée par les seuls effets pour les associés (titres reçus directement ou par l'intermédiaire de la société qui apporte) ; motif économique non mentionné, si les conditions des branches complètes et de la soulte sont traitées.
- **2.2** : calcul par le nombre d'actions (5 400 000 / 108 = 50 000) plutôt que par la parité ; plafond de la soulte vérifié par action CHAMBELLE Industrie (1,875 € pour 4 €) plutôt qu'en total ; équité vérifiée par branche (225 € et 121,875 €) plutôt que pour l'action entière.
- **2.3** : sens de l'opération justifié par la seule comparaison des droits de vote de TALVERGNE Holding, MARGUEVILLE Participations et CHAMBELLE Participations avant et après, sans recours aux notions d'initiatrice et de cible.
- **2.4** : présentation de la composition de l'apport de PRESSOLINE en valeurs nettes, si la reprise des valeurs brutes et des amortissements est indiquée dans A9.
- **2.5** : compte 261, 50 ou 508 au lieu de 503 pour les actions reçues ; écritures A3 et A5 remplacées par une seule écriture (débit 456, crédit 467), si le candidat indique que les bénéficiaires remettent les actions et la soulte directement aux associés ; écriture A4 qui solde d'abord le compte 778 vers le résultat ; comptes 421, 431, 444 ou 447 au lieu de 43 et 44.
- **2.6** : compte 1043 Primes d'apport au lieu de 1042, ou un sous-compte « prime de scission » de l'un ou l'autre ; A8 et A10 regroupées (soulte directement au crédit du 512) ; brevet au compte 2051 ou 203 s'il est justifié ; comptes 421, 431, 444 ou 447 au lieu de 43 et 44.
- **2.7** : extinction de la créance réciproque intégrée à A9 (fournisseurs reçus pour 254 000 € et créance clients de PRESSOLINE soldée), si la confusion est expliquée ; frais en deux écritures (1042 / 512 pour 52 000 €, puis 444 / 1042 pour 13 000 €).
- **2.8** : la logique du candidat prévaut lorsque ses montants découlent d'une erreur antérieure correctement reportée [`JUR-F08`].

### Erreurs fréquentes (rapports du jury)
- `JUR-R05` Difficulté à s'adapter : un seul mode d'évaluation retenu pour toute la scission ; contrôle apprécié au niveau des familles plutôt que des holdings ; **nombre d'actions PRESSOLINE calculé sur l'actif net comptable** (1 605 000 / 60 = 26 750 actions) : outre la spoliation des associés de CHAMBELLE Industrie, ce calcul donnerait à CHAMBELLE Participations 42,91 % des voix et conduirait à conclure, à tort, à un apport à l'endroit ; nombre d'actions calculé sur la valeur globale de CHAMBELLE Industrie (8 325 000 €) au lieu de la valeur de chaque branche.
- `JUR-R01` Prime de scission mal calculée : prime de PRESSOLINE calculée sur la valeur réelle (2 925 000 – 960 000 – 45 000 = 1 920 000 €) ou sans déduire la soulte (645 000 €) ; frais imputés pour leur montant brut (prime finale de 548 000 €).
- `JUR-F04` Absence de contrôle d'équilibre des écritures A1, A2, A7 et A9.
- `JUR-F07` Annexes mal exploitées : brevet oublié parce qu'il ne figure pas au bilan (actif net identifié de 5 205 000 € et fonds commercial de 195 000 € inscrits à tort) ; plus-value sur produits finis oubliée ; amortissements de CHAMBELLE Industrie repris dans A7 ou non repris dans A9 ; dette réciproque de 36 000 € non éteinte.
- Erreurs propres à ce cas :
  - résultat de scission constaté sur la branche « matériel de cave » (actions PRESSOLINE inscrites à leur valeur d'échange de 2 880 000 € et produit de 1 320 000 €), alors que la valeur d'apport retenue au traité est la valeur comptable ;
  - plafond de la soulte calculé sur la valeur de la branche (10 % × 2 925 000 = 292 500 €) ou sur le nominal des actions CHAMBELLE Industrie (120 000 €) au lieu du nominal des actions PRESSOLINE attribuées ;
  - exception de l'art. 743-3 invoquée pour revenir à la valeur réelle, alors que l'actif net comptable couvre le capital émis ;
  - engagement de conservation des titres pendant trois ans présenté comme condition du régime de faveur ;
  - usage des comptes 675 et 775, supprimés du PCG 2026, pour le résultat de scission chez CHAMBELLE Industrie.

### Références normatives

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| PCG art. 710-1, 710-2, 720-1, 730-1 ; C. com. L. 236-18 | Champ du titre VII, définitions de la scission et de l'apport partiel d'actif, inscription des apports, initiatrice et cible | [V] p. 81-82 ; Légifrance | F01 § 1 |
| PCG art. 740-1 ; guide pédagogique, compétence 1.2.a | Parité indépendante des règles d'évaluation des apports ; nombre d'actions d'une scission déterminé par la valeur d'échange de la branche | [V] p. 82 ; [S] p. imprimée 163 | F01 § 1 ; `programme/perimetre_ue4.yaml` |
| PCG art. 741-1, 741-2, 742-1, 742-2, 743-1 | Contrôle distinct apprécié au niveau des personnes morales ; apport à l'endroit et à l'envers ; valeur réelle (cas 4) et valeur comptable (cas 3) et leur justification | [V] p. 82-84 | F01 § 2.1 à 2.3 |
| PCG art. 743-3 | Retour aux valeurs réelles si l'actif net comptable ne permet pas la libération du capital | [V] p. 85 | F01 § 2.4 |
| PCG art. 744-1 et 744-2 ; comptes 205 et 1523 | Valeurs réelles des éléments identifiés, figurant ou non au bilan ; fonds commercial ; valeur comptable | [V] p. 85, 134-135 | F01 § 3.1 et § 3.2 |
| BOI-IS-FUS-10-20-40-20 § 170-180 | En valeur comptable, reprise des valeurs brutes et des amortissements | [V] | F01 § 3.2 |
| Corrigé du sujet zéro, Q 2.4 | Impôt différé intégré à l'apport en valeur réelle | [V] p. imprimée 216 | F01 § 3.3 |
| C. com. L. 236-1 al. 3 et L. 236-18 al. 3 ; corrigé du sujet zéro (parité) | Soulte limitée à 10 % de la valeur nominale des actions attribuées ; équité de l'échange | [V] Légifrance ; p. imprimée 214 | F01 § 4 |
| PCG art. 513-5 ; comptes 778 et 503 | Résultat exceptionnel lié à un événement majeur et inhabituel (hypothèse de l'annexe 2.4) ; actions reçues avant attribution (convention de rédaction) | [V] p. 42-43, 148 | F01 § 9 |
| PCG art. 212-9 ; avis CU CNC n° 2000-D | Frais imputés sur la prime, nets d'impôt | [V] p. 15-16 ; recueil p. 103 | F01 § 7 |
| C. civ. art. 1349 | Extinction par confusion de la créance et de la dette réciproques | [V] | F01 § 8 |
| CGI art. 210 B-1, 210 C-1, 210-0 A (I, 2°, et III) ; BOI-IS-FUS-20-30-10 § 70 ; BOI-IS-FUS-20-20 § 10 et 80 | Scission de plein droit sous le régime de faveur : branches complètes, services communs répartis, soulte limitée à 10 % du nominal, motif économique | [V] | F02 § 1 |
| CGI art. 210 A-1 et 210 A-3 ; BOI-IS-FUS-10-10-10 § 1 ; BOI-IS-FUS-10-20-30 § 210 et 330 | Plus-values non imposées chez la société scindée ; engagements des bénéficiaires ; imposition du résultat de la dernière période | [V] | F02 § 2 et § 4 |

---

## DOSSIER 3 – AUDIT (30 points — dont 12 points sur la durabilité)

| Question | Compétence visée | Points |
|---|---|---:|
| 3.1 Paie établie par un expert-comptable et mission du commissaire aux comptes ; ce que le cabinet peut faire pour VEILLANE | `3.1.a` Cadres d'exercice professionnel | 2 |
| 3.2 Démission du prédécesseur ; durée des fonctions du successeur et suppléant ; démarches avant l'acceptation | `3.1.b` Nomination et cessation | 1,5 |
| 3.3 Prestation gratuite et invitations offertes par l'entité ; ancienne gestionnaire de paie affectée à la mission | `3.1.c` Principes déontologiques | 1,5 |
| 3.4 Audit et examen limité : assurance, travaux, conclusion ; cadre de l'examen des comptes semestriels | `3.2.a` Notion d'audit | 1,5 |
| 3.5 Risques du cycle et assertions ; procédures et procédure analytique sur les salaires de base ; extrait de la NEP expert-comptable appliqué à la paie externalisée | `3.2.c` Approche par les risques ; `3.2.d` Démarche d'audit ; `3.1.d` Référentiel normatif (NEP) | 6 |
| 3.6 Droit de communication, entretiens avec les salariés, secret professionnel ; suite d'un refus persistant | `3.2.b` Moyens d'action du CAC | 1,5 |
| 3.7 Congés payés et majorations de décembre : calculs, écritures, caractère significatif, opinion selon la correction, parties du rapport | `3.2.e` Portée des opinions | 2 |
| 3.8 Responsabilité disciplinaire du prédécesseur et du cabinet ; comparaison avec les responsabilités civile et pénale | `3.1.e` Mise en cause de la responsabilité | 2 |
| 3.9 ISSB, EFRAG et GRI ; interopérabilité ; étendue et limites des informations ESRS ; réponse aux demandes | `3.3.a` Contexte et normes de durabilité | 3 |
| 3.10 Impacts, risques et opportunités ; parties prenantes affectées et utilisateurs | `3.3.b` Principes de construction du reporting | 3 |
| 3.11 Objectifs, axes et assurance limitée ; étapes de la démarche ; procédures sur deux données | `3.4.a` Objectifs de la mission et nature de l'assurance ; `3.4.b` Démarche | 4 |
| 3.12 Avis selon la correction ; différences avec l'opinion sur les comptes | `3.4.c` Portée des avis | 2 |
| **Total** | | **30** |

---

### Partie A – Audit des comptes (18 points)

### 3.1 Paie établie par un expert-comptable et mission du commissaire aux comptes (2 pts)

**Cadre de l'expert-comptable (0,75 pt)**
- Nul ne peut exercer l'expertise comptable sans être inscrit au **tableau de l'ordre**, que tiennent les conseils régionaux ; les sociétés d'expertise comptable y sont inscrites [V ord. 45-2138 art. 3, 7, 31, 40]. L'intervention de l'expert-comptable est **contractuelle** : un contrat écrit, la lettre de mission, définit la mission, les droits et obligations des parties et, le cas échéant, sa durée ; les honoraires sont convenus par écrit et fixés librement [V décret 2012-432 art. 151, 158 ; ord. art. 24].
- L'établissement des bulletins de paie et des déclarations sociales entre dans les missions qu'il peut accepter (hypothèse de l'annexe 3.1) ; c'est ce que fait PAYSONNE Conseil depuis 2019. L'expert-comptable **produit** l'information : son indépendance est une indépendance d'esprit envers son client, compatible avec ces travaux, dont il assume la responsabilité [V décret art. 145-146 ; ord. art. 12 ; F10 § 3].

**Cadre du commissaire aux comptes (0,5 pt)**
- Le cabinet exerce une **mission légale** de certification des comptes, confiée par l'assemblée générale ordinaire, sous le contrôle de la **H2A**, qui tient la liste des commissaires aux comptes, adopte les normes et contrôle leur activité [V L. 821-2 III, L. 821-13 I, L. 821-40 I, L. 821-53 ; L. 820-1 I].
- Son **indépendance** est une condition légale d'exercice, appréciée en réalité et en apparence ; il ne peut se prononcer sur des éléments qui résultent de ses propres prestations (autorévision) et exerce sa mission sans **immixtion dans la gestion** [V code de déontologie art. 5 I-II ; L. 821-27 1°, L. 821-54 I].

**Ce que le cabinet peut faire, et ne pas faire (0,75 pt)**
- **Refus de la paie** : établir la paie, c'est produire les rémunérations (44 900 000 €) et les cotisations (12 840 000 €), soit 57 740 000 € de charges de personnel, **75,6 %** du chiffre d'affaires de 2026, et la dette de congés payés. La directrice financière le dit elle-même : le cabinet « vérifierait ses propres calculs ». C'est le **risque d'autorévision** à l'état pur. VEILLANE n'est pas une entité d'intérêt public : il n'y a pas de liste fermée de services interdits, mais le cabinet ne peut accepter ou poursuivre sa mission de certification quand il existe un risque d'autorévision sans mesure de sauvegarde appropriée [V L. 821-28 IV ; code art. 5 II ; A. 821-55 § 23-30]. Aucune sauvegarde ne suffit sur le poste principal des comptes. Le refus vaut pour l'activité d'expertise comptable du cabinet, exercée par la même société [S, application].
- **Ce qu'il peut faire** : certifier les comptes et vérifier les informations en matière de durabilité, missions déjà confiées ; fournir des **prestations** qui ne créent aucun risque d'autorévision ni d'immixtion, après avoir vérifié son indépendance et établi une lettre de mission, par exemple l'examen limité des comptes semestriels (question 3.4) ou des attestations [V L. 821-2 IV, L. 821-3 ; R. 821-195 ; A. 821-55 § 15] ; faire part à la direction, dans le cadre de l'audit, de ses constats sur l'organisation de la paie (rapprochements, revue de la dette de congés), sans la concevoir ni l'exécuter. La paie reste confiée à PAYSONNE Conseil ou à un autre expert-comptable que choisit VEILLANE [S].

**Réponses tolérées**
- La mention qu'une paie établie par le cabinet avant une future désignation obligerait à analyser cette prestation antérieure et à en informer les actionnaires [V code art. 22] : sans pénalité, points complets si le refus est justifié.

**Erreurs fréquentes**
- Admettre la reprise de la paie au motif que le cabinet est aussi expert-comptable, ou appliquer au commissaire aux comptes l'indépendance d'esprit de l'expert-comptable (`JUR-A03`).
- Présenter les instances de chaque profession une à une, ce qui n'est pas demandé (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Ord. 45-2138 art. 3, 7, 12, 24, 31, 40 ; décret 2012-432 art. 145-146, 151, 158 | Tableau de l'ordre ; société d'expertise comptable ; lettre de mission ; indépendance d'esprit | [V] | F09 § 2, § 17 ; F10 § 2.2, § 3 |
| C. com. L. 820-1, L. 821-2, L. 821-3, L. 821-13, L. 821-27, L. 821-28 IV, L. 821-40, L. 821-53, L. 821-54 I ; R. 821-195 | Mission légale ; prestations ; H2A ; autorévision hors entité d'intérêt public ; non-immixtion | [V] ; application : [S] | F09 § 3, § 6 ; F10 § 4.1, § 5 ; F11 § 1 |
| Code de déontologie art. 5, 22 ; A. 821-55 § 15, § 23-30 | Indépendance ; prestations antérieures ; sauvegardes | [V] | F10 § 2.1, § 12 |

### 3.2 Démission du prédécesseur, durée des fonctions et démarches (1,5 pt)

**Démission de M. DOMBREUIL (0,5 pt)**
- Le commissaire aux comptes exerce sa mission jusqu'à son terme ; il peut démissionner pour des **motifs légitimes**, limitativement énumérés, dont la **survenance d'un événement de nature à compromettre le respect des règles** de la profession, notamment son indépendance ; il joint à son dossier les éléments qui le justifient ; il ne peut démissionner pour se soustraire à l'émission de son opinion, ni dans des conditions qui causent un préjudice à l'entité ; il informe la **H2A** des motifs, et l'AMF lorsque l'entité relève de cette autorité [V code art. 28 I, II, IV].
- **Application** : l'entrée du cabinet de M. DOMBREUIL dans le réseau ARDÉLYS, dont un membre établit la paie de VEILLANE, l'aurait conduit à se prononcer sur des charges calculées par son réseau (trois quarts des charges) : risque d'autorévision par le réseau [V code art. 5 II, 29-30 ; S, qualification]. Peu importe que l'événement procède de son propre choix : le texte ne distingue pas [S]. La démission est **légitime**. Elle respecte aussi les autres conditions : rapport sur les comptes de 2024 émis le 10/04/2025, aucun travail engagé sur 2025, démission à la mi-mai, qui laissait l'assemblée de juin désigner un successeur ; information de la H2A et de l'AMF, justificatifs au dossier.

**Durée des fonctions du cabinet et suppléant (0,5 pt)**
- Le commissaire aux comptes nommé en remplacement d'un autre ne demeure en fonction que **jusqu'à l'expiration du mandat de son prédécesseur** [V L. 821-44 al. 2]. M. DOMBREUIL avait été désigné pour les exercices 2022 à 2027 : le cabinet certifie les comptes de 2025, 2026 et 2027, et ses fonctions expirent après l'assemblée de 2028 qui statue sur les comptes de 2027, et non en 2031. La mention « six exercices » de la décision du 26/06/2025 ne peut déroger à la loi [S, effet de la règle légale]. À l'échéance, l'assemblée pourra renouveler le cabinet ou en désigner un autre pour six exercices [V L. 821-44 al. 1].
- Un **suppléant** n'est exigé que si le titulaire est une personne physique ou une société unipersonnelle [V L. 821-40 I al. 3]. Le cabinet, société de sept associés, n'en appelle pas : l'assemblée n'a rien oublié. C'est parce que M. DOMBREUIL exerçait à titre individuel que Mme PRÉVANCHE avait été désignée ; appelée à le remplacer en cas de démission, elle a refusé, d'où la désignation par l'assemblée [V L. 821-40 I al. 3-4 ; S, application].

**Démarches avant l'acceptation (0,5 pt)**
- Avant d'accepter, le cabinet vérifie que la mission est compatible avec les textes et le code, vérifie et consigne son **indépendance** et les **ressources** nécessaires, et réunit les informations sur l'entité (actionnariat, activité, direction) [V code art. 21 ; L. 821-4 II] ; il analyse ses missions et prestations antérieures pour l'entité : aucune ici [V code art. 22].
- Le code impose de **s'assurer auprès du prédécesseur** que son départ ne traduit pas une volonté de l'entité de **contourner les obligations légales** ; à la lettre, il vise le successeur d'un commissaire non renouvelé et le **suppléant** qui succède de plein droit à un titulaire démissionnaire [V code art. 26 I]. Le cabinet, désigné par l'assemblée après le refus de la suppléante, n'est pas visé mot pour mot, mais il prend contact avec M. DOMBREUIL avant d'accepter : les motifs d'une démission sont l'information la plus utile pour la vérification de l'art. 21 [S, application]. Ici, le motif tient au réseau du prédécesseur, non à un différend avec la direction.
- Après l'acceptation, le prédécesseur démissionnaire lui donne accès à **toutes les informations et à tous les documents pertinents** [V L. 821-44 al. 3] ; le cabinet prend connaissance de son dossier de travail pour contrôler le bilan d'ouverture [V NEP bilan d'ouverture § 06] (question 3.8).

**Réponses tolérées**
- Une démarche auprès du prédécesseur présentée comme une obligation du code, sans la nuance sur son champ, si son objet (motifs du départ, contournement des obligations légales) est exact : points complets.

**Erreurs fréquentes**
- Retenir un mandat de six exercices pour le successeur d'un commissaire démissionnaire (`JUR-A05`).
- Exiger un suppléant d'une société de commissaires aux comptes pluripersonnelle (`JUR-A01`).
- Développer les formalités de la désignation, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 21, 22, 26, 28 ; art. 5, 29-30 | Acceptation ; prestations antérieures ; succession ; démission ; réseau | [V] ; application : [S] | F09 § 3.7, § 12, § 19 ; F10 § 4.1 |
| C. com. L. 821-4 II, L. 821-40 I, L. 821-44 | Indépendance et ressources ; suppléant ; durée des fonctions du successeur ; accès aux documents | [V] | F09 § 3.4-3.5, § 12, § 19 |
| NEP bilan d'ouverture § 06 | Dossier du prédécesseur | [V] | F11 § 15.1 |

### 3.3 Proposition du directeur général et affectation de Mme LAVERGNE (1,5 pt)

**Prestation gratuite et invitations (0,75 pt)**
- **Qualification (0,5 pt)** : il est interdit au commissaire aux comptes, à la société de commissaires aux comptes, aux membres de sa direction et aux personnes qui participent à la mission de **solliciter ou d'accepter des cadeaux**, pécuniaires ou non, ou des **faveurs** de l'entité dont il certifie les comptes, au-delà d'un plafond fixé par arrêté [V code art. 14 I ; L. 821-31 II]. La sécurité gratuite de la soirée du cabinet (4 200 €) est une faveur accordée à la société elle-même ; les six invitations (1 500 €) sont des cadeaux à l'équipe ; l'un et l'autre dépassent le plafond (hypothèse de l'annexe 3.3). Une prestation fournie sans prix n'est pas non plus une opération courante conclue aux conditions du marché : elle crée entre l'entité et le cabinet une relation d'affaires, lien professionnel incompatible avec la mission [V code art. 34 I-II ; S, qualification]. Ce « geste entre partenaires » menace l'impartialité et l'apparence d'indépendance aux yeux d'un tiers objectif [V code art. 4, 5 ; A. 821-55 § 03, § 11].
- **Conduite (0,25 pt)** : le cabinet **décline** les deux offres par écrit, en rappelant la règle à M. GRANDVAUX, informe l'équipe et documente l'analyse [V A. 821-55 § 41-43]. Il confie la sécurité de sa soirée à un autre prestataire [S].

**Affectation de Mme LAVERGNE (0,75 pt)**
- **Qualification (0,5 pt)** : les personnes qui ont été salariées d'une entité ne peuvent y exercer des missions de commissaire aux comptes moins de **cinq ans** après la fin de leurs fonctions [V L. 821-33 al. 1]. Mme LAVERGNE, assistante, n'est pas commissaire aux comptes : le texte vise ceux qui exercent la mission, mais il signale le risque [S, lecture du texte]. Surtout, de janvier à juin 2026, elle contrôlait les heures et préparait les éléments variables transmis à PAYSONNE Conseil : elle vérifierait, sur l'exercice audité, ses **propres travaux** (autorévision) [V code art. 5 II]. Ses « excellentes relations » avec la directrice des ressources humaines créent un risque de **familiarité**, contraire à l'impartialité et à l'esprit critique [V code art. 4, 6 ; S, terme]. Son contrat de travail a pris fin : il n'y a plus de lien professionnel au sens de l'art. 34, mais la situation reste à risque [V code art. 34 I, III].
- **Conduite (0,25 pt)** : le cabinet **n'affecte pas** Mme LAVERGNE au dossier de VEILLANE, au moins pour l'exercice 2026, ni sur la paie ni sur les autres cycles, sans accès au dossier ; il documente l'analyse et la sauvegarde retenue [V A. 821-55 § 23-30, § 41-43 ; S, choix de la sauvegarde]. Le gain de temps invoqué par le chef de mission est précisément le signe du risque.

**Réponses tolérées**
- L'application directe de L. 821-33 à Mme LAVERGNE, si la conclusion (exclusion de l'équipe) est la même : points complets en qualification.
- L'admission de Mme LAVERGNE sur d'autres cycles que la paie, sous la supervision d'un autre membre de l'équipe, si le risque d'autorévision est identifié : 0,25 pt sur 0,5 en qualification.

**Erreurs fréquentes**
- Accepter les invitations au motif qu'elles sont d'usage, ou ne voir dans la prestation gratuite qu'un cadeau à l'équipe (`JUR-A05`).
- Conclure à la démission du cabinet alors qu'un refus et une sauvegarde suffisent (`JUR-A05`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Code de déontologie art. 4, 5, 6, 14, 34 ; C. com. L. 821-31 II | Impartialité ; indépendance ; esprit critique ; cadeaux et faveurs ; liens professionnels | [V] ; qualification : [S] | F10 § 2.1, § 4.1, § 14, § 15 |
| C. com. L. 821-33 | Ancien salarié de l'entité | [V] ; lecture : [S] | F10 § 4.1, § 15 |
| A. 821-55 § 03, § 11, § 23-30, § 41-43 | Tiers objectif ; sauvegardes ; documentation | [V] | F10 § 12 |

### 3.4 Audit des comptes et examen limité (1,5 pt)

- **Audit des comptes (0,5 pt)** : le commissaire aux comptes certifie, en justifiant de ses appréciations, que les comptes annuels sont **réguliers et sincères et donnent une image fidèle** ; il formule une opinion après un audit [V L. 821-53 ; NEP principes § 01]. Il obtient une **assurance raisonnable**, élevée mais non absolue, que les comptes pris dans leur ensemble ne comportent pas d'anomalies significatives, et l'exprime sous une forme **positive** [V NEP principes § 08].
- **Examen limité (0,5 pt)** : les procédures sont **moins étendues** ; elles consistent **essentiellement en entretiens avec la direction et en procédures analytiques**, complétés par le rapprochement des comptes avec les documents comptables et la lecture des procès-verbaux [V NEP examen limité § 07-08, § 19, § 21]. L'assurance obtenue, **moins élevée**, est une **assurance modérée** : la conclusion indique que le commissaire aux comptes **n'a pas relevé** d'anomalies significatives (forme **négative**) ; elle peut être sans réserve, avec réserve, défavorable, ou une impossibilité de conclure [V § 09-10, § 29]. Le président se trompe : l'examen limité n'apporte pas « la même assurance que la certification » ; il ne permet pas de dire que les comptes semestriels sont « certifiés », comme le souhaite le fonds. Seul un audit des comptes semestriels donnerait une assurance raisonnable.
- **Cadre (0,5 pt)** : aucune disposition légale ou réglementaire n'impose cet examen (hypothèse de l'annexe 3.4) : ce n'est pas une mission, mais une **prestation**, fournie sur la base d'une **lettre de mission** [V L. 821-2 III-IV, L. 821-3 ; R. 821-195]. La NEP examen limité ne vise que les examens réalisés en application de dispositions légales ou réglementaires [V § 01] : le cabinet peut s'y référer dans sa lettre de mission et en appliquer les principes [S]. Avant d'accepter, il vérifie qu'il peut réaliser la prestation de façon indépendante et impartiale [V A. 821-55 § 15] : examiner des comptes qu'il n'a pas établis ne crée pas de risque d'autorévision. Ses honoraires sont fixés en rapport avec les diligences [V code art. 12].

**Réponses tolérées**
- Le rapprochement avec un audit contractuel, si le candidat conclut que la demande du conseil vise un examen limité, d'assurance moindre : 0,25 pt sur 0,5 en cadre.

**Erreurs fréquentes**
- Présenter l'examen limité comme une certification allégée ou l'assurance modérée comme une garantie (`JUR-A01`).
- Faire de la typologie des missions le thème de la réponse, sans l'appliquer à la demande du conseil (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-53 ; NEP principes § 01, § 08 | Certification ; assurance raisonnable | [V] | F11 § 1.1 |
| NEP examen limité § 01, § 07-10, § 19, § 21, § 29 | Champ ; procédures ; assurance modérée ; conclusions | [V] | F11 § 24.2 |
| C. com. L. 821-2, L. 821-3 ; R. 821-195 ; A. 821-55 § 15 ; code art. 12 | Prestation ; lettre de mission ; indépendance ; honoraires | [V] ; application : [S] | F10 § 5, § 12 ; F11 § 1.2 |

### 3.5 Cycle personnel et paie (6 pts)

**a. Risques et assertions (2,5 pts)**
- **Risque inhérent élevé (0,5 pt)** : charges de personnel de 57 740 000 €, soit 75,6 % du chiffre d'affaires et 144 fois le seuil de signification ; 1 480 salariés sur 410 sites, 640 contrats courts ; données saisies de façon décentralisée par les chefs de site ; calculs externalisés ; changements en 2026 (accord sur les congés payés, clôture des plannings au 20, départ de la gestionnaire de paie) [V NEP risques § 02 ; S, application].
- **Six situations (1,5 pt ; 0,25 pt par situation rattachée au bon risque et à la bonne assertion)** :

| Situation | Risque | Assertions |
|---|---|---|
| 1. Heures majorées | Heures de nuit payées sans avoir été réalisées, ou majorations mal calculées (heures payées supérieures de 6 % aux heures facturées sur quatre sites) | Charges de personnel : **réalité**, **mesure** |
| 2. Contrats courts | Agents fictifs ou payés en double ; indemnités de fin de contrat oubliées | Charges : **réalité** ; dettes : **exhaustivité** |
| 3. Primes de panier et d'habillage | Primes versées pour des postes non réalisés ou non éligibles | Charges : **réalité**, **mesure** |
| 4. Congés payés | Dette calculée sans la moyenne des majorations prévue par l'accord du 15/03/2026 | Dettes : **évaluation et imputation** ; charge de congés : **mesure** |
| 5. Cotisations et réductions | Paramétrage des réductions erroné ou périmé ; écart de 118 000 € avec les DSN | Cotisations : **mesure**, **exhaustivité** ; dettes sociales : **exhaustivité** |
| 6. Majorations de décembre | Heures du 21 au 31/12/2026, nuits de fête comprises, rattachées à 2027 | Charges : **séparation des exercices** ; dettes : **exhaustivité** |

- **Risque lié au contrôle élevé (0,5 pt)** : les chefs de site saisissent et modifient seuls les plannings, sans validation ; aucun rapprochement entre les heures payées et les heures facturées ; vérification des heures par sondage seulement depuis le départ de la gestionnaire de paie ; journal de paie enregistré sans rapprochement avec les DSN ; dette de congés jamais revue ; PAYSONNE Conseil n'est chargée d'aucun contrôle des heures. Le cabinet ne peut s'appuyer sur les procédures de l'entité : **procédures de substance étendues** à la clôture [V NEP principes § 11, § 13 ; NEP risques § 02].

**b. Procédures et procédure analytique (2 pts)**
- **Procédures (1,25 pt ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 1,25 pt)** :
  - **rapprochement** des heures payées, par site et par mois, avec les plannings, les relevés d'heures signés et les heures facturées aux clients, en commençant par les quatre sites en écart : réalité et mesure des majorations ;
  - **tests sur un échantillon d'agents** tirés du journal de paie : contrat, carte professionnelle, relevés d'heures, recalcul du bulletin (salaire de base, majorations, primes de panier et d'habillage) ; et, en sens inverse, d'agents tirés des plannings vers la paie [V NEP sélection § 04, § 07] : réalité, mesure, exhaustivité ;
  - **contrats courts** : rapprochement des entrées et sorties avec les contrats et les DSN, recherche de doublons (même identité ou même compte bancaire pour deux agents) : réalité ;
  - **rapprochement des DSN** avec le journal de paie et les comptes 641, 645 et 431, et analyse de l'écart de 118 000 € ; recalcul des réductions de cotisations sur un échantillon de bulletins : mesure, exhaustivité ;
  - **contrôle de la dette de congés payés** : lecture de l'accord du 15/03/2026, rapprochement des jours acquis avec les compteurs, recalcul de l'indemnité journalière, majorations comprises : évaluation ;
  - **examen de la paie de janvier 2027** et des plannings du 21 au 31/12/2026 : séparation des exercices, exhaustivité des dettes ;
  - **déclarations écrites** de la direction sur l'exhaustivité des dettes sociales et les éléments transmis à PAYSONNE Conseil [V NEP déclarations § 1-4].
- **Procédure analytique de substance sur les salaires de base (0,75 pt)** :
  - **Attente (0,25 pt)** : agents en contrat à durée indéterminée : 1 080 × (6 × 2 000 + 6 × 2 050) = **26 244 000 €** ; agents en contrats courts : 150 × 24 300 = **3 645 000 €** ; encadrement et fonctions support : 180 × (6 × 3 400 + 6 × 3 468) = **7 417 440 €** ; attente totale **37 306 440 €** (salaires revalorisés au 01/07/2026 : 2 000 × 1,025 = 2 050 € ; 3 400 × 1,02 = 3 468 €).
  - **Écart (0,25 pt)** : 37 420 000 − 37 306 440 = **113 560 €**, soit **0,3 %** de l'attente et 0,38 fois l'écart acceptable de 300 000 € : écart acceptable.
  - **Conclusion et portée (0,25 pt)** : la procédure **corrobore les salaires de base**, sous réserve de la fiabilité des données utilisées (effectifs en ETP rapprochés des DSN, taux de revalorisation lus dans l'accord de branche) [V NEP procédures analytiques § 05, § 07 ; NEP éléments probants § 6]. Elle ne couvre ni les majorations, ni les primes, ni les congés payés, ni les cotisations, qui concentrent les risques des situations 1 à 6 : les tests de détail restent nécessaires.

**c. Application de l'extrait de la NEP expert-comptable (1,5 pt)**
- **Prise de connaissance et contact (0,5 pt)** : le cabinet **analyse la nature et l'étendue de la mission** de PAYSONNE Conseil [V NEP expert-comptable § 3] : elle calcule les bulletins, les cotisations et réductions, les DSN et la dette de congés, mais **ne contrôle pas les heures** que lui transmet VEILLANE. Il **prend contact** avec elle pour connaître le contenu de sa mission et se fait communiquer ses travaux (paramétrage des taux et des réductions, calcul de la dette de congés) [V § 4] ; la norme s'inscrit dans le droit d'information du commissaire aux comptes auprès des tiers qui ont accompli des opérations pour le compte de l'entité [V § 1 ; L. 821-61 al. 2].
- **Appréciation et procédures supplémentaires (0,75 pt)** : il apprécie si ces travaux constituent des **éléments suffisants et appropriés** [V § 5]. Ils peuvent l'être pour l'exactitude arithmétique des bulletins et des cotisations, si le paramétrage est à jour ; ils ne le sont pas pour la **réalité des heures**, que PAYSONNE Conseil reprend telles quelles, ni pour la **dette de congés**, calculée sans l'accord de 2026. Le cabinet détermine donc les **procédures supplémentaires** [V § 6] : tests sur les données d'entrée (plannings, relevés signés, heures facturées), recalcul d'un échantillon de bulletins et de réductions, revue du paramétrage, recalcul de la dette de congés, rapprochement des DSN et de la comptabilité (question b).
- **Rapport et documentation (0,25 pt)** : l'opinion **ne fait pas référence** aux travaux de PAYSONNE Conseil, qui ne sont que des éléments collectés à l'appui des conclusions du cabinet, seul responsable de son opinion ; le cabinet **documente** dans son dossier les travaux qu'il utilise [V § 7-8].

**Réponses tolérées**
- En a., le rattachement de la situation 1 à un risque de fraude (heures fictives), si l'assertion de réalité est retenue.
- En b., l'attente calculée par catégorie avec un salaire annuel moyen (24 300 € et 41 208 € par ETP), si les montants sont justes.

**Erreurs fréquentes**
- Recopier l'extrait de norme sans l'appliquer à PAYSONNE Conseil, ou en déduire que le cabinet peut s'en remettre au prestataire (`JUR-A06`).
- Conclure de la procédure analytique que toute la masse salariale est correcte (`JUR-A05`).
- Confondre réalité (flux) et existence (solde), ou séparation des exercices et exhaustivité (`JUR-A01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP principes § 11-13 ; NEP risques § 02 | Risque inhérent, risque lié au contrôle | [V] ; application : [S] | F11 § 4.1 |
| NEP éléments probants § 6, § 9-10 ; NEP sélection § 04, § 07 ; NEP déclarations § 1-4 | Assertions ; techniques ; sélection ; déclarations | [V] | F11 § 4.3, § 6, § 21 |
| NEP procédures analytiques § 03-07 | Procédure analytique de substance ; montant attendu et écart acceptable | [V] | F11 § 18.1 |
| NEP expert-comptable § 1, § 3-8 ; C. com. L. 821-61 al. 2 | Utilisation des travaux d'un expert-comptable ; informations auprès des tiers | [V] | F11 § 24.1, § 23.2 |

### 3.6 Réponse de la directrice des ressources humaines (1,5 pt)

- **Droit de communication et entretiens (0,5 pt)** : le commissaire aux comptes opère à toute époque les vérifications qu'il juge opportunes et peut se faire **communiquer sur place toutes les pièces utiles**, notamment les contrats ; ses collaborateurs ont les mêmes droits d'investigation [V L. 821-60]. Les contrats, cartes professionnelles, relevés signés et justificatifs d'absence sont les pièces qui établissent la réalité des salaires payés : un tableau anonymisé, établi par la direction, n'en est pas l'équivalent, car il ne permet pas de rattacher les paiements à des personnes et à des pièces [V NEP éléments probants § 6 ; S, application]. Les vérifications comprennent les **demandes d'information** auprès des personnes de l'entité, dont les chefs de site [V NEP éléments probants § 10 ; S, portée de L. 821-60]. PAYSONNE Conseil peut être interrogée comme tiers (question 3.5 c), mais cela ne dispense pas VEILLANE de communiquer ses propres pièces [V L. 821-61 al. 2].
- **Secret (0,5 pt)** : le secret professionnel ne peut être opposé au commissaire aux comptes dans sa mission, **sauf par les auxiliaires de justice** [V L. 821-61 al. 3] ; la confidentialité des données personnelles, que l'entité doit protéger, n'est pas un secret qui lui serait opposable [S]. Le commissaire aux comptes, ses collaborateurs et ses experts sont eux-mêmes **astreints au secret professionnel** pour tout ce qu'ils apprennent dans leur mission, sous les peines prévues par le code pénal [V L. 821-35 al. 1, L. 821-7 dernier al.] : les données consultées restent protégées. Le cabinet consulte les dossiers sur place et ne conserve que les éléments nécessaires à ses conclusions [S].
- **Suite d'un refus persistant (0,5 pt)** : le cabinet rappelle ses droits à la directrice des ressources humaines, puis porte la difficulté devant le président-directeur général et le conseil d'administration [V L. 821-63 I ; S, démarche]. Si le refus persiste et qu'aucune autre procédure ne permet de collecter des éléments suffisants sur la réalité des rémunérations, c'est une **limitation** : réserve pour limitation si ses incidences sont circonscrites, sinon **impossibilité de certifier**, l'enjeu portant sur les trois quarts des charges [V NEP rapport § 11, § 14]. Le refus de communiquer sur place les pièces utiles, par un dirigeant ou une personne au service de l'entité, est en outre un **délit d'obstacle** (cinq ans d'emprisonnement, 75 000 € d'amende) [V L. 821-6 3°]. En l'espèce, la difficulté a été levée par le président-directeur général (annexe 3.8).

**Réponses tolérées**
- La qualification des entretiens avec les chefs de site comme une technique de contrôle (demande d'information) plutôt que comme un droit : points complets si le refus d'y répondre est traité comme une entrave.

**Erreurs fréquentes**
- Admettre que la protection des données personnelles fait obstacle au droit de communication, ou oublier le secret auquel le cabinet est tenu (`JUR-A01`).
- Développer les règles de protection des données personnelles, qui ne sont pas au programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-60, L. 821-61, L. 821-63 I | Communication sur place ; collaborateurs ; tiers ; secret non opposable ; communication aux organes | [V] ; application : [S] | F09 § 5 ; F11 § 2, § 5 |
| C. com. L. 821-35, L. 821-7 ; L. 821-6 3° | Secret du commissaire aux comptes ; délit d'obstacle | [V] | F10 § 7 ; F11 § 13.3 |
| NEP éléments probants § 6, § 10 ; NEP rapport § 11, § 14 | Fiabilité ; demande d'information ; limitation | [V] | F11 § 6, § 8.1 |

### 3.7 Anomalies, écritures et opinion (2 pts)

**Calcul des anomalies (0,5 pt ; 0,25 pt par anomalie)**
- **Dette de congés payés** : 31 800 jours × (104 − 92) = **381 600 €**, plus 40 % de charges sociales, 152 640 € : **534 240 €** de dettes manquantes au 31/12/2026 (les 9 400 jours acquis avant le 01/01/2026 sont justes). La dette s'élève à 4 172 000 € au lieu de 3 790 400 €, et les charges sociales à 1 668 800 € au lieu de 1 516 160 €.
- **Majorations du 21 au 31/12/2026** : 180 000 € plus 40 %, 72 000 € : **252 000 €** de charges de 2026 non rattachées.

**Écritures de correction au 31/12/2026 (0,5 pt ; 0,25 pt par écriture)**

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 6412 | Congés payés | 381 600 | |
| | 645 | Cotisations de sécurité sociale et de prévoyance | 152 640 | |
| | 4282 | Dettes provisionnées pour congés à payer | | 381 600 |
| | 4382 | Charges sociales sur congés à payer | | 152 640 |

Libellé : complément de la dette de congés payés, accord du 15/03/2026 (écriture X1, équilibrée à 534 240 €).

| Date | Compte | Intitulé | Débit | Crédit |
|---|---|---|---:|---:|
| 31/12/2026 | 6411 | Salaires, appointements | 180 000 | |
| | 645 | Cotisations de sécurité sociale et de prévoyance | 72 000 | |
| | 4286 | Personnel – Autres charges à payer | | 180 000 |
| | 4386 | Organismes sociaux – Autres charges à payer | | 72 000 |

Libellé : majorations des heures du 21 au 31/12/2026 payées en janvier 2027 (écriture X2, équilibrée à 252 000 €). Après les deux corrections, le résultat avant effet d'impôt est de 2 140 000 − 534 240 − 252 000 = **1 353 760 €**.

**Caractère significatif (0,25 pt)** : 534 240 / 400 000 = **1,34** fois le seuil : significative à elle seule ; 252 000 / 400 000 = **0,63** fois ; ensemble, 786 240 €, **1,97** fois le seuil, et 2,06 fois avec les 36 000 € des autres cycles. Les anomalies s'apprécient individuellement et en cumul [V NEP anomalies § 14] ; toutes deux sous-évaluent les dettes et surévaluent le résultat (36,7 % du résultat publié).

**Opinion selon la décision de la direction (0,5 pt)**
- **Les deux anomalies sont corrigées** : il ne reste que 36 000 € (0,09 fois le seuil) : **certification sans réserve** ; le cabinet communique les anomalies non corrigées et obtient une déclaration écrite à laquelle en est joint l'état [V NEP anomalies § 15-17 ; NEP rapport § 08].
- **Seules les majorations sont corrigées** (position du président-directeur général) : il reste 534 240 + 36 000 = 570 240 € (**1,43** fois le seuil) : désaccord significatif, dont l'incidence est circonscrite à la dette de congés et quantifiée : **certification avec réserve pour désaccord** [V NEP rapport § 09-10]. L'argument du paiement en 2027 ne tient pas : les congés acquis en 2026 sont une dette de 2026 [V PCG art. 1214-42].
- **Aucune anomalie n'est corrigée** : 822 240 € (**2,06** fois le seuil) : deux désaccords significatifs, circonscrits et chiffrés : **certification avec réserve pour désaccord**, motivée par les deux points. Ce n'est pas un refus de certifier : les incidences portent sur deux postes identifiés et la réserve chiffrée suffit au lecteur [V NEP rapport § 09-10, § 12-13 ; S, qualification].

**Parties du rapport, dernier cas (0,25 pt)** : la partie « **Opinion avec réserve** » indique que, sous ces réserves, les comptes sont réguliers et sincères et donnent une image fidèle ; la partie « **Fondement de l'opinion avec réserve** » expose les deux motifs et leur incidence (dettes sociales sous-évaluées et résultat surévalué de 534 240 € et de 252 000 €). Les motifs sont communiqués au préalable au conseil d'administration ; le rapport est destiné à l'assemblée générale [V NEP rapport § 06, § 18 ; R. 821-180].

**Réponses tolérées**
- Les charges sociales de l'écriture X2 au compte 4382 ou 4386 et la dette de majorations au compte 421, si le libellé est juste : points complets.
- Une seule écriture regroupant les deux corrections, si les comptes et les montants sont justes : points complets en écritures.
- Un refus de certifier dans le dernier cas, motivé par le cumul des anomalies sur le poste principal des comptes : 0,25 pt sur 0,5 en opinion.

**Erreurs fréquentes**
- Oublier les charges sociales, ou les appliquer aux 9 400 jours acquis avant le 01/01/2026 (`JUR-F02`).
- Conclure à une certification sans réserve quand seule l'anomalie inférieure au seuil est corrigée (`JUR-A02`).
- Écriture sans libellé ou sans numéro de compte (`JUR-F03`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| NEP anomalies § 14-17 ; NEP caractère significatif § 9 | Appréciation individuelle et cumulée ; déclaration écrite | [V] | F11 § 4.2, § 14.1 |
| NEP rapport § 06, § 08-10, § 12-13, § 18 ; R. 821-180 | Opinions ; parties du rapport | [V] | F11 § 8 |
| PCG art. 1214-42 ; liste des comptes | Congés à payer (428, 6412) ; 645, 6411, 4282, 4286, 4382, 4386 | [V] | F11 § 18.2 |

### 3.8 Responsabilité disciplinaire après le contrôle d'activité (2 pts)

- **Faute disciplinaire et normes (0,5 pt)** : constitue une faute disciplinaire tout **manquement aux conditions légales d'exercice** de la profession, toute **négligence grave** et tout fait contraire à la probité ou à l'honneur [V L. 821-70 I]. Le commissaire aux comptes se conforme aux **normes homologuées** [V L. 821-11 I] ; la NEP documentation impose un dossier qui permette à un auditeur expérimenté, extérieur à la mission, de comprendre les procédures mises en œuvre, les éléments collectés, leurs résultats et les conclusions, avec l'identité de l'exécutant et la date des travaux [V NEP documentation § 04, § 08].
- **M. DOMBREUIL (0,5 pt)** : son dossier de 2024 sur la paie (une ligne de conclusion et le journal de paie) ne décrit ni procédures, ni éléments sélectionnés, ni résultats, ni auteur, ni date : **manquement à la NEP documentation**, sur un cycle qui représente les trois quarts des charges ; rien ne prouve que l'opinion reposait sur des éléments suffisants, ce qui peut caractériser une **négligence grave** [S, qualification]. Il exerce toujours : sa démission du mandat de VEILLANE n'empêche pas une sanction pour des faits commis pendant ce mandat [V R. 821-209 ; F09 § 3.7].
- **Le cabinet COLLÉVAN (0,5 pt)** : pour le bilan d'ouverture, il devait prendre connaissance du dossier du prédécesseur ; la certification sans réserve des comptes de 2024 n'est qu'une **présomption**, et, s'il n'obtient pas des travaux du prédécesseur des éléments suffisants, il met en œuvre ses propres procédures, au besoin complémentaires [V NEP bilan d'ouverture § 06-07, § 09-11]. S'appuyer sur un dossier vide sans aucune procédure est un **manquement à cette norme**, plus limité : ses travaux de 2025 sont documentés, et la paie de 2025 (congés de 2024 pris en 2025) pouvait couvrir une partie du solde d'ouverture [S, qualification]. La sanction peut viser la société et la signataire, Mme VAUCHELLE ; une sanction légère paraît plus probable qu'une interdiction [S]. Le cabinet complète son approche et sa documentation dès 2026.
- **Sanctions et distinction (0,5 pt)** : la H2A peut prononcer l'**avertissement**, le **blâme**, l'**interdiction d'exercer** tout ou partie des missions pour trois ans au plus, la **radiation**, le retrait de l'honorariat, et, en outre, la publication d'une déclaration sur le rapport, l'interdiction de fonctions de direction pour trois ans au plus et une **sanction pécuniaire** (250 000 € au plus pour une personne physique ; pour une société, un million d'euros ou la moyenne annuelle des honoraires de la mission) [V L. 821-71]. La responsabilité disciplinaire sanctionne le **manquement aux règles de la profession**, dans l'intérêt de la qualité de l'audit, **sans qu'un préjudice soit nécessaire**. La responsabilité **civile** répare un **dommage** causé à l'entité ou aux tiers par des fautes et négligences : elle suppose une faute, un **préjudice** et un lien de causalité, absents ici tant qu'aucune anomalie des comptes de 2024 ou de 2025 n'a causé de dommage [V L. 821-37 ; S, conditions]. La responsabilité **pénale** suppose une **infraction** définie par la loi (usage illégal du titre, exercice malgré une incompatibilité, informations mensongères sur la situation de l'entité données ou confirmées, violation du secret professionnel), punie d'amende ou d'emprisonnement : un défaut de documentation n'en est pas une [V L. 821-7, L. 821-8, L. 821-9 ; S, application].

**Réponses tolérées**
- La qualification du manquement de M. DOMBREUIL comme simple manquement aux conditions légales d'exercice, sans négligence grave : points complets si la faute disciplinaire est retenue.
- La mention que les faits sont recherchés sur une période limitée, en une phrase : ni points ni pénalité.
- Pour le cabinet, la conclusion à une simple insuffisance de documentation, sans faute disciplinaire caractérisée, si elle s'appuie sur les travaux de 2025 qui couvraient une partie du solde d'ouverture (NEP bilan d'ouverture § 10) : points complets.

**Erreurs fréquentes**
- Exiger un préjudice pour la responsabilité disciplinaire, ou confondre sanction disciplinaire et dommages-intérêts (`JUR-A01`).
- Décrire la saisine, l'enquête ou la commission qui statue, hors programme (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-11 I, L. 821-70 I, L. 821-71 ; R. 821-209 ; L. 820-14 | Normes obligatoires ; faute disciplinaire ; sanctions ; démission ; contrôle d'activité | [V] ; qualification : [S] | F09 § 3.7, § 7.2, § 16, § 19 |
| NEP documentation § 04, § 08 ; NEP bilan d'ouverture § 06-07, § 09-11 | Documentation ; bilan d'ouverture | [V] | F11 § 7, § 15.1, § 24.3 |
| C. com. L. 821-37, L. 821-7, L. 821-8, L. 821-9 | Responsabilité civile ; infractions | [V] ; conditions : [S] | F09 § 7.1, § 7.3 |

---

### Partie B – Durabilité (12 points)

### 3.9 Référentiels, interopérabilité et informations à publier (3 pts)

**Acteurs et objectifs (1,25 pt)**
- **ISSB et normes IFRS de durabilité (0,5 pt)** : l'ISSB, conseil de normalisation de la **Fondation IFRS**, a publié en 2023 IFRS S1 (exigences générales) et IFRS S2 (climat), qui reprennent les recommandations de la TCFD. Ses normes s'adressent aux **investisseurs** : elles portent sur les risques et opportunités liés à la durabilité qui peuvent affecter les flux de trésorerie, l'accès au financement ou le coût du capital, selon une approche de **matérialité financière** [S, ifrs.org ; F12 § 1].
- **EFRAG et ESRS (0,5 pt)** : l'EFRAG, conseiller technique de la Commission européenne, prépare les projets d'ESRS, que la Commission adopte par actes délégués [V règlement délégué 2026/1563, considérant 3]. Les ESRS reposent sur la **double matérialité** : impacts de l'entreprise sur les personnes et l'environnement, et effets financiers des enjeux de durabilité sur l'entreprise [V ESRS 1 (2026) § 2, § 35].
- **GRI (0,25 pt)** : la Global Reporting Initiative publie des normes universelles, sectorielles et thématiques, centrées sur les **impacts** de l'organisation sur l'économie, l'environnement et les personnes (matérialité d'impact) [S, globalreporting.org].

**Interopérabilité (0,5 pt)** : l'EFRAG et la GRI ont déclaré, fin août-début septembre 2023, que leurs définitions et indicateurs d'impact sont alignés ou étroitement alignés : une entreprise qui publie selon les ESRS est considérée comme publiant « en référence » aux normes GRI, et un index d'interopérabilité a été publié [V page EFRAG ; S, index]. La Fondation IFRS et l'EFRAG ont publié en mai 2024 un guide d'interopérabilité : la matérialité financière des ESRS est alignée sur celle d'IFRS S1, avec une forte convergence sur le climat [S]. La formule de synthèse : **GRI = impact**, **ISSB = financier**, **ESRS = les deux** [S].

**Étendue, limites et réponses au président (1,25 pt)**
- **Étendue et limites (0,5 pt)** : en déclarant son état conforme aux ESRS, VEILLANE publie les informations générales et, pour chaque thème matériel, ses politiques, actions, indicateurs et cibles, ou indique qu'elle n'en a pas, de façon que l'état donne une **image fidèle** de tous ses impacts, risques et opportunités matériels [V ESRS 1 (2026) § 3, § 25, § 29 ; ESRS 2 § 38-39]. Elle **ne publie pas** les informations sans importance matérielle [V ESRS 1 (2026) § 24].
- **« Trois rapports ? » (0,25 pt)** : non. Un seul état conforme aux ESRS couvre les deux matérialités. L'**index GRI** demandé par l'établissement public peut y être joint comme **information supplémentaire** tirée d'un autre référentiel, clairement signalée comme ne résultant pas de l'évaluation de la matérialité et sans obscurcir les informations matérielles [V ESRS 1 (2026) § 107, § 109], ou figurer dans un document distinct ; l'emploi, la santé et la sécurité, la formation et la sous-traitance sont d'ailleurs, chez VEILLANE, des thèmes probablement matériels, déjà traités dans l'état [S].
- **« Abandonner les ESRS ? » (0,25 pt)** : rien ne l'impose. La matérialité financière des ESRS rejoint celle de l'ISSB, mais une déclaration de conformité aux normes de l'ISSB suppose d'en respecter les exigences propres, notamment celles d'IFRS S2 sur le climat : VEILLANE peut répondre au fonds par des informations supplémentaires, signalées comme telles, ou par un rapport distinct, sans renoncer aux impacts que le fonds juge secondaires [V ESRS 1 (2026) § 108-109 ; S, interopérabilité].
- **« Ce que chacun nous demande ? » (0,25 pt)** : non plus. Une publication volontaire permet de choisir son référentiel, non de choisir ses thèmes à l'intérieur des ESRS : la déclaration de conformité impose de traiter **tous les thèmes matériels**, y compris les impacts sur les agents, même si le fonds s'y intéresse peu [V ESRS 1 (2026) § 24, § 29 ; S, application].

**Réponses tolérées**
- La présentation de l'ISSB et de la GRI sans dates, si leur objet et leur matérialité sont exacts.
- Le vocabulaire des ESRS de 2023 (« double importance », « incidences », « déclaration relative à la durabilité »).

**Erreurs fréquentes**
- Affirmer qu'un état conforme aux ESRS vaut conformité aux normes de l'ISSB et de la GRI sans nuance, ou inversement que ces référentiels s'excluent (`JUR-A05`).
- Développer le contenu d'IFRS S2 ou d'une norme thématique, ce qui n'est pas demandé (`JUR-F01`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| Pages ISSB, GRI, EFRAG ; règlement délégué 2026/1563, considérants 2-3 | Acteurs ; matérialités ; interopérabilité | [S] ; EFRAG et considérants : [V] | F12 § 1 |
| ESRS 1 (2026) § 2-3, § 24-25, § 29, § 35, § 107-109 ; ESRS 2 § 38-39 | Double matérialité ; image fidèle ; informations matérielles ; informations supplémentaires | [V] ; application : [S] | F12 § 2, § 6, § 17 |

### 3.10 Impacts, risques et opportunités ; parties prenantes (3 pts)

**Notions (0,5 pt)** : un **impact** est un effet, positif ou négatif, réel ou potentiel, de l'entreprise sur les personnes ou l'environnement, lié à ses activités propres et à sa chaîne de valeur ; un **risque** ou une **opportunité** est un effet financier, actuel ou attendu, sur la situation, les performances, les flux de trésorerie, l'accès au financement ou le coût du capital ; il peut découler d'un impact, d'une **dépendance** à l'égard de ressources humaines ou naturelles, ou d'autres facteurs [V ESRS 1 (2026) § 39-41, § 47-48].

**Application au contexte (1,5 pt ; 0,25 pt par élément correctement qualifié, dans la limite de 1,5 pt)**

| Élément du contexte | Impact | Risque ou opportunité |
|---|---|---|
| Travail de nuit | Impact négatif réel sur la santé des agents (troubles du sommeil des plus anciens) | Risque : absentéisme, inaptitudes, difficultés de recrutement |
| Travail isolé | Impact négatif réel : 41 accidents avec arrêt, 23 agressions ; 40 % des postes isolés sans alarme | Risque : coûts des accidents, mise en cause de la société ; opportunité : équiper tous les postes |
| Rotation (449 départs) | Impact sur la stabilité de l'emploi des agents | Risque : 449 × 2 900 = **1 302 100 €** de recrutement et de formation, perte de clients (changement fréquent des agents) ; opportunité : fidélisation et formation, atout dans les appels d'offres |
| Sous-traitance (9 % des heures) | Impact négatif réel sur les **travailleurs des sous-traitants** (durées excessives, heures de nuit non majorées), dans la chaîne de valeur | Risque de réputation et de perte de marchés, notamment auprès de l'établissement public (critère de 20 %) |
| Véhicules de ronde | Impact négatif : émissions et nuisances des 74 véhicules diesel pour les riverains ; impact positif : baisse des intrusions et des dégradations dans une zone d'activités | Risque : hausse du carburant (+ 9 %), exigences des appels d'offres ; opportunité : flotte électrique (coûts, accès aux marchés) |

Un même enjeu peut être matériel des deux points de vue, l'impact étant souvent la source du risque [V ESRS 1 (2026) § 36, § 48].

**Parties prenantes affectées et utilisateurs (1 pt)**
- **Parties prenantes affectées (0,75 pt)** : celles dont les intérêts sont ou peuvent être touchés par les activités de l'entreprise : les **agents** et autres salariés de VEILLANE, y compris en contrats courts ; les **travailleurs des sous-traitants**, dans la chaîne de valeur ; les **riverains** des sites et des parcours de ronde, communautés affectées ; les **clients** et les personnes présentes sur les sites surveillés, utilisateurs du service ; la nature peut être regardée comme une partie prenante silencieuse. Une **attention particulière** est due aux plus **vulnérables** : agents isolés la nuit, salariés des sous-traitants [V ESRS 1 (2026) AR 23 ; S, application].
- **Utilisateurs (0,25 pt)** : les utilisateurs de l'état de durabilité sont les investisseurs, prêteurs et créanciers (le fonds VIRELLE Capital Développement) et les autres utilisateurs, partenaires commerciaux (l'établissement public, comme donneur d'ordre), partenaires sociaux, société civile [V ESRS 1 (2026) § 4]. Un même acteur peut être les deux (un syndicat peut représenter les agents) [V § 42] ; mais l'intérêt du fonds pour les seuls risques ne réduit pas la place des parties affectées dans l'évaluation des impacts.

**Réponses tolérées**
- D'autres impacts, risques ou opportunités tirés du contexte (fatigue au volant lors des rondes de nuit, sécurité des sites clients), s'ils sont correctement qualifiés.
- Le classement des clients parmi les utilisateurs seulement, si les personnes présentes sur les sites sont retenues parmi les parties affectées.

**Erreurs fréquentes**
- Confondre parties prenantes affectées et utilisateurs, ou ne retenir que les risques financiers (`JUR-A01`).
- Conduire l'analyse de double matérialité (seuils, notation), ce qui n'est pas demandé (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| ESRS 1 (2026) § 4, § 36, § 39-42, § 47-48, AR 23 | Impacts ; risques et opportunités ; dépendances ; utilisateurs ; parties prenantes affectées | [V] ; application : [S] | F12 § 2, § 6, § 18 |

### 3.11 Mission du cabinet, démarche et procédures (4 pts)

**a. Objectifs, axes et assurance limitée (2 pts)**
- **Objectifs (0,75 pt)** : le cabinet émet un **avis** sur la conformité aux ESRS du **processus** mis en œuvre par VEILLANE pour déterminer les informations publiées (analyse de double matérialité) et sur la conformité des **informations** publiées [V L. 821-54 II, applicable par analogie ; LD 2026 § 2]. La mission est volontaire, conduite dans les conditions de la certification légale (hypothèse), confiée par l'assemblée générale ; le rapport lui est destiné. Elle est distincte de la certification des comptes et ne garantit ni la viabilité ni la qualité de la gestion [V L. 821-55 ; LD 2026 § 2].
- **Axes (0,5 pt)** : **axe 1**, le processus, et **axe 2**, les informations, s'appliquent ; l'axe relatif aux informations de la **taxonomie** est sans objet, VEILLANE n'y étant pas tenue et n'en publiant pas ; l'axe relatif au **balisage** l'est aussi, faute de règles applicables [V LD 2026 § 2, § 10 ; S, application à une mission volontaire]. La consultation du comité social et économique n'entre pas dans la mission (lettre de mission).
- **Assurance limitée (0,75 pt)** : les vérifications sont moindres, en **nature**, en **étendue** et en **durée**, que pour une assurance raisonnable ; la conclusion est exprimée sous une **forme négative** : le cabinet n'a pas relevé d'erreurs, d'omissions ou d'incohérences importantes [V LD 2026, « Niveau d'assurance »]. Elle ne garantit pas chaque donnée ; la direction reste responsable des informations publiées [S].

**b. Étapes et procédures (2 pts)**
- **Étapes (0,75 pt)** : lettre de mission ; **prise de connaissance** de l'entité (sites, agents, sous-traitants, flotte) et des systèmes qui produisent les données (logiciel de planification, plan de formation, paie) ; **planification**, avec la sélection des informations **vérifiées spécifiquement**, celles qui présentent un risque important de non-conformité ou de fortes attentes des utilisateurs : ici la rotation et la formation, suivies par l'établissement public et liées à un marché ; **contrôle du processus** (axe 1, achevé sans anomalie) ; **contrôle des informations** (axe 2) ; lecture d'ensemble et cohérence avec les comptes, avec des échanges avec l'équipe d'audit des comptes ; communication à la direction et déclarations écrites ; **rapport** d'assurance limitée par axe [V LD 2026 § 3-8, § 11-14, § 17 ; F13 § 3].
- **Procédures (1,25 pt ; 0,25 pt par procédure justifiée par son objectif, dans la limite de 0,75 pt par donnée)** :
  - *Taux de rotation* : **lecture de la définition** et comparaison avec celle de 2025 (comparabilité) ; **rapprochement** des 449 départs avec les DSN, le registre du personnel et les soldes de tout compte comptabilisés, en lien avec l'équipe d'audit des comptes (exhaustivité, exactitude) ; contrôle, sur un échantillon, que les fins de contrats courts sont exclues et que le dénominateur (1 320 agents) concorde avec l'effectif de l'annexe 3.1 ; **recalcul** : 449 / 1 320 = 34,0 % [V LD 2026 § 8.3.2].
  - *Heures de formation par agent* : **rapprochement** du plan de formation avec les feuilles de présence signées et les factures des organismes de formation (réalité, rattachement à l'exercice) ; contrôle de la **cohérence de méthode** avec 2025, établi sur les feuilles de présence (comparabilité) ; rapprochement avec les charges de formation comptabilisées ; procédure analytique par site et par type de formation ; **recalcul** après exclusion des sessions non suivies [V LD 2026 § 8.3.2 ; ESRS 1 (2026) § 19-20].

**Réponses tolérées**
- En b., une présentation des étapes dans l'ordre du programme (prise de connaissance, planification, contrôle de la conformité des informations et du processus, contrôle du balisage, contrôle des exigences de publication, rapport) : points complets.

**Erreurs fréquentes**
- Retenir les axes relatifs à la taxonomie et au balisage pour une entreprise qui n'y est pas tenue, ou présenter l'assurance limitée comme une garantie (`JUR-A05`, `JUR-A01`).
- Proposer des procédures sans lien avec les deux données ni objectif (`JUR-A06`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| C. com. L. 821-54 II, L. 821-55 ; LD 2026 § 2, § 10, « Niveau d'assurance » | Objectifs ; axes ; assurance limitée | [V] ; application à une mission volontaire : [S] | F13 § 2 ; F12 § 11 |
| LD 2026 § 3-8, § 8.3.1-8.3.2, § 11-14, § 17 | Étapes ; informations vérifiées spécifiquement ; techniques | [V] ; procédures : [S] | F13 § 3, § 7 |

### 3.12 Avis sur les informations et comparaison avec l'opinion sur les comptes (2 pts)

- **La direction corrige (0,5 pt)** : 28 250 − 6 480 = 21 770 heures, soit 21 770 / 1 320 = **16,5 heures** par agent, en hausse de **11,5 %** sur les 14,8 heures de 2025, et non de 44,6 %. Le processus étant conforme et les travaux sur la rotation s'étant achevés sans anomalie (annexe 3.11) : **avis de conformité** sur les deux axes [V LD 2026 § 17]. Le cabinet peut formuler une **observation** renvoyant à la note méthodologique, si elle décrit le passage du plan de formation aux feuilles de présence [V LD 2026 § 17 ; F13 § 4.4].
- **La direction ne corrige pas (0,75 pt)** : 21,4 heures au lieu de 16,5, soit une surévaluation de 29,7 %, et une hausse affichée de 44,6 % au lieu de 11,5 %, sur une donnée sociale suivie par un client qui en fait un critère de choix : les heures prévues ne sont pas des heures suivies, et l'information n'est ni **fidèle** ni **neutre** [V ESRS 1 (2026) § 19-20]. C'est une erreur non corrigée d'une importance telle qu'elle remet en cause la conformité des informations ; elle porte sur une donnée identifiée et chiffrable : incidences **clairement circonscrites**, réserve suffisante si elle donne le chiffre exact : **avis de conformité assorti d'une réserve motivée** sur les informations (axe 2) ; l'avis sur le processus (axe 1) reste un avis de conformité [V LD 2026 § 17 ; F13 § 4.3 ; S, qualification]. Ni non-conformité, l'erreur ne privant pas de sens l'ensemble de l'état, ni impossibilité, aucune limitation n'ayant empêché les vérifications.
- **Différences avec l'opinion sur les comptes (0,75 pt ; 0,25 pt par différence, dans la limite de 0,75 pt)** :
  - **assurance** : limitée, conclusion sous une forme négative (« nous n'avons pas relevé… »), contre une assurance raisonnable exprimée sous une forme positive (« nous certifions que les comptes sont réguliers et sincères et donnent une image fidèle ») [V LD 2026, « Niveau d'assurance » ; NEP principes § 08 ; NEP rapport § 08] ;
  - **objet et référentiel** : conformité aux ESRS d'un processus et d'informations largement qualitatives et prospectives, contre la régularité, la sincérité et l'image fidèle des comptes au regard du plan comptable général [V L. 821-54 II ; L. 821-53] ;
  - **structure** : un avis **par axe** (processus, informations), avec d'éventuelles observations et des éléments ayant fait l'objet d'une attention particulière, contre une opinion unique sur les comptes pris dans leur ensemble, avec la justification des appréciations [V LD 2026 § 17 ; NEP rapport § 18] ;
  - **vocabulaire des conclusions** : avis de conformité, avec réserve, de non-conformité, impossibilité d'émettre un avis, contre certification sans réserve, avec réserve, refus et impossibilité de certifier [V LD 2026 § 17 ; R. 821-180] ;
  - **cadre normatif** : lignes directrices de la H2A, dans l'attente d'une norme d'assurance européenne, contre des NEP homologuées [V F13 § 2.4 ; L. 821-11 I].
  Les deux rapports sont destinés à l'assemblée générale et signés par Mme VAUCHELLE.

**Réponses tolérées**
- Un avis de non-conformité dans le second cas, si le candidat motive l'impossibilité de circonscrire l'erreur par la place de la formation dans les informations sociales : 0,5 pt sur 0,75.

**Erreurs fréquentes**
- Remplacer la réserve par une observation, ou appliquer à l'avis le vocabulaire de la certification des comptes (`JUR-A02`).

**Références**

| Référence | Contenu mobilisé | Statut | Fiche |
|---|---|---|---|
| LD 2026 § 17, « Niveau d'assurance » | Avis, réserve, non-conformité, observations, structure par axe ; forme négative | [V] ; qualification : [S] | F13 § 2.3, § 4.1-4.4 |
| ESRS 1 (2026) § 19-20 | Représentation fidèle, neutralité | [V] | F12 § 17 |
| C. com. L. 821-11 I, L. 821-53, L. 821-54 II ; NEP principes § 08 ; NEP rapport § 08, § 18 ; R. 821-180 | Certification des comptes ; opinion ; structure du rapport | [V] | F11 § 1.1, § 8 |
